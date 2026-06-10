---
tags: [problema, contexto]
status: borrador
created: 2026-06-10
---

# AI SDLC

**AI SDLC** = AI Software Development Lifecycle: el ciclo de vida de desarrollo de software potenciado por IA. No es una metodología formal única, sino una evolución del SDLC tradicional donde la IA participa en prácticamente todas las etapas.

## SDLC tradicional

Requerimientos → Diseño → Desarrollo → Testing → Deploy → Operación y mantenimiento.

## Cómo participa la IA en cada fase

| Fase | Cómo ayuda la IA |
|---|---|
| Requerimientos | Genera historias de usuario, documentación y casos de uso |
| Diseño | Propone arquitecturas, diagramas, ADRs y modelos de datos |
| Desarrollo | Genera código, refactors, tests y documentación |
| Testing | Crea casos de prueba, fuzzing y análisis de cobertura |
| Security | Detecta vulnerabilidades y propone fixes |
| Deploy | Genera pipelines CI/CD e infraestructura |
| Operación | Analiza logs, métricas e incidentes |
| Mantenimiento | Refactoriza y migra código automáticamente |

Herramientas representativas: Cursor, GitHub Copilot, OpenAI Codex, Claude Code, CodeRabbit, Snyk.

## AI-Native SDLC: el paso siguiente

Las empresas más avanzadas ya no hablan de "AI Coding" sino de **AI-Native SDLC**:

```
Idea
 ↓ PRD generado por IA
 ↓ Arquitectura propuesta por IA
 ↓ Código generado por IA
 ↓ Tests generados por IA
 ↓ Security review automático
 ↓ Code review automático
 ↓ Deploy automático
 ↓ Observabilidad y remediación automática
```

Y la visión más avanzada es **multi-agente**: Product Manager Agent → Architect Agent → Developer Agent → Tester Agent → Security Agent → DevOps Agent, todos coordinados sobre un mismo repositorio y compartiendo contexto. Conceptos asociados: AI Engineering, Agentic SDLC, AI-Native Development, Autonomous Software Engineering, Multi-Agent Software Development. AWS, Microsoft, Google Cloud y GitHub empujan fuerte esta idea.

## Por qué esto no alcanza (y de ahí nace este vault)

AI SDLC acelera *fases* de un ciclo diseñado para humanos. Pero los cuellos de botella reales ya no están en las fases: están en el contexto, la decisión y la validación → [[Nuevos cuellos de botella]]. Generar más código no hace al equipo más rápido → [[Más código no es más velocidad]]. La respuesta no es una herramienta más, sino otro modelo organizacional → [[HACS]] y otra metodología → [[ODLC]].
