---
document_id: "GOVERNANCE-DIAGNOSTIC-2026-05-09"
document_type: "diagnostic-and-proposal-sketch"
author: "Claude Opus 4.7 (sesión Owner 2026-05-09)"
creation_date: "2026-05-09"
purpose: "Diagnóstico del estado actual de gates, caveats, decisiones humanas, alternate paths e inbox/outbox structure en el sistema /RAUL/. Sketch preliminar de propuesta arquitectónica para Phase 2."
audience: ["Raoul Bermúdez (Owner)", "Claude Opus 4.7", "Agentes de governance (Bruna, Aurelio)"]
status: "diagnostic-stage"
ssot_for: []
depends_on: ["DECISIONS.md", "RISK-POLICY.md", "agents/conceptual/*.md"]
version: "1.0"
how_to_use: "Anchor para diseño de Phase 2 (propuesta arquitectónica). Re-leer antes de discusión de propuesta. Si emergen gaps adicionales durante uso, añadir al final como apéndice."
---

# Diagnóstico de governance — Sistema /RAUL/ — 2026-05-09

## Origen

Pregunta del Owner durante sesión 2026-05-09:

> Me gustaría hacer una revisión de cómo está repo Raul respecto a gates de chequeo, caveats, rigurosidad para resultados impecables con las advertencias requeridas, requisitos para continuar (algunos provienen de decisiones de humanos, otros de terminar un proceso pendiente de un agente que debe entregar algún resultado o decisión a otro agente, mientras en medio hay decisión de humano — bien sea Owner, miembros de junta directiva, tercero, organismo gubernamental, entre otros). Después del diagnóstico, propuesta para estructurar caminos alternos que permitan buscar autorizaciones, convencer a humanos, presentar trabajo intermedio a la junta buscando alternativas no exploradas, introducir cambios, presentar rutas diferentes a decisores — sin corromper la estructura sólida y funcional ni los flujos de trabajo. Y estructurar adecuadamente carpetas de entrada/salida para deliverables especiales que bypass procedimientos del flujo estandarizado entre agentes, sin desorganizar.

Diagnóstico precede a propuesta arquitectónica (Phase 2). Esta entrega documenta SOLO el estado actual y gaps identificados.

---

## Marco — 5 dimensiones evaluadas

1. **Gates explícitos** — checkpoints estructurados antes/durante/después de producción.
2. **Caveat handling** — preservación literal de advertencias a lo largo de cadenas.
3. **Decision tracking** — captura de decisiones tomadas (y pendientes).
4. **Alternate paths / bypass** — rutas no-estándar en flujos.
5. **Inbox/outbox structure** — canales de entrada/salida con humanos no-Owner.

---

## 1. Gates explícitos — SÓLIDO

Cada agente clave tiene un set de outputs codificados (X-1 a X-5) que funcionan como gates. Pueden ser **producción gates** (entrega antes de pasar a siguiente capa) o **decision gates** (aprobación antes de continuar).

| Capa | Agente | Gate codes | Función | Decisor |
|---|---|---|---|---|
| Riesgo / Claims | **Bruna** | BR-1 a BR-5 | Aprobación claims públicos, precedentes transversales | Bruna autónoma + escalación Owner si sensitive; legal externo para SAPI/COVENIN/regulatorios |
| Estrategia contenido | **Aurelio** | AU-1 a AU-5 | Plan campaña, briefs CSC, recomendación reciclaje | Aurelio + Owner |
| Mensaje / brand | **Vael** | VA-1 a VA-5 | Messaging framework, positioning, guardrails | Vael + Owner |
| Verdad técnica | **Vera** | (VE-X de Vela usa otro código) | Selección dispositivos, normas IEC/UL/COVENIN | Vera + escalación I&D Genteca (Kike, Liliam) |
| Mercado | **Orlan** | OL-1 a OL-5 | Competencia, claim feasibility, innovation radar | Orlan |
| Producción CSC | Atlas, Luma, Vela, Orfeo, Solenne, Nerea, Oz, Renzo | AT-X, LU-X, VE-X, OR-X, SO-X, NE-X, varios | Ejecución de piezas finales | Cada agente productor |
| Distribución | **Ivo** | IV-1 a IV-5 | Logging cadena, rutas finales, feeds Sira/Celeste | Ivo |
| Archivado | **Sira**, **Celeste** | (sin codificación X) | Catálogo / KB persistencia | Sira (reciclaje), Celeste (KB largo plazo) |

**Patrón sólido observado:**
- Cada agente cierra outputs con sección "Supuestos y límites" (dependencies + escalations explícitas).
- "Mini-cover note" obligatoria por entrega (Solenne SO-5, Nerea NE-X) con trazabilidad VA-X / BR-X / fuentes.
- Gates BR-2 y BR-5 son acumulativos (logs permanentes).

**Veredicto:** la maquinaria de gates está bien construida. No hay déficit de checkpoints en producción de contenido.

---

## 2. Caveat handling — SÓLIDO

**Lo que funciona:**
- Bruna establece caveats literales palabra por palabra en BR-2.
- Vael los incorpora al messaging framework (VA-5 guardrails).
- Solenne/Nerea/Atlas/Luma/Vela/Orfeo respetan caveats sin reformulación.
- BR-5 acumula precedentes transversales en `04-system/03-governance/BR-5_*.md`.
- BR-2 acumula decisiones por dominio en `03-projects/<dominio>/_governance/`.

**Patrón observado:** "caveat travels with content". Una vez Bruna aprueba claim con caveat literal, ese caveat NO se modifica downstream — se preserva textual hasta la pieza final.

**Veredicto:** disciplina de caveats es robusta. Lo que falta NO es caveat handling sino los puntos donde el flujo se cruza con humanos NO-Owner.

---

## 3. Decision tracking — PARCIAL

### Lo que existe

- **`04-system/03-governance/DECISIONS.md`** — log permanente de decisiones arquitectónicas y de proceso. Inmutable salvo updates explícitos.
- **`03-projects/<dominio>/_governance/<fecha>_<dominio>_claim-approval-log_*.md`** — BR-2 logs por dominio.
- **`04-system/03-governance/BR-5_*.md`** — precedentes transversales.
- **`04-system/03-governance/task-log.md`** — log de delegaciones y outcomes.
- **`04-system/03-governance/inboxbot-tasklog.md`** — log de InboxBot.
- Cada agente productor cierra entrega con "mini-cover note" trazando inputs.

### Lo que NO existe

| Gap | Impacto |
|---|---|
| ❌ **Registro de decisiones-pendientes** (kanban de "X waiting for Y to decide") | Tareas se pausan sin trazabilidad clara. Owner debe recordar qué quedó pendiente con quién. |
| ❌ **Catálogo de decision-makers** (Owner, junta directiva Genteca, equipo I&D Kike+ML, SAPI, SENCAMER, FONDONORMA, legal externo, contraparte Panama, etc.) — quién puede decidir qué | Cada caso re-inventa "a quién le preguntamos esto". Sin estandarización. |
| ❌ **Estado "AWAITING-DECISION" en deliverables** | No hay forma estándar de marcar un output como "completo pero bloqueado pending external input". |
| ❌ **Mecanismo de reentry** después de decisión externa | Cuando junta decide, NO hay puente automático de "decisión recibida" → "reanudar cadena en este agente". Manual + ad-hoc. |
| ❌ **Deadlines / SLAs por decision-maker** | Sin métrica de cuánto tarda cada tipo de decisión, no se planifica con realismo. |

**Síntoma observado en sesión:** durante el ciclo de auditoría, varias entradas DECISIONS quedaron con "Pendiente acción Owner Drive web" sin estructura formal de "cuándo se cierra esto y dónde se registra el resultado". Se manejó bien por la sesión continua, pero un cron remoto NO podría hacerlo.

---

## 4. Alternate paths / bypass — CASI INEXISTENTE

### Patrones existentes (limitados)

- **Aurelio rechaza briefs saturantes con contrapropuesta + trade-offs** → micro-versión de alternative path, pero solo dentro del scope de Aurelio.
- **"Supuestos y límites"** en outputs deja explícitas las assumptions revisables → permite challenges, pero NO los estructura.
- **Argumentos rechazados (BR-1)** quedan registrados con razón, pero NO hay flujo para "esto fue rechazado, propongamos alternativa B".

### Gaps críticos

| Gap | Síntoma |
|---|---|
| ❌ **Owner-driven alternative pattern** | Owner no tiene mecanismo formal para decir "antes de seguir cadena, quiero presentar 3 opciones a junta y que ELLOS elijan, no la cadena". Hoy se hace ad-hoc. |
| ❌ **Junta-driven alternative pattern** | Si junta dice "hagan opción C que ningún agente propuso", ¿cómo se inyecta esa propuesta en la cadena para validación de riesgo (Bruna), técnica (Vera), mercado (Orlan)? Manual. |
| ❌ **Regulator-driven alternative pattern** | Si SAPI/SENCAMER pide cambios en certificados, ¿cómo entra esa exigencia al sistema? Hoy ad-hoc. |
| ❌ **Crisis / urgent override** | Sin protocolo para "crisis — tenemos 4 horas para responder, salteamos cadena estándar". |
| ❌ **Multi-decision-maker convergence** | Cuando una decisión necesita aprobación combinada (ej. Owner + junta + legal), no hay estructura para coordinar votos/aprobaciones. |

---

## 5. Inbox/outbox structure — SESGO OWNER-CÉNTRICO

### Lo que existe

```
01-inbox/
├── 01-owner-to-raul/        ← Owner → sistema
├── 02-deliverables-to-owner/ ← sistema → Owner
└── 03-raw-sources/           ← material crudo (gitignored)

G:\Mi unidad\RAUL\colaboradores\<dominio>\<colab>\
├── 01_De_<colab>_Para_Raoul/ ← colaborador → sistema
├── 02_De_Raoul_Para_<colab>/ ← sistema → colaborador
└── 03_Archivo/               ← procesados

G:\Mi unidad\RAUL-Exchange\Panama\  ← (legacy folder, dominio personal)
```

### Lo que NO existe

| Canal faltante | Qué necesita |
|---|---|
| ❌ **Junta directiva** | Entrega de presentations + RECEPCIÓN de decisiones + tracking de votos/aprobación. Hoy: PPTXs van a `02-deliverables-to-owner/` con título "Junta_*" pero la respuesta de junta no se captura formalmente. |
| ❌ **Regulator / gobierno** (SAPI, SENCAMER, FONDONORMA, COVENIN) | Submissions estructuradas + recepción de respuestas/certificados/objections. Hoy: refs en BR-2 ("verificación SENCAMER pendiente") pero workflow informal. |
| ❌ **Tercer party / contraparte** (ej. negociación Panama, inmobiliaria, legal externa) | Side-channel para correspondencia que NO es colaborador (no produce content) ni Owner (no decide en sistema). Hoy: no existe. |
| ❌ **Special deliverables overflow** | Para entregables one-off que no encajan con dominio o flujo estándar (ej. memo urgente a contraparte, response a regulator). Hoy: forzados a `01-owner-to-raul/` y se mezclan con tareas normales. |

**Riesgo de estructura actual:** todo lo que no es Owner ni colaborador termina en limbo entre `01-inbox/` y `colaboradores/`. Cuando llega una respuesta de junta o un email de SAPI, no hay carpeta canónica donde poner el archivo + iniciar el flujo de re-inyección.

---

## Resumen — gaps por severidad

| Gap | Severidad | Bloqueante para |
|---|---|---|
| No registro de decisiones-pendientes (kanban) | **Alta** | Operación remota / asíncrona |
| No catálogo de decision-makers | **Alta** | Estandarización / escalación |
| No mecanismo Owner-driven alternatives | **Alta** | Flexibilidad estratégica del Owner |
| No reentry post-decisión-externa | **Alta** | Continuidad de cadena cuando hay decision gate humano |
| No canal junta directiva formal | Media | Rastreabilidad de decisiones de junta |
| No canal regulador / gobierno | Media | Compliance + tracking de certificados |
| No canal tercer party / contraparte | Media | Operación no-Genteca (Panama, legal externa) |
| No bypass para deliverables one-off | Media | Flexibilidad operacional sin contaminar flujos estándar |
| No deadlines/SLAs por decision-maker | Baja | Planificación con realismo |
| No multi-decision-maker convergence | Baja | Decisiones que requieren múltiples sign-offs |

**Diagnóstico global:** el sistema /RAUL/ tiene **maquinaria de producción** muy bien construida (gates, caveats, agentes, KB), pero la **maquinaria de coordinación con humanos no-Owner** está casi sin estructurar. La cadena CSC asume que el Owner es el único decisor relevante; cuando entran junta/regulador/contraparte, todo se vuelve ad-hoc.

---

## Sketch preliminar — Phase 2 (propuesta arquitectónica)

**Principio rector:** las adiciones ENVUELVEN el sistema actual, NO lo modifican. La cadena CSC, los gates BR/AU/VA/OL, y la disciplina de caveats permanecen intactos.

### Adiciones propuestas (alto nivel)

**A. Registry de decisores (`04-system/03-governance/DECISION-MAKERS.md`)**
- Tabla canónica con: nombre/entidad, scope (qué puede decidir), canal preferido, SLA típico, escalación si no responde.
- Ej. rows: Owner, Junta Directiva Genteca, Equipo I&D Genteca (Kike + Liliam), SAPI Venezuela, SENCAMER, FONDONORMA, Legal externo, Contraparte Panama, etc.

**B. Pending-decisions kanban (`04-system/03-governance/PENDING-DECISIONS-REGISTRY.md`)**
- Tabla acumulativa con: decision-id, project, agente solicitante, decision-maker, fecha-solicitud, estado (PENDING / RESPONDED / EXPIRED), deadline si aplica, link al package, link a respuesta.
- Update on each new pending decision + on each response.

**C. Folders nuevos en `01-inbox/`**
- `04-decisions-in-flight/<project-id>/<decision-id>/` — context.md + options.md + decision-needed.md + response.md.
- `05-from-junta/`, `06-from-regulators/`, `07-from-third-parties/` — canales humanos no-Owner.
- `08-special-deliverables/` — overflow para one-offs.

**D. Templates en `04-system/04-tools-and-scripts/templates/`**
- `decision-request-template.md` (estructura: contexto, opciones, recomendación, qué necesitamos saber, deadline).
- `alternative-proposal-template.md` (Owner-driven alternative formal).
- `regulator-submission-template.md`.
- `junta-decision-package-template.md`.

**E. Patrón "Pause + Resume"**
- Cualquier agente que llega a un decision gate humano:
  1. Produce "decision package" con opciones + recomendación + caveats.
  2. Marca deliverable como `STATUS: AWAITING-DECISION-<id>`.
  3. Registra en PENDING-DECISIONS-REGISTRY.
  4. Cadena pausa.
- Cuando respuesta llega (a `05-from-junta/` etc.):
  1. InboxBot detecta + parsea.
  2. Marca decision-id como RESPONDED.
  3. Reinjecta a la cadena en el agente que pausó (vía Raul orchestrator).
  4. Cadena reanuda.

**F. Patrón "Owner-driven alternative"**
- Owner crea archivo en `01-inbox/01-owner-to-raul/_alt-<id>.md` siguiendo `alternative-proposal-template.md`.
- Raul detecta sufijo `_alt-` → enruta a Bruna primero (risk assessment) → luego a Aurelio si requiere planning → resto de cadena estándar.
- Documenta en DECISIONS.md como "Alternative path" con razón.

**G. Patrón "Crisis override"**
- Owner crea archivo `01-inbox/01-owner-to-raul/_urgent_<deadline>.md`.
- Raul ignora cadena estándar, va directo al agente más relevante con SLA agresivo.
- Post-crisis: Bruna hace post-mortem y registra precedente en BR-5.

### Lo que NO se propone

- ❌ **No reemplazar gates BR/AU/VA actuales.** Siguen siendo los de calidad.
- ❌ **No agregar nuevos agentes** solo para esto. Los existentes pueden manejar la coordinación.
- ❌ **No introducir frameworks externos** (Notion, Linear, Trello). Todo en local-first markdown.

---

## Próximos pasos sugeridos

1. **Owner revisa diagnóstico.** Confirma que el mapa refleja realidad. Flag gaps adicionales si hay.
2. **Phase 2 (propuesta detallada).** Tras revisión, Claude prepara propuesta concreta:
   - Schemas exactos para los 4 nuevos docs (DECISION-MAKERS, PENDING-DECISIONS-REGISTRY, templates).
   - Folder structure detallada con _index.md por carpeta nueva.
   - Modificaciones mínimas a InboxBot AGENT.md para soportar canales nuevos.
   - Plan de migración: qué decisiones actualmente "in-the-air" se inicializan en el registry.
3. **Owner aprueba propuesta.** Decide qué se ejecuta vs qué queda futuro.
4. **Ejecución.** Crear docs, folders, templates, ajustar InboxBot, entrada DECISIONS.

---

## Referencias

- [`DECISIONS.md`](DECISIONS.md) — log de decisiones arquitectónicas.
- [`RISK-POLICY.md`](RISK-POLICY.md) — política de riesgo (gates Bruna).
- [`MIGRATION-PLAN.md`](MIGRATION-PLAN.md) — plan migración general.
- `02-agents/conceptual/*.md` — definiciones SSOT de agentes.
- BR-2 logs — `03-projects/<dominio>/_governance/`.
- BR-5 precedentes — `04-system/03-governance/BR-5_*.md`.

---

**Estado de este doc:** diagnóstico completo. Propuesta arquitectónica (Phase 2) pendiente de session futura. Re-leer antes de discusión Phase 2.
