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
  
  $$HLR = \frac{\text{Objetivos cumplidos (OSR)}}{\text{Horas de intervención humana}}$$

Un HLR alto indica que los humanos se dedican a definir objetivos, evaluar estrategias y gobernar, delegando la ejecución repetitiva en los agentes.

---

## 2. Agent Accuracy (Tasa de Precisión / Retrabajo)

Mide la calidad del trabajo autónomo y la necesidad de intervención o corrección humana.

$$\text{Rework Rate} = \frac{\text{Artefactos de agentes rechazados o modificados por humanos}}{\text{Total de artefactos generados por agentes}}$$

### Rangos de Referencia:
- **Precisión Óptima (Rework < 10%)**: El agente opera de forma fluida. Sus decisiones están bien alineadas con las [[Fase 2 - Constraints]] y la [[Memoria organizacional]].
- **Degeneración de Autonomía (Rework > 30%)**: Los humanos actúan constantemente como correctores detallados de código o diseño. Indica desalineación de contexto o limitaciones del modelo LLM.

---

## 3. Agent Cost (Costo y Eficiencia de Agentes)

Evalúa la eficiencia financiera del uso de agentes en comparación con el costo de horas de ingeniería humana equivalentes.

$$\text{Costo por Objetivo} = \text{Costo de APIs de LLMs} + \text{Cómputo en Sandbox} + \text{Almacenamiento de Memoria}$$

A diferencia del costo de salarios humanos, el costo de agentes es altamente elástico y escalable. Sin embargo, loops infinitos o la falta de límites de ejecución pueden disparar los costos sin agregar valor.

---

## Hipótesis

- **H1**: Aumentar el ACR sin monitorear el *Rework Rate* disminuye la velocidad general del equipo debido a cuellos de botella en la revisión humana (ver [[Más código no es más velocidad]]).
- **H2**: A medida que madura la [[Memoria organizacional]], el *Rework Rate* de los agentes disminuye drásticamente debido a la recuperación de contexto relevante.

## Decisiones

- **D1**: Se establece como regla de [[Gobernanza]] que si el *Rework Rate* de un agente supera el 40% durante tres objetivos consecutivos, el agente debe ser suspendido y su sistema de prompts o recuperación de memoria debe ser auditado.

## Preguntas abiertas

- ¿Cómo diferenciar la corrección humana constructiva (ej. refinar el diseño estético) de una corrección por error técnico del agente al medir el *Rework Rate*?
- ¿Cómo calcular el costo de oportunidad de que un humano esté "esperando" las respuestas de un agente lento?

---
Relacionado: [[Roles de agentes]] · [[Roles humanos]] · [[Métricas operativas]] · [[Gobernanza]]
