---
tags: [referencias, recursos, herramientas]
status: borrador
created: 2026-06-10
---

# Recursos externos

Este documento registra los **repositorios y recursos de referencia externos** que sirven de inspiración, base tecnológica o ejemplos prácticos para el diseño y construcción de los agentes en [[HACS]] y las implementaciones de [[Cognitive OS - Arquitectura de referencia]].

> [!warning] Setup requerido (el vault es portable; tu clon no)
> Las notas del vault que referencian rutas `external/...` (los módulos del curso y [[Análisis - Construyendo un Arnés de IA desde Cero]]) asumen que estos repositorios fueron clonados localmente en el directorio `external/`, que está **excluido del control de versiones** vía `.gitignore`. Si clonaste solo este repo, esas rutas no existen todavía: ejecutá primero la sincronización descripta al final de esta nota.

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
| **luum-cognitive-os** | Luum-Home | Malla de gobernanza de 14 capas desarrollada en colaboración entre Luum y OliveX como arquitectura de referencia. | [Luum-Home/luum-cognitive-os](https://github.com/Luum-Home/luum-cognitive-os) |
| **byo-coding-agent** | betta-tech | Arnés de agente didáctico y extensible en Go con soporte para TUI, subagentes dinámicos, memoria local y MCP. | [betta-tech/byo-coding-agent](https://github.com/betta-tech/byo-coding-agent) |
| **ai-engineering-lab** | MatiasNAmendola | Laboratorio educativo de Ingeniería de IA implementando primitivas desde cero en Python y arquitectura limpia. | [MatiasNAmendola/ai-engineering-lab](https://github.com/MatiasNAmendola/ai-engineering-lab) |

---

## Recursos Audiovisuales y Multimedia

Para complementar la investigación técnica de HACS y Cognitive OS, analizamos y recomendamos los siguientes materiales multimedia:
- [[Análisis - Stop Using Claude Without an Agentic OS]]: Resumen y desglose de las 5 capas arquitectónicas de un sistema operativo de inteligencia artificial, sus beneficios en la automatización empresarial y comparativas de interfaces de usuario.
- [[Análisis - Adaptando Claude Code para SDD]]: Lecciones y arquitectura sobre la adaptación del orquestador líder, higiene de contexto en archivos físicos y estructuración de especificaciones en notación EARS.
- [[Análisis - Harness Engineering y la Paradoja de Herramientas]]: Estudio sobre el control de agentes a través de arneses simplificados (lección de Vercel D0), mitigación de la degradación de contexto en el 40% y los tres pilares del desarrollo de IA.
- [[Análisis - La Cultura del Token]]: Métricas de adopción de IA por tokens consumidos, Goodhart's Law aplicada a la IA (casos Meta, Amazon y Nvidia), los dos errores (tacaño vs performativo) y el concepto de Retorno del Token (Token ROI).
- [[Análisis - Construyendo un Arnés de IA desde Cero]]: Estudio y desglose detallado de la arquitectura de un arnés de IA basado en Go, detallando el bucle de ejecución dual (REPL y evaluación), gateways de aprobación de comandos, delegación recursiva de subagentes y compactación de tokens.
- [[Análisis - Escasez de Tokens y la Crisis de Capacidad de la IA]]: La crisis de cómputo actual, racionamiento de tokens, el peaje lingüístico del español, modelos insostenibles de tarifa plana y el inicio de la IA de dos velocidades.
- [[Análisis - Token Economics y las 5 Predicciones del Caos]]: Cinco escenarios inminentes sobre la economía de tokens corporativa (donaciones, stipends, token poker, budgets por equipo, recompensas por uso), la advertencia de George Hotz y el riesgo de deuda técnica masiva.

---

## Cómo clonar y mantener los repositorios actualizados

Para simplificar el clonado inicial y la sincronización de estos repositorios, existe el script de automatización `sync_external.sh` en la raíz del repositorio (si no está presente en tu clon, cloná manualmente los repos de la tabla dentro de `external/`).

### Instrucciones de sincronización:

Ejecuta el script desde la raíz del proyecto para clonar/actualizar todos los repositorios en la carpeta `external/`:

```bash
./sync_external.sh
```

El script verificará si el repositorio ya existe en `external/` y ejecutará un `git pull` para actualizarlo, o lo clonará desde cero si no estuviese presente.

---
Relacionado: [[Gobernanza]] · [[Roles de agentes]] · [[Cognitive OS - Arquitectura de referencia]] · [[Repositorios y catálogos de skills]] · [[Catálogo de herramientas y productividad]] · [[Nuevos roles profesionales en la era de IA]] · [[AI Engineering Lab - Repositorio de referencia]]
