# Conceptual Template — Canonical Agent Pattern

**Aplica a:** todo archivo `04-system/02-agents/conceptual/<agente>.md`.

> Este template es la plantilla canónica para los archivos conceptuales de
> agentes en el sistema /RAUL/. Toda nueva contratación (vía Michelina) y
> toda migración de un conceptual existente debe respetar esta estructura
> de 10 secciones obligatorias.

---

## Reglas duras

**Permitido en un conceptual:**

- Identidad, personalidad, misión, alcance, comportamiento operativo del
  agente.
- Rutas relativas-al-repo (`04-system/01-config/CLAUDE_core.md`).
- Capabilities descritas en abstracto ("delegar a un especialista", "buscar
  en web").
- Formatos de output portables (Markdown, JSON, texto estructurado).
- Referencias a otros conceptuales por nombre.

**Prohibido en un conceptual:**

- Frontmatter de runtime (`name:`, `model:`, `tools:`).
- Rutas OS-específicas (`C:\RAUL\...`, `G:\Mi unidad\...`).
- Tool names de un vendor concreto (`Agent tool`, `Gmail MCP`, `WebFetch`,
  `python-pptx`).
- Modelos LLM hardcoded (`claude-sonnet-4-6`, `gemini-pro`).
- Productos comerciales por nombre como dependencia obligatoria
  (`Perplexity Comet`, `Notion`).
- Referencias a archivos runtime (`.claude/agents/...`).

---

## Estructura obligatoria

Toda sección numerada del 1 al 10 es obligatoria. La sección 11 es opcional
y se usa solo cuando el agente tiene protocolos especiales o templates
reusables que no encajan en §6.

```markdown
# <Name> — <Role Title> (conceptual SSOT)

> Vendor-neutral SSOT. Runtime adapters viven en directorios LLM-específicos
> (`.claude/agents/`, futuros `.gemini/agents/`, etc.). Ver
> `04-system/01-config/LLM-GUIDELINES.md` y
> `04-system/02-agents/_runtime-adapter-guide.md` para el contrato de
> derivación.

## 1. Identity & Personality

[Quién es. Tono. Qué le importa. 2-4 párrafos. Esta sección preserva la
"experiencia equipo humano" — debe leerse como una persona, no como una
taxonomía de capabilities.]

## 2. Mission & Scope

[Qué hace. A quién sirve. Qué dominios cubre — global o anclado a uno.
Distinción clara si es transversal vs domain-specific. Capa o clase del
agente al final.]

## 3. Boundaries — What This Agent Does NOT Do

[Tabla o lista explícita de qué NO hace y quién cubre cada gap. Crítica
para evitar pisadas con otros agentes.]

| Acción | Quién la cubre |
|---|---|
| ... | ... |

## 4. Inputs Expected

[Qué necesita recibir para arrancar. Brief mínimo. Qué se pregunta cuando
falta información.]

## 5. Outputs Produced

[Qué entrega — descrito en términos de capability portable, no de tooling.
Ej: "estructura de slides en formato portable" en lugar de ".pptx via
python-pptx".]

## 6. Operating Protocol

[Pasos numerados de cómo opera. Cargas de contexto descritas con rutas
relativas-al-repo (`04-system/01-config/CLAUDE_core.md`), nunca con paths
OS-específicos. Si el agente tiene sub-protocolos especiales (ej.
escalación), van como §6.1, §6.2, etc.]

## 7. Output Format

[Estructura del entregable como markdown/JSON portable. Si hay formatos
secundarios opcionales (binarios), marcarlos como "derivado
runtime-dependiente".]

## 8. Interactions with Other Agents

[Quién le pasa trabajo, a quién se lo pasa, qué gates obligatorios existen.
Referencias a `ROUTING-GUIDE.md` cuando aplique.]

## 9. Quality Criteria

[Qué define "trabajo bien hecho" para este rol. Revisable por un humano
sin abrir el deliverable completo.]

## 10. Antipatterns

[Errores frecuentes a evitar. Tan importante como los principios.]

## 11. (Opcional) Special Protocols / Templates

[Solo si aplica: protocolos no-triviales reutilizables — como el blocked-
site protocol de Paxs, el canonical conceptual template de Michelina, o
templates de output como RESULTADO_RAUL.]

---

*<Class según `_taxonomy.md` vigente>. <Singleton si aplica>. <Domain o "transversal">.*
```

---

## Notas de uso

- El banner SSOT del inicio es **obligatorio textualmente** — no
  parafrasear.
- Las 10 secciones obligatorias deben aparecer en orden y con sus
  encabezados exactos.
- Si una sección no tiene contenido aplicable, escribir explícitamente
  "No aplica" con justificación breve, en lugar de omitir la sección.
- El footer final (clase + singleton + domain) usa la taxonomía vigente en
  `04-system/02-agents/_taxonomy.md`.

---

*Template canónico. Cambios mayores a este patrón requieren entrada en
`04-system/03-governance/DECISIONS.md` y migración subsiguiente de todos los
conceptuales existentes.*
