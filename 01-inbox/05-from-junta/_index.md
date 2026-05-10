---
document_id: "INBOX-05-FROM-JUNTA-INDEX"
document_type: "inbox-channel-index"
folder: "01-inbox/05-from-junta/"
purpose: "Canal de comunicación con la Junta Directiva Genteca (decisor JUNTA-GENT). Almacena packages enviados a junta (en _outgoing/) y respuestas formales recibidas. Vista lite del kanban filtrada a JUNTA-GENT; SSoT de estados en PENDING-DECISIONS-REGISTRY.md."
ssot_for: []
depends_on: ["04-system/03-governance/PENDING-DECISIONS-REGISTRY.md", "04-system/03-governance/DECISION-MAKERS.md"]
last_updated: "2026-05-09"
---

# 05-from-junta/ — Canal Junta Directiva Genteca

## Decisor asociado

`JUNTA-GENT` — ver [`DECISION-MAKERS.md`](../../04-system/03-governance/DECISION-MAKERS.md) para scope, SLA típico (2-4 semanas, cadencia reuniones mensuales) y patrón de escalación.

## Estructura

```
05-from-junta/
├── _index.md                              ← este archivo
├── _outgoing/                             ← packages enviados a junta
│   └── <decision-id>_<descripcion>.md
└── <fecha>_<decision-id>_response.md      ← respuestas formales recibidas
```

## Cómo se usa

### Outgoing (Raul → Junta)

1. Agente solicitante (típicamente Aurelio para campañas, Bruna para claims sensibles) genera `package.md` en `04-decisions-in-flight/<project>/<decision-id>/`.
2. Copia el package a `_outgoing/<decision-id>_<descripcion>.md` formateado para presentación física en reunión (usar `junta-decision-package-template.md` cuando esté disponible — pendiente Phase 3 step 4).
3. Owner lleva el deck/package a la reunión de junta.
4. Estado en `PENDING-DECISIONS-REGISTRY.md` pasa a `PENDING` (esperando reunión) o `IN-DELIBERATION` (reunión convocada con fecha).

### Incoming (Junta → Raul)

1. Tras la reunión, Owner (o secretario de junta) deposita aquí `<fecha>_<decision-id>_response.md` con el outcome formal (ej. `2026-05-04_DEC-2026-05-04-001_response.md`).
2. **InboxBot detecta** filename con patrón `_<decision-id>_response.md` → actualiza `PENDING-DECISIONS-REGISTRY.md` row correspondiente a `RESPONDED` y dispara reentry al agente solicitante.
3. Agente solicitante reanuda cadena con la decisión integrada.

## Histórico de decisiones a través de este canal

### Activas (sembrar manualmente)

| Decision-ID | Pieza | Estado | Fecha enviado | Fecha esperada respuesta |
|---|---|---|---|---|
| DEC-2026-05-08-001 | Marcas anglicismos junta (deck top-7) | PARTIALLY-RESPONDED | 2026-05-08 | TBD próxima reunión |

### Cerradas

| Decision-ID | Pieza | Outcome | Fecha cierre |
|---|---|---|---|
| DEC-2026-05-04-001 | GSM-MB-RB-RF-RE empaque (3 variantes) | Línea 2 (con NTC) elegida en convergence con I&D | 2026-05-09 (aprox) |

## Política de retención

- Responses viven aquí **90 días** post-cierre.
- Tras 90 días → mover a `05-archive/04-decisions-history/<año>/`.
- `_outgoing/` se limpia **30 días** después de respuesta recibida (el original sigue en `04-decisions-in-flight/<project>/<decision-id>/package.md`).

## Anti-patterns

- ❌ NO depositar aquí material que NO sea respuesta formal de junta (ej. opiniones individuales de un miembro fuera de reunión → `01-owner-to-raul/` o `07-from-third-parties/`).
- ❌ NO modificar responses una vez registradas (son acta histórica).
- ❌ NO usar este canal para decisiones tácticas que I&D o comercial pueden resolver (eso va por canales `IND-GENT` / `COMERCIAL-GENT` cuando se activen — hoy email/whatsapp vía Owner).

## Referencias

- [`PENDING-DECISIONS-REGISTRY.md`](../../04-system/03-governance/PENDING-DECISIONS-REGISTRY.md) — SSoT de estados.
- [`DECISION-MAKERS.md`](../../04-system/03-governance/DECISION-MAKERS.md) — fila JUNTA-GENT.
- `GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md` sección D, A.1, A.4.
