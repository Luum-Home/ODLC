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
| **Remediación en producción** (aplicar un fix, revertir, reiniciar o escalar un servicio) | ✅ aprueba | analiza, propone y aplica tras aprobación | Sí, salvo que la remediación sea irreversible: ahí rige esa fila |
| **Acción externa:** mensajes a terceros (clientes, proveedores, publicaciones) | ✅ siempre aprueba | redacta y propone | No |
| **Lo irreversible:** pagos, datos de clientes, borrado, migraciones destructivas | ✅ siempre aprueba, con validador externo siempre ([[Registro de decisiones]], D-16). Si quien ejecuta también valida, eso requiere además la excepción escrita de [[Núcleo ODLC para tiny teams]], que no reemplaza al validador externo | prepara y propone | No |

Las filas marcadas "Sí" se relajan a medida que sube el nivel de [[Modelo de madurez AI-Native]] y la confianza acumulada (evidencia en [[Memoria organizacional]] de tasas de acierto del agente — [[Métricas de agentes]]). Lo irreversible no se relaja con ningún nivel: en el Nivel 5 el humano deja la ejecución táctica pero conserva lo irreversible y las decisiones marcadas "siempre" (D-01).

**Regla de suspensión:** si el *Rework Rate* de un agente supera el 40% durante tres objetivos consecutivos, el dueño ordena suspender el agente y auditar su sistema de prompts o de recuperación de memoria (Decisión D1 en [[Métricas de agentes]]; responsable fijado en D-06). Regla provisoria: inaplicable hasta instrumentar el Rework Rate ([[Métricas de agentes#Instrumentación pendiente]]); umbral heurístico sin calibrar.

La columna "¿Se relaja con la madurez?" quedó adoptada como decisión en D-18.

## Controles técnicos

La matriz dice qué decide cada uno; estos controles hacen que el arnés de los agentes la respete sin depender de que el agente se porte bien. Son genéricos: cualquier herramienta que intercepte las acciones del agente antes y después de cada llamada puede implementarlos.

- **Interceptar antes y después de cada herramienta:** antes, para frenar lo que la matriz no le asigna al agente; después, para revisar lo que el agente afirma sobre el resultado.
- **Acotar el radio de impacto:** las escrituras fuera del alcance definido en [[Fase 2 - Constraints]] se advierten o se bloquean.
- **No aceptar resultados declarados:** "los tests pasan" o "está listo" valen solo si la corrida existe en el registro; si no, el cierre se rechaza.
- **Topes de llamadas, subagentes y gasto** por hora y por objetivo, para cortar bucles y costos descontrolados.
- **Reversión automática** a un estado limpio cuando el agente agota sus reintentos sin estabilizar el build.
- **Sandbox aislado** para builds, tests y análisis, sin permisos sobre producción salvo lo que la matriz habilita.
- **Respuesta graduada:** cada control bloquea, advierte o solo registra según el riesgo, y se vuelve más estricto a medida que el proyecto pasa de exploración a producción.
- **Defensa en profundidad:** cada control cubre un riesgo distinto; apagar uno deja un punto ciego que los demás no cubren.

El detalle de cómo se arma un arnés con estos controles está en [[Agent Loop Engineering]] y [[Módulo 3 - Gobernanza]].

## Process-as-code y evidencia

La gobernanza debe estar codificada en artefactos que los agentes puedan leer y ejecutar: reglas del repo, skills, playbooks, tests, PR gates y criterios de cierre. Un agente no debería inferir el proceso desde conversación; debería seguir reglas versionadas.

Además, todo loop agéntico con efectos reales debe cerrar por evidencia auditable — diff, tests, docs, revisión y checks — no por declaración del agente.

Ver: [[Patrones de loops agénticos para repositorios#2. Process-as-code para agentes]] y [[Patrones de loops agénticos para repositorios#8. Evidence-driven implementation]].

## Principios de diseño

1. **Autonomía ganada, no otorgada:** un agente amplía sus permisos cuando su historial de precisión lo justifica, no por default.
2. **Auditoría total:** toda acción de agente queda registrada con contexto, costo y evidencia, y la comunicación entre agentes pasa por mensajes estructurados que quedan en el registro, nunca por canales que no se pueden rastrear.
3. **Reversibilidad como criterio necesario, no suficiente:** una acción irreversible o externa requiere aprobación humana (filas de lo irreversible y de acción externa en la matriz); que sea reversible no alcanza para que el agente la haga solo, además tiene que figurar como del agente en la matriz (D-06).
4. **Presupuesto explícito:** los agentes tienen costo medible; la gobernanza incluye límites de gasto por objetivo ([[Fase 2 - Constraints]]).

## Preguntas abiertas

- ¿Cómo se audita una *cadena* de decisiones entre agentes (Planner → Builder → Reviewer) cuando el error emerge de la composición?
- ¿Qué regulaciones (EU AI Act) y marcos de atestación (SOC 2, ISO/IEC 42001) aplican y cómo mapean a esta matriz? → alimenta [[Riesgos]]
