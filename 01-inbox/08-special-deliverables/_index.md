---
document_id: "INBOX-08-SPECIAL-DELIVERABLES-INDEX"
document_type: "inbox-channel-index"
folder: "01-inbox/08-special-deliverables/"
purpose: "Overflow channel para entregables one-off que no encajan en los flujos canónicos: outputs producidos bajo Crisis override, entregables ad-hoc para terceros sin canal estable, materiales de transición durante migraciones, etc. Vivienda temporal hasta clasificar mejor o archivar."
ssot_for: []
depends_on: ["04-system/03-governance/PENDING-DECISIONS-REGISTRY.md", "04-system/03-governance/GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md"]
last_updated: "2026-05-09"
---

# 08-special-deliverables/ — Overflow channel

## Cuándo usar este canal

Este canal **NO es default**. Usar SOLO cuando ninguno de los canales canónicos aplica:

- ❌ Owner pide algo → `01-owner-to-raul/`
- ❌ Raul entrega a Owner → `02-deliverables-to-owner/`
- ❌ Insumo crudo → `03-raw-sources/`
- ❌ Decisión in-flight → `04-decisions-in-flight/`
- ❌ Comunicación con junta → `05-from-junta/`
- ❌ Comunicación con regulator → `06-from-regulators/`
- ❌ Comunicación con tercero → `07-from-third-parties/`
- ✅ **Si NO encaja en ninguno**: → `08-special-deliverables/`

## Casos típicos

1. **Crisis-DRAFT outputs** producidos bajo el patrón A.3 (Crisis override) — entregables generados sin pasar por gates de calidad estándar, marcados con `status: CRISIS-DRAFT`. Viven aquí hasta post-mortem de Bruna y promoción a APPROVED (en cuyo caso se mueven al canal apropiado).
2. **Entregables one-off para audiencias inesperadas** — ej. material para entrevista de podcast no planificada, contenido para evento al que Owner asiste como invitado de última hora.
3. **Materiales de transición** durante migraciones de sistema — outputs generados durante cambios estructurales que aún no tienen home definitivo.
4. **Outputs experimentales** que el sistema produce pero aún no están claros para clasificar (ej. test de capacidad de un agente nuevo).

## Convención de filename

`<fecha>_<descripcion-corta>_<status>.md` donde `<status>` es uno de: `crisis-draft`, `experimental`, `oneoff`, `transition`.

Ejemplos:
- `2026-05-09_podcast-tech-bull_oneoff.md`
- `2026-05-12_GST-counter-positioning_crisis-draft.md`
- `2026-05-15_test-agent-capability-X_experimental.md`

## Items actuales

| Filename | Tipo | Origen | Próxima acción |
|---|---|---|---|
| (vacío al inicio) | | | |

## Items archivados / promocionados

| Filename original | Outcome | Fecha | Nuevo home |
|---|---|---|---|
| (vacío al inicio) | | | |

## Política de retención

- Special-deliverables viven aquí **60 días** después de producción.
- Tras 60 días, Owner / Sira hacen revisión:
  - Si quedó útil pero no encajó en flujos → archivar a `05-archive/06-special-deliverables/<año>/` con metadata explicando por qué fue special.
  - Si fue crisis-draft promocionado → ya debería haberse movido al canal apropiado; si sigue aquí, indica que el post-mortem de Bruna está pendiente (escalar).
  - Si fue experimental que no llegó a nada → borrar con nota en commit message.
- `crisis-draft` items tienen flag de prioridad: post-mortem de Bruna debería resolverse en **72h** post-crisis (ver patrón A.3).

## Anti-patterns

- ❌ NO usar este canal como "no sé dónde va, lo dejo aquí" sin marcar tipo. Cada item DEBE tener `<status>` en filename.
- ❌ NO dejar crisis-drafts más de 72h sin escalar a Bruna para post-mortem.
- ❌ NO usar este canal para evitar disciplina de los flujos canónicos. Si patrón emerge (ej. múltiples one-offs del mismo tipo), considerar formalizarlo en su propio canal o ajuste a flujos existentes.

## Referencias

- `GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md` sección D y A.3 (Crisis override).
- [`RISK-POLICY.md`](../../04-system/03-governance/RISK-POLICY.md) — política de Bruna sobre crisis-drafts y post-mortem.
- [`PENDING-DECISIONS-REGISTRY.md`](../../04-system/03-governance/PENDING-DECISIONS-REGISTRY.md) — registry para decisiones que emergen de crisis.
