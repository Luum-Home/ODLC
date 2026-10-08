---
tags: [crudo, investigacion, objeciones]
status: crudo
created: 2026-10-08
---

# Propuestas existentes: Objeciones 3 y 4

Relevamiento de lo que otras personas u organizaciones ya propusieron para dos objeciones de "Objeciones al marco" (docs/06_fundacional): la 3 (no hay ni un caso medido) y la 4 (lo nuevo es la organización humano-agente y no tiene evidencia). No incluye propuestas propias. Todas las fuentes se consultaron el 2026-10-08; cada número cita de dónde sale.

## Resumen

1. Para juntar evidencia de un marco nuevo hay métodos con trayectoria: Design Science Research (Hevner 2004, Peffers 2007), su marco de evaluación FEDS (Venable 2016) y la investigación-acción técnica (Wieringa 2012).
2. La ingeniería de software empírica ofrece guías para estudios de caso (Runeson y Höst 2009), experimentos (Wohlin et al., 2012 y 2024) y síntesis de evidencia (EBSE: Kitchenham, Dybå y Jørgensen 2004).
3. Contra el autoengaño hay dos herramientas: los registered reports, con revisión del diseño antes de los datos (ESEM/MSR + EMSE), y los kill criteria con estado y fecha (Annie Duke 2022).
4. DORA/Accelerate muestra cómo armar evidencia con encuestas a escala y psicometría, y también dónde queda corta: datos autoinformados, sin datos crudos publicados y con conflicto de interés señalado por críticos.
5. Hay una lección medida sobre autoinforme: en el RCT de METR (2025) los desarrolladores tardaron 19% más con IA y aun así creyeron haber ganado 20%. En 2026 el mismo diseño se rompió porque la gente ya no aceptaba trabajar sin IA.
6. La historia del agilismo es un antecedente que advierte: en 2008 una revisión sistemática encontró 36 estudios empíricos, con evidencia débil, años después de la adopción masiva.
7. Para la organización humano-agente, la literatura de human-autonomy teaming (NASA, National Academies 2022, revisión de 76 estudios) tiene métodos de evaluación, pero casi todo en laboratorio y en dominios no-software.
8. Las escalas de autonomía (Parasuraman 2000, Knight Institute 2025, IMDA 2026) chocan con una crítica fuerte: el Defense Science Board (2012) y Bradshaw et al. (2013) pidieron abandonar los "niveles" y pensar en interdependencia (coactive design, 2014).
9. Los datos medidos sobre humano+IA son mixtos. Hay ganancias dentro de la "frontera" (BCG 2023, P&G 2025), pero un metaanálisis de 106 experimentos dio que la combinación rinde peor que el mejor de los dos solos (g = −0,23).
10. Separar estructura de proceso tiene un antecedente explícito en Team Topologies (2019, extendida a agentes en 2026), aunque su evidencia son casos autoinformados. Para la objeción 4 no aparece ninguna propuesta que ya haya medido una organización humano-agente de software separando modelo organizacional y proceso.

---

## Objeción 3: cómo un marco nuevo junta evidencia de que funciona

### 3.1 DORA / Accelerate: encuestas a escala con validación psicométrica

- **Quién y dónde.** Nicole Forsgren, Jez Humble y Gene Kim; libro *Accelerate* (2018) y los informes anuales State of DevOps (dora.dev/research, informes 2014–2025). Desde 2018 el programa sigue en Google Cloud.
- **Qué resuelve.** Cómo sostener que unas prácticas (entrega continua, cultura, arquitectura) predicen un desempeño de entrega y organizacional sin poder hacer experimentos en empresas reales.
- **Cómo construye la evidencia.** Según el investigador principal actual, Derek DeBellis (newsletter de DX, 2024-05-17): investigación cualitativa previa, encuestas piloteadas, análisis factorial exploratorio y confirmatorio, PLS en 2022 y un marco bayesiano desde 2023, más chequeos de sensibilidad con cuatro métodos de clustering. *Accelerate* se apoya en más de 23.000 respuestas a lo largo de cuatro años (resumen de getAbstract) y en más de 2.000 organizaciones (cynefin.io). El informe 2025, *State of AI-assisted Software Development*, suma casi 5.000 respuestas y más de 100 horas de datos cualitativos (blog de Google, 2025-09-23).
- **Dónde se aplicó.** Industria del software a escala global. Las cuatro métricas DORA se volvieron estándar de facto.
- **Evidencia de que funciona.** Medido: consistencia de los constructos y asociaciones estadísticas entre prácticas y resultados en datos de encuesta. No medido: causalidad. Los datos son autoinformados. El propio informe 2025 reporta que más del 80% *dice* que la IA mejoró su productividad (blog de Google), que es una percepción y no una medición (ver 3.10).
- **Críticas.** Junade Ali (Hackernoon, 2024-01-03): no se publican datos crudos, las preguntas subjetivas inducen correlaciones por sesgo de respuesta y el equipo trabajó para empresas (Puppet, Google Cloud) que se benefician de la recomendación de desplegar más rápido. DeBellis reconoce el problema de tratar datos ordinales como continuos.
- **Combinabilidad.** Complementa a 3.5 y 3.10 (la encuesta da amplitud y el experimento da causalidad). Su modo de evidencia choca con el hallazgo de 3.10 sobre la brecha entre percepción y medición.

### 3.2 Design Science Research (DSR) y su metodología DSRM

- **Quién y dónde.** Alan Hevner, Salvatore March, Jinsoo Park y Sudha Ram, "Design Science in Information Systems Research", *MIS Quarterly* 28(1):75–105, marzo de 2004: un marco conceptual y guías para ejecutar y evaluar investigación de diseño, ilustrado con tres ejemplos (ficha de la Universidad de Arizona). Ken Peffers, Tuure Tuunanen, Marcus Rothenberger y Samir Chatterjee, "A Design Science Research Methodology for Information Systems Research", *Journal of Management Information Systems* 24(3), 2007: seis actividades (identificar el problema, definir objetivos de la solución, diseñar y desarrollar, demostrar, evaluar y comunicar).
- **Qué resuelve.** Cómo hacer investigación cuyo producto es un artefacto (constructos, modelos, métodos o instancias), y no solo una explicación, con reglas para evaluarlo. Un marco de trabajo como ODLC entra en la categoría "método".
- **Dónde se aplicó.** Sistemas de información; es base de muchas tesis de ingeniería.
- **Evidencia de que funciona.** El artículo de Peffers et al. "demuestra" la DSRM aplicándola de forma retroactiva a cuatro estudios ya publicados (texto del PDF, sección "Demonstration in Four Case Studies"). Eso muestra que el método se puede usar, pero no que produzca mejores artefactos. La actividad 5 pide comparar los objetivos de la solución con resultados observados al usar el artefacto. No se encontraron mediciones de que la DSR mejore los resultados frente a otros enfoques.
- **Críticas o fallas.** La demostración es autoevaluación retroactiva. El método permite que quien diseña el artefacto lo evalúe, el mismo problema que la objeción 3 le marca a ODLC.
- **Combinabilidad.** Es el paraguas natural de 3.3 (cómo evaluar) y de 3.4 (evaluar en un contexto real).

### 3.3 FEDS: Framework for Evaluation in Design Science

- **Quién y dónde.** John Venable, Jan Pries-Heje y Richard Baskerville, *European Journal of Information Systems* 25(1):77–89, enero de 2016.
- **Qué resuelve.** Cuándo, cómo y qué evaluar dentro de un proyecto DSR. Ordena los episodios de evaluación en dos ejes: formativa o sumativa, y artificial (laboratorio, simulación) o naturalista (uso real).
- **Dónde se aplicó.** Proyectos DSR en sistemas de información; existe un tutorial FEDS2 (repositorio de Curtin).
- **Evidencia.** El artículo dice aportar evidencia de su utilidad (resumen en IDEAS/RePEc). No se encontró una medición comparativa.
- **Críticas.** No se encontraron críticas publicadas específicas en lo consultado.
- **Combinabilidad.** Complementa a 3.2. El eje artificial/naturalista ordena cuándo conviene un experimento controlado (3.5) y cuándo un piloto real (3.4, 3.7).

### 3.4 Technical Action Research (TAR)

- **Quién y dónde.** Roel Wieringa, tutorial "Designing technical action research and generalizing from real-world cases", CAiSE 2012 (Gdańsk). El método se cita como Wieringa y Moralı (2012).
- **Qué resuelve.** Cómo validar un artefacto nuevo usándolo para resolver un problema real de un cliente, cuando quien investiga es también quien lo creó, y cómo generalizar desde uno o pocos casos mediante "inferencia arquitectónica" (razonar sobre los mecanismos del caso y no por muestreo estadístico).
- **Dónde se aplicó.** Ingeniería de requisitos, seguridad e ingeniería de sistemas de información.
- **Evidencia.** Es un aporte metodológico; la página de la Universidad de Twente no reporta mediciones de su efectividad.
- **Críticas.** El doble rol de autor y evaluador sesga el resultado. La generalización por mecanismo es más débil que la estadística.
- **Combinabilidad.** Complementa a 3.2 y 3.3. Con 3.7 y 3.8, el riesgo del doble rol se puede compensar fijando de antemano el protocolo y el criterio de abandono.

### 3.5 Estudios de caso y experimentos en ingeniería de software (Runeson y Höst; Wohlin et al.)

- **Quién y dónde.** Per Runeson y Martin Höst, "Guidelines for conducting and reporting case study research in software engineering", *Empirical Software Engineering* 14(2):131–164, 2009; libro ampliado en 2012. Claes Wohlin, Per Runeson, Martin Höst, Magnus Ohlsson, Björn Regnell y Anders Wesslén, *Experimentation in Software Engineering*, Springer, 2.ª ed. 2012. La edición 2024 agrega capítulos sobre elección del diseño de investigación, encuestas, A/B testing, replicación y ciencia abierta.
- **Qué resuelve.** Cómo diseñar, ejecutar y reportar un estudio de caso (fenómeno en su contexto real, poco control) frente a un experimento (control y aleatorización, menos realismo), con listas de chequeo para quien investiga y para quien lee.
- **Dónde se aplicó.** Es referencia estándar en la investigación empírica de software. Las listas de Runeson y Höst se evaluaron con doctorandos y miembros del International Software Engineering Research Network (Lund University).
- **Evidencia.** El aporte es metodológico; no hay medición de que su uso mejore las conclusiones.
- **Críticas.** Los propios autores no dan criterios absolutos de qué es un buen estudio de caso.
- **Combinabilidad.** Es la caja de herramientas para ejecutar 3.2 y 3.4. Se complementa con 3.6, porque varios estudios de caso bien reportados son la materia prima de una síntesis.

### 3.6 Evidence-Based Software Engineering (EBSE) y la lección del agilismo

- **Quién y dónde.** Barbara Kitchenham, Tore Dybå y Magne Jørgensen, "Evidence-based Software Engineering", ICSE 2004, pp. 273–281. (ficha en la bibliografía EBSE de Durham).
- **Qué resuelve.** Trasladar la medicina basada en evidencia al software: preguntas formuladas, búsqueda sistemática, evaluación crítica de la evidencia e integración con la práctica. Advierte que el software tiene dos factores propios, la habilidad de quien ejecuta y el ciclo de vida, que dificultan comparar métodos.
- **Dónde se aplicó.** Revisiones sistemáticas en ingeniería de software. El caso más útil para ODLC es Dybå y Dingsøyr, "Empirical studies of agile software development: A systematic review", *Information and Software Technology* 50(9–10):833–859, 2008. De 1.996 estudios identificados, solo 36 eran empíricos, y la conclusión principal fue que hacían falta más y mejores estudios con una agenda común (ficha en SINTEF; resumen en la bibliografía EBSE de Durham).
- **Evidencia.** El aporte de EBSE es metodológico. La revisión de 2008 es un dato medido sobre el estado de la evidencia de un marco ya adoptado masivamente.
- **Críticas o fallas que enseñan.** El agilismo se difundió durante años sin evidencia empírica fuerte. Si la evidencia llega después de la adopción, el marco se discute por testimonio. Los autores de EBSE ya advertían en 2004 que faltaba la infraestructura para practicarla.
- **Combinabilidad.** Complementa a 3.5 (sintetiza sus resultados). Junto con 3.9 (CEBMa) comparte la raíz en la medicina basada en evidencia.

### 3.7 Registered reports (pre-registro con revisión antes de los datos)

- **Quién y dónde.** Tracks de Registered Reports de ESEM (2021–2024 en conf.researchr.org) y MSR (2025–2027), con la Etapa 2 publicada en la revista *Empirical Software Engineering*.
- **Qué resuelve.** Evita el HARKing (formular la hipótesis después de ver los resultados) y da feedback sobre el diseño antes de ejecutarlo. En ESEM 2024: la Etapa 1 es un plan de hasta 6 páginas que se revisa; los estudios confirmatorios reciben aceptación en principio y los exploratorios una aceptación de continuidad; los desvíos del protocolo se declaran y se justifican en la Etapa 2. La convocatoria lo dice así: "The results may also be negative!" (ESEM 2024 RR track).
- **Dónde se aplicó.** Psicología, y en software desde los tracks mencionados. MSR 2026 tuvo presentaciones de RR.
- **Evidencia.** Hay una medición en otra disciplina: Scheel, Schijen y Lakens (*Advances in Methods and Practices in Psychological Science*, abril de 2021) compararon 71 registered reports con 152 estudios estándar y encontraron 44% de resultados positivos contra 96%. Los autores aclaran que la comparación es correlacional y no prueba causalidad (TU Eindhoven).
- **Críticas.** Pre-registrar no garantiza que el diseño sea bueno. Los estudios exploratorios entran con aceptación más débil.
- **Combinabilidad.** Complementa a 3.4 y 3.8: el protocolo y el criterio de abandono se fijan antes. No hay contradicciones evidentes con el resto.

### 3.8 Kill criteria: estado + fecha, fijados de antemano

- **Quién y dónde.** Annie Duke, *Quit: The Power of Knowing When to Walk Away*, 4 de octubre de 2022. Resumen de Elliot Robia (Substack, 2023-07-17).
- **Qué resuelve.** La escalada de compromiso. Un criterio de abandono tiene que combinar un estado medible y una fecha, y se decide antes de empezar, cuando las emociones del momento todavía no pesan. Ejemplo citado: en mParticle, si no se lograba una reunión con un ejecutivo (estado) antes de la próxima reunión (fecha), el negocio se abandonaba.
- **Dónde se aplicó.** Decisiones empresariales y de producto, según testimonios del libro.
- **Evidencia.** Testimonial y anecdótica, con apoyo en la literatura de sesgos cognitivos. No se encontró un estudio que mida el efecto de los kill criteria.
- **Críticas.** Si el estado está mal elegido, se mata algo prometedor o se mantiene algo malo. El problema de Goodhart (objeción 1) aplica también al criterio de abandono.
- **Combinabilidad.** Complementa a 3.7 (el registered report fija hipótesis y análisis; el kill criterion fija la decisión). Es coherente con el bucle hipótesis-experimento de 3.9.

### 3.9 Evidence-Based Management: dos propuestas con el mismo nombre

- **CEBMa (Barends y Rousseau).** Eric Barends y Denise M. Rousseau, *Evidence-Based Management: How to Use Evidence to Make Better Organizational Decisions*, Kogan Page, 2018. Propone decidir integrando, después de evaluarlas críticamente, cuatro fuentes: literatura científica, datos de la organización, experiencia profesional y valores de los afectados. Origen declarado: medicina, década de 1990 (cebma.org).
- **Scrum.org EBM (Schwaber).** *Evidence-Based Management Guide* (Ken Schwaber / Scrum.org; versión 2020 en la copia curada por Martin Hinshelwood). Define cuatro Key Value Areas (Current Value, Unrealized Value, Time-to-Market, Ability to Innovate), metas en tres niveles (estratégica, intermedias y tácticas inmediatas) y un bucle de hipótesis, experimento, inspección y adaptación.
- **Qué resuelven.** CEBMa: cómo decide un gerente con evidencia de calidad desigual. Scrum.org: cómo medir valor y avanzar hacia metas bajo incertidumbre. Este último se parece mucho a la Fase 1 y la Fase 6 de ODLC.
- **Dónde se aplicaron.** CEBMa en formación gerencial y consultoría. Scrum.org EBM en la comunidad Scrum, con certificación PAL-EBM.
- **Evidencia.** La guía de Scrum.org no cita investigación empírica ni datos de efectividad (lectura de la guía 2020). No se encontró una medición de que aplicar EBM de CEBMa mejore resultados. El marco de evidencia no tiene, a su vez, evidencia medida sobre sí mismo.
- **Críticas.** Scrum.org EBM usa la palabra "evidencia" sin el rigor de evaluación de la fuente que exige CEBMa.
- **Combinabilidad.** CEBMa complementa a 3.6 (misma raíz). Scrum.org EBM es casi un antecedente directo de la parte heredada de ODLC: refuerza la objeción 4 en vez de contestarla.

### 3.10 RCT de campo sobre productividad con IA (METR) y la falla de su propio diseño

- **Quién y dónde.** METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity" (blog, 2025-07-10) y "We are Changing our Developer Productivity Experiment Design" (2026-02-24).
- **Qué resuelve.** Medir causalmente el efecto de herramientas de IA en trabajo real, sin depender del autoinforme.
- **Diseño y datos (2025).** 16 desarrolladores experimentados de repositorios grandes y 246 issues reales asignados al azar a "con IA" o "sin IA". Con IA tardaron 19% más. Antes pronosticaban una aceleración del 24% y, después de la tarea, todavía creían haber ganado un 20%.
- **Cohorte 2025-26 y falla.** 57 desarrolladores, 143 repositorios y más de 800 tareas. La aceleración estimada fue de −18% (IC −38% a +9%) entre los desarrolladores originales y de −4% (IC −15% a +9%) entre los nuevos. METR documentó sesgos de selección: más gente se negó a participar porque no quería trabajar sin IA, y entre 30% y 50% evitaba enviar tareas que no quería hacer sin IA. Como respuesta propone aleatorizar por desarrollador y no por tarea, usar tareas fijas, datos observacionales y estudios de uso del tiempo.
- **Evidencia.** Es dato medido con intervalos de confianza. Los propios autores limitan cómo generalizarlo.
- **Críticas.** Muestra chica en 2025. En 2026 el grupo de control se volvió difícil de reclutar, lo que sesga la estimación.
- **Qué enseña para la objeción 3.** Hay una brecha medida entre percepción y resultado en el mismo dominio de ODLC, y un piloto con grupo "sin agentes" puede volverse irreclutable cuando la práctica ya se adoptó.
- **Combinabilidad.** Contradice el uso del autoinforme como evidencia principal (3.1). Complementa a 3.5 (es un experimento de campo) y a 3.7 (podría pre-registrarse).

---

## Objeción 4: modelar y evaluar equipos humano-agente separando modelo organizacional y proceso

### 4.1 Human-Autonomy Teaming (HAT) de NASA Ames

- **Quién y dónde.** Summer Brandt, Joel Lachter, Ricky Russell y R. Jay Shively, "A Human-Autonomy Teaming Approach for a Flight-Following Task" (NASA NTRS, julio de 2017). Es parte del programa HAT de NASA Ames, que busca una relación de cooperación y trabajo en equipo entre operador y automatización, en lugar de pura supervisión (resumen NTRS).
- **Qué resuelve.** Diseñar automatización que coopere con el operador y no solo ejecute, y evaluarla contra una condición sin HAT.
- **Dónde se aplicó.** Estaciones terrestres de seguimiento de vuelos.
- **Evidencia.** Estudio con participantes y dos condiciones (con y sin HAT). Los usuarios prefirieron la estación con HAT y reportaron conciencia situacional suficiente con menos carga (resumen NTRS). Son medidas de preferencia y carga en simulación, no de desempeño organizacional.
- **Críticas.** Laboratorio o simulación, tarea acotada y dominio aeronáutico.
- **Combinabilidad.** Complementa a 4.3 (forma parte de esa literatura) y a 4.6 (comparte el foco en transparencia).

### 4.2 National Academies: *Human-AI Teaming: State-of-the-Art and Research Needs* (2022)

- **Quién y dónde.** Comité presidido por Mica Endsley; National Academies of Sciences, Engineering, and Medicine, 2022. Patrocinio del Departamento de Defensa, NASA y organizaciones sin fines de lucro (página de la publicación).
- **Qué resuelve.** Un estado del arte y una agenda de investigación para equipos humano-IA, con foco en la Fuerza Aérea.
- **Evidencia.** Es una revisión experta. Concluye que la IA seguirá siendo inadecuada para operar sola en muchas situaciones complejas y nuevas, y que va a tener que ser gestionada con cuidado por humanos.
- **Críticas o límites.** Excluyó explícitamente la interacción humano-robot y las dimensiones de software; el foco es militar.
- **Combinabilidad.** Complementa a 4.3 y 4.6. Respalda la premisa de "Human Governance" de HACS, pero como opinión experta y no como medición.

### 4.3 Revisión empírica de la literatura HAT (Schelble, Barron, McNeese y O'Neill)

- **Quién y dónde.** Beau Schelble, Amy Barron, Nathan McNeese y Thomas O'Neill, "Human–Autonomy Teaming: A Review and Analysis of the Empirical Literature" (registro de Clemson, 2020; publicado en *Human Factors*).
- **Qué resuelve.** Sintetiza qué se sabe empíricamente sobre equipos humano-autonomía. Incluye 76 artículos. Las variables independientes estudiadas son características del agente, composición del equipo, características de la tarea, diferencias individuales, entrenamiento y comunicación.
- **Evidencia.** Es una síntesis de estudios medidos. Hay hallazgos consistentes en algunas áreas, pero el vacío principal son los mecanismos que conectan entradas del equipo con resultados.
- **Críticas.** La base empírica es mayormente de laboratorio. Un estudio relacionado de la misma red, en *Human Factors* (2021), usa el paradigma Wizard of Oz: un humano simula al agente.
- **Combinabilidad.** El modelo de entrada, proceso y resultado de equipos que usa esta literatura separa composición (estructura) de interacción (proceso), justo la separación que pide la objeción 4. Complementa a 4.12 (metaanálisis de desempeño).

### 4.4 Tipos y niveles de automatización (Parasuraman, Sheridan y Wickens, 2000)

- **Quién y dónde.** "A model for types and levels of human interaction with automation", *IEEE Transactions on Systems, Man, and Cybernetics, Part A*, mayo de 2000.
- **Qué resuelve.** Decide qué automatizar y cuánto, separando cuatro funciones (adquisición de información, análisis, decisión y selección de acción, implementación) y un continuo de niveles dentro de cada una.
- **Dónde se aplicó.** Aviación, control de tráfico aéreo e industria de procesos. Es la referencia clásica de los "niveles".
- **Evidencia.** Es un modelo conceptual muy usado. Lo consultado no incluye una validación medida del modelo.
- **Críticas.** Ver 4.5.
- **Combinabilidad.** Es la base de 4.7 y 4.8. Choca con 4.5.

### 4.5 Contra los "niveles de autonomía": Defense Science Board (2012) y Bradshaw et al. (2013)

- **Quién y dónde.** Defense Science Board Task Force on the Role of Autonomy in DoD Systems, junio de 2012, copresidido por Robin Murphy y James Shields (presentación de Murphy alojada por National Academies; cobertura de Lawfare del 2012-09-12). Jeffrey Bradshaw, Robert Hoffman, Matthew Johnson y David Woods, "The Seven Deadly Myths of 'Autonomous Systems'", *IEEE Intelligent Systems*, 2013.
- **Qué propone.** El DSB recomienda abandonar el esfuerzo de definir niveles de autonomía y reemplazarlo por un marco de referencia que muestre cómo la autonomía apoya capacidades concretas, qué responsabilidades cognitivas se delegan al humano o a la máquina, y qué compromisos de diseño quedan a la vista. Según la diapositiva de recomendaciones, no hay sistemas totalmente autónomos, igual que no hay soldados totalmente autónomos (Lawfare). Bradshaw et al. cuentan entre sus mitos que la autonomía es unidimensional, que existen niveles claramente separados y que la autonomía es un componente que se enchufa.
- **Dónde se aplicó.** Doctrina de autonomía en defensa de EE. UU.
- **Evidencia.** Opinión experta fundamentada en experiencia operativa (falta de confianza de operadores en sistemas desplegados con apuro). No es una medición.
- **Por qué importa (propuesta que "fracasó").** Los niveles de autonomía fueron una propuesta dominante que un comité técnico pidió abandonar por contraproducente, porque ponían el foco en la máquina y no en la colaboración. Eso pega directo en el Modelo de madurez AI-Native y en la matriz de Gobernanza de HACS.
- **Combinabilidad.** Contradice a 4.4 y 4.7 y, en parte, a 4.8. Complementa a 4.6, que es la alternativa constructiva del mismo grupo.

### 4.6 Coactive design: diseñar para la interdependencia

- **Quién y dónde.** Matthew Johnson, Jeffrey Bradshaw, Paul Feltovich, Catholijn Jonker, M. Birna van Riemsdijk y Maarten Sierhuis, "Coactive Design: Designing Support for Interdependence in Joint Activity", *Journal of Human-Robot Interaction* 3(1), 2014 (OpenAlex).
- **Qué resuelve.** En vez de asignar niveles, modela las interdependencias entre humano y agente en cada tarea y diseña tres propiedades: observabilidad, predictibilidad y dirigibilidad.
- **Dónde se aplicó.** DARPA Virtual Robotics Challenge, con 26 equipos de ocho países en tareas de rescate ante desastres (resumen del artículo).
- **Evidencia.** El artículo demuestra el método en esa competencia. Lo consultado no incluye una comparación controlada contra diseño por niveles.
- **Críticas.** Viene de robótica y el análisis de interdependencias es costoso.
- **Combinabilidad.** Complementa a 4.5, 4.1 y 4.13: la interdependencia entre equipos es también el eje de las interaction modes de Team Topologies. Contradice a 4.4 y 4.7 como forma principal de modelar.

### 4.7 Niveles de autonomía para agentes de IA (Knight First Amendment Institute)

- **Quién y dónde.** Kevin Feng, David McDonald y Amy Zhang, "Levels of Autonomy for AI Agents", Knight First Amendment Institute at Columbia University, 2025-07-28.
- **Qué resuelve.** Separa la autonomía, como decisión de diseño, de la capacidad del modelo. Define cinco niveles por el rol del usuario: operador, colaborador, consultor, aprobador y observador. Propone "certificados de autonomía" emitidos por terceros y "evaluaciones asistidas" (repetir la tarea aumentando la participación del usuario hasta alcanzar un umbral de éxito).
- **Dónde se aplicó.** Lo cita la IMDA en su marco (4.8).
- **Evidencia.** No presenta datos empíricos que validen el marco (lectura del artículo).
- **Críticas.** Le cabe la crítica de 4.5: es una escala unidimensional.
- **Combinabilidad.** Complementa a 4.8, que lo adopta, y a 4.9. Contradice a 4.5. La separación entre autonomía y capacidad es compatible con 4.6.

### 4.8 IMDA: Model AI Governance Framework for Agentic AI (Singapur)

- **Quién y dónde.** Infocomm Media Development Authority (IMDA), Singapur. Lanzado el 22 de enero de 2026 en Davos (comunicado de IMDA). Versión 1.5 publicada el 20 de mayo de 2026 (PDF).
- **Qué resuelve.** Gobernanza de agentes para organizaciones que los despliegan, en cuatro dimensiones: acotar los riesgos de entrada, hacer a los humanos responsables de forma significativa, controles técnicos y procesos, y responsabilidad del usuario final. Pide definir puntos de control que requieran aprobación humana: acciones de alto impacto, irreversibles (borrar datos, enviar comunicaciones, pagar), comportamiento atípico o fuera de alcance, y límites definidos por el usuario. Pide además auditar que las aprobaciones humanas sigan siendo efectivas, por el sesgo de automatización. Describe modos de interacción humano-agente y remite al marco del Knight Institute.
- **Dónde se aplicó.** La versión 1.5 dice incorporar feedback de más de 60 empresas desde la 1.0 e incluye casos de estudio (Google con el Gobierno de Singapur, OCBC, MSD, PwC, Tencent, Workday y otros, además de un caso propio sobre OpenClaw publicado en mayo de 2026).
- **Evidencia.** Casos aportados por las organizaciones, sin grupo de comparación. El documento se presenta como "living document" y abre una convocatoria a más casos (Anexo B). Reconoce que hacen falta nuevos enfoques de testing para evaluar agentes.
- **Críticas.** Es voluntario. No mide si los puntos de control reducen incidentes. Hereda la escala de 4.7.
- **Combinabilidad.** Complementa a 4.9 (riesgos técnicos) y a 4.7. Tensión parcial con 4.5. Con 3.7 y 3.8 se podría convertir en hipótesis medibles (por ejemplo, la tasa de aprobaciones efectivas).

### 4.9 OWASP Top 10 for Agentic Applications (2026)

- **Quién y dónde.** OWASP GenAI Security Project, Agentic Security Initiative; publicado el 2025-12-09/10 (comunicado de OWASP). Participaron más de 100 investigadores y profesionales, con revisión de un Expert Review Board.
- **Qué resuelve.** Cataloga riesgos de seguridad propios de agentes que planifican, tienen memoria, usan herramientas y actúan con autoridad delegada, de ASI01 (secuestro de objetivo) a ASI10 (agentes rebeldes). Incluye ASI09 (explotación de la confianza humano-agente: el agente aprovecha el antropomorfismo y el sesgo de autoridad para que el humano apruebe errores, por ejemplo un pago fraudulento), según el resumen de Giskard (diciembre de 2025).
- **Dónde se aplicó.** Como referencia de seguridad. Hay mapeos cruzados con otros estándares, como AIUC-1.
- **Evidencia.** Según el comunicado, refleja ataques reales ya observados en empresas. Es una taxonomía de riesgos, no una evaluación de un modelo organizacional.
- **Críticas.** Cubre seguridad, no desempeño ni organización.
- **Combinabilidad.** Complementa a 4.8. ASI09 conecta con 4.10 y 4.12 (la confianza excesiva baja el desempeño fuera de la frontera).

### 4.10 "Frontera irregular", centauros y cyborgs (Harvard/BCG, Mollick)

- **Quién y dónde.** Fabrizio Dell'Acqua, Edward McFowland III, Ethan Mollick y otros, "Navigating the Jagged Technological Frontier" (HBS Working Paper, 2023). Resumen del propio Mollick, "Centaurs and Cyborgs on the Jagged Frontier" (One Useful Thing). Libro de Mollick, *Co-Intelligence: Living and Working with AI* (abril de 2024), con cuatro reglas: invitar siempre a la IA, ser el humano en el loop, tratarla como una persona diciéndole qué persona es, y asumir que es la peor IA que se va a usar (reseña de AMT Lab, 2025-03-28).
- **Qué resuelve.** Describe en qué tareas la IA ayuda y en cuáles perjudica, y dos patrones de trabajo: centauros (división estratégica de tareas entre humano e IA) y cyborgs (integración fina, ida y vuelta continua).
- **Dónde se aplicó.** 758 consultores de BCG (7% de la fuerza de consultoría) en 18 tareas realistas.
- **Evidencia (medida, con asignación aleatoria).** Dentro de la frontera, con GPT-4 completaron 12,2% más tareas, 25,1% más rápido y con 40% más calidad. Los de menor desempeño inicial mejoraron 43%. En una tarea diseñada fuera de la frontera, quienes trabajaron sin IA acertaron 84% de las veces y quienes usaron IA entre 60% y 70% (blog de Mollick). Los arquetipos centauro y cyborg son una tipología cualitativa; el libro se apoya más en ejemplos que en datos nuevos.
- **Críticas.** Tareas de un día, en un solo tipo de organización, con un modelo de 2023. "Centauro" y "cyborg" describen individuos, no organizaciones.
- **Combinabilidad.** Complementa a 4.11 y 4.12. Muestra que el efecto depende de la tarea, lo que apoya la idea de 4.6 de modelar por tarea y no por nivel global.

### 4.11 "The Cybernetic Teammate" (P&G)

- **Quién y dónde.** Fabrizio Dell'Acqua, Charles Ayoubi, Hila Lifshitz, Raffaella Sadun, Ethan Mollick y otros; NBER Working Paper 33641 (abril de 2025).
- **Qué resuelve.** Si la IA cambia el trabajo en equipo. El diseño de 2×2 cruza individuo o equipo con IA o sin IA, en desafíos reales de desarrollo de producto.
- **Dónde se aplicó.** 776 profesionales de Procter & Gamble en Europa y EE. UU.
- **Evidencia (medida, pre-registrada en el registro de la AEA).** Individuos con IA igualaron el desempeño de equipos sin IA. Con IA, las soluciones quedaron más balanceadas entre lo técnico y lo comercial, sin importar la función de quien las proponía. Las respuestas emocionales autoinformadas fueron más positivas.
- **Críticas.** Talleres de un día y agentes conversacionales, no autónomos. El efecto emocional es autoinformado.
- **Combinabilidad.** Es el antecedente metodológico más cercano a lo que pide la objeción 4, porque separa composición del equipo (estructura) de presencia de IA en un experimento factorial. Complementa a 4.10 y a 3.7, porque está pre-registrado.

### 4.12 Metaanálisis: cuándo sirve combinar humanos e IA (Vaccaro, Almaatouq y Malone)

- **Quién y dónde.** Michelle Vaccaro, Abdullah Almaatouq y Thomas Malone (MIT), "When combinations of humans and AI are useful: A systematic review and meta-analysis", *Nature Human Behaviour* 8(12):2293–2303, diciembre de 2024.
- **Qué resuelve.** Cuándo un sistema humano+IA rinde más que el mejor de los dos por separado.
- **Dónde se aplicó.** Revisión sistemática de 106 estudios experimentales y 370 tamaños de efecto, publicados entre enero de 2020 y junio de 2023.
- **Evidencia (medida).** En promedio, las combinaciones rindieron peor que el mejor de humanos o IA solos (g de Hedges = −0,23). En tareas de decisión hubo pérdidas y en tareas de creación de contenido, ganancias. Cuando el humano solo superaba a la IA sola, la combinación ganaba; cuando la IA era mejor, la combinación perdía (IDEAS/RePEc).
- **Críticas.** Los autores reconocen posible sesgo de publicación y heterogeneidad de diseños. Son experimentos de tareas cortas, no equipos organizacionales.
- **Combinabilidad.** Matiza a 4.10 y 4.11: no las contradice, pero muestra que la sinergia es rara. Da un criterio medible para evaluar cualquier unidad humano-agente: compararla contra el mejor de sus componentes solos, no solo contra el humano solo.

### 4.13 Team Topologies: estructura de equipos separada del proceso

- **Quién y dónde.** Matthew Skelton y Manuel Pais, *Team Topologies: Organizing Business and Technology Teams for Fast Flow*, IT Revolution, 2019 (resumen de Shortform, 2023-01-31). Skelton, "Team Topologies as the 'Infrastructure for Agency' with AI", QCon London, 2026-03-31 (InfoQ).
- **Qué resuelve.** Modela la organización con cuatro tipos de equipo (stream-aligned, platform, enabling y complicated-subsystem) y tres modos de interacción (colaboración, X-as-a-Service y facilitación), con la carga cognitiva y la ley de Conway como criterios de diseño. No prescribe ceremonias ni proceso, y por eso se combina con Scrum, Kanban u otros. En 2026 Skelton propone que esos principios sirvan como infraestructura de "agencia acotada" para agentes de IA, con autoridad delegada restringida por reglas y guardas.
- **Dónde se aplicó.** Casos de la comunidad: Footasylum pasó de 6 releases por año a más de 1.250 despliegues por semana; Improbable redujo 30 veces el MTTR y 5 veces los incidentes mayores (IT Revolution, Leah Brown, 2024-09-03).
- **Evidencia.** Los casos son autoinformados por las empresas o el ecosistema del libro, sin control. Hay un test académico relacionado: Alves, Pérez, Díaz, López-Fernández, Pais, Kon y Rocha (arXiv 2302.00033, enero de 2023) operacionalizaron una teoría de estructuras de equipos DevOps, derivaron 34 hipótesis y testearon 11. La extensión a agentes (2026) es una propuesta sin datos propios; el "80% de firmas sin beneficio tangible" que cita InfoQ no tiene fuente primaria en la nota.
- **Críticas.** Sesgo de selección en los casos publicados y conflicto de interés (casos promovidos por el ecosistema comercial del marco).
- **Combinabilidad.** Complementa a 4.6 (interdependencia y modos de interacción) y a 4.3 (estructura frente a interacción). Es el antecedente directo de "separar modelo organizacional de proceso". Independiente de 3.x en método, pero sus casos tienen el mismo problema de evidencia que la objeción 3.

### 4.14 Microsoft Work Trend Index 2025: "Frontier Firm" y human-agent ratio

- **Quién y dónde.** Microsoft, *2025 Work Trend Index*, presentado por Jared Spataro (blog de Microsoft, 2025-04-23).
- **Qué propone.** La "Frontier Firm", organizada alrededor de equipos humano-agente con un rol de "agent boss" para cada persona, y una métrica nueva, el *human-agent ratio*: cuántos agentes para qué tareas y cuántos humanos para guiarlos.
- **Evidencia.** Encuesta global, telemetría de Microsoft 365 y datos de LinkedIn. Los porcentajes citados (82% de líderes que dicen que es un año clave, 71% de trabajadores de Frontier Firms que dicen que su empresa prospera) son autoinforme. En el blog no figuran el tamaño de la muestra ni los países.
- **Críticas.** Lo publica un proveedor que vende la tecnología. El ratio no está definido operativamente.
- **Combinabilidad.** El "human-agent ratio" es una variable de composición de equipo que se podría poner a prueba con diseños como 4.11. Su base de evidencia choca con la lección de 3.10.

---

## Tabla de combinabilidad

Relación: **C** = se complementan, **X** = se contradicen, **I** = independientes. Se listan los pares con relación relevante; el resto se considera independiente.

| Par | Relación | Motivo |
|---|---|---|
| 3.2 DSR × 3.3 FEDS | C | FEDS es el "cómo evaluar" dentro de la DSRM. |
| 3.2 DSR × 3.4 TAR | C | TAR es una forma naturalista de la actividad "evaluación". |
| 3.4 TAR × 3.7 Registered reports | C | El pre-registro compensa el doble rol de autor y evaluador. |
| 3.7 Registered reports × 3.8 Kill criteria | C | Uno fija hipótesis y análisis; el otro, la decisión de abandono. |
| 3.5 Casos/experimentos × 3.6 EBSE | C | Los estudios bien reportados alimentan la síntesis. |
| 3.1 DORA × 3.10 METR | X | DORA se apoya en autoinforme; METR mide una brecha de unos 40 puntos entre lo percibido y lo medido. |
| 3.1 DORA × 3.5 Experimentos | C | Amplitud correlacional más causalidad local. |
| 3.9 CEBMa × 3.9 Scrum.org EBM | X (parcial) | Mismo nombre, distinto rigor: CEBMa exige evaluar la calidad de la evidencia y la guía de Scrum.org no cita evidencia. |
| 3.9 Scrum.org EBM × Objeción 4 | X | Es antecedente de la parte heredada de ODLC: refuerza que eso no es nuevo. |
| 3.10 METR × 4.11 Cybernetic teammate | C | Dos diseños experimentales de campo; uno mide tiempo y el otro calidad y estructura de equipo. |
| 4.4 Niveles × 4.5 DSB/Bradshaw | X | El DSB pide abandonar los niveles. |
| 4.5 DSB/Bradshaw × 4.6 Coactive design | C | Crítica y alternativa del mismo grupo de investigación. |
| 4.7 Knight × 4.8 IMDA | C | IMDA cita y adopta los modos de Knight. |
| 4.7 Knight × 4.5 DSB | X | Knight reintroduce una escala unidimensional. |
| 4.8 IMDA × 4.9 OWASP | C | Gobernanza organizacional más taxonomía de riesgo técnico. |
| 4.9 OWASP (ASI09) × 4.10 Frontera | C | La confianza excesiva explica la caída de desempeño fuera de la frontera. |
| 4.10 Frontera × 4.12 Metaanálisis | C (con matiz) | Ambos muestran que el efecto depende de la tarea; el metaanálisis muestra que en promedio no hay sinergia. |
| 4.11 Cybernetic teammate × 4.12 Metaanálisis | C (con matiz) | P&G encuentra ganancia en creación de contenido, que es el tipo de tarea donde el metaanálisis también ve ganancias. |
| 4.13 Team Topologies × 4.6 Coactive design | C | Modos de interacción entre equipos e interdependencia en la tarea son la misma idea a dos escalas. |
| 4.13 Team Topologies × 4.3 Revisión HAT | C | Ambos separan composición o estructura de interacción o proceso. |
| 4.14 Microsoft WTI × 3.10 METR | X | Evidencia de autoinforme frente a la brecha medida entre percepción y resultado. |
| 4.14 Microsoft WTI × 4.11 Cybernetic teammate | C | El "ratio" es una variable de composición que el diseño factorial de P&G permitiría testear. |
| 4.8 IMDA × 3.7/3.8 | C | Los puntos de control de IMDA se pueden convertir en hipótesis pre-registradas con criterio de abandono. |
| 4.2 National Academies × 4.7 Knight | I | Una es agenda de investigación y la otra, taxonomía de diseño; no se pisan. |

---

## Preguntas abiertas

1. **Grupo de control irreclutable.** METR no consiguió en 2026 suficiente gente dispuesta a trabajar sin IA. Un piloto de ODLC "con agentes frente a sin agentes" puede tener el mismo problema. Las alternativas que propone METR (aleatorizar por desarrollador, tareas fijas, datos observacionales) no están probadas todavía.
2. **Autoevaluación del autor.** DSR y TAR aceptan que quien diseña el marco lo evalúe. Ninguna fuente consultada dice cuánto sesgo introduce eso ni cómo acotarlo, más allá del pre-registro.
3. **¿Niveles o interdependencias?** La crítica del DSB (2012) y la adopción de niveles por Knight (2025) e IMDA (2026) conviven sin que se haya encontrado una comparación empírica entre ambos enfoques. Esto afecta directamente al Modelo de madurez y a la matriz de Gobernanza de HACS.
4. **Del individuo a la organización.** La evidencia medida (BCG 2023, P&G 2025, metaanálisis 2024) es de individuos o parejas en tareas de un día. No se encontró ningún estudio que mida una unidad organizacional humano-agente de software durante meses.
5. **Métrica de comparación.** El metaanálisis sugiere comparar contra "el mejor de los dos solos". Falta definir qué es "el agente solo" en un ciclo ODLC.
6. **Pistas no verificadas en este relevamiento.** Quedan sin abrir y, por lo tanto, sin citar: DESMET (Kitchenham, metodología para evaluar métodos y herramientas de software, década de 1990), Stol y Fitzgerald, "The ABC of Software Engineering Research" (TOSEM, 2018), "The agentic organization" de McKinsey (2025; la página no cargó) y "Why Human-Autonomy Teaming?" de Shively et al. (2017).
7. **Evidencia de los marcos de evidencia.** Ni EBM (CEBMa o Scrum.org) ni DSR tienen, en lo consultado, mediciones de que su uso mejore resultados. Queda abierto si esa ausencia es un problema o es inherente a los marcos metodológicos.

---

## Fuentes (todas consultadas el 2026-10-08)

- DORA, Research: https://dora.dev/research/
- DX Newsletter, "The science behind DORA" (2024-05-17): https://newsletter.getdx.com/p/the-science-behind-dora
- Junade Ali, "Bye bye DORA: flaws of the State of DevOps reports" (2024-01-03): https://hackernoon.com/bye-bye-dora-flaws-of-the-state-of-devops-reports
- getAbstract, resumen de *Accelerate*: https://getabstract.com/summary/32584
- Cynefin.io, Facilitation pack: Accelerate: https://cynefin.io/wiki/Facilitation_pack:_Accelerate
- Google, "How are developers using AI? Inside our 2025 DORA report" (2025-09-23): https://blog.google/technology/developers/dora-report-2025/
- DORA 2025 report: https://dora.dev/research/2025/dora-report/
- Hevner et al. 2004, ficha (Universidad de Arizona): https://experts.arizona.edu/en/publications/design-science-in-information-systems-research/
- Peffers et al. 2007, PDF: https://scholar.cgu.edu/samir-chatterjee/wp-content/uploads/sites/6/2013/07/jmis-article.pdf
- Venable, Pries-Heje y Baskerville 2016, FEDS: https://ideas.repec.org/a/taf/tjisxx/v25y2016i1p77-89.html
- Wieringa 2012, TAR (CAiSE): https://research.utwente.nl/en/publications/designing-technical-action-research-and-generalizing-from-real-wo/
- Runeson y Höst 2009, PDF en Lund University: https://lup.lub.lu.se/search/files/2838283/1276782.pdf ; libro 2012: https://lup.lub.lu.se/search/publication/3242770
- Wohlin et al., *Experimentation in Software Engineering*, ed. 2024 (Bookshare): https://bookshare.org/browse/book/6202903 ; ficha de la ed. 2012 en EBSE Durham: https://ebse.webspace.durham.ac.uk/?p=249
- Kitchenham, Dybå y Jørgensen 2004 (EBSE Durham): https://ebse.webspace.durham.ac.uk/ebse-bibliography/evidence-based-software-engineering/
- Dybå y Dingsøyr 2008 (SINTEF): https://www.sintef.no/en/publications/publication/1040587/ ; resumen (EBSE Durham): https://ebse.webspace.durham.ac.uk/?p=139
- ESEM 2024 Registered Reports: https://conf.researchr.org/track/esem-2024/esem-2024-registered-reports
- MSR 2026 Registered Reports: https://2026.msrconf.org/track/msr-2026-registered-reports
- Scheel, Schijen y Lakens 2021: https://research.tue.nl/en/publications/an-excess-of-positive-results-comparing-the-standard-psychology-l/
- Elliot Robia, "Kill Criteria" (2023-07-17), sobre Annie Duke, *Quit* (2022): https://elliotrobia.substack.com/p/kill-criteria
- CEBMa, "What is evidence-based management?": https://cebma.org/resources/frequently-asked-questions/what-is-evidence-based-management/
- Barends y Rousseau 2018, ficha del libro: https://libraries.escp.eu/doc/SYRACUSE/68016
- Evidence-Based Management Guide 2020 (Schwaber / Scrum.org, copia curada): https://engineering-leadership.hinshelwood.com/guides/evidence-based-management-guide/
- METR, estudio 2025 (2025-07-10): https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- METR, cambio de diseño (2026-02-24): https://metr.org/blog/2026-02-24-uplift-update/
- Brandt et al. 2017, NASA HAT flight-following: https://ntrs.nasa.gov/citations/20170011268 y https://ntrs.nasa.gov/citations/20170007259
- National Academies 2022, *Human-AI Teaming*: https://www.nationalacademies.org/publications/26355
- O'Neill / Schelble et al., revisión HAT (Clemson): https://open.clemson.edu/all_data/901
- Parasuraman, Sheridan y Wickens 2000 (resumen): https://andrewclark.super.site/all-media/a-model-for-types-and-levels-of-human-interaction-with-automation
- Defense Science Board 2012, presentación de R. Murphy: https://www.nationalacademies.org/cdn/materials/9fba07ce-1e6f-49ca-acbf-c566d0111e51
- Lawfare, "Defense Science Board on Autonomous Systems" (2012-09-12): https://www.lawfaremedia.org/article/defense-science-board-autonomous-systems
- Bradshaw et al. 2013, "Seven Deadly Myths": https://www.colorado.edu/irt/autonomous-systems/about/seven-deadly-myths-autonomous-systems
- Johnson et al. 2014, Coactive Design (OpenAlex): https://api.openalex.org/works/doi:10.5898%2FJHRI.3.1.JOHNSON
- Feng, McDonald y Zhang 2025, Knight Institute: https://knightcolumbia.org/content/levels-of-autonomy-for-ai-agents-1
- IMDA, comunicado (2026-01-22): https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2026/new-model-ai-governance-framework-for-agentic-ai
- IMDA, MGF for Agentic AI v1.5 (2026-05-20), PDF: https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf
- OWASP GenAI, lanzamiento del Top 10 agentic (2025-12-09): https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/
- Giskard, resumen OWASP Agentic Top 10 (2025-12-18): https://www.giskard.ai/knowledge/owasp-top-10-for-agentic-application-2026
- Ethan Mollick, "Centaurs and Cyborgs on the Jagged Frontier": https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged
- AMT Lab, reseña de *Co-Intelligence* (2025-03-28): https://amt-lab.org/reviews/2025/3/co-intelligence-offers-a-model-for-integratting-genai-into-your-work
- Dell'Acqua et al. 2025, "The Cybernetic Teammate" (NBER w33641): https://www.nber.org/papers/w33641
- Vaccaro, Almaatouq y Malone 2024 (IDEAS/RePEc): https://ideas.repec.org/a/nat/nathum/v8y2024i12d10.1038_s41562-024-02024-1.html
- InfoQ, Skelton en QCon London 2026 (2026-03-31): https://infoq.com/news/2026/03/ai-agency-team-topologies
- IT Revolution, "Team Topologies: five years of transforming organizations" (2024-09-03): https://itrevolution.com/articles/team-topologies-five-years-of-transforming-organizations
- Shortform, resumen de Team Topologies (2023-01-31): https://www.shortform.com/blog/team-topologies-interaction-modes/
- Alves et al. 2023, "Harmonizing DevOps Taxonomies": https://arxiv.org/abs/2302.00033
- Microsoft, 2025 Work Trend Index (2025-04-23): https://blogs.microsoft.com/blog/2025/04/23/the-2025-annual-work-trend-index-the-frontier-firm-is-born/
