# TOOLS-OWNER-SELECTED.md
## Inventario de herramientas externas elegidas por el Owner — sistema /RAUL/

**Versión:** 0.1 (seed inicial — va a crecer)
**Última actualización:** 2026-05-18
**Decisión que origina este archivo:** `04-system/03-governance/2026-05-18_tools-split-policy_canva-pro-adoption.md`

---

## Por qué este archivo existe (split CORE vs Owner-selected)

El repo /RAUL/ es **vendor-neutral por diseño** (ver norte arquitectónico §0 y el principio transversal `portable_text_as_ssot_principle` en memoria HOT). Esto significa que un clon limpio del repo, en otra máquina, con otro Owner y otro stack de herramientas comerciales, debe poder operar el sistema completo sin tener que adoptar las elecciones comerciales del Owner actual.

Mezclar tools comerciales del Owner (Claude Code, Canva Pro, claude.ai MCPs, Google Drive personal, etc.) con dependencias técnicas core (Python, git, pandas, python-pptx, PyMuPDF) en un único inventario confunde al clonador sobre qué es **obligatorio** para que el sistema funcione vs qué es **elección comercial sustituible**.

Por eso desde 2026-05-18 la documentación de tools vive en dos listas:

| Archivo | Qué lista | A quién aplica |
|---|---|---|
| `TOOLS-REQUIREMENTS.md` | **CORE** — open-source, requeridas para que los scripts del sistema corran | Cualquier clonador del repo, obligatorio |
| `TOOLS-OWNER-SELECTED.md` (este archivo) | **Owner-selected** — paid o account-based, sustituibles por alternativas | Solo el Owner actual; informativo para clonadores |

---

## Regla operativa para agentes

Cuando un agente planifique outputs considerando una tool Owner-selected, **debe mantener fallback CORE**. Los scripts existentes (python-pptx, matplotlib, python-docx, PyMuPDF, reportlab, etc.) **NO se deprecan** al adoptar tools externas — siguen siendo el path default mantenido.

Tools Owner-selected son **"mejor opción si está disponible"**, no reemplazo. Si la tool externa no está disponible (cuenta caducada, MCP no conectado, sin auth), el agente cae al path CORE sin pedirle nada al Owner.

---

## Inventario v0.1 — tools Owner-selected en uso o pendientes

### Runtime y modelo

| Tool | Estado | Scope de uso | Sustituible por (CORE / alt) | Fallback CORE si no disponible | Notas |
|---|---|---|---|---|---|
| **Claude Code CLI** | Activo | Runtime principal — todos los agentes corren acá | Otro runtime LLM con tools equivalentes (Cursor, Aider, Goose, custom MCP host); o ejecución manual con instrucciones del SSOT conceptual | Cualquier sesión humana puede operar leyendo `04-system/02-agents/conceptual/*.md` y siguiendo los protocolos manualmente | Configurado en `.claude/agents/` (runtime adapters) y `.claude/settings.local.json` |
| **Anthropic API** (Opus 4.7, Sonnet 4.6, Haiku 4.5) | Activo | Modelos LLM detrás de Claude Code y de las Cloud Routines | Otros LLM providers (OpenAI, Gemini, local models vía Ollama). El sistema es multi-LLM por diseño. | Los agentes están escritos en lenguaje vendor-neutral en el conceptual SSOT; cambiar provider requiere reescribir frontmatter de los AGENT.md pero NO los conceptuales | Ver `04-system/01-config/LLM-GUIDELINES.md` para política de asignación de modelos |

### MCPs de claude.ai (en uso visible en `.claude/settings.local.json`)

| Tool | Estado | Scope de uso | Sustituible por | Fallback CORE | Notas |
|---|---|---|---|---|---|
| **Google Drive MCP** (`mcp__claude_ai_Google_Drive__*`) | Activo | Búsqueda y creación de archivos en Drive del Owner | Acción manual del Owner (drag-drop, web Drive); rclone CLI; gdrive CLI | Owner sube/baja archivos manualmente; agentes producen entregables en filesystem local | Permisos: `create_file`, `search_files` |
| **Gmail MCP** (`mcp__claude_ai_Gmail__*`) | Activo | Creación de drafts de email | Owner redacta manualmente desde el draft `.md` que el agente produce | Agente entrega draft en `.md`, Owner lo copia/pega en Gmail | Limitación documentada: solo `create_draft`, no envío ni adjuntos (memoria `feedback_gmail_mcp_limitations`) |
| **Canva MCP** (`mcp__claude_ai_Canva__*`) | **PENDIENTE** (suscripción Owner + auth MCP) | Producción de presentaciones visuales — scope inicial **limitado a Vivienne** | python-pptx + matplotlib (path CORE, mantenido y funcional) | python-pptx + matplotlib siguen siendo el path default. Canva es upgrade opcional. | Decisión 2026-05-18: caso base = próxima entrega Cora proyecto Gama Notoriedad 2026. Pilot Vivienne antes de ampliar |
| **Google Calendar MCP** | Activo (permisos visibles) | Lectura de eventos para contextualizar tareas | Owner copia/pega contexto del calendario manualmente | Owner provee contexto en el brief | No es crítico para producción de entregables |

### Storage y backup

| Tool | Estado | Scope de uso | Sustituible por | Fallback CORE | Notas |
|---|---|---|---|---|---|
| **Google Drive personal** del Owner | Activo | Nube canónica del sistema — `01-inbox/`, `colaboradores/`, RAUL-Exchange | Cualquier object storage con sync local (Dropbox, OneDrive como primario, S3 + rclone, Nextcloud) | El repo es autocontenido en disco local; Drive solo provee canal de intercambio con humanos externos y mobile access | Decisión arquitectónica 2026-04-25 — ver DECISIONS.md y norte arquitectónico §0 |
| **OneDrive personal** del Owner | Activo (solo backup) | Backup automático de KB y memoria Claude Code | Cualquier backup target (Google Drive secundario, S3, NAS local, Backblaze) | Backup es defensa-en-profundidad; recovery primario es git para el repo y manual para memoria | Tareas Windows: `RAUL_KB_Backup_OneDrive` (23:00 diaria) y `RAUL_Memory_Backup_OneDrive` (23:05 diaria) |

### Cloud Routines (Anthropic)

| Tool | Estado | Scope de uso | Sustituible por | Fallback CORE | Notas |
|---|---|---|---|---|---|
| **Anthropic Routines** (Cloud) | Activo | Ejecución periódica de bridges (InboxBot, OwnerBridge, CoraBridge efímero) | Cron local + script + API call; GitHub Actions schedule; cualquier scheduler con acceso a Claude API | Owner ejecuta los bridges manualmente al inicio de sesión desktop | Limitación documentada: no soporta MCPs custom (memoria `reference_anthropic_routines_no_custom_mcp`) |

### Suscripciones complementarias (Owner-side, no en runtime directo)

| Tool | Estado | Scope de uso | Sustituible por | Fallback CORE | Notas |
|---|---|---|---|---|---|
| **Google AI Pro** | Activo (Owner-side) | Acceso a Gemini para tareas paralelas / sandbox / second opinion del Owner | Cualquier LLM web (ChatGPT Plus, Claude.ai web, Perplexity) | No aplica — no es runtime del sistema | No invocado por agentes del repo, uso humano del Owner |
| **Canva Pro** (suscripción anual ~$120/año) | **PENDIENTE** suscripción | Habilita el MCP Canva en claude.ai | Cualquier herramienta de diseño con MCP o API (Figma, Adobe Express, Beautiful.ai); o seguir con python-pptx CORE | python-pptx + matplotlib (path actual default) | Decisión 2026-05-18 — pilot Vivienne, ampliación a Atlas/Luma/Orfeo/Oz pending |

---

## Ampliación pendiente del scope Canva (NO ejecutar ahora)

Los siguientes agentes son **candidatos** a usar Canva como output engine secundario o primario una vez validado el pilot con Vivienne. **No están autorizados todavía** — esperar review post-pilot Vivienne con Cora antes de ampliar:

| Agente | Caso de uso potencial | Path CORE actual mantenido |
|---|---|---|
| **Atlas** | Mockups de empaque y arte de etiquetas | python-pptx + svg2rlg + PyMuPDF |
| **Luma** | Visuales para contenido social (Genteca, marca personal) | python-pptx + matplotlib + Pillow |
| **Orfeo** | Branding/identidad y visual concepts | python-pptx + Pillow |
| **Oz (light)** | Borrador rápido de etiquetas antes de pasar a Oz real | python-pptx + PyMuPDF |

**Trigger de ampliación:** review formal post-pilot Vivienne (post-entrega Cora V7+ proyecto Gama) — si los outputs Canva superan en calidad/velocidad al path python-pptx con criterios verificables, se autoriza extensión caso por caso.

---

## Para clonadores del repo

Esta lista es **informativa, no obligatoria**. Cada entrada incluye:
- **Estado** — si está activo en la instancia del Owner actual o pendiente
- **Sustituible por** — alternativas (open-source, commercial, manual) que cumplen función equivalente
- **Fallback CORE** — qué pasa si decides no adoptar la elección del Owner (típicamente: scripts python ya existentes en el repo, o acción manual)

**El sistema /RAUL/ corre sin ninguna de las tools de este archivo** si usas solo lo listado en `TOOLS-REQUIREMENTS.md` + un runtime LLM cualquiera + voluntad de ejecutar manualmente lo que las MCPs automatizan. Las tools Owner-selected son optimizaciones que el Owner actual eligió por costo/beneficio en su contexto.

---

## Cómo actualizar este archivo

Cuando el Owner adopte una nueva tool comercial o suscripción que un agente vaya a invocar:

1. Agregar fila en la tabla correspondiente (Runtime / MCPs / Storage / Cloud Routines / Suscripciones)
2. Llenar las 5 columnas: Estado, Scope, Sustituible por, Fallback CORE, Notas
3. Bump de versión y fecha en el header
4. Si la decisión es estructural (afecta varios agentes, política de fallback, etc.), abrir entrada en `DECISIONS.md`
5. Si afecta a un agente específico, actualizar también su SSOT conceptual y su AGENT.md runtime — pero **manteniendo el path CORE** en su pipeline

---

*Documento seed v0.1 producido el 2026-05-18 como parte de la decisión Owner sobre adopción Canva Pro + formalización de la política de split CORE vs Owner-selected. Va a crecer conforme el Owner adopte más tools y conforme se completen pilots.*
