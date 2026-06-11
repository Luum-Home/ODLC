---
tags: [referencias, laboratorio, rag, agent-runtime, clean-architecture, mcp, frameworks, nem, testing]
status: borrador
created: 2026-06-10
fuente:
  tipo: repositorio
  titulo: "AI Engineering Lab"
  autor: "MatiasNAmendola"
  url: "https://github.com/MatiasNAmendola/ai-engineering-lab"
  consultado: 2026-06-10
---

# AI Engineering Lab — Repositorio de Referencia (Análisis Exhaustivo)

El **Laboratorio de Ingeniería de IA** (disponible en [MatiasNAmendola/ai-engineering-lab](https://github.com/MatiasNAmendola/ai-engineering-lab)) es un repositorio de referencia técnico desarrollado bajo una filosofía de primeros principios (*bottom-up*). Su propósito es desmitificar los frameworks comerciales modernos mediante la implementación **desde cero y sin dependencias externas** de las primitivas de inferencia, RAG, runtimes de agentes, observabilidad y gobernanza de seguridad.

Este documento ofrece un **análisis exhaustivo y de bajo nivel** de todos los componentes, scripts, sandboxes, infraestructura, testing e investigaciones contenidas en el laboratorio.

---

## 1. Estructura del Vault de Conocimiento (Estilo Karpathy)

El repositorio está organizado siguiendo la metodología de **Obsidian Vault / LLM Wiki** recomendada por Andrej Karpathy para bases de código co-mantenidas por agentes de IA:

### 1.1 Archivos de Configuración y Rieles Operativos

*   **`CLAUDE.md`** (71 líneas): Manual de directrices y rieles operativos en la raíz. Define la estructura del vault (`/raw`, `/wiki`, `/external`), el flujo de compilación (Ingesta → Destilación → Compilación → Mantener Coherencia), guías de codificación (Think First, Simplicidad, Cambios Quirúrgicos, Consistencia) y comandos de ejecución por lenguaje (`uv` para Python, `bun` para TypeScript, `go` nativo para Go). Instruye a los agentes sobre cómo estructurar el código y la suite de testing.
*   **`AGENTS.md`**: Guía complementaria para agentes de IA con reglas específicas de mantenimiento del repositorio.
*   **`CONTRIBUTING.md`**: Guía de contribución para desarrolladores humanos y agentes.
*   **`README.md`** (276 líneas): Documento principal del repositorio con visión general, principios de diseño por componente (SOLID, KISS, Clean), guías de aprendizaje enlaces a la wiki, paisaje de la Ingeniería de IA con diagrama Mermaid, ecosistema de frameworks, tabla "Lo que pocos comentan" (retos de ingeniería críticos), filosofía arquitectónica del CTO, enlaces oficiales de motores de bases de datos, guía de ejecución por lenguaje, infraestructura local y calidad, y referencias.
*   **`Makefile`** (39 líneas): 11 targets de automatización:
    *   `check`: Ejecuta lint, typecheck, typecheck-ts y test en secuencia
    *   `lint`: `uvx ruff check .`
    *   `typecheck`: `uv run --with mypy mypy 00_primitives_scratch/`
    *   `typecheck-ts`: `cd 02_typescript_frameworks && bun x tsc --noEmit`
    *   `test`: `uv run --project 01_python_frameworks --with pytest pytest tests/ -v`
    *   `test-textbook`: Tests específicos del Textbook Generator
    *   `test-primitives`: Tests específicos de las primitivas
    *   `serve` / `serve-textbook`: Levanta el servidor FastAPI con uvicorn en puerto 8000
    *   `hook`: Instala el pre-commit hook
    *   `install-ts`: Instala dependencias TypeScript con bun
    *   `clean`: Limpia cachés de Python (__pycache__, pytest, mypy, ruff)
*   **`Dockerfile`**: Configuración de imagen Docker para contenerizar los servidores MCP.
*   **`docker-compose.yml`** (48 líneas): Orquesta 3 servicios:
    *   `db`: PostgreSQL 16 con extensión pgvector (imagen `pgvector/pgvector:pg16`), volumen persistente `pgdata`, healthcheck cada 5s
    *   `mcp-education`: Servidor MCP de Plataforma Educativa (puerto 8000), depende de `db` healthy
    *   `mcp-wallet`: Servidor MCP de Virtual Wallet (puerto 8001), depende de `db` healthy
*   **`.pre-commit-config.yaml`**: Configuración de hooks de pre-commit para validación automática.
*   **`.gitignore`**: Excluye `.venv/`, `node_modules/`, `__pycache__/`, `external/` (12 repos clonados), `*.db`, entre otros.

### 1.2 Directorios Principales

*   **`/00_primitives_scratch/`**: 5 scripts standalone de Python (~200 líneas cada uno) que implementan primitivas de IA desde cero sin dependencias externas.
*   **`/01_python_frameworks/`**: 15 demos de frameworks Python evaluados.
*   **`/02_typescript_frameworks/`**: 3 demos de frameworks TypeScript (Mastra, Flue, Pi).
*   **`/03_go_frameworks/`**: 1 demo de framework Go (Gollem).
*   **`/textbook_generator/`**: Aplicación principal de producción (Clean Architecture).
*   **`/tests/`**: Pirámide de testing completa (unit, integration, e2e, atdd, browser).
*   **`/wiki/`**: 13 artículos técnicos estructurados.
*   **`/raw/`**: Bandeja de entrada inmutable con requisitos brutos y transcripciones.
*   **`/scripts/`**: Scripts de automatización (`local_check.sh`, `deploy_mcp.sh`).
*   **`/external/`**: 12 repositorios de referencia clonados (gitignored).
*   **`/.atl/`**: Contexto SDD (Spec-Driven Development).

---

## 2. Primitivas Técnicas desde Cero (`00_primitives_scratch/`)

El núcleo educativo del laboratorio reside en sus scripts standalone de Python, diseñados con principios de simplicidad (KISS), You Aren't Gonna Need It (YAGNI) y responsabilidad única (SRP). Cada script tiene ~200 líneas y es auto-contenido.

### 2.1 Inferencia de LLMs y Protocolos de Red (`01_llm_inference_scratch.py`)

**Extensión**: ~286 líneas  
**Dependencias**: Cero (solo librería estándar de Python)  

Implementa la mecánica fundamental de interacción con modelos de lenguaje:

*   **Conexión HTTP Cruda**: Realiza llamadas directas a APIs de proveedores utilizando `urllib.request` sin envoltorios SDK. Construye los requests manualmente con headers, autenticación Bearer y payloads JSON.
*   **Server-Sent Events (SSE)**: Implementa un parser iterativo para consumir streams de texto token por token. Lee el stream línea por línea, parsea eventos del formato `data: {...}`, extrae el delta de contenido y renderiza incrementalmente en stdout.
*   **Cost Tracker en Tiempo Real**: Multiplica los tokens de entrada y salida reportados en la respuesta por las tarifas vigentes del modelo. Incluye tabla de precios de junio 2026:
    *   GPT-5.5: \$2.50/1M input, \$10.00/1M output
    *   Claude Opus 4.8: \$15.00/1M input, \$75.00/1M output
    *   Gemini 2.5 Pro: \$3.50/1M input, \$10.50/1M output
    *   MiniMax M3: \$0.40/1M input, \$1.60/1M output
*   **Structured Output Parsing**: Fuerza respuestas JSON mediante tool calling nativo del proveedor, eliminando parses manuales sobre texto libre.
*   **Soporte Multi-Proveedor**: Implementa adaptadores para OpenAI, Anthropic, Google y MiniMax con normalización de respuestas.

### 2.2 RAG y PGVector (`02_rag_postgres_pgvector.py`)

**Extensión**: ~268 líneas  
**Dependencias**: Cero (cosine similarity en Python puro)  

Pipeline completo de Retrieval-Augmented Generation:

*   **Similitud Coseno en Python Puro**: Implementa el producto punto normalizado sin NumPy:
    $$\text{Similitud Coseno}(A, B) = \frac{\sum_{i=1}^{n} A_i \cdot B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \cdot \sqrt{\sum_{i=1}^{n} B_i^2}}$$
*   **Sliding Window Chunking**: Divide el texto en ventanas superpuestas para preservar contexto entre chunks adyacentes (overlap configurable).
*   **Semantic Chunking**: Divide el texto en oraciones individuales, calcula embeddings para cada una y agrupa oraciones contiguas en un solo chunk mientras su similitud coseno se mantenga por encima de un umbral dinámico (ej: 0.85).
*   **Postgres DDL con PGVector**: Configura tablas con columnas de tipo `vector(n)`, índices HNSW para búsqueda aproximada, y filtros de metadatos.
*   **SQL Querying con Operador `<=>`**: Ejecuta búsquedas por similitud coseno (L2 distance) con `ORDER BY embedding <=> query_vector`.
*   **Evaluación de Calidad de Retrieval**:
    *   *Hit Rate*: Proporción de consultas donde al menos un documento relevante aparece en los top-k recuperados.
    *   *Mean Reciprocal Rank (MRR)*: Posición promedio del primer documento relevante recuperado.

### 2.3 Agent Runtime (`03_agent_runtime_scratch.py`)

**Extensión**: ~238 líneas  
**Dependencias**: Cero  

Motor de ejecución de agentes autónomos completo:

*   **Bucle ReAct (Reason-Act)**: El motor planifica acciones basadas en el prompt, llama herramientas del sistema de forma secuencial y evalúa los resultados antes de tomar la decisión final de parada. Implementa el ciclo `Thought → Action → Observation → Decision`.
*   **ExecutionContext Tracing**: Inyecta y arrastra `trace_id` e identificadores de span padre a través de llamadas a subagentes para mantener la trazabilidad jerárquica. Compatible con OpenTelemetry Context Propagation.
*   **EventBus Pub-Sub**: Hilo asíncrono que canaliza eventos (`agent_started`, `tool_call`, `agent_finished`) hacia suscriptores como logging y auditoría. Implementa el patrón Observer con colas thread-safe.
*   **TaskScheduler**: Cola de tareas síncrona que gestiona la ejecución secuencial de acciones planificadas por el agente.
*   **Hybrid Memory Engine**:
    *   *Short-term Memory*: Historial de conversación en contexto (ventana de tokens).
    *   *Long-term Memory*: Búsquedas vectoriales episódicas en pgvector para consolidación de hechos y recall semántico.

### 2.4 Observabilidad y Evaluaciones (`04_observability_and_evals.py`)

**Extensión**: ~218 líneas  
**Dependencias**: Cero  

Micro-librería de rastreo y evaluadores:

*   **TraceSpan Context Manager**: Estructura de trazas jerárquicas compatible con esquemas de telemetría como LangSmith y LangFuse. Registra span_id, parent_span_id, start_time, end_time, inputs, outputs y metadata.
*   **Serialización LangSmith/LangFuse Compatible**: Exporta trazas en formato JSON estructurado para ingestión directa en plataformas de observabilidad.
*   **Métricas Deterministas**:
    *   *Exact Match (EM)*: Comparación exacta de strings para categorizaciones (0 o 1).
    *   *Token F1 Overlap*: Mide la precisión y el recall a nivel de intersección de palabras individuales:
        $$\text{Precision} = \frac{|\text{tokens} \cap \text{reference}|}{|\text{tokens}|}, \quad \text{Recall} = \frac{|\text{tokens} \cap \text{reference}|}{|\text{reference}|}, \quad F1 = 2 \cdot \frac{P \cdot R}{P + R}$$
*   **G-Eval (LLM-as-a-Judge)**: Un agente LLM lee la respuesta generada, el contexto inyectado y una rúbrica de calidad para puntuar el resultado de 1 a 5 y justificar su calificación de forma estructurada.
*   **Versionado de Prompts**: Metadatos y etiquetas de traza para rastrear qué versión del prompt generó qué resultado, permitiendo rollback y comparación.

### 2.5 Gobernanza y Seguridad (`05_governance_and_security.py`)

**Extensión**: ~210 líneas  
**Dependencias**: Cero  

Guardarraíles de producción para agentes:

*   **SystemState Telemetry**: Monitor de estado del sistema que registra métricas (CPU, memoria, tokens consumidos, costos acumulados) en tiempo real.
*   **ToolGater (Interceptor RBAC)**: Motor de políticas basado en roles que evalúa si un agente tiene permiso para invocar una herramienta específica antes de ejecutarla. Define políticas como `ALLOW admin.*`, `DENIAL *.delete_database`, etc.
*   **PII Redaction**: Expresiones regulares que enmascaran información personal identificable (números de teléfono, correos electrónicos, números de identificación, secretos de entorno) antes de enviar el payload a la API externa de la LLM.
*   **Budget Gates**: Límites presupuestarios diarios que abortan la ejecución si el costo acumulado excede el umbral configurado.
*   **Kill Switches**: Mecanismo que aborta de forma instantánea cualquier ejecución de herramienta destructiva al activarse (ej: `DROP TABLE`, `DELETE FROM`).
*   **Rate Limiting**: Control de frecuencia de requests para evitar saturación de APIs externas y cumplir con cuotas de proveedores.

---

## 3. Sandboxes de Frameworks y Ecosistema de Terceros

El laboratorio evalúa y compara la experiencia de desarrollo (DX) y rendimiento de múltiples frameworks de agentes en tres lenguajes.

### 3.1 Python Sandbox (`01_python_frameworks/`)

**Total de demos**: 15 archivos Python  
**Gestor de dependencias**: `uv` con `pyproject.toml`  
**Entorno virtual**: `.venv/` aislado por proyecto  

#### 3.1.1 PydanticAI (`pydantic_ai_demo.py`)

**Framework**: [PydanticAI](https://github.com/pydantic/pydantic-ai)  
**Propósito**: Demostrar structured output con seguridad de tipos nativa  

Implementa agentes con validación estática de tipos mediante modelos Pydantic:
*   **Modelos de Salida**: `DatabaseConfig` (configuración de BD), `AIArchitectureProfile` (perfil de arquitectura de IA) como schemas Pydantic forzados.
*   **TestModel para Modo Offline**: Utiliza `TestModel` de PydanticAI para ejecutar el agente sin llamar a APIs reales, permitiendo testing determinístico en CI/CD.
*   **Inyección de Dependencias**: Inyecta servicios y contexto al agente mediante el sistema de dependencias de PydanticAI.

#### 3.1.2 LangChain Suite Completa (`langgraph_demo.py`)

**Framework**: [LangGraph](https://github.com/langchain-ai/langgraph) + suite LangChain  
**Propósito**: Grafos de estado con ciclos, bucles y coordinación multi-agente  

Implementa la suite completa de LangChain:
*   **LangGraph ReAct Loops**: Grafos de estado que permiten ciclos (bucles de reintentos), ramificaciones condicionales y coordinación de múltiples agentes.
*   **LangSmith Traces**: Integración nativa con LangSmith para depuración, pruebas y trazabilidad de ejecuciones.
*   **LangFuse Telemetry**: Telemetría de código abierto compatible con LangFuse para evaluaciones y gestión de prompts.
*   **LangServe REST API**: Expone componentes de LangChain como APIs REST باستخدام FastAPI.
*   **LangMem Long-term Memory**: Servicio especializado de memoria persistente para estado de agentes a largo plazo.

#### 3.1.3 CrewAI (`crewai_demo.py`)

**Framework**: [CrewAI](https://github.com/crewaiinc/crewai)  
**Propósito**: Orquestación de agentes colaborativos con juegos de rol  

Implementa un crew multi-agente:
*   **Agent Roles**: Define agentes especializados como `Architect` (diseñador de sistemas) y `Security Auditor` (revisor de seguridad).
*   **Task Delegation**: Las tareas se asignan a agentes específicos con roles, metas y backstories definidos.
*   **Collaborative Workflow**: Los agentes colaboran secuencialmente para completar tareas complejas.

#### 3.1.4 DeepAgents (`deepagents_demo.py`)

**Framework**: [Deep Agents](https://github.com/langchain-ai/deepagents) (LangChain)  
**Propósito**: Agente autónomo "batteries-included" sobre LangGraph  

Implementa agentes profundos con middleware:
*   **create_deep_agent() Factory**: Función fábrica que crea agentes autónomos con configuración declarativa.
*   **Sub-agents**: Capacidad de delegar tareas a sub-agentes especializados.
*   **Middleware Stack**:
    *   *TodoList*: Gestor de tareas pendientes persistente.
    *   *Skills*: Habilidades reutilizables inyectables.
    *   *SubAgent*: Middleware para orquestación de sub-agentes.
*   **Streaming**: Soporte nativo para streaming de tokens y eventos de ejecución.

#### 3.1.5 MCP Básico (`mcp_demo.py`)

**Framework**: [Model Context Protocol](https://modelcontextprotocol.io/) con FastMCP  
**Propósito**: Servidor MCP educativo con tools y resources  

Implementa un servidor MCP básico:
*   **FastMCP Server**: Servidor ligero que expone herramientas (`@mcp.tool()`) y recursos (`@mcp.resource()`).
*   **Tool Definitions**: Herramientas como `add(a, b)`, `get_weather(city)` con descripciones y schemas.
*   **Client Simulation**: Cliente MCP que conecta al servidor y ejecuta herramientas remotas.

#### 3.1.6 Servidores MCP Complejos

*   **`sqlite_mcp_server_demo.py`**: Servidor MCP que expone consultas de lectura y escritura seguras a bases de datos SQLite locales. Incluye sanitización de queries y restricciones de permisos.
*   **`mcp_educational_platform_demo.py`**: Servidor MCP complejo con arquitectura SSE (Server-Sent Events) que expone herramientas de negocio como asignación de cursos, consulta de calificaciones, generación de reportes educativos. Diseñado para integración con Cursor, Claude Code y otros clientes MCP.
*   **`mcp_virtual_wallet_demo.py`**: Servidor MCP de billetera virtual con transacciones financieras seguras (consulta de balances, transferencias, historial). Implementa validaciones de saldo y auditoría de movimientos.

#### 3.1.7 OpenAI Agents SDK

*   **`openai_agents_demo.py`**: Agente autónomo usando el SDK oficial de OpenAI con el patrón de **Handoff (Delegación)**, donde un agente inicial transfiere síncronamente el control de la conversación a otro agente especializado en base a la intención detectada.
*   **`sqlite_openai_agents_demo.py`**: Variante del anterior que integra directamente con bases de datos SQLite para persistencia de estado y consultas.

#### 3.1.8 RAG Avanzado con LlamaIndex (`llamaindex_advanced_demo.py`)

**Framework**: [LlamaIndex](https://github.com/run-llama/llama_index)  
**Propósito**: Pipeline de recuperación avanzada  

Implementa técnicas de RAG empresarial:
*   **Hierarchical Node Parsing**: Segmentación en nodos padre e hijos para conservar el contexto macro mientras se recuperan fragmentos granulares.
*   **Query Translation**: Reescribe y expande la consulta del usuario mediante un LLM para mejorar la cobertura de búsqueda (ej: "¿Cómo funciona RAG?" → "recuperación aumentada por generación, RAG, retrieval augmented generation").
*   **Reranking**: Reordena los chunks recuperados por similitud utilizando cross-encoders ligeros (ej: `bge-reranker-base`) para mejorar la precisión de los top-k finales.

#### 3.1.9 Bases de Datos Vectoriales y OLAP

*   **`lancedb_pydanticai_demo.py`**: Integración de agentes PydanticAI con [LanceDB](https://github.com/lancedb/lancedb) como base de datos vectorial in-process y serverless. Elimina la necesidad de infraestructura de red externa (todo corre en el mismo proceso).
*   **`duckdb_crewai_demo.py`**: Conecta agentes CrewAI a [DuckDB](https://github.com/duckdb/duckdb) para procesar logs de observabilidad masivos y telemetría histórica del sistema en memoria mediante consultas SQL analíticas de alto rendimiento.
*   **`duckdb_langgraph_demo.py`**: Variante del anterior usando LangGraph para orquestación de flujos de análisis de datos.

#### 3.1.10 Optimización de Modelos (`finetuning_demo.py`)

**Frameworks**: [Unsloth](https://github.com/unslothai/unsloth) + [Hugging Face](https://huggingface.co/)  
**Propósito**: Ajuste fino de modelos de código abierto  

Pipeline de fine-tuning:
*   **Modelos Base**: Adapta modelos abiertos (Llama, Mistral) a tareas estructuradas específicas.
*   **Técnicas de Optimización**: Utiliza Unsloth para aceleración 2-5x del entrenamiento y reducción de memoria.
*   **Dataset Preparation**: Preparación y formateo de datasets para entrenamiento supervisado.
*   **Exportación**: Exporta modelos entrenados a formatos GGUF, vLLM, etc.

### 3.2 TypeScript Sandbox (`02_typescript_frameworks/`)

**Total de demos**: 3 archivos TypeScript  
**Gestor de dependencias**: `bun` con `package.json`  
**Runtime**: Bun (alta velocidad)  
**Configuración**: `tsconfig.json` con `target: ESNext`  

#### 3.2.1 Mastra (`mastra_demo.ts`)

**Framework**: [Mastra](https://github.com/mastra-ai/mastra)  
**Propósito**: Agentes autónomos y workflows con validación estática de tipos  

Implementa agentes TypeScript nativos:
*   **Type-Safe Agents**: Validación estática de tipos nativa de TypeScript para inputs/outputs de agentes.
*   **Structured Workflows**: Flujos de trabajo estructurados con pasos secuenciales y condicionales.
*   **JSON Output Formatting**: Salidas formateadas en JSON con schemas Zod para validación runtime.
*   **Tool Integration**: Integración declarativa de herramientas externas con tipos estrictos.

#### 3.2.2 Flue (`flue_demo.ts`)

**Framework**: [Flue](https://github.com/withastro/flue) (por el equipo de Astro)  
**Propósito**: Integraciones nativas web para renderizado ligero  

Implementa patrones de renderizado de estado de agentes:
*   **createAgent Pattern**: Patrón fábrica para crear agentes con configuración declarativa.
*   **Web-Native Integration**: Integración nativa con frameworks web modernos (Astro, React, Vue).
*   **Lightweight Visualization**: Visualización ligera del estado de agentes sin overhead pesado.

#### 3.2.3 Pi Coding Agent (`pi_demo.ts`)

**Framework**: [Pi](https://github.com/earendel-works/pi/) (`@earendel-works/pi-coding-agent`)  
**Propósito**: Agente de codificación terminal-first ultra-ligero  

Implementa un agente de codificación embebido:
*   **createAgentSession**: Inicia una sesión de agente con configuración de herramientas y contexto.
*   **Event Subscriptions**: Suscripciones a eventos del agente (`onToken`, `onToolCall`, `onComplete`).
*   **Terminal-First**: Diseñado para ejecución en terminal sin UI gráfica, ideal para automatizaciones y scripts.
*   **Embedded & Ultra-Lightweight**: Huella mínima, diseñado para integrarse en editores de código y CLIs.

### 3.3 Go Sandbox (`03_go_frameworks/`)

**Total de demos**: 1 archivo Go  
**Versión de Go**: 1.25.1 (definida en `.go-version`)  
**Módulo**: `go.mod` con dependencia `github.com/fugue-labs/gollem`  

#### 3.3.1 Gollem (`main.go`)

**Framework**: [Gollem](https://github.com/fugue-labs/gollem)  
**Propósito**: Runtime de agentes con máquinas de estado deterministas  

Implementa agentes modelados como máquinas de estado:
*   **Typed Generic Agent**: `NewAgent[DatabaseAnalysis]` con genéricos de Go para tipado estático del estado.
*   **FuncTool with Typed Params**: Herramientas definidas como funciones con parámetros tipados (`FuncTool(name, description, handler)`).
*   **State Machine Transitions**: Transiciones seguras entre fases de ejecución (ej: `ANALYZE → PLAN → EXECUTE → VERIFY`).
*   **TestModel Offline Mode**: Modo de testing determinístico sin llamadas a APIs reales, permitiendo CI/CD sin API keys.

---

## 4. Aplicación de Producción: Textbook Generator (`textbook_generator/`)

Es la realización práctica de una aplicación empresarial robusta que integra agentes bajo principios de **Clean Architecture / SOLID / Screaming Architecture**.

### 4.1 Arquitectura en Capas

El sistema sigue una separación estricta en capas concéntricas:

```
┌─────────────────────────────────────────────────────────┐
│                   Infrastructure Layer                  │
│  (PydanticAI Agents, SQLAlchemy ORM, FastAPI, NEM Seeds)│
├─────────────────────────────────────────────────────────┤
│                   Application Layer                    │
│              (10 Use Cases, Workflow Logic)             │
├─────────────────────────────────────────────────────────┤
│                      Domain Layer                      │
│         (Pydantic Models, Abstract Ports)              │
└─────────────────────────────────────────────────────────┘
```

*   **Domain Layer** (`domain/`): Modelos Pydantic puros, enums y puertos abstractos. Cero dependencias externas.
*   **Application Layer** (`application/`): 10 casos de uso que orquestan la lógica de negocio.
*   **Infrastructure Layer** (`infrastructure/`): Implementaciones concretas de puertos (agentes, repositorios, API HTTP).

### 4.2 Modelos de Dominio (`domain/models.py`)

**Extensión**: 136 líneas  
**Framework**: Pydantic v2 con `BaseModel`  

#### 4.2.1 Entidades Core

*   **`Textbook`**: Libro de texto completo con título, materia, grado, estado global, timestamp de creación, 3 trimestres, fase de aprendizaje NEM y contexto local.
*   **`Trimestre`**: Trimestre del libro (1, 2 o 3) con título, metas de aprendizaje y lista de secuencias pedagógicas.
*   **`Secuencia`**: Secuencia didáctica con número, título, objetivos, score de alineación curricular, score de adecuación etaria, estado en el pipeline (DRAFT → GENERATING → PENDING_REVIEW → APPROVED/REJECTED), feedback de revisión, lecciones, campo formativo principal, campos vinculados, contenidos sintéticos IDs, PDA IDs, ejes articuladores y proyecto vinculado.
*   **`Lesson`**: Lección individual con número, título, secciones obligatorias (inicio/apertura, desarrollo/actividades, cierre/evaluación) y actividades interactivas.
*   **`GenerationStatus`**: Enum de estados de máquina (DRAFT, GENERATING, PENDING_REVIEW, APPROVED, REJECTED).
*   **`CurricularRequirement`**: Requisito curricular genérico con código (ej: REQ-ESP-1.1), descripción, materia y grado.

#### 4.2.2 Entidades NEM (Nueva Escuela Mexicana)

*   **`CampoFormativo`**: Enum con 4 valores oficiales SEP:
    *   `LENGUAJES`: "Lenguajes"
    *   `SABERES_PCIENTIFICO`: "Saberes y Pensamiento Científico"
    *   `ETICA_NATURALEZA_SOCIEDADES`: "Ética, Naturaleza y Sociedades"
    *   `HUMANO_COMUNITARIO`: "De lo Humano y lo Comunitario"
*   **`EjeArticulador`**: Enum con 7 ejes transversales:
    *   `PENSAMIENTO_CRITICO`: "Pensamiento crítico"
    *   `INTERCULTURALIDAD`: "Interculturalidad"
    *   `IGUALDAD_GENERO`: "Igualdad de género"
    *   `VIDA_SALUDABLE`: "Vida saludable"
    *   `INCLUSION`: "Inclusión"
    *   `LECTURA_ESCRITURA`: "Lectura y escritura"
    *   `ARTES_ESTETICA`: "Artes y experiencias estéticas"
*   **`FaseAprendizaje`**: Enum con 6 fases oficiales SEP:
    *   `FASE_1`: "Fase 1 - Preescolar 3°"
    *   `FASE_2`: "Fase 2 - Primaria 1°-2°"
    *   `FASE_3`: "Fase 3 - Primaria 3°-4°"
    *   `FASE_4`: "Fase 4 - Primaria 5°-6°"
    *   `FASE_5`: "Fase 5 - Secundaria 1°-2°"
    *   `FASE_6`: "Fase 6 - Secundaria 3°"
*   **`TipoProyecto`**: Enum con 3 tipos de proyectos integradores:
    *   `AULA`: "Proyecto de Aula"
    *   `ESCOLAR`: "Proyecto Escolar"
    *   `COMUNITARIO`: "Proyecto Comunitario"
*   **`ContenidoProgramaSintetico`**: Catálogo de contenidos del Programa Sintético SEP (DOF 2023) con campo formativo, fase, código oficial (ej: CF-LNG-F2-C01) y descripción.
*   **`ProcesoDesarrolloAprendizaje`**: PDA asociados a cada contenido sintético con FK a contenido, fase y descripción.
*   **`ContextoLocal`**: Datos del Programa Analítico del docente con FK al libro, tipo de comunidad (Urbana, Rural, Indígena, Migrante), lengua originaria, problemática local, saberes comunitarios y proyectos sugeridos.
*   **`EjeArticuladorTransversal`**: Mapeo de ejes articuladores por secuencia con FK a secuencia, eje, grado de profundidad (menciona, desarrolla, transversal) y descripción de integración.

### 4.3 Casos de Uso (`application/`)

**Total**: 10 casos de uso + archivo `use_cases.py` de exports  

1.  **`create_textbook.py`** (`CreateTextbookUseCase`): Crea un proyecto de libro de texto con título, materia y grado. Inicializa el esqueleto DRAFT.
2.  **`generate_book_outline.py`** (`GenerateBookOutlineUseCase`): Delega al Outline Agent el diseño de la macro-estructura (3 trimestres, 18 secuencias con títulos y objetivos).
3.  **`generate_sequence_content.py`** (`GenerateSequenceContentUseCase`): Delega al Content Generator Agent la redacción de lecciones con estructura Inicio/Desarrollo/Cierre.
4.  **`generate_book_workflow.py`** (`GenerateBookWorkflowUseCase`): Orquesta el flujo completo de generación en segundo plano (Background Tasks): crea esqueleto → genera secuencias 1..18 → evalúa con juez → deriva a HITL si score < 0.85.
5.  **`review_sequence.py`** (`ReviewSequenceUseCase`): Procesa la revisión humana de secuencias pendientes (aprobar o rechazar con feedback).
6.  **`contextualize_textbook.py`** (`ContextualizeTextbookUseCase`): Asocia contexto local (comunidad, problemática, saberes) al libro para adaptación al Programa Analítico docente.
7.  **`map_contenidos_pda.py`** (`MapContenidosPDAUseCase`): Mapea contenidos del Programa Sintético y PDA oficiales a una secuencia según campo formativo y fase.
8.  **`evaluate_pda_alignment.py`** (`EvaluatePDAAlignmentUseCase`): Evalúa con agente NEM especializado la alineación de una secuencia con los PDA oficiales SEP.
9.  **`generate_proyecto_integrador.py`** (`GenerateProyectoIntegradorUseCase`): Vincula un proyecto integrador (Aula, Escolar, Comunitario) a una secuencia.
10. **`export_conaliteg_format.py`** (`ExportConalitegFormatUseCase`): Exporta el libro completo al formato CONALITEG (Catálogo Nacional de Libros de Texto Gratuitos) con metadatos NEM.

### 4.4 Infraestructura (`infrastructure/`)

#### 4.4.1 Agentes de IA (`infrastructure/agents/`)

*   **`pydantic_agents.py`** (`PydanticTextbookAgentService`): Implementación de puertos de dominio usando PydanticAI.
    *   *Outline Agent*: Diseña macro-estructura del libro.
    *   *Content Generator Agent*: Redacta lecciones con estructura pedagógica.
    *   *Evaluation Agent*: Califica alineación curricular y adecuación etaria (0.0 a 1.0).
    *   *Modelo*: Gemini 1.5 Flash (por defecto) con Context Caching para reducir costos 80%.
*   **`nem_agents.py`** (`NEMOutlineAgentService`): Agentes especializados en alineación NEM/SEP.
    *   *NEM Content Mapper Agent*: Mapea contenidos y PDA del Programa Sintético.
    *   *NEM Alignment Evaluator*: Evalúa alineación con campos formativos y ejes articuladores.

#### 4.4.2 Base de Datos (`infrastructure/database/`)

*   **`db_models.py`**: Modelos ORM SQLAlchemy con 8+ tablas:
    *   `textbook`: Libros de texto
    *   `trimestre`: Trimestres
    *   `secuencia`: Secuencias didácticas
    *   `lesson`: Lecciones
    *   `curricular_requirement`: Requisitos curriculares
    *   `contexto_local`: Contexto local
    *   `contenido_programa_sintetico`: Contenidos NEM
    *   `proceso_desarrollo_aprendizaje`: PDA
    *   `eje_articulador_transversal`: Ejes por secuencia
*   **`sqlite_repository.py`**: Implementación de repositorios usando SQLite (archivo local, cero configuración de red).
    *   `SQLiteTextbookRepository`: CRUD de libros, trimestres, secuencias, lecciones.
    *   `SQLiteRequirementRepository`: CRUD de requisitos curriculares.
    *   `SQLiteNEMRepository`: CRUD de contenidos NEM, PDA, ejes.
*   **Seed Files NEM** (5 archivos con datos reales del DOF 2023):
    *   `seed_nem_fase2.py`: Fase 2 (Primaria 1°-2°)
    *   `seed_nem_fase3.py`: Fase 3 (Primaria 3°-4°)
    *   `seed_nem_fase4.py`: Fase 4 (Primaria 5°-6°)
    *   `seed_nem_fase5.py`: Fase 5 (Secundaria 1°-2°)
    *   `seed_nem_fase6.py`: Fase 6 (Secundaria 3°)
*   **`seed_nem_all.py`**: Script unificado que ejecuta todos los seeds de fase 2-6.

#### 4.4.3 API HTTP (`infrastructure/http/`)

*   **`api.py`** (315 líneas): Router FastAPI con 12 endpoints REST:
    *   `POST /api/books`: Crea libro y lanza generación en background
    *   `GET /api/books`: Lista todos los libros
    *   `GET /api/books/{id}`: Obtiene libro por ID
    *   `GET /api/reviews`: Lista secuencias pendientes de revisión HITL
    *   `POST /api/reviews/{secuencia_id}`: Aprueba o rechaza secuencia
    *   `POST /api/secuencias/{secuencia_id}/regenerate`: Regenera secuencia con feedback
    *   `POST /api/books/{textbook_id}/contexto-local`: Guarda contexto local
    *   `GET /api/books/{textbook_id}/contexto-local`: Obtiene contexto local
    *   `POST /api/secuencias/{secuencia_id}/map-contenidos`: Mapea contenidos NEM
    *   `POST /api/secuencias/{secuencia_id}/evaluate-pda`: Evalúa alineación PDA
    *   `POST /api/secuencias/{secuencia_id}/proyecto`: Vincula proyecto integrador
    *   `GET /api/books/{textbook_id}/export/conaliteg`: Exporta formato CONALITEG
    *   `POST /api/admin/requirements/populate`: Siembra requisitos curriculares
    *   `POST /api/admin/nem/seed-fase2`: Siembra datos NEM Fase 2

#### 4.4.4 Frontend (`static/`)

**Tecnología**: SPA (Single Page Application) vanilla JavaScript + HTML + CSS  
**Diseño**: Dark glassmorphism theme con efectos de vidrio esmerilado  
**Tipografía**: Google Fonts (Outfit para headings, Plus Jakarta Sans para body)  
**Iconos**: FontAwesome  

Interfaz "EduText.AI" con:
*   **Dashboard**: Métricas globales (libros generados, secuencias aprobadas, en revisión).
*   **Library**: Biblioteca de libros con tarjetas expandibles y filtros.
*   **Review Queue**: Cola de revisión HITL con botones de aprobar/rechazar, feedback y regeneración.
*   **NEM Metadata**: Visualización de campos formativos, ejes articuladores y PDA mapeados.
*   **Botones de Regeneración**: Feedback loops con instrucciones de regeneración.

### 4.5 Patrones Clave Implementados

#### 4.5.1 Fase de Gating Automática (HITL)

Las secuencias didácticas generadas son evaluadas por un agente Juez dual:
*   **Alineación Curricular**: Score de 0.0 a 1.0 midiendo cumplimiento de requisitos curriculares.
*   **Adecuación Etaria**: Score de 0.0 a 1.0 midiendo apropiación pedagógica para la edad (1° grado = 6 años).

**Lógica de Gating**:
```
IF curricular_alignment_score >= 0.85 AND age_appropriateness_score >= 0.85:
    status = APPROVED (automático)
ELSE:
    status = PENDING_REVIEW (cola HITL para revisión docente)
```

#### 4.5.2 Estrategia de Caché Pragmática (Context Caching)

En lugar de cachear lecciones creativas (lo que provocaría plagio inter-colegios y persistencia de alucinaciones), se implementa **Context Caching de Gemini**:
*   El proveedor de IA mantiene en memoria los lineamientos curriculares inyectados al prompt raíz.
*   Reduce las facturas de tokens en un **80%**.
*   Acelera el tiempo de respuesta a milisegundos en llamadas subsecuentes.

#### 4.5.3 Estado de Máquina de Secuencias

```
DRAFT → GENERATING → (Evaluation) → [score >= 0.85] → APPROVED
                            ↓
                     [score < 0.85] → PENDING_REVIEW → [Humano Aprueba] → APPROVED
                                                        ↓
                                                 [Humano Rechaza + Feedback] → GENERATING (regeneración)
```

---

## 5. Testing: Pirámide Completa

El laboratorio implementa una pirámide de testing exhaustiva validando desde funciones individuales hasta flujos completos de UI en navegador.

### 5.1 Tests de Primitivas (`tests/test_primitives.py`)

**Propósito**: Validar las 5 primitivas desde cero  
**Framework**: pytest  
**Tests**: Funciones puras sin mocking complejo  

*   `test_cosine_similarity()`: Valida cálculo de similitud coseno en Python puro.
*   `test_semantic_chunking()`: Valida agrupación de oraciones por umbral de similitud.
*   `test_trace_span_context()`: Valida propagación de contexto en trazas.
*   `test_token_f1_overlap()`: Valida cálculo de F1 a nivel de tokens.
*   `test_pii_redaction()`: Valida enmascaramiento de PII con regex.

### 5.2 Tests Específicos por Primitiva

*   **`tests/test_01_llm_inference.py`**: Tests de parser SSE, cost tracker, structured output parsing.
*   **`tests/test_02_rag_pgvector.py`**: Tests de chunking, embedding, retrieval quality (Hit Rate, MRR).
*   **`tests/test_03_agent_runtime.py`**: Tests de bucle ReAct, event bus, memory engine.
*   **`tests/test_04_observability.py`**: Tests de span serialization, metric calculations, G-Eval prompt.
*   **`tests/test_05_governance.py`**: Tests de ToolGater policies, budget gates, kill switch activation.

### 5.3 Tests de Servidores MCP (`tests/test_mcp_servers.py`)

**Propósito**: Validar servidores MCP (educational platform, virtual wallet)  
**Tests**:
*   `test_sqlite_mcp_server()`: Conecta a servidor MCP SQLite y ejecuta queries.
*   `test_educational_platform_mcp()`: Valida herramientas de asignación de cursos, calificaciones.
*   `test_virtual_wallet_mcp()`: Valida transacciones, balances, auditoría.

### 5.4 Smoke Test de API (`tests/smoke_test_api.py`)

**Propósito**: Validación rápida de que el servidor FastAPI arranca y responde  
**Tests**:
*   `test_health_check()`: GET `/health` responde 200.
*   `test_list_textbooks_empty()`: GET `/api/books` retorna lista vacía inicial.

### 5.5 Tests del Textbook Generator (`tests/textbook_generator/`)

#### 5.5.1 Unit Tests (`unit/`)

*   **`test_domain_models.py`**: Valida modelos Pydantic de dominio (Textbook, Secuencia, Lesson, enums NEM).

#### 5.5.2 Integration Tests (`integration/`)

*   **`test_repository_sqlite.py`**: Tests de repositorios SQLite con base de datos real (no mockeada).
    *   `test_create_textbook()`: Inserta libro y lo recupera.
    *   `test_create_secuencia_with_lessons()`: Inserta secuencia con lecciones anidadas.
    *   `test_update_secuencia_status()`: Actualiza estado de secuencia.
*   **`test_agent_services.py`**: Tests de servicios de agentes usando `TestModel` de PydanticAI (modo offline, sin API keys).
    *   `test_outline_agent()`: Valida generación de macro-estructura.
    *   `test_content_generator_agent()`: Valida generación de lecciones.
    *   `test_evaluation_agent()`: Valida scoring de alineación.
*   **`test_nem_agents.py`**: Tests de agentes NEM especializados.
*   **`test_nem_integration.py`**: Tests de integración completa de flujo NEM (mapeo de contenidos, evaluación PDA).

#### 5.5.3 E2E Tests (`e2e/`)

*   **`test_api_workflow_e2e.py`**: Tests de flujos completos vía HTTP con servidor FastAPI real.
    *   `test_create_textbook_workflow()`: POST libro → genera en background → verifica estados.
    *   `test_review_workflow()`: Genera libro → lista reviews pendientes → aprueba/rechaza.
*   **`test_nem_e2e.py`**: Tests E2E de flujos NEM completos.

#### 5.5.4 ATDD (Acceptance Test-Driven Development) (`atdd/`)

*   **`test_atdd_acceptance_criteria.py`**: Tests basados en criterios de aceptación formales (Given-When-Then).
*   **`test_nem_contextualization.py`**: Tests de contexto local y programa analítico.

#### 5.5.5 Browser Tests (`browser/`)

**Framework**: Playwright con Chromium headless  
**Extensión**: ~20 tests, ~90 segundos de ejecución  

*   **`test_browser_e2e.py`**: Tests de UI navegando la SPA real.
    *   Valida renderizado del dashboard, biblioteca, cola de revisión.
    *   Flujo completo: crear libro → generación → HITL review → aprobar/rechazar.
    *   Métricas del dashboard y estado de la API.
    *   Metadatos NEM (campos formativos, ejes articuladores).
    *   Botones de regeneración y feedback.
*   **`conftest.py`**: Configuración de fixtures que auto-arrancan servidor FastAPI en puerto efímero con SQLite temporal eliminada tras cada run.

---

## 6. Wiki: Artículos Técnicos (`wiki/`)

**Total de artículos**: 13 documentos técnicos  

### 6.1 Artículos de Primitivas

*   **`00_introduccion.md`**: Filosofía arquitectónica, directrices de Karpathy, perspectiva del CTO sobre transformación organizacional mediante IA, bucles de aprendizaje y elección pragmática de PostgreSQL + PGVector.
*   **`01_llm_inference.md`**: Protocolos HTTP/SSE, tokenización, estimación de costos, comparación de proveedores (OpenAI, Anthropic, Google, MiniMax).
*   **`02_rag_postgres_pgvector.md`**: Álgebra lineal en Python puro, sliding window, semantic chunking, esquema PGVector DDL, métricas de calidad de retrieval (Hit Rate, MRR).
*   **`03_agent_runtime.md`**: Anatomía de un agent runtime: bucles ReAct, buses de eventos asíncronos, schedulers, motores de memoria corto/largo plazo, OpenTelemetry Context Propagation.
*   **`04_observability_and_evals.md`**: Trazabilidad jerárquica de spans, compatibilidad con esquemas LangSmith/Langfuse, métricas determinísticas (Exact Match, Token F1), G-Eval (LLM-as-a-Judge) y versionado de prompts.
*   **`05_governance_and_security.md`**: Políticas de gating a nivel de ejecución (ToolGater), RBAC, máscara de PII, límites presupuestarios diarios y kill switches.

### 6.2 Artículos de Ecosistema

*   **`06_framework_ecosystem.md`**: Evolución comercial de la suite LangChain (LangChain → LangGraph → LangSmith → LangServe → LangMem → LangFuse), alternativas ligeras (Mastra, PydanticAI, CrewAI, OpenAI Agents SDK, Gollem, Flue, Pi) y matriz de decisión construir vs. adoptar.
*   **`07_entrevista_qa.md`**: Arsenal técnico de entrevistas con 52 secciones de preguntas y respuestas justificadas (State Machines vs. ReAct, Structured Outputs, Memory Engine, Event Bus, etc.).

### 6.3 Artículos de Arquitectura y ADRs

*   **`08_pipeline_architecture_adr.md`** (155 líneas): **ADR (Architecture Decision Record)** sobre topologías de pipelines con análisis de trade-offs:
    *   *Topología Lineal*: Output del paso N → input del paso N+1. Baja latencia, bajo costo, máxima predictibilidad.
    *   *Topología DAG (Directed Acyclic Graph)*: Nodos con aristas direccionales sin ciclos. Permite paralelización pero no corrección autónoma.
    *   *Topología Cíclica (ReAct Loop)*: Thought → Action → Observation → Decision con posibilidad de retorno. Máxima flexibilidad pero riesgo de bucles infinitos.
    *   *Topología Multi-Agente*: Redes de agentes autónomos coordinados. Alta complejidad, muy alto costo.
    *   Incluye tabla comparativa de autonomía, latencia, costo, predictibilidad y complejidad de testing.
*   **`09_system_design_textbook_generator.md`** (205 líneas): Diseño completo del sistema Textbook Generator:
    *   Contexto de dominio (audiencia de 6 años, estructura 3 trimestres × 6 secuencias, fases Inicio/Desarrollo/Cierre).
    *   Arquitectura de alto nivel con diagrama Mermaid (workflow híbrido orquestador + agentes).
    *   Componentes clave: Workflow Orchestrator, Curricular Standards RAG, PydanticAI Agents (Outline, Content Generator, Evaluation).
    *   Pipeline HITL con umbral 0.85.
    *   ADRs y decisiones de diseño.
*   **`10_nem_sep_alineacion.md`** (151 líneas): Análisis gap entre el sistema actual y los requisitos de la Nueva Escuela Mexicana (NEM):
    *   Lo que está bien encaminado (Clean Architecture, estructura trimestral, HITL, Context Caching).
    *   Gaps críticos: Campos Formativos integrados, Programa Sintético (Contenidos + PDA), Ejes Articuladores transversales, Programa Analítico docente.
    *   Plan de evolución con nuevas entidades de dominio.
*   **`11_adr_004_nem_integration.md`** (117 líneas): **ADR-004** documentando la decisión de introducir una capa de integración NEM:
    *   Contexto regulatorio (SEP, DOF 2023, Nueva Escuela Mexicana).
    *   Decisión: Entidades de dominio de primera clase (CampoFormativo, EjeArticulador, FaseAprendizaje, ContenidoProgramaSintetico, PDA, EjeArticuladorTransversal, ContextoLocal) + servicio NEM separado (Interface Segregation).
    *   Consecuencias y trade-offs.

### 6.4 Artículos de Stakeholders

*   **`12_playbook_presentacion_stakeholders.md`**: Guía de comunicación y ventas para traducir decisiones técnicas a ROI financiero:
    *   Clean Architecture → "Si Gemini es superado por Claude, el reemplazo toma horas en lugar de semanas."
    *   SQLite para catálogos → "Evitamos bases vectoriales costosas, 100% precisión curricular a costo operativo cero."
    *   Context Caching → "Reduce costos de tokens 80% y tiempo de espera a milisegundos."
    *   HITL → "Ninguna lección con errores llegará al aula."

---

## 7. Infraestructura Local y CI/CD

### 7.1 Calidad de Código Local (Sin Costos Cloud)

Para evitar el costo de ejecuciones remotas en GitHub Actions, toda la suite de validación corre localmente:

*   **`scripts/local_check.sh`**: Script bash que ejecuta en secuencia:
    1.  `uvx ruff check .` (linting Python)
    2.  `uv run --with mypy mypy 00_primitives_scratch/` (typechecking Python)
    3.  `cd 02_typescript_frameworks && bun x tsc --noEmit` (typechecking TypeScript)
    4.  `uv run --project 01_python_frameworks --with pytest pytest tests/ -v` (tests)
*   **`scripts/local_check.sh --install-hook`**: Instala el script como Git pre-commit hook, ejecutando automáticamente Ruff, Mypy, `tsc --noEmit` y pytest antes de cada commit.

### 7.2 Contenedores con Docker Compose

Levanta infraestructura completa con un comando:

```bash
docker-compose up -d
```

**Servicios expuestos**:
*   **PostgreSQL con pgvector**: `localhost:5432` (user: `postgres`, password: `postgres`, db: `ai_lab`)
*   **Servidor MCP Educativo (SSE)**: `http://localhost:8000`
*   **Servidor MCP Virtual Wallet (SSE)**: `http://localhost:8001`

**Volumen persistente**: `pgdata` para datos de PostgreSQL.

### 7.3 Despliegue en la Nube

**`scripts/deploy_mcp.sh`**: Script interactivo que despliega servidores MCP a:
*   **Railway**: Plataforma serverless con despliegue automático desde Git.
*   **Fly.io**: Despliegue de contenedores globales con edge computing.
*   **Google Cloud Run**: Serverless de Google Cloud con escalado automático.

---

## 8. Repositorios de Referencia (`external/`)

**Total de repos clonados**: 12 (todos gitignored en `.gitignore`)  

Propósito: Análisis local de código de terceros, estudio de patrones, benchmarking y referencia para decisiones arquitectónicas.

1.  **`agent-governance-toolkit/`** ([microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit)): Motor de seguridad y gobernanza de agentes de Microsoft. Referencia para políticas de gating, RBAC y kill switches.
2.  **`ai-engineering-from-scratch/`** ([rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)): Currículo completo de construcción de sistemas de IA desde cero. Referencia pedagógica.
3.  **`ai-engineering-hub/`** ([patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub)): Tutoriales prácticos para despliegues modernos de IA.
4.  **`badger/`** ([dgraph-io/badger](https://github.com/dgraph-io/badger)): Almacén Key-Value LSM Tree rápido en Go. Referencia para storage embebido de alta performance.
5.  **`bbolt/`** ([etcd-io/bbolt](https://github.com/etcd-io/bbolt)): Almacén Key-Value transaccional embebido en Go. Referencia para storage B+-tree persistente.
6.  **`deepagents/`** ([langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)): Arnés de agentes autónomos "batteries-included" sobre LangGraph. Referencia para middleware y sub-agentes.
7.  **`driftdb/`** ([DavidLiedle/DriftDB](https://github.com/DavidLiedle/DriftDB)): Motor de sincronización P2P en tiempo real. Referencia para colaboración distribuida.
8.  **`duckdb/`** ([duckdb/duckdb](https://github.com/duckdb/duckdb)): Base de datos analítica SQL in-process. Referencia para OLAP y procesamiento de logs masivos.
9.  **`ejemplo-harness-subagentes/`**: Ejemplo de arnés de sub-agentes (orquestación multi-agente).
10. **`memoria persistente/`**: Sistema de memoria persistente para agentes (episodic + semantic memory).
11. **`agent workflow repository/`**: Framework ligero de agentes con enfoque en simplicidad.
12. **`lancedb/`** ([lancedb/lancedb](https://github.com/lancedb/lancedb)): Base de datos vectorial serverless e in-process. Referencia para RAG sin infraestructura externa.

---

## 9. Arquitectura: Patrones y Convenciones

### 9.1 Clean Architecture (Detallado)

El Textbook Generator implementa Clean Architecture de Robert C. Martin (Uncle Bob):

*   **Dependency Rule**: Las dependencias solo apuntan hacia adentro (Infrastructure → Application → Domain).
*   **Ports & Adapters**: El Domain define interfaces abstractas (ports), Infrastructure implementa adaptadores concretos (PydanticAI agents, SQLAlchemy repos).
*   **Use Cases**: La Application Layer contiene 10 casos de uso que orquestan lógica de negocio sin conocer detalles de implementación.
*   **Entities**: El Domain Layer contiene modelos Pydantic puros (Textbook, Secuencia, Lesson, enums NEM) sin dependencias externas.

### 9.2 Aplicación de SOLID

*   **Single Responsibility Principle (SRP)**: Cada caso de uso tiene una única responsabilidad (ej: `CreateTextbookUseCase` solo crea libros).
*   **Open/Closed Principle (OCP)**: Nuevos proveedores de IA se agregan implementando puertos abstractos sin modificar casos de uso.
*   **Liskov Substitution Principle (LSP)**: Agentes intercambiables (PydanticAI ↔ TestModel) sin romper contratos.
*   **Interface Segregation Principle (ISP)**: Puertos separados para `TextbookAgentService` y `NEMAgentService`.
*   **Dependency Inversion Principle (DIP)**: Casos de uso dependen de abstracciones (puertos), no de implementaciones concretas.

### 9.3 Screaming Architecture

La estructura de carpetas "grita" el propósito del sistema:
*   `textbook_generator/` → El nombre del dominio es evidente.
*   `domain/models.py` → Contiene `Textbook`, `Secuencia`, `Lesson` → El dominio es educación.
*   `application/use_cases.py` → Contiene `CreateTextbookUseCase`, `GenerateBookWorkflowUseCase` → Las acciones del sistema son evidentes.

### 9.4 Convenciones de Nomenclatura

*   **Modelos de Dominio**: PascalCase (`Textbook`, `CampoFormativo`, `FaseAprendizaje`).
*   **Casos de Uso**: PascalCase + sufijo `UseCase` (`CreateTextbookUseCase`).
*   **Repositorios**: PascalCase con prefijo de tecnología (`SQLiteTextbookRepository`).
*   **Endpoints API**: snake_case en URLs (`/api/books/{id}/contexto-local`).
*   **Tests**: snake_case con prefijo `test_` (`test_create_textbook_workflow`).

### 9.5 Gestión de Errores

*   **Domain Layer**: Excepciones personalizadas (`ValueError` para entidades inválidas).
*   **Application Layer**: Propaga excepciones de dominio sin wrappear.
*   **Infrastructure Layer**: Catch de excepciones genéricas en API endpoints con logging y HTTP 500.

---

## 10. Tech Stack y Dependencias

### 10.1 Lenguajes y Runtimes

| Lenguaje | Versión | Gestor | Propósito |
|---|---|---|---|
| **Python** | 3.11+ | `uv` (rápido, PEP 723 inline metadata) | Primitivas, frameworks, Textbook Generator |
| **TypeScript** | ESNext | `bun` (alta velocidad) | Frameworks web-native (Mastra, Flue, Pi) |
| **Go** | 1.25.1 | `go` nativo (opcionalmente `goenv`) | Framework Gollem (máquinas de estado) |

### 10.2 Dependencias Python (Textbook Generator)

**Gestor**: `uv` con `pyproject.toml` en `01_python_frameworks/`  

| Paquete | Versión | Propósito |
|---|---|---|
| `pydantic` | 2.x | Validación de datos y modelos de dominio |
| `pydantic-ai` | latest | Framework de agentes con typed outputs |
| `fastapi` | 0.100+ | API REST asíncrona |
| `uvicorn` | 0.20+ | Servidor ASGI |
| `sqlalchemy` | 2.x | ORM para SQLite/PostgreSQL |
| `pytest` | 7.x | Framework de testing |
| `pytest-playwright` | latest | Tests E2E de browser |
| `langchain` | 0.2+ | Suite LangChain (demo) |
| `langgraph` | 0.2+ | Grafos de estado (demo) |
| `crewai` | 0.50+ | Multi-agentes (demo) |
| `llama-index` | 0.10+ | RAG avanzado (demo) |
| `duckdb` | latest | OLAP in-process (demo) |
| `lancedb` | latest | Vector DB serverless (demo) |

### 10.3 Dependencias TypeScript

**Gestor**: `bun` con `package.json` en `02_typescript_frameworks/`  

| Paquete | Versión | Propósito |
|---|---|---|
| `@mastra/core` | latest | Framework Mastra (agents + workflows) |
| `@flue/runtime` | latest | Framework Flue (web-native agents) |
| `@earendel-works/pi-coding-agent` | latest | Pi coding agent (terminal-first) |
| `typescript` | 5.x | Compilador TypeScript |
| `zod` | 3.x | Validación runtime de schemas |

### 10.4 Dependencias Go

**Módulo**: `go.mod` en `03_go_frameworks/`  

| Paquete | Versión | Propósito |
|---|---|---|
| `github.com/fugue-labs/gollem` | latest | Runtime de agentes con state machines |

---

## 11. Guía de Ejecución y Despliegue

### 11.1 Ejecutar Primitivas desde Cero

```bash
# Inferencia de LLMs
uv run 00_primitives_scratch/01_llm_inference_scratch.py

# RAG con PGVector (requiere PostgreSQL con pgvector)
uv run 00_primitives_scratch/02_rag_postgres_pgvector.py

# Agent Runtime
uv run 00_primitives_scratch/03_agent_runtime_scratch.py

# Observabilidad
uv run 00_primitives_scratch/04_observability_and_evals.py

# Gobernanza
uv run 00_primitives_scratch/05_governance_and_security.py
```

### 11.2 Ejecutar Demos de Frameworks Python

```bash
# PydanticAI
uv run 01_python_frameworks/pydantic_ai_demo.py

# LangGraph
uv run 01_python_frameworks/langgraph_demo.py

# CrewAI
uv run 01_python_frameworks/crewai_demo.py

# Servidor MCP Educativo
uv run 01_python_frameworks/mcp_educational_platform_demo.py --serve
```

### 11.3 Ejecutar Demos TypeScript

```bash
cd 02_typescript_frameworks
bun install
bun run mastra_demo.ts
bun run flue_demo.ts
bun run pi_demo.ts
```

### 11.4 Ejecutar Demo Go

```bash
cd 03_go_frameworks
go run main.go
```

### 11.5 Levantar Textbook Generator (Servidor Local)

```bash
make serve-textbook
# O directamente:
uv run --project 01_python_frameworks python -m uvicorn textbook_generator.main:app --reload --port 8000
```

**Acceso**: `http://localhost:8000` (SPA EduText.AI)

### 11.6 Levantar Infraestructura Completa con Docker

```bash
docker-compose up -d
```

**Endpoints**:
*   PostgreSQL: `localhost:5432`
*   MCP Educativo: `http://localhost:8000`
*   MCP Wallet: `http://localhost:8001`

### 11.7 Ejecutar Suite Completa de Testing

```bash
# Todos los tests
make test

# Solo primitivas
make test-primitives

# Solo Textbook Generator
make test-textbook

# Tests de browser (Playwright)
uv run --project 01_python_frameworks playwright install chromium  # Una vez
uv run --project 01_python_frameworks --with pytest --with pytest-playwright --with requests pytest tests/textbook_generator/browser/ -v
```

### 11.8 Desplegar MCP a la Nube

```bash
./scripts/deploy_mcp.sh
```

Opciones interactivas: Railway, Fly.io, Google Cloud Run.

---

## 12. Relación con HACS y la Metodología ODLC

El **AI Engineering Lab** representa la infraestructura tecnológica de referencia que da soporte a las fases de la metodología ODLC:

1.  **Fase 2 - Constraints**: Se implementa a través de la primitiva de gobernanza y seguridad (`05_governance_and_security.py`) inyectando límites de presupuesto, ToolGaters RBAC, PII redaction y kill switches.
2.  **Fase 4 - Execution**: Utiliza el orquestador híbrido de PydanticAI y workflows deterministas detallados en la aplicación del Textbook Generator (caso de uso `GenerateBookWorkflowUseCase`).
3.  **Fase 5 - Validation**: Se realiza mediante los evaluadores automatizados (F1 Token, G-Eval, Hit Rate, MRR) y las colas de revisión de calidad HITL con umbral 0.85.
4.  **Fase 6 - Learning**: Se concreta en los motores de memoria persistente episódica y semántica del Agent Runtime (`03_agent_runtime_scratch.py`).

---

## 13. Enlaces Oficiales y Recursos

### 13.1 Motores de Bases de Datos

*   [PostgreSQL](https://www.postgresql.org/) - Base relacional SQL
*   [pgvector](https://github.com/pgvector/pgvector) - Extensión vectorial para Postgres
*   [Qdrant](https://github.com/qdrant/qdrant) - Base vectorial dedicada en Rust
*   [Weaviate](https://github.com/weaviate/weaviate) - Base vectorial modular en Go
*   [LanceDB](https://github.com/lancedb/lancedb) - Base vectorial serverless e in-process
*   [DuckDB](https://github.com/duckdb/duckdb) - Base de datos analítica SQL in-process
*   [bbolt](https://github.com/etcd-io/bbolt) - Almacén Key-Value transaccional embebido en Go
*   [Badger](https://github.com/dgraph-io/badger) - Almacén Key-Value LSM Tree rápido en Go
*   [DriftDB](https://github.com/DavidLiedle/DriftDB) - Motor de sincronización P2P en tiempo real

### 13.2 Frameworks de Agentes Evaluados

*   [Mastra](https://github.com/mastra-ai/mastra) - TypeScript ligero y tipado
*   [PydanticAI](https://github.com/pydantic/pydantic-ai) - Python con seguridad de tipos
*   [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - Minimalista sobre APIs OpenAI
*   [Deep Agents](https://github.com/langchain-ai/deepagents) - Batteries-included sobre LangGraph
*   [CrewAI](https://github.com/crewaiinc/crewai) - Orquestación multi-agente
*   [LangGraph](https://github.com/langchain-ai/langgraph) - Grafos de estado con ciclos
*   [LlamaIndex](https://github.com/run-llama/llama_index) - RAG avanzado
*   [Gollem](https://github.com/fugue-labs/gollem) - Máquinas de estado deterministas
*   [Flue](https://github.com/withastro/flue) - Integraciones nativas web (Astro)
*   [Pi](https://github.com/earendel-works/pi/) - Agente de codificación terminal-first ultra-ligero

### 13.3 Referencias y Fuentes

*   [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) - Currículo de construcción de sistemas de IA
*   [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) - Tutoriales prácticos de despliegues modernos
*   [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) - Motor de seguridad y gobernanza de Microsoft
*   [Model Context Protocol](https://modelcontextprotocol.io/) - Protocolo estándar para herramientas de agentes
*   [Unsloth](https://github.com/unslothai/unsloth) - Aceleración de fine-tuning
*   [Hugging Face](https://huggingface.co/) - Modelos y datasets de código abierto

---

## 14. Resumen Ejecutivo

El **AI Engineering Lab** es un repositorio de referencia completo que cubre el espectro completo de la Ingeniería de IA:

| Dimensión | Cobertura |
|---|---|
| **Primitivas desde Cero** | 5 scripts (~200 líneas c/u) sin dependencias: Inferencia, RAG, Agent Runtime, Observabilidad, Gobernanza |
| **Frameworks Evaluados** | 15 demos Python + 3 TypeScript + 1 Go = 19 evaluaciones comparativas |
| **Aplicación de Producción** | Textbook Generator con Clean Architecture, 10 casos de uso, 136 líneas de modelos de dominio, integración NEM/SEP completa |
| **Testing** | Pirámide completa: unit, integration, e2e API, e2e browser (Playwright), ATDD |
| **Infraestructura** | Docker Compose (PostgreSQL+pgvector, 2 MCP servers), Makefile (11 targets), pre-commit hooks, despliegue cloud |
| **Wiki** | 13 artículos técnicos cubriendo primitivas, ecosistema, ADRs, diseño de sistemas, NEM/SEP, stakeholders |
| **Repositorios de Referencia** | 12 repos clonados para análisis local de patrones y benchmarking |
| **Documentación** | README (276 líneas), CLAUDE.md (71 líneas), AGENTS.md, CONTRIBUTING.md |

**Filosofía**: Construir desde los fundamentos para desmitificar abstracciones, comprender la mecánica profunda y tomar decisiones arquitectónicas informadas.

**Stack**: Python 3.11+, TypeScript ESNext, Go 1.25.1, PostgreSQL+pgvector, SQLite, PydanticAI, FastAPI, Playwright.

**Licencia**: MIT