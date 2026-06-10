---
tags: [fundacional, recursos, herramientas]
status: borrador
created: 2026-06-10
---

# Recursos externos

Este documento registra los **repositorios y recursos de referencia externos** que sirven de inspiración, base tecnológica o ejemplos prácticos para el diseño y construcción de los agentes en [[HACS]] y las implementaciones de [[Cognitive OS - Arquitectura de referencia]].

Estos repositorios se encuentran clonados en el directorio local `external/` (el cual está excluido del control de versiones mediante el archivo `.gitignore` para evitar duplicaciones).

---

## Repositorios Sincronizados

| Repositorio | Autor / Origen | Propósito / Relación con HACS | Enlace GitHub |
|---|---|---|---|
| **ejemplo-harness-subagentes** | betta-tech | Ejemplo práctico de arneses de pruebas para subagentes y flujos de trabajo autónomos. | [betta-tech/ejemplo-harness-subagentes](https://github.com/betta-tech/ejemplo-harness-subagentes) |
| **harness-sdd** | betta-tech | Framework y plantillas para diseño de software guiado por arneses de pruebas ejecutados por agentes. | [betta-tech/harness-sdd](https://github.com/betta-tech/harness-sdd) |
| **memoria persistente** | external source | Herramientas de almacenamiento y estructuración de memoria semántica y grafos para asistentes de IA. | [external memory lifecycle repository](https://github.com/external memory lifecycle repository) |
| **agent workflow repository** | external source | Utilidades de inteligencia artificial y orquestación liviana. | [external agent workflow repository](https://github.com/external agent workflow repository) |
| **gentle-pi** | external source | Pipelines de ejecución e integración continua optimizados para tareas automáticas. | [external source/gentle-pi](https://github.com/external source/gentle-pi) |
| **gentleman-guardian-angel** | external source | Agente de supervisión y gobernanza de límites de ejecución y seguridad (Gobernanza humana/agente). | [external source/gentleman-guardian-angel](https://github.com/external source/gentleman-guardian-angel) |
| **Gentleman-MCP** | external source | Servidores de Model Context Protocol (MCP) para dotar a los agentes de herramientas de lectura/escritura de sistema. | [external source/Gentleman-MCP](https://github.com/external source/Gentleman-MCP) |
| **BMAD-METHOD** | bmad-code-org | Framework de desarrollo ágil AI-Native y spec-driven mediante equipo de agentes (PM, Architect, QA, Scrum Master). | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) |
| **agent-os** | buildermethods | Sistema ligero para descubrir, desplegar e indexar estándares y convenciones de código para agentes locales. | [buildermethods/agent-os](https://github.com/buildermethods/agent-os) |
| **spec-kit** | github | Toolkit oficial de GitHub para Spec-Driven Development, estructurando flujos de specify/plan/tasks/implement. | [github/spec-kit](https://github.com/github/spec-kit) |
| **gsd-core** | open-gsd | Framework de meta-prompting y de ingeniería de contexto ágil para evitar la deriva de contexto en sesiones de agentes. | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) |
| **OpenSpec** | Fission-AI | Especificación abierta y unificada para guiar la comunicación de requerimientos (SDD) consumible por múltiples agentes. | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) |
| **Kiro** | kirodotdev | IDE y CLI nativo de agentes para desarrollo spec-driven, control de tareas y DevOps automatizado. | [kirodotdev/Kiro](https://github.com/kirodotdev/Kiro) |
| **luum-cognitive-os** | Luum-Home | Malla de gobernanza de 14 capas desarrollada en colaboración entre Luum y OliveX (disponible localmente en `~/Projects/luum/luum-agent-os/`). | [Luum-Home/luum-cognitive-os](https://github.com/Luum-Home/luum-cognitive-os) |

---

## Cómo mantener los repositorios actualizados

Para simplificar la sincronización de estos repositorios y asegurar que cuenten con las últimas actualizaciones de sus respectivos autores, hemos creado el script de automatización `sync_external.sh` en la raíz del repositorio.

### Instrucciones de sincronización:

Ejecuta el script desde la raíz del proyecto para actualizar todos los repositorios clonados en la carpeta `external/`:

```bash
./sync_external.sh
```

El script verificará si el repositorio ya existe en `external/` y ejecutará un `git pull` para actualizarlo, o lo clonará desde cero si no estuviese presente.

---
Relacionado: [[Gobernanza]] · [[Roles de agentes]] · [[Cognitive OS - Arquitectura de referencia]]
