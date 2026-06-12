---
tags: [problema, ia, frontend, ux, qa, validacion]
status: semilla
created: 2026-06-12
---

# Defectos perceptuales generados por IA

Los agentes de IA pueden producir interfaces que **compilan**, pasan tests unitarios básicos e incluso se ven correctas en una captura estática, pero fallan durante el uso real. Estos defectos no siempre rompen el build; rompen la percepción de estabilidad, confianza y calidad.

El ejemplo arquetípico es el **flickering**: una pantalla, componente, skeleton, modal, lista o estado de carga que parpadea, aparece y desaparece, cambia de tamaño o se re-renderiza de forma visible para el usuario.

## Tesis

El frontend generado por IA tiende a optimizar la apariencia estática del resultado, no necesariamente la continuidad perceptual de la interacción.

Esto expone una limitación de los gates tradicionales:

- el código puede compilar;
- los tests pueden pasar;
- una captura puede verse bien;
- el usuario igual puede percibir la interfaz como rota.

En términos de [[ODLC]], esto es una falla de [[Fase 5 - Validation]]: se validó la implementación, pero no se validó el resultado experimentado por el usuario.

## Definición

Un **defecto perceptual** es una falla observable durante la interacción que afecta la confianza, claridad o continuidad de la experiencia, aunque no necesariamente produzca un error técnico explícito.

No se limita a defectos visuales. Incluye cualquier comportamiento que el usuario percibe como inestable, errático o inconsistente.

## Ejemplos frecuentes

### Flickering y parpadeo

- Skeletons que aparecen después del contenido.
- Spinners que parpadean en cargas menores a 100–200 ms.
- Componentes que muestran estado vacío antes de hidratar datos.
- Transiciones que alternan entre loading, empty y loaded.
- Modales o popovers que se abren y cierran por re-render.

### Layout shift

- Tarjetas que saltan al cargar imágenes o fuentes.
- Tablas que cambian de ancho al llegar datos.
- Botones que se mueven al aparecer validaciones.
- Header o sidebar que cambian de altura entre estados.

### Estados inconsistentes

- Botones habilitados mientras una acción sigue pendiente.
- Doble submit por falta de estado `pending`.
- Formularios que pierden foco durante re-render.
- Filtros que muestran resultados viejos con loading nuevo.
- Optimistic UI sin rollback visible cuando falla la operación.

### Defectos de interacción

- Clicks que no hacen nada aunque el componente parezca activo.
- Áreas clickeables demasiado pequeñas.
- Modales sin escape/cierre consistente.
- Navegación con scroll inesperado.
- Estados hover/focus/tap inconsistentes entre desktop y mobile.

### Defectos responsive y de accesibilidad

- Interfaces correctas en desktop pero rotas en mobile.
- Orden de tabulación incorrecto.
- Foco invisible.
- Contraste insuficiente.
- Lectores de pantalla con labels ambiguos o ausentes.

### Inconsistencia de diseño

- Componentes generados fuera del design system.
- Variaciones innecesarias de spacing, radius, sombras o tipografía.
- Microcopys que no siguen el tono del producto.
- Animaciones decorativas que distraen o degradan performance.

## Por qué la IA los produce

### 1. Optimiza para plausibilidad local

El agente genera una solución que parece razonable en el contexto inmediato. Si no se le exige validar interacción real, puede resolver solo el estado feliz.

### 2. No percibe continuidad temporal

Una captura estática no muestra flickering, pérdida de foco, loading jitter ni transiciones erráticas. Muchos defectos perceptuales solo aparecen en el tiempo.

### 3. Subestima estados intermedios

Los agentes suelen modelar:

- estado inicial;
- estado con datos;
- estado de error.

Pero fallan en estados intermedios:

- hidratación;
- refetch;
- optimistic update;
- pending concurrente;
- datos parcialmente disponibles;
- latencia variable;
- navegación durante carga.

### 4. Mezcla patrones incompatibles

Puede combinar Suspense, loaders, client state, server state, optimistic UI y efectos manuales sin una estrategia clara de ownership del estado.

### 5. No respeta constraints visuales implícitos

Si el design system, los tokens, las reglas de motion o los patrones de loading no están explicitados en [[Fase 2 - Constraints]], el agente inventa.

## Por qué los tests tradicionales no alcanzan

Los tests unitarios y de integración detectan lógica rota, pero muchos defectos perceptuales requieren observar el sistema como usuario.

| Gate | Qué detecta | Qué puede no detectar |
|---|---|---|
| Typecheck/build | Errores estáticos | Flickering, layout shift, pérdida de foco |
| Unit tests | Lógica local | Continuidad entre estados |
| Screenshot estático | Apariencia puntual | Parpadeo, interacción, timing |
| E2E básico | Flujos felices | Jitter visual, estados transitorios |
| QA humana | Percepción real | Puede ser tardía, costosa o inconsistente |

## Validación recomendada

Los defectos perceptuales requieren una capa de validación orientada a experiencia:

- **Smoke visual interactivo**: abrir la pantalla real, navegar, clickear y observar transiciones.
- **E2E con latencia simulada**: probar loading, refetch, errores y acciones lentas.
- **Captura de video o trace**: revisar secuencias, no solo screenshots.
- **Visual regression testing**: detectar layout shift y diferencias inesperadas.
- **A11y checks**: validar foco, contraste, labels, navegación por teclado.
- **Performance UX**: medir CLS, INP, LCP y duración de estados de carga.
- **Design-system conformance**: verificar tokens, componentes permitidos y patrones de motion/loading.

## Implicación para HACS-ODLC

En un sistema [[HACS]], el agente no debe declarar éxito solo porque:

- compiló;
- pasó tests;
- generó una pantalla;
- adjuntó una captura.

Debe producir evidencia de que la interfaz funciona en interacción real. Esto conecta con:

- [[Fase 2 - Constraints]]: declarar reglas visuales, accesibilidad, responsive, motion y loading.
- [[Fase 4 - Execution]]: instrumentar estados de UI y generar tests/fixtures de latencia.
- [[Fase 5 - Validation]]: validar experiencia real, no solo implementación.
- [[Métricas de agentes]]: contar defectos perceptuales como retrabajo, aunque no sean errores de compilación.

## Señales de alerta

- El agente entrega solo screenshots estáticos.
- El PR no incluye estados loading/error/empty.
- No hay prueba con latencia simulada.
- Los componentes no usan el design system.
- Hay `useEffect` para sincronizar estados derivados sin justificación.
- Se mezclan estados locales y server state sin ownership claro.
- No se prueba mobile/keyboard.
- El agente dice “se ve bien” sin evidencia reproducible.

## Decisión

Los defectos perceptuales deben tratarse como defectos reales de producto, no como “detalles de polish”.

En trabajo generado por agentes, una UI no está validada hasta que exista evidencia mínima de:

1. estado feliz;
2. loading;
3. error;
4. empty state;
5. interacción básica;
6. responsive/mobile;
7. foco/teclado/accesibilidad básica;
8. ausencia de flickering o layout shift perceptible.

## Preguntas abiertas

- ¿Qué umbral de flickering o layout shift vuelve un objetivo “fallido” en [[Fase 5 - Validation]]?
- ¿Cómo medir defectos perceptuales dentro del *Rework Rate* sin convertir toda preferencia estética en error?
- ¿Debe existir un agente especializado en QA perceptual o UX probabilístico dentro de [[Roles de agentes]]?
- ¿Qué parte debe ser validación determinística y qué parte revisión humana?

---
Relacionado: [[Producción de software vs. velocidad real]] · [[Fase 5 - Validation]] · [[Métricas de agentes]] · [[Nuevos roles profesionales en la era de IA]]
