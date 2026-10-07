---
tags: [cognitive-os, agent-loop, arneses, gobernanza, memoria, evals]
status: semilla
created: 2026-06-13
---

# Agent Loop Engineering

**Agent Loop Engineering** es la disciplina de diseñar el loop de control de un agente, no solo su prompt.

Un agente no es únicamente un LLM con instrucciones. Es un sistema que observa, decide, actúa con herramientas, interpreta resultados, actualiza estado/memoria y decide si termina, reintenta, escala o continúa. La calidad del agente depende tanto del loop como del modelo.

## Definición formal

Agent Loop Engineering es el diseño explícito del ciclo repetible por el cual un agente:

```text
Trigger → Goal → State → Reason/Plan → Action → Observation → Verification → Memory Update → Termination/Replan
```

En forma mínima:

```text
Observation → Reason/Plan → Action → Observation → ...
```

En producción, el loop incluye:

- estado persistente;
- herramientas;
- memoria;
- budgets;
- políticas de acción;
- condiciones de terminación;
- verificación;
- retries;
- human-in-the-loop;
- trazas/evals;
- coordinación multi-agente.

## Por qué importa

El salto de *prompt engineering* a *loop engineering* es el salto de pedir una buena respuesta a diseñar un sistema que pueda perseguir un objetivo verificable bajo restricciones.

Un prompt puede resolver una tarea puntual. Un loop decide:

- cuándo actuar;
- con qué herramienta;
- cómo interpretar el resultado;
- qué hacer ante fallos;
- cuándo detenerse;
- qué guardar como aprendizaje;
- cuándo pedir intervención humana.

En [[HACS]], esto es la mecánica interna por la cual los [[Roles de agentes]] operan dentro de la [[Gobernanza]]. En [[ODLC]], es la forma técnica de recorrer [[Fase 3 - Strategy]], [[Fase 4 - Execution]], [[Fase 5 - Validation]] y [[Fase 6 - Learning]] sin depender de improvisación conversacional.

---

## Fundamentos conceptuales

### ReAct — Reason + Act

**ReAct** (Yao et al., 2022, [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)) define el loop mínimo: intercalar razonamiento y acciones con herramientas.

```text
Thought → Action → Observation → Thought → Action → ...
```

Su aporte central es que el agente no solo “piensa” ni solo “llama herramientas”: usa observaciones externas para corregir su trayectoria.

Límite: ReAct por sí solo no define memoria persistente, políticas de seguridad, budgets, condiciones de stop ni aprendizaje entre sesiones.

### Reflexion — feedback convertido en memoria

**Reflexion** (Shinn et al., 2023, [arXiv:2303.11366](https://arxiv.org/abs/2303.11366)) agrega una fase posterior al intento fallido:

```text
Attempt → Feedback → Reflection → Memory Update → Retry
```

Su aporte es convertir fallos en texto reutilizable sin fine-tuning. Esto se alinea con [[Fase 6 - Learning]] y con prácticas como session summaries, bug notes, gotchas y repair loops.

Riesgo: si el feedback es incorrecto o la reflexión es falsa, se produce [[Riesgos|contaminación de memoria]].

### Tree of Thoughts — búsqueda deliberada

**Tree of Thoughts** (Yao et al., 2023, [arXiv:2305.10601](https://arxiv.org/abs/2305.10601)) expande el loop lineal a una búsqueda sobre múltiples caminos de razonamiento:

```text
Generate alternatives → Evaluate → Select/Backtrack → Continue
```

Sirve cuando:

- hay decisiones irreversibles;
- hay alta incertidumbre;
- el primer plan suele ser malo;
- conviene comparar estrategias antes de ejecutar.

Costo: más tokens, más latencia y más necesidad de arbitraje.

### Voyager — loop + biblioteca de skills

**Voyager** (Wang et al., 2023, [arXiv:2305.16291](https://arxiv.org/abs/2305.16291)) agrega una idea clave: el aprendizaje no es solo memoria textual, sino acumulación de habilidades ejecutables.

Patrón:

```text
Explore → Attempt → Error/Feedback → Improve → Save Skill → Reuse Skill
```

Esto conecta con [[Repositorios y catálogos de skills]] y con la visión de [[Cognitive OS - Arquitectura de referencia]]: el sistema mejora cuando transforma aprendizajes repetibles en herramientas, skills o políticas reutilizables.

---

## Niveles de madurez del loop

| Nivel | Loop | Sirve para | Riesgo principal |
|---|---|---|---|
| **L0** | Single prompt | Respuestas simples, generación puntual | No hay agencia real; todo depende del prompt inicial |
| **L1** | LLM + tools loop | Tareas cortas con herramientas | Loop infinito, repetición, tool ping-pong |
| **L2** | Loop + state/memory | Tareas multi-step y continuidad entre pasos | Memoria mala contamina decisiones futuras |
| **L3** | Loop + guardrails/HITL | Tareas riesgosas o con efectos reales | Fricción, latencia, exceso de aprobación humana |
| **L4** | Loop + evals/tracing | Producción y auditoría | Overhead operacional y falsa confianza en métricas incompletas |
| **L5** | Multi-agent loop | Investigación amplia, debugging complejo, migraciones | Coordinación, costo, conflictos de archivos, síntesis pobre |
| **L6** | Self-improving loop | Skills, lessons, evals, mejora acumulativa | Drift, falsa mejora, memory/skill poisoning |

Principio de diseño: empezar en el loop más simple que resuelve el objetivo y subir de nivel solo cuando la complejidad del problema lo exige.

---

## Componentes que hay que diseñar

### 1. Trigger

Define qué inicia el loop.

Ejemplos:

- pedido del usuario;
- PR abierto;
- issue creado;
- alerta de producción;
- failing CI;
- cron;
- release gate;
- cambio de archivo;
- evento externo de negocio.

Un trigger mal definido produce loops que corren en momentos incorrectos o sobre señales débiles.

### 2. Goal

El objetivo debe ser verificable.

Malo:

> Mejorá el repo.

Bueno:

> Hacer que `make test-targeted` pase y que el chequeo estricto de drift no reporte inconsistencias.

En ODLC, el Goal se formaliza en [[Fase 1 - Objective]] y se acota con [[Fase 2 - Constraints]].

### 3. State

El loop necesita estado explícito, no solo historial conversacional.

Estado mínimo:

- objetivo actual;
- plan vigente;
- herramientas usadas;
- archivos tocados;
- errores vistos;
- decisiones tomadas;
- presupuesto consumido;
- bloqueos;
- intentos/retries;
- evidencia recolectada.

Sin estado explícito, el agente depende de una ventana de contexto frágil.

### 4. Action policy

Define qué puede hacer el agente y bajo qué condiciones.

Ejemplos:

- leer archivos: permitido;
- editar archivos: permitido dentro del radio de impacto;
- ejecutar tests: permitido;
- commitear/pushear: solo si el usuario lo pidió;
- tocar secretos: prohibido;
- borrar ramas: solo si están mergeadas y con confirmación;
- ejecutar SQL destructivo: requiere HITL;
- lanzar subagentes: limitado por presupuesto.

La action policy materializa [[Gobernanza]] dentro del loop.

### 5. Observation parser

No alcanza con “ver texto”. El loop debe interpretar observaciones.

Categorías útiles:

- pass;
- fail;
- flaky;
- timeout;
- blocked;
- conflict;
- permission issue;
- stale cache;
- external dependency;
- generated artifact drift;
- no-progress;
- high-risk action.

Un agente con mal observation parser puede mirar un error y extraer la conclusión equivocada.

### 6. Termination

La terminación es una de las partes más subestimadas del loop.

Condiciones de stop:

- criterios de aceptación cumplidos;
- pruebas/verificaciones pasan;
- evidencia suficiente recolectada;
- presupuesto agotado;
- mismo error repetido 2–3 veces;
- no-progress detectado;
- requiere decisión humana;
- riesgo alto;
- conflicto de archivos;
- dependencia externa caída.

Sin terminación explícita aparecen loops infinitos, gasto de tokens y reportes prematuros de éxito.

### 7. Memory update

Define qué se guarda al final o durante el loop.

Guardar:

- bugfixes;
- decisiones;
- patrones;
- gotchas;
- evidencia;
- comandos que funcionaron;
- comandos que fallaron;
- límites encontrados;
- nuevas skills reutilizables.

No guardar:

- hipótesis no verificadas como hechos;
- summaries sin trazabilidad cuando había que inspeccionar la fuente;
- errores transitorios como reglas permanentes;
- secretos, credenciales o datos sensibles.

La memoria es parte del loop, pero también puede envenenarlo.

---

## Patrón aplicado: TDD para agentes

TDD para agentes no se resuelve diciendo "hacé TDD" en el prompt. Se resuelve diseñando un loop donde el agente no pueda saltarse el ciclo de aprendizaje y verificación.

El patrón operativo es:

```text
Init de capacidades → Estado persistente → Apply con evidencia obligatoria → Verify que audita proceso → Dispatcher de siguiente paso → Memoria/artifacts para continuidad
```

### 1. Init de capacidades

Antes de exigir TDD, el sistema debe detectar qué capacidades reales tiene el proyecto:

- test runner disponible;
- comandos de test por capa;
- cobertura;
- linter/typechecker;
- estructura de tests existente;
- restricciones de edición;
- convenciones del repo.

Sin esta fase, el agente inventa comandos, promete cobertura inexistente o aplica una receta genérica que no encaja con el proyecto.

### 2. Estado persistente

El TDD agéntico necesita estado fuera de la conversación:

- capacidades detectadas;
- modo TDD activo/inactivo;
- tareas pendientes;
- progreso por task;
- tests escritos;
- evidencia RED/GREEN/REFACTOR;
- bloqueos;
- archivos tocados;
- resultados de verificación.

Ese estado puede vivir en memoria, archivos OpenSpec, artefactos del repo o una combinación. Lo importante es que el siguiente turno o subagente pueda reconstruir dónde está parado el loop.

### 3. Apply con evidencia obligatoria

La fase de implementación debe exigir evidencia por unidad de trabajo, no solo resultado final.

Evidencia mínima:

| Paso | Evidencia esperada | Riesgo que evita |
|---|---|---|
| **RED** | test nuevo falla por la razón correcta | escribir código sin test o test irrelevante |
| **GREEN** | implementación mínima hace pasar el test | sobre-ingeniería y cambios no necesarios |
| **TRIANGULATE** | segundo caso evita green falso | tests tautológicos o hardcodeados |
| **REFACTOR** | mejora interna con tests pasando | deuda técnica y regresiones silenciosas |

TRIANGULATE es un paso agregado por este patrón; en Beck (*Test-Driven Development: By Example*, 2002) triangular es una estrategia opcional para llegar a GREEN.

Si el agente no registra esta evidencia, la tarea no debería considerarse completa.

### 4. Verify que audita proceso

La verificación no debe limitarse a "los tests pasan". Debe auditar también el proceso:

- si hubo RED real;
- si el test toca código productivo;
- si las assertions verifican comportamiento y no tautologías;
- si hay casos suficientes para el escenario;
- si la capa de test elegida corresponde al riesgo;
- si el resultado cubre spec, design y constraints;
- si hay warnings por cobertura, mocks excesivos o smoke tests débiles.

Esto transforma TDD en una práctica verificable, no en una declaración de intención.

### 5. Dispatcher que decide el siguiente paso

Un dispatcher evita que el agente decida desde intuición conversacional. Debe computar:

- qué artifacts existen;
- qué dependencias están listas;
- qué tasks faltan;
- si apply está bloqueado, listo o completo;
- si verify pasó o dejó issues;
- cuál es el próximo paso recomendado.

El agente debería rutear por estado estructurado, no por "me parece que ya seguimos".

### 6. Memoria y artifacts para continuidad

El loop debe guardar outputs reutilizables:

- testing capabilities;
- apply-progress;
- verify-report;
- decisiones;
- gotchas;
- comandos válidos;
- fallos encontrados;
- cambios de alcance.

La continuidad es clave porque TDD agéntico suele cruzar subagentes, compactaciones, sesiones y ramas. Sin artifacts, cada agente vuelve a empezar y aumenta el riesgo de context rot o premature success.

### Lectura desde ODLC

Este patrón ubica TDD dentro de ODLC:

- **Objective**: comportamiento esperado y criterios de aceptación.
- **Constraints**: comandos reales, capas de test, límites de edición y seguridad.
- **Strategy**: selección de capa de test y plan de ciclos.
- **Execution**: RED/GREEN/TRIANGULATE/REFACTOR con evidencia.
- **Validation**: auditoría independiente de resultado y proceso.
- **Learning**: persistencia de capacidades, reportes, fallos y convenciones.

La diferencia central con TDD humano informal es que el agente necesita un arnés que le impida hacer trampa: estado explícito, compuertas, evidencia y verificación independiente.

---

## Patrones de repositorio para loops agénticos

Cuando el loop opera sobre un repositorio, el diseño debe incluir patrones específicos: process-as-code, memoria con ciclo de vida, revisión fresca adversarial, implementación basada en evidencia y dispatcher por estado.

Estos patrones convierten el repo en una superficie operativa para agentes, no solo en un lugar donde guardar código.

Ver: [[Patrones de loops agénticos para repositorios]].

## Guardrails y human-in-the-loop

Un loop serio necesita compuertas para acciones riesgosas:

- allow/deny por herramienta;
- approval gates;
- audit log;
- rollback;
- resumability;
- structured decision records;
- budget caps;
- rate limits;
- blast radius;
- trust score antes de declarar éxito.

Esto conecta directamente con [[Luum Cognitive OS - Implementación de referencia]]: la Safety Mesh no reemplaza al agente; gobierna su loop.

---

## Multi-agent loops

Un multi-agent loop coordina varios loops especializados bajo un agente líder.

Patrón:

```text
Lead Agent:
  plan
  spawn subagents
  collect summaries
  reconcile
  verify
  final answer/action
```

Útil para:

- investigación amplia;
- debugging complejo;
- auditorías de repo;
- comparación de alternativas;
- migraciones grandes;
- revisión de seguridad;
- validación independiente.

Riesgos:

- duplicación;
- drift entre agentes;
- costo;
- conflicto de archivos;
- mala síntesis;
- “todos coinciden” pero nadie verificó fuente primaria.

En HACS, el multi-agent loop debe estar subordinado a [[Roles humanos]] y [[Gobernanza]], no operar como enjambre sin propietario.

---

## Failure modes del loop

### Loop infinito

El agente repite acciones sin condición de stop efectiva.

Mitigación: max turns, retry budget, no-progress detector, cost caps y escalamiento humano.

### Tool ping-pong

El agente alterna entre las mismas herramientas sin obtener nueva información.

Mitigación: registrar tool history, exigir hipótesis nueva antes de repetir y cortar tras repeticiones equivalentes.

### Observation blindness

El agente ve la salida de una herramienta pero interpreta mal el error o ignora señales importantes.

Mitigación: parsers estructurados, clasificación de errores, tests determinísticos y revisión humana en casos ambiguos.

### Context rot

El historial acumulado degrada la precisión; el agente arrastra detalles irrelevantes o contradictorios.

Mitigación: compactación, summaries estructurados, estado explícito y reinicio limpio con contexto mínimo viable.

### Memory poisoning

El agente guarda una conclusión falsa, obsoleta o mal contextualizada y la reutiliza después.

Mitigación: guardar evidencia junto con la memoria, distinguir hipótesis de hechos, curaduría periódica y expiración de observaciones frágiles.

### Premature success

El agente declara “done” sin evidencia suficiente.

Mitigación: claim validator, trust score, ground-truth checks, verificación independiente y [[Fase 5 - Validation]].

### Over-agentification

Se usa un loop agéntico complejo para una tarea lineal simple.

Mitigación: elegir el menor nivel de madurez suficiente; preferir scripts determinísticos cuando el camino es conocido.

### No budget awareness

El loop consume tokens, tiempo o cómputo sin progreso proporcional.

Mitigación: budgets explícitos, token/cost accounting, timeouts y stop por no-progress.

### No source-of-truth discipline

El agente responde desde summaries o memoria cuando debía inspeccionar código, logs o documentación primaria.

Mitigación: política de fuentes primarias, evidence citations y obligación de abrir archivos/salidas relevantes antes de decidir.

### No replayability

No quedan trazas, comandos ni evidencia para reproducir lo que ocurrió.

Mitigación: tracing, logs de herramientas, comandos registrados, snapshots de estado y decisiones estructuradas.

---

## Relación con Cognitive OS

El [[Cognitive OS - Arquitectura de referencia]] puede leerse como una arquitectura para operar agent loops gobernados:

- **Interfaz de Definición**: captura Trigger, Goal y Constraints.
- **Bus de Memoria**: provee estado histórico y guarda Memory Updates.
- **Motor de Orquestación**: ejecuta Reason/Plan, Action Policy y coordinación multi-agente.
- **Sandbox de Ejecución**: contiene las acciones con herramientas.
- **Validation Engine**: recolecta evidencia y audita la ejecución. La decisión de terminar, reintentar o escalar la toma el propio agent loop (su condición de termination), que corre dentro del Motor de Orquestación.
- **Aprendizaje (Fase 6)**: no es uno de los cinco componentes de la arquitectura; en su diagrama es la etapa que transforma la evidencia en memoria, políticas o skills y escribe en el Bus de Memoria.

Agent Loop Engineering es, por lo tanto, la disciplina microscópica; Cognitive OS es la arquitectura macroscópica que la vuelve operable en una organización.

---

## Decisiones

- **D1**: En HACS-ODLC, ningún loop con efectos reales debe depender solo de un prompt. Debe declarar objetivo, estado, herramientas permitidas, presupuestos, stop conditions y evidencia esperada.
- **D2**: La complejidad del loop debe crecer por necesidad, no por moda. ReAct simple antes que multi-agent, workflow determinístico antes que agente si el camino ya está conocido.
- **D3**: Todo loop que escribe memoria debe separar hechos, hipótesis, decisiones y evidencia para evitar memory poisoning.

## Preguntas abiertas

- ¿Qué métricas estándar deberíamos usar para detectar no-progress en loops largos?
- ¿Cuándo conviene transformar una memoria repetida en skill ejecutable?
- ¿Cómo versionar skills generadas por agentes sin introducir drift?
- ¿Qué parte del observation parser debe ser determinística y qué parte puede delegarse a un LLM judge?

---
Relacionado: [[Cognitive OS - Arquitectura de referencia]] · [[Análisis - Construyendo un Arnés de IA desde Cero]] · [[Luum Cognitive OS - Implementación de referencia]] · [[Riesgos]] · [[Glosario y taxonomía]] · [[Repositorios y catálogos de skills]]
