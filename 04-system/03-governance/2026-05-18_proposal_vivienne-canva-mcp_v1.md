---
documento: Proposal formal — Vivienne + Canva MCP como output engine PPTX (scope acotado a Vivienne, V1)
fecha: 2026-05-18
autor: Raul (Opus 4.7) — proposal post governance doc + post auth Canva MCP
status: PROPUESTA — 4 decisiones E1-E4 RESUELTAS por Owner 2026-05-18 (ver §9); pilot caso base pendiente (V7/V8.4 PPTX Cora Gama Notoriedad 2026, post-feedback Cora sobre Word V6)
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
4. **Híbrido permanente Canva-layout + python-pptx-charts es DEFAULT, no contingencia** — *DECISIÓN ARQUITECTÓNICA FIRME 2026-05-18 (ver DECISIONS.md entry de la misma fecha).* Canva siempre renderea layout + narrativa visual + brand consistency; python-pptx siempre genera los slides de charts con editabilidad nativa garantizada por construcción. No depende del comportamiento del export Canva sobre charts (el riesgo §8.1.6 queda resuelto por esta decisión). Workflow detallado en §2.5.
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
  │   create-design-from-brand-template (si brand template oficial Pro)
  │   o copy-design desde regular design base (ej. DAHKE-vJnnU Gama)
  │   o generate-design-structured (si no hay asset base)
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
| `mcp__claude_ai_Canva__create-design-from-brand-template` | Crear design nuevo a partir de brand template oficial Pro del dominio | Si existe brand template **oficial Pro** para el tipo de deck. **NO aplica al caso Gama Notoriedad 2026** (asset `DAHKE-vJnnU` es regular design, no brand template oficial — ver §3.2 update). |
| `mcp__claude_ai_Canva__copy-design` | Copiar un regular design base + renombrar la copia con identificador entrega | **Path operativo default Gama Notoriedad 2026** — copy-design desde `DAHKE-vJnnU`. Aplica cuando el asset base del dominio/cliente es regular design (no brand template Pro). |
| `mcp__claude_ai_Canva__generate-design-structured` | Generar design nuevo desde scratch usando outline VI-1 + brand kit | Si no existe asset base (brand template Pro ni regular design) — primer deck del dominio o tipo nuevo |
| `mcp__claude_ai_Canva__start-editing-transaction` | Abrir transacción atómica de edición (rollback-safe) | Antes de poblar/modificar slides |
| `mcp__claude_ai_Canva__perform-editing-operations` | Vaciar contenido literal del VI-1 slide a slide (textos, imágenes, tablas) | Iterativo, slide por slide |
| `mcp__claude_ai_Canva__commit-editing-transaction` | Confirmar edición y persistir cambios | Al cerrar transacción exitosa |
| `mcp__claude_ai_Canva__export-design` | Exportar a `.pptx` y `.pdf` | Al final, para entregable + backup local |
| `mcp__claude_ai_Canva__get-design-thumbnail` | Generar thumbnail para preview en cover note / handoff | Opcional, post-export |

Los otros ~22 tools del MCP (search assets, AI generative, etc.) **no se autorizan en V1** — quedan fuera de scope hasta validación de pilot. Específicamente: cualquier tool que reformule contenido (Magic Switch, Magic Write, etc.) está **prohibido por política de fidelidad de copy** (ver §7 sub-política).

### 2.5 Workflow híbrido permanente — Canva layout + python-pptx charts (DEFAULT)

> **Status arquitectónico:** workflow DEFAULT permanente desde decisión 2026-05-18 (DECISIONS.md). NO es contingencia condicional al riesgo 8.1.6 (que queda resuelto por esta decisión). Todo deck que pase por engine Canva sigue este workflow por construcción.

**Principio operativo.** Canva renderea **todo lo narrativo** (portadas, secciones, slides de copy, slides descriptivos, tablas no-data). python-pptx renderea **todo lo que sea chart con data binding exacto** (barras, líneas, heatmaps, scatter, dispersión, área). El merge final compone los dos outputs en un único PPTX entregable.

**Pasos técnicos.**

1. **Identificación de slides chart-críticos en el VI-1.** Durante producción del outline Vivienne marca cada slide con su engine: `engine: canva` (narrativo / copy / portada / sección / tabla descriptiva) o `engine: python-pptx` (chart con data binding). El VI-1 lleva esta clasificación como metadata por slide.
2. **Render Canva del subset narrativo.** `start-editing-transaction` → `perform-editing-operations` para todos los slides marcados `engine: canva` → `commit-editing-transaction` → `export-design` (.pptx). Los slides chart-críticos quedan como **placeholders** en el design Canva (slide vacío o con título solamente).
3. **Render python-pptx del subset chart-crítico.** En paralelo (o tras export Canva), `build_deck_v*.py` extendido genera **solo los slides chart-críticos** como PPTX standalone, heredando paleta + tipografía del brand kit `brand-kit.md` §4 (helpers ya codificados).
4. **Merge final.** Dos rutas operativas:
   - **Ruta A — script Python (`build_merge_canva_pptx_v*.py`, a desarrollar en pilot):** abre el PPTX exportado de Canva con `python-pptx`, reemplaza los slides placeholder por los slides chart standalone preservando orden + numeración. Output: PPTX único compuesto. **Default V1 cuando el script esté disponible.**
   - **Ruta B — merge manual en PowerPoint local:** Owner abre PPTX Canva en PowerPoint, copia los slides chart desde el PPTX standalone python-pptx y los inserta en posición. **Default V1 mientras el script A no exista.**
5. **Validación post-merge.** Diff visual rápido — verificar que (a) charts mantienen editabilidad nativa (click en chart en PowerPoint debe abrir editor de datos), (b) numeración correlativa de slides es consistente, (c) brand kit (paleta + tipografía) es consistente entre slides Canva y python-pptx.
6. **Cover note declara split por slide.** Mini-cover note §5 lista qué slides son `engine: canva` y cuáles `engine: python-pptx`, para trazabilidad y para guiar futuras iteraciones.

**Garantías por construcción.**

- **Editabilidad de charts asegurada** — los charts son python-pptx nativos siempre, no dependen del comportamiento del export Canva.
- **Aesthetic Canva aplicado al layout** — slides narrativos heredan brand template Gamma + brand kit Canva consistentemente.
- **Sin decisión condicional por slide en runtime** — la regla es estática (chart → python-pptx, no-chart → Canva), no requiere lógica de "¿se aplanó el chart?" en cada deck.
- **Fallback CORE intacto** — si Canva entero cae, `build_deck_v*.py` puede renderear el deck completo en python-pptx (incluyendo lo narrativo), según política split (`2026-05-18_tools-split-policy_canva-pro-adoption.md` §3).

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

### 3.2 Template Gama — regular design `DAHKE-vJnnU` como base operativa (path `copy-design`)

**Update 2026-05-18 (post-setup Owner):** la estrategia original (registrar V8.3 PPTX como **brand template oficial Pro** vía `create-design-from-brand-template`) **no se materializó** — Owner subió a Canva un subconjunto de slides adaptadas desde V8/V8.3 vía software **Gamma** como **regular design** (`type=design`, `category=design`), no como brand template oficial. Detalles canónicos del asset: `02-knowledge-base/02-domains/06-consultoria-externa/clientes/gama/canva-assets.md` §2.

**Asset operativo confirmado:**
- ID Canva: `DAHKE-vJnnU`
- Título Canva: `NOTORIEDAD-GAMA-2026.pptx` (literal — divergencia naming respecto al canónico `Gama V0.1 CANDIDATO / ...`, ver §9 directriz)
- Tipo: **regular design** (no brand template oficial Pro)
- Páginas: 20
- Edit URL: https://www.canva.com/d/pbO8CIP7BCZmIFX
- View URL: https://www.canva.com/d/0UiP-9mKlZk7yIA
- Origen: subset slides V8/V8.3 → Gamma → upload Canva (lo importante NO es el contenido sino el **formato** — layouts, typography, brand styling que Cora aprobó visualmente)

**Path operativo Vivienne — `copy-design` desde regular design:**

`mcp__claude_ai_Canva__create-design-from-brand-template` **NO aplica** sobre `DAHKE-vJnnU` (ese tool requiere brand template oficial Pro; `DAHKE-vJnnU` es regular design). El path operativo default es:

1. **`mcp__claude_ai_Canva__copy-design`** con `design_id = DAHKE-vJnnU` → retorna nuevo `design_id` para copia editable.
2. Renombrar copia con identificador de la entrega (ej. `2026-05-XX_gama-notoriedad-2026_v8.4`) — vía tool de update title si existe, o rename manual en UI por Owner como fallback.
3. Resto del workflow §4 sigue idéntico (start-editing-transaction → perform-editing-operations slide a slide → commit → export).

**Implicaciones del path regular design + copy-design:**

- **Favorable.** Aesthetic aspiracional Cora se hereda **desde día uno** — el regular design refleja el lenguaje visual que Cora encuentra deseable (subset slides V8/V8.3 que Cora ya vio, paso por Gamma alinea al aesthetic Cora-aprobado).
- **Adversa.** Atributos del V8.3 original (charts editables nativos, aspect ratio 16:9, brand kit aplicado consistente) **no están garantizados** en el regular design — Gamma puede haber alterado en el paso intermedio. Particularmente crítico: si Gamma aplanó los charts del V8.3 como imágenes en el export, los charts del regular design no son editables. **Esto NO bloquea operación** — el híbrido permanente §2.5 garantiza editabilidad de charts por construcción (python-pptx siempre para charts, independiente del comportamiento Canva).

**Naming.** El título del asset en Canva quedó como `NOTORIEDAD-GAMA-2026.pptx` (el nombre del archivo upload), divergente del naming canónico propuesto en §9 directriz operativa adicional (`Gama V0.1 CANDIDATO / Estudio Notoriedad / Template Maestro V1`). **No se renombra ahora** — referencia operativa por ID (`DAHKE-vJnnU`), consistente con política referencia-por-ID-no-por-nombre. El rename + sufijo V0.1 CANDIDATO aplicaría cuando Owner haga rename manual en Canva UI.

**Roadmap a brand template oficial Pro — mejora futura.** Cuando Owner promueva manualmente este diseño (o uno derivado) a brand template oficial vía Canva UI Pro features, Vivienne podría migrar a `create-design-from-brand-template`. Mientras tanto, `copy-design` desde `DAHKE-vJnnU` es el path operativo default y se documenta como tal en §4 workflow paso 3 + §7.1 draft AGENT.md.

**Brand kit V0.1 CANDIDATO `kAHKE4GYHQQ`** sigue aplicando como reference de paleta + tipografía + assets — la copy-design hereda el brand kit Canva referenced en el design original; verificar smoke test paso 2 antes de invocar copy-design.

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
¿Hay asset Canva base para el tipo de deck + dominio?
  ├─ Sí — brand template oficial Pro → mcp__claude_ai_Canva__create-design-from-brand-template
  │       (heredando aspect ratio, paleta, tipo, slides maestros)
  │
  ├─ Sí — regular design base (caso default para Gama Notoriedad 2026) →
  │       mcp__claude_ai_Canva__copy-design (design_id = DAHKE-vJnnU)
  │       → renombrar copia con identificador entrega
  │       (heredando layout + brand styling + brand kit referenced)
  │
  └─ No → mcp__claude_ai_Canva__generate-design-structured
          (con outline VI-1 como input estructurado + brand kit referenced)
```

**Caso Gama Notoriedad 2026 (default operativo V1):** `copy-design` desde `DAHKE-vJnnU` (regular design Gamma-derived) — ver §3.2 update post-setup Owner para el rationale completo. El path `create-design-from-brand-template` NO aplica sobre `DAHKE-vJnnU` (no es brand template oficial Pro). Roadmap futuro: promoción manual a brand template oficial → migración a `create-design-from-brand-template`.

**IDs canónicos a consultar antes de invocar el tool:** ver `02-knowledge-base/02-domains/06-consultoria-externa/clientes/gama/canva-assets.md` §1 (brand kit `kAHKE4GYHQQ`) y §2 (regular design base `DAHKE-vJnnU`).

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

> **Update 2026-05-18 (post-decisión híbrido permanente):** la métrica original 6.3.4 ("editabilidad de charts en export Canva") fue removida porque ya **no medimos si Canva aplana charts** — la decisión arquitectónica del híbrido permanente (DECISIONS.md 2026-05-18) asume que los charts siempre van por python-pptx, así que la editabilidad está garantizada por construcción. Las nuevas métricas focalizan en la **viabilidad operativa del workflow híbrido** (fidelidad layout Canva + overhead merge + balance entre engines).

| # | Métrica | Cómo medir | Threshold |
|---|---|---|---|
| 6.3.1 | **Fidelidad de copy y caveats Bruna 100% preservada** | Diff manual de cada slide del Canva vs VI-1 outline. Cualquier rephrasing = violación. | 0 violaciones |
| 6.3.2 | **Calidad visual percibida por Cora ≥ V8.3** | Cora evalúa side-by-side y opina cuál se ve mejor (binario o escala 1-5) | Canva ≥ V8.3 |
| 6.3.3 | **Tiempo end-to-end Owner→Cora-ready ≤ V8.3** | Cronómetro desde brief Vivienne hasta PPTX listo en Drive Cora | Canva ≤ tiempo V8.3 (~2-3 horas reportado) |
| 6.3.4 | **Fidelidad layout Canva vs aspiracional Cora** | Diff visual subjetivo del template Gamma renderado por Vivienne vs el sample original que Cora produjo en Gamma. Owner (y opcional Cora) opinan si el aesthetic se mantiene. | Match ≥ 80% percibido (sin escala formal — juicio Owner / Cora) |
| 6.3.5 | **Tiempo de merge híbrido aceptable** | Cronómetro del paso 4 §2.5 (merge Canva PPTX + python-pptx chart slides) — manual o vía script Ruta A si está disponible | ≤30 min manual; ≤5 min con script Ruta A |
| 6.3.6 | **Balance engine por slide razonable** | Conteo de slides con `engine: python-pptx` vs `engine: canva`. Idealmente python-pptx solo en slides chart-críticos. | python-pptx ≤ 30% del deck (los chart-críticos); el resto en Canva |

**Si todas las métricas pasan → pilot OK → autorizar updates AGENT.md §7.**
**Si 6.3.1 falla → pilot ABORTADO independiente de las otras** (fidelidad de copy es no-negociable).
**Si 6.3.2 o 6.3.4 fallan pero 6.3.3 + 6.3.5 + 6.3.6 pasan → re-evaluar — quizá brand template necesita iteración antes de migrar.**
**Si 6.3.6 falla (>50% slides en python-pptx) → revisar VI-1 — el deck puede ser sobre-cargado de charts y necesita reformulación narrativa, no decisión de engine.**

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
3. **Design base.** Tres rutas según el asset Canva del dominio: (a) si existe brand template oficial Pro → `create-design-from-brand-template`; (b) si existe regular design base (ej. Gama Notoriedad 2026 → `DAHKE-vJnnU`) → `copy-design` desde ese `design_id` + renombrar copia con identificador entrega; (c) si no hay asset base → `generate-design-structured` desde VI-1 outline. Consultar `02-knowledge-base/02-domains/<dominio>/clientes/<cliente>/canva-assets.md` antes de invocar — los IDs canónicos viven ahí.
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
| 8.1.6 | ~~**Charts editables nativos no se preservan en export PPTX** (Canva los puede aplanar como imágenes).~~ **RESUELTO 2026-05-18.** | ~~MEDIA~~ N/A | **RESUELTO por decisión arquitectónica 2026-05-18** (DECISIONS.md — "Híbrido Canva-layout + python-pptx-charts como DEFAULT permanente"). El híbrido §2.5 ahora es default por construcción: charts siempre se renderean en python-pptx, independiente del comportamiento del export Canva. No dependemos de Canva para charts → no hay riesgo de aplanamiento. La métrica original 6.3.4 fue reformulada (ver §6.3 update). |

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

## 9. Decisiones Owner resueltas 2026-05-18

> **Update 2026-05-18 (post-proposal):** Owner confirmó las 4 decisiones con los defaults recomendados por Raul + agregó una directriz operativa adicional ("Gama V0.1 CANDIDATO" — ver final de §9). Las 4 quedan RESUELTAS y activas a partir de esta fecha.

### E1 — Brand kit por cliente vs por dominio — RESUELTA

**Resolución Owner (2026-05-18):** **E1.c — Híbrido escalonado.**

- **Por dominio** para dominios propios: Genteca, Plenus, Finca, Teca (un brand kit por dominio).
- **Por cliente** para `consultoria-externa`: cada cliente externo = un brand kit Canva propio (Gama es el primero; futuros clientes serán independientes).

Refleja la realidad operativa — dominios propios tienen marca única, consultoría externa es servicio multi-cliente con marcas distintas. Coherente con estructura de KB (`02-knowledge-base/02-domains/<dominio>/clientes/<cliente>/brand-kit.md` para consultoría externa, `02-knowledge-base/02-domains/<dominio>/wiki/brand/` para dominios propios).

**Contexto histórico de la decisión.** Un cliente puede vivir dentro de un dominio (Gama es un cliente dentro de `consultoria-externa`, que puede tener múltiples clientes futuros — cada uno con marca distinta). Las opciones consideradas fueron: E1.a (todo por cliente), E1.b (por dominio + override), E1.c (híbrido escalonado).

### E2 — Sharing de designs Canva con clientes — RESUELTA

**Resolución Owner (2026-05-18):** **Comment para review / View para final / Edit caso por caso si cliente lo pide.**

- **Default review** = Comment (E2.b). Cliente comenta sin modificar; preserva trazabilidad de quién cambió qué.
- **Default final entregable** = View (E2.a). Cliente lee, no edita. Si quiere cambios, los pide.
- **Edit (E2.c)** solo si cliente lo solicita explícito; se evalúa caso por caso. Evita que el cliente modifique caveats Bruna sin que nos enteremos.

**Contexto histórico de la decisión.** Canva permite compartir con 3 niveles de permiso (view / comment / edit), cada uno con trade-offs entre control e IP vs colaboración.

### E3 — Retención de designs Canva post-cierre engagement — RESUELTA

**Resolución Owner (2026-05-18):** **E3.c — 12 meses post-cierre + export PPTX local committeado siempre como SSOT binario.**

- Designs Canva se mantienen vivos en cuenta 12 meses post-cierre del proyecto. Pasados los 12 meses → archive.
- **PPTX + PDF exportados al repo siempre.** El export local committeado es **SSOT binario permanente** independiente del estado en Canva. Si Canva cae o cierra cuenta, el repo conserva el deck final.
- Política consistente con principio transversal `portable_text_as_ssot_principle` — Canva es runtime-dependiente; el SSOT vive en repo.

**Contexto histórico de la decisión.** Cuando un proyecto con cliente externo cierra, ¿qué pasa con los designs Canva? Opciones: archivar inmediato, exportar+borrar, mantener N meses, decisión por cliente.

### E4 — Quién aprueba un nuevo brand template oficial — RESUELTA

**Resolución Owner (2026-05-18):** **E4.d — Híbrido escalonado.**

- **Owner siempre** valida visualmente y autoriza.
- **Bruna además** si el template incluye claims visuales (badges, frases, iconos con significado regulatorio / de superlative / de claim de marca).
- **Cliente además** si el template va a ser base de un deck que se le presenta (ej. Cora para Gama).

Para template Gama V1 (basado en V8.3): Owner + Cora. Si en el futuro hay template Genteca con badges/superlatives: Owner + Bruna. Si hay template Genteca para deck cliente externo (raro): Owner + Bruna + cliente.

**Contexto histórico de la decisión.** Un brand template es pieza estratégica — cuando Vivienne lo usa de base, hereda todo. Si el template tiene errores, propaga errores. Opciones: solo Owner, Owner+Bruna, Owner+cliente, híbrido escalonado.

---

### Directriz operativa adicional (Owner 2026-05-18) — "Gama V0.1 CANDIDATO"

**Mientras el brand kit Gama esté pre-validación con Cora** (5 items pendientes según brand-kit.md §5 — hex exacto rojo, tipografía oficial, logo, color secundario, restricciones logo), todo lo subido a Canva debe llevar etiqueta explícita **"Gama V0.1 CANDIDATO"** en el naming.

**Aplica a:**
- **Brand kit en Canva UI** — naming: `Gama V0.1 CANDIDATO` (no `Gama` ni `Gama Brand Kit`).
- **Brand template basado en V8.3 PPTX** — naming: `Gama V0.1 CANDIDATO / Estudio Notoriedad / Template Maestro V1` (no `Gama / Estudio Notoriedad / Template Maestro V1` como estaba propuesto en §3.2).
- **Cualquier referencia a Gama brand assets en Canva** mientras esté pre-validación: assets, designs derivados, comentarios internos en la UI.

**Cuándo se quita el sufijo "V0.1 CANDIDATO":** cuando Cora valide los 5 items pendientes del brand-kit.md §5 y el Owner confirme el upgrade a V1. En ese momento se renombran brand kit + brand template + assets, y se documenta el upgrade en `DECISIONS.md`.

**Razón.** Evita que el brand kit candidato se propague accidentalmente como oficial (a otros decks, a futuros clientes, a referencias internas) antes de que Cora lo valide. Pattern consistente con caveats de fidelidad de §3.3 (versionado de brand kits) y §8.3.3 (riesgo de brand kit V0.1 candidato no validado).

---

## 10. Próximos pasos secuenciados

### 10.1 Antes del pilot (Owner + setup)

> **Update 2026-05-18:** E1-E4 RESUELTAS (ver §9). Naming Canva ajustado a "Gama V0.1 CANDIDATO" hasta validación Cora — ver §9 directriz operativa adicional.

| # | Acción | Responsable | Bloqueador para |
|---|---|---|---|
| 10.1.1 | ~~Decidir E1-E4~~ **RESUELTA 2026-05-18** (ver §9): E1.c híbrido / E2 comment+view / E3.c 12 meses + export local / E4.d híbrido escalonado | Owner — DONE | — |
| 10.1.2 | Subir brand kit Gama a Canva con naming **"Gama V0.1 CANDIDATO"** — decidir camino: (a) manual via Canva UI, (b) vía MCP si hay tool `create-brand-kit` o equivalente | Owner (o Raul autorizado) | 10.1.4, pilot |
| 10.1.3 | Registrar V8.3 PPTX como brand template Gama en Canva con naming **"Gama V0.1 CANDIDATO / Estudio Notoriedad / Template Maestro V1"** (sufijo V0.1 CANDIDATO obligatorio hasta validación Cora) | Owner (o Raul autorizado) | pilot |
| 10.1.4 | Validar con Cora 5 items pendientes brand-kit.md §5 (hex exacto, tipografía, logo, color secundario, restricciones logo). Cuando Cora valide → renombrar brand kit + brand template removiendo sufijo "V0.1 CANDIDATO" + entry en DECISIONS.md formalizando upgrade a V1 | Owner via Cora | upgrade a V1; no bloquea pilot interno |

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

*Update 2026-05-18 (post-setup Owner): §3.2 actualizado reflejando que el asset Canva subido es **regular design `DAHKE-vJnnU`** (NO brand template oficial Pro), por lo que el path operativo default es **`copy-design`** desde ese ID — no `create-design-from-brand-template`. §4 paso 3 + §2.2 diagrama + §2.4 mapping reflejan las 3 rutas (brand template Pro / regular design vía copy-design / generate-design-structured). Brand template oficial Pro queda como mejora futura cuando Owner promueva manualmente el diseño. Detalles canónicos del asset en `02-knowledge-base/02-domains/06-consultoria-externa/clientes/gama/canva-assets.md` §2.*
