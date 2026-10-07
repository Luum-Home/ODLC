---
tags: [odlc, definicion]
status: borrador
created: 2026-06-10
---

# ODLC — Objective Driven Lifecycle

## Definición de trabajo

**ODLC es la metodología de trabajo de un sistema [[HACS]]: un ciclo orientado a resultados medibles que reemplaza el foco en tareas por el foco en objetivos.** El trabajo no comienza con requerimientos, tickets o historias de usuario; comienza con objetivos medibles y resultados esperados.

## El ciclo

```
Objective → Constraints → Strategy → Execution → Validation → Learning
    ↑                                                            │
    └────────────── el aprendizaje alimenta el próximo ──────────┘
```

1. [[Fase 1 - Objective]] — resultado esperado, métrica de éxito, impacto, horizonte
2. [[Fase 2 - Constraints]] — presupuesto, tecnología, regulación, seguridad, personas
3. [[Fase 3 - Strategy]] — alternativas, tradeoffs, riesgos, selección justificada
4. [[Fase 4 - Execution]] — humanos y agentes ejecutan código, tests, docs, infra, operaciones
5. [[Fase 5 - Validation]] — el resultado se valida **contra el objetivo original**, no contra la implementación
6. [[Fase 6 - Learning]] — todo resultado genera aprendizaje reutilizable, guardado en [[Memoria organizacional]]

## Diferencias con SDLC y Scrum

La comparación es contra SDLC y Scrum porque son el punto de partida más común. Kanban ya no tiene sprints y mide flujo, así que está más cerca de ODLC en cadencia; la diferencia que se mantiene es la unidad de trabajo (tarjeta vs. objetivo) y el criterio de cierre. Los valores del Manifiesto Ágil no se reemplazan: ver [[Relectura del Manifiesto Ágil]].

| | SDLC / Scrum | ODLC |
|---|---|---|
| Unidad de trabajo | Requerimiento, historia, ticket | **Objetivo medible** |
| Ejecutor | Humanos | Humanos + agentes ([[Unidad organizacional]]) |
| Éxito | Entregado / sprint completado | **Outcome validado con evidencia** |
| Conocimiento | Documentación estática | **Memoria viva** ([[Memoria organizacional]]) |
| Cierre del ciclo | Release / retro | **Learning que alimenta el próximo objetivo** |

ODLC no gira alrededor de backlog, historias o sprints. Gira alrededor de objetivos, evidencia, validación y aprendizaje. Detalle por marco: [[Comparativa con metodologías existentes]].

## Qué busca resolver

**Reducir la distancia entre intención y resultado** mediante objetivos medibles, memoria organizacional y agentes especializados. Directamente apuntado a los [[Nuevos cuellos de botella]]: comprensión, decisión, alineación, contexto y validación.

## Relacionado

[[Manifiesto HACS-ODLC]] · [[Métricas operativas]] · [[Modelo de madurez AI-Native]] (ODLC pleno = nivel 4)
