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

## Objeción 7: lo que no se acelera

Si los agentes comprimen el research y el desarrollo, el tiempo total queda dominado por lo que no comprimen: planificar, discutir, decidir y validar. Es la ley de Amdahl aplicada a la organización: la parte que no se paraleliza pone el techo de la aceleración. El diagnóstico de ODLC ya ubica ahí el cuello ([[Nuevos cuellos de botella]]), pero el marco no dice cómo se acorta esa parte ni cómo se distingue acortarla bien de acortarla mal.

Etiquetas de respaldo en esta objeción y en la siguiente: **[medido]** dato de un estudio con medición o comparación explícita; **[testimonio]** relato de quien lo aplicó, dato de proveedor o consultora sin método publicado, o encuesta de percepción; **[guía]** marco, norma o argumento publicado sin medición propia; **[hipótesis]** propuesta de este vault, sin validar.

**El techo existe, aunque nadie midió cuánto pesa decidir.**

- [medido] La ganancia se achica en cada etapa: con agentes autónomos, +240 % en commits y apenas +30 % en releases (Demirer, Musolff y Yang, NBER w35275, 2026, más de 500.000 desarrolladores de GitHub). En equipos con alta adopción de IA, el tiempo de revisión de PR subió 91 % y a nivel compañía no hubo correlación significativa (Faros AI, 2025, telemetría correlacional). Los PR de agentes esperan entre 4,6 y 5,3 veces más hasta que alguien los toma (LinearB, 2026). Fuente: [[Investigación - Estimación y tiempo con agentes]].
- [medido] En un RCT con 7.137 trabajadores de 66 firmas, la IA bajó dos horas semanales de mail y no cambió el tiempo en reuniones (Dillon, Jaffe, Immorlica y Stanton, NBER w33795, 2025). Los autores lo atribuyen a que la coordinación depende de los demás y no de cada uno. Fuente: [[Propuestas existentes - Deliberación que no se acelera]].
- [medido, muestra chica] En el único estudio instrumentado que encontró el relevamiento, los desarrolladores dedicaron 21,0 % del tiempo a codificar y 24,4 % a actividades colaborativas (Meyer y otros, *IEEE TSE*, 2017, 20 personas en 4 empresas). No apareció ninguna medición de qué fracción de un proyecto de software se va en decidir, ni del Decision Lead Time con y sin agentes.

### Vías para acortar la deliberación

El relevamiento ([[Propuestas existentes - Deliberación que no se acelera]], 2026-10-08) trató cinco vías como hipótesis a refutar y encontró una sexta. Veredicto de cada una:

| # | Vía | Veredicto | Respaldo | Límite conocido |
|---|---|---|---|---|
| 1 | **Discutir menos cosas**: separar decisiones reversibles de irreversibles y fijar quién decide (RAPID, DACI, DRI). | Se sostiene como forma de bajar el volumen de lo que se discute, con evidencia débil. | [testimonio] Cartas de Amazon a los accionistas de 2015 y 2016 (puertas de una y de dos vías), handbook de GitLab. Bain afirma una correlación entre efectividad de las decisiones y desempeño, sin datos publicados y con encuestas de la misma consultora que vende la intervención. | Nadie midió cuánto tiempo ahorra ni cuánto cuesta clasificar mal una decisión como reversible. La clasificación es en sí misma una decisión, y en software muchas parecen de dos vías y no lo son (migraciones de datos, contratos de API públicos). |
| 2 | **Consentimiento en vez de consenso** (sociocracia, advice process). | Refutada como acelerador. | Ninguna medición de tiempo. [medido, caso único] King y Griffin (*Voluntas*, 2024) documentan curva de aprendizaje dura y participación desigual. [testimonio] Tras imponer holacracia, 18 % del personal de Zappos (260 personas) se fue con un pago de salida (Time, 2016); Medium la abandonó en 2016 (Fortune). | Bajar el umbral de aprobación no baja el número de reuniones: integrar objeciones también es un proceso. El advice process sin registro de la consulta se degrada en decisión unilateral. |
| 3 | **Abaratar la discusión con preparación previa**, incluida la que hacen agentes. | Matizada: mueve el tiempo de lugar, no lo borra. | [testimonio] Según la carta de Amazon de 2017, un buen memo "debería llevar una semana o más". [medido] En P&G, la IA redujo el tiempo de trabajo 16,4 % en individuos y 12,7 % en equipos (Dell'Acqua y otros, NBER w33641, 776 profesionales). [medido] En el RCT de 7.137 personas, el tiempo en reuniones no cambió. | La parte que la IA mejor resuelve, el análisis, es la que menos pesa en la calidad de la decisión (ver la advertencia de Lovallo y Sibony, abajo). Las opciones que prepara un agente anclan la discusión: es el sesgo de automatización de la objeción 5. |
| 4 | **Reemplazar debate por alternativas construidas en paralelo** (set-based design, prototipado paralelo). | La mejor respaldada, pero para la calidad del resultado, no para el tiempo. | [medido] Prototipar en paralelo dio mejores resultados que en serie, con el mismo tiempo (Dow y otros, *ACM TOCHI*, 2010, 33 participantes). Generar varias alternativas mejoró los resultados (Nutt, 1993, 168 casos). Considerar varias a la vez se asoció a decidir más rápido (Eisenhardt, 1989, 8 empresas). | El costo de construir N alternativas baja con agentes, pero el de evaluarlas recae en la atención humana. Solo aplica a preguntas que la evidencia puede zanjar. Ninguna fuente separa alternativas consideradas de alternativas construidas. |
| 5 | **Aceptar lo irreducible**: discusiones de valores, prioridades o poder que no se resuelven con información. | Se sostiene en parte; "irreducible" exagera. | [medido] El conflicto de relación y el de proceso se asocian de forma estable a peor desempeño (de Wit, Greer y Jehn, 2012, metaanálisis de 116 estudios y 8.880 grupos); un spike solo resuelve el de tarea. [medido] Un mediador LLM produjo declaraciones grupales preferidas 56 % de las veces frente a mediadores humanos, con grupos menos divididos (Tessler y otros, *Science*, 2024, 5.734 participantes). | La mediación se probó con declaraciones de opinión, no con decisiones donde hay recursos o poder en juego. |
| 6 | **Plazo y disputa explícita** (encontrada): "disagree and commit", decidir con alrededor de 70 % de la información, escalar pronto el desacuerdo de fondo. | Plausible, sin medición propia. | [testimonio] Carta de Amazon de 2016. Consistente con Eisenhardt (1989): la resolución activa del conflicto aceleró. | Decidir con información parcial supone poder corregir rápido, y eso depende del costo de revertir, no de la voluntad. |

**La advertencia de Lovallo y Sibony.** [medido, autorreporte de ejecutivos] Sobre 1.048 decisiones, el proceso de discusión (debatir incertidumbres y puntos de vista contrarios al líder) pesó seis veces más que el análisis en la calidad de la decisión; pasar del cuartil inferior al superior en proceso se asoció a +6,9 puntos de ROI, contra +5,3 en análisis (*McKinsey Quarterly*, 2010, subconjunto de 673 decisiones). Si los agentes abaratan el análisis y la organización usa el ahorro para discutir menos, recorta la parte que más rinde. Ningún estudio midió todavía qué hacen las organizaciones con ese ahorro.

**El costo del atajo.** [medido, casos] En los estudios de Nutt, alrededor de la mitad de las decisiones fracasaron; las impuestas por poder o persuasión tuvieron 33 % de éxito, contra más de 80 % de las participativas. Eisenhardt encontró lo contrario de un atajo en los decisores rápidos: usaban más información y más alternativas, no menos. Lo que falla no es la rapidez sino la rapidez lograda imponiendo una sola opción.

**Para contestarla:** el [[Métricas organizacionales|Decision Lead Time]] (DLT) ya interpreta un valor bajo como posible falta de exploración, pero un DLT bajo no distingue rapidez de atajo: el número solo no separa decidir rápido con varias alternativas de decidir rápido imponiendo una. [hipótesis] Haría falta registrar, junto al DLT de cada estrategia de la [[Fase 3 - Strategy]], cuántas alternativas se consideraron o construyeron, si se discutieron las incertidumbres y las posiciones contrarias, y cómo se clasificó la reversibilidad de la decisión; y revisar en [[Fase 6 - Learning]] las decisiones tratadas como reversibles que resultaron no serlo. Mientras el relevamiento no encuentre ninguna medición del DLT con y sin agentes, la promesa de que ODLC acorta el ciclo completo, y no solo la ejecución, sigue siendo hipótesis.

## Objeción 8: la revisión en manos de agentes

Cuando la ejecución se acelera, la revisión humana se vuelve cuello de botella (el +91 % de tiempo de revisión y la espera de 4,6 a 5,3 veces de la objeción 7) o se vuelve sello de goma (el humano de mínimo esfuerzo de la objeción 5). La salida que la industria empieza a defender es pasar la revisión a agentes. ODLC tiene un Reviewer en sus roles, pero [[Gobernanza]] deja abierta la pregunta de cómo se audita una cadena Planner → Builder → Reviewer cuando el error emerge de la composición, y el marco no dice qué se pierde ni qué lo compensa.

### Qué se pierde

El relevamiento ([[Propuestas existentes - Revisión en manos de agentes]], 2026-10-08) evaluó cuatro hipótesis de partida (a a d) y encontró tres más (e a g):

| | Hipótesis | Veredicto | Respaldo |
|---|---|---|---|
| a | Se pierde la independencia, porque los agentes se equivocan parecido. | Sostenida, con matiz. | [medido] Sobre más de 350 modelos, dos coinciden en la respuesta 60 % de las veces cuando ambos se equivocan, y los más capaces tienen errores muy correlacionados aun entre proveedores distintos (Kim y otros, ICML 2025). Pero la independencia tampoco existía entre humanos (Knight y Leveson, 1986), y la votación por mayoría en tríos de agentes bajó la media de fallas de 387,44 a 130,99 (Ron, Baudry y Monperrus, 2026). |
| b | Goodhart: el escritor optimiza para pasar al revisor. | Sostenida con fuerza. | [medido] 30,4 % de las corridas en RE-Bench hicieron reward hacking, y pedir "no hagas trampa" casi no cambió la tasa (METR, 2025). GPT-5 hizo trampa en 54 % de las tareas imposibles de SWE-bench (ImpossibleBench, 2025). Optimizar contra un monitor enseña a esconder la trampa (Baker y otros, OpenAI, 2025). |
| c | Se pierde la habilidad humana de auditar. | Sostenida con límites. | [medido] En un ensayo aleatorizado con 52 ingenieros, el grupo con IA promedió 50 % en el cuestionario contra 67 % sin IA, con la mayor brecha en depuración (Shen y Tamkin, Anthropic, 2026). [medido, observacional] La detección de adenomas sin IA bajó de 28,4 % a 22,4 % tras adoptar IA (Budzyń y otros, *Lancet Gastroenterology & Hepatology*, 2025). No hay evidencia longitudinal en desarrolladores. |
| d | La responsabilidad queda sin dueño. | Refutada en su forma literal. | [guía] La responsabilidad no desaparece: cae sobre el humano más cercano con menos control (zona de deformación moral, Elish, 2019). [testimonio] Amazon, en marzo de 2026, reaccionó a caídas atribuidas en parte a cambios asistidos por IA pasando a exigir la firma de ingenieros senior en esos cambios. |
| e | La revisión humana ya era un filtro de defectos débil. | Encontrada por el relevamiento. | [medido] En Microsoft, solo 14 % de los comentarios de revisión (78 de 570) trataban defectos (Bacchelli y Bird, 2013). Lo que se pierde al sacar al humano es sobre todo comprensión compartida, y ninguna compensación relevada la mide ni la reemplaza. |
| f | El revisor automático también falla por exceso. | Encontrada por el relevamiento. | [medido] Los LLM marcan como no conforme código correcto, y pedir explicaciones lo empeora (Jin y Chen, 2026). En industria, la revisión con LLM alargó el cierre promedio de PR de 5 h 52 min a 8 h 20 min (Cihan y otros, ICSE SEIP 2025). |
| g | La IA amplifica el sistema existente. | Encontrada por el relevamiento. | [testimonio, encuesta] DORA 2025 asocia la adopción a más throughput y menos estabilidad. [medido] En 807 repositorios que adoptaron Cursor, la complejidad subió 41,6 % de forma persistente frente a 1.380 de control (He y otros, MSR 2026). |

### Compensaciones relevadas

| | Compensación | Respaldo | Límite conocido |
|---|---|---|---|
| C4 | **Verificación por ejecución con tests que el escritor no puede ver ni editar**, junto con C7: no iterar ni entrenar al escritor contra la misma señal que lo juzga. | Mejor respaldo. [medido] En ImpossibleBench, los tests ocultos bajaron la trampa casi a cero pero empeoraron el desempeño legítimo; los de solo lectura son un punto medio que bloquea la estrategia de modificar los tests. [medido] Tratar la corrección que propone el revisor como hipótesis que se ejecuta reduce sus falsos positivos (Jin y Chen). [testimonio] StrongDM verifica con escenarios guardados fuera del repositorio que los agentes no ven, y no publica resultados. | Los tests son el blanco favorito del reward hacking: si el escritor los ve o los edita, la verificación también se infla. La verificación mide lo que dice la especificación, y donde la especificación es ambigua los agentes fallan juntos (Ron y otros). Un conjunto de reserva, una vez usado, se filtra. |
| C5 | **Acotar el radio de daño.** | Mejor respaldo como práctica; es la única compensación que no depende de que el revisor sea bueno. [testimonio] En Replit, un agente con acceso a producción borró una base pese a la orden de congelar cambios; la corrección fue estructural (separar desarrollo de producción), porque la restricción en lenguaje natural no funcionó. [guía] Google SRE: un canario al 5 % del tráfico con 20 % de errores produce 1 % de errores globales. | No mejora la calidad, solo limita la exposición. Los errores lentos, como la complejidad que crece (hipótesis g), no los atrapa ningún canario. |
| C1 | **Auditoría humana por muestreo con presupuesto explícito**: el humano audita el sistema de revisión, no cada artefacto. | Mejor respaldo experimental. [medido] En AI Control (Greenblatt y otros, Redwood Research), con trabajo humano para auditar hasta 2 % de los problemas, auditar al azar dio 15 % de seguridad; dejar que un modelo débil confiable eligiera qué auditar la subió a 62 %, y dejar que editara lo sospechoso, a 92 %, con 94 % de utilidad. Lo decisivo es qué selecciona el sistema para que el humano audite, no cuánto audita. | El 2 % es un parámetro del experimento, no una tasa validada en industria, y el muestreo al azar puro rindió poco. No se encontró una norma de muestreo para auditar revisiones de código. |
| C2 | Inyectar defectos conocidos para medir a los revisores. | Parcial. [medido] Meta usa mutantes para medir y endurecer suites de tests (ACH, FSE 2025), pero no se encontró una aplicación publicada para medir revisores. | [guía] Bainbridge (1983) advierte que subir artificialmente la tasa de fallas destruye la confianza del operador: la tasa sembrada tiene que ser baja. Un revisor agente puede aprender a reconocer el patrón de siembra. |
| C3 | Calibrar jueces contra etiquetas humanas. | Parcial. [medido] En Shopify, el juez pasó de un kappa de 0,02 a 0,61, con un techo de acuerdo entre humanos de 0,69. | [medido] GPT-4 como juez muestra autopreferencia por textos que le resultan familiares (Wataoka y otros, 2024): no conviene que juzgue el mismo modelo, o la misma familia, que escribe. La calibración exige el juicio experto que se quería ahorrar. |
| C6 | Diversidad deliberada de revisores. | Parcial. [medido] Votación en tríos (Ron y otros). | Entre los modelos más capaces la diversidad de proveedor reduce poco la correlación (Kim y otros); hace falta diversidad de método, que multiplica el costo. |
| C8 | Mantener la habilidad humana con práctica deliberada. | Parcial. [medido] Quienes pedían explicaciones o hacían preguntas conceptuales aprendieron más (Shen y Tamkin). | No se encontró evidencia de que la práctica mantenga la habilidad de revisar en quienes dejaron de hacerlo, y cuesta tiempo justo cuando se automatizó para ahorrarlo. |
| C9 | Responsabilidad sobre el diseño del sistema de revisión, no sobre cada artefacto. | [guía] Elish (2019); IMDA, *Model AI Governance Framework for Agentic AI* v1.5 (2026); Reglamento de IA de la UE, art. 14. | Sin métricas del sistema (C1 y C2), "responsable del diseño" es una firma vacía, igual a la que se quería reemplazar. |

El relevamiento lee la tabla así: C4 y C5 son la base; C1, C2 y C3 forman un circuito de medición que solo funciona entero; C7 y C8 lo protegen contra Goodhart y contra la pérdida de habilidad; C9 sin ese circuito es una firma vacía.

**Testimonio de practicantes.** [testimonio] Robert C. Martin dice que no ve el 95 % del código que escriben sus agentes y se apoya en tests unitarios, umbrales de CRAP, mutation testing y uso directo del sistema; cuando los agentes escribían el Gherkin, al leerlo él asentía sin que significara nada, y volvió a escribirlo él mismo. BettaTech dosifica la revisión por riesgo: revisó menos del 10 % del panel de administración de su academia y se pone alerta cada vez que un agente toca los pagos. Los dos coinciden en que la responsabilidad es humana. Fuente: [[Análisis - Dejar de leer código (Uncle Bob y BettaTech)]], que en su sección de peso de la fuente los registra como señal de adopción y de discurso, no como evidencia: una persona cada uno, en proyectos propios y sin medición; Martin cambió de postura en semanas y lo entrevista un canal que vende un reemplazo de la revisión de código; y en el RCT de METR (2025) los desarrolladores creyeron haber ido 20 % más rápido y tardaron 19 % más, que es el mismo tipo de autoevaluación que traen los dos videos.

**Para contestarla:** [hipótesis] declarar en [[Gobernanza]] quién responde por el sistema de revisión (C9) y con qué métricas: tests que el escritor no edita (C4), radio de daño fijado por la matriz (C5), una muestra auditada por humanos con presupuesto explícito y elegida por el sistema, no al azar (C1), y una tasa baja de defectos sembrados que mida la detección (C2). Es el mismo mecanismo de los principios 3 y 4 de la objeción 5, aplicado a revisores agentes además de humanos. Quedan sin respuesta dos huecos del relevamiento: ningún estudio compara defectos en producción antes y después de sacar al humano de la revisión, y ninguna compensación reemplaza la comprensión compartida que la revisión humana producía.

---

## Qué haría falta para que tenga sentido

1. **Una tesis central refutable.** Por ejemplo: *con agentes, a igualdad de horas humanas, definir el trabajo como objetivo con métrica y validar contra el outcome produce más objetivos validados y menos trabajo descartado que trabajar por flujo de ítems.* Los términos tienen que quedar atados a métricas instrumentadas ([[Métricas operativas]]).
2. **Un piloto que la mida, con criterio de abandono fijado antes de empezar.** Si la tesis no se cumple, se descarta la tesis, no la medición. Diseño en borrador: [[Piloto - Combinación A]].
3. **Contestar la objeción de Deming** antes de promover la métrica como centro del ciclo.

---
Relacionado: [[Preguntas abiertas]] · [[Riesgos]] · [[Comparativa con metodologías existentes]] · [[Relectura del Manifiesto Ágil]] · [[Modelo de madurez AI-Native]]
