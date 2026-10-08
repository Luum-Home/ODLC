---
tipo: protocolo
version: 1
estado: borrador              # borrador | sellado | en_curso | cerrado
diseno: linea_base_multiple   # linea_base_multiple | abab
inicio:                       # lunes de la semana 1 (decisión pendiente del dueño)
semanas: 12                   # 8 a 12
periodos_por_semana: 2        # puntos de medición por semana
fecha_corte:                  # fin de la última semana + ventana_outcome_dias
tiers: [producto, clientes, operacion]
ventanas:                     # período de inicio permitido por posición; con 12 semanas y 2 por semana
  1: [6, 7, 8]
  2: [11, 12, 13]
  3: [16, 17, 18]
asignacion:                   # se sortea con el comando de la nota y se sella; no se elige
  producto:
  clientes:
  operacion:
fases_abab: []                # solo si diseno es abab: [1-6-A, 7-12-B, 13-18-A, 19-24-B]
semilla_atd:                  # en el protocolo sellado va su sha256; el valor se revela al cierre
fase0_perfiles: [fundador_solo, tiny_team, bootstrapper]
fase0_temas: [revision_desbordada, decidir_vs_construir, validar_pocos_clientes, sumar_gente]
fase0_temas_centrales: [revision_desbordada, decidir_vs_construir]
umbrales:                     # decididos en P-05 y P-09 del Registro de decisiones; sin fuente salvo kappa_min
  fase0:
    min_entrevistas: 12       # fijas (P-05)
    extension: 5
    kappa_min: 0.6
    confirma_dolor_casos: 6   # en casos, no en porcentajes (P-05)
    confirma_compromiso_casos: 3
    descarta_dolor_casos: 2   # 2 o menos descarta
  nivel_outcome_min: 2
  ventana_outcome_dias: 28
  k4_semana: 8                # corte parcial de K4 (P-09)
  alfa: 0.05
  adherencia_min: 0.7
  caida_entrega_max: 0.5
  latencia_baja_s: 30
  aprobacion_alerta: 0.95
  aprendizaje_min_caracteres: 40
  tasa_siembra_max: 0.15
  min_semillas_k3: 4
  min_semillas_contraste: 5
  tolerancia_horas: 0.2
  arrastre_max: 0.5
  auditorias_por_semana_min: 1
---

Copia del protocolo de la nota "Piloto - Combinación A" con los parámetros elegidos. Se sella antes de la semana 1.
