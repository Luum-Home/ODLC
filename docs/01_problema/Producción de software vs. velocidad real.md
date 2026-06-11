---
tags: [problema, hipotesis, producción, devops, ci-cd]
status: borrador
created: 2026-06-10
---

# Producción de software vs. velocidad real

Existe una narrativa simplista: "la IA acelera la producción de software." La realidad es más incómoda. Acelerar *fases* —generar código— no acelera el *ciclo completo*. La producción se volvió más rápida, pero la entrega de valor real (código en producción, medible, utilizable) depende de CI/CD, testing, seguridad, observabilidad y deployment.

Una empresa puede generar 100.000 líneas de código por semana con agentes y tener cero despliegues confiables por mes. El verdadero cuello de botella ya no es escribir código → [[Nuevos cuellos de botella]].

## Lo que la IA sí optimiza

> Las aceleraciones de la tabla son **estimaciones ilustrativas**, no mediciones — pendiente de respaldarlas con datos (DORA, estudios de Copilot, casos propios).

| Fase | Aceleración típica (ilustrativa) | Riesgo |
|---|---|---|
| Planificación | Especificación automática (PRDs, historias, ADRs) | Especificaciones ambiguas → agentes las interpretan mal |
| Codificación | 5x-10x en generación de features | Sloppy code, inconsistencia de patrones |
| Testing | Generación automática de suites unitarias | Falso sentido de cobertura, tests de baja calidad |
| Refactor | Detección de deuda y migraciones | Pérdida de comportamiento si no hay validación |
| Documentación | Generación inline y post-hoc | Docs desactualizados y sin revisar |
| Debugging | Análisis de errores y root cause | Dependencia del contexto (que frecuentemente falta) |

## Lo que la IA no optimiza por sí sola

- **CI/CD pipelines**: los agentes escriben YAML, pero no diseñan estrategias de despliegue ni eligen trade-offs (blue/green, canary, rolling).
- **Seguridad como cultura**: agentes detectan vulnerabilidades conocidas pero no comprenden superficies de ataque de organización.
- **Observabilidad con propósito**: los agentes pueden instrumentar, pero decidir QUÉ medir y CÓMO alertar sigue siendo humano.
- **Feature flags, rollbacks, circuit breakers**: decisiones operativas que requieren conocimiento del negocio.
- **Deployment risk**: un agente puede crear un Dockerfile, pero no decide si se pone en producción un cambio de base de datos crítica.
- **Reversibilidad**: los agentes raramente preguntan "¿qué pasa si esto falla?" antes de ejecutar.

## Anti-patrones de "optimización" sin calidad

1. **El Sloppy Cannon**: desarrollador que maximiza tokens y líneas producidas, sin preocuparse por revisión → [[Análisis - Token Economics y las 5 Predicciones del Caos]].
2. **Coverage Theater**: 90% de coverage con tests triviales que no validan comportamiento real.
3. **Pipeline como decoración**: pipelines CI/CD verdes sin tests de integración reales, sin smoke tests en staging.
4. **Feature-flag mania**: desplegar rápido no es lo mismo que desplegar bien.
5. **"Funciona en mi sandbox"**: agentes que producen código que pasa tests locales pero falla en producción porque no conocen el entorno.

## Cómo sí optimizar la producción

### Infraestructura como código

Los agentes crean IaC (Terraform, Pulumi, CloudFormation) pero arquitectos humanos deciden el diseño. El agente es ejecutor, no diseñador de resiliencia regional.

### Pipelines CI/CD

- **Linters y formatters automáticos** (ruff, prettier, gofmt) → gatekeepers de calidad.
- **Tests unitarios + integración + E2E** → pirámide de testing obligatoria.
- **Mutation testing** para validar calidad de tests, no solo cobertura.
- **SAST/DAST** como pasos del pipeline, no como revisiones manuales.
- **Feature flags** controlados por humanos con reglas de rollback automáticas.

### Testing automation

- **Tests generados por agentes** deben pasar el mismo estándar que los humanos: legibilidad, assertions específicas, sin duplicados, con nombres significativos.
- **ATDD (Acceptance Test-Driven Development)**: los agentes generan tests contra criterios de aceptación definidos en [[Fase 1 - Objective]].
- **Property-based testing** para encontrar casos borde que agentes no anticipan.
- **Chaos engineering** para validar robustez del sistema que agentes no modelan.

### Observabilidad de producción

- **Logs estructurados, métricas, trazas distribuidas** (OpenTelemetry, Langfuse, LangSmith).
- Los agentes analizan logs y sugieren parches, pero humanos deciden prioridades.
- SLOs/SLIs como requisitos no funcionales que los agentes deben respetar.

### Gobernanza de despliegue

- **Gatekeepers automáticos**: no se hace deploy si no pasan tests críticos (smoke + contract + security).
- **Canary releases**: un 1% del tráfico para validar antes de rollout completo.
- **Automated rollbacks**: detectores de errores que revierten automáticamente.
- **Aprobación humana** para cambios en infraestructura crítica → [[Gobernanza]].

## El modelo HACS-ODLC: producción como parte de la estrategia

En [[Fase 4 - Execution]], el trabajo del agente incluye:

- Producir artefactos trazables al objetivo ([[Fase 1 - Objective]]).
- Instrumentar para evidencia en [[Fase 5 - Validation]].
- Respetar constraints de performance, seguridad y costo ([[Fase 2 - Constraints]]).
- Generar pipelines, tests y docs como entregables, no como decorado.

En HACS, el humano es quien elige la estrategia de producción (CI/CD, observabilidad, rollout); el agente es quien la ejecuta.

## Métricas de producción relevantes

| Métrica | Qué mide | Por qué importa |
|---|---|---|
| Deployment Frequency | Frecuencia de deploys a producción | Velocidad real de entrega |
| Change Failure Rate | % de deploys con rollback/fix | Calidad del cambio |
| MTTR (Mean Time To Recovery) | Tiempo en recuperar tras fallo | Resiliencia del sistema |
| Lead Time for Changes | Tiempo de commit a producción | Velocidad real, no imaginada |
| Test Effectiveness | Ratio de bugs detectados en test vs producción | Calidad de la pirámide de testing |

Todas derivan de [[Métricas operativas]] (Time To Outcome, OSR) y [[Métricas de agentes]] (Agent Accuracy, Agent Cost).

## Diferencia entre "acelerar" y "optimizar"

- **Acelerar** → menos tiempo para lo mismo.
- **Optimizar** → hacer mejor con los mismos recursos (incluye calidad, seguridad, sostenibilidad).

La IA acelera. HACS-ODLC optimiza: velocidad con gobernanza, calidad y aprendizaje.

## Preguntas abiertas

- ¿Cómo medir el costo de calidad diferida (technical debt) en unidades de tiempo/producción?
- ¿Debería existir una fase previa a Execution donde se formalice la estrategia de CI/CD, observabilidad y rollout?
- ¿Qué papel juega un agente "DevOps Agent" especializado en [[Roles de agentes]]?

---
Relacionado: [[Más código no es más velocidad]] · [[Nuevos cuellos de botella]] · [[AI SDLC]] · [[Fase 4 - Execution]] · [[Fase 5 - Validation]] · [[Métricas operativas]] · [[Métricas de agentes]] · [[Análisis - Token Economics y las 5 Predicciones del Caos]]
