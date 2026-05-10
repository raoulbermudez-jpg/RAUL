---
document_id: "INBOX-06-FROM-REGULATORS-INDEX"
document_type: "inbox-channel-index"
folder: "01-inbox/06-from-regulators/"
purpose: "Canal de comunicación con organismos regulatorios (SAPI-VE, SENCAMER, FONDONORMA). Submissions enviados (en _outgoing/) y respuestas/notificaciones recibidas. Vista lite del kanban filtrada a regulators; SSoT de estados en PENDING-DECISIONS-REGISTRY.md."
ssot_for: []
depends_on: ["04-system/03-governance/PENDING-DECISIONS-REGISTRY.md", "04-system/03-governance/DECISION-MAKERS.md"]
last_updated: "2026-05-09"
---

# 06-from-regulators/ — Canal Organismos Regulatorios

## Decisores asociados

| ID | Organismo | Scope típico |
|---|---|---|
| `SAPI-VE` | Servicio Autónomo de la Propiedad Intelectual (Venezuela) | Registro/oposición de marcas, clearances IP |
| `SENCAMER` | Servicio Autónomo Nacional de Normalización, Calidad, Metrología y Reglamentos Técnicos | Normas COVENIN, certificaciones técnicas |
| `FONDONORMA` | Fondo para la Normalización y Certificación de la Calidad | Verificación de normas, auditorías QMS |

Ver [`DECISION-MAKERS.md`](../../04-system/03-governance/DECISION-MAKERS.md) para SLA típico (meses) y patrón de escalación.

## Estructura

```
06-from-regulators/
├── _index.md                              ← este archivo
├── _outgoing/                             ← submissions a regulators
│   └── <regulator>_<fecha>_<id>_submission.md
└── <regulator>_<fecha>_<id>.md            ← respuestas/notificaciones recibidas
```

## Cómo se usa

### Outgoing (Raul → Regulator)

1. **Submissions formales requieren acompañamiento de Legal externo (`LEGAL-EXT`)** — cualquier package que vaya a regulator pasa primero por revisión de legal vía Owner.
2. Agente solicitante (típicamente Bruna para claims regulatorios, Vael para marcas) genera package en `04-decisions-in-flight/<project>/<decision-id>/`.
3. Owner valida con legal externo, luego copia versión final a `_outgoing/<regulator>_<fecha>_<decision-id>_submission.md` (o adjunto PDF si es submission física).
4. Owner ejecuta submission física vía web del organismo (sapi.gob.ve, sencamer.gob.ve, fondonorma.org.ve) — esos sistemas viven **fuera** del sistema RAUL.
5. Estado en `PENDING-DECISIONS-REGISTRY.md` pasa a `PENDING` con deadline estimado en meses.

### Incoming (Regulator → Raul)

1. Cuando llega notificación del regulator (típicamente email a Owner o notificación en web del organismo), Owner deposita aquí `<regulator>_<fecha>_<decision-id>.md` con resumen + adjunto si aplica.
2. **InboxBot detecta** filename con patrón `<regulator>_*_<decision-id>*` → actualiza `PENDING-DECISIONS-REGISTRY.md` row a `RESPONDED` y dispara reentry al agente solicitante.
3. Agente solicitante reanuda cadena con la decisión integrada.

## Histórico

### Activas (sembrar manualmente)

| Decision-ID | Pieza | Regulator(es) | Estado | Fecha submission |
|---|---|---|---|---|
| DEC-2026-05-08-001 (sub-track SAPI) | Marcas anglicismos junta — registro IP | SAPI-VE | PENDING (no submitted aún — pendiente decisión Owner sobre presupuesto IP) | TBD |
| DEC-2026-05-03-001 | COVENIN 3445 verification (Argumento 8) | SENCAMER + FONDONORMA + LEGAL-EXT | PENDING | TBD |

### Cerradas

| Decision-ID | Outcome | Fecha cierre |
|---|---|---|
| (vacío al inicio) | | |

## Política de retención

- Responses + submissions viven aquí **180 días** post-cierre (más largo que otros canales por tracking de plazos regulatorios).
- Tras 180 días → mover a `05-archive/04-decisions-history/<año>/<decision-id>/` con metadata explícita de regulator + número de expediente externo si aplica.
- `_outgoing/` se limpia **60 días** después de respuesta recibida (más largo que otros canales — útil para apelaciones).

## Anti-patterns

- ❌ NUNCA hacer submission a regulator sin clearance previo de legal externo (`LEGAL-EXT`) y Bruna (`BR-2`).
- ❌ NO depositar aquí material informal sobre regulators (ej. opinión sobre cómo está SAPI procesando casos en general → `02-knowledge-base/` como nota de mercado).
- ❌ NO confundir SENCAMER (certifica) con FONDONORMA (elabora normas) — direccionar correctamente desde el origen.

## Referencias

- [`PENDING-DECISIONS-REGISTRY.md`](../../04-system/03-governance/PENDING-DECISIONS-REGISTRY.md) — SSoT de estados.
- [`DECISION-MAKERS.md`](../../04-system/03-governance/DECISION-MAKERS.md) — filas SAPI-VE, SENCAMER, FONDONORMA.
- [`RISK-POLICY.md`](../../04-system/03-governance/RISK-POLICY.md) — política de Bruna sobre claims regulatorios.
- `GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md` sección D, A.1, A.4.
