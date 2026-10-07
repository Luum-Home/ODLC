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
  calidad: ""            # RNF: performance, disponibilidad, escalabilidad, mantenibilidad
  regulatorios: ""       # normas que aplican (datos personales, industria, región)
  seguridad: ""          # superficies que no se tocan sin aprobación (ver Gobernanza)
  recursos_humanos: ""   # quiénes están disponibles, con qué dedicación y capacidades
```

## Reglas

1. **Las constraints las fijan humanos** ([[Roles humanos]] — Sponsor: presupuesto; Product: producto y regulatorias; Architect: técnicas y seguridad); los agentes las *verifican* durante [[Fase 4 - Execution]].
2. **El presupuesto de agentes es una constraint de primera clase.** Los agentes tienen costo medible ([[Métricas de agentes]]); ignorarlo repite el error de tratar la ejecución como gratis.
3. **El presupuesto se expresa como distribución cuando hay historial.** Con costos de objetivos anteriores, una simulación Monte Carlo da percentiles ("85% de probabilidad de gastar menos de X") en lugar de una cifra puntual; la constraint se fija sobre un percentil explícito ([[Métricas operativas#Pronóstico probabilístico (simulación Monte Carlo)]]).
4. **Constraint violada = tarea detenida y escalada.** Si una estrategia en curso choca contra una restricción, la tarea afectada se detiene y se escala al dueño de la constraint; el resto de la ejecución sigue. No se "negocia" silenciosamente.
5. **Las constraints se versionan con el objetivo; relajarlas requiere decisión humana explícita del rol que las fijó.**

## Relación con Gobernanza

Las constraints son por-objetivo; la [[Gobernanza]] es del sistema. La matriz de autonomía de gobernanza actúa como conjunto de constraints permanentes que todo objetivo hereda.
