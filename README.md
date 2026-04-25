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

## Cómo usar RAUL con LLMs

1. Antes de tocar nada, leer:
   - `04-system/01-config/CLAUDE.md` (reglas maestras, tono, límites).
   - `04-system/01-config/CONTEXT_core.md` (mapa general de dominios y del árbol RAUL).
   - `04-system/01-config/FOLDER-ARCHITECTURE.md` (detalle de carpetas y roles).
   - `04-system/03-governance/DECISIONS.md` (decisiones estructurales ya tomadas).

2. Para tareas por dominio:
   - Ir a `02-knowledge-base/02-domains/<dominio>/index.md` para entender alcance, marcas y tipos de proyecto.
   - Navegar luego a `03-projects/<dominio>/` para ver proyectos activos, su estado y contexto operativo.

3. Para entender el routing y los agentes:
   - Revisar `04-system/02-agents/content-supply-chain/ARCHITECTURE_Content-Supply-Chain.md`.
   - Revisar `04-system/02-agents/content-supply-chain/AGENTS_Content-Supply-Chain.md`.

## Convenciones clave del sistema

- **Core vs companion**:
  - Archivos con sufijo `PERPLEXITY` son documentos *companion*: contexto, diseño, método o memoria operativa.
  - No son SSOT por defecto. Las reglas y arquitectura final viven en:
    - `04-system/01-config/*` (CLAUDE, CONTEXT_core, FOLDER-ARCHITECTURE, NAMING-CONVENTIONS, etc.).
    - `04-system/05-indexes/*` (domains-index, projects-index, research-index).
    - Los `index.md` de cada dominio en `02-knowledge-base/02-domains/`.

- **Task-log canónico**:
  - El log operativo de delegaciones y resultados vive en
    - `04-system/03-governance/task-log.md`
  - Cualquier log anterior (en repos previos) se considera histórico y está congelado.

- **.gitignore y datos fuera de Git**:
  - No se versionan:
    - `01-inbox/01-owner-to-raul/`, `01-inbox/02-deliverables-to-owner/`, `01-inbox/03-raw-sources/`.
    - `05-archive/` completo.
    - Binarios pesados (`.pdf`, `.pptx`, `.docx`, imágenes, vídeo, audio, etc.) salvo excepciones en `02-knowledge-base/**/specs/`.
  - RAUL en GitHub contiene el “cerebro” del sistema (Markdown, scripts, configuración), no los buzones ni el archivo histórico.

- **Numeración de dominios**:
  - `02-knowledge-base/02-domains/` sigue esta numeración oficial:
    - `01-genteca`
    - `02-plenus-metabolica`
    - `03-finca-ganaderia`
    - `04-teca-teak4food`
    - `05-marca-personal-raoul`
    - `99-other-domains`
  - La numeración refleja prioridad de activación y orden operativo, no necesariamente el orden histórico.
