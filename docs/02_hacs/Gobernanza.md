---
tags: [hacs, gobernanza]
status: borrador
created: 2026-06-10
---

# Gobernanza

Componente de [[HACS]] que define **seguridad, compliance, auditoría, costos y límites de autonomía**. Materializa el principio **Human Governance** del [[Manifiesto HACS-ODLC]]: los agentes ejecutan; los humanos definen hasta dónde.

## Límites de autonomía (matriz borrador)

Esta matriz es la única lista de aprobaciones humanas del marco, ordenada por tipo de acción ([[Registro de decisiones]], D-01). Las demás notas la enlazan en lugar de repetirla.

| Acción | Humano | Agente | ¿Se relaja con la madurez? |
|---|---|---|---|
| Definir objetivo | ✅ decide | propone, analiza | No |
| Decisión de arquitectura | ✅ aprueba | propone con tradeoffs | Sí |
| Escribir código / tests / docs | supervisa | ✅ ejecuta | Sí |
| Merge a main | aprueba | propone PR | Sí |
| **Deploy a producción** | ✅ aprueba | prepara y ejecuta tras aprobación | Sí |
| Cambios de seguridad / accesos | ✅ siempre decide | detecta y propone | No |
| Gasto fuera de presupuesto | ✅ siempre decide | alerta | No |
| **Lo irreversible:** pagos, datos de clientes, borrado, migraciones destructivas | ✅ siempre aprueba (validador externo o excepción escrita, ver [[Núcleo ODLC para tiny teams]]) | prepara y propone | No |

Las filas marcadas "Sí" se relajan a medida que sube el nivel de [[Modelo de madurez AI-Native]] y la confianza acumulada (evidencia en [[Memoria organizacional]] de tasas de acierto del agente — [[Métricas de agentes]]). Lo irreversible no se relaja con ningún nivel: en el Nivel 5 el humano deja la ejecución táctica pero conserva lo irreversible y las decisiones marcadas "siempre" (D-01).

**Regla de suspensión:** si el *Rework Rate* de un agente supera el 40% durante tres objetivos consecutivos, el dueño ordena suspender el agente y auditar su sistema de prompts o de recuperación de memoria (Decisión D1 en [[Métricas de agentes]]; responsable fijado en D-06). Regla provisoria: inaplicable hasta instrumentar el Rework Rate ([[Métricas de agentes#Instrumentación pendiente]]); umbral heurístico sin calibrar.

## Implementación de referencia

La gobernanza de HACS se materializa técnicamente en [[Luum Cognitive OS - Implementación de referencia]]: una malla de seguridad de 14 capas (Safety Mesh) que intercepta las acciones de los agentes con hooks `PreToolUse`/`PostToolUse`. El detalle técnico vive en esa nota y en [[Módulo 3 - Gobernanza]]; esta nota define solo el QUÉ conceptual.

## Process-as-code y evidencia

La gobernanza debe estar codificada en artefactos que los agentes puedan leer y ejecutar: reglas del repo, skills, playbooks, tests, PR gates y criterios de cierre. Un agente no debería inferir el proceso desde conversación; debería seguir reglas versionadas.

Además, todo loop agéntico con efectos reales debe cerrar por evidencia auditable — diff, tests, docs, revisión y checks — no por declaración del agente.

Ver: [[Patrones de loops agénticos para repositorios#2. Process-as-code para agentes]] y [[Patrones de loops agénticos para repositorios#8. Evidence-driven implementation]].

## Principios de diseño

1. **Autonomía ganada, no otorgada:** un agente amplía sus permisos cuando su historial de precisión lo justifica, no por default.
2. **Auditoría total:** toda acción de agente queda registrada con contexto, costo y evidencia.
3. **Reversibilidad como criterio necesario, no suficiente:** una acción irreversible o externa requiere aprobación humana; que sea reversible no alcanza para que el agente la haga solo, además tiene que figurar como del agente en la matriz (D-06).
4. **Presupuesto explícito:** los agentes tienen costo medible; la gobernanza incluye límites de gasto por objetivo ([[Fase 2 - Constraints]]).

## Preguntas abiertas

- ¿Cómo se audita una *cadena* de decisiones entre agentes (Planner → Builder → Reviewer) cuando el error emerge de la composición?
- ¿Qué regulaciones (EU AI Act) y marcos de atestación (SOC 2, ISO/IEC 42001) aplican y cómo mapean a esta matriz? → alimenta [[Riesgos]]
