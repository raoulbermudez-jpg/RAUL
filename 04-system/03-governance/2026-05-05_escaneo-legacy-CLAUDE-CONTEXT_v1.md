# Escaneo de referencias legacy en docs config core

**Versión:** v1
**Fecha:** 2026-05-05
**Contexto:** Pendiente declarado en snapshot CSC 2026-05-02 ("limpieza pasada-2 de menciones legacy 'Content Strategist' / 'guion de Nerea' sin códigos AU-X / NE-X" en CLAUDE_genteca / CONTEXT_genteca).
**Tipo:** análisis interno — NO modifica archivos. Lista de hallazgos para revisión Owner.
**Archivos escaneados:**
- `04-system/01-config/CLAUDE.md` (raíz)
- `04-system/01-config/CONTEXT_core.md`
- `04-system/01-config/CLAUDE_genteca.md`
- `04-system/01-config/CONTEXT_genteca.md`
- `04-system/02-agents/content-supply-chain/AGENTS_Content-Supply-Chain.md` (incluido por dry-run CSC; ver memo paralelo)

---

## Resumen ejecutivo

| Archivo | Hallazgos | Severidad | Acción sugerida |
|---|---|---|---|
| `CLAUDE.md` (raíz) | 6 entradas Capa 2b sin familias codificadas + 1 entrada Orfeo desactualizada + 1 regla routing ambigua | **Alta** | Reescribir tabla Capa 2b + reescribir regla routing Solenne vs Nerea |
| `CONTEXT_core.md` | Sin hallazgos legacy críticos. Describe estructura de carpetas, no agentes. | Baja | Sin acción. |
| `CLAUDE_genteca.md` | 1 entrada Solenne con "video scripts" incoherente + Vael sin códigos VA-X | Media | Reescribir 2 filas tabla Capa 3 |
| `CONTEXT_genteca.md` | Snapshot proyectos activos del 2026-04-25 — desactualizado a hoy 2026-05-05 | Media | Refrescar tabla §"Contexto de proyectos activos" |
| `AGENTS_CSC.md` | Ver memo dry-run CSC §H2 — pasada-2 sincronización con ARCHITECTURE v1.1 | Media | Tarea separada (no incluida aquí) |

---

## Hallazgos detallados

### 1. `CLAUDE.md` (raíz) — Capa 2b Content Supply Chain

**Ubicación exacta:** sección "Capa 2 — Servicios Globales ⭐" → subsección "2b — Content Supply Chain ⭐" → tabla con 9 agentes.

#### 1.1 Orfeo desactualizado (severidad alta)

**Texto actual:**
```
| Orfeo ⭐ | Producción | Audio & Conversation Producer | Contenido multi-voz, podcasts, conversaciones estilo studio |
```

**Problema:** Orfeo fue redirigido el 2026-05-03 a Motion Graphics & Visual Systems Production Lead. Ya NO produce audio. La memoria persistente de redirección está documentada en snapshot CSC. Esta línea contradice el conceptual vigente de Orfeo y la ARCHITECTURE v1.1.

**Texto sugerido:**
```
| Orfeo ⭐ | Producción | Motion Graphics & Visual Systems Production Lead (OR-1..OR-5) | Motion graphics, overlays, transiciones, animated assets reutilizables; integra a video producido por Luma |
```

#### 1.2 Vela sin scope multi-voz (severidad alta)

**Texto actual:**
```
| Vela ⭐ | Producción | Narration & Voiceover | Narración de voz única, voiceover para video o presentación |
```

**Problema:** Vela fue ampliado el 2026-05-03 a único productor de audio del CSC, cubriendo single-voice y multi-voz (diálogo / podcast corto). Esta línea omite multi-voz.

**Texto sugerido:**
```
| Vela ⭐ | Producción | Voiceover & Audio Production Lead (VE-1..VE-5) | Único productor de audio del CSC. Voiceover single-voice y conversaciones de una o dos voces (diálogo / podcast corto) ejecutando NE-4 con turnos etiquetados Voz A / Voz B |
```

#### 1.3 Aurelio / Nerea / Atlas / Bruna / Ivo / Sira sin códigos de outputs (severidad media)

**Texto actual (6 filas):**
```
| Aurelio ⭐ | Estrategia | Content Strategist | First gate ... |
| Nerea ⭐ | Estrategia | Script & Narrative Architect | Después de Aurelio ... |
| Atlas ⭐ | Producción | Static Visual Producer | Carruseles, infografías ... |
| Bruna ⭐ | Gobernanza | Brand & Risk Governance | Gate obligatorio ... |
| Ivo ⭐ | Distribución | Distribution & Channel Strategist | Canal, fecha, metadata ... |
| Sira ⭐ | Memoria | Archive, Version & Recycling | Versiona, cataloga ... |
```

**Problema:** Todos los conceptuales y runtimes thin-adapter ya operan con familias codificadas (AU-X / NE-X / AT-X / BR-X / IV-X / Sira tiene catálogo canónico path declarado). CLAUDE.md raíz no las refleja — desincroniza con SSOT.

**Texto sugerido:**
```
| Aurelio ⭐ | Estrategia | Content Strategist (AU-1..AU-5) | First gate — campañas, lanzamientos, planes multi-formato. AU-1 plan, AU-2 mapa trimestral, AU-3 brief Nerea, AU-4 brief Solenne, AU-5 reciclaje |
| Nerea ⭐ | Estrategia | Script & Narrative Architect (NE-1..NE-5) | Después de Aurelio. NE-1 guion largo, NE-2 reel, NE-3 carrusel narrativo capítulo, NE-4 audio single/multi-voz etiquetado, NE-5 narrative map |
| Atlas ⭐ | Producción | Static Visual Production Lead (AT-1..AT-5) | AT-1 carousel pack, AT-2 single static / key visual, AT-3 infografía, AT-4 layout PDF (handoff Oz si refinamiento), AT-5 visual adaptation matrix |
| Bruna ⭐ | Gobernanza | Risk & Claims Governance Lead (BR-1..BR-5) | Gate obligatorio antes de Ivo. 4 fases del pipeline (VA / AU / NE / SO). BR-2 acumulativo por dominio. BR-5 precedentes transversal |
| Ivo ⭐ | Distribución | Content Publication & Logging Orchestrator (IV-1..IV-5) | IV-1 chain log, IV-2 outputs index, IV-3 feed Sira, IV-4 feed Celeste, IV-5 publication summary. No publica sin sello Bruna |
| Sira ⭐ | Memoria | Archive, Version & Recycling Librarian | Single source of truth reciclaje (AU-5) en `04-system/05-indexes/`. Sin entrada en catálogo, no existe como memoria reciclable |
```

#### 1.4 Regla routing Solenne vs Nerea ambigua post-redirección Orfeo (severidad alta)

**Texto actual:**
```
**Routing para Content Supply Chain (Capa 2b):**
- ...
- **Solenne vs. Nerea**: Solenne es escritora B2B Genteca-específica (blog, LinkedIn, email, product copy). Nerea es la arquitecta de guiones y narrativa para producción multimodal (video, audio, carrusel). Si el output final es texto publicable directamente → Solenne. Si el output alimenta a Orfeo/Luma/Vela/Atlas → Nerea.
```

**Problemas:**
1. La frontera operativa formal Solenne ↔ Nerea (snapshot CSC §4) es más específica: carrusel editorial individual = Solenne (SO-1); carrusel narrativo capítulo de serie con arco macro multi-pieza = Nerea (NE-3).
2. Mencionar Orfeo en "alimenta a Orfeo" es residuo de cuando Orfeo era audio. Ahora Orfeo es motion graphics que se alimenta de NE-X igual, pero la lista debe leerse "Atlas / Luma / Vela / Orfeo" (todos los de Capa 3) sin singularizar Orfeo.

**Texto sugerido:**
```
- **Solenne vs. Nerea (frontera operativa):**
  - Pieza editorial individual (post LinkedIn suelto, email, header, body landing simple, descripción producto, copy empaque, caption, ficha amigable, **carrusel editorial estándar**) → **Solenne (SO-1 / SO-2 / SO-3)**.
  - Pieza audiovisual o pieza dentro de **serie con arco narrativo macro multi-pieza** (incluye carrusel narrativo capítulo) → **Nerea (NE-X)**, con SO-4 de Solenne como input de body editorial cuando aplica.
  - Si la pieza alimenta a Atlas / Luma / Vela / Orfeo (cualquier productor Capa 3) → entra por Nerea.
```

---

### 2. `CONTEXT_core.md`

**Hallazgos:** sin entradas legacy críticas. El doc describe estructura de carpetas, principios local-first y referencia a índices. No menciona agentes específicos ni nomenclatura legacy de outputs.

**Acción sugerida:** ninguna en esta pasada. _(Verificar en próxima auditoría si la sección "Archivos core vs companion (PERPLEXITY)" sigue vigente — el commit `7ddca3f` ya incluyó "limpieza PERPLEXITY".)_

---

### 3. `CLAUDE_genteca.md` — Capa 3 dominio Genteca

**Ubicación exacta:** sección "Agentes disponibles para Genteca (Capa 3)" → tabla con 7 agentes.

#### 3.1 Solenne con scope incoherente (severidad media)

**Texto actual:**
```
| Solenne | Contenido B2B: blog, LinkedIn, email, video scripts, case studies, product copy |
```

**Problema:** "video scripts" no es scope de Solenne. La frontera operativa formal asigna video scripts a Nerea (NE-1 / NE-2). Solenne hace SO-1 / SO-2 / SO-3 / SO-4 — texto editorial publicable directamente o body editorial input para Nerea.

**Texto sugerido:**
```
| Solenne | Copy & Editorial Execution Lead (SO-1..SO-5): post LinkedIn, email, body landing simple, descripción producto, copy empaque, captions, fichas amigables, body editorial (SO-4) input para Nerea cuando hay narrativa multi-pieza, mini-cover note de trazabilidad |
```

#### 3.2 Vael sin códigos VA-X (severidad media)

**Texto actual:**
```
| Vael | Estrategia de marca y mensajería, positioning, tono de voz, campaign briefs, launch kits |
```

**Texto sugerido:**
```
| Vael | Brand & Messaging Strategist (VA-1..VA-5): VA-1 messaging framework, VA-2 positioning, VA-3 message map por campaña × audiencia × canal, VA-4 content brief para CSC, VA-5 guardrails (claims defendibles ✅ / con caveat ⚠ / prohibidos ❌) |
```

#### 3.3 Renzo y Oz sin familias codificadas (informativo)

**Estado actual:** familias OR-X (Orfeo) y OC-X (Oz) están **declaradas pero no migradas** según snapshot CSC §"Familias de outputs codificadas (recordatorio)" — ambos marcados "(no migrado en esta sesión)".

**Acción sugerida:** sin acción ahora. Cuando se codifiquen formalmente, actualizar también este CLAUDE_genteca.

---

### 4. `CONTEXT_genteca.md` — snapshot proyectos activos

**Ubicación exacta:** sección "Contexto de proyectos activos (snapshot 2026-04-25)" → tabla.

#### 4.1 Snapshot proyectos desfasado 10 días (severidad media)

**Texto actual:**
```
## Contexto de proyectos activos (snapshot 2026-04-25)

| Proyecto | Estado | Nota |
|----------|--------|------|
| Empaque GSM-MB / RB / RF | En revisión (Keiddys) | Nuevas cajas, cambio visual — 3 versiones de delta enviadas a Ozwaldo |
| Etiquetas nueva línea GST-R | En revisión (I&D) | 4 productos, brief técnico v1 generado, pendiente confirmación curva inversa |
```

**Estado real al 2026-05-05 (verificable en working tree y commits recientes):**
- **Empaque GSM-MB-RB-RF:** completó cadena CSC Alternativa B refinada (B-sin-NTC) con cadena Vael VA-5 → Bruna BR-2 → Solenne SO-1 v3 → Orlan OL-1 → Atlas mockup → Aurelio AU-1 v2.1 (este último de hoy). Listo para Junta Directiva. Commit `81a38a7`.
- **Etiquetas GST-R:** Oz entregó propuesta visual única (PROP_GST_ETQ.jpg) el 2026-05-04 con 3 productos × 3 líneas. Línea 2 seleccionada. GST-RD pendiente próxima entrega Oz. Commit `1348785`. Falta GST-RD + título "Supervisor Trifásico de Voltaje" + 5 decisiones Owner D1-D5.

**Texto sugerido:**
```
## Contexto de proyectos activos (snapshot 2026-05-05)

| Proyecto | Estado | Nota |
|----------|--------|------|
| Empaque GSM-MB / RB / RF / RE | Listo para Junta Directiva | Alternativa B refinada (B-sin-NTC). Cadena CSC completa: VA-5 → BR-2 → SO-1 v3 → OL-1 → Atlas mockup → AU-1 v2.1. Cambio quirúrgico: "Sensor NTC incorporado*" → "Autoprotección térmica activa*" (anti revelación de IP por observación José Miguel Canudas) |
| Etiquetas GST-R | Propuesta Oz v1 recibida 2026-05-04 | 3 productos visibles (RM/RR/RT) en 3 líneas de diseño. Línea 2 seleccionada Owner. GST-RD pendiente próxima entrega Oz + título "Supervisor Trifásico de Voltaje" + decisiones D1-D5 (color RM, indicadores superiores, badges, diales/datos técnicos, pantone azul). Brief técnico Vera v1 con gap curva inversa pendiente I&D |
```

---

## Conclusión + recomendaciones

### Acciones de alta prioridad

1. **Reescribir tabla Capa 2b en `CLAUDE.md` raíz** (1.1 + 1.2 + 1.3) — este doc es el primer cargado por cualquier sesión Raul. Su desactualización propaga errores a todas las sesiones.
2. **Reescribir regla routing Solenne vs Nerea en `CLAUDE.md` raíz** (1.4).

### Acciones de media prioridad

3. **Reescribir 2 filas en `CLAUDE_genteca.md`** (3.1 Solenne + 3.2 Vael).
4. **Refrescar snapshot proyectos en `CONTEXT_genteca.md`** (4.1).
5. **Pasada-2 AGENTS_CSC** — ver memo dry-run §H2 (separado).

### Acciones diferidas

6. Renzo + Oz familias codificadas — cuando se codifiquen formalmente.
7. CONTEXT_core.md sección PERPLEXITY — verificar vigencia tras commit `7ddca3f`.

### Modo de aplicación recomendado

Las 5 acciones (1-5) se pueden ejecutar en **un solo commit** `docs(config): pasada-2 limpieza legacy CLAUDE / CONTEXT / AGENTS — sincronización con ARCHITECTURE v1.1`. Tamaño estimado: 1 archivo CLAUDE.md raíz + 1 CLAUDE_genteca + 1 CONTEXT_genteca + 1 AGENTS_CSC = 4 archivos. Cero cambios de comportamiento — solo doc.

**No ejecutado autónomamente** porque toca docs core que el Owner debería revisar antes de commit. Quedan listos los textos sugeridos arriba para copy-paste.

---

*Escaneo preparado autónomamente entre sesiones de Owner. Todos los textos sugeridos están alineados con la SSOT vigente al 2026-05-05 (ARCHITECTURE_CSC v1.1, conceptuales actualizados, snapshot CSC 2026-05-02).*
