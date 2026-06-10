---
tags: [casos, alta-tienda, odlc, hacs]
status: borrador
created: 2026-06-10
---

# Caso — Alta Tienda

Este caso de estudio documenta la primera aplicación real del marco **HACS** y la metodología **ODLC** en **Alta Tienda**, una plataforma de comercio electrónico de rápido crecimiento en América Latina. El objetivo fue rediseñar y automatizar el proceso de alta y verificación de comercios (KYC y pasarelas de pago).

---

## 1. El Problema (Contexto Inicial)
El onboarding de nuevos vendedores en Alta Tienda requería 5 días promedio. El flujo implicaba revisión manual de documentación legal, verificación fiscal y configuraciones complejas de pasarelas de pago. Este cuello de botella limitaba la velocidad de adquisición de clientes y cargaba operativamente al equipo humano de soporte.

---

## 2. Aplicación del Ciclo ODLC

### [[Fase 1 - Objective|Fase 1: Objective]]
- **Declaración**: Automatizar la validación de documentación legal y la configuración de pasarelas de pago para nuevos comercios en Alta Tienda.
- **Métrica de Éxito**: Reducir el tiempo promedio de onboarding de 5 días a menos de 24 horas (para el 90% de los comercios).
- **Horizonte**: 3 semanas para desarrollo y validación en producción.

### [[Fase 2 - Constraints|Fase 2: Constraints]]
- **Presupuesto**: Máximo de $1,500 USD en costos de tokens de modelos de lenguaje durante el ciclo.
- **Técnicas**: No alterar el esquema principal de la base de datos de usuarios. Cumplir con normativas PCI en el manejo de credenciales de pago.
- **Gobernanza**: Todo comercio rechazado por fraude debe pasar a revisión por un operador humano para evitar falsos positivos automatizados.

### [[Fase 3 - Strategy|Fase 3: Strategy]]
Se evaluaron tres alternativas en el orquestador:
- *Alternativa A*: Refactorizar el flujo usando validadores externos SaaS (Costo alto, integración rígida).
- *Alternativa B*: Crear un microservicio con agentes especializados ([[Roles de agentes]]) integrados a la arquitectura de referencia de [[Cognitive OS - Arquitectura de referencia]] para analizar documentos legales mediante OCR inteligente y configurar APIs de pasarelas.
- *Decisión*: Se seleccionó la **Alternativa B** debido a su bajo costo operativo proyectado y flexibilidad para adaptarse a cambios regulatorios futuros de forma autónoma.

### [[Fase 4 - Execution|Fase 4: Execution]]
- El agente **Planner** estructuró las tareas de desarrollo de código del microservicio.
- El agente **Builder** generó el código en Python para la ingesta de documentos y la integración con la API de OpenAI (GPT-4o).
- El agente **Reviewer** identificó una vulnerabilidad de inyección de prompts en el módulo de extracción de datos del PDF y propuso un fix.
- Los humanos supervisaron los Pull Requests y autorizaron el despliegue al Sandbox de ejecución y posteriormente a staging.

### [[Fase 5 - Validation|Fase 5: Validation]]
Se procesaron 250 comercios de prueba en staging y luego se liberó al 10% del tráfico en producción.
- **Resultado Real**: El tiempo promedio de verificación y alta bajó a **2.3 horas** (superando la meta de <24h).
- **Evidencia**: Tasa de acierto del 96.4% en OCR de documentos. Solo un 3.6% de los comercios requirió fallback manual humano por documentos borrosos.
- **Objective Success Rate (OSR)**: 100% (el objetivo de negocio se cumplió y validó con datos).

### [[Fase 6 - Learning|Fase 6: Learning]]
Se registraron tres aprendizajes en la [[Memoria organizacional]]:
1. **Validado**: Los modelos LLM multimodales son altamente precisos analizando PDFs notariales, pero fallan si el contraste de la foto de la identificación es bajo.
2. **Decisión Descartada**: Se descartó la re-verificación automática de documentos fallidos. Es más barato y rápido enviarlos directamente al operador humano que reintentar con otro prompt.
3. **Reutilizable**: Estructura de validación segura para prompts de extracción de datos que se subió al catálogo de código del Cognitive OS.

---

## 3. Impacto en Métricas Organizacionales
- **Context Retrieval Time (CRT)**: Cayó a 5 minutos para el agente Builder, ya que el contexto histórico de la API de Alta Tienda estaba indexado en la memoria semántica.
- **Time To Outcome (TTO)**: Completado en 16 días totales desde la formulación de la hipótesis hasta el 10% en producción.
- **Agent Contribution Ratio (ACR)**: 82% del código y scripts de testeo fueron redactados y validados autónomamente por agentes.

---
Relacionado: [[HACS]] · [[ODLC]] · [[Métricas operativas]] · [[Cognitive OS - Arquitectura de referencia]]
