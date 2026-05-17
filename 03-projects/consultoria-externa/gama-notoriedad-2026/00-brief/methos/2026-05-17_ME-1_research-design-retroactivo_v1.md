---
autor: Methos (Research Design & Methodology Lead)
proyecto: gama-notoriedad-2026
tipo: ME-1 Research Design Memo (retroactivo)
version: v1
fecha: 2026-05-17
status: draft — para revisión Owner antes de circulación
confidencialidad: interno equipo / NO para Gama
---

# ME-1 — Research Design Memo (Retroactivo)
## Notoriedad Gama 2026 — Diseño que debió haber existido

**Fecha:** 2026-05-17
**Autor:** Methos
**Para:** Owner / Cora (cuando aplique)
**Objetivo del memo:** Documentar el diseño de investigación que el estudio Gama 2026 debió haber tenido si hubiera partido de un proceso de diseño formal. Sirve como (a) diagnóstico de lo ejecutado, (b) blueprint de referencia para ola 2027, y (c) primer output canónico del agente Methos en este proyecto.

> **Nota de encuadre:** Este no es un escrito de demolición del trabajo realizado. El análisis V2 entregado a Cora el 2026-05-16 es técnicamente competente dentro de su scope. El propósito de este memo es elevar el techo hacia 2027, documentando el gap entre el diseño implícito que se ejecutó y el diseño formal que habría maximizado la validez y la accionabilidad del estudio.

---

## 1. Objetivo de negocio del estudio

**Como fue ejecutado (inferido de brief y plan v2):**
El objetivo de negocio no fue articulado explícitamente en ningún documento de brief. Se infirió operativamente como: *"Producir un deck de brand health con comparativo 2025–2026 para el equipo de mercadeo de Gama y su comité directivo."*

**Como debería haberse articulado formalmente:**

> Gama necesita determinar si su posición de marca en el corredor Caracas–Altos Mirandinos ha mejorado, empeorado o se ha mantenido respecto a 2025, para tomar decisiones de inversión en comunicación, precio y fidelización en el siguiente ciclo presupuestal (H2 2026). Los hallazgos deben ser suficientemente específicos para diferenciar acciones entre segmentos NSE C+/C y D/E.

**Por qué importa la diferencia:** un objetivo de negocio explícito que menciona la decisión downstream (inversión en comunicación, precio, fidelización) obliga al diseño a garantizar que el instrumento sea capaz de producir respuestas accionables a esas tres dimensiones. Sin esa articulación, el riesgo es un estudio que produce hallazgos descriptivos interesantes pero no directamente vinculados a decisiones de inversión — que es exactamente lo que ocurrió en algunas secciones (ej. precio sin curva de elasticidad, importancia sin discriminación real entre atributos).

---

## 2. Preguntas de investigación formales

Un diseño formal hubiera articulado las preguntas de investigación antes del instrumento. Las preguntas que el estudio debía responder, estructuradas por tipo:

### 2.1 Preguntas descriptivas (comparativas inter-ola)

| ID | Pregunta de investigación | Variables requeridas |
|---|---|---|
| D1 | ¿Cómo evolucionó la salud de marca de Gama (notoriedad, consideración, compra, preferencia) de 2025 a 2026 en la muestra total y en C+/C? | P16, P17, P19, P20, P21 × ola |
| D2 | ¿Cuál es el posicionamiento percibido de Gama en los 10 atributos funcionales vs la competencia? | P22, P23 × marcas |
| D3 | ¿Cómo perciben los shoppers el precio de Gama en comparación con cadenas competidoras? | P31, P32, P33, P34 |
| D4 | ¿En qué misiones de compra está presente / ausente Gama vs competencia? | P26 |

### 2.2 Preguntas relacionales / analíticas

| ID | Pregunta de investigación | Técnica analítica requerida |
|---|---|---|
| R1 | ¿Qué atributos funcionales son los drivers reales de preferencia por Gama, controlando por correlación entre atributos? | Regresión logística / KDA con Shapley |
| R2 | ¿Hay diferencia estadísticamente significativa en la salud de marca de Gama entre 2025 y 2026? | z-test de diferencia de proporciones inter-ola |
| R3 | ¿La cobertura física de Gama (n° sucursales por parroquia) explica la variación en preferencia? | Correlación Pearson / regresión geoespacial |

### 2.3 Preguntas que el estudio NO podía responder (debían ser explicitadas antes de fieldwork)

| ID | Pregunta imposible en este diseño | Razón técnica |
|---|---|---|
| I1 | ¿Cuál es el precio psicológicamente óptimo que Gama debería comunicar por categoría? | Requiere Van Westendorp o Gabor-Granger — no implementado |
| I2 | ¿Qué trade-off precio/calidad motivaría al shopper de D/E a cambiar preferencia hacia Gama? | Requiere Conjoint / DCM — no implementado |
| I3 | ¿Cuánta share of wallet vale en USD el grupo "11 perdidos a mercado grande"? | Requiere frecuencia + ticket promedio — no medido |
| I4 | ¿Qué activos visuales / sensoriales (colores, logo, jingle) son únicamente reconocibles de Gama? | Requiere DBA (Distinctive Brand Assets) — no implementado |
| I5 | ¿Cuál es la probabilidad de que un comprador de Gama lo recomiende activamente? | Requiere NPS — no implementado |

**Regla metodológica aplicada:** documentar explícitamente lo que un estudio NO puede responder es tan importante como documentar lo que sí puede, antes de iniciar el fieldwork (Groves et al., *Survey Methodology*, 2nd ed., 2009, Ch. 3).

---

## 3. Metodología recomendada (diseño ideal para 2026)

### 3.1 Clasificación del tipo de estudio

El estudio es de naturaleza **descriptiva longitudinal** (tracker de dos olas: 2025 + 2026) con elementos **relacionales** (drivers de preferencia vía análisis multivariante). No es causal (no hay asignación aleatoria de tratamientos) ni experimental.

Implicación: los hallazgos de drivers (regresión logística) son correlacionales, no causales. Toda afirmación del tipo "X genera preferencia" debe leerse como "X se asocia estadísticamente con mayor probabilidad de preferencia, sin poder descartar causalidad inversa o variables confundidas."

### 3.2 Metodología recomendada (cuanti con complemento cuali)

**Fase principal — Cuantitativa:**
- Encuesta estructurada face-to-face (F2F) en punto de intercepción en supermercados de cadena, Caracas + Altos Mirandinos.
- Justificación del modo F2F: el universo son shoppers activos en el punto de compra. El modo F2F en intercepción maximiza la representatividad geográfica y de NSE sin depender de acceso a internet ni listas de panel (sesgos de cobertura documentados en Couper, 2017, *Designing Effective Web Surveys*, §2.4). En el contexto venezolano, la penetración desigual de internet hace al panel online inadecuado para representar NSE D/E.
- Duración estimada: 20-25 minutos (cuestionario actual en rango correcto).

**Fase complementaria recomendada (no ejecutada en 2026) — Cuali:**
- 4-6 entrevistas en profundidad (30-45 min) con compradores de Gama (preferentes) vs compradores de Páramo (competencia directa) en C+/C.
- Propósito: comprender el "trabajo" que el shopper contrata a Gama vs Páramo — hallazgo que la cuanti no puede producir sola (Christensen et al., *Competing Against Luck*, 2016).
- Esta fase cuali hubiera informado (a) la formulación de atributos P22-P23, (b) el diseño de las misiones P26, y (c) la tesis estratégica final con mayor sustento interpretativo.

### 3.3 Justificación de técnicas cuantitativas (lo que debió haber estado en el diseño)

| Técnica | Justificación | Fuente |
|---|---|---|
| Notoriedad espontánea (TOM) — pregunta abierta antes de mostrar lista | Estándar global para medir salience sin contaminar. La lista asistida (P17) solo puede ir después. | Keller, *Strategic Brand Management*, 4th ed., 2013, §3 |
| Embudo secuencial (notoriedad → consideración → compra → preferencia) | El modelo de embudo refleja el proceso cognitivo-conductual del shopper. Cada etapa condiciona a la siguiente. | Aaker, *Managing Brand Equity*, 1991 |
| Importancia de atributos — **debería ser MaxDiff, no Likert** | Likert plano produce yea-saying bias: todos los atributos parecen importantes. MaxDiff fuerza trade-offs reales. Ver §4.2. | Louviere et al., *Best-Worst Scaling*, 2015; Finn & Louviere, 1992 |
| Asociación marca × atributo — multi-select binario (P23) | Correcto para medir linkage marca-atributo a nivel agregado. Limitación: no captura intensidad de asociación. | Keller, *op. cit.*, §5 |
| Regresión logística para drivers | Correcto cuando Y es binaria (prefiere Gama: sí/no) y se controla por multicolinealidad de atributos. El estudio lo implementó en Fase B (validado). | Hosmer & Lemeshow, *Applied Logistic Regression*, 3rd ed., 2013 |
| Ranking forzado (P31) para precio | Metodología válida pero interpretación delicada: todo respondiente asigna posición a toda marca, independientemente de conocimiento real. | Orme, *Getting Started with Conjoint Analysis*, 4th ed., 2019, §2 |
| Correlación Pearson para territorial | Correcto dado n pequeño de parroquias y variables continuas. Con n=10 puntos, la potencia del test es muy baja. | Cochran, *Sampling Techniques*, 3rd ed., 1977, §1.13 |

---

## 4. Diseño muestral

### 4.1 Diseño ejecutado — evaluación

| Dimensión | Lo ejecutado | Evaluación Methos |
|---|---|---|
| Marco muestral | Shoppers ≥1 compra/mes en supermercados de cadena | Adecuado para el objetivo declarado |
| Tipo de muestreo | Por cuotas (geo × NSE) en intercepción F2F | Adecuado para el contexto. No probabilístico en sentido estricto — cuotas son guía de reclutamiento. |
| n total | 402 | Suficiente para Total; insuficiente para subgrupos clave (ver §4.2) |
| Cuotas geográficas | Baruta 122 · Libertador 80 · Sucre 79 · Chacao 70 · El Hatillo 31 · Altos Mirandinos 20 | Razonables para cobertura, pero la distribución no parece derivada de potencia estadística a priori |
| Cuotas NSE | C+/C 104 (25.9%) · D 127 (31.6%) · E 171 (42.5%) | El segmento de interés primario (C+/C, n=104) tiene margen de error ±9.6% — marginal para análisis de subgrupo |
| Cuotas sexo / edad | No documentadas en brief | No está documentado si se establecieron cuotas de sexo y edad a priori o si son consecuencia del fieldwork |

### 4.2 Potencia estadística — evaluación formal

**Premisa:** el tamaño de muestra adecuado depende del test analítico más exigente planificado. Para un z-test de diferencia de proporciones entre dos marcas (ej. Gama 8% vs competidor X%) con:
- Nivel de confianza α = 0.05
- Potencia 1-β = 0.80
- Diferencia mínima detectable (MDD) = 10 pp (diferencia estratégicamente relevante)
- p1 = 0.08, p2 = 0.18

La fórmula de Cochran (1977, p. 57):

```
n = (z_α/2 + z_β)² × [p1(1-p1) + p2(1-p2)] / (p1 - p2)²
n = (1.96 + 0.84)² × [0.08×0.92 + 0.18×0.82] / (0.10)²
n = 7.84 × [0.0736 + 0.1476] / 0.01
n ≈ 7.84 × 0.2212 / 0.01 ≈ 173 por grupo
```

Para comparar Gama (n=32 en C+/C) con cualquier competidor en C+/C, la potencia es dramáticamente inferior a 80%. Diferencias de menos de ~25 pp entre proporciones no serán detectables con ese n. El estudio reportó este caveat correctamente en el doc técnico, pero la solución debería haber sido diseñar un booster a priori.

**Recomendación para 2027 (ver también ME-5 cuando se produzca):**

| Segmento | n ejecutado 2026 | n recomendado 2027 | MDD al 95% / 80% potencia |
|---|---|---|---|
| Total | 402 | 600 | ±5.0 pp |
| C+/C | 104 | 200 | ±7.1 pp |
| Pref-Gama | 32 | 80 (booster) | ±11 pp |
| Por parroquia clave | 18-122 (variable) | ≥50 mínimo | Análisis territorial habilitado |

### 4.3 Cuotas que debieron diseñarse a priori

Un brief formal debería haber especificado:

```
CUOTAS A PRIORI — Notoriedad Gama 2027 (propuesta)

n total objetivo: 600
Distribución NSE:
  C+/C:   200  (booster vs 104 en 2026 — habilita análisis por subgrupo)
  D:      200
  E:      200

Distribución geográfica (proporcional a volumen de shoppers por zona):
  Baruta:             ~150
  Sucre:              ~110
  Chacao:              ~90
  Libertador:         ~100
  El Hatillo:          ~80
  Altos Mirandinos:    ~70

Cuotas adicionales recomendadas:
  Sexo: 50% mujeres (± 5%)
  Edad: proporcional a perfil comprador (grupo adulto 25-54 debe representar ≥60%)
  Rol en compra: ≥80% decisores o codecisores de compra

Criterio de elegibilidad (screener):
  - Residente o trabajador del área geográfica
  - Realiza compras en supermercados de cadena ≥1 vez/mes
  - Mayor de 18 años
  - No trabaja en investigación de mercado, publicidad o cadenas de supermercado
```

---

## 5. Instrumentos — evaluación del cuestionario 2026

### 5.1 Fortalezas del cuestionario ejecutado

- Estructura de embudo secuencial correcta (TOM → asistida → consideración → compra → preferencia): cumple con el principio de no contaminar con mención de marcas antes de la espontánea.
- P22 (importancia) antes de P23 (asociación): correcto — evitar contaminar la percepción de importancia con el hecho de haber nombrado las marcas.
- Multi-select binario en P23 (asociación): operativamente robusto y comparable inter-ola.
- Ranking forzado en P31 (precio): produce datos ordinales más discriminativos que una escala de percepción libre.
- Módulos publicitario (P35-P42) y El Recreo (P43-P45) tratados como módulos independientes: decisión metodológicamente correcta para no contaminar el tracker principal.

### 5.2 Debilidades del cuestionario ejecutado — con propuesta de mejora

| Elemento | Problema | Impacto | Solución propuesta (2027) |
|---|---|---|---|
| P22 — Escala Likert 5 puntos para importancia | Yea-saying: todos los atributos saturan en 87-97% T2B. La escala no discrimina. | La variable importancia es inutilizable para priorización de inversión en comunicación | Reemplazar con MaxDiff (Best-Worst Scaling) — 8-10 tareas × 4 atributos por tarea. Produce utilidades escaladas que sí permiten jerarquía real. (Louviere et al., 2015) |
| P26 — 5 misiones genéricas | Solo cubre 5 ocasiones altamente abstractas ("mercado grande", "abastecimiento"). Ehrenberg-Bass recomienda 12-20 CEPs específicos con "7W framework" (por qué, cuándo, dónde, con quién, etc.) | No permite mapear mental availability por ocasión específica. No identifica CEPs donde Gama está ausente vs presente. | Expandir a 15-20 CEPs específicos. Ejemplo: "cuando se me acabó la leche", "para la comida de domingo en familia", "compra antes del fin de semana", "después de trabajar en semana". (Sharp, *How Brands Grow*, 2010, ch. 6; Romaniuk, 2023) |
| Sin NPS | Lealtad activa y probabilidad de recomendación no se miden | No hay KPI global de advocacy. No permite benchmark internacional. | Agregar: "¿Qué tan probable es que recomiendes [Gama] a un familiar o amigo? (0-10)" — por cada marca usada. Estándar Reichheld (2003). |
| Sin switching explícito | No se pregunta "si X no estuviera disponible, ¿a cuál irías?" | No se pueden construir flujos de sustitución. El cruce P21×P24 es proxy imperfecto. | Agregar después de P21 (preferida): "Si [marca preferida] no estuviera disponible hoy, ¿a cuál irías?" — single-select. |
| Sin penetración 12m | P20 mide compra últimos 3 meses, no 12m | Subestima penetración real. No permite calcular share of wallet financiero. Ehrenberg-Bass mide penetración anual, no trimestral. | Agregar: "¿En cuáles de estas cadenas compraste al menos 1 vez en los últimos 12 meses?" |
| Sin frecuencia ni ticket | No se pregunta cuántas veces/mes ni cuánto gasta | Share of wallet en valores $ no puede estimarse | Agregar: "¿Cuántas veces al mes vas a [cadena principal]?" y "¿Cuánto sueles gastar en una visita típica a [cadena]?" |
| Sin precio psicológico | P33 es escala ordinal de percepción (barato/caro) sin curva | No permite derivar precio óptimo por categoría | Van Westendorp (4 preguntas: muy barato / barato / caro / muy caro) en 3 categorías KVI (carne, pollo, granos) |
| Sin Distinctive Brand Assets | Solo se testa recordación de frases (P35-P42) | No se mide unicidad de colores, logo, jingles | Incluir: "¿Qué marca asocias con [color/logo/slogan]?" — test de atribución de assets sin nombre |
| Sin screener documentado | El cuestionario actual no tiene sección de screener documentada formalmente | Riesgo de contaminar muestra con non-shoppers o respondientes de bajo interés | Screener formal: ≥1 compra/mes en cadena, decisor/codecidsor, rango etario, excluir industria |
| Sin attention checks | No se documentan mecanismos de control de calidad de respuesta en la BBDD | Riesgo de respuestas de baja calidad no detectadas (en F2F es menor que en panel, pero existe) | En F2F: instrucción al encuestador de verificar coherencia. Agregar pregunta trampa si se migra a modo online en futuro. |

### 5.3 Ausencia de personalidad de marca / imagery

El cuestionario cubre bien el nivel 1 (Salience) y el nivel 2 (Performance) de Keller CBBE, pero omite los niveles 3 (Imagery — ¿qué valores/personalidad representa Gama?) y 4 (Resonance — ¿hay conexión emocional, advocacy?). Para un tracker que quiere informar estrategia de comunicación, esta es una brecha sustantiva.

**Propuesta 2027:** agregar batería de 8-10 adjetivos de personalidad de marca (cercano, sofisticado, accesible, tradicional, moderno, confiable, divertido, exclusivo) en escala "¿en qué medida esta palabra describe a [marca]? (1-5)" para las 3 marcas principales (Gama, Páramo, Plan Suárez). Referencia: Aaker, J.L., *Dimensions of Brand Personality*, Journal of Marketing Research, 1997.

---

## 6. Plan de análisis a priori

Este es el plan analítico que debería haberse documentado ANTES de ver los datos. La ausencia de este documento a priori implica riesgo de análisis post-hoc (data-driven hypothesis formulation = HARKing), que es una violación metodológica grave según el marco AAPOR (Wasserstein & Lazar, *American Statistician*, 2016; ver también la sección de alertas en ME-4).

### 6.1 Análisis planificados por pregunta de investigación

| Pregunta | Test / análisis | Software | Output esperado |
|---|---|---|---|
| D1 — Evolución de salud de marca | z-test diferencia de proporciones inter-ola (n1=785 2025, n2=402 2026) | Python statsmodels | Tabla con Δpp + p-value + signo significancia por etapa × marca |
| D2 — Posicionamiento atributos | z-score por atributo (normalización vs campo) + z-score por marca (perfil interno) | Python scipy | Heatmap 10×10 atributos × marcas |
| D3 — Percepción precio | Distribución frecuencias P33 + mean rank P31 + top-3 % P32 | Python pandas | Tablas + clasificación SENSIBLE/INTERMEDIA/FRAGMENTADA |
| D4 — Misiones | Cross-tab marca × misión + chi-cuadrado de asociación | Python scipy | Tabla de presencia por misión × marca |
| R1 — Drivers preferencia | Regresión logística (Y=Pref-Gama) con 10 predictores binarios P23. Reportar OR + IC 95% + p-value + pseudo R² McFadden | Python statsmodels | Tabla drivers con ranking OR |
| R2 — Comparativo inter-ola | z-test de proporciones con corrección por n diferente | Python statsmodels | Iconos ↑/↓/≈ por métrica × marca |
| R3 — Territorial | Pearson r (cobertura × preferencia por parroquia, n parroquias ≥10, filtro base mínima n≥18) | Python scipy | r + p-value + scatter plot |

### 6.2 Análisis adicionales (no estaban en el plan original — fueron incorporados en Fase B/C sin pre-registro)

| Análisis | Status en 2026 | Riesgo metodológico |
|---|---|---|
| Drivers por competidor (logit para cada marca) | Ejecutado en Fase C | Análisis post-hoc inspirado en comentarios de Cora. Válido analíticamente, pero no pre-registrado. |
| DNA z-score comparativo cross-brand | Ejecutado en Fase C | Ídem |
| Latent class sobre P22+P26+P30 | No ejecutado | Recomendado para 2027 |
| Switching implícito P21×P24 | Ejecutado parcialmente | Proxy aceptable, pero limitado como evidencia de flujos reales |

---

## 7. Supuestos y límites formales del estudio

Todo estudio tiene supuestos que, si se violan, comprometen la validez de sus conclusiones. El diseño implícito de este estudio asumió los siguientes, que debieron haberse documentado a priori:

| Supuesto | Verificado en datos? | Riesgo si se viola |
|---|---|---|
| Los shoppers de supermercado de cadena representan suficientemente el universo comprador de Gama | Parcialmente — se excluyó canal popular/chino/online | Subestimación de penetración en NSE D/E donde el canal informal es relevante |
| Las cuotas geográficas son proporcionales a la distribución real de shoppers | No verificado contra dato externo | Posible sobre/subrepresentación de zonas |
| Los 10 atributos de P22-P23 son los más relevantes para la categoría supermercado en Caracas | No validado con cuali previo | Pueden faltar atributos críticos (ej. conveniencia digital, delivery, parking) |
| La comparación 2025-2026 es válida aunque el cuestionario cambió en algunos ítems | Se restringió comparación a ítems comunes — correcto | Si la formulación de ítems comunes también cambió, el comparativo es inválido |
| La regresión logística identifica drivers causales | FALSO — identifica correlatos estadísticos | Recomendar inversión en atributos solo porque son predictores estadísticos puede ser error si la causalidad es inversa |
| n=32 (Pref-Gama en C+/C) es suficiente para la regresión logística | Parcialmente válido (ratio 40:1 aceptable, pero SE amplios) | Los OR de la regresión deben interpretarse como direcciones, no como estimaciones precisas |

---

## 8. Cronograma ideal que debió haberse seguido

El estudio operó con un cronograma de emergencia (3 días) impuesto por el deadline de Cora. Un estudio con este nivel de complejidad analítica debería tener:

| Fase | Duración ideal | Lo ejecutado |
|---|---|---|
| Brief + diseño (ME-1) | 3-5 días | No existió formalmente |
| Diseño instrumento (ME-2) | 5-7 días (incluye revisión y piloto) | El instrumento fue pre-existente — no hubo piloto documentado |
| Fieldwork (Cora) | 15-20 días para n=402 F2F | No documentado — fecha de campo pendiente |
| Recepción + QA de BBDD | 2-3 días | Ejecutado en Fase A (1-2 días) |
| Análisis (Cuanti) | 7-10 días | Ejecutado en 3-4 días (comprimido) |
| Redacción + deck (Vivienne) | 3-5 días | Integrado con análisis (comprimido) |
| Revisión cliente + iteración | 3-5 días | 1 ronda de comentarios Cora |
| **Total ideal** | **38-50 días** | **~4 días desde inicio análisis hasta entrega** |

La compresión fue operativamente exitosa, pero impidió aplicar las mejoras metodológicas que hubieran requerido iteración en el diseño (piloto de cuestionario, cuali previa, diseño a priori).

---

## 9. Presupuesto estimado (referencial para 2027)

Sin presupuesto de fieldwork documentado en el brief original. Para ola 2027 con las mejoras recomendadas:

| Componente | Estimado referencial | Notas |
|---|---|---|
| Diseño metodológico (Methos) | Interno — sin costo incremental | Costo de oportunidad del Owner |
| Fieldwork n=600 F2F Caracas (Cora + campo) | USD 8,000–14,000 | Depende de honorario Cora + supervisión |
| Análisis cuanti (Cuanti) | Interno | Cuando el agente esté operativo |
| MaxDiff software/análisis | USD 500–2,000 si externo | Sawtooth SSI Web o Lighthouse Studio; puede hacerse con paquetes R/Python gratuitos |
| Van Westendorp (3 categorías) | Sin costo incremental | Añadir preguntas al cuestionario |
| Auditoría precios real (Rec. 6 de Reflexiones 2027) | USD 3,000–8,000 | Proveedor externo o shoppers misteriosos |
| Conjoint/DCM (Rec. 7 — solo si Gama lo aprueba) | USD 10,000–20,000 adicionales | Inversión estratégica de ola mayor |
| Deck ejecutivo + presentación | Interno (Vivienne) | |
| **Total mínimo (sin Conjoint)** | **USD 11,500–24,000** | |
| **Total con Conjoint** | **USD 21,500–44,000** | |

---

## 10. Referencias metodológicas citadas en este memo

- Aaker, D.A. (1991). *Managing Brand Equity*. Free Press.
- Aaker, J.L. (1997). Dimensions of Brand Personality. *Journal of Marketing Research*, 34(3), 347-356.
- Christensen, C.M., Hall, T., Dillon, K., & Duncan, D.S. (2016). *Competing Against Luck*. HarperBusiness.
- Cochran, W.G. (1977). *Sampling Techniques*, 3rd ed. Wiley.
- Couper, M.P. (2017). *Designing Effective Web Surveys*. Cambridge University Press.
- Finn, A., & Louviere, J.J. (1992). Determining the Appropriate Response to Evidence of Public Concern: The Case of Food Safety. *Journal of Public Policy & Marketing*, 11(2), 12-25.
- Groves, R.M., Fowler, F.J., Couper, M.P., Lepkowski, J.M., Singer, E., & Tourangeau, R. (2009). *Survey Methodology*, 2nd ed. Wiley.
- Hosmer, D.W., & Lemeshow, S. (2013). *Applied Logistic Regression*, 3rd ed. Wiley.
- Keller, K.L. (2013). *Strategic Brand Management*, 4th ed. Prentice Hall.
- Louviere, J.J., Flynn, T.N., & Marley, A.A.J. (2015). *Best-Worst Scaling: Theory, Methods and Applications*. Cambridge University Press.
- Orme, B.K. (2019). *Getting Started with Conjoint Analysis*, 4th ed. Research Publishers LLC.
- Reichheld, F.F. (2003). The One Number You Need to Grow. *Harvard Business Review*, 81(12), 46-54.
- Romaniuk, J. (2023). *Better Brand Health*. Ehrenberg-Bass Institute. Oxford University Press.
- Sharp, B. (2010). *How Brands Grow*. Oxford University Press.
- Wasserstein, R.L., & Lazar, N.A. (2016). The ASA's Statement on p-Values: Context, Process, and Purpose. *The American Statistician*, 70(2), 129-133.

---

*Fin del ME-1 — Research Design Memo Retroactivo v1*
*Siguiente output: ME-3 (Methodology Rationale) y ME-4 (Vigilance Q2-2026)*
