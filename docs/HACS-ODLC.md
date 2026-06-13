---
tags: [moc]
status: evergreen
created: 2026-06-10
---

# HACS + ODLC — Mapa de Contenido

> **Tesis fuerte:** la unidad organizacional cambia de "equipo humano" a **sistema cognitivo humano-agente**. Lo demás (metodología, métricas, arquitectura) se deriva de eso.

## Parte I — El Problema

- [[AI SDLC]] — cómo la IA se integra en cada fase del ciclo de vida tradicional, y por qué eso no alcanza
- [[Por qué fallan las metodologías actuales]] — Scrum optimiza coordinación humana; DevOps optimiza entrega; ninguna optimiza colaboración humano-agente
- [[Nuevos cuellos de botella]] — del código al contexto, de la implementación a la decisión
- [[Más código no es más velocidad]] — la crítica de AWS al "AI coding" como métrica
- [[Comparativa con metodologías existentes]] — Scrum, SAFe, DevOps, Team Topologies, Platform Engineering
- [[Producción de software vs. velocidad real]] — qué optimiza la IA y qué no: CI/CD, testing automation, observabilidad y gobernanza de despliegue como disciplina
- [[Software bloated]] — el anti-patrón de código, dependencias y funcionalidad sobredimensionada, y por qué los agentes lo producen estructuralmente
- [[Defectos perceptuales generados por IA]] — flickering, layout shift, pérdida de foco y otros defectos UI que no aparecen en builds verdes ni capturas estáticas

## Parte II — HACS (el modelo organizacional)

- [[HACS]] — definición y componentes del sistema
- [[Unidad organizacional]] — de roles humanos a humanos + agentes + memoria + gobernanza
- [[Roles humanos]] — Sponsor, Product, Architect, Operator
- [[Roles de agentes]] — Planner, Architect, Builder, Reviewer, Security, Memory
- [[Memoria organizacional]] — qué se guarda y cómo se modela
- [[Gobernanza]] — límites de autonomía humano/agente

## Parte III — ODLC (la metodología)

- [[ODLC]] — el ciclo completo y diferencias con SDLC/Scrum
- [[Fase 1 - Objective]] → [[Fase 2 - Constraints]] → [[Fase 3 - Strategy]] → [[Fase 4 - Execution]] → [[Fase 5 - Validation]] → [[Fase 6 - Learning]]
- [[Requisitos funcionales y no funcionales]] — adaptación de la distinción clásica al modelo AI-Native, mapeo a Constraints y Gobernanza

## Parte IV — Métricas

- [[Métricas operativas]] — Objective Success Rate, Time To Outcome, Learning Velocity
- [[Métricas de agentes]] — Agent Contribution, Agent Accuracy, Agent Cost
- [[Métricas organizacionales]] — Knowledge Reuse, Context Retrieval Time, Decision Lead Time

## Parte V — Cognitive OS (la implementación)

- [[Cognitive OS - Arquitectura de referencia]] — Interfaz de Definición → Bus de Memoria → Motor de Orquestación de Agentes → Sandbox de Ejecución → Motor de Validación y Observabilidad
- [[Agent Loop Engineering]] — diseño del ciclo trigger → goal → state → action → observation → validation → memory/termination que gobierna agentes, herramientas, retries y evals
- [[Luum Cognitive OS - Implementación de referencia]] — la Safety Mesh de 14 capas que materializa la Gobernanza
- [[Caso - Alta Tienda]] — primer caso de aplicación real (métricas pendientes de evidencia)
- [[Síntesis - Economía de tokens]] — implicaciones consolidadas de los tres análisis de tokens
- [[Análisis - Stop Using Claude Without an Agentic OS]] — resumen y lecciones del Agentic OS (capas, beneficios y opciones)
- [[Análisis - Adaptando Claude Code para SDD]] — lecciones de Harness Engineering y multi-agentes en flujos SDD
- [[Análisis - Harness Engineering y la Paradoja de Herramientas]] — los tres pilares de un arnés y la degradación de contexto
- [[Análisis - La Cultura del Token]] — métricas de token por empleado, Goodhart's Law, teatro de IA y el Retorno del Token (Token ROI)
- [[Análisis - Construyendo un Arnés de IA desde Cero]] — arquitectura de bucle dual, polimorfismo, subagentes dinámicos y memoria persistente
- [[Análisis - Escasez de Tokens y la Crisis de Capacidad de la IA]] — racionamiento de tokens, peaje lingüístico, sostenibilidad del modelo de suscripción y la IA de dos velocidades
- [[Análisis - Token Economics y las 5 Predicciones del Caos]] — token poker, budgets por equipo, pair prompting y la advertencia de deuda técnica

## Parte VI — Fundacional

- [[Manifiesto HACS-ODLC]] — 6 valores, el manifiesto ODLC operativo, y adaptación sobre imposición (cherry-picking según madurez)
- [[Modelo de madurez AI-Native]] — niveles 0 a 5
- [[Glosario y taxonomía]] — Objective, Constraint, Strategy, Evidence, Memory, Agent, Governance
- [[Riesgos]] — humanos, técnicos, organizacionales
- [[Roadmap]] — v0.1 → v2.0
- [[Preguntas abiertas]] — lo que todavía no sabemos responder
- [[Nuevos roles profesionales en la era de IA]] — CAIO, AI Engineer, Context Engineer, Memory Engineer y su alineación con el modelo HACS

## Parte VII — Capacitación y Educación

- [[Cursos HACS-ODLC]] — programa formativo modular (Construcción de agentes, Arneses, Gobernanza y Ciberseguridad)

## Parte VIII — Referencias externas

> Catálogos volátiles (status `borrador` permanente): describen herramientas y repos de terceros con fecha de consulta, no fundamentos del marco.

- [[Recursos externos]] — repositorios de referencia, setup de `external/` e instrucciones de clonado
- [[Especificación de agentes cross-CLI]] — estándar de archivos de configuración de identidad y comportamiento (CLAUDE.md, SOUL.md, VOICE.md)
- [[Repositorios y catálogos de skills]] — directorios, registries públicos (skills.sh) y especificación técnica de habilidades para agentes
- [[Catálogo de herramientas y productividad]] — runtimes, orquestadores, APIs e infraestructura para productividad de desarrollo de IA
- [[AI Engineering Lab - Repositorio de referencia]] — análisis de primitivas técnicas desde cero, arquitectura limpia en producción y testing E2E con Playwright
