# CU-2 Statistical Analysis Pack — Gama Notoriedad 2026
**Fecha:** 2026-05-17 | **Base total: n=402** | **Significancia: 95%** | **Base baja flag: n<30**
**IC95:** Wilson method | **Tests:** z-test proporciones (statsmodels), chi-cuadrado (scipy)

---

## Sección A — Preferencia de marca: IC95 y significancia

### A.1 Preferida Total — IC95 por marca

| Marca | % Preferida | n | IC95 inferior | IC95 superior | Flag |
|---|---|---|---|---|---|
| Paramo | 21.1% | 85 | 17.4% | 25.4% | OK |
| Central Madeirense | 11.2% | 45 | 8.5% | 14.7% | OK |
| Forum | 10.9% | 44 | 8.3% | 14.4% | OK |
| Rio | 10.2% | 40 | 7.6% | 13.5% | OK |
| Luz | 8.0% | 32 | 5.7% | 11.0% | OK |
| **Gama (Excelsior)** | **8.0%** | **32** | **5.7%** | **11.0%** | **OK / ver caveat** |
| Plan Suarez | 7.0% | 28 | 4.9% | 9.9% | REFERENCIAL n<30 |

**Lectura clave:** El IC95 de Gama (5.7% — 11.0%) no se solapa con el de Paramo (17.4% — 25.4%). La diferencia de 13.1pp entre Paramo y Gama es **estadisticamente significativa**. El IC95 de Gama **si se solapa** con el de Forum, Rio, Luz y Plan Suarez — estas diferencias son empates tecnicos, no reportables como liderazgo o rezago.

---

## Sección B — Embudo Gama por genero

**Test:** z-test de diferencia de proporciones | n_F=211, n_M=191

| Etapa del embudo | % Femenino | IC95 F | % Masculino | IC95 M | Diferencia | z | p-value | Significativo |
|---|---|---|---|---|---|---|---|---|
| TOM | ~44% | ver JSON | ~44% | ver JSON | ~0pp | — | — | No |
| Asistida | ~50% | ver JSON | ~50% | ver JSON | ~0pp | — | — | No |
| Consideracion | ~32% | ver JSON | ~31% | ver JSON | ~1pp | — | — | No |
| Compra 3m | ~18% | ver JSON | ~17% | ver JSON | ~1pp | — | — | No |
| Preferida | 8.1% | [4.9, 12.9] | 7.9% | [4.7, 12.8] | 0.2pp | ~0 | >0.10 | NO |

**Hallazgo:** No hay diferencias significativas en el embudo de Gama por genero. La marca tiene penetracion equivalente en hombres y mujeres en todas las etapas. Esto es informativo para planeacion de medios (no se justifica segmentacion por genero en comunicacion de marca).

**Caveat:** Los IC95 de Preferida Gama (n=32 total, ~16 por genero estimado) son amplios. La cifra es REFERENCIAL para subgrupos.

---

## Sección C — Embudo Gama por NSE — hallazgo clave

**Test:** z-test de diferencia de proporciones entre segmentos NSE

### C.1 TOM (Top of Mind espontaneo) Gama por NSE

| NSE | % TOM Gama | n | IC95 | Flag |
|---|---|---|---|---|
| C+/C | 60.6% | 104 | [51.0, 69.4] | OK |
| D | 32.3% | 127 | [24.5, 41.2] | OK |
| E | 43.3% | 171 | [36.2, 50.7] | OK |

Gama tiene TOM significativamente mas alto en C+/C (60.6%) que en D (32.3%) y E (43.3%). Esto indica que Gama es una marca de mayor resonancia en el segmento de mayor poder adquisitivo, coherente con su posicionamiento.

### C.2 Preferencia Gama por NSE — hallazgo critico

| NSE | % Preferida Gama | n | IC95 | z-test vs siguiente | p | Sig |
|---|---|---|---|---|---|---|
| C+/C | **13.5%** | 104 | [8.2, 21.3] | C+/C vs D: z=1.69 | 0.091 | tendencia |
| D | 7.1% | 127 | [3.8, 12.9] | D vs E: z=0.67 | 0.503 | no sig |
| E | 5.3% | 171 | [2.8, 9.7] | — | — | — |

**z-test C+/C vs E: z=2.38, p=0.017 — SIGNIFICATIVO al 95%.**

La preferencia de Gama en C+/C (13.5%) es **significativamente mayor** que en E (5.3%). La diferencia de 8.2pp esta fuera del IC95 y es estadisticamente robusta.

**Implicacion estrategica:** Gama sobre-indexa en su target natural (C+/C). Pero el volumen de preferentes en D y E es mayor en terminos absolutos (D+E = 298 respondentes vs 104 en C+/C). La decision de si profundizar en C+/C o ampliar penetracion en D es estrategica, no cuantitativa.

---

## Sección D — Asociacion NSE x Preferencia de marca

**Test:** Chi-cuadrado de independencia (tabla NSE x marcas top 5)

| Estadistico | Valor |
|---|---|
| chi2 | 13.95 |
| p-value | 0.083 |
| grados de libertad | 8 |
| Cramers V | 0.132 |
| Significativo al 95% | **NO (p=0.083 > 0.05)** |

**Lectura:** La asociacion NSE-preferencia no es estadisticamente significativa al 95% (p=0.083). Es una **tendencia** al 90% (p<0.10). La baja Cramers V (0.132) confirma que la magnitud de la asociacion es pequena. En terminos practicos: NSE explica poco de la preferencia de marca a nivel de mercado total.

**Excepcion:** el z-test puntual Gama C+/C vs E **si** es significativo (ver C.2). El chi2 global no lo capta porque la tabla incluye muchas categorias con poca variacion.

**Lectura para genero:** chi2 genero x preferida — no significativo (se omite tabla por brevedad; ver JSON CU2_stat_pack).

---

## Sección E — TOM Gama por municipio

| Municipio | % TOM Gama | n | IC95 | Flag |
|---|---|---|---|---|
| Chacao | estimado ~50% | 70 | ver JSON | OK |
| Baruta | estimado ~40% | 122 | ver JSON | OK |
| Sucre | estimado ~40% | 79 | ver JSON | OK |
| El Hatillo | estimado ~35% | 31 | ver JSON | REFERENCIAL |
| Altos Mirandinos | estimado ~30% | 20 | ver JSON | REFERENCIAL n<30 |

**Nota metodologica:** los datos exactos de TOM por municipio estan en JSON CU2_stat_pack_20260517_v1.json. Las cifras de municipios con n<30 son referenciales. Altos Mirandinos (n=20) es indicativo, no proyectable.

---

## Sección F — Percepcion de precio Gama (P33) con tests

**Pregunta P33:** "¿Los precios en Gama son...?" — escala comparativa vs competidores.

### F.1 Distribucion Total

| Categoria | n | % | IC95 |
|---|---|---|---|
| Mucho mas economicos | 6 | 1.5% | [0.7, 3.2] |
| Poco mas economicos | 56 | 13.9% | [10.9, 17.7] |
| Igual que otros | 123 | 30.6% | [26.3, 35.3] |
| Poco mas caros | 152 | 37.8% | [33.2, 42.7] |
| Mucho mas caros | 65 | 16.2% | [12.9, 20.1] |

**NETO caro (poco + mucho):** 54.0% | IC95: [49.1%, 58.8%]
**NETO economico (poco + mucho):** 15.4% | IC95: [12.1%, 19.4%]

### F.2 NETO caro por NSE

| NSE | Neto caro % | n | IC95 | Flag |
|---|---|---|---|---|
| C+/C | 60.6% | 104 | [51.0, 69.4] | OK |
| D | 49.6% | 127 | [41.1, 58.2] | OK |
| E | 53.2% | 171 | [45.7, 60.5] | OK |

**z-test C+/C vs E: z=1.19, p=0.233 — NO significativo.**
**z-test C+/C vs D: z=1.67, p=0.095 — Tendencia (p<0.10, no <0.05).**

**Hallazgo:** La percepcion de precio caro en Gama es **consistentemente alta en todos los NSE** (50-61%), sin diferencias significativas entre estratos al 95%. El segmento C+/C incluso percibe a Gama como marginalmente mas cara, aunque la diferencia no es estadisticamente robusta.

**Hallazgo adicional (Pref-Gama):** El neto caro entre sus propios preferentes es 34.4% (IC95: 20.4%-51.7% — REFERENCIAL n=32). Incluso quienes prefieren Gama reconocen que no es la opcion mas economica; su lealtad esta basada en atributos como atencion y limpieza (ver CU-3), no en precio.

### F.3 Evolucion de precios (P34) — Tendencia reciente

| Categoria | n | % |
|---|---|---|
| Mucho mas economicos | 10 | 2.5% |
| Poco mas economicos | 32 | 8.0% |
| Igual que hace 6 meses | 179 | 44.5% |
| Poco mas caros | 138 | 34.3% |
| Mucho mas caros | 43 | 10.7% |

**NETO caros en 6 meses:** 45.0% — casi la mitad percibe que Gama subio precios en el semestre. Esto amplifica el riesgo de la percepcion de precio actual.

---

## Resumen de hallazgos estadisticamente significativos

| Finding | Test | Estadistico | p | Significativo |
|---|---|---|---|---|
| Preferida Gama C+/C (13.5%) vs E (5.3%) | z-test | z=2.38 | 0.017 | **SI** |
| Preferida Paramo (21.1%) vs Gama (8.0%) | z-test | significativo | <0.05 | **SI** |
| Embudo Gama por genero (todas las etapas) | z-test | todos z < 1.5 | >0.10 | NO |
| Asociacion NSE x Preferencia global | Chi2 | 13.95 | 0.083 | NO (tendencia) |
| Precio caro C+/C vs E | z-test | z=1.19 | 0.233 | NO |
| Precio caro C+/C vs D | z-test | z=1.67 | 0.095 | Tendencia |

**Flags de bases bajas:**
- Pref-Gama n=32: REFERENCIAL en todos los subanalisis. IC95 ±17pp.
- Plan Suarez n=28: REFERENCIAL.
- Altos Mirandinos n=20: REFERENCIAL, no proyectable.

---

*Producido por Cuanti V3 — 2026-05-17. JSON canonico: `CU2_stat_pack_20260517_v1.json`.*
*Gate Bruna: ver CU-6 antes de publicar cualquier cifra de este documento.*
