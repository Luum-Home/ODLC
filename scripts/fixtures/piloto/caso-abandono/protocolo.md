---
tipo: protocolo
version: 1
estado: sellado               # borrador | sellado | en_curso | cerrado
diseno: linea_base_multiple   # linea_base_multiple | abab
inicio: 2026-11-02            # lunes de la semana 1 (FICTICIO)
semanas: 12
periodos_por_semana: 2        # un punto de medición cada media semana: 24 puntos
fecha_corte: 2027-02-21T23:59:00-03:00   # fin de la semana 12 + 28 días de seguimiento
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
umbrales:                     # PROPUESTAS sin fuente salvo kappa_min: decisión pendiente del dueño
  fase0:
    min_entrevistas: 10
    extension: 5
    kappa_min: 0.6            # Hartmann y otros 2004, citado por WWC 2010
    confirma_dolor: 0.5
    confirma_compromiso: 0.3
    descarta_dolor: 0.2
  nivel_outcome_min: 2
  ventana_outcome_dias: 28
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

Protocolo FICTICIO: caso en que la Fase 0 descarta el problema.
