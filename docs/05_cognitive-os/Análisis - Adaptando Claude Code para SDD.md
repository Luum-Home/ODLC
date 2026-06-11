---
tags: [recursos, cognitive-os, material-audiovisual, sdd, arneses]
status: borrador
created: 2026-06-10
fuente:
  tipo: video
  titulo: "Esto es lo que Aprendí Adaptando Claude Code para SDD"
  canal: "BettaTech"
  url: "https://www.youtube.com/watch?v=ElGlTv2A_bM"
  consultado: 2026-06-10
---

# Análisis — Adaptando Claude Code para SDD

Este documento analiza y resume estructuradamente el video referencial **"Esto es lo que Aprendí Adaptando Claude Code para SDD"** (disponible en [YouTube](https://www.youtube.com/watch?v=ElGlTv2A_bM)). El video aborda la disciplina de **Harness Engineering** aplicada al flujo de **Spec-Driven Development (SDD)**, modelando un sistema multi-agente disciplinado y eficiente con intervención humana obligatoria.

---

## 1. Harness Engineering vs. Spec-Driven Development (SDD)

El autor establece una importante distinción terminológica y conceptual:
- **Harness Engineering**: Es la disciplina general de la ingeniería de software nativa de IA que consiste en estructurar, instrumentar y automatizar flujos de trabajo de desarrollo (como Cascada, Iterativo, TDD, SDD) utilizando agentes de IA para ejecutar cada etapa.
- **Spec-Driven Development (SDD)**: Es un flujo de trabajo de desarrollo específico donde el diseño del software (la especificación) se define primero como fuente de verdad y precede a cualquier línea de código, actuando la IA como un transpilador de la spec al código fuente.

---

## 2. Arquitectura del Sistema Multi-Agente

Para evitar que un único agente de IA intente realizar todo el ciclo y degrade su contexto o cometa errores, se propone dividir las responsabilidades en cuatro agentes especializados coordinados por un estado de memoria externa:

```
                  ┌─────────────────────────────────┐
                  │          Agente Líder           │
                  │         (Orquestador)           │
                  └─────────────────────────────────┘
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│   Spec Author   │       │   Implementer   │       │    Reviewer     │
│ (Requisitos/Dis)│       │ (Construcción)  │       │  (Validación)   │
└─────────────────┘       └─────────────────┘       └─────────────────┘
```

1. **Agente Líder / Orquestador (`leader.md`)**: El "jefe" del flujo. Lee la memoria del estado del proyecto (un archivo JSON de tareas) y gatilla secuencialmente a los agentes según el estado de la tarea:
   - `pending` → Llama al **Spec Author** → Cambia a `spec ready`.
   - **HITL (Pausa Humana)**: Espera aprobación humana para cambiar a `in progress`.
   - `in progress` → Llama al **Implementer** y **Reviewer** → Cambia a `done`.
2. **Spec Author Agent (`spec_author.md`)**: Responsable de redactar la especificación técnica en tres archivos dentro del directorio `specs/`:
   - `requirements.md`: Historias de usuario o requisitos funcionales.
   - `design.md`: Explicación técnica detallada (archivos a modificar, clases/funciones a crear, código descartado).
   - `tasks.md`: Lista granular de subtareas paso a paso para el implementador.
3. **Implementer Agent (`implementer.md`)**: Un agente de código de alcance limitado. No define arquitectura; simplemente toma la especificación de `tasks.md` y edita quirúrgicamente las líneas indicadas.
4. **Reviewer Agent (`reviewer.md`)**: Valida que el código generado coincida con el diseño de la especificación, ejecuta linters y pruebas unitarias (`pytest`), y aprueba o rechaza los cambios.

---

## 3. Principio de Higiene y Curaduría de Contexto

Uno de los mayores aprendizajes del video es la **higiene de contexto**:
- **Evitar la Degradación de Chats**: Los chats de LLM muy largos acumulan ruido e historial innecesario.
- **Filtro de Contexto Externo**: En lugar de transferir el historial del chat del *Spec Author* al *Implementer*, el sistema persiste la salida útil en archivos Markdown físicos (`specs/design.md`, `specs/tasks.md`).
- **Contexto Mínimo Viable (MVC)**: El implementador se inicia en una sesión limpia y nueva, recibiendo únicamente el código base y la especificación refinada en disco. Esto reduce drásticamente el costo de tokens y evita que el modelo alucine o pierda el foco de la tarea.

---

## 4. Notación EARS (Easy Approach to Requirements Syntax)

En lugar de utilizar historias de usuario genéricas (que tienden a ser ambiguas), el video recomienda redactar los requisitos técnicos bajo la **Notación EARS**.
EARS propone plantillas estrictas y condicionales para declarar requisitos:

> **Fórmula EARS:**
> *`[Gatillo/Condición] [Precondición] el sistema debe [Comportamiento esperado]`*
>
> **Ejemplo:**
> *"Cuando el usuario ejecuta el comando `recent` sin pasar el parámetro `--limit`, el sistema debe imprimir un máximo de 5 notas en orden descendente."*

### Beneficio para la Validación
La estructura de EARS es tan precisa que **cada requisito funcional se mapea de forma directa 1:1 a un test unitario**, eliminando ambigüedades en la fase de validación del *Reviewer*.

---

## 5. Alineación con HACS-ODLC

* **Gobernanza Humana (HITL)**: El autor enfatiza no automatizar al 100% el ciclo sin supervisión humana. Las compuertas de cambio de estado (de `spec ready` a `in progress`) requieren la aprobación explícita de un ingeniero para evitar la deriva técnica del software.
* **Memoria Organizacional**: Todas las decisiones de arquitectura e historiales de cambios se persisten de forma estructurada en un archivo `history.md`, sirviendo como bitácora permanente del sistema.

---
Relacionado: [[Cognitive OS - Arquitectura de referencia]] · [[Recursos externos]] · [[Memoria organizacional]] · [[Módulo 2 - Ingeniería de arneses]] · [[Fase 3 - Strategy]]
