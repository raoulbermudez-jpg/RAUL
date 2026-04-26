# Fase 4 — Runbook de ejecución
## Reconfiguración de Drive Desktop + InboxBot

**Versión:** 1.0
**Fecha de preparación:** 2026-04-25
**Ejecutor:** Owner (Raoul Bermúdez) — esta fase requiere acciones manuales
**Tiempo estimado:** 2-3 horas en bloque continuo
**Ventana de inestabilidad:** hasta 24h mientras el trigger InboxBot se re-sincroniza con la nueva ruta

---

## Prerequisitos antes de ejecutar

- [ ] Sistema /RAUL/ en estado estable (Fases 1-3 completas ✅)
- [ ] No hay briefs activos en el inbox viejo que no se hayan procesado
- [ ] Tienes acceso a Google Drive Desktop en este equipo
- [ ] Tienes acceso a la plataforma de automatizaciones (Routines, donde vive el trigger InboxBot)
- [ ] Avisa a cualquier colaborador que usará el inbox que habrá mantenimiento por X horas

---

## Paso 1 — Inventariar y migrar contenido de inboxes anteriores

Antes de reconfigurar, asegúrate de que no se pierda nada:

1. Revisar `C:\WorkspaceIA\PROJECTS\Claude code\Owner Inbox\` → copiar lo que valga a `C:\RAUL\01-inbox\02-deliverables-to-owner\`
2. Revisar `C:\WorkspaceIA\Owner Inbox\` (si existe) → mismo destino.
3. Revisar `C:\WorkspaceIA\PROJECTS\Claude code\Team inbox\` → si hay algo, copiarlo a `C:\RAUL\01-inbox\01-owner-to-raul\`
4. Marcar como completado cuando estés seguro de que nada se perdió.

---

## Paso 2 — Reconfigurar Google Drive Desktop

**Objetivo:** que las carpetas correctas de `/RAUL/` se sincronicen con tu Google Drive.

**Configuración objetivo:**

| Carpeta local | Carpeta en Drive |
|---------------|-----------------|
| `C:\RAUL\01-inbox\01-owner-to-raul\` | `Mi unidad\RAUL\01-inbox\01-owner-to-raul\` |
| `C:\RAUL\01-inbox\02-deliverables-to-owner\` | `Mi unidad\RAUL\01-inbox\02-deliverables-to-owner\` |
| `C:\RAUL\02-knowledge-base\` | `Mi unidad\RAUL\02-knowledge-base\` |

**Lo que NO debe sincronizarse a Drive:**
- `C:\RAUL\04-system\` (vive en git, no necesita Drive)
- `C:\RAUL\03-projects\` (local + git)
- `C:\RAUL\05-archive\` (backup separado)

**Pasos en Google Drive Desktop:**
1. Abrir Google Drive Desktop → Preferencias → Mis carpetas.
2. Eliminar las carpetas viejas que estaban sincronizadas (rutas del sistema anterior).
3. Agregar las tres carpetas listadas arriba.
4. Verificar que la sincronización comienza correctamente (íconos de sync en el explorador).
5. Esperar a que el sync inicial complete antes de continuar.

---

## Paso 3 — Actualizar el trigger InboxBot

El trigger actual (`trig_01RgGGbpCvckUzSwkyGMDNtm`) apunta a rutas del sistema anterior.

**Opción A — Editar el trigger existente (recomendado si es posible):**
1. Abrir la plataforma de automatizaciones (Routines / Make / equivalente donde está configurado).
2. Localizar el trigger `trig_01RgGGbpCvckUzSwkyGMDNtm`.
3. Actualizar la ruta de lectura: `G:\Mi unidad\RAUL\01-inbox\01-owner-to-raul\`
4. Verificar que los marcadores `DONE_*.txt` y la lógica de drafts de Gmail siguen funcionando.
5. Guardar.

**Opción B — Recrear el trigger:**
1. Pausar o eliminar `trig_01RgGGbpCvckUzSwkyGMDNtm`.
2. Crear nuevo trigger con:
   - Lectura: `G:\Mi unidad\RAUL\01-inbox\01-owner-to-raul\`
   - Marcadores DONE_: en la misma carpeta
   - Gmail: create_draft (no send directo)
   - Frecuencia: cada 4h (o la que prefieras)
3. Anotar el nuevo trigger ID y registrarlo en `DECISIONS.md`.

---

## Paso 4 — Test end-to-end

1. Subir un archivo de prueba a `G:\Mi unidad\RAUL\01-inbox\01-owner-to-raul\` desde el móvil o Drive web.
2. Esperar un ciclo del InboxBot (hasta 4h, o forzarlo manualmente si la plataforma lo permite).
3. Verificar que se genera un draft en Gmail con la tarea procesada.
4. Verificar que el Owner puede ver el contenido de `01-inbox\02-deliverables-to-owner\` desde el móvil/Drive.

---

## Paso 5 — Archivar el repo histórico

Una vez que el test del paso 4 sea exitoso:

1. Hacer un último commit en `C:\WorkspaceIA\PROJECTS\Claude code\` si hay cambios pendientes.
2. Comprimir o renombrar la carpeta a `Claude-code_pre-migration_2026-04-25` como referencia histórica.
3. No borrar — mantener como backup por al menos 30 días.

---

## Paso 6 — Registrar finalización

Una vez completado todo:

1. Agregar entrada en `DECISIONS.md`: "Fase 4 completada — InboxBot y Drive reconfiguraron con rutas /RAUL/. Nuevo trigger ID: [XXXXXXXXX]."
2. Agregar entrada en `task-log.md`: `| 2026-XX-XX | Raul | Fase 4 — Drive Desktop reconfigurado + trigger InboxBot actualizado | delivered |`
3. Actualizar `MIGRATION-PLAN.md` marcando Fase 4 como completada.

---

## Rollback (si algo sale mal)

Si la reconfiguración de Drive o el trigger falla:
1. Restaurar las rutas anteriores en Drive Desktop.
2. Reactivar el trigger viejo `trig_01RgGGbpCvckUzSwkyGMDNtm` con sus rutas originales.
3. El repo `/RAUL/` no se toca — el rollback es solo de Drive + trigger.
4. Reportar el error y decidir cuándo reintentar.

---

## Notas

- `03-raw-sources/` **no** se sincroniza con Drive (raw sources son locales por diseño).
- `04-system/` y `03-projects/` tampoco van a Drive — se acceden por git.
- Este runbook puede ejecutarse en partes: pasos 1-2 en una sesión, paso 3-4 en otra.
