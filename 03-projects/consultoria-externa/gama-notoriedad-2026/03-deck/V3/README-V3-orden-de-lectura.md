# V3 — Notoriedad Gama 2026 · Capa Analítica Ampliada

**Fecha:** 2026-05-17
**Para:** Cora Urrea
**De:** Raoul Bermudez
**Confidencial · NDA**

---

## Qué es esto y qué NO es

El **V3** es una **capa analítica ampliada** sobre el estudio Notoriedad Gama 2026.

**NO reemplaza** el V2 que recibiste el 2026-05-16. El V2 sigue siendo el documento principal. El V3 es un complemento que **suma rigor metodológico, reanálisis estadístico y síntesis cualitativa estructurada** sobre el mismo dataset.

**Por qué hay un V3:** trabajamos en paralelo con tres especialistas adicionales (Methos para diseño metodológico, Cuanti para reanálisis estadístico riguroso con RF+SHAP+k-means, Sinta para síntesis cualitativa y pirámide Minto). El resultado es una capa que eleva el techo del análisis sin contradecir nada del V2.

---

## Qué tiene de NUEVO el V3 vs el V2

| Aspecto | V2 (2026-05-16) | V3 (2026-05-17) |
|---|---|---|
| Modelos drivers | Logit | Logit + Random Forest + SHAP + Gini (convergencia) |
| Segmentación | Banners cruzados | K-means formal k=3 (silhouette + BIC validados) |
| Síntesis cualitativa | Frecuencias de respuestas | Análisis temático (Braun & Clarke) + triangulación + pirámide Minto |
| Caveats | Por bloque | Por claim individual + gate de governance interna |
| Tesis | 10 recomendaciones | 4 argumentos MECE + 5 recomendaciones priorizadas |

**Convergencia:** los 3 drivers que identificaste en V2 (atención, limpieza, promociones) están **confirmados** en V3 por 4 métodos independientes. Ninguna recomendación V3 contradice una V2; las refinan, integran o extienden.

**Lo NUEVO en V3 sin precedente en V2:**
1. **Limpieza/orden** sube de "tendencia borderline" a **driver secundario confirmado** (SHAP+Gini lo validan donde el logit quedaba en p=0.061)
2. **3 segmentos k-means formales** (no por NSE): Mayoría Exigente (59%), Pragmaticos Convertibles (33%), Nucleo Leal (8%) — el seg_2 es la oportunidad de conversión de corto plazo
3. **Mecanismo cualitativo de la preferencia**: el análisis temático sugiere que la atención opera como reconocimiento personal (hipótesis), no solo como atributo funcional
4. **Tesis central reformulada como pirámide Minto**: "Gama tiene el activo más diferenciador y lo comunica en el terreno equivocado"

---

## Orden de lectura sugerido

### Si tienes 5 minutos
1. `2026-05-17_Notoriedad-Gama-2026_Resumen-Ejecutivo-V3.pptx` (7 slides)

### Si tienes 30 minutos
1. `2026-05-17_Notoriedad-Gama-2026_Resumen-Ejecutivo-V3.pptx` (7 slides) — pa entrar
2. `2026-05-17_Notoriedad-Gama-2026_V3.pptx` (46 slides) — análisis completo
   - Lee primero **Bloque 1** (tesis + 4 argumentos MECE) — slides 6 a 9
   - Después **Bloque 8** (recomendaciones priorizadas) — slides 35 a 39
   - Y luego al gusto por bloque temático

### Si quieres trazabilidad técnica completa
3. Memos detallados disponibles a pedido (CU-1..CU-6 v2 de Cuanti, IN-1..IN-6 de Sinta, ME-1/ME-3/ME-4 de Methos)

---

## Cómo presentar V3 a Gama (sugerencia)

**Nota:** el V3 contiene información nueva (especialmente los 3 segmentos k-means) que Gama no vio en el V2. Recomiendo:

1. **Recordarles primero que el V2 es la entrega principal y sigue siendo válido**. El V3 es trabajo nuestro de profundización metodológica.
2. **Presentar la tesis V3 como evolución** ("ahora podemos decir con más rigor que..."), no como ruptura.
3. **Los segmentos nuevos como oportunidad estratégica**, no como dato contradictorio.
4. El Resumen Ejecutivo (7 slides) es el formato ideal para reunión ejecutiva con Gama.

---

## Marco interpretativo

El V3 pasó por un **gate de governance interno** que revisó claim-by-claim los caveats metodológicos y aprobó con ajustes editoriales menores (formulaciones que enfatizan recomendaciones estratégicas derivadas de datos, no críticas a la creatividad o inversión actual de Gama).

**Lo que el V3 puede afirmar con alta certeza** (4 métodos convergentes):
- Atención es el driver #1 de preferencia (OR=5.73 [IC95: 1.6-20.4])
- Precio NO es driver de preferencia (OR=1.03, SHAP #10)
- Existe gap comunicacional masivo (4.2% recall espontáneo de campañas)
- 3 segmentos de mercado con perfiles distintos validados estadísticamente

**Lo que requiere validación adicional** (hipótesis derivadas):
- Mecanismo cualitativo de "reconocimiento personal" — requiere FGIs/IDIs
- Barrera de precio para el 92% no preferente — requiere Van Westendorp o auditoría in-store
- Causa del gap de surtido en El Cafetal — requiere proyecto cuali de formatos

Esto se detalla en la slide RE-6 del Resumen Ejecutivo y en cada caveat de pie de slide del deck principal.

---

## Ola 2027

El V3 incluye un **roadmap metodológico 2027** (slide 41 del deck) con 5 mejoras obligatorias de bajo costo + 2 opcionales con inversión incremental. Ya tienes el documento extenso `2026-05-16_Reflexiones-para-ola-2027.docx`; el V3 lo amplía y prioriza.

---

## Archivos en esta carpeta V3/

| Archivo | Contenido |
|---|---|
| `README-V3-orden-de-lectura.md` | Este archivo |
| `2026-05-17_Notoriedad-Gama-2026_V3.pptx` | Deck principal V3 (46 slides) |
| `2026-05-17_Notoriedad-Gama-2026_Resumen-Ejecutivo-V3.pptx` | Resumen Ejecutivo V3 (7 slides) |

---

**Cualquier duda, escribe.**

Raoul
