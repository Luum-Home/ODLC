---
tags: [casos, odlc, hacs]
status: borrador
created: 2026-06-10
---

# Caso — Onboarding de comercios

Este caso **ilustrativo** muestra cómo se aplicarían el marco **HACS** y la metodología **ODLC** en un cliente de e-commerce que quiere rediseñar y automatizar el alta y verificación de comercios (KYC y configuración de pasarelas de pago).

> [!warning] Estado de la evidencia
> Este caso no tiene mediciones: no hay logs, dashboards ni queries que respalden resultados. Sirve como ejemplo de cómo se recorre el ciclo, no como evidencia de que funcione — exactamente la distinción que exige [[Fase 5 - Validation]] (Evidence over Opinions).

---

## 1. El problema (contexto inicial)
El onboarding de nuevos vendedores tarda días. El flujo implica revisión manual de documentación legal, verificación fiscal y configuraciones complejas de pasarelas de pago. Ese cuello de botella limita la velocidad de adquisición de comercios y carga al equipo humano de soporte.

---

## 2. Aplicación del ciclo ODLC

### [[Fase 1 - Objective|Fase 1: Objective]]
- **Declaración**: bajar el tiempo de onboarding de días a menos de un día para la gran mayoría de los comercios.
- **Métrica de éxito**: un percentil alto (p. ej. p90) del tiempo de onboarding por debajo del umbral fijado, no un promedio.
- **Horizonte**: un ciclo corto, de pocas semanas, para desarrollo y validación en producción.

### [[Fase 2 - Constraints|Fase 2: Constraints]]
- **Presupuesto**: un tope explícito de gasto en tokens para el ciclo.
- **Técnicas**: no alterar el esquema principal de la base de usuarios; cumplir la normativa aplicable al manejo de credenciales de pago.
- **Gobernanza**: todo comercio rechazado por fraude pasa a revisión de un operador humano, para evitar falsos positivos automatizados.

### [[Fase 3 - Strategy|Fase 3: Strategy]]
Se evalúan dos alternativas:
- *Alternativa A*: refactorizar el flujo usando validadores externos SaaS (costo alto, integración rígida).
- *Alternativa B*: un servicio con agentes especializados ([[Roles de agentes]]) integrados al arnés del equipo, que analizan documentos legales con OCR asistido por un modelo multimodal y configuran las APIs de pasarelas.
- *Decisión*: la **Alternativa B**, por menor costo operativo proyectado y flexibilidad ante cambios regulatorios.

### [[Fase 4 - Execution|Fase 4: Execution]]
- El agente **Planner** estructura las tareas de desarrollo del servicio.
- El agente **Builder** genera el código de ingesta de documentos y la integración con el modelo.
- El agente **Reviewer** detecta una vulnerabilidad de inyección de prompts en la extracción de datos del PDF y propone un fix.
- Los humanos supervisan los Pull Requests y autorizan el despliegue al sandbox y después a staging.

### [[Fase 5 - Validation|Fase 5: Validation]]
Se procesa un lote de comercios de prueba en staging y después se libera a un porcentaje chico del tráfico en producción.
- **Resultado**: hay que medir el mismo percentil que fijó el objetivo. Si solo se registra el promedio, la meta queda sin verificar.
- **Evidencia**: tasa de acierto del OCR y porcentaje de comercios que caen al fallback manual, con la fuente de cada número.
- **Objective Success Rate (OSR)**: solo determinable si la métrica registrada es la misma que se declaró en la Fase 1.

### [[Fase 6 - Learning|Fase 6: Learning]]
Aprendizajes del tipo que se registran en la [[Memoria organizacional]]:
1. **Validado**: los modelos multimodales leen bien PDFs de documentación legal, pero fallan con fotos de identificación de bajo contraste.
2. **Decisión descartada**: reintentar automáticamente la verificación de documentos fallidos. Sale más barato y rápido derivarlos al operador humano que reintentar con otro prompt.
3. **Reutilizable**: una estructura de validación segura para prompts de extracción de datos, subida al catálogo de skills del equipo.

---

## 3. Impacto en métricas organizacionales
Cómo se leerían las métricas del marco en un caso así (sin valores: no hay medición):
- **Context Retrieval Time (CRT)**: necesita una línea base previa para comparar.
- **Time To Outcome (TTO)**: se cuenta desde la definición del objetivo hasta el outcome validado; un despliegue parcial sin validación no lo cierra.
- **Agent Contribution Ratio (ACR)**: proporción del código y los scripts de testeo redactados y validados por agentes, medida sobre los PRs.

---
Relacionado: [[HACS]] · [[ODLC]] · [[Métricas operativas]] · [[Gobernanza]]
