# BR-2 — Gate de Claims GME (Exceline Profesional, Protector Monofasico Inteligente)
**Producido por:** Bruna — Risk & Claims Governance Lead
**Fecha de emision:** 2026-05-06
**Dominio:** Genteca
**Producto:** GME — Exceline Profesional, Protector Monofasico Inteligente (GME-R220 / GME-B220 / GME-M220)
**Horizonte:** Lanzamiento octubre 2026
**Tipo de output:** BR-2 especifico de campana — gate prioritario pre-produccion

**Este BR-2 es el primer gate formal del GME en el sistema /RAUL/. Las entradas que siguen se numeran de forma autonoma (#GME-01 en adelante) para no colisionar con el log acumulativo del dominio Genteca (entradas #1–#14 en `2026-05-03_genteca_claim-approval-log_v1.md`, que cubre el proyecto empaque GSM). Bruna recomienda que Celeste decida si este gate se incorpora como bloque al log acumulativo del dominio o se mantiene como archivo separado de campana. Las entradas aqui son auditables independientemente.**

---

## Cover Note BR-X (mini-cover obligatorio)

### Insumos consumidos

| Documento | Version / Fecha | Estado al momento del gate |
|---|---|---|
| Vael VA-5 — Messaging Guardrails GME | v1 / 2026-05-06 | Propuesta — PENDIENTE gate Bruna |
| Vael VA-1 — Messaging Framework GME | v1 / 2026-05-06 | Propuesta — pilares pendientes aprobacion Owner |
| Aurelio AU-1 — Plan de Campana GME | v1 / 2026-05-06 | Propuesta — gates Bruna declarados por pieza |
| Vera VE-1 — Validacion tecnica GME | v1 / 2026-05-06 | Vigente — 15 preguntas pendientes engineering |
| Orlan OL-3 — Innovation Radar GME | v1 / 2026-05-06 | Vigente — Limite 1: mercado chino OEM cubierto superficialmente |
| Comentarios tecnicos encuesta GME | — / 2026-05-06 | Vigente — 29 respuestas, sin clasificacion tematica completada |
| BR-5 Precedentes transversales | #1–#4 / 2026-05-03 | Vigentes — aplicados por claim donde corresponde |
| BR-2 Genteca acumulativo | v1 entradas #1–#14 / 2026-05-05 | Vigente — cubre proyecto empaque GSM |
| RISK-POLICY | v1.0 / 2026-04-25 | Vigente |

### Validez temporal de este gate

Este gate es valido mientras: (a) las preguntas Q2/Q3 de Vera no reciban respuesta de engineering con resultado distinto al supuesto, (b) OL-3 de Orlan en segunda iteracion no detecte un competidor nuevo en el nicho, (c) el Owner no modifique el modelo SKU, y (d) no exista decision de naming que implique claim de posicion adicional. **Fecha de revision obligatoria: agosto 2026** (8 semanas antes del lanzamiento de octubre, momento en que deben estar resueltas las preguntas de engineering y el naming confirmado).

### Clausulas RISK-POLICY referenciadas

- RISK-POLICY v1.0 §2 (clasificacion de acciones por riesgo) — aplicada para delimitar que corresponde a gate interno vs. escalacion Owner vs. asesoria legal externa.
- RISK-POLICY v1.0 §3 (principio de no afirmar datos que puedan ser falsos) — fundamento de todas las suspensiones condicionadas a engineering.

### Precedentes BR-5 invocados

- Precedente #1 — Superlativo de performance con dato cuantitativo en mercado opaco: aplica a Claim A.
- Precedente #2 — Superlativo de exclusion requiere ausencia verificada: aplica a Claim A (formulacion de "unico") y a Claim #GME-05 (multi-aplicacion).
- Precedente #3 — Comparativos directos prohibidos en empaque y PdV publico: aplica transversalmente a todos los claims de todos los canales de este lanzamiento.
- Precedente #4 — Garantia de resultado de proteccion del equipo no usable sin RTB especifico y asuncion de obligacion legal: aplica directamente a Claim H y a cualquier formulacion de beneficio para el consumidor final.

### Decisiones Owner pendientes que condicionan este gate

1. Naming finalista (deadline 30 mayo 2026) — si el nombre elegido implica superlativo o exclusion, Bruna debe recibir el naming para gate adicional antes de que sea usado en ningun material.
2. Modalidad SKU (1 hardware configurable vs. 3 SKUs fisicos) — afecta directamente la formulacion de #GME-05 ("un solo hardware, tres modos").
3. Scope geografico del lanzamiento V1 (Venezuela / Colombia / Caribe) — si hay Colombia desde el dia 1, el tratamiento de certificaciones pasa de "tema sensible" a "gate bloqueante" para ciertos canales.
4. Pricing definitivo (Escenario A: $35 unico / Escenario B: diferenciado por variante) — afecta la formulacion del Claim A y el Pilar 4 del framework.

---

## Seccion 1 — Gate por claim prioritario

---

### #GME-01 — Claim A: "Primer protector monofasico inteligente con WiFi y medicion de voltaje y corriente a precio accesible en Venezuela / LATAM"

**Categoria:** ⏸ SUSPENDIDO — condicionado a segunda iteracion OL-3 + decision de scope

**Argumento decisivo:**

El claim de "primero" en su formulacion actual aplica el patron del BR-5 Precedente #1 (superlativo de performance con dato cuantitativo en mercado con alta opacidad competitiva): OL-3 v1 no encontro ningun competidor en el rango $30–60 con la combinacion V+I+WiFi+motor protections en multiples busquedas a mayo 2026. Esa ausencia es evidencia real de vacancia. La vacancia competitiva verificada en fuentes primarias opera a favor del claim superlativo segun el criterio establecido en 2026-05-03.

Sin embargo, OL-3 declara explicitamente en sus Supuestos y Limites que la busqueda del mercado chino OEM fue superficial (Limite 1): AliExpress y Alibaba contienen cientos de productos de nicho que no aparecen en Google convencional. OL-3 §Proximas indagaciones identifica la busqueda profunda en plataformas chinas como la accion mas urgente para consolidar el Claim A. Ese gap no resuelto impide a Bruna cerrar el gate con la solidez auditoria que requiere un superlativo de posicion: si un OEM chino con la combinacion completa a $20–30 existe y no fue encontrado, el claim "primero" es factualmente falso, y la produccion del material seria un riesgo de credibilidad tecnica y de reputacion ante la audiencia mas exigente (el tecnico instalador que ya conoce el ecosistema IoT).

La formulacion mas defendible, cuando OL-3 complete la segunda iteracion, sera: "El primer protector monofasico en Venezuela con medicion de voltaje y corriente, WiFi y configuracion multi-aplicacion en el rango de precio accesible." Esa combinacion de superlativo + scope geografico acotado (Venezuela) + rango de precio es la arquitectura que minimiza la exposicion. El scope "en LATAM" o "en el mundo" no se aprueba por Bruna: OL-3 no tiene cobertura suficiente del mercado latinoamericano de fabricantes regionales (OL-3 §1.4 solo encontro GAM-B220 propio, PrevenIng sin confirmar, y ausencia de otros LATAM — lo cual es hallazgo pero no es busqueda sistematica del continente).

Una condicion adicional: Vera debe confirmar que las funciones V+I+WiFi+motor protections estan implementadas en firmware de produccion — no solo visibles en mockups de encuesta. El Claim A es un claim de mercado, pero si las funciones no estan implementadas en produccion, el superlativo cae por su base tecnica antes de llegar al argumento de mercado (Vera VE-1 §Supuesto 1 declara que los mockups se asumen como representacion de firmware avanzado, pero esta es una asuncion interna, no una confirmacion de engineering).

**Caveat literal (condicionado a desbloquearse con OL-3 segunda iteracion y confirmacion Vera):**

Cuando el claim sea aprobado, el caveat de scope debe aparecer integrado en la formulacion misma del claim — no como nota a pie de pagina sino como parte del claim: "El primer protector monofasico en Venezuela con medicion de voltaje y corriente, WiFi y configuracion multi-aplicacion en el rango de precio accesible." Si el Owner insiste en usar "en LATAM", Bruna requiere que OL-3 extienda la busqueda a fabricantes de Colombia, Mexico, Brasil y proveedores chino-B2B con distribucion LATAM documentada antes de aprobar ese scope.

**Dependencia explícita para desbloquear:**

1. Orlan completa segunda iteracion OL-3 (busqueda profunda AliExpress con terminos en ingles y chino, verificacion PrevenIng Paraguay) — resultado esperado segun AU-1: semana 4 de mayo 2026.
2. Vera recibe confirmacion de engineering de que las funciones V+I+WiFi+motor protections estan implementadas en firmware de produccion (no solo en mockups).
3. Una vez resueltos (1) y (2), Bruna recibe los resultados y emite el gate final. Si (1) devuelve un OEM chino con la combinacion completa a precio similar: el Claim A pasa a ❌ RECHAZADO y se formula alternativa sin superlativo.

**Reglas de invalidez:**

- OL-3 segunda iteracion detecta un competidor (chino OEM o LATAM) con V+I+WiFi+motor protections a precio $20–50: Claim A pasa a ❌. Bruna emite BR-4 si el material ya fue producido.
- Engineering responde que las funciones del firmware de produccion difieren materialmente de los mockups: el RTB tecnico del claim se cae antes del argumento de mercado.
- Owner define scope geografico de lanzamiento que incluye mercados donde la busqueda de Orlan es incompleta: el scope del claim debe limitarse a mercados con busqueda verificada.
- Naming finalista incorpora "primero" o "unico" como parte del nombre: ese naming requiere gate adicional de Bruna antes de usar el nombre en cualquier material (BR-5 Precedente #2).

**Piezas bloqueadas hasta resolver:** P-04 landing (Aurelio AU-1), P-01 post (version con superlativo), P-02 email (si incluye el claim de "primero").

---

### #GME-02 — Claim B: "Proteccion integral: voltaje + corriente + subcarga + arranques por hora en un solo protector monofasico"

**Categoria:** ⏸ SUSPENDIDO — condicionado a confirmacion de engineering Q15 + Q8 + revision de la logica de tres intentos

**Argumento decisivo:**

El conjunto V+I+subcarga+arranques/hora no existe en ningun competidor del rango $30–60 segun OL-3 §Seccion 3 (Diferenciado). Los mockups del GME muestran todos los elementos en la UI: U>/U< (voltaje), I>/I< (corriente), activacion de subcarga + % + tiempo de deteccion, toggle de arranques maximos por hora. Funcionalmente, el claim es el mas defendible del portafolio del GME en terminos de vacancia competitiva.

El problema no es el claim en si: es que "integral" implica que cada funcion actua fisicamente — que el contactor se abre, no que el evento se registra en pantalla. Vera VE-1 §4 Claim B es explicita: "el equipo de firmware debe confirmar que cada funcion activa fisicamente el contactor." Sin esa confirmacion, Bruna no puede aprobar el adjetivo "integral" porque no puede excluir el escenario en que alguna de las cuatro funciones solo hace logging sin actuacion fisica.

El segundo problema, de naturaleza diferente y potencialmente mas grave para la responsabilidad del producto, es la logica de tres intentos confirmada en los mockups (log muestra "Off Tercera falla de Sobrecarga" y "Off Tercera falla de Subcarga"). Si el GME hace dos reintentos antes de bloquear, un equipo conectado puede sufrir un segundo intento destructivo sin que el usuario lo sepa ni haya sido informado de esa logica. El claim "proteccion integral" en un material de marketing — sin informacion clara sobre la logica de reintentos — crea la expectativa de desconexion al primer evento. Cuando el comportamiento real es diferente, la brecha entre promesa y realidad es un riesgo de reclamacion legitima bajo la Ley de Proteccion al Consumidor venezolana (que no requiere mala fe, solo promesa no cumplida). Esta situacion tiene paralelo directo con la razon del Precedente #4 del BR-5 (garantia de resultado sin RTB universal).

No es que el comportamiento de tres intentos sea incorrecto o malo: puede ser la logica tecnica mas adecuada para motores y compresores (intentar el rearranque antes de bloquear definitivamente es practica legitima en protectores de motor). El problema es la comunicacion, no el producto. Una vez que engineering confirme la logica de reintentos y Vael la integre como feature comunicado (no ocultado), el claim "integral" puede reconsiderarse con la claridad adicional de que la logica incluye reintentos antes del bloqueo.

La logica de tres intentos no es necesariamente un bloqueo permanente del claim B — pero es un requisito de honestidad tecnica en la comunicacion que debe resolverse antes de que el claim vaya a produccion. Bruna no puede aprobar "integral" sin que engineering confirme (a) actuacion fisica de cada funcion y (b) logica de reintentos con comunicacion clara de ese comportamiento.

**Caveat literal (para cuando se desbloquee):**

El claim en su formulacion base puede ser: "Proteccion activa ante voltaje, corriente, subcarga y arranques excesivos — con logica de reintentos inteligente antes del bloqueo de seguridad." Esa formulacion es honesta, diferenciadora, y no oculta el comportamiento de reintentos sino que lo convierte en feature. El texto exacto de comunicacion sera propuesto por Vael y revisado por Bruna cuando engineering confirme la logica.

Si el claim aparece en piezas con restriccion de espacio (empaque tiro), la formulacion compacta aprobable seria: "Proteccion V+I+subcarga+arranques/hora — con reintentos antes del bloqueo de seguridad." La segunda clausula es obligatoria: sin ella, el claim "integral" crearia la expectativa de desconexion inmediata al primer evento, que no corresponde al comportamiento real.

**Dependencia explícita para desbloquear:**

1. Engineering responde Vera Q15 (logica de tres intentos: ¿cuantos reintentos, cuando se resetea el contador, es configurable?) — antes del 15 julio 2026 segun AU-1 §7.2.
2. Engineering confirma Vera Q8 (rango de medicion de corriente y metodo) y que cada funcion activa fisicamente el contactor.
3. Vael propone formulacion de reintentos integrada al claim y Bruna la aprueba como caveat literal de produccion.

**Reglas de invalidez:**

- Engineering confirma que alguna de las cuatro funciones (especialmente arranques/hora) solo hace logging sin actuacion fisica: el claim "integral" debe retirarse y reformularse para nombrar solo las funciones que actuan fisicamente.
- Engineering confirma que la logica de reintentos no es configurable y es de tres intentos fijos: la formulacion del claim debe incluir obligatoriamente el caveat de reintentos sin posibilidad de eliminarlo por restriccion de espacio.
- Vera detecta, en la respuesta de engineering, que la logica de sobrecarga no implementa curva de disparo sino umbral fijo: el claim de "integral" en contexto tecnico (ficha tecnica, ingeniero de proyectos) debe aclararse con esa limitacion.

**Piezas bloqueadas hasta resolver:** P-05 ficha tecnica, P-07 video R/B/M (si el guion menciona el claim B explicitamente).

---

### #GME-03 — Claim C: "Sin app que instalar. Sin cloud requerida."

**Categoria:** ⏸ SUSPENDIDO — condicionado a confirmacion de engineering Q2 + Q3 (Vera VE-1 §5)

**Argumento decisivo:**

Este es el claim de mayor impacto arquitectonico del portafolio GME y el que tiene la mayor exposicion de riesgo si resulta falso. El modelo de webserver local (URL 192.168.0.21 visible en todos los mockups) es un diferenciador real frente a Tuya (dependencia de cloud confirmada en OL-3 §1.5) y Shelly (cloud opcional pero presente). "Sin app que instalar" es plenamente defendible y no requiere confirmacion adicional: el acceso desde browser nativo es verificable en los mockups y ninguna app store esta involucrada.

El problema es la segunda parte: "sin cloud requerida." OL-3 y Vera identifican el mismo riesgo: si la proteccion activa (el disparo fisico del contactor ante sobrecarga, subcarga o variacion de voltaje) requiere que el modulo WiFi y el webserver esten activos, el claim "sin cloud" es verdadero para la interfaz pero falso para la funcion critica del producto, que es la proteccion. Un tecnico que instala el GME en una sala de maquinas sin cobertura WiFi y asume que el equipo queda protegido porque "no requiere cloud" — cuando en realidad necesita WiFi para que el contactor funcione — es el escenario de responsabilidad mas grave posible. Vera VE-1 §4 Claim C identifica este riesgo como "el gap mas critico del memo."

El segundo riesgo arquitectonico identificado por Vera (§4 Claim C): si el MCU de proteccion y el MCU del webserver son el mismo chip, un cuelgue del webserver puede dejar la proteccion inactiva. Este riesgo va mas alla del claim: es un riesgo de seguridad del producto que engineering debe resolver antes del lanzamiento independientemente de lo que Bruna decida sobre el claim.

Bruna suspende el Claim C hasta que engineering responda Q2 (operacion offline) y Q3 (arquitectura MCU). El resultado de esas respuestas determina cual de tres escenarios aplica:

- **Escenario favorable:** proteccion activa funciona completamente sin WiFi, MCU de proteccion es independiente del webserver. En ese caso el claim "sin cloud requerida" es plenamente defendible y se aprueba con el caveat de scope de red local para la interfaz.
- **Escenario intermedio:** proteccion activa funciona sin WiFi, pero la interfaz de monitoreo requiere conectividad. En ese caso "sin cloud requerida" se aprueba con el matiz de que la interfaz requiere red WiFi local (no cloud). El claim se reformula: "Proteccion activa sin cloud. Control desde tu red local cuando estes conectado."
- **Escenario desfavorable:** proteccion activa requiere WiFi activo. En ese caso el claim "sin cloud requerida" pasa a ❌ RECHAZADO porque es falso para la funcion critica. La alternativa seria: "Interfaz sin app — control desde tu red WiFi local" — que describe la UI sin afirmar independencia de red para la proteccion.

El claim C es critico para P-03 (empaque), P-04 (landing) y P-06 (video WiFi demo). El empaque debe estar en imprenta antes del 1 septiembre 2026. La fecha limite para tener la respuesta de engineering Q2/Q3 es antes del 15 julio 2026 (AU-1 §7.2). Si engineering no responde antes del 15 julio, el empaque se produce con el Escenario intermedio como maximo — o directamente sin el Claim C, con solo el Claim D aprobado ("el estado de tu equipo desde tu browser, en la misma red WiFi").

**Caveat literal — Escenario favorable (texto exacto para produccion):**

Para piezas de empaque y landing: "Control desde cualquier browser en la misma red WiFi. Sin app que instalar. Sin servidor en la nube. La proteccion actua independientemente de la conexion a internet."

Para piezas audiovisuales (P-06 video): el guion no puede mostrar acceso desde fuera de la red local ni afirmar funcionamiento sin WiFi hasta confirmar el Escenario favorable. El scope "en la misma red WiFi" debe ser explicito en la narracion.

**Caveat literal — Escenario intermedio (texto exacto para produccion si Q2 favorable y Q3 adverso):**

"Control desde cualquier browser en la misma red WiFi. Sin app que instalar. Sin servidor en la nube para la interfaz de usuario. La proteccion actua ante variaciones electricas independientemente de la conexion a internet; la interfaz de monitoreo requiere red WiFi local activa."

**Dependencia explícita para desbloquear:**

1. Engineering responde Vera Q2 (operacion offline de la logica de proteccion) — antes del 15 julio 2026.
2. Engineering responde Vera Q3 (arquitectura MCU: separacion entre logica de proteccion y webserver, watchdog dedicado) — antes del 15 julio 2026.
3. Con las respuestas en mano, Bruna emite el gate final del Claim C indicando cual de los tres escenarios aplica y el caveat literal correspondiente. Hasta ese gate final, el Claim C no pasa a produccion ejecutable en ninguna pieza publica.

**Reglas de invalidez:**

- Engineering confirma que la proteccion activa requiere WiFi activo: Claim C pasa de SUSPENDIDO a ❌ RECHAZADO. No hay reformulacion posible que sostenga "sin cloud requerida" si la funcion critica del producto falla sin red.
- Engineering identifica que el MCU de proteccion y el webserver comparten el mismo hilo critico sin watchdog independiente: Bruna requiere que engineering implemente la separacion antes del lanzamiento antes de gatear el Claim C — independientemente del resultado de Q2, porque el riesgo de seguridad del producto es un requisito de diseno, no solo de comunicacion.
- Algun material de comunicacion (post LinkedIn, email, landing) usa el Claim C antes del gate final de Bruna: Aurelio AU-1 es responsable de comunicar a Solenne y Nerea que el Claim C esta bloqueado.

**Piezas bloqueadas hasta resolver:** P-03 empaque (si se quiere incluir el claim), P-04 landing, P-06 video WiFi demo. Estas piezas pueden avanzar en produccion usando el Claim D aprobado ("el estado de tu equipo desde tu browser, en la misma red WiFi") sin necesidad de esperar el gate del Claim C.

---

### #GME-04 — Claim H: Formulacion de "proteccion del equipo / instalacion / negocio"

**Categoria:** ⚠ APROBADO CON CAVEAT — formulacion de accion verificable / ❌ RECHAZADO — formulacion de garantia de resultado

**Argumento decisivo:**

Este claim es el equivalente directo del Claim H y del Claim L del proyecto empaque GSM, gateados en entradas #8 y #12 del BR-2 Genteca (2026-05-03). El criterio establecido en esas entradas — y elevado a BR-5 Precedente #4 (2026-05-03) — aplica sin modificacion al GME: cualquier formulacion que implique que el equipo conectado al GME quedara protegido ante fallas electricas crea una garantia de resultado que no puede ser sostenida por ningun RTB tecnico disponible.

El GME protege ante condiciones electricas especificas: sobrevoltaje, subvoltaje, sobrecarga de corriente, subcarga (dry run), inestabilidad de frecuencia (pendiente confirmacion Q14 de Vera de si es activa o solo diagnostica), y arranques excesivos por hora. No protege ante: transientes de alta energia (descargas atmosfericas directas, conmutacion inductiva de alta potencia), fallas de ground, averias mecanicas internas del equipo conectado, instalacion incorrecta (fusibles de mayor calibre, cableado subdimensionado aguas arriba), ni ningun otro fenomeno fuera de su logica de medicion declarada.

La Ley de Proteccion al Consumidor y al Usuario venezolana (y sus equivalentes en Colombia y Caribe si el lanzamiento se extiende) interpreta las promesas de marketing como compromisos implicitos. Si el empaque dice "protege tu negocio" y el compresor del negocio se dana por un transiente de alta energia que el GME no puede detectar, hay base para reclamo legitimo. El GME no puede defenderse con "era un fenomeno fuera de nuestra especificacion" si el empaque no especifico ese limite. Esta es exactamente la situacion que el Precedente #4 previene.

**Formulaciones PROHIBIDAS (❌ — sin alternativa en ninguna pieza publica):**

- "Tu equipo estara protegido."
- "Garantiza la proteccion del equipo."
- "Nunca mas te quedas sin equipo."
- "Protege tu inversion."
- "Evita que la bomba se dane."
- "Tu negocio estara protegido."
- "Garantiza la vida util del compresor / bomba / motor."
- Cualquier variante que prometa que el equipo conectado no sufrira daños como resultado de instalar el GME.

**Formulacion APROBADA (⚠ con caveat — texto exacto para produccion):**

Para piezas de empaque (tiro — espacio reducido): "El GME monitorea las condiciones electricas y actua ante sobrecarga, subcarga y variaciones de voltaje — segun el perfil del equipo conectado."

Para piezas de landing y video (espacio amplio): "El GME detecta las variaciones electricas que danan equipos — y actua antes de que lleguen a la carga. Subcarga, sobrecarga, alto voltaje, bajo voltaje, inestabilidad de frecuencia — segun el perfil del equipo que conectas. Refrigeracion, bombas o motores: el GME responde segun su logica."

Para piezas de audiencia consumidor final (lenguaje accesible): "Un protector que vigila las condiciones electricas de tu equipo — y lo desconecta automaticamente si detecta una variacion peligrosa. Subcarga, sobrecarga, alto o bajo voltaje: el GME actua segun el tipo de equipo que proteges."

**Regla de caveat estructural obligatorio:**

En cualquier pieza donde aparezca el beneficio de proteccion para el consumidor final, debe coexistir — en proximidad visual o en el mismo parrafo — la descripcion de las condiciones ante las que el GME actua. No es aceptable decir "protege tu equipo" sin declarar ante que lo protege. La distincion entre "actua ante X condiciones" y "protege ante todo" es la linea entre el claim aprobado y el rechazado.

**Regla adicional derivada de la logica de tres intentos (conexion con #GME-02):**

Si el GME hace reintentos antes del bloqueo definitivo, cualquier formulacion de "proteccion" en materiales de audiencia consumidor final debe coexistir con una explicacion (en nivel de consideration / decision, no en empaque) de que el GME intenta el rearranque antes de bloquear. Un consumidor que no sabe esto puede percibir que el equipo "no respondio" al primer evento de falla, lo que puede generar desconfianza en el producto y reclamos de garantia incorrectos. La logica de reintentos no esta implementada en ninguna formulacion del Claim H por ahora — pero Bruna alerta a Aurelio y a Vael: cuando el Claim B se desbloquee (#GME-02), la informacion sobre reintentos debe integrarse en los materiales de nivel MOFU/BOFU.

**Reglas de invalidez:**

- Solenne o cualquier otro agente de produccion usa una formulacion de garantia de resultado en cualquier pieza de cualquier audiencia: la pieza debe ser detenida y reformulada antes de publicacion. El sello de Bruna sobre el Claim H solo cubre las formulaciones listadas como APROBADAS en esta entrada.
- Engineering confirma que la logica de proteccion activa del GME tiene un fallo de cobertura adicional no contemplado (ej. no actua ante sobre-frecuencia): la formulacion aprobada debe actualizarse para no incluir ese fenomeno como funcion del GME.

**Piezas desbloqueadas con esta decision (formulacion de accion, NO de garantia):**

P-01 post, P-02 email, P-03 empaque (con las formulaciones aprobadas arriba), P-04 landing (con las formulaciones aprobadas arriba). Estas piezas pueden avanzar con las formulaciones de accion aprobadas sin esperar mas gates. Solenne recibe las formulaciones literales aprobadas como restriccion operativa en AU-4.

---

## Seccion 2 — Claims adicionales evaluados

---

### #GME-05 — "Multi-aplicacion: configura para R/B/M con un solo hardware"

**Categoria:** ⚠ APROBADO CON CAVEAT — formulacion basica / ⏸ SUSPENDIDO — formulacion con superlativo de exclusion

**Argumento decisivo:**

La formulacion basica ("tres modos de aplicacion: Refrigeracion, Bombas, Motores") es plenamente defendible. Los mockups del GME muestran el selector R/B/M con parametros visiblemente distintos por modo (tiempos de reconexion, umbrales de subcarga, maniobra diaria en modo B — Vera §3.1–3.2). La diferenciacion es real incluso si los modos solo cambian defaults: porque la diferenciacion de defaults segun aplicacion ya tiene valor funcional para el tecnico que instala en un compresor vs. una bomba sumergible. No es necesario que el codigo de firmware sea radicalmente diferente entre modos para que el claim sea verdadero.

El riesgo de "un solo hardware" esta condicionado a la decision Owner pendiente sobre modalidad SKU (AU-1 §7.3: decision antes del 15 junio 2026). Si el Owner decide 3 SKUs fisicos diferentes (R/B/M en hardware distinto), el claim "un solo hardware, tres modos" es factualmente falso y debe retirarse. Si el Owner confirma que es 1 hardware con diferenciacion por firmware y etiqueta (Escenario A del Van Westendorp), el claim es plenamente verdadero.

La formulacion con superlativo de exclusion ("el unico con tres modos" o "ningun otro protector en este precio tiene tres modos") requiere gate adicional de Bruna por aplicacion del BR-5 Precedente #2: el "unico" requiere que Orlan verifique la ausencia del atributo en competidores relevantes. OL-3 §Seccion 3 confirma que ningun competidor en el rango $30–60 tiene configuracion multi-aplicacion — pero la busqueda del mercado chino OEM es incompleta. Hasta que OL-3 segunda iteracion confirme la ausencia, el superlativo de exclusion no se aprueba. La formulacion basica (sin "unico") puede usarse ya.

**Caveat literal aprobado (texto exacto para produccion — formulacion basica):**

Para empaque y piezas de awareness: "Un protector. Tres modos de aplicacion: Refrigeracion, Bombas, Motores. Los parametros de proteccion preajustados segun el tipo de carga que conectas."

Para piezas tecnicas (ficha, video R/B/M): "Selector de modo R/B/M: cada modo precarga los parametros de subcarga, reconexion y reintento correctos para ese tipo de carga. Refrigeracion: 300 s de reconexion, 60% subcarga, 10 s de deteccion. Bombas: 120 s de reconexion, 70% subcarga, 5 s de deteccion, maniobra diaria. Motores: 60 s de reconexion, tiempo de deteccion de sobrecarga configurable 0.1–5 s."

**Dependencia para formulacion con superlativo:**

- OL-3 segunda iteracion sin encontrar competidor con multi-aplicacion en $30–60: superlativo "el unico en este rango de precio con tres modos" puede gatearse.
- Decision Owner de 1 hardware configurable (no 3 SKUs fisicos): el claim "un solo hardware" puede usarse.

**Reglas de invalidez:**

- Owner decide 3 SKUs fisicos: "un solo hardware" debe retirarse de toda pieza donde aparezca.
- OL-3 encuentra competidor con configuracion multi-aplicacion a precio similar: el superlativo de exclusion no puede usarse.

---

### #GME-06 — "Visibilidad total del equipo desde tu celular"

**Categoria:** ❌ RECHAZADO en esta formulacion

**Argumento decisivo:**

"Total" es un superlativo absoluto que el GME no puede sostener. El GME muestra V, I, Hz, estado del rele, ultima falla por tipo — pero no muestra temperatura de descarga, estado de valvulas, flujo hidraulico, temperatura de bobinado, ni historial cronologico de fallas (gap Vera §2). Un tecnico exigente que evalua el producto sabra que la visibilidad es parcial (util, relevante, diferenciadora — pero no "total"). Ademas, el scope es red local: "desde tu celular" sin calificacion implica acceso desde cualquier parte, lo cual no esta confirmado en el GME.

**Alternativa aprobada:** "El estado de tu equipo, en tu browser — voltaje, corriente, frecuencia y ultima falla, en tiempo real desde la misma red WiFi." Esta formulacion es especifica, verdadera, diferenciadora y no usa superlativos indefendibles.

**Regla de invalidez:** Si engineering implementa antes del lanzamiento un historial cronologico de fallas con timestamp y un mecanismo de acceso remoto (VPN relay, MQTT push notification), el scope del claim puede ampliarse — pero requiere nuevo gate de Bruna con esas funciones confirmadas.

---

### #GME-07 — "Tan preciso como instrumentacion profesional"

**Categoria:** ❌ RECHAZADO — sin alternativa disponible hasta que engineering declare clase de exactitud

**Argumento decisivo:**

El GME no declara clase de exactitud de medicion IEC 60255-1 en ninguna pantalla. Vera §1.2 es inequivoco: "un display de 15.6 A sin tolerancia documentada es un riesgo de credibilidad tecnica." La instrumentacion profesional (Clase 0.2–0.5 IEC 60255-1) es materialmente mas precisa que la logica de un rele de proteccion (para la cual Clase 3–5 es suficiente para actuar en el umbral). El claim de comparacion con instrumentacion profesional no tiene ningun RTB que lo sostenga y podria generar desconfianza en la audiencia tecnica exactamente mas valiosa (el ingeniero de proyectos que sabe que un rele de proteccion no tiene la misma clase de exactitud que un analizador de calidad de energia).

**Alternativa disponible cuando engineering confirme:**

Si engineering declara Clase 1 (±1% V/I), el claim posible es: "Medicion a ±1% para una lectura confiable en campo." Verdad especifica y modesta que no compara con instrumentacion de laboratorio.

**Dependencia:** Vera Q8 (exactitud de medicion). Sin ese dato, el claim es ❌ RECHAZADO sin alternativa.

---

### #GME-08 — Pricing claim: "$35 al precio de un protector basico, con la inteligencia de uno profesional"

**Categoria:** ⚠ APROBADO CON CAVEAT — formulacion de valor / ❌ RECHAZADO — formulacion con comparativo directo implicito de precio

**Argumento decisivo:**

El claim de democratizacion del precio es el argumento mas solido del Pilar 4 (VA-1). La brecha 15x–23x con Littelfuse 77C (OL-3 §1.1) es verificable y es el RTB central de precio. El problema es la formulacion: si "protector profesional" implica una clase de exactitud o certificacion IEC/UL que el GME no tiene, el claim es una comparacion implicita que puede ser cuestionada por la audiencia tecnica.

La formulacion aprobada evita la comparacion directa de categoria ("protector profesional") y ancla la diferenciacion en las funciones especificas: "Las funciones que antes solo existian en equipos industriales de varios cientos de dolares — ahora en el formato que el tecnico independiente puede instalar y pagar." Esta formulacion es plenamente aprobada: no compara con ninguna marca, no afirma certificacion, describe funciones verificables (subcarga configurable, modos de aplicacion, medicion V+I) sin implicar que el GME tiene la misma clase industrial que un Littelfuse 77C.

Bruna ratifica que los datos comparativos directos (ej. "Littelfuse 77C: $552 vs GME: $35") son validos en argumentario de ventas interno y en material de distribuidor — no en empaque fisico ni en post publico (BR-5 Precedente #3).

**Caveat literal aprobado (texto exacto para produccion):**

Para empaque y landing (audiencia mixta): "Las funciones que antes costaban cientos de dolares — ahora a precio de herramienta profesional."

Para argumentario de ventas interno (distribuidor, pieza B del P-09): comparacion de precio directa con Littelfuse 77C puede incluirse con la nota de que la comparacion es de funciones, no de certificaciones — el GME no tiene las mismas certificaciones que el 77C.

---

### #GME-09 — "Multivoltaje 120/220V"

**Categoria:** ❌ RECHAZADO en V1 — pendiente confirmacion engineering

**Argumento decisivo:**

Los SKUs del GME aparecen como "220" (GME-R220, GME-B220, GME-M220). Vera Q10 pide confirmacion de si el hardware soporta 120 Vac. Usar el claim sin confirmacion de hardware es sobrepromesa directa de una especificacion no confirmada — el tipo de over-claim mas clasico y mas danino para la credibilidad tecnica del producto ante la audiencia de instaladores.

No hay alternativa posible en V1: si el hardware solo soporta 220V, el claim no existe. Si engineering confirma variante 120V para octubre 2026, el claim se habilita para los SKUs con esa capacidad (no para los 220V).

**Dependencia:** Vera Q10 — antes del 1 agosto 2026.

---

### #GME-10 — "Sensibilidad menor a 1 segundo ante fluctuaciones"

**Categoria:** ❌ RECHAZADO — pendiente confirmacion engineering, con testigo que cuestiona el claim

**Argumento decisivo:**

El tiempo de respuesta del GME ante sobre/subvoltaje no esta declarado en ninguna pantalla. Vera §2 tabla marca "[pendiente engineering]" para tiempo de respuesta. Adicionalmente, el tecnico de refrigeracion (comentario encuesta #104359489) senala explicitamente que "la electronica no posee la suficiente sensibilidad para detectar en un muy corto periodo de tiempo una fluctuacion" — lo que indica que su evaluacion previa del producto sugiere que podria NO tener respuesta menor a 1 s. Usar este claim sin el dato de engineering es sobrepromesa con un testigo que la contradice activamente.

Si engineering confirma tiempo de respuesta cuantitativo (ej. "deteccion de subvoltaje en 200 ms"), ese dato especifico puede usarse aplicando el patron del BR-5 Precedente #1 (superlativo con dato cuantitativo en mercado opaco). Pero el claim requiere que el dato verifique el threshold de 1 s: si el dato de engineering dice 2 s (como el default del ICM492 y Wagner DSP-1 segun Vera §2), el claim queda descartado y solo puede usarse la formulacion de la funcion sin comparacion de velocidad.

**Dependencia:** Vera Q1 (sampling rate del ADC y tiempo de respuesta) — antes del 1 agosto 2026.

---

### #GME-11 — "Historial de las ultimas 20 fallas con fecha y hora"

**Categoria:** ❌ RECHAZADO en V1 — el producto no tiene esa funcion implementada

**Argumento decisivo:**

Los mockups del GME muestran "ultima ocurrencia por tipo de falla" — no log cronologico con 20 entradas ni timestamp de fecha y hora. Vera §2 tabla es explicita: "Ultima ocurrencia por tipo (9 tipos) — sin timestamp cronologico." Vera Q4 (profundidad real del log) y Q5 (RTC interno) estan marcadas como pendientes de engineering.

Prometer en V1 lo que no esta implementado es el antipattern central de la comunicacion de producto y el que genera reclamos mas inmediatos y verificables por parte del tecnico que instala el producto y accede a la interfaz. El pedido de 20 fallas con fecha y hora aparece en 6 comentarios de la encuesta (incluyendo comentario de un Instructor FONDOIN certificado), lo que hace que la expectativa sea alta y especifica en la audiencia tecnica prioritaria.

**Alternativa en V1 (texto exacto para produccion):** "El GME registra el tipo de la ultima falla para cada categoria de evento — subcarga, sobrecarga, voltaje, frecuencia. Hasta 9 tipos de evento con indicador de ultima ocurrencia."

**Condicion de habilitacion para V2/roadmap:** Si engineering implementa historial cronologico con RTC antes del lanzamiento de octubre (confirmado con Vera antes del 1 agosto), el claim se puede gatear para esa funcion. Pero en el estado actual de informacion, el claim se rechaza para V1 sin condicion de espera adicional: la ausencia en los mockups es evidencia suficiente.

---

## Seccion 3 — Caveats literales para empaque / landing / video

Los textos que siguen son los que deben usar Solenne (SO-1 para copy) y los guionistas (Nerea para video). Son invariables: no se parafrasan, no se condensan mas alla de lo indicado para cada canal.

### Caveat H-01 — Formulacion de beneficio de proteccion (para todas las piezas, todas las audiencias)

**Para empaque tiro (espacio muy reducido):**
"El GME monitorea las condiciones electricas y actua ante sobrecarga, subcarga y variaciones de voltaje — segun el perfil del equipo conectado."

**Para landing y email (espacio amplio):**
"El GME detecta las variaciones electricas que danan equipos — y actua antes de que lleguen a la carga. Subcarga, sobrecarga, alto voltaje, bajo voltaje — segun el perfil del equipo que conectas. Refrigeracion, Bombas o Motores: el GME responde segun su modo."

**Para video / guion (narracion):**
"No es un protector que apaga cuando ya es tarde. Es un protector que mide, detecta la variacion antes de que dane el equipo — y actua segun si lo que conectas es una nevera, una bomba o un motor."

**Regla de invalidez del Caveat H-01:** Si qualquier pieza usa una variante de las formulaciones prohibidas listadas en #GME-04, el claim completo de proteccion debe detenerse y reformularse. El caveat H-01 no es opcional para las piezas que activen el beneficio de proteccion para el consumidor final.

### Caveat C-01 — Formulacion del webserver local (para cuando se desbloquee #GME-03)

**Version corta (empaque, espacio reducido):**
"Control desde cualquier browser en la misma red WiFi. Sin app. Sin cloud."

**Version completa (landing, email):**
"Control desde cualquier browser en la misma red WiFi. Sin app que instalar. Sin servidor en la nube. La proteccion actua independientemente de la conexion a internet." [Este texto solo es valido si engineering confirma Escenario favorable de Q2/Q3.]

**Version intermedia (si Q2 favorable pero Q3 adverso):**
"Control desde cualquier browser en la misma red WiFi. Sin app que instalar. Sin servidor en la nube para la interfaz de usuario. La proteccion actua ante variaciones electricas; la interfaz de monitoreo requiere red WiFi local activa."

### Caveat E-01 — Formulacion multi-aplicacion (para todas las piezas)

**Para empaque:** "Un protector. Tres modos: Refrigeracion, Bombas, Motores. Los parametros de proteccion preajustados segun el equipo que conectas."

**Para ficha tecnica y audiencia tecnica:** "Selector de modo R/B/M con parametros diferenciados por aplicacion: umbrales de subcarga, tiempos de reconexion y logica de reintento preconfigurados segun la carga. Modo Bombas incluye maniobra diaria activable."

### Caveat L-01 — Formulacion del log de fallas (para todas las piezas en V1)

**Para ficha tecnica:** "El GME registra el tipo de ultima falla para cada categoria de evento (subcarga, sobrecarga, alto voltaje, bajo voltaje, inestabilidad de frecuencia, rotor trancado — hasta 9 categorias). Sin historial cronologico con fecha y hora en V1."

**Para argumentario de ventas (P-09):** Igual que ficha tecnica, con adicion: "Historial cronologico con fecha y hora: en evaluacion para versiones futuras del firmware."

---

## Seccion 4 — Reglas de invalidez (condiciones que invalidan aprobaciones de hoy)

Las siguientes condiciones invalidan una decision aprobada de este gate. Cualquier agente del sistema (Vael, Aurelio, Solenne, Ivo) que detecte una de estas condiciones debe escalar a Raoul antes de continuar produccion.

### INV-01 — Engineering responde Q2 con resultado adverso (Claim C)
Si engineering confirma que la proteccion activa del GME requiere WiFi activo: Claim C pasa de SUSPENDIDO a ❌ RECHAZADO. Toda pieza que haya sido producida con el Claim C en cualquier escenario debe revisarse. Aurelio emite alerta de calendario porque P-03, P-04 y P-06 deben reformularse.

### INV-02 — Engineering responde Q3 con resultado adverso (Claim C — riesgo arquitectonico)
Si engineering confirma que el MCU de proteccion y el webserver comparten el mismo hilo critico sin watchdog independiente: Bruna requiere que el riesgo de seguridad del producto sea resuelto antes del lanzamiento. El gate del Claim C no se emite hasta que engineering confirme que el riesgo arquitectonico esta resuelto — independientemente del resultado de Q2.

### INV-03 — OL-3 segunda iteracion detecta competidor con la combinacion completa (Claim A)
Si Orlan encuentra en AliExpress, Alibaba o mercado LATAM un producto con V+I+WiFi+motor protections (subcarga, arranques/hora, multi-aplicacion) en el rango $20–50: Claim A pasa a ❌ RECHAZADO. El producto GME sigue siendo diferenciado en Venezuela (por marca, servicio, garantia local, soporte), pero el superlativo de "primero" no es defendible.

### INV-04 — Owner define 3 SKUs fisicos distintos (Claim #GME-05)
Si el Owner decide que los tres modos requieren hardware fisicamente distinto (Escenario B): el claim "un solo hardware, tres modos" es factualmente falso y debe retirarse de toda pieza donde aparezca. La formulacion "tres protectores especializados: Refrigeracion, Bombas, Motores — de la misma familia Exceline" puede sustituirlo.

### INV-05 — Naming finalista incluye superlativo o claim de posicion (Claim A o #GME-05)
Si el nombre comercial elegido por el Owner (deadline 30 mayo 2026) incluye una palabra que implica "primero", "unico", "mas completo" u otro superlativo: ese naming requiere gate adicional de Bruna antes de aparecer en cualquier material. La decision de naming es del Owner, pero el gate de Bruna sobre el nombre en si — si implica claim de posicion — es obligatorio antes de produccion.

### INV-06 — Engineering cambia specs del producto (cualquier claim)
Si engineering responde alguna de las 15 preguntas de Vera con un resultado que cambia materialmente las funciones del producto (ej. subcarga solo hace logging sin actuacion fisica, o multivoltaje confirmado 120V): Vera actualiza la tabla VE-1 y Bruna recibe el update para revisar los gates afectados. El criterio es: cualquier respuesta de engineering que contradiga un supuesto en el que se basa una decision de este gate invalida esa decision.

### INV-07 — Decision de naming genera conflicto SAPI VE preexistente
Si el nombre comercial elegido (GIM, SmartGuard, Sentinela, o cualquier otro) resulta tener registro previo en SAPI VE que impide su uso: el naming debe cambiarse antes de que cualquier pieza de marketing sea producida con ese nombre. Bruna no gestiona la busqueda SAPI — ese es trabajo del Owner o de asesoria legal de IP. Pero si el naming cambia despues de producida una pieza, todas las piezas con el nombre anterior deben ser retiradas o modificadas.

---

## Seccion 5 — Proximos pasos para Aurelio + produccion

### Gates BLOQUEANTES para piezas especificas con fecha objetivo

| Gate | Piezas bloqueadas | Fecha limite para resolver | Consecuencia si no resuelve |
|---|---|---|---|
| Naming Owner (#INV-05) | Todos los materiales con nombre de producto (P-01, P-02, P-03, P-04, P-06, P-07, P-08, P-09) | **30 mayo 2026** | Solenne (SO-1) no puede iniciar copy con nombre. Production delay de toda la campana. |
| Claim H formulacion exacta (#GME-04) | P-01, P-02, P-03, P-04 — cualquier pieza con beneficio de proteccion para consumidor | **Resuelto con este gate — puede avanzar YA** | Solenne puede usar los caveats H-01 aprobados en esta entrada. No hay bloqueo adicional. |
| Claim C gate Bruna (#GME-03) | P-03 empaque (si se incluye el claim), P-04 landing, P-06 video WiFi demo | **15 julio 2026** (respuesta engineering Q2/Q3) + gate final Bruna | Si no resuelve antes del 15 julio: P-03 empaque con solo Claim D (formulacion acotada). P-04 landing con formulacion de webserver sin afirmar independencia WiFi. P-06 sin afirmar "sin cloud" hasta gate. |
| Claim B gate Bruna (#GME-02) | P-05 ficha tecnica, P-07 video R/B/M (si menciona el claim B explicitamente) | **15 julio 2026** (respuesta engineering Q15 + Q8) + gate Bruna | P-05 se lanza sin claim B o con formulacion reducida. P-07 puede producirse enfocando el argumento en los tres modos (Claim E aprobado) sin usar "integral". |
| Claim A gate Bruna (#GME-01) | P-04 landing (version con superlativo), P-01 post (version con "primero") | **Semana 4 mayo 2026** (OL-3 segunda iteracion) + gate Bruna | P-04 landing y P-01 post se producen sin el superlativo "primero" — usan el territorio diferenciado sin superlativo hasta que Bruna gate el Claim A. No hay bloqueo critico de calendario. |
| Empaque P-03 en imprenta | P-03 empaque — todos los SKUs R/B/M | **1 septiembre 2026** (en imprenta) | Oz debe recibir el brief a mas tardar primera semana de julio. Si naming no esta confirmado al 30 mayo, el brief a Oz se comprime peligrosamente. |

### Resumen de estado para Solenne (SO-1) — que puede usar YA vs. que espera

**PUEDE USAR YA (sin gate adicional):**
- Claim D: "El estado de tu equipo desde tu browser — voltaje, corriente, frecuencia y ultima falla, en tiempo real desde la misma red WiFi." (scope red local, sin "desde cualquier parte")
- Claim E formulacion basica: "Un protector. Tres modos: Refrigeracion, Bombas, Motores." (sin superlativo de exclusion)
- Caveat H-01: formulaciones de accion verificable de proteccion (sin garantia de resultado)
- Caveat L-01: formulacion honesta del log de fallas V1
- Pricing claim: "Las funciones que antes costaban cientos de dolares — ahora a precio de herramienta profesional." (sin comparativo de marca en empaque)

**ESPERA GATE (no producir con estos claims hasta gate Bruna explicito):**
- Claim A ("primero en Venezuela/LATAM en este rango de precio") — espera OL-3 segunda iteracion
- Claim B ("proteccion integral") — espera engineering Q15 + Q8
- Claim C ("sin cloud requerida" en su formulacion completa) — espera engineering Q2 + Q3

**PROHIBIDO SIN EXCEPCION:**
- Cualquier formulacion de garantia de resultado de proteccion del equipo
- "Visibilidad total" (#GME-06 rechazado)
- "Tan preciso como instrumentacion profesional" (#GME-07 rechazado)
- "Multivoltaje 120/220" (#GME-09 rechazado en V1)
- "Sensibilidad <1 s" (#GME-10 rechazado sin dato engineering)
- "Historial de las ultimas 20 fallas con fecha y hora" (#GME-11 rechazado en V1)
- Comparativos directos de marca en empaque fisico y materiales publicos (BR-5 Precedente #3)
- Mencionar ESP32 por nombre en materiales publicos (riesgo de activar objecion de precio)

---

## Seccion 6 — Recomendacion de proceder / esperar

### Piezas que pueden arrancar produccion YA

Las siguientes piezas pueden entrar a produccion ejecutable sin necesidad de esperar mas gates:

- **P-07 — Video aplicacion R/B/M:** El claim E (tres modos) esta aprobado en su formulacion basica. Nerea puede empezar el guion NE-1 usando el territorio de multi-aplicacion sin superlativo. El video no depende del Claim C ni del Claim B — puede estructurarse como demostracion de los tres modos con los parametros verificables de los mockups.

- **P-08 — Carrusel GAM → GME:** La logica de "evolucion del portafolio Exceline" no depende de ningun claim suspendido. El argumento de "la siguiente generacion del GAM-B220" es plenamente aprobado. El carrusel puede producirse con los claims D y E aprobados.

- **P-09 — Material de training para distribuidores (3 piezas):** El argumentario de canal (reemplazo del GAM, un SKU tres aplicaciones, precio lista) no depende de claims suspendidos. Los datos comparativos directos de precio (Littelfuse 77C vs GME) pueden incluirse en la pieza B (argumentario interno al distribuidor). Solenne puede iniciar SO-2 para P-09 en paralelo con la decision de naming.

- **P-02 — Email comunidad Exceline Profesional (sin Claim A y sin Claim C completo):** El email puede producirse con los claims D y E aprobados, el Caveat H-01 aprobado, y sin el superlativo "primero". Un email de lanzamiento tecnico enfocado en los tres modos y el webserver local (formulacion D) tiene sustancia suficiente sin necesidad de esperar gates adicionales.

### Piezas que deben esperar gates especificos

- **P-03 — Empaque fisico (gate critico: imprenta antes del 1 septiembre):** Puede disenar a nivel de layout y paleta visual YA (identidad Exceline Profesional aprobada, Oz puede iniciar el arte con los claims aprobados). El copy del empaque puede incluir Claim D, Claim E, Caveat H-01. Si el naming se confirma antes del 30 mayo y Claim C se resuelve antes del 15 julio, el empaque puede tener el claim completo. Si Claim C no se resuelve antes del 15 julio, el empaque va a imprenta sin ese claim — con solo el claim D de webserver acotado a red local.

- **P-04 — Landing producto:** Puede disenar estructura y wireframe YA. El copy con el superlativo "primero" espera el gate del Claim A (OL-3 segunda iteracion). El copy de la landing puede lanzarse al dia del lanzamiento con el Claim A o sin el — no es gate critico de calendario.

- **P-05 — Ficha tecnica:** BLOQUEADA hasta respuesta engineering Q2/Q7/Q8–Q9. No hay copy de ficha tecnica posible sin esos datos. Se emite en version reducida si no llegan antes del 1 agosto.

- **P-06 — Video WiFi demo:** El guion NE-2 puede prepararse YA para la formulacion D (webserver local, red local, sin afirmar sin cloud hasta gate C). Si el Claim C se resuelve favorablemente antes del 15 julio, el guion se actualiza con la version completa. Si no, el video va a produccion con el scope acotado.

- **P-01 — Post LinkedIn con superlativo "primero":** Espera Claim A. La version tecnica de P-01 sin superlativo puede producirse YA.

---

## Seccion 7 — Tabla resumen de decisiones

| # | Claim | Categoria | Pieza(s) afectada | Caveat literal | Dependencia | Prioridad de resolucion | Precedente BR-5 |
|---|---|---|---|---|---|---|---|
| #GME-01 | "Primero en Venezuela/LATAM en este rango" | ⏸ SUSPENDIDO | P-04 landing, P-01 (version superlativo) | Scope geografico acotado + rango de precio en el mismo claim | OL-3 2a iteracion + Vera Q confirmacion specs | **Alta** — naming deadline 30 mayo + lanzamiento | BR-5 #1, #2 |
| #GME-02 | "Proteccion integral V+I+subcarga+arranques/hora" | ⏸ SUSPENDIDO | P-05 ficha tecnica, P-07 video | Reintentos + confirmacion de actuacion fisica por funcion | Engineering Q15 + Q8 antes del 15 julio | **Alta** — P-05 deadline 1 agosto | — |
| #GME-03 | "Sin app. Sin cloud requerida." | ⏸ SUSPENDIDO | P-03 empaque, P-04 landing, P-06 video | 3 caveats C-01 segun escenario Q2/Q3 | Engineering Q2 + Q3 antes del 15 julio | **Alta critica** — P-03 imprenta 1 sept | — |
| #GME-04 | Formulacion de "proteccion del equipo/negocio" | ⚠ APROBADO CON CAVEAT (formulacion accion) / ❌ RECHAZADO (garantia) | P-01, P-02, P-03, P-04 — todas las piezas | Caveats H-01 textuales — invariables | Ninguna adicional — puede avanzar YA | Resuelto | BR-5 #4 |
| #GME-05 | "Un solo hardware, tres modos" | ⚠ APROBADO CON CAVEAT (formulacion basica) / ⏸ SUSPENDIDO (superlativo exclusion) | P-03, P-07, P-08, P-09 | Caveat E-01 — invariable | Decision Owner: 1 hardware vs 3 SKUs (deadline 15 junio) | **Alta** — afecta P-03 empaque | BR-5 #2 |
| #GME-06 | "Visibilidad total desde el celular" | ❌ RECHAZADO | Todas las piezas | — | Ninguna — rechazado sin alternativa hasta RTC+log cronologico | Resuelto | — |
| #GME-07 | "Tan preciso como instrumentacion profesional" | ❌ RECHAZADO | Todas las piezas | — | Engineering Q8 para alternativa modesta | Resuelto | — |
| #GME-08 | Pricing claim democratizacion | ⚠ APROBADO CON CAVEAT | P-03 empaque, P-04 landing, P-09 argumentario | "Las funciones que antes costaban cientos de dolares — ahora a precio de herramienta profesional" | Ninguna adicional | Resuelto | BR-5 #3 (para formato comparativo en P-09) |
| #GME-09 | "Multivoltaje 120/220V" | ❌ RECHAZADO V1 | Todas las piezas V1 | — | Engineering Q10 para habilitacion V2 | Baja (V2/roadmap) | — |
| #GME-10 | "Sensibilidad <1 s ante fluctuaciones" | ❌ RECHAZADO | Todas las piezas | — | Engineering Q1 para alternativa con dato | Media — fecha 1 agosto | BR-5 #1 (si dato confirma) |
| #GME-11 | "Historial 20 fallas con fecha y hora" | ❌ RECHAZADO V1 | Todas las piezas V1 | Caveat L-01 para piezas tecnicas | Engineering Q4 + Q5 para V2 | Media — no es gate de lanzamiento V1 | — |

---

## Notas finales de Bruna

### Riesgo de mayor magnitud identificado en este gate

El riesgo de mayor magnitud en este lanzamiento no es ninguno de los claims de marketing: es la combinacion de la arquitectura del Claim C (operacion offline del GME sin WiFi) con la logica de tres intentos del Claim B. Si el GME requiere WiFi para activar la proteccion Y hace dos reintentos antes de bloquear definitivamente, un equipo instalado en un entorno sin WiFi estable puede sufrir dos arranques destructivos sin proteccion efectiva — y el marketing de "sin cloud requerida" puede ser invocado como prueba de que el usuario fue inducido a creer que el equipo quedaba protegido en cualquier condicion de conectividad.

Este riesgo no es un riesgo de comunicacion — es un riesgo de diseno del producto que tiene consecuencias de comunicacion. Bruna lo identifica y lo eleva a Raoul para que Owner lo discuta con el equipo de engineering como prioridad critica, independientemente de lo que se decida sobre los claims.

### Tratamiento del riesgo de objecion del tecnico sofisticado (ESP32)

La objecion del tecnico que conoce IoT ("un ESP32 a $10 y lo programo yo") no genera ninguna restriccion de claim en este gate — porque no es un claim del GME, es una objecion de precio que se responde con argumento de valor. Bruna confirma que la linea de respuesta de Vael (VA-5 §ESP32) es correcta y no requiere caveat ni aprobacion adicional de Bruna: es argumentario de ventas, no claim de marketing publico.

### Sobre certificaciones

Las certificaciones del GME estan "[pendiente engineering]" (Vera §5 Q12). Bruna ratifica que no puede aprobarse ningun claim de certificacion (CE, IEC, UL, FCC, COVENIN) hasta que el Owner confirme que la certificacion esta emitida, vigente y aplica a los modelos especificos del lanzamiento. El tratamiento es identico al establecido en la entrada #13 del BR-2 Genteca (empaque GSM). Si el scope geografico del lanzamiento incluye Colombia desde el dia 1, las certificaciones pasan de tema sensible a gate bloqueante para el canal ferretero colombiano bajo RETIE.

### Escalacion a asesoria legal externa

Este gate no requiere asesoria legal externa en el estado actual de informacion. Los claims gateados aqui son defensibles con el marco interno de RISK-POLICY y los precedentes BR-5 vigentes. Sin embargo, si el Owner decide incluir en el empaque o en la landing algun tipo de garantia de durabilidad del equipo conectado (ej. "garantia de 1 ano si el equipo se dana con el GME instalado") o si el lanzamiento se extiende a Colombia con claims de certificacion pendientes, Bruna requiere que el Owner consulte asesoria legal externa antes de ese claim especifico. No es el caso hoy — pero es el escenario que lo activaria.

---

*Bruna — Risk & Claims Governance Lead | Dominio Genteca | 2026-05-06*
*Output BR-2 especifico campana GME v1*
*Ruta: `C:\RAUL\03-projects\genteca\2025-04_GME_estudios-mercado\_intel\Bruna_gate_GME_2026-05-06.md`*
*Candidato a incorporar al log acumulativo `03-projects/genteca/_governance/2026-05-03_genteca_claim-approval-log_v1.md` — decision Celeste.*
