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

El **Harness-Software Design Development (Harness-SDD)** — patrón propuesto por el repositorio de referencia [betta-tech/harness-sdd](https://github.com/betta-tech/harness-sdd) (ver [[Recursos externos]]) — propone que todo desarrollo realizado por agentes autónomos deba iniciarse y gobernarse por un arnés.

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

## 3. Validación de Reclamos de Éxito (Ground Truth Checker)

Uno de los principales problemas al delegar tareas críticas a los agentes autónomos de desarrollo es el **auto-reporte ficticio** o alucinaciones de éxito. Un agente puede escribir en su reporte: *"He creado la API de usuarios y todos los 15 tests unitarios pasan exitosamente"*, cuando en realidad no ha creado el archivo correcto o las pruebas fallaron.

Para mitigar esto, dentro de la Safety Mesh (ver [[Módulo 3 - Gobernanza#3. La Malla de Seguridad de 14 Capas (14-Layer Safety Mesh)|Módulo 3 § Safety Mesh]]) de la arquitectura [[Cognitive OS - Arquitectura de referencia]] se integra la herramienta **Ground Truth Checker** (`lib/ground_truth.py` y el hook `claim-validator.sh`).

### ¿Cómo opera el Ground Truth Checker?

1. **Extracción Semántica de Reclamos**: Tras cada finalización de tarea por parte del agente, el sistema lee la salida textual y extrae declaraciones de éxito mediante patrones estructurados:
   - *"Created file `path/to/file`"*
   - *"N tests passing"*
   - *"Build succeeded"*
2. **Auditoría Determinista contra la Realidad**:
   - **Verificación de archivos**: Verifica la existencia física del archivo modificado o creado usando funciones del sistema (`os.path.exists`).
   - **Verificación de funciones/tests**: Realiza búsquedas de texto directo y análisis estático (grep) sobre la suite para validar que las firmas de las funciones y los recuentos declarados coincidan con el archivo final.
3. **Puntaje de Alucinación (Hallucination Score)**: El componente genera una métrica entre `0.0` (todos los reclamos validados coinciden con la realidad en disco) y `1.0` (ninguno de los reclamos declarados es real).
4. **Comportamiento en Ganchos (claim-validator.sh)**:
   - En fases de **Reconstrucción/Estabilización**: Se reporta una alerta descriptiva (**WARN** con exit 0), permitiendo al desarrollador corregir el flujo.
   - En fases de **Producción/Mantenimiento**: Si se detecta cualquier discrepancia o alucinación de archivo, el gancho detiene la entrega (**BLOCK** con exit 2) y rechaza la propuesta del agente.

---

## 4. El Patrón del "Día de la Justicia" (Judgment Day) y Arbitraje entre Agentes

Además de las verificaciones deterministas del compilador y el linter, los arneses de pruebas más avanzados implementan **mecanismos de arbitraje cognitivo** para evaluar el código generado por un agente antes de que sea entregado o integrado al repositorio principal. El exponente más claro de esta técnica es el patrón **"Día de la Justicia" (Judgment Day)**.

### Evaluación Ciega y Paralela (Dual Blind Review)
El principio de este patrón establece que **el agente que escribe el código nunca debe juzgar su propio trabajo**. En su lugar, el arnés de gobernanza orquesta un flujo de revisión ciega:
1. **Lanzamiento de Jueces en Paralelo**: Se instancian dos agentes de revisión independientes y aislados (Juez A y Juez B) que reciben la misma porción de código y criterios de aceptación, sin ver los reportes del otro.
2. **Clasificación de Perfiles (Optimista vs. Pesimista)**:
   - **El Agente Optimista**: Evalúa bajo la premisa de "inocente hasta que se demuestre lo contrario". Valida que el flujo principal de negocio funcione, que la arquitectura propuesta cumpla el objetivo y que la velocidad de entrega sea óptima.
   - **El Agente Pesimista**: Trabaja bajo el modelado de amenazas y asume "culpable hasta que se demuestre lo contrario". Busca vulnerabilidades de seguridad, condiciones de carrera (race conditions), fugas de memoria, inputs maliciosos y falta de manejo de excepciones.
3. **Compuertas de Arbitraje**: Al finalizar, un componente orquestador consolida los veredictos mediante reglas de decisión:
   - **Confirmados (Confirmed)**: Defectos encontrados por ambos jueces de forma independiente. Pasan automáticamente al Agente de Corrección (*Fix Agent*) para su refactorización quirúrgica.
   - **Sospechosos (Suspect)**: Problemas señalados por un solo juez. Se marcan para revisión pero no se auto-corrigen de inmediato para evitar falsos positivos.
   - **Contradictorios (Contradictions)**: Si un juez aprueba el cambio y el otro encuentra una discrepancia estructural crítica, el arnés congela la entrega y escala una alerta interactiva para que un humano actúe como árbitro supremo.

### Integración Nativa en Modelos de Frontera (Actor-Critic)
Modelos de frontera más avanzados (como *Claude Fable 5*) traen dinámicas de este estilo en sus pipelines internos de razonamiento. A través de arquitecturas de tipo **Actor-Critic**, el modelo realiza múltiples pasadas de autorreflexión antes de emitir una respuesta en su canal de salida: un sub-proceso genera una hipótesis de código (optimista) y otro sub-proceso simula ataques o fallas de ejecución (pesimista), arbitrando la respuesta final para entregar código con una tasa de error significativamente menor.

---

## 5. Prácticas en el Repositorio Local

> [!warning] Setup previo
> Estas prácticas requieren los repositorios de referencia clonados en `external/` (carpeta fuera del control de versiones). Instrucciones de clonado en [[Recursos externos]].

En la carpeta `external/` de este proyecto se clonan repositorios clave de referencia sobre esta materia (ver [[Recursos externos]]):
- `external/harness-sdd/`: Contiene el framework conceptual y ejemplos prácticos de cómo estructurar desarrollos guiados por arneses.
- `external/ejemplo-harness-subagentes/`: Un ejemplo en Python de cómo un agente coordinador orquesta y valida subagentes.
- `external/gentle-pi/`: Contiene la especificación de diseño real y el flujo de ejecución del skill de arbitraje ciego en `skills/judgment-day/SKILL.md`.

Te recomendamos explorar dichos directorios para asimilar cómo la verificación determinista de código se complementa con el arbitraje cognitivo.

---
Siguiente módulo: [[Módulo 3 - Gobernanza]]
Relacionado: [[Cognitive OS - Arquitectura de referencia]] · [[Recursos externos]] · [[Manifiesto HACS-ODLC]] · [[Riesgos]] · [[Gobernanza]]

