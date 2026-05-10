---
document_id: "GOVERNANCE-PATTERNS"
document_type: "governance-patterns-catalog"
purpose: "Catálogo vivo de patrones operativos de governance del sistema /RAUL/. SSoT activo para A.1-A.5+. La sección A del proposal Phase 2 queda como histórico de la propuesta original; este doc es el que se actualiza cuando emergen patrones nuevos."
audience: ["Todos los agentes de governance (Bruna, Aurelio, Vael, Vera, Orlan)", "InboxBot", "Owner"]
status: "active"
ssot_for: ["governance-patterns-catalog"]
depends_on: ["GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md", "DECISION-MAKERS.md", "PENDING-DECISIONS-REGISTRY.md", "FRONTMATTER-CONVENTIONS.md"]
version: "1.0"
last_updated: "2026-05-10"
how_to_use: "Cuando un agente o Owner llega a una situación operativa que requiere governance (decisión externa bloqueante, alternativa fuera de cadena estándar, urgencia, multi-decisor, modificación post-CSC, etc.), buscar aquí el patrón aplicable. Si ninguno encaja, escalar a Owner para evaluar si formalizar uno nuevo."
---

# GOVERNANCE-PATTERNS.md

## Catálogo vivo de patrones operativos de governance — Sistema /RAUL/

**Versión:** 1.0
**Última actualización:** 2026-05-10 (creación inicial — incluye A.1-A.4 ya establecidos en proposal Phase 2 + nuevo A.5 formalizado en sesión 2026-05-10)

---

## Cómo se usa este catálogo

1. **Identificar la situación operativa** que tienes enfrente (decisión bloqueada, urgencia, modificación de output CSC, etc.).
2. **Buscar el patrón que aplica** en la tabla de abajo.
3. **Seguir los pasos** del patrón. Si el patrón referencia otros artefactos del sistema (templates, registros, status field), usarlos tal como están especificados.
4. **Si ningún patrón encaja**, NO improvisar. Escalar a Owner para evaluar si formalizar un patrón nuevo (A.6+).

| Patrón | Nombre | Cuándo aplica | Detalle |
|---|---|---|---|
| A.1 | Pause + Resume | Decisión externa bloqueante (cualquier decisor humano fuera de cadena CSC) | Ver proposal §A.1 (resumen abajo) |
| A.2 | Owner-driven alternative | Owner propone alternativa que la cadena CSC estándar NO produciría | Ver proposal §A.2 (resumen abajo) |
| A.3 | Crisis override | Urgencia genuina con deadline corto que no permite gates estándar | Ver proposal §A.3 (resumen abajo) |
| A.4 | Multi-decision-maker convergence | Decisión requiere aprobación combinada de múltiples decisores | Ver proposal §A.4 (resumen abajo) |
| A.5 | Owner post-CSC derivative | Owner modifica un deliverable CSC antes de presentarlo/distribuirlo, basado en input post-CSC (reuniones, intuición, ajustes) | **Detalle completo abajo** — nuevo, formalizado 2026-05-10 |

---

## A.1 — Pause + Resume (resumen)

**Cuándo aplica:** un agente del sistema (Bruna, Aurelio, Vael, etc.) llega a un punto donde no puede continuar sin input de un humano externo (Owner, junta, regulator, contraparte).

**Resumen:** crear Decision-ID `DEC-YYYY-MM-DD-NNN`, workspace en `01-inbox/04-decisions-in-flight/<project-id>/<decision-id>/`, copia adaptada al `_outgoing/` del canal, append fila en `PENDING-DECISIONS-REGISTRY.md` con estado inicial, status del deliverable bloqueado pasa a `AWAITING-DECISION-<id>`. InboxBot detecta respuesta cuando llega y reanuda al agente original.

**Detalle completo:** [`GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md` §A.1](GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md).

---

## A.2 — Owner-driven alternative (resumen)

**Cuándo aplica:** Owner quiere proponer una alternativa que ningún agente generó vía cadena estándar (caso típico: junta dice "ninguna opción nos convence, exploremos D que no consideraron"; o Owner tiene una intuición desviada del análisis).

**Resumen:** Owner crea archivo en `01-inbox/01-owner-to-raul/_alt-<descripcion>.md` (sufijo `_alt-` activa routing especial). Pasa por gates Bruna → Vera → Orlan ANTES del flujo CSC normal. Si los 3 OK, regresa a Aurelio para integrar al plan + Owner aprueba final.

**Detalle completo:** [`GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md` §A.2](GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md).

---

## A.3 — Crisis override (resumen)

**Cuándo aplica:** urgencia genuina (deadline corto, situación reactiva — junta convocada con 6h de aviso, regulator exige 48h, competidor lanza algo que requiere counter-positioning rápido).

**Resumen:** Owner crea archivo `01-inbox/01-owner-to-raul/_urgent_<deadline>_<descripcion>.md`. Raul ignora cadena estándar y va directo al agente más relevante con SLA agresivo. Output marcado `status: CRISIS-DRAFT`. Bruna hace pasada rápida si hay claims sensibles. **Post-mortem obligatorio en 72h:** Bruna documenta qué se saltó, qué riesgos quedaron sin gatear, qué remediación si emergen issues.

**Detalle completo:** [`GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md` §A.3](GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md).

---

## A.4 — Multi-decision-maker convergence (resumen)

**Cuándo aplica:** decisión que requiere aprobación combinada de múltiples decisores (ej. claim sensible que requiere Owner + junta + legal externo, o lanzamiento que requiere I&D + comercial + Owner).

**Resumen:** agente generador identifica que multiple-stakeholder approval es necesaria. Genera "convergence package" con sub-paquetes uno por decisor. Sistema registra `convergence-decision-id` que agrupa N sub-decisions paralelas. Cada sub-decision sigue Pause+Resume (A.1). Estado: `PARTIALLY-RESPONDED` hasta que todas reportan. Si todas APRUEBAN → cadena reanuda. Si alguna RECHAZA → activa A.2 (alternative) o cierra como `CLOSED-NOT-VIABLE`. Si CONFLICT → escalación a Owner.

**Detalle completo:** [`GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md` §A.4](GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md).

---

## A.5 — Owner post-CSC derivative (NUEVO — formalizado 2026-05-10)

### Cuándo aplica

Owner toma un deliverable producido por la cadena CSC (típicamente un deck de Vivienne, pero puede ser un email de Solenne, un visual de Atlas, un guion de Nerea) y **lo modifica antes de presentarlo o distribuirlo**, con base en input que llegó **después** de cerrada la cadena CSC:

- Reuniones con colaboradores que aportaron observaciones tras revisar el output original.
- Conversaciones informales (whatsapp, café) que sugirieron ajustes.
- Intuición o reframe del Owner basado en contexto que la cadena no tenía.
- Ajustes tácticos pre-presentación (orden de slides, cambio de tono para audiencia específica, énfasis distinto).

El output modificado **es lo que de verdad se presenta o distribuye**, no la versión CSC original. Sin formalizar este patrón, el sistema asume erróneamente que la versión CSC es la presentada → decisiones se vinculan a la versión incorrecta, claims nuevos no pasan por gate de riesgo.

**Cuándo NO aplica:**

- Si la modificación es trivial (typo, ajuste de formato sin cambio de mensaje) → puede actualizarse el original CSC directamente con bump de versión, no requiere A.5.
- Si la modificación introduce un mensaje radicalmente distinto / contradictorio al análisis CSC → eso es A.2 (Owner-driven alternative), no A.5.
- Si la modificación es porque la cadena CSC tenía un error técnico → corregir el original CSC y refrescar la cadena downstream, no derivar.

### Pasos

1. **Crear archivo binario modificado** en el project folder, etapa correcta:
   - Path: `03-projects/<dominio>/<project-id>/04-published-and-hand-off/<fecha>_<deck>_owner-presented.<ext>`
   - El binario (.pptx, .pdf, .docx) **NO se commitea** (ya gitignored por convención existente).
   - Vive en local + Drive sync para disponibilidad al presentar.

2. **Crear DELTA.md** en el mismo folder, COMMITEADO:
   - Path: `03-projects/<dominio>/<project-id>/04-published-and-hand-off/<fecha>_<deck>_owner-presented_DELTA.md`
   - Punto de partida: `04-system/04-tools-and-scripts/templates/delta-document-template.md`.
   - Frontmatter mínimo:
     ```yaml
     ---
     document_id: <project-id>-deck-owner-presented-<fecha>
     document_type: owner-derivative-for-presentation
     status: APPROVED  # Owner es productor + aprobador en este caso (a menos que claims nuevos requieran Bruna — ver paso 3)
     agent_originating: <agente CSC original — Vivienne, Solenne, Atlas, Nerea>
     modified_by: OWNER
     basado_en: <link relativo a la versión CSC original>
     para_presentar_a: <ID per DECISION-MAKERS — JUNTA-GENT, COMERCIAL-GENT, etc.>
     fecha_presentacion: YYYY-MM-DD
     pattern_applied: A.5
     ---
     ```
   - Cuerpo:
     - **Por qué se modificó** (1-2 párrafos): qué reuniones / colaboradores / input post-CSC motivó los cambios.
     - **Qué cambió** slide-a-slide o sección-por-sección: agregado / removido / modificado, con razón por cambio.
     - **Claims o mensajes nuevos** introducidos respecto a la versión CSC original (sección crítica — ver paso 3).
     - **Declaración explícita:** "esta es la versión vigente para presentar; ignorar `<link a versión CSC original>` para esta presentación".

3. **Si el DELTA introduce claims o mensajes nuevos** que NO existían en la versión CSC original → submit a Bruna para revisión:
   - **Si hay tiempo antes de presentar:** Bruna ejecuta BR-3 quick (preguntas binarias: defensible / hay precedente / requiere caveat). Resultado documentado en el DELTA bajo sección "Bruna review post-derivative".
   - **Si NO hay tiempo:** activar A.3 (Crisis override) en el DELTA → `status: CRISIS-DRAFT`. Bruna hace post-mortem en 72h post-presentación.

4. **Si la presentación va a un decisor formal** (junta, regulator, etc.): activar A.1 (Pause+Resume) con el DELTA como pieza presentada:
   - Generar `DEC-YYYY-MM-DD-NNN`.
   - Workspace en `01-inbox/04-decisions-in-flight/<project-id>/<decision-id>/`.
   - En `context.md`, campo explícito: `pieza_presentada: <path al DELTA.md>` (NO al deck CSC original).
   - Append fila en `PENDING-DECISIONS-REGISTRY.md` con decisor correspondiente.
   - Copiar DELTA + binario al `_outgoing/` del canal.

5. **Post-presentación:**
   - Si activó A.1 → acta de respuesta llega por canal (`05-from-junta/`, `06-from-regulators/`, `07-from-third-parties/`). InboxBot detecta y reanuda.
   - Si NO activó A.1 (presentación informal sin decisor formal): Owner registra brevemente el outcome en el mismo DELTA bajo sección "Outcome de presentación" (qué se concluyó, qué próximas acciones, qué cambios al producto/proyecto).
   - **Si la presentación generó cambios al producto / al proyecto:** actualizar el project folder + DECISIONS.md entry si el cambio es arquitectónico.

6. **Cierre del derivative:**
   - DELTA queda como artefacto permanente en `04-published-and-hand-off/`.
   - Status del DELTA pasa a `PUBLISHED` cuando se presentó.
   - Si Bruna hizo post-mortem (caso A.3 escalation), su review se anexa al DELTA o se linkea desde él.

### Por qué este patrón

Sin él:

- Las modificaciones Owner pre-presentación quedan **invisibles al sistema**: agentes asumen que la versión CSC es lo presentado.
- Las **decisiones de junta/decisor se vinculan a la versión incorrecta** del package — incoherencia entre lo que se presentó y lo que el sistema cree que se presentó.
- Los **claims nuevos introducidos por Owner no pasan por gate de Bruna** — riesgo de claims indefendibles publicados sin trazabilidad.
- **Trazabilidad del proceso real se pierde:** future agents que revisen el proyecto no entienden por qué la decisión final difiere del análisis CSC.

Con A.5 explícito:

- El delta queda **documentado y commiteado** (visible al sistema).
- La decisión se vincula al **DELTA, no al CSC original** (coherencia).
- Los claims nuevos pasan por **Bruna retroactiva** (gate de riesgo no se salta).
- Future agents tienen **el contexto completo** del proceso (CSC original + delta + outcome).

### Distinción crítica vs A.2 (Owner-driven alternative)

| Dimensión | A.2 (Alternative) | A.5 (Derivative) |
|---|---|---|
| Cuándo se inserta | ANTES o EN LUGAR DE la cadena CSC | DESPUÉS de la cadena CSC |
| Relación con CSC | Contradice / desafía análisis CSC | Adapta / refina output CSC |
| Dirección | Owner propone idea que CSC no consideró | Owner modifica idea que CSC sí produjo |
| Routing | Bruna → Vera → Orlan → Aurelio (gates pre-CSC) | Bruna post-derivative SI hay claims nuevos (gate post-CSC) |
| Filename | Sufijo `_alt-` en `01-owner-to-raul/` | Sufijo `_owner-presented` + DELTA en `04-published-and-hand-off/` |
| Output esperado | Plan ajustado o nueva pieza | Pieza modificada lista para presentar |

Si dudas si tu caso es A.2 o A.5: pregunta "¿la cadena CSC ya produjo el output principal y solo lo estoy ajustando?" → A.5. "¿Estoy proponiendo algo que la cadena CSC no produjo o que contradice su análisis?" → A.2.

---

## Cómo proponer un patrón nuevo (A.6+)

Si encuentras una situación operativa recurrente que ningún patrón actual cubre:

1. **Documentar el caso concreto** que lo motiva (1 párrafo): qué pasó, por qué los patrones actuales no aplican.
2. **Drafft del patrón** siguiendo la estructura de A.1-A.5: cuándo aplica, pasos, por qué este patrón.
3. **Identificar relaciones** con patrones existentes (extiende, contradice, complementa).
4. **Escalar a Owner** para approval.
5. Si aprobado: agregar al catálogo aquí + entry en `DECISIONS.md` + update memoria si afecta cómo opera el sistema.

---

## Referencias

- [`GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md`](GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md) — propuesta arquitectónica original con detalle de A.1-A.4.
- [`DECISION-MAKERS.md`](DECISION-MAKERS.md) — IDs de decisores referenciados en pasos de cada patrón.
- [`PENDING-DECISIONS-REGISTRY.md`](PENDING-DECISIONS-REGISTRY.md) — registry de decisiones in-flight (alimentado por A.1, A.4 y A.5 cuando va a decisor formal).
- [`FRONTMATTER-CONVENTIONS.md`](../01-config/FRONTMATTER-CONVENTIONS.md) — campo `status` referenciado por casi todos los patrones (`CRISIS-DRAFT` para A.3, `AWAITING-DECISION-<id>` para A.1/A.4/A.5, etc.).
- Templates: `04-system/04-tools-and-scripts/templates/` — `decision-request-template`, `alternative-proposal-template`, `regulator-submission-template`, `junta-decision-package-template`, `delta-document-template`.
- [`DECISIONS.md`](DECISIONS.md) — log cronológico de decisiones arquitectónicas, incluye entry 2026-05-10 sobre formalización A.5.

---

## Notas de versión

- **v1.0 — 2026-05-10** — creación inicial. Incluye A.1-A.4 como resúmenes con link al proposal Phase 2 (donde están con detalle completo) + A.5 formalizado en detalle. A partir de aquí, este doc es el SSoT activo del catálogo de patrones.
