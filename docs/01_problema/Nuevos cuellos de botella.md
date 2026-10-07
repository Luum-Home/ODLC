---
tags: [problema, hipotesis]
status: borrador
created: 2026-06-10
---

# Nuevos cuellos de botella

Cuando los agentes abaratan la ejecución, el cuello de botella se desplaza. El problema deja de ser **producir código** y pasa a ser **convertir conocimiento distribuido en decisiones correctas y resultados medibles**.

## El desplazamiento

| Antes (cuello de botella) | Ahora (cuello de botella) |
|---|---|
| Código | **Contexto** |
| Implementación | **Decisión** |
| Entrega | **Validación** |
| Documentación | **Memoria** |

## Los cinco cuellos de botella actuales

1. **Comprensión del problema** — entender qué hay que resolver antes de resolver nada.
2. **Toma de decisiones** — elegir entre alternativas con tradeoffs, con evidencia incompleta.
3. **Alineación organizacional** — que todos (humanos y agentes) empujen hacia el mismo objetivo.
4. **Fragmentación del contexto y pérdida de memoria** — el conocimiento vive disperso en cabezas, chats, tickets y docs desactualizados.
5. **Validación** — confirmar que el resultado logró el objetivo, no solo que el código compila.

## Observaciones

- Cada uno de estos cuellos mapea a un componente de [[HACS]]: comprensión del problema → [[Fase 1 - Objective]] + [[Roles humanos]] (rol Product); contexto/memoria → [[Memoria organizacional]]; decisión → [[Roles humanos]] + [[Gobernanza]]; validación → [[Fase 5 - Validation]]; alineación → [[Fase 1 - Objective]].
- El foco pasa de "líneas de código generadas" a "tiempo desde la definición del objetivo hasta la validación del outcome" (Time To Outcome, [[Métricas operativas]]) → [[Más código no es más velocidad]].

## Preguntas abiertas

- ¿Cómo se *mide* cada cuello de botella hoy, para poder demostrar el desplazamiento? Candidatos: [[Métricas organizacionales]] (Context Retrieval Time, Decision Lead Time).
