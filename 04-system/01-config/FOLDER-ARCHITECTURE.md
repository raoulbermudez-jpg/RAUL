# FOLDER-ARCHITECTURE.md
## Sistema Raul 2026 — Local-first · Vendor-neutral · Multi-LLM

**Versión:** 2.1
**Última actualización:** 2026-04-21
**Decisión registrada en:** `04-system/03-governance/DECISIONS.md`

Este documento define la arquitectura de carpetas del sistema Raul.

Objetivos:

- **Local-first / App-less**: el sistema de archivos es la base de datos.
- **Vendor-neutral**: nada depende de Notion, Obsidian, SaaS o bases propietarias.
- **Multi-LLM**: cualquier modelo (Claude, GPT, Gemini, etc.) puede operar.
- **Soporte amplio**: content supply chain (Capas 2–5), investigación, consultoría, proyectos diversos y temas no relacionados.
- **Bajo lock-in**: Markdown + carpetas claras, fácil de migrar y mantener.
- **Eficiencia en tokens**: carga por capas (core + dominio) para no saturar contexto.

Para reglas finas de nombres de carpetas y archivos, ver `04-system/01-config/NAMING-CONVENTIONS.md`. Para el plan de migración desde la estructura previa, ver `04-system/03-governance/MIGRATION-PLAN.md`.

---

## 1. Vista general del árbol

Raíz lógica del sistema:

```text
/RAUL/
  .claude/             ← runtime de Claude Code (NO mover — convención del tool)
    agents/            ← derivados de /04-system/02-agents/conceptual/
  01-inbox/            ← entrada/salida direccional y raw sources
  02-knowledge-base/   ← wiki compilada (LLM-first) + specs + assets por dominio
  03-projects/         ← trabajo operativo por dominio/proyecto
  04-system/           ← reglas, agentes, routing, config
  05-archive/          ← histórico y snapshots
```

Cualquier cambio estructural debe actualizarse aquí y en `/RAUL/04-system/03-governance/DECISIONS.md`.

**Nota sobre `.claude/`:** vive en raíz porque Claude Code busca `.claude/agents/` relativo al directorio donde se abre la CLI. Mover `.claude/` rompe la delegación de subagentes. La fuente conceptual vive en `/RAUL/04-system/02-agents/conceptual/`; lo de `.claude/agents/` es derivado (ver §5).

---

## 2. 01-inbox/ — Entrada e ingesta (direccional)

Función: capturar entradas desde el Owner, entregas desde Raul, y fuentes externas crudas.

```text
/RAUL/01-inbox/
  01-owner-to-raul/             ← Owner → Raul (tareas, briefs, pedidos)
  02-deliverables-to-owner/     ← Raul → Owner (entregas, borradores, versiones para revisar)
  03-raw-sources/               ← insumos crudos (fuentes sin procesar para compilar)
  README.md
```

- `01-owner-to-raul/`
  - Briefs, pedidos, prompts en texto, archivos que el Owner sube (Drive, email, móvil).
  - Bots o scripts leen aquí periódicamente y crean/actualizan proyectos en `03-projects/`.

- `02-deliverables-to-owner/`
  - Entregas de Raul al Owner: informes, presentaciones, piezas finales o borradores para revisión.
  - Semánticamente es outbox; se agrupa bajo `01-inbox/` para mantener un solo hub de I/O.

- `03-raw-sources/`
  - PDFs, transcripciones, capturas, artículos web, etc. aún no procesados.
  - Lo valioso se compila después a `02-knowledge-base/` o a un proyecto en `03-projects/`.

- `README.md`
  - Explica qué tipo de archivos admite cada subcarpeta, quién los deposita, cómo se procesan, qué agente/bot los atiende.

---

## 3. 02-knowledge-base/ — LLM Wiki + specs + assets compilados

Función: memoria acumulativa de Raul. Aquí vive el conocimiento estable (wiki), los documentos de especificación por dominio (datasheets, catálogos) y los assets visuales específicos de cada dominio.

```text
/RAUL/02-knowledge-base/
  _index.md
  01-foundations/
    01-methodology.md
    02-local-first-philosophy.md
    03-llm-usage-patterns.md
  02-domains/
    01-genteca/
      _index.md
      wiki/                    ← artículos de conocimiento del dominio
        01-fundamentos-tecnicos.md
        02-proteccion-motores.md
        ...
        market/                ← market intelligence específico de Genteca (provisional)
      specs/                   ← hojas de especificación, catálogos, datasheets de producto
        _index-specs.md
        <documentos de producto>
      assets/                  ← fotos, packaging, diagramas eléctricos, fichas visuales
        products/
        packaging/
        diagrams/
        uncoded/
    02-finca-ganaderia/
      _index.md
      wiki/
      specs/                   ← solo si aplica
      assets/                  ← fotos de finca, material agro, etc.
    03-plenus-metabolica/      ← Raoul's Products: alimentos funcionales, salud metabólica, longevidad
      _index.md
      wiki/
      specs/
      assets/                  ← mockups empaques, etiquetas, creatividades Plenus
    04-teca-teak4food/         ← marca Teak4Food (NO alimentos funcionales)
      _index.md
      wiki/
      specs/
      assets/                  ← fotos de finca, branding Teak4Food, material comercial agro
    05-marca-personal-raoul/   ← marca personal Raoul (distinta de Plenus)
      _index.md
      wiki/
      assets/                  ← fotos personales, branding personal, materiales de charla
    99-other-domains/
      _index.md
  03-cross-cutting/            ← temas transversales que no encajan en un dominio
    01-ai-systems-and-agents.md
    02-marketing-tecnico.md
    03-microbiota-y-fermentos.md
    04-salud-metabolica.md
    assets/                    ← íconos genéricos, plantillas comunes, material realmente transversal
  04-sops-and-playbooks/       ← SOPs generales NO específicos de content supply chain
    01-investigacion-tecnica-SOP.md
    02-evaluacion-papers-SOP.md
    03-consultoria-ingenieria-SOP.md
  05-glossary-and-tables/
    glossary-tecnico.md
    reference-tables.md
```

**Distinción `wiki/` vs `specs/` vs `assets/` (clave):**

| Subcarpeta | Qué contiene | Quién produce | Quién consume |
|---|---|---|---|
| `wiki/` | Artículos compilados y curados sobre el dominio (fundamentos, guías, patrones, lecciones aprendidas) | Paxs + especialistas del dominio compilando desde `01-inbox/03-raw-sources/` y proyectos cerrados | Todos los agentes como contexto persistente |
| `specs/` | Hojas de especificación de producto, datasheets, catálogos comerciales, manuales | Celeste (intake de raw → formato estable) | Vera/Orlan/Oz y agentes que necesitan datos exactos |
| `assets/` | Material visual específico del dominio (fotos, diagramas, mockups, iconografía de marca) | Dominio (Ozwaldo en Genteca, equivalentes en otros) | Capa 3 de producción (Atlas, Luma) y comunicación |

Un dominio puede tener solo `wiki/` (ej. marca personal sin specs), `wiki/ + assets/` (ej. Finca), o los tres (Genteca, Plenus, Teca).

**Regla de assets:**
- Assets **específicos de un dominio** → dentro del dominio (`02-domains/<dominio>/assets/`).
- Assets **realmente transversales** (íconos genéricos, plantillas) → `03-cross-cutting/assets/`.
- No existe un `/02-assets/` top-level; la regla es domain-first.

**Principios:**

- Todo aquí es Markdown (excepto binarios obvios en `assets/` y `specs/` cuando aplique).
- Cada dominio tiene `_index.md` que define alcance, marcas implicadas, tipos de proyectos típicos, y enlaces a proyectos relevantes de `03-projects/`.
- Content supply chain (ARCHITECTURE, AGENTS, ROUTING, RUNBOOK, SOPs de cadena) vive en `04-system/`, **no se duplica aquí**.

---

## 4. 03-projects/ — Trabajo operativo por dominio y proyecto

Función: ejecutar trabajo concreto — campañas, consultorías, investigación, scripts, etc. Organización: dominio → proyecto (con estados 00–04).

```text
/RAUL/03-projects/
  genteca/
    2026-04_GST-R_etiquetas/
      00-brief/
      01-strategy-and-design/
      02-production/
      03-review-and-release/
      04-published-and-hand-off/
      README.md
    2026-04_GSM-MB-RB-RF_empaque/
      (misma estructura 00→04)
  finca-ganaderia/
    2026-05_rotacion_potreros/
      00-brief/
      01-research-and-models/
      02-simulations-and-scenarios/
      03-recommendations-and-report/
      04-client-deliverables/
      README.md
  plenus-metabolica/
  teca-teak4food/
  marca-personal-raoul/
  research-generic/
    2026-05_cancer-metabolico-review/
      00-brief/
      01-literature-mapping/
      02-deep-dive-notes/
      03-synthesis-and-diagrams/
      04-paper-or-report-draft/
      README.md
  sandbox-and-experiments/
    2026-05_llm-evaluations/
    2026-05_new-fermentation-protocols/
```

**Convenciones:**

- Carpeta de proyecto: `YYYY-MM_slug-descriptivo/`.
- Estados típicos (adaptables por tipo de proyecto):
  - `00-brief/` — pedido, contexto, constraints.
  - `01-strategy-and-design/` o `01-research-and-models/`.
  - `02-production/` — contenido, análisis, código, borradores.
  - `03-review-and-release/` o `03-recommendations/`.
  - `04-published-and-hand-off/` — entregables finales, logs de publicación, notas para Sira.
- `README.md` por proyecto: objetivo, stakeholders, enlaces a KB, estado actual, decisiones clave.
- Aquí pueden convivir Markdown, código, binarios (PDFs/PPTX/imágenes) y datos.

**Disciplinas deliberadamente abiertas:**

- `sandbox-and-experiments/`: reglas de promoción a proyecto formal se deciden caso a caso y se registran en `DECISIONS.md` cuando surja el primer precedente.
- `research-generic/` vs dominio específico: mismo criterio — caso a caso cuando aparezca el primer precedente.

**Política git (resumen — detalle en §10):** binarios pesados gitignored por defecto. Markdown y código se versionan.

---

## 5. 04-system/ — Reglas, agentes, routing, configuración

Función: cerebro del sistema Raul. Define cómo se trabaja, no el trabajo en sí.

```text
/RAUL/04-system/
  01-config/
    CLAUDE.md               ← instrucciones maestras para agentes
    CONTEXT.md              ← contexto ampliado complementario a CLAUDE.md
    LLM-GUIDELINES.md       ← cómo usar Claude, GPT, etc.
    NAMING-CONVENTIONS.md   ← estándares de nombres (carpetas/archivos)
    FOLDER-ARCHITECTURE.md  ← ESTE documento
    CLAUDE-CODE-RULES.md    ← reglas de operación de Claude Code en este repo
    # (futuros — ver §8)
    CLAUDE_core.md          ← núcleo compacto para cargar siempre
    CONTEXT_core.md         ← contexto breve general
    CLAUDE_<domain>.md      ← reglas específicas por dominio
    CONTEXT_<domain>.md     ← contexto específico por dominio
  02-agents/
    conceptual/             ← FUENTE DE VERDAD (vendor-neutral)
      aurelio.md
      nerea.md
      orfeo.md
      luma.md
      vela.md
      atlas.md
      bruna.md
      ivo.md
      sira.md
      ...
    content-supply-chain/
      ARCHITECTURE_Content-Supply-Chain.md
      AGENTS_Content-Supply-Chain.md
      ROUTING-GUIDE.md
      RUNBOOK_Raul_Global.md
  03-governance/
    DECISIONS.md            ← log de decisiones arquitectónicas
    MIGRATION-PLAN.md       ← plan de fases para reorganizaciones
    task-log.md             ← log operativo de delegaciones
    RISK-POLICY.md
    SECURITY-AND-ACCESS.md
  04-tools-and-scripts/
    scripts/
      ocr_stubs.py
      descargar_genteca_v2.py
      inbox_bot.py
      ...
    templates/
      project-template/README.md
      sop-template.md
      report-template.md
  05-indexes/
    projects-index.md       ← índice ligero de proyectos activos
    kb-index-by-domain.md   ← índice de KB por dominio
    research-index.md       ← líneas de investigación abiertas
```

**Regla de agentes (SSOT):**

- **`02-agents/conceptual/*.md`** es la **fuente de verdad**. Describe misión, alcance, inputs/outputs, interacciones y flujos — vendor-neutral, sin frontmatter de runtime.
- **`/RAUL/.claude/agents/<nombre>/AGENT.md`** es **derivado**. Se produce a partir de su equivalente en `conceptual/` añadiendo frontmatter específico de Claude Code (`name`, `description`, `model`, `tools`).
- **Orden de edición:** siempre editar `conceptual/` primero; luego actualizar el derivado.
- **Futuro:** cuando haya segundo LLM operando, se crea otro derivado paralelo (ej. `/RAUL/.openai/agents/`) desde el mismo `conceptual/`. Nunca dos fuentes sin un maestro.

**Content supply chain:** se mantiene solo aquí para no duplicar single source of truth.

**Relación `CLAUDE.md` ↔ `CONTEXT.md`:**

- `CLAUDE.md` = sistema maestro: reglas globales, estilo, políticas de uso de LLMs, filosofía de trabajo.
- `CONTEXT.md` = contexto ampliado complementario a CLAUDE.md: historia, background detallado, ejemplos, info "lenta" que no cambia a diario. Debe empezar declarando su rol: "Contexto ampliado complementario a CLAUDE.md".

---

## 6. 05-archive/ — Histórico

Función: memoria fría, baja rotación, pero valiosa.

```text
/RAUL/05-archive/
  01-knowledge-base-old/
    snapshots-YYYY-MM/
  02-projects-completed/
    2023/
    2024/
    2025/
  03-system-history/
    CHANGELOG-system.md
    old-CLAUDE-configs/
    old-routing-guides/
  04-research-parked/
    temas-aparcados-sin-prioridad.md
```

- Nada aquí se edita en el día a día.
- Si algo vuelve a ser relevante, se trae a `02-knowledge-base/` o `03-projects/`.

---

## 7. Principios de uso para LLMs y agentes

Para cualquier LLM que trabaje en este sistema:

1. **Punto de entrada:** leer primero `/RAUL/04-system/01-config/CLAUDE.md` (o `CLAUDE_core.md` cuando esté disponible), `FOLDER-ARCHITECTURE.md`, `NAMING-CONVENTIONS.md`.
2. **Identificar tipo de tarea:**
   - Ingesta / bandejas → `01-inbox/`
   - Conocimiento estable → `02-knowledge-base/`
   - Trabajo de proyecto → `03-projects/`
   - Reglas y agentes → `04-system/`
   - Histórico → `05-archive/`
3. **Compilar antes que saturar contexto:** sintetizar material crudo en artículos `.md` en `02-knowledge-base/` o dossiers en `03-projects/`. No trabajar siempre sobre decenas de PDFs.
4. **Respetar vendor-neutralidad:** no introducir dependencias a formatos propietarios o nombres de herramientas. Todo conocimiento clave en `.md` legible por cualquier editor.
5. **Minimizar tokens:** consultar índices (`_index.md`, `projects-index.md`, `kb-index-by-domain.md`) antes de abrir rutas masivamente. Trabajar por dominio/proyecto.
6. **Cargar por capas** según el tipo de tarea (ver §8).

---

## 8. Estrategia de contexto — core + por dominio (optimización de tokens)

Principio: **no todo el sistema debe cargarse en cada sesión**. La carga es por capas según la tarea.

### 8.1 Nivel core (siempre cargado)

Archivos pequeños, compactos, que cualquier agente puede leer sin costo significativo de tokens.

| Archivo | Tamaño objetivo | Contenido |
|---|---|---|
| `CLAUDE_core.md` | 1–2k tokens máximo | Filosofía de trabajo, reglas globales, estilo general de respuestas, políticas de seguridad y vendor-neutralidad |
| `CONTEXT_core.md` | 200–500 tokens | Descripción breve de dominios, cómo usar el árbol `/RAUL/`, rol general de los agentes principales |

**Uso:** se cargan siempre, en toda sesión, independientemente del dominio de la tarea. Son la entrada universal.

### 8.2 Nivel dominio (cargado on-demand)

Archivos específicos de un dominio, cargados solo cuando la tarea lo requiere.

| Archivo | Contenido |
|---|---|
| `CLAUDE_<domain>.md` | Reglas específicas de ese dominio: tono, constraints, prioridades, vocabulario obligado, terminología a evitar |
| `CONTEXT_<domain>.md` | Productos/servicios clave, marcas implicadas, vocabulario típico, restricciones relevantes, stakeholders |

Dominios previstos como piloto (orden de prioridad):
1. `genteca` — primero por ser el dominio con más actividad.
2. `plenus-metabolica`
3. `teca-teak4food`
4. `marca-personal-raoul`

### 8.3 Patrón de carga

| Tipo de tarea | Archivos cargados |
|---|---|
| Tarea general, multi-dominio o de sistema | `CLAUDE_core.md` + `CONTEXT_core.md` |
| Tarea específica de un dominio | core + `CLAUDE_<domain>.md` + `CONTEXT_<domain>.md` |
| Tarea con documentos técnicos puntuales | lo anterior + archivos KB específicos por cita, no masivos |

### 8.4 Generación e implementación

- `CLAUDE_core.md` y `CONTEXT_core.md` se extraen de los `CLAUDE.md` / `CONTEXT.md` actuales como destilación compacta. Los largos se preservan como referencia ampliada.
- El primer piloto por dominio (`CLAUDE_genteca.md` + `CONTEXT_genteca.md`) se diseña cuando el sistema ya esté migrado y estable.
- Ver `MIGRATION-PLAN.md` fase 6 para el detalle operativo.

### 8.5 Mantenimiento

- Cambios en reglas globales → `CLAUDE_core.md` + decisión en `DECISIONS.md`.
- Cambios en contexto de un dominio (nuevo producto, nueva marca, cambio de posicionamiento) → `CONTEXT_<domain>.md`.
- Cualquier agente que necesite reglas/contexto de un dominio debe cargarlos explícitamente al inicio de la tarea; no suponer que están ya en sesión.

---

## 9. Roadmap y cambios futuros

- Roadmap vivo en `/RAUL/04-system/03-governance/DECISIONS.md`.
- Plan de migración desde estado previo en `/RAUL/04-system/03-governance/MIGRATION-PLAN.md`.

Disparadores para refactors futuros:

- Nuevas marcas o líneas de dominio → nuevo `02-domains/<dominio>/`.
- Refactors de `02-knowledge-base/` basados en patrones reales de uso.
- Revisión de estrategia git cuando `03-projects/` crezca.
- Ajustes en `01-inbox/` al añadir nuevas fuentes remotas (APIs, S3).
- Si el marketing cross-dominio crece, reevaluar ascender parte de Genteca/wiki/market/ a `03-cross-cutting/02-marketing-tecnico.md`.

---

## 10. Implementación física

Esta sección fija decisiones concretas de infraestructura. Sin ellas, la arquitectura es abstracta.

### 10.1 Ubicación en disco

- Raíz: `C:\RAUL\` (Windows, máquina del Owner).
- Pendiente: definir si `/RAUL/` también reside en otro host (backup server, NAS, etc.).

### 10.2 Estrategia git

- **Repo git = todo `/RAUL/` con `.gitignore` estricto.**
- **Se versiona:**
  - Todo `04-system/` (reglas, agentes, scripts, templates).
  - Todo `02-knowledge-base/` excepto binarios pesados.
  - `03-projects/**/*.md` y `03-projects/**/*.py` y equivalentes texto/código.
  - `.claude/agents/` (derivado pero útil para quien clona).
  - `01-inbox/README.md` y equivalentes.
- **Se ignora:**
  - `01-inbox/03-raw-sources/` entero (PDFs, imágenes, transcripciones crudas).
  - `01-inbox/01-owner-to-raul/` y `02-deliverables-to-owner/` (son buzones operativos).
  - `03-projects/**/*.{pdf,pptx,docx,xlsx,png,jpg,jpeg,mp4,mov,wav,mp3}` y similares.
  - `02-knowledge-base/**/assets/**/*.{jpg,png,mp4,...}` (binarios pesados).
  - `05-archive/` entero (se respalda aparte, no se versiona).

Ejemplo `.gitignore` inicial:

```gitignore
/01-inbox/01-owner-to-raul/
/01-inbox/02-deliverables-to-owner/
/01-inbox/03-raw-sources/
/05-archive/
*.pdf
*.pptx
*.docx
*.xlsx
*.png
*.jpg
*.jpeg
*.mp4
*.mov
*.wav
*.mp3
!/02-knowledge-base/**/specs/**/*.pdf  # excepciones si una spec vive como PDF
```

### 10.3 Google Drive mirror

- **Mirroreadas a Drive:**
  - `/RAUL/01-inbox/01-owner-to-raul/`
  - `/RAUL/01-inbox/02-deliverables-to-owner/`
  - `/RAUL/02-knowledge-base/` (para consulta remota)
- **NO mirroreadas:**
  - `/RAUL/04-system/` (vive en git, no necesita Drive).
  - `/RAUL/03-projects/` (local + git; si el Owner necesita acceso puntual, se exporta entregable específico a `01-inbox/02-deliverables-to-owner/`).
  - `/RAUL/05-archive/` (backup aparte).

Configuración concreta de Drive Desktop: mapear solo las carpetas listadas arriba.

### 10.4 InboxBot

- El trigger actual `trig_01RgGGbpCvckUzSwkyGMDNtm` apunta a rutas antiguas. Se **re-crea** con nuevos paths:
  - Lectura: `G:\Mi unidad\RAUL\01-inbox\01-owner-to-raul\`
  - Escritura (drafts Gmail, marcadores DONE_): sin cambio conceptual.
- Detalle de reconfiguración en `MIGRATION-PLAN.md` fase 4.

### 10.5 Backup

- `05-archive/` se respalda a un destino externo (ej. segundo disco, NAS, o cold storage).
- Política sugerida: snapshot mensual de `/RAUL/` completo excluyendo `05-archive/` (que ya es archivo).

---

## 11. Ciclo de vida de proyectos

- **Activo:** vive en `03-projects/<dominio>/<proyecto>/`.
- **Publicado pero vigente:** permanece en `03-projects/<dominio>/<proyecto>/04-published-and-hand-off/`.
- **Archivado:** se mueve a `05-archive/02-projects-completed/<año>/<proyecto>/` cuando Sira lo propone y el Owner aprueba. Criterio inicial sugerido: sin actividad 90 días tras quedar en estado `04-published-and-hand-off/`.

---

Fin de FOLDER-ARCHITECTURE.md v2.1
