---
cliente: Gama (Cadena de Supermercados Gama Express)
canal_consultoria: Cora Urrea (cora.urrea@gmail.com)
proposito: Registro de assets Gama en Canva (brand kits + brand templates) — IDs, estado, divergencias del plan original
status: V0.1 — brand kit CANDIDATO (pendiente validación Cora); brand template como regular design (no brand template oficial), adaptado desde V8/V8.3 vía Gamma
ultima_actualizacion: 2026-05-18
last_touched: 2026-05-18
relacionados:
  - 02-knowledge-base/02-domains/06-consultoria-externa/clientes/gama/brand-kit.md
  - 04-system/03-governance/2026-05-18_proposal_vivienne-canva-mcp_v1.md
  - 04-system/03-governance/DECISIONS.md (entry 2026-05-18 — Canva E1-E4 + V0.1 CANDIDATO directriz)
---

# Canva assets — Gama

> Este archivo es el **registro operativo** de los assets Gama subidos a Canva (brand kits + brand templates). El **SSOT textual** del brand kit (paleta hex, tipografía, logo, do/don't) sigue siendo `brand-kit.md` en este mismo directorio. Canva es **derivado** (política firme proposal §3.4 + DECISIONS.md 2026-05-18).

---

## 1. Brand kit Gama V0.1 CANDIDATO

| Campo | Valor |
|---|---|
| **ID Canva** | `kAHKE4GYHQQ` |
| **Naming en Canva UI** | `Gama V0.1 CANDIDATO` (sufijo obligatorio por DECISIONS.md 2026-05-18 hasta validación Cora) |
| **Fecha creación** | 2026-05-18 |
| **Estado** | V0.1 CANDIDATO — pendiente validación Cora (5 items abiertos en `brand-kit.md` §5: hex exacto rojo Gama, tipografía oficial, logo, color secundario, restricciones logo) |
| **Fuente de assets** | Web scraping de [empresa.gamaenlinea.com](https://empresa.gamaenlinea.com/) (portal corporativo Gama Enlinea — NO es sitio de marca consumer; ver caveat §1.1) |
| **SSOT textual de referencia** | `02-knowledge-base/02-domains/06-consultoria-externa/clientes/gama/brand-kit.md` |

### 1.1 Divergencia del plan original

El proposal Vivienne+Canva (`04-system/03-governance/2026-05-18_proposal_vivienne-canva-mcp_v1.md` §3.4) establecía que el brand kit Canva se ingiere desde el **markdown KB** como SSOT. En la práctica, Owner pobló el brand kit Canva por **web scraping del portal corporativo Gama Enlinea** (`https://empresa.gamaenlinea.com/`), no por sync manual desde el markdown KB.

**Implicación adicional — fuente es portal corporativo, no sitio consumer.** `empresa.gamaenlinea.com` es el portal corporativo de Gama Enlinea (no necesariamente el sitio de marca consumer / B2C). Esto significa que los assets capturados pueden tener orientación corporate/institucional (logos formales, paletas oficiales documentadas) en lugar de assets de campaña consumer. **Caveat operativo:** validar manualmente que colores y logos capturados sean efectivamente los **corporativos oficiales** y no banners promocionales del portal corporativo (notas internas, campañas a empleados, comunicaciones B2B).

**Implicación general.** El portal corporativo es **más autoritativo** en un sentido (refleja la identidad oficial documentada de Gama) pero **menos curada** en otro (puede incluir paletas y assets de banners promocionales no-corporativos, ofertas estacionales, headers de campaña interna). El markdown KB sigue siendo el SSOT textual de referencia — Canva es derivado del portal corporativo, no del KB.

**Mitigación obligatoria.** Owner debe validar manualmente en la UI de Canva que los assets capturados por scraping no incluyan:

- Colores de banners promocionales no-corporativos (ej. fondos amarillos / verdes de campañas).
- Logos secundarios de marcas blancas / proveedores que aparezcan en la web.
- Tipografías de copy publicitario que no sean las tipografías corporativas oficiales.
- Imágenes / patterns de campañas estacionales.

Si el scraping capturó assets extra-corporativos, **limpiar en UI Canva antes de cualquier render Vivienne**. Documentar la limpieza en este archivo (próxima entry — campo "Notas de limpieza post-scraping").

### 1.2 Notas de limpieza post-scraping

*Pendiente — Owner pasará revisión manual en Canva UI y reportará qué assets requirieron descarte.*

---

## 2. Template Gama — regular design (NO brand template oficial)

| Campo | Valor |
|---|---|
| **ID Canva** | `DAHKE-vJnnU` |
| **Título oficial en Canva** | `NOTORIEDAD-GAMA-2026.pptx` (literal como aparece en la UI Canva tras upload) |
| **Tipo Canva** | **regular design** (`type=design`, `category=design`) — **NO brand template oficial** |
| **Páginas** | 20 |
| **Edit URL** | https://www.canva.com/d/pbO8CIP7BCZmIFX |
| **View URL** | https://www.canva.com/d/0UiP-9mKlZk7yIA |
| **Fecha creación** | 2026-05-18 |
| **Origen** | Subconjunto de slides adaptadas desde **V8/V8.3 PPTX** (commits `ca910fe`, `4c8571b`, `e715496`, `d13cd26`) usando software **Gamma** (anteriormente Cora) — lo importante NO es el contenido sino el **formato** (layouts, typography, brand styling que Cora aprobó visualmente) |
| **Estado** | V0.1 CANDIDATO operativo (regular design — sin sufijo en el título Canva por ahora; ver §2.3 divergencia naming) |

### 2.1 Divergencia del plan original — regular design en lugar de brand template oficial

El proposal §3.2 establecía un **brand template oficial** Canva (feature Pro) como destino del V8.3 PPTX. En la práctica, Owner subió el archivo como **regular design** (`type=design`), no como brand template oficial. Canva clasifica el asset como `category=design` — un diseño regular editable, no un template del catálogo de la cuenta.

**Implicación operativa crítica para Vivienne.**

- **NO se puede invocar `mcp__claude_ai_Canva__create-design-from-brand-template`** sobre `DAHKE-vJnnU` — ese tool requiere un brand template oficial (asset Pro de la cuenta), y `DAHKE-vJnnU` es un regular design.
- **El path operativo default es `mcp__claude_ai_Canva__copy-design`** desde el ID `DAHKE-vJnnU`. Vivienne crea una copia editable del regular design → la renombra con el identificador de la entrega (ej. `2026-05-XX_gama-notoriedad-2026_v8.4`) → poblada con el contenido del VI-1 outline vía `perform-editing-operations` → exporta a PPTX/PDF.
- **Path Vivienne paso a paso:**
  1. `mcp__claude_ai_Canva__copy-design` con `design_id = DAHKE-vJnnU` → retorna nuevo `design_id` para la copia editable.
  2. (opcional) renombrar copia con identificador entrega vía tool de update title si existe; si no, el rename queda en UI Canva manual por Owner.
  3. `mcp__claude_ai_Canva__start-editing-transaction` sobre el nuevo `design_id`.
  4. `mcp__claude_ai_Canva__perform-editing-operations` para vaciar contenido VI-1 slide a slide.
  5. `mcp__claude_ai_Canva__commit-editing-transaction` → `mcp__claude_ai_Canva__export-design`.
- **El roadmap a brand template oficial Pro queda como mejora futura** — cuando Owner promueva manualmente este diseño (o uno derivado) a brand template oficial vía Canva UI Pro features, Vivienne podría migrar a `create-design-from-brand-template`. Mientras tanto, `copy-design` desde `DAHKE-vJnnU` es el path operativo default.

### 2.2 Implicación favorable y adversa del origen

**Implicación favorable.** El template como regular design adaptado vía Gamma desde V8/V8.3 hereda:

- El aesthetic aspiracional aprobado por Cora visualmente (formato, layouts, typography, brand styling).
- La estructura de slides validada en V8/V8.3 (los layouts vienen del PPTX que Cora ya vio).
- Reduce el riesgo de entregar un PPTX que Cora considere visualmente "frío" o "consultor genérico" — el template ya refleja el lenguaje visual que Cora encuentra deseable.

**Implicación adversa.** El paso por Gamma (export Gamma → upload Canva como regular design) puede haber alterado atributos del V8.3 original:

- Charts nativos editables (commit `4c8571b` — pedido Cora explícito) **no están garantizados** en el regular design si Gamma los aplanó como imágenes en el export.
- Aspect ratio 16:9 (commit `d13cd26`) puede haber cambiado en el paso por Gamma — Owner debe verificar en la UI Canva.
- Brand kit Gama (rojo, tipografía) aplicado en V8.3 puede haberse perdido o alterado al pasar por Gamma.

Particularmente crítico: si Gamma aplanó los charts del V8.3 como imágenes durante el export, los charts en `DAHKE-vJnnU` ya no son editables nativos. Esto **no bloquea** el path operativo — el híbrido permanente §2.3 ya garantiza editabilidad por construcción (python-pptx para charts críticos).

### 2.3 Divergencia naming — referencia operativa por ID

El naming canónico propuesto en proposal V1 §3.2 y §9 (directriz "Gama V0.1 CANDIDATO") era `Gama V0.1 CANDIDATO / Estudio Notoriedad / Template Maestro V1`. Sin embargo, el título real del asset en Canva quedó como **`NOTORIEDAD-GAMA-2026.pptx`** — el nombre del archivo upload.

**Decisión operativa.** **NO renombrar** el asset en Canva por ahora. El sufijo `V0.1 CANDIDATO` aplicaría cuando Owner promueva manualmente el diseño en Canva UI (rename + posible promoción a brand template Pro). Mientras tanto:

- **Referencia operativa = ID** (`DAHKE-vJnnU`), consistente con política §4.1 ("Referencia por ID, no por nombre"). El nombre puede divergir del naming canónico sin afectar operación de Vivienne, que identifica el asset por ID inmutable.
- **Documentado como divergencia naming** — el proposal V1 §3.2 y §9 directriz hablan del naming canónico aspiracional; la realidad operativa es el título Canva tal cual.
- **Cuándo se reconciliará:** cuando Owner haga el rename manual en Canva UI (alineando a `Gama V0.1 CANDIDATO / ...`) o cuando se promueva a brand template oficial Pro — entonces se actualiza este archivo + DECISIONS.md.

### 2.4 Mitigación estructural — híbrido como default permanente

**El enfoque híbrido Canva-layout + python-pptx-charts queda adoptado como DEFAULT, no como contingencia/fallback al riesgo 8.1.6 del proposal.** Ver `DECISIONS.md` entry 2026-05-18 — "Híbrido permanente Canva layout + python-pptx charts".

Resumido: Canva (vía copy-design desde `DAHKE-vJnnU`) genera layout + brand styling (heredando aesthetic Cora del template Gamma); python-pptx genera los slides de charts (heredando editabilidad y data binding exacto del V8.3); merge final via script Python o manual. La editabilidad de charts queda garantizada **independiente** del comportamiento del export Canva o de si Gamma aplanó charts en el paso intermedio — no dependemos de Canva para charts.

---

## 3. Otros assets detectados en cuenta Canva

### 3.1 Brand kit huérfano `kAHKE82Q8d8`

| Campo | Valor |
|---|---|
| **ID Canva** | `kAHKE82Q8d8` |
| **Naming en Canva UI** | _Sin nombre — probablemente default Canva vacío_ |
| **Estado** | NO USAR |
| **Acción recomendada** | Owner **difiere cleanup** (2026-05-18 — no urgente). El asset queda marcado NO USAR en este registro; Vivienne lo ignora por política §4.1 (referencia por ID, no por nombre). Cuando Owner tenga ventana de housekeeping Canva, borrar o renombrar a `_VACIO_NO_USAR` en UI. |

**Rationale.** Vivienne identifica brand kits por **ID** (no por nombre — ver política §4 abajo). Un brand kit con ID válido pero sin contenido relevante puede generar confusión en futuras llamadas `mcp__claude_ai_Canva__list-brand-kits` si Vivienne intenta auto-seleccionar. Mientras el cleanup no se ejecute, Vivienne debe consultar este archivo (`canva-assets.md` §1) para confirmar que el brand kit operativo es `kAHKE4GYHQQ` y nunca `kAHKE82Q8d8`.

---

## 4. Política de identificación de assets Gama en Canva

### 4.1 Referencia por ID, no por nombre

**Vivienne debe referenciar brand kits y diseños base por su ID Canva** (`kAHKE4GYHQQ` para el brand kit, `DAHKE-vJnnU` para el regular design base), no por nombre. Razón: los nombres pueden cambiar (sufijo V0.1 CANDIDATO se quitará post-validación Cora; futuras versiones tendrán naming distinto; el título del template quedó como `NOTORIEDAD-GAMA-2026.pptx` divergente del naming canónico — ver §2.3); los IDs son inmutables.

**Implicación operativa para Vivienne.** Workflow §4 del proposal — paso 2 (smoke test) y paso 3 (creación del design base) — debe consultar este archivo (`canva-assets.md`) para obtener el ID correcto del brand kit / regular design antes de invocar los tools MCP. Específicamente para el deck Notoriedad Gama 2026, el paso 3 usa **`copy-design`** desde `DAHKE-vJnnU` (NO `create-design-from-brand-template`, que requeriría brand template oficial Pro — feature no disponible sobre este asset; ver §2.1).

### 4.2 Naming convention

Naming sigue el patrón `Gama V<N>.<M> <ESTADO>` donde `ESTADO ∈ {CANDIDATO, VALIDADO}`:

| Versión | Naming | Cuándo |
|---|---|---|
| V0.1 CANDIDATO | `Gama V0.1 CANDIDATO` | Estado actual — pre-validación Cora |
| V1 VALIDADO | `Gama V1 VALIDADO` (sufijo "VALIDADO" opcional — el sufijo CANDIDATO sí es obligatorio) | Post-validación de los 5 items pendientes en `brand-kit.md` §5 |
| V1.1, V2, etc. | `Gama V<N>.<M> <ESTADO>` | Iteraciones futuras (cambios paleta, tipografía, logo) |

### 4.3 Versionado — nueva entrada por upgrade

Cualquier nueva versión del brand kit (V0.2, V1.0 post-validación, V1.1, V2, etc.) entra como **nuevo registro** en este archivo (no overwrite del registro V0.1). La versión anterior queda como histórico, con campo "Estado" actualizado a "Reemplazado por V<N>".

Mismo régimen para brand templates: nueva versión = nuevo registro, registro anterior pasa a "Reemplazado por V<N>".

### 4.4 Sincronización con KB markdown SSOT

- Si `brand-kit.md` (SSOT textual) cambia → Owner sincroniza manualmente a Canva UI (o vía MCP si existe `create-brand-kit` / `update-brand-kit` — verificar inventario tools).
- Si Owner edita brand kit directamente en Canva UI → debe reflejarlo en `brand-kit.md` Y en este archivo (entry de upgrade).
- **Anti-patrón.** Editar solo en Canva sin sincronizar a KB → drift entre SSOT textual y derivado Canva → riesgo §8.1.5 del proposal (ALTA si no hay disciplina).

---

## 5. Referencias cruzadas

- **SSOT textual brand kit:** `02-knowledge-base/02-domains/06-consultoria-externa/clientes/gama/brand-kit.md` (V0.1 candidato — paleta hex + tipografía + helpers python-pptx/docx/matplotlib).
- **Proposal Vivienne+Canva V1:** `04-system/03-governance/2026-05-18_proposal_vivienne-canva-mcp_v1.md` §3 (Brand kit + brand templates strategy).
- **DECISIONS.md entries Canva 2026-05-18:**
  - Resolución E1-E4 + directriz V0.1 CANDIDATO.
  - Adopción híbrido permanente Canva-layout + python-pptx-charts como default (ver §2.2 arriba).
- **Governance Canva Pro + split CORE:** `04-system/03-governance/2026-05-18_tools-split-policy_canva-pro-adoption.md`.
- **Commits V8.x baseline del PPTX original** (subconjunto de slides adaptado vía Gamma → upload Canva como regular design `DAHKE-vJnnU` — ver §2): `ca910fe` (V8), `4c8571b` (V8.1 charts nativos), `e715496` (V8.2 datos + contraste), `d13cd26` (V8.3 16:9). El PPTX V8.3 sigue siendo SSOT estructural en repo; el regular design Canva es derivado del subset Gamma de V8/V8.3.

---

*Archivo creado 2026-05-18 por Raul (Opus 4.7) tras setup operativo Canva del Owner (brand kit Gama subido + diseño base subido como regular design adaptado vía Gamma desde V8/V8.3). Documenta divergencias del plan original del proposal V1 (commit `c4147e5`) y la mitigación vía híbrido permanente. **Update 2026-05-18:** Owner confirmó datos del template (ID `DAHKE-vJnnU`, título `NOTORIEDAD-GAMA-2026.pptx`, tipo regular design, 20 páginas), URL real del scraping del brand kit (`empresa.gamaenlinea.com`, no `excelsiorgama.com` asumido), y diferimiento de cleanup del huérfano `kAHKE82Q8d8`. Path Vivienne operativo: `copy-design` desde `DAHKE-vJnnU`. Brand template oficial Pro queda como roadmap futuro.*
