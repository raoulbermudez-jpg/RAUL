# Guía práctica — Construcción de un sistema /RAUL/-like (KB + Wiki + Projects)

Esta guía resume el proceso que se usó para construir /RAUL/ (Genteca + Plenus) y sirve como blueprint para repetir el patrón en otros dominios o enseñar cómo hacerlo.

## 1. Filosofía del sistema

- Un solo **core** (`/RAUL/`) con:
  - Arquitectura explícita (FOLDER-ARCHITECTURE).
  - Contexto central (CONTEXT_core).
  - Plan de migración (MIGRATION-PLAN).
  - Registro de decisiones (DECISIONS).
  - Registro de tareas/hitos (Team/task-log).

- Cada **dominio** tiene:
  - Su subcarpeta en `02-knowledge-base/02-domains/XX-nombre-dominio/`.
  - Una wiki LLM (artículos, patrones, lecciones).
  - Una specs area (si aplica).
  - Una carpeta de assets visuales.

- Los **proyectos** viven en `03-projects/<dominio>/<año-mes_slug>/` con estructura estándar `00-brief` → `04-published-and-hand-off`.

- El **Owner** mantiene disciplina de fases:
  - No avanzar de Fase N a N+1 sin punto de control y decisión explícita.
  - No tocar índices “plantilla v1” sin orden.

## 2. Fases de construcción

### Fase 1 — Skeleton

- Crear estructura mínima `/RAUL/`:
  - `01-inbox/` (owner-to-raul, team-to-raul, raw-sources).
  - `02-knowledge-base/` (core, domains, cross-cutting, sops).
  - `03-projects/`.
  - `04-system/` (config, agents, tools, indexes).
  - `05-archive/`.
- Escribir:
  - `CONTEXT_core.md`.
  - `FOLDER-ARCHITECTURE.md` (v1).
  - `MIGRATION-PLAN.md`.
  - `DECISIONS.md` (stub).
  - `.gitignore` (binarios, temp, etc.).

### Fase 2 — System + agentes

- Migrar:
  - Reglas del sistema (CLAUDE-CODE-RULES, CONTEXT, etc.) a `04-system/01-config/`.
  - Agentes locales a `.claude/agents/` + fichas conceptuales a `04-system/02-agents/conceptual/`.
  - Rutas de documentación (RUNBOOK, ARCHITECTURE) a `04-system/` según `FOLDER-ARCHITECTURE.md`.
- Confirmar:
  - `git status` limpio.
  - Ejecuciones de subagentes funcionan en el nuevo repo.
  - Fase 2 cerrada en `Team/task-log.md`.

### Fase 3 — KB por dominio + proyectos

Para cada dominio:

1. **Definir estructura de dominio** (`02-domains/XX-dominio/`):

   - `_index.md` (dominio):
     - Alcance.
     - Marcas implicadas (si aplica).
     - Audiencias.
     - Estructura de carpetas (wiki/specs/assets).
     - Tipos de proyectos típicos.
     - Equipo humano relevante.
     - Agentes anclados al dominio.
     - Proyectos activos (link a `projects-index`).
     - Integraciones externas (ej. NotebookLM) como “puertas abiertas”.

   - `wiki/_index.md`:
     - Estado (stub vs poblado).
     - Subcarpetas (market, clinical, fundamentals, etc.).
     - Lista de artículos futuros (mínimo 5–7).
     - “Qué va aquí” / “Qué NO va aquí”.
     - Producción/consumo (qué agentes producen, quién consume).

   - `wiki/market/_index.md` (si aplica):
     - Alcance (clientes, competidores, manuales de marca, pricing).
     - “Alcance inicial de competidores” (no exhaustivo; Owner define foco).
     - Taxonomía de tipos de competidor (adaptada al dominio).
     - Productor/consumidor.
     - Índice de documentos (aunque comience con `_pendiente_`).

   - `specs/_index-specs.md`:
     - Qué es una ficha de producto en ese dominio.
     - Qué incluye: composición, claims, etiquetas, certificaciones, etc.
     - Convención de nombres.
     - Qué NO va en specs (separar de wiki y de proyectos).

   - `assets/_index.md`:
     - Estructura: products, packaging, diagrams/infographics, uncoded.
     - Convención de nombres.
     - Qué NO va aquí.

2. **Migrar materiales desde el repo viejo** (si los hay):

   - KB (docs técnicos, datasheets, etc.) → `specs/` y `wiki/`.
   - Assets → `assets/`.
   - Proyectos activos → `03-projects/<dominio>/...` con estructura 00–04.

3. **Crear READMEs de proyectos**:

   - `README.md` en cada proyecto:
     - Título del proyecto.
     - Dominio, período, estado (00–04).
     - Objetivo.
     - Stakeholders (tabla).
     - Organización por carpetas (tabla).
     - Pendientes inmediatos.
     - Enlaces a KB.
     - Decisiones clave.

4. **Disciplina de commits**:

   - Commit de migración por dominio:
     - `Fase 3 — KB <dominio> + assets + proyectos activos migrados`.
   - Commit de ajustes finos de índices (Owner):
     - `Owner edits — plantilla <dominio> v1`.

### Fase 4 — Limpieza y ecosistema externo

- Archivar/marcar repos viejos (sin borrar hasta tener backups).
- Integrar:
  - Google Drive / Dropbox como repositorio de binarios.
  - Inbox bots (email → 01-inbox/).
  - Conectores de KB externos (ej. NotebookLM) mediante procesos definidos (no copiado ciego).

## 3. Reutilización como curso

Para dar un curso:

- Usar este documento como backbone de syllabus.
- Cargar ejemplos reales:
  - Índices de Genteca y Plenus.
  - READMEs de proyectos Genteca.
- Ejercicio guiado:
  - Los asistentes definen un nuevo dominio (ej. “Marca personal”, “Unidad de negocio nueva”).
  - Siguen Fase 3 para ese dominio:
    - Diseñar `_index.md`, `wiki/_index.md`, `wiki/market/_index.md`, etc.
  - Revisan y hacen commits disciplinados.