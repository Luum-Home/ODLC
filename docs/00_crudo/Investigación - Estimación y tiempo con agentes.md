---
tags: [crudo, investigacion, estimacion]
status: crudo
created: 2026-10-07
---

# Investigación: estimación y tiempo cuando el trabajo lo ejecutan agentes

Pregunta: cuando el trabajo de software lo ejecutan agentes de IA, ¿tiene sentido estimar tiempo? ¿Qué se estima, qué se fija como tope y qué se pronostica? Fuentes consultadas el 2026-10-07. Convención: **[medido]** = dato observado en un estudio; **[autorreporte]** = encuesta o percepción; **[opinión]** = argumento o predicción sin medición propia.

## Resumen

1. Los LLM sobreestiman cuánto tardan ellos mismos: entre 4 y 7 veces antes de la tarea y entre 5 y 10 veces en tareas de varios pasos [medido, Garikaparthi 2026]. El sesgo existe, pero su tamaño cambia mucho según el modelo: de 1,16x a 9,9x en el mismo banco de pruebas [medido, Ofengenden y Andriushchenko 2026].
2. Dar feedback de calibración en contexto reduce el error, pero no se transfiere a tareas nuevas [medido, Garikaparthi 2026]. Eso respalda que un factor de corrección fijo es frágil.
3. El costo de ejecución tampoco se predice bien: la misma tarea puede consumir hasta 30 veces más tokens según la corrida, y los modelos predicen su propio consumo con correlación de 0,39 como máximo [medido, Bai et al. 2026]. Por eso tiene sentido ponerle un tope a la ejecución en vez de estimarla. La herramienta existe, pero es un tope blando [doc. Anthropic].
4. La estimación no desaparece, se corre de lugar: el formato de la especificación cambia el gasto un 29,7% [medido, Smékal 2026], y escribir la especificación es trabajo humano que sí hay que estimar [opinión, Jones 2026].
5. Al acelerarse la ejecución, el cuello de botella pasa a la revisión humana: el tiempo de revisión de PR subió 91% [medido, Faros 2025], los PR de agentes esperan entre 4,6 y 5,3 veces más hasta que alguien los toma [medido, LinearB 2026], y la ganancia se achica en cada etapa, de commits a releases [medido, Demirer et al. 2026].
6. En contra: en una empresa, la revisión automática superó a la humana y la cola se descongestionó porque los PR empezaron a saltear la revisión humana [medido, He et al. 2026]. La atención humana es escasa, pero también se la esquiva.
7. Productividad real con control: -19% en 2025 [medido, RCT METR]. Seguimiento 2026: posible aceleración, pero METR mismo dice que el dato no es confiable, en parte porque con agentes en paralelo no se puede medir el tiempo de cada tarea [medido con sesgo, METR 2026].
8. El "horizonte de tareas" de METR mide horas *humanas* reemplazables con 50% de éxito, no cuánto tarda el agente; METR no publica el tiempo de reloj [METR 2026].
9. La evidencia del mercado (A/B) sigue requiriendo semanas de tráfico; los usuarios simulados con LLM aciertan el signo del efecto en 70% de los casos y exageran la magnitud [medido, Hut y Masoero 2026]: sirven para filtrar candidatos, no para reemplazar la prueba con usuarios.
10. No se encontró ningún caso publicado de pronóstico por throughput/Monte Carlo (Vacanti, Magennis) aplicado a trabajo hecho por agentes: es un hueco.

## Casos y estudios

### METR: horizonte de tareas (2025, TH1.1 en 2026)

- **Quién:** Kwa, West, Becker y otros (METR), 2025-03-19; actualización TH1.1 del 2026-01-29; nota de limitaciones de Thomas Kwa del 2026-01-22; panel actualizado al 2026-05-08.
- **Qué midieron:** la duración, *para un humano*, de las tareas que un modelo completa con 50% de probabilidad. Los tiempos humanos salen de expertos medidos ("baseliners").
- **Resultado [medido]:** el horizonte se duplicó cada ~7 meses durante 6 años; Claude 3.7 Sonnet rondaba 1 hora (2025). Con TH1.1, la duplicación desde 2023 queda en 131 días contra 165 con TH1, y la suite pasó de 170 a 228 tareas (de 14 a 31 tareas de 8 h o más). Según el panel, las mediciones por encima de 16 h no son confiables con la suite actual.
- **Lo que no mide:** según la nota de Kwa, el horizonte "is not the length of time AIs can work independently"; es trabajo humano serial reemplazable. Las barras de error abarcan un factor ~2 hacia cada lado y el horizonte varía entre 40 y 100 veces según el dominio. METR no publica el tiempo de reloj del agente porque depende del proveedor y del harness; solo dice que los agentes son "varias veces" más rápidos que los humanos en las tareas que resuelven.
- **Fuentes:** https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ · https://metr.org/blog/2026-1-29-time-horizon-1-1/ · https://metr.org/notes/2026-01-22-time-horizon-limitations/ · https://metr.org/time-horizons/

### METR: RCT con desarrolladores open source (2025)

- **Quién:** Becker, Rush, Barnes y Rein (METR), 2025-07-10.
- **Qué midieron:** 16 desarrolladores con experiencia y 246 issues reales (~2 h cada uno) en sus propios repos, asignados al azar a "con IA" o "sin IA". El tiempo lo reportaron ellos mismos, con grabación de pantalla.
- **Resultado [medido]:** con IA tardaron 19% más. Antes esperaban una aceleración de 24% y, después de vivir la demora, seguían creyendo que habían ganado 20% [autorreporte].
- **Límites declarados:** muestra chica, repos maduros, poca experiencia previa con Cursor.
- **Fuente:** https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/

### METR: seguimiento del experimento de productividad (2026)

- **Quién:** METR, 2026-02-24.
- **Qué midieron:** 57 desarrolladores, más de 800 tareas, 143 repos (finales de 2025).
- **Resultado [medido, con sesgo declarado]:** desarrolladores originales, aceleración estimada de 18% (IC −38% a +9%); desarrolladores nuevos, 4% (IC −15% a +9%). METR declara el dato poco confiable: muchos se negaron a trabajar sin IA, entre 30% y 50% evitó cargar tareas que no querían hacer sin IA, bajó el pago, y el tiempo por tarea dejó de medirse bien con agentes en paralelo, porque la gente trabajaba en otra cosa mientras el agente corría.
- **Fuente:** https://metr.org/blog/2026-02-24-uplift-update/

### METR: análisis de transcripciones de Claude Code (2026)

- **Quién:** Amy Deng (METR), 2026-02-17.
- **Qué midieron:** 5.305 transcripciones de 7 personas del staff (enero 2026). GPT-5 estimó cuánto le llevaría la tarea a un ingeniero sin IA, y eso se comparó con el tiempo humano activo.
- **Resultado:** factor de ahorro entre ~1,5x y ~13x, presentado como cota superior blanda. La validación del juez LLM tuvo solo 34 etiquetas de referencia. Los usuarios avanzados corrían más de 2 agentes a la vez, y monitorear y cambiar de contexto consumía esfuerzo. La propia nota advierte que un ahorro de tiempo de 10x no implica 10x de valor.
- **Dato metodológico relevante:** METR usa un LLM para estimar el tiempo *humano* de la tarea, que es justo la clase de estimación que el sesgo de h4 vuelve sospechosa.
- **Fuente:** https://metr.org/notes/2026-02-17-exploratory-transcript-analysis-for-estimating-time-savings-from-coding-agents/

### Garikaparthi: "Can LLMs Perceive Time?" (2026)

- **Quién:** Aniketh Garikaparthi (TCS Research), arXiv 2604.00010, 2026-03-09 (workshop ICLR 2026).
- **Qué midieron:** 68 tareas en 7 categorías, con GPT-5, GPT-4o, OLMo3-7B y Qwen3-8B. Antes de cada tarea, el modelo estimaba su propia duración, y eso se comparaba con el tiempo real.
- **Resultado [medido]:** sobreestimación de 6,11x (GPT-5) y 3,60x (GPT-4o), con correlaciones de 0,55 y 0,35; en los modelos abiertos la correlación fue casi nula. Al ordenar qué tarea tarda más, quedaron cerca del azar (46%–58%), y en pares contraintuitivos GPT-5 acertó 18%. En tareas de varios pasos, el error fue de 5 a 10 veces. El feedback de calibración en contexto bajó el error de 13,2x a 2,3x, pero generalizó mal a tareas nuevas.
- **Explicación propuesta:** el modelo ve tokens, no tiempo transcurrido, y conoce las duraciones humanas por sus datos de entrenamiento.
- **Fuente:** https://arxiv.org/html/2604.00010v1

### Ofengenden y Andriushchenko: "Your Agents Are Not Time Aware" (2026)

- **Quién:** Michael Ofengenden y Maksym Andriushchenko, LessWrong, 2026-08-14.
- **Qué midieron:** ProgramBench (200 tareas) y AgentTime (235 tareas de 18 benchmarks); el tiempo de reloj se tomó con un timer fuera del sandbox.
- **Resultado [medido]:** Claude Opus 4.8 predijo ~99 min contra 85 reales (1,16x); GPT-5.5 Codex predijo ~72 min contra 17,5 (4,12x); en tareas cortas, la sobrepredicción llegó a 3,1x y 9,9x según el modelo. Cuando se les preguntó por su velocidad, los agentes se creyeron 3 a 4 veces más rápidos que un experto humano, así que no razonan solo en horas humanas. Sin timestamps, la estimación retrospectiva empeora.
- **Fuente:** https://www.lesswrong.com/posts/eAbuPXbjakop5rSJx/your-agents-are-not-time-aware

### Monperrus y Stenqvist: sesgo temporal de los agentes de código (2026)

- **Quién:** Martin Monperrus y Evita Stenqvist, 2026-09-07.
- **Qué reportan:** casos anecdóticos [no controlados]: un trabajo estimado en "3-4 semanas" que llevó 11 minutos, y otro de "6-8 horas" que llevó 10 minutos. Proponen cambiar las unidades de tiempo por unidades observables (archivos, tool calls, tokens), inyectar el tiempo transcurrido en el harness y registrar duraciones en el repo. El riesgo que señalan: un agente que sobreestima el costo puede declarar "fuera de alcance" un trabajo barato.
- **Fuente:** https://www.monperrus.net/martin/coding-agents-sense-of-time

### Calikli y Alhamed: formato del pedido de estimación (FSE 2025)

- **Quién:** Gül Calikli (U. Glasgow) y Mohammed Alhamed, FSE 2025 (2025-06-24).
- **Qué midieron:** replicaron con GPT-4, Gemini 1.5 Pro y Llama 3.1 los experimentos de Jørgensen y Halkjelsvik con humanos: 880 prompts sobre 704 historias de 3 proyectos open source.
- **Resultado [medido]:** igual que los humanos, los LLM dan estimaciones más bajas cuando la pregunta es "¿cuánto se completa en Y horas?" que cuando es "¿cuánto esfuerzo requiere X?", y muestran un patrón análogo al anclaje. La estimación de un LLM reproduce sesgos humanos de juicio.
- **Fuente:** https://conf.researchr.org/details/fse-2025/fse-2025-research-papers/104/Impact-of-Request-Formats-on-Effort-Estimation-Are-LLMs-Different-than-Humans-

### Bai et al.: consumo de tokens en tareas agénticas (2026)

- **Quién:** Bai, Huang, Wang, Sun, Mihalcea, Brynjolfsson, Pentland y Pei; arXiv 2604.22750 (versión final del 2026-10-02).
- **Resultado [medido]:** las tareas agénticas consumen ~1.000 veces más tokens que el chat; la misma tarea varía hasta 30x entre corridas; los modelos predicen su propio consumo con correlación de 0,39 como máximo; y gastar más tokens no da más precisión, que suele tocar techo con un costo intermedio.
- **Fuente:** https://arxiv.org/abs/2604.22750

### Smékal: especificación y gasto de tokens (2026)

- **Quién:** Jakub Smékal, arXiv 2608.25399, 2026-08-26.
- **Resultado [medido]:** 2.700 corridas con Kimi K3. Reducir una especificación completa a una historia de usuario pelada sube el gasto un 29,7%; la sensibilidad al prompt va de 13% a 115% según la tarea; la varianza entre corridas no cambia con el prompt; y un predictor basado en una sonda barata acertó el 36% en tareas no vistas.
- **Fuente:** https://arxiv.org/abs/2608.25399

### Derek Jones (The Shape of Code): crítica y "la estimación se corre aguas arriba" (2026)

- **Quién:** Derek Jones, 2026-05-10 y 2026-09-06/13.
- **Qué sostiene [opinión con datos ajenos]:** la investigación sobre estimación con LLM es en gran parte inválida, porque los datasets públicos tienen estimaciones (story points) y no tiempos reales, y además son órdenes de magnitud más chicos de lo necesario. Con agentes, la estimación pasa a la especificación y a sus iteraciones. Con un dataset de 289 proyectos, aun suponiendo 90% menos de codificación y 50% menos de testing, solo 10 a 15 proyectos muestran un ahorro total grande, porque en ese dominio la codificación pesa ~32% del esfuerzo.
- **Fuentes:** https://shape-of-code.com/2026/05/10/software-task-estimation-using-llms-is-fake-research/ · https://shape-of-code.com/2026/09/06/software-effort-estimation-in-2026/ · https://shape-of-code.com/2026/09/

### DORA 2025: State of AI-assisted Software Development

- **Quién:** DORA (Google Cloud), reseña de Matt Saunders en InfoQ, 2025-09-29.
- **Resultado:** casi 5.000 profesionales; ~90% usa IA; más de 80% dice ser más productivo [autorreporte]. La adopción de IA correlaciona con más throughput y también con más inestabilidad: más fallas de cambio y más retrabajo [correlación de encuesta]. La IA funciona como amplificador. Sobre la confianza en la salida de la IA, la reseña cita a Stack Overflow 2025: confía 33% y desconfía 46%.
- **Fuente:** https://www.infoq.com/news/2025/09/dora-state-of-ai-in-dev-2025 (no se abrió el informe primario).

### Faros AI: "AI Productivity Paradox" (2025)

- **Quién:** Faros AI, publicado el 2025-07-23; más de 10.000 desarrolladores en 1.255 equipos.
- **Resultado [telemetría, correlacional]:** en equipos con alta adopción de IA hubo +21% de tareas, +98% de PR mergeados, +91% de tiempo de revisión, PR 154% más grandes y +9% de bugs por desarrollador; a nivel compañía no hubo correlación significativa.
- **Fuente:** https://www.faros.ai/blog/ai-software-engineering

### LinearB: 2026 Software Engineering Benchmarks

- **Quién:** LinearB, 2026; 8,1 millones de PR, más de 4.800 organizaciones, 42 países.
- **Resultado [telemetría]:** los PR de agentes tardan 5,3x más en ser tomados para revisión (en otro pasaje, la misma página dice 4,6x), se revisan 2x más rápido una vez tomados, y se aceptan en 32,7% contra 84,4% de los manuales.
- **Fuente:** https://linearb.io/blog/engineering-benchmarks-report

### He et al.: mandato "2x" en una empresa (2026)

- **Quién:** He, Agarwal, Denisov-Blanch, Azaletskiy, Koyejo y Vasilescu; arXiv 2607.01904, 2026-07-02.
- **Resultado [medido, longitudinal]:** 802 desarrolladores y 196.212 PR (enero 2024 a abril 2026). El throughput per cápita llegó a 2,09x; la carga por revisor casi se duplicó; la revisión automática superó a la humana; las tasas de merge y revert se mantuvieron.
- **Fuente:** https://arxiv.org/abs/2607.01904

### Demirer, Musolff y Yang: "Writing Code vs. Shipping Code" (NBER, 2026)

- **Quién:** NBER w35275, mayo 2026, revisado en septiembre 2026.
- **Resultado [medido, event study]:** más de 500.000 desarrolladores de GitHub. Efecto acumulado en commits: +30% con autocompletado, +180% con agentes interactivos y +240% con agentes autónomos; en releases, apenas +30%. La elasticidad de sustitución entre la salida de la IA y el esfuerzo humano es 0,23, es decir, complementos fuertes.
- **Advertencia:** fuentes secundarias citan cifras de una versión anterior (+741% de código, +20% de releases, más de 100.000 desarrolladores). Acá se usan las de la página del NBER.
- **Fuente:** https://www.nber.org/papers/w35275

### Anthropic: "How AI is transforming work at Anthropic" (2025)

- **Quién:** Anthropic, 2025-12-02; encuesta a 132 personas, 53 entrevistas y ~200.000 transcripciones de Claude Code.
- **Resultado:** la mayoría dice poder delegar del todo solo entre 0% y 20% de su trabajo, y +50% de productividad [autorreporte]. En el uso registrado, las tool calls autónomas consecutivas pasaron de 9,8 a 21,2 y los turnos humanos por tarea bajaron de 6,2 a 4,1 [medido].
- **Fuente:** https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic

### Anthropic: task budgets (documentación)

- **Qué es:** un presupuesto de tokens para todo el loop agéntico; el modelo ve una cuenta regresiva y cierra ordenadamente. La documentación lo define como "a soft hint, not a hard cap": el tope duro sigue siendo `max_tokens`. Recomienda calibrar el presupuesto midiendo la distribución real (p99) en vez de adivinar, y advierte que un presupuesto muy chico puede llevar al modelo a rechazar o recortar la tarea. Está en beta y no está disponible en Claude Code.
- **Fuente:** https://platform.claude.com/docs/en/build-with-claude/task-budgets

### Vacanti / Magennis: pronóstico por flujo y Monte Carlo

- **Qué es:** pronosticar a partir de métricas de flujo (cycle time, throughput, WIP, ley de Little) y simulación de Monte Carlo sobre el historial, en lugar de estimar ítem por ítem (Vacanti, *Actionable Agile Metrics for Predictability*; Magennis, *Forecasting and Simulating Software Development Projects*).
- **Aplicación a agentes:** no se encontró ningún caso publicado con datos. Solo apareció una opinión (Rob Sandberg, 2026-04-15): Monte Carlo debería seguir siendo la base, y los agentes, señalar contexto cualitativo; un LLM que da "nueve sprints" con el mismo tono seguro haya razonado o no, no sirve como pronóstico.
- **Fuentes:** https://actionableagile.com/books/aamfp · https://www.productionalchemist.com/p/agents-cant-replace-monte-carlo-they

### Hut y Masoero (Amazon): ¿pueden los agentes simular un A/B? (COLM 2026)

- **Resultado [medido]:** sobre 67 tests A/B históricos, la simulación con un modelo base acierta el signo en 70% de los casos y exagera la magnitud del efecto. Una calibración en dos fases baja el error ~77x y un diseño intra-sujeto achica el error estándar ~2,4x. El paper parte de que cada A/B consume semanas de tiempo de reloj para acumular poder estadístico, y propone el simulador para filtrar candidatos antes de gastar tráfico real.
- **Fuente:** https://cdn.amazon.science/45/eb/51d943ea4f37847edc8c37c9521d/scipub-approval152129-48433523-can-ai-agents-simulate-ab-test-outcomes-a-validation-framework-for-agentic-experimentation.pdf

### Lu et al.: Agent A/B (2025–2026)

- **Resultado [medido]:** 1.000 agentes en Amazon.com contra un experimento paralelo con humanos; los resultados coincidieron en la dirección. Los autores dicen explícitamente que no reemplaza la prueba con usuarios reales y que sirve para mitigar la escasez de tráfico.
- **Fuente:** https://arxiv.org/html/2504.09723v4

## Evidencia por hipótesis

### h1: el tiempo de ejecución del agente no se estima, se le pone un tope (tiempo o costo)

**Veredicto: matizada (sostenida para la ejecución, refutada como "dejar de estimar").**

- **A favor:** el modelo no sabe cuánto va a tardar (Garikaparthi; Ofengenden y Andriushchenko); el consumo varía hasta 30x entre corridas de la misma tarea y los modelos lo predicen mal, con correlación de 0,39 como máximo (Bai et al.). Con esa varianza, un tope es más honesto que un número puntual. Los evaluadores ya trabajan así: METR corre a los agentes con límites de tokens y de tiempo. La documentación de task budgets recomienda calibrar el tope con el p99 medido, no con una estimación.
- **En contra o matiz:** (a) los topes de tokens disponibles son blandos, y un tope mal calibrado lleva al modelo a recortar o abandonar la tarea; o sea, el tope también necesita una estimación de la distribución. (b) El gasto responde de forma predecible al formato de la especificación (+29,7%, Smékal), lo que habilita estimar el costo *antes* de correr con una sonda barata (36% de acierto, todavía bajo). (c) Jones sostiene que la estimación se mueve a la especificación y a sus iteraciones, que son trabajo humano. (d) El tiempo de reloj del agente casi nunca domina: METR no lo publica porque depende del harness.
- **Formulación que la evidencia soporta mejor:** a la ejecución del agente se le pone un tope calibrado con la distribución histórica de consumo; lo que se estima es la especificación y las rondas de revisión.

### h2: el recurso escaso es la atención humana para decidir y validar, y se pronostica con su historial

**Veredicto: matizada (escasez sostenida por la evidencia; "se pronostica con su historial" sin evidencia directa).**

- **A favor (escasez):** +91% de tiempo de revisión (Faros); los PR de agentes esperan entre 4,6 y 5,3 veces más para ser tomados y se aceptan en 32,7% (LinearB); la ganancia cae de +240% en commits a +30% en releases, con una elasticidad de 0,23 entre salida de IA y esfuerzo humano (Demirer et al.); la carga por revisor casi se duplicó (He et al.); solo entre 0% y 20% del trabajo es delegable del todo [autorreporte, Anthropic]; monitorear y cambiar de contexto pesa con agentes en paralelo (METR, transcripciones).
- **En contra:** en He et al., la cola de revisión humana se alivió porque los PR empezaron a saltear la revisión humana y la automática pasó a ser mayoría, con merge y revert estables; la atención humana se sustituye en parte. En Anthropic bajaron los turnos humanos por tarea (de 6,2 a 4,1). DORA asocia la mayor velocidad a más inestabilidad: si la validación humana se saltea, el costo reaparece como retrabajo.
- **Sobre "se pronostica con su historial":** el marco de Vacanti y Magennis (ley de Little, Monte Carlo sobre throughput) se aplicaría naturalmente a la cola de revisión, pero no se encontró ningún caso publicado que lo haga con trabajo de agentes. Además, METR documenta que con agentes en paralelo el tiempo por tarea deja de ser medible por autorreporte, así que el historial hay que capturarlo como eventos del flujo (entrada y salida de cola), no como horas declaradas.

### h3: el tiempo hasta que el mundo da evidencia no se comprime y domina el tiempo total

**Veredicto: matizada ("no se comprime" refutada en parte; "domina" sin evidencia general).**

- **A favor:** los A/B requieren semanas para juntar poder estadístico, y eso depende del tráfico, no de la velocidad de construcción (Hut y Masoero, en la introducción del paper). La caída de commits a releases y la falta de efecto a nivel compañía (Demirer et al.; Faros) son consistentes con cuellos de botella después del código. El dato de Jones (codificación ≈32% del esfuerzo en un dominio) muestra que acelerar la codificación tiene un techo de impacto total.
- **En contra:** (a) se comprime en parte: los usuarios simulados aciertan el signo en 70% de los casos y, calibrados, bajan mucho el error (Hut y Masoero), y Agent A/B reproduce la dirección del efecto. Sirven para descartar candidatos antes de gastar tráfico, no para dar la evidencia final. (b) Ningún estudio abierto mide qué fracción del tiempo hasta el resultado es "esperar al mercado" contra revisión o integración. Las cifras de "el 80% del ciclo no es codificar" que circulan son de fuentes de vendors u opinión, no se verificaron y no se citan como dato. (c) En trabajo interno o técnico, la evidencia es un test o un despliegue, no el mercado; la hipótesis aplica a decisiones de producto, no a todo el trabajo.

### h4: los LLM estiman en horas humanas porque reproducen sus datos de entrenamiento, y un factor de corrección es frágil

**Veredicto: sostenida en lo central, con un matiz en el mecanismo.**

- **A favor (sesgo y causa):** la sobreestimación es sistemática (de 4 a 7 veces, y de 5 a 10 en tareas de varios pasos), y la explicación propuesta es que el modelo conoce duraciones humanas y no tiene acceso a su propia velocidad (Garikaparthi). Los LLM reproducen sesgos humanos de juicio como el anclaje y el efecto del formato del pedido (Calikli y Alhamed).
- **A favor (fragilidad del factor):** con el mismo banco de pruebas, el factor va de 1,16x a 9,9x según el modelo y el largo de la tarea (Ofengenden y Andriushchenko); la calibración en contexto mejora el caso visto pero no generaliza (Garikaparthi); el gasto varía hasta 30x entre corridas (Bai et al.). Un factor fijo hereda toda esa varianza.
- **Matiz:** no estiman *solo* en horas humanas. Si se les pregunta, los agentes se creen 3 a 4 veces más rápidos que un experto humano, pero igual sobreestiman su tiempo real (Ofengenden y Andriushchenko). Que la causa sean los datos de entrenamiento es una hipótesis razonable de los autores, no algo probado causalmente. Además, según Jones, los datasets de estimación tienen estimaciones y no tiempos reales: ni siquiera la "hora humana" que reproduce el modelo está bien medida.
- **Alternativas al factor que aparecen en la literatura [opinión o propuesta, sin evaluación comparativa]:** inyectar el tiempo transcurrido y timestamps en el harness, expresar el trabajo en unidades observables (tool calls, archivos, tokens) y registrar duraciones reales para recalibrar (Monperrus y Stenqvist).

## Preguntas que la evidencia deja abiertas

- ¿Qué fracción del tiempo total hasta el resultado (de la idea a la evidencia) se va en especificar, ejecutar, revisar, integrar y esperar al mercado cuando ejecutan agentes? Ningún estudio abierto lo descompone.
- ¿El pronóstico por throughput/Monte Carlo sigue funcionando cuando el throughput de ejecución cambia con cada versión del modelo? La estacionariedad del historial, que ese método supone, se rompe con cada cambio de modelo o harness.
- ¿Un factor de corrección recalibrado de forma continua (ventana móvil por modelo y tipo de tarea) es estable en la práctica? Solo hay evidencia de que un factor fijo y la calibración en contexto no generalizan.
- ¿Cuánto del alivio de la cola de revisión (He et al.) es sustitución legítima por revisión automática y cuánto es control salteado que vuelve como inestabilidad (DORA)?
- ¿Cómo se mide el tiempo humano cuando una persona supervisa varios agentes en paralelo? METR reconoce que su método dejó de servir para eso.
- ¿Las predicciones de costo con sonda barata (Smékal, 36%) mejoran lo suficiente para presupuestar antes de correr?

## Fuentes (consultadas el 2026-10-07)

| Fuente | Autor(es) | Fecha | URL |
|---|---|---|---|
| Measuring AI Ability to Complete Long Tasks | Kwa, West, Becker et al. (METR) | 2025-03-19 | https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ |
| Time Horizon 1.1 | METR | 2026-01-29 | https://metr.org/blog/2026-1-29-time-horizon-1-1/ |
| Clarifying limitations of time horizon | Thomas Kwa (METR) | 2026-01-22 | https://metr.org/notes/2026-01-22-time-horizon-limitations/ |
| Task-Completion Time Horizons (panel) | METR | act. 2026-05-08 | https://metr.org/time-horizons/ |
| Early-2025 AI on experienced OS developers (RCT) | Becker, Rush, Barnes, Rein (METR) | 2025-07-10 | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ |
| Uplift update | METR | 2026-02-24 | https://metr.org/blog/2026-02-24-uplift-update/ |
| Transcript analysis for time savings | Amy Deng (METR) | 2026-02-17 | https://metr.org/notes/2026-02-17-exploratory-transcript-analysis-for-estimating-time-savings-from-coding-agents/ |
| Can LLMs Perceive Time? | Aniketh Garikaparthi | 2026-03-09 | https://arxiv.org/html/2604.00010v1 |
| Your Agents Are Not Time Aware | Ofengenden, Andriushchenko | 2026-08-14 | https://www.lesswrong.com/posts/eAbuPXbjakop5rSJx/your-agents-are-not-time-aware |
| Coding Agents Have Completely Wrong Sense of Time | Monperrus, Stenqvist | 2026-09-07 | https://www.monperrus.net/martin/coding-agents-sense-of-time |
| Impact of Request Formats on Effort Estimation | Calikli, Alhamed (FSE 2025) | 2025-06-24 | https://conf.researchr.org/details/fse-2025/fse-2025-research-papers/104/Impact-of-Request-Formats-on-Effort-Estimation-Are-LLMs-Different-than-Humans- |
| How Do AI Agents Spend Your Money? | Bai, Huang, Wang et al. | 2026-04-24 (rev. 2026-10-02) | https://arxiv.org/abs/2604.22750 |
| Can your AI agent be cheaper? | Jakub Smékal | 2026-08-26 | https://arxiv.org/abs/2608.25399 |
| Software task estimation using LLMs is fake research | Derek Jones | 2026-05-10 | https://shape-of-code.com/2026/05/10/software-task-estimation-using-llms-is-fake-research/ |
| Software effort estimation in 2026 | Derek Jones | 2026-09-06 | https://shape-of-code.com/2026/09/06/software-effort-estimation-in-2026/ |
| Archivo de septiembre 2026 (ahorro por proyecto) | Derek Jones | 2026-09-13 | https://shape-of-code.com/2026/09/ |
| DORA 2025 (reseña) | Matt Saunders (InfoQ) | 2025-09-29 | https://www.infoq.com/news/2025/09/dora-state-of-ai-in-dev-2025 |
| AI Productivity Paradox | Faros AI | 2025-07-23 | https://www.faros.ai/blog/ai-software-engineering |
| 2026 Software Engineering Benchmarks | LinearB | 2026 | https://linearb.io/blog/engineering-benchmarks-report |
| AI Writes Faster Than Humans Can Review | He, Agarwal, Denisov-Blanch et al. | 2026-07-02 | https://arxiv.org/abs/2607.01904 |
| Writing Code vs. Shipping Code (NBER w35275) | Demirer, Musolff, Yang | 2026-05 (rev. 2026-09) | https://www.nber.org/papers/w35275 |
| How AI is transforming work at Anthropic | Anthropic | 2025-12-02 | https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic |
| Task budgets (documentación) | Anthropic | 2026 (beta 2026-03-13) | https://platform.claude.com/docs/en/build-with-claude/task-budgets |
| Actionable Agile Metrics for Predictability | Daniel S. Vacanti | s/f en la página | https://actionableagile.com/books/aamfp |
| Agents Can't Replace Monte Carlo | Rob Sandberg | 2026-04-15 | https://www.productionalchemist.com/p/agents-cant-replace-monte-carlo-they |
| Can AI Agents Simulate A/B Test Outcomes? | Hut, Masoero (COLM 2026) | 2026 | https://cdn.amazon.science/45/eb/51d943ea4f37847edc8c37c9521d/scipub-approval152129-48433523-can-ai-agents-simulate-ab-test-outcomes-a-validation-framework-for-agentic-experimentation.pdf |
| Agent A/B | Lu, Hsu, Gu et al. | 2026-03-10 (v4) | https://arxiv.org/html/2504.09723v4 |

Fuentes vistas solo como resultado de búsqueda y no usadas como dato: el libro de Magennis (ficha en Amazon), notas de vendors sobre la "ley de Amdahl" aplicada al delivery y recomendaciones de duración de A/B atribuidas a Kohavi por terceros.
