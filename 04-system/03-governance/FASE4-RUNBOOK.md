# Fase 4 — Runbook de ejecución
## Reconfiguración de InboxBot (OneDrive)

**Versión:** 1.1
**Fecha de preparación:** 2026-04-25
**Última revisión:** 2026-04-26 — migrado de Google Drive a OneDrive (1TB disponible, sin costo adicional)
**Ejecutor:** Owner (Raoul Bermúdez) — esta fase requiere acciones manuales
**Tiempo estimado:** 30–60 min
**Ventana de inestabilidad:** hasta 24h mientras el trigger InboxBot se re-sincroniza con la nueva ruta

---

## Decisión de arquitectura

El inbox usa **OneDrive** (Microsoft, 1TB) en lugar de Google Drive (200GB).

| | Google Drive | OneDrive (elegido) |
|---|---|---|
| Espacio disponible | 200 GB (95 GB usados) | 1 TB |
| Costo extra | Posiblemente sí | No |
| Path local | `G:\Mi unidad\...` (streaming) | `C:\Users\User\OneDrive\...` (local) |
| App móvil | Drive | OneDrive |

Google Drive queda en modo **streaming** (G: como unidad virtual, sin backup de PC).

---

## Paths definitivos

| Propósito | Path local | Cloud |
|---|---|---|
| InboxBot lee (briefs del Owner) | `C:\Users\User\OneDrive\RAUL\01-inbox\01-owner-to-raul\` | OneDrive web / app móvil |
| Raul deposita entregables | `C:\Users\User\OneDrive\RAUL\01-inbox\02-deliverables-to-owner\` | OneDrive web / app móvil |

---

## Prerequisitos antes de ejecutar

- [x] Sistema /RAUL/ en estado estable (Fases 1-3 completas ✅)
- [x] Carpetas OneDrive creadas (`01-owner-to-raul\` y `02-deliverables-to-owner\`) ✅
- [x] Google Drive Desktop en modo streaming, sin backup de PC ✅
- [ ] No hay briefs activos en el inbox viejo que no se hayan procesado
- [ ] Tienes acceso a la plataforma de automatizaciones (Routines, donde vive el trigger InboxBot)

**Paso 2 verificado 2026-04-26:** README visible en PC y en app OneDrive móvil ✅

---

## Paso 1 — Inventariar y migrar contenido de inboxes anteriores

Antes de reconfigurar, asegúrate de que no se pierda nada:

1. Revisar `C:\WorkspaceIA\PROJECTS\Claude code\Owner Inbox\` → copiar lo que valga a `C:\RAUL\01-inbox\02-deliverables-to-owner\`
2. Revisar `C:\WorkspaceIA\Owner Inbox\` (si existe) → mismo destino.
3. Revisar `C:\WorkspaceIA\PROJECTS\Claude code\Team inbox\` → si hay algo, copiarlo a `C:\RAUL\01-inbox\01-owner-to-raul\`
4. Marcar como completado cuando estés seguro de que nada se perdió.

---

## Paso 2 — Verificar sincronización OneDrive

Las carpetas ya existen en `C:\Users\User\OneDrive\RAUL\`. Verificar que OneDrive Desktop las está sincronizando:

1. Abre el Explorador de archivos → navega a `C:\Users\User\OneDrive\RAUL\01-inbox\`
2. Verifica que los íconos de las carpetas muestran la nube o la palomita de OneDrive (sync activo)
3. Desde tu móvil (app OneDrive), navega a `RAUL/01-inbox/01-owner-to-raul/` — deberías ver el `README.md`
4. Si no aparece, abre OneDrive Desktop → verifica que no está en pausa

---

## Paso 3 — Reconfigurar el trigger InboxBot ✅ (2026-04-26)

El InboxBot fue rediseñado como agente agnóstico en:
`C:\RAUL\.claude\agents\inboxbot\AGENT.md`

El trigger viejo (`trig_01RgGGbpCvckUzSwkyGMDNtm`) apuntaba a rutas de Google Drive muertas.
El nuevo agente usa el filesystem local de OneDrive — sin dependencia de Drive MCP.

**Para actualizar o recrear el trigger en Routines (Claude Code Desktop):**
1. Pausar o eliminar el trigger `trig_01RgGGbpCvckUzSwkyGMDNtm`
2. Crear nueva Routine con este prompt exacto:
   ```
   Ejecuta InboxBot. Lee y sigue al pie de la letra C:\RAUL\.claude\agents\inboxbot\AGENT.md
   ```
3. Frecuencia: cada 4 horas (o manual)
4. Anotar el nuevo trigger ID en `DECISIONS.md`

**Para otros LLMs:** cargar `AGENT.md` como system prompt y ejecutar.

---

## Paso 4 — Test end-to-end

1. Desde el móvil (app OneDrive), sube un archivo de prueba a `RAUL/01-inbox/01-owner-to-raul/`
2. Verifica en el PC que aparece en `C:\Users\User\OneDrive\RAUL\01-inbox\01-owner-to-raul\`
3. Esperar un ciclo del InboxBot (hasta 4h, o forzarlo manualmente si la plataforma lo permite)
4. Verificar que se genera un draft en Gmail con la tarea procesada
5. Verificar que el Owner puede ver entregables en `RAUL/01-inbox/02-deliverables-to-owner/` desde el móvil

---

## Paso 5 — Archivar el repo histórico

Una vez que el test del paso 4 sea exitoso:

1. Hacer un último commit en `C:\WorkspaceIA\PROJECTS\Claude code\` si hay cambios pendientes.
2. Comprimir o renombrar la carpeta a `Claude-code_pre-migration_2026-04-25` como referencia histórica.
3. No borrar — mantener como backup por al menos 30 días.

---

## Paso 6 — Registrar finalización

Una vez completado todo:

1. Agregar entrada en `DECISIONS.md`: "Fase 4 completada — InboxBot reconfigurado con OneDrive. Nuevo trigger ID: [XXXXXXXXX]."
2. Agregar entrada en `task-log.md`: `| 2026-XX-XX | Raul | Fase 4 — InboxBot actualizado a OneDrive | delivered |`
3. Actualizar `MIGRATION-PLAN.md` marcando Fase 4 como completada.

---

## Rollback (si algo sale mal)

Si el trigger falla con OneDrive:
1. Reactivar el trigger viejo `trig_01RgGGbpCvckUzSwkyGMDNtm` con sus rutas originales.
2. Las carpetas de OneDrive no se tocan — el rollback es solo del trigger.
3. Reportar el error y decidir cuándo reintentar.

---

## Notas

- `03-raw-sources/` permanece en `C:\RAUL\01-inbox\03-raw-sources\` — local únicamente, no va a OneDrive ni a Drive.
- `C:\RAUL\` completo está en git — no necesita sincronización cloud adicional.
- Google Drive Desktop queda en modo streaming (G:) sin backup de PC — no interferirá.
- OneDrive maneja el inbox. Git maneja el sistema.
