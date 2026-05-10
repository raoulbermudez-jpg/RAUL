---
decision_id: "DEC-2026-05-03-001"
project_id: "covenin-3445"
project_full_name: "COVENIN 3445 verification — Argumento 8 (claims regulatorios)"
agent_solicitante: "Bruna"
decisor_ids: ["SENCAMER", "FONDONORMA", "LEGAL-EXT"]
fecha_solicitud: "2026-05-03"
estado: "PENDING"
deadline: "TBD (plazos regulatorios — meses)"
migration_type: "retroactive"
migrated_on: "2026-05-09"
---

# DEC-2026-05-03-001 — Verificación COVENIN 3445 (Argumento 8)

## Qué decisión está bloqueada

Bruna solicitó verificación normativa formal para sostener el "Argumento 8" en claims de productos Genteca. Argumento 8 quedó **bloqueado pending verificación oficial** vs norma COVENIN 3445.

Decisión multi-decisor (patrón A.4):

- **SENCAMER** — certificación técnica.
- **FONDONORMA** — verificación de norma.
- **LEGAL-EXT** — interpretación legal del cumplimiento.

Per BR-2 entry #28.

## Por qué está bloqueada

- Sin verificación, Bruna NO puede liberar Argumento 8 para uso público.
- Submissions a SENCAMER y FONDONORMA requieren clearance previo de LEGAL-EXT (regla del canal `06-from-regulators/`).
- Plazos regulatorios típicos: meses.

## Decisores y sub-tracking

| Sub-decisor | Estado | Vía |
|---|---|---|
| LEGAL-EXT | PENDING | Email vía Owner (paso 1 — clearance previo) |
| SENCAMER | PENDING (no submitted) | Web SENCAMER post-clearance legal |
| FONDONORMA | PENDING (no submitted) | Web FONDONORMA post-clearance legal |

## Dónde vive el material original

- **Risk analysis:** BR-2 entry #28 (en governance log Bruna).
- **Governance:** `03-projects/genteca/_governance/2026-05-03_genteca_claim-approval-log_v1.md`
- **No project folder dedicado** — esta decisión es transversal a productos Genteca que tocan COVENIN 3445.

## Estado canónico

Ver fila `DEC-2026-05-03-001` en [`PENDING-DECISIONS-REGISTRY.md`](../../../../04-system/03-governance/PENDING-DECISIONS-REGISTRY.md).

## Próxima acción

1. Owner contacta LEGAL-EXT con scope del Argumento 8 + relación con COVENIN 3445.
2. Tras clearance legal, agente prepara submissions paralelas a SENCAMER y FONDONORMA (canal `01-inbox/06-from-regulators/_outgoing/`).
3. Bruna libera Argumento 8 para uso público SOLO cuando los 3 sub-decisores respondan favorablemente. Si alguno bloquea → CLOSED-NOT-VIABLE o reformulación del argumento.

## Nota de migración

Retroactivo 2026-05-09. Decisión transversal (no project folder dedicado). Material vive en governance log de claims.
