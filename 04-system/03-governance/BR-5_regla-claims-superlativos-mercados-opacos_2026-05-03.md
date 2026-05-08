# Precedents & Guidelines Memo — Risk & Claims (transversal)
**Mantenido por:** Bruna — Risk & Claims Governance Lead
**Ubicacion canonica:** `04-system/03-governance/`
**Ultima actualizacion:** 2026-05-08

---

## Por tipo de claim

### Afirmaciones absolutas (superlativos: "el mas", "unico", "siempre")

#### Precedente #1 — 2026-05-03 — Superlativo de velocidad con dato cuantitativo en mercado con alta opacidad competitiva

**Dominio del caso original:** Genteca
**Caso original:** Bruna_gate_empaque_v1 §2 Claim A / BR-2 Genteca entrada #1
**Producto:** Exceline GSM-MB / GSM-RB / GSM-RF / GSM-RE (empaque, lanzamiento Q2 2026)
**Claim evaluado:** "El mas rapido ante parpadeos (< 0,03 s)"

**Decisión:** APROBADO CON CAVEAT

**Criterio sentado:**

Un superlativo de performance ("el mas rapido", "el mas veloz", "el de mayor potencia") combinado con un dato cuantitativo propio verificable es APROBABLE en un mercado con alta opacidad competitiva (competidores no publican el dato de forma sistematica) cuando se cumplen las tres condiciones siguientes:

1. El dato cuantitativo propio existe y esta medido bajo condicion reproducible (laboratorio interno o certificado externo). La declaracion del Owner o del responsable tecnico de I&D confirmatoria de la medicion es suficiente para el gate conceptual; el documento de laboratorio debe existir antes de la produccion final del material.

2. No existe competidor con dato PUBLICADO igual o superior al dato propio. La ausencia de publicacion del dato por parte de un competidor no equivale a que ese competidor tenga un dato mejor no comunicado — es evidencia de que ese competidor no puede o no quiere defender el atributo publicamente. Esa asimetria de informacion opera A FAVOR del claim superlativo del que si publica el dato.

3. La formulacion combina el superlativo con el dato cuantitativo en el mismo claim. Esa estructura es la mas defensible: si el superlativo es cuestionado, el dato cuantitativo sobrevive como afirmacion tecnica autonoma.

**Regla Owner aplicada (2026-05-03):** En mercados donde los competidores no publican el atributo de forma verificable, asumir que Genteca es el unico / el mas rapido. Nunca usar "uno de los mas rapidos" porque comunica mediocridad y es innecesariamente debil cuando la evidencia disponible respalda el superlativo.

**Riesgos asumidos con esta regla:**
- Un competidor puede tener un dato no publicado que eventualmente emerja. Mitigation: el laboratorio propio puede defender el dato ante cualquier reto.
- Un competidor puede publicar un dato mejor despues del lanzamiento. Mitigation: la condicion de revision (ver abajo) activa un BR-4 si eso ocurre.
- La ausencia de dato publicado por un competidor puede reflejar ausencia real del atributo o simplemente falta de comunicacion. La regla asume que si un competidor no lo comunica, no puede defenderlo — lo cual es razonable para la defensa legal del claim.

**Condicion de revision:**
Este criterio debe revisarse si:
- Un competidor venezolano publica (en datasheet oficial, no en material de distribuidor) un dato de velocidad de desconexion ante parpadeos igual o inferior al dato propio de Genteca. En ese caso: Orlan hace refresh de OL-5, Bruna reevalua el superlativo y puede emitir BR-4 si el material ya esta publicado.
- El laboratorio de I&D de Genteca modifica el dato oficial (hacia arriba o hacia abajo). En ese caso: Vera hace refresh de brief tecnico, Bruna reevalua.
- El claim ya esta publicado en empaque impreso y el competidor reta el superlativo con evidencia verificable. En ese caso: protocolo de incidente §6.7 de Bruna; decision de mantener / aclarar / corregir / retirar.

**Formulacion prohibida (ratificada como precedente):**
"Uno de los mas rapidos" — prohibida por decision Owner 2026-05-03, ratificada como norma de precedente. No usar en ningun dominio del sistema /RAUL/ para claims de performance en mercados donde el dato propio es el mas alto conocido.

**Casos posteriores que aplicaron este precedente:** (pendiente — actualizar cuando aplique)

---

#### Precedente #2 — 2026-05-03 — Superlativo de exclusion ("unico") requiere ausencia verificada del atributo en competidores

**Dominio del caso original:** Genteca
**Caso original:** Bruna_gate_empaque_v1 §2 Claim B / BR-2 Genteca entrada #2
**Claim evaluado:** "El unico en proteger tecnologia inverter"

**Decision:** RECHAZADO

**Criterio sentado:**

El superlativo de exclusion ("el unico", "la unica marca", "el unico producto") requiere evidencia de que NINGUN competidor relevante tiene el atributo nombrado. Cuando existen competidores que lo tienen y lo comunican, el claim "unico" es factualmente falso y debe rechazarse sin excepcion.

La alternativa correcta cuando el atributo no es exclusivo pero el ARGUMENTO TECNICO QUE LO SUSTENTA si lo es: formular el claim sin el superlativo de exclusion y dejar que el RTB diferenciador haga el trabajo. En el caso de inverter: "Protege tecnologia Inverter" no es exclusivo, pero "Protege tecnologia Inverter — tiempo de respuesta < 0,03 s" si lo es, porque ninguno de los competidores que usan el claim de inverter puede respaldar ese dato.

**Condicion de revision:**
Este criterio no tiene condicion de revision: es una regla absoluta. Si los competidores que tienen el atributo desaparecen del mercado, el claim "unico" puede reconsiderarse con refresh de Orlan.

**Casos posteriores que aplicaron este precedente:** (pendiente)

---

### Comparativos directos (vs marca tercero)

#### Precedente #3 — 2026-05-03 — Comparativos directos de marca prohibidos en empaque; permitidos en argumentario interno y sustento de Junta

**Dominio del caso original:** Genteca
**Caso original:** Bruna_gate_empaque_v1 §2 Claims A-C y temas sensibles Vael VA-5 §11
**Rango de aplicacion:** Empaques fisicos de producto y materiales de punto de venta publicos

**Criterio sentado:**

Los comparativos directos (mencionar marca o producto de un competidor por nombre en el claim) estan prohibidos en empaque fisico y en materiales de punto de venta publicos para el dominio Genteca (mercado venezolano). La razon no es solo legal (riesgo de publicidad comparativa bajo la Ley de Proteccion al Consumidor y al Usuario, Arts. relativos a publicidad engañosa y denigratoria) sino tambien estrategica: el empaque llega al distribuidor y al instalador antes que a la competencia, y un comparativo directo invita a la retaliacion.

El comparativo indirecto (superlativo + dato cuantitativo propio, sin nombrar al competidor) es la forma correcta de comunicar diferenciacion. "El mas rapido ante parpadeos (< 0,03 s)" es un comparativo indirecto — cualquier competidor puede verificarlo contra su propio dato, pero el empaque no denigra a nadie por nombre.

Los datos comparativos directos (ej. "WellSpec: 200-300 ms; Genteca: < 30 ms") son material de argumentario de ventas interno y de presentacion a Junta Directiva — no de empaque.

**Casos posteriores que aplicaron este precedente:** (pendiente)

---

### Claims sobre garantias y resultados

#### Precedente #4 — 2026-05-03 — Garantia de resultado de proteccion del equipo no usable sin RTB especifico y asuncion de obligacion legal

**Dominio del caso original:** Genteca
**Caso original:** Bruna_gate_empaque_v1 §2 Claim L (rechazo preventivo)

**Criterio sentado:**

Cualquier formulacion del tipo "garantiza la proteccion del equipo", "evita daños al equipo", "su equipo estara protegido" implica una garantia de resultado que, bajo la Ley de Proteccion al Consumidor y al Usuario venezolana (y equivalentes en Colombia/Mexico si el producto se exporta), puede generar obligacion legal de reparar o compensar al consumidor cuando el equipo resulta dañado pese al protector.

Esta clase de claims requiere:
1. Un RTB tecnico que demuestre que el equipo queda protegido en TODOS los casos de uso relevantes (no solo en los casos favorables).
2. Revision por asesorıa legal externa antes de aprobar.

Para la linea GSM: el protector protege ante parpadeos y fluctuaciones de voltaje, pero no ante todos los fenomenos electricos que pueden dañar un equipo (transientes de alta energia, fallas de ground, etc.). Por tanto, no existe RTB que sostenga una garantia de resultado universal. El claim es rechazado preventivamente en todas sus formulaciones.

**Condicion de revision:** Si Vera desarrolla un RTB tecnico especifico que demuestre proteccion verificada ante un tipo concreto de evento (ej. "protege el compresor ante parpadeos de red en el 100% de los casos bajo las condiciones de instalacion especificadas") y Owner decide asumir la obligacion legal correspondiente, el claim puede reconsiderarse con asesorıa legal. Bruna sola no puede aprobarlo.

**Casos posteriores que aplicaron este precedente:** (pendiente)

---

---

### Claims de arquitectura tecnica (operacion offline / dependencia de red)

#### Precedente #5 — 2026-05-06 — Claim de "sin dependencia de red/cloud" requiere que la funcion critica de seguridad sea independiente de la conectividad

**Dominio del caso original:** Genteca
**Caso original:** Bruna_gate_GME_2026-05-06.md §#GME-03 / BR-2 Genteca entrada #17
**Producto:** GME — Exceline Profesional, Protector Monofasico Inteligente
**Claim evaluado:** "Sin app que instalar. Sin cloud requerida."

**Decision:** SUSPENDIDO — pendiente confirmacion de engineering sobre operacion offline de la funcion critica de seguridad

**Criterio sentado:**

Un claim de "sin dependencia de cloud / sin conexion a internet requerida" en un dispositivo IoT que tiene una funcion critica de seguridad (actuar un contactor, disparar un rele, cortar la alimentacion) debe verificar que la funcion critica opera independientemente de la conectividad de red — no solo que la interfaz de usuario puede funcionar sin cloud.

La distincion es: "sin cloud para la interfaz" es un claim de UX. "Sin cloud requerida" como claim de producto implica que el producto cumple su funcion primaria (proteccion activa) sin dependencia de red. Si la proteccion activa (la funcion critica de seguridad) requiere WiFi activo para ejecutar su logica, el claim "sin cloud requerida" es materialmente falso para el caso de uso critico — aunque la UI sea local.

**Tres escenarios de aplicacion:**

1. Escenario favorable: la funcion critica de seguridad opera completamente sin WiFi; la UI opera con red local. El claim completo es defendible.
2. Escenario intermedio: la funcion critica opera sin WiFi; la UI requiere red local para acceso. El claim debe aclararse: "Proteccion activa sin cloud; interfaz de monitoreo en red WiFi local."
3. Escenario desfavorable: la funcion critica de seguridad requiere WiFi activo. El claim "sin cloud requerida" es RECHAZADO porque es falso para la funcion critica. Solo puede usarse el claim de UI: "Interfaz sin app, desde tu red WiFi local."

**Riesgo arquitectonico adicional (nuevo en este precedente):**

Cuando el procesamiento de la funcion critica de seguridad y el webserver/interfaz comparten el mismo microcontrolador sin watchdog independiente, un cuelgue de la interfaz puede inhabilitar la proteccion. Este riesgo va mas alla de la comunicacion — es un riesgo de seguridad del producto que debe resolverse antes del lanzamiento, independientemente de lo que se decida sobre el claim de marketing. Bruna puede identificar el riesgo y elevarlo al Owner, pero la decision de diseno es del equipo de engineering.

**Aplicabilidad cross-dominio:**

Este criterio aplica a cualquier producto del sistema /RAUL/ que:
(a) tenga una funcion critica de seguridad (actuacion fisica sobre carga electrica, control de acceso, proteccion de datos criticos), y
(b) haga un claim de "sin dependencia de red/cloud/internet".

El claim debe verificar que la funcion critica pasa el test de operacion offline antes de aprobarse.

**Condicion de revision:**
Este criterio no tiene condicion de revision: es una regla basada en la definicion de funcion critica de seguridad. Su aplicacion puede matizarse segun el tipo de funcion critica en cada producto (ej. un dispositivo de monitoreo sin funcion de actuacion puede hacer el claim sin la misma exigencia), pero el principio es invariable.

---

### Comportamiento con reintentos en productos de proteccion

#### Precedente #6 — 2026-05-06 — La logica de reintentos en productos de proteccion debe comunicarse — no ocultarse — cuando el claim implica accion inmediata

**Dominio del caso original:** Genteca
**Caso original:** Bruna_gate_GME_2026-05-06.md §#GME-02 / BR-2 Genteca entrada #16
**Producto:** GME — Exceline Profesional, Protector Monofasico Inteligente
**Claim evaluado:** "Proteccion integral: voltaje + corriente + subcarga + arranques por hora"

**Decision:** SUSPENDIDO — pendicionado a (a) confirmacion de actuacion fisica de cada funcion y (b) definicion de como se comunica la logica de reintentos

**Criterio sentado:**

Cuando un producto de proteccion tiene una logica de reintentos antes del bloqueo definitivo (ej. "tres intentos antes de bloquear"), y ese producto hace un claim de "proteccion integral" o "proteccion activa", el claim crea en el usuario la expectativa de desconexion al primer evento de falla. Si el comportamiento real es diferente (el producto reintenta antes de bloquear), hay una brecha entre la promesa implicita del claim y el comportamiento real del producto.

Esta brecha puede generar:
1. Desconfianza: el usuario ve que el equipo conectado no se desconecto al primer evento de falla y concluye que el protector "no funciono".
2. Reclamo legitimo: si el equipo conectado sufre dano durante el segundo o tercer intento de rearranque, el usuario puede argumentar que el protector prometio proteccion integral sin aclarar los reintentos.

La logica de reintentos no es incorrecta ni mala para el producto — puede ser la logica tecnica mas adecuada para el tipo de carga. Pero debe comunicarse como feature (no ocultarse) cuando el claim implica proteccion activa ante el evento.

**Formulacion aprobada para claims con logica de reintentos:**

"Proteccion activa ante [funciones] — con logica de reintentos inteligente antes del bloqueo de seguridad." Esta formulacion describe el mecanismo completo, convierte el comportamiento de reintentos en un feature positivo (inteligencia de reintentos), y no crea la expectativa incorrecta de desconexion al primer evento.

**Aplicabilidad cross-dominio:**

Este criterio aplica a cualquier producto del sistema /RAUL/ que:
(a) tenga una logica de reintentos, tolerancia, o ventana de no-disparo antes de la actuacion definitiva, y
(b) haga un claim de proteccion activa, integral, o completa.

El nivel de comunicacion requerido de la logica de reintentos varia segun el canal: en empaque (audiencia mixta) puede bastar con la formulacion "con reintentos antes del bloqueo"; en ficha tecnica (audiencia tecnica) se requiere el numero de intentos, la condicion de reset del contador, y la posibilidad de configuracion.

**Condicion de revision:**
Este criterio se revisa si el producto cambia la logica de reintentos a desconexion inmediata al primer evento — en ese caso, el claim de proteccion inmediata es directamente aprobable sin la clausula de reintentos.

---

### Datos cuantitativos de campo en contextos regulatorios / de infraestructura opacos (sin fuente estadistica publicable)

#### Precedente #7 — 2026-05-08 — Argumento tecnico con dato cuantitativo de campo venezolano sin fuente publicable: tres salidas validas; reformulacion a condicion generica es la mas rapida

**Dominio del caso original:** Genteca
**Caso original:** BR-1 argumentos-venta atlas-legacy §Argumento 7 (2026-05-07) / BR-2 Genteca entrada #28
**Producto:** Argumentario de ventas tecnico Genteca — cable sumergible correctamente dimensionado
**Claim evaluado:** "Con CORPOELEC ya en 210V (en sistemas nominales 220V) en muchas zonas, una caida adicional de 10V en el cable deja al motor a 200V — 91% de la tension nominal"

**Decision sobre el caso:** NARANJA (2026-05-07, BR-1) → AMARILLO con caveat (2026-05-08, Owner autoriza Opcion A)

**Trigger del patron (cuando aplica este precedente):**

Un argumento tecnico que descansa en una afirmacion cuantitativa especifica del contexto venezolano — o de cualquier contexto con infraestructura de datos opaca — sin fuente estadistica publicable. Ejemplos del patron:

- "X% de desequilibrio frecuente en CORPOELEC"
- "temperatura ambiente de Y grados en zonas industriales venezolanas"
- "Z% de subtension en instalaciones de la region"
- "W% probabilidad de falla en N anos segun datos de campo"
- "[Red de suministro] ya en [valor] en muchas zonas"

El dato es plausible y reconocido por practicantes del sector. El problema no es la plausibilidad: es la ausencia de fuente publicable. Si un cliente formal o un competidor pide la referencia, no hay respuesta verificable.

**Las tres salidas validas:**

**Salida 1 (reformulacion — usable hoy):** Eliminar el dato cuantitativo especifico. Reformular como condicion generica observable. Mantener el ejemplo numerico solo como ilustracion del impacto fisico, no como estadistica. Resultado: AMARILLO con caveat.

Patron de reformulacion:
- Antes: "[Fuente sin datos] ya en [valor cuantitativo] en [muchas zonas / porcentaje / frecuencia]"
- Despues: "en redes con variabilidad de tension [o: ambientes industriales con temperatura elevada / instalaciones con red inestable / etc.]"
- El ejemplo numerico sobrevive con el marcador "ilustrativo": "si la red entrega [valor inferior al nominal], una caida adicional de [delta] en el cable deja al motor a [resultado] — [porcentaje]% de la tension nominal; este calculo es ilustrativo del impacto fisico, no una estadistica de frecuencia."

**Salida 2 (evidencia — mas fuerte, requiere accion):** Respaldar el dato cuantitativo con fuente verificable: informe MPPEE, norma COVENIN de calidad de energia, informe CORPOELEC, registro de mantenimiento industrial documentado, encuesta sectorial. Con fuente verificable, el claim puede pasar a VERDE (fuente solida: informe oficial con metodologia clara) o AMARILLO (fuente de nivel medio: registro de mantenimiento, encuesta de distribuidor). Esta salida requiere que Orlan o Vera provean la fuente — Bruna no investiga.

**Salida 3 (uso interno solamente):** Mantener el dato cuantitativo sin reformulacion, pero limitar el argumento a entrenamiento interno del equipo comercial. El dato es valioso para que el vendedor comprenda el contexto y reconozca la condicion cuando la ve. No pasa a material externo (decks de ventas, fichas comerciales, empaque, material de distribuidor) en ninguna formulacion. Estado: ROJO para uso externo, valido para uso interno.

**Resultado del caso concreto:**

Owner eligio Salida 1 (Opcion A). Argumento 7 reformulado en `wiki/tech/argumentos-venta-tecnicos.md` (Genteca KB):
- "CORPOELEC ya en 210V en muchas zonas" → "redes con variabilidad de tension" (condicion generica)
- El ejemplo del 91% Vn se mantiene como ilustrativo, no estadistico
- El argumento fisico central (formula delta-V, caida maxima 3% Vn, seccion minima 6 mm² para 60m/5HP/220V) queda intacto

**Caveat literal estandar para Salida 1:**

"La magnitud de [el fenomeno: la variabilidad de tension / el desequilibrio de red / la temperatura de operacion] depende de cada zona y cada instalacion; el ejemplo del [porcentaje o valor] es ilustrativo del impacto fisico, no una estadistica de frecuencia."

Para el caso especifico de cable sumergible / subtension:
"La magnitud de la variabilidad de tension depende de cada zona y cada instalacion; el ejemplo del 91% de Vn es ilustrativo del impacto fisico de una caida combinada (red + cable), no una estadistica de frecuencia para la red venezolana."

**Aplicabilidad cross-dominio:**

Este patron aplica a cualquier dominio del sistema /RAUL/ donde un argumento tecnico use un dato de campo cuantitativo sobre infraestructura con opacidad estadistica: red electrica venezolana (CORPOELEC), condiciones climaticas / temperatura industrial, tasas de falla de equipos en campo local, datos de calidad de agua o gas, metricas de conectividad o red de telecomunicaciones, cualquier afirmacion del tipo "en muchas zonas / instalaciones / casos de [pais o region sin estadisticas publicadas]".

No se limita a Genteca. Plenus, Finca, Teca, Panama, marca-personal: si el argumento usa un dato cuantitativo de campo sin fuente publicable como premisa de un claim externo, aplica este precedente.

**Conexion con Precedente #3 (comparativos directos):**

Precedente #3 (gate GME, 2026-05-03): prohibe comparativos directos con marcas terceras sin evidencia publicable. Precedente #7 (este): pauta como manejar datos cuantitativos de contexto sin fuente publicable. Logica compartida: "reformular o respaldar antes de externalizar." En ambos casos, el argumento fisico o tecnico subyacente puede ser solido — el problema es la forma en que se expresa sin respaldo, no el mecanismo que describe. En ambos, la reformulacion correcta preserva el argumento de fondo.

**Regla operativa para productores de claims (Vera / Solenne / Vael / Aurelio / cualquier agente CSC):**

Cuando un argumento contiene [numero] + [fuente opaca] + [escala geografica o sectorial sin estadistica] (ej. "X% en muchas zonas", "frecuente en [pais]", "tipico en instalaciones [region]"):
1. No pasar a uso externo sin gate de Bruna.
2. Proponer reformulacion Salida 1 al Owner como camino rapido.
3. Si el Owner quiere mantener el dato cuantitativo: solicitar a Orlan / Vera la fuente verificable (Salida 2).
4. Si no hay fuente posible y el Owner quiere el dato exacto: limitar al uso interno (Salida 3).

**Condicion de revision:**

Este precedente no tiene condicion de revision de la regla. Su aplicacion puede matizarse en contextos donde existe estadistica publica robusta sobre la infraestructura del pais en cuestion (ej. si Venezuela publica estadisticas oficiales de calidad de energia con metodologia verificable, la Salida 2 se vuelve la ruta principal). La condicion de revision es: "aparece fuente estadistica publicable para el dato en cuestion" — en ese caso ese argumento especifico pasa por Salida 2 sin necesidad de Salida 1.

**Casos posteriores que apliquen este precedente:** (pendiente — actualizar cuando aplique)

---

## References

- WORKSTREAM_v5_innovaciones.md §Regla de gateo de claims superlativos (2026-05-03)
- Bruna_gate_empaque_v1.md §2 Claims A, B, C, L (decisiones originales de este precedente)
- BR-2 Genteca — `03-projects/genteca/_governance/` (entradas #1 a #13; entrada #28 — caso origen de Precedente #7)
- Vera_brief_tecnico_v1.md (facts tecnicos que sustentan los RTBs)
- Orlan_competencia_v1.md Secciones 1, 2, 4 (landscape competitivo Venezuela)
- RISK-POLICY.md v1.0 (2026-04-25) — gobernanza general del sistema
- BR-1 argumentos-venta atlas-legacy — `03-projects/genteca/_governance/2026-05-07_BR-1_argumentos-venta-atlas-legacy.md` §Argumento 7 (origen de Precedente #7)
