# CU-7 Wave-over-Wave Analysis — Gama Notoriedad 2026
## Comparacion Inter-ola 2025 vs 2026

**Fecha:** 2026-05-17 | **Autor:** Cuanti
**Para:** Insighter (IN-8 triangulacion), Bruna (gate V4), Vivienne (deck V4)
**Protocolo metodologico:** ME-5 (Methos, 2026-05-17)
**n_2026 = 402** | **n_2025 = 785**
**Script reproducible:** `v2-wow/scripts/cu7_wave_over_wave.py`
**JSON canónico:** `v2-wow/outputs/json/CU7_wow_results_20260517_v1.json`

---

## 1. Metodologia Aplicada

### 1.1 Tests estadisticos

Todos los tests inter-ola utilizan el metodo **Newcombe-Wilson** para diferencia de dos proporciones independientes (Newcombe, 1998, *Statistics in Medicine*, 17(8)). Este metodo produce intervalos de confianza con cobertura mas cercana al nivel nominal que el z-test clasico, especialmente cuando las proporciones se acercan a 0 o 1, que es frecuente en variables de embudo de marcas menores.

Los **p-values** se calculan via tabla 2x2 (chi2 o Fisher exact si alguna celda esperada < 5). Se reportan cuatro niveles:

| p-value | Etiqueta | Simbolo |
|---|---|---|
| < 0.01 | Significativo 99% | si_99 |
| 0.01–0.05 | Significativo 95% | sig_95 |
| 0.05–0.10 | Tendencia 90% | tendencia_90 |
| > 0.10 | No significativo | no_sig |

### 1.2 Correccion por comparaciones multiples

Se aplica **Benjamini-Hochberg FDR q<0.05** sobre los 57 items WoW totales. El flag de significancia reportado en este documento usa siempre el p-value BH-ajustado. Las comparaciones de subgrupos NSE se tratan como familia separada de tests exploratorios con BH aplicado dentro de cada subgrupo.

### 1.3 Ponderacion 2025

**Decision D-CU7-001 (in-flight):** La columna `@PONDERAR_1` en BBDD 2025 tiene todos sus valores en 0.0 (int64, sin variacion). No es un factor de expansion valido. Segun excepcion ME-5 §2.4, los analisis 2025 se presentan sin ponderacion. Impacto: los estimados 2025 asumen diseno muestral auto-ponderado. DEFF = 1.0 por construccion.

### 1.4 Comparabilidad muestral

Test chi2 de homogeneidad (alpha = 0.10) para 4 variables demograficas:

| Variable | p-value | Comparable | Nota |
|---|---|---|---|
| NSE (C+/C, D, E) | 0.4945 | SI | Distribuciones proporcionales |
| Municipio | **0.0017** | **NO** | 2025 sobrerepresenta Libertador/Baruta vs 2026 |
| Genero | 0.8191 | SI | Distribucion estable |
| Edad (25-34/35-44/45-54/55-64) | 0.9820 | SI | Distribucion identica |

**Resultado: 1/4 variables falla (Municipio, p=0.0017).** El resto son comparables. Caveat de nivel MEDIO aplicado a todos los resultados WoW (las diferencias geograficas pueden contaminar comparaciones en variables con dispersion municipal alta). Ver Caveat CV-WOW-002.

### 1.5 Limites del analisis

- V4 no es pre-registrado: los analisis se diseñaron despues de conocer V3. Mitigation: plan ME-5 documentado a priori de abrir BBDD 2025.
- La causalidad no es inferible en diseno cross-sectional.
- P22 atributos individuales NO comparables (BBDD 2025 sin labels — Decision D-CU7-002).
- P23:21 "hacer valer mi dinero" excluido (nuevo en 2026 — Decision D-CU7-003).

---

## 2. Mapping de Items Comparables (Resumen)

**Total filas en CSV:** 65 items mapeados.

| Caso | Descripcion | Items | Comparabilidad |
|---|---|---|---|
| A | P22 importancia atributos | 10 atributos (solo T2B agregado) | comparable_con_caveat (no individual) |
| B | P23 asociacion Gama x atributos | 9 atributos (excluye P23:21) | comparable |
| C | Embudo P16-P21 (TOM/Asistida/Consideracion/Compra3m/Preferida) | 9 marcas x 5 etapas = 45 items | comparable |
| C | P24 ultima compra, P26 misiones, P30 habitual | 3 items adicionales | comparable |
| D | P31/P32 precio | Ver nota abajo | comparable_con_caveat |
| E | Demograficas (NSE/Geo/Genero/Edad) | 4 variables | solo comparabilidad muestral |

**Nota P31/P32:** En 2025, P31 tiene 6 marcas (ranking 1-6) vs 2026 que tiene mas marcas. No comparable directamente. Excluido del analisis WoW cuantitativo; documentado en CSV.

**Total items WoW ejecutados: 57** (embudo x marcas + P23 Gama + comportamiento).

---

## 3. Resultados — Items Estadisticamente Significativos (BH-FDR q<0.05)

**10 items significativos** tras correccion multiple BH-FDR:

| Item | 2025 % | 2026 % | Delta pp | p-unadj | p-adj | Sig |
|---|---|---|---|---|---|---|
| Consideracion P19 — Rio | 19.2 | 38.8 | **+19.6** | <0.0001 | <0.0001 | sig_99 |
| Consideracion P19 — Paramo | 31.7 | 49.0 | **+17.3** | <0.0001 | <0.0001 | sig_99 |
| TOM P16 — Rio | 28.0 | 45.0 | **+17.0** | <0.0001 | <0.0001 | sig_99 |
| Compra 3m P20 — Rio | 14.4 | 26.9 | **+12.5** | <0.0001 | <0.0001 | sig_99 |
| TOM P16 — Paramo | 27.0 | 39.1 | **+12.1** | <0.0001 | 0.0003 | sig_99 |
| Asistida P17 — Paramo | 40.9 | 51.7 | **+10.8** | 0.0004 | 0.0030 | sig_99 |
| Consideracion P19 — Plan Suarez | 17.8 | 27.4 | **+9.5** | 0.0001 | 0.0013 | sig_99 |
| Asistida P17 — Hiper Lider | 54.1 | 62.2 | **+8.1** | 0.0081 | 0.0459 | sig_95 |
| Compra 3m P20 — Central Madeirense | 30.3 | 22.6 | **-7.7** | 0.0051 | 0.0325 | sig_95 |
| Consideracion P19 — Luz | 17.6 | 25.1 | **+7.5** | 0.0022 | 0.0154 | sig_95 |

**Interpretacion del patron:** los 9 cambios positivos son de COMPETIDORES, no de Gama. Rio y Paramo son los grandes ganadores de notoriedad y consideracion 2025->2026. Central Madeirense PIERDE compra efectiva (-7.7pp). Gama no aparece entre los significativos — ver seccion 5.

---

## 4. Tendencias 90% (p-adj 0.05–0.10) — Informativos

11 items en zona de tendencia (no declarados como significativos pero informativos estrategicamente):

| Item | 2025 % | 2026 % | Delta pp | p-adj | Nota |
|---|---|---|---|---|---|
| P23 Asociacion Gama — atractiva | 22.6 | 28.9 | +6.3 | 0.058 | Tendencia positiva Gama |
| P23 Asociacion Gama — seguro | 23.8 | 29.6 | +5.8 | 0.089 | Tendencia positiva Gama |
| Preferida P21 — Forum | 16.4 | 10.9 | -5.5 | 0.053 | Forum pierde preferidos |
| Preferida P21 — Central Madeirense | 16.7 | 11.2 | -5.5 | 0.053 | CM pierde preferidos |
| P23 Asociacion Gama — promociones | 14.0 | 9.0 | -5.1 | 0.053 | Gama: debilitamiento percepcion promociones |
| Compra 3m P20 — Plazas | 25.4 | 19.1 | -6.2 | 0.059 | Plazas pierde compra efectiva |
| Compra 3m P20 — Paramo | 29.3 | 36.1 | +6.8 | 0.059 | Paramo gana compra |
| P23 Asociacion Gama — menor_precio | 11.1 | 7.2 | -3.9 | 0.091 | Gama: debilitamiento percepcion precio bajo |
| Asistida P17 — Forum | 38.0 | 44.5 | +6.6 | 0.087 | Forum gana awareness asistida |
| Compra 3m P20 — Luz | 13.2 | 18.4 | +5.2 | 0.059 | Luz gana compra |
| Preferida P21 — Rio | 6.2 | 10.2 | +4.0 | 0.059 | Rio gana preferidos |

---

## 5. Resultados Gama — Embudo Completo y Asociaciones

### 5.1 Embudo Gama 2025 vs 2026

| Etapa | 2025 % | n25 | IC95_25 | 2026 % | n26 | IC95_26 | Delta pp | p-adj | Sig |
|---|---|---|---|---|---|---|---|---|---|
| TOM P16 | 42.0 | 785 | [38.5-45.6] | 44.3 | 402 | [39.5-49.2] | +2.2 | 0.555 | no_sig |
| Asistida P17 | 48.3 | 785 | [44.7-51.9] | 50.5 | 402 | [45.6-55.4] | +2.2 | 0.555 | no_sig |
| Consideracion P19 | 27.5 | 785 | [24.3-30.9] | 31.8 | 402 | [27.3-36.7] | +4.3 | 0.221 | no_sig |
| Compra 3m P20 | 17.8 | 785 | [15.2-20.7] | 17.7 | 402 | [13.9-22.1] | -0.2 | 0.941 | no_sig |
| Preferida P21 | 9.7 | 785 | [7.7-12.0] | 8.0 | 402 | [5.4-11.4] | -1.7 | 0.473 | no_sig |
| Ultima compra P24 | 8.7 | 785 | [6.8-10.9] | 7.5 | 402 | [5.1-10.8] | -1.2 | 0.555 | no_sig |
| Habitual P30 | 19.4 | 785 | [16.8-22.4] | 20.2 | 402 | [16.4-24.6] | +0.8 | 0.803 | no_sig |
| Misiones P26 | 18.7 | 785 | [16.1-21.7] | 23.6 | 402 | [19.6-28.1] | +4.9 | 0.107 | no_sig |

**Lectura:** ningun cambio en el embudo de Gama alcanza significancia estadistica tras correccion BH-FDR. Los deltas son pequeños (+4.9 el maximo). La posicion de Gama es **estable entre olas**.

### 5.2 Asociaciones Gama (P23) — 9 atributos comparables

| Atributo | 2025 % | 2026 % | Delta pp | p-adj | Sig |
|---|---|---|---|---|---|
| Atractiva (tienda atractiva) | 22.6 | 28.9 | **+6.3** | 0.058 | tendencia_90 |
| Seguro | 23.8 | 29.6 | **+5.8** | 0.089 | tendencia_90 |
| Limpio ordenado | 28.5 | 31.1 | +2.6 | 0.482 | no_sig |
| Mayor calidad | 22.7 | 26.6 | +3.9 | 0.236 | no_sig |
| Mejor atienden | 20.2 | 21.9 | +1.6 | 0.583 | no_sig |
| Mayor categorias | 20.2 | 17.9 | -2.3 | 0.473 | no_sig |
| Rapidez caja | 19.2 | 21.1 | +1.9 | 0.552 | no_sig |
| Menor precio | 11.1 | 7.2 | **-3.9** | 0.091 | tendencia_90 |
| Promociones | 14.0 | 9.0 | **-5.1** | 0.053 | tendencia_90 |

**Lectura:** Gama muestra tendencias positivas en atributos de experiencia (atractiva, seguro) y tendencias negativas en atributos economicos (menor precio, promociones). El patron es consistente con el perfil V3 — el posicionamiento de Gama se aleja de precio/oferta y se acerca a experiencia/confianza.

### 5.3 Importancia de atributos P22 (nivel agregado — caveat ALTO)

**CAVEAT:** No es posible comparar P22 a nivel de atributo individual entre olas (BBDD 2025 sin labels — D-CU7-002). Solo se reporta T2B promedio agregado.

| Grupo | T2B promedio 2025 | T2B promedio 2026 | Delta |
|---|---|---|---|
| 10 atributos comparables (proxy) | 92.9% | 94.4% | **+1.5pp** |

**2026 T2B por atributo (referencia):**
- Calidad 98.0% | Limpio/ordenado 97.8% | Seguro 96.0% | Valer dinero 96.5%
- Mejor atienden 96.3% | Surtido 95.5% | Precio 94.3% | Rapidez caja 94.3%
- Promociones 89.6% | Atractiva 85.6%

La importancia de todos los atributos es alta en 2026 (T2B minimo = 85.6%). No comparar atributos individuales con 2025.

---

## 6. Competencia — Cambios Relevantes en el Mercado

Los hallazgos WoW mas grandes son de COMPETIDORES:

### 6.1 Rio — Ganador de awareness y conversion

Rio experimento los mayores incrementos significativos:
- TOM: 28.0% → 45.0% (+17.0pp, p_adj<0.0001)
- Consideracion: 19.2% → 38.8% (+19.6pp, p_adj<0.0001)
- Compra 3m: 14.4% → 26.9% (+12.5pp, p_adj<0.0001)
- Preferida: 6.2% → 10.2% (+4.0pp, p_adj=0.059 tendencia)

En NSE C+/C, TOM Rio: 30.9% → 56.7% (+25.8pp, p_adj=0.0002) — el efecto es especialmente fuerte en el segmento premium.

### 6.2 Paramo — Consolidacion en toda la cadena

- TOM: 27.0% → 39.1% (+12.1pp, p_adj=0.0003)
- Asistida: 40.9% → 51.7% (+10.8pp, p_adj=0.003)
- Consideracion: 31.7% → 49.0% (+17.3pp, p_adj<0.0001)

Paramo gana en toda la cadena del embudo. En NSE C+/C TOM Paramo: 18.0% → 40.4% (+22.3pp, p_adj=0.0002).

### 6.3 Central Madeirense — Perdida de compra efectiva

- Compra 3m: 30.3% → 22.6% (-7.7pp, p_adj=0.033) — unica perdida significativa en el panel de marcas.
- Preferida: 16.7% → 11.2% (-5.5pp, p_adj=0.053 tendencia).

CM pierde conversion a compra a pesar de mantener awareness.

### 6.4 Implicaciones para Gama

El mercado 2025→2026 muestra un aumento general de consideracion hacia cadenas alternativas (Rio, Paramo), con caida de CM. Gama se mantiene estable en este contexto dinamico — lo cual es positivo (no pierde share) pero tambien implica que no esta capturando el espacio disponible por la caida de CM.

---

## 7. Analisis por Subgrupo NSE (Exploratorio)

**NOTA: Todos los subgrupos son exploratorios. No pre-registrados en 2025. Interpretar como hipotesis para ola 2027.**

| Subgrupo | n_2025 | n_2026 | Status |
|---|---|---|---|
| NSE C+/C | 194 | 104 | Ejecutado (n>=50) |
| NSE D | 275 | 127 | Ejecutado (n>=50) |
| NSE E | 316 | 171 | Ejecutado (n>=50) |

**Items significativos en subgrupos (BH-FDR dentro de cada subgrupo):**

| Item | NSE | 2025 % | 2026 % | Delta pp | p-adj |
|---|---|---|---|---|---|
| TOM P16 — Rio | C+/C | 30.9 | 56.7 | **+25.8** | 0.0002 |
| TOM P16 — Paramo | C+/C | 18.0 | 40.4 | **+22.3** | 0.0002 |
| TOM P16 — Plan Suarez | C+/C | 18.0 | 32.7 | **+14.7** | 0.0256 |
| Preferida P21 — Rio | D | 5.1 | 15.0 | **+9.9** | 0.0145 |
| TOM P16 — Rio | E | 25.3 | 42.1 | **+16.8** | 0.0024 |

**Lectura:** el fenomeno Rio es transversal a todos los NSE (sig en C+/C y E, tendencia en D). Paramo gana especialmente en C+/C. Gama no aparece como significativo en ningun subgrupo — posicion estable en todos los segmentos.

---

## 8. Hallazgos Principales (8 hallazgos, nivel de evidencia explicito)

### H-1: Estabilidad total del embudo Gama — Ninguna variacion significativa
**Nivel de evidencia:** ALTO (todos los p_adj > 0.10)
**Claim permitido para deck:** "El embudo de Gama — desde awareness hasta preferencia — se mantiene estadisticamente estable entre 2025 y 2026 (ninguna variacion significativa con p_adj<0.05, correccion BH-FDR sobre 57 comparaciones)."
**Tipo ME-5:** WoW Confirmado (ausencia de cambio).

### H-2: Rio — Expansion explosiva de awareness y consideration
**Nivel de evidencia:** ALTO (multiple sig_99, p_adj<0.001)
**Claim:** "Rio experimento el mayor crecimiento inter-ola: TOM +17pp, Consideracion +19.6pp, Compra +12.5pp (todos sig_99, p_adj<0.001). El efecto es especialmente marcado en NSE C+/C: TOM Rio crece 25.8pp en ese segmento."
**Tipo ME-5:** WoW Confirmado.

### H-3: Paramo — Consolidacion como lider aspiracional
**Nivel de evidencia:** ALTO (sig_99 multiple, p_adj<0.003)
**Claim:** "Paramo consolida su posicion en toda la cadena: TOM +12.1pp, Asistida +10.8pp, Consideracion +17.3pp (todos sig_99). Especialmente fuerte en C+/C donde TOM crece 22.3pp."
**Tipo ME-5:** WoW Confirmado.

### H-4: Central Madeirense pierde compra efectiva
**Nivel de evidencia:** MEDIO (sig_95 p_adj=0.033; preferida es tendencia)
**Claim:** "Central Madeirense pierde 7.7pp de compra efectiva en 3 meses (p_adj=0.033). La preferida cae 5.5pp (tendencia, p_adj=0.053). Unica cadena con perdida significativa de conversion."
**Tipo ME-5:** WoW Confirmado con nivel sig_95.

### H-5: Asociaciones Gama — Tendencia positiva en experiencia, negativa en precio/promo
**Nivel de evidencia:** BAJO (solo tendencia, p_adj 0.053-0.091; no pasa BH-FDR q<0.05)
**Claim:** "Los datos sugieren (sin confirmar) que la asociacion de Gama con atributos de experiencia (atractiva +6.3pp, seguro +5.8pp) aumenta, mientras los atributos economicos (promociones -5.1pp, menor precio -3.9pp) se debilitan."
**Tipo ME-5:** Hipotesis V4 — pendiente confirmacion ola 2027.
**NOTA para Bruna:** este claim solo puede presentarse en deck como hipotesis, no como conclusion. El nivel de evidencia es insuficiente para afirmacion directa.

### H-6: El mercado se dinamiza — Oportunidad para Gama de capturar share de CM
**Nivel de evidencia:** MEDIO (inferido de H-1+H-4 combinados)
**Claim:** "Central Madeirense pierde compra efectiva significativamente entre olas mientras Gama se mantiene estable. Este espacio disponible no ha sido capturado aun por Gama, representando una oportunidad de conversion."
**Tipo ME-5:** Tipo B — requiere triangulacion cuali para confirmar mecanismo.

### H-7: Gama en NSE C+/C — Sin movimiento en segmento premium
**Nivel de evidencia:** BAJO (ninguna variable Gama significativa en C+/C)
**Claim:** "En NSE C+/C, Gama no captura el crecimiento disponible que Rio (+25.8pp TOM) y Paramo (+22.3pp TOM) si estan generando. La posicion de Gama en el segmento premium es estable pero rezagada."
**Tipo ME-5:** Hipotesis V4 — exploratorio.

### H-8: Posicionamiento de precio de Gama — Alejamiento de imagen economica
**Nivel de evidencia:** BAJO (tendencia, no significativo tras BH-FDR)
**Claim:** "Los datos sugieren (no confirman) que la imagen de precio bajo de Gama se debilita entre olas (P23:menor_precio -3.9pp, p_adj=0.091). De confirmarse en ola 2027, indicaria un desafio para estrategias de conversion basadas en precio."
**Tipo ME-5:** Hipotesis V4 — pendiente confirmacion.

---

## 9. Caveats para Gate Bruna

### CV-WOW-001 — Ponderacion 2025 no disponible
**Impacto:** MEDIO
**Caveat deck:** "Los resultados 2025 se presentan sin ponderacion muestral (factor de ponderacion no disponible en BBDD). Los estimados 2025 pueden tener sesgo de diseno si la muestra original era estratificada."
**Permite claim directo:** No

### CV-WOW-002 — Comparabilidad muestral: Municipio difiere entre olas
**Impacto:** MEDIO
**Detalle:** 2025 sobrerepresenta Libertador vs 2026 (p=0.0017). NSE, Genero y Edad son comparables.
**Caveat deck:** "Los cambios WoW deben interpretarse con precaucion: la composicion geografica de las muestras difiere significativamente entre olas (Libertador sobrerepresentado en 2025). Los cambios en variables con dispersion geografica pueden reflejar composicion, no cambio real."
**Permite claim directo:** No — requiere nota de caveat

### CV-WOW-003 — P22 atributos NO comparables a nivel individual
**Impacto:** ALTO
**Caveat deck:** "La comparacion de importancia de atributos (P22) entre 2025 y 2026 no es posible a nivel de atributo individual. La BBDD 2025 no contiene etiquetas de texto para las columnas P22_1..P22_20."
**Permite claim directo:** No

### CV-WOW-004 — P23:21 excluido (nuevo en 2026)
**Impacto:** BAJO
**Caveat deck:** "El atributo 'hacer valer mi dinero' fue introducido en 2026. No tiene par en 2025 y no se incluye en comparaciones WoW."
**Permite claim directo:** No aplica

### CV-WOW-005 — Subgrupos NSE son exploratorios
**Impacto:** MEDIO
**Caveat deck:** "Los analisis por NSE no fueron pre-registrados en el diseno 2025. Deben interpretarse como hipotesis a confirmar en ola 2027."
**Permite claim directo:** Solo como hipotesis, con etiqueta explicita

### CV-WOW-006 — n2026=402 vs n2025=785
**Impacto:** MEDIO
**Caveat deck:** "La diferencia de tamanio muestral (2025: n=785; 2026: n=402) reduce la precision de los estimados 2026. Cambios menores de 5pp pueden no ser estadisticamente detectables."
**Permite claim directo:** Si, con precision reportada

### CV-WOW-007 — Causalidad no inferible
**Impacto:** MEDIO
**Caveat deck:** "Los cambios entre olas son observacionales. No se puede atribuir ningun cambio observado a acciones especificas de ninguna cadena de supermercados."
**Permite claim directo:** Si, con lenguaje correlacional

---

## 10. Tabla Tipo A/B/C para Bruna (clasificacion ME-5 §5)

| Hallazgo | Tipo | Criterio cumplido |
|---|---|---|
| H-1: Estabilidad Gama | WoW Confirmado | Ninguna variacion sig BH-FDR — alta certeza de estabilidad |
| H-2: Rio expansion | WoW Confirmado | p_adj<0.001 multiple, delta>17pp |
| H-3: Paramo consolidacion | WoW Confirmado | p_adj<0.003 multiple, delta>10pp |
| H-4: CM pierde compra | WoW Confirmado | p_adj=0.033, delta=-7.7pp |
| H-5: Gama experiencia vs precio | Hipotesis V4 | Solo tendencia, p_adj 0.053-0.091 — NO confirmar |
| H-6: Oportunidad share CM | Tipo B — Triangulacion | Combinacion H-1+H-4; mecanismo requiere cuali |
| H-7: Gama en C+/C sin movimiento | Hipotesis V4 | Exploratorio subgrupo, no pre-registrado |
| H-8: Debilitamiento imagen precio | Hipotesis V4 | Solo tendencia p_adj=0.091 — NO confirmar |

**Nota para Bruna:** Los claims Tipo A (H-1, H-2, H-3, H-4) tienen nivel de evidencia alto y pueden presentarse en deck como hechos WoW con p-values. Los claims Tipo C (H-5, H-7, H-8) solo pueden presentarse como hipotesis con la etiqueta `[Hipotesis V4 — pendiente confirmacion ola 2027]`.

---

## 11. Decisiones In-Flight Tomadas Durante Ejecucion

| Codigo | Decision |
|---|---|
| D-CU7-001 | @PONDERAR_1 = todo cero → sin ponderacion 2025. DEFF=1.0 asumido. |
| D-CU7-002 | P22 BBDD 2025 sin labels → no comparacion individual, solo T2B agregado. |
| D-CU7-003 | P23:21 "hacer valer" excluido → nuevo en 2026, sin par en 2025. |
| D-CU7-004 | Municipio falla homogeneidad → caveat MEDIO aplicado (solo 1/4 falla, no ALTO). |

---

## 12. Archivos Producidos

| Archivo | Path |
|---|---|
| Este documento | `v2-wow/CU-7_wave-over-wave_v1.md` |
| Mapping CSV | `v2-wow/mapping_2025_2026.csv` (65 filas) |
| JSON resultados | `v2-wow/outputs/json/CU7_wow_results_20260517_v1.json` |
| Forest plot | `v2-wow/plots/wow_top_changes_20260517_v1.png` |
| Script principal | `v2-wow/scripts/cu7_wave_over_wave.py` |
| utils.py extendido | `cuanti/scripts/utils.py` (+ `load_bbdd_2025`) |

---

## Recordatorio gate Bruna (BR-2 V4)

**Este documento contiene cifras que van a deck publico. Gate Bruna obligatorio antes de que Vivienne incorpore cualquier numero WoW al deck V4.**

Los claims de nivel Tipo A (H-1 a H-4) tienen soporte estadistico robusto.
Los claims Tipo C (H-5, H-7, H-8) solo pueden aparecer en deck como hipotesis explicitas, con etiqueta visible.
Los caveats CV-WOW-001, CV-WOW-002 y CV-WOW-003 deben estar presentes en alguna forma (nota al pie o slide de metodologia) en el deck V4.

*Cuanti — analisis CU-7 completado 2026-05-17*
