---
tipo: unidad
id: U-000                     # correlativo; el nombre del archivo es el id
tier: producto                # producto | clientes | operacion (los tres tipos de objetivo del protocolo)
modo_declarado: flujo         # flujo (sin método) | metodo (con método); el script NO lo usa para asignar la condición
creada_en: 2026-11-02T09:00:00-03:00    # al crear el archivo; se contrasta con el primer commit que lo agrega
entregada_en:                 # merge a main que la pone en manos de clientes; vacío si se abandonó antes
estado: en_curso              # en_curso | entregada | descartada (revertida o eliminada después de entregar) | abandonada (antes de entregar)
descartada_en:                # obligatorio si estado es descartada o abandonada
motivo_descarte:              # texto corto; en abandonada con método, citar el criterio de abandono que se activó
# --- solo con método (fase B); sin método se deja vacío ---
resultado_esperado: ""        # qué cambia para el cliente potencial si sale bien (outcome, no output)
metrica:
  nombre: ""                  # número observable
  baseline:                   # valor actual
  target:                     # valor que cuenta como logrado
  ventana_dias: 28            # cuánto se espera la evidencia después de entregar
criterio_abandono: ""         # estado + fecha (Duke): "si al <fecha> no hay <evidencia>, se abandona"
commits: []                   # hashes que implementan la unidad
---

Contexto breve. Sin método: una línea con el ítem. Con método: el objetivo en la forma de la Fase 1.
