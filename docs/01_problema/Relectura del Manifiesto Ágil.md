---
tags: [problema, manifiesto, agile, hipotesis]
status: borrador
created: 2026-10-07
---

# Relectura del Manifiesto Ágil

HACS-ODLC no deroga el Manifiesto Ágil (2001): lo relee para equipos humano-agente. Lo que se rompe son **prácticas de métodos concretos** (los sprints de Scrum; story points y velocity, prácticas nacidas en XP y muy usadas por equipos Scrum, ausentes de The Scrum Guide 2020), no los valores del paraguas ágil. Esta nota recorre los 4 valores y los 12 principios uno por uno y declara qué se mantiene, qué se intensifica, qué se reemplaza y qué se invierte.

> [!note] Agile no es Scrum
> Agile es la declaración de valores y principios. **Scrum**, **XP** y **Kanban** son métodos que cuelgan de ella y no comparten supuestos: Scrum trabaja en iteraciones de tiempo fijo; Kanban no tiene iteraciones (flujo continuo, límites de WIP, sistema pull); XP aporta prácticas técnicas (TDD, integración continua, pair programming, releases chicas). Criticar "Agile" por los sprints es criticar a Scrum. Detalle por método: [[Comparativa con metodologías existentes]].

*Fuente: agilemanifesto.org y agilemanifesto.org/principles.html, consultados 2026-10-07. Los valores y principios se parafrasean; el texto original se verifica con:*

```bash
curl -sL https://agilemanifesto.org/principles.html | sed 's/<[^>]*>//g' | grep -v '^\s*$'
```

---

## Los 4 valores

| Valor ágil | Veredicto | En HACS-ODLC |
|---|---|---|
| Individuos e interacciones sobre procesos y herramientas | **Se divide** | Ver sección siguiente. |
| Software funcionando sobre documentación exhaustiva | **Se mantiene, refinado** | "Funcionando" no alcanza: tiene que lograr el objetivo (*Outcomes over Output*). *Memory over Documentation* desciende directamente de este valor ([[Manifiesto HACS-ODLC]]). |
| Colaboración con el cliente sobre negociación de contratos | **Se mantiene** | Pesa más: con ejecución barata, el cuello de botella es decidir qué se quiere ([[Nuevos cuellos de botella]], [[Fase 1 - Objective]]). |
| Responder al cambio sobre seguir un plan | **Se intensifica** | Replanificar con agentes es barato; la [[Fase 3 - Strategy]] produce un plan descartable, no un compromiso. |

### ¿Las herramientas pasan a estar por encima de las personas?

Hipótesis de esta nota: **no se invierte del todo; se divide según qué se esté haciendo.**

- **Para decidir, el valor se mantiene y se refuerza.** *Human Governance* dice lo mismo que el valor ágil: ni el proceso ni la herramienta deciden por el humano ([[Gobernanza]]).
- **Para ejecutar, se invierte.** Un agente no sostiene acuerdos tácitos ni recuerda la conversación de ayer. Lo que entre humanos se resolvía hablando, con un agente tiene que estar escrito: arnés, matriz de gobernanza, gates, memoria. En la ejecución, el proceso explícito y la herramienta valen más que la interacción informal ([[Cognitive OS - Arquitectura de referencia]]).
- **El agente no es una "herramienta" en el sentido de 2001.** En 2001 herramienta era el tracker o el IDE; el agente participa e interactúa. La dicotomía individuo/herramienta deja de ser limpia, y por eso el valor no se puede aplicar literal.
- **Riesgo:** que el proceso diseñado para agentes se derrame sobre los humanos y vuelva la ceremonia vacía que el [[Manifiesto HACS-ODLC]] dice evitar. El proceso explícito es para el agente; para el humano se mantiene el valor original.

---

## Los 12 principios

| # | Principio (parafraseado) | Veredicto | En HACS-ODLC |
|---|---|---|---|
| 1 | Satisfacer al cliente con entregas tempranas y continuas de software valioso | Se mantiene | "Valioso" pasa a significar outcome validado ([[Fase 5 - Validation]]). |
| 2 | Aceptar requisitos cambiantes, aun tarde | Se mantiene | El cambio cuesta menos; el límite es la capacidad humana de validar. |
| 3 | Entregar seguido, de semanas a meses, mejor cuanto más corto | Se mantiene; la escala quedó vieja | Hipótesis: con agentes la cadencia de entrega pasa a horas o días; se mide con el throughput de validaciones ([[Métricas operativas]]). |
| 4 | Negocio y desarrollo trabajan juntos a diario | Se intensifica | La decisión de negocio es el nuevo cuello de botella. |
| 5 | Proyectos alrededor de personas motivadas, con entorno y confianza | **Supuesto expuesto** | Ver [[#El humano que no es proactivo]]. Al agente no se le da confianza: se le da autonomía acotada ([[Gobernanza]]). |
| 6 | La conversación cara a cara es la forma más eficiente de transmitir información | **Se invierte para agentes** | Para un agente lo más eficiente es contexto escrito y persistente ([[Memoria organizacional]]). Entre humanos sigue valiendo. |
| 7 | El software funcionando es la medida principal del progreso | **Se reemplaza** | La medida es el outcome validado: *Objective Success Rate*, *Time To Outcome* ([[Métricas operativas]]). |
| 8 | Ritmo sostenible para sponsors, desarrolladores y usuarios | Se mantiene, más en riesgo | Los agentes trabajan sin pausa y la carga de revisión cae sobre el humano: fatiga de gobernanza ([[Preguntas abiertas]]). |
| 9 | Atención continua a la excelencia técnica y al buen diseño | Se intensifica | Contra el código inflado que los agentes producen estructuralmente ([[Software bloated]]). |
| 10 | Simplicidad: maximizar el trabajo no hecho | **Pasa a ser central** | Con costo marginal bajo y decreciente, no hacer es la disciplina difícil ([[Más código no es más velocidad]]). |
| 11 | Las mejores arquitecturas emergen de equipos autoorganizados | Se mantiene para humanos; condicional para agentes | La autoorganización de agentes está acotada por la matriz de gobernanza; el Nivel 5 del [[Modelo de madurez AI-Native]] es su extremo. |
| 12 | El equipo reflexiona a intervalos regulares y ajusta | Se mantiene | Es la [[Fase 6 - Learning]]; la diferencia es que aprende el sistema, no solo las personas. |

**Balance:** 9 de 12 principios siguen en pie (varios intensificados), uno se reemplaza (7), uno se invierte para agentes (6) y uno queda expuesto como supuesto (5). De los valores, tres se mantienen y el primero se divide.

---

## El humano que no es proactivo

El principio 5 asume personas motivadas. HACS hereda ese supuesto sin declararlo: "el humano sube de altitud" ([[Unidad organizacional]]) da por hecho alguien que toma la iniciativa. El supuesto tiene dos caras:

- **Evitar trabajo de más juega a favor.** Es el principio 10. Con agentes, el que tiende a hacer de más es el agente; un humano que frena lo innecesario actúa como control contra el [[Software bloated]].
- **No ser proactivo es el problema.** Los agentes absorben la ejecución, que era donde alguien poco proactivo igual aportaba. Lo que le queda al humano en HACS es iniciativa pura: formular el objetivo, decidir la estrategia, validar, curar la memoria. Con un humano pasivo:
  - el objetivo queda vago y el agente llena el vacío con output;
  - la validación se vuelve aprobación automática (sesgo de automatización);
  - la [[Fase 6 - Learning]] se saltea, como hoy se saltean las retros.
- **Scrum ya compensaba esto sin decirlo.** El sprint, el compromiso de sprint y la daily externalizan la disciplina: la estructura empuja cuando la persona no lo hace. Kanban depende de que alguien tire del trabajo (pull). ODLC saca los sprints y hasta ahora no ponía nada en su lugar.

Los seis principios de diseño para tolerar a este humano, con su respaldo en la literatura, están en [[Objeciones al marco#Principios para tolerar al humano de mínimo esfuerzo]].

**Principio de diseño que se deriva (propuesta):** ODLC se diseña para el humano de mínimo esfuerzo; el camino barato tiene que ser el correcto. Las compuertas siguientes se adoptan como **prácticas del [[Núcleo ODLC para tiny teams]]**, no como reglas de [[Fase 1 - Objective]] ni de [[Fase 6 - Learning]] ([[Registro de decisiones]], D-11).

- La plantilla de objetivo no permite arrancar sin métrica de éxito y dueño. [[Fase 1 - Objective]] pide ambos en sus reglas; en el núcleo, el tablero marca las fichas sin métrica o sin dueño.
- La validación no se aprueba sin evidencia adjunta. [[Fase 5 - Validation]] ya exige citar datos auditables (*Evidence over Opinions*); en el núcleo es la constancia de outcome.
- El agente propone, pero el humano escribe la métrica; aceptar con un "ok" no cuenta como decisión. En el núcleo, el dueño del objetivo fija el target.
- El cierre de ciclo no se registra sin la entrada de aprendizaje. [[Fase 6 - Learning]] no tiene esa compuerta; en el núcleo queda como extensión del piloto.

Esto es hipótesis, no práctica validada. Cómo medir si funciona queda en [[Preguntas abiertas]].

---
Relacionado: [[Manifiesto HACS-ODLC]] · [[Por qué fallan las metodologías actuales]] · [[Comparativa con metodologías existentes]] · [[Unidad organizacional]] · [[Gobernanza]]
