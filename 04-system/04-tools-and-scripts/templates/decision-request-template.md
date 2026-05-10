---
decision_id: DEC-YYYY-MM-DD-NNN
project: <project-id>
piece: <pieza-bloqueada>
agent_requesting: <nombre-agente>
decisor: <ID de DECISION-MAKERS.md — ej. OWNER, JUNTA-GENT, IND-GENT>
date_request: YYYY-MM-DD
deadline: YYYY-MM-DD  # o "open" si no hay deadline
canal: <canal correcto per DECISION-MAKERS — ej. 01-owner-to-raul/, 05-from-junta/_outgoing/>
status: PENDING  # PENDING | IN-DELIBERATION | SUSPENDED-UPSTREAM | RESPONDED | ESCALATED | EXPIRED | CLOSED-WITHDRAWN | CLOSED-CONFLICT | CLOSED-NOT-VIABLE | PARTIALLY-RESPONDED
---

# Decision Request — <título corto>

## Contexto

<por qué esta decisión es necesaria, qué proyecto/pieza está bloqueada, qué urgencia hay, qué pasaría si no se decide>

## Opciones

### Opción A — <nombre>

- **Qué propone:** ...
- **Pros:** ...
- **Contras:** ...
- **Caveats:** (literal de Bruna si aplica)

### Opción B — <nombre>

- **Qué propone:** ...
- **Pros:** ...
- **Contras:** ...
- **Caveats:** ...

### Opción C — <nombre>

- **Qué propone:** ...
- **Pros:** ...
- **Contras:** ...
- **Caveats:** ...

> Si solo hay 2 opciones reales, eliminar Opción C. Si hay >3, agregar Opción D, E, etc. Mantener formato consistente.

## Recomendación del agente solicitante

<cuál opción + por qué + qué riesgos asume el agente al recomendar esto>

## Información que necesitamos recibir de vuelta

1. <pregunta específica que el decisor debe responder>
2. <pregunta específica>
3. (si conflicto entre opciones, qué criterio de tiebreak prefiere el decisor)

## Trazabilidad

- **Cadena CSC origen:** <links a inputs Vera/Orlan/Vael/etc>
- **BR-X relacionados:** <links a entries de Bruna en governance log>
- **DECISIONS.md entries previas:** <si la decisión modifica algo previamente decidido>
- **Project folder:** `03-projects/<dominio>/<proyecto>/`
- **Workspace de la decisión:** `01-inbox/04-decisions-in-flight/<project-id>/<decision-id>/`

---

_Instrucciones de uso: guardar como `package.md` en `01-inbox/04-decisions-in-flight/<project-id>/<decision-id>/`. Si decisor es externo (JUNTA-GENT, SAPI-VE, etc.), copiar versión adaptada al `_outgoing/` del canal correspondiente. Registrar fila nueva en `04-system/03-governance/PENDING-DECISIONS-REGISTRY.md`. El agente solicitante genera el `decision_id` siguiendo formato DEC-YYYY-MM-DD-NNN (NNN secuencial dentro del día)._

_Template v1.0 — 2026-05-09 — Phase 3 step 4_
