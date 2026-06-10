---
tags: [fundacional, manifiesto, hacs, odlc]
status: evergreen
created: 2026-06-10
---

# Manifiesto HACS-ODLC

> **Declaración Fundacional:**
> "La IA no es una herramienta más. Los agentes no son simples asistentes.
> Los equipos ya no están compuestos únicamente por personas.
> El objetivo no es automatizar trabajo; el objetivo es amplificar la capacidad cognitiva colectiva de una organización."

Como profesionales del desarrollo de software y la ingeniería de sistemas organizacionales, reconocemos que el advenimiento de agentes de software autónomos rompe las suposiciones básicas de las metodologías tradicionales (Scrum, DevOps, Agile). Para prosperar en una era AI-Native, adoptamos una nueva unidad de trabajo y un nuevo modelo de colaboración humano-agente basado en los siguientes cinco valores:

---

## Los 5 Valores Fundamentales

### 1. Intent over Tasks (Intención sobre Tareas)
*Valoramos la definición explícita de la intención por encima de la gestión detallada de tareas.*

- **Por qué**: Escribir, refinar e iterar sobre tickets detallados (historias de usuario, subtareas de Jira) es un proceso pensado para humanos debido a limitaciones de comunicación y velocidad de contexto. Los agentes autónomos pueden descomponer planes complejos en segundos. Lo que requiere el sistema no son micro-instrucciones, sino directrices de alto nivel y metas claras.
- **En la práctica**: Reemplazamos el backlog de historias por una plantilla de objetivos formalizada ([[Fase 1 - Objective]]).

### 2. Outcomes over Output (Resultados sobre Entregables)
*Valoramos el logro de resultados medibles por encima de la cantidad de software producido.*

- **Por qué**: Generar más líneas de código o desplegar más características no equivale a acelerar la organización (ver [[Más código no es más velocidad]]). El código es un costo; el resultado es el valor. La IA reduce el costo de generar código a cero, lo que puede provocar una explosión de deuda técnica si no se orienta el ciclo hacia el éxito de negocio verificado.
- **En la práctica**: El éxito de un ciclo se mide en producción contra el objetivo de negocio original ([[Fase 5 - Validation]]), no contra si las historias se completaron.

### 3. Memory over Documentation (Memoria sobre Documentación)
*Valoramos una memoria viva y participativa por encima de documentación estática.*

- **Por qué**: La documentación tradicional (wikis, READMEs desactualizados, hilos de Slack archivados) es pasiva, difícil de buscar y muere al momento de escribirse. La memoria organizacional debe participar activamente en el ciclo de trabajo de los agentes y humanos, sirviendo de base para justificar decisiones pasadas y evitar resolver problemas ya resueltos.
- **En la práctica**: Diseñamos una [[Memoria organizacional]] que es consultada por los agentes antes de proponer estrategias y es escrita automáticamente en cada cierre de ciclo.

### 4. Evidence over Opinions (Evidencia sobre Opiniones)
*Valoramos la validación respaldada por evidencia empírica por encima de opiniones de diseño.*

- **Por qué**: En sistemas humano-agente complejos, los fallos de comportamiento, sesgos y alucinaciones no pueden gestionarse con especulaciones. Cada decisión debe contrastarse con evidencia dura (logs, pruebas unitarias automatizadas, tests de estrés, métricas de producción).
- **En la práctica**: Toda estrategia de ejecución requiere una prueba de verificación explícita que demuestre que el código resuelve el objetivo.

### 5. Human Governance (Gobernanza Humana)
*Valoramos el control estratégico humano por encima de la autonomía descontrolada de los agentes.*

- **Por qué**: Delegar la responsabilidad del negocio y la ética a agentes autónomos es irresponsable. Los agentes ejecutan, sugieren y validan, pero los humanos lideran la visión y deciden los límites de riesgo aceptables.
- **En la práctica**: Establecemos políticas de [[Gobernanza]] claras donde el despliegue a producción, cambios críticos de arquitectura y aprobación de presupuestos requieren supervisión humana.

---

Al priorizar los elementos de la izquierda sobre los de la derecha, cambiamos la escala del desarrollo de software: de un ciclo de producción a un **ciclo de aprendizaje continuo orientado a objetivos**.

---
Relacionado: [[HACS]] · [[ODLC]] · [[Por qué fallan las metodologías actuales]]
