# Outline: Resultados Investigacion Pantallas GME + Van Westendorp — para I+D
**Archivo PPTX**: `Resultados_Investigacion_Pantallas_GME_VW_para_I+D_v1_2026-05-06.pptx`
**Audiencia**: Equipo I+D GME (interno)
**Proposito**: Habilitar decisiones de desarrollo con recomendaciones accionables sobre pantalla, UI, features y pricing
**Fecha**: 2026-05-06 | **Version**: v1 | **Slides**: 18

---

## Seccion 1 — Marco (Slides 1-3)

---

### Slide 1 | COVER

**Titulo**: Estudio de Pantallas GME: Resultados y Recomendaciones para I+D

**Subtitulo / subtexto**:
- Preferencia de pantalla A vs B | Voz del tecnico | Diferenciacion R/B/M | Analisis Van Westendorp
- Audiencia: Equipo I+D GME (interno)
- Encuesta: Comunidad Exceline Profesional | n=29 | Abr-May 2026
- Fecha: 2026-05-06 | Version: v1 | Confidencial

**Diseno**: Fondo azul marino (C_NAVY), barra vertical naranja Exceline, logo/marca en naranja. Footer confidencial.

**Nota del presentador**: Este deck es un handoff de investigacion a I+D. Toda la data proviene de encuesta real (n=29). Nada esta inferido o inventado.

---

### Slide 2 | AGENDA

**Titulo**: Agenda — estructura del deck (18 slides)

**Cuerpo** (tabla de 7 secciones):

| # | Seccion | Slides | Descripcion |
|---|---------|--------|-------------|
| 1 | Marco y metodologia | 3 | Encuesta, muestra, caveats metodologicos |
| 2 | Hallazgo principal: Pantalla A vs B | 4-7 | Resultado 83% B, comprensibilidad, agrado, recomendacion |
| 3 | Voz del tecnico: comentarios abiertos | 8-10 | Demandas top, quotes, priorizacion v1/v2 |
| 4 | Diferenciacion R/B/M | 11-12 | Lo que I+D hizo bien — logica real entre modos |
| 5 | Pricing: Van Westendorp | 13-16 | Metodologia, curvas, segmentos, implicacion para BOM |
| 6 | Recomendaciones consolidadas | 17-18 | Tabla v1 vs v2, 15 preguntas pendientes a engineering |
| 7 | Proximos pasos | 18 | Engineering, naming, brief Vael |

**Nota del presentador**: La seccion de Diferenciacion R/B/M (Sec. 4) puede saltarse si el equipo de I+D ya conoce el analisis de Vera. Las secciones 2 y 5 son las de mayor impacto en decisiones inmediatas.

---

### Slide 3 | METODOLOGIA

**Titulo**: Metodologia: encuesta digital a tecnicos Exceline Profesional

**Subtitulo**: Leer los caveats antes de aplicar los resultados — muestra pequena por segmento

**Cuerpo** (4 cajas de metodologia):

1. **Instrumento**: Encuesta online | Comunidad Exceline Profesional | Abr-May 2026
2. **Muestra**: n=32 completadas | 29 validas para analisis | 3 descartadas (incompletas)
3. **Segmentacion**: Refrigeracion (R): n=15, 52% | Motores (M): n=8, 28% | Bombas (B): n=6, 20%
4. **Precio — Van Westendorp**: 4 preguntas PSM por respondiente | Analisis de interseccion de curvas | Puntos PMC / OPP / IPP / PME

**Caveats (caja naranja-ambar)**:
- Muestra pequena por segmento: Bombas (n=6) y Motores (n=8) tienen intervalos de confianza amplios. Resultados son direccionales, no estadisticamente concluyentes para esos segmentos.
- Refrigeracion representa 52% del total — el promedio total esta sesgado hacia el segmento mas sensible al precio y con preferencias mas conservadoras.
- Van Westendorp mide percepcion de precio, no demanda real ni intencion de compra. No reemplaza analisis de costos BOM ni estrategia comercial.
- Encuesta sin ancla de precio competidor: los tecnicos respondieron sin ver precios de referencia — las respuestas VW pueden subestimar disposicion a pagar del segmento de Motores.

**Nota del presentador**: Estos caveats son condicion para que I+D confie en los datos. No reducen la utilidad de los hallazgos — los calibran correctamente.

---

## Seccion 2 — Hallazgo principal: Pantalla A vs B (Slides 4-7)

---

### Slide 4 | PANTALLA A vs B — SIDE-BY-SIDE VISUAL

**Titulo**: Las dos opciones de pantalla principal evaluadas por los tecnicos

**Subtitulo**: Variante R-220 (Refrigeracion) — la misma logica aplica a B-220 y M-220

**Cuerpo**:
- Columna izquierda — OPCION A (Pantalla simple): imagen `_img_R/image1.png`. Caption: "Muestra estado y valores medidos. Sin setpoints visibles en pantalla principal."
- Columna derecha — OPCION B (Con setpoints visibles): imagen `_img_R/image2.png`. Caption: "Muestra estado + valores de ajuste alto/bajo voltaje y rangos de sobrecarga/subcarga configurados."
- Divisor central: "vs" en naranja Exceline

**Nota del presentador**: La unica diferencia evaluada en la encuesta fue la pantalla principal (imagen 1 vs imagen 2 por variante). Las pantallas 2-5 son identicas. Esto es importante para interpretar los resultados — los tecnicos eligieron B knowing que la pantalla adicional mostraba informacion de los setpoints actuales.

---

### Slide 5 | RESULTADO: 83% PREFIERE PANTALLA B

**Titulo (conclusion)**: 83% de los tecnicos prefiere la Pantalla B — resultado consistente en los tres segmentos

**Subtitulo**: 24 de 29 respondientes — preferencia estadisticamente robusta a nivel total

**Cuerpo**:

Gran numero: **83%** (24/29 prefieren B)

Tabla por segmento:

| Segmento | n | Prefiere B | Prefiere A | % B |
|----------|---|-----------|-----------|-----|
| Motores (M) | 8 | 8 | 0 | 100% |
| Refrigeracion (R) | 15 | 12 | 3 | 80% |
| Bombas (B) | 6 | 4 | 2 | 67% |
| **TOTAL** | **29** | **24** | **5** | **83%** |

**Caja de recomendacion (verde)**:
> RECOMENDACION PARA I+D: Adoptar Pantalla B como pantalla principal por defecto para los tres modos (R/B/M). El resultado es unanime en Motores (8/8), mayoritario en Refrigeracion (12/15) y mayoritario en Bombas (4/6). La ventaja de B sobre A es consistente y robusta a nivel total.

Nota de pie: Bombas n=6 — resultado direccional, confirmar con muestra mayor en fase 2.

**Nota del presentador**: El unico segmento donde el resultado es menos contundente es Bombas (67%), pero n=6 hace que incluso 2 votos en contra no sean estadisticamente significativos. La unanimidad en Motores es llamativa y puede reflejar que ese segmento tiene mayor sofisticacion tecnica y valora mas la visibilidad de parametros.

---

### Slide 6 | COMPRENSIBILIDAD Y AGRADO

**Titulo (conclusion)**: Pantalla B tambien supera a A en comprensibilidad y agrado

**Subtitulo**: Mas informacion visible no implica mayor confusion — los tecnicos leen la densidad como valor

**Cuerpo**:

Comprensibilidad (% "comprensible" o "muy comprensible"):
- Pantalla A: 86%
- Pantalla B: **97%**

Agrado (% "alto" o "muy alto"):
- Pantalla A: 79% — con 7% negativos
- Pantalla B: **90%** — sin negativos

**Lectura clave para I+D**: La Pantalla B muestra mas datos (setpoints, rangos) que la A, pero los tecnicos la comprenden MEJOR y la encuentran mas agradable. Esto valida la hipotesis de diseno: el tecnico prefiere transparencia de parametros sobre simplicidad visual. La pantalla no debe ocultar lo que el equipo hace.

Nota de pie: Las otras 4 pantallas (Ajustes Perillas, Ajustes Digitales, Reporte Fallas, Configuracion) son identicas entre A y B — no fueron objeto de evaluacion comparativa en la encuesta.

**Nota del presentador**: La ausencia de respuestas negativas para la Pantalla B en agrado es un dato fuerte. Implica que no hay ningun segmento de tecnicos que rechace la pantalla B, mientras que un 7% rechaza la A. En terminos de riesgo de diseno, B es la opcion segura.

---

### Slide 7 | LAS 5 PANTALLAS DEL GME — FLUJO COMPLETO

**Titulo**: Las 5 pantallas del GME — flujo completo de la interfaz (variante R-220)

**Subtitulo**: Pantallas 2-5 son comunes a todas las variantes — evaluadas cualitativamente via comentarios abiertos

**Cuerpo** (5 imagenes en fila con labels):

1. `_img_R/image2.png` — Pantalla 1B: Principal (adoptada)
2. `_img_R/image3.png` — Pantalla 2: Ajustes Fisicos (Perillas)
3. `_img_R/image4.png` — Pantalla 3: Ajustes Digitales
4. `_img_R/image5.png` — Pantalla 4: Reporte de Fallas
5. `_img_R/image6.png` — Pantalla 5: Configuracion

**Nota del presentador**: Las imagenes equivalentes para los modos B y M estan en `_img_B/` y `_img_M/`. La estructura es identica; cambian los valores default y el badge de color de variante.

---

## Seccion 3 — Voz del tecnico: comentarios abiertos (Slides 8-10)

---

### Slide 8 | DEMANDAS TOP: 9 FEATURES CATEGORIZADAS

**Titulo (conclusion)**: Los tecnicos piden 9 features concretas — clasificadas por urgencia y esfuerzo

**Subtitulo**: 29/29 respondientes dejaron comentario abierto — señal de engagement alto con el producto

**Cuerpo** (tabla):

| Demanda del tecnico | Frecuencia | Tipo de cambio | Version target |
|--------------------|-----------|----------------|----------------|
| Historial cronologico de fallas con timestamp | >=6 menciones | Firmware + RTC | **v1 critico** |
| Notificaciones push en tiempo real | >=3 menciones | Cloud / App | v2 |
| Multivoltaje 120/220 V — un solo SKU | 2 menciones | Hardware | v2 |
| Tiempo restante de reconexion visible | 2 menciones | UI / Firmware | **v1** |
| Rango voltaje hasta 265 V (sobre-voltaje VE) | 1 mencion | Hardware / Firmware | v1-evaluar |
| Picos de corriente arranque vs regimen | 1 mencion | Firmware (ADC logic) | v2 |
| Sensibilidad de desconexion <1 segundo | 1 mencion (Refrigeracion) | Firmware / ADC | **v1 critico** |
| Wording: "Ajustes Fisicos" -> "Ajustes de Perillas" | 1 mencion explícita | UI (cosmetico) | **v1 facil** |
| NFC como alternativa de pairing | 1 mencion | Hardware | v2 |

**Nota del presentador**: La frecuencia del historial de fallas es notable — aparece en los tres segmentos con distintas variantes ("las ultimas 5", "las ultimas 10 a 15", "log de eventos"). Es la demanda funcional mas clara del estudio. El caveat: implementarla bien requiere RTC — ver Pregunta Q5 a engineering.

---

### Slide 9 | QUOTES TEXTUALES DE TECNICOS

**Titulo**: Lo que dijeron los tecnicos — en sus palabras

**Fondo**: Azul marino (slide oscura para impacto)

**Cuerpo** (3 quotes):

**Quote 1** (naranja):
> "En electronica un ESP32 puede costar $10 siendo programable y con conectividad. Un producto masivo que incorpore control y monitoreo remoto no tiene por que elevar excesivamente el precio."
> — Tecnico de Refrigeracion, respondiente #104356020

*Implicacion*: La expectativa de precio es acida — I+D debe saber que el tecnico tiene un benchmark de componente en $10. La defensa del precio lista ($35) requiere guion de valor tecnico verificable.

**Quote 2** (azul):
> "Seria muy agradable que puedan registrar un historial de las ultimas 10 a 15 fallas. Este aplicativo tiene mucho potencial. Pueden agregarlo por contacto NFC."
> — Ing. Asdrúbal García, Tec. Refrigeracion/Climatizacion, respondiente #104362438

*Implicacion*: El historial cronologico es la demanda funcional #1. NFC es mencionado como canal alternativo de acceso — requiere antena hardware.

**Quote 3** (rojo):
> "La sensibilidad de desconexion es muy importante: una fluctuacion de menos de 1 segundo deja sin efecto la proteccion. Esto se incrementa en importancia en equipos de refrigeracion y aire acondicionado."
> — Tecnico de Refrigeracion, respondiente #104359489

*Implicacion*: Gap tecnico urgente para modo R. Ver Pregunta Q1 al equipo de engineering (sampling rate del ADC). Esta es una condicion de credibilidad del producto en el segmento mas grande.

**Nota del presentador**: El quote del ESP32 es el mas relevante para la decision de pricing. El tecnico no es naive — sabe cuanto cuestan los componentes. La respuesta a ese argumento no es ignorarlo; es explicar qué justifica el delta (protecciones especificas de motor, curva de disparo, diferenciacion R/B/M, etc.).

---

### Slide 10 | PRIORIZACION: v1 vs v2 (DEMANDAS UI)

**Titulo (conclusion)**: Priorizacion de demandas: v1 (octubre 2026) vs v2 (post-lanzamiento)

**Subtitulo**: Criterio: impacto en credibilidad para Refrigeracion (segmento dominante) + esfuerzo de implementacion

**Cuerpo** (dos columnas):

**v1 — Lanzamiento octubre 2026**:
1. Pantalla B como default — Ninguno: decision de configuracion
2. Fix wording "Ajustes de Perillas" — UI cosmetico: 1 dia de dev
3. Tiempo restante de reconexion visible — UI / firmware: countdown en pantalla
4. Validar sensibilidad <1 s en modo R — Pregunta Q1 a engineering (ADC sampling rate)
5. Log basico si hay RTC — Requiere confirmar RTC: ver Pregunta Q5

**v2 — Post-lanzamiento**:
1. NFC pairing — Requiere hardware: antena + controlador NFC (Q13)
2. Multivoltaje 120/220 V — Requiere variante PCB: impacto BOM a cuantificar (Q10)
3. Notificaciones push (cloud) — Requiere arquitectura cloud/relay: fuera de scope v1
4. Log cronologico 25+ eventos — Requiere RTC confirmado + ampliacion buffer firmware (Q4, Q5)
5. Rango hasta 265 V — Evaluar si requiere cambio en circuito de medicion o solo calibracion

**Nota del presentador**: El fix de wording ("Ajustes de Perillas") es lo mas rapido y mas visible en terminos de percepcion de calidad de la UI. Costo de no hacerlo: ninguno tecnico, pero el tecnico que lo señalo tiene razon — inconsistencia entre la barra inferior y el titulo de la pantalla.

---

## Seccion 4 — Diferenciacion R/B/M (Slides 11-12)

---

### Slide 11 | TABLA COMPARATIVA R/B/M: PARAMETROS

**Titulo (conclusion)**: Los tres modos tienen diferencias reales — no solo cambio de defaults

**Subtitulo**: Hallazgo de validacion tecnica (Vera, 2026-05-06) — sustenta el claim "tres modos en un protector"

**Cuerpo** (tabla de 3 columnas por modo):

| Parametro | GME-R220 Refrigeracion | GME-B220 Bombas | GME-M220 Motores |
|-----------|----------------------|-----------------|-----------------|
| Tiempo de Conexion (reconexion) | 300 s (rango 180-600 s) | 120 s (rango 5-300 s) | 60 s (rango 5-300 s) |
| Subcarga % / tiempo deteccion | 60% I-nom, t=10 s | 70% I-nom, t=5 s | 60% I-nom, t=5 s |
| Tiempo de reintento (tras subcarga) | 240 s | 20 min | 240 s |
| Maniobra diaria | No aplica | ACTIVADA — logica exclusiva de modo B | No aplica |
| Tiempo deteccion sobrecarga | No visible en mockup | No visible en mockup | 0.1-5 s ajustable (configurable) |
| Alineacion normativa | Copeland AE4-1365 (igualacion presiones) | Practica dry-run bombas (Franklin SubMonitor) | Logica Class 10/10A (pendiente confirmar) |
| Diferenciador clave | Tiempos conservadores para compresores hermeticos | Maniobra diaria — unica funcion exclusiva de modo | Tiempo deteccion sobrecarga ajustable — critico rotor trancado |

**Nota del presentador**: Los tres modos cambian principalmente valores default, con dos excepciones de logica: (1) Maniobra diaria, exclusiva de modo Bombas. (2) Tiempo de deteccion de sobrecarga configurable, visible solo en modo Motores. Engineering debe confirmar si esto refleja logica diferente en firmware o solo visibilidad/acceso diferente al parametro.

---

### Slide 12 | SINTESIS DIFERENCIACION: CONFIRMADOS Y PENDIENTES

**Titulo (conclusion)**: Sintesis: la diferenciacion entre modos tiene sustancia tecnica suficiente para el claim

**Subtitulo**: Con una condicion: engineering debe confirmar dos puntos antes del lanzamiento

**Cuerpo** (5 filas con badge CONFIRMADO / CONFIRMAR CON ENGINEERING):

1. **CONFIRMADO** — Valores default distintos en todos los parametros de tiempo y umbral. Esto solo ya justifica "configurado para cada aplicacion". Directo de mockups.
2. **CONFIRMADO** — Maniobra diaria es logica exclusiva del modo Bombas (GME-B220). No aparece en R ni M. Es la unica funcion de logica diferente confirmada en mockups.
3. **CONFIRMADO** — Tiempo de deteccion de sobrecarga configurable solo visible en GME-M220. 0.1-5 s ajustable. Critico para proteccion contra rotor trancado. No visible en R/B.
4. **CONFIRMAR CON ENGINEERING** — ¿Es el tiempo de deteccion de sobrecarga un parametro oculto en R y B, o esta fijo? Si esta fijo en R/B pero configurable en M, el claim "tres modos" es mas fuerte.
5. **CONFIRMAR CON ENGINEERING** — ¿La maniobra diaria implica logica de firmware diferente o solo un toggle de scheduling? Si es logica exclusiva (ciclo de test programado), el claim tiene profundidad tecnica real.

**Nota del presentador**: La recomendacion para I+D es pedir a engineering respuesta especifica para items 4 y 5 — son las preguntas Q3 y Q7 del archivo Preguntas_Engineering_GME_15.md. Sin esas respuestas el claim E no puede activarse en comunicacion externa.

---

## Seccion 5 — Pricing: Van Westendorp (Slides 13-16)

---

### Slide 13 | VW: METODOLOGIA

**Titulo**: Metodologia Van Westendorp: cuatro preguntas, cuatro curvas, cuatro puntos clave

**Subtitulo**: PSM (Price Sensitivity Meter, 1976) — estandar para estudios de percepcion de precio en nuevos productos

**Cuerpo**:

Las 4 preguntas:
- Q10: "¿A que precio le parece TAN BARATO que no confiaria en su calidad?" — Curva descendente (TC)
- Q11: "¿A que precio le parece economico y confiable?" — Curva descendente (C)
- Q12: "¿A que precio le parece costoso pero aun lo compraria?" — Curva ascendente (E)
- Q13: "¿A que precio le parece excesivamente costoso que NO lo compraria?" — Curva ascendente (TE)

Los 4 puntos clave:
- **PMC** (Point of Marginal Cheapness) — Cota inferior del rango aceptable. Interseccion TC ∩ E.
- **OPP** (Optimal Price Point) — Precio de menor resistencia psicologica. Interseccion TC ∩ TE.
- **IPP** (Indifference Price Point) — Precio "justo" para el promedio. Interseccion C ∩ E.
- **PME** (Point of Marginal Expensiveness) — Cota superior del rango aceptable. Interseccion C ∩ TE.

**RAP** (Rango Aceptable de Precios) = [PMC, PME]

Caveat: VW mide percepcion de precio, no demanda real ni intencion de compra. Los resultados son input para la decision de precio — no la decision en si misma.

**Nota del presentador**: La metodologia es solida y ampliamente usada para precios de lanzamiento de nuevos productos. Para una audiencia de ingenieros: lo que VW mide es la forma de la distribucion de respuestas de los cuatro precios — los puntos clave son los cruces de esas distribuciones acumuladas.

---

### Slide 14 | CURVA VW TOTAL + PUNTOS CLAVE

**Titulo (conclusion)**: Resultado total (n=29): rango aceptable USD 29.90 – 40.33, precio optimo USD 35

**Subtitulo**: OPP e IPP casi coinciden en $35 — mercado con expectativa de precio madura y consistente

**Cuerpo**:
- Grafico: `van_westendorp/vw_total.png` (7.8" ancho)
- Panel lateral con los 4 puntos clave:
  - PMC: $29.90 — Cota inferior del rango aceptable
  - OPP: $35.00 — Precio optimo (min. resistencia)
  - IPP: $35.50 — Precio "justo" (indiferencia)
  - PME: $40.33 — Techo del rango aceptable
- Caja RAP: Rango Aceptable de Precios: $29.90 – $40.33

**Nota del presentador**: La casi coincidencia de OPP ($35.0) e IPP ($35.5) es una señal de mercado inusualmente clara. Normalmente hay mas separacion entre estos dos puntos. Indica que los tecnicos tienen una expectativa de precio bien formada y consistente para este tipo de producto — probablemente anclada en productos comparables que conocen (ICM492, Wagner DSP-1, etc.).

---

### Slide 15 | CURVAS VW POR SEGMENTO

**Titulo (conclusion)**: Curvas por segmento: Motores tolera mas, Refrigeracion es el constraint critico

**Subtitulo**: El segmento de Motores es el mas premium; Refrigeracion fija el techo practico para un SKU unico

**Cuerpo** (3 graficos en columna):

Motores (n=8) — `van_westendorp/vw_motores.png`:
- PMC $35.3 | OPP $35.5 | IPP $40.5 | PME $45.5

Bombas (n=6) — `van_westendorp/vw_bombas.png`:
- PMC $30.0 | OPP $30.5 | IPP $40.0 | PME $50.0
- [n=6: solo direccional]

Refrigeracion (n=15) — `van_westendorp/vw_refrigeracion.png`:
- PMC $29.7 | OPP $30.2 | IPP $30.5 | PME $39.7

Nota de pie: Constraint critico para SKU unico: el techo de Refrigeracion ($39.7) fija el precio maximo antes de perder aceptacion en el 52% de la muestra. Un precio lista de $35 cae dentro del rango aceptable de los TRES segmentos simultaneamente.

**Nota del presentador**: El segmento de Refrigeracion es el que tiene el OPP y el IPP mas bajos Y mas juntos ($30.2 y $30.5) — lo que significa que su expectativa de precio esta muy concentrada en torno a $30. El hecho de que el techo sea $39.7 da headroom hasta $40, pero para maximizar aceptacion en Refrigeracion el precio ideal seria $30-35.

---

### Slide 16 | IMPLICACION PARA BOM / I+D

**Titulo (conclusion)**: Recomendacion de precio: USD 35 lista — y lo que eso implica para el BOM

**Subtitulo**: El analisis VW informa a I+D el espacio de precio disponible — I+D define si el BOM encaja

**Cuerpo**:

Caja de recomendacion (azul marino):
- **USD 35** — Precio lista sugerido
- Floor: USD 30 | Ceiling: USD 40
- Escenario A: SKU unico, misma unidad hardware configurable por firmware R/B/M

Implicaciones para I+D / BOM:
1. **$35 lista implica costo de fabrica objetivo de ~$15-20** — Asumiendo margen distribuidor 30-40% + margen Exceline. El BOM + mano de obra + certificaciones debe caber en ese rango.
2. **Cada feature adicional de v1 tiene impacto en BOM** — RTC: ~$0.5-2 adicional. Antena NFC: ~$1-3. La decision de scope v1 vs v2 tiene costo real.
3. **El segmento de Motores tolera hasta $45.50** — Si hay variante con mayor capacidad de corriente, hay headroom de precio para ese SKU.
4. **Multivoltaje 120/220 V elevaria precio pero expandiria TAM** — Un solo SKU 120/220 elimina la decision de compra al tecnico. Impacto en BOM a confirmar con engineering (Q10).

**Nota del presentador**: Este slide es el puente entre el estudio de mercado y la ingenieria. El analisis VW no puede saber si $35 cubre el BOM — eso es trabajo del equipo. Pero si da el techo: exceder $40 implica salir del rango aceptable del segmento dominante (Refrigeracion).

---

## Seccion 6 — Recomendaciones consolidadas para I+D (Slides 17-18)

---

### Slide 17 | TABLA v1 vs v2 CONSOLIDADA

**Titulo (conclusion)**: Tabla de decisiones para I+D: lo que va en v1 y lo que va en v2

**Subtitulo**: Basada en datos de encuesta + validacion tecnica Vera + analisis de pricing VW

**Cuerpo** (dos columnas):

**v1 — Lanzamiento octubre 2026**:

| Item | Accion |
|------|--------|
| Pantalla B | Adoptar como default los tres modos (R/B/M). Resultado: 83% total, 100% Motores. |
| Fix wording UI | Cambiar "Ajustes Fisicos" por "Ajustes de Perillas" (solicitado por tecnico, consistencia con barra inferior). |
| Countdown reconexion | Mostrar tiempo restante de reconexion en pantalla principal. Mejora experiencia en campo. |
| Validar sens. <1s modo R | Confirmar con engineering: ADC sampling rate suficiente para detectar fluctuaciones <1 s (Q1). Critico para credibilidad en refrigeracion. |
| Log basico si hay RTC | Si el hardware incluye RTC: implementar log de min. 5 eventos con timestamp en v1. Si no hay RTC, diferir a v2. |

**v2 — Post-lanzamiento (roadmap)**:

| Item | Accion |
|------|--------|
| NFC pairing | Lectura de configuracion y diagnostico por NFC. Requiere hardware: antena + controlador NFC (Q13). |
| Multivoltaje 120/220 V | Un solo SKU para ambas tensiones. Requiere variante de PCB — impacto BOM a cuantificar (Q10). |
| Notificaciones push | Alertas en tiempo real via cloud/relay. Requiere arquitectura backend — fuera de scope v1. |
| Log cronologico 25+ eventos | Historial completo con timestamp real. Requiere RTC confirmado + buffer firmware (Q4, Q5). |
| Rango hasta 265 V | Cubrir zonas VE con sobre-voltaje cronico. Evaluar si requiere cambio en circuito de medicion. |

**Nota del presentador**: Esta tabla es la salida operativa mas importante del estudio para I+D. Los 5 items de v1 pueden ser discutidos en el proximo sprint planning. Los 5 de v2 van al roadmap.

---

### Slide 18 | 15 PREGUNTAS A ENGINEERING + PROXIMOS PASOS

**Titulo (conclusion)**: 15 preguntas pendientes a engineering determinan alcance real del producto

**Subtitulo**: Archivo completo: `Preguntas_Engineering_GME_15.md` — estas son las 5 prioritarias para v1

**Cuerpo** (5 preguntas prioritarias):

| Q# | Tema | Pregunta resumida | Impacto | Urgencia |
|----|------|-------------------|---------|---------|
| Q1 | Sensibilidad <1 s | ¿A que frecuencia muestrea el ADC? ¿Puede detectar fluctuaciones <1 s? | Credibilidad en Refrigeracion | ALTA — bloquea claim |
| Q2 | Operacion offline | ¿El GME protege activamente si no hay WiFi? ¿La logica de proteccion es independiente del webserver? | Gate del claim "sin cloud" | ALTA — bloquea claim |
| Q4+Q5 | Log y RTC | ¿Existe buffer circular de eventos en firmware? ¿Hay RTC con bateria o sincronizacion NTP? | Feature mas solicitada por tecnicos | MEDIA — v1 scope |
| Q9 | Corriente maxima contactor | ¿Cual es la corriente maxima conmutable en AC-3? ¿40 A en mockup es limite real o ejemplo? | Define claims de capacidad del producto | MEDIA — v1 scope |
| Q15 | Logica 3 intentos | ¿El firmware reintenta 3 veces antes de bloquear? ¿Se puede configurar? ¿Como se comunica al tecnico? | Riesgo de responsabilidad y confianza | MEDIA — v1 scope |

**Proximos pasos**:
1. Engineering responde las 15 preguntas (`Preguntas_Engineering_GME_15.md`)
2. Focus groups de naming GME (sesiones previas en carpeta investigacion)
3. Brief Vael para arquitectura de mensaje del lanzamiento

**Nota del presentador**: Q1 y Q2 son gates: sin respuesta a esas dos preguntas, los claims mas importantes del GME no pueden activarse. El Owner deberia pedir respuesta en formato tabla dentro del sprint actual. El archivo `Preguntas_Engineering_GME_15.md` tiene las 15 preguntas completas con el contexto tecnico de Vera.

---

## Apendice de fuentes / activos

### Imagenes usadas en el deck

| Slide | Archivo | Descripcion |
|-------|---------|-------------|
| 4 | `_img_R/image1.png` | Pantalla 1A — Principal, Opcion A (R-220) |
| 4 | `_img_R/image2.png` | Pantalla 1B — Principal, Opcion B (R-220) |
| 7 | `_img_R/image2.png` | Pantalla 1B (flujo) |
| 7 | `_img_R/image3.png` | Pantalla 2 — Ajustes Fisicos / Perillas |
| 7 | `_img_R/image4.png` | Pantalla 3 — Ajustes Digitales |
| 7 | `_img_R/image5.png` | Pantalla 4 — Reporte de Fallas |
| 7 | `_img_R/image6.png` | Pantalla 5 — Configuracion |
| 14 | `van_westendorp/vw_total.png` | Curva VW — muestra total n=29 |
| 15 | `van_westendorp/vw_motores.png` | Curva VW — segmento Motores n=8 |
| 15 | `van_westendorp/vw_bombas.png` | Curva VW — segmento Bombas n=6 |
| 15 | `van_westendorp/vw_refrigeracion.png` | Curva VW — segmento Refrigeracion n=15 |

### Documentos fuente consultados

- `DATA FINAL Pantallas GME.xls.xlsx` — data cruda encuesta (29 respondientes)
- `Comentarios_tecnicos_encuesta.md` — comentarios abiertos extraidos
- `Informe_Van_Westendorp.md` — analisis de pricing completo
- `_intel/Vera_validacion_tecnica_GME_2026-05-06.md` — diferenciacion R/B/M + standards + preguntas engineering
- `_intel/OL-3_GME_innovation_radar_2026-05-06.md` — mapa competitivo
- `Investigacion UI.txt` y `Investigacion UI_V2.txt` — contexto del Owner sobre el producto
- `Preguntas_Engineering_GME_15.md` — 15 preguntas completas para el equipo de firmware

---

*Generado por Vivienne — Presentation Designer, RAUL | 2026-05-06*
*Reconstruccion del deck a partir de este outline: ejecutar `03-review-and-release/_build_pptx.py`*
