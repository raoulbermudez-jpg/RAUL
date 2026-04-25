# NAMING-CONVENTIONS.md
## Estándares de nombres para carpetas y archivos — Sistema Raul 2026

**Versión:** 0.1 (stub inicial)
**Estado:** por desarrollar durante operación real

Este documento definirá las convenciones de nombres del sistema. Como stub inicial, se listan los principios acordados y los patrones ya en uso. El detalle fino se completará a medida que aparezcan casos reales y se tomen decisiones registradas en `DECISIONS.md`.

---

## 1. Principios generales

- **Sin espacios** en nombres de carpeta (facilita scripting, CLI, git).
- **Minúsculas** por defecto, excepto archivos fundacionales del sistema y acrónimos.
- Separadores:
  - `-` (guion) para legibilidad dentro del slug.
  - `_` (underscore) para separar fecha/slug/versión.
- **Sin acentos** en nombres de carpeta y slug; sí permitidos dentro del contenido Markdown.
## Excepciones de naming

Regla general:
- Los nombres de carpetas no llevan espacios.
- Los nombres de archivos operativos del sistema tampoco deben llevar espacios por defecto.

Excepción explícita:
- Los archivos companion con sufijo `PERPLEXITY` pueden llevar un espacio antes del sufijo para mejorar legibilidad humana.

Ejemplos válidos:
- `CONTEXT_session-2026-04-22 PERPLEXITY.md`
- `KB-SYSTEM-GUIDE PERPLEXITY.md`
- `core-sources-index PERPLEXITY.md`

Aclaraciones:
- Esta excepción aplica solo a archivos companion, no a carpetas.
- El sufijo `PERPLEXITY` sirve para indicar origen, distinguir documentos de apoyo y evitar confusión con archivos core del sistema.
- Si un documento deja de ser companion y se promueve a core, debe retirarse el sufijo `PERPLEXITY` y volver a la convención general de naming.

---

## 2. Patrones ya acordados

### 2.1 Carpetas top-level del sistema

- `NN-nombre/` con `NN` de 2 dígitos.
- Ej: `01-inbox/`, `02-knowledge-base/`, `03-projects/`, `04-system/`, `05-archive/`.

### 2.2 Dominios dentro de `02-knowledge-base/02-domains/` y `03-projects/`

- En KB: `NN-nombre-dominio/` (ej. `01-genteca/`, `03-plenus-metabolica/`).
- En projects: nombre plano sin numeración (ej. `genteca/`, `plenus-metabolica/`).

### 2.3 Proyectos

- Formato: `YYYY-MM_slug-descriptivo/`.
- Slug: palabras separadas por guion, minúsculas, sin acentos, sin caracteres especiales.
- Ejemplos: `2026-04_GST-R_etiquetas/`, `2026-05_rotacion-potreros/`, `2026-05_cancer-metabolico-review/`.

### 2.4 Etapas dentro de un proyecto

- `00-brief/` → `04-published-and-hand-off/` (o variantes según tipo de proyecto).
- Numeración fija para que el orden alfabético refleje el flujo de trabajo.

### 2.5 Archivos fundacionales del sistema

- PascalCase o UPPERCASE para los más importantes:
  - `FOLDER-ARCHITECTURE.md`, `MIGRATION-PLAN.md`, `DECISIONS.md`.
  - `CLAUDE.md`, `CONTEXT.md`, `CLAUDE_core.md`, `CONTEXT_core.md`.
  - `NAMING-CONVENTIONS.md`, `LLM-GUIDELINES.md`, `CLAUDE-CODE-RULES.md`.

### 2.6 Artículos de wiki

- Formato: `nn-slug-descriptivo.md` con número de orden de lectura (ej. `01-fundamentos-tecnicos.md`, `02-proteccion-motores.md`).

### 2.7 Agentes

- Conceptual (SSOT): `/RAUL/04-system/02-agents/conceptual/<nombre>.md` — minúsculas.
- Derivado Claude Code: `/RAUL/.claude/agents/<nombre>/AGENT.md` — mismo nombre minúscula + archivo llamado `AGENT.md`.

### 2.8 Assets

- Dentro del dominio correspondiente, subcarpetas por tipo: `products/`, `packaging/`, `diagrams/`, `uncoded/`.
- Nombres de archivos visuales: incluir código de producto cuando aplique (ej. `GSM-MB-RB-RF_frontal.png`, `GST-R_etiqueta_v2.pdf`).

### 2.9 Índices

- `_index.md` para índices generales de carpeta.
- `_index-<tipo>.md` para índices especializados (ej. `_index-specs.md`).

---

## 3. Por definir (pendientes)

- Política exacta sobre acentos dentro de nombres de archivo (hoy: evitarlos).
- Longitud máxima recomendada de slugs de proyecto.
- Convención exacta para versiones dentro de un proyecto (v1, v2, v3 vs fecha vs rev-YYYY-MM-DD).
- Patrón para archivos temporales o borradores (¿prefijo `_draft_`? ¿subcarpeta `drafts/`?).
- Convención de capitalización para siglas en slugs (GST-R vs gst-r).

Cada uno de estos puntos se resolverá caso a caso y se registrará en `DECISIONS.md` cuando surja el primer precedente.

---

Este documento es un stub vivo y se expandirá con la operación real del sistema.
