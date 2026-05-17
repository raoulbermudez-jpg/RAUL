---
status: aprobada-para-implementar
fecha: 2026-05-15
fecha_decision: 2026-05-17
decision: B+A hybrid
autor: Raul-desktop
para: Owner
relacionado: 04-system/02-agents/conceptual/inboxbot.md v5.2, raul.md §6.0
---

## DECISIÓN — 2026-05-17

**Aprobada implementar B+A hybrid.** La opción D (cambio de Drive MCP) fue investigada y descartada: verificación Paxs 2026-05-17 confirmó vía 3 GitHub issues (#52586 open, #22726 closed "not planned", #53489) que Anthropic Cloud Routines NO aceptan custom HTTP MCP connectors con URL arbitraria. El routine de InboxBot está bound al catálogo pre-built de Anthropic, donde `claude.ai Google Drive` no expone update/delete por ID. Ver `reference_anthropic_routines_no_custom_mcp.md`.

**Queue:** implementación B+A hybrid pendiente para próxima sesión Raul-desktop. Estimado 2-3h (edits SSOT v5.3 + AGENT.md + raul.md §6.0 + redeploy prompt routine).



# Propuesta — fix estructural a la acumulación de duplicados de InboxBot en Drive

## Problema

Drive MCP en el entorno cloud del routine InboxBot **solo soporta `create_file`** — no expone `update_file` ni `delete_file` por ID. Cada ciclo del bot reescribe `_ESTADO.md` y `_log-ciclos.md` con un `create_file` → Drive resuelve la colisión de nombre creando `_ESTADO (1).md`, `_ESTADO (2).md`, etc. Igual para `_log-ciclos`.

**Evidencia (2026-05-15, antes del cleanup de hoy):**
- 7 versiones stale de `_ESTADO.md` acumuladas
- 7 versiones stale de `_log-ciclos.md` acumuladas
- 24 versiones acumuladas históricas de `inboxbot-tasklog.md` (v4.0)

Cada ciclo añade una más. El bot reconoce la limitación (v5.0 §6.5) y registra los IDs stale en una nota operativa para que Raul-desktop limpie — pero esto es manual overhead cada sesión.

## Opciones evaluadas

| Opción | Pros | Contras |
|---|---|---|
| **A. Manual cleanup ritual** en raul.md §6.0 | Sin cambio de SSOT, simple | Sigue acumulando entre sesiones; overhead manual recurrente |
| **B. Per-cycle files** para ambos (`_cycle_<ts>.md`) | Cero colisiones, escrituras atómicas a nombres únicos | Fragmenta el log; "current state" requiere sort por mtime |
| **C. Log canónico en repo, ephemeral en Drive** | Repo es SSOT limpia; log persistente versionado | Bot escribe `_pending-cycle_<ts>.md`; raul.md mergea; complica el contrato |
| **D. Cambiar de MCP** | Resuelve raíz | Requiere investigación; fuera de scope inmediato |

## Recomendación — Híbrido B+A (separar concerns)

**Separar las dos superficies en función de su semántica natural:**

### Superficie 1 — Log de ciclos (append-only, history)

Semántica: cada ciclo escribe UNA fila, append-only. Encaja perfecto con per-cycle files.

**Cambio:**
- Eliminar `01-inbox/00-cola/_log-ciclos.md` como output canónico.
- Reemplazar por `01-inbox/00-cola/_cycles/cycle_<YYYY-MM-DDTHHMM>.md` — un archivo por ciclo.
- Cada cycle file contiene: la fila IB-2 + opcionalmente el snapshot IB-4 de ese momento (para auditoría histórica).
- El "log" se lee por directory listing de `_cycles/` ordenado por nombre (= timestamp).
- Cero colisiones porque cada nombre es único.
- Raul-desktop periódicamente consolida cycle files → `04-system/03-governance/inboxbot-cycle-log.md` en el repo (versionado en git) y borra los cycle files consolidados.

### Superficie 2 — Tablero de estado (full overwrite, current state)

Semántica: el Owner consulta UN archivo para ver el estado actual. Necesita ser único y siempre fresco.

**Cambio:**
- Mantener `01-inbox/_ESTADO.md` como path canónico.
- Aceptar la limitación de Drive (sigue creando duplicados numerados).
- Formalizar el cleanup en **raul.md §6.0**: al inicio de cada sesión desktop, eliminar duplicados `_ESTADO (N).md` consolidando contenido del más reciente a `_ESTADO.md`.
- Reducir el costo: ahora es UN archivo, no dos. Cleanup toma <30s.

### Otros archivos del v4.0 ya superseded

- `inboxbot-tasklog.md` queda eliminado (su rol es heredado por `_cycles/`). Versión histórica archivada en `02-deliverables-to-owner/_archived/v4-legacy/inboxbot-tasklog_v4-final.md` (ya hecho 2026-05-15).

## Cambios concretos en SSOT

### `04-system/02-agents/conceptual/inboxbot.md` v5.3

- **§5 IB-2 (Cycle Log Entry):** cambiar de "fila append-only en `_log-ciclos.md`" a "archivo único `_cycles/cycle_<ts>.md` por ciclo, conteniendo: timestamp NOW UTC, canales, items, tickets, errores, + snapshot IB-4 inline".
- **§6.5 paso 2:** reescribir para escritura atómica de cycle file con nombre único; eliminar instrucción de "appendear fila" y nota operativa sobre IDs stale (ya no aplica al log).
- **§6.5 paso 1 (IB-4):** mantener escritura a `_ESTADO.md`; conservar nota operativa "Drive MCP no soporta overwrite — IDs stale a limpiar por Raul-desktop" (aún aplica a esta superficie).
- **§7.3:** rediseñar el formato — ahora es archivo completo por ciclo, no fila de tabla.
- **§10 antipatterns:** retirar el antipattern "saltarse heartbeat en ciclo vacío" (siempre se crea cycle file). Añadir antipattern "intentar appendear a un cycle file ya existente" (rompe atomicidad).

### `.claude/agents/inboxbot/AGENT.md`

- Path map: añadir `_cycles/` como output de IB-2.
- Tool map: para IB-2, `Write` (filesystem) / `mcp__claude_ai_Google_Drive__create_file` (cloud) — sin Edit/append.

### `.claude/agents/raul/AGENT.md` (y raul.md conceptual §6.0)

- Añadir paso "session-start cleanup":
  ```
  - Limpiar `_ESTADO (N).md` duplicados en G:\Mi unidad\RAUL\01-inbox\
  - Consolidar cycle files antiguos (>30 días) de `00-cola/_cycles/` → 04-system/03-governance/inboxbot-cycle-log.md; borrar los consolidados
  ```

### `04-system/03-governance/inboxbot-cycle-log.md` (NUEVO)

- Log canónico histórico versionado en git. Una fila por ciclo, append-only manual (mergea Raul-desktop). Formato igual al actual `_log-ciclos.md`.
- Inicializado con la consolidación del estado actual al momento del migration cutover.

### Actualización del prompt del routine remoto

- Vía `RemoteTrigger update` con la versión adaptada del SSOT v5.3.

## Verificación

Una vez aplicado:
- Próximo ciclo del bot crea `cycle_2026-05-16T0600.md` en `_cycles/` (no colisiona).
- `_ESTADO.md` sigue creando duplicados pero ahora es solo este archivo (1 file vs 2).
- Raul-desktop al iniciar sesión limpia los duplicados de `_ESTADO.md` (estimado 1 archivo por sesión vs ~7 actualmente).

## Riesgos

- **Migración**: el cambio invalida un ciclo del bot mientras se redeploy el prompt. Mitigación: deploy en ventana nocturna (23:00–06:00 sin ciclos).
- **Bot remoto fuera de fase**: si el prompt del routine no se actualiza, el bot v5.2 sigue escribiendo a `_log-ciclos.md`. Mitigación: `RemoteTrigger update` inmediato al cierre del cambio en repo (igual procedimiento que v5.1 → v5.2).
- **Visibilidad para el Owner**: el Owner consulta `_ESTADO.md` (sigue siendo el punto único). Los cycle files son auditables pero no requeridos para uso diario.

## Tamaño del trabajo

- Edits SSOT inboxbot.md: ~30 líneas
- Edits AGENT.md inboxbot: ~5 líneas
- Edits raul.md §6.0: ~10 líneas
- Nuevo archivo inboxbot-cycle-log.md: ~20 líneas seed
- Update remote prompt vía `RemoteTrigger update`: 1 llamada
- Migration cutover script (consolidar cycle files actuales → log canónico): ~50 líneas Python

**Estimado total**: 2–3 horas de sesión.

## Decisión pendiente Owner

- [ ] Aprobar el cambio
- [ ] O priorizar alternativa (e.g., investigar D — cambiar de MCP)
- [ ] O posponer (vivir con el ritual A + cleanup manual)

Mientras tanto, el cleanup manual de hoy (2026-05-15) deja el sistema en estado limpio. La acumulación reaparecerá en el próximo ciclo del bot (3-4 archivos más en 24h).
