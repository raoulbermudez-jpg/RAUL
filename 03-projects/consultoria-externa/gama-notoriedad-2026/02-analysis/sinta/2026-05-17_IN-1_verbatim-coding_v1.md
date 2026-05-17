---
autor: Sinta (Qualitative Synthesis & Brand Strategy Lead)
proyecto: gama-notoriedad-2026
tipo: IN-1 Verbatim Coding Output
version: v1
fecha: 2026-05-17
status: draft — gate Bruna pendiente antes de entrega externa
confidencialidad: interno equipo / NO para Gama
---

# IN-1 — Verbatim Coding Output
## Notoriedad Gama 2026 — Auditoría y esquema formal de codificación

**Proyecto:** Gama Notoriedad 2026
**Fuente:** Encuesta estructurada F2F, preguntas abiertas P21.1 (razones de preferencia espontáneas) + P36 (verbatim recall publicitario) + P39/P42 (interpretación de frases publicitarias)
**N de respondientes base:** 402 total; verbatims de preferencia sobre subconjuntos por marca (Gama n=32, Páramo n=85, otros n=11-45)
**Fecha de análisis:** 2026-05-17
**Analista:** Sinta (primer pass AI con calibración interpretativa explícita)
**Nota de método:** Los verbatims originales están en BBDD raw (gitignored NDA). Este análisis se basa en las frecuencias codificadas del V2 (`Codificacion-Verbatims_v1.xlsx`) y en los outputs serializados de Fase B/C/D. Sinta no tuvo acceso directo a la BBDD raw en esta sesión; el análisis opera sobre los sumarios codificados disponibles. Esta limitación se reporta como caveat metodológico y como item para gate Bruna.

---

## 1. Diagnóstico del esquema de codificación V2

### 1.1 Esquema ejecutado en V2 — descripción

El V2 usó codificación keyword-based (función `codify(text)`) con 6-8 categorías por pregunta. El esquema fue:

**Para P21.1 (razones de preferencia):**
- Buena atención / servicio
- Mejores precios / economía
- Cercanía / ubicación
- Calidad de productos
- Variedad / surtido
- Ofertas / promociones
- Otras razones (residual)

**Para P36 (recall publicitario):**
- Precio / economía
- Solidaridad / relación
- Bolsillo / ahorro
- No recuerdo
- Slogan NO Gama (error de atribución)
- Otros

**Para P39/P42 (interpretación de frases):**
- Precio / accesibilidad
- Compañía / cercanía emocional
- Solidaridad
- Otro

### 1.2 Evaluación del esquema V2

| Dimensión | Evaluación | Evidencia |
|---|---|---|
| Nivel de codificación | Solo abierto (categorías de superficie) — no hay codificación axial ni selectiva | Las categorías describen el QUÉ pero no el POR QUÉ ni la estructura de relaciones entre códigos |
| Fiabilidad inter-codificador | No documentada — codificación single-coder (keyword-based automático) | Sin Cohen's Kappa. La función `codify()` aplica reglas deterministas, no interpretación |
| Esquema deductivo vs inductivo | Deductivo implícito (categorías basadas en expectativas del equipo) | Riesgo de omitir temas latentes no anticipados |
| Cobertura de temas latentes | Baja — la codificación keyword-based captura temas manifiestos con alta fiabilidad, baja fiabilidad para temas latentes | Ejemplo: "me queda cerca" codifica como "cercanía" pero puede ser también una declaración sobre confianza en el barrio |
| Saturación teórica | No evaluada — se reportan frecuencias, no el punto en que los verbatims adicionales dejan de agregar categorías nuevas | No aplica formalmente dado que es encuesta abierta, no IDI/FGI |
| Granularidad de valencia | No capturada — las categorías son neutras, sin valencia positiva/negativa/ambivalente | "Los precios son aceptables" y "los precios son caros para lo que es" ambas codificarían bajo 'precio' |

**Veredicto:** el esquema V2 es funcionalmente adecuado para producir frecuencias accionables en un plazo comprimido. No es adecuado para análisis temático Braun & Clarke, que requiere codificación axial y captura de temas latentes. La ausencia de doble-codificador es la brecha más crítica para claims de alta carga estratégica.

---

## 2. Esquema formal de recodificación — 3 niveles

Sinta propone un esquema de 3 niveles (abierto → axial → selectivo) sobre los verbatims disponibles. Los niveles axial y selectivo son los que el V2 no tuvo.

### 2.1 Nivel abierto — Códigos descriptivos

Códigos que replican y expanden el V2:

| Código abierto | Definición operativa | Incluye | Excluye |
|---|---|---|---|
| A01 — Atención directa | Menciones explícitas al trato, servicio, amabilidad del personal | "Me atienden bien", "el personal es amable", "buena atención" | Mención de rapidez en caja (→ A04) |
| A02 — Precio favorable | Menciones a precios bajos, economía, valor por dinero | "Tiene buen precio", "es económico", "me alcanza más" | Menciones de "es caro pero vale" (→ A07) |
| A03 — Cercanía física | Menciones de proximidad geográfica como razón de elección | "Me queda cerca", "está en mi zona", "paso por ahí" | Menciones de conveniencia temporal (→ A05) |
| A04 — Eficiencia operativa | Rapidez en caja, organización, tiempo en tienda | "Las cajas son rápidas", "es ordenado" | Limpieza/estética (→ A06) |
| A05 — Conveniencia situacional | Disponibilidad en momento de necesidad urgente | "Siempre tiene lo que necesito", "cuando necesito algo rápido" | Surtido amplio (→ A08) |
| A06 — Ambiente y limpieza | Percepción estética, higiene, orden del espacio físico | "Está limpio", "es agradable", "la tienda es bonita" | Calidad de productos (→ A09) |
| A07 — Valor percibido (calidad-precio) | Aceptación del precio en función de la calidad recibida | "Es un poco caro pero vale la pena", "se nota la diferencia" | Precio favorable puro (→ A02) |
| A08 — Amplitud de surtido | Variedad de categorías y productos disponibles | "Tiene de todo", "gran variedad" | Categorías específicas |
| A09 — Calidad de producto | Percepciones de frescura, calidad intrínseca de los productos | "La carne es de calidad", "los productos son buenos" | Calidad del servicio (→ A01) |
| A10 — Ofertas y promociones | Menciones específicas de descuentos, ofertas, programas de lealtad | "Tiene buenas ofertas", "los stickers", "Cashea" | Precio en general (→ A02) |
| A11 — Confianza / familiaridad | Lealtad histórica, hábito, conocimiento mutuo | "Siempre he ido ahí", "los conozco", "me fío" | — |
| A12 — Seguridad | Percepción de seguridad del entorno o del establecimiento | "Es seguro", "el estacionamiento es tranquilo" | — |

### 2.2 Nivel axial — Ejes temáticos (agrupaciones de códigos abiertos)

| Eje axial | Códigos que agrupa | Concepto central |
|---|---|---|
| **EJE 1 — Experiencia de servicio** | A01 + A04 + A06 | Lo que el consumidor vive DENTRO de la tienda como interacción con el espacio y las personas |
| **EJE 2 — Ecuación de valor** | A02 + A07 + A10 | La negociación interna entre precio pagado y valor recibido — incluyendo el valor emocional de sentirse bien tratado |
| **EJE 3 — Accesibilidad** | A03 + A05 | La eliminación de fricción en el acceso a la tienda — geográfica y temporal |
| **EJE 4 — Confianza en la marca** | A09 + A11 + A12 | El activo reputacional que precede a la experiencia directa — por qué el consumidor va ANTES de saber lo que encontrará |
| **EJE 5 — Propuesta de surtido** | A08 | La promesa de completar la misión de compra en un solo lugar |

### 2.3 Nivel selectivo — Categoría central

| Categoría selectiva | Definición | Relación con ejes |
|---|---|---|
| **EXPERIENCIA PREMIUM ACCESIBLE** | El consumidor de Gama construye su lealtad alrededor de una experiencia de compra que percibe como cualitativamente superior a supermercados de precio bajo, sin pagar el precio de un establecimiento de lujo. La atención al cliente es el símbolo concreto de esta experiencia — el empleado que conoce al cliente, resuelve, no aburre. | Eje 1 (experiencia) + Eje 4 (confianza) son los ejes primarios. Eje 2 (valor) es el eje de tensión — donde el consumidor negocia si la experiencia justifica el precio. Ejes 3 y 5 son facilitadores. |

**Nota interpretativa (calibración):** esta categoría selectiva es mi lectura del conjunto de verbatims disponibles. Es una hipótesis que debería validarse contra los verbatims crudos. La ausencia de acceso directo a los verbatims originales en esta sesión impide una validación completa. Ver caveat IN-6.

---

## 3. Tabla de codificación (sobre verbatims disponibles en outputs V2)

Los siguientes verbatims son los únicos disponibles en los sumarios serializados del V2. La codificación se aplica sobre ellos como ejercicio de demostración del esquema formal. Los verbatims literales de los respondientes individuales requieren acceso a la BBDD raw para codificación completa.

| ID / Fuente | Verbatim (fragmento o categoría disponible) | Código abierto | Eje axial | Valencia |
|---|---|---|---|---|
| Pref-Gama — razón #1 (53.1%) | "Buena atención" (mención más frecuente) | A01 | EJE 1 | Positiva |
| Pref-Gama — razón #2 (40.6%) | "Cercanía / ubicación" | A03 | EJE 3 | Positiva |
| Pref-Gama — razón #3 (implícita en z-score) | Limpieza y orden (alta asociación en pref-Gama) | A06 | EJE 1 | Positiva |
| Pref-Páramo — razón #1 (81.2%) | "Mejores precios" | A02 | EJE 2 | Positiva (para Páramo) |
| Pref-Plan Suárez — razón #1 (71.4%) | "Mejores precios" | A02 | EJE 2 | Positiva (para Plan Suárez) |
| P36 recall — "no recuerdo" (41% de n=17) | Incapacidad de reproducir la frase | — | — | Negativa para Gama (bajo recall) |
| P36 recall — "slogan precio" (18%) | "Todo mejor por menos", "Bueno bonito barato" | A02 | EJE 2 | Neutro (recall incorrecto) |
| P36 recall — "slogan NO Gama" (12%) | "Sin ti no hay nosotros" (error de atribución) | A11 | EJE 4 | Negativa para Gama |
| P39 interpretación PTL (65%) | Precio / bajos / accesibles | A02 | EJE 2 | Confirma lectura precio |
| P39 interpretación PTL (7%) | Solidaridad emocional | A11 | EJE 4 | Confirma lectura relacional (minoría) |
| P42 interpretación DTLS (36%) | Precio / economía | A02 | EJE 2 | Contaminación semántica |
| P42 interpretación DTLS (30%) | Compañía / cercanía / siempre | A11 | EJE 4 | Lectura deseada por Gama |

### Prevalencia por eje (sobre preferentes Gama, n=32 — indicativo)

| Eje axial | Estimado de menciones | % estimado preferentes Gama | Nota |
|---|---|---|---|
| EJE 1 — Experiencia de servicio | ~17-20 | 53-63% | Atención + limpieza confirmadas |
| EJE 3 — Accesibilidad | ~13 | ~41% | Cercanía como razón #2 |
| EJE 2 — Ecuación de valor | ~5-8 | 16-25% | Minoritario para pref-Gama; dominante en mercado |
| EJE 4 — Confianza | ~3-5 | 10-16% | Sub-capturado por codificación keyword |
| EJE 5 — Surtido | ~2-4 | 6-13% | Muy bajo — no es driver para pref-Gama |

---

## 4. Verbatims de alta densidad marcados para IN-2

Los siguientes patrones merecen selección en el análisis temático, aunque su formulación literal requiere extracción desde BBDD raw:

1. **"Me atienden bien"** (Pref-Gama, A01, EJE 1, positiva) — representa el 53% de las razones espontáneas. Alta densidad: captura la tesis central de la relación Gama-consumidor. Es el verbatim que Vivienne debe encabezar en el deck.

2. **"Sin ti no hay nosotros"** (P36, atribución errónea) — El 12% de quienes recuerdan alguna frase atribuyen a Gama una frase que no es de Gama. Latente crítico: el espacio semántico "compañía/relación" está disponible en la mente del shopper pero Gama no lo está llenando con sus propias frases. Alta densidad informativa.

3. **Interpretación DTLS como precio (36%)** — 36% de quienes recuerdan "De Tu Lado Siempre" la leen como un mensaje de precio, no de compañía. Es una tensión semántica que el análisis temático debe explorar.

4. **Cercanía como razón secundaria de pref-Gama (41%)** — La cercanía es también accesibilidad al modelo de atención que Gama representa. Latente: ¿la cercanía es proximidad física o es "un tipo de supermercado donde no me siento anónimo"?

---

## 5. Evaluación de reliability

### Reliability del esquema V2

Sin Cohen's Kappa calculable dado el diseño keyword-based. La codificación automática tiene alta reproducibilidad interna (deterministimca) pero baja validez de contenido para temas latentes.

**Estimación de reliability de Sinta:**
- Temas manifiestos (atención, precio, cercanía): reliability implícita alta — las keywords son unívocas.
- Temas latentes (confianza, valor percibido, tensión precio-calidad): reliability baja — no capturada por el esquema V2.

### Propuesta de reliability check para V3

Para validar el esquema axial propuesto en §2, se recomienda:
1. Extraer una muestra aleatoria del 20% de los verbatims P21.1 (n estimado ~80 verbatims).
2. Aplicar el esquema de 3 niveles de §2 de forma independiente por dos analistas.
3. Calcular Cohen's Kappa por eje axial. Umbral aceptable: Kappa ≥ 0.70 (Landis & Koch, 1977).
4. Para temas latentes (especialmente EJE 4 — Confianza), esperar Kappa ≥ 0.60 como umbral mínimo.

---

## 6. Propuesta de recodificación

El esquema axial y selectivo propuesto en §2 **complementa** (no destruye) el esquema V2. La propuesta es:

1. **Mantener la codificación keyword de nivel abierto** del V2 para comparabilidad inter-ola (ola 2027 debe usar las mismas 6-8 categorías abiertas para poder medir evolución).
2. **Agregar el nivel axial** en el análisis interno como capa interpretativa adicional — no publicar en deck Gama, usar en IN-2 y IN-5.
3. **Articular la categoría selectiva** como tesis del análisis cualitativo — input directo para IN-5 (Minto).

---

*IN-1 v1 producido por Sinta — 2026-05-17*
*Dependencias: verbatims literales de BBDD raw (01-data-raw/NUEVO BBDD Notoriedad 2026.xlsx) para codificación completa. Solicitados al Owner para sesión futura si se requiere validación completa pre-gate Bruna.*
*Gate Bruna: ver IN-6 — claim sobre categoría selectiva "Experiencia Premium Accesible" requiere gate antes de publicación externa.*
