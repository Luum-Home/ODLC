---
tags: [fundacional, estrategia, historia]
status: borrador
created: 2026-10-08
---

# Cómo nacieron los marcos que se adoptaron

Un vault que solo junta objeciones no le cambia la forma de trabajar a nadie. Esta nota mira cómo nacieron los marcos que sí se adoptaron, para sacar de ahí el camino que tiene que seguir ODLC.

| Marco | Cómo nació |
|---|---|
| **XP** | Kent Beck en un proyecto real (el C3 de Chrysler, 1996); el libro *Extreme Programming Explained* en 1999. |
| **Scrum** | Jeff Sutherland en su empresa (1993); el paper "SCRUM Development Process" de Ken Schwaber se presentó en OOPSLA 1995 (publicado en las actas en 1997). |
| **Kanban** | David J. Anderson con equipos concretos en Microsoft y Corbis; el libro *Kanban* en 2010. |
| **Team Topologies** | Años de consultoría de Matthew Skelton y Manuel Pais; el libro en 2019. |
| **Squads y tribes** | El whitepaper *Scaling Agile @ Spotify* de Henrik Kniberg y Anders Ivarsson (2012). Ex integrantes de Spotify contaron después que el modelo fue aspiracional y nunca se implementó del todo (Jeremiah Lee, "Spotify's Failed #SquadGoals", 2020, que cita a un agile coach de la empresa). |

*Verificación (2026-10-08):*

```bash
curl -sL "https://api.crossref.org/works?query.bibliographic=SCRUM+Development+Process+Schwaber+OOPSLA&rows=1&select=title,issued"
curl -sL -A Mozilla/5.0 https://www.jeremiahlee.com/posts/failed-squad-goals/ | sed 's/<[^>]*>/ /g' | grep -o "never fully implemented"
```

Las fechas de XP, Kanban y Team Topologies salen de sus libros, citados como fuente canónica en [[Comparativa con metodologías existentes]].

---

## Tres cosas en común

1. **Salieron de un equipo haciendo algo distinto, no de un debate.** Primero la práctica, después el nombre.
2. **Son un conjunto chico de elementos concretos y con nombre, aplicables el lunes.** XP tenía 12 prácticas en su primera edición. Scrum, en *The Scrum Guide* 2020, tiene 3 responsabilidades, 5 eventos y 3 artefactos. El *Kanban Method* de Anderson tiene 6 prácticas generales, con el límite de WIP como idea central. Team Topologies, 4 tipos de equipo y 3 modos de interacción. ODLC, en cambio, tiene 6 fases, 6 valores, matrices y niveles de madurez pensados para una empresa grande, y nada que una persona sola pueda arrancar mañana.
3. **Ninguno tenía evidencia al nacer.** En la revisión sistemática de Dybå y Dingsøyr (2008), de 1.996 estudios sobre desarrollo ágil solo 36 eran empíricos, años después de la adopción masiva ([[Propuestas existentes - Objeciones 3 y 4]]). Exigir evidencia completa antes de proponer es más de lo que cumplió cualquiera de ellos. La condición de que ODLC sea demostrable se cumple igual si la propuesta nace junto con su piloto, como XP en el C3.

---

## Lo que ODLC tiene de nuevo

La crítica sirvió para encontrar qué aporta ODLC que ninguno de los marcos anteriores tiene:

- **La unidad de trabajo humano + agentes**, en lugar de un equipo de personas.
- **Diseñar para el humano de mínimo esfuerzo.** Los marcos anteriores suponen gente motivada; los principios de tolerancia de [[Objeciones al marco#Principios para tolerar al humano de mínimo esfuerzo]] no.
- **Verificar por ejecución en lugar de por lectura**, con el humano auditando el sistema de revisión.
- **Medir si cada acto humano hizo su trabajo** (métricas de pasividad, fallas sembradas), en lugar de medir esfuerzo o velocidad.
- **Asumir que decidir y validar se aceleran mucho menos que ejecutar** y organizar el método alrededor de eso ([[Objeciones al marco#Objeción 7: lo que no se acelera]]).

Eso puede ser para ODLC lo que el límite de WIP fue para Kanban: la idea central que lo distingue. Son hipótesis hasta que el piloto las pruebe.

---

## El camino que se sigue

1. Destilar un núcleo chico, con nombre y aplicable el lunes: [[Núcleo ODLC para tiny teams]].
2. Correrlo en un caso real con protocolo pre-registrado: [[Piloto - Combinación A]]. Es el equivalente del C3 para XP.
3. Las objeciones y los relevamientos quedan como el respaldo de cada práctica, que es lo que XP y Scrum no tuvieron al nacer.

---
Relacionado: [[Objeciones al marco]] · [[Comparativa con metodologías existentes]] · [[Piloto - Combinación A]] · [[Núcleo ODLC para tiny teams]]
