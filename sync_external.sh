#!/bin/bash
# Script para clonar y mantener actualizados los repositorios externos de referencia en external/

# Lista de repositorios a sincronizar
REPOS=(
  "https://github.com/betta-tech/ejemplo-harness-subagentes"
  "https://github.com/betta-tech/harness-sdd"
  "https://github.com/external memory lifecycle repository"
  "https://github.com/external agent workflow repository"
  "https://github.com/external source/gentle-pi"
  "https://github.com/external source/gentleman-guardian-angel"
  "https://github.com/external source/Gentleman-MCP"
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

for repo in "${REPOS[@]}"; do
  # Extraer el nombre del repositorio de la URL
  repo_name=$(basename "$repo" .git)
  
  if [ -d "external/$repo_name" ]; then
    echo "Actualizando external/$repo_name..."
    # Ir al directorio, actualizar vía pull y regresar
    (cd "external/$repo_name" && git pull)
  else
    echo "Clonando $repo en external/$repo_name..."
    git clone "$repo" "external/$repo_name"
  fi
  echo "---------------------------------------------------------"
done

echo "Sincronización finalizada con éxito."
