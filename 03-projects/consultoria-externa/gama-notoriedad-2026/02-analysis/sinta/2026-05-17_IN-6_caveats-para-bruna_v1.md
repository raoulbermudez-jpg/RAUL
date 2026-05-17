---
autor: Sinta (Qualitative Synthesis & Brand Strategy Lead)
proyecto: gama-notoriedad-2026
tipo: IN-6 Caveats Memo — Gate Bruna
version: v1
fecha: 2026-05-17
para: Bruna (gate de aprobacion previo a publicacion externa)
cc: Owner, Vivienne
status: PENDIENTE GATE BRUNA — no circular externamente
nota_uso: Este memo es auto-contenido. Bruna puede dar GO / NO-GO / AJUSTAR sin leer IN-1..IN-5. Los claims cuantitativos con caveat ya fueron procesados por Cuanti en CU-6 v2; este memo integra los claims cualitativos adicionales y las afirmaciones estratégicas que Sinta introduce.
---

# IN-6 — Caveats Memo (Gate Bruna)
## Notoriedad Gama 2026 — Claims cualitativos y estratégicos para aprobación

**Para:** Bruna
**De:** Sinta
**Fecha:** 2026-05-17
**Referencia paralela:** CU-6 v2 de Cuanti (claims cuantitativos — leer en paralelo)

---

## GATE BRUNA PENDIENTE

Lista de claims que requieren revisión y aprobación antes de cualquier uso externo (deck Vivienne, comunicaciones a Cora, presentación a Gama):

**Prioridad 1 (alta sensibilidad estratégica):** C-001, C-002, C-004
**Prioridad 2 (metodológicos — caveat de transparencia):** C-003, C-005, C-007
**Prioridad 3 (nuevos en V3 — no en V2):** C-006, C-008

---

## Sección 1 — Claims cualitativos de alta carga estratégica

### C-001 — "La campaña de Gama comunica precio cuando debería comunicar experiencia"

**Origen:** IN-2 Tema 4 + IN-4 T-07 + IN-5 Argumento 1
**Formulación exacta en uso:**
> "La comunicación actual ("PRECIOS DE TU LADO") no amplifica el driver #1 de preferencia (atención). El 65% que recuerda PTL la lee como mensaje de precio — exactamente el atributo menos predictivo de la preferencia por Gama (OR=1.03, p=0.966)."

**Caveats:**
1. La afirmación sobre la campaña implica un juicio sobre la estrategia de comunicación de Gama — es el claim de mayor sensibilidad con el cliente.
2. El dato de recall (0/17 espontáneo, n=43-50 asistido) tiene bases bajas. Las bases bajas reducen la certeza estadística pero no eliminan la dirección del hallazgo.
3. La interpretación de "debería comunicar experiencia" es un claim prescriptivo derivado de los datos del estudio — no un dato del estudio. Está fundamentado en la convergencia de drivers (OR + SHAP + verbatims) pero contiene un salto interpretativo que Bruna debe validar.
4. El deck de Vivienne debe presentar esto como recomendación estratégica apoyada en datos — no como crítica directa a la campaña actual. El tono importa.

**Recomendación Bruna:** AJUSTAR formulación para presentación a Cora. La afirmación es sólida en evidencia; la sensibilidad está en el tono. Propuesta de formulación alternativa: "El estudio indica que comunicar la experiencia de atención (el driver más fuerte) puede tener mayor impacto que comunicar precio (el atributo menos predictivo de la preferencia). Una revisión de la plataforma de comunicación está justificada por los datos."

**Status sugerido:** GO con ajuste de tono. Requiere aprobación Bruna antes de deck Vivienne.

---

### C-002 — "El seg_2 (Pragmáticos Convertibles) es la oportunidad más inmediata de crecimiento"

**Origen:** IN-5 Argumento 4. Nuevo en V3, sin precedente en V2.
**Formulación exacta:**
> "El k-means identifica un segmento de 133 shoppers (33% de la muestra) con menor resistencia al precio y menores expectativas — la combinación óptima para conversión con una campaña de primera prueba bien diseñada."

**Caveats:**
1. El silhouette del k-means es moderado (~0.195) — los segmentos se solapan en los márgenes. El seg_2 no es un grupo discreto; es una tendencia central. Hay individuos del seg_1 que se comportan como seg_2 y viceversa.
2. "33% de la muestra" no equivale a "33% del universo de shoppers de Caracas" — la muestra es shoppers de supermercado de cadena por cuotas, no probabilística.
3. "Menor resistencia al precio" (3.44 vs 3.66/5) es una diferencia de 0.22 puntos en escala 1-5. Estadísticamente no significativa entre seg_1 y seg_2 directamente — es la media de cluster resultante del k-means, no un z-test head-to-head.
4. La afirmación de que son "convertibles" es interpretativa — se basa en la lógica de que menos exigencia + menos resistencia a precio = menor barrera. Es una hipótesis de comportamiento, no un dato de intención de compra.

**Recomendación Bruna:** GO con caveat de silhouette moderado. El claim debe presentarse como "el análisis de segmentación sugiere" (no "el análisis prueba"). El tamaño de muestra n=133 es suficiente para una lectura descriptiva accionable.

**Status sugerido:** GO con caveat explícito de solapamiento en márgenes.

---

### C-003 — "La barrera de precio es el obstáculo que impide que el 92% llegue a experimentar la propuesta de valor de Gama"

**Origen:** IN-3 §3 (cuello de botella CBBE) + IN-4 §2.2
**Formulación exacta:**
> "La percepción de precio caro (54%) actúa como barrera de entrada. El logit no captura esta barrera porque mide el efecto sobre quienes ya están en el mercado Gama — pero el mecanismo de no-conversión requiere datos que este estudio no tiene."

**Caveats:**
1. La afirmación de que el precio es la barrera de entrada es una hipótesis de mecanismo derivada del análisis de convergencia — no es un dato directo del estudio. El estudio no pregunta "¿por qué no elige Gama?" a los no-preferentes de Gama.
2. Podrían existir otras barreras igualmente importantes (falta de sucursal cercana, hábito con otra marca, primera experiencia negativa) que este estudio no puede distinguir.
3. La certeza de este claim es media (confirmada por triangulación cuali+cuanti, pero sin datos de no-consumidores directos).

**Recomendación Bruna:** AJUSTAR formulación. En lugar de "la barrera es el precio", formular como "la percepción de precio caro es la hipótesis más parsimoniosa para explicar la baja conversión, dada la evidencia disponible — requiere validación con investigación de no-consumidores (FGIs o Van Westendorp)."

**Status sugerido:** GO con calificación explícita de hipótesis. No presentar como dato verificado.

---

## Sección 2 — Claims cualitativos sobre verbatims y codificación

### C-004 — "La atención opera como símbolo de reconocimiento personal, no solo como atributo funcional"

**Origen:** IN-2 Tema 1 (tesis latente) + IN-4 §3.2 (mecanismo cuali)
**Formulación exacta:**
> "Los preferentes de Gama no experimentan la atención como un atributo funcional de servicio — la experimentan como reconocimiento personal, la señal de que la tienda los ve como personas con nombre, no como números en la fila."

**Caveats:**
1. Esta es la afirmación de más alto contenido interpretativo del análisis. No hay verbatims literales que la soporten directamente en los datos disponibles — es una construcción inferida del patrón de frecuencias y de la dominancia de "atención" como razón espontánea.
2. La ausencia de acceso a verbatims literales en esta sesión (BBDD raw gitignored) limita la solidez de esta interpretación. Sería necesaria la extracción y lectura de los verbatims de P21.1 de pref-Gama para confirmar que el contenido semántico es efectivamente "reconocimiento personal" y no simplemente "el personal es amable".
3. Esta interpretación es valiosa estratégicamente (informa la dirección de comunicación) pero requiere triangulación con verbatims reales.

**Recomendación Bruna:** NO-GO hasta verificar verbatims literales de P21.1 de pref-Gama desde BBDD raw. Alternativamente, GO si se presenta como hipótesis interpretativa ("la evidencia sugiere que la atención puede estar operando como...") en lugar de afirmación verificada.

**Status sugerido:** AJUSTAR — requiere acceso a verbatims literales o presentarse como hipótesis marcada.

---

### C-005 — "El 12% que atribuye 'Sin ti no hay nosotros' a Gama indica que el espacio semántico de compañía está disponible"

**Origen:** IN-1 §4 + IN-2 Tema 4
**Formulación exacta:**
> "El 12% de los shoppers que recuerdan alguna frase publicitaria atribuyen a Gama el slogan 'Sin ti no hay nosotros' — que no es de Gama. Esto indica que el espacio semántico 'compañía / estar de tu lado' ya está proyectado sobre la marca por una parte del mercado, aunque Gama no lo ha construido explícitamente."

**Caveats:**
1. Base: n=17 (shoppers que recuerdan alguna frase en P35). 12% de n=17 = 2 personas. Dos observaciones no pueden soportar una afirmación estratégica.
2. El dato estadístico es una anécdota de base baja, no evidencia sólida. Su valor es directivo/inspirador (señala una dirección posible) — no concluyente.
3. Podría ser simplemente confusión de marcas sin significado estratégico.

**Recomendación Bruna:** NO-GO como afirmación estratégica directa. Se puede mencionar como "dato anecdótico sugerente" en el contexto de la recomendación de comunicación, con aclaración explícita de la base baja (n=2). No usar como evidencia primaria.

**Status sugerido:** NO-GO como claim. GO como anécdota de apoyo con caveat explícito de base (n=2).

---

## Sección 3 — Claims metodológicos heredados de V2 que Sinta valida

### C-006 — Convergencia triple como elevación de limpieza/orden a driver secundario

**Origen:** CU-3 v2 + IN-5 Argumento 1 (Sinta integra limpieza como parte del constructo "experiencia")
**Formulación:**
> "La limpieza y el orden del local es el segundo driver más importante de la preferencia por Gama, con soporte convergente de tres métodos: OR logit = 4.0 (p=0.061, borderline), SHAP #2 (0.0735), Gini RF #2 (0.1609)."

**Caveats:**
1. El p-value del logit es 0.061 — no significativo al 95%. El claim de "driver secundario confirmado" descansa principalmente en SHAP y Gini, no en el logit.
2. El IC95 del OR logit es muy amplio: 0.940 a 16.913 — no excluye OR=1 en el límite inferior (aunque apenas).
3. Cuanti elevó este claim de "tendencia" a "driver secundario confirmado" en CU-6 v2 sección D-002. Sinta lo integra en IN-5 de forma consistente con esa elevación.

**Acción Bruna (ya procesada en CU-6 v2):** GO con caveat de p-logit borderline. El claim fue aprobado por Cuanti en CU-6 v2. Sinta no genera caveat adicional — confirma que la integración cuali (limpieza como parte del constructo experiencia de servicio en EJE 1 axial) es coherente con la elevación de Cuanti.

**Status:** GO — delegado a decisión de CU-6 v2.

---

### C-007 — Ausencia de verbatims literales en esta sesión de Sinta

**Origen:** limitación de acceso en esta sesión (BBDD raw gitignored, NDA)
**Descripción:** Sinta produjo IN-1..IN-6 basándose en los outputs serializados del V2 (frecuencias codificadas, z-scores, outputs logit, JSONs) y en los sumarios de Methos y Cuanti. No tuvo acceso directo a los verbatims literales de BBDD raw en esta sesión.

**Impacto en claims:**
- Los verbatims citados en IN-1 y IN-2 son frecuencias de categorías ("53.1% cita atención") y verbatims inferidos de esas categorías — no verbatims literales con ID de participante.
- Los temas latentes de IN-2 son construcciones interpretativas sin ancla directa en texto verbatim literal.
- El esquema de codificación de IN-1 es una propuesta metodológica formal — no ha sido aplicado sobre verbatims reales en esta sesión.

**Implicación para gate Bruna:**
Cualquier claim que dependa de verbatims literales (ID de participante, cita exacta) debe ser verificado contra BBDD raw antes de publicación externa. Los claims basados en frecuencias de categorías (P21.1: "53.1% cita atención") son reproducibles directamente desde los outputs V2 verificados por CU-1.

**Acción requerida:** Owner debe evaluar si se requiere una segunda sesión de Sinta con acceso a BBDD raw para validar los temas latentes de IN-2 antes de producir el deck de Vivienne. Si el timeline lo permite, esa sesión elevaría la confianza de los claims C-004 y fortalecería IN-2.

**Status:** PENDIENTE DECISIÓN OWNER — no bloquea el gate Bruna en los claims de alta certeza.

---

### C-008 — Segmentación como aportación nueva del V3

**Origen:** CU-4 v2 + IN-5 Argumento 4
**Descripción:** Los 3 segmentos k-means son un hallazgo nuevo en V3 — no existían en el V2 entregado a Cora. Si el deck de Vivienne los incluye, Cora recibirá información que no estaba en el deck V2. Esto requiere una decisión de Owner sobre cómo manejar la comunicación con Cora: ¿se presenta el V3 como actualización del V2 o como deliverable separado?

**Caveat del dato:** silhouette moderado (~0.195) — los segmentos son válidos pero con solapamiento en márgenes. Caveat obligatorio en deck: "los perfiles representan tendencias centrales, no categorías discretas".

**Status:** GO con caveat. Decisión de packaging (cómo presentar a Cora) es del Owner — Sinta no puede decidirlo.

---

## Sección 4 — Claims heredados de CU-6 v2 que Sinta confirma como insumo de IN-5

Los siguientes claims cuantitativos ya fueron aprobados (o condicionados) por Cuanti en CU-6 v2. Sinta los integra en su pirámide Minto (IN-5) de forma consistente con la decisión de CU-6 v2. Bruna no necesita revisarlos de nuevo en este memo — se referencia a CU-6 v2 para cada uno.

| Claim cuanti | Status CU-6 v2 | Integración Sinta en IN-5 |
|---|---|---|
| Atención = driver principal (OR=5.73) | GO pleno con IC95 | Argumento 1 — el más fuerte de la pirámide |
| Limpieza = driver secundario (SHAP #2) | GO con caveat p-logit | Argumento 1 — parte del constructo experiencia |
| Promociones = driver terciario (OR=3.64) | GO con IC95 | Argumento 2 |
| El precio no es driver (SHAP #10) | GO | Argumento 2 (contrasta precio vs. promociones) |
| 3 segmentos k-means publicables | GO con caveat silhouette | Argumento 4 |
| Preferida C+/C 13.5% sig > E 5.3% | GO con IC95 | Contexto SCR de IN-5 |
| 54% neto caro | GO con IC95 | Argumento 3 (barrera de precio) |
| 45% percibe subida de precio | GO con caveat retrospectiva | Argumento 3 (urgencia de acción) |

---

## Sección 5 — Checklist ejecutivo de gate para Bruna

| # | Claim | Tipo | Recomendación Sinta | Status final Bruna |
|---|---|---|---|---|
| C-001 | Campaña comunica precio, debería comunicar experiencia | Estratégico-sensible | AJUSTAR tono | ________ |
| C-002 | Seg_2 como oportunidad inmediata de conversión | Nuevo V3 | GO con caveat silhouette | ________ |
| C-003 | Precio como barrera de entrada (hipótesis de mecanismo) | Interpretativo | AJUSTAR como hipótesis | ________ |
| C-004 | Atención como reconocimiento personal (latente) | Interpretativo sin verbatims literales | NO-GO hasta verbatims reales / GO como hipótesis | ________ |
| C-005 | "Sin ti no hay nosotros" como señal de espacio semántico | Anecdótico n=2 | NO-GO como claim / GO como anécdota con caveat | ________ |
| C-006 | Limpieza como driver secundario (ya en CU-6 v2) | Cuanti elevado por SHAP | GO — delegado a CU-6 v2 | ________ |
| C-007 | Ausencia de verbatims literales en sesión Sinta | Metodológico | PENDIENTE DECISIÓN OWNER | ________ |
| C-008 | Segmentación k-means como nuevo contenido para Cora | Packaging / comunicación | GO con caveat — decisión Owner | ________ |

---

## Sección 6 — Lo que NO se puede concluir de los análisis cualitativos de Sinta

| Conclusión prohibida | Alternativa correcta |
|---|---|
| "Los consumidores de Gama se sienten reconocidos como personas" | "El 53% de los preferentes de Gama cita atención al cliente como razón #1 de preferencia — el mecanismo profundo requiere investigación cuali dedicada" |
| "La campaña de Gama es un fracaso" | "El recall de las campañas actuales es bajo (4.2% espontáneo) y la lectura dominante es precio, no compañía ni experiencia" |
| "El 33% del mercado es convertible por Gama" | "K-means identifica un segmento de ~33% con menor resistencia al precio — son un segmento prioritario de conversión potencial, no garantía de conversión" |
| "Gama debe cambiar de campaña" | "El estudio justifica revisar la plataforma de comunicación para alinearla con los drivers reales de preferencia" |
| "Los verbatims confirman la experiencia de reconocimiento personal" | "Las frecuencias de razones espontáneas son consistentes con la hipótesis de reconocimiento personal — los verbatims literales requieren acceso a BBDD raw para confirmación" |

---

*IN-6 v1 producido por Sinta — 2026-05-17*
*Dependencia paralela: CU-6 v2 de Cuanti para claims cuantitativos.*
*Acción requerida Owner: (1) Activar a Bruna para gate de este memo + CU-6 v2. (2) Decidir si se requiere sesión adicional de Sinta con acceso a verbatims literales para validar C-004 antes de producción del deck de Vivienne.*
