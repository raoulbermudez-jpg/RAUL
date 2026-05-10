---
package_id: JUNTA-YYYY-MM-DD-NNN
junta: JUNTA-GENT  # JUNTA-GENT | <otra-junta-si-aplica>
project: <project-id>
linked_decision_id: DEC-YYYY-MM-DD-NNN  # decision_id en PENDING-DECISIONS-REGISTRY
date_presented: YYYY-MM-DD
meeting_reference: <ref-reunión-junta — ej. "Reunión ordinaria mayo 2026" o "Convocatoria extraordinaria 2026-05-15">
status: PRESENTED  # PRESENTED | IN-DELIBERATION | RESPONDED-APPROVED | RESPONDED-REJECTED | RESPONDED-MODIFIED
---

# Junta Decision Package — <título>

## Resumen ejecutivo (1 página máximo)

<para junta — qué decisión necesitamos, opciones principales, recomendación, qué pasa si no deciden hoy>

> Crítico: este resumen es lo único que algunos miembros de junta van a leer. Debe poder leerse en <2 minutos y dejar la pregunta clara: ¿qué tienen que decidir HOY?

## Contexto operativo

<qué proyecto, qué cadena CSC produjo el insumo, qué ya se aprobó previamente>

- **Proyecto:** <project-id> — <descripción de 1 línea>
- **Origen del análisis:** <cadena CSC: research → Orlan → Vera → Vael → Aurelio → ...>
- **Decisiones previas relacionadas:** <DECISIONS.md entries que esta decisión modifica o complementa>
- **Decisor único o convergence:** <si esta decisión requiere también otros decisores per A.4, mencionarlo>

## Opciones presentadas

### Opción A — <nombre>

- **Qué propone:** ...
- **Pros para Genteca:** ...
- **Contras / riesgos:** ...
- **Implicaciones financieras estimadas:** <si aplica>
- **Caveats Bruna:** (literal)
- **Validación Vera:** <APPROVED / CONDITIONED + qué condición>
- **Validación Orlan:** <competitive sense + dato de mercado relevante>

### Opción B — <nombre>

[mismo formato]

### Opción C — <nombre>

[mismo formato si aplica]

## Recomendación del sistema /RAUL/

<cuál opción + por qué — agregar caveats Bruna y validaciones Vera/Orlan>

> La recomendación es *del sistema*, no del Owner ni de un agente individual. Debe ser defendible si junta cuestiona el racional.

## Lo que NO podemos decidir aquí

<flag si hay sub-decisiones que requieren otro decisor — escala a Multi-decision-maker convergence A.4>

- **Sub-decisión 1:** <descripción> — requiere <decisor> en <plazo>
- **Sub-decisión 2:** ...

> Esta sección protege a junta de aprobar algo que en realidad requiere validación regulatoria, técnica o legal aún no completada.

## Acta de respuesta (a llenar post-reunión)

- **Fecha respuesta:** YYYY-MM-DD
- **Decisión:** <opción aprobada / modificación / rechazo>
- **Conditions / caveats agregados por junta:** <texto literal>
- **Asistentes que votaron:** <lista>
- **Disensos / abstenciones:** <si los hubo, registrarlos>
- **Next steps assigned:** <a quién, qué, cuándo>
- **Sub-decisiones que junta delegó:** <a quién decisor — alimenta nuevo Decision-ID si aplica>

---

_Instrucciones de uso: guardar como `<decision-id>_<descripcion>.md` en `01-inbox/05-from-junta/_outgoing/`. El package físico (deck PPTX si aplica) se mantiene aparte para presentación; este .md sirve como registro estructurado del package + acta de respuesta. Cuando llegue acta formal post-reunión, depositar también en `01-inbox/05-from-junta/<fecha>_<decision-id>_response.md` para que InboxBot detecte y actualice `PENDING-DECISIONS-REGISTRY.md`._

_Template v1.0 — 2026-05-09 — Phase 3 step 4_
