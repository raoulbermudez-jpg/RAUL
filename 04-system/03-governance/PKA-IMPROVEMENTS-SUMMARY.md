---
document_id: "PKA-IMPROVEMENTS-SUMMARY"
document_type: "analysis-and-recommendations"
author: "GitHub Copilot (Copilot Chat in VS Code)"
creation_date: "2026-05-08"
purpose: "Proporcionar análisis técnico y recomendaciones de mejora para el PKA basadas en auditoría, para que Claude Opus 4.7 evalúe antes de ejecutar cambios"
audience: ["Claude Opus 4.7", "Raoul Bermúdez", "Team"]
status: "historical-record"
ssot_for: []
depends_on: ["PKA-AUDIT-CHECKLIST.md", "FOLDER-ARCHITECTURE.md", "DECISIONS.md"]
version: "1.0"
how_to_use: "Record histórico del análisis original de Copilot. NO usar como SSOT activo. Para estado actualizado de cada recomendación, ver SCRIPTS-DEPENDENCIES.md (decisiones 1-5) y DECISIONS.md (entrada 2026-05-08 PKA audit cycle). Defectos de numeración (dos I.2, dos I.3, sección VI duplicada) preservados intencionalmente como evidencia del proceso."
---

# PKA-IMPROVEMENTS-SUMMARY.md
## Resumen ejecutable de mejoras recomendadas — Sistema Raul 2026

**Propósito:** Análisis ejecutable de la arquitectura del PKA con recomendaciones de mejora para que Claude Opus evalúe antes de ejecutar cambios.

**Quién lo usa:** Claude Opus 4.7 (evaluación), Raoul (aprobación), Copilot (implementación)  
**Cuándo:** Antes de hacer cambios estructurales al PKA  
**Cómo:** Leer, discutir, evaluar riesgos, registrar decisión en DECISIONS.md, ejecutar si se aprueba

---

## ⚠️ AUDITORÍA PROFUNDA — HALLAZGOS CRÍTICOS (2026-05-08)

Durante revisión profunda de estructura, scripts y proyectos se identificaron:

**CRÍTICOS (Impactan orden de ejecución):**
1. **3 scripts Python con rutas hardcodeadas** a `04-system/05-indexes/`:
   - `fase4_kb_formatter.py` línea 24-28: `PROGRESS_FILE = INDEXES_DIR / "fase4_progress.json"`
   - `pendrive_pipeline.py` línea 27: `REPORT_DIR = Path("C:/RAUL/04-system/05-indexes")`
   - `descargar_genteca_v2.py`: referencias indirectas
   - **Riesgo:** Si separamos `05-indexes/` en `canonical/` + `06-logs/`, estos scripts fallan

2. **Proyectos con estructura inconsistente:**
   - `2026-04_GSM-MB-RB-RF_empaque/`: estructura completa (00-04) ✓
   - `2026-04_GST-R_etiquetas/`: estructura completa (00-04) ✓
   - `2026-05-07_marcas-anglicismos-junta/`: **INCOMPLETO** (solo etapa 03)
   - `2026-05_GIII-MV_manual/`: **INCOMPLETO** (solo etapa 01)

**IMPORTANTES:**
3. **Naming violation:** Proyecto `GME Estudios de mercado/` (tiene espacios)
4. **Archivos sueltos:** WORKSTREAM_v5, build_deck.py, _governance/ sin documentación
5. **Dominios:** Solo Genteca tiene proyectos; otros 4 dominios vacíos (escalabilidad OK, confusión de "8 proyectos activos")

**Impacto en recomendaciones:** El orden de I.1-I.3 ha sido revisado. I.2 (SCRIPTS-DEPENDENCIES) es ahora crítico y debe ejecutarse PRIMERO.

---

## Contexto

Análisis hecho por Copilot el 2026-05-08 con auditoría profunda (no solo nivel 2-3, sino también revisión de scripts, dependencias y estado real de proyectos).

---

## I. MEJORAS DE PRIORIDAD ALTA (Ejecutar en próximas 2 semanas)

### I.1 — Consolidar y clarificar SSOT (Single Source of Truth)

**Problema:** 
- Hay potencial confusión entre archivos core en `04-system/01-config/` e índices en `04-system/05-indexes/`.
- Un cambio en `FOLDER-ARCHITECTURE.md` podría no sincronizar con la realidad del repo.
- Los documentos companion (sufijo `PERPLEXITY`) podrían ser usados como SSOT por error.

**Recomendación:**
- Crear un nuevo documento: `04-system/03-governance/SSOT-MATRIX.md` que liste explícitamente:
  - Fuente de verdad para cada concepto (ej. "estructura de carpetas" → `FOLDER-ARCHITECTURE.md`)
  - Quién es responsable de mantenerla actualizada
  - Cuándo se revisa (diaria, semanal, por ciclo de proyecto)
  - Qué sucede si diverge de la realidad

**Formato propuesto:**

| Concepto | SSOT | Responsable | Cadencia | Audiencia |
|----------|------|-------------|----------|-----------|
| Estructura de carpetas | `04-system/01-config/FOLDER-ARCHITECTURE.md` | Raoul | Cambios ad-hoc + auditoría mensual | Todos los agentes |
| Nombres de archivos/carpetas | `04-system/01-config/NAMING-CONVENTIONS.md` | Claude (en consulta) | Cambios ad-hoc + auditoría mensual | Todos |
| Decisiones arquitectónicas | `04-system/03-governance/DECISIONS.md` | Raoul | Cada decisión (log permanente) | Todos |
| Estado de dominios | `04-system/05-indexes/domains-index.md` | Raoul + especialista por dominio | Al cambiar estado del dominio | Agentes del dominio |
| Estado de proyectos | `04-system/05-indexes/projects-index.md` | Raoul + PM de proyecto | Semanal o al cambio de estado | Equipos de proyecto |
| Alcance de dominio | `02-knowledge-base/02-domains/<dominio>/_index.md` | Especialista de dominio | Trimestral o al cambiar alcance | Equipo del dominio |
| Delegaciones | `04-system/03-governance/task-log.md` | Raoul (o bot) | Diaria/por delegación | Raoul, agentes |

**Acción recomendada:**
- Copilot/Claude: crear `SSOT-MATRIX.md` basado en template arriba
- Revisar y completar en sesión con Raoul
- Registrar decisión en `DECISIONS.md`
- Hacer referencia en `README.md` de raíz y `CONTEXT_core.md`

---

### I.2 — Separar índices de logs en `04-system/05-indexes/`

**Problema:**
- La carpeta `05-indexes/` mezcla:
  - Índices de contenido (ej. `domains-index.md`, `projects-index.md`) — debería ser SSOT vivo
  - Logs de ejecución (ej. `fase4_20260427_0723.log`) — son históricos/debug
  - Catálogos de assets (ej. `pendrive_D_assets_catalog.json`) — provisionales

**Recomendación:**
- Crear subcarpeta: `04-system/05-indexes/canonical/` para índices vivos
- Crear subcarpeta: `04-system/06-logs/` para logs de ejecución
- Mover a `06-logs/`:
  - `fase4_*.log`
  - `pendrive_pipeline_*.log`
  - Cualquier log de script o bot
- Mantener en `05-indexes/canonical/`:
  - `domains-index.md`
  - `projects-index.md`
  - `kb-index-by-domain.md`
  - `research-index.md` (si existe)

**Estructura propuesta:**

```text
04-system/
  05-indexes/
    canonical/
      _index.md           ← mapa de los índices canónicos
      domains-index.md    ← SSOT de dominios activos
      projects-index.md   ← SSOT de proyectos activos
      kb-index-by-domain.md
      research-index.md
  06-logs/
    _index.md
    fase4_*.log
    pendrive_pipeline_*.log
    [otros logs de ejecución]
```

**Acción recomendada:**
- Copilot: crear `04-system/06-logs/` y mover logs correspondientes
- Crear `04-system/05-indexes/canonical/_index.md`
- Actualizar `FOLDER-ARCHITECTURE.md` para reflejar el cambio
- Registrar en `DECISIONS.md`
- Actualizar referencias en `README.md`

---

### I.3 — Definir política explícita de versionado de documentos

**Problema:**
- Algunos documentos tienen frontmatter o comentarios con versión (ej. `FOLDER-ARCHITECTURE.md` v2.2)
- Otros no tienen marcas de versión
- No hay proceso claro de cómo se propagan cambios

**Recomendación:**
- Crear plantilla de frontmatter YAML estándar para documentos vivos:

```yaml
---
title: "Nombre del documento"
type: "core | companion"  # core = SSOT, companion = apoyo
version: "X.Y.Z"          # seguir semver
last_updated: "2026-05-DD"
updated_by: "nombre o rol"
reviewed_by: "si aplica"
approval_required: true/false
ssot_for: ["concepto1", "concepto2"]
---
```

- Aplicar a todos los documentos en `04-system/01-config/` (son core)
- Aplicar a todos los índices en `04-system/05-indexes/canonical/`
- Documentar la convención en `NAMING-CONVENTIONS.md` o nuevo archivo `04-system/01-config/FRONTMATTER-CONVENTIONS.md`

**Acción recomendada:**
- Copilot: crear template y aplicar a documentos principales
- Definir quién aprueba cambios de cada documento (usualmente Raoul)
- Crear script o checklist para verificar frontmatter antes de cambios

---

### I.2 — Crear SCRIPTS-DEPENDENCIES.md (CRÍTICO — Ejecutar PRIMERO)

**Problema (hallazgo de auditoría profunda):**
- 3 scripts Python tienen rutas hardcodeadas a `04-system/05-indexes/`
- Si separamos `05-indexes/` sin actualizar, se rompen inmediatamente

**Recomendación:**
1. Crear `04-system/01-config/SCRIPTS-DEPENDENCIES.md`
2. Documentar cada script y su dependencia de rutas
3. Actualizar scripts para usar variables de entorno
4. Registrar en `DECISIONS.md`

---

### I.3 — Estandarizar estructura de proyectos (NUEVA PRIORIDAD ALTA)

**Problema (hallazgo de auditoría profunda):**
- 2 proyectos completos, 2 incompletos
- Naming violation: `GME Estudios de mercado/` (espacios)

**Recomendación:**
1. Crear plantilla de proyecto
2. Crear `PROJECT-INCOMPLETE-REGISTRY.md`
3. Documentar decisión para incompletos

---

## II. MEJORAS DE PRIORIDAD MEDIA (Ejecutar en próximas 4–6 semanas, DESPUÉS de I.1-I.4)

### II.1 — Separar índices de logs (SOLO después de I.2 completado)

**Contexto:** Depende de que scripts estén actualizados con env vars.

**Recomendación:**
- Crear `04-system/05-indexes/canonical/` para índices
- Crear `04-system/06-logs/` para logs
- Mover logs SOLO después de confirmar I.2 completado

---

### II.2 — Crear PKA-FLOW.md: diagrama del flujo operativo

**Problema:**
- El PKA tiene una arquitectura clara, pero no hay un único documento que explique el flujo end-to-end.
- Un nuevo agente o colaborador debe leer `FOLDER-ARCHITECTURE.md`, `DECISIONS.md` y otros para entender cómo fluye el contenido.

**Recomendación:**
- Crear `04-system/01-config/PKA-FLOW.md` que documente:
  - **Entrada:** cómo el contenido llega a `01-inbox/`
  - **Procesamiento:** cómo se decide si va a KB, proyecto o archivo
  - **Compilación:** cómo raw sources se convierten en wiki
  - **Ejecución:** cómo proyectos consumen KB y generan entregas
  - **Salida:** cómo se entregan resultados y se archiva contenido
  - **Feedback loop:** cómo se captura el aprendizaje (00-raul-intelligence)

**Acción recomendada:**
- Copilot: crear `PKA-FLOW.md` con diagramas y descripción narrativa
- Incluir ejemplos reales de cómo un brief se convierte en proyecto
- Incluir ejemplos de cómo contenido bruto (PDFs, transcripciones) llega a wiki
- Incluir decisión tree para routing (¿esto va a KB? ¿proyecto? ¿archivo?)

---

### II.2 — Formalizar plantillas de proyecto

**Problema:**
- Proyectos siguen patrón `00-brief` a `04-published`, pero hay riesgos de inconsistencia
- No hay una plantilla reutilizable que garantice que todos los proyectos tengan:
  - README.md clara
  - Estructura de etapas consistente
  - Enlace a dominio y KB
  - Registro de stakeholders

**Recomendación:**
- Crear `04-system/04-tools-and-scripts/templates/project-template/` con plantillas reutilizables
- Documentar cómo usarlas en instrucciones para agentes

**Acción recomendada:**
- Copilot: crear plantillas
- Aplicar a proyecto actual como prueba piloto
- Documentar en `04-system/01-config/CLAUDE.md`

---

### II.4 — Definir política de archivo y limpieza de `01-inbox`

**Problema:**
- `01-inbox` está excluido de Git (buena decisión)
- Pero no hay política explícita sobre:
  - Cuándo se mueve contenido de `01-owner-to-raul` a proyecto
  - Cuándo se purga `01-inbox` vs archivo
  - Quién es responsable de limpieza

**Recomendación:**
- Crear `04-system/03-governance/INBOX-POLICY.md` que documente:
  - Ciclo de vida de archivos en cada subcarpeta de inbox
  - Retención máxima (TTL) para cada tipo
  - Responsables de limpieza
  - Cadencia de auditoría

**Acción recomendada:**
- Copilot: crear `INBOX-POLICY.md`
- Definir quién es responsable
- Registrar en `DECISIONS.md`

---

## III. MEJORAS DE PRIORIDAD BAJA (Ejecutar en próximas 8–12 semanas o cuando sea natural)

### III.1 — Automatizar generación de índices

Script Python que:
- Lea estructura real de `02-knowledge-base/02-domains/`
- Genere índices automáticamente
- Genere reporte de discrepancias

---

### III.3 — Crear dashboard HTML de salud del PKA

Script que genere `PKA-Dashboard.html` con:
- Conteo de dominios y proyectos
- Últimas actualizaciones
- Alertas de proyectos vencidos

### III.4 — Integración de agentes con versionado automático

Cuando un agente o Claude modifique un documento core:
- Registrar versión automáticamente (frontend para edición)
- Crear snapshot en `04-system/05-indexes/snapshots/`
- Notificar a Raoul para aprobación si afecta SSOT

---

## VI. RIESGOS Y MITIGACIONES

| Riesgo | Severidad | Mitigación |
|--------|-----------|-----------|
| **Separar índices rompe scripts** (si no se completa I.2 primero) | CRÍTICO | Ejecutar I.2 ANTES que cualquier reorganización. Mapear dependencias. Usar env vars. |
| Proyectos incompletos nunca finalizan | Alto | Crear registry (I.3) y decisión explícita en DECISIONS.md |
| Documentos viven de forma desincronizada | Alto | Crear SSOT-MATRIX (I.1) con responsables y cadencias |
| Agentes crean carpetas/archivos sin convención | Medio | Documentar NAMING-CONVENTIONS, actualizar PROMPT de Claude |
| Scripts de automatización quedan obsoletos | Medio | Versionarlos y documentar mantenimiento cada trimestre |
| Alcance de dominios crece sin límite | Bajo | Revisar PKA-FLOW con criterios de inclusión/exclusión por dominio |

---

## VII. CONCLUSIÓN

Este documento establece un plan de mejora estructurado y realista para el PKA. **Las prioridades ALTA son ejecutables en 2 semanas**, con énfasis en **I.2 (SCRIPTS-DEPENDENCIES)** como paso crítico que debe completarse **antes** de cualquier reorganización de carpetas.

**Próximo paso:** Copilot presenta esto a Claude Opus para evaluación y aprobación antes de ejecutar cambios estructurales.

## IV. DECISIONES Y PRÓXIMOS PASOS

### IV.1 — Decisión de Raoul/Claude Opus

Antes de ejecutar **cualquiera** de estas mejoras, revisar:

1. ¿Son las prioridades las correctas para el contexto actual?
2. ¿Hay mejoras que contradigan decisiones existentes?
3. ¿Hay impacto en agentes o flujos?
4. ¿Necesita reprogramación de scripts?

### IV.2 — Recomendación de secuencia (CRÍTICO: I.2 debe ser PRIMERO)

Si se aprueban todas:

1. **Semana 1, Día 1:** I.1 (SSOT-MATRIX)
2. **Semana 1, Día 2-3:** I.2 (SCRIPTS-DEPENDENCIES — CRÍTICO, debe ser primero) — requiere actualizar 3 scripts
3. **Semana 1, Día 4-5:** I.3 (Estandarizar proyectos) — crear plantilla y registry
4. **Semana 2:** I.4 (Versionado de documentos)
5. **Semana 3:** II.1 (Separar índices/logs — SOLO después de I.2)
6. **Semana 4:** II.2 (PKA-FLOW)
7. **Semana 5:** II.3 (Plantillas de proyecto)
8. **Semana 6:** II.4 (INBOX-POLICY)
9. **Después:** III.x (automatización)

### IV.3 — Registro en DECISIONS.md

Crear entrada documentando decisión, razonamiento y responsables.

---

## V. ARCHIVOS INVOLUCRADOS

### Nuevos archivos a crear:

- `04-system/03-governance/SSOT-MATRIX.md`
- `04-system/01-config/SCRIPTS-DEPENDENCIES.md` (I.2 — CRÍTICO)
- `04-system/03-governance/PROJECT-INCOMPLETE-REGISTRY.md` (I.3)
- `04-system/01-config/PKA-FLOW.md`
- `04-system/03-governance/INBOX-POLICY.md`
- `04-system/04-tools-and-scripts/templates/project-template/README.md`

### Archivos a actualizar:

- `04-system/01-config/FOLDER-ARCHITECTURE.md`
- `04-system/01-config/NAMING-CONVENTIONS.md`
- `04-system/03-governance/DECISIONS.md`
- `README.md` (raíz)

### Archivos a reorganizar:

- Mover logs de `04-system/05-indexes/` a `04-system/06-logs/`
- Crear `04-system/05-indexes/canonical/`

---

## VI. RIESGOS Y MITIGACIÓN

| Riesgo | Impacto | Mitigación |
|--------|---------|-----------|
| Cambios estructurales rompan scripts | Alto | Revisar scripts antes de reorganizar |
| Agentes desincronizados | Medio | Crear proceso explícito de sync |
| Índices se desfasen nuevamente | Medio | Automatizar o revisar cadencia |
| Documentación nueva no se mantiene | Bajo–Medio | Incluir en auditoría mensual |

---

**Documento preparado por:** GitHub Copilot  
**Para revisión por:** Claude Opus 4.7, Raoul Bermúdez  
**Versión:** 1.0 | **Fecha:** 2026-05-08
