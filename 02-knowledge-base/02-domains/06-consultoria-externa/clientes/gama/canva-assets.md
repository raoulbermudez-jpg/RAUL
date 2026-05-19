---
cliente: Gama (Cadena de Supermercados Gama Express)
canal_consultoria: Cora Urrea (cora.urrea@gmail.com)
proposito: Registro de assets Gama en Canva (brand kits + brand templates) — IDs, estado, divergencias del plan original
status: V0.1 — brand kit CANDIDATO (pendiente validación Cora); brand template basado en sample previo Gamma de Cora (no V8.3 PPTX repo)
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
| **Fuente de assets** | Web scraping de [excelsiorgama.com](https://excelsiorgama.com) (URL Excelsior Gama / Gama Express — verificar dominio exacto con Owner si difiere) |
| **SSOT textual de referencia** | `02-knowledge-base/02-domains/06-consultoria-externa/clientes/gama/brand-kit.md` |

### 1.1 Divergencia del plan original

El proposal Vivienne+Canva (`04-system/03-governance/2026-05-18_proposal_vivienne-canva-mcp_v1.md` §3.4) establecía que el brand kit Canva se ingiere desde el **markdown KB** como SSOT. En la práctica, Owner pobló el brand kit Canva por **web scraping de la web pública Gama** (excelsiorgama.com), no por sync manual desde el markdown KB.

**Implicación.** La web pública es **más autoritativa** en un sentido (refleja lo que Gama publica como sí misma hoy, sin curado interno) pero **menos curada** en otro (puede incluir paletas y assets de banners promocionales no-corporativos, ofertas estacionales, headers de campaña). El markdown KB sigue siendo el SSOT textual de referencia — Canva es derivado de la web, no del KB.

**Mitigación obligatoria.** Owner debe validar manualmente en la UI de Canva que los assets capturados por scraping no incluyan:

- Colores de banners promocionales no-corporativos (ej. fondos amarillos / verdes de campañas).
- Logos secundarios de marcas blancas / proveedores que aparezcan en la web.
- Tipografías de copy publicitario que no sean las tipografías corporativas oficiales.
- Imágenes / patterns de campañas estacionales.

Si el scraping capturó assets extra-corporativos, **limpiar en UI Canva antes de cualquier render Vivienne**. Documentar la limpieza en este archivo (próxima entry — campo "Notas de limpieza post-scraping").

### 1.2 Notas de limpieza post-scraping

*Pendiente — Owner pasará revisión manual en Canva UI y reportará qué assets requirieron descarte.*

---

## 2. Brand template Gama (V1 — pendiente confirmación nombre/ID)

| Campo | Valor |
|---|---|
| **ID Canva** | _Pendiente — Owner debe confirmar el ID del template subido_ |
| **Naming en Canva UI** | _Pendiente — sugerido: `Gama V0.1 CANDIDATO / Estudio Notoriedad / Template Maestro V1`_ |
| **Fecha creación** | 2026-05-18 |
| **Origen** | Sample previo que **Cora produjo con Gamma** (gamma.app) — **NO el V8.3 PPTX del repo** (commits `4c8571b`, `e715496`, `d13cd26`) |
| **Estado** | V0.1 CANDIDATO (mismo régimen que el brand kit; sufijo se quita post-validación Cora) |

### 2.1 Divergencia del plan original

El proposal §3.2 establecía el **V8.3 PPTX** (commit `d13cd26`) como brand template oficial Gama, justificado por: aspect ratio 16:9 correcto, datos correctos + heatmaps con contraste (V8.2), charts nativos editables (V8.1 — pedido Cora explícito), estructura Pirámide Minto visual, brand kit Gama aplicado consistente.

En la práctica, Owner subió como template un **sample previo producido por Cora con Gamma** — alineado al aesthetic aspiracional Cora pero estructuralmente distinto al V8.3.

**Implicación favorable.** Alinea Vivienne al aesthetic aspiracional de Cora **desde día uno**. Reduce el riesgo de entregar un PPTX que Cora considere visualmente "frío" o "consultor genérico" — el template ya refleja el lenguaje visual que Cora encuentra deseable.

**Implicación adversa.** Pierde la **validación estructural del V8.3**, específicamente:

- Charts nativos editables (commit `4c8571b` — pedido Cora explícito 2026-05-18).
- Aspect ratio 16:9 confirmado correcto (commit `d13cd26` — fix post V8.2).
- Layouts aprobados implícitamente por la cadena V8.0 → V8.3 (commits `ca910fe`, `4c8571b`, `e715496`, `d13cd26`).
- Brand kit Gama (rojo `#E30613`, Montserrat + Open Sans) aplicado consistente y revisado contra `brand-kit.md`.

Estos atributos del V8.3 **no están garantizados** en el template derivado de Gamma. Particularmente crítico: **Gamma no produce charts nativos editables** — exporta a PPTX aplanando charts como imágenes. Si Vivienne usa este template como base sin más, los charts del export Canva pueden quedar como imágenes, incumpliendo el pedido explícito Cora del commit `4c8571b`.

### 2.2 Mitigación — híbrido como default permanente

**El enfoque híbrido Canva-layout + python-pptx-charts queda adoptado como DEFAULT, no como contingencia/fallback al riesgo 8.1.6 del proposal.** Ver `DECISIONS.md` entry 2026-05-18 — "Híbrido permanente Canva layout + python-pptx charts".

Resumido: Canva genera layout + brand styling (heredando aesthetic Cora del template Gamma); python-pptx genera los slides de charts (heredando editabilidad y data binding exacto del V8.3); merge final via script Python o manual. La editabilidad de charts queda garantizada **independiente** del comportamiento del export Canva — no dependemos de Canva para charts.

### 2.3 Acción pendiente — confirmar nombre e ID del template con Owner

Owner aún no comunicó el nombre exacto ni el ID del brand template que subió. Acción: pedir confirmación en próximo turno. Una vez recibido, actualizar la tabla §2 de este archivo con el ID real + naming definitivo, y referenciar desde el proposal §3.2 + DECISIONS.md si procede.

---

## 3. Otros assets detectados en cuenta Canva

### 3.1 Brand kit huérfano `kAHKE82Q8d8`

| Campo | Valor |
|---|---|
| **ID Canva** | `kAHKE82Q8d8` |
| **Naming en Canva UI** | _Sin nombre — probablemente default Canva vacío_ |
| **Estado** | NO USAR |
| **Acción recomendada** | Owner puede borrarlo o renombrarlo en UI Canva para evitar ambigüedad operativa |

**Rationale.** Vivienne identifica brand kits por **ID** (no por nombre — ver política §4 abajo). Un brand kit con ID válido pero sin contenido relevante puede generar confusión en futuras llamadas `mcp__claude_ai_Canva__list-brand-kits` si Vivienne intenta auto-seleccionar. Cleanup proactivo (borrar o renombrar a `_VACIO_NO_USAR`) elimina el riesgo.

---

## 4. Política de identificación de assets Gama en Canva

### 4.1 Referencia por ID, no por nombre

**Vivienne debe referenciar brand kits y brand templates por su ID Canva** (`kAHKE4GYHQQ` para el brand kit, ID pendiente para el template), no por nombre. Razón: los nombres pueden cambiar (sufijo V0.1 CANDIDATO se quitará post-validación Cora; futuras versiones tendrán naming distinto); los IDs son inmutables.

**Implicación operativa para Vivienne.** Workflow §4 del proposal — paso 2 (smoke test) y paso 3 (create-design-from-brand-template) — debe consultar este archivo (`canva-assets.md`) para obtener el ID correcto del brand kit / template antes de invocar los tools MCP.

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
- **Commits V8.x baseline del template original V8.3 (no usado como template Canva — referencia estructural):** `ca910fe` (V8), `4c8571b` (V8.1 charts nativos), `e715496` (V8.2 datos + contraste), `d13cd26` (V8.3 16:9).

---

*Archivo creado 2026-05-18 por Raul (Opus 4.7) tras setup operativo Canva del Owner (brand kit Gama subido + brand template basado en sample Gamma de Cora). Documenta divergencias del plan original del proposal V1 (commit `c4147e5`) y la mitigación vía híbrido permanente. Pendiente: confirmar con Owner el nombre exacto y el ID del brand template (§2.3).*
