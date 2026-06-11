---
tags: [cursos, educacion, capacitacion, seguridad, agentes, no-code]
status: borrador
created: 2026-06-11
autor: Damián, OliveX Security
fuente: "[[Draft Damián - Agentes de IA aplicados al trabajo técnico]]"
recibido: 2026-06-11
---

# Agentes de IA aplicados al trabajo técnico

Capacitación práctica para equipos de infraestructura, operaciones, soporte, seguridad, QA y datos.

**OliveX Security** | 8 horas (4 encuentros de 2 horas)

---

> [!note] Serie aplicada — complemento de la serie técnica
> Este curso es la **serie aplicada**: está orientada a perfiles técnicos sin experiencia en programación que trabajan con herramientas comerciales y plataformas no-code (ChatGPT, Claude, n8n, Make, Zapier, etc.).
>
> Es complementaria de la serie técnica [[Cursos HACS-ODLC]], que cubre la construcción del sistema: ingeniería de arneses, gobernanza de agentes, ciberseguridad desde código, etc.
>
> **Serie técnica** = construir el sistema. **Serie aplicada** = operar agentes con herramientas comerciales, sin programar.

---

## Resumen ejecutivo

La inteligencia artificial ya no se limita a responder preguntas. Los nuevos agentes son capaces de consultar documentación, ejecutar acciones sobre herramientas corporativas, automatizar procesos y asistir en tareas técnicas complejas.

La adopción efectiva, sin embargo, requiere más que acceso a un modelo. Los equipos necesitan aprender a diseñar agentes confiables, conectarlos a sistemas reales y, sobre todo, operarlos de forma segura.

Este curso está diseñado para que profesionales técnicos sin experiencia en programación puedan crear, evaluar y desplegar agentes útiles para su trabajo diario, aplicando criterios de seguridad en cada paso. Al finalizar, cada participante habrá construido agentes propios sobre casos reales de su organización y contará con una metodología para seguir desarrollándose de forma segura dentro de su equipo.

---

## Información general

| | |
|---|---|
| **Duración** | 8 horas (4 encuentros de 2 horas) |
| **Modalidad** | Remoto |

**Dirigido a:**
- Infraestructura
- Operaciones
- Soporte técnico
- Seguridad informática
- QA
- Datos
- Líderes técnicos

**Requisitos:**
- Cuentas de pago de ChatGPT y/o Claude (los planes gratuitos limitan GPTs, Projects y conectores).
- Acceso a documentación no sensible para las prácticas.
- Para el encuentro de herramientas: una herramienta o API de prueba del equipo y una cuenta en una plataforma no-code.
- Para el laboratorio de seguridad: un conjunto de datos de prueba en un entorno aislado.

> [!warning] Trazabilidad
> Las capacidades disponibles por plan cambian con frecuencia. Estado verificado contra fuentes oficiales al 2026-06-11:
> - **ChatGPT — GPTs personalizados**: usar GPTs está disponible para usuarios autenticados, pero **crear o editar GPTs requiere suscripción paga** y puede depender de permisos de workspace ([OpenAI Help: GPTs in ChatGPT](https://help.openai.com/en/articles/8554407-gpts-in-chatgpt)). Para este curso, una cuenta Free sirve para consumir GPTs compartidos, no para construirlos.
> - **ChatGPT — Workspace Agents**: no son lo mismo que los GPTs individuales. OpenAI los presenta como agentes Codex-powered para workflows de equipo, con permisos, memoria, herramientas y ejecución en la nube; al 2026-06-11 están en research preview para **Business, Enterprise, Edu y Teachers** ([OpenAI: Introducing workspace agents in ChatGPT](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)). No asumir disponibilidad en planes individuales Plus/Pro/Go.
> - **Claude — Cowork**: la documentación de soporte indica disponibilidad en planes pagos **Pro, Max, Team y Enterprise** para Claude Desktop en macOS/Windows ([Claude Help: Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)). La observación original de que podría requerir solo Business/Team quedó desactualizada frente a esta fuente.
> - **Claude — Agent SDK**: a partir del 2026-06-15, Pro, Max, Team y Enterprise pueden reclamar crédito mensual separado para Agent SDK y `claude -p`; ese crédito no aplica a Cowork ni a Claude Code interactivo ([Claude Help: Agent SDK with your plan](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)).
> - **Claude — subagentes**: la construcción de subagentes formales en Claude Code usa definiciones en `.claude/agents/` o `~/.claude/agents/`, con system prompt, herramientas y permisos propios ([Claude Code Docs: subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)). No confundir esto con Cowork.
> - **Carpeta `.agent/` con `INSTRUCTIONS.md`, `SOUL.md`, `VOICE.md`, `MEMORY.md`**: no es una capacidad oficial de Cowork. En este vault se trata como patrón HACS-ODLC vendor-neutral de redirección cognitiva; el origen verificable más cercano para `SOUL.md`/`MEMORY.md` está en OpenClaw, que carga `SOUL.md`, `USER.md` y memoria al iniciar ([OpenClaw: SOUL.md](https://docs.openclaw.ai/concepts/soul), [OpenClaw: default AGENTS.md](https://docs.openclaw.ai/reference/AGENTS.default)).
>
> No asumir que una cuenta de pago individual garantiza acceso a todas las funcionalidades de construcción de agentes en ambas plataformas; re-verificar antes de cada dictado.

---

## Objetivos de aprendizaje

Al finalizar el curso, los participantes podrán:

- Comprender cómo funcionan los modelos de IA modernos y cuáles son sus limitaciones.
- Diseñar prompts robustos y reutilizables.
- Crear agentes con conocimiento propio usando documentación corporativa.
- Automatizar tareas operativas mediante herramientas no-code.
- Conectar agentes con sistemas y servicios externos.
- Evaluar calidad, costos y riesgos asociados.
- Aplicar controles de seguridad específicos para agentes de IA en cada etapa.
- Construir agentes seguros y listos para uso interno.

---

## Metodología

El curso combina **30% de conceptos y fundamentos** con **70% de práctica aplicada**. Cada encuentro dura 2 horas, con aproximadamente 30 minutos de concepto y 90 minutos de taller. El cuarto encuentro funciona como jornada de práctica integradora.

**Método de trabajo:** Construir → Probar → Asegurar → Mejorar

La seguridad no se concentra en una sola clase: aparece como un cierre concreto en cada encuentro. Después de construir algo, se aplica el control de seguridad que corresponde a esa etapa. Los participantes trabajan sobre tareas reales de su entorno mientras construyen un agente que evoluciona durante toda la capacitación, y cada clase concluye con un entregable que pasa a formar parte del proyecto final.

---

## Programa

| Encuentro | Tema | Descripción |
|-----------|------|-------------|
| [[Encuentro 1 - Fundamentos y primer agente\|Encuentro 1]] | Fundamentos y primer agente | Cómo funcionan los modelos actuales; chatbot vs. asistente vs. agente; primer asistente sobre documentación real. |
| [[Encuentro 2 - Prompting seguro y agentes con conocimiento propio\|Encuentro 2]] | Prompting seguro y agentes con conocimiento propio | Anatomía del prompt robusto; técnicas avanzadas; GPTs/Claude Projects; memoria de trabajo vs. base de conocimiento; RAG y conocimiento corporativo. |
| [[Encuentro 3 - Herramientas, MCP, automatización y operación\|Encuentro 3]] | Herramientas, MCP, automatización y operación | MCP; plataformas no-code base (n8n, Make, Zapier, Lindy, Botpress); ecosistema avanzado opcional; integración con APIs; operación segura. |
| [[Encuentro 4 - Seguridad, evaluación y laboratorio integrador\|Encuentro 4]] | Seguridad, evaluación y laboratorio integrador | Modelo de amenazas de agentes; prompt injection, tool poisoning y más; checklist de seguridad; laboratorio integrador y proyecto final. |

---

## Proyecto final

Durante toda la capacitación los participantes construyen un agente propio basado en una necesidad real de su área. El proyecto integra conocimiento corporativo, automatización, herramientas externas, controles de seguridad y documentación operativa. Al finalizar el curso, cada participante cuenta con una solución funcional y segura, lista para evolucionar dentro de su equipo.

---

## Entregables

### Para cada participante

- Agente funcional.
- Biblioteca de prompts reutilizables.
- Flujo automatizado.
- Documentación técnica.
- Checklist de seguridad.

### Para la organización

- Catálogo inicial de agentes.
- Guía de adopción de IA.
- Mapa de herramientas recomendadas.
- Guía de seguridad para agentes.
- Backlog de automatizaciones identificadas.

---

## Beneficios para la organización

- Reducción de tareas repetitivas.
- Mayor velocidad de acceso al conocimiento interno.
- Mejor aprovechamiento de las herramientas de IA existentes.
- Incorporación de criterios de seguridad desde el diseño.
- Creación de capacidades internas sostenibles.
- Primeros casos de uso implementados durante la capacitación.

La propuesta está orientada a generar resultados tangibles desde la primera semana y a dejar capacidades instaladas dentro de los equipos, más allá del uso puntual de una herramienta específica.

---

## Anexo: panorama del ecosistema de agentes

Material de referencia para profundizar fuera del curso:

1. **Runtimes y arneses locales**: ejecución local, control, sandbox y memoria persistente.
2. **Orquestadores colaborativos**: coordinación de múltiples agentes y revisión humana.
3. **Infraestructura y APIs**: gateways de modelos, optimización de costos y fine-tuning.
4. **Productividad y calidad**: revisión asistida, skills, checklists y estándares operativos.

Ver: [[Catálogo de herramientas y productividad]].

---

Relacionado: [[Cursos HACS-ODLC]] · [[Draft Damián - Agentes de IA aplicados al trabajo técnico]] · [[Módulo 4 - Ciberseguridad aplicada]] · [[Glosario y taxonomía]]
