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

## 2026-05-07 — F6 (Mirror Coach + Persona Delegation) conscientemente diferida hasta F5 estable

**Decisión:** No iniciar F6 en este ciclo. Diferida formalmente hasta que F5 (Madurez operativa) lleve al menos 3 meses estable, según pre-requisito declarado en `02-knowledge-base/00-raul-intelligence/methodology/Hoja_De_Ruta_Raul.md` §F6 (línea 421).

**Contexto y motivación:**

- En sesión 2026-05-07 el Owner preguntó por el agente coach personal y agente clon que recordaba haber diseñado.
- Excavación arqueológica del repo + drives confirmó: el blueprint metodológico existe (Hoja de Ruta v0.3 + research Paxs en `_private/research/2026-05-04_paxs_ai-coach-cloning.md`), pero el agente Espejo nunca fue construido.
- Estado real de fases predecesoras al 2026-05-07:
  - F0/F1/F2: completas.
  - F3 multi-dominio: en curso (Genteca activo, Panamá iniciado, Plenus/Finca/Teca pendientes).
  - F4 validación + métricas: NO iniciada (sin KPIs por dominio, sin golden outputs, sin rúbricas formales).
  - F5 madurez operativa: parcial (Sira/Celeste/Ivo/Bruna BR-5 operan ad-hoc, sin auditoría trimestral ni cadencia formal validada como estable).
- 6 brechas explícitas no resueltas en el blueprint del Espejo (R3-R8 + AC2-AC3 del research Paxs) bloquean construirlo correctamente aunque la fase estuviera lista.
- Prioridad real del Owner es Genteca/GME/GST/Panamá. Adelantar F6 sin F4/F5 maduras: costo > beneficio.

**Alternativas consideradas:**

- **Construir agente Espejo ahora con blueprint parcial.** Rechazado: las 6 brechas explícitas en el research Paxs producirían un agente con boundaries equivocados; además F5 sin estabilidad de 3 meses no provee la señal mínima para que el coach tenga insumo real.
- **Cerrar las brechas R3-R8 a v0.4 sin construir agente.** Diferido: trabajo metodológico valioso pero no urgente; se reactiva cuando F5 esté cerca de estable.

**Implicaciones:**

- F6 NO se inicia hasta dos gates simultáneos: F5 estable 3+ meses + F4 con métricas mínimas operativas.
- El research de Paxs (2026-05-04) queda preservado en `_private/` como insumo activable; cuando se reactive F6, partir de R3-R8 + AC2-AC3 antes de diseñar conceptual del agente Espejo.
- Acción complementaria autorizada en esta sesión: construir `02-knowledge-base/00-raul-intelligence/PKA_LEGACY_MAP.md` para indexar contenido /RAUL/ disperso en C:/G:/D:/OneDrive/Google Drive y no volver a perder rastros del trabajo legacy.

**Estado:** Vigente desde 2026-05-07. Próxima revisión: cuando F5 acumule 3 meses de operación estable o cuando el Owner solicite reactivación explícita.

---

## 2026-05-07 — OPEN QUESTION (pendiente): ¿Librarian por dominio o transversal cuando se activen Plenus/Finca/Teca/marca-personal/Panamá?

**Estado:** Abierta. NO es una decisión tomada — es una pregunta arquitectónica registrada para revisión cuando se active el segundo dominio del sistema (probablemente Plenus, dado que `Presentación final Raoul - QTorta.pptx` y `Plenus.pptx` ya fueron rescatados a `03-projects/plenus/` el 2026-05-07).

**Contexto y motivación:**

- El Owner recordó haber diseñado un flujo `01-inbox/03-raw-sources/` → procesamiento → archivo en KB con curación impecable. La memoria es real: ese flujo existe y lo opera **Celeste**.
- Pero el conceptual de Celeste declara explícitamente: "Si en el futuro se activan KBs de Plenus, Finca, Teca o marca-personal, esos dominios tendrán sus propios librarians (no se reusa este rol — cada dominio tiene su propio set, según política de `domain-specialist`)."
- La Hoja de Ruta v0.3 da por sentado este patrón implícitamente al describir Fase 3 ("activar dominios + identificar gap de domain-specialists"), pero NO valida explícitamente que la curación deba ser domain-specific en lugar de global-service.
- Con 5 dominios futuros (Plenus, Finca, Teca, marca-personal, Panamá) → 5 Celestes con conceptuales casi idénticos podría ser overhead innecesario si la lógica de curación (clasificar Technical vs Market, convertir a Markdown limpio, archivar con naming canónico) es esencialmente la misma entre dominios.

**Las dos opciones (a evaluar cuando llegue el momento):**

- **(A) Patrón actual — un librarian por dominio.** Cada dominio tiene su Celeste-equivalente. Boundaries claras, taxonomía y vocabulario domain-specific embebidos en el agente. Costo: 5 agentes con conceptuales muy parecidos, 5 hire rounds Tier 0 a ejecutar.
- **(B) Promover a `global-service` transversal — un solo librarian para todos los dominios.** Más simple de mantener; rompe la regla de domain-specialist; requiere que el agente conozca taxonomías de todos los dominios o que reciba `domain` como parámetro de contexto. Costo: arquitectura más acoplada al multi-dominio, pero menos overhead de mantenimiento.

**Trigger de revisión:** cuando el Owner solicite activación formal del **segundo dominio** (más allá de Genteca). En ese momento, antes de que Michelina diseñe el librarian del nuevo dominio, decidir si:
- se contrata uno nuevo siguiendo (A), o
- se promueve Celeste (o un sucesor renombrado) a transversal siguiendo (B).

**Por qué no decidir ahora:**

- Solo hay un dominio activo (Genteca). No hay aún señal suficiente sobre cuánto difiere realmente la lógica de curación entre dominios — taxonomías de Plenus (metabólica/yogurt) y Finca (ganadería) podrían ser tan distintas que (A) sea imprescindible, o tan similares que (B) sea claramente superior. Decidir ahora es prematuro.

**Implicaciones de no decidir antes del trigger:**

- Si el Owner no reabre esta pregunta antes de activar Plenus, **por defecto Michelina diseñará un librarian Plenus nuevo siguiendo (A)**. No es problema — solo cierra la opción (B) sin debate consciente. Esta entrada existe precisamente para que la pregunta no se pierda.

**Acción adicional registrada:** auditar `G:\Mi unidad\WorkspaceIA\RAG_SOURCES\` (10 files, encontrado en excavación 2026-05-07) cuando se rescate contenido legacy de Plenus/Finca/Teca, por si contiene reglas o material útil del flujo raw→KB anterior.

---

## 2026-05-07 — Integración de atlas legacy 2026-03 a KB Genteca + GST-RD/GST-RG pendientes de aclarar con engineering

**Decisión:** integrar selectivamente el set de atlas y RAG generados con Opus 4.6 en marzo 2026 (rescatados desde Drive y OneDrive en sesión 2026-05-07) a la KB activa de Genteca, según veredicto de auditoría técnica de Vera. Ejecutado en modo autónomo autorizado por el Owner.

**Contexto:**

- 9 archivos legacy fueron rescatados a `01-inbox/03-raw-sources/genteca/legacy-atlas-2026-03/` (8 atlas/RAG + 1 instrumental NotebookLM descartado).
- Vera realizó auditoría técnica completa el 2026-05-07: ningún hallazgo crítico de contradicción técnica con trabajo reciente (GME, GST, GSM); 6 riesgos identificados, principalmente claims comparativos en Atlas 4 que requieren gate Bruna.
- Owner autorizó ejecución completa del plan de Vera en modo autónomo.

**Resultado de la integración:**

| Archivo legacy | Acción ejecutada |
|---|---|
| Atlas 1 — Motores Trifásicos | INTEGRADO → `wiki/tech/motores-trifasicos-fundamentos.md` |
| Atlas 2 — Protecciones Eléctricas | INTEGRADO → `wiki/tech/protecciones-electricas-motores.md` |
| Atlas 3 — Aplicaciones | INTEGRADO (tablas + patrones) → `wiki/tech/aplicaciones-bombeo-refrigeracion.md` |
| Atlas 4 — Mercado Venezuela | PARCIAL: archivado en `legacy-atlas/`; argumentos físicos puros extraídos a `wiki/tech/argumentos-venta-tecnicos-INTERNO-PENDIENTE-GATE.md` (uso interno solamente, pendiente gate Bruna) |
| Atlas 5 — Exceline Profesional | ARCHIVADO en `legacy-atlas/` (specs ya cubiertas en `specs/` activos) |
| Atlas 6 — Genius | ARCHIVADO en `legacy-atlas/` (specs ya cubiertas en `specs/` activos) |
| RAG Integrador v2 | INTEGRADO (Protocolo + Q&A) → `wiki/tech/protocolo-seleccion-producto-genteca.md` |
| URLs Bibliography | INTEGRADO → `wiki/references/referencias-bibliograficas-motores-trifasicos.md` |
| URLs CopyPaste NotebookLM | DESCARTADO (instrumental obsoleto, contenido duplicado en Bibliography) |

**Decisión D3 — GST-RD y GST-RG pendientes de aclarar con engineering:**

Los productos GST-RD (supervisor con LCD e histórico) y GST-RG (curva inversa tiempo-voltaje) figuraban en marzo 2026 como "en desarrollo próximo". Al 2026-05-07 no hay evidencia en la KB activa ni en proyectos de avance en el desarrollo. Decisión conservadora aplicada en modo autónomo: en los wikis integrados, las referencias a estos productos se neutralizaron como "estado de disponibilidad NO confirmado" y se marcaron como "pendiente aclaración con engineering antes de mencionarlos a clientes".

**Acción pendiente del Owner:** decidir si agregar 2 preguntas sobre estado real de GST-RD/RG al lote de 15 preguntas engineering GME ya en vuelo con Kike, o abrir hilo separado, o esperar evidencia natural.

**Decisión D2 — argumentos de venta:**

El Atlas 4 contenía SALES_ARGs comparativos contra Schneider y genéricos chinos que entran en zona Precedente #3 de Bruna (gate GME). Decisión aplicada:
- Argumentos basados en física verificable → extraídos a doc interno `argumentos-venta-tecnicos-INTERNO-PENDIENTE-GATE.md`
- Argumentos comparativos contra terceros + datos placeholder ("Y% probabilidad falla", "30% del Schneider" sin fuente) → quedan archivados solo en `legacy-atlas/`, NO se extrajeron al wiki
- Bruna delegada para BR-1 sobre los argumentos extraídos antes de cualquier uso externo

**Implicaciones:**

- `wiki/tech/` y `wiki/references/` son carpetas nuevas en la KB de Genteca (no existían antes 2026-05-07).
- `legacy-atlas/` es nueva carpeta hermana de `wiki/`, `specs/`, `assets/` — archivo histórico de consulta, no fuente activa de claims.
- `argumentos-venta-tecnicos-INTERNO-PENDIENTE-GATE.md` está en KB pero marcado prominentemente como NO publicable hasta gate Bruna.
- Los 8 archivos legacy rescatados (excepto el descartado) viven en `legacy-atlas/` para auditoría futura — no editar.

**Estado:** completo en lo operativo. Pendiente del Owner: D3 (canal con engineering) + revisar BR-1 de Bruna cuando esté disponible + autorizar uso externo de argumentos técnicos extraídos cuando Bruna gate.

---

(próximas entradas debajo, en orden cronológico)
