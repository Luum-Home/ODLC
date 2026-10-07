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
- **¿Cómo coexiste HACS con equipos Scrum, XP o Kanban?**
  - En organizaciones grandes, la migración completa es inviable en el corto plazo. ¿Cómo interactúa una unidad cognitiva HACS orientada a objetivos con un equipo Scrum que trabaja por historias y sprints, o con un equipo Kanban que trabaja por flujo continuo? ¿Cómo mapear dependencias entre ambos mundos?
- **¿Qué pasa con un humano que no es proactivo?**
  - HACS supone que el humano define objetivos, decide y valida por iniciativa propia. Scrum compensaba la falta de iniciativa con sprints y compromisos; ODLC no tiene un equivalente. ¿Cómo se mide si las salvaguardas de diseño (plantilla que no arranca sin métrica, validación que no se aprueba sin evidencia) alcanzan? → [[Relectura del Manifiesto Ágil#El humano que no es proactivo]]

### 2. Economía y Retorno de Inversión (ROI)
- **¿Cómo se calcula el ROI real de implementar Cognitive OS?**
  - Configurar sandboxes seguros, buses de memoria estructurados y pagar tokens de modelos comerciales tiene un costo financiero inmediato. ¿Cómo cuantificamos el valor de evitar fallos de diseño y aumentar el aprendizaje organizativo en comparación con la contratación de ingenieros humanos tradicionales?

### 3. Límites Técnicos y Deriva de Contexto
- **¿Cómo resolver la escala y degradación del contexto?**
  - A medida que un repositorio acumula cientos de objetivos y miles de entradas en memoria, la ventana de contexto de los agentes se degrada. ¿Cómo curamos y sintetizamos la memoria de manera eficiente sin perder los matices históricos importantes? → [[Memoria organizacional]]
- **¿Cómo mitigar la sobrecarga de revisión humana (Fatiga de Gobernanza)?**
  - Si la [[Gobernanza]] requiere aprobación humana para cada PR, despliegue y cambio arquitectónico, el humano puede convertirse rápidamente en el nuevo cuello de botella operativo, aprobando cosas de forma automática por fatiga. ¿Cómo automatizar la gobernanza sin perder el control moral y de riesgo?

### 4. Sesgo y Evolución de la Memoria
- **¿Cómo evitamos que la memoria organizacional amplifique malas decisiones históricas?**
  - Si una mala decisión arquitectónica se registra en memoria y los agentes la consumen como "verdad aprendida", ¿cómo detectamos y corregimos este sesgo sistemático en ciclos futuros? ¿Quién lidera la reescritura de la memoria semántica?

---

## Próximos Pasos para la Investigación
1.  **Modelado híbrido**: Diseñar un caso de estudio sobre un equipo mixto (humanos en Scrum o Kanban usando agentes de soporte) para trazar puntos de fricción reales.
2.  **Esquema de Sandbox**: Prototipar una configuración segura y rápida en un contenedor Docker local para medir la latencia y robustez de la validación automatizada de código.

---
Relacionado: [[Gobernanza]] · [[Por qué fallan las metodologías actuales]] · [[Riesgos]]
