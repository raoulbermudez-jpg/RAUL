# Messaging Guardrails — GME (Exceline Profesional, Protector Monofasico Inteligente)
**Fecha:** 2026-05-06
**Basado en:** OL-3 Orlan (2026-05-06) + Vera memo tecnico VE-1 v1 (2026-05-06) + Van Westendorp GME (2026-05-06) + Comentarios_tecnicos_encuesta.md + BR-5 Precedentes #1–#4 (2026-05-03) + RISK-POLICY.md v1.0 (2026-04-25)
**Producido por:** Vael — Brand & Messaging Strategist
**Para:** Bruna (gate de claims) / Solenne (limite operativo al escribir) / Aurelio (constraints de campana) / Nerea (constraints de guion)
**Estado:** PROPUESTA de categorizacion — La decision final (aprobado / aprobado con caveat literal / rechazado) es de Bruna. Sin gate explícito de Bruna, los claims marcados ⚠ y ❌ no pasan a produccion.

---

## Claims candidatos categorizados

### Claim A — "Primer protector monofasico inteligente con WiFi y medicion de voltaje y corriente a precio accesible en Venezuela / LATAM"

| Campo | Detalle |
|---|---|
| **Categoria** | ⚠ Defendible con caveat |
| **RTB disponible** | OL-3 §3 y §4 Claim A: no se encontro ningun competidor en el rango $30–60 con esta combinacion en multiples busquedas a mayo 2026. OL-3 §Limites: la cobertura del mercado chino OEM fue superficial (Limite 1). |
| **Caveat obligatorio si se usa** | Acotar geografía explícitamente: "en Venezuela" o "en LATAM" (no claim global). Acotar precio: "en este rango de precio" o "por menos de $X". No usar "primero en el mundo". La formulacion mas defensible: "el primer protector monofasico en Venezuela con medicion de voltaje y corriente, WiFi y configuracion multi-aplicacion en el rango de precio accesible." |
| **Argumento** | OL-3 clasifico este atributo como Diferenciado. El claim superlativo con dato de scope geográfico + rango de precio aplica el patron de BR-5 Precedente #1 (superlativo + dato cuantitativo propio es la formulacion mas defensible). Sin embargo, la investigacion de mercado chino OEM esta incompleta — riesgo de que exista un producto sin nombre en AliExpress con estas funciones. |
| **Gate Bruna:** | REQUERIDO antes de uso publico. Orlan debe completar la segunda iteracion del OL-3 (busqueda profunda en AliExpress) antes de que Bruna pueda aprobar el claim con solidez. |
| **Aplica BR-5** | Precedentes #1 (superlativo + dato cuantitativo) y #2 (superlativo de exclusion — el "primero" puede asimilarse al "unico"). Requiere que el scope este acotado. |

---

### Claim B — "Proteccion integral: voltaje + corriente + subcarga + arranques por hora en un solo protector monofasico"

| Campo | Detalle |
|---|---|
| **Categoria** | ⚠ Defendible con caveat |
| **RTB disponible** | Pantallas GME (fuente primaria): los 4 elementos estan visibles en la UI — voltaje (U>/U<), corriente (I>/I<), subcarga (activacion + % + tiempo de deteccion), toggle de arranques por hora. Vera §4 Claim B: "Tecnicamente plausible, con condiciones." |
| **Caveat obligatorio si se usa** | Requiere que Vera reciba confirmacion de engineering de que cada funcion activa fisicamente el contactor (no solo registra el evento en pantalla). En particular: (a) subcarga dispara el contactor tras el tiempo de deteccion confirmado, (b) el contador de arranques/hora funciona correctamente en rolling window o ciclo configurado. Vera §4 Claim B: "el equipo de firmware debe confirmar que cada funcion activa fisicamente el contactor." |
| **Riesgo adicional critico** | La logica de "tres intentos antes de bloqueo" confirmada en los mockups (log muestra "Off Tercera falla de Sobrecarga" / "Off Tercera falla de Subcarga") debe comunicarse explicitamente en la documentacion de producto. Si el GME hace dos reintentos antes de bloquear, un usuario puede pensar que el equipo no respondio al primer evento. El claim de "proteccion integral" debe coexistir con la explicacion de la logica de reintentos. |
| **Argumento** | El conjunto V+I+subcarga+arranques/hora no existe en ningun competidor del rango $30–60 (OL-3 §4 Claim B). El claim es funcionalmente unico en su nicho de precio una vez que engineering confirme la implementacion. |
| **Gate Bruna:** | REQUERIDO. Ademas de la confirmacion de engineering, Bruna debe revisar si la logica de "tres intentos" genera exposicion de responsabilidad (Vera §4 Claim B, Bruna §Proximos pasos). |

---

### Claim C — "Sin app que instalar. Sin cloud requerida."

| Campo | Detalle |
|---|---|
| **Categoria** | ⚠ Defendible con caveat (condicion tecnica critica pendiente) |
| **RTB disponible** | URL 192.168.0.21 visible en todas las capturas del GME. Vera §4 Claim C: "Tecnicamente plausible para la interfaz — condicion critica pendiente para la proteccion." OL-3 §3: "ningún competidor relevante a este precio usa este modelo de UI." |
| **Caveat obligatorio si se usa** | El claim "sin cloud requerida" es valido para la interfaz de usuario (configuracion y monitoreo desde browser local). Sin embargo, la pregunta critica es si la PROTECCION ACTIVA (disparo del contactor) funciona sin conexion WiFi. Si el GME requiere WiFi activo para ejecutar la logica de proteccion, el claim se convierte en "sin cloud, pero con WiFi obligatorio" — un matiz importante. Vera §5 Q2: esta es la pregunta de operacion offline, marcada como prioridad alta. |
| **Riesgo de arquitectura** | Vera §4 Claim C: "si el MCU de proteccion y el MCU del webserver son el mismo chip, un cuelgue del webserver podria dejar la proteccion inactiva." Si esto es cierto, el claim "sin cloud" tiene una vulnerabilidad de arquitectura subyacente que va mas alla del mensaje. |
| **Argumento** | El modelo de webserver local es un diferenciador real frente a Tuya (dependencia de cloud confirmada en OL-3) y Shelly (cloud opcional pero presente). Una vez que engineering confirme la operacion offline, este es uno de los claims mas solidos del portafolio GME. |
| **Gate Bruna:** | REQUERIDO. Sujeto a confirmacion de engineering (Vera §5 Q2 y Q3). Hasta que llegue esa respuesta, el claim no debe usarse en materiales publicos. Puede usarse en presentaciones internas y argumentario de ventas con la caveat explicita. |

---

### Claim D — "Conoce el estado de tu equipo desde el telefono"

| Campo | Detalle |
|---|---|
| **Categoria** | ✅ Defendible — con alcance acotado a red local |
| **RTB disponible** | Pantalla de mediciones GME: voltaje, corriente, frecuencia, estado del rele, entrada digital, ultima falla — todo visible desde el browser en la misma red WiFi. Vera §4 Claim D: "Defendible — acotar a red local." |
| **Condicion de uso** | El lenguaje debe especificar el alcance: "desde cualquier browser en la misma red WiFi" o "mientras estes en la red del equipo". No usar "desde cualquier lugar", "remotamente", "en tiempo real desde cualquier parte" — esas formulaciones implican acceso remoto no confirmado en el GME. |
| **Argumento** | Esta es la formulacion mas conservadora y mas inmediatamente verdadera. No requiere confirmacion adicional de engineering. Es el claim mas rapido en activar segun Vera §Proximos pasos: "Vael puede usar este claim ya, acotando explicitamente." |
| **Gate Bruna:** | No requerido para la version acotada a red local. Si en versiones futuras se amplia a acceso remoto (VPN, relay, notificaciones push), ese nuevo scope si requiere gate de Bruna. |

---

### Claim E — "Para neveras, bombas y motores — un solo protector, tres modos de aplicacion"

| Campo | Detalle |
|---|---|
| **Categoria** | ✅ Defendible — con confirmacion tecnica de implementacion |
| **RTB disponible** | Pantalla de Configuracion GME: selector R/B/M visible. Diferencias en parametros de subcarga, tiempo de reconexion y tiempo de reintento por modo documentadas en Vera §3.1. Maniobra diaria como logica exclusiva del modo B (Vera §3.2). OL-3 §3: "Configuracion multi-aplicacion (Motores/Bombas/Refrigeracion) en un solo hardware — ningún competidor a este precio segmenta por aplicacion." |
| **Condicion de uso** | Si el claim se usa en comunicacion profunda (para ingeniero de proyectos o tecnico exigente), debe poder respaldarse con la pregunta "que cambia exactamente entre modos". La respuesta correcta en el estado actual de conocimiento: "Los parametros default cambian segun la logica de cada aplicacion (tiempos de subcarga, umbrales de reintento, reconexion) y hay funciones exclusivas por modo (maniobra diaria en Bombas, tiempo de deteccion de sobrecarga en Motores)." No afirmar que el "codigo de firmware" es radicalmente diferente entre modos — eso no esta confirmado y puede debilitarse si engineering responde que es el mismo motor con distintos defaults. |
| **Argumento** | Este es el claim mas unico del portafolio GME. Ningún competidor identificado en $30–60 tiene esta funcionalidad. El claim es verdad funcional incluso si los modos solo cambian defaults — porque la diferenciacion de defaults segun aplicacion ya es un valor real. Vera §4 Claim E: "Defendible, con matiz." |
| **Gate Bruna:** | No requerido en su formulacion basica ("tres modos de aplicacion"). Si se agrega lenguaje de superlativo ("el unico con tres modos" o "ningún otro protector en este precio"), si requiere gate de Bruna (BR-5 Precedente #2). |

---

### Claim F — "Visibilidad total del equipo desde tu celular"

| Campo | Detalle |
|---|---|
| **Categoria** | ❌ No usar (en esta formulacion) |
| **Razon** | "Total" es afirmacion absoluta. El GME muestra V, I, Hz, estado del rele, ultima falla por tipo — pero no muestra temperatura de descarga, estado de valvulas, flujo hidraulico, temperatura de bobinado, ni historial cronologico de fallas. La visibilidad es parcial (relevante, util, diferenciadora — pero no "total"). Ademas, el alcance es red local, no "desde cualquier celular en cualquier lugar". |
| **Alternativa** | "El estado de tu equipo, en tu telefono — voltaje, corriente, frecuencia y ultima falla, en tiempo real desde la red WiFi." Especifico, verdadero, sin superlativo indefendible. |

---

### Claim G — "Tan preciso como instrumentacion profesional"

| Campo | Detalle |
|---|---|
| **Categoria** | ❌ No usar |
| **Razon** | El GME no declara clase de exactitud de medicion IEC 60255-1. Vera §1.2: "un display de 15.6 A sin tolerancia documentada es un riesgo de credibilidad tecnica." Sin clase declarada, el claim de precision es indefendible ante cualquier tecnico que pregunte la tolerancia. La instrumentacion profesional (Clase 0.2–0.5) es materialmente mas precisa que la logica de un relé de proteccion (Clase 3–5 es suficiente para actuar en el umbral). |
| **Alternativa** | No hacer claim de precision hasta que engineering declare clase de exactitud. Si declaran Clase 1 (±1% V/I), el claim posible es: "Medicion a ±1% para una lectura confiable en campo" — verdad especifica y modesta, no superlativo. |

---

### Claim H — "Proteccion que defiende lo importante: tu equipo, tu instalacion, tu negocio"

| Campo | Detalle |
|---|---|
| **Categoria** | ⚠ Defendible con caveat (en la version que no implica garantia de resultado) / ❌ No usar en version que implica garantia |
| **Razon** | Este es el equivalente directo del Claim H del proyecto empaque GSM. BR-5 Precedente #4 (2026-05-03): cualquier formulacion que implique "garantiza la proteccion del equipo" o "tu equipo estara protegido" genera obligacion legal de resultado. El GME protege ante variaciones de voltaje, sobrecarga y subcarga — no ante todos los fenomenos electricos posibles. |
| **Formulacion prohibida** | "Tu equipo estara protegido." / "Nunca mas te quedas sin equipo." / "Proteccion que garantiza la vida util de tu compresor / bomba / motor." |
| **Formulacion defendible** | "El GME monitorea las condiciones electricas y actua antes de que una sobrecarga, subcarga o variacion de voltaje danhe el equipo — segun el perfil del equipo conectado." Describe la accion, no garantiza el resultado. |
| **Gate Bruna:** | REQUERIDO si se usa cualquier formulacion que se acerque a garantia de resultado. La version descriptiva-de-accion puede usarse sin gate de Bruna. |

---

### Claim I — "La inteligencia que el ESP32 hace posible"

| Campo | Detalle |
|---|---|
| **Categoria** | ❌ No usar (como claim de marketing externo) |
| **Razon** | Mencionar el componente interno del producto activa la objecion de precio que el Informe VW ya anticipo: el tecnico que sabe que un ESP32 cuesta $10 se pregunta por que paga $35 por un "ESP32 con carcasa". El componente es un insumo interno — exponer la "cocina" del producto no es argumento de valor sino puerta de objecion. Puede usarse en conversacion tecnica con ingenieros (argumentario tecnico de que el modulo WiFi tiene certificacion FCC si se confirma que el GME usa modulo ESP32/ESP-WROOM certificado), pero no como claim de comunicacion publica. |
| **Nota adicional** | Si el modulo WiFi del GME es un ESP32 o ESP-WROOM-32 estandar, la certificacion FCC del modulo ya existe como base para la certificacion FCC del producto final (Vera §1.1). Esa es la lectura util del componente — un argumento para el equipo de ingenieria y el track de certificacion, no para el empaque. |

---

### Claim J — "Multivoltaje 120/220V"

| Campo | Detalle |
|---|---|
| **Categoria** | ❌ No usar en V1 (pendiente confirmacion de engineering) |
| **Razon** | El GME aparece como "220" en los SKUs (GME-R220, GME-B220, GME-M220). OL-3 §3 lo marca como Expuesto. Vera §5 Q10: "pendiente engineering si el hardware actual soporta 120 VAC o solo 220 VAC." Varios tecnicos lo pidieron en la encuesta (comentario #104362640: "que sea multivoltaje para que se adapte a los 120 o 220Vac"). Usar este claim sin confirmacion de hardware es sobrepromesa directa de una especificacion no confirmada. |
| **Alternativa** | No hacer claim de multivoltaje. Si engineering confirma variante 120V para el lanzamiento de octubre 2026, el claim puede habilitarse con el producto correcto. |

---

### Claim K — "Sensibilidad menor a 1 segundo ante fluctuaciones"

| Campo | Detalle |
|---|---|
| **Categoria** | ❌ No usar (pendiente confirmacion de engineering) |
| **Razon** | Tiempo de respuesta del GME ante sobre/subvoltaje: "[pendiente engineering]" en toda la tabla de Vera §2. El tecnico de refrigeracion (comentario #104359489) pidio explicitamente sensibilidad <1 s — lo que implica que su evaluacion preliminar del producto es que podria NO tenerla. Usar este claim sin el dato de engineering es sobrepromesa con un testigo que la cuestiona. |
| **Condicion de habilitacion** | Si engineering confirma tiempo de respuesta de V con dato cuantitativo (ej. "tiempo de deteccion ante subvoltaje: 200 ms"), ese dato especifico puede usarse. El claim de "<1 s" requiere que el dato verifique el threshold. Si el dato de engineering dice "2 s" (como es el default de ICM492 y Wagner DSP-1), el claim queda descartado. |

---

### Claim L — "Historial de las ultimas 20 fallas con fecha y hora"

| Campo | Detalle |
|---|---|
| **Categoria** | ❌ No usar en V1 |
| **Razon** | Los mockups del GME muestran "ultima ocurrencia por tipo de falla" — no log cronologico con 20 entradas ni timestamp de fecha y hora. Vera §2 tabla fila "Profundidad log de fallas": "Ultima ocurrencia por tipo (9 tipos) — sin timestamp cronologico." Vera §2 fila "RTC / timestamp real": "[pendiente engineering]." El pedido de 20 fallas con fecha y hora aparece en la encuesta (comentario #104362252: "que registre las ultimas 20 fallas"; comentario #104362438: "historial de las ultimas 10 a 15 fallas"). Es un feature deseable que el producto V1 no tiene. Prometer en V1 lo que no esta implementado es el antipattern central de la comunicacion de producto. |
| **Alternativa en V1** | "El GME registra el tipo de la ultima falla para cada categoria de evento — subcarga, sobrecarga, voltaje, frecuencia." Verdad verificable. Cuando el historial cronologico este implementado (roadmap), el claim se habilita. |

---

### Claim M — "Notificaciones en tiempo real"

| Campo | Detalle |
|---|---|
| **Categoria** | ❌ No usar en V1 (pendiente confirmacion) |
| **Razon** | El webserver local del GME es accedido por el usuario activamente (pull). No hay evidencia de notificaciones push (el dispositivo avisa proactivamente al telefono). El pedido aparece en la encuesta (#104359424: "alertas en la aplicacion para que se puedan reflejar las fallas en tiempo real"; #104364291: "que genere una notificacion de falla"). Es un pedido legitimo que el producto V1 no parece tener. |
| **Condicion de habilitacion** | Si engineering implementa push notifications (MQTT, webhook a mensajeria, o notificacion nativa del browser) antes del lanzamiento de octubre, el claim puede habilitarse con el scope correcto (notificacion en red local o con acceso externo configurado). |

---

## Temas sensibles transversales

### Pricing: como defender USD 35 ante el comentario "ESP32 a $10"

**El riesgo:** El tecnico sofisticado que ya conoce el ecosistema IoT puede percibir el GME como "un ESP32 con carcasa" (comentario encuesta #104356020). La objecion: "con $10 compro el componente y lo programo yo".

**La respuesta correcta de mensaje (no de negacion):** El GME no es el ESP32. El ESP32 es el componente de conectividad de un producto cuya propuesta de valor es otra: la logica de proteccion calibrada por tipo de carga (subcarga diferenciada para compresor vs bomba vs motor), el contactor integrado que actua fisicamente, la interfaz sin programacion, el soporte y la garantia de una marca local con 40 anos de trayectoria en el sector. Un ESP32 a $10 no tiene contactor, no tiene lógica de subcarga, no tiene modos de aplicacion, y el tecnico que lo instala responde ante el cliente si algo falla. El GME transfiere esa responsabilidad a Exceline.

**Formulacion de mensaje defensible (para argumentario de ventas — no para empaque):** "Un ESP32 cuesta $10 y un tornillo cuesta un centavo. La diferencia entre un producto y sus componentes es la ingenieria que los integra, la logica que los hace trabajar juntos, y la responsabilidad que asumes cuando los instalas en casa de un cliente."

**Nota para Bruna:** esta linea de argumentacion no requiere claim de superlativo — es un argumento de valor, no de posicion en el mercado. No requiere gate de Bruna salvo que se use en materiales publicos donde se mencione ESP32 por nombre (que podria percibirse como comparativo).

---

### Norma: el GME no tiene certificacion UL 508 declarada

**Estado:** Las certificaciones del GME estan "[pendiente engineering]" (Vera §1.2 y §5 Q12). El competidor funcional mas cercano en el segmento industrial (Littelfuse 77C) tiene UL 508 + UL 1053 + CE + CSA + FCC. Liyuan C1-S2 tiene CE + ISO 9001.

**Regla de uso:** No afirmar "certificado UL" ni "certifica UL 508" ni "cumple IEC 60947-4-1" hasta que la certificacion este emitida. Tampoco implicar que el GME no tiene certificacion donde eso sea riesgo — no mencionar el tema en comunicacion al consumidor final si no es relevante para la decision de compra.

**Formulacion neutra mientras no hay certificacion:** Hablar de funciones y resultados verificables ("protege ante sobrecarga, subcarga y variacion de voltaje"), no de certificaciones formales. Si el distribuidor o el ingeniero pregunta directamente, la respuesta honesta es: "el producto esta en proceso de certificacion formal; para el mercado venezolano las certificaciones IEC no son actualmente exigidas por organismo regulador activo."

**Gate Bruna:** Si el material de lanzamiento va a canal formal en Colombia (RETIE) o Caribe, Bruna debe revisar que no haya lenguaje que implique certificacion inexistente.

---

### Comparacion con competidores: prudencia, sin nombre directo en materiales publicos

**Regla general (BR-5 Precedente #3):** Los comparativos directos (mencionar Littelfuse, Wagner, Franklin Electric, Tuya por nombre) estan prohibidos en empaque fisico y materiales de PdV publicos. Permitidos en argumentario de ventas interno y presentaciones a Junta.

**El caso Tuya / Shelly:** La distincion entre "smart breaker generico" y "guardamotor inteligente" es una distincion de categoria, no un comparativo de marca. Explicar que "los smart breakers de uso general no tienen proteccion de subcarga ni logica de reintento para motores" no nombra marcas — describe una categoria. Ese argumento es defendible en materiales publicos. Si se agrega "como Tuya" o "como un Shelly", se convierte en comparativo directo — prohibido en materiales publicos, permitido en argumentario interno.

**El caso Littelfuse:** La brecha de precio (15x–23x) es el argumento implicito del Pilar 4. No es necesario nombrar a Littelfuse para activar ese argumento — basta con decir "las funciones que antes solo existian en equipos industriales de varios cientos de dolares". Esa formulacion es completamente defendible y no nombra a nadie.

---

### Proteccion de carga: Claim H — prohibicion directa del Claim H del proyecto empaque GSM

**Regla** (BR-5 Precedente #4, ratificado aqui para el GME):

Cualquier formulacion del tipo:
- "Tu equipo estara protegido"
- "Garantiza la vida util del compresor"
- "Evita que la bomba se dane"
- "Protege tu inversion"
- "Nunca mas perdes un equipo"

...implica garantia de resultado y es ❌ prohibida sin RTB tecnico que demuestre proteccion ante TODOS los casos de uso relevantes y sin revision legal externa.

El GME protege ante condiciones electricas especificas (sobre/subvoltaje, sobrecarga, subcarga, inestabilidad de frecuencia). No protege ante transientes de alta energia, fallas de ground, averias mecanicas internas, instalacion incorrecta, ni otros fenomenos fuera de su logica de medicion.

**Alternativa correcta para todas las audiencias:**
"El GME detecta variaciones electricas que danan equipos — y actua antes de que lleguen a la carga. Subcarga, sobrecarga, alto voltaje, bajo voltaje, inestabilidad de frecuencia — segun el perfil del equipo que conectas."

Esta formulacion describe accion verificable, no promete resultado garantizado.

---

## Gate de Bruna

**Estado:** PENDIENTE — este VA-5 es la propuesta de Vael para el gate de Bruna.

**Items que requieren gate explicito de Bruna PRIORITARIO antes de cualquier salida publica del GME:**

| Prioridad | Claim / Tema | Tipo de riesgo | Condicion previa al gate |
|---|---|---|---|
| 1 | Claim A — "Primero en LATAM / Venezuela en este rango de precio" | Superlativo BR-5 #1/#2 | Orlan debe completar busqueda en AliExpress/chino OEM primero |
| 2 | Claim C — "Sin cloud requerida" | Arquitectura tecnica — si es falso, es sobrepromesa estructural | Engineering debe confirmar Q2 (operacion offline) de Vera primero |
| 3 | Claim B — "Proteccion integral V+I+subcarga+arranques/h" | Feature no confirmada en firmware de produccion + logica de tres intentos | Engineering debe confirmar que cada funcion activa el contactor + explicar logica de reintentos |
| 4 | Claim H / formulaciones de "proteccion del equipo" | Garantia de resultado — responsabilidad legal (BR-5 #4) | Bruna establece exactamente donde esta la linea para el GME (igual que establecio para GSM) |
| 5 | Naming finalista (si incluye superlativo o exclusion) | Superlativo BR-5 #1/#2 | Owner aprueba naming; luego Bruna revisa si el nombre implica claim de posicion |

**Items que NO requieren gate de Bruna (pueden avanzar a produccion con caveat de scope):**
- Claim D ("estado del equipo desde el telefono, en la misma red WiFi") — uso inmediato con esa formulacion
- Claim E ("tres modos de aplicacion") en su formulacion basica — puede avanzar
- El anti-mensaje de "Claim H" (descripcion de accion, no garantia de resultado) — puede avanzar en esa formulacion

---

## Supuestos y limites

- **Insumos aguas arriba que sostienen este guardrail:**
  - Vera: `Vera_validacion_tecnica_GME_2026-05-06.md` — VE-1 v1 (2026-05-06). 15 preguntas pendientes para engineering. Los claims B, C y K son condicionados a respuestas especificas de engineering.
  - Orlan: `OL-3_GME_innovation_radar_2026-05-06.md` — OL-3 v1 (2026-05-06). Limite 1: mercado chino OEM cubierto superficialmente. Claim A no puede consolidarse hasta que Orlan complete la segunda iteracion.
  - BR-5 Precedentes: #1 (superlativo + dato cuantitativo), #2 (superlativo de exclusion), #3 (comparativos directos en empaque publico), #4 (garantia de resultado de proteccion del equipo) — todos emitidos 2026-05-03.
  - RISK-POLICY.md v1.0 (2026-04-25).

- **Validez temporal:** Este VA-5 es valido mientras: (a) OL-3 no detecte un nuevo competidor en el nicho, (b) engineering no cambie specs del producto, (c) Bruna no emita un nuevo BR-2 que redefina criterios. Revision obligatoria si cualquiera de esos triggers ocurre. Fecha limite sugerida: agosto 2026 (8 semanas antes del lanzamiento).

- **Cambios aguas arriba que invalidan este guardrail:**
  - Engineering confirma que la proteccion activa requiere WiFi activo → Claim C pasa de ⚠ a ❌.
  - Engineering confirma multivoltaje 120/220 en V1 → Claim J pasa de ❌ a ✅ para las variantes con esa capacidad.
  - Orlan encuentra competidor chino OEM con V+I+WiFi+underload a $20–30 → Claim A pasa de ⚠ a ❌ (o su scope se estrecha aun mas).
  - Bruna emite BR-2 especifico para GME → este VA-5 se actualiza reflejando las decisiones de Bruna.

- **Decisiones Owner pendientes:**
  1. Naming finalista: si el nombre elegido implica superlativo o exclusion, necesita gate adicional de Bruna.
  2. Scope geografico de lanzamiento: si hay Colombia o Caribe en V1, el tema de certificaciones se convierte en critico (de tema sensible a gate bloqueante en algunos canales).
  3. Pricing: si el Owner decide Escenario B (pricing diferenciado por variante), el claim de "precio accesible" del Claim A necesita recalibrarse por variante.

- **Claims con gate pendiente de Bruna en este VA-5:** Claims A, B, C, H (en su version de garantia de resultado). Estos no pasan a Aurelio / Nerea / Solenne hasta que Bruna los gate explicitamente. Claims D y E en sus formulaciones basicas pueden pasar sin gate de Bruna.

---

*Vael — Brand & Messaging Strategist | Dominio Genteca | 2026-05-06*
*Output VA-5 v1 — Messaging Guardrails GME*
*Candidato a archivar en Market KB — Celeste decide filename y clasificacion final*
