---
tags: [cursos, educacion, gobernanza, lideres, tecnico]
status: borrador
created: 2026-06-10
---

# Módulo 3 — Gobernanza de sistemas cognitivos (Híbrido)

Este módulo está dirigido tanto a líderes de proyecto como a ingenieros de software. Aprenderás a definir e implementar la **gobernanza de autonomía**, asegurando que los agentes autónomos operen dentro de límites financieros, éticos y técnicos seguros.

---

## 1. El Concepto de Gobernanza Humana (Human Governance)

El quinto valor del [[Manifiesto HACS-ODLC]] establece que **los humanos lideran la estrategia y deciden los límites de riesgo, mientras que los agentes analizan y ejecutan**. 

Un sistema sin gobernanza (donde un agente puede desplegar a producción sin revisión o realizar compras de servidores de forma autónoma) es altamente inestable y peligroso para la organización.

---

## 2. Los Tres Pilares de la Gobernanza de Agentes

### A. Límites de Presupuesto (Cost Caps)
- **Definición**: Reglas duras de software que impiden que los agentes consuman créditos ilimitados en llamadas a modelos de lenguaje (LLM).
- **Implementación**: 
  - Límite de dólares ($) de tokens por ciclo de objetivo.
  - Límite de cantidad de iteraciones automáticas por objetivo (ej. no más de 5 reintentos automáticos en compilación).

### B. Compuertas de Aprobación Humana (Human-in-the-Loop - HITL)
- **Definición**: Puntos del ciclo de desarrollo donde el agente debe pausar su ejecución y esperar que un humano valide y firme la acción antes de continuar.
- **Acciones obligatorias HITL**:
  - Aprobación de la estrategia seleccionada ([[Fase 3 - Strategy]]).
  - Despliegues de código a entornos de producción.
  - Modificación de esquemas de bases de datos.
  - Acceso a secretos del sistema o claves criptográficas de API de producción.

### C. Registro de Auditoría (Audit Trails)
- **Definición**: Trazabilidad completa de las acciones del agente.
- **Implementación**: Cada cambio de código propuesto por un agente en Git debe ir firmado con su ID de agente y linkeado con la decisión arquitectónica en la [[Memoria organizacional]] que lo justifica.

---

En el entorno local y en la carpeta `external/` cuentas con herramientas de referencia clave (ver [[Recursos externos]]):
-   `external/gentleman-guardian-angel/`: Un agente diseñado para actuar como "Ángel Guardián" o supervisor de seguridad. Su propósito es interceptar las llamadas a comandos del sistema propuestas por otros agentes, auditar que no contengan comandos peligrosos (como `rm -rf /` o lecturas de secretos del entorno), y requerir la confirmación interactiva de un operador humano antes de su ejecución.
-   **Luum Cognitive OS (`~/Projects/luum/luum-agent-os/`)**: Repositorio desarrollado en colaboración entre **Luum** y **OliveX**. Contiene la implementación real de la malla de gobernanza para agentes de desarrollo (`cos` CLI y ganchos de control).
    -   *Práctica*: Accede al directorio `~/Projects/luum/luum-agent-os/` y examina el archivo de configuración `cognitive-os.yaml` para comprender cómo se estructuran las fases de proyecto y políticas de calidad. Revisa la carpeta `hooks/` para estudiar el comportamiento de scripts restrictivos como `claim-validator.sh` (evita falsificaciones de tests) y `blast-radius.sh` (restringe el radio de escritura de archivos).

---
Siguiente módulo: [[Módulo 4 - Ciberseguridad aplicada]]
Relacionado: [[Gobernanza]] · [[Manifiesto HACS-ODLC]] · [[Recursos externos]]
