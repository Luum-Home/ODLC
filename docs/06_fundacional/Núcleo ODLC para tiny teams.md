---
tags: [fundacional, nucleo, tiny-teams]
status: borrador
created: 2026-10-08
---

# Núcleo ODLC para tiny teams

Dinámica de trabajo para una a tres personas que construyen con agentes de IA. Cada elemento deja un archivo que mide `scripts/piloto_metricas.py`. Es la [[Piloto - Combinación A|combinación A]] aplicada; las etiquetas remiten a [[#Respaldo]].

## Lo que lo distingue

La unidad es humano más agentes [hipótesis]. Se diseña para el humano de mínimo esfuerzo [hipótesis]. Se verifica corriendo y el humano audita el sistema de revisión, no cada artefacto [medido]. Se mide si cada acto humano hizo su trabajo, no esfuerzo ni velocidad [guía]. Decidir y validar se aceleran mucho menos que construir, y ahí va el tiempo humano [medido]. Con pocos clientes vale lo que le cuesta algo al cliente [medido]. Todo objetivo nace con criterio de abandono [medido].

## Roles

| Rol | Qué hace | Deja en el repo | Difícil de fingir porque | Respaldo |
|---|---|---|---|---|
| **Dueño del objetivo** (humano) | Fija target y salida, elige, valida, audita. Solo, cubre Sponsor, Product, Architect y Operator | Decisiones `decidida_por: humano` | Timestamps de la herramienta | [hipótesis] |
| **Escritor** (agente) | Redacta la ficha, propone alternativas, implementa | PR, `registro-ia/` | Los tests los escribe otro agente y no puede editarlos | [medido] |
| **Revisor** (agente) | Dos pasadas por PR: mismo modelo con contexto limpio y otra familia de capacidad comparable, sin saber quién escribió | `hallazgos`, `modelo_revisor` | El script alerta si comparte familia con el escritor | [medido] |
| **Validador externo** (asesor, par o cliente que paga) | Aprueba lo irreversible; si no hay, excepción escrita | Decisión `clase: irreversible` | Es otra persona | [guía] |

## Artefactos y reglas

| Elemento | Qué es y cuándo | Deja en el repo | Difícil de fingir porque | Respaldo |
|---|---|---|---|---|
| **Ficha de objetivo** (central) | Antes de construir: resultado para el cliente, métrica con baseline, target y ventana, criterio de abandono con fecha, superficies que no se tocan | `unidades/U-*.md` | Se mide adherencia; `creada_en` contra el primer commit | [medido] |
| **Elegir, no aprobar** | En decisiones significativas, dos opciones o más; el humano escribe el número que espera mover y qué lo haría rechazar | `decisiones/D-*.md` | La elección vacía cuenta como pasividad | [medido] |
| **Lo irreversible frena** | Lo reversible avanza con revisor y tests; pagos, datos de clientes, borrado y deploy esperan al validador | `clase` en la decisión | Nadie aprueba lo propio | [guía] |
| **Se verifica corriendo** | Cada PR cierra por CI obligatorio, no por lectura ni por declaración del agente | Corridas de CI | Alcanza también al administrador | [medido] |
| **Hallazgo con test** | Ningún hallazgo se aplica sin un test que falle antes y pase después | Test en el PR | El rojo previo queda en CI | [medido] |
| **Auditoría por sorteo** | Cada semana, un sorteo elige una unidad aprobada y el humano revisa su respaldo | Decisión `auditoria_muestreo` | No elige quien revisa | [guía] |
| **Semilla** | Con tasa baja, entra un defecto conocido a la revisión | Manifiesto comprometido por hash | Sin semillas detectadas, la aprobación vale cero (K3) | [hipótesis] |
| **Constancia de outcome** | A los 28 días de entregar, escalera de 0 (opinión o usuario simulado) a 3 (pago); cuentan 2 y 3 | `validaciones/V-*.md` | Pide un artefacto que un tercero pueda abrir | [medido] |
| **Aprendizaje** | Al cerrar la unidad, un hook lo crea vacío | `aprendizajes/A-*.md` | Lo vacío o repetido se cuenta | [hipótesis] |
| **Tablero** | Cada media semana: P1 (outcome validado), P2 (descarte tras entregar), abandono temprano, espera separada del trabajo, adherencia, pasividad, semillas y criterios de abandono | Salida del script; exit 1 con un criterio activo | Sin autoinforme; protocolo sellado | [medido]; umbrales [hipótesis] |

## Qué NO es

- **No es Scrum con agentes:** sin sprint, daily ni backlog; cierra el outcome validado, no el Done.
- **No reemplaza hablar con clientes.**
- **No demuestra el marco en general:** un caso único demuestra el caso; generalizar exige la regla 5-3-20 ([[Piloto - Combinación A#12. Qué puede concluir este piloto y qué no]]).
- **No evalúa personas:** nadie cobra ni se califica por las métricas.

## Cómo empezar el lunes

1. Copiar `scripts/fixtures/piloto/plantillas/` al repo y sellar `protocolo.md`: sin sello, el script no calcula.
2. Configurar escritor, agente de tests y revisor de otro proveedor; registrarlos en `registro-ia/`; CI obligatorio sin excepción para administradores.
3. Escribir la primera ficha con criterio de abandono y fecha.
4. Instalar el hook de aprendizaje y agendar sorteo y tablero.
5. Antes de construir, nombrar los clientes reales del escalón 2.

En el piloto, el núcleo entra por tipo de objetivo según el sorteo.

## Cuándo se agranda

Cambiar el modelo organizacional inicial se asoció con el triple de fallas [medido]; por eso el núcleo ya trae las costuras. Al sumar gente se agrega un dueño nombrado por ficha (`responsable_humano`, de [[Fase 1 - Objective]]); la auditoría la hace alguien distinto del dueño; la segunda persona puede validar lo irreversible; la pasividad se agrega por etapa y el dato individual vuelve solo a la persona; y un consejo de pares con reuniones regulares, metas y feedback [medido]. No hay umbral medido para contratar.

---

## Respaldo

Convención de [[Investigación - Tiny teams y bootstrapping]]: [medido] incluye estudios observacionales y de otro dominio, aclarado en cada línea; [guía] es recomendación sin evaluación de resultados; [testimonio] es relato o dato autodeclarado; [hipótesis] es propuesta de este vault sin evidencia directa, que se prueba en el piloto.

### Ideas distintivas, contrastadas

1. **Unidad humano más agentes** [hipótesis]. Las startups con IA son 12 % a 25 % más chicas (Kim y Koning 2026, correlacional) y redujeron empleo ~8 % (Gupta y otros 2026) [medido]; que produzcan como equipos grandes no está medido ([[Investigación - Tiny teams y bootstrapping]], huecos).
2. **Humano de mínimo esfuerzo** [hipótesis]. Principios 1 y 2 de la Objeción 5 en [[Objeciones al marco]]; la autogestión mejoró solo a los proactivos (Lee) [medido].
3. **Verificar corriendo y auditar el sistema** [medido]. Respaldo en benchmarks y en un experimento controlado: tests de solo lectura bloquean la trampa de modificar tests (ImpossibleBench); auditar un 2 % elegido por un modelo débil dio 62 % de seguridad, contra 15 % al azar (AI Control). Matiz: los tests son el blanco favorito del reward hacking, y tomar "los tests pasan" como garantía es una validación poco confiable (Dhanorkar y otros 2026). Compensaciones C1 y C4 de [[Propuestas existentes - Revisión en manos de agentes]].
4. **Medir el acto, no el esfuerzo** [guía]. IMDA propone tasa de rechazo y tiempo de respuesta, sin umbrales validados. Con una persona no choca con nada; con dos o más reabre el conflicto 2.2 de [[Síntesis - Cómo encajan las propuestas existentes]] (medir personas contra no evaluarlas con números), que la combinación A resuelve midiendo la etapa.
5. **Decidir y validar no se aceleran** [medido], con matiz. La ganancia cae de +240 % en commits a +30 % en releases (Demirer y otros 2026), el tiempo de revisión subió 91 % (Faros) y el tiempo en reuniones no cambió con IA (Dillon y otros); el vault los lee como "consistentes con el techo tipo Amdahl". Se refina la idea: la preparación sí se abarata (12,7 % a 16,4 % en P&G) y nadie midió el tiempo de decidir con y sin agentes ([[Propuestas existentes - Deliberación que no se acelera]]). Queda "se aceleran mucho menos", no "no se aceleran".
6. **Pocos clientes** [medido, observacional]. En Kickstarter, 50 % más compromisos de pago se asocian con 9 % más probabilidad de comercializar (Xu). The Mom Test no tiene evaluación propia [testimonio].
7. **Criterio de abandono** [medido]. El efecto replicado del enfoque científico es abandonar antes las ideas malas (Camuffo y otros 2020, 116 startups; réplica 2024, 759 firmas). En startups, no en equipos con agentes.

### Por elemento

- **Dueño del objetivo** [hipótesis]: [[Roles humanos]] supone que los cuatro roles pueden ser menos personas; ninguna fuente resuelve la separación de funciones con una sola (COSO 2006) [guía].
- **Escritor y Revisor** [medido], estudios recientes y chicos: es la combinación mínima de [[Propuestas existentes - Autorrevisión en equipos de uno]]. Una pasada con contexto limpio más una de otra familia encontró 56,7 % de errores sembrados contra 42,7 % de dos pasadas del mismo modelo (Song 2026, un autor); ocultar la autoría redujo la autopreferencia (Chae y otros 2026). La revisión entre familias depende de la dirección y puede empeorar (Xiang y otros 2026: de 71,6 % a 89,7 % en un sentido, de 91,4 % a 82,8 % en el otro), y un revisor liviano no aportó. Tests de un agente separado: 87,8 % de precisión contra 61,0 % con un solo agente (AgentCoder). Los errores siguen correlacionados entre proveedores (Kim y otros 2025): el revisor reduce el sesgo, no es independiente. Nada de esto se midió en producción.
- **Validador externo** [guía]: controles compensatorios (COSO 2006) y aprobación concentrada en lo irreversible (IMDA). Los consejos de pares influyen [medido], pero nadie midió al par como control.
- **Ficha de objetivo** [medido]: Camuffo y otros, ver idea 7; criterio con estado y fecha (Duke, en la Síntesis) [testimonio].
- **Elegir, no aprobar** [medido, otro dominio]: elección activa (Carroll y otros 2009) y forzado cognitivo (Buçinca y otros 2021). Asegura que haya decisión, no que sea buena, y es lo peor valorado por quien no disfruta pensar.
- **Hallazgo con test** [medido]: regresiones al aplicar hallazgos (13 contra 3, Xiang y otros 2026) y sobrecorrección del revisor (Jin y Chen 2026), en [[Propuestas existentes - Autorrevisión en equipos de uno]].
- **Lo irreversible frena** [guía]: IMDA; principio 5 de la Objeción 5; segunda persona externa o excepción escrita, sin reemplazo encontrado en [[Propuestas existentes - Autorrevisión en equipos de uno]].
- **CI que alcanza al administrador** [guía]: GitHub deja a los administradores saltarse la protección de ramas salvo que se active "Do not allow bypassing the above settings".
- **Se verifica corriendo** [medido, benchmarks]: ImpossibleBench (tests de solo lectura); Jin y Chen 2026; StrongDM [testimonio].
- **Auditoría por sorteo** [guía]: COSO 2006. Quedó fuera de la combinación mínima de autorrevisión por falta de evidencia, no por falta de valor, igual que la revisión humana diferida (no replicó) y el par externo (solo testimonio); el núcleo la conserva porque la combinación A la usa. El sorteo puro rindió poco en AI Control; elegir qué auditar con un modelo débil es una mejora medida que el piloto no incorpora.
- **Semilla** [hipótesis]: en software no hay aplicación publicada para medir revisores; la evidencia es de rayos X de aeropuerto y de un laboratorio con N = 24 donde no bajaron los errores de comisión. Bainbridge (1983) pide tasa baja. Es la pieza más débil según la Síntesis.
- **Constancia de outcome** [medido, observacional]: Xu; los usuarios simulados fallan en categorías nuevas (Brand y otros) y aplanan grupos (Wang y otros) [medido].
- **Aprendizaje** [hipótesis]: los debriefs mejoran el desempeño (Tannenbaum y Cerasoli 2013) [medido], pero todos suponen alguien que los convoca; el disparador automático no tiene evidencia.
- **Tablero** [medido] contra autoinforme: en el ensayo de METR los desarrolladores tardaron 19 % más y creían haber ganado 20 %. Umbrales [hipótesis]: ver la tabla de decisiones pendientes del piloto.
- **Cuándo se agranda** [medido, observacional]: Stanford Project on Emerging Companies (cambiar el modelo inicial, triple de fallas) y Chatterji y otros 2019 (RCT con 100 firmas: 28 % más crecimiento, 10 puntos menos de falla; no respondieron quienes tenían MBA o venían de aceleradoras). Las costuras desde el día uno son inferencia de la investigación, no resultado de SPEC.

## Relación con el resto del vault

El núcleo es la versión aplicable de [[ODLC]]. Las seis fases ([[Fase 1 - Objective]] a [[Fase 6 - Learning]]), el [[Modelo de madurez AI-Native]], la [[Gobernanza]] completa y los cuatro [[Roles humanos]] quedan como referencia para organizaciones más grandes. La correspondencia con las fases está en la sección 5 de [[Piloto - Combinación A]]. Origen del encargo: [[Cómo nacieron los marcos que se adoptaron]].

### Tensiones declaradas (no se resuelven acá)

- **Quien valida no es quien ejecutó** ([[Fase 5 - Validation]], regla 3). Con una persona no se cumple; el núcleo lo compensa con sorteo, revisor de otra familia y validador externo, sin separación real.
- **Merge a main con aprobación humana** ([[Gobernanza]]). El núcleo deja avanzar lo reversible con revisor agente y tests, y el piloto sortea una condición donde decide el agente solo. La matriz dice "configurable por madurez".
- **Adopción por niveles** ([[Modelo de madurez AI-Native]], [[Manifiesto HACS-ODLC]]). El núcleo pone la ficha como unidad desde el primer día, que es el criterio del Nivel 4, y la evidencia de SPEC sugiere no cambiar de modelo a mitad de camino.
- **ODLC sin agentes** ([[Manifiesto HACS-ODLC]]). El Manifiesto dice que la Fase 1 y la Fase 6 sin agentes ya son ODLC; el núcleo supone agentes. No redefine qué cuenta como ODLC.
- **Revisión del piloto contra la combinación mínima de autorrevisión.** El piloto especifica un revisor de otra familia; la combinación mínima pide además una pasada con contexto limpio, autoría oculta, tests de un agente separado y hallazgos atados a un test. Sumarlos antes del sello es decisión del dueño; después, un desvío declarado.
- **La métrica no evalúa personas.** El núcleo la escribe como regla; [[Objeciones al marco]] la lista como candidata a respuesta a Deming, todavía no escrita para el marco entero.

## Decisiones pendientes que hereda del piloto

Las toma el dueño, según la sección 13 de [[Piloto - Combinación A]]: producto del MVP; diseño (línea de base múltiple o A-B-A-B); duración, fechas y seguimiento; duración, incentivo y umbrales de la Fase 0; quién codifica a ciegas; ventana de outcome y nivel mínimo (28 días, nivel 2); alfa; umbrales de K1 a K3; latencia baja y alerta de aprobación; tasa de siembra (15 %) y semillas mínimas; tolerancia de horas; fuente de los bloques activos; segunda suscripción para el revisor; validador externo para lo irreversible; e implementar K4 en el script.

## Comandos de verificación

Read-only, desde la raíz del repo.

```bash
# Palabras del cuerpo principal (hasta la sección Respaldo, sin frontmatter)
awk 'NR>5 && /^## Respaldo/{exit} NR>5' "docs/06_fundacional/Núcleo ODLC para tiny teams.md" | wc -w
# El tablero corre sobre el fixture ficticio (exit 0) y el sello rechaza un protocolo alterado (exit 2)
python3 scripts/piloto_metricas.py scripts/fixtures/piloto; echo exit=$?
# Las plantillas que nombra "Cómo empezar el lunes"
ls scripts/fixtures/piloto/plantillas/
# Cifras citadas, en sus notas de origen
grep -n "25 % menos empleados\|triplicó la tasa de falla\|28 % más grandes" "docs/00_crudo/Investigación - Tiny teams y bootstrapping.md"
grep -n "15 % de seguridad\|solo lectura" "docs/00_crudo/Propuestas existentes - Revisión en manos de agentes.md"
grep -n "techo tipo Amdahl\|12,7 % a 16,4 %" "docs/00_crudo/Propuestas existentes - Deliberación que no se acelera.md"
```

---
Relacionado: [[Piloto - Combinación A]] · [[Objeciones al marco]] · [[Cómo nacieron los marcos que se adoptaron]] · [[ODLC]] · [[Roles humanos]] · [[Gobernanza]]
