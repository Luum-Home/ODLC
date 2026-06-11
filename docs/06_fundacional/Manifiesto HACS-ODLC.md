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

Como profesionales del desarrollo de software y la ingeniería de sistemas organizacionales, reconocemos que el advenimiento de agentes de software autónomos rompe las suposiciones básicas de las metodologías tradicionales (Scrum, DevOps, Agile). Para prosperar en una era AI-Native, adoptamos una nueva unidad de trabajo y un nuevo modelo de colaboración humano-agente basado en los siguientes seis valores:

> Los cinco primeros valores provienen de los canvases fundacionales (PDFs en la raíz del repo); el sexto (Purpose over Technology) fue incorporado durante la evolución del vault.

---

## Los 6 Valores Fundamentales

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

### 6. Purpose over Technology (Propósito sobre Tecnología)
*Valoramos el propósito y el resultado por encima de la tecnología, el framework o el lenguaje específico.*

- **Por qué**: El código, el framework, la base de datos y el lenguaje son medios para alcanzar un objetivo, no fines en sí mismos. Atarse a una tecnología específica convierte al equipo en rehén de decisiones transitorias en un entorno donde los modelos, frameworks y proveedores cambian cada trimestre. La arquitectura correcta es la que permite reemplazar cualquier componente sin rescribir el sistema ([[Nuevos cuellos de botella]], [[Producción de software vs. velocidad real]]).
- **En la práctica**: Diseñamos sistemas con arquitectura limpia (puertos y adaptadores), interfaces estables y protocolos abiertos (MCP, OpenAPI). Los agentes son agnósticos al modelo LLM subyacente. Las decisiones tecnológicas se documentan como ADRs descartables; las decisiones de propósito y restricciones de negocio permanecen en [[Memoria organizacional]].

---

## El Manifiesto ODLC

De los canvases fundacionales, la declaración operativa que resume el ciclo:

> **"No optimizamos la producción de software.**
> **Optimizamos el logro de objetivos.**
> **El código es un medio.**
> **El resultado es el producto.**
> **Todo ciclo debe producir aprendizaje.**
> **Todo aprendizaje debe alimentar el siguiente objetivo."**

Al priorizar los elementos de la izquierda sobre los de la derecha, cambiamos la escala del desarrollo de software: de un ciclo de producción a un **ciclo de aprendizaje continuo orientado a objetivos**.

---

## Adaptación sobre imposición (cómo adoptar este manifiesto)

Como el Manifiesto Ágil, esto es una **declaración de valores, no un proceso a imponer**. HACS y ODLC deben adaptarse al contexto y las circunstancias de cada organización; imponerlos como dinámica rígida repite el error que convirtió a Agile en ceremonia vacía.

- **Esto se construye antes de tiempo, a propósito.** El marco se diseña para el camino hacia sistemas cada vez más capaces (AGI / superinteligencia), donde la unidad humano-agente será la norma. Que el destino sea ese no significa que hoy se adopte completo.
- **Cherry-picking deliberado.** Ante las falencias actuales de los modelos (alucinaciones, deriva de contexto, costo, validación inmadura — ver [[Riesgos]]), se aconseja **seleccionar los pasos, fases y herramientas que aporten valor hoy** y dejar el resto documentado para cuando la capacidad de los modelos lo habilite. Adoptar la [[Fase 1 - Objective]] y la [[Fase 6 - Learning]] sin agentes ya es ODLC; usar la matriz de [[Gobernanza]] con un solo agente ya es HACS.
- **El nivel de adopción lo marca la madurez, no la ambición.** El [[Modelo de madurez AI-Native]] existe exactamente para esto: cada nivel habilita prácticas nuevas; saltar niveles impone un marco que el sistema (humanos + modelos) todavía no puede sostener.
- **La evidencia decide qué se adopta.** Cada práctica incorporada se valida contra resultados ([[Fase 5 - Validation]]); lo que no aporta en tu contexto, se descarta sin culpa — y eso también es aprendizaje.

---
Relacionado: [[HACS]] · [[ODLC]] · [[Modelo de madurez AI-Native]] · [[Riesgos]] · [[Por qué fallan las metodologías actuales]]
