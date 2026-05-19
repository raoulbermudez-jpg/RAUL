---
documento: Proposal formal — Vivienne + Canva MCP como output engine PPTX (scope acotado a Vivienne, V1)
fecha: 2026-05-18
autor: Raul (Opus 4.7) — proposal post governance doc + post auth Canva MCP
status: PROPUESTA — pendiente validación Owner + pilot caso base (V7 PPTX Cora Gama Notoriedad 2026)
proyecto_pilot: gama-notoriedad-2026 (consultoria-externa) — próxima entrega Cora tras feedback V6
scope: Vivienne únicamente. Ampliación multi-agente (Atlas / Luma / Orfeo / Oz light) explícitamente diferida.
governance_base: [[2026-05-18_tools-split-policy_canva-pro-adoption]] (decisiones canónicas Canva Pro + split CORE)
lecciones_base: [[2026-05-18_LECCIONES-V5-V6-PLAN-EVOLUCION-SISTEMA]] (Bucket 5 — ampliación de Vivienne)
referencias_arquitectonicas: norte arquitectónico §0 (vendor-neutral) / `portable_text_as_ssot_principle` / DECISIONS.md 2026-05-12
restricciones_explicitas: NO editar `vivienne/AGENT.md` ni `vivienne.md` conceptual en esta sesión — el draft del bloque AGENT.md va como anexo del proposal (§7) y se aplica solo post-pilot con autorización Owner explícita
---

# Proposal — Vivienne + Canva MCP como output engine PPTX (V1)

> **Cómo leer este documento.** §1 diagnostica el flujo actual y dolores. §2 propone arquitectura híbrida (Canva default, python-pptx fallback CORE obligatorio). §3 estrategia de brand kit + brand templates. §4 workflow paso a paso para Vivienne. §5 mini-cover note. §6 plan de pilot con métricas A/B. §7 draft del bloque AGENT.md (ANEXO — NO aplicar todavía). §8 riesgos + mitigaciones. §9 decisiones Owner pendientes (E1-E4). §10 próximos pasos secuenciados. Si tenés 5 minutos: leer §1, §2, §6 y §9.

---

## 1. Diagnóstico actual — Vivienne con python-pptx

### 1.1 Flujo vigente (lo que hace Vivienne hoy)

```
Owner → brief (audiencia + decisión + dominio + material fuente + formato)
  ↓
Vivienne carga brand kit pre-flight (§6.1 paso 6 conceptual)
  ↓
Vivienne produce VI-1 outline (Markdown SSOT — §7.2 conceptual)
  ↓
Vivienne genera build_deck_v*.py (python-pptx + matplotlib)
  ↓
Vivienne ejecuta el script → PPTX renderizado en disco
  ↓
Vivienne entrega: VI-1 .md + .pptx + cover note narrativa
```

Caso base validado: V8.3 PPTX Gama Notoriedad 2026 (commit `d13cd26`, 2026-05-18) — 16:9 restaurado tras V8.2.

### 1.2 Dolores conocidos del path actual

| Dolor | Status mitigación | Validado en |
|---|---|---|
| **Token explosion >32K** cuando se produce outline + script + render en una sola invocación | **Codificado** en `vivienne/AGENT.md` runtime guardrails (commit `debde3d`, 2026-05-18) — protocolo de 3 invocaciones obligatorio para decks >30 slides con ≥5 charts | Casos V3 y V5 deck Gama 2026-05-17/18 (memoria `feedback_vivienne_token_explosion_pattern_v1`) |
| **Fidelidad visual limitada vs lo que cliente espera** | NO mitigado — python-pptx + matplotlib alcanza calidad consultoría pero con alto costo de líneas de código por slide y muchas iteraciones | V8 → V8.1 → V8.2 → V8.3 (4 versiones para ajustar charts, datos y aspect ratio — commits `ca910fe`, `4c8571b`, `e715496`, `d13cd26`) |
| **Charts editables requirieron 2 iteraciones** | NO mitigado — `build_deck_v8.0` usaba matplotlib PNG, V8.1 tuvo que reconstruir charts nativos editables a pedido Cora | Commits `4c8571b` (V8.1 charts nativos editables — pedido Cora) y `e715496` (V8.2 datos correctos + contraste heatmaps) |
| **Retoques manuales pre-Cora** del Owner sobre el PPTX | NO mitigado — Owner abre PPTX en PowerPoint local y ajusta antes de drop a Cora | Implícito en ciclo V5+V6+V8 |
| **Brand kit drift** entre paleta declarada y output real | **Mitigado** parcialmente por brand kit Gama V0.1 + helpers python-pptx codificados en brand-kit.md §4 | Caso "rojo vino tinto" V5/V6 corregido en V8 |

### 1.3 Lo que se mantiene fuera del scope de Canva (anti-deprecación CORE)

Por la política de split (`tools-split-policy_canva-pro-adoption.md` §3 — fallback CORE obligatorio), las siguientes piezas **NO migran a Canva** y siguen siendo path CORE:

| Pieza | Por qué se mantiene CORE | Engine |
|---|---|---|
| **VI-1 outline** (Markdown SSOT) | Es portable text, vendor-neutral, auditable, multi-LLM. SSOT del deck. | Markdown puro |
| **Word formal artifact** (consultoría externa) | Patrón Word-first → PPTX-after validado V5/V6 (memoria `feedback_word_first_pptx_after_policy`). Word es el contenido aprobado, PPTX es destilación. | python-docx + matplotlib |
| **Charts críticos editables con datos exactos** | Cora pidió charts nativos editables (commit `4c8571b`). Canva renderea bien layout pero charts complejos con data binding requieren python-pptx para garantizar fidelidad. | python-pptx (charts nativos) |
| **`build_deck_v*.py` scripts existentes** | Fallback CORE obligatorio por split policy. Si Canva MCP cae, Vivienne ejecuta script python. | python-pptx + matplotlib |
| **Brand kit markdown SSOT** | `02-knowledge-base/02-domains/06-consultoria-externa/clientes/gama/brand-kit.md` es la fuente de verdad. Canva sincroniza desde KB, no al revés. | Markdown puro |

---

## 2. Arquitectura propuesta

### 2.1 Principios

1. **VI-1 outline sigue siendo SSOT** — sin cambios. El outline Markdown sigue siendo lo que vive en repo, lo que se audita, lo que es portable.
2. **Output engine PPTX cambia a Canva MCP** como **default cuando aplique** (ver condiciones §2.3).
3. **`build_deck_v*.py` con python-pptx se mantiene como fallback CORE obligatorio** — política split aplica literal. No se borra, no se deprecia, se mantiene testeado.
4. **Híbrido para charts** — Canva renderea layout + narrativa visual + brand consistency; charts críticos editables con data binding exacto se generan con python-pptx en slides puntuales y se mergean o re-linkean.
5. **Brand kit en KB sigue siendo SSOT** — Canva ingiere el brand kit desde KB markdown; Canva nunca actúa como SSOT del brand kit.

### 2.2 Diagrama de flujo propuesto (híbrido)

```
Owner → brief
  ↓
Vivienne carga brand kit pre-flight (igual que hoy)
  ↓
Vivienne produce VI-1 outline (igual que hoy, Markdown SSOT)
  ↓
Vivienne smoke-test Canva MCP (list-brand-kits)
  ├─ MCP healthy → path Canva
  │     ↓
  │   create-design-from-brand-template (si template existe)
  │   o generate-design-structured (si no)
  │     ↓
  │   start-editing-transaction
  │     ↓
  │   perform-editing-operations (slide-a-slide, vaciado literal del VI-1)
  │     ↓
  │   ¿slide requiere chart editable crítico?
  │     ├─ Sí → pause transacción → generar slide con python-pptx → merge
  │     └─ No → continuar con Canva nativo
  │     ↓
  │   commit-editing-transaction → export-design (.pptx + .pdf)
  │     ↓
  │   drop a Drive cliente + link Canva editable
  │
  └─ MCP no healthy → fallback CORE (silencioso, sin pedir input al Owner)
        ↓
      build_deck_v*.py (python-pptx + matplotlib)
        ↓
      Cover note declara que se usó fallback CORE
```

### 2.3 Cuándo usar Canva (default) vs cuándo fallback CORE forzado

| Condición | Engine |
|---|---|
| Brand kit del dominio existe en Canva + MCP healthy + deck es ≤40 slides con ≤10 charts | **Canva default** |
| Brand kit del dominio NO existe en Canva (primer deck del dominio) | **Fallback CORE + advertir Owner** que el brand kit debe subirse a Canva antes de migrar ese dominio |
| MCP no healthy (smoke test `list-brand-kits` falla o timeout) | **Fallback CORE silencioso** — reportar en cover note del entregable |
| Deck contiene >5 charts críticos con data binding exacto (estadísticas densas, heatmaps, scatter) | **Híbrido** — Canva para layout/narrativa, python-pptx para esos slides |
| Deck es interno / quick draft / sin consumidor cliente | **Fallback CORE preferente** — overhead Canva no se justifica para outputs efímeros |
| Owner pide explícitamente "render con python-pptx" (ej. caso A/B contra Canva) | **Fallback CORE forzado** |

### 2.4 Mapping de los 30 tools Canva MCP a acciones de Vivienne (críticos)

| Tool MCP | Acción Vivienne | Cuándo se invoca |
|---|---|---|
| `mcp__claude_ai_Canva__list-brand-kits` | Smoke test MCP healthy + selección de brand kit del dominio | Inicio de cada sesión Canva — primer tool call |
| `mcp__claude_ai_Canva__create-design-from-brand-template` | Crear design nuevo a partir de brand template oficial del dominio | Si existe brand template para el tipo de deck (ej. "Gama / Estudio Notoriedad / Cora") |
| `mcp__claude_ai_Canva__generate-design-structured` | Generar design nuevo desde scratch usando outline VI-1 + brand kit | Si no existe brand template — primer deck del dominio o tipo nuevo |
| `mcp__claude_ai_Canva__start-editing-transaction` | Abrir transacción atómica de edición (rollback-safe) | Antes de poblar/modificar slides |
| `mcp__claude_ai_Canva__perform-editing-operations` | Vaciar contenido literal del VI-1 slide a slide (textos, imágenes, tablas) | Iterativo, slide por slide |
| `mcp__claude_ai_Canva__commit-editing-transaction` | Confirmar edición y persistir cambios | Al cerrar transacción exitosa |
| `mcp__claude_ai_Canva__export-design` | Exportar a `.pptx` y `.pdf` | Al final, para entregable + backup local |
| `mcp__claude_ai_Canva__get-design-thumbnail` | Generar thumbnail para preview en cover note / handoff | Opcional, post-export |

Los otros ~22 tools del MCP (search assets, AI generative, etc.) **no se autorizan en V1** — quedan fuera de scope hasta validación de pilot. Específicamente: cualquier tool que reformule contenido (Magic Switch, Magic Write, etc.) está **prohibido por política de fidelidad de copy** (ver §7 sub-política).

### 2.5 Manejo de charts híbridos (paso a paso técnico)

Cuando un slide requiere chart crítico editable con data binding exacto:

1. Pausar transacción Canva tras `start-editing-transaction` (sin commit).
2. Generar el slide específico con `python-pptx` (charts nativos editables tipo `XL_CHART_TYPE.BAR_CLUSTERED`, etc.).
3. Dos rutas de merge:
   - **Ruta A — merge externo:** exportar parcial Canva → merge con python-pptx local del slide → output PPTX final compuesto. Más complejo, mayor fidelidad.
   - **Ruta B — re-link en Canva:** upload del PNG del chart python-pptx a Canva via `mcp__claude_ai_Canva__upload-asset` (si tool existe) o paste manual, con nota explícita en cover note de que ese chart NO es editable nativo en Canva.
4. Decisión Ruta A vs B se toma por slide según criticidad de edición cliente.

**Default V1:** Ruta B (re-link) — más simple, valida workflow. Ruta A se evalúa si Cora pide editar charts del PPTX entregado.

---

## 3. Brand kit + brand templates strategy

### 3.1 Brand kit Gama — primer caso

**Estado actual:**
- Brand kit V0.1 candidato en KB: `02-knowledge-base/02-domains/06-consultoria-externa/clientes/gama/brand-kit.md` (paleta hex + tipografía + helpers python-pptx/docx/matplotlib codificados)
- Smoke test Canva MCP: `list-brand-kits` retorna `{"items":[]}` — cuenta vacía
- 5 items pendientes validación Cora (hex exacto rojo Gama, tipografía oficial, logo, color secundario, restricciones logo) — documentados en brand-kit.md §5

**Acción propuesta:**
1. Owner sube brand kit Gama a Canva manualmente (UI Canva) o vía MCP si hay tool de creación (verificar — el mapping §2.4 lista `list-brand-kits` pero no `create-brand-kit`). **Decisión cuál camino → §9 E1 / §10 paso 1.**
2. Brand kit en Canva = derivado del SSOT markdown KB. Si KB cambia, Canva se actualiza (manualmente o vía MCP).
3. Política firme: **el SSOT del brand kit es markdown en KB**. Canva nunca actúa como SSOT — solo como derivado consumido por Vivienne en render.

### 3.2 Brand template Gama — registrar V8.3 como oficial

**Candidato:** PPTX V8.3 (commit `d13cd26`, 2026-05-18) — última versión validada en producción con 16:9 restaurado.

**Por qué V8.3:**
- Aspect ratio 16:9 correcto
- Datos correctos + heatmaps con contraste (V8.2 fix)
- Charts nativos editables (V8.1 fix solicitado por Cora)
- Estructura narrativa Pirámide Minto visual aplicada
- Brand kit Gama (rojo `#E30613`, Montserrat + Open Sans) aplicado consistente

**Acción propuesta:**
1. Owner sube V8.3 PPTX como brand template oficial Gama en Canva (UI Canva o vía MCP si hay tool — verificar).
2. Naming sugerido: `Gama / Estudio Notoriedad / Cliente Cora / Template Maestro V1` (basado en `create_design_from_brand_template` semantics).
3. Cuando próxima entrega Cora requiera deck, Vivienne invoca `create-design-from-brand-template` con ese template como base — heredando aspect ratio, paleta, tipografía, estructura de slides maestros.

### 3.3 Brand kits de otros dominios (cuándo lleguen)

**Política propuesta:**
- **Un brand kit por dominio.** Genteca = 1 brand kit. Plenus = 1 brand kit. Marca-personal = 1 brand kit. Consultoría externa = **un brand kit por cliente** (Gama es uno, futuros clientes serán independientes).
- **Trigger de creación:** primer deck Vivienne con engine Canva en ese dominio/cliente. Antes de eso, no se crea (overhead innecesario).
- **Ownership:** Owner crea/edita en Canva UI o autoriza Raul a crear vía MCP. Vivienne consume, nunca crea brand kits autónomamente.
- **Versionado:** Canva no tiene versionado nativo robusto para brand kits — si cambia, queda registrado en cambio del markdown KB SSOT con `last_touched` + entry en `DECISIONS.md` si la decisión es estructural.

**Decisión Owner pendiente — ver §9 E1.**

### 3.4 Política firme: SSOT en KB, Canva es derivado

| Capa | Quién es SSOT | Quién es derivado |
|---|---|---|
| Brand kit (paleta, tipo, logo, do/don't) | Markdown en KB | Brand kit en Canva |
| Brand template (estructura de slides maestros) | PPTX original validado (V8.3 para Gama) committeado en repo | Brand template en Canva |
| Outline de deck | VI-1 Markdown en repo | Design en Canva |
| Backup del deck final | PPTX/PDF exportado de Canva + dropeado a Drive cliente | Design vivo en Canva cloud |

**Implicación operativa:** si Canva cae, cierra cuenta o el Owner cambia de proveedor de diseño, **el repo /RAUL/ conserva todo lo necesario para regenerar cualquier deck**. El brand kit está en markdown, el template está en PPTX committeado, el outline está en markdown, y los scripts python-pptx fallback están vivos.

---

## 4. Workflow paso a paso (para Vivienne en runtime)

### Paso 1 — Producir VI-1 outline (igual que hoy)

Vivienne ejecuta §6.1 a §6.3 del conceptual: brief read → arco narrativo → VI-1 Markdown. Sin cambios respecto al flujo actual. El outline es la fuente de verdad de qué dice cada slide y en qué orden.

### Paso 2 — Smoke test Canva MCP

```
Vivienne llama mcp__claude_ai_Canva__list-brand-kits
  ├─ Retorna items con brand kit del dominio → continuar paso 3
  ├─ Retorna {"items":[]} o brand kit no encontrado → advertir Owner + fallback CORE
  └─ Error / timeout → fallback CORE silencioso + nota en cover note
```

**Política:** smoke test es **obligatorio** antes de cualquier operación de render Canva. Detecta auth caducada, cuota agotada, MCP desconectado.

### Paso 3 — Crear design base

```
¿Existe brand template para el tipo de deck + dominio?
  ├─ Sí → mcp__claude_ai_Canva__create-design-from-brand-template
  │       (heredando aspect ratio, paleta, tipo, slides maestros)
  └─ No → mcp__claude_ai_Canva__generate-design-structured
          (con outline VI-1 como input estructurado + brand kit referenced)
```

### Paso 4 — Edición atómica slide por slide

```
mcp__claude_ai_Canva__start-editing-transaction
  ↓
Para cada slide del VI-1:
  ↓
  mcp__claude_ai_Canva__perform-editing-operations
    - text inserts (título-como-conclusión literal del VI-1, body literal)
    - image inserts (PNGs de charts pre-generados o assets brand kit)
    - layout adjustments respetando:
        * 4 bullets max (política del upgrade reciente)
        * infografía vs bullets (decision tree §6.3 paso 2 conceptual)
        * Pirámide Minto visual (slide descriptiva → slide analítica)
        * white space disciplinado
  ↓
  ¿slide requiere chart crítico editable con data binding exacto?
    ├─ Sí → pause Canva → python-pptx slide standalone → merge (Ruta B default V1)
    └─ No → continuar con Canva nativo
  ↓
Siguiente slide
```

**Regla crítica de fidelidad de copy:** las `perform-editing-operations` vacían **literal** el contenido del VI-1. Cualquier rephrasing automático de Canva (sugerencias de Magic Write, etc.) es **violación de política** — Vivienne no usa esas features. Ver §7 sub-política "Fidelidad de copy en Canva".

### Paso 5 — Commit + export

```
mcp__claude_ai_Canva__commit-editing-transaction
  ↓
mcp__claude_ai_Canva__export-design (formato .pptx)
mcp__claude_ai_Canva__export-design (formato .pdf, opcional)
  ↓
mcp__claude_ai_Canva__get-design-thumbnail (para cover note)
  ↓
Descarga local a 03-projects/<dominio>/<proyecto>/03-deck/V<N>/
  basename: <YYYY-MM-DD>_<scope>_<tipo-deck>_v<N>.pptx
```

### Paso 6 — Drop a Drive cliente + link Canva editable

```
Owner (manual): copia PPTX + PDF a G:\Mi unidad\RAUL\colaboradores\<dominio>\<cliente>\02_De_Raoul_Para_<cliente>\
Owner (manual): comparte link Canva editable con cliente (ver §9 E2 — comment / view / edit)
Owner (manual): email a cliente con paths Drive + link Canva
```

### Paso 7 — Entrega a Raul con cover note + handoff

Vivienne devuelve a Raul:
- Ruta absoluta del VI-1 .md
- Ruta absoluta del PPTX exportado de Canva
- Ruta absoluta del PDF (si exportado)
- Link Canva editable (URL retornado por API)
- Thumbnail PNG de la primera slide
- Mini-cover note declarando engine usado + slides híbridos si aplica + items abiertos

---

## 5. Mini-cover note Vivienne+Canva (formato handoff)

Cada entrega Vivienne con engine Canva debe llevar mini-cover note en el VI-1 Markdown (extensión de la cover note existente §7.2 conceptual) declarando:

```markdown
## Cover note (engine Canva MCP)
- **Brand kit Canva usado:** Gama V0.1 candidato (último sync KB → Canva: YYYY-MM-DD)
- **Brand template base:** Gama / Estudio Notoriedad / Template Maestro V1 (o N/A si generate-structured)
- **Engine por slide:**
  - Slides 1-12, 15-25: Canva nativo
  - Slides 13-14: python-pptx merge (charts editables — Ruta B re-link)
- **Link Canva editable:** https://canva.com/design/<design_id>/edit?...
- **Export local PPTX:** `C:\RAUL\03-projects\...\YYYY-MM-DD_..._v8.4.pptx`
- **Export local PDF:** `C:\RAUL\03-projects\...\YYYY-MM-DD_..._v8.4.pdf`
- **Smoke test MCP (timestamp):** `list-brand-kits` OK, 1 item retornado
- **Fallback CORE invocado:** No (o "Sí — reason: <X>" si aplica)
- **Items abiertos:** (idem cover note conceptual — claims pendientes, refresh data, validaciones)
- **Material fuente consumido:** (idem cover note conceptual)
- **Claims sensibles + sello BR-2:** (idem cover note conceptual)
- **Storyboard / arco narrativo:** (idem cover note conceptual)
```

**Razón:** trazabilidad explícita del engine permite (a) auditar qué se hizo con qué tool, (b) detectar drift entre Canva y python-pptx outputs en A/B test del pilot, (c) facilitar fallback CORE si el cliente pide regeneración sin Canva.

---

## 6. Plan de pilot

### 6.1 Pilot — caso base

**Proyecto:** `consultoria-externa/gama-notoriedad-2026`
**Entregable pilot:** próxima versión PPTX (probable V8.4 / V9) cuando llegue feedback Cora sobre V6 Word actualmente en PAUSA (ver session handoff 2026-05-19).
**Cliente:** Cora Urrea (cora.urrea@gmail.com)
**Trigger:** feedback Cora sobre Word V6 → ajustes Word si aplica → arrancar pilot Canva paralelo con build_deck_v8.4.py CORE.

### 6.2 A/B test real

Producir la misma entrega por **dos rutas paralelas**, comparar lado a lado:

| Ruta | Engine | Producido por |
|---|---|---|
| **A — Canva MCP** | Canva nativo + híbrido para charts críticos | Vivienne (proposal V1 de este doc) |
| **B — python-pptx CORE** | Extensión de `build_deck_v8.3.py` → `build_deck_v8.4.py` | Vivienne (path actual default) |

**Quien compara:** Owner directo. Idealmente Cora también ve las dos versiones y opina (si Cora acepta participar — opcional).

### 6.3 Métricas de éxito

| # | Métrica | Cómo medir | Threshold |
|---|---|---|---|
| 6.3.1 | **Fidelidad de copy y caveats Bruna 100% preservada** | Diff manual de cada slide del Canva vs VI-1 outline. Cualquier rephrasing = violación. | 0 violaciones |
| 6.3.2 | **Calidad visual percibida por Cora ≥ V8.3** | Cora evalúa side-by-side y opina cuál se ve mejor (binario o escala 1-5) | Canva ≥ V8.3 |
| 6.3.3 | **Tiempo end-to-end Owner→Cora-ready ≤ V8.3** | Cronómetro desde brief Vivienne hasta PPTX listo en Drive Cora | Canva ≤ tiempo V8.3 (~2-3 horas reportado) |
| 6.3.4 | **Tasa de retoques manuales Cora ↓** | Cora reporta cuántos ajustes manuales hace pre-presentación. Si entregamos PPTX editable Canva, Cora puede editar directo. | Canva ≤ retoques V8.3 |

**Si todas las métricas pasan → pilot OK → autorizar updates AGENT.md §7.**
**Si 6.3.1 falla → pilot ABORTADO independiente de las otras** (fidelidad de copy es no-negociable).
**Si 6.3.2 falla pero 6.3.3 y 6.3.4 pasan → re-evaluar — quizá brand template necesita iteración antes de migrar.**

### 6.4 Métricas de fracaso (abort triggers)

| # | Trigger | Acción |
|---|---|---|
| 6.4.1 | Cualquier pérdida de fidelidad de copy (Canva reformuló sin permiso) | **Abort pilot.** Documentar caso en `feedback_canva_copy_drift_antipattern` (memoria nueva). Sub-política §7 era insuficiente — revisar. |
| 6.4.2 | Regression vs V8.3 (calidad visual claramente inferior) | **Abort migración.** Mantener python-pptx CORE como default. Documentar lecciones. |
| 6.4.3 | Charts críticos editables ilegibles o no-editables en export PPTX Canva | **Abort migración para charts.** Mantener híbrido permanente (Canva layout + python-pptx charts) en lugar de migrar todo. |
| 6.4.4 | Tiempo end-to-end ≥2× V8.3 | **Re-evaluar.** Overhead Canva no compensa. Posible: workflow muy verbose, optimizar antes de descartar. |
| 6.4.5 | Cora rechaza link Canva por razones de propiedad de design / IP / privacy | **Re-evaluar política §9 E2-E3.** Posible: solo entregar PPTX exportado, no link editable. |

### 6.5 Documentación post-pilot

Independiente del resultado, post-pilot se crea memoria nueva:
- Si OK: `feedback_vivienne_canva_engine_validated_v1` + actualización `project_vivienne_upgrade_2026-05-18`
- Si ABORTADO: `feedback_canva_pilot_failed_v1` con diagnóstico de causa raíz

Y entry en `04-system/03-governance/DECISIONS.md` con outcome + decisión Owner (continuar / pivotear / abortar).

---

## 7. Updates a Vivienne AGENT.md (DRAFT — NO aplicar todavía)

> **STATUS:** Este es el **draft del bloque** a insertar en `.claude/agents/vivienne/AGENT.md` cuando el pilot valide la propuesta. **NO editar el runtime ahora.** La edición sucede solo cuando: (1) pilot completado, (2) métricas §6.3 pasaron, (3) Owner autoriza explícitamente.

### 7.1 Sección nueva propuesta para `vivienne/AGENT.md`

Insertar **después de la sección "Runtime guardrails — anti-token-explosion"** (que es la última política mayor codificada en el commit `debde3d`):

```markdown
### Output engine: Canva MCP (opcional, default cuando aplique)

Vivienne tiene un **output engine externo opcional** vía Canva MCP (`mcp__claude_ai_Canva__*`) que se usa como default cuando se cumplen las condiciones de §X.X. El path CORE (python-pptx + matplotlib) **se mantiene como fallback obligatorio** y NO se deprecia (política `04-system/03-governance/2026-05-18_tools-split-policy_canva-pro-adoption.md` §3 — fallback CORE obligatorio).

**Cuándo usar Canva (default):**

| Condición | Engine |
|---|---|
| Brand kit del dominio existe en Canva + MCP healthy + deck es ≤40 slides con ≤10 charts | Canva default |
| Brand kit del dominio NO existe en Canva | Fallback CORE + advertir Owner |
| MCP no healthy (smoke test falla) | Fallback CORE silencioso + nota en cover note |
| Deck con >5 charts críticos con data binding exacto | Híbrido (Canva layout + python-pptx charts) |
| Deck interno / quick draft / sin consumidor cliente | Fallback CORE preferente |
| Owner pide explícitamente "render con python-pptx" | Fallback CORE forzado |

**Workflow Canva (cuando aplica):**

1. **Smoke test obligatorio.** Antes de cualquier render, ejecutar `mcp__claude_ai_Canva__list-brand-kits` para confirmar auth y conectividad. Si falla → fallback CORE silencioso.
2. **Brand kit pre-flight extendido.** Verificar que el brand kit del dominio existe en Canva Y que está sincronizado con el SSOT markdown del KB. Si Canva tiene versión más vieja que el KB, advertir Owner antes de render.
3. **Design base.** Si existe brand template para el tipo de deck + dominio: `create-design-from-brand-template`. Si no: `generate-design-structured` desde VI-1 outline.
4. **Edición atómica.** `start-editing-transaction` → `perform-editing-operations` slide por slide vaciando contenido **literal** del VI-1 (respetando 4-bullets-max, infografía-vs-bullets, Pirámide Minto visual, white space).
5. **Charts críticos híbridos.** Si slide tiene chart crítico editable con data binding exacto: pause Canva, generar slide python-pptx standalone, merge (Ruta B re-link default).
6. **Commit + export.** `commit-editing-transaction` → `export-design` (.pptx + .pdf opcional) → descarga local + thumbnail.
7. **Mini-cover note Canva-aware.** Cover note del VI-1 declara engine usado, brand kit Canva con timestamp sync, slides híbridos si aplica, link Canva editable, paths locales exportados, resultado smoke test.

**Política firme — fidelidad de copy en Canva (NO NEGOCIABLE):**

Canva **NO reescribe contenido bajo ninguna circunstancia**. Las `perform-editing-operations` vacían **literal** el contenido del VI-1. Cualquier feature Canva que reformule contenido automáticamente (Magic Write, Magic Switch, sugerencias AI de re-phrasing, traducciones automáticas, etc.) está **prohibido**. Si Canva sugiere cambio de redacción, Vivienne ignora y mantiene literal el VI-1.

**Por qué:** el VI-1 es el SSOT del contenido (decidido por especialistas Cuanti/Sinta/Methos + gateado por Bruna). Cualquier rephrasing pierde fidelidad de claims, caveats metodológicos, y trazabilidad. Una sola violación = abort pilot + memoria post-mortem (caso base: §6.4.1 del proposal V1).

**Política firme — SSOT en KB markdown:**

El brand kit en Canva es **derivado** del SSOT markdown en KB (`02-knowledge-base/02-domains/<dominio>/...`). Si KB cambia → Canva se sincroniza (manual o vía MCP). Canva nunca actúa como SSOT — si Canva cae o el Owner cambia de proveedor de diseño, el brand kit sigue vivo en markdown KB.

El brand template en Canva es **derivado** del PPTX original validado committeado en repo (ej. V8.3 PPTX Gama). Si template cambia, se re-genera desde el PPTX original.

**Política firme — auth verification:**

Antes de arrancar render Canva, smoke test `list-brand-kits`. Si retorna error / timeout / vacío inesperado → no proceder con Canva, fallback CORE silencioso, reportar en cover note. No reintentar smoke test más de 1 vez en la misma invocación.

**Política firme — anti-deprecación CORE:**

`build_deck_v*.py` scripts existentes **se mantienen vivos y testeados**. Periódicamente (al menos cada 3 meses), ejecutar build_deck_vN.py de un caso reciente para confirmar que python-pptx + matplotlib siguen funcionando como fallback. Si un script CORE deja de funcionar (cambio de versión python-pptx, deprecación matplotlib, etc.), priorizar arreglar el script antes de seguir usando Canva — la portabilidad del repo depende de eso.
```

### 7.2 Sección complementaria propuesta para conceptual SSOT `vivienne.md`

Añadir nueva sub-sección **§6.8** en el conceptual (después de §6.7 "Word-first → PPTX-after"):

```markdown
### 6.8 Output engine externo opcional (Canva MCP — runtime-específico)

Para plataformas de ejecución que tengan acceso a un MCP de diseño visual externo (ej. Canva MCP en claude.ai), Vivienne puede usarlo como output engine PPTX **opcional**. Esto es runtime-específico — el conceptual SSOT solo declara el **principio**, no la tool.

**Principio:** el output engine PPTX puede ser sustituido por una tool externa siempre que se cumplan tres condiciones:

1. **VI-1 outline sigue siendo SSOT.** El outline Markdown es la fuente de verdad del contenido. La tool externa solo renderea.
2. **Fidelidad de copy preservada.** La tool externa NO reformula el contenido del VI-1. Cualquier feature de rephrasing automático está prohibido.
3. **Fallback CORE mantenido.** El path open-source vendor-neutral (python-pptx + matplotlib) se mantiene funcional y testeado. Si la tool externa falla, Vivienne cae al path CORE silencioso.

**Detalles de tool específica (Canva MCP):** ver runtime adapter `.claude/agents/vivienne/AGENT.md` sección "Output engine: Canva MCP".

**Política de brand kit con tool externa:** el brand kit en la tool externa es derivado del SSOT markdown en KB. La tool externa nunca actúa como SSOT del brand kit.

**Documentos de referencia:** `04-system/03-governance/2026-05-18_tools-split-policy_canva-pro-adoption.md` (política split CORE vs Owner-selected) + `04-system/03-governance/2026-05-18_proposal_vivienne-canva-mcp_v1.md` (proposal V1 + pilot).
```

### 7.3 Política de aplicación

- §7.1 (AGENT.md runtime) **NO aplicar** hasta que pilot pase métricas §6.3 + Owner autorice explícitamente.
- §7.2 (conceptual SSOT) **NO aplicar** hasta que §7.1 esté aplicado — el conceptual va después del runtime, no antes (el conceptual codifica el principio una vez que la implementación está validada).
- Cuando se apliquen, commit separado con mensaje claro referenciando este proposal y el pilot que validó.

---

## 8. Riesgos y mitigaciones

### 8.1 Riesgos técnicos

| # | Riesgo | Probabilidad | Mitigación |
|---|---|---|---|
| 8.1.1 | **MCP rate limits / quota agotada.** Canva Pro tiene quotas API, en pico de uso puede retornar 429. | BAJA en V1 (uso bajo); MEDIA si se escala | Fallback CORE silencioso documentado en §2.3 + §7.1. Smoke test antes de cada sesión Canva. Si 429 mid-transacción, abort transacción y completar con python-pptx. |
| 8.1.2 | **Versionado de designs en cloud.** Designs Canva viven en cloud. ¿Qué pasa si Canva borra design por inactividad? ¿Quién es SSOT? | MEDIA | VI-1 markdown sigue siendo SSOT. Cada export Canva se descarga local + commitea (PPTX + PDF). Si design Canva se pierde, regenerar desde VI-1. Política firme: **backup local PPTX/PDF en cada commit del proyecto**. |
| 8.1.3 | **Reescritura accidental por Canva AI features** (Magic Write, Magic Switch, Magic Resize, etc.). | MEDIA si no se controla, BAJA con política | Política explícita §7.1 sub-política "Fidelidad de copy en Canva" — prohibición literal de features que reformulan. Solo `perform-editing-operations` (manual / scripted), no AI generative. |
| 8.1.4 | **Canva cae o cierra cuenta.** Servicio externo, dependencia commercial. | BAJA pero posible | Fallback CORE python-pptx nunca se borra. Scripts `build_deck_v*.py` se mantienen testeados. Brand kit en markdown KB. PPTX V8.3 (template oficial) committeado en repo. Regeneración 100% posible desde repo. |
| 8.1.5 | **Brand kit drift entre Canva y KB markdown.** Owner edita en Canva UI, no actualiza KB. O viceversa. | ALTA si no hay disciplina | Política firme §7.1: **SSOT = markdown KB**. Cualquier cambio importante en KB debe sincronizarse a Canva manualmente o vía MCP. Periodic check (mensual) de paleta hex KB vs Canva. |
| 8.1.6 | **Charts editables nativos no se preservan en export PPTX** (Canva los puede aplanar como imágenes). | MEDIA — verificar en pilot | Híbrido para charts críticos (Ruta B re-link con python-pptx). Si export Canva aplana, pivotear a Ruta A (merge externo) o mantener híbrido permanente. Medir en §6.3.4. |

### 8.2 Riesgos de gobernanza / proceso

| # | Riesgo | Probabilidad | Mitigación |
|---|---|---|---|
| 8.2.1 | **Scope creep** — empezar con Vivienne y "aprovechar" para Atlas/Luma/Orfeo/Oz antes de validar pilot. | MEDIA | Restricción explícita en este proposal: scope Vivienne únicamente V1. Ampliación según `project_canva_expansion_pending` requiere pilot OK + Owner autoriza por agente individual. |
| 8.2.2 | **Bruna gate pasado por alto** porque "el deck se ve bien en Canva". | BAJA con política, ALTA si se relaja | Claims sensibles siguen requiriendo sello BR-2 antes del render — política conceptual §6.6 + §9. Engine PPTX no cambia esto. Cover note Canva-aware (§5) declara claims sensibles + sello BR-2. |
| 8.2.3 | **Owner no tiene tiempo de comparar A/B en pilot.** | MEDIA | Pilot opcional — si Owner no puede comparar, default = Canva ON pero con fallback CORE listo. Captura aprendizajes en cualquier caso. |
| 8.2.4 | **Cora no quiere editar en Canva** (prefiere PPTX en PowerPoint). | MEDIA | Entregar siempre PPTX exportado + PDF + link Canva editable (3 formatos). Cora elige. Si Cora ignora link Canva consistentemente → pivotear a "Canva interno solo, no compartir con cliente". |

### 8.3 Riesgos de fidelidad

| # | Riesgo | Probabilidad | Mitigación |
|---|---|---|---|
| 8.3.1 | **Caveats metodológicos perdidos** en migración a Canva (texto pequeño que el render omite por layout). | MEDIA | Diff manual obligatorio en pilot (§6.3.1). Política §7.1 fidelidad de copy. Si caveat se pierde por layout: forzar slide separado con caveat completo. |
| 8.3.2 | **Numeración de claims (BR-2 #N) no se preserva** en re-render. | MEDIA | Numeración va en VI-1, se vacía literal en `perform-editing-operations`. Validar en pilot. Si se pierde, agregar numeración como text frame protegido. |
| 8.3.3 | **Brand kit V0.1 candidato no validado por Cora** se sube a Canva como oficial → propaga error. | ALTA si no se valida | Antes de subir brand kit a Canva, validar 5 items pendientes §5 de brand-kit.md con Cora. Mientras no esté validado, etiquetar template/brand-kit Canva como "V0.1 CANDIDATO" en naming. |

---

## 9. Decisiones Owner pendientes (E1-E4)

Capturadas, NO resueltas en este proposal — requieren input Owner antes o durante pilot.

### E1 — ¿Brand kit por cliente o por dominio?

**Contexto.** Un cliente puede vivir dentro de un dominio (Gama es un cliente dentro de `consultoria-externa`, y `consultoria-externa` puede tener múltiples clientes futuros — cada uno con su marca distinta).

**Opciones:**
- **E1.a — Por cliente.** Cada cliente externo = un brand kit Canva. `consultoria-externa` tendría N brand kits (Gama, FuturaCliente1, FuturaCliente2, etc.). Dominios propios (Genteca, Plenus) también = un brand kit cada uno.
- **E1.b — Por dominio + override por cliente.** Un brand kit base por dominio (`consultoria-externa` tendría uno genérico) + overrides para clientes con marca propia. Más complejo, menos claro.
- **E1.c — Híbrido.** Por dominio para dominios propios + por cliente para `consultoria-externa`. Reconoce que dominios propios tienen marca única (Genteca) mientras consultoría externa siempre es por cliente.

**Recomendación Raul:** **E1.c (híbrido).** Refleja la realidad operativa — Genteca tiene una sola marca, mientras consultoría externa es servicio multi-cliente con marcas distintas por cliente. Coherente con estructura de KB (`02-knowledge-base/02-domains/<dominio>/clientes/<cliente>/brand-kit.md` para consultoría externa, `02-knowledge-base/02-domains/<dominio>/wiki/brand/` para dominios propios).

### E2 — ¿Compartir designs Canva con clientes en view, comment o edit?

**Contexto.** Canva permite compartir designs con 3 niveles de permiso. Cada nivel tiene trade-offs.

**Opciones:**
- **E2.a — Solo view.** Cliente ve, no edita. Si quiere cambios, los pide a nosotros. Más control, menos colaboración.
- **E2.b — Comment.** Cliente puede agregar comentarios sin modificar. Buen balance para review.
- **E2.c — Edit.** Cliente puede editar directo. Máxima colaboración, pero riesgo de IP / accidental damage / propagación a equipos del cliente.

**Recomendación Raul:** **Default = E2.b (comment) para revisión / E2.a (view) para final.** Edit (E2.c) solo si cliente lo pide explícito y se evalúa caso por caso. Esto preserva trazabilidad de quién cambió qué y evita que el cliente modifique caveats Bruna sin que nos enteremos.

### E3 — ¿Política de retención de designs Canva al cerrar engagement con cliente?

**Contexto.** Cuando se cierra un proyecto con un cliente externo (ej. Gama Notoriedad termina), ¿qué pasa con los designs Canva del proyecto?

**Opciones:**
- **E3.a — Archivar en Canva.** Mantener cuenta Canva con el design archived. Recuperable si cliente vuelve.
- **E3.b — Exportar + borrar.** Exportar PPTX/PDF a Drive cliente y a repo, luego borrar design Canva. Reduce overhead Canva.
- **E3.c — Mantener vivo por X tiempo.** Mantener N meses (ej. 12) post-cierre por si cliente pide ajuste, luego archive.
- **E3.d — Decisión por cliente.** Preguntar a cada cliente al cierre si quieren acceso continuado al design Canva o no.

**Recomendación Raul:** **E3.c (12 meses) + export local committeado.** Balance entre disponibilidad para cliente y limpieza de cuenta Canva. PPTX/PDF exportados quedan en repo siempre (SSOT permanente).

### E4 — ¿Quién aprueba un nuevo brand template oficial?

**Contexto.** Un brand template Canva (estructura de slides maestros con paleta, tipo, layouts) es una pieza estratégica — cuando Vivienne lo usa de base, hereda todo. Si el template tiene errores, propaga errores. ¿Quién autoriza un nuevo template?

**Opciones:**
- **E4.a — Solo Owner.** Owner valida visualmente y autoriza.
- **E4.b — Owner + Bruna.** Si el template incluye claims visuales (badges, frases, iconos con significado regulatorio), Bruna también gatea.
- **E4.c — Owner + cliente** (para clientes externos). Cliente valida que su marca está bien representada.
- **E4.d — Híbrido escalonado.** Owner siempre. Bruna si hay claims visuales. Cliente si es template para deck que se le presenta.

**Recomendación Raul:** **E4.d (híbrido escalonado).** Para template Gama V1 (basado en V8.3): Owner + Cora (representa Gama). Si en el futuro hay template Genteca con badges/superlatives: Owner + Bruna.

---

## 10. Próximos pasos secuenciados

### 10.1 Antes del pilot (Owner + setup)

| # | Acción | Responsable | Bloqueador para |
|---|---|---|---|
| 10.1.1 | Decidir E1-E4 (brand kit scope / sharing permissions / retention / template approval) | Owner | 10.1.2, 10.1.3 |
| 10.1.2 | Subir brand kit Gama a Canva — decidir camino: (a) manual via Canva UI, (b) vía MCP si hay tool `create-brand-kit` o equivalente | Owner (o Raul autorizado) | 10.1.4, pilot |
| 10.1.3 | Registrar V8.3 PPTX como brand template oficial Gama en Canva (naming: `Gama / Estudio Notoriedad / Template Maestro V1`) | Owner (o Raul autorizado) | pilot |
| 10.1.4 | Validar con Cora 5 items pendientes brand-kit.md §5 (hex exacto, tipografía, logo, color secundario, restricciones logo) — opcional pero recomendable antes de uso público | Owner via Cora | release público; no bloquea pilot interno |

### 10.2 Pilot (cuando llegue feedback Cora V6)

| # | Acción | Responsable | Effort estimado |
|---|---|---|---|
| 10.2.1 | Llegada feedback Cora sobre Word V6 → ajustes Word si aplica | Owner + Cora | depende feedback |
| 10.2.2 | Vivienne invocada con engine Canva → ejecuta workflow §4 → produce PPTX V8.4 (o V9) Canva | Raul → Vivienne | 1-2 sesiones |
| 10.2.3 | En paralelo: Vivienne invocada con engine python-pptx CORE → produce PPTX V8.4 (o V9) python-pptx (extensión de build_deck_v8.3.py) | Raul → Vivienne | 1 sesión |
| 10.2.4 | Owner compara A/B side-by-side, evalúa métricas §6.3 | Owner | 30-60 min |
| 10.2.5 | Opcional: Cora compara A/B y opina | Cora | depende disponibilidad |
| 10.2.6 | Decisión Owner: pilot PASS / PIVOT / ABORT | Owner | inmediato post-comparación |

### 10.3 Post-pilot (según outcome)

#### Si pilot PASS

| # | Acción | Responsable |
|---|---|---|
| 10.3.1 | Aplicar updates §7.1 a `.claude/agents/vivienne/AGENT.md` | Raul (commit separado) |
| 10.3.2 | Aplicar updates §7.2 a `04-system/02-agents/conceptual/vivienne.md` | Raul (commit separado, después de 10.3.1) |
| 10.3.3 | Crear memoria `feedback_vivienne_canva_engine_validated_v1` con caso pilot Gama V8.4 | Raul |
| 10.3.4 | Actualizar memoria `project_vivienne_upgrade_2026-05-18` con status post-Canva | Raul |
| 10.3.5 | Entry en `DECISIONS.md` con outcome pilot + decisiones Owner E1-E4 resueltas | Raul |
| 10.3.6 | Revisitar ampliación multi-agente diferida (Atlas / Luma / Orfeo / Oz light) — proposal por agente, NO batch | Raul + Owner |

#### Si pilot PIVOT (ej. fidelidad copy fallo pero calidad visual OK)

| # | Acción | Responsable |
|---|---|---|
| 10.3.7 | Memoria `feedback_canva_copy_drift_antipattern` con caso |
| 10.3.8 | Re-trabajar §7 con políticas más estrictas, repetir pilot |
| 10.3.9 | Mantener python-pptx CORE como default durante re-iteración |

#### Si pilot ABORT

| # | Acción | Responsable |
|---|---|---|
| 10.3.10 | Memoria `feedback_canva_pilot_failed_v1` con diagnóstico causa raíz | Raul |
| 10.3.11 | Mantener python-pptx CORE como default permanente para Vivienne | sin cambios |
| 10.3.12 | Owner decide si mantener suscripción Canva Pro o cancelar (~$120/año) | Owner |
| 10.3.13 | Ampliación multi-agente Canva descartada hasta nueva propuesta con tool distinta (Figma, Beautiful.ai, Gamma.app) | — |

---

## 11. Referencias cruzadas

- **Governance base:** [[2026-05-18_tools-split-policy_canva-pro-adoption]] — decisiones canónicas Canva Pro + split CORE (commit `d5ff1ee`, 2026-05-18)
- **Lecciones base:** [[2026-05-18_LECCIONES-V5-V6-PLAN-EVOLUCION-SISTEMA]] — Bucket 5 hiring + Bucket 4 mejoras infra
- **Conceptual SSOT Vivienne:** `04-system/02-agents/conceptual/vivienne.md` — versión vigente con §6.7 Word-first → PPTX-after
- **Runtime AGENT.md Vivienne:** `.claude/agents/vivienne/AGENT.md` — versión vigente con commit `debde3d` (upgrade 6 políticas)
- **Brand kit Gama:** `02-knowledge-base/02-domains/06-consultoria-externa/clientes/gama/brand-kit.md` V0.1 candidato
- **Inventario tools Owner-selected:** `04-system/04-tools-and-scripts/TOOLS-OWNER-SELECTED.md` v0.1 (entrada Canva MCP)
- **Inventario tools CORE:** `04-system/04-tools-and-scripts/TOOLS-REQUIREMENTS.md` v1.1 (python-pptx + matplotlib siguen vivos)
- **Norte arquitectónico §0:** vendor-neutral
- **Memoria HOT:** [[project_arquitectura_norte_repo_raul]]
- **Memoria HOT:** [[project_portable_text_as_ssot_principle]]
- **Memoria HOT:** [[project_canva_expansion_pending]] — scope Vivienne ahora, multi-agente diferido
- **Memoria HOT:** [[feedback_tools_inventory_split_policy]] — fallback CORE obligatorio
- **Memoria HOT:** [[feedback_vivienne_token_explosion_pattern_v1]] — workaround 3 invocaciones vigente, Canva NO lo reemplaza
- **Memoria HOT:** [[feedback_word_first_pptx_after_policy]] — Word primero, PPTX (Canva o python-pptx) después
- **Memoria HOT:** [[project_vivienne_upgrade_2026-05-18]] — 6 políticas del upgrade reciente siguen vigentes
- **Session handoff vigente:** [[project_session_handoff_2026-05-19]] — V5+V6 entregados, PAUSA Cora
- **Caso pilot proyecto:** `03-projects/consultoria-externa/gama-notoriedad-2026/` (commits `d13cd26`, `e715496`, `4c8571b`, `ca910fe` para V8.x baseline)

---

## 12. Patrón de referencia

Este proposal sigue el patrón estructural del governance doc base (`2026-05-18_tools-split-policy_canva-pro-adoption.md`) y del doc de lecciones V5+V6 (`2026-05-18_LECCIONES-V5-V6-PLAN-EVOLUCION-SISTEMA.md`):

- Frontmatter con metadata completa
- Resumen ejecutivo / cómo leer al inicio
- Secciones numeradas con rationale + alternativas + implicaciones cuando aplica
- Decisiones Owner explícitas con opciones + recomendación Raul
- Próximos pasos secuenciados con responsables + bloqueadores
- Referencias cruzadas con [[link]] markup para memorias HOT

---

*Proposal V1 producido por Raul (Opus 4.7) el 2026-05-18 tras autorización Owner para arrancar proposal formal Vivienne + Canva MCP. Scope acotado a Vivienne — ampliación multi-agente diferida. NO toca runtime de Vivienne ni conceptual SSOT en esta sesión — los drafts §7 se aplican post-pilot con autorización Owner explícita. Pilot pendiente de feedback Cora sobre Word V6 (PAUSA actual session handoff 2026-05-19).*
