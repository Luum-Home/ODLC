---
tags: [fundacional, roadmap]
status: borrador
created: 2026-06-10
---

# Roadmap

Este **Roadmap** define los hitos de maduración y despliegue del ecosistema **HACS + ODLC**. El objetivo es transicionar desde un marco conceptual abstracto hacia especificaciones técnicas formales y herramientas que permitan la adopción empresarial a gran escala.

---

## Fases de Evolución

### v0.1 — Concepto (Completado)
- **Hito**: Formulación de la tesis fundacional: *"la unidad básica de trabajo cambia de equipo humano a sistema cognitivo humano-agente"*.
- **Entregables**: Captura inicial de ideas (notas de la conversación fundacional sobre AI SDLC).

### v0.2 — Canvas y Estructuración (Completado)
- **Hito**: Estructuración de los canvases fundacionales (`HACS_Canvas.pdf` y `ODLC_Canvas.pdf`, dos páginas cada uno) y formalización del ciclo de 6 fases de [[ODLC]] y los 4 componentes de [[HACS]].
- **Entregables**: `HACS_Canvas.pdf` y `ODLC_Canvas.pdf`, de referencia histórica en `00_crudo/`.

### v0.3 — Whitepaper y Vault Vivo (En Progreso - Actual)
- **Hito**: Consolidar el whitepaper y migrar la fuente de verdad a un vault interconectado en Markdown, permitiendo que humanos y LLMs interactúen sobre una misma base de verdad.
- **Entregables ya producidos**: `HACS_ODLC_Whitepaper_v0.1.pdf` y `HACS_ODLC_Master_Document_v0.2.pdf` (snapshots históricos de versiones anteriores, archivados en `00_crudo/`).
- **En progreso**: notas atómicas de Métricas, ingeniería de agentes y bases Fundacionales en este directorio `docs/` (fuente canónica viva).

### v1.0 — Especificación formal (Planificado)
- **Hito**: Estandarizar los protocolos de datos y esquemas de [[HACS]] (memoria, roles de agentes, ejecución en sandbox) para permitir implementaciones interoperables.
- **Entregables**:
  - Esquemas de bases de datos para el bus de memoria (esquemas de grafos y vectores para la [[Memoria organizacional]]).
  - Protocolos de comunicación JSON-Schema para los [[Roles de agentes]].
  - Configuración de políticas de seguridad para la ejecución segura en Sandboxes de desarrollo.

### v2.0 — Adopción empresarial y Automatización Adaptativa (Futuro)
- **Hito**: Integración del modelo en organizaciones de desarrollo de software tradicionales.
- **Entregables**:
  - Herramientas de diagnóstico para auditar el [[Modelo de madurez AI-Native]].

---

## Hipótesis de Roadmap

- **H1**: Estandarizar esquemas en la versión v1.0 facilitará que desarrolladores externos creen agentes y herramientas compatibles entre sí.
- **H2**: La transición al desarrollo v2.0 requiere que los LLMs locales/open-source alcancen paridad de razonamiento lógico con los modelos de frontera propietarios del momento, para reducir costos de tokens operativos. (Hipótesis formulada en junio 2026; "paridad" debe reevaluarse contra la frontera vigente, no contra modelos fijos.)

## Preguntas abiertas

- ¿Qué tipo de certificaciones organizacionales son viables para auditar que un equipo implementa correctamente ODLC?

---
Relacionado: [[Modelo de madurez AI-Native]] · [[HACS]]
