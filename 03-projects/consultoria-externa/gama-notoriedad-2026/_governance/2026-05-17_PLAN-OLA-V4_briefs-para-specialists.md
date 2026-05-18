---
fecha: 2026-05-17
autor: Raul (subagent híbrido Opus 4.7)
proyecto: gama-notoriedad-2026
ola: V4 (capa wave-over-wave 2025↔2026 + cualitativo integrado)
status: PLAN — pendiente ejecución por specialists (bloqueada por hallazgo arquitectónico, ver task-log 2026-05-17)
v3_anterior: ENTREGADO 2026-05-17 (deck V3 46 slides + Resumen Ejecutivo V3 7 slides), commit `c1fe4e6`
contexto: |
  Owner asumió que Cora compartió nueva ola de campo "Notoriedad V2.0".
  Diagnóstico Tier 1 reveló:
  - BBDD V2.0 = idéntica a V1 (402×295, mismo archivo, NO nueva ola).
  - Material nuevo real: BBDD 2025 raw (n=785, 444 cols) + 10 docs cualitativos Gama (~42k chars).
  - Guía con preguntas marcadas rojo/negro indica comparabilidad inter-ola (negro=2025+2026, rojo=2026 only).
  - Draft V4 email a Cora (commit `235ee66`) preguntó A/B; Cora respondió en hechos compartiendo
    BBDD raw 2025 + cualitativo (eligió A ampliado: wave-over-wave + cuali integration).
  Trabajo legítimo para V4:
  - Capa wave-over-wave 2025↔2026 robusta sobre los 24 ítems comparables.
  - Análisis cualitativo profundo sobre los 10 docs.
  - Triangulación cuali-cuanti que el V3 no pudo hacer (verbatims eran limitados, E-1 quedó parcial).
  - Deck V4 integrador (NO V3-bis: integra V3 base + capa WoW + capa cuali).
inputs_disponibles:
  - BBDD 2026: G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\BBDD Notoriedad 2026.xlsx (402×295, idéntica a V1)
  - BBDD 2025 raw: G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\Notoriedad 2025.xlsx (785×444 cols, hoja "NotoriedadVF2V23_SPSS2")
  - Guía preguntas 2026 con marcado rojo: G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\GUIA DE PREGUNTAS NOTORIEDAD 2026.docx
  - Cuestionario 2025 papel: G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\Cuestionario en papel Notoriedad_2025.xls
  - Cualitativo Gama (10 archivos en subcarpeta Cualitativo Gama\): 6 resúmenes de sesiones + 4 verbatims raw + 1 resumen App Gama. Total ~42k chars
artefactos_v3_reutilizables:
  - 00-brief/methos/ME-1, ME-3, ME-4 (research design, methodology rationale, vigilance Q2 2026)
  - 02-analysis/cuanti/CU-1..CU-6 v2 (reconciliation, stat-pack, drivers RF+SHAP, segmentation k-means, pricing, caveats)
  - 02-analysis/cuanti/scripts/00_cuanti_master.py + 04_drivers_rf_shap.py + 05_segmentation_kmeans_lca.py + utils.py
  - 02-analysis/sinta/IN-1..IN-6 (verbatim coding limited, thematic, framework mapping, triangulation, Minto pyramid, caveats)
  - 03-deck/V3/deck V3 46 slides + Resumen Ejecutivo V3 7 slides + outlines VI-1a/VI-1b
salida_destino: G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\02_De_Raoul_Para_Cora\Notoriedad V2.0\ (carpeta ya creada)
trabajo_intermedio:
  - 02-analysis/methos/v2/ (creada)
  - 02-analysis/cuanti/v2-wow/ (creada)
  - 02-analysis/sinta/v2/ (creada)
  - 03-deck/V4/ (creada)
---

# Plan ola V4 — Briefs autocontenidos para specialists

Este documento contiene los briefs de invocación listos para cada specialist
de la cadena V4. Cada brief es **autocontenido** (specialist no necesita
contexto adicional fuera de leer los inputs señalados). Cuando la limitación
arquitectónica del Raul-subagent se resuelva (ver `feedback_raul_subagent_no_nested_delegation.md`),
la próxima invocación con tool Agent disponible debe ejecutar estos briefs en
el orden indicado.

---

## OLA 1 — Methos (ME-5 methodology plan V4)

**Objetivo:** definir la metodología formal de la capa V4 (wave-over-wave + cualitativo integrado), construyendo encima de ME-1/ME-3/ME-4 ya existentes. NO duplicar trabajo anterior.

**Output canónico:** ME-5 — Methodology Plan for V4 Layer (Wave-over-Wave + Qualitative Integration)

**Brief de invocación a Methos:**

```
Eres Methos. Lee primero tu SSOT en C:\rAUL\04-system\02-agents\conceptual\methos.md.

CONTEXTO: V3 del estudio Notoriedad Gama 2026 ya fue entregado a Cora el 2026-05-17 (deck 46 slides + Resumen Ejecutivo 7 slides, commit `c1fe4e6`). Cora compartió ahora material adicional que permite construir una capa V4: BBDD 2025 raw (n=785) + 10 docs de cualitativo Gama (~42k chars). Tu trabajo previo en este proyecto:
- ME-1 (research design retroactivo): C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\00-brief\methos\2026-05-17_ME-1_research-design-retroactivo_v1.md
- ME-3 (methodology rationale): mismo path, ME-3
- ME-4 (vigilance Q2 2026): mismo path, ME-4
LEELOS ANTES de empezar para no duplicar.

TAREA: Escribir ME-5 — Methodology Plan for V4 Layer. Cubre:
1. Marco: qué agrega V4 sobre V3 (wave-over-wave + cuali profundo + triangulación). Qué NO toca (V3 base se preserva).
2. Wave-over-wave 2025↔2026:
   - Mapping de ítems comparables (24 negros) entre BBDDs (2025 tiene P22 con 20 atributos vs 2026 con 10; P23 cross-marca con distinto orden de marcas — hay reconciliación a hacer).
   - Tests estadísticos: z-test de diferencia de proporciones por ítem, controlado por NSE C+/C y D/E donde n permita. Eficiencia: especifica corrección por comparaciones múltiples (Bonferroni o BH).
   - Decisión sobre ponderación 2025: la BBDD 2025 tiene @PONDERAR_1 — ¿se usa ponderada o no, y con qué efecto en SE?
   - Test de comparabilidad de muestra (NSE × geo × edad × género 2025 vs 2026) ANTES de comparar variables sustantivas.
3. Análisis cualitativo:
   - 10 docs de cualitativo: 6 resúmenes (sesiones focus groups Gama, segmentos 18-30 ocasionales/frecuentes, 31-50 ocasionales/frecuentes, 50+ ocasionales/frecuentes) + 4 verbatims raw paralelos.
   - Diseño analítico: análisis temático Braun & Clarke (deductivo desde framework V3 + inductivo emergente).
   - Protocolo de codificación: niveles 1 (codes), 2 (themes), 3 (overarching narratives). Sin Kappa inter-rater (analista único), documentar limitación.
4. Triangulación cuali-cuanti V4:
   - Mecanismo "atención = reconocimiento personal" (hipótesis V3 IN-5): ¿lo confirman los verbatims raw?
   - 3 segmentos k-means V3 (Mayoría Exigente / Pragmáticos Convertibles / Núcleo Leal): ¿narrativa cualitativa los valida o los rompe?
   - Barreras de compra que cuanti no captura (objections, sticky perceptions sobre Gama).
5. Plan de claims V4: qué claims son defendibles con qué evidencia (3 tipos: WoW confirmados, cuali corroborated, hipótesis aún sin cerrar).
6. Decisiones críticas que Methos requiere del Owner antes de Cuanti/Sinta ejecuten:
   - Ponderación 2025 sí/no.
   - Threshold de significancia y corrección comparaciones múltiples.
   - Si la triangulación contradice un claim V3, ¿se ajusta deck V4 o se preserva V3 + nota de honestidad?

ENTREGA: texto Markdown completo de ME-5 v1. Raul lo escribe al archivo. No escribas archivos tú; devuelve el contenido como texto.

PATHS:
- ME-1/3/4 previos: C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\00-brief\methos\
- BBDD 2026: G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\BBDD Notoriedad 2026.xlsx
- BBDD 2025: G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\Notoriedad 2025.xlsx
- Guía con rojos: G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\GUIA DE PREGUNTAS NOTORIEDAD 2026.docx
- Cualitativo: G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\Cualitativo Gama\
- Reflexiones-2027 (insumo): C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\99-comms\2026-05-16_Reflexiones-para-ola-2027.md
- V3 deck README: C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\03-deck\V3\README-V3-orden-de-lectura.md

CRITERIO: ME-5 debe ser ejecutable. Cuanti y Sinta lo leerán DIRECTAMENTE como input. No teoría — plan de análisis con decisiones tomadas (o explícitamente diferidas al Owner con razón).
```

**Destino archivo:** `C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\00-brief\methos\v2\2026-05-XX_ME-5_methodology-plan-V4_v1.md`

---

## OLA 2 — Cuanti (CU-7 wave-over-wave 2025↔2026)

**Depende de:** ME-5 (Methos define mapping y método).

**Output canónico:** CU-7 — Wave-over-Wave 2025↔2026 Findings + JSONs estructurados + plots.

**Brief de invocación a Cuanti:**

```
Eres Cuanti. Lee primero tu SSOT en C:\rAUL\04-system\02-agents\conceptual\cuanti.md.

CONTEXTO: Construyendo capa V4 sobre el deck V3 ya entregado. Tu trabajo previo en este proyecto:
- CU-1 reconciliation, CU-2 stat-pack, CU-3 RF+SHAP, CU-4 k-means, CU-5 pricing, CU-6 caveats: en
  C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis\cuanti\
- Scripts existentes en .\cuanti\scripts\ (utils.py para carga estandarizada de BBDD 2026).
LEE ME-5 de Methos PRIMERO (C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\00-brief\methos\v2\2026-05-XX_ME-5_methodology-plan-V4_v1.md).

TAREA: Ejecutar el análisis wave-over-wave 2025↔2026 sobre los ítems comparables.

PASO 1 — Inventario y mapping:
- BBDD 2026 (n=402, 295 cols): paths en ME-5.
- BBDD 2025 (n=785, 444 cols, hoja "NotoriedadVF2V23_SPSS2"): paths en ME-5.
- Variables 2025 son código corto (P16_1, P17O_X, P22_1..P22_20, P23_X_Y, P24, P31_1..P31_6, P32_1..P32_6, etc.); 2026 son texto largo con código embebido entre llaves.
- Crear `cuanti/v2-wow/mapping_2025_2026.csv` con todas las correspondencias declaradas.
- Identificar ítems donde 2025 tenía MÁS opciones que 2026 (P22 20→10 atributos, P23 20→10 marcas): documentar qué se compara (intersección) y qué se descarta.

PASO 2 — Comparabilidad muestral:
- Distribución NSE 2025 vs 2026 (chi-cuadrado de homogeneidad).
- Distribución Municipio/Parroquia 2025 vs 2026 (mismo test).
- Edad y género (mismo test).
- Reportar SI las muestras son comparables o NO; si no, qué post-stratification aplica.
- Decidir según ME-5: ponderar 2025 con @PONDERAR_1 sí/no.

PASO 3 — Wave-over-Wave por ítem:
Para cada uno de los 24 ítems comparables (al menos: P16 TOM, P17 asistida, P19 consideración, P20 compra 3m, P21 preferida, P22 importancia atributos, P23 asociación, P24 última compra, P26 misiones, P30 habitual; demográficas):
- % 2025 vs % 2026 (total + por NSE C+/C y D/E donde n permita).
- z-test de diferencia de proporciones (Newcombe-Wilson preferible para muestras moderadas).
- p-value + magnitud de cambio (pp) + IC 95% del delta.
- Corrección Bonferroni o BH según ME-5.
- Flag de comparabilidad si tras post-stratification el delta cambia >2 pp.

PASO 4 — Outputs:
- `cuanti/v2-wow/CU-7_wave-over-wave_v1.md`: documento Markdown con metodología aplicada + tablas + interpretación + 6-10 hallazgos principales con dirección de cambio + magnitud.
- `cuanti/v2-wow/outputs/json/CU7_wow_results_20260517_v1.json`: estructura por ítem (estimate_2025, estimate_2026, delta_pp, p_value, sig_flag, ci_95_low, ci_95_high, n_2025, n_2026).
- `cuanti/v2-wow/plots/wow_top_changes_20260517_v1.png`: forest plot de los top deltas significativos.
- Documentar limitaciones EN EL DOCUMENTO (sample bias, p-value inflation, etc.).

PASO 5 — Caveats para Bruna:
- CU-7-caveats: lista explícita de claims con nivel de evidencia (alto/medio/bajo) listo para gate Bruna.

ENTREGA: texto Markdown del CU-7 + opcionalmente código Python en bloque (Raul lo materializa).
```

**Destino archivos:** `C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis\cuanti\v2-wow\`

---

## OLA 3 — Sinta (IN-7 cualitativo profundo + IN-8 triangulación V4)

**Depende de:** ME-5 (Methos define protocolo cuali) + CU-7 (Cuanti aporta findings WoW para triangulación).

**Output canónico:** IN-7 Qualitative Deep + IN-8 Triangulation V4

**Brief de invocación a Sinta:**

```
Eres Sinta. Lee primero tu SSOT en C:\rAUL\04-system\02-agents\conceptual\sinta.md.

CONTEXTO: V3 ya entregado con IN-1..IN-6 trabajando con verbatims muy limitados (E-1 del V3, parcialmente cubierta). Ahora tienes acceso a 10 docs de cualitativo Gama (~42k chars) que NO tuvimos en V3.

LEE PRIMERO:
- ME-5 (Methos plan V4): C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\00-brief\methos\v2\2026-05-XX_ME-5_methodology-plan-V4_v1.md
- CU-7 wave-over-wave (Cuanti): C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis\cuanti\v2-wow\CU-7_wave-over-wave_v1.md
- IN-1..IN-6 V3 previos: C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis\sinta\
- Reflexiones-2027 (insumo): C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\99-comms\2026-05-16_Reflexiones-para-ola-2027.md

INPUTS NUEVOS DE CUALITATIVO (G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\Cualitativo Gama\):
- 6 resúmenes de sesiones FG (segmentos 18-30 / 31-50 / 50+ × ocasionales/frecuentes)
- 4 verbatims raw paralelos (sesiones online 4, 5, 6, adicional)
- 1 resumen sesiones cualitativas App Gama (~10k chars)

TAREA 1 — IN-7 Análisis cualitativo profundo:
- Codificación deductiva-inductiva (Braun & Clarke 2006):
  - Códigos deductivos partiendo del framework V3 (drivers atención/limpieza/promociones; barreras precio/surtido/cobertura; segmentos).
  - Códigos inductivos emergentes (lo que NO esperabas).
- Frecuencias por código × segmento (ocasional vs frecuente; jóvenes vs medianos vs mayores).
- Temas (nivel 2): agrupar códigos en 4-6 temas con evidencia citada.
- Narrativas overarching (nivel 3): 2-3 hilos narrativos transversales.
- Output: `sinta/v2/IN-7_cualitativo-profundo_v1.md` con metodología + códigos + frecuencias + verbatims ilustrativos + 6-8 hallazgos cualitativos clave.

TAREA 2 — IN-8 Triangulación V4 cuali-cuanti:
- Para cada hallazgo cuanti V3 + CU-7 WoW, evaluar si el cualitativo:
  - (A) CONFIRMA (mismo mecanismo, misma dirección)
  - (B) AMPLIFICA (más rico, agrega capa)
  - (C) MATIZA (parcialmente válido, condicional)
  - (D) CONTRADICE (datos divergentes — claim cuanti requiere reformulación)
- Hipótesis V3 "atención = reconocimiento personal" (IN-5): ¿los verbatims raw la sustentan?
- 3 segmentos k-means V3: ¿narrativa cualitativa los valida o sugiere otra estructura?
- Barreras de compra emergentes en cuali que cuanti no detectó: enuméralas como hallazgos nuevos V4.
- Output: `sinta/v2/IN-8_triangulacion-V4_v1.md` con tabla de hallazgos × estado (A/B/C/D) + 4-6 hallazgos V4 puramente nuevos (que ni V3 ni CU-7 tenían).

CRITERIO: Citar verbatims literales en español venezolano (no parafrasear). Mantener voz del informante. Marcar claramente cuando un hallazgo viene de App Gama (B2B distinto al supermercado físico).

ENTREGA: texto Markdown de IN-7 e IN-8.
```

**Destino archivos:** `C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis\sinta\v2\`

---

## OLA 4 — Vivienne (deck V4 con SEPARACIÓN VI-1 / VI-2)

**Depende de:** CU-7 + IN-7 + IN-8.

**Output canónico:** VI-1a outline deck V4 (Markdown) y VI-1b outline Resumen V4 (Markdown), luego VI-2 render deck V4 .pptx y Resumen V4 .pptx — en **invocaciones SEPARADAS**.

**Memoria crítica aplicable:** `feedback_vivienne_token_explosion_pattern_v1.md`. Vivienne explota límite output API en decks >40 slides cuando se pide outline + .pptx en una sola invocación. **NO PEDIR AMBOS EN UN MISMO CALL.**

### Sub-ola 4.1 — VI-1 outlines (Markdown only)

**Brief Vivienne 4.1:**

```
Eres Vivienne. Lee primero tu SSOT en C:\rAUL\04-system\02-agents\conceptual\vivienne.md.

CONTEXTO: V4 del estudio Notoriedad Gama 2026. V3 ya entregado (deck 46 slides + Resumen 7). V4 integra V3 base + capa wave-over-wave + capa cualitativa profunda.

LEE PRIMERO:
- V3 outlines previos: C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\03-deck\V3\VI-1a_OUTLINE-DECK-V3.md + VI-1b_OUTLINE-RESUMEN-EJECUTIVO-V3.md
- CU-7 WoW: C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis\cuanti\v2-wow\CU-7_wave-over-wave_v1.md
- IN-7 cuali: C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis\sinta\v2\IN-7_cualitativo-profundo_v1.md
- IN-8 triangulación V4: C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis\sinta\v2\IN-8_triangulacion-V4_v1.md

TAREA: SOLO outlines en Markdown. NO generar .pptx en este call.

- VI-1a: outline deck V4 (~50 slides; integra V3 base + 1 sección WoW de 6-8 slides + 1 sección cuali de 4-6 slides + ajustes en cierre). Para cada slide: título, bullets/visuales clave, fuente (V3/CU-7/IN-7/IN-8), caveat si aplica.
- VI-1b: outline Resumen V4 (~8 slides; arranque hilo conductor + 3 hallazgos principales V4 + recomendaciones priorizadas con badge "validado WoW" o "cuali confirmado").

ENTREGA: 2 textos Markdown (VI-1a y VI-1b). NO render .pptx. NO bloques de código python-pptx.
```

**Destino:** `C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\03-deck\V4\VI-1a_OUTLINE-DECK-V4.md` y `VI-1b_OUTLINE-RESUMEN-EJECUTIVO-V4.md`

### Sub-ola 4.2 — VI-2 deck V4 render (.pptx)

**Brief Vivienne 4.2 (invocación distinta tras revisar VI-1a):**

```
Eres Vivienne. Lee primero tu SSOT.

LEE VI-1a aprobado: C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\03-deck\V4\VI-1a_OUTLINE-DECK-V4.md

TAREA ÚNICA: Generar el script python-pptx que renderiza el deck V4 conforme al outline.

- Heredar estilo visual del deck V3 (paleta, layouts, tipografía). Referenciar deck V3 .pptx para diff visual.
- Output: bloque de código python que Raul ejecuta para generar el .pptx.
- Path destino: C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\03-deck\V4\2026-05-XX_Notoriedad-Gama-2026_V4.pptx
- NO escribas outline aquí. Si necesitas refrescar el contenido, RELEELO de VI-1a; no lo rescribas.

CRITERIO: ÚNICAMENTE el código python-pptx. Una palabra final tipo "DONE" tras el bloque.
```

### Sub-ola 4.3 — VI-3 Resumen Ejecutivo render (.pptx)

**Brief Vivienne 4.3 (invocación separada tras VI-1b aprobado):**

Mismo patrón que 4.2 pero para el Resumen Ejecutivo (8 slides).

---

## OLA 5 — Bruna (gate claims V4)

**Depende de:** CU-7 + IN-7 + IN-8 + VI-1a outline V4 (no espera al .pptx render).

**Output canónico:** BR-2 V4 gate review.

**Brief de invocación a Bruna:**

```
Eres Bruna. Lee primero tu SSOT en C:\rAUL\04-system\02-agents\conceptual\bruna.md.

CONTEXTO: Capa V4 del estudio Notoriedad Gama 2026. V3 ya pasó tu gate BR-2 el 2026-05-17 (commit `c1fe4e6`). V4 agrega capa wave-over-wave + cualitativa.

LEE PRIMERO:
- BR-2 V3 anterior (precedente de criterios aplicados): buscar en C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\ por "BR-2" o "bruna gate".
- CU-7 caveats: en CU-7_wave-over-wave_v1.md sección "Caveats para Bruna".
- IN-8 triangulación V4: hallazgos clasificados A/B/C/D.
- VI-1a outline deck V4: claims por slide.

TAREA: Gate claim-by-claim. Para cada claim del deck V4 outline:
- ¿La evidencia (CU-7 + IN-8 + V3 base) soporta el nivel de afirmación?
- ¿Caveats explícitos donde EPV bajo, n pequeño, comparabilidad no validada, hallazgo cuali single-source?
- ¿Algún claim contradice o tensiona claim V3 ya entregado? Si sí, ¿reformulación V4 o nota de honestidad explícita?

ENTREGA: BR-2 V4 review con (a) APROBADOS, (b) APROBADOS con ajuste de wording, (c) BLOQUEADOS con razón. Incluir wording sugerido para los ajustes (b).
```

**Destino:** `C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\_governance\2026-05-XX_genteca-V4_claim-approval-log.md`

---

## OLA 6 — Drop a Drive Cora OUTBOX

**Output:** Raul (cuando Vivienne + Bruna terminen) copia los entregables finales a `G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\02_De_Raoul_Para_Cora\Notoriedad V2.0\` + escribe `README-V4-orden-de-lectura.md` + crea draft email Gmail.

**Entregables finales esperados en Drive OUTBOX:**
- `2026-05-XX_Notoriedad-Gama-2026_V4.pptx`
- `2026-05-XX_Notoriedad-Gama-2026_Resumen-Ejecutivo-V4.pptx`
- `README-V4-orden-de-lectura.md`
- (Opcional) `2026-05-XX_DOC-TECNICO-V4-wave-over-wave-y-cuali.docx` si Cuanti/Sinta producen un anexo técnico.

**Memoria aplicable:** `feedback_drive_path_explicit_in_email_body.md` (embebir ruta Drive desde perspectiva del receptor).

---

## Decisiones Owner requeridas antes de arrancar ejecución

1. **Resolver bloqueo Raul-subagent nested delegation** (ver `feedback_raul_subagent_no_nested_delegation.md`). Elegir patrón remediación.
2. **Confirmar scope V4** vs solo enviar nota de alcance (alternativa B del draft V4 email). Mi recomendación: V4 completa porque Cora ya compartió el material en hechos.
3. **Decisión política V3 vs V4:** ¿se entrega V4 como reemplazo del V3 o como capa complementaria? Mi recomendación: capa complementaria (V3 sigue siendo "deck principal", V4 es "anexo analítico ampliado wave-over-wave + cualitativo"). Esto preserva la inversión narrativa V3 y minimiza el costo de aprendizaje para Gama.

---

*Plan preparado por Raul-subagent (Opus 4.7) el 2026-05-17. Pendiente ejecución por specialists tras resolución del bloqueo arquitectónico.*
