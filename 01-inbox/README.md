# 01-inbox/

Entrada y salida operativa del sistema. Separado por dirección y propósito.

## Subcarpetas

### Canales originales (Owner ↔ Raul + insumos)

- `00-cola/` — **Cola de trabajo.** InboxBot deja aquí un `TICKET_*.md` por cada ítem que captura de los canales remotos; Raul-desktop los consume al inicio de sesión (ritual §6.0 de `raul.md`). Contiene también `_log-ciclos.md` (heartbeat de InboxBot). Vive en el mirror de Drive — InboxBot no alcanza el repo local. Ver `04-system/02-agents/conceptual/inboxbot.md`.
- `01-owner-to-raul/` — Owner → sistema. Briefs, pedidos, archivos que el Owner deposita remotamente (Drive, móvil). El canal vivo es el mirror de Drive; InboxBot lo escanea y **captura** cada ítem como ticket en `00-cola/` (no procesa — captura).
- `02-deliverables-to-owner/` — Raul → Owner. Entregables finales o borradores para revisión, producidos por Raul en sesión desktop.
- `03-raw-sources/` — Insumos crudos (PDFs, transcripciones, capturas, artículos web) pendientes de compilar a `02-knowledge-base/` o a un proyecto en `03-projects/`. Canal desktop/repo — no es parte del modelo remoto.
- `_ESTADO.md` — **Tablero de estado** (en el mirror de Drive). Archivo único que el Owner consulta desde remoto: cola del Owner + actividad de colaboradores + flags de higiene + ítems añejos. Lo regenera InboxBot cada ciclo.

### Canales de governance (Phase 3 — desde 2026-05-09)

> **Estos canales son desktop/repo, NO parte del modelo remoto.** Viven solo en el repo local; no se espejan a Drive. Los maneja Raul en sesión desktop. Si una respuesta de decisión llega remotamente, el Owner la deja en `01-owner-to-raul/` como cualquier ítem; InboxBot la captura como ticket normal y Raul reconoce el decision-id al consumir la cola (ver `raul.md` §6.6).

- `04-decisions-in-flight/` — Workspace por decisión: cada package Pause+Resume vive aquí (`<project-id>/<decision-id>/context.md + package.md + options.md + recommendation.md + response.md`). SSoT del estado en `04-system/03-governance/PENDING-DECISIONS-REGISTRY.md`.
- `05-from-junta/` — Canal Junta Directiva Genteca. `_outgoing/` para packages enviados, raíz para responses formales recibidas. Decisor: `JUNTA-GENT`.
- `06-from-regulators/` — Canal organismos regulatorios (SAPI-VE, SENCAMER, FONDONORMA). `_outgoing/` para submissions, raíz para notificaciones recibidas. Decisores: `SAPI-VE`, `SENCAMER`, `FONDONORMA`.
- `07-from-third-parties/` — Canal contrapartes externas (Panama contractors, legal externo, otros). Subcarpeta por party (`<party-name>/_outgoing/` y raíz para correspondencia). Decisores: `PANAMA-CONTRA`, `LEGAL-EXT`, etc.
- `08-special-deliverables/` — Overflow: crisis-drafts, one-offs, materiales de transición que no encajan en los otros canales.

## Reglas

1. **Nada de `01-inbox/` es "verdad estable".** Lo valioso se compila a KB o a proyecto y luego se mueve o descarta.
2. **Cada canal tiene `_index.md`** con su política específica (estructura, lifecycle, retención, anti-patterns). Consultar antes de depositar archivos.
3. **Decisiones in-flight cruzan canales:** el package vive en `04-decisions-in-flight/`, una copia adaptada va a `05-from-*/_outgoing/` o `06-from-*/_outgoing/` o `07-from-*/<party>/_outgoing/` según el decisor. Estado canónico en `PENDING-DECISIONS-REGISTRY.md`.
4. **El routing de respuestas de decisión lo hace Raul-desktop**, no InboxBot. Desde el rediseño v5.0 de InboxBot (2026-05-14), InboxBot solo captura ítems como tickets; Raul reconoce el decision-id al consumir la cola y enruta a la maquinaria Phase 3 (ver `raul.md` §6.6). InboxBot ya no monitorea los canales 05/06/07 ni dispara reentry.

## Referencias

- [`04-system/03-governance/DECISION-MAKERS.md`](../04-system/03-governance/DECISION-MAKERS.md) — quién decide qué, IDs de decisor, canal preferido.
- [`04-system/03-governance/PENDING-DECISIONS-REGISTRY.md`](../04-system/03-governance/PENDING-DECISIONS-REGISTRY.md) — kanban de decisiones in-flight.
- [`04-system/03-governance/GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md`](../04-system/03-governance/GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md) — arquitectura completa (sección D para folder structure).
