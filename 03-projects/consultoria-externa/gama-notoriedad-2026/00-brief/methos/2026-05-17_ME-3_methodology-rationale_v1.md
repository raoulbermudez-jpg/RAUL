---
autor: Methos (Research Design & Methodology Lead)
proyecto: gama-notoriedad-2026
tipo: ME-3 Methodology Selection Rationale
version: v1
fecha: 2026-05-17
status: draft — para revisión Owner antes de circulación
confidencialidad: interno equipo / puede compartirse con Cora en versión abreviada
---

# ME-3 — Methodology Selection Rationale
## Notoriedad Gama 2026 — Defensa y cuestionamiento de cada técnica

**Fecha:** 2026-05-17
**Autor:** Methos
**Para:** Owner / Cora / futura referencia Cuanti
**Propósito:** Para cada técnica realmente usada en el estudio, evaluar si fue la elección apropiada, documentar sus supuestos, identificar limitaciones conocidas, y proponer alternativas para ola 2027. Este documento es el insumo primario para conversaciones técnicas con Cora sobre el upgrade metodológico.

> **Tono de este documento:** técnico y directo, pero no destructivo. El estudio ejecutado es metodológicamente competente para su scope y plazo. Las críticas que siguen son sobre lo que se podría hacer mejor con más recursos y tiempo, no sobre lo que falló.

---

## Sección 1 — Notoriedad espontánea (TOM) y asistida

### Técnica usada

Pregunta abierta (P16) para notoriedad espontánea "Top of Mind" → lista asistida (P17) posterior. Codificación de respuestas espontáneas para calcular TOM por marca.

### Veredicto: APROPIADA

**Justificación:**

La secuencia espontánea → asistida es el estándar de oro para medir salience de marca (Keller, 2013, §3). Invertir el orden contaminaría la espontánea con los estímulos de la lista. El protocolo ejecutado respeta este principio correctamente.

**Supuestos que el diseño asume:**

1. El respondiente en el momento de la entrevista tiene activos los mismos patrones de asociación que tendría en el momento de una decisión de compra real. Esto puede no ser cierto si la entrevista se hace fuera del punto de compra o en un momento no congruente con la situación de compra (limitación menor en F2F de intercepción).
2. La codificación de respuestas espontáneas es consistente entre encuestadores — ambigüedades en nombres de marca (ej. "Gama Excelsior" vs "Gama" vs "el Gama") se resuelven de la misma manera.

**Limitación conocida:** la notoriedad TOM mide el "primer brand que viene a la mente" en contexto de pregunta directa. No mide mental availability en contextos específicos de compra (para eso se necesitan CEPs — ver ME-1 §5.2 y sección 5 de este doc).

**Alternativa que se podría agregar (2027):** complementar TOM con medición de "link" a CEPs específicos: "¿Qué supermercado de cadena viene a la mente cuando piensas en [hacer el mercado del mes]?" por cada CEP. Produce un "share of mind" por ocasión, que es el indicador que Ehrenberg-Bass recomienda trackear. (Romaniuk, 2023; Sharp, 2010, ch. 6).

---

## Sección 2 — Embudo de marca (P16 → P17 → P19 → P20 → P21)

### Técnica usada

Embudo secuencial de 5 etapas: notoriedad espontánea → asistida → consideración → compra últimos 3 meses → preferida. Tasas de conversión calculadas entre etapas.

### Veredicto: APROPIADA con matices

**Justificación:**

El modelo de embudo secuencial es el marco estándar para brand health tracking en CPG/retail (Aaker, 1991; Keller, 2013). La secuencia impone un orden lógico que refleja el proceso cognitivo del comprador: primero debe conocer (para luego considerar, comprar y preferir). Las tasas de conversión entre etapas son diagnósticos estratégicos valiosos (ej. alta notoriedad + baja consideración = problema de relevancia percibida).

**Supuesto crítico:** el embudo asume que las etapas son estrictamente jerárquicas. En la práctica del retail moderno, un shopper puede comprar una marca sin haberla "considerado" formalmente (compra impulsiva en el pasillo), o puede preferir una marca que no usó en los últimos 3 meses (lealtad actitudinal sin compra reciente por inaccesibilidad). Estos casos rompen la lógica secuencial del embudo.

**Limitación conocida:** "compra últimos 3 meses" (P20) es una ventana de memoria relativamente corta. Para categorías con frecuencia de compra quincenal o mensual, 3 meses puede subestimar la base de compradores reales. La alternativa estándar Ehrenberg-Bass es penetración 12 meses (Ehrenberg et al., *Double Jeopardy and the Duplication of Purchase Law*, 2004).

**Alternativa para 2027:** mantener los 5 ítems del embudo para comparabilidad, pero AGREGAR penetración 12 meses como sexta métrica. Permite calcular tanto el KPI de corto plazo (reciente) como el de largo plazo (penetración anual) que es la métrica maestra en How Brands Grow.

### Sobre la tasa de conversión Pref-Gama (n=32)

El margen de error de ±17.3% sobre n=32 implica que cualquier porcentaje reportado para este subgrupo tiene un intervalo de confianza de ~35 pp de amplitud. El estudio manejó esto correctamente con caveats explícitos. Para uso estratégico real, estas cifras deben tratarse como indicaciones cualitativas, no como datos para decisiones de inversión.

**Falla metodológica que se debió prevenir:** el bajo n de Pref-Gama era predecible antes del fieldwork (si Gama tiene ~8% de preferencia en C+/C, con n=402 se esperaban ~32 casos). Un plan muestral con booster de Pref-Gama (sobremuestreo dirigido) hubiera sido la solución. Ver recomendación de n=80 para Pref-Gama en ME-1 §4.2.

---

## Sección 3 — Importancia declarada de atributos (P22 — Likert 5 puntos)

### Técnica usada

Escala Likert de 5 puntos ("Nada importante" a "Muy importante") aplicada a 10 atributos de supermercado. Métrica reportada: Top-2 Box (T2B = % "Muy importante" + "Importante").

### Veredicto: INAPROPIADA para el objetivo de priorización — es la brecha metodológica más grave del instrumento

**Justificación del problema:**

El resultado fue que todos los atributos obtuvieron T2B entre 87% y 97% — una distribución prácticamente plana que no permite discriminar cuáles atributos son más importantes que otros. Este fenómeno tiene nombre: **yea-saying bias** (Paulhus, 1991) — la tendencia del respondiente a marcar positivo en preguntas de importancia cuando no hay costo por hacerlo.

El problema no es del instrumento en sí (Likert es válido para medir grado de acuerdo con afirmaciones), sino de su aplicación a preguntas de importancia sin forzar trade-offs. Cuando se pregunta "¿qué tan importante es X?" y "¿qué tan importante es Y?" en preguntas separadas, el respondiente puede responder "muy importante" a ambas sin contradicción. Esto produce datos sin poder discriminativo.

**Consecuencia directa:** la sección de importancia de atributos, tal como fue medida, no puede fundamentar recomendaciones del tipo "Gama debería invertir en [atributo A] más que en [atributo B]". El Doc Técnico reconoció esto correctamente. El análisis mitigó el problema con z-scores de normalización (que extraen señal relativa a pesar de la saturación), pero el problema de raíz es el instrumento.

**Evidencia en la literatura:**

> "Rating scales tend to produce importance data that are highly skewed toward the top of the scale, making it difficult to distinguish between attributes that are truly important and those that are merely acceptable." — Louviere, Flynn & Marley, *Best-Worst Scaling*, 2015, p. 3.

> "The standard Likert-type importance rating is the worst way to measure attribute importance... it overestimates the importance of all attributes simultaneously." — Orme, *Getting Started with Conjoint Analysis*, 2019, p. 45.

**Alternativa recomendada para 2027: MaxDiff (Best-Worst Scaling)**

MaxDiff presenta al respondiente conjuntos de 3-5 atributos y le pide que seleccione cuál es el MÁS importante y cuál es el MENOS importante de ese conjunto. Cada atributo aparece aproximadamente 3 veces en diferentes conjuntos. El resultado son utilidades escaladas (anchored max-diff scores o HB bayesian scores) que producen una jerarquía ordinal con distancias reales entre atributos.

| Dimensión | Likert T2B (ejecutado) | MaxDiff (propuesto) |
|---|---|---|
| Discriminación entre atributos | Baja — todos saturan en 87-97% | Alta — produce jerarquía con distancias métricas |
| Carga cognitiva | Baja | Moderada (8-10 tareas vs una sola tabla) |
| Tiempo en cuestionario | ~2 min | ~4 min |
| Costo analítico | Trivial (tablas de frecuencia) | Moderado (HB-MNL en Python/R o Sawtooth) |
| Accionabilidad para inversión | Muy baja | Alta — permite decir "atributo A es 2.3x más importante que atributo B" |
| Comparabilidad inter-ola | Alta si se mantiene idéntico | Alta si se mantienen los mismos atributos |

**Diseño de MaxDiff recomendado para 10 atributos:**
- 10 atributos × 10 tareas × 4 atributos por tarea (diseño balanceado).
- Cada atributo aparece exactamente 4 veces. Cada par aparece máximo 1 vez.
- Duración estimada: 3-4 min adicionales al cuestionario.
- Software: Lighthouse Studio (Sawtooth) si se tiene licencia; alternativa gratuita con `pylogit` en Python.

### Sobre la técnica de z-score para mitigar el problema Likert

El Doc Técnico documentó el uso de z-score por atributo (z = (val_marca - mean_atributo) / sd_atributo) para extraer posicionamiento relativo pese a la saturación Likert. Esta fue una solución analítica inteligente y defensible, pero es una mitigación post-hoc, no una solución al problema de diseño. El dato de z-score es informativo, pero los umbrales operativos (|z| > 0.7) no tienen base estadística formal — son juicios de experto razonables pero no anclados en un test de hipótesis formal.

---

## Sección 4 — Asociación marca × atributo (P23 — multi-select binario)

### Técnica usada

Para cada marca, el respondiente marca si asocia o no la marca con cada uno de los 10 atributos (binario sí/no). Se calcula % de asociación por marca × atributo. Multi-select: el respondiente puede marcar todas las marcas que asocia con cada atributo.

### Veredicto: APROPIADA

**Justificación:**

El multi-select binario para asociación de marca-atributo es el estándar de la industria (Keller, 2013, §5; Young & Rubicam BrandAsset Valuator; WPP BrandZ). Es robusto, fácil de administrar en F2F, y produce datos directamente comparables inter-ola si los atributos no cambian.

**Supuesto crítico:** la asociación se mide a nivel agregado (% que asocia la marca con el atributo). No captura la intensidad ni la confianza de la asociación. Una marca donde el 40% la asocia "fuertemente" con limpieza y otra donde el 40% la asocia "vagamente" producen el mismo número. Esto es inherente al diseño binario.

**Limitación conocida:** el cambio de 20 atributos (2025) a 10 atributos (2026) rompe la comparabilidad en los 10 atributos eliminados. La decisión fue correcta (comparar solo lo coincidente), pero implica que la "Normalización" del deck 2025 no es directamente reproducible en 2026 en toda su extensión.

**Fortaleza del análisis ejecutado:** el heatmap z-score cross-brand (Slide 13 del deck V2) es una de las mejores visualizaciones del estudio — convierte los porcentajes brutos en posicionamiento diferencial, permitiendo identificar claramente los atributos donde Gama sobreindeda y los donde tiene brechas vs competencia. Es un análisis correcto y accionable.

---

## Sección 5 — Importancia declarada vs derivada: el gap central del estudio

### El problema de la importancia declarada

Las técnicas de importancia declarada (Likert, ranking directo) tienen un problema conocido desde los años 1970: las personas no siempre saben — o no quieren revelar — qué atributos realmente motivan sus decisiones. Declaran importantes los atributos socialmente deseables ("calidad", "limpieza") aunque sus decisiones reales las tome por precio o conveniencia.

### La importancia derivada como alternativa

La importancia derivada estima el peso de cada atributo a partir de su correlación con la variable de outcome (ej. preferencia). No pregunta directamente qué importa — lo infiere del patrón de elecciones. Las técnicas más comunes son: regresión múltiple (OLS), regresión logística, Shapley Value Analysis, Conjoint Analysis.

### Lo que el estudio ejecutó (convergencia metodológica — fortaleza real)

El análisis de Fase B implementó, sin haberlo planificado formalmente a priori, una convergencia de tres aproximaciones independientes a la importancia:

1. **Importancia declarada** (P22 Likert T2B) — aunque sesgada por yea-saying.
2. **Asociación y z-score** (P23 + normalización) — importancia relativa inferida de la fortaleza diferencial de asociación.
3. **Regresión logística** (P21=Gama ~ P23 atributos) — **importancia derivada** real: efecto independiente de cada atributo sobre la probabilidad de preferencia.

La convergencia entre estas tres fuentes para el atributo "Atención" (declarada alta + z-score positivo + OR=5.73 en logit) es evidencia robusta de que "Atención" es efectivamente el driver central de preferencia de Gama. Esto es metodológicamente sólido y constituye el hallazgo más confiable del estudio.

**Tabla de convergencia (resumida del Doc Técnico):**

| Atributo | Importancia declarada T2B | Z-score asociación | OR logit | Convergencia |
|---|---|---|---|---|
| Atención al cliente | ~94% T2B | +0.47 (medio) | 5.73*** | ALTA — driver confirmado |
| Limpieza | ~97% T2B | +0.82 (alto) | 4.03** | ALTA — driver confirmado |
| Promociones | ~89% T2B | +0.31 (medio) | 3.62** | MEDIA-ALTA |
| Precio | ~93% T2B | -0.21 (negativo) | 1.03 (NS) | BAJA — no es driver real de Gama |

Esta tabla no estaba en el análisis oficial pero puede derivarse de los JSONs. Es el corazón del insight estratégico del estudio.

---

## Sección 6 — Precio en escala (P33) y ranking forzado (P31)

### 6.1 P33 — Escala ordinal de percepción de precio (bajos/medios/altos)

### Técnica usada

Escala ordinal de 5 niveles (precios muy bajos → bajos → medios → altos → muy altos) para evaluar la percepción general del nivel de precios de Gama. Métrica derivada: NETO de "caros" menos "económicos".

### Veredicto: APROPIADA para el objetivo declarado; insuficiente para la decisión de negocio implícita

**Justificación de lo apropiado:** mide directamente la percepción de precio, que es la variable relevante para estrategia de comunicación (si Gama es percibida cara pero sus precios son competitivos, el problema es de comunicación, no de estructura de precios). Fácil de administrar en F2F. Comparable inter-ola.

**Insuficiencia para decisión de negocio:** la escala ordinal indica *si* Gama es percibida cara o barata, pero no indica *cuánto* cuesta demasiado ni cuál sería el precio aceptable. Para recomendar acciones de precio específicas (ej. "si Gama reduce precio en leche un 8%, captura X% de share"), se necesita una curva de elasticidad, no una percepción categórica.

**Alternativa para 2027:** Van Westendorp Price Sensitivity Meter (Van Westendorp, 1976) en 3-4 categorías KVI (Known Value Items — los productos cuyo precio el consumidor conoce de memoria). Produce Optimal Price Point (OPP) y Acceptable Price Range. Cuatro preguntas por categoría:

- "¿A qué precio te parecería muy barato (tanto que dudarías de la calidad)?"
- "¿A qué precio te parecería barato/buena compra?"
- "¿A qué precio te parecería caro (pero lo comprarías)?"
- "¿A qué precio te parecería tan caro que no lo comprarías?"

Nota: el Van Westendorp tiene limitaciones propias — funciona mejor para productos discretos con precio conocido que para "percepción general de una cadena". Para cadenas de supermercado, la aplicación correcta es por categoría/SKU específico, no por la tienda en general. (Ver Conjointly.com, Van Westendorp documentation, 2024; Sawtoothsoftware.com, 2024).

### 6.2 P31 — Ranking forzado 1-10 de cadenas por precio

### Técnica usada

Ranking forzado donde el respondiente ordena 10 cadenas de "más económica" (1) a "más cara" (10). Métricas: mean rank + % Top-3.

### Veredicto: APROPIADA con caveats de interpretación importantes

**Justificación:** el ranking forzado elimina el problema de la heterogeneidad de escala (distintos respondientes usan distintos "extremos" de una escala Likert) — todos usan exactamente el mismo espacio ordinal 1-10. Es una medida más discriminativa que una escala de rating para comparar posicionamiento relativo entre muchas marcas.

**Caveat crítico de interpretación (documentado en Doc Técnico, bien):** en el ranking forzado, TODA cadena recibe una posición en CADA respondiente — incluyendo cadenas que el respondiente no conoce o no frecuenta. El respondiente que nunca ha ido a Gama igualmente le asigna una posición. Esto introduce ruido significativo: la posición de Gama refleja parcialmente su reputación percibida, no solo la experiencia de precio.

**Alternativa para 2027:** combinar el ranking forzado (para comparativo inter-ola) con una pregunta filtro: "¿En cuáles de estas cadenas has comprado en el último mes?" — y calcular el mean rank SOLO entre los que conocen o han visitado la cadena. Esto daría un rank de "insiders" (más preciso) y un rank "general" (más comparable inter-ola).

### 6.3 P32 — Mejor precio por categoría (single-select)

### Técnica usada

Para cada una de las 15 categorías, el respondiente elige cuál cadena tiene el mejor precio (single-select, incluyendo opción "ninguno en particular"). Clasificación resultante: SENSIBLE / INTERMEDIA / FRAGMENTADA según % líder y % "ninguno".

### Veredicto: APROPIADA — una de las secciones mejor diseñadas del cuestionario

**Justificación:** el diseño forced-choice por categoría produce datos directamente accionables (Gama lidera en X categorías, es segunda en Y, no aparece en Z). La clasificación SENSIBLE/INTERMEDIA/FRAGMENTADA es una heurística analítica robusta y fácil de comunicar a cliente.

**Limitación:** el respondiente elige "mejor precio" basado en percepción, no en compra real. La correlación entre percepción de precio y precio real puede ser baja si la categoría no es KVI. Solución: triangular con auditoría de precios reales (Reflexiones 2027, Rec. 6).

---

## Sección 7 — Regresión logística para drivers de preferencia (faseB_step8)

### Técnica usada

Regresión logística: Y = P21 contiene "Gama" (1/0) ~ P23 × 10 atributos binarios (asociación Gama con cada atributo). Reporta OR + IC 95% + p-value + pseudo R² McFadden = 0.44.

### Veredicto: APROPIADA — la técnica más sofisticada y más valiosa del estudio

**Justificación técnica:**

El logit es la técnica correcta cuando Y es binaria (Hosmer & Lemeshow, 2013, §1). El modelo estima el efecto INDEPENDIENTE de cada atributo sobre la probabilidad de preferencia, controlando por la correlación entre atributos (multicolinealidad). Sin este control, habría atributos que aparecerían como "drivers" simplemente por correlacionar con el driver real — confundiendo la interpretación.

El pseudo R² McFadden de 0.44 es sustancialmente alto para un modelo de drivers en consumer research. Los umbrales estándar son >0.2 para aceptable y >0.4 para robusto (McFadden, 1974; Louviere et al., 2000). Este resultado indica que los 10 atributos de P23 explican una proporción sustancial de la varianza en preferencia por Gama.

**Supuesto del modelo que debe explicitarse:**

1. **Independencia de observaciones:** cada respondiente es una observación. En un diseño de intercepción F2F con rutas aleatorias, este supuesto es razonablemente satisfecho.
2. **No multicolinealidad severa:** atributos como "Limpieza" y "Calidad de los productos" probablemente correlacionan — el logit los controla conjuntamente, pero si la correlación es muy alta (r > 0.8), los SE se inflan y algunos coeficientes se vuelven inestables. Recomendación: verificar matriz de correlaciones entre predictores antes de interpretar.
3. **La relación es lineal en los log-odds:** supuesto estándar del logit. No verificable sin datos, pero es estándar asumir.

**Limitación principal:** el ratio n_Pref-Gama (32) vs n_no-Gama (370) implica que la clase minoritaria es muy pequeña. En logit desbalanceado, los coeficientes tienden a ser más variables (SE más amplios) y el umbral de decisión puede estar sesgado. El Doc Técnico mencionó que el ratio 40:1 está "dentro de lo aceptable" — este juicio es correcto pero merece precisión: el ratio 40:1 (400 obs / 10 predictores) se refiere al criterio de EPV (Events Per Variable) de 10:1 recomendado por Peduzzi et al. (1996). Para n=402 con 10 predictores y 32 casos positivos, el EPV real es 32/10 = 3.2, que está POR DEBAJO del umbral de 10. Esto significa que algunos coeficientes pueden estar sobrestimados (problemas de separación perfecta o cuasi-separación).

### Alerta de escala para Owner

La interpretación de los OR debe ser **direccional**, no cuantitativa exacta, dada la EPV baja. Decir "Atención es el driver más importante de preferencia" es sólido. Decir "Atención multiplica las odds exactamente 5.73 veces" es demasiado preciso para una muestra de n=32 en la clase positiva.

**Alternativa más robusta para 2027:** Key Drivers Analysis con Shapley Value Regression (Lipovetsky & Conklin, 2001; Shapley, 1953). Shapley Values distribuyen la R² total del modelo entre los predictores de manera que controla multicolinealidad sin los problemas del logit con clases desbalanceadas. Es el estándar emergente en brand research (Quirks.com, 2024; RadiusInsights.com, 2024).

Con el booster de Pref-Gama a n=80 (ME-1 §4.2), el EPV sería 80/10 = 8, aún bajo pero más estable. Para logit robusto en drivers, n_positivo ≥ 100 sería el ideal.

---

## Sección 8 — Normalización z-score por marca y por atributo

### Técnica usada

Z-score de dos tipos:
1. Z por marca (perfil interno): z = (val_atributo - mean_marca) / sd_marca — identifica sobre/subíndices de la marca relativa a su propio perfil promedio.
2. Z por atributo (vs competencia): z = (val_marca - mean_atributo) / sd_atributo — identifica marcas que sobreindexan vs el campo en cada atributo.

### Veredicto: APROPIADA — solución elegante a la limitación Likert

**Justificación:** los z-scores extraen señal relativa de datos con baja varianza absoluta (el problema Likert de §3). Son equivalentes a "reescalar" las proporciones para que la comparabilidad sea interna a cada dimensión, no entre dimensiones. Es una práctica estándar en análisis de posicionamiento de marca.

**Limitación:** los umbrales operativos (|z| > 0.7 para "diferenciador real", |z| > 1.0 para "fortaleza fuerte") son convencionales, no estadísticos. No tienen un p-value asociado — no se puede decir "este z es significativamente mayor que cero". Son herramientas descriptivas, no inferenciales.

**Uso apropiado:** para visualización e interpretación de posicionamiento relativo (heatmap del Slide 13), son apropiados. Para fundamentar recomendaciones de inversión ("invertir en atributo X porque su z es +0.8"), son indicativos pero no concluyentes — deben complementarse con el análisis de drivers (logit o Shapley).

---

## Sección 9 — Territorial: correlación Pearson cobertura × preferencia

### Técnica usada

Correlación de Pearson entre número de sucursales Gama por parroquia (variable X, fuente: datos propios Gama) y % preferencia Gama por parroquia (variable Y, fuente: BBDD encuesta, filtrado por parroquias con n≥18). Resultado: r = 0.164, p = 0.651 (no significativo, n = 10 parroquias).

### Veredicto: METODOLÓGICAMENTE CORRECTO, pero de baja potencia estadística

**Justificación del resultado:**

El test fue correctamente especificado (Pearson para relación lineal entre dos variables continuas). El resultado no significativo (p=0.651) es honesto — con n=10 puntos, solo una correlación muy alta (r > 0.60 aprox.) sería detectable al 95% de confianza. Un r=0.164 con ese n no permite concluir ni que existe ni que no existe relación.

**Implicación correctamente interpretada:** "la cobertura física no explica la variación en preferencia" es una afirmación válida en términos descriptivos — la correlación observada es débil. Pero no es evidencia de que NO exista relación — solo de que no se puede demostrar con 10 puntos de datos.

**Alternativa que hubiera incrementado potencia:** un análisis a nivel de zona de influencia de cada sucursal (buffers de 500m, 1km, 2km de radio) con interpolación de preferencia a partir de la BBDD geo-referenciada de los respondientes (si se georeferenció la entrevista). Esto multiplicaría los puntos de datos de 10 parroquias a N sucursales × buffers — potencia estadística sustancialmente mayor. Requeriría GIS y datos de dirección del respondiente.

**Para 2027:** agregar pregunta "¿A cuántos minutos de tu casa queda [Gama preferida]?" → modelo de utilidad espacial (travel time × preferencia).

---

## Sección 10 — Recall publicitario (P35-P42) y El Recreo (P43-P45)

### Técnica usada (recall publicitario)

Recall espontáneo (P35, n=17 base que recuerda) → recall asistido "PRECIOS DE TU LADO" (P37, n=43) y "DE TU LADO SIEMPRE" (P40, n=50). Verbatims codificados en 6 categorías keyword-based.

### Veredicto: APROPIADA para objetivos de diagnóstico preliminar; insuficiente para evaluación formal de campaña

**Justificación:** la secuencia recall espontáneo → asistido es el protocolo estándar de pre-test y post-test publicitario. La escala de bases (4.2% recall espontáneo, 10.7% asistido "PTL", 12.4% asistido "DTLS") produce un diagnóstico claro: awareness de campaña es bajo, con "DE TU LADO SIEMPRE" ligeramente superior.

**Limitación fundamental:** n=17 (espontáneo) y n=43-50 (asistido) son bases muy bajas para conclusiones robustas. El estudio manejó esto con caveats explícitos, lo cual es la respuesta correcta. Pero la pregunta de fondo es: ¿debería incluirse evaluación publicitaria en el mismo cuestionario que el tracker de salud de marca?

**Problema de diseño:** la evaluación publicitaria en el tracker principal contamina el cuestionario (alerta al respondiente de que hay comunicación de Gama) y distorsiona potencialmente las respuestas en secciones posteriores del tracker. El protocolo estándar es separar: tracker de salud de marca en ola independiente de la evaluación de comunicación (pre-test + post-test con exposición controlada). (Copy Testing Best Practices, ARF, 2020).

Para 2027: considerar separar el módulo publicitario del tracker principal, o al menos reordenarlo al final del cuestionario (actualmente ya va al final — eso es correcto).

### Técnica usada (El Recreo, P43-P45)

Módulo filtrado: solo respondientes que frecuentan El Recreo (n=21). Percepción de Gama vs supers de la zona + intención de compra si Gama abre.

### Veredicto: APROPIADA como módulo exploratorio, con caveat de base baja bien documentado

El módulo es metodológicamente correcto dado que fue solicitado específicamente por Cora y se reportó con caveats claros. La base n=21 hace que cualquier porcentaje tenga m.e. ±21.3% — por eso el análisis es cualitativo/indicativo. No hay alternativa metodológica sin más campo específico en El Recreo.

---

## Sección 11 — Análisis de coincidencia P21×P24 (preferida vs última compra)

### Técnica usada

Match directo entre nombre de marca en P21 (preferida) y P24 (última lugar de compra), con normalización de nombres. % de coincidencia por segmento.

### Veredicto: APROPIADA como proxy de "loyal share of wallet"

**Justificación:** la no-coincidencia entre marca preferida y lugar de última compra es un indicador directo de que el shopper tiene una preferencia declarada pero no la actúa — es "loyal attitude, not loyal behavior." Este gap es estratégicamente valioso (los "11 perdidos a Páramo de mercado grande" en preferentes-Gama son oportunidad cuantificada).

**Limitación:** una sola compra (la última) no refleja el patrón habitual. Si el shopper va a Gama 3 veces al mes y a Páramo 1 vez (para el mercado grande), la coincidencia depende de cuándo fue la última compra. Esto es el argumento para medir frecuencia × ticket (ME-1 §5.2, brecha señalada).

---

## Sección 12 — Codificación de verbatims (razones de preferencia P21.1)

### Técnica usada

Categorización manual de respuestas abiertas en 6-8 categorías keyword-based. Sin cálculo formal de confiabilidad entre codificadores (inter-rater reliability).

### Veredicto: APROPIADA para el volumen y plazo; debería formalizarse en 2027

**Justificación:** para n=402 verbatims, la codificación manual es la técnica más eficiente. Las categorías emergentes son relevantes y las frecuencias producen insights claros (Buena atención 53.1% en preferentes-Gama).

**Limitación:** sin confiabilidad entre codificadores (Cohen's Kappa), no se puede afirmar que otro analista produciría las mismas categorías con la misma frecuencia. Para un estudio de investigación formal, se requiere al menos un segundo codificador independiente y reporte de Kappa ≥ 0.70 (Landis & Koch, 1977).

**Para 2027:** si el volumen de verbatims permite, implementar doble codificación en una muestra aleatoria del 20% para validar. Alternativamente, usar NLP con verificación manual en categorías ambiguas. Modelos de topic modeling (LDA o BERTopic) pueden proporcionar categorías sin sesgo de hipótesis previa.

---

## 13. Hallazgos críticos para Owner

Hay un conjunto de decisiones analíticas que, aunque técnicamente defensibles, merecen atención específica del Owner antes de que sus conclusiones se usen en decisiones de inversión:

### Hallazgo crítico 1 — EPV bajo en regresión logística

Como se documentó en §7, el EPV (Events Per Variable) real en el logit de drivers es 3.2 (32 casos positivos / 10 predictores). El umbral recomendado en la literatura es EPV ≥ 10 (Peduzzi et al., 1996, *Journal of Clinical Epidemiology*, 49(12), 1373-1379). Con EPV bajo, algunos OR pueden estar sobrestimados.

**Recomendación:** los OR del logit deben presentarse a Cora con el caveat explícito de que son "indicaciones direccionales". No recomendar a Gama una inversión específica en un atributo basándose SOLO en el OR sin cruzar con el z-score y la importancia declarada. La convergencia de los tres métodos para Atención (§5) sí es suficientemente robusta para soportar una recomendación.

**Decisión Owner requerida:** si el OR de algún atributo de la regresión logística se presentó como un número exacto en el deck de Cora sin el caveat de EPV, el Owner puede querer añadir una nota aclaratoria en futuras comunicaciones. No es una falla que invalide el hallazgo de Atención como driver, pero sí debe manejarse con transparencia.

### Hallazgo crítico 2 — Comparabilidad inter-ola no está formalmente validada

El comparativo 2025→2026 asume que las diferencias observadas reflejan cambios reales en la salud de marca, pero no se ha documentado si:
- El cuestionario 2025 tenía exactamente la misma formulación en los ítems comparados.
- Las condiciones de fieldwork (fecha de campo, clima económico, eventos externos) fueron comparables.
- El perfil NSE y geográfico de la muestra 2025 (n=785) y 2026 (n=402) es suficientemente similar para hacer comparación directa.

El estudio reportó las diferencias con test de significancia inter-ola (z-test), lo cual es correcto. Pero la interpretación de las diferencias como "cambio de mercado" requiere que se descarten explicaciones alternativas (diferente momento del año, diferente composición de muestra).

**Recomendación:** agregar en el deck V2, en la slide de tendencias, un disclaimers: "Las diferencias inter-ola se reportan con test de significancia estadística. La interpretación como cambio real de mercado asume que las condiciones de fieldwork y el perfil muestral fueron suficientemente comparables entre olas."

### Hallazgo crítico 3 — Likert plano en P22 hace que la "importancia" del atributo no sea comparable con la "asociación"

La matriz de posicionamiento (importancia × asociación) que aparece en la slide de posicionamiento (C3 del deck) combina en sus dos ejes variables de distinta calidad:
- Eje X (importancia): derivada de Likert saturado — baja discriminación real
- Eje Y (asociación): derivada de multi-select binario — discriminación razonable

La interpretación habitual de "atributos en el cuadrante alta importancia / baja asociación → brechas prioritarias" puede estar distorsionada porque el eje de importancia no discrimina bien. Los atributos en la "zona de brecha" podrían estar ahí solo porque el Likert sobreestimó su importancia.

**Recomendación para Cora:** advertir que la accionabilidad de la matriz de posicionamiento depende de cuánto se crea en la importancia declarada. Si se confía más en los OR del logit (importancia derivada), el orden de prioridad de atributos puede ser distinto al sugerido por la matriz.

---

## 14. Tabla resumen — Veredictos por técnica

| Técnica | Veredicto | Acción recomendada 2027 |
|---|---|---|
| Notoriedad espontánea/asistida (P16/P17) | APROPIADA | Mantener. Agregar CEPs específicos. |
| Embudo de marca (P16-P21) | APROPIADA con matices | Mantener + agregar penetración 12m |
| Importancia atributos Likert (P22) | INAPROPIADA para el objetivo | Reemplazar con MaxDiff |
| Asociación marca×atributo binario (P23) | APROPIADA | Mantener |
| Regresión logística drivers (Fase B) | APROPIADA — mejor técnica del estudio | Mantener + Shapley para 2027 + booster n |
| Normalización z-score | APROPIADA | Mantener como complemento |
| Ranking forzado precio (P31) | APROPIADA con caveats | Mantener + filtro "conoce la cadena" |
| Percepción precio ordinal (P33) | APROPIADA parcialmente | Mantener + Van Westendorp en KVIs |
| Mejor precio por categoría (P32) | APROPIADA | Mantener |
| Territorial correlación Pearson | APROPIADA, baja potencia | Para 2027: análisis espacial por sucursal |
| Recall publicitario (P35-P42) | APROPIADA para diagnóstico preliminar | Considerar separar del tracker principal |
| Coincidencia P21×P24 | APROPIADA como proxy | Complementar con frecuencia + ticket |
| Codificación verbatims | APROPIADA, sin validación formal | Formalizar inter-rater reliability |

---

## 15. Referencias metodológicas citadas en este memo

- Aaker, D.A. (1991). *Managing Brand Equity*. Free Press.
- ARF (2020). *Copy Testing Best Practices*. Advertising Research Foundation.
- Hosmer, D.W., & Lemeshow, S. (2013). *Applied Logistic Regression*, 3rd ed. Wiley.
- Keller, K.L. (2013). *Strategic Brand Management*, 4th ed. Prentice Hall.
- Landis, J.R., & Koch, G.G. (1977). The Measurement of Observer Agreement for Categorical Data. *Biometrics*, 33(1), 159-174.
- Lipovetsky, S., & Conklin, M. (2001). Analysis of Regression in Game Theory Approach. *Applied Stochastic Models in Business and Industry*, 17(4), 319-330.
- Louviere, J.J., Flynn, T.N., & Marley, A.A.J. (2015). *Best-Worst Scaling: Theory, Methods and Applications*. Cambridge University Press.
- Louviere, J.J., Hensher, D.A., & Swait, J.D. (2000). *Stated Choice Methods: Analysis and Application*. Cambridge University Press.
- McFadden, D. (1974). Conditional Logit Analysis of Qualitative Choice Behavior. En Zarembka, P. (ed.), *Frontiers in Econometrics*, 105-142. Academic Press.
- Orme, B.K. (2019). *Getting Started with Conjoint Analysis*, 4th ed. Research Publishers LLC.
- Paulhus, D.L. (1991). Measurement and Control of Response Bias. En Robinson, J.P. et al. (eds.), *Measures of Personality and Social Psychological Attitudes*, 17-59. Academic Press.
- Peduzzi, P., Concato, J., Kemper, E., Holford, T.R., & Feinstein, A.R. (1996). A Simulation Study of the Number of Events per Variable in Logistic Regression Analysis. *Journal of Clinical Epidemiology*, 49(12), 1373-1379.
- Quirks.com (2024). Applying the Shapley Value Method to Marketing Research. [quirks.com/articles/applying-the-shapley-value-method-to-marketing-research]
- Reichheld, F.F. (2003). The One Number You Need to Grow. *Harvard Business Review*, 81(12), 46-54.
- Romaniuk, J. (2023). *Better Brand Health*. Oxford University Press / Ehrenberg-Bass Institute.
- Sharp, B. (2010). *How Brands Grow*. Oxford University Press.
- Shapley, L.S. (1953). A Value for N-Person Games. *Contributions to the Theory of Games*, 2, 307-317. Princeton University Press.
- Van Westendorp, P. (1976). NSS-Price Sensitivity Meter (PSM) — A New Approach to Study Consumer Perception of Price. ESOMAR Congress Papers.

---

*Fin del ME-3 — Methodology Selection Rationale v1*
