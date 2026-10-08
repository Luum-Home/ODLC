---
tags: [metricas, organizacion, hacs]
status: borrador
created: 2026-06-10
---

# Métricas organizacionales

Las **métricas organizacionales** evalúan la salud del flujo de información, la reusabilidad del conocimiento y la velocidad de toma de decisiones estratégicas dentro de la estructura completa de [[HACS]]. Estas métricas no miden al agente individual ni el resultado de un solo objetivo, sino la eficiencia colectiva y la capacidad de la organización para operar como un sistema cognitivo distribuido.

> [!note] KRR y CRT fuera del núcleo
> El Knowledge Reuse Rate y el Context Retrieval Time quedan fuera del [[Núcleo ODLC para tiny teams]] y se mantienen como referencia para empresas. Su rediseño se pospone: el mandato de la decisión D1 invita a inflar el KRR (Goodhart) y el CRT se superpone con el Decision Lead Time ([[Registro de decisiones]], D-10).

## 1. Knowledge Reuse Rate (KRR)

Mide el grado en que los nuevos objetivos capitalizan la [[Memoria organizacional]] existente (ADRs, postmortems, lecciones aprendidas) en lugar de resolver problemas desde cero.

$$KRR = \frac{\text{Decisiones y lecciones en memoria referenciadas en nuevos objetivos}}{\text{Total de decisiones estratégicas tomadas}}$$

### Importancia
- Un KRR bajo indica "amnesia organizacional", donde humanos y agentes repiten los mismos errores o reescriben soluciones arquitectónicas previamente descartadas.
- Un KRR alto refleja que la [[Fase 6 - Learning]] está alimentando efectivamente la [[Fase 3 - Strategy]] de los ciclos siguientes.

---

## 2. Context Retrieval Time (CRT)

Mide el tiempo necesario para indexar, buscar y consolidar el contexto histórico requerido antes de iniciar la ejecución de un nuevo objetivo.

$$CRT = T_{\text{contexto listo para ejecución}} - T_{\text{aprobación del objetivo}}$$

### Optimización en HACS
- En equipos tradicionales, el CRT es alto y fragmentado (reuniones de onboarding, lectura de wikis desactualizados, chats en Slack).
- En HACS, el agente Memory y las herramientas de Cognitive OS deben reducir el CRT a minutos u horas mediante la automatización de búsquedas vectoriales y síntesis de grafos de conocimiento.

---

## 3. Decision Lead Time (DLT)

Mide el tiempo que tarda la unidad HACS desde que se define un objetivo con sus restricciones hasta que se elige y aprueba formalmente la estrategia de ejecución.

$$DLT = T_{\text{aprobación de estrategia}} - T_{\text{definición de restricciones}}$$

### Comportamiento del DLT
- Mide la eficiencia de la [[Fase 3 - Strategy]].
- Si el DLT es demasiado alto, indica parálisis por análisis o fallos en la gobernanza humano-agente para arbitrar alternativas contradictorias.
- Si el DLT es demasiado bajo, puede significar una falta de exploración de alternativas de diseño críticas, derivando en mayor retrabajo posterior.

---

## Instrumentación pendiente

Como en [[Métricas operativas]] y [[Métricas de agentes]], las fórmulas están definidas pero **la recolección del dato no**. Falta, para cada una, fuente del evento, unidad y responsable del registro.

| Métrica | Qué falta definir |
|---|---|
| **KRR** | Qué cuenta como **"referenciar" una entrada de memoria**: si es una cita explícita en el documento de estrategia, un enlace, o una recuperación registrada por el agente Memory. La diferencia importa porque la recuperación automática puede inflar el numerador sin que la lección haya influido en la decisión. Falta también qué califica como "decisión estratégica" en el denominador. |
| **CRT** | Los **timestamps** de inicio y fin, y sobre todo qué significa "contexto listo para ejecución" — hoy no hay un evento observable que lo marque. En el modo tradicional que la nota usa como comparación (reuniones, lectura de wikis), ese tiempo directamente no se registra en ningún sistema, así que la comparación con HACS no tiene línea base. |
| **DLT** | Dónde se registran la **aprobación formal de la estrategia** y la definición de restricciones. La nota interpreta valores altos y bajos del DLT en sentidos opuestos (parálisis por análisis vs. falta de exploración), pero sin un rango de referencia calibrado esa lectura queda a criterio de quien mire el número. |

## Hipótesis

- **H1**: Aumentar el KRR disminuye directamente el *Time To Outcome* (TTO) de los objetivos complejos, ya que se evitan debates de diseño redundantes.
- **H2**: La automatización de la curaduría de memoria por parte del agente Memory disminuye el CRT de forma lineal con el paso de los ciclos.

## Decisiones

- **D1**: Se requerirá que cada propuesta de estrategia en la [[Fase 3 - Strategy]] referencie explícitamente al menos una entrada previa de la [[Memoria organizacional]] (ADR o postmortem) para garantizar el uso activo del conocimiento acumulado.

## Preguntas abiertas

- ¿Cómo medir el valor cuantitativo (ROI) de evitar que se cometa un error gracias a una lección archivada en memoria?
- ¿Cómo se escala el CRT cuando el repositorio y el histórico de decisiones crecen exponencialmente?

---
Relacionado: [[Memoria organizacional]] · [[Fase 3 - Strategy]] · [[README]] · [[Nuevos cuellos de botella]]
