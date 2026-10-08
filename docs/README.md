---
tags: [meta]
status: evergreen
created: 2026-06-10
---

# Vault HACS + ODLC

**Autor:** Matías Nahuel Améndola.
**Contribuciones:** Sebastián Gauna.

> [!note] Si estás leyendo esto desde GitHub
> La explicación general del repositorio está en `../README.md`.
> Este archivo explica cómo usar `docs/` como vault de conocimiento.

Este vault es el **documento de trabajo vivo** de HACS (Human-Agent Collaborative Systems) y ODLC (Objective Driven Lifecycle). No es un whitepaper terminado: es la base editable desde la cual se construye la metodología, al estilo de cómo evolucionaron el Agile Manifesto, Team Topologies o Domain-Driven Design.

Los PDFs históricos están en `00_crudo/` (`HACS_Canvas.pdf`, `ODLC_Canvas.pdf`, `HACS_ODLC_Whitepaper_v0.1.pdf`, `HACS_ODLC_Master_Document_v0.2.pdf`). Son **snapshots históricos**; la fuente canónica de verdad es este vault en markdown.

## Principios del vault (estilo Karpathy)

1. **Markdown plano, versionado en git.** Nada de formatos propietarios. El texto plano es future-proof, diffeable, y legible tanto por humanos como por LLMs/agentes. Un agente debe poder cargar cualquier nota como contexto sin preprocesamiento.
2. **Una idea por nota (notas atómicas).** Cada nota es autocontenida: se entiende sin haber leído las demás. Si una nota crece con dos ideas, se divide.
3. **Append-and-review.** Todo lo crudo entra primero a `00_crudo/` (inbox). En cada revisión, lo que madura se promueve a nota atómica; lo que no, se borra o se queda esperando.
4. **Documentos vivos, no prosa cerrada.** Las notas capturan *hipótesis*, *evidencia*, *decisiones* y *preguntas abiertas* — explícitamente separadas. Una afirmación sin evidencia se marca como hipótesis, no se disfraza de hecho.
5. **Links sobre jerarquía.** Las carpetas son una conveniencia; la estructura real son los enlaces internos tipo wikilink y el mapa de contenido [[HACS-ODLC]]. Un link a una nota que no existe todavía marca trabajo pendiente, no un error.
6. **Escrito para tu yo futuro y para agentes.** Contexto explícito, sin sobreentendidos. Fechas absolutas, no relativas. Ejemplos concretos antes que abstracciones.

## Estructura

| Carpeta | Contenido |
|---|---|
| `00_crudo/` | Inbox: material sin procesar (append-and-review) |
| `01_problema/` | Por qué las metodologías actuales no alcanzan |
| `02_hacs/` | El modelo organizacional HACS |
| `03_odlc/` | La metodología ODLC, fase por fase |
| `04_metricas/` | Métricas operativas, de agentes y organizacionales |
| `05_ingenieria-de-agentes/` | Ingeniería de agentes y arneses (loops, patrones, economía de tokens), análisis de videos y casos de uso |
| `06_fundacional/` | Manifiesto, madurez, glosario, roadmap, riesgos, preguntas abiertas |
| `07_cursos/` | Programa de capacitación: Construcción de agentes, arneses, gobernanza y ciberseguridad |
| `08_referencias/` | Catálogos volátiles: repos externos, herramientas, skills, especificaciones de terceros |

**Punto de entrada:** [[HACS-ODLC]]

## Rutas de lectura rápidas

**Para entender el marco completo:**

1. [[HACS-ODLC]]
2. [[Por qué fallan las metodologías actuales]]
3. [[HACS]]
4. [[ODLC]]
5. [[Agent Loop Engineering]]
6. [[Manifiesto HACS-ODLC]]
7. [[Glosario y taxonomía]] — vocabulario formal del marco; sirve también como consulta suelta mientras se leen las demás notas.

**Para capacitación y ofertas:**

- [[Cursos HACS-ODLC]]

**Para herramientas y referencias externas:**

- [[Recursos externos]]
- [[Catálogo de herramientas y productividad]]

## Convenciones de notas

Frontmatter mínimo en cada nota:

```yaml
---
tags: [hacs | odlc | problema | metricas | ...]
status: crudo | semilla | borrador | evergreen
created: YYYY-MM-DD
---
```

- `crudo`: material sin destilar, tal como entró al inbox. Exclusivo de `00_crudo/`: no es una nota atómica todavía y no debería enlazarse como fuente canónica. Una nota que parte de material crudo lo cita en el frontmatter con `origen:`, no con `fuente:` ([[Registro de decisiones]], D-12).
- `semilla`: idea capturada, mayormente preguntas abiertas.
- `borrador`: estructura completa, contenido en evolución.
- `evergreen`: estable, se actualiza solo con nueva evidencia.

Las notas meta, como este README y el [[Inbox]], llevan el tag `meta` y `status: evergreen` aunque vivan en `00_crudo/` (D-12).

El orden refleja el flujo de *append-and-review*: lo que entra como `crudo` se promueve a nota atómica (`semilla` → `borrador` → `evergreen`) o se descarta.

Secciones recurrentes dentro de las notas: **Hipótesis**, **Evidencia**, **Decisiones**, **Preguntas abiertas**. Mantenerlas separadas es deliberado: es lo que distingue un documento de trabajo de marketing.
