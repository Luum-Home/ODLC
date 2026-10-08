---
tags: [cursos, educacion, construccion-agentes]
status: borrador
created: 2026-06-10
---

# Módulo 1 — Construcción de agentes (Para todo público)

Este módulo introduce el concepto de **agentes de inteligencia artificial** a cualquier miembro de la organización, independientemente de su trasfondo técnico. Aprenderás a diseñar el comportamiento, personalidad y límites de un agente utilizando lenguaje natural estructurado.

---

## 1. ¿Qué es un Agente y en qué se diferencia de un Chatbot?

Un chat simple (como el uso básico de ChatGPT o Gemini) es reactivo: espera que le hagas una pregunta y te da una respuesta puntual de una sola vez.

Un **agente de IA**, en cambio, es proactivo e interactivo. Cuenta con:
1.  **Ciclo de Ejecución (Loop)**: Piensa, planifica, ejecuta acciones y observa los resultados de forma iterativa hasta cumplir una meta.
2.  **Herramientas**: Puede interactuar con archivos, buscar en internet, ejecutar programas o conectarse a APIs.
3.  **Memoria**: Almacena información a corto y largo plazo para mantener el contexto histórico.

---

## 2. Diseñando la Identidad del Agente

Para construir un agente consistente y evitar que responda de forma genérica, utilizamos dos archivos markdown fundamentales de la [[Especificación de agentes cross-CLI]]:

### A. El Archivo `SOUL.md` (La Constitución del Agente)
Define quién es el agente, cuáles son sus valores innegociables y cuáles son sus límites.

#### Plantilla Básica de `SOUL.md` para no técnicos:
```markdown
# Identidad del Agente
Actúas como un Coordinador de Onboarding de Clientes con alta empatía y obsesión por la eficiencia.

## Valores Core
1. **Claridad sobre Cortesía Excesiva**: Prefiere respuestas precisas a disculpas largas.
2. **Pragmatismo**: Si un cliente se equivoca enviando un formato de archivo, propón la solución y el enlace correcto de inmediato.

## Límites
- Nunca ofrezcas descuentos financieros sin aprobación humana.
- Si detectas un posible caso de fraude, delega el caso a soporte humano de inmediato.
```

### B. El Archivo `VOICE.md` (El Estilo de Comunicación)
Define cómo se expresa el agente ante el usuario o el equipo.

#### Plantilla Básica de `VOICE.md` para no técnicos:
```markdown
# Estilo Editorial

## Tono
- Profesional, directo y resolutivo.
- No uses frases de relleno ("¡Hola! Espero que estés muy bien el día de hoy...").
- No uses exclamaciones excesivas.

## Formato
- Usa listas con viñetas para pasos a seguir.
- Escribe en párrafos cortos (máximo 3 líneas).
```

---

## 3. Práctica: Redactar una Intención (Intent over Tasks)

En lugar de darle al agente una lista de tareas paso a paso (ej. "1. Abre el excel, 2. Copia la fila A, 3. Pégala en el mail"), bajo la filosofía de [[Manifiesto HACS-ODLC|Intent over Tasks]] debes definir el **Objetivo** y las **Restricciones**:

- **Mal input (Centrado en Tareas)**: *"Agente, por favor entra a la base de datos de vendedores, busca quién no subió su DNI y mándales un mail diciendo que lo hagan"*.
- **Buen input (Centrado en Intención - ODLC)**: el objetivo sigue la plantilla de [[Fase 1 - Objective]] y las restricciones van en un bloque aparte. Los valores son de ejemplo:

```yaml
objective:
  resultado_esperado: "Todos los vendedores dados de alta hoy tienen su identificación tributaria válida cargada"
  metrica_de_exito: "Vendedores del día con identificación válida: baseline 60%, target 100%"
  fecha_objetivo: "Hoy, antes del cierre de la jornada"
  impacto_de_negocio: "Sin identificación válida el vendedor no puede facturar ni cobrar"
  responsable_humano: "Responsable de onboarding de vendedores"

constraints:
  - El contacto solo puede ser por correo electrónico interno.
  - Si el vendedor falló en el primer intento, se le envía el enlace a la guía de ayuda.
```

Con intención y restricciones, el agente propone una estrategia; un humano la aprueba ([[Fase 3 - Strategy]]), y cada mensaje a un tercero espera aprobación humana antes de enviarse, como indica la fila "acción externa" de la matriz de [[Gobernanza#Límites de autonomía (matriz borrador)|Gobernanza]] ([[Registro de decisiones]], D-18).

---
Siguiente módulo: [[Módulo 2 - Ingeniería de arneses]]
Relacionado: [[Manifiesto HACS-ODLC]] · [[Especificación de agentes cross-CLI]]
