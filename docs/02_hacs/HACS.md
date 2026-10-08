---
tags: [hacs, definicion]
status: borrador
created: 2026-06-10
---

# HACS — Human-Agent Collaborative Systems

## Definición de trabajo

**HACS es un modelo organizacional para equipos compuestos por humanos, agentes autónomos, memoria organizacional y mecanismos de gobernanza, operando como una única unidad cognitiva distribuida.**

## Hipótesis central

La unidad básica de trabajo deja de ser exclusivamente humana. Los equipos pasan a estar formados por personas y agentes colaborando sobre una memoria compartida. Esta es la tesis fuerte de todo el vault: lo interesante no es la metodología ([[ODLC]]) en sí, sino que **la unidad organizacional cambia de "equipo humano" a "sistema cognitivo humano-agente"**.

## Los cuatro componentes

| Componente | Aporta |
|---|---|
| **Humanos** | Visión, objetivos, restricciones, ética, priorización → [[Roles humanos]] |
| **Agentes** | Análisis, ejecución, verificación de implementación, documentación, monitoreo → [[Roles de agentes]] |
| **Memoria** | Decisiones, evidencia, aprendizaje, contexto histórico → [[Memoria organizacional]] |
| **Gobernanza** | Seguridad, compliance, auditoría, costos → [[Gobernanza]] |

## Infraestructura mínima

Para que los cuatro componentes operen como una unidad, el arnés que corre a los agentes necesita, sea cual sea la herramienta:

- **Memoria compartida** entre humanos y agentes, con las decisiones enlazadas a los commits y PRs que las implementan ([[Memoria organizacional]]).
- **Sandbox aislado** donde los agentes compilan, prueban y analizan sin tocar producción.
- **Verificación por evidencia:** un objetivo se cierra con logs, resultados de tests y métricas contra el objetivo original ([[Fase 5 - Validation]]), no con la palabra del agente.
- **Gobernanza por tipo de acción**, aplicada con controles técnicos que interceptan lo que el agente intenta hacer ([[Gobernanza#Controles técnicos]]).
- **Independencia del modelo:** separar la orquestación del modelo que la ejecuta permite cambiar de proveedor sin rehacer el sistema (hipótesis, sin medir).

## Cuándo un equipo es HACS

HACS queda sin umbral mínimo hasta tener datos del piloto ([[Registro de decisiones]], D-19). Lo único que el marco fija es cuándo se exige el Nivel 3 de [[Modelo de madurez AI-Native]]: cuando hay agentes que escriben en sistemas compartidos (D-02). **Sistema compartido** es un sistema que usan otras personas o clientes y sobre el que el agente tiene permisos de escritura. Un agente que escribe solo en el repo propio del MVP no cae ahí.

## Qué NO es HACS

- No es "IA asistiva" (Copilot dentro de un equipo Scrum sigue siendo nivel 1 del [[Modelo de madurez AI-Native]]).
- No es automatizar trabajo: el objetivo es **amplificar la capacidad colectiva de la organización** ([[Manifiesto HACS-ODLC]]).
- No es eliminar humanos: la gobernanza es explícitamente humana (**Human Governance**).

## Flujo de trabajo base

Objective → Constraints → Strategy → Execution → Validation → Learning. La formalización de este flujo es [[ODLC]].

## Relacionado

[[Unidad organizacional]] · [[Por qué fallan las metodologías actuales]] · [[Riesgos]] · [[Gobernanza]] · [[Agent Loop Engineering]]
