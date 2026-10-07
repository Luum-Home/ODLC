---
tags: [odlc, fase]
status: borrador
created: 2026-06-10
---

# Fase 1 — Objective

Primera fase de [[ODLC]]. Define **el resultado esperado, las métricas de éxito, el impacto de negocio y el horizonte temporal**. Todo lo que sigue (constraints, estrategia, ejecución, validación) se deriva de lo que se declare acá.

## Plantilla

```yaml
objective:
  resultado_esperado: ""        # qué cambia en el mundo si esto sale bien
  metrica_de_exito: ""          # número observable, con baseline y target
  fecha_objetivo: ""            # horizonte temporal explícito
  impacto_de_negocio: ""        # por qué importa, en términos del Sponsor
  responsable_humano: ""        # Sponsor (acepta o rechaza el resultado)
```

## Ejemplo

> "Reducir la mediana del tiempo de onboarding de vendedores de 5 días (baseline) a 1 día antes del <fecha>; impacto: <impacto de negocio>; responsable: Sponsor de Ventas."
>
> *(Ejemplo ilustrativo: los valores entre `< >` son placeholders, no datos reales.)*

Nótese lo que **no** dice: no menciona features, pantallas ni tecnología. Eso es de [[Fase 3 - Strategy]] en adelante.

## Reglas

1. **Medible o no es objetivo.** Si no se puede validar con evidencia en [[Fase 5 - Validation]], es una expresión de deseo.
2. **Outcome, no output.** "Lanzar el módulo X" es output; "reducir el churn 2 puntos" es outcome → [[Más código no es más velocidad]].
3. **Un dueño humano.** La formulación del objetivo es responsabilidad de [[Roles humanos]]: formula Product; aprueba Sponsor. Los agentes pueden proponer y refinar, no decidir.

## Métricas asociadas

Objective Success Rate, Time To Outcome → [[Métricas operativas]].

## Preguntas abiertas

- ¿Tamaño correcto de un objetivo? ¿Cómo se detecta uno "demasiado grande" que debería partirse?
- ¿Cómo conviven objetivos concurrentes que compiten por las mismas restricciones?
