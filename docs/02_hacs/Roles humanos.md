---
tags: [hacs, roles]
status: semilla
created: 2026-06-10
---

# Roles humanos

Los humanos en [[HACS]] aportan: **visión, objetivos, restricciones, ética y priorización**. No ejecutan tareas que un agente puede ejecutar con evidencia de calidad equivalente; deciden, gobiernan y validan.

| Rol | Responsabilidad (borrador) |
|---|---|
| **Sponsor** | Dueño del *por qué*: define el impacto de negocio esperado, asigna presupuesto, acepta o rechaza el resultado final contra el objetivo ([[Fase 5 - Validation]]) |
| **Product** | Dueño del *qué*: formula objetivos medibles ([[Fase 1 - Objective]]), prioriza entre objetivos en conflicto, define restricciones de producto ([[Fase 2 - Constraints]]) |
| **Architect** | Dueño del *cómo de alto nivel*: evalúa estrategias y tradeoffs ([[Fase 3 - Strategy]]), fija restricciones técnicas, aprueba decisiones de arquitectura ([[Gobernanza]]) |
| **Operator** | Dueño del *sistema en marcha*: supervisa la ejecución de agentes ([[Fase 4 - Execution]]), interviene en escalamientos, gestiona costos y límites de autonomía |

Cuando una sola persona cubre todos los roles, quien ejecuta también valida. Se acepta por escrito, compensado con las revisiones automáticas y con un validador externo para lo irreversible. A partir de dos personas, quien ejecuta no valida ([[Registro de decisiones]], D-04).

## Hipótesis

- Estos cuatro roles pueden ser menos de cuatro personas (una persona puede cubrir varios), pero **ninguno puede ser un agente**: son los puntos donde la gobernanza humana es constitutiva, no opcional.

## Preguntas abiertas

- ¿Falta un rol explícito de *Ethics/Compliance* o queda dentro de Sponsor + [[Gobernanza]]?
- ¿Cómo evoluciona la carrera profesional cuando "junior developer" deja de ser el punto de entrada? (relacionado con [[Riesgos]]: pérdida de conocimiento humano)
