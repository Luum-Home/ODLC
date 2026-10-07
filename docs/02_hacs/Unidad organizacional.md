---
tags: [hacs, organizacion]
status: borrador
created: 2026-06-10
---

# Unidad organizacional

## Antes → Después

**Antes** (equipo tradicional): Product Manager, Architect, Developers, QA, DevOps.

**Después** (sistema HACS): **Humans + Agents + Memory + Governance.**

## ¿Qué cambia?

1. **Los roles dejan de mapear 1:1 a personas.** "QA" deja de ser una persona y pasa a ser una *capacidad* del sistema, ejercida mayormente por agentes ([[Roles de agentes]]) bajo supervisión humana ([[Gobernanza]]).
2. **La memoria deja de vivir en las cabezas.** En un equipo humano, el contexto se pierde con la rotación. En HACS, la [[Memoria organizacional]] es un componente de primera clase, no un subproducto.
3. **La coordinación deja de ser el costo dominante.** Los eventos de Scrum existen para la inspección y adaptación empírica de un equipo humano; con agentes cambia el costo de sincronizar, no la necesidad de inspeccionar.
4. **El humano sube de altitud.** De ejecutar tareas a definir intención, restricciones y criterios de éxito ([[Roles humanos]]). Esto supone un humano proactivo, y es un supuesto: Scrum compensaba la falta de iniciativa con sprints y compromisos, y ODLC tiene que diseñar para el humano de mínimo esfuerzo ([[Relectura del Manifiesto Ágil#El humano que no es proactivo]]).

## Hipótesis

- La carga cognitiva (concepto de Cognitive Load Theory, Sweller, 1988, aplicado a equipos por *Team Topologies*, Skelton y Pais, 2019) se redistribuye: los agentes absorben la carga *intrínseca* de ejecución; los humanos retienen la carga *germana* (en Team Topologies, la del dominio y el aprendizaje de alto valor, no la "de decisión"). La carga *extraña* es la del entorno y las herramientas. → hipótesis a validar.

## Preguntas abiertas

- ¿Qué reemplaza la disciplina externa que daban el sprint y la daily cuando el humano no es proactivo? (ver [[Relectura del Manifiesto Ágil]])

- ¿Cuál es el tamaño mínimo viable de un sistema HACS? ¿Un humano + N agentes ya califica?
- ¿Cómo se organizan *múltiples* unidades HACS entre sí? (el problema que SAFe intenta resolver para humanos — ver [[Comparativa con metodologías existentes]])
