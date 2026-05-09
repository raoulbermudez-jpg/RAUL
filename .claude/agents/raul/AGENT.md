# Raul — Runtime adapter for Claude Code

Carga la SSOT vendor-neutral antes de operar:
`C:\RAUL\04-system\02-agents\conceptual\raul.md`

Toda la identidad, misión, protocolo de ejecución, formato de outputs,
criterios de calidad, antipatterns y reglas duras viven en el conceptual.
Este archivo solo aporta el wiring específico de Claude Code.

## Implementation notes for Claude Code

### Path mappings (rutas absolutas Windows)

| Referencia conceptual | Path absoluto runtime |
|---|---|
| `04-system/01-config/CLAUDE_core.md` | `C:\RAUL\04-system\01-config\CLAUDE_core.md` |
| `04-system/01-config/CLAUDE_genteca.md` | `C:\RAUL\04-system\01-config\CLAUDE_genteca.md` |
| `04-system/01-config/CONTEXT_genteca.md` | `C:\RAUL\04-system\01-config\CONTEXT_genteca.md` |
| `04-system/01-config/OWNER_PROFILE.md` | `C:\RAUL\04-system\01-config\OWNER_PROFILE.md` |
| `04-system/02-agents/_roster.md` | `C:\RAUL\04-system\02-agents\_roster.md` |
| `04-system/02-agents/content-supply-chain/ROUTING-GUIDE.md` | `C:\RAUL\04-system\02-agents\content-supply-chain\ROUTING-GUIDE.md` |
| `04-system/03-governance/RISK-POLICY.md` | `C:\RAUL\04-system\03-governance\RISK-POLICY.md` |
| `02-knowledge-base/00-raul-intelligence/_index.md` | `C:\RAUL\02-knowledge-base\00-raul-intelligence\_index.md` |
| `task-log.md` | `C:\RAUL\04-system\03-governance\task-log.md` |

### Tool mappings

| Capability conceptual | Tool Claude Code |
|---|---|
| Delegación a especialista | `Agent` (con `subagent_type: <name>`) |
| Lectura de archivos del repo | `Read` |
| Escritura del task-log y de aprendizajes | `Write`, `Edit` |
| Búsqueda de patrones en archivos del repo | `Grep` |

### Runtime-specific notes

- **Invocación como skill, no como subagente.** Raul no lleva frontmatter
  (`name:` / `model:` / `tools:`). En sesión directa, el Owner llama a
  Raul por intención (no por nombre explícito). Vía InboxBot, la
  invocación se hace con un briefing estructurado — ver
  `.claude/agents/inboxbot/AGENT.md`.
- **Subagente delegation contract.** Cuando Raul delega vía `Agent`, debe
  pasar un brief autocontenido: tarea + contexto de dominio + instrucción
  explícita de devolver el resultado como texto (Raul maneja la escritura
  de archivos finales, no los especialistas).
- **Contexto core auto-cargado.** El archivo `CLAUDE.md` en raíz del repo
  se auto-carga al inicio de cada sesión Claude Code; ese archivo es la
  puerta de entrada a `CLAUDE_core.md` y al resto.
- Para asignar `model:` cuando se invoca a un subagente, consultar
  `04-system/01-config/LLM-GUIDELINES.md` §4.
