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

La comparación es contra SDLC y Scrum porque son el punto de partida más común. Kanban no usa iteraciones de tiempo fijo y gestiona el flujo de work items, así que está más cerca de ODLC en cadencia; la diferencia que se mantiene es la unidad de trabajo (work item vs. objetivo) y el criterio de cierre (Done del workflow vs. outcome validado). Los valores del Manifiesto Ágil no se reemplazan: ver [[Relectura del Manifiesto Ágil]].

| | SDLC | Scrum (The Scrum Guide 2020) | ODLC |
|---|---|---|---|
| Unidad de trabajo | Requerimiento, ticket | Product Backlog Item, orientado a un Sprint Goal / Product Goal | **Objetivo medible** |
| Ejecutor | Humanos | Humanos (Scrum Team) | Humanos + agentes ([[Unidad organizacional]]) |
| Éxito | Entregado | Increment que cumple la Definition of Done y avanza el Sprint Goal | **Outcome validado con evidencia** |
| Conocimiento | Documentación estática | No lo define la guía | **Memoria viva** ([[Memoria organizacional]]) |
| Cierre del ciclo | Release | Sprint Review y Sprint Retrospective | **Learning que alimenta el próximo objetivo** |

ODLC no gira alrededor de backlog, historias o sprints. Gira alrededor de objetivos, evidencia, validación y aprendizaje. Detalle por marco: [[Comparativa con metodologías existentes]].

Durante la transición ODLC convive con Scrum y Kanban: reemplaza la unidad de trabajo solo en equipos que arrancan desde cero, y en equipos existentes se adopta de a poco ([[Registro de decisiones]], D-03).

## Qué busca resolver

**Reducir la distancia entre intención y resultado** mediante objetivos medibles, memoria organizacional y agentes especializados. Directamente apuntado a los [[Nuevos cuellos de botella]]: comprensión, decisión, alineación, contexto y validación.

## Relacionado

[[Manifiesto HACS-ODLC]] · [[Métricas operativas]] · [[Modelo de madurez AI-Native]] (ODLC pleno = nivel 4)
