---
tags: [problema, hipotesis]
status: borrador
created: 2026-06-10
---

# Por qué fallan las metodologías actuales

## Hipótesis

- **Scrum optimiza coordinación humana.** Backlog, historias, sprints y ceremonias existen para sincronizar personas con ancho de banda limitado.
- **DevOps optimiza entrega.** CI/CD, automatización de infra y feedback loops acortan el camino del commit a producción.
- **Ninguna optimiza la colaboración humano-agente.** Todas asumen que el trabajo lo producen exclusivamente humanos y que las herramientas son pasivas.

Los modelos actuales de trabajo fueron diseñados para equipos compuestos exclusivamente por humanos.

## Situación actual vs. señales del cambio

**Situación que asumen las metodologías:** los humanos producen el código, ejecutan los análisis, generan la documentación, realizan las pruebas y toman todas las decisiones operativas.

**Señales de cambio ya visibles:** generación automática de código, agentes de revisión, agentes de testing, agentes de documentación, agentes de operaciones, agentes de arquitectura.

## Cambio de paradigma

| Modelo | Flujo |
|---|---|
| Tradicional | Humanos → Herramientas → Resultado |
| AI-Assisted | Humanos → IA Asistiva → Herramientas → Resultado |
| Human-Agent | Humanos → Agentes Autónomos → Herramientas → Resultado |

La IA cambia el costo de ejecución, pero los cuellos de botella permanecen en contexto, decisiones, alineación, validación y aprendizaje → [[Nuevos cuellos de botella]].

## Evidencia

> ⚠️ Pendiente: esta sección necesita datos reales (estudios DORA, casos propios, postmortems). Hoy la hipótesis se sostiene en observación directa, no en evidencia formal.

## Preguntas abiertas

- ¿Falla Scrum, o falla *Scrum aplicado a equipos con agentes*? ¿Es reemplazo o extensión? (ver [[Preguntas abiertas]])
- ¿Qué partes de Scrum/DevOps sobreviven dentro de [[ODLC]]?

Relacionado: [[Comparativa con metodologías existentes]], [[HACS]]
