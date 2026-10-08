#!/usr/bin/env python3
"""
nucleo_tablero.py — tablero mínimo del Núcleo ODLC para tiny teams.

Lee fichas de objetivo con frontmatter YAML y, si existe, el registro de PR,
y reporta:

  - fichas con criterio de abandono vencido y sin veredicto  (alerta)
  - fichas sin métrica completa (métrica, baseline, target)   (alerta)
  - fichas sin dueño                                          (alerta)
  - proporción de PR con test que falla antes y pasa después  (informativo)

No necesita el protocolo sellado del piloto. Read-only, determinista y solo
stdlib: no consulta el reloj ni la red ni git; la fecha de corte se pasa por
argumento. Los timestamps son los que declara cada archivo: el registro es
declarado y auditable (cualquiera puede contrastarlo con el historial del
repo), no automático.

Estructura del directorio de datos:

  fichas/*.md        una ficha por objetivo (plantilla: fixtures/nucleo/plantillas/ficha.md)
  registro-pr/*.md   opcional, un archivo por PR (plantilla: .../registro-pr.md)

Uso:
  python3 scripts/nucleo_tablero.py <directorio-de-datos> --fecha AAAA-MM-DD

Exit codes: 0 = sin alertas
            1 = al menos una alerta
            2 = error (argumentos, directorio o datos ilegibles)
"""
import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from piloto_metricas import DatosInvalidos, load_dir  # noqa: E402  (parser YAML compartido)

VEREDICTOS = ("sigue", "abandona", "cumplido")


def vacio(v):
    return v is None or (isinstance(v, str) and not v.strip())


def fecha(v, archivo, campo):
    if vacio(v):
        return None
    try:
        return date.fromisoformat(str(v)[:10])
    except ValueError:
        raise DatosInvalidos(f"{archivo}: {campo} {v!r} no es una fecha AAAA-MM-DD")


def tablero(base, corte):
    salida, alertas = [], []
    fichas = load_dir(base, "fichas")
    if not fichas:
        raise DatosInvalidos(f"no hay fichas en {os.path.join(base, 'fichas')}")
    salida.append(f"Corte: {corte.isoformat()} · {len(fichas)} ficha(s)")
    for f in fichas:
        a = f["_archivo"]
        ident = f.get("id") or a
        if vacio(f.get("dueno")):
            alertas.append(f"{ident}: sin dueño")
        faltan = [c for c in ("metrica", "baseline", "target") if vacio(f.get(c))]
        if faltan:
            alertas.append(f"{ident}: métrica incompleta (falta {', '.join(faltan)})")
        ver = f.get("veredicto")
        if not vacio(ver) and ver not in VEREDICTOS:
            raise DatosInvalidos(f"{a}: veredicto {ver!r} no es uno de {', '.join(VEREDICTOS)}")
        limite = fecha(f.get("abandono_fecha"), a, "abandono_fecha")
        if limite is None or vacio(f.get("abandono_criterio")):
            alertas.append(f"{ident}: sin criterio de abandono con fecha")
        elif limite <= corte and vacio(ver):
            alertas.append(f"{ident}: criterio de abandono vencido el {limite.isoformat()} sin veredicto")
        salida.append(f"  {ident}: dueño {f.get('dueno') or 's/d'}, abandono {limite or 's/d'}, "
                      f"veredicto {ver or 'pendiente'}")

    prs = load_dir(base, "registro-pr")
    if not prs:
        salida.append("PR con test que falla antes y pasa después: sin registro-pr/")
    else:
        ok = sum(1 for p in prs if p.get("test_falla_antes") is True and p.get("test_pasa_despues") is True)
        salida.append(f"PR con test que falla antes y pasa después: {ok}/{len(prs)} ({ok / len(prs):.2f})")
    return salida, alertas


def main(argv):
    args = argv[1:]
    if len(args) != 3 or args[1] != "--fecha":
        print(__doc__.split("Uso:")[1].split("Exit")[0].strip(), file=sys.stderr)
        return 2
    base = args[0]
    if not os.path.isdir(base):
        print(f"ERROR: no existe el directorio {base}", file=sys.stderr)
        return 2
    try:
        corte = date.fromisoformat(args[2])
        salida, alertas = tablero(base, corte)
    except (DatosInvalidos, ValueError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    print("\n".join(salida))
    print(f"Alertas ({len(alertas)}):")
    for x in alertas:
        print(f"  - {x}")
    return 1 if alertas else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
