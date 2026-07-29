---
tags: [hacs, gobernanza]
status: borrador
created: 2026-06-10
---

# Gobernanza

Componente de [[HACS]] que define **seguridad, compliance, auditoría, costos y límites de autonomía**. Materializa el principio **Human Governance** del [[Manifiesto HACS-ODLC]]: los agentes ejecutan; los humanos definen hasta dónde.

## Límites de autonomía (matriz borrador)

| Acción | Humano | Agente |
|---|---|---|
| Definir objetivo | ✅ decide | propone, analiza |
| Decisión de arquitectura | ✅ aprueba | propone con tradeoffs |
| Escribir código / tests / docs | supervisa | ✅ ejecuta |
| Merge a main | aprueba (configurable por madurez) | propone PR |
| **Deploy a producción** | ✅ aprueba | prepara y ejecuta tras aprobación |
| Cambios de seguridad / accesos | ✅ siempre decide | detecta y propone |
| Gasto fuera de presupuesto | ✅ siempre decide | alerta |

La matriz **no es fija**: se relaja a medida que sube el nivel de [[Modelo de madurez AI-Native]] y la confianza acumulada (evidencia en [[Memoria organizacional]] de tasas de acierto del agente — [[Métricas de agentes]]).

**Regla de suspensión:** si el *Rework Rate* de un agente supera el 40% durante tres objetivos consecutivos, el agente debe ser suspendido y su sistema de prompts o recuperación de memoria auditado (Decisión D1 en [[Métricas de agentes]]).

## Implementación de referencia

La gobernanza de HACS se materializa técnicamente en [[Luum Cognitive OS - Implementación de referencia]]: una malla de seguridad de 14 capas (Safety Mesh) que intercepta las acciones de los agentes con hooks `PreToolUse`/`PostToolUse`. El detalle técnico vive en esa nota y en [[Módulo 3 - Gobernanza]]; esta nota define solo el QUÉ conceptual.

## Process-as-code y evidencia

La gobernanza debe estar codificada en artefactos que los agentes puedan leer y ejecutar: reglas del repo, skills, playbooks, tests, PR gates y criterios de cierre. Un agente no debería inferir el proceso desde conversación; debería seguir reglas versionadas.

Además, todo loop agéntico con efectos reales debe cerrar por evidencia auditable — diff, tests, docs, revisión y checks — no por declaración del agente.

Ver: [[Patrones de loops agénticos para repositorios#2. Process-as-code para agentes]] y [[Patrones de loops agénticos para repositorios#8. Evidence-driven implementation]].

## Principios de diseño

1. **Autonomía ganada, no otorgada:** un agente amplía sus permisos cuando su historial de precisión lo justifica, no por default.
2. **Auditoría total:** toda acción de agente queda registrada con contexto, costo y evidencia.
3. **Reversibilidad como criterio:** acciones reversibles → agente autónomo; irreversibles o externas → aprobación humana.
4. **Presupuesto explícito:** los agentes tienen costo medible; la gobernanza incluye límites de gasto por objetivo ([[Fase 2 - Constraints]]).

## Preguntas abiertas

- ¿Cómo se audita una *cadena* de decisiones entre agentes (Planner → Builder → Reviewer) cuando el error emerge de la composición?
- ¿Qué marcos regulatorios aplican (EU AI Act, SOC 2) y cómo mapean a esta matriz? → alimenta [[Riesgos]]
