#!/usr/bin/env python3
"""
piloto_metricas.py — medidas del piloto de la combinación A (HACS-ODLC).

Calcula, desde los artefactos con frontmatter YAML del repo del MVP, las
medidas pre-registradas en docs/06_fundacional/Piloto - Combinación A.md:
la Fase 0 (validación del problema por entrevistas), las medidas primarias
(P1 outcome validado, P2 trabajo descartado), el contraste de revisión contra
el mejor componente solo, las métricas de pasividad, la siembra de defectos y
los criterios de abandono.

Read-only, determinista y sin dependencias (solo stdlib): no consulta el reloj
ni la red; toda fecha de corte sale del protocolo. No usa git: la verificación
del sello compara el SHA-256 de protocolo.md contra el archivo de sello y la
cadena de desvíos declarados.

Estructura esperada del directorio de datos (subdirectorios opcionales salvo
protocolo.md y protocolo.sha256):

  protocolo.md            frontmatter con diseño, calendario y umbrales
  protocolo.sha256        sello: hash del protocolo al momento de congelarlo
  desvios/*.md            desvíos declarados (hash_anterior -> hash_nuevo)
  fase0/entrevistas/*.md  registro por entrevista (codificación del entrevistador)
  fase0/codificacion/*.md codificación ciega: una por entrevista del agente
                          (agente_ciego) y, aparte, la recodificación humana
                          (persona_ciega); nunca dos del mismo tipo
  unidades/*.md           unidad de trabajo (ítem sin método, objetivo con método)
  decisiones/*.md         decisión o revisión humana / del agente
  validaciones/*.md       evidencia de outcome por unidad
  aprendizajes/*.md       entradas de la Fase 6
  registro-ia/*.md        modelo + versión + configuración + hash del prompt
  semanas/*.md            bloques activos de 15 min y costo por semana
  siembra/manifiesto.md   defectos sembrados (se revela al cierre)
  siembra.sha256          hash del manifiesto comprometido al inicio

Otros subdirectorios (p. ej. plantillas/, caso-abandono/) se ignoran.

Uso:
  python3 scripts/piloto_metricas.py <directorio-de-datos>

Exit codes: 0 = sin criterios de abandono activos
            1 = al menos un criterio de abandono activo
            2 = error (datos ilegibles, sello roto, protocolo inválido o con
                claves desconocidas, codificación duplicada, más entrevistas
                de las previstas en la Fase 0)
"""
import hashlib
import itertools
import math
import os
import re
import statistics
import sys
from datetime import date, datetime


class DatosInvalidos(Exception):
    pass


# --------------------------------------------------------------------------
# Subconjunto de YAML suficiente para las plantillas (sin pyyaml)
# --------------------------------------------------------------------------

def _strip_comment(line):
    out, quote = [], None
    for i, ch in enumerate(line):
        if quote:
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch == "#" and (i == 0 or line[i - 1] in " \t"):
            break
        out.append(ch)
    return "".join(out).rstrip()


def _scalar(txt):
    t = txt.strip()
    if t in ("", "~", "null"):
        return None
    if t in ("true", "false"):
        return t == "true"
    if len(t) >= 2 and t[0] == t[-1] and t[0] in "\"'":
        return t[1:-1]
    if t.startswith("[") and t.endswith("]"):
        inner = t[1:-1].strip()
        if not inner:
            return []
        parts, buf, quote = [], [], None
        for ch in inner:
            if quote:
                buf.append(ch)
                if ch == quote:
                    quote = None
            elif ch in "\"'":
                quote = ch
                buf.append(ch)
            elif ch == ",":
                parts.append("".join(buf))
                buf = []
            else:
                buf.append(ch)
        parts.append("".join(buf))
        return [_scalar(p) for p in parts]
    if re.fullmatch(r"-?\d+", t):
        return int(t)
    if re.fullmatch(r"-?\d+\.\d+", t):
        return float(t)
    return t


def _parse_block(lines, start, indent):
    """Parsea un bloque (mapping o lista) con indentación `indent`."""
    i = start
    if i < len(lines) and lines[i][1].startswith("- "):
        res = []
        while i < len(lines) and lines[i][0] == indent and lines[i][1].startswith("- "):
            res.append(_scalar(lines[i][1][2:]))
            i += 1
        return res, i
    res = {}
    while i < len(lines) and lines[i][0] == indent:
        txt = lines[i][1]
        m = re.match(r"^([^:]+?):(?:\s+(.*))?$", txt)
        if not m:
            raise DatosInvalidos(f"línea YAML no soportada: {txt!r}")
        key, val = m.group(1).strip(), m.group(2)
        i += 1
        if val is None or val == "":
            if i < len(lines) and lines[i][0] > indent:
                child, i = _parse_block(lines, i, lines[i][0])
                res[key] = child
            else:
                res[key] = None
        else:
            res[key] = _scalar(val)
    return res, i


def parse_yaml(text):
    lines = []
    for raw in text.splitlines():
        s = _strip_comment(raw)
        if not s.strip():
            continue
        indent = len(s) - len(s.lstrip(" "))
        lines.append((indent, s.strip()))
    if not lines:
        return {}
    data, i = _parse_block(lines, 0, lines[0][0])
    if i != len(lines):
        raise DatosInvalidos(f"indentación inconsistente cerca de {lines[i][1]!r}")
    return data


def read_frontmatter(path):
    raw = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---[ \t]*(?:\n|$)", raw, flags=re.S)
    if not m:
        raise DatosInvalidos(f"{path}: sin frontmatter delimitado por ---")
    try:
        fm = parse_yaml(m.group(1))
    except DatosInvalidos as e:
        raise DatosInvalidos(f"{path}: {e}")
    fm["_archivo"] = os.path.basename(path)
    fm["_cuerpo"] = raw[m.end():]
    return fm


def load_dir(base, sub):
    d = os.path.join(base, sub)
    if not os.path.isdir(d):
        return []
    return [read_frontmatter(os.path.join(d, f)) for f in sorted(os.listdir(d)) if f.endswith(".md")]


def sha256_file(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


# --------------------------------------------------------------------------
# Utilidades numéricas
# --------------------------------------------------------------------------

def ts(v):
    if v is None or v == "":
        return None
    try:
        return datetime.fromisoformat(str(v))
    except ValueError:
        raise DatosInvalidos(f"timestamp inválido: {v!r}")


def mean(xs):
    return sum(xs) / len(xs) if xs else None


def median(xs):
    return statistics.median(xs) if xs else None


def nap(a, b, mayor_es_mejor=True):
    """Nonoverlap of All Pairs (Parker y Vannest 2009): proporción de pares
    (a, b) en que la observación de B mejora a la de A; empates valen 1/2."""
    if not a or not b:
        return None
    s = 0.0
    for x in a:
        for y in b:
            if y == x:
                s += 0.5
            elif (y > x) == mayor_es_mejor:
                s += 1
    return s / (len(a) * len(b))


def wilson(k, n, z=1.96):
    if n == 0:
        return (None, None)
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (max(0.0, c - h), min(1.0, c + h))


def kappa(pares):
    """Kappa de Cohen para codificación binaria. pares = [(a, b), ...]."""
    n = len(pares)
    if n == 0:
        return None, None
    po = sum(1 for a, b in pares if a == b) / n
    pa = sum(a for a, _ in pares) / n
    pb = sum(b for _, b in pares) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    if pe == 1:
        return None, po
    return (po - pe) / (1 - pe), po


def fmt(v, nd=2):
    if v is None:
        return "s/d"
    if isinstance(v, float):
        return f"{v:.{nd}f}"
    return str(v)


# --------------------------------------------------------------------------
# Sello y desvíos
# --------------------------------------------------------------------------

def verificar_sello(base, salida):
    prot = os.path.join(base, "protocolo.md")
    sello = os.path.join(base, "protocolo.sha256")
    if not os.path.isfile(prot) or not os.path.isfile(sello):
        raise DatosInvalidos("faltan protocolo.md o protocolo.sha256")
    actual = sha256_file(prot)
    sellado = open(sello, encoding="utf-8").read().split()[0].strip()
    desvios = sorted(load_dir(base, "desvios"), key=lambda d: (str(d.get("fecha")), d["_archivo"]))
    cadena = sellado
    for d in desvios:
        if d.get("hash_anterior") != cadena:
            raise DatosInvalidos(
                f"desvío {d['_archivo']} no encadena: hash_anterior {d.get('hash_anterior')} != {cadena}")
        cadena = d.get("hash_nuevo")
    if cadena != actual:
        raise DatosInvalidos(
            f"sello roto: protocolo.md tiene sha256 {actual} y la cadena sello+desvíos termina en {cadena}")
    salida.append(f"Sello: OK ({sellado[:12]}…, {len(desvios)} desvío(s) declarado(s))")
    for d in desvios:
        salida.append(f"  - desvío {d.get('fecha')}: {d.get('motivo')}")


# --------------------------------------------------------------------------
# Fase 0
# --------------------------------------------------------------------------

# Claves exactas de umbrales.fase0 (P-05 y P-10). Una clave faltante o
# desconocida es un error: una clave vieja o mal escrita no puede caer en
# silencio a un valor por defecto.
CLAVES_FASE0 = (
    "entrevistas_fijas",              # tramo 1: las primeras N por fecha (P-05)
    "extension",                      # entrevistas que se suman una sola vez si el tramo 1 es ambiguo
    "kappa_min",
    "confirma_dolor_casos",           # umbrales del tramo 1 (P-05)
    "confirma_compromiso_casos",
    "descarta_dolor_casos",
    "extension_confirma_dolor_casos",         # umbrales propios del tramo 2 (P-10)
    "extension_confirma_compromiso_casos",
    "extension_descarta_dolor_casos",
)
CODIFICADORES = ("agente_ciego", "persona_ciega")
SENALES_COMPROMISO = ("tiempo", "dinero", "solucion_casera")  # libro de códigos (P-10)


def _regla(dolor, comp, k, umb, pre, kappa_min):
    if k is None or k < kappa_min:
        return "ambiguo", True
    if dolor >= umb[f"{pre}confirma_dolor_casos"] and comp >= umb[f"{pre}confirma_compromiso_casos"]:
        return "confirmado", False
    if dolor <= umb[f"{pre}descarta_dolor_casos"]:
        return "descartado", False
    return "ambiguo", False


def fase0(base, prot, salida, kills, alertas):
    u = prot["umbrales"]["fase0"]
    entrevistas = load_dir(base, "fase0/entrevistas")
    if not entrevistas:
        salida.append("Fase 0: sin entrevistas registradas")
        return None
    temas = prot.get("fase0_temas") or []
    centrales = prot.get("fase0_temas_centrales") or temas
    perfiles = set(prot.get("fase0_perfiles") or [])

    ids = set()
    for e in entrevistas:
        if e.get("id") in ids:
            raise DatosInvalidos(f"{e['_archivo']}: id de entrevista repetido {e.get('id')!r}")
        ids.add(e.get("id"))
        if not e.get("fecha"):
            raise DatosInvalidos(f"{e['_archivo']}: falta fecha (el tramo 1 se arma por fecha, P-10)")
        for s in e.get("senales_compromiso") or []:
            if s not in SENALES_COMPROMISO:
                raise DatosInvalidos(f"{e['_archivo']}: señal de compromiso {s!r} fuera del libro de códigos "
                                     f"({', '.join(SENALES_COMPROMISO)})")

    # Una codificación por entrevista y por tipo de codificador (P-10): la
    # recodificación humana se guarda aparte y no pisa la del agente.
    cods = {c: {} for c in CODIFICADORES}
    for c in load_dir(base, "fase0/codificacion"):
        quien, eid = c.get("codificador"), c.get("entrevista")
        if quien not in CODIFICADORES:
            raise DatosInvalidos(f"{c['_archivo']}: codificador {quien!r} (debe ser {' o '.join(CODIFICADORES)})")
        if eid not in ids:
            raise DatosInvalidos(f"{c['_archivo']}: codifica la entrevista {eid!r}, que no está registrada")
        if eid in cods[quien]:
            raise DatosInvalidos(f"{c['_archivo']}: segunda codificación {quien} de {eid} "
                                 f"(la otra es {cods[quien][eid]['_archivo']})")
        cods[quien][eid] = c
    ciego = cods["agente_ciego"]

    validas = sorted((e for e in entrevistas if not perfiles or e.get("perfil") in perfiles),
                     key=lambda e: (str(e.get("fecha")), str(e.get("id"))))
    fuera = len(entrevistas) - len(validas)
    n1, n_ext = int(u["entrevistas_fijas"]), int(u["extension"])
    n2 = n1 + n_ext
    kappa_min = u["kappa_min"]

    def evaluar(tramo):
        pares_dolor, pares_comp = [], []
        dolor, comp, inducidas, sin_cod = 0, 0, 0, 0
        for e in tramo:
            dm = e.get("dolor_mencionado") or {}
            if any(v == "inducido" for v in dm.values()):
                inducidas += 1
            c = ciego.get(e.get("id"))
            if c is None:
                sin_cod += 1
                continue
            cd = c.get("dolor") or {}
            for t in temas:
                pares_dolor.append((1 if dm.get(t) == "espontaneo" else 0, 1 if cd.get(t) == "si" else 0))
            b_c = 1 if c.get("compromiso") == "si" else 0
            pares_comp.append((1 if (e.get("senales_compromiso") or []) else 0, b_c))
            # dolor = codificación ciega "si" en un tema central que el entrevistador no indujo (P-10)
            if any(cd.get(t) == "si" and dm.get(t) != "inducido" for t in centrales):
                dolor += 1
            comp += b_c
        return pares_dolor, pares_comp, dolor, comp, inducidas, sin_cod

    salida.append(f"Fase 0: {len(entrevistas)} entrevistas, {len(validas)} con perfil válido "
                  f"({fuera} fuera de perfil); tramo 1 = primeras {n1} por fecha, extensión única de {n_ext}")

    def reportar(nombre, tramo, pre):
        pd, pc, dolor, comp, ind, sin_cod = evaluar(tramo)
        k_d, po_d = kappa(pd)
        k_c, po_c = kappa(pc)
        n = len(tramo)
        salida.append(f"  {nombre} ({n} entrevistas, {tramo[0].get('fecha')} a {tramo[-1].get('fecha')}): "
                      f"{sin_cod} sin codificación ciega, {ind} con algún tema inducido por el entrevistador")
        salida.append(f"    acuerdo entrevistador vs. agente ciego — dolor: kappa {fmt(k_d)} "
                      f"(acuerdo {fmt(po_d)}); compromiso: kappa {fmt(k_c)} (acuerdo {fmt(po_c)})")
        if sin_cod:
            salida.append(f"    faltan codificaciones ciegas: {nombre} en curso")
            return "en_curso"
        umb = (f"confirma con dolor ≥ {u[pre + 'confirma_dolor_casos']} y compromiso ≥ "
               f"{u[pre + 'confirma_compromiso_casos']}; descarta con dolor ≤ {u[pre + 'descarta_dolor_casos']}")
        salida.append(f"    según el agente ciego: dolor central no inducido en {dolor} de {n} entrevistas, "
                      f"compromiso en {comp} de {n} ({umb})")
        res, por_kappa = _regla(dolor, comp, k_d, u, pre, kappa_min)
        if por_kappa:
            salida.append(f"    acuerdo insuficiente (kappa de dolor < {kappa_min} o indefinido): "
                          "revisar el libro de códigos y recodificar")
        salida.append(f"    veredicto del {nombre}: {res.upper()}")
        return res

    if len(validas) < n1:
        salida.append(f"  tramo 1 incompleto: {len(validas)} de {n1} entrevistas con perfil válido")
        res = "en_curso"
    else:
        res = reportar("tramo 1", validas[:n1], "")
        if res in ("confirmado", "descartado") and len(validas) > n1:
            raise DatosInvalidos(f"Fase 0: el tramo 1 dio {res.upper()} y quedó congelado, pero hay "
                                 f"{len(validas)} entrevistas con perfil válido (previstas {n1}, P-10)")
        if res == "ambiguo":
            if len(validas) > n2:
                raise DatosInvalidos(f"Fase 0: hay {len(validas)} entrevistas con perfil válido y la extensión "
                                     f"admite como máximo {n2} (P-10)")
            if len(validas) < n2:
                salida.append(f"  extensión en curso: {len(validas)} de {n2} entrevistas con perfil válido")
                res = "en_curso"
            else:
                res = reportar("tramo 2", validas[:n2], "extension_")
                if res == "ambiguo":
                    res = "descartado"
                    salida.append("    sigue ambiguo después de la extensión pre-registrada: cuenta como descartado")

    # Recodificación humana (P-06, P-10): se informa aparte, no decide.
    persona = cods["persona_ciega"]
    if persona:
        pd, pc = [], []
        for eid, cp in sorted(persona.items()):
            ca = ciego.get(eid)
            if ca is None:
                alertas.append(f"recodificación humana de {eid} sin codificación del agente para comparar")
                continue
            da, dp = ca.get("dolor") or {}, cp.get("dolor") or {}
            for t in temas:
                pd.append((1 if da.get(t) == "si" else 0, 1 if dp.get(t) == "si" else 0))
            pc.append((1 if ca.get("compromiso") == "si" else 0, 1 if cp.get("compromiso") == "si" else 0))
        k_p, po_p = kappa(pd)
        k_pc, po_pc = kappa(pc)
        salida.append(f"  recodificación humana (persona ciega) de {len(persona)} entrevistas, contra el agente: "
                      f"dolor kappa {fmt(k_p)} (acuerdo {fmt(po_p)}); compromiso kappa {fmt(k_pc)} "
                      f"(acuerdo {fmt(po_pc)}); no entra en el veredicto")
        if k_p is None or k_p < kappa_min:
            alertas.append(f"acuerdo agente vs. persona ciega en dolor por debajo de {kappa_min} o indefinido: "
                           "el agente codificador no queda verificado")
    else:
        salida.append("  recodificación humana (persona ciega): sin registros")

    salida.append(f"  resultado Fase 0: {res.upper()}")
    if res == "descartado":
        kills.append("K0 Fase 0: el problema no se confirma; el piloto no arranca")
    return res


# --------------------------------------------------------------------------
# Piloto
# --------------------------------------------------------------------------

def semana_de(dt, inicio):
    return (dt.date() - inicio).days // 7 + 1


def periodo_de(dt, inicio, ppw):
    """Período de medición (1-indexado): la semana partida en `ppw` tramos."""
    dias = (dt - datetime.combine(inicio, datetime.min.time(), dt.tzinfo)).total_seconds() / 86400
    return int(dias * ppw // 7) + 1


def condicion_unidad(u, prot, inicio, inicios_tier, ppw):
    w = periodo_de(ts(u["creada_en"]), inicio, ppw)
    if prot["diseno"] == "abab":
        for f in prot["fases_abab"]:
            d, h, c = f.split("-") if isinstance(f, str) else f
            if int(d) <= w <= int(h):
                return w, c
        return w, None
    s = inicios_tier.get(u.get("tier"))
    if s is None:
        raise DatosInvalidos(f"{u['_archivo']}: tier {u.get('tier')!r} fuera del protocolo")
    return w, ("B" if w >= s else "A")


def asignaciones_posibles(tiers, ventanas):
    slots = sorted(ventanas, key=lambda k: int(k))
    for orden in itertools.permutations(tiers):
        for starts in itertools.product(*[ventanas[s] for s in slots]):
            yield dict(zip(orden, starts))


def piloto(base, prot, salida, kills, alertas):
    inicio = date.fromisoformat(str(prot["inicio"]))
    ppw = int(prot.get("periodos_por_semana", 1))
    N = int(prot["semanas"]) * ppw
    corte = ts(prot["fecha_corte"])
    cerrado = prot.get("estado") == "cerrado"
    u = prot.get("umbrales", {})
    tiers = prot.get("tiers") or []
    inicios_tier = {}
    if prot["diseno"] == "linea_base_multiple":
        asig = prot["asignacion"]
        inicios_tier = {t: int(s) for t, s in asig.items()}
    unidades = load_dir(base, "unidades")
    if not unidades:
        salida.append("Piloto: sin unidades registradas")
        return
    vals = load_dir(base, "validaciones")
    decs = load_dir(base, "decisiones")
    aprs = load_dir(base, "aprendizajes")
    regs = load_dir(base, "registro-ia")
    sems = load_dir(base, "semanas")

    salida.append("")
    salida.append(f"Piloto: diseño {prot['diseno']}, {prot['semanas']} semanas ({N} períodos de medición) "
                  f"desde {inicio}, corte {corte.date()}"
                  f"{'' if cerrado else ' (PROVISORIO: protocolo no cerrado)'}")
    if inicios_tier:
        salida.append("  inicio del método por tipo de objetivo: " +
                      ", ".join(f"{t}=período {s}" for t, s in sorted(inicios_tier.items(), key=lambda x: x[1])))

    nivel_min = u.get("nivel_outcome_min", 2)
    ventana = u.get("ventana_outcome_dias", 28)
    por_unidad = {}
    for v in vals:
        por_unidad.setdefault(v.get("unidad"), []).append(v)
        if v.get("fuente") == "simulada" and (v.get("nivel_evidencia") or 0) > 0:
            alertas.append(f"{v['_archivo']}: evidencia de usuarios simulados con nivel > 0; "
                           "se cuenta como nivel 0 (filtra, no valida)")

    def nivel(v):
        return 0 if v.get("fuente") == "simulada" else (v.get("nivel_evidencia") or 0)

    def validada(un):
        ent = ts(un.get("entregada_en"))
        if ent is None:
            return False, False
        pendiente = (corte - ent).days < ventana
        for v in por_unidad.get(un["id"], []):
            ev = ts(v.get("evidencia_en"))
            if ev and nivel(v) >= nivel_min and 0 <= (ev - ent).days <= ventana:
                return True, False
        return False, pendiente

    filas = []
    for un in unidades:
        w, c = condicion_unidad(un, prot, inicio, inicios_tier, ppw)
        ok, pend = validada(un)
        pago = any(nivel(v) >= 3 for v in por_unidad.get(un["id"], []))
        filas.append({"u": un, "w": w, "c": c, "t": un.get("tier"), "valid": ok, "pend": pend, "pago": pago,
                      "sem": semana_de(ts(un["creada_en"]), inicio),
                      "desc": un.get("estado") == "descartada",
                      "aband": un.get("estado") == "abandonada",
                      "entregada": un.get("estado") in ("entregada", "descartada") and un.get("entregada_en")})

    # --- P1 y P2 por fase -------------------------------------------------
    salida.append("")
    salida.append("Medidas primarias")
    for c in ("A", "B"):
        fs = [f for f in filas if f["c"] == c]
        ent = [f for f in fs if f["entregada"]]
        nv = sum(f["valid"] for f in fs)
        nd = sum(f["desc"] for f in fs)
        npend = sum(f["pend"] and not f["valid"] for f in fs)
        npago = sum(f["pago"] for f in fs)
        salida.append(f"  fase {c}: {len(fs)} unidades, {len(ent)} entregadas; "
                      f"P1 outcome validado (nivel ≥ {nivel_min} en ≤ {ventana} d): {nv} "
                      f"(tasa {fmt(nv / len(ent) if ent else None)}; {npend} con ventana abierta; "
                      f"{npago} con compromiso de pago); "
                      f"P2 descartadas después de entregar: {nd} (tasa {fmt(nd / len(fs) if fs else None)})")
    tasa = {}
    for c in ("A", "B"):
        fs = [f for f in filas if f["c"] == c]
        tasa[c] = (sum(f["desc"] for f in fs) / len(fs)) if fs else None
    salida.append("  secundaria (Camuffo): abandono antes de entregar")
    for c in ("A", "B"):
        fs = [f for f in filas if f["c"] == c]
        dias = [(ts(f["u"]["descartada_en"]) - ts(f["u"]["creada_en"])).total_seconds() / 86400
                for f in fs if f["aband"] and f["u"].get("descartada_en")]
        salida.append(f"    fase {c}: {sum(f['aband'] for f in fs)} abandonadas de {len(fs)}; "
                      f"mediana de días hasta abandonar {fmt(median(dias), 1)}")

    # --- K4: piloto no informativo, con corte parcial en la semana 8 (P-09) --
    sem_k4 = int(u["k4_semana"])
    if semana_de(corte, inicio) <= sem_k4:
        salida.append(f"  K4 (corte parcial en la semana {sem_k4}): pendiente, la fecha de corte no llega a esa semana")
    else:
        hasta_k4 = {"A": 0, "B": 0}
        for f in filas:
            if f["c"] not in hasta_k4:
                continue
            for v in por_unidad.get(f["u"]["id"], []):
                ev = ts(v.get("evidencia_en"))
                if ev and nivel(v) >= nivel_min and semana_de(ev, inicio) <= sem_k4:
                    hasta_k4[f["c"]] += 1
        salida.append(f"  K4 (corte parcial en la semana {sem_k4}): validaciones de nivel ≥ {nivel_min} "
                      f"hasta esa semana: fase A {hasta_k4['A']}, fase B {hasta_k4['B']}")
        if not any(hasta_k4.values()):
            kills.append(f"K4 piloto no informativo: ninguna validación de nivel ≥ {nivel_min} en la fase A "
                         f"ni en la B al llegar a la semana {sem_k4}")

    # --- series semanales por tier, NAP y prueba de aleatorización --------
    series_p1 = {t: [0] * N for t in tiers}
    series_p2 = {t: [0] * N for t in tiers}
    for f in filas:
        if 1 <= f["w"] <= N and f["t"] in series_p1:
            series_p1[f["t"]][f["w"] - 1] += int(f["valid"])
            series_p2[f["t"]][f["w"] - 1] += int(f["desc"])

    naps_p1, naps_p2, p_valor = {}, {}, None
    if prot["diseno"] == "linea_base_multiple":
        for t in tiers:
            s = inicios_tier[t]
            a1, b1 = series_p1[t][:s - 1], series_p1[t][s - 1:]
            a2, b2 = series_p2[t][:s - 1], series_p2[t][s - 1:]
            naps_p1[t] = nap(a1, b1, True)
            naps_p2[t] = nap(a2, b2, False)
            salida.append(f"  {t}: P1 por período {series_p1[t]} | NAP P1 {fmt(naps_p1[t])} | "
                          f"P2 por período {series_p2[t]} | NAP P2 {fmt(naps_p2[t])}")

        def stat(asg):
            difs = []
            for t in tiers:
                s = asg[t]
                difs.append(mean(series_p1[t][s - 1:]) - mean(series_p1[t][:s - 1]))
            return mean(difs)

        obs = stat(inicios_tier)
        todas = list(asignaciones_posibles(tiers, prot["ventanas"]))
        if inicios_tier not in todas:
            raise DatosInvalidos("la asignación sellada no está entre las permitidas por las ventanas")
        ge = sum(1 for a in todas if stat(a) >= obs - 1e-12)
        p_valor = ge / len(todas)
        salida.append(f"  prueba de aleatorización (P1, diferencia media B−A): observado {fmt(obs, 3)}, "
                      f"p = {ge}/{len(todas)} = {fmt(p_valor, 3)}")
        # filtración: ¿se movió la línea de base de los tiers todavía sin método?
        for t in tiers:
            otros = [s for x, s in inicios_tier.items() if x != t and s < inicios_tier[t]]
            if otros:
                k = min(otros)
                antes = series_p1[t][:k - 1]
                despues = series_p1[t][k - 1:inicios_tier[t] - 1]
                if antes and despues and mean(despues) > mean(antes) + 1e-9:
                    alertas.append(f"línea de base de '{t}' sube antes de su inicio "
                                   f"({fmt(mean(antes))} → {fmt(mean(despues))}): posible filtración entre tipos")
    else:
        pool = [0] * N
        for t in tiers:
            for i in range(N):
                pool[i] += series_p1[t][i]
        fases = []
        for f in prot["fases_abab"]:
            d, h, c = f.split("-")
            fases.append((int(d), int(h), c))
        segs = [(c, pool[d - 1:h]) for d, h, c in fases]
        a_vals = [x for c, xs in segs if c == "A" for x in xs]
        b_vals = [x for c, xs in segs if c == "B" for x in xs]
        naps_p1["todos"] = nap(a_vals, b_vals, True)
        salida.append(f"  P1 por período {pool} | NAP P1 {fmt(naps_p1['todos'])}")
        if len(segs) >= 3:
            a1, b1, a2 = mean(segs[0][1]), mean(segs[1][1]), mean(segs[2][1])
            if b1 != a1:
                arr = (a2 - a1) / (b1 - a1)
                salida.append(f"  índice de arrastre (A2−A1)/(B1−A1): {fmt(arr)}")
                if arr > u.get("arrastre_max", 0.5):
                    alertas.append("arrastre alto en ABAB: la segunda línea de base no volvió; "
                                   "el contraste A/B subestima el efecto")

    # filtración directa: unidades sin método que igual declaran métrica
    filtradas = sorted(f["u"]["id"] for f in filas if f["c"] == "A" and ((f["u"].get("metrica") or {}).get("nombre")))
    if filtradas:
        alertas.append(f"{len(filtradas)} unidad(es) de línea de base con métrica declarada "
                       f"(arrastre del método a la fase A): {', '.join(filtradas)}")

    # --- Adherencia (K1) y caída de entrega (K2) ---------------------------
    adh_min = u.get("adherencia_min", 0.7)
    adh_sem = {}
    for f in filas:
        if f["c"] != "B":
            continue
        m = f["u"].get("metrica") or {}
        completo = all(m.get(k) not in (None, "") for k in ("nombre", "baseline", "target", "ventana_dias")) \
            and f["u"].get("resultado_esperado") not in (None, "")
        adh_sem.setdefault(f["sem"], []).append(completo)
    k1 = False
    for w in sorted(adh_sem):
        par = adh_sem[w] + adh_sem.get(w + 1, [])
        if w + 1 in adh_sem and len(par) >= 3 and sum(par) / len(par) < adh_min:
            k1 = True
    total_b = [x for xs in adh_sem.values() for x in xs]
    salida.append("")
    salida.append(f"Adherencia al método (unidades B con objetivo y métrica completos): "
                  f"{fmt(sum(total_b) / len(total_b) if total_b else None)}")
    if k1:
        kills.append(f"K1 adherencia: en dos semanas seguidas (≥ 3 unidades) menos de {adh_min} de unidades completas")

    if prot["diseno"] == "linea_base_multiple":
        caida = u.get("caida_entrega_max", 0.5)
        for t in tiers:
            s = inicios_tier[t]
            ent_sem = [0] * N
            for f in filas:
                if f["t"] == t and f["entregada"] and 1 <= f["w"] <= N:
                    ent_sem[f["w"] - 1] += 1
            a, b = ent_sem[:s - 1], ent_sem[s - 1:]
            ma = mean(a)
            ult = b[-3 * ppw:]
            if ma and len(ult) == 3 * ppw and mean(ult) < (1 - caida) * ma \
                    and mean(series_p1[t][s - 1:]) <= mean(series_p1[t][:s - 1]):
                kills.append(f"K2 costo del método en '{t}': entrega de las últimas 3 semanas cae más de "
                             f"{caida} contra la línea de base, sin mejora de P1")

    # --- Pasividad -------------------------------------------------------
    salida.append("")
    salida.append("Pasividad del humano (decisiones tomadas por humano)")
    lat_min = u.get("latencia_baja_s", 30)
    grupos = {}
    for d in decs:
        if d.get("decidida_por") != "humano":
            continue
        un = next((x for x in filas if x["u"]["id"] == d.get("unidad")), None)
        fase = un["c"] if un else "?"
        clave = "auditoria" if d.get("clase") == "auditoria_muestreo" else f"{fase}/{d.get('condicion_revision') or '-'}"
        grupos.setdefault(clave, []).append(d)
    for clave in sorted(grupos):
        ds = grupos[clave]
        lats = [(ts(d["decidida_en"]) - ts(d["propuesta_en"])).total_seconds() for d in ds]
        aprob = sum(d.get("resultado") == "aprobada" for d in ds) / len(ds)
        baja = sum(x < lat_min for x in lats) / len(lats)
        forz = [d for d in ds if d.get("condicion_revision") == "HA"]
        vacia = None
        if forz:
            vacia = sum(1 for d in forz if not any((d.get("eleccion_forzada") or {}).get(k)
                                                    for k in ("metrica_escrita", "que_cambiaria_veredicto"))) / len(forz)
        salida.append(f"  {clave}: n={len(ds)}, aprobación sin cambios {fmt(aprob)}, "
                      f"mediana de latencia {fmt(median(lats), 0)} s, < {lat_min} s: {fmt(baja)}"
                      + (f", elección forzada vacía {fmt(vacia)}" if vacia is not None else ""))
        if aprob > u.get("aprobacion_alerta", 0.95) and baja > 0.5:
            alertas.append(f"pasividad en {clave}: aprobación {fmt(aprob)} y mayoría de latencias < {lat_min} s")

    # aprendizajes vacíos o repetidos
    vistos, vacios, repetidos, citados = set(), 0, 0, 0
    min_chars = u.get("aprendizaje_min_caracteres", 40)
    for a in aprs:
        txt = re.sub(r"\s+", " ", str(a.get("leccion") or "")).strip().lower()
        if len(txt) < min_chars:
            vacios += 1
        elif txt in vistos:
            repetidos += 1
        vistos.add(txt)
        if a.get("citado_por"):
            citados += 1
    cerradas_b = sum(1 for f in filas if f["c"] == "B" and f["u"].get("estado") in ("entregada", "descartada", "abandonada"))
    validos = len(aprs) - vacios - repetidos
    salida.append(f"  aprendizajes: {len(aprs)} ({vacios} vacíos, {repetidos} repetidos); "
                  f"LV = {validos}/{cerradas_b} unidades B cerradas = {fmt(validos / cerradas_b if cerradas_b else None)}; "
                  f"citados por unidades posteriores: {citados}")

    # --- Siembra de defectos y contraste con el mejor componente ----------
    salida.append("")
    salida.append("Siembra de defectos y contraste humano+agente contra el mejor componente solo")
    man_path = os.path.join(base, "siembra", "manifiesto.md")
    compromiso = os.path.join(base, "siembra.sha256")
    det = {"H": [0, 0], "A": [0, 0], "HA": [0, 0]}
    if os.path.isfile(man_path):
        if os.path.isfile(compromiso):
            esperado = open(compromiso, encoding="utf-8").read().split()[0]
            if sha256_file(man_path) != esperado:
                raise DatosInvalidos("el manifiesto de siembra no coincide con el hash comprometido al inicio")
            salida.append("  manifiesto revelado: coincide con el hash comprometido")
        else:
            alertas.append("manifiesto de siembra sin hash comprometido: no hay prueba de que se fijó antes")
        man = read_frontmatter(man_path)
        semillas = man.get("semillas") or {}
        total_pr = len({d.get("pr") for d in decs if d.get("pr")})
        salida.append(f"  semillas: {len(semillas)} sobre {total_pr} PR revisados "
                      f"(tasa {fmt(len(semillas) / total_pr if total_pr else None)}; "
                      f"tope pre-registrado {u.get('tasa_siembra_max')})")
        if total_pr and len(semillas) / total_pr > (u.get("tasa_siembra_max") or 1):
            alertas.append("tasa de siembra por encima del tope: riesgo de Bainbridge (pérdida de confianza)")
        for pr, archivo in sorted(semillas.items()):
            d = next((x for x in decs if x.get("pr") == pr), None)
            if d is None:
                alertas.append(f"semilla {pr} sin decisión de revisión registrada")
                continue
            c = d.get("condicion_revision")
            if c not in det:
                continue
            det[c][1] += 1
            if d.get("resultado") in ("modificada", "rechazada") and archivo in (d.get("hallazgos") or []):
                det[c][0] += 1
        for c in ("H", "A", "HA"):
            k, n = det[c]
            lo, hi = wilson(k, n)
            salida.append(f"  {c}: detectadas {k}/{n} (IC95 Wilson {fmt(lo)}–{fmt(hi)})")
        if det["HA"][1] >= u.get("min_semillas_k3", 4) and det["HA"][0] == 0:
            kills.append("K3 compuerta muerta: la condición humano+agente no detectó ninguna semilla")
    else:
        salida.append("  manifiesto todavía no revelado (se revela al cierre)")

    # verificación de la asignación de condiciones de revisión (commit-reveal)
    semilla_atd = prot.get("semilla_atd")
    if semilla_atd:
        conds = ["H", "A", "HA"]
        malas = [d.get("pr") for d in decs if d.get("pr") and d.get("condicion_revision")
                 and conds[int(hashlib.sha256(f"{semilla_atd}:{d['pr']}".encode()).hexdigest(), 16) % 3]
                 != d.get("condicion_revision")]
        if malas:
            alertas.append(f"condición de revisión distinta de la sorteada en {len(malas)} PR: {', '.join(sorted(malas))}")
        else:
            salida.append("  condiciones de revisión: coinciden con el sorteo sellado")

    # H2 es exploratoria (P-08): se reporta, no entra en la regla de decisión
    vaccaro = "sin_datos"
    mins = u.get("min_semillas_contraste", 5)
    if all(det[c][1] >= mins for c in det):
        p = {c: det[c][0] / det[c][1] for c in det}
        mejor = max(p["H"], p["A"])
        lo, hi = wilson(*det["HA"])
        vaccaro = "sostiene" if lo > mejor else ("descarta" if hi < mejor else "ambiguo")
    salida.append(f"  contraste HA contra max(H, A), exploratorio: {vaccaro.upper()} "
                  f"(requiere ≥ {mins} semillas por condición)")

    # --- TTO separado en trabajo y espera ---------------------------------
    salida.append("")
    salida.append("Tiempo hasta el outcome, separado (unidades validadas)")
    for c in ("A", "B"):
        trab, esp = [], []
        for f in filas:
            if f["c"] != c or not f["valid"]:
                continue
            cr, en = ts(f["u"]["creada_en"]), ts(f["u"]["entregada_en"])
            ev = min(ts(v["evidencia_en"]) for v in por_unidad[f["u"]["id"]]
                     if (v.get("nivel_evidencia") or 0) >= nivel_min)
            trab.append((en - cr).total_seconds() / 86400)
            esp.append((ev - en).total_seconds() / 86400)
        salida.append(f"  fase {c}: mediana trabajo {fmt(median(trab), 1)} d, mediana espera de evidencia {fmt(median(esp), 1)} d")

    # --- Horas humanas (bloques activos) ----------------------------------
    paridad = None
    if sems and prot["diseno"] == "linea_base_multiple":
        bl = {int(s["semana"]): s.get("bloques_activos_15min") or 0 for s in sems}
        primera = (min(inicios_tier.values()) - 1) // ppw + 1
        ultima = (max(inicios_tier.values()) - 1) // ppw + 1
        pre = [bl[w] for w in bl if w < primera]
        post = [bl[w] for w in bl if w > ultima]
        if pre and post:
            ratio = mean(post) / mean(pre)
            paridad = abs(ratio - 1) <= u.get("tolerancia_horas", 0.2)
            salida.append("")
            salida.append(f"Horas humanas: bloques activos/semana antes del primer inicio {fmt(mean(pre), 1)}, "
                          f"después del último {fmt(mean(post), 1)} (razón {fmt(ratio)}; "
                          f"{'dentro' if paridad else 'FUERA'} de la tolerancia {u.get('tolerancia_horas')})")
            if not paridad:
                alertas.append("las horas humanas no son comparables entre fases: el resultado no puede sostener la tesis")

    # --- Registro de modelos ----------------------------------------------
    cambios = sorted(regs, key=lambda r: str(r.get("desde")))
    salida.append("")
    salida.append(f"Registro de IA: {len(cambios)} configuración(es)")
    hitos = list(inicios_tier.values())
    vigente = {}
    for r in cambios:
        p = periodo_de(ts(r["desde"]), inicio, ppw)
        salida.append(f"  período {p}: {r.get('rol')} {r.get('herramienta')} {r.get('modelo')} "
                      f"(familia {r.get('familia')}) {r.get('version')} prompt {str(r.get('prompt_sha256'))[:12]}")
        if p > 1 and any(abs(p - h) <= ppw for h in hitos):
            alertas.append(f"cambio de modelo en el período {p}, a una semana o menos de un inicio de "
                           f"tratamiento: confusión posible")
        vigente[r.get("rol")] = r
        esc, rev = vigente.get("escritor"), vigente.get("revisor")
        if esc and rev and (esc.get("familia") or esc.get("modelo")) == (rev.get("familia") or rev.get("modelo")):
            alertas.append(f"período {p}: el revisor es de la misma familia de modelo que el escritor "
                           f"(sesgo de autopreferencia, Panickssery y otros 2024)")

    # auditoría compensatoria por muestreo (COSO 2006)
    aud = {}
    for d in decs:
        if d.get("clase") == "auditoria_muestreo":
            aud[semana_de(ts(d["decidida_en"]), inicio)] = aud.get(semana_de(ts(d["decidida_en"]), inicio), 0) + 1
    minimo = u.get("auditorias_por_semana_min", 1)
    faltan = [w for w in range(1, int(prot["semanas"]) + 1) if aud.get(w, 0) < minimo]
    salida.append(f"Auditoría por muestreo: {sum(aud.values())} en {int(prot['semanas'])} semanas; "
                  f"semanas por debajo del mínimo ({minimo}): {faltan or 'ninguna'}")
    if faltan:
        alertas.append(f"auditoría compensatoria incompleta en las semanas {faltan}")

    # --- Regla de decisión --------------------------------------------------
    salida.append("")
    veredicto = "ambiguo"
    if prot["diseno"] == "linea_base_multiple":
        alfa = u.get("alfa", 0.05)
        difs = {}
        for t in tiers:
            s0 = inicios_tier[t]
            difs[t] = mean(series_p1[t][s0 - 1:]) - mean(series_p1[t][:s0 - 1])
        buenos = sum(1 for t in tiers if difs[t] > 0)
        malos = sum(1 for t in tiers if difs[t] <= 0)
        p2_ok = tasa["A"] is not None and tasa["B"] is not None and tasa["B"] <= tasa["A"]
        if p_valor is not None and p_valor <= alfa and buenos >= 2 and p2_ok and paridad is not False and not k1:
            veredicto = "sostiene"
        elif malos >= 2 and (mean(list(difs.values())) <= 0 or not p2_ok):
            veredicto = "descarta"
        salida.append(f"Regla de decisión: p ≤ {alfa}: {p_valor is not None and p_valor <= alfa}; "
                      f"tiers con P1 B > A: {buenos}/{len(tiers)}; P2 B ≤ A: {p2_ok}; "
                      f"paridad de horas: {paridad}; adherencia sin K1: {not k1}")
    salida.append(f"VEREDICTO {'FINAL' if cerrado else 'PROVISORIO'} sobre la tesis: {veredicto.upper()}; "
                  f"componente de revisión (Vaccaro, H2 exploratoria): {vaccaro.upper()}")
    if veredicto == "descarta" and cerrado:
        kills.append("K5 tesis descartada por la regla de decisión pre-registrada")


def validar_protocolo(prot):
    """Falla con un mensaje claro si el protocolo no trae lo que el cálculo usa.
    Corre antes de cualquier cálculo: una plantilla sin completar sale con
    exit 2 y 'protocolo incompleto: falta <campo>' en vez de un traceback."""
    def falta(campo):
        raise DatosInvalidos(f"protocolo incompleto: falta {campo}")

    for campo in ("inicio", "semanas", "fecha_corte"):
        if prot.get(campo) in (None, ""):
            falta(campo)
    try:
        date.fromisoformat(str(prot["inicio"]))
    except ValueError:
        raise DatosInvalidos(f"protocolo inválido: inicio {prot['inicio']!r} no es una fecha AAAA-MM-DD")
    ts(prot["fecha_corte"])
    if prot["diseno"] == "linea_base_multiple":
        if not prot.get("ventanas"):
            falta("ventanas")
        asig = prot.get("asignacion")
        if not isinstance(asig, dict):
            falta("asignacion")
        for t in prot.get("tiers") or []:
            if asig.get(t) in (None, ""):
                falta(f"asignacion.{t}")
    elif not prot.get("fases_abab"):
        falta("fases_abab")
    umbrales = prot.get("umbrales")
    if not isinstance(umbrales, dict):
        falta("umbrales")
    if umbrales.get("k4_semana") in (None, ""):
        falta("umbrales.k4_semana")
    f0 = umbrales.get("fase0")
    if not isinstance(f0, dict):
        falta("umbrales.fase0")
    faltan = [k for k in CLAVES_FASE0 if f0.get(k) in (None, "")]
    sobran = sorted(k for k in f0 if k not in CLAVES_FASE0)
    if faltan or sobran:
        raise DatosInvalidos("protocolo inválido en umbrales.fase0: "
                             + "; ".join(x for x in (
                                 f"faltan {', '.join(faltan)}" if faltan else "",
                                 f"claves desconocidas {', '.join(sobran)}" if sobran else "") if x))
    for k in CLAVES_FASE0:
        if k != "kappa_min" and not isinstance(f0[k], int):
            raise DatosInvalidos(f"protocolo inválido: umbrales.fase0.{k} debe ser un entero (casos, no proporción)")


def main(argv):
    if len(argv) != 2:
        print(__doc__.split("Uso:")[1].strip(), file=sys.stderr)
        return 2
    base = argv[1]
    if not os.path.isdir(base):
        print(f"ERROR: no existe el directorio {base}", file=sys.stderr)
        return 2
    salida, kills, alertas = [], [], []
    try:
        verificar_sello(base, salida)
        prot = read_frontmatter(os.path.join(base, "protocolo.md"))
        if prot.get("diseno") not in ("linea_base_multiple", "abab"):
            raise DatosInvalidos("protocolo.diseno debe ser linea_base_multiple o abab")
        validar_protocolo(prot)
        r0 = fase0(base, prot, salida, kills, alertas)
        if r0 == "descartado":
            salida.append("Piloto: no corresponde (K0 activo)")
        else:
            piloto(base, prot, salida, kills, alertas)
    except (DatosInvalidos, KeyError, TypeError, ValueError) as e:
        print("\n".join(salida))
        print(f"ERROR: {type(e).__name__}: {e}", file=sys.stderr)
        return 2
    print("\n".join(salida))
    print("")
    print(f"Alertas ({len(alertas)}):")
    for a in alertas:
        print(f"  - {a}")
    print(f"Criterios de abandono activos ({len(kills)}):")
    for k in kills:
        print(f"  - {k}")
    return 1 if kills else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
