---
tags: [odlc, fase]
status: borrador
created: 2026-06-10
---

# Fase 5 — Validation

Quinta fase de [[ODLC]]. **Se valida el resultado contra el objetivo original, no contra la implementación.** Que el código compile, los tests pasen y el deploy salga verde es validación de *implementación*; ODLC pregunta otra cosa: ¿la métrica declarada en [[Fase 1 - Objective]] se movió?

## ¿Qué significa éxito?

Éxito = la métrica alcanzó el target sin violar ninguna constraint de [[Fase 2 - Constraints]], con evidencia verificable. Entregar a tiempo o sin incidentes no es éxito en sí; respetar las constraints (presupuesto incluido) es condición necesaria, no suficiente.

## Plantilla

```yaml
validation:
  target: ""               # copiado de objective.metrica_de_exito (baseline y target), sin reinterpretar
  resultado_real: ""       # qué midió la realidad
  desviacion: ""           # gap entre ambos, y lectura honesta del gap
  evidencia: []            # datos, dashboards, queries — lo que un tercero podría auditar
  veredicto: ""            # logrado | parcial | fallido
```

## Reglas

1. **El target no se reinterpreta a posteriori.** Si el objetivo era "de 5 días a 1 día" y se llegó a 2, es *parcial* — valioso, pero parcial. Mover el arco después de patear es el anti-patrón que ODLC existe para impedir.
2. **Evidence over Opinions:** la validación cita datos auditables, no impresiones ("se siente más rápido").
3. **Quien valida no es quien ejecutó.** El veredicto lo da el Sponsor ([[Roles humanos]]), con análisis preparado por agentes.
4. **Fallar es un resultado válido** — si produce aprendizaje ([[Fase 6 - Learning]]). Lo inválido es no poder determinar si se falló.
5. **Validar proceso además de resultado:** en loops agénticos, especialmente TDD, la validación debe auditar la evidencia del ciclo, no solo que el estado final pase tests. Ver [[Agent Loop Engineering#Patrón aplicado: TDD para agentes]].
6. **Revisión con contexto fresco:** para cambios relevantes, la validación debe separar el contexto que produjo la implementación del contexto que la revisa. Ver [[Patrones de loops agénticos para repositorios#7. Fresh-context validation]].

## Validación perceptual

En interfaces generadas o modificadas por agentes, un build verde o una captura estática no alcanzan. También hay que validar defectos perceptuales como flickering, layout shift, pérdida de foco, estados loading/empty/error inconsistentes y fallas responsive o de accesibilidad.

Ver: [[Defectos perceptuales generados por IA]].

## Métricas asociadas

Objective Success Rate y Time To Outcome ([[Métricas operativas]]) se calculan en esta fase.

## Preguntas abiertas

- ¿Cuánto se espera para validar métricas que tardan en moverse (churn, retención)? ¿Validación diferida como estado del ciclo?

---
Relacionado: [[ODLC]] · [[Métricas operativas]] · [[Defectos perceptuales generados por IA]]
