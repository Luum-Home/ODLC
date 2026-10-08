#!/usr/bin/env python3
"""Casos de error de la Fase 0 sobre copias descartables de los fixtures. Read-only sobre el repo.
Exit 0 si cada caso da el exit esperado, 1 si alguno no."""
import hashlib, os, re, shutil, subprocess, sys, tempfile
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = os.path.join(REPO, "scripts/fixtures/piloto")
def resellar(d):
    h = hashlib.sha256(open(os.path.join(d, "protocolo.md"), "rb").read()).hexdigest()
    open(os.path.join(d, "protocolo.sha256"), "w").write(f"{h}  protocolo.md\n")
def caso(nombre, src, mut, esperado):
    tmp = tempfile.mkdtemp(); d = os.path.join(tmp, "c"); shutil.copytree(src, d)
    try:
        mut(d)
        p = subprocess.run([sys.executable, os.path.join(REPO, "scripts/piloto_metricas.py"), d], capture_output=True, text=True)
        err = (p.stderr.strip().splitlines() or [""])[-1]
        ok = p.returncode == esperado
        print(f"{'OK ' if ok else 'MAL'} {nombre}: exit={p.returncode} (esperado {esperado}) {err}")
        return ok
    finally:
        shutil.rmtree(tmp)
def sub_prot(a, b):
    def m(d):
        p = os.path.join(d, "protocolo.md"); s = open(p).read(); assert a in s, a
        open(p, "w").write(s.replace(a, b)); resellar(d)
    return m
def dup_agente(d):
    shutil.copy(os.path.join(d, "fase0/codificacion/E01-ciego.md"), os.path.join(d, "fase0/codificacion/E01-ciego-bis.md"))
def ent_extra_n(nuevo):
    def m(d):
        s = open(os.path.join(d, "fase0/entrevistas/E12.md")).read()
        s = s.replace("id: E12", f"id: {nuevo}"); s = re.sub(r"fecha: \S+", "fecha: 2026-10-30", s)
        assert not os.path.exists(os.path.join(d, f"fase0/entrevistas/{nuevo}.md"))
        open(os.path.join(d, f"fase0/entrevistas/{nuevo}.md"), "w").write(s)
    return m
def senal_vieja(d):
    p = os.path.join(d, "fase0/entrevistas/E02.md"); s = open(p).read()
    open(p, "w").write(s.replace("senales_compromiso: []", "senales_compromiso: [reputacion]"))
def quita_desvio(d):
    os.remove(os.path.join(d, "desvios/DV-02.md"))
ab, ext, dv = os.path.join(F, "caso-abandono"), os.path.join(F, "caso-extension"), os.path.join(F, "caso-desvio")
r = [
  caso("clave vieja min_entrevistas", ab, sub_prot("entrevistas_fijas: 12", "min_entrevistas: 12"), 2),
  caso("clave desconocida en fase0", ab, sub_prot("    extension: 5 ", "    extension: 5\n    confirma_dolor: 0.5 "), 2),
  caso("falta k4_semana", ab, sub_prot("  k4_semana: 8", "  k4_seman: 8"), 2),
  caso("umbral en proporción", ab, sub_prot("descarta_dolor_casos: 2 ", "descarta_dolor_casos: 0.2 "), 2),
  caso("dos codificaciones agente_ciego de E01", ab, dup_agente, 2),
  caso("13 entrevistas con tramo 1 no ambiguo", ab, ent_extra_n("E13"), 2),
  caso("18 entrevistas en la extensión", ext, ent_extra_n("E18"), 2),
  caso("señal 'reputacion' fuera del libro de códigos", ab, senal_vieja, 2),
  caso("desvío faltante en la cadena", dv, quita_desvio, 2),
  caso("cadena de desvíos válida", dv, lambda d: None, 0),
]
sys.exit(0 if all(r) else 1)
