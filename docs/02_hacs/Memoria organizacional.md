---
tags: [hacs, memoria]
status: borrador
created: 2026-06-10
---

# Memoria organizacional

Componente de [[HACS]] que conserva conocimiento y contexto de forma **persistente, recuperable y compartida** entre humanos y agentes. Es la respuesta al cuello de botella de fragmentación del contexto ([[Nuevos cuellos de botella]]).

## Principio

**Memory over Documentation** ([[Manifiesto HACS-ODLC]]): la documentación tradicional se escribe una vez y se desactualiza; la memoria se consulta y actualiza en cada ciclo. La diferencia no es el formato sino el *uso*: la memoria participa del flujo de trabajo (los agentes la leen antes de decidir y la escriben después de aprender — [[Fase 6 - Learning]]).

## ¿Qué se guarda?

- ☑ **Decisiones** (con alternativas consideradas y justificación — ADRs)
- ☑ **Evidencia** (resultados de validación, datos que sostienen o refutan hipótesis)
- ☑ **Arquitectura** (estado actual y su porqué)
- ☑ **Métricas** (series históricas de [[Métricas operativas]])
- ☑ **Incidentes** (postmortems, causas raíz)
- ☑ **Costos** (de ejecución humana y de agentes)
- ☑ **Lecciones aprendidas** (salida de cada [[Fase 6 - Learning]])

## Memoria con ciclo de vida

La memoria organizacional no debe ser acumulativa sin caducidad. Las decisiones, políticas y preferencias necesitan señales de vigencia.

Patrón mínimo:

```text
memoria creada → memoria activa → memoria stale / necesita revisión → revisión humana/agente → actualizar, superseder o marcar vigente
```

Una memoria vieja no es necesariamente falsa, pero tampoco debe ser usada como verdad vigente sin verificación. El agente Memory debe poder distinguir entre memoria activa, memoria que necesita revisión, memoria supersedida y memoria descartada.

Ver: [[Patrones de loops agénticos para repositorios#3. Memoria con ciclo de vida]].

## Modelo de memoria (hipótesis)

- Cada entrada es **atómica, fechada y linkeable** (los mismos principios de este vault — ver [[README]]).
- Distinción entre memoria *episódica* (qué pasó: incidentes, validaciones) y *semántica* (qué sabemos: convenciones, arquitectura, lecciones).
- La memoria se **cura**: el agente Memory ([[Roles de agentes]]) consolida duplicados y marca entradas obsoletas; memoria sin curaduría degenera en el mismo ruido que la documentación tradicional.

## Métricas asociadas

Knowledge Reuse Rate y Context Retrieval Time → [[Métricas organizacionales]].

## Preguntas abiertas

- ¿Qué *no* debe guardarse? (privacidad, costo de ruido, derecho al olvido organizacional)
- ¿La memoria es por unidad HACS o global a la organización? ¿Cómo se comparte entre unidades?
