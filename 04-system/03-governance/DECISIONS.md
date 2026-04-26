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

## 2026-04-25 — Política agentes globales vs. locales

**Decisión:** Los agentes Michelina, Paxs y Vivienne se mantienen en **ambas ubicaciones** (global `C:\Users\User\.claude\agents\` y local `C:\Raul\.claude\agents\`), con la copia local como **fuente autoritativa** y los archivos conceptuales en `04-system/02-agents/conceptual/` como **SSOT vendor-neutral**.

**Contexto y motivación:**
- Los tres agentes existían solo en global antes de la migración. Se copiaron al repo local para que el sistema /RAUL/ sea autocontenido y versionable.
- La copia global es legado; se mantiene para no romper otros proyectos abiertos desde `C:\Users\User\`.
- La copia local en `/RAUL/.claude/agents/` es la que opera en sesiones abiertas desde `C:\Raul`.

**Regla operativa:**
- Cualquier modificación a Michelina, Paxs o Vivienne se hace primero en `04-system/02-agents/conceptual/<agente>.md` (SSOT), luego se refleja en `C:\Raul\.claude\agents\<agente>\AGENT.md` (derivado local).
- La copia global (`C:\Users\User\.claude\agents\`) **no se actualiza automáticamente** — es responsabilidad del Owner sincronizarla manualmente si usa esos agentes desde otros proyectos.
- Si en el futuro se decide eliminar la copia global, registrar la decisión aquí.

**Estado:** Vigente desde 2026-04-25.

---

## 2026-04-25 — Auditoría completa y cierre de brechas estructurales (Fase 3.5)

**Decisión:** ejecutar una auditoría exhaustiva del sistema /RAUL/ antes de iniciar trabajo operativo, identificar todas las brechas respecto a `FOLDER-ARCHITECTURE.md` v2.1, y cerrarlas en una sesión continua.

**Contexto y motivación:**
- El Owner estableció el principio "no construir grandes proyectos ni KB sin una base sólida". La auditoría garantiza que el skeleton esté completo, los índices operativos pobaldos, la governance documentada y los patrones de contexto implementados.
- Se identificaron y cerraron 16 brechas en 3 tiers de prioridad.

**Brechas cerradas:**
- Tier 1: fix Celeste (rutas y nombre de índice), CLAUDE.md trim (108→108 líneas, `@CONTEXT_core.md`), CONTEXT.md congelado como legacy.
- Tier 2: LLM-GUIDELINES.md, RISK-POLICY.md, SECURITY-AND-ACCESS.md creados.
- Tier 3: skeletons dominios 02-05 + 99, kb-index-by-domain, research-index, templates (project/sop/report), 01-foundations stubs (3), 03-cross-cutting indexes (4), 04-sops _index, 05-glossary-and-tables.
- Fase 3.5 (esta sesión): `02-knowledge-base/_index.md`, cross-cutting assets `_index.md`, Genteca assets subdirs `_index.md`, glossary renombrado a `glossary-tecnico.md`, FOLDER-ARCHITECTURE.md actualizado, `CLAUDE_core.md` creado, `CLAUDE_genteca.md` + `CONTEXT_genteca.md` (piloto Fase 6), NAMING-CONVENTIONS.md elevado a v1.0, scripts de migración archivados.

**Estado:** completo. Pendiente solo Fase 4 (Drive + InboxBot — requiere acción del Owner).

---

## 2026-04-25 — Estructura 03-cross-cutting/ como subdirectorios en lugar de archivos planos

**Decisión:** `03-cross-cutting/` usa subdirectorios por tema (`ai-systems/`, `marketing-tecnico/`, `microbiota/`, `salud-metabolica/`) con `_index.md` en cada uno, en lugar de archivos planos como especificaba el v2.1 original de `FOLDER-ARCHITECTURE.md`.

**Razón:** el patrón de subdirectorios es más escalable (cada área puede crecer con múltiples artículos), consistente con el patrón de dominios, y facilita la carga selectiva de contexto por tema. `FOLDER-ARCHITECTURE.md` fue actualizado para reflejar esto.

**Estado:** vigente desde 2026-04-25.

---

## 2026-04-25 — CLAUDE_core.md como entrada vendor-neutral; CLAUDE.md como Claude Code entry point

**Decisión:** mantener `CLAUDE.md` como el archivo que Claude Code carga automáticamente. `CLAUDE_core.md` es la versión compacta vendor-neutral para uso con otros LLMs (GPT, Gemini, etc.) o como contexto manual ligero. No reemplaza a `CLAUDE.md`; son complementarios.

**Razón:** Claude Code requiere `CLAUDE.md` por convención. `CLAUDE_core.md` cumple el objetivo de la Fase 6 (eficiencia de tokens con otros LLMs) sin romper el flujo actual de Claude Code.

**Estado:** vigente desde 2026-04-25.

---

(próximas entradas debajo, en orden cronológico)
