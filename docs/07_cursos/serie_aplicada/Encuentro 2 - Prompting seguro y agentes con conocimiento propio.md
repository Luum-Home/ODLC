---
tags: [cursos, educacion, capacitacion, seguridad, agentes, no-code, serie-aplicada]
status: borrador
created: 2026-06-11
autor: Damián, OliveX Security
fuente: "[[Draft Damián - Agentes de IA aplicados al trabajo técnico]]"
---

# Encuentro 2 — Prompting seguro y agentes con conocimiento propio

**Serie aplicada · OliveX Security** | Encuentro 2 de 4 · 2 horas

← [[Encuentro 1 - Fundamentos y primer agente|Encuentro anterior]] · [[Curso - Agentes de IA aplicados al trabajo técnico|Índice del curso]]

---

## Objetivo

Diseñar instrucciones consistentes y transformar el asistente en un activo con conocimiento corporativo.

---

## Contenidos

- Anatomía de un prompt robusto: rol, contexto, restricciones, formato y ejemplos.
- Técnicas: few-shot, descomposición de tareas, razonamiento paso a paso y salida estructurada.
- Interacción, evaluación y errores frecuentes.
- GPTs personalizados, Claude Projects e instrucciones de sistema.
- Conocimiento propio e introducción a RAG; técnicas para reducir alucinaciones y trazabilidad de respuestas.
- Gestión de memoria y contexto: diferencia entre ventana de contexto y base de conocimiento.
  - **Ventana de contexto**: memoria de trabajo; lo que el agente tiene “en la cabeza” durante la conversación.
  - **Base de conocimiento**: biblioteca; el lugar al que el agente va a buscar información cuando necesita recuperar contenido externo.

---

## Taller

- Conversión de una tarea real en un prompt maestro reutilizable, probado en dos modelos.
- Construcción de un agente con runbooks, procedimientos, políticas, FAQs y documentación técnica.

---

> **Cómo hacerlo seguro:** no incluir credenciales ni secretos en los prompts, escribir instrucciones que el agente respete aunque le pidan lo contrario (ver [[Módulo 4 - Ciberseguridad aplicada]] para el tratamiento técnico de [[Módulo 4 - Ciberseguridad aplicada|prompt injection]]), y controlar el acceso y la curaduría de la base de conocimiento —definiendo quién ve qué y usando solo fuentes confiables.

---

## Entregables

- Prompt maestro versionado y biblioteca inicial de prompts.
- Agente con conocimiento corporativo.

---

Encuentro anterior: [[Encuentro 1 - Fundamentos y primer agente]]
Siguiente encuentro: [[Encuentro 3 - Herramientas, MCP, automatización y operación]]
← [[Curso - Agentes de IA aplicados al trabajo técnico|Índice del curso]]
