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
| **0** | **Tradicional** | Procesos y herramientas diseñados y ejecutados exclusivamente por humanos. | Scrum tradicional, Jira, revisiones manuales, documentación en wikis estáticos. |
| **1** | **IA Asistiva** | Los humanos usan herramientas de IA de forma individual para acelerar su trabajo diario. | Copilot en el IDE, chat con LLMs para resolver dudas de código. La IA no tiene contexto compartido ni autonomía. |
| **2** | **Agentes Especializados** | Se introducen agentes autónomos aislados para ejecutar tareas concretas y repetitivas. | Agente de revisión de PRs automático, generador de tests unitarios al compilar. Sin memoria común. |
| **3** | **Memoria Organizacional** | Agentes y humanos colaboran utilizando un sustrato de conocimiento compartido y estructurado. | Los agentes leen y escriben en la [[Memoria organizacional]] (ADRs, lecciones aprendidas). Se reduce el Context Retrieval Time. |
| **4** | **ODLC Pleno** | La organización adopta la metodología orientada a objetivos y restricciones. La ejecución es mayormente autónoma. | Adopción total de [[ODLC]]. El agente Planner orquesta sub-agentes bajo límites estrictos de [[Gobernanza]] humana. |
| **5** | **Organización Autónoma** | Unidades HACS adaptativas autogestionadas. Múltiples agentes coordinan y refinan sub-objetivos de negocio. | El humano interviene únicamente para gobernar objetivos estratégicos y presupuestos globales. Auto-remediación en producción. |

---

## Criterios de Evaluación y Transición

Para transicionar de un nivel a otro, la organización debe medir y cumplir ciertos umbrales operativos:

- **De Nivel 1 a Nivel 2**: Integrar pipelines de CI/CD con llamadas automatizadas a agentes (ej. CodeRabbit, Snyk). Medir el *Agent Contribution Ratio* inicial.
- **De Nivel 2 a Nivel 3**: Implementar bases de datos vectoriales de contexto de arquitectura y decisiones históricas (ADRs) conectadas a los agentes. Medir la tasa de reutilización (*Knowledge Reuse Rate*).
- **De Nivel 3 a Nivel 4**: Reemplazar la unidad de trabajo del método vigente (historias y sprints en Scrum, tarjetas en un tablero Kanban, tickets de Jira) por plantillas de objetivos e implementar entornos seguros de Sandbox para la validación autónoma de agentes.

> [!warning] Transiciones sin definir
> Los criterios de **0 → 1** y **4 → 5** todavía no están escritos. El modelo describe los seis niveles en la tabla de arriba, pero solo especifica cómo se cruzan tres de los cinco umbrales. No se completan acá de forma especulativa: definirlos exige decidir qué evidencia habilita el salto, y esa es una definición del autor, no una omisión de redacción. Ver [[Modelo de madurez AI-Native#Preguntas abiertas|Preguntas abiertas]].

---

## Hipótesis

- **H1**: Intentar saltar directamente del Nivel 1 al Nivel 4 sin consolidar la [[Memoria organizacional]] (Nivel 3) resulta en fallos de ejecución catastróficos debido a alucinaciones de contexto de los agentes.
- **H2**: A partir del Nivel 4, el *Time To Outcome* (TTO) se reduce en más del 60% comparado con organizaciones tradicionales en Nivel 1 o 2.

## Decisiones

- **D1**: Se establece el **Nivel 3** como el estándar mínimo requerido para iniciar cualquier proyecto piloto de desarrollo de agentes autónomos en la empresa.

## Preguntas abiertas

- ¿Qué habilita la transición **0 → 1**? ¿Alcanza con la adopción individual de herramientas de IA, o hay un umbral mínimo de uso sostenido que distinga "probamos Copilot" de "el equipo trabaja en Nivel 1"?
- ¿Qué habilita la transición **4 → 5**? El Nivel 5 supone auto-remediación en producción y coordinación multi-agente de sub-objetivos: falta definir qué evidencia de confiabilidad justifica retirar al humano de la ejecución.
- ¿Cómo auditar la madurez de manera objetiva sin depender puramente de autoevaluaciones del equipo?
- ¿El Nivel 5 es deseable para todas las industrias, o sectores regulados (como fintech o salud) deben detenerse permanentemente en el Nivel 4?

---
Relacionado: [[HACS]] · [[ODLC]] · [[Memoria organizacional]] · [[Gobernanza]]
