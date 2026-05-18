---
slug: raul-subagent-no-nested-delegation
last_touched: 2026-05-17
created: 2026-05-17
contexto: Patrón Raul-subagent híbrido (commit `6ec26a8` 2026-05-17)
caso_base: Primera invocación real Raul-subagent vía OwnerBridge para ola Notoriedad V2.0 Gama
tags: [architecture, subagent, delegation, claude-code-harness, tier-system, raul-runtime, blocker]
severity: alto — bloquea uso real del patrón Raul-subagent para trabajo que requiere specialists
status: descubierto — pendiente decisión Owner sobre patrón remediación
---

# Raul-subagent NO puede delegar a sub-subagents (claude-code harness limit)

## Hallazgo

Cuando Raul es invocado como **subagent explícito** (`Agent(subagent_type='raul', ...)`) en Claude Code, el tool catalog expuesto al subagent **NO incluye `Agent` ni `Task`**. Las únicas herramientas disponibles son:

```
Read, Write, Edit, Grep, Glob, Bash, WebFetch, WebSearch
```

Esto contradice la asumpción del commit `6ec26a8` (2026-05-17, "feat(agents): Raul Opus 4.7 + Tier-based execution + invocación híbrida"):

- Mi propio AGENT.md declara `tools: [..., Agent, ...]` en frontmatter.
- El conceptual §8 documenta "Raul → cualquier especialista: vía mecanismo de delegación del runtime activo."
- El runtime adapter `raul/AGENT.md` documenta `Agent` como la tool para delegación.

Pero **el harness de Claude Code no respeta esa declaración cuando Raul mismo es invocado como subagent**. La declaración `tools:` en frontmatter parece interpretarse como techo permisivo solo cuando el agent es invocado como leaf-node desde main Claude, no cuando es ya un subagent.

## Implicación operativa

**Raul-subagent NO puede orquestar specialists.** Solo puede:
- Leer/buscar (Tier 1).
- Escribir en territorio propio: task-log, intelligence/, cola de tickets, índices propios (Tier 2).
- Ejecutar Bash limitado (lectura git, scripts utilitarios).

NO puede invocar a Methos, Cuanti, Sinta, Vivienne, Bruna, Vera, Orlan, etc.

Esto **anula el valor del patrón Raul-subagent híbrido** para cualquier trabajo no trivial que requiera la cadena de especialistas — que es la mayor parte del trabajo real.

## Caso base — Notoriedad V2.0 Gama, 2026-05-17

Owner invocó Raul-subagent vía OwnerBridge para arrancar ola Notoriedad V2.0 Gama. Tras triage Tier 1:
- BBDD V2.0 = idéntica a V1 (no nueva ola de campo).
- Material nuevo: BBDD 2025 raw (n=785, 444 cols) + 10 docs cualitativos Gama.
- Cadena diseñada: Methos ME-5 → Cuanti CU-7 wave-over-wave → Sinta IN-7+IN-8 → Vivienne (VI-1/VI-2 separados) → Bruna gate → drop.

Al intentar delegar a Methos, descubrí que **Agent tool no está expuesto**. Las opciones reales fueron:
- (A) Ejecutar yo todo el trabajo de specialists — violación grave cardinal rule §3 ("Raul no ejecuta").
- (B) Preparar terreno Tier 1-2 + escribir briefs estructurados para que la próxima invocación los use.
- (C) Reportar al Owner y esperar instrucciones.

Tomé (B) + reporte explícito al regresar el Owner. Esto preserva la cardinal rule pero **demuestra que el patrón Raul-subagent híbrido tal como está codificado en `6ec26a8` no funciona para trabajo real con specialists**.

## Patrones de remediación a considerar (decisión Owner)

### Opción 1 — Raul como skill puro encarnado en main Claude (rollback parcial)

Revertir el frontmatter `name: raul + model: claude-opus-4-7 + tools: [...]` y volver a main-Claude-as-Raul-skill. Main Claude tiene acceso completo a Agent/Task tool y puede orquestar specialists. Costo: pierde la garantía Opus 4.7 (main Claude puede ser el modelo default de la sesión). Beneficio: arquitectura funcional.

### Opción 2 — Raul-subagent solo para triage + delegación implícita via texto al main

Raul-subagent hace Tier 1-2 (triage, briefs, organización) y devuelve al main "ejecuta estas N invocaciones de specialists con estos briefs". Main Claude las ejecuta. Costo: 2 hops por sesión (main → Raul-subagent → return → main → specialists). Beneficio: preserva Opus 4.7 para el triage estratégico de Raul.

### Opción 3 — Aceptar el límite y rediseñar territorio Raul-subagent

Reconocer que Raul-subagent es solo para tareas donde NO se requiere delegación a specialists: meta-decisiones del sistema, audits del repo, planning estratégico de fases, governance docs, captura de aprendizajes, ediciones a SSOTs. Cuando hay trabajo de specialists, main Claude lo orquesta directo sin pasar por Raul-subagent. Costo: el patrón híbrido pierde gran parte de su scope original. Beneficio: clarifica el split de responsabilidades.

### Opción 4 — Hack: Raul-subagent escribe a un trigger file que dispare invocaciones desde main

Raul-subagent escribe un archivo JSON con las delegaciones planeadas; main Claude lo lee al retomar y ejecuta. Costo: feo, asíncrono, no es lo que diseñamos. Beneficio: ninguno claro.

## Anti-patrón confirmado

**No usar opción A (Raul-subagent ejecuta trabajo de specialists directo) bajo la racionalización "es Tier 3 con las 4 condiciones".** Las 4 condiciones explícitamente requieren "subagent failure precedente" — no aplica si el subagent ni siquiera puede ser invocado. Invocar Tier 3 masivamente porque "no tengo Agent tool" sería rationalization, no rationale. La cardinal rule prevalece sobre la conveniencia de output.

## Referencias

- Commit `6ec26a8` (2026-05-17): "feat(agents): Raul Opus 4.7 + Tier-based execution + invocación híbrida"
- Conceptual `04-system/02-agents/conceptual/raul.md` §6.7 (Tier-based execution policy) + §8 (Interactions with Other Agents)
- Runtime `.claude/agents/raul/AGENT.md` (declara Agent tool en frontmatter)
- task-log entry 2026-05-17 (Raul subagent híbrido descubrimiento bloqueo)
- Session handoff `project_session_handoff_2026-05-18.md` en memoria HOT

## Acción recomendada al Owner

Antes de la próxima invocación que requiera specialists:
1. Decidir cuál de las 4 opciones de remediación (o combinación).
2. Si Opción 1 o 3: editar SSOT `raul.md` + runtime `raul/AGENT.md` para reflejar el patrón nuevo. Commit.
3. Si Opción 2: mantener Raul-subagent como triage layer; codificar en conceptual la convención "Raul-subagent devuelve plan de delegación al main que ejecuta".
4. Reabrir la ola Notoriedad V2.0 con el patrón corregido. Los briefs preparatorios ya están listos para reutilizar.
