---
tipo: decision
id: D-000
unidad: U-000                 # unidad a la que pertenece
pr: PR-000                    # si es la revisión de un PR; vacío si es otra decisión
clase: reversible             # reversible | irreversible | significativa | auditoria_muestreo
condicion_revision:           # H (humano solo) | A (agente solo) | HA (humano + agente); solo en PR de fase B, sorteada
propuesta_por: agente         # agente | humano | sorteo (auditoría)
decidida_por: humano          # humano | agente (condición A)
propuesta_en: 2026-11-02T09:00:00-03:00   # timestamp del evento de la herramienta (PR abierto, propuesta registrada)
decidida_en: 2026-11-02T09:10:00-03:00    # timestamp de la aprobación o rechazo en la herramienta, no el recordado
resultado: aprobada           # aprobada | modificada | rechazada
opciones_presentadas: 1       # en HA y en decisiones significativas, al menos 2
eleccion_forzada:             # solo HA: el humano escribe, no tilda
  metrica_escrita: ""         # el número de la métrica que espera mover este cambio
  que_cambiaria_veredicto: "" # qué evidencia lo haría rechazar
hallazgos: []                 # archivos (ruta) donde la revisión marcó un problema
modelo_revisor:               # si decidió o asistió un agente: id del registro-ia vigente
---

Justificación de la verificación (responsabilidad sobre el proceso, no sobre el resultado): qué se miró y cómo.
