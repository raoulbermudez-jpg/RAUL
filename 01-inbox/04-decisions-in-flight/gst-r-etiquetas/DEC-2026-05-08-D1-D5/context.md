---
decision_id: "DEC-2026-05-08-D1-D5"
project_id: "gst-r-etiquetas"
project_full_name: "GST Labels — 5 decisiones Owner pendientes (umbrella)"
agent_solicitante: "Owner (auto)"
decisor_ids: ["OWNER"]
fecha_solicitud: "2026-05-04"
estado: "PENDING"
deadline: "2026-07 (launch deadline)"
migration_type: "retroactive"
migrated_on: "2026-05-09"
umbrella: true
sub_decisions_pending_definition: true
---

# DEC-2026-05-08-D1-D5 — GST Labels (umbrella, 5 sub-decisiones)

## Qué decisión está bloqueada

Memoria `project_gst_labels_july_deadline.md` registra **5 decisiones Owner pendientes (D1-D5)** sobre las etiquetas GST. Owner es auto-solicitante y auto-decisor (es Owner quien necesita decidir).

Estado actual: **umbrella row** — las 5 sub-decisiones existen como referencia en memoria pero NO tienen scope concreto detallado. Cuando se materialicen, esta decisión se expande a 5 entries separadas:

- `DEC-2026-05-08-D1` (TBD)
- `DEC-2026-05-08-D2` (TBD)
- `DEC-2026-05-08-D3` (TBD)
- `DEC-2026-05-08-D4` (TBD)
- `DEC-2026-05-08-D5` (TBD)

## Por qué está bloqueada

- Lanzamiento July 2026 — deadline duro.
- Oz entregó propuesta v1 (Línea 2 seleccionada).
- Pendiente GST-RD + 5 decisiones Owner sobre detalles de etiqueta.
- Sin las 5 D resueltas, no se puede pasar a arte final con Oz.

## Decisor

- **OWNER** — todas las 5 D son scope Owner (no requieren input externo).

## Dónde vive el material original

- **Project folder:** `03-projects/genteca/2026-04_GST-R_etiquetas/`
  - `00-brief/`, `01-strategy-and-design/`, `02-production/`
- **Propuesta Oz v1:** `01-inbox/02-deliverables-to-owner/2026-04-20-gst-r-etiquetas-brief-ozwaldo-v2.pdf` (+ versiones .pptx).
- **Memoria:** `project_gst_labels_july_deadline.md` — estado completo + Línea 2 seleccionada + D1-D5 pendientes.

## Estado canónico

Ver fila `DEC-2026-05-08-D1-D5` en [`PENDING-DECISIONS-REGISTRY.md`](../../../../04-system/03-governance/PENDING-DECISIONS-REGISTRY.md).

## Próxima acción

1. Owner detalla scope concreto de cada D1..D5.
2. Cuando D-N tenga scope, se crea sub-folder `01-inbox/04-decisions-in-flight/gst-r-etiquetas/DEC-2026-05-08-D1/` con su propio context + 4 archivos canónicos.
3. Owner resuelve secuencialmente o en paralelo según urgencia July deadline.
4. Cuando las 5 D estén RESPONDED, esta umbrella row se cierra con outcome consolidado.

## Nota de migración

Retroactivo 2026-05-09. Umbrella row mantenida por decisión Owner Phase 3 step 2 (no expandir hasta que D1-D5 tengan scope concreto).
