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

El **Harness-Software Design Development (Harness-SDD)** propone que todo desarrollo realizado por agentes autónomos deba iniciarse y gobernarse por un arnés.

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

---

## 3. Prácticas en el Repositorio Local

En la carpeta `external/` tienes clonados dos repositorios clave de referencia sobre esta materia (ver [[Recursos externos]]):
-   `external/harness-sdd/`: Contiene el framework conceptual y ejemplos de cómo diseñar código guiado por arneses.
-   `external/ejemplo-harness-subagentes/`: Un ejemplo funcional en Python de cómo un agente principal delega subtareas en subagentes enjaulados bajo arneses de testeo y consolida los resultados.

Te recomendamos ingresar a esos directorios, explorar su código y ejecutar sus suites de pruebas locales (`pytest`) para familiarizarte con el patrón de diseño.

---
Siguiente módulo: [[Módulo 3 - Gobernanza]]
Relacionado: [[Cognitive OS - Arquitectura de referencia]] · [[Recursos externos]]
