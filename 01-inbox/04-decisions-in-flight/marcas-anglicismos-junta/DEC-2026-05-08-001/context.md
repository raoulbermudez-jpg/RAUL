---
decision_id: "DEC-2026-05-08-001"
project_id: "marcas-anglicismos-junta"
project_full_name: "Marcas tecnológicas Genteca SAPI — deck Junta (top-7 candidatos)"
agent_solicitante: "Owner"
decisor_ids: ["JUNTA-GENT", "SAPI-VE"]
fecha_solicitud: "2026-05-08"
estado: "PARTIALLY-RESPONDED"
deadline: "TBD próxima reunión Junta + presupuesto IP"
migration_type: "retroactive"
migrated_on: "2026-05-09"
---

# DEC-2026-05-08-001 — Marcas tecnológicas Genteca (top-7 + decisión SAPI)

## Qué decisión está bloqueada

Owner pidió a la cadena CSC un análisis para decidir qué marcas tecnológicas registrar en SAPI Venezuela. Cadena cerrada 2026-05-07: deck v1+v2 dual (Caso A/B sobre NTC) con top 7 candidatos.

Decisión multi-decisor (patrón A.4):

- **JUNTA-GENT** — aprobar top-N marcas a registrar (input estratégico).
- **SAPI-VE** — registro formal vía abogado IP (decisor-organismo, post-aprobación junta).

## Por qué está bloqueada

Estado actual: **PARTIALLY-RESPONDED**.

- **Junta:** pending — no ha respondido sobre el deck top-7.
- **SAPI:** no submitted aún — depende de aprobación junta + 3 escalaciones críticas Owner pendientes (memoria):
  1. Verificar estado SAPI de marca "Exceline" (existing? clearance?).
  2. Addendum HDE Vera (validación técnica de claims que sostendrían cada marca).
  3. Presupuesto IP — costos $880-$1,640/marca, plazo 6-12 meses (ver memoria `reference_sapi_venezuela_quick.md`).

## Decisores y sub-tracking

| Sub-decisor | Estado | Próximo paso |
|---|---|---|
| JUNTA-GENT | PENDING | Esperar próxima reunión Junta o presentar en convocatoria extraordinaria |
| SAPI-VE | PENDING (no submitted) | Bloqueado por aprobación Junta + 3 escalaciones Owner |

## Dónde vive el material original

- **Project folder:** `03-projects/genteca/2026-05-07_marcas-anglicismos-junta/`
  - `build_deck.py` — generador del deck v1+v2.
  - `03-review-and-release/` — versiones finales del deck.
- **Memoria:** `project_marcas_anglicismos_junta.md` — estado completo + top 7 candidatos + 3 escalaciones críticas.
- **Reference SAPI:** `reference_sapi_venezuela_quick.md` — clase 9, costos, plazos, doctrina equivalencia perceptual.

## Estado canónico

Ver fila `DEC-2026-05-08-001` en [`PENDING-DECISIONS-REGISTRY.md`](../../../../04-system/03-governance/PENDING-DECISIONS-REGISTRY.md).

## Próxima acción

1. Owner resuelve las 3 escalaciones críticas (verificación SAPI Exceline, addendum HDE Vera, presupuesto IP).
2. Owner agenda presentación a Junta (canal `01-inbox/05-from-junta/_outgoing/`).
3. Tras response Junta, abrir sub-track SAPI con LEGAL-EXT (canal `01-inbox/06-from-regulators/_outgoing/`).

## Nota de migración

Retroactivo 2026-05-09. La granularidad sub-decisor (junta + SAPI) podría considerarse split en 2 decision-IDs separados (`-001-junta` y `-001-sapi`); por ahora unificada con sub-tracking en tabla.
