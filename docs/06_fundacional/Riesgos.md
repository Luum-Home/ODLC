---
tags: [fundacional, riesgos]
status: borrador
created: 2026-06-10
---

# Riesgos

La implementación de **HACS** y la adopción de **ODLC** representan una transformación profunda de la cultura de ingeniería y operativa. Por ello, es crucial identificar y estructurar los riesgos asociados para diseñar salvaguardas efectivas desde el diseño de la [[Gobernanza]].

---

## 1. Riesgos Humanos

### A. Dependencia Cognitiva
- **Descripción**: Los humanos asumen que las propuestas y códigos generados por los agentes son 100% correctos y omiten revisiones críticas exhaustivas (ceguera de automatización).
- **Mitigación**: Exigir firmas digitales humanas explícitas en cada cambio y auditorías aleatorias sobre los PRs aprobados por agentes.

### B. Atrofia de Conocimiento (Pérdida de Expertise)
- **Descripción**: Al delegar la codificación completa a agentes Builder, los ingenieros humanos pierden la capacidad de entender en profundidad el funcionamiento del sistema, quedando inhabilitados para resolver incidentes graves complejos.
- **Mitigación**: Rotación de roles. Los ingenieros humanos deben escribir periódicamente componentes críticos o liderar refactorizaciones profundas de forma manual.

---

## 2. Riesgos Técnicos

### A. Alucinaciones e Inconsistencias
- **Descripción**: Los agentes proponen estrategias de ejecución basadas en APIs inexistentes o versiones de librerías deprecadas.
- **Mitigación**: Conectar los agentes a un compilador y linters dentro del Sandbox de ejecución seguro. El código no puede proponerse si no compila e integra exitosamente.

### B. Bucles Infinitos de Ejecución (Infinite Loops)
- **Descripción**: Un agente Builder intenta resolver recursivamente un test roto y consume miles de dólares en tokens en pocas horas.
- **Mitigación**: Límites rígidos y alertas de costos (Cost Caps) a nivel del orquestador en [[Cognitive OS - Arquitectura de referencia]]. Límite de 5 reintentos automáticos antes de requerir intervención de un operador humano. Ver [[Agent Loop Engineering]] para failure modes como loop infinito, tool ping-pong, observation blindness, context rot, memory poisoning y premature success.

### C. Contaminación de Memoria
- **Descripción**: Entradas obsoletas o erróneas en la memoria organizacional desvían la toma de decisiones de los agentes en ciclos futuros.
- **Mitigación**: Curaduría obligatoria. El agente Memory debe correr tareas periódicas de purga y consolidación bajo supervisión del rol humano de Architect.

### D. Obsolescencia de Memoria
- **Descripción**: Una memoria verdadera en su momento envejece y sigue siendo recuperada como guía vigente. Esto produce context rot por memoria persistente: decisiones, políticas o preferencias obsoletas contaminan loops futuros.
- **Mitigación**: Ciclo de vida de memoria con estados de vigencia, revisión periódica, relaciones de supersession y obligación de verificar memorias stale antes de usarlas como fuente de decisión. Ver [[Patrones de loops agénticos para repositorios#Stale memory como failure mode]].

### E. Inyección de Prompts (Directa e Indirecta)
- **Descripción**: Un atacante secuestra el comportamiento del agente mediante instrucciones maliciosas, ya sea en el prompt directo o —el vector de mayor riesgo— embebidas en datos externos que el agente lee (páginas web, PDFs, correos).
- **Mitigación**: Escaneo semántico y determinista de entradas antes de procesar el objetivo, y auditoría de la memoria al persistir observaciones. Detalle técnico en [[Módulo 4 - Ciberseguridad aplicada]].

### F. Secuestro de Ejecución en Sandbox
- **Descripción**: Código vulnerable o malicioso generado por un agente escapa de un sandbox mal aislado y daña el host o la red interna.
- **Mitigación**: Aislamiento de infraestructura (contenedores con virtualización de syscalls), límites de escritura por directorio y simulación periódica de intrusión (`/pentest-self`). Ver [[Módulo 4 - Ciberseguridad aplicada]].

---

## 3. Riesgos Organizacionales

### A. Métricas Incompatibles (Fricción de Gestión)
- **Descripción**: La gerencia continúa exigiendo métricas tradicionales (Story Points cerrados, horas completadas) mientras el equipo intenta trabajar bajo la métrica OSR y TTO.
- **Mitigación**: Alinear los incentivos organizacionales. El éxito del equipo se asocia al cumplimiento de objetivos de negocio, no a la producción física de software.

### B. Fugas de Datos y Privacidad
- **Descripción**: Envío accidental de credenciales sensibles, claves de bases de datos o información privada de usuarios (PII) a las APIs de modelos de lenguaje externos de terceros.
- **Mitigación**: Filtros de sanitización y redacción de PII antes del envío de datos al orquestador, detección de secretos en cada escritura al repositorio, y uso preferente de modelos open-source locales para datos hiper-confidenciales. Detalle técnico en [[Módulo 4 - Ciberseguridad aplicada]].

---

## Hipótesis

- **H1**: Implementar un sandbox restrictivo con validaciones estáticas automatizadas reduce las alucinaciones de código integradas a producción a prácticamente cero.
- **H2**: Aumentar la automatización de la gobernanza de costos previene fugas de presupuesto por loops infinitos en un 100%.

## Preguntas abiertas

- ¿Cómo equilibrar la velocidad de desarrollo del agente frente al tiempo de espera y el costo de ejecutar tests end-to-end completos en cada validación?
- ¿Qué responsabilidad legal asume la organización si un agente autónomo causa daños directos en producción debido a una alucinación no detectada? → [[Gobernanza]]

---
Relacionado: [[Gobernanza]] · [[Roles humanos]] · [[Por qué fallan las metodologías actuales]] · [[Agent Loop Engineering]] · [[Patrones de loops agénticos para repositorios]]
