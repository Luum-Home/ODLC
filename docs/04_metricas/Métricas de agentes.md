---
tags: [metricas, agentes, hacs]
status: borrador
created: 2026-06-10
---

# Métricas de agentes

Las **métricas de agentes** evalúan el desempeño, la eficiencia y el costo de los agentes autónomos de software que forman parte de la unidad cognitiva [[HACS]]. Estas métricas son fundamentales para balancear la autonomía de los agentes con la supervisión humana, asegurando que los agentes actúen como multiplicadores de capacidad en lugar de generadores de ruido o retrabajo.

## 1. Agent Contribution Ratio (ACR) & Human Leverage Ratio (HLR)

Miden la proporción de tareas del ciclo de vida completadas por agentes frente a las completadas por humanos.

- **ACR (Tasa de Contribución de Agentes)**: El porcentaje de artefactos (líneas de código, pruebas, diagramas de arquitectura, documentación, scripts de despliegue) producidos y consolidados por agentes.
  
  $$ACR = \frac{\text{Artefactos aprobados generados por agentes}}{\text{Total de artefactos consolidados}}$$

- **HLR (Tasa de Apalancamiento Humano)**: Mide el volumen de resultados de negocio validados que un humano es capaz de coordinar y gobernar por unidad de tiempo.
  
  $$HLR = \frac{\text{Nº de objetivos validados con éxito (numerador de la OSR)}}{\text{Horas de intervención humana, en la misma ventana}}$$

Un HLR alto indica que los humanos se dedican a definir objetivos, evaluar estrategias y gobernar, delegando la ejecución repetitiva en los agentes.

---

## 2. Agent Accuracy (Tasa de Precisión / Retrabajo)

Mide la calidad del trabajo autónomo y la necesidad de intervención o corrección humana.

$$\text{Rework Rate} = \frac{\text{Artefactos de agentes rechazados o modificados por humanos}}{\text{Total de artefactos generados por agentes}}$$

### Rangos de Referencia:

> [!warning] Umbrales sin base empírica
> Los tres valores de abajo (10%, 30%, 40%) son una **heurística inicial**, no un resultado medido: no provienen de un estudio, un benchmark ni de datos históricos del equipo. Se documentan como punto de partida para poder discutirlos, y quedan **pendientes de calibrar** contra retrabajo real una vez que la métrica se instrumente. El caso más delicado es el 40%: dispara una regla ejecutable (suspender un agente, D1) y se replica en [[Gobernanza]], de modo que recalibrarlo obliga a actualizar los dos lugares.

- **Precisión Óptima (Rework < 10%)**: El agente opera de forma fluida. Sus decisiones están bien alineadas con las [[Fase 2 - Constraints]] y la [[Memoria organizacional]].
- **Señal de degradación (Rework > 30%)**: Los humanos actúan constantemente como correctores detallados de código o diseño. Indica desalineación de contexto o limitaciones del modelo LLM. Acción: revisar el arnés y el contexto del agente.
- **Umbral de suspensión (Rework > 40% sostenido por 3 objetivos consecutivos)**: Se activa la Decisión D1 — ver sección Decisiones.

En trabajos de frontend, el *Rework Rate* debe incluir defectos perceptuales aunque no rompan el build: flickering, layout shift, pérdida de foco, estados loading/empty/error inconsistentes, regresiones responsive y fallas básicas de accesibilidad. Ver [[Defectos perceptuales generados por IA]].

---

## 3. Agent Cost (Costo y Eficiencia de Agentes)

Evalúa la eficiencia financiera del uso de agentes.

$$\text{Costo por Objetivo} = \text{Costo de APIs de LLMs} + \text{Cómputo en Sandbox} + \text{Almacenamiento de Memoria}$$

A diferencia del costo de salarios humanos, el costo de agentes es altamente elástico y escalable. Sin embargo, loops infinitos o la falta de límites de ejecución pueden disparar los costos sin agregar valor.

---

## Instrumentación pendiente

Las fórmulas de arriba están definidas; **la instrumentación no**. Ninguna de estas métricas declara todavía de qué evento sale el dato, con qué herramienta se recolecta ni quién lo registra, así que hoy no son medibles de forma reproducible: dos personas midiendo el mismo ciclo obtendrían números distintos. Se deja explícito qué falta, en vez de asumir que la fórmula alcanza.

| Métrica | Qué falta definir |
|---|---|
| **ACR** | Una **unidad común de "artefacto"**. Hoy la definición mezcla líneas de código, pruebas, diagramas, documentación y scripts de despliegue, que no son conmensurables: un diagrama no equivale a 200 líneas. Falta decidir si se cuenta por artefacto discreto (PR, archivo, documento) o si se pondera, y de dónde sale el conteo (¿autoría de commits? ¿etiquetas en el PR?). Falta también el criterio de atribución cuando el artefacto es mixto (agente genera, humano corrige). |
| **HLR** | Cómo se contabiliza una **hora de intervención humana**: si es tiempo de reloj, tiempo imputado, o tiempo activo sobre la herramienta; si incluye definir el objetivo y gobernar, o solo corregir al agente; y quién lo registra (¿imputación manual? ¿telemetría del IDE?). Sin esa definición el denominador es arbitrario. |
| **Rework Rate** | Qué cuenta como **"modificado por un humano"** y con qué granularidad (¿un typo corregido es retrabajo?), sobre qué ventana se mide, y de qué fuente sale el evento (¿diffs sobre el commit del agente? ¿estados del PR?). Se cruza con la pregunta abierta de distinguir corrección constructiva de corrección por error. |
| **Costo por Objetivo** | Cómo se **atribuye el gasto a un objetivo**: falta una clave de correlación entre las llamadas a la API, el cómputo de Sandbox y el almacenamiento de memoria, por un lado, y el objetivo que los originó, por el otro. Sin esa trazabilidad solo se puede medir el costo agregado del equipo, no el de un ciclo. |

Instrumentar esto es requisito para calibrar los umbrales de la sección anterior: hasta entonces, los números de esta nota son hipótesis de trabajo, no mediciones.

## Hipótesis

- **H1**: Aumentar el ACR sin monitorear el *Rework Rate* disminuye la velocidad general del equipo debido a cuellos de botella en la revisión humana (ver [[Más código no es más velocidad]]).
- **H2**: A medida que madura la [[Memoria organizacional]], el *Rework Rate* de los agentes disminuye drásticamente debido a la recuperación de contexto relevante.

## Decisiones

- **D1**: Se establece como regla de [[Gobernanza]] que si el *Rework Rate* de un agente supera el 40% durante tres objetivos consecutivos, el dueño ordena suspender el agente y auditar su sistema de prompts o de recuperación de memoria ([[Registro de decisiones]], D-06).

## Preguntas abiertas

- ¿Cómo diferenciar la corrección humana constructiva (ej. refinar el diseño estético) de una corrección por error técnico del agente al medir el *Rework Rate*?
- ¿Cómo calcular el costo de oportunidad de que un humano esté "esperando" las respuestas de un agente lento?

---
Relacionado: [[Roles de agentes]] · [[Roles humanos]] · [[Métricas operativas]] · [[Gobernanza]] · [[Defectos perceptuales generados por IA]]
