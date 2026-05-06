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

*Bruna — Risk & Claims Governance Lead — Sistema /RAUL/*
*Log iniciado: 2026-05-03. Dominio: Genteca. Primer gate formal del sistema /RAUL/.*
*Ultima actualizacion: 2026-05-05 (entrada #14).*
*Appendear nuevas decisiones al final de este archivo. No reemplazar entradas existentes.*
