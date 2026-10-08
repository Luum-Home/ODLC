---
tags: [fundacional, piloto, hipotesis]
status: borrador
created: 2026-10-08
---

# Piloto: combinación A

Diseño del piloto que pone a prueba la combinación A, "medir para aprender", de [[Síntesis - Cómo encajan las propuestas existentes]]. Contesta el punto 2 de "Qué haría falta para que tenga sentido" en [[Objeciones al marco]]: un piloto que mida la tesis con el criterio de abandono fijado antes de empezar.

**Estado:** borrador del protocolo. No está sellado. Se sella cuando el dueño resuelva las decisiones pendientes (sección 13); desde ese commit, cualquier cambio es un desvío declarado (sección 9).

Decisiones del dueño que esta nota no reabre: el sujeto es un MVP propio y nuevo, construido por el dueño solo o con un equipo mínimo, con sus suscripciones de IA, sin financiamiento externo y con clientes potenciales reales. El producto concreto es un parámetro. La duración es de 8 a 12 semanas. La comparación es de caso único, alternando períodos sin y con el método. El público del marco son los tiny teams y los bootstrappers, y todo lo que se arme tiene que ser demostrable.

## Resumen

1. **Lo que se puede demostrar es el caso, no el marco.** Un caso único bien diseñado muestra que el método funcionó para esa persona en ese MVP. Para generalizar una intervención, el What Works Clearinghouse exige la regla 5-3-20: al menos 5 estudios de caso único que cumplan sus estándares, hechos por al menos 3 equipos de investigación distintos en 3 lugares geográficos distintos, con al menos 20 experimentos en total (Kratochwill y otros, 2010). "Equipo" ahí es un grupo de investigadores independiente, no un equipo de trabajo (sección 12).
2. **Tesis:** a igualdad de horas humanas activas, trabajar con la combinación A produce más unidades de trabajo con outcome validado y menos trabajo descartado después de entregar que trabajar por flujo de ítems con los mismos agentes. En la revisión de cambios, humano más agente detecta al menos tanto como el mejor de los dos solos.
3. **El A-B-A-B elegido por el dueño tiene un problema de fondo.** Lo aprendido con el método no se desaprende, y la propia guía del WWC desaconseja el diseño de reversión cuando el efecto no se revierte. Se recomienda una **línea de base múltiple entre tres tipos de objetivo, con inicio sorteado**, y dentro de ella un **diseño de tratamientos alternantes** para la revisión de PR (humano solo, agente solo, humano más agente). Las dos opciones quedan especificadas y el script calcula las dos.
4. **Puntos de medición:** dos por semana (media semana). Con 12 semanas hay 24 puntos y cada fase de cada tipo de objetivo tiene al menos 5, como exige el WWC para cumplir sin reservas. La prueba de aleatorización tiene 162 asignaciones posibles, así que el p mínimo es 0,006. Con 8 semanas quedan 48 asignaciones (p mínimo 0,021).
5. **Fase 0, antes de la línea de base:** entre 10 y 15 entrevistas sobre hechos pasados, al estilo de The Mom Test, codificadas a ciegas por un segundo codificador, con acuerdo reportado. Si el problema no se confirma, el piloto no arranca.
6. **Medidas primarias:** P1, unidades con outcome validado por período (evidencia de nivel 2 o más dentro de los 28 días posteriores a la entrega). P2, tasa de unidades descartadas después de entregar. Las dos salen de archivos y timestamps del repo del MVP; ninguna medida usa autoinforme.
7. **Con pocos clientes, la evidencia es una escalera:** uso, compromiso de tiempo o reputación, y compromiso de pago. La preventa es el escalón más fuerte. Los usuarios simulados con LLM se registran pero valen cero: filtran, no validan.
8. **Seis criterios de abandono** (K0 a K5) y una regla de decisión fijada de antemano, con tres salidas: sostiene, descarta o ambiguo. Con un resultado ambiguo no se declara apoyo y no se extiende el piloto para buscar significancia.
9. **Pre-registro verificable:** el protocolo se commitea, su SHA-256 queda como sello, y el script se niega a calcular (exit 2) si el protocolo cambió sin un desvío encadenado. La asignación de inicios, el sorteo de condiciones de revisión y el manifiesto de defectos sembrados usan compromiso y revelación (commit-reveal).
10. **Script:** `scripts/piloto_metricas.py` (solo stdlib, read-only y determinista). Sobre el fixture ficticio da AMBIGUO: la tasa de outcome sube de 0,17 a 0,81, pero p = 0,123 con 24 puntos ralos. Es la advertencia principal del diseño: con el volumen de una sola persona, el límite es la cantidad de unidades, no la estadística.

---

## 1. Alcance: qué prueba este piloto y qué no

| Pregunta | Este piloto la contesta | Por qué |
|---|---|---|
| ¿La combinación A mejoró el trabajo de esta persona en este MVP? | Sí, si se cumple la regla de decisión | Un diseño de caso único con tres demostraciones del efecto es la evidencia que el WWC acepta para un caso |
| ¿ODLC funciona para tiny teams en general? | No | Hace falta la regla 5-3-20 del WWC (sección 12). Este piloto es, como mucho, el primero de esa serie |
| ¿El producto tiene mercado? | No es la pregunta | El outcome del producto es la variable que mide el método, no el objeto del piloto. Un producto sin tracción vuelve no informativo al piloto (criterio K4) |
| ¿Qué componente de A explica el efecto? | Solo para la revisión | La revisión se compara contra sus componentes solos; el resto del método entra como paquete |

Seth Roberts presenta la autoexperimentación como fuente de hipótesis, no como prueba de generalidad (citado en [[Investigación - Tiny teams y bootstrapping]]). Ese es el techo honesto de un n = 1.

## 2. Tesis pre-registrada

### H1 (primaria)

> En el MVP <producto, decisión pendiente>, durante <8 a 12> semanas, con las horas humanas activas por semana dentro de ±20 % entre fases, las unidades de trabajo que se hacen con la combinación A producen **más unidades con outcome validado por período (P1)** y **una tasa de descarte después de entregar igual o menor (P2)** que las unidades que se hacen por flujo de ítems con los mismos agentes y suscripciones.

**Contraste con el mejor componente solo.** Vaccaro, Almaatouq y Malone (2024) encontraron, en un metaanálisis de 106 experimentos, que en promedio la combinación humano más IA rinde peor que el mejor de los dos por separado (g = −0,23; citado en [[Propuestas existentes - Objeciones 3 y 4]]). Por eso la comparación contra "humano más agente sin método" no alcanza. En este piloto el contraste se hace donde existe una verdad conocida: la revisión de cambios con defectos sembrados.

### H2 (revisión, contra el mejor componente)

> En la revisión de PR durante la fase con método, la tasa de detección de defectos sembrados en la condición humano más agente (HA) no es menor que la mayor de las tasas de humano solo (H) y agente solo (A).

### H3 (secundaria, de Camuffo)

> Con el método, las unidades que no validan se abandonan antes de entregarse y en menos días.

Camuffo y otros (2020, 116 startups) y su réplica (2024, 759 firmas, cuatro ensayos) encuentran que el enfoque científico lleva a abandonar más ideas malas. En la réplica, el efecto replicado es ese (citado en [[Investigación - Tiny teams y bootstrapping]]). H3 separa dos cosas que la tesis original de [[Objeciones al marco]] mezclaba como "trabajo descartado": abandonar una unidad antes de construirla es barato y esperable con el método; descartarla después de entregarla es desperdicio. P2 mide solo lo segundo.

### H4 (exploratoria, de la Objeción 5)

> Las métricas de pasividad y la detección de semillas anticipan los defectos que llegan a producción.

Es la condición de refutación que [[Objeciones al marco]] deja escrita para los principios 3 y 4. Con el volumen de un piloto de una persona no hay potencia para una correlación, así que H4 se reporta como descriptiva y no entra en la regla de decisión.

### Términos y métricas

| Término de la tesis | Métrica computable | Campo de origen |
|---|---|---|
| Unidad de trabajo | Un archivo en `unidades/`: un ítem sin método o un objetivo con método | `unidad.md` |
| Con / sin método | Período de creación de la unidad contra el inicio sorteado de su tipo de objetivo; el campo `modo_declarado` no se usa | `creada_en`, `tier`, `protocolo.asignacion` |
| Outcome validado | Validación con `nivel_evidencia` ≥ 2, de fuente real, con `evidencia_en` dentro de los 28 días posteriores a `entregada_en` | `validacion.md` |
| Trabajo descartado | `estado: descartada`: se entregó y después se revirtió o se eliminó | `unidad.md` |
| Igualdad de horas humanas | Razón de bloques activos de 15 minutos por semana entre la parte sin método y la parte con método, dentro de ±20 % | `semana.md` |
| Detección | Decisión `modificada` o `rechazada` cuyos `hallazgos` incluyen el archivo de la semilla | `decision.md` y `siembra/manifiesto.md` |

## 3. Diseño

### 3.1 Por qué el A-B-A-B no conviene

En un diseño de reversión, el efecto se demuestra cuando la conducta vuelve a la línea de base al retirar la intervención y cambia otra vez al reintroducirla. La documentación técnica del WWC dice que, si la variable dependiente difícilmente se revierta después de la primera intervención, el diseño ABAB no es apropiado y sí lo es una línea de base múltiple (Kratochwill y otros, 2010, introducción).

La combinación A es casi toda aprendizaje: escribir un objetivo con métrica, pensar en alternativas, mirar la evidencia antes de construir. En la segunda fase A, el dueño va a seguir pensando así aunque no complete las plantillas. Eso tiene tres consecuencias:

- **Sesgo hacia el nulo.** Si A2 se parece a B1, el contraste A/B subestima el efecto. El script lo detecta con un índice de arrastre, (A2 − A1) / (B1 − A1), y avisa por encima de 0,5 (umbral propuesto, sin fuente).
- **No hay período de lavado posible.** Los ensayos N-of-1 de medicina usan *washout* entre tratamientos (CENT 2015), pero un hábito mental no se lava con tiempo.
- **Costo de negocio.** Volver a trabajar sin método durante 3 semanas con clientes potenciales reales es pedirle al MVP que empeore a propósito.

### 3.2 Alternativas de caso único

| Diseño | Cómo demuestra el efecto | Fuente | Encaje con este piloto |
|---|---|---|---|
| Reversión ABAB | Introducir, retirar y reintroducir | WWC 2010: mínimo cuatro fases | Malo para el método entero por el arrastre. Sirve para componentes que sí se revierten |
| Línea de base múltiple entre conductas (acá, entre tipos de objetivo) | El tratamiento entra escalonado en tres series; cada serie que cambia cuando entra el tratamiento, y no antes, es una demostración | WWC 2010: mínimo seis fases (tres series), al menos 5 puntos por fase para cumplir sin reservas | Bueno: no requiere desaprender. Riesgo propio: que el método se filtre a los tipos que todavía están sin método |
| Tratamientos alternantes | Alternar condiciones rápido, con orden sorteado, y comparar las series | Barlow y Hayes (1979); WWC 2010: cinco repeticiones de la secuencia | Bueno para la revisión de PR, donde la condición cambia de un PR al siguiente. Riesgo: interferencia entre tratamientos (confusión secuencial, arrastre y efectos de alternación, según Barlow y Hayes) |
| Criterio cambiante | El resultado sigue criterios que se escalonan | WWC 2010 | No aplica: el método no tiene una dosis graduable |
| Aleatorización dentro del caso único | Sortear los momentos de inicio para habilitar una prueba de aleatorización | Kratochwill y Levin (2010) recomiendan convertir los diseños tradicionales en diseños aleatorizados siempre que se pueda | Se adopta en la línea de base múltiple |

### 3.3 Recomendación: línea de base múltiple con inicio sorteado, más tratamientos alternantes en la revisión

**Tipos de objetivo (las tres series).** Se eligen para que el trabajo de cada uno sea distinto y el método se pueda aplicar a uno sin aplicarlo a los otros:

- `producto`: funcionalidad que el cliente potencial usa.
- `clientes`: adquisición y validación (página de aterrizaje, contacto, preventa, entrevistas de producto).
- `operacion`: calidad, infraestructura, costo y soporte.

**Calendario (12 semanas, 2 puntos por semana, 24 períodos).** El inicio de cada serie se sortea dentro de una ventana, y también se sortea qué tipo ocupa cada posición:

| Posición | Ventana de inicio (período) | Puntos sin método | Puntos con método |
|---|---|---|---|
| 1 | 6, 7 u 8 (semanas 3 a 4) | 5 a 7 | 17 a 19 |
| 2 | 11, 12 o 13 (semanas 6 a 7) | 10 a 12 | 12 a 14 |
| 3 | 16, 17 o 18 (semanas 8 a 9) | 15 a 17 | 7 a 9 |

Hay 3! × 3³ = 162 asignaciones posibles, así que la prueba de aleatorización puede llegar a p = 1/162 ≈ 0,006. El estadístico es la media, entre los tres tipos, de la diferencia de P1 entre la parte con método y la parte sin método. El script enumera las 162 asignaciones y cuenta cuántas dan un estadístico igual o mayor que el observado.

**Con 8 semanas (16 períodos):** ventanas {6, 7}, {8, 9} y {11, 12}. Cada fase sigue teniendo al menos 5 puntos, pero el escalonamiento entre las posiciones 1 y 2 puede ser de medio período de semana, y hay 48 asignaciones (p mínimo 0,021). Es una opción válida con menos margen; con 12 semanas sobra espacio para el seguimiento de outcomes.

**Por qué media semana y no semana.** Con puntos semanales, para que cada fase tenga 5 puntos en 12 semanas los inicios tienen que caer exactamente en las semanas 6, 7 y 8. Solo se podría sortear el orden (6 asignaciones), con un p mínimo de 0,167: la prueba nunca alcanzaría 0,05. El costo de la media semana es que P1 por período queda ralo (muchos ceros), lo que el fixture muestra.

**Tratamientos alternantes dentro de la fase con método.** Cada PR de un tipo que ya entró en el método recibe una condición de revisión sorteada:

- **H, humano solo:** el revisor agente no corre o su salida queda oculta.
- **A, agente solo:** decide el revisor agente. Solo para cambios reversibles; las semillas se revierten antes del deploy, y la auditoría por muestreo (sección 5) cubre lo aprobado así.
- **HA, humano más agente:** el agente revisa primero y el humano decide con elección forzada (escribe el número de la métrica que espera mover y qué evidencia lo haría rechazar).

La condición sale de `sha256("<semilla_atd>:<PR>") mod 3`. La semilla se compromete por hash en el protocolo y se revela al cierre, así que la condición no se puede elegir después de ver el PR. El WWC pide cinco repeticiones de la secuencia alternante, que se cumplen con cinco o más PR por condición.

### 3.4 Si el dueño mantiene el A-B-A-B

| | Línea de base múltiple más alternantes (recomendada) | A-B-A-B |
|---|---|---|
| Puntos por fase, 12 semanas | ≥ 5 en las seis fases | 6 por fase (fases de 3 semanas) |
| Puntos por fase, 8 semanas | ≥ 5 | 4 por fase: cumple "con reservas" según el WWC |
| Supuesto que exige | Que los tres tipos sean independientes | Que el efecto se revierta al retirar el método |
| Qué pasa si el supuesto falla | La línea de base del tipo sin método sube antes de su inicio; el script lo marca como filtración | A2 no vuelve; el efecto se subestima; el script reporta el índice de arrastre |
| Prueba estadística | Aleatorización de inicios (162 o 48 asignaciones) | No implementada: requeriría sortear los puntos de cambio de fase |
| Costo de negocio | Ninguno extra | Tres semanas de trabajar peor a propósito con clientes reales |
| Complejidad diaria | Hay que llevar el tipo de cada unidad y respetar qué tipos están con método | Una sola regla por semana |

**Recomendación:** línea de base múltiple. Si el dueño elige A-B-A-B, el protocolo cambia `diseno: abab` y `fases_abab: [1-6-A, 7-12-B, 13-18-A, 19-24-B]`, y el resultado se lee como "efecto de introducir el método", no como "efecto que desaparece al retirarlo". Con un índice de arrastre alto, el veredicto queda en ambiguo aunque B supere a A.

## 4. Fase 0: validación del problema

### 4.1 Qué valida y cuándo

La Fase 0 valida el problema del público del marco (tiny teams, fundadores solos y bootstrappers que construyen con agentes de IA), no el del MVP. Corre antes de la semana 1 y no cuenta dentro de las 8 a 12 semanas. Duración propuesta: hasta 3 semanas (decisión pendiente).

**Cuántas entrevistas.** Entre 10 y 15. Guest, Bunce y Johnson (2006), con 60 entrevistas en profundidad, encontraron que la saturación ocurrió dentro de las primeras doce y que los elementos básicos de los metatemas aparecieron desde la sexta. Su muestra fueron mujeres de dos países de África occidental; acá hay tres perfiles distintos y el dominio es otro, por eso el máximo de 15.

### 4.2 Principios (The Mom Test, parafraseados)

Fitzpatrick (2013), según el resumen de Michael Lynch: hablar de la vida de la persona y no de la idea; preguntar por hechos concretos del pasado y no por opiniones ni por el futuro; escuchar más de lo que se habla; y buscar compromisos (tiempo, reputación o dinero) en lugar de elogios. La página del libro no presenta evaluación empírica de estas reglas ([[Investigación - Tiny teams y bootstrapping]]): se usan como disciplina de entrevista, no como método validado.

Reglas operativas:

1. **No se presenta ODLC ni la idea.** Si la persona pregunta por qué se la entrevista, la respuesta es "estoy estudiando cómo trabajan quienes construyen solos con agentes".
2. **No se nombra el tema antes de que aparezca.** Si el entrevistador sugiere un dolor ("¿no te pasa que…?"), ese tema se registra como `inducido` y no cuenta.
3. **Solo hechos pasados.** "La última vez que…", "¿qué hiciste después?", "¿cuánto tiempo te llevó?". "Usualmente", "me gustaría" o "usaría" no cuentan como dato.
4. **El compromiso cuenta solo si ya ocurrió:** horas gastadas en un rodeo, dinero pagado por una herramienta, un script casero, haberle pedido ayuda a un tercero.

### 4.3 Guion de preguntas

Las preguntas abren sin sugerir el dolor; las repreguntas solo profundizan lo que la persona ya mencionó.

1. Contame qué estás construyendo ahora y cómo es una semana típica de trabajo. *(contexto)*
2. ¿Qué hiciste ayer o el último día que trabajaste en el producto, de principio a fin?
3. La última vez que trabajaste con un agente en algo grande, ¿qué pasó después de que terminó? ¿Qué hiciste con lo que generó? *(abre el tema de revisión sin nombrarlo)*
   - Si menciona que no le dio el tiempo para revisar: ¿cuándo fue la última vez? ¿qué hiciste? ¿qué pasó después?
4. Pensá en la última semana: ¿en qué se te fue el tiempo? Si tuvieras que repartirlo entre construir y todo lo demás, ¿cómo quedó? *(abre decidir y validar frente a construir)*
   - Si menciona decisiones trabadas: ¿cuál fue la última? ¿cuánto tardaste? ¿cómo la destrabaste?
5. ¿Cómo sabés si algo que lanzaste funcionó? Contame la última vez que lo averiguaste. *(abre validar con pocos clientes)*
   - ¿Con cuántas personas lo hablaste? ¿Qué hicieron ellas, no qué dijeron?
6. ¿Trabajaste con alguien más en este producto o en uno anterior? ¿Qué cambió cuando se sumó? *(abre sumar gente)*
7. ¿Probaste algo para resolver lo que me contaste? ¿Qué, cuándo, cuánto te costó, lo seguís usando? *(señales de compromiso)*
8. ¿Hay alguien más con quien debería hablar? *(compromiso de reputación y reclutamiento)*

### 4.4 Canales de reclutamiento

Sin nombrar organizaciones del dueño ni pagar por las entrevistas (decisión pendiente si se ofrece un incentivo):

- Comunidades públicas de fundadores independientes: foros, subforos y servidores de chat abiertos.
- Comunidades de usuarios de herramientas de agentes de programación.
- Autores de publicaciones públicas recientes sobre construir productos con agentes.
- Fichas de productos lanzados hace poco en directorios públicos de lanzamientos, contactando a quien lo hizo.
- Encuentros abiertos de desarrolladores.
- Referidos de entrevistados, con un máximo de 2 por referente para no concentrar la muestra en un círculo.

### 4.5 Registro y codificación ciega

Cada entrevista genera un archivo con la plantilla `entrevista.md`: fecha, perfil, canal, duración, `dolor_mencionado` por tema (`espontaneo`, `no_mencionado` o `inducido`), `senales_compromiso` (hechos pasados) y citas cortas anonimizadas. El cuerpo tiene solo hechos, en orden.

**Mitigación del sesgo de confirmación.** El entrevistador es el diseñador del marco. Un segundo codificador, que puede ser una persona o un agente sin acceso a la hipótesis ni al protocolo, lee **solo el cuerpo** de cada entrevista y codifica con la plantilla `codificacion.md`. Si es un agente, no puede ser el modelo que asistió al entrevistador, y se registra en `registro-ia`.

**Libro de códigos** (lo único que recibe el codificador ciego):

| Código | Se marca "si" cuando el texto relata un hecho pasado de… |
|---|---|
| `revision_desbordada` | haber recibido de una herramienta más resultado del que pudo revisar, o haber aceptado algo sin revisarlo por falta de tiempo |
| `decidir_vs_construir` | tiempo concreto perdido en decidir, discutir o validar, comparable o mayor que el de construir |
| `validar_pocos_clientes` | no haber podido saber si algo funcionó por tener pocos usuarios o pocas respuestas |
| `sumar_gente` | un problema concreto que apareció al sumar a otra persona al trabajo |
| `compromiso` | haber gastado tiempo, dinero o reputación en ese problema (herramienta pagada, script propio, ayuda pedida) |

**Acuerdo.** Kappa de Cohen entre el entrevistador (`espontaneo` = 1) y el codificador ciego (`si` = 1), por tema y para el compromiso. El WWC toma como mínimo aceptable un kappa de 0,60 (Hartmann y otros, 2004, citado en Kratochwill y otros, 2010) y pide medir acuerdo en al menos 20 % de las sesiones; acá se codifica el 100 %.

### 4.6 Regla de decisión de la Fase 0 (pre-registrada)

La regla usa la codificación ciega, no la del entrevistador. Los umbrales numéricos no tienen fuente: son **propuestas que decide el dueño**.

| Resultado | Condición (propuesta) | Qué se hace |
|---|---|---|
| Confirmado | ≥ 10 entrevistas con perfil válido; kappa de dolor ≥ 0,60; al menos 50 % con dolor en un tema central (`revision_desbordada` o `decidir_vs_construir`) y al menos 30 % con señal de compromiso | Arranca la línea de base |
| Descartado | Dolor central en menos de 20 % | **K0: el piloto no arranca.** El problema que ODLC dice atacar no aparece en el público elegido |
| Ambiguo | Cualquier otro caso, o kappa < 0,60 | Una sola extensión de 5 entrevistas (y recodificación si el kappa fue bajo). Si sigue ambiguo, cuenta como descartado |

## 5. La combinación A en el día a día

### 5.1 Con método (fase B de cada tipo de objetivo)

| Fase ODLC | Práctica concreta | Pieza de la combinación A | Qué deja en el repo |
|---|---|---|---|
| [[Fase 1 - Objective]] | Cada unidad nace como objetivo: resultado esperado para el cliente potencial, métrica con baseline, target y ventana, y criterio de abandono con estado y fecha. El agente propone la redacción; el humano escribe el target. | Meta separada del pronóstico (Beyond Budgeting); kill criteria (Duke) | `unidades/U-*.md` completo |
| [[Fase 2 - Constraints]] | Presupuesto de tokens por unidad y superficies que no se tocan (pagos, datos de clientes, borrado) | Aprobación humana solo en lo irreversible (IMDA) | Campos en la unidad; `registro-ia` |
| [[Fase 3 - Strategy]] | El agente presenta al menos dos alternativas con costos; el humano elige una entre opciones, no aprueba una sola. Se cita al menos un aprendizaje previo si existe. | Fricción concentrada en decisiones significativas | `decisiones/D-*.md` con `opciones_presentadas` ≥ 2 |
| [[Fase 4 - Execution]] | El escritor y el revisor son agentes de **familias de modelo distintas**. Los PR reciben la condición de revisión sorteada (H, A o HA). | Contra la autopreferencia del revisor (Panickssery y otros, 2024) | PR, `decisiones/` con `condicion_revision` |
| [[Fase 5 - Validation]] | A los 28 días de la entrega se registra la evidencia del outcome con la escalera de la sección 7, citando un artefacto que un tercero pueda abrir. El veredicto copia el target sin reinterpretarlo. | Validar contra el outcome; responsabilidad sobre el proceso de verificación (Mosier y Skitka) | `validaciones/V-*.md` |
| [[Fase 6 - Learning]] | Al cerrarse una unidad (entregada, descartada o abandonada), un hook crea el archivo de aprendizaje vacío con la unidad enlazada. El debrief no depende de que alguien lo convoque: depende de que el vacío quede visible en las métricas. | Debrief (Tannenbaum y Cerasoli); "hacer visible" (principio 6) | `aprendizajes/A-*.md` |

Transversales, en las dos fases:

- **Auditoría compensatoria por muestreo.** Una vez por semana, un sorteo elige una unidad ya aprobada (en especial, lo aprobado por el agente solo) y el humano revisa su respaldo contra la evidencia. Es el control que COSO (2006) propone cuando no hay gente para separar funciones (citado en [[Investigación - Tiny teams y bootstrapping]]); queda registrado como decisión de clase `auditoria_muestreo`.
- **Una persona, todos los roles.** Ninguna fuente relevada resuelve la separación de funciones con una sola persona. Las compensaciones del piloto son tres: el muestreo de COSO, un revisor agente de otra familia sabiendo que no es independiente (los modelos de proveedores distintos también se equivocan parecido, Kim y otros, 2025, en [[Propuestas existentes - Revisión en manos de agentes]]), y para lo irreversible, un validador externo (asesor, par o el propio cliente que paga) o la excepción escrita.
- **Medir la etapa o la persona.** Con una persona, el conflicto 2.2 de la Síntesis desaparece: la etapa de revisión y el revisor son lo mismo. Las métricas de pasividad se devuelven al propio dueño como calibración y no se usan para nada más.
- **Sin recompensa por la métrica.** Nadie cobra ni se evalúa por P1 (Holmström y Milgrom, en la Síntesis).

### 5.2 Sin método (fase A de cada tipo)

Se trabaja como se trabajaría sin ODLC, con los mismos agentes y suscripciones: una lista de ítems, el agente implementa, el humano revisa el PR como le parezca y lo mergea. Lo único que se agrega es el registro mínimo para poder medir:

- `unidades/U-*.md` con tipo, timestamps y estado. **Sin** resultado esperado, métrica ni criterio de abandono; si el dueño los escribe igual, el script lo marca como filtración del método.
- `decisiones/` para cada revisión de PR (los timestamps salen de la herramienta, no del recuerdo).
- `validaciones/` a los 28 días de cada entrega, con la misma escalera de evidencia. Sin esto, el outcome de la fase A no se podría comparar.
- Sin aprendizajes, sin elección forzada, sin alternativas, sin condiciones de revisión sorteadas.

Registrar ya es una intervención leve: completar la validación de los ítems puede hacer que el dueño mire el outcome. Es una amenaza declarada (sección 10), no un descuido.

## 6. Medidas

Regla general: **ninguna medida sale de autoinforme.** En el ensayo de METR (2025), los desarrolladores tardaron 19 % más con IA y aun así creían haber ganado 20 % (citado en [[Propuestas existentes - Objeciones 3 y 4]]). Todo dato es un campo de un archivo con timestamp de herramienta, contrastable con el commit que lo agregó (comando en la sección 9).

### 6.1 Primarias

| Medida | Definición operativa | Evento de origen | Unidad | Ventana |
|---|---|---|---|---|
| **P1** Outcome validado | Unidades creadas en el período cuya validación tiene `nivel_evidencia` ≥ 2, `fuente: real` y `evidencia_en` entre `entregada_en` y 28 días después | `unidades/*.md` (`creada_en`, `entregada_en`), `validaciones/*.md` | Unidades por período de media semana y tipo de objetivo | 24 períodos más 28 días de seguimiento sin unidades nuevas |
| **P2** Descarte después de entregar | Unidades con `estado: descartada` dividido por unidades de la fase | `unidades/*.md` (`estado`, `descartada_en`, commit de reversión) | Proporción por fase | Toda la fase |

### 6.2 Contraste de la revisión (H2)

| Medida | Definición operativa | Evento de origen | Unidad | Ventana |
|---|---|---|---|---|
| **R** Detección por condición | Semillas detectadas sobre semillas revisadas, por condición H, A y HA, con intervalo de Wilson al 95 % | `siembra/manifiesto.md` cruzado con `decisiones/*.md` (`pr`, `resultado`, `hallazgos`) | Proporción | Fase con método |
| Regla del contraste | Sostiene si el límite inferior de HA supera la mayor tasa entre H y A; descarta si el límite superior de HA queda por debajo; si no, ambiguo. Exige ≥ 5 semillas por condición (propuesta) | Calculado | Categórico | Cierre |

### 6.3 Secundarias

| Medida | Definición operativa | Evento de origen | Unidad | Ventana |
|---|---|---|---|---|
| S1 Abandono temprano (H3) | Unidades con `estado: abandonada` y mediana de días entre `creada_en` y `descartada_en` | `unidades/*.md` | Conteo y días | Fase |
| S2 Tasa de outcome | P1 dividido por unidades entregadas | Como P1 | Proporción | Fase |
| S3 Compromiso de pago | Unidades con validación de nivel 3 | `validaciones/*.md` | Conteo | Fase |
| S4 TTO separado | Mediana de días de trabajo (creada a entregada) y de espera de evidencia (entregada a evidencia) | `unidades/`, `validaciones/` | Días | Fase |
| S5 Adherencia | Unidades de la fase B con resultado esperado y métrica completos | `unidades/*.md` | Proporción por semana | Fase B |
| S6 Horas humanas activas | Bloques distintos de 15 minutos con al menos un evento (commit del MVP o registro de sesión de agente) | Comando de bloques (sección 9) volcado a `semanas/*.md` | Bloques por semana | Semana |
| S7 Costo | Facturación de suscripciones y APIs prorrateada | `semanas/*.md` | USD por semana | Semana |
| S8 Velocidad de aprendizaje (LV) | Aprendizajes válidos (40 o más caracteres, no repetidos) sobre unidades cerradas con método | `aprendizajes/*.md` | Proporción | Fase B |
| S9 Reutilización (KRR) | Aprendizajes con `citado_por` no vacío | `aprendizajes/*.md` | Conteo | Piloto |
| S10 Auditoría compensatoria | Decisiones `auditoria_muestreo` por semana | `decisiones/*.md` | Conteo por semana | Semana |
| S11 Registro de IA | Configuraciones vigentes y cambios, con familia del escritor y del revisor | `registro-ia/*.md` | Lista | Piloto |

### 6.4 Pasividad del humano y siembra de defectos

Son los principios 3 y 4 de la Objeción 5 en [[Objeciones al marco]], instrumentados. Se calculan por fase y por condición de revisión, solo sobre decisiones tomadas por el humano:

| Métrica | Definición | Origen |
|---|---|---|
| Aprobación sin cambios | `resultado: aprobada` sobre el total | `decisiones/*.md` |
| Latencia | `decidida_en − propuesta_en`; mediana y proporción por debajo de 30 s (umbral propuesto, sin fuente) | timestamps de la herramienta |
| Elección forzada vacía | Decisiones HA con `metrica_escrita` y `que_cambiaria_veredicto` vacíos | `decisiones/*.md` |
| Aprendizajes vacíos o repetidos | Menos de 40 caracteres o texto repetido | `aprendizajes/*.md` |
| Detección de semillas | Sección 6.2 | manifiesto y decisiones |

La aprobación sin cambios es el indicador y la detección de semillas es el contraindicador que impide leer una aprobación del 100 % como éxito: es el par de Grove que señala la Síntesis.

**Riesgo de Goodhart.** Toda métrica de pasividad se puede inflar sin cambiar la conducta: demorar la aprobación para no caer debajo de 30 s, escribir cualquier número en la elección forzada, escribir aprendizajes largos y vacíos. El dueño, además, diseñó las métricas y sabe que existen. Mitigaciones: las métricas de pasividad **no entran en la regla de decisión de la tesis**, solo en alertas y en K3; la elección forzada se audita en el muestreo semanal; y la única métrica que no se puede inflar sin detectar el defecto es la de semillas.

**Siembra escasa (Bainbridge).** Bainbridge (1983) advierte que subir artificialmente la tasa de fallas hace que el operador deje de confiar en el sistema; la tasa sembrada tiene que ser baja (citado en [[Propuestas existentes - Revisión en manos de agentes]]). Tope propuesto: 15 % de los PR revisados, sin fuente para la cifra. Consecuencia que se acepta por escrito: con unos 40 PR en la fase con método, quedan menos de 6 semillas para repartir entre tres condiciones, así que **H2 probablemente termine sin datos suficientes**. Es preferible reportarlo así que sembrar más y arruinar la confianza que se quiere medir.

**Cómo se siembra.** Un script o agente distinto del revisor, con su propia semilla aleatoria guardada fuera del repo, aplica con probabilidad fija una mutación chica a un PR del escritor antes de abrirlo, con el mismo autor de commit que el escritor, en archivos que no sean irreversibles (nunca pagos, migraciones ni borrado de datos). Registra el PR y el archivo en el manifiesto. Al inicio se commitea solo el hash del manifiesto (`siembra.sha256`). Un chequeo de CI revierte toda semilla antes del deploy, la detecte o no la revisión. La siembra de seguridad aeroportuaria (Threat Image Projection) y el laboratorio de Bahner y otros (2008) son la evidencia disponible, de otro dominio ([[Objeciones al marco]]).

**Antecedente en software y alcance.** Sembrar defectos conocidos para estimar cuántos se escapan es una técnica vieja de software: la siembra de errores de Mills y el *bebugging* de Gilb, en los setenta. Los experimentos de inspección miden a los revisores sobre documentos con defectos conocidos (Porter, Votta y Basili, *IEEE Transactions on Software Engineering* 21(6), 1995). Lo que no se encontró es una aplicación publicada para medir revisores automáticos en producción; Meta usa mutantes para endurecer suites de tests, no para medir al revisor ([[Propuestas existentes - Revisión en manos de agentes]]). La semilla solo existe en este piloto, con la condición HA y su criterio K3; el [[Núcleo ODLC para tiny teams]] no la incluye porque el repo no trae un sembrador.

## 7. Outcomes con pocos clientes (el hueco de la Objeción 2)

### 7.1 Qué cuenta como evidencia

Escalera, del más débil al más fuerte. Solo los niveles 2 y 3 cuentan para P1:

| Nivel | Evidencia | Ejemplos con artefacto auditable |
|---|---|---|
| 0 | Nada, opinión o usuario simulado | "Le gustó"; respuesta de un usuario simulado con LLM |
| 1 | Uso | Consulta de analítica que muestra que un cliente potencial usó la función |
| 2 | Compromiso de tiempo o reputación | Demo agendada y asistida; presentación a un tercero; uso repetido en tres días distintos |
| 3 | Compromiso económico | Preventa, pago, carta de intención firmada |

La escalera sigue el orden de compromiso de The Mom Test (tiempo, reputación, dinero) y la evidencia relevada en [[Investigación - Tiny teams y bootstrapping]]: con pocos clientes, la señal más fuerte es la que le cuesta algo al cliente. En proyectos no financiados de Kickstarter, 50 % más compromisos de pago se asocian con 9 % más probabilidad de comercializar (Xu, observacional; citado en esa nota).

**Usuarios simulados.** Se permiten para filtrar ideas antes de exponerlas a clientes reales. Se registran con `fuente: simulada` y el script los cuenta como nivel 0 aunque el archivo diga otra cosa. Fallan justo en categorías nuevas (Brand y otros), aplanan grupos demográficos (Wang y otros), y cuando aciertan (Park y otros, 2024) es porque se construyeron con entrevistas de dos horas a las personas reales (citados en la misma nota).

**Con números chicos.** P1 se cuenta en unidades, no en porcentajes de una población. Ninguna inferencia del piloto supone muestreo de clientes; la inferencia es sobre el método dentro del caso.

### 7.2 Qué se mide mientras se espera

- **Tiempo de espera separado del tiempo de trabajo (S4).** Contesta el pedido de [[Métricas operativas]]: el TTO se descompone en trabajo (creada a entregada) y espera de evidencia (entregada a evidencia).
- **Nivel 1 como señal temprana**, que no cuenta para P1 pero se reporta.
- **Abandono temprano (S1)**, que no espera al mercado: un objetivo cuyo criterio de abandono se cumple se cierra sin construirse.
- **Proceso:** adherencia, decisiones con alternativas, aprendizajes no vacíos. No prueban outcome, pero muestran si el método se aplicó.
- **Seguimiento de 28 días** después de la última semana, sin unidades nuevas, para que las unidades de las últimas semanas, casi todas de la fase con método, no queden censuradas. El script usa `fecha_corte` del protocolo y marca las ventanas abiertas.

## 8. Criterios de abandono y regla de decisión

Se fijan antes de empezar y los evalúa el script. Exit 1 si alguno está activo. Los umbrales sin fuente son **propuestas que decide el dueño**.

| Criterio | Estado medible | Cuándo se evalúa | Qué se hace |
|---|---|---|---|
| **K0** Problema no confirmado | Resultado de la Fase 0: descartado | Al cerrar la Fase 0 | El piloto no arranca |
| **K1** Método inaplicable | En dos semanas seguidas con 3 o más unidades con método, menos de 70 % están completas | Semanal | Se detiene el piloto. Es un hallazgo contra el método para este público: un tiny team no lo sostiene |
| **K2** Costo del método | En un tipo con método, la entrega de las últimas 3 semanas cae más de 50 % contra su línea de base, sin mejora de P1 | Semanal desde la tercera semana con método | Se detiene ese tipo y se reporta |
| **K3** Compuerta muerta | En HA, 4 o más semillas revisadas y ninguna detectada | Al cierre (el manifiesto se revela entonces) | La aprobación humana de HA no cuenta como validación; H2 se descarta |
| **K4** Piloto no informativo | Ninguna validación de nivel 2 o más en toda la fase A ni en la B al llegar a la semana 8 | Semana 8 | El producto no da outcome observable. El piloto no puede decidir la tesis: se declara no informativo; no se pivotea el producto a mitad sin desvío |
| **K5** Tesis descartada | La regla de decisión da "descarta" con el protocolo cerrado | Al cierre | Se descarta la tesis, no la medición |

K4 está en el protocolo pero no en el script (exige evaluar a la semana 8 con el corte parcial): queda como decisión pendiente implementarlo o evaluarlo a mano con el comando de la sección 9.

**Regla de decisión de H1** (línea de base múltiple, al cierre):

- **Sostiene** si se cumplen todas: p de la prueba de aleatorización ≤ 0,05; P1 con método mayor que sin método en al menos 2 de los 3 tipos; tasa de P2 con método menor o igual que sin método; razón de horas activas dentro de ±20 %; y K1 inactivo.
- **Descarta** si en al menos 2 de los 3 tipos P1 con método no supera a P1 sin método, y además la diferencia media es ≤ 0 o P2 empeora.
- **Ambiguo** en cualquier otro caso.

**Qué se hace con un ambiguo.** No se declara apoyo. No se agregan semanas para buscar significancia: eso se registraría como desvío con `visto_datos: true` y el resultado quedaría marcado como exploratorio. El paso pre-registrado es replicar el diseño con otra persona o con otro MVP (línea de base múltiple entre casos), que es además el camino hacia los 3 equipos que pide el WWC.

**Alfa y ventanas.** El 0,05 es convención y no tiene una fuente específica para este piloto. Las ventanas de inicio salen de exigir al menos 5 puntos por fase (WWC).

## 9. Pre-registro verificable

### 9.1 Pasos

1. **Resolver las decisiones pendientes** (sección 13) y copiarlas al `protocolo.md` del repo del MVP, con la plantilla de `scripts/fixtures/piloto/plantillas/protocolo.md`. El protocolo incluye el hash de `semilla_atd`, no su valor.
2. **Commitear el protocolo sin asignación** y tomar el hash de ese commit:

   ```bash
   git log -1 --format=%H -- protocolo.md
   ```

3. **Sortear la asignación de inicios desde ese hash**, de modo que nadie la elija y cualquiera la recalcule:

   ```bash
   python3 - <<'EOF'
   import hashlib, itertools
   semilla = "<hash del commit del paso 2>"
   tiers = ["producto", "clientes", "operacion"]
   ventanas = [[6, 7, 8], [11, 12, 13], [16, 17, 18]]
   opciones = [dict(zip(o, s)) for o in itertools.permutations(tiers) for s in itertools.product(*ventanas)]
   print(opciones[int(hashlib.sha256(semilla.encode()).hexdigest(), 16) % len(opciones)])
   EOF
   ```

   El orden de enumeración es el mismo que usa el script, así que la asignación sellada tiene que estar entre las 162 que el script considera.
4. **Escribir la asignación en el protocolo, calcular el sello y commitear los dos juntos.** Ese commit es el pre-registro:

   ```bash
   shasum -a 256 protocolo.md | awk '{print $1"  protocolo.md"}' > protocolo.sha256
   ```

   Se commitean también `siembra.sha256` (hash del manifiesto de siembra vacío, que el script de siembra irá completando fuera del repo) y una copia de esta nota tal como esté en ese momento.
5. **Cualquier cambio posterior** a `protocolo.md` exige un archivo en `desvios/` con `hash_anterior`, `hash_nuevo`, `motivo` y `visto_datos`. El script recorre la cadena desde el sello y termina con exit 2 si no llega al hash actual.
6. **Al cierre** se revelan la `semilla_atd` (en el protocolo, como desvío declarado) y el manifiesto. El script verifica que el manifiesto coincida con el hash comprometido y que cada condición de revisión coincida con el sorteo.

Prueba de que el sello funciona, sobre una copia descartable del fixture (sed con la sintaxis de macOS):

```bash
d=$(mktemp -d) && cp -R scripts/fixtures/piloto/. "$d" && sed -i '' 's/alfa: 0.05/alfa: 0.10/' "$d/protocolo.md"
python3 scripts/piloto_metricas.py "$d"; echo exit=$?; rm -rf "$d"
# ERROR: DatosInvalidos: sello roto: protocolo.md tiene sha256 0996768a… y la cadena sello+desvíos termina en 24715de2…
# exit=2
```

### 9.2 Comandos auxiliares

Bloques activos de 15 minutos en una semana, solo con commits del MVP (subestima si se trabaja sin commitear; sumar los timestamps de los registros de sesión de los agentes es una decisión pendiente):

```bash
git -C <repo-mvp> log --since=<lunes> --until=<lunes+7d> --format=%at | awk '{print int($1/900)}' | sort -u | wc -l
```

Contrastar el `creada_en` declarado con el primer commit que agregó el archivo:

```bash
git -C <repo-mvp> log --diff-filter=A --format=%aI -- unidades/U-012.md | tail -1
```

## 10. Amenazas a la validez

| Amenaza | Cómo opera acá | Mitigación | Qué queda |
|---|---|---|---|
| n = 1 | Una persona, un producto | Tres demostraciones del efecto (WWC); conclusión acotada al caso | La generalización exige la regla 5-3-20 (sección 12) |
| Arrastre del método | Lo aprendido en un tipo se filtra a los tipos sin método | Tipos de trabajo distintos; el script alerta si sube la línea de base de un tipo antes de su inicio y si una unidad sin método declara métrica | Una filtración sin rastro en los archivos no se detecta |
| Interferencia entre tratamientos en la revisión | Ver la revisión del agente en HA cambia cómo el humano revisa en H | Sorteo por PR; condición fijada por hash | Barlow y Hayes la describen; no se elimina |
| Sesgo del diseñador que es el sujeto | Conoce la hipótesis, las métricas y el calendario | Pre-registro con sello; inicio sorteado; semillas que no conoce; codificación ciega en la Fase 0; evidencia de outcome con artefacto auditable; el análisis lo hace un script fijado antes; un juez adversarial revisa el informe final | Saber cuándo entra el método es inevitable: no hay ciego posible |
| Reactividad del registro | Registrar unidades y validaciones en la fase A ya puede cambiar la conducta | Registro mínimo en A; sin métrica ni aprendizaje | Sesgo hacia el nulo |
| Maduración | El MVP crece, el dueño mejora con las herramientas, aparecen más clientes | Los inicios escalonados: si todos los tipos mejoran a la vez, sin importar su inicio, es maduración y no método | Una maduración que coincida con el orden sorteado no se separa |
| Historia (eventos externos) | Un lanzamiento, una nota en un medio, una caída del proveedor | Registro de eventos en `desvios/` con fecha | Igual que maduración |
| Cambio de modelos de IA | El proveedor cambia o retira el modelo durante el piloto | `registro-ia` con modelo, familia, versión, configuración y hash del prompt; preferir versiones fijadas; el script alerta si un cambio cae a una semana o menos de un inicio | Si el cambio coincide con un inicio, ese tipo no cuenta como demostración limpia |
| Revisor no independiente | El agente revisor favorece lo que él mismo produjo (Panickssery y otros, 2024) y comparte errores con otros modelos (Kim y otros, 2025) | Revisor de otra familia; el script alerta si coinciden | La correlación entre familias no se elimina |
| Volumen bajo | Pocas unidades por período: P1 queda lleno de ceros | Puntos de media semana; prueba de aleatorización, que no supone normalidad | El fixture muestra que un efecto grande en tasa puede no alcanzar p ≤ 0,05 |
| Goodhart sobre las métricas del piloto | Inflar aprendizajes, latencias o niveles de evidencia | Las de pasividad no deciden; la evidencia exige artefacto; auditoría semanal | Ver sección 6.4 |
| Piloto contra mandato | Un piloto exitoso no predice la adopción obligatoria (checklist de la OMS frente a Ontario, en [[Objeciones al marco]]) | Se declara | No se resuelve con un piloto |

## 11. Plantillas y script

### 11.1 Plantillas

Están en `scripts/fixtures/piloto/plantillas/` y no bajo `docs/`, porque su frontmatter es el de los artefactos del MVP y no el contrato del vault (tags, status, created).

| Plantilla | Alimenta | Fase ODLC |
|---|---|---|
| `unidad.md` (objetivo o ítem) | P1, P2, S1, S2, S4, S5, filtración | 1, 2 |
| `decision.md` | Pasividad, R, S10 | 3, 4, 5 |
| `validacion.md` | P1, S2, S3, S4 | 5 |
| `aprendizaje.md` | S8, S9, pasividad | 6 |
| `entrevista.md`, `codificacion.md` | Fase 0 y kappa | — |
| `registro-ia.md` | S11, amenazas | — |
| `semana.md` | S6, S7, paridad de horas | — |
| `protocolo.md`, `desvio.md`, `manifiesto-siembra.md` | Sello, asignación, siembra | — |

### 11.2 Script

`scripts/piloto_metricas.py <directorio>`: solo stdlib (incluye un lector de YAML acotado a las plantillas), read-only, sin reloj ni red; la fecha de corte sale del protocolo. Exit 0 sin criterios de abandono activos, 1 con al menos uno, 2 por error o sello roto. Calcula la Fase 0 (kappa, regla), P1, P2, NAP por tipo (Parker y Vannest, 2009: proporción de pares en que la observación con método mejora a la de línea de base, con empates a 1/2, según la documentación de SingleCaseES), la prueba de aleatorización, adherencia, pasividad, siembra con intervalos de Wilson, el contraste de Vaccaro, el TTO separado, la paridad de horas, el registro de IA, la auditoría por muestreo y la regla de decisión. Soporta `diseno: abab` con el índice de arrastre.

El fixture `scripts/fixtures/piloto/` es **ficticio**: 12 entrevistas, 49 unidades, 12 semanas. `scripts/fixtures/piloto/caso-abandono/` es una Fase 0 que descarta el problema.

```bash
python3 scripts/piloto_metricas.py scripts/fixtures/piloto; echo exit=$?
```

```text
Sello: OK (24715de2cd28…, 0 desvío(s) declarado(s))
Fase 0: 12 entrevistas, 12 con perfil válido (0 fuera de perfil), 0 sin codificación ciega, 0 con algún tema inducido por el entrevistador
  acuerdo entrevistador vs. codificador ciego — dolor: kappa 0.91 (acuerdo 0.96); compromiso: kappa 1.00 (acuerdo 1.00)
  según el codificador ciego: dolor central en 7/12 (0.58), señal de compromiso en 5/12 (0.42)
  resultado Fase 0: CONFIRMADO

Piloto: diseño linea_base_multiple, 12 semanas (24 períodos de medición) desde 2026-11-02, corte 2027-02-21
  inicio del método por tipo de objetivo: clientes=período 7, producto=período 12, operacion=período 17

Medidas primarias
  fase A: 25 unidades, 23 entregadas; P1 outcome validado (nivel ≥ 2 en ≤ 28 d): 4 (tasa 0.17; 0 con ventana abierta; 2 con compromiso de pago); P2 descartadas después de entregar: 1 (tasa 0.04)
  fase B: 24 unidades, 16 entregadas; P1 outcome validado (nivel ≥ 2 en ≤ 28 d): 13 (tasa 0.81; 1 con ventana abierta; 5 con compromiso de pago); P2 descartadas después de entregar: 0 (tasa 0.00)
  secundaria (Camuffo): abandono antes de entregar
    fase A: 2 abandonadas de 25; mediana de días hasta abandonar 5.0
    fase B: 8 abandonadas de 24; mediana de días hasta abandonar 1.5
  producto: P1 por período [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0] | NAP P1 0.60 | P2 por período [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] | NAP P2 0.50
  clientes: P1 por período [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0] | NAP P1 0.64 | P2 por período [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] | NAP P2 0.50
  operacion: P1 por período [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0] | NAP P1 0.62 | P2 por período [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] | NAP P2 0.53
  prueba de aleatorización (P1, diferencia media B−A): observado 0.244, p = 20/162 = 0.123

Adherencia al método (unidades B con objetivo y métrica completos): 0.96

Pasividad del humano (decisiones tomadas por humano)
  A/-: n=23, aprobación sin cambios 0.83, mediana de latencia 90 s, < 30 s: 0.30
  B/H: n=7, aprobación sin cambios 0.71, mediana de latencia 240 s, < 30 s: 0.00
  B/HA: n=3, aprobación sin cambios 0.33, mediana de latencia 900 s, < 30 s: 0.00, elección forzada vacía 0.00
  auditoria: n=12, aprobación sin cambios 0.58, mediana de latencia 930 s, < 30 s: 0.00
  aprendizajes: 12 (5 vacíos, 4 repetidos); LV = 3/24 unidades B cerradas = 0.12; citados por unidades posteriores: 5

Siembra de defectos y contraste humano+agente contra el mejor componente solo
  manifiesto revelado: coincide con el hash comprometido
  semillas: 3 sobre 39 PR revisados (tasa 0.08; tope pre-registrado 0.15)
  H: detectadas 0/1 (IC95 Wilson 0.00–0.79)
  A: detectadas 0/0 (IC95 Wilson s/d–s/d)
  HA: detectadas 2/2 (IC95 Wilson 0.34–1.00)
  condiciones de revisión: coinciden con el sorteo sellado
  contraste HA contra max(H, A): SIN_DATOS (requiere ≥ 5 semillas por condición)

Tiempo hasta el outcome, separado (unidades validadas)
  fase A: mediana trabajo 3.7 d, mediana espera de evidencia 10.5 d
  fase B: mediana trabajo 1.3 d, mediana espera de evidencia 11.0 d

Horas humanas: bloques activos/semana antes del primer inicio 65.7, después del último 66.0 (razón 1.01; dentro de la tolerancia 0.2)

Registro de IA: 3 configuración(es)
  período 1: escritor cli-de-agentes-ficticia modelo-ficticio-w (familia proveedor-x) 2026-09 prompt 664c363a61eb
  período 1: revisor cli-de-agentes-ficticia modelo-ficticio-r (familia proveedor-y) 2026-09 prompt ae3f4cd49bf9
  período 21: escritor cli-de-agentes-ficticia modelo-ficticio-w (familia proveedor-x) 2026-12 prompt dc37ae224ccd
Auditoría por muestreo: 12 en 12 semanas; semanas por debajo del mínimo (1): ninguna

Regla de decisión: p ≤ 0.05: False; tiers con P1 B > A: 3/3; P2 B ≤ A: True; paridad de horas: True; adherencia sin K1: True
VEREDICTO FINAL sobre la tesis: AMBIGUO; componente de revisión (Vaccaro): SIN_DATOS

Alertas (1):
  - línea de base de 'operacion' sube antes de su inicio (0.00 → 0.20): posible filtración entre tipos
Criterios de abandono activos (0):
exit=0
```

```bash
python3 scripts/piloto_metricas.py scripts/fixtures/piloto/caso-abandono; echo exit=$?
```

```text
...
  resultado Fase 0: DESCARTADO
Piloto: no corresponde (K0 activo)
...
Criterios de abandono activos (1):
  - K0 Fase 0: el problema no se confirma; el piloto no arranca
exit=1
```

**Lo que enseña el fixture.** Los datos ficticios tienen un efecto grande en tasa (0,17 contra 0,81) y en abandono temprano (5 contra 1,5 días), y aun así el veredicto es ambiguo: 49 unidades en 24 períodos dejan series casi binarias, el NAP queda cerca de 0,6 y la prueba de aleatorización da p = 0,123. La tasa sube en parte porque con método se abandonan más unidades antes de entregarlas (8 contra 2), lo que achica el denominador; por eso la tesis se decide sobre P1 en conteo y no sobre la tasa. Con el volumen real de una persona, el piloto puede terminar ambiguo aunque el método funcione. La regla no se ablanda por eso: el resultado ambiguo lleva a la réplica (sección 8).

## 12. Qué puede concluir este piloto y qué no

**Con una sola persona se demuestra, en el mejor caso, que el método funcionó en ese caso: esa persona, ese MVP, esas semanas. No se demuestra que el marco funcione en general.** Ningún resultado de este piloto, por favorable que sea, autoriza a escribir "ODLC funciona para tiny teams".

### La regla 5-3-20 del What Works Clearinghouse

La documentación técnica del WWC (Kratochwill y otros, 2010, sección E) fija cuándo los resultados de varios estudios de caso único se combinan en una calificación de la intervención. Exige las tres condiciones a la vez:

1. **5:** al menos cinco artículos de investigación con diseño de caso único sobre la intervención, cada uno de los cuales cumpla los estándares del WWC, con o sin reservas.
2. **3:** que esos estudios los hayan hecho al menos tres equipos de investigación distintos, en tres lugares geográficos distintos.
3. **20:** que la suma de experimentos (ejemplos de diseño de caso único) entre todos los artículos llegue al menos a 20.

**"Equipo" en el WWC no significa equipo de trabajo.** Son grupos de investigadores independientes que diseñan, conducen y reportan los estudios. Diez tiny teams que corran el protocolo evaluados por el mismo autor del marco cuentan como un solo equipo de investigación. Tampoco "experimento" es lo mismo que "persona": un estudio con línea de base múltiple entre tres personas puede contar como uno o varios ejemplos de diseño según cómo se reporte, y el WWC no lo resuelve para este dominio.

El propio WWC aclara (nota 14) que esos umbrales son convenciones profesionales y que podrían revisarse con evidencia metaanalítica futura. Este piloto los adopta como vara, no como verdad empírica.

### Según el resultado

- **Si sostiene:** que, para esta persona y este MVP, la combinación A produjo más outcomes validados sin más horas ni más desperdicio, con tres demostraciones del efecto. Cuenta como un experimento de un estudio de un equipo de investigación, que además es el autor del marco.
- **Si descarta:** que la combinación A, tal como se especificó, no mejoró el trabajo de un tiny team en su caso más favorable (su propio diseñador). Es evidencia fuerte contra la parte heredada de ODLC para este público, y se registra en [[Objeciones al marco]] como resultado, no como falla de medición.
- **Si queda ambiguo:** nada sobre la tesis. Sí queda qué se aprendió sobre el costo de medir con una persona y qué volumen haría falta en la réplica.
- **H2:** con la siembra escasa, lo más probable es "sin datos". Lo que sí aporta es si la compuerta HA estuvo muerta (K3).
- **En ningún caso** el piloto valida la novedad de [[HACS]] (la organización humano-agente a escala); prueba un método de trabajo de una persona con agentes ([[Objeciones al marco]], Objeción 4).

### Camino de replicación (trabajo futuro)

No es parte de este piloto. Indica qué haría falta para llegar a 5-3-20 si el resultado sostiene o queda ambiguo:

| Paso | Qué | Aporta a la regla |
|---|---|---|
| 1 | Publicar el protocolo, las plantillas y el script con el resultado de este piloto, sea cual sea | Permite que otros corran exactamente lo mismo |
| 2 | Que otros tiny teams o fundadores solos corran el mismo protocolo sellado en su propio MVP, con línea de base múltiple entre tipos de objetivo o entre personas del equipo | Suma experimentos hacia los 20 |
| 3 | Que al menos dos grupos de evaluadores sin relación con el autor del marco, en lugares distintos, conduzcan y reporten estudios: ellos sellan el protocolo, sortean los inicios, guardan el manifiesto de siembra y corren el script | Son los equipos de investigación 2 y 3; el autor solo puede ser uno |
| 4 | Que cada estudio cumpla los estándares del WWC por sí mismo (tres demostraciones, ≥ 5 puntos por fase, acuerdo entre codificadores donde haya codificación) | Cada uno cuenta como uno de los 5 artículos |
| 5 | Reportar también los resultados negativos y los ambiguos | Sin esto, la serie tiene sesgo de publicación, como advierte el metaanálisis de Vaccaro y otros sobre su propio campo |

Mientras no se cumpla la regla completa, el marco solo puede decir "funcionó en N casos", con N y sus condiciones explícitos.

## 13. Decisiones pendientes del dueño

| Decisión | Propuesta de esta nota | Fuente de la propuesta |
|---|---|---|
| Producto concreto del MVP | — | Parámetro del dueño |
| Diseño | Línea de base múltiple más alternantes | WWC 2010; Kratochwill y Levin 2010 |
| Duración | 12 semanas, 2 puntos por semana, más 28 días de seguimiento | WWC (≥ 5 puntos por fase) |
| Fecha de inicio y de corte | — | Calendario del dueño |
| Duración e incentivo de la Fase 0 | Hasta 3 semanas, sin incentivo | Sin fuente |
| Umbrales de la Fase 0 | 50 % dolor, 30 % compromiso, 20 % descarte, extensión de 5 | Sin fuente; el kappa mínimo de 0,60 sí tiene (WWC) |
| Quién codifica a ciegas | Un agente de otra familia de modelo, sin acceso al protocolo | Sin fuente |
| Ventana de outcome y nivel mínimo | 28 días, nivel 2 | Sin fuente |
| Alfa | 0,05 | Convención |
| Umbrales de K1, K2, K3 | 70 %, 50 % en 3 semanas, 4 semillas | Sin fuente |
| Latencia baja y alerta de aprobación | 30 s y 95 % | Sin fuente; ThinkTech usa una tasa de anulación del 5 % como heurística, también sin validar (Síntesis) |
| Tasa de siembra | 15 % de los PR | Sin fuente para la cifra; Bainbridge pide que sea baja |
| Semillas mínimas para H2 | 5 por condición | Sin fuente |
| Tolerancia de horas | ±20 % | Sin fuente |
| Fuente de los bloques activos | Commits más registros de sesión de los agentes | Sin fuente |
| Segunda suscripción para el revisor | Un proveedor distinto del escritor | Panickssery y otros 2024 |
| Validador externo para lo irreversible | Un par o asesor, o excepción escrita | [[Investigación - Tiny teams y bootstrapping]] |
| Implementar K4 en el script | Sí, con corte parcial en la semana 8 | — |

## 14. Fuentes

Abiertas el 2026-10-08 para esta nota:

- Kratochwill, T. R., Hitchcock, J., Horner, R. H., Levin, J. R., Odom, S. L., Rindskopf, D. M. y Shadish, W. R., *Single-Case Designs Technical Documentation*, What Works Clearinghouse, versión 1.0 (piloto), junio de 2010. https://ies.ed.gov/ncee/WWC/Docs/ReferenceResources/wwc_scd.pdf (texto extraído con pdftotext: introducción sobre reversión y línea de base múltiple; sección de estándares sobre tres demostraciones, puntos por fase, alternantes y acuerdo; sección E, "Recommendations for combining studies", y su nota 14, sobre la regla 5-3-20).
- Kratochwill, T. R. y Levin, J. R., "Enhancing the scientific credibility of single-case intervention research: Randomization to the rescue", *Psychological Methods* 15(2), 2010, doi:10.1037/a0017736 (resumen vía OpenAlex). https://api.openalex.org/works/doi:10.1037/a0017736
- Barlow, D. H. y Hayes, S. C., "Alternating Treatments Design: One Strategy for Comparing the Effects of Two Treatments in a Single Subject", *Journal of Applied Behavior Analysis* 12, 1979, doi:10.1901/jaba.1979.12-199 (resumen vía OpenAlex). https://api.openalex.org/works/doi:10.1901/jaba.1979.12-199
- Vohra, S. y otros, "CONSORT extension for reporting N-of-1 trials (CENT) 2015 Statement", *BMJ*, 2015, doi:10.1136/bmj.h1738 (resumen vía OpenAlex). https://api.openalex.org/works/doi:10.1136/bmj.h1738
- Guest, G., Bunce, A. y Johnson, L., "How Many Interviews Are Enough?", *Field Methods* 18(1):59-82, 2006, doi:10.1177/1525822X05279903 (resumen vía Crossref). https://api.crossref.org/works/10.1177/1525822X05279903
- Lynch, M., reseña de *The Mom Test* (Rob Fitzpatrick, 2013), sin fecha en la página. https://mtlynch.io/book-reports/the-mom-test/
- Parker, R. I. y Vannest, K. J., "An Improved Effect Size for Single-Case Research: Nonoverlap of All Pairs", *Behavior Therapy* 40(4):357-367, 2009, doi:10.1016/j.beth.2008.10.006 (metadatos vía Crossref; sin resumen). https://api.crossref.org/works/10.1016/j.beth.2008.10.006
- Pustejovsky, J. E., Swan, D. M. y Chen, M., "Effect size definitions and mathematical details", viñeta del paquete SingleCaseES (definición de NAP). https://cran.r-project.org/web/packages/SingleCaseES/vignettes/Effect-size-definitions.html

Citadas desde notas del vault, con la fuente original en cada una: Vaccaro y otros 2024, METR 2025, registered reports y kill criteria ([[Propuestas existentes - Objeciones 3 y 4]]); Bainbridge 1983, Kim y otros 2025 ([[Propuestas existentes - Revisión en manos de agentes]]); Camuffo y otros 2020 y 2024, COSO 2006, Panickssery y otros 2024, Xu, Brand y otros, Wang y otros, Park y otros 2024, Roberts 2004 ([[Investigación - Tiny teams y bootstrapping]]); Threat Image Projection, Bahner y otros 2008, checklists de la OMS y Ontario ([[Objeciones al marco]]); Beyond Budgeting, Holmström y Milgrom, IMDA, Mosier y Skitka, Tannenbaum y Cerasoli, ThinkTech ([[Síntesis - Cómo encajan las propuestas existentes]]).

## Comandos de verificación

Read-only, desde la raíz del repo.

```bash
# El script corre sobre el fixture (exit 0) y sobre el caso de abandono (exit 1)
python3 scripts/piloto_metricas.py scripts/fixtures/piloto; echo exit=$?
python3 scripts/piloto_metricas.py scripts/fixtures/piloto/caso-abandono; echo exit=$?
# WWC: reversión no apropiada si el efecto no se revierte; tres intentos; 5 puntos; 5-3-20
curl -sL https://ies.ed.gov/ncee/WWC/Docs/ReferenceResources/wwc_scd.pdf -o /tmp/wwc.pdf && pdftotext /tmp/wwc.pdf - | grep -n "unlikely to be reversed\|at least three attempts\|at least 5 data points per phase\|five repetitions of the alternating\|three different research teams\|totals at least 20\|professional conventions\|at least 0.60 if"; rm -f /tmp/wwc.pdf
# Guest y otros: saturación dentro de las primeras doce entrevistas
curl -s https://api.crossref.org/works/10.1177/1525822X05279903 | grep -o "saturation occurred within the first twelve interviews"
# Barlow y Hayes: tres formas de interferencia entre tratamientos
curl -s "https://api.openalex.org/works/doi:10.1901/jaba.1979.12-199" | grep -o "carryover\|sequential\|alternation" | sort -u
# Insumos del vault que la nota cita
grep -n "g de Hedges = −0,23" "docs/00_crudo/Propuestas existentes - Objeciones 3 y 4.md"
grep -n "Bainbridge (1983)" "docs/00_crudo/Propuestas existentes - Revisión en manos de agentes.md"
grep -n "Panickssery\|COSO" "docs/00_crudo/Investigación - Tiny teams y bootstrapping.md" | head -3
```
