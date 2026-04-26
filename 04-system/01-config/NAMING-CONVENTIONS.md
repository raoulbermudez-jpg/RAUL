# NAMING-CONVENTIONS.md
## Estándares de nombres para carpetas y archivos — Sistema Raul 2026

**Versión:** 1.0
**Última actualización:** 2026-04-25

Este documento define las convenciones de nombres del sistema. Los patrones aquí registrados están en uso activo; los pendientes de definición están marcados explícitamente en §3.

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

### 2.8 Specs de producto (KB)

- Formato: `YYYY-MM-DD_<tipo-doc>_<slug-producto>.md`
- Tipo de documento: `hoja-especificaciones`, `catalogo`, `guia-programacion`, `manual`, `ficha-tecnica`.
- Slug producto: nombre de marca + código + descripción breve, todo minúsculas y guiones.
- Ejemplos:
  - `2026-04-17_hoja-especificaciones_exceline-gsm-asbs-protector-aa-consola.md`
  - `2026-04-17_catalogo_exceline-profesional-breakers.md`
  - `2026-04-17_guia-programacion_exceline-gtc-b1c-programador-horario.md`

### 2.9 Assets

- Dentro del dominio correspondiente, subcarpetas por tipo: `products/`, `packaging/`, `diagrams/`, `uncoded/`.
- Nombres de archivos visuales: incluir código de producto cuando aplique (ej. `GSM-MB-RB-RF_frontal.png`, `GST-R_etiqueta_v2.pdf`).

### 2.10 Índices

- `_index.md` para índices generales de carpeta (siempre comienza con underscore para distinguirlos de artículos).
- `_index-<tipo>.md` para índices especializados (ej. `_index-specs.md`).

### 2.11 Archivos de governance y log

- Log de tareas: `task-log.md` — tabla plana con columnas Fecha / Agente / Tarea / Outcome.
- Log de decisiones: `DECISIONS.md` — entradas cronológicas con formato definido en el propio archivo.

### 2.12 Versiones dentro de proyectos

- Sufijo `_v<N>` para versiones iterativas de un mismo entregable (ej. `GSM-RF_empaque_delta_v3.md`).
- No usar fechas como versionado de archivos dentro de proyectos (la fecha va en el log o README, no en el nombre del archivo).

---

## 3. Por definir (pendientes)

- Longitud máxima recomendada de slugs de proyecto.
- Patrón para archivos temporales o borradores dentro de proyectos (¿prefijo `_draft_`? ¿subcarpeta `drafts/`?).
- Convención de capitalización para siglas en slugs de proyectos (GST-R vs gst-r en folder names).
- Política de nombres en `03-cross-cutting/` cuando un tema crece más allá de un solo artículo (subdirectorio vs. múltiples artículos planos).

Cada uno de estos puntos se resolverá caso a caso y se registrará en `DECISIONS.md` cuando surja el primer precedente.

---

## Notas de versión

- **v1.0 — 2026-04-25** — stub elevado a versión completa con todos los patrones activos documentados.
