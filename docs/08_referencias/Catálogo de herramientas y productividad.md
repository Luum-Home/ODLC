---
tags: [referencias, herramientas, productividad, infraestructura, agents, workspaces]
status: borrador
created: 2026-06-10
---

# Catálogo de Herramientas y Productividad

El ecosistema de desarrollo guiado por inteligencia artificial cuenta con un conjunto diverso de herramientas, runtimes, espacios de trabajo y plataformas de optimización. Este catálogo recopila y clasifica las soluciones más destacadas para programadores y arquitectos que diseñan sistemas cognitivos humano-agente.

---

## 1. Runtimes de Agente y Arneses Locales (CLI)

Estas herramientas actúan como el entorno de ejecución (núcleo) donde operan los agentes de codificación autónomos, interactuando con el sistema operativo local.

| Herramienta / Enlace | Descripción y Enfoque Técnico | Características Principales |
|---|---|---|
| **[OpenClaw](https://openclaw.ai/)** | Asistente personal autónomo diseñado para ejecutarse localmente/de forma persistente. Es relevante para HACS-ODLC porque formaliza archivos de personalidad y memoria (`SOUL.md`, `USER.md`, `MEMORY.md`) que el agente lee al iniciar. Ojo: tiene más de 500 CVEs en NVD y su marketplace de skills distribuyó malware en 2026. Se estudia, no se instala en la máquina de trabajo. | - Integración con mensajería (Telegram, Discord, Slack).<br>- Soporte de MCP y habilidades modulares.<br>- `SOUL.md` define voz, límites y estilo; `AGENTS.md` define reglas operativas ([docs](https://docs.openclaw.ai/concepts/soul)). Consultado 2026-06-11. |
| **[Pi](https://pi.dev/)** | Arnés de agente minimalista orientado a terminal (CLI) y modular. | - Extensible a través de TypeScript.<br>- Enfoque en bloques de construcción reutilizables.<br>- Configurable en múltiples modos (TUI, RPC). |
| **[OpenCode](https://opencode.ai/)** | Agente de codificación nativo para la terminal con enfoque en privacidad local. | - Interfaz TUI pulida y rápida.<br>- Gestión de sesiones múltiples.<br>- Integración con Language Server Protocol (LSP). |
| **[Agent Zero](https://www.agent-zero.ai/)** | Framework agentic autónomo que corre aislado en Docker. Ojo: no pide aprobación antes de ejecutar comandos y la interfaz web arranca sin contraseña. | - Instalación vía script o Docker (`docker run -p 127.0.0.1:5080:80 agent0ai/agent-zero`: publicar el puerto solo en localhost, porque `-p 80:80` lo abre a toda la red).<br>- Puede mantenerse sandboxed en Docker y conectar el host mediante A0 CLI cuando haga falta acceso local ([docs](https://www.agent-zero.ai/p/docs/installation/)).<br>- Útil para laboratorios de seguridad por su separación explícita entre contenedor y host. Consultado 2026-06-11. |
| **[Hermes Agent](https://hermes-agent.nousresearch.com/docs/)** | Orquestador autónomo de Nous Research diseñado para auto-mejoramiento y memoria persistente. | - Bucle cerrado de aprendizaje: memoria curada por el agente, creación/evolución de skills y recall entre sesiones.<br>- Backends local, Docker, SSH, Daytona, Singularity y Modal.<br>- Soporta automatizaciones programadas y subagentes aislados ([docs](https://hermes-agent.nousresearch.com/docs/)). Consultado 2026-06-11. |

---

## 1.1 Agentes personales de los vendors (siempre encendidos)

La versión SaaS de lo que hace OpenClaw: un agente con computadora propia en la nube, memoria, tareas programadas y mensajería, sin instalar nada. Salieron entre mayo y septiembre de 2026.. Consultado 2026-10-08.

*   **[dots](https://learn.chatgpt.com/docs/dots)** (OpenAI): agente en la nube al que se le habla por ChatGPT, Slack o Teams, con acceso opcional a la computadora local. Pro de US\$100 a 500 por mes, Business Premium y Enterprise. No está para particulares en el EEE, el Reino Unido ni Suiza.
*   **[Grok Bot](https://docs.x.ai/grok-bot/overview.md)** (xAI): varios bots con nombre y rol sobre una computadora en la nube de Cursor, manejados por app, Slack o @bot en X. Incluido en los planes pagos de Cursor y en SuperGrok. Todos los bots de un usuario comparten computadora y credenciales: separarlos no aísla nada.
*   **[Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)** con **Dispatch** (Anthropic): es el equivalente de Claude, no hay un producto aparte. Tareas programadas, ejecución en la nube en Pro y Max, y Dispatch para pedirle tareas desde el celular (beta cerrada). Todos los planes pagos.
*   **[Claude Tag](https://www.anthropic.com/news/introducing-claude-tag)** (Anthropic): compañero de equipo en Slack con memoria por canal. Solo Team y Enterprise.
*   **[Gemini Spark](https://support.google.com/gemini/answer/17094507)** (Google): agente personal con agendas, skills y MCP. Google AI Ultra fuera del EEE, el Reino Unido, Suiza y Nigeria. En Pro, solo EE.UU. y en inglés.
*   **[Meta Muse](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)** (Meta): agente en una VM propia, con un segundo agente que aprueba lo que sale a internet. Se le habla por su app o por WhatsApp. Solo EE.UU.
*   Manus (por Telegram) y Perplexity Personal Computer (sobre una Mac mini propia) son de la misma categoría, pero solo los encontramos en prensa, sin fuente oficial consultable.

---

## 2. Orquestadores y Espacios de Trabajo Colaborativos

Plataformas para gestionar múltiples agentes, coordinar flujos de trabajo paralelos y proporcionar interfaces de control de proyectos para humanos y equipos de IA.

*   **[Superconductor](https://www.superconductor.com/)**: Un espacio de trabajo colaborativo para orquestar y ejecutar múltiples agentes de desarrollo (como Claude Code) en paralelo sobre tickets de software. Permite a los humanos revisar los cambios de forma visual y móvil.
*   **[Paperclip](https://github.com/paperclipai/paperclip)**: Plataforma de control y alineación organizativa para "compañías formadas por agentes de IA". Proporciona herramientas de gestión de presupuestos, asignación de tareas, organigramas y monitoreo de objetivos estratégicos.
*   **[Odysseus](https://github.com/odysseus-dev/odysseus)** (licencia AGPL-3.0; repo movido desde `pewdiepie-archdaemon/odysseus`, verificado 2026-10-07): Workspace de IA autohospedado que se define como una experiencia tipo ChatGPT/Claude ejecutada con hardware y datos propios, local-first y privacy-first. Útil para conversar en el curso sobre límites de herramientas SaaS y soberanía de datos; tratarlo como proyecto emergente/joven, no como estándar empresarial maduro. Consultado 2026-06-11.

---

## 3. Infraestructura, APIs y Optimización de Modelos

Servicios y tecnologías de backend que facilitan el acceso, ruteo y entrenamiento optimizado de modelos de lenguaje grandes.

*   **[OpenRouter](https://openrouter.ai/)**: Un gateway y enrutador unificado de APIs que permite acceder a cientos de modelos de LLM (tanto propietarios como de código abierto) con optimización de costos y balances automáticos.
*   **[Hugging Face](https://huggingface.co/)**: El hub de colaboración más grande del mundo para compartir y descubrir modelos de machine learning, conjuntos de datos (datasets) y aplicaciones interactivas (Spaces).
*   **[Unsloth](https://unsloth.ai/)**: Un framework de optimización de código abierto que acelera el ajuste fino (fine-tuning) de LLMs locales (como Llama 3 o Mistral). El README del proveedor declara entrenamiento "2× faster with 70% less VRAM" (cifra del proveedor, [unslothai/unsloth](https://github.com/unslothai/unsloth) consultado 2026-10-07), sin baseline público ni mediciones independientes.

---

## 4. Servicios de Productividad y Metodologías para Agentes

Servicios de revisión automática y extensiones de diseño de comportamiento que aseguran la calidad y disciplina en el código producido por IAs.

*   **[CodeRabbit](https://www.coderabbit.ai/)**: Plataforma SaaS que automatiza las revisiones de código y proporciona feedback contextual directamente en las Pull Requests de repositorios de Git.
*   **[OpenHuman](https://tinyhumans.ai/openhuman)** (Código en **[tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman)**): Proyecto de TinyHumans orientado a crear un asistente personal superinteligente. Destaca por proveer una interfaz visual intuitiva y un motor de memoria subconsciente a largo plazo que persiste entre sesiones cotidianas.
*   **[Superpowers](https://github.com/obra/superpowers)**: Un plugin de habilidades diseñado específicamente para Claude Code. Obliga al agente a seguir metodologías de ingeniería estrictas (como TDD, YAGNI, DRY) redactando y evaluando su trabajo a través de directrices `SKILL.md`.

---

## 5. Plataformas No-Code para Agentes y Automatización LLM

Constructores visuales de flujos y agentes orientados a perfiles técnicos sin experiencia en programación. Permiten conectar LLMs, herramientas, bases de conocimiento y APIs sin escribir código.

*   **[n8n](https://n8n.io/)**: Orquestador de automatizaciones open-source con interfaz visual de nodos. Soporta cientos de servicios, ejecución self-hosted y nodos de IA nativos. Consultado 2026-06-11.
*   **[Make](https://www.make.com/)**: Plataforma visual de automatización (antes Integromat) con escenarios multistep, mapeo de datos y más de 1.000 conectores listos. Consultado 2026-06-11.
*   **[Zapier](https://zapier.com/)**: Automatización sin código entre apps populares; énfasis en simplicidad y velocidad de despliegue para flujos de dos pasos. Consultado 2026-06-11.
*   **[Lindy](https://www.lindy.ai/)**: Agentes de IA no-code con tareas programadas, integraciones, memoria de largo plazo y capacidad de delegar subtareas. Consultado 2026-06-11.
*   **[Botpress](https://botpress.com/)**: Plataforma visual para construir y desplegar chatbots y agentes conversacionales sobre LLMs, con flujos de diálogo y canales integrados. Consultado 2026-06-11.
*   **[Langflow](https://www.langflow.org/)**: Interfaz visual de flujos sobre LangChain; permite conectar componentes LLM, RAG, herramientas y memoria sin programar. Open-source y desplegable en local o cloud. Consultado 2026-06-11.
*   **[Flowise](https://flowiseai.com/)**: Constructor visual de flujos LLM open-source orientado a RAG, agentes y chatbots. Desplegable en local (Node.js) o en servicios cloud; API integrada. Consultado 2026-06-11.
*   **[Dify](https://dify.ai/)**: Plataforma de desarrollo de aplicaciones LLM con editor visual de flujos, RAG integrado, gestión de prompts, variables de entorno y observabilidad incorporada. Open-source con opción cloud. Consultado 2026-06-11.

---

## 6. Directrices de Selección

> [!TIP]
> **¿Cómo elegir el entorno de ejecución de tu agente?**
> 1.  Si buscás **ejecución local controlada**: **Agent Zero** (Docker + puente host opcional) u **OpenCode**. Agent Zero sirve como objeto de práctica dentro de una VM descartable, no como laboratorio seguro de por sí: configurá contraseña y no montes el home ni el socket de Docker.
> 2.  Si el objetivo es enseñar **memoria/persona persistente y archivos de comportamiento**: usá **OpenClaw** como caso de estudio (`AGENTS.md`, `SOUL.md`, `USER.md`, `MEMORY.md`), leyendo su documentación y no instalándolo en la máquina de trabajo: tiene más de 500 CVEs y su marketplace de skills distribuyó malware en 2026.
> 3.  Si querés mostrar **aprendizaje continuo y skills auto-evolutivas**: incorpora **Hermes Agent**, cuidando que el auto-mejoramiento tenga revisión humana antes de promover skills.
> 4.  Si querés discutir **soberanía de datos y workspace local tipo ChatGPT/Claude**: menciona **Odysseus**, con la advertencia de madurez temprana.
> 5.  Si tienes un **equipo de desarrollo humano-agente trabajando sobre Jira/GitHub**: integra **Superconductor** para revisión multiplayer paralela.
> 6.  Si querés mostrar **un agente siempre encendido sin autohospedar nada**: usá **Claude Cowork** (tareas programadas, Dispatch), que es el único al alcance de un plan individual barato. **dots**, **Grok Bot**, **Gemini Spark** y **Meta Muse** se muestran desde la cuenta del instructor: piden planes de US\$100 o más, o no están disponibles en todas las regiones.

> [!warning] Nota docente — curso aplicado vs. arneses avanzados
> Para perfiles no programadores, estas herramientas no reemplazan la ruta principal del curso (ChatGPT/Claude + no-code + MCP). Sirven como bloque de discusión para explicar las limitaciones actuales de los SaaS: permisos por plan, datos fuera del workspace, falta de memoria gobernada y necesidad de sandbox/HITL. Si se incluyen en vivo, hacerlo como demo controlada o lectura comparativa, no como requisito del curso.
