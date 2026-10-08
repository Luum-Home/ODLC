# HACS + ODLC

Repositorio de trabajo para definir, organizar y evolucionar **HACS** y **ODLC**: un marco para operar equipos humanos + agentes de IA como una unidad de trabajo gobernada, medible y con memoria.

## En una frase

Este repo no es una app ni una librería: es un **vault de conocimiento versionado en Markdown** para construir una metodología de trabajo AI-native.

## Qué problema intenta resolver

La IA ya puede producir código, documentación, análisis y automatizaciones muy rápido, pero eso no garantiza mejores resultados organizacionales. El cuello de botella se mueve de “escribir más rápido” a:

- definir objetivos claros;
- mantener contexto y memoria;
- coordinar humanos y agentes;
- validar resultados con evidencia;
- gobernar seguridad, costos y autonomía.

Este repo documenta una respuesta a ese problema.

## Conceptos principales

### HACS — Human-Agent Collaborative Systems

**HACS** es el modelo organizacional: equipos compuestos por humanos, agentes, memoria compartida y gobernanza.

La tesis central: la unidad de trabajo deja de ser solo el equipo humano y pasa a ser un **sistema cognitivo humano-agente**.

Entrada recomendada: [`docs/02_hacs/HACS.md`](docs/02_hacs/HACS.md)

### ODLC — Objective Driven Lifecycle

**ODLC** es la metodología operativa de un sistema HACS.

En vez de organizar el trabajo alrededor de tickets, tareas o sprints, ODLC lo organiza alrededor de objetivos medibles:

```text
Objective → Constraints → Strategy → Execution → Validation → Learning
```

Entrada recomendada: [`docs/03_odlc/ODLC.md`](docs/03_odlc/ODLC.md)

### Ingeniería de agentes

Cómo se diseñan y gobiernan los loops de agentes y los arneses que los corren: estado, herramientas, condiciones de corte, evidencia y presupuesto de tokens. Incluye análisis de material audiovisual y el caso Alta Tienda.

Entrada recomendada: [`docs/05_ingenieria-de-agentes/Agent Loop Engineering.md`](docs/05_ingenieria-de-agentes/Agent%20Loop%20Engineering.md)

## Cómo leer este repo

Si querés entender el marco completo:

1. [`docs/HACS-ODLC.md`](docs/HACS-ODLC.md) — mapa de contenido.
2. [`docs/01_problema/Por qué fallan las metodologías actuales.md`](docs/01_problema/Por%20qué%20fallan%20las%20metodologías%20actuales.md) — problema.
3. [`docs/02_hacs/HACS.md`](docs/02_hacs/HACS.md) — modelo organizacional.
4. [`docs/03_odlc/ODLC.md`](docs/03_odlc/ODLC.md) — metodología.
5. [`docs/05_ingenieria-de-agentes/Agent Loop Engineering.md`](docs/05_ingenieria-de-agentes/Agent%20Loop%20Engineering.md) — ingeniería de agentes.
6. [`docs/06_fundacional/Manifiesto HACS-ODLC.md`](docs/06_fundacional/Manifiesto%20HACS-ODLC.md) — principios.

Si querés usarlo para capacitación:

- [`docs/07_cursos/Cursos HACS-ODLC.md`](docs/07_cursos/Cursos%20HACS-ODLC.md)

Si querés ver herramientas y referencias externas:

- [`docs/08_referencias/Recursos externos.md`](docs/08_referencias/Recursos%20externos.md)
- [`docs/08_referencias/Catálogo de herramientas y productividad.md`](docs/08_referencias/Catálogo%20de%20herramientas%20y%20productividad.md)

## Estructura del repo

```text
docs/
  00_crudo/                 Material recibido o sin procesar
  01_problema/              Diagnóstico: por qué SDLC/Scrum/DevOps no alcanzan solos
  02_hacs/                  Modelo organizacional Human-Agent Collaborative Systems
  03_odlc/                  Metodología Objective Driven Lifecycle y sus fases
  04_metricas/              Métricas operativas, de agentes y organizacionales
  05_ingenieria-de-agentes/ Loops y arneses de agentes, análisis y casos
  06_fundacional/           Manifiesto, glosario, madurez, riesgos y roadmap
  07_cursos/                Material de capacitación y propuestas comerciales
  08_referencias/           Catálogos de herramientas, repos y fuentes externas
external/                   Repositorios de terceros usados como referencia
```

## Estado del material

El material está vivo. No debe leerse como whitepaper final ni como documentación cerrada.

Estados usados en las notas:

- `semilla`: idea capturada, todavía inmadura.
- `borrador`: estructura útil, contenido en evolución.
- `evergreen`: nota estable, actualizable con nueva evidencia.

Los PDFs históricos están en `docs/00_crudo/`. La fuente canónica actual es el Markdown dentro de `docs/`. Una nota que parte de material de `docs/00_crudo/` lo cita en el frontmatter con `origen:`, no con `fuente:` (decisión D-12 de `docs/06_fundacional/Registro de decisiones.md`).

## Cómo trabajar con el vault

Recomendación: abrir `docs/` como raíz del vault en Obsidian.

Motivos:

- los `[[wikilinks]]` están pensados desde `docs/`;
- `external/` contiene repos clonados y no debería mezclarse con las notas;
- el contenido canónico vive en Markdown dentro de `docs/`.

Guía del vault: [`docs/README.md`](docs/README.md)

## Qué NO es este repo

- No es una implementación productiva de agentes.
- No es un framework cerrado.
- No es una promesa de reemplazar Scrum, DevOps o Platform Engineering.
- No es un catálogo neutral de herramientas: las referencias externas están al servicio del marco HACS/ODLC.

## Licencia y uso

Pendiente de formalizar. Hasta que exista una licencia explícita, tratar el contenido como material de trabajo interno/no redistribuible.
