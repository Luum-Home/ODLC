---
tags: [fundacional, preguntas]
status: borrador
created: 2026-06-10
---

# Preguntas abiertas

Este documento consolida las principales **preguntas abiertas** e interrogantes sin resolver identificadas durante los debates de diseño de **HACS** y la metodología **ODLC**. Estas preguntas sirven como líneas de investigación priorizadas para futuros ciclos de evolución del vault.

---

## Bloques Temáticos

### 1. Adopción e Integración Organizacional
- **¿Cómo se certifica o audita un sistema HACS?**
  - Si una empresa desea transicionar a ODLC, ¿existe un framework objetivo de certificación o auditoría independiente? ¿Cómo se evalúa la veracidad de su nivel de madurez?
- **¿Cómo se coordina HACS con equipos Scrum, XP o Kanban mientras conviven?**
  - Que conviven durante la transición está decidido: ODLC reemplaza la unidad de trabajo solo en equipos que arrancan desde cero, y en los existentes se adopta de a poco ([[Registro de decisiones]], D-03). Queda abierto el cómo: ¿cómo interactúa una unidad cognitiva HACS orientada a objetivos con un equipo Scrum que trabaja por Product Backlog Items y Sprints, o con un equipo Kanban que trabaja por flujo continuo? ¿Cómo mapear dependencias entre ambos mundos?
- **¿Qué pasa con un humano que no es proactivo?**
  - HACS supone que el humano define objetivos, decide y valida por iniciativa propia. Scrum compensaba la falta de iniciativa con sprints y compromisos; ODLC no tiene un equivalente. ¿Cómo se mide si las salvaguardas de diseño (plantilla que no arranca sin métrica, validación que no se aprueba sin evidencia) alcanzan? → [[Relectura del Manifiesto Ágil#El humano que no es proactivo]] · principios propuestos y su respaldo: [[Objeciones al marco#Principios para tolerar al humano de mínimo esfuerzo]]
  - ¿Cómo se logra que el debrief de Learning ocurra si nadie lo convoca? La evidencia sobre debriefs supone que alguien los conduce.
- **¿Cómo se acorta la deliberación sin convertirla en atajo?**
  - Si los agentes comprimen el research y el desarrollo, el tiempo total queda dominado por planificar, discutir, decidir y validar. Ninguna vía relevada tiene medido cuánto acorta la decisión, y un Decision Lead Time bajo no distingue decidir rápido con varias alternativas de decidir rápido imponiendo una. ¿Qué hay que registrar junto al DLT para separar los dos casos? → [[Objeciones al marco#Objeción 7: lo que no se acelera]]

### 2. Economía y Retorno de Inversión (ROI)
- **¿Cómo se calcula el ROI real de implementar Cognitive OS?**
  - Configurar sandboxes seguros, buses de memoria estructurados y pagar tokens de modelos comerciales tiene un costo financiero inmediato. ¿Cómo cuantificamos el valor de evitar fallos de diseño y aumentar el aprendizaje organizativo en comparación con la contratación de ingenieros humanos tradicionales?

### 3. Límites Técnicos y Deriva de Contexto
- **¿Cómo resolver la escala y degradación del contexto?**
  - A medida que un repositorio acumula cientos de objetivos y miles de entradas en memoria, la ventana de contexto de los agentes se degrada. ¿Cómo curamos y sintetizamos la memoria de manera eficiente sin perder los matices históricos importantes? → [[Memoria organizacional]]
- **¿Cómo mitigar la sobrecarga de revisión humana (Fatiga de Gobernanza)?**
  - Aunque el merge a main es configurable por madurez ([[Gobernanza]]), las aprobaciones que la matriz única marca como humanas ([[Registro de decisiones]], D-01) pueden saturar al humano: puede convertirse rápidamente en el nuevo cuello de botella operativo, aprobando cosas de forma automática por fatiga. ¿Cómo automatizar la gobernanza sin perder el control moral y de riesgo?
- **¿Qué compensa la revisión cuando pasa a manos de agentes?**
  - Si la revisión humana exhaustiva se vuelve cuello de botella o sello de goma y pasa a agentes, ¿con qué métricas responde quien diseña el sistema de revisión (tests que el escritor no edita, radio de daño, muestreo humano, defectos sembrados), y qué reemplaza la comprensión compartida que producía la revisión humana? → [[Objeciones al marco#Objeción 8: la revisión en manos de agentes]]

### 4. Sesgo y Evolución de la Memoria
- **¿Cómo evitamos que la memoria organizacional amplifique malas decisiones históricas?**
  - Si una mala decisión arquitectónica se registra en memoria y los agentes la consumen como "verdad aprendida", ¿cómo detectamos y corregimos este sesgo sistemático en ciclos futuros? ¿Quién lidera la reescritura de la memoria semántica?

---

## Próximos Pasos para la Investigación
1.  **Modelado híbrido**: Diseñar un caso de estudio sobre un equipo mixto (humanos en Scrum o Kanban usando agentes de soporte) para trazar puntos de fricción reales.
2.  **Esquema de Sandbox**: Prototipar una configuración segura y rápida en un contenedor Docker local para medir la latencia y robustez de la validación automatizada de código.

---
Relacionado: [[Gobernanza]] · [[Por qué fallan las metodologías actuales]] · [[Riesgos]]
