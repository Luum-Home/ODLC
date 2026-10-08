---
tags: [odlc, requisitos, calidad, constraints]
status: borrador
created: 2026-06-10
---

# Requisitos funcionales y no funcionales

## Por qué importa este documento

En la ingeniería de software tradicional, todo proyecto se divide en:
- **Requisitos funcionales (RF)**: qué debe hacer el sistema (features, casos de uso)
- **Requisitos no funcionales (RNF)**: cómo debe hacerlo (performance, seguridad, escalabilidad, mantenibilidad, disponibilidad)

En la ingeniería AI-Native (HACS + ODLC) esa distinción no desaparece, pero se reformula. Los agentes pueden ejecutar funcionalidades rápido, pero cumplir RNF requiere gobernanza: [[Fase 2 - Constraints]] es donde los RNF viven de forma natural.

## Traducción al modelo ODLC

| Ingeniería tradicional | Modelo ODLC | Dónde vive |
|---|---|---|
| Requisitos funcionales | Derivados de la estrategia elegida, trazables a la métrica del objetivo | [[Fase 3 - Strategy]], [[Fase 5 - Validation]] |
| Requisitos no funcionales | Constraints + gobernanza + métricas | [[Fase 2 - Constraints]], [[Gobernanza]], [[Métricas operativas]] |
| Historias de usuario | Objetivo como unidad de trabajo ([[Glosario y taxonomía]]); especificaciones EARS como detalle de ejecución | [[Fase 1 - Objective]], [[Análisis - Adaptando Claude Code para SDD]] |
| NFR de performance | Constraints `calidad` | [[Fase 2 - Constraints]] |
| NFR de seguridad | Constraints `seguridad` + Safety Mesh | [[Fase 2 - Constraints]], [[Gobernanza]] |
| NFR de disponibilidad | SLOs/SLIs (aún no formalizado) | TBD |
| NFR de costo | Constraints `presupuesto` + Agent Cost | [[Fase 2 - Constraints]], [[Métricas de agentes]] |

## Plantilla — Requisitos funcionales

```yaml
requisitos_funcionales:
  - id: RF-01
    descripcion: "El sistema debe permitir crear libros de texto estructurados en 3 trimestres"
    criterio_aceptacion: "Se genera libro con 18 secuencias en < 5 minutos"
    notacion_ears: "Cuando el usuario solicita generar un libro, el sistema debe crear la estructura completa y disparar el workflow de generación"
    evidencia: "[[Fase 5 - Validation]] - métrica de éxito"
    trazabilidad: "[[Fase 1 - Objective]] - objetivo del ciclo"
```

Los requisitos funcionales en ODLC deben ser trazables a la métrica del objetivo y validables en [[Fase 5 - Validation]]. Un RF sin métrica de validación es una aspiración, no un requisito.

## Plantilla — Requisitos no funcionales

```yaml
requisitos_no_funcionales:
  - id: RNF-01
    categoria: performance
    descripcion: "El sistema debe responder en < 2 segundos al 95% de las consultas"
    medicion: "Latencia P95 en producción, medida con observabilidad"
    constraint_vinculada: "[[Fase 2 - Constraints]] - calidad"
    tolerancia: "Hasta 5 segundos en escenarios de carga alta"

  - id: RNF-02
    categoria: seguridad
    descripcion: "Toda llamada externa a proveedores LLM debe sanitizar PII"
    medicion: "Auditoría de logs y pruebas de filtración"
    constraint_vinculada: "[[Fase 2 - Constraints]] - seguridad + [[Gobernanza]]"
    herramienta: "PII Redaction, interceptor de [[Módulo 4 - Ciberseguridad aplicada]]; no es una de las 14 capas de la Safety Mesh"

  - id: RNF-03
    categoria: escalabilidad
    descripcion: "El sistema debe soportar 1000 usuarios concurrentes sin degradación"
    medicion: "Test de carga en staging"
    constraint_vinculada: "[[Fase 2 - Constraints]] - calidad"

  - id: RNF-04
    categoria: disponibilidad
    descripcion: "SLO del 99.9% de uptime (≈8,76 horas caídas/año)"
    medicion: "Observabilidad en producción"
    constraint_vinculada: A definir - TBD en [[Fase 2 - Constraints]]
    tolerancia: "99.5% mínimo"

  - id: RNF-05
    categoria: mantenibilidad
    descripcion: "Cobertura de tests >= 80%, con tests de integración y E2E"
    medicion: "Pipeline CI/CD - métricas de cobertura"
    constraint_vinculada: "[[Fase 2 - Constraints]] - calidad"

  - id: RNF-06
    categoria: costo
    descripcion: "Costo de agentes no debe superar $X por objetivo"
    medicion: "Agent Cost en [[Métricas de agentes]]"
    constraint_vinculada: "[[Fase 2 - Constraints]] - presupuesto"
```

## Categorías de requisitos no funcionales críticos en sistemas AI-Native

Adicional a los RNF clásicos, los sistemas cognitivos humano-agente requieren:

### 1. Costo de cómputo de agentes
- Costo máximo de tokens por objetivo
- Costo máximo mensual por equipo
- Budget de emergencia para picos
- Gobernanza de qué agente usa qué modelo (caros vs baratos)

### 2. Trazabilidad de decisiones de IA
- Toda respuesta de agente debe ser auditable (prompt + output)
- Toda decisión con impacto organizacional debe estar registrada en [[Memoria organizacional]]
- Linkeado a [[Fase 6 - Learning]]

### 3. Gobernanza y autonomía
- Matriz de acciones autónomas vs con aprobación humana ([[Gobernanza]])
- Rate limits de herramientas críticas
- Kill switches para ejecución destructiva

### 4. Calidad de contexto
- Umbral de contexto a calibrar (el 40% proviene de un video y no está verificado, ver [[Análisis - Harness Engineering y la Paradoja de Herramientas]])
- Métricas de ruido de contexto
- Gobernanza de qué contexto se inyecta a qué agente

### 5. Reversibilidad
- Toda acción del agente es reversible o pasa antes por aprobación humana ([[Gobernanza]]). Ser reversible es necesario pero no suficiente: la acción además tiene que figurar como del agente en la matriz ([[Registro de decisiones]], D-06)
- Snapshots automáticos antes de cambios destructivos
- Feature flags para cambios de larga duración

### 6. Rework Rate
- Medir retrabajo humano como % del trabajo del agente ([[Métricas de agentes]])
- Umbrales heurísticos sin calibrar: ver [[Métricas de agentes]]

## Reglas

1. **Todo RNF necesita métrica medible.** Si un RNF no se puede medir, no es un requisito, es un deseo.
2. **RNF vinculados a constraints.** Cada RNF debe referenciar una constraint de [[Fase 2 - Constraints]] o proponer una nueva.
3. **RNF respetados por agentes.** Los agentes no pueden "negociar" RNF; si violan uno, escalan a humano.
4. **Evolución documentada.** Los RNF son constraints y siguen la regla de versionado de [[Fase 2 - Constraints]].

## Integración con el ciclo ODLC

```
[[Fase 1 - Objective]]: define el outcome y su métrica; los requisitos funcionales se derivan en [[Fase 3 - Strategy]]
     ↓
[[Fase 2 - Constraints]]: define CÓMO no se puede romper (RNF como constraints)
     ↓
[[Fase 3 - Strategy]]: elige CÓMO hacerlo respetando RNF
     ↓
[[Fase 4 - Execution]]: ejecuta con instrumentación para validar RNF
     ↓
[[Fase 5 - Validation]]: valida funcional + no funcional con evidencia
     ↓
[[Fase 6 - Learning]]: aprende qué RNF fueron bien calibrados
```

## Preguntas abiertas

- ¿Cómo manejar RNF que tardan en evidenciarse (ej: mantenibilidad se mide a 6 meses)?
- ¿Deberían los RNF tener su propia fase de definición paralela a Constraints?
- ¿Cómo evitar el anti-patrón de "relajar RNF silenciosamente" durante la ejecución?
- ¿Hay RNF emergentes específicos de IA (calidad de contexto, tasa de alucinaciones) que no mapeen a categorías tradicionales?

## Relacionado
[[Fase 1 - Objective]] · [[Fase 2 - Constraints]] · [[Fase 5 - Validation]] · [[Gobernanza]] · [[Métricas de agentes]] · [[Métricas operativas]] · [[Análisis - Adaptando Claude Code para SDD]] · [[Producción de software vs. velocidad real]]
