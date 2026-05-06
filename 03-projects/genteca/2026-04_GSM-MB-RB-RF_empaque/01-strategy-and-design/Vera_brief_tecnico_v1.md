# Brief técnico consolidado — Innovaciones GSM-MB / RB / RF / RE
**Documento:** Vera_brief_tecnico_v1  
**Fecha:** 2026-05-03  
**Elaborado por:** Vera (domain-specialist Genteca)  
**Dirigido a:** Vael, Bruna, Solenne, Junta Directiva (lectura transversal)  
**Workstream:** WORKSTREAM_v5_innovaciones — Paso 2 del pipeline CSC  
**Fuentes consumidas:** Comentarios sobre las innovaciones (Owner), Chat WhatsApp Canudas 02-05-2026, Transcripción reunión 29-04-2026 + acta, 8 archivos specs-i-d (datasheets GSM-RE / GSM-RECS + 6 etiquetas/instrucciones línea GSM-RE)

---

## 1. Sensor NTC — Verificación técnica

### 1.1 Qué es un termistor NTC

NTC significa "Negative Temperature Coefficient" (coeficiente de temperatura negativo). Es un componente electrónico cuya resistencia eléctrica disminuye a medida que su temperatura aumenta. Esta propiedad permite utilizarlo como sensor de temperatura: cuando el NTC se calienta, su resistencia cae, lo que modifica la señal de voltaje que entrega a un circuito de control. El circuito de control detecta ese cambio y puede disparar una acción — en este caso, abrir el relé de potencia y desconectar la carga.

El comportamiento es continuo y proporcional: el NTC "informa" en todo momento cuánto calor hay en su entorno. El disparo de protección ocurre cuando la temperatura supera un umbral definido por diseño, punto en el que la reducción de resistencia es suficiente para que el circuito de control ordene la desconexión.

**Verificación externa:** La mecánica descrita es consistente con la práctica estándar de aplicación de NTC para protección térmica en electrónica de potencia. El NTC actúa como sensor en un divisor de voltaje; la señal resultante es leída por el microcontrolador o circuito comparador, que ejecuta la desconexión al superarse el umbral. (Fuentes: TDK Application Note — NTC Thermistors; Electronics Tutorials — Thermistors and NTC Thermistors.)

### 1.2 Ubicación dentro del producto

Según el Owner (Comentarios sobre las innovaciones): el sensor NTC está ubicado junto al relé de potencia que maneja la carga, dentro del protector. Esta es la posición técnicamente correcta: el relé de potencia es el elemento que conduce la corriente de la carga y, por tanto, el que sufre mayor calentamiento cuando circulan corrientes excesivas. Colocar el NTC adyacente al relé maximiza la sensibilidad del sensor ante el calor que el propio relé genera.

No hay información en los datasheets publicados (GSM-RE, GSM-RECS) que especifique la ubicación interna del NTC, lo cual es normal: esos documentos son de especificaciones de usuario, no de diseño interno. La ubicación declarada por el Owner es coherente con la práctica de diseño y con el mecanismo de protección descrito.

### 1.3 Qué protege exactamente

**a) Al protector mismo — el relé de potencia**

Cuando la corriente que circula por el relé supera el valor para el que fue diseñado, el relé se calienta. Si el calentamiento se prolonga, puede llegar a un punto de destrucción (fusión de contactos, daño en la bobina). El NTC detecta ese calentamiento y dispara la desconexión antes de que se produzca el daño irreversible. Esta es la función primaria y más directa del NTC: autoprotección del protector mismo.

Canudas (WhatsApp 02-05-2026) lo describe con precisión: "protege al protector y al cableado de una condición de trabajo para la cual no fueron diseñados: un calor excesivo que puede llevar a la destrucción de estos."

**b) Al cableado de instalación (sobrecorrientes prolongadas)**

El cableado que alimenta la carga debe estar dimensionado para la corriente nominal de esa carga más un margen de sobrecarga normal. Si por cualquier causa circula una corriente excesiva — rotor trabado, rodamientos dañados, carga sobredimensionada — el cableado también se calienta. Al cortar la corriente mediante el NTC (vía el relé), se protege indirectamente ese cableado de una situación de sobrecorriente prolongada que podría generar calentamiento y eventualmente un incendio.

**c) Por convección, ante bornes flojos / falsos contactos**

Si hay bornes flojos o conexiones en mal estado en el propio protector, se produce un punto caliente por resistencia de contacto elevada. Ese calor se transfiere por convección hasta el sensor NTC. El Owner señala que este mecanismo es más indirecto: el NTC puede dispararse ante ese calor ambiental dentro del equipo, pero la cadena causal es más larga (borne flojo → punto caliente → convección → NTC → disparo). Esta capacidad existe pero no debe presentarse como la función principal del NTC.

Los datasheets existentes (GSM-RE y GSM-RECS, página 2/2, sección "Información de seguridad") ya advierten: "Revise su enchufe y tomacorriente. Si están flojos o en mal estado se produce una mala conexión y pueden dañar el protector y el equipo doméstico a proteger." Esto es coherente: la protección por convección ante bornes flojos es un respaldo parcial, no un sustituto de una instalación correctamente apretada.

### 1.4 Qué NO protege el NTC

**La carga conectada (motor, compresor, electrónica inverter) no queda protegida térmicamente de forma directa en todos los casos.**

La lógica es la siguiente: el NTC dispara cuando el relé se calienta lo suficiente. El relé se calienta cuando la corriente que circula por él es suficientemente alta y se sostiene el tiempo necesario para acumular calor. Esto ocurre cuando la carga demanda una corriente cercana al límite nominal del protector.

Canudas lo explica (WhatsApp 02-05-2026): "Si la carga es de 20 A, evidentemente funcionará como una protección contra sobrecarga, pero solo en ese valor de corriente. Para cargas inferiores no califica como una protección contra sobrecarga."

El analogía que usa Canudas es precisa: es equivalente a tener un térmico electromecánico ajustado para proteger un motor de 20 A. Funciona como protección de sobrecarga para cargas que alcanzan ese nivel de corriente. Para cargas pequeñas, la corriente que circula por el relé no genera suficiente calor para que el NTC dispare.

**Por tanto:**
- Carga grande (cercana a los nominales del protector, aprox. 20 A): el NTC actúa como protección de sobrecarga. Al proteger el relé y cortar la corriente, también protege indirectamente la carga y la instalación.
- Carga pequeña: el NTC protege al protector y al cableado ante el calor que el propio relé genere, pero no actuará como protección contra sobrecarga de esa carga pequeña porque la corriente que ella demanda no genera suficiente calor en el relé.

### 1.5 Validación del rango de corriente: ¿20 A aplica a todos los modelos?

De los datasheets verificados en specs-i-d:

| Modelo | Voltaje nominal | Carga máxima | Fuente |
|---|---|---|---|
| GSM-RE120A | 120 V~ | 20 A / 1 HP | GSMRE220MS.pdf (instrucciones) + datasheet GSM-RE |
| GSM-RE220M | 220 V~ | 20 A / 3.0 HP | GSMRE220MS.pdf (instrucciones) + datasheet GSM-RE |
| GSM-RE220CS | 220 V~ | 16 A / 3.0 HP | GSMRE220CS.pdf (instrucciones) |
| GSM-RE220C (variante toma china) | 220 V~ | 16 A / 3.0 HP | GD-INJ-258-02-V2-E.pdf |

**Observación importante:** El datasheet GSM-RECS indica "3 HP, 16 A @ Cosj=1" como capacidad de salida, mientras que el modelo GSM-RE220M (NEMA 6-15) indica 20 A. Las referencias a "≈ 20 A" de Canudas aplican a los modelos con relé de 20 A (GSM-RE220M, GSM-RE120A). El modelo con toma china (GSM-RE220CS / GSM-RE220C) tiene capacidad de 16 A.

**Para los modelos GSM-MB, GSM-RB, GSM-RF** que son el scope de este workstream: los datasheets de esos modelos específicos no están en el lote de specs-i-d proporcionado. El lote disponible cubre exclusivamente la subfamilia GSM-RE. La referencia de Canudas a "GSMRB (junto a sus segmentaciones) y GSMRE" y a cargas de "2 HP (220VAC) y 1 HP (120VAC)" sugiere que los nominales son similares a los RE, pero la confirmación exacta para MB/RB/RF requiere sus propios datasheets. **Pendiente — ver sección 5.**

### 1.6 Validación de temperatura ambiente máxima 55 °C

Canudas menciona: "trabajando a una temperatura ambiente máxima de 55 Celsius".

El datasheet GSM-RE (página 2/2, especificaciones técnicas) documenta explícitamente: **"Temperatura de operación: -5 a +55 °C"**. El mismo dato aparece en el datasheet GSM-RECS. El dato de 55 °C como límite máximo de temperatura ambiente está respaldado por los documentos de specs publicados.

**Conclusión sección 1:** El sensor NTC es una capa de autoprotección térmica del protector y de la instalación. Es técnicamente correcto denominarlo "autoprotección térmica". No es ni reemplaza a un protector térmico de motor. El copy "Sensor NTC incorporado*" con asterisco que derive al retiro es la formulación más honesta y defendible.

---

## 2. Tiempo de respuesta < 30 ms — Verificación técnica

### 2.1 Qué es un "parpadeo" o flicker

En calidad de energía eléctrica, un parpadeo (flicker) es una variación rápida y transitoria del voltaje de la red — habitualmente dentro del rango de ±10 % respecto al voltaje nominal — que se repite con suficiente frecuencia o intensidad como para ser perceptible o perjudicial. La IEC (norma IEC 61000-4-15, referenciada en IEC 61000-3-3) lo define técnicamente como la "impresión de inestabilidad de la sensación visual inducida por un estímulo luminoso cuya luminancia fluctúa con el tiempo".

En el contexto de supervisores de voltaje para equipos de refrigeración y aire acondicionado, un parpadeo es una caída o elevación breve del voltaje de la red (duración de milisegundos a pocos ciclos) que puede causar la desconexión y reconexión inmediata del equipo. Para compresores, esta secuencia rápida de apagado/encendido es muy dañina: el compresor intenta arrancar contra la presión de refrigerante aún presente en el sistema (el refrigerante no tuvo tiempo de redistribuirse), lo que genera un esfuerzo mecánico extremo — rotor casi trabado — y corrientes de arranque muy elevadas y sucesivas.

**Distinción respecto a transientes:** Un transiente de alta energía (IEC 1000-4-5, norma bajo la cual está verificado el GSM-RE) es un pico de voltaje de muy corta duración (microsegundos a pocos milisegundos) y de muy alta amplitud, producido por descargas atmosféricas o conmutación de cargas inductivas. El GSM-RE ya incluye un supresor de picos de 410 joules para manejar ese fenómeno. El tiempo de respuesta de < 30 ms es relevante para el fenómeno de parpadeo (flicker), no para transientes: los transientes se mitigan con el supresor MOV/varistor, no con la velocidad de respuesta del relé.

### 2.2 La mejora de 150 ms a < 30 ms: qué abarca exactamente

Los datasheets actuales de la línea GSM-RE (versiones publicadas en specs-i-d) especifican:

- "Tiempo de desconexión ante parpadeos (flickers) e inestabilidad: **150 milisegundos**"

Este es el valor de la generación anterior del producto. La innovación consiste en reducir ese tiempo de desconexión a **menos de 30 ms**.

En términos técnicos, el "tiempo de desconexión" en este contexto es el tiempo transcurrido entre la detección de la condición de falla (parpadeo / inestabilidad) y la apertura efectiva del relé de potencia que desconecta la carga. Es la cadena completa: detección + procesamiento + actuación del relé.

**¿Aplica solo a parpadeos o también a sobre/subtensión?**

Los datasheets hacen una distinción explícita entre dos tiempos:
1. "Tiempo de desconexión ante fallas voltaje bajo y alto: entre 0,4 y 3 segundos de acuerdo a la intensidad de la falla."
2. "Tiempo de desconexión ante parpadeos (flickers) e inestabilidad: 150 milisegundos."

La mejora de 150 ms a < 30 ms aplica al segundo parámetro, es decir, a la detección de parpadeos e inestabilidad. No hay evidencia en el material disponible de que el tiempo de desconexión ante sobre/subtensión severa (el parámetro de 0,4 a 3 s) haya cambiado. Esta distinción es importante para el copy: la frase "El más rápido ante parpadeos (< 0,03 s)" está bien acotada.

### 2.3 ¿Es "< 30 ms" o "< 0,03 s"? ¿Hay un valor típico medido?

Las dos formulaciones son equivalentes matemáticamente: 30 ms = 0,03 s. La versión "< 0,03 s" fue acordada por Canudas y el Owner en el chat del 02-05-2026 ("El más rápido ante parpadeos (< 0,03 s)"). Es la formulación para empaque.

Respecto a si existe un valor típico medido (ej. 25 ms, 28 ms): la materia prima disponible solo confirma el threshold "< 30 ms" mencionado en la reunión del 29-04-2026. No hay en los datasheets actuales ni en la transcripción un valor de medición específico documentado. El Owner indica que la mejora viene de I&D. El dato oficial verificable para empaque es el umbral "< 30 ms / < 0,03 s".

**Estado:** El valor "< 30 ms" como especificación de la nueva versión no aparece aún en los datasheets publicados — los datasheets en specs-i-d corresponden a la versión anterior (150 ms). Eso es esperado si los datasheets aún no fueron actualizados con las nuevas especificaciones. **Los datasheets deben actualizarse antes o simultáneamente al lanzamiento del empaque nuevo. Pendiente — ver sección 5.**

### 2.4 Por qué la velocidad importa para tecnología inverter — explicación técnica

Los equipos de aire acondicionado y refrigeración con tecnología inverter utilizan un variador de frecuencia electrónico para controlar la velocidad del compresor, en lugar de arrancar y parar el motor a velocidad fija. Esto implica que la tarjeta de control del inverter está activa constantemente gestionando la alimentación al motor.

La electrónica de control inverter es sensible a la forma de onda de la alimentación: necesita una señal de voltaje estable para operar correctamente. Un parpadeo (caída y recuperación rápida del voltaje) puede causar dos problemas en equipos inverter:

1. **Inestabilidad en el bus de continua interno del inverter:** la tarjeta del inverter rectifica el voltaje AC a DC para generar la señal de frecuencia variable. Una caída brusca de voltaje AC afecta ese bus DC y puede causar errores o disparos del propio sistema de protección del inverter.
2. **Ciclos de arranque sucesivos muy rápidos:** si el protector de voltaje no responde con suficiente velocidad ante un parpadeo, la carga puede reconectarse y desconectarse en ciclos cortos antes de que el protector haya tenido tiempo de actuar limpiamente. Cada arranque de un compresor de inverter implica una corriente de arranque significativa; ciclos sucesivos agotan y pueden dañar los componentes de potencia.

Una respuesta de < 30 ms garantiza que el protector detecta el parpadeo y abre el circuito en menos de dos ciclos de red (un ciclo de 60 Hz dura ~16,7 ms), minimizando la exposición del equipo a la condición inestable.

**El caveat del Owner (verificado como correcto técnicamente):** Los picos de alta energía (transientes por descarga atmosférica o conmutación inductiva) son un problema diferente. La mayoría de equipos inverter ya incluyen protección contra esos transientes de fábrica (varistores MOV en la placa de control). El valor del tiempo < 30 ms no está dirigido a esos transientes — para esos existe el supresor de 410 J ya presente en el GSM-RE. El valor de < 30 ms aporta específicamente ante parpadeos y ciclos de inestabilidad que la protección de fábrica del inverter no maneja: son fenómenos de duración más larga (decenas de milisegundos a segundos) pero de amplitud menor.

**Síntesis técnica para el copy:** La frase "Protege tecnología Inverter" se sustenta en que el tiempo de respuesta ultrarrápido ante parpadeos reduce la exposición de la electrónica inverter a condiciones de inestabilidad de red. El claim no aplica a protección contra picos de alta energía (eso es el supresor, no la velocidad de respuesta del relé). Esa distinción debe estar clara en el material del QR y en el argumentario de ventas, pero no necesita resolverse en el empaque.

---

## 3. Coherencia con datasheets I&D

### 3.1 Contradicciones entre el copy propuesto (Alternativa A) y los datasheets actuales

**Frase 1 — "El más rápido ante parpadeos (< 0,03 s)"**

Los datasheets en specs-i-d especifican 150 milisegundos como tiempo de desconexión ante parpadeos e inestabilidad. El copy propuesto afirma < 0,03 s. Hay una discrepancia directa entre el copy nuevo y los datasheets actuales. Esto no es un error del copy — es consecuencia de que los datasheets no han sido actualizados para reflejar la nueva generación del producto. Esta discrepancia puede generar problemas si alguien contrasta empaque vs. hoja de especificaciones.

**Acción requerida (ver sección 5):** Los datasheets deben actualizarse para reflejar el nuevo tiempo de desconexión ante parpadeos antes de que el empaque entre en producción.

**Frase 2 — "Protege tecnología Inverter"**

Los datasheets actuales no mencionan explícitamente compatibilidad con tecnología inverter. No hay contradicción directa (el datasheet no dice que NO protege inverter), pero tampoco hay respaldo afirmativo en los documentos publicados. Según la transcripción del 29-04-2026, el claim de compatibilidad inverter ya estaba en la etiqueta del producto desde 2018 (Raoul: "vi por casualidad en una etiqueta en el año 2018... para este equipo es compatible inverter"). Sin embargo, ese claim no aparece en los datasheets del lote disponible.

**Frase 3 — "Sensor NTC incorporado*"**

No hay mención del NTC en ninguno de los datasheets del lote. Los datasheets corresponden a la versión anterior del producto. El asterisco con explicación en el retiro es la mecánica correcta para introducir este claim sin contradicción formal con los datasheets existentes. Pero los datasheets deberán actualizarse.

**Lengüeta — "Nuevo. La Protección más completa"**

No contradice nada en los datasheets. Es un claim de posicionamiento, no de especificación técnica. Sin conflicto.

### 3.2 Datos en los datasheets que el copy debería incorporar (o no contradecir)

- **Carga máxima 20 A (modelos NEMA) / 16 A (modelos toma china):** el empaque no menciona límite de carga. No es necesario en el tiro, pero el retiro debe incluir referencia al nominal máximo del modelo específico para que el NTC quede correctamente encuadrado.
- **Temperatura de operación -5 a +55 °C:** el dato de 55 °C de Canudas está respaldado. No se necesita en el tiro pero puede usarse en el material del QR.
- **Supresor de picos 410 J:** esta capacidad ya existe y no cambia. No está en el copy propuesto de la Alternativa A (correcto — es una función existente, no una innovación nueva). No requiere incorporarse al tiro.
- **Tiempo de conexión inteligente 3 minutos:** tampoco cambia. No requiere mención en el copy de innovaciones.

### 3.3 Diferencias entre modelos que afectan el copy de empaque

Los cuatro modelos del scope (GSM-MB, GSM-RB, GSM-RF, GSM-RE) comparten el copy de empaque según decisión del workstream. Las diferencias relevantes entre modelos son:

- **Color de la etiqueta / empaque:** GSM-RE120A = verde; GSM-RE220M y GSM-RE220CS = azul. La línea MB/RB/RF tiene sus propios colores según decisiones previas de diseño.
- **Capacidad de corriente:** 20 A (modelos NEMA 120V y 220V) vs. 16 A (modelos toma china). Esta diferencia NO impacta el copy del tiro. Sí debe reflejarse en el retiro si se menciona el nominal de corriente como referencia para el NTC.
- **Aplicación declarada:** GSM-RE = "Aires Acondicionados y Refrigeración". Los modelos MB/RB/RF tienen sus propias aplicaciones declaradas. El copy de empaque debe mantenerse consistente con la aplicación de cada modelo — no hay conflicto con las innovaciones propuestas.
- **Compatibilidad inverter:** todos los modelos del scope la tienen. No hay diferencia por modelo en este aspecto.

---

## 4. Caveats para retiro — redacción literal lista para gate de Bruna

Los siguientes textos están redactados como podrían aparecer en el retiro del empaque (o como nota al pie del asterisco NTC). Bruna los recibe para gate de riesgo, no como texto aprobado de producción.

---

**Caveat 1 — Encuadre del NTC como capa adicional, no reemplazo del termomagnético**

> *El Sensor NTC incorporado actúa como una capa adicional de protección térmica que respalda al interruptor termomagnético de la instalación. No reemplaza al breaker ni a ninguna protección de sobrecorriente del circuito. El protector de voltaje GSM no mide corriente. La correcta selección y calibración del breaker termomagnético por parte del instalador es indispensable.*

---

**Caveat 2 — Honestidad sobre cargas pequeñas**

> *La protección térmica del Sensor NTC actúa cuando la corriente de la carga conectada se aproxima al límite nominal del protector. Para cargas de baja demanda de corriente, el Sensor NTC protege al protector y al cableado de la instalación, pero no actúa como protección de sobrecarga de la carga conectada.*

---

**Caveat 3 — Acotamiento del tiempo < 30 ms a parpadeos**

> *El tiempo de desconexión de menos de 30 milisegundos (< 0,03 s) aplica ante parpadeos (fluctuaciones rápidas del voltaje de la red eléctrica) e inestabilidad de la red. Un parpadeo es una variación breve y repetida del voltaje que puede causar ciclos de arranque sucesivos dañinos para compresores y equipos de refrigeración. Este tiempo de respuesta no aplica a la desconexión ante sobre voltaje o bajo voltaje pronunciados, cuyo tiempo de desconexión es entre 0,4 y 3 segundos según la intensidad de la falla.*

---

**Caveat 4 — Dimensionamiento del cableado como precondición**

> *Para que el Sensor NTC pueda respaldar eficazmente la protección del cableado, la instalación debe contar con conductores dimensionados correctamente para la carga conectada. Un cableado subdimensionado puede calentarse y deteriorarse antes de que el NTC alcance la temperatura de disparo. El instalador es responsable del correcto dimensionamiento del cableado según la normativa eléctrica aplicable.*

---

**Caveat 5 — Tecnología inverter: alcance de la protección**

> *La frase "Protege tecnología Inverter" se refiere a la protección ante parpadeos (flickers) e inestabilidad de red a la que los equipos con tecnología inverter son especialmente sensibles. El tiempo de desconexión de < 0,03 s minimiza la exposición de la electrónica de control inverter a esas condiciones. Este protector incluye además un supresor de picos de 410 joules ante transientes de alta energía. La protección contra transientes de fábrica incluida en muchos equipos inverter y la protección ante parpadeos de este protector son complementarias.*

---

## 5. Pendientes para I&D / fuentes — lista de puntos no verificables con la materia prima disponible

| # | Pendiente | Quién debe resolver | Impacto en empaque |
|---|---|---|---|
| P-1 | Datasheets de GSM-MB, GSM-RB y GSM-RF no están en el lote specs-i-d. No se pudieron verificar nominales de corriente, temperatura de operación ni especificaciones publicadas para esos tres modelos. | I&D Genteca / Raoul solicitar a laboratorio | Alto. Si los nominales de MB/RB/RF difieren de los RE, el copy de caveats y retiro debe ajustarse por modelo. |
| P-2 | El tiempo de desconexión de < 30 ms ante parpadeos no está documentado en ningún datasheet del lote (los actuales dicen 150 ms). Para que el claim sea auditable frente a terceros, I&D debe emitir una especificación actualizada que documente el nuevo valor. | I&D Genteca — laboratorio | Alto. El empaque nuevo y el datasheet no pueden quedar desincronizados en producción. |
| P-3 | No hay valor típico medido (ej. 25 ms, 28 ms) en la materia prima disponible. El claim oficial es el umbral "< 30 ms". Si I&D puede aportar un valor típico medido en banco de pruebas, fortalece el argumento técnico. | I&D Genteca — laboratorio | Medio. El claim "< 30 ms" es defendible como umbral; el valor típico fortalecería pero no es indispensable. |
| P-4 | La mención de compatibilidad inverter ("Protege tecnología Inverter") no aparece en los datasheets actuales del lote. Si existió en una etiqueta anterior (2018, según transcripción), ese documento no está en el lote. Confirmar la trazabilidad documental de ese claim. | Raoul / Keiddys — archivo histórico de etiquetas | Medio. Bruna necesitará esa trazabilidad para el gate. |
| P-5 | El NTC y su umbral de disparo (temperatura de disparo del circuito de control) no están documentados en los datasheets públicos. Para el QR y el argumentario de ventas, sería útil tener esa especificación (ej. "dispara a X °C en la superficie del relé"). | I&D Genteca — laboratorio | Bajo para empaque. Alto para contenido QR y argumentario. |
| P-6 | Comparativo de tiempo de respuesta vs. competidores (TQ, Protector). Acordado por Raoul y Alberto en reunión 29-04-2026 como tarea para Víctor y Luis González. No es insumo de este workstream de empaque, pero alimenta el argumentario de ventas y respalda el superlativo "El más rápido" si Orlan lo requiere. | Orlan (análisis competencia) + Víctor / Luis González | Indirecto. Aplica a la regla de gateo de claims superlativos del workstream. |

---

## Cover note — Supuestos y alcance de este documento

**Supuestos de trabajo:**

1. Los datasheets de GSM-RE y GSM-RECS en el lote de specs-i-d son representativos de la arquitectura técnica de la familia GSM-MB/RB/RF/RE en cuanto a capacidad de corriente nominal (20 A modelos NEMA, 16 A modelos toma china) y temperatura de operación máxima (55 °C). Esta asunción es razonable dado que Canudas confirma los mismos valores para GSMRB y GSMRE, pero debe verificarse formalmente para MB/RB/RF (Pendiente P-1).

2. El valor de < 30 ms como nuevo tiempo de desconexión ante parpadeos proviene exclusivamente de la reunión del 29-04-2026 y de los comentarios del Owner. No hay, a la fecha de este brief, un datasheet actualizado que lo documente. Se asume que I&D lo tiene medido y puede emitir especificación actualizada (Pendiente P-2).

3. Los mecanismos técnicos del NTC descritos en la sección 1 se apoyan en la declaración del Owner, en la precisión de Canudas, y en fuentes técnicas externas estándar (TDK Application Notes, Electronics Tutorials). Son técnicamente correctos y consistentes entre sí.

**Lo que este brief no determina:**

- Qué claims son defendibles legalmente. Eso es Bruna (BR-1, BR-2).
- Qué formulación de copy va en el empaque. Eso es Solenne.
- Si el superlativo "El más rápido" se sostiene frente a competencia. Eso es Orlan.
- Qué va en el QR (contenido ejecutado). Eso es un workstream separado post-decisión de Junta.

**Validez de este documento:** La información técnica es válida con los datasheets vigentes a 2026-05-03. Cuando I&D emita datasheets actualizados (Pendientes P-1 y P-2), este brief debe revisarse para confirmar que las afirmaciones siguen siendo consistentes.
