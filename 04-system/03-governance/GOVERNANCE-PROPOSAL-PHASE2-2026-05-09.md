---
document_id: "GOVERNANCE-PROPOSAL-PHASE2-2026-05-09"
document_type: "architectural-proposal"
author: "Claude Opus 4.7"
creation_date: "2026-05-09"
purpose: "Propuesta arquitectónica detallada para resolver gaps identificados en GOVERNANCE-DIAGNOSTIC-2026-05-09.md (decision tracking + alternate paths + inbox/outbox channels). Doc-only — no ejecuta cambios. Owner revisa y aprueba antes de implementación."
audience: ["Raoul Bermúdez (Owner)", "Claude Opus 4.7 (futuras sesiones)", "Agentes de governance (Bruna, Aurelio, InboxBot)"]
status: "proposal-pending-owner-review"
ssot_for: []
depends_on: ["GOVERNANCE-DIAGNOSTIC-2026-05-09.md", "DECISIONS.md", "RISK-POLICY.md", ".claude/agents/inboxbot/AGENT.md"]
version: "1.0"
how_to_use: "Leer completo. Anotar qué se aprueba / modifica / rechaza. Owner decide en qué orden ejecutar. Cada componente es independiente — pueden ejecutarse incrementalmente."
---

# Propuesta arquitectónica Phase 2 — Governance del Sistema /RAUL/

## Resumen ejecutivo

El [diagnóstico 2026-05-09](GOVERNANCE-DIAGNOSTIC-2026-05-09.md) identificó que el sistema /RAUL/ tiene **maquinaria de producción sólida** (gates BR/AU/VA, caveats literales, cadena CSC) pero **maquinaria de coordinación con humanos no-Owner casi inexistente**. Los gaps críticos:

1. No hay registro de decisiones-pendientes ni catálogo de decision-makers.
2. No hay mecanismo formal para Owner-driven alternatives, junta-driven alternatives, o crisis override.
3. No hay reentry pattern post-decisión externa.
4. No hay canales para junta directiva, reguladores, third parties ni special deliverables.

Esta propuesta agrega **infraestructura de coordinación** que envuelve el sistema actual SIN modificarlo. La cadena CSC, los gates de calidad, y la disciplina de caveats permanecen intactos.

**Componentes de la propuesta:**

- **A.** 4 patrones operativos formalizados.
- **B.** 2 documentos canónicos nuevos (DECISION-MAKERS, PENDING-DECISIONS-REGISTRY).
- **C.** Convención de status field en deliverables.
- **D.** 5 carpetas nuevas en `01-inbox/`.
- **E.** 4 templates en `04-system/04-tools-and-scripts/templates/`.
- **F.** Modificaciones quirúrgicas a InboxBot AGENT.md.
- **G.** Plan de migración inicial (siembra del registry con decisiones actuales).

**Principio rector:** adiciones se ENVUELVEN alrededor del sistema actual. Nada existente se modifica salvo InboxBot, y solo se le añaden 4-5 secciones nuevas (no se rompen las existentes).

**Plan de adopción:** componentes son independientes. Owner puede ejecutarlos en cualquier orden o saltarse algunos. Recomendación de orden al final del doc.

---

## A. Cuatro patrones operativos formalizados

### A.1 — Patrón "Pause + Resume" (decisión externa bloqueante)

**Cuando aplica:** un agente productor (Bruna, Aurelio, Vael, Atlas, etc.) llega a un punto donde no puede continuar sin input/aprobación de un humano no-Owner (junta, regulador, I&D externo, etc.).

**Pasos:**

1. **Agente identifica decision gate.** Detecta que la información disponible es insuficiente para producir output sin riesgo. Concretamente: claim que requiere validación legal externa, propuesta que requiere voto junta, spec técnica que requiere confirmación I&D.

2. **Agente genera "decision package"** siguiendo `decision-request-template.md`:
   - Contexto operativo (qué proyecto, qué pieza, qué urgencia)
   - 2-4 opciones con trade-offs explícitos
   - Recomendación del agente (con caveats)
   - Qué información necesitamos saber para decidir
   - Deadline si aplica
   - Quién es el decisor
3. **Agente marca su deliverable in-flight** con `status: AWAITING-DECISION-<id>` en frontmatter.

4. **Sistema registra en `PENDING-DECISIONS-REGISTRY.md`** con id único, link al package, link al deliverable bloqueado.

5. **Sistema entrega package al canal correcto:**
   - Junta → `01-inbox/05-from-junta/_outgoing/<package>.md` + presentación física vía Drive
   - Regulador → `01-inbox/06-from-regulators/_outgoing/`
   - Third party → `01-inbox/07-from-third-parties/_outgoing/`
   - Owner final approval → `01-inbox/02-deliverables-to-owner/`

6. **Cadena pausa.** Agente NO continúa producción dependiente.

7. **Cuando llega respuesta:** Owner deposita en `01-inbox/05-from-junta/<id>_response.md` (o canal correspondiente).

8. **InboxBot detecta nueva respuesta**, parsea decision-id del filename, marca registry como `RESPONDED`, notifica al agente original (vía Raul orchestrator) para reanudar.

9. **Agente reanuda** con la decisión incorporada. Si decisión rechaza opción A y aprueba B, agente produce con B. Si pide opción nueva (C), eso activa "Owner-driven alternative" (A.2).

**Ejemplo concreto:**

```
2026-05-04 — Bruna (BR-2 GSM empaque) detecta que naming "Thermo-Safe"
requiere SAPI clearance antes de uso público.
↓
Bruna genera: 01-inbox/04-decisions-in-flight/GSM-empaque/DEC-2026-05-04-001/
  ├── package.md (request a SAPI)
  ├── context.md (proyecto + urgencia)
  └── recommendation.md (alternativa interna mientras espera SAPI)
↓
Marca BR-2 entry: status: AWAITING-DECISION-DEC-2026-05-04-001
↓
Registry: PENDING-DECISIONS-REGISTRY.md gets new row
↓
Owner ve task en outbox, lleva a abogado SAPI
↓
[2-6 meses pasan]
↓
Respuesta SAPI llega: clearance OK
↓
Owner deposita: 01-inbox/06-from-regulators/DEC-2026-05-04-001_response.md
↓
InboxBot detecta, marca RESPONDED
↓
Bruna reanuda BR-2, libera claim "Thermo-Safe" para uso público
```

### A.2 — Patrón "Owner-driven alternative"

**Cuando aplica:** Owner quiere proponer una alternativa que NINGÚN agente generó vía cadena estándar. Caso típico: junta dice "ninguna de las opciones nos convence, exploremos D que no consideraron"; o Owner solo tiene una intuición desviada del análisis estándar.

**Pasos:**

1. **Owner crea archivo en `01-inbox/01-owner-to-raul/_alt-<descripcion>.md`** siguiendo `alternative-proposal-template.md`:
   - Qué se propone
   - Por qué (motivación + evidencia anecdótica si aplica)
   - Qué cadena estándar produciría diferente
   - A qué se opone explícitamente

2. **Raul detecta sufijo `_alt-`** en el archivo y enruta SIN PASAR por flujo CSC normal:
   - Primero a Bruna (risk assessment + ¿hay precedentes contra?)
   - Si Bruna OK: a Vera (¿es técnicamente factible?)
   - Si Vera OK: a Orlan (¿es competitivamente sensato?)
   - Si los 3 OK: regresa a Aurelio para integrar al plan + Owner aprueba final.

3. **Si cualquier agente flag riesgo:** se documenta en BR-1 + Owner decide override o descartar.

4. **Si aprobado:** se documenta en `DECISIONS.md` como entrada con label "Alternative path" + razón. Opción se integra al plan estándar.

**Por qué este patrón:**

Sin él, las alternatives ad-hoc del Owner generan ruido (cadena estándar las trata como tarea normal y produce análisis no relevante). Con el patrón explícito, las alts pasan por gates de validación apropiados (riesgo, técnica, mercado) sin desperdiciar producción CSC.

### A.3 — Patrón "Crisis override"

**Cuando aplica:** urgencia genuina (deadline corto, situación reactiva). Ej. junta convocada con 6 horas de aviso requiere material; regulador exige respuesta en 48h; competidor lanza algo que requiere counter-positioning rápido.

**Pasos:**

1. **Owner crea archivo `01-inbox/01-owner-to-raul/_urgent_<deadline>_<descripcion>.md`** con:
   - Deadline (fecha + hora explícitas)
   - Qué se necesita (output type)
   - Mínimo viable aceptable
   - Qué aspectos pueden saltarse vs cuáles NO

2. **Raul ignora cadena estándar.** Va directo al agente más relevante con SLA agresivo: "tenés Xh, aquí el contexto, producí mínimo viable".

3. **Agente produce sin pasar por gates de calidad estándar.** Output marcado `status: CRISIS-DRAFT` para distinguir de producción regular.

4. **Si hay claims sensibles**, Bruna hace pasada rápida (BR-3 quick) — preguntas binarias: "¿es defensible?" "¿hay precedente directo?". No análisis exhaustivo.

5. **Post-crisis (24-72h después):** Bruna hace post-mortem en BR-5 con:
   - Qué se decidió saltarse del flujo estándar
   - Qué riesgos quedaron sin gatear
   - Si emergen issues posteriores, qué remediación

6. **Si no emergen issues**, el output pasa de `CRISIS-DRAFT` a `APPROVED` y se integra a la documentación normal.

**Por qué este patrón:**

Sin él, las crisis o saltean el sistema completo (sin trazabilidad) o sobre-aplican rigor que no permite el deadline. El patrón da una válvula con disciplina de post-mortem.

### A.4 — Patrón "Multi-decision-maker convergence"

**Cuando aplica:** decisión que requiere aprobación combinada de múltiples decisores (ej. claim sensible que requiere Owner + junta + legal externo, o lanzamiento que requiere I&D + comercial + Owner).

**Pasos:**

1. **Agente generador identifica que multiple-stakeholder approval es necesaria.**

2. **Genera "convergence package"** con sub-paquetes uno por decisor (cada uno con su scope-relevante).

3. **Sistema registra una convergence-decision-id** que agrupa N sub-decisions paralelas.

4. **Cada sub-decision sigue patrón Pause+Resume** (A.1) en su canal.

5. **Sistema espera todas.** Estado: PARTIALLY-RESPONDED hasta que todas reportan.

6. **Cuando todas responden:**
   - Si todas APRUEBAN → cadena reanuda con luz verde.
   - Si alguna RECHAZA → cadena bloqueada; activa A.2 (alternative) o cierra como CLOSED-NOT-VIABLE.
   - Si CONFLICT entre decisores → escalación a Owner con summary de cada posición.

7. **Documentación final:** entrada en DECISIONS.md con quién aprobó / rechazó / conflicto-resuelto-cómo.

**Por qué este patrón:**

Cuando 3+ humanos deben firmar, sin estructura el proceso se vuelve "Owner persigue uno por uno y arma puzzle mental". El patrón explicita el sub-tracking y desbloquea solo cuando hay convergence real.

---

## B. Documentos canónicos nuevos

### B.1 — `04-system/03-governance/DECISION-MAKERS.md`

**Propósito:** registro central de quién tiene autoridad para decidir qué, con scope, canal preferido, SLA típico, y patrón de escalación. Consultado por agentes cuando llegan a decision gate para saber a quién enrutar.

**Schema (tabla):**

| Decisor | Tipo | Scope | Canal preferido | SLA típico | Escalación si timeout/no-response |
|---|---|---|---|---|---|
| Owner (Raoul) | Humano-individual | Decisiones arquitectónicas, estratégicas, de scope, override de cualquier otro decisor | `01-owner-to-raul/` | <24h cuando online; pausa cuando offline | N/A (Owner es máxima autoridad interna) |
| Junta Directiva Genteca | Humano-grupo | Decisiones estratégicas Genteca (productos, lanzamientos, capital), aprobaciones de campañas grandes | Presentación física + `05-from-junta/` para respuestas | 2-4 semanas (cadencia reuniones) | Owner mediates si urgente |
| Equipo I&D Genteca (Kike + Liliam principalmente) | Humano-grupo | Decisiones técnicas dispositivos, validación specs, escalación de riesgo de diseño | Email/whatsapp; future channel `colaboradores/Genteca/I-D/` | 1-7 días | Owner |
| Equipo comercial Genteca (Kike + ML + MPR vendedores) | Humano-grupo | Pricing, positioning, decisiones de canal comercial | Similar I&D | 3-7 días | Owner |
| SAPI Venezuela | Organismo-gov | Registro/oposición de marcas, clearances IP | Web SAPI (paralelo al sistema RAUL) | Meses (típico 6-12) | Legal externo cuando casos contenciosos |
| SENCAMER | Organismo-gov | Normas técnicas COVENIN, certificaciones | Web SENCAMER (paralelo) | Meses | Legal externo |
| FONDONORMA | Organismo-norm | Verificación normas, auditorías | Web FONDONORMA (paralelo) | Meses | Legal externo |
| Legal externo | Humano-individual | Casos sensibles claims, IP contencioso, contratos importantes | Email vía Owner | 3-7 días | N/A (Owner decide cuándo escalar) |
| Contraparte Panama (varios) | Humano-individual | Negociaciones apt Embassy Club, contratos, pagos | Email/WhatsApp; future channel `07-from-third-parties/Panama/` | Variable | Owner |
| Asesores Plenus (futuro) | Humano-grupo | Decisiones científicas/nutricionales sobre formulación | (sin canal aún) | TBD | Owner |
| Audiencia / mercado (vía investigación) | Humano-grupo (proxy) | Validación de mensaje vía estudio (ej. GME study) | Estudios de mercado encargados | Semanas-meses | N/A — datos, no decisión |

**Reglas de uso:**

1. Cuando un agente llega a decision gate, consulta esta tabla para identificar decisor + canal correcto.
2. Si el decisor no está en la tabla, escala a Owner para definir entrada nueva ANTES de proceder.
3. Cualquier modificación a esta tabla se registra en DECISIONS.md.
4. Cuando un decisor se vuelve obsoleto (ej. cambio de organigrama Genteca), se mueve a sección "Histórico" en este mismo doc, NO se borra.

**Sección "Histórico" (template):**

```
## Histórico de decisores (ya no activos)

| Decisor | Fecha activo | Razón cierre | Decisor sucesor |
|---|---|---|---|
| (vacío al inicio) | | | |
```

### B.2 — `04-system/03-governance/PENDING-DECISIONS-REGISTRY.md`

**Propósito:** kanban acumulativo de decisiones in-flight. Toda decisión que activa Pause+Resume se registra aquí. Permite Owner / agentes / cron tasks ver estado de cualquier decisión sin tener que escanear inbox.

**Schema (tabla acumulativa, append-only para historia):**

| Decision-ID | Project / Pieza | Agente solicitante | Decisor | Fecha solicitud | Estado | Deadline | Package | Respuesta |
|---|---|---|---|---|---|---|---|---|
| DEC-2026-05-09-001 | (siembra inicial) | (siembra) | (siembra) | 2026-05-09 | (siembra) | - | - | - |

**Estados posibles:**

| Estado | Significado | Próximo paso |
|---|---|---|
| `PENDING` | Solicitud entregada, esperando respuesta | Esperar / monitorear deadline |
| `IN-DELIBERATION` | Decisor confirmó que está trabajando en respuesta | Esperar SLA típico |
| `RESPONDED` | Respuesta recibida y registrada | Reanudar cadena del agente solicitante |
| `ESCALATED` | Pasó SLA típico sin respuesta, se escaló al next-level | Esperar nueva respuesta |
| `EXPIRED` | Deadline pasó sin respuesta. Decisión muerta. | Cerrar o reactivar como decision-id nuevo |
| `CLOSED-WITHDRAWN` | Owner / agente retiró la solicitud antes de respuesta | Documentar razón |
| `CLOSED-CONFLICT` | Multi-decisor: hubo conflicto, escalado a Owner | Owner resuelve, status pasa a RESPONDED con resolución Owner |

**Reglas de uso:**

1. **Append-only.** Decisiones cerradas (RESPONDED / EXPIRED / CLOSED-*) NO se borran de la tabla. Quedan como historial.
2. Cualquier agente que active Pause+Resume DEBE crear row aquí.
3. InboxBot lee este archivo en cada ciclo para detectar decisions con response esperada.
4. Owner puede agregar manualmente notas en columna extra "Owner notes" si necesita anotar contexto.
5. Cuando estado pasa a RESPONDED, agente solicitante registra el outcome + linka al deliverable resultante.

**Sección al final del doc:**

```
## Estadísticas (auto-generadas idealmente; manual por ahora)

- Total decisiones en flight (PENDING + IN-DELIBERATION + ESCALATED): N
- Total cerradas RESPONDED: N
- Total CLOSED-CONFLICT: N
- Tiempo promedio respuesta por decisor: tabla
```

---

## C. Status field convention en deliverables

**Propósito:** estandarizar un campo en frontmatter YAML de cada deliverable para que cualquier agente / Owner / cron task sepa de un vistazo en qué estado está esa pieza.

**Field nuevo en frontmatter:** `status`

**Valores posibles:**

| Status | Significado | Quién lo setea |
|---|---|---|
| `DRAFT` | En desarrollo, no terminado | Agente productor durante producción |
| `IN-REVIEW-INTERNAL` | Producido, esperando validación de gate interno (Bruna, Vera, Vael, etc.) | Agente productor cuando termina draft |
| `AWAITING-DECISION-<id>` | Bloqueado pending decisión externa identificada por id | Agente que activa Pause+Resume |
| `IN-REVIEW-OWNER` | Aprobado por gates internos, esperando luz verde Owner | Cualquier agente |
| `APPROVED` | Owner aprobó, listo para distribución | Owner |
| `PUBLISHED` | Distribuido / entregado al destino final | Ivo (post-publication) |
| `ARCHIVED` | Movido a 05-archive (proyecto cerrado o pieza obsoleta) | Sira / Owner |
| `CRISIS-DRAFT` | Producido bajo Crisis override, pending post-mortem | Agente que produjo bajo crisis |
| `WITHDRAWN` | Cancelado antes de publicación (por Owner / por riesgo) | Owner / Bruna |

**Reglas:**

1. **Todo deliverable producido por agente** debe tener `status` field. (Migración gradual aceptable — pieces existentes pueden quedar sin field; nuevas piezas SÍ deben tenerlo.)
2. Solo el `status` field es obligatorio. Si un deliverable es viejo y no tiene este field, asume `APPROVED` (default conservador).
3. Cuando un deliverable cambia de estado, se actualiza el field + opcional log entry abajo.
4. Cuando estado es `AWAITING-DECISION-<id>`, debe haber row correspondiente en `PENDING-DECISIONS-REGISTRY.md`.

---

## D. Folder structure nueva en `01-inbox/`

**Estructura propuesta:**

```
01-inbox/
├── 01-owner-to-raul/                   ← (existente)
├── 02-deliverables-to-owner/            ← (existente)
├── 03-raw-sources/                      ← (existente)
├── 04-decisions-in-flight/              ← NUEVO
│   ├── _index.md                        ← lista activa de decision packages
│   └── <project-id>/
│       └── <decision-id>/
│           ├── context.md               ← qué proyecto / qué pieza está bloqueada
│           ├── package.md               ← request al decisor
│           ├── options.md               ← alternativas con trade-offs
│           ├── recommendation.md        ← lo que el agente recomienda
│           └── response.md              ← (vacío hasta que llega respuesta)
├── 05-from-junta/                       ← NUEVO
│   ├── _index.md                        ← histórico de presentations + responses
│   ├── _outgoing/                       ← packages enviados a junta
│   └── <fecha>_<decision-id>_response.md  ← respuestas que llegan
├── 06-from-regulators/                  ← NUEVO
│   ├── _index.md
│   ├── _outgoing/                       ← submissions a SAPI/SENCAMER/FONDONORMA
│   └── <regulator>_<fecha>_<id>.md      ← respuestas recibidas
├── 07-from-third-parties/               ← NUEVO
│   ├── _index.md
│   └── <party-name>/
│       ├── _outgoing/
│       └── <fecha>_<topic>.md
└── 08-special-deliverables/             ← NUEVO
    ├── _index.md                        ← registro de overflow
    └── <fecha>_<descripcion>.md         ← entregables one-off
```

**Convenciones:**

- Decision-IDs siguen formato `DEC-YYYY-MM-DD-NNN` (NNN = secuencial dentro del día).
- `_outgoing/` carpeta indica "enviado al humano externo, esperando respuesta".
- Filename de respuestas linkeable a decision-id permite InboxBot parsear.
- `_index.md` por carpeta lista activos + cerrados (lite version del registry, scoped por canal).

**Política de retención:**

- Decisiones cerradas (RESPONDED / EXPIRED / CLOSED-*) viven aquí 90 días después de cierre, luego se mueven a `05-archive/04-decisions-history/<año>/`.
- `_outgoing/` se limpia 30 días después de respuesta recibida.
- Special-deliverables se archivan 60 días después de producción.

---

## E. Templates en `04-system/04-tools-and-scripts/templates/`

### E.1 — `decision-request-template.md`

```markdown
---
decision_id: DEC-YYYY-MM-DD-NNN
project: <project-id>
piece: <pieza-bloqueada>
agent_requesting: <nombre-agente>
decisor: <de DECISION-MAKERS.md>
date_request: YYYY-MM-DD
deadline: YYYY-MM-DD (o "open" si no hay deadline)
canal: <canal correcto per DECISION-MAKERS>
status: PENDING
---

# Decision Request — <título corto>

## Contexto

<por qué esta decisión es necesaria, qué proyecto/pieza está bloqueada, urgencia>

## Opciones

### Opción A — <nombre>
- **Qué propone:** ...
- **Pros:** ...
- **Contras:** ...
- **Caveats:** (literal de Bruna si aplica)

### Opción B — <nombre>
[mismo formato]

### Opción C — <nombre>
[mismo formato]

## Recomendación del agente solicitante

<cuál opción + por qué + qué riesgos asume>

## Información que necesitamos recibir de vuelta

1. <pregunta específica>
2. <pregunta específica>
3. (si conflicto entre opciones, qué criterio de tiebreak prefiere el decisor)

## Trazabilidad

- Cadena CSC origen: <links a inputs Vera/Orlan/Vael/etc>
- BR-X relacionados: <links>
- DECISIONS.md entries previas: <si aplica>
```

### E.2 — `alternative-proposal-template.md`

```markdown
---
alt_id: ALT-YYYY-MM-DD-NNN
proposed_by: Owner | <agente>
date: YYYY-MM-DD
opposes_chain_output: <link a output de cadena estándar que se está desafiando>
status: PROPOSED
---

# Alternative Proposal — <título corto>

## Qué se propone

<descripción clara de la alternativa>

## Por qué (motivación)

<racional, evidencia, intuición — explícito sobre qué tipo de soporte tiene>

## Qué cadena estándar produciría diferente

<comparación: la cadena estándar generaría X, esta propuesta es Y, diferencia es Z>

## A qué se opone explícitamente

<si la propuesta contradice análisis previo de Vera/Orlan/Bruna, hacerlo explícito y dar razón>

## Validaciones requeridas (auto-routing)

- [ ] Bruna risk assessment
- [ ] Vera technical feasibility
- [ ] Orlan competitive sensibility
- [ ] (otros si aplican)

## Resolución (a llenar después de validaciones)

<una vez los gates corren: aprobada / aprobada con modificaciones / rechazada con razón>
```

### E.3 — `regulator-submission-template.md`

```markdown
---
submission_id: REG-YYYY-MM-DD-NNN
regulator: SAPI | SENCAMER | FONDONORMA | OTRO
project: <project-id>
piece: <pieza-relacionada>
date_submission: YYYY-MM-DD
expected_response_date: YYYY-MM-DD
legal_external_involved: yes | no
status: SUBMITTED | IN-REVIEW | RESPONDED | OBJECTED | APPROVED | REJECTED
---

# Regulator Submission — <regulador> — <título>

## Submission

<contenido del filing — formato per regulador>

## Anexos

<lista de docs anexos, links si están en el repo>

## Tracking

- Fecha submission: YYYY-MM-DD
- Acuse recibo: <fecha + ref-id del regulador>
- Próxima acción esperada: <ej. "respuesta SAPI en ~6 meses">
- Escalación si no hay respuesta para: <fecha>

## Resolución

<contenido cuando llega respuesta del regulador>
```

### E.4 — `junta-decision-package-template.md`

```markdown
---
package_id: JUNTA-YYYY-MM-DD-NNN
junta: Junta-Directiva-Genteca | Junta-otra-entidad
project: <project-id>
date_presented: YYYY-MM-DD
meeting_reference: <ref-reunión-junta>
status: PRESENTED | IN-DELIBERATION | RESPONDED-APPROVED | RESPONDED-REJECTED | RESPONDED-MODIFIED
---

# Junta Decision Package — <título>

## Resumen ejecutivo (1 página máximo)

<para junta — qué decisión necesitamos, opciones principales, recomendación, qué pasa si no deciden hoy>

## Contexto operativo

<qué proyecto, qué cadena CSC produjo el insumo, qué ya se aprobó previamente>

## Opciones presentadas

[mismo formato que decision-request-template, con detalle suficiente para junta]

## Recomendación del sistema /RAUL/

<cuál opción + por qué — agregar caveats Bruna y validaciones Vera/Orlan>

## Lo que NO podemos decidir aquí

<flag si hay sub-decisiones que requieren otro decisor — escala a Multi-decision-maker convergence>

## Acta de respuesta (a llenar post-reunión)

- Fecha respuesta: YYYY-MM-DD
- Decisión: <opción aprobada / modificación / rechazo>
- Conditions / caveats agregados por junta: <texto literal>
- Next steps assigned: <a quién, qué, cuándo>
```

---

## F. Modificaciones a InboxBot AGENT.md

InboxBot necesita aprender 3 capacidades nuevas. Cambios mínimos a AGENT.md:

### F.1 — Detectar respuestas en canales nuevos

Añadir a la tabla de Canales (sección "Canales monitoreados"):

| Canal | Path | Estado |
|---|---|---|
| Junta directiva responses | `01-inbox/05-from-junta/<filename>.md` (excluir `_outgoing/` y `_index.md`) | Activo |
| Regulator responses | `01-inbox/06-from-regulators/<filename>.md` | Activo |
| Third-party responses | `01-inbox/07-from-third-parties/<party>/<filename>.md` | Activo |

### F.2 — Parsear decision-id de filename

Añadir a la sección "Algoritmo de ejecución" (entre Paso 1 y Paso 2):

> **Paso 1.5 — Identificación de tipo de tarea:**
>
> Para cada archivo encontrado en canales nuevos (05/06/07):
> 1. Extraer decision-id del filename si match pattern `(DEC|JUNTA|REG|ALT)-YYYY-MM-DD-NNN`.
> 2. Si match: tipo = "decision-response"; load decision-id, look up en `PENDING-DECISIONS-REGISTRY.md`, identificar agente solicitante.
> 3. Si no match: tipo = "general-input" (procesar como tarea Owner-equivalente).

### F.3 — Reentry pattern

Añadir al algoritmo después del Paso 5d (Gmail draft):

> **Paso 6 — Reentry para decision-responses:**
>
> Si tipo == "decision-response":
> 1. Update `PENDING-DECISIONS-REGISTRY.md`: cambiar estado a RESPONDED, llenar columna response con link al archivo.
> 2. Identificar agente solicitante de la row.
> 3. Invocar Raul orchestrator con briefing: "Decision DEC-XXX RESPONDED. Reanudar producción de <pieza-bloqueada>. Respuesta del decisor en `<file>`. Agente original: <nombre>."
> 4. Cadena reanuda en agente original con la decisión incorporada.

### F.4 — Detección de status AWAITING-DECISION

Añadir al Paso 4 (Recibir resultado de Raul):

> Si Raul devuelve `Status propuesto: AWAITING-DECISION-<id>` (en lugar de los actuales EN-PROCESO / APROBADO-PARA-X):
> 1. NO entregar a outbox como deliverable final.
> 2. En su lugar: leer el package generado (que debería estar en `01-inbox/04-decisions-in-flight/<project>/<decision-id>/`).
> 3. Verificar que entry existe en `PENDING-DECISIONS-REGISTRY.md`.
> 4. Crear Gmail draft al Owner con resumen del package + indicación de qué decisor + canal de respuesta esperado.
> 5. NO crear DONE marker hasta que la decisión sea RESPONDED.

**Restricción crítica:** modificar AGENT.md vía Read+Edit (memoria 2026-04-25). Nunca Write.

---

## G. Plan de migración inicial (siembra)

**Objetivo:** poblar `PENDING-DECISIONS-REGISTRY.md` con decisiones actualmente "in-the-air" para tener trazabilidad desde día 1.

**Decisiones a migrar (identificadas en sesión 2026-05-09 o memoria):**

| Decision-ID | Project | Solicitante | Decisor | Fecha origen | Estado actual real | Notas |
|---|---|---|---|---|---|---|
| DEC-2026-05-04-001 | GSM-MB-RB-RF empaque | Owner | Junta Directiva Genteca | 2026-05-04 | RESPONDED (junta eligió Línea 2) | Convergence con I&D para WhatsApp Kike-Canudas |
| DEC-2026-05-06-001 | GME protector monofásico | Bruna | Owner + I&D | 2026-05-06 | PENDING (escalación riesgo de diseño) | Memoria menciona "discusión engineering pendiente" |
| DEC-2026-05-06-002 | GME claim "primero LATAM" | Bruna | Owner | 2026-05-06 | SUSPENDIDO (segunda iteración OL-3 + confirmación specs) | per BR-2 entry #15 |
| DEC-2026-05-08-001 | Marcas anglicismos junta | Owner | Junta Directiva + SAPI | 2026-05-08 | PARTIALLY-RESPONDED (junta pending; SAPI no submitted) | 3 escalaciones críticas Owner pendientes per memoria |
| DEC-2026-05-03-001 | COVENIN 3445 verification | Bruna | SENCAMER/FONDONORMA + Legal | 2026-05-03 | PENDING (Argumento 8 bloqueado) | per BR-2 entry #28 |
| DEC-2026-04-29-001 | GST-RD product clarity | Owner | I&D Genteca (Kike) | 2026-04-29 | CLOSED-WITHDRAWN (canal C — esperar evidencia natural) | per DECISIONS 2026-05-08 D3 |
| DEC-2026-05-08-D1 a D5 | GST Labels owner decisions | Owner (auto) | Owner | 2026-05-04 | PENDING | 5 decisiones Owner pendientes per memoria |

**Acción:** primer commit del registry incluye estas filas como semilla. Decisiones futuras se appendean.

**Decisión Owner recomendada:** revisar la tabla anterior, confirmar si todas las entries son correctas, y agregar las que falten que recordés. Cualquier decisión "viva" debe entrar.

---

## H. Validation checklist (post-implementación)

Para validar que el sistema nuevo funciona correctamente, después de implementar:

- [ ] DECISION-MAKERS.md creado con todos los decisores conocidos.
- [ ] PENDING-DECISIONS-REGISTRY.md creado con siembra inicial (G).
- [ ] 5 carpetas nuevas en `01-inbox/` con `_index.md` cada una.
- [ ] 4 templates en `04-system/04-tools-and-scripts/templates/`.
- [ ] InboxBot AGENT.md actualizado con 4 modificaciones (F.1-F.4) — Read+Edit.
- [ ] Status field convention documentada en `NAMING-CONVENTIONS.md` o doc separado.
- [ ] Test con una decisión real: pasar un caso por Pause+Resume end-to-end.
- [ ] DECISIONS.md actualizado con entrada cubriendo la implementación.
- [ ] Memoria actualizada con pointers al nuevo sistema (entry tipo "feedback" sobre cómo usar).

---

## I. Alternativas consideradas + razones de rechazo

**Alt-1: Usar herramientas externas (Notion / Linear / Trello) para tracking de decisiones.**
- ❌ Rechazado: viola principio local-first / vendor-neutral. Crea dependencia externa. Sincronización entre sistemas es fricción permanente.

**Alt-2: Solo modificar DECISIONS.md existente para incluir pendings.**
- ❌ Rechazado: DECISIONS.md es log-permanente para arquitectónicas; mezclar pendings operacionales contamina la semántica. Mejor doc separado.

**Alt-3: Crear un agente especializado "Decision Coordinator" en lugar de patrones.**
- ❌ Rechazado: agrega complejidad de un nuevo agente sin valor neto vs documentación de patrones que cualquier agente existente puede ejecutar. Bruna + Aurelio + InboxBot juntos cubren las necesidades.

**Alt-4: Bypass channel único (`08-special-deliverables/`) sin diferenciar junta/regulator/third-party.**
- ❌ Rechazado: cada canal tiene SLA diferente y formato distinto de respuesta. Mezclarlos genera fricción de procesamiento. Mejor canales separados con _index.md por canal.

**Alt-5: Hacer la implementación en una sola sesión vs incremental.**
- ❌ Rechazado: scope grande, mejor incremental. Cada componente (DECISION-MAKERS, REGISTRY, folders, templates, InboxBot mods) es independiente. Owner puede aprobar y ejecutar uno por uno.

**Alt-6: Auto-detection de decision gates por keywords en outputs (sin convention explícita de status field).**
- ❌ Rechazado: keywords son frágiles. Convention explícita de status YAML field es robusta y auto-documentada.

**Alt-7: Permitir que cualquier agente actualice PENDING-DECISIONS-REGISTRY.**
- ❌ Rechazado: append-only por agente solicitante, update-only por InboxBot. Reduce conflictos de escritura concurrente.

---

## J. Recomendación de orden de ejecución

Si Owner aprueba la totalidad, sugiero ejecutar incremental en este orden (cada paso commiteable independiente):

1. **Crear DECISION-MAKERS.md** — independiente, sin dependencias. Útil inmediatamente como referencia.
2. **Crear PENDING-DECISIONS-REGISTRY.md** con siembra (sección G). Útil para Owner consultar estado de pendientes.
3. **Crear 5 nuevas carpetas en `01-inbox/` con `_index.md`**.
4. **Crear 4 templates en `04-system/04-tools-and-scripts/templates/`**.
5. **Modificar InboxBot AGENT.md** (F.1-F.4) — Read+Edit, gradual.
6. **Documentar status field convention** en NAMING-CONVENTIONS.md.
7. **Actualizar DECISIONS.md** con entrada cubriendo la implementación.
8. **Update MEMORY.md** — entry feedback sobre cómo usar el sistema.

Pasos 1-4 son docs/files puros, ~30 min total.
Paso 5 requiere cuidado por restricción Read+Edit, ~20 min.
Pasos 6-8 son cleanup, ~15 min.

**Total ejecución estimado: ~1 hora.**

---

## K. Próximos pasos (después de Owner review)

1. Owner revisa este doc completo. Anota:
   - Qué se aprueba.
   - Qué se modifica (con detalle del cambio deseado).
   - Qué se rechaza (con razón).
   - Qué falta (gap no cubierto en propuesta).

2. Conversación de ajustes (1 sesión).

3. Ejecución incremental de pasos aprobados (1-2 sesiones).

4. Test con caso real (1 decisión que pase end-to-end).

5. Iterar / ajustar según test.

---

**Estado del doc:** propuesta completa, pending Owner review. NO es ejecutable hasta aprobación. Cada componente es independiente — Owner puede aprobar parcialmente.
