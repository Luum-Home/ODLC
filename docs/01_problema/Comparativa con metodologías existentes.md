---
tags: [problema, comparativa]
status: semilla
created: 2026-06-10
---

# Comparativa con metodologías existentes

Crítica formal de [[ODLC]]/[[HACS]] contra los marcos dominantes. Cada fila es una hipótesis a desarrollar con honestidad: qué hace bien cada marco, qué no cubre, y qué reutilizamos.

| Marco | Qué optimiza | Qué no cubre | Qué reutilizamos |
|---|---|---|---|
| **SDLC** | Secuencia: requerimientos → desarrollo → mantenimiento | Asume ejecución cara y humana; sin aprendizaje estructural | La noción de ciclo de vida |
| **Scrum** | Coordinación humana (backlog, historias, sprints) | Agentes como ejecutores; validación contra objetivos | Iteración corta, retro → [[Fase 6 - Learning]] |
| **SAFe** | Coordinación a escala entre múltiples equipos humanos | Escala vía *más proceso*, no vía *más agentes* | Alineación estratégica → [[Fase 1 - Objective]] |
| **DevOps** | Entrega continua, feedback técnico | Decisión y contexto; optimiza el pipeline, no la intención | Automatización, observabilidad → [[Fase 4 - Execution]] |
| **Team Topologies** | Estructura de equipos y carga cognitiva | Los "equipos" siguen siendo 100% humanos | Carga cognitiva como límite → base de [[Unidad organizacional]] |
| **Platform Engineering** | Self-service para desarrolladores | La plataforma sirve humanos, no sistemas humano-agente | Golden paths → análogo para agentes en [[Cognitive OS - Arquitectura de referencia]] |
| **BMAD-METHOD** | Roles de agentes (PM, Architect, QA) y flujos YAML para desarrollo ágil y spec-driven | Colaboración simétrica e interactiva humano-agente y gobernanza a nivel de negocio | Roles especializados de agentes y enfoque de diseño antes de codificar (spec-driven) |
| **Agent OS (Builder Methods)** | Captura, indexación y despliegue de estándares y convenciones del código para asistentes de desarrollo (Cursor, Claude Code) | Ciclo de vida de negocio completo orientado a Outcomes, métricas y límites de autonomía de gobernanza | El concepto de indexación y descubrimiento automatizado de estándares (comandos `index-standards` y `discover-standards` sobre `agent-os/standards/`) |

## Diferencia de fondo

SDLC: requerimientos, historias de usuario, desarrollo, testing, mantenimiento.
ODLC: **objetivos, outcomes, ejecución, validación, aprendizaje, memoria viva**.

ODLC no gira alrededor de backlog, historias o sprints. Gira alrededor de objetivos, evidencia, validación y aprendizaje.

## Alternativas en el Espacio de Desarrollo AI-Native

Además del modelo [[HACS]] y [[ODLC]], existen otros marcos que intentan estructurar el ciclo de vida de desarrollo de software AI-Native (o AIDLC):

1.  **GSD Core (Git. Ship. Done.)**:
    -   *Enfoque*: Una alternativa mucho más ligera y de "baja ceremonia" frente a BMAD-METHOD. Se centra en meta-prompting y en ingeniería de contexto ágil para iteraciones veloces sin el overhead de simular roles de equipos completos.
2.  **GitHub Spec Kit**:
    -   *Enfoque*: Caja de herramientas centrada en comandos rápidos (`/speckit.specify`, `/speckit.plan`, `/speckit.tasks`) integrados a la terminal o IDE para mantener al programador humano en el control absoluto de la orquestación (human-in-the-loop) en lugar de automatizar de forma multi-agente.
3.  **OpenSpec y AWS Kiro**:
    -   *Enfoque*: Especificaciones abiertas de comunicación y definición de especificaciones técnicas formateadas para el consumo óptimo por LLMs.

*Nota de verificación (2026-07-28, contra los clones de `external/`): Agent OS instala sus estándares en `agent-os/standards/` y despliega sus comandos a `.claude/commands/agent-os/` (`external/agent-os/scripts/project-install.sh:199,389`); no usa `.agent/INSTRUCTIONS.md` — esa ruta pertenece a la propuesta propia de este vault, ver [[Especificación de agentes cross-CLI]]. GSD Core se expande como "Git. Ship. Done.", no "Getting Stuff Done" (`external/gsd-core/README.md:5`). Los comandos de Spec Kit llevan el prefijo `speckit.` en la versión vigente del clon (`external/spec-kit/README.md:161-165`).*

---

## Preguntas abiertas

- ¿Cómo se *integra* ODLC con Scrum en una adopción gradual? (crítico para [[Modelo de madurez AI-Native]] niveles 1–3; ver [[Preguntas abiertas]])
- Team Topologies habla de "carga cognitiva del equipo" — ¿cómo se redefine cuando parte de la cognición es de agentes?
