# CONTEXT_core.md
## Contexto general del sistema Raul (PKA · LLM Wiki · Local-first)

Este sistema es el entorno de trabajo de Raoul Bermúdez. Está diseñado como un **Personal Knowledge Assistant (PKA)** con principios **local-first**, **vendor-neutral** y estilo **LLM Wiki**.

Estructura raíz (`C:\RAUL\`):

- `01-inbox/` — Entrada y salida operativa.
  - `01-owner-to-raul/`: briefs, pedidos, prompts y archivos enviados por el Owner (incluyendo desde móvil/Drive/email).
  - `02-deliverables-to-owner/`: entregables de Raul hacia el Owner (informes, presentaciones, piezas finales o borradores).
  - `03-raw-sources/`: material crudo (papers, manuales, transcripciones, capturas) pendiente de procesar.
- `02-knowledge-base/` — LLM Wiki compilada.
  - `01-foundations/`: metodología, filosofía local-first, patrones de uso de LLM.
  - `02-domains/`: conocimiento organizado por dominio:
    - `01-genteca/`
    - `02-finca-ganaderia/`
    - `03-plenus-metabolica/` (Raoul’s Products, alimentos funcionales, salud metabólica, longevidad saludable)
    - `04-teca-teak4food/`
    - `05-marca-personal-raoul/`
    - `99-other-domains/`
    - cada dominio puede tener `wiki/` (artículos) + `specs/` (fichas técnicas) + `assets/` propios.
  - `03-cross-cutting/`: temas transversales (AI systems, marketing técnico, microbiota, etc.).
  - `04-sops-and-playbooks/`: SOPs generales reutilizables.
  - `05-glossary-and-tables/`: glosarios, tablas de referencia.
- `03-projects/` — Trabajo operativo por dominio y proyecto.
  - Carpetas por dominio (`genteca/`, `plenus-metabolica/`, etc.).
  - Dentro de cada proyecto: etapas `00-brief/` → `04-published-and-hand-off/` + `README.md`.
- `04-system/` — Reglas, agentes y gobierno del sistema.
  - `01-config/`: `CLAUDE_core.md`, este `CONTEXT_core.md`, FOLDER-ARCHITECTURE, NAMING-CONVENTIONS, etc.
  - `02-agents/`: definiciones conceptuales de agentes y configuración específica de `.claude/`.
  - `03-governance/`: DECISIONS, MIGRATION-PLAN, políticas.
  - `04-tools-and-scripts/`: scripts y plantillas.
  - `05-indexes/`: índices de proyectos, KB y research.
- `05-archive/` — Histórico y snapshots (no se edita en el día a día).

Principios clave:

- **LLM Wiki**: el objetivo no es solo buscar en PDFs, sino compilar conocimiento en `.md` estructurados dentro de `02-knowledge-base/`. El material de `01-inbox/03-raw-sources/` se destila a artículos y SOPs que persisten.
- **App-less**: el sistema de archivos es la “base de datos”. No se depende de herramientas tipo Notion/Obsidian como verdad principal.
- **Contexto por dominio**: para tareas específicas de un dominio, se puede complementar este contexto core con archivos `CLAUDE_<dominio>.md` / `CONTEXT_<dominio>.md` y con los `.md` relevantes de la wiki de ese dominio.
- **Economía de tokens**: usar este contexto core como base, y añadir solo el contexto de dominio y documentos estrictamente necesarios para cada tarea.

### Archivos core vs companion (PERPLEXITY)

Dentro de `/RAUL/`, algunos archivos terminan en `PERPLEXITY`. Ese sufijo indica que:

- son documentos companion (contexto de sesiones, memoria operativa, guías de diseño),
- viven dentro del repo para mantener continuidad y versionado,
- pero no son Single Source of Truth automático del sistema.

Los archivos core del sistema incluyen, entre otros:

- la configuración y reglas en `04-system/01-config/` (CLAUDE-CODE-RULES, CLAUDE.md, CONTEXT.md, CONTEXT_core.md, FOLDER-ARCHITECTURE, NAMING-CONVENTIONS),
- los índices operativos en `04-system/05-indexes/` (domains-index.md, projects-index.md),
- y los `_index.md` de cada dominio que el Owner haya revisado y aprobado explícitamente.

Los companion docs están indexados en:

- `04-system/05-indexes/companion-docs-index.md`

Cualquier regla o procedimiento que nazca en un archivo `PERPLEXITY` debe considerarse idea candidata, no norma, hasta que el Owner la integre explícitamente en un archivo core.

Rol esperado de los agentes:

- Usar `01-inbox/` como interfaz de entrada/salida.
- Consultar `02-knowledge-base/` para conocimiento estable.
- Trabajar en `03-projects/` para tareas concretas.
- Respetar las reglas y convenciones definidas en `04-system/`.
- Proponer compilaciones y mejoras a la wiki cuando encuentren conocimiento nuevo o fragmentado.
