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

## Diferencia de fondo

SDLC: requerimientos, historias de usuario, desarrollo, testing, mantenimiento.
ODLC: **objetivos, outcomes, ejecución, validación, aprendizaje, memoria viva**.

ODLC no gira alrededor de backlog, historias o sprints. Gira alrededor de objetivos, evidencia, validación y aprendizaje.

## Preguntas abiertas

- ¿Cómo se *integra* ODLC con Scrum en una adopción gradual? (crítico para [[Modelo de madurez AI-Native]] niveles 1–3; ver [[Preguntas abiertas]])
- Team Topologies habla de "carga cognitiva del equipo" — ¿cómo se redefine cuando parte de la cognición es de agentes?
