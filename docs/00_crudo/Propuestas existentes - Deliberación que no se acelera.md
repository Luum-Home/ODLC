---
tags: [crudo, investigacion, objeciones]
status: crudo
created: 2026-10-08
---

# Propuestas existentes: la deliberación que no se acelera

Relevamiento de lo que otras personas u organizaciones ya propusieron para un problema que el vault plantea en "Nuevos cuellos de botella" (docs/01_problema) y que mide el Decision Lead Time de "Métricas organizacionales" (docs/04_metricas): si los agentes comprimen el research y el desarrollo, el tiempo total queda dominado por planificar, discutir, decidir y alinear, como en la ley de Amdahl, donde la parte que no se paraleliza pone el techo de la aceleración. Las cinco vías de partida venían de una conversación previa y se trataron como hipótesis a refutar. No incluye propuestas propias. Todas las fuentes se consultaron el 2026-10-08; cada número cita de dónde sale. Las etiquetas [medido], [testimonio] y [opinión] indican el tipo de evidencia.

## Resumen

1. **Vía 1, separar reversibles de irreversibles y fijar quién decide: se sostiene como forma de bajar el volumen de lo que se discute, con evidencia débil.** El respaldo es testimonio (cartas de Amazon de 2015 y 2016, handbook de GitLab) y una correlación de consultora sin datos publicados (Bain). Nadie midió cuánto tiempo ahorra, ni cuánto cuesta clasificar mal una decisión como reversible.
2. **Vía 2, consentimiento en vez de consenso: no se sostiene como acelerador.** No apareció ninguna medición de tiempo. Los casos documentados muestran carga de reuniones y participación desigual (King y Griffin, 2024), y los dos casos más conocidos de autogestión formal terminaron en salidas (18 % del personal de Zappos) o en abandono (Medium, 2016).
3. **Vía 3, abaratar la discusión con preparación previa (incluidos agentes): matizada.** La preparación mueve el tiempo de lugar, no lo borra (un buen memo de Amazon "debería llevar una semana o más"). Con IA, la preparación individual se abarata de forma medida (12,7 % a 16,4 % menos tiempo en P&G), pero en un RCT de 7.137 personas el tiempo en reuniones no cambió. Además, la parte que la IA mejor resuelve, el análisis, es la que menos pesa en la calidad de la decisión: el proceso pesó seis veces más (Lovallo y Sibony, 2010).
4. **Vía 4, reemplazar debate por alternativas construidas en paralelo: es la mejor respaldada, pero para otra cosa.** Hay evidencia medida de que explorar alternativas en paralelo mejora el resultado (Dow et al. 2010; Nutt 1993) y de que considerar varias a la vez se asocia a decidir más rápido (Eisenhardt 1989, 8 empresas). La objeción clásica a Toyota, el costo de sostener varias alternativas, se debilita con agentes. Pero el costo pasa a la evaluación humana de N alternativas, y solo aplica a preguntas que la evidencia puede zanjar.
5. **Vía 5, aceptar lo irreducible: se sostiene en parte, aunque "irreducible" exagera.** El conflicto de relación y de proceso se asocia de forma estable a peor desempeño (metaanálisis de 116 estudios), y un spike no lo resuelve. Pero un mediador con IA logró en laboratorio declaraciones grupales preferidas y grupos menos divididos en temas de valores (Tessler et al., 2024). Se puede abaratar, aunque no eliminar.
6. **Otra vía encontrada: plazo y disputa explícita** ("disagree and commit", decidir con 70 % de la información, escalar pronto el desacuerdo de fondo). Es testimonio de Amazon. Es consistente con Eisenhardt (la resolución activa del conflicto acelera), sin medición propia.
7. **Reparto de tiempo:** en el único estudio con instrumentación abierto, los desarrolladores dedicaron 21,0 % a codificar y 24,4 % a actividades colaborativas (Meyer et al., 20 personas, 4 empresas). No se encontró ninguna medición de qué fracción de un proyecto de software se va en decidir.
8. **IA y reuniones (2025):** el efecto promedio sobre el tiempo en reuniones fue nulo, pero escondía firmas con +13 % y otras con −9 % (Dillon et al.). Los autores lo atribuyen a que la coordinación depende de los demás, no de cada uno.
9. **Costo de decidir rápido y mal:** la mitad de las decisiones estudiadas por Nutt fracasaron. Las impuestas por poder o persuasión tuvieron 33 % de éxito, contra más de 80 % de las participativas. La rapidez por sí sola no es lo que falla: falla la rapidez lograda imponiendo una sola opción.
10. **Huecos:** no hay ningún estudio que mida el Decision Lead Time con y sin agentes, ni el costo de equivocarse al clasificar una decisión como reversible, ni una comparación de tiempo entre consentimiento y consenso.

---

## Vía 1: discutir menos cosas (reversibilidad y derechos de decisión)

### 1.1 Decisiones de tipo 1 y tipo 2 (puertas de una y de dos vías)

- **Quién y dónde.** Jeff Bezos, carta a los accionistas de Amazon de 2015 (publicada en abril de 2016, SEC exhibit 99.1). La complementa la carta de 2016 con "high-velocity decision making".
- **Qué resuelve.** Que una organización grande aplique a decisiones reversibles el proceso pesado que corresponde a las irreversibles. Según la carta, el resultado es lentitud, aversión al riesgo y menos experimentación. Las de tipo 2 "can and should be made quickly by high judgment individuals or small groups".
- **Dónde se aplicó.** Amazon. GitLab lo adoptó como norma explícita: decidir suponiendo reversibilidad y volver atrás si no funciona (handbook, sección "Making Decisions", vista en resultados de búsqueda; la página abierta no devolvió el contenido).
- **Evidencia.** [testimonio]. La carta de 2016 agrega tres reglas: decidir con alrededor de 70 % de la información deseada, corregir rápido y "disagree and commit". No publica ningún dato.
- **Críticas o fallas.** (a) La clasificación es en sí misma una decisión, y nadie dice quién la toma ni cómo se audita. (b) En software, muchas decisiones parecen de dos vías y no lo son: migraciones de datos, contratos de API públicos, compromisos con clientes. No se encontró ningún estudio del costo de equivocarse en esa clasificación. (c) La regla del 70 % supone poder corregir rápido, y eso depende de la observabilidad y del costo de revertir, no de la voluntad.
- **Combinabilidad.** Es la puerta de entrada de las demás: decide a qué decisiones se les aplica la 1.2, la vía 3 o la vía 4. En el vault ya aparece como criterio de degradación controlada (principio 5 de la objeción 5).

### 1.2 Derechos de decisión explícitos: RAPID, DACI, DRI

- **Quién y dónde.** RAPID: Paul Rogers y Marcia Blenko, "Who Has the 'D'?", *Harvard Business Review*, 2006-06-28 (versión en bain.com). Roles: Recommend, Agree (veto), Perform, Input, Decide. DACI: originado en Intuit y difundido por el Team Playbook de Atlassian (Driver, Approver, Contributors, Informed), con un único aprobador: "The one person (yes: one!)". DRI: GitLab (TeamOps).
- **Qué resuelve.** La demora que se produce cuando no está claro quién decide, cuando demasiados tienen veto o cuando demasiados opinan. Rogers y Blenko ubican los cuellos de botella en cuatro interfaces: global/local, centro/unidad de negocio, función/función y adentro/afuera (socios).
- **Dónde se aplicó.** Bain lo usa como producto de consultoría (cita a Wyeth como ejemplo). DACI se usa en Atlassian y en equipos de producto. DRI en GitLab.
- **Evidencia.** [medido por la consultora, sin datos publicados]. Bain afirma una correlación, "con al menos 95 % de confianza", entre la efectividad de las decisiones y el desempeño del negocio, a partir de un programa de 10 años con más de 1.000 empresas (Paul Rogers, bain.com, 2017-11-18). El benchmarking se basa en encuestas y entrevistas. El artículo de 2006 dice que "solo alrededor de 15 %" de las empresas decide de forma efectiva. El playbook de Atlassian dice que, según una encuesta de McKinsey, los proyectos con DACI tienen 25 % más de éxito; no da la referencia y no se pudo verificar, así que no se usa como dato.
- **Críticas o fallas.** Es correlación con datos autoinformados de la misma consultora que vende la intervención. El rol "Agree" de RAPID reintroduce el veto que se quería evitar. Fijar quién decide acorta la espera, pero no el desacuerdo: si quien tiene la D decide contra la opinión de quien ejecuta, el costo reaparece como resistencia en la ejecución (ver Nutt, sección de costos).
- **Combinabilidad.** Se combina con la 1.1: la reversibilidad define cuánto proceso lleva una decisión y RAPID/DACI definen quién la toma. Es compatible con la vía 3 (el Recommend o el Driver es quien prepara, y puede apoyarse en agentes). Choca en parte con la vía 2, que distribuye la decisión en el círculo.

---

## Vía 2: consentimiento en lugar de consenso

### 2.1 Sociocracia y Sociocracy 3.0

- **Quién y dónde.** Sociocracia (Gerard Endenburg, Países Bajos) y sus derivadas: Sociocracy for All y S3. Un círculo aprueba una propuesta si no hay objeciones razonadas, es decir, argumentos de que la propuesta dañaría el propósito del grupo. El criterio es "good enough for now, safe enough to try"; según los resultados de búsqueda, no es unanimidad ni consenso. Las páginas de S3 y de Sociocracy for All devolvieron 404 o 403, y la definición se tomó de las descripciones de búsqueda de esas mismas organizaciones.
- **Qué resuelve.** El veto por preferencia del consenso: no hace falta que a todos les guste la propuesta, alcanza con que nadie demuestre que hace daño.
- **Dónde se aplicó.** Cooperativas, ONG, comunidades de vivienda y algunas empresas.
- **Evidencia.** [estudio de caso]. King y Griffin, *Voluntas*, 2024: un único caso (Phoenix Co-Housing), 4 días de observación y 16 entrevistas. Encuentran que empodera a los miembros y reduce la dominación, pero documentan una curva de aprendizaje dura, participación desigual ("not everybody" participa) y cuatro formas de desigualdad: estatus (síndrome del fundador), expectativas, aplicación desigual de las reglas entre círculos y capacidades (tiempo, energía, habilidades emocionales). **No se encontró ninguna medición del tiempo de decisión frente al consenso o a la decisión jerárquica.**
- **Críticas o fallas.** Bajar el umbral de aprobación no baja el número de reuniones: la integración de objeciones es en sí misma un proceso. Los casos de autogestión formal más difundidos dejaron costos medidos. En Zappos, 18 % del personal (260 personas) se fue con un pago de salida después del memo de marzo de 2015 que impuso holacracia (Time, 2016-01-14). Medium abandonó holacracia porque, según Andy Doyle, ejercía un "small but persistent tax" sobre la efectividad (Fortune, 2016-03-04). Holacracia no es sociocracia, pero comparte la gobernanza por consentimiento.
- **Combinabilidad.** Es compatible con la 1.1 ("safe enough to try" es el criterio de reversibilidad visto desde el grupo) y con la vía 4 (un experimento barato hace más fácil consentir). Choca con la 1.2: un solo decisor y un círculo que consiente son modelos alternativos.

### 2.2 Advice process

- **Quién y dónde.** Dennis Bakke (AES, *Joy at Work*, 2005), difundido por Frederic Laloux (*Reinventing Organizations*, 2014). Cualquiera puede decidir después de consultar a quienes saben y a los afectados. No hace falta ni consentimiento ni consenso.
- **Qué resuelve.** Combina la velocidad de la decisión individual con la legitimidad de la consulta, sin bloqueo.
- **Dónde se aplicó.** AES, Morning Star, Buurtzorg y Equal Experts, que lo usa como "backbone" de su gestión (playbook público).
- **Evidencia.** [testimonio]. El playbook de Equal Experts no publica datos de velocidad ni de resultado. La evidencia de Laloux son casos elegidos por el autor (ya señalado en la objeción 6 del vault).
- **Críticas o fallas.** Depende de que quien decide consulte de verdad. Sin registro de la consulta, se degrada en decisión unilateral, que es la táctica que Nutt asocia al fracaso. No hay medición de tiempo.
- **Combinabilidad.** Se combina naturalmente con la vía 3: la consulta asíncrona sobre un documento escrito es su forma más barata. Encaja con la 1.2 si el que decide es el DRI.

---

## Vía 3: abaratar la discusión con preparación previa

### 3.1 Memo narrativo de seis páginas (Amazon)

- **Quién y dónde.** Amazon. Carta a los accionistas de 2017: narrativas de seis páginas en lugar de diapositivas, leídas en silencio al comienzo de la reunión.
- **Qué resuelve.** Que la reunión arranque con todos sabiendo lo mismo, y que la claridad del razonamiento se ponga a prueba al escribir y no en la sala.
- **Evidencia.** [testimonio]. La carta no mide el ahorro. Sí dice cuánto cuesta: el error típico es creer que un buen memo sale en uno o dos días, cuando "great memos probably should take a week or more".
- **Críticas o fallas.** Es la refutación más directa de "abaratar": la preparación no achica el tiempo total, lo saca de la reunión y lo pone en la escritura. Gana si muchas personas leen el memo (se escribe una vez y se ahorra en cada lector), y pierde con audiencias chicas.
- **Combinabilidad.** Es la base material de la 2.2 (consultar sobre un texto), de la 1.2 (el Recommend entrega un memo) y de la 3.3 (es la tarea que se delegaría en agentes).

### 3.2 RFC, design docs y ADR

- **Quién y dónde.** RFC internos (Uber y otras; Gergely Orosz, "Scaling Engineering Teams via RFCs", 2018-10-03, actualizado en 2022) y Architecture Decision Records (Michael Nygard, 2011).
- **Qué resuelve.** Decidir de forma asíncrona y dejar registrada la decisión y su contexto, para no volver a discutirla.
- **Dónde se aplicó.** En Uber, el proceso pasó de mails a toda la ingeniería a listas por dominio, plantillas y campos de aprobador a medida que la organización creció de decenas a "un par de miles" de ingenieros. Orosz advierte que con varios miles aparecen problemas nuevos, sin detallarlos.
- **Evidencia.** [testimonio] para los RFC. Para los ADR [medido, minería de repositorios]: de Santana Junior et al. (ICSA 2026) analizaron 921 repositorios de GitHub con alrededor de 5.800 ADR. Cerca de 3.674 (63 %) se abrieron directamente con estado "accepted", "bypassing the deliberative context", y los atributos de los ADR mostraron correlaciones mayormente chicas con la calidad del proyecto (code smells, tiempo de resolución de issues).
- **Críticas o fallas.** El dato de los ADR muestra que el registro tiende a convertirse en acta de una decisión ya tomada en otro lado: documenta, pero no reemplaza la deliberación. No se encontró ninguna medición de cuánto tiempo de decisión ahorran los RFC.
- **Combinabilidad.** El ADR es la memoria que evita reabrir decisiones; conecta con la hipótesis H1 de "Métricas organizacionales" (referenciar memoria evita debates redundantes), que sigue sin evidencia directa.

### 3.3 Agentes que preparan opciones y tradeoffs, y facilitan la discusión

- **Quién y dónde.** No hay una propuesta formal con nombre. La evidencia viene de experimentos con IA generativa en trabajo de conocimiento y en deliberación grupal.
- **Evidencia [medido]:**
  - *Preparación.* Dell'Acqua et al., "The Cybernetic Teammate" (NBER w33641, 2025; *Organization Science*, 2026): 776 profesionales de P&G, experimento de campo preregistrado. Un individuo con IA igualó a un equipo de dos sin IA (+0,37 DE contra +0,39 DE de equipos con IA). La IA redujo el tiempo de trabajo 16,4 % en individuos y 12,7 % en equipos, y las propuestas quedaron más balanceadas entre la mirada técnica y la comercial.
  - *Reuniones.* Dillon, Jaffe, Immorlica y Stanton, "Shifting Work Patterns with Generative AI" (NBER w33795, versión del 2025-11-17): RCT en 66 firmas y 7.137 trabajadores. Quienes usaron la herramienta dedicaron dos horas menos por semana al mail, pero el tiempo en reuniones no cambió: el resultado descarta efectos fuera de −0,01 a 0,21 horas sobre una media de 5,22 horas semanales. El efecto se concentró en conductas que cada uno "could change independently".
  - *Heterogeneidad.* Dillon, Jaffe, Peng y Cambon, "Early Impacts of M365 Copilot" (arXiv 2504.11443, 2025): más de 6.000 trabajadores en 56 firmas. El efecto nulo promedio sobre las reuniones combina seis firmas con +26 minutos semanales (+13 %) y otras con −25 minutos (−9 %). Además, los usuarios entraron más tarde y se fueron antes de las reuniones.
  - *Facilitación.* Alsobay, Rothschild, Hofman y Goldstein (arXiv 2508.08242, revisado el 2026-07-02): 1.475 participantes en 281 grupos. Un facilitador LLM aumentó la información compartida, pero no tuvo efecto significativo sobre la decisión final.
- **Críticas o fallas.** (a) **El análisis no es lo que más pesa.** Lovallo y Sibony (*McKinsey Quarterly*, marzo de 2010; 1.048 decisiones reportadas por ejecutivos) encontraron que el proceso, es decir, discutir incertidumbres y puntos de vista contrarios al líder, importó seis veces más que el análisis. Pasar de cuartil inferior a superior en proceso se asoció a +6,9 puntos de ROI, contra +5,3 en análisis (subconjunto de 673 decisiones). Si los agentes abaratan el análisis y la organización usa el ahorro para acortar la discusión, se recorta la parte que más rinde. (b) La coordinación es un equilibrio del grupo: el ahorro individual no se traslada a la reunión si los demás no cambian (Dillon et al.). (c) Las opciones preparadas por un agente anclan la discusión. Es el sesgo de automatización que el vault ya trató en la objeción 5.
- **Combinabilidad.** Es complementaria de la vía 4 (el agente prepara y además construye) y de la 1.2 (el agente asiste al Recommend). Choca con su uso como excusa para acortar el debate (ver crítica a).

---

## Vía 4: reemplazar debate por evidencia construyendo alternativas en paralelo

### 4.1 Set-based concurrent engineering (Toyota)

- **Quién y dónde.** Allen Ward, Jeffrey Liker, John Cristiano y Durward Sobek, "The Second Toyota Paradox: How Delaying Decisions Can Make Better Cars Faster", *Sloan Management Review*, primavera de 1995; Sobek, Ward y Liker, "Toyota's Principles of Set-Based Concurrent Engineering", 1999. El PDF del artículo de 1995 devolvió 403; se usa lo que dicen los resúmenes y la revisión de Toche et al.
- **Qué resuelve.** En vez de elegir pronto una alternativa e iterarla, se sostienen conjuntos de alternativas y se los va angostando a medida que la evidencia descarta las débiles. La decisión se demora a propósito y se vuelve más barata, porque llega con datos.
- **Dónde se aplicó.** Desarrollo de producto en Toyota. Raudberget (*Strojniški vestnik*, 2010) documenta implementaciones en cuatro empresas.
- **Evidencia.** [testimonio y casos]. Raudberget reporta mejoras autoevaluadas en innovación, costo y desempeño del producto, con costo de desarrollo algo mayor y plazos más largos. Toche, Pellerin y Fortin (*Design Science*, 2020), en una revisión que partió de 1.733 publicaciones, concluyen que SBD tiene "relatively low theoretical development" y que el costo de sostener varias alternativas durante mucho tiempo puede ser perjudicial.
- **Críticas o fallas.** La crítica central es el costo de construir N alternativas, y es la que más cambia con agentes. Lo que no cambia es el costo de evaluarlas: comparar N prototipos consume atención humana, que es el recurso que la investigación de estimación del vault identificó como escaso (revisión +91 %, PR de agentes esperando 4,6 a 5,3 veces más).
- **Combinabilidad.** Es el complemento natural de la 1.1: las alternativas paralelas transforman una decisión de una vía en varias apuestas chicas de dos vías. Se combina con la 3.3 (agentes que construyen las alternativas).

### 4.2 Prototipado paralelo y "build to decide"

- **Quién y dónde.** Steven Dow, Alana Glassco, Jonathan Kass, Melissa Schwarz, Daniel Schwartz y Scott Klemmer, "Parallel Prototyping Leads to Better Design Results, More Divergence, and Increased Self-Efficacy", *ACM TOCHI* 17(4), 2010. Uber, "AI prototyping" (Aayush Agrawal y Akanksha Sharma, blog de Uber, 2026-04-15).
- **Qué resuelve.** Reemplazar la discusión sobre descripciones abstractas por la comparación de cosas concretas.
- **Evidencia.** [medido, laboratorio] Dow et al.: 33 participantes, la misma cantidad de prototipos (cinco más el final) y el mismo tiempo en ambas condiciones. Las piezas hechas en paralelo superaron a las hechas en serie en click-through real y en evaluación de expertos, y fueron más diversas. Casi la mitad de los participantes en serie reaccionó mal a la crítica; ninguno en paralelo. [testimonio] Uber: un PM dice que dos horas de prototipado destrabaron cuatro semanas de discusión, y otro exploró seis conceptos en unos 20 minutos.
- **Críticas o fallas.** Dow et al. miden calidad del diseño, no tiempo de decisión, y con novatos en una tarea chica. El mismo post de Uber lista los riesgos: tomar el prototipo por una decisión ("prototype seduction"), saltear el registro de los tradeoffs, anclarse en el primer prototipo, prototipar en silos y suponer que prototipar no cuesta nada.
- **Combinabilidad.** Igual que la 4.1. Además necesita la 3.2: si nadie registra por qué ganó una alternativa, la comparación no deja memoria.

### 4.3 Evidencia de decisión que respalda la vía

- **Eisenhardt**, "Making Fast Strategic Decisions in High-Velocity Environments", *Academy of Management Journal*, 1989 (resumen de AcaWiki; el PDF devolvió 404): estudio inductivo de 8 empresas de microcomputadoras. Los decisores rápidos usaron más información y más alternativas, no menos. La proposición 2 dice que cuantas más alternativas se consideran a la vez, más rápido es el proceso. La resolución activa del conflicto también aceleró. [medido, 8 casos]
- **Nutt**, "The Identification of Solution Ideas During Organizational Decision Making", *Management Science*, 1993: 168 casos. La táctica más usada, imponer una idea ya armada, "seldom successful"; generar varias alternativas mejoró los resultados. [medido, casos]
- **Límite.** Ninguna de las dos fuentes separa "alternativas consideradas" de "alternativas construidas". La vía 4 extrapola de una a la otra.

---

## Vía 5: aceptar lo irreducible

- **Quién y dónde.** No es una propuesta con autor. Es la conclusión de que algunas discusiones, sobre valores, prioridades, poder o confianza, no se resuelven con más información.
- **Evidencia [medido]:**
  - de Wit, Greer y Jehn, "The Paradox of Intragroup Conflict: A Meta-Analysis", *Journal of Applied Psychology* 97(2), 2012: 116 estudios y 8.880 grupos. El conflicto de relación y el de proceso tuvieron relaciones negativas estables con el desempeño. El de tarea no, y se asoció mejor al desempeño en equipos de alta dirección y cuando se medía la calidad de la decisión. Lo que un spike resuelve es el conflicto de tarea, justamente el menos dañino; los otros dos no se resuelven con evidencia técnica.
  - En contra de "irreducible": Tessler et al., *Science*, 2024-10-18 (vía MIT Technology Review, 2024-10-17). Con 5.734 participantes en el Reino Unido, un mediador LLM (la "Habermas Machine") produjo declaraciones grupales sobre temas divisivos (Brexit, inmigración, salario mínimo) que los participantes eligieron 56 % de las veces frente a las de mediadores humanos, y los grupos quedaron menos divididos. Los autores reconocen que no verifica hechos ni modera la discusión. Son declaraciones de opinión, no decisiones con recursos o poder en juego.
- **Críticas o fallas.** "Irreducible" lo exagera: hay evidencia de que la mediación abarata el acuerdo en temas de valores. Pero no hay evidencia de que lo haga cuando hay intereses o poder en juego. La carta de Amazon de 2016 recomienda escalar pronto el desacuerdo de fondo en vez de dejar que gane el que aguanta más; es testimonio.
- **Combinabilidad.** Funciona como filtro previo a las demás: separa lo que se puede zanjar con evidencia (vía 4) de lo que necesita un decisor (vía 1.2) o una mediación (3.3, en la forma de Tessler).

---

## Costo de decidir rápido y mal

- **Nutt** (Ohio State University, nota de prensa del 2002-08-06, sobre más de 400 decisiones): alrededor de 50 % de las decisiones fracasan y cerca de un tercio nunca se usan. Dos tercios se apoyan en tácticas propensas al fracaso. Las implementadas por poder o persuasión tienen 33 % de éxito, frente a más de 80 % de las participativas. [medido, casos]
- **Lovallo y Sibony** (2010): ver 3.3. El proceso de discusión se asoció a +6,9 puntos de ROI. [medido, autorreporte de ejecutivos]
- **Eisenhardt** (1989): la rapidez se asoció a mejor desempeño, pero lograda con más alternativas y más información, no con menos. [medido, 8 casos]
- **Bezos** (carta de 2016): para la mayoría de las decisiones, ser lento cuesta más que equivocarse, si se puede corregir rápido. [opinión]
- **Lectura conjunta.** Las fuentes no se contradicen si se separa *rapidez* de *atajo*. Decidir rápido considerando varias alternativas se asocia a buenos resultados; decidir rápido imponiendo una sola, a fracasos. El Decision Lead Time del vault, que interpreta un DLT bajo como posible "falta de exploración", necesitaría distinguir esos dos casos: el número solo no los separa.

---

## Tabla de combinabilidad

| | 1.1 Reversibilidad | 1.2 Derechos de decisión | 2 Consentimiento / advice | 3 Preparación (memo, RFC, agentes) | 4 Alternativas en paralelo | 5 Lo irreducible |
|---|---|---|---|---|---|---|
| **1.1** | — | Complementa: una define cuánto proceso, la otra quién decide | Complementa ("safe enough to try") | Complementa: la preparación pesada se reserva para las de una vía | Complementa: convierte una de una vía en varias de dos vías | Filtro previo |
| **1.2** | | — | Choca en parte: un decisor contra un círculo; el advice process encaja con un DRI | Complementa: quien recomienda prepara | Complementa: quien decide elige entre construidas | Necesaria: lo que no se zanja con evidencia lo zanja alguien |
| **2** | | | — | Complementa: consultar sobre texto es lo más barato | Complementa: un experimento chico es fácil de consentir | Débil: el consentimiento no resuelve conflicto de relación (King y Griffin) |
| **3** | | | | — | Complementa, con riesgo de anclaje si el agente arma una sola opción | Parcial: mediación con IA (Tessler) |
| **4** | | | | | — | No aplica: solo sirve para el conflicto de tarea |

---

## Evidencia sobre el reparto de tiempo entre coordinación y ejecución

- **Meyer, Barton, Murphy, Zimmermann y Fritz**, "The Work Life of Developers", *IEEE TSE* 43(12), 2017: monitoreo de 20 desarrolladores de 4 empresas durante 11 días en promedio. Codificar ocupó 21,0 % del tiempo, el mail 14,5 % y las actividades colaborativas (reuniones planificadas e informales) 24,4 %. Los autores advierten que las reuniones probablemente estén subestimadas. [medido, muestra chica]
- **Dillon et al.** (2025): media de 5,22 horas semanales en reuniones de Teams en trabajadores de conocimiento, sin cambio con IA. [medido]
- **Microsoft Work Trend Index**, "Breaking down the infinite workday", 2025-06-17, con telemetría de Microsoft 365 hasta febrero de 2025: 57 % de las reuniones son llamadas ad hoc sin invitación, y hay una interrupción cada 2 minutos en horario central. [medido por el vendor, sin método publicado]
- **Ya en el vault** ("Investigación - Estimación y tiempo con agentes", 2026-10-07): la ganancia cae de +240 % en commits a +30 % en releases (Demirer et al., NBER 2026), y la codificación es cerca de 32 % del esfuerzo en un dominio (Jones). Son consistentes con el techo tipo Amdahl, aunque ninguno mide el tiempo de decisión.
- **Lo que no se encontró:** ninguna medición abierta de qué fracción de un proyecto de software se va en decidir. La encuesta de McKinsey "Decision making in the age of urgency" (2019, 1.259 respuestas según los resultados de búsqueda) se cita mucho con cifras de tiempo y costo de las decisiones, pero no se pudo abrir (timeout repetido) y no se usa como dato.

---

## Huecos

1. **Ninguna medición del Decision Lead Time con y sin agentes.** Los experimentos con IA miden mail, documentos y reuniones, no el tiempo desde la definición del problema hasta la decisión.
2. **Ninguna comparación de tiempo entre consentimiento, consenso y decisor único** en organizaciones reales.
3. **Ningún estudio del costo de clasificar mal la reversibilidad**: cuántas decisiones tratadas como de dos vías resultaron de una, y qué costaron.
4. **"Build to decide" con agentes no tiene evidencia controlada.** Lo que hay es Dow et al. (novatos, una tarea chica, calidad y no tiempo) y testimonio de Uber. Falta medir si construir N alternativas acorta la decisión una vez que se cuenta la evaluación humana.
5. **La paradoja de Lovallo y Sibony no está resuelta para agentes:** si la IA abarata el análisis, ¿la organización invierte el ahorro en mejor proceso de discusión o lo usa para discutir menos? Ningún estudio lo mide.
6. **La coordinación como equilibrio del grupo:** los RCT de Copilot trataron individuos dentro de equipos sin tratar. Un diseño aleatorizado por equipo podría dar un resultado distinto sobre las reuniones; no se encontró ninguno.

---

## Fuentes (todas consultadas el 2026-10-08)

- Amazon, carta a los accionistas de 2015 (SEC, exhibit 99.1): https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm
- Amazon, carta a los accionistas de 2016: https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders
- Amazon, carta a los accionistas de 2017: https://www.aboutamazon.com/news/company-news/2017-letter-to-shareholders
- Rogers y Blenko, "Who Has the 'D'?" (2006-06-28): https://www.bain.com/insights/who-has-the-d
- Rogers, "The five essential steps for making better business decisions" (Bain, 2017-11-18): https://www.bain.com/insights/the-five-essential-steps-for-making-better-business-decisions-ameinfo/
- Atlassian Team Playbook, DACI: https://www.atlassian.com/team-playbook/plays/daci
- King y Griffin, "Governing for the Common Good: The Possibilities of Sociocracy in Nonprofit Organizations", *Voluntas* (2024): https://eprints.whiterose.ac.uk/207175 y https://www.cambridge.org/core/product/5ABEA6985AD4D87B0AAC99CBA843E3A5/core-reader
- Time, "Zappos' Weird Management Style Is Costing It More Employees" (2016-01-14): https://time.com/4180791/zappos-holacracy-buyouts
- Fortune, "Management changes at Medium" (2016-03-04): https://fortune.com/2016/03/04/management-changes-at-medium/
- Equal Experts, playbook "The Advice Process": https://playbooks.equalexperts.com/advice-process
- Orosz, "Scaling Engineering Teams via RFCs: Writing Things Down" (2018-10-03, act. 2022-09-21): https://blog.pragmaticengineer.com/scaling-engineering-teams-via-writing-things-down-rfcs/
- de Santana Junior et al., "Architecture Decision Records: Adoption, Impact, and Developer Engagement in Open-Source Software" (ICSA 2026): https://conf.researchr.org/details/icsa-2026/icsa-2026-papers/34/Architecture-Decision-Records-Adoption-Impact-and-Developer-Engagement-in-Open-Sou
- Dell'Acqua et al., "The Cybernetic Teammate" (NBER w33641): https://www.nber.org/papers/w33641 y https://www.nber.org/system/files/working_papers/w33641/w33641.pdf
- Dillon, Jaffe, Immorlica y Stanton, "Shifting Work Patterns with Generative AI" (NBER w33795; arXiv 2504.11436v4): https://www.nber.org/papers/w33795 y https://arxiv.org/abs/2504.11436v2
- Dillon, Jaffe, Peng y Cambon, "Early Impacts of M365 Copilot" (arXiv 2504.11443): https://arxiv.org/abs/2504.11443
- Alsobay, Rothschild, Hofman y Goldstein, "Bringing Everyone to the Table" (arXiv 2508.08242): https://arxiv.org/abs/2508.08242
- Lovallo y Sibony, "The case for behavioral strategy", *McKinsey Quarterly* (marzo de 2010), PDF de curso: https://docs.univr.it/documenti/OccorrenzaIns/matdid/matdid176416.pdf
- Toche, Pellerin y Fortin, "Set-based design: a review and new directions", *Design Science* (2020): https://www.cambridge.org/core/services/aop-cambridge-core/content/view/DD708BAB57193C6635CA85C7508FE82E/S2053470120000165a.pdf/set-based-design-a-review-and-new-directions.pdf
- Raudberget, "Practical Applications of Set-Based Concurrent Engineering in Industry", *Strojniški vestnik* 56(11) (2010): https://sv-jme.eu/?p=5976
- Dow et al., "Parallel Prototyping Leads to Better Design Results, More Divergence, and Increased Self-Efficacy", *ACM TOCHI* (2010), versión enviada: https://hci.stanford.edu/publications/2010/parallel-prototyping/ParallelPrototyping2010-submitted.pdf
- Agrawal y Sharma, "AI prototyping" (Uber, 2026-04-15): https://www.uber.com/us/en/blog/ai-prototyping
- Eisenhardt (1989), resumen en AcaWiki: https://acawiki.org/Making_fast_strategic_decisions_in_high-velocity_environments
- Nutt, "The Identification of Solution Ideas During Organizational Decision Making", *Management Science* (1993): https://ideas.repec.org/a/inm/ormnsc/v39y1993i9p1071-1085.html
- Ohio State University, "Half of business decisions fail…" (2002-08-06): https://news.osu.edu/half-of-business-decisions-fail-because-of-managements-blunders-new-study-finds/
- de Wit, Greer y Jehn, "The Paradox of Intragroup Conflict: A Meta-Analysis" (2012): https://repub.eur.nl/pub/37902
- MIT Technology Review, "AI could help people find common ground during deliberations" (2024-10-17), sobre Tessler et al., *Science*: https://www.technologyreview.com/2024/10/17/1105810/ai-could-help-people-find-common-ground-during-deliberations/
- Meyer et al., "The Work Life of Developers: Activities, Switches and Perceived Productivity", *IEEE TSE* (2017): https://thomas-zimmermann.com/publications/files/meyer-tse-2018.pdf
- Microsoft WorkLab, "Breaking down the infinite workday" (2025-06-17): https://microsoft.com/en-us/worklab/work-trend-index/breaking-down-infinite-workday

Fuentes vistas solo como resultado de búsqueda o que no se pudieron abrir, y que no se usan como dato: McKinsey, "Decision making in the age of urgency" (2019; timeout en todas las URL); Herbsleb y Mockus sobre demora del trabajo distribuido (403 y conexión rechazada); Ward et al. (1995), PDF con 403; handbook de GitLab "Making Decisions" (la página no devolvió el contenido); Chiang et al., "LLM-Powered Devil's Advocate" (IUI 2024); páginas de S3 y Sociocracy for All (404 y 403); y la cifra de "25 % más de éxito con DACI" que Atlassian atribuye a McKinsey sin referencia.
