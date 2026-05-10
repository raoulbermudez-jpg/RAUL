# 01-inbox/

Entrada y salida operativa del sistema. Separado por dirección y propósito.

## Subcarpetas

### Canales originales (Owner ↔ Raul + insumos)

- `01-owner-to-raul/` — Owner → Raul. Briefs, pedidos, prompts y archivos que el Owner deposita (Drive, móvil, email). InboxBot lee aquí y crea tareas.
- `02-deliverables-to-owner/` — Raul → Owner. Entregables finales o borradores para revisión.
- `03-raw-sources/` — Insumos crudos (PDFs, transcripciones, capturas, artículos web) pendientes de compilar a `02-knowledge-base/` o a un proyecto en `03-projects/`.

### Canales de governance (Phase 3 — desde 2026-05-09)

- `04-decisions-in-flight/` — Workspace por decisión: cada package Pause+Resume vive aquí (`<project-id>/<decision-id>/context.md + package.md + options.md + recommendation.md + response.md`). SSoT del estado en `04-system/03-governance/PENDING-DECISIONS-REGISTRY.md`.
- `05-from-junta/` — Canal Junta Directiva Genteca. `_outgoing/` para packages enviados, raíz para responses formales recibidas. Decisor: `JUNTA-GENT`.
- `06-from-regulators/` — Canal organismos regulatorios (SAPI-VE, SENCAMER, FONDONORMA). `_outgoing/` para submissions, raíz para notificaciones recibidas. Decisores: `SAPI-VE`, `SENCAMER`, `FONDONORMA`.
- `07-from-third-parties/` — Canal contrapartes externas (Panama contractors, legal externo, otros). Subcarpeta por party (`<party-name>/_outgoing/` y raíz para correspondencia). Decisores: `PANAMA-CONTRA`, `LEGAL-EXT`, etc.
- `08-special-deliverables/` — Overflow: crisis-drafts, one-offs, materiales de transición que no encajan en los otros canales.

## Reglas

1. **Nada de `01-inbox/` es "verdad estable".** Lo valioso se compila a KB o a proyecto y luego se mueve o descarta.
2. **Cada canal tiene `_index.md`** con su política específica (estructura, lifecycle, retención, anti-patterns). Consultar antes de depositar archivos.
3. **Decisiones in-flight cruzan canales:** el package vive en `04-decisions-in-flight/`, una copia adaptada va a `05-from-*/_outgoing/` o `06-from-*/_outgoing/` o `07-from-*/<party>/_outgoing/` según el decisor. Estado canónico en `PENDING-DECISIONS-REGISTRY.md`.
4. **InboxBot detecta responses** por filename pattern (decision-id en el nombre) en canales 05/06/07 y dispara reentry al agente solicitante.

## Referencias

- [`04-system/03-governance/DECISION-MAKERS.md`](../04-system/03-governance/DECISION-MAKERS.md) — quién decide qué, IDs de decisor, canal preferido.
- [`04-system/03-governance/PENDING-DECISIONS-REGISTRY.md`](../04-system/03-governance/PENDING-DECISIONS-REGISTRY.md) — kanban de decisiones in-flight.
- [`04-system/03-governance/GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md`](../04-system/03-governance/GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md) — arquitectura completa (sección D para folder structure).
