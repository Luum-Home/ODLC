---
tags: [problema, anti-patron, bloat, deuda-tecnica]
status: borrador
created: 2026-06-10
---

# Software bloated

> "Bloat is not abundance. It is hidden cost."

Software bloated es el anti-patrón de código, dependencias o funcionalidad sobredimensionada respecto al propósito real del sistema. Se manifiesta como:

- **Código inflado**: más líneas de las necesarias para lograr lo mismo.
- **Dependencias importadas** que aportan poco al caso de uso.
- **Funcionalidades que nadie pidió** ("preparación para el futuro").
- **Over-engineering** disfrazado de robustez.
- **Contexto de prompts hinchado** en agentes: tokens sin propósito.

## Por qué importa en la era AI-Native

Los agentes de IA tienden a producir bloat de forma estructural:

1. **Velocidad sin discriminación**: generan rápido pero no evalúan qué es esencial versus qué es ruido.
2. **Patrones de entrenamiento**: replican soluciones que vieron en datasets sin saber si son apropiadas para el proyecto.
3. **Ausencia de costo percibido**: no sienten el peso de mantener código extra; humanos sí.
4. **Falta de gobernanza de simplicidad**: sin reglas explícitas como "hacer lo mínimo necesario", el agente opta por lo más completo.

La consecuencia: un equipo con agentes puede producir 10x código pero también 10x deuda técnica invisible → [[Más código no es más velocidad]].

## Síntomas detectables

| Señal | Qué indica |
|---|---|
| Repositorio crece pero métricas de negocio no se mueven | [[Más código no es más velocidad]] |
| PRs gigantes sin impacto claro en objetivo | Sloppy cannon ([[Análisis - Token Economics y las 5 Predicciones del Caos]]) |
| Dependencias nuevas por cada feature | Falta de disciplina de mínimos |
| Agentes reintentan soluciones con más código cuando falla | Falta de principio de simplicidad |
| Ventana de contexto llena de información no utilizada | Degradación semántica ([[Análisis - Harness Engineering y la Paradoja de Herramientas]]) |

## Antídotos en HACS-ODLC

- **Purpose over Technology y Outcomes over Output** ([[Manifiesto HACS-ODLC]]): toda línea responde a un propósito de negocio verificable; el volumen producido no es valor.
- **Constraints de simplicidad** ([[Fase 2 - Constraints]]): declarar como restricción "mínima implementación para lograr el objetivo".
- **Gobernanza de revisión** ([[Gobernanza]]): agentes deben pasar el filtro de "¿esto es necesario o es bloat?" antes de commit.
- **Validación por evidencia** ([[Fase 5 - Validation]]): medir el valor entregado, no el volumen generado.
- **Pruning periódico**: ciclos dedicados a eliminar código, dependencias y documentación obsoleta.

## Principio operativo

> "Si no puedo explicar por qué esta línea existe en tres frases o menos, probablemente está de más."

El agente ideal no es el que escribe más, sino el que logra el objetivo con lo mínimo indispensable. La simplicidad es una constraint de primera clase, no un lujo posterior.

## Preguntas abiertas

- ¿Cómo medir bloat objetivamente? (líneas de código vs funcionalidad, dependencias vs features usadas, tokens vs outcome)
- ¿Debe existir un "Bloat Rate" como métrica HACS derivada de [[Métricas de agentes]]?
- ¿Quién es el responsable humano de auditar bloat producido por agentes?

## Relacionado

[[Más código no es más velocidad]] · [[Producción de software vs. velocidad real]] · [[Manifiesto HACS-ODLC]] · [[Nuevos cuellos de botella]] · [[Gobernanza]] · [[Fase 2 - Constraints]] · [[Análisis - Token Economics y las 5 Predicciones del Caos]] · [[Análisis - Harness Engineering y la Paradoja de Herramientas]]
