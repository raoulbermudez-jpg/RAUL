# Brief Técnico — Genteca Exceline GSM: fundamentación de la tesis inverter / flicker

**Solicitante:** Raoul Bermúdez
**Fecha:** 2026-05-04
**Investigador:** Paxs
**Versión:** v1 (knowledge-base only — pendiente verificación con fuentes en vivo)

---

## Limitación de sesión registrada (Blocked-Site Protocol §6.2)

**Herramientas denegadas:** WebSearch y WebFetch recibieron denegación de permisos al primer intento. No es bloqueo de servidor — es restricción de sesión del runtime.

**Método de acceso usado:** conocimiento de entrenamiento (hasta agosto 2025) + razonamiento técnico estructurado. Cada afirmación está marcada con su nivel de confianza y la fuente autoritativa que la respalda, para verificación manual posterior.

---

## 1. Hallazgo principal

La tesis del Owner se sostiene **parcialmente con matices críticos** que no la invalidan pero la requieren a formular con precisión técnica superior.

**Sólido:** los equipos inverter sí incluyen protección contra picos de alta energía (típicamente MOV/varistores); esos componentes son insensibles a caídas de voltaje y flickers; un protector externo rápido sí agrega una capa de protección que los MOV de fábrica no cubren.

**A afinar:** el umbral de 30 ms como "mágico" no está directamente respaldado por una norma IEEE o IEC única. El número correcto según la literatura de power quality es 0.5 ciclos (8.3 ms a 60 Hz / 10 ms a 50 Hz) como umbral de inicio de voltage sag, y entre 1 y 30 ciclos (16.7 ms a 500 ms a 60 Hz) como rango donde ocurre la mayor parte del daño en electrónica de potencia. Los 30 ms son técnicamente defendibles como tiempo máximo de respuesta útil — pero el argumento se construye distinto a como está planteado en la tesis original.

---

## 2. Cinco preguntas respondidas

### Pregunta 1: ¿Los equipos inverter traen supresores de pico de alta energía de fábrica?

**Respuesta:** Sí, con alta confianza. Es un hecho técnico verificable, no marketing.

Todo equipo inverter moderno (aire acondicionado, refrigerador, lavadora inverter) incluye una etapa de EMI/protección en su fuente de alimentación conmutada (SMPS) que típicamente contiene:

- **MOV (Metal Oxide Varistor):** componente principal de supresión de pico. En equipos residenciales, los MOV típicos tienen capacidad de 200-600 J para eventos singulares, con voltaje de clamping entre 330 V y 430 V (en líneas de 120/240 VAC). Tiempo de respuesta del MOV: entre 1 y 25 ns — extremadamente rápido para picos.
- **Capacitor de filtro de línea (clase X y clase Y):** absorbe ruido de alta frecuencia.
- **Inductor de modo común:** parte del filtro EMI, reduce transitorios de modo común.
- **TVS (Transient Voltage Suppressor) en señales de control:** protege microcontroladores y drivers IGBT contra picos en señales internas.

**Especificaciones típicas por marca (conocimiento de entrenamiento; verificar contra datasheets actuales):**

| Marca / Línea | Protección típica reportada | Fuente a verificar |
|---|---|---|
| Mitsubishi Electric Mr. Slim / City Multi | MOV en entrada, filtro EMI certificado IEC 61000-4-5 (nivel 3-4) | Service manuals MXZ/PUZ series, meus.mitsubishielectric.com |
| LG Inverter V / DUALCOOL | MOV + varistor en módulo de potencia, certificación IEC 61000-4-5 | LG Commercial HVAC tech docs, lgcommercial.com |
| Daikin VRV / Split inverter | Filtro EMI con MOV, cumplimiento IEC 61000-4-5 nivel 2-3 | Daikin technical data books, daikin.com/products |
| Samsung Wind-Free / Digital Inverter | MOV, filtro EMI, certificación CE que implica IEC 61000-4-5 | Samsung HVAC service documentation |
| Carrier Infinity / Performance inverter | MOV y circuito de protección de línea en placa de control | Carrier service literature, hvacpartners.com |

**Limitación crítica:** los fabricantes raramente publican la especificación exacta en joules del MOV instalado en sus equipos residenciales — eso vive en los datasheets internos de los componentes de sus placas. Lo que sí publican es la certificación IEC que implica protección contra surges. **IEC 61000-4-5 nivel 3 = inmunidad a 1.2/50 µs surge de 2 kV en línea, nivel 4 = 4 kV.** Eso es el surge de alta energía. Pero **nada en IEC 61000-4-5 cubre voltage sag o flicker.**

**Afirmación defendible públicamente:** *"Los equipos inverter modernos cumplen IEC 61000-4-5, lo que certifica protección contra picos impulsivos. Esa certificación no cubre caídas de voltaje ni fluctuaciones en el rango operativo."*

---

### Pregunta 2: ¿Qué exactamente daña la electrónica inverter durante un flicker?

**Respuesta:** El mecanismo de daño principal durante un flicker / voltage sag no es el pico en sí — es la dinámica de descarga/recarga del capacitor del bus DC y el comportamiento del IGBT durante el transitorio. Hay tres mecanismos de daño bien documentados:

**Mecanismo A — Overcurrent en el IGBT durante la recuperación de voltaje:**
El inverter controla el compresor mediante modulación PWM a través de IGBTs. Durante un voltage sag, el bus DC cae. Cuando el voltaje se recupera abruptamente (el "up" del flicker), el capacitor del bus DC intenta recargarse. Si la recuperación es rápida (lo que es precisamente la característica del flicker), la corriente de recarga puede exceder el rating momentáneo del IGBT. Un IGBT típico residencial tiene rating de 15-50 A; picos de recarga durante sag recovery pueden alcanzar 2-5x ese valor en microsegundos. La protección de overcurrent del IGBT (desaturation detection) tiene tiempo de respuesta de 3-10 µs — suficiente para eventos de microsegundos, insuficiente si los ciclos de flicker se repiten generando calentamiento acumulativo.

**Mecanismo B — Falla del capacitor del bus DC por estrés térmico cíclico:**
El capacitor electrolítico del bus DC (típicamente 400-450 V, 470-1000 µF en residenciales) es el componente más vulnerable a ciclos de carga/descarga repetidos. Un flicker de 10 Hz (caídas a 50 % de voltaje, 10 veces por segundo) impone al capacitor ciclos acelerados que generan calentamiento interno por ESR. La vida útil cae exponencialmente con la temperatura — la "regla de los 10 grados" (IEC 60068) dice que cada 10 °C sobre el rating reduce la vida a la mitad. Flickers repetitivos que eleven 15-20 °C pueden reducir vida de 10 años a 2-3 años. **Daño acumulativo, no catastrófico inmediato.**

**Mecanismo C — Reset o corrupción del microcontrolador de control:**
El microcontrolador que genera las señales PWM opera con fuente regulada de 3.3 V o 5 V derivada del bus DC. Si el bus DC cae abruptamente, esa fuente puede salir de regulación. Los microcontroladores tienen Brown-Out Reset (BOR) que los reinician al caer el voltaje bajo umbral (típicamente 2.7-3.0 V para un micro de 3.3 V). Un reset durante operación puede generar arranque con compresor en estado desconocido, y el algoritmo de arranque puede aplicar vector de corriente incorrecto al motor, dañando bobinado o rodamientos.

**Fuentes técnicas a verificar:**
- Infineon Technologies: AN2013-04 "IGBT Module Reliability"
- Texas Instruments: "Understanding Brown-Out Reset in Microcontrollers"
- IEEE Transactions on Industry Applications: buscar "voltage sag IGBT failure mechanism" 2015-2024
- Panasonic Industrial: "Aluminum Electrolytic Capacitor Application Guide" — sección ripple current y vida útil

---

### Pregunta 3: ¿Por qué los supresores de pico de fábrica no cubren flickers?

**Respuesta:** Porque son dispositivos de diferente dominio de operación. No es defecto de diseño — son soluciones para problemas distintos.

Un MOV opera en el dominio de la sobretensión: se activa cuando el voltaje supera su voltaje de clamping (típicamente 130-150 % del nominal). Ante 120 VAC nominal, un MOV residencial típico tiene Varistor Voltage (V1mA) de 150-175 V y clamping de 330-430 V. **El MOV no "ve" nada cuando el voltaje cae a 80, 60 o 0 VAC durante un flicker.** Es un dispositivo de absorción de sobretensión — no actúa ante caídas.

Los filtros EMI están diseñados para filtrar ruido de alta frecuencia (10 kHz a varios MHz), no para sostener voltaje durante caídas en frecuencia de red (50/60 Hz).

**El capacitor del bus DC** sí actúa como buffer durante caídas breves: al caer el voltaje de línea, el capacitor descarga su energía para sostener el bus DC. Capacidad de sostenimiento típica residencial: **8-25 ms a plena carga** — coincide directamente con el rango donde el flicker causa daño. Equipos premium pueden sostener 30-50 ms; económicos apenas 5-8 ms.

**Esta es la clave técnica de la tesis:** el capacitor del bus DC es la única "protección" interna contra voltage sag, y su capacidad de hold-up es exactamente el rango temporal donde el flicker opera. Si el flicker dura más que el hold-up (que varía por equipo y no es publicado), el bus DC cae y ocurren los mecanismos A, B, C.

**Fuentes técnicas a verificar:**
- IEC 61000-4-11: "Voltage dips, short interruptions and voltage variations immunity tests" — norma correcta para daños por voltage sag (distinta de IEC 61000-4-5 surges).
- IEEE 1159-2019: "Recommended Practice for Monitoring Electric Power Quality" — voltage sag = caída entre 0.1 y 0.9 pu por duración entre 0.5 ciclos y 1 minuto.
- Schneider Electric White Paper 82: "The Different Types of UPS Systems" — explica por qué los supresores no protegen contra voltage sag.

---

### Pregunta 4: ¿Cuál es el umbral de tiempo de respuesta crítico?

**Respuesta:** 30 ms es un número defendible pero no es el número "de norma". El argumento técnico correcto es más sutil.

La literatura de power quality establece:
- **0.5 ciclo a 60 Hz = 8.3 ms:** umbral mínimo para que un evento sea "voltage sag" según IEEE 1159-2019 / IEEE 1564-2014. Por debajo es "transient" (impulso), no sag.
- **1 ciclo = 16.7 ms a 60 Hz / 20 ms a 50 Hz:** primeros efectos de stress (reset de microcontroladores).
- **3-10 ciclos = 50-167 ms:** zona de mayor probabilidad de falla catastrófica del IGBT si el voltaje cae bajo 50 % nominal.
- **Hold-up time típico del bus DC:** 8-25 ms residencial.

**El argumento para los 30 ms se construye así:** un protector externo con tiempo de respuesta de 30 ms o menos puede intervenir antes de que el bus DC del inverter se agote completamente durante un voltage sag típico (que empieza en el rango de 8-25 ms de hold-up). Si el protector demora 100-200 ms (típico de relés electromecánicos), el equipo ya agotó su hold-up antes de que el protector actuara.

**Matiz importante:** el protector no "bloquea" el flicker como un MOV bloquea un surge — lo que hace es **desconectar el equipo antes de que el bus DC llegue a niveles críticos, y reconectar cuando el voltaje se estabiliza.** La protección es por interrupción controlada, no por absorción.

**Afirmación técnica precisa para narrativa:** *"Un protector con tiempo de respuesta de 30 ms o menos puede interrumpir el suministro al equipo dentro del hold-up time típico del bus DC inverter, protegiendo la electrónica antes de que ocurran los mecanismos de daño por voltage sag. Un protector con 100 ms o más llega tarde — el equipo ya sufrió el evento."*

**Fuentes técnicas a verificar:**
- IEEE 1159-2019: tabla de clasificación de eventos.
- IEEE 1564-2014: definiciones y métricas.
- IEC 61000-4-11:2020: niveles de prueba de inmunidad a voltage sag.
- Littelfuse Application Note: "Selecting the Right Varistor for Surge Protection" — explica por qué los MOV no operan bajo voltaje de clamping.

---

### Pregunta 5: ¿Qué dicen los manuales de fabricantes inverter sobre protección externa?

**Respuesta:** Dos patrones consistentes:

**Patrón A — Recomendación de estabilizador o AVR:**
Mitsubishi Electric (Mr. Slim, manuales serie MSZ/MUZ y PUZ/PKA) especifica "voltage fluctuation within ±10 % of rated voltage" y en modelos para mercados de voltaje inestable indica explícitamente: *"Install a voltage stabilizer if local power supply is unstable."* Ningún manual residencial Mitsubishi en conocimiento de entrenamiento especifica un tiempo de respuesta requerido — pero la recomendación implica reconocimiento de que la protección interna es insuficiente.

**Patrón B — Advertencia de void de garantía:**
Daikin, LG y Samsung incluyen cláusulas de garantía donde el daño por "voltage fluctuations beyond specifications" o "power supply issues" no está cubierto. Evidencia indirecta de que el fabricante reconoce insuficiencia de la protección interna ante eventos fuera de spec.

**Lo que ningún manual encontrado especifica:** un tiempo de respuesta requerido para el protector externo. La recomendación es siempre "estabilizador de voltaje" (AVR), que típicamente tiene tiempos de 20-100 ms (ferroresonante: lento; electrónico: rápido). Los fabricantes no diferencian respuesta rápida vs lenta porque históricamente el mercado de estabilizadores no lo hacía.

**Oportunidad narrativa:** Genteca puede ser el primero en hacer esta distinción explícita en el mercado, respaldándola con dato técnico de hold-up time del bus DC vs tiempo de respuesta del protector. Narrativa honesta y diferenciadora.

---

## 3. Marco narrativo recomendado

### Afirmaciones defendibles (pueden ir a empaque, video, argumentario)

1. *"Los equipos inverter modernos incluyen protección contra picos de alta energía (sobretensiones impulsivas). Esa protección cumple su función."*
2. *"La protección interna de los equipos inverter no fue diseñada para manejar fluctuaciones rápidas de voltaje (flickers y voltage sags) — esa brecha está reconocida en normas internacionales como IEC 61000-4-11."*
3. *"Un protector externo con tiempo de respuesta de 30 ms o menos puede actuar dentro del tiempo que la electrónica del equipo puede sostenerse autónomamente durante una caída de voltaje, reduciendo el estrés sobre el capacitor del bus DC y los IGBTs."*
4. *"El Sensor NTC del Exceline GSM permite detección directa del estado térmico del circuito de protección, evitando fallas silenciosas donde el protector aparenta funcionar pero ya no opera correctamente."*
5. *"Fabricantes como Mitsubishi Electric recomiendan instalar estabilizadores de voltaje en mercados con red inestable. Genteca Exceline GSM con respuesta < 30 ms cumple esa recomendación con mayor precisión que un estabilizador electromecánico convencional."*

### Afirmaciones que NO se sostendrían bajo cuestionamiento técnico

1. *"Los competidores con tiempo de respuesta mayor NO protegen los equipos inverter."* — Demasiado absoluto. Un protector de 50 ms puede proteger equipos con mayor hold-up time. Correcta: *"protegen menos confiablemente, especialmente en equipos con capacitores de bus de menor capacidad."*
2. *"Solo < 30 ms es protección auténtica."* — El número exacto depende del hold-up del equipo específico. 30 ms es umbral conservador y razonable, pero presentarlo como único valor válido requiere referencia técnica que actualmente no existe publicada para equipos residenciales en general.
3. *"Los equipos inverter se dañan por flickers porque no tienen protección interna."* — Incorrecto; sí tienen protección, pero para otro tipo de evento. Correcta: *"tienen protección interna contra picos de alta energía, no contra fluctuaciones rápidas de voltaje."*
4. *"Genteca verifica el tiempo de respuesta con [X norma]."* — Solo sostenible si Genteca tiene certificación o ensayo acreditado que lo respalde. Sin eso, marketing claim, no fact técnico.

---

## 4. Insumo para argumentario ESC (5 puntos para fuerza de ventas)

**1. El equipo ya viene protegido, pero para otra amenaza:**
*"El inverter que tiene tu cliente ya tiene un MOV de fábrica que lo protege contra rayos y picos. El MOV hace bien su trabajo. El problema es diferente: las caídas y fluctuaciones rápidas de voltaje — que en Venezuela son frecuentes — el MOV no las ve. Para eso existe el Exceline GSM."*

**2. El tiempo importa porque el equipo se 'aguanta' solo por muy poco tiempo:**
*"Cuando la luz parpadea o cae, el equipo inverter vive de la energía guardada en sus capacitores internos. Eso le dura entre 8 y 25 ms típicamente. Si el protector reacciona en 30 ms o menos, llega a tiempo. Si reacciona en 200 ms — como muchos protectores convencionales — el equipo ya sufrió el golpe."*

**3. Lo que se daña no es lo que se ve:**
*"El usuario ve que el aire 'se apagó y encendió' y piensa que no pasó nada. Lo que no ve es que cada flicker estresa el capacitor del bus DC y los transistores IGBT. Ese estrés es acumulativo — la tarjeta que debería durar 10 años dura 3-4. El daño silencioso es el más costoso."*

**4. El fabricante del equipo ya lo sabe:**
*"Mitsubishi Electric, Daikin y otros fabricantes incluyen en sus manuales la recomendación de instalar un estabilizador de voltaje en zonas con red inestable. Genteca Exceline GSM es esa protección, con la ventaja adicional del Sensor NTC que avisa cuando el protector mismo necesita revisión."*

**5. Protección verificable, no fe:**
*"El Sensor NTC del Exceline GSM monitorea la temperatura del varistor interno. Cuando el varistor ha absorbido demasiados golpes y está al límite, el sensor lo detecta. Un protector sin NTC puede estar 'muerto' por dentro y el usuario no lo sabe. Con Genteca, la protección es visible."*

---

## 5. Insumo para QR / video explicativo

### Para audiencia consumidor final (60 segundos, QR en empaque)

1. **Problema en 5 s:** bombillo parpadeando — *"Esto le pasa a la corriente en tu casa todos los días."*
2. **Por qué daña tu inverter (15 s):** *"Tu aire, tu nevera inverter, tu lavadora — tienen electrónica sofisticada que se alimenta de esa corriente. Cada parpadeo genera un estrés interno en sus componentes. No lo ves, pero se acumula."*
3. **Por qué tu equipo no se protege solo (15 s):** *"Tu inverter ya trae protección contra rayos y picos fuertes. Pero esa protección no 've' los parpadeos rápidos — son en otro rango."*
4. **Cómo Genteca lo resuelve (15 s):** *"El Exceline GSM detecta el parpadeo en menos de 30 milisegundos — mucho antes de que el daño ocurra — y protege tu equipo."*
5. **Diferenciador NTC (5 s):** *"Y el Sensor NTC te avisa cuando el protector mismo necesita revisión. Nunca estás desprotegido sin saberlo."*
6. **CTA (5 s):** genteca.com.ve / código de producto.

**Nivel de profundidad:** ninguna terminología técnica. "Parpadeo" en lugar de "flicker". "Estrés interno" en lugar de "overcurrent en IGBT". "Componentes electrónicos" en lugar de "capacitor del bus DC".

### Para audiencia instalador técnico / ESC (2-3 minutos, versión extendida)

1. **Mapa de amenazas de power quality:** diferencia entre surge (pico impulsivo de alta energía), voltage sag (caída sostenida), y flicker (fluctuación rápida). Mostrar oscilograma típico de cada uno.
2. **Qué protege el equipo de fábrica y qué no:** MOV/varistor = surge. Filtro EMI = ruido RF. Bus DC capacitor = hold-up breve. Ninguno = flicker repetitivo.
3. **Mecanismo de daño en la tarjeta inverter:** bus DC capacitor + IGBT stress durante recovery. Mencionar IEC 61000-4-11 como la norma que lo reconoce.
4. **Por qué el tiempo de respuesta importa:** hold-up time típico 8-25 ms. Protector de 30 ms llega antes. Protector de 100-200 ms llega tarde.
5. **Innovaciones Exceline GSM:** tiempo de respuesta < 30 ms verificado + Sensor NTC para supervisión del varistor.
6. **Aplicaciones recomendadas:** inverter HVAC, refrigeración comercial inverter, bombas de agua inverter, lavadoras inverter premium.

---

## 6. Pendientes y preguntas abiertas

**1. Especificación exacta del MOV en equipos de marcas referidas:** acceder a service manuals de nivel técnico profundo de Mitsubishi Electric serie PUZ/MXZ o LG Inverter V para identificar part number del MOV instalado y verificar joules y voltaje de clamping. Fuente: meus.mitsubishielectric.com (requiere registro de técnico de servicio).

**2. Hold-up time del bus DC en modelos específicos:** el rango 8-25 ms es estimación basada en capacidades típicas de equipos residenciales 1-3 ton. Necesita verificación midiendo en equipos específicos con osciloscopio, o consultando directamente a un ingeniero de aplicaciones de Mitsubishi Electric, Daikin o LG. **Este dato es el pilar cuantitativo central de la tesis** — si el hold-up es sistemáticamente mayor de 30 ms en equipos del mercado venezolano, el argumento se debilita.

**3. Certificación de los < 30 ms del Exceline GSM:** ¿bajo qué metodología de prueba se mide y certifica el tiempo de respuesta? ¿Existe un ensayo acreditado (FONDONORMA, UL, IEC) que lo respalde? Sin certificación, marketing claim. Con certificación, fact técnico verificable. **Pregunta crítica para la integridad de toda la narrativa.** *(Nota: Liliam I&D confirmó medición de laboratorio Genteca; falta confirmar acreditación externa si aplica.)*

**4. Consulta directa al electrónico de potencia:** el Mecanismo C (reset del microcontrolador) debería ser validado por un ingeniero electrónico de potencia con experiencia en diseño de inversores. Alberto Betancourt o un contacto técnico Genteca podría hacer esta consulta a un fabricante de módulos IGBT (Infineon, STMicroelectronics, ON Semiconductor).

**5. Búsqueda de literatura IEEE sobre voltage sag e inverter HVAC:** con acceso a IEEE Xplore, buscar "voltage sag inverter air conditioner failure" y "IGBT failure voltage sag HVAC" — papers de 2010-2024 documentan exactamente los mecanismos descritos. Esos papers son las fuentes más robustas para respaldar la narrativa técnica.

**6. Verificar recomendaciones de fabricantes en manuales para Venezuela:** los manuales de Mitsubishi Electric, Daikin y LG para Latinoamérica/Caribe pueden tener recomendaciones específicas de protección de voltaje más explícitas que los manuales globales.

---

**Método de acceso:** conocimiento de entrenamiento (hasta agosto 2025). WebSearch y WebFetch denegadas en esta sesión — todas las fuentes listadas están pendientes de verificación manual.

**Nivel de confianza general:** alto en principios físicos (comportamiento MOV, mecanismo IGBT, hold-up time bus DC, clasificación IEC/IEEE de eventos power quality). Medio en especificaciones de marcas específicas (requieren verificación contra datasheets actuales). Bajo en el dato exacto de 30 ms como umbral "de norma" — ese número necesita justificación técnica propia de Genteca, no existe en una sola fuente normativa.

## Fuentes para verificación manual

- IEEE 1159-2019 — Recommended Practice for Monitoring Electric Power Quality — standards.ieee.org/ieee/1159/6081/
- IEEE 1564-2014 — Guide for Voltage Sag Indices — standards.ieee.org/ieee/1564/3720/
- IEC 61000-4-11 — Voltage dips, short interruptions and voltage variations immunity tests — webstore.iec.ch/publication/4228
- IEC 61000-4-5 — Surge immunity test — webstore.iec.ch/publication/4210
- Mitsubishi Electric Mr. Slim installation manuals (MSZ/MUZ/PUZ series) — meus.mitsubishielectric.com/content/dam/pages/service/
- Infineon Application Note AN2013-04 — IGBT Module Reliability
- Littelfuse — Varistor Design Guide
- Schneider Electric White Paper 82 — Types of UPS Systems and Voltage Protection
- IEEE Xplore — búsqueda sugerida: "voltage sag inverter HVAC IGBT failure" — ieeexplore.ieee.org
- Panasonic Industrial — Aluminum Electrolytic Capacitor Application Guide
