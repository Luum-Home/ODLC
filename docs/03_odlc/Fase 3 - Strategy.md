---
tags: [odlc, fase]
status: borrador
created: 2026-06-10
---

# Fase 3 — Strategy

Tercera fase de [[ODLC]]. **Evaluación de alternativas, tradeoffs y riesgos, y selección justificada de la mejor estrategia.** Es la fase que ataca el cuello de botella de *decisión* ([[Nuevos cuellos de botella]]).

## Plantilla

```yaml
strategy:
  alternativas:
    - nombre: "A"
      descripcion: ""
      pros: []
      contras: []
      riesgos: []
      costo_estimado: ""        # o tope de tiempo y costo en tiny teams (D-08)
    - nombre: "B"
      # ...
    - nombre: "C"
      # ...
  elegida: ""
  justificacion: ""      # por qué esta y por qué no las otras — esto va a Memoria
  referencias_memoria: [] # ≥1 ADR/postmortem aplicable; vacío solo con motivo
  aprobada_por: ""       # Architect humano
  fecha_aprobacion: ""
```

## Reglas

1. **Mínimo dos alternativas reales.** Una sola opción no es estrategia, es decisión ya tomada buscando justificación.
2. **Los agentes generan y analizan; los humanos eligen.** El agente Architect ([[Roles de agentes]]) produce alternativas con tradeoffs y evidencia de [[Memoria organizacional]] (¿ya intentamos algo así? ¿qué pasó?); el humano Architect ([[Roles humanos]]) decide.
3. **La justificación se escribe para el futuro.** Alternativas descartadas y porqués van a memoria como ADR — son el insumo de [[Fase 6 - Learning]] y de futuras estrategias.
4. **Evidence over Opinions** ([[Manifiesto HACS-ODLC]]): los tradeoffs se sostienen con datos (benchmarks, costos, incidentes previos), no con preferencias.

## Preguntas abiertas

- ¿Cuándo amerita un *spike* de ejecución exploratoria antes de elegir? ¿Cómo se acota?
- Decision Lead Time se mide desde la aprobación de las constraints hasta la aprobación formal de la estrategia: ver [[Métricas organizacionales#3. Decision Lead Time (DLT)]].
