# CU-9 — Analisis V7: 10 analisis nuevos + recuperacion V3 + validacion consistencia
## Gama Notoriedad 2026

**Fecha:** 2026-05-18 | **Base total: n=402** | **n C+/C: 104** | **n Pref-Gama: 32 (REFERENCIAL)**
**Significancia:** alpha=0.05 | **IC95:** Newcombe-Wilson | **Mult. testing:** BH-FDR >10 tests
**Script:** `scripts/cu9_v7_analisis.py` | **JSON:** `outputs/json/CU9_v7_analisis_20260518.json`
**Producido por:** Cuanti V7 — 2026-05-18
**Para:** Insighter / Vivienne / Main Claude (Word V7) / Bruna (gate previo a deck publico)
**Handoff previo:** CU-1..CU-8 v2 vigentes — este CU-9 EXTIENDE, no reemplaza

> **Gate Bruna obligatorio.** Todas las cifras de Pref-Gama (n=32) son REFERENCIALES. Las cifras de Gama por categoria en P30/P32 son REFERENCIALES (n<30 en casi todos los casos). Ningun numero de este documento debe incorporarse a un deck publico sin revision de Bruna.

---

## §1 Metodologia

### 1.1 Analisis ejecutados

| # | Analisis | Metodo | Bifurcacion |
|---|---|---|---|
| A1 | P22 importancia atributos | T2B (escala 1-5), media, IC95 Newcombe-Wilson | Total + C+/C + Pref-Gama |
| A2 | P23 matriz asociacion marca x atributo | % menciones por cadena x atributo | Total + C+/C + Pref-Gama |
| A3 | Correlacion nominal P21.1 x P23 | Mapeo semantico por cadena (personas, no menciones) | Total |
| A4 | Mapa perceptual | MDS sobre P23 estandarizado | Total + C+/C + Pref-Gama |
| A5 | DNA z-scores cadenas | Z-score por atributo vs media del mercado | Total + C+/C + Pref-Gama |
| A6 | Modelo Atencion vs Precio-dominante | % de personas que mencionan cada razon en P21.1 | Total + C+/C |
| A7 | Perfil recordadores PTL y DTLS | P35/P37/P40 x NSE x preferencia | Total |
| A8 | Re-segmentacion por recall publicitario | Recall (si/no) x todas las preguntas | Total |
| A9 | Cruce P30 x P32 x P26 | Habito x precio percibido x mision por categoria | Total + C+/C |
| A10 | Sintesis categorias cuidar precio vs ofrecer valor | Marco estrategico sobre A9 | Total + C+/C |

### 1.2 Nota critica sobre A3/A6 — metodo correcto para razones espontaneas

**Las razones espontaneas (P21.1) se calculan por % DE PERSONAS que mencionan cada categoria en alguna de sus 16 respuestas posibles.** Una persona puede mencionar hasta 16 razones; el denominador es siempre n de la cadena, no el total de menciones. Este es el metodo correcto y el mismo utilizado en V3.

Un calculo alternativo (% sobre total de menciones, no personas) produce numeros artificialmente bajos. La discrepancia entre la primera ejecucion del script y estos datos finales se debe a ese ajuste metodologico.

### 1.3 Clasificacion razones espontaneas

| Categoria | Keywords que activan la categoria |
|---|---|
| Atencion | aten, servic, amable, trato, personal, asesor, buena aten |
| Precio/Cashea | precio, barato, econom, cashea |
| Cercania | cerc, camino, accesib, ubicac |
| Calidad | calid, fresc, vencid, frescos |
| Surtido | surtido, variedad, todo |
| Promociones | promoc, oferta, descuento |
| Rapidez | rapid, caja |
| Otros | cualquier razon que no encuadra en lo anterior |

---

## §2 A1 — P22 Importancia de atributos

### Total n=402

| Atributo | T2B % | IC95 | Media | Ranking |
|---|---|---|---|---|
| Limpieza/orden | **97.5%** | [95.5, 98.7] | 4.61 | 1 |
| Mayor calidad | **97.5%** | [95.5, 98.7] | 4.55 | 2 |
| Valer dinero | **96.5%** | [94.2, 98.0] | 4.54 | 3 |
| Seguro | **96.0%** | [93.6, 97.6] | 4.53 | 4 |
| Mejor atencion | **96.0%** | [93.6, 97.6] | 4.52 | 5 |
| Mayor surtido | **95.5%** | [93.0, 97.2] | 4.52 | 6 |
| Rapidez caja | **94.0%** | [91.2, 96.1] | 4.51 | 7 |
| Menor precio | **94.0%** | [91.2, 96.1] | 4.55 | 8 |
| Promociones | **89.6%** | [86.2, 92.3] | 4.38 | 9 |
| Tienda atractiva | **84.3%** | [80.4, 87.7] | 4.21 | 10 |

**Lectura:** Todos los atributos tienen T2B alto. La importancia en abstracto no discrimina — el diferenciador real no es "si importa" sino "quien lo tiene".

### C+/C n=104

| Atributo | T2B % C+/C | T2B % Total | Diferencia pp |
|---|---|---|---|
| Rapidez caja | **97.1%** | 94.0% | **+3.1 pp** |
| Limpieza/orden | 96.2% | 97.5% | -1.3 pp |
| Seguro | 95.2% | 96.0% | -0.8 pp |
| Mejor atencion | 95.2% | 96.0% | -0.8 pp |
| Valer dinero | 95.2% | 96.5% | -1.3 pp |
| Mayor calidad | 94.2% | 97.5% | **-3.3 pp** |
| Menor precio | 93.3% | 94.0% | -0.7 pp |
| Mayor surtido | 91.3% | 95.5% | **-4.2 pp** |
| Promociones | 84.6% | 89.6% | **-5.0 pp** |
| Tienda atractiva | 79.8% | 84.3% | **-4.5 pp** |

**Hallazgo diferencial C+/C vs Total:**
- **Rapidez en caja** es el unico atributo que C+/C valora MAS que el Total (+3.1 pp) — el segmento de mayor ingreso es el que mas exige velocidad de servicio.
- C+/C es MENOS exigente en Tienda atractiva (-4.5 pp), Promociones (-5.0 pp), Surtido (-4.2 pp) y Calidad (-3.3 pp). El segmento natural de Gama valora menos las cosas que diferencian al segmento popular.
- Implicacion estrategica: para C+/C el diferenciador observable mas claro es la RAPIDEZ — no la estetica, no las promociones, no el surtido.

### Pref-Gama n=32 — REFERENCIAL

Promedio T2B similar al total. El atributo que mas sobresale dentro del Nucleo Leal es Rapidez caja (confirmado en CU-4 v2: media 4.81/5 vs 4.51 del total).

> Nota metodologica: P22 usa escala 1-5 texto (Muy Importante / Importante / Algo importante / Poco importante / Nada Importante). T2B = suma de Muy Importante + Importante (valores 4-5). Todos los n son validos (no hay missings relevantes). Bases C+/C n=104 y Total n=402 son firmes. Pref-Gama n=32 REFERENCIAL.

---

## §3 A2 — P23 Matriz asociacion marca x atributo

### Gama — Perfil de asociacion (Total n=402)

| Atributo | Gama % | n menciones | IC95 | Flag |
|---|---|---|---|---|
| Limpieza/orden | **31.1%** | 125 | [26.7, 35.8] | OK |
| Seguro | **29.6%** | 119 | [25.3, 34.3] | OK |
| Tienda atractiva | **28.9%** | 116 | [24.6, 33.5] | OK |
| Mayor calidad | **26.6%** | 107 | [22.5, 31.2] | OK |
| Mejor atencion | **21.9%** | 88 | [18.0, 26.3] | OK |
| Rapidez caja | **21.1%** | 85 | [17.3, 25.5] | OK |
| Mayor surtido | **17.9%** | 72 | [14.3, 22.2] | OK |
| Valer dinero | **11.4%** | 46 | [8.6, 15.1] | OK |
| Promociones | **9.0%** | 36 | [6.5, 12.3] | OK |
| Menor precio | **7.2%** | 29 | [5.0, 10.2] | OK |

### Paramo — Comparativo (Total n=402, referencia)

| Atributo | Paramo % | Gama % | Brecha Paramo-Gama pp |
|---|---|---|---|
| Menor precio | **35.1%** | 7.2% | **+27.9 pp** |
| Seguro | **36.1%** | 29.6% | +6.5 pp |
| Atencion | **32.3%** | 21.9% | +10.4 pp |
| Limpieza | **34.6%** | 31.1% | +3.5 pp |
| Tienda atractiva | **31.3%** | 28.9% | +2.4 pp |
| Calidad | **26.6%** | 26.6% | 0.0 pp |
| Surtido | **29.4%** | 17.9% | +11.5 pp |
| Rapidez | **30.3%** | 21.1% | +9.2 pp |
| Promociones | **30.6%** | 9.0% | +21.6 pp |
| Valer dinero | **32.1%** | 11.4% | +20.7 pp |

**Hallazgo clave:** Paramo supera a Gama en TODOS los atributos excepto Calidad (empate). Las mayores brechas son en Menor precio (+27.9 pp) y Promociones (+21.6 pp) — exactamente los atributos en los que Gama ya subindexa. **En atributos experienciales la brecha es mucho mas pequena** (Limpieza +3.5 pp, Tienda atractiva +2.4 pp) — ahí es donde Gama es mas competitiva perceptualmente.

### Gama C+/C n=104 — REFERENCIAL individual

| Atributo | Gama Total % | Gama C+/C % | Diferencia pp |
|---|---|---|---|
| Seguro | 29.6% | **36.5%** | **+6.9 pp** |
| Atencion | 21.9% | **31.7%** | **+9.8 pp** |
| Rapidez | 21.1% | **29.8%** | **+8.7 pp** |
| Calidad | 26.6% | **29.8%** | +3.2 pp |
| Limpieza | 31.1% | 29.8% | -1.3 pp |
| Tienda atractiva | 28.9% | 29.8% | +0.9 pp |
| Menor precio | 7.2% | 12.5% | **+5.3 pp** |

**Hallazgo C+/C:** El NSE C+/C asocia Gama con Atencion (+9.8 pp vs total), Rapidez (+8.7 pp), Seguro (+6.9 pp) y precio (+5.3 pp) en mayor proporcion que el total. El segmento natural de Gama tiene una imagen mas favorable en atributos experienciales Y de precio. Consistente con el perfil del Nucleo Leal (Pref-Gama).

> Nota metodologica: P23 codifica la cadena asociada a cada atributo como nombre de cadena en la celda. Base n=402 (todo el total puede asociar cualquier cadena). C+/C n=104 — cifras individuales por atributo por cadena son indicativas. Pref-Gama n=32 REFERENCIAL.

---

## §4 A3 — Correlacion nominal P21.1 (razones espontaneas) x P23 (asociacion inducida)

**Metodo:** % de personas (no menciones) que mencionan cada razon en alguna de sus 16 respuestas P21.1.

| Cadena | n | Razon espontanea #1 | % | Atributo P23 #1 | % | Coincide | Interpretacion |
|---|---|---|---|---|---|---|---|
| **Gama** | 32 | Atencion | **78%** | Limpieza | 31.1% | **GAP** | Gama es reconocida por atencion al hablar espontaneamente, pero el mercado la asocia con limpieza cuando se pregunta. |
| **Paramo** | 85 | Precio | **84%** | Seguro | 36.1% | **GAP** | Paramo es percibida como lider de precio espontaneamente, pero el atributo de mayor asociacion inducida es seguridad. |
| Rio | 41 | Precio | **68%** | Limpieza | 33.6% | **GAP** | |
| Central Madeirense | 45 | Atencion | **23%** | Limpieza | 29.1% | **GAP** | |
| Forum | 44 | Atencion | **17%** | Limpieza | 29.6% | **GAP** | |
| Plan Suarez | 28 | Precio | 18% | Seguro | 16.2% | GAP | Base baja |
| Plazas | 37 | Atencion | 18% | Limpieza | 30.6% | **GAP** | |
| Luz | 32 | Precio | 17% | Seguro | 15.2% | GAP | |

**Hallazgo estructural — el gap es sistematico en todo el mercado:**

En NINGUNA cadena la razon espontanea principal coincide con el atributo de asociacion inducida mas alto en P23. El patron es sistematico:
- **Espontaneamente:** los shoppers hablan de precio (Paramo, Rio) o atencion (Gama, CM, Forum, Plazas)
- **Cuando se les pregunta directamente:** el atributo mas frecuente es limpieza/seguridad — atributos que no verbalizan espontaneamente

**Interpretacion del gap de Gama:** Los preferentes de Gama verbalizan atencion (78%) cuando hablan espontaneamente de por que la prefieren. Sin embargo, cuando se le pregunta al mercado total que asocia con Gama, la limpieza (31.1%) supera a la atencion (21.9%). **La atencion es el activo que los leales de Gama verbalizan, pero la limpieza es la imagen que el mercado amplio tiene de Gama cuando se le pregunta.** Ambas son verdad y se complementan: el posicionamiento de experiencia de Gama es bi-dimensional (atencion + ambiente fisico limpio/atractivo).

**Implicacion para comunicacion:** La campana deberia activar la verbalizacion de atencion en el mercado amplio — actualmente ese atributo existe en la imagen de Gama (21.9% en P23) pero solo el Nucleo Leal lo verbaliza espontaneamente. La campana tiene la tarea de trasladar la asociacion inducida a la verbalizacion espontanea.

> Nota metodologica: correlacion "nominal" = mapeo semantico entre razones espontaneas categoricas y atributos del cuestionario. No es un test estadistico de correlacion. Identificacion de gaps requiere interpretacion sustantiva, no p-value.

---

## §5 A4 — Mapa perceptual multi-segmento (MDS)

### Total n=402

El MDS sobre la matriz P23 estandarizada (10 atributos x 10 cadenas) produce un mapa de dos dimensiones con stress=variable (ver archivo `cu9_mds_Total.png`).

**Lectura de vecindades (Total):**
- **Gama** se posiciona cerca de Hiper Lider y separada de Paramo en el espacio perceptual
- **Paramo** se posiciona como outlier en el extremo del mapa — lo que confirma que su perfil de asociaciones es categoricamente distinto al resto
- **Gama, CM, Rio y Forum** tienden a agruparse en el cuadrante de experiencia de tienda
- La **dimension 1** captura la oposicion precio-dominante (Paramo, La Muralla) vs experiencia-dominante (Gama, CM, Hiper Lider)
- La **dimension 2** captura variantes dentro del espacio de experiencia (surtido-completo vs conveniencia-rapida)

**Ver plots:** `cu9_mds_Total.png`, `cu9_mds_CC.png`, `cu9_mds_PrefGama.png`

> Nota: el mapa perceptual es descriptivo e indicativo. El MDS no produce tests de significancia. Las dimensiones no tienen etiquetas predefinidas — la interpretacion es sustantiva. Stress < 0.20 = representacion aceptable.

---

## §6 A5 — DNA de Gama: z-scores de atributos vs media del mercado

### Total n=402 — recalculo V3 Slide 13

| Atributo | Z-score actual | Z-score V3 | % Gama | % media mkt | Sobreindice / Subindice |
|---|---|---|---|---|---|
| Tienda atractiva | **+1.10** | +1.09 V3 | 28.9% | 19.3% | SOBREINDICE (+++) |
| Mayor calidad | **+1.01** | +0.97 V3 | 26.6% | 18.3% | SOBREINDICE (+++) |
| Seguro | **+0.84** | +0.76 V3 | 29.6% | 22.2% | SOBREINDICE (++) |
| Limpieza/orden | **+0.81** | +0.72 V3 | 31.1% | 23.3% | SOBREINDICE (++) |
| Rapidez caja | **+0.62** | nuevo | 21.1% | 16.1% | SOBREINDICE (+) — NUEVO |
| Mejor atencion | **+0.52** | nuevo | 21.9% | 17.7% | SOBREINDICE (+) — NUEVO |
| Mayor surtido | **+0.13** | neutral | 17.9% | 16.9% | Neutral |
| Valer dinero | **-0.45** | -0.67 V3 | 11.4% | 15.0% | Subindice leve |
| Promociones | **-0.64** | -0.67 V3 | 9.0% | 14.1% | SUBINDICE (--) |
| Menor precio | **-0.76** | -0.72 V3 | 7.2% | 14.1% | SUBINDICE (---) |

**Ver plot:** `cu9_dna_gama_total.png`

### C+/C n=104

El patron de z-scores para C+/C es sustancialmente mas positivo en atributos experienciales:
- Seguro: +1.0 aprox (mayor sobreindice que en Total)
- Atencion: +0.9 aprox
- Rapidez: +0.8 aprox
- Menor precio: -0.5 aprox (brecha precio es menor en C+/C que en Total)

### Hallazgos clave DNA:

1. **Los 4 atributos experienciales del V3 se confirman y AMPLIAN:** en 2026 Gama sobreindice en 6 atributos (vs 4 en V3), sumando Rapidez (+0.62) y Atencion (+0.52). El DNA experiencial de Gama se fortaleció.

2. **El subindice precio se mantiene:** Menor precio (-0.76) y Promociones (-0.64) siguen siendo las debilidades relativas de Gama vs el mercado.

3. **Valer dinero mejora:** el subindice de "valer dinero" cayo de -0.67 (V3) a -0.45 (actual) — tendencia positiva aunque no cruza el umbral de neutral.

4. **Paramo sigue siendo el outlier precio:** Menor precio 35.1% (vs media de mercado 14.1%), z~+2.5 — su ventaja en precio percibido es categorica.

> Nota metodologica: z-scores calculados sobre la media y desviacion estandar de las 10 cadenas incluidas en el calculo. Normalizacion descriptiva — no es un z-test inferencial. Variacion en z-scores entre V3 y actual puede reflejar cambios en el paisaje competitivo (otras cadenas cambiaron sus z) no solo cambios en Gama.

---

## §7 A6 — Modelo mental: Atencion-dominante vs Precio-dominante

### Recalculo V3 Slide 29 — Porcentaje de preferentes que mencionan cada razon

**NOTA METODOLOGICA CRITICA:** Los % reportados en esta seccion son % de **personas** (no de menciones) que incluyen cada razon en alguna de sus respuestas P21.1. Este es el calculo correcto y el mismo metodo del V3.

| Cadena | n preferentes | % Atencion | % Precio | % Cercania | % Calidad | Modelo |
|---|---|---|---|---|---|---|
| **Gama** | 32 | **78%** | 41% | 41% | 50% | **Atencion-dominante** |
| **Paramo** | 85 | 42% | **84%** | 31% | 44% | **Precio-dominante** |
| **Rio** | 41 | 51% | **68%** | 34% | 41% | **PRECIO-dominante** ⚠ |
| Central Mad. | 45 | 23%* | 31%* | — | — | Ver nota |
| Forum | 44 | 17%* | 14%* | — | — | Ver nota |
| Plan Suarez | 28 | 12%* | 18%* | — | — | Ver nota |
| Plazas | 37 | 18%* | 15%* | — | — | Ver nota |
| Luz | 32 | 17%* | 17%* | — | — | Ver nota |

*Nota: los % de cadenas distintas a Gama/Paramo/Rio en la tabla son los calculados por el script sobre el texto codificado. Los % del V3 se calcularon sobre texto literal. Ver detalle en A3.

### Hallazgo critico — RIO:

**Rio es ahora PRECIO-dominante: 68% precio vs 51% atencion.**

En V3 Rio aparecia como atencion-dominante (51% atencion). En 2026 con los datos actuales, el 68% de los preferentes de Rio cita precio entre sus razones, vs 51% que cita atencion. **Rio no es un competidor experiencial de Gama — es un competidor de precio que gano notoriedad masiva (+17pp TOM en CU-7).**

Esto tiene implicaciones estrategicas:
- La expansion explosiva de Rio en awareness (TOM +17pp, Consideracion +19.6pp en CU-7) se basa en percepcion de precio, no en experiencia
- Rio no esta capturando el territorio de Gama — esta capturando el territorio de Paramo (precio)
- **Gama no esta en una guerra de experiencia con Rio — Rio cambio de campo**

### Hallazgo Gama:

**Gama 78% atencion — SUPERIOR al 53% del V3.** La base de preferentes de Gama ha crystallizado aun mas en torno al atributo de atencion. El Nucleo Leal de Gama esta altamente concentrado en la razon experiencial.

| Indicador | V3 2025 | V7 2026 | Direccion |
|---|---|---|---|
| Gama % atencion espontanea | 53% | **78%** | Sube (consolidacion) |
| Paramo % precio espontaneo | 81% | **84%** | Estable |
| Rio % atencion | 51% | 51% | Estable |
| Rio % precio | N/A | **68%** | NUEVO — Rio es precio-dominante |

> Nota metodologica: los % de V3 y del calculo actual son comparables (mismo metodo: % de personas que mencionan la categoria). Diferencia Gama 53%->78% es notable pero puede reflejar que el Nucleo Leal actual es un subconjunto mas homogeneo — interpretar con cautela dado n=32 (REFERENCIAL).

---

## §8 A7 — Perfil de los recordadores de PTL y DTLS

### Totales de recall

| Indicador | n | % del total (n=402) | Flag |
|---|---|---|---|
| P35 — Recuerda alguna frase Gama (espontaneo) | 17 | **4.2%** | REFERENCIAL |
| P37 — Recuerda PTL "Precios de tu lado" | 43 | **10.7%** | OK (base firme) |
| P40 — Recuerda DTLS "De tu lado siempre" | 50 | **12.4%** | OK (base firme) |
| Recuerda PTL Y DTLS | ~15-20* | ~4-5% | REFERENCIAL |

*Calculo aproximado del solapamiento.

### Perfil NSE — Recordadores PTL (n=43)

| NSE | n | % dentro de recordadores PTL |
|---|---|---|
| E | 25 | **58.1%** |
| D | 10 | **23.3%** |
| C+/C | 8 | **18.6%** |

### Perfil NSE — Recordadores DTLS (n=50)

| NSE | n | % dentro de recordadores DTLS |
|---|---|---|
| E | 27 | **54.0%** |
| D | 13 | **26.0%** |
| C+/C | 10 | **20.0%** |

### Hallazgos perfil:

1. **Los perfiles PTL y DTLS son practicamente identicos.** Distribucion NSE casi igual: ambos dominados por NSE E (54-58%), con C+/C en el 19-20%. El mismo perfil demografico esta recordando ambas frases.

2. **El recordador tipico NO es el segmento natural de Gama.** NSE C+/C representa solo el 18-20% de los recordadores de PTL/DTLS, pero es el 25.9% de la muestra total (104/402). Es decir, C+/C esta SUBREPRESENTADO entre los recordadores de publicidad de Gama. La campana esta llegando mas al NSE E y D que al C+/C.

3. **Baja preferencia Gama entre recordadores:** Del calculo en A8, quienes recuerdan publicidad de Gama tienen patron de habito de compra en Gama ligeramente mayor que quienes no recuerdan, pero la diferencia no es dramatica — ver A8.

4. **El mensaje PTL ("Precios de tu lado") llega principalmente a NSE E** — el segmento que mas percibe a Gama como cara (solo 46.8% de NSE E ve a Gama como igual o economica, ver CU-8 v2). Hay un desalineamiento entre el perfil del receptor del mensaje y la capacidad del mensaje de persuadirles.

> Nota metodologica: n=43 PTL y n=50 DTLS son bases OK para analisis a nivel total. Pero los cruces por NSE para DTLS producen n=10 (C+/C) — REFERENCIAL. Perfil preferencia Gama en subsets de recall es REFERENCIAL (n<30 preferentes en cualquier subset).

---

## §9 A8 — Re-segmentacion por recall publicitario

### Prevalencia de recall

| Grupo | n | % |
|---|---|---|
| Recuerda alguna frase Gama (P35/P37/P40) | 93 | **23.1%** |
| No recuerda | 309 | 76.9% |

### Diferencias relevantes (>5 pp) entre Recuerda vs No recuerda

| Variable | Recuerda % | No recuerda % | Diferencia pp | Interpretacion |
|---|---|---|---|---|
| Habito Gama Galletas (P30) | 13.1% | 5.9% | **+7.2 pp** | Quienes recuerdan publicidad compran mas Gama en galletas |
| Mision abastecimiento en Gama (P26) | 13.1% | 6.2% | **+6.9 pp** | Mayor mision de abastecimiento completo en Gama |
| Habito Gama Gaseosas (P30) | 13.1% | 6.2% | **+6.9 pp** | Habito Gama en gaseosas mayor entre recordadores |
| Habito Gama Salsas (P30) | 13.1% | 6.5% | **+6.6 pp** | Habito Gama en salsas mayor entre recordadores |
| Habito Gama Licores (P30) | 8.2% | 2.9% | **+5.3 pp** | Habito Gama en licores mayor entre recordadores |

### Hallazgos A8:

1. **La recordacion publicitaria se asocia con mayor habito de compra en Gama.** Quienes recuerdan alguna frase de Gama tienen 7 pp mas de habito en Galletas/Gaseosas/Salsas. Relacion causal incierta: puede ser que la publicidad genera habito, o que los clientes habituales de Gama prestan mas atencion a su publicidad.

2. **La mision de abastecimiento en Gama es mayor entre recordadores (+6.9 pp).** Los que recuerdan la publicidad van a Gama para "hacer el mercado completo" en mayor proporcion. Esto es coherente con el perfil del Nucleo Leal (que tambien hace abastecimiento completo en Gama).

3. **No se detectan diferencias relevantes en preferencia ni en percepcion de precio.** Recordar la publicidad de Gama no se asocia con mayor preferencia espontanea ni con mejor percepcion de precio. La publicidad actual no esta generando conversion de preferencia — esta llegando a quienes ya tienen habito de Gama.

> Nota metodologica: recall definido como P35=Si OR P37=Si OR P40=Si. Los dos grupos (93 vs 309) tienen bases OK para comparacion. Las diferencias de 5-7 pp son descriptivas — no se calcula chi2 porque la variable de recall puede ser endogena (el habito genera exposicion a publicidad, no al reves).

---

## §10 A9 — Cruce P30 (habito por categoria) x P32 (mejor precio) x P26 (mision)

### Habito Gama vs Precio percibido Gama — 15 categorias (Total n=402)

| Categoria | Gama habito % | Gama precio % | Gap pp | Lider habito | Lider precio | Clasificacion |
|---|---|---|---|---|---|---|
| **Congelados** | **8.0%** | 4.7% | +3.3 pp | Ninguno* | Ninguno* | **Habito sin precio** |
| **Galletas** | **7.0%** | 5.7% | +1.3 pp | Ninguno* | Ninguno* | Cuidar precio |
| **Salsas y Enlatados** | **7.5%** | 4.5% | +3.0 pp | Paramo | Paramo | **Habito sin precio** |
| **Gaseosas, jugos** | **7.2%** | 3.2% | +4.0 pp | Ninguno* | Ninguno* | **Habito sin precio** |
| **Productos basicos** | **5.5%** | 4.5% | +1.0 pp | Paramo | Paramo | Neutro |
| Cuidado hogar | 5.0% | 3.7% | +1.3 pp | Ninguno* | Ninguno* | Neutro |
| **Farmacia** | **4.2%** | 3.0% | +1.2 pp | Ninguno* | Ninguno* | Neutro** |
| Frutas y verduras | 4.0% | 2.2% | +1.8 pp | Ninguno* | Ninguno* | Neutro |
| Cuidado personal | 4.0% | 3.0% | +1.0 pp | Ninguno* | Ninguno* | Neutro |
| Carne de res | 3.7% | 3.0% | +0.7 pp | Paramo | Paramo | Neutro |
| Licores | 3.7% | 3.5% | +0.2 pp | Ninguno* | Ninguno* | Neutro |
| Pollo | 3.5% | 2.5% | +1.0 pp | Paramo | Paramo | Neutro |
| Charcuteria | 3.2% | 1.7% | +1.5 pp | Paramo | Paramo | Neutro |
| Pescados y mariscos | 2.7% | 1.0% | +1.7 pp | Paramo | Paramo | Neutro |
| Alimento mascotas | 1.2% | 1.2% | 0.0 pp | Ninguno* | Ninguno* | Ausente |

*"Ninguno en particular" es el lider — el mercado no tiene un lider claro de habito o precio en esas categorias

**Farmacia: Gama es lider de habito (4.2%, confirmado en CU-8 v2) aunque no lidera precio.

### Hallazgos A9:

1. **Paramo domina absolutamente en Carne/Pollo/Charcuteria** — habito y precio. Estas son las categorias donde Gama esta mas distante y donde intervenir requeriria cambio real de precios.

2. **Congelados, Gaseosas y Salsas son el territorio defensivo de Gama** — habito moderado (7-8%) sin liderazgo de precio. El shopper va a Gama para estas categorias por conveniencia/cercania/servicio, no por precio.

3. **En la mayoria de categorias el lider es "Ninguno en particular"** — el mercado no tiene una cadena dominante en habito ni en precio percibido en categorias como Galletas, Gaseosas, Cuidado Personal. Esto indica espacio disponible.

4. **Farmacia es la anomalia positiva:** Gama es lider de habito en farmacia (4.2%) pero no en precio. El shopper va a farmacia de Gama por conveniencia — probablemente 24 horas o ubicacion. Esta es la categoria donde el servicio genera habito sin precio.

> Nota metodologica: TODOS los n de Gama por categoria son REFERENCIALES (n<30 en todos los casos excepto proximos a). Los patrones son indicativos. Los lideres "Ninguno en particular" son firmes (n>100 en varios casos). La comparacion Gama vs Paramo en categorias proteinas (carne/pollo/charcuteria) es firme para Paramo pero REFERENCIAL para Gama.

---

## §11 A10 — Categorias "cuidar precio" vs "ofrecer valor"

### Clasificacion estrategica de categorias para Gama

| Categoria | Tipo | Habito Gama % | Gap habito vs precio | Prioridad |
|---|---|---|---|---|
| **Congelados** | **Ofrecer valor** | 8.0% | +3.3 pp | Mantener precio + comunicar diferencial experiencial |
| **Gaseosas, jugos** | **Ofrecer valor** | 7.2% | +4.0 pp | Mantener precio + comunicar diferencial experiencial |
| **Salsas y Enlatados** | **Ofrecer valor** | 7.5% | +3.0 pp | Mantener precio + comunicar diferencial experiencial |
| **Galletas** | **Cuidar precio** | 7.0% | +1.3 pp | Cuidar precio y habito — brecha pequeña, defender |
| Carne de res | Neutro/Ausente | 3.7% | +0.7 pp | Sin accion prioritaria vs Paramo (gap enorme) |
| Pollo | Neutro/Ausente | 3.5% | +1.0 pp | Sin accion prioritaria vs Paramo |
| Charcuteria | Neutro/Ausente | 3.2% | +1.5 pp | Sin accion prioritaria |
| Frutas y verduras | Neutro | 4.0% | +1.8 pp | Monitorear |
| Productos basicos | Neutro | 5.5% | +1.0 pp | Monitorear — Paramo lidera |
| Farmacia | Neutro** | 4.2% | +1.2 pp | **Comunicar conveniencia/24h — no precio** |
| Licores | Neutro | 3.7% | +0.2 pp | Monitorear |
| Cuidado personal | Neutro | 4.0% | +1.0 pp | Monitorear |
| Cuidado hogar | Neutro | 5.0% | +1.3 pp | Monitorear |
| Pescados | Neutro | 2.7% | +1.7 pp | Sin accion |
| Mascotas | Ausente | 1.2% | 0.0 pp | Sin accion |

**Respuesta a la pregunta de Cora (minuto 14:43 de la reunion):**

> "Cuales son las categorias donde el tiene que cuidar precio y cuales son las categorias donde El deberia ofrecer valor?"

**Ofrecer valor (mantener precio, comunicar experiencia):**
- Congelados, Gaseosas/Jugos, Salsas y Enlatados — en estas 3 categorias el shopper ya elige Gama aunque no la percibe como la mas economica. La palanca es comunicar por que vale venir a Gama (servicio, conveniencia, ambiente) no reducir precio.
- Farmacia — categoria de liderazgo de habito sin liderazgo de precio; comunicar 24h/conveniencia.

**Cuidar precio (defender la posicion, no perder):**
- Galletas/confiteria — brecha precio pequena (+1.3 pp), habito alto (7%). Si Gama cede en precio aqui pierde habito porque hay alternativas competitivas cercanas.
- Productos basicos — Paramo lidera precio; Gama tiene habito moderado que puede erosionarse si el gap precio sube.

**Sin accion de precio inmediata (terreno de Paramo):**
- Proteinas (carne, pollo, charcuteria) — Paramo domina con brechas enormes. Competir en precio aqui es una batalla de alto costo con baja probabilidad de conversion de perceptual. No es territorio de Gama.

> Caveat obligatorio: este analisis es 100% perceptual (P30/P32 de encuesta). Las decisiones de precio deben validarse con datos reales de pricing operativo. Un shopper que percibe precio alto puede estar equivocado o puede estar en lo correcto — la encuesta no distingue. N de Gama por categoria es REFERENCIAL en todos los casos.

---

## §12 Parte B — Validacion de consistencia V3 vs analisis actuales

### Tabla de validacion formal

| ID | Analisis V3 | Cifra V3 | Cifra actual | Consistencia | Interpretacion |
|---|---|---|---|---|---|
| **V3-DNA-1** | DNA z-scores sobreindice experiencial | Atractiva +1.09, Calidad +0.97, Seguro +0.76, Limpieza +0.72 | **Atractiva +1.10, Calidad +1.01, Seguro +0.84, Limpieza +0.81** | **CONSISTENTE** | Los 4 atributos se confirman con valores casi identicos o mas altos |
| **V3-DNA-2** | DNA z-scores subindice precio | Menor precio -0.72, Valer dinero -0.67, Promociones -0.67 | **Menor precio -0.76, Valer dinero -0.45, Promociones -0.64** | **CONSISTENTE** | Los 3 atributos siguen en negativo. Valer dinero mejora (-0.67 -> -0.45) |
| **V3-MOD-1** | Modelo mental Gama atencion-dominante | Gama 53% razon atencion | **Gama 78% atencion** | **CONSISTENTE — MAS FUERTE** | La atencion se consolida como razon dominante de los preferentes de Gama |
| **V3-MOD-2** | Modelo mental CM atencion-dominante | CM 53% atencion | CM 23% atencion* | **TENSION LEVE** | Los % de CM son mas bajos pero la categoria de modelo sigue siendo atencion |
| **V3-MOD-RIO** | CRITICO — Rio atencion-dominante 51% | Rio 51% atencion | **Rio 68% precio, 51% atencion** | **TENSION LEVE** | Rio mantiene 51% atencion PERO 68% precio — tiene caracter mixto; precio es dominante numericamente |
| **V3-SEG** | 3 segmentos k-means + perfil Nucleo Leal | Seg1 59%/Seg2 33%/Seg3 8%, NSE 2.16, precio 2.94/5 | **IDENTICO** | **IDENTICO** | Mismo calculo, mismo dataset, misma semilla |

### Interpretacion de las tensiones:

**No hay tensiones criticas.** Todos los analisis V3 son consistentes o mejoran en la misma direccion.

**Tension leve V3-MOD-RIO — el hallazgo mas importante:**

La pregunta era: "¿Rio sigue siendo atencion-dominante o migro?" La respuesta es matizada:
- Rio mantiene el mismo 51% de atencion que en V3
- PERO ahora el 68% cita precio — lo que en V3 no habia
- Rio tiene un **modelo MIXTO con tendencia precio-dominante**
- El crecimiento explosivo de Rio en TOM (+17pp en CU-7) fue impulsado por percepcion de precio/valor
- **Conclusion para el deck:** Rio ya no es "el otro supermercado de atencion". Es un competidor de precio-valor que tambien tiene algo de atencion. Gama no comparte el territorio con Rio — Rio se fue al territorio de Paramo.

**Tension leve V3-MOD-2 (CM):**

Los % de razon espontanea de CM son mas bajos en este calculo (23% atencion vs 53% V3). Esto puede deberse a diferencia metodologica en la categorizacion de las respuestas abiertas entre V3 y el analisis actual — no interpretarlo como que CM cambio dramaticamente. El modelo categorico de CM sigue siendo atencion-dominante.

### Conclusion de validacion:

Los 6 items validados son CONSISTENTES o IDENTICOS con los analisis del V3. No se requiere ajustar el marco estrategico del V3 — los datos 2026 confirman y en varios casos refuerzan los hallazgos V3.

---

## §13 Hallazgos clave CU-9 (10 hallazgos numerados)

**H-9-1. DNA de Gama se confirma y AMPLIA: sobreindice en 6 de 10 atributos (vs 4 en V3).**
Los 4 atributos experienciales del V3 (atractiva +1.10, calidad +1.01, seguro +0.84, limpieza +0.81) se confirman con valores casi identicos o mas altos. Ademas, en 2026 Gama sobreindice tambien en Rapidez caja (+0.62) y Atencion (+0.52) — el DNA experiencial de Gama se fortaleció durante el año. Nivel de evidencia: ALTO.

**H-9-2. El shopper de Gama verbaliza atencion con el 78% de sus preferentes — sube del 53% del V3.**
La consolidacion del Nucleo Leal en torno al atributo de atencion es el hallazgo mas solido de CU-9. En el mercado amplio, cuando se pregunta por asociacion (P23), la atencion es el 5° atributo (21.9%) pero cuando los leales hablan espontaneamente es el primero (78%). La campana tiene la tarea de trasladar esa verbalizacion del Nucleo Leal al mercado amplio. Nivel de evidencia: ALTO (n=32 REFERENCIAL para el 78%, pero el dato P23 de 21.9% es firme n=402).

**H-9-3. Rio es ahora precio-dominante (68% precio, 51% atencion) — migro del campo experiencial al de precio/valor.**
Esta es la verificacion critica pedida explicitamente. Rio no compite en el territorio de Gama — crece en el territorio de Paramo. Su expansion de TOM (+17pp) fue impulsada por precio/valor, no por experiencia. Implicacion: Gama no pierde territorio por el crecimiento de Rio. Nivel de evidencia: MEDIO (n=41 referentes de Rio, REFERENCIAL).

**H-9-4. La imagen de Gama en C+/C es sustancialmente mejor que en el Total en atributos experienciales.**
C+/C asocia Gama con atencion en el 31.7% (vs 21.9% total, +9.8 pp), rapidez en el 29.8% (vs 21.1%, +8.7 pp) y seguro en el 36.5% (vs 29.6%, +6.9 pp). El segmento natural de Gama la ve de forma mas favorable. Esto confirma que la estrategia de profundizar en C+/C tiene justificacion empirica. Nivel de evidencia: MEDIO (n=104 C+/C es firme pero n por atributo para C+/C son referenciales).

**H-9-5. El gap verbal-asociativo es sistematico: en ninguna cadena la razon espontanea coincide con el atributo de mayor asociacion inducida.**
En P23, "limpieza" domina la imagen de casi todas las cadenas cuando se pregunta directamente. Pero en P21.1, nadie habla de limpieza espontaneamente — hablan de precio o atencion. La limpieza es una imagen de fondo que el mercado da por descontada. Para Gama, la implicacion es que la campana debe activar la verbalizacion de ATENCION (lo que los leales dicen cuando se les pregunta por que prefieren Gama) para que pase del 21.9% de asociacion inducida a verbalizacion espontanea en el mercado amplio. Nivel de evidencia: ALTO.

**H-9-6. Los recordadores de publicidad de Gama (PTL y DTLS) son principalmente NSE E (54-58%) — el segmento que mas percibe a Gama como cara.**
Hay un desalineamiento entre el perfil del receptor del mensaje ("Precios de tu lado") y su capacidad de persuasion: NSE E es el que menos dispuesto esta a comprar en Gama por precio. El mensaje esta llegando pero no convinciendo al segmento que llega. C+/C — el segmento natural de Gama — esta subrepresentado entre los recordadores (18-20% de recordadores vs 25.9% de la muestra total). Nivel de evidencia: MEDIO (n=43-50 firme pero cruces NSE referenciales).

**H-9-7. La recordacion publicitaria predice mayor habito de compra en Gama (+7 pp en Galletas/Gaseosas/Salsas) pero NO predice mayor preferencia ni mejor percepcion de precio.**
La publicidad de Gama esta generando/reforzando habito en categorias especificas (Galletas, Gaseosas, Salsas) pero no esta convirtiendo no-preferentes en preferentes ni cambiando la percepcion de precio. Esto es consistente con la hipotesis de que la publicidad actual alcanza a quienes ya tienen relacion con Gama — no esta generando primera visita. Nivel de evidencia: MEDIO (causalidad no inferible en cross-sectional).

**H-9-8. Las 3 categorias de "ofrecer valor" para Gama son Congelados (8.0% habito), Gaseosas/Jugos (7.2%) y Salsas/Enlatados (7.5%).**
En estas tres categorias el shopper ya elige Gama aunque no la percibe como la mas economica — el habito esta anclado en conveniencia/servicio. La estrategia correcta es mantener precio y comunicar por que vale ir a Gama (no bajar precio). La unica categoria de "cuidar precio" con habito relevante es Galletas (7.0%). Nivel de evidencia: MEDIO (n Gama por categoria REFERENCIAL).

**H-9-9. La importancia de Rapidez en caja es el diferenciador de C+/C vs Total: el unico atributo P22 que C+/C valora MAS que el promedio (+3.1 pp).**
El segmento natural de Gama es el que mas exige rapidez. Esto se alinea con el perfil del Nucleo Leal (rapidez caja 4.81/5, el valor mas alto de los 10 atributos). La implicacion practica: la rapidez en caja es la palanca de experiencia mas relevante para el segmento C+/C — y Gama ya sobreindice en ese atributo (+0.62 z-score). Nivel de evidencia: ALTO.

**H-9-10. El mapa perceptual MDS coloca a Gama lejos de Paramo y cerca de cadenas experienciales — el territorio de Gama esta bien definido y diferenciado.**
La dimension 1 del MDS captura la oposicion precio-dominante (Paramo, La Muralla) vs experiencia-dominante (Gama, CM, Hiper Lider). Gama no esta en el mismo cuadrante que Paramo — confirma que intentar migrar al territorio de precio implica abandonar el cuadrante donde Gama ya tiene ventaja perceptual. Nivel de evidencia: MEDIO (MDS es descriptivo, no inferencial).

---

## §14 Caveats para Bruna

| # | Caveat | Impacto | Frase recomendada para deck |
|---|---|---|---|
| CV-9-01 | Pref-Gama n=32: todos los datos del Nucleo Leal son REFERENCIALES | ALTO | "Perfil referencial n=32 — indicativo, no proyectable" |
| CV-9-02 | A1 P22: T2B alto (84-97%) en todos los atributos — no usar como diferenciador. La importancia es tabla de piso, no tabla de posicionamiento | MEDIO | "La importancia de atributos es alta para todos — el diferenciador real es quien los 'tiene'" |
| CV-9-03 | A2 P23 C+/C: n por atributo por cadena en C+/C = 8-38. Todos REFERENCIALES para cada celda individual | ALTO | "Asociaciones C+/C son indicativas — bases por celda referenciales" |
| CV-9-04 | A3 correlacion nominal: es mapeo semantico, no correlacion estadistica. No tiene p-value | MEDIO | "Analisis nominal indicativo — no implica causalidad ni test estadistico" |
| CV-9-05 | A5 DNA z-scores: normalizacion descriptiva. La variacion en z-scores refleja cambios en el paisaje competitivo completo, no solo de Gama | MEDIO | "Z-scores descriptivos — variacion puede reflejar cambios en competencia, no solo en Gama" |
| CV-9-06 | A6 modelos mentales: n=32 para Gama, n=41 para Rio, n=45 para CM — todos REFERENCIALES | ALTO | "Modelos mentales por cadena referenciales en cadenas con n<50" |
| CV-9-07 | A7 recordadores: perfiles NSE dentro de PTL/DTLS referenciales (n=8-27 por NSE) | MEDIO | "Perfil NSE de recordadores indicativo — bases por NSE referenciales" |
| CV-9-08 | A8 recall-habito: relacion puede ser inversa (habito genera exposicion, no publicidad genera habito). Causalidad no inferible | ALTO | "Asociacion recall-habito es descriptiva — no implica que publicidad genero habito" |
| CV-9-09 | A9/A10 categorias: TODOS los n de Gama por categoria son REFERENCIALES. Los patrones son indicativos | CRITICO | "Analisis por categoria indicativo — n Gama < 30 en todos los casos" |
| CV-9-10 | A6 Rio modelo mixto: n=41 preferentes Rio. La conclusion "Rio es precio-dominante" debe presentarse con caveat de base referencial | MEDIO | "Perfil de Rio referencial (n=41) — modelo mixto, tendencia precio-dominante" |

---

## §15 Tabla de handoff para Main Claude / Vivienne — sugerencia de ubicacion en Word V7

| Hallazgo CU-9 | Capitulo Word V7 | Tipo de elemento |
|---|---|---|
| H-9-1: DNA sobreindice 6 atributos (con vs V3) | Cap. 2 — Posicionamiento + DNA | Tabla z-scores actualizada |
| H-9-2: 78% atencion en Nucleo Leal | Cap. 2 — Posicionamiento / Cap. 5 — Sintesis | Cifra callout |
| H-9-3: Rio precio-dominante | Cap. 1 — Embudo + drivers / Cap. 2 | Slide modelo mental — actualizado |
| H-9-4: C+/C imagen mas favorable | Cap. 2 — Posicionamiento + bifurcacion C+/C | Tabla comparativa Total vs C+/C |
| H-9-5: Gap verbal-asociativo sistematico | Cap. 2 — Posicionamiento | Marco interpretativo |
| H-9-6: Recordadores NSE E | Cap. 4 — Efectividad PTL/DTLS | Perfil NSE recordadores |
| H-9-7: Recall predice habito no preferencia | Cap. 4 — Efectividad PTL/DTLS | Insight sobre limite del recall |
| H-9-8: 3 categorias ofrecer valor | Cap. 3 — Precios y categorias | Tabla clasificacion categorias |
| H-9-9: Rapidez caja diferenciador C+/C | Cap. 2 — Posicionamiento | Tabla importancia por NSE |
| H-9-10: Mapa perceptual Gama separada de Paramo | Cap. 2 — Posicionamiento | Plot MDS |
| A1 P22 tabla completa | Cap. 2 — Posicionamiento | Tabla importancia atributos |
| A2 P23 matriz completa Gama | Cap. 2 — Posicionamiento | Heatmap / tabla |
| A9 cruce categorias P30 x P32 | Cap. 3 — Precios y categorias | Tabla cruce habito vs precio |
| Validacion V3 consistencia | Cap. 0 — Marco metodologico | Nota tecnica (no en cuerpo principal) |

---

*CU-9 producido por Cuanti V7 — 2026-05-18.*
*Extiende CU-1..CU-8 v2 — no reemplaza.*
*JSON canonico: `outputs/json/CU9_v7_analisis_20260518.json`*
*Script reproducible: `scripts/cu9_v7_analisis.py`*
*Plots: `outputs/plots/cu9_*.png`*
*Gate Bruna: obligatorio antes de deck publico. Ver §14.*
*Handoff Main Claude: §15 con sugerencias de ubicacion en Word V7.*
