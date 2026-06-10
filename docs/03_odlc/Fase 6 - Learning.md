---
tags: [odlc, fase]
status: borrador
created: 2026-06-10
---

# Fase 6 — Learning

Sexta y última fase de [[ODLC]] — y la que cierra el loop: **todo resultado genera aprendizaje reutilizable para ciclos futuros.** "Todo ciclo debe producir aprendizaje; todo aprendizaje debe alimentar el siguiente objetivo" ([[Manifiesto HACS-ODLC]]).

## Plantilla

```yaml
learning:
  funciono: []                 # prácticas/decisiones a repetir
  no_funciono: []              # con causa raíz, no solo el síntoma
  decisiones_validadas: []     # hipótesis de Strategy que la realidad confirmó
  decisiones_descartadas: []   # y por qué — tan valioso como lo validado
  conocimiento_reutilizable: []# lo que el próximo ciclo debería encontrar en memoria
```

## Reglas

1. **El destino es la [[Memoria organizacional]], no un documento suelto.** Una retro cuyo output muere en una pizarra de Miro es teatro de aprendizaje. Cada ítem se guarda atómico, fechado y linkeado para que agentes y humanos lo *encuentren* en la [[Fase 3 - Strategy]] del próximo ciclo.
2. **Aprende el sistema, no solo las personas.** La diferencia con la retro de Scrum: el aprendizaje queda disponible para los agentes (que lo citarán como evidencia) y sobrevive a la rotación de personas.
3. **Lo descartado también se guarda.** Saber qué no funcionó y por qué evita re-explorar callejones sin salida — es la base del Knowledge Reuse Rate ([[Métricas organizacionales]]).

## Métricas asociadas

Learning Velocity ([[Métricas operativas]]), Knowledge Reuse Rate ([[Métricas organizacionales]]).

## Preguntas abiertas

- ¿Quién cura el aprendizaje acumulado? (rol del agente Memory — [[Roles de agentes]]) ¿Con qué cadencia se consolida para que no degenere en ruido?
