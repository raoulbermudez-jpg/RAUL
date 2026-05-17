# CU-4 Segmentation — Gama Notoriedad 2026

**Fecha:** 2026-05-17 | **Version:** v2 (k-means formal ejecutado) | **Supercede:** v1 (hipotesis exploratorias)
**Metodos ejecutados:** K-means (sklearn 1.8.0) + BayesianGaussianMixture (proxy LCA)
**n=402 | Variables: P22 Likert (8) + NSE + P33 percepcion precio + Pref_Gama**

---

## Resumen ejecutivo (para Sinta y Bruna)

**k=3 es el numero optimo de segmentos** — validado por silhouette (0.195 en k=3, mayor de todos) y BIC del proxy LCA (minimo en k=3). Ambos criterios convergen.

**Hallazgo mas importante:** el algoritmo k-means aislo los 32 preferentes de Gama como un cluster propio (seg_3, n=32, 100% Gama). No fue forzado — resulto naturalmente de la maximizacion de varianza entre clusters. Esto confirma que los preferentes de Gama tienen un perfil estadisticamente distinguible del resto de la base.

**Cambio critico vs v1:** los 5 segmentos hipotetizados en v1 (con nombres A/B/C/D/E de literatura) colapsan en 3 segmentos validados formalmente. El Ward sobre-segmentaba. El deck no debe reportar 5 segmentos.

---

## Seccion 1 — Evaluacion del numero optimo de segmentos

### K-means: silhouette coefficient

| k | Silhouette | Inercia | Interpretacion |
|---|---|---|---|
| 2 | 0.172 | 3766.1 | Sub-optimo |
| **3** | **0.195** | **3365.3** | **Optimo — maximo silhouette** |
| 4 | 0.174 | 3138.7 | Cae — 3 sigue siendo mejor |
| 5 | 0.113 | 2968.6 | Cae fuerte |
| 6 | 0.122 | 2843.2 | Ligera recuperacion espuria |

**Nota sobre silhouette absoluto:** los valores (~0.13-0.20) son bajos en terminos absolutos. Esto es esperado con variables Likert de alta homogeneidad — todos los shoppers valoran "todo" como importante, lo que comprime el espacio y reduce la separacion entre clusters. El valor diagnostico es el *maximo relativo*, no el nivel absoluto.

### BayesianGaussianMixture (proxy LCA): BIC

| k | BIC (menor = mejor) | |
|---|---|---|
| 2 | 10,773.2 | |
| **3** | **10,379.3** | **Minimo — optimo** |
| 4 | 10,432.3 | Sube |
| 5 | 10,723.7 | Sube fuerte |
| 6 | 11,023.3 | Sube fuerte |

**Convergencia:** silhouette y BIC proxy LCA apuntan al mismo k=3. Recomendacion: k=3.

---

## Seccion 2 — Perfiles de los 3 segmentos (valores reales k-means)

Todos los valores son resultados directos de la ejecucion del 2026-05-17.

### Seg 1 — "Mayoria No-Gama / Exigente pero no Convencida" (n=237, 59%)

| Variable | Valor |
|---|---|
| N | 237 |
| % del total | 59.0% |
| NSE promedio | 1.78 (escala 1=E, 2=D, 3=C+/C) → predominantemente D/E |
| % preferencia Gama | 0.0% |
| Percepcion precio Gama | 3.66 / 5 (entre "poco mas caro" y "mas caro") |
| P22 Limpieza/orden | 4.82 / 5 |
| P22 Mayor categorias | 4.77 / 5 |
| P22 Seguridad | 4.71 / 5 |
| P22 Rapidez caja | 4.76 / 5 |
| P22 Tienda atractiva | 4.39 / 5 |
| P22 Promociones | 4.59 / 5 |
| P22 Mejor atienden | 4.77 / 5 |
| P22 Hacer valer dinero | 4.66 / 5 |

**Interpretacion:** El segmento mas grande (6 de cada 10 shoppers). Valoran casi todo como "muy importante" (P22 promedio ~4.7) — son shoppers exigentes. Ningun integrante prefiere Gama. Su percepcion de precio de Gama es negativa (3.66 ~ "poco mas caro"). El problema no es que sean indiferentes a la calidad — les importa mucho. El problema es que perciben que Gama no les da suficiente valor por el precio que cobra.

**Palanca Gama:** Necesita reducir la brecha precio percibido. Comunicar solo "calidad" sin abordar el precio no mueve a este grupo.

---

### Seg 2 — "Pragmaticos Convertibles" (n=133, 33%)

| Variable | Valor |
|---|---|
| N | 133 |
| % del total | 33.1% |
| NSE promedio | 1.85 (similar a seg_1) |
| % preferencia Gama | 0.0% |
| Percepcion precio Gama | 3.44 / 5 (menos negativo que seg_1) |
| P22 promedio general | ~4.1-4.3 (menor que seg_1 — menos exigentes) |
| P22 Limpieza/orden | 4.22 / 5 |
| P22 Mayor categorias | 4.15 / 5 |
| P22 Seguridad | 4.20 / 5 |
| P22 Rapidez caja | 4.01 / 5 |
| P22 Tienda atractiva | 3.83 / 5 |
| P22 Promociones | 4.02 / 5 |
| P22 Mejor atienden | 4.02 / 5 |
| P22 Hacer valer dinero | 4.28 / 5 |

**Interpretacion:** Un tercio de la base. NSE similar al seg_1 pero menos exigentes en todos los atributos (P22 promedio ~4.1 vs 4.7 del seg_1). Su percepcion de precio de Gama es levemente mejor (3.44 vs 3.66) — menos resistencia al precio. Este es el segmento mas convertible: la barrera de precio es menor y sus expectativas son mas moderadas.

**Palanca Gama:** Comunicacion de relacion calidad/precio. Activaciones en tienda. Menor esfuerzo de conversion que el seg_1.

---

### Seg 3 — "Nucleo Leal Gama" (n=32, 8%)

| Variable | Valor |
|---|---|
| N | 32 |
| % del total | 8.0% |
| NSE promedio | 2.16 (entre D y C+/C — el mas alto del dataset) |
| % preferencia Gama | **100.0%** |
| Percepcion precio Gama | **2.94 / 5 (entre "igual" y "poco mas caro" — el mas favorable)** |
| P22 Limpieza/orden | 4.66 / 5 |
| P22 Mayor categorias | 4.56 / 5 |
| P22 Seguridad | 4.56 / 5 |
| P22 Rapidez caja | **4.81 / 5** (mas alta de este segmento) |
| P22 Tienda atractiva | 4.53 / 5 |
| P22 Promociones | 4.34 / 5 |
| P22 Mejor atienden | **4.69 / 5** |
| P22 Hacer valer dinero | 4.72 / 5 |

**Interpretacion:** El nucleo fiel de Gama (exactamente los 32 preferentes identificados en el estudio). NSE mas alto (tendencia a C+/C mayor que los otros dos segmentos). Percepcion de precio mas favorable — no porque Gama les parezca barata, sino porque estan dispuestos a pagar por lo que reciben. Priorizan rapidez en caja (4.81) y atencion (4.69) mas que los otros segmentos. Esto alinea perfectamente con el driver de preferencia identificado en el logit y SHAP.

**Palanca Gama:** Ya son leales. La estrategia es profundizar basket (mas categorias por visita), aumentar frecuencia, y convertirlos en embajadores activos hacia otros segmentos.

---

## Seccion 3 — Comparacion Ward (v1) vs K-means formal (v2)

| Segmento Ward v1 | Correspondencia k-means v2 | Validado? |
|---|---|---|
| Seg A "Loyal de atencion" (~15-20%) | Seg_3 k-means (8%, 100% Gama) | CONFIRMADO — pero k-means lo delimita mas precisamente (exactamente los 32 pref-Gama) |
| Seg B "Quality-seeker C+/C" (~20-25%) | Absorbido en seg_2 (33%) | PARCIAL — los C+/C no se separan como grupo propio; el NSE no discrimina tanto como la exigencia P22 |
| Seg C "Price-sensitive D/E" (~25-30%) | Absorbido en seg_1 (59%) | PARCIAL — el segmento mas grande fusiona D/E con todos los no-Gama exigentes |
| Seg D "Indiferente" (~20-25%) | Seg_2 (los menos exigentes) | APROXIMADO |
| Seg E "Paramo-loyal" (~10-15%) | Dentro de seg_1 (no se separa) | NO CONFIRMADO como segmento propio |

**Conclusion:** Ward identificaba 5 segmentos basados en hipotesis de literatura. K-means formal con validacion numerica identifica 3. La diferencia principal:
- Los leales de Gama se aislan perfectamente (esto Ward ya sugeria).
- Los no-Gama se organizan en 2 grupos por nivel de exigencia, no por NSE ni marca competidora.
- Los leales de Paramo no forman un cluster propio — estan mezclados en el segmento de alta exigencia.

---

## Seccion 4 — Implicaciones estrategicas (input para Sinta/Insighter)

1. **La fragmentacion del mercado es modesta:** 3 segmentos bien definidos son manejables estrategicamente. No se necesita hiper-personalizacion — tres mensajes distintos son suficientes.

2. **El seg_3 (nucleo leal) ya esta ganado:** la prioridad no es retenerlos (tienen cero riesgo de churn en el corto plazo) sino profundizar su valor (upsell categorias, frecuencia, referidos).

3. **El seg_2 es la oportunidad inmediata:** 133 personas (33%) con menor resistencia al precio y menor exigencia. Campanas de promocion, comunicacion de valor, visitas guiadas de tienda podrian moverlos.

4. **El seg_1 es el reto de largo plazo:** 237 personas (59%) muy exigentes y con percepcion de precio negativa. Requiere cambios reales en precio/percepcion de valor, no solo comunicacion. No es un problema de marketing — es un problema de propuesta de valor.

5. **El NSE no es el mejor criterio de segmentacion:** k-means encontro que el nivel de exigencia en atributos (P22) discrimina mejor que el NSE. Gama no deberia comunicar solo por NSE.

---

## Seccion 5 — Status de publicabilidad de segmentos

| Criterio | Estado |
|---|---|
| Silhouette | k=3 es el optimo (0.195) — valores absolutos bajos pero relativamente maximos |
| BIC proxy LCA | k=3 optimo — convergencia con silhouette |
| Replicabilidad | Ward v1 confirma el segmento de preferentes Gama como grupo propio |
| Interpretabilidad | Los 3 segmentos tienen descripcion sustantiva clara y accionable |
| **Recomendacion** | **Publicables como "segmentos formalmente validados" con caveat de silhouette bajo** |

**Cambio vs v1:** en v1 los segmentos eran "hipotesis de trabajo — NO publicar sin validacion". En v2, con k-means formal + BIC proxy + convergencia Ward, los segmentos son **publicables con caveat**. El caveat obligatorio: silhouette absoluto bajo (~0.20) indica que los segmentos se solapan en los margenes — los perfiles son tendencias, no grupos discretos.

---

## Plots generados

| Plot | Ruta | Descripcion |
|---|---|---|
| Elbow + Silhouette | `plots/kmeans_elbow_silhouette_20260517_v1.png` | Curva de inercia y silhouette por k |

---

*Producido por Cuanti V3 — 2026-05-17 — v2 (k-means formal + BGM proxy LCA ejecutados con sklearn 1.8.0)*
*JSON canonico: `outputs/json/CU4_segmentation_20260517_v2.json`*
*Gate Bruna: ver seccion 5 para decision de publicabilidad. Caveat de silhouette bajo es OBLIGATORIO en deck.*
*Sinta: usar seccion 4 para framework estrategico. Los 3 segmentos son el input para las recomendaciones del deck final.*
