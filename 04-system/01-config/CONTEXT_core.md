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
    - - `01-genteca/`
    - `02-plenus-metabolica/` (Raoul’s Products, alimentos funcionales, salud metabólica, longevidad saludable)
    - `03-finca-ganaderia/`
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
- **Economía de tokens**: usar este contexto core como base, y añadir solo el contexto de dominio y documentos estrictamente necesarios para cada tarea. La memoria persistente del sistema opera en **2 tiers** (desde 2026-05-12): **`MEMORY.md`** (HOT, auto-load por conversación, entradas tocadas <6 meses o marcadas `always_load: true`) y **`MEMORY_ARCHIVE.md`** (COLD, on-demand, leer explícitamente solo cuando una tarea actual requiera contexto histórico). Política de archivado mensual mueve entradas HOT inactivas → ARCHIVE. Memorias llevan frontmatter `last_touched: YYYY-MM-DD` que se actualiza al recordar/referenciar.
- **Mapa operativo explícito**: para orientarse rápido, usar los índices en `04-system/05-indexes/`:
  - `domains-index.md` para ver dominios activos y su estado.
  - `projects-index.md` para ver proyectos activos y su etapa.
  - `research-index.md` para líneas de investigación abiertas.
- **Gobernanza y migración**: los cambios estructurales y de infraestructura (migración a C:\RAUL, Fase 4 Drive + InboxBot, etc.) se registran en:
  - `04-system/03-governance/DECISIONS.md`
  - `04-system/03-governance/MIGRATION-PLAN.md`
  - `04-system/03-governance/task-log.md`

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

---

### Configuración de paths para scripts (`RAUL_ROOT`)

Los scripts Tier 1 (`fase4_kb_formatter.py`, `pendrive_pipeline.py`, `backup_kb_to_onedrive.ps1`) resuelven sus paths via la variable de entorno `RAUL_ROOT`, con fallback a `C:\RAUL` si no está seteada.

**Resolución (orden de precedencia):**
1. Argumento explícito (`get_paths(root="...")`, para tests).
2. Variable de entorno `RAUL_ROOT`.
3. Default hardcoded `C:\RAUL`.

**Configuración recomendada:**
- **Producción Windows:** setear permanentemente vía `setx` o System Properties (ver paso a paso abajo).
- **Sesión puntual:** `$env:RAUL_ROOT = "C:\RAUL"` antes de invocar scripts (válido solo en esa shell).
- **Sin setup:** scripts usan el default `C:\RAUL`. Máquinas existentes no requieren cambios.

**Cómo setear `RAUL_ROOT` permanentemente (Windows) — paso a paso:**

Opción 1 — PowerShell:

```powershell
# Abrir PowerShell como administrador (para system-wide) o normal (para user-only)
setx RAUL_ROOT "C:\RAUL" /M     # /M = system-wide (requiere admin); sin /M = user-only

# IMPORTANTE: setx no afecta la sesión activa. Cerrar y abrir nueva PowerShell.
# Verificar en la nueva sesión:
$env:RAUL_ROOT                  # debe imprimir: C:\RAUL
```

Opción 2 — GUI Windows:

1. Win + X → System → Advanced system settings → Environment Variables.
2. New (en System variables si querés system-wide, o User variables para tu usuario): Name = `RAUL_ROOT`, Value = `C:\RAUL`.
3. OK → reiniciar PowerShell, CMD, VS Code, y cualquier otro IDE/terminal abierto para que recarguen el entorno.

**Verificación end-to-end (post-setup):**

```powershell
# 1. Confirmar que la variable está visible en una nueva PowerShell
$env:RAUL_ROOT

# 2. Self-test del helper Python
python "C:\RAUL\04-system\04-tools-and-scripts\raul_paths.py"
# Debe mostrar: ROOT = C:\RAUL  [OK]
# Si la variable está mal seteada, ROOT mostraría el valor seteado (no el default).
```

**Cuándo conviene setearlo:**
- Si querés usar un root distinto al default `C:\RAUL` (ej. clonar el repo en otra ubicación para test).
- Si tenés varios checkouts del repo y querés cambiar entre ellos via env var.
- Para CI/CD o setups portables.

Si solo trabajás con un único `C:\RAUL`, no necesitás setear la variable — el default funciona.

**Helper Python:** scripts importan `from raul_paths import paths`. El helper vive en `04-system/04-tools-and-scripts/raul_paths.py` y provee paths canónicos (`ROOT`, `INBOX`, `KB`, `PROJECTS`, `SYSTEM`, `INDEXES_DIR` apuntando a `05-indexes/`, `LOGS_DIR` apuntando a `06-logs/`, `PENDRIVE`, `ENV_FILE`).

**PowerShell:** scripts usan `$env:RAUL_ROOT` con fallback inline.

Detalles operativos: `04-system/01-config/SCRIPTS-DEPENDENCIES.md`.
