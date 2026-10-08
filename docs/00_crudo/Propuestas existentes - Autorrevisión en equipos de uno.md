---
tags: [crudo, investigacion, tiny-teams, revision]
status: crudo
created: 2026-10-08
---

# Propuestas existentes: autorrevisión en equipos de uno

Pregunta: el marco exige que quien ejecuta no valide. En un equipo de una persona que trabaja con agentes de IA, todos los roles los tiene la misma persona, y usar un agente como revisor choca con la autopreferencia medida (Panickssery y otros, 2024). ¿Qué soluciones aporta la comunidad (desarrolladores solos, indie hackers, fundadores, equipos chicos) y qué evidencia hay de que funcionen?

Contexto: el crudo "Investigación - Tiny teams y bootstrapping" (sección 4) concluyó que ninguna fuente propone una separación de funciones que funcione con una sola persona, y el crudo "Propuestas existentes - Revisión en manos de agentes" relevó errores correlacionados entre modelos (Kim y otros, ICML 2025), reward hacking y la base de verificación por ejecución. Este documento no repite esos hallazgos: los usa como punto de partida y releva propuestas específicas para el caso de una persona.

Convención de evidencia: **[medido]** = estudio con comparación o medición explícita; **[testimonio]** = relato de quien lo aplicó, comentario de foro, dato de proveedor sin método publicado; **[opinión]** = argumento, guía o recomendación sin medición propia. Fuentes consultadas el 2026-10-08. Reddit (r/ExperiencedDevs, r/SaaS, r/indiehackers) e Indie Hackers no pudieron abrirse (bloqueo al agente y HTTP 403); los testimonios de foro salen de Hacker News y GitHub Discussions.

## Resumen

1. La autopreferencia está replicada y tiene un mecanismo plausible: familiaridad (menor perplejidad) y reconocimiento de autoría. Es más dañina justo cuando el modelo se equivocó: en código, 50 a 75 % de preferencia por la propia respuesta errónea (Chen y otros, 2025).
2. Cambiar de familia reduce el sesgo de familia (3,4 a 8,4 puntos de "favor" medidos en jueces de la misma familia; Awuni y otros, 2026), pero no lo vuelve independiente: los errores siguen correlacionados entre proveedores (crudo previo).
3. En revisión de código, el revisor de otra familia ayuda o perjudica según la dirección: Claude revisando a Codex subió de 71,6 % a 89,7 %; Codex revisando a Claude bajó de 91,4 % a 82,8 % (Xiang y otros, 2026).
4. El contexto limpio (sesión nueva, sin el razonamiento del escritor) tiene respaldo débil: supera a repetir la revisión en la misma sesión, pero no fue significativamente mejor que una sola autorrevisión al promediar corridas (Song, 2026).
5. La combinación con mejor dato para una persona: una revisión con contexto limpio más una de otra familia encontró 56,7 % de errores sembrados contra 42,7 % de dos revisiones del mismo modelo (Song, 2026, p = 0,006).
6. La base más sólida sigue siendo externa al revisor: tests escritos por un agente separado (precisión de tests 87,8 % contra 61,0 % con un solo agente; AgentCoder) y de solo lectura para el escritor (ImpossibleBench).
7. Ocultar la autoría al juez casi elimina la autopreferencia en un estudio (Chae y otros, 2026), pero la ofuscación tiene límite: con paráfrasis completa el sesgo vuelve (Mahbub y Feng, 2025).
8. Revisión diferida por la misma persona: el único resultado a favor (dos semanas de espera; Daneman y Stainton, 1993, n = 10 por condición) no se replicó con 64 participantes (Burgoyne y otros, 2022).
9. Checklists genéricas no mostraron beneficio (Hatton, 2008, 308 inspecciones; Porter y otros, 1995); las basadas en el historial propio de defectos (PSP) sí se asocian con menos defectos, con evidencia observacional.
10. Hueco central: ningún estudio mide defectos en producción de una persona sola con agentes según la configuración de revisión. Las recomendaciones de abajo salen de experimentos con errores sembrados y benchmarks, no de producción.

---

## Evidencia sobre autopreferencia, y si cambiar de familia la reduce

### Qué está medido sobre la autopreferencia

- **Reconocimiento y preferencia van juntos.** [medido] Panickssery, Bowman y Feng (arXiv 2404.13076, 2024-04-15): GPT-4 y Llama 2 distinguen sus propios textos de los de otros modelos y humanos sin ajuste fino, y hay una correlación lineal entre capacidad de autorreconocimiento y fuerza de la autopreferencia; el ajuste fino que mueve una mueve la otra.
- **Mecanismo de familiaridad.** [medido] Wataoka, Takahashi y Ri (arXiv 2410.21819, 2024): los LLM puntúan más alto que los humanos las salidas de menor perplejidad, sean o no propias. El sesgo sería preferencia por lo familiar, no por lo propio en sí.
- **La autopreferencia es dañina cuando el juez se equivocó como generador.** [medido] Chen, Wei, Zhu, Feng y Meng (arXiv 2504.03846, 2025): en tareas verificables, buena parte de la autopreferencia de los modelos fuertes está justificada (sus respuestas son mejores), pero cuando la propia respuesta es incorrecta Qwen2.5-72B la prefiere 86 % de las veces en MATH500, y en código (MBPP+) los modelos grandes muestran 50 a 75 % de preferencia dañina contra tasas base por debajo de 40 %. Generar razonamiento largo antes del veredicto reduce el sesgo dañino.
- **Punto ciego de autocorrección.** [medido] Tsui (Self-Correction Bench, arXiv 2507.02778, COLM 2026): sobre 14 modelos abiertos sin razonamiento, 64,5 % de punto ciego en promedio: corrigen un error si viene de afuera y no si es propio. Agregar "Wait" lo redujo 89,3 %. No evaluó modelos de razonamiento.
- **Es en parte un artefacto del rol del mensaje.** [medido] Chen, Su y Chiang (arXiv 2606.05976, 2026-06-04): reetiquetar la misma afirmación como proveniente de otro rol del chat subió la tasa de corrección explícita entre 23 y 93 puntos, con efecto significativo en 10 de 13 combinaciones de modelo y dominio.
- **Saber quién es el autor sesga en ambas direcciones.** [medido] Chae y otros (arXiv 2608.18091, 2026): con evaluación ciega la autopreferencia en gran parte desapareció; con etiquetas de autoría visibles, los jueces inflaron lo atribuido a sí mismos y bajaron lo atribuido a otros, sin importar la fuente real.
- **La ofuscación tiene techo.** [medido] Mahbub y Feng (arXiv 2512.05379, 2025-12-05): reemplazar algunos sinónimos reduce la autopreferencia, pero al neutralizar el estilo con paráfrasis completa la preferencia vuelve; el reconocimiento opera en varios niveles semánticos.
- **En jueces de software el problema mayor puede ser el prompt, no el autor.** [medido] Zhao, Esmaeili y Fard (arXiv 2604.16790, abril de 2026): con el mismo código, cambiar la posición o agregar señales de autoridad o "refinado" movió la precisión de un juez chico de 86 % a 17 %; en GPT, un distractor bajó la precisión en generación de tests de 77,46 % a 62,51 %.

### ¿Cambiar de familia o de proveedor la reduce?

- [medido] Spiliopoulou y otros (arXiv 2508.06709, 2025-08-08): GPT-4o y Claude 3.5 Sonnet puntúan más alto sus propias salidas y también las de otros modelos de su misma familia (sesgo de familia), con más de 5.000 pares anotados por expertos y nueve jueces.
- [medido] Awuni y otros (arXiv 2609.17857, 2026-09-15): con cuatro familias abiertas y 9.312 juicios, las cuatro muestran un "favor" a la misma familia de 3,4 a 8,4 puntos (p = 0,0002), y cambiar la composición del panel respecto de uno balanceado cambia 18,5 % de los resultados por pares. Controlar calidad, estilo y longitud casi no cambia el coeficiente.
- [medido] Verga y otros (Cohere, "Replacing Judges with Juries", arXiv 2404.18796, 2024): un panel de tres modelos chicos de familias distintas correlacionó mejor con humanos que GPT-4 solo (Pearson 0,917 contra 0,817 en Chatbot Arena), mostró menos sesgo intramodelo y costó unas siete veces menos. Tareas de QA y chat, no código.
- **Límite.** El crudo previo registró que los modelos más capaces se equivocan parecido aun entre proveedores (Kim y otros, ICML 2025). Cambiar de familia ataca el sesgo de preferencia, no la correlación de errores.

**Lectura.** Hay evidencia medida de que un juez de otra familia reduce el sesgo de autopreferencia y de familia, y de que ocultar la autoría ayuda. No hay evidencia de que lo vuelva independiente. Para código, ver la sección S1: el efecto depende de la capacidad del revisor y de la dirección del par.

---

## Soluciones

### S1. Revisor de otra familia o de otro proveedor

- **Quién lo propone y dónde.** [testimonio] En Hacker News, "Codex vs. Claude Code (today)" (2025-12-22, https://news.ycombinator.com/item?id=46391391), el usuario veidr cuenta que hace que Codex revise a Claude y viceversa, y que cuando discrepan lo resuelven con tests; advierte que Codex a veces inventa bugs de concurrencia y Claude tiende a omitir sin inventar. En el hilo del lanzamiento de la revisión de código de Claude Code (marzo de 2026, https://news.ycombinator.com/item?id=47313787) aparecen flujos parecidos.
- **Qué resuelve.** Ataca la autopreferencia y el sesgo de familia.
- **Evidencia.** [medido] Xiang, Zhang, Zhang y Xu ("Cross-Model LLM Code Review", arXiv 2607.21656, 2026-07-22, Agentic SE @ KDD'26), 116 tareas de LiveCodeBench: Codex solo 71,6 %; revisado por Claude 89,7 % (p = 0,001); autorrevisión de Codex 84,5 % (p = 0,022). Claude solo 91,4 %; revisado por Codex 82,8 % (p = 0,046); autorrevisión de Claude sin cambios. Claude revisando a Codex produjo 26 arreglos y 5 regresiones; Codex revisando a Claude, 3 arreglos y 13 regresiones. [medido] Song ("When Does a Second Model Help?", arXiv 2610.01471, 2026-10-01): 30 artefactos con 150 errores sembrados, 900 sesiones; la revisión de otra familia (GPT-5.4) obtuvo F1 32,3 % contra 28,6 % del contexto limpio con el mismo modelo, diferencia no significativa; en código ganó el contexto limpio (F1 40,7 %) y en documentos la otra familia (hasta 42,1 %); el revisor liviano (Gemini 2.5 Flash) no superó a la autorrevisión.
- **Críticas y límites.** El revisor puede empeorar código correcto si reescribe en vez de corregir (Xiang y otros). En Song, capacidad del revisor e identidad del modelo quedan confundidas, todos los artefactos vienen de un solo generador y los errores son sembrados. Ningún estudio mide defectos en producción.
- **Costo para una persona.** Una segunda suscripción o API. Xiang y otros estiman unos USD 1,40 por arreglo neto con Claude revisando a Codex. Más tiempo para arbitrar discrepancias.
- **Combinabilidad.** Con S2 (sumar una revisión con contexto limpio da la mejor cobertura medida) y con S5 (arbitrar con ejecución, como hace el testimonio de veidr).

### S2. Revisión con contexto limpio

- **Quién lo propone y dónde.** [opinión, guía de proveedor] Documentación de Claude Code, "Best practices" (https://code.claude.com/docs/en/best-practices, consultada 2026-10-08): propone un patrón escritor/revisor en sesiones separadas y un paso de revisión adversarial con un subagente que ve solo el diff y los criterios, no el razonamiento que produjo el cambio; afirma que una sesión nueva no queda sesgada hacia el código que acaba de escribir.
- **Qué resuelve.** El anclaje en el razonamiento del escritor y el punto ciego de autocorrección.
- **Evidencia.** [medido] Song ("Cross-Context Review", arXiv 2603.12123, 2026-03-12, revisado 2026-10-01): con 150 errores sembrados, la revisión en sesión nueva (F1 28,6 %) superó a repetir la revisión en la misma sesión (21,7 %, p ajustado = 0,004). Pero en la versión revisada, al promediar corridas, no fue significativamente mejor que una sola autorrevisión en la misma sesión (27,1 %; p = 0,26). [medido] Tsui (2025) y Chen, Su y Chiang (2026): presentar el mismo error como ajeno sube mucho la corrección, lo que es consistente con el mecanismo.
- **Críticas y límites.** El resultado robusto es "no repetir la revisión en la misma sesión", no "el contexto limpio gana". El mismo modelo con contexto limpio sigue reconociendo su estilo (Panickssery y otros; Mahbub y Feng).
- **Costo para una persona.** Muy bajo: una sesión o subagente más.
- **Combinabilidad.** Base natural de S1, S3 y S5. Se potencia con evaluación ciega (no decirle al revisor quién escribió el código; Chae y otros).

### S3. Revisión diferida en el tiempo por la misma persona

- **Quién lo propone y dónde.** [opinión] Josh Sherman, "Solo developers should still do code reviews" (2019-03-18, https://joshtronic.com/2019/03/18/solo-developers-should-still-do-code-reviews/): abrir un PR y revisarlo al día siguiente "como si no fuera el autor"; cuenta que así evitó "un par" de bugs en producción [testimonio].
- **Qué resuelve.** La sobrefamiliaridad del autor con lo que escribió.
- **Evidencia.** [medido] Daneman y Stainton (1993), según la revisión de Burgoyne y otros: los estudiantes detectaron menos errores en su propio ensayo recién escrito, y a las dos semanas lo corrigieron tan bien como uno ajeno ya conocido; las muestras eran de 10 por condición. [medido] Burgoyne, Saba-Sadiya, Harris, Becker, Brascamp y Hambrick (*Psychological Research*, 2022): con 64 participantes y una segunda sesión a la semana, el experimento 1 no encontró efecto de autogeneración y el experimento 2 lo encontró débil y no significativo. [testimonio] Abrahamsson y Kautz (2002), relato de un estudiante del curso PSP: revisar el diseño solo le resultó muy difícil y la revisión con un compañero mejoró el diseño.
- **Críticas y límites.** La evidencia es de corrección de textos, no de código. La base empírica a favor es chica y no replicó. Para quien trabaja con agentes hay un matiz: la persona no escribió el código, así que la sobrefamiliaridad aplica menos al código y más a la especificación o al plan que sí escribió.
- **Costo para una persona.** Latencia (un día por cambio) más que horas.
- **Combinabilidad.** Con S4: diferir la revisión humana de la especificación y del resultado contra ella, no de cada línea.

### S4. Revisar contra la especificación, el plan o los tests, no contra el código

- **Quién lo propone y dónde.** [opinión, guía de proveedor] Claude Code "Best practices": revisar el diff contra el plan, verificar que cada requisito esté implementado y que los casos borde tengan tests, y empezar la implementación en una sesión nueva a partir de una especificación escrita. [testimonio] Shachar Azriel (Baz), AI Native DevCon, junio de 2026 (transcripción: https://tessl.io/registry/ainativedev/aidevcon-2026-ldn/files/talk-azriel-executable-specs-agentic-coding/transcript.md): verificar la funcionalidad desplegada en staging contra la especificación, con agentes separados para planificar y verificar.
- **Qué resuelve.** Saca el juicio del terreno donde el revisor reconoce el estilo (el código) y lo lleva a un criterio externo escrito antes.
- **Evidencia.** [medido, inspección humana] Porter, Votta y Basili (1995), según Basili y otros (*Empirical Software Engineering*, 1996): en inspección de requisitos, leer con escenarios por tipo de defecto rindió cerca de 35 % más que la lectura ad hoc o con checklist. [medido, en contra] Jin y Chen (arXiv 2603.00539, 2026-02-28): al juzgar conformidad con requisitos, los LLM marcan como no conforme código correcto, y los prompts más detallados (con explicación y corrección propuesta) empeoran la tasa de error. Proponen validar la corrección propuesta con tests. [testimonio] Azriel: con 10 a 15 requisitos verificados en secuencia, la calidad del agente verificador se degradó.
- **Críticas y límites.** Un agente ejecuta con la misma fidelidad una especificación equivocada; si la persona escribió la especificación, su sesgo se traslada ahí. No hay estudio que compare, para una persona con agentes, revisar código contra revisar especificación.
- **Costo para una persona.** Escribir la especificación antes; es tiempo que se mueve, no que se agrega, según la guía de proveedor (sin medición).
- **Combinabilidad.** Con S5 (la especificación se vuelve tests) y con S3 (lo que la persona revisa en diferido es la especificación).

### S5. Tests escritos antes, o por un agente separado que el escritor no puede editar

- **Quién lo propone y dónde.** [opinión] Simon Willison, "Vibe engineering" (2025-10-07, https://simonwillison.net/2025/Oct/7/vibe-engineering/): una suite de tests robusta como primera condición del trabajo con agentes. Claude Code "Best practices": un agente escribe los tests y otro el código que los pasa.
- **Qué resuelve.** Reemplaza el juicio de un revisor por una señal externa ejecutable que no depende de la autopreferencia.
- **Evidencia.** [medido] Huang y otros (AgentCoder, arXiv 2312.13010): con GPT-3.5 en HumanEval, un solo agente que escribe código y tests llegó a 71,3 % de pass@1 y 61,0 % de precisión de tests; con un agente diseñador de tests separado, 79,9 % y 87,8 %. Los autores atribuyen parte de la diferencia a que los tests escritos después de ver el código heredan sus puntos ciegos. [medido] Zhong, Raghunathan y Carlini (ImpossibleBench, arXiv 2510.20270, 2025-10-23): GPT-5 hizo trampa en 54 % de tareas imposibles de SWE-bench; los tests de solo lectura eliminan la modificación de tests y los ocultos llevan la trampa casi a cero, a costa de rendimiento legítimo; permitir varios envíos subió la trampa unos 5 puntos. [medido] Kamoi y otros (TACL, 2024) y Huang y otros (ICLR 2024): la autocorrección funciona con retroalimentación externa confiable y no con retroalimentación generada por el propio modelo. [medido, matiz] Fucci y otros (arXiv 1611.05994, 2016; 39 profesionales): el orden test antes o después no tuvo influencia importante; lo que se asoció con calidad fue avanzar en pasos chicos y uniformes.
- **Críticas y límites.** Lo que importa según la evidencia es la separación (quién escribe los tests y si el escritor los puede tocar), no tanto el "antes". Un juez ejecutable solo cubre lo que los tests expresan. Si la misma persona escribe especificación y tests, el sesgo de la especificación pasa a los tests.
- **Costo para una persona.** Bajo con agentes: un agente más y permisos de solo lectura sobre el directorio de tests.
- **Combinabilidad.** Es la base de todas. Con S6 se vuelve imposible de saltear.

### S6. Branch protection y CI obligatorios aunque seas solo

- **Quién lo propone y dónde.** [testimonio] GitHub Community, "How to protect master branch on solo-developer projects?" (2020-10-15, https://github.com/orgs/community/discussions/23727): el que pregunta señala que no puede aprobar su propio PR; la respuesta propuesta es exigir checks de estado sin exigir revisiones e incluir a los administradores. [opinión, documentación] GitHub, "About protected branches": por defecto las reglas no aplican a administradores, salvo que se active; se puede exigir que el último push lo apruebe otra persona. GitHub Changelog (2021-11-10): exigir PR sin exigir revisión pasó a ser una opción separada.
- **Qué resuelve.** No es revisión: es un control que impide que la persona, con prisa, saltee S5. Corresponde a la idea de COSO de restringir la anulación de controles por la dirección (S10).
- **Evidencia.** [medido, observacional, fuente secundaria] Vasilescu y otros (ESEC/FSE 2015), según un resumen en DEV Community (el original en ACM devolvió 403): en 246 proyectos de GitHub, los equipos con CI integraron más contribuciones sin pérdida observable de calidad y sus desarrolladores principales encontraron más bugs. [medido, correlacional] Santos, da Costa y Kulesza (ESEM 2022, arXiv 2208.02598; 90 proyectos): actividad y salud del build y tiempo de arreglo de builds rotos se correlacionaron con issues de bugs.
- **Críticas y límites.** Ningún estudio mide esto para una persona sola. La persona sigue siendo administradora: puede desactivar la regla. El control vale como fricción y registro, no como independencia.
- **Costo para una persona.** Minutos de configuración y minutos de CI por cambio.
- **Combinabilidad.** Hace obligatorios S5 y los checks automáticos de S1 y S2 si se corren en CI.

### S7. Prompts adversariales o "red team" del propio código

- **Quién lo propone y dónde.** [opinión, guía de proveedor] Claude Code "Best practices", sección "Add an adversarial review step"; la misma guía advierte que un revisor al que se le pide encontrar huecos casi siempre reporta alguno aunque el trabajo esté bien, y que perseguirlos todos lleva a sobreingeniería.
- **Qué resuelve.** Activa la capacidad de corrección que el modelo no usa sobre lo propio.
- **Evidencia.** [medido] Tsui (2025): un simple "Wait" redujo el punto ciego 89,3 %. [medido, en contra] Kamoi y otros (2024): no hay trabajo que muestre autocorrección exitosa con retroalimentación de LLM por prompt, salvo tareas muy aptas. Jin y Chen (2026): pedir explicaciones y correcciones aumenta los falsos positivos. [testimonio] jgraettinger1, en https://news.ycombinator.com/item?id=47313787 (marzo de 2026): al usar Claude o Codex para autorrevisión, el modelo "siempre encuentra unos 8 problemas" sin importar cuántos haya.
- **Críticas y límites.** Convierte un sesgo de aprobación en un sesgo de objeción. Sin una forma barata de separar señal de ruido (S5), sube el costo de arbitraje.
- **Costo para una persona.** Bajo en tokens, alto en atención para descartar falsos positivos.
- **Combinabilidad.** Solo útil acoplado a S5 (validar cada hallazgo con un test que falle) y con la instrucción de reportar solo lo que afecta corrección o requisitos.

### S8. Votación o panel entre varios modelos

- **Quién lo propone y dónde.** Verga y otros (Cohere, 2024); Ron, Baudry y Monperrus (N-version con agentes, 2026, relevado en el crudo previo).
- **Qué resuelve.** Diluye el sesgo de un juez y aprovecha que distintos revisores encuentran cosas distintas.
- **Evidencia.** [medido] PoLL: mejor correlación con humanos y menos sesgo intramodelo que un juez grande (sección de autopreferencia). [medido] Smit y otros (ICML 2024) y Zhang y otros (arXiv 2502.08788, 2025): el debate multiagente no supera de forma confiable a self-consistency o a cadena de pensamiento, aun gastando más; la heterogeneidad de modelos lo mejora de forma consistente. [testimonio con datos públicos] v.j.k., "Best AI Code Reviewer in 2026?" (DEV Community, 2026-05-12): equipo chico de SaaS, cuatro revisores comerciales en paralelo sobre 146 PR y 679 hallazgos; 93,4 % de las ubicaciones marcadas las marcó un solo revisor. El autor trabaja en uno de los proveedores y lo declara; dataset en github.com/vlad-ko/pr-review-bench.
- **Críticas y límites.** Si los revisores casi no coinciden, la votación por mayoría descartaría casi todo; sirve más la unión filtrada por ejecución que el voto. La composición del panel cambia el veredicto (18,5 % en Awuni y otros).
- **Costo para una persona.** Multiplica tokens y, sobre todo, el arbitraje.
- **Combinabilidad.** Variante cara de S1; se justifica para cambios irreversibles.

### S9. Mercados o comunidades de revisión entre pares

- **Quién lo propone y dónde.** [testimonio] "Ask HN: Paid code review services for solo developers?" (2012-09-27, https://news.ycombinator.com/item?id=4581810): recomiendan intercambiar revisiones con alguien en la misma situación y Code Review Stack Exchange. [testimonio] "Code Review as a Service" (2021-12-20, https://news.ycombinator.com/item?id=29623505): PullRequest.com a USD 699 por mes; un desarrollador solo (dirtbag__dad) valoró la calidad y la variedad de miradas pero mencionó demoras y falta de contexto; otros comentaristas objetaron que un externo sin contexto del dominio no ve los problemas de arquitectura.
- **Qué resuelve.** Es la única opción que da independencia real de criterio (otra persona).
- **Evidencia.** [medido, fuera de código] El crudo de tiny teams ya relevó que el consejo de pares mejoró crecimiento y supervivencia de firmas (Chatterji y otros, 2019), sin evidencia de que funcione como validador independiente. Para revisión de código pagada o intercambiada no se encontró medición.
- **Críticas y límites.** Contexto, demora, confidencialidad del código y costo. Escala mal a cada cambio.
- **Costo para una persona.** Alto por cambio; razonable solo para hitos o para lo irreversible.
- **Combinabilidad.** Con S10: el par externo audita una muestra o los cambios de mayor radio de daño.

### S10. Controles compensatorios por muestreo (COSO)

- **Quién lo propone y dónde.** [opinión, guía] COSO, guía para empresas públicas chicas (2006), según el resumen de Cydney Posner en Cooley (2006-07-11, https://www.cooley.com/news/insight/2006/new-coso-guidance-for-smaller-companies): reconoce recursos insuficientes para separar funciones y la capacidad de la dirección de saltearse controles; propone que quien dirige revise reportes, elija transacciones para verificar su respaldo, haga conteos y revise conciliaciones, y que el software externo incorpore controles. [opinión, experimento de seguridad] Greenblatt y otros ("AI Control", arXiv 2312.06942): un modelo no confiable, uno confiable más débil y trabajo humano escaso reservado para auditar lo más sospechoso.
- **Qué resuelve.** Reemplaza "otra persona aprueba cada acción" por "la persona audita una muestra contra evidencia", que es viable con una sola persona.
- **Evidencia.** No se encontró medición de la eficacia de los controles compensatorios en software ni en una persona sola. La tasa de 2 % de AI Control (crudo previo) es un parámetro de experimento.
- **Críticas y límites.** La persona que audita la muestra es la misma que diseñó el sistema; el muestreo aleatorio solo vale si lo elige algo que ella no controla (un script con semilla registrada, por ejemplo). Sin una tasa de defectos conocida (defectos sembrados, crudo previo C2) no se sabe qué detecta la muestra.
- **Costo para una persona.** Proporcional a la tasa de muestreo; es el control humano más barato por unidad de cobertura.
- **Combinabilidad.** Es la capa humana encima de S1 a S8; con S9 para que la muestra la mire un externo de vez en cuando.

### S11. Checklists

- **Quién lo propone y dónde.** Humphrey, PSP (SEI, década de 1990): revisión personal de diseño y código con checklist armada a partir de los defectos que uno mismo registra. Guías de proveedores de revisión (sin medición).
- **Qué resuelve.** Que la autorrevisión no dependa de la memoria y apunte a los errores propios recurrentes.
- **Evidencia.** [medido, en contra de checklists genéricas] Hatton ("Testing the value of checklists in code inspections", *IEEE Software* 25(4), 2008; página del autor): 308 inspecciones sobre el mismo código, sin resultados significativos a favor de las checklists. [medido] Porter, Votta y Basili (1995), según Basili y otros (1996): la lectura con checklist no fue más efectiva que la ad hoc. [medido, observacional] Hayes y Over (SEI, CMU/SEI-97-TR-001, 1997; 298 ingenieros) reportaron una reducción de la densidad total de defectos en un factor de 1,5, según Abrahamsson y Kautz (2002); en su propio curso, Abrahamsson y Kautz vieron bajar la mediana de 67 a 48 defectos por KLOC y los defectos encontrados en test de 10 a 5 por KLOC.
- **Críticas y límites.** Los datos de PSP los registra el mismo desarrollador sobre sí mismo, y el efecto de la revisión no está aislado del resto del proceso. La checklist genérica no tiene respaldo.
- **Costo para una persona.** Bajo si la checklist sale del historial de defectos; con agentes, ese historial puede salir de los hallazgos rechazados y aceptados.
- **Combinabilidad.** Mejor como insumo de S4 y S5 (cada ítem recurrente se vuelve un test o un check de CI) que como lista para leer.

---

## Tabla de combinabilidad y costo

Costo para una persona: bajo = minutos por cambio o configuración única; medio = suscripción adicional o arbitraje frecuente; alto = pago por cambio o latencia de días.

| | Evidencia | Costo | S1 otra familia | S2 contexto limpio | S3 diferida | S4 contra especificación | S5 tests separados | S6 CI y protección | S7 adversarial | S8 panel | S9 pares | S10 muestreo | S11 checklist |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **S1** | medido, mixto | medio | | suma cobertura | neutro | complementa | arbitra | se automatiza | tensión (ruido) | lo incluye | neutro | alimenta | neutro |
| **S2** | medido, débil | bajo | suma cobertura | | neutro | complementa | complementa | se automatiza | lo habilita | base | neutro | alimenta | neutro |
| **S3** | medido, no replicado | medio (latencia) | neutro | neutro | | se aplica a la especificación | neutro | neutro | neutro | neutro | complementa | complementa | complementa |
| **S4** | medido humano, LLM en contra | bajo a medio | complementa | complementa | se le aplica | | se traduce en | neutro | tensión (falsos positivos) | neutro | complementa | define qué muestrear | insumo |
| **S5** | medido | bajo | arbitra | complementa | neutro | sale de | | se vuelve obligatorio | filtra | filtra | neutro | da la señal | absorbe |
| **S6** | guía, observacional | bajo | ejecuta | ejecuta | neutro | neutro | protege | | neutro | ejecuta | neutro | registra | neutro |
| **S7** | medido, mixto | bajo tokens, alto atención | ruido | se apoya | neutro | ruido | necesita | neutro | | variante | neutro | neutro | neutro |
| **S8** | medido fuera de código | medio a alto | generaliza | incluye | neutro | neutro | necesita | ejecuta | incluye | | neutro | alimenta | neutro |
| **S9** | testimonio | alto | neutro | neutro | complementa | revisa | neutro | neutro | neutro | neutro | | audita la muestra | neutro |
| **S10** | guía | proporcional | se apoya | se apoya | complementa | se apoya | se apoya | registra | neutro | se apoya | lo usa | | neutro |
| **S11** | medido en contra (genérica), observacional (PSP) | bajo | neutro | neutro | complementa | insumo | se absorbe en | neutro | neutro | neutro | neutro | neutro | |

Lectura: S5 y S6 son la base y no dependen de un revisor. S1 y S2 forman el par con mejor cobertura medida y necesitan S5 para arbitrar. S7 y S8 multiplican hallazgos y ruido. S3, S9, S10 y S11 son las capas humanas: ninguna tiene medición en software para una persona.

## Combinación mínima que respalda la evidencia para una persona sola

Criterio: solo entra lo que tiene medición a favor en el escenario más parecido; lo que es guía va marcado como tal.

1. **Tests escritos por un agente separado, de solo lectura para el escritor** (S5). Mayor efecto medido (AgentCoder, ImpossibleBench) y apoyado por el resultado general de que la autocorrección funciona con retroalimentación externa (Kamoi y otros).
2. **Revisión automática en dos pasadas distintas: una con contexto limpio del mismo modelo y una de otra familia, sin decirle a ninguna quién escribió el código** (S2, S1 y evaluación ciega). Es la combinación con mejor cobertura medida (56,7 % contra 42,7 %, Song, 2026) y la evaluación ciega redujo la autopreferencia (Chae y otros, 2026). El revisor de otra familia tiene que ser de capacidad comparable o mayor: uno liviano no aportó (Song) y uno que reescribe puede empeorar (Xiang y otros).
3. **Ningún hallazgo del revisor se aplica sin un test que falle antes y pase después** (S5 sobre S1, S2 y S7). La evidencia de regresiones (13 contra 3 en Xiang y otros) y de sobrecorrección (Jin y Chen) obliga a este filtro.
4. **CI obligatorio con la regla aplicada también al administrador** (S6). La evidencia es guía y observacional, pero es lo que hace que 1 a 3 no dependan de la disciplina del momento.

Lo que queda afuera de la combinación mínima por falta de evidencia, no por falta de valor: la revisión humana diferida (S3, no replicada), el muestreo compensatorio (S10, solo guía) y el par externo (S9, solo testimonio). Para lo irreversible, el crudo de tiny teams ya dejó planteado que la segunda persona tiene que ser externa o que la excepción se acepta por escrito; esta búsqueda no encontró nada que lo reemplace.

## Huecos

- **Producción.** Ningún estudio mide defectos en producción de una persona sola con agentes según cómo se revisa. Todo lo medido es con errores sembrados o benchmarks (Song; Xiang y otros; AgentCoder).
- **Código de agentes revisado por agentes de otra familia, a escala.** Los dos estudios directos (Song, 2026; Xiang y otros, 2026) son recientes, con un generador o un par de modelos, y uno es de un solo autor.
- **Revisión humana diferida de código.** La evidencia es de corrección de textos y no replicó; no se encontró estudio con código.
- **Muestreo compensatorio en software.** No hay tasa de muestreo medida ni estudio de eficacia; COSO es guía contable.
- **Mercados de revisión.** Solo testimonios; no se encontraron datos de defectos detectados por revisores pagos o por intercambio.
- **Reddit e Indie Hackers.** No pudieron abrirse; la voz de practicantes queda sesgada hacia Hacker News.
- **Fuentes vistas solo en resultados de búsqueda y no usadas como evidencia:** Johnson y Disney sobre calidad de datos en PSP, la cifra de Hatton sobre equipos de dos personas, el original de Vasilescu y otros (ACM, 403) y el de Daneman y Stainton (Springer, requiere login; se cita a través de Burgoyne y otros).
- **Separación de funciones con una persona.** Sigue sin aparecer una propuesta que dé independencia real sin una segunda persona; lo relevado reduce el sesgo, no lo elimina.

## Fuentes (consultadas el 2026-10-08)

- Abrahamsson y Kautz, "The Personal Software Process: Experiences from Denmark", EUROMICRO 2002, versión de autor en arXiv 1903.10893: https://arxiv.org/pdf/1903.10893
- Abrahamsson, Kautz, Sieppi y Lappalainen, "Improving Software Developer's Competence: Is the Personal Software Process Working?", 2002, arXiv 1311.0228: https://arxiv.org/abs/1311.0228
- Anthropic, "Best practices for Claude Code" (documentación, sin fecha visible): https://code.claude.com/docs/en/best-practices
- Awuni y otros, "Who Judges Matters: Measuring Family-Conditioned Preference in LLM-as-Judge Panels", arXiv 2609.17857, 2026-09-15: https://arxiv.org/abs/2609.17857
- Azriel (Baz), "Executable specs", AI Native DevCon, junio de 2026, transcripción: https://tessl.io/registry/ainativedev/aidevcon-2026-ldn/files/talk-azriel-executable-specs-agentic-coding/transcript.md
- Basili y otros, "The Empirical Investigation of Perspective-Based Reading", *Empirical Software Engineering*, 1996 (incluye el resultado de Porter, Votta y Basili, 1995): https://www.cs.umd.edu/~mvz/handouts/emp_pbr.pdf
- Burgoyne y otros, "Revisiting the self-generation effect in proofreading", *Psychological Research*, 2022 (incluye el resultado de Daneman y Stainton, 1993): https://englelab.gatech.edu/articles/2022/Burgoyne%20et%20al.%20(2022)%20Revisiting%20the%20self-generation%20effect%20in%20proofreading.pdf
- Chae y otros, "Self- and Other-Labels Induce Bidirectional Bias in LLM Judges", arXiv 2608.18091, 2026: https://arxiv.org/abs/2608.18091
- Chen, Su y Chiang, "The Self-Correction Illusion", arXiv 2606.05976, 2026-06-04: https://papers.cool/arxiv/2606.05976
- Chen, Wei, Zhu, Feng y Meng, "Do LLM Evaluators Prefer Themselves for a Reason?", arXiv 2504.03846: https://arxiv.org/html/2504.03846v3
- Cooley (Posner), "New COSO guidance for smaller companies", 2006-07-11: https://www.cooley.com/news/insight/2006/new-coso-guidance-for-smaller-companies
- DEV Community (a3e_ecosystem), resumen de Vasilescu y otros, ESEC/FSE 2015: https://dev.to/a3e_ecosystem/ci-does-not-buy-you-speed-or-quality-it-buys-you-both-5g9m
- Fucci, Erdogmus, Turhan, Oivo y Juristo, "A Dissection of the Test-Driven Development Process", arXiv 1611.05994, 2016: https://arxiv.org/abs/1611.05994
- GitHub Docs, "About protected branches": https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- GitHub Changelog, "Require pull requests without requiring reviews", 2021-11-10: https://github.blog/changelog/2021-11-10-require-pull-requests-without-requiring-reviews/
- GitHub Community, "How to protect master branch on solo-developer projects?", 2020-10-15: https://github.com/orgs/community/discussions/23727
- Greenblatt, Shlegeris, Sachan y Roger, "AI Control", arXiv 2312.06942: https://arxiv.org/abs/2312.06942
- Hacker News, "Ask HN: Paid code review services for solo developers?", 2012-09-27: https://news.ycombinator.com/item?id=4581810
- Hacker News, "Code Review as a Service", 2021-12-20: https://news.ycombinator.com/item?id=29623505
- Hacker News, "Codex vs. Claude Code (today)", 2025-12-22: https://news.ycombinator.com/item?id=46391391
- Hacker News, "Code Review for Claude Code", marzo de 2026: https://news.ycombinator.com/item?id=47313787
- Hatton, "Testing the value of checklists in code inspections", *IEEE Software* 25(4), 2008, página del autor: https://leshatton.org/checklists_in_code_inspections.html
- Hayes y Over, "The Personal Software Process: An Empirical Study of the Impact of PSP on Individual Engineers", CMU/SEI-97-TR-001, 1997: https://www.sei.cmu.edu/library/the-personal-software-process-psp-an-empirical-study-of-the-impact-of-psp-on-individual-engineers
- Huang y otros, "AgentCoder", arXiv 2312.13010: https://arxiv.org/html/2312.13010v2
- Huang, Chen y otros, "Large Language Models Cannot Self-Correct Reasoning Yet", ICLR 2024, arXiv 2310.01798: https://arxiv.org/abs/2310.01798
- Jin y Chen, "Are LLMs Reliable Code Reviewers?", arXiv 2603.00539, 2026-02-28: https://arxiv.org/abs/2603.00539
- Kamoi, Zhang, Zhang, Han y Zhang, "When Can LLMs Actually Correct Their Own Mistakes?", TACL 2024, arXiv 2406.01297: https://arxiv.org/abs/2406.01297
- Mahbub y Feng, "Mitigating Self-Preference by Authorship Obfuscation", arXiv 2512.05379, 2025-12-05: https://arxiv.org/abs/2512.05379
- Panickssery, Bowman y Feng, "LLM Evaluators Recognize and Favor Their Own Generations", arXiv 2404.13076, 2024-04-15: https://arxiv.org/abs/2404.13076
- Santos, da Costa y Kulesza, "Investigating the Impact of Continuous Integration Practices on the Productivity and Quality of Open-Source Projects", ESEM 2022, arXiv 2208.02598: https://arxiv.org/abs/2208.02598
- Sherman, "Solo developers should still do code reviews", 2019-03-18: https://joshtronic.com/2019/03/18/solo-developers-should-still-do-code-reviews/
- Smit y otros, "Should we be going MAD?", ICML 2024: https://proceedings.mlr.press/v235/smit24a.html
- Song, "Cross-Context Review", arXiv 2603.12123, 2026-03-12, revisado 2026-10-01: https://arxiv.org/abs/2603.12123
- Song, "When Does a Second Model Help? Cross-Model Review in LLM Verification", arXiv 2610.01471, 2026-10-01: https://arxiv.org/html/2610.01471v1
- Spiliopoulou y otros, "Play Favorites: A Statistical Method to Measure Self-Bias in LLM-as-a-Judge", arXiv 2508.06709, 2025-08-08: https://arxiv.org/abs/2508.06709
- Tsui, "Self-Correction Bench", arXiv 2507.02778, COLM 2026: https://arxiv.org/abs/2507.02778
- v.j.k., "Best AI Code Reviewer in 2026? We Ran 4 in Parallel for 3 Weeks", DEV Community, 2026-05-12: https://dev.to/_vjk/best-ai-code-reviewer-in-2026-we-ran-4-in-parallel-for-3-weeks-146-prs-679-findings-1c0f
- Verga y otros, "Replacing Judges with Juries", arXiv 2404.18796, 2024: https://arxiv.org/html/2404.18796v2
- Wataoka, Takahashi y Ri, "Self-Preference Bias in LLM-as-a-Judge", arXiv 2410.21819, 2024: https://arxiv.org/abs/2410.21819
- Willison, "Vibe engineering", 2025-10-07: https://simonwillison.net/2025/Oct/7/vibe-engineering/
- Xiang, Zhang, Zhang y Xu, "Cross-Model LLM Code Review: Should you use Claude to review Codex or vice versa?", arXiv 2607.21656, 2026-07-22: https://arxiv.org/html/2607.21656v1
- Zhang y otros, "Stop Overvaluing Multi-Agent Debate", arXiv 2502.08788, 2025: https://arxiv.org/abs/2502.08788
- Zhao, Esmaeili y Fard, "Bias in the Loop: Auditing LLM-as-a-Judge for Software Engineering", arXiv 2604.16790, abril de 2026: https://arxiv.org/html/2604.16790v1
- Zhong, Raghunathan y Carlini, "ImpossibleBench", arXiv 2510.20270, 2025-10-23: https://arxiv.org/html/2510.20270v1

No pudieron abrirse y no se usan como evidencia directa: Reddit (bloqueado para el agente), Indie Hackers (HTTP 403), Vasilescu y otros en ACM DL (HTTP 403), Daneman y Stainton en Springer (requiere login), eprints de Kingston para Hatton (DNS).
