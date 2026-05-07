# Incidente — InboxBot remoto no procesó tarea del Owner

**Fecha:** 2026-05-07
**Tipo:** Falla operativa de rutina automática (no crítica — recuperada manualmente)
**Severidad:** Media (cadena CSC ejecutó manualmente sin pérdida de calidad, pero la rutina remota no cumplió su función)
**Estado:** Diagnosticado. Acciones de remediación pendientes de Owner.

---

## Resumen ejecutivo

El Owner colocó una tarea (`tarea sobre GSM-R y marcas de tecnologías a partir de anglicismos aceptables en Venezuela.gdoc`) en el inbox de Drive a las **07:36 hora Caracas**. La rutina remota `raul-inboxbot` (cron `0 0,2,3,10,12,14,16,18,20,22 * * *`, trigger ID `trig_01RgGGbpCvckUzSwkyGMDNtm`) tenía disparos programados a las **08:00 y 10:00 am Caracas** posteriores a la creación. Ninguno procesó la tarea: no hay DONE marker, no hay deliverable, no hay error en outbox.

La tarea se procesó manualmente en sesión local Claude Code el mismo día (cadena CSC completa Aurelio → Paxs ‖ Vera ‖ Orlan → Vael → Bruna → Nerea → Vivienne, deliverable entregado en outbox).

---

## Hallazgo raíz: duplicación estructural en Google Drive

Existen **DOS jerarquías paralelas** con el mismo nombre `01-inbox/01-owner-to-raul/` en el Drive personal del Owner:

### Jerarquía A — canónica (referenciada por path en `AGENT.md` v3.2)

```
RAUL (id: 124VdcO237NDXAowD0DZ0BoJVMiQNMKPG)
└── 01-inbox (id: 1unAvLLh2J52L6cX0HhAzR6WVUTKJg4k5)
    ├── 01-owner-to-raul (id: 1haWHQdhwwlrdcL-sS28K819CzAKdHevM)  ← CANÓNICA
    └── 02-deliverables-to-owner (id: 1fg_w_9HeYh9G88GMUox6W3lniMPe1Tf-)
```

### Jerarquía B — legacy / duplicada (debe eliminarse o renombrarse)

```
[parent desconocido — id: 1Yex3K9hQnPgaVQ1QRSiH8PClP9NJMKrc]
├── 01-owner-to-raul (id: 1OeBw7clLega1GDV7YtNo3tKpPOygqwz3)
├── 02-deliverables-to-owner (id: 1x6AHhN3MXLfBTLl1fbbsCKTFqEL2Sizg)
├── genteca
├── Downloads
└── WorkspaceIA
```

El parent `1Yex3K9hQnPgaVQ1QRSiH8PClP9NJMKrc` contiene también `Downloads` y `WorkspaceIA` — son trazas de estructura legacy (probablemente Drive Backup & Sync descontinuado) que sobrevivieron a la migración 2026-04 a Drive Desktop streaming.

### Evidencia

La búsqueda Drive del archivo del Owner devolvió **dos fileIds distintos** con el mismo título, cada uno bajo un parent distinto:

| fileId | parentId | Parent path | Creado (UTC) | Creado (Caracas) |
|---|---|---|---|---|
| `1zGD4MHB5_PgnDOXwZeAzLv1h0h_R4a3aJLCc7gnEgMg` | `1haWHQdhwwlrdcL-sS28K819CzAKdHevM` | Jerarquía A (canónica) | 11:36 | **07:36** |
| `1Mvv-9ndgnEfgVv4Uca3tB1A8-XyE4YyMKQvGt903Sgs` | `1OeBw7clLega1GDV7YtNo3tKpPOygqwz3` | Jerarquía B (legacy) | 12:50 | 08:50 |

El primer fileId (07:36) es la creación original desde móvil del Owner; el segundo (08:50) es una copia/duplicado que apareció ~75 min después por mecanismo desconocido (posiblemente sincronización cruzada de algún servicio legacy).

---

## Hipótesis sobre por qué la rutina no procesó

### Hipótesis 1 (más probable): InboxBot remoto apunta a la jerarquía B legacy

El AGENT.md v3.2 referencia el path `RAUL/01-inbox/01-owner-to-raul/` por nombre. Si el InboxBot remoto en cloud resuelve este path y elige la primera carpeta que encuentra con ese nombre — y por orden alfabético de fileId esa es la jerarquía B legacy — entonces escanea una carpeta donde la tarea no estaba al momento del primer disparo (08:00 Caracas). La tarea apareció en la jerarquía B 50 minutos después (08:50 Caracas).

A las **10:00 am Caracas** (segundo disparo programado), la tarea ya estaba en ambas jerarquías. Si el InboxBot procesó la jerarquía B y vio el archivo, debería haber generado DONE marker en esa carpeta. No lo hizo. Esto podría indicar que el InboxBot también falló en el segundo disparo por otra razón, o que apunta a un parentId hardcoded distinto de ambas.

### Hipótesis 2: bug silencioso en resolución de `.gdoc`

El AGENT.md v3.2 §3 dice que `.gdoc` requiere Drive MCP para extraer doc_id y leer contenido. Si el Drive MCP del entorno cloud falló al resolver el `.gdoc` — y el InboxBot no escribió error en outbox como el AGENT.md le instruye — quedó en estado de falla silenciosa.

### Hipótesis 3: race condition en sync Drive cloud

Archivo creado 07:36 Caracas; primer disparo 08:00 (24 min después). Para `.gdoc` de móvil con título largo y caracteres acentuados, la propagación a la API Drive puede tardar más que la sync de Drive Desktop. El InboxBot de las 08:00 podría no haber visto el archivo aún. Pero esto no explica el segundo disparo a las 10:00.

### Hipótesis combinada

La hipótesis más explicativa es que la rutina **escanea la jerarquía A canónica** (correcto), **pero falla silenciosamente al resolver `.gdoc`** (Hipótesis 2). La duplicación estructural (Hipótesis 1) es un riesgo paralelo que debe remediarse aunque no sea la causa directa de esta incidencia particular.

---

## Acciones recomendadas para el Owner

### Inmediatas (pre-próximo disparo de la rutina)

1. **Revisar el prompt remoto del InboxBot** en Web UI: `https://claude.ai/code/routines/trig_01RgGGbpCvckUzSwkyGMDNtm`. Confirmar si referencia path por nombre o por parentId hardcoded.
2. **Revisar logs de los disparos de hoy** (08:00 y 10:00 Caracas) en la misma Web UI. Si hay logs de error o de "no tasks found", confirma una de las hipótesis.

### Estructurales (consolidar Drive)

3. **Eliminar o vaciar la jerarquía B legacy** (`1OeBw7clLega1GDV7YtNo3tKpPOygqwz3`). Antes de eliminar:
   - Mover cualquier archivo no procesado de la legacy a la canónica.
   - Verificar que no hay otras rutinas o procesos apuntando a la legacy.
4. **Identificar el parent `1Yex3K9hQnPgaVQ1QRSiH8PClP9NJMKrc`** y su origen — probablemente es la raíz legacy de Drive Backup & Sync. Considerar eliminarlo entero si no tiene contenido vivo.

### Mejoras al InboxBot AGENT.md (v3.3)

5. **Reforzar el manejo de errores en resolución `.gdoc`**: añadir log explícito cuando Drive MCP devuelve error o vacío, y escribir error en outbox del Owner como dice §5d.
6. **Validación previa de carpeta**: el InboxBot debería resolver el path canónico por **fileId** (no por nombre), y abortar si encuentra ambigüedad de nombres en el path.
7. **Heartbeat por disparo**: registrar en `inboxbot-tasklog.md` la línea "Disparo X — escaneo Y carpetas — Z tareas encontradas — N procesadas" en cada ejecución, incluso cuando no hay tareas (para distinguir "no había tareas" de "rutina no disparó").

---

## Estado actual

- Tarea del Owner **procesada manualmente** en sesión local Claude Code 2026-05-07 (cadena CSC completa).
- Deliverable entregado en outbox Drive: `2026-05-07_Vivienne_anglicismos-marcas-genteca_APROBADO-PARA-owner.pptx`.
- DONE marker creado en jerarquía A canónica: `DONE_tarea-anglicismos-marcas-genteca_2026-05-07.txt`.
- Archivos fuente movidos a `_archived/`.
- Gmail draft enviado al Owner con resumen + escalaciones.
- Este memo documenta el incidente para evitar recurrencia.

---

## Trazabilidad

- Trigger ID rutina: `trig_01RgGGbpCvckUzSwkyGMDNtm`
- AGENT.md afectado: `C:\RAUL\.claude\agents\inboxbot\AGENT.md` v3.2
- Memoria persistente actualizada: `feedback_drive_dual_inbox_hierarchy.md` (a crear)
