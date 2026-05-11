---
title: "Verificacion Tecnica GRN-MV — Preguntas Q1-Q5 para correccion de guion de video"
type: Technical
author: Vera
consumer: Nerea (script architect)
product_code: GRN-MV
product_line: Exceline Profesional
aplicacion: Vaciado 2 niveles / bomba sumergible en pozo
date: 2026-05-10
sources:
  - HDE V9 (GRN-MV_HDE_V9.pdf)
  - MAN REV3 (GRN-MV_MAN REV3.pdf) — fuente de verdad operativa
  - MAN V3 (GRN-MV_MAN_V3.pdf)
  - MAN V3 IMP (GRN-MV_MAN_V3_IMP.pdf)
  - HDE V4 (GRN-MV_HDE_V4.pdf) — unica version con tabla de especificaciones completa
  - GLA R V2 (GRN-MV_GLA_R_V2.pdf) — tabla de specs mas reciente con valores coherentes
  - GLA T V1 REV3 (GRN-MV_GLA_T_V1_REV3.pdf) — tabla corrupta, no usar para valores
---

# Nota Tecnica — GRN-MV Video: Verificacion Q1-Q5

Aplicacion de referencia: vaciado de pozo, 2 niveles, 3 sondas (REF + MIN + MAX). Bomba sumergible. Bomba OFF cuando nivel cae bajo MIN; bomba ON cuando nivel recupera MAX.

---

## Q1 — Tiempo de deteccion 10 s: cuando aplica

**Respuesta: MATIZ. Los 10 s estan documentados exclusivamente en el contexto del ajuste de sensibilidad (comisionamiento), no como retardo operativo de ciclo normal.**

Los documentos presentan el tiempo de 10 s de la siguiente forma:

MAN V3 (seccion "Ajuste de Sensibilidad"):
> "Con las sondas ya cubiertas por el liquido, espere el tiempo de deteccion despues de estabilizado el nivel (10 segundos). Si enciende el LED verde, deje el ajuste en el valor recomendado. De lo contrario, aumente la sensibilidad."
> "IMPORTANTE: Recuerde esperar 10 segundos cada vez que ajuste la sensibilidad."

MAN V3 IMP replica identicamente este texto. MAN REV3 no menciona el valor de 10 s en ningun paso operativo — solo dice "Ajuste la perilla de sensibilidad en funcion del liquido conductor de la aplicacion" sin especificar tiempo.

**Interpretacion tecnica razonada:**

El guion actual (contador 1→10s visible en pantalla al tocar MAX y al dejar MIN) no tiene sustento en los documentos publicados. El comportamiento documentado del 10 s es:

- Es el tiempo que debe transcurrir durante el AJUSTE DE SENSIBILIDAD (puesta en marcha) para que el relé confirme que puede detectar el liquido con la perilla en el valor configurado.
- NO existe en ningun documento un retardo de 10 s para la activacion o desactivacion operativa del rele durante el ciclo normal de vaciado.

**Juicio tecnico (no documentado, requiere confirmacion de ingenieria):**

Relacionando con la logica de reles de nivel de este tipo (clase IEC 60947-1), es comun que el tiempo de deteccion sea simetrico (el mismo retardo aplica tanto para activacion como para desactivacion), pero el valor tipico de retardo operativo en un rele de nivel de baja complejidad suele ser del orden de 2-5 s, no 10 s. Los 10 s documentados parecen ser el tiempo de estabilizacion para prueba de sensibilidad, no el retardo del rele en operacion ciclica.

**Para el guion:** eliminar el contador 1→10s como comportamiento visible en ciclo de vaciado/llenado normal. Si se quiere mostrar un retardo anti-falsos-positivos, hay que confirmarlo con ingenieria de Genteca — no esta documentado publicamente.

**FLAG DE ESCALACION:** Confirmar con I+D si el relé tiene retardo operativo configurable o fijo distinto de los 10 s de sensibilidad. Pregunta especifica: "En ciclo normal de vaciado, hay retardo entre que el nivel toca MAX y el rele activa la bomba? Cuanto? Es el mismo retardo al caer por debajo de MIN?"

---

## Q2 — Memoria de tarea: que memoriza exactamente

**Respuesta: MATIZ. Los documentos dicen que memoriza la "tarea en ejecucion" (vaciado o llenado), no el estado del rele. La recarga post-apagon no esta documentada con detalle sobre revalidacion de sondas.**

HDE V9 (Caracteristicas Generales):
> "Sistema inteligente de memoria de tarea: Mantiene la continuidad del servicio incluso despues de una interrupcion electrica. Si el equipo se encontraba en proceso de vaciado o llenado al momento del corte, retoma automaticamente la ultima funcion al restablecerse la energia."

MAN V3 / MAN V3 IMP (Descripcion del Producto):
> "Su sistema inteligente ante un apagon o parpadeo memoriza la tarea en ejecucion (vaciado o llenado) y al restablecerse el servicio retorna con esta funcionalidad."

**Interpretacion:**

1. Lo que se memoriza es la APLICACION CONFIGURADA (vaciado vs llenado), no el estado instantaneo del rele (bomba ON u OFF al momento del corte).

2. Al volver la energia, el dispositivo "retoma" en modo vaciado — lo que fisicamente significa que el rele revalua el estado de las sondas en ese momento y actua en consecuencia (bomba ON si el nivel esta sobre MAX, bomba OFF si el nivel esta bajo MIN, comportamiento indeterminado en la zona intermedia entre MIN y MAX).

3. No hay documentacion sobre si hay una espera de revalidacion de sondas post-apagon (con o sin los 10 s). El texto "retoma automaticamente" sugiere rearranque sin retardo adicional, pero no es explicito.

**Para el guion:** la descripcion correcta es "el GRN-MV recuerda en que modo estaba configurado (vaciado) y retoma esa funcion automaticamente." NO se debe decir "el rele recuerda si la bomba estaba encendida o apagada." La bomba volvera a encenderse o apagarse segun el nivel real de las sondas al momento de restaurar la energia.

**FLAG DE ESCALACION (menor):** Confirmar si hay retardo de revalidacion post-apagon. Para el guion es relevante porque cambia la animacion del escenario de corte de luz.

---

## Q3 — Comportamiento de LEDs en vaciado

**Respuesta: SI para los estados base. NO hay documentacion de estados intermedios ni parpadeo.**

Los siguientes estados estan documentados consistentemente en MAN REV3, MAN V3, MAN V3 IMP y MAN REV1/REV2:

| LED    | Estado | Significado en vaciado        | Fuente                      |
|--------|--------|-------------------------------|-----------------------------|
| Rojo   | ON     | Producto energizado           | MAN REV3, MAN V3, MAN V3 IMP |
| Rojo   | OFF    | Producto sin energia          | MAN REV3, MAN V3, MAN V3 IMP |
| Verde  | ON     | Bomba encendida               | MAN REV3, MAN V3, MAN V3 IMP |
| Verde  | OFF    | Bomba apagada                 | MAN REV3, MAN V3, MAN V3 IMP |

Nota: MAN V3 IMP tiene una redaccion ligeramente distinta en el cuerpo de texto — "LED verde encendido: Nivel de liquido por encima del punto de referencia" — que es equivalente a "bomba encendida" en modo vaciado, pero formulada desde el nivel fisico en lugar del estado de la carga. Esto no es contradiccion.

**Estados intermedios / parpadeo:**
No documentados en ninguno de los documentos de la KB. No existe mencion de parpadeo durante deteccion, durante ajuste de sensibilidad, ni post-apagon.

**Para el guion:** LED rojo = encendido/apagado segun presencia de tension. LED verde = estado del rele de salida (bomba ON/OFF). Sin animacion de parpadeo — no hay base documental para ello. Si el guion muestra parpadeo durante los 10 s, eliminarlo.

---

## Q4 — Perilla de sensibilidad: que mostrar al instalador

**Respuesta: SI con rango documentado. El ajuste por conductividad es real pero no tiene tabla de referencia en los documentos.**

**Rango documentado:**

La tabla de especificaciones mas completa y coherente es la de HDE V4 y GLA R V2:

- HDE V4: "Impedancia de activacion: Ajustable 2,5 K a 100 K Ohm"
- GLA R V2: "Impedancia de activacion ajustable: 2,5 a 300 kOhm" (rango ampliado en version mas reciente)

El rango final publicado es 2,5 kOhm a 300 kOhm (GLA R V2, version mas reciente de la tabla de specs).

**Procedimiento documentado (MAN V3 / MAN V3 IMP):**

1. Verificar que la perilla este alineada con el valor sugerido (punta de flecha blanca).
2. Con sondas ya cubiertas por el liquido, esperar 10 segundos.
3. Si enciende el LED verde: ajuste correcto, no tocar.
4. Si NO enciende el LED verde: aumentar sensibilidad (girar hacia mayor sensibilidad).
5. Repetir esperando 10 s cada vez que se ajuste.

**Relacion con conductividad del agua del pozo:**

Agua de pozo tiene conductividad tipicamente menor que agua de red (menos minerales disueltos) y notablemente mayor que agua destilada. A mayor resistividad del agua (menos conductora), se necesita mas sensibilidad (impedancia de activacion mas alta = perilla girada hacia valores altos). No existe una tabla de referencia agua-de-pozo vs posicion de perilla en los documentos — es un ajuste empirico en campo.

**"Muy alta" / "Muy baja":**
- Sensibilidad muy alta (impedancia de activacion baja): el rele podria activarse con condensacion en las sondas o humedad ambiental, generando falsos positivos.
- Sensibilidad muy baja (impedancia de activacion alta): el rele no detecta el liquido aunque las sondas esten sumergidas (LED verde no enciende en los 10 s de prueba).

**Para el guion:** mostrar la punta de flecha blanca como punto de partida. El mensaje al instalador: "Si con las sondas cubiertas el LED verde no enciende despues de 10 segundos, gire la perilla hacia mayor sensibilidad y espere otros 10 segundos. Repita hasta que el LED verde encienda."

---

## Q5 — Terminales clave: sanity check y omisiones del guion

**Respuesta: CONFIRMADO con una correccion de terminologia y adiciones importantes.**

### Terminales — confirmacion

| Terminal | Funcion en vaciado 2 niveles | Estado en KB                              |
|----------|------------------------------|-------------------------------------------|
| T1       | Sonda MAX                    | Confirmado en todos los manuales y HDE    |
| T2       | Sonda MIN                    | Confirmado en todos los manuales y HDE    |
| T3       | Alimentacion (A1/Fase 1)     | Confirmado en todos los manuales          |
| T4       | Alimentacion (A2/Fase 2)     | Confirmado en todos los manuales          |
| T5       | Sonda de referencia (REF)    | Confirmado en todos los manuales          |
| T6       | Contacto NC (no usar en vaciado) | Confirmado — en vaciado se usa T8 NA  |
| T7       | Contacto Comun (C)           | Confirmado — voltaje a controlar          |
| T8       | Contacto NA                  | Confirmado — carga / contactor de bomba   |

**Correccion de terminologia del brief:**
El brief dice "T8 (NA, abre cuando rele apaga bomba)." Es correcto el comportamiento, pero tecnicamente: T8 es el contacto NA — CIERRA cuando el rele se activa (bomba ON) y ABRE cuando el rele se desactiva (bomba OFF). En vaciado la bomba esta ON cuando el nivel supera MAX y OFF cuando cae bajo MIN. No es un error critico en el guion, pero la descripcion debe ser precisa para el instalador: "T7 alimenta la bobina del contactor; T8 cierra el circuito cuando el rele activa la bomba."

**Adiciones que el guion deberia incluir y que tipicamente se omiten:**

1. **Orientacion de la sonda de referencia:** debe quedar siempre sumergida (es la referencia de masa electrica del circuito de deteccion). En aplicacion de pozo: la sonda REF (T5) debe estar instalada en el punto mas bajo del pozo, por debajo de MIN. Si REF queda fuera del agua, el circuito de deteccion pierde la referencia y el rele puede comportarse erroneamente.

2. **Distancia maxima entre sondas y tablero:** HDE V9 menciona este parametro en su tabla de especificaciones pero no publica el valor (celda vacia). HDE V4 tampoco lo cuantifica. No hay valor documentado en la KB. FLAG DE ESCALACION: Confirmar con ingenieria la distancia maxima de cableado entre sondas y el GRN-MV — relevante para instalaciones de pozo profundo donde el tablero queda lejos del nivel del agua.

3. **Distancia minima entre sondas:** HDE V9 menciona "Distancia maxima entre sonda de referencia y sonda de nivel maximo" en la tabla de especificaciones sin valor. GLA T V1 REV3 menciona una separacion minima recomendada de 2 mm (pero este dato corresponde al empaque/blister del producto, no a las sondas en campo). FLAG DE ESCALACION: Confirmar separacion minima fisica entre sondas en campo.

4. **Tipo de sondas:** MAN REV3 y GLA R V2 mencionan "Electrodos Exceline especialmente seleccionados para este rele (disponibles por separado)." El guion deberia aclarar que las sondas son accesorios separados y que el instalador debe usar sondas apropiadas para agua de pozo (material resistente a corrosion).

5. **Aplicacion de llenado vs vaciado — conexion de salida:** para evitar confusion futura, el guion debe dejar claro que en vaciado la carga va en T8 (NA). En llenado la carga va en T6 (NC). El GRN-MV no tiene selector fisico de modo — el modo se define por como se conecta la salida. Esta distincion no es obvia para un instalador nuevo.

---

## Resumen de flags de escalacion a ingenieria de Genteca

| # | Pregunta de escalacion                                                                 | Impacto en guion       |
|---|----------------------------------------------------------------------------------------|------------------------|
| E1 | Hay retardo operativo de rele (activacion/desactivacion) en ciclo normal? Valor?       | Alto — escena del contador |
| E2 | El retardo (si existe) es simetrico para MAX (bomba ON) y MIN (bomba OFF)?             | Alto — escena del contador |
| E3 | Hay revalidacion de sondas con retardo post-apagon?                                    | Medio — escena de corte de luz |
| E4 | Distancia maxima de cableado sonda-tablero                                              | Bajo — nota tecnica de instalacion |
| E5 | Separacion minima entre sondas en campo                                                 | Bajo — nota tecnica de instalacion |

**Prioridad para el guion:** E1 y E2 son bloqueantes para la escena del contador. E3 es deseable. E4 y E5 son opcionales para el nivel de detalle de un video de instalacion.

---

## Divergencias entre documentos

| Parametro                 | HDE V4          | GLA R V2        | GLA T V1 REV3 (corrupto) | Resolucion                    |
|---------------------------|-----------------|-----------------|--------------------------|-------------------------------|
| Impedancia de activacion  | 2,5K - 100K Ohm | 2,5 - 300 kOhm  | 2,5 a 300 kOhm           | GLA R V2 (mas reciente): 300K |
| Voltaje max electrodos    | 38 V~           | 12 V~           | Dato desplazado (5-300s) | Discrepancia real — ESCALAR   |
| Corriente max electrodos  | 1 mA            | 1 mA            | Dato desplazado          | 1 mA consistente              |
| Capacidad contactos       | 3,5 A @ 250 V~  | 3,5 A @ 250 V~  | 16 A / 1,5 HP @ 120V     | Discrepancia — ESCALAR        |
| Peso                      | 0,179 Kg        | 0,098 Kg        | Dato desplazado          | Discrepancia real             |
| Dimensiones               | 98,5x40,8x53,2  | 60x100x38,9     | Dato desplazado          | MAN REV3: 88x51 mm — ESCALAR  |

Nota: La tabla de GLA T V1 REV3 tiene los valores corridos una fila respecto a los parametros — no usar directamente. La HDE V9 (version mas reciente de la HDE) tiene la tabla de especificaciones tecnicas completamente vacia, lo que impide usarla como fuente de verdad para valores numericos. Esto es una brecha de documentacion que deberia corregirse.

**Discrepancia critica para el video:** Voltaje maximo en los electrodos (38 V~ en HDE V4 vs 12 V~ en GLA R V2) — no impacta el guion del video pero si la seleccion de sondas y el cableado. Escalar a ingenieria.

---

## OWNER OVERRIDE — 2026-05-10

El Owner (Raoul) confirma por conocimiento directo del producto que la documentacion en KB esta desactualizada en dos puntos relevantes para el guion. Los hallazgos de Vera son correctos como diagnostico de la documentacion pero NO son la verdad operativa del producto. Las siguientes correcciones son autoritativas para el guion v2.1 y para futuras consultas.

Fechas de los documentos revisados:
- HDE V9: ultima modificacion 11-mar-2025 (pre-julio 2025 → desactualizada per criterio del Owner)
- MAN REV3: ultima modificacion 20-feb-2025 (pre-julio 2025 → desactualizada)
- MAN V3: ultima modificacion 23-oct-2025 (post-julio 2025, pero igual no documenta los puntos siguientes en el contexto correcto)

### Correccion 1 — Tiempo de deteccion 10 s: UN solo mecanismo (ANULA respuesta Q1)

**Verdad operativa segun Owner (refinado 2026-05-10):**

Los 10 segundos son UN UNICO mecanismo de retardo operativo del rele, NO dos conceptos separados. Funcion del retardo: descartar falsos positivos en la deteccion de las sondas causados por OLEAJE / turbulencia / salpicaduras / inestabilidad transitoria del nivel del liquido.

**Comportamiento unificado:**

El rele espera 10 segundos despues de cualquier cambio de estado de una sonda (sumergida → sin liquido, o sin liquido → sumergida) antes de actuar sobre la salida (encender o apagar la bomba). Este retardo aplica siempre:

- En la transicion MAX (subida del nivel toca MAX → el rele espera 10 s antes de encender la bomba).
- En la transicion MIN (bajada del nivel deja MIN sin liquido → el rele espera 10 s antes de apagar la bomba).
- En el procedimiento de calibracion de sensibilidad (las sondas pasan de sin liquido a sumergidas durante la prueba → el LED verde no se ilumina hasta cumplirse los 10 s de estabilizacion).

**Reframe de la respuesta Q1:**

La interpretacion original de Vera ("los 10 s solo aparecen en calibracion, no en ciclo operativo") fue incorrecta por una razon de framing: la doc menciona los 10 s exclusivamente en el contexto del ajuste de sensibilidad porque ese es el momento en que el instalador necesita conocer explicitamente el comportamiento — para no concluir prematuramente que la sensibilidad esta mal ajustada cuando en realidad el rele solo esta esperando estabilizacion. Pero el mecanismo subyacente (10 s de validacion tras cambio de estado de sonda) opera siempre, no solo en calibracion.

**Estado documental:**

- La existencia de los 10 s SI esta en MAN V3 y MAN V3 IMP (citado literalmente en Q1 original).
- Lo que NO esta documentado es: (a) que aplica al ciclo operativo de vaciado/llenado, no solo a calibracion; (b) su funcion como anti-falsos-positivos por oleaje/turbulencia; (c) que es simetrico en ambas transiciones.

**Para el guion:** mantener el contador 1→10s visible en pantalla en ambas transiciones (Escenas 5 y 7). En Escena 10 (ajuste de sensibilidad), aclarar que son el MISMO retardo, no un concepto distinto. La voz en off de Escena 5 ya cita correctamente "turbulencia o salpicaduras" como causa.

### Correccion 2 — Memoria de tarea (ANULA Q2 parcialmente)

**Verdad operativa segun Owner:** El GRN-MV memoriza el ESTADO DEL RELE al momento del corte de tension. Hay dos estados posibles que se memorizan:

1. **Estado "mandando arrancar la bomba":** el rele estaba enviando senal de activacion al contactor de la bomba (en vaciado, eso significa que el nivel del pozo estaba sobre MAX y la bomba estaba extrayendo agua).
2. **Estado "esperando recuperacion de nivel":** el rele estaba esperando que el nivel del liquido cambiara para actuar (en vaciado, eso significa que el nivel estaba bajo MIN y la bomba estaba apagada esperando recarga del pozo).

Al volver la tension: el rele retoma el estado memorizado SIEMPRE Y CUANDO el estado actual de las sondas lo permita. Es decir, hay revalidacion de sondas — si la situacion cambio durante el corte (ej: el pozo se recargo mas alla de MAX durante el apagon), el rele actua segun el estado actual real, no segun el memorizado.

**Lo que NO se memoriza:** el guion no debe sugerir que el rele "recuerda" cosas mas alla del estado del comando (start signal / waiting). No memoriza el tiempo transcurrido, no memoriza el conteo de los 10 s en progreso, no memoriza posiciones intermedias.

**Configuracion vs memoria — aclaracion del Owner:**
- La CONFIGURACION (vaciado vs llenado) se define por como se conecta la salida fisicamente al contacto NA (T8) o NC (T6). No es algo que el rele "decida" — es como esta cableado.
- En vaciado de pozo, la bomba esta DENTRO del pozo y extrae agua hacia afuera. Cuando el nivel del pozo baja mucho, la bomba se apaga para esperar recarga. El video es de esta aplicacion.
- En llenado, la bomba esta a la entrada de un tanque, llenandolo desde un suministro externo. (Este caso no aplica al video, solo se menciona como contraste si Nerea decide incluirlo).

**Para el guion:** la escenificacion correcta de la memoria de tarea es:
- Mostrar el rele en estado "comando bomba ON" (bomba extrayendo agua del pozo).
- Cortar la luz → todo apagado.
- Volver la luz → el rele recuerda que estaba en estado "comando bomba ON", revalida sondas (sigue habiendo agua sobre MAX), y vuelve a enviar la senal de arranque a la bomba.
- O variante: mostrar el rele en estado "esperando recuperacion" (bomba apagada, nivel bajo MIN). Corte de luz. Vuelve la luz → el rele recuerda que estaba esperando, revalida sondas (sigue bajo MIN), sigue esperando.

### Correcciones colaterales

- Las escalaciones E1, E2 y E3 quedan CERRADAS con palabra del Owner. Persisten E4 y E5 (distancias) como escalaciones a ingenieria para futura revision tecnica de docs, pero no son bloqueantes para el video.
- La interpretacion de Q3 (LEDs), Q4 (perilla) y Q5 (terminales) permanece valida — el Owner no las contradijo.
- La interpretacion de Q5 sobre la sonda REF en el punto mas bajo del pozo permanece valida y es la guia para Nerea.
