# 04-system/

Cerebro del sistema Raul. Define cómo se trabaja, no el trabajo en sí.

## Subcarpetas

- `01-config/` — Archivos maestros: CLAUDE.md, CONTEXT.md, FOLDER-ARCHITECTURE, NAMING-CONVENTIONS, LLM-GUIDELINES, CLAUDE-CODE-RULES + archivos de contexto core y por dominio (futuro).
- `02-agents/`
  - `conceptual/` — **Fuente de verdad (SSOT)** de cada agente, vendor-neutral.
  - `content-supply-chain/` — ARCHITECTURE, AGENTS, ROUTING-GUIDE, RUNBOOK.
- `03-governance/` — DECISIONS.md, MIGRATION-PLAN.md, task-log.md, políticas.
- `04-tools-and-scripts/` — Scripts reutilizables y plantillas.
- `05-indexes/` — Índices ligeros (proyectos activos, KB por dominio, research abiertos).

## Regla de agentes

`02-agents/conceptual/*.md` es SSOT. `/RAUL/.claude/agents/<nombre>/AGENT.md` es derivado con frontmatter específico de Claude Code. Editar siempre conceptual primero.
