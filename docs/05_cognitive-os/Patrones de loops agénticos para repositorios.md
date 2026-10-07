---
tags: [cognitive-os, agent-loop, repositorios, gobernanza, memoria, validacion]
status: semilla
created: 2026-06-13
---

# Patrones de loops agénticos para repositorios

Un repositorio AI-native no es solo un contenedor de código. Es un entorno operativo donde humanos y agentes comparten reglas, memoria, evidencia, validación y criterios de cierre.

Estos patrones describen cómo diseñar repositorios que puedan ser trabajados por agentes sin depender de improvisación conversacional.

---

## 1. Repo como sistema operativo para agentes

Un repositorio preparado para agentes debe exponer sus reglas de operación como artefactos legibles por humanos y máquinas.

Debe contener, de forma explícita:

- cómo se inicia un cambio;
- qué fases debe atravesar;
- qué límites de autonomía existen;
- qué evidencia debe producirse;
- qué tests o checks son obligatorios;
- qué rol valida;
- cuándo se puede cerrar;
- qué aprendizaje debe persistirse.

La unidad mínima no es “un prompt bueno”, sino un conjunto de contratos que el agente puede seguir, auditar y reutilizar.

---

## 2. Process-as-code para agentes

El proceso no puede vivir solo en la cabeza del equipo. Debe estar codificado como parte del repositorio.

Patrón:

```text
Reglas del repo → skills → flujo de contribución → playbook de revisión → tests → PR gates
```

Un repositorio AI-native debe declarar sus reglas operativas como artefactos legibles por agentes.

Ejemplos de artefactos:

- índice de instrucciones para agentes;
- skills o runbooks por tipo de tarea;
- reglas de contribución;
- convenciones de commits y PRs;
- playbook de revisión;
- plantillas de issue/spec;
- gates de CI;
- criterios de evidencia.

Esto transforma el proceso en una superficie ejecutable. El agente no “recuerda” cómo trabajar: lo lee, lo aplica y deja evidencia.

### Riesgo mitigado

- drift de proceso;
- agentes improvisando reglas;
- revisiones inconsistentes;
- dependencia de conocimiento tácito;
- pérdida de contexto entre sesiones.

---

## 3. Memoria con ciclo de vida

No alcanza con memoria persistente. Una memoria que nunca caduca termina funcionando como una verdad eterna, aunque haya envejecido.

Patrón:

```text
memoria creada → memoria activa → memoria stale / necesita revisión → revisión humana/agente → actualizar, superseder o marcar vigente
```

La [[Memoria organizacional]] no debe ser acumulativa sin caducidad. Las decisiones, políticas y preferencias necesitan señales de vigencia.

### Estados mínimos

| Estado | Significado | Acción esperada |
|---|---|---|
| **Creada** | La observación acaba de persistirse | Indexar y hacer recuperable |
| **Activa** | Puede usarse como contexto vigente | Recuperar normalmente |
| **Necesita revisión** | La vigencia temporal o contextual es dudosa | Verificar antes de usar |
| **Supersedida** | Otra memoria más nueva la reemplaza | Mostrar relación, no usar como fuente principal |
| **Descartada** | Ya no aplica o fue falsa | Mantener para auditoría o eliminar según política |

### Qué memorias deberían tener revisión periódica

- decisiones de arquitectura;
- políticas de seguridad;
- preferencias de equipo;
- convenciones de implementación;
- supuestos de negocio;
- runbooks operativos;
- límites de autonomía de agentes.

### Regla

Una memoria vieja no es necesariamente falsa. Pero tampoco debe ser tratada como vigente sin verificación.

---

## 4. Stale memory como failure mode

[[Riesgos|Memory poisoning]] no significa solo guardar algo falso. También puede significar guardar algo que fue verdadero, pero envejeció.

Dos nombres útiles:

- **Obsolescencia de memoria**: una decisión, política o preferencia pierde vigencia y sigue siendo recuperada como actual.
- **Context rot por memoria persistente**: el sistema arrastra contexto viejo a loops nuevos, degradando decisiones futuras.

### Ejemplo abstracto

```text
Mes 1: “Usar librería A para autenticación” era correcto.
Mes 9: el equipo migró a librería B.
Mes 12: un agente recupera la memoria vieja y vuelve a proponer librería A.
```

La memoria no estaba “mal” cuando fue creada. El problema es que no tenía ciclo de revisión.

### Mitigaciones

- `review_after` conceptual para decisiones/políticas/preferencias;
- relaciones `supersedes` / `superseded_by`;
- revisión periódica de memorias críticas;
- obligación de verificar memorias stale contra el repo actual;
- diferenciación explícita entre hecho, hipótesis, decisión y preferencia.

---

## 5. Apply/Judge/Fix loop

Un cambio agéntico serio no termina cuando el Builder produce código. Necesita un loop adversarial de revisión.

Patrón:

```text
apply → fresh review → findings → fix → re-review → merge
```

### Fases

1. **Apply**: el agente implementa una unidad de trabajo acotada.
2. **Fresh review**: un reviewer con contexto fresco inspecciona diff, tests, docs y contratos.
3. **Findings**: los hallazgos se clasifican como blockers, warnings o suggestions.
4. **Fix**: el agente corrige los blockers sin expandir el alcance.
5. **Re-review**: se verifica que los blockers fueron cerrados y que no se introdujeron regresiones.
6. **Merge/close**: solo si la evidencia alcanza el umbral definido por [[Gobernanza]].

Este patrón separa producción de validación. El mismo agente puede ejecutar ambas capacidades, pero el contexto debe resetearse o independizarse para evitar sesgo de confirmación.

---

## 6. TDD con evidencia

Pedirle a un agente “hacé TDD” es insuficiente. El loop debe exigir evidencia auditable.

Patrón:

```text
RED → GREEN → TRIANGULATE → REFACTOR → evidence table → verify
```

TRIANGULATE es un paso agregado por este patrón; en Beck (*Test-Driven Development: By Example*, 2002) triangular es una estrategia opcional para llegar a GREEN.

Evidencia mínima por tarea:

| Paso | Evidencia | Riesgo mitigado |
|---|---|---|
| **RED** | test fallando por la razón esperada | implementación sin test real |
| **GREEN** | código mínimo que hace pasar el test | sobre-ingeniería |
| **TRIANGULATE** | segundo caso o borde relevante | green falso o hardcodeo |
| **REFACTOR** | mejora con tests pasando | deuda técnica accidental |
| **VERIFY** | ejecución de comandos y revisión de assertions | premature success |

El agente no debería marcar una tarea como completa si no puede mostrar evidencia del ciclo.

Ver también: [[Agent Loop Engineering#Patrón aplicado: TDD para agentes]].

---

## 7. Fresh-context validation

La validación con el mismo hilo que implementó el cambio tiende a confirmar sus propias hipótesis. Para cambios relevantes, conviene introducir revisión con contexto fresco.

Patrón:

```text
implementation context ≠ validation context
```

La revisión fresca debe inspeccionar:

- diff completo;
- archivos afectados por frontera;
- tests agregados o modificados;
- cobertura de errores y bordes;
- docs actualizadas;
- contratos públicos;
- riesgos de migración;
- alineación con reglas del repo.

Esto se alinea con [[Fase 5 - Validation]]: validar no es creerle al productor del artefacto, sino contrastar evidencia contra el objetivo y las restricciones.

---

## 8. Evidence-driven implementation

La implementación no se declara terminada porque el agente lo dice. Se cierra porque produjo evidencia suficiente.

Patrón:

```text
diff + tests + docs + review + checks
```

Todo loop agéntico que modifica un sistema debe producir evidencia auditable en cada frontera afectada.

### Fronteras típicas

| Frontera | Evidencia esperada |
|---|---|
| Store / persistencia | migraciones, tests de lectura/escritura, compatibilidad |
| API / MCP / HTTP | payloads, errores, contratos, tests de handler |
| UI / TUI | render de estados, navegación, tests visuales o snapshots |
| Sync / cloud | push/pull, idempotencia, replay, errores determinísticos |
| Docs | comandos, paths y comportamiento actualizados |
| Seguridad | permisos, secretos, inputs no confiables, blast radius |

---

## 9. Dispatcher por estado, no por intuición

Un agent loop robusto no decide el siguiente paso por sensación conversacional. Lo decide por estado estructurado.

Patrón:

```text
si faltan specs → spec
si faltan tasks → tasks
si hay blockers → fix
si tests pasan y review aprueba → close
```

Un dispatcher mínimo necesita:

- estado explícito;
- phase readiness;
- blockers;
- artifacts existentes;
- evidencia faltante;
- próximo paso recomendado;
- condición de stop.

### Estado mínimo recomendado

```yaml
loop_state:
  phase: spec | tasks | apply | verify | fix | close
  goal: ""
  artifacts:
    specs: present | missing
    tasks: present | missing
    apply_progress: present | missing
    verify_report: present | missing
  blockers: []
  tests:
    command: ""
    status: pass | fail | not_run
  review:
    status: pending | approved | changes_requested
  next_recommended: ""
```

Esto reduce loops infinitos, premature success y pérdida de continuidad entre agentes.

---

## 10. Riesgos que mitiga

| Riesgo | Mitigación del patrón |
|---|---|
| Context rot | memoria con ciclo de vida y revisión de stale context |
| Memory poisoning | separar falso de obsoleto; relaciones de supersession |
| Premature success | evidence-driven implementation + verify independiente |
| Observation blindness | review fresca y parsers de estado |
| Tool ping-pong | dispatcher con next step computable |
| Over-agentification | fases y gates explícitos para decidir cuándo usar agentes |
| No replayability | artifacts, reports, diffs, tests y summaries persistidos |
| Drift de proceso | process-as-code dentro del repo |

---

## Decisiones

- **D1**: En HACS-ODLC, la memoria persistente debe tratarse como un sistema con ciclo de vida, no como almacenamiento acumulativo infinito.
- **D2**: Los repositorios AI-native deben declarar reglas operativas en artefactos legibles por agentes.
- **D3**: Los loops que modifican sistemas deben cerrar por evidencia, no por afirmación del agente.
- **D4**: Para cambios relevantes, la validación debe separar contexto de implementación y contexto de revisión.
- **D5**: El siguiente paso del loop debe derivarse de estado estructurado siempre que sea posible.

---
Relacionado: [[Agent Loop Engineering]] · [[Memoria organizacional]] · [[Gobernanza]] · [[Roles de agentes]] · [[Fase 4 - Execution]] · [[Fase 5 - Validation]] · [[Fase 6 - Learning]] · [[Riesgos]]
