---
tags: [referencias, agentes, seguridad, openclaw, agent-zero, hermes, odysseus, dots, grok-bot, planes]
status: borrador
created: 2026-10-07
consultado: 2026-10-07
---

# Agentes abiertos y planes SaaS: verificación

Qué puede construir hoy un alumno con cada plan de ChatGPT, Claude y Gemini, qué riesgos tienen los cuatro agentes abiertos que el curso menciona como alternativa (OpenClaw, Agent Zero, Hermes Agent y Odysseus) y qué ofrecen los vendors en la misma categoría (dots, Grok Bot, Cowork, Muse). Sirve de respaldo para el callout de requisitos de [[Curso - Agentes de IA aplicados al trabajo técnico]] y para el ecosistema avanzado de [[Encuentro 3 - Herramientas, MCP, automatización y operación]].

> [!warning] Esto vence rápido
> Todo lo de esta nota se consultó el 2026-10-07. Entre junio y octubre cambiaron tres de las cinco afirmaciones sobre planes que tenía el curso. Antes de cada dictado corré:
> ```bash
> scripts/verificar_fuentes_agentes.sh
> ```
> Baja cada fuente y busca la frase que respalda cada dato. Sale con 0 si todo sigue igual, 1 si alguna frase desapareció (la nota puede estar vencida) y 2 si no pudo bajar alguna página. Las páginas de help.openai.com y el blog de Microsoft dan 403 a curl. El script las lista al final para mirarlas a mano.

---

## 1. Qué puede construir el alumno, por plan

| Plataforma | Plan individual pago | Plan de organización |
|---|---|---|
| **ChatGPT** | Plus y Pro **ya no pueden crear GPTs nuevos**. Los existentes se usan y se editan hasta que se retiren, el 2026-12-11. Pueden crear skills y plugins propios (sin compartirlos con un equipo). No tienen Workspace Agents. | Business, Enterprise y Edu: Workspace Agents, cobrados por tokens desde el 2026-07-06. En Enterprise vienen apagados y los habilita el admin. Plugins compartibles en el workspace. |
| **Claude** | Pro: Cowork, skills y plugins propios (sin compartir), subagentes en Claude Code. El Agent SDK y `claude -p` consumen los límites del plan. Pro **no** recibe créditos de API. | Max y Team reciben créditos de API mensuales desde el 2026-10-07. Team además comparte plugins entre colegas. Enterprise no recibe créditos. |
| **Gemini** | Gemini Spark como agente personal: en Ultra, en todos los países salvo el Espacio Económico Europeo, el Reino Unido, Suiza y Nigeria. En Pro, por ahora solo en EE.UU. y en inglés. Los Gems se reemplazan por skills en cuentas personales desde noviembre de 2026. | Gemini Enterprise (Business, Standard, Plus): agentes no-code con Workflow Builder, en preview. Workspace Studio para flujos. Los Gems siguen en cuentas de trabajo hasta 2027. |

**Fuentes y frases que las respaldan:**
- GPTs: [help.openai.com 8554407](https://help.openai.com/en/articles/8554407-gpts-in-chatgpt) dice *"New GPT creation and publishing are not available on personal ChatGPT accounts"*. El retiro del 2026-12-11 está en [help.openai.com 20001519](https://help.openai.com/en/articles/20001519). La migración oficial lleva los GPTs a **plugins**, no a Workspace Agents ([learn.chatgpt.com](https://learn.chatgpt.com/docs/migrate-custom-gpts)). Ojo: learn.chatgpt.com habla del retiro en Enterprise y help.openai.com dice que afecta a todos los planes. Se toma la segunda, que es la más restrictiva.
- Workspace Agents por tokens: nota del 2026-07-06 en [ChatGPT Business, release notes](https://help.openai.com/en/articles/11391654-chatgpt-business-release-notes).
- Agent Builder (platform.openai.com) **cierra el 2026-11-30** ([developers.openai.com](https://developers.openai.com/api/docs/guides/agent-builder)). No usarlo en el curso.
- Cowork en planes pagos: [support.claude.com 13345190](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork).
- Créditos de API solo para Max y Team: [support.claude.com 17154008](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans) (*"Free, Pro, and Enterprise plans aren't eligible"*). Cubren el uso con API key de una organización de Console vinculada. Con el login de la suscripción, el SDK sigue consumiendo los límites del plan ([15036540](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)).
- Plugins y skills en Claude: [13837440](https://support.claude.com/en/articles/13837440), [12512180](https://support.claude.com/en/articles/12512180). Subagentes: [code.claude.com](https://code.claude.com/docs/en/sub-agents).
- Gems y skills: [support.google.com 15146780](https://support.google.com/gemini/answer/15146780). Spark: [17094507](https://support.google.com/gemini/answer/17094507). Gemini Enterprise: [ediciones](https://docs.cloud.google.com/gemini/enterprise/docs/editions).

**Para el requisito del curso:** con ChatGPT Plus ya no alcanza para el taller de "crear un GPT". La alternativa en plan individual son skills o plugins (ChatGPT, Claude) o un Project de Claude con instrucciones propias. Si el taller tiene que mostrar agentes compartidos por un equipo, hace falta un workspace Business o Team.

---

## 2. Los cuatro agentes abiertos

Ninguno de los cuatro es para que un perfil que no programa lo instale en la máquina de trabajo. Se usan para discutir los límites de los SaaS (permisos por plan, datos afuera, memoria sin gobierno) y, si hay práctica, la arma el instructor en una VM descartable.

### OpenClaw

Licencia MIT, gobernado por la OpenClaw Foundation ([LICENSE](https://raw.githubusercontent.com/openclaw/openclaw/main/LICENSE)). Para el curso interesa su diseño de persona y memoria en archivos (`SOUL.md`, `USER.md`, `MEMORY.md`, `AGENTS.md`), que es de donde sale el patrón de carpeta `.agent/` del vault.

Riesgos verificados:
- **575 CVEs en NVD** al 2026-10-07 (búsqueda por CPE `cpe:2.3:a:openclaw:openclaw`, la cuenta la hace el script). En junio se citaba "138+". Desde junio se publicaron más de 200.
- CVE-2026-25253: ejecución remota con un clic, robando el token del gateway por un parámetro de la URL. Parcheado en 2026.1.29.
- CVE-2026-22172 y CVE-2026-32922: bypass de autorización y escalada de privilegios. VulnCheck les dio 9.9 en CVSS 3.1 (9.4 en CVSS 4.0). NVD no les puso puntaje propio.
- Campaña ClawHavoc (febrero de 2026): Koi Security encontró 341 skills maliciosas en ClawHub, 335 de ellas instalaban el infostealer AMOS ([The Hacker News](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html)). El post original de Koi ya no está: redirige a Palo Alto Networks, que compró la empresa.
- SecurityScorecard contó 40.214 instancias expuestas en febrero, con autenticación débil o inexistente ([informe](https://securityscorecard.com/blog/beyond-the-hype-moltbots-real-risk-is-exposed-infrastructure-not-ai-superintelligence/)). Hoy el host escucha en loopback por defecto, pero **la imagen de contenedor sigue publicando el puerto** ([docs](https://docs.openclaw.ai/gateway/security)).
- Las credenciales se guardan en texto plano por defecto y el propio agente las puede leer. Hay SecretRefs, pero son opcionales ([docs](https://docs.openclaw.ai/gateway/secrets)).
- Microsoft publicó una guía que dice que no corresponde correrlo en una estación de trabajo estándar ([blog, 2026-02-19](https://www.microsoft.com/en-us/security/blog/2026/02/19/running-openclaw-safely-identity-isolation-runtime-risk/), da 403 a curl).

> [!danger] Advertencia para el curso
> Lo usamos para estudiar cómo organiza la persona y la memoria, no para instalarlo en la máquina de trabajo. Tiene más de 500 CVEs publicadas y su marketplace de skills distribuyó malware en 2026. Si lo querés probar: VM descartable, sin credenciales reales y sin exponer el gateway a la red.

### Agent Zero

Licencia MIT, de Agent Zero s.r.o. ([LICENSE](https://raw.githubusercontent.com/agent0ai/agent-zero/main/LICENSE)). Corre en Docker, con navegador, escritorio Linux y ejecución de código. Última versión revisada: v2.13 (2026-09-23).

Lo que el vault decía y no se sostiene: que "privilegia control humano".
- No pide aprobación antes de ejecutar código o comandos. El README le aconseja al usuario revisar las acciones sensibles, pero es un consejo, no un control.
- La interfaz web arranca sin contraseña.
- El `docker run -p 80:80` que citaba el Catálogo publica el puerto en todas las interfaces de red.
- El plugin `_orchestrator` lanza sub-agentes con los permisos salteados (`bypassPermissions`, `always_approve`).

CVEs: CVE-2026-30624 (ejecución remota por la configuración de servidores MCP, 8.6), CVE-2026-4307 y CVE-2026-4308 (path traversal y SSRF, parcheadas en [v1.9](https://github.com/agent0ai/agent-zero/releases/tag/v1.9)), y CVE-2026-51852/51853 (traversal en el explorador de archivos, versiones 1.7 a 1.10, publicadas el 2026-09-30).

> [!danger] Advertencia para el curso
> Corre aislado en Docker, pero no pide aprobación antes de ejecutar y la interfaz arranca sin contraseña. Antes de usarlo: configurá usuario y contraseña, publicá el puerto solo en localhost (`-p 127.0.0.1:5080:80`), no montes tu home ni el socket de Docker (montarlo [equivale a darle root al host](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)) y usá la última versión.

### Hermes Agent (Nous Research)

Licencia MIT ([LICENSE](https://raw.githubusercontent.com/NousResearch/hermes-agent/main/LICENSE)). Sigue antes de la 1.0 (v0.21.5, 2026-09-24) y saca versión casi todas las semanas. Crea y mejora sus propias skills solo. Tiene instalador de un comando y app de escritorio.

Lo que el vault tenía que corregir:
- No aprueba cada comando. Solo intercepta los que coinciden con patrones peligrosos, y por defecto (modo `smart`) un LLM auxiliar decide cuáles aprobar ([docs de seguridad](https://hermes-agent.nousresearch.com/docs/user-guide/security)). Con `/yolo` se apaga todo.
- El escaneo de prompt injection mira solo los archivos de contexto (`AGENTS.md`, `SOUL.md`), no lo que lee de la web o del mail.
- CVE-2026-71963 (septiembre de 2026): ejecución remota al abrir un repo malicioso, versiones 0.18.2 a 0.21.0 ([CVE.org](https://cveawg.mitre.org/api/cve/CVE-2026-71963)). En agosto hubo otras dos, por la cadena de suministro del catálogo MCP y por sobreescritura de credenciales.

> [!warning] Advertencia para el curso
> Sirve para una demo guiada por el instructor. Si hay práctica: VM descartable, `approvals.mode: manual`, nada de claves reales y anotar la versión probada.

### Odysseus

Workspace de IA autohospedado que lanzó PewDiePie el 2026-05-31. El repo hoy está en `odysseus-dev/odysseus` (la URL vieja `pewdiepie-archdaemon/odysseus` redirige). La licencia pasó de MIT a **AGPL-3.0-or-later** el 2026-06-09 ([LICENSE](https://raw.githubusercontent.com/odysseus-dev/odysseus/main/LICENSE)), y eso pesa para cualquier uso empresarial que lo modifique.

- Sin releases ni tags: los parches de seguridad van a la rama principal y no se versionan ([SECURITY.md](https://raw.githubusercontent.com/odysseus-dev/odysseus/main/SECURITY.md)). No se puede fijar una versión.
- El agente tiene shell, Python, archivos, mail y MCP. Su política de seguridad pide tratarlo como una consola de administración.
- El primer día se reportó una ejecución remota de un clic (issue #350), cerrada sin CVE ni advisory. El repo no publica advisories.
- Corrección sobre la investigación de junio: no es single-user (tiene cuentas, admin y permisos por usuario) ni lo mantiene una sola persona. Entre septiembre y octubre, PewDiePie hizo menos de la mitad de los commits.

> [!warning] Advertencia para el curso
> Se usa para discutir soberanía de datos y qué cambia la licencia AGPL, no para instalar. Sin releases, no hay forma de saber qué parches tiene una instalación.

---

## 3. Los agentes personales de los vendors

Entre agosto y septiembre de 2026 los vendors grandes sacaron su propia versión de lo que hace OpenClaw: un agente siempre encendido, con computadora propia en la nube, memoria, tareas programadas y mensajería. Ya no hace falta autohospedar nada para mostrarlo en clase, pero ninguno entra en un plan individual barato.

| Producto | Qué es | Planes | Ojo |
|---|---|---|---|
| **[dots](https://learn.chatgpt.com/docs/dots)** (OpenAI, fines de septiembre de 2026) | Agente siempre encendido con computadora y navegador en la nube. Se le habla por ChatGPT, Slack o Teams (Teams en alpha). Puede usar la computadora local y los plugins de ChatGPT. | Pro 100, 200 y 500 (US\$100 a 500 por mes), Business Premium y Enterprise. En Enterprise viene apagado. | No está para particulares en el EEE, el Reino Unido ni Suiza. Los controles de modelo de Enterprise no aplican a dots. Desconectar una app no borra lo que ya guardó en memoria. |
| **[Grok Bot](https://docs.x.ai/grok-bot/overview.md)** (xAI, beta desde agosto de 2026) | Varios "Bots" con nombre y rol que trabajan en una computadora en la nube, con rutinas y skills. Se manejan por app propia, por Slack o mencionando @bot en X. Corre sobre la infraestructura de Cursor. | Todos los planes individuales pagos de Cursor (desde US\$20), Cursor Teams, o vinculando SuperGrok (no Lite) o X Premium+. | Todos los Bots de un usuario comparten la misma computadora y las mismas credenciales: separarlos no aísla nada. Corre solo en EE.UU. Los logs de auditoría son solo de Enterprise. |
| **[Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)** con Dispatch (Anthropic) | No hay un producto aparte: el equivalente es Cowork, que tiene tareas programadas, ejecución en la nube (desde el 2026-10-06 en Pro y Max) y Dispatch para pedirle tareas desde el celular. | Todos los planes pagos. Dispatch está en beta cerrada para Pro y Max. | Pide aprobación por defecto. En enero de 2026 PromptArmor mostró robo de archivos con un .docx con instrucciones ocultas ([The Register](https://www.theregister.com/2026/01/15/anthropics_claude_bug_cowork/)). No encontramos confirmación de que esté corregido. |
| **[Claude Tag](https://www.anthropic.com/news/introducing-claude-tag)** (Anthropic, junio de 2026) | Compañero de equipo en Slack, con memoria por canal y un modo que avisa por su cuenta. | Solo Team y Enterprise, en beta. Consume créditos de la organización. | No está en planes individuales. |
| **[Gemini Spark](https://support.google.com/gemini/answer/17094507)** (Google, mayo de 2026) | Agente personal con agendas, skills, apps conectadas y MCP. | Ultra fuera del EEE, el Reino Unido, Suiza y Nigeria. Pro, solo EE.UU. | Pide aprobación antes de enviar, modificar, comprar o completar formularios. |
| **[Meta Muse](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)** (Meta, septiembre de 2026) | Agente personal en una VM propia, con un segundo agente que aprueba todo lo que sale a internet. Se le habla en su app o por WhatsApp. | Gratis lo básico, con suscripción para más uso. | Solo en EE.UU. |

También hay agentes de este tipo de Manus (por Telegram) y de Perplexity (sobre una Mac mini propia), pero solo los encontramos en prensa, sin fuente oficial que se pudiera consultar. De Microsoft y Amazon no encontramos nada equivalente lanzado en 2026.

**Para el curso:** sirven para mostrar la categoría sin instalar nada, y para discutir lo mismo que con OpenClaw (un agente con tus credenciales que actúa solo) con controles de fábrica. Pero ninguno está al alcance de un alumno con ChatGPT Plus o Claude Pro, salvo Cowork. Lo práctico: hacer la demo de tareas programadas con Cowork y mostrar dots o Grok Bot desde la cuenta del instructor.

---

## Cómo se hizo

Tres agentes revisaron las afirmaciones del vault y las hipótesis de una investigación de junio, con la consigna de refutarlas. De las de junio cayeron cinco: el total de CVEs de OpenClaw, que Hermes aprobaba cada comando, que Odysseus era single-user y de un solo mantenedor, y el rótulo "public preview" de la app de Hermes. El script de arriba repite la parte que se puede repetir.

---
Relacionado: [[Catálogo de herramientas y productividad]] · [[Módulo 4 - Ciberseguridad aplicada]] · [[Especificación de agentes cross-CLI]] · [[Curso - Agentes de IA aplicados al trabajo técnico]]
