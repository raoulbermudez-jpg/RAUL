# CU-6 Methodological Caveats Memo — Gama Notoriedad 2026
**Para:** Bruna (gate de aprobacion previo a publicacion) | **Cc:** Insighter, Vivienne
**De:** Cuanti V3 | **Fecha:** 2026-05-17

**Instruccion de uso:** Este memo es auto-contenido. Para cada claim listado, Bruna puede dar GO / NO-GO / AJUSTAR sin leer los otros cinco documentos CU-1..CU-5. Los claims de V2 estan marcados como tales; los claims nuevos de V3 tambien.

---

## Resumen ejecutivo para Bruna (leer primero)

**3 claims en riesgo que requieren decision urgente:**
1. Cualquier claim que proyecte cifras del segmento C+/C: el JSON de faseA tenia n=0 por bug. Las cifras del deck V2 son correctas (calculadas separadamente), pero hay riesgo residual en cualquier reporte que lea el JSON directamente.
2. Los OR del logit (OR=5.73 para atencion, OR=3.64 para promociones): son robustos en direccion pero los IC95 son muy anchos (ej. OR atencion puede ser 1.6 o 20.4). No reportar como "exactamente 5.7 veces mas likely" sin el IC.
3. Toda cifra de segmentacion (CU-4): los segmentos son hipotesis exploratorias — NO publicar como segmentos confirmados. Requieren validacion con k-means formal.

**7 claims completamente limpios para GO:**
Preferencia Gama 8.0% Total, TOM 44.3%, Asistida 50.2%, top drivers atencion y promociones (con IC), percepcion precio caro 54%, brecha precio vs Paramo significativa, diferencia preferencia C+/C vs E significativa.

---

## Seccion 1 — Lo que se midio bien (GO directo)

| Claim | Soporte estadistico | IC95 | Recomendacion Bruna |
|---|---|---|---|
| Preferencia Gama Total = 8.0% | n=402, m.e. ±4.89% | [5.7%, 11.0%] | GO — cifra solida |
| TOM Gama = 44.3% | n=402, z-test vs competidores | [39.5%, 49.2%] | GO |
| Paramo es el lider de preferencia (21.1%) | n=402, sig vs todos los demas | [17.4%, 25.4%] | GO |
| Paramo lidera TOM (38.8%) con ventaja sig sobre Gama | z-test p=0.002 | — | GO |
| Driver atencion: mayor que cualquier otro atributo (OR=5.73) | Logit p=0.007 + convergencia triple | IC95: [1.6x, 20.4x] | GO con IC obligatorio |
| Driver promociones: segundo lugar (OR=3.64) | Logit p=0.031 | IC95: [1.1x, 11.8x] | GO con IC obligatorio |
| Percepcion precio caro Gama Total = 54% | n=402 | [49.1%, 58.8%] | GO |
| Gama ocupa posicion 6/10 en ranking de precio | P31 ranking forzado n=402 | — | GO con caveat "ranking forzado" |
| 45% percibe que Gama subio precios en 6 meses | P34 n=402 | — | GO con caveat de retrospectiva |
| Preferencia Gama C+/C (13.5%) sig > E (5.3%) | z-test z=2.38, p=0.017 | diferencia 8.2pp | GO |
| Cobertura cobertura fisica NO correlaciona con preferencia (r=0.164, p=0.651) | Pearson n=10 parroquias | — | GO con caveat "n pequeno de parroquias" |

---

## Seccion 2 — Claims con limitaciones — AJUSTAR antes de publicar

### L-001: Cifras del segmento C+/C en general

**Contexto:** El JSON `faseA_embudo_bbdd.json` reporta n_C+/C=0 por bug de encoding. Los scripts posteriores calcularon C+/C correctamente (n=104 verificado), por lo que las cifras del deck V2 son correctas. Sin embargo, hay riesgo de confusion para cualquiera que compare JSON vs slides.

**Impacto:** Bajo en deck V2 ya entregado. Medio si se comparte el JSON con Cora o si se re-publica.

**Caveat literal para deck:** ninguno adicional necesario en V2. Para V3: verificar que toda cifra C+/C provenga de calculos directos del BBDD (lo que hace el script V3), no del JSON faseA.

**Recomendacion Bruna:** AJUSTAR — incluir nota en archivo tecnico de que JSON faseA C+/C es artefacto (no afecta deck), y regenerar ese JSON antes de ola 2027.

---

### L-002: OR del logit — reportar con IC95 obligatoriamente

**Contexto:** OR=5.73 para atencion y OR=3.64 para promociones son estadisticamente significativos pero con IC95 muy amplios (atencion: [1.6, 20.4]; promociones: [1.1, 11.8]).

**Razon:** n_pref_gama=32 (REFERENCIAL). Los SE de los coeficientes son amplios por la base pequena.

**Claim exacto que SE PUEDE publicar:**
> "Quienes asocian a Gama con buena atencion tienen significativamente mayor probabilidad de preferirla como cadena (OR=5.7, IC95: 1.6-20.4, p=0.007)"

**Claim que NO se puede publicar:**
> "Gama tiene 5.7 veces mas probabilidad de ser preferida por quienes asocian buena atencion" [sin IC → infla precision]
> "La probabilidad de preferencia es exactamente 5.7x mayor" [exactitud falsa]

**Recomendacion Bruna:** AJUSTAR — todo claim sobre drivers debe incluir IC95 o al menos la frase "con amplio rango de incertidumbre por base referencial de 32 preferentes".

---

### L-003: Convergencia triple de atencion — robusto pero con matiz de sesgo declarativo

**Contexto:** La convergencia logit + razon espontanea + z-score de asociacion para "atencion" es el hallazgo mas solido del estudio. Sin embargo, los tres metodos comparten el sesgo de autopercepcion: el respondente que prefiere Gama puede sobre-atribuir virtudes a su marca.

**Claim que SE PUEDE publicar:**
> "La evidencia convergente de tres metodologias independientes apunta a la calidad de atencion como el diferenciador central de Gama"

**Claim que requiere matiz:**
> "Los shoppers de Gama tienen 5.7 veces mas probabilidad de preferirla por la atencion" [omite que es correlacion, no causalidad]

**Caveat literal recomendado para deck:**
> "Estudio observacional — los drivers reflejan correlacion con preferencia, no causalidad demostrada."

**Recomendacion Bruna:** GO con caveat de correlacion vs causalidad. Es estandar en market research pero debe estar en notas metodologicas del deck.

---

### L-004: Limpieza/orden (OR=3.99, p=0.061) — borderline estadistico

**Contexto:** limpio_ordenado tiene OR=3.99, casi igual que el driver de promociones, pero p=0.061 (no significativo al 95%). En el V2 se reporto como "tendencia".

**Claim que SE PUEDE publicar:**
> "La asociacion con limpieza y orden muestra una tendencia consistente con la preferencia (OR=4.0, p=0.061), aunque no alcanza significancia al 95%"

**Claim que NO se puede publicar:**
> "La limpieza es el tercer driver de preferencia de Gama" [sin caveat de p>0.05]

**Recomendacion Bruna:** AJUSTAR — cambiar "driver" a "tendencia estadistica" con el p-value explicitado.

---

### L-005: Datos de publicidad (P35-P42) — bases muy bajas

**Contexto:**
- P36 (verbatim recordacion espontanea): base n=17 (4.2% del total que recuerda publicidad espontaneamente). BASE CRITICA.
- P38 recall asistido "PRECIOS DE TU LADO": n=43 (10.7%).
- P41 recall asistido "DE TU LADO SIEMPRE": n=50 (12.4%).

**Claim que NO se puede publicar:**
> "X% de los consumidores recuerda el mensaje de Gama" [proyectable al universo]
> Cualquier distribucion de verbatims sobre n=17 como si fuera representativa

**Claim que SE PUEDE publicar:**
> "Entre quienes recuerdan publicidad espontanea de Gama (n=17, base baja — lectura cualitativa), los mensajes asociados son..." [con caveat prominente]

**Caveat literal OBLIGATORIO en cada slide de publicidad:**
> "BASE BAJA: n=[17/43/50] — resultados indicativos, no proyectables al universo de shoppers"

**Recomendacion Bruna:** AJUSTAR — asegurarse de que los slides de publicidad tengan caveat de base baja en titulo o subtitulo, no solo en nota al pie.

---

### L-006: Datos El Recreo (P43-P45) — base n=21

**Contexto:** n=21 shoppers que conocen o compran en El Recreo. Base insuficiente para cualquier inferencia al universo.

**Claim que NO se puede publicar:**
> Cualquier porcentaje de P43-P45 como representativo de la zona El Recreo

**Claim que SE PUEDE publicar:**
> "Entre los 21 respondentes que frecuentan El Recreo (INDICATIVO — no proyectable), X% expresaria..."

**Recomendacion Bruna:** AJUSTAR — este modulo debe tener flag de "indicativo, solo lectura de tendencia" como encabezado del slide, no solo al pie.

---

### L-007: Diferencias TOM por municipio — bases referenciales

**Contexto:** Altos Mirandinos (n=20), El Hatillo (n=31), El Recreo (n=21) tienen bases referenciales o en limite.

**Claim que se puede publicar:** diferencias entre municipios grandes (Chacao n=70, Baruta n=122, Sucre n=79).

**Claim que requiere caveat:** Altos Mirandinos, El Hatillo, El Recreo — REFERENCIAL. Los % no son proyectables a esas zonas.

**Recomendacion Bruna:** AJUSTAR — agregar footnote "*Base referencial n<35" en cada celda de municipios pequenos en tablas.

---

## Seccion 3 — Lo que NO se puede concluir de estos datos

| Conclusion prohibida | Por que no | Alternativa correcta |
|---|---|---|
| "Gama tiene X% de share de mercado en Caracas" | La muestra no es probabilistica del universo total de shoppers | "Entre los shoppers de cadenas de supermercado C+/C/D/E entrevistados, 8% prefiere Gama" |
| "El precio de Gama esta fuera del rango aceptable" | P33 no mide rangos PSM, solo percepcion ordinal | "54% percibe los precios de Gama como mas caros que la competencia" |
| "La atencion al cliente es la CAUSA de la preferencia por Gama" | Estudio observacional — correlacion, no causalidad | "La atencion al cliente es el atributo mas fuertemente asociado con la preferencia por Gama" |
| "Los segmentos A/B/C/D/E identificados son los segmentos del mercado" | Clustering jerarquico exploratorio, sin validacion formal | "Los datos sugieren 5 perfiles de shopper hipotetizados — pendiente validacion" |
| "Gama crece/cae en TOM vs 2025" | La comparacion 2025-2026 fue descontinuada por cambios metodologicos en el cuestionario | "Los datos 2025 y 2026 no son directamente comparables por diferencias metodologicas" |
| "El precio de Gama es X Bs o X USD" | No se midio precio en escala monetaria en ningun punto del cuestionario | "Se mide percepcion ordinal de precio, no precio absoluto" |
| "X% de los preferentes de Gama son leales exclusivos" | Solo se mide ultima compra (P24), no patron completo de gasto | "X% de los preferentes de Gama realizaron su ultima compra en Gama" |

---

## Seccion 4 — Bases bajas — tabla maestra para Bruna

| Subgrupo | n | Flag | Margen de error aproximado | Recomendacion de uso |
|---|---|---|---|---|
| Pref-Gama | 32 | REFERENCIAL | ±17.3pp | Solo lectura cualitativa / indicativa |
| Pref-Plan Suarez | 28 | REFERENCIAL | ±18.5pp | Solo lectura cualitativa / indicativa |
| El Recreo (P43-P45) | 21 | REFERENCIAL | ±21.4pp | Solo indicativo, con flag prominente |
| Altos Mirandinos (municipio) | 20 | REFERENCIAL | ±21.9pp | Solo indicativo |
| P35-P36 recall espontaneo | 17 | BASE CRITICA | ±23.7pp | Solo cualitativo — no % |
| La Vega (parroquia) | 12 | REFERENCIAL | ±28.3pp | No usar en inferencia |
| Candelaria | 7 | EXCLUIR | ±37pp+ | Agrupar en "Libertador Centro/Oeste" |
| San Bernardino | 6 | EXCLUIR | ±40pp+ | Agrupar |
| San Juan, Catedral, Santa Teresa, Santa Rosalia | 4 c/u | EXCLUIR | ±49pp+ | Agrupar |

---

## Seccion 5 — Claims nuevos de V3 que requieren gate adicional

Los siguientes son **findings nuevos** de CU-2, CU-3, CU-4, CU-5 que NO estaban en el deck V2 entregado a Cora. Bruna debe gaterarlos antes de que aparezcan en cualquier comunicacion:

| Finding nuevo | Status | Recomendacion |
|---|---|---|
| "Gama sobre-indexa en C+/C (13.5%) vs E (5.3%), diferencia significativa p=0.017" | NUEVO CU-2 | GO — incluir IC95 |
| "No hay diferencias significativas en el embudo de Gama por genero" | NUEVO CU-2 | GO |
| "La asociacion NSE-preferencia global no es significativa al 95% (p=0.083)" | NUEVO CU-2 | GO con matiz (es tendencia) |
| "54% percibe Gama como mas cara — transversal a todos los NSE" | NUEVO CU-5 | GO |
| "45% percibe subida de precios en 6 meses" | NUEVO CU-5 | GO |
| "Los segmentos hipotetizados sugieren 5 perfiles distintos" | NUEVO CU-4 | NO-GO como afirmacion — solo como hipotesis de trabajo |
| "Pseudo R2 logit reproducido identicamente al V2 (0.4371)" | NUEVO CU-1 | GO — certificacion interna |

---

## Seccion 6 — Pending items que requieren autorizacion Owner

| Item | Tipo | Por que pende |
|---|---|---|
| RF+SHAP analysis (CU-3) | pip install scikit-learn shap | Zona amarilla RISK-POLICY — requiere autorizacion Owner |
| K-means formal / LCA (CU-4) | pip install scikit-learn | Misma razon |
| Regenerar faseA_embudo_bbdd.json corregido | Script | Cambio en archivo del V2 — requiere autorizacion Owner |

---

*Producido por Cuanti V3 — 2026-05-17*
*Este memo es el gate obligatorio antes de cualquier comunicacion externa de cifras numericas.*
*Bruna tiene decision final sobre GO/NO-GO/AJUSTAR de cada claim.*
*El analisis cuantitativo es responsabilidad de Cuanti; la aprobacion de publicacion es responsabilidad de Bruna.*
