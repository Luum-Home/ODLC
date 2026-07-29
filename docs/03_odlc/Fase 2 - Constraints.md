---
tags: [odlc, fase]
status: borrador
created: 2026-06-10
---

# Fase 2 — Constraints

Segunda fase de [[ODLC]]. Hace explícitos los límites dentro de los cuales cualquier estrategia es válida. Las restricciones implícitas son la causa clásica de estrategias brillantes e inviables.

## Plantilla

```yaml
constraints:
  presupuesto: ""        # dinero total, incluyendo costo de agentes (tokens/cómputo)
  tecnologicos: ""       # stack obligatorio/prohibido, deuda existente, integraciones
  regulatorios: ""       # normas que aplican (datos personales, industria, región)
  seguridad: ""          # superficies que no se tocan sin aprobación (ver Gobernanza)
  recursos_humanos: ""   # quiénes están disponibles, con qué dedicación y capacidades
```

## Reglas

1. **Las constraints las fijan humanos** ([[Roles humanos]]: Product, Architect); los agentes las *verifican* durante [[Fase 4 - Execution]].
2. **El presupuesto de agentes es una constraint de primera clase.** Los agentes tienen costo medible ([[Métricas de agentes]]); ignorarlo repite el error de tratar la ejecución como gratis.
3. **Constraint violada = ciclo detenido.** Si una estrategia en curso choca contra una restricción, se escala a humano, no se "negocia" silenciosamente.

## Relación con Gobernanza

Las constraints son por-objetivo; la [[Gobernanza]] es del sistema. La matriz de autonomía de gobernanza actúa como conjunto de constraints permanentes que todo objetivo hereda.

## Preguntas abiertas

- ¿Las constraints se versionan con el objetivo o evolucionan durante el ciclo? ¿Quién puede relajarlas a mitad de camino?
