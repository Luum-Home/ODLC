---
tags: [crudo, investigacion, modelos]
status: crudo
created: 2026-10-07
---

# Investigación: selección de modelos bajo incertidumbre

Pregunta: los modelos cambian todo el tiempo, aparecen proveedores nuevos, no se sabe qué usan otras organizaciones y no hay certeza de qué modelo rinde mejor en qué tarea, ni siquiera con varios agentes en paralelo. ¿Cómo lo resuelven en la práctica las organizaciones y qué dice la evidencia?

Fuentes consultadas el 2026-10-07. Convención: **[dato]** = medido por quien lo publica; **[declarado]** = afirmación de una empresa sobre sí misma sin método publicado; **[opinión]** o **[predicción]** = interpretación o pronóstico.

## Resumen

1. Las organizaciones que publicaron su método no eligen "el mejor modelo": corren sus propios evals sobre tráfico real o simulado y confirman con A/B en producción (Intercom, Shopify, Notion).
2. Los benchmarks públicos ordenan bastante bien el nivel general (correlación mediana 0,68 entre benchmarks de distintas categorías, Epoch AI, 2026), pero sobreestiman el desempeño absoluto en tareas reales.
3. Ejemplo medido: en SWE-bench Verified los mantenedores mergearían unos 24 puntos porcentuales menos de lo que aprueba el grader automático (METR, 2026).
4. Hay evidencia directa de memorización en SWE-bench (76% de acierto en rutas de archivo sin ver el repo, contra 53% fuera del benchmark) y de sesgo de divulgación en Chatbot Arena.
5. Elegir bien un solo modelo es una línea de base difícil de superar: la mayoría de los routers, incluido uno comercial, no le ganan de forma confiable (LLMRouterBench, 2026).
6. La diversidad de proveedores reduce poco la correlación de errores: los modelos más capaces se equivocan parecido aunque sean de empresas distintas (Kim et al., ICML 2025; Hossain et al., 2026).
7. Diez jueces aportan la información de unos 3,5 jueces independientes (Hossain et al., 2026). El consenso no prueba nada; el desacuerdo sí sirve como señal de error (AUROC 0,75 contra 0,59 de la entropía propia, Gorbett y Jana, 2026).
8. El mismo nombre de modelo no garantiza el mismo comportamiento: el comportamiento deriva entre versiones (Chen et al., 2023) y fallas de infraestructura degradan la calidad sin cambiar el ID (Anthropic, 2025).
9. Cambiar de modelo tiene un costo medible: los prompts no se transfieren bien entre modelos (PromptBridge, 2025). Aun así, solo el 11% de las empresas encuestadas cambió de proveedor en un año (Menlo, 2025).
10. Veredictos: h1 matizada, h2 matizada, h3 refutada en su primera mitad y sostenida con límites en la segunda, h4 matizada (registrar modelo+versión es necesario pero no alcanza).

## Casos

### Intercom (Fin, atención al cliente)

- **Quién:** Fergal Reid, Chief AI Officer de Intercom, en el podcast *Chain of Thought* (episodio del 2026-02-26).
- **Qué hicieron:** reemplazaron un modelo GPT por un Qwen de 14B con fine-tuning para una tarea de canonicalización de consultas. Miden los cambios con A/B en producción, separando resoluciones "blandas" de "duras".
- **Qué midieron:** **[declarado]** el gasto en esa tarea rondaba los 250.000 USD por mes y ahorraron casi todo. **[declarado]** la tasa de resolución de Fin pasó de cerca del 30% a casi 70%, y la atribuyen más a la infraestructura alrededor del modelo (re-rankers propios, RAG) que al modelo base. **[declarado]** respuestas más lentas se asociaron con más resolución.
- **Lectura:** el criterio de cambio fue la métrica de negocio propia, no un ranking público. Las cifras no tienen método publicado.
- **Fuente:** https://chainofthought.transistor.fm/episodes/how-intercom-cut-250k-month-by-ditching-gpt-for-qwen

### Shopify (Sidekick, agente para comerciantes)

- **Quién:** Andrew McNamara, Ben Lafferty y Michael Garner, Shopify Engineering, 2025-08-26.
- **Qué hicieron:** armaron "Ground Truth Sets" (GTX) a partir de conversaciones reales en vez de un set curado. Cada conversación la etiquetan al menos tres expertos de producto. Calibran un juez LLM contra esas etiquetas y usan un simulador de comerciantes para probar cada cambio candidato antes de producción.
- **Qué midieron:** **[dato]** el juez pasó de un kappa de Cohen de 0,02 a 0,61, con un techo de acuerdo entre humanos de 0,69. El acuerdo entre humanos funciona como techo del juez.
- **Lectura:** el artículo no dice qué modelo usan. La pieza central es el aparato de evaluación, no la elección del proveedor.
- **Fuente:** https://shopify.engineering/building-production-ready-agentic-systems

### Notion (Notion AI)

- **Quién:** Sarah Sachs (líder de modelado de IA de Notion), en un caso de cliente publicado por Braintrust, proveedor de la plataforma de evals. Es un caso de proveedor y no tiene fecha visible.
- **Qué hicieron:** cuando sale un modelo nuevo corren evals de regresión (qué se rompe) y evals "de frontera" (qué mejora), identifican en qué se diferencia del anterior y lo despliegan solo en los casos de uso donde gana.
- **Qué midieron:** **[declarado]** menos de 24 horas para desplegar un modelo de frontera nuevo; 70 ingenieros alineados sobre los mismos evals.
- **Fuente:** https://braintrust.dev/customers/notion

### GitHub Copilot (modo "auto")

- **Quién:** GitHub, changelog del 2025-12-10.
- **Qué hicieron:** el modo auto elige el modelo según la disponibilidad en tiempo real, entre GPT-5.1-Codex-Max, GPT-5 mini, GPT-4.1, Sonnet 4.5 y Haiku 4.5 según el plan. El usuario ve qué modelo respondió pasando el cursor sobre la respuesta.
- **Qué midieron:** nada publicado sobre calidad. **[predicción]** GitHub anuncia que más adelante va a rutear según la complejidad del pedido.
- **Lectura:** un router comercial grande rutea hoy por disponibilidad y costo (10% de descuento en auto), no por la calidad en la tarea. Exponer el modelo usado por respuesta es una forma de procedencia.
- **Fuente:** https://github.blog/changelog/2025-12-10-auto-model-selection-is-generally-available-in-github-copilot-in-visual-studio-code/

### Anthropic (proveedor, postmortem de calidad)

- **Quién:** Anthropic Engineering, 2025-09-17.
- **Qué pasó:** tres bugs de infraestructura degradaron respuestas entre agosto y principios de septiembre de 2025 sin cambiar el modelo: ruteo a un pool con otra ventana de contexto, corrupción de salida y una mala compilación de top-k en TPU.
- **Qué midieron:** **[dato]** en el pico (31 de agosto), el 16% de los pedidos a Sonnet 4 estaba afectado por el error de ruteo. Los evals internos no lo detectaron a tiempo y se descubrió por reportes de la comunidad. Como respuesta, extendieron los evals de calidad al monitoreo continuo en producción.
- **Lectura:** "modelo X versión Y" no fija el comportamiento; la pila de servicio también importa.
- **Fuente:** https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues

### Menlo Ventures (qué usan otras organizaciones)

- **Quién:** Menlo Ventures, *2025 Mid-Year LLM Market Update*. Encuesta del 30 de junio al 10 de julio de 2025 a 150 decisores técnicos.
- **Qué midieron:** **[dato de encuesta]** participación en uso empresarial: Anthropic 32%, OpenAI 25%, Google 20%, Llama 9%, DeepSeek 1%. En los últimos 12 meses, el 66% pasó a un modelo más nuevo del mismo proveedor, el 23% no cambió nada y el 11% cambió de proveedor. Al mes de su lanzamiento, Claude 4 tenía el 45% del uso entre usuarios de Anthropic.
- **Lectura:** el cambio dominante es de versión dentro del mismo proveedor, no de proveedor. La muestra es chica y la publica un inversor de Anthropic, lo que es un posible sesgo.
- **Fuente:** https://menlovc.com/perspective/2025-mid-year-llm-market-update/

### METR (evaluador independiente)

- **Quién:** Parker Whitfill, Cheryl Wu, Joel Becker y Nate Rush, nota del 2026-03-10. Además, el RCT del 2025-07-10 y su actualización del 2026-02-24.
- **Qué midieron:**
  - **[dato]** 4 mantenedores de scikit-learn, Sphinx y pytest revisaron 296 PRs de agentes que pasaban el grader de SWE-bench Verified. Mergearían unos 24 pp menos de lo que aprueba el grader. Los parches humanos de referencia se aceptaron al 68%. La tasa de merge mejora unos 9,6 pp por año más lento que el puntaje automático. Límites: sin CI, un solo intento y 3 de 12 repos.
  - **[dato]** en el RCT de 2025, 16 desarrolladores experimentados y 246 tareas: con IA tardaron 19% más, aunque esperaban ir 24% más rápido.
  - **[dato]** en la actualización de 2026, el cambio estimado en tiempo fue -18% (IC -38% a +9%) para 10 desarrolladores que volvieron y -4% (IC -15% a +9%) para 47 nuevos. Los dos intervalos cruzan cero. METR los considera evidencia muy débil por selección: muchos rechazaron trabajar sin IA, y con varios agentes concurrentes el tiempo por tarea se mide mal.
- **Fuentes:** https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/ · https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ · https://metr.org/blog/2026-02-24-uplift-update/

## Evidencia por hipótesis

### h1. "Qué modelo es mejor" no tiene respuesta estable; conviene preguntar "qué modelo pasa mis evals para este tipo de tarea, a qué costo, hoy"

**A favor**
- Las tres empresas que publicaron su método (Intercom, Shopify, Notion) deciden con evals propios y A/B, no con rankings. Son datos de práctica, no de resultado comparado.
- El "hoy" está justificado: el comportamiento del "mismo" servicio cambia en semanas. **[dato]** En GPT-4, el acierto en identificar números primos cayó de 84% a 51% entre marzo y junio de 2023 (Chen, Zaharia y Zou, https://arxiv.org/abs/2307.09009). El postmortem de Anthropic muestra degradación sin cambio de modelo.
- **[dato]** Cuando el test y los criterios se personalizan, el ranking de modelos cambia respecto de los benchmarks estándar (Itzhak et al., COLM 2026, https://arxiv.org/abs/2604.14137).

**En contra**
- A nivel grueso sí hay una respuesta bastante estable. **[dato]** Correlación mediana 0,68 entre benchmarks de categorías distintas y 0,79 dentro de la misma categoría (Emberson y Edelman, Epoch AI, 2026-01-23, https://epoch.ai/data-insights/benchmark-correlations). Los propios autores advierten que la amplitud temporal infla la correlación.
- **[dato]** Bajo una evaluación unificada (400K instancias, 21 datasets, 33 modelos), varios routers recientes, incluido uno comercial, no superan de forma confiable al mejor modelo individual (Li et al., https://arxiv.org/abs/2601.07206, 2026-01-12). La pregunta "cuál es el mejor modelo para mi mezcla de tareas" tiene una respuesta útil.
- Los evals propios no se sostienen solos. **[dato]** En 17 de 19 practicantes entrevistados, los resultados de evaluación no se traducían en cambios concretos (van der Maden et al., 2026-01-25, https://arxiv.org/abs/2604.16304).

**Veredicto: matizada.** Como práctica, la reformulación se sostiene. Lo que no se sostiene es que no haya señal general: el ranking grueso es bastante estable y una buena línea de base suele ser un solo modelo bien evaluado, con el router como optimización a demostrar.

### h2. Los benchmarks públicos predicen poco el desempeño en tareas propias

**A favor**
- **[dato]** Gap de 24 pp entre el grader de SWE-bench y la decisión de merge de los mantenedores (METR, 2026).
- **[dato]** 76% de acierto en rutas de archivo con solo el texto del issue en SWE-bench Verified, contra 53% en repos fuera del benchmark. Similitud literal de 5-gramas de 35% contra 18% (Liang, Garg y Zilouchian Moghaddam, Microsoft, https://arxiv.org/abs/2506.12286, versión de diciembre de 2025).
- **[dato]** En Chatbot Arena, Meta probó 27 variantes privadas antes de Llama 4. Google y OpenAI recibieron alrededor del 19,2% y el 20,4% de los datos. Con poco dato extra de Arena se obtienen hasta 112% de ganancia relativa en esa distribución (Singh et al., https://arxiv.org/abs/2504.20879, 2025-04-29). Los autores lo resumen así: "selective disclosure of performance results".
- **[dato]** RCT de METR (2025): las ganancias en benchmarks no se tradujeron en velocidad para desarrolladores experimentados en sus propios repos.
- **[dato]** Los evals de Anthropic no detectaron una degradación real en producción (postmortem de 2025).

**En contra**
- La alta correlación entre benchmarks (Epoch) sugiere que sí predicen el nivel general.
- **[dato]** GDPval (Patwardhan et al., OpenAI, https://arxiv.org/abs/2510.04374, 2025-10-05), con 44 ocupaciones y tareas armadas por profesionales con un promedio de 14 años de experiencia, muestra mejora aproximadamente lineal en el tiempo. Hay benchmarks construidos sobre trabajo real que acortan la distancia. Ojo: lo publica un proveedor.
- La actualización de METR de 2026 sugiere que la brecha con el trabajo real se achicó, aunque con evidencia débil.

**Hueco:** no se encontró ningún estudio que mida la correlación entre el ranking en un benchmark público y el ranking en los evals internos de una organización. La afirmación "predicen poco" no está medida en esos términos.

**Veredicto: matizada.** Los benchmarks públicos sirven para armar la lista corta (descartar modelos de otro nivel) y predicen mal el desempeño absoluto y el orden fino entre los modelos de frontera en una tarea propia, sobre todo en benchmarks viejos o contaminados.

### h3. Jueces de proveedores distintos tienen errores menos correlacionados, y su desacuerdo es una señal útil para escalar a un humano

**Primera mitad (menos correlación entre proveedores distintos)**
- **[dato]** Sobre más de 350 modelos, cuando dos modelos se equivocan coinciden en la respuesta el 60% de las veces en HELM, contra un 33% esperable al azar. Ser del mismo desarrollador suma unos +6,6 puntos de acuerdo en el leaderboard de HuggingFace. Pero la precisión es el predictor más fuerte: los modelos más capaces tienen errores muy correlacionados aun con arquitectura y proveedor distintos (Kim, Garg, Peng y Garg, ICML 2025, https://arxiv.org/abs/2506.07962).
- **[dato]** Diez jueces con correlación de error media de 0,21 equivalen a unos 3,5 jueces independientes. En hasta el 28% de las comparaciones, corregir por errores compartidos invierte la conclusión. La dependencia es más fuerte entre jueces de frontera de proveedores distintos (Hossain, Yousefi y Lim, https://arxiv.org/abs/2609.22512, 2026-09-18).
- **[dato]** Los jueces favorecen a los modelos parecidos a ellos, y los errores se vuelven más similares a medida que crece la capacidad (Goel et al., "Great Models Think Alike", ICML 2025, https://arxiv.org/abs/2502.04313).
- A favor, con evidencia más vieja: un panel de modelos chicos de familias distintas superó a un juez GPT-4 en seis datasets y costó más de 7 veces menos (Verga et al., Cohere, https://arxiv.org/abs/2404.18796, 2024-04-29).

**Segunda mitad (el desacuerdo como señal para escalar)**
- **[dato]** La perplejidad que un modelo verificador asigna a la respuesta de otro modelo detecta errores mejor que la incertidumbre propia, incluidos errores con alta confianza: AUROC 0,75 contra 0,59 en MMLU (Gorbett y Jana, https://arxiv.org/abs/2603.25450, revisado en junio de 2026).
- **[dato]** La evaluación selectiva en cascada, que confía en el juez o escala según una confianza calibrada, logró más de 80% de acuerdo con humanos y unos 80% de cobertura (Jung, Brahman y Choi, https://arxiv.org/abs/2407.18370, 2024; ICLR 2025). Escala a un modelo más fuerte, no necesariamente a un humano.
- **[dato]** En debate multiagente, casi toda la ganancia viene del voto mayoritario y no del debate (Choi, Zhu y Li, NeurIPS 2025, https://arxiv.org/abs/2508.17536).
- Límite: el desacuerdo detecta los errores no compartidos. Los compartidos, que según Kim y Hossain son muchos entre modelos fuertes, pasan como consenso.

**Veredicto: la primera mitad queda refutada en su forma fuerte; la segunda se sostiene con límites.** Cambiar de proveedor reduce poco la correlación de errores entre modelos de frontera. El desacuerdo sí es una señal útil para escalar, pero el acuerdo no prueba que la respuesta sea correcta. Hay que calibrar contra etiquetas humanas, como hace Shopify con su techo de kappa 0,69.

### h4. Sin registrar modelo+versión por artefacto no se puede aprender qué modelo rinde mejor

**A favor**
- Las convenciones semánticas de OpenTelemetry para GenAI distinguen el modelo pedido (`gen_ai.request.model`) del que efectivamente respondió (`gen_ai.response.model`). Ver https://github.com/open-telemetry/semantic-conventions-genai, en desarrollo y con el esquema todavía marcado "TODO"; las definiciones se leyeron en la documentación de Traceloop (https://traceloop.com/docs/openllmetry/contributing/semantic-conventions).
- Copilot auto rutea dinámicamente y muestra el modelo usado por respuesta. Sin ese dato, la calidad observada no se puede atribuir a un modelo.
- **[dato]** Every Eval Ever (Batzner et al., https://arxiv.org/abs/2606.14516, 2026-06-12): los resultados de evaluación están dispersos en formatos incompatibles y con metadatos inconsistentes. Proponen un esquema único y hoy reúnen 22.235 modelos y 2.273 benchmarks.

**En contra / matices**
- Para comparar modelos no siempre hace falta procedencia histórica: un A/B (Intercom) solo necesita registrar la asignación de cada brazo, y un eval offline se puede volver a correr sobre un set fijo (Shopify GTX, Notion).
- Modelo+versión no alcanza. El postmortem de Anthropic muestra degradación con el mismo ID de modelo, y Chen et al. muestran deriva bajo el mismo nombre de servicio. Intercom atribuye la mayor parte de su mejora a la infraestructura, no al modelo. Para atribuir hace falta además prompt, parámetros, herramientas y la configuración del harness.

**Veredicto: matizada.** Para aprender de los resultados en producción (aprobado o rechazado, mergeado o no, resuelto o no), registrar modelo+versión por artefacto es necesario. No alcanza solo: también hay que registrar prompt, configuración y harness. Y no es el único camino, porque los evals offline reejecutables y los A/B con asignación registrada permiten aprender sin la procedencia histórica de cada artefacto.

### Costo de cambiar de modelo (transversal)

- **[dato]** Reusar un prompt optimizado para un modelo en otro rinde bastante peor que un prompt optimizado para el destino; los autores llaman a esto "model drifting" y lo describen como frecuente y severo (Wang et al., PromptBridge, https://arxiv.org/abs/2512.01420, 2025-12-01).
- **[dato de encuesta]** Solo el 11% de las empresas cambió de proveedor en un año; lo dominante es actualizar la versión dentro del mismo proveedor (Menlo, 2025).
- **[declarado]** Intercom capturó un ahorro grande cambiando de modelo en una sola tarea, con un modelo propio con fine-tuning. El cambio por tarea, no global, parece ser donde el costo de cambiar se paga.
- Para enjambres: más modelos en un ensemble dan rendimientos decrecientes frente a una buena selección (LLMRouterBench). Con agentes concurrentes, METR no logró medir bien el tiempo por tarea.

## Preguntas abiertas

1. ¿Qué correlación hay entre el ranking en benchmarks públicos y el ranking en los evals internos de una organización, para la misma familia de tareas? No se encontró ninguna medición publicada.
2. ¿Cuánto reduce la correlación de errores mezclar proveedores frente a mezclar prompts, temperaturas o roles con el mismo modelo, en jueces de código y no en MMLU?
3. ¿Qué umbral de desacuerdo entre jueces justifica escalar a un humano, y con qué tasa de falsos negativos por errores compartidos?
4. ¿Qué parte de la variación en calidad se debe al modelo y qué parte al harness, el prompt y la recuperación de contexto? Intercom lo declara para su caso, pero falta una medición controlada.
5. ¿Cuánto cuesta en horas migrar un prompt o un agente de un modelo a otro en un caso real? PromptBridge mide pérdida de rendimiento, no horas de trabajo.
6. Pendiente de verificar: OpenAI publicó "Why we no longer evaluate SWE-bench Verified" (https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/), que según resúmenes de terceros documenta tests defectuosos y filtración al entrenamiento. La página devolvió 403 y no se pudo abrir; no se citan sus números.

## Fuentes (consultadas el 2026-10-07)

| Fuente | Autor / organización | Fecha | URL |
|---|---|---|---|
| Correlated Errors in Large Language Models | Kim, Garg, Peng, Garg (ICML 2025) | 2025-06-09 | https://arxiv.org/abs/2506.07962 |
| Agreement Overstates Evidence: Error Dependence in LLM Judge Consensus | Hossain, Yousefi, Lim | 2026-09-18 | https://arxiv.org/abs/2609.22512 |
| Great Models Think Alike and this Undermines AI Oversight | Goel et al. (ICML 2025) | 2025-02 | https://arxiv.org/abs/2502.04313 |
| Replacing Judges with Juries (PoLL) | Verga et al. (Cohere) | 2024-04-29 | https://arxiv.org/abs/2404.18796 |
| Trust or Escalate | Jung, Brahman, Choi | 2024-07-25 | https://arxiv.org/abs/2407.18370 |
| Cross-Model Disagreement as a Label-Free Correctness Signal | Gorbett, Jana | 2026-03-26 (rev. 2026-06-11) | https://arxiv.org/abs/2603.25450 |
| Debate or Vote | Choi, Zhu, Li (NeurIPS 2025) | 2025-08 | https://arxiv.org/abs/2508.17536 |
| The Leaderboard Illusion | Singh et al. | 2025-04-29 | https://arxiv.org/abs/2504.20879 |
| The SWE-Bench Illusion | Liang, Garg, Zilouchian Moghaddam (Microsoft) | 2025-06 (v. 2025-12) | https://arxiv.org/abs/2506.12286 |
| Many SWE-bench-passing PRs would not be merged into main | Whitfill, Wu, Becker, Rush (METR) | 2026-03-10 | https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/ |
| Measuring the Impact of Early-2025 AI on Experienced OS Developer Productivity | METR | 2025-07-10 | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ |
| We are Changing our Developer Productivity Experiment Design | METR | 2026-02-24 | https://metr.org/blog/2026-02-24-uplift-update/ |
| Benchmark correlations | Emberson, Edelman (Epoch AI) | 2026-01-23 | https://epoch.ai/data-insights/benchmark-correlations |
| GDPval | Patwardhan et al. (OpenAI) | 2025-10-05 | https://arxiv.org/abs/2510.04374 |
| LLMRouterBench | Li et al. | 2026-01-12 | https://arxiv.org/abs/2601.07206 |
| PromptBridge: Cross-Model Prompt Transfer | Wang et al. | 2025-12-01 | https://arxiv.org/abs/2512.01420 |
| Results-Actionability Gap | van der Maden et al. | 2026-01-25 | https://arxiv.org/abs/2604.16304 |
| From Feelings to Metrics (vibe-testing) | Itzhak, Habba, Stanovsky, Belinkov (COLM 2026) | 2026 | https://arxiv.org/abs/2604.14137 |
| Every Eval Ever | Batzner et al. | 2026-06-12 | https://arxiv.org/abs/2606.14516 |
| How is ChatGPT's behavior changing over time? | Chen, Zaharia, Zou | 2023-07-18 (rev. 2023-10-31) | https://arxiv.org/abs/2307.09009 |
| A postmortem of three recent issues | Anthropic Engineering | 2025-09-17 | https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues |
| Building production-ready agentic systems (Sidekick) | McNamara, Lafferty, Garner (Shopify) | 2025-08-26 | https://shopify.engineering/building-production-ready-agentic-systems |
| How Intercom cut $250K/month by ditching GPT for Qwen | Chain of Thought, con Fergal Reid | 2026-02-26 | https://chainofthought.transistor.fm/episodes/how-intercom-cut-250k-month-by-ditching-gpt-for-qwen |
| Notion customer story | Braintrust (caso de proveedor) | sin fecha | https://braintrust.dev/customers/notion |
| Auto model selection GA in VS Code | GitHub changelog | 2025-12-10 | https://github.blog/changelog/2025-12-10-auto-model-selection-is-generally-available-in-github-copilot-in-visual-studio-code/ |
| 2025 Mid-Year LLM Market Update | Menlo Ventures | 2025-07 | https://menlovc.com/perspective/2025-mid-year-llm-market-update/ |
| OpenTelemetry GenAI semantic conventions | OpenTelemetry | en desarrollo | https://github.com/open-telemetry/semantic-conventions-genai |
| OpenLLMetry semantic conventions | Traceloop | consultado 2026-10-07 | https://traceloop.com/docs/openllmetry/contributing/semantic-conventions |
