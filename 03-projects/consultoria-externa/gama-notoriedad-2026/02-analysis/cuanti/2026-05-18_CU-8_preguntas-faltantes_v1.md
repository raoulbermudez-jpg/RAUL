# CU-8 Preguntas Faltantes — Gama Notoriedad 2026
**Fecha:** 2026-05-18 | **Base total: n=402** | **Significancia: alpha=0.05 (BH-FDR)**
**IC95:** Newcombe-Wilson | **Producido por:** Cuanti V4

> **Contexto:** CU-1 a CU-7 procesaron el embudo de notoriedad, drivers, pricing P31/P33/P34 y PTL. Este documento cubre las 12 preguntas restantes con datos en BBDD 2026 que no habian sido analizadas. Extiende, no reemplaza, lo ya documentado.

> **Gate Bruna obligatorio:** antes de incorporar cualquier cifra de este documento a un deck publico, Bruna debe revisar el §5 Caveats completo. Particularmente P44/P45 (base n=21) y todos los resultados de P32 (todas las celdas son REFERENCIALES).

---

## §1 Metodologia

### Preguntas procesadas
12 preguntas: PF8, PF9, PF10, P25, P26, P30, P32, P40, P41, P42, P44, P45.
PTL (P35/P37/P38/P39) se incluye solo como contraparte comparativa en cruces C1-C3 — no como analisis nuevo (ya estaba en plan original).

### Decisions metodologicas vigentes (ME-5)
- **Multiple tests:** BH-FDR (Benjamini-Hochberg False Discovery Rate) para todas las baterias de tests simultaneos >10.
- **IC95 proporciones:** metodo Newcombe-Wilson en todos los casos.
- **Base baja:** n<30 = REFERENCIAL (reportar pero no concluir con certeza). n<10 = excluir de inferencia.
- **Alpha:** 0.05.

### Hallazgo estructural: P26
P26 en BBDD es "Mejor supermercado por MISION DE COMPRA" (5 tipos: abastecimiento general, reabastecimiento parcial, no alimentos, evento/celebracion, urgencia), NO "mejor lugar por categoria de producto" como describia la guia de preguntas. Esto afecta el cruce B1 que originalmente buscaba P26×P32 por categoria. Se ajusta el cruce para usar P30 (habitual por categoria) vs P32 (mejor precio por categoria), que es analitica y metodologicamente equivalente para responder la pregunta de negocio.

### BLOCKER documentado
**[BLOCKER-CU8-P44/P45]:** P44 y P45 solo tienen datos validos en n=21 respondentes (parroquia El Recreo, unica zona con sucursal Gama activa). El resto de la muestra tiene respuestas en blanco por diseno del cuestionario (filtro P43). Todos los resultados de P44/P45 son ESTRICTAMENTE REFERENCIALES. No proyectables al mercado total.

---

## §2 Resultados por pregunta

### PF8 — Relacion con la zona (n=402)

| Categoria | n | % | IC95 |
|---|---|---|---|
| Vivo en la zona | 251 | 62.4% | [57.7, 66.9] |
| Trabajo en la zona | 104 | 25.9% | [21.8, 30.4] |
| No vivo ni trabajo, pero visito con frecuencia | 39 | 9.7% | [7.1, 13.1] |
| Pasaba por aqui por casualidad | 8 | 2.0% | [0.9, 3.9] |

**Lectura:** La muestra es predominantemente residente de la zona (62%). El 26% es trabajador, componente relevante para comunicacion en punto de venta. El 10% es visitante frecuente — potencial captable.

---

### PF9 — Rol en decision de compras del hogar (n=402)

| Categoria | n | % | IC95 |
|---|---|---|---|
| Responsable del 50% o mas de las decisiones | 251 | 62.4% | [57.7, 66.9] |
| Unico responsable de las decisiones | 151 | 37.6% | [33.1, 42.3] |

**Lectura:** El 100% de la muestra es decision-maker principal o co-principal. No hay respondentes con rol secundario. Esto es coherente con el filtro de reclutamiento del estudio (compradores activos).

**Cruce PF8 x PF9 (E2):** chi2=1.04, p=0.594 — NO significativo. El rol en la decision de compras es independiente de si el respondente vive, trabaja o visita la zona. No hay perfil diferenciado por relacion geografica.

---

### PF10 — Donde suele hacer compras de mercado (multi-select, n=402)

**Tipos de establecimiento visitados:**

| Tipo | n | % base total |
|---|---|---|
| Supermercados de cadena | 367 | 91.3% |
| Supermercados independientes grandes | 93 | 23.1% |
| Abastos / Bodegas | 82 | 20.4% |
| Tiendas independientes / chinos | 76 | 18.9% |
| Mercados populares | 64 | 15.9% |
| Mercados callejeros / Gochos | 54 | 13.4% |
| Tiendas especializadas (carniceria, fruteria) | 46 | 11.4% |
| Supermercados independientes pequenos | 20 | 5.0% |
| Delivery / Aplicaciones | 2 | 0.5% |

**Cadenas de supermercados nombradas (multi-mention, sobre n=367 cadena-goers):**

| Cadena | Menciones |
|---|---|
| Paramo | 119 |
| Forum | 87 |
| Rio | 75 |
| Central Madeirense | 71 |
| Plazas | 59 |
| Luz | 52 |
| **Gama** | **50** |
| Plan Suarez | 35 |

**Lectura (E1):** 9 de cada 10 compradores de la zona van a supermercados de cadena. Gama aparece en 7a posicion en menciones espontaneas de cadenas habituales (50/367 = 13.6% de quienes van a cadenas). La distancia con Paramo (119 menciones) es considerable, pero Gama supera a Plan Suarez y se ubica por encima de varios competidores. El ecosistema es de canales mixtos: 20% va a abastos/bodegas y 19% a chinos en paralelo con cadenas — la competencia no es solo entre supermercados.

---

### P25 — Razon de la ultima compra (n=402)

| Mision | n | % | IC95 |
|---|---|---|---|
| Reabastecimiento parcial | 270 | 67.2% | [62.5, 71.6] |
| Abastecimiento general completo | 94 | 23.4% | [19.4, 27.8] |
| Urgencia (pocos productos) | 31 | 7.7% | [5.4, 10.8] |
| Evento / celebracion | 6 | 1.5% | [0.7, 3.2] |
| No alimentos (electrodomesticos, ropa) | 1 | 0.2% | — |

**Lectura:** Dos tercios de las ultimas compras fueron de reabastecimiento parcial. Esto implica que el "ticket promedio" de la visita tipica no es un mercado grande sino una compra de mantenimiento. Solo 1 de 4 respondentes hizo su ultimo mercado grande en el supermercado consultado. Implicacion para comunicacion de precio: el shopper tipico en una visita reciente fue a "completar" el mercado, no a hacerlo completo.

---

### P26 — Mejor supermercado por mision de compra (n=402)

| Mision | Lider | Lider % | Gama % | Gap Gama-Lider | Ninguno % |
|---|---|---|---|---|---|
| Abastecimiento general completo | Paramo | 21.6% | 7.2% | -14.4 pp | 5.0% |
| Reabastecimiento parcial | Paramo | 16.4% | 8.7% | -7.7 pp | — |
| Evento / celebracion | Paramo | 13.7% | 9.2% | -4.5 pp | — |
| **Urgencia (pocos productos)** | **Gama** | **12.2%** | **12.2%** | **0 pp** | 24.6% |
| No alimentos (electrodom., ropa) | Hiper Lider | 6.0% | 0.5% | -5.5 pp | — |

**Hallazgo critico:** Gama es el supermercado LIDER para la mision de "compras de urgencia / pocos productos" con 12.2% de las menciones. Para las otras misiones de volumen (abastecimiento general, reabastecimiento parcial), Paramo lidera con ventaja. Para no alimentos, el mercado es de Hiper Lider.

> Nota: todos los resultados de P26 son REFERENCIALES para Gama (n por categoria < 50 en la mayoria de misiones). La posicion de lider en urgencia es un hallazgo de tendencia, no estadisticamente concluyente por si solo.

---

### P30 — Supermercado habitual por categoria (n=402)

**Gama en habito de compra por categoria (excluye "Ninguno en particular"):**

| Categoria | Gama % | Gama n | Lider | Lider % | Flag |
|---|---|---|---|---|---|
| Congelados | 8.0% | 32 | Paramo | 11.4% | OK |
| Salsas y Enlatados | 7.5% | 30 | Paramo | 20.4% | OK |
| Gaseosas, jugos y aguas | 7.2% | 29 | Paramo | 10.7% | REFERENCIAL |
| Galletas y confiteria | 7.0% | 28 | Central Madeirense | 13.9% | REFERENCIAL |
| Farmacia | 4.2% | 17 | **Gama (lider)** | 4.2% | REFERENCIAL |
| Cuidado y limpieza hogar | 5.0% | 20 | Paramo | 11.2% | REFERENCIAL |
| Productos basicos | 5.5% | 22 | Paramo | 19.7% | REFERENCIAL |
| Frutas, legumbres | 4.0% | 16 | Central Madeirense | 9.2% | REFERENCIAL |
| Carne de res | <3% | <12 | Paramo | ~30%+ | REFERENCIAL |
| Pollo | <3% | <12 | Paramo | ~30%+ | REFERENCIAL |
| Charcuteria | <3% | <12 | Paramo | ~30%+ | REFERENCIAL |

**Hallazgo farmacia:** Gama empata en liderazgo de habitual en categoria Farmacia (4.2%), por encima de Plan Suarez (3.5%), Forum y Paramo. Base n=17, REFERENCIAL.

**Paramo domina habitual en proteinas:** Carne, Pollo y Charcuteria tienen a Paramo como lider con mas de 30% de menciones en cada categoria. La ventaja de Paramo en estas categorias es estructural.

---

### P32 — Mejor precio por categoria (n=402, TODOS REFERENCIALES para Gama)

**Tabla maestra: lider en P32 + posicion y % de Gama por categoria**

| Categoria | Lider precio | Lider % | Gama % | Gama pos | Gap pp | Flag |
|---|---|---|---|---|---|---|
| **Farmacia** | Plan Suarez | 3.7% | **3.0%** | **#2** | -0.7 pp | REFERENCIAL |
| **Licores** | Forum | 4.7% | **3.5%** | **#4** | -1.2 pp | REFERENCIAL |
| Galletas y confiteria | Paramo | 11.4% | 5.7% | #8 | -5.7 pp | REFERENCIAL |
| Congelados | Paramo | 11.4% | 4.7% | #6 | -6.7 pp | REFERENCIAL |
| Salsas y Enlatados | Paramo | 20.9% | 4.5% | #9 | -16.4 pp | REFERENCIAL |
| Productos basicos | Paramo | 18.4% | 4.5% | #8 | -13.9 pp | REFERENCIAL |
| Cuidado y limpieza | Forum | 9.7% | 3.7% | #8 | -6.0 pp | REFERENCIAL |
| Gaseosas, jugos | Paramo | 10.2% | 3.2% | #8 | -7.0 pp | REFERENCIAL |
| Cuidado Personal | Paramo | 10.0% | 3.0% | #8 | -7.0 pp | REFERENCIAL |
| Carne de res | Paramo | 36.3% | 3.0% | #7 | -33.3 pp | REFERENCIAL |
| Pollo | Paramo | 35.3% | 2.5% | #9 | -32.8 pp | REFERENCIAL |
| Charcuteria | Paramo | 34.8% | 1.7% | #9 | -33.1 pp | REFERENCIAL |
| Frutas, legumbres | Central Madeirense | 13.2% | 2.2% | #9 | -11.0 pp | REFERENCIAL |
| Alimento mascotas | Paramo | 4.0% | 1.2% | #9 | -2.8 pp | REFERENCIAL |
| Pescados y mariscos | Paramo | 6.0% | 1.0% | #9 | -5.0 pp | REFERENCIAL |

**Patron general:** Paramo es el lider de precio percibido en 11 de 15 categorias. Gama no lidera en ninguna categoria de alta rotacion. Sus posiciones mas cercanas al liderazgo son Farmacia (#2, gap -0.7 pp) y Licores (#4, gap -1.2 pp) — dos categorias de compra poco frecuente y con alto porcentaje de "Ninguno en particular" (85% y 66% respectivamente).

**Interpretacion del alto "Ninguno en particular":** En Farmacia el 85% de respondentes no asigna ningun supermercado como mejor precio — la mayoria no compra farmacia en supermercados. En Licores, 66% dice ninguno. Esto significa que la "posicion #2" de Gama en Farmacia se da en un mercado muy pequeño de percepcion (solo ~60 personas respondieron un nombre especifico de supermercado en Farmacia).

---

### P40 / P41 / P42 — "De Tu Lado Siempre" (DTLS)

**P40 — Recall espontaneo de DTLS:**

| Respuesta | n | % | IC95 |
|---|---|---|---|
| Si, recuerda | 50 | 12.4% | [9.5, 16.1] |
| No recuerda | 352 | 87.6% | [83.9, 90.5] |

> Base total: n=402. Caveat: 87.6% del mercado NO ha visto ni escuchado DTLS. La frase tiene distribucion muy baja.

**P41 — Agrado de DTLS (base: n=50 que recordaron, REFERENCIAL):**

| Nivel de agrado | n | % |
|---|---|---|
| Mucho | 11 | 22.0% |
| Bastante | 10 | 20.0% |
| Algo | 18 | 36.0% |
| Poco | 6 | 12.0% |
| Nada | 5 | 10.0% |
| **Top2 (Mucho+Bastante)** | **21** | **42.0%** |

> Nota: base n=50 — REFERENCIAL. El IC95 del Top2 es aproximadamente [28%, 57%]. No concluyente estadisticamente pero la distribucion bimodal (22% Mucho + 36% Algo + 12+10% bajo) sugiere agrado moderado.

**P42 — Interpretacion de DTLS (open-end, base n=50, REFERENCIAL):**

Los 50 respondentes que recordaron DTLS explican su interpretacion. Categorias tematicas:

| Tema | n | % | Ejemplos |
|---|---|---|---|
| Precio / economia | 21 | 42.0% | "Que los precios estan a tu favor", "Se ajusta al bolsillo", "Piensa en mi bolsillo" |
| Acompanamiento / apoyo relacional | 13 | 26.0% | "Que siempre estan alli para ti", "Que son alguien en quien confiar" |
| Bienestar del cliente | 8 | 16.0% | "Pensando en la comodidad de sus clientes", "Piensa en el bienestar de uno" |
| Fidelidad / confianza | 4 | 8.0% | "La fidelidad del cliente", "Que siempre estara cerca" |
| Otros | 4 | 8.0% | Variados |

**Hallazgo interpretacion DTLS:** Aunque el nombre "De Tu Lado Siempre" es una frase relacional, el 42% de quienes la recuerdan la interpreta en clave de PRECIO / ECONOMIA. Solo el 26% la interpreta como acompanamiento/apoyo relacional. Esto indica que la frase tiene ambiguedad semantica: parte del mercado la lee como promesa de precio, parte como promesa de cercanía/apoyo.

---

### P44 / P45 — Gama vs cadenas de la zona (EL RECREO, n=21)

**BLOCKER ACTIVO: base n=21 respondentes de El Recreo. TODO es REFERENCIAL e indicativo.**

**P44 — Gama vs cadenas de la zona (n=21 validos):**

| Percepcion | n | % |
|---|---|---|
| Igual que las cadenas de la zona | 16 | 76.2% |
| Mucho mejor | 2 | 9.5% |
| Mejor | 1 | 4.8% |
| Mucho peor | 2 | 9.5% |

**P45 — Disposicion a comprar si Gama abre sucursal (n=21 validos):**

| Nivel de disposicion | n | % |
|---|---|---|
| Dispuesto | 10 | 47.6% |
| Algo dispuesto | 5 | 23.8% |
| Muy Dispuesto | 3 | 14.3% |
| Poco dispuesto | 2 | 9.5% |
| Nada dispuesto | 1 | 4.8% |
| **Alta disposicion (Muy + Dispuesto)** | **13** | **61.9%** |

**Por NSE (El Recreo, base muy baja — puramente indicativo):**

| NSE | n | Alta disposicion % |
|---|---|---|
| C+/C | 4 | 100.0% — EXCLUIR INFERENCIA |
| D | 3 | 33.3% — EXCLUIR INFERENCIA |
| E | 14 | 57.1% — REFERENCIAL |

> Interpretacion con extrema precaucion: entre los 21 residentes de El Recreo donde Gama opera, la percepcion mayoritaria (76%) es de paridad con otras cadenas de la zona (ni mejor ni peor). La disposicion a comprar en Gama es alta (62% alta/muy alta) pero la base es demasiado pequena para proyectar. Bruna debe decidir si estas cifras pueden mencionarse en el deck o solo en el documento interno.

---

## §3 Cruces analiticos — Respuesta directa al Owner

### A1. Categorias donde Gama sale relevante como la MAS ECONOMICA (Top-3)

**Respuesta directa:** Gama no lidera como "el mas economico" en ninguna categoria de alta rotacion. Los tres mejores resultados relativos de Gama en P32 son:

1. **Farmacia:** posicion #2 (3.0%), gap -0.7 pp vs lider Plan Suarez (3.7%). Pero el 85% de los encuestados no nombra a nadie como lider de precio en farmacia — la categoria es de perception muy dispersa.
2. **Licores:** posicion #4 (3.5%), gap -1.2 pp vs lider Forum (4.7%). Mismo patron: 66% dice "Ninguno". Mercado de percepcion pequeño.
3. **Galletas y confiteria:** posicion #8 (5.7%), gap -5.7 pp vs lider Paramo (11.4%). Aqui el mercado de percepcion es mas activo (menos "Ninguno") pero Paramo lidera con ventaja.

**Implicacion:** No existe una categoria donde Gama sea percibida como la opcion mas economica de forma relevante. La brecha de imagen de precio documentada en CU-5 (Gama percibida cara por 54% en P33) se confirma categoria por categoria. La estrategia de comunicacion de precio debe partir de cero en casi todas las categorias de alta rotacion.

---

### A2. Cruce P32 x P21 — percepcion de precio por categoria entre preferentes de Gama

**Respuesta directa:** Los preferentes de Gama (n=32, REFERENCIAL) tienen una percepcion de precio marcadamente distinta al resto del mercado:

| Categoria | Gama precio - Preferentes | Gama precio - No preferentes | Brecha |
|---|---|---|---|
| Salsas y Enlatados | **46.9%** | 0.8% | +46.1 pp |
| Productos basicos | **34.4%** | 1.9% | +32.5 pp |
| Carne de res | **25.0%** | 1.1% | +23.9 pp |
| Frutas, legumbres | **18.8%** | 0.8% | +18.0 pp |
| Charcuteria | **15.6%** | 0.5% | +15.1 pp |

> Base n=32 para preferentes — TODOS REFERENCIALES. No proyectables.

**Interpretacion:** Los propios preferentes de Gama ven a Gama como la opcion de mejor precio en varias categorias — una percepcion que el mercado general NO comparte. Esto confirma que hay un segmento pequeno pero fiel que construye su preferencia PARCIALMENTE sobre la percepcion de precio favorable. El reto es que esta percepcion positiva de precio esta "atrapada" en el nucleo de clientes actuales y no ha penetrado al mercado mas amplio.

---

### A3. Categorias donde Gama debe vigilar el precio en NSE C+/C para crecer en mercado natural

**Respuesta directa:** Las categorias de mayor alerta (gap mas grande entre Paramo/CM/Forum y Gama en NSE C+/C):

| Categoria | Lider | Lider % | Gama C+/C % | Gap pp | Prioridad |
|---|---|---|---|---|---|
| Carne de res | Paramo | 36.3% | 6.7% | -29.6 pp | CRITICA |
| Pollo | Paramo | 35.3% | 5.8% | -29.5 pp | CRITICA |
| Charcuteria | Paramo | 34.8% | 5.8% | -29.0 pp | CRITICA |
| Frutas, legumbres | Central Madeirense | 13.2% | 3.8% | -9.4 pp | ALTA |
| Productos basicos | Paramo | 18.4% | 9.6% | -8.8 pp | ALTA |
| Congelados | Paramo | 11.4% | 5.8% | -5.6 pp | MEDIA |

**Interpretacion:** Las proteinas (carne, pollo, charcuteria) son donde Paramo tiene la ventaja de imagen de precio MAS amplia y donde el NSE C+/C —el mercado natural de Gama— claramente percibe la diferencia. Si Gama quiere crecer en su segmento natural, la imagen de precio en proteinas es la batalla mas importante. Actuar sobre precio O comunicacion en estas 3 categorias tendria el mayor impacto percibido.

---

### A4. Tabla completa: lider P32 + posicion Gama + gap pp por categoria

Ver tabla maestra en §2 (P32). Resumen interpretativo:

- **Paramo domina en 11/15 categorias.** Su ventaja es sistematica, no sectorial.
- **Gama esta en posicion #7-#9 en la mayoria de categorias** — esto es consistente con el ranking general de P31 (posicion #6 en ranking forzado).
- **Unicas categorias donde Gama se acerca al top:** Farmacia (#2) y Licores (#4), ambas con bases de percepcion muy pequenas.
- **Las dos categorias de mayor volumen (productos basicos, proteinas)** son donde Gama tiene los peores numeros de percepcion de precio.

---

### B1. Relacion entre lugar de compra (P30 habitual) y percepcion de mejor precio (P32)

**Respuesta directa:** En 11 de 15 categorias, el lider de habito (P30) COINCIDE con el lider de mejor precio (P32). Esto indica que en la mayor parte del universo de categorias, el precio percibido SI es el driver principal de la eleccion de cadena.

**Las 4 excepciones (lider habitual ≠ lider precio) son analiticas:**

| Categoria | Lider habitual P30 | Lider precio P32 | Interpretacion |
|---|---|---|---|
| Galletas y confiteria | Central Madeirense | Paramo | CM tiene mejor percepcion de surtido/oferta en confiteria que de precio |
| Licores | Luz | Forum | El shopper de licores va a Luz por razones distintas al precio (cercania, surtido) |
| Farmacia | Gama (!) | Plan Suarez | Gama es el supermercado de farmacia habitual para quienes van en cadena, pero Plan Suarez es percibido como mas economico |
| Cuidado y limpieza | Paramo | Forum | Aqui hay competencia de precio con Forum que no se traduce aun en habito |

**Implicacion para Gama:** La "anomalia" de Farmacia es la mas rica: Gama ya es el lider de habitual en farmacia (compran ahi con frecuencia) pero NO tienen la percepcion de mejor precio. Esto indica que el shopper de farmacia en Gama va por conveniencia (esta de camino) — no porque lo perciba como el mas economico. Esta es una oportunidad: si Gama comunica precio en farmacia, puede convertir habito en conviccion.

---

### B2. Relacion mision / lugar / precio

**B2a — Mision ultima compra (P25) x Percepcion precio Gama en Productos Basicos (P32):**

| Mision ultima compra | n | Gama mejor precio basicos % |
|---|---|---|
| Abastecimiento general | 94 | 1.1% — REFERENCIAL |
| Reabastecimiento parcial | 270 | 5.9% — REFERENCIAL |
| Urgencia | 31 | 3.2% — REFERENCIAL |

**Interpretacion:** Quienes fueron a hacer mercado completo (abastecimiento general) NO le atribuyen a Gama el mejor precio en basicos (1.1%). Quienes fueron a completar (reabastecimiento parcial) si lo hacen ligeramente mas (5.9%). La mision dicta el nivel de sensibilidad al precio: los shoppers de mercado completo son mas exigentes con el precio y en ese contexto Gama falla mas.

**B2b — Congruencia habito (P30) x Preferencia (P21) en Productos Basicos:**

- Preferentes de Gama (n=32) que compran habitualmente en Gama en Productos Basicos: **56.2%** — REFERENCIAL.
- Porcentaje del total de la muestra que compra habitualmente en Gama en Basicos: **5.5%**.

La brecha entre 56% (preferentes) y 5.5% (total) confirma que los preferentes de Gama tienen una alta congruencia entre su preferencia declarada y su comportamiento de compra. El reto es que ese grupo es muy pequeno (n=32/402 = 8.0% del mercado).

---

### C1. Comparativo recall PTL vs DTLS

| Frase | Recall espontaneo | n que recuerda |
|---|---|---|
| "Precios de Tu Lado" (PTL) | 10.7% | 43 |
| "De Tu Lado Siempre" (DTLS) | 12.4% | 50 |
| Publicidad Gama en general (P35) | 4.2% | 17 |

**z-test PTL vs DTLS:** z=-0.754, p=0.451 — NO SIGNIFICATIVO.

**Respuesta directa:** Las dos frases tienen recalls estadisticamente identicos — no hay diferencia significativa entre cuantos recuerdan una vs la otra. Ambas tienen una penetracion muy baja (~11-12%), que es coherente con el 4.2% que recuerda la publicidad de Gama en general (P35 — recall espontaneo previo a estimulo). El recall de DTLS es ligeramente mayor (+1.7 pp) pero la diferencia es ruido estadistico.

---

### C2. Cual frase registra MAS y cual se acerca al territorio relacional

**Agrado (top2 Mucho+Bastante):**

| Frase | Base | Top2 % |
|---|---|---|
| PTL "Precios de Tu Lado" | 43 | **53.5%** |
| DTLS "De Tu Lado Siempre" | 50 | **42.0%** |

**z-test agrado:** p-value no concluyente (bases pequeñas, ambas REFERENCIALES).

**Respuesta directa:** PTL genera mayor agrado (53.5% vs 42.0%) entre quienes la recuerdan. La diferencia de 11.5 pp es relevante en magnitud pero NO estadisticamente significativa dado el tamaño de las bases.

---

### C3. DTLS genera mejor interpretacion relacional que PTL

**Comparativo temas de interpretacion:**

| Tema | DTLS % | PTL % |
|---|---|---|
| Precio / economia | **42%** | **72%** |
| Acompanamiento / apoyo relacional | **26%** | 2% |
| Bienestar del cliente | 16% | — |
| Fidelidad / confianza | 8% | — |

> Bases n=50 (DTLS) y n=43 (PTL) — REFERENCIALES.

**Respuesta directa:** Si. DTLS genera interpretacion en territorio relacional (26%) y de bienestar (16%) que PTL practicamente no activa (2%). Sin embargo, el tema de precio/economia domina incluso en DTLS (42%). PTL es leida casi exclusivamente como una promesa de precio (72%). La hipotesis del Owner se confirma en direccion: DTLS es MAS ambigua (puede ser precio O relacion), mientras PTL es unidimensional (solo precio). Si el objetivo estrategico es posicionarse en el territorio relacional de "acompanamiento", DTLS es la frase con mayor potencial semantico.

**Advertencia:** el 42% de DTLS que lo lee como promesa de precio puede ser un riesgo — si la marca no la cumple en precio, la frase puede generar disonancia. Esta tension entre lectura de precio y lectura relacional es el dato mas relevante para la decision.

---

### D1. P44 — Como se percibe Gama vs cadenas de la zona (n=21, SOLO INDICATIVO)

Entre los 21 respondentes de El Recreo:
- **76.2% percibe a Gama IGUAL que las cadenas de la zona.** Ni mejor ni peor.
- 14.3% la percibe mejor (Mucho mejor + Mejor).
- 9.5% la percibe peor (Mucho peor).

**Lectura:** La paridad perceptual es el hallazgo. Gama no tiene una imagen de superioridad clara en su zona de operacion actual. Tampoco tiene una imagen negativa grave. El "Igual" dominante puede ser bueno (no hay rechazo) o malo (no hay diferenciacion).

---

### D2. P45 — Disposicion a comprar si Gama abre sucursal (n=21, SOLO INDICATIVO)

- **Alta disposicion (Muy Dispuesto + Dispuesto): 61.9%** — la mayoria de los residents de El Recreo estaria dispuesto a comprar en Gama si abre mas cerca.
- Solo 14.3% (3 personas) dice Poco o Nada dispuesto.

**Lectura:** La intencion de compra es positiva en la zona de El Recreo, lo cual es coherente con el hecho de que Gama ya opera ahi. Sin embargo, con n=21, estas cifras son puramente ilustrativas.

---

### E1. PF10 — Distribucion de cadenas habituales (donde hace mercado)

Ver datos completos en §2 (PF10). Resumen: Paramo lidera en menciones (119), seguido de Forum (87), Rio (75), Central Madeirense (71). Gama ocupa la 7a posicion (50 menciones, 13.6% de quienes van a supermercados de cadena). La competencia es de canales mixtos: 20% de la muestra tambien va a abastos/bodegas.

---

### E2. PF8 x PF9 — Perfil del respondente

- 62.4% vive en la zona | 25.9% trabaja en la zona.
- 100% es decision-maker principal o co-principal en compras del hogar.
- La asociacion PF8 x PF9 no es estadisticamente significativa (chi2=1.04, p=0.594).

---

## §4 Hallazgos clave (10 hallazgos)

1. **Gama lidera "compras de urgencia" (P26):** Con 12.2% de menciones, Gama es el supermercado que el shopper elige cuando necesita comprar pocos productos con urgencia — superando a Paramo (9.5%). Es el unico territorio donde Gama es el primer nombre que viene a la mente. Esta posicion es coherente con su perfil de tienda de conveniencia/proximidad percibida.

2. **Gama es habitual en Farmacia (P30):** Gama empata el liderazgo de compra habitual en la categoria Farmacia (4.2%). Esto no es trivial — sugiere que el shopper usa a Gama como resolutor de urgencias y necesidades puntuales (farmacia + urgencia son el mismo territorio de comportamiento). Base n=17, referencial.

3. **Percepcion de mejor precio: Gama no lidera en ninguna categoria de alta rotacion (P32):** En las 15 categorias medidas, Gama no es percibida como la mas economica en ninguna de alta demanda. Sus mejores posiciones son Farmacia (#2) y Licores (#4), ambas con bases de percepcion muy diluidas (85% y 66% "Ninguno", respectivamente).

4. **Paramo domina precio en proteinas con ventajas estructurales (P32 x A3):** Carne, Pollo y Charcuteria tienen a Paramo liderando con gaps de 29-33 pp sobre Gama en el NSE C+/C. Estas son las categorias donde el shopper de mayor poder adquisitivo busca mejor precio y donde Gama esta mas lejos. Vigilar precio en estas categorias es la accion de mayor impacto percibido posible.

5. **Los preferentes de Gama SÍ perciben a Gama como economica en categorias clave (A2):** En Salsas y Enlatados, 46.9% de los preferentes de Gama (n=32, REFERENCIAL) cree que Gama tiene el mejor precio — vs 0.8% del resto del mercado. Esta percepcion de precio favorable "atrapada" en el nucleo de clientes actuales es el activo de precio mas relevante que tiene la marca, aunque no haya permeado al mercado general.

6. **En 11/15 categorias, el lider de habito y el lider de precio percibido son el mismo supermercado (B1):** La congruencia precio-habito es alta en el mercado. La excepcion mas rica es Farmacia: Gama es el lider de habitual pero no de precio. El shopper va a Gama por conveniencia, no por economia — oportunidad de comunicacion.

7. **DTLS y PTL tienen el mismo nivel de recall (C1) — ambos muy bajos:** 12.4% recuerda DTLS y 10.7% recuerda PTL. La diferencia no es estadisticamente significativa. Ambas frases son practicamente desconocidas para el mercado (88-89% no las ha visto). El problema no es cual frase es mejor — es que ninguna ha tenido distribucion suficiente.

8. **DTLS activa territorio relacional; PTL es solo precio (C3):** El 26% de quienes recuerdan DTLS la interpretan como acompanamiento/apoyo. Solo el 2% de quienes recuerdan PTL lo hace. Si el objetivo es posicionarse en territorio relacional, DTLS tiene ventaja semantica clara — aunque PTL genera mayor agrado puntual (53% vs 42% top2 agrado, diferencia no significativa estadisticamente).

9. **El shopper de Gama es predominantemente residente de la zona (62%) y decision-maker unico o principal (100%):** El perfil sociodemografico del respondente confirma que se encuesta al decisor real de compra. La compra habitual no es de paso — es del vecino de la zona. Esto tiene implicaciones para medios: canales de comunicacion hiperlocal (WhatsApp de comunidad, activaciones en zona) son mas eficientes que medios masivos.

10. **Mision dominante: reabastecimiento parcial (67%):** 2 de cada 3 visitas al supermercado son para completar el mercado, no para hacerlo completo. El shopper no va a "hacer el mercado" — va a "completar lo que falta". Esto redefine el ticket esperado y el tipo de oferta que Gama debe tener lista en cada visita.

---

## §5 Caveats para Bruna

| # | Caveat | Impacto | Frase recomendada para deck |
|---|---|---|---|
| CV-1 | P32 — TODOS los porcentajes de Gama por categoria tienen n<30. Son REFERENCIALES. | ALTO | "Tendencia indicativa — base referencial (n<30 por categoria)" |
| CV-2 | P44/P45 — Solo n=21 respondentes (El Recreo). No proyectable al mercado total. | ALTO | "Dato piloto — n=21, no proyectable" |
| CV-3 | P41 DTLS agrado — base n=50. IC95 muy amplio (+/- 14 pp en top2). | ALTO | "Referencial — base n=50" |
| CV-4 | P38 PTL agrado — base n=43. IC95 amplio (+/- 15 pp en top2). | ALTO | "Referencial — base n=43" |
| CV-5 | A2 cruce P32 x P21: preferentes de Gama n=32 — REFERENCIAL en todos los cruces. | MEDIO | "Tendencia — n=32, no concluyente" |
| CV-6 | P26 (misiones): la frase en cuestionario dice "mejor lugar para comprar por categoria de producto" pero en BBDD esta codificada como "mejor lugar por mision". El enunciado puede haber sido mal interpretado por algunos respondentes. | MEDIO | "Pregunta de mision de compra, no de categoria especifica" |
| CV-7 | C2 comparativo agrado PTL vs DTLS: diferencia de 11.5 pp (53% vs 42%) NO es estadisticamente significativa. No reportar como "PTL es mejor" sin caveat. | MEDIO | "Tendencia indicativa — diferencia no significativa al 95%" |
| CV-8 | P30 en casi todas las categorias para Gama: n por categoria 15-32 — mayoria REFERENCIAL. Solo Congelados y Salsas tienen n=30-32 que bordean el umbral. | MEDIO | "Habito de compra Gama referencial en la mayoria de categorias" |
| CV-9 | P25 "evento y no alimentos": n<10 — excluidos de inferencia. | BAJO | No reportar por separado — agregar a "Otros" |
| CV-10 | B2b cruce habito x preferencia: "preferentes de Gama" identificados por P21 incluyen solo n=32 — todas las cifras son indicativas. | BAJO | Reportar solo como patron directional |

---

## §6 Tabla resumen ejecutivo para Vivienne

Esta tabla conecta cada hallazgo clave de CU-8 con el slide o seccion recomendada en el deck de Notoriedad 2026.

| Hallazgo CU-8 | Fuente | Dato clave | Slide sugerido |
|---|---|---|---|
| Gama lidera mision de urgencia | P26 | 12.2% lider en urgencia | Posicionamiento Gama: "la tienda de tu zona para lo urgente" |
| Gama es habitual en Farmacia | P30 | 4.2% lider categoria Farmacia | Slide categorias de fortaleza (junto con urgencia) |
| Gama no lidera precio en alta rotacion | P32 tabla maestra | Gap -14 a -33 pp en proteinas | Slide brechas de imagen precio (alerta estrategica) |
| Paramo domina proteinas (precio) | P32 + A3 | Carne 36.3% Paramo vs 3.0% Gama | Slide vigilancia precio NSE C+/C — 3 categorias criticas |
| Preferentes ven a Gama economica | A2 | 46.9% en enlatados (ref) | Slide activos latentes de precio (caveat referencial) |
| 76% precio = habito en 11/15 cats | B1 | Coincidencia lider precio-habito | Slide drivers de eleccion de cadena por categoria |
| DTLS/PTL recall bajo (11-12%) | C1 | 88% no conoce ninguna frase | Slide awareness comunicacion — oportunidad de inversion |
| DTLS activa territorio relacional | C3 | 26% relacional vs 2% en PTL | Slide decision de frase: argumento para DTLS |
| Shopper es vecino de zona (62%) | PF8 | 62.4% vive en zona | Slide perfil del comprador — implicacion para medios locales |
| Mision dominante: completar mercado | P25 | 67.2% reabastecimiento parcial | Slide comportamiento de compra — "mision incompleta" |

---

*Producido por Cuanti V4 — 2026-05-18.*
*JSON canonico: `CU8_preguntas_faltantes_20260518_v1.json`.*
*Script reproducible: `scripts/cu8_preguntas_faltantes.py`.*
*Gate Bruna: obligatorio antes de publicar cualquier cifra de este documento. Ver §5 completo.*
*Handoff a Insighter: CU-8 completo. Preguntas de negocio A1-E2 respondidas en §3.*
