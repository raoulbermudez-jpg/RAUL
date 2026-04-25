# LLM-GUIDELINES.md
## Cómo usar modelos de lenguaje en el sistema /RAUL/

**Versión:** 1.0
**Última actualización:** 2026-04-25

Este documento define las reglas operativas para el uso de LLMs dentro del sistema /RAUL/. Se aplica a Claude Code, Claude.ai, Perplexity, ChatGPT y cualquier otro modelo que opere sobre los archivos o el contexto del sistema.

---

## 1. Principio de vendor-neutralidad

El conocimiento del sistema vive en Markdown plain-text. Ningún agente, documento o flujo de trabajo puede crear dependencia a un formato o herramienta propietaria como verdad principal.

- **Correcto:** artículos wiki en `.md`, specs en `.md`, agentes definidos en `.md`.
- **Incorrecto:** exportar conocimiento clave a formatos solo legibles con Notion, Obsidian, o un SaaS específico.

Cualquier LLM (Claude, GPT, Gemini, Perplexity, etc.) debe poder operar sobre el sistema sin instalación especial.

---

## 2. Estrategia de carga de contexto

Cargar solo lo necesario para la tarea. No saturar el contexto con archivos masivos cuando se puede usar índices y referencias puntuales.

| Tipo de tarea | Carga mínima recomendada |
|---|---|
| Tarea general / multi-dominio | `CLAUDE.md` + `CONTEXT_core.md` (auto-cargados) |
| Tarea Genteca | Core + `_index.md` Genteca + specs puntuales |
| Tarea Plenus | Core + `_index.md` Plenus |
| Tarea de sistema / governance | Core + archivo de governance específico |
| Investigación nueva | Core + `research-index.md` + artículo wiki relevante |

**Regla:** consultar el índice del dominio (`_index.md`) antes de abrir archivos masivos. Los índices están diseñados para orientar sin consumir contexto.

---

## 3. Compilar antes que saturar

Cuando una tarea requiere leer muchos documentos, el agente responsable (Celeste, Paxs, o el especialista) debe **destilar el conocimiento en un artículo wiki** dentro de `02-knowledge-base/` en lugar de arrastrar decenas de archivos al contexto en cada sesión.

- **Correcto:** Paxs lee 15 PDFs → redacta `wiki/01-fundamentos-tecnicos.md` → las sesiones futuras cargan ese artículo.
- **Incorrecto:** cada sesión carga los 15 PDFs directamente.

---

## 4. Modelos recomendados por tipo de tarea

| Tarea | Modelo recomendado | Razón |
|---|---|---|
| Orquestación, routing, planificación | Claude Opus (via Claude Code) | Mejor razonamiento multi-paso |
| Redacción, scripts, copy | Claude Sonnet | Mejor balance velocidad/calidad para producción |
| Investigación web en tiempo real | Perplexity | Acceso a fuentes actualizadas |
| Tareas rápidas / clasificación | Claude Haiku | Económico para tareas simples |
| Decks y presentaciones complejas | Claude Opus (Vivienne) | Razonamiento estructural + python-pptx |

Estos son valores por defecto. El Owner puede ajustar por sesión según necesidad.

---

## 5. Salidas y persistencia

- Toda salida valiosa de un LLM que deba persistir va a `02-knowledge-base/` (wiki o specs) o a `03-projects/<dominio>/<proyecto>/`.
- Los chats y sesiones son efímeros. Si una conversación produce conocimiento o una decisión relevante, se extrae y se escribe en el archivo correspondiente antes de cerrar.
- Los archivos `PERPLEXITY.md` del sistema son companion docs de sesión — útiles como borrador, no como fuente autoritativa. Ver `CONTEXT_core.md` para detalles.

---

## 6. Seguridad y datos sensibles

- No pegar credenciales, contraseñas, tokens de API ni datos personales identificables en prompts o archivos del repo.
- Si una tarea requiere datos sensibles, procesarlos localmente sin subir al repo ni a servicios de chat.
- Ver `SECURITY-AND-ACCESS.md` para política completa.

---

## 7. Calidad de outputs

- Los outputs de LLMs son **borradores**, no verdades. Siempre requieren revisión del Owner o del agente especialista antes de entrar a la KB.
- Al archivar un artículo wiki generado por LLM, indicar la fuente: `_Generado con [modelo], revisado por [Owner/agente], [fecha]._`
- Las specs técnicas (datasheets, manuales) NO se generan con LLMs — se procesan desde documentos fuente reales vía Celeste.

---

## Notas de versión

- **v1.0 — 2026-04-25** — documento inicial.
