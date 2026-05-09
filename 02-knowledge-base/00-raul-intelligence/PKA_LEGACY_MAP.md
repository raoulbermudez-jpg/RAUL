# PKA_LEGACY_MAP — Índice maestro de contenido /RAUL/ disperso

**Versión:** v0.2
**Última actualización:** 2026-05-07
**Tipo:** índice operativo vivo
**Audiencia:** privada (paths con info personal y de colaboradores)

---

## 0. Cómo se usa este documento

Punto de entrada para localizar cualquier contenido relacionado con /RAUL/, PKA, agentes IA, KB o dominios que viva FUERA del repo activo `C:\RAUL\`. Se actualiza cuando se rescata, mueve, archiva o crea una ubicación nueva.

**Origen:** sesión 2026-05-07. El Owner preguntó por trabajo legacy del coach/clon que recordaba haber hecho. Excavación reveló que el blueprint existe (Hoja de Ruta + research Paxs) pero el agente nunca se construyó, y reveló también múltiples ubicaciones dispersas con contenido valioso. Este mapa se crea para que el sistema no vuelva a perder rastro de su propio pasado.

**Documento fuente complementario:** `2026-05-04_GUIA-CARPETAS-RAUL.md` (Google Drive, 16 KB) — guía oficial del Owner sobre la estructura del repo activo. Este mapa NO la duplica: la referencia como SSOT para la estructura interna y se enfoca en lo que la guía no cubre (legacy disperso, contenido externo, ubicaciones a depurar).

---

## 1. UBICACIONES CANÓNICAS VIVAS (SSOT)

| Ubicación | Rol | Notas |
|---|---|---|
| `C:\RAUL\` | Repo activo maestro (~5,059 files, 281 carpetas). SSOT versionado en git. | Punto de operación diaria. |
| `G:\Mi unidad\RAUL\` | Canal cloud Owner ↔ InboxBot. | 01-inbox vivo (~75 files). Bajo gestión InboxBot. |
| `G:\Mi unidad\RAUL\colaboradores\` | Canal Drive con colaboradores externos por dominio (Genteca, Academicos). Migrado 2026-05-09 desde `RAUL-Exchange/`. | Estructura `<dominio>/<nombre>/01_De_X_Para_Raoul/`, `02_De_Raoul_Para_X/`, `03_Archivo/`. IDs en `reference_drive_exchange_ids.md` (parcialmente stale, actualizar). |
| `G:\Mi unidad\RAUL-Exchange\Panama\` | Dominio Panama (apt Embassy Club). Activación RAUL pendiente. | Estructura temática (sin colaboradores). |
| `C:\Users\User\OneDrive\RAUL-backup\` | Espejo nightly del KB. Recovery 30d. | Cron `RAUL_KB_Backup_OneDrive` 23:00 robocopy /MIR. |

---

## 2. DOCUMENTOS METODOLÓGICOS DE REFERENCIA

Documentos que sostienen el diseño del sistema. Algunos viven duplicados en repo + Google Drive — el repo es SSOT.

| Documento | Ubicación primaria | Estado |
|---|---|---|
| `Hoja_De_Ruta_Raul.md` v0.3 | `02-knowledge-base/00-raul-intelligence/methodology/` | Vivo. Norte estratégico. |
| `Apéndice_A_Notas_Privadas.md` v0.1 | `02-knowledge-base/00-raul-intelligence/methodology/_private/` (gitignored) | Vivo. Detalles sensibles. |
| `2026-05-04_GUIA-CARPETAS-RAUL.md` | Google Drive (ID `19dcmN_D3O2bCBpXW2Sn_oHcfwLG8M9w6`) | Guía oficial Owner. Verificar si está en repo. |
| `ARCHITECTURE_Content-Supply-Chain.md` | `04-system/02-agents/content-supply-chain/` (repo) + Google Drive | Vivo. v1.0. |
| `AGENTS_Content-Supply-Chain.md` | `04-system/02-agents/content-supply-chain/` (repo) + Google Drive | Vivo. Fichas 9 agentes CSC. |
| `CLAUDE.md` | Raíz repo + Google Drive | Vivo. Entry point Claude Code. |
| `CLAUDE_core.md` | Raíz repo | Versión vendor-neutral compacta. |
| `_taxonomy.md` (6 clases agentes) | `04-system/02-agents/` | Lock 2026-05-01. |
| `DECISIONS.md` | `04-system/03-governance/` | Vivo. Log de decisiones arquitectónicas. |
| `RISK-POLICY.md` | `04-system/03-governance/` | Vivo. Política de riesgo y revisión humana. |
| `LLM-GUIDELINES.md` | `04-system/03-governance/` | Vivo. Reglas multi-LLM. |
| `FOLDER-ARCHITECTURE.md` v2.1 | `04-system/01-config/` | Vivo. Arquitectura de carpetas. |

---

## 3. RESEARCH ACTIVABLE (insumo para fases futuras)

Material de investigación que NO está en uso operativo pero queda preservado para fases posteriores del roadmap.

| Documento | Ubicación | Activable cuando |
|---|---|---|
| `2026-05-04_paxs_ai-coach-cloning.md` | `02-knowledge-base/00-raul-intelligence/methodology/_private/research/` | F5 estable 3+ meses → diseñar agente Espejo (F6.1). |
| `RECURSO--ICOR-Tom--Fuentes-Didacticas-PKA-con-IA--Ene-Abr-2026.md` | Google Drive (ID `1m0oM5yCJzqip_EQSN17vJ70YOn5p5cKD`) | Cuando se profundice metodología PKA o se haga staging para NotebookLM. |

---

## 4. UBICACIONES LEGACY ARCHIVADAS

| Ubicación | Estado | Acción recomendada |
|---|---|---|
| `C:\_ARCHIVED_2026-05-04\` | Cuarentena pre-migración. Contiene `from_C_drive/WorkspaceIA/`, `from_OneDrive/RAUL/`, `from_G_drive/WorkspaceIA Backup/`. | Eliminar después de 2026-07-04 si no hay reclamaciones. |
| `C:\Users\User\OneDrive\RAUL\` | Canal OneDrive descontinuado por DECISIONS.md 2026-05-01. Vivo solo por compatibilidad. | Migrar restos a `G:\Mi unidad\RAUL\` y eliminar. |
| `C:\Users\User\OneDrive\Microsoft Copilot Chat Files\` | Chatlogs Copilot. | Bajo valor. Eliminar si no hay info recuperable. |

---

## 5. CONTENIDO POR DOMINIO

### 5.1 Genteca

| Ubicación | Tipo | Estado |
|---|---|---|
| `C:\RAUL\03-projects\genteca\` | Proyectos activos (GME, GST, GSM, etc.) | Vivo. SSOT. |
| `C:\RAUL\02-knowledge-base\02-domains\01-genteca\` | KB activa Genteca | Vivo. |
| `D:\01. Exceline\` | Product DB Exceline (~30.9 GB, 5,259 files) | Externo. NO copiar. Fuente para Vera/Orlan. |
| `D:\02. Exceline-Profesional\` | Product DB Exceline Pro (~14.6 GB, 5,744 files) | Externo. NO copiar. |
| `D:\03. Genius\` | Product DB Genius (~3.6 GB, 1,618 files) | Externo. NO copiar. Tiene "OJO REVISAR Y DEPURAR". |
| `G:\Mi unidad\RAUL\colaboradores\Genteca\` | Carpetas por colaborador (Ana-Mendez, Cora-Urrea, Julio-Heredia, Liliam-Ramirez, Oswaldo, Rhinoska-Celis, Valeria-Ostos) + `_memoria-tareas-pendientes/` (carpeta especial, no colaborador) | Vivo. Canal externo. Migrado 2026-05-09 desde `RAUL-Exchange/Genteca/`. |
| `G:\Mi unidad\WorkspaceIA Backup\Genteca\` | KB legacy archivada (01_Biblioteca_Tecnica, 02_ProtMotores_Atlas, 03_Productos_Exceline, 04_Compartidos_Equipo, 05_Guiones_Video) | Legacy. Auditar y rescatar lo valioso → `02-domains/01-genteca/`. |

### 5.2 Plenus (metabólica)

| Ubicación | Tipo | Estado |
|---|---|---|
| `C:\RAUL\02-knowledge-base\02-domains\02-plenus-metabolica\` | KB stub | Sin contenido sustancial. |
| `C:\RAUL\03-projects\plenus\Presentación final Raoul - QTorta.pptx` (114 MB) | Presentación QTorta yogurt (fecha original 2023-06-15) | Rescatado 2026-05-07 desde OneDrive raíz. Gitignored por `*.pptx`. |
| `C:\RAUL\03-projects\plenus\Plenus.pptx` (5.5 MB) | Presentación Plenus (fecha original 2024-11-19) | Rescatado 2026-05-07 desde OneDrive raíz. Gitignored por `*.pptx`. |
| `G:\Mi unidad\WorkspaceIA Backup\Plenus\` | KB legacy | Legacy. Auditar. |

### 5.3 Finca (ganadería)

| Ubicación | Tipo | Estado |
|---|---|---|
| `C:\RAUL\02-knowledge-base\02-domains\03-finca-ganaderia\` | KB stub | Sin contenido sustancial. |
| `G:\Mi unidad\01 - Ganadería y Finca\` | Operaciones activas (Cogoyal, Genética, Papelón, Producción, Sanidad, Congreso) | Vivo. Activación RAUL pendiente. |
| `G:\Mi unidad\WorkspaceIA Backup\Finca\` | KB legacy | Legacy. Auditar. |
| `C:\Users\User\OneDrive\Calculo de volumen por rola o arbol al 20 3 2017.xlsx` | Cálculos forestales antiguos | Archivar si vale, ignorar si no. |

### 5.4 Teca / Teak4Food

| Ubicación | Tipo | Estado |
|---|---|---|
| `C:\RAUL\02-knowledge-base\02-domains\04-teca-teak4food\` | KB stub | Sin contenido sustancial. |
| `G:\Mi unidad\02 - Negocios y Proyectos\Teak4food\` | Operaciones activas | Vivo. Activación RAUL pendiente. |
| `C:\Users\User\OneDrive\Teak4food Movie.mov` (151 MB) | Video Teak4Food | Archivar a media o eliminar. |
| `G:\Mi unidad\WorkspaceIA Backup\Teak4Food\` | KB legacy | Legacy. Auditar. |

### 5.5 Panamá

| Ubicación | Tipo | Estado |
|---|---|---|
| `C:\RAUL\02-knowledge-base\02-domains\` (sin carpeta dedicada todavía) | — | Activación RAUL pendiente. |
| `G:\Mi unidad\RAUL-Exchange\Panama\` | Análisis mercado, Contratos, EmbassyClub, Finanzas, Reparaciones | Vivo. Drive creado 2026-05-01. |

### 5.6 Marca personal Raoul

| Ubicación | Tipo | Estado |
|---|---|---|
| `C:\RAUL\02-knowledge-base\02-domains\05-marca-personal-raoul\` | KB stub | Sin contenido localizado todavía. **FALTANTE.** |

---

## 6. CONTENIDO PERSONAL (NO-PKA, no migrar)

Documentado para que el sistema no lo trate como huérfano.

- `C:\Users\User\OneDrive\Seguros Vida\` — pólizas Pan-American Life.
- `G:\Mi unidad\03 - Finanzas Personales\` — finanzas privadas.
- `G:\Mi unidad\04 - Documentos Legales\` — documentos legales.
- `G:\Mi unidad\05 - Personal y Familia\` — fotos / familia.
- `G:\Mi unidad\06 - Educación y Cultura\` — material educativo.
- `C:\Users\User\OneDrive\Pictures\` — screenshots / Camera Roll.

---

## 7. INBOX-LEGACY POR PROCESAR

Ubicaciones con contenido sin clasificar que conviene revisar y archivar/eliminar.

- `G:\Mi unidad\_Para Revisar\` — ~20 docs Google sin título / sin destino.
- `C:\Users\User\OneDrive\` raíz — varios `.pptx`/`.xlsx` sueltos (Innovación pizarra sala.pptx, Book.xlsx, Horas exceline.xlsx).
- `C:\Users\User\OneDrive\Attachments\` — adjuntos integrados.

---

## 8. CONTENIDO A ELIMINAR / CONSOLIDAR

Marcado para depuración con fecha-objetivo.

| Ubicación | Acción | Fecha |
|---|---|---|
| `C:\_ARCHIVED_2026-05-04\` | Eliminar si no hay reclamaciones | Después 2026-07-04 |
| `C:\Users\User\OneDrive\RAUL\` | Migrar a G: y eliminar | Cuando se confirme migración |
| `G:\Mi unidad\WorkspaceIA Backup\` | Eliminar después de archivar valioso a `C:\RAUL\` | Después de auditoría |
| `G:\Mi unidad\07 - Tecnología e IA\` (Google AI Studio + Earth) | Ignorar (no PKA) | — |
| ~~`OneDrive\Desktop\One Drive Windows Escritorio\Frussion\Presentación final Raoul - QTorta .pptx`~~ | Eliminado 2026-05-07 (duplicado del rescatado) | ✅ done |
| ~~`OneDrive\Desktop\Personal dic 2022\Finca\Yogurt\Cremades\Wallace\Plenus.pptx`~~ | Eliminado 2026-05-07 (duplicado del rescatado) | ✅ done |

---

## 9. ZONAS PENDIENTES DE EXPLORAR

Cosas que esta excavación NO cubrió completamente y conviene revisitar.

- Búsquedas Google Drive truncadas en sesión 2026-05-07 (queries pendientes: "brand", "templates", "teams", "knowledge").
- `C:\Users\User\Documents\` — verificar si existe o está vacío.
- Subcarpetas profundas de `D:\03. Genius\` (especialmente "OJO REVISAR Y DEPURAR" y "Productos Clientes").
- Carpetas no exploradas en G:\: 03 Finanzas Personales / 04 Legales / 05 Familia / 06 Educación / 08 Archivo (asumidas no-PKA pero sin verificación).

---

## 10. Changelog

### v0.2 — 2026-05-07

- Plenus rescatado: `Presentación final Raoul - QTorta.pptx` (114 MB) y `Plenus.pptx` (5.5 MB) movidos desde OneDrive raíz a `03-projects/plenus/`. Filename QTorta normalizado (eliminado espacio raro antes de `.pptx`). Ambos gitignored por `*.pptx`.
- Duplicados eliminados de OneDrive: copia QTorta en `Frussion\` y copia Plenus en `Personal dic 2022\Finca\Yogurt\Cremades\Wallace\` (verificadas idénticas en tamaño y fecha antes de eliminar).
- Sección 5.2 Plenus actualizada para reflejar nuevas rutas y fechas originales de los archivos.
- Sección 8 actualizada con registro de eliminaciones (tachado).

### v0.1 — 2026-05-07

- Versión inicial. Excavación arqueológica completa de C:/G:/D:/OneDrive + búsquedas online en Google Drive.
- Origen: sesión donde el Owner pidió rescatar trabajo legacy (coach personal, clon digital, bibliotecaria, LLM wiki sin DB) que recordaba haber diseñado.
- Hallazgo principal: F6 (Mirror Coach + Persona Delegation) está documentada en blueprint pero no construida. Decisión registrada en `DECISIONS.md` 2026-05-07: F6 diferida hasta F5 estable 3+ meses.
- Material legacy más valioso identificado: `2026-05-04_paxs_ai-coach-cloning.md` (preservado), `Hoja_De_Ruta_Raul.md` v0.3 (vivo), `2026-05-04_GUIA-CARPETAS-RAUL.md` (Google Drive).
