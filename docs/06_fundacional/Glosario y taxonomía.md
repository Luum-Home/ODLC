---
tags: [fundacional, taxonomía, glosario]
status: evergreen
created: 2026-06-10
---

# Glosario y taxonomía

Este documento define la taxonomía y el vocabulario formal (Ubiquitous Language) del marco **HACS + ODLC**. Establecer definiciones precisas de primeros principios es fundamental para alinear tanto a humanos como a agentes autónomos que interactúan en el sistema.

---

## Conceptos Core (La Taxonomía)

### 1. Objective (Objetivo)
- **Definición**: La meta de negocio medible, acotada en el tiempo, que inicia un ciclo de trabajo.
- **Propósito**: Reemplaza al ticket tradicional o la historia de usuario. Define *qué* resultado se quiere lograr, no *cómo* se debe codificar.
- **Ver en el vault**: [[Fase 1 - Objective]].

### 2. Constraint (Restricción)
- **Definición**: Los límites infranqueables dentro de los cuales debe alcanzarse el objetivo. Pueden ser financieros, técnicos, regulatorios, temporales o humanos.
- **Propósito**: Acota el espacio de soluciones posibles para los agentes y define los límites de seguridad del sistema.
- **Ver en el vault**: [[Fase 2 - Constraints]].

### 3. Strategy (Estrategia)
- **Definición**: La propuesta de solución técnica y operativa que equilibra las restricciones para lograr el objetivo.
- **Propósito**: Estructura el debate de alternativas y tradeoffs arquitectónicos antes de iniciar cualquier desarrollo.
- **Ver en el vault**: [[Fase 3 - Strategy]].

### 4. Evidence (Evidencia)
- **Definición**: Datos empíricos, resultados de pruebas, logs de producción e informes de métricas que demuestran la consecución del objetivo.
- **Propósito**: Elimina la especulación y las opiniones sobre si una funcionalidad en producción realmente cumple la meta del negocio.
- **Ver en el vault**: [[Fase 5 - Validation]].

### 5. Memory (Memoria)
- **Definición**: El almacén persistente, estructurado y recuperable de conocimiento que comparten humanos y agentes.
- **Propósito**: Proporciona contexto evolutivo para evitar la amnesia organizacional y acelerar la toma de decisiones.
- **Ver en el vault**: [[Memoria organizacional]].

### 6. Agent (Agente)
- **Definición**: Entidad autónoma de software impulsada por LLMs con un rol y contrato de capacidades definidos dentro del flujo.
- **Propósito**: Ejecuta tareas cognitivas complejas (código, testing, seguridad, curaduría de contexto).
- **Ver en el vault**: [[Roles de agentes]].

### 7. Governance (Gobernanza)
- **Definición**: El conjunto de reglas, permisos y autorizaciones reguladas por humanos que acotan el nivel de autonomía de los agentes.
- **Propósito**: Garantiza que las acciones críticas (como el despliegue a producción o gastos de presupuesto) requieran validación humana.
- **Ver en el vault**: [[Gobernanza]].

### 8. Outcome (Resultado)
- **Definición**: El cambio observable en el negocio o en el comportamiento de los usuarios que produce un ciclo de trabajo, verificado con [[Glosario y taxonomía#4. Evidence (Evidencia)|Evidencia]]. Se distingue del *output* (el entregable producido: código, documento, despliegue): "lanzar el módulo X" es output, "reducir el churn 2 puntos" es outcome.
- **Propósito**: Es la unidad de éxito de [[ODLC]] — un objetivo se cierra cuando su outcome está validado, no cuando el entregable está en producción. Sostiene el valor *Outcomes over Output* del [[Manifiesto HACS-ODLC]] y es lo que miden el *Objective Success Rate* y el *Time To Outcome*.
- **Ver en el vault**: [[Fase 1 - Objective]] · [[Fase 5 - Validation]] · [[Métricas operativas]].

### 9. Sandbox (Entorno de Ejecución)
- **Definición**: El entorno aislado y con permisos acotados donde los agentes ejecutan acciones con efectos reales (CLI, Git, compilador, test runner) sin alcanzar directamente los sistemas productivos.
- **Propósito**: Separa la orquestación lógica del agente de la ejecución física, de modo que un error o una alucinación tenga un radio de impacto contenido. Es donde se materializan los límites de la [[Gobernanza]] en tiempo de ejecución y donde se recolecta buena parte de la evidencia de validación.
- **Ver en el vault**: [[Cognitive OS - Arquitectura de referencia]] · [[Gobernanza]].

---

## Términos del Sistema

- **HACS (Human-Agent Collaborative Systems)**: El modelo organizacional que define a los equipos de software como unidades cognitivas distribuidas de humanos y agentes sobre una memoria compartida. Ver [[HACS]].
- **ODLC (Objective Driven Lifecycle)**: La metodología de trabajo iterativa de HACS, heredera de los valores del Manifiesto Ágil ([[Relectura del Manifiesto Ágil]]), que desplaza el foco del código hacia la consecución de objetivos y el aprendizaje continuo. Ver [[ODLC]].
- **Cognitive OS**: La capa de arquitectura de software y tooling de soporte que materializa el funcionamiento lógico de HACS y ODLC. Ver [[Cognitive OS - Arquitectura de referencia]].
- **Agent Loop Engineering**: Disciplina de diseño del loop de control de un agente: trigger, goal, state, action policy, observation parser, termination, memory update, guardrails, tracing y evals. Ver [[Agent Loop Engineering]].

---

## Términos de Arneses y Arbitraje

Patrones operativos usados en la implementación técnica ([[Luum Cognitive OS - Implementación de referencia]]) y en el programa de cursos ([[Módulo 2 - Ingeniería de arneses]]).

- **Arnés (Harness)**: Entorno lógico que envuelve al LLM unificando contexto, herramientas, memoria externa y validaciones automáticas. Hace al sistema agnóstico al modelo.
- **Agent Loop (Bucle de Agente)**: Ciclo repetible en el que un agente observa, razona/planifica, actúa con herramientas, interpreta resultados, actualiza estado/memoria y decide si termina, reintenta o escala.
- **Safety Mesh (Malla de Seguridad)**: Conjunto de interceptores independientes (hooks `PreToolUse`/`PostToolUse`) que aplican la [[Gobernanza]] en tiempo de ejecución, con comportamientos BLOCK/WARN/LOG sensibles a la fase del proyecto.
- **HITL (Human-in-the-Loop)**: Compuerta donde el agente pausa su ejecución y espera aprobación humana explícita antes de continuar (deploys, esquemas de datos, secretos).
- **Ground Truth Checker**: Validador determinista que contrasta los reclamos de éxito del agente ("tests pasan", "archivo creado") contra la realidad del sistema de archivos, generando un puntaje de alucinación.
- **Judgment Day (Día de la Justicia)**: Patrón de arbitraje cognitivo donde el código generado por un agente es evaluado por jueces independientes antes de integrarse — el autor nunca juzga su propio trabajo.
- **Dual Blind Review**: Mecanismo del Judgment Day: dos agentes revisores aislados evalúan el mismo código sin ver el veredicto del otro.
- **Agente Optimista / Agente Pesimista**: Perfiles de los jueces del Dual Blind Review. El optimista valida que el flujo de negocio funcione ("inocente hasta demostrar lo contrario"); el pesimista busca vulnerabilidades, race conditions y fallas de manejo de errores ("culpable hasta demostrar lo contrario").
- **Compuertas de Arbitraje (Confirmed / Suspect / Contradictions)**: Reglas de consolidación de veredictos: defectos confirmados por ambos jueces van al Fix Agent; los señalados por uno solo se marcan; las contradicciones estructurales escalan a un humano como árbitro.
- **Fix Agent**: Agente de corrección que refactoriza quirúrgicamente los defectos confirmados por el arbitraje.

---
Relacionado: [[README]] · [[Manifiesto HACS-ODLC]] · [[Fase 6 - Learning]] · [[Agent Loop Engineering]]
