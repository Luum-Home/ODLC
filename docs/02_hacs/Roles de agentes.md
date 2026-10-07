---
tags: [hacs, roles, agentes]
status: semilla
created: 2026-06-10
---

# Roles de agentes

Los agentes en [[HACS]] aportan: **análisis, ejecución, validación, documentación y monitoreo**. Operan dentro de los límites definidos por la [[Gobernanza]] y leen/escriben la [[Memoria organizacional]].

| Agente | Función (borrador) |
|---|---|
| **Planner** | Descompone objetivos en planes y coordina la ejecución de los demás agentes |
| **Architect** | Propone arquitecturas, ADRs y modelos de datos; analiza tradeoffs para [[Fase 3 - Strategy]] |
| **Builder** | Genera código, infraestructura, migraciones y documentación técnica |
| **Reviewer** | Revisa código y artefactos contra estándares, specs y decisiones previas en memoria |
| **Security** | Detecta vulnerabilidades, propone fixes, audita dependencias y configuraciones |
| **Memory** | Captura decisiones, evidencia y aprendizajes; mantiene la memoria recuperable y curada |

Se parece al pipeline multi-agente del [[AI SDLC]] avanzado (PM Agent → Architect Agent → Developer Agent → Tester Agent → Security Agent → DevOps Agent); difiere en que la memoria es persistente y curada ([[Memoria organizacional]], no solo contexto de sesión), en los límites de autonomía explícitos y en el conjunto de roles (Memory sí; Tester y DevOps sin definir).

Otros agentes que aparecen en el vault son instancias de estos roles: el **Fix Agent** ([[Glosario y taxonomía]]) es una instancia de Builder; los **jueces** del Judgment Day son instancias de Reviewer; el **Lead Agent** de [[Agent Loop Engineering]] es el Planner en modo orquestador.

## Loops de revisión entre agentes

El rol Builder produce cambios, pero el rol Reviewer debe validar con distancia crítica. Para cambios relevantes, el patrón recomendado es:

```text
apply → fresh review → findings → fix → re-review → merge
```

La separación de contexto reduce sesgo de confirmación: quien valida no debería depender únicamente del hilo que produjo la implementación.

Ver: [[Patrones de loops agénticos para repositorios#5. Apply/Judge/Fix loop]] y [[Patrones de loops agénticos para repositorios#7. Fresh-context validation]].

## Hipótesis

- La especialización por rol (vs. un agente generalista) mejora trazabilidad y auditoría, aunque los modelos subyacentes sean el mismo. El rol es un *contrato*, no una capacidad técnica distinta.

## Preguntas abiertas

- ¿Falta un agente *Tester* explícito o es parte de Reviewer? ¿Y un agente *Ops/Observability*?
- ¿Cómo se mide la contribución y precisión de cada agente? → [[Métricas de agentes]]
- Decisión: las contradicciones estructurales escalan a un humano ([[Fase 3 - Strategy]], [[Glosario y taxonomía]]); abierto: ¿puede el Planner pre-filtrar?
