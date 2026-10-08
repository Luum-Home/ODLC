---
tags: [crudo, investigacion, objeciones]
status: crudo
created: 2026-10-08
---

# Propuestas existentes para las objeciones 1 y 2

Pregunta: ¿qué soluciones ya propusieron otras personas u organizaciones para las dos primeras objeciones de "Objeciones al marco" (docs/06_fundacional)? La objeción 1 es la crítica de Deming a la gestión por objetivos: los objetivos numéricos se manipulan. La objeción 2: si el éxito solo cuenta con el outcome validado, el ciclo de feedback se vuelve lento. Este documento releva propuestas ajenas, con autor y fuente. No agrega propuestas propias.

Fuentes consultadas el 2026-10-08. Convención de evidencia: **[dato]** = medido por quien lo publica, con método visible; **[declarado]** = resultado que una organización afirma sobre sí misma o sobre sus clientes, sin método publicado o con conflicto de interés; **[opinión]** = argumento o recomendación sin medición. Lo que solo apareció en resultados de búsqueda, sin abrir la fuente, queda fuera o marcado como "no verificado".

## Resumen

1. La objeción 1 tiene propuestas viejas y bien argumentadas, pero casi ninguna probada con un diseño controlado. Abundan los casos de falla documentados (Wells Fargo 2016, Ford Pinto) y escasean los experimentos que muestren una defensa que funcione.
2. Las defensas se agrupan en cuatro familias: separar la meta de la compensación (OKR según Doerr y Google; Holmström y Milgrom 1991), medir más de una cosa a la vez (indicadores pareados de Grove, Balanced Scorecard), cambiar el tipo de meta (metas relativas de Beyond Budgeting) y dejar de evaluar personas contra metas (Deming y Joiner).
3. El único dato cuantitativo sobre OKR en software que se encontró es correlacional: madurez de OKR asociada a satisfacción y experimentación en una empresa (Butler, Zimmermann y Bird, ICSE 2024). No compara con OKR atados a compensación.
4. Las propuestas de las familias 1 y 4 se contradicen entre sí: los OKR mantienen metas numéricas ambiciosas, y Deming pide eliminarlas. Ordóñez et al. (2009) cuestionan además las metas "estiradas" que los OKR promueven.
5. Para la objeción 2 hay propuestas con datos medidos, casi todas de experimentación online a gran escala: métricas proxy aprendidas de experimentos pasados (Netflix), surrogate index (Athey et al.), reducción de varianza (CUPED, alrededor de 50% en Bing) y tests secuenciales.
6. La medicina es el contraejemplo central. Los surrogate endpoints aceleran las decisiones y fallaron con consecuencias graves (CAST, 1991). De 46 aprobaciones oncológicas aceleradas con más de 5 años de seguimiento, solo 20 (43%) mostraron beneficio clínico (Liu et al., JAMA 2024).
7. La industria tiene un resultado más optimista: las inversiones de signo entre efecto corto y largo son raras, y se concentran en calidad de contenido, monetización y precios (Sigerson et al., 2026). El mismo trabajo dice que no hay sustituto para un experimento largo bien hecho.
8. En producto, las propuestas de indicadores adelantados (Torres, North Star, 4DX, innovation accounting) no presentan evidencia propia: se apoyan en testimonios o casos sin control.
9. Usuarios simulados con LLM: aciertan promedios agregados en algunos dominios (Argyle et al., 2023), pero fallan en varianza, en coeficientes y en reproducibilidad (Bisbee et al., 2024), y en 53% de las tareas de UX dan distribuciones distintas a las reales (Kuric et al., 2026).
10. No se encontró ninguna propuesta que resuelva la objeción 2 para organizaciones con poco tráfico o pocos experimentos históricos: las técnicas con datos medidos suponen volumen y un historial de experimentos largos.

---

## Objeción 1: los objetivos numéricos se manipulan

Para ubicar el problema: el punto 11b de Deming pide eliminar la gestión por objetivos y la gestión por números y metas numéricas, y el 12b agrega abolir la calificación anual por mérito (Deming, *Out of the Crisis*, MIT Press, 1982/1986, pp. 23-24, transcripto en deming.org). Manheim y Garrabrant (arXiv:1803.04585, 2018, v4 2019) distinguen cuatro mecanismos de Goodhart: regresional (el proxy arrastra ruido), extremal (la relación se rompe en los extremos), causal (intervenir sobre el proxy cambia su vínculo con la meta) y adversarial (agentes con intereses propios corrompen la métrica, la ley de Campbell). Los autores no proponen mitigaciones; la taxonomía sirve para ver qué variante ataca cada propuesta de abajo.

### 1.1 OKR separados de la compensación

- **Quién y dónde.** Andy Grove en Intel; difundido por John Doerr (*Measure What Matters*, 2018). La organización de Doerr, en una página firmada por Ryan Panchadsaram (sin fecha visible), dice que lo que diferencia a los OKR del MBO es que están "divorced from compensation". La guía re:Work de Google (sin fecha visible) aclara que los OKR no son sinónimo de evaluación de desempeño, que se publican para toda la organización y que el rango esperado de cumplimiento está entre 60% y 70%.
- **Qué resuelve.** La variante adversarial: si la meta no paga, se reduce el incentivo a pactar metas blandas o falsear el número. La calificación esperada por debajo de 100% busca que no convenga proponer metas seguras.
- **Dónde se aplicó.** Intel y Google según las propias fuentes. En el estudio de Butler, Zimmermann y Bird (ICSE 2024, arXiv:2311.00236), una empresa multinacional de software con unos 4.000 ingenieros.
- **Evidencia.** [declarado] Google y whatmatters.com describen la práctica sin medir su efecto. [dato] Butler et al.: 47 entrevistas y 512 respuestas de encuesta (13% de respuesta). La madurez de OKR se correlaciona con satisfacción y con uso de experimentación (p<0,05); solo 45% de los equipos se considera efectivo midiendo sus metas, y 60% de los managers reporta mala traducción de los OKR ejecutivos a métricas de equipo. Es correlacional y el estudio no analiza el vínculo con compensación.
- **Críticas o fallas.** Butler et al. registran la preocupación de que las metas medibles empujen a "embellecer números", sin cuantificar el gaming. Torres (producttalk.org, 2022-12) observa que cuando la rendición de cuentas premia el desempeño y no el aprendizaje aparecen el *sandbagging* y la competencia entre equipos. Que la meta esté separada del sueldo en el papel no impide que se use en la evaluación de hecho; ninguna fuente abierta midió esa brecha.
- **Combinabilidad.** Se complementa con 1.5 (Holmström y Milgrom), que da el fundamento teórico de separar la meta del pago. Choca con 1.6 (Deming y Joiner), que no acepta metas numéricas, y con 1.7, que cuestiona las metas estiradas.

### 1.2 Indicadores pareados

- **Quién y dónde.** Andrew Grove, *High Output Management* (1983). El pasaje se consultó como cita subrayada en Goodreads (fuente secundaria; el libro no se abrió): como los indicadores dirigen la actividad, hay que emparejarlos para medir a la vez el efecto y el contraefecto. Ejemplo de Grove: nivel de inventario junto con faltantes.
- **Qué resuelve.** La optimización unilateral (variantes regresional y extremal): mover un número a costa de otro que nadie mira.
- **Dónde se aplicó.** Intel, según el propio Grove. No se encontró una medición independiente.
- **Evidencia.** [opinión] Recomendación de práctica, sin datos.
- **Críticas o fallas.** No protege contra la variante adversarial si ambos indicadores se pueden falsear. Elegir el contraindicador correcto exige saber de antemano qué se va a sacrificar.
- **Combinabilidad.** Se complementa con 1.3 (Balanced Scorecard), que generaliza la idea a varias perspectivas. Tiene tensión con 2.3 (North Star), que pide una sola métrica.

### 1.3 Balanced Scorecard

- **Quién y dónde.** Robert Kaplan y David Norton, "The Balanced Scorecard: Measures That Drive Performance", *Harvard Business Review*, enero-febrero de 1992. Sostienen que las medidas financieras tradicionales dan señales engañosas para la mejora continua y la innovación, y proponen equilibrarlas con medidas operativas.
- **Qué resuelve.** Que una sola métrica, sobre todo financiera, domine las decisiones.
- **Dónde se aplicó.** Adopción masiva desde 1992, con decenas de libros y proyectos (Strohhecker, System Dynamics Conference, 2004).
- **Evidencia.** [dato, limitado] Strohhecker reconstruye la teoría de mejora implícita del BSC y la prueba en un micromundo de simulación con participantes. Sus resultados preliminares indican que el efecto del BSC sobre el desempeño podría estar sobreestimado.
- **Críticas o fallas.** Strohhecker señala que las críticas publicadas son raras y cita a Nørreklit (*Management Accounting Research*, 2000) como excepción, por los supuestos de causalidad del modelo. El texto de Nørreklit no se abrió en este relevamiento.
- **Combinabilidad.** Se complementa con 1.2. Es independiente de 1.1: puede usarse con o sin vínculo a la compensación, y el artículo de 1992 no resuelve la variante adversarial.

### 1.4 Beyond Budgeting: metas relativas y separación de meta, pronóstico y asignación

- **Quién y dónde.** Beyond Budgeting Round Table (BBRT), modelo desarrollado en 1998 (white paper "Beyond Budgeting at 25", Bjarte Bogsnes, marzo de 2023). La autoría original suele atribuirse a Jeremy Hope y Robin Fraser; esa atribución no se verificó en una fuente abierta en este relevamiento. Los principios vigentes (bb_principles.pdf de la BBRT) piden metas direccionales, ambiciosas y relativas en lugar de metas fijas y en cascada; evaluar el desempeño de forma holística, "not based on measurement only and not for rewards only"; y premiar el éxito compartido frente a la competencia, no contra contratos de desempeño fijos.
- **Qué resuelve.** La negociación de metas blandas y el sesgo de los pronósticos. En una entrevista de 2013 (rebelsguidetopm.com, 2013-11-11), Bogsnes explica que Statoil separó meta, pronóstico y asignación de recursos, con números y frecuencias distintas para cada uno, y que la calidad del pronóstico mejoró al sacarle el sesgo de gaming que traían las metas.
- **Dónde se aplicó.** Statoil/Equinor (testimonio de Bogsnes). El white paper menciona adopción creciente sin listar casos con datos.
- **Evidencia.** [declarado] Encuesta de BCG a practicantes, citada por la BBRT: 59% reporta aumento de ventas, 56% ahorro en el proceso de presupuesto y 52% mejores decisiones. Son autorreportes de adoptantes, citados por la organización que promueve el modelo y sin grupo de control. [testimonio] Bogsnes sobre Statoil.
- **Críticas o fallas.** El propio white paper reconoce implementaciones reducidas a pronósticos móviles, que pierden el resto del modelo. No se encontró una evaluación independiente con control.
- **Combinabilidad.** Se complementa con 1.5 (pago de baja potencia, premios de equipo) y con 1.6 (evaluación holística en lugar de contra la meta). Tiene tensión parcial con 1.1: los OKR fijan resultados clave absolutos; Beyond Budgeting prefiere metas relativas.

### 1.5 Incentivos de baja potencia cuando hay tareas difíciles de medir

- **Quién y dónde.** Bengt Holmström y Paul Milgrom, "Multitask Principal-Agent Analyses: Incentive Contracts, Asset Ownership, and Job Design", *Journal of Law, Economics, & Organization*, vol. 7, 1991, pp. 24-52.
- **Qué resuelve.** Si una persona reparte esfuerzo entre tareas medibles y no medibles, pagar fuerte por la medible desvía esfuerzo de la otra. El modelo muestra que puede ser óptimo pagar sueldo fijo o un incentivo débil aunque exista una buena medida objetiva, y que separar las tareas en puestos distintos atenúa el problema. Ejemplo del paper: pagar a docentes por el resultado de pruebas estandarizadas sacrifica la creatividad y la comunicación oral y escrita. En una nota al pie, una docente de Carolina del Sur que en 1989 pasó respuestas a sus alumnos para mejorar su calificación.
- **Dónde se aplicó.** Es teoría económica, con amplia influencia en el diseño de contratos. Este relevamiento no buscó aplicaciones empresariales medidas.
- **Evidencia.** [teoría formal] Modelo matemático con ejemplos ilustrativos, no prueba empírica.
- **Críticas o fallas.** No dice cuánto incentivo es "bajo" en un caso concreto, y los propios autores suponen que el agente aporta esfuerzo aun sin pago explícito.
- **Combinabilidad.** Da fundamento a 1.1 y a 1.4. Contradice esquemas de pago por cumplimiento de meta, como el que la CFPB describe en Wells Fargo (caso de falla, abajo).

### 1.6 Mejorar el sistema en lugar de fijar metas (Deming, Joiner)

- **Quién y dónde.** W. Edwards Deming, puntos 11 y 12 (*Out of the Crisis*), que reemplazan la gestión por objetivos por "liderazgo". Brian Joiner, *Fourth Generation Management*, según la cita de Mark Graban (leanblog.org, 2025-03-16): ante una meta, la gente puede mejorar el sistema, distorsionar el sistema o distorsionar los números, y elige lo más fácil. La pregunta de Deming que Graban toma como ancla es "¿con qué método?".
- **Qué resuelve.** Las variantes causal y adversarial: en lugar de defender la métrica, quita el incentivo a manipularla. La evaluación individual contra metas desaparece.
- **Dónde se aplicó.** Graban cita el caso de Paul O'Neill en Alcoa: los días perdidos por lesión cada 100 trabajadores bajaron de 1,86 a 0,2, y a 0,125 en 2012.
- **Evidencia.** [testimonio] El caso Alcoa se presenta sin control y con una métrica que, a su vez, se podría manipular. No se encontró una prueba controlada del enfoque de Deming aplicado a metas de producto.
- **Críticas o fallas.** Dice qué no hacer y deja abierto qué reemplaza a la meta en la práctica cotidiana. Las herramientas de control estadístico de procesos asociadas a Deming y Wheeler (*Understanding Variation*, 1993) no se abrieron en este relevamiento.
- **Combinabilidad.** Contradice 1.1 y 2.1 (4DX), que ponen metas numéricas en el centro. Se complementa con 1.4 (evaluación holística) y con 1.5.

### 1.7 La meta como medicamento: dosis y efectos adversos

- **Quién y dónde.** Lisa Ordóñez, Maurice Schweitzer, Adam Galinsky y Max Bazerman, "Goals Gone Wild: The Systematic Side Effects of Overprescribing Goal Setting", *Academy of Management Perspectives* 23(1), febrero de 2009, pp. 6-16. Resumen consultado en HBS Working Knowledge (2009-03-02).
- **Qué resuelve.** No elimina las metas: propone usarlas con dosis y supervisión, como un medicamento recetado. Lista efectos adversos (foco estrecho, más conducta no ética, preferencias de riesgo distorsionadas, aprendizaje inhibido, menor motivación intrínseca) y diez preguntas para hacerse antes de fijar una meta. Las metas funcionan mejor cuando se sabe exactamente qué conducta se busca y el riesgo ético es bajo.
- **Dónde se aplicó.** Es una revisión con casos de falla: Ford Pinto (meta de menos de 2.000 libras y menos de USD 2.000, con 53 muertes atribuidas en el resumen), mecánicos de Sears y Bausch & Lomb.
- **Evidencia.** [opinión con casos] Revisión narrativa. Locke y Latham respondieron en la misma revista (2009) defendiendo la literatura de fijación de metas; esa respuesta no se abrió.
- **Críticas o fallas.** Los casos se eligieron por haber fallado (sesgo de selección), y la disputa con Locke y Latham es sobre cuánto pesa la evidencia de efectos adversos.
- **Combinabilidad.** Contradice las metas estiradas de 1.1. Se complementa con 1.2 y 1.3, que atacan el foco estrecho.

### 1.8 Evidence-Based Management (Scrum.org)

- **Quién y dónde.** Scrum.org, *Evidence-Based Management Guide* (versión de septiembre de 2020, consultada en dokk.org). La versión de 2018 agregó el área Unrealized Value y movió las medidas concretas a un apéndice de ejemplos, porque cada organización tiene que encontrar las suyas (InfoQ, 2019-01-23, entrevista a Patricia Kong y Kurt Bittner).
- **Qué resuelve.** Pasar de medir actividad a medir valor (cuatro áreas: valor actual, valor no realizado, capacidad de innovar, tiempo al mercado), con un ciclo de hipótesis, experimento e inspección. La jerarquía meta estratégica / metas intermedias / metas tácticas inmediatas también responde a la objeción 2: las metas intermedias existen porque la estratégica está demasiado lejos para navegarla directamente.
- **Dónde se aplicó.** InfoQ menciona a Net Health y a una empresa de software inmobiliario.
- **Evidencia.** [declarado] La empresa inmobiliaria reporta 92% de aumento del EBITDA ajustado y un eNPS que pasó de 26 a "high 60s" en un año. Fuente: el proveedor del marco, sin control ni método publicado.
- **Críticas o fallas.** La guía no advierte de forma explícita contra el gaming ni contra usar las métricas para premiar o castigar personas, que es exactamente la objeción de Deming.
- **Combinabilidad.** Se complementa con 2.2 (resultados de producto como metas intermedias) y con 2.5. Es independiente de la cuestión de la compensación: no la resuelve ni la contradice.

### Caso de falla que enseña: Wells Fargo, 2016

- **Fuente.** CFPB, comunicado del 2016-09-08 (archivo de consumerfinance.gov).
- **Qué pasó.** [dato regulatorio] Empujados por metas de venta e incentivos de compensación, empleados abrieron sin autorización unas 1,5 millones de cuentas de depósito y unas 565.000 de tarjeta de crédito. Hubo multas por USD 100 millones (CFPB), 35 millones (OCC) y 50 millones (Los Ángeles). La orden incluye revisar las mediciones de desempeño y las metas de venta.
- **Qué enseña.** Es la variante adversarial de Goodhart con pago de alta potencia (1.5) y sin indicador pareado de autorización del cliente (1.2). También muestra que el remedio que eligió el regulador fue revisar las metas, no solo controlar más.

---

## Objeción 2: el outcome tarda y el ciclo se vuelve lento

### 2.1 Medidas adelantadas y rezagadas (4DX)

- **Quién y dónde.** Chris McChesney, Sean Covey y Jim Huling, *The 4 Disciplines of Execution* (FranklinCovey, 2012). Página de FranklinCovey consultada: actuar sobre las medidas adelantadas, que son acciones de alto impacto bajo control del equipo, mientras las rezagadas son los resultados.
- **Qué resuelve.** Que el equipo tenga algo que mover y mirar cada semana mientras el resultado tarda.
- **Dónde se aplicó.** Clientes de FranklinCovey.
- **Evidencia.** [declarado] Whirlpool, con USD 5,7 millones incrementales en 90 días, y DeKalb Medical Center, que pasó del percentil 3 al 99 en satisfacción de pacientes. Son casos del vendedor, sin control.
- **Críticas o fallas.** Supone que se sabe de antemano qué medida adelantada predice el resultado. La historia de los surrogate endpoints (2.6) muestra que esa suposición puede ser falsa y, además, peligrosa. Una medida adelantada controlable por el equipo es justamente la más fácil de inflar (objeción 1).
- **Combinabilidad.** Contradice 1.6 (Deming). Requiere 2.6 y 2.7 para validar que la medida adelantada predice el resultado.

### 2.2 Resultados de producto como indicadores adelantados (Teresa Torres)

- **Quién y dónde.** Teresa Torres, *Continuous Discovery Habits* (2021); "Opportunity Solution Trees" (producttalk.org, 2023-12-06) y "Defining Product Outcomes" (producttalk.org, 2022-12).
- **Qué resuelve.** Distingue resultados de negocio (rezagados), resultados de producto (cambios de conducta del cliente que el equipo puede influir) y métricas de tracción, y recomienda que el equipo se haga cargo del resultado de producto. Entre el resultado y la solución, el árbol de oportunidades pone pruebas de supuestos, que dan feedback antes de construir.
- **Dónde se aplicó.** La página menciona Grailed, trivago y SuperAwesome sin resultados medidos.
- **Evidencia.** [opinión] La página enumera beneficios sin datos empíricos ni comparaciones.
- **Críticas o fallas.** Torres admite que el resultado de producto puede empezar siendo solo "direccional" hasta que se sepa medirlo. Advierte que una rendición de cuentas que premia el desempeño produce *sandbagging* (conecta con la objeción 1).
- **Combinabilidad.** Se complementa con 1.8 (metas intermedias de EBM) y con 2.5 (la prueba de supuestos puede ser un experimento controlado). Comparte el riesgo de 2.1.

### 2.3 North Star Metric

- **Quién y dónde.** Sean Ellis (entrevista en el podcast de Intercom, fecha no visible) y Amplitude, *North Star Playbook* (introducción de John Cutler, fecha no visible). Para Ellis, la North Star mide el valor que el cliente experimenta con el tiempo; ejemplos: noches reservadas en Airbnb, usuarios activos diarios en Facebook. La distingue de la "métrica que importa ahora", que es temporal.
- **Qué resuelve.** Alinear equipos alrededor de una métrica que anticipe el crecimiento sostenido y no sea de vanidad.
- **Dónde se aplicó.** Dropbox, Eventbrite y otras, según testimonios de Ellis.
- **Evidencia.** [opinión] El playbook reconoce que ningún marco garantiza el éxito y no presenta datos comparativos.
- **Críticas o fallas.** Una sola métrica es justamente lo que critican 1.2 y 1.3. Ellis condiciona todo a tener encaje producto-mercado.
- **Combinabilidad.** Tiene tensión con 1.2 y 1.3. Se complementa con 2.8: Chou (2026) trata la North Star como meta y estudia cómo mezclarla con proxies.

### 2.4 Contabilidad de la innovación y aprendizaje validado (Lean Startup)

- **Quién y dónde.** Eric Ries, *The Lean Startup* (2011). Consultado a través de la guía de SAFe "Applied Innovation Accounting in SAFe" (Scaled Agile, sin fecha ni autor visibles; buena parte detrás de login). Propone medir el progreso con hitos de aprendizaje en lugar de P&L o ROI.
- **Qué resuelve.** Que una iniciativa temprana tenga una rendición de cuentas antes de que existan resultados financieros.
- **Dónde se aplicó.** SAFe lo incorpora para épicas y MVP.
- **Evidencia.** [opinión] No se encontró una medición en las fuentes abiertas.
- **Críticas o fallas.** El contenido completo de SAFe no estaba accesible. El libro de Ries no se abrió en este relevamiento.
- **Combinabilidad.** Se complementa con 2.2 y 2.5.

### 2.5 Experimentos controlados con un criterio de evaluación que anticipe el largo plazo (OEC)

- **Quién y dónde.** Ron Kohavi, Diane Tang y Ya Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020). Dmitriev, Frasca, Gupta, Kohavi y Vaz, "Pitfalls of Long-Term Online Controlled Experiments" (IEEE Big Data, 2016-12). Hohnhold, O'Brien y Tang, "Focusing on the Long-term: It's Good for Users and Business" (KDD 2015). Kohavi y Thomke, "The Surprising Power of Online Experiments" (HBR, septiembre-octubre de 2017).
- **Qué resuelve.** Un experimento aleatorizado separa el efecto propio de "las otras causas" que menciona la objeción 2. El OEC tiene que medirse en el corto plazo y predecir el valor de largo plazo. Dmitriev et al. dan ejemplos de por qué el corto plazo engaña: subir precios aumenta el ingreso inmediato y reduce el valor de vida del cliente.
- **Dónde se aplicó.** Microsoft/Bing y Google.
- **Evidencia.** [dato] Hohnhold et al. midieron el aprendizaje de largo plazo de los usuarios con grupos de holdback de larga duración en los anuncios de Google Search. El resultado llevó a rediseñar la subasta por calidad y a reducir 50% la carga de anuncios en búsqueda móvil. [dato] Kohavi y Thomke: un cambio de títulos en Bing, postergado por baja prioridad, subió 12% el ingreso, más de USD 100 millones anuales solo en EE.UU.
- **Críticas o fallas.** Dmitriev et al. advierten que en experimentos largos el resultado puede deberse más a inestabilidad de cookies, sesgo de supervivencia y de selección que al efecto real. Hace falta volumen de usuarios.
- **Combinabilidad.** Es la base de 2.7, 2.8, 2.9 y 2.10. Se complementa con 1.2: un OEC suele combinar métricas con guardas.

### 2.6 Surrogate endpoints en medicina, y su historia de fallas

- **Quién y dónde.** Concepto regulatorio de la FDA (aprobación acelerada basada en medidas sustitutas "razonablemente probables" de predecir beneficio clínico). Crítica clásica de Thomas Fleming y David DeMets, "Surrogate end points in clinical trials: are we being misled?", *Annals of Internal Medicine* 125(7):605-613, 1996-10-01 (consultado el registro de PubMed; el texto completo no se abrió).
- **Qué resuelve.** Decidir sin esperar años a la mortalidad o a la calidad de vida.
- **Dónde se aplicó y qué falló.**
  - [dato] CAST (Echt et al., *NEJM* 324:781-788, 1991-03-21). La hipótesis era que suprimir la ectopia ventricular reduce la muerte súbita: el sustituto mejoraba y los pacientes morían más. Con encainida o flecainida, 43 muertes arrítmicas contra 16 con placebo (p=0,0004), y 17 contra 5 por causas cardíacas no arrítmicas (p=0,01), en 1.498 pacientes con 10 meses de seguimiento medio.
  - [dato] Liu, Kesselheim y Cliff (*JAMA* 331(17):1471-1479, 2024-05-07): de 46 indicaciones oncológicas con aprobación acelerada y más de 5 años de seguimiento, 20 (43%) mostraron beneficio clínico en los ensayos confirmatorios, y una se convirtió en aprobación regular pese a un ensayo confirmatorio negativo.
  - [dato] Ciani, Manyara, Chan y Taylor (2022-12, PMC9743760): los ensayos con desenlaces sustitutos sobreestiman el beneficio en más de 40% respecto de los que usan desenlaces finales (razón ajustada 1,46; IC95% 1,05-2,04). Solo un tercio de los ensayos discutía si el sustituto estaba validado. Caso citado: rosiglitazona, aprobada por bajar la glucemia, que no mostró beneficio cardiovascular y fue retirada en 2010.
- **Críticas.** Las fallas de arriba. Ciani et al. proponen guías de reporte (SPIRIT-SURROGATE y CONSORT-SURROGATE).
- **Combinabilidad.** Es la advertencia empírica contra 2.1, 2.2 y 2.3 usados sin validar. Se complementa con 2.7, que formaliza cuándo un sustituto es válido.

### 2.7 Surrogate index (Athey, Chetty, Imbens, Kang)

- **Quién y dónde.** Susan Athey, Raj Chetty, Guido Imbens y Hyunseung Kang, "The Surrogate Index: Combining Short-Term Proxies to Estimate Long-Term Treatment Effects More Rapidly and Precisely", NBER Working Paper 26463 (2019-11), publicado en *Review of Economic Studies* 93(4):2284-2312 (2026).
- **Qué resuelve.** Combina varios resultados de corto plazo en un índice. Bajo el supuesto de surrogacy de Prentice (el resultado final es independiente del tratamiento dado el índice), el efecto sobre el índice es igual al efecto de largo plazo. Caracteriza el sesgo cuando el supuesto falla y propone formas de validarlo con resultados adicionales.
- **Dónde se aplicó.** Un experimento de capacitación laboral en California con varias sedes.
- **Evidencia.** [dato] Con el empleo de los primeros seis trimestres se estimó el efecto a nueve años sobre la tasa media de empleo, con una reducción de 35% del error estándar.
- **Críticas o fallas.** Todo depende del supuesto de Prentice: es exactamente el que falló en CAST (2.6). Validarlo requiere haber observado alguna vez el resultado largo.
- **Combinabilidad.** Se complementa con 2.6 (lo que la medicina aprendió sobre validar sustitutos) y con 2.8 (la versión industrial).

### 2.8 Métricas proxy aprendidas de experimentos pasados

- **Quién y dónde.** Winston Chou (Netflix), "Blending Proxy Metrics with a North Star" (arXiv:2606.21745, 2026-06-19, aceptado en ECML PKDD 2026). Sigerson et al., "Evaluating for the long term: Learnings from industry" (arXiv:2608.08043, 2026): 25 investigadores de 15 plataformas online y 4 universidades.
- **Qué resuelve.** Chou estima, con experimentos históricos, cuánto pesar la métrica proxy frente a la North Star según la potencia del experimento y la calidad del proxy. Con mejores proxies convienen experimentos más chicos y frecuentes.
- **Dónde se aplicó.** Netflix (Chou). Sigerson et al. resumen la práctica de 15 plataformas.
- **Evidencia.** [dato agregado] Sigerson et al.: las inversiones de signo entre efecto corto y largo son raras y se concentran en calidad de contenido, monetización y precios. Un proxy simple (el efecto de corto plazo sobre la misma métrica de largo plazo) suele rendir igual o mejor que índices complejos. El abstract de Chou no trae números de resultados.
- **Críticas o fallas.** Sigerson et al.: no hay sustituto para un experimento largo bien hecho, los surrogates experimentales son preferibles a los observacionales y eso exige muchos experimentos largos que la mayoría de las plataformas no tiene. Quedan abiertos los tratamientos que cambian con el tiempo y los efectos que no pasan por el proxy.
- **Combinabilidad.** Se complementa con 2.5 y 2.7. Matiza 2.6: en producto digital la inversión de signo parece menos frecuente que en medicina, salvo en monetización y precios.

### 2.9 Reducción de varianza (CUPED)

- **Quién y dónde.** Alex Deng, Ya Xu, Ron Kohavi y Toby Walker, "Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data", WSDM 2013 (resumen en exp-platform.com).
- **Qué resuelve.** Usa datos previos al experimento para bajar la varianza y llegar a una conclusión con menos usuarios o menos días.
- **Dónde se aplicó.** Bing.
- **Evidencia.** [dato] Alrededor de 50% de reducción de varianza: la misma potencia con la mitad de usuarios o de duración.
- **Críticas o fallas.** La ganancia depende de cuánto se correlaciona el dato previo con la métrica, y no sirve si no hay historia previa del usuario. El resumen no trae otras limitaciones.
- **Combinabilidad.** Se complementa con 2.5, 2.8 y 2.10. Acorta el tiempo hasta una respuesta sin cambiar la métrica, por lo que no choca con la objeción 1.

### 2.10 Tests secuenciales y bayesianos (mirar antes sin engañarse)

- **Quién y dónde.** Ramesh Johari y coautores, "Always Valid Inference: Bringing Sequential Analysis to A/B Testing" (arXiv:1512.04922, 2015-12; v. 2019-07), con Optimizely. Alex Deng, Jiannan Lu y Shouyuan Chen, "Continuous Monitoring of A/B Tests without Pain: Optional Stopping in Bayesian Testing" (arXiv:1602.05549, 2016-02).
- **Qué resuelve.** Permite parar un experimento apenas hay evidencia suficiente, en lugar de esperar un tamaño fijo, sin invalidar la inferencia.
- **Dónde se aplicó.** Johari et al. dicen que el método se implementó en una plataforma comercial y se usó en cientos de miles de experimentos.
- **Evidencia.** [dato de despliegue y prueba formal] Johari et al. dan p-valores y intervalos siempre válidos. Deng et al. prueban la validez bayesiana con reglas de parada adecuadas y advierten contra reglas impropias.
- **Críticas o fallas.** [dato de simulación] David Robinson ("Is Bayesian A/B Testing Immune to Peeking? Not Exactly", varianceexplained.org, 2015-08-21). En sus simulaciones sin efecto real, 22,68% de los tests cruzan p<0,05 en algún momento si se mira todos los días. Con una regla bayesiana de pérdida esperada, mirar a diario lleva a adoptar la variante en 11,8% de los casos, más de cuatro veces lo esperado. El método bayesiano no promete controlar el error tipo I.
- **Combinabilidad.** Se complementa con 2.9. Robinson y Deng et al. no se contradicen: coinciden en que la validez depende de la regla de parada.

### 2.11 Usuarios simulados con LLM

- **Quién y dónde.**
  - A favor: Lisa Argyle, Ethan Busby, Nancy Fulda, Joshua Gubler, Christopher Rytting y David Wingate, "Out of One, Many: Using Language Models to Simulate Human Samples", *Political Analysis* 31(3):337-351, 2023 (arXiv:2209.06899).
  - En contra: James Bisbee, Joshua Clinton, Cassy Dorff, Brenton Kenkel y Jennifer Larson, "Synthetic Replacements for Human Survey Data? The Perils of Large Language Models", *Political Analysis*, 2024. Eduard Kuric, Peter Demcak y Matus Krajcovic, "What Would GPT Click" (arXiv:2605.18302, 2026-05-18).
- **Qué resuelve.** Tener respuestas "de usuarios" en minutos, sin esperar al mundo.
- **Evidencia.**
  - [dato] Argyle et al.: con GPT-3 condicionado en perfiles reales, correlaciones tetracóricas con el voto de la encuesta ANES de 0,90 (2012), 0,92 (2016) y 0,94 (2020). Los mismos autores reconocen sesgo hacia candidatos demócratas, mal desempeño con independientes y resultados limitados a política de EE.UU.
  - [dato] Bisbee et al.: ChatGPT replica promedios de la ANES, pero con menos varianza. 48% de los coeficientes de regresión difieren significativamente y en cerca de un tercio de esos casos el signo se invierte. Además, el mismo prompt dio distribuciones distintas entre abril y julio de 2023.
  - [dato] Kuric et al.: en doce pruebas de primer clic con 3.431 participantes reales, las respuestas sintéticas dieron una distribución significativamente distinta en 53% de las tareas.
- **Críticas o fallas.** Las de arriba. Reproducen el promedio esperable y fallan en la variación y en lo inesperado, que es lo que un ciclo de aprendizaje necesita detectar.
- **Combinabilidad.** Como reemplazo del outcome, lo contradicen 2.6 (un sustituto no validado) y los propios datos de Bisbee y Kuric. Ninguna fuente abierta probó su uso como filtro previo a un experimento real.

---

## Tabla de combinabilidad

Los pares que no figuran se consideran independientes: atacan problemas distintos y no se condicionan.

| Propuesta A | Propuesta B | Relación | Motivo |
|---|---|---|---|
| 1.1 OKR sin compensación | 1.5 Holmström-Milgrom | complementa | El modelo multitarea justifica no pagar por la métrica medible |
| 1.1 OKR sin compensación | 1.6 Deming-Joiner | contradice | Los OKR mantienen metas numéricas y Deming pide eliminarlas |
| 1.1 OKR sin compensación | 1.7 Ordóñez et al. | contradice | Los OKR promueven metas estiradas (60-70%) y Ordóñez documenta sus efectos adversos |
| 1.1 OKR sin compensación | 1.4 Beyond Budgeting | contradice en parte | Resultados clave absolutos contra metas relativas; coinciden en desacoplar meta y pago |
| 1.2 Indicadores pareados | 1.3 Balanced Scorecard | complementa | Los dos miden varias dimensiones para evitar el sacrificio silencioso |
| 1.2 Indicadores pareados | 2.3 North Star | contradice en parte | Varias métricas con contraefecto contra una sola métrica central |
| 1.2 Indicadores pareados | 2.5 OEC | complementa | Un OEC con métricas de guarda es un par efecto y contraefecto |
| 1.4 Beyond Budgeting | 1.5 Holmström-Milgrom | complementa | Premios de equipo, relativos y de baja potencia |
| 1.4 Beyond Budgeting | 1.6 Deming-Joiner | complementa | Ambos quitan la evaluación contra un número fijo |
| 1.5 Holmström-Milgrom | caso Wells Fargo | contradice | Wells Fargo es el pago de alta potencia que el modelo desaconseja |
| 1.6 Deming-Joiner | 2.1 4DX | contradice | 4DX pone metas y marcadores numéricos en el centro |
| 1.8 EBM | 2.2 Torres | complementa | Las metas intermedias de EBM cumplen el papel de los resultados de producto |
| 2.1 4DX | 2.6 Surrogates médicos | contradice como supuesto | 4DX asume que la medida adelantada predice; CAST muestra que puede no hacerlo |
| 2.2 Torres | 2.5 Experimentos | complementa | La prueba de supuestos puede ser un experimento controlado |
| 2.3 North Star | 2.8 Proxies aprendidos | complementa | Chou mezcla proxy y North Star según la potencia del experimento |
| 2.5 Experimentos | 2.9 CUPED | complementa | CUPED acorta el mismo experimento |
| 2.5 Experimentos | 2.10 Tests secuenciales | complementa | Permite parar antes sin perder validez |
| 2.6 Surrogates médicos | 2.7 Surrogate index | complementa | El índice formaliza el supuesto de validez que faltó en CAST |
| 2.6 Surrogates médicos | 2.8 Proxies aprendidos | matiza | La industria reporta inversiones de signo raras, salvo monetización y precios |
| 2.7 Surrogate index | 2.8 Proxies aprendidos | complementa | Misma idea, una académica y otra industrial |
| 2.9 CUPED | 2.10 Tests secuenciales | complementa | Menos varianza y parada temprana se suman |
| 2.11 Usuarios LLM | 2.6 Surrogates médicos | contradice como reemplazo | Es un sustituto no validado; Bisbee y Kuric muestran desvíos |
| 1.x (defensas contra el gaming) | 2.1-2.3 (indicadores adelantados) | tensión | La medida adelantada controlable por el equipo es la más fácil de inflar; ninguna fuente de 2.1-2.3 trae una defensa |

---

## Preguntas abiertas

1. No se encontró un estudio que compare OKR atados a la compensación con OKR separados de ella. La separación se recomienda en todas las fuentes y no se midió en ninguna.
2. Ninguna fuente abierta trata el gaming de métricas por agentes de IA en un ciclo de trabajo. La literatura de *reward hacking* no se relevó acá y sería el paso siguiente para la objeción 1 aplicada a agentes.
3. Las técnicas con datos medidos para acortar el ciclo (2.7 a 2.10) suponen tráfico alto y un historial de experimentos largos. Para equipos chicos o B2B con pocos clientes no se encontró una propuesta con evidencia.
4. Ninguna fuente propone separar el tiempo de espera de evidencia del tiempo de trabajo, que es lo que pide la objeción 2 para el *Time To Outcome*. El concepto más cercano son los holdbacks largos (Hohnhold et al.), que corren en paralelo al trabajo siguiente.
5. Sigerson et al. reportan inversiones de signo raras en plataformas online, y la medicina reporta fallas frecuentes de los sustitutos. No está claro de qué lado cae un objetivo de negocio típico de ODLC.
6. Pendientes de abrir: el texto completo de Fleming y DeMets (1996), Nørreklit (2000), Locke y Latham (2009), Austin (*Measuring and Managing Performance in Organizations*, 1996), *Understanding Variation* de Wheeler (1993) y las fuentes primarias de Hope y Fraser.

---

## Comandos de verificación

Registros de PubMed (CAST y Liu et al.) y punto 11b de Deming. Son read-only.

```bash
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=1900101&rettype=abstract&retmode=text" | grep -n "43 receiving"
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=38583175&rettype=abstract&retmode=text" | grep -n "20/46"
curl -sL -A "Mozilla/5.0" https://deming.org/explore/fourteen-points/ | sed 's/<[^>]*>/ /g' | tr -s ' \n' | grep -o "Eliminate management by objective[^.]*\."
```

---

## Fuentes (consultadas el 2026-10-08)

- Deming, W. E., 14 puntos, transcripción de *Out of the Crisis*, pp. 23-24. https://deming.org/explore/fourteen-points/
- Manheim, D. y Garrabrant, S., "Categorizing Variants of Goodhart's Law", arXiv:1803.04585, 2018 (v4 2019). https://ar5iv.arxiv.org/html/1803.04585
- Panchadsaram, R., "OKR meaning, definition, example", whatmatters.com (sin fecha visible). https://www.whatmatters.com/faqs/okr-meaning-definition-example
- Google re:Work, "Set goals with OKRs" (sin fecha visible). https://rework.withgoogle.com/en/guides/set-goals-with-okrs
- Butler, J., Zimmermann, T. y Bird, C., "Objectives and Key Results in Software Teams", ICSE 2024, arXiv:2311.00236. https://ar5iv.labs.arxiv.org/html/2311.00236
- Grove, A., *High Output Management* (1983), pasaje subrayado en Goodreads. https://www.goodreads.com/notes/27140043-high-output-management/63310182-andrii-vozniuk/b67bdf40-405b-415d-950f-158e5a7bbdef
- Kaplan, R. y Norton, D., "The Balanced Scorecard: Measures That Drive Performance", HBR, 1992-01. https://hbr.org/1992/01/the-balanced-scorecard-measures-that-drive-performance-2
- Strohhecker, J., "Simulation Based Experiments for Testing the Balanced Scorecard's Built-in Performance Improvement Theory", System Dynamics Conference, 2004. https://proceedings.systemdynamics.org/2004/SDS_2004/PAPERS/410STROH.pdf
- Beyond Budgeting Round Table, "Our Principles". https://www.bbrt.org/wp-content/uploads/bb_principles.pdf
- Bogsnes, B., "Beyond Budgeting at 25", white paper, 2023-03. https://bbrt.org/wp-content/uploads/bb-white-paper.pdf
- Entrevista a Bjarte Bogsnes, parte 1, rebelsguidetopm.com, 2013-11-11. https://rebelsguidetopm.com/beyond-budgeting-an-interview-with-bjarte-bogsnes-part-1/
- Holmström, B. y Milgrom, P., "Multitask Principal-Agent Analyses", JLEO 7, 1991. https://people.duke.edu/~qc2/BA532/1991%20JLEO%20Holmstrom%20Milgrom.pdf
- Graban, M., "The Problem With Arbitrary Targets", leanblog.org, 2025-03-16. https://www.leanblog.org/2025/03/arbitrary-targets-real-improvement-gaming-the-numbers/
- HBS Working Knowledge, "When Goal Setting Goes Bad" (sobre Ordóñez et al. 2009), 2009-03-02. https://www.library.hbs.edu/working-knowledge/when-goal-setting-goes-bad
- Scrum.org, *Evidence-Based Management Guide*, 2020-09. https://dokk.org/library/The_Evidence-Based_Management_Guide_scrum_2020
- InfoQ, "Evidence-Based Management Guide Updated", 2019-01-23. https://www.infoq.com/articles/evidence-based-management-guide-updated
- CFPB, comunicado sobre Wells Fargo, 2016-09-08. https://www.consumerfinance.gov/archive/newsroom/consumer-financial-protection-bureau-fines-wells-fargo-100-million-widespread-illegal-practice-secretly-opening-unauthorized-accounts/
- FranklinCovey, "The 4 Disciplines of Execution". https://www.franklincovey.com/the-4-disciplines/
- Torres, T., "Opportunity Solution Trees", producttalk.org, 2023-12-06. https://www.producttalk.org/opportunity-solution-trees/
- Torres, T., "Defining Product Outcomes", producttalk.org, 2022-12. https://www.producttalk.org/2022/12/defining-product-outcomes/
- Intercom, podcast con Sean Ellis (sin fecha visible). https://www.intercom.com/blog/podcasts/sean-ellis-growth/
- Amplitude, *North Star Playbook* (sin fecha visible). https://amplitude.com/books/north-star
- Scaled Agile, "Applied Innovation Accounting in SAFe" (sin fecha visible). https://framework.scaledagile.com/guidance-applied-innovation-accounting-in-safe
- Kohavi, R., Tang, D. y Xu, Y., *Trustworthy Online Controlled Experiments*, Cambridge UP, 2020. https://experimentguide.com/
- Dmitriev, P. et al., "Pitfalls of Long-Term Online Controlled Experiments", IEEE Big Data 2016. https://exp-platform.com/pitfalls-of-long-term/
- Hohnhold, H., O'Brien, D. y Tang, D., "Focusing on the Long-term", KDD 2015. https://research.google/pubs/focus-on-the-long-term-its-better-for-users-and-business/
- Kohavi, R. y Thomke, S., "The Surprising Power of Online Experiments", HBR, 2017-09. https://hbr.org/2017/09/the-surprising-power-of-online-experiments
- Fleming, T. y DeMets, D., *Ann Intern Med* 125(7):605-13, 1996, registro PMID 8815760. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=8815760&rettype=abstract&retmode=text
- Echt, D. et al. (CAST), *NEJM* 324:781-8, 1991, PMID 1900101. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=1900101&rettype=abstract&retmode=text
- Liu, I., Kesselheim, A. y Cliff, E., *JAMA* 331(17):1471-9, 2024, PMID 38583175. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=38583175&rettype=abstract&retmode=text
- Ciani, O. et al., "Surrogate endpoints in trials: a call for better reporting", 2022-12. https://pmc.ncbi.nlm.nih.gov/articles/PMC9743760
- Athey, S., Chetty, R., Imbens, G. y Kang, H., "The Surrogate Index", NBER WP 26463. https://www.nber.org/papers/w26463
- Chou, W., "Blending Proxy Metrics with a North Star", arXiv:2606.21745, 2026. https://arxiv.org/abs/2606.21745
- Sigerson et al., "Evaluating for the long term: Learnings from industry", arXiv:2608.08043, 2026. https://arxiv.org/abs/2608.08043
- Deng, A., Xu, Y., Kohavi, R. y Walker, T., CUPED, WSDM 2013. https://exp-platform.com/cuped/
- Johari, R. et al., "Always Valid Inference", arXiv:1512.04922. https://arxiv.org/abs/1512.04922
- Deng, A., Lu, J. y Chen, S., "Continuous Monitoring of A/B Tests without Pain", arXiv:1602.05549. https://arxiv.org/abs/1602.05549
- Robinson, D., "Is Bayesian A/B Testing Immune to Peeking? Not Exactly", 2015-08-21. http://varianceexplained.org/r/bayesian-ab-testing/
- Argyle, L. et al., "Out of One, Many", *Political Analysis*, 2023, arXiv:2209.06899. https://ar5iv.labs.arxiv.org/html/2209.06899
- Bisbee, J. et al., "Synthetic Replacements for Human Survey Data?", *Political Analysis*, 2024. https://www.cambridge.org/core/product/B92267DC26195C7F36E63EA04A47D2FE
- Kuric, E., Demcak, P. y Krajcovic, M., "What Would GPT Click", arXiv:2605.18302, 2026. https://arxiv.org/abs/2605.18302
