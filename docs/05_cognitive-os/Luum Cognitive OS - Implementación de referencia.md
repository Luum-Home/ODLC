---
tags: [cognitive-os, implementacion, gobernanza, safety-mesh]
status: borrador
created: 2026-06-10
fuente: "https://github.com/Luum-Home/luum-cognitive-os (consultado 2026-06-10)"
---

# Luum Cognitive OS — Implementación de referencia

Implementación técnica de la [[Gobernanza]] de [[HACS]]: [luum-cognitive-os](https://github.com/Luum-Home/luum-cognitive-os), una capa de gobernanza y malla de seguridad para agentes de programación desarrollada en colaboración entre **Luum** y **OliveX**. No es un framework de agentes, sino una capa que se monta sobre herramientas existentes (Claude Code, Cursor, Codex) para interceptar acciones no autorizadas.

Esta nota documenta el **CÓMO** técnico. El **QUÉ** conceptual (principios y matriz de autonomía) vive en [[Gobernanza]].

En términos de [[Agent Loop Engineering]], `luum-cognitive-os` no reemplaza el loop del agente: lo gobierna. Sus hooks intervienen action policy, observation parsing, termination, retries, claim validation, budgets y rollback.

## La Malla de Seguridad de 14 Capas (Safety Mesh)

`luum-cognitive-os` intercepta las llamadas de los agentes en el ciclo de vida del CLI usando hooks (`PreToolUse` / `PostToolUse`). La tabla completa de las 14 capas está documentada en [[Módulo 3 - Gobernanza]]. Las cinco capas más representativas:

1. **Prevención de Resultados Fabricados (`claim-validator.sh`, capa 6)**: Evita que los agentes reporten tests pasados o tareas listas sin haber corrido físicamente los comandos de prueba. Su comportamiento depende de la fase del proyecto (*Phase Awareness*): en fases de Reconstrucción/Estabilización alerta (**WARN**); en Producción/Mantenimiento **bloquea** ante cualquier discrepancia.
2. **Control de Radio de Impacto (`blast-radius.sh`, capa 2)**: Advierte si el agente intenta modificar archivos o directorios fuera del alcance de trabajo seguro definido en las restricciones ([[Fase 2 - Constraints]]).
3. **Prevención de Bucles y Costos Descontrolados (`rate-limiter.sh`, capa 4)**: Limita llamadas a herramientas, generación de subagentes y gasto de tokens por hora para evitar bucles infinitos.
4. **Validación de Confianza (`trust-score-validator.sh`, capa 8)**: Hook `PostToolUse` sobre la salida del agente que busca un Trust Report (score, evidencia, incertidumbres, pasos de verificación humana). Si falta, emite un **WARN** y deja seguir; si está malformado (hay marcador de score pero no se puede parsear), **bloquea** (exit 2). Cuando el reporte es válido, registra el score en `.cognitive-os/metrics/trust-scores.jsonl`.
5. **Reversión Automática (`auto-rollback-trigger.sh`, capa 11)**: Revierte los cambios a un estado limpio si el agente falla en estabilizar el build tras agotar su límite de reintentos.

## Principios de diseño de la malla

- **Defensa en profundidad**: cada capa atiende un riesgo distinto; deshabilitar una crea un punto ciego que las demás no cubren.
- **Espectro de control**: no todo bloquea — las capas se clasifican en BLOCK / WARN / LOG según su impacto.
- **Sensibilidad de fase**: la malla es permisiva en fases tempranas y estricta en producción, según `cognitive-os.yaml`.

Es la materialización del principio de [[Gobernanza]] "autonomía ganada, no otorgada", y del criterio de reversibilidad.

## Relacionado

[[Gobernanza]] · [[Cognitive OS - Arquitectura de referencia]] · [[Agent Loop Engineering]] · [[Módulo 3 - Gobernanza]] · [[Módulo 4 - Ciberseguridad aplicada]] · [[Recursos externos]]
