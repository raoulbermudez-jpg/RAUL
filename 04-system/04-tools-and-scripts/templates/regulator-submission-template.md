---
submission_id: REG-YYYY-MM-DD-NNN
regulator: SAPI-VE  # SAPI-VE | SENCAMER | FONDONORMA | OTRO
project: <project-id>
piece: <pieza-relacionada>
linked_decision_id: DEC-YYYY-MM-DD-NNN  # decision_id en PENDING-DECISIONS-REGISTRY que esta submission resuelve
date_submission: YYYY-MM-DD
expected_response_date: YYYY-MM-DD  # estimado per SLA típico del regulador (meses)
legal_external_involved: yes  # yes | no — debe ser "yes" para submissions formales (regla del canal 06-from-regulators/)
status: SUBMITTED  # SUBMITTED | IN-REVIEW | RESPONDED | OBJECTED | APPROVED | REJECTED
---

# Regulator Submission — <regulator> — <título>

## Submission

<contenido del filing — formato per regulador>

> Estructura del contenido depende del regulador:
> - **SAPI-VE** (marcas): clase Niza, denominativo / mixto, descripción de productos/servicios, declaración de uso, reproducción del signo.
> - **SENCAMER** (certificación): producto, normas COVENIN aplicables, ensayos realizados, evidencia de cumplimiento.
> - **FONDONORMA** (auditoría QMS): scope del sistema, evidencia documental, cronograma de auditoría.

## Anexos

<lista de docs anexos, links si están en el repo>

- [ ] <doc 1>: <ruta o ref externo>
- [ ] <doc 2>: <ruta o ref externo>
- [ ] Clearance LEGAL-EXT: <fecha + ref del estudio jurídico>
- [ ] BR-X de Bruna que aprobó claims: <link>

## Tracking

- **Fecha submission:** YYYY-MM-DD
- **Acuse recibo:** <fecha + ref-id del regulador — ej. número de expediente SAPI>
- **Próxima acción esperada:** <ej. "respuesta SAPI en ~6 meses, observaciones formales si las hay">
- **Escalación si no hay respuesta para:** YYYY-MM-DD
- **Owner notes:** <contexto adicional, conversaciones informales con el regulador, etc.>

## Resolución

<contenido cuando llega respuesta del regulador>

- **Fecha respuesta:** YYYY-MM-DD
- **Outcome:** <APPROVED / OBJECTED / REJECTED / requested-modifications>
- **Texto literal de la respuesta:** <transcripción si es relevante para Bruna>
- **Conditions / observaciones:** <qué pidió el regulador para aprobar, si aplica>
- **Próximos pasos:** <re-submission con mods / aceptar como aprobado / apelación / abandonar>
- **Bruna update:** <BR-X registrando que el claim quedó habilitado / bloqueado>

---

_Instrucciones de uso: guardar como `<regulator>_<fecha>_<decision-id>_submission.md` en `01-inbox/06-from-regulators/_outgoing/`. Cuando llegue notificación del regulador, depositar respuesta en `01-inbox/06-from-regulators/<regulator>_<fecha>_<decision-id>.md` (raíz del canal); InboxBot detecta y actualiza `PENDING-DECISIONS-REGISTRY.md` a `RESPONDED`. NUNCA submission sin clearance previo de LEGAL-EXT y Bruna._

_Template v1.0 — 2026-05-09 — Phase 3 step 4_
