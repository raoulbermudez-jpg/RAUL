---
autor: Methos (Research Design & Methodology Lead)
proyecto: gama-notoriedad-2026
tipo: ME-5 Methodology Plan for V4 Layer
version: v1
fecha: 2026-05-17
status: OPERATIVO — insumo directo para Cuanti (CU-7) y Sinta (IN-7/IN-8)
dependencias_upstream: ME-1 v1, ME-3 v1, ME-4 v1 (mismo path), Plan V4 (_governance/2026-05-17_PLAN-OLA-V4_briefs-para-specialists.md)
confidencialidad: interno equipo / NO para Gama ni Cora en esta versión
---

# ME-5 — Methodology Plan for V4 Layer
## Wave-over-Wave 2025↔2026 + Qualitative Integration + Triangulation
## Notoriedad Gama 2026

**Fecha:** 2026-05-17
**Autor:** Methos
**Para:** Cuanti (ejecución CU-7), Sinta (ejecución IN-7/IN-8), Owner (decisiones marcadas)
**Propósito:** Definir el protocolo metodológico completo de la capa V4, de modo que Cuanti y Sinta puedan ejecutar directamente sin ambigüedades. Cada decisión metodológica de este memo tiene una razón explícita. Las decisiones que requieren confirmación del Owner están marcadas como **[DECISION-OWNER]** con una recomendación pre-pagada de Methos. Las decisiones que Methos toma directamente en ausencia del Owner están marcadas **[DECISION-METHOS]**.

> **Nota de encuadre:** Este documento no repite lo documentado en ME-1/ME-3/ME-4. Los specialists deben haberlos leído. Este memo asume ese background y opera sobre él.

---

## 1. Marco V4 — Qué agrega, qué preserva, qué excluye

### 1.1 Qué es V4

V4 es una **capa analítica complementaria** sobre V3 entregado el 2026-05-17. No es V3-bis. No reemplaza ni modifica el deck V3 de 46 slides ni el Resumen Ejecutivo de 7 slides.

V4 añade tres capas de evidencia que V3 no tenía:

| Capa V4 | Fuente | Agente responsable |
|---|---|---|
| Wave-over-wave 2025↔2026 (cuanti) | BBDD 2025 raw n=785 + BBDD 2026 n=402 | Cuanti (CU-7) |
| Análisis cualitativo profundo | 10 docs cualitativo Gama (~42k chars) | Sinta (IN-7) |
| Triangulación cuali-cuanti | Hallazgos V3 + CU-7 + IN-7 | Sinta (IN-8) |

**V4 produce:** (a) confirmación o revisión de claims V3 con nueva evidencia longitudinal; (b) insights cualitativos que el cuestionario cuantitativo no podía generar; (c) una tipología de claims con nivel de evidencia explícito para el deck V4.

### 1.2 Qué NO toca V4

**[DECISION-OWNER — confirmada pre-invocación, commit `00f2df8`]:** V3 se preserva como capa principal. V4 es anexo analítico complementario.

Operativamente esto significa:

- Los 4 claims de alta certeza V3 (Atención driver #1, Precio no driver, Gap comunicacional, 3 segmentos k-means) no se "reabren" desde cero en V4. Si la evidencia WoW o cuali los corrobora, se presenta como corroboración. Si los matiza, se presenta como matiz (ver protocolo §6.3).
- El deck V4 no regrabará las 46 slides V3. Añadirá una sección WoW (6-8 slides) y una sección cuali/triangulación (4-6 slides) integradas en la narrativa existente.
- Vivienne recibe esta instrucción explícita al construir VI-1a.

### 1.3 Inputs disponibles para V4

| Input | Path | Descripción |
|---|---|---|
| BBDD 2026 | `G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\BBDD Notoriedad 2026.xlsx` | n=402, 295 cols. Hoja única. Idéntica a V1. |
| BBDD 2025 | `G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\Notoriedad 2025.xlsx` | n=785, 444 cols. Hoja: `NotoriedadVF2V23_SPSS2`. Columna de ponderación: `@PONDERAR_1`. |
| Guía 2026 con rojos | `G:\...\GUIA DE PREGUNTAS NOTORIEDAD 2026.docx` | Negro = comparable 2025+2026. Rojo = 2026 only. Mapping de ítems autorizado. |
| Cuestionario 2025 papel | `G:\...\Cuestionario en papel Notoriedad_2025.xls` | Referencia de formulación exacta de preguntas 2025 para verificar comparabilidad de enunciado. |
| Cualitativo 10 docs | `G:\...\Notoriedad V2.0\Cualitativo Gama\` | Ver §4.1 para inventario detallado. |

---

## 2. Wave-over-Wave 2025↔2026 — Protocolo completo para Cuanti

### 2.1 Paso 0: Pre-requisito — Verificar formulación exacta de ítems comparables

**Antes de cualquier comparación cuantitativa**, Cuanti debe:

1. Leer el cuestionario 2025 (`Cuestionario en papel Notoriedad_2025.xls`) y extraer el enunciado exacto de cada pregunta marcada en negro en la Guía 2026.
2. Comparar enunciado 2025 vs enunciado 2026 ítem por ítem.
3. Producir una columna `enunciado_identico` (sí/no) en el mapping CSV.

**[DECISION-METHOS]:** Si el enunciado difiere en algún elemento sustantivo (no solo puntuación o format), ese ítem se marca como `comparable_con_caveat` y se incluye en el análisis con nota explícita de la diferencia. No se excluye automáticamente — la exclusión haría invisible la comparación completa — pero se presenta con caveat de nivel medio de comparabilidad.

**Razón:** cambios menores de formulación producen drift de respuesta documentado en literatura (Tourangeau et al., *The Psychology of Survey Response*, 2000, §5.3). El caveat protege al receptor sin eliminar la información.

### 2.2 Paso 1: Mapping de ítems comparables (output: `mapping_2025_2026.csv`)

Cuanti construye el archivo CSV con las siguientes columnas:

```
pregunta_id_2025 | nombre_columna_2025 | pregunta_id_2026 | nombre_columna_2026 |
tipo_variable | marcado_guia | enunciado_identico | n_opciones_2025 | n_opciones_2026 |
estrategia_reconciliacion | notas
```

**Estrategias de reconciliación por tipo de problema:**

**Caso A — P22: Importancia de atributos (20 atributos en 2025 → 10 en 2026)**

La Guía 2026 marca en negro los 10 atributos que se mantuvieron. La comparación inter-ola se hace **únicamente sobre esa intersección de 10 atributos**.

Los 10 atributos eliminados en 2026 no se comparan. Si la Guía marca alguno de los 10 eliminados como negro (caso hipotético de discrepancia), escalar al Owner antes de proceder.

Estrategia de reporte: tabla 10×2 (atributos × ola) con T2B Likert en ambas olas. Nota explícita: "Los 10 atributos reportados son el subconjunto comparable. Los 10 atributos adicionales 2025 no tienen par en 2026."

**Caso B — P23: Asociación marca×atributo (distinto orden de marcas entre olas)**

El número de marcas puede diferir entre olas (nuevas marcas añadidas o eliminadas en 2026 vs 2025). Protocolo:

1. Identificar el listado de marcas en 2025 y en 2026.
2. Intersección: marcas presentes en **ambas olas** = marcas comparables.
3. Unión menos intersección: marcas solo en una ola = reportar descriptivamente para esa ola, no en tabla comparativa.
4. El orden de presentación de atributos en P23 puede diferir entre olas. La variable comparada es la asociación de cada marca×atributo (binaria), no el orden. El orden es irrelevante para la comparación estadística si las variables están correctamente mapeadas por nombre.

**[DECISION-METHOS]:** Si Cuanti detecta que alguna marca fue formulada de manera diferente (ej. "Supermercado Plan Suárez" en 2025 vs "Plan Suárez" en 2026), se tratan como la misma marca previa verificación con la Guía. Documentar en columna `notas` del mapping.

**Caso C — Variables de embudo (P16 TOM, P17 asistida, P19 consideración, P20 compra 3m, P21 preferida)**

Estas preguntas son de respuesta abierta o multi-select de marcas. La comparación se hace a nivel de **proporción de menciones de cada marca** (ej. % que menciona Gama en TOM), que es invariante al orden de la lista. No hay problema de reconciliación si las marcas están correctamente mapeadas.

**Caso D — Variables de precio (P31 ranking, P32 mejor precio por categoría)**

P31 en 2025 puede tener distinto número de marcas o distinto enunciado de opciones. Verificar. Si el número de marcas difiere, el ranking relativo (mean rank) no es directamente comparable — en ese caso reportar solo la posición relativa de Gama dentro del campo disponible en cada ola, con nota de la diferencia en la base de marcas.

P32 por categoría: comparar solo las categorías presentes en ambas olas con el mismo enunciado.

**Caso E — Demográficas y cuotas (NSE, geo, edad, género)**

Estas variables se usan en el Paso 2 (comparabilidad muestral), no en el análisis sustantivo WoW. Ver §2.3.

### 2.3 Paso 2: Test de comparabilidad muestral — OBLIGATORIO antes de sustantivo

**Razón metodológica:** comparar proporciones sustantivas entre olas asume que las muestras son suficientemente similares en composición. Si la muestra 2025 tiene sustancialmente más NSE D/E que la 2026, o cubre más zonas geográficas, las diferencias observadas en, por ejemplo, preferencia de marca pueden reflejar diferencias de composición, no cambios reales de mercado. (Groves et al., *Survey Methodology*, 2nd ed., 2009, §2.5; Cochran, *Sampling Techniques*, 3rd ed., 1977, §5A).

**Tests requeridos:**

| Dimensión | Test | Hipótesis nula | Criterio |
|---|---|---|---|
| NSE (3-4 categorías: C+/C, D, E, otro) | Chi-cuadrado de homogeneidad | Las distribuciones NSE 2025 y 2026 son iguales | p > 0.10 = muestras comparables; p ≤ 0.10 = diferencia relevante |
| Municipio/Parroquia (las presentes en ambas olas) | Chi-cuadrado de homogeneidad | Distribuciones geográficas iguales | Ídem |
| Género (M/F/otro) | Chi-cuadrado de homogeneidad | Distribuciones de género iguales | Ídem |
| Edad (agrupada en 3-4 rangos: 18-30 / 31-50 / 51+) | Chi-cuadrado de homogeneidad | Distribuciones de edad iguales | Ídem |

**[DECISION-METHOS]:** Se usa α = 0.10 (no 0.05) para el test de homogeneidad muestral. Razón: el objetivo del test es detectar desequilibrios que ameriten post-stratification. Con α = 0.05 se corre el riesgo de NO detectar desequilibrios moderados que sí son metodológicamente relevantes (error tipo II costoso). En la literatura de survey methodology, el umbral p < 0.10 para tests auxiliares de calidad de datos es la práctica estándar. (Groves et al., 2009, §2.7).

**Interpretación de resultados:**

- Si **todas** las variables demográficas pasan el test (p > 0.10): las muestras son comparables. Proceder al análisis WoW sin post-stratification.
- Si **alguna** variable falla (p ≤ 0.10): reportar cuál y en qué dirección (ej. "2025 tiene sobre-representación de NSE E vs 2026"). Aplicar post-stratification limitada (ver §2.4). No bloquear el análisis — documentar y continuar con caveats.
- Si **múltiples variables** fallan simultáneamente: el comparativo inter-ola tiene riesgo de sesgo de composición moderado-alto. Presentar resultados con caveat explícito de nivel ALTO en la tabla WoW y en el gate de Bruna.

### 2.4 Ponderación de BBDD 2025 — Decisión con razón

La BBDD 2025 tiene la columna `@PONDERAR_1`.

**[DECISION-METHOS: Usar ponderación 2025 — sí.]**

**Razón:**

La existencia de una columna de ponderación en la BBDD 2025 indica que quien produjo esa BBDD ya determinó que la muestra raw no era auto-ponderada (o no era representativa del universo objetivo sin ajuste). Usar los datos sin ponderar cuando existe un factor de ponderación producido por el equipo de fieldwork equivale a ignorar la corrección de diseño muestral que el propio proveedor consideró necesaria.

**Efecto en errores estándar (SE):** la ponderación ajusta los estimados puntuales (medias, proporciones) pero generalmente aumenta los SE comparado con los datos sin ponderar (design effect ≥ 1.0). Esto es correcto y esperado — los SE ponderados reflejan mejor la incertidumbre real del estimado para el universo objetivo.

**Qué debe hacer Cuanti:**

1. Verificar que `@PONDERAR_1` es un factor de expansión (valor ~1.0 promedio, rango típico 0.3-3.0) y no un flag binario. Si es flag binario, escalar antes de aplicar.
2. Aplicar la ponderación en todos los análisis de 2025 (frecuencias, proporciones, tests estadísticos) usando el módulo de diseño muestral de `statsmodels` o `survey` equivalente (con `weights=` en las funciones pertinentes).
3. Reportar n sin ponderar (para efectos de grados de libertad y SE) y estimado ponderado (para la proporción reportada). Formato: "42.3% (n_efectivo = 718)".
4. Calcular el **design effect (DEFF)** promedio de las variables clave: DEFF = Var(ponderado) / Var(sin ponderar). Si DEFF > 2.0 en alguna variable clave, reportarlo como caveat (la ponderación infló sustancialmente la incertidumbre en esa variable).

**Excepción:** si al verificar la columna `@PONDERAR_1` Cuanti detecta que todos los valores son 1.0 (sin variación), entonces la ponderación es trivial (no hay ajuste). Documentarlo y proceder sin ajuste, reportando que el diseño muestral 2025 es auto-ponderado.

### 2.5 Paso 3: Tests estadísticos wave-over-wave

**Test base: Newcombe-Wilson para diferencia de dos proporciones independientes**

**[DECISION-METHOS: Newcombe-Wilson, no z-test clásico.]**

**Razón:** el z-test de diferencia de proporciones estándar (basado en distribución normal asintótica) tiene cobertura nominal correcta solo cuando ambas proporciones están alejadas de los extremos (0 y 1) y los n son suficientemente grandes. Para proporciones pequeñas (p < 0.10, frecuentes en este estudio — TOM de marcas menores, subgrupos geográficos) o proporciones grandes (p > 0.90), el intervalo de confianza clásico puede tener cobertura deficiente (Newcombe, 1998, *Statistics in Medicine*, 17(8), 857-872). El método Newcombe-Wilson (intervalo de confianza basado en la inversión del test de Wilson para cada proporción individual) produce IC con cobertura más cercana al nominal en todo el rango de proporciones. Es computacionalmente trivial en Python con `statsmodels` (`proportion_confint` método `wilson`).

**Formato de output por ítem comparado:**

```
{
  "variable_id": "P21_gama",
  "label": "Preferencia Gama (total muestra)",
  "estimate_2025": 0.082,
  "n_2025": 785,
  "estimate_2026": 0.080,
  "n_2026": 402,
  "delta_pp": -0.2,
  "ci_95_low_delta": -4.1,
  "ci_95_high_delta": 3.7,
  "p_value": 0.912,
  "sig_flag": "no_sig",
  "method": "Newcombe-Wilson",
  "weighted_2025": true,
  "comparability_caveat": null
}
```

**Niveles de significancia reportados:**

| p-value | Etiqueta | Símbolo en tabla |
|---|---|---|
| < 0.01 | Significativo 99% | ↑↑ / ↓↓ |
| 0.01–0.05 | Significativo 95% | ↑ / ↓ |
| 0.05–0.10 | Tendencia 90% | ↑° / ↓° |
| > 0.10 | No significativo | ≈ |

**[DECISION-METHOS]:** Se reportan los 4 niveles (incluyendo tendencia 90%) para no perder información con muestras moderadas. El receptor (Cora, Gama) puede tomar sus propias decisiones sobre qué niveles considera accionables. La transparencia sobre el nivel de evidencia es preferible a colapsar todo en 0.05 binario. (Wasserstein et al., *The American Statistician*, 2019, 73(S1) — ver también ME-4 §3 Alerta 4).

### 2.6 Corrección por comparaciones múltiples

**Número de comparaciones:** el análisis WoW incluirá aproximadamente 24-40 ítems comparables (embudo × marcas principales + atributos × marcas en intersección + precio + misiones). Esto genera un problema de inflación de error tipo I (con 40 tests al α=0.05, se esperan ~2 falsos positivos por azar solo).

**[DECISION-METHOS: Benjamini-Hochberg (BH), no Bonferroni.]**

**Razón:** Bonferroni controla el Family-Wise Error Rate (FWER) — la probabilidad de cometer aunque sea un error tipo I en toda la familia de tests. Es apropiado cuando todos los tests son independientes y cualquier falso positivo tiene consecuencias graves. En este contexto, los tests son correlacionados (ítems del mismo embudo correlacionan fuertemente entre olas), y el costo de los falsos negativos (declarar "sin cambio" cuando hay cambio real) también es importante estratégicamente.

Benjamini-Hochberg controla la False Discovery Rate (FDR) — la proporción esperada de falsos positivos entre los declarados significativos — que es el criterio más apropiado para exploración de múltiples ítems en investigación de mercado. BH es más potente que Bonferroni (detecta más cambios reales) a costa de una tasa de FDR controlada (5%). (Benjamini & Hochberg, *Journal of the Royal Statistical Society B*, 1995, 57(1), 289-300).

**Implementación:** Python `statsmodels.stats.multitest.multipletests(p_values, method='fdr_bh')` devuelve p-values ajustados y flags de rechazo con BH.

**Presentación:** en la tabla de resultados WoW, incluir tanto el p-value unadjusted como el p-value BH-adjusted. El flag de significancia reportado usa el p ajustado. En nota al pie: "Corrección por comparaciones múltiples: Benjamini-Hochberg FDR q<0.05."

### 2.7 Análisis por subgrupo (NSE × geo)

El análisis por subgrupo se ejecuta **solo donde n es suficiente**.

**[DECISION-METHOS]:** Umbral mínimo de n por subgrupo-ola: n ≥ 50 en AMBAS olas para que el test sea informativo.

**Razón:** con n < 50 en alguna ola, el intervalo de confianza del delta tiene una amplitud > ±14 pp (asumiendo p=0.5, el caso más conservador, IC 95%). Ese nivel de incertidumbre hace el test poco accionable estratégicamente. Reportar proporciones descriptivas sin test formal para subgrupos con n < 50, con nota explícita.

**Subgrupos priorizados (en orden de importancia estratégica):**

1. NSE C+/C (segmento premium de interés para Gama)
2. NSE D/E combinado (segmento de volumen)
3. Municipio Baruta (mayor presencia Gama)
4. Municipio Sucre/Chacao (zonas de competencia intensa)

**Corrección múltiple en subgrupos:** los análisis de subgrupo se tratan como una familia separada de tests (exploratorios). Aplicar BH también dentro de cada subgrupo. Reportar como exploratorios: "Estos análisis de subgrupo no estaban pre-registrados en la ola 2025 y deben interpretarse como hipótesis a confirmar en ola 2027, no como conclusiones definitivas." (Wasserstein & Lazar, 2016).

### 2.8 Variables incluidas en el análisis WoW (lista maestra)

Cuanti construye el mapping CSV verificando ítem por ítem con la Guía de Preguntas. La lista a continuación es la propuesta de Methos basada en el conocimiento de ambas BBDD; Cuanti la confirma o ajusta al abrir los archivos:

**Embudo de marca (por cada marca presente en ambas olas):**
- P16: TOM (% menciona marca en espontánea)
- P17: Notoriedad asistida
- P19: Consideración
- P20: Compra últimos 3 meses
- P21: Preferida

**Asociación e importancia:**
- P22: Importancia de los 10 atributos comunes (T2B Likert — comparación descriptiva, sin test de significancia sobre la media ya que la escala es la misma estructura pero el n diferente puede producir resultados artefactuales; ver ME-3 §3)
- P23: Asociación marca×atributo (% asocia marca X con atributo Y) — solo para las marcas e intersección de atributos comunes

**Comportamiento:**
- P24: Última compra (distribución por marca)
- P26: Misiones (distribución por misión — solo las misiones presentes en ambas olas)
- P30: Supermercado habitual (distribución por marca)

**Precio:**
- P31: Mean rank y % Top-3 por marca (con nota sobre diferencias en set de marcas entre olas)
- P32: % menciona marca como "mejor precio" por categoría — solo categorías en ambas olas

**Notas de exclusión a priori:**
- Módulo publicitario (P35-P45): probablemente 2026 only. Verificar con Guía. Si es solo 2026, no se compara.
- Preguntas marcadas en rojo en la Guía: por definición, 2026 only. No comparar.

---

## 3. Análisis Cualitativo — Protocolo para Sinta

### 3.1 Inventario de materiales cualitativos

La carpeta `Cualitativo Gama\` contiene aproximadamente 10 documentos. Sinta debe inventariarlos al abrir la carpeta y clasificarlos antes de proceder. La estructura esperada según el brief V4 es:

| Tipo de doc | Cantidad esperada | Descripción |
|---|---|---|
| Resúmenes de sesión (focus groups) | 6 | Segmentos: 18-30 ocasionales / 18-30 frecuentes / 31-50 ocasionales / 31-50 frecuentes / 50+ ocasionales / 50+ frecuentes |
| Verbatims raw | 4 | Transcripciones parciales o completas de sesiones online (identificadas como sesiones 4, 5, 6, y adicional) |
| Resumen App Gama | 1 | Sesiones cualitativas sobre la aplicación de Gama — contexto B2B o digital distinto al supermercado físico |

**Si la estructura real difiere:** Sinta documenta el inventario real en IN-7 §1 y ajusta el protocolo. No asume estructura — verifica.

**Distinción crítica — App Gama:** los materiales de App Gama reflejan un contexto distinto (posiblemente usuarios de la app, no necesariamente shoppers en supermercado físico). Sinta debe marcar todos los hallazgos derivados de App Gama con la etiqueta `[FUENTE: App Gama — contexto digital/B2B]` y no mezclar con hallazgos del tracker físico sin nota explícita.

### 3.2 Diseño analítico: análisis temático Braun & Clarke (2006)

**Referencia canónica:** Braun, V., & Clarke, V. (2006). Using Thematic Analysis in Psychology. *Qualitative Research in Psychology*, 3(2), 77-101.

El análisis sigue el protocolo de 6 fases de Braun & Clarke:

1. **Familiarización:** leer todos los materiales dos veces. Notar primeras impresiones.
2. **Generación inicial de códigos:** codificación línea por línea de los materiales (especialmente verbatims raw). Cada código captura una unidad de significado.
3. **Búsqueda de temas:** agrupar códigos en temas candidatos.
4. **Revisión de temas:** verificar que cada tema tiene suficiente evidencia textual y es distinto de los otros.
5. **Definición y naming de temas:** articular claramente qué es y qué no es cada tema.
6. **Producción del reporte:** escribir la narrativa analítica con verbatims ilustrativos.

**Modo de codificación: deductivo-inductivo en dos pasadas:**

**Primera pasada — deductiva:** aplicar el framework de drivers V3 como estructura de códigos a priori:
- Categoría D1: Atención / servicio / personal (driver #1 V3)
- Categoría D2: Limpieza / orden / higiene (driver #2 V3)
- Categoría D3: Promociones / ofertas (driver #3 V3)
- Categoría B1: Precio (barrera documentada)
- Categoría B2: Surtido / variedad (barrera documentada)
- Categoría B3: Cobertura / conveniencia geográfica (barrera documentada)
- Categoría S1: Segmento Mayoría Exigente — referencias a calidad y experiencia
- Categoría S2: Segmento Pragmáticos Convertibles — referencias a precio/cercanía como motivos
- Categoría S3: Núcleo Leal — referencias a fidelidad, identidad con la marca

**Segunda pasada — inductiva:** identificar unidades de significado que NO encajan en las categorías anteriores. Estos son los hallazgos emergentes de mayor valor: lo que V3 no anticipó. Crear categorías emergentes con nombre derivado del contenido, no de la estructura previa.

### 3.3 Protocolo de codificación: 3 niveles

**Nivel 1 — Codes (unidades básicas):**
- Unidad: fragmento de texto que expresa un significado cohesivo (una oración o fragmento de oración).
- Nombre del código: etiqueta descriptiva en 2-5 palabras.
- Registro: tabla con columnas [código, fragmento_verbatim, fuente_doc, segmento_entrevistado, pasada_deductiva_o_inductiva].

**Nivel 2 — Themes (agrupaciones de códigos):**
- Un tema agrupa 3 o más códigos que comparten un patrón de significado subyacente.
- Cada tema debe tener: nombre, definición (2-3 oraciones), lista de códigos que lo componen, fragmentos verbatim ilustrativos (mínimo 2 por tema).
- Target: 4-6 temas principales. Si emergen más de 8, agrupar o jerarquizar.

**Nivel 3 — Overarching narratives (hilos transversales):**
- 2-3 narrativas que atraviesan múltiples temas y son el "esqueleto" de la interpretación cualitativa V4.
- Cada narrativa se articula como una proposición completa (una oración de declaración de hallazgo), no como un título.
- Ejemplo de formato esperado: "La preferencia por Gama está mediada por relaciones interpersonales con el personal, no por atributos funcionales abstractos de la tienda."

### 3.4 Limitación inter-rater — Documentación obligatoria

El análisis cualitativo V4 tiene un solo analista (Sinta). No hay segundo codificador para calcular Kappa inter-rater (Landis & Koch, 1977; Krippendorff, 2004, *Content Analysis*, §11).

**Sinta debe incluir en IN-7 §1 (Metodología) el siguiente texto:**

> "El presente análisis fue realizado por un único analista (Sinta). La ausencia de un segundo codificador independiente implica que el coeficiente de confiabilidad entre codificadores (Kappa de Cohen o alfa de Krippendorff) no puede calcularse. Los resultados cualitativos deben interpretarse como la perspectiva analítica de un único observador riguroso, no como clasificaciones con validación inter-subjetiva formal. Esta limitación reduce la replicabilidad pero no invalida los hallazgos — la interpretación temática single-analyst es la práctica estándar en investigación cualitativa aplicada cuando el presupuesto y el tiempo no permiten doble codificación. Para ola 2027, se recomienda doble codificación en un 20% de los materiales."

---

## 4. Triangulación Cuali-Cuanti V4 — Protocolo para Sinta

### 4.1 Principio de triangulación

La triangulación metodológica combina evidencia de fuentes independientes para fortalecer o matizar una proposición (Denzin, 1978, *The Research Act*, Ch. 10; Creswell & Plano Clark, *Designing and Conducting Mixed Methods Research*, 3rd ed., 2018, §2). En este estudio, la triangulación opera en una dirección específica: **los hallazgos cuantitativos V3 y CU-7 son los de referencia; los materiales cualitativos los corroboran, amplifican, matizan o contradicen.**

Esta dirección (cuanti como ancla) es deliberada: el cuantitativo tiene más poder estadístico para afirmaciones de prevalencia ("cuántos"); el cualitativo tiene más poder para afirmaciones de mecanismo y proceso ("por qué" y "cómo"). Las proposiciones de V3 son prevalencia + correlación; V4 añade la capa de mecanismo.

### 4.2 Hipótesis de triangulación #1: "Atención = Reconocimiento Personal" (V3 IN-5)

**Proposición V3 (hipótesis derivada, no confirmada):** el driver de preferencia "Atención al cliente" no opera como atributo funcional abstracto (rapidez, eficiencia) sino como reconocimiento personal — el personal de Gama conoce a los compradores por nombre o les genera una experiencia de pertenencia. Esta hipótesis emergió del análisis temático V3 con verbatims limitados (razones abiertas de preferencia P21.1).

**Protocolo de validación/refutación en V4:**

Sinta busca en los verbatims raw (los 4 documentos) evidencia específica de:

- Menciones a interacciones personalizadas con el personal (nombre propio, reconocimiento, memoria de compras previas, trato diferenciado).
- Contraste entre descripciones de atención como "rápida/eficiente" (funcional) vs "cálida/personalizada" (relacional).
- Ausencia o presencia de este patrón por segmento (¿es más marcado en clientes frecuentes vs ocasionales? ¿en mayores vs jóvenes?).

**Criterio de validación:**

| Evidencia encontrada | Estatus hipótesis IN-5 | Acción para deck V4 |
|---|---|---|
| ≥3 verbatims independientes con referencia explícita a reconocimiento personal, en ≥2 segmentos | CONFIRMADA | Presentar como hallazgo V4 con evidencia combinada cuanti+cuali |
| 1-2 verbatims en 1 solo segmento | PARCIALMENTE SUGERIDA | Presentar como hipótesis plausible no confirmada, con cita literal |
| No se encuentra referencia explícita; atención descripta en términos funcionales | NO CONFIRMADA — reformular | El driver "Atención" se mantiene, pero se describe solo como funcional. Nota de honestidad: la hipótesis de reconocimiento personal no fue corroborada. |

**Nota:** la ausencia de evidencia en los verbatims no equivale a refutación (la hipótesis puede ser cierta pero no haber emergido en las sesiones de focus group). Sinta articula esta distinción al reportar.

### 4.3 Hipótesis de triangulación #2: Validación de los 3 segmentos k-means V3

**Segmentos V3 (Cuanti CU-4):**
- Segmento 1 — Mayoría Exigente (59%): shoppers que valoran experiencia de compra, menos sensibles al precio, distribución más uniforme de preferencias de marca.
- Segmento 2 — Pragmáticos Convertibles (33%): shoppers orientados por precio y conveniencia. Oportunidad de conversión de corto plazo para Gama.
- Segmento 3 — Núcleo Leal (8%): núcleo de preferentes de Gama, alta asociación con drivers de atención.

**Protocolo de validación cualitativa:**

Sinta analiza los materiales cualitativos buscando:

1. ¿Los segmentos naturales emergentes en los focus groups corresponden a los 3 perfiles k-means? (Ej. ¿hay un grupo que habla principalmente de precio vs uno que habla principalmente de experiencia?)
2. ¿Los segmentos por edad/frecuencia de compra del diseño cualitativo (18-30 vs 31-50 vs 50+, ocasional vs frecuente) muestran patrones de prioridades coherentes con los k-means?
3. ¿Emergen en los focus groups perfiles que NO encajan en los 3 segmentos y que sugieren una estructura de 4 o más grupos?

**Criterio:**

| Evidencia | Estatus segmentos k-means | Acción |
|---|---|---|
| Los 3 perfiles son reconocibles en los materiales cuali, con características similares a k-means | CONFIRMADOS — narrativa cuali coherente | Presentar en deck V4 como "triangulación cuali-cuanti confirma estructura de mercado" |
| 2 de 3 perfiles son reconocibles; el tercero no emerge claramente | PARCIALMENTE CONFIRMADOS | Presentar con matiz: 2 perfiles robustos, 1 requiere validación adicional |
| Los materiales cuali sugieren una estructura diferente (ej. 2 o 4 grupos con distinta lógica) | TENSIÓN — requiere nota de honestidad | Ver §6.3 protocolo de tensión V3/V4 |

### 4.4 Hipótesis de triangulación #3: Barreras de compra no capturadas por cuanti

El cuestionario cuantitativo mide atributos de importancia y asociación, pero no captura directamente las barreras que impiden a los no-preferentes de Gama considerar o probar la cadena. Los focus groups son el espacio donde estas barreras emergen como narrativa.

**Protocolo de identificación:**

Sinta busca activamente en los materiales cualitativas menciones de:

1. **Percepciones negativas sticky:** prejuicios, rumores, experiencias negativas previas que persisten a pesar de posibles cambios reales en Gama.
2. **Objeciones de precio explícitas:** afirmaciones sobre el nivel de precios de Gama que sean falsas o exageradas, sugiriendo sesgo de percepción vs realidad.
3. **Barreras de acceso:** menciones de que Gama no está "de paso" en la ruta habitual, que sus horarios no convienen, que el estacionamiento es difícil, u otras barreras físicas de conveniencia.
4. **Barreras de identidad:** afirmaciones del tipo "Gama es para cierto tipo de persona" que excluyan al entrevistado por auto-percepción de perfil.
5. **Barreras de surtido específicas:** categorías concretas donde la percepción de ausencia o mala calidad en Gama es persistente.

**Output de este protocolo:** lista de 4-8 barreras enumeradas como "Hallazgos V4 nuevos" con frecuencia aproximada de mención (alta/media/baja) y cita verbatim ilustrativa. Estas barreras son insights adicionales que el cuantitativo no midió y que Gama puede usar para diseñar intervenciones específicas.

---

## 5. Plan de Claims V4 — Tipología y niveles de evidencia

Todos los hallazgos de V4 se clasifican en una de tres tipologías antes de pasar al gate de Bruna. Cuanti y Sinta deben etiquetar cada hallazgo al final de sus documentos respectivos.

### Tipo A — WoW Confirmados

**Criterio:** el cambio inter-ola es estadísticamente significativo (p BH-ajustado < 0.05) en la misma dirección que la narrativa V3, con magnitud ≥ 3 pp (diferencia mínima prácticamente relevante para estrategia de marca en este contexto).

**Etiqueta en deck V4:** `[WoW Confirmado | p=X.XX | Δ=±X pp]`

**Nivel de afirmación permitido:** "Entre 2025 y 2026, [métrica] [aumentó/disminuyó] en [X] puntos porcentuales (estadísticamente significativo)."

**Ejemplo hipotético:** "La notoriedad espontánea de Gama aumentó de 38% (2025) a 44% (2026), incremento de 6 pp significativo al 95% de confianza."

### Tipo B — Cuali Corroborated

**Criterio:** hallazgo V3 (ya establecido cuantitativamente en el estudio base) que tiene corroboración directa en el material cualitativo V4. La triangulación añade la capa de mecanismo o narrativa que el cuantitativo no podía proveer.

**Condición:** el hallazgo cuantitativo debe existir primero (de V3 o de CU-7). El cualitativo corrobora o amplía — no reemplaza.

**Etiqueta en deck V4:** `[Triangulado: cuanti V3 + cuali V4]`

**Nivel de afirmación permitido:** "Los datos cuantitativos muestran que [X]. Los grupos focales proveen el mecanismo: [Y, con verbatim]."

**Ejemplo hipotético:** "Los datos cuantitativos muestran que Atención es el driver #1 de preferencia (OR=5.73). Los focus groups revelan que esta atención opera como [narrativa concreta con cita]."

### Tipo C — Hipótesis Aún Sin Cerrar

**Criterio:** proposición que tiene alguna evidencia (cuali o cuanti) pero no el nivel de corroboración requerido para Tipo A o B. Puede ser: tendencia WoW borderline (p BH-ajustado entre 0.05 y 0.20), hallazgo cualitativo de una sola sesión o segmento, o hipótesis derivada sin fuente de datos directa.

**Etiqueta en deck V4:** `[Hipótesis V4 — pendiente confirmación ola 2027]`

**Nivel de afirmación permitido:** "Los datos sugieren, aunque no permiten confirmar, que [X]. Se recomienda diseñar ola 2027 para testear esta hipótesis directamente."

**Ejemplo hipotético:** "Los materiales cualitativos sugieren que la barrera de precio para Gama puede ser más perceptual que real. Esta hipótesis requiere auditoría de precios in-store (ver Reflexiones 2027, Rec. 6) para confirmación."

---

## 6. Decisiones Críticas — Con Recomendaciones Pre-pagadas de Methos

### 6.1 Ponderación 2025 — DECIDIDA

**[DECISION-METHOS: Usar ponderación 2025 sí.** Ver §2.4 para razón completa.]

No requiere confirmación del Owner — Methos toma esta decisión con base en principio metodológico estándar.

### 6.2 Threshold de significancia y corrección múltiple — DECIDIDA

**[DECISION-METHOS: α = 0.05 para el análisis sustantivo WoW, con corrección BH-FDR. α = 0.10 para test auxiliar de comparabilidad muestral.** Ver §2.5 y §2.6 para razón completa.]

No requiere confirmación del Owner — decisión metodológica estándar con razón explícita.

### 6.3 Protocolo cuando triangulación V4 contradice un claim V3

**[DECISION-OWNER — requerida, con recomendación pre-pagada de Methos]**

Esta es la decisión de mayor consecuencia en V4. Si un hallazgo WoW o cualitativo contradice directamente un claim que ya fue entregado a Cora en el deck V3, existen tres posiciones posibles:

**Posición I — Preservar V3 + nota de honestidad en V4**
V3 se mantiene intacto como entregado. V4 presenta la contradicción explícitamente con el lenguaje de Tipo C ("Los datos V4 matizan esta afirmación...") y recomienda nueva ola de confirmación.

- Ventaja: evita señal confusa a Cora/Gama sobre la consistencia del trabajo.
- Riesgo: si la contradicción es sustantiva, V4 tiene menor utilidad accionable.

**Posición II — Ajustar wording en V4 con reformulación**
El claim V3 se reformula en V4 con un enunciado más preciso o acotado, sin declararlo erróneo. Ej: "La atención es el driver de preferencia entre los clientes de Gama [V3]" → "La atención es el driver de preferencia entre los clientes de Gama, aunque los datos WoW sugieren que su magnitud relativa puede variar por ola [V4]."

- Ventaja: honestidad académica sin dramaturgia innecesaria.
- Riesgo: Cora puede percibir inconsistencia si compara V3 y V4 side-by-side.

**Posición III — Declarar divergencia explícita y escalar**
V4 declara abiertamente "El dato WoW contradice la afirmación V3 en [dimensión específica]. La causa puede ser [A, B, C]. Se recomienda no comunicar ninguna de las dos versiones a Gama hasta tener evidencia adicional."

- Ventaja: máxima honestidad epistémica.
- Riesgo: crea incertidumbre sobre todo el estudio.

**Recomendación pre-pagada de Methos: Posición II (reformulación) para matices menores; Posición III (divergencia explícita + escalar) solo para contradicciones directas de claims de alta certeza V3.**

La distinción entre matiz menor y contradicción directa se define así:

- **Matiz menor:** la dirección del hallazgo se mantiene, cambia la magnitud o la condición de aplicabilidad. (Ej: Atención sigue siendo driver, pero el WoW muestra que su OR disminuyó entre olas.)
- **Contradicción directa:** la dirección del hallazgo se invierte. (Ej: V3 dice que Precio NO es driver; el WoW muestra que en 2025 Precio SÍ era driver significativo.)

**[DECISION-OWNER]:** ¿Confirma Methos aplica Posición II para matices y Posición III para contradicciones directas? Si el Owner tiene preferencia diferente (ej. siempre Posición I), indicarlo antes de que Bruna ejecute el gate V4.

---

## 7. Plan de análisis a priori — Resumen ejecutivo para Cuanti y Sinta

### Para Cuanti:

| Paso | Análisis | Herramienta | Output |
|---|---|---|---|
| 0 | Verificar formulación exacta de ítems | Manual (BBDD + Guía + Cuestionario papel) | Columna `enunciado_identico` en mapping CSV |
| 1 | Construir mapping_2025_2026.csv | Python pandas | Archivo CSV con 24-40 filas |
| 2 | Tests de comparabilidad muestral (4 variables demográficas) | `scipy.stats.chi2_contingency` | Tabla de resultados + flag "comparable / ajuste recomendado" |
| 3 | Verificar y aplicar ponderación `@PONDERAR_1` | `statsmodels` con `weights` | DEFF por variable clave |
| 4 | Newcombe-Wilson por ítem comparado | `statsmodels.stats.proportion` | JSON por ítem (ver formato §2.5) |
| 5 | Corrección BH-FDR sobre todos los p-values | `statsmodels.stats.multitest.multipletests(method='fdr_bh')` | p_adjusted por ítem |
| 6 | Análisis por subgrupo NSE C+/C y D/E (donde n≥50 en ambas olas) | Ídem pasos 4-5, por subconjunto | Tablas de subgrupo |
| 7 | Forest plot de deltas significativos | `matplotlib` | PNG forest plot top cambios |
| 8 | CU-7 caveats para Bruna | Manual | Lista claims × nivel de evidencia |

**Script base recomendado:** adaptar `utils.py` y `00_cuanti_master.py` existentes para agregar función `load_bbdd_2025(weighted=True)` paralela a `load_bbdd_2026()`. No reescribir — extender.

### Para Sinta:

| Paso | Análisis | Output |
|---|---|---|
| 0 | Inventariar los 10 docs cuali (confirmando estructura real vs esperada) | Tabla de inventario en IN-7 §1 |
| 1 | Leer dos veces todos los materiales. Notas de familiarización. | Notas inline (no publicadas) |
| 2 | Codificación deductiva (9 categorías pre-definidas §3.2) | Tabla código-fragmento-fuente |
| 3 | Codificación inductiva (categorías emergentes) | Misma tabla, columna `tipo=inductivo` |
| 4 | Agrupación en 4-6 temas (Nivel 2) | Tabla de temas con definición y frecuencia |
| 5 | Articular 2-3 narrativas overarching (Nivel 3) | Proposiciones en texto libre |
| 6 | Hipótesis triangulación #1: "Atención = reconocimiento personal" | Evaluación A/B/C + verbatims |
| 7 | Hipótesis triangulación #2: Validación segmentos k-means | Evaluación A/B/C + narrativa |
| 8 | Hipótesis triangulación #3: Barreras emergentes | Lista 4-8 barreras con cita |
| 9 | Clasificar todos los hallazgos en Tipo A/B/C para Bruna | Tabla hallazgos × tipo |
| 10 | IN-8: tabla de hallazgos × estado triangulación (Confirma/Amplifica/Matiza/Contradice) | Tabla + narrativa |

---

## 8. Supuestos, límites y dependencias de este plan

### 8.1 Supuestos que si se violan invalidan partes del plan

| Supuesto | Qué se invalida si se viola |
|---|---|
| La Guía de Preguntas 2026 (con marcado rojo/negro) es la fuente autoritativa de comparabilidad inter-ola | Todo el mapping §2.2. Escalar al Owner para nueva fuente de verdad. |
| `@PONDERAR_1` es un factor de expansión continuo, no un flag binario | La decisión de ponderación §2.4 (requiere ajuste si es flag). |
| Los 10 docs cualitativos cubren los 6 segmentos esperados (18-30/31-50/50+ × ocas/frec) + verbatims + App Gama | El protocolo §3.1. Ajustar al inventario real. |
| Los datos de BBDD 2025 son la versión final que Cora/Gama usó para sus reportes anteriores | Si hay una versión posterior, reemplazar antes de correr cualquier análisis. |

### 8.2 Límites del plan

- **V4 no es pre-registrado:** los análisis de V4 se diseñaron después de conocer los resultados de V3 (lo que en rigor los hace semi-confirmatorios, no prospectivos). Esta limitación es inevitable dado el contexto del proyecto. Se mitiga documentando el plan completo a priori antes de abrir la BBDD 2025 para análisis WoW, y declarando el estatus en los caveats. (Wasserstein & Lazar, 2016).
- **La causalidad no es inferible:** los cambios WoW son correlacionales. No se puede atribuir un cambio en preferencia a ninguna acción específica de Gama sin un diseño experimental.
- **El análisis cualitativo es exploratorio por diseño:** los focus groups no son representativos de la población. Sus hallazgos generan hipótesis, no confirmaciones de prevalencia.
- **Los segmentos k-means de V3 no son perfiles deterministas:** un respondiente puede pertenecer a distintos segmentos en diferentes momentos. La segmentación describe perfiles promedio de grupo, no identidades fijas.

### 8.3 Dependencias de la cadena

```
ME-5 (este doc)
    → Cuanti (CU-7: análisis WoW, JSON, forest plot, caveats)
    → Sinta (IN-7: cuali profundo, IN-8: triangulación V4)
        ← CU-7 como input para IN-8
    → Bruna (gate V4: CU-7 caveats + IN-8 clasificación A/B/C)
    → Vivienne (VI-1a outline V4: recibe CU-7 + IN-7 + IN-8)
```

Cuanti puede ejecutar CU-7 en paralelo con Sinta ejecutando IN-7. Sinta necesita CU-7 finalizado ANTES de escribir IN-8 (triangulación requiere los hallazgos WoW).

---

## 9. Referencias metodológicas citadas en este memo

- Benjamini, Y., & Hochberg, Y. (1995). Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing. *Journal of the Royal Statistical Society: Series B (Methodological)*, 57(1), 289-300.
- Braun, V., & Clarke, V. (2006). Using Thematic Analysis in Psychology. *Qualitative Research in Psychology*, 3(2), 77-101.
- Cochran, W.G. (1977). *Sampling Techniques*, 3rd ed. Wiley.
- Creswell, J.W., & Plano Clark, V.L. (2018). *Designing and Conducting Mixed Methods Research*, 3rd ed. SAGE Publications.
- Denzin, N.K. (1978). *The Research Act: A Theoretical Introduction to Sociological Methods*. McGraw-Hill.
- Groves, R.M., Fowler, F.J., Couper, M.P., Lepkowski, J.M., Singer, E., & Tourangeau, R. (2009). *Survey Methodology*, 2nd ed. Wiley.
- Krippendorff, K. (2004). *Content Analysis: An Introduction to Its Methodology*, 2nd ed. SAGE Publications.
- Landis, J.R., & Koch, G.G. (1977). The Measurement of Observer Agreement for Categorical Data. *Biometrics*, 33(1), 159-174.
- Newcombe, R.G. (1998). Interval Estimation for the Difference Between Independent Proportions: Comparison of Eleven Methods. *Statistics in Medicine*, 17(8), 857-872.
- Tourangeau, R., Rips, L.J., & Rasinski, K. (2000). *The Psychology of Survey Response*. Cambridge University Press.
- Wasserstein, R.L., & Lazar, N.A. (2016). The ASA's Statement on p-Values: Context, Process, and Purpose. *The American Statistician*, 70(2), 129-133.
- Wasserstein, R.L., Schirm, A.L., & Lazar, N.A. (2019). Moving to a World Beyond "p < 0.05". *The American Statistician*, 73(S1), 1-19.

---

*Fin del ME-5 — Methodology Plan for V4 Layer v1*
*Siguiente en cadena: Cuanti ejecuta CU-7 (puede arrancar inmediatamente). Sinta ejecuta IN-7 en paralelo; IN-8 espera CU-7 finalizado.*
*Decision-Owner pendiente: §6.3 — protocolo cuando triangulación contradice claim V3.*
