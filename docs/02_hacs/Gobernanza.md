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

---

## Implementación de Referencia: Luum Cognitive OS

La gobernanza de HACS se materializa técnicamente mediante [luum-cognitive-os](https://github.com/Luum-Home/luum-cognitive-os), una capa de gobernanza y malla de seguridad para agentes de programación desarrollada en colaboración entre **Luum** y **OliveX**. No es un framework de agentes, sino una capa que se monta sobre herramientas existentes (Claude Code, Cursor, Codex) para interceptar acciones no autorizadas.

### La Malla de Seguridad de 14 Capas (Safety Mesh)
`luum-cognitive-os` intercepta las llamadas de los agentes en el ciclo de vida del CLI usando hooks (`PreTool` / `PostTool`) que previenen fallos críticos:

1.  **Prevención de Resultados Fabricados (`claim-validator.sh`)**: Evita que los agentes reporten tests pasados o tareas listas sin haber corrido físicamente los comandos de prueba en la terminal (Bloqueo en Capa 6).
2.  **Control de Radio de Impacto (`blast-radius.sh`)**: Advierte y bloquea al agente si intenta modificar archivos o directorios fuera del alcance de trabajo seguro definido en las restricciones ([[Fase 2 - Constraints]]).
3.  **Prevención de Bucles y Costos Descontrolados (`rate-limiter.sh`)**: Cita límites máximos de llamadas a herramientas, generación de subagentes y gasto de tokens de API por hora para evitar bucles infinitos.
4.  **Validación de Confianza (`trust-score-validator.sh`)**: Exige que el agente redacte un reporte de confianza con evidencia empírica verificable antes de declarar la tarea terminada.
5.  **Reversión Automática (`auto-rollback-trigger.sh`)**: Realiza un `git checkout` o reversión completa si el agente falla en estabilizar el build tras agotar su límite de reintentos.

---

## Principios de diseño

1. **Autonomía ganada, no otorgada:** un agente amplía sus permisos cuando su historial de precisión lo justifica, no por default.
2. **Auditoría total:** toda acción de agente queda registrada con contexto, costo y evidencia.
3. **Reversibilidad como criterio:** acciones reversibles → agente autónomo; irreversibles o externas → aprobación humana.
4. **Presupuesto explícito:** los agentes tienen costo medible; la gobernanza incluye límites de gasto por objetivo ([[Fase 2 - Constraints]]).

## Preguntas abiertas

- ¿Cómo se audita una *cadena* de decisiones entre agentes (Planner → Builder → Reviewer) cuando el error emerge de la composición?
- ¿Qué marcos regulatorios aplican (EU AI Act, SOC 2) y cómo mapean a esta matriz? → alimenta [[Riesgos]]
