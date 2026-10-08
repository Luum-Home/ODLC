---
tipo: ficha
id: F-000
dueno:                    # persona que responde por el objetivo
creada_en:                # AAAA-MM-DD, antes del primer commit del objetivo
resultado_cliente:        # qué cambia para el cliente, en una frase
metrica:                  # qué se mide
baseline:                 # valor de hoy, con su fuente
target:                   # valor que se espera mover
ventana_hasta:            # AAAA-MM-DD en que se mide el target
abandono_criterio:        # qué resultado haría abandonar el objetivo
abandono_fecha:           # AAAA-MM-DD en que se mira ese criterio
no_tocar: []              # superficies fuera de alcance (no-gos)
tope_tiempo:              # días de trabajo activo como máximo; al llegar, se decide (D-08)
tope_costo:               # USD como máximo (tokens y servicios); al llegar, se decide (D-08)
veredicto:                # vacío hasta decidir: sigue | abandona | cumplido
veredicto_fecha:
---

Ficha de objetivo del Núcleo ODLC. Se escribe antes de construir. El veredicto se completa a más tardar en `abandono_fecha`.
