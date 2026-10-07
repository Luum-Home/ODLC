---
tags: [problema, comparativa]
status: semilla
created: 2026-06-10
---

# Comparativa con metodologías existentes

Crítica formal de [[ODLC]]/[[HACS]] contra los marcos dominantes. Cada fila es una hipótesis a desarrollar con honestidad: qué hace bien cada marco, qué no cubre, y qué reutilizamos.

> [!important] Regla de comparación: la fuente canónica, no la herramienta
> Cada método se compara contra su definición canónica, nunca contra cómo lo implementa una herramienta. Un tablero de columnas en Jira o Trello no es Kanban si no limita el WIP, no tira del trabajo y no mide el flujo; un equipo con "sprints" en Jira no hace Scrum si no tiene sus responsabilidades, eventos y artefactos. Fuentes canónicas usadas en esta nota:
> - **Manifiesto Ágil**: agilemanifesto.org (2001).
> - **Scrum**: *The Scrum Guide*, Ken Schwaber y Jeff Sutherland, versión de noviembre de 2020 (scrumguides.org).
> - **Kanban**: *The Kanban Guide*, Daniel Vacanti, versión de mayo de 2025 (kanbanguides.org); la otra escuela es el *Kanban Method* de David J. Anderson (*Kanban: Successful Evolutionary Change for Your Technology Business*, 2010).
> - **XP**: Kent Beck, *Extreme Programming Explained* (1999; 2.ª edición con Cynthia Andres, 2004).
> - **Sooner Safer Happier**: Jon Smart con Zsolt Berend, Myles Ogilvie y Simon Rohrer (IT Revolution, 2020).
> - **Gestión por objetivos**: Peter Drucker, *The Practice of Management* (1954); Joshua Seiden, *Outcomes Over Output* (2019); crítica en el punto 11 de los 14 puntos de W. Edwards Deming (deming.org).
> - **Organizaciones Teal**: Frederic Laloux, *Reinventing Organizations* (2014). Las tres rupturas (autogestión, integridad, propósito evolutivo) y el *advice process* se citan del libro; no se verificaron por comando.
>
> Verificación de las guías y del libro (2026-10-07):
> ```bash
> curl -sL https://scrumguides.org/scrum-guide.html | sed 's/<[^>]*>/ /g' | LC_ALL=C /usr/bin/grep -oE "November 2020|Ken Schwaber|Jeff Sutherland" | sort -u
> curl -sL https://kanbanguides.org/english/ | LC_ALL=C /usr/bin/grep -oE "Kanban Guide \(May 2025\)|Daniel Vacanti" | sort -u
> curl -sL https://itrevolution.com/product/sooner-safer-happier/ | LC_ALL=C /usr/bin/grep -oE "Zsolt Berend|Myles Ogilvie|Simon Rohrer" | sort -u
> curl -sL https://deming.org/explore/fourteen-points/ | sed 's/<[^>]*>/ /g' | tr -s ' \n' | LC_ALL=C /usr/bin/grep -oi "eliminate management by objective"
> curl -sL "https://openlibrary.org/search.json?q=reinventing+organizations+laloux&fields=title,author_name,first_publish_year&limit=1"
> curl -sL "https://openlibrary.org/search.json?q=outcomes+over+output+seiden&fields=title,author_name,first_publish_year&limit=1"
> curl -sL "https://openlibrary.org/search.json?q=the+practice+of+management+drucker&fields=title,author_name,first_publish_year&limit=1"
> ```

| Marco | Qué optimiza | Qué no cubre | Qué reutilizamos |
|---|---|---|---|
| **SDLC** | Secuencia: requerimientos → desarrollo → mantenimiento | Asume ejecución cara y humana; sin aprendizaje estructural | La noción de ciclo de vida |
| **Manifiesto Ágil** | Valores y principios para responder a la incertidumbre con feedback frecuente (no es un método) | No contempla agentes como participantes: asume conversación cara a cara y personas motivadas | Los valores, releídos uno por uno → [[Relectura del Manifiesto Ágil]] |
| **Scrum** | Coordinación humana (Product Backlog, Sprints, Sprint Goal y Product Goal; las historias de usuario son una práctica externa a la guía) | Agentes como ejecutores; validación contra objetivos | Iteración corta, retro → [[Fase 6 - Learning]] |
| **XP (Extreme Programming)** | Calidad técnica con feedback rápido (TDD, CI, pair programming, releases chicas) | Asume que el código lo escribe un humano; no cubre validación contra objetivos de negocio | TDD como guardarraíl de agentes → [[Fase 5 - Validation]]; pair programming como antecedente del trabajo humano-agente |
| **Kanban** | Flujo continuo (sistema pull; WIP, throughput, Work Item Age y cycle time según The Kanban Guide; lead time es medida del Kanban Method de Anderson) | Supone que alguien tira del trabajo; el work item sigue siendo la unidad y el cierre es "terminado", no outcome validado | Métricas de flujo → [[Métricas operativas]]; límites de WIP como límite de capacidad de revisión humana ([[Gobernanza]]) |
| **Sooner Safer Happier (Jon Smart, BVSSH)** | Agilidad de negocio orientada a resultados: *Better Value Sooner Safer Happier* como meta, sin importar el método; patrones y antipatrones de práctica | Organizaciones de personas; no contempla agentes ni gobernanza de autonomía | *Focus on Outcomes* refuerza *Outcomes over Output*; Safer → [[Gobernanza]]; Happier → ritmo sostenible y el humano no proactivo ([[Relectura del Manifiesto Ágil]]); el formato patrón/antipatrón como modelo para catalogar los de HACS |
| **Gestión por objetivos (MBO, OKR, Outcomes Over Output)** | Alinear el trabajo a objetivos medibles en vez de a actividades (Drucker, 1954; Seiden, 2019) | Deming pide eliminarla porque los objetivos numéricos se manipulan; no contempla agentes | Es el linaje directo de [[Fase 1 - Objective]]; la crítica de Deming queda abierta en [[Objeciones al marco]] |
| **Organizaciones Teal (Laloux)** | Autogestión (*advice process*, roles en lugar de puestos), integridad y propósito evolutivo: "sentir y responder" en lugar de "predecir y controlar" | Organizaciones de personas; evidencia basada en estudios de caso elegidos por el autor; desconfía de metas y pronósticos | Vocabulario del Nivel 5 del [[Modelo de madurez AI-Native]]; roles que no mapean 1:1 a personas ([[Unidad organizacional]]); el *advice process* como candidato para la consulta entre agentes. Tensiones con la [[Gobernanza]] y la medición: [[Objeciones al marco]] |
| **SAFe** | Coordinación a escala entre múltiples equipos humanos | Escala vía *más proceso*, no vía *más agentes* | Alineación estratégica → [[Fase 1 - Objective]] |
| **DevOps** | Entrega continua, feedback técnico | Decisión y contexto; optimiza el pipeline, no la intención | Automatización, observabilidad → [[Fase 4 - Execution]] |
| **Team Topologies** | Estructura de equipos y carga cognitiva | Los "equipos" siguen siendo 100% humanos | Carga cognitiva como límite → base de [[Unidad organizacional]] |
| **Platform Engineering** | Self-service para desarrolladores | La plataforma sirve humanos, no sistemas humano-agente | Golden paths → análogo para agentes en [[Cognitive OS - Arquitectura de referencia]] |
| **BMAD-METHOD** | Roles de agentes (PM, Architect, QA) y flujos YAML para desarrollo ágil y spec-driven | Colaboración simétrica e interactiva humano-agente y gobernanza a nivel de negocio | Roles especializados de agentes y enfoque de diseño antes de codificar (spec-driven) |
| **Agent OS (Builder Methods)** | Captura, indexación y despliegue de estándares y convenciones del código para asistentes de desarrollo (Cursor, Claude Code) | Ciclo de vida de negocio completo orientado a Outcomes, métricas y límites de autonomía de gobernanza | El concepto de indexación y descubrimiento automatizado de estándares (comandos `index-standards` y `discover-standards` sobre `agent-os/standards/`) |

## Diferencia de fondo

SDLC: requerimientos, historias de usuario, desarrollo, testing, mantenimiento.
ODLC: **Objective → Constraints → Strategy → Execution → Validation → Learning**, sobre memoria viva.

ODLC no gira alrededor de backlog, historias o sprints. Gira alrededor de objetivos, evidencia, validación y aprendizaje.

No hay que confundir los niveles: Agile es la declaración de valores; Scrum, XP y Kanban son métodos que la implementan con supuestos distintos (Kanban, por ejemplo, nunca tuvo iteraciones de tiempo fijo). ODLC se aparta de prácticas de esos métodos, no de los valores ágiles.

## Alternativas en el Espacio de Desarrollo AI-Native

Además del modelo [[HACS]] y [[ODLC]], existen otros marcos que intentan estructurar el ciclo de vida de desarrollo de software AI-Native (o AIDLC):

1.  **GSD Core (Git. Ship. Done.)**:
    -   *Enfoque*: Una alternativa mucho más ligera y de "baja ceremonia" frente a BMAD-METHOD. Se centra en meta-prompting y en ingeniería de contexto ágil para iteraciones veloces sin el overhead de simular roles de equipos completos.
2.  **GitHub Spec Kit**:
    -   *Enfoque*: Caja de herramientas centrada en comandos rápidos (`/speckit.specify`, `/speckit.plan`, `/speckit.tasks`) integrados a la terminal o IDE para mantener al programador humano en el control absoluto de la orquestación (human-in-the-loop) en lugar de automatizar de forma multi-agente.
3.  **OpenSpec y AWS Kiro**:
    -   *OpenSpec*: formato abierto de especificaciones para LLMs.
    -   *Kiro (AWS)*: IDE y CLI de agentes con flujo spec-driven.

*Nota de verificación (2026-07-28, contra los clones de `external/`): Agent OS instala sus estándares en `agent-os/standards/` y despliega sus comandos a `.claude/commands/agent-os/` (`external/agent-os/scripts/project-install.sh:199,389`); no usa `.agent/INSTRUCTIONS.md` — esa ruta pertenece a la propuesta propia de este vault, ver [[Especificación de agentes cross-CLI]]. GSD Core se expande como "Git. Ship. Done.", no "Getting Stuff Done" (`external/gsd-core/README.md:5`). Los comandos de Spec Kit llevan el prefijo `speckit.` en la versión vigente del clon (`external/spec-kit/README.md:161-165`). `external/` no se versiona (está en `.gitignore`): se reconstruye con `./sync_external.sh` desde la raíz del repo, que clona agent-os, gsd-core y spec-kit entre otros. Los números de línea corresponden a los clones locales re-verificados el 2026-10-07 (agent-os `cae8e66`, gsd-core `28ac89d8`, spec-kit `5ae7ff5`, según `git -C external/<repo> log -1 --format=%h`); un sync posterior trae HEAD y puede correrlos.*

---

## Preguntas abiertas

- ¿Cómo se *integra* ODLC con Scrum o Kanban en una adopción gradual? Un equipo Kanban parece estar más cerca (sin sprints, con métricas de flujo): ¿la transición es más corta? (crítico para [[Modelo de madurez AI-Native]] niveles 1–3; ver [[Preguntas abiertas]])
- Team Topologies habla de "carga cognitiva del equipo" — ¿cómo se redefine cuando parte de la cognición es de agentes?
