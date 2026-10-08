---
tags: [fundacional, madurez, hacs, odlc]
status: borrador
created: 2026-06-10
---

# Modelo de madurez AI-Native

El **Modelo de madurez AI-Native** ayuda a las organizaciones a evaluar cómo integran la inteligencia artificial en su ciclo de desarrollo de software y en su estructura de trabajo. El modelo describe la evolución desde el desarrollo puramente humano (Nivel 0) hasta las organizaciones adaptativas autogestionadas por objetivos (Nivel 5).

---

## Definición de los Niveles de Madurez

| Nivel | Nombre | Descripción | Características Clave |
|---|---|---|---|
| **0** | **Tradicional** | Procesos y herramientas diseñados y ejecutados exclusivamente por humanos. | Métodos ágiles ejecutados solo por humanos, trackers manuales, revisiones manuales, documentación en wikis estáticos. |
| **1** | **IA Asistiva** | Los humanos usan herramientas de IA de forma individual para acelerar su trabajo diario. | Copilot en el IDE, chat con LLMs para resolver dudas de código. La IA no tiene contexto compartido ni autonomía. |
| **2** | **Agentes Especializados** | Se introducen agentes autónomos aislados para ejecutar tareas concretas y repetitivas. | Agente de revisión de PRs automático, generador de tests unitarios al compilar. Sin memoria común. |
| **3** | **Memoria Organizacional** | Agentes y humanos colaboran utilizando un sustrato de conocimiento compartido y estructurado. | Los agentes leen y escriben en la [[Memoria organizacional]] (ADRs, lecciones aprendidas). Se reduce el Context Retrieval Time. |
| **4** | **ODLC Pleno** | La organización adopta la metodología orientada a objetivos y restricciones. La ejecución es mayormente autónoma. | Adopción total de [[ODLC]]. El agente Planner orquesta sub-agentes bajo límites estrictos de [[Gobernanza]] humana. |
| **5** | **Organización Autónoma** | Unidades HACS adaptativas autogestionadas. Múltiples agentes coordinan y refinan sub-objetivos de negocio. | El humano deja la ejecución táctica: gobierna objetivos estratégicos y presupuestos globales, y conserva la aprobación de lo irreversible (pagos, datos de clientes, borrado, migraciones destructivas), que no se relaja con la madurez ([[Registro de decisiones]], D-01). Auto-remediación en producción dentro de la matriz de [[Gobernanza]]. |

> [!note] El Nivel 5 usa vocabulario Teal
> "Autogestionadas" viene de las organizaciones Teal (Frederic Laloux, *Reinventing Organizations*, 2014), donde la autogestión reemplaza la aprobación jerárquica por el *advice process* y desconfía de metas y pronósticos. La convivencia con la matriz de aprobaciones humanas de [[Gobernanza]] quedó fijada: la autogestión alcanza la ejecución táctica y lo irreversible sigue con aprobación humana ([[Registro de decisiones]], D-01). Lo que el nivel todavía no define es cómo convive con un marco centrado en métricas. Detalle: [[Objeciones al marco#Objeción 6: el Nivel 5 habla de autogestión sin definirla]] y [[Comparativa con metodologías existentes]].

---

## Criterios de Evaluación y Transición

Para transicionar de un nivel a otro, la organización debe medir y cumplir condiciones de entrada (los umbrales numéricos todavía no están calibrados):

- **De Nivel 1 a Nivel 2**: Integrar pipelines de CI/CD con llamadas automatizadas a agentes (ej. CodeRabbit, Snyk). Medir el *Agent Contribution Ratio* inicial.
- **De Nivel 2 a Nivel 3**: Conectar a los agentes un almacén recuperable de decisiones históricas (ADRs, postmortems), con la tecnología que sea. Medir la tasa de reutilización (*Knowledge Reuse Rate*).
- **De Nivel 3 a Nivel 4**: Pasar a plantillas de objetivos como unidad de trabajo. En equipos existentes, de a poco y conviviendo con la unidad del método vigente (Product Backlog Items y Sprints en Scrum, work items en Kanban, tickets en un tracker); el reemplazo directo queda para equipos que arrancan desde cero ([[Registro de decisiones]], D-03). Además, implementar entornos seguros de Sandbox para la validación autónoma de agentes.

> [!warning] Transiciones sin definir
> Los criterios de **0 → 1** y **4 → 5** todavía no están escritos. El modelo describe los seis niveles en la tabla de arriba, pero solo especifica cómo se cruzan tres de los cinco umbrales. No se completan acá de forma especulativa: definirlos exige decidir qué evidencia habilita el salto, y esa es una definición del autor, no una omisión de redacción. Ver [[Modelo de madurez AI-Native#Preguntas abiertas|Preguntas abiertas]].

---

## Hipótesis

- **H1**: Intentar saltar directamente del Nivel 1 al Nivel 4 sin consolidar la [[Memoria organizacional]] (Nivel 3) resulta en fallos de ejecución catastróficos debido a alucinaciones de contexto de los agentes.
- **H2**: A partir del Nivel 4, el *Time To Outcome* (TTO) se reduce en más del 60% comparado con organizaciones tradicionales en Nivel 1 o 2.

## Decisiones

- **D1**: Se exige el **Nivel 3** para iniciar un piloto solo cuando los agentes escriben en sistemas compartidos. Para adoptar ODLC alcanza con usar la ficha de objetivo con criterio de abandono y registrar el resultado validado ([[Núcleo ODLC para tiny teams]]), desde cualquier nivel ([[Registro de decisiones]], D-02).

## Preguntas abiertas

- ¿Qué habilita la transición **0 → 1**? ¿Alcanza con la adopción individual de herramientas de IA, o hay un umbral mínimo de uso sostenido que distinga "probamos Copilot" de "el equipo trabaja en Nivel 1"?
- ¿Qué habilita la transición **4 → 5**? El Nivel 5 supone auto-remediación en producción y coordinación multi-agente de sub-objetivos: falta definir qué evidencia de confiabilidad justifica retirar al humano de la ejecución táctica (lo irreversible no se retira, D-01).
- ¿Cómo auditar la madurez de manera objetiva sin depender puramente de autoevaluaciones del equipo?
- ¿El Nivel 5 es deseable para todas las industrias, o sectores regulados (como fintech o salud) deben detenerse permanentemente en el Nivel 4?

---
Relacionado: [[HACS]] · [[ODLC]] · [[Memoria organizacional]] · [[Gobernanza]]
