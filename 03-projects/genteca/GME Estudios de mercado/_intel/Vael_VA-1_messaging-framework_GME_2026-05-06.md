# Messaging Framework — GME (Exceline Profesional, Protector Monofasico Inteligente)
**Fecha:** 2026-05-06
**Scope:** Lanzamiento de producto nuevo — octubre 2026
**Audiencias cubiertas:** Tecnico instalador electrico (primaria), consumidor final / dueno de equipo, distribuidor / canal ferretero, cliente premium / ingeniero de proyectos
**Producido por:** Vael — Brand & Messaging Strategist
**Insumos aguas arriba:** Ver seccion "Supuestos y limites"
**Estado:** PROPUESTA — Owner aprueba pilares antes de pasar a produccion. Claims sensibles requieren gate Bruna (ver VA-5).

---

## Nota editorial

Se producen dos archivos separados: este (VA-1, framework de mensaje) y `Vael_VA-5_guardrails_GME_2026-05-06.md`. La separacion es deliberada: VA-1 es el insumo de Aurelio y Nerea; VA-5 es el insumo de Bruna. Combinarlos diluiria la cadena de responsabilidad aguas abajo.

---

## 1. Pilares de mensaje (4 pilares)

### Pilar 1 — Inteligencia especializada para cada maquina

**Eje narrativo:**
El GME no es un protector de voltaje avanzado ni un smart relay generico: es el unico dispositivo en su rango de precio que combina medicion simultanea de voltaje, corriente y frecuencia con logica de proteccion diferenciada segun el tipo de carga (Refrigeracion, Bombas, Motores). Cada modo precarga los valores y tiempos correctos para esa maquina. Esto no es marketing: es ingenieria de proteccion aplicada a tres mundos mecanicos distintos.

**Que dice:**
Un protector con cerebro calibrado para lo que proteges, no un protector generico que el tecnico tiene que reconfigurar desde cero cada vez.

**Que NO dice:**
No promete que el modo R/B/M tiene logica de firmware radicalmente diferente en cada caso. Vera aclara que los modos cambian principalmente valores default, con al menos una diferencia de logica confirmada (maniobra diaria en modo Bombas). El claim se ancla en "configurado para" — no en "codigo diferente para".

**RTBs:**
- Pantalla de Configuracion GME (fuente primaria, Vera §3.1): selector R/B/M con parametros visiblemente distintos — tiempo de reconexion 300 s (R) vs 120 s (B) vs 60 s (M); umbral de subcarga 60% (R/M) vs 70% (B); tiempo de deteccion de subcarga 10 s (R) vs 5 s (B/M).
- Modo Bombas unico con "maniobra diaria" activa — logica exclusiva de ese modo (Vera §3.2).
- Ningun competidor en el rango $30–60 ofrece configuracion multi-aplicacion: no existe en Tuya TOMPD 63A, Shelly Pro 1PM, ICM492, Wagner DSP-1, Liyuan C1-S2 (OL-3 Seccion 3, clasificacion Diferenciado).
- El precedente funcional mas cercano (Franklin SubMonitor Connect) esta especializado solo en bombas, cuesta significativamente mas, y opera en trifasico (OL-3 §1.3).

**Categoria diferenciacion OL-3:** Diferenciado

**Audiencia primaria del pilar:** Tecnico instalador electrico (reconoce inmediatamente que configurar un protector de bomba distinto a uno de compresor es lo correcto); Cliente premium / ingeniero de proyectos (valida tecnica).

---

### Pilar 2 — Vision completa del equipo desde la red local

**Eje narrativo:**
El GME corre un webserver local en la misma red WiFi. No requiere instalar ninguna app, no depende de ningun servidor en la nube para mostrar voltaje, corriente, frecuencia, estado del rele y ultima falla. El tecnico abre el browser del telefono y entra a 192.168.0.21. La informacion esta ahi, en tiempo real, sin friccion tecnologica.

**Que dice:**
Visibilidad instantanea desde cualquier dispositivo en la misma red, sin barreras de instalacion ni suscripciones.

**Que NO dice:**
No promete acceso remoto desde fuera de la red local (eso requiere VPN, port forwarding o relay cloud — no confirmado en el GME). No promete notificaciones push (pedido en encuesta, no confirmado en implementacion). El alcance del claim es red local.

**RTBs:**
- URL 192.168.0.21 visible en todas las capturas de pantalla del GME (Vera §2 tabla, fila "Conectividad").
- Ninguna app requerida: browser nativo como interfaz (Vera §2 tabla, fila "App requerida": "No — browser nativo").
- Competidores con WiFi en este rango de precio requieren app propietaria con dependencia de cloud: Tuya TOMPD requiere Smart Life/Tuya cloud (OL-3 §1.5); Shelly Pro 1PM opera con app aunque tiene API local (OL-3 §1.5).
- Diferenciador confirmado por OL-3 §3 (clasificacion Diferenciado): "Interfaz web local (webserver en IP local 192.168.0.21) accesible desde cualquier browser sin instalacion de app — ningún competidor relevante a este precio usa este modelo de UI."

**Condicion tecnica critica (Vera §4, Claim C):** Este pilar asume que la proteccion activa (disparo del contactor) funciona sin conexion WiFi activa. Si el GME requiere WiFi para ejecutar la logica de proteccion, el pilar se debilita estructuralmente. La respuesta a la pregunta Q2 de Vera (operacion offline) es gate obligatorio antes de activar este pilar en comunicacion publica.

**Categoria diferenciacion OL-3:** Diferenciado

**Audiencia primaria del pilar:** Tecnico instalador electrico (UX directo, sin apps que ensenar al cliente); consumidor final que ya tiene smartphone pero no quiere instalar nada mas.

---

### Pilar 3 — Medicion que da informacion, no solo proteccion

**Eje narrativo:**
El GME mide voltaje, corriente y frecuencia simultaneamente y los muestra en pantalla principal. Cuando el equipo falla, el GME muestra el tipo de falla — subcarga, sobrecarga, alto voltaje, bajo voltaje, inestabilidad de frecuencia — no solo una luz roja. El tecnico que vuelve al sitio sabe que paso, no solo que algo fallo.

**Que dice:**
Informacion de diagnostico que el tecnico puede leer y usar. El protector que explica la falla.

**Que NO dice:**
No promete historial cronologico con timestamp (ese es el gap identificado por Vera §2 y OL-3 §3: "Expuesto"). No promete log de 20 fallas (pedido de la encuesta, no implementado en V1). No promete notificaciones push en tiempo real (pedido en encuesta, no confirmado). El claim se ancla en "ultima falla por tipo visible en pantalla" — exactamente lo que los mockups muestran.

**RTBs:**
- Pantalla de Mediciones GME: voltaje (V), corriente (A), frecuencia (Hz) en tiempo real (Vera §2 tabla; fuente primaria mockups).
- Pantalla de Reporte de Fallas: 9 tipos de falla con indicador de ultima ocurrencia — subcarga, sobrecarga, alto voltaje, bajo voltaje, rotor trancado, inestabilidad, entre otros (Vera §4 Claim B).
- Encuesta: comentario #104362438 (Ing. Garcia, FONDOIN): "que puedan registrar un historial de las ultimas 10 a 15 fallas" — la demanda existe; el GME cubre la ultima falla por tipo como punto de partida.
- Encuesta: comentario #104359489: "la sensibilidad de desconexion es muy importante" — el GME mide y actua; la conversacion sobre tiempo de respuesta es tecnicamente relevante (pending Q1 de Vera sobre sampling rate).
- Comparativa: Wagner DSP-1 tiene 25 eventos (sin timestamp), ICM493 tiene 5 eventos. El GME, con 9 tipos de falla en pantalla, esta en el nivel del extremo inferior del segmento para profundidad de log. En la pantalla de informacion en tiempo real (V+I+Hz), ningun competidor a este precio la ofrece simultaneamente (OL-3 §3 Diferenciado).

**Nota para comunicacion:** El angulo de mensaje para este pilar es la informacion de diagnostico en tiempo real (V+I+Hz + tipo de falla), no el historial. El historial cronologico es una aspiracion de roadmap que no debe prometerse en V1 sin confirmacion de ingenieria.

**Categoria diferenciacion OL-3:** Diferenciado (medicion V+I+Hz en tiempo real en este rango de precio); Paridad (log de fallas — nivel bajo del segmento).

**Audiencia primaria del pilar:** Tecnico instalador electrico (diagnostico rapido en campo); cliente premium / ingeniero de proyectos (datos para reporte de mantenimiento).

---

### Pilar 4 — Precio de herramienta profesional, no de premium industrial

**Eje narrativo:**
Las funciones que el GME ofrece — proteccion de subcarga, arranques por hora, medicion V+I, configuracion por tipo de carga, interfaz WiFi — solo existian en equipos industriales de $400 a $800 antes de este producto. El GME las pone al alcance del tecnico independiente y del dueno de una nevera comercial o una bomba de agua. No es que sea "barato": es que democratiza funciones antes reservadas a otro presupuesto.

**Que dice:**
Inteligencia de proteccion industrial a precio de herramienta profesional.

**Que NO dice:**
No compara directamente con marcas por nombre en materiales publicos (BR-5 Precedente #3 — comparativos directos prohibidos en empaque y POP). No afirma que el GME tiene las mismas certificaciones que un equipo industrial. No promete el mismo nivel de exactitud de medicion que instrumentacion certificada.

**RTBs:**
- OL-3 §3: el competidor funcional mas cercano (Littelfuse 77C: V+I+underload+single-phase) cuesta ~$552 en distribuidor. El GME tiene precio target $35 OPP (Van Westendorp n=29). La brecha es de 15x a 23x.
- OL-3 §1.1: "La unica marca global que combina monofasico + V + I + underload es Littelfuse 77C/MP8000, pero a precio entre 15x y 30x el objetivo GME."
- Van Westendorp §1: precio $35 dentro del rango aceptable de los tres segmentos (Refrigeracion $29.67–$39.67, Motores $35.25–$45.50, Bombas $30–$50).
- Encuesta comentario #104356020: "un producto masivo que ahora incorpore capacidad de control y monitoreo remoto no tiene por que elevar excesivamente el precio" — la expectativa de democratizacion existe en la audiencia.

**Nota para comunicacion:** El comentario del tecnico sobre el ESP32 a $10 es una objecion latente. La respuesta no es atacar la comparacion sino demostrar lo que el ESP32 solo no hace: logica de subcarga calibrada por aplicacion, contactor integrado, lógica de reintentos, interfaz sin programacion. Esa es la conversion del valor del precio.

**Categoria diferenciacion OL-3:** Diferenciado (la combinacion completa de features en este rango de precio no existe en fuentes verificadas a mayo 2026).

**Audiencia primaria del pilar:** Dueno de negocio / dueno de equipo (justificacion de precio); distribuidor / canal ferretero (argumento de venta frente a alternativas mas baratas); tecnico que conoce IoT y se pregunta "por que no solo uso un Tuya".

---

## 2. Mensajes base por audiencia

### Audiencia 1 — Tecnico instalador electrico VE

**Perfil:** 30–50 anos, tablerista o electricista independiente, instala en refrigeracion comercial y residencial, bombas de agua, motores industriales livianos. Conoce el contexto electrico venezolano (parpadeos, alto/bajo voltaje, inestabilidad de frecuencia). 29 respondientes de la encuesta. Audiencia de la comunidad Exceline Profesional.

**Mensaje principal:**
El protector que sabe distinguir si protege una nevera, una bomba o un motor — y se configura para eso desde el telefono, sin apps que instalar.

**Sub-mensajes:**
1. Mide voltaje, corriente y frecuencia al mismo tiempo. Cuando vuelvas al equipo, ya sabes que tipo de falla tuvo.
2. Entra desde cualquier browser. No necesitas ensenarte ni ensenarte a tu cliente ninguna app nueva.
3. Configurado para el tipo de carga: los tiempos de reconexion, los umbrales de subcarga, la logica de reintento — ya estan preajustados para refrigeracion, bombas o motores.

**Tono y registro:**
Tecnico-pragmatico. Reconoce la competencia del instalador. No le explica lo basico; asume que sabe lo que es una subcarga o un pico de arranque. Habla de "configuras", "mides", "sabes que fallo" — verbos del oficio. Sin hype. Sin exclamaciones. El producto habla por sus features concretas.

**Pilares activados:** Pilar 1 (multi-aplicacion), Pilar 2 (webserver local), Pilar 3 (diagnostico).

---

### Audiencia 2 — Consumidor final / dueno de equipo

**Perfil:** Dueno de nevera comercial, negocio con bomba de agua, taller con motor. No es tecnico. Compra el protector porque el tecnico se lo recomienda o porque ya le quemo un equipo. Su miedo es el costo de reparacion del equipo, no los detalles del protector.

**Mensaje principal:**
Un protector que cuida lo que mas cuesta: el equipo que hace funcionar tu negocio.

**Sub-mensajes:**
1. Entiende si lo que esta conectado es una nevera, una bomba o un motor — y protege segun eso.
2. Antes de que algo falle de verdad, ya lo vio venir. Puedes saber el estado del equipo desde tu telefono.
3. Lo instala tu tecnico de confianza. Tu solo lo usas.

**Tono y registro:**
Cercano, sin tecnicismos. El consumidor final no compra "subcarga configurable": compra "que no se me dane la nevera". El mensaje traduce los features a consecuencias tangibles para el negocio. No usar jerga IEC ni terminos de engineering. No prometer "proteccion total del equipo" (Claim H / BR-5 Precedente #4 — prohibido).

**Pilares activados:** Pilar 1 (traduccion de "modo correcto para tu equipo" a beneficio), Pilar 2 (visibilidad del estado), Pilar 4 (precio accesible).

---

### Audiencia 3 — Distribuidor / canal ferretero

**Perfil:** Ferretero o distribuidor que revende a tecnicos y duenos de equipo. Decide que productos poner en el anaquel. Necesita saber por que este vende mejor que los alternativos. Le preocupa la rotacion, la garantia y el precio al publico.

**Mensaje principal:**
El protector que el tecnico va a buscar porque hace lo que ningun otro en este precio hace.

**Sub-mensajes:**
1. Reemplaza al GAM (que ya no tiene reposicion). El cliente que tenia GAM ahora tiene una opcion mas avanzada.
2. Un solo SKU para tres aplicaciones. Menos referencias en vitrina, mas cobertura de mercado.
3. El tecnico que lo conoce lo recomienda. Es un producto que se vende por reputacion tecnica, no solo por precio.

**Tono y registro:**
Comercial-directo. El distribuidor no necesita la historia tecnica: necesita el argumento de rotacion. "Reemplaza al GAM" es un argumento concreto de canal que ninguna otra pieza de comunicacion dice igual. "Un SKU, tres aplicaciones" reduce complejidad de inventario. El argumento de precio se da en terminos de margen y competencia, no de features.

**Pilares activados:** Pilar 1 (un SKU multi-aplicacion = simplicidad de portafolio), Pilar 4 (precio competitivo para el canal).

**Nota:** El mensaje del GAM como predecesor descontinuado es un argumento de canal valido. En comunicacion publica al tecnico o consumidor, el GAM puede mencionarse como "la generacion anterior" sin implicar que era inferior en todas las dimensiones — solo que fue reemplazado por esta evolucion conectada.

---

### Audiencia 4 — Cliente premium / ingeniero de proyectos

**Perfil:** Ingeniero de mantenimiento o proyectos en instalacion HVAC/R comercial o industrial ligera. Especifica productos para proyectos. Necesita datos tecnicos verificables, no promesas de marketing. Puede hacer preguntas sobre clases de disparo, exactitud de medicion, certificaciones.

**Mensaje principal:**
Proteccion de motor configurable con medicion V+I+Hz en tiempo real y interfaz web local — en formato monofasico accesible.

**Sub-mensajes:**
1. Tres perfiles de proteccion (Refrigeracion, Bombas, Motores) con parametros de subcarga, reintento y reconexion diferenciados segun la logica del segmento.
2. Interfaz web sin dependencia de cloud ni app propietaria. El estado del equipo disponible en red local desde cualquier browser.
3. Verificacion de frecuencia en tiempo real — relevante en redes electricas con inestabilidad de Hz (Venezuela, Caribe).

**Tono y registro:**
Tecnico-formal. Este publico tolera — y valida — datos especificos. Usar valores de los mockups donde esten verificados (tiempos de subcarga, umbrales). Ser honesto con lo que esta pendiente de confirmacion de engineering (rango nominal de corriente, clase de disparo IEC, estado de certificaciones). No inflar con lenguaje de "certificado industrial" si la certificacion no esta confirmada. El credito de este publico se gana con honestidad tecnica, no con superlativo.

**Pilares activados:** Pilar 1 (logica de aplicacion), Pilar 2 (arquitectura local), Pilar 3 (datos de medicion).

---

## 3. Jerarquia de mensajes

### Jerarquia global (aplica a todos los canales y audiencias como fundamento)

**Nivel 1 — Central (siempre presente, en toda pieza):**
La combinacion: un hardware, tres modos de proteccion (R/B/M), medicion V+I+Hz, interfaz web local sin app.

Este es el territorio que ningun competidor a este precio ocupa. Es el nucleo del producto. Toda pieza de comunicacion — empaque, hoja de ventas, reel, ficha tecnica — debe poder derivarse de este nucleo.

**Nivel 2 — Secundario (segun contexto y audiencia):**
- Para tecnico: diagnostico en campo (tipo de falla visible, acceso desde browser)
- Para consumidor: "lo que hace funcionar tu negocio, protegido"
- Para distribuidor: reemplazo del GAM + argumento de simplificacion de portafolio
- Para ingeniero: datos de configuracion (tiempos, umbrales, seleccion de modo) + arquitectura sin cloud

**Nivel 3 — Reservado para etapa de consideration / decision (no para awareness):**
- Subcarga configurable por modo (porcentaje y tiempo de deteccion)
- Logica de reintentos (tres intentos antes de bloqueo — cuando engineering confirme y el claim este comunicado correctamente)
- Maniobra diaria en modo Bombas
- Parametros de frecuencia como proteccion activa (cuando Vera confirme que es activa, no solo diagnostica)

**Nivel 4 — Callado (no decir en ninguna etapa hasta que las condiciones esten resueltas):**
- Historial cronologico de fallas con timestamp (gap funcional — no implementado en V1 segun mockups)
- Notificaciones push en tiempo real (pedido de encuesta — no confirmado en implementacion)
- Acceso remoto fuera de red local (no confirmado)
- Multivoltaje 120/220 (pendiente engineering — ver VA-5)
- Claims de certificacion UL/CE/IEC especificos (estado pendiente — ver VA-5)
- "Primero en el mercado" sin scope y verificacion adicional (ver VA-5)

---

## 4. Anti-mensaje

Qué el GME NO debe decir. Cada item tiene una razon trazable a Vera, Orlan o BR-5.

**A — "Protege tu equipo" / "Tu equipo estara protegido" / "Evita danos al equipo"**
Razon: Equivalente al Claim H del proyecto empaque GSM. BR-5 Precedente #4 (2026-05-03): cualquier formulacion que implique garantia de resultado de proteccion del equipo puede generar obligacion legal. El GME protege ante condiciones electricas especificas; no puede prometer proteccion ante todos los fenomenos posibles. Alternativa correcta: "El GME monitorea y actua ante variaciones de voltaje, sobrecarga y subcarga — segun el perfil del equipo conectado."

**B — "Notificaciones en tiempo real" / "Alertas al instante"**
Razon: El webserver local del GME muestra estado en tiempo real cuando el usuario accede al browser. No hay evidencia en los mockups ni en los insumos de Vera de que el GME emita notificaciones push o alertas proactivas al telefono. Este feature fue pedido en encuesta (#104359424, #104364291) pero no esta confirmado en V1. Prometer esto sin confirmacion de engineering es sobrepromesa.

**C — "El mas rapido" / "Respuesta en menos de 1 segundo" / "Sensibilidad <1s"**
Razon: El tiempo de respuesta ante sobre/subvoltaje del GME no esta declarado en ninguna pantalla. Vera §2 tabla: "[pendiente engineering]". Un tecnico de refrigeracion (comentario #104359489) lo pidio explicitamente. Pero ese mismo comentario indica que el GME actual "no posee la suficiente sensibilidad" para <1 s segun su evaluacion. Usar este claim sin dato de engineering confirmado es sobrepromesa con un testigo que la contradice.

**D — "Tan preciso como instrumentacion profesional" / "Precision de laboratorio"**
Razon: El GME no declara clase de exactitud de medicion (IEC 60255-1). Vera §1.2: "un display de 15.6 A sin tolerancia documentada es un riesgo de credibilidad tecnica". El claim de precision requiere que engineering declare clase de exactitud. Sin ese dato, cualquier claim de precision es indefendible ante un tecnico exigente.

**E — "Certificado" / "Certificacion IEC" / "Cumple UL" sin especificar**
Razon: Estado de certificaciones del GME es "[pendiente engineering]" (Vera §1.2, §5 Q12). Usar lenguaje de certificacion sin que esta este emitida es riesgo legal y de reputacion. Alternativa mientras se completan certificaciones: hablar del producto por sus funciones verificadas, no por sus certificaciones pendientes.

**F — Comparativos directos con marca competidora en materiales publicos**
Razon: BR-5 Precedente #3 (2026-05-03). Prohibidos en empaque fisico y materiales de PdV publicos para el dominio Genteca. Los datos comparativos (Littelfuse 77C a $552 vs GME a $35) son validos en argumentario de ventas interno y presentacion a Junta — no en empaque ni en post publico.

**G — "Unico en el mercado" sin scope definido**
Razon: BR-5 Precedente #2. El superlativo de exclusion requiere evidencia de que ningun competidor relevante tiene el atributo. OL-3 tiene limitaciones de cobertura del mercado chino OEM (Limite 1 de OL-3). El claim "unico" global es indefendible a mayo 2026. El claim "unico en LATAM" o "unico en este rango de precio en Venezuela" es mas estrecho y mas defendible, pero aun requiere gate de Bruna.

**H — "Historial de las ultimas 20 fallas" / "Registro con fecha y hora"**
Razon: Los mockups del GME muestran "ultima ocurrencia por tipo" — no log cronologico con timestamp. El RTC del GME no esta confirmado (Vera §2 tabla, fila "RTC / timestamp real": "[pendiente engineering]"). Prometer historial con fecha/hora antes de que engineering lo confirme e implemente es sobrepromesa directa de una feature que el producto no tiene en V1. Alternativa: "El GME registra el tipo de ultima falla para cada categoria" — verdad verificable.

**I — "El ESP32 hace posible esto a bajo costo"**
Razon: El comentario de la encuesta #104356020 menciona ESP32 como benchmark de precio. Si se usa el ESP32 como argumento de transparencia ("la inteligencia que el ESP32 hace posible"), se corre el riesgo de activar la objecion de precio ("entonces por que no compro un ESP32 directamente"). El componente es un insumo interno del producto, no un argumento de marketing. Ignorar la objecion o atacar directamente el ESP32 tampoco funciona. La respuesta correcta es la diferenciacion por valor: lo que el GME hace que un ESP32 sin integracion especifica no hace (logica de subcarga, contactor integrado, modos de aplicacion, interfaz sin programacion).

---

## 5. Naming — Propuestas creativas

**Nota metodologica:**
Owner pidio creatividad sin sesgo por focus groups previos. Las propuestas que siguen son generadas de forma autonoma, agrupadas en cinco categorias. Owner revisara junto con los resultados de los focus groups previos cuando esten disponibles. Esta seccion es PROPUESTA — la decision es del Owner.

**Criterios de evaluacion aplicados:**
- Compatibilidad con familia Exceline / Exceline Profesional
- Evocacion del diferenciador principal (multi-aplicacion + inteligencia + accesibilidad)
- Registrabilidad preliminar (no investigacion formal — senalamiento de riesgos basado en el patron de Orlan para "Thermo-Safe" / "Thermal Shield" / "Escudo Termico" en el proyecto empaque GSM)
- Usabilidad en codigo de producto SKU (coherencia con GAM, GSM, GST-R)

---

### Categoria A — Descriptivos funcionales

**A1 — Protector Integral Monofasico (PIM)**
- Descriptor: Un hardware, tres aplicaciones. Voltaje, corriente y WiFi integrados.
- Pros: Describe exactamente lo que es. Sin ambiguedad. El ingeniero de proyectos lo entiende sin contexto. Compatible con la logica de naming del GAM ("Guardamotor Autoreinicializable Monofasico").
- Contras: Largo. No construye territorio de marca propio. "Protector Integral" ya circulo internamente — puede generar sesgo si los focus groups tambien lo evaluaron. Dificil de abreviar en un code SKU memorable.
- Compatibilidad familia: Alta (mismo patron descriptivo que GAM, GSM, GST).

**A2 — Supervisor Inteligente Monofasico (SIM)**
- Descriptor: Monitorea, analiza y actua — segun el equipo que protege.
- Pros: "Supervisor" evoca la funcion de monitoreo activo (V+I+Hz en tiempo real) sin prometer "proteccion total". Mas defensible que "protector" ante el riesgo del Claim H. "Inteligente" ancla el diferenciador de configurabilidad. Abreviatura SIM tiene resonancia (tarjeta SIM — conectividad).
- Contras: "Supervisor" puede sonar pasivo para el tecnico que valora la accion (desconexion, reintento). "SIM" como acronimo puede causar confusion con telecomunicaciones.
- Compatibilidad familia: Media — rompe con el patron "G" del portafolio Exceline Profesional (GAM, GSM, GST).

---

### Categoria B — Bautizados espanol (fantasía + descriptor)

**B1 — Sentinela / Sentinela Pro**
- Descriptor: Proteccion que vigila, mide y actua — calibrada para lo que proteges.
- Pros: Evoca vigilancia activa y presencia permanente. Sonoridad profesional en espanol. "Sentinela Pro" funciona bien en la familia Exceline Profesional. Escalable como nombre de linea (Sentinela R, Sentinela B, Sentinela M).
- Contras: "Sentinel" en ingles tiene registro de marca en multiples jurisdicciones (revisar SAPI VE; riesgo potencial similar al senalado por Orlan para "Thermal Shield"). La variante espanola "Sentinela" puede tener menor exposicion que la inglesa.
- Compatibilidad familia: Media-alta — nombre fantasía con descriptor de aplicación es el patron sugerido por el Owner en Investigacion UI_V2.

**B2 — Vigilia / Vigilia Pro**
- Descriptor: Monitoreo constante. Proteccion que nunca duerme.
- Pros: Evoca presencia continua y cuidado. Sin connotaciones militares. Raiz latina natural en espanol venezolano. Facil de pronunciar. Diferente de cualquier producto Exceline existente.
- Contras: "Vigilia" puede asociarse a ritos funerarios en algunos contextos culturales venezolanos — riesgo de connotacion no deseada. Requiere validacion cultural con el publico objetivo.
- Compatibilidad familia: Media.

**B3 — Nexo / Nexo Pro**
- Descriptor: El puente entre tu equipo y lo que necesitas saber para protegerlo.
- Pros: Evoca conectividad (el puente entre equipo y tecnico via WiFi). Corto, memorable, pronunciable. No tiene connotaciones negativas obvias. Escalable.
- Contras: "Nexo" es un concepto muy abstracto — puede no activar inmediatamente la funcion de proteccion. Riesgo de confusion con marcas existentes en el espacio tech (revisar SAPI VE). No evoca "protector" por si solo.
- Compatibilidad familia: Baja — muy lejos del patron tecnico-descriptivo de Exceline Profesional.

---

### Categoria C — Bautizados anglicismo o bilingue

**B4 / C1 — SmartGuard / SmartGuard Pro**
- Descriptor: Proteccion inteligente para neveras, bombas y motores — desde tu telefono.
- Pros: "Smart" es inmediatamente asociado a conectividad WiFi y configurabilidad digital — el diferenciador central del GME. "Guard" evoca proteccion activa. Combinacion directa y sin ambiguedad. Facil de abreviar en codigo (SGM para motores, SGB para bombas, etc.).
- Contras: "SmartGuard" es un nombre comun en el espacio de seguridad y proteccion — alta probabilidad de marca registrada existente en Venezuela y en LATAM. Requiere verificacion SAPI VE urgente antes de avanzar.
- Compatibilidad familia: Media — anglicismo, pero Owner acepto anglicismos temporalmente con alternativa espanola.

**C2 — OneGuard / OneGuard Pro**
- Descriptor: Un protector. Tres aplicaciones. Para lo que mas cuidas.
- Pros: "One" activa el diferenciador de un-hardware-tres-modos directamente. Memorable. Internacionalizable sin problemas de pronunciacion. Escalable como familia.
- Contras: "OneGuard" tiene presencia de marca en sectores de seguridad y garantias en LATAM (revisión SAPI VE necesaria). El argumento "un protector para todo" puede generar objecion tecnica: el tecnico exigente puede cuestionar si realmente es lo mismo para refrigeracion que para motores.
- Compatibilidad familia: Media.

---

### Categoria D — Conceptuales / metaforicos

**D1 — Escudo Pro / EscudoPro**
- Descriptor: La inteligencia detras de la proteccion de tu equipo.
- Pros: "Escudo" es la metafora de proteccion mas directa en espanol. Sin ambiguedad de funcion. "Pro" alinea con Exceline Profesional. Mas corto que los descriptivos funcionales.
- Contras: Orlan ya investigo "Escudo Termico" para el proyecto empaque GSM (referenciado en el brief). Si "Escudo" tiene exposicion de marca en SAPI VE similar a "Thermal Shield" en el precedente de Orlan, el riesgo existe. Necesita verificacion. Ademas, "Escudo" por si solo no activa el diferenciador de inteligencia / conectividad.
- Compatibilidad familia: Media-alta.

**D2 — Argos / Argos Pro**
- Descriptor: Cien ojos sobre tu equipo. Mide, vigila y actua.
- Pros: Argos (el gigante de cien ojos de la mitologia griega) evoca vigilancia total y percepcion multiple — analogia directa con la medicion V+I+Hz simultanea. Nombre unico, memorable, con historia. No es un nombre comun en el espacio de productos electricos.
- Contras: Requiere explicar el referente mitologico a parte de la audiencia (menos inmediato que "SmartGuard"). Puede sonar academico para el tecnico de campo. Riesgo de confusion con la marca Argos (retail en Colombia/UK) aunque en productos electricos el solapamiento es menor.
- Compatibilidad familia: Baja — lejos del patron de naming existente.

---

### Categoria E — Familia de marca (continuidad con GSM, GAM, GST-R)

**E1 — GIM (Guardamotor Inteligente Monofasico)**
- Descriptor: GIM-R220, GIM-B220, GIM-M220 — el paso siguiente del portafolio Exceline Profesional.
- Pros: Continuidad perfecta con la logica de codificacion existente (G=Genteca/Exceline, I=Inteligente, M=Monofasico, luego variante R/B/M y voltaje). El tecnico que conoce el GAM-B220 o el GSM entiende el codigo inmediatamente. Facil de inventariar, facil de pedir al distribuidor.
- Contras: No construye nombre comercial para el consumidor final. Funciona bien para el tecnico y el distribuidor; el consumidor final necesita un nombre que le diga algo. Puede requerir un nombre comercial paralelo (GIM como codigo de producto + "Exceline ProSmart" o similar como nombre de cara al publico).
- Compatibilidad familia: Maxima — es extension directa de la logica existente.

**E2 — GPM (Guardaprotector Programable Monofasico)**
- Descriptor: GPM-R220, GPM-B220, GPM-M220 — proteccion configurable para cada aplicacion.
- Pros: "Programable" activa el diferenciador de configurabilidad por aplicacion (los tres modos). Mantiene la estructura de codigo de la familia. "G" de Genteca/Exceline, "P" de Programable (o Profesional), "M" de Monofasico.
- Contras: "GPM" puede ser confundido con "gallones por minuto" en contexto de bombas — colision semantica en la audiencia de bombas. La "P" de Programable puede sonar a que el usuario necesita programar — lo opuesto al mensaje de facilidad de configuracion.
- Compatibilidad familia: Alta en estructura; riesgo de colision semantica en nicho de bombas.

---

### Recomendacion finalista — Top 2 con argumento

**Finalista 1 — GIM (Guardamotor Inteligente Monofasico) como CODIGO DE PRODUCTO + SmartGuard Pro como NOMBRE COMERCIAL (sujeto a verificacion SAPI VE)**

Razon: El portafolio Exceline Profesional existe en el canal como codigos G___. El tecnico y el distribuidor buscan, piden y facturan por codigo. GIM-R220 / GIM-B220 / GIM-M220 es inmediatamente legible en ese universo. Pero el consumidor final y el mercado de awareness digital necesitan un nombre que active el diferenciador — "SmartGuard" hace ese trabajo con precision (smart = conectividad + configurabilidad; guard = proteccion activa). La combinacion de codigo de portafolio + nombre comercial es el patron que mejor sirve a todas las audiencias simultaneamente.

Condicion critica: verificar disponibilidad de "SmartGuard" en SAPI VE antes de comprometerse. Si esta tomado, explorar "OneGuard" o "Sentinela" como alternativas de nombre comercial.

**Finalista 2 — Sentinela Pro como nombre comercial unico (con codigo GIM opcional)**

Razon: Si el Owner quiere un nombre en espanol puro con sonoridad profesional y escalabilidad como familia (Sentinela R, Sentinela B, Sentinela M), este es el candidato mas solido. Evoca vigilancia activa, es pronunciable, no tiene connotaciones negativas claras en contexto electrico venezolano, y se diferencia de cualquier nombre existente en el portafolio. El riesgo de "Sentinel" como marca registrada en ingles es real — la variante espanola "Sentinela" tiene menor exposicion pero no es cero.

**Nota a Owner:** estas son propuestas construidas sin acceso a los focus groups previos con tecnicos. Cuando esos resultados esten disponibles, la recomendacion debe cruzarse contra:
- Que nombres generaron mayor adhesion o rechazo en los grupos
- Si "GIM" o variantes de "guarda + apellido" tuvieron resonancia o confusion
- Si los tecnicos prefieren nombre en espanol o anglicismo

---

## 6. Conexion con pilares de contenido Exceline Profesional

Los cuatro pilares del GME se alinean directamente con los pilares de contenido existentes de Exceline (wiki brand §Pilares de contenido):

| Pilar de contenido Exceline | Pilar GME que alimenta |
|---|---|
| Maestros de la Energia (45%) — formacion tecnica | Pilar 1 (multi-aplicacion) + Pilar 3 (diagnostico) |
| Innovar para Proteger (30%) — lanzamientos | Pilares 1, 2, 3, 4 — el GME es el lanzamiento de este pilar en 2H2026 |
| Un Legado que se Siente (25%) — trayectoria Exceline | Pilar 4 (democratizacion: "lo que era industrial, ahora accesible") |

La premisa de comunicacion Exceline ("CONOCEMOS LO QUE PROTEGEMOS") se conecta directamente con el Pilar 1 del GME: el producto literalmente "conoce" si protege una nevera, una bomba o un motor.

---

## Supuestos y limites

- **Insumos aguas arriba que sostienen este framework:**
  - Vera: `Vera_validacion_tecnica_GME_2026-05-06.md` — memo tecnico VE-1 v1 (2026-05-06). Contiene 15 preguntas pendientes para engineering. Los claims de los Pilares 1 y 2 tienen condiciones tecnicas no resueltas (ver VA-5 para detalle).
  - Orlan: `OL-3_GME_innovation_radar_2026-05-06.md` — Innovation Radar v1 (2026-05-06). Snapshot mayo 2026. Mercado chino OEM cubierto superficialmente (Limite 1 del OL-3 — pendiente investigacion adicional de AliExpress).
  - Van Westendorp: `Informe_Van_Westendorp.md` — n=29, muestra pequena por segmento. Precios en USD referidos a tecnico/instalador como cliente final.
  - Comentarios tecnicos encuesta: `Comentarios_tecnicos_encuesta.md` — 29 comentarios, clasificacion tematica no completada.
  - Investigacion UI: `Investigacion UI_V2.txt` — respuestas Owner sobre GAM, naming y lanzamiento.
  - Brand wiki Exceline: `01-identidad-de-marca.md` + `02-estrategia-digital-y-audiencias.md` (2026-04-30).
  - Governance: `RISK-POLICY.md` v1.0 (2026-04-25) + `BR-5_regla-claims-superlativos-mercados-opacos_2026-05-03.md`.

- **Brand wiki vigente al momento de redaccion:** 2026-04-30. Eslogan Exceline Profesional vigente: "Garantiza confianza y duracion". Premisa central: "CONOCEMOS LO QUE PROTEGEMOS".

- **Validez temporal:** Este framework es valido mientras el OL-3 de Orlan no cambie la clasificacion de los diferenciadores primarios (especialmente si un competidor LATAM o chino OEM lanza producto con V+I+WiFi+motor protections a precio similar). Revisar en un Q o ante cualquier senal de nuevo competidor en el nicho. Fecha limite sugerida de revision: agosto 2026 (8 semanas antes del lanzamiento de octubre).

- **Cambios aguas arriba que invalidarian este framework:**
  - Si Vera recibe respuestas de engineering que confirman que la proteccion activa del GME requiere WiFi activo (invalidaria el Pilar 2 en su formulacion actual).
  - Si OL-3 en segunda iteracion encuentra un competidor chino OEM con V+I+WiFi+underload a $20–30 (invalidaria el Pilar 4 y debilitaria el Pilar 1 como diferenciadores de nicho vacio).
  - Si engineering confirma que los modos R/B/M solo cambian defaults sin ninguna diferencia de logica (debilitaria el Pilar 1 — no lo elimina, pero reduce el nivel del claim).
  - Si Bruna establece restricciones adicionales sobre el uso de "inteligente" o "configurado" en el contexto venezolano.
  - Si el Owner decide pricing diferenciado por variante (invalida el Pilar 4 tal como esta formulado — que asume SKU unico a $35).

- **Decisiones del Owner pendientes:**
  1. Aprobacion de los 4 pilares propuestos (obligatorio antes de pasar a produccion CSC).
  2. Naming finalista — Owner decide tras cruzar con focus groups previos. El framework puede avanzar sin nombre definido, pero VA-4 (content brief) requiere nombre antes de producir copy con nombre de producto.
  3. Pricing: este framework asume Escenario A de Van Westendorp (SKU unico a $35). Si el Owner decide Escenario B (pricing diferenciado por variante), el Pilar 4 necesita revision.
  4. Scope geografico del lanzamiento: si el lanzamiento es exclusivamente Venezuela, los claims de certificacion (o su ausencia) son menos urgentes. Si hay mercado Colombia o Caribe desde el dia 1, las certificaciones son gate critico.

- **Claims con gate pendiente de Bruna:** Ver VA-5 `Vael_VA-5_guardrails_GME_2026-05-06.md` — items marcados como ⚠ (Defendible con caveat) y ❌ (No usar) requieren gate de Bruna antes de pasar a produccion. En particular: Claim A ("primero en el mercado"), Claim B ("proteccion integral" — condicionada a confirmacion de engineering), Claim C ("sin cloud") y el naming finalista si implica superlativo.

---

*Vael — Brand & Messaging Strategist | Dominio Genteca | 2026-05-06*
*Output VA-1 v1 — Messaging Framework GME*
*Candidato a archivar en Market KB — Celeste decide filename y clasificacion final*
