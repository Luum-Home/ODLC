---
tipo: protocolo
version: 1
estado: sellado               # borrador | sellado | en_curso | cerrado
diseno: linea_base_multiple   # linea_base_multiple | abab
inicio: 2026-11-09            # lunes de la semana 1 (FICTICIO)
semanas: 12
periodos_por_semana: 2        # un punto de medición cada media semana: 24 puntos
fecha_corte: 2027-02-28T23:59:00-03:00   # fin de la semana 12 + 28 días de seguimiento
tiers: [producto, clientes, operacion]
ventanas:                     # período de inicio permitido por posición (≥ 5 puntos por fase)
  1: [6, 7, 8]
  2: [11, 12, 13]
  3: [16, 17, 18]
asignacion:                   # sorteada y sellada antes de la semana 1
  clientes: 7
  producto: 12
  operacion: 17
semilla_atd: fixture-ficticio-7f3a    # en el piloto real se revela al cierre; antes solo su hash
fase0_perfiles: [fundador_solo, tiny_team, bootstrapper]
fase0_temas: [revision_desbordada, decidir_vs_construir, validar_pocos_clientes, sumar_gente]
fase0_temas_centrales: [revision_desbordada, decidir_vs_construir]
umbrales:                     # decididos en P-05, P-09 y P-10 del Registro de decisiones; sin fuente salvo kappa_min
  fase0:
    entrevistas_fijas: 12     # tramo 1: las primeras 12 por fecha; su veredicto se congela (P-05, P-10)
    extension: 5              # una sola vez, solo si el tramo 1 da ambiguo
    kappa_min: 0.6            # Hartmann y otros 2004, citado por WWC 2010
    confirma_dolor_casos: 6   # tramo 1, en casos y no en porcentajes (P-05)
    confirma_compromiso_casos: 3
    descarta_dolor_casos: 2   # 2 o menos descarta
    extension_confirma_dolor_casos: 9         # tramo 2, sobre 17 (P-10; sin fuente)
    extension_confirma_compromiso_casos: 5
    extension_descarta_dolor_casos: 3
  nivel_outcome_min: 2
  ventana_outcome_dias: 28
  k4_semana: 8                # corte parcial de K4 (P-09)
  nap_min: 0.75
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

Protocolo FICTICIO: caso de cadena de desvíos declarados, sin datos todavía. Errata corregida en el texto.
