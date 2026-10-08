---
tags: [cursos, educacion, gobernanza, lideres, tecnico]
status: borrador
created: 2026-06-10
---

# Módulo 3 — Gobernanza de sistemas cognitivos (Híbrido)

Este módulo está dirigido tanto a líderes de proyecto como a ingenieros de software. Aprenderás a definir e implementar la **gobernanza de autonomía**, asegurando que los agentes autónomos operen dentro de límites financieros, éticos y técnicos seguros.

---

## 1. El Concepto de Gobernanza Humana (Human Governance)

El quinto valor del [[Manifiesto HACS-ODLC]] establece que **los humanos lideran la estrategia y deciden los límites de riesgo, mientras que los agentes analizan y ejecutan**. 

Un sistema sin gobernanza (donde un agente puede desplegar a producción sin revisión o realizar compras de servidores de forma autónoma) es altamente inestable y peligroso para la organización.

---

## 2. Los Tres Pilares de la Gobernanza de Agentes

### A. Límites de Presupuesto (Cost Caps)
- **Definición**: Reglas duras de software que impiden que los agentes consuman créditos ilimitados en llamadas a modelos de lenguaje (LLM).
- **Implementación**: 
  - Límite de dólares ($) de tokens por ciclo de objetivo.
  - Límite de cantidad de iteraciones automáticas por objetivo (ej. no más de 5 reintentos automáticos en compilación).

### B. Compuertas de Aprobación Humana (Human-in-the-Loop - HITL)
- **Definición**: Puntos del ciclo de desarrollo donde el agente debe pausar su ejecución y esperar que un humano valide y firme la acción antes de continuar.
- **Acciones obligatorias HITL**: este módulo no mantiene una lista propia. La fuente única de qué acciones requieren aprobación humana es la matriz de [[Gobernanza#Límites de autonomía (matriz borrador)|Gobernanza § Límites de autonomía]]. Lo irreversible (pagos, datos de clientes, borrado, migraciones destructivas) frena siempre, en cualquier nivel de madurez ([[Registro de decisiones]], D-01).

### C. Registro de Auditoría (Audit Trails)
- **Definición**: Trazabilidad completa de las acciones del agente.
- **Implementación**: Cada cambio de código propuesto por un agente en Git debe ir firmado con su ID de agente y linkeado con la decisión arquitectónica en la [[Memoria organizacional]] que lo justifica.

---

## 3. La Malla de Seguridad de 14 Capas (14-Layer Safety Mesh)

La gobernanza técnica en la arquitectura de [[Cognitive OS - Arquitectura de referencia]] no depende de un único punto de control. En su lugar, implementa una **Malla de Seguridad de 14 Capas (Safety Mesh)**, una serie de interceptores independientes ejecutados en el ciclo de vida de las herramientas (`PreToolUse` y `PostToolUse`).

### Estructura de la Malla de Seguridad

| Capa | Componente / Hook | Tipo | Momento | Objetivo de Contención / Prevención | Comportamiento |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | `clarification-gate.sh` | Semántico | Pre-Launch | Bloquea tareas redactadas con ambigüedad extrema antes de ejecutarlas. | **BLOCK** si puntaje > 60 |
| **2** | `blast-radius.sh` | Determinista | Pre-Launch | Advierte sobre el impacto estimado de la tarea en archivos/directorios. | **WARN** (informativo) |
| **3** | `dry-run-preview.sh` | Determinista | Pre-Launch | Ejecución simulada para validar planes sin consumir recursos. | **BLOCK** si `DRY_RUN=true` |
| **4** | `rate-limiter.sh` | Determinista | Pre-Tool | Evita loops infinitos de llamadas de API y sobrecostos financieros. | **BLOCK** si excede límites |
| **5** | `scope-proportionality.sh`| Determinista | Post-Tool | Evita que un arreglo menor se convierta en una reescritura masiva. | **BLOCK** si es desproporcional |
| **6** | `claim-validator.sh` | Determinista | Post-Tool | Valida en el sistema de archivos las afirmaciones de tests y creación de archivos. | **BLOCK** en producción si hay fallas |
| **7** | `assumption-tracker.sh` | Semántico | Post-Tool | Detecta y registra suposiciones lingüísticas hechas por el agente. | **WARN** si hay 3+ suposiciones |
| **8** | `trust-score-validator.sh`| Determinista | Post-Tool | Asegura la presencia y correcto formato de reportes de confianza. | **WARN** si falta el Trust Report; **BLOCK** (exit 2) si está malformado |
| **9** | `confidence-gate.sh` | Determinista | Post-Tool | Bloquea la propagación de resultados si el score de confianza es bajo. | **BLOCK** en producción si score < 50 |
| **10**| `clarification-interceptor.sh`| Semántico | Post-Tool | Intercepta marcas de ambigüedad a mitad del objetivo para guiar al usuario. | **LOG** + Señal al orquestador |
| **11**| `auto-rollback-trigger.sh`| Determinista | Post-Tool | Revierte automáticamente los cambios a un estado limpio tras fallar retries. | **BLOCK** + Git Revert |
| **12**| `cos_lib/cross_verifier.py` | Semántico | On-Demand | Un segundo modelo de lenguaje audita y verifica el resultado del primero. | Llamada de biblioteca |
| **13**| `reinvention-check.sh` | Semántico | Post-Tool | Evita duplicar código al advertir si ya existe una solución en el sistema. | **WARN** + Sugerencia de reúso |
| **14**| `cos_lib/memory_scanner.py` | Determinista | Antes de persistir en memoria | Escanea el contenido que se va a guardar en memoria (prompt injection, secuestro de rol, exfiltración de credenciales, Unicode invisible) y lo marca como bloqueado si encuentra amenazas. | Llamada de biblioteca |

> [!note] Capa 14: código vs. documentación del repo
> La descripción de la Capa 14 sigue el código de `cos_lib/memory_scanner.py` (escaneo de seguridad antes de persistir). La tabla de `docs/04-Concepts/root/safety-mesh.md` del propio repo le atribuye otra función: detectar memorias viejas o contradictorias al inicio de sesión.

---

### Principios de Diseño de la Malla (Defensa en Profundidad)

1. **Independencia de Capas**: Cada capa atiende a un riesgo diferente. Deshabilitar una capa genera una vulnerabilidad ciega que el resto de los filtros no pueden subsanar (ej. la verificación de tests no soluciona el riesgo de sobrecosto del `rate-limiter`).
2. **Degradación Gradual (Spectrum of Control)**: No todos los filtros detienen al agente. Se clasifican según su impacto:
   - **BLOCK**: Detención inmediata de la ejecución (Capas 1, 3, 4, 5, 11).
   - **WARN**: Advertencia al operador humano, permitiendo continuar (Capas 2, 7, 13).
   - **LOG**: Registro silencioso en `.cognitive-os/metrics/` para auditoría y aprendizaje del sistema (Capa 10).
   - **WARN o BLOCK según el reporte**: la Capa 8 (`trust-score-validator.sh`) advierte si falta el Trust Report y bloquea (exit 2) si está malformado.
   - **Dependiente del estado del proyecto**: las Capas 6 (`claim-validator.sh`) y 9 (`confidence-gate.sh`) alertan/loguean en estados permisivos y **bloquean** en Producción/Mantenimiento (ver Phase Awareness, punto 3).
   - **Sin clasificar**: las Capas 12 (`cos_lib/cross_verifier.py`) y 14 (`cos_lib/memory_scanner.py`) se invocan como llamadas de biblioteca (On-Demand y antes de persistir en memoria, respectivamente) y todavía no están categorizadas dentro del espectro. *Pendiente de definición del autor antes del dictado.*
3. **Sensibilidad al estado del proyecto (Phase Awareness)**: El comportamiento de la malla se adapta al estado del proyecto definido en `cognitive-os.yaml`. Se dice "estado" y no "fase" para no confundirlo con las fases de ODLC ([[Registro de decisiones]], D-13):
   - En los estados de **Reconstrucción** o **Estabilización**, los ganchos de control son más permisivos (alertas prioritarias sobre bloqueos) para acelerar el desarrollo.
   - En los estados de **Producción** o **Mantenimiento**, los ganchos de control se tornan estrictamente prohibitivos para proteger la estabilidad operativa.

---

## 4. Gobernanza Basada en Prompts (Prompt-Driven Governance)

Tradicionalmente, los ganchos de gobernanza se programaban de forma imperativa (ej. scripts en Bash con complejas expresiones regulares de `grep -E`). No obstante, la arquitectura moderna de gobernanza introduce el paradigma de **Prompt-Driven Governance**.

### ¿Por qué migrar a Prompts en Gobernanza?
- **Juicio Semántico**: Expresiones como "I think" o "Probably" a veces denotan razonamiento válido basados en pruebas de compilador, y no necesariamente suposiciones ciegas. Un script determinista de regex bloquea indiscriminadamente. Un prompt evaluado por un modelo rápido como *Claude Haiku* diferencia el contexto lingüístico real.
- **Mantenibilidad en Prosa**: Cambiar las reglas de aceptación o los umbrales de ambigüedad implica editar instrucciones en Markdown en lugar de refactorizar scripts Bash y depurar caracteres de escape.
- **Arquitectura Híbrida**: Los controles aritméticos rápidos (como el presupuesto de API o conteo de archivos modificados) se mantienen en Bash determinista por eficiencia (órdenes de magnitud sin medición publicada: latencia <100ms, costo \$0). Las evaluaciones cognitivas subjetivas (como calidad de intenciones o detección de supuestos) se delegan secuencialmente a prompts semánticos (órdenes de magnitud sin medición publicada: latencia de 1 a 2s, costo aproximado de \$0.0005 por llamada).

---

## 5. Simulación de Ataques y Auditoría de Malla (`/pentest-self`)

Para garantizar que ningún cambio en la configuración de la malla de gobernanza debilite los controles, se utiliza la suite automatizada de pruebas de penetración autónoma `/pentest-self`. Este comando simula ataques semánticos y técnicos sobre el propio entorno:
- Probar inyecciones de prompts diseñadas para forzar el modo administrador.
- Intentar escrituras en áreas fuera del Sandbox asignado.
- Provocar loops de llamadas continuas para validar la efectividad del `rate-limiter`.

---

## 6. Ejercicios Prácticos y Herramientas de Referencia

> [!warning] Setup previo
> Estas prácticas requieren los repositorios de referencia clonados en `external/` (carpeta fuera del control de versiones). Instrucciones de clonado en [[Recursos externos]].

En la carpeta `external/` cuentas con herramientas de referencia clave (ver [[Recursos externos]]):
- `external/gentleman-guardian-angel/`: Un revisor de código asistido por IA, agnóstico de proveedor (Claude, Gemini, Codex, Ollama y otros), escrito en Bash puro y sin dependencias. Se instala como hook de `pre-commit` y valida los archivos en *staging* contra los estándares declarados en el `AGENTS.md` del proyecto, aprobando o bloqueando el commit. Sirve como ejemplo de compuerta automática en el ciclo de vida —un control preventivo antes de que el cambio entre al repositorio—, no de interceptación de llamadas al sistema.
- **Implementación de Referencia en luum-cognitive-os**: Puedes estudiar los flujos y esquemas declarativos en los repositorios públicos de referencia para observar la configuración del orquestador en `cognitive-os.yaml` y el código fuente de los interceptores pre y post-ejecución.

---
Siguiente módulo: [[Módulo 4 - Ciberseguridad aplicada]]
Relacionado: [[Gobernanza]] · [[Manifiesto HACS-ODLC]] · [[Recursos externos]] · [[Riesgos]] · [[Cognitive OS - Arquitectura de referencia]]

