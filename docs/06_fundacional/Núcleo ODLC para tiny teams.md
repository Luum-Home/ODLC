---
tags: [fundacional, nucleo, tiny-teams]
status: borrador
created: 2026-10-08
---

# Núcleo ODLC para tiny teams

Para una a tres personas que construyen con agentes: tres roles y siete reglas. La unidad es humano más agentes [hipótesis]; el tiempo humano va a decidir y validar, que se aceleran mucho menos que construir [hipótesis]. Todo es hipótesis hasta que el [[Piloto - Combinación A|piloto]] lo pruebe. Las etiquetas remiten a [[#Respaldo]].

## Los diez elementos

| Elemento | Qué es y qué deja | Etiqueta | Antecedente |
|---|---|---|---|
| **Dueño del objetivo** (humano) | Fija target y abandono, elige, valida, audita | [hipótesis] | Sin antecedente directo: funde los cuatro [[Roles humanos]] |
| **Escritor** (agente) | Escribe ficha y código; no edita los tests, que escribe otro agente | [medido, benchmark] | Separar quien escribe de quien prueba |
| **Revisor** (agente) | Dos pasadas por PR, contexto limpio y otra familia, sin revelar la autoría (P-07) | [medido, benchmark] | Inspección de código (Fagan, 1976) |
| **Ficha de objetivo** | Antes de construir: resultado para el cliente, métrica con baseline y target, criterio de abandono con fecha, topes de tiempo y costo (D-08), lo que no se toca | Ficha [hipótesis]; abandono [hipótesis] con respaldo [medido, otro tratamiento] | Shape Up (pitch, apetito, no-gos, circuit breaker); OKR y Lean Startup |
| **Se verifica corriendo** | Cada PR cierra por CI obligatorio, también para el administrador | [medido, benchmark] | Integración continua de XP |
| **Hallazgo con test** | Ningún hallazgo se aplica sin un test que falle antes y pase después. `registro-pr/` | [medido, benchmark]; la regla del rojo previo [hipótesis] | Test de regresión de TDD y XP |
| **Lo irreversible frena** | Pagos, datos de clientes, borrado y migraciones destructivas esperan siempre a un validador externo (asesor, par o cliente). Con una persona, además, excepción escrita compensada con constancia de outcome (D-16, D-17) | [guía] | Puertas de una y dos vías (Amazon) |
| **Auditoría elegida** | Semanal: un modelo distinto del escritor elige la unidad más sospechosa, más una fracción al azar; el humano la revisa. Registra criterio o semilla y unidad | [medido, benchmark de juguete] + [guía] | Muestreo de auditoría (COSO) |
| **Constancia de outcome** | Al cierre, un compromiso o pago de cliente que un tercero pueda abrir | Escalera [hipótesis]; pago como señal [medido, observacional, otra plataforma] | Sin antecedente: escalera propia |
| **Tablero** | `scripts/nucleo_tablero.py`: abandono vencido sin veredicto, fichas sin métrica, dueño o topes, PR con rojo previo. Registro declarado y auditable | Umbrales [hipótesis] | Circuit breaker de Shape Up |

## Qué NO es

- **No es Scrum con agentes:** sin sprint ni daily; el dueño ordena una cola de fichas y el trabajo cierra con el outcome validado, no con el Done.
- **No reemplaza hablar con clientes.**
- **No evalúa personas:** nadie cobra ni se califica por las métricas.

## Cómo empezar el lunes

Sin sellar el protocolo del piloto.

1. Copiar `scripts/nucleo_tablero.py`, `scripts/piloto_metricas.py` (lo usa el tablero) y `scripts/fixtures/nucleo/plantillas/`.
2. Escribir la primera ficha en `fichas/` con criterio de abandono y fecha.
3. Configurar escritor, agente de tests y revisor de dos pasadas; CI obligatorio con "Do not allow bypassing the above settings".
4. Agendar la auditoría semanal y correr `python3 scripts/nucleo_tablero.py . --fecha AAAA-MM-DD` cada media semana.
5. Antes de construir, nombrar los clientes que pueden dejar la constancia.

## Costo mínimo [hipótesis]

- **Protección de ramas en repo privado:** GitHub Pro o Team.
- **Segunda pasada del revisor (otra familia):** otra suscripción, del orden de USD 20 por mes.
- **Fuera del repo:** selector de auditoría, CI y agente de tests.
- **Horas:** unas dos por semana.
- **Límite:** el núcleo no impide que un administrador único apague su propio CI.

## Cuándo se agranda

Cambiar el modelo de empleo inicial se asoció con el triple de fallas [medido, observacional, fuente secundaria]. El núcleo trae las costuras: dueño nombrado por ficha (`responsable_humano`, de [[Fase 1 - Objective]]), auditoría por alguien distinto del dueño, segunda persona como validador y un consejo de pares [medido]. En un equipo existente se adopta de a poco ([[Registro de decisiones]], D-03). No hay umbral medido para contratar.

---

## Respaldo

Convención de [[Investigación - Tiny teams y bootstrapping]]: [medido] aclara entre corchetes si es benchmark, observacional, cualitativo o de otro dominio; [guía] es recomendación sin evaluación de resultados; [testimonio] es relato o dato autodeclarado o de proveedor; [hipótesis] es propuesta de este vault sin evidencia directa.

### Ideas que lo sostienen

1. **Unidad humano más agentes** [hipótesis]. Las startups con IA son 12 % a 25 % más chicas (Kim y Koning 2026, correlacional, leído vía fuente secundaria: SSRN devolvió 403) y redujeron empleo ~8 % en las más expuestas (Gupta y otros 2026) [medido, observacional]; que produzcan como equipos grandes no está medido.
2. **Decidir y validar se aceleran mucho menos** [hipótesis]. Apoyo [medido, indirecto]: la ganancia cae de +240 % en commits a +30 % en releases (Demirer y otros 2026, NBER) y el tiempo en reuniones no cambió con IA (Dillon y otros, NBER). El tiempo de revisión subió 91 % según Faros [testimonio, dato de proveedor]. La preparación sí se abarata (12,7 % a 16,4 % en P&G) y nadie midió el tiempo de decidir con y sin agentes ([[Propuestas existentes - Deliberación que no se acelera]]).
3. **Medir el acto, no el esfuerzo** [guía]. IMDA propone tasa de rechazo y tiempo de respuesta, sin umbrales validados.

### Por elemento

- **Dueño del objetivo** [hipótesis]: ninguna fuente resuelve la separación de funciones con una sola persona (COSO 2006) [guía].
- **Escritor y Revisor** [medido, benchmark]: tests de un agente separado, 87,8 % de precisión contra 61,0 % con un solo agente (AgentCoder, GPT-3.5 en HumanEval). Una pasada con contexto limpio más una de otra familia encontró 56,7 % de errores sembrados contra 42,7 % (Song 2026, preprint de un autor); el contexto limpio solo no fue significativamente mejor que una autorrevisión (p = 0,26). Ocultar la autoría redujo la autopreferencia (Chae y otros 2026). La revisión entre familias depende de la dirección y puede empeorar (Xiang y otros 2026), y los errores siguen correlacionados entre proveedores (Kim y otros 2025). Nada de esto se midió en producción ([[Propuestas existentes - Autorrevisión en equipos de uno]]).
- **Ficha de objetivo**: el criterio de abandono es [hipótesis] con respaldo [medido, otro tratamiento]. Camuffo y otros (2020, 116 startups) dieron la misma tasa de abandono temprano; la réplica (2024, 759 firmas) dio más abandono, no antes. Lo que se trató fue el método científico en startups, no una ficha con fecha. Los topes de tiempo y costo reemplazan la estimación [hipótesis]: el pronóstico por Monte Carlo necesita más objetivos cerrados de los que produce un equipo chico ([[Registro de decisiones]], D-08).
- **Se verifica corriendo** [medido, benchmark]: los tests de solo lectura bloquean la trampa de modificarlos (ImpossibleBench). Tomar "los tests pasan" como garantía es una validación poco confiable (Dhanorkar y otros 2026) [medido, cualitativo, 17 entrevistas]. GitHub deja a los administradores saltarse la protección salvo con "Do not allow bypassing the above settings" [guía].
- **Hallazgo con test** [medido, benchmark]: regresiones al aplicar hallazgos, 13 contra 3 (Xiang y otros 2026), y sobrecorrección del revisor (Jin y Chen 2026). Exigir que el test falle antes es [hipótesis] tomada de TDD; el orden test antes o después no tuvo efecto importante en Fucci y otros (2016).
- **Lo irreversible frena** [guía]: aprobación concentrada en lo irreversible (IMDA) y controles compensatorios (COSO 2006). El deploy no está en la lista: lo aprueba el dueño, como en [[Gobernanza]] y en la Fase 2 del piloto. Los consejos de pares influyen [medido], pero nadie midió al par como control.
- **Auditoría elegida** [medido, benchmark de juguete] + [guía]: en AI Control, auditar al azar un 2 % dio 15 % de seguridad; que un modelo débil eligiera qué auditar subió a 62 %, y a 92 % si además editaba lo sospechoso. Problemas de programación con GPT-4 y GPT-3.5, no producción. [[Objeciones al marco]] pide la muestra "elegida por el sistema, no al azar"; la fracción al azar cubre lo que el selector no ve.
- **Constancia de outcome**: la escalera de niveles y la ventana de 28 días del piloto son [hipótesis] (sin fuente, sección 13 del piloto). En Kickstarter, más compromisos de pago se asocian con más probabilidad de comercializar (Xu) [medido, observacional, otra plataforma]. Los usuarios simulados fallan en categorías nuevas (Brand y otros) [medido].
- **Tablero**: las fechas son las que declara cada archivo; el script no usa git, así que el registro es declarado y auditable contra el historial, no automático. Contra el autoinforme: en el ensayo de METR, 16 desarrolladores con herramientas de 2025 tardaron 19 % más y creían haber ganado 20 % [medido, RCT].
- **Cuándo se agranda** [medido, observacional, fuente secundaria]: el triple de fallas sale de una nota de prensa de Stanford GSB (2007) sobre el Stanford Project on Emerging Companies (Baron, Hannan y Burton). Chatterji y otros 2019: RCT con 100 firmas, 28 % más crecimiento y 10 puntos menos de falla con consejos de pares [medido].

## Extensiones para el piloto

Quedan fuera del núcleo; las define [[Piloto - Combinación A]] y las mide `scripts/piloto_metricas.py` con el protocolo sellado.

- **Elegir, no aprobar**: dos opciones o más y el número que se espera mover. [medido, otro dominio]: elección activa (Carroll y otros 2009) y forzado cognitivo (Buçinca y otros 2021).
- **Aprendizaje** al cerrar la unidad [hipótesis]. Antecedente: retrospectiva y after-action review; los debriefs mejoran el desempeño (Tannenbaum y Cerasoli 2013) [medido], pero suponen alguien que los convoca.
- **Tablero del piloto**: P1, P2, abandono temprano, espera separada del trabajo (flow efficiency de Lean y Kanban), adherencia, pasividad y K0 a K5.
- **Semilla de defectos**: solo existe con la condición HA y su criterio K3; el repo no trae sembrador. Antecedente y alcance en la sección 6.4 del piloto.

## Tensiones declaradas

- **Quien valida no es quien ejecutó** ([[Fase 5 - Validation]], regla 3). Con una persona no se cumple: se acepta por escrito, compensado con la constancia de outcome que un tercero puede abrir y, para lo irreversible, con el validador externo siempre; desde dos personas, quien ejecuta no valida ([[Registro de decisiones]], D-04, D-16 y D-17).
- **Excepción explícita al principio 3 de [[Gobernanza]].** Con una persona sola, el revisor agente decide lo reversible, merge incluido, desde el primer día y sin historial, aunque ser reversible no alcanza ([[Registro de decisiones]], D-06). Lo irreversible, la acción externa y lo marcado "siempre" quedan fuera.
- **Suspensión por Rework.** [[Gobernanza]] prevé que el dueño suspenda al agente con Rework sobre 40 % (D-06); el núcleo no la trae.
- **No iterar contra la señal que juzga** (C7 en [[Objeciones al marco]]). Iterar al escritor hasta que pase CI es exactamente eso; el agente de tests separado lo atenúa, no lo elimina.
- **Comprensión compartida.** Ninguna compensación reemplaza lo que la revisión humana producía ([[Objeciones al marco]]).
- **Primero la práctica, después el nombre** ([[Cómo nacieron los marcos que se adoptaron]]). El núcleo nombra antes de practicar; los nombres son provisionales hasta el piloto.
- **Adopción por niveles** ([[Modelo de madurez AI-Native]]). La ficha como unidad desde el primer día es el criterio del Nivel 4.
- **ODLC sin agentes** ([[Manifiesto HACS-ODLC]]). El núcleo supone agentes, pero lo que cuenta como adopción de ODLC es la ficha con criterio de abandono y el resultado validado, con o sin agentes ([[Registro de decisiones]], D-02).
- **La métrica no evalúa personas.** Es regla del núcleo; [[Objeciones al marco]] la lista como respuesta a Deming todavía no escrita.

## Relación con el resto del vault

El núcleo es la versión aplicable de [[ODLC]]. Las seis fases, el [[Modelo de madurez AI-Native]], la [[Gobernanza]] completa y los cuatro [[Roles humanos]] quedan como referencia para organizaciones más grandes. Las decisiones del piloto están en su sección 13 y en [[Registro de decisiones]]. Las métricas de reutilización de conocimiento y de recuperación de contexto quedan fuera del núcleo, como referencia para empresas (D-10). Origen del encargo: [[Cómo nacieron los marcos que se adoptaron]].

## Comandos de verificación

Read-only, desde la raíz del repo.

```bash
# Palabras del cuerpo principal (hasta la sección Respaldo, sin frontmatter)
awk 'NR>5 && /^## Respaldo/{exit} NR>5' "docs/06_fundacional/Núcleo ODLC para tiny teams.md" | wc -w
# Tablero del núcleo: caso sin alertas (exit 0) y caso con alertas (exit 1)
python3 scripts/nucleo_tablero.py scripts/fixtures/nucleo/caso-sin-alertas --fecha 2026-11-30; echo exit=$?
python3 scripts/nucleo_tablero.py scripts/fixtures/nucleo/caso-con-alertas --fecha 2026-11-30; echo exit=$?
# El tablero del piloto no lee criterios de abandono por ficha (da 0)
grep -c criterio_abandono scripts/piloto_metricas.py
# Protección de ramas en repos privados: Pro, Team o Enterprise
curl -s https://docs.github.com/en/get-started/learning-about-github/githubs-plans | grep -o "Protected branches" | head -1
# Cifras citadas, en sus notas de origen
grep -n "triplicó la tasa de falla\|28 % más grandes\|25 % menos empleados" "docs/00_crudo/Investigación - Tiny teams y bootstrapping.md"
sed -n '77,78p;117p' "docs/00_crudo/Investigación - Tiny teams y bootstrapping.md"
grep -n "15 % de seguridad\|solo lectura" "docs/00_crudo/Propuestas existentes - Revisión en manos de agentes.md"
grep -n "p = 0,26\|AgentCoder, arXiv" "docs/00_crudo/Propuestas existentes - Autorrevisión en equipos de uno.md"
grep -n "techo tipo Amdahl\|12,7 % a 16,4 %" "docs/00_crudo/Propuestas existentes - Deliberación que no se acelera.md"
```

Salida al 2026-10-08:

```text
$ python3 scripts/nucleo_tablero.py scripts/fixtures/nucleo/caso-sin-alertas --fecha 2026-11-30; echo exit=$?
Corte: 2026-11-30 · 2 ficha(s)
  F-001: dueño fundadora, abandono 2026-11-23, veredicto sigue
  F-002: dueño fundadora, abandono 2026-12-14, veredicto pendiente
PR con test que falla antes y pasa después: 1/2 (0.50)
Alertas (0):
exit=0
$ python3 scripts/nucleo_tablero.py scripts/fixtures/nucleo/caso-con-alertas --fecha 2026-11-30; echo exit=$?
Corte: 2026-11-30 · 2 ficha(s)
  F-001: dueño fundadora, abandono 2026-11-23, veredicto sigue
  F-003: dueño s/d, abandono 2026-11-16, veredicto pendiente
PR con test que falla antes y pasa después: sin registro-pr/
Alertas (4):
  - F-003: sin dueño
  - F-003: métrica incompleta (falta baseline)
  - F-003: sin tope (tope_tiempo, tope_costo)
  - F-003: criterio de abandono vencido el 2026-11-16 sin veredicto
exit=1
```

Precios leídos el 2026-10-08 en páginas oficiales: GitHub Team, USD 4 por usuario por mes los primeros 12 meses (github.com/pricing); Claude Pro, USD 20 por mes (claude.com/pricing); Google AI Pro, USD 19,99 por mes (gemini.google/subscriptions). La página de precios de OpenAI devolvió 403: sin dato.

---
Relacionado: [[Piloto - Combinación A]] · [[Objeciones al marco]] · [[Cómo nacieron los marcos que se adoptaron]] · [[ODLC]] · [[Roles humanos]] · [[Gobernanza]]
