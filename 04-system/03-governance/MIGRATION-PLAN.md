# MIGRATION-PLAN.md
## De estructura previa (repo + workspace hermano) a `/RAUL/`

**Versión:** 1.0
**Última actualización:** 2026-04-21
**Decisión registrada en:** `04-system/03-governance/DECISIONS.md`
**Arquitectura destino:** `04-system/01-config/FOLDER-ARCHITECTURE.md` v2.1

---

## 0. Pre-requisitos

Antes de arrancar fase 1:

1. ✅ `FOLDER-ARCHITECTURE.md` v2.1 aprobado por el Owner.
2. ✅ Entrada en `DECISIONS.md` declarando la migración, fecha, alcance y responsable.
3. ✅ Backup del estado actual:
   - Snapshot de `C:\WorkspaceIA\PROJECTS\Claude code\` (repo completo).
   - Snapshot de `C:\WorkspaceIA\PROJECTS\Genteca\Work In Progress\` (26+ archivos activos).
   - Export del trigger InboxBot actual (`trig_01RgGGbpCvckUzSwkyGMDNtm`) y sus configuraciones.
4. ✅ Ventana de tiempo dedicada: aprox. 4 días hábiles distribuibles; fase 4 exige bloque continuo de 3-4 horas.

---

## 1. Fase 1 — Skeleton paralelo (día 1, medio día)

**Objetivo:** crear `/RAUL/` vacío en disco, con el árbol completo pero sin contenido migrado. Ningún archivo actual se mueve. Los documentos fundacionales (FOLDER-ARCHITECTURE.md, MIGRATION-PLAN.md) se escriben aquí como parte de esta fase.

**Acciones:**

1. Crear `C:\RAUL\` y todas las subcarpetas del árbol definido en `FOLDER-ARCHITECTURE.md` §1.
2. **[YA HECHO]** Escribir `FOLDER-ARCHITECTURE.md` v2.1 en `04-system/01-config/`.
3. **[YA HECHO]** Escribir `MIGRATION-PLAN.md` v1.0 en `04-system/03-governance/`.
4. Crear `README.md` stub en cada subcarpeta top-level con una línea describiendo su función.
5. Escribir `DECISIONS.md` en `04-system/03-governance/` con la primera entrada de decisión (migración).
6. Escribir `NAMING-CONVENTIONS.md` stub en `04-system/01-config/` (detalle posterior).
7. Inicializar git en `/RAUL/` con el `.gitignore` de FOLDER-ARCHITECTURE §10.2.
8. Primer commit: "Skeleton Raul 2026 — pre-migration".

**Archivos tocados:** ninguno del estado previo.

**Validación:**
- `ls -R C:\RAUL\` muestra el árbol completo.
- `git status` en `/RAUL/` reporta clean tree tras primer commit.
- Estado previo (`C:\WorkspaceIA\PROJECTS\Claude code\` + `PROJECTS/Genteca/`) intacto.

**Rollback:** borrar `C:\RAUL\`. Cero impacto.

**Riesgo:** bajo.

---

## 2. Fase 2 — Migrar system (día 2)

**Objetivo:** trasladar CLAUDE.md, CONTEXT.md, Team/* y los 17 agentes a sus posiciones finales en `/RAUL/04-system/` y `/RAUL/.claude/`. Validar que Claude Code sigue operando desde `/RAUL/`.

**Acciones:**

1. **Copiar** (no mover) los siguientes a sus destinos:

   | Origen | Destino |
   |---|---|
   | `Claude code/CLAUDE.md` | `/RAUL/04-system/01-config/CLAUDE.md` |
   | `Claude code/CONTEXT.md` | `/RAUL/04-system/01-config/CONTEXT.md` (añadir nota inicial: "Contexto ampliado complementario a CLAUDE.md") |
   | `Claude code/Team/ROUTING-GUIDE.md` | `/RAUL/04-system/02-agents/content-supply-chain/ROUTING-GUIDE.md` |
   | `Claude code/Team/RUNBOOK_Raul_Global.md` | `/RAUL/04-system/02-agents/content-supply-chain/RUNBOOK_Raul_Global.md` |
   | `Claude code/Team/roster.md` | `/RAUL/04-system/02-agents/conceptual/_roster.md` |
   | `Claude code/Team/task-log.md` | `/RAUL/04-system/03-governance/task-log.md` |
   | `Claude code/Team/CLAUDE-CODE-RULES.md` | `/RAUL/04-system/01-config/CLAUDE-CODE-RULES.md` |
   | `Claude code/Team/content/ARCHITECTURE_Content-Supply-Chain.md` | `/RAUL/04-system/02-agents/content-supply-chain/ARCHITECTURE_Content-Supply-Chain.md` |
   | `Claude code/Team/content/AGENTS_Content-Supply-Chain.md` | `/RAUL/04-system/02-agents/content-supply-chain/AGENTS_Content-Supply-Chain.md` |
   | `Claude code/ocr_stubs.py` | `/RAUL/04-system/04-tools-and-scripts/scripts/ocr_stubs.py` |
   | `Claude code/Team/celeste_screening_loteC.py` | `/RAUL/04-system/04-tools-and-scripts/scripts/celeste_screening_loteC.py` |
   | `Claude code/CHANGELOG_GrupoA-D.md` (×4) | `/RAUL/05-archive/03-system-history/` |
   | `Claude code/CLAUDE.before_grupoA.md` | `/RAUL/05-archive/03-system-history/old-CLAUDE-configs/` |
   | `Claude code/Team/roster.before_grupoA.md` | `/RAUL/05-archive/03-system-history/` |
   | `Claude code/Team/celeste-lote-*.md` (×2) | `/RAUL/05-archive/03-system-history/` |

2. **Agentes: crear `conceptual/` como SSOT derivando desde los AGENT.md actuales:**

   Para cada uno de los 17 agentes en `Claude code/.claude/agents/<nombre>/AGENT.md`:
   - Copiar el cuerpo (sin frontmatter) a `/RAUL/04-system/02-agents/conceptual/<nombre>.md`.
   - Copiar el archivo entero (con frontmatter) a `/RAUL/.claude/agents/<nombre>/AGENT.md`.
   - Al finalizar: ambos archivos existen; `conceptual/<nombre>.md` es SSOT, `AGENT.md` es derivado.

3. **Actualizar paths internos** en los archivos copiados. Usar búsqueda+reemplazo global sobre `/RAUL/`:
   - `c:\WorkspaceIA\PROJECTS\Claude code\` → `C:\RAUL\` (y derivados)
   - `Team/` → `04-system/` cuando se refiera a docs migrados
   - `Team/content/` → `04-system/02-agents/content-supply-chain/`
   - `.claude/agents/` → `.claude/agents/` (sin cambio, ya en raíz)
   - `Knowledge Base/Technical/` → `02-knowledge-base/02-domains/01-genteca/specs/`
   - `Knowledge Base/Market/` → `02-knowledge-base/02-domains/01-genteca/wiki/market/`
   - `Assets/Products/` → `02-knowledge-base/02-domains/01-genteca/assets/products/`
   - `Assets/Packaging/` → `02-knowledge-base/02-domains/01-genteca/assets/packaging/`
   - `Assets/Diagrams/` → `02-knowledge-base/02-domains/01-genteca/assets/diagrams/`
   - `Assets/Uncoded/` → `02-knowledge-base/02-domains/01-genteca/assets/uncoded/`
   - `Owner Inbox/` → `01-inbox/02-deliverables-to-owner/`
   - `Team inbox/` → `01-inbox/01-owner-to-raul/`

4. **Abrir Claude Code en `/RAUL/`** y validar:
   - `/agents` lista los 17 agentes correctamente desde `/RAUL/.claude/agents/`.
   - Delegación a un agente de prueba (ej. Paxs) funciona.
   - Lecturas a paths actualizados no fallan (spot-check en 3-4 archivos).

5. Commit: "Fase 2 — system migrado a 04-system/ y agentes a .claude/+conceptual/".

**Archivos tocados:**
- Creación: todo bajo `/RAUL/04-system/` y `/RAUL/.claude/`.
- Lectura: repo previo.
- **No se borra nada del estado previo en esta fase.**

**Validación:**
- Claude Code abre en `/RAUL/`, delega correctamente.
- Los 17 agentes aparecen.
- Referencias internas en los docs copiados no tienen paths del estado previo.

**Rollback:** borrar `/RAUL/04-system/` y `/RAUL/.claude/`. Volver a operar desde `Claude code/`.

**Riesgo:** medio. Principales puntos de fallo:
- Paths internos mal actualizados → agente no encuentra archivo referenciado. Mitigación: grep exhaustivo post-replace.
- Frontmatter de agentes desalineado entre `conceptual/` y `.claude/agents/` → Claude Code puede fallar al cargar. Mitigación: validar con `/agents` antes de cerrar fase.

---

## 3. Fase 3 — Migrar knowledge + projects (día 3)

**Objetivo:** mover la Knowledge Base técnica, los assets y los proyectos operativos de Genteca a la nueva estructura.

**Acciones:**

1. **KB Technical (192 docs):**
   - Mover `Claude code/Knowledge Base/Technical/*.md` → `/RAUL/02-knowledge-base/02-domains/01-genteca/specs/`.
   - Copiar `Claude code/Knowledge Base/Technical/_index.md` → `/RAUL/02-knowledge-base/02-domains/01-genteca/specs/_index-specs.md`.
   - Actualizar paths internos del índice.
   - Crear `/RAUL/02-knowledge-base/02-domains/01-genteca/wiki/` vacío con stub `_index.md` (se poblará después).
   - Crear `_index.md` del dominio Genteca describiendo alcance, marcas (Exceline, Exceline Profesional, Genius), enlaces a `wiki/`, `specs/` y proyectos activos.

2. **KB Market:**
   - Mover `Claude code/Knowledge Base/Market/*` → `/RAUL/02-knowledge-base/02-domains/01-genteca/wiki/market/`.
   - Decisión v2.1: queda bajo Genteca provisionalmente (está fuertemente ligado a Genteca). Reevaluar cuando market cross-dominio crezca.

3. **Assets Genteca:**
   - `Claude code/Assets/Products/` → `/RAUL/02-knowledge-base/02-domains/01-genteca/assets/products/`
   - `Claude code/Assets/Packaging/` → `/RAUL/02-knowledge-base/02-domains/01-genteca/assets/packaging/`
   - `Claude code/Assets/Diagrams/` → `/RAUL/02-knowledge-base/02-domains/01-genteca/assets/diagrams/`
   - `Claude code/Assets/Uncoded/` → `/RAUL/02-knowledge-base/02-domains/01-genteca/assets/uncoded/`
   - Actualizar `_index.md` correspondientes.

4. **Proyectos Genteca activos** (`PROJECTS/Genteca/Work In Progress/` con 26+ archivos):
   - Identificar las 2 campañas en curso:
     - **GSM-MB-RB-RF empaque** (archivos con prefijo `GSM-MB-RB-RF_*`)
     - **GST-R etiquetas** (archivos con prefijo `GST-R_*`)
   - Crear en `/RAUL/03-projects/genteca/`:
     - `2026-04_GSM-MB-RB-RF_empaque/` con subcarpetas `00-brief/` a `04-published-and-hand-off/`
     - `2026-04_GST-R_etiquetas/` con misma estructura
   - Repartir los archivos por etapa:
     - Briefs técnicos y pedidos → `00-brief/`
     - Delta v1-v2-v3, scripts generadores → `03-review-and-release/`
     - PDFs finales comentados → `03-review-and-release/` o `04-published-and-hand-off/` según estado Keiddys
     - Emails a Ozwaldo → `03-review-and-release/`
     - PPTX editables → según destino
   - Crear `README.md` en cada proyecto con objetivo, stakeholders y estado.
   - Scripts operativos (`gen_gst_r_pptx_v2.py`, etc.) quedan dentro del proyecto si son ad-hoc; si son reutilizables, mover a `04-system/04-tools-and-scripts/scripts/`.
   - Si hay archivos ambiguos, usar carpeta `unsorted/` temporal dentro del proyecto; resolver luego.

5. **Staging:**
   - `C:\WorkspaceIA\Staging\Genteca\2026-04-19\` → `/RAUL/01-inbox/03-raw-sources/genteca/2026-04-19/`

6. **RAG_SOURCES y scripts huérfanos del parent workspace:**
   - `C:\WorkspaceIA\RAG_SOURCES\` (lo no procesado aún) → `/RAUL/01-inbox/03-raw-sources/`
   - `C:\WorkspaceIA\descargar_genteca*.py` → `/RAUL/04-system/04-tools-and-scripts/scripts/`

7. Commit: "Fase 3 — KB Genteca + assets + proyectos activos migrados".

**Archivos tocados:** movimiento masivo.

**Validación:**
- KB índice de Genteca lista 192 specs.
- Vera/Orlan (test: delegar una consulta técnica) pueden localizar un spec sheet específico (GSM-ASBS, por ejemplo).
- Ambos proyectos de Genteca tienen `README.md` y estructura 00-04.
- Grep de `Knowledge Base/Technical` en `/RAUL/` devuelve cero resultados (todos los refs actualizados).

**Rollback:** el estado previo aún existe intacto; se puede reanudar operando desde ahí. El contenido movido se restaura por reverso.

**Riesgo:** alto. Principales puntos:
- Pérdida o duplicación de archivos durante el movimiento → usar `copy` + validación, luego `delete` solo cuando se confirma integridad.
- Clasificación errónea por etapa en proyectos → dejar `unsorted/` temporal; resolver luego.

---

## 4. Fase 4 — Reconfigurar inbox + Drive + InboxBot (día 4, bloque continuo 3-4h)

**Objetivo:** mover el flujo remoto del Owner (Drive, InboxBot) a la nueva estructura. **Ventana de inestabilidad operativa remota: 24-48h hasta validación completa.**

**Prerequisito:** Antes de ejecutar esta fase, portar el script `inboxbot.py` desde el entorno histórico (`C:\WorkspaceIA\PROJECTS\Claude code\...`) a `C:\RAUL\04-system\04-tools-and-scripts\scripts\inboxbot.py`, manteniendo la misma lógica pero actualizando rutas según este plan y la sección 10.3–10.4 de `FOLDER-ARCHITECTURE.md`.

**Acciones — en orden estricto:**

1. **Avisar al Owner** que el flujo remoto estará en mantenimiento durante las próximas X horas. No subir briefs al Team Inbox viejo durante la ventana.

2. **Migrar contenido actual de inboxes:**
   - `C:\WorkspaceIA\PROJECTS\Claude code\Owner Inbox\*` → `/RAUL/01-inbox/02-deliverables-to-owner/` (archivar lo antiguo en `05-archive/` si aplica).
   - `C:\WorkspaceIA\PROJECTS\Claude code\Team inbox\*` (vacío) — nada que migrar.
   - `C:\WorkspaceIA\Owner Inbox\*` → `/RAUL/01-inbox/02-deliverables-to-owner/` (dedup con lo anterior).

3. **Reconfigurar Google Drive Desktop:**
   - Detener sync actual.
   - Re-mapear `G:\Mi unidad\RAUL\` = `C:\RAUL\01-inbox\` + `C:\RAUL\02-knowledge-base\` (según §10.3 de la arquitectura).
   - Validar sync bidireccional funciona.
   
   **Configuración objetivo de Drive Desktop (Fase 4)**

- Modo "Mi unidad" (My Drive): stream o mirror según preferencia de espacio en disco (no afecta la lógica de RAUL).
- Directorios locales sincronizados desde "Este equipo" hacia Google Drive:
  - `C:\RAUL\01-inbox\01-owner-to-raul`  <->  `Mi unidad\RAUL\01-inbox\01-owner-to-raul`
  - `C:\RAUL\01-inbox\02-deliverables-to-owner`  <->  `Mi unidad\RAUL\01-inbox\02-deliverables-to-owner`
  - `C:\RAUL\02-knowledge-base`  <->  `Mi unidad\RAUL\02-knowledge-base`

Esta configuración debe aplicarse en Drive for desktop en la misma ventana de trabajo en que se porte `inboxbot.py` y se re‑cree el trigger, para que el cut-over sea atómico y fácil de revertir si algo falla.

4. **Re-crear InboxBot trigger:**
   - Eliminar (o pausar) trigger `trig_01RgGGbpCvckUzSwkyGMDNtm`.
   - Crear nuevo trigger con:
     - Lectura: `G:\Mi unidad\RAUL\01-inbox\01-owner-to-raul\*`
     - Marcadores DONE_: en la misma carpeta.
     - Gmail drafts: sin cambio.
     - Frecuencia: cada 4h (igual que antes).
   - Guardar nuevo trigger ID en `DECISIONS.md`.

5. **Test end-to-end:**
   - Owner sube un archivo de prueba a `G:\Mi unidad\RAUL\01-inbox\01-owner-to-raul\` desde su móvil.
   - Esperar ciclo InboxBot (hasta 4h o forzar manual).
   - Verificar que Raul lo procesa y deja una entrega en `01-inbox/02-deliverables-to-owner/`.
   - Verificar que el Owner ve la entrega en Drive móvil.

6. **Archivar estado previo:**
   - Mover `C:\WorkspaceIA\PROJECTS\Claude code\` entero → `/RAUL/05-archive/03-system-history/Claude-code_pre-migration_YYYY-MM-DD/`.
   - Mover `C:\WorkspaceIA\PROJECTS\Genteca\` (lo que no se migró por obsoleto) → `/RAUL/05-archive/02-projects-completed/Genteca_pre-migration_YYYY-MM-DD/`.

7. Commit: "Fase 4 — inbox + Drive + InboxBot reconfigurados. Migración completa.".

**Archivos tocados:** inboxes + config externa (Drive, Zapier/Routines).

**Validación:**
- Test end-to-end completo (paso 5).
- Owner confirma acceso desde móvil a deliverables.
- 24-48h sin incidentes tras cut-over.

**Rollback:** complejo. Requiere:
- Restaurar trigger viejo con ID original.
- Re-mapear Drive a estructura anterior.
- Revertir carpetas archivadas.

Por eso esta fase exige ventana dedicada y paso-a-paso validado.

**Riesgo:** alto. Mitigación: correr fase en horario de baja actividad del Owner; mantener canal directo (mensaje) durante la ventana.

---

## 5. Fase 5 — Post-migración: limpieza y cierre (día 5)

**Tras fase 4 validada (72h estables):**

1. Entrada final en `DECISIONS.md`: migración completada, fecha, lecciones aprendidas, ajustes pendientes.
2. Actualizar `task-log.md` con las 4 fases como entregas.
3. Generar snapshot inicial de `05-archive/01-knowledge-base-old/snapshots-YYYY-MM/` con el estado de la KB pre-migración (si no se hizo antes).
4. Crear `projects-index.md`, `kb-index-by-domain.md`, `research-index.md` en `04-system/05-indexes/` con el estado actual (poblados, no vacíos).
5. Primera revisión de agentes: leer `conceptual/` y verificar que todos ellos mencionan rutas actualizadas.

**Riesgo:** bajo.

---

## 6. Fase 6 — Contexto core + piloto por dominio (futura, opcional, disparable a voluntad del Owner)

**Objetivo:** implementar la estrategia de contexto descrita en `FOLDER-ARCHITECTURE.md` §8 — archivos core compactos y el primer par piloto por dominio.

**Pre-requisitos:** fases 1-5 completadas y estables. Sistema en operación al menos 1 semana tras migración para tener señal real de qué contenido es "core" vs "dominio".

**Acciones:**

1. **Generar `CLAUDE_core.md`:**
   - Leer `CLAUDE.md` actual (tras migración, en `/RAUL/04-system/01-config/CLAUDE.md`).
   - Destilar a 1-2k tokens máximo con: filosofía de trabajo, reglas globales, estilo de respuestas, políticas de seguridad y vendor-neutralidad.
   - Escribir en `/RAUL/04-system/01-config/CLAUDE_core.md`.
   - `CLAUDE.md` original queda como referencia ampliada (rol similar a CONTEXT.md).

2. **Generar `CONTEXT_core.md`:**
   - Leer `CONTEXT.md` actual.
   - Destilar a 200-500 tokens con: descripción breve de dominios, cómo usar el árbol `/RAUL/`, rol general de agentes principales.
   - Escribir en `/RAUL/04-system/01-config/CONTEXT_core.md`.

3. **Primer piloto: Genteca** (dominio con más actividad):
   - `CLAUDE_genteca.md`: reglas específicas — tono de marca Genteca, terminología obligada (ej. "tensión nominal" no "voltaje nominal"), constraints del equipo humano (Keiddys/Valeria/Oscar/Ozwaldo), prioridades de comunicación B2B.
   - `CONTEXT_genteca.md`: productos clave (Exceline, Exceline Profesional, Genius), líneas actuales (GSM, GST-R, GI+, GII+, GIII+, GOCT, GSPT, etc.), marcas, mercados, vocabulario típico, restricciones regulatorias.
   - Ambos en `/RAUL/04-system/01-config/`.

4. **Actualizar `CLAUDE_core.md`** para incluir el patrón de carga:
   - "Si la tarea es de Genteca, carga también `CLAUDE_genteca.md` + `CONTEXT_genteca.md`".
   - Regla análoga para dominios futuros.

5. **Validar con sesiones reales:**
   - Ejecutar 3-5 tareas de Genteca bajo el nuevo patrón de carga.
   - Medir si el output es igual o mejor con core + dominio que con CLAUDE.md/CONTEXT.md completos.
   - Si OK, proceder con siguientes dominios en orden: `plenus-metabolica`, `teca-teak4food`, `marca-personal-raoul`.

6. Commit: "Fase 6 — contexto core + piloto Genteca".

**Validación:**
- `CLAUDE_core.md` < 2k tokens, `CONTEXT_core.md` < 500 tokens.
- Par Genteca (CLAUDE + CONTEXT) cubre una tarea real sin necesidad de cargar los docs largos originales.
- Primera decisión de calidad documentada en `DECISIONS.md`.

**Rollback:** los archivos core son aditivos; no reemplazan a los originales. Si no funcionan, se ignoran y se siguen usando los largos.

**Riesgo:** bajo (solo aditivo). El costo es el tiempo de destilación y el diseño del piloto.

---

## 7. Resumen de fases

| Fase | Día | Riesgo | Rollback | Archivos tocados |
|---|---|---|---|---|
| 1. Skeleton paralelo | 1 (medio día) | Bajo | Borrar `/RAUL/` | Ninguno del estado previo |
| 2. Migrar system | 2 | Medio | Borrar 2 carpetas | `04-system/` + `.claude/` creados; previo intacto |
| 3. Migrar knowledge + projects | 3 | Alto | Estado previo aún intacto hasta cierre | Movimiento masivo de KB + Assets + PROJECTS/Genteca |
| 4. Inbox + Drive + InboxBot | 4 (3-4h bloque) | Alto | Complejo | Trigger, Drive config, archivo final del estado previo |
| 5. Post-cleanup | 5 | Bajo | N/A | Indexes + decisions |
| 6. Contexto core + piloto (futura) | TBD | Bajo | Solo aditivo | Core + dominio Genteca |

**Total estimado para fases 1-5:** ~4 días hábiles distribuibles. Fase 4 requiere bloque continuo. Fase 6 es disparable a voluntad del Owner tras estabilización.

---

Fin de MIGRATION-PLAN.md v1.0
