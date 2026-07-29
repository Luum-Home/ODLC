#!/bin/bash
# Script para clonar y mantener actualizados los repositorios externos de referencia en external/
#
# Exit codes: 0 = todo OK (clonado/actualizado sin fallos) | 1 = hubo fallos o
# clones sucios | 2 = error de uso/entorno (falta git, no es un repo, etc.)
set -uo pipefail

# --- Entorno: no colgarse pidiendo credenciales, cortar conexiones lentas ---
# macOS no trae `timeout` de coreutils por defecto (un intento anterior de
# usarlo falló con exit 127). En su lugar usamos los límites de git para
# abortar transferencias lentas o colgadas.
export GIT_TERMINAL_PROMPT=0
export GIT_ASKPASS=/usr/bin/true
GIT=(git -c http.lowSpeedLimit=1000 -c http.lowSpeedTime=15)

command -v git >/dev/null 2>&1 || { echo "ERROR: git no está disponible en PATH." >&2; exit 2; }

# Lista de repositorios a sincronizar
# NOTA: los 5 repos de la organización Gentleman-Programming (engram,
# gentle-ai, gentle-pi, gentleman-guardian-angel, Gentleman-MCP) nacieron en
# este script (commit 57ff279) como placeholders con espacios
# ("https://github.com/external source/gentle-pi", etc.), que `git clone`
# rechaza de entrada. Restauradas a sus URLs reales, verificadas contra los
# remotes configurados en los clones locales de external/
# (`git -C external/<repo> remote get-url origin`) y confirmadas alcanzables
# con `git ls-remote`.
REPOS=(
  "https://github.com/betta-tech/ejemplo-harness-subagentes"
  "https://github.com/betta-tech/harness-sdd"
  "https://github.com/Gentleman-Programming/engram"
  "https://github.com/Gentleman-Programming/gentle-ai"
  "https://github.com/Gentleman-Programming/gentle-pi"
  "https://github.com/Gentleman-Programming/gentleman-guardian-angel"
  "https://github.com/Gentleman-Programming/Gentleman-MCP"
  "https://github.com/bmad-code-org/BMAD-METHOD"
  "https://github.com/buildermethods/agent-os"
  "https://github.com/github/spec-kit"
  "https://github.com/open-gsd/gsd-core"
  "https://github.com/Fission-AI/OpenSpec"
  "https://github.com/kirodotdev/Kiro"
  "https://github.com/betta-tech/byo-coding-agent"
)

# Crear directorio external si no existe
mkdir -p external

echo "Iniciando sincronización de repositorios en external/..."
echo "========================================================="

CLONADOS=()
ACTUALIZADOS=()
FALLIDOS=()
SUCIOS=()

for repo in "${REPOS[@]}"; do
  # Extraer el nombre del repositorio de la URL
  repo_name=$(basename "$repo" .git)
  dest="external/$repo_name"

  if [ -d "$dest" ]; then
    # Un `git pull` sobre un clon con cambios locales sorprende de dos formas
    # distintas: si hay archivos BORRADOS sin commitear, el pull los restaura
    # silenciosamente; si hay archivos MODIFICADOS, el pull falla. En vez de
    # dejar que pase cualquiera de las dos, detectamos el estado sucio antes
    # y lo reportamos como tal, sin intentar el pull.
    estado_sucio="$("${GIT[@]}" -C "$dest" status --porcelain 2>&1)"
    estado_rc=$?
    if [ $estado_rc -ne 0 ]; then
      echo "Fallo al inspeccionar external/$repo_name (¿no es un repo git válido?)."
      FALLIDOS+=("$repo_name: git status falló")
    elif [ -n "$estado_sucio" ]; then
      echo "Omitiendo external/$repo_name: tiene cambios locales sin commitear."
      echo "    ${estado_sucio//$'\n'/$'\n    '}"
      SUCIOS+=("$repo_name")
    else
      echo "Actualizando external/$repo_name..."
      if "${GIT[@]}" -C "$dest" pull; then
        ACTUALIZADOS+=("$repo_name")
      else
        echo "Fallo al actualizar external/$repo_name."
        FALLIDOS+=("$repo_name: git pull falló")
      fi
    fi
  else
    echo "Clonando $repo en external/$repo_name..."
    if "${GIT[@]}" clone "$repo" "$dest"; then
      CLONADOS+=("$repo_name")
    else
      echo "Fallo al clonar $repo."
      FALLIDOS+=("$repo_name: git clone falló ($repo)")
    fi
  fi
  echo "---------------------------------------------------------"
done

echo "Resumen de sincronización:"
echo "  clonados:           ${#CLONADOS[@]}"
echo "  actualizados:       ${#ACTUALIZADOS[@]}"
echo "  sucios (omitidos):  ${#SUCIOS[@]}"
for s in "${SUCIOS[@]:-}"; do
  [ -n "$s" ] && echo "    - $s"
done
echo "  fallidos:           ${#FALLIDOS[@]}"
for f in "${FALLIDOS[@]:-}"; do
  [ -n "$f" ] && echo "    - $f"
done

if [ "${#FALLIDOS[@]}" -gt 0 ] || [ "${#SUCIOS[@]}" -gt 0 ]; then
  echo "Sincronización terminada CON PROBLEMAS (ver resumen arriba)."
  exit 1
fi

echo "Sincronización finalizada con éxito."
exit 0
