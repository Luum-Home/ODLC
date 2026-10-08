---
tags: [referencias, recursos, herramientas]
status: borrador
created: 2026-06-10
---

# Recursos externos

Este documento registra los **repositorios y recursos de referencia externos** que sirven de inspiración, base tecnológica o ejemplos prácticos para el diseño y construcción de los agentes en [[HACS]] y de los arneses que los operan ([[Agent Loop Engineering]]).

> [!warning] Setup requerido (el vault es portable; tu clon no)
> Las notas del vault que referencian rutas `external/...` (los módulos del curso y [[Análisis - Construyendo un Arnés de IA desde Cero]]) asumen que estos repositorios fueron clonados localmente en el directorio `external/`, que está **excluido del control de versiones** vía `.gitignore`. Si clonaste solo este repo, esas rutas no existen todavía: ejecutá primero la sincronización descripta al final de esta nota.

---

## Repositorios Sincronizados

| Repositorio | Autor / Origen | Propósito / Relación con HACS | Enlace GitHub |
|---|---|---|---|
| **ejemplo-harness-subagentes** | betta-tech | Variante del ejemplo harness (CLI de notas en Python) con subagentes leader/implementer/reviewer definidos en `.claude/agents/`. | [betta-tech/ejemplo-harness-subagentes](https://github.com/betta-tech/ejemplo-harness-subagentes) |
| **harness-sdd** | betta-tech | Repo de ejemplo (CLI de notas en Python) con specs EARS y una puerta de aprobación humana. | [betta-tech/harness-sdd](https://github.com/betta-tech/harness-sdd) |
| **engram** | Gentleman-Programming | Memoria persistente para agentes de código, agnóstica del agente y distribuida como binario único. | [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram) |
| **gentle-ai** | Gentleman-Programming | Configurador de ecosistema para agentes de código: memoria persistente, flujos Spec-Driven Development, skills, servidores MCP y modelo asignable por fase. | [Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai) |
| **gentle-pi** | Gentleman-Programming | Paquete para el agente Pi con flujo Spec-Driven Development, subagentes, evidencia TDD y guardas de seguridad; incluye la skill `judgment-day`. | [Gentleman-Programming/gentle-pi](https://github.com/Gentleman-Programming/gentle-pi) |
| **gentleman-guardian-angel** | Gentleman-Programming | Revisor de código con IA, agnóstico de proveedor y escrito en Bash, que corre como hook de pre-commit. | [Gentleman-Programming/gentleman-guardian-angel](https://github.com/Gentleman-Programming/gentleman-guardian-angel) |
| **Gentleman-MCP** | Gentleman-Programming | Gateway de chat en Go sobre gRPC/TLS hacia modelos locales vía Ollama; pese al nombre, no implementa el protocolo MCP. | [Gentleman-Programming/Gentleman-MCP](https://github.com/Gentleman-Programming/Gentleman-MCP) |
| **BMAD-METHOD** | bmad-code-org | Framework de desarrollo ágil AI-Native y spec-driven mediante equipo de agentes (PM, Architect, QA, Scrum Master). | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) |
| **agent-os** | buildermethods | Sistema ligero para descubrir, desplegar e indexar estándares y convenciones de código para agentes locales. | [buildermethods/agent-os](https://github.com/buildermethods/agent-os) |
| **spec-kit** | github | Toolkit oficial de GitHub para Spec-Driven Development, estructurando flujos de specify/plan/tasks/implement. | [github/spec-kit](https://github.com/github/spec-kit) |
| **gsd-core** | open-gsd | Framework de meta-prompting y de ingeniería de contexto ágil para evitar la deriva de contexto en sesiones de agentes. | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) |
| **OpenSpec** | Fission-AI | Especificación abierta y unificada para guiar la comunicación de requerimientos (SDD) consumible por múltiples agentes. | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) |
| **Kiro** | kirodotdev | IDE y CLI nativo de agentes para desarrollo spec-driven, control de tareas y DevOps automatizado. | [kirodotdev/Kiro](https://github.com/kirodotdev/Kiro) |
| **byo-coding-agent** | betta-tech | Arnés de agente didáctico y extensible en Go con soporte para TUI, subagentes dinámicos, memoria local y MCP. | [betta-tech/byo-coding-agent](https://github.com/betta-tech/byo-coding-agent) |

Son los 14 repositorios que clona `sync_external.sh` (verificable con `grep -c '^  "https://github.com/' sync_external.sh` desde la raíz).

## Referenciados, no sincronizados

Repositorios citados por el vault que `sync_external.sh` no clona.

| Repositorio | Autor / Origen | Propósito / Relación con HACS | Enlace GitHub |
|---|---|---|---|
| **ai-engineering-lab** | MatiasNAmendola | Laboratorio educativo de Ingeniería de IA implementando primitivas desde cero en Python y arquitectura limpia. | [MatiasNAmendola/ai-engineering-lab](https://github.com/MatiasNAmendola/ai-engineering-lab) |

---

## Libros y marcos de referencia

| Recurso | Autor | Relación con HACS-ODLC | Enlace |
|---|---|---|---|
| **Sooner Safer Happier: Antipatterns and Patterns for Business Agility** (IT Revolution, 2020) | Jon Smart (con Zsolt Berend, Myles Ogilvie y Simon Rohrer) | Agilidad de negocio con meta *Better Value Sooner Safer Happier* (BVSSH) y foco en resultados; ver la fila en [[Comparativa con metodologías existentes]]. | [soonersaferhappier.com](https://www.soonersaferhappier.com/) |
| **Manifiesto Ágil** (2001) | Beck, Cockburn, Fowler, Schwaber, Sutherland y otros | Valores y principios releídos uno por uno en [[Relectura del Manifiesto Ágil]]. | [agilemanifesto.org](https://agilemanifesto.org/) |

*Verificación (2026-10-07): el sitio de Sooner Safer Happier declara BVSSH como meta y "Focus on Outcomes" como patrón; los OKRs aparecen en la oferta comercial del sitio, no verificado en el libro. El libro no se leyó para esta nota. Los coautores están verificados en `https://itrevolution.com/product/sooner-safer-happier/`. Comando del sitio: `curl -sL https://www.soonersaferhappier.com/ | sed 's/<[^>]*>/ /g' | tr -s ' \n' | LC_ALL=C /usr/bin/grep -oiE "[^.]{0,100}(better value|outcome|antipattern)[^.]{0,100}"`*

---

## Recursos Audiovisuales y Multimedia

Para complementar la investigación técnica de HACS y de la ingeniería de agentes, analizamos y recomendamos los siguientes materiales multimedia:
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
Relacionado: [[Gobernanza]] · [[Roles de agentes]] · [[Agent Loop Engineering]] · [[Repositorios y catálogos de skills]] · [[Catálogo de herramientas y productividad]] · [[Nuevos roles profesionales en la era de IA]] · [[AI Engineering Lab - Repositorio de referencia]]
