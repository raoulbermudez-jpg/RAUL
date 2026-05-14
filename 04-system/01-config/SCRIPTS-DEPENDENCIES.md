---
document_id: "SCRIPTS-DEPENDENCIES"
document_type: "operational-reference"
author: "Claude Opus 4.7 (auditoría 2026-05-08)"
creation_date: "2026-05-08"
last_updated: "2026-05-08"
purpose: "Inventario canónico de scripts ejecutables del sistema /RAUL/, sus dependencias de paths, y el plan de refactor para soportar reorganización estructural sin romperlos"
audience: ["Raoul Bermúdez (Owner)", "Claude Opus 4.7", "Agentes de mantenimiento"]
status: "active"
ssot_for: ["scripts-inventory", "scripts-path-dependencies", "env-vars-canonical"]
depends_on: ["FOLDER-ARCHITECTURE.md", "NAMING-CONVENTIONS.md", "DECISIONS.md"]
version: "1.0"
how_to_use: "Consultar antes de mover carpetas, renombrar root, o tocar cualquier script Python/PowerShell. Actualizar al añadir scripts nuevos. Re-auditar cuando se refactorice un script de Tier 1."
---

# SCRIPTS-DEPENDENCIES.md
## Inventario y dependencias de paths — Sistema /RAUL/

**Propósito:** documentar qué scripts existen, qué paths usan hardcoded, y cómo refactorizarlos para que la reorganización estructural del repo no los rompa.

**Origen:** auditoría 2026-05-08 ejecutada por Claude Opus 4.7 tras detección por GitHub Copilot de 3 scripts críticos. Auditoría identificó 22 scripts activos (vs. 3 reportados originalmente).

---

## Decisiones registradas (Owner, 2026-05-08)

| # | Decisión | Estado |
|---|---|---|
| 1 | Crear este documento como SSOT de dependencias de scripts | Ejecutado (commit 9207aaf) |
| 2 | Tier 3 (legacy pre-/RAUL/): abandonar — mover a `05-archive/03-system-history/legacy-scripts/` | Ejecutado (commit 52d7e9b) |
| 3 | Renombrar `GME Estudios de mercado/` → naming compliant + actualizar scripts internos | Ejecutado como `2025-04_GME_estudios-mercado/` (commit b41279e) |
| 4 | Casing canónico: `C:\RAUL` (uppercase). Forward slash vs backslash queda al criterio del autor (pathlib y PowerShell aceptan ambos) | Ejecutado parcial (commit 3c3cad1 — scripts; md files pendientes en cleanup futuro) |
| 5 | Refactor Tier 1 a env vars con helper `raul_paths.py` (flat, no en `_lib/` por simplicidad) | Ejecutado (commit f1d98fa) |
| 6 | Separación física `05-indexes/` (canonical curated, flat) ↔ `06-logs/` (runtime + machine-generated). Helper renombra `INDEXES_CANONICAL_DIR` → `INDEXES_DIR`, elimina `REPORTS_DIR`. | Ejecutado (este commit) |

Estas decisiones deben replicarse como entrada en [DECISIONS.md](../03-governance/DECISIONS.md) tras ejecución completa.

---

## Tier 1 — Pipeline operativo activo (refactor obligatorio)

Scripts que corren regularmente o que son orquestados por agentes/cron. Refactor a env vars antes de cualquier reorganización de `04-system/`.

| Script | Líneas con paths | Variables actuales | Dependencias críticas |
|---|---|---|---|
| `04-system/04-tools-and-scripts/fase4_kb_formatter.py` | 24-29 | `STAGING`, `KB_SPECS`, `INDEXES_DIR`, `PROGRESS_FILE`, `LOG_FILE`, `ENV_FILE` | **Bloquea** separación `05-indexes/` ↔ `06-logs/`. Usa `.env` en root. |
| `04-system/04-tools-and-scripts/pendrive_pipeline.py` | 18-23 | `PENDRIVE` (D:/), `KB_GENTECA`, `STAGING`, `ASSETS_BASE`, `REPORT_DIR`, `LOG_FILE` | **Bloquea** misma separación. `D:/` es pendrive físico (correcto que sea hardcoded). |
| `04-system/04-tools-and-scripts/scripts/backup_kb_to_onedrive.ps1` | 12-14 | `$source`, `$dest`, `$logDir` | Corre vía Task Scheduler `RAUL_KB_Backup_OneDrive` (23:00 diario). Mover el .ps1 requiere reconfigurar la tarea. |

### Plan de refactor Tier 1

**Variables de entorno canónicas:**

```
RAUL_ROOT          = C:\RAUL                     (default)
RAUL_INBOX         = ${RAUL_ROOT}\01-inbox
RAUL_KB            = ${RAUL_ROOT}\02-knowledge-base
RAUL_PROJECTS      = ${RAUL_ROOT}\03-projects
RAUL_SYSTEM        = ${RAUL_ROOT}\04-system
RAUL_INDEXES_DIR   = ${RAUL_SYSTEM}\05-indexes               (canonical curated indexes)
RAUL_LOGS_DIR      = ${RAUL_SYSTEM}\06-logs                  (runtime logs + machine-generated reports)
```

**Helper Python propuesto:** crear `04-system/04-tools-and-scripts/_lib/raul_paths.py` con función `get_paths()` que retorna un dataclass con todos los paths resueltos. Cada script Tier 1 hace `from _lib.raul_paths import get_paths`.

**PowerShell:** usar `$env:RAUL_ROOT` con fallback a `C:\RAUL` (la actualización de `backup_kb_to_onedrive.ps1` debe corregir el casing de `C:\Raul` → `C:\RAUL` simultáneamente — ver sección "Casing canónico").

**Configuración de la variable:** documentar en [CLAUDE.md](CLAUDE.md) y en `04-system/01-config/CONTEXT_core.md` que `RAUL_ROOT` puede setearse via:
1. System Environment Variables (Windows) — preferido para producción.
2. `.env` file en root del repo — preferido para desarrollo (ya existe).
3. Default hardcoded en `raul_paths.py` (`C:\RAUL`).

**Estado de ejecución (2026-05-08):**

Ejecutado como Paso 3d. Deviations del plan original:

- **Helper plano `raul_paths.py`** directo en `04-tools-and-scripts/`, NO en `_lib/`. Razón: un solo módulo, simplicidad de import, evita complicaciones de package/namespace. Si emergen más helpers, refactorizar a `_lib/` entonces.
- **Documentación de `RAUL_ROOT` solo en `CONTEXT_core.md`**, NO en `CLAUDE.md`. Razón: CLAUDE.md describe rol de agente (Identity, Cardinal Rule, routing); paths son configuración de sistema, pertenecen a CONTEXT_core.

Self-test del helper post-3d + post-separación 05-indexes/06-logs: 8/9 paths [OK] (todos activos incluyendo INDEXES_DIR y LOGS_DIR), 1/9 [MISSING] esperado (`.env` opcional según Owner).

---

## Tier 2 — Scripts de proyecto (auto-contenidos)

Scripts que viven dentro de un proyecto y son específicos de él. NO se refactorizan masivamente: se actualizan solo si se renombra el proyecto o si el proyecto se archiva.

| Script | Path hardcoded | Acción |
|---|---|---|
| `03-projects/genteca/2026-04_GSM-MB-RB-RF_empaque/03-review-and-release/gsm_empaque_redlines_v4.py:15-16` | `C:\RAUL\01-inbox\...`, `C:\RAUL\03-projects\...` | Movido a su proyecto (follow-up #2). Casing fix en commit 3c3cad1. |
| `03-projects/genteca/2026-05-07_marcas-anglicismos-junta/build_deck.py:205` | OUTPUT a su propio folder | Auto-contenido. Solo casing fix. |
| `03-projects/genteca/2026-04_GSM-MB-RB-RF_empaque/03-review-and-release/build_junta_pptx.py:34` | `C:\Raul\...` | Casing fix. |
| `03-projects/genteca/2026-04_GSM-MB-RB-RF_empaque/02-production/Atlas_mockups_v1/render_B_v2.py:27` | `C:\Raul\...` | Casing fix. |
| `03-projects/genteca/2026-04_GSM-MB-RB-RF_empaque/03-review-and-release/Junta_PPTX_v2/build_v6.py:20` | `C:\Raul\...` | Casing fix. |

### Sub-grupo Tier 2 especial: GME Estudios de mercado

6 scripts internos referencian la carpeta padre por nombre absoluto:

| Script | Línea |
|---|---|
| `_extract_comments.py` | 7-8 |
| `_analyze_survey.py` | 8 |
| `_extract_images.py` | 7 |
| `_van_westendorp.py` | 15-16 |
| `_read_docx.py` | 7 |
| `03-review-and-release/_build_pptx.py` | 22-23 |

**Acción coordinada (Paso 3):**
1. Renombrar carpeta `GME Estudios de mercado/` → `2025-XX_GME_estudios-mercado/` (mes específico a confirmar Owner — el contenido sugiere proyecto GME activo en 2025-2026, pero la fecha de inicio del proyecto debe estimarse). Sugerencia: usar `2025-04_` si no hay fecha mejor (alineado al ciclo Q2 2025).
2. Actualizar las 6 referencias internas en el mismo commit.
3. Si algún cron task o referencia externa apunta a la carpeta vieja, también actualizar.

**Excepción si rename no procede:** documentar en DECISIONS.md como excepción de naming (C3 del checklist) con razón explícita.

---

## Tier 3 — Legacy pre-/RAUL/ (abandonar)

Scripts cuyos paths hardcoded apuntan a workspaces previos al sistema /RAUL/ (`C:\WorkspaceIA\`, `G:\Mi unidad\WorkspaceIA\`). Probabilidad alta de que ya no funcionen y/o que sus inputs no existan en esas rutas.

| Script | Path legacy |
|---|---|
| `04-system/04-tools-and-scripts/scripts/descargar_genteca.py:10` | `G:\Mi unidad\WorkspaceIA\RAG_SOURCES` |
| `04-system/04-tools-and-scripts/scripts/descargar_genteca_v2.py:10` | mismo |
| `04-system/04-tools-and-scripts/scripts/celeste_screening_loteC.py:12-13` | `G:/Mi unidad/WorkspaceIA/RAG_SOURCES`, `c:/WorkspaceIA/PROJECTS/Claude code/Owner Inbox/` |
| `04-system/04-tools-and-scripts/scripts/ocr_stubs.py:14,16-17` | Tesseract path absoluto, `c:\WorkspaceIA\PROJECTS\Claude code\Knowledge Base\Technical`, `G:\Mi unidad\WorkspaceIA\RAG_SOURCES` |
| `03-projects/genteca/2026-04_GST-R_etiquetas/02-production/gen_gst_r_pdf_v2.py:21-22` | `C:\WorkspaceIA\PROJECTS\Genteca\Work In Progress\`, `C:\WorkspaceIA\Owner Inbox\` |
| `03-projects/genteca/2026-04_GST-R_etiquetas/02-production/gen_gst_r_pptx_v2.py:15-18` | mismo |

### Plan de archivado (Paso 3, decisión 2)

**Destino:** `05-archive/03-system-history/legacy-scripts/`

**Procedimiento:**
1. Crear `05-archive/03-system-history/legacy-scripts/` con `_index.md` explicativo.
2. Mover los 6 scripts arriba listados.
3. Crear redirección documental: dejar archivo `04-system/04-tools-and-scripts/scripts/_LEGACY_MOVED.md` que indique destino del archivado.
4. NO modificar el contenido de los scripts archivados — preservar como historial.
5. Registrar en DECISIONS.md.

**Riesgo cubierto:** si en el futuro un agente busca esos scripts, encuentra el redirector y entiende que están abandonados, no rotos.

---

## Scripts excluidos del refactor

### `01-inbox/03-raw-sources/genteca/gst-labels/` (3 scripts)

`gen_redlines.py`, `gen_redlines_zoom.py`, `gen_gla_t.py` — generadores one-shot que viven con sus propios inputs. NO son código operativo del sistema. Quedan tal cual.

---

## Casing canónico (decisión 4)

**Estándar:** `C:\RAUL` — uppercase, backslash en raw strings Python.

**Estado post-fix (commits 3c3cad1, f1d98fa, 5b7ef15, 27487a2):**

✅ Casing normalizado a `C:\RAUL` en scripts (3b) y en docs (follow-up #1, 36 archivos / 341 ocurrencias). Tier 1 además refactorizado a env var `RAUL_ROOT` via helper `raul_paths.py` (3d).

Snapshot histórico pre-fix (referencia):
- `C:/RAUL` (forward slash uppercase) → `fase4_kb_formatter.py`, `pendrive_pipeline.py` — refactorizados a `paths.*` en 3d.
- `C:\Raul` (mixed case) → `backup_kb_to_onedrive.ps1`, `build_junta_pptx.py`, `render_B_v2.py`, `build_v6.py`, `gsm_empaque_redlines_v4.py` — corregidos en 3b.
- `C:\RAUL` (canónico) → `gen_redlines*`, `gen_gla_t`, GME scripts — ya estaban correctos.

**Notas:**
- En Python, raw strings con backslash: `r"C:\RAUL\..."` (no doble backslash, no forward slash).
- En PowerShell: `"C:\RAUL\..."` (sin raw, comillas dobles).
- En Markdown / config docs: usar forward slash `/RAUL/` para consistencia visual.
- En `pathlib.Path()`: aceptar cualquier separador, pero **construir** con backslash para Windows-nativo.

**Filesystem es case-insensitive en Windows**, por lo que el casing inconsistente NO produce errores en runtime ahora — pero romperá en migraciones a Linux/Docker, en git case-sensitive, y produce diffs ruidosos.

---

## Riesgos cross-cutting (no son scripts pero dependen de paths)

### 1. InboxBot AGENT.md

`.claude/agents/inboxbot/AGENT.md` contiene paths absolutos hardcoded de los canales de Drive (`G:\Mi unidad\RAUL\01-inbox\...`) y la trigger config. Desde el rediseño v5.0 (capture-only, 2026-05-14) InboxBot **ya no escribe al repo** — todos sus outputs (tickets en `00-cola/`, `_log-ciclos.md`, `_ESTADO.md`, marcadores) viven en la nube de Drive. Si se reorganizan esas carpetas de Drive, hay que editar AGENT.md.

**Restricción crítica (memoria):** `.claude/agents/<agente>/AGENT.md` debe modificarse con **Read+Edit, NUNCA con Write**. Write produce loops de permisos.

### 2. InboxBot canales (Drive Desktop)

InboxBot lee de `G:\Mi unidad\RAUL\01-inbox\01-owner-to-raul\`. Esto NO es path local — es Google Drive Desktop streaming. Está documentado en AGENT.md y NO debe normalizarse a `C:\RAUL\`.

### 3. Cueva legacy

Path `C:\Users\User\Mi unidad\RAUL\` es residuo de Google Backup & Sync (descontinuada). InboxBot está instruido para detectarlo y rechazar. No hay verificación automática — riesgo activo.

### 4. Cron tasks externas (Task Scheduler)

Conocida: `RAUL_KB_Backup_OneDrive` (23:00 diario) ejecuta `backup_kb_to_onedrive.ps1` por path absoluto. Si se mueve el .ps1, hay que reconfigurar la tarea programada.

**Acción de auditoría sugerida (no bloqueante):** Owner exporta lista de tareas programadas con `schtasks /Query /TN RAUL_KB_Backup_OneDrive /XML` y la guarda como referencia en este doc.

### 5. `.env` en root

`fase4_kb_formatter.py:29` hardcoded `C:/RAUL/.env`. Patrón aceptable (env file en root del repo). Confirmar que `.env` está en `.gitignore` (debe estarlo).

---

## Validación post-refactor (checklist)

Después de ejecutar Paso 3, validar:

- [x] `raul_paths.py` creado, testado y consumido por `fase4_kb_formatter.py` + `pendrive_pipeline.py`.
- [x] `backup_kb_to_onedrive.ps1` usa `$env:RAUL_ROOT` con fallback + casing corregido.
- [x] Tier 3 movido a `05-archive/03-system-history/legacy-scripts/` con `_index.md`.
- [x] `_LEGACY_MOVED.md` creado en `04-system/04-tools-and-scripts/scripts/`.
- [x] Carpeta `GME Estudios de mercado/` renombrada (`2025-04_GME_estudios-mercado/`) y 13 archivos con citaciones actualizados.
- [x] DECISIONS.md actualizado con entrada cubriendo decisiones 1-4 (commit 9252e83).
- [x] Documentación de `RAUL_ROOT` añadida a `CONTEXT_core.md`.
- [ ] `RAUL_ROOT` seteado a nivel de sistema (Owner action — opcional, default funciona). Paso a paso documentado en `CONTEXT_core.md` sección "Configuración de paths para scripts (`RAUL_ROOT`)".
- [x] `gsm_empaque_redlines_v4.py` movido a `03-projects/genteca/2026-04_GSM-MB-RB-RF_empaque/03-review-and-release/`.
- [x] `FOLDER-ARCHITECTURE.md` actualizado con la reorganización 05-indexes/06-logs (Opción B flat: 05-indexes/ contiene 5 índices canónicos directos; 06-logs/ contiene logs + pendrive_D_*).

---

## Comando de detección de regresiones

Para verificar que no se introduzcan paths hardcoded en futuros scripts:

```powershell
# Buscar paths absolutos C:\RAUL o C:/RAUL en archivos Python/PowerShell
Select-String -Path "C:\RAUL\**\*.py","C:\RAUL\**\*.ps1" `
  -Pattern 'C:[/\\]+(?i)raul' `
  -Exclude *.git*,*worktrees*,*05-archive* |
  Where-Object { $_.Line -notmatch '_lib[/\\]raul_paths' }
```

(Cualquier match fuera de `_lib/raul_paths.py` debe revisarse.)

---

## Referencias cruzadas

- [FOLDER-ARCHITECTURE.md](FOLDER-ARCHITECTURE.md) — estructura canónica de carpetas.
- [NAMING-CONVENTIONS.md](NAMING-CONVENTIONS.md) — reglas C3 (no espacios en folders).
- [DECISIONS.md](../03-governance/DECISIONS.md) — log permanente de decisiones arquitectónicas.
- [PKA-AUDIT-CHECKLIST.md](../03-governance/PKA-AUDIT-CHECKLIST.md) — sección G1 (riesgos de scripts).
- [PKA-IMPROVEMENTS-SUMMARY.md](../03-governance/PKA-IMPROVEMENTS-SUMMARY.md) — propuesta original I.2 (parcial).
- [.claude/agents/inboxbot/AGENT.md](../../.claude/agents/inboxbot/AGENT.md) — config con paths hardcoded (manejar con Read+Edit).

---

**Próxima revisión:** al ejecutar Paso 3, o cuando se añada un script nuevo en `04-system/04-tools-and-scripts/`.
