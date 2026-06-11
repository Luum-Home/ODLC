---
tags: [cursos, educacion, capacitacion]
status: borrador
created: 2026-06-10
---

# Programa de Capacitación HACS + ODLC

Este programa formativo está diseñado para educar a miembros de la organización en la adopción del modelo [[HACS]] y la metodología [[ODLC]]. El objetivo es nivelar conocimientos prácticos tanto en audiencias técnicas como no técnicas, capacitando en la creación, testeo, gobernanza y aseguramiento de agentes cognitivos.

---

## Estructura del Programa

El curso se divide en **cuatro módulos independientes** que cubren el espectro de habilidades requeridas para operar en una organización AI-Native:

```mermaid
grid-layout
  "Módulo 1: Construcción de Agentes" : "Para todo público. Diseño de identidad y comportamiento (SOUL/VOICE)."
  "Módulo 2: Ingeniería de Arneses" : "Técnico. Validación automática, sandboxes y entornos de prueba."
  "Módulo 3: Gobernanza" : "Híbrido. Límites de autonomía, auditoría y control de costos."
  "Módulo 4: Ciberseguridad Aplicada" : "Avanzado. Prompt injection, fuga de datos y seguridad en sandboxes."
```

### Módulos Formativos

1.  **[[Módulo 1 - Construcción de agentes]]**
    *   *Público objetivo*: Todo público (negocio, operaciones, producto e ingenieros).
    *   *Foco*: Aprender qué es un agente, cómo se diferencia de un chat simple, y cómo estructurar archivos de personalidad y constitución (`SOUL.md`, `VOICE.md`).
2.  **[[Módulo 2 - Ingeniería de arneses]]**
    *   *Público objetivo*: Ingenieros de software y desarrolladores de agentes.
    *   *Foco*: Diseño de arneses de prueba (Test Harness), validaciones automatizadas y ejecución en entornos seguros de Sandbox.
3.  **[[Módulo 3 - Gobernanza]]**
    *   *Público objetivo*: Líderes de producto, ingenieros y roles en transición desde marcos ágiles (Scrum Masters, DevOps).
    *   *Foco*: Establecimiento de límites de autonomía humano-agente, control presupuestario de APIs y flujos de aprobación (Human-in-the-loop).
4.  **[[Módulo 4 - Ciberseguridad aplicada]]**
    *   *Público objetivo*: Desarrolladores sénior, auditores y especialistas de seguridad.
    *   *Foco*: Identificación y mitigación de vulnerabilidades de agentes (inyección de prompts, secuestro de ejecución, sanitización de datos sensibles y PII).

---

## Serie aplicada

**[[Curso - Agentes de IA aplicados al trabajo técnico]]** · Damián, OliveX Security · 8 hs (4 encuentros)

Orientada a perfiles técnicos sin programación (infraestructura, operaciones, soporte, seguridad, QA, datos) que necesitan crear y operar agentes con herramientas comerciales y plataformas no-code. La serie técnica HACS-ODLC arriba cubre construir el sistema; esta serie cubre usarlo.

---

## Cómo utilizar este material
- **Autocapacitación**: Lee secuencialmente cada uno de los módulos en tu lector de Markdown o editor de Obsidian.
- **Talleres prácticos**: Utiliza los repositorios de referencia clonados en la carpeta `external/` (ver [[Recursos externos]]) para realizar las prácticas del Módulo 2, Módulo 3 y Módulo 4.

---
Relacionado: [[README]] · [[HACS]] · [[ODLC]] · [[Recursos externos]]
