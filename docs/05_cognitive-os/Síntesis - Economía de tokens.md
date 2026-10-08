---
tags: [cognitive-os, tokens, sintesis, gobernanza, metricas]
status: borrador
created: 2026-06-10
---

# Síntesis — Economía de tokens

Consolidación de las implicaciones para HACS-ODLC de los tres análisis sobre economía de tokens. Cada análisis ataca un ángulo distinto; esta nota unifica las conclusiones para que el vault tenga **una sola fuente de implicaciones**, en lugar de tres tablas que se pisan.

| Análisis | Ángulo |
|---|---|
| [[Análisis - La Cultura del Token]] | Organizacional/cultural: métricas por empleado, Goodhart's Law, teatro de IA, Token ROI |
| [[Análisis - Escasez de Tokens y la Crisis de Capacidad de la IA]] | Físico/infraestructura: racionamiento, peaje lingüístico del español, modelo de suscripción insostenible |
| [[Análisis - Token Economics y las 5 Predicciones del Caos]] | Económico/corporativo: stipends, token poker, budgets por equipo, deuda técnica |

## Implicaciones consolidadas para HACS-ODLC

1. **Medir conversión, no consumo.** La métrica madura es valor por token (Token ROI), nunca volumen de tokens ni volumen de código. Mapea a Agent Contribution y Agent Cost ([[Métricas de agentes]]) y a Objective Success Rate ([[Métricas operativas]]). Premiar consumo bruto es Goodhart's Law garantizada.
2. **El presupuesto de tokens es una constraint de primera clase.** Se declara por objetivo en [[Fase 2 - Constraints]] y se estima en [[Fase 3 - Strategy]] (práctica "token poker"), no se descubre en Execution. En tiny teams no se estima: se fija un tope de tiempo y costo por objetivo, y el pronóstico por Monte Carlo se retoma con los datos del piloto ([[Registro de decisiones]], D-08).
3. **Evitar los dos errores simétricos.** Ni error tacaño (recortar el acceso y matar la experimentación) ni error performativo (gamificar el consumo): uso libre con foco en resultado, gobernado por [[Gobernanza]] con límites de gasto y alertas — no con rankings.
4. **Diseñar para la escasez.** Arnés agnóstico al proveedor, contextos destilados (no heredar chats completos), memoria externa ([[Memoria organizacional]]) como amortiguador de re-procesamiento, y conciencia del peaje lingüístico para equipos hispanohablantes.
5. **La deuda técnica generada por agentes es el riesgo agregado.** Volumen barato + incentivos de consumo + sin estimación de costo = crisis de deuda a escala inédita (advertencia de Hotz, según el video, no verificada). Mitigación: revisión obligatoria en [[Fase 5 - Validation]] y detección temprana de patrones en [[Fase 6 - Learning]] → [[Software bloated]].

## Relacionado

[[Gobernanza]] · [[Métricas de agentes]] · [[Métricas operativas]] · [[Más código no es más velocidad]] · [[Software bloated]]
