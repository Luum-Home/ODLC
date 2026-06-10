---
tags: [hacs, roles, agentes]
status: semilla
created: 2026-06-10
---

# Roles de agentes

Los agentes en [[HACS]] aportan: **análisis, ejecución, validación, documentación y monitoreo**. Operan dentro de los límites definidos por la [[Gobernanza]] y leen/escriben la [[Memoria organizacional]].

| Agente | Función (borrador) |
|---|---|
| **Planner** | Descompone objetivos en planes ejecutables; propone secuencia y dependencias |
| **Architect** | Propone arquitecturas, ADRs y modelos de datos; analiza tradeoffs para [[Fase 3 - Strategy]] |
| **Builder** | Genera código, infraestructura, migraciones y documentación técnica |
| **Reviewer** | Revisa código y artefactos contra estándares, specs y decisiones previas en memoria |
| **Security** | Detecta vulnerabilidades, propone fixes, audita dependencias y configuraciones |
| **Memory** | Captura decisiones, evidencia y aprendizajes; mantiene la memoria recuperable y curada |

Equivale al pipeline multi-agente del [[AI SDLC]] avanzado (PM Agent → Architect Agent → Developer Agent → Tester Agent → Security Agent → DevOps Agent), pero con dos diferencias: comparten [[Memoria organizacional]] como sustrato común, y operan bajo límites de autonomía explícitos.

## Hipótesis

- La especialización por rol (vs. un agente generalista) mejora trazabilidad y auditoría, aunque los modelos subyacentes sean el mismo. El rol es un *contrato*, no una capacidad técnica distinta.

## Preguntas abiertas

- ¿Falta un agente *Tester* explícito o es parte de Reviewer? ¿Y un agente *Ops/Observability*?
- ¿Cómo se mide la contribución y precisión de cada agente? → [[Métricas de agentes]]
- ¿Qué pasa cuando dos agentes proponen estrategias contradictorias? ¿Quién arbitra — Planner o un humano ([[Roles humanos]])?
