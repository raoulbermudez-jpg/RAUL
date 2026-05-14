# Guía de carpetas RAUL — qué es cada una y cómo se usa

**Versión:** 1.1
**Fecha:** 2026-05-14 (v1.1 — añadidos `00-cola/` y `_ESTADO.md` tras el rediseño de InboxBot a capture-only; ver `OPERATIVA-REMOTA-Y-COLABORADORES.md` v2.0)
**Propósito:** mapa único de todas las carpetas con "Raul" en el sistema, qué hace cada una, cuál tocas tú vs. cuál es del runtime, y dónde vive cada tipo de archivo (raw, curado, KB, portafolio Genteca).

Lectura recomendada cuando dudes "¿dónde está X?" o "¿puedo borrar esto?".

---

## Parte 1 — Mapa de carpetas con "Raul" (todas)

### A. Carpetas vivas que SÍ tocas tú

| Carpeta | Función | Cuándo la tocas |
|---|---|---|
| `C:\RAUL\` | **Repo maestro local.** Aquí vive todo el contenido del sistema /RAUL/: agentes, KB, projects, governance, scripts, conceptual SSOT, configuración. | Edición directa cuando trabajas en sesión Claude Code. Versionado con git. |
| `G:\Mi unidad\RAUL\01-inbox\` | **Canal cloud Owner ↔ InboxBot.** Lo que dejas/recibes desde el celular. | Subes tareas a `01-owner-to-raul/`, lees entregables de `02-deliverables-to-owner/` desde la app Drive móvil. |
| `G:\Mi unidad\RAUL\colaboradores\` | **Punto de intercambio cloud con colaboradores externos.** Cada colaborador tiene su propia carpeta con `01_De_X_Para_Raoul/` + `02_De_Raoul_Para_X/` + `03_Archivo/`. | Cuando depositas archivos para un colaborador (en su `02_De_Raoul_Para_X/`) o revisas lo que él te envió (en su `01_De_X_Para_Raoul/`). |
| `G:\Mi unidad\RAUL-Exchange\Panama\` | **Dominio personal Panama (apt Embassy Club).** Sin colaboradores. | Estructura temática: Analisis-Mercado, Contratos, EmbassyClub, Finanzas, Reparaciones. Activación RAUL pendiente. |

### B. Carpetas vivas que NO tocas (sistema automático las maneja)

| Carpeta | Función | Por qué no tocarla |
|---|---|---|
| `C:\Users\User\.claude\projects\C--Raul\` | **Runtime de Claude Code.** Memoria persistente (`memory/`) + transcripts JSONL de sesiones + outputs de subagentes. | Claude Code la busca en esa ruta exacta. Tocarla rompe la herramienta, pierde memoria entre sesiones. |
| `C:\Users\User\OneDrive\RAUL-backup\` | **Backup nightly automático del KB.** Mirror del `02-knowledge-base/` con historial 30 días vía OneDrive. | El cron `RAUL_KB_Backup_OneDrive` corre cada noche a 23:00. Si tocas algo, el próximo cron lo sobreescribe igual. |

### C. Carpetas archivadas el 2026-05-04 (legacy → cuarentena)

| Carpeta | Estado | Eliminación |
|---|---|---|
| `C:\_ARCHIVED_2026-05-04\` | Cuarentena temporal de 4 carpetas legacy (WorkspaceIA, Mi unidad cueva, OneDrive viejo, Arrancar Claude) | Eliminar manualmente después de 30-60 días sin echar de menos nada. README dentro del archive documenta cada subcarpeta. |
| `C:\WorkspaceIA\` | Predecesor del repo /RAUL/ — contenido ya copiado al archive | Eliminar manualmente cuando confirmes (algunos archivos estaban en uso al momento del archivado). |
| `G:\Mi unidad\WorkspaceIA\` y `G:\Mi unidad\WorkspaceIA Backup\` | Espejos legacy en Drive — contenido copiado | Eliminar desde Drive Desktop o Drive web. |
| `C:\Users\User\Mi unidad\RAUL\` | Cueva de Backup & Sync (descontinuada) | Eliminar la subcarpeta `RAUL/` (no la `Mi unidad/` entera, que tiene otras carpetas vivas no-RAUL). |
| `C:\Users\User\OneDrive\RAUL\` | Canal OneDrive descontinuado | Eliminar tras confirmar que el paquete v1 que vivía solo aquí ya está copiado a `G:\Mi unidad\RAUL\01-inbox\02-deliverables-to-owner\`. |

### D. Carpetas con nombre "Raul" pero NO relacionadas con el sistema

| Carpeta | Por qué tiene "Raul" | Acción |
|---|---|---|
| `C:\Users\User\OneDrive\Desktop\Personal dic 2022\Raul De Cardenas\` | Carpeta personal con nombre de **otra persona** (Raúl De Cárdenas). Contiene 1 ficha de producto Opcenter APS de jul-2025. | No tocar. No es del sistema /RAUL/. |

---

## Parte 2 — Cosas que tocas tú: instructivo detallado

### 2.1 Cuándo y cómo usar `C:\RAUL\` (repo maestro)

**Cuándo:** durante sesiones interactivas de Claude Code, cuando trabajas localmente en el PC.

**Estructura interna principal:**

```
C:\RAUL\
├── 01-inbox\                       ← lo que entra crudo (raw + briefs sin procesar)
│   ├── 01-owner-to-raul\           ← (legacy local — el canal vivo es G:)
│   ├── 02-deliverables-to-owner\   ← (legacy local)
│   └── 03-raw-sources\             ← RAW del Owner / colaboradores / pendrive antes de curar
├── 02-knowledge-base\              ← KB curado (output de Celeste/Sira)
│   ├── 00-raul-intelligence\       ← wiki del Owner (estilo, voz, preferencias, metodología)
│   ├── 01-foundations\             ← fundamentos genéricos (cross-domain)
│   ├── 02-domains\                 ← dominios (genteca, plenus-metabolica, ...)
│   │   └── 01-genteca\             ← portafolio Genteca (specs + wiki + assets)
│   ├── 03-cross-cutting\           ← temas transversales (ai-systems framework, etc.)
│   ├── 04-sops-and-playbooks\      ← playbooks operativos
│   └── 05-glossary-and-tables\     ← glosario
├── 03-projects\                    ← proyectos activos por dominio
│   └── genteca\                    ← (e.g., 2026-04_GSM-MB-RB-RF_empaque)
├── 04-system\                      ← gobierno + tools + indexes
│   ├── 01-config\                  ← CLAUDE.md, CONTEXT, FOLDER-ARCHITECTURE
│   ├── 02-agents\                  ← roster + conceptual + ROUTING-GUIDE
│   ├── 03-governance\              ← DECISIONS, RISK-POLICY, runbooks
│   ├── 04-tools-and-scripts\       ← scripts (incl. backup_kb_to_onedrive.ps1)
│   └── 05-indexes\                 ← índices Sira (kb-index, projects-index, etc.)
└── .claude\agents\                 ← thin-adapters / AGENT.md de cada agente
```

**Reglas operativas:**
- Editas `.md` libremente, son la fuente de verdad.
- No editas archivos generados por scripts (logs, reports), se regeneran.
- Commits de git: bajo tu criterio o cuando una sesión cierra hito mayor.

### 2.2 Cuándo y cómo usar `G:\Mi unidad\RAUL\01-inbox\`

**Cuándo:** estás fuera del PC (en el celular / tablet / otro PC) y necesitas:
- Pedirle al sistema /RAUL/ que produzca algo.
- Recibir un entregable del sistema.

**Cómo (resumen, detalle completo en `OPERATIVA-REMOTA-Y-COLABORADORES.md`):**

| Acción | Carpeta | Notas |
|---|---|---|
| Dejar tarea desde celular | `RAUL/01-inbox/01-owner-to-raul/` | Cualquier formato sirve para la captura; InboxBot solo registra nombre y tipo |
| Consultar el estado de todo | `RAUL/01-inbox/_ESTADO.md` | **Un solo archivo** — cola del Owner, actividad de colaboradores, flags. Lo regenera InboxBot cada ciclo |
| Recibir entregables | `RAUL/01-inbox/02-deliverables-to-owner/` | Lo que Raul-desktop produzca (`.md`, `.pdf`, `.pptx`, `.svg`) |
| (Interno) Cola de trabajo | `RAUL/01-inbox/00-cola/` | InboxBot deja un `TICKET_*.md` por ítem; Raul-desktop los consume. No necesitas abrirla — el `_ESTADO.md` la resume |

**Modelo capture-only (desde el rediseño v5.0 de InboxBot, 2026-05-14):** lo
que dejas remotamente queda **encolado, no procesado**. InboxBot captura,
encola y notifica; el trabajo real lo hace Raul cuando abres una sesión
desktop. Los canales de gobernanza (`04-decisions-in-flight/`,
`05-from-junta/`, etc.) **no son parte del modelo remoto** — son
desktop/repo.

**Frecuencia InboxBot:** cada 2 h en ventana 6:00–23:00 Caracas (10
disparos diarios). Configurable en Routines de Claude Code Desktop.

### 2.3 Cuándo y cómo usar `G:\Mi unidad\RAUL\colaboradores\` (y `RAUL-Exchange\Panama\`)

**Cuándo:** intercambio de archivos con colaboradores externos (Genteca, Academicos) + acceso al dominio personal Panama.

**Estructura post-cleanup 2026-05-09:**

```
G:\Mi unidad\RAUL\colaboradores\          ← colaboradores con flujo bidireccional
├── Genteca/
│   ├── Oswaldo/
│   │   ├── 01_De_Oswaldo_Para_Raoul/    ← Oz te envía cosas
│   │   ├── 02_De_Raoul_Para_Oswaldo/    ← tú le dejas cosas
│   │   └── 03_Archivo/                  ← procesados (InboxBot mueve aquí)
│   ├── Cora-Urrea/         (misma estructura 01/02/03)
│   ├── Liliam-Ramirez/
│   ├── Ana-Mendez/
│   ├── Valeria-Ostos/
│   ├── Rhinoska-Celis/
│   ├── Julio-Heredia/
│   └── _memoria-tareas-pendientes/      ← carpeta especial (prefijo `_`, NO colaborador, InboxBot la ignora)
└── Academicos/
    └── Daniel-Rubio/

G:\Mi unidad\RAUL-Exchange\               ← legacy, mantenido solo para Panama
└── Panama/                               ← dominio personal (sin colaboradores)
    ├── Analisis-Mercado/
    ├── Contratos/
    ├── EmbassyClub/
    ├── Finanzas/
    └── Reparaciones/
```

**Convención por carpeta de colaborador (perspectiva Owner):**
- **`01_De_<colab>_Para_Raoul/`** = lo que el colaborador te deja a ti (tu inbox para él).
- **`02_De_Raoul_Para_<colab>/`** = lo que tú le dejas a él (su inbox).
- **`03_Archivo/`** = histórico de archivos ya procesados (InboxBot mueve fuentes aquí post-procesamiento).

**Naming asimétrico:** la carpeta padre del colaborador puede ser `<Nombre-Apellido>` (ej. `Cora-Urrea/`) mientras el subfolder usa solo `<Nombre>` (ej. `01_De_Cora_Para_Raoul/`). InboxBot deriva el shortname del subfolder.

**Cómo InboxBot trata los canales de colaborador:** escanea todos los `01_De_X_Para_Raoul/` igual que el inbox del Owner. Cuando un colaborador deja un archivo, InboxBot lo **captura** como ticket (`fuente: colaborador:<nombre>`) y lo refleja en la sección "Actividad de colaboradores" del `_ESTADO.md`. **No procesa, no escribe en `02_De_Raoul_Para_X/`, no infiere dominio.** El procesamiento y la respuesta los hace Raul en sesión desktop.

**Reglas:**
- Cada colaborador ve **solo su carpeta personal** (sharing individual desde Drive web).
- No mezclar dominios (Genteca vs Panamá) en una misma persona.
- Para onboardear nuevo colaborador: `OPERATIVA-REMOTA-Y-COLABORADORES.md §2.3-2.5`.

---

## Parte 3 — Tipos de archivo y dónde vive cada uno

### 3.1 Archivos RAW (sin curar)

**Ubicación:** `C:\RAUL\01-inbox\03-raw-sources\`

**Qué son:** todo lo que entra al sistema sin haber sido procesado todavía. Incluye briefs del Owner, transcripciones de reunión crudas, hojas técnicas de I&D, fotos del pendrive, archivos de colaboradores, presentaciones recibidas.

**Subcarpetas activas hoy:**

```
03-raw-sources\
└── genteca\
    ├── 2026-04-19\               ← presentación Junta Directiva V3 (input inicial)
    ├── gsm-labels\               ← raw labels GSM
    ├── gst-labels\               ← raw labels GST (etq-originales, redlines, etc.)
    ├── marcas\                   ← raw de tema marcas
    ├── ntc-gsm-hojas-glase\      ← raw hojas técnicas GSM
    └── pendrive-D\               ← extracción del pendrive físico
```

**Quién lo procesa:** Celeste decide qué entra a KB; Sira indexa para reciclaje. Después de procesar, la versión curada vive en `02-knowledge-base/` y el raw se mantiene como referencia histórica.

**Política:** no editar archivos raw. Si un raw tiene un error, se duplica corregido en otra carpeta — el original queda como evidencia de fuente.

### 3.2 Archivos CURADOS (en KB)

**Ubicación:** `C:\RAUL\02-knowledge-base\02-domains\01-genteca\` (para Genteca; cada dominio tiene su rama)

**Qué son:** versiones limpias, estructuradas, con metadata, listas para que los agentes las consulten. Salen del trabajo de Celeste (selección) + Sira (indexado).

**Estructura del KB Genteca:**

```
02-knowledge-base\02-domains\01-genteca\
├── _index.md                     ← índice del dominio (siempre cargado)
├── specs\                        ← 193 archivos: hojas técnicas + catálogos + comparativas
├── wiki\
│   ├── brand\                    ← brand kit Exceline, identidad
│   └── market\                   ← contexto de mercado venezolano
└── assets\
    ├── diagrams\                 ← diagramas técnicos
    ├── packaging\                ← arte de empaque (visuales)
    ├── products\                 ← imágenes de producto
    ├── uncoded\                  ← legacy / sin código asignado
    ├── logo-exceline.png
    ├── logo-exceline-40-aniversario.png
    └── logo-genius.png
```

**Cómo agregar algo al KB:**
1. Tú dejas el raw en `01-inbox/03-raw-sources/`.
2. Le pides a Celeste que evalúe si vale la pena promover a KB.
3. Si aprueba, Sira lo indexa y le da nombre canónico (`YYYY-MM-DD_tema_v1.md`).
4. El curado queda en la rama correspondiente (`specs/`, `wiki/brand/`, `wiki/market/`, `assets/`).
5. Sira actualiza los índices en `04-system/05-indexes/`.

### 3.3 Portafolio detalles técnicos Genteca (lo que preguntaste)

**Ubicación:** `C:\RAUL\02-knowledge-base\02-domains\01-genteca\specs\`

**Inventario:** 193 archivos `.md` con detalles de todo el portafolio Exceline.

**Qué encuentras ahí:**
- Catálogos comerciales (`2026-04-17_catalogo-comercial_exceline-todos-productos.md`).
- Catálogos por línea (Profesional Breakers, Profesional Control y Distribución, Profesional Protección Trifásica).
- Hojas técnicas individuales por modelo (GSM-MB, GSM-RB, GSM-RF, GSM-RE, GST-RT, GST-RD, GST-RM, GST-RR, GIII-MV, etc.).
- Comparativas vs competencia (TQ, Powest, Avtek, WellSpec, Breakermatic, etc.).
- Curvas IDMT, trip classes, parámetros eléctricos.

**Cómo navegar:**
- Empezar por `_index.md` del dominio Genteca (siempre cargado).
- Para búsquedas específicas: índices Sira en `04-system/05-indexes/kb-index-by-domain.md`.
- Para encontrar hoja de un modelo específico: filename siempre contiene el modelo (ej. buscar `GSM-RE`).

**HDE (hojas de especificación) sin actualizar con cambios recientes:**
- Las HDE actuales reflejan los modelos previos (sin NTC, sin < 30 ms).
- Las versiones nuevas con innovaciones se actualizan cuando I&D emita las HDE actualizadas (pendiente operativo registrado).

### 3.4 Índices y catálogos (output de Sira)

**Ubicación:** `C:\RAUL\04-system\05-indexes\`

**Contenido relevante:**

| Archivo | Para qué |
|---|---|
| `kb-index-by-domain.md` | Mapa completo del KB por dominio (Genteca, Plenus, etc.) |
| `domains-index.md` | Índice de dominios activos |
| `projects-index.md` | Proyectos activos por dominio |
| `research-index.md` | Investigaciones de Paxs |
| `companion-docs-index.md` | Documentos compañeros (PERPLEXITY, etc.) |
| `pendrive_D_*` | Logs y reportes de procesamiento del pendrive físico (cuando se conecta D:) |
| `fase4_*.log` | Logs de la migración Fase 4 (histórico) |

---

## Parte 4 — Reglas de oro para evitar confusión

### 4.1 Regla 1: el contenido de trabajo SOLO vive en `C:\RAUL\`

Todo lo demás es **canal, runtime, backup o legacy**. Si trabajas con un archivo y no estás en `C:\RAUL\`, te estás equivocando de ubicación.

### 4.2 Regla 2: Drive es para movilidad y colaboración

`G:\Mi unidad\RAUL\` (incluye `colaboradores/`) y `G:\Mi unidad\RAUL-Exchange\Panama\` solo existen para que tú (desde celular) o colaboradores (desde sus PCs) puedan dejar/recibir cosas. **No es lugar de trabajo.**

### 4.3 Regla 3: OneDrive solo es respaldo

`OneDrive\RAUL-backup\` es backup automático del KB. **No edites ahí.** Tu próxima edición se sobrescribe en el siguiente cron.

### 4.4 Regla 4: rutas que NO existen como canal del sistema

Estas rutas NO se usan, aunque existan físicamente:
- `C:\Users\User\Mi unidad\RAUL\` → **cueva legacy Backup & Sync.** No sincroniza con la nube.
- `C:\Users\User\OneDrive\RAUL\` → archivada hoy. OneDrive no es canal de InboxBot.

Si AGENT.md o un Routine apunta ahí, **lo rechaza automáticamente** desde v3.2.

### 4.5 Regla 5: cuando dudes dónde guardar algo

| Tipo de archivo | Carpeta correcta |
|---|---|
| Brief / tarea para el sistema | `G:\Mi unidad\RAUL\01-inbox\01-owner-to-raul\` (desde celular) o trabajar directamente en sesión Claude Code (desde PC) |
| Archivo crudo recibido (PDF, transcripción, datasheet) | `C:\RAUL\01-inbox\03-raw-sources\genteca\` (o el subdominio que corresponda) |
| Archivo curado y validado | `C:\RAUL\02-knowledge-base\02-domains\01-genteca\specs\` (o `wiki/`, `assets/` según tipo) |
| Trabajo en proyecto activo | `C:\RAUL\03-projects\<dominio>\<período>_<código>_<tema>\` |
| Decisión / política / runbook | `C:\RAUL\04-system\03-governance\` |
| Para colaborador externo | `G:\Mi unidad\RAUL\colaboradores\<dominio>\<persona>\02_De_Raoul_Para_<persona>\` |

---

## Parte 5 — FAQ rápida

**P: ¿Dónde está la KB?**
R: `C:\RAUL\02-knowledge-base\`. Backup en `OneDrive\RAUL-backup\`.

**P: ¿Dónde están los detalles técnicos del portafolio Genteca?**
R: `C:\RAUL\02-knowledge-base\02-domains\01-genteca\specs\` — 193 archivos.

**P: ¿Dónde están los archivos crudos antes de curar?**
R: `C:\RAUL\01-inbox\03-raw-sources\genteca\` — separados por tema (gsm-labels, gst-labels, etc.).

**P: ¿Quién cura los raw?**
R: Celeste decide qué entra a KB; Sira indexa y nombra. Tú apruebas mover si están de acuerdo.

**P: Si subo algo desde el celular, ¿dónde llega?**
R: Si lo subiste a `Mi unidad/RAUL/01-inbox/01-owner-to-raul/` → InboxBot lo **captura y encola** en el próximo ciclo (máx ~2 h): crea un ticket en `00-cola/` y lo refleja en `_ESTADO.md`. Queda **encolado, no procesado** — el trabajo real lo hace Raul cuando abres una sesión desktop.

**P: ¿Dónde veo el estado de lo que dejé?**
R: `Mi unidad/RAUL/01-inbox/_ESTADO.md` — un solo archivo, regenerado por InboxBot cada ciclo, con la cola del Owner, la actividad de colaboradores y flags de higiene.

**P: ¿Puedo borrar `OneDrive\RAUL-backup\`?**
R: No. Es backup nightly del KB con 30 días de historial. Si tu disco falla, lo necesitas.

**P: ¿Puedo borrar `C:\Users\User\.claude\projects\C--Raul\`?**
R: No. Es runtime de Claude Code, contiene memoria persistente y transcripts. Borrarlo rompe Claude Code.

**P: ¿Y `C:\WorkspaceIA\`?**
R: Sí, ya lo archivaste hoy en `C:\_ARCHIVED_2026-05-04\`. Eliminar el original cuando confirmes que no necesitas nada después de 30-60 días.

**P: ¿`Raul De Cardenas` en OneDrive?**
R: No tocar. Es de otra persona, no del sistema.

---

*Mantenido en `C:\RAUL\04-system\03-governance\GUIA-CARPETAS-RAUL.md`. Actualizar si emergen nuevas carpetas o se reorganiza la estructura.*
