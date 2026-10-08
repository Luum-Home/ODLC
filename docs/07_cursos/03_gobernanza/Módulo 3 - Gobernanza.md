---
tags: [cursos, educacion, gobernanza, lideres, tecnico]
status: borrador
created: 2026-06-10
---

# Módulo 3 — Gobernanza de sistemas humano-agente (Híbrido)

Este módulo está dirigido tanto a líderes de proyecto como a ingenieros de software. Su objetivo es definir e implementar la **gobernanza de autonomía**: qué decide cada uno, cómo se hace cumplir en el arnés y cómo se evita que la aprobación humana se vuelva un sello de goma. No depende de ninguna herramienta en particular.

**Objetivos de aprendizaje.** Al terminar el módulo, quien lo cursa puede:

1. Leer la matriz única de aprobaciones de [[Gobernanza]] y ubicar cualquier acción de un agente en una fila.
2. Traducir la matriz a controles técnicos del arnés.
3. Reconocer el sesgo de automatización y diseñar la supervisión para que lo atenúe.
4. Elegir compensaciones cuando la revisión pasa a manos de agentes.

Etiquetas de respaldo: **[medido]** estudio con medición; **[testimonio]** relato o dato de proveedor sin método publicado; **[guía]** marco o norma sin medición propia; **[hipótesis]** propuesta de este vault, sin validar.

---

## 1. El concepto de gobernanza humana

El quinto valor del [[Manifiesto HACS-ODLC]] establece que **los humanos lideran la estrategia y deciden los límites de riesgo, mientras que los agentes analizan y ejecutan**.

Un sistema sin gobernanza, donde un agente puede desplegar a producción sin revisión o contratar servidores por su cuenta, traslada el riesgo a quien menos control tiene sobre él: la responsabilidad no desaparece, cae sobre el humano más cercano (zona de deformación moral, Elish, 2019) [guía].

---

## 2. La matriz única de aprobaciones

Este módulo no mantiene una lista propia de aprobaciones. La fuente única es la matriz de [[Gobernanza#Límites de autonomía (matriz borrador)|Gobernanza § Límites de autonomía]], ordenada por tipo de acción ([[Registro de decisiones]], D-01). En clase se trabaja sobre la matriz vigente, no sobre una copia.

Lo que hay que saber leer:

- **Qué no se relaja con la madurez** (D-18): definir objetivos, cambios de seguridad y accesos, gasto fuera de presupuesto, acciones externas (mensajes a clientes, proveedores, publicaciones) y lo irreversible (pagos, datos de clientes, borrado, migraciones destructivas). Lo irreversible exige siempre un validador externo (D-16).
- **Qué sí se relaja**: arquitectura, código, merge, deploy y remediación en producción, a medida que el agente acumula historial de aciertos ([[Modelo de madurez AI-Native]]). La remediación que resulta irreversible se rige por la fila de lo irreversible.
- **Reversible no alcanza**: que una acción se pueda deshacer es necesario pero no suficiente para que el agente la haga solo; además tiene que figurar como del agente en la matriz (D-06).

**Ejercicio 1.** Dada una lista de veinte acciones reales de un agente (abrir un PR, rotar una credencial, responder un ticket de cliente, revertir un deploy, borrar una rama, subir el límite de gasto), ubicar cada una en una fila de la matriz y justificar la ubicación. Las que no entran en ninguna fila se anotan como hallazgo: son las preguntas que la matriz todavía no contesta.

---

## 3. Los tres pilares operativos

### A. Límites de presupuesto

- **Definición**: reglas duras que impiden que los agentes consuman crédito sin límite.
- **Implementación**: tope de gasto por objetivo y por hora, y tope de iteraciones automáticas por objetivo. Un tope de reintentos antes de escalar a una persona (por ejemplo, 5) es una heurística [hipótesis], no un valor calibrado. En tiny teams, los topes de tiempo y costo de la ficha reemplazan la estimación ([[Núcleo ODLC para tiny teams]], D-08). El gasto fuera de presupuesto lo decide siempre un humano.

### B. Compuertas de aprobación humana (Human-in-the-Loop)

- **Definición**: puntos donde el agente pausa y espera que una persona apruebe antes de continuar.
- **Dónde van**: exactamente en las filas de la matriz que lo piden. IMDA (*Model AI Governance Framework for Agentic AI*, v1.5, 2026) recomienda concentrar la aprobación humana en puntos significativos (alto impacto, irreversibilidad, conducta atípica del agente) y denegar por defecto si falla la infraestructura de aprobación [guía].

### C. Registro de auditoría

- **Definición**: trazabilidad completa de las acciones del agente, con contexto, costo y evidencia.
- **Implementación**: cada cambio propuesto por un agente queda identificado con el agente que lo hizo y enlazado con la decisión de la [[Memoria organizacional]] que lo justifica. La comunicación entre agentes pasa por mensajes estructurados que quedan en el registro.

---

## 4. De la matriz al arnés: controles técnicos

La matriz dice quién decide; los controles hacen que el arnés la respete sin depender de que el agente se porte bien. El catálogo genérico está en [[Gobernanza#Controles técnicos]]; en este módulo se trabajan cuatro ideas de diseño:

1. **Interceptar antes y después de cada herramienta.** Antes, para frenar lo que la matriz no le asigna al agente; después, para contrastar lo que el agente afirma sobre el resultado (verificación de reclamos, [[Módulo 2 - Ingeniería de arneses]]).
2. **Respuesta graduada.** Cada control bloquea, advierte o solo registra según el riesgo, y se vuelve más estricto a medida que el proyecto pasa de exploración a producción. Se habla de "estado del proyecto" y no de "fase" para no confundirlo con las fases de ODLC ([[Registro de decisiones]], D-13).
3. **Defensa en profundidad.** Cada control cubre un riesgo distinto: la verificación de tests no cubre el sobrecosto, y el tope de gasto no cubre el reclamo falso. Apagar uno deja un punto ciego que los demás no cubren.
4. **Controles deterministas y controles con modelo.** Los chequeos aritméticos (gasto, cantidad de archivos tocados, radio de impacto) conviene hacerlos con código determinista: son baratos, rápidos y auditables. Los juicios semánticos (si una tarea está redactada con ambigüedad, si el agente hizo suposiciones) pueden delegarse a un modelo evaluador, con reglas escritas en prosa que se editan sin tocar código. La diferencia de latencia y costo entre los dos es un orden de magnitud sin medición publicada [hipótesis]. Un evaluador con modelo también se equivoca por exceso: los LLM marcan como no conforme código correcto (Jin y Chen, 2026) [medido].

**Ejercicio 2.** Para tres filas de la matriz (merge a main, acción externa, lo irreversible), escribir qué control del arnés la hace cumplir, en qué momento intercepta, qué hace si falla y cómo se prueba que el control funciona (sección 6).

---

## 5. El sesgo de automatización: cuando aprobar deja de supervisar

Poner un humano en la compuerta no garantiza que supervise. Frente a un agente que propone todo, la persona tiende a aceptar sin revisar: es el sesgo de automatización. Parasuraman y Manzey (2010) concluyen que no se previene con entrenamiento ni con instrucciones [medido, revisión]. Quienes se percibían responsables de justificar su estrategia verificaron más y cometieron menos errores de omisión y de comisión (Mosier, Skitka y otros, NASA, 1996) [medido, simulación de aviación]. Experimentar fallas de la automatización redujo la complacencia y los errores de omisión, pero no los de comisión (Bahner y otros, 2008, N = 24) [medido, muestra chica].

Consecuencias de diseño, desarrolladas en la Objeción 5 de [[Objeciones al marco]]:

- **Un "ok" no vale como aprobación**: la persona escribe el número que espera mover, elige entre opciones o marca qué cambiaría su veredicto. Las funciones de forzado cognitivo redujeron la sobreconfianza en la IA (Buçinca y otros, 2021, N = 199) [medido].
- **Medir la supervisión, no la motivación**: IMDA sugiere medir la tasa de rechazo o modificación y el tiempo de respuesta [guía]; aprobaciones en segundos y una tasa cercana al 100 % son señales de pasividad, sin umbrales validados [hipótesis].
- **Fallas sembradas**: errores conocidos en la cola de revisión miden cuántos atrapa cada revisor; la tasa sembrada tiene que ser baja, porque subirla destruye la confianza del operador (Bainbridge, 1983) [guía].
- **Responsabilidad sobre el proceso de verificación**, no solo sobre el resultado.

**Ejercicio 3.** Revisar el registro de aprobaciones de una semana (real o del caso de clase) y calcular tiempo mediano de aprobación y tasa de rechazo o modificación. Discutir qué haría falta para saber si esos valores indican un agente bueno o un humano pasivo.

---

## 6. La revisión en manos de agentes: qué se pierde y qué lo compensa

Cuando la ejecución se acelera, la revisión humana se vuelve cuello de botella o sello de goma, y la salida que empieza a defender la industria es pasar la revisión a agentes. La Objeción 8 de [[Objeciones al marco]] releva qué se pierde (independencia, porque los modelos se equivocan parecido; Goodhart, porque el escritor optimiza para pasar al revisor; habilidad humana de auditar) y qué lo compensa. En clase se trabajan las compensaciones con su respaldo:

| | Compensación | Respaldo | Límite |
|---|---|---|---|
| C4 | Verificación por ejecución con tests que el escritor no puede ver ni editar, y C7: no iterar al escritor contra la misma señal que lo juzga | [medido] Los tests ocultos bajaron la trampa casi a cero en ImpossibleBench; los de solo lectura bloquean la estrategia de modificarlos | Si el escritor ve o edita los tests, la verificación se infla |
| C5 | Acotar el radio de daño (la matriz fija qué toca el agente) | [guía] Google SRE: un canario al 5 % del tráfico con 20 % de errores da 1 % de errores globales | No mejora la calidad; no atrapa errores lentos |
| C1 | Auditoría humana por muestreo con presupuesto explícito, elegida por el sistema y no al azar | [medido, benchmark] En AI Control, con presupuesto para auditar 2 %, el azar dio 15 % de seguridad y la selección por un modelo confiable, 62 % | El 2 % es un parámetro del experimento, no una tasa validada en industria |
| C2 | Defectos sembrados para medir a los revisores | Parcial: Meta usa mutantes para medir suites de tests [medido], sin aplicación publicada a revisores | Un revisor agente puede aprender el patrón de siembra |
| C3 | Calibrar jueces contra etiquetas humanas | [medido] En Shopify, el juez pasó de kappa 0,02 a 0,61, con un techo de acuerdo entre humanos de 0,69 | Exige el juicio experto que se quería ahorrar; evitar que juzgue la misma familia que escribe |
| C6 | Diversidad deliberada de revisores | [medido] La votación en tríos de agentes bajó las fallas | Entre los modelos más capaces, cambiar de proveedor reduce poco la correlación |
| C8 | Mantener la habilidad humana con práctica deliberada | Parcial [medido]: quienes hacían preguntas conceptuales aprendieron más | Sin evidencia de que mantenga la habilidad de revisar |
| C9 | Responsabilidad sobre el diseño del sistema de revisión | [guía] Elish (2019); IMDA (2026); Reglamento de IA de la UE, art. 14 | Sin las métricas de C1 y C2 es una firma vacía |

Lectura: C4 y C5 son la base; C1, C2 y C3 forman un circuito de medición que solo funciona entero; C7 y C8 lo protegen; C9 sin ese circuito es una firma vacía. Quedan dos huecos sin respuesta: ningún estudio compara defectos en producción antes y después de sacar al humano de la revisión, y ninguna compensación reemplaza la comprensión compartida que producía la revisión humana.

El [[Núcleo ODLC para tiny teams]] aplica una versión mínima: revisor de dos pasadas sin revelar la autoría (P-07), ningún hallazgo aplicado sin un test que falle antes y pase después, y auditoría semanal elegida por un modelo distinto del escritor.

---

## 7. Verificar los controles: autoataque periódico

Un control que nunca se vio disparar da sensación de cobertura sin cobertura. Después de cada cambio de configuración del arnés se corre una suite propia de ataques controlados: inyecciones de prompt que buscan saltear las reglas, escrituras fuera del sandbox y loops de llamadas para comprobar que los topes cortan la sesión. El detalle técnico está en [[Módulo 4 - Ciberseguridad aplicada]].

---

## 8. Prácticas y herramientas de referencia

> [!warning] Setup previo
> Estas prácticas requieren los repositorios de referencia clonados en `external/` (carpeta fuera del control de versiones). Instrucciones de clonado en [[Recursos externos]].

- `external/gentleman-guardian-angel/`: revisor de código asistido por IA, agnóstico de proveedor (Claude, Gemini, Codex, Ollama y otros), escrito en Bash puro y sin dependencias. Se instala como hook de `pre-commit` y valida los archivos en *staging* contra los estándares declarados en el `AGENTS.md` del proyecto, aprobando o bloqueando el commit. Sirve como ejemplo de compuerta automática previa a que el cambio entre al repositorio, no de interceptación de llamadas a herramientas.
- **Práctica integradora**: tomar la matriz de [[Gobernanza]], elegir la herramienta de agentes que use el grupo y configurar para tres filas el control que la hace cumplir (ejercicio 2), con una prueba de autoataque por control.

---
Siguiente módulo: [[Módulo 4 - Ciberseguridad aplicada]]
Relacionado: [[Gobernanza]] · [[Objeciones al marco]] · [[Manifiesto HACS-ODLC]] · [[Recursos externos]] · [[Riesgos]]
