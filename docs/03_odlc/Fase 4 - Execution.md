---
tags: [odlc, fase]
status: borrador
created: 2026-06-10
---

# Fase 4 — Execution

Cuarta fase de [[ODLC]]. **Humanos y agentes ejecutan la estrategia elegida.** Es la fase que el [[AI SDLC]] ya aceleró — y por eso es la que *menos* diferencia a ODLC: aquí la novedad no es cómo se ejecuta, sino que la ejecución está subordinada a un objetivo validable.

## ¿Qué ejecutan los agentes?

- ☑ **Código** (features, refactors, migraciones)
- ☑ **Tests** (unitarios, integración, cobertura)
- ☑ **Docs** (técnica, de usuario, ADRs)
- ☑ **Infra** (IaC, pipelines CI/CD)
- ☑ **Observabilidad** (dashboards, alertas, instrumentación)
- ☑ **Operaciones** (análisis de logs, triage de incidentes, remediación propuesta; aplicarla en producción requiere aprobación humana)

## Plantilla

```yaml
execution:
  humanos_involucrados: []     # roles y dedicación
  agentes_involucrados: []     # qué agente hace qué (ver Roles de agentes)
  sistemas_involucrados: []    # repos, entornos, servicios
  entregables: []              # artefactos esperados, cada uno trazable al objetivo
```

## Reglas

1. **Todo artefacto trazable al objetivo.** Si un entregable no contribuye a la métrica de [[Fase 1 - Objective]], es scope creep — se corta o se vuelve objetivo propio.
2. **La ejecución respeta la matriz de [[Gobernanza]]:** qué puede hacer un agente solo y qué requiere aprobación humana.
3. **Constraint violada → la tarea afectada se detiene y se escala al dueño de la constraint**, no se improvisa; el resto de la ejecución sigue ([[Fase 2 - Constraints]]).
4. **Evidencia desde el día uno:** la ejecución produce los datos que [[Fase 5 - Validation]] va a necesitar; instrumentar al final es demasiado tarde.
5. **TDD agéntico con arnés:** cuando un agente implementa con TDD, no alcanza con pedirle "hacé TDD". La ejecución debe incluir init de capacidades, estado persistente y evidencia RED/GREEN/REFACTOR auditable. Ver [[Agent Loop Engineering#Patrón aplicado: TDD para agentes]] y [[Patrones de loops agénticos para repositorios#6. TDD con evidencia]].
6. **Implementación basada en evidencia:** un cambio producido por agentes no se cierra por afirmación, sino por diff, tests, docs, revisión y checks en cada frontera afectada. Ver [[Patrones de loops agénticos para repositorios#8. Evidence-driven implementation]].

## Métricas asociadas

Agent Contribution Ratio ([[Métricas de agentes]]), Human Leverage Ratio ([[Métricas de agentes]]).
