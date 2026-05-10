---
document_id: "PENDING-DECISIONS-REGISTRY"
document_type: "governance-registry-kanban"
author: "Claude Opus 4.7 + Owner"
creation_date: "2026-05-09"
last_updated: "2026-05-09"
purpose: "Kanban acumulativo (append-only) de decisiones in-flight que activan el patrón Pause+Resume. Permite a Owner / agentes / cron tasks ver el estado de cualquier decisión sin escanear inboxes."
audience: ["Owner", "InboxBot", "Agentes que activan Pause+Resume (Bruna, Aurelio, Vael, Vera, Orlan, etc.)"]
status: "active"
ssot_for: ["pending-decisions-kanban"]
depends_on: ["DECISION-MAKERS.md", "GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md"]
version: "1.0"
how_to_use: "Cualquier agente que active Pause+Resume DEBE crear una row aquí con un Decision-ID único (formato DEC-YYYY-MM-DD-NNN). InboxBot lee este archivo en cada ciclo para detectar decisions con response esperada y dispara la lógica de reentry. Append-only: decisiones cerradas (RESPONDED, EXPIRED, CLOSED-*) NO se borran — quedan como historial."
---

# PENDING-DECISIONS-REGISTRY — Kanban acumulativo de decisiones in-flight

## Cómo se usa este registro

1. **Toda decisión que active Pause+Resume crea una row.** El agente solicitante (Bruna, Aurelio, etc.) genera el Decision-ID y appendea a la tabla cuando entrega el package al decisor.
2. **InboxBot actualiza el campo `Estado`** cuando detecta respuesta del decisor en el canal correspondiente (ej. `01-inbox/05-from-junta/DEC-2026-05-09-001_response.md`).
3. **Cuando el estado pasa a `RESPONDED`**, el agente solicitante registra el outcome en `Respuesta` + linka al deliverable resultante. NO borrar la row.
4. **Append-only.** Decisiones cerradas (RESPONDED / EXPIRED / CLOSED-*) quedan como historial.
5. **Owner puede agregar notas manuales** en columna `Owner notes` para anotar contexto que el agente no captura.
6. **Cuando el deliverable queda en estado `AWAITING-DECISION-<id>`** (ver C en proposal Phase 2), el `<id>` referenciado debe existir aquí.

---

## Estados posibles (vocabulario canónico)

| Estado | Significado | Próximo paso |
|---|---|---|
| `PENDING` | Solicitud entregada, esperando respuesta del decisor | Esperar / monitorear deadline |
| `IN-DELIBERATION` | Decisor confirmó que está trabajando en respuesta | Esperar SLA típico |
| `SUSPENDED-UPSTREAM` | Decisión bloqueada esperando insumo previo (no esperando al decisor — ej. segunda iteración Orlan, confirmación Vera) | Desbloquear upstream antes de notificar al decisor |
| `PARTIALLY-RESPONDED` | Multi-decisor: una o más sub-decisiones respondieron, otras no | Esperar restantes; tracker en columna Respuesta |
| `RESPONDED` | Respuesta recibida y registrada | Reanudar cadena del agente solicitante |
| `ESCALATED` | Pasó SLA típico sin respuesta, se escaló al next-level | Esperar nueva respuesta |
| `EXPIRED` | Deadline pasó sin respuesta. Decisión muerta. | Cerrar o reactivar como decision-id nuevo |
| `CLOSED-WITHDRAWN` | Owner / agente retiró la solicitud antes de respuesta | Documentar razón |
| `CLOSED-CONFLICT` | Multi-decisor: hubo conflicto, escalado a Owner | Owner resuelve, status pasa a RESPONDED con resolución Owner |
| `CLOSED-NOT-VIABLE` | Multi-decisor: alguien rechazó y no se va a alternative | Documentar razón en Respuesta |

> **Deltas vs proposal Phase 2 sección B.2** (resueltos por Owner 2026-05-09 al implementar Step 2 de Phase 3):
> - `PARTIALLY-RESPONDED` — formalizado como canónico (estaba referenciado en patrón A.4 sin entrada en B.2).
> - `CLOSED-NOT-VIABLE` — formalizado como canónico (estaba referenciado en patrón A.4 sin entrada en B.2).
> - `SUSPENDED-UPSTREAM` — nuevo estado, no presente en proposal. Distingue "esperando decisor" de "esperando insumo upstream". Caso real: claims de Bruna que dependen de segunda iteración Orlan/Vera antes de poder enrutar a decisor.
>
> Estos deltas se consolidan en `DECISIONS.md` cuando se ejecute Step 7 de Phase 3.

---

## Tabla de decisiones in-flight (append-only)

| Decision-ID | Project / Pieza | Agente solicitante | Decisor (ID) | Fecha solicitud | Estado | Deadline | Package | Respuesta | Owner notes |
|---|---|---|---|---|---|---|---|---|---|
| DEC-2026-05-04-001 | GSM-MB-RB-RF-RE empaque (3 variantes) | Owner | JUNTA-GENT + IND-GENT | 2026-05-04 | RESPONDED | - | `03-projects/01-genteca/gsm-empaque/` (PPTX 23 slides + memo AU-1 v2.3) | Junta eligió Línea 2 (con NTC) en convergence con I&D vía WhatsApp Kike-Canudas. Pendiente arte final con Oz. | Caso real que originó el patrón A.4 Multi-decision-maker convergence. |
| DEC-2026-05-06-001 | GME protector monofásico Exceline | Bruna | OWNER + IND-GENT | 2026-05-06 | PENDING | - | Cadena CSC GME cerrada 2026-05-06 (research → Orlan → Vera → Vivienne deck) | - | Escalación de riesgo de diseño Bruna→Owner pendiente discusión engineering. Lanzamiento octubre 2026. |
| DEC-2026-05-06-002 | GME claim "primero LATAM" | Bruna | OWNER | 2026-05-06 | SUSPENDED-UPSTREAM | - | BR-2 entry #15 | - | Bloqueado upstream: requiere segunda iteración OL-3 + confirmación specs antes de poder enrutar a Owner. Caso fundador del estado SUSPENDED-UPSTREAM. |
| DEC-2026-05-08-001 | Marcas anglicismos junta (deck top-7) | Owner | JUNTA-GENT + SAPI-VE | 2026-05-08 | PARTIALLY-RESPONDED | - | Deck v1+v2 dual (Caso A/B sobre NTC) | Junta: pending. SAPI: no submitted aún. | 3 escalaciones críticas Owner pendientes per memoria: verificar SAPI Exceline + addendum HDE Vera + presupuesto IP. Cadena CSC completa cerrada 2026-05-07. |
| DEC-2026-05-03-001 | COVENIN 3445 verification (Argumento 8) | Bruna | SENCAMER + FONDONORMA + LEGAL-EXT | 2026-05-03 | PENDING | - | BR-2 entry #28 | - | Argumento 8 bloqueado pending verificación normativa formal. Convergence requiere los 3 decisores. |
| DEC-2026-04-29-001 | GST-RD product clarity | Owner | IND-GENT (Kike) | 2026-04-29 | CLOSED-WITHDRAWN | - | Pregunta vía canal informal | Cerrado por Owner: estrategia "canal C — esperar evidencia natural" (no forzar respuesta de Kike). | Per DECISIONS log entry 2026-05-08 D3. Caso histórico de cierre voluntario antes de respuesta. |
| DEC-2026-05-08-D1-D5 | GST Labels — 5 decisiones Owner pendientes | Owner (auto) | OWNER | 2026-05-04 | PENDING | 2026-07 (launch deadline) | Propuesta Oz v1 línea 2 + memoria GST labels | - | Umbrella row por decisión Owner 2026-05-09: se mantiene como una sola entrada hasta que las D1-D5 se materialicen con scope concreto. Cuando lleguen, se expande a sub-IDs `DEC-2026-05-08-D1` ... `-D5`. |

---

## Reglas de mantenimiento

1. **ID único.** Formato `DEC-YYYY-MM-DD-NNN` donde NNN es secuencial dentro del día (001, 002, ...). Para sub-decisiones dentro de un umbrella, sufijo letra/número (`-D1`, `-D2` o `-a`, `-b`).
2. **Append-only.** Nunca borrar rows cerradas — son historial auditable.
3. **Update privilege:**
   - Append: agente solicitante (cuando crea la solicitud).
   - Update estado: InboxBot (cuando detecta respuesta) o agente solicitante (cuando reanuda cadena).
   - Update `Owner notes`: solo Owner (manual).
4. **Cuando estado pasa a RESPONDED:** agente solicitante DEBE llenar `Respuesta` con resumen del outcome + path al deliverable resultante.
5. **Si una decisión se reactiva** (ej. EXPIRED → re-solicitada): NO modificar la row vieja; crear DEC-ID nuevo y referenciar la vieja en `Owner notes`.

---

## Estadísticas (manual por ahora; auto-generadas eventualmente)

**Snapshot 2026-05-09:**

- Total decisiones registradas (siembra): **7** (de las cuales 1 es umbrella de 5 sub-decisiones)
- En flight (PENDING + IN-DELIBERATION + ESCALATED + PARTIALLY-RESPONDED + SUSPENDED-UPSTREAM): **5**
  - PENDING: 3 (DEC-2026-05-06-001, DEC-2026-05-03-001, DEC-2026-05-08-D1-D5)
  - SUSPENDED-UPSTREAM: 1 (DEC-2026-05-06-002)
  - PARTIALLY-RESPONDED: 1 (DEC-2026-05-08-001)
- Cerradas RESPONDED: **1** (DEC-2026-05-04-001)
- Cerradas CLOSED-WITHDRAWN: **1** (DEC-2026-04-29-001)
- CLOSED-CONFLICT: 0
- CLOSED-NOT-VIABLE: 0
- EXPIRED: 0

**Tiempo promedio respuesta por decisor:**

| Decisor | N decisiones cerradas | Tiempo promedio respuesta |
|---|---|---|
| JUNTA-GENT | 1 (parcial via convergence) | ~5 días (DEC-2026-05-04-001 entregada 2026-05-04, Línea 2 confirmada antes de 2026-05-09) |
| IND-GENT | 1 (parcial via convergence con JUNTA-GENT) | ~5 días |
| OWNER | 1 (CLOSED-WITHDRAWN, no es respuesta de fondo) | N/A (no aplica para withdrawn) |
| Otros | 0 | N/A |

> Tabla incompleta hasta acumular más casos cerrados. Re-evaluar cuando haya ≥3 decisiones cerradas por decisor.

---

## Referencias

- [`DECISION-MAKERS.md`](DECISION-MAKERS.md) — registro de decisores y sus IDs cortos referenciados en columna `Decisor`.
- [`GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md`](GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md) — propuesta arquitectónica completa (sección B.2 schema, sección G siembra, sección A.1 patrón Pause+Resume).
- [`DECISIONS.md`](DECISIONS.md) — log permanente de decisiones arquitectónicas (este registry es para decisiones operacionales in-flight, NO para arquitectónicas).
- [`RISK-POLICY.md`](RISK-POLICY.md) — política de riesgo Bruna (origen de varias decisiones BR-* en este registro).

---

## Decisiones Owner sobre el diseño de este registro (resueltas 2026-05-09)

Estas decisiones se tomaron al implementar Step 2 de Phase 3 y se reflejan ya en el cuerpo del registry. Quedan documentadas aquí para auditoría:

1. **Formalizar `PARTIALLY-RESPONDED` y `CLOSED-NOT-VIABLE` como canónicos** → ✅ Sí (ambos). Razón: ya en uso vía patrón A.4, coherencia inmediata. Delta a consolidar en `DECISIONS.md` durante Step 7.
2. **Crear estado `SUSPENDED-UPSTREAM`** → ✅ Sí. Razón: distingue "esperando decisor" (acción del decisor) de "esperando insumo upstream" (acción de un agente del sistema). Caso fundador: DEC-2026-05-06-002.
3. **Modelado DEC-2026-05-08-D1-D5** → ✅ Umbrella row. Razón: las 5 D no tienen scope concreto en memoria todavía; se expande cuando se materialicen.
4. **Quién genera el Decision-ID** → ✅ Agente solicitante. Razón: modelo directo, no requiere mods adicionales a InboxBot. InboxBot solo actualiza estado/respuesta.

---

**Estado:** activo desde 2026-05-09 con siembra inicial de 7 decisiones (sección G del proposal). Append-only.
