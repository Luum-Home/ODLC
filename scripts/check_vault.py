#!/usr/bin/env python3
"""
check_vault.py — chequeo de operabilidad del vault Markdown HACS/ODLC.

Read-only, determinista, sin dependencias externas (no requiere pyyaml ni
ningún paquete fuera de la stdlib) y sin depender del estado de sesión: toma
la lista de archivos directamente de `git ls-files`, no del filesystem a
ojo, así que corre igual en cualquier checkout limpio del repo.

Qué chequea (y cómo leer cada hallazgo):

  wikilinks_rotos
      `[[Nota]]` cuyo destino no existe como nota en docs/. El texto
      reportado es "archivo:línea -> [[texto original del wikilink]]".

  anclas_rotas
      `[[Nota#Sección]]` donde la nota SÍ existe pero "Sección" no es un
      heading literal (#, ##, ...) de esa nota. Un ancla sólo se valida
      cuando la nota destino es inambigua (ver colisión de basename); si hay
      dos notas con el mismo nombre no se intenta adivinar cuál.

  links_md_rotos
      `[texto](ruta/relativa.md)` — se resuelve relativo al archivo que lo
      contiene, con URL-decode (para %20, %C3%A1, etc.) y comparando en
      NFC/NFD (para que un acento compuesto de otra forma no dé falso
      positivo). Cubre el README raíz y toda nota del vault; los links
      http(s)/mailto/anclas puras (#x) se ignoran.

  colision_basename
      Dos o más notas en docs/ comparten el mismo nombre de archivo sin
      extensión. Un wikilink `[[Nota]]` a ese nombre es ambiguo en
      Obsidian (y en este script no se resuelve para anclas).

  frontmatter_ausente_o_sin_cierre / frontmatter_sin_<campo> /
  status_fuera_de_convencion / fecha_created_invalida
      Contrato de frontmatter de las notas de docs/: bloque YAML delimitado
      por `---`, con los campos tags/status/created; status debe ser uno de
      {crudo, semilla, borrador, evergreen}; created debe matchear YYYY-MM-DD.
      (El README raíz no lleva frontmatter y se excluye de este chequeo.)

  moc_ausente
      Nota de docs/ que no aparece citada por wikilink en el mapa de
      contenido (docs/HACS-ODLC.md). Las notas bajo 00_crudo/ y 07_cursos/
      se reportan aparte (moc_ausente_agrupada_bajo_hub) porque se agrupan
      bajo un hub y no cuentan como hallazgo real.

Trampas conocidas que este script maneja explícitamente:

  - Alias de wikilink escapado dentro de tablas markdown: `[[Nota\\|alias]]`.
    Sin des-escapar el `\\|` antes de partir por el separador de alias, el
    target queda como "Nota\\" y se reporta como roto por error.
  - `git ls-files` octal-escapa nombres de archivo no-ASCII por defecto
    (p. ej. "Más código..." aparece como "M\303\241s..."). Se corre con
    `-c core.quotepath=off` y se normaliza todo a NFC.
  - Bloques de código (```...``` e `código inline`) pueden contener texto
    de ejemplo con pinta de wikilink o link markdown (p. ej. una nota que
    documenta la sintaxis `[[wikilinks]]`); se enmascaran antes de buscar
    links, preservando el conteo de líneas para que los reportes de
    "archivo:línea" sigan siendo exactos.

Uso:
  ./scripts/check_vault.py [ruta-al-repo]      (default: cwd)

Exit codes: 0 = sin hallazgos | 1 = hallazgos | 2 = error de uso/entorno
"""
import os
import re
import subprocess
import sys
import unicodedata
import urllib.parse
from collections import defaultdict

STATUS_OK = {"crudo", "semilla", "borrador", "evergreen"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WIKILINK = re.compile(r"(?<!\!)\[\[([^\]\[]+?)\]\]")
MDLINK = re.compile(r"(?<!\!)\[[^\]\n]*\]\(([^)\s]+?)(?:\s+\"[^\"]*\")?\)")
HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*$")
MOC_HUB_PREFIXES = ("00_crudo" + os.sep, "07_cursos" + os.sep)


def nfc(s):
    return unicodedata.normalize("NFC", s)


def git_tracked_md(repo):
    """Lista de rutas .md trackeadas por git, relativas a `repo`.

    Usa -c core.quotepath=off porque, por default, `git ls-files` escapa a
    octal los nombres de archivo no-ASCII (una nota como
    "Más código no es más velocidad.md" sale como "M\\303\\241s...md"), lo
    que rompe cualquier comparación de rutas contra el filesystem. Se
    normaliza a NFC además, porque distintas fuentes (git, macOS APFS,
    URL-decode) pueden entregar el mismo nombre en NFC o NFD.
    """
    try:
        out = subprocess.run(
            ["git", "-c", "core.quotepath=off", "-C", repo, "ls-files", "--", "*.md"],
            capture_output=True, text=True, check=True,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"ERROR: no se pudo listar archivos con git ls-files: {e}", file=sys.stderr)
        sys.exit(2)
    return sorted(nfc(p) for p in out.splitlines() if p.strip())


def mask_code(text):
    """Enmascara bloques ``` ``` y código `inline`, preservando el conteo
    de líneas y columnas, para no confundir ejemplos de sintaxis
    (p. ej. una nota que documenta cómo se escribe un wikilink) con links
    reales."""
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", lambda m: " " * len(m.group(0)), text)
    return text


def parse_frontmatter(raw):
    """Devuelve (dict campo->valor, bloque_bien_delimitado)."""
    if not raw.startswith("---\n") and raw.strip() != "---":
        return None, False
    m = re.match(r"^---\n(.*?)\n---[ \t]*(?:\n|$)", raw, flags=re.S)
    if not m:
        return {}, False
    fm = {}
    for ln in m.group(1).splitlines():
        mm = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", ln)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip()
    return fm, True


def path_exists_any_norm(path):
    for form in ("NFC", "NFD"):
        if os.path.exists(unicodedata.normalize(form, path)):
            return True
    return os.path.exists(path)


def main():
    repo = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    vault = os.path.join(repo, "docs")

    if not os.path.exists(os.path.join(repo, ".git")):
        print(f"ERROR: {repo} no parece la raíz de un repo git.", file=sys.stderr)
        return 2
    if not os.path.isdir(vault):
        print(f"ERROR: no existe {vault}", file=sys.stderr)
        return 2

    tracked = git_tracked_md(repo)
    all_md = [os.path.join(repo, p) for p in tracked if not p.startswith("external/")]
    vault_md = [p for p in all_md if p.startswith(vault + os.sep)]

    if not vault_md:
        print(f"ERROR: no se encontró ninguna nota .md trackeada bajo {vault}", file=sys.stderr)
        return 2

    # También indexamos archivos no-.md de docs/ (adjuntos: pdf, png, ...)
    # como destinos válidos de wikilink, por si alguna nota enlaza un
    # adjunto en vez de otra nota.
    try:
        all_tracked_out = subprocess.run(
            ["git", "-c", "core.quotepath=off", "-C", repo, "ls-files", "--", "docs"],
            capture_output=True, text=True, check=True,
        ).stdout
    except subprocess.CalledProcessError as e:
        print(f"ERROR: git ls-files docs falló: {e}", file=sys.stderr)
        return 2
    attach_basenames = {nfc(os.path.basename(p)) for p in all_tracked_out.splitlines() if p.strip()}

    findings = defaultdict(list)

    # -- índices de notas del vault --------------------------------------
    basename_index = defaultdict(list)     # stem -> [ruta relativa al repo]
    relvault_index = {}                    # ruta relativa al vault sin ext -> ruta absoluta
    for p in vault_md:
        stem = nfc(os.path.splitext(os.path.basename(p))[0])
        basename_index[stem].append(os.path.relpath(p, repo))
        rel_noext = nfc(os.path.splitext(os.path.relpath(p, vault))[0])
        relvault_index[rel_noext] = p

    # -- 1. links markdown relativos (todo el repo, incluye README raíz) -
    for p in all_md:
        raw = open(p, encoding="utf-8").read()
        masked = mask_code(raw)
        rel = os.path.relpath(p, repo)
        base = os.path.dirname(p)
        for n, line in enumerate(masked.splitlines(), 1):
            for m in MDLINK.finditer(line):
                href = m.group(1)
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", href) or href.startswith("#"):
                    continue  # esquema externo (http, mailto...) o ancla pura
                path_part = urllib.parse.unquote(href.split("#")[0])
                if not path_part:
                    continue
                cand = os.path.normpath(os.path.join(base, path_part))
                if not path_exists_any_norm(cand):
                    findings["links_md_rotos"].append(
                        f"{rel}:{n} -> [{href}] no existe ({os.path.relpath(cand, repo)})"
                    )

    # -- 2/3. wikilinks y anclas (sólo notas del vault) -------------------
    heading_cache = {}

    def headings_of(path):
        if path not in heading_cache:
            hs = set()
            with open(path, encoding="utf-8") as fh:
                for ln in fh:
                    mm = HEADING.match(ln)
                    if mm:
                        hs.add(mm.group(1).strip())
            heading_cache[path] = hs
        return heading_cache[path]

    for p in vault_md:
        raw = open(p, encoding="utf-8").read()
        masked = mask_code(raw)
        rel = os.path.relpath(p, repo)
        for n, line in enumerate(masked.splitlines(), 1):
            for m in WIKILINK.finditer(line):
                # Trampa: en tablas markdown el separador de alias va
                # escapado como \| ("[[Nota\|alias]]"). Si no se
                # des-escapa antes de partir, "Nota\" queda como target y
                # se reporta como roto por error.
                inner = m.group(1)
                unescaped = inner.replace("\\|", "|")
                target = unescaped.split("|", 1)[0]
                tgt, _, anchor = target.partition("#")
                tgt, anchor = tgt.strip(), anchor.strip()
                if not tgt:
                    continue
                stem = nfc(tgt.split("/")[-1])
                tgt_nfc = nfc(tgt)

                dest = None
                if tgt_nfc in relvault_index:
                    dest = relvault_index[tgt_nfc]
                elif stem in basename_index and len(basename_index[stem]) == 1:
                    dest = os.path.join(repo, basename_index[stem][0])

                if dest is None:
                    if stem not in basename_index and stem not in attach_basenames:
                        findings["wikilinks_rotos"].append(f"{rel}:{n} -> [[{inner}]]")
                    continue  # basename ambiguo (colisión) o adjunto: no se evalúa ancla

                if anchor:
                    if anchor not in headings_of(dest):
                        findings["anclas_rotas"].append(
                            f"{rel}:{n} -> [[{tgt}#{anchor}]] (la nota existe, la sección no)"
                        )

    # -- 4. colisiones de basename -----------------------------------------
    for stem, paths in sorted(basename_index.items()):
        if len(paths) > 1:
            findings["colision_basename"].append(f"{stem!r} -> {', '.join(sorted(paths))}")

    # -- 5. contrato de frontmatter (sólo notas de docs/) -------------------
    for p in vault_md:
        raw = open(p, encoding="utf-8").read()
        rel = os.path.relpath(p, repo)
        fm, ok = parse_frontmatter(raw)
        if fm is None or not ok:
            findings["frontmatter_ausente_o_sin_cierre"].append(rel)
            continue
        for campo in ("tags", "status", "created"):
            if campo not in fm or fm[campo] == "":
                findings[f"frontmatter_sin_{campo}"].append(rel)
        st = fm.get("status")
        if st and st not in STATUS_OK:
            findings["status_fuera_de_convencion"].append(f"{rel}: status={st!r}")
        cr = fm.get("created")
        if cr and not DATE_RE.match(cr):
            findings["fecha_created_invalida"].append(f"{rel}: created={cr!r}")

    # -- 6. cobertura del mapa de contenido ---------------------------------
    moc_path = os.path.join(vault, "HACS-ODLC.md")
    if not os.path.isfile(moc_path):
        findings["moc_no_encontrado"].append("docs/HACS-ODLC.md")
    else:
        moc_raw = mask_code(open(moc_path, encoding="utf-8").read())
        listed = set()
        for m in WIKILINK.finditer(moc_raw):
            unescaped = m.group(1).replace("\\|", "|")
            t = unescaped.split("|", 1)[0].split("#")[0].strip()
            if t:
                listed.add(nfc(t.split("/")[-1]))
        for p in vault_md:
            rel = os.path.relpath(p, repo)
            relvault = os.path.relpath(p, vault)
            stem = nfc(os.path.splitext(os.path.basename(p))[0])
            if stem in listed or relvault in ("HACS-ODLC.md", "README.md"):
                continue
            if relvault.startswith(MOC_HUB_PREFIXES):
                findings["moc_ausente_agrupada_bajo_hub"].append(rel)  # informativo
            else:
                findings["moc_ausente"].append(rel)

    # ------------------------------------------------------------ reporte
    INFORMATIVE = {"moc_ausente_agrupada_bajo_hub"}

    print("=" * 72)
    print(f"REPO:  {repo}")
    print(f"VAULT: {vault}")
    print(f"notas .md en docs/ .......... {len(vault_md)}")
    print(f"archivos .md totales ......... {len(all_md)} (incluye README.md raíz)")
    print("=" * 72)

    total = 0
    for k in sorted(findings):
        v = findings[k]
        marker = " (informativo, no cuenta)" if k in INFORMATIVE else ""
        print(f"\n### {k}  ({len(v)}){marker}")
        for item in sorted(v):
            print(f"  - {item}")
        if k not in INFORMATIVE:
            total += len(v)

    print(f"\n{'=' * 72}\nTOTAL HALLAZGOS: {total}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
