---
tags: [cursos, educacion, capacitacion, seguridad, agentes, no-code]
status: borrador
created: 2026-06-11
autor: Damián, OliveX Security
fuente: "[[Draft Damián - Agentes de IA aplicados al trabajo técnico]]"
recibido: 2026-06-11
---

# Agentes de IA aplicados al trabajo técnico

Capacitación práctica para equipos de infraestructura, operaciones, soporte, seguridad, QA y datos.

**OliveX Security** | 8 horas (4 encuentros de 2 horas)

---

> [!note] Serie aplicada — complemento de la serie técnica
> Este curso es la **serie aplicada**: está orientada a perfiles técnicos sin experiencia en programación que trabajan con herramientas comerciales y plataformas no-code (ChatGPT, Claude, n8n, Make, Zapier, etc.).
>
> Es complementaria de la serie técnica [[Cursos HACS-ODLC]], que cubre la construcción del sistema: ingeniería de arneses, gobernanza de agentes, ciberseguridad desde código, etc.
>
> **Serie técnica** = construir el sistema. **Serie aplicada** = operar agentes con herramientas comerciales, sin programar.

---

## Resumen ejecutivo

La inteligencia artificial ya no se limita a responder preguntas. Los nuevos agentes son capaces de consultar documentación, ejecutar acciones sobre herramientas corporativas, automatizar procesos y asistir en tareas técnicas complejas.

La adopción efectiva, sin embargo, requiere más que acceso a un modelo. Los equipos necesitan aprender a diseñar agentes confiables, conectarlos a sistemas reales y, sobre todo, operarlos de forma segura.

Este curso está diseñado para que profesionales técnicos sin experiencia en programación puedan crear, evaluar y desplegar agentes útiles para su trabajo diario, aplicando criterios de seguridad en cada paso. Al finalizar, cada participante habrá construido agentes propios sobre casos reales de su organización y contará con una metodología para seguir desarrollándose de forma segura dentro de su equipo.

---

## Información general

| | |
|---|---|
| **Duración** | 8 horas (4 encuentros de 2 horas) |
| **Modalidad** | Remoto |

**Dirigido a:**
- Infraestructura
- Operaciones
- Soporte técnico
- Seguridad informática
- QA
- Datos
- Líderes técnicos

**Requisitos:**
- Cuentas de pago de ChatGPT y/o Claude (los planes gratuitos limitan GPTs, Projects y conectores).
- Acceso a documentación no sensible para las prácticas.
- Para el encuentro de herramientas: una herramienta o API de prueba del equipo y una cuenta en una plataforma no-code.
- Para el laboratorio de seguridad: un conjunto de datos de prueba en un entorno aislado.

---

## Objetivos de aprendizaje

Al finalizar el curso, los participantes podrán:

- Comprender cómo funcionan los modelos de IA modernos y cuáles son sus limitaciones.
- Diseñar prompts robustos y reutilizables.
- Crear agentes con conocimiento propio usando documentación corporativa.
- Automatizar tareas operativas mediante herramientas no-code.
- Conectar agentes con sistemas y servicios externos.
- Evaluar calidad, costos y riesgos asociados.
- Aplicar controles de seguridad específicos para agentes de IA en cada etapa.
- Construir agentes seguros y listos para uso interno.

---

## Metodología

El curso combina **30% de conceptos y fundamentos** con **70% de práctica aplicada**. Cada encuentro dura 2 horas, con aproximadamente 30 minutos de concepto y 90 minutos de taller. El cuarto encuentro funciona como jornada de práctica integradora.

**Método de trabajo:** Construir → Probar → Asegurar → Mejorar

La seguridad no se concentra en una sola clase: aparece como un cierre concreto en cada encuentro. Después de construir algo, se aplica el control de seguridad que corresponde a esa etapa. Los participantes trabajan sobre tareas reales de su entorno mientras construyen un agente que evoluciona durante toda la capacitación, y cada clase concluye con un entregable que pasa a formar parte del proyecto final.

---

## Programa

### Encuentro 1 — Fundamentos y primer agente

**Objetivo:** comprender el funcionamiento práctico de los modelos actuales y construir el primer asistente sobre información real.

**Contenidos:**
- Cómo funcionan los modelos de lenguaje: contexto, memoria, alucinaciones y límites.
- Chatbot vs. asistente vs. agente.
- Panorama de modelos a 2026: ChatGPT, Claude, Gemini y Codex (el Codex 2026 es un agente, distinto del modelo de 2021).
- Criterios para seleccionar la herramienta según el caso.

**Taller:**
- Identificación de oportunidades de automatización en el área propia.
- Creación de un primer asistente basado en documentación real.
- Comparación de resultados entre dos modelos.

> **Cómo hacerlo seguro:** clasificar la documentación antes de cargarla y definir qué información nunca va al agente, entendiendo que todo lo que entra al contexto puede salir.

**Entregable:**
- Primer asistente funcional.
- Mapa inicial de oportunidades de automatización.

---

### Encuentro 2 — Prompting seguro y agentes con conocimiento propio

**Objetivo:** diseñar instrucciones consistentes y transformar el asistente en un activo con conocimiento corporativo.

**Contenidos:**
- Anatomía de un prompt robusto: rol, contexto, restricciones, formato y ejemplos.
- Técnicas: few-shot, descomposición de tareas, razonamiento paso a paso y salida estructurada.
- Interacción, evaluación y errores frecuentes.
- GPTs personalizados, Claude Projects e instrucciones de sistema.
- Conocimiento propio e introducción a RAG; técnicas para reducir alucinaciones y trazabilidad de respuestas.

**Taller:**
- Conversión de una tarea real en un prompt maestro reutilizable, probado en dos modelos.
- Construcción de un agente con runbooks, procedimientos, políticas, FAQs y documentación técnica.

> **Cómo hacerlo seguro:** no incluir credenciales ni secretos en los prompts, escribir instrucciones que el agente respete aunque le pidan lo contrario, y controlar el acceso y la curaduría de la base de conocimiento —definiendo quién ve qué y usando solo fuentes confiables.

**Entregable:**
- Prompt maestro versionado y biblioteca inicial de prompts.
- Agente con conocimiento corporativo.

---

### Encuentro 3 — Herramientas, MCP, automatización y operación

**Objetivo:** permitir que los agentes ejecuten acciones sobre sistemas reales y dejarlos listos para operar.

**Contenidos:**
- Introducción a MCP (Model Context Protocol): arquitectura y casos de uso. Ver también [[Módulo 4 - Ciberseguridad aplicada]] para los aspectos de seguridad en servidores MCP.
- Herramientas no-code: n8n, Make, Zapier, Lindy y Botpress.
- Introducción a Claude Code y Codex para tareas de sistemas.
- Integración con APIs y herramientas corporativas.
- Operación: human-in-the-loop (ver [[Glosario y taxonomía]]), observabilidad, costos y consumo de tokens, versionado.

**Taller:**
- Conexión de un agente a un sistema externo y construcción de un flujo automatizado.
- Dejar el agente monitoreado, acotado y versionado.

> **Cómo hacerlo seguro:** aplicar mínimo privilegio en los conectores, allowlist de herramientas y dominios, aprobación humana para acciones irreversibles y verificación del origen de los servidores MCP. Ningún agente con autoaprobación ciega; límites operativos y de costo como control.

**Entregable:**
- Agente conectado a herramientas reales, monitoreado y documentado.

---

### Encuentro 4 — Seguridad, evaluación y laboratorio integrador

**Objetivo:** evaluar y blindar los agentes construidos y consolidar el proyecto final en una jornada de práctica.

**Contenidos:**
- Nuevo modelo de amenazas de los agentes de IA.
- Prompt injection y prompt injection indirecta, tool poisoning, knowledge poisoning, data exfiltration y confused deputy. Ver [[Módulo 4 - Ciberseguridad aplicada]] para el tratamiento técnico de estas vulnerabilidades.
- Seguridad en MCP, mínimo privilegio, sandboxing, logging y auditoría.
- Gobierno y control operativo de agentes.

**Taller:**
- Evaluación de seguridad de los propios agentes contra un checklist, sobre datos de prueba en un entorno aislado.
- Identificación de riesgos, aplicación de mitigaciones y refuerzo de los agentes.
- Cierre y presentación del proyecto final integrador.

> **Cómo hacerlo seguro:** toda la evaluación se corre sobre datos de prueba y en sandbox, nunca sobre información real, para no exponer nada durante el ejercicio.

**Entregable:**
- Informe de hallazgos y checklist de seguridad.
- Agentes reforzados y proyecto final funcional.

---

## Proyecto final

Durante toda la capacitación los participantes construyen un agente propio basado en una necesidad real de su área. El proyecto integra conocimiento corporativo, automatización, herramientas externas, controles de seguridad y documentación operativa. Al finalizar el curso, cada participante cuenta con una solución funcional y segura, lista para evolucionar dentro de su equipo.

---

## Entregables

### Para cada participante

- Agente funcional.
- Biblioteca de prompts reutilizables.
- Flujo automatizado.
- Documentación técnica.
- Checklist de seguridad.

### Para la organización

- Catálogo inicial de agentes.
- Guía de adopción de IA.
- Mapa de herramientas recomendadas.
- Guía de seguridad para agentes.
- Backlog de automatizaciones identificadas.

---

## Beneficios para la organización

- Reducción de tareas repetitivas.
- Mayor velocidad de acceso al conocimiento interno.
- Mejor aprovechamiento de las herramientas de IA existentes.
- Incorporación de criterios de seguridad desde el diseño.
- Creación de capacidades internas sostenibles.
- Primeros casos de uso implementados durante la capacitación.

La propuesta está orientada a generar resultados tangibles desde la primera semana y a dejar capacidades instaladas dentro de los equipos, más allá del uso puntual de una herramienta específica.

---

Relacionado: [[Cursos HACS-ODLC]] · [[Draft Damián - Agentes de IA aplicados al trabajo técnico]] · [[Módulo 4 - Ciberseguridad aplicada]] · [[Glosario y taxonomía]]
