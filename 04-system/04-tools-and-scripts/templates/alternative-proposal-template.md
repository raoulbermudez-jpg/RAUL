---
alt_id: ALT-YYYY-MM-DD-NNN
proposed_by: Owner  # Owner | <nombre-agente>
date: YYYY-MM-DD
opposes_chain_output: <link a output de cadena estándar que se está desafiando>
status: PROPOSED  # PROPOSED | IN-VALIDATION | APPROVED | APPROVED-WITH-MODS | REJECTED
---

# Alternative Proposal — <título corto>

## Qué se propone

<descripción clara de la alternativa — qué se haría diferente vs lo que la cadena estándar produciría>

## Por qué (motivación)

<racional, evidencia, intuición — explícito sobre qué tipo de soporte tiene>

- Tipo de evidencia: [analítica / anecdótica / intuición / dato externo / feedback de tercero]
- Fuente: <quién/qué motiva esta alternativa>

## Qué cadena estándar produciría diferente

<comparación: la cadena estándar generaría X, esta propuesta es Y, diferencia es Z>

| Aspecto | Cadena estándar | Esta propuesta |
|---|---|---|
| <ej. mensaje> | <X> | <Y> |
| <ej. canal> | <X> | <Y> |
| <ej. tono> | <X> | <Y> |

## A qué se opone explícitamente

<si la propuesta contradice análisis previo de Vera/Orlan/Bruna, hacerlo explícito y dar razón>

- Contradice análisis de: <agente + entry-id>
- Razón para contradecirlo: <por qué el solicitante cree que el análisis previo no aplica o es insuficiente>

## Validaciones requeridas (auto-routing)

InboxBot detecta sufijo `_alt-` en filename y enruta al gate correcto antes de ejecutar:

- [ ] **Bruna** risk assessment — ¿hay precedentes en BR-5 que bloqueen esto?
- [ ] **Vera** technical feasibility — ¿es técnicamente factible?
- [ ] **Orlan** competitive sensibility — ¿es competitivamente sensato?
- [ ] (otros si aplican: Vael coherencia narrativa, Aurelio impacto en plan)

## Resolución (a llenar después de validaciones)

<una vez los gates corren: aprobada / aprobada con modificaciones / rechazada con razón>

- **Bruna:** <APPROVED / CONDITIONED / REJECTED + razón>
- **Vera:** <APPROVED / CONDITIONED / REJECTED + razón>
- **Orlan:** <APPROVED / CONDITIONED / REJECTED + razón>
- **Decisión final Owner:** <integrar al plan / descartar / modificar>

## Si aprobada — integración al flujo

- DECISIONS.md entry con label "Alternative path": <link>
- Cambio en plan estándar: <qué se modifica>
- Decision-ID asociada (si activa Pause+Resume): <DEC-YYYY-MM-DD-NNN>

---

_Instrucciones de uso: guardar como `_alt-<descripcion>.md` en `01-inbox/01-owner-to-raul/`. El sufijo `_alt-` activa el routing especial que pasa por gates Bruna→Vera→Orlan ANTES de incorporar al flujo CSC normal. Si Owner es el solicitante, frontmatter `proposed_by: Owner`._

_Template v1.0 — 2026-05-09 — Phase 3 step 4_
