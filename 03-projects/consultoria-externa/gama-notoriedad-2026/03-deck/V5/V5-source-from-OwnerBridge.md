# Notoriedad y Preferencia de Marca — Gama 2026
## DECK PRINCIPAL V5 · Fresh Start desde Notoriedad 2.0

**Fecha:** 2026-05-18
**Equipo analítico:** Cora Urrea + Raoul Bermudez
**Versión:** V5 — análisis independiente y completo · Eje: datos 2026
**Confidencial / NDA**

> **Nota de entrega OwnerBridge:** Este documento es el V5 completo en formato .md, producido desde los datos disponibles en Drive (V4 + V4 RE + V3 + V2). Incluye: (1) Deck Principal V5, (2) Resumen Ejecutivo V5, (3) Diff V5 vs V4. El build en .pptx con gráficos visuales requiere ejecución desktop (scripts python-pptx). Los `[GRÁFICO PLACEHOLDER: ...]` marcan donde van los charts en el .pptx.

---

## MARCO V5: REGLAS DE LECTURA Y METODOLOGÍA

### Qué es V5 y en qué se diferencia de las versiones anteriores

V5 es un análisis independiente construido desde los datos de Notoriedad 2.0 sin dependencia estructural de V3 ni V4. No invalida el trabajo analítico acumulado — lo reorganiza con un eje diferente: los datos de 2026 son la base, los datos de 2025 son comparación, el cualitativo es insight e hipótesis.

**Lo que NO cambia:** los datos, las cifras, los caveats estadísticos, los verbatims. Son idénticos a V4.

**Lo que SÍ cambia:**
1. El eje del análisis es 2026 (no la confirmación de V3)
2. NSE C+/C es el Capítulo 1 (no un análisis exploratorio en WoW)
3. Los hallazgos cualitativos son hipótesis e insights (no conclusiones trianguladas co-iguales al cuanti)
4. Los datos 2025 son referencia comparativa al final (no capa analítica co-principal)

### Iconografía de certeza V5

| Ícono | Significado |
|---|---|
| ✅ | Conclusión: evidencia cuantitativa significativa (≥95%), base ≥30 |
| ⚠ | Hipótesis apoyada: tendencia estadística (p 0.05-0.10) o soporte cuali con patrón robusto |
| 💡 | Insight cuali: hallazgo de FG — útil para hypothesizing y diseño de activaciones, NO para extrapolación estadística |
| 📊 | Referencia evolutiva: dato 2025 como comparación (caveats de comparabilidad aplican) |

### Ficha técnica del estudio 2026

| Dimensión | Especificación |
|---|---|
| Universo | Shoppers regulares (≥1 compra/mes) en supermercados de cadena, Caracas + Altos Mirandinos |
| Muestra principal | n=402 entrevistas face-to-face (2026) |
| Margen de error Total | ±4.89% al 95% de confianza (Wilson) |
| NSE | C+/C combinado: n=104 (25.9%) · D: n=127 (31.6%) · E: n=171 (42.5%) |
| Geografía | Baruta (122) · Libertador (80) · Sucre (79) · Chacao (70) · El Hatillo (31) · A. Mirandinos (20) |
| Referencia comparativa 2025 | n=785 — comparable en preguntas comunes con caveats |
| Modelos estadísticos | Logit (AUC=0.929, Pseudo R²=0.4371) · RF/SHAP · K-means k=3 · Z-test BH-FDR |
| Subgrupo drivers | n pref-Gama=32 (referencial — IC95 amplio en OR) |
| Fecha campo | [Pendiente confirmación Cora] |

**Caveats metodológicos generales:**
- C+/C combinado (C+ y C no son separables en la BBDD). n=104 implica m.e. ±9.8% al 95%
- Los resultados 2025 se presentan sin ponderación muestral (factor no disponible). Posible sesgo de diseño
- Composición geográfica difiere entre olas (Libertador sobrerepresentado en 2025). Cambios en variables con dispersión geográfica pueden reflejar composición, no cambio real
- Análisis WoW por NSE no pre-registrados en diseño 2025 — exploratorios, confirmar en ola 2027

---

## BLOQUE 1 — NSE C+/C: el segmento natural de Gama

*Bloque central de V5. El segmento C+/C (n=104, 25.9%) define el campo de batalla principal.*

### 1A — Perfil del segmento C+/C 2026

| Dimensión | C+/C 2026 | Total 2026 |
|---|---|---|
| Tamaño en muestra | n=104 (25.9%) | n=402 |
| Geografía dominante | Baruta · Chacao · El Hatillo | Baruta · Libertador · Sucre |
| NSE por definición | C+ y C combinados | C+/C + D + E |
| Rol de decisión de compra | Alta (buyer principal del hogar) | 62.4% principal / 37.6% única |

⚠ Caveat: C+/C combinado (C+ y C no separables en BBDD). n=104 implica margen de error ±9.8% al 95% — análisis con mayor incertidumbre estadística que el Total.

### 1B — Gama en C+/C 2026: posición fuerte, sin crecimiento

| Métrica | C+/C 2026 | Total 2026 | Diferencial |
|---|---|---|---|
| TOM (Top of Mind) | **60.6%** | 44.3% | +16.3pp vs Total |
| Preferida | **13.5%** | 8.0% | +5.5pp vs Total |
| Compra 3m | (ver BBDD para dato granular) | 17.7% | — |

✅ **Conclusión:** Gama tiene sobrerepresentación significativa en C+/C vs Total. El segmento C+/C es donde Gama tiene su posición más fuerte y es el segmento alineado con su DNA de marca (experiencia premium, atención, calidad).

[GRÁFICO PLACEHOLDER: Embudo de Gama C+/C vs Total — barras comparativas por etapa del embudo. Cada par de barras: C+/C (color primario) vs Total (color secundario)]

### 1C — La amenaza: Rio y Paramo crecen explosivamente en C+/C

📊 **Referencia evolutiva 2025→2026 (NSE C+/C — exploratorio):**

| Cadena | TOM C+/C 2025 | TOM C+/C 2026 | Delta | Significancia |
|---|---|---|---|---|
| **Rio** | ~30.9% | **56.7%** | **+25.8pp** | sig_99 (p_adj=0.0002) |
| **Paramo** | ~18.0% | **40.4%** | **+22.3pp** | sig_99 (p_adj=0.0002) |
| Gama | ~58.4% | 60.6% | +2.2pp | no significativo |

⚠ **Caveat obligatorio (CV-WOW-005):** Los análisis por NSE en WoW no fueron pre-registrados en el diseño 2025. Deben interpretarse como hipótesis a confirmar en ola 2027. La composición geográfica 2025 puede sesgar los deltas. Causalidad no inferible.

💡 **Lectura estratégica:** Si las tendencias son reales, el segmento natural de Gama está siendo penetrado agresivamente por sus dos competidores principales. La posición actual de Gama en C+/C es sólida (TOM 60.6%); la velocidad de Rio y Paramo en ese segmento es la señal de alerta más importante del estudio — pendiente confirmación ola 2027.

[GRÁFICO PLACEHOLDER: Barras agrupadas TOM en C+/C — Rio/Paramo/Gama, comparativo 2025 vs 2026. Flecha roja en Rio y Paramo]

### 1D — El Nucleo Leal de Gama vive en C+/C

El Segmento 3 (Nucleo Leal, 8% de la muestra total) está sobrerrepresentado en C+/C. Los frecuentes de 18-30 y 50+ con uso 24h son el perfil dominante. El activo del 24 horas es especialmente diferenciador en C+/C — Rio y Paramo no tienen un equivalente funcional.

💡 **Insight cuali:** El 24h genera fidelidad transversal en C+/C. El corpus FG incluye referencias directas: "El de 24 horas es un tiro al piso, de verdad que sí." (Frecuentes 18-30) + "Eso es impelable." (Ocasionales 50+). [Hipótesis cuali — no proyectable estadísticamente]

---

## BLOQUE 2 — Salud de marca Gama 2026: Total

### 2A — El embudo 2026: posición sólida, conversión a preferencia baja

| Etapa del embudo | Gama 2026 | Gama 2025 (ref) | Delta WoW |
|---|---|---|---|
| TOM (Top of Mind) | **44.3%** | 42.0% | +2.2pp — no sig |
| Asistida | **60.2%** | ~58.0% | +2.2pp — no sig |
| Consideración | **31.8%** | 27.5% | +4.3pp — no sig |
| Compra últimos 3m | **17.7%** | 17.8% | -0.2pp — no sig |
| Preferida | **8.0%** | 9.7% | -1.7pp — no sig |
| Habitual | **20.2%** | 19.4% | +0.8pp — no sig |
| Última compra | — | — | -1.2pp — no sig |
| Misión 3m | — | — | +4.9pp — no sig |

✅ **Conclusión:** El embudo de Gama es estadísticamente estable en 2026 (0/8 indicadores con variación significativa). En un mercado donde Rio y Paramo crecen explosivamente, la estabilidad de Gama es fortaleza defensiva — sus activos diferenciadores (24h, atención relacional) generan una base estable.

⚠ Nota: La conversión TOM→Preferida es baja (44.3% → 8.0%). El Bloque 3 explica los mecanismos que determinan esta conversión.

[GRÁFICO PLACEHOLDER: Funnel / waterfall — embudo Gama 2026. Etapas en eje X, % en eje Y. Línea de referencia 2025]

### 2B — Posición competitiva 2026

| Cadena | TOM 2026 | Preferida 2026 | Movimiento WoW |
|---|---|---|---|
| **Rio** | **45.0%** | 10.2% | +17.0pp TOM sig_99 |
| **Gama** | **44.3%** | **8.0%** | 0pp (estable) |
| Paramo | ~39.1% | — | +12.1pp TOM sig_99 |
| C. Madeirense | — | 11.2% | -7.7pp compra sig_95 |
| Plan Suárez | — | — | — |

📊 **Referencia evolutiva:** Rio superó a Gama en TOM entre 2025 y 2026 (45.0% vs 44.3%). Paramo creció más en consideración (+17.3pp). CM pierde compra. Gama permanece estable — fortaleza relativa en mercado muy dinámico.

[GRÁFICO PLACEHOLDER: Mapa de posicionamiento — TOM vs Preferida. Burbujas por cadena, tamaño = cambio WoW. Rio y Paramo con flecha ascendente]

### 2C — Posicionamiento y atributos Gama 2026

Gama lidera en el espacio "experiencial premium" (Calidad, Atractiva, Limpieza, Seguro). Su DNA de marca es claro en su segmento natural (C+/C). Los atributos de precio se debilitan en tendencia.

| Atributo | Posición Gama | WoW 2025→2026 | Certeza |
|---|---|---|---|
| Atención al cliente | Líder (driver #1 OR=5.73) | — | ✅ Alta |
| Limpieza | Líder (driver #2 OR=3.99*) | — | ✅ Alta |
| Tienda atractiva | Alta | +6.3pp (tendencia p_adj=0.058) | ⚠ Solo tendencia |
| Seguro | Alta | +5.8pp (tendencia p_adj=0.089) | ⚠ Solo tendencia |
| Menor precio | Baja | -3.9pp (tendencia p_adj=0.091) | ⚠ Solo tendencia |
| Promociones | Media-baja | -5.1pp (tendencia p_adj=0.053) | ⚠ Solo tendencia |

⚠ **ADVERTENCIA:** Ninguno de los movimientos de atributos 2025→2026 pasa la corrección BH-FDR (umbral q<0.05). Son informativos — señales direccionales a monitorear en ola 2027. No son conclusiones del estudio.

---

## BLOQUE 3 — Drivers de preferencia Gama 2026

### 3A — El modelo logístico: qué predice que alguien prefiera Gama

**Pregunta:** ¿Cuáles asociaciones con una cadena predicen que el shopper la prefiera?
**Modelo:** Regresión logística (statsmodels). Variable dependiente: Preferida=Gama (1/0).

| Driver | OR logit | IC95 | Sig | SHAP rank | Convergencia |
|---|---|---|---|---|---|
| **Atención al cliente** | **5.73** | [1.6, 20.4] | *** p<0.01 | #1 | Logit + RF + SHAP + razón espontánea |
| Limpieza | 3.99 | [0.94, 16.91] | * p<0.10 | #2 | Logit borderline + SHAP + Gini |
| **Promociones** | **3.64** | [1.1, 11.8] | ** p<0.05 | #3 | Logit + SHAP + razón espontánea |
| **Precio (menor precio)** | **1.03** | — | NS p=0.966 | **#10** | 4 métodos: no driver |

**Métricas del modelo:** Pseudo R²=0.4371 · AUC=0.929 · n pref-Gama=32 (referencial)

✅ **Conclusión 1:** Quien asocia Gama con atención tiene 5.7x más odds de preferirla. La convergencia de 4 métodos independientes es el mayor respaldo de robustez disponible en este estudio.

✅ **Conclusión 2:** El precio NO es predictor de preferencia (OR=1.03, NS, SHAP #10). Comunicar precio en Gama es invertir en el atributo menos relevante para la conversión.

✅ **Conclusión 3:** Las promociones son palanca táctica (OR=3.64**) — su función es atraer a la primera visita, no comunicar precio bajo.

⚠ Caveat: n pref-Gama=32 implica IC95 amplios. OR=5.73 es el estimado central con IC95 [1.6, 20.4]. El patrón es robusto por convergencia de métodos.

[GRÁFICO PLACEHOLDER: Barras horizontales OR con IC95 — drivers ordenados por magnitud. Color verde para sig, gris para NS. Línea de corte OR=1]

### 3B — K-means: los tres tipos de shoppers de Gama

| Segmento | Tamaño | Perfil cuantitativo | Oportunidad |
|---|---|---|---|
| Seg 1 — Mayoría Exigente | **59%** (n≈237) | Alta exigencia, no exclusivos Gama, misión múltiple | Defensa + comunicación de experiencia |
| Seg 2 — Pragmáticos Convertibles | **33%** (n≈133) | Resistencia precio 3.44/5 (vs 3.66 Seg1), **0% pref-Gama actual** | Mayor retorno C/P — target de conversión prioritario |
| Seg 3 — Núcleo Leal | **8%** (n≈32) | Alta frecuencia, uso 24h, lealtad alta, vínculo afectivo | Retención + advocacy |

✅ **Conclusión:** El Segmento 2 (Pragmáticos Convertibles, 33%) tiene la menor resistencia al precio (3.44 vs 3.66/5) y 0% preferencia actual — mayor potencial de conversión a corto plazo de los tres clusters.

💡 **Insight cuali Seg 2:** El corpus FG sugiere que la resistencia no es solo un cálculo económico sino una autoexclusión identitaria ("Gama es para otro tipo de persona"). La activación más efectiva sería una primera experiencia guiada, no descuentos. [Hipótesis cuali — ver Bloque 6B]

⚠ Caveat: silhouette score ~0.20 (moderado). Los segmentos son tendencias interpretativas, no categorías discretas. Los perfiles se solapan en los márgenes.

[GRÁFICO PLACEHOLDER: Scatter plot k-means con centroides — 2 componentes principales PCA. Seg1 azul, Seg2 naranja, Seg3 verde]

---

## BLOQUE 4 — Comportamiento y misiones de compra 2026

### 4A — Misiones: Gama líder en urgencia, ausente en mercado grande

| Misión de compra | Gama 2026 | Posición competitiva |
|---|---|---|
| Compra urgente / cercana | 12.2% | **#2 del mercado** |
| Mercado grande / abastecimiento | 7.2% | **#7 del mercado** |

✅ **Conclusión:** Hay una brecha estructural entre la misión donde Gama gana (urgencia) y la misión donde el gasto por viaje es mayor (mercado grande). El 34% de los propios preferentes de Gama va a Páramo, CM o Forum para el mercado grande — pérdida de share of wallet en el propio Núcleo Leal.

📊 **Referencia evolutiva:** El espacio de CM en mercado grande se liberó parcialmente en 2026 (-7.7pp compra, sig_95) — una oportunidad no capturada aún por Gama.

[GRÁFICO PLACEHOLDER: Mapa de misiones × cadena — posicionamiento competitivo. Eje X: urgencia, Eje Y: mercado grande. Cada burbuja es una cadena]

### 4B — Coincidencia preferido↔última compra

La coincidencia entre "cadena preferida declarada" y "última cadena donde efectivamente compró" mide la brecha entre intención y conducta. En Gama, la tasa de coincidencia es alta en el Núcleo Leal (Seg 3) pero el volumen de transacciones de "mercado grande" se pierde en la misión de abastecimiento.

---

## BLOQUE 5 — Diagnóstico comunicacional 2026

### 5A — Gap de recall: la campaña no registra

| Métrica | Resultado 2026 | Certeza |
|---|---|---|
| Recall espontáneo "PRECIOS DE TU LADO" | **0/17 = 0%** | ✅ Alta (base n=17, m.e. amplio pero resultado categórico) |
| Recall asistido (con estímulo) | ~11% | ⚠ Base pequeña (n≈17-50) |
| Interpretación de PTL como "mensaje de precio" | 65% | ⚠ Base referencial |
| Interpretación de PTL como "solidaridad/apoyo" | 35% | ⚠ Base referencial |
| Ningún frase de Gama en recuerdo espontáneo | 95.8% | ✅ Base n=402 |

✅ **Conclusión:** Existe un gap comunicacional medible y material:
- La campaña "PRECIOS DE TU LADO" no registra recall espontáneo en ningún respondiente
- Cuando se presenta asistida, se interpreta mayoritariamente como mensaje de precio
- Precio es el predictor #10 de preferencia (OR=1.03 NS)

El resultado: Gama invierte recursos comunicacionales en el territorio menos predictivo de la preferencia.

⚠ Nota: bases del módulo publicitario son pequeñas (n=17-50). El hallazgo de recall 0% es robusto; los % de interpretación son referenciales.

[GRÁFICO PLACEHOLDER: Embudo de comunicación — espontáneo vs asistido vs interpretación. Pie chart para split precio/solidaridad]

---

## BLOQUE 6 — Insights cualitativos: hipótesis y señales (NO conclusiones del estudio)

> **REGLA DE LECTURA OBLIGATORIA DE ESTE BLOQUE:** Todo hallazgo aquí es insight cualitativo o hipótesis. El corpus base es 12 documentos FG (8 sesiones presenciales + 4 online), 6 segmentos, ~42,094 caracteres. Máximo ~42 personas presenciales. El cualitativo establece mecanismos, barreras y territorios de marca — NO prevalencia estadística. Una conclusión del cuanti con n=402 tiene mayor peso para decisiones estratégicas que un verbatim de 1-2 personas. El peso de los insights cuali es proporcional al número de grupos/participantes que los expresan.

### 6A — El mecanismo del driver de atención: hipótesis del "acompañamiento-guía"

**Lo que el cuanti establece (✅ alta certeza):**
OR=5.73*** — quien asocia Gama con atención tiene 5.7x más odds de preferirla. Convergencia de 4 métodos. Resultado cuantitativo robusto.

**La hipótesis cuali (💡 6/7 grupos FG — patrón robusto para hipótesis):**
El corpus FG documenta espontáneamente en 6 de 7 grupos la imagen de Gama como "guía experta de confianza" que acompaña la compra. El mecanismo no sería el reconocimiento nominal ("te conocen por tu nombre") sino el acompañamiento activo ("siempre hay alguien que te orienta").

> "Una mujer joven, pero con experiencia. Que sea como una guía, que te diga: 'Mira, hoy llegó el pan árabe fresco, llévatelo'."
> — Mary Francis Bossia, Ocasionales 18-30

> "Alguien de Caracas que te oriente y sea como una guía de compras, que no se quede atrás con la tecnología."
> — Moisés Torrealba, Ocasionales 18-30

💡 **Insight:** Si la hipótesis es correcta, el mensaje correcto es "en Gama siempre hay alguien que te ayuda" (creíble para el shopper), no "en Gama te conocen por tu nombre" (hipérbole difícil de verificar).

**Certeza:** Hipótesis cuali robusta (6/7 FG, emergente no inducido). Requiere claim testing cuantitativo para confirmar como plataforma comunicacional.

### 6B — La barrera del sifrinaje: hipótesis de autoexclusión identitaria

**Lo que el cuanti establece (✅ alta certeza):**
- Precio OR=1.03 (NS, SHAP #10): el precio no predice preferencia
- 54% percibe Gama como cara
- Paradoja documentada: la percepción de precio no afecta la preferencia → algo más explica la barrera de conversión

**La hipótesis cuali (💡 patrón en múltiples grupos):**
El corpus FG sugiere que la barrera no es un cálculo económico comparativo sino una autoexclusión simbólica — "Gama es para otro tipo de persona." El shopper se autoexcluye antes de entrar a verificar precios.

> "A mi me parece que es un poco costoso... el sifrinaje y tal, pero para hacer un mercado grande... es mejor ir al Lux o al Páramo."
> — Azahara Betancourt, Ocasionales 18-30

*"Sifrinaje" es vocabulario espontáneo del informante — no es una caracterización de Gama por el equipo analítico. Refleja cómo segmentos de no-usuarios codifican la barrera de entrada percibida.*

💡 **Insight:** Si la barrera es identitaria, los descuentos de precio no la mueven (comunicar precio bajo refuerza la distancia simbólica). La activación correcta del Seg 2 sería una primera experiencia que resignifique la pertenencia — no una oferta económica.

**Certeza:** Hipótesis cuali. 1 verbatim central + patrón consistente en varios grupos. Requiere validación cuantitativa (cuestionario de barreras estructurado).

### 6C — Gama Club: activo invisible con interés transversal

**El cuanti:** No hay pregunta directa sobre Gama Club en el cuestionario 2026.

**La hipótesis cuali (💡 6/7 grupos FG):**
El Gama Club genera interés genuino y transversal en todos los segmentos, pero su saldo es completamente invisible en el canal digital. El usuario no puede ver cuánto tiene acumulado, qué puede canjear, ni cuándo.

> "Las millas... yo ni sabía que eso se podía usar para pagar hasta hace poco. Yo pensaba que era como los puntos del banco que uno nunca usa."
> — Gregory, Frecuentes 18-30

💡 **Insight:** La única barrera documentada es operacional — no es un problema de propuesta de valor sino de visibilidad digital. La solución: saldo visible en app + equivalente en dinero + canje en caja. Baja inversión, alta accionabilidad. **Sin soporte cuantitativo directo en esta ola.**

**Certeza:** Hipótesis cuali (6/7 FG, patrón robusto). Requiere medición cuantitativa en ola 2027 para dimensionar el impacto.

### 6D — Canal digital: dos barreras distintas, dos soluciones distintas

**La hipótesis cuali (💡 corpus digital Bs FG):**

*Barrera 1 — Inconsistencia de inventario:* Patrón en 3/4 documentos de uso digital (Corpus B).
> "Yo dejé de usar la página porque a veces pides algo que dice que hay y a la media hora te llaman para decirte que no tienen."
> — Mujer, 42 años, segmento Frecuentes 31-50 (sesión online)

Solución indicada: sincronización de inventario en tiempo real (inversión tecnológica).

*Barrera 2 — Desconfianza en frescos:* Patrón en 5/7 segmentos FG. El shopper no confía en que los perecederos online tengan la misma calidad que en tienda. Solución: empezar la propuesta digital por no-perecederos.

💡 **Insight:** Ambas barreras son operacionales y resolubles sin reposicionamiento de marca. **Nota de alcance: estos hallazgos van más allá del brief original de notoriedad/brand health. Se incluyen por alta accionabilidad — ver decisión CO-3 del Owner.**

**Certeza:** Hipótesis cuali. Sin soporte cuantitativo en esta ola.

### 6E — El arquetipo no apropiado: hipótesis de territorio disponible

**La hipótesis cuali emergente (💡 6/7 grupos FG, no inducido por el moderador):**
Sin ninguna pregunta directa sobre personificación, 6 de 7 grupos convergieron espontáneamente en el mismo imaginario: Gama como mujer de 35-45 años, caraqueña, profesional, activa, guía experta de confianza.

> "Yo me la imagino como una mujer, como de unos 35 años, super activa, líder, entusiasta, que sabe lo que hace."
> — Moisés Torrealba, Ocasionales 18-30

💡 **Insight:** Este arquetipo no está apropiado por ningún competidor directo (Rio, Paramo, CM). Si se confirma cuantitativamente podría ser un territorio diferenciador de comunicación. La coherencia es notable: el arquetipo "guía experta" es la personificación exacta de lo que el OR=5.73 mide.

**Certeza:** Hipótesis cuali emergente (6/7 grupos). Requiere obligatoriamente: (1) prueba de concepto cuantitativa con el target, y (2) verificación de Gama sobre restricciones de contratos de imagen vigentes y plataforma de marca global antes de cualquier desarrollo creativo.

---

## BLOQUE 7 — Evolución comparativa 2025→2026 (referencia, no base del análisis)

*Este bloque usa los datos 2025 exclusivamente como referencia para entender qué cambió. Los datos 2026 son el análisis primario.*

### 7A — Gama: posición defensiva sólida (0/8 métricas con variación significativa)

| Indicador | Delta WoW | Significancia (BH-FDR) |
|---|---|---|
| TOM | +2.2pp | p_adj>0.10 — no significativo |
| Asistida | +2.2pp | p_adj>0.10 — no significativo |
| Consideración | +4.3pp | p_adj>0.10 — no significativo |
| Compra 3m | -0.2pp | p_adj>0.10 — no significativo |
| Preferida | -1.7pp | p_adj>0.10 — no significativo |
| Última compra | -1.2pp | p_adj>0.10 — no significativo |
| Habitual | +0.8pp | p_adj>0.10 — no significativo |
| Misiones | +4.9pp | p_adj>0.10 — no significativo |

✅ **Lectura correcta:** Gama es la única gran cadena del mercado que mantiene posición estadísticamente estable entre 2025 y 2026. En un mercado donde 9 de 10 cambios significativos son aumentos de competidores, la estabilidad es una fortaleza relativa — no un estancamiento.

⚠ Caveats: Factor de ponderación muestral 2025 no disponible. Composición geográfica difiere entre olas. n_2025=785, n_2026=402, corrección BH-FDR.

### 7B — Movimiento competitivo 2025→2026 (Total)

| Cadena | Métrica | Delta | Significancia |
|---|---|---|---|
| Rio | TOM | **+17.0pp** | sig_99 (p_adj<0.0001) |
| Rio | Consideración | +19.6pp | sig_99 (p_adj<0.0001) |
| Rio | Compra 3m | +12.5pp | sig_99 (p_adj<0.0001) |
| Rio | Preferida | +4.0pp | tendencia (p_adj=0.059) |
| Paramo | TOM | **+12.1pp** | sig_99 (p_adj=0.0003) |
| Paramo | Asistida | +10.8pp | sig_99 (p_adj=0.003) |
| Paramo | Consideración | +17.3pp | sig_99 (p_adj<0.0001) |
| CM | Compra 3m | **-7.7pp** | sig_95 (p_adj=0.033) |
| CM | Preferida | -5.5pp | tendencia (p_adj=0.053) |
| Gama | (todos) | ~0pp | no significativo (0/8) |

📊 **Lectura del movimiento:** El mercado venezolano de supermercados de cadena tuvo movimiento significativo en 2026. Rio es el ganador absoluto (TOM +17pp, consideración +20pp, compra +13pp, todo sig_99). Paramo consolida posición en toda la cadena del embudo. CM es el único perdedor significativo. Gama no se mueve en ninguna dirección.

[GRÁFICO PLACEHOLDER: Mapa 2x2 competidores — eje X=cambio consideración WoW, eje Y=cambio compra WoW. Rio y Paramo en cuadrante superior-derecho. CM inferior-izquierdo. Gama en centro]

---

## BLOQUE 8 — TESIS V5: EL DIAGNÓSTICO CENTRAL DESDE LOS DATOS 2026

**Tesis V5:** Gama posee el activo relacional más diferenciador del mercado (atención como driver #1, OR=5.73*** con convergencia de 4 métodos), su posición es estadísticamente estable y el 24h es una ventaja funcional sin equivalente en los competidores. Pero el crecimiento de Gama es cero mientras Rio y Paramo penetran el segmento C+/C — el segmento donde Gama tiene su mayor fortaleza. La estrategia correcta requiere tres movimientos simultáneos: (1) comunicar el activo que mueve la preferencia, no el precio que no la mueve; (2) activar el 33% convertible con el mecanismo correcto (primera experiencia, no descuento); (3) responder al avance en C+/C antes de ola 2027.

### Los 4 argumentos MECE desde los datos 2026

**Arg. 1 — El activo es real, robusto y sin equivalente competitivo** ✅ Alta certeza
OR=5.73 convergente en 4 métodos independientes. 53% de preferentes citan atención como razón espontánea #1. Rio y Paramo no tienen equivalente documentado. Limpieza es driver secundario (OR=3.99*). El activo existe y es defensivo.

**Arg. 2 — El activo no está siendo comunicado** ✅ Alta certeza en el gap, certeza media en la causalidad
Recall espontáneo PTL = 0/17 = 0%. 65% interpreta PTL como mensaje de precio (atributo OR=1.03 NS). El recurso comunicacional está invertido en el territorio equivocado.

**Arg. 3 — El segmento de conversión existe, es grande y tiene mecanismo de barrera conocido (hipótesis)** ✅ + 💡
Seg 2 (33% del mercado): 0% preferencia actual, menor resistencia al precio (3.44 vs 3.66/5 cuanti). Hipótesis cuali: la barrera es identitaria, la activación correcta es primera experiencia guiada. El mercado disponible de CM (-7.7pp compra, sig_95) complementa esta oportunidad.

**Arg. 4 — La presión competitiva en C+/C se intensifica (hipótesis WoW pendiente confirmación 2027)** ⚠ Hipótesis apoyada
Rio +25.8pp TOM en C+/C (exploratorio sig_99). Paramo +22.3pp TOM en C+/C (exploratorio sig_99). Gama +2.2pp (estable). La posición actual es sólida; la velocidad de los competidores en el segmento natural de Gama es la señal de alerta más importante del estudio.

---

## BLOQUE 9 — RECOMENDACIONES PRIORIZADAS V5

*Las recomendaciones son evaluación analítica — no un dato empírico. La prioridad asume continuidad de condiciones de mercado y está ordenada por combinación de certeza de evidencia + accionabilidad estimada.*

### Rec. 1 — Quick win: Activar digitalmente el Gama Club

**Qué:** Saldo visible en app + equivalente en dinero + opción de canje en caja.
**Por qué:** Interés genuino y transversal documentado en todos los segmentos (hipótesis cuali, 6/7 FG). La única barrera documentada es operacional — opacidad digital del saldo.
**Accionabilidad:** Alta — cambio de producto digital, sin nueva investigación, sin inversión de capital mayor.
**Potencial adicional:** El espacio disponible de CM (-7.7pp compra, sig_95) puede capturarse con un mecanismo de lealtad visible. El Gama Club bien ejecutado es ese mecanismo.
**Evidencia:** 💡 Insight cuali (6/7 FG). Validar con cuanti en ola 2027.

### Rec. 2 — Quick win: Reorientar el anzuelo promocional

**Qué:** Mantener stickers/Cashea/Club como palanca táctica (OR=3.64** confirmado), pero cambiar el mensaje de "precio bajo" a "razón específica para venir esta semana."
**Por qué:** Las promociones son el Driver #3 (OR=3.64** — cuanti confirmado). Pero el mensaje "precio bajo" refuerza la distancia simbólica del Seg 2 (hipótesis cuali del sifrinaje). El mismo activo, con el mensaje correcto, no activa la barrera identitaria.
**Mensaje correcto:** "Esta semana hay una razón para venir a Gama" (acceso a experiencia/producto específico) vs "Precios de tu lado" (mensaje de precio bajo que OR=1.03 NS confirma irrelevante para preferencia).
**Evidencia:** ✅ Cuanti OR=3.64** + 💡 Hipótesis cuali mecanismo

### Rec. 3 — Mid-term: Diseño de activación para Seg 2 (33% del mercado)

**Secuencia de activación:**
1. Anzuelo: razón específica para la primera visita (no precio bajo)
2. Primera experiencia guiada que active el activo de atención (OR=5.73)
3. Retención: Gama Club visible + saldo acumulado comunicado

**Por qué:** El Seg 2 tiene 0% preferencia actual + menor resistencia al precio en cuanti (3.44 vs 3.66/5). La hipótesis cuali indica que la barrera es identitaria — se neutraliza con la primera experiencia de acompañamiento, no con descuentos. El motor de conversión es resignificar la pertenencia.
**Evidencia:** ✅ Cuanti k-means Seg 2 + 💡 Hipótesis cuali mecanismo identitario

### Rec. 4 — Mid-term: Canal digital (requiere decisión CO-3 del Owner)

⚠ Nota de alcance: estas recomendaciones van más allá del brief original de notoriedad/brand health. Se incluyen por alta accionabilidad pero sugieren conversación de scope adicional con Gama.

- **Barrera 1 (inventario):** Sincronización de inventario en tiempo real — inversión tecnológica media
- **Barrera 2 (frescos):** Diseñar propuesta de delivery inicial solo con no-perecederos — bajo riesgo operacional

### Rec. 5 — Long-term: Estrategia ofensiva en C+/C antes de ola 2027

**Diseñar y ejecutar respuesta al avance de Rio y Paramo en C+/C** mientras la posición de Gama (TOM 60.6%) aún es ventajosa. La posición actual es sólida; la ventana de respuesta ofensiva se cierra si Rio/Paramo completan la penetración del segmento.

### Rec. 6 — Long-term: Explorar plataforma "acompañamiento-guía" (sujeto a CO-3 + DW-2)

Si la hipótesis cuali del arquetipo se confirma con concept testing cuantitativo, explorar el arquetipo femenino espontáneo (35-45 años, guía experta) como plataforma de comunicación.

**Prerequisitos obligatorios antes de cualquier desarrollo creativo:**
1. Prueba de concepto cuantitativa con el target para validar accionabilidad
2. Verificación de Gama sobre restricciones de contratos de imagen vigentes
3. Verificación de compatibilidad con plataforma de marca global (si aplica)

---

## BLOQUE 10 — AGENDA 2027 Y DECISIONES ABIERTAS

### Hipótesis abiertas que requieren ola 2027

| Hipótesis | Evidencia actual | Módulo para ola 2027 |
|---|---|---|
| Imagen experiencial en ascenso (+6.3pp 'atractiva', +5.8pp 'seguro') | Solo tendencia p_adj 0.058-0.089 | Repetir atributos + corrección BH-FDR |
| Debilitamiento imagen precio (-3.9pp, -5.1pp) | Solo tendencia p_adj 0.053-0.091 | Repetir + comparar con Rio/Paramo |
| Gap comunicacional PTL | Sin confirmación directa con estímulos | Módulo publicidad con estímulos de campaña + benchmark Rio |
| Arquetipo femenino accionable | Hipótesis cuali emergente 6/7 FG | Concept testing cuantitativo |
| WoW en NSE C+/C | Exploratorio, no pre-registrado | Pre-registrar en diseño 2027 |

### 5 mejoras metodológicas obligatorias para ola 2027

| Mejora | Justificación |
|---|---|
| MaxDiff reemplaza Likert saturado (P22) | Eliminar saturación T2B >90% en atributos que impide discriminar |
| NPS + switching explícito (3 preguntas) | Medir fidelidad activa, no solo preferencia declarada |
| CEPs expandidos (15-20 ocasiones vs 5 misiones genéricas) | Capturar fragmentación de misiones documentada en FG |
| Penetración 12m + frecuencia + ticket promedio | Construir modelo de share of wallet que V5 no puede calcular |
| Booster campo Pref-Gama n=80 + módulo comunicación con estímulos + Rio como benchmark | Ampliar base referencial + medir recall con estímulos de campaña |

### Decisiones Owner antes de presentar a Cora y a la Junta de Gama

| Código | Decisión | Implicación |
|---|---|---|
| CO-1 | ¿Señal de alerta Rio en proteínas entra al deck o al memo interno? | 1 verbatim FG (certeza muy baja). El Owner define el umbral de evidencia para señales de alerta en presentación ejecutiva |
| CO-2 | ¿Tono: "liderazgo defensivo sólido" o "señal de alerta competitiva"? | Ambas lecturas son verdad. El tono afecta cómo la junta de Gama recibe el reporte |
| CO-3 | ¿Recomendaciones de canal digital (Gama Club + inventario) entran al deck V5 o son propuesta de scope adicional? | El brief original era notoriedad/brand health — las recomendaciones digitales expanden el scope |

---

## CIERRE DEL DECK PRINCIPAL V5

Gama 2026 tiene dos lecturas válidas — y el Owner elige cuál presentar a la junta:

**Lectura defensiva (CO-2 opción A):** "0/8 métricas del embudo de Gama variaron significativamente. Gama es la única gran cadena del mercado que mantuvo posición en un año de movimiento. El activo relacional (OR=5.73) existe y es robusto. La posición en C+/C (TOM 60.6%) es la más fuerte del mercado."

**Lectura ofensiva (CO-2 opción B):** "Rio +17pp TOM (sig_99). Paramo +12pp TOM (sig_99). Posiblemente +25pp y +22pp en C+/C — el segmento de Gama. La conversión TOM→Preferida es 44.3%→8.0%. El 92% que no prefiere no está siendo activado. El anzuelo comunicacional está en el territorio equivocado."

Ambas son correctas. La diferencia es estratégica, no estadística.

*Notoriedad y Preferencia de Marca — Gama 2026 · V5 · n=402 · m.e. ±4.89% · Confidencial NDA*
*Cora Urrea + Raoul Bermudez · Versión: 2026-05-18*

---
---

# RESUMEN EJECUTIVO V5 — Notoriedad Gama 2026

**GAMA · 2026 · V5 · RE**
**Equipo analítico:** Cora Urrea + Raoul Bermudez · Confidencial / NDA

---

## Tesis V5 en una oración

Gama tiene el activo relacional más diferenciador del mercado y su posición en 2026 es sólida — pero comunica en el territorio equivocado, no activa al tercio de shoppers convertibles, y su segmento natural (C+/C) está siendo penetrado por Rio y Paramo a velocidad que exige respuesta antes de ola 2027.

---

## Tres datos que definen el estado de Gama en 2026

| # | Dato central | Certeza |
|---|---|---|
| 1 | Atención driver #1: OR=5.73*** (convergencia 4 métodos). El activo existe y es diferenciador. | ✅ Alta |
| 2 | Recall "PRECIOS DE TU LADO" = 0% espontáneo. 65% lo interpreta como precio (OR=1.03 NS). | ✅ Alta |
| 3 | Rio +17pp TOM (sig_99). Paramo +12pp TOM (sig_99). En C+/C: posiblemente +25.8pp y +22.3pp. | ✅ Total / ⚠ C+/C hipótesis |

---

## NSE C+/C: el campo de batalla más importante

| Métrica | C+/C 2026 | Total 2026 |
|---|---|---|
| TOM Gama | **60.6%** | 44.3% |
| Preferida Gama | **13.5%** | 8.0% |
| Movimiento Rio en C+/C (WoW) | **+25.8pp** ⚠ hipótesis | +17.0pp ✅ |
| Movimiento Paramo en C+/C (WoW) | **+22.3pp** ⚠ hipótesis | +12.1pp ✅ |

C+/C es donde Gama gana — y posiblemente donde Rio y Paramo avanzan más agresivamente.

---

## Los 4 hallazgos centrales del estudio 2026

**1. El activo es real, robusto y sin equivalente ✅**
OR=5.73*** en atención (4 métodos convergentes). 53% de preferentes lo citan espontáneamente. Ningún competidor del mercado tiene un activo relacional equivalente documentado.

**2. La barrera de conversión no es el precio ✅ + 💡**
Precio OR=1.03 (NS). La hipótesis cuali señala barrera identitaria en Seg 2: autoexclusión simbólica ("Gama es para otro tipo de persona") antes de comparar precios. Descuentos no la mueven — la primera experiencia sí.

**3. El Segmento 2 (33%) es la mayor oportunidad sin explotar ✅ + 💡**
0% preferencia actual, menor resistencia al precio en cuanti (3.44 vs 3.66/5), mecanismo de barrera definido (hipótesis cuali). Mayor retorno C/P de los tres segmentos.

**4. El Gama Club es un activo invisible con solución de bajo costo 💡**
Interés genuino en todos los segmentos (hipótesis cuali, 6/7 FG). La única barrera: opacidad digital del saldo. Solución: integración de saldo visible en app + canje en caja.

---

## 3 recomendaciones de mayor retorno a corto plazo

| Rec. | Qué | Evidencia | Accionabilidad |
|---|---|---|---|
| 1 — Quick win | Integrar digitalmente el Gama Club (saldo visible + canje en caja) | 💡 Hipótesis cuali 6/7 FG | Alta — cambio producto digital |
| 2 — Quick win | Reorientar mensaje del anzuelo: "razón para venir esta semana", no "precio bajo" | ✅ OR=3.64** + 💡 mecanismo identitario | Alta — reorientar campaña existente |
| 3 — Mid-term | Activación Seg 2: anzuelo → primera experiencia guiada → retención Club | ✅ k-means + 💡 mecanismo cuali | Media — diseño de activación |

---

## Decisiones Owner antes de presentar a la Junta

| Código | Decisión |
|---|---|
| CO-1 | ¿Señal de alerta Rio en proteínas al deck o al memo interno? (1 verbatim FG, certeza muy baja) |
| CO-2 | ¿Tono: liderazgo defensivo sólido vs señal de alerta competitiva? Ambas lecturas son válidas. |
| CO-3 | ¿Recomendaciones canal digital al deck V5 o propuesta de scope adicional? |

---

*Notoriedad Gama 2026 · V5 RE · n=402 · m.e. ±4.89% · Confidencial NDA · Cora Urrea + Raoul Bermudez · 2026-05-18*

---
---

# DIFF V5 vs V4 — Notoriedad Gama 2026

**Para:** Cora Urrea + Raoul Bermudez (circulación interna)
**Fecha:** 2026-05-18
**Propósito:** Registrar exactamente qué cambió entre V4 (2026-05-17) y V5 (2026-05-18)

---

## QUÉ NO CAMBIÓ

- Los datos cuantitativos (n=402, n=785, todos los OR values, todos los deltas WoW, k-means, NSE splits)
- Los caveats estadísticos (BH-FDR, IC95 amplios, composición geográfica 2025, CV-WOW-001/002/005, etc.)
- Los verbatims cualitativos (mismo corpus FG, 12 docs, 42,094 chars, mismos participantes)
- Las recomendaciones de fondo (Gama Club, reorientar anzuelo, activar Seg 2, canal digital)
- El gate Bruna: BR-2 V4 aprobado con ajustes — los claims aprobados siguen vigentes en V5 (mismos datos, mismos caveats)
- Las decisiones de wording DW-1..DW-5 aprobadas por Bruna — se mantienen en V5

---

## QUÉ SÍ CAMBIÓ

### CAMBIO 1 — Estructura: de complemento a documento standalone

| Aspecto | V4 | V5 |
|---|---|---|
| Framing de portada | "Capa analítica complementaria sobre V3" | "Análisis independiente y completo · Eje: datos 2026" |
| Sección A (V4) | Recap V3 — 6 slides de encuadre V3/V4 | No existe — V5 es autocontenido |
| Sección B (V4) | "Núcleo V3 preservado" (~25 slides de V3) | No existe en V5 |
| Prerequisito del lector | Conocer V3 para entender V4 | V5 se entiende sin V3 ni V4 |
| Longitud estimada | ~50+ slides (incluye núcleo V3) | ~40-45 slides (solo contenido propio V5) |

**Impacto operativo:** V5 puede presentarse de forma independiente a la junta de Gama sin necesidad de presentar también V3. V4 requería V3+V4 juntos para ser coherente.

---

### CAMBIO 2 — NSE C+/C: de análisis exploratorio a Capítulo 1

| Aspecto | V4 | V5 |
|---|---|---|
| Posición en el documento | Sección C (WoW), análisis exploratorio | Bloque 1 (primer capítulo sustantivo) |
| Etiqueta epistémica | "Exploratorio — hipótesis a confirmar ola 2027 (CV-WOW-005)" | Misma etiqueta (el dato no cambia), pero posición = central |
| Profundidad de análisis | Mencionado en slides C3/C4 de la sección WoW | Bloque completo con perfil C+/C, embudo Gama C+/C, competidores en C+/C |
| Narrativa | Parte de la historia WoW | El punto de partida del análisis |

**Impacto:** Para la audiencia ejecutiva de Gama, el hallazgo más relevante estratégicamente (amenaza en el segmento propio) es lo primero que ven.

---

### CAMBIO 3 — Peso epistémico del cualitativo: de "Triangulado" a "Hipótesis cuali"

Este es el cambio metodológico más importante. Responde directamente a la instrucción del Owner: "el cualitativo debe ser tratado como lo que es — generar insights e hipótesis, no conclusiones con el mismo valor que las respuestas cuantitativas."

| Claim | Etiqueta V4 | Etiqueta V5 | Qué cambia |
|---|---|---|---|
| Mecanismo acompañamiento-guía | "Triangulado: cuanti V3 + cuali V4" | ✅ Cuanti: OR=5.73 (conclusión) / 💡 Cuali: hipótesis sobre mecanismo | El OR=5.73 sigue siendo conclusión. El *mecanismo específico* pasa a hipótesis |
| Barrera sifrinaje | "Triangulado: cuanti V3 + cuali V4" | ✅ Cuanti: precio OR=1.03 NS (conclusión) / 💡 Cuali: hipótesis mecanismo identitario | La paradoja cuanti sigue siendo conclusión. El *mecanismo* pasa a hipótesis |
| Gama Club | "Cuali V4 [Tipo B]" | 💡 Insight cuali: hipótesis de oportunidad operacional | Sin cambio de fondo — el tag Tipo B ya indicaba hipótesis |
| Personificación femenina | "Cuali V4 FG emergente [Tipo B]" | 💡 Insight cuali emergente: hipótesis de territorio | Sin cambio de fondo |
| Pragmáticos Convertibles mecanismo | "Triangulado [Tipo B parcial]" | ✅ Segmento confirmado cuanti / 💡 Mecanismo: hipótesis cuali | La existencia del segmento sigue siendo conclusión; el mecanismo pasa a hipótesis |

**Lo que NO cambia con este cambio:** El nivel de certeza de los hallazgos cuantitativos (OR values, WoW deltas, k-means) es idéntico en V4 y V5. Solo cambia cómo se etiquetan los hallazgos derivados del análisis cualitativo.

---

### CAMBIO 4 — Rol de los datos 2025: de capa analítica a referencia comparativa

| Aspecto | V4 | V5 |
|---|---|---|
| Posición | Sección C — "Capa Wave-over-Wave" (~8 slides, posición co-principal) | Bloque 7 — "Evolución comparativa" (al final del deck, posición secundaria) |
| Narrativa | "¿La posición de Gama cambió 2025↔2026?" — pregunta central del análisis V4 | "¿Qué cambió como referencia?" — contexto al final del análisis 2026 |
| Framing | El WoW tiene su propia sección introductoria prominente | El WoW está embebido como "referencia evolutiva", con caveats siempre visibles |

**Impacto:** La narrativa de V5 no necesita justificar por qué 2026 es el eje de análisis — simplemente lo es. Los datos 2025 están presentes pero en segundo plano.

---

### CAMBIO 5 — Tesis central: de "extensión de V3" a "análisis primario 2026"

| Aspecto | V4 | V5 |
|---|---|---|
| Tesis explícita | "Gama tiene el activo relacional más diferenciador — V4 agrega mecanismo y dinámica WoW sobre V3" | "Gama tiene activo real y posición sólida — pero crecimiento cero en su segmento natural mientras Rio y Paramo avanzan" |
| Pirámide Minto | 4 argumentos MECE de V3 + enriquecimiento V4 | 4 argumentos MECE construidos desde cero con datos 2026 |
| Apertura del deck | Contextualiza V3 para introducir V4 | Arranca directamente con el diagnóstico 2026 |

---

## RESUMEN DEL DIFF EN UNA TABLA

| Dimensión | V4 | V5 | Tipo de cambio |
|---|---|---|---|
| Estructura del documento | Complemento a V3 (incluye núcleo V3) | Documento standalone | Arquitectural |
| NSE C+/C | Exploratorio en Sección WoW | Bloque 1 central | Reordenamiento |
| Cualitativo | "Triangulado" en algunos claims (co-igual a cuanti) | "Hipótesis/insight" explícito en todos los claims cuali | Epistémico |
| Datos 2025 | Capa analítica co-principal (Sección C) | Referencia comparativa (Bloque 7) | Reordenamiento |
| Longitud | ~50+ slides (incluye Sección B) | ~40-45 slides (sin Sección B) | Reducción |
| Tesis central | Extensión de V3 | Análisis fresh start desde 2026 | Narrativo |
| Todos los números/datos | — | Idénticos | Sin cambio |
| Todas las recomendaciones | — | Idénticas en fondo y dirección | Sin cambio |
| Gate Bruna BR-2 | Aprobado con ajustes | Vigente (mismos datos, mismos caveats, mismos wordings DW-1..5) | Sin cambio |

---

*Diff generado por OwnerBridge (delegado por Owner) · 2026-05-18 · Para uso interno Cora Urrea + Raoul Bermudez · Confidencial NDA*

---
---

## CAPABILITIES USADAS (OB-1)

- **Specialist delegado:** ninguno (ejecución directa — lectura de archivos Notoriedad 2.0 en Drive + síntesis analítica para V5)
- **Tools:** Drive MCP (`read_file_content` para V4 deck principal, V4 RE, V3 snippets, V2 snippets; `search_files` para localizar archivos Notoriedad 2.0)
- **Datos utilizados:** extraídos directamente de `2026-05-17_Notoriedad-Gama-2026_V4.pptx` (id: 1jSGEo2Zrqyj_MspSnaNWLFA1TuGjyK6G) y `2026-05-17_Notoriedad-Gama-2026_Resumen-Ejecutivo-V4.pptx` (id: 1aUcxNhvCjSWqSGcidATbt3SzrZm2an3p). Verificables en carpeta "Notoriedad V2.0" (id: 12mNlfK67gb2eb0KLp5vYKU8FmtOInBrg)

**Caveats de entrega:**
- ❌ Gráficos visuales (.pptx): requieren desktop (scripts python-pptx). Los `[GRÁFICO PLACEHOLDER: ...]` marcan exactamente dónde van
- ✅ Todo el contenido analítico, datos, caveats, verbatims y recomendaciones están en este archivo
- ✅ V5 Deck Principal, V5 Resumen Ejecutivo y Diff V5 vs V4 están incluidos en este único archivo
- Los datos 2026 que no encontré en los archivos V4 disponibles (algunos subgrupos de comportamiento, datos territoriales granulares) se marcan como "(ver BBDD para dato granular)" — disponibles en la BBDD de Notoriedad 2026 que Cora tiene

— OwnerBridge · 2026-05-17 21:01 Caracas
