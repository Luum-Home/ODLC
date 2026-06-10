---
tags: [fundacional, especificacion, cross-cli, openclaw]
status: borrador
created: 2026-06-10
---

# Especificación de agentes cross-CLI

La **Especificación de agentes cross-CLI** describe el estándar de arquitectura basado en archivos markdown para configurar la identidad, tono, memoria y comandos operativos de agentes de inteligencia artificial de forma portátil. Este estándar permite que un mismo repositorio de código sea interpretado y operado de manera consistente por múltiples plataformas y CLI de agentes, incluyendo **Claude Code (Anthropic)**, **OpenClaw**, **Hermes Agent**, **Pi**, **OpenCode**, entre otros.

---

## 1. Filosofía: Configuración basada en Archivos (File-Based Configuration)

En lugar de depender de prompts del sistema (system prompts) gigantescos y monolíticos, las plataformas avanzadas de agentes y el modelo [[HACS]] proponen una arquitectura de **revelación progresiva y modular**. Los agentes leen archivos markdown específicos al inicio de la sesión para estructurar su contexto.

### Beneficios:
- **Portabilidad**: Las instrucciones están en formato plano en el repositorio, versionadas en Git.
- **Inspectabilidad**: Los humanos pueden auditar, editar y limitar el comportamiento del agente editando texto plano.
- **Eficiencia de Contexto**: Permite al agente cargar dinámicamente solo los módulos o "habilidades" requeridos.

---

## 2. Los Archivos Core de la Especificación

El comportamiento de un agente cross-CLI se define mediante los siguientes archivos en la raíz del proyecto o en un directorio de configuración (`.agent/` o `.openclaw/`):

### A. `CLAUDE.md` (El Protocolo de Arranque / Boot Protocol)
- **Función**: Actúa como el mapa operativo del proyecto.
- **Contenido**: 
  - Comandos para compilar, correr tests y ejecutar linters.
  - Guías de estilo de código específicas de la tecnología del repositorio.
  - Convenciones de nombres, patrones arquitectónicos y estructura de directorios.
- **Uso**: Leído por Claude Code, OpenClaw y otros motores de ejecución para entender las herramientas locales ([[Cognitive OS - Arquitectura de referencia]]).

### B. `SOUL.md` (El Núcleo Constitucional / Constitutional Layer)
- **Función**: Define la identidad "núcleo", los valores éticos, el estilo de razonamiento y los límites de seguridad del agente.
- **Contenido**:
  - Reglas de toma de decisiones estratégicas.
  - Límites de autonomía (qué acciones requieren aprobación humana).
  - Identidad de rol (ej. "Actúas como un arquitecto pragmático de sistemas distribuidos").
- **Uso**: Previene la deriva cognitiva en hilos de conversación largos.

### C. `VOICE.md` (La Personalidad y el Tono / Editorial Guide)
- **Función**: Gobierna el estilo comunicativo y lingüístico del agente.
- **Contenido**:
  - Nivel de formalidad y concisión (ej. "ve directo al grano, evita introducciones amigables").
  - Vocabulario preferido y prohibido (ej. evitar el "AI sludge" o respuestas del tipo "¡Excelente pregunta! Estaré encantado de ayudarte...").
  - Estructura y formato preferencial de respuestas (ej. uso estricto de markdown y links a archivos).

### D. `MEMORY.md` (Memoria Semántica y Hechos)
- **Función**: Registro persistente de hechos consolidados sobre el usuario, el negocio y el sistema.
- **Contenido**:
  - Preferencias específicas del usuario.
  - Arquitectura consolidada y decisiones técnicas del proyecto.
  - Historial de incidentes resueltos o patrones técnicos validados.
- **Uso**: Mantiene la continuidad entre sesiones independientes.

### E. `SESSION.md` (Protocolo de Relevo / Wind-down Protocol)
- **Función**: Facilita la transición de turnos de agentes en tareas asincrónicas de larga duración.
- **Contenido**:
  - Resumen escrito por el agente al finalizar su ejecución con el estado actual del trabajo, bloqueantes encontrados y próximos pasos detallados para el agente que despierte en la siguiente sesión.

---

## 3. Construcción de Archivos Cross-CLI Interoperables

Para asegurar que estos archivos funcionen en herramientas como OpenClaw, Claude Code y Hermes, deben seguir las siguientes reglas de diseño de primeros principios:

1.  **Formatos Estándar**: Utilizar exclusivamente Markdown plano con jerarquías de encabezados claras (`#`, `##`, `###`) y listas con viñetas. Evitar sintaxis propietarias.
2.  **Mapeo de Migración**: Frameworks como **OpenClaw** tienen importadores integrados que buscan archivos `CLAUDE.md` o `.claude/CLAUDE.md` para migrar configuraciones heredadas hacia el archivo de configuración del agente (`AGENTS.md` o `USER.md`).
3.  **Independencia del Modelo (Model Agnostic)**: Redactar las reglas de forma asertiva ("Haz X", "Evita Y") en lugar de redactar prompts específicos de un proveedor (como tags `<instruction>` de Anthropic o formatos JSON específicos), garantizando que modelos como Claude 3.5 Sonnet, GPT-4o o modelos Open Source (Llama 3, Hermes) los comprendan por igual.

---

## Hipótesis

- **H1**: Los agentes configurados con un `VOICE.md` restrictivo que prohíbe las frases performativas reducen el consumo de tokens en un 15% y aceleran los tiempos de respuesta del CLI.
- **H2**: La existencia de un `CLAUDE.md` reduce en un 90% los errores del agente al intentar ejecutar comandos de compilación o testeo locales.

## Preguntas abiertas

- ¿Cómo estandarizar la sintaxis de los comandos en `CLAUDE.md` para que sean compatibles tanto en entornos Unix (macOS/Linux) como en Windows sin duplicar la documentación?
- ¿Debería la memoria en `MEMORY.md` auto-limitarse por antigüedad para evitar sobrecargar la ventana de contexto del agente?

---
Relacionado: [[Recursos externos]] · [[Roles de agentes]] · [[Gobernanza]] · [[Cognitive OS - Arquitectura de referencia]]
