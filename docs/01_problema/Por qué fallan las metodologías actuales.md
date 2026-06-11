---
tags: [problema, hipotesis, metodologias, metricas]
status: borrador
created: 2026-06-10
---

# Por qué fallan las metodologías actuales

Las metodologías y marcos de trabajo dominantes en la industria del software fueron diseñados para resolver problemas de eras pasadas. Al analizar su propósito de diseño original, se hace evidente por qué resultan inadecuadas frente al paradigma de desarrollo asistido por agentes:

*   **Waterfall (Cascada)**: Fue diseñada para proyectos con requerimientos altamente previsibles y estables, donde el costo de cambiar el diseño físico o lógico a mitad de camino era prohibitivo.
*   **Scrum / Agile**: Fueron creadas para gestionar la **incertidumbre funcional** mediante ciclos cortos de retroalimentación, asumiendo que la coordinación entre humanos con ancho de banda y velocidad limitados es el principal reto.
*   **DevOps**: Fue diseñada para acelerar y automatizar la **entrega y operación** del software (acortando el camino entre el commit humano y producción).
*   **Platform Engineering (Ingeniería de Plataformas)**: Fue estructurada para **escalar equipos humanos** reduciendo su carga cognitiva a través de portales de autoservicio (IDPs) y caminos dorados (*golden paths*).
*   **AI Engineering (Ingeniería de IA)**: Se enfoca en la arquitectura técnica para **construir productos que integran IA** (evaluaciones, bases de datos vectoriales y APIs de LLM).

## El Nuevo Contexto no Contemplado

Ninguno de los marcos anteriores fue diseñado para operar en un contexto caracterizado por las siguientes dinámicas de desarrollo autónomo:

1.  **Orquestación de Multi-Agentes**: Un único desarrollador humano actúa como supervisor de **varios agentes autónomos trabajando en paralelo** (hipótesis de orden de magnitud: 5 a 10; pendiente de evidencia empírica).
2.  **Generación de Código e Infraestructura Autónoma**: Los Pull Requests (PRs) se generan automáticamente por agentes de codificación.
3.  **Higiene Documental Autónoma**: La documentación del sistema se escribe, refactora y actualiza sola tras cada cambio en el código.
4.  **Validación de Pruebas Autónoma**: Los casos de prueba, unitarios y de integración se auto-generan y se corrigen solos al mutar las firmas del código.
5.  **Requerimientos Volátiles**: Los objetivos e intenciones de negocio cambian a nivel de requerimientos diariamente.
6.  **Costo Marginal Cero**: El costo marginal de producir una nueva línea de código o infraestructura lógica tiende a cero.

---

## Lo que está Muriendo: La Obsolescencia de las Métricas Tradicionales

En esta nueva realidad, las métricas tradicionales de productividad y gestión de proyectos pierden su significado y se vuelven inútiles (o fácilmente manipulables por los agentes):

*   **Story Points (Puntos de Historia)**: Diseñados para medir la complejidad percibida y el esfuerzo humano. Pierden sentido cuando un agente puede escribir una API completa en segundos o minutos (cifra ilustrativa, no medida: el punto es que el esfuerzo humano dejó de ser proporcional al volumen producido).
*   **Velocity (Velocidad de Sprint)**: El concepto de medir cuántas tareas o puntos puede completar un equipo en dos semanas carece de relevancia cuando la producción es instantánea y el cuello de botella se traslada a la toma de decisiones y validaciones.
*   **Burndown Charts (Gráficos de Trabajo Pendiente)**: Monitorear el progreso diario de tareas humanas en un sprint de tiempo fijo es obsoleto ante bucles de agentes que resuelven backlogs enteros de forma asíncrona.
*   **Número de PRs y Líneas de Código**: Convertir el volumen de entregas en una métrica de rendimiento incentiva a los agentes a inundar el repositorio con código innecesario, aumentando la deuda técnica y los costos de contexto.

---

## Por qué ODLC tiene Sentido

Dado que el código se ha vuelto un comodity y su costo marginal tiende a cero, el verdadero reto ya no es *escribir* el programa, sino **garantizar que el software construido satisfaga los objetivos reales del negocio dentro de los límites de seguridad y gobernanza**.

Aquí es donde entra **ODLC** (Objective-Driven Lifecycle), estructurando el ciclo de vida alrededor de objetivos probabilísticos en lugar de tareas deterministas:

$$\text{Objective} \longrightarrow \text{Constraints} \longrightarrow \text{Strategy} \longrightarrow \text{Execution} \longrightarrow \text{Validation} \longrightarrow \text{Learning}$$

-   **Objective (Objetivo)**: Define la intención última (el *outcome* deseado), con métrica de éxito y dueño humano → [[Fase 1 - Objective]].
-   **Constraints (Restricciones)**: Presupuesto (incluido el de tokens), tecnología, regulación, seguridad y personas; los límites de autonomía de agentes son un subconjunto, no el todo → [[Fase 2 - Constraints]].
-   **Strategy (Estrategia)**: Los agentes proponen alternativas con tradeoffs y evidencia; **la decisión es humana** (Human Governance) → [[Fase 3 - Strategy]].
-   **Execution (Ejecución)**: Escritura e implementación autónoma mediada por arneses locales, bajo la matriz de [[Gobernanza]] → [[Fase 4 - Execution]].
-   **Validation (Validación)**: Pruebas de caja negra, Ground Truth Checking y arbitraje ciego para asegurar el cumplimiento del objetivo, validando contra el objetivo y no contra la implementación → [[Fase 5 - Validation]].
-   **Learning (Aprendizaje)**: Resumen y persistencia de memoria (memorias persistentes) para la siguiente iteración → [[Fase 6 - Learning]].

---
Relacionado: [[Comparativa con metodologías existentes]] · [[HACS]] · [[Nuevos cuellos de botella]] · [[Más código no es más velocidad]]

