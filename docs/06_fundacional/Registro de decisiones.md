---
tags: [fundacional, decisiones]
status: borrador
created: 2026-10-08
---

# Registro de decisiones

Decisiones de autor sobre el marco, con fecha, motivo y estado. Una decisión se cambia agregando una entrada nueva que la supersede, no editando la anterior. El contexto de cada una está en la auditoría del vault (2026-10-07), en [[Objeciones al marco]] y en el foco en tiny teams fijado el 2026-10-08.

**Contexto general (2026-10-08):** el público del marco son las empresas que achican equipos (en transición) y los emprendedores que arrancan solos (sin historia). Mientras exista el primer grupo, la convivencia con Scrum, Kanban, niveles de madurez y aprobaciones no se puede evitar, así que varias decisiones tienen una respuesta para cada grupo.

---

## Decisiones sobre el marco (aprobadas por el dueño el 2026-10-08)

| # | Decisión | Motivo | Notas afectadas |
|---|---|---|---|
| D-01 | Una sola lista de aprobaciones humanas, por tipo de acción, en [[Gobernanza]]. "Lo irreversible frena" (pagos, datos de clientes, borrado, migraciones destructivas) no se relaja con la madurez. El Nivel 5 se redefine sobre esa base: el humano deja la ejecución táctica pero conserva lo irreversible. | Había cinco listas distintas de aprobaciones humanas y el Nivel 5 contradecía los "siempre" de la matriz. | [[Gobernanza]], [[Modelo de madurez AI-Native]], [[Manifiesto HACS-ODLC]], [[Glosario y taxonomía]], [[Módulo 3 - Gobernanza]] |
| D-02 | Adopta ODLC quien usa la ficha de objetivo con criterio de abandono y registra el resultado validado ([[Núcleo ODLC para tiny teams]]). La exigencia de Nivel 3 para pilotos queda solo para agentes que escriben en sistemas compartidos. | "Ya es ODLC" y "ya es HACS" no tenían umbral y la regla del Nivel 3 contradecía la definición del Nivel 2. | [[Manifiesto HACS-ODLC]], [[Modelo de madurez AI-Native]], [[HACS]], [[Unidad organizacional]] |
| D-03 | ODLC convive con Scrum y Kanban durante la transición. Reemplaza la unidad de trabajo solo en equipos que arrancan desde cero; en equipos existentes se adopta de a poco. | El cambio brusco del modelo organizacional inicial se asoció a más fallas ([[Investigación - Tiny teams y bootstrapping]], fuente secundaria). | [[ODLC]], [[Unidad organizacional]], [[Comparativa con metodologías existentes]], [[Preguntas abiertas]] |
| D-04 | Con una sola persona, que quien ejecuta valide se acepta por escrito, compensado con las revisiones automáticas y el validador externo para lo irreversible. A partir de dos personas, quien ejecuta no valida. | Con una persona es inevitable; ninguna fuente lo resuelve ([[Propuestas existentes - Autorrevisión en equipos de uno]]). | [[Roles humanos]], [[Fase 5 - Validation]] |
| D-05 | Un veredicto "parcial" cuenta como no logrado en la tasa de éxito de objetivos; la tasa de parciales se reporta aparte. | La tasa era binaria y el veredicto tenía tres valores. Dos jueces independientes propusieron lo mismo. | [[Métricas operativas]], [[Fase 5 - Validation]] |
| D-06 | Que una acción sea reversible es necesario pero no suficiente para que la haga el agente sin aprobación. La suspensión de un agente la ordena el dueño. | El principio de reversibilidad chocaba con la matriz y la regla de suspensión no tenía responsable. | [[Gobernanza]] |
| D-07 | Cada hipótesis que el piloto mide lleva "se refuta si…". Las demás quedan como hipótesis declarada, sin criterio inventado. | Varias hipótesis no decían cómo se refutarían. | Notas con sección Hipótesis; [[Piloto - Combinación A]] |
| D-08 | En tiny teams, topes de tiempo y costo en lugar de estimaciones. El pronóstico por Monte Carlo se retoma con los datos del piloto. | Monte Carlo necesita más objetivos cerrados de los que produce un equipo chico ([[Investigación - Estimación y tiempo con agentes]]). | [[Métricas operativas]], [[Fase 2 - Constraints]], [[Síntesis - Economía de tokens]] |
| D-10 | Las métricas de reutilización de conocimiento y de recuperación de contexto quedan fuera del núcleo, como referencia para empresas. Su rediseño se pospone. | Para tiny teams casi no aportan, y su rediseño está abierto (Goodhart por mandato, superposición con el tiempo de decisión). | [[Métricas organizacionales]], [[Núcleo ODLC para tiny teams]] |
| D-11 | Las compuertas que proponía la Relectura se adoptan como prácticas del núcleo, no como reglas de la Fase 1 y la Fase 6. | El núcleo ya las tiene como prácticas medibles. | [[Relectura del Manifiesto Ágil]], [[Fase 1 - Objective]], [[Fase 6 - Learning]] |
| D-12 | El material crudo se cita con el campo `origen:`, no `fuente:`. Inbox pasa a nota meta. | El README dice que lo crudo no se usa como fuente canónica, y cinco notas de cursos lo hacían. | Notas de [[Cursos HACS-ODLC]], [[Inbox]], README |
| D-13 | Los niveles L0 a L6 del loop pasan a llamarse "niveles de complejidad del loop", y las fases de la Safety Mesh, "estado del proyecto". | Chocaban con los niveles de madurez y con las fases de ODLC. | [[Agent Loop Engineering]], [[Módulo 3 - Gobernanza]], [[Glosario y taxonomía]] |

## Decisiones del 2026-10-08 (segunda tanda)

Surgen del juez adversarial que revisó la aplicación de D-01 a D-13 y de la deprecación de Cognitive OS por el dueño.

| # | Decisión | Motivo | Supersede |
|---|---|---|---|
| D-15 | **Cognitive OS queda deprecado** (pedido del dueño). Se retiran del vault la implementación `luum-cognitive-os`, su Safety Mesh y la arquitectura de referencia "Cognitive OS". Las ideas genéricas que sirven (memoria compartida, sandbox, verificación, gobernanza por tipo de acción) quedan en HACS y en Gobernanza sin la marca. La carpeta `05_cognitive-os/` se renombra y conserva lo que no dependía de Cognitive OS. El Módulo 3 del curso se reescribe genérico. | El producto se deprecó. ODLC no dependía de él: ninguna fase, ni el núcleo ni el piloto lo usan. | D-14 (la atribución a OliveX era de ese producto y se va con él) |
| D-16 | **Lo irreversible exige siempre el validador externo.** La excepción escrita de D-04 cubre solo que quien ejecuta valide; no reemplaza al validador externo. | Una lectura con "o" dejaba que la excepción escrita reemplazara al validador justo en lo que no se relaja. D-04 ya decía "compensado con". | Aclara D-04 |
| D-17 | La compensación de D-04 es la **constancia de outcome que un tercero puede abrir y verificar**, además de las revisiones automáticas (que revisan código, no outcome). | Las revisiones automáticas no compensan la autovalidación del outcome. | Completa D-04 |
| D-18 | La columna "¿Se relaja con la madurez?" de la matriz de [[Gobernanza]] se adopta como está: **no** se relajan definir objetivos, seguridad y accesos, gasto fuera de presupuesto ni lo irreversible; **sí** arquitectura, código, merge y deploy. Las acciones externas (mensajes a terceros) y la remediación en producción se agregan como filas propias. | La columna la completó la aplicación de D-01 y conviene registrarla como decisión, no como efecto lateral. | Completa D-01 |
| D-19 | **HACS queda sin umbral mínimo** hasta tener datos del piloto. "Agente que escribe en sistemas compartidos" (D-02) se define como agente con permisos de escritura sobre un sistema que usan otras personas o clientes; un agente que escribe solo en el repo propio del MVP no cae ahí. | D-02 sacó "ya es HACS" sin reemplazo y el término no estaba definido. | Completa D-02 |
| D-20 | La autogestión de estilo Teal sigue con **dos tensiones abiertas** (aprobación jerárquica de lo irreversible frente al advice process, y métricas frente a "sentir y responder"). D-01 solo fija la frontera humano/agente. | La aplicación de D-01 había dado por resuelta una de las dos. | Corrige la lectura de D-01 |
| D-21 | El motivo de D-03 se corrige: la evidencia de más fallas viene de cambios del modelo de empleo de fundadores (fuente secundaria), **extrapolada** a la adopción gradual de un método, sin medición de gradualidad. | El motivo decía más que la fuente. | Corrige el motivo de D-03 |

## Pendientes del dueño

| # | Decisión | Por qué no la toma la arquitectura |
|---|---|---|
| D-09 | Promesas comerciales del curso (entregables, cupos, precios, criterios de aprobación) | Decisión de negocio. |

---

## Decisiones del piloto (sección 13 de [[Piloto - Combinación A]])

Tomadas por arquitectura a pedido del dueño el 2026-10-08. Se confirman al sellar el protocolo; cambiarlas después es un desvío declarado.

| # | Decisión | Motivo |
|---|---|---|
| P-01 | **Producto:** lo elige el dueño con estos criterios: un problema que ya le contaron al menos tres clientes potenciales a los que puede contactar cada semana; un precio chico que permita preventa; sin manejo propio de pagos ni de datos sensibles en las 12 semanas (un checkout de terceros sí); construible por una persona; y **que no sea un producto sobre ODLC**. | El fixture mostró que lo que limita es la cantidad de unidades con outcome: el producto tiene que dar feedback en días. Un producto sobre el propio método mezclaría la tesis con la demanda del método y contaminaría la Fase 0. |
| P-02 | **Diseño:** línea de base múltiple entre los tres tipos de objetivo, con inicio y orden sorteados, más tratamientos alternantes para la revisión de PR. Se descarta A-B-A-B. | El aprendizaje con el método no se revierte y el WWC desaconseja el retiro en ese caso; A-B-A-B además obliga a trabajar peor con clientes reales. |
| P-03 | **Tamaño de unidad:** como máximo 3 días de trabajo activo; lo que sea más grande se parte. | Para que cada media semana tenga datos en cada tipo y la serie no quede rala. [hipótesis] |
| P-04 | **Duración:** 12 semanas, 2 puntos por semana, más 28 días de seguimiento. | Mínimo del WWC (al menos 5 puntos por fase) con tres fases escalonadas. |
| P-05 | **Fase 0:** 12 entrevistas fijas. Confirma si al menos 6 de 12 mencionan el dolor sin que se les sugiera y al menos 3 de 12 muestran compromiso (tiempo, dinero o una solución casera ya probada). Descarta si 2 o menos lo mencionan. Lo intermedio es ambiguo: se suman 5 entrevistas una sola vez y, si sigue ambiguo, se descarta. Sin incentivo. Hasta 3 semanas. | Guest y otros (2006): la saturación llegó dentro de las primeras doce entrevistas. Contar en casos y no en porcentajes evita la ambigüedad de redondeo. Los umbrales en sí no tienen fuente. |
| P-06 | **Codificación ciega:** un agente de otra familia sin acceso al protocolo, más 3 entrevistas recodificadas por una persona externa para verificar al agente. Acuerdo mínimo kappa 0,60. | El kappa mínimo viene del WWC. La recodificación humana controla que el agente codificador no sea el punto débil. |
| P-07 | **Revisor:** dos pasadas automáticas por PR (contexto limpio del mismo modelo y otra familia de capacidad comparable o mayor), sin revelar la autoría, y ningún hallazgo se aplica sin un test que falle antes y pase después. | Es la combinación mínima de [[Propuestas existentes - Autorrevisión en equipos de uno]]. La regla del test filtra las regresiones que puede meter un revisor de otra familia: en Xiang y otros (2026), Codex revisando a Claude produjo 13 regresiones y 3 arreglos. Costo: una segunda suscripción. |
| P-08 | **H2 (contra el mejor componente solo) pasa a exploratoria.** | Con el volumen de PR de una persona, 15 % de siembra repartido en tres condiciones difícilmente llega a 5 semillas por condición; la tesis se decide con H1. |
| P-10 | **Fase 0 en dos tramos con veredicto congelado:** se evalúan las primeras 12 entrevistas por fecha; solo si dan ambiguo se suman 5 y se evalúa sobre 17 con umbrales propios: confirma con al menos 9 de dolor y al menos 5 de compromiso, descarta con 3 o menos. Más entrevistas de las previstas invalidan los datos. Cuenta como dolor la codificación ciega "sí" que el entrevistador no marcó como inducida. Compromiso = tiempo, dinero o una solución casera ya probada (unifica el libro de códigos). La recodificación humana de P-06 se registra aparte y se informa su kappa contra el agente; no pisa la codificación del agente. | Evita la parada opcional (agregar entrevistas hasta cambiar el veredicto) y que la segunda oportunidad baje la vara. Umbrales para 17 proporcionales a los de 12, sin fuente. | Completa P-05 y P-06 |
| P-09 | Se mantienen como propuestas sin fuente, declaradas: alfa 0,05; K1 70 %; K2 50 % en 3 semanas; K3 4 semillas; latencia 30 s y aprobación 95 %; siembra 15 %; tolerancia de horas ±20 %; ventana de outcome 28 días con nivel mínimo 2. Se implementa K4 en el script con corte parcial en la semana 8. | No hay fuente mejor; declararlas antes de empezar es lo que las vuelve honestas. |

---
Relacionado: [[Objeciones al marco]] · [[Núcleo ODLC para tiny teams]] · [[Piloto - Combinación A]] · [[Preguntas abiertas]]
