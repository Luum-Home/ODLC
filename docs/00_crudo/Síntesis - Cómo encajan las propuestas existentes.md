---
tags: [crudo, investigacion, objeciones, sintesis]
status: crudo
created: 2026-10-08
---

# Síntesis: cómo encajan las propuestas existentes

Pregunta: ¿las soluciones a las seis objeciones de "Objeciones al marco" (docs/06_fundacional) ya existen, dispersas, y alcanza con juntarlas para que encajen? Es la hipótesis del dueño del vault y acá se evalúa, no se da por cierta. Insumos: los tres relevamientos de "Propuestas existentes" (objeciones 1 y 2, 3 y 4, 5 y 6) y, como contexto, las investigaciones sobre selección de modelos y sobre estimación con agentes, todos en docs/00_crudo. Este documento no agrega mecanismos nuevos: solo cruza propuestas que ya tienen autor y fuente. Las búsquedas de integraciones previas se hicieron el 2026-10-08.

Convención de evidencia (unifica las tres de los relevamientos): **[medido]** = estudio con comparación o metaanálisis; **[medido, otro dominio]** = medido, pero fuera del software o de la organización humano-agente; **[guía]** = marco o recomendación de un organismo o autor, sin evaluación de resultados; **[testimonio]** = relato de quien lo aplicó o encuesta de percepción; **[teoría]** = modelo formal o conceptual. Las referencias del tipo "1.4" o "5.9" remiten a la numeración de cada relevamiento.

## Resumen

1. La hipótesis se sostiene a medias. Las piezas existen y varias atacan más de una objeción, pero el encaje exige elegir en tres conflictos, y quedan al menos seis huecos que ningún relevamiento resolvió.
2. "Nadie las juntó" es falso en parte. Hay integraciones parciales: BOSSA nova (Beyond Budgeting + Sociocracia + Open Space + Agile, 2020), EBM + OKR (Scrum.org), IMDA v1.5 (autonomía graduada + auditoría de la supervisión), una guía de 2026 contra la sobreconfianza que combina tasa de anulación, controles con errores conocidos y fricción, y un marco teórico de organizaciones de software humano-agente (Wang y Liu, 2026). Ninguna cubre las seis objeciones.
3. Las propuestas que atacan más objeciones a la vez son Beyond Budgeting (1, 5 y 6), IMDA (3, 4, 5 y 6), la responsabilidad sobre el proceso de Mosier y Skitka (1, 5 y 6) y la formalización de roles de Lee y Edmondson (5 y 6).
4. Hay una convergencia que ningún relevamiento vio por separado: Deming ("¿con qué método?"), Mosier (responsabilidad por la verificación, no por el resultado) y Equinor (el "qué" y el "cómo" pesan mitad y mitad) piden lo mismo: juzgar el método y no el número.
5. El conflicto más serio es interno a ODLC: los principios 3 y 4 de la Objeción 5 miden a cada humano, y la respuesta a Deming (Objeción 1) y la teoría de la autodeterminación piden no evaluar personas contra números. Hay que elegir medir la etapa de revisión o medir a la persona.
6. El segundo conflicto es niveles de autonomía (Knight, IMDA, CSA y el propio Modelo de madurez) contra la crítica del Defense Science Board y Bradshaw. No hay comparación empírica entre ambos enfoques.
7. El tercero es autogestión contra aprobación. Solo se resuelve redefiniendo "autogestión" como dominios con restricciones escritas (Sociocracy 3.0, Holacracy), no como advice process.
8. Se arman tres combinaciones mínimas coherentes: A, "medir para aprender"; B, "jerarquía con autonomía graduada"; y C, "interdependencia sin metas". Las tres comparten el mismo núcleo para la Objeción 3: registered report, kill criteria, TAR/FEDS y comparar contra el mejor componente solo.
9. La combinación A es la más compatible con el diagnóstico del marco. Su pieza más débil es inyectar fallas en la revisión de código, que extrapola desde rayos X de aeropuerto y un laboratorio de N = 24 donde no bajaron los errores de comisión.
10. Casi todas las piezas que sostienen las combinaciones son guía o testimonio; lo medido viene de aviación, medicina, ahorro previsional o tareas de un día. Juntar piezas no valida el conjunto: la Objeción 3 sigue abierta con cualquier combinación.
11. Huecos sin propuesta: feedback con poco tráfico, debrief sin convocante, evidencia organizacional humano-agente de software, intervenciones que funcionen para quien no disfruta pensar, gaming de métricas por agentes y separar la espera de evidencia del tiempo de trabajo.
12. Lo más cercano a evidencia organizacional en software es He y otros (2026, una empresa, 802 desarrolladores, 28 meses), que no separa modelo organizacional de proceso, y dos estudios cualitativos de 2026 (Dhanorkar y otros; Qadri y otros).

---

## 1. Matriz propuesta × objeción

Objeciones: **O1** Deming y el gaming de metas; **O2** feedback lento; **O3** ningún caso medido; **O4** lo nuevo (humano-agente) sin evidencia; **O5** humano de mínimo esfuerzo; **O6** autogestión sin definir.

Celdas: **P** = la objeción para la que la propuesta se relevó; **C** = ataque cruzado detectado en esta síntesis (la propuesta viene de otro relevamiento); **T** = la propuesta tensiona o empeora esa objeción. Vacío = sin relación relevante. La última columna resume la evidencia con la que cuenta la propuesta.

| Propuesta (origen) | O1 | O2 | O3 | O4 | O5 | O6 | Evidencia |
|---|---|---|---|---|---|---|---|
| 1.1 OKR separados de la compensación | P | | | | | T | [testimonio]; correlacional en Butler y otros 2024 |
| 1.2 Indicadores pareados (Grove) | P | C | | | C | | [guía] |
| 1.3 Balanced Scorecard | P | | | | | | [medido, limitado] simulación de Strohhecker |
| 1.4 / 6.6 Beyond Budgeting (Equinor) | P | | | | C | P | [testimonio]; adopción baja medida (Hudson 2012) |
| 1.5 Incentivos de baja potencia (Holmström y Milgrom) | P | | | | C | | [teoría] |
| 1.6 Deming y Joiner: mejorar el sistema | P | | | | T | C | [testimonio] Alcoa |
| 1.7 Ordóñez y otros: dosis de metas | P | | | | C | C | [opinión con casos] |
| 1.8 / 3.9 EBM de Scrum.org | C | P | | T | | | [testimonio] del proveedor |
| 3.9 EBM de CEBMa (Barends y Rousseau) | | | P | | | | [guía] |
| 2.1 4DX: medidas adelantadas | T | P | | | | | [testimonio] del vendedor |
| 2.2 Resultados de producto (Torres) | C | P | | | | | [opinión] |
| 2.3 North Star | T | P | | | | | [opinión] |
| 2.4 Contabilidad de la innovación | | P | C | | | | [opinión] |
| 2.5 Experimentos con OEC | C | P | C | | | | [medido] Google, Bing |
| 2.6 Historia de los surrogates médicos | C | P | | | | | [medido, otro dominio] |
| 2.7 Surrogate index | | P | | | | | [medido, otro dominio] |
| 2.8 Proxies aprendidos (Chou; Sigerson) | | P | | | | | [medido] plataformas con tráfico |
| 2.9 CUPED | | P | C | | | | [medido] Bing |
| 2.10 Tests secuenciales | | P | C | | | | [medido] despliegue y simulación |
| 2.11 Usuarios simulados con LLM | | P | | C | | | [medido], en contra como reemplazo |
| 3.1 DORA / Accelerate | | | P | | | | [medido, correlacional, autoinforme] |
| 3.2-3.4 DSR, FEDS, TAR | | | P | C | | | [guía] metodológica |
| 3.5 Runeson y Höst; Wohlin | | | P | | | | [guía] metodológica |
| 3.6 EBSE y la lección del agilismo | | | P | | | | [medido] estado de la evidencia ágil |
| 3.7 Registered reports | C | | P | | | | [medido, otro dominio] Scheel y otros 2021 |
| 3.8 Kill criteria (Duke) | C | C | P | | | | [testimonio] |
| 3.10 RCT de METR | | | P | P | C | | [medido] |
| 4.1-4.3 Human-autonomy teaming (NASA, NAS, revisión) | | | | P | C | | [medido, otro dominio] laboratorio |
| 4.4 Niveles de automatización (Parasuraman 2000) | | | | P | C | C | [teoría] |
| 4.5 DSB 2012 y Bradshaw 2013 contra los niveles | | | | P | T | C | [guía] opinión experta |
| 4.6 Coactive design | | | | P | C | C | [testimonio] DARPA VRC |
| 4.7 / 6.7 Autonomía graduada (Knight, IMDA, CSA) | | | C | P | C | P | [guía]; CSA con análisis retrospectivo propio |
| 4.8 / 5.9 IMDA: auditar la supervisión | | | C | P | P | C | [guía] |
| 4.9 OWASP Agentic Top 10 (ASI09) | | | | P | C | | [guía] |
| 4.10 Frontera irregular (BCG) | | | | P | C | | [medido] tareas de un día |
| 4.11 Cybernetic Teammate (P&G) | | | C | P | | | [medido] pre-registrado, un día |
| 4.12 Metaanálisis humano + IA (Vaccaro y otros) | | | C | P | | | [medido] |
| 4.13 Team Topologies | | | | P | | C | [testimonio]; 11 hipótesis testeadas en Alves y otros |
| 4.14 Microsoft WTI: human-agent ratio | | | | P | | | [testimonio] del proveedor |
| 5.1 Autodeterminación (Deci y Ryan) | C | | | | P | C | [medido] correlacional y de laboratorio |
| 5.2 Defaults | | | | | P | | [medido]; efecto chico a escala |
| 5.3 Elección activa obligatoria | C | | | | P | | [medido, otro dominio] ahorro |
| 5.4 Poka-yoke y pit of success | | | | | P | | [testimonio] |
| 5.5 Modelo de Fogg | | | | | P | | [opinión] |
| 5.6 Forzado cognitivo (Buçinca) | | | | | P | | [medido] N = 199 |
| 5.7 Responsabilidad percibida (Mosier, Skitka) | C | | | | P | C | [medido, otro dominio] aviación |
| 5.8 Exposición a fallas (Bahner) | | | C | C | P | | [medido, otro dominio] N = 24 |
| 5.10 Checklists: piloto y mandato | C | | C | | P | | [medido, otro dominio] |
| 5.11 Debriefs (Tannenbaum y Cerasoli) | | C | | | P | C | [medido] metaanálisis |
| 5.12 Monitorear e intervenir (Anthropic) | | | | C | P | C | [medido] datos del proveedor |
| 6.1 Holacracy | | | | | C | P | [medido, transversal] Weirauch y otros |
| 6.2 Sociocracy 3.0 | | C | C | | | P | [guía] |
| 6.3 Advice process | | | | | T | P | [testimonio] |
| 6.4 Freeman: tiranía de la falta de estructura | | | | | | P | [testimonio] |
| 6.5 Roles formalizados (Lee y Edmondson) | | | | | C | P | [medido] experimento de campo |
| 6.8 Foss y Klein: jerarquía que funcione | | | | | | P | [opinión] |
| 6.9 Zappos, Medium, Buurtzorg | C | | C | | | P | [testimonio]; costo medido de segunda mano |
| He y otros 2026, mandato "2x" (contexto) | | | C | C | C | | [medido] longitudinal, una empresa |
| Jueces cruzados y techo humano (contexto: Shopify, Gorbett y Jana) | | | C | C | C | | [medido] |
| Pronóstico por flujo (Vacanti, Magennis; contexto) | | C | | | | | [guía]; sin caso con agentes |
| Hut y Masoero: A/B simulado (contexto) | | C | | | | | [medido] 67 A/B históricos |

### Qué justifica las celdas C menos obvias

- **1.2 en O5.** Los principios 3 y 4 de la Objeción 5 forman un par de Grove: la tasa de aprobación es el indicador y la tasa de fallas sembradas detectadas es el contraindicador que impide leer una aprobación del 100 % como éxito. La nota de IMDA (5.9) dice lo mismo sin nombrar a Grove.
- **1.4 / 6.6 en O5.** Desacoplar la medición de la recompensa contingente es, según el propio relevamiento de 5 y 6, compatible con la teoría de la autodeterminación (5.1). No vuelve proactivo a nadie, pero evita una de las causas medidas de la pérdida de motivación intrínseca (d = −0,28 a −0,40 por recompensa contingente, Deci y otros 1999).
- **1.5 en O5.** El modelo multitarea predice que, si se paga por lo medible, el esfuerzo sale de lo no medible. En ODLC, validar es la tarea difícil de medir. [teoría]
- **1.6 y 1.7 en O6.** Deming y Ordóñez coinciden con la desconfianza Teal hacia las metas que la Objeción 6 señala, y así le dan un fundamento a "sentir y responder" que Laloux, según el vault, no tiene.
- **2.5, 2.9 y 2.10 en O3.** Las mismas técnicas que acortan el feedback de producto sirven para medir el piloto de ODLC: la parada secuencial es la versión estadística de un kill criterion. Requieren volumen, que un piloto chico no tiene.
- **3.7 y 3.8 en O1.** Pre-registrar la métrica y el criterio de abandono impide que quien diseña el marco mueva el arco después de ver el resultado. Es Goodhart aplicado al propio autor.
- **3.10 en O5.** Los desarrolladores de METR creyeron haber ganado 20 % cuando perdieron 19 %. El humano no es un juez fiable de su propio desempeño con IA, lo que refuerza medir actos y no percepciones.
- **4.6 en O5.** Las tres propiedades de coactive design (observabilidad, predictibilidad y dirigibilidad) son la versión de diseño del principio 6 ("hacer visible").
- **5.7 en O1 y O6.** La responsabilidad sobre el proceso de verificación es la pregunta de Deming ("¿con qué método?") en otro dominio, y la sanción por no consultar del advice process (6.3) es responsabilidad ante otros.
- **5.8 en O3 y O4.** Las fallas sembradas producen un dato con respuesta conocida, uno de los pocos instrumentables desde el primer día de un piloto humano-agente. [extrapolación: viene de rayos X de aeropuerto y control de procesos]
- **5.10 en O1 y O3.** La checklist tildada sin cambiar la práctica es Goodhart sobre una compuerta. Además, el salto del piloto de la OMS (mortalidad del 1,5 % al 0,8 %) al mandato de Ontario (0,71 % contra 0,65 %, p = 0,13) advierte que un piloto exitoso de ODLC no garantiza el resultado bajo adopción obligatoria.
- **5.11 en O2.** El debrief produce aprendizaje sobre el proceso sin esperar el outcome de mercado. [extrapolación: el metaanálisis mide desempeño en la tarea, no aprendizaje sobre objetivos de negocio]
- **6.2 en O2 y O3.** "Suficientemente seguro para probar" con fecha de revisión es estructuralmente un kill criterion (estado + fecha) aplicado a acuerdos organizacionales.
- **He y otros (2026).** Muestra, en una organización real de software, que la cola de revisión humana se alivió porque los PR empezaron a saltear la revisión humana, con merge y revert estables. Es dato para O4 (cómo se reorganiza el trabajo) y para O5 (el humano esquiva la compuerta en lugar de tildarla).

### Propuestas que atacan varias objeciones a la vez

| Propuesta | Objeciones | Qué la vuelve transversal | Evidencia |
|---|---|---|---|
| IMDA v1.5 (4.8 / 5.9 / 6.7) | O3, O4, O5, O6 | Aprobación por tipo de acción, medición de la supervisión y denegación por defecto; sus indicadores se pueden pre-registrar | [guía] |
| Beyond Budgeting (1.4 / 6.6) | O1, O5, O6 | Separa meta, pronóstico y asignación; evaluación integral; desacopla medición y recompensa | [testimonio] |
| Responsabilidad sobre el proceso (5.7) | O1, O5, O6 | Juzgar el método de verificación y no el resultado | [medido, otro dominio] |
| Roles formalizados (6.5) | O5, O6 | Mide que la autogestión solo beneficia a quien ya es proactivo | [medido] un experimento de campo |
| Kill criteria y registered reports (3.7, 3.8) | O1, O2, O3 | Fijan antes la métrica, la fecha y la decisión | [testimonio] y [medido, otro dominio] |
| Fallas sembradas (5.8) | O3, O4, O5 | Dan una verdad conocida contra la cual medir la supervisión | [medido, otro dominio] |
| Coactive design (4.6) | O4, O5, O6 | Observabilidad y dirigibilidad en lugar de niveles | [testimonio] |
| Checklists, piloto contra mandato (5.10) | O1, O3, O5 | Compuerta de forma = Goodhart; el piloto no predice la escala | [medido, otro dominio] |

---

## 2. Conflictos entre relevamientos

Cada relevamiento listó contradicciones dentro de sus dos objeciones. Estos son los pares de relevamientos distintos que chocan, o choques internos que solo aparecen al juntar las respuestas a objeciones distintas.

### 2.1 La métrica en el centro contra quienes desconfían de las metas

- **Lados.** OKR (1.1), 4DX (2.1), North Star (2.3) y EBM de Scrum.org (1.8), relevados para O1 y O2, contra Deming y Joiner (1.6), Beyond Budgeting (6.6, relevado para O6), la teoría de la autodeterminación (5.1, relevada para O5) y la desconfianza Teal hacia las metas que plantea la Objeción 6.
- **Qué tendría que elegir el marco.** Si la métrica del objetivo funciona como meta de desempeño o como instrumento de aprendizaje.
- **Opción "meta".** Mantiene la tradición de OKR y 4DX y la promesa de foco. Deja abierta la objeción de Deming, convierte al Nivel 5 "autogestionado" en vocabulario sin contenido y expone a la medida adelantada controlable por el equipo (o por el agente) a ser la más fácil de inflar.
- **Opción "aprendizaje".** Es la salida que el propio vault ya insinúa ("medir para aprender, no para controlar"). Se apoya en Equinor (separar meta, pronóstico y asignación) y en Holmström y Milgrom (no pagar por lo medible). Implica renunciar a las metas estiradas de los OKR como compromiso y aceptar que la evidencia de esta salida es testimonial, con adopción completa baja (Hudson 2012) y un fracaso documentado (Valuckas 2016).

### 2.2 Medir a cada humano contra no evaluar personas con números

- **Lados.** Los principios 3 y 4 de la Objeción 5 (IMDA 5.9: supervisores atípicos, tiempo de respuesta; Threat Image Projection: desempeño individual del operador; Bahner 5.8) contra Deming 12b (abolir la calificación por mérito, relevado para O1), la teoría de la autodeterminación (5.1: la vigilancia es motivación controlada) y Beyond Budgeting (evaluación no basada solo en medición).
- **Por qué es el conflicto más serio.** Es interno a ODLC: la respuesta candidata a la Objeción 1 dice "la métrica no se usa para evaluar personas", y el principio 4 dice "si no atrapa ninguna falla, su aprobación vale cero", que es una evaluación individual con un número.
- **Opción "medir la etapa".** La tasa de detección se agrega por etapa de revisión o por tipo de cambio y se usa para calibrar cuánto vale una aprobación, no para calificar a nadie. Es compatible con Deming (mejorar el sistema), con Holmström y Milgrom y con Mosier (responsabilidad por el proceso). Pierde la capacidad de detectar al supervisor individual que aprueba todo, que es justamente el humano de mínimo esfuerzo.
- **Opción "medir a la persona".** Detecta al aprobador automático, como pretenden IMDA y Threat Image Projection. Choca con Deming y con la teoría de la autodeterminación, y en una organización que se declara autogestionada se lee como vigilancia. Si se elige, la respuesta a la Objeción 1 tiene que acotarse a "la métrica del objetivo no evalúa personas" y declarar que la métrica de supervisión sí lo hace.
- **Lo que nadie midió.** Si medir la supervisión individual, sin ligarla a compensación, deteriora la motivación en un entorno de trabajo real. La predicción de la teoría de la autodeterminación viene de laboratorio con tareas interesantes.

### 2.3 Aprobar cada acción contra monitorear e intervenir

- **Lados.** Elección activa (5.3), forzado cognitivo (5.6) y justificación escrita de IMDA, contra Anthropic (5.12), coactive design (4.6, relevado para O4) y el dato de He y otros (2026, investigación de estimación), donde los humanos saltean la revisión cuando la cola crece. La escasez medida de atención para revisar (Faros: +91 % de tiempo de revisión; LinearB: PR de agentes que esperan entre 4,6 y 5,3 veces más) empuja hacia el monitoreo.
- **Qué tendría que elegir el marco.** Dónde poner la fricción.
- **Opción "fricción en todo acto de validación"** (principio 2 tal como está escrito). Es la que más reduce la sobreconfianza en laboratorio, pero es la peor valorada, la que menos sirve a quien no disfruta pensar (Buçinca y otros) y la que el humano esquiva cuando la carga sube (He y otros).
- **Opción "fricción concentrada"** (IMDA: alto impacto, irreversible, conducta atípica; el resto, monitoreo con intervención simple). Es la reconciliación que ya propone IMDA. Deja sin forzado cognitivo la mayoría de las validaciones, que pasan a depender de las métricas de pasividad y de las fallas sembradas. La evidencia del monitoreo es del proveedor, sobre usuarios que eligen usar la herramienta, no sobre humanos pasivos.

### 2.4 Niveles de autonomía contra interdependencia

- **Lados.** Knight (4.7), IMDA y CSA (6.7, presentados por el relevamiento de 5 y 6 como la forma publicada de reconciliar autonomía y aprobaciones), el principio 5 y el Modelo de madurez del vault, contra el Defense Science Board (2012), Bradshaw y otros (2013) y coactive design (4.5, 4.6, relevados para O4).
- **Qué tendría que elegir el marco.** Si el Modelo de madurez y la matriz de Gobernanza se expresan como niveles o como análisis de interdependencias por tarea.
- **Opción "niveles por tipo de acción".** Es operable, la usan los marcos de 2025-2026 y trae criterios de promoción y degradación (CSA). IMDA asigna el nivel por acción y no por organización, lo que atenúa en parte la crítica de "autonomía unidimensional". Hereda la crítica completa del DSB para un modelo de madurez de cinco niveles organizacionales.
- **Opción "interdependencia".** Responde a la crítica del DSB y es coherente con Team Topologies (modos de interacción). Es costosa, viene de robótica y tampoco tiene comparación controlada contra los niveles.
- **Lo que nadie midió.** Ninguna fuente compara resultados entre ambos enfoques (pregunta abierta 3 del relevamiento de 3 y 4). Elegir es una decisión de diseño, no una conclusión de la evidencia.

### 2.5 Autogestión contra matriz de aprobaciones

- **Lados.** Advice process (6.3) y el vocabulario Teal del Nivel 5, contra la matriz de aprobaciones por rol del vault, la aprobación humana obligatoria para lo irreversible (IMDA, Reglamento de IA de la UE, relevados para O4 y O5), los criterios de promoción de CSA, que dependen de una "autoridad superior", y Foss y Klein (6.8).
- **Un agravante que viene de O5.** Bakke admite que el advice process no acomoda a quien no actúa como colega responsable, y Lee midió que la descentralización radical no mejora la experiencia del empleado promedio. La autogestión pura y el diseño para el humano de mínimo esfuerzo se contradicen.
- **Opción "autogestión con reglas escritas".** Dominios con restricciones y consentimiento (Sociocracy 3.0), roles formalizados y revisables (Lee, Freeman, Holacracy), y aprobación humana por tipo de acción solo en lo irreversible. Es coherente con todo lo relevado, pero "autogestionada" pasa a significar "autoridad delegada por reglas explícitas", no Teal en el sentido de Laloux.
- **Opción "jerarquía bien diseñada".** Foss y Klein más autonomía graduada. Es coherente y elimina la tensión, pero disuelve la Objeción 6 en lugar de contestarla: el Nivel 5 deja de hablar de autogestión.

### 2.6 Protocolo fijo contra adaptar sobre la marcha

- **Lados.** Registered reports y kill criteria (3.7, 3.8: fijar hipótesis, análisis y decisión antes de los datos) contra "evaluar y evolucionar" de Sociocracy 3.0, "sentir y responder" de Beyond Budgeting y el ciclo de inspección y adaptación de EBM.
- **Magnitud.** Menor de lo que parece. Los registered reports admiten desvíos declarados y justificados en la Etapa 2, y Sociocracy 3.0 fija fechas de revisión. La elección real es qué se congela (la tesis central y el criterio de abandono del piloto) y qué se adapta (la operación diaria). Ninguna fuente lo resuelve explícitamente para un marco que se evalúa mientras se usa.

### 2.7 Indicadores adelantados con un validador pasivo (interacción, no contradicción)

- **Lados.** Medidas adelantadas controlables (4DX, Torres), relevadas para O2, y el humano de mínimo esfuerzo de O5.
- **Por qué importa.** Cada propuesta, sola, es razonable. Juntas forman el escenario más frágil: un indicador adelantado que el equipo, o el agente, puede mover, validado por alguien que aprueba en segundos. Ninguna fuente de O2 trae defensa contra el gaming (relevamiento de 1 y 2) y ninguna fuente aborda el gaming de métricas por agentes (pregunta abierta 2 del mismo relevamiento). Cualquier combinación que use indicadores adelantados necesita las piezas de O1 y de O5 en la misma compuerta.

---

## 3. Combinaciones coherentes

Las tres comparten un **núcleo para la Objeción 3**, porque las propuestas metodológicas no chocan con ninguna de contenido:

- Diseño: DSR con evaluación según FEDS (artificial y luego naturalista) y TAR para el piloto real (3.2-3.4). [guía]
- Contra el autoengaño: registered report de la tesis central y kill criteria con estado y fecha (3.7, 3.8). [medido, otro dominio] y [testimonio]
- Comparador: el mejor componente solo, no solo el humano solo (Vaccaro y otros, 4.12). [medido]
- Fuente de datos: actos y eventos registrados, no autoinforme (lección de METR, 3.10). [medido]
- Advertencia de escala: un piloto exitoso no predice el resultado bajo mandato (checklists, 5.10). [medido, otro dominio]

Este núcleo no produce evidencia: solo ordena cómo juntarla. Con cualquier combinación, la Objeción 3 queda abierta hasta que corra un piloto.

### Combinación A: "medir para aprender"

| Objeción | Piezas | Evidencia |
|---|---|---|
| O1 | Separar meta, pronóstico y asignación, con evaluación integral (Beyond Budgeting, 6.6); no pagar por la métrica (Holmström y Milgrom, 1.5); indicadores pareados (1.2) | [testimonio], [teoría], [guía] |
| O2 | Resultados de producto como metas intermedias (Torres 2.2, EBM 1.8); con tráfico, CUPED y tests secuenciales (2.9, 2.10); sin tráfico, A/B simulado solo como filtro (Hut y Masoero) | [opinión]; [medido] con tráfico |
| O3 | Núcleo común | ver arriba |
| O4 | Separar estructura (Team Topologies, 4.13) de proceso; diseño factorial pre-registrado como plantilla (P&G, 4.11) | [testimonio]; [medido] un día |
| O5 | Fricción concentrada en puntos significativos (IMDA); métricas de pasividad pareadas con fallas sembradas **agregadas por etapa** (5.8, 5.9); responsabilidad sobre el proceso (Mosier, 5.7); debrief estructurado (5.11) | [guía]; [medido, otro dominio]; [medido] |
| O6 | Dominios con restricciones y consentimiento (Sociocracy 3.0, 6.2); roles formalizados y revisables (Lee 6.5, Freeman 6.4); aprobación humana solo en lo irreversible (6.7) | [guía]; [medido] un experimento |

- **Por qué no se contradice.** Resuelve el conflicto 2.1 por "aprendizaje", el 2.2 por "medir la etapa", el 2.3 por "fricción concentrada" y el 2.5 por "reglas escritas". La convergencia Deming-Mosier-Equinor (juzgar el método) atraviesa O1, O5 y O6.
- **Qué deja abierto.** El conflicto 2.4 (usa aprobación por tipo de acción, sin responder a la crítica del DSB contra el Modelo de madurez); el aprobador individual que aprueba todo, que la medición por etapa no identifica; O2 sin tráfico; el debrief sin convocante.
- **Pieza más débil.** Las fallas sembradas en la revisión de código. [extrapolación] La evidencia viene de rayos X de aeropuerto y de un laboratorio de control de procesos con N = 24 donde no bajaron los errores de comisión, que son los relevantes para aprobar un cambio de un agente. Es la pieza que sostiene la interpretación de todas las métricas de pasividad.

### Combinación B: "jerarquía con autonomía graduada"

| Objeción | Piezas | Evidencia |
|---|---|---|
| O1 | OKR separados de la compensación (1.1) más indicadores pareados (1.2) y Holmström y Milgrom (1.5) | [testimonio], [guía], [teoría] |
| O2 | Medidas adelantadas (4DX 2.1 o North Star 2.3) validadas con surrogate index o proxies aprendidos (2.7, 2.8) | [testimonio]; [medido] con historial de experimentos |
| O3 | Núcleo común | ver arriba |
| O4 | Niveles por tipo de acción (Knight 4.7, IMDA 4.8) y riesgos de OWASP (4.9) | [guía] |
| O5 | Elección activa obligatoria (5.3), auditoría individual de la supervisión (5.9) y fallas sembradas por persona (5.8) | [medido, otro dominio]; [guía] |
| O6 | Jerarquía que decide qué delegar (Foss y Klein, 6.8) con promoción y degradación de autonomía (CSA, 6.7) | [opinión]; [guía] |

- **Por qué no se contradice.** Sin promesa de autogestión, medir a cada supervisor no choca con nada declarado, y la delegación graduada la decide una autoridad, como piden Foss y Klein y CSA.
- **Qué deja abierto.** Deming queda parcialmente sin contestar: los OKR mantienen metas numéricas y estiradas (Ordóñez y otros); la crítica del DSB a los niveles queda entera; la Objeción 6 se disuelve en lugar de contestarse (el Nivel 5 deja de ser autogestión); O2 exige un historial de experimentos largos que una organización chica no tiene.
- **Pieza más débil.** Los niveles de autonomía. Ningún marco de autonomía graduada tiene validación comparativa, y CSA valida sus niveles con un análisis retrospectivo de diez incidentes hecho por el propio autor del marco.

### Combinación C: "interdependencia sin metas"

| Objeción | Piezas | Evidencia |
|---|---|---|
| O1 | Eliminar la meta numérica y preguntar "¿con qué método?" (Deming y Joiner, 1.6) | [testimonio] |
| O2 | Pruebas de supuestos antes de construir (Torres, 2.2) y debriefs (5.11) | [opinión]; [medido] |
| O3 | Núcleo común | ver arriba |
| O4 | Coactive design (4.6) con modos de interacción de Team Topologies (4.13) | [testimonio] |
| O5 | Monitorear e intervenir (5.12) con observabilidad y dirigibilidad; responsabilidad sobre el proceso (5.7) | [medido] del proveedor; [medido, otro dominio] |
| O6 | Dominios con restricciones (6.2) y roles formalizados (6.5) | [guía]; [medido] |

- **Por qué no se contradice.** Sin metas numéricas no hay gaming de metas ni medición individual que choque con la autodeterminación, y la interdependencia reemplaza los niveles.
- **Qué deja abierto.** Contesta la Objeción 1 abandonando el centro del marco: "objetivo con métrica, validado contra el outcome" deja de ser la unidad del ciclo, y con eso se cae el diagnóstico que el vault considera su fortaleza. Deja sin compuerta al humano pasivo: la evidencia del monitoreo es de usuarios que eligen la herramienta.
- **Pieza más débil.** Coactive design aplicado a una organización de software. [extrapolación] Viene de robótica (DARPA VRC), su análisis de interdependencias es costoso y no tiene comparación controlada.

### Lectura de las tres

La combinación A es la única que conserva el diagnóstico del marco (el objetivo con métrica como unidad) y además contesta las seis objeciones sin disolver ninguna. B es más simple de operar, pero deja a Deming y al DSB abiertos y renuncia a la autogestión. C es la más coherente con Deming y Teal, pero deja de ser ODLC. En las tres, la mayoría de las piezas son guía o testimonio, y las piezas medidas provienen de otro dominio.

---

## 4. Integraciones previas encontradas

Búsquedas del 2026-10-08: "agentic organization" de McKinsey; Beyond Budgeting combinado con sociocracia u Holacracy; EBM combinado con OKR; coactive design aplicado a agentes LLM; el ciclo de vida AI-DLC de AWS; marcos que combinen contramedidas al sesgo de automatización con diseño organizacional; estudios de campo de organizaciones de software humano-agente.

| Integración | Qué combina | Objeciones que cubre | Qué no cubre | Evidencia |
|---|---|---|---|---|
| Jutta Eckstein y John Buck, *Company-wide Agility with Beyond Budgeting, Open Space & Sociocracy* (BOSSA nova), 2.ª ed. 2020 | Beyond Budgeting, Open Space, Sociocracia y Agile | O1 en parte (Beyond Budgeting), O6 | Agentes, supervisión, O2, O3, O5 | [testimonio] casos de practicantes, según la página del libro |
| Scrum.org, EBM + OKR ("Using OKRs with Scrum and Evidence Based Management", 2021-08-31; webinar de Yuval Yeret, 2025-09-03) | Metas en tres niveles de EBM con OKR | O1 en parte, O2 | Deming, agentes, O5, O6 | Visto solo en resultados de búsqueda; las páginas no cargaron. No se usa como dato |
| IMDA, *Model AI Governance Framework for Agentic AI* v1.5 (2026) | Autonomía graduada de Knight, puntos significativos de aprobación, auditoría de la supervisión, denegación por defecto | O4, O5, O6 en parte | Métricas de objetivo (O1, O2), evidencia propia (O3) | [guía] |
| ThinkTech Research, "Overreliance on AI" (2026-04-13) | Seguimiento de la tasa de anulación, controles por muestreo con errores conocidos, ejercicios "IA apagada", evaluación humana previa a ver la recomendación | O5 (principios 2, 3 y 4 juntos) | O1, O2, O4, O6; no es un marco organizacional | [guía]; cita a NIST, Parasuraman y Manzey, FAA 2013, Goddard y otros 2012, art. 14 de la UE |
| Zhongjie Wang y Mingyi Liu, "Software Engineering in the Agent Era: From Trustworthy Change to Human-Agent Software Organizations", arXiv 2609.04630 (2026-09-04) | Cambio confiable (de la intención a la operación), topología de responsabilidad, "celda humano-agente" sin autoridad de aceptación | O4, O6 en parte (quién acepta el riesgo) | O1, O2, O5; los autores declaran que sus constructos son hipótesis a probar | [teoría] |
| McKinsey, "The agentic organization: Contours of the next paradigm for the AI era" (Sukharevsky, Krivkovich, Gast y otros, según fragmentos de búsqueda) | Cinco pilares: modelo de negocio, modelo operativo, gobernanza, personas y cultura, tecnología y datos; "equipos agénticos" chatos orientados a resultados; control embebido en tiempo real | O4 y O6 como declaración | Medición, gaming, sesgo de automatización, validación | La página no cargó (timeout). Contenido tomado de fragmentos de búsqueda y de un resumen secundario (headquarter.ai), que no encuentra datos que lo respalden. Fecha no verificada |
| AWS, "AI-Driven Development Life Cycle" (Raja SP, 2025-07-31) | Fases Inception, Construction y Operations; "bolts" en lugar de sprints; el agente planifica y pregunta, el humano valida antes de avanzar | O4 como proceso | O1, O2, O3, O5 (supone validación humana efectiva), O6 | [guía] del proveedor, sin mediciones |

**Veredicto de la búsqueda.** Existen integraciones de dos o tres piezas, siempre dentro de una misma familia: gestión sin presupuesto con autogestión (BOSSA nova), gestión por evidencia con metas (EBM + OKR), gobernanza de agentes con supervisión (IMDA, ThinkTech), u organización humano-agente de software en teoría (Wang y Liu). No se encontró ninguna que cruce las familias de O1 y O2 (medición) con las de O5 (supervisión) y O6 (autogestión), y ninguna que traiga evidencia medida del conjunto. La parte "nadie las juntó" de la hipótesis vale para la integración completa, no para las parciales.

**Evidencia empírica cercana que apareció en la búsqueda** (no son integraciones, pero achican el hueco de O4):

- Dhanorkar, Passi y Vorvoreanu, arXiv 2606.05391 (2026-06-03): entrevistas a 17 desarrolladores experimentados que supervisan agentes de software. Encuentran supervisión preventiva (planificar con el agente), en tiempo real y posterior, y que se usan validaciones poco confiables, como tomar los tests que pasan como garantía de corrección. [medido, cualitativo]
- Qadri y otros, arXiv 2609.29901 (2026-09-24): estudio cualitativo *in situ* de un agente persistente y proactivo desplegado en varios equipos de una empresa grande de tecnología. Reporta rupturas de normas tácitas de trabajo, de límites relacionales y de confianza. [medido, cualitativo; el resumen no da el tamaño de la muestra]

---

## 5. Huecos sin propuesta

| Hueco | Objeción | Lo más cercano que existe | Por qué no alcanza |
|---|---|---|---|
| Feedback con poco tráfico o pocos experimentos históricos | O2 | A/B simulado (Hut y Masoero: acierta el signo en 70 %); Agent A/B; pronóstico por flujo (Vacanti, Magennis) | Los simuladores sirven para filtrar, no para validar; no hay caso de pronóstico por flujo con agentes; CUPED, surrogate index y proxies suponen volumen |
| Separar la espera de evidencia del tiempo de trabajo | O2 | Holdbacks largos que corren en paralelo (Hohnhold y otros) | Ningún estudio descompone el tiempo hasta el resultado entre especificar, ejecutar, revisar, integrar y esperar |
| Debrief que ocurra sin que nadie lo convoque | O5 | Debriefs (d = 0,67), "evaluar y evolucionar" de Sociocracy 3.0, revisión fechada | Todos suponen a alguien que lo conduce; ninguna fuente prueba un disparador automático |
| Intervención que funcione para quien no disfruta pensar | O5 | Defaults (sin pensar) y forzado cognitivo (el que más rechaza ese perfil) | Buçinca y Lee coinciden: lo que funciona beneficia a quien ya piensa o ya es proactivo |
| Contramedidas al sesgo de automatización en revisión de código de agentes | O5, O4 | Mosier, Bahner, Threat Image Projection; Dhanorkar y otros 2026 (cualitativo) | Toda la evidencia medida es de aviación, control de procesos y aeropuertos [extrapolación] |
| Umbrales de las métricas de pasividad | O5 | Tasa de rechazo y tiempo de respuesta (IMDA) | Sin umbrales validados ni base de comparación medida |
| Organización humano-agente de software medida durante meses, separando estructura y proceso | O4 | He y otros 2026 (longitudinal, una empresa); P&G 2025 (un día); Qadri y otros 2026 (cualitativo) | Ninguno compara modelos organizacionales; He y otros mide throughput y revisión, no estructura |
| Gaming de métricas por agentes | O1 | Taxonomía de Goodhart (Manheim y Garrabrant), OWASP ASI01 (secuestro de objetivo) | La literatura de *reward hacking* no se relevó; ninguna fuente lo trata dentro de un ciclo de trabajo |
| Comparación empírica entre niveles de autonomía e interdependencia | O4, O6 | DSB y Bradshaw contra Knight, IMDA y CSA | Conviven sin comparación |
| Grupo de control reclutable cuando la práctica ya se adoptó | O3 | Alternativas de METR (aleatorizar por desarrollador, tareas fijas, datos observacionales) | No están probadas |
| Qué es "el agente solo" como comparador en un ciclo ODLC | O3, O4 | Criterio de Vaccaro y otros | El criterio existe; su operacionalización para ciclos de objetivo, no |
| Evaluación independiente de Beyond Budgeting | O1, O6 | Testimonio de Bogsnes; Hudson 2012; Valuckas 2016 | Sin evaluación con control |

---

## 6. Fuentes nuevas (consultadas el 2026-10-08)

Abiertas y usadas:

- Eckstein, J. y Buck, J., *Company-wide Agility with Beyond Budgeting, Open Space & Sociocracy*, Leanpub, 2.ª ed. 2020 (página del libro). https://leanpub.com/bossanova
- Raja SP, "AI-Driven Development Life Cycle: Reimagining Software Engineering", AWS DevOps & Developer Productivity Blog, 2025-07-31. https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle
- ThinkTech Research, "Overreliance on AI: Automation Bias, Skill Atrophy, and Organizational Controls", 2026-04-13. https://thinktech.ngo/risk-library/overreliance
- Wang, Z. y Liu, M., "Software Engineering in the Agent Era: From Trustworthy Change to Human-Agent Software Organizations", arXiv 2609.04630, 2026-09-04. https://arxiv.org/abs/2609.04630
- Dhanorkar, S., Passi, S. y Vorvoreanu, M., "Human oversight of agentic systems in practice", arXiv 2606.05391, 2026-06-03. https://arxiv.org/abs/2606.05391
- Qadri, R. y otros, "Working with Agentic 'Teammates': When a New Organizational Actor Collides with the Human Ecosystem of Work", arXiv 2609.29901, 2026-09-24. https://arxiv.org/abs/2609.29901
- headquarter.ai, "McKinsey agentic organization" (resumen secundario, sin fecha visible). https://www.headquarter.ai/en/post/mckinsey-agentic-organization

Vistas solo en resultados de búsqueda, sin abrir (no se usan como dato):

- McKinsey, "The agentic organization: Contours of the next paradigm for the AI era" (la página dio timeout tres veces; autores tomados de fragmentos de búsqueda, fecha no verificada). https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era
- Scrum.org, "Using OKRs with Scrum and Evidence Based Management" (2021-08-31, según el buscador) y "A Discussion about Evidence-Based Management, OKRs and Other Metrics" (las páginas devolvieron contenido vacío). https://www.scrum.org/node/51628 · https://www.scrum.org/node/77835
- "LLM Constitutional Multi-Agent Governance", arXiv 2603.13189 (apareció al buscar coactive design aplicado a agentes; trata gobernanza entre agentes, no interdependencia humano-agente). https://arxiv.org/abs/2603.13189

Las demás fuentes citadas están en los tres relevamientos de propuestas y en las dos investigaciones de contexto, con sus fechas de consulta.

## Comandos de verificación

Read-only. Confirman que los insumos contienen los datos que esta síntesis cruza.

```bash
cd docs/00_crudo
grep -n "Threat Image Projection" "../06_fundacional/Objeciones al marco.md"
grep -n "seguridad psicológica" "Propuestas existentes - Objeciones 5 y 6.md"
grep -n "abandonar el esfuerzo de definir niveles" "Propuestas existentes - Objeciones 3 y 4.md"
grep -n "saltear la revisión humana" "Investigación - Estimación y tiempo con agentes.md"
curl -s "https://export.arxiv.org/api/query?id_list=2609.04630,2606.05391,2609.29901" | grep -o "<title>[^<]*</title>"
```
