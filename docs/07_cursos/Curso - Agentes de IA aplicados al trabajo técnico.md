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
> Lo que se puede construir por plan cambia cada pocas semanas: entre junio y octubre de 2026 se vencieron tres de estas afirmaciones. Estado al 2026-10-07, con fuentes en [[Agentes abiertos y planes SaaS - Verificación]]:
> - **ChatGPT Plus/Pro ya no pueden crear GPTs nuevos.** Los existentes se usan hasta su retiro, el 2026-12-11, y la migración oficial los convierte en plugins. Para el taller de "crear un asistente", en plan individual usar skills o plugins.
> - **Workspace Agents** son solo de Business, Enterprise y Edu, y se cobran por tokens desde el 2026-07-06.
> - **Agent Builder** de platform.openai.com cierra el 2026-11-30. No usarlo.
> - **Claude Cowork** está en todos los planes pagos (Pro, Max, Team, Enterprise). Skills y plugins propios también, pero compartirlos con colegas requiere Team o Enterprise.
> - **Créditos de API de Claude**: desde el 2026-10-07 los tienen Max y Team. Pro no. Con el login de la suscripción, el Agent SDK y `claude -p` siguen consumiendo los límites del plan.
> - **Gemini**: el agente personal (Spark) pide Google AI Pro o Ultra. Los Gems se reemplazan por skills en cuentas personales desde noviembre de 2026.
> - **Carpeta `.agent/` con `SOUL.md`, `MEMORY.md`**: no es una función de Cowork. Es un patrón del vault inspirado en OpenClaw.
>
> Antes de cada dictado: `scripts/verificar_fuentes_agentes.sh`.

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

El curso combina **25% de conceptos y fundamentos** con **75% de práctica aplicada** (30 + 90 minutos por encuentro). Cada encuentro dura 2 horas, con aproximadamente 30 minutos de concepto y 90 minutos de taller. El cuarto encuentro funciona como jornada de práctica integradora.

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
