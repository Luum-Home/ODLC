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

---

## Términos del Sistema

- **HACS (Human-Agent Collaborative Systems)**: El modelo organizacional que define a los equipos de software como unidades cognitivas distribuidas de humanos y agentes sobre una memoria compartida. Ver [[HACS]].
- **ODLC (Objective Driven Lifecycle)**: La metodología de trabajo ágil e iterativa de HACS que desplaza el foco del código hacia la consecución de objetivos y el aprendizaje continuo. Ver [[ODLC]].
- **Cognitive OS**: La capa de arquitectura de software y tooling de soporte que materializa el funcionamiento lógico de HACS y ODLC. Ver [[Cognitive OS - Arquitectura de referencia]].

---
Relacionado: [[README]] · [[Manifiesto HACS-ODLC]] · [[Fase 6 - Learning]]
