# DECISIONS.md
## Log de decisiones arquitectónicas y de proceso — Sistema Raul 2026

Este documento registra decisiones que afectan la estructura, el proceso o las políticas del sistema Raul. Se consulta y se actualiza cada vez que una decisión impacta `FOLDER-ARCHITECTURE.md`, agentes, routing, inboxes o políticas de uso de LLM.

**Formato de cada entrada:**

- Fecha (ISO)
- Decisión (una línea)
- Contexto y motivación
- Alternativas consideradas
- Implicaciones
- Estado

---

## 2026-04-21 — Adopción de arquitectura Raul 2026 v2.1 y migración a `/RAUL/`

**Decisión:** adoptar la arquitectura definida en `FOLDER-ARCHITECTURE.md` v2.1 como estructura base del sistema Raul, y ejecutar la migración descrita en `MIGRATION-PLAN.md` v1.0 desde el estado previo (repo `C:\WorkspaceIA\PROJECTS\Claude code\` + workspace hermano `C:\WorkspaceIA\PROJECTS\<dominio>\`) a `C:\RAUL\`.

**Contexto y motivación:**

- El estado previo tenía governance mezclada con scripts y checkpoints; trabajo operativo por dominio sin separación por campaña ni estados formales (WIP/Review/Approved plano); backups junto a archivos vivos; y dependencias implícitas a convenciones de rutas de Claude Code.
- Se requería un sistema con principios explícitos: **local-first**, **vendor-neutral**, **multi-LLM**, con soporte amplio para múltiples dominios (Genteca, Finca, Plenus, Teca, marca personal) y tipos de trabajo (content supply chain, investigación, consultoría, sandbox).
- La arquitectura incorpora una estrategia de **contexto por capas (core + dominio)** para minimizar consumo de tokens.

**Alternativas consideradas:**

- **Refactor mínimo del estado previo** (solo `Team/governance/` + `Team/content-system/` + `Team/history/`). Rechazado: no resolvía la ingesta direccional, la memoria cross-dominio ni el contexto por capas.
- **Adopción parcial** (solo `governance/`, dejando el resto). Rechazado: la mezcla con workspace operativo hermano seguía generando fricción y no eliminaba los paths duros a `Team/*`.

**Implicaciones:**

- 4 fases de migración (1–4) + post-cleanup (5) + piloto de contexto core + dominio (6, futura y opcional).
- Ventana de inestabilidad operativa remota durante fase 4 (24–48h) al reconfigurar Drive mirror e InboxBot.
- `02-agents/conceptual/*.md` pasa a ser **SSOT** vendor-neutral de agentes; `/RAUL/.claude/agents/<nombre>/AGENT.md` queda como **derivado** con frontmatter específico de Claude Code.
- Assets son **por dominio** (`02-domains/<dominio>/assets/`); solo lo realmente transversal vive en `03-cross-cutting/assets/`.
- `CLAUDE.md` y `CONTEXT.md` se mantienen separados; en el futuro se complementan con `CLAUDE_core.md` / `CONTEXT_core.md` compactos + pares por dominio (`CLAUDE_<dominio>.md` / `CONTEXT_<dominio>.md`).

**Estado:** Fase 1 en ejecución. Skeleton `C:\RAUL\` creado; `FOLDER-ARCHITECTURE.md` v2.1, `MIGRATION-PLAN.md` v1.0, `CONTEXT_core.md`, stubs README, `NAMING-CONVENTIONS.md` stub, `.gitignore`, `DECISIONS.md` (este archivo) y primer commit creados como parte de Fase 1.

## 2026-04-24 — Numeración oficial de dominios en 02-knowledge-base/02-domains

Se fija la numeración oficial actual de dominios de la siguiente forma:

- `01-genteca`
- `02-plenus-metabolica`
- `03-finca-ganaderia`
- `04-teca-teak4food`
- `05-marca-personal-raoul`
- `99-other-domains`

Criterio:
- La numeración refleja prioridad de activación y orden operativo del sistema, no necesariamente el orden histórico en que los dominios fueron concebidos.
- A partir de esta decisión, la documentación estructural y los índices del sistema deben alinearse con esta numeración.

Notas:
- `02-plenus-metabolica` queda formalizado como nombre y posición oficiales.
- Cualquier referencia previa a `03-plenus-metabolica` en documentación estructural debe considerarse obsoleta y actualizarse.

---

(próximas entradas debajo, en orden cronológico)
