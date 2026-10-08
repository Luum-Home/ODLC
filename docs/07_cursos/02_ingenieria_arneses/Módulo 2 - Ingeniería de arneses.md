---
tags: [cursos, educacion, arneses, tecnico]
status: borrador
created: 2026-06-10
---

# Módulo 2 — Ingeniería de arneses (Técnico)

Este módulo está dirigido a ingenieros de software y desarrolladores. Aprenderás a construir **arneses de prueba (Test Harnesses)** y configurar entornos aislados de ejecución (Sandboxes) para validar el comportamiento lógico de los agentes de forma automática.

---

## 1. ¿Qué es un Arnés de Pruebas (Test Harness) para Agentes?

En ingeniería de software tradicional, las pruebas unitarias validan que una función de código de entrada y salida determinista funcione como se espera. 

En el desarrollo con agentes de IA, el comportamiento no es 100% determinista. Un **Arnés de Pruebas** es un entorno controlado que:
1.  **Instrumenta al Agente**: Le provee mocks de APIs, archivos de prueba estructurados y bases de datos temporales.
2.  **Ejecuta Validaciones Automáticas**: Evalúa si el código generado compila, si las pruebas unitarias pasan, o si las respuestas cumplen con los criterios de seguridad e integridad técnica (ej. análisis estático de vulnerabilidades).
3.  **Provee Feedback**: Devuelve los errores al agente (ej. mensajes del compilador o fallos de tests) para que intente auto-corregirse en el siguiente ciclo.

---

## 2. Desarrollo Guiado por Arneses (Harness-SDD)

El **Harness-SDD** (arnés + *Spec Driven Development*) — patrón propuesto por el repositorio de referencia [betta-tech/harness-sdd](https://github.com/betta-tech/harness-sdd) (ver [[Recursos externos]]) — propone que todo desarrollo realizado por agentes autónomos deba iniciarse y gobernarse por un arnés.

### Flujo Operativo:
```
[Humano define objetivo/test] 
       ↓
[Arnés de Pruebas inicial (Falla)] 
       ↓
[Agente Builder genera código en Sandbox] 
       ↓
[Arnés de Pruebas ejecuta validación] 
       ↓
[¿Pasa?] ── (No) ──> [Agente recibe error y corrige]
       ↓ (Sí)
[Aprobación en Gobernanza]
```

### Ejemplo Práctico de Validación de Código por un Arnés (Concepto):
```python
import subprocess
import sys

def run_agent_validation(sandbox_path):
    print("Iniciando validación del código del agente...")
    
    # 1. Ejecutar Linter
    linter = subprocess.run(["flake8", sandbox_path], capture_output=True, text=True)
    if linter.returncode != 0:
        return False, f"Fallo de linter: {linter.stdout}"
        
    # 2. Ejecutar Tests Unitarios
    test_run = subprocess.run(["pytest", f"{sandbox_path}/tests/"], capture_output=True, text=True)
    if test_run.returncode != 0:
        return False, f"Tests rotos:\n{test_run.stdout}"
        
    return True, "Validación exitosa"
```

## 3. Validación de reclamos de éxito

Uno de los principales problemas al delegar tareas críticas a los agentes autónomos de desarrollo es el **auto-reporte ficticio** o alucinaciones de éxito. Un agente puede escribir en su reporte: *"He creado la API de usuarios y todos los 15 tests unitarios pasan exitosamente"*, cuando en realidad no creó el archivo correcto o las pruebas fallaron.

La mitigación es un control del arnés que no acepta resultados declarados: lo que el agente afirma se contrasta contra la realidad antes de cerrar la tarea ([[Gobernanza#Controles técnicos]]; en el glosario, *verificación de reclamos*).

### Cómo se arma

1. **Extraer los reclamos**: al terminar cada tarea, el arnés lee la salida del agente y extrae las declaraciones de éxito con patrones estructurados:
   - *"Created file `path/to/file`"*
   - *"N tests passing"*
   - *"Build succeeded"*
2. **Contrastarlos de forma determinista**:
   - **Archivos**: verificar que el archivo creado o modificado exista y tenga el contenido declarado.
   - **Tests y build**: aceptar "los tests pasan" solo si la corrida existe en el registro del CI o del sandbox, con su salida; contar los tests de esa corrida, no los que el agente dice.
3. **Responder según el riesgo**: en exploración, una discrepancia puede quedar como advertencia para que la persona corrija el flujo; cuando el cambio va a producción, cualquier reclamo sin respaldo rechaza la entrega. Esa graduación sigue el estado del proyecto, no las fases de ODLC ([[Registro de decisiones]], D-13).

> [!note] Límite
> Contrastar reclamos detecta el reporte falso, no el test mal escrito: un test que pasa sin probar lo que dice sigue pasando. Por eso se combina con tests que el escritor no puede editar y con el arbitraje de la sección siguiente ([[Objeciones al marco#Objeción 8: la revisión en manos de agentes]], compensación C4).

---

## 4. El Patrón del "Día de la Justicia" (Judgment Day) y Arbitraje entre Agentes

Además de las verificaciones deterministas del compilador y el linter, los arneses de pruebas más avanzados implementan **mecanismos de arbitraje cognitivo** para evaluar el código generado por un agente antes de que sea entregado o integrado al repositorio principal. El exponente más claro de esta técnica es el patrón **"Día de la Justicia" (Judgment Day)**.

### Evaluación Ciega y Paralela (Dual Blind Review)
El principio de este patrón establece que **el agente que escribe el código nunca debe juzgar su propio trabajo**. En su lugar, el arnés de gobernanza orquesta un flujo de revisión ciega:
1. **Lanzamiento de Jueces en Paralelo**: Se instancian dos jueces ciegos e independientes (Juez A y Juez B) con **el mismo objetivo de revisión y los mismos criterios** (*identical target and criteria*, según `skills/judgment-day/SKILL.md`), sin ver los reportes del otro. El orquestador no revisa el código por su cuenta.
2. **Compuertas de Arbitraje**: Al finalizar, el orquestador consolida los veredictos mediante reglas de decisión:
   - **Confirmados (Confirmed)**: Defectos encontrados por ambos jueces de forma independiente. En la primera ronda se pide aprobación antes de corregirlos; los aprobados van a un agente de corrección separado (*Fix Agent*), y después de cada corrección se vuelve a lanzar a los dos jueces en paralelo. Tras dos iteraciones de corrección con problemas pendientes, se pregunta si seguir.
   - **Sospechosos (Suspect)**: Problemas señalados por un solo juez. Se reportan y se triagean, pero no se auto-corrigen.
   - **Contradictorios (Contradictions)**: Si los jueces se contradicen, se escala para una decisión manual de un humano.
3. **Variante propuesta por el vault: perfiles Optimista vs. Pesimista**. La skill de origen no define perfiles distintos para los jueces; esta variante, propia del vault, les asigna sesgos complementarios:
   - **El Agente Optimista**: Evalúa bajo la premisa de "inocente hasta que se demuestre lo contrario". Valida que el flujo principal de negocio funcione y que la arquitectura propuesta cumpla el objetivo.
   - **El Agente Pesimista**: Trabaja bajo el modelado de amenazas y asume "culpable hasta que se demuestre lo contrario". Busca vulnerabilidades de seguridad, condiciones de carrera (race conditions), fugas de memoria, inputs maliciosos y falta de manejo de excepciones.

### Una Analogía Útil: el Patrón Actor-Critic
El arbitraje ciego se puede pensar como una versión explícita del patrón **Actor-Critic** del aprendizaje por refuerzo, donde un componente propone una acción y otro la evalúa, y el resultado surge del arbitraje entre ambos: el agente Builder que escribe el código ocupa el rol de *actor* y los jueces, el de *critic*. La diferencia es que acá cada rol es un agente separado, con su propio contexto y su propio reporte auditable, en lugar de un componente interno del modelo.

> [!note] Sobre el razonamiento interno de los modelos
> Los modelos de frontera actuales razonan antes de responder —es una capacidad documentada por los proveedores—, pero **no hay documentación pública que describa esa deliberación como una arquitectura Actor-Critic con sub-procesos optimista y pesimista**. Conviene presentarlo como analogía didáctica y no como afirmación sobre el funcionamiento interno de un producto concreto.

---

## 5. Prácticas en el Repositorio Local

> [!warning] Setup previo
> Estas prácticas requieren los repositorios de referencia clonados en `external/` (carpeta fuera del control de versiones). Instrucciones de clonado en [[Recursos externos]].

En la carpeta `external/` de este proyecto se clonan repositorios clave de referencia sobre esta materia (ver [[Recursos externos]]):
- `external/harness-sdd/`: Repo de ejemplo (CLI de notas en Python) con specs EARS y una puerta de aprobación humana.
- `external/ejemplo-harness-subagentes/`: Variante del ejemplo harness (CLI de notas) con subagentes leader/implementer/reviewer definidos en `.claude/agents/`.
- `external/gentle-pi/`: Contiene la especificación de diseño real y el flujo de ejecución del skill de arbitraje ciego en `skills/judgment-day/SKILL.md`.

Te recomendamos explorar dichos directorios para asimilar cómo la verificación determinista de código se complementa con el arbitraje cognitivo.

---
Siguiente módulo: [[Módulo 3 - Gobernanza]]
Relacionado: [[Agent Loop Engineering]] · [[Recursos externos]] · [[Manifiesto HACS-ODLC]] · [[Riesgos]] · [[Gobernanza]]

