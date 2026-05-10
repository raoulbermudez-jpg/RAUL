---
document_id: "INBOX-07-FROM-THIRD-PARTIES-INDEX"
document_type: "inbox-channel-index"
folder: "01-inbox/07-from-third-parties/"
purpose: "Canal de comunicación con contrapartes externas no-regulatorias y no-junta (contratistas Panama, asesores externos, vendedores, etc.). Cada party tiene su subcarpeta con _outgoing/ y respuestas/correspondencia. Vista lite del kanban filtrada a third parties."
ssot_for: []
depends_on: ["04-system/03-governance/PENDING-DECISIONS-REGISTRY.md", "04-system/03-governance/DECISION-MAKERS.md"]
last_updated: "2026-05-09"
---

# 07-from-third-parties/ — Canal Contrapartes Externas

## Decisores asociados

| ID | Decisor | Scope |
|---|---|---|
| `PANAMA-CONTRA` | Contrapartes apt Embassy Club Panama (inmobiliaria, contratistas, vecinos) | Negociaciones, contratos, mantenimiento, pagos |
| `LEGAL-EXT` | Legal externo (estudio jurídico) | Asesoría legal, contratos, casos contenciosos |
| (otros TBD) | A definir conforme aparezcan | |

Ver [`DECISION-MAKERS.md`](../../04-system/03-governance/DECISION-MAKERS.md) para SLA típico (variable) y patrón de escalación.

## Estructura

```
07-from-third-parties/
├── _index.md                    ← este archivo
└── <party-name>/                ← una subcarpeta por contraparte
    ├── _outgoing/               ← packages enviados a esa party
    │   └── <fecha>_<topic>.md
    └── <fecha>_<topic>.md       ← correspondencia recibida
```

**Convención `<party-name>`:** kebab-case identificador estable. Ejemplos:
- `panama-embassy-inmobiliaria/`
- `panama-contratista-pintura/`
- `legal-ext-rodriguez-asociados/`

## Cómo se usa

### Outgoing (Raul → Party)

1. Owner (o agente con scope external como Aurelio en casos de partnership) crea package en `<party-name>/_outgoing/<fecha>_<topic>.md`.
2. Owner ejecuta envío vía email/whatsapp/llamada (canal real fuera del sistema).
3. Si la interacción genera decision in-flight (ej. negociación de contrato), registrar en `PENDING-DECISIONS-REGISTRY.md` con decisor apropiado.

### Incoming (Party → Raul)

1. Owner deposita correspondencia recibida en `<party-name>/<fecha>_<topic>.md`.
2. Si la respuesta cierra una decisión in-flight (decision-id referenciado en filename), InboxBot detecta y actualiza registry a `RESPONDED`.
3. Si es correspondencia operativa rutinaria (no decisión), queda como histórico de relación con la party.

## Parties activas

### Panama Embassy Club ecosystem

| Party-name | Tipo | Decisor ID | Última interacción |
|---|---|---|---|
| (vacío al inicio — sembrar conforme se establezcan canales) | | | |

> Per memoria `project_panama_domain.md`: dominio Panama recién activado. Drive creado, RAUL pendiente de activación. Cuando se materialicen contratos/contrapartes específicas, crear subcarpeta por party.

### Legal externo

| Party-name | Tipo | Decisor ID | Última interacción |
|---|---|---|---|
| (vacío al inicio) | | | |

## Política de retención

- Correspondencia de relaciones activas: **sin TTL automático** (es histórico de relación).
- Correspondencia de relaciones cerradas (party ya no activa): mover a `05-archive/05-relations-history/<party-name>/` cuando se confirme cierre definitivo.
- `_outgoing/` se limpia **30 días** después de respuesta recibida si el package fue copia de algo que vive en otro lado.

## Anti-patterns

- ❌ NO usar este canal para regulators (eso es `06-from-regulators/`) ni junta (eso es `05-from-junta/`).
- ❌ NO crear subcarpetas por persona individual dentro de una organización (usar nombre de la organización + persona como sub-tópico en filenames).
- ❌ NO depositar aquí información sensible legal sin haber validado con `LEGAL-EXT` que es seguro hacerlo (algunos casos contenciosos requieren chain-of-custody más estricta).

## Referencias

- [`PENDING-DECISIONS-REGISTRY.md`](../../04-system/03-governance/PENDING-DECISIONS-REGISTRY.md) — SSoT de estados.
- [`DECISION-MAKERS.md`](../../04-system/03-governance/DECISION-MAKERS.md) — fila PANAMA-CONTRA, LEGAL-EXT.
- `project_panama_domain.md` (memoria) — contexto del dominio Panama.
- `GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md` sección D.
