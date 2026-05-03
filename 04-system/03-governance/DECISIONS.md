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

## 2026-05-01 — Auditoría de agnosticidad: limpieza de vestigios y consolidación de Drive

**Decisión:** ejecutar 8 acciones de saneamiento para reforzar la promesa "local-first, vendor-neutral, multi-LLM, agnóstico a APIs externas".

**Acciones ejecutadas:**

1. **Google Drive como nube canónica.** Resuelto conflicto OneDrive vs. Google Drive. Google Drive (`G:\Mi unidad\RAUL\`) es el único canal remoto del repo (mirror + Owner ↔ colaboradores ↔ InboxBot). OneDrive queda fuera del ámbito de Raul (uso personal del Owner). FOLDER-ARCHITECTURE §10.3, MIGRATION-PLAN §4 y `.claude/agents/inboxbot/AGENT.md` actualizados. KB en OneDrive: pendiente de implementación si el Owner decide backup secundario.
2. **Tarea pendiente OneDrive eliminada** (`Estrategia Integral de Comunicación Targets Exceline Profesional.txt`).
3. **Vestigios eliminados de Google Drive:** `Mi unidad\WorkspaceIA\` (15.6 MB) y `Mi unidad\WorkspaceIA Backup\` (255 MB). Total 270 MB liberados.
4. **Copias globales de agentes eliminadas.** Michelina, Paxs y Vivienne dejan de existir en `C:\Users\User\.claude\agents\`. Quedan únicamente en `C:\Raul\.claude\agents\` (runtime) y `04-system/02-agents/conceptual/` (SSOT). Refuerza la regla "RAUL es autocontenido". Si en el futuro se requiere usarlos desde otro proyecto fuera de C:\Raul, se copian entonces — no antes.
5. **`michelina.md` conceptual saneado.** Removidas referencias específicas a Claude Code y al campo `model:`. La instrucción de generar derivados runtime delega ahora a `LLM-GUIDELINES.md` para mantener la SSOT 100% libre de runtime.
6. **InboxBot clarificado como agente Claude (no Python).** Runtime activo = `.claude/agents/inboxbot/AGENT.md` + Remote Trigger cada 4h. El script `inboxbot.py` legacy NO se porta. MIGRATION-PLAN §4 actualizado.
7. **`04-system/06-companion-docs/` creado.** 4 archivos PERPLEXITY consolidados allí: `CONTEXT_session-2026-04-22`, `KB-SYSTEM-GUIDE`, `core-sources-index`, `session-log_2026-04-22`. `companion-docs-index.md` actualizado con las nuevas rutas.
8. **`CONTEXT.md` legacy banner verificado** (ya existente desde 2026-04-25, sin acción adicional necesaria).

**Implicaciones:**

- El árbol `04-system/` gana una sexta carpeta numerada: `06-companion-docs/`. La promoción a 7+ requeriría revisar `FOLDER-ARCHITECTURE.md` §5.
- Los 3 agentes globales históricamente accesibles desde cualquier proyecto Claude pierden esa propiedad. Decisión consciente: el repo /RAUL/ es la única fuente. Si el Owner necesita Vivienne en otro proyecto, copia desde el repo.
- Cualquier referencia futura al modelo Claude o a Claude Code en `04-system/02-agents/conceptual/` debe extraerse a `LLM-GUIDELINES.md`.
- Pendiente menor: validar que ningún otro conceptual (verificado solo `michelina.md` y `inboxbot.md`) tenga fugas runtime.

**Estado:** completo. Próxima sesión: el Owner traerá sugerencias adicionales para análisis y reestructuración.

---

## 2026-05-01 — Lock de taxonomía nominal de agentes (6 clases canónicas)

**Decisión:** adoptar una taxonomía nominal de 6 clases para clasificar
todos los agentes del sistema /RAUL/, reemplazando la nomenclatura previa
de capas (`Capa 1`, `Capa 2`, `Capa 2a`, `Capa 2b`, `Capa 3`).

Las 6 clases canónicas son:

- `orchestration`
- `governance`
- `global-service`
- `domain-specialist`
- `content-supply-chain`
- `execution-utility`

Convención de nomenclatura: nombres en minúsculas, separadas por guion (no
espacio), para consistencia en tablas, frontmatter, footers de conceptual
y operaciones de grep.

**Contexto y motivación:**

- La nomenclatura "Capa 1 / 2a / 2b / 3" funciona estructuralmente pero es
  opaca para un humano que clona el repo desde GitHub: requiere lectura
  cruzada de varios documentos para entender qué hace cada capa.
- La promesa "vendor-neutral, multi-LLM, fácil de operar también con
  Gemini/Perplexity" exige que la clasificación sea autodescriptiva.
- La transición a Modelo A (conceptual SSOT grueso + runtime delgado)
  requiere que cada conceptual indique en su footer la clase del agente; un
  nombre nominal es más legible que una etiqueta de capa.
- La clase `content-supply-chain` se nombra explícitamente así (no
  `content-pipeline`) para alinearse con la arquitectura existente
  documentada en
  `04-system/02-agents/content-supply-chain/ARCHITECTURE_Content-Supply-Chain.md`.

**Alternativas consideradas:**

- **Mantener nomenclatura de capas** (`Capa 1` / `2a` / `2b` / `3`).
  Rechazado: opaca para clonadores externos del repo, no
  autodescriptiva, no escalable a múltiples runtimes.
- **5 clases sin `content-supply-chain` separada** (CSC distribuida entre
  `governance` para Bruna y `global-service` para los demás). Rechazado:
  rompe la lectura del pipeline coreografiado de CSC y diluye la
  diferencia entre servicios on-demand (Paxs, Vivienne) y pasos de
  pipeline (Aurelio, Nerea, etc.).
- **7+ clases con sub-clases dentro de CSC** (estrategia / producción /
  distribución / memoria como clases separadas). Rechazado: complejidad
  innecesaria; CSC ya define internamente esas posiciones en
  `ARCHITECTURE_Content-Supply-Chain.md`.

**Implicaciones:**

- Se materializa `04-system/02-agents/_taxonomy.md` con la definición
  formal de cada clase, criterios de membresía y reglas de gestión
  (creación, eliminación y movimiento de agentes entre clases).
- `_roster.md` se mueve de `conceptual/_roster.md` a
  `02-agents/_roster.md` y se reescribe usando las 6 clases nominales.
- Cada conceptual de agente lleva en su footer la clase nominal según esta
  taxonomía (ej. `*orchestration. Singleton.*`).
- Bruna mantiene **doble pertenencia documentada** a `governance` (rol
  funcional) y `content-supply-chain` (posición en pipeline). Es la única
  doble-pertenencia permitida bajo esta taxonomía.
- Documentos a actualizar como parte del Paso 8 de la migración Modelo A:
  `CLAUDE.md`, `FOLDER-ARCHITECTURE.md`,
  `04-system/02-agents/content-supply-chain/ROUTING-GUIDE.md`,
  `04-system/02-agents/content-supply-chain/AGENTS_Content-Supply-Chain.md`.
- Cualquier futura clase requiere entrada nueva en este DECISIONS.md
  según las reglas de gestión de `_taxonomy.md`.

**Mapeo de la nomenclatura previa a la nueva:**

| Capa previa | Clase nominal |
|---|---|
| Capa 1 — Orquestación | `orchestration` |
| Capa 2 / 2a — Servicios Globales | `global-service` (Paxs, Vivienne) o `governance` (Michelina) según función |
| Capa 2b — Content Supply Chain | `content-supply-chain` |
| Capa 3 — Especialistas de Dominio | `domain-specialist` |
| (sin clase explícita) — Bruna | `governance` (+ `content-supply-chain` por posición) |
| (sin clase explícita) — InboxBot | `execution-utility` |

**Estado:** vigente desde 2026-05-01. Habilita el Paso 1 de la migración
Modelo A en `04-system/02-agents/`.

---

(próximas entradas debajo, en orden cronológico)
