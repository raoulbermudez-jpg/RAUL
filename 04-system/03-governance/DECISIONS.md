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

## 2026-05-08 — Cierre BR-2 sobre argumentos de venta atlas-legacy + canal D3 elegido (esperar evidencia natural)

**Contexto:** complementa la entrada 2026-05-07 sobre integración de atlas legacy. El Owner regresó al sistema y revisó el BR-1 emitido por Bruna sobre los 8 argumentos de venta extraídos del Atlas 4.

**Decisiones del Owner:**

1. **BR-2 emitido:** autorizó los 7 argumentos VERDE+AMARILLO+NARANJA-reformulado para uso externo. Bruna appendeó las 7 entradas al log de claims `2026-05-03_genteca_claim-approval-log_v1.md` (entradas #22-28). Argumento 8 (COVENIN 3445) sigue ROJO — bloqueado hasta verificación SENCAMER/FONDONORMA.

2. **Argumento 7 reformulado:** se eliminó el dato cuantitativo "CORPOELEC ya en 210V en muchas zonas" del Argumento 7 (cable sumergible). Se convirtió en "redes con variabilidad de tensión" como condición genérica. El ejemplo del 91% Vn se mantiene como ilustrativo, no estadístico. Pasa de NARANJA a AMARILLO con caveat. Reformulación aplicada en `wiki/tech/argumentos-venta-tecnicos.md`.

3. **Documento renombrado:** `argumentos-venta-tecnicos-INTERNO-PENDIENTE-GATE.md` → `argumentos-venta-tecnicos.md` (tras BR-2 aprobado). El header del documento refleja el nuevo estado y mantiene el Argumento 8 marcado como bloqueado.

**Decisión D3 — canal para aclarar GST-RD/GST-RG:**

El Owner delegó a Raul la elección del canal. Decisión: **canal C — esperar evidencia natural**. Razones:
- El lote engineering GME (15 preguntas) está en vuelo con Kike + escalación de riesgo de diseño pendiente con el Owner. Sumar 2 preguntas más diluiría el foco GME (lanzamiento octubre 2026, alto stakes).
- Abrir hilo separado con Kike/Keiddys para preguntas no urgentes saturaría el canal de aprobaciones sin valor inmediato — los wikis ya neutralizaron el riesgo (referencias a GST-RD/RG marcadas como "estado disponibilidad NO confirmado").
- Si un proyecto futuro toca GST-RD o GST-RG, naturalmente se preguntará en ese contexto.

**Marcador de seguimiento:** cualquier interacción con Kike/Keiddys donde naturalmente surjan los productos GST-RD/RG es oportunidad de pescar la respuesta. Si en 2 meses sigue sin haber claridad, reabrir D3.

**Acción pendiente del Owner:**
- Argumento 8 (COVENIN 3445): coordinar con Genteca/legal la verificación SENCAMER/FONDONORMA del certificado vigente y alcance por modelo.

**Estado:** D3 cerrado por canal C. BR-2 cerrado para 7/8 argumentos. Argumento 8 queda en lista de pendientes con acción identificada.

---

## 2026-05-08 — Ciclo de auditoría PKA + remediaciones Pasos 1-3c

**Decisión:** ejecutar ciclo de auditoría del PKA propuesto por GitHub Copilot, evaluado por Claude Opus 4.7, con remediaciones priorizadas en 4 pasos. Pasos 1, 2, 3a, 3b y 3c ejecutados. Paso 3d (refactor Tier 1 a variables de entorno) queda pendiente para sesión separada.

**Contexto y motivación:**

- Copilot Chat (VS Code) produjo 3 documentos de auditoría (`PKA-AUDIT-CHECKLIST.md`, `PKA-IMPROVEMENTS-SUMMARY.md`, `PKA-FLOW.md`) e identificó 3 hallazgos críticos: scripts con paths hardcoded, naming violation `GME Estudios de mercado/`, proyectos con estructura incompleta.
- Owner pidió evaluación de Claude Opus 4.7 antes de ejecutar cambios.
- Claude amplió el scope tras auditoría completa: 22 scripts (no 3) con paths hardcoded, 5 riesgos cross-cutting no vistos por Copilot (InboxBot AGENT.md hardcoded, dual hierarchy Drive G:\ vs cueva legacy, Task Scheduler dependiente de paths absolutos, casing inconsistente, ubicación de `.env`).
- Owner eligió Opción 2 (Claude dirige y ejecuta) sobre Opción 1 (brief a Copilot), por mejor preservación de memoria persistente y disciplina Modelo A.

**Pasos ejecutados:**

| Paso | Descripción | Commit |
|---|---|---|
| 1 | Consolidación `PKA-FLOW.md` (versión rica de Copilot a `01-config/`, duplicado en `03-governance/` eliminado) | 9207aaf |
| 2 | Creación `SCRIPTS-DEPENDENCIES.md` como SSOT de inventario y dependencias de scripts | 9207aaf |
| 3a | Archivo de 6 scripts Tier 3 legacy (era pre-/RAUL/) a `05-archive/03-system-history/legacy-scripts/` + redirector | 52d7e9b |
| 3b | Casing canónico `C:\RAUL` en 6 scripts (5 Python + 1 PowerShell). Tier 1 ya tenía casing correcto | 3c3cad1 |
| 3c | Rename `GME Estudios de mercado/` → `2025-04_GME_estudios-mercado/` + 13 archivos con citaciones actualizadas (6 scripts internos + 7 docs/notes) | b41279e |

**Paso pendiente:**

- **3d** — Refactor Tier 1 (`fase4_kb_formatter.py`, `pendrive_pipeline.py`, `backup_kb_to_onedrive.ps1`) a variables de entorno (`RAUL_ROOT`, `RAUL_INDEXES_DIR`, `RAUL_LOGS_DIR`). Prerrequisito para separación `05-indexes/canonical/` ↔ `06-logs/` (recomendación I.2 de Copilot).

**Hallazgos cross-cutting documentados (en `SCRIPTS-DEPENDENCIES.md`):**

1. `.claude/agents/inboxbot/AGENT.md` tiene path hardcoded a `inboxbot-tasklog.md` — manejar con Read+Edit (Write produce loops de permisos).
2. Dual hierarchy en Google Drive (`G:\Mi unidad\RAUL\` canónico vs `C:\Users\User\Mi unidad\RAUL\` cueva legacy descontinuada). Riesgo activo de InboxBot.
3. Task Scheduler `RAUL_KB_Backup_OneDrive` referencia path absoluto del `.ps1`. Mover el script requiere reconfigurar la tarea programada.
4. Casing inconsistente (`C:/RAUL`, `C:\RAUL`, `C:\Raul`). Fix parcial aplicado en Paso 3b (scripts); md files quedan para cleanup futuro.
5. `.env` en root del repo es patrón aceptable (debe seguir en `.gitignore`).

**Alternativas consideradas:**

- **Copilot ejecuta los cambios** (Opción 1 del Owner): rechazado — Copilot no tiene memoria persistente (Modelo A, taxonomía, BR-1/BR-5 vigentes, dual hierarchy). Riesgo de pisar disciplina ya establecida.
- **Mantener ordenación original Copilot** (SSOT-MATRIX como I.1 prioritario): modificado — Claude reordenó por riesgo creciente. Auditoría completa de paths primero, porque scripts hardcoded eran bloqueantes para reorganización.
- **Versionado SemVer agresivo en frontmatter (I.4 Copilot)**: rechazado — alto overhead, baja utilidad. DECISIONS.md ya cumple esa función.
- **Auto-generación de índices + dashboard HTML (III.1, III.3 Copilot)**: rechazado — contradice disciplina vendor-neutral si los scripts se vuelven dependencia operativa.
- **Mover scripts Tier 3 a worktree de pruebas vs `05-archive/`**: rechazado — los archivados no son recuperables, son evidencia histórica. Git log preserva el contenido.

**Documentos generados/consolidados:**

- `04-system/01-config/SCRIPTS-DEPENDENCIES.md` — SSOT de inventario de 22 scripts en 3 tiers, plan de variables canónicas, comando de regresión grep.
- `04-system/01-config/PKA-FLOW.md` — flujo end-to-end del PKA (versión rica de Copilot consolidada).
- `04-system/03-governance/PKA-AUDIT-CHECKLIST.md` — checklist operacional para auditorías futuras (cadencia: mensual o cada 5 proyectos).
- `04-system/03-governance/PKA-IMPROVEMENTS-SUMMARY.md` — análisis de mejoras priorizadas (referencia histórica del proceso, no SSOT activo).
- `04-system/03-governance/CLAUDE-REVIEW-PROMPT.md` — template del prompt usado por Owner para invocar evaluación.
- `05-archive/03-system-history/legacy-scripts/_index.md` — inventario de scripts archivados (gitignored, en disco).
- `04-system/04-tools-and-scripts/scripts/_LEGACY_MOVED.md` — redirector que indica destino de archivado.

**Implicaciones:**

- Toda incorporación futura de scripts debe documentarse en `SCRIPTS-DEPENDENCIES.md`.
- La separación canonical/logs en `05-indexes/` queda en stand-by hasta que se ejecute Paso 3d.
- Owner conoce los riesgos cross-cutting documentados.
- Carpeta `2025-04_GME_estudios-mercado/` queda activa para que Owner agregue estudios adicionales desde su disco duro.

**Follow-ups menores pendientes:**

- Casing `\Raul\` en `_intel/Bruna_gate_GME_*.md` y `_intel/Aurelio_AU-1_*.md` (mixed case en md files, no rompe en Windows pero rompe en case-sensitive systems).
- Posible cleanup posterior si emergen otros stale references al revisar `_intel/` y `_governance/` con más detalle.

**Estado:** Pasos 1-3c cerrados (commits 9207aaf, 52d7e9b, 3c3cad1, b41279e). Paso 3d en stand-by para sesión limpia.

---

## 2026-05-09 — Cleanup colaboradores (RAUL-Exchange → RAUL/colaboradores) + cueva legacy + status agentes globales

**Decisión:** consolidar el canal Drive de colaboradores externos bajo `RAUL/colaboradores/<dominio>/<nombre>/` (estructura clara y consistente con AGENT.md de InboxBot), limpiar artefactos vestigiales en cueva legacy local, y reflejar en memoria/DECISIONS el estado real de agentes globales.

**Contexto y motivación:**

- Owner reportó confusión sobre múltiples ubicaciones con elementos /RAUL/-related: `C:\RAUL\` (repo), `C:\Users\User\.claude\` (Claude Code internals), `C:\Users\User\Mi unidad\` (cueva legacy Backup & Sync), `G:\Mi unidad\` (Drive Desktop streaming).
- Recon read-only mostró: (1) en Drive existían dos top-level folders `RAUL/` y `RAUL-Exchange/`, semánticamente confusos — el primero para Owner inbox, el segundo para colaboradores; (2) `RAUL-Exchange/Genteca/<colab>/01_De_X_Para_Raoul/` no matcheaba el path que esperaba InboxBot AGENT.md (`RAUL/colaboradores/<colab>/inbox/`) → InboxBot fallaba silenciosamente al escanear colaboradores; (3) cueva legacy local tenía 1 archivo huérfano + un `.claude/settings.local.json` que pertenecía a otra máquina (`raoul.bermudez` user, sincronizado pre-Backup-&-Sync-EOL); (4) `C:\Users\User\.claude\agents\` está VACÍO contradiciendo memoria 2026-04-25 que esperaba Michelina/Paxs/Vivienne ahí.
- El estado pre-cleanup tenía ~9 colaboradores y 1 carpeta especial activos; sistema en modo piloto. Owner explícitamente dijo: "no hay tantos archivos en juego porque apenas estoy usando mi repo raul para trabajar. Podemos decir que prácticamente los trabajos son una prueba para pulir el repo." → riesgo bajo para cleanup disruptivo.

**Decisiones del Owner durante la sesión:**

1. **A (disruptivo es OK):** mover RAUL-Exchange/ → RAUL/colaboradores/ por consistencia con repo bien estructurado.
2. **C (cirugía):** limpiar solo los 2 vestigios RAUL-related en cueva legacy, dejar archivo personal del Owner intacto.
3. **A (memoria stale):** actualizar memoria sobre agentes globales para reflejar realidad (vacío).
4. **SÍ:** entrada formal en DECISIONS.md (esta entrada).
5. **A1:** preservar capa de dominio en colaboradores (`<dominio>/<colab>/`).
6. **B1:** mantener naming español/numeral (`01_De_X_Para_Raoul/`, `02_De_Raoul_Para_X/`, `03_Archivo/`) en lugar de simplificar a inbox/outbox/archive.
7. **C1:** Memoria_Tareas_Pendientes va a `RAUL/colaboradores/Genteca/_memoria-tareas-pendientes/` (prefijo `_` señala "no es colaborador").
8. **P4:** dejar Panama en `RAUL-Exchange/Panama/` por ahora — Panama no es colaboradores (carpetas temáticas Analisis-Mercado/Contratos/EmbassyClub/Finanzas/Reparaciones), su activación al sistema RAUL queda pendiente de definir mejor el caso de uso.

**Acciones ejecutadas:**

1. **Drive moves (G:\):**
   - Creado `G:\Mi unidad\RAUL\colaboradores\Genteca\` y `Academicos\`.
   - Movidas 7 carpetas Genteca: Ana-Mendez, Cora-Urrea, Julio-Heredia, Liliam-Ramirez, Oswaldo, Rhinoska-Celis, Valeria-Ostos.
   - Movido y renombrado `Memoria_Tareas_Pendientes` → `_memoria-tareas-pendientes`.
   - Movido Daniel-Rubio (Academicos).
   - rmdir de `RAUL-Exchange/Genteca/` y `RAUL-Exchange/Academicos/` (vacíos post-move).
   - **Drive IDs:** colaboradores individuales preservados (move atómico mantiene ID); padres `Genteca/`/`Academicos/` viejos eliminados, nuevos creados con nuevos IDs. Permisos compartidos con colaboradores siguen activos vía link directo a su carpeta.

2. **Cueva legacy local:**
   - Eliminado `C:\Users\User\Mi unidad\RAUL\01-inbox\01-owner-to-raul\Prueba 1 del 4 de mayo.txt`.
   - Eliminado `C:\Users\User\Mi unidad\.claude\` (solo contenía `settings.local.json` de otra máquina).

3. **Repo updates (commits en este push):**
   - `.claude/agents/inboxbot/AGENT.md`: Read+Edit (no Write) — nuevo path pattern colaboradores, scan logic con dominio + shortname, archivado por canal (`_archived/` para Owner, `03_Archivo/` para colaboradores).
   - `04-system/02-agents/conceptual/inboxbot.md`: revisado, sin cambios necesarios (path-agnóstico por diseño).
   - `04-system/03-governance/GUIA-CARPETAS-RAUL.md`: estructura colaboradores reescrita en sección 2.3 + tabla raíz + tabla de quick-reference.
   - `04-system/03-governance/OPERATIVA-REMOTA-Y-COLABORADORES.md`: replace_all `RAUL-Exchange` → `RAUL/colaboradores` (todas las refs en este doc apuntaban a colaboradores; Panama no aparecía).
   - `02-knowledge-base/00-raul-intelligence/PKA_LEGACY_MAP.md`: 2 entradas de tabla actualizadas.
   - `03-projects/genteca/2026-04_GST-R_etiquetas/02-production/Oz_propuesta_v1/README.md`: 2 referencias de path actualizadas.
   - `04-system/03-governance/2026-05-05_status-cierre.md`: NO modificado (doc histórico, refs reflejan estado de esa fecha).

4. **Memoria actualizada (`C:\Users\User\.claude\projects\C--RAUL\memory\`):**
   - `feedback_drive_dual_inbox_hierarchy.md`: añadido status update aclarando que el cleanup NO resolvió la dual hierarchy del incidente 2026-05-07 (ese es Drive cloud, requiere Owner action en Drive web).
   - `reference_drive_exchange_ids.md`: añadida sección "Reorganización 2026-05-09" con estructura nueva y nota sobre IDs preservados/cambiados.

**Aclaración importante — qué NO se resolvió:**

El incidente original InboxBot 2026-05-07 fue causado por **dos jerarquías paralelas en Drive cloud** con el mismo nombre `01-inbox/01-owner-to-raul/` bajo parents distintos: canónica `RAUL` (id `124VdcO237NDXAowD0DZ0BoJVMiQNMKPG`) y legacy parent `1Yex3K9hQnPgaVQ1QRSiH8PClP9NJMKrc` (residual de Drive Backup & Sync que sobrevivió a la migración 2026-04). Este cleanup NO tocó esa duplicación — requiere acción Owner desde Drive web para identificar y consolidar/eliminar el legacy parent. El riesgo de duplicación silenciosa en rutinas automáticas persiste hasta entonces.

**Status de agentes globales `C:\Users\User\.claude\agents\`:**

Recon mostró que la carpeta está VACÍA. La entrada 2026-04-25 ("Política agentes globales vs. locales") esperaba Michelina/Paxs/Vivienne ahí. Owner confirmó (decisión 3) que el flujo actual es siempre `C:\RAUL\` → no necesita copia global. La entrada 2026-04-25 queda como historial; la realidad actual es: agentes solo en `C:\RAUL\.claude\agents\` + SSOT en `04-system/02-agents/conceptual/`.

**Alternativas consideradas:**

- **Mover RAUL-Exchange a RAUL/colaboradores conservando naming inglés (inbox/outbox/archive):** rechazado — Owner prefirió B1 español/numeral para que colaboradores vean naming claro en su Drive.
- **Mover Panama a RAUL/colaboradores/Panama/ literal (decisión 1.A literal):** rechazado — Panama no tiene colaboradores, son carpetas temáticas. Forzarlo en colaboradores/ es semánticamente incorrecto.
- **Mover Panama a RAUL/dominios-personal/Panama/ (nueva ubicación):** rechazado — compromete decisión arquitectónica antes de que el caso de uso esté maduro.
- **Eliminar cueva legacy completamente:** rechazado — contiene archivo personal del Owner (helados, finanzas, fotos BlackBerry 2014-2015). Cleanup quirúrgico (decisión C) preserva el archivo personal.
- **Resolver dual hierarchy Drive cloud en esta sesión:** out of scope — requiere Drive web access que no estaba disponible en la sesión filesystem-based.

**Implicaciones:**

- InboxBot debería ahora encontrar correctamente colaboradores en `RAUL/colaboradores/<dominio>/<nombre>/01_De_<shortname>_Para_Raoul/`. Test pendiente Owner cuando arranque rutina remota.
- Memoria de IDs Drive en `reference_drive_exchange_ids.md` para `RAUL-Exchange/Genteca` y `RAUL-Exchange/Academicos` parents está stale; los IDs internos de colaboradores siguen válidos.
- `RAUL-Exchange/` en Drive ahora contiene solo Panama. Cuando Panama active al sistema RAUL, refactor adicional decidirá ubicación canónica.
- Riesgo dual hierarchy 2026-05-07 sigue activo hasta acción Owner Drive web.

**Update final 2026-05-09 (continuación de sesión, post-DECISIONS-write):**

Drive cloud dual hierarchy del incidente 2026-05-07 → ✅ **resuelta** vía Drive web Owner action.

Recon adicional vía Drive MCP confirmó que el legacy parent `1Yex3K9hQnPgaVQ1QRSiH8PClP9NJMKrc` era el folder auto-creado **"Mi PC"** por Google Backup & Sync (descontinuado). Visible en Drive web bajo `Computadoras > Mi PC`. Contenía 5 subfolders:

- `01-owner-to-raul` (con tarea incidente 2026-05-07 + TEST-SYNC inerte)
- `02-deliverables-to-owner` (4 deliverables, todos duplicados verificados del canónico)
- `genteca/2026-04-19/` (1 archivo `GST_Exceline_Presentacion_JD_V3_texto.md`, existe en local)
- `Downloads` (descargas misceláneas pre-RAUL)
- `WorkspaceIA` (workspace pre-/RAUL/; scripts archivados en commit 52d7e9b; resto inerte)

Owner ejecutó vía Drive web: rename defensivo `Mi PC` → `Mi PC - LEGACY DELETE 2026-05-09` → Move to Papelera. Drive index lo invalidó inmediatamente — searches de `01-owner-to-raul` y `02-deliverables-to-owner` devuelven ahora solo el canónico (verificado post-trash vía Drive MCP). Folder físico en Papelera (30 días recuperable; auto-purge si no se vacía manualmente).

**Estado:**
- Decisiones 1-8 + ajustes ejecutadas en sesión 2026-05-09.
- Drive cloud dual hierarchy: ✅ resuelta esta sesión (Owner action vía Drive web + verificado).
- Cueva legacy local: ✅ resuelta (commit edbb547).
- RAUL-Exchange/colaboradores reorganización: ✅ ejecutada (commit edbb547).
- Pendiente menor: (a) validación operacional InboxBot remoto en próximo cron disparo; (b) decisión futura sobre Panama si/cuando active al sistema /RAUL/.

---

## 2026-05-10 — Implementación Phase 3 governance: 6 componentes + 8 sub-decisiones de diseño

**Decisión:** ejecutar incremental los 6 componentes operativos del plan aprobado en `GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md` (sección J — pasos 1-6), formalizando 8 sub-decisiones de diseño que emergieron durante la ejecución y que ajustan o extienden lo propuesto originalmente.

**Contexto y motivación:**

El sistema /RAUL/ tenía documentación del flujo CSC (Capa 2b — Aurelio → Nerea/Solenne → producción → Bruna → Ivo) pero NO tenía formalizada la coordinación con humanos externos al sistema (junta directiva Genteca, regulators SAPI/SENCAMER/FONDONORMA, contrapartes Panama, legal externo). La diagnóstica `GOVERNANCE-DIAGNOSTIC-2026-05-09.md` identificó esta brecha (gates de decisión sin canal estructurado, decisiones in-flight sin tracking, cadenas Pause+Resume sin patrón). El proposal Phase 2 propuso una arquitectura completa; este Phase 3 ejecuta los 6 componentes que quedaban pendientes tras el step 1 (DECISION-MAKERS.md ya commiteado el 2026-05-09 en `1f1ca02`).

**Componentes ejecutados:**

| # | Componente | Commit | Output principal |
|---|---|---|---|
| 1 | DECISION-MAKERS.md (registro 11 decisores) | `1f1ca02` (2026-05-09) | `04-system/03-governance/DECISION-MAKERS.md` |
| 2 | PENDING-DECISIONS-REGISTRY.md + siembra 7 decisiones | `8dc0bc6` | `04-system/03-governance/PENDING-DECISIONS-REGISTRY.md` |
| 3 | 5 carpetas inbox (04-decisions-in-flight/, 05-from-junta/, 06-from-regulators/, 07-from-third-parties/, 08-special-deliverables/) con `_index.md` por canal + `_outgoing/` donde aplica | `a2cc124` | `01-inbox/` reorganizado |
| 3.A | Colateral: track de 4 archivos audit fase4 (`skipped_*.txt` + `ocr_candidates_hde_man.json`) | `fe90647` | `04-system/06-logs/` |
| 3.B | Colateral: hybrid retroactive migration de 5 in-flight decisions a `04-decisions-in-flight/<project>/<decision-id>/context.md` | `428775f` | 5 context.md migrados |
| 4 | 4 templates governance (decision-request, alternative-proposal, regulator-submission, junta-decision-package) | `ff0e977` | `04-system/04-tools-and-scripts/templates/` |
| 5 | InboxBot v3.2 → v3.3 (mods F.1-F.4: detección canales nuevos, Paso 1.5 parseo decision-id, Paso 6 reentry, manejo AWAITING-DECISION) | `bf19a04` | `.claude/agents/inboxbot/AGENT.md` |
| 6 | FRONTMATTER-CONVENTIONS.md con status field (9 valores canónicos) + cross-ref desde NAMING-CONVENTIONS.md | `5c7352f` | `04-system/01-config/FRONTMATTER-CONVENTIONS.md` |

**Sub-decisiones de diseño (8) tomadas durante ejecución:**

Estas no estaban resueltas en el proposal Phase 2 y se formalizaron en sesión 2026-05-09 / 2026-05-10:

1. **Formalizar `PARTIALLY-RESPONDED` como estado canónico** — referenciado en patrón A.4 del proposal pero ausente en lista canónica B.2. Casos reales (DEC-2026-05-08-001 marcas anglicismos en convergence junta+SAPI) requieren el estado.

2. **Formalizar `CLOSED-NOT-VIABLE` como estado canónico** — idem A.4. Necesario para multi-decisor cuando alguien rechaza y no se va a alternative path.

3. **Crear nuevo estado `SUSPENDED-UPSTREAM`** — no existía en proposal. Distingue "esperando decisor" (acción del decisor humano) de "esperando insumo upstream" (acción de un agente del sistema). Caso fundador: DEC-2026-05-06-002 (claim primero LATAM bloqueado pending segunda iteración OL-3 + confirmación specs antes de poder enrutar a OWNER). Sin este estado, este tipo de bloqueos se mapean a PENDING con nota — pierde semántica útil para Bruna y para tracking de upstream.

4. **DEC-2026-05-08-D1-D5 (GST Labels) modelado como umbrella row** — el proposal sembraba esta entry sin definir si expandir a 5 sub-IDs (D1, D2, ..., D5) o tratarla como una sola decisión agrupadora. Decisión: umbrella hasta que las 5 D tengan scope concreto; cuando se materialicen, se expande con sub-IDs `DEC-2026-05-08-D1` ... `-D5`.

5. **Decision-ID generado por agente solicitante (no por InboxBot)** — el proposal no especificaba quién genera el ID. Decisión: el agente que activa Pause+Resume genera el ID al crear el package (formato `DEC-YYYY-MM-DD-NNN`). InboxBot solo actualiza estado y respuesta. Razón: modelo directo, evita mods adicionales a InboxBot AGENT.md.

6. **Track de skipped_*.txt + ocr_candidates como audit data** (no gitignore) — colateral 1 del step 3. Snapshot persistente del output de fase4 (2049 archivos del pendrive D omitidos por filtros): permite revisitar candidatos a OCR mejorado en el futuro. Trade-off aceptado: re-runs de fase4 generarán diffs informativos.

7. **Migración retroactiva hybrid: solo las 5 in-flight a `04-decisions-in-flight/`** (no las 2 cerradas) — colateral 2 del step 3. Decisiones cerradas (DEC-2026-05-04-001 RESPONDED, DEC-2026-04-29-001 CLOSED-WITHDRAWN) quedan referenciadas solo en registry; las 5 activas reciben workspace `<project-id>/<decision-id>/context.md`. Convención retroactiva nueva: solo `context.md` requerido (no fabricar `package.md` / `options.md` / `recommendation.md` / `response.md` para decisiones que ya existían pre-2026-05-09).

8. **Status field documentado en doc separado FRONTMATTER-CONVENTIONS.md** (no en NAMING-CONVENTIONS.md) — step 6. El proposal sección J recomendaba NAMING-CONVENTIONS pero ese doc tiene scope estricto de nombres de carpeta/archivo (subtitle explícito); status field es frontmatter YAML, scope distinto. Doc separado da home extensible para futuras convenciones de frontmatter (`risk_level`, `expiry_date`, `channel_published`, `reuse_potential` — sección 3 "Por definir").

**Alternativas consideradas:**

Las alternativas estructurales del proposal Phase 2 quedaron documentadas en su sección I (7 alternatives rechazadas: tools externos tipo Notion, mezclar pendings con DECISIONS, agente Decision Coordinator dedicado, canal único bypass, implementación monolítica, auto-detection por keywords, escritura concurrente al registry). Para las 8 sub-decisiones de esta sesión, las alternativas concretas se discutieron inline con Owner (ver mensajes user/assistant en la sesión 2026-05-09 / 2026-05-10) y la racional de cada elección quedó embebida arriba.

Nota específica para sub-decisión 3 (SUSPENDED-UPSTREAM): la alternativa era "mantener PENDING con nota explícita en Owner notes". Rechazada porque pierde la distinción semántica que importa para Bruna (¿estoy esperando humano externo o estoy esperando agente interno?). Coste de añadir vocabulario es mínimo.

Nota específica para sub-decisión 7 (hybrid migration): alternativas eran solo prospectiva (no migrar nada — barato pero deja registry sin workspaces para casos activos) y full retroactiva (incluir las 2 cerradas — máxima coherencia pero duplica info que ya vive en project folders). Hybrid es el balance.

**Implicaciones:**

- **Cualquier agente que active Pause+Resume** ahora tiene workflow estructurado: generar `DEC-YYYY-MM-DD-NNN`, crear package en `01-inbox/04-decisions-in-flight/<project-id>/<decision-id>/`, copiar versión adaptada al `_outgoing/` del canal correspondiente (05/06/07), añadir fila a `PENDING-DECISIONS-REGISTRY.md`.

- **InboxBot ahora ejecuta reentry** cuando detecta archivos con pattern `(DEC|JUNTA|REG|ALT)-\d{4}-\d{2}-\d{2}-[A-Z0-9]+` en canales 05/06/07: actualiza registry, identifica agente solicitante, invoca Raul para reanudar cadena. Skip automático para archivos correspondientes a decisiones aún PENDING/IN-DELIBERATION/SUSPENDED-UPSTREAM/PARTIALLY-RESPONDED (evita loops).

- **Frontmatter `status` extiende vocabulario de deliverables** con 9 valores canónicos. `AWAITING-DECISION-<id>` linkea explícitamente con registry; `CRISIS-DRAFT` linkea con patrón A.3 (override) y obliga post-mortem Bruna en 72h.

- **Vocabulario de estados extendido** vs proposal Phase 2: la lista canónica del registry pasa de 7 (B.2) a 10 estados con la formalización de PARTIALLY-RESPONDED + CLOSED-NOT-VIABLE + SUSPENDED-UPSTREAM. Las 5 templates governance (step 4) ya reflejan los 10 estados en sus `status:` enum.

- **`01-inbox/` ahora tiene 8 canales** (3 originales + 5 nuevos), cada uno con `_index.md` que documenta política de retención, anti-patterns y flujo. README parent actualizado.

- **NAMING-CONVENTIONS.md sigue enfocado en nombres** de carpeta/archivo. FRONTMATTER-CONVENTIONS.md es el nuevo home para convenciones de campos YAML.

- **Audit data del pendrive D ahora versionada** en git: 2049 paths omitidos + 35K de candidatos OCR. Permite recuperar selectivamente material si en el futuro hay capacidad para OCR mejorado.

- **5 packages retroactivos** en `04-decisions-in-flight/` (gme/, marcas-anglicismos-junta/, covenin-3445/, gst-r-etiquetas/) con context.md apuntando al material original disperso. Convención retroactiva (solo `context.md`) documentada en `_index.md`.

**Estado:**

- Pasos 1-6 ejecutados y commiteados en sesiones 2026-05-09 / 2026-05-10. 8 commits totales para los componentes (`1f1ca02`, `8dc0bc6`, `a2cc124`, `fe90647`, `428775f`, `ff0e977`, `bf19a04`, `5c7352f`).
- Step 7 (este DECISIONS entry): ✅ commit `54261d8`.
- Step 8 (MEMORY.md entry feedback): ✅ archivo `feedback_phase3_governance_pause_resume.md` + pointer en `MEMORY.md` (vive en `C:\Users\User\.claude\projects\C--Raul\memory\`, fuera del repo por diseño — memoria es per-installation, no per-repo).
- **Phase 3 governance: COMPLETADA 2026-05-10.** 9 commits totales (8 componentes + 1 closure entry).
- Validación end-to-end pendiente (sección H del proposal — checklist post-implementación): pasar una decisión real por Pause+Resume completo. Caso test natural: cuando Bruna desbloquee DEC-2026-05-06-002 (post OL-3 v2 + specs), pasarla por el nuevo flujo. Si funciona end-to-end, marcar el sistema como "validado en producción".
- Colaterales abiertos (no Phase 3, scope OCR pilot paralelo): `04-system/07-temp/`, `04-system/06-logs/ocr_candidates_hde_man_v2.json`, `04-system/06-logs/ocr_candidates_final.json`, `04-system/06-logs/ocr_dedup_report.md`. Resolver como bloque separado.

---

## 2026-05-10 — Formalización del pattern A.5 (Owner post-CSC derivative) + creación del catálogo vivo `GOVERNANCE-PATTERNS.md`

**Decisión:** formalizar A.5 — Owner post-CSC derivative — como nuevo patrón operativo de governance, y crear `04-system/03-governance/GOVERNANCE-PATTERNS.md` como catálogo vivo SSoT que reemplaza la sección A del proposal Phase 2 como referencia activa (el proposal queda como histórico).

**Contexto y motivación:**

Pregunta operativa del Owner durante sesión 2026-05-10 destapó una situación recurrente no cubierta por los 4 patrones originales: Owner toma un deliverable producido por la cadena CSC (típicamente decks de Vivienne, pero generalizable a outputs de Solenne / Atlas / Nerea), lo modifica con base en input post-CSC (reuniones con colaboradores, conversaciones informales, intuición / reframe basado en contexto que la cadena no tenía), y presenta esa versión modificada — NO la versión CSC original.

Sin formalizar este flujo, el sistema asume erróneamente que la versión CSC es lo presentado: agentes vinculan decisiones a la versión incorrecta, claims nuevos introducidos por Owner mid-modification no pasan por gate de Bruna, y la trazabilidad del proceso real se pierde.

A.5 es distinto de A.2 (Owner-driven alternative) — A.2 inserta una alternativa ANTES o EN LUGAR de la cadena CSC; A.5 ADAPTA un output que la cadena ya produjo. La distinción importa porque el routing es diferente (A.2 va por Bruna→Vera→Orlan pre-CSC; A.5 va por Bruna post-derivative solo si introduce claims nuevos).

**Alternativas consideradas:**

- **Extender A.2 para cubrir derivatives.** ❌ Rechazado: A.2 es "Owner desafía análisis CSC con propuesta nueva"; A.5 es "Owner refina output CSC pre-presentación". Mezclar pierde semántica útil para routing.
- **Documentar A.5 directamente en el proposal Phase 2** (revisar como v1.1). ❌ Rechazado: el proposal es histórico de la propuesta original; revisarlo retroactivamente borra la distinción entre lo propuesto y lo aprendido en implementación. Mejor catálogo vivo separado.
- **Documentar A.5 solo en memoria sin doc canónico.** ❌ Rechazado: memoria es per-installation; los patrones de governance son SSoT del repo y necesitan home estable y versionable.
- **Cubrir el caso ad-hoc cada vez que aparezca, sin patrón formal.** ❌ Rechazado: la pregunta del Owner emergió porque está pasando — sin patrón formal, cada caso se improvisará distinto y se pierden las garantías (Bruna review de claims nuevos, vinculación correcta de decisiones al DELTA).

**Implicaciones:**

- **Nuevo doc canónico:** `04-system/03-governance/GOVERNANCE-PATTERNS.md` v1.0. Incluye A.1-A.4 como resúmenes con link al proposal (para detalle completo) + A.5 con detalle full. A partir de aquí, este doc es el SSoT del catálogo de patrones; futuros A.6+ se agregan aquí.
- **Cross-ref en proposal Phase 2 §A:** nota agregada apuntando al catálogo vivo.
- **A.5 en operación:**
  - Output Owner-modificado vive en `03-projects/<dominio>/<project-id>/04-published-and-hand-off/` con sufijo `_owner-presented`.
  - Binario .pptx/.pdf/.docx gitignored como siempre; DELTA.md commiteado.
  - DELTA.md usa `delta-document-template.md` con frontmatter `pattern_applied: A.5`, campo `basado_en` linkeando a versión CSC original.
  - Si introduce claims nuevos → Bruna BR-3 quick antes de presentar; si no hay tiempo, escalar a A.3 (Crisis) con `status: CRISIS-DRAFT` + post-mortem 72h.
  - Si presentación va a decisor formal → activar A.1 (Pause+Resume) con `pieza_presentada` apuntando al DELTA.
- **Mecanismo de extensión documentado:** sección "Cómo proponer un patrón nuevo" en `GOVERNANCE-PATTERNS.md` da el flujo para A.6+.
- **Memoria actualizada:** `feedback_phase3_governance_pause_resume.md` extendida para mencionar A.5 como complemento del flujo Pause+Resume.

**Estado:**

- `GOVERNANCE-PATTERNS.md` creado con A.1-A.5 documentados.
- Cross-ref en proposal Phase 2 §A agregado.
- Memoria actualizada (vive fuera del repo en `C:\Users\User\.claude\projects\C--Raul\memory\`).
- **Pendiente cuando aparezca el primer caso real:** ejecutar A.5 end-to-end (Owner modifica un deck, crea DELTA, presenta, registra outcome). Será el primer test del patrón.

---

(próximas entradas debajo, en orden cronológico)
