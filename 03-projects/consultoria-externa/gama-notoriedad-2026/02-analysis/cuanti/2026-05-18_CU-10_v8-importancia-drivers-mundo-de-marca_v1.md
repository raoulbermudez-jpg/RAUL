# CU-10 — V8: Top Box puro P22 + Drivers de preferencia + Mundo de marca
## Gama Notoriedad 2026

**Fecha:** 2026-05-18 | **Base total: n=402** | **n C+/C: 104** | **n Pref-Gama: 32 (REFERENCIAL)**
**Significancia:** alpha=0.05 | **IC95:** Newcombe-Wilson | **VIF umbral:** 10
**Script principal:** `scripts/cu10_v8_analisis.py` + `scripts/cu10_v8_e3_fix.py`
**JSON:** `outputs/json/CU10_v8_analisis_20260518.json`
**Producido por:** Cuanti V8 — 2026-05-18
**Para:** Insighter / Vivienne / Main Claude (Word V8) / Bruna (gate previo a deck publico)
**Handoff previo:** CU-1..CU-9 vigentes — este CU-10 EXTIENDE, no reemplaza

> **Gate Bruna obligatorio.** Pref-Gama (n=32) es REFERENCIAL en todas las secciones. Paramo (n=85), Rio (n=41), CM (n=45), Forum (n=44), Plazas (n=37), Luz (n=32) tienen bases que permiten descripcion pero NO inferencia. Plan Suarez (n=28) REFERENCIAL. Ningun numero de este documento debe incorporarse a un deck publico sin revision de Bruna.

> **Nota de codificacion P24/P25.** En esta BBDD, P24 = cadena de ultima compra (experiencia reciente), P25 = razon de esa compra (tipo de mision, no cadena). No existe columna "alguna vez ha comprado" separada. La variable de experiencia habitual se construye desde P26 (cadena habitual por mision de compra). El cruce de experiencia es: exp_reciente = P24 == cadena, exp_habitual = cualquier P26 == cadena.

---

## §1 Metodologia

| # | Entregable | Metodo | Base |
|---|---|---|---|
| E1 | P22 Top Box puro (Muy Importante) | % valor 5 en escala 1-5 | Total + C+/C + 8 marcas preferidas |
| E2 | Viabilidad regresion + drivers preferencia | VIF entre P22 + Logistica por cadena (DV binaria) | n=402 completo / por cadena |
| E3 | Mundo de marca P21 x P23 x experiencia | % menciones P23 por cadena x atributo x segmento | Total + Pref + Exp_reciente |
| E4 | Sintesis integradora | Analisis sustantivo integrando E1+E2+E3 | -- |

### Nota critica E2 — Por que logistica y no lineal

La pregunta de Cora menciona "regresion lineal". La variable dependiente (DV) es preferencia 0/1 (binaria: prefiere o no prefiere la cadena). La regresion lineal con DV binaria produce probabilidades fuera del rango [0,1] y residuos no-normales, lo que invalida los supuestos del modelo. **El metodo correcto tecnico es la regresion logistica**, que produce probabilidades dentro de [0,1] y coeficientes interpretables como odds ratios. Esta nota queda explicada brevemente en el deck para que Cora tenga el contexto del ajuste metodologico.

---

## §2 E1 — P22 Top Box puro: % "Muy Importante" por segmento y marca

### 2.1 Total n=402 — TB puro vs T2B comparado

| Ranking TB | Atributo | TB % | T2B % | Gap T2B-TB | Ranking T2B | Delta rank |
|---|---|---|---|---|---|---|
| 1 | Limpieza/orden | **63.9%** | 97.5% | 33.6 pp | 1 | 0 |
| 2 | Menor precio | **62.4%** | 94.0% | 31.6 pp | 8 | **+6** |
| 3 | Rapidez caja | **58.7%** | 94.0% | 35.3 pp | 7 | **+4** |
| 4 | Mayor calidad | **58.7%** | 97.5% | 38.8 pp | 2 | **-2** |
| 5 | Seguro | **57.7%** | 96.0% | 38.3 pp | 4 | -1 |
| 6 | Valer dinero | **57.7%** | 96.5% | 38.8 pp | 3 | **-3** |
| 7 | Mayor surtido | **57.2%** | 95.5% | 38.3 pp | 6 | -1 |
| 8 | Mejor atencion | **57.0%** | 96.0% | 39.0 pp | 5 | **-3** |
| 9 | Promociones | **50.5%** | 89.6% | 39.1 pp | 9 | 0 |
| 10 | Tienda atractiva | **42.5%** | 84.3% | 41.8 pp | 10 | 0 |

**Top-5 TB puro: Limpieza, Menor precio, Rapidez, Calidad, Seguro**
**Top-5 T2B (V7): Limpieza, Calidad, Valer dinero, Seguro, Atencion**

**El top-5 CAMBIA al usar TB puro.** Los atributos que suben de ranking con TB puro:
- **Menor precio sube 6 puestos** (rank 8 en T2B → rank 2 en TB): cuando se filtra solo "Muy Importante", precio es el segundo atributo mas critico del mercado. Esto refuerza la presion de precio que Gama enfrenta.
- **Rapidez caja sube 4 puestos** (rank 7 → rank 3): la urgencia percibida sobre velocidad es subestimada por el T2B.

Los atributos que bajan de ranking:
- **Mejor atencion baja 3 puestos** (rank 5 → rank 8): muchos responden "importante" pero no "MUY importante". La atencion es ampliamente valorada pero con intensidad moderada en el mercado amplio.
- **Valer dinero baja 3 puestos** (rank 3 → rank 6): similar, valoracion amplia pero con menos intensidad de "Muy Importante".

> **Implicacion analitica critica:** el T2B infla artificialmente la importancia de atributos relacionales (atencion, valor) frente a los funcionales (precio, rapidez). El TB puro revela que el consumidor venezolano tiene prioridades funcionales mas severas que lo que el T2B sugiere.

### 2.2 C+/C n=104 — TB puro

| Ranking TB | Atributo | TB % C+/C | TB % Total | Diferencia pp |
|---|---|---|---|---|
| 1 | Mejor atencion | **64.4%** | 57.0% | **+7.4 pp** |
| 2 | Limpieza/orden | **63.5%** | 63.9% | -0.4 pp |
| 3 | Valer dinero | **62.5%** | 57.7% | +4.8 pp |
| 4 | Rapidez caja | **61.5%** | 58.7% | +2.8 pp |
| 5 | Seguro | **60.6%** | 57.7% | +2.9 pp |
| 6 | Menor precio | **60.6%** | 62.4% | -1.8 pp |
| 7 | Mayor calidad | **54.8%** | 58.7% | -3.9 pp |
| 8 | Mayor surtido | **52.9%** | 57.2% | -4.3 pp |
| 9 | Promociones | **42.3%** | 50.5% | -8.2 pp |
| 10 | Tienda atractiva | **40.4%** | 42.5% | -2.1 pp |

**Hallazgo C+/C TB puro:**
- **Mejor atencion #1 en C+/C** (vs #8 en Total TB). El segmento natural de Gama exige atencion con mucha mayor intensidad que el mercado total.
- C+/C menos intenso en Calidad (-3.9 pp), Surtido (-4.3 pp) y Promociones (-8.2 pp). El C+/C da por descontada la calidad minima y no busca promociones como criterio principal.

### 2.3 Pref-Gama n=32 — TB puro (REFERENCIAL)

| Ranking TB | Atributo | TB % Pref-Gama | TB % Total | Diferencia pp |
|---|---|---|---|---|
| 1 | Rapidez caja | **84.4%** | 58.7% | **+25.7 pp** |
| 2 | Mejor atencion | **71.9%** | 57.0% | **+14.9 pp** |
| 2 | Valer dinero | **71.9%** | 57.7% | **+14.2 pp** |
| 4 | Limpieza/orden | **65.6%** | 63.9% | +1.7 pp |
| 5 | Mayor surtido | **62.5%** | 57.2% | +5.3 pp |
| 6 | Seguro | **56.2%** | 57.7% | -1.5 pp |
| 6 | Mayor calidad | **56.2%** | 58.7% | -2.5 pp |
| 8 | Tienda atractiva | **50.0%** | 42.5% | +7.5 pp |
| 9 | Menor precio | **43.8%** | 62.4% | **-18.6 pp** |
| 10 | Promociones | **25.0%** | 50.5% | **-25.5 pp** |

**Hallazgo Pref-Gama TB puro (REFERENCIAL):**
- **Rapidez caja #1 con 84.4%** — confirmado con T2B (96.9%) y media 4.81/5 del CU-4. Los leales de Gama tienen una exigencia extrema en velocidad de caja.
- **Menor precio -18.6 pp vs Total** y **Promociones -25.5 pp**: el Nucleo Leal de Gama es el segmento que MENOS exige precio y promociones como criterio "Muy Importante". Eligen Gama por atencion y rapidez, no por precio.

### 2.4 Tabla resumen TB puro por todas las marcas preferidas

| Atributo | Total | Pref-Gama | Pref-Paramo | Pref-Rio | Pref-CM | Pref-Forum | Pref-Plazas | Pref-Luz | Pref-PlanS |
|---|---|---|---|---|---|---|---|---|---|
| Limpieza/orden | 63.9% | 65.6% | 60.0% | 68.3% | 60.0% | 68.2% | 67.6% | 50.0%* | 57.1%* |
| Menor precio | 62.4% | 43.8%* | 68.2% | 63.4% | 55.6% | 50.0% | 59.5% | 78.1%* | 50.0%* |
| Rapidez caja | 58.7% | **84.4%*** | 50.6% | 65.9% | 62.2% | 75.0% | 62.2% | 56.2%* | 57.1%* |
| Mayor calidad | 58.7% | 56.2%* | 56.5% | 51.2% | 60.0% | 70.5% | 62.2% | 37.5%* | 67.9%* |
| Seguro | 57.7% | 56.2%* | 56.5% | 58.5% | 57.8% | 56.8% | 67.6% | 56.2%* | 53.6%* |
| Valer dinero | 57.7% | 71.9%* | 63.5% | 51.2% | 57.8% | 50.0% | 54.1% | 75.0%* | 53.6%* |
| Mayor surtido | 57.2% | 62.5%* | 50.6% | 73.2% | 60.0% | 65.9% | 48.6% | 50.0%* | 67.9%* |
| Mejor atencion | 57.0% | 71.9%* | 55.3% | 56.1% | 57.8% | 54.5% | 56.8% | 53.1%* | 42.9%* |
| Promociones | 50.5% | 25.0%* | 55.3% | 36.6% | 46.7% | 43.2% | 43.2% | 59.4%* | 57.1%* |
| Tienda atractiva | 42.5% | 50.0%* | 34.1% | 34.1% | 37.8% | 47.7% | 51.4% | 28.1%* | 28.6%* |

*REFERENCIAL: n<30 en esa celda. Pref-Gama n=32, Pref-Luz n=32, Pref-Plan Suarez n=28.

**Lectura por marca:**
- **Paramo preferentes:** Menor precio (68.2%) es el atributo mas exigido, seguido de Valer dinero (63.5%). Perfil funcional-precio.
- **Rio preferentes:** Mayor surtido es #1 (73.2%) — Rio se elige por amplitud de oferta. Rapidez en caja segundo (65.9%).
- **Forum preferentes:** Mayor calidad #1 (70.5%) + Rapidez caja #2 (75.0%). Perfil experiencia-calidad-velocidad.
- **Luz preferentes:** Menor precio #1 (78.1%) + Valer dinero (75.0%) — perfil precio-dominante intenso (REFERENCIAL).

> **Ver plots:** `cu10_heatmap_tb_puro.png`, `cu10_tb_vs_t2b_reranking.png`

---

## §3 E2 — Evaluacion de viabilidad y Regresion logistica

### 3.1 Evaluacion VIF — Multicolinealidad entre predictores P22

| Atributo | VIF | Estado |
|---|---|---|
| Mejor atencion | 1.35 | OK (<5) |
| Rapidez caja | 1.33 | OK (<5) |
| Promociones | 1.29 | OK (<5) |
| Menor precio | 1.27 | OK (<5) |
| Seguro | 1.23 | OK (<5) |
| Mayor surtido | 1.22 | OK (<5) |
| Mayor calidad | 1.19 | OK (<5) |
| Limpieza/orden | 1.18 | OK (<5) |
| Tienda atractiva | 1.12 | OK (<5) |
| Valer dinero | 1.08 | OK (<5) |

**VIF maximo = 1.35 — multicolinealidad practicamente inexistente.** Las 10 importancias P22 son suficientemente independientes entre si para una regresion valida. No se requiere KDA ni Shapley para este dataset.

### 3.2 Tamanios muestrales por cadena

| Cadena | n preferentes | Viable (n>=50) | Nota |
|---|---|---|---|
| **Paramo** | **85** | **SI** | Unica cadena con base suficiente |
| Rio | 41 | No | Excluida (n<50) |
| Forum | 44 | No | Excluida (n<50) |
| Central Madeirense | 45 | No | Excluida (n<50) |
| Plazas | 37 | No | Excluida (n<50) |
| Gama | 32 | No | Excluida (n<50) — REFERENCIAL |
| Luz | 32 | No | Excluida (n<50) — REFERENCIAL |
| Plan Suarez | 28 | No | Excluida (n<50) — REFERENCIAL |

**Resultado:** solo Paramo cumple el umbral de n>=50 para regresion confiable. Para las 7 cadenas restantes, la regresion logistica produciria intervalos de confianza muy amplios con riesgo alto de error tipo II. No se corren.

**Alternativa para cadenas excluidas:** ver §3.4 — analisis descriptivo de diferencias de importancia media.

### 3.3 Regresion logistica — Paramo (DV: prefiere Paramo=1, otro=0)

| Parametro | Valor |
|---|---|
| n total | 402 |
| n preferentes Paramo | 85 |
| n no-preferentes | 317 |
| Pseudo-R² McFadden | 0.021 (pobre) |
| LLR p-value | 0.574 (modelo no significativo) |
| Convergencia | Si |

**Coeficientes significativos (p<0.05):**

| Atributo | B | SE | p-valor | OR | Interpretacion |
|---|---|---|---|---|---|
| Mayor calidad | -0.435 | 0.214 | 0.042 | 0.648 | Un punto mas en importancia de calidad REDUCE 35.2% las odds de preferir Paramo |

**Solo 1 atributo significativo. El modelo global no es significativo (LLR p=0.574). Pseudo-R²=0.021 — el modelo explica menos del 2.1% de la varianza en preferencia Paramo.**

**Interpretacion:** Las importancias declaradas en P22 no predicen la preferencia de cadena. Un consumidor que dice que "calidad es muy importante" tiene MENOR probabilidad de preferir Paramo — lo que es coherente: Paramo se elige por precio/conveniencia, no por calidad. Pero la magnitud del efecto es pequena y el modelo global falla.

**Conclusion E2:** La regresion logistica no es el instrumento adecuado para este dataset porque:
1. Las importancias declaradas (P22) son percibidas como importantes por todos (TB puro 57-64% para la mayoria), por lo que tienen baja varianza discriminante.
2. La DV binaria por cadena con bases pequenas genera potencia estadistica insuficiente.
3. El verdadero predictor de preferencia es la imagen (P23), no la importancia (P22) — el mundo de marca (E3) es mas informativo.

**Recomendacion tecnica para versiones futuras:** si se quiere predecir preferencia, la variable independiente correcta es la asociacion inducida P23 (binaria por atributo x cadena) cruzada con P22 como ponderador de importancia — lo que es esencialmente un analisis de importancia-rendimiento (IP map). Esto se puede calcular con los datos actuales pero requiere una corrida separada fuera del alcance de este CU-10.

> **Ver plot:** `cu10_coefs_paramo.png`

### 3.4 Analisis descriptivo complementario — diferencias de importancia por preferentes vs no-preferentes

Para las cadenas con n<50, en lugar de regresion se reporta la diferencia en TB % entre preferentes y no-preferentes de cada cadena:

**Gama (n=32 REFERENCIAL):**

| Atributo | TB% Pref-Gama | TB% No-Pref-Gama | Diferencia |
|---|---|---|---|
| Rapidez caja | 84.4% | 55.5% | **+28.9 pp** |
| Mejor atencion | 71.9% | 54.5% | **+17.4 pp** |
| Valer dinero | 71.9% | 55.7% | **+16.2 pp** |
| Mayor surtido | 62.5% | 56.5% | +6.0 pp |
| Limpieza/orden | 65.6% | 63.6% | +2.0 pp |
| Seguro | 56.2% | 57.9% | -1.7 pp |
| Mayor calidad | 56.2% | 58.9% | -2.7 pp |
| Tienda atractiva | 50.0% | 41.8% | +8.2 pp |
| Menor precio | 43.8% | 64.0% | **-20.2 pp** |
| Promociones | 25.0% | 52.4% | **-27.4 pp** |

**Los preferentes de Gama son los que MAS exigen Rapidez (+28.9 pp) y Atencion (+17.4 pp) y los que MENOS exigen Precio (-20.2 pp) y Promociones (-27.4 pp) vs el resto del mercado.** Esta brecha es el sello del Nucleo Leal de Gama.

> Nota: este analisis descriptivo NO es equivalente a una regresion. No controla por covariables. Es indicativo.

---

## §4 E3 — Mundo de marca: P21 x P23 x Experiencia

### 4.1 Tabla P23 Total — % que asocia cada cadena con cada atributo (n=402)

| Cadena | Surtido | Calidad | Precio | Atencion | Promoc | Atractiva | Limpieza | Seguro | Rapidez | V.Dinero |
|---|---|---|---|---|---|---|---|---|---|---|
| **Gama** | 17.9% | 26.6% | **7.2%** | 21.9% | **9.0%** | 28.9% | 31.1% | 29.6% | 21.1% | 11.4% |
| **Paramo** | 29.4% | 26.6% | **35.1%** | 32.3% | **30.6%** | 31.3% | 34.6% | 36.1% | 30.3% | 32.1% |
| **Rio** | 21.9% | 26.1% | 13.9% | 23.9% | 17.4% | 28.1% | 33.6% | 27.1% | 21.6% | 17.4% |
| Central Mad. | 20.6% | 22.6% | 17.7% | 21.1% | 17.2% | 18.9% | 29.1% | 27.6% | 20.4% | 18.9% |
| Forum | 24.1% | 24.9% | 18.7% | 21.1% | 18.7% | 25.4% | 29.6% | 26.9% | 20.1% | 19.9% |
| Plazas | 17.4% | 21.4% | 10.9% | 21.1% | 15.9% | 19.9% | 30.6% | 28.1% | 15.7% | 12.9% |
| Plan Suarez | 14.2% | 13.4% | 11.9% | 11.4% | 11.2% | 11.2% | 14.9% | 16.2% | 10.4% | 11.4% |
| Luz | 11.4% | 10.9% | 12.2% | 13.4% | **14.9%** | 9.7% | 14.9% | 15.2% | 10.0% | 13.7% |

**Lecturas por cadena:**

- **Gama:** Imagen dominada por Limpieza (31.1%) + Seguro (29.6%) + Atractiva (28.9%) + Calidad (26.6%). Claro perfil experiencial. Debilidad en Precio (7.2%) y Promociones (9.0%) — las brechas mas grandes respecto a Paramo son en precio (+27.9 pp) y promociones (+21.6 pp).
- **Paramo:** Unica cadena con asociacion fuerte en TODOS los atributos. Domina en Seguro (36.1%), Precio (35.1%), Limpieza (34.6%), Atencion (32.3%), Valer dinero (32.1%), Promociones (30.6%). Es la cadena con imagen mas rica y completa del mercado.
- **Rio:** Imagen concentrada en Limpieza (33.6%) + Atractiva (28.1%) + Atencion (23.9%). Pero NINGUNO de sus atributos supera a Paramo. Perfil experiencial similar a Gama pero sin la claridad de liderazgo en ninguno. Refuerza el hallazgo CU-9: Rio compite en territorio de experiencia, no de precio.
- **Central Madeirense:** Imagen mas debil que Paramo/Rio en todos los atributos. Limpieza lidera (29.1%) pero los demas son mediocres. Sin diferenciacion clara.
- **Forum:** Perfil similar a CM, ligeramente mejor en Surtido (24.1%) y Calidad (24.9%). Imagen de cadena completa sin liderazgo en ninguna dimension.
- **Plazas:** Imagen experiencial (Limpieza 30.6%, Seguro 28.1%) pero sin precio (10.9%). Posicionamiento similar a Gama en atributos experienciales pero con menor notoriedad global.
- **Plan Suarez:** Imagen debil en todos los atributos (todos <17%). Bajo posicionamiento perceptual en la muestra total.
- **Luz:** Imagen debil (todos <15%) excepto Promociones (14.9%). Unica cadena donde Promociones es relativamente su punto mas alto — perfil de cadena economica/promocional.

> **Ver plot:** `cu10_heatmap_mundo_total.png`, `cu10_gama_vs_mercado_p23.png`

### 4.2 Tabla P23 Experiencia reciente (P24 = ultima compra en esa cadena)

La tabla siguiente muestra el % de asociacion P23 entre quienes compraron en esa cadena en su ultima visita. El denominador es n de quienes declararon esa cadena como su ultima compra.

| Cadena (n exp) | Surtido | Calidad | Precio | Atencion | Promoc | Atractiva | Limpieza | Seguro | Rapidez | V.Dinero |
|---|---|---|---|---|---|---|---|---|---|---|
| **Gama (n=30)*** | 80.0% | 76.7% | 43.3% | 83.3% | 50.0% | 73.3% | 76.7% | 86.7% | 73.3% | 46.7% |
| **Paramo (n=83)** | 74.7% | 62.7% | 80.7% | 80.7% | 68.7% | 66.3% | 83.1% | 78.3% | 75.9% | 84.3% |
| Rio (n=47) | 72.3% | 85.1% | 44.7% | 72.3% | 53.2% | 76.6% | 80.9% | 76.6% | 83.0% | 63.8% |
| Central Mad. (n=48) | 75.0% | 70.8% | 64.6% | 77.1% | 66.7% | 56.2% | 81.2% | 72.9% | 68.8% | 68.8% |
| Forum (n=56) | 71.4% | 71.4% | 62.5% | 66.1% | 60.7% | 75.0% | 80.4% | 80.4% | 67.9% | 73.2% |
| Plazas (n=36) | 72.2% | 80.6% | 50.0% | 77.8% | 61.1% | 69.4% | 75.0% | 80.6% | 66.7% | 61.1% |
| Plan Suarez (n=23)* | 78.3% | 73.9% | 73.9% | 87.0% | 69.6% | 43.5% | 87.0% | 91.3% | 73.9% | 78.3% |
| Luz (n=31)* | 74.2% | 71.0% | 77.4% | 71.0% | 83.9% | 48.4% | 71.0% | 83.9% | 64.5% | 71.0% |

*Gama n=30, Plan Suarez n=23, Luz n=31: bases OK/REFERENCIAL — interpretar con precaucion.

**Hallazgos clave tabla experiencia:**

1. **Gama — validacion por experiencia:** quienes compraron en Gama en su ultima visita la asocian con Atencion en un 83.3% (vs 21.9% total). La brecha es de +62.5 pp — la experiencia real de compra en Gama activa la asociacion con atencion de forma dramatica. Seguro (86.7%) y Limpieza (76.7%) son igualmente altos. **La experiencia en Gama es consistente con su posicionamiento declarado en P23: quien va, confirma la imagen.**

2. **Gama — validacion precio:** entre compradores recientes, Gama es asociada con precio solo en 43.3%. No hay revision de la percepcion de precio tras la experiencia de compra — el precio sigue siendo una debilidad incluso entre quienes van.

3. **Paramo — experiencia vs total:** quienes compraron en Paramo la asocian con Valer dinero en 84.3% (vs 32.1% total) y Precio en 80.7% (vs 35.1%). La experiencia confirma y amplifica la imagen de precio de Paramo.

4. **Rio — experiencia:** Calidad es el atributo mas alto entre compradores recientes de Rio (85.1% vs 26.1% total). Quienes van a Rio experimentan alta calidad de productos — una fortaleza latente que no esta capturada en la imagen general.

5. **Brecha general experiencia vs imagen total:** el patron universal es que la experiencia de compra eleva TODOS los atributos de asociacion. Quien va a cualquier cadena la percibe mejor en todos los atributos. Esto es efecto de consistencia cognitiva (racionalizar la eleccion) + efecto real de exposicion a la experiencia.

> **Ver plot:** `cu10_heatmap_mundo_experiencia.png`, `cu10_gama_brechas_segmentos.png`

### 4.3 Brechas P23 Gama: Preferentes vs Total vs Experiencia

| Atributo | Total (n=402) | Pref. Gama (n=32)* | Exp. reciente (n=30)* | Brecha Pref-Total | Brecha Exp-Total |
|---|---|---|---|---|---|
| Mejor atencion | 21.9% | **84.4%** | 83.3% | **+62.5 pp** | +61.4 pp |
| Limpieza/orden | 31.1% | **90.6%** | 76.7% | **+59.5 pp** | +45.6 pp |
| Seguro | 29.6% | **84.4%** | 86.7% | **+54.8 pp** | +57.1 pp |
| Mayor surtido | 17.9% | **71.9%** | 80.0% | **+54.0 pp** | +62.1 pp |
| Rapidez caja | 21.1% | **75.0%** | 73.3% | **+53.9 pp** | +52.2 pp |
| Tienda atractiva | 28.9% | **81.2%** | 73.3% | **+52.3 pp** | +44.4 pp |
| Mayor calidad | 26.6% | **78.1%** | 76.7% | **+51.5 pp** | +50.1 pp |
| Promociones | 9.0% | 50.0%* | 50.0% | +41.0 pp | +41.0 pp |
| Valer dinero | 11.4% | 46.9%* | 46.7% | +35.5 pp | +35.3 pp |
| Menor precio | 7.2% | 31.2%* | 43.3% | +24.0 pp | +36.1 pp |

*REFERENCIAL

**Lectura:** las brechas entre preferentes/compradores y la imagen total de Gama son enormes en todos los atributos (+24 a +62 pp). Gama tiene una imagen bifurcada: para quien no la conoce bien, es una cadena experiencial mediocre (por debajo de Paramo en casi todo); para quien la prefiere o ha comprado, es una cadena de excelencia experiencial percibida. **La tarea de comunicacion de Gama es cerrar esa brecha — trasladar la imagen de los leales al mercado amplio.**

### 4.4 Tabla resumen: Mundo de marca por cadena

| Cadena | Atributos centrales (top 3 P23 Total) | 4to atributo | Atributo sombra (en preferentes) | n pref | Flag |
|---|---|---|---|---|---|
| **Gama** | Limpieza, Seguro, Atractiva | Calidad | **Atencion (+62.5 pp en pref)** | 32 | REF* |
| **Paramo** | Seguro, Precio, Limpieza | Atencion | Valer dinero (+60 pp en pref) | 85 | OK |
| **Rio** | Limpieza, Atractiva, Seguro | Atencion | Calidad (+69 pp en pref) | 41 | OK |
| **Central Mad.** | Limpieza, Seguro, Calidad | Atencion | Atencion (+63 pp en pref) | 45 | OK |
| **Forum** | Limpieza, Seguro, Atractiva | Surtido | Valer dinero (+60 pp en pref) | 44 | OK |
| **Plazas** | Limpieza, Seguro, Calidad | Atencion | Atencion (+68 pp en pref) | 37 | OK |
| **Plan Suarez** | Seguro, Limpieza, Surtido | Precio | Valer dinero (+71 pp en pref) | 28 | REF* |
| **Luz** | Seguro, Promociones, Limpieza | Atencion | Surtido (+67 pp en pref) | 32 | REF* |

*REFERENCIAL

**Hallazgo estructural — el mundo de marca de todas las cadenas converge en Limpieza y Seguro.** Estos son atributos de imagen de piso (tabla de higiene): todas las cadenas los tienen en el top-3 de asociacion. El diferenciador real entre cadenas es:
- En el 4to y 5to atributo (donde emerge la personalidad real de cada cadena)
- En los atributos de "sombra" (lo que los preferentes ven que el mercado amplio no ve)

**Gama:** el atributo de sombra es ATENCION — lo que los leales de Gama tienen internalizado pero el mercado amplio no ha capturado todavia. Gama es la cadena donde la brecha imagen-total vs imagen-preferentes es la mas alta en el atributo de atencion.

### 4.5 Espacio competitivo: similitudes y diferencias

**Cadenas perceptualmente similares a Gama:**
- **Plazas:** perfil de asociacion casi identico a Gama en atributos experienciales (Limpieza 30.6%, Seguro 28.1%, Calidad 21.4%). Sin liderazgo de precio (10.9%). Base de preferentes moderada. Es el competidor perceptual mas cercano a Gama.
- **Rio:** imagen similar en Limpieza + Atractiva, pero con mejor posicion en Calidad entre compradores (85.1% en experiencia vs 76.7% Gama). Rio es el competidor experiencial que puede absorber clientes de Gama en el futuro si mejora su imagen de atencion.

**Cadenas perceptualmente distintas a Gama:**
- **Paramo:** opuesto completo — domina en precio/valor mientras Gama domina en ambiente/experiencia.
- **Luz y Plan Suarez:** imagen muy debil en todo — no representan un benchmark competitivo real para Gama.

---

## §5 E4 — Sintesis integradora

### 5.1 TB puro vs T2B: la correccion de Cora revela una realidad mas dura

El top-5 del T2B (usado en V7) era: Limpieza, Calidad, Valer dinero, Seguro, Atencion. El top-5 del TB puro es: Limpieza, Menor precio, Rapidez, Calidad, Seguro. La correccion de Cora es metodologicamente correcta y sustancialmente importante.

**El T2B suavizaba la importancia del precio.** Al filtrar solo "Muy Importante", Menor precio sube 6 posiciones y aparece como la segunda prioridad del mercado venezolano. Esto no es ruido — es una senial real: hay una porcion del mercado que no solo considera importante el precio sino que lo marca como critico. Gama subindexaba en precio antes; esto confirma que la brecha perceptual de precio es un problema mas severo de lo que el T2B insinuaba.

**La atencion baja 3 posiciones en TB.** La atencion es ampliamente valorada (57% T2B como base) pero con menor intensidad. Para el mercado amplio, la atencion es "importante" pero no "la mas critica". Sin embargo — y este es el hallazgo clave — para el NUCLEO LEAL de Gama, la atencion es #2 en TB puro (71.9%). El mercado amplio no le da intensidad maxima a la atencion; los leales de Gama si. La campana de Gama debe trabajar para elevar la intensidad percibida de la atencion en el mercado amplio.

### 5.2 Drivers de preferencia (E2) confirman o desafian la importancia declarada (E1)?

La regresion logistica produce un resultado que parece sorprendente pero es coherente: **las importancias declaradas en P22 no predicen significativamente la preferencia de cadena.** El unico coeficiente significativo es que Mayor calidad tiene efecto NEGATIVO sobre preferencia Paramo — lo que tiene logica: Paramo se elige por precio, no calidad.

**La brecha verbal-conductual en este estudio opera a un nivel diferente:** no es que los consumidores digan que algo importa y luego no lo usen como criterio. Es que las importancias P22 son tan uniformemente altas (todos los atributos en 57-64% de TB puro) que no discriminan entre quienes prefieren distintas cadenas. Lo que realmente discrimina es la IMAGEN (P23): quien percibe que Gama tiene atencion (21.9% en total vs 84.4% en preferentes) va a Gama.

**Implicacion:** el modelo de decision no es "importancia x percepcion" (IP map simple) sino "percepcion de que la cadena TIENE el atributo mas valorado por mi". La campana de Gama debe trabajar en elevar la percepcion de que Gama tiene atencion y rapidez — no en reclamar que son importantes (todos lo saben).

### 5.3 Mundo de marca de Gama: alineacion con lo que sus preferentes valoran

El mundo de marca de Gama en el mercado total es: **Limpieza + Seguro + Atractiva + Calidad**. Sin embargo, lo que los preferentes de Gama valoran con maxima intensidad en TB puro es: **Rapidez (84.4%) + Atencion (71.9%) + Valer dinero (71.9%)**.

Hay una **brecha parcial** entre la imagen proyectada de Gama (ambiente-limpieza-estetica) y lo que sus leales exigen con intensidad (rapidez-atencion-valor). No es una contradiccion total — ambas dimensiones coexisten en los preferentes (en la tabla de preferentes todos los atributos suben dramaticamente). Pero si el deck V8 presenta a Gama como "la cadena de la limpieza y el ambiente", estara sub-comunicando lo que en realidad mueve la preferencia del Nucleo Leal.

**Gama deberia comunicar: atencion rapida en ambiente limpio + buen valor.** No solo el ambiente.

Lo que predice preferencia (E2) no son las importancias declaradas sino la imagen. Y la imagen de Gama en los que la prefieren tiene como atributo de sombra mas fuerte la ATENCION (+62.5 pp). La campana tiene que transferir ese atributo del grupo de leales al mercado amplio.

### 5.4 Espacio competitivo refinado — implicaciones para V8

**La confusion competitiva principal:** Gama, Rio y Plazas tienen perfiles P23 parecidos en el mercado total (todos en el cluster experiencial-limpieza). Pero sus "atributos de sombra" difieren:
- Gama: sombra = Atencion (+62.5 pp en preferentes)
- Rio: sombra = Calidad (+69 pp en compradores recientes)
- Plazas: sombra = Atencion (+68 pp en preferentes)

Gama y Plazas comparten el diferenciador de sombra (atencion). Rio tiene un diferenciador distinto (calidad de productos). Si Gama quiere defender el territorio de la atencion, necesita que el mercado amplio la vea de forma diferente a Plazas en ese atributo.

**Paramo sigue siendo el unico con imagen rica y completa.** Su imagen es high-equity en todos los atributos incluyendo precio. Competir con Paramo frontalmente es imposible para Gama — pero tampoco es necesario: los preferentes de Gama estan en un segmento que no pondera precio con intensidad maxima.

### 5.5 Implicaciones para Word V8

| Capitulo V8 | Cambio vs V7 | Fuente |
|---|---|---|
| Cap. 2 — DNA Gama | Actualizar top-5 importancia con TB puro. Subrayar Rapidez como atributo critico subestimado | E1 |
| Cap. 2 — Diferenciacion NSE | C+/C exige Atencion como #1 en TB puro — diferencial vs Total mas marcado | E1 §2.2 |
| Cap. 2 — DNA Gama vs mercado | Mundo de marca Gama = Limpieza+Seguro+Atractiva en total / Atencion es atributo sombra | E3 §4.4 |
| Cap. 2 — Espacio competitivo | Plazas = competidor perceptual mas cercano a Gama. Rio = cluster experiencial con ventaja de calidad en compradores | E3 §4.5 |
| Cap. 4 — Drivers preferencia | Las importancias no predicen preferencia (baja varianza discriminante). Lo que discrimina es la imagen P23. Modelo conceptual: percepcion → preferencia, no importancia → preferencia | E2 |
| Cap. 4 — Brecha verbal-conductual | Atencion: mercado amplio = 57% "importante" pero no "muy"; preferentes Gama = 71.9% TB puro. La campana debe intensificar la percepcion de atencion, no solo declararla | E1+E2+E3 |

---

## §6 Caveats para Bruna — CU-10

| # | Caveat | Impacto | Frase recomendada para deck |
|---|---|---|---|
| CV-10-01 | Pref-Gama n=32: todos los datos del Nucleo Leal REFERENCIALES | ALTO | "Perfil referencial n=32 — indicativo" |
| CV-10-02 | TB puro vs T2B: la correccion metodologica cambia rankings pero no invalida V7 — son dos metricas distintas | MEDIO | "TB puro complementa T2B — no lo contradice, lo afina" |
| CV-10-03 | Regresion logistica Paramo: pseudo-R²=0.021, modelo no significativo. No usar para comunicar "drivers de preferencia Paramo" como hecho firme | ALTO | "Modelo logistico descriptivo e indicativo — no inferencial" |
| CV-10-04 | E2 para 7 cadenas excluidas: sin regresion. El analisis descriptivo de diferencias de importancia es valido como contexto, no como driver analysis formal | MEDIO | "Drivers por cadena indicativos — bases insuficientes para regresion" |
| CV-10-05 | Tabla experiencia reciente (P24): denominador = n que compraron en esa cadena (no n total). Los % son altos por diseño — no comparar directamente con tabla total sin ajustar | ALTO | "Tabla experiencia: base = compradores recientes de esa cadena, NO muestra total" |
| CV-10-06 | P23 vs P21: asociacion inducida ≠ razon espontanea de preferencia. Las dos metricas se complementan — el deck no debe presentar P23 como "por que eligio Gama" sino como "imagen que el mercado tiene de Gama" | MEDIO | "P23 = imagen de mercado, no razon de preferencia" |
| CV-10-07 | Mundo de marca: el "atributo sombra" es especulativo cuando n_pref < 30 — basado en brechas, no en test estadistico | MEDIO | "Atributo sombra indicativo — brecha descriptiva, no estadisticamente confirmada" |

---

## §7 Handoff para Main Claude / Vivienne — V8

| Entregable CU-10 | Capitulo Word V8 | Tipo de elemento |
|---|---|---|
| E1 tabla TB puro Total | Cap. 2 — Importancia atributos | Tabla actualizada (reemplaza tabla V7) |
| E1 reranking TB vs T2B | Cap. 2 — Nota metodologica o box de insight | Nota "la correccion de Cora" |
| E1 Pref-Gama TB | Cap. 2 — Perfil Nucleo Leal | Tabla REFERENCIAL con footnote |
| E1 por cadena preferida | Cap. 2 — Tabla comparativa marcas | Tabla heatmap (ver plot) |
| E2 VIF + decision | Cap. 4 — Drivers / Nota metodologica | Parrafo de transparencia metodologica |
| E2 regresion Paramo | Cap. 4 | Tabla coefs + interpretacion cautelosa |
| E2 descriptivo Gama | Cap. 4 | Diferencias de importancia Nucleo Leal |
| E3 tabla P23 total | Cap. 2 — Mundo de marca | Tabla heatmap (ver plot) |
| E3 brechas Gama | Cap. 2 — DNA Gama | Grafico tornado Gama brechas |
| E3 experiencia | Cap. 2 — Validacion por experiencia | Tabla con nota de denominador |
| E3 mundos de marca | Cap. 2 — Positioning statements | Tabla resumen 8 cadenas |
| E4 sintesis | Cap. 4 — Implicaciones + Cap. 5 — Conclusiones | 5 parrafos |

---

*CU-10 producido por Cuanti V8 — 2026-05-18.*
*Extiende CU-1..CU-9 — no reemplaza.*
*JSON canonico: `outputs/json/CU10_v8_analisis_20260518.json`*
*Scripts: `scripts/cu10_v8_analisis.py` (E1+E2) + `scripts/cu10_v8_e3_fix.py` (E3)*
*Plots: `outputs/plots/cu10_*.png`*
*Gate Bruna: obligatorio antes de deck publico. Ver §6.*
*Handoff Main Claude/Vivienne: §7.*
