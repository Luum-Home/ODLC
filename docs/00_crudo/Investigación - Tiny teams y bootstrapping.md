---
tags: [crudo, investigacion, tiny-teams]
status: crudo
created: 2026-10-08
---

# Investigación: tiny teams y bootstrapping

Pregunta: el dueño del vault fijó dos públicos objetivo, (1) empresas que achican equipos a "tiny teams" apoyados en agentes y (2) emprendedores que arman un MVP con sus suscripciones de IA, sin capital externo, escuchando a clientes potenciales, y que forman equipo recién cuando necesitan escalar. Fijó también una condición: todo lo que proponga el marco tiene que ser demostrable. Este relevamiento busca qué evidencia existe para esos dos públicos y qué cambia en el marco. Insumos del vault: HACS-ODLC (mapa de contenido), Objeciones al marco y Modelo de madurez AI-Native (06_fundacional), Roles humanos y Gobernanza (02_hacs) y la sección de huecos de "Síntesis - Cómo encajan las propuestas existentes" (00_crudo). Fuentes consultadas el 2026-10-08.

Convención de evidencia (la misma de la Síntesis): **[medido]** = estudio con comparación, ensayo o panel con estrategia de identificación; **[medido, otro dominio]** = medido fuera del software o de la organización humano-agente; **[guía]** = estándar o recomendación de un organismo, sin evaluación de resultados; **[testimonio]** = relato de quien lo aplicó, dato autodeclarado o encuesta; **[opinión]** = argumento o marco conceptual sin medición propia.

## Resumen

1. Hay evidencia medida de que las startups con IA son más chicas: 25 % menos empleados en Y Combinator y 12 % menos en PitchBook (Kim y Koning, 2026, correlacional), y ~8 % menos empleo en las más expuestas tras ChatGPT (Gupta y otros, 2026, 94.789 startups). Que produzcan como equipos grandes no está medido. Solo hay ingresos autodeclarados.
2. "Tiny teams" como etiqueta lo popularizó Shawn Wang (swyx, Latent Space), que lo define como equipos con más millones de ARR que empleados (julio de 2025). Antes estaba la apuesta de Sam Altman sobre la empresa de una persona y mil millones (2023). Las listas de ingresos por empleado (Henry Shi) seleccionan por el mismo resultado que muestran.
3. Las críticas pesan: el ARR de las startups de IA suele ser una proyección del consumo de tokens ("vibe revenue"), los casos se eligen entre los que sobrevivieron (Pieter Levels: más de 70 intentos, 4 rentables) y el tiny team suele ser una fase, no un estado: Cursor pasó a ~300 personas.
4. Sobre bootstrapping contra capital de riesgo, el dato serio (Puri y Zarutskie, 2012) dice que las firmas con VC fallan menos los primeros cinco años y más después, crecen más y no son más rentables al salir. Las cifras de "supervivencia doble del bootstrapping" que circulan no tienen fuente primaria.
5. El enfoque científico tiene ensayos aleatorizados: Camuffo y otros (116 startups, 2020) y su réplica (759 firmas, cuatro RCT, 2024). El efecto que se replica es abandonar más ideas malas. Los ensayos de Bailey y otros (553 startups, 2026) y Germann y otros (1.024 emprendedores, 2026) apuntan en la misma dirección.
6. Customer development (Blank), The Mom Test (Fitzpatrick) y el pretotyping (Savoia) no publican evaluación propia. Sus páginas muestran testimonios y adopción en universidades, no datos.
7. Con muestras chicas sí hay métodos con base: preventas y señales de pago (Xu: 50 % más compromisos de pago se asocian con 9 % más probabilidad de comercializar), pruebas con 5 usuarios para usabilidad (Nielsen), y diseños de caso único con estándares explícitos (What Works Clearinghouse). Los priors bayesianos "objetivos" exigen miles de experimentos previos (Deng, 2015). Un emprendedor no los tiene.
8. Los usuarios simulados con LLM sirven como filtro, no como validación. Fallan justo en categorías nuevas (Brand y otros), aplanan grupos demográficos (Wang y otros) y, cuando aciertan (Park y otros, 2024), es porque se construyeron con entrevistas de dos horas a las personas reales.
9. Con una a tres personas, la separación de funciones se rompe por construcción. COSO (2006) acepta controles compensatorios: revisión de reportes, muestreo de transacciones y conciliaciones. GitHub deja por defecto que los administradores se salten la protección de ramas. Un agente como revisor tiene sesgo hacia lo que él mismo produce (Panickssery y otros, 2024).
10. Para pasar de fundador solo a equipo, el estudio más fuerte es el Stanford Project on Emerging Companies: cambiar el modelo de organización inicial triplicó la tasa de falla y subió la rotación de los más antiguos. Lo que se diseña al principio pesa, y cambiarlo cuesta.
11. Los consejos de pares que promueven prácticas formales (reuniones regulares, metas, feedback) dieron firmas 28 % más grandes y 10 puntos menos de falla (Chatterji y otros, 2019, RCT con 100 firmas). Es lo más cercano a evidencia de qué proceso introducir al crecer.
12. Para n = 1, una dinámica de trabajo se puede demostrar con diseños de caso único (tres demostraciones del efecto y al menos 5 puntos por fase), preregistro y métricas calculadas del repo. Generalizar al marco exige al menos 5 estudios de 3 equipos distintos con 20 experimentos en total. Una persona sola demuestra su caso, no el marco.

---

## 1. Tiny teams: qué evidencia hay

### Quién acuñó o popularizó el término

- **Sam Altman (2023).** Contó que en un grupo de chat con otros CEO tenían una apuesta sobre el año en que aparecería la primera empresa de una persona valuada en mil millones. La cita aparece en la nota 1 de Gupta y otros (2026), que también remite a The Economist (2025-08-11). [opinión]
- **Shawn Wang (swyx), "The Tiny Teams Playbook", Latent Space, 2025-07-15.** Define tiny teams como equipos con más millones de ARR que empleados. Resume un track del AI Engineer World's Fair: 7 equipos encuestados con ~100 empleados y ~200 millones de dólares de ARR entre todos; Bolt.new, 20 millones de ARR en 60 días con 15 personas. Las recomendaciones (generalistas senior, períodos de prueba pagos, pocas reuniones, automatizar soporte con IA) salen de entrevistas a equipos elegidos por el curador. [testimonio]
- **Henry Shi, Lean AI Native Companies Leaderboard.** Criterios: más de 5 millones de dólares de ARR, menos de 50 empleados, menos de 5 años de antigüedad, con excepciones para quienes superan 1 millón de ARR por empleado. Los datos combinan registros públicos, anuncios y confirmación de los fundadores. Jeremiah Owyang (2025-05-13) promedió el top 10 de esa lista: 3,48 millones de dólares de ingreso por empleado con 24 empleados en promedio, contra 610.668 dólares del top 10 de SaaS tradicional. Sin Midjourney, 2,47 millones. [testimonio, datos autodeclarados]

**Calidad como evidencia:** la lista entra por ingresos altos con pocos empleados y después muestra que hay ingresos altos con pocos empleados. Selecciona por la variable dependiente. La comparación de Owyang enfrenta a los mejores de un grupo con incumbentes de ~21.000 empleados, y él mismo admite que el cociente es difícil de medir con precisión.

### Lo medido

- **Kim (INSEAD) y Koning (HBS), "AI-Native Firms", SSRN, junio de 2026** (leído a través de la nota de HCAmag del 2026-07-20; SSRN devolvió 403). Usaron ~2.900 startups de Y Combinator (2020–2024) y decenas de miles de PitchBook, cruzadas con datos laborales de Revelio Labs. Las startups con IA en el producto son 25 % más chicas en YC y 12 % en PitchBook, tienen ~15 % menos gerentes y alrededor de medio nivel jerárquico menos. Los autores aclaran que el resultado es correlacional. [medido, observacional]
- **Gupta, Qian, Simintzi y Sun, "Generative AI and Entrepreneurship", 2026-04-14** (versión de conferencia NBER). Es un panel trimestral de 94.789 startups estadounidenses fundadas entre 2018 y 2021 (Crunchbase y PitchBook), que usa el lanzamiento de ChatGPT como shock. Las startups más expuestas redujeron empleo en dos trimestres, sobre todo en roles junior y de implementación, y escalaron más rápido. El empleo agregado no cambió porque se crearon más firmas. Según la nota de UNC (2026-02-12), el recorte fue de ~8 %, las primeras rondas fueron ~12 % más chicas y hubo ~7 % más startups activas en los sectores expuestos. [medido, cuasi-experimental]

### Casos con números y por qué no alcanzan

- **Cursor (Anysphere).** Según Wikipedia, con fuentes periodísticas: 100 millones de ARR en enero de 2025, 500 millones en junio de 2025, más de 1.000 millones en noviembre de 2025 y 3.000 millones en mayo de 2026, con ~300 empleados en agosto de 2025 (Fortune). [testimonio vía prensa] El caso emblema del tiny team dejó de ser chico al escalar.
- **Pieter Levels (Photo AI).** Fundador solo, sin capital externo. Ingresos autodeclarados en redes de 132.000 dólares mensuales; según la misma nota (ppc.land, 2025-05-25), lanzó más de 70 proyectos y 4 fueron rentables. [testimonio] Es el ejemplo más citado del público 2 y, a la vez, el que mejor muestra el sesgo de supervivencia.
- **Stripe, carta anual 2024 (2025-02-27).** Cita a Lovable (17 millones de ARR en 3 meses) y a Bolt (20 millones en 2 meses), y dice que sus datos muestran a las startups de IA creciendo a ritmo récord. [testimonio de proveedor] La comparación de meses hasta 5 millones de ARR contra el SaaS de 2018, que circula en prensa, está en un gráfico de la carta que no se pudo extraer como texto. No se usa.

### Críticas

- **ARR inflado.** MediaNama (abril de 2026) documenta el caso Emergent, que anunció 100 millones de ARR en 8 meses el 2026-02-17. El ARR de varias plataformas de "vibe coding" es una extrapolación del consumo reciente de tokens, no ingreso contratado. Chaitanya Chokkareddy lo llamó "vibe revenue run rate". [opinión, con un caso documentado] Para el marco, el ingreso por empleado es una métrica expuesta a Goodhart, igual que las de la Objeción 1.
- **Sesgo de supervivencia.** Ninguna fuente sobre tiny teams publica el denominador: cuántos equipos chicos con IA lo intentaron y fracasaron. El caso Levels lo hace visible por accidente.
- **Gupta y otros** muestran que el achique por firma convive con más firmas. El tiny team describe la unidad, no la economía.

## 2. Bootstrapping contra capital de riesgo, y la evidencia de los métodos

### Supervivencia y resultados

- **Puri y Zarutskie, Journal of Finance, 2012** (NBER w14250, 2008). Usaron datos del Census de EE. UU. que siguen firmas desde su nacimiento durante dos décadas, con firmas sin VC emparejadas. Las firmas con VC fallan menos en los primeros cinco años y, si sobreviven, fallan más que las demás después. Son más grandes en todas las etapas y no son más rentables al salir. [medido, observacional] La comparación no aísla el efecto del capital: el VC elige a quién financiar.
- **Paul O'Brien (2026-04-21)** argumenta que las estadísticas de supervivencia del bootstrapping mezclan negocios de modelo conocido (panaderías, servicios) con startups que buscan un modelo escalable, y que la ventaja desaparece al separarlos. [opinión] Las cifras de "el bootstrapping sobrevive el doble" que devolvió la búsqueda no traían estudio primario y no se usan.
- **Carta, Founder Ownership Report 2025** (vía Funds Society, 2025-03-21; carta.com devolvió 403): sobre más de 45.000 startups de 2015 a 2024, el 35 % de las nuevas de 2024 tuvo un fundador solo, contra el 17 % en 2017, y esas firmas fueron el 17 % de las que cerraron rondas de VC. [medido, descriptivo, solo clientes de Carta]

### Customer development, The Mom Test y Lean Startup

- **Steve Blank** define a una startup como "una organización formada para buscar un modelo de negocio repetible y escalable" (blog, 2010-01-25). El customer development es su método para probar cada componente del modelo, y Eric Ries lo combinó con desarrollo ágil bajo el nombre Lean Startup. [opinión]
- **Rob Fitzpatrick, The Mom Test.** La página del libro no presenta datos: muestra testimonios (Seedcamp, John Mullins) y su uso en el currículo de Harvard y UCL. [testimonio] No se encontró ninguna evaluación empírica de sus reglas.
- **Alberto Savoia, The Right It (pretotyping, desarrollado en Google en 2010).** Dice haberse aplicado "con gran éxito en cientos de proyectos", sin datos en la página. [testimonio]
- **Shepherd y Gruber, Entrepreneurship Theory and Practice, 2020.** Revisan los cinco bloques de Lean Startup y concluyen que la investigación académica va detrás de la práctica. [opinión, revisión]
- **Felin, Gambardella, Stern y Zenger, Long Range Planning, 2020.** Critican a Lean Startup porque no guía cómo generar hipótesis, el feedback de clientes tiene límites como fuente de aprendizaje y la experimentación tiende a dar resultados incrementales. Proponen una "visión basada en teoría". [opinión]

### Ensayos de campo: enfoque científico contra intuición

| Estudio | Diseño | Resultado | Tipo |
|---|---|---|---|
| Camuffo, Cordova, Gambardella y Spina, *Management Science*, 2020 | RCT, 116 startups italianas, 16 mediciones en ~1 año; ambos grupos reciben 10 sesiones de feedback de mercado, el tratado aprende a formular y testear hipótesis | Mejor desempeño, más pivotes y la misma tasa de abandono temprano. Lectura de los autores: el método reduce falsos positivos | [medido] |
| Camuffo, Gambardella, Messinese, Novelli, Paolucci y Spina, *Strategic Management Journal*, 2024 (réplica) | 759 firmas, cuatro RCT | Más abandono de ideas. Efecto no lineal en pivotes radicales: los tratados hacen pocos, ni ninguno ni muchos. El resumen no reporta efecto sobre ingresos | [medido] |
| Bailey, Fehder, Floyd, Hochberg y Lee, NBER w34755, 2026-01 | RCT, 553 startups de ciencia y tecnología en 12 espacios de coworking de EE. UU.; capacitación intensiva corta (método no especificado en el resumen) | Los tratados cierran más y antes; los que sobreviven levantan más capital, más rápido, y tienen más empleo e ingresos | [medido] |
| Germann, Anderson, Espinosa-Balbuena y Narayanan, seminario HEC, 2026-03-13 | RCT, 1.024 emprendedores en Uganda y Kenia; aceleradora Lean Startup de ~8 semanas | A dos años, 240 % más experimentos que el control; cada experimento adicional se asocia con más ventas y ganancias | [medido, otro contexto] |
| Leatherbee y Katila, SSRN 2017 | 152 equipos I-Corps (NSF), longitudinal | Los componentes del método (hipótesis, sondeo, convergencia) se encadenan como se espera; los miembros con MBA lo resisten | [medido, observacional] |
| Koning, Hasan y Chatterji, *Management Science*, 2022 | Adopción escalonada de herramientas de A/B testing en startups tecnológicas | Pocas lo adoptan; las que lo adoptan mejoran 30–100 % al año | [medido, observacional] |
| Avdeenko, Frölich y Helmsmüller, CEPR DP 16265, 2021 | RCT, 3.975 microemprendedores en Indonesia, capacitación general | Sin efecto en ganancias ni ventas | [medido, otro contexto] |

**Lectura:** el resultado que se repite entre ensayos es abandonar antes lo que no funciona, no ganar más. Encaja con un ciclo que registra los objetivos fallidos como aprendizaje (candidato de respuesta a la Objeción 1). El A/B testing de Koning y otros supone tráfico, que el público 2 no tiene.

## 3. Validar con poco tráfico o pocos clientes

Es el hueco "feedback con poco tráfico" de la Síntesis. Métodos con fuente, ordenados por cuánto compromiso del cliente exigen.

| Método | Qué decide | Respaldo | Límite |
|---|---|---|---|
| Entrevistas de descubrimiento | Qué problemas y necesidades existen | Griffin y Hauser (*Marketing Science*, 1993) estudian cuántos clientes hay que entrevistar y cuántas necesidades se pierden; el resumen plantea la pregunta, la cifra no se pudo verificar (el PDF del MIT pide CAPTCHA) [medido, otro dominio] | Detecta necesidades, no disposición a pagar. Fitzpatrick advierte sobre las respuestas complacientes, sin datos propios |
| Pruebas de usabilidad con 5 usuarios | Problemas de uso | Nielsen (2000), con el modelo de Nielsen y Landauer (1993): con una tasa de descubrimiento típica de 31 % por usuario, 5 usuarios encuentran ~85 % de los problemas [medido] | Vale para grupos homogéneos; con grupos distintos hacen falta 3 o 4 por grupo. No mide demanda |
| Preventas y compromisos de pago (crowdfunding, smoke test) | Demanda con algo en juego | Xu ("Learning from the Crowd"; nota de Darden, 2018-03-30): de 262 emprendedores de Kickstarter, el 63 % usó la campaña para medir demanda. En proyectos no financiados, 50 % más compromisos de pago se asocian con 9 % más probabilidad de comercializar [medido, observacional] | Mide la intención en una plataforma con su propia audiencia. No hay estudio que valide smoke tests o "fake doors" en B2B |
| Pretotipo y MVP conserje | Si la propuesta de valor se sostiene antes de construir | Savoia, Ries [testimonio] | Sin evaluación publicada |
| Inferencia bayesiana con prior | Decidir con pocos datos usando conocimiento previo | Deng (Microsoft, WWW 2015) aprende el prior de miles de experimentos de Bing [medido] | El prior "objetivo" exige un historial que el público 2 no tiene. Un prior subjetivo es posible, pero no está validado para este uso |
| Diseños de caso único | Si una intervención cambia una conducta en una unidad | What Works Clearinghouse (Kratochwill y otros, 2010): estándares explícitos; ver sección 6 [guía] | Pensados para conducta individual, no para mercados |
| Usuarios simulados con LLM | Filtrar ideas antes de exponerlas | Park y otros (arXiv 2411.10109): agentes construidos con entrevistas de 2 h a 1.052 personas reproducen la Encuesta Social General con 83–86 % de la consistencia que esas personas tienen consigo mismas dos semanas después, contra 74 % de los agentes armados solo con datos demográficos [medido] | Necesita entrevistar primero a las personas reales. Brand, Israeli y Ngwe (SSRN 2023; EC 2024): la disposición a pagar estimada con LLM es "a menudo inexacta" y a veces de signo contrario; el ajuste fino con encuestas previas mejora dentro de la categoría, no en categorías nuevas [medido]. Wang, Morgenstern y Dickerson (arXiv 2402.01908; 3.200 participantes, 16 identidades, 4 LLM): los LLM representan mal y aplanan a los grupos demográficos [medido]. Hut y Masoero (ya en el vault): aciertan el signo en 70 % y exageran la magnitud |

**Lectura:** con pocos clientes, la evidencia más fuerte es la que cuesta algo al cliente (pago, compromiso, tiempo). El método más barato, el usuario simulado, falla donde más se lo usaría: con productos nuevos para gente que todavía no se entrevistó.

## 4. Una persona con todos los roles

El vault supone que los cuatro roles humanos (Sponsor, Product, Architect, Operator) "pueden ser menos de cuatro personas", y Gobernanza pide aprobación humana para lo irreversible. Con una persona, quien ejecuta y quien valida son la misma. Propuestas existentes:

- **Controles compensatorios (COSO, *Internal Control over Financial Reporting — Guidance for Smaller Public Companies*, 2006; resumen de Cooley).** COSO reconoce que las empresas chicas no tienen gente para separar funciones y que la dirección puede saltarse los controles. Propone que quien dirige revise los reportes de transacciones, elija transacciones al azar para revisar su respaldo, haga conteos y revise conciliaciones. [guía] Traducido al vault: muestreo de lo que hizo el agente contra evidencia, en vez de aprobar cada acción.
- **Herramientas que lo dejan pasar por defecto.** GitHub permite exigir que el último push lo apruebe alguien distinto de quien lo hizo, pero por defecto la protección de ramas no aplica a los administradores, salvo que se active "Do not allow bypassing the above settings". [guía, documentación] Una persona sola que es administradora no tiene segundo par de ojos salvo que se ate las manos explícitamente.
- **El agente como segundo par de ojos.** Panickssery y otros (arXiv 2404.13076, 2024): los LLM reconocen sus propios textos y los puntúan mejor; la fuerza del sesgo crece con la capacidad de autorreconocerse. [medido] El crudo "Propuestas existentes - Revisión en manos de agentes" (00_crudo) ya relevó que modelos de proveedores distintos se equivocan parecido (Kim y otros, ICML 2025). Un agente revisor reduce el riesgo, pero no es independiente.
- **Asesores y pares externos.** Chatterji, Delecourt, Hasan y Koning (*Strategic Management Journal*, 2019): RCT con 100 firmas tecnológicas de alto crecimiento en India. Quienes recibieron consejos de pares con gestión formal crecieron 28 % más y tuvieron 10 puntos menos de probabilidad de fallar a dos años. Quienes tenían MBA o venían de aceleradoras no respondieron. [medido] Hasan y Koning (*SMJ*, 2019): en un bootcamp, una desviación estándar más de desempeño de los equipos vecinos se asoció con dos tercios de desviación estándar más en la calidad del prototipo, solo en equipos sin vínculos previos. [medido] Hay evidencia de que el par externo influye. No la hay de que funcione como validador independiente de lo irreversible.
- **Concentrar la aprobación humana en lo irreversible** (IMDA, ya en Objeciones al marco, principio 5). Con una persona, la regla "dos personas para lo irreversible" exige que la segunda sea externa (asesor, cliente, par) o que se acepte la excepción por escrito.

**Lectura:** ninguna fuente propone una separación de funciones que funcione con una sola persona. Las alternativas son controles compensatorios por muestreo, revisores externos solo para lo irreversible y agentes revisores sabiendo que no son independientes. La que más se acerca a un validador externo en el público 2 es el cliente que paga (sección 3).

## 5. De fundador solo a equipo

- **Stanford Project on Emerging Companies (SPEC).** Baron, Hannan y Burton (*American Journal of Sociology*, 2001): en startups de alta tecnología, cambiar el modelo de empleo de los fundadores aumentó la rotación, concentrada en los empleados más antiguos, y la rotación empeoró el desempeño. [medido, observacional] Según Stanford GSB (2007), sobre más de 150 startups de Silicon Valley: las que cambiaron el modelo inicial tuvieron el triple de probabilidad de fallar y valuaciones casi seis veces menores, y los modelos burocrático y autocrático tuvieron las peores tasas de falla. Baron y Hannan (*California Management Review*, 2002) concluyen que las decisiones iniciales de organización tienen efectos duraderos. [medido, observacional]
- **Chatterji y otros (2019),** sección 4: reuniones regulares, metas consistentes y feedback frecuente, transmitidos por pares, se asociaron con más crecimiento y menos falla. [medido] Es lo más cercano a "qué procesos introducir".
- **Hellmann y Puri (SSRN 2000):** en startups de Silicon Valley, las que tienen VC profesionalizan antes su gestión de personas y traen antes un CEO de afuera. [medido, observacional]
- **Startup Genome, "premature scaling" (v1.2, marzo de 2012; encuesta a más de 3.200 startups).** Dice que el 74 % de las startups de internet de alto crecimiento falla por escalar antes de tiempo, que las que escalan prematuramente tienen equipos 3 veces más grandes en la misma etapa y que las que escalan bien tardan 76 % más en llegar a su tamaño de equipo. [testimonio: encuesta autoadministrada; la atribución causal no surge del diseño]
- **Kim y Koning (2026)** y **Gupta y otros (2026),** sección 1: las startups con IA contratan menos gerentes y menos juniors. La primera contratación del público 2 tiende a ser un senior. [medido, correlacional]

**Lectura:** no hay umbral medido de cuándo contratar. Lo que hay es evidencia de que cambiar el modelo de organización a mitad de camino cuesta. Para el marco, conviene que la forma de trabajo de una persona ya tenga las costuras por donde entra la segunda: roles como funciones con dueño explícito, aunque el dueño sea el mismo, y evidencia en el repo y no en la cabeza del fundador. Es una inferencia de este documento a partir de SPEC, no un resultado de SPEC.

## 6. Demostrar con n chico

- **Estándares de diseño de caso único (What Works Clearinghouse, Kratochwill, Hitchcock, Horner, Levin, Odom, Rindskopf y Shadish, 2010).** [guía]
  - Hacen falta al menos tres demostraciones del efecto en tres momentos distintos. AB, ABA y BAB no alcanzan.
  - Un diseño de reversión ABAB necesita cuatro fases con al menos 5 puntos cada una (3 o 4 puntos lo aceptan "con reservas").
  - Si el efecto no se puede revertir, corresponde una línea de base múltiple (mínimo seis fases), no ABAB. Es el caso típico de una forma de trabajo: lo aprendido no se desaprende.
  - Para generalizar una intervención piden al menos 5 estudios, de 3 equipos de investigación en 3 lugares, con 20 experimentos en total. Los propios autores aclaran que esos umbrales son convenciones profesionales.
- **Análisis visual.** Ninci, Vannest, Willson y Zhang (*Behavior Modification*, 2015): metaanálisis de 19 artículos y 32 efectos, con un acuerdo entre analistas de 0,76. [medido] Mirar el gráfico no alcanza; existen tests de aleatorización para casos únicos (Heyvaert y Onghena, *Journal of Contextual Behavioral Science*, 2014, revisión del estado del arte).
- **Ensayos N-of-1 y preregistro.** CENT 2015 (BMJ) es la guía de reporte de ensayos N-of-1; los Registered Reports (Chambers, *Cortex*, 2013) fijan hipótesis y análisis antes de ver los datos. [guía] Ya están en el núcleo de las tres combinaciones de la Síntesis.
- **Autoexperimentación.** Seth Roberts (*Behavioral and Brain Sciences*, 2004) presenta 12 años de autoexperimentos como fuente de ideas nuevas, no como prueba. [testimonio] Es el límite honesto del caso n = 1: genera hipótesis de buena calidad y no demuestra generalidad.
- **Medir desde artefactos.** La investigación del vault sobre estimación ya registró que, con agentes en paralelo, METR no pudo medir el tiempo por tarea. Por eso las métricas tienen que salir de eventos con timestamp en el repo y el tracker (commits, PR, cierre de objetivo), calculadas por script, y no de autorreporte. El RCT de METR (2025) muestra cuánto se equivoca la percepción: los desarrolladores tardaron 19 % más con IA y creían haber ganado 20 %.

**Propuesta derivada (hipótesis de este documento, no hallada aplicada a trabajo de software):**

1. Línea de base múltiple a través de objetivos o proyectos de la misma persona.
2. Preregistro como commit fechado, con hipótesis, métrica, script de cálculo y criterio de abandono.
3. Al menos 5 puntos por fase y test de aleatorización en vez de análisis visual.
4. La afirmación "el marco funciona" recién con 3 operadores distintos.

Cumple la condición del dueño ("demostrable") en el nivel del caso y la deja explícitamente pendiente en el nivel del marco.

---

## Hallazgo → parte del vault

| Hallazgo | Parte del vault | Efecto |
|---|---|---|
| Startups con IA 12–25 % más chicas, con menos gerentes y juniors (Kim y Koning; Gupta y otros) | Roles humanos, Modelo de madurez | **Igual**: respalda la premisa de unidades chicas; no prueba que produzcan como equipos grandes |
| El ingreso por empleado de los tiny teams se basa en datos autodeclarados, seleccionados por el resultado, con ARR proyectado | Métricas (Métricas de agentes, Human Leverage Ratio) | **Contradice** usar ingreso o ARR por persona como métrica del marco: Goodhart, igual que la Objeción 1 |
| El tiny team suele ser una fase (Cursor llegó a ~300 personas) | Modelo de madurez | **Contradice** un modelo pensado solo para "organizaciones": falta el recorrido de una persona a un equipo |
| VC: menos fallas los primeros 5 años y más después; no más rentables (Puri y Zarutskie) | Fases (Fase 1, Fase 2 como restricción de capital) | **Igual**: ninguna vía tiene ventaja probada; el capital entra como restricción del objetivo |
| El efecto replicado del enfoque científico es abandonar ideas malas antes (Camuffo 2020 y 2024; Bailey y otros 2026) | Fases (Fase 1, Fase 6), Objeción 1 | **Simplifica**: respalda que un objetivo con hipótesis y criterio de abandono funciona, y que el objetivo fallido cuente como aprendizaje |
| Mom Test, customer development y pretotyping sin evaluación propia | Fases (Fase 1, Fase 5) | **Igual**: usables como técnica, no como evidencia |
| Con pocos clientes, el compromiso de pago es la señal más fuerte (Xu) | Fases (Fase 5), Objeción 2 | **Simplifica**: indicador temprano y validador externo a la vez para el público 2 |
| Priors bayesianos "objetivos" exigen miles de experimentos (Deng) | Métricas operativas (pronóstico), Objeción 2 | **Contradice** la idea de que un emprendedor decida bayesianamente "con datos": el prior será subjetivo y hay que declararlo |
| Los usuarios simulados con LLM fallan en categorías nuevas y aplanan grupos | Fases (Fase 5), hueco de la Síntesis | **Igual**: confirma "filtrar, no validar" |
| Separación de funciones imposible con una persona; COSO propone controles por muestreo | Gobernanza, Roles humanos | **Contradice** "dos personas para lo irreversible" en el público 2; **simplifica** si se adopta muestreo compensatorio más un validador externo solo para lo irreversible |
| GitHub deja a los administradores saltarse la protección por defecto | Gobernanza (process-as-code) | **Igual**: el control existe; hay que activarlo explícitamente |
| El agente revisor favorece lo suyo (Panickssery) y comparte errores con otros modelos | Gobernanza, Roles de agentes | **Contradice** usar un agente como segundo par de ojos independiente para lo irreversible |
| Los consejos de pares con gestión formal mejoran crecimiento y supervivencia (Chatterji) | Roles humanos, Objeción 5 | **Simplifica**: un asesor externo es una pieza con evidencia para el humano solo |
| Cambiar el modelo organizacional inicial triplica la falla (SPEC) | Modelo de madurez (transiciones), Manifiesto (adaptación por madurez) | **Contradice** en parte la adopción por niveles: cada salto de nivel es un cambio de modelo con costo medido; conviene diseñar las costuras desde el día uno |
| Diseños de caso único con estándares explícitos; generalizar exige 5 estudios de 3 equipos con 20 experimentos | Objeción 3, Métricas | **Simplifica** la demostración para n = 1; **contradice** cualquier afirmación general basada en un solo caso (Caso - Alta Tienda incluido) |
| D1 fija el Nivel 3 como mínimo para un piloto | Modelo de madurez | **Igual** para el público 1; para el público 2, el repo con memoria versionada ya es el Nivel 3, sin infraestructura aparte (inferencia, no medida) |

## Huecos

| Hueco | Lo más cercano | Por qué no alcanza |
|---|---|---|
| Productividad medida de fundadores solos o equipos de 1 a 3 con agentes | Kim y Koning; Gupta y otros | Miden tamaño y financiamiento, no producción ni calidad por persona |
| Denominador de los tiny teams (cuántos lo intentaron y fallaron) | Caso Levels (70 intentos, 4 rentables) | Anécdota autodeclarada |
| Evaluación empírica de The Mom Test, smoke tests y MVP conserje | Xu (crowdfunding) | Otra plataforma y otra audiencia; nada en B2B ni en software de nicho |
| Réplica del efecto sobre ingresos del enfoque científico | Camuffo 2020 (sí); réplica 2024 (el resumen solo reporta abandono y pivotes) | Falta leer el texto completo de la réplica |
| Revisión diferida por la misma persona (revisar en frío lo propio) como sustituto de la segunda persona | Nada encontrado | Sin propuesta ni evidencia |
| Asesor externo como validador de lo irreversible | Chatterji; Hasan y Koning | Miden influencia del consejo, no control |
| Cuándo contratar a la primera persona | Startup Genome (encuesta); SPEC | Sin umbral medido; Carta publica días hasta la primera contratación, pero el informe devolvió 403 y no se usa |
| Diseños de caso único aplicados a dinámicas de trabajo de software | WWC, CENT, Roberts | Ninguno en software; la propuesta de la sección 6 no está probada |
| Prior subjetivo declarado para decisiones de producto con n chico | Deng (prior objetivo) | Sin validación del uso subjetivo |
| La cifra de Griffin y Hauser sobre cuántas entrevistas alcanzan | Resumen de *Marketing Science*, 1993 | El texto completo pide CAPTCHA; no se verificó |
| Meses hasta 5 millones de ARR, IA contra SaaS (Stripe) | Carta anual 2024 | El dato está en un gráfico no extraíble; no se usa |

## Fuentes (todas consultadas el 2026-10-08)

Abiertas y usadas:

- Wang, S. (swyx), "The Tiny Teams Playbook", Latent Space, 2025-07-15. https://www.latent.space/p/tiny
- Shi, H., Lean AI Native Companies Leaderboard (criterios y método). https://leanaileaderboard.com/
- Owyang, J., "AI Startups are Dominating Traditional Software in one Key Metric", 2025-05-13. https://web-strategist.com/blog/2025/05/13/ai-startups-are-dominating-traditional-software-in-one-key-metric/
- Gupta, A., Qian, F., Simintzi, E. y Sun, Y., "Generative AI and Entrepreneurship", 2026-04-14. https://conference.nber.org/conf_papers/f232872.pdf
- UNC Kenan-Flagler, "Generative AI is changing how startups scale", 2026-02-12. https://www.kenan-flagler.unc.edu/news/generative-ai-is-changing-how-startups-scale/
- HCAmag, "Will AI-native firms require fewer workers?" (sobre Kim y Koning, "AI-Native Firms"), 2026-07-20. https://www.hcamag.com/ca/specialization/transformation/will-ai-native-firms-require-fewer-workers/582971
- Wikipedia, "Cursor (company)" (cifras con fuentes periodísticas). https://en.wikipedia.org/wiki/Cursor_(company)
- MediaNama, "Explained: Emergent's $100 million ARR claim", 2026-04. https://www.medianama.com/2026/04/223-explained-emergent-100-million-arr-claim-ai-startups-revenue/
- Rijo, L., "How one photo AI app generates $132K monthly after 70 failed startups", ppc.land, 2025-05-25. https://ppc.land/how-one-photo-ai-app-generates-132k-monthly-after-70-failed-startups/
- Stripe, carta anual 2024, 2025-02-27. https://stripe.com/annual-updates/2024
- Puri, M. y Zarutskie, R., NBER w14250 (2008); Journal of Finance 67(6), 2012. https://www.nber.org/papers/w14250
- O'Brien, P., "Bootstrapped startups don't win more often", 2026-04-21. https://seobrien.com/bootstrapped-startups-dont-win-more-often-youre-reading-the-data-wrong
- Funds Society, sobre Carta Founder Ownership Report 2025, 2025-03-21. https://fundssociety.com/en/?p=268192
- Blank, S., "What's A Startup? First Principles", 2010-01-25. https://steveblank.com/2010/01/25/whats-a-startup-first-principles/
- Fitzpatrick, R., The Mom Test (página del libro). https://www.momtestbook.com/
- Savoia, A., Pretotyping. https://www.pretotyping.org/
- Camuffo, A. y otros, *Management Science*, 2020, doi:10.1287/mnsc.2018.3249 (resumen vía Crossref). https://api.crossref.org/works/10.1287/mnsc.2018.3249
- Camuffo, A. y otros, *Strategic Management Journal* 45(6), 2024, doi:10.1002/smj.3580 (resumen vía Crossref). https://api.crossref.org/works/10.1002/smj.3580
- Gambardella, A. y otros, Innovation Growth Lab, 2018-01-24. https://www.innovationgrowthlab.org/blog/what-are-effects-scientific-approach-entrepreneurial-experimentation
- Bailey, E., Fehder, D., Floyd, E., Hochberg, Y. y Lee, D. J., "Learning to Quit?", NBER w34755, 2026-01. https://www.nber.org/papers/w34755
- HEC Paris, seminario de Frank Germann (Germann, Anderson, Espinosa-Balbuena y Narayanan), 2026-03-13. https://www.hec.edu/fr/faculte-et-recherche/evenements/frank-germann-campus-room-t037
- Leatherbee, M. y Katila, R., SSRN 2017, doi:10.2139/ssrn.2902869 (resumen vía Crossref).
- Koning, R., Hasan, S. y Chatterji, A., *Management Science*, 2022, doi:10.1287/mnsc.2021.4209 (resumen vía Crossref).
- Avdeenko, A., Frölich, M. y Helmsmüller, S., CEPR DP 16265, 2021. https://ideas.repec.org/p/cpr/ceprdp/16265.html
- Shepherd, D. y Gruber, M., *Entrepreneurship Theory and Practice*, 2020, doi:10.1177/1042258719899415 (resumen vía Crossref).
- Felin, T., Gambardella, A., Stern, S. y Zenger, T., *Long Range Planning*, 2020, doi:10.1016/j.lrp.2019.06.002 (contenido según el resumen del repositorio del MIT). https://dspace.mit.edu/handle/1721.1/134124
- Griffin, A. y Hauser, J., "The Voice of the Customer", *Marketing Science*, 1993, doi:10.1287/mksc.12.1.1 (solo el resumen).
- Nielsen, J., "Why You Only Need to Test with 5 Users", 2000-03-18. https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/
- Murray, S., "Crowdfunding: Beyond Financing" (sobre Ting Xu), Darden, 2018-03-30. https://news.darden.virginia.edu/crowdfunding-beyond-financing
- Deng, A., "Objective Bayesian Two Sample Hypothesis Testing for Online Controlled Experiments", WWW 2015. https://exp-platform.com/objective-bayesian-ab/
- Park, J. S. y otros, "Generative Agent Simulations of 1,000 People", arXiv 2411.10109. https://arxiv.org/abs/2411.10109
- Brand, J., Israeli, A. y Ngwe, D., "Using LLMs for Market Research", SSRN 2023, doi:10.2139/ssrn.4395751 (resumen vía Crossref).
- Wang, Morgenstern y Dickerson, "Large language models that replace human participants can harmfully misportray and flatten identity groups", arXiv 2402.01908. https://arxiv.org/abs/2402.01908
- Kratochwill, T. R. y otros, *Single-Case Designs Technical Documentation*, What Works Clearinghouse, 2010. https://files.eric.ed.gov/fulltext/ED510743.pdf
- Ninci, J. y otros, *Behavior Modification*, 2015, doi:10.1177/0145445515581327 (resumen vía Crossref).
- Roberts, S., *Behavioral and Brain Sciences*, 2004, doi:10.1017/s0140525x04000068 (resumen vía Crossref).
- Cooley, "New COSO Guidance for Smaller Companies", 2006. https://www.cooley.com/news/insight/2006/new-coso-guidance-for-smaller-companies
- GitHub Docs, "About protected branches". https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- Panickssery, A. y otros, "LLM Evaluators Recognize and Favor Their Own Generations", arXiv 2404.13076, 2024. https://arxiv.org/abs/2404.13076
- Chatterji, A., Delecourt, S., Hasan, S. y Koning, R., *Strategic Management Journal*, 2019, doi:10.1002/smj.2987 (resumen vía Crossref).
- Hasan, S. y Koning, R., *Strategic Management Journal*, 2019, doi:10.1002/smj.3032 (resumen vía Crossref).
- Baron, J., Hannan, M. y Burton, M. D., "Labor Pains", *American Journal of Sociology*, 2001, doi:10.1086/320296 (resumen según el buscador y la ficha de la revista). https://www.journals.uchicago.edu/doi/10.1086/320296
- Stanford GSB, "Michael Hannan: Startups Need to Think About Employees From the Get-Go", 2007. https://www.gsb.stanford.edu/insights/michael-hannan-startups-need-think-employees-get-go
- Baron, J. y Hannan, M., *California Management Review* 44(3), 2002. https://cmr.berkeley.edu/2002/05/44-3-organizational-blueprints-for-success-in-high-tech-start-ups-lessons-from-the-stanford-project-on-emerging-companies
- Hellmann, T. y Puri, M., SSRN 2000, doi:10.2139/ssrn.243149 (resumen vía Crossref).
- Marmer, M., Herrmann, B. L., Dogrultan, E. y Berman, R., *Startup Genome Report Extra on Premature Scaling*, v1.2, marzo de 2012. https://startupgenome.com/report/why-startups-fail-premature-scaling/why-startups-fail-premature-scaling

Solo por título o referencia, sin leer el contenido (no se usan como dato): Heyvaert y Onghena (2014), doi:10.1016/j.jcbs.2013.10.002; CENT 2015, doi:10.1136/bmj.i5381; Chambers (2013), doi:10.1016/j.cortex.2012.12.016; Nielsen y Landauer (1993), doi:10.1145/169059.169166.

Bloqueadas (403 o CAPTCHA, sin dato usado): Carta, Solo Founders Report 2025 (https://carta.com/data/solo-founders-report); SSRN de Kim y Koning (https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6905079); Bloomberg, Dave Lee, 2026-04-16; Fast Company sobre ARR inflado; PDF del MIT de Griffin y Hauser.

Ya citadas en otros crudos del vault: Hut y Masoero (Investigación - Estimación y tiempo con agentes), METR 2025 (ídem), Kim y otros ICML 2025 (Propuestas existentes - Revisión en manos de agentes), IMDA v1.5 (Objeciones al marco).

## Comandos de verificación

Read-only. Reproducen los datos centrales desde la fuente.

```bash
# Réplica de Camuffo y otros: 759 firmas, cuatro RCT
curl -s https://api.crossref.org/works/10.1002/smj.3580 | grep -o "759 firms in four randomized control trials"
# Chatterji y otros: 28 % y 10 puntos
curl -s https://api.crossref.org/works/10.1002/smj.2987 | grep -o "grew 28% larger and were 10 percentage points less likely to fail"
# WWC: tres demostraciones y 5 puntos por fase
curl -sL -A "Mozilla/5.0" https://files.eric.ed.gov/fulltext/ED510743.pdf -o /tmp/wwc.pdf && pdftotext /tmp/wwc.pdf - | grep -n "at least three attempts\|at least 5 data points per phase"; rm -f /tmp/wwc.pdf
# Park y otros: 83 %, 82 %, 86 % contra 74 %
curl -s "https://export.arxiv.org/api/query?id_list=2411.10109" | tr "\n" " " | grep -o "83%, 82%, and 86%[^.]*74%"
# Gupta y otros: panel de 94.789 startups
curl -sL https://conference.nber.org/conf_papers/f232872.pdf -o /tmp/g.pdf && pdftotext /tmp/g.pdf - | grep -o "quarterly panel of 94,789 startups"; rm -f /tmp/g.pdf
# Startup Genome: 74 % y equipos 3 veces más grandes
curl -sL https://startupgenome.com/report/why-startups-fail-premature-scaling/why-startups-fail-premature-scaling -o /tmp/sg.pdf && pdftotext /tmp/sg.pdf - | grep -n "74% of high growth\|3 times bigger"; rm -f /tmp/sg.pdf
```
