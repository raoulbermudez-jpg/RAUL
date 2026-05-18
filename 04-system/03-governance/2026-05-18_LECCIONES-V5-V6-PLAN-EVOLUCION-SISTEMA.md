---
documento: Lecciones V5+V6 y Plan de Evolución del Sistema /RAUL/
fecha: 2026-05-18
autor: Main Claude (Opus 4.7) — captura de aprendizajes post sesión nocturna V5+V6
status: PROPUESTA — para revisión Owner y ejecución en sesión próxima
proyecto_base: gama-notoriedad-2026 (consultoria-externa) — caso de prueba real
alcance: arquitectura del repo, configuración de agentes, modelos LLM dinámicos, trabajo remoto, agentes subutilizados, gaps de hiring, decisiones pendientes
---

# Lecciones V5+V6 y Plan de Evolución del Sistema /RAUL/

> **Cómo leer este documento:** capítulos 1-3 son diagnóstico (qué tenemos y cómo se está usando), 4-8 son propuestas (qué cambiar), 9-12 son ejecución (qué hacer concretamente en próxima sesión). Si tenés 10 minutos: leer §1 y §10.

---

## 1. Resumen ejecutivo

Durante las sesiones nocturnas del 2026-05-17 y 2026-05-18 produjimos 5 versiones consecutivas (V3 → V4 → V5 → V6 + Word V6) del estudio Notoriedad Gama 2026 para Cora. Este ciclo intensivo reveló patrones operativos del sistema /RAUL/ que merecen consolidación como políticas y plan de evolución.

**Los 6 hallazgos centrales:**

1. **Main Claude está absorbiendo trabajo de specialists** que no existen (escribió ~5000 líneas python entre V5 deck, V6 charts y V6 Word). Esto es síntoma de un gap: no hay un specialist "DocBuilder" para reportes formales `.docx`/`.md` largos. Cuando Vivienne falla (token explosion en decks grandes con charts), main Claude cubre — pero eso no escala.

2. **Vivienne tiene un patrón de falla predecible** ya documentado (memoria `feedback_vivienne_token_explosion_pattern_v1`): explota >32K tokens output en decks con muchos charts python-pptx + matplotlib en una sola invocación. Workaround: separar en 3 invocaciones (charts / deck / RE). Sigue sin codificarse en su SSOT.

3. **El patrón `Word-first → PPTX-after`** que el Owner introdujo en V6 es estructuralmente mejor que el patrón anterior. Razones: editable, evita token explosion, sirve como guía para Vivienne, queda como archivo de consulta. **Recomendación: política default para consultorías externas.**

4. **Raul-subagent híbrido tiene un bug arquitectónico no resuelto:** el harness de Claude Code NO expone el tool `Agent` a un subagent invocado vía `Agent(subagent_type='raul')`. Documentado el 2026-05-17 (memoria `feedback_raul_subagent_no_nested_delegation`). Decisión Owner pendiente: 4 opciones de remediación, ninguna implementada. **De facto aplicamos Opción 2 (main Claude orquesta) sin formalizarla en SSOT.**

5. **Distribución actual de modelos LLM es estática y sub-óptima.** 4 agentes en Opus 4.7 (raul, bruna, michelina, paxs), 20 en Sonnet 4.6 default. Specialists complejos como Cuanti (análisis estadístico denso) y Sinta (análisis temático) corren en Sonnet pero tendrían mejor calidad en Opus para tareas largas. Inversamente, tareas mecánicas (Sira indexación, Ivo logging) podrían correr en Haiku con ahorro de tokens. **No hay framework de selección dinámica.**

6. **Specialists subutilizados** (de los 25 production): nunca se invocaron en sesiones recientes Atlas, Aurelio, Celeste, Ivo, Luma, Nerea, Orfeo, Orlan, Oz, Renzo, Sira, Solenne, Vael, Vela, Vera. Esto puede ser correcto (proyectos no requieren su scope) o síntoma de que el sistema no los está activando cuando deberían intervenir. **Análisis pendiente.**

**Conclusión:** el sistema funciona, pero opera muy por debajo de su capacidad de diseño. Main Claude está sobrecargado, Vivienne tiene fallas predecibles no corregidas, y la asignación de modelos LLM es estática cuando debería ser dinámica por complejidad de tarea.

---

## 2. Inventario de agentes y modelos LLM (estado al 2026-05-18)

### 2.1 Modelos asignados — distribución actual

| Modelo | Cantidad | Agentes |
|---|---|---|
| **claude-opus-4-7** (Opus 4.7) | 4 | raul, bruna, michelina, paxs |
| **claude-sonnet-4-6** (Sonnet 4.6) | 20 | atlas, aurelio, celeste, cuanti, ivo, luma, methos, nerea, orfeo, orlan, oz, renzo, sinta, sira, solenne, vael, vela, vera, vivienne |
| **(default / inherit)** | 2 + bridges cloud | corabridge-gama-test, inboxbot + ownerbridge (corre cloud) |

### 2.2 Taxonomía vs uso real

| Clase taxonómica | Total agentes | Usados en V5+V6 | Subutilizados |
|---|---|---|---|
| Orchestration | 1 (raul) | 0 directo (Opción 2 de facto) | raul como subagent invocable |
| Governance | 2 (bruna, celeste) | bruna 0 (reuso V4) | celeste 0 |
| Global-service | 2 (vivienne, michelina) | vivienne 2 (1 fallo) | michelina 0 |
| Domain-specialist | 8 (vera, orlan, vael, solenne, aurelio, nerea, oz, renzo) | 0 | TODOS — proyecto consultoria-externa no usa specialists Genteca |
| Content-supply-chain | 6 (atlas, luma, orfeo, vela, ivo, sira) | 0 | TODOS |
| Execution-utility | 3 (methos, cuanti, sinta) | cuanti 2, sinta 0 (reuso V4), methos 0 (reuso V4) | sinta y methos reutilizados |
| Remote bridges | 3 (ownerbridge, inboxbot, corabridge) | ownerbridge 1 (input V5) | inboxbot y corabridge no se usaron |
| Built-in | 1 (Explore) | 1 vez (búsqueda histórica) | Eficiente cuando se usa, subutilizado en general |

**Lectura:** el proyecto `consultoria-externa/gama-notoriedad-2026` solo activa el cluster Execution-utility (Cuanti, Sinta, Methos) + Vivienne (global) + Bruna (gate). Los 17 specialists Genteca/CSC quedan dormidos. **Esto es correcto** — son specialists de otro dominio. Pero significa que el ROI de la migración Modelo A (21 agentes canónicos) no se materializa hasta que haya carga en los otros dominios.

### 2.3 Frontmatter declarado vs comportamiento real

| Agente | Modelo declarado | Tools declaradas | Comportamiento observado |
|---|---|---|---|
| raul | opus-4-7 | Read/Write/Edit/Grep/Glob/Bash/**Agent**/WebFetch/WebSearch | **`Agent` declarado pero el harness NO lo expone cuando es subagent invocado** — bug arquitectónico documentado |
| vivienne | sonnet-4-6 | Read/Write/Edit/Grep/Glob/Bash | Token explosion >32K en decks grandes con charts — workaround no codificado en SSOT |
| cuanti | sonnet-4-6 | Read/Write/Bash/Grep | Funciona bien, pero análisis muy densos (CU-8 con 12 preguntas + 5 cruces nuevos) bordean tiempo límite |
| bridges (corabridge/inboxbot/ownerbridge) | sin modelo | varía | Corren en cloud (Anthropic Routines) — no usan modelo local |

---

## 3. Patrones de uso reales — V3 a V6 (5 versiones consecutivas en 36 horas)

### 3.1 Quién hizo qué — vista consolidada

| Versión | Generador principal | Especialistas invocados | Patrón |
|---|---|---|---|
| V3 (2026-05-17 AM) | Vivienne (deck completo) | Methos, Cuanti, Sinta, Bruna (cadena completa) | Cadena canónica funcionando |
| V4 (2026-05-17 PM) | Vivienne (deck + RE) | Cuanti CU-7, Sinta IN-7/IN-8 (extensiones de V3) | Extension layer sobre V3 |
| V5 (2026-05-18 fresh) | **OwnerBridge** + Main Claude (fallback deck) + Vivienne (RE) | Vivienne (deck fallo, RE OK) | OwnerBridge → main Claude (Vivienne timeout en deck) |
| V6 Word (2026-05-18 noche) | **Main Claude (directo)** | Cuanti CU-8 v1+v2, Explore (búsqueda) | Word-first, no Vivienne |
| V6 PPTX (pendiente) | (pendiente Vivienne) | Vivienne | Después de aprobación Owner |

### 3.2 Anti-patrones detectados

1. **Main Claude como ejecutor cuando Vivienne falla** — V5 deck: yo escribí 1000 líneas python-pptx en 25 min. Funciona pero no es escalable.

2. **Reinvención de wheels** — generé `extract_guia.py` y `extract_cuali.py` en V6 sin verificar si scripts equivalentes existían (afortunadamente no).

3. **OwnerBridge desktop-less limitation** — generó el .md V5 pero NO pudo producir .pptx (sin desktop). El Owner tuvo que esperar a sesión local para render. Sería más eficiente si OwnerBridge entregara directamente al pipeline desktop de Raul.

4. **Tareas sin TaskCreate hasta que el system reminder lo pide** — varios bloques de trabajo se hicieron sin tracking explícito (tracking se agregó retroactivamente).

### 3.3 Patrones que SÍ funcionan

1. **SendMessage para continuar agente con full context** — CU-8 v2 reusó la session de CU-8 v1. Ahorro estimado: 5-10 min vs invocar Cuanti fresh.

2. **Explore para búsquedas multi-ubicación** — entregó síntesis estructurada de 5 patrones de feedback Owner en <2 min. Subutilizado en general.

3. **Reuso de gates entre versiones** — Bruna BR-2 V4 se reusó en V5 y V6 sin reinvocación porque los datos no cambiaron. Política emergente correcta.

4. **Memoria HOT con `last_touched` y `always_load: true`** — funcionó bien para mantener handoffs vigentes accesibles. Sistema 2 tiers (MEMORY.md / MEMORY_ARCHIVE.md) probó valor.

---

## 4. Lecciones V5+V6 validadas — políticas a adoptar formalmente

### 4.1 Word-first → PPTX-after (NUEVA POLÍTICA)

**Para qué:** consultorías externas que requieren reporte formal de consulta + presentación.

**Por qué funciona:**
- Word es editable colaborativamente (Owner + cliente revisan en mismo formato)
- Evita el patrón de falla de Vivienne (token explosion en decks con charts)
- Sirve como guía estructurada para Vivienne después (PPTX se hace SOBRE el Word aprobado)
- Queda como archivo de consulta de largo plazo

**Workflow propuesto:**
```
1. Cuanti/Sinta/Methos producen análisis técnicos
2. Main Claude genera Word formal con todo (charts inline + tablas + notas metodológicas)
3. PAUSA — Owner + cliente revisan Word
4. Vivienne renderea PPTX usando Word aprobado como guía (3 invocaciones separadas)
5. Drop final + email
```

**A codificar en:** `04-system/01-config/LLM-GUIDELINES.md` o nuevo `04-system/03-governance/WORKFLOW-CONSULTING-EXTERNAL.md`.

### 4.2 Reuso de gates entre versiones (NUEVA POLÍTICA)

**Regla:** si los datos no cambian entre versiones (mismo n, misma BBDD, mismos cálculos), el gate de Bruna anterior **se reusa** sin reinvocación. Solo se reinvoca Bruna cuando:
- Llegan datos nuevos
- Se introducen claims nuevos
- Cambia el wording de claims existentes (no solo presentación)

**Ya aplicado en V5 y V6** (BR-2 V4 vigente). **A codificar en SSOT de Bruna.**

### 4.3 SendMessage continuation pattern (NUEVA POLÍTICA)

**Regla:** cuando una extensión de análisis se pide al mismo specialist que produjo el análisis base (CU-8 v2 sobre CU-8 v1), usar SendMessage al subagent existente en lugar de invocar nuevo via Agent.

**Beneficio:** continúa con full context, no relee inputs, más rápido y barato.

**A codificar en:** runtime `_runtime-adapter-guide.md`.

### 4.4 Vivienne workaround formal (POLÍTICA YA DOCUMENTADA, PENDIENTE INSTRUMENTAR)

La memoria `feedback_vivienne_token_explosion_pattern_v1` ya documenta el patrón y el workaround. **Falta:**
- Codificar el workaround en `vivienne/AGENT.md` (instrucción permanente "para decks >30 slides con charts, separar en 3 invocaciones: A) make_charts.py, B) deck assembly, C) RE assembly")
- Considerar hire de "DocBuilder" / "PPTXRender" especialista en renderizado mecánico

### 4.5 Word formal como artefacto SSOT (NUEVA POLÍTICA)

V6 Word es 50-70 páginas, 2.5 MB, con 20 charts inline. La memoria del repo dice "binarios son derivados runtime". Pero el Word V6 ES el SSOT (no derivado de un .md anterior, es el primary deliverable). **Posible excepción al principio `portable_text_as_ssot_principle`.** Necesita decisión Owner.

---

## 5. Problemas identificados (sin resolver)

### 5.1 Bug Raul-subagent nested delegation (CRÍTICO, sin resolver desde 2026-05-17)

- **Status:** documentado en memoria + intelligence/, decisión Owner pendiente entre 4 opciones de remediación
- **Aplicado de facto:** Opción 2 — main Claude orquesta. Funcionó en V5+V6.
- **Pendiente:** formalizar en SSOT de Raul + en CLAUDE.md raíz (Cardinal Rule).

### 5.2 Main Claude sobrecarga ejecutiva

- Escribió ~5000 líneas Python en V5+V6 (decks, charts, Word)
- Si esta carga persiste, el patrón Raul-subagent híbrido nunca se prueba realmente
- **Causas:** (a) Vivienne falla en decks grandes, (b) no hay specialist DocBuilder, (c) main Claude tiene Agent tool y termina absorbiendo todo

### 5.3 Specialists Genteca subutilizados

15 agentes (atlas, vael, solenne, vera, orlan, nerea, oz, etc.) no se invocaron porque el proyecto activo es consultoria-externa. Esto es correcto contextualmente, pero significa:
- Sus SSOTs pueden estar desactualizados sin que lo notemos
- Sus modelos LLM (todos Sonnet 4.6 actualmente) no se han stress-tested
- Cualquier evolución del repo no se está validando contra ellos

**Acción sugerida:** sesión de mantenimiento mensual donde se haga un "smoke test" con cada specialist (invocación dummy + check de output básico).

### 5.4 Variable PD2 (edad) en BBDD no procesable

Documentado en CU-8 v2 — la variable PD2 está en formato no numérico, impide construir rangos etarios. **Pendiente:** pedir a Cora re-exportar BBDD con PD2 codificada.

### 5.5 Gap: no hay specialist "DocBuilder"

Cuando se necesita generar documentos formales largos (`.docx`/`.md` >30 páginas con tablas + charts + notas metodológicas), main Claude termina haciéndolo directo. **Vivienne está pensada para PPTX, no para Word.**

**Propuesta:** hire de un specialist nuevo via Michelina. Detalles en §8.

### 5.6 Documento `PLAN_mejora_agentes_flujos_2026.md` (2026-04-29) sigue EN ESPERA

3 opciones A/B/C de mejora desde abril, no ejecutadas. Una de ellas (Opción B — plantillas Oz) sigue siendo relevante para GST julio 2026.

---

## 6. Propuesta: Modelos LLM dinámicos

### 6.1 Estado actual (estático)

Cada agente tiene 1 modelo fijo en su frontmatter. No hay mecanismo para que un agente use un modelo distinto según complejidad de la tarea.

### 6.2 Propuesta: matrix de modelo × complejidad

| Modelo | Cuándo usar | Costo relativo | Specialists candidatos |
|---|---|---|---|
| **Opus 4.7** (~75 USD/M tokens output) | Tareas que requieren razonamiento estratégico denso o coordinación compleja | 5× | raul, bruna (gobernanza), michelina (hire), paxs (research deep), **cuanti** (análisis estadístico denso), **sinta** (análisis temático profundo), vivienne (decks 40+ slides con narrativa compleja) |
| **Sonnet 4.6** (~15 USD/M tokens output) | Default para specialists con scope acotado y trabajo recurrente | 1× | atlas, vael, solenne, nerea, orlan, vera, methos (default), aurelio, oz, renzo, luma, vela, orfeo |
| **Haiku 4.5** (~3 USD/M tokens output) | Tareas mecánicas: indexación, logging, formato, extracción de patterns conocidos | 0.2× | sira (indexación), ivo (logging publicación), celeste (curation rutinaria), inboxbot (captura), corabridge (drop), ownerbridge (drop simple) |

### 6.3 Implementación técnica: 3 opciones

**Opción A — Per-agent override en invocación (simple, manual)**

Usar el parámetro `model` del tool `Agent` cuando se invoca. Main Claude decide en runtime según contexto.

```
Agent(subagent_type='cuanti', model='opus', prompt='...')  # para análisis denso
Agent(subagent_type='cuanti', model='sonnet', prompt='...') # para análisis simple
```

Pros: cero cambios de config. Contras: la decisión cae en main Claude (humano-dependiente).

**Opción B — Tiered model en frontmatter del agente (semi-estático)**

Cada agente define un mapping de tareas a modelos en su SSOT/runtime:

```yaml
model_tier:
  default: claude-sonnet-4-6
  long_analysis: claude-opus-4-7
  format_only: claude-haiku-4-5
```

El agent declara qué tier usar en el prompt. Main Claude pasa el parámetro `model` correspondiente.

Pros: explícito en cada agente. Contras: requiere editar 25 AGENT.md.

**Opción C — Routing automático por longitud de prompt + tipo de tarea (avanzado)**

Wrapper que analiza el brief (longitud, keywords como "análisis denso", "tabla grande", "indexar") y selecciona modelo. Más sofisticado pero requiere infraestructura nueva.

### 6.4 Recomendación

**Empezar con Opción A** (per-invocation override). Es la única que se puede probar sin tocar config. Validar con 3 casos de uso reales:
- Cuanti en Opus para análisis denso (CU-8 v3)
- Sira en Haiku para indexación de batch
- Vivienne en Opus para deck 50+ slides

Si funciona, migrar a Opción B (frontmatter tiered).

---

## 7. Workflows remotos — evolución y aprendizajes

### 7.1 OwnerBridge (ya documentado en memoria, status: producción permanente)

**Funciona cuando:** Owner está fuera y necesita disparar trabajo simple desde móvil.
**No funciona cuando:** la tarea requiere desktop (.pptx render, scripts python). V5 deck es ejemplo — OwnerBridge generó el .md pero no pudo .pptx.

**Mejora propuesta:** OwnerBridge debería **explícitamente devolver "tarea preparada, requiere desktop"** en lugar de intentar resolver con resultado parcial. Eso clarifica handoff.

### 7.2 InboxBot v5.0 (capture-only, validado)

Funcionando como diseñado. No requiere cambios. Posible mejora: análisis de cuáles tickets se transicionan más rápido vs cuáles se acumulan, para detectar bloqueos.

### 7.3 CoraBridge (efímero, expirado el 2026-05-17 23:59)

Decisión pendiente: ¿desactivar o convertir a permanente? Si Cora va a seguir como cliente recurrente, vale extender. Si fue solo para el proyecto Gama, desactivar.

### 7.4 Propuestas nuevas de bridges

| Nombre | Para qué | Prioridad |
|---|---|---|
| **DesktopBridge** | OwnerBridge entrega .md de tarea preparada; un agent local en sesión Raul lo lee y completa el render desktop | MEDIA |
| **ClientBridge genérico** | Reemplazo de CoraBridge ad-hoc — cualquier colaborador externo puede tener su propio bridge con expiry configurable | BAJA — solo si tenemos >2 colaboradores externos activos |

---

## 8. Agentes a hire (nuevos roles)

### 8.1 DocBuilder (PRIORIDAD ALTA)

**Rol:** especialista en producción de documentos formales largos (`.docx`/`.md`/`.pdf`) con tablas + charts + notas metodológicas. Lo que Vivienne es a PPTX, DocBuilder sería a Word/PDF.

**Capacidades:**
- python-docx + reportlab + matplotlib
- Plantillas: consulting formal, research report, technical spec, executive briefing
- Lectura de outputs de specialists (CU-*, IN-*, ME-*) y producción de documento integrado
- Iconografía + notas metodológicas anexas + lámina anexa táctica (patrón V6)

**Modelo sugerido:** Sonnet 4.6 default, Opus 4.7 para documentos >50 páginas

**Justifica hire por:** V5 y V6 main Claude absorbió esta carga (5000+ líneas de python). DocBuilder libera a main Claude para orquestación.

**Vía:** invocar a Michelina cuando próxima sesión arranque.

### 8.2 PriceAnalyst (PRIORIDAD MEDIA — específico para pricing/conjoint)

Si vienen más estudios con tema precios (Van Westendorp PSM, Gabor-Granger, Conjoint, DCE), vale tener specialist dedicado. Cuanti puede cubrir pero queda muy ancho.

### 8.3 (Otros considerados, decisión Owner)

- **VideoEditor** — si Genteca produce más video (Luma cubre actualmente). No prioritario.
- **TranscriptAnalyzer** — si volumen de Tactiq transcripts crece (actualmente Owner los lee manualmente). Posible.

---

## 9. Ajustes recomendados pendientes — consolidados

Lista de decisiones/cambios documentados en memoria que NO se han implementado:

| # | Item | Fecha doc | Memoria | Status |
|---|---|---|---|---|
| 1 | Patrón Raul-subagent: elegir entre 4 opciones de remediación | 2026-05-17 | `feedback_raul_subagent_no_nested_delegation` | Aplicado Opción 2 de facto, sin formalizar |
| 2 | Vivienne workaround codificado en SSOT | 2026-05-17 | `feedback_vivienne_token_explosion_pattern_v1` | Doc actualizada V5+V6, falta editar `vivienne/AGENT.md` |
| 3 | Plan abril 2026 mejora agentes Genteca (3 opciones A/B/C) | 2026-04-29 | `04-system/03-governance/PLAN_mejora_agentes_flujos_2026.md` | EN ESPERA — Opción B (plantillas Oz) sigue relevante para GST julio |
| 4 | CoraBridge: desactivar o extender | 2026-05-17 | `project_corabridge_gama_test` | Expiry pasó — sin decisión |
| 5 | BBDD PD2 (edad) re-exportar con rangos | 2026-05-18 | CU-8 v2 § blockers | Pendiente pedir a Cora |
| 6 | Verificar SAPI Exceline (4 marcas tecnológicas NTC) | 2026-05-07 | `project_marcas_anglicismos_junta` | 3 escalaciones críticas pendientes |
| 7 | Junta GME — protector monofásico Exceline | 2026-05-06 | `project_gme_protector_monofasico` | Escalación riesgo diseño Bruna→Owner pendiente |
| 8 | GST-RD: 5 decisiones Owner D1-D5 | 2026-05-04 | `project_gst_labels_july_deadline` | Pendientes |
| 9 | Backup memoria → OneDrive: validar restore | 2026-05-12 | `reference_memory_onedrive_backup` | Backup corriendo, restore no testeado |
| 10 | Modelo LLM dinámico framework | nuevo (este doc) | — | Para arrancar |
| 11 | DocBuilder hire vía Michelina | nuevo (este doc) | — | Para arrancar |
| 12 | ~75 WIP no commiteados en working tree | 2026-05-17 | session handoff | Owner debe commit-por-workstream |

---

## 10. Plan ejecutable para próxima sesión (priorizado)

### Bucket 1 — Cierre del ciclo V6 (próximas 24-48h, alta urgencia)

| # | Acción | Effort | Bloqueador |
|---|---|---|---|
| 1.1 | Cora revisa Word V6 en Drive Cora | — | tiempo Cora |
| 1.2 | Aplicar ajustes Cora al Word (si aplica) | 30-60 min | depende de feedback |
| 1.3 | Disparar Vivienne V6 PPTX (3 invocaciones separadas con anti-token-explosion) | ~1.5 h | Word aprobado |
| 1.4 | Drop final V6 (Word + 2 PPTX) + README + draft email Cora | 20 min | PPTX listo |
| 1.5 | Commit + push V6 final | 5 min | — |

### Bucket 2 — Capturar aprendizajes en memoria/SSOT (próxima sesión, ~30 min)

| # | Acción | Effort |
|---|---|---|
| 2.1 | Crear memoria `feedback_word_first_pptx_after_policy` con patrón V6 | 10 min |
| 2.2 | Crear memoria `feedback_send_message_continuation_pattern` con caso CU-8 v1→v2 | 10 min |
| 2.3 | Crear memoria `feedback_gate_reuse_between_versions_policy` con caso Bruna V4→V5→V6 | 10 min |
| 2.4 | Actualizar `feedback_vivienne_token_explosion_pattern_v1` con caso V6 main Claude fallback Word | 5 min |

### Bucket 3 — Decisiones Owner pendientes a tomar (próxima sesión, ~45 min de diálogo)

| # | Decisión | Opciones | Recomendación mía |
|---|---|---|---|
| 3.1 | Raul-subagent nested delegation: cuál de las 4 opciones de remediación adoptar | Op1 rollback / Op2 main orquesta / Op3 rediseñar scope / Op4 trigger files | **Op2** formalizada en SSOT (ya funciona de facto) |
| 3.2 | CoraBridge: desactivar o convertir permanente | Desact. / Permanente / Híbrido (extender 30d) | **Híbrido** si Cora seguirá siendo cliente activo |
| 3.3 | Word formal como excepción a `portable_text_as_ssot_principle` | Sí / No / Caso-por-caso | **Caso-por-caso** — solo para reportes formales >30 págs con charts |
| 3.4 | DocBuilder hire | Sí ya / Sí cuando se repita necesidad / No (main Claude cubre) | **Sí cuando se repita** (1 caso no justifica hire; 2 sí) |
| 3.5 | Modelos LLM dinámicos: Opción A/B/C | Per-invocation / Tiered frontmatter / Routing automático | **Op A primero** (sin cambios config, prueba en 3 casos) |
| 3.6 | PLAN mejora agentes Genteca abril 2026: retomar | Opción A One Pager auto / Opción B plantillas Oz / Opción C enriquecer Vael | **Opción B** (GST julio cerca, mayor ROI) |

### Bucket 4 — Mejoras de infraestructura (próxima 1-2 semanas)

| # | Acción | Effort | Prioridad |
|---|---|---|---|
| 4.1 | Codificar workaround Vivienne en `vivienne/AGENT.md` (instrucción permanente para decks grandes) | 15 min | ALTA |
| 4.2 | Probar Cuanti en Opus 4.7 con caso real (CU-9 si surge) — comparar calidad output vs costo | 1 sesión | MEDIA |
| 4.3 | Probar Sira/Ivo en Haiku 4.5 — medir si la indexación rutinaria mantiene calidad | 1 sesión | BAJA |
| 4.4 | Smoke test mensual de specialists Genteca subutilizados (atlas, vael, solenne, etc.) | 30 min/mes | BAJA |
| 4.5 | OwnerBridge: agregar mensaje "tarea preparada, requiere desktop" cuando aplique | 30 min | MEDIA |
| 4.6 | Validar restore de backup memoria desde OneDrive | 15 min | MEDIA |

### Bucket 5 — Hiring (próximas 2-4 semanas)

| # | Hire | Vía | Justificación |
|---|---|---|---|
| 5.1 | DocBuilder (Word/PDF formal) | Michelina + Paxs research | Validado por carga main Claude en V5+V6 |
| 5.2 | (Otros según Bucket 3 decisiones) | — | Depende de Owner |

---

## 11. Decisiones Owner pendientes — consolidadas para próxima sesión

(Ver Bucket 3 arriba — extraído acá para acceso rápido)

1. **Raul-subagent remediación:** ¿Opción 1, 2, 3, 4 o híbrida?
2. **CoraBridge:** ¿desactivar, permanente, o extender 30 días?
3. **Word como SSOT:** ¿caso-por-caso aceptable o mantener regla estricta?
4. **DocBuilder hire:** ¿proceder ya o esperar segundo caso?
5. **Modelos LLM dinámicos:** ¿empezar con Opción A esta semana?
6. **Plan abril 2026 mejora Genteca:** ¿retomar Opción B (Oz) antes de GST julio?
7. **CO de Notoriedad Gama:** ¿1, 2, 3 todas tomadas para V6, ratificar?

---

## 12. Memoria a crear/actualizar post-sesión

Cuando esta sesión cierre, las siguientes memorias deben crearse o actualizarse:

| Memoria | Acción | Contenido |
|---|---|---|
| `feedback_word_first_pptx_after_policy` | CREAR | Política V6 — Word-first → PPTX-after para consultorías externas |
| `feedback_send_message_continuation_pattern` | CREAR | Patrón continuation con SendMessage al subagent existente |
| `feedback_gate_reuse_between_versions_policy` | CREAR | Bruna gate se reusa cuando datos no cambian |
| `feedback_main_claude_executor_fallback_antipattern` | CREAR | Cuándo SÍ y cuándo NO debe main Claude absorber trabajo de specialists |
| `feedback_vivienne_token_explosion_pattern_v1` | UPDATE | Agregar caso V6 (Word generado por main Claude para evitar el patrón) |
| `project_consultoria_externa_gama_notoriedad_2026` | UPDATE | V5 + V6 entregados, próximos pasos PPTX V6 |
| `project_session_handoff_2026-05-19` | CREAR | Handoff próxima sesión con buckets 1-5 |
| `project_modelo_a_migration_state` | UPDATE | Agregar status post-V6 (4 agentes en Opus, 20 en Sonnet, framework dinámico propuesto) |
| `reference_modelos_llm_dinamicos_framework` | CREAR | Si Owner aprueba Opción A, documentar para futuros invocaciones |
| `project_lecciones_v5_v6` (este doc) | EXISTE en disco | Ya creado — referenciar desde MEMORY.md |

---

## Anexo A — Inventario completo de archivos del ciclo V5+V6

### Producidos por Cuanti
- `02-analysis/cuanti/2026-05-18_CU-8_preguntas-faltantes_v1.md` (32 KB)
- `02-analysis/cuanti/2026-05-18_CU-8_preguntas-faltantes_v2.md` (~28 KB)
- `02-analysis/cuanti/scripts/cu8_preguntas_faltantes.py` (51 KB)
- `02-analysis/cuanti/scripts/cu8_v2_extension.py` (~40 KB)
- `02-analysis/cuanti/outputs/json/CU8_preguntas_faltantes_20260518_v1.json` (121 KB)
- `02-analysis/cuanti/outputs/json/CU8_v2_extension_20260518.json` (~60 KB)
- `02-analysis/cuanti/outputs/plots/cu8_v2_heatmap_desconexion.png` (~80 KB)

### Producidos por Vivienne (V5 RE)
- `03-deck/V5/build_resumen_ejecutivo_v5.py` (38 KB)
- `03-deck/V5/2026-05-18_Notoriedad-Gama-2026_Resumen-Ejecutivo-V5.pptx` (350 KB)
- 3 charts PNG en `03-deck/V5/charts/`

### Producidos por Main Claude (V5 deck fallback + V6 todo)
- `03-deck/V5/build_deck_v5.py` (~70 KB) — V5 deck fallback
- `03-deck/V5/2026-05-18_Notoriedad-Gama-2026_V5.pptx` (1.7 MB) — V5 deck render
- 9 charts PNG en `03-deck/V5/charts/`
- `03-deck/V6/generate_charts_v6.py` (~25 KB) — V6 charts script
- `03-deck/V6/build_word_v6.py` (~110 KB) — V6 Word script
- `03-deck/V6/2026-05-18_Notoriedad-Gama-2026_V6.docx` (2.5 MB) — V6 Word
- 11 charts PNG en `03-deck/V6/charts/`
- `02-analysis/extract_guia.py` + `02-analysis/guia_preguntas_2026.md`
- `02-analysis/cuali_textos.json` (42 KB extracción cualitativo)
- `02-analysis/extract_cuali.py`

### Producidos por OwnerBridge (cloud)
- `2026-05-18_OwnerBridge_instruccion-de-continuar-con-v5_v1.md` (45 KB)
- `2026-05-18_OwnerBridge_instruccion-nueva_v1.md` (5 KB)
- Logs BRIDGE_LOG_OWNER_*

### Producidos por Explore
- (Respuesta en sesión — síntesis de 5 patrones de feedback Owner, sin archivo persistente)

---

## Anexo B — Referencias cruzadas

- Memoria HOT: `MEMORY.md` (índice 200 líneas, auto-load cada sesión)
- Arquitectura repo: `02-knowledge-base/00-raul-intelligence/methodology/`
- Conceptual agents: `04-system/02-agents/conceptual/*.md`
- Runtime agents: `.claude/agents/*/AGENT.md`
- CLAUDE.md raíz: `04-system/01-config/CLAUDE.md`
- Plan abril 2026: `04-system/03-governance/PLAN_mejora_agentes_flujos_2026.md`
- Migration state: memoria `project_modelo_a_migration_state`

---

*Documento producido por Main Claude (Opus 4.7) en sesión nocturna 2026-05-18, durante pausa de revisión Owner del Word V6. Material derivado de observación directa del ciclo V3→V4→V5→V6 + lectura de memoria HOT + inventario de configuración de agentes.*

*Propósito: dejar plan ejecutable y aprendizaje consolidado antes del cierre de sesión. NO requiere acción inmediata — diseñado para retomar en sesión próxima cuando el Owner pueda discutir cada Bucket.*

*Status: PROPUESTA. Cada Bucket requiere validación Owner antes de ejecución.*
