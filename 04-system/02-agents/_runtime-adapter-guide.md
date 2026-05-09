# Runtime Adapter Guide — Contrato de derivación por LLM

**Aplica a:** todo archivo runtime de un agente — actualmente
`.claude/agents/<agente>/AGENT.md`, futuros equivalentes para Gemini,
Perplexity u otros.

> El conceptual SSOT (`04-system/02-agents/conceptual/<agente>.md`) define
> qué hace y cómo opera un agente. Este documento define cómo se construye
> el archivo runtime que lo ejecuta en una plataforma concreta.

---

## §1 — Contrato universal (aplica a cualquier LLM)

### 1.1 — Estructura mínima de un runtime

Todo archivo runtime contiene tres bloques en este orden:

1. **Frontmatter** específico de la plataforma (campos según el LLM).
2. **Carga del SSOT** vendor-neutral con el path absoluto del conceptual.
3. **Implementation notes** con path mappings, tool mappings y notas de
   ejecución propias de la plataforma.

### 1.2 — Qué SÍ va en el runtime

- Frontmatter de la plataforma (nombre, modelo, tools, descripción).
- Path mappings: rutas absolutas del SO específico (`C:\RAUL\...`).
- Tool mappings: nombres de tools concretos del runtime (`Read`, `WebSearch`,
  `Agent`, etc.).
- Procedimientos específicos del runtime (ej: cómo escribir un nuevo agent
  file en este runtime).
- Notas de invocación (ej: subagente vs skill, frecuencia de trigger).

### 1.3 — Qué NO va en el runtime

- Comportamiento operativo del agente (vive en conceptual §6).
- Identidad, personalidad, misión (vive en conceptual §1-2).
- Output formats (vive en conceptual §7).
- Quality criteria, antipatterns (vive en conceptual §9-10).
- Cualquier sección de las 10 canónicas del conceptual.

### 1.4 — Regla de oro

Si un archivo runtime crece más de ~50 líneas, hay contenido que pertenece
al conceptual. Cuando esto pase, migrar el contenido al conceptual y
adelgazar el runtime.

### 1.5 — Plantilla universal de runtime

```markdown
[FRONTMATTER ESPECÍFICO DE LA PLATAFORMA — ver §2/§3/§4 según LLM activo]

# <Agente> — Runtime adapter for <plataforma>

Carga la SSOT vendor-neutral antes de operar:
`<path absoluto al conceptual>`

## Implementation notes for <plataforma>

### Path mappings
[mapeos relativos-al-repo → absolutos OS-específicos relevantes para este
agente]

### Tool mappings
[capability del conceptual → tool concreto del runtime]

### Runtime-specific notes
[invocación, procedimientos especiales del runtime, cualquier nota propia]
```

---

## §2 — Claude Code (Anthropic Claude vía Claude Code)

### 2.1 — Path del runtime

`.claude/agents/<firstname-lowercase>/AGENT.md` (relativo a la raíz del repo).

### 2.2 — Frontmatter requerido

```yaml
---
name: <firstname-lowercase>
description: <una línea de cuándo invocar — clave para routing automático>
model: <model id según LLM-GUIDELINES.md §4>
tools:
  - <solo las tools estrictamente necesarias>
---
```

**Excepción** — agentes invocables como skill (no como subagente): no llevan
frontmatter. Ejemplo actual: `raul`.

### 2.3 — Tools disponibles en Claude Code (mapping desde capabilities conceptuales)

| Capability conceptual | Tool Claude Code |
|---|---|
| Lectura de archivos del repo | `Read` |
| Escritura/creación de archivos | `Write` |
| Edición incremental | `Edit` |
| Búsqueda de patrones en archivos | `Grep` |
| Búsqueda de archivos por nombre/path | `Glob` |
| Web search | `WebSearch` |
| Web fetch (HTML/PDF directo) | `WebFetch` |
| Ejecución de comandos shell | `Bash` |
| Ejecución de comandos PowerShell | `PowerShell` |
| Delegación a otro agente | `Agent` |

Asignar **solo** las tools necesarias. Sobre-equipar es antipattern.

### 2.4 — Convención de paths absolutos (Windows actual)

- Conceptual SSOT: `C:\RAUL\04-system\02-agents\conceptual\<agente>.md`
- Roster: `C:\RAUL\04-system\02-agents\_roster.md`
- LLM Guidelines: `C:\RAUL\04-system\01-config\LLM-GUIDELINES.md`
- (otros según el agente)

### 2.5 — Notas operativas Claude Code

- Subagentes se invocan vía `Agent` tool con `subagent_type: <name>`.
- El campo `description` del frontmatter es lo que Claude Code usa para
  routing automático — debe ser específico y accionable.
- Para asignar `model:`, consultar `LLM-GUIDELINES.md` §4.

---

## §3 — Gemini (RESERVADO)

Sección reservada. Se llenará cuando exista operación real con Gemini sobre
este repo. Mientras tanto: no crear `.gemini/agents/` ni archivos runtime
para Gemini.

Cuando se materialice, esta sección debe contener:
- Path del runtime (probable: `.gemini/agents/<agente>/AGENT.md`).
- Frontmatter requerido (formato Gemini).
- Tool mapping desde capabilities conceptuales.
- Convención de paths absolutos.
- Notas operativas.

---

## §4 — Perplexity (RESERVADO)

Sección reservada. Se llenará cuando exista operación real con Perplexity
sobre este repo. Mismas consideraciones que §3.

---

## §5 — Procedimiento para añadir un runtime nuevo

Cuando se decida soportar un LLM adicional:

1. Validar que existe operación real planeada (no scaffolding prematuro).
2. Registrar la decisión en `04-system/03-governance/DECISIONS.md`.
3. Llenar la sección correspondiente (§3, §4, o nueva §5/§6) de este guide.
4. Crear el directorio runtime en raíz del repo (ej. `.gemini/agents/`).
5. Comenzar a derivar runtimes desde conceptuales existentes,
   priorizando los agentes más invocados.
6. **NUNCA** modificar conceptuales para acomodar un runtime nuevo. Si un
   conceptual no es derivable, el problema está en el conceptual y se
   migra al patrón canónico, no al revés.

---

*Contrato de derivación. Cambios mayores requieren entrada en
`DECISIONS.md`.*
