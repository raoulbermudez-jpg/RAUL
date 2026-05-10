---
document_id: "INBOX-04-DECISIONS-IN-FLIGHT-INDEX"
document_type: "inbox-channel-index"
folder: "01-inbox/04-decisions-in-flight/"
purpose: "Workspace de packages de decisión activos: cada decisión que activa Pause+Resume tiene su carpeta aquí con context / package / options / recommendation / response. Vista scoped por proyecto; el SSoT del estado vive en PENDING-DECISIONS-REGISTRY.md."
ssot_for: []
depends_on: ["04-system/03-governance/PENDING-DECISIONS-REGISTRY.md", "04-system/03-governance/DECISION-MAKERS.md"]
last_updated: "2026-05-09"
---

# 04-decisions-in-flight/ — Workspace de packages de decisión

## Propósito

Carpeta donde **vive el material físico** de cada decisión in-flight. La fuente de verdad sobre el **estado** de cada decisión es [`PENDING-DECISIONS-REGISTRY.md`](../../04-system/03-governance/PENDING-DECISIONS-REGISTRY.md); aquí están los archivos que componen el package.

## Estructura por decisión

### Decisiones nuevas (prospectivas — convención completa)

```
<project-id>/
└── <decision-id>/
    ├── context.md          ← qué proyecto / qué pieza está bloqueada
    ├── package.md          ← request al decisor
    ├── options.md          ← alternativas con trade-offs
    ├── recommendation.md   ← lo que el agente solicitante recomienda
    └── response.md         ← (vacío hasta que llega respuesta)
```

### Decisiones migradas retroactivamente (convención mínima)

Decisiones que ya estaban in-flight antes del 2026-05-09 (Phase 3 step 3) se migran con **solo `context.md`**, que apunta a las rutas reales donde vive el material original (project folder, governance log, memoria, etc.). Los archivos `package.md` / `options.md` / `recommendation.md` / `response.md` NO se fabrican retroactivamente.

```
<project-id>/
└── <decision-id>/
    └── context.md          ← incluye frontmatter con migration_type: "retroactive" + rutas al material original
```

Cuando llegue response a una decisión migrada, se crea `response.md` directamente (sin reconstruir el package).

## Cómo se usa

1. **Agente solicitante** (Bruna / Aurelio / Vael / etc.) crea `<project-id>/<decision-id>/` y los 4 archivos iniciales (context, package, options, recommendation).
2. **Si el decisor es interno (OWNER)**: agente además copia `package.md` a `01-inbox/02-deliverables-to-owner/` para que Owner lo vea en su flujo normal.
3. **Si el decisor es externo (JUNTA-GENT, SAPI-VE, etc.)**: agente copia `package.md` al `_outgoing/` del canal correspondiente (`05-from-junta/_outgoing/`, `06-from-regulators/_outgoing/`, etc.).
4. **Cuando llega respuesta**: InboxBot la deposita en el canal correspondiente; agente solicitante (o Owner manualmente) la copia a `response.md` aquí, actualiza `PENDING-DECISIONS-REGISTRY.md` a `RESPONDED`, y reanuda la cadena.

## Items activos

| Decision-ID | Project | Estado | Decisor(es) | Path |
|---|---|---|---|---|
| DEC-2026-05-06-001 | GME protector monofásico | PENDING | OWNER + IND-GENT | [`gme/DEC-2026-05-06-001/`](gme/DEC-2026-05-06-001/context.md) |
| DEC-2026-05-06-002 | GME claim "primero LATAM" | SUSPENDED-UPSTREAM | OWNER | [`gme/DEC-2026-05-06-002/`](gme/DEC-2026-05-06-002/context.md) |
| DEC-2026-05-08-001 | Marcas anglicismos junta | PARTIALLY-RESPONDED | JUNTA-GENT + SAPI-VE | [`marcas-anglicismos-junta/DEC-2026-05-08-001/`](marcas-anglicismos-junta/DEC-2026-05-08-001/context.md) |
| DEC-2026-05-03-001 | COVENIN 3445 (Argumento 8) | PENDING | SENCAMER + FONDONORMA + LEGAL-EXT | [`covenin-3445/DEC-2026-05-03-001/`](covenin-3445/DEC-2026-05-03-001/context.md) |
| DEC-2026-05-08-D1-D5 | GST Labels (umbrella) | PENDING | OWNER | [`gst-r-etiquetas/DEC-2026-05-08-D1-D5/`](gst-r-etiquetas/DEC-2026-05-08-D1-D5/context.md) |

Las 5 fueron migradas retroactivamente el 2026-05-09 (Phase 3 step 3, colateral 2) como decisión hybrid: solo decisiones in-flight reciben workspace; las cerradas (DEC-2026-05-04-001 RESPONDED, DEC-2026-04-29-001 CLOSED-WITHDRAWN) quedan referenciadas solo en registry.

## Items cerrados (RESPONDED / EXPIRED / CLOSED-*)

| Decision-ID | Estado final | Fecha cierre | Notas |
|---|---|---|---|
| (vacío al inicio) | | | |

## Política de retención

- Decisiones cerradas viven aquí **90 días** después del cierre.
- Tras 90 días → mover a `05-archive/04-decisions-history/<año>/<decision-id>/`.
- `_outgoing/` de canales asociados se limpia 30 días tras respuesta recibida.

## Referencias

- [`PENDING-DECISIONS-REGISTRY.md`](../../04-system/03-governance/PENDING-DECISIONS-REGISTRY.md) — SSoT de estados.
- [`DECISION-MAKERS.md`](../../04-system/03-governance/DECISION-MAKERS.md) — IDs de decisores y canales.
- `GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md` sección D y A.1 — patrón Pause+Resume.
