# Claim Approval / Rejection Log — Genteca
**Mantenido por:** Bruna — Risk & Claims Governance Lead
**Ubicacion canonica:** `03-projects/genteca/_governance/`
**Ultima actualizacion:** 2026-05-03

---

## Entradas

### #1 — 2026-05-03 — "El mas rapido ante parpadeos (< 0,03 s)"

- **Claim evaluado (texto exacto):** "El mas rapido ante parpadeos (< 0,03 s)"
- **Producto / pieza:** Empaque frente (tiro) — GSM-MB / GSM-RB / GSM-RF / GSM-RE
- **Decision:** Aprobado con caveat
- **Caveat textual obligatorio:** "El tiempo de desconexion de menos de 30 milisegundos (< 0,03 s) aplica ante parpadeos (fluctuaciones rapidas del voltaje de la red electrica) e inestabilidad de la red. No aplica a la desconexion ante sobre voltaje o bajo voltaje pronunciados, cuyo tiempo de desconexion es de 0,4 a 3 segundos segun la intensidad de la falla. Segun especificacion tecnica del laboratorio I&D Genteca."
- **Condicion de produccion:** I&D debe emitir datasheet actualizado con el valor < 30 ms documentado antes de imprimir el empaque.
- **Rationale:** Dato cuantitativo confirmado por Owner como medicion formal de laboratorio (cierra Vera P-2). Ningun competidor venezolano publica dato comparable. WellSpec (mas agresivo) publica 200-300 ms. Superlativo + dato cuantitativo es la formulacion mas defensible.
- **Criterio aplicado:** Superlativo con dato cuantitativo verificable en mercado con alta opacidad competitiva.
- **Precedente BR-5 referenciado:** BR-5 Precedente #1 — sentado por esta decision.
- **Evidencia consultada:** Vera_brief_tecnico_v1 §2.2-§2.3; Orlan_competencia_v1 Secciones 1 y 7; WORKSTREAM_v5 §Datos tecnicos confirmados.
- **Scope:** Empaque fisico (tiro) linea Exceline GSM-MB / GSM-RB / GSM-RF / GSM-RE. Lanzamiento Q2 2026.

---

### #2 — 2026-05-03 — "El unico en proteger tecnologia inverter"

- **Claim evaluado (texto exacto):** "El unico en proteger tecnologia inverter"
- **Producto / pieza:** Propuesta de empaque frente (tiro) — GSM-MB / GSM-RB / GSM-RF / GSM-RE
- **Decision:** Rechazado
- **Alternativa propuesta:** "Protege tecnologia Inverter" (sin superlativo — ver #3)
- **Rationale:** Factualmente falso. Avtek, Breakermatic y JVTRONIC ya comunican "para tecnologia inverter" con lineas especificas. El claim "unico" es verificablemente incorrecto y daria a la competencia un argumento trivial para cuestionar la credibilidad del empaque.
- **Criterio aplicado (BR-5 Precedente #2):** Superlativo de exclusion sin evidencia de ausencia universal del atributo en competidores — rechazado sin excepcion.
- **Evidencia consultada:** Orlan_competencia_v1 Seccion 4.
- **Scope:** Empaque fisico linea Exceline GSM — aplica a todos los canales publicos.

---

### #3 — 2026-05-03 — "Protege tecnologia Inverter" (sin superlativo)

- **Claim evaluado (texto exacto):** "Protege tecnologia Inverter"
- **Producto / pieza:** Empaque frente (tiro) — GSM-MB / GSM-RB / GSM-RF / GSM-RE
- **Decision:** Aprobado con caveat
- **Caveat textual obligatorio:** "La proteccion ante parpadeos (fluctuaciones rapidas del voltaje de la red) que ofrece este protector es especialmente beneficiosa para equipos con tecnologia inverter, cuya electronica de control es sensible a variaciones rapidas del voltaje. Este protector no reemplaza la proteccion contra transientes de alta energia (descargas atmosfericas, conmutacion inductiva) presente en el equipo inverter de fabrica. Ambas protecciones son complementarias."
- **Condicion de uso:** Debe aparecer en tiro en proximidad visual al dato "< 0,03 s". Sin esa proximidad, mover al retiro como bullet de caracteristicas.
- **Rationale:** Claim no exclusivo (Avtek y Breakermatic lo usan), pero el RTB diferenciador (velocidad < 30 ms que protege la electronica inverter ante parpadeos) si es exclusivo de Genteca. La proximidad visual crea el argumento de causa-efecto diferenciador.
- **Criterio aplicado:** Claim de aplicacion con paridad competitiva — aprobado cuando el RTB diferenciador esta en proximidad visual.
- **Evidencia consultada:** Vera_brief_tecnico_v1 §2.4; Orlan_competencia_v1 Seccion 4.
- **Scope:** Empaque fisico (tiro) — linea Exceline GSM. Q2 2026.

---

### #4 — 2026-05-03 — "Sensor NTC incorporado*"

- **Claim evaluado (texto exacto):** "Sensor NTC incorporado*"
- **Producto / pieza:** Empaque frente (tiro) — GSM-MB / GSM-RB / GSM-RF / GSM-RE
- **Decision:** Aprobado con caveat (asterisco obligatorio)
- **Caveat textual obligatorio (bloque condensado de retiro):** "Sensor NTC: sensor de temperatura ubicado junto al rele de potencia. Detecta calentamiento excesivo (a partir de 60 degC internos) causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos), y desconecta la carga para proteger al protector mismo y al cableado de la instalacion. Para cargas de baja demanda de corriente, el sensor NTC protege al protector y al cableado, pero no actua como proteccion de sobrecarga directa de la carga conectada. Funciona como capa adicional de proteccion termica; no reemplaza al interruptor termomagnetico de la instalacion."
- **Rationale:** NTC existe, ubicacion junto al rele confirmada por Owner y Canudas, mecanismo verificado por Vera. Territorio en blanco de comunicacion (ningun competidor lo usa). Asterisco es condicion necesaria para evitar interpretacion incorrecta del 40% del mercado que confunde "proteccion termica" con proteccion del motor.
- **Criterio aplicado:** Claim tecnico con riesgo de interpretacion incorrecta — aprobado con caveat de retiro obligatorio.
- **Evidencia consultada:** Vera_brief_tecnico_v1 §1.1-§1.4; Orlan_competencia_v1 Seccion 3; WhatsApp Canudas 02-05-2026.
- **Scope:** Empaque fisico (tiro + retiro) — linea Exceline GSM. Q2 2026.

---

### #5 — 2026-05-03 — "Autoproteccion termica"

- **Claim evaluado (texto exacto):** "Autoproteccion termica"
- **Producto / pieza:** Empaque frente (tiro) — alternativa al badge NTC en Alt. B o C
- **Decision:** Aprobado
- **Caveat textual obligatorio:** Mismo bloque de retiro que entry #4 si se usa como alternativa a "Sensor NTC incorporado*".
- **Rationale:** Describe con precision la funcion primaria del NTC (el protector se autoprotege). Prefijo "auto" corrige activamente el malentendido del 40% del mercado. Tecnicamente honesto y diferenciado.
- **Criterio aplicado:** Afirmacion descriptiva de funcion verificada sin riesgo de over-claim.
- **Evidencia consultada:** Vera_brief_tecnico_v1 §1.3(a); Orlan §6.3.
- **Scope:** Empaque fisico (tiro) — linea Exceline GSM. Q2 2026.

---

### #6 — 2026-05-03 — "Nuevo. La Proteccion mas completa" (lengueta)

- **Claim evaluado (texto exacto):** "Nuevo. La Proteccion mas completa"
- **Producto / pieza:** Lengueta tiro empaque — GSM-MB / GSM-RB / GSM-RF / GSM-RE
- **Decision:** Aprobado con caveat
- **Caveat arquitectonico obligatorio:** El superlativo "La Proteccion mas completa" esta aprobado condicionado a que los tres sub-claims (Claim A + Claim C + Claim D) esten visibles en el mismo tiro. Si alguno de los tres es eliminado del tiro por restricciones de espacio, la lengueta debe ajustarse a "Nuevo. Una proteccion mas completa".
- **Rationale:** "La" (superlativo absoluto) aprobado porque los tres sub-claims que lo sustentan — velocidad, inverter, NTC — estan aprobados y ningun competidor venezolano los tiene simultaneamente. La dependencia estructural lengueta/sub-claims es una fortaleza arquitectonica.
- **Criterio aplicado:** Superlativo cualitativo aprobado cuando los sub-claims verificables que lo sustentan estan presentes en el mismo empaque.
- **Evidencia consultada:** Vera_brief_tecnico_v1 §3.1; Orlan_competencia_v1 Secciones 1, 3, 4.
- **Scope:** Empaque fisico (lengueta tiro) — linea Exceline GSM. Q2 2026.

---

### #7 — 2026-05-03 — "Respaldo del breaker termomagnetico"

- **Claim evaluado (texto exacto):** "Respaldo del breaker termomagnetico"
- **Producto / pieza:** Material off-empaque (QR / argumentario de ventas / sustento de Junta)
- **Decision:** Aprobado solo off-empaque
- **Texto aprobado para off-empaque:** "El Sensor NTC actua como una capa adicional de proteccion termica que respalda al interruptor termomagnetico de la instalacion. No reemplaza al breaker ni a ninguna proteccion de sobrecorriente del circuito. La correcta seleccion y calibracion del breaker termomagnetico por parte del instalador sigue siendo indispensable."
- **Rationale:** Tecnicamente correcto y util para el instalador. En el empaque introduce al breaker como actor que el consumidor residencial no comprende en ese contexto y complejiza el mensaje innecesariamente.
- **Criterio aplicado:** Claim correcto pero inapropiado para el canal empaque por complejidad de mensaje para audiencia mixta.
- **Evidencia consultada:** Vera_brief_tecnico_v1 §4 Caveat 1; WORKSTREAM_v5 §Encuadre tecnico NTC.
- **Scope:** Excluido del empaque fisico. Permitido en QR, argumentario, sustento Junta. Q2 2026.

---

### #8 — 2026-05-03 — "Protege al motor" / "Protege a la carga"

- **Claim evaluado (texto exacto):** "Protege al motor" / "Protege a la carga"
- **Producto / pieza:** Cualquier material de comunicacion de la linea Exceline GSM
- **Decision:** Rechazado sin alternativa en empaque
- **Alternativa propuesta:** No existe formulacion honesta equivalente para empaque. Para canales con espacio suficiente para caveats extensos: puede describirse la proteccion del rele y el cableado, aclarando que para cargas de baja demanda la carga misma no queda protegida directamente.
- **Rationale:** Vera §1.4 es inequivoco: el NTC solo actua como proteccion de sobrecarga de la carga cuando la corriente se aproxima al nominal del protector (~20 A). Para cargas pequenas, la carga no queda protegida. La sobrepromesa es verificable y puede generar reclamos legitimos. Prohibicion sin excepciones.
- **Criterio aplicado:** Sobrepromesa tecnica verificablemente incorrecta para el universo completo de casos de uso.
- **Evidencia consultada:** Vera_brief_tecnico_v1 §1.4; delta_v4 §4.
- **Scope:** Prohibido en empaque y todos los materiales publicos. Q2 2026 y adelante.

---

### #9 — 2026-05-03 — "Uno de los mas rapidos"

- **Claim evaluado (texto exacto):** "Uno de los mas rapidos"
- **Producto / pieza:** Cualquier material de comunicacion de la linea Exceline GSM
- **Decision:** Rechazado
- **Alternativa propuesta:** "El mas rapido ante parpadeos (< 0,03 s)" (entry #1)
- **Rationale:** Prohibicion explicita del Owner 2026-05-03. El paisaje competitivo respalda el superlativo absoluto; la formulacion debil es innecesaria ademas de estrategicamente contraria a la posicion de liderazgo de Genteca.
- **Criterio aplicado (BR-5 Precedente #1):** Prohibicion Owner ratificada; superlativo debil innecesario cuando el dato propio es el mas alto conocido.
- **Evidencia consultada:** WORKSTREAM_v5 §Regla de gateo; Orlan_competencia_v1 Seccion 2.
- **Scope:** Prohibido en todos los materiales de comunicacion. Vigente como politica permanente salvo revision Owner.

---

### #10 — 2026-05-03 — "El mas rapido de la categoria" (Alternativa C Vael)

- **Claim evaluado (texto exacto):** "El mas rapido de la categoria"
- **Producto / pieza:** Lengueta tiro empaque Alternativa C — GSM-MB / GSM-RB / GSM-RF / GSM-RE
- **Decision:** Aprobado con caveat
- **Caveat textual obligatorio:** Mismo que entry #1 (caveat de retiro del Claim A — acotacion a parpadeos, referencia a I&D, tiempo de sobre/subtension de 0,4-3 s).
- **Condicion de produccion:** Igual que entry #1 — datasheet I&D actualizado antes de imprimir.
- **Rationale:** "De la categoria" (protectores enchufables residenciales monofasicos) es equivalente a "ante parpadeos" en terminos de campo de comparacion. Mismo RTB, mismo criterio, misma condicion.
- **Criterio aplicado (BR-5 Precedente #1):** Igual que entry #1.
- **Evidencia consultada:** Vera_brief_tecnico_v1 §2.2; Orlan_competencia_v1 Secciones 1 y 2.
- **Scope:** Empaque fisico (lengueta tiro) Alternativa C — linea Exceline GSM. Q2 2026.

---

### #11 — 2026-05-03 — "Actua en < 0,03 s antes de que la fluctuacion llegue a tu equipo" (Alternativa C Vael)

- **Claim evaluado (texto exacto):** "Actua en < 0,03 s antes de que la fluctuacion llegue a tu equipo"
- **Producto / pieza:** Frase dominante empaque Alternativa C — GSM-MB / GSM-RB / GSM-RF / GSM-RE
- **Decision:** Aprobado con caveat
- **Caveat textual obligatorio:** Mismo que entry #1 (acotacion a parpadeos, no sobre/subtension).
- **Condicion de produccion:** Igual que entry #1 — datasheet I&D actualizado antes de imprimir.
- **Rationale:** La frase describe el mecanismo sin sobrepromesa de resultado. No afirma que el equipo queda protegido; afirma que el protector actua en ese tiempo ante la fluctuacion. Es la formulacion mas honesta de beneficio para el consumidor final.
- **Criterio aplicado:** Afirmacion de mecanismo verificado con dato cuantitativo — aprobado con caveat de acotacion.
- **Evidencia consultada:** Vera_brief_tecnico_v1 §2.2; Orlan_competencia_v1 Secciones 1 y 2.
- **Scope:** Empaque fisico Alternativa C — linea Exceline GSM. Q2 2026.

---

### #12 — 2026-05-03 — "Garantiza la proteccion del equipo" / "evita danos" (rechazo preventivo)

- **Claim evaluado (texto exacto):** "Garantiza la proteccion del equipo" / "evita danos al equipo" / formulaciones equivalentes de garantia de resultado
- **Producto / pieza:** Cualquier material de comunicacion de la linea Exceline GSM
- **Decision:** Rechazado preventivo
- **Alternativa propuesta:** Describir el mecanismo de proteccion sin afirmar resultado garantizado: "actua en < 0,03 s ante parpadeos", "protege al protector mismo y al cableado", "especialmente beneficioso para equipos inverter".
- **Rationale:** Garantia de resultado de proteccion del equipo implica obligacion legal bajo la Ley de Proteccion al Consumidor y al Usuario venezolana (Arts. sobre garantias implicitas y responsabilidad por producto). No existe RTB tecnico que sostenga proteccion universal del equipo ante todos los fenomenos que pueden danarlo. Rechazo preventivo antes de que aparezca en copy de Solenne.
- **Criterio aplicado (BR-5 Precedente #4):** Garantia de resultado sin RTB especifico — rechazado sin revision legal externa.
- **Evidencia consultada:** Vael VA-5 §11 (temas sensibles — garantias).
- **Scope:** Prohibido en todos los materiales publicos de la linea Exceline GSM y de cualquier producto Genteca salvo revision legal especifica.

---

### #13 — 2026-05-03 — Claims de certificacion IEC / COVENIN (bloqueado)

- **Claim evaluado (texto exacto):** Cualquier referencia a "certificado IEC [numero]", "aprobado COVENIN [numero]" o equivalente para los modelos GSM-MB / GSM-RB / GSM-RF / GSM-RE
- **Producto / pieza:** Empaque — GSM-MB / GSM-RB / GSM-RF / GSM-RE
- **Decision:** Gate bloqueado — pendiente confirmacion Owner
- **Rationale:** El datasheet GSM-RE menciona IEC 1000-4-x y COVENIN. Orlan §8 (Expuesto) señala que las certificaciones no estan completamente verificadas para los modelos MB/RB/RF/RE especificamente. Bruna no puede gatear un claim de certificacion sin verificar que la certificacion existe, esta vigente y aplica a los modelos especificos del empaque. Si Solenne o Oz quieren incluir mencion de certificacion, el Owner debe confirmar que normas estan certificadas y con que numero de certificado para estos modelos.
- **Criterio aplicado:** Claim regulatorio — requiere evidencia documental especifica antes de aprobacion.
- **Evidencia consultada:** Orlan_competencia_v1 §8 (Expuesto); Vera Pendiente P-1.
- **Scope:** Bloqueado hasta confirmacion del Owner. Q2 2026.

---

---

### #14 — 2026-05-05 — "Autoproteccion termica activa*" (tiro Alternativa B sin NTC)

- **Claim evaluado (texto exacto):** "Autoproteccion termica activa*" (tiro) + caveat de retiro segun §8.3 de Bruna_gate_empaque_v1
- **Producto / pieza:** Empaque Alternativa B — tiro (badge funcion termica) + retiro (asterisco) — GSM-MB / GSM-RB / GSM-RF / GSM-RE
- **Trigger:** Junta elige Alternativa B. Observacion Canudas: "Sensor NTC incorporado" revela secreto industrial. Vael propone formulacion "Autoproteccion termica activa*" como finalista unica.
- **Decision:** Aprobado con caveat — condicional suspensiva a Vera (Pendiente P-5)
- **Caveat textual obligatorio (palabra por palabra):** "Autoproteccion termica activa: sensor de temperatura ubicado junto al rele de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se danen. Protege al protector mismo y a la instalacion electrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actua como proteccion de sobrecarga directa de la carga conectada. Funciona como capa adicional de proteccion termica; no reemplaza al interruptor termomagnetico de la instalacion."
- **Condicion suspensiva (flag Vera P-5):** Si Vera confirma que el NTC es fusible termico de corte unico (no reutilizable tras actuar), el tiro debe cambiar a "Autoproteccion termica*" (Claim E, #5 de este log, sin condicion). El cuerpo del caveat de retiro es invariable; solo cambia el encabezado.
- **Formulacion de respaldo (si P-5 = fusible unico):** "Autoproteccion termica*" (aprobado sin condicion — entrada #5 de este log).
- **Rationale:** Extension razonable del Claim E (#5, aprobado 2026-05-03). El adjetivo "activa" es tecnicamente plausible: el mecanismo de curva de tiempo inverso del NTC (confirmado en Vera §1.2 y WhatsApp Canudas) es consistente con operacion continua. El caveat de retiro no promete continuidad ni reutilizacion; describe la funcion sin comprometer el mecanismo especifico. El riesgo tecnico (nivel bajo/medio) queda mitigado por el caveat. El riesgo reputacional es bajo: el termino es vacante en el mercado VE (Orlan OL-1 §3). El riesgo regulatorio es bajo: no existe norma venezolana que defina "proteccion activa" para este tipo de dispositivo. Nivel global: bajo con condicion suspensiva.
- **Cláusula / criterio RISK-POLICY aplicado:** RISK-POLICY v1.0 §3 (principio de no afirmar datos que puedan ser falsos) — aplicado como fundamento para la condicion suspensiva sobre P-5. Criterio Bruna sobre extension de claim: adicion de calificador de modo sin nuevo claim de resultado no constituye claim nuevo.
- **Precedente BR-5 referenciado:** Sin precedente directo existente para "formulacion de funcion sin componente". Este caso es candidato a Precedente #5 del BR-5 transversal (pendiente confirmacion P-5 para formalizacion).
- **Evidencia consultada:** Vael_VA-5_naming-funcion-termica_v1 (finalista unica); Orlan_OL-1_competencia-naming-termico_v1 §3-§4; Bruna_gate_empaque_v1 §2 Claim E + §7.1; Vera_brief_tecnico_v1 §1.1-§1.4; WhatsApp Canudas (curva tiempo inverso); BR-5 Precedentes #1-#4.
- **Scope:** Empaque fisico Alternativa B — tiro + retiro — GSM-MB / GSM-RB / GSM-RF / GSM-RE. Lanzamiento Q2 2026. Condicion suspensiva aplica al arte final de imprenta; no es bloqueante para memo de Junta 2026-05-06.

---

---

## Bloque GME — Gate campana lanzamiento octubre 2026 (2026-05-06)

**Referencia:** `Bruna_gate_GME_2026-05-06.md` en `03-projects/genteca/GME Estudios de mercado/_intel/` — archivo fuente con rationale completo, caveats literales, reglas de invalidez y proximos pasos. Las entradas que siguen son el resumen de decisiones para trazabilidad del log acumulativo.

---

### #15 — 2026-05-06 — Claim A GME: "Primero en Venezuela/LATAM en este rango de precio"

- **Claim evaluado (texto exacto):** "Primer protector monofasico inteligente con WiFi y medicion de voltaje y corriente a precio accesible en Venezuela / LATAM"
- **Producto / pieza:** GME-R220 / GME-B220 / GME-M220 — P-04 landing, P-01 post LinkedIn (version superlativo)
- **Decision:** SUSPENDIDO — pendiente OL-3 segunda iteracion (busqueda profunda AliExpress/chino OEM) + confirmacion specs engineering en firmware produccion
- **Caveat textual (cuando se desbloquee):** Scope geografico acotado + rango de precio integrado en el mismo claim: "El primer protector monofasico en Venezuela con medicion de voltaje y corriente, WiFi y configuracion multi-aplicacion en el rango de precio accesible."
- **Rationale:** OL-3 v1 no encontro competidor en $30–60 con la combinacion completa — vacancia verificada en fuentes primarias. Sin embargo, la busqueda del mercado chino OEM fue declarada superficial (OL-3 Limite 1). Superlativo de posicion no se gateable sin exhaustividad razonable de la busqueda. Scope "en LATAM" o "en el mundo" rechazado hasta busqueda sistematica adicional.
- **Criterio aplicado:** BR-5 Precedente #1 (superlativo con dato cuantitativo en mercado opaco — aplicable una vez resuelta la dependencia de OL-3). BR-5 Precedente #2 (superlativo de exclusion requiere ausencia verificada).
- **Evidencia consultada:** OL-3 v1 §Seccion 3 y §Limites; Vera VE-1 §Supuesto 1; VA-5 §Claim A; AU-1 §7.1.
- **Scope:** GME — campana lanzamiento octubre 2026. Piezas P-04 y P-01 (version superlativo).

---

### #16 — 2026-05-06 — Claim B GME: "Proteccion integral V+I+subcarga+arranques/hora"

- **Claim evaluado (texto exacto):** "Proteccion integral: voltaje + corriente + subcarga + arranques por hora en un solo protector monofasico"
- **Producto / pieza:** GME — P-05 ficha tecnica, P-07 video R/B/M
- **Decision:** SUSPENDIDO — condicionado a engineering Q15 (logica tres intentos) + Q8 (confirmacion actuacion fisica de cada funcion)
- **Caveat textual (cuando se desbloquee):** "Proteccion activa ante voltaje, corriente, subcarga y arranques excesivos — con logica de reintentos inteligente antes del bloqueo de seguridad." La mencion de reintentos es obligatoria en el claim o en proximidad inmediata.
- **Rationale:** El conjunto V+I+subcarga+arranques/hora es el mas diferenciado del portafolio GME (OL-3 §Diferenciado). El bloqueo es: (a) necesidad de confirmar que cada funcion activa el contactor fisicamente (no solo logging), y (b) logica de tres intentos antes del bloqueo que debe comunicarse — no ocultarse — para evitar brecha entre expectativa y comportamiento real.
- **Criterio aplicado:** RISK-POLICY v1.0 §3 (no afirmar datos que puedan ser falsos) — aplicado a la funcion de actuacion fisica no confirmada. BR-5 Precedente #4 (analogia: no comunicar un comportamiento de proteccion que no se corresponde con el resultado real para el usuario).
- **Evidencia consultada:** Vera VE-1 §4 Claim B; OL-3 §Seccion 3; VA-5 §Claim B; comentarios encuesta.
- **Scope:** GME — P-05 y P-07. Campana octubre 2026.

---

### #17 — 2026-05-06 — Claim C GME: "Sin app que instalar. Sin cloud requerida."

- **Claim evaluado (texto exacto):** "Sin app que instalar. Sin cloud requerida."
- **Producto / pieza:** GME — P-03 empaque (si se incluye), P-04 landing, P-06 video WiFi demo
- **Decision:** SUSPENDIDO — condicionado a engineering Q2 (operacion offline) y Q3 (arquitectura MCU proteccion/webserver). Tres escenarios posibles segun respuesta; caveats literales distintos por escenario (ver archivo fuente).
- **Caveat textual (Escenario favorable — Q2 favorable + Q3 favorable):** "Control desde cualquier browser en la misma red WiFi. Sin app. Sin cloud. La proteccion actua independientemente de la conexion a internet."
- **Rationale:** "Sin app que instalar" es plenamente defendible. "Sin cloud requerida" es verdad para la interfaz pero potencialmente falso para la proteccion activa si el GME requiere WiFi para disparar el contactor. Riesgo arquitectonico adicional: si el MCU de proteccion y el webserver comparten el mismo hilo sin watchdog, un cuelgue del webserver puede inhabilitar la proteccion. Este es el riesgo de mayor magnitud identificado en el gate (nota final del archivo fuente).
- **Criterio aplicado:** RISK-POLICY v1.0 §3.
- **Evidencia consultada:** Vera VE-1 §4 Claim C y §5 Q2/Q3; OL-3 §1.5; VA-5 §Claim C; AU-1 §7.1 y §7.2.
- **Scope:** GME — P-03, P-04, P-06. Critico: gate debe resolverse antes del 15 julio 2026 para no comprimir ventana de imprenta del empaque (deadline 1 septiembre).

---

### #18 — 2026-05-06 — Claim H GME: Formulacion de "proteccion del equipo / instalacion / negocio"

- **Claim evaluado (texto exacto):** Varias formulaciones — ver sub-categorias abajo
- **Producto / pieza:** GME — todas las piezas (P-01 a P-10) donde aparezca beneficio de proteccion para el consumidor final
- **Decision (formulacion de garantia de resultado):** RECHAZADO — equivalente a entrada #12 del log (empaque GSM) y BR-5 Precedente #4. Formulaciones prohibidas: "Tu equipo estara protegido", "Garantiza la proteccion del equipo", "Nunca mas te quedas sin equipo", "Protege tu inversion", "Evita que la bomba se dane", "Tu negocio estara protegido", cualquier variante que prometa resultado de proteccion del equipo conectado.
- **Decision (formulacion de accion verificable):** APROBADO CON CAVEAT — texto exacto por canal en archivo fuente §Caveats literales (Caveat H-01). Puede usarse YA sin gate adicional.
- **Caveat textual aprobado (empaque tiro):** "El GME monitorea las condiciones electricas y actua ante sobrecarga, subcarga y variaciones de voltaje — segun el perfil del equipo conectado."
- **Caveat textual aprobado (landing / email):** "El GME detecta las variaciones electricas que danan equipos — y actua antes de que lleguen a la carga. Subcarga, sobrecarga, alto voltaje, bajo voltaje — segun el perfil del equipo que conectas. Refrigeracion, Bombas o Motores: el GME responde segun su modo."
- **Rationale:** Transferencia directa del Precedente #4 al GME. El GME protege ante condiciones electricas especificas; no protege ante transientes de alta energia, fallas de ground, averias mecanicas, instalacion incorrecta. La Ley de Proteccion al Consumidor venezolana interpreta promesas de marketing como compromisos implicitos. La formulacion de accion verificable (describe lo que el GME hace, sin prometer el resultado final sobre el equipo conectado) es la unica defensa juridicamente sostenible.
- **Criterio aplicado:** BR-5 Precedente #4. RISK-POLICY v1.0 §3.
- **Evidencia consultada:** VA-5 §Claim H y §Proteccion de carga; Vera VE-1 §4; BR-2 entrada #12.
- **Scope:** GME — todas las piezas y todos los canales. Vigente como politica permanente para el producto GME, igual que para la linea GSM.

---

### #19 — 2026-05-06 — Claims rechazados GME (grupo)

- **Claims evaluados:** (A) "Visibilidad total del equipo desde tu celular" — (B) "Tan preciso como instrumentacion profesional" — (C) "Multivoltaje 120/220V" (V1) — (D) "Sensibilidad <1 s ante fluctuaciones" — (E) "Historial de las ultimas 20 fallas con fecha y hora" (V1)
- **Producto / pieza:** GME — todas las piezas del lanzamiento octubre 2026
- **Decision:** RECHAZADOS — sin alternativa posible en el estado actual de informacion (excepto (B) y (D) que tienen alternativa cuando engineering declare dato cuantitativo)
- **Rationale (por claim):**
  - "Visibilidad total": superlativo absoluto indefendible — el GME muestra V/I/Hz/estado/ultima falla, no temperatura de descarga, historial cronologico, ni acceso remoto fuera de red.
  - "Tan preciso como instrumentacion profesional": sin clase de exactitud declarada IEC 60255-1, el claim es indefendible ante audiencia tecnica.
  - "Multivoltaje 120/220": SKUs son "220"; Q10 de Vera pendiente; claim no existente hasta confirmacion hardware.
  - "Sensibilidad <1 s": dato de engineering no disponible; y el tecnico de la encuesta (#104359489) lo cuestiona activamente — usar el claim sin dato es sobrepromesa con testigo adverso.
  - "Historial 20 fallas": mockups muestran ultima ocurrencia por tipo sin log cronologico; RTC pendiente; feature no implementada en V1.
- **Criterio aplicado:** RISK-POLICY v1.0 §3. BR-5 Precedente #1 (para sensibilidad y precision: el superlativo con dato cuantitativo es aprobable si el dato de engineering lo confirma — pero no sin el dato).
- **Evidencia consultada:** Vera VE-1 §2 tabla y §4; VA-5 §Claims F, G, J, K, L; comentarios encuesta #104359489, #104362252, #104362438, #104362640.
- **Scope:** GME — todos los canales y piezas. V1 octubre 2026.

---

### #20 — 2026-05-06 — Claim #GME-05: "Multi-aplicacion — un solo hardware, tres modos"

- **Claim evaluado (texto exacto):** "Un solo hardware, tres modos de aplicacion: Refrigeracion, Bombas, Motores" / "Multi-aplicacion: configura para R/B/M con un solo hardware"
- **Producto / pieza:** GME — P-03, P-07, P-08, P-09
- **Decision (formulacion basica sin superlativo):** APROBADO CON CAVEAT — Caveat E-01 (texto exacto en archivo fuente §Caveats). Puede usarse YA.
- **Decision (formulacion con superlativo de exclusion):** SUSPENDIDO — pendiente OL-3 segunda iteracion + decision Owner sobre modalidad SKU.
- **Decision (formulacion "un solo hardware"):** SUSPENDIDO — condicionado a decision Owner sobre 1 hardware configurable vs. 3 SKUs fisicos (deadline 15 junio 2026).
- **Caveat textual aprobado (formulacion basica — empaque):** "Un protector. Tres modos: Refrigeracion, Bombas, Motores. Los parametros de proteccion preajustados segun el equipo que conectas."
- **Rationale:** Los tres modos tienen diferencias reales verificadas en mockups: valores default distintos en todos los parametros de tiempo y umbral, logica de maniobra diaria exclusiva de modo B, y tiempo de deteccion de sobrecarga configurable visible en modo M pero no en R/B (Vera §3.1–3.2). El claim de "un solo hardware" depende de la decision SKU del Owner — si son 3 SKUs fisicos, el claim es factualmente falso.
- **Criterio aplicado:** BR-5 Precedente #2 (superlativo de exclusion requiere ausencia verificada — la segunda iteracion de OL-3 debe confirmar que ningun competidor en $30–60 tiene configuracion multi-aplicacion).
- **Evidencia consultada:** Vera VE-1 §3.1–3.2; OL-3 §Diferenciado; VA-5 §Claim E; AU-1 §7.3.
- **Scope:** GME — campana octubre 2026.

---

### #21 — 2026-05-06 — Claim #GME-08: Pricing claim democratizacion

- **Claim evaluado (texto exacto):** "$35 al precio de un protector basico, con la inteligencia de uno profesional" / variantes de posicionamiento de precio
- **Producto / pieza:** GME — P-03 empaque, P-04 landing, P-09 argumentario de ventas distribuidor
- **Decision:** APROBADO CON CAVEAT
- **Caveat textual aprobado (piezas publicas — empaque, landing):** "Las funciones que antes costaban cientos de dolares — ahora a precio de herramienta profesional."
- **Caveat textual aprobado (argumentario interno distribuidor — P-09 pieza B):** Comparacion directa de precio con Littelfuse 77C (~$552 vs GME $35) con la nota: "La comparacion es de funciones accesibles — el GME no tiene las mismas certificaciones industriales que el 77C."
- **Rationale:** La brecha 15x–23x con el competidor funcional mas cercano (Littelfuse 77C: $552 en distribuidor segun OL-3 §1.1) es el RTB central del Pilar 4. La formulacion de democratizacion no compara con ninguna marca por nombre en materiales publicos (BR-5 Precedente #3), describe funciones verificables, y no afirma certificacion industrial que el GME no tiene.
- **Criterio aplicado:** BR-5 Precedente #3 (comparativos directos prohibidos en empaque y materiales publicos; permitidos en argumentario interno).
- **Evidencia consultada:** OL-3 §1.1; VA-1 §Pilar 4; Informe Van Westendorp (precio $35 dentro del rango aceptable de los tres segmentos).
- **Scope:** GME — campana octubre 2026.

---

---

## Bloque Argumentos de venta tecnicos — Atlas 4 legacy (2026-05-07)

**Referencia:** `03-projects/genteca/_governance/2026-05-07_BR-1_argumentos-venta-atlas-legacy.md` — archivo fuente con analisis detallado, caveats literales, riesgos transversales y precedentes aplicados. Las entradas que siguen son el registro formal de las decisiones autorizadas por el Owner el 2026-05-07.

**Scope del bloque:** Argumentario tecnico Exceline Profesional / linea GST, extraido por Vera del Atlas 4 legacy (marzo 2026). Uso externo: equipos de ventas, distribuidores, material tecnico comercial. Argumento 8 (COVENIN 3445) EXCLUIDO — sigue bloqueado, pendiente verificacion documental.

---

### #22 — 2026-05-07 — Argumento 1: Monitor de red obligatorio Venezuela

- **Claim evaluado (texto exacto):** "El monitor de red y el rele de sobrecarga son complementarios — no sustitutos. El rele actua cuando la corriente de falla ya se establecio; el monitor de red actua antes, al detectar la condicion de red que la causara (falta de fase, desequilibrio, subtension)."
- **Identificador:** `argumento-venta-monitor-red`
- **Producto / pieza:** Argumentario de ventas tecnico Exceline Profesional — uso externo (distribuidores, equipo comercial, material tecnico)
- **Decision:** APROBADO CON CAVEAT (AMARILLO)
- **Caveat textual obligatorio (palabra por palabra):** "El monitor de red y el rele de sobrecarga son complementarios — no sustitutos. El rele actua cuando la corriente de falla ya se establecio; el monitor de red actua antes, al detectar la condicion de red que la causara (falta de fase, desequilibrio, subtension). Los tiempos citados corresponden a especificaciones tecnicas estandar de dispositivos de proteccion. La frecuencia de estas condiciones varia segun la instalacion y la zona de suministro."
- **Condicion de uso:** El caveat es obligatorio en cualquier pieza escrita que use este argumento. En uso oral, la regla transversal aplica: los datos sobre la red venezolana se presentan como condiciones tecnicas observables, no como estadisticas.
- **Rationale:** Fundamento fisico irrefutable (IEC 60947-4-1). Riesgo unico: deslizamiento oral hacia "tres causas principales" como afirmacion estadistica. El caveat previene ese deslizamiento. Autorizado por el Owner 2026-05-07.
- **Clausula RISK-POLICY aplicada:** RISK-POLICY v1.0 §3 — no afirmar datos que puedan ser falsos (aplicado al dato de frecuencia de fallas en red venezolana sin fuente publicable).
- **Precedente BR-5 referenciado:** BR-5 Precedente #3 (comparativos directos prohibidos — el argumento esta libre de referencia a marcas; conforme).
- **Evidencia consultada:** BR-1 fuente §Argumento 1; IEC 60947-4-1.
- **Scope:** Argumentario de ventas tecnico — uso externo Exceline Profesional. Vigente desde 2026-05-07.

---

### #23 — 2026-05-07 — Argumento 2: Rele electronico vs bimetalico

- **Claim evaluado (texto exacto):** Comparativo tecnico: tres limitaciones del rele bimetalico clasico (no deteccion de desequilibrio, ausencia de memoria termica entre ciclos, tiempos de disparo en stall) vs rele electronico. Diferencial de costo del conjunto: 5-15%.
- **Identificador:** `argumento-venta-rele-electronico-vs-bimetalico`
- **Producto / pieza:** Argumentario de ventas tecnico Exceline Profesional — uso externo
- **Decision:** APROBADO CON CAVEAT (AMARILLO)
- **Caveat textual obligatorio (palabra por palabra):** "Las limitaciones descritas (deteccion de desequilibrio, memoria termica, tiempo de disparo en stall) corresponden al diseno estandar del rele bimetalico clasico — verificables en las curvas tiempo-corriente de especificacion del dispositivo. La condicion de desequilibrio de red (en torno al 5%) es una condicion tecnica frecuente en redes con variabilidad de suministro, que el profesional puede verificar con un multimetro en su instalacion. El diferencial de costo del 5-15% es una estimacion de referencia; varia segun el conjunto de maniobra especifico."
- **Condicion de uso:** El diferencial de costo debe presentarse siempre como estimacion de referencia, no como dato de precision. El dato de desequilibrio CORPOELEC se presenta como condicion tecnica observable, no como estadistica publicada.
- **Rationale:** Las tres limitaciones tecnicas del bimetalico son hechos de especificacion verificables. El dato de desequilibrio "frecuente en CORPOELEC" necesita el marco de condicion tecnica observable (no estadistica). El diferencial de costo es aritmeticamente correcto con rangos conservadores. Autorizado por el Owner 2026-05-07.
- **Clausula RISK-POLICY aplicada:** RISK-POLICY v1.0 §3 (dato de campo venezolano sin fuente publicable — reformulado como condicion tecnica).
- **Precedente BR-5 referenciado:** BR-5 Precedente #3 (comparativo tecnologia vs tecnologia — no marca; conforme).
- **Evidencia consultada:** BR-1 fuente §Argumento 2.
- **Scope:** Argumentario de ventas tecnico — uso externo Exceline Profesional. Vigente desde 2026-05-07.

---

### #24 — 2026-05-07 — Argumento 3: Coordinacion Tipo 2

- **Claim evaluado (texto exacto):** Distincion Tipo 1 / Tipo 2 segun IEC 60947-4-1. Beneficio operacional: solo fusibles como recambio ante cortocircuito (vs contactor completo en Tipo 1). Diferencial de costo del conjunto: 15-25% superior para Tipo 2.
- **Identificador:** `argumento-venta-coordinacion-tipo-2`
- **Producto / pieza:** Argumentario de ventas tecnico Exceline Profesional — uso externo (incluyendo fichas tecnicas y especificaciones formales)
- **Decision:** APROBADO SIN RESTRICCIONES (VERDE)
- **Caveat textual obligatorio:** Ninguno. En canales donde la audiencia exija precision (licitaciones, fichas tecnicas formales), presentar el diferencial de costo como "referencia aproximada que varia segun fabricante y diseno del conjunto."
- **Rationale:** Argumento 100% normativo (IEC 60947-4-1). Diferencial de costo es referencia estandar del sector, no afirmacion estadistica. Sin comparativo de marcas. Sin datos de campo no verificables. Listo para uso externo incluyendo fichas tecnicas. Autorizado por el Owner 2026-05-07.
- **Clausula RISK-POLICY aplicada:** Ninguna — argumento libre de riesgos identificados.
- **Precedente BR-5 referenciado:** Ninguno requerido.
- **Evidencia consultada:** BR-1 fuente §Argumento 3; IEC 60947-4-1.
- **Scope:** Argumentario de ventas tecnico y fichas tecnicas formales — uso externo Exceline Profesional. Vigente desde 2026-05-07.

---

### #25 — 2026-05-07 — Argumento 4: PTC para sumergibles

- **Claim evaluado (texto exacto):** Mecanismo PTC para deteccion de marcha en seco en bombas sumergibles: la corriente del motor baja (o se mantiene) sin carga hidraulica — el rele de sobrecarga no detecta la condicion — el PTC mide temperatura real del devanado (150-160 degC) y actua cuando el rele no puede. Costo de reemplazo de motor sumergible significativamente superior al motor superficial equivalente.
- **Identificador:** `argumento-venta-ptc-sumergibles`
- **Producto / pieza:** Argumentario de ventas tecnico Exceline Profesional — uso externo
- **Decision:** APROBADO CON CAVEAT (AMARILLO)
- **Caveat textual obligatorio (palabra por palabra):** "La marcha en seco es uno de los modos de falla mas daninos en bombas sumergibles, porque la corriente del motor — el parametro que el rele de sobrecarga monitorea — no sube cuando falta el agua: la carga hidraulica desaparece y la corriente puede bajar o mantenerse. Solo el termistor PTC en el devanado detecta el calentamiento resultante. Los motores sumergibles tienen costos de reemplazo significativamente superiores a motores superficiales equivalentes por su diseno especial (sellado, construccion); el costo del PTC representa una fraccion pequena del valor del equipo protegido."
- **Condicion de uso:** No usar "3-10x mas costoso" como dato cuantitativo en canales externos sin catalogo de precios citado. No usar "problema mas frecuente" como afirmacion estadistica — reformular como "uno de los modos de falla mas daninos."
- **Rationale:** Mecanismo fisico irrefutable (secuencia corriente/temperatura en marcha en seco). Las dos afirmaciones sin fuente reformuladas en el caveat. Temperatura de disparo PTC (150-160 degC) verificable en especificaciones de componentes estandar. Autorizado por el Owner 2026-05-07.
- **Clausula RISK-POLICY aplicada:** RISK-POLICY v1.0 §3 (dato sin fuente: "problema mas frecuente" y "3-10x" — reformulados en caveat).
- **Precedente BR-5 referenciado:** BR-5 Precedente #3 (sin comparativo de marcas; conforme).
- **Evidencia consultada:** BR-1 fuente §Argumento 4.
- **Scope:** Argumentario de ventas tecnico — uso externo Exceline Profesional. Vigente desde 2026-05-07.

---

### #26 — 2026-05-07 — Argumento 5: Clase 10 para bombas

- **Claim evaluado (texto exacto):** Seleccion de Clase 10 vs Clase 20 para bombas centrifugas segun IEC 60947-4-1 Tabla VIII. Tiempo de arranque bomba centrifuga: 2-5 segundos. Clase 20 (disenada para cargas de alta inercia) genera riesgo de dano en stall con bomba centrifuga. Clase 10 es la seleccion correcta para este tipo de carga.
- **Identificador:** `argumento-venta-clase-10-bombas`
- **Producto / pieza:** Argumentario de ventas tecnico Exceline Profesional — uso externo (incluyendo fichas tecnicas y especificaciones formales)
- **Decision:** APROBADO SIN RESTRICCIONES (VERDE)
- **Caveat textual obligatorio:** Ninguno.
- **Rationale:** Argumento 100% normativo y tecnico. Todos los datos cuantitativos provienen de IEC 60947-4-1 o de la fisica del equipo (tiempo de arranque bomba centrifuga). Sin comparativo de marcas. Sin datos de campo sin respaldo. Listo para uso externo incluyendo fichas tecnicas y especificaciones para licitacion. Autorizado por el Owner 2026-05-07.
- **Clausula RISK-POLICY aplicada:** Ninguna — argumento libre de riesgos identificados.
- **Precedente BR-5 referenciado:** Ninguno requerido.
- **Evidencia consultada:** BR-1 fuente §Argumento 5; IEC 60947-4-1 Tabla VIII.
- **Scope:** Argumentario de ventas tecnico y fichas tecnicas formales — uso externo Exceline Profesional. Vigente desde 2026-05-07.

---

### #27 — 2026-05-07 — Argumento 6: Anti-short cycle en hardware GST-RR / GSC-CR

- **Claim evaluado (texto exacto):** Tiempo minimo de reconexion de 180 segundos restringido por hardware en GST-RR y GSC-CR. Diferenciador verificable contra la ficha tecnica del producto. Referencia a "otros protectores ajustables" (categoria funcional, sin marca nombrada) que permiten configurar el temporizador desde 0 o 5 segundos.
- **Identificador:** `argumento-venta-anti-short-cycle-hardware`
- **Producto / pieza:** Argumentario de ventas tecnico — GST-RR / GSC-CR — uso externo
- **Decision:** APROBADO SIN RESTRICCIONES (VERDE)
- **Caveat textual obligatorio:** Ninguno. Nota operacional: verificar que la ficha tecnica publicada del GST-RR y GSC-CR sea la version vigente antes de uso externo en canal donde la audiencia pueda verificar el dato (distribuidores tecnicos, licitaciones). Confirmar que no hay confusion de nomenclatura con modelos GST-RD / GST-RG (en estado incierto segun DECISIONS.md 2026-05-07 D3) — los modelos RR y CR son distintos pero la verificacion es previa al uso externo.
- **Rationale:** Argumento basado en spec de producto verificable (180 s por hardware). Fundamento fisico correcto (calor por ciclos de arranque sucesivos, verificable con calculo de energia). Sin comparativo de marcas ("otros protectores ajustables" es descripcion de categoria funcional — conforme BR-5 Precedente #3). Autorizado por el Owner 2026-05-07.
- **Clausula RISK-POLICY aplicada:** Ninguna aplicada — argumento libre de riesgos identificados con la nota operacional de verificacion de ficha tecnica.
- **Precedente BR-5 referenciado:** BR-5 Precedente #3 (descripcion de categoria funcional vs comparativo de marca — conforme).
- **Evidencia consultada:** BR-1 fuente §Argumento 6; ficha tecnica GST-RR / GSC-CR (version vigente a confirmar).
- **Scope:** Argumentario de ventas tecnico — uso externo GST-RR / GSC-CR. Vigente desde 2026-05-07.

---

### #28 — 2026-05-07 — Argumento 7: Cable sumergible correctamente dimensionado (reformulado)

- **Claim evaluado (texto exacto — version reformulada Opcion A autorizada):** "En instalaciones donde la tension de suministro puede estar por debajo del nominal (condicion comun en redes con variabilidad), una caida adicional de 10V en el cable puede dejar al motor a 91% de Vn. A esa tension, el par de arranque es 83% del nominal (par proporcional a V^2) y la corriente sube para compensar. Disenar siempre con la caida de tension en cable dentro del 3% del nominal — para 60 metros de profundidad y 5 HP a 220V, eso implica seccion minima de 6 mm^2."
- **Identificador:** `argumento-venta-cable-sumergible-dimensionado`
- **Producto / pieza:** Argumentario de ventas tecnico Exceline Profesional — uso externo
- **Decision:** APROBADO CON CAVEAT (AMARILLO) — Opcion A (reformulacion sin dato CORPOELEC cuantitativo) autorizada por el Owner 2026-05-07.
- **Caveat textual obligatorio (palabra por palabra):** "En instalaciones donde la tension de suministro puede estar por debajo del nominal (condicion comun en redes con variabilidad), una caida adicional de 10V en el cable puede dejar al motor a 91% de Vn. A esa tension, el par de arranque es 83% del nominal (par proporcional a V^2) y la corriente sube para compensar. Disenar siempre con la caida de tension en cable dentro del 3% del nominal — para 60 metros de profundidad y 5 HP a 220V, eso implica seccion minima de 6 mm^2."
- **Restriccion critica:** El dato original "CORPOELEC ya en 210V en muchas zonas" fue ELIMINADO de la formulacion aprobada. El ejemplo numerico del 91% se mantiene como ilustrativo de la fisica (condicion generica de "redes con variabilidad"), NO como estadistica de la red venezolana. Prohibido restituir el dato cuantitativo de CORPOELEC en ninguna pieza externa sin fuente verificable (ver BR-1 Opcion B — requiere accion de Orlan).
- **Rationale:** El argumento fisico (seccion del cable como parametro de diseno del sistema, caida de tension, consecuencias en par y corriente, norma del 3%) es solido y verificable (IEC 60364 y equivalentes, calculo de seccion vs caida estandar). El dato "210V en muchas zonas" fue eliminado por carecer de fuente publicable — reemplazado por "redes con variabilidad" como condicion generica. El ejemplo numerico del 91% se conserva como ilustracion de la fisica, no como afirmacion estadistica. Autorizado por el Owner 2026-05-07.
- **Clausula RISK-POLICY aplicada:** RISK-POLICY v1.0 §3 (dato cuantitativo de campo sin fuente — eliminado; ejemplo numerico reencuadrado como ilustrativo).
- **Precedente BR-5 referenciado:** BR-5 Precedente #3 (sin comparativo de marcas; conforme). Nota: este caso ilustra la regla transversal BR-1 sobre "datos de campo venezolano sin fuente" (candidato a Precedente BR-5 si el Owner decide formalizarlo).
- **Evidencia consultada:** BR-1 fuente §Argumento 7 (Opcion A); IEC 60364; DECISIONS.md 2026-05-07.
- **Scope:** Argumentario de ventas tecnico — uso externo Exceline Profesional. Vigente desde 2026-05-07. Si el Owner opta por Opcion B (evidencia verificable de dato CORPOELEC via Orlan), esta entrada se actualiza a AMARILLO con formulacion mas especifica — requiere nueva entrada en este log.

---

*Bruna — Risk & Claims Governance Lead — Sistema /RAUL/*
*Log iniciado: 2026-05-03. Dominio: Genteca. Primer gate formal del sistema /RAUL/.*
*Ultima actualizacion: 2026-05-07 (entradas #22 a #28 — bloque argumentos de venta tecnicos Atlas 4 legacy; 7 argumentos autorizados por Owner; Argumento 8 COVENIN 3445 excluido, sigue bloqueado).*
*Archivos fuente: bloque GME en `03-projects/genteca/GME Estudios de mercado/_intel/Bruna_gate_GME_2026-05-06.md`; bloque argumentos en `03-projects/genteca/_governance/2026-05-07_BR-1_argumentos-venta-atlas-legacy.md`*
*Appendear nuevas decisiones al final de este archivo. No reemplazar entradas existentes.*
