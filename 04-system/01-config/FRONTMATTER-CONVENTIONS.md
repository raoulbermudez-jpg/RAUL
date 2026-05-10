---
document_id: "FRONTMATTER-CONVENTIONS"
document_type: "system-convention"
purpose: "Convenciones canónicas para campos de frontmatter YAML en deliverables del sistema /RAUL/. Permite a agentes / Owner / cron tasks parsear estado, ownership y trazabilidad de cualquier pieza sin abrir el cuerpo del documento."
audience: ["Todos los agentes productores (Capa 2b CSC + Capa 3 dominios)", "InboxBot", "Owner"]
status: "active"
ssot_for: ["frontmatter-yaml-conventions"]
depends_on: ["GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md", "PENDING-DECISIONS-REGISTRY.md"]
version: "1.0"
last_updated: "2026-05-10"
---

# FRONTMATTER-CONVENTIONS.md

## Estándares de campos YAML para deliverables — Sistema /RAUL/

**Versión:** 1.0
**Última actualización:** 2026-05-10 (creación inicial — Phase 3 step 6)

Este documento define las **convenciones de frontmatter YAML** que cualquier deliverable producido por el sistema debe seguir. Complementa a `NAMING-CONVENTIONS.md` (que cubre nombres de carpetas y archivos) — el frontmatter es el otro vector estructural que permite a los agentes operar sobre piezas sin parsear su contenido.

---

## 1. Principios generales

- **Frontmatter es metadata estructurada.** No es contenido — es el "qué tipo de cosa es esto, en qué estado está, de quién depende".
- **Lectura programática.** Cualquier agente debe poder hacer `head -N` de un archivo y entender lo esencial sin leer el body.
- **Permisivo en lo no canónico.** Los campos canónicos (definidos aquí) son obligatorios o recomendados; otros campos ad-hoc son aceptables (ej. `audience`, `tags`) si aportan valor a un dominio específico.
- **Migración gradual.** Documentos legacy sin frontmatter NO se reescriben en masa. Solo deliverables nuevos deben cumplir la convención.

---

## 2. Campos canónicos

### 2.1 — `status` (obligatorio en deliverables nuevos)

**Propósito:** estado actual de la pieza en su ciclo de vida. Permite a Owner / agentes / cron tasks ver de un vistazo si una pieza está en draft, esperando aprobación, bloqueada por una decisión, etc.

**Valores canónicos:**

| Status | Significado | Quién lo setea |
|---|---|---|
| `DRAFT` | En desarrollo, no terminado | Agente productor durante producción |
| `IN-REVIEW-INTERNAL` | Producido, esperando validación de gate interno (Bruna, Vera, Vael, etc.) | Agente productor cuando termina draft |
| `AWAITING-DECISION-<id>` | Bloqueado pending decisión externa identificada por id (ej. `AWAITING-DECISION-DEC-2026-05-08-001`) | Agente que activa Pause+Resume |
| `IN-REVIEW-OWNER` | Aprobado por gates internos, esperando luz verde Owner | Cualquier agente |
| `APPROVED` | Owner aprobó, listo para distribución | Owner |
| `PUBLISHED` | Distribuido / entregado al destino final | Ivo (post-publication) |
| `ARCHIVED` | Movido a `05-archive/` (proyecto cerrado o pieza obsoleta) | Sira / Owner |
| `CRISIS-DRAFT` | Producido bajo Crisis override (patrón A.3), pending post-mortem Bruna | Agente que produjo bajo crisis |
| `WITHDRAWN` | Cancelado antes de publicación (por Owner / por riesgo) | Owner / Bruna |

**Reglas:**

1. **Todo deliverable producido por agente** debe tener `status` field en frontmatter. Migración gradual aceptable: piezas existentes pre-2026-05-10 pueden quedar sin field; piezas nuevas SÍ deben tenerlo.
2. **Default para legacy:** si un deliverable es viejo y no tiene este field, asumir `APPROVED` (conservador — la pieza ya está en uso).
3. **Cuando un deliverable cambia de estado**, se actualiza el field. Opcionalmente, log entry abajo del frontmatter (`## Status log`) para auditoría.
4. **Cuando estado es `AWAITING-DECISION-<id>`**, debe existir fila correspondiente en [`PENDING-DECISIONS-REGISTRY.md`](../03-governance/PENDING-DECISIONS-REGISTRY.md). El sufijo `<id>` es el `decision_id` exacto de esa fila.
5. **Transiciones inválidas a evitar:**
   - `PUBLISHED` → `DRAFT` (si una pieza publicada necesita revisión, abrir nueva versión, no degradar status).
   - `ARCHIVED` → cualquier otro (las piezas archivadas se reactivan creando deliverable nuevo, no cambiando status).
   - `WITHDRAWN` → `PUBLISHED` directo (debe pasar por `IN-REVIEW-*` y nuevo `APPROVED`).

**Ejemplos de uso:**

```yaml
---
document_id: "GME-launch-press-release"
status: "AWAITING-DECISION-DEC-2026-05-06-001"
agent_producing: "Solenne"
# ... resto del frontmatter
---
```

```yaml
---
document_id: "GST-R-etiqueta-final-v3"
status: "APPROVED"
approved_by: "OWNER"
approved_date: "2026-05-04"
# ...
---
```

---

### 2.2 — Otros campos comunes (recomendados, no obligatorios)

Estos campos aparecen recurrentemente en docs del sistema. NO son obligatorios pero seguir el naming canónico facilita parsing:

| Campo | Tipo | Uso típico |
|---|---|---|
| `document_id` | string | ID corto único del deliverable (kebab-case o slug). Útil para cross-referencing. |
| `document_type` | string | Categoría: `governance-registry`, `kb-article`, `decision-package`, `csc-deliverable`, etc. |
| `agent_producing` | string | Nombre del agente que produjo (Bruna, Vael, Atlas, etc.). |
| `agent_solicitante` | string | Para decision packages: agente que activó Pause+Resume. |
| `decision_id` | string | Para piezas vinculadas a decisión: `DEC-YYYY-MM-DD-NNN`. |
| `project_id` | string | Slug del proyecto asociado (kebab-case). |
| `domain` | string | `genteca`, `plenus`, `finca`, `teca`, `marca-personal`, `panama`, `cross-cutting`. |
| `creation_date` / `last_updated` | string YYYY-MM-DD | Fechas. |
| `version` | string | Versión semántica (`1.0`, `1.1`, etc.) o secuencial (`v3`). |
| `depends_on` | list[string] | Paths a docs upstream que este pieza depende de. |
| `ssot_for` | list[string] | Conceptos para los cuales este doc es Single Source of Truth. |
| `audience` | list[string] | Roles / agentes destinatarios. |
| `purpose` | string | Una línea explicando el porqué del doc. |
| `how_to_use` | string | Guía breve de uso. |

---

### 2.3 — Decision packages (frontmatter específico)

Para deliverables que son packages de decisión (viven en `01-inbox/04-decisions-in-flight/<project-id>/<decision-id>/`), usar el template canónico [`decision-request-template.md`](../04-tools-and-scripts/templates/decision-request-template.md), que ya incluye los campos requeridos:

- `decision_id`, `project`, `piece`, `agent_requesting`, `decisor`, `date_request`, `deadline`, `canal`, `status`.

Ver también [`alternative-proposal-template.md`](../04-tools-and-scripts/templates/alternative-proposal-template.md), [`regulator-submission-template.md`](../04-tools-and-scripts/templates/regulator-submission-template.md), [`junta-decision-package-template.md`](../04-tools-and-scripts/templates/junta-decision-package-template.md).

---

## 3. Por definir (futuras convenciones)

Espacio para campos que se irán formalizando conforme aparezcan necesidades:

- **`risk_level`** — etiqueta de riesgo (`LOW`/`MEDIUM`/`HIGH`/`CRITICAL`) para piezas que pasaron por Bruna. Pendiente decisión Owner sobre si se duplica info de BR-X o se mantiene solo en governance log.
- **`expiry_date`** — fecha tras la cual una pieza requiere revisión obligatoria (ej. claims regulatorios con plazo de validez).
- **`channel_published`** — para piezas con `status: PUBLISHED`, lista de canales donde se distribuyó (LinkedIn, email, web, etc.). Útil para Ivo + Sira.
- **`reuse_potential`** — etiqueta `HIGH`/`MEDIUM`/`LOW` para piezas candidatas a reciclaje (input para Sira via AU-5).

Cada uno se resuelve caso a caso y se registra aquí + en `DECISIONS.md` cuando surja el primer precedente.

---

## 4. Validación automática (futura)

Pendiente: script de validación que escanee deliverables nuevos y flag piezas que:

- Tienen `status: AWAITING-DECISION-<id>` pero el `<id>` no existe en `PENDING-DECISIONS-REGISTRY.md`.
- Tienen `status: PUBLISHED` pero sin `channel_published`.
- Tienen `status: APPROVED` por más de 90 días sin transición a `PUBLISHED` o `WITHDRAWN`.

Cuando se implemente, se documentará aquí + en `04-system/04-tools-and-scripts/`.

---

## Referencias

- [`NAMING-CONVENTIONS.md`](NAMING-CONVENTIONS.md) — convenciones de nombres de archivo y carpeta (complementario).
- [`PENDING-DECISIONS-REGISTRY.md`](../03-governance/PENDING-DECISIONS-REGISTRY.md) — registry de decisiones in-flight (referenciado por `status: AWAITING-DECISION-<id>`).
- [`DECISION-MAKERS.md`](../03-governance/DECISION-MAKERS.md) — IDs de decisores referenciados en frontmatter de decision packages.
- [`GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md`](../03-governance/GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md) sección C — origen de la convención `status`.
- Templates en [`04-system/04-tools-and-scripts/templates/`](../04-tools-and-scripts/templates/) — frontmatter pre-poblado para casos comunes.

---

## Notas de versión

- **v1.0 — 2026-05-10** — creación inicial. Documenta `status` field convention (Phase 3 step 6 del plan governance). Campos comunes recomendados. Templates linkeados.
