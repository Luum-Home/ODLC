---
tags: [fundacional, critica, hipotesis]
status: borrador
created: 2026-10-07
---

# Objeciones al marco

¿Tiene sentido ODLC? Esta nota junta las objeciones más fuertes contra el marco y lo que haría falta para contestarlas. Respuesta provisoria: **ODLC tiene sentido como hipótesis a probar, todavía no como metodología a adoptar.** Las objeciones de abajo son la razón.

---

## Lo que sostiene al marco

- **El diagnóstico apunta al cuello de botella correcto.** Cuando ejecutar se abarata, lo escaso pasa a ser definir qué se quiere, decidir y validar ([[Nuevos cuellos de botella]]). Un ciclo cuya unidad es el objetivo con métrica, validado contra el outcome, ataca ese cuello; un ciclo organizado alrededor de producir ítems no.
- **La memoria consultable por agentes es nueva de verdad.** Que el aprendizaje de un ciclo quede disponible como evidencia para los agentes del ciclo siguiente ([[Fase 6 - Learning]], [[Memoria organizacional]]) no lo resuelve ningún marco anterior.

---

## Objeción 1: "orientado a objetivos" no es nuevo, y tiene una crítica pendiente

La gestión por objetivos tiene setenta años de linaje: *Management by Objectives* (Peter Drucker, *The Practice of Management*, 1954), los OKR, *Outcomes Over Output* (Joshua Seiden, 2019), el ciclo construir-medir-aprender de Lean Startup y *Better Value Sooner Safer Happier* ([[Comparativa con metodologías existentes]]).

Y tiene una crítica clásica que ODLC no contestó: W. Edwards Deming, en el punto 11 de sus 14 puntos, pide eliminar la gestión por objetivos, porque los objetivos numéricos se manipulan y llevan a gestionar el número en lugar del sistema. ODLC pone una métrica en el centro de cada objetivo y se expone exactamente a eso (Goodhart: [[Análisis - La Cultura del Token]]).

*Fuente verificable:* `curl -sL https://deming.org/explore/fourteen-points/ | sed 's/<[^>]*>/ /g' | tr -s ' \n' | grep -oi "eliminate management by objective"`

**Para contestarla:** declarar qué hace ODLC distinto de MBO. Candidatos a desarrollar: el objetivo se valida contra evidencia y no se negocia como meta de desempeño individual; la métrica no se usa para evaluar personas; [[Fase 6 - Learning]] registra los objetivos fallidos como aprendizaje y no como incumplimiento. Ninguno de los tres está escrito hoy como regla.

## Objeción 2: el ciclo de feedback puede volverse más lento

Scrum mide un Increment porque se observa en días. El outcome real tarda lo que tarde el mundo en reaccionar (adopción, uso, mercado), y además se confunde con otras causas. Si el éxito solo cuenta cuando el outcome está validado, el aprendizaje puede ser más lento que en los métodos que ODLC critica, lo que contradice la promesa de velocidad.

**Para contestarla:** definir qué se aprende mientras se espera el outcome (indicadores tempranos, validaciones parciales) y cómo se separa el tiempo de espera de evidencia del tiempo de trabajo en el *Time To Outcome* ([[Métricas operativas#Instrumentación pendiente]]).

## Objeción 3: no hay ni un caso medido

El [[Caso - Alta Tienda]] es ilustrativo; las métricas de [[Métricas operativas]], [[Métricas de agentes]] y [[Métricas organizacionales]] no tienen instrumentación; y una auditoría del vault (2026-10-07) encontró contradicciones en el núcleo, como qué conserva el humano en el Nivel 5 o desde cuándo una adopción "ya es ODLC" ([[Modelo de madurez AI-Native]], [[Manifiesto HACS-ODLC]]). Hoy el marco es un conjunto de hipótesis, no una metodología probada.

## Objeción 4: ¿ODLC es una metodología de IA?

El [[Manifiesto HACS-ODLC]] dice que adoptar la [[Fase 1 - Objective]] y la [[Fase 6 - Learning]] sin agentes ya es ODLC. Si funciona sin agentes, ODLC es gestión por resultados, una idea vieja y ya probada en otros contextos. Lo nuevo queda en [[HACS]]: la organización humano-agente, la [[Gobernanza]] de la autonomía y la memoria. Y eso es justamente lo que no tiene evidencia.

**Para contestarla:** separar explícitamente lo heredado (ODLC como gestión por resultados, con la objeción 1 contestada) de lo nuevo (HACS como hipótesis), y no presentar la novedad de uno como respaldo del otro.

## Objeción 5: supone personas motivadas

El marco asume un humano que define objetivos, decide y valida por iniciativa propia. Es el mismo supuesto del principio 5 del Manifiesto Ágil y de las organizaciones Teal, y queda expuesto cuando el humano no es proactivo ([[Relectura del Manifiesto Ágil#El humano que no es proactivo]]).

Scrum y Kanban flaquean ante ese humano por la misma razón: dependen de rituales que hacen las personas (daily, retro, tirar del trabajo) y nada mide si el ritual cumplió su función. Cuando la gente se desengancha, el ritual sigue ocurriendo vacío y el sistema no se entera.

### Principios para tolerar al humano de mínimo esfuerzo

La idea viene de los sistemas tolerantes a fallos: no se asume que el componente es confiable, se diseña para que el sistema funcione cuando falla. Acá el humano de mínimo esfuerzo no es una desviación a corregir sino el estado para el que se diseña. Son seis principios propuestos por este vault; cada uno indica qué respaldo tiene en la literatura relevada ([[Propuestas existentes - Objeciones 5 y 6]], 2026-10-08) y qué sigue siendo hipótesis.

| # | Principio | Respaldo | Límite conocido |
|---|---|---|---|
| 1 | **Que "lo justo" alcance.** Al humano se le pide un acto de juicio chico, concreto y suficiente; la proactividad (proponer, recordar, perseguir pendientes) la ponen los agentes. | Indirecto. En un experimento de campo de 12 meses, la autogestión mejoró la experiencia solo de los empleados proactivos (Lee, con Edmondson): depender de la iniciativa deja afuera al empleado promedio. Anthropic (2026) observa que los usuarios experimentados pasan de aprobar cada acción a supervisar e intervenir; es dato del proveedor, sin revisión por pares. | Un agente que propone todo frente a un humano pasivo es el escenario clásico del sesgo de automatización (Parasuraman y Manzey, 2010). Por eso este principio no funciona solo, sin los principios 3 y 4. |
| 2 | **Que el camino barato sea el correcto, y que fingir cueste más que hacerlo bien.** Un "ok" no vale como aprobación: el humano escribe el número de la métrica, elige entre opciones o marca qué cambiaría su veredicto. | Parcial. La elección activa obligatoria subió la inscripción 28 puntos frente al opt-in (Carroll y otros, 2009). Las funciones de forzado cognitivo redujeron la sobreconfianza en la IA (Buçinca y otros, 2021, N = 199). | La elección forzada asegura que haya decisión, no que sea buena, y requiere un humano competente. El forzado cognitivo es el diseño peor valorado y el que menos beneficia a quien no disfruta pensar. Una compuerta que verifica forma se vuelve casilla tildada: la checklist quirúrgica bajó la mortalidad del 1,5 % al 0,8 % en el piloto de la OMS y no tuvo efecto significativo bajo mandato en Ontario (0,71 % contra 0,65 %, p = 0,13). Los defaults, en unidades de gobierno, mueven 1,4 puntos contra 8,7 en revistas académicas (DellaVigna y Linos, 2022). |
| 3 | **Detectar la degradación con métricas de pasividad**: aprobaciones en segundos, tasa de aprobación cercana al 100 %, cero ediciones a lo que propone el agente, entradas de [[Fase 6 - Learning]] vacías o repetidas. No se mide la motivación; se mide si cada acto humano hizo su trabajo. | Propuesto por una guía, sin validar. IMDA (*Model AI Governance Framework for Agentic AI*, v1.5, 2026) sugiere medir la supervisión con la tasa de rechazo o modificación y el tiempo de respuesta. | Sin umbrales validados. Una tasa de rechazo baja también es compatible con un agente bueno: el indicador necesita una línea de base, que da el principio 4. |
| 4 | **Inyectar fallas conocidas**: errores sembrados en la cola de revisión, para medir cuántos atrapa cada humano. Si no atrapa ninguno, su aprobación vale cero. | Práctica existente y evidencia parcial. La seguridad aeroportuaria usa *Threat Image Projection*: el equipo de rayos X proyecta amenazas ficticias y registra si el operador las detecta (p. ej. "Using threat image projection data for assessing individual screener performance", 2005, doi:10.2495/safe050411). En laboratorio, experimentar fallas de la automatización redujo la complacencia y los errores de omisión (Bahner y otros, 2008, N = 24). | El mismo estudio no redujo los errores de comisión (aceptar una recomendación equivocada), que son los más relevantes acá. Muestra chica. |
| 5 | **Degradación controlada cuando el humano no responde**: lo reversible avanza, lo irreversible se frena y escala a otra persona; redundancia de dos personas solo donde el daño lo justifica. | Propuesto por guías y regulación, sin validación comparativa. IMDA concentra la aprobación humana en puntos significativos (alto impacto, irreversible, conducta atípica) y deniega por defecto si falla la infraestructura de aprobación. El Reglamento de IA de la UE (art. 14) exige verificación por dos personas solo para identificación biométrica remota. | Ningún marco de autonomía graduada tiene validación empírica comparativa. Qué es "irreversible" lo define la matriz de [[Gobernanza]], que todavía tiene decisiones pendientes. |
| 6 | **Hacer visible, no reemplazar la gestión.** Ningún sistema arregla a quien no le importa; puede acotar el daño y volver la falla visible para que sea tema de responsabilidad, no un descubrimiento tardío. | Medido en laboratorio. Quienes se percibían responsables de justificar su estrategia verificaron más la automatización y cometieron menos errores de omisión y de comisión (Mosier, Skitka y otros, NASA, 1996). Parasuraman y Manzey (2010) concluyen que el sesgo no se previene con entrenamiento ni con instrucciones. | Simulaciones de aviación. La responsabilidad tiene que recaer sobre el proceso de verificación, no solo sobre el resultado. Las campañas de concientización no alcanzan. |

**Lo que el relevamiento no resolvió:** cómo lograr que el debrief de la [[Fase 6 - Learning]] ocurra si nadie lo convoca. Los debriefs bien conducidos mejoran el desempeño alrededor de 25 % (metaanálisis de Tannenbaum y Cerasoli, 2013, d = 0,67), pero todos los estudios suponen que alguien los conduce.

**Por qué esto diferencia a ODLC de Scrum y Kanban (hipótesis):** no supone gente motivada; mide si cada acto humano produjo efecto. Se refuta si, en un piloto, las métricas de pasividad y la tasa de fallas sembradas detectadas no se correlacionan con los errores que llegan a producción.

## Objeción 6: el Nivel 5 habla de autogestión sin definirla

"Unidades HACS adaptativas autogestionadas" ([[Modelo de madurez AI-Native]]) es vocabulario de las organizaciones Teal (Frederic Laloux, *Reinventing Organizations*, 2014). El marco lo usa sin resolver dos tensiones con esa tradición:

- **Gobernanza.** Teal reemplaza la aprobación jerárquica por el *advice process*: decide cualquiera, después de consultar a los afectados y a quienes saben. ODLC tiene una matriz de aprobaciones humanas por rol y un Sponsor que acepta o rechaza ([[Gobernanza]], [[Roles humanos]]), más cerca de una organización jerárquica orientada a resultados que de la autogestión.
- **Medición.** Teal desconfía de metas, presupuestos y pronósticos y prefiere "sentir y responder" a "predecir y controlar". ODLC gira alrededor de métricas. La salida posible es medir para aprender, no para controlar, pero hoy no está escrita.

La evidencia de Laloux también es débil como prueba: estudios de caso de organizaciones elegidas por el autor, con sesgo de supervivencia. Sirve como marco, no como demostración.

---

## Qué haría falta para que tenga sentido

1. **Una tesis central refutable.** Por ejemplo: *con agentes, a igualdad de horas humanas, definir el trabajo como objetivo con métrica y validar contra el outcome produce más objetivos validados y menos trabajo descartado que trabajar por flujo de ítems.* Los términos tienen que quedar atados a métricas instrumentadas ([[Métricas operativas]]).
2. **Un piloto que la mida, con criterio de abandono fijado antes de empezar.** Si la tesis no se cumple, se descarta la tesis, no la medición. Diseño en borrador: [[Piloto - Combinación A]].
3. **Contestar la objeción de Deming** antes de promover la métrica como centro del ciclo.

---
Relacionado: [[Preguntas abiertas]] · [[Riesgos]] · [[Comparativa con metodologías existentes]] · [[Relectura del Manifiesto Ágil]] · [[Modelo de madurez AI-Native]]
