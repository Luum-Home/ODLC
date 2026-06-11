---
tags: [metricas, operaciones, odlc]
status: borrador
created: 2026-06-10
---

# Métricas operativas

Las **métricas operativas** en [[ODLC]] evalúan la efectividad general del ciclo de vida de desarrollo de software desde una perspectiva de negocio y eficiencia de entrega. A diferencia de las métricas ágiles tradicionales (como la velocidad del Sprint en Story Points o las horas trabajadas), las métricas operativas de ODLC se centran en el valor entregado y en la capacidad de aprendizaje continuo del sistema [[HACS]].

## 1. Objective Success Rate (OSR)

El **Tasa de Éxito de Objetivos** mide la proporción de objetivos definidos que se cumplen satisfactoriamente en la validación final.

$$OSR = \frac{\text{Objetivos validados con éxito}}{\text{Total de objetivos iniciados}}$$

### Detalles de implementación
- Se calcula de forma binaria al final de la [[Fase 5 - Validation]] utilizando la [[Glosario y taxonomía#4. Evidence (Evidencia)|Evidencia]] recolectada.
- Un objetivo es exitoso solo si la métrica de éxito definida en la [[Fase 1 - Objective]] alcanza el umbral acordado bajo las [[Fase 2 - Constraints]] establecidas.
- Si el objetivo se entrega pero no se cumplen las métricas de negocio esperadas, se considera una desviación y cuenta como un fallo en la OSR (aunque el código esté en producción).

---

## 2. Time To Outcome (TTO)

El **Tiempo hasta el Resultado** mide el tiempo total transcurrido desde la formalización de un objetivo hasta la validación y obtención del resultado de negocio esperado.

$$TTO = T_{\text{validación del outcome}} - T_{\text{definición del objetivo}}$$

### Diferencia con Lead Time / Cycle Time
- El *Cycle Time* tradicional mide desde que se empieza a codificar una tarea hasta que se despliega.
- El *TTO* incluye la investigación estratégica inicial ([[Fase 3 - Strategy]]), la ejecución de desarrollo e infraestructura ([[Fase 4 - Execution]]) y, fundamentalmente, el tiempo en producción necesario para recolectar la evidencia de validación de negocio.

---

## 3. Learning Velocity (LV)

La **Velocidad de Aprendizaje** mide el ritmo de absorción e integración de nuevo conocimiento en la [[Memoria organizacional]] de la empresa.

$$LV = \frac{\text{Lecciones validadas e integradas en memoria}}{\text{Ciclos de objetivos completados}}$$

### Detalles de implementación
- Proviene directamente de la [[Fase 6 - Learning]].
- No todo aprendizaje es válido; para computar en la métrica, la lección debe catalogarse como conocimiento reutilizable en formato de "decisiones validadas/descartadas" o "patrones de diseño actualizados".

---

## Hipótesis

- **H1**: Centrar las métricas en OSR en lugar de "cantidad de código" o "tickets cerrados" reduce el desperdicio y la deuda técnica (en línea con la crítica de AWS: [[Más código no es más velocidad]]).
- **H2**: Un TTO corto correlaciona directamente con una alta madurez del sistema adaptativo de agentes.

## Decisiones

- **D1**: Se descarta el uso de Story Points o estimaciones basadas en esfuerzo humano como métricas operativas principales. La única medida de progreso válida es la proximidad al resultado.

## Preguntas abiertas

- ¿Cómo medir objetivos que requieren largos períodos de observación (ej. métricas de retención de usuarios a 3 meses) sin congelar el ciclo ODLC?
- ¿Cómo ponderar el impacto de factores externos incontrolables (ej. caídas de mercado) en la OSR de un equipo HACS?

---
Relacionado: [[Métricas de agentes]] · [[Métricas organizacionales]] · [[Fase 5 - Validation]]
