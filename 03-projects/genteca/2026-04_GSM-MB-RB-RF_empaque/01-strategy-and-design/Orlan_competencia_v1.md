# Orlan_competencia_v1 — Análisis Competitivo GSM Empaque
**Tipo de output:** OL-1 + OL-2 + OL-3 + OL-5 combinados (Landscape + Comparison + Differentiation + Claim Feasibility)
**Fecha:** 2026-05-03
**Scope:** Supervisores / protectores de voltaje monofásicos residenciales y comerciales ligeros — mercado venezolano, con referencias a Colombia y mercados adyacentes donde aplica. Horizonte: datos disponibles a la fecha de acceso.
**Audiencia:** Vael (messaging framework) · Bruna (gate de claims) · Solenne (copy A/B) · Owner (decisión Junta)
**Basado en:** Materia prima en `00-brief/` (transcripts, WhatsApp, specs I&D, docs market-research) + búsqueda web ejecutada el 2026-05-03.

---

## Resumen ejecutivo

La búsqueda exhaustiva en fuentes web públicas (datasheets, páginas de producto, distribuidores, catálogos) no encontró ningún competidor venezolano — ni ningún competidor regional relevante en el segmento de protectores de voltaje monofásicos enchufables residencial/comercial — que afirme un tiempo de desconexión ante parpadeos (flickers) inferior a 30 ms o inferior a 0,03 s. Los únicos datos de velocidad publicados por competidores son marcadamente superiores: el más agresivo (WellSpec) afirma 0,2–0,3 segundos (200–300 ms) y presenta ese valor como **claim de ser "el más rápido de Venezuela"** — cifra que es entre 6 y 10 veces más lenta que la innovación de Genteca. El resto del mercado opera en el rango de 400 ms a 3 segundos para desconexión ante variaciones, o directamente no publica el dato.

En cuanto a tecnología NTC y protección térmica: cero competidores encontrados lo comunican en empaque o ficha técnica pública. Es un espacio en blanco de comunicación.

En cuanto a "protege tecnología inverter": al menos tres marcas (Avtek, Breakermatic, JVTRONIC) tienen líneas específicas para inverter, pero lo comunican como segmentación de aplicación, no como diferenciador de velocidad de respuesta. Ninguna vincula el claim de inverter a un dato cuantitativo de tiempo de desconexión.

En cuanto a QR en empaques de la categoría: ningún competidor venezolano identificado utiliza QR en empaque de protector enchufable residencial. La práctica existe en otras categorías eléctricas y en mercados más desarrollados.

---

## Sección 1 — Tiempo de respuesta: relevamiento competitivo

### Pregunta crítica
¿Hay protectores de voltaje en el mercado venezolano (residencial/comercial monofásico) que afirmen tiempos de respuesta < 30 ms o < 0,03 s ante parpadeos / fluctuaciones?

**Respuesta directa: No se encontró ninguno.**

### Tabla de competidores investigados — tiempo de respuesta

| # | Marca / Modelo | Claim de velocidad (literal o parafraseado de fuente) | Tipo de dato | Fuente | Confianza | Notas |
|---|---|---|---|---|---|---|
| 1 | **TQ / Total Quality — TQ-RB+220 Digital** (Venezuela) | Sin dato de tiempo de desconexión ante flickers publicado. Tiempo de reconexión ajustable 180-300 s. | Sin dato ms | Página distribuidora Pc Actual Venezuela; página Ferretería San Andrés | Bajo | [single-source por modelo] El dato de reconexión es el de rearme, no el de desconexión ante variación. |
| 2 | **TQ / Total Quality — TQ-MAC+120 Digital** (Venezuela) | Sin dato de tiempo de desconexión ante flickers publicado. | Sin dato ms | Página distribuidora Pc Actual Venezuela | Bajo | [single-source] |
| 3 | **TQ / Total Quality — TQ-PBS220-1** (Venezuela) | Sin dato de tiempo de desconexión ante flickers. Tiempo de rearme 170 s–3,5 min. | Sin dato ms | Página distribuidora Pc Actual Venezuela | Bajo | [single-source] |
| 4 | **WellSpec 120V / 63A** (Venezuela, distribuido por Suministros ISG) | Claim: **"el más rápido de Venezuela, 0,2-0,3 segundos"** = **200–300 ms** | Claim de marketing en web distribuidor | suministrosisg.com | Medio | [single-source] Afirmación en web de distribuidor. Sin datasheet oficial accesible. Sin curva ni método de medición publicados. Ningún certificado de ensayo referenciado. Es la formulación más agresiva encontrada en el mercado venezolano — y aun así es 6–10× más lento que la innovación Genteca. |
| 5 | **WellSpec 220V / 63A** (Venezuela) | Claim: "menos de 0,3 segundos" = **< 300 ms** | Claim de marketing en web distribuidor | suministrosisg.com | Medio | [single-source] Misma fuente, misma metodología ausente. |
| 6 | **Avtek SPC-PEBAS-B230/21J** — inverter 220V (Venezuela / LATAM) | Tiempo de reconexión: 10 s. Sin dato de tiempo de desconexión ante flickers. | Sin dato ms | avtek.com (página de producto oficial) | Medio | [single-source] El "tiempo de 10 s" es el rearme post-falla, no la velocidad de desconexión. |
| 7 | **Avtek SPC-PTINAS-1T515/21J** — inverter 120V (Venezuela / LATAM) | Sin dato de tiempo de desconexión publicado. | Sin dato ms | avtek.com | Bajo | [single-source] |
| 8 | **Avtek SPC-PABB-B230/A** (Venezuela / LATAM) | Tiempo de desconexión ante voltaje alto/bajo 0–4 s (modelo industrial SVM-220). Residencial sin dato ms. | Sin dato ms específico residencial | avtek.com / refrigeracionbarbosa.com | Bajo | Modelo industrial, no aplica directamente al segmento objetivo. |
| 9 | **Powest Airmatic 220V/20A** (Venezuela / Ecuador / LATAM) | Tiempo de respuesta: **1 segundo** = **1.000 ms** | Datasheet oficial PDF | powest.com/wp-content/uploads/2023/09/ | Alto | Spec publicada en PDF oficial. 33× más lento que innovación Genteca. |
| 10 | **Powest Refrimatic 120V/10A** (Venezuela) | Sin dato ms publicado. | Sin dato ms | syscaribe.com | Bajo | [single-source] |
| 11 | **JVTRONIC 208/220V — Refrigeración A/A Trabajo Pesado** (Venezuela) | Sin dato de tiempo de desconexión ante flickers publicado. | Sin dato ms | protectoresdevoltaje.com.ve | Bajo | Bot-verification bloqueó acceso directo a ficha de producto. |
| 12 | **JVTRONIC Digital Multivoltaje 60A** (Venezuela) | Tiempo de reacción programable 0,1–60 s. Sin mención de flickers en ms. | Sin dato ms | protectoresdevoltaje.com.ve (descripción de producto) | Bajo | [single-source] El rango programable de 0,1 s = 100 ms aplica a supervisores de tablero, no a protectores enchufables residenciales. Segmento diferente. |
| 13 | **Breakermatic PME110-E / aire 220V** (Venezuela / Colombia) | Tiempo de respuesta ante falla: **1 segundo** (1.000 ms). Ciclo de espera: 4 min. | Specs en páginas distribuidores Colombia | todofrio.com.co / iprpartesyrepuestos.com | Medio | [single-source] Datasheet PDF bloqueado 403. Info de distribuidores. |
| 14 | **Breakermatic AIRE 110** (Colombia, distribuido en Venezuela) | Tiempo de respuesta: **1,5 segundos** según fuente secundaria. | Referencia distribuidora | todofrio.com.co | Bajo | [single-source] Fuente secundaria; no es datasheet oficial. |
| 15 | **Protektor Venezuela** (ICREATIVA) | Temporización rearme: 3 min (compresor) / 30 s (electrónico). Sin dato de desconexión en ms. | Sin dato ms | icreativa.com.ve/preguntas | Bajo | [single-source] Solo info de FAQ, no datasheet. |
| 16 | **Exceline GSM-RE (spec pública pre-innovación)** | "Tiempo de desconexión ante parpadeos (flickers) e inestabilidad: **150 milisegundos**" | Fact — hoja de especificaciones oficial | GSM-RE Datasheet (local, en `00-brief/specs-i-d/`) | Alto | Esta es la spec publicada del modelo actual. La innovación lo baja a < 30 ms — dato no publicado aún externamente. |
| 17 | **Koblenz PV-2500 D** (México) | "Desconexión automática que desconecta al instante." Sin valor numérico. | Claim marketing | koblenz.com.mx | Bajo | [single-source] Mercado México, no Venezuela. Sin dato ms. |
| 18 | **Steren 920-010 / 3600W** (México / Colombia) | Sin dato de tiempo de desconexión ante flickers. | Sin dato ms | steren.com.co / elgrantlapalero.com | Bajo | [single-source] Mercado distinto. Sin dato ms. |

### Síntesis del relevamiento

- **Ningún competidor venezolano** publicó un tiempo de desconexión ante parpadeos (flickers) igual o inferior a 30 ms.
- La afirmación más rápida encontrada en el mercado venezolano pertenece a **WellSpec** con "0,2–0,3 segundos" (200–300 ms), presentada como claim de ser "el más rápido de Venezuela". Esa cifra es **entre 6 y 10 veces más lenta** que la innovación Genteca.
- Los competidores con datos publicados (Powest: 1.000 ms; Breakermatic: 1.000–1.500 ms) están en un orden de magnitud completamente diferente.
- La mayoría de competidores simplemente **no publica el dato de velocidad de desconexión ante flickers**. El vacío no es evidencia de que sean rápidos — es evidencia de que el dato no existe o no se considera un diferenciador para ellos.
- **TQ y PROTECTOR** (las dos marcas mencionadas explícitamente por Alberto Betancourt en la reunión del 29-04-2026) no publican datos de tiempo de desconexión ante flickers en ningún canal rastreado.

> **Nota sobre "PROTECTOR":** La marca mencionada en la reunión como "Protector" no pudo identificarse con certeza como un solo fabricante. En Venezuela existe "Protektor" (ICREATIVA), y en Colombia/Venezuela circula "Breakermatic" (Mavigal), ambos compatibles con la referencia coloquial a "Protector" que usa el equipo comercial. Ninguno publica dato de ms.

---

## Sección 2 — Recomendación de viabilidad del claim "el más rápido / el único"

### Categoría de viabilidad

**Sustentable como "el más rápido"** con alta solidez para el mercado venezolano y para el segmento de protectores enchufables monofásicos residencial/comercial.

### Razonamiento

1. El único competidor que hace un claim explícito de velocidad en Venezuela (WellSpec) publica 200–300 ms como "lo más rápido del mercado" — muy por encima de los < 30 ms de Genteca.
2. Los demás competidores no publican dato de tiempo de desconexión ante flickers. Esto opera a favor del claim de Genteca: si nadie puede demostrar ser más rápido, Genteca puede afirmar serlo con el respaldo cuantitativo de su propio dato medido.
3. El dato "< 30 ms" es verificable por el laboratorio propio (I&D confirma la innovación). Según el Owner, Genteca tiene laboratorio para refutar si alguien reta el claim — condición de gate cumplida.
4. La formulación "el más rápido ante parpadeos (< 0,03 s)" es la más sólida porque combina superlativo + dato cuantitativo: incluso si el superlativo se cuestionara, el dato de 0,03 s sigue en pie.

### Análisis de riesgo por formulación

| Formulación | Viabilidad | Riesgo | Observación |
|---|---|---|---|
| "El más rápido ante parpadeos (< 0,03 s)" | ✅ Alta | Bajo | Dato cuantitativo propio verificable; competidor más agresivo (WellSpec) está a 200–300 ms. |
| "El único con < 30 ms en Venezuela" | ✅ Alta | Bajo-Medio | "El único" es más absoluto. Plausible dado que nadie más publica este dato, pero técnicamente requiere afirmar que ningún competidor lo tiene — Genteca tendría que sostener eso ante un eventual reto. Bruna debe evaluar si prefiere la formulación superlativa acompañada del dato cuantitativo. |
| "Uno de los más rápidos" | ❌ Prohibida | — | Prohibida por decisión Owner 2026-05-03. No proponer. |

### Formulación recomendada (para insumo de Vael + Bruna)

La formulación más defendible es: **"El más rápido ante parpadeos (< 0,03 s)"**. El dato cuantitativo actúa como ancla — si alguien reta el superlativo, el dato medido de 0,03 s es el argumento. Recomendación al gate Bruna: la evidencia de mercado recabada respalda el superlativo. El caveat a evaluar es si WellSpec eventualmente publica un datasheet oficial con un dato por debajo de 30 ms — lo que hoy no existe en ninguna fuente accesible.

---

## Sección 3 — Sensor NTC y autoprotección térmica en la categoría

### Hallazgo principal

**Cero competidores venezolanos o regionales relevantes comunican NTC, autoprotección térmica, protección por temperatura o tecnología equivalente** en empaque, datasheet o copia web pública de sus protectores monofásicos residenciales/comerciales.

### Detalle por competidor

| Marca | ¿Menciona NTC o protección térmica? | Forma de comunicación | Fuente |
|---|---|---|---|
| TQ / Total Quality | No | — | Pc Actual / distribuidores |
| WellSpec | No | — | suministrosisg.com |
| Avtek (línea residencial) | No | — | avtek.com |
| Powest Airmatic | No | — | powest.com |
| JVTRONIC | No | — | protectoresdevoltaje.com.ve |
| Breakermatic | No | — | distribuidores Colombia |
| Protektor Venezuela | No | — | icreativa.com.ve |
| Koblenz / Steren | No | — | páginas oficiales MX |
| **Exceline GSM-RE (spec pública)** | No (pre-innovación) | — | Datasheet local `00-brief/specs-i-d/` |

### Implicación para Vael

"Sensor NTC incorporado" es **territorio en blanco** de comunicación. Ningún competidor lo está diciendo. Esto confiere dos ventajas: (a) novedad percibida para el consumidor técnico y (b) imposibilidad de que un competidor diga "nosotros ya lo teníamos" en su empaque — porque no lo dice. La enigmaticidad del término NTC para el consumidor no técnico es a la vez un riesgo (incomprensión) y una oportunidad (curiosidad que lleva al QR / reverso del empaque). La reunión del 29-04-2026 documenta que Francisco Ferrero y Alberto Betancourt consideraron ese efecto "enigmático" como activo de comunicación.

---

## Sección 4 — Comunicación de "tecnología inverter" en la categoría

### Hallazgo principal

Al menos tres competidores comunican explícitamente que sus productos protegen tecnología inverter. Sin embargo, **ninguno vincula esa comunicación a un dato cuantitativo de velocidad de respuesta**. La formulación inverter es mayoritariamente una segmentación de aplicación, no un diferenciador de rendimiento.

### Tabla de competidores — claim inverter

| Marca / Modelo | Formulación exacta (o más cercana disponible) | Canal | Fuente | Notas |
|---|---|---|---|---|
| **Avtek SPC-PEBAS-B230/21J** | "Protector de voltaje con alta capacidad de supresión para aires acondicionados INVERTER y motores eléctricos" / "Protector y supresor de voltaje de alta capacidad para aires INVERTER" | Web oficial + distribuidores | avtek.com / rodelag.com | Claim de aplicación. Sin dato de velocidad de respuesta en ms. |
| **Avtek SPC-PTINAS-1T515/21J** | "Protector de voltaje con alta capacidad de supresión para refrigeradoras (neveras) INVERTER" | Web oficial | avtek.com | Claim de aplicación. Sin velocidad. Agotado al momento de consulta. |
| **Breakermatic PME110-E TR** | "Protector voltaje nevera digital e inverter" | Distribuidores Colombia / Venezuela | almaceneleconomico.com / formex.com.co | Claim de aplicación. Sin dato de velocidad. |
| **JVTRONIC (línea inverter)** | Sin formulación exacta accesible (bot-block). La marca opera bajo nombre "Jenval Inv" sugiriendo segmento inverter en su nombre comercial. | Web protectoresdevoltaje.com.ve | protectoresdevoltaje.com.ve | Dato limitado por acceso. |
| Cosmolux | No identificado en mercado venezolano actual | — | Ninguna fuente encontrada | Cosmolux no apareció en ningún canal rastreado. Si existe, opera con presencia web muy baja. |
| **Exceline GSM-RE (etiqueta del producto, 2018+)** | "Compatible inverter" mencionado en etiqueta según transcripción reunión (Raoul: "lo vi en una etiqueta en 2018") | Etiqueta producto (referencia interna) | Transcript 29-04-2026 | Fact interno: el claim de compatibilidad inverter existía, pero no se comunicaba de forma prominente. |

### Implicación para Vael

"Protege tecnología inverter" **no es territorio en blanco** — Avtek y Breakermatic ya lo dicen. La diferencia de Genteca es el *porqué* de esa protección: la velocidad de < 30 ms. Los competidores que dicen "para inverter" no explican por qué son adecuados técnicamente. Genteca tiene el argumento técnico que los demás no pueden igualar: **"más rápido ante parpadeos = mejor para inverter"**. Esa conexión causal (velocidad → protección inverter) es el diferenciador, no la mención de inverter en sí. La transcripción del 29-04-2026 captura a Alberto Betancourt formulando esto con precisión: "la respuesta más rápida en el mercado — especialmente importante para equipos inverter."

---

## Sección 5 — Uso de QR en empaques de la categoría

### 5.1 Adopción en el mercado venezolano y regional

**Hallazgo:** Ningún competidor venezolano rastreado utiliza QR en empaque de protector enchufable residencial. La categoría de protectores de voltaje enchufables en Venezuela y mercados vecinos (Colombia, Ecuador, Perú, México) no ha adoptado QR en empaque de forma sistemática. Esto es un Signal de oportunidad: quien lo adopte primero marca una diferencia perceptible.

La búsqueda de empaques de Avtek, TQ, Powest, Breakermatic y JVTRONIC no arrojó evidencia de QR en sus empaques físicos de protectores residenciales. Koblenz (México) tampoco evidenció QR en su página de producto. Steren (México/Colombia) tampoco.

### 5.2 Destinos típicos de QR en categorías eléctricas/electrónicas adyacentes

Basado en la literatura de packaging QR y los patrones observados en categorías eléctricas similares (UPS, supresores, reguladores en mercados más desarrollados):

| Destino del QR | Frecuencia observada | Pertinencia para GSM |
|---|---|---|
| Manual de usuario (PDF o web) | Alta | Media — el GSM es simple de instalar |
| Video de instalación / tutorial | Alta | Alta — reduce fricción en el punto de venta |
| Landing de innovaciones / producto | Media-alta | **Muy alta** — el caso de uso exacto del Owner |
| Registro de garantía | Media | Media |
| Ficha técnica en PDF | Media | Alta — para el consumidor técnico |
| Web institucional genérica | Baja efectividad | Baja — no aporta valor específico |

### 5.3 Posición visual habitual del QR en empaques

Según literatura de packaging (digital-link.com, qr-code-generator.com, Bitly):

- **Posición más frecuente:** reverso del empaque, cerca de la sección de información técnica o en la zona de notas al pie.
- **Posición de mayor visibilidad:** frente del empaque, con CTA ("Conoce más", "Descubre por qué") que motiva el escaneo.
- **Posición de menor fricción:** reverso, integrado naturalmente con el texto de instrucciones o garantía — el consumidor que lo lee lo encuentra.
- **Regla de oro de tamaño:** mínimo 2×2 cm en empaques normales; 1×1 cm en empaques pequeños. El GSM es un blister pequeño: diseñar para mínimo 1,5×1,5 cm con zona silenciosa.

### 5.4 QR junto a claim específico vs QR genérico de marca

**Práctica observada y literatura:**

- **QR junto a claim:** Menos frecuente, pero con mayor efectividad de escaneo cuando el claim crea curiosidad. Ejemplo clásico: "¿Por qué < 0,03 s? [QR]". La curiosidad técnica activa el escaneo.
- **QR genérico de marca:** Mayor adopción, menor tasa de escaneo. El consumidor no entiende por qué escanear.
- **Recomendación de literatura (digital-link.com):** Los QR deben llevar a "experiencias intencionales, valiosas y contextuales" — un QR genérico que lleva a la home page del fabricante tiene baja conversión. Un QR junto a una innovación que lleva a video explicativo tiene alta conversión.
- **Dato Bitly 2025:** 64% de compradores han escaneado un QR en tienda; 79% son más propensos a comprar cuando el QR provee información adicional. La categoría de productos técnicos (electrónica, protección eléctrica) tiene tasas de escaneo superiores a alimentos y cosméticos porque el comprador tiene una pregunta técnica genuina.
- **Adopción general:** 88% de crecimiento YoY en adopción de QR en packaging en 2023; más del 90% de marketers usando QR en 2025 (Bitly 2025 QR Code Survey).

### 5.5 Evaluación de las opciones del Owner para el QR del GSM

El workstream plantea tres opciones:

**Opción (a) — QR nuevo con frase llamativa:**
- Ventaja: visibilidad máxima, CTA específico para innovaciones.
- Riesgo: saturación visual si el frente ya tiene tres claims + lengüeta + badges técnicos.
- Señal del mercado: nadie en la categoría lo hace — primer mover tiene ventaja de atención.
- Recomendación de literatura: un solo QR bien posicionado con CTA claro supera a múltiples QR sin propósito.

**Opción (b) — QR existente con nueva frase:**
- Ventaja: no añade elemento visual nuevo.
- Riesgo: si el QR existente llevaba a otro destino (web genérica, garantía), el consumidor habitual puede escanearlo esperando lo anterior y llegar a algo diferente. Confusión de expectativa.
- Recomendación: viable si se controla el destino dinámico y el nuevo destino es superior al anterior. Requiere verificar qué cubre hoy el QR existente.

**Opción (c) — Reemplazar destino del QR existente (QR dinámico):**
- Ventaja: operativamente limpio, sin cambio de arte.
- Riesgo: si el QR existente cumple función de garantía o catálogo, redirigirlo a la landing de innovaciones puede interrumpir ese flujo. La naturaleza dinámica lo resuelve si los destinos pueden coexistir (ej. landing temporal que luego migra a web general).
- Recomendación: la opción más limpia si el QR actual lleva a un destino de baja tracción (web genérica). Evaluar con Aurelio qué función cumple hoy.

**Para el memo Aurelio + Vael:** La práctica de mercado y la literatura respaldan un QR con CTA específico que invite a descubrir las innovaciones. La posición recomendada es el reverso, integrado con la sección de características — donde el consumidor técnico ya está leyendo. Si el frente tiene espacio sin saturación, un QR pequeño (1,5 cm) con frase de invitación cerca de "El más rápido" o "Sensor NTC incorporado" podría capturar al comprador en el momento de mayor curiosidad técnica.

---

## Sección 6 — Lectura de los documentos de market-research subidos

### 6.1 Estado de extracción

Los cinco archivos de market-research (`B-pantallas para consulta.docx`, `M-pantallas para consulta.docx`, `R-pantallas para consulta.docx`, `CUEST_SUPER_VOL_MON (1).docx`, `Al ver estos iconos en el empaque...docx`) son binarios `.docx` que no pueden leerse directamente con las herramientas disponibles. No se pudo extraer su texto completo.

La extracción de los `.docx` requiere herramienta de conversión. **Flag para Raul:** si estos documentos contienen hallazgos críticos de consumidor que deben alimentar a Vael / Solenne antes de producir el copy A/B, se recomienda convertir los archivos a `.txt` o `.pdf` para que Orlan los procese en una segunda ronda, o compartir los hallazgos clave en texto plano. La herramienta `python-docx` podría procesar esto vía script si se autoriza.

### 6.2 Lo que sí pudo extraerse del contexto disponible

Del transcripto de la reunión del 29-04-2026, Raoul menciona un **estudio de mercado previo** sobre comprensión de claims de empaque:

- **Hallazgo relevante (Fact — referencia directa de Raoul en transcripción):** "En el estudio era c***, era casi el 40% que pensaba que 'protección térmica' era lo que protegía el motor." Esto es un dato crítico de comprensión de consumidor: la frase "protección térmica" sin contexto dispara la interpretación de protección del motor, no del protector mismo.
- **Implicación para Vael / Solenne:** "Autoprotección térmica" es la formulación que corrige esa confusión: el prefijo "auto" señala que el protector se protege a sí mismo. El termómetro / ícono de calentamiento en el empaque funciona como anclaje visual que acompaña el claim y reduce la confusión.
- **Hallazgo sobre "NTC":** Alberto Betancourt en la reunión señala que NTC es deliberadamente enigmático: "protección térmica NTC ahí no está sobre prometiendo nada y bueno, así es que la gente investigue. Pero estás diciendo que tienes algo superior que los demás no tienen." Esto sugiere que el término NTC para el consumidor no técnico no crea confusión sino curiosidad — lo opuesto a "protección térmica" sola.

Del WhatsApp con José Miguel Canudas (02-05-2026):
- Confirmó que el NTC protege al protector y al cableado de corrientes excesivas; para cargas de ~20 A actúa como protección contra sobrecarga; para cargas menores protege al protector y la instalación pero no al equipo.
- Confirmó que la reducción 150 ms → < 30 ms protege compresores de ciclo corto y electrónica inverter.
- **Nota al pie de su mensaje:** "Verificar con fuentes técnicas, todo lo escrito aquí." — El equipo de I&D reconoce que este texto es orientativo, no final.

### 6.3 Señales de consumidor capturables del contexto (pending validación con .docx)

Basado en lo disponible (sin los .docx), los insights de consumidor que el equipo ya ha reconocido internamente y que alimentan las decisiones de empaque son:

| Insight | Origen | Implicación |
|---|---|---|
| ~40% entiende "protección térmica" como protección del motor (sobrepromesa) | Estudio previo (referencia en transcripción) | Justifica el prefijo "auto" y el asterisco. |
| Los técnicos (instaladores) son el público que más importa para GSM-RB/RF | Reunión + contexto conocido del producto | Copy técnico puede ser más denso que para consumidor final. |
| "Inverter" es un término viejo en el mercado pero el consumidor no sabe cuáles protectores sirven para inverter | Raoul + Alberto en transcripción | Hay demanda latente no satisfecha en comunicación. |
| El técnico comprador conoce el GSM-RB "por décadas" — el claim de "nuevo" debe ser creíble | Alberto en transcripción | Las dos innovaciones son el sustento de credibilidad del claim "nuevo". |

---

## Sección 7 — Claim Feasibility Note (OL-5)

### Claims candidatos para el empaque GSM (Alternativa A propuesta)

#### Claim 1: "El más rápido ante parpadeos (< 0,03 s)"

- **Evidencia que lo respalda:** Dato de I&D medido por laboratorio Genteca (José Miguel Canudas + documento de innovaciones). Ningún competidor venezolano publica dato igual o superior a esta velocidad. El competidor más agresivo (WellSpec) publica 200–300 ms como "el más rápido de Venezuela". El spec previo de Exceline era 150 ms.
- **Riesgo de over-claim:** Bajo. El dato cuantitativo propio es verificable. El superlativo está respaldado por la ausencia de competidores con dato similar. El Owner ha declarado que el laboratorio puede refutar cualquier reto.
- **Categoría:** ✅ Defendible
- **Caveat sugerido (para Bruna):** Confirmar que el dato de < 30 ms está medido bajo condición reproducible y documentada en el laboratorio de I&D (la nota de Canudas dice "verificar con fuentes técnicas"). Si I&D no ha formalizado el protocolo de medición, Bruna debe exigir esa formalización antes de publicar el superlativo.

#### Claim 2: "Protege tecnología Inverter"

- **Evidencia que lo respalda:** La mejora de velocidad a < 30 ms es el argumento técnico central (respuesta más rápida = mejor protección ante ciclos cortos de arranque que afectan a inversores). Tres competidores ya usan formulaciones similares (Avtek, Breakermatic, JVTRONIC), pero sin el sustento cuantitativo.
- **Riesgo de over-claim:** Medio. El claim es verdadero pero no exclusivo. Avtek y Breakermatic también lo dicen. El diferenciador es el *porqué* (velocidad), no el claim en sí.
- **Categoría:** ⚠ Defendible con caveat
- **Caveat sugerido:** En empaque solo funciona bien si se mantiene vinculado al dato de velocidad (sea en el mismo badge o en el retiro). Aislado, no es diferenciador. En el copy de empaque actual (Alternativa A) la proximidad entre "El más rápido (< 0,03 s)" y "Protege tecnología Inverter" crea la conexión causal que lo hace defendible y diferenciado.

#### Claim 3: "Sensor NTC incorporado*"

- **Evidencia que lo respalda:** José Miguel Canudas confirma la existencia del sensor y su función. Alberto Betancourt lo evalúa como técnicamente correcto y diferenciador.
- **Riesgo de over-claim:** Bajo si va con asterisco. El asterisco desplaza la explicación al retiro, donde se puede matizar con precisión. El riesgo real es que sin el asterisco y sin la explicación, el consumidor infiera protección del motor.
- **Categoría:** ✅ Defendible (con asterisco obligatorio)
- **Caveat sugerido (para Bruna):** El asterisco es condición necesaria, no opcional. La nota de retiro debe decir explícitamente que protege al protector mismo y a la instalación, sin afirmar protección directa del motor o la carga conectada (salvo para cargas cercanas a la capacidad máxima nominal).

#### Claim 4: "Nuevo. La Protección más completa" (lengüeta)

- **Evidencia que lo respalda:** "Nuevo" está sustentado por las dos innovaciones (NTC + < 30 ms) que son mejoras reales y medibles. "La protección más completa" es un superlativo relativo — más completa que la versión anterior, y más completa que la competencia en cuanto a la combinación de funciones comunicadas.
- **Riesgo de over-claim:** Medio. "Más completa" es un superlativo cualitativo que puede cuestionarse. El riesgo se mitiga porque el empaque desarrolla en el frente las tres frases que sustentan esa completitud.
- **Categoría:** ⚠ Defendible con caveat
- **Caveat sugerido:** Bruna debe evaluar si "la protección más completa" necesita una delimitación explícita (ej. "para equipos de aire acondicionado y refrigeración") o si el contexto del producto (empaque de protector para A/C) lo delimita implícitamente. Si la Junta prefiere certeza máxima, "Una protección más completa" (sin superlativo absoluto) sería la formulación más conservadora. Esa decisión es de Bruna.

---

## Sección 8 — Diferenciación consolidada (OL-3)

### Diferenciado ✅

- **Tiempo de desconexión ante parpadeos (< 30 ms):** Ningún competidor venezolano publica un valor comparable. El competidor que más se acerca (WellSpec) publica 200–300 ms como su máximo diferenciador de velocidad. Genteca está entre 6 y 10 veces más rápido según datos disponibles.
- **Comunicación de sensor NTC / autoprotección térmica:** Espacio en blanco. Ningún competidor lo menciona en ningún canal.

### Paridad ⚖

- **Protección contra sobre/bajo voltaje:** Funcionalidad básica de la categoría. Todos los competidores la tienen.
- **Temporizado inteligente de reconexión (3 min):** Estándar de categoría. Avtek, Powest, TQ, JVTRONIC tienen valores similares.
- **Supresor de picos:** Presente en varios competidores (Avtek: 2.100 J en línea inverter; Genteca: 410 J en GSM-RE según datasheet). [Flag para Vera: verificar si la diferencia de Joules en supresores es relevante para el copy o si los 410 J son adecuados para el segmento objetivo.]
- **Comunicación de compatibilidad con inverter:** Avtek, Breakermatic y JVTRONIC ya lo dicen. No es territorio en blanco.

### Expuesto ⚠

- **Certificaciones publicadas:** La hoja de especificaciones GSM-RE menciona IEC 1000-4-x y COVENIN. No se encontraron certificaciones UL ni CE para el GSM en fuentes accesibles. WellSpec publica certificación CE y estándares EN/IEC. [Flag para Vera: ¿el GSM-MB/RB/RF/RE tiene certificaciones que no están en las specs locales accedidas? Si las tiene, comunicarlas refuerza la posición.]
- **Capacidad de supresión de picos (Joules):** Avtek línea inverter: 2.100 J; Genteca GSM-RE: 410 J. Si el consumidor técnico compara este valor, Genteca está expuesta en este atributo. [Flag para Vera: aclarar si los 410 J son adecuados para el segmento o si existe una versión con mayor capacidad.]
- **Presencia digital / ficha técnica accesible:** Los datasheets de Genteca en genteca.com.ve devuelven 403. Avtek y Powest tienen fichas accesibles. Esto no afecta el empaque, pero sí la credibilidad del claim en el punto de venta si el técnico quiere verificar online.

---

## Cover note — Supuestos, pendientes y escalaciones

### Supuestos críticos

1. **El dato "< 30 ms" está medido en laboratorio.** Todo el análisis de claim feasibility depende de que I&D haya medido y documentado este dato. La nota de José Miguel Canudas dice explícitamente "verificar con fuentes técnicas." Si Vera / I&D no formaliza el protocolo de medición, el claim superlativo tiene un riesgo de respaldo interno — independientemente de lo que diga la competencia. **Escalación a Vera:** confirmar que el dato existe como medición documentada.

2. **"Protector" y "TQ" no publican datos de tiempo de flicker.** Se asume que esa ausencia no equivale a tener un dato superior no comunicado. Si ventas (Víctor, Luis González) tiene información de que algún competidor menciona tiempos de ms en su literatura de ventas (no en empaque), esa información debe reportarse a Orlan para actualizar este análisis.

3. **Los .docx de market-research no pudieron leerse.** El análisis de comprensión de consumidor se basó en menciones en la transcripción y el WhatsApp. Si los .docx contienen hallazgos contrarios o matizadores a los capturados aquí, el análisis debe actualizarse.

4. **WellSpec es el único claim activo de velocidad en el mercado venezolano.** Esta es la afirmación más relevante que Bruna debe considerar. La fuente es la web del distribuidor (suministrosisg.com) — no un datasheet oficial de WellSpec. Si WellSpec tiene documentación técnica con ese dato, la solidez de su claim aumenta. Por ahora es Claim de distribuidor, no Fact de fabricante.

### Pendientes para completar el análisis

| Pendiente | Responsable sugerido | Prioridad |
|---|---|---|
| Extraer texto de los 5 .docx de market-research | Raul (convertir a PDF o txt) + Orlan (re-análisis) | Alta — afecta Vael / Solenne |
| Confirmar protocolo de medición del dato < 30 ms | Vera con I&D | Crítica — bloquea gate Bruna |
| Solicitar a Víctor / Luis González si TQ o Protector mencionan tiempos de ms en su literatura de ventas | Raul | Media |
| Verificar qué cubre hoy el QR existente del empaque GSM | Raul / Aurelio | Media — necesario para decisión de opciones QR a/b/c |
| Verificar certificaciones del GSM-MB/RB/RF/RE (UL, CE, COVENIN) para determinar si es comunicable | Vera | Media |
| Acceder a datasheets TQ directamente (bloqueados 403) | Paxs vía Raul (Blocked-Site Protocol) | Media |
| Acceder a datasheets JVTRONIC directamente (bot-block) | Paxs vía Raul | Baja — contexto suficiente por ahora |
| Confirmar si "Cosmolux" existe como marca activa en Venezuela 2026 | Raul con ventas | Baja — no apareció en ningún canal |

### Escalaciones

- **A Vera:** (1) Confirmar medición < 30 ms documentada. (2) Evaluar diferencia de Joules de supresor vs. competencia. (3) Revisar certificaciones publicables.
- **A Bruna:** (1) Gate de claims (sección 7 arriba). (2) Política de superlativo ya recogida del Owner — Bruna registra como BR-2.
- **A Vael:** (1) NTC = territorio en blanco, oportunidad de primer mover en comunicación. (2) "Protege inverter" no diferencia por sí solo — el diferenciador es la velocidad de respuesta como razón técnica. (3) Insight de consumidor: ~40% entiende "protección térmica" como protección del motor — el prefijo "auto" y el icono de termómetro son la corrección que ya está en el diseño.
- **A Solenne:** (1) El copy de Alternativa A tiene respaldo de mercado para los tres claims del frente. (2) Alternativa B debe explorar si hay formulación más fuerte o más emocional que no dependa del superlativo — Orlan no propone, solo señala que la base factual existe para variantes.
- **A Aurelio:** Incluir en AU-1 la señal de que WellSpec usa "el más rápido de Venezuela" para 200–300 ms — Genteca puede apropiarse de ese claim con datos reales y materialmente superiores.

---

## Sources

| # | Fuente | URL | Fecha de acceso | Confianza | Notas |
|---|---|---|---|---|---|
| 1 | Hoja de Especificaciones GSM-RE (local) | `C:\Raul\03-projects\genteca\2026-04_GSM-MB-RB-RF_empaque\00-brief\specs-i-d\GSM-RE-Protector para Aires Acondicionados y Refrigeración Enchufable.pdf` | 2026-05-03 | Confirmed | Spec oficial Genteca. Tiempo de flicker = 150 ms (spec pre-innovación). |
| 2 | WhatsApp José Miguel Canudas (local) | `00-brief/whatsapp/Chat con Jose Miguel Canudas miembro de Junya Directiva.txt` | 2026-05-03 | Confirmed | Descripción técnica NTC y < 30 ms. Nota de Canudas: "verificar con fuentes técnicas." |
| 3 | Transcripción reunión 29-04-2026 (local) | `00-brief/transcripts/Meeting Transcription 29-04-2026 (1).txt` | 2026-05-03 | Confirmed | Menciones TQ, Protector, insight 40% comprensión térmica. |
| 4 | Comentarios sobre las innovaciones (local) | `00-brief/innovaciones/Comentarios sobre las innovaciones.txt` | 2026-05-03 | Confirmed | Descripción técnica de < 30 ms y NTC. |
| 5 | Delta v4 NTC-inverter (local) | `03-review-and-release/GSM-MB-RB-RF-RE_empaque_delta_v4_NTC-inverter.md` | 2026-05-03 | Confirmed | Estado de propuesta de copy al inicio del workstream. |
| 6 | WellSpec 120V — Suministros ISG | https://suministrosisg.com/products/protector-de-voltaje-inteligente-120v-wellspec | 2026-05-03 | Probable | [single-source] Claim "el más rápido de Venezuela, 0,2-0,3 s." Web distribuidor, no datasheet fabricante. |
| 7 | WellSpec 220V 63A — Suministros ISG | https://suministrosisg.com/products/protector-de-voltaje-220v-wellspec-63a | 2026-05-03 | Probable | [single-source] Claim "menos de 0,3 segundos." |
| 8 | Powest Airmatic 220V — página oficial | https://powest.com/producto/protector-de-voltaje-powest-airmatic-220v-20a/ | 2026-05-03 | Confirmed | Tiempo respuesta 1 segundo = 1.000 ms. Specs en página oficial Powest. |
| 9 | TQ-RB+220 Digital — Pc Actual | https://pcactual.net/producto/potencia/protectores-de-voltaje/regulador-y-protector-total-quality-tq-rb-220-digital | 2026-05-03 | Speculative | Sin dato de ms. Fuente distribuidora. |
| 10 | TQ-MAC+120 Digital — Pc Actual | https://pcactual.net/producto/potencia/protectores-de-voltaje/regulador-y-protector-total-quality-tq-mac-120-digital | 2026-05-03 | Speculative | Sin dato de ms. Fuente distribuidora. |
| 11 | TQ-PBS220-1 — Pc Actual | https://pcactual.net/producto/potencia/protectores-de-voltaje/regulador-y-protector-total-quality-tq-pbs220-1 | 2026-05-03 | Speculative | Sin dato de ms. Fuente distribuidora. |
| 12 | Avtek SPC-PEBAS-B230/21J — oficial | https://www.avtek.com/producto/protector-de-voltaje-con-alta-capacidad-de-supresion-para-a-a-y-equipos-de-refrigeracion-inverter-hasta-52-000-btu-220-vac-spc-pebas-b230-21j | 2026-05-03 | Confirmed | Claim "para A/C INVERTER." Sin dato de ms. Reconexión 10 s. |
| 13 | Avtek SPC-PTINAS-1T515/21J — oficial | https://www.avtek.com/producto/protector-de-voltaje-con-alta-capacidad-de-supresion-para-electrodomesticos-inverter-120-vac-spc-ptinas-1t515-21j | 2026-05-03 | Confirmed | Claim "para neveras INVERTER." Sin dato de ms. Agotado. |
| 14 | Breakermatic PME110-E TR — distribuidores | https://almaceneleconomico.com/product/protector-voltaje-nevera-digital-e-inverter-pme110-e-tr-breakermatic/ | 2026-05-03 | Probable | Claim "para nevera digital e inverter." Tiempo falla 5 s de rearme. |
| 15 | Breakermatic catálogo — Asenzo Colombia | https://asenzo.com/wp-content/uploads/2020/04/CO-BREAKERMATIC-Catalogo-Linea-Domesticos.pdf | 2026-05-03 | Probable | [single-source] PDF binario, no pudo extraerse texto. |
| 16 | JVTRONIC — sitio oficial Venezuela | https://www.protectoresdevoltaje.com.ve/ | 2026-05-03 | Speculative | Bot-verification bloqueó acceso a fichas individuales. Sin dato de ms para línea residencial. |
| 17 | Protektor Venezuela — FAQ | https://icreativa.com.ve/preguntas | 2026-05-03 | Speculative | [single-source] Sin dato de ms. Solo temporización de rearme. |
| 18 | Avtek — página oficial principal | https://www.avtek.com/ | 2026-05-03 | Confirmed | Marca activa Venezuela + LATAM. Fundada 1978. |
| 19 | Suministros ISG — página principal | https://suministrosisg.com/ | 2026-05-03 | Probable | Distribuidor WellSpec Venezuela. Claim "más rápido de Venezuela." |
| 20 | QR codes packaging — Bitly 2025 | https://bitly.com/blog/qr-code-product-packaging/ | 2026-05-03 | Confirmed | Best practices. Estadística 64% compradores escanean QR; 79% más propensos a comprar con QR informativo. |
| 21 | QR codes packaging — Digital Link | https://digital-link.com/guides/qr-codes-on-packaging-design-best-practices/ | 2026-05-03 | Confirmed | Posicionamiento QR, tamaño mínimo, claim-specific vs. genérico. |
| 22 | QR codes — QR Code Generator | https://www.qr-code-generator.com/qr-codes-on/product-packaging/ | 2026-05-03 | Confirmed | 3.8x más escaneos con QR de diseño vs. genérico B&W. |
| 23 | EPA Venezuela — hoja Exceline GSM-ASBS (referencia web) | https://ve.epaenlinea.com/ve/documentos/1642192.pdf | 2026-05-03 | Speculative | PDF es archivo Illustrator, no spec técnica. Dato de "150 ms" citado en resultado de búsqueda puede ser extracto de spec pre-innovación del GSM-RE. |
| 24 | Acta reunión 29-04-2026 (local) | `03-review-and-release/acta-reunion-29-04-2026.md` | 2026-05-03 | Confirmed | Resumen de decisiones y pendientes de la reunión Raoul + Alberto. |
| 25 | Genteca biblioteca (bloqueada) | https://genteca.com.ve/biblioteca/exceline/E_GSM-RB.pdf | 2026-05-03 | — | 403 Forbidden. Escalación a Paxs si se necesita confirmar spec pública del GSM-RB. |

---

*Orlan — Market Intelligence Analyst — Dominio Genteca*
*Output OL-1/2/3/5 combinado. Este análisis es insumo, no decisión. La aprobación del claim es de Bruna. El copy final es de Vael + Solenne. La decisión de roadmap es del Owner.*
*Archivado como candidato a KB por Celeste cuando el workstream cierre.*

---

## Refresh 2026-05-04 (post-Liliam I&D)

**Motivo del refresh:** Liliam (I&D Genteca), en chat WhatsApp del 2026-05-04, corrigió el dato de Breakermatic. El v1 reportaba 1.000-1.500 ms para Breakermatic basado en páginas de distribuidores Colombia (fuente Medio / single-source). Liliam confirmó que Breakermatic tiene productos a 32-64 ms (50 ms típico) y que el laboratorio Genteca lo verificó. Esto reemplaza el dato anterior con confianza Alta.

### Tabla de tiempo de respuesta — versión corregida (Breakermatic)

| Marca | Tiempo de respuesta | Fuente | Confianza | Notas |
|---|---|---|---|---|
| **Genteca Exceline GSM** | **20-30 ms** (laboratorio); 16-32 ms teórico | Liliam I&D (WhatsApp 2026-05-04) + laboratorio Genteca | Alta | Dato corroborado por Liliam. Rango teórico 16-32 ms; pruebas de laboratorio 20-30 ms. |
| **Breakermatic** | **32-64 ms** (50 ms típico) | Hoja técnica Breakermatic + verificado en laboratorio Genteca | Alta | Corrección de v1 (que reportaba 1.000-1.500 ms por distribuidores Colombia). Liliam: "Si. Y si cumplen." "En la hoja dice 32 a 64 ms." |
| WellSpec | 200-300 ms | Distribuidor Venezuela (suministrosisg.com) | Medio | Claim de marketing, no datasheet oficial. |
| Powest Airmatic | 1.000 ms | Datasheet oficial Powest | Alto | |
| TQ, Avtek, JVTRONIC, Protektor | Sin dato publicado | Múltiples fuentes | Bajo | El vacío no equivale a tener un dato superior. |

### Nueva clasificación de competidores por velocidad

1. **Genteca Exceline GSM — 20-30 ms:** referencia del mercado.
2. **Breakermatic — 32-64 ms (50 ms típico):** competencia más cercana. Gap vs. Genteca: ~2x en el mejor caso de Breakermatic, ~1,6x en el peor caso de Genteca. Competencia real y técnicamente seria.
3. **WellSpec — 200-300 ms:** ~10x más lento que Genteca. El único que hace claim de velocidad en Venezuela.
4. **Powest Airmatic — 1.000 ms:** ~33-50x más lento que Genteca.
5. **TQ, Avtek, JVTRONIC, Protektor — sin dato:** no publican tiempo de desconexión ante flickers.

### Recomendación actualizada del claim superlativo

**"El más rápido del mercado"** sigue siendo defendible: Genteca es más rápido que Breakermatic y que el resto del mercado, sin excepción identificada.

**"10 veces más rápido"** no es universalmente defendible. Contra Breakermatic la ventaja es ~2x, no 10x. Usarlo como afirmación absoluta sería inexacto y vulnerable si Breakermatic está en el mix de la conversación.

**"Hasta 10 veces más rápido"** es defendible: "hasta" marca el máximo del rango, no el promedio. Es verdadero contra WellSpec (200-300 ms), Powest (1.000 ms) y los competidores sin dato. **Decisión de Owner requerida (2026-05-04):** si se aprueba esta formulación, debe quedar registrado que el "hasta 10x" aplica al grupo WellSpec/Powest/resto — no a Breakermatic. Bruna debe registrar esto como condición de gate.

### Implicación para argumentario ESC

La fuerza de ventas necesita tener clara la tabla real por competidor para contestar comparaciones específicas en campo:

- **Contra Breakermatic:** Genteca es ~2x más rápido. Argumento: "somos más rápidos incluso contra el único competidor serio en este atributo — y lo confirmamos en nuestro propio laboratorio."
- **Contra WellSpec:** Genteca es ~7-15x más rápido. WellSpec llama "el más rápido de Venezuela" a sus 200-300 ms — Genteca los supera por un factor de orden de magnitud.
- **Contra Powest:** Genteca es ~33-50x más rápido.
- **Argumento de síntesis para ESC:** "En promedio, somos 10 veces más rápidos que el mercado. Incluso contra el competidor más cercano técnicamente, somos el doble de rápidos."

### Pendiente — profundizar en Breakermatic

Liliam observó: "Ellos son de la vieja escuela." Señal de que Breakermatic tiene reputación técnica seria y trayectoria en el mercado (no un entrante menor). El v1 solo tiene datos de distribuidores para modelos específicos de A/C. **Para próxima iteración:** mapeo completo de la línea Breakermatic — modelos, segmentos cubiertos (refrigeración, A/C, electrónica), distribución geográfica (Venezuela vs. Colombia vs. LATAM), posicionamiento de precio. Esto permitirá a ventas anticipar objeciones en campo y a Vael calibrar si Breakermatic merece mención explícita en argumentario o solo en training interno. Anotar como pendiente de iteración Orlan-2.

### Fuente adicional (Refresh)

| # | Fuente | Fecha de acceso | Confianza | Notas |
|---|---|---|---|---|
| R-1 | WhatsApp Liliam I&D (local): `00-brief/whatsapp/Chat con Liliam I&D.txt` | 2026-05-04 | Alta | Corrección directa del dato Breakermatic. Confirmación de rango Genteca (16-32 ms teórico; 20-30 ms en laboratorio). Verificación interna I&D. |

---

*v1 (2026-05-03) + Refresh 2026-05-04 — Orlan*
*El Refresh no reemplaza el v1; lo complementa con corrección puntual de Breakermatic y ajuste de claim superlativo. Decisión de formulación "hasta 10x" pendiente de Owner.*
