---
tags: [problema, evidencia]
status: borrador
created: 2026-06-10
---

# Más código no es más velocidad

> "More AI-generated code doesn't make your team faster." — AWS (@awscloud en X, 2026-06-09: https://x.com/awscloud/status/2064449711155589396; hilo que presenta un episodio con Charity Majors, de Honeycomb)
>
> Verificación (2026-10-07): `curl -sL https://api.fxtwitter.com/awscloud/status/2064449711155589396 | python3 -c "import json,sys; t=json.load(sys.stdin)['tweet']; print(t['created_at'], t['text'])"`

Generar más código con IA no necesariamente mejora el SDLC completo. Si después hay **más bugs, más revisiones, más deuda técnica y más mantenimiento**, el resultado final puede ser incluso **más lento**.

## Por qué importa

Es la refutación directa de la métrica naïve del "AI coding" (líneas generadas, % de código escrito por IA). La aceleración local de una fase ([[AI SDLC]]) puede *empeorar* el throughput global si las fases siguientes —review, testing, validación, mantenimiento— no escalan al mismo ritmo. Es teoría de restricciones aplicada: optimizar una etapa que no es el cuello de botella no mejora el sistema.

## Consecuencia metodológica

El foco se mueve de **output** (código generado) a **outcome** (valor en producción):

- Métrica vieja: líneas de código, story points, velocity.
- Métrica nueva: **tiempo desde la definición del objetivo hasta la validación del outcome** → [[Métricas operativas]] (Time To Outcome).

Este es el fundamento del principio **Outcomes over Output** del [[Manifiesto HACS-ODLC]], y la razón por la que [[ODLC]] valida contra el objetivo y no contra la implementación ([[Fase 5 - Validation]]).

## Preguntas abiertas

- Leer el hilo completo y el episodio que promociona para citar el argumento, no solo la frase.
- ¿Hay datos públicos (DORA, GitClear, estudios de Copilot) que cuantifiquen el efecto "más código → más mantenimiento"?
