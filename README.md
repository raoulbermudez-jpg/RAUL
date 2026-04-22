# RAUL — Sistema personal Raoul Bermúdez

Personal Knowledge Assistant (PKA) local-first, vendor-neutral, multi-LLM.

## Estructura raíz

- `01-inbox/` — Entrada y salida operativa (Owner ↔ Raul + raw sources).
- `02-knowledge-base/` — LLM Wiki compilada por dominio (wiki, specs, assets).
- `03-projects/` — Trabajo operativo por dominio y proyecto.
- `04-system/` — Reglas, agentes, routing, configuración.
- `05-archive/` — Histórico y snapshots.

## Puntos de entrada

1. `04-system/01-config/CLAUDE.md` — instrucciones maestras para agentes.
2. `04-system/01-config/CONTEXT_core.md` — contexto general del sistema.
3. `04-system/01-config/FOLDER-ARCHITECTURE.md` — arquitectura detallada de carpetas.
4. `04-system/03-governance/MIGRATION-PLAN.md` — plan de fases de migración.
5. `04-system/03-governance/DECISIONS.md` — log de decisiones arquitectónicas.

Para convenciones de nombres, ver `04-system/01-config/NAMING-CONVENTIONS.md`.
