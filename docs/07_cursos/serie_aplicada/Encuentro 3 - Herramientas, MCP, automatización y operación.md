---
tags: [cursos, educacion, capacitacion, seguridad, agentes, no-code, serie-aplicada]
status: borrador
created: 2026-06-11
autor: Damián, OliveX Security
fuente: "[[Draft Damián - Agentes de IA aplicados al trabajo técnico]]"
---

# Encuentro 3 — Herramientas, MCP, automatización y operación

**Serie aplicada · OliveX Security** | Encuentro 3 de 4 · 2 horas

← [[Encuentro 2 - Prompting seguro y agentes con conocimiento propio|Encuentro anterior]] · [[Curso - Agentes de IA aplicados al trabajo técnico|Índice del curso]]

---

## Objetivo

Permitir que los agentes ejecuten acciones sobre sistemas reales y dejarlos listos para operar.

---

## Contenidos

- Introducción a MCP (Model Context Protocol): arquitectura y casos de uso. Ver también [[Módulo 4 - Ciberseguridad aplicada]] para los aspectos de seguridad en servidores MCP.
- Herramientas no-code base para automatización y construcción de flujos de agentes:
  - **[n8n](https://n8n.io/)** — orquestador de automatizaciones open-source con nodos visuales para APIs, bases de datos y servicios.
  - **[Make](https://www.make.com/)** — plataforma visual de automatización (antes Integromat) con cientos de conectores listos.
  - **[Zapier](https://zapier.com/)** — automatización sin código entre apps populares; enfocado en simplicidad y velocidad de despliegue.
  - **[Lindy](https://www.lindy.ai/)** — agentes de IA no-code con tareas programadas, integraciones y memoria de largo plazo.
  - **[Botpress](https://botpress.com/)** — plataforma visual para construir y desplegar chatbots y agentes conversacionales con LLMs.
- Ecosistema avanzado opcional para proyectos que requieran mayor control técnico, ejecución local o composición de flujos LLM:
  - **Hermes Agent**, **Odysseus**, **OpenClaw** y **Agent Zero** como referencias de arneses, runtimes locales o agentes autónomos. Se discuten, no se instalan en la máquina de trabajo: los cuatro tuvieron fallas de ejecución remota reportadas en 2026. Riesgos y advertencias en [[Agentes abiertos y planes SaaS - Verificación]].
  - **[Langflow](https://www.langflow.org/)** — interfaz visual de flujos sobre LangChain; permite conectar componentes LLM, RAG, herramientas y memoria sin programar.
  - **[Flowise](https://flowiseai.com/)** — constructor visual de flujos LLM open-source; orientado a RAG, agentes y chatbots desplegables en local o cloud.
  - **[Dify](https://dify.ai/)** — plataforma de desarrollo de aplicaciones LLM con editor visual, RAG integrado, gestión de prompts y observabilidad.
- Introducción a Claude Code y Codex para tareas de sistemas. Para hacerlo accesible a perfiles no programadores, el material de apoyo debe usar guías visuales, capturas de pantalla y recorridos paso a paso que desmitifiquen la terminal como entorno de trabajo.
- Integración con APIs y herramientas corporativas.
- Operación: [[Glosario y taxonomía|human-in-the-loop (HITL)]], observabilidad, costos y consumo de tokens, versionado.
- Observabilidad operativa: monitoreo de logs, seguimiento de ejecución, control preventivo de costos por consumo de tokens y revisión periódica de errores.

---

## Taller

- Conexión de un agente a un sistema externo y construcción de un flujo automatizado.
- Dejar el agente monitoreado, acotado y versionado.

---

> **Cómo hacerlo seguro:** aplicar [[Módulo 4 - Ciberseguridad aplicada|mínimo privilegio]] en los conectores, allowlist de herramientas y dominios, aprobación humana para acciones irreversibles y verificación del origen de los servidores MCP. Ningún agente con autoaprobación ciega; límites operativos y de costo como control.

---

## Entregables

- Agente conectado a herramientas reales, monitoreado y documentado.

---

Encuentro anterior: [[Encuentro 2 - Prompting seguro y agentes con conocimiento propio]]
Siguiente encuentro: [[Encuentro 4 - Seguridad, evaluación y laboratorio integrador]]
← [[Curso - Agentes de IA aplicados al trabajo técnico|Índice del curso]]
