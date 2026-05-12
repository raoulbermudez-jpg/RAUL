---
title: "PKA Audit Framework — adaptado a /RAUL/ post-Plan-Maestro"
type: foundations
status: candidate
version: 1.0
owner: Raoul Bermudez
created: 2026-05-12
updated: 2026-05-12
last_touched: 2026-05-12
confidence: medium
source_type: mixed
provenance:
  - "GPT 5.5 (2026-05-02): REPO_QUALITY_CHECKLIST_RAUL.md + PKA_AUDIT_CHECKLIST_GENERIC.md (originales en 01-inbox/03-raw-sources/raul-meta/2026-05-12_pka-audit-frame_gpt5.5/)"
  - "/RAUL/ post-Plan-Maestro Modelo A (sesión 2026-05-12, commits 9cc60f4 → 22878bc)"
adaptation_notes: |
  Marco original de GPT 5.5 adaptado al estado actual de /RAUL/ tras cerrar
  Plan Maestro Modelo A y bundle de eficiencia. Incorpora 7 secciones nuevas
  específicas al estado /RAUL/ no presentes en el original (Modelo A,
  taxonomía 6 clases, memoria 2-tier, chunking, Phase 3 governance, SSOT
  portable, índices markdown-first). Estructura de carpetas adaptada de
  12-folder GPT a 5-folder /RAUL/. Sin validators-by-risk-type (postpuesto
  hasta multi-dominio).
tags:
  - audit
  - quality-control
  - methodology
  - pka
---

# PKA Audit Framework — /RAUL/

> **Estado: candidate (v1.0).** Este framework está en período de validación
> (90 días, 3 auditorías reales). Solo se promueve a `status: stable` tras
> confirmar valor real. Ver `04-system/03-governance/DECISIONS.md` entrada
> "2026-05-12 — PKA Audit Framework adoptado como candidate" cuando exista.

## 0. Propósito y alcance

Este documento es la **guía operativa de auditoría de calidad de /RAUL/**.
Se usa para responder de forma estructurada preguntas como:

- ¿La arquitectura del sistema cumple los principios declarados (local-first, vendor-neutral, multi-LLM, files-as-database)?
- ¿Los 21 agentes están en patrón canónico Modelo A?
- ¿La taxonomía nominal de 6 clases está aplicada consistentemente?
- ¿La memoria opera en 2-tier con política activa?
- ¿Hay deuda técnica acumulada que requiera atención?
- ¿Existen riesgos no cubiertos por la gobernanza actual?
- ¿Qué brechas hay y cómo se priorizan?

**Audiencia:** Owner + Raul (orchestrator) durante auditorías periódicas.
También útil cuando se evalúa adoptar el sistema /RAUL/ como template para
otra persona (futuro starter-kit).

**Cuándo usar:**

- Auditoría programada (cada 30/90/180 días según madurez del sistema).
- Disparo por incidente o brecha detectada.
- Pre-decisión arquitectónica mayor (validar fundamentos antes de cambiar).
- Pre-extracción de starter-kit (asegurar que se hereda solo lo validado).

---

## 1. Principios rectores de /RAUL/ (auditorables)

### 1.1 Local-first

El conocimiento canónico vive en archivos del filesystem, no en aplicaciones cloud-bound.

**Criterios de cumplimiento:**

- [ ] El repo se puede leer y editar desde VS Code sin instalación adicional.
- [ ] El repo se versiona con Git.
- [ ] Ninguna aplicación externa (Notion, Obsidian, Airtable, etc.) es SSOT de información crítica.
- [ ] Cloud (Google Drive) opera como mirror / canal remoto, no como fuente.
- [ ] Backups son derivables del repo (no dependen de servicio externo).

### 1.2 Vendor-neutral / Multi-LLM

El sistema puede correr en cualquier LLM con esfuerzo mínimo de portabilidad.

**Criterios de cumplimiento:**

- [ ] Conceptuales de agentes (`04-system/02-agents/conceptual/`) están escritos LLM-agnóstico.
- [ ] Solo runtime adapters (`.claude/agents/<agente>/AGENT.md`) tienen wiring específico a Claude Code.
- [ ] Cambiar de LLM = reescribir runtimes (~70-130 líneas/agente), no conceptuales.
- [ ] Tools mappings concretos viven en runtime; conceptual habla en capability portable.

### 1.3 Files-as-database / Portable text format as SSOT

Per `DECISIONS.md` entrada 2026-05-12. Markdown estructurado es SSOT canónico; binarios son derivados runtime-dependientes.

**Criterios de cumplimiento:**

- [ ] Outputs con representación binaria (PowerPoint, Word, Sheets, PDF generado) tienen versión Markdown como SSOT.
- [ ] Las 3 excepciones documentadas se respetan: (a) Excel computacional → CSV+YAML, (b) PDFs anotados → PDF + JSON anotaciones, (c) cloud docs colaboración activa → cloud temporal.
- [ ] Conceptuales NO listan `.pptx via python-pptx` o equivalentes como capability — eso es runtime.

### 1.4 App-less

El sistema de archivos es la base de datos. No se depende de UI propietaria para operar.

**Criterios de cumplimiento:**

- [ ] Búsquedas se hacen con `Grep`/`Glob`/`Read` (LLM-tools); no requieren UI específica.
- [ ] Índices son Markdown estructurados (`_index-specs.md`, `_roster.md`, etc.), no bases vectoriales o de grafos obligatorias.
- [ ] Cualquier humano puede operar el sistema solo con VS Code + git.

### 1.5 Trazabilidad por defecto

Toda conclusión, decisión, output debe ser auditable.

**Criterios de cumplimiento:**

- [ ] Cada output relevante puede rastrearse hacia: fuente, agente que lo generó, fecha, contexto.
- [ ] Decisiones arquitectónicas viven en `DECISIONS.md` con formato canónico.
- [ ] Cadena CSC produce SI-3 (trazabilidad por cadena) al cerrar cada cadena.
- [ ] Memoria persistente lleva frontmatter con `last_touched`.

---

## 2. Sistema de puntuación

Para cada criterio usar escala 0-5:

| Puntaje | Significado |
|---:|---|
| 0 | No existe |
| 1 | Existe mínimo, incompleto o desordenado |
| 2 | Parcial, sin estándar claro |
| 3 | Funcional con brechas visibles |
| 4 | Bien implementado, documentado y usable |
| 5 | Excelente, completo, consistente, mantenible y probado |

### Interpretación global

| Promedio global | Diagnóstico |
|---:|---|
| 0.0 - 1.5 | Sistema inmaduro / requiere rediseño |
| 1.6 - 2.5 | Base útil con brechas importantes |
| 2.6 - 3.5 | Sistema funcional en evolución |
| 3.6 - 4.3 | Sistema sólido y operativo |
| 4.4 - 5.0 | Sistema maduro, bien gobernado, escalable |

---

## 3. Severidad de brechas

| Severidad | Definición |
|---|---|
| Crítica | Pérdida de información, exposición de secretos, errores graves, outputs peligrosos |
| Alta | Afecta calidad / escalabilidad / seguridad / trazabilidad de forma importante |
| Media | Limita eficiencia o claridad, no bloquea sistema |
| Baja | Mejora deseable, no urgente |

---

## 4. Estructura canónica de /RAUL/

A diferencia de la propuesta de 12 carpetas top-level del frame original GPT 5.5, /RAUL/ usa **5 carpetas top-level** con responsabilidades compactadas.

```text
C:\RAUL\
├── 01-inbox/                      # Entrada y salida operativa
│   ├── 01-owner-to-raul/          # Owner → Raul (briefs, pedidos)
│   ├── 02-deliverables-to-owner/  # Raul → Owner (entregables)
│   ├── 03-raw-sources/            # Material crudo pendiente proceso
│   ├── 04-decisions-in-flight/    # Phase 3 governance packages
│   ├── 05-from-junta/             # Phase 3 channel
│   ├── 06-from-regulators/        # Phase 3 channel
│   └── 07-from-third-parties/     # Phase 3 channel
│
├── 02-knowledge-base/             # LLM Wiki compilada
│   ├── 00-raul-intelligence/      # Memoria operativa Raul
│   ├── 01-foundations/            # Metodología, principios, frameworks
│   ├── 02-domains/                # Por dominio (wiki + specs + assets)
│   │   ├── 01-genteca/
│   │   ├── 02-plenus-metabolica/
│   │   ├── 03-finca-ganaderia/
│   │   ├── 04-teca-teak4food/
│   │   ├── 05-marca-personal-raoul/
│   │   └── 99-other-domains/
│   ├── 03-cross-cutting/          # Temas transversales
│   ├── 04-sops-and-playbooks/     # SOPs reutilizables
│   └── 05-glossary-and-tables/    # Glosarios + tablas referencia
│
├── 03-projects/                   # Trabajo operativo
│   └── <dominio>/<proyecto>/      # Etapas 00-brief → 04-published
│
├── 04-system/                     # Reglas, agentes, gobierno
│   ├── 01-config/                 # CLAUDE.md, CONTEXT_core.md, etc.
│   ├── 02-agents/                 # Conceptuales + content-supply-chain
│   ├── 03-governance/             # DECISIONS, RISK-POLICY, task-log
│   ├── 04-tools-and-scripts/      # Scripts y plantillas
│   ├── 05-indexes/                # Índices Markdown (Sira SSOT)
│   ├── 06-logs/                   # Logs operativos
│   └── 07-temp/                   # Scratch dir (gitignored)
│
└── 05-archive/                    # Histórico (no se edita day-to-day)
```

**Equivalencia con frame original GPT 5.5** (para auditorías que vienen de templates genéricos):

| Concepto GPT (12 folders) | Equivalente /RAUL/ (5 folders) |
|---|---|
| `00_inbox/` | `01-inbox/` |
| `01_sources/` | `01-inbox/03-raw-sources/` + `02-knowledge-base/02-domains/<dom>/` |
| `02_wiki/` | `02-knowledge-base/02-domains/<dom>/wiki/` |
| `03_projects/` | `03-projects/` |
| `04_operations/` | dentro de `03-projects/<dom>/<proy>/` (tasks, calendars, contacts per proyecto) |
| `05_outputs/` | dentro de `03-projects/<dom>/<proy>/04-published-and-hand-off/` |
| `06_agents/` | `.claude/agents/` (runtime) + `04-system/02-agents/` (conceptual) |
| `07_memory/` | `C:\Users\User\.claude\projects\C--Raul\memory\` (FUERA del repo) |
| `08_indexes/` | `04-system/05-indexes/` |
| `09_integrations/` | `.claude/` + `04-system/01-config/` |
| `10_logs/` | `04-system/06-logs/` + `04-system/03-governance/task-log.md` |
| `docs/` | `04-system/01-config/` + `02-knowledge-base/01-foundations/` |

---

## 5. Áreas de auditoría y checklists

### 5.1 Estructura general

| Criterio | Estado | Puntaje 0-5 | Observaciones |
|---|---|---:|---|
| Las 5 carpetas top-level existen y tienen propósito explícito | | | |
| Subcarpetas siguen convención `NN-nombre-en-kebab` | | | |
| Cada carpeta principal tiene README.md o equivalente | | | |
| No hay mezcla entre fuentes crudas, KB compilado, outputs y código | | | |
| Estructura permite crecer por dominio sin refactor | | | |
| Estructura permite crecer por agente sin refactor | | | |
| Repo navegable en VS Code en <30 segundos | | | |
| `_taxonomy.md` + `_roster.md` están al día | | | |

### 5.2 Fuente canónica y portabilidad

| Criterio | Estado | Puntaje | Observaciones |
|---|---|---:|---|
| Conocimiento principal en Markdown / YAML / JSON / CSV | | | |
| Documentos originales preservados (no sobrescritos) | | | |
| Outputs generados se diferencian visiblemente de fuentes | | | |
| Repo respaldable y versionable con git | | | |
| Reglas claras para binarios (.pptx, .docx, .pdf) | | | |
| Principio "Portable text as SSOT" aplicado (`DECISIONS.md` 2026-05-12) | | | |
| 3 excepciones SSOT documentadas y respetadas | | | |
| Drive cloud opera como mirror, no como fuente | | | |

### 5.3 LLM-agnóstico / Multi-LLM

| Criterio | Estado | Puntaje | Observaciones |
|---|---|---:|---|
| Conceptuales de agentes son vendor-neutral (sin python-pptx, WebSearch, etc. en §1-§10) | | | |
| Runtime adapters separados en `.claude/agents/` | | | |
| `_runtime-adapter-guide.md` documenta contrato de derivación | | | |
| `LLM-GUIDELINES.md` define model assignment policy | | | |
| Cambiar de LLM = solo runtime rewrite, no conceptual | | | |
| Reservados `.gemini/`, `.perplexity/` documentados (aunque vacíos) | | | |

### 5.4 Modelo A compliance (NEW respecto a frame GPT)

Modelo A = conceptual SSOT grueso + runtime delgado. Validado en sesión 2026-05-12.

| Criterio | Estado | Puntaje | Observaciones |
|---|---|---:|---|
| 21/21 agentes tienen banner SSOT verbatim en conceptual | | | |
| 21/21 agentes tienen las 10 secciones canónicas (§1 Identity → §10 Antipatterns) | | | |
| 21/21 agentes tienen footer correcto `*<clase>. <singleton?>. <domain o transversal>.*` | | | |
| 21/21 agentes tienen `Operaciones de control de versión (git add/commit/push)` en §3 boundaries | | | |
| Runtimes son ~70-130 líneas (solo wiring de plataforma) | | | |
| Sin duplicación defensiva runtime ↔ conceptual | | | |
| `_template-conceptual.md` actualizado con convenciones vigentes | | | |

### 5.5 Taxonomía nominal de 6 clases (NEW)

Las 6 clases canónicas: `orchestration`, `governance`, `global-service`, `content-supply-chain`, `domain-specialist`, `execution-utility`.

| Criterio | Estado | Puntaje | Observaciones |
|---|---|---:|---|
| `_taxonomy.md` define las 6 clases con criterios de membresía | | | |
| `_roster.md` clasifica cada agente con su clase + dominio | | | |
| Cada conceptual tiene footer con la clase correcta | | | |
| Docs estructurales (CLAUDE.md, ROUTING-GUIDE, FOLDER-ARCH, AGENTS_CSC) usan nomenclatura nominal (no "Capa X") | | | |
| Bruna documentada como doble-clase (governance + content-supply-chain) | | | |
| InboxBot clasificado como `execution-utility` | | | |

### 5.6 Memoria 2-tier (NEW)

Per `DECISIONS.md` entrada 2026-05-12.

| Criterio | Estado | Puntaje | Observaciones |
|---|---|---:|---|
| `MEMORY.md` (HOT layer) opera como auto-load por conversación | | | |
| `MEMORY_ARCHIVE.md` (COLD layer) existe con header explicativo | | | |
| Política de archivado mensual documentada y respetada | | | |
| Convención `last_touched` y `always_load` aplicada en memorias nuevas | | | |
| CONTEXT_core.md documenta el sistema 2-tier | | | |
| Sin MEMORY.md inflado >50 entradas | | | |

### 5.7 Chunking de conceptuales largos (NEW)

Per `DECISIONS.md` entrada 2026-05-12 (bundle eficiencia).

| Criterio | Estado | Puntaje | Observaciones |
|---|---|---:|---|
| Conceptuales con §11 >50 líneas tienen `<agent>_templates.md` companion | | | |
| 6 agentes chunked (aurelio/sira/vael/oz/solenne/bruna) con sus companion files | | | |
| Excepción InboxBot documentada (§11 = Phase 3 protocol crítico operacional, inline) | | | |
| `_template-conceptual.md` §11 documenta la convention | | | |

### 5.8 Phase 3 governance (NEW)

Sistema Pause+Resume para coordinar con humanos externos (Junta, regulators, third-parties).

| Criterio | Estado | Puntaje | Observaciones |
|---|---|---:|---|
| `PENDING-DECISIONS-REGISTRY.md` existe con schema canónico | | | |
| `DECISION-MAKERS.md` documenta decisores con IDs cortos | | | |
| Canales 04/05/06/07 en `01-inbox/` activos | | | |
| InboxBot §11 conceptual implementa protocolo completo | | | |
| Status vocabulary respetado (PENDING/IN-DELIBERATION/SUSPENDED-UPSTREAM/PARTIALLY-RESPONDED/RESPONDED/EXPIRED/CLOSED-*) | | | |
| Decision-IDs siguen regex canónica `(DEC\|JUNTA\|REG\|ALT)-YYYY-MM-DD-NNN` | | | |
| Decisiones in-flight con responses esperadas tienen row en registry | | | |

### 5.9 KB / Wiki estructurada

| Criterio | Estado | Puntaje | Observaciones |
|---|---|---:|---|
| `02-knowledge-base/` separada de fuentes crudas (`01-inbox/03-raw-sources/`) | | | |
| Cada dominio activo tiene `wiki/` + `specs/` + `assets/` (cuando aplica) | | | |
| `_index-specs.md` por dominio mantenido al día (Celeste responsabilidad en Genteca) | | | |
| Páginas wiki llevan frontmatter con metadatos | | | |
| Distinción evidencia / interpretación / decisión presente en páginas relevantes | | | |
| Páginas tienen estado de vigencia (`active` / `archived` / `superseded by X`) | | | |

### 5.10 Cobertura de dominios

Dominios activos o reservados en /RAUL/: Genteca, Plenus-metabolica, Finca-ganaderia, Teca-teak4food, marca-personal-raoul, 99-other-domains (incluye Panama emergente).

Por cada dominio, verificar:

| Dominio | Carpetas creadas | KB poblada | Proyectos activos | Agentes domain-specialist | Estado |
|---|:---:|:---:|:---:|:---:|---|
| Genteca | | | | | |
| Plenus-metabolica | | | | | |
| Finca-ganaderia | | | | | |
| Teca-teak4food | | | | | |
| marca-personal-raoul | | | | | |
| Panama (other-domains) | | | | | |

**Criterios de madurez por dominio:**

| Nivel | Significado |
|---:|---|
| 0 | Dominio no existe |
| 1 | Carpeta creada pero vacía |
| 2 | Estructura parcial (algunos directorios) |
| 3 | KB básica + 1+ proyecto activo |
| 4 | KB poblada + agentes domain-specialist contratados + workflows activos |
| 5 | Dominio maduro con feedback loop estable |

### 5.11 Frontmatter convention

| Criterio | Estado | Puntaje | Observaciones |
|---|---|---:|---|
| Frontmatter en notas wiki sigue formato canónico | | | |
| Campo `confidence` (low/medium/high) presente en notas con asserts | | | |
| Campo `source_type` presente | | | |
| Campo `last_touched` presente en memorias | | | |
| Campo `status` con valores canónicos (active/archived/superseded/etc.) | | | |
| Campo `sensitivity` presente cuando aplica (public/internal/confidential/sensitive) | | | |
| `FRONTMATTER-CONVENTIONS.md` actualizado | | | |

### 5.12 DECISIONS.md / registro de decisiones arquitectónicas

| Criterio | Estado | Puntaje | Observaciones |
|---|---|---:|---|
| `DECISIONS.md` existe y crece append-only | | | |
| Cada entrada tiene: fecha, decisión 1-línea, contexto, alternativas, implicaciones, estado | | | |
| Decisiones se referencian desde docs operativos cuando aplican | | | |
| Sin entradas inconsistentes / contradictorias sin reconciliación | | | |
| Phase 3 decisions van también a `PENDING-DECISIONS-REGISTRY.md` cuando son in-flight | | | |

### 5.13 Memoria persistente / aprendizajes

| Criterio | Estado | Puntaje | Observaciones |
|---|---|---:|---|
| MEMORY.md HOT presenta menos de ~50 entradas | | | |
| `00-raul-intelligence/` mantiene aprendizajes operativos | | | |
| Owner Profile documentado | | | |
| Domain Boundaries documentadas | | | |
| Estilo de escritura del Owner documentado | | | |
| Decisiones pasadas referenciables desde memoria | | | |

### 5.14 Logs y observabilidad

| Criterio | Estado | Puntaje | Observaciones |
|---|---|---:|---|
| `task-log.md` con cada delegación registrada (formato Markdown table) | | | |
| Outcomes claros (delivered/pending/blocked) | | | |
| Inboxbot tiene su task log separado o integrado | | | |
| Errores significativos quedan registrados | | | |
| Auditorías recurrentes producen logs en `04-system/06-logs/audits/` (futura ubicación) | | | |

### 5.15 Seguridad, privacidad, permisos

| Criterio | Estado | Puntaje | Observaciones |
|---|---|---:|---|
| `.gitignore` excluye secretos, scratch, baks, etc. | | | |
| Sin claves API o tokens commiteados | | | |
| `.env.example` sin secretos reales | | | |
| Datos sensibles del Owner protegidos (no commiteados) | | | |
| Agentes con permisos mínimos (sin acceso write fuera de su scope) | | | |
| Bruna gate obligatorio antes de Ivo publicación | | | |
| Cero git operations por agentes (Owner manual) | | | |

### 5.16 Documentación

| Criterio | Estado | Puntaje | Observaciones |
|---|---|---:|---|
| `CLAUDE.md` y `CONTEXT_core.md` reflejan estado actual del sistema | | | |
| Cada agente tiene conceptual + runtime documentados | | | |
| `ROUTING-GUIDE.md` actualizado con clases nominales | | | |
| `FOLDER-ARCHITECTURE.md` describe estructura vigente | | | |
| `_taxonomy.md` y `_roster.md` sincronizados | | | |
| Docs estructurales sin nomenclatura obsoleta ("Capa X" en system-wide) | | | |

### 5.17 Mantenimiento periódico

| Criterio | Estado | Puntaje | Observaciones |
|---|---|---:|---|
| Inbox owner-to-raul revisado al menos semanalmente | | | |
| `01-inbox/03-raw-sources/` se destila a KB cuando aplica | | | |
| Memorias inactivas >6 meses se archivan según política 2-tier | | | |
| Auditorías programadas (cada 30/90 días según madurez) | | | |
| Backups verificados | | | |
| Decisiones in-flight con SLA tracked en registry | | | |

---

## 6. Plantilla de diagnóstico por área

Aplicar este template a cada área §5.1-§5.17:

```text
Área: <nombre>
Puntaje promedio: X/5
Brechas detectadas:
  - <descripción 1> (severidad: Crítica/Alta/Media/Baja)
  - <descripción 2>
Recomendaciones priorizadas:
  1. <acción concreta>
  2. <acción concreta>
Próxima revisión: YYYY-MM-DD
```

---

## 7. Resumen ejecutivo de auditoría

Tras completar §5, consolidar en este formato:

```markdown
# Auditoría /RAUL/ — YYYY-MM-DD

## Estado general
**Promedio global:** X.X / 5
**Nivel de madurez:** <inmaduro / útil con brechas / funcional / sólido / maduro>

## Principales fortalezas
- <fortaleza 1>
- <fortaleza 2>

## Principales debilidades
- <debilidad 1>
- <debilidad 2>

## Riesgos críticos
- <riesgo 1>
- <riesgo 2>

## Puntajes por área

| Área | Puntaje | Prioridad de mejora |
|---|---:|---|
| 5.1 Estructura general | | |
| 5.2 Fuente canónica | | |
| 5.3 LLM-agnóstico | | |
| 5.4 Modelo A | | |
| 5.5 Taxonomía 6 clases | | |
| 5.6 Memoria 2-tier | | |
| 5.7 Chunking | | |
| 5.8 Phase 3 governance | | |
| 5.9 KB / Wiki | | |
| 5.10 Cobertura dominios | | |
| 5.11 Frontmatter | | |
| 5.12 DECISIONS | | |
| 5.13 Memoria persistente | | |
| 5.14 Logs y observabilidad | | |
| 5.15 Seguridad / permisos | | |
| 5.16 Documentación | | |
| 5.17 Mantenimiento | | |

## Brechas detectadas

| Brecha | Área | Severidad | Recomendación | Esfuerzo estimado |
|---|---|---|---|---|
| | | | | |

## Plan de mejora priorizado

### Prioridad 1 — Críticas (esta semana)
- [ ] ...

### Prioridad 2 — Altas (este mes)
- [ ] ...

### Prioridad 3 — Medias (próximos 90 días)
- [ ] ...

### Prioridad 4 — Bajas (cuando haya bandwidth)
- [ ] ...

## Próxima auditoría

**Fecha planeada:** YYYY-MM-DD
**Foco específico:** <si hay áreas que necesitan re-evaluación>
**Cambios al framework propuestos:** <learnings sobre el framework mismo>
```

---

## 8. Cómo aplicar este framework

### 8.1 Auditoría completa (cada 90 días o disparada por incidente)

1. **Preparación:**
   - Leer este framework completo.
   - Revisar resultados de auditoría anterior (si existe).
   - Identificar áreas específicas que recibieron cambios mayores desde última auditoría (priorizar revisión).

2. **Ejecución (por área):**
   - Para cada checklist §5.X: marcar Estado + asignar Puntaje + escribir Observaciones.
   - No saltarse áreas — incluso si parecen "obvio que está bien", el ejercicio de verificar revela cosas.
   - Cuando una brecha aparezca, clasificarla por severidad usando §3.

3. **Consolidación:**
   - Escribir resumen ejecutivo siguiendo §7.
   - Generar plan de remediación priorizado.
   - Guardar como `04-system/03-governance/audits/YYYY-MM-DD_self-audit_vN.md`.

4. **Cierre:**
   - Append entrada a `task-log.md` con resumen 1-línea + puntaje promedio.
   - Si la auditoría revela problemas estructurales: entrada en `DECISIONS.md`.
   - Programar próxima auditoría.

5. **Feedback al framework:**
   - Al final, anotar qué áreas del framework fueron difíciles de aplicar o no agregaron valor → input para v1.1.

### 8.2 Auditoría parcial (focused)

Cuando el disparador es un área específica (ej. "verificar Modelo A compliance tras nuevo agente"):

1. Aplicar solo el §5.X relevante.
2. Producir reporte corto (solo esa área).
3. NO promediar puntaje global con auditorías parciales.

### 8.3 Pre-decisión arquitectónica

Antes de aprobar cambios estructurales mayores (nueva clase de agente, nueva carpeta top-level, nuevo principio):

1. Aplicar §5.1-§5.8 (los principios fundamentales) para confirmar línea base.
2. Asegurar que la decisión no rompa criterios actualmente en 4-5/5.
3. Documentar en `DECISIONS.md` con referencia explícita a este framework.

---

## 9. Período de validación (estado: candidate)

Este framework v1.0 está en **período de prueba de 90 días** (hasta ~2026-08-12) durante el cual se ejecutarán **3 auditorías reales**:

| Auditoría # | Fecha objetivo | Foco |
|---|---|---|
| 1 (baseline) | 2026-05-12 a 2026-05-26 | Aplicar framework completo, generar baseline. Identificar áreas del framework difíciles/ambiguas. |
| 2 (validación) | 2026-06-12 ± 1 semana | Re-auditar áreas que recibieron remediación tras auditoría 1. |
| 3 (madurez) | 2026-08-12 ± 1 semana | Evaluación final del framework + decisión sobre v2.0 stable o ajustes. |

**Criterios de éxito del framework:**

- [ ] Las 3 auditorías producen scores reproducibles (mismo auditor da scores similares en áreas que no cambiaron).
- [ ] Cada auditoría surfacea al menos 1 brecha que no era visible sin el framework.
- [ ] Las remediaciones priorizadas tienen impact mesurable.
- [ ] Tiempo de aplicación es razonable (<3 horas para auditoría completa).
- [ ] Framework cubre los blind spots reales que importan a /RAUL/.

**Decisión post-período de validación:**

- Si éxito → promover a `status: stable` v2.0, evaluar construir Audit Agent (vía Michelina + Paxs).
- Si parcial → refinar a v1.x, extender período.
- Si fallo → descartar este framework, mantener auditorías informales.

---

## 10. Cambios respecto al original GPT 5.5

Este framework adapta `REPO_QUALITY_CHECKLIST_RAUL.md` (GPT 5.5, 2026-05-02) con los siguientes cambios sustanciales:

### Añadido (7 secciones nuevas)

- §1.3 Files-as-database / Portable text as SSOT (DECISIONS.md 2026-05-12)
- §5.4 Modelo A compliance
- §5.5 Taxonomía nominal 6 clases
- §5.6 Memoria 2-tier (HOT + ARCHIVE)
- §5.7 Chunking de conceptuales largos
- §5.8 Phase 3 governance (Pause+Resume)
- §9 Período de validación con criterios de éxito explícitos

### Modificado (adaptación al estado real /RAUL/)

- Estructura: 12 folders GPT → 5 folders /RAUL/ con mapping explícito
- Dominios: 7 dominios placeholder GPT → 5 dominios /RAUL/ (Genteca, Plenus-metabolica, Finca-ganaderia, Teca-teak4food, marca-personal-raoul + 99-other)
- "Agentes centrales + validadores + domain packs" → taxonomía 6 clases nominales
- Memoria flat → memoria 2-tier
- Conceptuales monolíticos → conceptual SSOT + runtime delgado (Modelo A)
- Frontmatter convention enriquecido con `last_touched` y referencia a memory 2-tier

### Descartado por ahora (no aplicable a /RAUL/ en estado actual)

- Vector / graph indexes (`08_indexes/vector/`, `08_indexes/graph/`) — overengineering para escala actual.
- JSON Schemas para todos los outputs — /RAUL/ es Markdown-first.
- Workflows en YAML pre-compilados — /RAUL/ usa delegación dinámica de Raul.
- Domain pack como estructura granular (`glossary.md`, `taxonomy.md`, `workflows.yaml`, etc.) — sobre-granularidad para Genteca; reconsiderar cuando Plenus/Finca/Teca crezcan.
- LLM Gateway abstracto — postpuesto hasta materialización Gemini/Perplexity.
- Validators por tipo de riesgo (10 propuestos por GPT) — postpuesto hasta multi-dominio con producción.

### Referencias

- Original GPT 5.5: `01-inbox/03-raw-sources/raul-meta/2026-05-12_pka-audit-frame_gpt5.5/REPO_QUALITY_CHECKLIST_RAUL.md`
- Sister doc genérico: `01-inbox/03-raw-sources/raul-meta/2026-05-12_pka-audit-frame_gpt5.5/PKA_AUDIT_CHECKLIST_GENERIC.md`
- Evaluación inicial: `01-inbox/02-deliverables-to-owner/2026-05-12_eval_pka-audit-frame_gpt5.5.md`

---

## 11. Changelog del framework

| Versión | Fecha | Cambios |
|---|---|---|
| 1.0 | 2026-05-12 | Versión inicial adaptada de GPT 5.5 con 7 secciones nuevas + estructura 5-folder /RAUL/. Estado: candidate. Período de validación 90 días. |

---

*Framework operativo en período de validación. Cualquier ajuste durante el período se registra en §11 changelog + entrada en DECISIONS.md cuando la próxima auditoría confirme que el cambio aporta valor real.*
