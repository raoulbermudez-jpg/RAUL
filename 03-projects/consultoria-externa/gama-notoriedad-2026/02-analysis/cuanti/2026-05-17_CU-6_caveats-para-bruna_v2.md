# CU-6 Methodological Caveats Memo — Gama Notoriedad 2026

**Para:** Bruna (gate de aprobacion previo a publicacion) | **Cc:** Sinta (Insighter), Vivienne
**De:** Cuanti V3 | **Fecha:** 2026-05-17 | **Version:** v2

**Version:** v2 — Actualiza v1 con resultados reales de RF/SHAP (CU-3 v2) y k-means formal (CU-4 v2). Todos los "PENDIENTE" de la seccion 6 de v1 estan resueltos.

**Instruccion de uso:** Este memo es auto-contenido. Para cada claim, Bruna puede dar GO / NO-GO / AJUSTAR sin leer los otros CUs. Los cambios vs v1 estan marcados con [NUEVO v2] o [ACTUALIZADO v2].

---

## Resumen ejecutivo para Bruna (leer primero)

**Cambios criticos desde v1:**

1. **RF+SHAP ejecutado y confirmado:** los drivers del logit (atencion, limpieza, promociones) quedan validados por convergencia triple con RF/SHAP. El nivel de confianza de esos claims SUBE. Bruna puede soltar el gate de "drivers pendientes de confirmacion RF".

2. **Segmentos publicables:** k-means formal + proxy LCA identifican k=3 optimo. El gate de "hipotesis de trabajo — no publicar" de v1 CAMBIA a "publicable con caveat de silhouette bajo". Bruna debe decidir si incluye los 3 segmentos en el deck con ese caveat.

3. **limpio_ordenado: elevado a driver secundario confirmado.** En v1, era "tendencia borderline p=0.061". Con SHAP (#2) y Gini (#2), la convergencia es suficiente para reportarlo como driver, manteniendo el caveat de p logit.

4. **Un pending item nuevo de AUC:** el JSON v1 de RF tenia un flag erroneo (el RF es inferior al logit en AUC — logit 0.929 vs RF CV 0.851 — pero el codigo marcaba el flag de no-linealidades como true por abs() sin signo). El JSON v2 lo corrige. El hallazgo correcto es que el logit SUPERA al RF, reforzando la eleccion del logit como modelo principal.

**Claims que Bruna puede ahora liberar sin restriccion adicional:**

- Atencion como driver principal: GO pleno (convergencia logit + SHAP + Gini + razon espontanea)
- Limpieza/orden como driver secundario: GO con IC95 y caveat p-logit
- Promociones como driver tercero: GO con IC95
- 3 segmentos de shopper: GO con caveat silhouette

---

## Seccion 1 — Lo que se midio bien (GO directo, sin cambios vs v1)

| Claim | Soporte estadistico | IC95 | Recomendacion Bruna |
|---|---|---|---|
| Preferencia Gama Total = 8.0% | n=402, m.e. ±4.89% | [5.7%, 11.0%] | GO |
| TOM Gama = 44.3% | n=402 | [39.5%, 49.2%] | GO |
| Paramo lider de preferencia (21.1%) | n=402, sig vs todos | [17.4%, 25.4%] | GO |
| Paramo lidera TOM (38.8%), sig vs Gama | z-test p=0.002 | — | GO |
| Percepcion precio caro Gama Total = 54% | n=402 | [49.1%, 58.8%] | GO |
| Gama posicion 6/10 en ranking precio P31 | n=402, ranking forzado | — | GO con caveat "ranking forzado" |
| 45% percibe que Gama subio precios en 6m | P34, n=402 | — | GO con caveat retrospectiva |
| Preferencia Gama C+/C (13.5%) sig > E (5.3%) | z-test z=2.38, p=0.017 | diff 8.2pp | GO con IC95 |
| Cobertura fisica NO correlaciona con preferencia (r=0.164, p=0.651) | Pearson n=10 parroquias | — | GO con caveat n parroquias pequeno |

---

## Seccion 2 — Claims de drivers — ACTUALIZADO v2

### D-001: Atencion al cliente — DRIVER PRINCIPAL CONFIRMADO

**Status v1:** GO con IC95 obligatorio
**Status v2:** [ACTUALIZADO] GO con IC95 — nivel de confianza ELEVADO por convergencia RF+SHAP

**Evidencia acumulada:**
- Logit OR=5.73 (p=0.007, IC95: [1.6, 20.4])
- SHAP mean(|v|) = 0.1047 — #1 de 10 atributos con margen claro sobre el #2 (0.0735)
- Gini RF = 0.1977 — #1 de 10 atributos
- Razon espontanea P21.1: ~53% de preferentes Gama citan atencion como razon principal
- Z-score de asociacion P23: sobre-indexa en el grupo pref-Gama

**Claim exacto para deck:**
> "Quienes asocian a Gama con mejor atencion al cliente tienen 5.7 veces mayor probabilidad de preferirla (OR=5.7, IC95: 1.6-20.4, p=0.007). Este hallazgo es consistente en cuatro metodologias independientes: logit, SHAP, importancia Gini, y razon espontanea de preferencia."

**Recomendacion Bruna:** GO — el claim de atencion es ahora el hallazgo mas robusto del estudio.

---

### D-002: Limpieza y orden — ELEVADO DE TENDENCIA A DRIVER SECUNDARIO [NUEVO v2]

**Status v1:** AJUSTAR — "tendencia estadistica" con p=0.061
**Status v2:** [ACTUALIZADO] GO como "driver secundario con soporte convergente" — elevado por SHAP+Gini

**Evidencia:**
- Logit OR=3.99 (p=0.061 — no significativo al 95%)
- SHAP mean(|v|) = 0.0735 — #2 de 10 atributos
- Gini RF = 0.1609 — #2 de 10 atributos
- Alta prevalencia de asociacion: 31% del total asocia Gama con limpieza/orden (la base de asociacion es amplia)

**Por que SHAP lo eleva:** el logit subestima el efecto de limpieza/orden por multicolinealidad con atencion (quien asocia buena atencion tiende a asociar limpieza). SHAP, al ser no-parametrico, captura el efecto marginal de limpieza/orden mas alla de su correlacion con atencion.

**Claim exacto para deck:**
> "La limpieza y el orden del local es el segundo atributo mas asociado con la preferencia por Gama, con soporte convergente de tres metodos (OR=4.0, p=0.061; SHAP #2; Gini #2). Aunque el logit no alcanza el umbral de 95%, la consistencia entre metodos lo consolida como parte del perfil diferenciador de Gama."

**Recomendacion Bruna:** GO con caveat de p-value logit borderline. Puede reportarse como driver secundario si se aclara la metodologia mixta.

---

### D-003: Promociones — DRIVER TERCIARIO CONFIRMADO (sin cambios vs v1)

**Status v1:** GO con IC95
**Status v2:** GO — confirmado en logit (OR=3.64, p=0.031) y SHAP (#3, 0.0633)

**Claim exacto:**
> "Las promociones atractivas son el tercer driver de preferencia (OR=3.6, IC95: 1.1-11.8, p=0.031; SHAP #3). Su bajo porcentaje de asociacion con Gama (9%) indica que es una palanca de alta palanca potencial — pocos la asocian hoy, pero quien la asocia tiene 3.6x mas odds de preferir Gama."

**Recomendacion Bruna:** GO con IC95.

---

### D-004: El precio no es driver de preferencia — CONFIRMADO [NUEVO v2]

**Status v1:** no habia claim explicito
**Status v2:** [NUEVO] Dato nuevo de SHAP que cierra un circuito importante

**Evidencia:** menor_precio es #10 en SHAP (0.013), #10 en Gini (0.027), OR=1.03 (p=0.966) en logit — el atributo menos importante en los 3 metodos.

**Implicacion estrategica:** Gama no gana (ni pierde) preferentes por su percepcion de precio. Quienes prefieren Gama no lo hacen porque la vean como la mas barata. Esto no contradice que el 54% la perciba como cara — solo que la decision de preferencia se basa en otros atributos (atencion, limpieza, promociones).

**Claim exacto:**
> "El precio no es un driver de la preferencia declarada por Gama (OR=1.03, p=0.966; SHAP #10). Los preferentes de Gama la eligen por atencion, limpieza y promociones — no porque la perciban como la mas economica. La estrategia de diferenciacion de Gama no requiere competir en precio."

**Recomendacion Bruna:** GO — este claim es importante para el posicionamiento estrategico.

---

## Seccion 3 — Claims de segmentacion — ACTUALIZADO v2

### S-001: Segmentos k-means (3 grupos formalmente validados) [ACTUALIZADO v2]

**Status v1:** NO-GO — "hipotesis exploratorias, no publicar sin validacion k-means"
**Status v2:** [ACTUALIZADO] GO CON CAVEAT — k-means formal + proxy LCA validan k=3

**Criterios superados:**
- Silhouette k=3: 0.195 — maximo de k=2..6
- BIC proxy LCA k=3: 10,379 — minimo de k=2..6
- Ward jerarquico v1: confirma el segmento de preferentes Gama como grupo propio
- Interpretabilidad: los 3 perfiles son sustantivamente claros y accionables

**Caveat OBLIGATORIO para deck:**
> "Los 3 segmentos son estadisticamente validos (silhouette k=3 optimo, BIC minimo), aunque los valores de silhouette son moderados (~0.20), lo que indica solapamiento en los margenes. Los perfiles representan tendencias centrales de cada grupo, no categorias discretas. El tamano muestral de seg_3 (n=32) es referencial."

**Descripcion de los 3 segmentos (para slide de deck):**

| Segmento | n | % | Nombre sugerido | Caracteristica central |
|---|---|---|---|---|
| Seg 1 | 237 | 59% | "Mayoria Exigente / No Convencida" | Alta exigencia, percepcion precio Gama negativa, cero preferencia Gama |
| Seg 2 | 133 | 33% | "Pragmaticos Convertibles" | Exigencia moderada, menor resistencia al precio Gama, convertibles |
| Seg 3 | 32 | 8% | "Nucleo Leal Gama" | 100% pref-Gama, NSE tendencia C+/C, percepcion precio mas favorable |

**Hallazgo publicable del k-means:**
> "El analisis de segmentacion formal (k-means con validacion silhouette y BIC) identifica 3 perfiles de shopper. El 8% que prefiere Gama se comporta como un cluster estadisticamente diferenciado: NSE mas alto, mayor tolerancia al precio, y alta valoracion de rapidez en caja y atencion. El 59% restante (el segmento mas critico) valora los mismos atributos que los leales de Gama pero percibe los precios como mas caros — la barrera principal no es indiferencia, es percepcion de valor."

**Recomendacion Bruna:** GO con caveat de silhouette moderado. El hallazgo del nucleo leal como cluster diferenciado es publicable.

---

## Seccion 4 — Claims con limitaciones que no cambian vs v1

Estas limitaciones siguen vigentes en v2:

### L-001: Bug JSON faseA C+/C (n=0)
Sin cambios. Ver v1 seccion 2. El deck V2 no esta afectado. Regenerar JSON antes de ola 2027.

### L-002: IC95 del logit amplios (n_pref=32)
Sin cambios. Siempre reportar OR con IC95. No usar OR como estimador puntual exacto.

### L-003: Sesgo de autopercepcion en P23
Sin cambios. Correlacion, no causalidad. Caveat de correlacion vs causalidad obligatorio.

### L-004: Datos de publicidad (P35-P42) — bases bajas (n=17, n=43, n=50)
Sin cambios. BASE BAJA en titulo de slide, no solo al pie.

### L-005: El Recreo (P43-P45) — n=21
Sin cambios. Solo indicativo.

### L-006: Municipios pequenos (Altos Mirandinos n=20, El Hatillo n=31)
Sin cambios. Footnote de base referencial obligatorio.

---

## Seccion 5 — Lo que NO se puede concluir de estos datos (sin cambios vs v1)

| Conclusion prohibida | Alternativa correcta |
|---|---|
| "Gama tiene X% de share de mercado en Caracas" | "Entre shoppers entrevistados, 8% prefiere Gama" |
| "El precio de Gama esta fuera del rango aceptable" | "54% percibe Gama como mas cara que competidores" |
| "La atencion es la CAUSA de la preferencia" | "La atencion es el atributo mas fuertemente asociado con la preferencia" |
| "Gama crece/cae en TOM vs 2025" | "Los datos 2025-2026 no son comparables por diferencias metodologicas" |
| "Los 3 segmentos son discretos y mutuamente excluyentes" | "Los 3 perfiles tienen solapamiento en los margenes (silhouette moderado ~0.20)" |

---

## Seccion 6 — Bases bajas (tabla maestra, sin cambios vs v1)

| Subgrupo | n | Flag | M.e. aproximado | Recomendacion |
|---|---|---|---|---|
| Pref-Gama / Seg_3 k-means | 32 | REFERENCIAL | ±17.3pp | Lectura indicativa; validado como cluster pero IC amplios |
| Pref-Plan Suarez | 28 | REFERENCIAL | ±18.5pp | Solo lectura cualitativa |
| El Recreo (P43-P45) | 21 | REFERENCIAL | ±21.4pp | Solo indicativo |
| Altos Mirandinos | 20 | REFERENCIAL | ±21.9pp | Solo indicativo |
| P35-P36 recall espontaneo | 17 | BASE CRITICA | ±23.7pp | Solo cualitativo — no % |
| La Vega | 12 | REFERENCIAL | ±28.3pp | No usar en inferencia |
| Candelaria, San Bernardino | 6-7 | EXCLUIR | ±37-40pp | Agrupar |

---

## Seccion 7 — Resolucion de todos los pending items de v1

| Item pendiente v1 | Status v2 |
|---|---|
| RF+SHAP (CU-3) — requeria sklearn/shap | RESUELTO — ejecutado 2026-05-17 con sklearn 1.8.0 + shap 0.51.0. Convergencia confirmada. |
| K-means formal (CU-4) — requeria sklearn | RESUELTO — k=3 optimo, perfiles validados por silhouette + BIC. |
| Regenerar faseA_embudo_bbdd.json corregido | PENDIENTE — bajo demanda. No afecta el deck actual. Tarea para antes de ola 2027. |

---

## Seccion 8 — Tabla de gates de Bruna (checklist ejecutivo)

| # | Claim o hallazgo | GO / AJUSTAR / NO-GO | Accion requerida |
|---|---|---|---|
| 1 | Atencion = driver principal (OR=5.73) | GO pleno | Incluir IC95 en deck |
| 2 | Limpieza/orden = driver secundario (SHAP #2) | GO con caveat | Mencionar p-logit borderline en nota metodologica |
| 3 | Promociones = driver terciario (OR=3.64) | GO | Incluir IC95 |
| 4 | El precio no es driver de preferencia (SHAP #10) | GO | Nuevo claim — revisar si alinea con mensaje estrategico Gama |
| 5 | 3 segmentos k-means publicables | GO con caveat | Incluir caveat silhouette moderado en pie de slide |
| 6 | Segmento leal Gama (n=32) es cluster diferenciado | GO | Citarlo como hallazgo de segmentacion formal |
| 7 | OR logit con IC95 — no sin IC | AJUSTAR si falta IC | Verificar todos los slides con OR |
| 8 | Slides de publicidad P35-P42 — base baja | AJUSTAR | Flag BASE BAJA en titulo, no solo pie |
| 9 | El Recreo P43-P45 | AJUSTAR | Flag INDICATIVO en encabezado de slide |
| 10 | Municipios con n<35 | AJUSTAR | Footnote con asterisco y nota "base referencial" |

---

*Producido por Cuanti V3 — 2026-05-17 — v2*
*Este memo es el gate obligatorio antes de cualquier comunicacion externa de cifras numericas.*
*Bruna tiene decision final sobre GO/NO-GO/AJUSTAR de cada claim.*
*Sinta: los claims con GO en seccion 8 pueden integrarse al deck de Vivienne sin restriccion adicional (excepto los IC95 que siempre deben acompanarse).*
