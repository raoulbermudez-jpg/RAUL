---
autor: Sinta (Qualitative Synthesis & Brand Strategy Lead)
proyecto: gama-notoriedad-2026
tipo: IN-4 Cuanti+Cuali Convergence Analysis
version: v1
fecha: 2026-05-17
status: draft — gate Bruna pendiente
confidencialidad: interno equipo
---

# IN-4 — Cuanti+Cuali Convergence Analysis
## Notoriedad Gama 2026 — Triangulación sistemática cuali + cuanti

**Proyecto:** Gama Notoriedad 2026
**Fuentes cuanti:** CU-1 (reconciliación), CU-2 (stat pack), CU-3 v2 (drivers RF/SHAP), CU-4 v2 (segmentación k-means), CU-5 (precio)
**Fuentes cuali:** IN-1 (coding), IN-2 (temas), IN-3 (CBBE), Doc Técnico V2, razones espontáneas P21.1

---

## 1. Mapa de triangulación — tabla claim-by-claim

| # | Afirmación | Evidencia cuali | Evidencia cuanti | Relación | Nivel de certeza |
|---|---|---|---|---|---|
| T-01 | La atención al cliente es el driver primario de preferencia por Gama | Razón espontánea #1: 53% pref-Gama cita "buena atención". Tema 1 IN-2: carácter simbólico, no solo funcional. | Logit OR=5.73*** (p=0.007). SHAP #1 (0.1047). Gini RF #1 (0.1977). Triple convergencia. | **CONFIRMA — cuali y cuanti dicen lo mismo desde ángulos distintos** | Alta |
| T-02 | Limpieza/orden es el segundo driver de preferencia | Seg_3 (núcleo leal) valora limpieza 4.66/5. Tema 1 IN-2: limpieza como parte del constructo "experiencia de servicio". | SHAP #2 (0.0735). Gini RF #2 (0.1609). OR logit borderline (3.99, p=0.061). | **CONFIRMA — con matiz: cuali integra limpieza en el constructo experiencia, cuanti la separa como ítem** | Media-Alta |
| T-03 | Promociones es el tercer driver de preferencia | Razón de preferencia baja espontáneamente (no en top-3 verbatims de pref-Gama). Pero z-score de asociación Gama con "Promociones" es negativo (-0.67). | OR=3.64** (p=0.031). SHAP #3 (0.0633). | **MATIZA — cuali no confirma espontáneamente, cuanti sí mide efecto estadístico. Ver explicación §2.1** | Media |
| T-04 | El precio no es driver de preferencia para Gama | Razones de pref-Gama no incluyen precio de forma significativa. Tema 2 IN-2: el precio opera como zona de tensión, no como razón positiva de elección. | OR=1.03 (p=0.966). SHAP #10 (0.013). Confirmado en los 3 métodos. | **CONFIRMA — convergencia total. El cuali matiza el mecanismo: no es que el precio no importe, es que la decisión de preferencia se basa en otros atributos** | Alta |
| T-05 | Los preferentes de Gama aceptan el precio porque experimentan una compensación en servicio | Tema 2 IN-2 (la negociación interna de valor). Verbatim inferido: distribución P33 en pref-Gama prácticamente plana (34% caro, 34% igual, 31% económico). | Seg_3 percepción precio: 2.94/5 — el más favorable de los 3 segmentos. Pref-Gama neto caro = 34% vs. 54% total. | **CONFIRMA — cuali articula el mecanismo (negociación de valor), cuanti muestra el resultado (precio percibido más favorable en pref-Gama)** | Alta |
| T-06 | El mercado tiene 3 segmentos diferenciados por nivel de exigencia, no por NSE | Tema 5 IN-2: dos velocidades (leales vs no-convertidos). Análisis JTBD: jobs distintos para cada segmento. | K-means k=3 validado (silhouette 0.195). NSE no discrimina entre seg_1 y seg_2 (NSE promedio similar: 1.78 vs 1.85). El criterio discriminante es exigencia en P22. | **CONFIRMA — cuali nombra el mecanismo (nivel de exigencia + ecuación de valor ya resuelta o no), cuanti lo valida formalmente** | Media-Alta |
| T-07 | La campaña "PRECIOS DE TU LADO" no amplifica los drivers reales de Gama | Tema 4 IN-2: gap entre driver #1 (atención) y mensaje dominante (precio). Atribución de "Sin ti no hay nosotros" a Gama como evidencia de espacio semántico disponible. | 4.2% recall espontáneo total; 0/17 recuerdan PTL espontáneamente. 65% que recuerdan PTL la leen como mensaje de precio (no de compañía). P-value sobre bases bajas — ver caveat. | **CONFIRMA — cuali explica el por qué (la premisa estratégica de la campaña está desalineada con el driver real), cuanti muestra el resultado (recall bajo + lectura de precio)** | Media (base baja n=17-50 para datos publicitarios) |
| T-08 | Gama gana misión de urgencia, pierde misión de mercado grande | Tema 3 IN-2: cercanía como posicionamiento de conveniencia situacional. JTBD §4: Gama contratada para J3/J4 pero no para J1. | Misión urgencia: #2 (12.2%). Misión mercado grande: #7 (7.2%). | **CONFIRMA — total alineación cuali+cuanti** | Alta |
| T-09 | El 34% de preferentes-Gama que "se va" en mercado grande no se pierde por precio sino por surtido/misión | Tema 3 IN-2 (lealtad situacional). Los preferentes de Gama tienen percepción de precio más favorable — no se van por precio. | 34% de pref-Gama compraron en otra cadena en última compra. Destino: Páramo (4), CM (3), Forum (2). Páramo = mejor percepción de surtido para mercado grande. | **CUALI MATIZA CUANTI — el dato cuanti solo dice "se fueron". El cuali sugiere que el motivo es surtido/formato, no precio. Es hipótesis — requiere validación** | Media-Baja |
| T-10 | Gama sobre-indexa en C+/C: es la marca de su segmento natural | Inferencia CBBE Nivel 2: el DNA de experiencia tiene mayor valor percibido en C+/C que en D/E. | TOM C+/C 60.6% vs Total 44.3%. Preferida C+/C 13.5% vs Total 8.0%. z-test C+/C vs E sig (p=0.017). | **CONFIRMA** | Alta |

---

## 2. Interpretación de divergencias

### 2.1 — La paradoja de las Promociones (T-03)

**El cuanti dice:** las promociones tienen OR=3.64** (p=0.031) y SHAP #3 — son el tercer driver de preferencia estadístico.

**El cuali dice:** las razones espontáneas de los pref-Gama no incluyen promociones como razón explícita prioritaria. El z-score de asociación Gama-Promociones es negativo (-0.67) — Gama no es percibida como la marca de las promociones.

**Hipótesis explicativa de la divergencia:** El efecto de promociones en el logit no refleja que Gama sea reconocida POR sus promociones. Refleja que aquellos shoppers que sí han accedido a una promoción de Gama (una minoría que ya interactuó con Cashea, el club de lealtad o los stickers) tienen significativamente más probabilidad de preferirla. La promoción no convierte porque el shopper espera verla — convierte porque cuando la experimenta, activa la visita que le permite también experimentar la atención y la limpieza.

En otras palabras: la promoción puede ser el "anzuelo de primera prueba" que introduce al shopper al modelo experiencial de Gama. Pero no se percibe como fortaleza actual — es una palanca sub-activada con alto potencial de retorno.

**Implicación estratégica:** comunicar promociones no es comunicar "tenemos precios bajos" — es comunicar "tenemos una razón específica para que vengas esta semana". La diferencia es tácticamente crucial.

### 2.2 — La paradoja del precio percibido y la preferencia real (T-04 y T-05)

**El cuanti dice:** 54% percibe Gama como cara (P33). El precio no es driver (OR=1.03, SHAP #10).

**Esto parece una contradicción** — ¿cómo puede el precio ser la percepción más extendida Y el atributo menos predictivo de la preferencia?

**Hipótesis explicativa:** el precio opera como barrera de entrada, no como criterio de elección una vez dentro. Para el 92% no-preferente, el precio percibido impide la primera visita o la repetición — nunca llegan a experimentar lo que generaría preferencia. Para el 8% preferente, el precio ya fue aceptado (la negociación de valor de T-05 ya ocurrió) y deja de ser variable en la decisión.

El logit captura el efecto sobre quienes ya prefieren o no prefieren — no captura la barrera de entrada. Es un modelo correcto para su pregunta (¿qué predice preferencia entre quienes ya están en el mercado Gama?), pero no responde la pregunta de conversión (¿qué impide que el 92% llegue a preferir Gama?). Para esa pregunta, el precio sí importa.

**Implicación metodológica:** el estudio tiene dos preguntas superimpuestas: (a) ¿qué genera preferencia en quienes ya conocen a Gama? y (b) ¿qué impide que más personas la conozcan o la prueben? El logit responde bien la (a). La (b) requiere los datos que no hay: Van Westendorp, FGIs con no-clientes, datos de primera visita.

### 2.3 — El cuello de botella de conversión (T-09 — divergencia de certeza baja)

**El cuanti dice:** 34% de pref-Gama se fue a otra cadena en última compra. Destinos: Páramo, CM, Forum.

**El cuali sugiere (hipótesis):** no se fueron por precio (su percepción de precio Gama es más favorable que la del mercado total) sino por surtido/formato para la misión de mercado grande.

**Certeza baja** porque no hay verbatims sobre el motivo de la última compra en otra cadena (P25 no fue analizado con suficiente detalle en los outputs disponibles). Esta hipótesis deriva de la lógica cruzada entre T-04 (precio no es driver), T-08 (pierde misión mercado grande) y la percepción de precio de pref-Gama (más favorable).

---

## 3. El cuali sobre los drivers — ¿por qué "Atención" es el driver #1?

Esta es la pregunta central de IN-4 según el encargo. El cuanti responde QUÉ. El cuali responde POR QUÉ.

### 3.1 Lo que el cuanti dice sobre "Atención"

- OR logit = 5.73 (p=0.007): quien asocia Gama con mejor atención tiene 5.7 veces más odds de preferirla.
- SHAP #1 (0.1047): el atributo con mayor contribución marginal al modelo RF.
- Gini RF #1 (0.1977): el atributo más usado como criterio de decisión en los árboles del bosque.
- Asociación Gama-Atención: z-score +0.47 (medio) vs. campo — Gama sobreindea en este atributo pero no es el atributo con más alta z (ese es "Tienda atractiva" con +1.09).

Por qué el logit da el OR más alto a "Atención" cuando no tiene el z-score más alto: porque el logit mide el efecto CONDICIONAL sobre preferencia, no el nivel de asociación. Gama puede tener alta asociación con "Tienda atractiva" (z=+1.09) pero si ese atributo no diferencia a quienes prefieren vs. no prefieren Gama, no tiene OR alto. "Atención" tiene un OR alto porque dentro del subgrupo que asocia Gama con buena atención, la proporción de preferentes es dramáticamente mayor que en el subgrupo que no la asocia con atención.

### 3.2 Lo que el cuali agrega — el mecanismo

La atención no es un atributo en la misma categoría lógica que "limpieza" o "rapidez en caja". Esos son atributos que el shopper evalúa con criterios objetivos observables. La atención es un atributo relacional — depende de la interacción específica entre un empleado y un cliente.

**Mecanismo propuesto (tesis cuali):**

La atención al cliente de Gama opera como señal de reconocimiento personal. En un contexto de mercado donde los supermercados de mayor volumen (Páramo) operan con la lógica de eficiencia industrial (rotación alta de clientes, precio competitivo como propuesta principal), el shopper de Gama experimenta algo cualitativamente diferente: alguien le habló por su nombre, le ayudó a encontrar algo, o simplemente le resolvió un problema sin burocracia.

Ese momento de reconocimiento personal es el que cristaliza la preferencia. No es que el shopper haya hecho un análisis racional de atributos — es que experimentó algo que lo hizo sentir diferente a como se siente en otros supermercados.

**Por qué la atención tiene el OR más alto (interpretación cuali):**

Porque la atención es el atributo con mayor capacidad de sorpresa positiva. El shopper no espera buena atención en un supermercado — espera precio y surtido. Cuando la atención supera las expectativas (que son bajas para esta categoría), el efecto sobre la preferencia es desproporcionado. Esto es coherente con la teoría de la satisfacción de Kano: los atributos que producen el mayor impacto en lealtad son los que superan la expectativa, no los que la cumplen.

**Implicación comunicacional:**

No se puede comunicar la atención de Gama describiendo la atención de Gama. Se comunica mostrando el momento de reconocimiento — el empleado que recuerda que el cliente no puede comer gluten, la cajera que explica de cuál aceite hay descuento esta semana. La campaña debe mostrar el momento, no el atributo.

---

## 4. Gaps no resueltos

Preguntas que los datos disponibles no pueden responder y que constituyen la agenda de research futura:

1. **¿La barrera de precio es real o perceptual?** Los datos no tienen precios reales de referencia. Sin auditoría in-store, no podemos saber si Gama efectivamente es más cara o solo se percibe así. Si es perceptual, la solución es comunicación. Si es real, la solución requiere acción en surtido y negociación con proveedores.

2. **¿Por qué el seg_1 (Mayoría Exigente) no convierte si valora los atributos que Gama tiene?** El seg_1 valora atención 4.77/5 y limpieza 4.82/5 — casi tan alto como el seg_3. Pero cero preferencia Gama. La barrera no es falta de valoración del atributo — es algo anterior. ¿Es precio percibido? ¿Es falta de primera visita? ¿Es hábito con otra marca? Sin FGIs con el seg_1, no podemos saberlo.

3. **¿Qué hizo que los 32 pref-Gama cruzaran la barrera?** ¿Fue una primera visita por cercanía? ¿Una promoción? ¿Una recomendación de alguien? Este es el "conversion pathway" que Gama necesita replicar. Sin IDIs con el seg_3 no lo sabemos.

4. **¿El club de lealtad de Gama está acelerando o manteniendo la base de preferentes?** Activo existente con potencial alto — pero sin datos de desempeño del club cruzados con el tracker, no podemos evaluarlo.

5. **¿El formato Express limita la conversión en misión de mercado grande?** La hipótesis territorial del V2 (Baruta 6 sucursales, 2.4% preferencia) y la evidencia de misiones sugieren que el formato físico puede ser el cuello de botella en la conversión de misión grande. Requiere proyecto de formatos.

---

*IN-4 v1 producido por Sinta — 2026-05-17*
*La triangulación T-01, T-04, T-05, T-08 y T-10 tienen alta certeza y son los claims más robustos del V3. T-03 y T-09 requieren caveat explícito. Ver IN-6.*
