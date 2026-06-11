---
tags: [recursos, cognitive-os, material-audiovisual, tokens, capacidad, costos, gobernanza]
status: borrador
created: 2026-06-10
fuente:
  tipo: video
  titulo: "La IA se queda SIN GASOLINA y lo vamos a pagar MUY CARO"
  canal: "Gustavo Entrala"
  url: "https://www.youtube.com/watch?v=ZsKszAkq0jI"
  consultado: 2026-06-10
---

# Análisis — Escasez de Tokens y la Crisis de Capacidad de la IA

> [!warning] Trazabilidad
> Esta nota contiene cifras muy específicas (uptime de Claude, cancelación de Sora, recortes de Gemini, pérdidas de OpenAI/Anthropic, medición de Singular sobre el peaje lingüístico, proyecciones de Goldman Sachs). Todas provienen del video, que a su vez cita fuentes secundarias, y **no fueron verificadas de forma independiente**. Leerlas como "según el video".

Este documento presenta un análisis y resumen estructurado del video referencial **"La IA se está quedando sin gasolina"** (disponible en [YouTube](https://www.youtube.com/watch?v=ZsKszAkq0jI)). El video aborda la crisis de capacidad de cómputo que afecta a los principales proveedores de IA, el racionamiento de tokens, el peaje lingüístico del español y la emergencia de una IA de dos velocidades.

---

## 1. Contexto: Degradación Percibida vs. Real

Usuarios de ChatGPT, Claude y otros modelos reportan de forma creciente una pérdida de calidad: respuestas más cortas, razonamiento más superficial y cortes inesperados. No es solo ruido en redes sociales; titulares de medios como el Wall Street Journal confirman que la IA está consumiendo tanta energía que se queda sin capacidad de cómputo. Las tarifas planas que prometían un "buffet libre" de inteligencia artificial han comenzado a imponer límites reales, incluso en cuentas de pago.

---

## 2. El Problema: Escasez de Tokens y Consumo Agéntico

El recurso escaso no es el petróleo, son los **tokens**. Cuando un usuario escribe a una IA, el modelo no lee palabras, lee fragmentos (tokens). El consumo escala drásticamente según el tipo de uso:

- **Consulta simple**: entre 500 y 1.000 tokens.
- **Sesión de trabajo de una hora con un agente**: entre 50.000 y 500.000 tokens.
- **IA agéntica**: consume entre **10 y 100 veces más** que una pregunta simple.

Es equivalente a pasar de encender una bombilla a poner en marcha una fábrica entera. Al mismo tiempo, hay más usuarios, más consultas y tareas cada vez más sofisticadas. El caso extremo conocido: un programador gastó casi **$15.000 USD en 2,5 horas** de sesión de IA. El CTO de Uber reportó que el presupuesto anual de IA de la empresa se agotó en solo 4 meses.

---

## 3. El Peaje Lingüístico del Español

Las IA no usan los mismos tokens en español que en inglés para expresar la misma idea. La empresa Singular ha medido que un mismo párrafo técnico consume **62 tokens en español** frente a **39 tokens en inglés**, un **59% más de consumo**. Esto significa que:

- Los usuarios hispanohablantes con planes gratuitos alcanzan sus límites antes.
- En planes con tope de tokens, el límite llega antes hablando en español.
- Cuando hay escasez de capacidad, los hispanohablantes lo notan primero y con más intensidad.

> **Implicación:** El español paga un peaje estructural en la economía de tokens, creando una desventaja sistémica para 500 millones de hispanohablantes.

---

## 4. Caso Anthropic/Claude: Uptime, Racionamiento y Esfuerzo de Razonamiento

La API de Claude ha registrado un **98,95% de uptime** durante algunas fases del año, acumulando casi **24 horas de cortes**. Marzo de 2026 fue el peor mes con **13 horas de caída** en un solo mes (el estándar del sector exige 99,99%, los "cuatro nueves"). Medidas concretas de Anthropic:

- **Racionamiento en horas pico**: límites de tokens impuestos entre las 5 y 11 AM Pacific (1 a 7 PM en España).
- **Mayor consumo por modelo**: Claude 4.7 consume un **46% más de tokens** que su predecesor por el mismo texto, reflejando el costo del razonamiento extendido.
- **Expansión de infraestructura**: Dario Amodei negoció con Elon Musk para albergar a Anthropic en Colossus, el centro de datos de xAI en Memphis.

---

## 5. Caso OpenAI/Sora y Google Gemini: Recortes Silenciosos

### OpenAI / Sora
- Sora fue **cancelada el 24 de marzo de 2026**, consumiendo casi **$1M en computación al día**.
- El acuerdo con Disney, valorado en más de **$1.000M**, fue cancelado.

### Google Gemini
- **4 recortes en 4 meses** sin aviso previo a usuarios.
- **Diciembre 2025**: la capa gratuita sufrió una caída del **92%** en capacidad.
- **Marzo 2026**: incluso los usuarios Ultra (máximo nivel de suscripción) fueron recortados.

> **Patrón:** Los proveedores ajustan la capacidad de forma opaca, sin comunicación transparente, erosionando la confianza del usuario.

---

## 6. Infraestructura Insuficiente

La inversión en centros de datos es masiva pero aún insuficiente:

- **$700.000 millones** invertidos este año para ampliar centros de datos.
- **Goldman Sachs** proyecta que la demanda superará la oferta en **10 GW de consumo eléctrico al año** hasta 2028.
- **Proyecto Stargate** ($500.000M) fue **suspendido** en Texas.

La infraestructura física (energía, refrigeración, chips) no escala al ritmo de la demanda de tokens, especialmente con el auge de la IA agéntica.

---

## 7. El Modelo Económico Insostenible

El modelo de tarifa plana ("buffet") no es financieramente viable:

- **OpenAI**: pérdidas estimadas de **$14.000M en 2026**.
- **Anthropic**: pérdidas estimadas de **$3.000M en 2025**.
- Solo el **5,5%** de los 900 millones de usuarios de ChatGPT pagan suscripción.
- Los usuarios intensivos consumen desproporcionadamente más recursos de los que paga su suscripción.

La tendencia apunta hacia **suscripciones más elevadas** para usuarios intensivos, modelos de pago por uso (taxímetro) y la eliminación progresiva de las tarifas planas ilimitadas.

---

## 8. IA de Dos Velocidades y Bucle de Desigualdad

La crisis de capacidad está creando una **IA de dos velocidades**: quienes más paguen tendrán acceso a más inteligencia, mejor rendimiento y mayor disponibilidad. Esto genera un bucle de desigualdad:

- El bien escaso ya no es la tierra ni el capital, es la **inteligencia**.
- Los hispanohablantes parten con un **hándicap estructural** (peaje lingüístico del 59%).
- Las organizaciones con presupuesto limitado quedan relegadas a modelos degradados o racionados.

---

## 9. Caminos de Democratización

El video menciona tres vías para contrarrestar la concentración:

1. **Modelos open source**: especialmente los provenientes de China, que ofrecen alternativas sin dependencia de proveedores centralizados.
2. **IA soberana**: infraestructura de cómputo propia por país o región para reducir la dependencia de hyperscalers.
3. **IA pública**: modelos financiados y operados como bien público.

Sin embargo, la tendencia dominante del mercado va en sentido contrario: concentración en pocos proveedores, opacidad en el racionamiento y precios crecientes.

---

## 10. Implicaciones para Gobernanza HACS y ODLC

Esta crisis de capacidad tiene implicaciones directas para el diseño de sistemas cognitivos humano-agente:

- **Diversificación de proveedores**: un Cognitive OS debe ser agnóstico al modelo y capaz de alternar entre proveedores según disponibilidad y costo ([[Análisis - Harness Engineering y la Paradoja de Herramientas]] demuestra que es posible con arneses bien diseñados).
- **Gestión eficiente de tokens**: la orquestación multi-agente con contextos destilados (no heredar el chat completo) y el límite del 40% de ventana de contexto son mecanismos de defensa directos contra la escasez.
- **Presupuesto de tokens como métrica de gobernanza**: los roles de gobernanza HACS deben contemplar el costo de tokens como restricción operativa, no solo la calidad de output.
- **Memoria externa como amortiguador**: persistir conocimiento en sistemas como [[Memoria organizacional|memoria persistente]] reduce la dependencia de re-procesar contexto costoso en cada sesión.
- **Evaluación del peaje lingüístico**: para equipos hispanohablantes, las métricas de Agent Cost deben considerar el sobrecosto estructural del idioma.

---
Relacionado: [[Cognitive OS - Arquitectura de referencia]] · [[Gobernanza]] · [[Recursos externos]] · [[Análisis - Harness Engineering y la Paradoja de Herramientas]] · [[Métricas de agentes]] · [[Memoria organizacional]] · [[Síntesis - Economía de tokens]] · [[Análisis - La Cultura del Token]] · [[Análisis - Token Economics y las 5 Predicciones del Caos]]