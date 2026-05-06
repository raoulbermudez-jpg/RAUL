# Dry-run mental CSC end-to-end — 3 casos canónicos

**Versión:** v1
**Fecha:** 2026-05-05
**Contexto:** Pendiente declarado en snapshot CSC 2026-05-02 ("validar 3 casos canónicos para detectar gaps antes de seguir construyendo"). Ejecutado autónomamente entre sesiones de Owner.
**Insumos:** `02-agents/content-supply-chain/ARCHITECTURE_Content-Supply-Chain.md` v1.1 (2026-05-03) · `02-agents/content-supply-chain/AGENTS_Content-Supply-Chain.md` v1.0 (2026-04-21) · conceptuales en `02-agents/conceptual/` · runtimes thin-adapter en `.claude/agents/`.
**Tipo:** análisis interno — NO modifica código ni docs core; produce findings para revisión.

---

## Cómo se hizo este dry-run

Para cada caso canónico se trazó el pipeline declarado por la SSOT (cadenas A/B/C/D del ARCHITECTURE) y se cross-checkeó nodo por nodo contra:

1. Misión y outputs codificados de cada agente en su conceptual.
2. Boundaries declarados (qué NO hace cada agente).
3. Inputs esperados y handoffs a aguas abajo.
4. Coherencia entre ARCHITECTURE v1.1, AGENTS v1.0 y conceptuales individuales.
5. Reglas de invalidez de Bruna §6.9 y gates por fase §6.4-bis.
6. Frontera Solenne ↔ Nerea operativa (carrusel editorial vs carrusel narrativo capítulo).
7. Frontera Orfeo ↔ Vela post-redirección 2026-05-03 (Orfeo solo motion, Vela único productor de audio).

El objetivo NO es validar pieza por pieza sino detectar dónde la cadena se rompe, queda ambigua o produce conflictos antes de que un caso real lo descubra a costa de tiempo del Owner.

---

## Caso 1 — Podcast 2 voces GST-R (Cadena B)

### Brief simulado

Owner pide un podcast corto (10-12 min) sobre la nueva línea GST-R, dos voces (host A neutro, host B técnico). Audiencia: instaladores eléctricos venezolanos. Distribución: YouTube + Spotify + waveform 60s para LinkedIn.

### Pipeline declarado (Cadena B)

```
Vera/Orlan → Vael → Aurelio → Nerea (NE-4 etiquetado) → Solenne (SO-X)
  → Vela (audio multi-voz) → (opcional) Luma video-cast → Bruna → Ivo → Sira
```

### Trazado nodo por nodo

| # | Nodo | Output esperado | Estado SSOT | Observación |
|---|---|---|---|---|
| 1 | Vera | Brief técnico GST-R | ✅ Existe en `03-projects/genteca/2026-04_GST-R_etiquetas/00-brief/GST-R_nueva_linea_brief_tecnico_v1.md` | Aplicable. Tiene gaps marcados §5 (curva inversa exacta sin definir) — claims con caveat literal heredan a Bruna. |
| 2 | Orlan | OL-1 / OL-2 competencia GST | ⚠ Existe `Orlan_OL-1_competencia-naming-termico_v1.md` para empaque GSM, NO para GST-R | Orlan tendría que producir OL-X específico GST-R. Sin él, el podcast sale con datos competitivos genéricos o sin diferenciación competitiva. |
| 3 | Vael | VA-1 / VA-3 / VA-5 línea GST-R | ⚠ Existe `Vael_messaging_framework_v1.md` empaque, no específico GST-R | Igual que (2): VA-X para GST-R no existe. Aurelio bajaría sin framework messaging dedicado. |
| 4 | Aurelio | AU-1 plan podcast + AU-3 brief a Nerea | ✅ Patrón AU-X codificado | OK siempre que (2) y (3) existan. |
| 5 | Nerea | NE-4 multi-voz con turnos etiquetados Voz A / Voz B | ✅ NE-4 explícitamente codificado para multi-voz | OK — formato turnos etiquetados está documentado en conceptual Nerea §11.3. |
| 6 | Solenne | SO-X copy editorial / on-screen / captions | ⚠ Coexiste con NE-4: el conceptual Nerea §11.3 sugiere que el contenido editorial del podcast (descripción, captions) sale de Solenne, pero ARCHITECTURE Cadena B línea 78 dice "Solenne → SO-X copy editorial / on-screen / captions" como nodo paralelo a NE-4, no aguas abajo. **Frontera no clara:** ¿Solenne consume NE-4 finalizado y produce captions? ¿O Solenne produce primero y Nerea integra a NE-4? | El conceptual sugiere lo primero (Solenne post-NE-4). ARCHITECTURE Cadena B sugiere paralelo. **Gap de orden.** |
| 7 | Vela | VE-1 voiceover script multi-voz + VE-2 timing + VE-4 voice bundle | ✅ VE-X codificado, NE-4 etiquetado como input único | OK. Boundaries claras: no inventa diálogos, no reasigna turnos. |
| 8 | Luma (opcional) | LU-X video-cast | ✅ Cadena B línea 82 "(opcional) Luma → video-cast" | OK pero no resuelto: si la pieza solo tiene waveform 60s para LinkedIn, ¿quién produce ese waveform — Vela o Luma? **Gap de scope.** |
| 9 | Bruna | BR-2 aprobación 4 fases (VA-X + AU-X + NE-X + SO-X) | ✅ §6.4-bis declara gate por fase | OK. Pero como (2) (3) faltan, Bruna gatea con caveat heredado de Vera §5 (curva inversa) sin VA-5 dedicado GST-R — riesgo de claim sin gate previo. |
| 10 | Ivo | IV-1..IV-5 publicación 3 canales (YouTube, Spotify, LinkedIn) | ✅ IV-X codificado | OK. Multicanal soportado. |
| 11 | Sira | catálogo + AU-5 candidato | ✅ Ruta `04-system/05-indexes/` declarada | OK. |

### Gaps detectados Caso 1

- **G1.1.** No hay OL-X ni VA-X específico GST-R. Bajar a producción sin esos insumos genera podcast con messaging genérico.
- **G1.2.** Frontera Solenne ↔ Nerea en Cadena B no resuelta: ¿quién va primero — NE-4 → Solenne post-procesa, o Solenne paralelo? El conceptual y ARCHITECTURE dan señales contradictorias.
- **G1.3.** Producción del waveform 60s LinkedIn no asignada explícitamente. Es subproducto de audio (Vela) o pieza de video (Luma)? Sin regla, decide el productor que reciba primero.
- **G1.4.** AGENTS_CSC v1.0 ficha Vela (líneas 233-267) describe Vela como solo single-voice — desactualizado vs ARCHITECTURE v1.1 y conceptual. Si un agente lee AGENTS y no ARCHITECTURE, escala a Owner pidiendo otro productor para multi-voz que ya no existe.

---

## Caso 2 — Reel motion-heavy bombas (Cadena A — variante reel)

### Brief simulado

Owner pide un reel de 30s para Instagram sobre el GST-RM ProMotor para bombas hidroneumáticas. Quiere motion graphics fuerte (curva inversa visualizada como animación), narración corta, on-screen text destacado. Cierre con CTA al WhatsApp.

### Pipeline declarado (Cadena A — reel)

```
Vera (técnico) → Vael (messaging) → Aurelio (AU-1)
  → Nerea (NE-2 reel)
    → en paralelo:
       Atlas (AT-2 key visual estático base + AT-1 si aplica)
       Orfeo (OR-1 motion system + OR-2 animated assets + OR-3 scene motion map)
       Vela (VE-1 voiceover narración corta single-voice)
    → Luma (LU-1 spec + LU-2 cut list integrando motion + audio + visuales)
  → Bruna → Ivo → Sira
```

### Trazado nodo por nodo

| # | Nodo | Output esperado | Estado SSOT | Observación |
|---|---|---|---|---|
| 1 | Vera | Reusa brief GST-R existente | ✅ | OK — el brief técnico Vera v1 cubre GST-RM con detalle, incluye caveats curva inversa. |
| 2 | Vael | VA-3 message map reel + VA-5 guardrails | ⚠ No existe VA-X dedicado GST-R | Mismo gap G1 — bajaría sin framework dedicado. |
| 3 | Aurelio | AU-1 plan reel + AU-3 brief a Nerea | ✅ | OK formato. |
| 4 | Nerea | NE-2 reel con hook 3s, beat único, CTA WhatsApp | ✅ NE-2 codificado | OK. |
| 5 | Atlas | AT-2 key visual estático ProMotor (base sobre la que Orfeo anima) | ✅ AT-2 codificado | OK. Pero **dependencia de orden con Orfeo no declarada**: ¿Atlas entrega primero AT-2 → Orfeo lo anima? ¿O Orfeo decide qué necesita y solicita a Atlas? El conceptual Orfeo lista AT-X como input pero no formaliza el handshake. **Gap de coordinación.** |
| 6 | Orfeo | OR-1 + OR-2 + OR-3 motion system + animated assets + scene motion map | ✅ OR-X codificado | OK. Reglas tool-agnósticas y brand wiki como input declarados. |
| 7 | Vela | VE-1 narración single-voice + VE-2 timing | ✅ VE-X codificado para single-voice | OK. |
| 8 | Luma | LU-1 spec + LU-2 cut list + LU-4 captions + LU-3 multi-format (9:16 reel + 1:1 LinkedIn) + LU-5 handoff a Ivo | ✅ LU-X codificado, integración audio Vela + visual Atlas + motion Orfeo declarada | OK. |
| 9 | Bruna | BR-2 gate por fase | ✅ | OK con caveat heredado curva inversa Vera §5. |
| 10 | Ivo | IV-1..IV-5 publicación Instagram + LinkedIn | ✅ | OK. |
| 11 | Sira | catálogo + AU-5 | ✅ | OK. |

### Gaps detectados Caso 2

- **G2.1.** Mismo gap G1.1: VA-X GST-R no existe.
- **G2.2.** Coordinación Atlas → Orfeo en piezas motion-heavy no formalizada. ¿Atlas produce AT-2 primero y Orfeo lo anima, o iteran? Sin protocolo, riesgo de retrabajo (Atlas entrega un layout que no se anima bien y Orfeo pide cambios).
- **G2.3.** El conceptual Orfeo §8 Interactions lista Atlas como "Antes" pero el conceptual Atlas §8 Interactions no lista Orfeo como "Después" (verificable). **Inconsistencia bidireccional posible.** _(no verificado en este dry-run — requiere lectura cruzada de ambos conceptuales en sesión Owner)_
- **G2.4.** Brand kit motion: ¿existe redline maestro de motion system para Genteca? Conceptual Orfeo cita "visual system de Oz cuando existe" — para Genteca no parece existir aún. Sin sistema maestro, cada reel inventa motion ad-hoc.

---

## Caso 3 — Carrusel narrativo serie ABC (Cadena A — carrusel)

### Brief simulado

Owner pide una serie de 3 carruseles LinkedIn sobre la línea GST-R: Carrusel A "qué es un supervisor trifásico", Carrusel B "curva inversa explicada", Carrusel C "cómo elegir entre RM/RR/RT/RD". Arco macro: educar a instaladores en 3 capítulos. Cadencia semanal.

### Pipeline declarado (Cadena A — carrusel narrativo serie)

```
Vera (técnico) → Vael (VA-X serie) → Aurelio (AU-1 + AU-2 trimestral + NE-5 narrative map invocado vía Nerea)
  → Nerea (NE-3 por capítulo + NE-5 narrative map) + Solenne (SO-4 body editorial input)
    → Atlas (AT-1 carousel pack por capítulo)
  → Bruna (gate por capítulo) → Ivo (3 publicaciones programadas) → Sira (catálogo + propuesta reciclaje)
```

### Trazado nodo por nodo

| # | Nodo | Output esperado | Estado SSOT | Observación |
|---|---|---|---|---|
| 1 | Vera | Brief técnico GST-R | ✅ Reusa | OK. |
| 2 | Vael | VA-1 framework + VA-3 message map serie | ⚠ Mismo gap | OK formato, falta documento. |
| 3 | Aurelio | AU-1 serie + AU-2 (acumulativo trimestre) + AU-3 brief a Nerea | ✅ Codificado, AU-2 path declarado en `03-projects/<dominio>/_governance/` | OK. |
| 4 | Nerea | NE-3 por capítulo + NE-5 narrative map | ✅ NE-3 codificado solo para "carrusel narrativo capítulo de serie con arco macro" — caso aplica perfectamente | OK. Frontera Solenne ↔ Nerea correcta: serie con arco → Nerea. |
| 5 | Solenne | SO-4 body editorial como input para NE-3 | ✅ SO-4 codificado para Genteca | OK. |
| 6 | Atlas | AT-1 carousel pack (set de slides) por capítulo | ✅ AT-1 codificado | OK. Inputs declarados: NE-3 + SO-4. |
| 7 | Bruna | BR-2 gate por capítulo + caveat literal por slide si aplica | ✅ §6.4-bis | OK. Pero **¿gate por capítulo o por serie completa?** En serie con arco, si el cap 1 sale aprobado y el cap 2 cambia el ángulo del arco, ¿Bruna re-gatea cap 1? **Gap de gate sobre series.** |
| 8 | Ivo | IV-1 chain log con 3 sub-cadenas + IV-2 outputs index + IV-5 publication summary | ✅ IV-X codificado | OK. |
| 9 | Sira | catálogo serie + propuesta AU-5 reciclaje (carruseles educativos son alta probabilidad de reciclaje) | ✅ | OK. |

### Gaps detectados Caso 3

- **G3.1.** Mismo gap G1.1: VA-X GST-R no existe (recurrente — ver hallazgo transversal).
- **G3.2.** Bruna sobre series con arco macro: gate por capítulo o por serie completa? Si arco cambia mid-serie, ¿reaperturas? El conceptual Bruna §6.9 reglas de invalidez no cubre este caso. **Gap de regla.**
- **G3.3.** AU-2 acumulativo trimestral: la convención dice que vive en `03-projects/<dominio>/_governance/`. Para Genteca, esa carpeta existe (`03-projects/genteca/_governance/2026-05-03_genteca_claim-approval-log_v1.md` recién commiteado) — pero el AU-2 trimestral aún no se ha producido. ¿Se invoca cada vez que hay nueva campaña o tiene cadencia propia? **Ambigüedad de invocación.**
- **G3.4.** Coordinación Atlas con paleta del producto en serie multi-capítulo: ¿cada capítulo usa color del producto principal (RM gris, RR azul, RT verde, RD negro-dorado) o serie usa identidad propia? **Decisión Owner pendiente** — no es gap del sistema sino del proyecto, pero sin guía Aurelio AU-1 lo deja al criterio de Atlas.

---

## Hallazgos transversales (cross-case)

### H1 — VA-X específico de línea de producto faltante (recurrente en los 3 casos)

GST-R no tiene VA-1 / VA-3 / VA-5 dedicado. Los 3 casos bajan a producción con messaging genérico o heredado de empaque GSM. **Acción recomendada:** Vael produce VA-1 y VA-5 GST-R antes de cualquier campaña GST-R (incluida la de etiquetas que ya está activa). Sin esto, Bruna gatea sin framework previo y los caveats heredados pueden ser insuficientes.

### H2 — AGENTS_CSC v1.0 desactualizado vs ARCHITECTURE v1.1

`AGENTS_Content-Supply-Chain.md` (2026-04-21) NO refleja:
- Vela ampliada a single + multi-voz (sigue diciendo "voz-única").
- Orfeo redirección a motion graphics OR-X (sigue describiendo "Audio & Conversation Producer" en otras menciones, pero ya cambió en su ficha §3 dentro de AGENTS — verificar coherencia).
- Códigos de outputs (AU-X / NE-X / VA-X / BR-X / SO-X / VE-X / OR-X / AT-X / LU-X / IV-X) en fichas de Atlas, Luma, Vela, Bruna, Ivo, Sira.
- Boundaries actualizadas Solenne ↔ Nerea (carrusel editorial vs carrusel narrativo capítulo).

**Riesgo:** un agente nuevo (o el mismo Raul cargando AGENTS sin ARCHITECTURE) puede tomar decisiones según versión obsoleta.

**Acción recomendada:** Pasada-2 limpieza AGENTS_CSC (también pendiente declarado snapshot 2026-05-02). Sincronizar con ARCHITECTURE v1.1 y conceptuales actuales.

### H3 — Frontera Solenne ↔ Nerea en Cadena B no resuelta

¿Solenne consume NE-4 finalizado y produce captions/descripción, o produce SO-X paralelo a NE-4? Las dos lecturas son posibles según ARCHITECTURE línea 78 vs conceptual Nerea §11.3.

**Acción recomendada:** decidir orden canónico y reflejar en ARCHITECTURE Cadena B + conceptual Nerea + conceptual Solenne. Recomendación basada en lógica: Solenne post-NE-4 (consume el guion estable y produce paratexto editorial). Pero es decisión Owner.

### H4 — Coordinación Atlas ↔ Orfeo en piezas motion-heavy

No hay protocolo formal de handshake. Conceptual Orfeo lista Atlas como "Antes" pero el conceptual Atlas no necesariamente lista Orfeo como "Después" (verificación pendiente). En piezas motion-heavy, esto produce iteración (Atlas entrega layout, Orfeo descubre que no anima bien, vuelve a Atlas).

**Acción recomendada:** documentar protocolo en ARCHITECTURE — Atlas entrega AT-X "anima-ready" (con capas separadas, sin texto rasterizado, con safe-areas declaradas). Orfeo aporta requisitos de animación a Atlas antes de que Atlas finalice cuando la pieza es declaradamente motion-heavy.

### H5 — Gate Bruna sobre series con arco macro

Sin regla específica. Si capítulos posteriores cambian el arco, ¿reaperturas de capítulos anteriores? El conceptual Bruna §6.9 cubre invalidez pero no reaperturas por arco.

**Acción recomendada:** añadir cláusula a §6.9 — "Cuando una serie modifica el arco macro mid-serie, los capítulos publicados quedan flagged para revisión por coherencia narrativa, no para retiro automático. Decisión Owner de re-publicar correcciones o dejar histórico."

### H6 — Brand kit motion para Genteca no existe

Para piezas motion-heavy (Caso 2), Orfeo invoca "visual system de Oz cuando existe". Para Genteca no existe aún. Sin sistema maestro, cada reel inventa motion ad-hoc → fragmentación visual de la marca.

**Acción recomendada:** producir motion system Genteca v1 (Orfeo OR-1) como artefacto de marca, no como output de campaña. Tarea para Owner + Orfeo + Vael (validar tono).

### H7 — AU-2 acumulativo trimestral: cuándo se invoca

`03-projects/genteca/_governance/` ya tiene archivos pero no AU-2. ¿Se produce cada vez que hay nueva campaña o tiene cadencia propia (mensual / trimestral)?

**Acción recomendada:** decidir cadencia y reflejar en conceptual Aurelio.

---

## Resumen ejecutivo de gaps

| ID | Tipo | Severidad | Owner asume / Sistema asume |
|---|---|---|---|
| H1 | Insumo faltante (VA-X GST-R) | Alta | Sistema bloquea hasta producir |
| H2 | Doc desactualizado (AGENTS_CSC) | Media | Sistema corrige (pasada-2) |
| H3 | Frontera ambigua (Solenne ↔ Nerea Cadena B) | Media | Owner decide regla canónica |
| H4 | Protocolo faltante (Atlas ↔ Orfeo) | Media | Sistema documenta tras decisión Owner |
| H5 | Regla faltante (Bruna gate series) | Baja | Sistema añade cláusula §6.9 |
| H6 | Artefacto faltante (motion system Genteca) | Media | Owner + Orfeo + Vael producen |
| H7 | Cadencia ambigua (AU-2 trimestral) | Baja | Owner decide y Aurelio refleja |

| ID | Tipo | Severidad |
|---|---|---|
| G1.3 | Producción waveform LinkedIn no asignada | Baja |
| G2.4 | Brand kit motion Genteca = H6 | (consolidado) |
| G3.4 | Paleta serie multi-capítulo | Decisión por proyecto |

---

## Próximos pasos sugeridos (no ejecutar sin Owner)

1. **Vael produce VA-1 + VA-5 GST-R** antes de seguir con campañas GST-R (incluida etiquetas activa).
2. **Pasada-2 limpieza AGENTS_CSC v1.0 → v1.1** sincronizando con ARCHITECTURE v1.1 y conceptuales actuales (pendiente declarado snapshot 2026-05-02).
3. **Decidir frontera Solenne ↔ Nerea Cadena B** y reflejar en ARCHITECTURE + conceptuales.
4. **Documentar protocolo Atlas ↔ Orfeo** en ARCHITECTURE para piezas motion-heavy.
5. **Añadir cláusula §6.9 Bruna** sobre gate de series con arco modificado.
6. **Producir motion system Genteca v1** como artefacto de marca (Orfeo OR-1 inaugural).
7. **Decidir cadencia AU-2** y reflejar en conceptual Aurelio.

---

*Dry-run preparado autónomamente entre sesiones de Owner. Findings derivados exclusivamente de lectura de ARCHITECTURE / AGENTS / conceptuales — no se consultaron piezas reales producidas. Cualquier gap aquí listado puede estar resuelto en lugares no consultados; verificar antes de actuar.*
