---
documento: Política de split CORE vs Owner-selected en inventario de tools + adopción Canva Pro (scope Vivienne)
fecha: 2026-05-18
autor: Raul (Opus 4.7) — captura formal de 2 decisiones Owner interrelacionadas
status: ACTIVA — implementación documental inmediata; pilot Vivienne pendiente suscripción Owner + auth MCP
proyecto_base_canva: gama-notoriedad-2026 (consultoria-externa) — caso base próxima entrega Cora
alcance: política de inventario de tools del sistema + scope inicial de adopción Canva Pro
referencias_arquitectonicas: norte arquitectónico §0 (vendor-neutral) / principio transversal `portable_text_as_ssot_principle` / decisión 2026-04-25 (`DECISIONS.md`)
---

# Política de split CORE vs Owner-selected + adopción Canva Pro

> **Cómo leer este documento:** §1-2 capturan las dos decisiones con su contexto y rationale. §3 codifica la regla del fallback CORE que aplica a todos los agentes. §4 lista los próximos pasos en orden. §5 lista las decisiones Owner pendientes (escalaciones). Si tenés 5 minutos: leer §1, §2 y §3.

---

## 1. Decisión 1 — Adopción de Canva Pro (scope inicial: Vivienne)

**Decisión.** El Owner se suscribe a Canva Pro (plan anual, ~$120 USD/año) y autoriza el uso del **Canva MCP de claude.ai** (`mcp__claude_ai_Canva__*`, ~30 tools disponibles) como output engine **opcional** para Vivienne en su pipeline de presentaciones.

**Scope explícito.** El uso de Canva queda **limitado a Vivienne** en esta primera iteración. El path técnico es: Vivienne produce su outline VI-1 estructurado (Pirámide Minto, narrativa, jerarquía, brand kit consistency check) y luego invoca el MCP Canva para renderear el deck visual sobre ese outline.

**Caso base.** Próxima entrega Cora del proyecto `consultoria-externa/gama-notoriedad-2026` (V7 PPTX, pendiente arranque tras feedback Cora sobre V5+V6 Word).

**Rationale.**

- **Calidad visual** para entregas a clientes externos requiere un nivel que python-pptx + matplotlib alcanza con costo alto (líneas de código por slide, edición posterior incómoda, brand kit difícil de mantener consistente).
- **Pattern V5+V6** validó que Vivienne tiene fallas predecibles en decks grandes con charts python-pptx (token explosion >32K — memoria `feedback_vivienne_token_explosion_pattern_v1`). Un output engine externo descarga ese trabajo del modelo.
- **Editable post-render por el cliente** — un .pptx generado en Canva queda con structure nativa Canva, accesible al cliente para ajustes finos sin reabrir el pipeline interno.
- **MCP nativo en claude.ai** — no requiere infraestructura nueva ni scripts custom. Vivienne lo invoca como cualquier otra tool una vez auth.

**Alternativas consideradas.**

- *Quedarse solo con python-pptx + matplotlib (path actual).* Funciona pero arrastra los problemas de token explosion + tiempo de iteración + calidad visual limitada para entregas a clientes externos premium.
- *Adoptar Figma + Figma MCP en lugar de Canva.* Figma es más profesional pero el Owner ya tiene tracción visual + familiaridad con Canva, y el ecosistema de plantillas es mayor para outputs de consultoría. Diferido — re-evaluar si pilot Canva no convence.
- *Pasar a Beautiful.ai o Gamma.app.* Considerados — Canva gana por amplitud de uso del Owner en otras tareas (no solo agentes del repo).

**Implicaciones.**

- Pendiente acción Owner: completar suscripción anual + auth del MCP Canva en claude.ai.
- Pendiente edición runtime: actualizar `.claude/agents/vivienne/AGENT.md` con instrucciones de invocación Canva — **NO en esta sesión**. Va en proposal formal de upgrade Vivienne+Canva que se redacta cuando el MCP esté auth y el caso base esté listo.
- **Update 2026-05-18:** proposal formal `2026-05-18_proposal_vivienne-canva-mcp_v1.md` redactado y entregado en commit `c4147e5`. Las **4 decisiones Owner E1-E4** del proposal (brand kit scope / sharing permissions / retention / template approval) quedaron **RESUELTAS** por el Owner el 2026-05-18 con los defaults recomendados por Raul + directriz operativa adicional "Gama V0.1 CANDIDATO" para el período pre-validación con Cora. Ver proposal §9 para detalle.
- Inventario actualizado: entrada de Canva agregada a `TOOLS-OWNER-SELECTED.md` v0.1 con estado "PENDIENTE" (suscripción + auth).
- python-pptx + matplotlib **siguen siendo path default mantenido** en Vivienne. Canva es upgrade opcional, no reemplazo. Si el MCP falla o el Owner pausa la suscripción, Vivienne cae a path CORE sin pedir nada.

**Ampliación pendiente (NO ejecutar ahora).** Los siguientes agentes son **candidatos** a usar Canva como output engine secundario o primario una vez validado el pilot con Vivienne:

| Agente | Caso de uso potencial |
|---|---|
| **Atlas** | Mockups de empaque + arte de etiquetas |
| **Luma** | Visuales para contenido social (Genteca, marca personal) |
| **Orfeo** | Branding/identidad y visual concepts |
| **Oz (light)** | Borrador rápido de etiquetas antes de pasar a Oz real |

**Trigger de ampliación:** review formal post-pilot Vivienne — si los outputs Canva superan en calidad/velocidad al path python-pptx con criterios verificables (tiempo de producción, cantidad de ciclos cliente, calidad visual auto-evaluada), se autoriza extensión caso por caso. **Sin calendarización.**

---

## 2. Decisión 2 — Política de split CORE vs Owner-selected en inventario de tools

**Decisión.** La documentación de herramientas externas del sistema /RAUL/ vive a partir de 2026-05-18 en **dos listas separadas y explícitamente etiquetadas**:

| Archivo | Categoría | Definición operativa |
|---|---|---|
| `04-system/04-tools-and-scripts/TOOLS-REQUIREMENTS.md` | **CORE / agnósticas** | Open-source, requeridas para que el sistema funcione en cualquier clon del repo. Python, git, pandas, python-pptx, python-docx, PyMuPDF, reportlab, matplotlib, Pillow, pytesseract, Tesseract, Pandoc, etc. |
| `04-system/04-tools-and-scripts/TOOLS-OWNER-SELECTED.md` (NUEVO) | **Owner-selected / externas** | Paid o account-based, sustituibles. Claude Code CLI, Anthropic API, claude.ai MCPs, Canva Pro, Google Drive personal, OneDrive backup, Google AI Pro, Anthropic Routines, etc. |

**Rationale.**

- El repo /RAUL/ es **vendor-neutral por diseño** (norte arquitectónico §0 y principio transversal `portable_text_as_ssot_principle`).
- Mezclar tools comerciales del Owner con dependencias técnicas core confunde al clonador del repo sobre qué es **obligatorio** para que el sistema funcione vs qué es **elección comercial sustituible**.
- Cualquier instancia hipotética de /RAUL/ con otro Owner, otro stack comercial, otra cuenta de cloud, debe poder operar el sistema completo sin tener que adoptar las elecciones del Owner actual.

**Alternativas consideradas.**

- *Mantener una sola lista con tags `core` / `owner-selected`.* Rechazado por el Owner: confunde menos pero no impone la disciplina de separación — agentes y operadores pueden no leer la tag y tratar todo como "instalado".
- *No documentar las Owner-selected en absoluto* (asumir que son obvias desde `.claude/settings.local.json`). Rechazado: settings es permisos, no documenta scope ni fallback. Y el clonador del repo no debería tener que reverse-engineer las decisiones del Owner desde la configuración runtime.
- *Crear `TOOLS-OWNER-SELECTED.md` pero sin política de fallback CORE.* Rechazado: sin la regla del fallback, agentes podrían planificar outputs asumiendo siempre que la tool externa está disponible, y romperse silenciosamente cuando no lo esté.

**Implicaciones.**

- Creado `04-system/04-tools-and-scripts/TOOLS-OWNER-SELECTED.md` v0.1 (seed inicial, va a crecer).
- Actualizado `04-system/04-tools-and-scripts/TOOLS-REQUIREMENTS.md` a v1.1 con nota de scope al inicio que explica el split y referencia este governance doc.
- Esta política se vuelve **regla del repo** para futuras decisiones sobre tools: si una tool es paid o account-based, va a Owner-selected; si es open-source y obligatoria, va a CORE.

---

## 3. Regla operativa para todos los agentes — fallback CORE obligatorio

**Regla.** Cuando un agente planifique outputs considerando una tool Owner-selected, **debe mantener fallback CORE**. Los scripts existentes en el repo (python-pptx, python-docx, matplotlib, PyMuPDF, reportlab, Pillow, etc.) **NO se deprecan** al adoptar tools externas. Siguen siendo el **path default mantenido**.

**Cómo aplicar la regla:**

1. **Default = CORE.** El pipeline por defecto del agente usa scripts python existentes. Esto es lo que corre cuando la tool externa no está disponible.
2. **Owner-selected = upgrade opcional.** Si la tool externa está disponible (auth OK, scope habilitado para ese agente), el agente puede preferirla como output engine.
3. **Detección de no-disponibilidad = caída silenciosa.** Si la tool externa falla (MCP no conecta, auth caducada, error de API), el agente cae al path CORE **sin pedir input al Owner**. El Owner se entera del fallback en el reporte del agente, no como bloqueo.
4. **No deprecar scripts CORE existentes.** Aunque un agente migre 100% de su uso real a la tool Owner-selected, los scripts CORE se mantienen funcionales y testeados. Esto preserva la portabilidad del repo.

**Frase canónica para agentes:** *"Tools Owner-selected son mejor opción si están disponibles, no reemplazo del path CORE."*

---

## 4. Próximos pasos (orden de ejecución)

### Inmediato (esta sesión, 2026-05-18)

| # | Acción | Status |
|---|---|---|
| 4.1 | Crear `TOOLS-OWNER-SELECTED.md` v0.1 con seed inicial | DONE |
| 4.2 | Actualizar `TOOLS-REQUIREMENTS.md` a v1.1 con nota de scope | DONE |
| 4.3 | Crear este governance doc | DONE |
| 4.4 | Agregar entrada en `DECISIONS.md` referenciando este doc | DONE |
| 4.5 | Commit con mensaje claro referenciando las 2 decisiones | DONE |

### Acción Owner (fuera de la sesión Raul)

| # | Acción | Bloqueador para |
|---|---|---|
| 4.6 | Suscripción anual Canva Pro (~$120) | 4.7 |
| 4.7 | Auth del MCP Canva en claude.ai (`mcp__claude_ai_Canva__*` activo) | 4.8, pilot Vivienne |

### Próxima sesión (post-suscripción Owner)

| # | Acción | Effort estimado |
|---|---|---|
| 4.8 | Proposal formal upgrade Vivienne+Canva: editar `vivienne/AGENT.md` + actualizar conceptual SSOT con sección "Canva como output engine opcional" + protocolo de fallback CORE | 1-2 hr |
| 4.9 | Pilot Vivienne con caso base: V7 PPTX Cora (Notoriedad Gama) producido vía Canva | 1 sesión |
| 4.10 | Review post-pilot: comparar V7 Canva vs línea base python-pptx (tiempo, ciclos, calidad). Documentar en task-log y handoff. | 30 min |

### Diferido (post-review pilot)

| # | Acción | Trigger |
|---|---|---|
| 4.11 | Decisión Owner: extender Canva a Atlas / Luma / Orfeo / Oz light, o mantener limitado a Vivienne | Solo si pilot Vivienne convence |
| 4.12 | Si ampliación aprobada: proposal individual por agente (no batch) — cada uno con su pilot caso base | Caso por caso |

---

## 5. Decisiones Owner pendientes (escalaciones)

Detectadas durante captura de estas decisiones — no bloquean la implementación documental pero requieren atención eventual:

| # | Pendiente | Severidad | Recomendación |
|---|---|---|---|
| 5.1 | ¿Migrar también `LLM-GUIDELINES.md` (`04-system/01-config/`) al split CORE vs Owner-selected? Actualmente lista modelos Anthropic específicos (Opus 4.7, Sonnet 4.6, Haiku 4.5) que son Owner-selected, no CORE. | MEDIA | Diferir — no es urgente, pero próxima revisión de ese doc debería incluir nota tipo "los modelos listados son los del proveedor Anthropic; sustituibles por otros LLM providers" |
| 5.2 | ¿Settings de permisos en `.claude/settings.local.json` deberían referenciar este governance doc o el TOOLS-OWNER-SELECTED.md? | BAJA | Diferir — el settings es runtime de Claude Code (Owner-selected por definición); no necesita cross-reference si los docs nuevos están bien indexados |
| 5.3 | ~~Pilot Vivienne + Canva, ¿requiere validación adicional con Bruna (gate de gobernanza) sobre claims visuales/marca?~~ **RESUELTA 2026-05-18** vía decisión E4 del proposal (`2026-05-18_proposal_vivienne-canva-mcp_v1.md` §9 E4 — híbrido escalonado): Owner siempre + Bruna si hay claims visuales (badges, frases, iconos con significado regulatorio) + cliente si va a deck que se le presenta. | — | DONE — ver proposal §9 |

---

## 6. Patrón de referencia

Este doc sigue el patrón estructural del doc de lecciones V5+V6 (`04-system/03-governance/2026-05-18_LECCIONES-V5-V6-PLAN-EVOLUCION-SISTEMA.md`): frontmatter con metadata + resumen ejecutivo navegable + decisiones con rationale + alternativas + implicaciones + próximos pasos + escalaciones pendientes.

---

## Anexo — referencias cruzadas

- **Norte arquitectónico §0** — principio vendor-neutral fundacional
- **Memoria HOT** `project_arquitectura_norte_repo_raul.md` — captura el norte arquitectónico
- **Memoria HOT** `project_portable_text_as_ssot_principle.md` — principio transversal Markdown SSOT + binarios como derivados
- **DECISIONS.md 2026-04-25** — política agentes globales vs locales (precedente de doc separation por scope)
- **DECISIONS.md (esta misma fecha)** — entrada 2026-05-18 referenciando este governance doc
- **`TOOLS-REQUIREMENTS.md` v1.1** — inventario CORE actualizado
- **`TOOLS-OWNER-SELECTED.md` v0.1** — inventario Owner-selected nuevo
- **Memoria HOT** `feedback_vivienne_token_explosion_pattern_v1` — justifica adopción de output engine externo
- **Memoria HOT** `project_vivienne_upgrade_2026-05-18` — upgrade Bucket 1 + B3.4 aplicado a Vivienne; Canva es el siguiente upgrade lógico
- **Doc lecciones V5+V6** `2026-05-18_LECCIONES-V5-V6-PLAN-EVOLUCION-SISTEMA.md` — contexto operativo que motivó la búsqueda de output engines mejores

---

*Documento producido por Raul (Opus 4.7) el 2026-05-18 capturando dos decisiones Owner interrelacionadas. La parte documental (inventarios + este doc + DECISIONS) queda completa en esta sesión. La parte runtime (edición de `vivienne/AGENT.md` + conceptual SSOT + pilot caso base) queda explícitamente diferida al proposal formal de upgrade Vivienne+Canva en próxima sesión, post-suscripción y auth Owner.*
