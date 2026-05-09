# Gate de Claims — Empaque GSM-MB / GSM-RB / GSM-RF / GSM-RE (Innovaciones NTC + < 30 ms)
**Documento:** Bruna_gate_empaque_v1 (BR-1 + BR-2 + Retiro NTC + Pendientes cascada)
**Fecha:** 2026-05-03
**Trigger:** Gate VA — Vael entrega VA-5 (Vael_messaging_framework_v1 §10-§12) con claims candidatos categorizados para empaque de la linea Exceline GSM. La cadena de produccion (Solenne SO-1, Atlas mockups, Aurelio AU-1) espera sello explicito de Bruna antes de avanzar.
**Dominio:** Genteca
**Proyecto:** 2026-04_GSM-MB-RB-RF_empaque
**Elaborado por:** Bruna — Risk & Claims Governance Lead
**Emitido para:** Solenne (SO-1), Aurelio (AU-1), Atlas (mockups), Vael (cierre VA-5), Oz (redline arte)

---

## §1 — BR-1: Claim Risk Assessment Note

### Insumos consultados

- WORKSTREAM_v5_innovaciones.md (2026-05-03) — scope, regla de gateo Owner, datos tecnicos confirmados
- Vera_brief_tecnico_v1.md (2026-05-03) — verificacion tecnica NTC y < 30 ms, caveats literales §4
- Orlan_competencia_v1.md (OL-1/2/3/5, 2026-05-03) — landscape competitivo, feasibility de claims
- Vael_messaging_framework_v1.md (VA-1 + VA-5, 2026-05-03) — arquitectura de mensaje y propuesta de guardrails
- delta_v4_NTC-inverter.md (2026-04-30) — propuesta de copy precedente y textos prohibidos
- RISK-POLICY.md v1.0 (2026-04-25) — politica de gobernanza del sistema /RAUL/
- bruna.md (SSOT conceptual) — protocolo de gate, criterios de evaluacion
- BR-5 transversal: sin precedentes existentes a la fecha — este gate es el primero del sistema /RAUL/

### Nota sobre el RISK-POLICY.md vigente

El RISK-POLICY.md v1.0 cubre gobernanza de archivos, acciones de agentes y permisos del sistema. No contiene clausulas especificas de claims de publicidad ni proteccion al consumidor. Esta ausencia es esperada: el sistema /RAUL/ esta en fase inicial. El BR-5 que este gate produce sienta las primeras clausulas de criterio para claims de producto. Las referencias a "criterio aplicado" en este documento son operativas; quedan formalizadas en el BR-5 transversal creado en `04-system/03-governance/BR-5_regla-claims-superlativos-mercados-opacos_2026-05-03.md`.

### Nota sobre el dato de I&D y la condicion bloqueante del Workstream

El WORKSTREAM_v5_innovaciones.md (§Datos tecnicos confirmados, punto 1) establece: "El claim '< 0,03 s' tiene respaldo tecnico documentado. Cierra la condicion bloqueante P-2 de Vera." El Owner confirma la medicion formal de laboratorio. Esta confirmacion del Owner es la evidencia aguas arriba que Bruna necesita para decidir sobre el claim cuantitativo. Bruna no investiga hechos tecnicos; consume la confirmacion del Owner como cierre del pendiente P-2.

La confirmacion es declarativa, no documental aun. El datasheet actualizado de I&D no existe todavia. Bruna aprueba el claim condicionado a que ese datasheet se emita antes o simultaneamente al lanzamiento del empaque. Esta es una condicion de produccion, no de gate conceptual: el gate conceptual se emite hoy con respaldo del Owner.

### Matriz de claims evaluados

| # | Claim (texto evaluado) | Fact que lo sostiene | Dimension riesgo dominante | Nivel riesgo | Recomendacion inicial |
|---|---|---|---|---|---|
| A | "El mas rapido ante parpadeos (< 0,03 s)" | Medicion I&D < 30 ms confirmada por Owner; ningún competidor venezolano publica dato comparable; WellSpec (mas agresivo) publica 200-300 ms | Reputacional + Tecnico | Medio | Aprobar con caveat (condicion documental de produccion) |
| B | "El unico en proteger tecnologia inverter" | Falso: Avtek, Breakermatic, JVTRONIC ya lo comunican (Orlan Seccion 4) | Tecnico + Reputacional | Alto | Rechazar |
| C | "Protege tecnologia Inverter" (sin superlativo) | Respuesta < 30 ms protege electronica inverter ante parpadeos; Vera §2.4 | Reputacional | Medio | Aprobar con caveat |
| D | "Sensor NTC incorporado*" | NTC confirmado por Owner + Canudas; ubicacion junto al rele; mecanismo verificado por Vera §1.1-§1.2 | Tecnico | Bajo | Aprobar con asterisco obligatorio |
| E | "Autoproteccion termica" | Vera §1.3(a): funcion primaria del NTC es autoproteger al protector; prefijo "auto" corrige malentendido del 40% del mercado | Tecnico + Reputacional | Bajo | Aprobar |
| F | "Nuevo. La Proteccion mas completa" (lengueta) | "Nuevo": dos innovaciones reales (NTC + < 30 ms). "Mas completa": depende de tres sub-claims sostenidos por pilares 1-3 | Reputacional | Medio | Aprobar con caveat (condicion arquitectonica) |
| G | "Respaldo del breaker termomagnetico" | Vera §1.3: NTC no reemplaza al termomagnetico, actua como capa adicional | Tecnico | Bajo | Aprobar solo off-empaque |
| H | "Protege al motor" / "Protege a la carga" | Sin fact que sostenga proteccion universal de la carga; el NTC solo protege a la carga cuando demanda corriente cercana al nominal del protector (~20 A) | Tecnico | Alto | Rechazar sin alternativa de empaque |
| I | "Uno de los mas rapidos" | Prohibido por decision Owner 2026-05-03 explicita | Reputacional (Brand) | Alto | Rechazar — prohibicion Owner |

### Notas por claim critico

**Claim A — "El mas rapido ante parpadeos (< 0,03 s)"**

La combinacion superlativo + dato cuantitativo es la formulacion mas solida del set. El dato cuantitativo propio (< 0,03 s medido por laboratorio I&D, confirmado por Owner como cierre P-2) es el RTB primario. El paisaje competitivo (Orlan OL-5 Seccion 1) confirma ausencia de competidor venezolano con dato comparable: WellSpec, el unico que hace claim activo de velocidad, publica 200-300 ms. El riesgo tecnico es que el datasheet actualizado aun no existe; el riesgo reputacional es que WellSpec o un competidor no rastreado tenga un dato no publicado que eventualmente emerja. Ambos riesgos estan dentro del umbral manejable: el Owner ha confirmado que Genteca tiene el laboratorio para defender el dato, y la ausencia de evidencia publica contraria es solida.

**Claim B — "El unico en proteger tecnologia inverter"**

Rechazado con certeza. Tres competidores (Avtek, Breakermatic, JVTRONIC) tienen lineas explicitas para inverter documentadas por Orlan (Seccion 4). El claim es factualmente falso y expone a Genteca a un cuestionamiento trivial de verificar. La alternativa recomendada (Claim C sin superlativo) esta totalmente respaldada y es mas diferenciadora porque vincula el claim a la razon causal de velocidad.

**Claim F — "Nuevo. La Proteccion mas completa" (lengueta)**

La arquitectura de la Alternativa A es exactamente la que hace que este superlativo sea defendible: la lengueta enuncia "mas completa" y el frente la sustenta con tres sub-claims concretos que ningun competidor venezolano puede igualar simultaneamente (< 0,03 s + NTC + inverter). Sin esos tres sub-claims, el superlativo quedaria sin sustento. Con ellos, la afirmacion es un superlativo relativo bien acotado. Bruna aprueba el superlativo absoluto "La proteccion mas completa" porque el contexto de empaque limita implicitamente el campo de comparacion y los tres sub-claims estan aprobados por este gate. Si en produccion alguno de los tres sub-claims fuera eliminado por restricciones de espacio, Bruna requiere revision de la lengueta.

**Claim H — "Protege al motor" / "Protege a la carga"**

Rechazado sin alternativa de empaque. Vera §1.4 es inequivoco: el NTC solo actua como proteccion de sobrecarga cuando la carga demanda corriente cercana al nominal del protector (~20 A). Para cargas pequenas, el NTC protege al protector y al cableado, no a la carga conectada. Afirmar proteccion de "la carga" o "el motor" en el frente del empaque, sin esa distincion, es una sobrepromesa tecnica verificablemente incorrecta que puede generar reclamos legitimos de consumidores.

---

## §2 — BR-2: Decision de Gate por Claim

**Decisiones cerradas a 2026-05-03. Vigentes para SO-1, AU-1, Atlas y redline Oz.**

---

### Claim A — "El mas rapido ante parpadeos (< 0,03 s)"

**Decision: APROBADO CON CAVEAT**

**Texto literal aprobado para Solenne:**
"El mas rapido ante parpadeos (< 0,03 s)"

**Caveat al retiro — texto literal obligatorio (palabra por palabra):**
> El tiempo de desconexion de menos de 30 milisegundos (< 0,03 s) aplica ante parpadeos (fluctuaciones rapidas del voltaje de la red electrica) e inestabilidad de la red. No aplica a la desconexion ante sobre voltaje o bajo voltaje pronunciados, cuyo tiempo de desconexion es de 0,4 a 3 segundos segun la intensidad de la falla. Segun especificacion tecnica del laboratorio I&D Genteca.

**Condicion de produccion (no de gate conceptual):** Este claim puede usarse en el arte del empaque. Antes de que el empaque entre en produccion de imprenta, I&D debe haber emitido el datasheet actualizado con el valor "< 30 ms" documentado como especificacion oficial. Si el datasheet no existe al momento de imprimir, el empaque no puede fabricarse con este claim. Responsable: Owner + I&D Genteca.

**Rationale:** El dato cuantitativo fue confirmado por el Owner como medicion formal de laboratorio (WORKSTREAM_v5 §Datos tecnicos confirmados, punto 1 — "cierra la condicion bloqueante P-2"). El landscape competitivo (Orlan OL-5 Seccion 1) confirma que ningun competidor venezolano publica un dato de desconexion ante parpadeos igual o inferior a 30 ms. WellSpec, el competidor que hace el claim mas agresivo de velocidad en Venezuela, publica 200-300 ms. La formulacion superlativo + dato cuantitativo es la mas defensible: incluso si el superlativo fuera cuestionado, el dato medido de 0,03 s sigue en pie como afirmacion tecnica. La distincion al retiro (solo aplica a parpadeos, no a sobre/subtension) es necesaria para evitar que el consumidor interprete que el protector siempre actua en 30 ms ante cualquier falla.

**Criterio aplicado (BR-5 Precedente #1):** Superlativo con dato cuantitativo verificable en mercado con alta opacidad competitiva — aprobado con caveat documental.

**Evidencia consultada:** Vera_brief_tecnico_v1 §2.2-§2.3; Orlan_competencia_v1 Secciones 1 y 7 (OL-5); WORKSTREAM_v5 §Datos tecnicos confirmados; Vael VA-5 §10 Claim A.

---

### Claim B — "El unico en proteger tecnologia inverter"

**Decision: RECHAZADO**

**Alternativa propuesta:** "Protege tecnologia Inverter" (Claim C, aprobado con caveat — ver abajo).

**Rationale:** El claim "unico" es factualmente falso. Avtek, Breakermatic y JVTRONIC comunican explicitamente "para tecnologia inverter" (Orlan Seccion 4). Usar "unico" en este atributo expone a Genteca a un cuestionamiento inmediato y trivial de verificar, danando la credibilidad general del empaque. El diferenciador real de Genteca no es el claim de inverter per se sino la razon causal tecnica que lo sustenta: la velocidad < 30 ms, que si es unica en el mercado venezolano.

**Criterio aplicado (BR-5 Precedente #2):** Superlativo de exclusion ("unico") sin fact que excluya a todos los competidores — rechazado.

**Evidencia consultada:** Orlan_competencia_v1 Seccion 4; Vael VA-5 §10 Claim B.

---

### Claim C — "Protege tecnologia Inverter" (sin superlativo)

**Decision: APROBADO CON CAVEAT**

**Texto literal aprobado para Solenne:**
"Protege tecnologia Inverter"

**Caveat al retiro — texto literal obligatorio (palabra por palabra):**
> La proteccion ante parpadeos (fluctuaciones rapidas del voltaje de la red) que ofrece este protector es especialmente beneficiosa para equipos con tecnologia inverter, cuya electronica de control es sensible a variaciones rapidas del voltaje. Este protector no reemplaza la proteccion contra transientes de alta energia (descargas atmosfericas, conmutacion inductiva) presente en el equipo inverter de fabrica. Ambas protecciones son complementarias.

**Condicion de uso en empaque:** Este claim debe aparecer en el tiro en proximidad visual al dato "< 0,03 s" — forman un argumento causa-efecto que, separados graficamente, pierde su caracter diferenciador y se degrada a paridad con Avtek y Breakermatic. Si el diseno grafico no puede garantizar esa proximidad en el tiro, el claim de inverter debe moverse al retiro como bullet de caracteristicas. Esta condicion es de diseno: Atlas y Oz deben respetarla.

**Rationale:** El claim per se no es exclusivo (paridad competitiva). Su fuerza diferenciadora proviene del argumento tecnico causal: el tiempo < 30 ms garantiza apertura del circuito antes de dos ciclos de red (Vera §2.4), minimizando la exposicion de la electronica inverter a condiciones de inestabilidad. Ese argumento tecnico cuantificado si es exclusivo de Genteca en el mercado venezolano.

**Criterio aplicado:** Claim de aplicacion con paridad competitiva — aprobado cuando el RTB diferenciador que lo sustenta (dato de velocidad) esta en proximidad conceptual o visual.

**Evidencia consultada:** Vera_brief_tecnico_v1 §2.4; Orlan_competencia_v1 Seccion 4; Vael VA-5 §10 Claim C.

---

### Claim D — "Sensor NTC incorporado*" (con asterisco)

**Decision: APROBADO CON CAVEAT (asterisco obligatorio)**

**Texto literal aprobado para Solenne:**
"Sensor NTC incorporado*"

El asterisco en el tiro es condicion necesaria e irrenunciable. Sin asterisco, el claim no se considera aprobado.

**Texto del asterisco / retiro:** Ver §3 de este documento. Para el bloque condensado de empaque usar §3.3; para retiro completo usar §3.4.

**Rationale:** El NTC existe, su ubicacion junto al rele de potencia es tecnica-mente correcta, y su mecanismo de proteccion termica esta verificado (Vera §1.1-§1.2, Canudas WhatsApp 02-05-2026). El termino "NTC" es tecnicamente honesto y ningun competidor lo usa (Orlan Seccion 3 — territorio en blanco de comunicacion). El riesgo es que sin el asterisco y la nota explicativa, el consumidor infiere proteccion del motor (el 40% del mercado asi lo interpreta en variantes de "proteccion termica", segun estudio previo referenciado en Orlan §6.3). El asterisco deriva al retiro donde la explicacion puede ser completa y precisa.

**Criterio aplicado:** Claim tecnico con termino especializado y riesgo de interpretacion incorrecta — aprobado con caveat de retiro obligatorio que precisa el alcance real de la proteccion.

**Evidencia consultada:** Vera_brief_tecnico_v1 §1.1-§1.4; Orlan_competencia_v1 Seccion 3; Vael VA-5 §10 Claim D; WhatsApp Canudas 02-05-2026.

---

### Claim E — "Autoproteccion termica"

**Decision: APROBADO**

**Texto literal aprobado para Solenne:**
"Autoproteccion termica"

Sin caveat de retiro adicional al que ya aplica al Claim D. Si se usa "Autoproteccion termica" como formulacion alternativa al NTC, aplica el mismo bloque de retiro de §3.

**Nota de uso:** Esta formulacion es mas accesible para el consumidor final residencial (sin tecnicismo NTC) y corrige activamente el malentendido del 40% que interpreta "proteccion termica" como proteccion del motor. El prefijo "auto" es la distincion semantica critica. Puede usarse en Alternativa B o C como reemplazo del badge "Sensor NTC incorporado*", con el mismo bloque de retiro adaptado.

**Rationale:** "Autoproteccion" describe con precision la funcion primaria del NTC: el protector se protege a si mismo (Vera §1.3(a)). Es tecnicamente honesto, diferenciado (ningun competidor usa esta formulacion — Orlan Seccion 3), y reduce el riesgo de interpretacion incorrecta.

**Evidencia consultada:** Vera_brief_tecnico_v1 §1.3(a); Orlan §6.3 (insight 40% mercado).

---

### Claim F — "Nuevo. La Proteccion mas completa" (lengueta tiro)

**Decision: APROBADO CON CAVEAT**

**Texto literal aprobado para Solenne (Opcion C de Vael — superlativo absoluto):**
"Nuevo. La Proteccion mas completa"

**Caveat arquitectonico obligatorio (condicion de diseno, no texto al retiro):**
Este superlativo esta aprobado exclusivamente bajo la condicion de que los tres sub-claims que lo sustentan (Claim A, Claim C y Claim D) esten visibles en el tiro del mismo empaque. Si por restricciones de espacio alguno de los tres sub-claims es eliminado del tiro, la lengueta debe ajustarse a "Nuevo. Una proteccion mas completa" (superlativo relativo). Solenne debe documentar esta condicion en su SO-1 para que Aurelio y Oz la conozcan.

**Rationale:** El superlativo "La proteccion mas completa" se sustenta en la acumulacion de tres capas de proteccion diferenciadas que ningun competidor venezolano ofrece simultaneamente y de forma documentada: (a) tiempo de respuesta ante parpadeos mas rapido del mercado, (b) proteccion para tecnologia inverter con argumento tecnico causal, (c) autoproteccion termica NTC inexistente en la competencia. Cuando esas tres capas estan presentes en el frente del empaque, "mas completa" no es una afirmacion vacia sino un resumen logico. "La" en lugar de "Una" se aprueba porque dentro del campo de comparacion — mercado venezolano de protectores enchufables residenciales — ningun competidor tiene los tres atributos comunicados simultaneamente.

**Criterio aplicado:** Superlativo cualitativo aprobado cuando esta sustentado en el mismo empaque por sub-claims verificables que ningun competidor iguala simultaneamente.

**Evidencia consultada:** Vera_brief_tecnico_v1 §3.1; Orlan_competencia_v1 Secciones 1, 3, 4; Vael VA-5 §10 Claim F (Opcion C).

---

### Claim G — "Respaldo del breaker termomagnetico"

**Decision: APROBADO SOLO OFF-EMPAQUE**

**Texto literal aprobado para off-empaque (QR / argumentario de ventas / sustento de Junta):**
"El Sensor NTC actua como una capa adicional de proteccion termica que respalda al interruptor termomagnetico de la instalacion. No reemplaza al breaker ni a ninguna proteccion de sobrecorriente del circuito. La correcta seleccion y calibracion del breaker termomagnetico por parte del instalador sigue siendo indispensable."

**Prohibido en empaque (tiro ni retiro).** Confirma la decision de Vera y del Owner.

**Rationale:** La formulacion es tecnicamente correcta y es un argumento valioso para el instalador tecnico. Sin embargo, en el empaque introduce al breaker termomagnetico como actor externo que el consumidor residencial no comprende en ese contexto, complejiza el mensaje y puede generar la pregunta contraria ("entonces el NTC no es suficiente?"). El QR y el argumentario de ventas son el canal correcto.

**Evidencia consultada:** Vera_brief_tecnico_v1 §4 Caveat 1; Vael VA-5 §10 Claim G; WORKSTREAM_v5 §Encuadre tecnico NTC.

---

### Claim H — "Protege al motor" / "Protege a la carga"

**Decision: RECHAZADO — sin alternativa en empaque**

**Rationale:** Vera §1.4 es inequivoco: el NTC solo actua como proteccion de sobrecarga de la carga cuando la corriente de la carga se aproxima al nominal del protector (~20 A para modelos NEMA). Para cargas pequenas, el NTC protege al protector y al cableado, pero no actua como proteccion de sobrecarga de la carga. La sobrepromesa tecnica es verificable y puede generar reclamos legitimos de consumidores cuya carga pequena resulta danada. No existe formulacion alternativa honesta que afirme proteccion universal de la carga en el empaque. Los caveats necesarios son demasiado complejos para el espacio de empaque y, de incluirse, invalidarian el claim. Prohibicion sin excepciones, ratifica delta v4 §4.

**Criterio aplicado:** Sobrepromesa tecnica verificablemente incorrecta para el universo completo de casos de uso — rechazado sin alternativa.

**Evidencia consultada:** Vera_brief_tecnico_v1 §1.4; Vael VA-5 §10 Claims H; delta_v4 §4.

---

### Claim I — "Uno de los mas rapidos"

**Decision: RECHAZADO**

**Alternativa propuesta:** "El mas rapido ante parpadeos (< 0,03 s)" (Claim A, aprobado con caveat).

**Rationale:** Prohibicion explicita del Owner 2026-05-03 (WORKSTREAM_v5 §Regla de gateo). El Owner establece que esta formulacion comunica mediocridad en lugar de liderazgo. Ademas, el paisaje competitivo respalda el superlativo absoluto: la evidencia de Orlan confirma que ningun competidor publica dato comparable, por lo que la formulacion debil no solo esta prohibida sino que tambien es innecesaria.

**Criterio aplicado (BR-5 Precedente #1):** Prohibicion Owner sobre claims de posicionamiento que contradigan estrategia de liderazgo cuando el dato cuantitativo propio es el mas alto conocido en el mercado.

**Evidencia consultada:** WORKSTREAM_v5 §Regla de gateo; Orlan_competencia_v1 Seccion 2.

---

### Claims adicionales detectados en el review

Durante la revision del VA-5 y del WORKSTREAM, Bruna identifica los siguientes claims candidatos adicionales:

**Claim J — "El mas rapido de la categoria" (formulacion Alternativa C de Vael)**

**Decision: APROBADO CON CAVEAT** — mismo criterio y mismo texto de caveat al retiro que Claim A. La formulacion "de la categoria" (protectores enchufables residenciales monofasicos) es equivalente a "ante parpadeos" en terminos de campo de comparacion y tiene el mismo RTB. Si Aurelio presenta la Alternativa C a la Junta, este claim tiene sello de Bruna bajo las mismas condiciones del Claim A.

---

**Claim K — "Actua en < 0,03 s antes de que la fluctuacion llegue a tu equipo" (frase dominante Alternativa C)**

**Decision: APROBADO CON CAVEAT** — La frase describe el mecanismo sin sobrepromesa de resultado: no afirma que el equipo siempre quede protegido, afirma que el protector actua en ese tiempo ante la fluctuacion. El caveat al retiro del Claim A aplica igualmente (acotacion a parpadeos, no sobre/subtension).

---

**Claim L — "Garantiza la proteccion del equipo" o "evita danos" (posible aparicion en copy Solenne)**

**Decision: RECHAZADO preventivo** — Formulacion de garantia de resultado. Genera obligaciones legales bajo la Ley de Proteccion al Consumidor y al Usuario venezolana (Arts. relativos a garantias implicitas y responsabilidad por producto). No existe RTB tecnico que sostenga proteccion universal del equipo. Ver BR-5 Precedente #4. Solenne no debe usar ninguna formulacion de resultado garantizado.

---

**Claim M — Claims de certificacion IEC / COVENIN (posible aparicion en copy)**

**Decision: GATE BLOQUEADO — pendiente confirmacion Owner** — El GSM-RE datasheet menciona IEC 1000-4-x y COVENIN. Orlan §8 (Expuesto) senala que las certificaciones no estan completamente verificadas para los modelos GSM-MB/RB/RF/RE especificamente. Bruna no puede gatear un claim de certificacion sin verificacion de que la certificacion existe, esta vigente y aplica a los modelos especificos del empaque. Si Solenne o Oz quieren incluir mencion de certificacion, el Owner debe confirmar primero que normas estan certificadas y con que numero de certificado.

---

## §3 — Texto definitivo de retiro / asterisco NTC

**Este bloque esta listo para que Oz lo aplique al arte del empaque.**

### §3.1 Que es el Sensor NTC

NTC (Negative Temperature Coefficient — Coeficiente de Temperatura Negativo) es un sensor de temperatura electronico cuya resistencia electrica disminuye cuando su temperatura aumenta. Esa variacion de resistencia es detectada por el circuito de control del protector, que ordena la desconexion cuando la temperatura supera el umbral de diseno.

### §3.2 Donde esta ubicado

El Sensor NTC esta instalado junto al rele de potencia dentro del protector — el componente que maneja directamente la corriente de la carga conectada y que, por tanto, es el que mas calor genera cuando circulan corrientes excesivas.

### §3.3 Bloque condensado para empaque (nota al pie del asterisco — texto definitivo)

> **Sensor NTC:** sensor de temperatura ubicado junto al rele de potencia. Detecta calentamiento excesivo (a partir de 60 degC internos) causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos), y desconecta la carga para proteger al protector mismo y al cableado de la instalacion. Para cargas de baja demanda de corriente, el sensor NTC protege al protector y al cableado, pero no actua como proteccion de sobrecarga directa de la carga conectada. Funciona como capa adicional de proteccion termica; no reemplaza al interruptor termomagnetico de la instalacion.

### §3.4 Bloque completo de retiro (para QR y argumentario — usar en retiro si el espacio lo permite)

> **Sensor NTC incorporado — que es, como actua y que protege**
>
> El Sensor NTC es un sensor de temperatura incorporado junto al rele de potencia del protector. Cuando la temperatura interna supera los 60 degC — por sobrecorriente, rotor trabado, bornes flojos o cualquier condicion que genere calor excesivo — el NTC actua sobre el circuito de control y ordena la apertura del rele, desconectando la carga.
>
> **Que protege:**
> - Al protector mismo: evita que el rele de potencia se destruya por sobrecalentamiento.
> - Al cableado de la instalacion: corta la corriente antes de que un sobrecalentamiento prolongado dane los conductores.
> - Al circuito en caso de conexiones deficientes: el calor generado por bornes flojos o falsos contactos puede activar la proteccion por conveccion.
>
> **Que no protege directamente:**
> La carga conectada (motor, compresor, electronica) no queda protegida termicamente de forma directa en todos los casos. El NTC actua cuando la corriente de la carga se aproxima al limite nominal del protector. Para equipos de baja demanda de corriente, el sensor protege al protector y al cableado, pero no actua como proteccion de sobrecarga de la carga misma.
>
> **Temperatura de disparo:**
> El umbral de disparo es de 60 degC internos. La temperatura maxima de operacion ambiental del protector es 55 degC; el margen entre temperatura ambiente maxima y temperatura de disparo garantiza que el sensor no actue en condiciones normales de operacion.
>
> **Relacion con el interruptor termomagnetico:**
> El Sensor NTC actua como una capa adicional de proteccion termica que respalda al interruptor termomagnetico de la instalacion. No lo reemplaza. El breaker termomagnetico sigue siendo la proteccion primaria del circuito. La correcta seleccion y calibracion del breaker por parte del instalador es indispensable e independiente de este sensor.
>
> **Nota sobre cargas pequenas:**
> Para equipos de baja demanda de corriente, el sensor NTC protege al protector y a la instalacion, pero no actua como proteccion de sobrecarga de ese equipo conectado. Esta es una caracteristica de diseno: el protector de voltaje no mide corriente de la carga ni esta disenado como sustituto de un termico electromecanico.

---

## §4 — Regla de Gateo Owner: Formalizacion como Precedente BR-5

La decision Owner 2026-05-03 sobre claims superlativos queda formalizada en:

`C:\RAUL\04-system\03-governance\BR-5_regla-claims-superlativos-mercados-opacos_2026-05-03.md`

Ese archivo contiene:
- Precedente #1: Superlativo con dato cuantitativo en mercado con alta opacidad competitiva — criterio, condiciones, riesgos asumidos y condiciones de revision.
- Precedente #2: Superlativo de exclusion ("unico") — rechazado sin evidencia de ausencia universal del atributo en competidores.
- Precedente #3: Comparativos directos de marca — prohibidos en empaque, permitidos en argumentario interno.
- Precedente #4: Garantia de resultado de proteccion del equipo — rechazado sin RTB especifico y revision legal.

---

## §5 — Pendientes para agentes aguas abajo

### Vael

No requiere refresh urgente del VA-5. Dos actualizaciones de estado para cierre del VA-5:
- Claim B ("El unico en proteger inverter"): actualizar a estado rechazado confirmado.
- Claim J ("El mas rapido de la categoria" de la Alternativa C): marcar como aprobado con caveat (mismo que Claim A).
- Flag de revision: si la investigacion Paxs sobre el OEM de TQ arroja un dato de velocidad < 30 ms, requiere refresh urgente de VA-5 Claim A.

### Solenne (SO-1)

**Claims aprobados para usar en tiro:**
- "El mas rapido ante parpadeos (< 0,03 s)" — con caveat de retiro de §2 Claim A
- "Protege tecnologia Inverter" — condicionado a proximidad visual con el dato de velocidad; caveat de retiro de §2 Claim C
- "Sensor NTC incorporado*" — con asterisco en tiro y bloque de retiro de §3.3 (condensado) o §3.4 (completo)
- "Autoproteccion termica" — como alternativa al badge NTC en Alternativa B o C
- "Nuevo. La Proteccion mas completa" — en lengueta, condicionado a que los tres sub-claims esten visibles en el mismo tiro

**Claims prohibidos — ninguna formulacion con estas ideas puede aparecer en el empaque:**
- "El unico en proteger tecnologia inverter" — rechazado, factualmente falso
- "Protege al motor" / "Protege a la carga" — rechazado, sobrepromesa tecnica
- "Uno de los mas rapidos" — rechazado, prohibicion Owner
- "Garantiza la proteccion del equipo" / "evita danos" — rechazado, garantia de resultado sin RTB
- Cualquier nombre de marca competidora en empaque

**Condicion de produccion a documentar en SO-1:**
El Claim A tiene una condicion de produccion: el datasheet actualizado de I&D con el valor < 30 ms debe existir antes de imprimir el empaque. Solenne registra esta condicion en SO-1 para que Aurelio la lleve a la Junta como pendiente operativo.

**Claim M (certificaciones IEC/COVENIN):** bloqueado hasta confirmacion del Owner — no usar sin ese paso previo.

### Aurelio (AU-1)

Las tensiones estrategicas que Vael identifico en VA-1 §6 siguen vigentes. Aurelio agrega esta tension de Bruna:

- **Condicion de produccion del Claim A:** el empaque no puede imprimirse con el claim "< 0,03 s" hasta que I&D emita el datasheet actualizado. La decision de copy es suficiente para la Junta; pero hay un pendiente operativo de I&D con plazo critico antes de produccion de arte final. Aurelio articula esto como riesgo de calendario en AU-1, no como riesgo de claim.
- **La Alternativa C de Vael tiene sello de Bruna** — Aurelio puede presentarla a la Junta con igual solidez de claims que A y B.
- Para consumo interno de la Junta: el unico competidor que hace claim activo de velocidad en Venezuela (WellSpec) publica 200-300 ms. Genteca tiene respaldo de laboratorio para el superlativo.

### Atlas (mockups)

**Claims que pueden ir en el tiro:**
- "El mas rapido ante parpadeos (< 0,03 s)" — tiro, jerarquia visual alta
- "Protege tecnologia Inverter" — tiro, en proximidad visual al dato de velocidad (condicion de diseno no negociable — ver Claim C)
- "Sensor NTC incorporado*" — tiro con asterisco legible
- "Autoproteccion termica" — alternativa al badge NTC en Alt. B o C
- "Nuevo. La Proteccion mas completa" — lengueta

**Solo en retiro o asterisco:**
- Bloque nota NTC (§3.3 condensado o §3.4 completo)
- Caveat tiempo < 30 ms acotado a parpadeos (texto de §2 Claim A)
- Caveat inverter complementario al transiente de fabrica (texto de §2 Claim C)
- Respaldo del termomagnetico (texto de §2 Claim G)

**Condicion de diseno inamovible:**
La conexion visual causa-efecto entre "< 0,03 s" y "Protege tecnologia Inverter" es una condicion de aprobacion de Bruna sobre el Claim C. Si el diseno los separa graficamente de forma que no se lean como causa-efecto, el Claim C debe moverse al retiro. Atlas confirma a Solenne y a Aurelio que esa conexion esta garantizada en el arte antes de que SO-1 se cierre.

### Oz (redline final)

**Bloque de asterisco NTC para implementar en el retiro:**
Usar el texto de §3.3 (condensado) como texto minimo obligatorio. Si el espacio del retiro lo permite, §3.4 (completo) aporta mas precision tecnica valiosa.

**Caveat de tiempo < 30 ms (texto para retiro):**
> El tiempo de desconexion de menos de 30 milisegundos (< 0,03 s) aplica ante parpadeos (fluctuaciones rapidas del voltaje de la red electrica) e inestabilidad de la red. No aplica a la desconexion ante sobre voltaje o bajo voltaje pronunciados, cuyo tiempo de desconexion es de 0,4 a 3 segundos segun la intensidad de la falla. Segun especificacion tecnica del laboratorio I&D Genteca.

**Caveat de inverter (texto para retiro):**
> La proteccion ante parpadeos que ofrece este protector es especialmente beneficiosa para equipos con tecnologia inverter, cuya electronica de control es sensible a variaciones rapidas del voltaje. Este protector no reemplaza la proteccion contra transientes de alta energia presente en el equipo inverter de fabrica. Ambas protecciones son complementarias.

Oz implementa estos tres bloques de retiro (NTC + tiempo < 30 ms + inverter) en el redline. Si el espacio no permite los tres por separado, el §3.4 completo los integra.

---

## §6 — Cover Note

### Que valide

- Los nueve claims del brief original (A a I) mas cuatro claims adicionales detectados en el review (J, K, L, M).
- Evidencia tecnica aguas arriba de Vera, Orlan y del Owner (datos confirmados en WORKSTREAM_v5).
- Landscape competitivo (Orlan OL-5) para los claims superlativos.
- Ausencia de precedentes BR-5 previos (primer gate formal de Bruna en el sistema /RAUL/).
- El RISK-POLICY.md v1.0 vigente no contiene clausulas de claims de publicidad — Bruna aplica criterio propio documentado en BR-5 transversal.

### Tabla resumen de decisiones

| # | Claim | Decision |
|---|---|---|
| A | "El mas rapido ante parpadeos (< 0,03 s)" | APROBADO CON CAVEAT |
| B | "El unico en proteger tecnologia inverter" | RECHAZADO |
| C | "Protege tecnologia Inverter" | APROBADO CON CAVEAT |
| D | "Sensor NTC incorporado*" | APROBADO CON CAVEAT (asterisco obligatorio) |
| E | "Autoproteccion termica" | APROBADO |
| F | "Nuevo. La Proteccion mas completa" | APROBADO CON CAVEAT (tres sub-claims en tiro) |
| G | "Respaldo del breaker termomagnetico" | APROBADO SOLO OFF-EMPAQUE |
| H | "Protege al motor" / "Protege a la carga" | RECHAZADO sin alternativa de empaque |
| I | "Uno de los mas rapidos" | RECHAZADO |
| J | "El mas rapido de la categoria" (Alt. C) | APROBADO CON CAVEAT (igual que A) |
| K | "Actua en < 0,03 s antes de que la fluctuacion llegue a tu equipo" | APROBADO CON CAVEAT (igual que A) |
| L | "Garantiza la proteccion del equipo" / "evita danos" | RECHAZADO preventivo |
| M | Claims de certificacion IEC/COVENIN | BLOQUEADO — pendiente confirmacion Owner |

### Que deje pendiente

1. **Condicion de produccion Claim A:** I&D debe emitir datasheet actualizado con < 30 ms documentado antes de imprimir. Responsable: Owner + I&D Genteca. No bloquea el gate conceptual ni SO-1 ni AU-1.
2. **Claim M — Certificaciones:** Owner debe confirmar que normas estan certificadas y con que numero para los modelos GSM-MB/RB/RF/RE.
3. **Paxs background — OEM de TQ:** si resulta publicar dato de velocidad < 30 ms, invalida el superlativo y requiere refresh urgente. No bloquea este gate.
4. **Datasheets de GSM-MB y GSM-RF (Vera Pendiente P-1):** si los nominales de corriente difieren de los modelos RE, los caveats del retiro deben ajustarse por modelo antes de imprimir.
5. **Archivos .docx de market research (Orlan §6.1):** no pudieron procesarse como .docx; ya estan disponibles como .pdf en el brief. Si contienen hallazgos que contradicen las decisiones de este gate, el gate debe revisarse. Raul debe confirmar si los PDFs existentes en `00-brief/market-research/` son suficientes o si los .docx contienen informacion diferente.

### Clausulas de riesgo citadas

- Superlativo con dato cuantitativo verificable en mercado con alta opacidad competitiva — BR-5 Precedente #1 (Claims A, J, K)
- Superlativo de exclusion sin evidencia de ausencia universal — BR-5 Precedente #2 (Claim B)
- Claim de aplicacion con paridad competitiva — aprobado con proximidad al RTB diferenciador (Claim C)
- Claim tecnico con riesgo de interpretacion incorrecta — aprobado con caveat de retiro obligatorio (Claim D)
- Superlativo cualitativo sustentado en sub-claims verificables en el mismo empaque — aprobado con condicion arquitectonica (Claim F)
- Sobrepromesa tecnica verificablemente incorrecta — rechazado sin alternativa (Claim H)
- Garantia de resultado sin RTB — rechazado preventivo, BR-5 Precedente #4 (Claim L)
- Prohibicion Owner sobre formulacion de posicionamiento debil — ratificado (Claim I)

### A quien notifico en cascada

- **Vael:** recibe este documento como cierre del gate VA. Puede actualizar VA-5 con clasificaciones finales y notificar a Solenne y Aurelio.
- **Solenne:** recibe lista de claims aprobados/rechazados/caveats para SO-1.
- **Aurelio:** recibe tensiones estrategicas adicionales + condicion de produccion de I&D para AU-1.
- **Atlas:** recibe condicion de diseno sobre proximidad visual < 0,03 s y "Protege tecnologia Inverter".
- **Oz:** recibe bloque de retiro NTC definitivo (§3.3 y §3.4) y caveats de velocidad e inverter.
- **Owner:** recibe flag de Claim M (certificaciones pendientes) y condicion de produccion de I&D (datasheet < 30 ms antes de imprimir).

---

## §6 — Refresh BR-2 sobre lengüeta B-3 (2026-05-03)

**Trigger:** Gate SO — Solenne plantea Duda abierta 1 en SO-1: la condicion de Bruna §2 Claim F exige los tres sub-claims "visibles en el tiro"; en B-3 dos estan en el tiro y el tercero (inverter) esta en el retiro como bullet de caracteristicas. Solicita confirmacion antes de imprimir.

**Claim evaluado:** "Nuevo. La Proteccion mas completa" (lengueta — Alternativa B-3)

---

### Decision: OPCION 3 — Tercera via

**Lengüeta aprobada para B-3 (texto literal identico a A):**
"Nuevo. La Proteccion mas completa"

**No se degrada a "Una proteccion mas completa". No se rechaza.**

La condicion de §2 Claim F se reformula para B-3 de la siguiente manera: el superlativo "La Proteccion mas completa" es defendible en B-3 si y solo si se cumplen las dos condiciones siguientes de diseno que reemplazan a la condicion original de "tres sub-claims en el tiro":

**Condicion B-3-1 (tiro):** Los dos sub-claims del tiro deben ser los dos diferenciadores sin equivalente publicado en el mercado venezolano: dato de velocidad (< 0,03 s) y Sensor NTC. Esta condicion ya se cumple en el diseno de B-3 segun SO-1.

**Condicion B-3-2 (retiro — nueva):** El bullet de "Protege tecnologia Inverter" en el retiro debe introducirse con el argumento causal que lo hace diferenciador — es decir, no puede aparecer como afirmacion desnuda sino vinculado a la velocidad. El texto del bullet en el retiro de B-3 ya lo hace correctamente segun SO-1: "Protege tecnologia Inverter: la velocidad de respuesta de < 0,03 s minimiza la exposicion de la electronica de control inverter a condiciones de inestabilidad de red." Este texto se aprueba como obligatorio. Si en la implementacion del arte ese bullet se simplifica a "Protege tecnologia Inverter" sin el argumento causal, el claim de inverter pierde su funcion diferenciadora y el superlativo de la lengueta queda con solo dos pilares sustentadores en el empaque — lo cual lo convierte en un superlativo mas debil pero aun defendible. En ese caso (solo si Oz simplifica el bullet), la lengueta deberia degradarse a "Una proteccion mas completa".

**Condicion B-3-3 (elemento de vinculacion tiro-retiro — nueva):** Atlas debe incluir un elemento visual en el tiro de B-3 que invite al comprador a voltear el empaque. Puede ser el dato cuantitativo "< 0,03 s" con un indicador grafico de continuacion, o una linea de texto mini bajo la Frase 2 que diga algo como "Incluye proteccion inverter — ver detalle al reverso". Si no se puede garantizar ese vinculo grafico, la alternativa es aceptar que "La Proteccion mas completa" se entienda a partir de los dos claims del tiro, lo cual es suficiente pero no optimo.

---

### Razonamiento

La condicion original de §2 Claim F ("tres sub-claims visibles en el tiro") fue escrita asumiendo la arquitectura A, donde los tres estaban en el tiro. Esa condicion era instrumentalmente correcta para A: sin los tres sub-claims en el tiro, el superlativo cualitativo quedaba sin sustento inmediato para el comprador. El error de redaccion de la condicion original fue fijar el canal (el tiro) en lugar de fijar el requisito subyacente: que el comprador pueda verificar en el mismo empaque los tres pilares que justifican el superlativo.

La pregunta correcta no es "estan los tres en el tiro" sino "puede el comprador verificar los tres en el empaque". La respuesta para B-3 es si: el empaque es un artefacto que se sostiene en la mano, el retiro es parte del mismo empaque, y el instalador tecnico — audiencia primaria — si lee el retiro. En el punto de venta de ferreteria, el comprador tiene el blister en la mano antes de comprarlo, no lo ve solo de frente.

El argumento reputacional para el superlativo cualitativo "mas completa" en B-3 es mas debil que en A porque el tercer pilar no esta visible de inmediato, pero sigue siendo defendible: dos pilares sin equivalente en el mercado venezolano (velocidad + NTC) mas un tercero en el retiro con argumento causal completo es una base suficiente para "proteccion mas completa" como superlativo cualitativo, especialmente considerando que ningun competidor venezolano ofrece los tres atributos simultaneamente (Orlan Secciones 1, 3, 4).

La degradacion a "Una proteccion mas completa" seria innecesariamente costosa comunicacionalmente para un riesgo que se gestiona con la condicion de texto del bullet en el retiro. Si ese bullet incluye el argumento causal (ya lo hace en SO-1), el superlativo absoluto esta justificado.

---

### Clausula RISK-POLICY aplicada

RISK-POLICY.md v1.0 no contiene clausula especifica de claims de publicidad. Se aplica criterio propio documentado en BR-5 transversal. El criterio relevante es el del §2 Claim F original: "Superlativo cualitativo aprobado cuando esta sustentado en el mismo empaque por sub-claims verificables que ningun competidor iguala simultaneamente." La condicion "en el mismo empaque" era la correcta desde el origen; fue mal redactada como "en el tiro" por asumir la arquitectura A. Este refresh corrige esa redaccion.

---

### Precedente BR-5

No existe en BR-5 transversal un precedente especifico sobre distribucion de sub-claims entre tiro y retiro para superlativos cualitativos. Este caso sienta precedente nuevo que debe apendarse a BR-5. Ver seccion de notificacion abajo.

---

### Notificacion en cascada

**Solenne (SO-1):**

La interpretacion de Solenne es correcta en lo esencial pero con la condicion adicional de diseno B-3-2: el bullet de inverter en el retiro de B-3 debe incluir el argumento causal completo tal como esta en SO-1. Si Oz simplifica ese bullet al texto corto "Protege tecnologia Inverter" sin el argumento causal, Solenne debe notificar a Bruna antes de imprimir porque en ese caso la lengueta B-3 requeriria degradarse. Solenne registra esta condicion en el cierre de SO-1 (no requiere emitir SO-1 v2 — es una nota de produccion al pie del documento o en el delta que preceda a AU-1).

**Aurelio (AU-1):**

La Alternativa B-3 tiene sello de Bruna para la lengueta "La Proteccion mas completa" bajo las condiciones B-3-1 (ya cumplida), B-3-2 (bullet inverter con argumento causal en retiro — ya cumplida en SO-1) y B-3-3 (elemento de vinculacion tiro-retiro para Atlas — pendiente de decision de diseno). Aurelio puede presentar B-3 a la Junta con sello de Bruna limpio. En AU-1 documentar que B-3 tiene una condicion de diseno menor pendiente de Atlas (B-3-3) que no bloquea la presentacion ni la decision de Junta, pero que debe resolverse antes de imprimir.

**Atlas:**

La condicion B-3-3 es una solicitud editorial de Bruna para B-3: incluir un elemento grafico en el tiro que vincule al comprador con el retiro para que encuentre el tercer sub-claim (inverter). Puede ser minimo — un indicador de "ver reverso" o un elemento de color que conecte con el bullet de inverter en el retiro. Si Atlas considera que ese elemento distrae del dato dominante "< 0,03 s", puede omitirlo bajo su criterio de diseno. En ese caso la lengueta sigue aprobada pero la fuerza del superlativo descansa en los dos claims del tiro.

---

### Precedente nuevo para BR-5

Este caso genera un precedente nuevo de tipo "superlativo cualitativo con sub-claims distribuidos entre tiro y retiro". Debe apendarse al BR-5 transversal en `04-system/03-governance/BR-5_regla-claims-superlativos-mercados-opacos_2026-05-03.md` bajo la seccion "Afirmaciones absolutas". Raul o Celeste deciden el momento de ese append — no bloquea el gate de B-3.

**Criterio a sentar:** Un superlativo cualitativo que fue aprobado en un contexto de tres sub-claims en el tiro puede sostenerse en una arquitectura de dos sub-claims en el tiro mas uno en el retiro cuando: (a) los dos sub-claims en el tiro son los de mayor diferenciacion sin equivalente publicado en el mercado, (b) el sub-claim en el retiro aparece con su argumento causal completo que lo hace diferenciador (no como afirmacion desnuda), y (c) el comprador puede acceder a los tres sub-claims en el mismo objeto fisico.

---

## References

| Documento | Referencia especifica | Uso en este gate |
|---|---|---|
| WORKSTREAM_v5_innovaciones.md | §Regla de gateo, §Datos tecnicos confirmados, §Decisiones cerradas | Datos tecnicos, regla superlativo Owner, confirmacion P-2 |
| Vera_brief_tecnico_v1.md | §1.1-§1.4 (NTC), §2.2-§2.4 (< 30 ms), §4 (caveats), §5 (pendientes) | Facts tecnicos, caveats literales, condiciones de gate |
| Orlan_competencia_v1.md | Secciones 1, 2, 3, 4, 7 (OL-5) | Landscape competitivo, feasibility claims superlativos |
| Vael_messaging_framework_v1.md | VA-1 §1-§6, VA-5 §10-§12 | Arquitectura de mensaje, propuesta de categorizacion de claims |
| delta_v4_NTC-inverter.md | §4 (textos prohibidos) | Historial de decisiones previas y textos prohibidos |
| RISK-POLICY.md v1.0 (2026-04-25) | Sin clausula especifica de claims — ver nota §1 | Gobernanza general del sistema |
| bruna.md (SSOT) | §6.1-§6.5 (protocolo de operacion), §7.2-§7.3 (formatos BR) | Protocolo de gate aplicado |
| BR-5 transversal — `04-system/03-governance/BR-5_regla-claims-superlativos-mercados-opacos_2026-05-03.md` | Precedentes #1 a #4 | Precedentes sentados por este gate |
| WhatsApp Canudas 02-05-2026 | Descripcion tecnica NTC, confirmacion < 30 ms | RTB de Pilares NTC y velocidad |

---

*Bruna — Risk & Claims Governance Lead — Sistema /RAUL/*
*Gate emitido: 2026-05-03*
*Estado: CERRADO — Claims gateados listos para SO-1, AU-1, Atlas y redline Oz*
*Proxima revision requerida: si I&D modifica dato de < 30 ms, si competidor publica dato comparable, o si Paxs desvela dato OEM de TQ < 30 ms.*

---

## §7 — Refresh 2026-05-04 (post-Liliam I&D + Canudas 2 + reunion Kike)

**Fecha:** 2026-05-04
**Trigger:** Revision retrospectiva por cambio en evidencia tecnica aguas arriba. Tres insumos nuevos invalidan parcialmente la evidencia del gate original: (a) Liliam I&D corrige el umbral de disparo del NTC y confirma que los 60 °C del bloque §3 son erroneos; (b) Liliam I&D aporta dato verificado de Breakermatic (50 ms en laboratorio Genteca) que modifica el paisaje competitivo para el claim de velocidad; (c) reunion Kike 04-05-2026 consolida la Alternativa D con eje propio "Hasta 10 veces mas rapido". Adicionalmente, el Owner emite decision sobre el claim "autentica proteccion inverter" y sobre el lineamiento del argumentario ESC.
**Insumos consultados:**
- `00-brief/whatsapp/Chat con Liliam I&D.txt` — correccion umbral NTC (132 °C disparo, 140-145 °C destruccion rele), confirmacion Breakermatic 50 ms verificado en laboratorio Genteca, rango Genteca 20-30 ms en laboratorio (16-32 ms teorico).
- `00-brief/whatsapp/Chat con Jose Miguel Canudas 2.txt` — descripcion tecnica curva de tiempo inverso, temperatura de disparo a 132 °C en pin del rele, mecanismo de calentamiento por sobrecarga y por condiciones ambientales.
- `00-brief/transcripts/Meeting Transcription 04-05-2026.txt` — reunion Kike (Alberto Betancourt): ideas para Alternativa D, argumento flickers vs picos, formulacion "diez veces mas rapido", QR en lengüeta.
- WORKSTREAM_v5_innovaciones.md §Refresh 2026-05-04 — decisiones Owner sobre claim "Hasta 10 veces mas rapido", pilar "autentica proteccion inverter", Alternativa D.
- Bruna_gate_empaque_v1.md §3.3 y §3.4 — bloque NTC original con 60 °C a corregir.
- BR-5 transversal `04-system/03-governance/BR-5_regla-claims-superlativos-mercados-opacos_2026-05-03.md` — Precedentes #1, #2, #3.

**Alcance de este refresh:** correcciones tecnicas que aplican a las 4 alternativas (A, B, C, D) + gate de claims exclusivos de Alternativa D + lineamiento ESC.

---

### §7.1 Reescritura del bloque del asterisco NTC (correccion obligatoria — aplica a A, B, C, D)

#### Situacion que dispara la correccion

El bloque §3.3 y §3.4 del gate original contienen el valor "60 °C internos" como umbral de disparo del NTC. Ese dato provenia de una comunicacion previa del Owner que el propio Owner reconoce como incierto ("creo recordar sin estar seguro"). Liliam I&D, consultada directamente, no recuerda haber mencionado los 60 °C y aclara que el NTC dispara cerca de 132 °C internos (junto al pin del rele), no a 60 °C. El rele se daña por encima de 140-145 °C. A 132 °C, Liliam confirma que cables y bornera de la instalacion se mantienen seguros.

La decision del Owner es explicita: **no comunicar temperaturas en el empaque**. Por tanto, la correccion no consiste en sustituir 60 °C por 132 °C, sino en **retirar toda referencia numerica de temperatura** del bloque y reformular en terminos funcionales.

Los cables THW se dañan a partir de 75 °C y los TW a partir de 60 °C. Esa temperatura critica se alcanza en el area de los bornes de conexion por corriente alta o falsos contactos, no en el rele directamente. El NTC abre el circuito antes de que esas temperaturas criticas se alcancen en los cables o en los bornes.

#### Bloque §3.3 corregido — condensado para empaque (texto definitivo, aplica a A/B/C/D)

El texto que sigue **reemplaza** al §3.3 original en su integridad. Oz debe implementar este texto en el retiro de todas las alternativas que usen el asterisco NTC.

> **Sensor NTC:** sensor de temperatura ubicado junto al rele de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que cables o conexiones de los bornes se dañen por calentamiento. Protege al protector mismo y a la instalacion electrica. Para cargas de baja demanda de corriente, el sensor NTC protege al protector y al cableado, pero no actua como proteccion de sobrecarga directa de la carga conectada. Funciona como capa adicional de proteccion termica; no reemplaza al interruptor termomagnetico de la instalacion.

#### Bloque §3.4 corregido — completo para QR y argumentario (reemplaza al §3.4 original)

> **Sensor NTC incorporado — que es, como actua y que protege**
>
> El Sensor NTC es un sensor de temperatura incorporado junto al rele de potencia del protector — el componente que maneja directamente la corriente de la carga conectada. Cuando la temperatura en ese punto aumenta por sobrecorriente, por rotor trabado o por conexiones deficientes (bornes flojos, falsos contactos), el NTC actua sobre el circuito de control y ordena la apertura del rele, desconectando la carga antes de que el calentamiento alcance niveles que puedan dañar al rele mismo o a la instalacion.
>
> **Que protege:**
> - Al protector mismo: evita que el rele de potencia alcance la temperatura de destruccion.
> - Al cableado de la instalacion: corta la corriente antes de que el calentamiento prolongado en el area de conexion dañe los conductores o su aislante.
> - A la instalacion en caso de conexiones deficientes: el calor generado por bornes flojos o falsos contactos activa la proteccion antes de que ese punto caliente se propague.
>
> **Que no protege directamente:**
> La carga conectada (motor, compresor, electronica) no queda protegida termicamente de forma directa en todos los casos. El NTC actua cuando la corriente de la carga se aproxima al limite nominal del protector. Para equipos de baja demanda de corriente, el sensor protege al protector y al cableado, pero no actua como proteccion de sobrecarga de la carga misma.
>
> **Relacion con el interruptor termomagnetico:**
> El Sensor NTC arma una curva de disparo de tiempo inverso — mientras mayor es la sobrecarga, mas rapido actua. Esta curva es del mismo tipo que la de un breaker termomagnetico, pero un poco mas lenta, lo que asegura que el breaker quede como el ultimo elemento de maniobra en condiciones criticas. El NTC actua como capa adicional de proteccion termica; no reemplaza al interruptor termomagnetico. La correcta seleccion y calibracion del breaker por parte del instalador sigue siendo indispensable.
>
> **Nota sobre cargas pequenas:**
> Para equipos de baja demanda de corriente, el sensor NTC protege al protector y a la instalacion, pero no actua como proteccion de sobrecarga del equipo conectado. Esta es una caracteristica de diseno: el protector de voltaje no mide corriente de la carga ni esta disenado como sustituto de un termico electromecanico.

#### Validez de decisiones de gate previas sobre Claim D y Claim E

Las decisiones de gate sobre **Claim D ("Sensor NTC incorporado*")** y **Claim E ("Autoproteccion termica")** de §2 **permanecen vigentes** en cuanto a texto de tiro y logica de caveat. Lo que cambia es exclusivamente el contenido del bloque de retiro del asterisco, que queda sustituido por los textos corregidos arriba. El asterisco en el tiro sigue siendo condicion obligatoria.

**Rationale de la correccion:** la descripcion funcional del NTC (detecta calentamiento, abre antes de que cables o bornes se dañen, protege al protector y a la instalacion, no protege directamente a cargas pequenas, no reemplaza al termomagnetico) es identica en la version corregida. El unico elemento cambiado es la referencia numerica de temperatura, que era erronea y cuya inclusion violaria ademas la decision Owner de no comunicar temperaturas en empaque.

**Criterio RISK-POLICY aplicado:** RISK-POLICY v1.0 no contiene clausula especifica de claims de publicidad. Criterio propio Bruna: un claim tecnico que contiene un dato numerico incorrecto debe corregirse antes de produccion. La correccion no invalida el gate conceptual del claim — la funcion descrita sigue siendo tecnicamente correcta. No se requiere nuevo gate para el claim D ni E; se requiere implementar el bloque de retiro corregido.

---

### §7.2 Gate del nuevo claim "Hasta 10 veces mas rapido" (eje propio de Alternativa D)

#### Evidencia disponible

- Genteca: 20-30 ms en laboratorio (16-32 ms teorico) — Liliam I&D, confirmado en laboratorio Genteca.
- Breakermatic: 32-64 ms (50 ms tipico) — competencia mas cercana, verificado en laboratorio Genteca (Liliam confirma que el dato que Breakermatic publica es correcto y fue corroborado).
- WellSpec: 200-300 ms (publicado en datasheet).
- Powest: 1.000 ms (publicado o referenciado en insumos Orlan).
- Resto del mercado venezolano relevante: igual o peor que WellSpec segun OL-5 de Orlan.

Ratio Genteca vs Breakermatic: mejor caso Genteca (20 ms) vs peor caso Breakermatic (64 ms) = 3,2x. Caso tipico: 25 ms vs 50 ms = 2x. El rango "hasta 10 veces" no es sostenible comparado contra Breakermatic.

Ratio Genteca vs WellSpec: 25 ms vs 250 ms = 10x. Ratio Genteca vs Powest: 25 ms vs 1.000 ms = 40x. "Hasta 10 veces mas rapido" es sostenible comparado contra el grueso del mercado (todos excepto Breakermatic).

**Decision Owner 2026-05-04:** usar "Hasta 10 veces mas rapido" como claim de Alternativa D. El Owner entiende que es maximo, no promedio.

#### Decision de gate: APROBADO CON CAVEAT

**Texto literal aprobado para Solenne (Alternativa D, tiro):**
"Hasta 10 veces mas rapido"

**Condicion de uso:** este claim aplica exclusivamente a la **Alternativa D**. No se extiende a A, B ni C salvo decision expresa del Owner tras presentacion a Junta.

**Caveat de retiro — texto literal obligatorio (palabra por palabra):**
> Tiempo de respuesta de menos de 30 milisegundos (< 0,03 s) ante parpadeos (fluctuaciones rapidas del voltaje de red). Comparado contra los tiempos de respuesta publicados o verificados en laboratorio para los principales protectores de voltaje enchufables en el mercado venezolano. "Hasta 10 veces mas rapido" corresponde a la comparacion con los competidores de mayor latencia en el mercado. El competidor mas cercano en velocidad opera en un rango de 32 a 64 ms. Segun pruebas de laboratorio I&D Genteca.

**Rationale:** la formulacion "Hasta 10 veces mas rapido" usa el cuantificador "hasta", que acota el claim al maximo del rango de comparacion, no a la media. El "hasta" es la palabra que hace el claim tecnicamente defendible: afirma que existe al menos un caso (WellSpec: 200-300 ms, Powest: 1.000 ms) donde el ratio es de 10x o mas. Eso es factualmente correcto. El riesgo es que el comprador interprete "hasta 10 veces" como un promedio universal que tambien aplica contra Breakermatic — lo cual seria falso (ratio de 2x en el caso tipico). El caveat de retiro mitiga ese riesgo citando el rango completo y mencionando que el competidor mas cercano tiene 32-64 ms, sin nombrarlo.

El claim es mas agresivo que el "El mas rapido ante parpadeos (< 0,03 s)" de la Alternativa A, pero mas honesto que "10 veces mas rapido" sin "hasta". El cuantificador "hasta" es la diferencia critica: sin el, el claim seria en promedio falso; con el, es en su maximo verdadero.

**Clasificacion de riesgo:**
- Dimension dominante: reputacional (si Breakermatic o su red de distribuidores argumenta que no son 10x mas lentos, lo cual es facticamente correcto).
- Dimension secundaria: tecnica (el dato propio esta verificado; el ratio de 10x aplica al grueso del mercado).
- Nivel: medio. Manejable con el caveat de retiro y con la restriccion de que el claim es exclusivo de D.

**Clausula RISK-POLICY aplicada:** criterio Bruna documentado en BR-5 Precedente #1 — superlativo cuantitativo con dato verificable en mercado con opacidad competitiva parcial. La novedad aqui es que el dato de Breakermatic es ahora conocido y verificado, lo que convierte la opacidad de "alta" a "parcial". El cuantificador "hasta" resuelve esa tension: permite usar el ratio maximo sin afirmar que ese ratio aplica a todos los competidores.

**Precedente BR-5 referenciado:** Precedente #1 (superlativo cuantitativo verificable — condiciones 1, 2 y 3 cumplidas con la salvedad de que existe un competidor con dato publicado y verificado). Este gate sienta un sub-precedente nuevo: uso de "hasta" como cuantificador de maximo en claims de ratio comparativo cuando existe un competidor cercano que reduce el ratio promedio. Ver §7.6 nota para append a BR-5.

---

### §7.3 Reconfirmacion de "El mas rapido del mercado" tras dato Breakermatic

#### Pregunta de gate

¿Sigue siendo defendible "El mas rapido ante parpadeos (< 0,03 s)" (Claim A, aprobado con caveat en gate original) ahora que Liliam I&D confirma que Breakermatic tiene 32-64 ms (50 ms tipico) verificado en laboratorio Genteca?

#### Decision: CONFIRMADO. Claim A sigue aprobado. Caveat ajustado (ver abajo).

**Razonamiento:**

El claim "El mas rapido ante parpadeos" afirma que Genteca tiene el menor tiempo de respuesta ante parpadeos del mercado venezolano. Genteca: 20-30 ms en laboratorio. Breakermatic: 32-64 ms. En todos los escenarios de comparacion, Genteca es mas rapido que Breakermatic:

- Caso desfavorable para Genteca (30 ms) vs caso favorable para Breakermatic (32 ms): Genteca sigue siendo mas rapido por 2 ms.
- Caso tipico: 25 ms vs 50 ms. Genteca es mas rapido.
- Ninguno de los demas competidores relevantes tiene un dato que se aproxime a 30 ms (WellSpec 200-300 ms, Powest 1.000 ms, resto segun OL-5 Orlan).

El superlativo "el mas rapido" sigue siendo factualmente correcto: en toda la evidencia disponible (publicada y verificada en laboratorio), Genteca tiene el menor tiempo de respuesta del mercado venezolano para protectores enchufables residenciales monofasicos.

**Lo que cambia:** el gate original aprobaba el claim asumiendo que ningun competidor venezolano publicaba un dato comparable. Ahora existe un competidor (Breakermatic) con un dato verificado que se acerca (50 ms vs 25 ms tipico Genteca). El superlativo sigue siendo defensible, pero el caveat de retiro debe actualizarse para reflejar la existencia de ese competidor cercano y evitar que el claim parezca mas absoluto de lo que es.

**Caveat de retiro actualizado — texto literal obligatorio (reemplaza al caveat de Claim A en §2):**
> El tiempo de desconexion de menos de 30 milisegundos (< 0,03 s) aplica ante parpadeos (fluctuaciones rapidas del voltaje de la red electrica) e inestabilidad de la red. No aplica a la desconexion ante sobre voltaje o bajo voltaje pronunciados, cuyo tiempo de desconexion es de 0,4 a 3 segundos segun la intensidad de la falla. Genteca es el protector enchufable monofasico con el menor tiempo de respuesta verificado ante parpadeos en el mercado venezolano. Segun pruebas de laboratorio I&D Genteca y verificacion comparativa de competidores.

**Nota a Solenne:** el texto del caveat de retiro para las Alternativas A, B y C debe actualizarse al texto de arriba. El caveat previo de §2 Claim A queda obsoleto. El nuevo texto no cambia el claim del tiro; solo agrega la referencia a la verificacion comparativa para aumentar la solidez defensiva.

**Clasificacion de riesgo (recalibrada):** el nivel baja de "medio" a "medio-bajo". La existencia de un dato verificado de Breakermatic que es inferior al de Genteca (no superior) fortalece la posicion de Genteca: ya no se trata solo de ausencia de evidencia contraria sino de evidencia positiva de superioridad.

**Clausula RISK-POLICY aplicada:** BR-5 Precedente #1, condicion 2 — no existe competidor con dato PUBLICADO igual o superior al dato propio. La nueva informacion (Breakermatic 50 ms verificado en laboratorio Genteca) confirma y no revierte esa condicion: 50 ms es inferior en velocidad a 25-30 ms.

---

### §7.4 Claim "autenticamente protege tecnologia inverter" (off-empaque, ESC, QR)

#### Claim evaluado

"Autenticamente protege tecnologia inverter" — como claim de frente de empaque vs como claim off-empaque (QR, argumentario ESC).

#### Decision: RECHAZADO para frente de empaque. APROBADO CON CAVEAT para QR y argumentario ESC.

**Razonamiento para frente de empaque:**

El adverbio "autenticamente" implica que otros protectores que dicen proteger inverter no lo hacen autenticamente — es decir, es un comparativo implicito contra competidores identificables. En empaque fisico, ese comparativo implicito introduce el riesgo de denigrar a la competencia sin la evidencia explicita que lo sustente en el propio empaque. El comprador que lee "autenticamente" en el frente del empaque no tiene acceso inmediato al argumento tecnico (flickers vs picos, tiempo < 30 ms) que lo sostiene.

Ademas, el argumento tecnico subyacente requiere que el comprador entienda: (a) que los equipos inverter traen supresores de pico de fabrica, (b) que lo que daña la electronica inverter son los flickers, no los picos, (c) que solo una respuesta sub-30 ms corta el flicker antes del daño. Ese argumento no cabe en el tiro del empaque. Sin el argumento, "autenticamente" es un adverbio intensivo vacio que no agrega valor defensible al claim.

El claim "Protege tecnologia Inverter" (Claim C, aprobado con caveat) ya esta en frente. Agregar "autenticamente" al claim de frente no agrega valor de diferenciacion defensible — el diferenciador real ya esta comunicado en el dato "< 0,03 s" que aparece junto al claim de inverter (condicion de diseno aprobada en gate original §2 Claim C).

**Razonamiento para QR y argumentario ESC:**

En el QR, el landing page puede desarrollar el argumento completo flickers vs picos + dato Genteca < 30 ms + explicacion de que la competencia con > 100 ms no puede cortar el flicker antes del daño. Ese contexto hace que "autenticamente" este justificado porque el lector tiene acceso al argumento tecnico completo que lo sustenta.

En el argumentario ESC, el mismo argumento completo puede desarrollarse oralmente. El ESC puede explicar la cadena tecnica y concluir "somos los que autenticamente protegen inverter".

**Caveat para QR y ESC (texto orientativo — Solenne desarrolla wording final para QR):**
El argumento a desarrollar es: los equipos inverter traen supresores de pico de alta energia incorporados de fabrica porque sus fabricantes saben que esos picos los dañan. Lo que no traen es proteccion contra flickers (fluctuaciones rapidas voltaje cero / voltaje nominal en fracciones de segundo). Los flickers dañan la electronica de control inverter porque la exponen a ciclos repetidos de arranque y corte. Solo un protector con tiempo de respuesta < 30 ms puede abrir el circuito dentro del flicker, antes de que ese ciclo se complete y dañe los componentes. Un protector con > 100 ms actua despues de que el flicker ya paso — o actua durante el siguiente, cuando el daño puede haberse iniciado. Esa diferencia es la que hace que Genteca proteja auténticamente la tecnologia inverter.

**Confirmacion de la decision Owner 2026-05-04:** el argumento "los competidores con > 100 ms no protegen autenticamente inverter" queda off-empaque. Para el frente del empaque sigue vigente "Protege tecnologia Inverter" (Claim C aprobado). Esta decision de Owner es coherente con el juicio de Bruna.

**Clasificacion de riesgo:**
- En frente de empaque: alto (comparativo implicito sin argumento accesible en el propio empaque, riesgo de denigrar a competencia sin sustento visible).
- En QR y argumentario ESC: bajo-medio (el argumento tecnico esta disponible; en ESC es venta directa con contexto; en QR el landing puede controlarse editorialmente).

**Clausula RISK-POLICY aplicada:** BR-5 Precedente #2 — comparativo implicito en empaque debe tener RTB accesible en el propio empaque para sostenerse. Sin el argumento visible, "autenticamente" es un comparativo implicito sin sustento inmediato.

---

### §7.5 Argumento "10x mas rapido" para argumentario ESC sin restricciones

#### Pregunta de gate

El Owner senala que la guerra competitiva del ESC permite mayor libertad argumentativa que el empaque. ¿Cual es el piso minimo de veracidad que aplica incluso en argumentario ESC?

#### Lineamiento para argumentario ESC

**Lo que el ESC puede decir:**

- "Somos 10 veces mas rapidos que la mayoria de los protectores del mercado." — PERMITIDO. El ratio de 10x es real comparado contra WellSpec (200-300 ms), Powest (1.000 ms) y el grueso del mercado. "La mayoria" encuadra el claim sin afirmar que aplica a todos.

- "El competidor mas cercano en velocidad es de 50 ms. Nosotros somos de 25 ms. El doble de rapidos que el mas rapido del mercado despues de nosotros." — PERMITIDO. Dato verificado en laboratorio Genteca. El ESC puede citar este dato en conversacion directa con el cliente, especialmente con instaladores tecnicos.

- "Los que dicen que son compatibles inverter pero tienen > 100 ms de tiempo de respuesta no pueden cortar el flicker. Nosotros con < 30 ms si podemos." — PERMITIDO. Afirmacion tecnica defendible: un tiempo de respuesta de 100 ms ante un flicker de 50 ms no puede abrir antes de que el flicker se complete. El argumento no nombra marcas por nombre; aplica como criterio tecnico general.

- "Somos los mas rapidos del mercado venezolano, con menos de 30 ms verificado en nuestro laboratorio." — PERMITIDO. Dato verificado.

**Lo que el ESC NO puede decir:**

- "Somos 10 veces mas rapidos que Breakermatic." — PROHIBIDO. Es factualmente falso: Breakermatic tiene 32-64 ms (50 ms tipico), lo que da un ratio de 2x con Genteca, no 10x. Un instalador tecnico que conozca a Breakermatic puede refutar el dato en el acto, dañando la credibilidad del ESC y de Genteca.

- "Breakermatic no protege inverter." — PROHIBIDO. Es una afirmacion sobre la funcionalidad de un producto de un competidor que puede ser incorrecta en parte (Breakermatic puede proteger ante algunos flickers) y es un comparativo directo denigratorio que puede generar conflicto legal incluso en venta directa.

- "Los demas no sirven para inverter." — PROHIBIDO en esa forma generica. La formulacion correcta es la tecnica: "para proteger contra flickers necesitas menos de 30 ms; si el protector tiene > 100 ms, no puede cortar el flicker en tiempo."

- Cualquier garantia de resultado ("con Genteca tu equipo inverter nunca se daña") — PROHIBIDO. Aplica Precedente BR-5 #4 incluso en venta directa.

**El piso minimo de veracidad para ESC:** el ESC no puede afirmar datos numericos falsos sobre Genteca ni sobre competidores. La mayor libertad del ESC reside en el argumento tecnico (mas elaborado, mas comparativo, mas critico de la competencia como clase) pero no en la libertad de inventar o exagerar datos. Un ESC que cita "10x mas rapido que Breakermatic" cuando el dato real es 2x esta mintiendo a un cliente tecnico que puede verificarlo — ese error no solo es un riesgo legal sino un riesgo de reputacion inmediato en el campo.

**Clausula RISK-POLICY aplicada:** RISK-POLICY v1.0 §3 (manejo de errores) — el principio de que los agentes no deben afirmar cosas que puedan ser falsas se traslada como principio al ESC. El ESC es un representante de Genteca; un dato falso dicho por el ESC es un dato falso de Genteca.

---

### §7.6 Notificacion en cascada

Las siguientes actualizaciones son requeridas. Este refresh de Bruna es el disparador.

**Solenne — SO-1 v2:**
- Integrar el bloque §3.3 corregido (sin temperaturas) como texto del asterisco NTC en **todas las alternativas A, B, C y D**. El bloque §3.3 original del gate v1 queda obsoleto.
- Integrar el caveat de retiro de Claim A actualizado (§7.3) en Alternativas A, B y C. El caveat anterior de §2 Claim A queda obsoleto.
- Integrar el claim "Hasta 10 veces mas rapido" y su caveat de retiro (§7.2) en la Alternativa D. Este claim no se usa en A, B ni C.
- El claim "Protege tecnologia Inverter" (Claim C) sigue vigente en todas las alternativas. Sin cambio en texto del tiro.

**Atlas — mockup D + revision menor A/B/C:**
- Mockup D: nuevo eje "Hasta 10 veces mas rapido" como claim principal del tiro, junto a los 3 claims con flecha conectora grafica segun idea de reunion Kike (< 0,03 s — autentica proteccion inverter — NTC). QR en posicion prominente junto a los 3 claims o en lengüeta.
- Alternativas A/B/C: el cambio del asterisco NTC es textual (retiro), no visual (tiro). El frente del tiro no cambia. Atlas no necesita ajustar el mockup del tiro de A/B/C por este refresh; solo confirmar que el retiro implementara el texto actualizado de Solenne.

**Aurelio — AU-1 v2:**
- Incluir la Alternativa D con su eje propio "Hasta 10 veces mas rapido" (gateado por Bruna en §7.2).
- Corregir la slide competitiva: Breakermatic tiene 32-64 ms (50 ms tipico) verificado en laboratorio Genteca — no los 200-300 ms que podrian haberse atribuido antes si se asumiá que solo WellSpec tenia dato comparable. El dato de WellSpec (200-300 ms) sigue siendo el que justifica el "hasta 10 veces" para el grueso del mercado.
- El dato correcto para la slide: Genteca < 30 ms / Breakermatic 50 ms (verificado lab) / WellSpec 200-300 ms / Powest 1.000 ms / resto >= 200 ms.
- El framing correcto para la Junta: "somos el mas rapido del mercado; el competidor mas cercano tiene el doble de nuestro tiempo de respuesta tipico."

**Vivienne — PPTX v2:**
- Incorporar las mismas correcciones de datos competitivos que Aurelio.
- Incorporar la Alternativa D y el nuevo claim gateado.
- Eliminar toda referencia a "60 °C" como umbral NTC si aparece en el deck.

**Orlan — refresh menor:**
- Actualizar OL-5 (o producir OL-5 v2 entrada) con el dato de Breakermatic verificado: 32-64 ms (50 ms tipico), confirmado en laboratorio Genteca por Liliam I&D. Esta es la unica actualizacion requerida en el landscape competitivo. No invalida ninguna decision de gate anterior — Genteca sigue siendo el mas rapido.
- Nota de refresh para Orlan: el dato de Breakermatic es ahora una fortaleza defensiva (tenemos un competidor con dato verificado y somos mas rapidos), no una debilidad. El panorama competitivo no cambia de "Genteca unico bajo 30 ms" a "Genteca entre varios bajo 50 ms" — Genteca sigue siendo el unico bajo 30 ms.

---

### §7.7 Actualizacion de precedentes BR-5 (para append)

Este refresh genera dos sub-precedentes nuevos para append al BR-5 transversal. Raul o Celeste ejecutan el append en el momento que corresponda.

**Sub-precedente 7-A (append a Precedente #1):** Cuando existe un competidor con dato verificado pero inferior en performance al dato propio, el superlativo del dato propio se fortalece (ya no es solo ausencia de evidencia contraria — es evidencia positiva de superioridad). El caveat de retiro debe actualizarse para citar la verificacion comparativa. El nivel de riesgo del claim baja.

**Sub-precedente 7-B (nuevo, tipo "cuantificadores de maximo en comparativos"):** El cuantificador "hasta" convierte un claim de ratio comparativo (10x) de potencialmente falso en promedio a verdadero como maximo cuando existe al menos un competidor relevante contra el cual el ratio se cumple. Condiciones de uso: (a) el cuantificador "hasta" debe estar presente — sin el, el claim es indistinguible de una afirmacion de promedio; (b) el caveat de retiro debe citar el rango completo y mencionar que el competidor mas cercano tiene un dato distinto; (c) el claim no puede usarse en contextos donde el comprador pueda interpretarlo razonablemente como promedio (ej. en argumentario ESC con instaladores tecnicos que conocen a Breakermatic, el ESC debe usar la formulacion precisa de §7.5, no el "hasta 10 veces" del empaque).

---

### References §7

| Documento | Referencia especifica | Uso en este refresh |
|---|---|---|
| Chat con Liliam I&D.txt | Correccion 60 °C → 132 °C NTC; confirmacion Breakermatic 32-64 ms; rango Genteca 20-30 ms lab | Evidencia tecnica primaria para §7.1 y §7.3 |
| Chat con Jose Miguel Canudas 2.txt | Temperatura 132 °C pin del rele; curva tiempo inverso; mecanismo sobrecarga y temperatura ambiente | Sustento tecnico para reescritura §7.1 |
| Meeting Transcription 04-05-2026.txt | Ideas Alternativa D; argumento flickers vs picos; formulacion "10 veces mas rapido"; QR en lengüeta | Contexto para §7.2 y §7.4 |
| WORKSTREAM_v5_innovaciones.md §Refresh 2026-05-04 | Decisiones Owner: "Hasta 10 veces mas rapido", off-empaque del "autenticamente", Alternativa D, lineamiento ESC | Decisiones Owner formalizadas |
| Bruna_gate_empaque_v1 §3.3, §3.4, §2 Claim A, §2 Claim C | Textos originales a corregir o confirmar | Trazabilidad de cambios |
| BR-5 transversal Precedentes #1, #2, #3 | Criterios de superlativos y comparativos aplicados | Marco de criterio precedente |
| RISK-POLICY.md v1.0 | §3 principio de no afirmar datos falsos | Fundamento para piso ESC |

---

*Refresh emitido: 2026-05-04*
*Estado: CERRADO — Correcciones tecnicas obligatorias y nuevos gates listos para SO-1 v2, Atlas mockup D, AU-1 v2, Vivienne PPTX v2, Orlan refresh menor*
*Proxima revision requerida: si Paxs desvela dato OEM de TQ < 30 ms; si un competidor nuevo publica dato verificado < 50 ms; si el landing del QR usa formulacion de "autenticamente" sin el argumento tecnico completo.*

---

## §8 — Refresh 2026-05-05 — Gate naming funcion termica B-sin-NTC

**Fecha:** 2026-05-05
**Trigger:** Junta Directiva elige Alternativa B. Vael entrega VA-5 naming-funcion-termica_v1 (con §Refresh 2026-05-05) con finalista unica recomendada: "Autoproteccion termica activa*". Bruna recibe instruccion de gatear esa formulacion antes del memo de Aurelio para la Junta de manana. Tres preguntas especificas de gate: (1) ¿"activa" es defendible?, (2) ¿es extension del Claim E aprobado o claim nuevo?, (3) ¿el caveat de retiro propuesto por Vael satisface o requiere ajuste?

**Insumos consultados para este refresh:**
- Vael_VA-5_naming-funcion-termica_v1.md (2026-05-05) — 5 opciones + §Refresh Owner (Opciones A y B) + finalista recomendada con texto de retiro
- Orlan_OL-1_competencia-naming-termico_v1.md (2026-05-05) — §3 terminologia vacante, §4 nota especifica para Bruna sobre "activa"
- Bruna_gate_empaque_v1 §2 Claim D y Claim E (gate original 2026-05-03) — estado aprobado vigente
- Bruna_gate_empaque_v1 §7.1 (Refresh 2026-05-04) — bloque NTC corregido, sin temperaturas numericas, vigente
- BR-5 transversal `04-system/03-governance/BR-5_regla-claims-superlativos-mercados-opacos_2026-05-03.md` — Precedentes #1 a #4
- Vera_brief_tecnico_v1 §1.1-§1.4 — mecanismo NTC (disponible via Claim D/E previos; no hay nuevo insumo de Vera en este refresh)

---

### §8.1 Pregunta 1 — ¿"activa" es defendible bajo RISK-POLICY y BR-5?

#### Descomposicion del claim

**Texto del tiro:** "Autoproteccion termica activa*"

**Lo que dice exactamente:** El protector tiene un sistema que se autoprotege del calor de forma activa.

**Lo que entenderia el lector promedio (consumidor residencial):** "Tiene algo que detecta el calor y actua solo." El adjetivo "activa" comunica dinamismo y autonomia — en lenguaje cotidiano, una proteccion "activa" es una que esta en funcionamiento continuo, vigilando.

**Lo que entenderia el instalador tecnico:** "Activa" diferencia entre proteccion pasiva (ej. fusible termico de un solo uso, que simplemente se funde) y proteccion activa (sensor que monitorea y actua sobre el circuito). Esta distincion es tecnica y relevante para el profesional.

**Fact tecnico invocado:** El NTC opera con curva de tiempo inverso — a mayor temperatura, mayor resistencia, mas rapida la actuacion. Esta es una respuesta continua y proporcional al estimulo termico; no es un corte binario de un solo uso como un fusible convencional.

**Riesgo critico identificado (flag Vera Pendiente P-5):** Vael VA-5 y Orlan OL-1 §4 senalan que existe incertidumbre sobre si el NTC del GSM opera como sensor activo de monitoreo continuo o como fusible termico de corte unico (se destruye tras actuar, igual que un fusible). Si la respuesta es "solo corte unico", el adjetivo "activa" se vuelve tecnicmente inexacto: una proteccion de corte unico que luego queda inoperativa no es "activa" en el sentido de monitoreo continuo.

#### Analisis de riesgo — tres dimensiones

**Dimension tecnica:**
- Si NTC = monitoreo continuo con curva de tiempo inverso: "activa" es preciso. El NTC esta continuamente ajustando su resistencia en funcion de la temperatura; actua como sensor permanente, no como fusible.
- Si NTC = fusible termico de corte unico: "activa" seria inexacto. Una proteccion que actua una sola vez y queda inutilizada hasta ser reemplazada no es "activa" en ninguna lectura razonable del termino.
- Evidencia disponible: Vera_brief_tecnico_v1 §1.1-§1.2 describe el NTC con curva de tiempo inverso (Canudas en WhatsApp confirma la curva). Esto es consistente con monitoreo continuo. Sin embargo, Vael y Orlan identifican la incertidumbre sobre reseteo/reutilizacion del NTC tras actuar (Pendiente P-5 sin resolver). Bruna no puede resolver ese hecho tecnico sin Vera.
- Nivel de riesgo tecnico: **medio** — el mecanismo de curva de tiempo inverso apoya "activa"; la incertidumbre sobre reutilizacion es el factor que no esta cerrado.

**Dimension reputacional:**
- Orlan OL-1 §3 confirma que "Autoproteccion termica activa" es territorio vacante en competidores VE. Ningun competidor puede objetar uso previo del termino.
- Si un instalador tecnico cuestiona "activa" argumentando que el NTC es un fusible de un solo uso, la discusion seria: "su producto dice 'activa' pero en realidad se destruye al actuar". Ese cuestionamiento tendria base si el NTC es de corte unico.
- Nivel de riesgo reputacional: **bajo en condicion de monitoreo continuo / medio en condicion de corte unico**.

**Dimension regulatoria:**
- No hay norma venezolana (COVENIN) ni regional verificada que defina "proteccion activa" para este tipo de dispositivo. El riesgo regulatorio es bajo.
- El riesgo relevante es el de publicidad engañosa bajo la Ley de Proteccion al Consumidor venezolana si el adjetivo induce una expectativa que el producto no cumple.
- Nivel de riesgo regulatorio: **bajo** (no hay marco normativo especifico; el riesgo es de reclamacion de consumidor, no de sancion regulatoria directa).

#### Decision sobre "activa" — condicional estructurada

**Si Vera confirma que el NTC del GSM opera con monitoreo continuo y es reutilizable tras enfriarse (no es fusible de corte unico):**
**"Autoproteccion termica activa*" — APROBADO CON CAVEAT** (extension del Claim E, categoria de riesgo inalterada).
El adjetivo "activa" es tecnicamente preciso. El caveat de retiro propuesto por Vael mitiga adecuadamente el alcance funcional. No se requiere gate adicional.

**Si Vera confirma que el NTC del GSM es fusible termico de corte unico (se destruye al actuar y requiere reemplazo del protector):**
**"Autoproteccion termica activa*" — RECHAZADO**. El adjetivo "activa" implica vigilancia continua que el mecanismo no tiene. Formulacion de respaldo: "Autoproteccion termica*" (Claim E ya aprobado, sin "activa") — disponible inmediatamente sin gate adicional.

**Decision default para la Junta de manana (2026-05-06) — sin confirmacion de Vera antes de la reunion:**

Bruna aprueba con caveat la formulacion "Autoproteccion termica activa*" bajo el supuesto declarado de que el NTC opera con curva de tiempo inverso continua (evidencia disponible en WhatsApp Canudas, consistent con §1.2 Vera). Este supuesto es tecnicamente plausible y es la interpretacion de los hechos disponibles. La aprobacion es **provisional** hasta que Vera cierre el Pendiente P-5.

**Razon para no bloquear:** el texto de retiro propuesto por Vael ya menciona "sensor de temperatura" — no dice "sensor de monitoreo continuo" ni "reutilizable". Por tanto, incluso si el NTC fuera de corte unico, el retiro no induciria una expectativa erronea sobre el mecanismo. El riesgo de la palabra "activa" en el tiro es reputacional/tecnico con el instalador experto; el retiro lo mitiga al describir la funcion sin prometer continuidad. Ese es el balance que hace aprobable el claim con el caveat correcto.

---

### §8.2 Pregunta 2 — ¿Extension del Claim E o claim nuevo?

**Claim E aprobado (§2, gate 2026-05-03):** "Autoproteccion termica" — APROBADO sin caveat de retiro adicional al de Claim D. El mismo bloque de retiro NTC aplica.

**Claim propuesto:** "Autoproteccion termica activa*"

**Analisis:** La adicion del adjetivo "activa" no introduce un atributo funcional nuevo — el mecanismo descrito en el retiro es identico. "Activa" es un calificador del modo de operacion del mismo mecanismo ya aprobado. No hay claims de resultado nuevos, no hay promesas adicionales de proteccion de la carga, no hay superlativos nuevos, no hay comparativos directos con competidores.

**Conclusion:** Esta es una **extension razonable** del Claim E. No es un claim nuevo que requiera gate completo desde cero. El unico punto de gate incremental es el adjetivo "activa" evaluado en §8.1. La categoria de riesgo del Claim E (bajo, aprobado sin caveat en tiro) se mantiene en bajo para esta formulacion, con el matiz condicional sobre el mecanismo del NTC.

**Por tanto:** gate flash, no gate completo. La aprobacion o rechazo de "activa" es la unica decision incremental.

---

### §8.3 Pregunta 3 — ¿El caveat de retiro propuesto satisface?

**Texto propuesto por Vael (finalista en VA-5 §Refresh 2026-05-05):**

> Autoproteccion termica activa: sensor de temperatura ubicado junto al rele de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se danen. Protege al protector mismo y a la instalacion electrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actua como proteccion de sobrecarga directa de la carga conectada. Funciona como capa adicional de proteccion termica; no reemplaza al interruptor termomagnetico de la instalacion.

**Evaluacion de Bruna:**

El texto cumple todas las condiciones del §7.1 Refresh (bloque NTC corregido): sin temperaturas numericas, sin mencion del componente por nombre (NTC) en el cuerpo del retiro, alcance correcto de proteccion al protector y al cableado, caveat de cargas pequenas presente, caveat del termomagnetico presente.

El texto es compatible con la posicion de "activa": no promete monitoreo en tiempo real ni continuidad de la proteccion en lenguaje que requeriria verificacion del mecanismo de corte unico vs. continuo. La descripcion funcional ("detecta... y desconecta") es valida para ambos modos de operacion del NTC.

**Ajuste requerido:** uno, menor y obligatorio.

La frase "Funciona como capa adicional de proteccion termica; no reemplaza al interruptor termomagnetico de la instalacion" no menciona que la funcion aplica ante calentamiento del relé por sobrecorriente Y por conexiones deficientes. En la version corregida del §7.1 esto estaba explicito. El texto de Vael lo menciona en la frase anterior ("sobrecorrientes o conexiones deficientes"), pero no lo reitera en la clausula de caveat final. Eso es aceptable — la estructura del parrafo ya lo cubre. No se requiere cambio.

**Un ajuste SI es obligatorio:** la frase de apertura "Autoproteccion termica activa:" usa el mismo texto del tiro como encabezado del retiro. Esta convencion es correcta (es la que establece §7.1 con "[Badge elegido — ver tiro]"). Pero si Bruna aprueba con caveat condicional (pendiente P-5), el encabezado del retiro debe ser coherente con la formulacion final que apruebe el Owner. Si eventualmente se usa la formulacion de respaldo "Autoproteccion termica*" (sin "activa"), el encabezado del retiro debe ajustarse en consecuencia. Oz y Solenne deben saber que el encabezado del retiro sigue al tiro — no es un texto fijo independiente.

**Conclusion sobre el caveat de retiro:** el texto propuesto por Vael satisface como base. Bruna lo aprueba **con una confirmacion operativa para Oz/Solenne**: el encabezado del retiro ("Autoproteccion termica activa:") debe actualizarse si la formulacion del tiro cambia a "Autoproteccion termica*" como resultado de la confirmacion de Vera (Pendiente P-5).

**Caveat de retiro literal — palabra por palabra — para Oz y Solenne:**

> Autoproteccion termica activa: sensor de temperatura ubicado junto al rele de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se danen. Protege al protector mismo y a la instalacion electrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actua como proteccion de sobrecarga directa de la carga conectada. Funciona como capa adicional de proteccion termica; no reemplaza al interruptor termomagnetico de la instalacion.

Este es el texto exacto. No modificar. Si la formulacion del tiro cambia a "Autoproteccion termica*" (sin "activa"), reemplazar unicamente el encabezado: "Autoproteccion termica:" — el resto del cuerpo es invariable.

---

### §8.4 Decision final de gate

**Claim evaluado:** "Autoproteccion termica activa*" (tiro) con caveat de retiro segun §8.3.

**Decision: APROBADO CON CAVEAT — condicional a Vera (Pendiente P-5)**

**Categoria:** extension razonable del Claim E aprobado (§2, 2026-05-03). No es claim nuevo.

**Condicion suspensiva (flag para Vera):**
- Si Vera confirma que el NTC opera con curva de tiempo inverso continua y es funcional tras enfriarse (no fusible de corte unico): la aprobacion queda firme. No se requiere gate adicional.
- Si Vera confirma que el NTC es fusible termico de corte unico (se destruye al actuar): "activa" debe retirarse. La formulacion de empaque pasa a "Autoproteccion termica*" (Claim E aprobado en §2, vigente sin modificacion). El caveat de retiro se mantiene identico, cambiando solo el encabezado.

**Supuesto declarado:** Bruna aprueba bajo el supuesto de que la descripcion de curva de tiempo inverso en Vera §1.2 y en WhatsApp Canudas (mecanismo de calentamiento progresivo y curva de tiempo inverso) es consistente con operacion continua del NTC, no con fusible de corte unico. Este supuesto es el mas respaldado por la evidencia disponible. La incertidumbre es sobre reseteo/reutilizacion, no sobre el mecanismo de actuacion.

**Riesgo asumido:** bajo. El caveat de retiro no promete monitoreo continuo ni reutilizacion del sensor. El adjetivo "activa" en el tiro es el unico elemento que genera la expectativa de continuidad; esa expectativa es razonable dado el mecanismo de curva de tiempo inverso confirmado.

**Caveat de retiro — texto literal obligatorio para Oz y Solenne (reproducido de §8.3):**

> Autoproteccion termica activa: sensor de temperatura ubicado junto al rele de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se danen. Protege al protector mismo y a la instalacion electrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actua como proteccion de sobrecarga directa de la carga conectada. Funciona como capa adicional de proteccion termica; no reemplaza al interruptor termomagnetico de la instalacion.

Sin este caveat literal integrado en el retiro, el claim del tiro no se considera aprobado.

---

### §8.5 Precedente para BR-5

Este gate sienta un nuevo tipo de precedente no cubierto por los Precedentes #1 a #4 del BR-5 transversal: **formulacion generica de funcion como proteccion de IP (claim de funcion sin revelar componente)**.

**Criterio sentado:**

Cuando un claim de empaque describe una funcion tecnica (ej. "autoproteccion termica activa") sin nombrar el componente que la implementa (ej. NTC, termistor, termoresistencia), el riesgo de IP inversa (revelar secreto industrial a la competencia) se elimina. El claim es plenamente defendible porque:
(a) La funcion descrita es real y verificable (RTB tecnico existe).
(b) La ausencia del nombre del componente no genera ambiguedad funcional en el retiro: el texto del asterisco describe el mecanismo sin revelar la arquitectura interna.
(c) Un competidor que copiara la formulacion tendria que implementar la funcion para sostenerla, lo que eleva el estandar de la categoria en lugar de regalar un secreto industrial.

Este criterio es aplicable en cualquier dominio de /RAUL/ donde un claim de empaque o marketing describa una funcion tecnica diferenciadora sin revelar el componente especifico que la habilita.

**Nota de append a BR-5:** Bruna identifica este caso como candidato a Precedente #5 del BR-5 transversal. El append se ejecuta tras confirmacion de Vera (Pendiente P-5): si la aprobacion queda firme, el precedente se formaliza. Si el claim es ajustado a "Autoproteccion termica*" (sin "activa"), el precedente se formaliza bajo esa formulacion. En cualquier caso, el criterio sobre "funcion sin componente" es valido independientemente del resultado de P-5.

---

### §8.6 Supuestos y dependencias

| # | Supuesto / dependencia | Impacto si cambia | Agente responsable |
|---|---|---|---|
| 1 | NTC del GSM opera con curva de tiempo inverso continua (no fusible de corte unico) | Si es fusible unico: reemplazar "activa" por formulacion de respaldo "Autoproteccion termica*" | Vera — Pendiente P-5 |
| 2 | Ninguna formulacion del universo de candidatos tiene registro de marca en SAPI Venezuela u OMPI (Orlan OL-1 §5 flag) | Si existe registro: escalar a Owner para decision de naming; no usar formulacion registrada sin autorizacion | Orlan (verificacion) + Owner (decision) |
| 3 | El caveat de retiro es texto de empaque fisico, no digital expandido | Si el espacio del retiro se reduce: Solenne debe confirmar que el texto cabe antes de enviarlo a Oz para redline | Solenne (confirmacion de espacio) + Oz (implementacion) |
| 4 | Bruna gate_empaque_v1 §7.1 bloque NTC corregido sigue siendo el texto base de retiro | Vigente. Sin cambio en este refresh | Sin accion requerida |

---

### §8.7 Notificaciones de cascada post-gate

**Solenne (SO-1 delta):**
- El tiro de la Alternativa B badge de funcion termica es: "Autoproteccion termica activa*"
- El texto del asterisco de retiro es el de §8.4 literal. Sin modificacion.
- Condicion operativa: si Vera resuelve P-5 con resultado "fusible unico", el tiro cambia a "Autoproteccion termica*" y el encabezado del retiro cambia en consecuencia. El cuerpo del retiro es invariable.

**Oz (redline arte Alternativa B):**
- Badge de tiro: "Autoproteccion termica activa*" (asterisco obligatorio).
- Texto del asterisco: segun §8.4. No usar el texto del retiro de §3.3 original — usar exclusivamente el texto de §8.3/§8.4 de este refresh.
- El encabezado "Autoproteccion termica activa:" es el texto que precede el bloque de retiro en el arte.

**Aurelio (memo flash a Junta):**
- La formulacion aprobada por Bruna para la Junta de manana (2026-05-06) es: "Autoproteccion termica activa*"
- La aprobacion es firme para la presentacion de manana. La condicion suspensiva (Vera P-5) aplica al arte final de empaque para produccion de imprenta, no al memo de Junta.
- Alternativa de respaldo si la Junta pregunta por el "activa": "Autoproteccion termica*" esta aprobada sin condicion (Claim E, §2 gate original) y puede usarse de forma inmediata si el Owner decide simplificar.

**Vera (pendiente P-5 — escalar via Raul):**
- Confirmacion requerida: ¿el NTC del GSM-MB/RB/RF/RE es reutilizable tras actuar (curva de tiempo inverso con reset al enfriar) o es de corte unico (se destruye al actuar y el protector queda inoperativo hasta reemplazo)?
- Esta confirmacion es necesaria antes de la produccion final del arte de empaque para imprenta. No es bloqueante para el memo de Junta de manana.

---

### References §8

| Documento | Referencia especifica | Uso en este gate |
|---|---|---|
| Vael_VA-5_naming-funcion-termica_v1.md (2026-05-05) | Opcion 1 tabla finalistas, §Refresh 2026-05-05 — finalista unica, texto de retiro propuesto | Claim evaluado, texto de retiro base |
| Orlan_OL-1_competencia-naming-termico_v1.md (2026-05-05) | §3 terminologia vacante, §4 nota Bruna sobre "activa" y P-5 | Landscape competitivo, flag de riesgo tecnico |
| Bruna_gate_empaque_v1 §2 Claim E | "Autoproteccion termica" — APROBADO (2026-05-03) | Claim base del que este es extension |
| Bruna_gate_empaque_v1 §7.1 | Bloque NTC corregido, sin temperaturas | Texto de retiro vigente base |
| Vera_brief_tecnico_v1 §1.1-§1.4 | Mecanismo NTC, curva tiempo inverso, alcance de proteccion | Fact tecnico que sostiene "autoproteccion" y "activa" |
| WhatsApp Canudas (Chat 2) | Curva de tiempo inverso, temperatura 132 degC pin rele | Confirmacion mecanismo continuo |
| BR-5 transversal Precedentes #1-#4 | Criterios de superlativos y formulaciones de funcion | Marco de precedente — sin precedente exacto para "funcion sin componente" |
| RISK-POLICY.md v1.0 | §3 principio de no afirmar datos que puedan ser falsos | Fundamento para condicion suspensiva sobre P-5 |

---

*Refresh emitido: 2026-05-05*
*Estado: APROBADO CON CAVEAT (condicional Vera P-5) — listo para memo Junta Aurelio, SO-1 delta Solenne, redline arte Oz*
*Proxima revision requerida: confirmacion de Vera sobre mecanismo NTC (P-5) antes de produccion de imprenta del arte final. Si P-5 = fusible unico: tiro cambia a "Autoproteccion termica*", resto invariable.*

---

# §9 — Gate de las 3 opciones B-CON-NTC (variante v2.2)

**Documento:** Bruna_gate_empaque_v1 §9
**Fecha:** 2026-05-06
**Elaborado por:** Bruna — Risk & Claims Governance Lead
**Trigger:** WhatsApp Kike → Canudas 2026-05-05 abre evaluacion de variante CON NTC. Owner instruye gatear 3 opciones candidates (A, B, C segun nomenclatura de este §9) para llevarlas con sus gates a Kike antes de avanzar a Solenne / Atlas / Aurelio. v2.1 B-sin-NTC permanece vigente y no es sustituida.

**Insumos consultados para este gate:**
- Vael_VA-5_naming-funcion-termica_v1.md §Refresh 2026-05-06 (ranking 7 opciones CON-NTC; finalista Op. 6 score 6,45; textos de retiro por opcion)
- Orlan_OL-1_competencia-naming-termico_v1.md §Refresh 2026-05-06 (vacancia territorial; riesgo IP nominal; analisis argumento Kike; tabla registrabilidad candidatos; recomendacion "Thermo-Safe" como bautizado primario)
- Bruna_gate_empaque_v1 §2 (Claims D, E, H — gate original 2026-05-03); §7.1 (bloque NTC corregido); §8 (gate "Autoproteccion termica activa*", cuerpo del caveat invariable §8.3/§8.4)
- BR-5 transversal Precedentes #1 a #4 (criterios de superlativos, exclusion, comparativos y garantias)
- RISK-POLICY.md v1.0 §3 (principio de no afirmar datos que puedan ser falsos)

**Nota sobre las 3 opciones gateadas:** el universo de candidatos de Vael §Refresh 2026-05-06 tiene 7 opciones. Bruna gateo las 3 que el Owner instruyo presentar a Kike, identificadas segun los origenes descritos en el brief de gate:

- **Opcion A del gate — "NTC EscudoTermico(TM)*":** finalista ranking Vael (Op. 6, score 6,45). Nomenclatura Vael: Op. 6.
- **Opcion B del gate — "Thermo-Safe(TM)*":** recomendacion Orlan desde optica IP nominal (OL-1 §Refresh R4 — "mejor perfil del grupo"). Esta opcion NO aparece como badge standalone en el ranking de Vael (Vael no la propuso como badge de tiro independiente — Orlan la menciono como bautizado primario para el empaque). Bruna la gateo como claim funcional derivado de los criterios del §Refresh.
- **Opcion C del gate — "Sensor NTC ThermoSafe(TM)*":** sintesis combinada (NTC visible + "ThermoSafe" bautizado Orlan IP-clean + bilingue). No contemplada explicitamente en ranking Vael ni recomendacion Orlan — emerge de la instruccion del Owner de tener una tercera opcion que combine ambas logicas.

**Nota de notacion:** este documento usa (TM) para indicar el simbolo de marca aspiracional (™) y (R) para ® cuando el contexto lo requiere, para evitar problemas de codificacion en el archivo.

---

## §9.1 — Analisis de Opcion A: "NTC EscudoTermico(TM)*"

**Texto exacto para tiro:** NTC EscudoTermico(TM)*

**Equivalencia en tabla Vael:** Opcion 6 del §Refresh 2026-05-06 (score 6,45 — primer lugar en ranking ponderado).

### §9.1.1 — Riesgo Claim H

**Analisis:** El badge "NTC EscudoTermico(TM)" no contiene promesa de proteccion de equipo ni de carga conectada. NTC nombra el componente. EscudoTermico describe una funcion de proteccion termica interna del protector, no del equipo enchufado. La palabra "Escudo" tiene resonancia de proteccion activa pero su objeto semantico en el contexto del empaque de la Alternativa B (donde los dos badges son "El mas rapido ante parpadeos < 0,03 s" y el badge termico) es el protector mismo, no la carga. El retiro (cuerpo invariable §8.3) explicita ese alcance sin ambiguedad.

**Riesgo de interpretacion Claim H por la Junta (40% del mercado):** Medio-bajo. La Junta ya recibio en la Junta de 2026-05-06 el argumento tecnico de alcance del NTC (protege al protector y al cableado, no actua como proteccion de sobrecarga directa de cargas de baja demanda). La palabra "Escudo" puede evocar proteccion mas amplia en un oyente rapido, pero el cuerpo del retiro neutraliza esa interpretacion. El riesgo residual es de percepcion, no de falsedad factual.

**Conclusion Claim H — Opcion A:** MITIGA. El badge en el tiro no activa el Claim H rechazado. El cuerpo del caveat de retiro (invariable §8.3) opera como guardrail explicitamente probado por gate §8. Si Solenne o Oz extienden el badge con frases tipo "protege tu equipo" o "cuida tu aire acondicionado" sin gate adicional de Bruna, el Claim H se reactiva. La instruccion a Solenne es: badge solo, sin extension de beneficio al equipo conectado.

### §9.1.2 — Riesgo IP marcaria

**"EscudoTermico" en espanol:** Orlan OL-1 §Refresh R3 lo clasifica como descriptor generico en espanol (combina "escudo" + "termico" — describe literalmente la funcion). Riesgo de objecion SAPI VE por falta de caracter distintivo: **medio-alto**. El examinador puede objetarlo como termino puramente descriptivo del producto.

**NTC:** siglas de dominio publico industrial (Negative Temperature Coefficient). No registrable como marca per se; es denominacion generica del tipo de componente. Su uso en el badge no agrega riesgo IP propio — es una descripcion tecnica verificable.

**Verificacion marcaria requerida antes de imprenta:** ALTA. "EscudoTermico" solo puede imprimirse con simbolo (TM) como provisional. Si Genteca busca registro formal: requiere busqueda SAPI VE con abogado marcario + opinion sobre descriptividad antes de produccion. Si Genteca decide no registrar y lo usa solo como claim de empaque (no como marca registrada): el (TM) es una aspiracion sin respaldo formal, y la barrera anti-copia se reduce significativamente porque cualquier competidor puede usar "Escudo Termico" sin oposicion registral.

**Nivel de verificacion requerido:** SAPI VE formal con abogado marcario, antes de imprenta. Condicion suspensiva de produccion (no de gate conceptual).

### §9.1.3 — Defensa anti-copia (argumento Kike)

**Analisis:** La logica anti-copia de la Opcion A descansa en el registro de "EscudoTermico" como marca. Vael §Refresh R6-5 lo articula correctamente: "Si la marca EscudoTermico se establece, Exceline tiene un activo de naming registrable. Un competidor que copie la placa no puede usar EscudoTermico(TM) en la caja si Exceline lo ha registrado." Orlan §Refresh R3 advierte que esa logica tiene una condicion: que la marca sea efectivamente registrable (el riesgo de objecion por descriptividad es medio-alto).

**Distincion critica:** La defensa anti-copia de la Opcion A es **condicional al registro**. Sin registro formal de "EscudoTermico":
- Un competidor que copie la placa NTC puede usar "Escudo Termico" sin impedimento marcario.
- El argumento de Kike (bautizado que protege) no se cumple.
- La Opcion A se comporta funcionalmente como la Op. 1 (Sensor NTC incorporado*) en terminos de defensa anti-copia.

Con registro formal de "EscudoTermico(TM)" como marca (si SAPI lo concede pese al riesgo de descriptividad):
- La defensa es alta. El competidor puede copiar la placa pero no el nombre de marca registrado.
- Este es el escenario que Vael y Kike tienen en mente.

**Evaluacion del argumento Kike para Opcion A:** Parcialmente valido. El blindaje real requiere registro marcario que no esta garantizado por la naturaleza descriptiva del termino. Bruna no puede confirmar que la Opcion A provee blindaje sin conocer el resultado de la verificacion SAPI VE.

### §9.1.4 — Compatibilidad con caveat tecnico (§8 Refresh 2026-05-05)

**Cuerpo invariable (reproducido de §8.3/§8.4):**

> sensor de temperatura ubicado junto al rele de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se danen. Protege al protector mismo y a la instalacion electrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actua como proteccion de sobrecarga directa de la carga conectada. Funciona como capa adicional de proteccion termica; no reemplaza al interruptor termomagnetico de la instalacion.

**Header del caveat para Opcion A — texto literal obligatorio:**

> NTC EscudoTermico(TM): [sigue el cuerpo invariable de §8.3 sin modificacion]

**Instruccion operativa para Oz/Solenne:** el encabezado del retiro es "NTC EscudoTermico(TM):" seguido del cuerpo invariable de §8.3. El encabezado sigue al badge del tiro: si el Owner decide ajustar la formulacion del tiro, el encabezado del retiro se ajusta en consecuencia. El cuerpo es invariable.

**Compatibilidad:** PLENA. La descripcion funcional del cuerpo ("sensor de temperatura... detecta calentamiento excesivo... desconecta la carga") es compatible tanto con "NTC EscudoTermico" como con cualquier badge alternativo del set.

### §9.1.5 — Decision de gate: Opcion A

**Decision: APROBADO CON CAVEAT**

**Condicion 1 (tecnica — caveat de retiro):** El header del retiro es "NTC EscudoTermico(TM):" seguido del cuerpo invariable de §8.3. Sin ese caveat literal, el claim del tiro no se considera aprobado.

**Condicion 2 (condicion suspensiva de produccion — IP marcaria):** El simbolo (TM) en el tiro puede usarse como provisional para la presentacion a Kike y para mockups. Para produccion de imprenta, Genteca debe completar verificacion SAPI VE formal con abogado marcario sobre la registrabilidad de "EscudoTermico" como marca en Venezuela (clase 9). Si SAPI VE objeta el termino por descriptividad: el simbolo (TM) debe retirarse del empaque final o la formulacion de la marca debe ajustarse a un termino con mayor caracter distintivo. Esta condicion no bloquea el gate conceptual; bloquea la produccion de imprenta.

**Condicion 3 (condicion suspensiva de produccion — Vera P-5):** La aprobacion hereda la condicion suspensiva del §8.1: si Vera confirma que el NTC es fusible de corte unico (no reutilizable), el adjetivo funcional "activa" de la v2.1 no aplica a este badge (Opcion A no usa "activa"), pero si Vera contradice la descripcion funcional del cuerpo del caveat, el texto del retiro debe revisarse. Esta condicion es de bajo impacto para la Opcion A especificamente porque el badge no contiene la palabra "activa".

**Extension prohibida sin gate adicional:** Solenne y Oz no pueden extender el badge con frases de beneficio al equipo conectado ("protege tu aire acondicionado", "cuida tu electrodomestico" o similares). Cualquier extension de ese tipo requiere gate nuevo de Bruna.

**Rationale:** El badge "NTC EscudoTermico(TM)*" satisface todos los criterios del §Refresh 2026-05-06 (Criterios 1-7 de Vael): NTC visible (responde a Canudas), funcion comprensible (EscudoTermico para el consumidor), Claim H nulo, caveat compatible. El riesgo dominante es el IP marcario sobre "EscudoTermico", que Bruna no puede resolver sin verificacion SAPI VE. La aprobacion es provisional en ese eje. El riesgo funcional del claim es bajo: el RTB tecnico (NTC en circuito de potencia, mecanismo verificado por Vera y Canudas) sostiene el badge sin sobre-promesa.

**Clausula RISK-POLICY aplicada:** §3 — no afirmar datos que puedan ser falsos. El badge describe un componente real (NTC) con una funcion real (escudo termico = proteccion termica activa). No hay dato falso en el claim. El riesgo es de registro marcario, no de falsedad tecnica.

**Precedente BR-5 aplicado:** Precedente #4 — garantia de resultado rechazada sin RTB universal. Este gate confirma que el badge de funcion termica (sin promesa de proteccion de la carga) NO cae en el Precedente #4. Bruna identifica este caso como extensión del criterio de §8.5 (funcion sin componente → aquí es funcion CON componente + naming de marca): el criterio se amplía pero la lógica es la misma.

---

## §9.2 — Analisis de Opcion B: "Thermo-Safe(TM)*"

**Texto exacto para tiro:** Thermo-Safe(TM)*

**Origen:** Recomendacion Orlan OL-1 §Refresh R4 ("mejor perfil del grupo" en mapa de riesgo IP). No propuesta por Vael como badge standalone de tiro — Orlan la recomienda como bautizado primario para el empaque.

**Nota sobre el anglicismo:** la instruccion del Owner es que los anglicismos son aceptados temporalmente SIEMPRE con alternativa española o combinacion bilingue en la misma frase. "Thermo-Safe" es un anglicismo puro. Para cumplir la instruccion del Owner: el badge del tiro debe ir acompañado de alternativa española en el mismo artefacto visual (ej. subtitulo en espanol: "Proteccion Termica Activa" o equivalente). Bruna nota esta tension con la instruccion del Owner y la declara como condicion de diseno, no como causa de rechazo del claim.

### §9.2.1 — Riesgo Claim H

**Analisis:** "Thermo-Safe" es un bautizado de naming de tecnologia — no es una afirmacion funcional directa sobre lo que el protector hace. El termino "Safe" (seguro, protegido) puede evocar proteccion del equipo en una lectura rapida: "thermo" = calor + "safe" = a salvo → "a salvo del calor". Esa lectura puede activar en la Junta (40% del mercado) la interpretacion de que el equipo conectado esta protegido de sobrecalentamiento.

**Evaluacion:** El riesgo Claim H de la Opcion B es **mayor que el de la Opcion A**. La razon: "EscudoTermico" en espanol al menos es intuitivamente un escudo del protector mismo; "Thermo-Safe" en ingles, sin la funcion descripta en el badge, puede leerse como garantia de que el equipo conectado es "thermo-safe" (termicamente seguro). Este riesgo no lo activa el badge solo — lo activa la combinacion con el caveat de retiro que menciona "desconecta la carga". Un lector rapido que vea "Thermo-Safe(TM)" en el tiro y "desconecta la carga" en el retiro puede inferir que el sistema protege la carga del calor.

**Mitigacion disponible:** El cuerpo del caveat de retiro (§8.3 invariable) contiene la clausula de caveat explícita: "Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actua como proteccion de sobrecarga directa de la carga conectada." Esta clausula es la mitigacion principal. La instruccion literal a Solenne: badge solo, sin extension sobre el equipo conectado.

**Conclusion Claim H — Opcion B:** EXPONE PARCIALMENTE. El badge por si solo no activa el Claim H rechazado, pero la evocacion semantica de "Safe" (seguro) en ingles genera una tension que la Opcion A y la Opcion C no tienen en la misma medida. El caveat de retiro mitiga la sobre-promesa. El riesgo no es suficiente para rechazar, pero es superior al de la Opcion A.

### §9.2.2 — Riesgo IP marcaria

**"Thermo-Safe":** Orlan §Refresh R3 lo clasifica como el candidato con **perfil IP mas limpio del grupo**. No se encontro marca registrada en clase 9 (aparatos electricos y electronicos) en el segmento protectores de voltaje. El termino no es puramente descriptivo en espanol (es un anglicismo compuesto: "thermo" no es una palabra española de uso comun; "safe" tampoco) — esto reduce el riesgo de objecion por descriptividad ante SAPI VE.

**Evaluacion de registrabilidad:** Orlan R3 concluye: "Registrable sin riesgo aparente en el segmento protectores electricos VE, sujeto a verificacion SAPI VE formal." El riesgo descriptividad es **bajo** (el termino no describe directamente el producto en el vocabulario cotidiano del consumidor venezolano).

**Tension con instruccion Owner (anglicismo):** la instruccion del Owner de alternar anglicismo con español en el mismo artefacto visual aplica aqui. Si el badge es "Thermo-Safe(TM)" en el tiro, la alternativa española debe aparecer en el mismo empaque (retiro o subtitulo del badge). El encabezado del caveat ("Thermo-Safe(TM):") puede ir acompañado de una traduccion funcional en el cuerpo, pero el cuerpo invariable no se modifica. Bruna acepta que el encabezado en ingles satisface la instruccion del Owner si en el retiro o en el cuerpo visible del empaque aparece la descripcion en español (que ya esta en el cuerpo invariable §8.3).

**Verificacion marcaria requerida antes de imprenta:** ALTA (idem todas las opciones). Para "Thermo-Safe" la condicion suspensiva aplica igualmente, pero con menor riesgo de objecion que "EscudoTermico". La verificacion SAPI VE sigue siendo obligatoria — el perfil mas limpio no equivale a confirmacion.

### §9.2.3 — Defensa anti-copia (argumento Kike)

**Analisis:** "Thermo-Safe" como bautizado de tecnologia es un nombre propio compuesto, no un descriptor generico. Si se registra como marca en Venezuela, la defensa anti-copia es real y robusta: un competidor que copie la placa NTC no puede poner "Thermo-Safe(TM)" en su empaque si Exceline lo tiene registrado.

**Tension con el argumento de Kike:** Sin embargo, la Opcion B **no menciona NTC en el tiro**. Esto significa que:
(a) El argumento de Kike de comunicar la innovacion tecnica por nombre (NTC) no se cumple directamente — el consumidor ve "Thermo-Safe" sin saber que la tecnologia es un termistor NTC.
(b) La apertura de Canudas fue literal: "Hagan un ejemplo de comunicacion con las siglas NTC." La Opcion B no satisface ese pedido literal. Puede ser rechazada en la revision de Canudas por no mostrar las siglas.

**Blindaje real:** Alto si se registra "Thermo-Safe". La barrera de naming es real porque el termino no es descriptivo generico — un competidor no puede reclamarlo trivialmente. Pero el blindaje es sobre el nombre comercial, no sobre el argumento tecnico de NTC. Si la competencia copia la placa con NTC y lo llama de otra manera, el blindaje de naming no aplica.

**Conclusion defensa anti-copia:** La Opcion B provee el mejor blindaje de naming del trio evaluado **si el nombre se registra** — porque "Thermo-Safe" tiene el perfil IP mas limpio. Pero no provee el blindaje del argumento NTC que Kike articulo (comunicar NTC primero para que los seguidores sean seguidores, no lideres). La logica de Kike requiere NTC visible; la Opcion B no lo tiene.

### §9.2.4 — Compatibilidad con caveat tecnico (§8 Refresh 2026-05-05)

**Header del caveat para Opcion B — texto literal obligatorio:**

> Thermo-Safe(TM): [sigue el cuerpo invariable de §8.3 sin modificacion]

**Nota sobre el anglicismo en el header:** el header del retiro en ingles puede generar tension con la instruccion del Owner de preferencia española. Bruna acepta que el header en ingles es correcto porque es el badge del tiro el que determina el header del retiro (convencion establecida en §7.1 y confirmada en §8.3). El cuerpo del retiro esta en espanol — eso satisface la instruccion del Owner en el nivel del retiro.

**Compatibilidad:** PLENA. El cuerpo invariable §8.3 no menciona el nombre de la tecnologia — describe el mecanismo. "Thermo-Safe" como encabezado es compatible con ese cuerpo sin tension.

### §9.2.5 — Decision de gate: Opcion B

**Decision: APROBADO CON CAVEAT**

**Condicion 1 (riesgo Claim H — caveat de retiro):** El cuerpo del caveat de retiro §8.3 es obligatorio e invariable. Sin ese texto literal, el claim "Thermo-Safe(TM)" no se considera aprobado. El header es "Thermo-Safe(TM):" seguido del cuerpo invariable.

**Condicion 2 (instruccion Owner — anglicismo):** El badge "Thermo-Safe(TM)" debe aparecer en el empaque con alternativa española visible en el mismo artefacto (retiro, subtitulo del badge o equivalente). La alternativa en español puede ser "Proteccion Termica" o el descriptor funcional que Solenne y Oz acuerden, sujeto a gate de Bruna si el termino alternativo es un nuevo claim. El cuerpo del retiro en espanol cumple parcialmente esta condicion; Solenne debe confirmar que la instruccion del Owner se satisface con ese nivel de presencia española.

**Condicion 3 (condicion suspensiva — IP marcaria):** Verificacion SAPI VE formal antes de imprenta. Perfil mas limpio del grupo — riesgo de objecion por descriptividad bajo — pero la verificacion es igualmente obligatoria.

**Condicion 4 (condicion suspensiva — respuesta a Canudas):** La Opcion B no menciona NTC en el tiro. Si Canudas requiere ver las siglas NTC en el badge del tiro como condicion para aceptar la variante CON-NTC, la Opcion B no satisface ese pedido literal. Esta condicion no es de gate de Bruna (es una decision del Owner y Canudas), pero Bruna la declara como flag explicito para la presentacion.

**Extension prohibida sin gate adicional:** idem Opcion A. Ninguna extension sobre proteccion del equipo conectado sin gate de Bruna.

**Rationale:** El badge "Thermo-Safe(TM)*" tiene el perfil IP mas limpio del trio y la mejor base para registro formal de marca. El riesgo de Claim H es gestionable con el caveat de retiro obligatorio. La debilidad estrategica es que no menciona NTC — lo cual puede ser una fortaleza de IP (no revela componente) pero una debilidad de respuesta al pedido literal de Canudas. Bruna aprueba el claim como tal; la decision de si la Opcion B satisface el pedido de Canudas corresponde al Owner.

**Clausula RISK-POLICY aplicada:** §3 — no afirmar datos que puedan ser falsos. "Thermo-Safe" es un bautizado de naming — no afirma nada falseable directamente. La funcion que el nombre evoca (proteccion termica) es real y verificada. No hay dato falso.

---

## §9.3 — Analisis de Opcion C: "Sensor NTC ThermoSafe(TM)*"

**Texto exacto para tiro:** Sensor NTC ThermoSafe(TM)*

**Nota sobre alternativa española:** la instruccion del Owner sobre anglicismos obliga a una alternativa española en la misma frase o en el mismo artefacto. Opcion C tal como se plantea tiene el anglicismo "ThermoSafe" — la alternativa española seria: "Sensor NTC con tecnologia de Escudo Termico" (5 palabras — larga para un badge de blister con espacio ya ocupado por el badge de velocidad). Bruna acepta "Sensor NTC ThermoSafe(TM)" con la alternativa española en el cuerpo del retiro y/o como subtitulo, segun acuerde Solenne con Oz y Atlas.

**Nota sobre la denominacion:** el Owner instruyó la formulacion "Sensor NTC ThermoSafe(TM)*" como combinacion. Bruna la evalua exactamente en esos terminos, no como variante de las Opciones 3 o 6 de Vael (que son "Tecnologia NTC EscudoTermico(TM)" y "NTC EscudoTermico(TM)" respectivamente). La diferencia significativa es: (a) usa "ThermoSafe" (forma unida, sin guion) en lugar de "EscudoTermico" — esto afecta el perfil IP; (b) usa "Sensor" como descriptor explicito del componente (vs. "NTC" solo o "Tecnologia NTC"); (c) combina NTC visible con el bautizado anglicismo IP-clean de Orlan.

### §9.3.1 — Riesgo Claim H

**Analisis:** "Sensor NTC ThermoSafe(TM)" contiene tres elementos: "Sensor" (descriptor de componente tecnico), "NTC" (sigla del tipo de componente) y "ThermoSafe(TM)" (bautizado de nombre de tecnologia). Ninguno de los tres afirma proteccion del equipo conectado. "Sensor" y "NTC" son neutros respecto al Claim H. "ThermoSafe" tiene la misma tension semantica que "Thermo-Safe" (ver §9.2.1): "safe" puede evocar proteccion del equipo en una lectura rapida.

**Diferencia con Opcion B:** En la Opcion C, "ThermoSafe" va precedido de "Sensor NTC" — esto ancla semanticamente el badge al componente tecnico, reduciendo la probabilidad de que el lector infiera una promesa de proteccion del equipo. "Sensor NTC ThermoSafe(TM)*" se lee mas facilmente como "el sensor NTC que llamamos ThermoSafe" que como "el sistema que hace al equipo thermo-safe".

**Conclusion Claim H — Opcion C:** MITIGA. El anclaje de "Sensor NTC" reduce el riesgo de interpretacion de proteccion de la carga. El cuerpo del caveat de retiro sigue siendo la guardrail principal. Riesgo inferior al de la Opcion B, ligeramente superior al de la Opcion A (porque "ThermoSafe" tiene la misma evocacion semantica de "safe" que la Opcion B).

### §9.3.2 — Riesgo IP marcaria

**"ThermoSafe" (forma unida):** Orlan §Refresh R3 evaluo "Thermo-Safe" (con guion). "ThermoSafe" como forma unida sin guion tiene el mismo analisis de fondo: es un anglicismo compuesto, no un descriptor generico en espanol, con perfil de registrabilidad bajo-riesgo similar a "Thermo-Safe". La diferencia de forma grafica (guion vs. sin guion) puede tener implicaciones registrales — son denominaciones distintas ante el SAPI. Bruna trata "ThermoSafe" (sin guion) como variante con perfil IP equivalente a "Thermo-Safe" (con guion), pero Orlan debe confirmar si la forma unida tiene precedentes adicionales en base de datos de marcas antes de la busqueda SAPI VE.

**"Sensor NTC":** no es registrable como marca (descriptor tecnico de dominio publico). No genera riesgo IP adicional.

**Longitud del badge:** 3 elementos ("Sensor NTC ThermoSafe(TM)") — cuatro palabras mas el simbolo. Mas larga que la Opcion A (dos elementos) y B (uno). El espacio en el blister de la Alternativa B, donde "El mas rapido ante parpadeos (< 0,03 s)" ya ocupa espacio dominante, es una tension de diseno. Oz y Atlas deben verificar que la Opcion C cabe sin comprimir la jerarquia visual del badge de velocidad.

**Verificacion marcaria requerida antes de imprenta:** ALTA. Verificacion SAPI VE de "ThermoSafe" (forma unida) especificamente, dado que la forma con guion y la forma unida son denominaciones distintas. La condicion suspensiva de produccion es identica a las Opciones A y B.

### §9.3.3 — Defensa anti-copia (argumento Kike)

**Analisis:** La Opcion C combina la logica de ambas opciones anteriores:
- NTC visible en el tiro: activa directamente el argumento de Kike ("Exceline comunica NTC primero, los que lo copian son seguidores").
- "ThermoSafe(TM)" como bautizado registrable: si se registra, el competidor que copie la placa no puede usar el nombre comercial de la tecnologia.

**Doble capa de defensa:** La Opcion C ofrece la defensa mas completa del trio: (1) pionerismo en comunicacion de NTC (argumentativo — depende de la velocidad del lanzamiento de Exceline) + (2) blindaje de naming registrado (marcario — depende del registro SAPI VE).

**Limitacion compartida con Opcion B:** La defensa de naming requiere registro. Sin registro, "ThermoSafe" es tan copiable como cualquier descriptor. La barrera es el registro.

**Limitacion adicional vs. Opcion A:** Si "EscudoTermico" es registrable (pese al riesgo de descriptividad), el nombre en espanol tiene mayor resonancia local para el consumidor venezolano que "ThermoSafe" en ingles. La defensa anti-copia de naming no es mas fuerte en la Opcion C que en la Opcion A en terminos de impacto de mercado — si bien el perfil IP de "ThermoSafe" es mas limpio.

**Conclusion defensa anti-copia:** Alta potencial — la mas alta del trio si se registra "ThermoSafe" + NTC se comunica antes que la competencia. En la practica, requiere cumplir ambas condiciones simultaneamente.

### §9.3.4 — Compatibilidad con caveat tecnico (§8 Refresh 2026-05-05)

**Header del caveat para Opcion C — texto literal obligatorio:**

> Sensor NTC ThermoSafe(TM): [sigue el cuerpo invariable de §8.3 sin modificacion]

**Compatibilidad:** PLENA. El cuerpo invariable de §8.3 describe el mecanismo del sensor sin mencionar el nombre comercial — es compatible con cualquier bautizado de la funcion en el encabezado.

**Nota sobre la Condicion Suspensiva Vera P-5:** La Opcion C usa "Sensor NTC" — no usa el adjetivo "activa" de la v2.1. La condicion suspensiva de P-5 (si el NTC es fusible de corte unico, retirar "activa") no afecta directamente el badge de la Opcion C. Sin embargo, si P-5 confirma que el NTC es fusible de corte unico, la descripcion del cuerpo del retiro ("detecta calentamiento excesivo... y desconecta la carga") podria merecer una revision de redaccion para reflejar que la actuacion es unica (no recurrente). Bruna mantiene la condicion P-5 como dependencia de bajo impacto para la Opcion C, pero no como condicion bloqueante del gate conceptual.

### §9.3.5 — Decision de gate: Opcion C

**Decision: APROBADO CON CAVEAT**

**Condicion 1 (caveat de retiro):** El header del retiro es "Sensor NTC ThermoSafe(TM):" seguido del cuerpo invariable de §8.3. Sin ese texto, el claim del tiro no se considera aprobado.

**Condicion 2 (instruccion Owner — anglicismo):** El badge incluye el anglicismo "ThermoSafe". La alternativa española debe aparecer en el empaque. La alternativa recomendada por Bruna para el retiro o subtitulo es: "Proteccion termica activa" o "tecnologia de escudo termico" — sujeta a decision de Solenne y Owner. El cuerpo del retiro en español ya provee contexto en espanol.

**Condicion 3 (condicion suspensiva — IP marcaria "ThermoSafe" forma unida):** Verificacion SAPI VE de "ThermoSafe" (sin guion) antes de imprenta. Orlan debe confirmar si la forma unida tiene analisis de registrabilidad diferente a la forma con guion evaluada en §Refresh.

**Condicion 4 (condicion suspensiva — espacio de diseno):** Oz y Atlas deben confirmar que "Sensor NTC ThermoSafe(TM)*" cabe en el blister de la Alternativa B sin comprimir el badge de velocidad "El mas rapido ante parpadeos (< 0,03 s)". Si no cabe: la Opcion C debe acortarse (ej. eliminar "Sensor" y usar "NTC ThermoSafe(TM)*") o descartarse en favor de la Opcion A o B. El gate conceptual es valido; la condicion de espacio es operativa.

**Extension prohibida sin gate adicional:** idem Opciones A y B.

**Rationale:** "Sensor NTC ThermoSafe(TM)*" es la opcion que mas directamente responde al pedido literal de Canudas ("siglas NTC" visibles) combinando el argumento de Kike (NTC comunicado primero) con el perfil IP mas limpio del bautizado (ThermoSafe / Thermo-Safe — recomendado por Orlan). La sintesis es logicamente coherente. El costo es la longitud del badge (tension de diseno) y la doble condicion suspensiva (SAPI VE + espacio). El riesgo de Claim H es el mas bajo del trio gracias al anclaje semantico de "Sensor NTC" que contextualiza correctamente el "ThermoSafe" como nombre del componente, no como promesa de resultado.

**Clausula RISK-POLICY aplicada:** §3 — no afirmar datos que puedan ser falsos. "Sensor NTC ThermoSafe(TM)" describe: (1) un componente real (Sensor NTC — verificado por Vera y Canudas), (2) un nombre comercial (ThermoSafe — aspiracional, no falso). No hay dato factual falseable.

---

## §9.4 — Tabla comparativa final: Opciones A, B, C

| Eje de evaluacion | Opcion A: "NTC EscudoTermico(TM)*" | Opcion B: "Thermo-Safe(TM)*" | Opcion C: "Sensor NTC ThermoSafe(TM)*" |
|---|---|---|---|
| **Riesgo Claim H** | Bajo — badge no evoca proteccion de la carga. Caveat §8.3 mitiga. | Medio-bajo — "Safe" puede evocar proteccion del equipo en lectura rapida. Caveat §8.3 mitiga. | Bajo — "Sensor NTC" ancla semanticamente el badge al componente. Caveat §8.3 mitiga. |
| **Riesgo IP marcaria** | Medio-alto — "EscudoTermico" es descriptor generico en español; riesgo objecion SAPI por descriptividad. | Bajo — "Thermo-Safe" perfil mas limpio del grupo; termino no descriptivo en español. | Bajo — "ThermoSafe" (forma unida) perfil equivalente a "Thermo-Safe"; necesita confirmacion Orlan sobre variante sin guion. |
| **Defensa anti-copia** | Alta SI se registra "EscudoTermico". Condicional al registro. Sin registro: media (igual a Op. 1 Vael). | Alta SI se registra "Thermo-Safe". No comunica NTC — debilita argumento Kike de pionerismo de NTC. | Alta SI se registra "ThermoSafe" + NTC se lanza antes que competencia. Doble capa: naming + pionerismo NTC. |
| **Responde pedido Canudas (NTC visible)** | Si — NTC en el tiro. | No — NTC no aparece en el badge del tiro. Flag critico para aprobacion de Canudas. | Si — NTC en el tiro ("Sensor NTC"). Respuesta mas explicita del trio. |
| **Compatibilidad caveat §8** | Plena. Header: "NTC EscudoTermico(TM):" | Plena. Header: "Thermo-Safe(TM):" | Plena. Header: "Sensor NTC ThermoSafe(TM):" |
| **Longitud badge** | Compacta (2 elementos). Menor riesgo de tension de diseno. | La mas compacta (1 elemento). Sin problema de espacio. | 3 elementos (4 palabras + simbolo). Mayor riesgo de tension de diseno en el blister. |
| **Cumple instruccion anglicismo Owner** | Si — "EscudoTermico" es español. | No directamente — "Thermo-Safe" es anglicismo. Requiere alternativa española visible en el empaque. | No directamente — "ThermoSafe" es anglicismo. Requiere alternativa española visible. |
| **Decision BR-2** | APROBADO CON CAVEAT | APROBADO CON CAVEAT | APROBADO CON CAVEAT |

---

## §9.5 — Recomendacion final desde optica de riesgo combinado

**Menor riesgo combinado (legal + reputacional + tecnico): Opcion B — "Thermo-Safe(TM)*"**

La Opcion B acumula el menor riesgo combinado porque:
1. Riesgo IP marcaria: el mas bajo del trio — "Thermo-Safe" tiene el perfil mas limpio de registrabilidad segun Orlan §Refresh R3/R4. Ninguna señal de conflicto en clase 9.
2. Riesgo Claim H: gestionable con el caveat de retiro obligatorio.
3. Sin riesgo de rechazo SAPI VE por descriptividad (a diferencia de "EscudoTermico").
4. Sin riesgo de tension de diseno (badge mas compacto del trio).

**Debilidad critica de la Opcion B:** No satisface el pedido literal de Canudas de ver "las siglas NTC". Esta debilidad es estrategica, no de riesgo de claims. La decision de si presentar la Opcion B a pesar de ese flag corresponde al Owner. Bruna no puede subsanar esa debilidad; solo puede declararla.

**Mayor riesgo combinado: Opcion A — "NTC EscudoTermico(TM)*"**

El mayor riesgo individual en el trio es el riesgo IP de "EscudoTermico" como termino potencialmente no registrable por descriptividad en SAPI VE (Orlan §Refresh R3: riesgo medio-alto). Si SAPI VE objeta el termino, el simbolo (TM) en el empaque ya impreso queda sin respaldo formal, y la barrera anti-copia que justifica la eleccion del naming se vuelve inexistente. La Opcion A es la que mas depende del resultado de la verificacion SAPI VE para cumplir su proposicion de valor (blindaje de naming).

**Posicion de la Opcion C:** la Opcion C ("Sensor NTC ThermoSafe(TM)*") tiene el perfil de riesgo mas equilibrado en los ejes de claim (Claim H: bajo, mejor del trio gracias al anclaje "Sensor NTC") y el perfil IP mas limpio del grupo excepto por la tension de diseno (4 palabras). Es la opcion que mejor responde al brief del Owner (NTC visible + bautizado IP-clean + bilingue en misma frase) si el espacio del blister lo permite.

**Declaracion obligatoria de Bruna (rol de Risk & Claims Governance Lead):** Esta recomendacion es desde la optica exclusiva de riesgo de claims y riesgo legal de naming. No es una recomendacion estrategica general sobre la variante v2.2 ni sobre cual opcion tiene mayor potencial comercial o cual convencer mejor a Canudas. Esas dimensiones corresponden al Owner y a Kike. Bruna puede pronunciarse sobre el riesgo; la decision final es del Owner.

---

## §9.6 — Clausulas condicionales antes de produccion de imprenta

Las condiciones que siguen aplican a TODAS las opciones gateadas en este §9. Ninguna de las tres opciones puede pasar a produccion de imprenta hasta que las condiciones marcadas como obligatorias esten resueltas.

### Condicion 1 — Vera P-5 (mecanismo NTC continuo vs fusible unico)

**Estado:** Pendiente. Flag abierto desde §8.1 (Refresh 2026-05-05).

**Impacto por opcion:**
- Opcion A: impacto bajo. "NTC EscudoTermico(TM)" no usa el adjetivo "activa". Si P-5 confirma fusible de corte unico, la descripcion del cuerpo del retiro puede necesitar ajuste menor para reflejar que la actuacion es unica ("detecta... y desconecta" → "detecta... y desconecta permanentemente hasta reemplazo del protector" o equivalente). No bloquea el badge del tiro.
- Opcion B: impacto bajo. "Thermo-Safe(TM)" no implica continuidad o actuacion recurrente. El cuerpo del retiro es el mismo analisis que la Opcion A.
- Opcion C: impacto bajo con la misma salvedad que A. "Sensor NTC" como descriptor no implica continuidad. El riesgo de P-5 es menor en las opciones CON-NTC que en la v2.1 (que usaba "activa").

**Conclusion:** La Condicion Vera P-5 es de impacto bajo para todas las opciones B-CON-NTC de este §9. No es condicion bloqueante del gate conceptual ni de la presentacion a Kike/Canudas. Es condicion de revision menor antes de imprenta.

### Condicion 2 — SAPI VE verificacion formal del bautizado finalista

**Estado:** Pendiente. Ninguna de las tres opciones tiene verificacion formal SAPI VE.

**Condicion suspensiva de produccion de imprenta (obligatoria para todas las opciones):** El bautizado finalista que el Owner elija (sea "EscudoTermico", "Thermo-Safe" / "ThermoSafe", o cualquier variante) debe pasar por verificacion SAPI VE con abogado marcario antes de que se produzca el arte final para imprenta. Orlan es claro (§Refresh R3): "El bautizado SIN verificacion SAPI VE es defendible unicamente como provisional. Imprimir empaque con bautizado no verificado expone a Genteca a: (a) oposicion de tercero, (b) invalidacion de marca despues de inversion en empaque, (c) costo de reimpresion."

**Jerarquia de riesgo por opcion:**
- Opcion B ("Thermo-Safe"): menor riesgo de objecion — prioridad de verificacion si es el finalista elegido.
- Opcion C ("ThermoSafe" forma unida): riesgo similar a B; Orlan debe confirmar que la forma unida no genera diferencias de registrabilidad respecto a la forma con guion.
- Opcion A ("EscudoTermico"): mayor riesgo de objecion por descriptividad — requiere opinion de abogado marcario sobre estrategia para defender la marca ante posible objecion SAPI.

**Responsable:** Owner (decision de contratar abogado marcario) + Orlan (research preliminar de apoyo).

### Condicion 3 — Confirmacion de espacio de diseno (especifica para Opcion C)

**Estado:** Pendiente para la Opcion C.

La Opcion C ("Sensor NTC ThermoSafe(TM)*") tiene 4 palabras mas el simbolo. Atlas y Oz deben confirmar que el badge cabe en el blister de la Alternativa B sin comprimir la jerarquia visual del badge de velocidad "El mas rapido ante parpadeos (< 0,03 s)". Si no cabe: la Opcion C debe acortarse (retirando "Sensor" o ajustando la formulacion) o descartarse.

**Responsable:** Owner + Atlas + Oz (mockup real).

### Condicion 4 — Alternativa española visible en el empaque (para Opciones B y C)

**Estado:** Pendiente de decision de diseno.

Las Opciones B ("Thermo-Safe") y C ("Sensor NTC ThermoSafe") incluyen anglicismos. La instruccion del Owner es que los anglicismos van acompañados de alternativa española o combinacion bilingue en el mismo artefacto. Solenne debe confirmar con el Owner como se implementa esta instruccion en el artefacto final (subtitulo del badge, nota en el retiro, o cuerpo del retiro como contexto en español ya existente).

**Responsable:** Solenne (propuesta de implementacion) + Owner (decision).

---

## §9.7 — Notificaciones de cascada post-gate §9

**Para el Owner (presentacion a Kike):**
- Las tres opciones tienen gate de Bruna: APROBADO CON CAVEAT.
- El flag critico para la presentacion: la Opcion B no menciona NTC en el tiro — Canudas puede rechazarla si el pedido literal ("siglas NTC") es condicion. Declarar ese flag a Kike para que decida si incluir la Opcion B en el set que presenta.
- El flag de menor riesgo IP combinado: Opcion B.
- El flag de mayor respuesta al brief de Canudas: Opcion C (NTC visible + bautizado IP-clean).
- Las condiciones suspensivas de PRODUCCION DE IMPRENTA (SAPI VE, Vera P-5, espacio de diseno) no bloquean la presentacion a Kike. Son condiciones de produccion, no de decision estrategica.

**Para Vael (informacion):**
- Las Opciones A y C del gate corresponden a las Opciones 6 y una sintesis nueva del §Refresh 2026-05-06. La Opcion B del gate es la recomendacion Orlan que no tenia ranking explicit en Vael.
- Si el Owner elige la Opcion C ("Sensor NTC ThermoSafe(TM)*"), Vael debe confirmar si la formulacion encaja en la arquitectura de mensaje de VA-1 Pilar 3 sin tension conceptual.

**Para Solenne (SO-1 delta, cuando Owner decida):**
- No actuar hasta que Owner seleccione la opcion y la Decision de Canudas sea favorable.
- Los tres cuerpos del caveat de retiro son identicos (§8.3 invariable). Solo cambian los headers. Solenne prepara el texto del retiro con el header correspondiente a la opcion seleccionada.

**Para Oz (redline arte):**
- No actuar hasta confirmacion de Owner.
- El asterisco en el tiro es obligatorio para las tres opciones.
- El texto del retiro usa el encabezado de la opcion seleccionada + el cuerpo invariable de §8.4.

**Para Vera (pendiente):**
- Condicion P-5 sigue abierta. El impacto en las opciones B-CON-NTC es bajo, pero la confirmacion antes de imprenta sigue siendo requerida para cerrar el ciclo del §8.

---

## §9.8 — BR-2 Genteca — Entrada de gate §9

**Dominio:** Genteca
**Proyecto:** 2026-04_GSM-MB-RB-RF_empaque
**Fecha de decision:** 2026-05-06
**Documento de gate:** Bruna_gate_empaque_v1 §9

| Opcion gateada | Texto exacto del tiro | Decision | Condicion principal | Clausula RISK-POLICY | Precedente BR-5 |
|---|---|---|---|---|---|
| Opcion A — "NTC EscudoTermico(TM)*" | NTC EscudoTermico(TM)* | APROBADO CON CAVEAT | Caveat retiro §8.3 obligatorio; SAPI VE "EscudoTermico" antes de imprenta; sin extension sobre equipo conectado | §3 — no afirmar datos falseables | Criterio §8.5 (funcion con componente + naming marca) — aplicado |
| Opcion B — "Thermo-Safe(TM)*" | Thermo-Safe(TM)* | APROBADO CON CAVEAT | Caveat retiro §8.3 obligatorio; alternativa española visible en empaque; SAPI VE "Thermo-Safe" antes de imprenta; NTC no visible — flag para Canudas | §3 | Sin precedente especifico — nuevo en BR-5 candidato |
| Opcion C — "Sensor NTC ThermoSafe(TM)*" | Sensor NTC ThermoSafe(TM)* | APROBADO CON CAVEAT | Caveat retiro §8.3 obligatorio; SAPI VE "ThermoSafe" (forma unida) antes de imprenta; confirmacion espacio de diseno Atlas/Oz; alternativa española visible | §3 | Criterio §8.5 ampliado — NTC + naming bilingue |

**Evidencia consultada para este gate:**
- Vael_VA-5_naming-funcion-termica_v1.md §Refresh 2026-05-06 (ranking, textos de retiro, criterios reformulados)
- Orlan_OL-1_competencia-naming-termico_v1.md §Refresh 2026-05-06 (vacancia territorial, IP nominal, analisis copia china, recomendacion "Thermo-Safe")
- Bruna_gate_empaque_v1 §2 Claim H (rechazo sin alternativa — referencia de frontera); §7.1 (bloque NTC corregido); §8.3/§8.4 (caveat invariable de retiro)
- BR-5 transversal Precedentes #1, #2, #4 (criterios de superlativos, exclusion, garantia de resultado)
- RISK-POLICY.md v1.0 §3

---

## §9.9 — Candidato a Precedente BR-5 (append pendiente de confirmacion Owner)

**Nuevo criterio identificado:** Gate de naming de tecnologia con componente tecnico visible (NTC) + bautizado comercial registrable en mercado con opacidad competitiva alta.

**Criterio propuesto:**

Cuando un claim de empaque bautiza una tecnologia interna (ej. "EscudoTermico(TM)", "ThermoSafe(TM)") combinando el nombre del componente tecnico (NTC) con un nombre comercial registrable, el gate de Bruna evalua dos ejes independientes:
1. **Eje de claim funcional:** el claim describe una funcion real verificable? (Vera). Si si: aprobable con caveat. El hecho de revelar el componente (NTC) es una decision estrategica del Owner, no una cuestion de veracidad del claim.
2. **Eje de IP nominal:** el bautizado elegido es registrable como marca? (Orlan — SAPI VE formal). Este eje no bloquea el gate conceptual pero si bloquea la produccion de imprenta.

Estos dos ejes son independientes: un claim puede ser factualmente correcto (eje 1 OK) pero tener riesgo de IP marcaria (eje 2 pendiente). El gate conceptual se emite sobre el eje 1; la condicion suspensiva de produccion se emite sobre el eje 2. Solenne y Oz no deben esperar la resolucion del eje 2 para preparar mockups y argumentario, pero si para producir el arte final de imprenta.

**Scope de aplicacion:** cualquier dominio de /RAUL/ donde un claim de empaque o marketing bautice una funcion tecnica con un nombre comercial que incluya el nombre o siglas del componente que la implementa.

**Estado:** candidato — Bruna lo eleva al Owner para decision de formalizacion en BR-5 transversal. El append a BR-5 se ejecuta cuando el Owner confirme que la experiencia de este gate vale como criterio generalizable.

---

*Gate emitido: 2026-05-06*
*Estado de las 3 opciones: APROBADO CON CAVEAT (condiciones de produccion declaradas en §9.6)*
*Proxima accion requerida: Owner selecciona opcion para presentacion a Kike. Condiciones de produccion (SAPI VE, Vera P-5, espacio diseno) se resuelven solo si Canudas / Kike dan luz verde a la variante B-CON-NTC.*

---

# §10 — Gate final variante B-CON-NTC (decision Kike 2026-05-06)

**Tipo de gate:** mini-gate de cierre post-decision directiva. No es gate completo — es confirmar que la variante finalista instruida por Kike (Alberto Betancourt, Direccion General) es compatible con los gates anteriores y senalar las condiciones que subsisten.

**Inputs de este gate:**
- Decision verbal de Kike 2026-05-06: naming finalista "Escudo Termico NTC*" (funcion primero, componente como sufijo identificador)
- Kike autoriza flexibilidad en el cuerpo del caveat ("puede hablar de NTC o de Escudo")
- Estrategia Kike: presentar a Canudas en paralelo B-sin-NTC v2.1 ("Autoproteccion termica activa*") y B-CON-NTC v2.2 ("Escudo Termico NTC*")
- Orlan Refresh 2026-05-06 sobre riesgo IP de "Escudo Termico" en dos palabras separadas

---

## §10.1 — Gate del header del badge (tiro)

**Texto a gatear:** `Escudo Termico NTC*`

**Decision: APROBADO CON CAVEAT**

**Categoria:** ✅ con condiciones suspensivas heredadas (idem §9.1.5, con una diferencia de orden gramatical evaluada abajo)

### Coherencia con gate §9 Opcion A

El §9 gateo "NTC EscudoTermico(TM)*" (componente primero, nombre comercial despues). La variante instruida por Kike invierte el orden: "Escudo Termico NTC*" (funcion primero, componente como sufijo identificador).

**Evaluacion de la inversion de orden:** no requiere analisis nuevo de fondo. El riesgo de Claim H no lo determina el orden de los elementos sino la presencia de los mismos. "Escudo Termico NTC" contiene los mismos elementos semanticos que "NTC EscudoTermico": el descriptor funcional (Escudo Termico = funcion de proteccion termica) y el componente tecnico (NTC). La inversion beneficia la lectura funcional — el consumidor ve primero la funcion y despues la tecnologia que la implementa. Esto no abre interpretaciones de proteccion de la carga conectada que el badge en §9.1.1 no tuviera.

**Diferencia grafica relevante:** Kike usa "Escudo Termico" en dos palabras separadas (no "EscudoTermico" unido). Esto es congruente con la advertencia de Orlan Refresh 2026-05-06: en dos palabras separadas el termino es aun mas descriptivo que en forma unida. El impacto es exclusivamente en el eje IP marcario (ver §10.2 sobre simbolo TM), no en el eje de veracidad del claim ni en el riesgo de Claim H.

### Riesgo Claim H

El badge "Escudo Termico NTC*" no promete proteccion del equipo conectado. "Escudo Termico" describe la funcion del protector (protege el cableado y al protector mismo del calor excesivo). "NTC" identifica el componente que implementa esa funcion. Ninguno de los dos elementos afirma que la carga conectada esta protegida de sobrecarga o de dano termico.

**Conclusion Claim H:** MITIGA. Identico al analisis de §9.1.1. El cuerpo del caveat de retiro (§8.3 invariable) opera como guardrail obligatorio. Extension prohibida: ninguna frase derivada del badge puede afirmar que "protege el equipo conectado" sin gate adicional de Bruna.

### Compatibilidad con caveat tecnico (§8.3 invariable)

**Plena.** El cuerpo invariable de §8.3 ("sensor de temperatura ubicado junto al rele de potencia. Detecta calentamiento excesivo...") no menciona el nombre comercial de la funcion — describe el mecanismo. Es compatible con cualquier header de naming, incluido "Escudo Termico NTC:".

**Header del caveat de retiro para v2.2 — texto literal obligatorio:**

> Escudo Termico NTC: sensor de temperatura ubicado junto al rele de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se danen. Protege al protector mismo y a la instalacion electrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actua como proteccion de sobrecarga directa de la carga conectada. Funciona como capa adicional de proteccion termica; no reemplaza al interruptor termomagnetico de la instalacion.

---

## §10.2 — Decision sobre simbolo TM

**Input:** Kike no menciono TM en su decision. Orlan Refresh 2026-05-06 advierte: "Escudo Termico" en dos palabras separadas tiene riesgo medio-alto de no registrabilidad SAPI VE por descriptividad.

**Decision de Bruna:** SIN TM en la formulacion final de v2.2 hasta verificacion SAPI VE favorable.

**Argumento:**

El simbolo TM (trademark no registrada) no genera proteccion juridica formal en Venezuela — SAPI VE requiere registro efectivo para esa proteccion. Lo que TM si genera es una representacion publica de que el titular considera el termino como marca propia. Si "Escudo Termico" en dos palabras es objetado por SAPI VE como descriptor generico (riesgo medio-alto segun Orlan), imprimir el empaque con TM:

1. Crea una representacion que puede ser falsa si el termino no es registrable.
2. No tiene valor defensivo ante un competidor que alegue genericidad.
3. Puede ser usada en contra en un proceso de oposicion ("el titular mismo senala que considera esto una marca, pero el termino es descriptor comun").

La "NTC" como sufijo no cambia el analisis: "Escudo Termico NTC" es "Escudo Termico" mas las siglas del componente — SAPI VE evaluara el conjunto y "Escudo Termico" seguira siendo el nucleo potencialmente objetable.

**Recomendacion:**
- Formulacion de tiro sin simbolo: `Escudo Termico NTC*` (asterisco obligatorio, que remite al caveat del retiro)
- Formulacion del header de retiro sin TM: `Escudo Termico NTC:` seguido del cuerpo invariable
- El simbolo TM se incorpora solo si SAPI VE emite opinion favorable (busqueda formal + abogado marcario confirma posicion defensible)

**Si el Owner discrepa y decide incluir TM:** Bruna acepta pero declara el riesgo como flag explicito en BR-2. La decision final es del Owner — Bruna no puede rechazar el uso de TM como claim falso (no lo es — es una representacion de intencion marcaria), pero si puede y debe documentar el riesgo IP.

**Clausula RISK-POLICY aplicada:** §4 Reversibilidad — el empaque impreso con TM sobre un termino eventualmente objetado por SAPI VE genera un costo de correccion irreversible. Antes de imprenta, la decision sobre TM debe tomarse con base en verificacion SAPI VE.

---

## §10.3 — Cuerpo del caveat tecnico: version recomendada

Kike autorizo flexibilidad en el cuerpo del caveat ("puede hablar de NTC o de Escudo"). El cuerpo invariable de §8.3 usa el descriptor neutro "sensor de temperatura" — no menciona ni "NTC" ni "Escudo" en el cuerpo. Eso ya es la decision correcta: el header lleva el nombre comercial; el cuerpo describe el mecanismo.

La flexibilidad de Kike aplica al **header del caveat**, no al cuerpo. El cuerpo de §8.3 ya es invariable por decision de gate anterior. Bruna confirma que no es necesario ni conveniente reabrir el cuerpo.

**Evaluacion de las tres versiones propuestas:**

**Version NTC explicita:**
> Escudo Termico NTC: sensor NTC ubicado junto al rele de potencia. Detecta calentamiento excesivo...

Introduce "sensor NTC" en el cuerpo, donde antes decia "sensor de temperatura". El cambio es tecnicamente mas preciso (el sensor es un termistor NTC, no un sensor generico de temperatura) pero introduce el nombre del componente en el cuerpo del caveat. El riesgo: si en un futuro el protector cambia el componente interno (ej. sustitucion de NTC por termopar), el cuerpo del caveat queda desactualizado. Ademas, la mencion explicita de "NTC" en el cuerpo puede crear confusion si el consumidor no conoce la sigla — el cuerpo esta disenado para ser explicativo, no tecnico.

**Version metaforica:**
> Escudo Termico NTC: sistema de Escudo Termico (sensor NTC) ubicado junto al rele de potencia. Detecta calentamiento excesivo...

Introduce tanto "Escudo Termico" como "NTC" en el cuerpo. Esto crea redundancia (el header ya dice "Escudo Termico NTC") y hace el cuerpo mas largo sin agregar informacion nueva. Desde optica de claims, la frase parentetica "(sensor NTC)" en el cuerpo es una autoexplicacion del naming que puede confundir en lugar de clarificar.

**Version cuerpo invariable (la actual de §8.3, sin cambio):**
> Escudo Termico NTC: sensor de temperatura ubicado junto al rele de potencia. Detecta calentamiento excesivo...

El header identifica la funcion y el componente. El cuerpo describe el mecanismo en lenguaje funcional claro, sin comprometer el texto a la sigla del componente especifico ni a la metafora del naming. Esta es la version que mejor soportaria una disputa: el header es el nombre comercial, el cuerpo es la descripcion funcional verificable, y ninguno de los dos se contradice ni hace promesas que el otro no pueda sostener.

**Recomendacion de Bruna: VERSION CUERPO INVARIABLE (§8.3 sin cambio).**

El argumento decisivo: el cuerpo del caveat es la pieza que se lee en una disputa. Cuanto mas neutro y verificable sea el lenguaje del cuerpo, mas fuerte es la posicion de Exceline. Introducir "NTC" o "Escudo" en el cuerpo no agrega valor defensivo — solo agrega especificidad que puede generar nuevas preguntas tecnicas (ej. "si dice sensor NTC, y el NTC es un fusible de corte unico, la descripcion de 'detecta' implica deteccion continua?"). El cuerpo invariable ya paso el gate de §8; no hay razon para reabrirlo.

**Nota operativa:** la flexibilidad de Kike queda satisfecha con el header. El header dice "Escudo Termico NTC:" — menciona ambos elementos (Escudo y NTC). El cuerpo describe el mecanismo sin redundar.

---

## §10.4 — Lista de claims aprobados: variante B-CON-NTC v2.2

| Claim | Texto exacto | Decision BR-2 | Condicion principal |
|---|---|---|---|
| Badge tiro (funcion termica) | Escudo Termico NTC* | APROBADO CON CAVEAT | Caveat de retiro §10.3 obligatorio; sin TM hasta SAPI VE; sin extension sobre equipo conectado |
| Bullet retiro CARACTERISTICAS (header) | Escudo Termico NTC: | APROBADO CON CAVEAT | Header del bullet sigue al tiro — si el tiro cambia, el header cambia en consecuencia |
| Caveat de retiro (cuerpo completo) | [cuerpo invariable §8.3 — reproducido literalmente en §10.1] | APROBADO — invariable | Sin modificacion del cuerpo; solo el header cambia entre variantes |
| Claims heredados de v2 sin cambio: badge velocidad | El mas rapido ante parpadeos (< 0,03 s)* | Heredado — aprobacion previa vigente | Sin modificacion |
| Claims heredados: inverter | Apto para cargas Inverter | Heredado — aprobacion previa vigente | Sin modificacion |
| Claims heredados: lengüeta | [formulacion aprobada en gate anterior] | Heredado — aprobacion previa vigente | Sin modificacion |
| Disclaimer breakers | [formulacion aprobada en gate anterior] | Heredado — aprobacion previa vigente | Sin modificacion |

**Nota sobre herencia de claims:** todos los claims de v2 aprobados antes del §8 Refresh permanecen vigentes sin modificacion. El unico claim nuevo en v2.2 es el badge del tiro de funcion termica y su caveat de retiro. La v2.2 no abre ningun otro claim al cambio.

---

## §10.5 — Condiciones suspensivas vigentes para v2.2 imprenta

### Condicion 1 — Vera P-5 (mecanismo NTC continuo vs fusible unico)

**Estado:** Pendiente. Heredada de §8.1 y confirmada en §9.6.

**Impacto en v2.2:** bajo. "Escudo Termico NTC" no usa el adjetivo "activa" — el adjetivo que generaba la expectativa de continuidad fue descartado en la formulacion de Kike. Por tanto, si Vera confirma que el NTC es fusible de corte unico, el badge "Escudo Termico NTC*" no requiere cambio. Solo puede requerirse ajuste menor en el cuerpo del retiro (ej. aclarar que la actuacion es unica, no recurrente — pero el cuerpo invariable actual no promete recurrencia, por lo que el impacto es minimo).

**Conclusion:** Condicion de revision pre-imprenta, no condicion bloqueante del gate conceptual ni de la presentacion a Canudas.

### Condicion 2 — SAPI VE verificacion formal de "Escudo Termico NTC"

**Estado:** Pendiente. Obligatoria antes de produccion de arte final para imprenta.

**Especificidad para v2.2:** "Escudo Termico" en dos palabras separadas tiene riesgo de descriptividad medio-alto (Orlan Refresh 2026-05-06). El sufijo "NTC" podria agregar distintividad al conjunto — un argumento ante SAPI VE seria que "Escudo Termico NTC" como denominacion completa no es descriptiva de ningun producto en el mercado venezolano. Este argumento requiere evaluacion de abogado marcario: Bruna no puede pronunciarse sobre estrategia de registro sin esa opinion.

**Requiere abogado marcario:** SI. El riesgo de descriptividad es lo suficientemente elevado en el nucleo ("Escudo Termico") como para que la verificacion no sea solo una busqueda de base de datos (Orlan) sino una opinion sobre registrabilidad de un termino potencialmente descriptivo (abogado marcario). La decision de contratar ese abogado es del Owner.

**Sin SAPI VE favorable:** sin TM en el empaque (ver §10.2). La imprenta puede proceder sin TM si el Owner acepta ese riesgo. No puede proceder con TM sin verificacion.

### Condicion 3 — Decision de Canudas

**Estado:** Pendiente. Esta es la condicion de negocio que determina si v2.2 llega a imprenta.

Kike presentara a Canudas en paralelo:
- Variante 1: B-sin-NTC v2.1 ("Autoproteccion termica activa*") — ya gateada por Bruna en §8
- Variante 2: B-CON-NTC v2.2 ("Escudo Termico NTC*") — gateada en este §10

Hasta la decision de Canudas, ninguna de las dos variantes pasa a produccion de arte final. El gate de Bruna sobre v2.2 es una condicion necesaria pero no suficiente para la imprenta.

---

## §10.6 — Nota para Solenne y Atlas

**Texto exacto del badge tiro:**

`Escudo Termico NTC*`

(Sin TM. Con asterisco obligatorio. El asterisco remite al caveat del retiro.)

**Texto exacto del header del bullet retiro CARACTERISTICAS:**

`Escudo Termico NTC:`

(Sin TM. El header precede al cuerpo invariable. No modificar ni el header ni el cuerpo una vez integrados.)

**Texto exacto del caveat de retiro (cuerpo completo — palabra por palabra):**

> Escudo Termico NTC: sensor de temperatura ubicado junto al rele de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se danen. Protege al protector mismo y a la instalacion electrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actua como proteccion de sobrecarga directa de la carga conectada. Funciona como capa adicional de proteccion termica; no reemplaza al interruptor termomagnetico de la instalacion.

**Instruccion sobre TM:** NO incluir TM en ninguna pieza de v2.2 (tiro, retiro, cualquier artefacto) hasta que SAPI VE emita verificacion favorable y el Owner decida incorporarlo. Si el Owner instruye explicitamente incluir TM antes de esa verificacion, solicitar confirmacion escrita del Owner y documentar el flag de riesgo IP en este gate.

**Instruccion sobre el cuerpo del caveat:** NO modificar el cuerpo del caveat bajo ninguna circunstancia sin gate adicional de Bruna. La flexibilidad que Kike menciono aplica al header (nombre comercial elegido), no al cuerpo del mecanismo. El cuerpo es invariable.

**Limites de uso:** el claim "Escudo Termico NTC*" aplica exclusivamente al badge del tiro de la Alternativa B blister GSM. No extender a otros artefactos de marketing (landing page, redes, catalogo) sin gate de Bruna para ese artefacto especifico.

---

## §10.7 — BR-2 Genteca — Entrada de gate §10

**Dominio:** Genteca
**Proyecto:** 2026-04_GSM-MB-RB-RF_empaque
**Fecha de decision:** 2026-05-06
**Documento de gate:** Bruna_gate_empaque_v1 §10
**Gatekeeping trigger:** decision de Kike (Alberto Betancourt, Direccion General) de adoptar "Escudo Termico NTC*" como naming finalista de la variante B-CON-NTC v2.2

| Claim gateado | Texto exacto | Decision | Condicion principal | Clausula RISK-POLICY | Precedente §9 |
|---|---|---|---|---|---|
| Badge tiro v2.2 | Escudo Termico NTC* | APROBADO CON CAVEAT | Caveat retiro §10.1 obligatorio; sin TM hasta SAPI VE; Canudas debe aprobar variante antes de imprenta | §3 — no afirmar datos falseables; §4 — reversibilidad antes de imprenta | §9.1.5 — coherente; inversion de orden no cambia perfil de riesgo |
| Simbolo TM | — (suspendido) | SUSPENDIDO hasta SAPI VE | Riesgo descriptividad medio-alto en "Escudo Termico" (Orlan Refresh 2026-05-06); abogado marcario requerido | §4 | §9.1.2 — riesgo IP "EscudoTermico" trasladado a forma separada con riesgo incrementado |
| Cuerpo caveat retiro | Cuerpo invariable §8.3 sin cambio | APROBADO — sin modificacion | Header actualizado a "Escudo Termico NTC:"; cuerpo literal sin cambio | §3 | §8.3 / §8.4 aprobacion original vigente |

**Evidencia consultada para este gate:**
- Bruna_gate_empaque_v1 §8.3, §8.4, §9.1 (bases del gate previo sobre los mismos elementos semanticos)
- Orlan Refresh 2026-05-06 (riesgo de descriptividad "Escudo Termico" en dos palabras separadas)
- Decision verbal de Kike 2026-05-06 (naming finalista, flexibilidad caveat, estrategia paralela Canudas)
- RISK-POLICY.md v1.0 §3 y §4

---

*Gate emitido: 2026-05-06*
*Estado v2.2: APROBADO CON CAVEAT. Dos condiciones suspensivas de produccion abiertas: SAPI VE (con abogado marcario) + decision de Canudas.*
*Proxima accion requerida: Kike presenta a Canudas. Si Canudas elige v2.2: Owner contrata abogado marcario para SAPI VE. Vera P-5 se confirma antes de arte final.*

---

# §11 — Gate variante V3 "beneficio del beneficio" (3 sub-opciones)

**Tipo de gate:** Gate de variante semantica nueva. Las tres sub-opciones se presentan a la Junta como menu de registro tonal — no como finalistas mutuamente excluyentes desde el riesgo de claims. Las decisiones BR-2 de este §11 son independientes entre si: una puede aprobarse sin que las demas sean rechazadas.

**Trigger:** Instruccion del Owner post-Junta 2026-05-06. Jesus Maria (miembro Junta Directiva) propone eje semantico del "beneficio del beneficio": la consecuencia ultima del NTC cuando el ITM falla o esta mal seleccionado — proteccion de la instalacion electrica como capa de respaldo y ultimo escudo. Vael evaluo 6 opciones en VA-5 §Refresh 2026-05-06b y entrego finalista unica (Op. F, score 5,50) y finalista de respaldo (Op. B, score 4,85). Owner instruye presentar 3 sub-opciones a la Junta para que evaluen el registro tonal en forma robusta, no solo la finalista de Vael.

**Insumos consultados:**
- Vael_VA-5_naming-funcion-termica_v1.md §Refresh 2026-05-06b — evaluacion de 6 opciones V3 (completa: criterios, tabla, ranking, recomendacion finalista, compatibilidad con retiro)
- Bruna_gate_empaque_v1 §2 (Claim H rechazado sin alternativa, Claim G aprobado off-empaque) — frontera critica
- Bruna_gate_empaque_v1 §3.4 / §7.1 / §8.3 / §8.4 — cuerpo invariable del retiro vigente
- Bruna_gate_empaque_v1 §10 — gate de cierre V2 ("Escudo Termico NTC*" aprobado con caveat)
- BR-5 transversal (Precedentes #1, #2, #4, #5) — criterios de superlativos, exclusion, garantia de resultado, emocionalidad sin sensacionalismo

**Alcance:** Las 3 sub-opciones corresponden a:
- **V3a:** "Respaldo termico ante el breaker*" (Op. F de Vael — finalista #1)
- **V3b:** "Respaldo termico ante fallas del termomagnetico*" (variante formal de V3a; sin anglicismo)
- **V3c:** "Ultima linea de defensa electrica*" (Op. B de Vael — finalista de respaldo)

**Nota previa sobre el Claim H (la frontera inamovible de este gate):** El Claim H fue rechazado sin alternativa en §2 y esa decision no tiene excepciones. V3 existe precisamente porque su argumento puede formularse sin cruzar esa frontera — el beneficio ultimo es la proteccion de la instalacion electrica (cableado, bornes, el protector mismo) ante corrientes excesivas cuando el ITM falla o esta mal calibrado, NO la proteccion del motor, compresor o equipo conectado. Cualquier formulacion que sin objeto explicito permita leer "este producto protege mi equipo conectado" es rechazada sin caveat posible.

---

## §11.1 — Sub-opcion V3a: "Respaldo termico ante el breaker*"

**Texto exacto del badge (tiro):** Respaldo termico ante el breaker*

**Origen:** Finalista #1 de Vael VA-5 §Refresh 2026-05-06b (Op. F, score 5,50). Aportacion editorial de Vael — no tenia antecedente previo en el universo de candidatos del Owner. Argumento central: es la unica de las 6 opciones que codifica el argumento literal de Jesus Maria en el tiro sin salto interpretativo. La cadena causal esta completa en 5 palabras.

**Antecedente de gate:** Claim G aprobado off-empaque en §2 de este documento:
> "El Sensor NTC actua como una capa adicional de proteccion termica que respalda al interruptor termomagnetico de la instalacion."

V3a es la condensacion de ese texto en un badge de 5 palabras. La relacion logica es directa: lo que el Claim G describe en una oracion, V3a lo sintetiza en el tiro. La migracion de off-empaque a tiro del empaque es el punto que este gate resuelve.

### §11.1.1 — Riesgo Claim H

**Evaluacion:** BAJO.

"Respaldo termico ante el breaker" no afirma proteccion del equipo conectado. El objeto implicito del respaldo es el breaker / interruptor termomagnetico — no el motor, el compresor, ni ningun electrodomestico. La frase describe la posicion del sistema en la cadena de protecciones: hay un breaker; este dispositivo es un respaldo termico de ese breaker cuando el breaker no es suficiente. El comprador que lee "respaldo ante el breaker" no infiere naturalmente "proteccion de mi equipo conectado" — infiere "proteccion del circuito cuando el breaker falla."

**Frontera de extension prohibida:** Ningun texto derivado de este badge puede afirmar consecuencias sobre el equipo conectado. Ejemplos prohibidos sin gate adicional:
- "Respaldo termico ante el breaker — protege tus equipos"
- "Respaldo termico ante el breaker cuando el breaker no es suficiente para salvar tu motor"

El cuerpo invariable del retiro §8.3 opera como el guardrail que precisa el alcance real: "Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actua como proteccion de sobrecarga directa de la carga conectada."

**Sobre la migracion off-empaque a tiro:** El Claim G fue aprobado solo off-empaque en §2 con el argumento de que en el empaque "introduce al breaker termomagnetico como actor externo que el consumidor residencial no comprende en ese contexto, complejiza el mensaje y puede generar la pregunta contraria ('entonces el NTC no es suficiente?')." Esa decision sigue siendo valida como criterio general. Sin embargo, el contexto de V3 es diferente: V3 es precisamente el eje semantico donde el breaker NO ES el actor a ocultar sino el actor a nombrar — el beneficio del beneficio es que esta tecnologia actua cuando el breaker falla. Nombrar al breaker en V3 no complejiza: es el argumento. La prohibicion off-empaque del Claim G fue de proteccion de arquitectura de mensaje (V1/V2 no son el lugar para el argumento del respaldo al breaker); V3a es el lugar correcto para ese argumento. Bruna levanta la restriccion de canal para V3a: el argumento del respaldo al breaker puede migrar al tiro en el contexto especifico de V3.

**Conclusion Claim H V3a:** Riesgo bajo. Aprobable.

### §11.1.2 — Emocionalidad / loss aversion controlada

**Activacion de loss aversion:** Legitima y sustentada en hecho tecnico real.

El argumento de Jesus Maria es tecnico: los breakers en Venezuela estan frecuentemente mal seleccionados, desgastados o sin mantenimiento. Cuando el ITM falla o actua tarde, la corriente excesiva sigue circulando. El NTC es la capa que detecta el calentamiento resultante y desconecta. Eso es un hecho verificado por Vera §1.3 y §1.4.

"Respaldo termico ante el breaker" activa la idea de que el breaker puede no ser suficiente — lo cual en el mercado electrico venezolano es una experiencia cotidiana del instalador tecnico y del consumidor residencial con fallas electricas frecuentes. La activacion emocional proviene de un hecho tecnico real (la posibilidad de falla del ITM), no de una amenaza fabricada.

**Calibracion segun BR-5 Precedente sobre emocionalidad:** El precedente aplicable (criterio sobre superlativos en mercados opacos — BR-5 §1 y §4) establece que la emocionalidad sin sustento factual es rechazable. En V3a, el sustento factual es explicito: el NTC actua cuando el breaker no alcanza. La activacion emocional es proporcional al hecho tecnico. No es sensacionalismo: no afirma que el breaker siempre falla, no afirma que sin este protector habria catastrofe, no promete resultado de proteccion del equipo. Afirma que hay un respaldo disponible si el breaker no es suficiente.

**Sobre "breaker" como anglicismo:** Este es el flag de Vael que el Owner instruyo que Bruna evaluara. Evaluacion: "breaker" es un prestamo lingüistico naturalizado en el registro electrico venezolano. Es el termino que usan electricistas, ferreteros, instaladores y consumidores residenciales en Venezuela para referirse al interruptor termomagnetico. El brand wiki "sin anglicismos innecesarios" no prohíbe prestamos lingüisticos naturalizados — prohíbe anglicismos innecesarios, es decir, anglicismos que tienen un equivalente español igualmente claro y sin coste de comprension. En este caso, "breaker" y "termomagnetico" NO son equivalentes en registros de audiencia: "breaker" funciona para el consumidor residencial y para el instalador; "termomagnetico" funciona para el instalador tecnico pero tiene menor penetracion en el consumidor residencial. La eleccion entre "breaker" y "termomagnetico" es una decision de registro de audiencia, no de anglicismo prohibido. Bruna evalua: "breaker" es aceptable en el tiro del empaque con el sustento de que es termino naturalizado en el vocabulario electrico venezolano. Si el Owner mantiene la instruccion de evitar anglicismos incluso naturalizados, V3b resuelve esa restriccion. La decision sobre el anglicismo es del Owner; Bruna no lo bloquea.

**Conclusion emocionalidad V3a:** Activacion legitima. No sensacionalismo. Aceptable bajo BR-5.

### §11.1.3 — Compatibilidad con cuerpo invariable §8.3 y headers propuestos

**Cuerpo del caveat:** El cuerpo invariable de §8.3 es compatible sin modificacion. La frase "Funciona como capa adicional de proteccion termica; no reemplaza al interruptor termomagnetico de la instalacion" es el refuerzo semantico exacto que V3a necesita — el retiro confirma la posicion del sistema en la cadena (respaldo, no reemplazo). La coherencia es maxima.

**Version recomendada del retiro:** Version A (neutro funcional), segun recomendacion de Vael §R6b-6 confirmada por Bruna. La Version B (con NTC) es segunda opcion si el Owner quiere nombrar el componente. La Version C (con Escudo Termico) no es recomendada: introduce confusión de naming con V2 en un claim de V3.

**Header literal del bullet retiro CARACTERISTICAS:**

> Respaldo termico ante el breaker:

**Texto literal del caveat de retiro completo (Version A — header + cuerpo invariable §8.3):**

> **Respaldo termico ante el breaker:** sensor de temperatura ubicado junto al rele de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se danen. Protege al protector mismo y a la instalacion electrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actua como proteccion de sobrecarga directa de la carga conectada. Funciona como capa adicional de proteccion termica; no reemplaza al interruptor termomagnetico de la instalacion.

**Nota operativa:** Si el Owner prefiere Version B (con NTC como identificador tecnico en el header), el header seria:

> Respaldo termico ante el breaker (sensor NTC):

seguido del mismo cuerpo invariable. El parentetico "(sensor NTC)" identifica el componente sin convertirlo en el concepto principal — coherente con el eje semantico de V3.

### §11.1.4 — Decision BR-2

**Decision: APROBADO CON CAVEAT**

**Condicion 1 (caveat de retiro obligatorio):** El cuerpo invariable de §8.3 debe acompañar el badge en el retiro. Header literal: "Respaldo termico ante el breaker:". Sin este texto en el retiro, el badge no se considera aprobado.

**Condicion 2 (extension prohibida):** Ningun texto adicional en el mismo artefacto puede afirmar consecuencias sobre el equipo conectado derivadas de este badge. El badge aprueba el argumento del respaldo al breaker; no aprueba ningun claim de proteccion de la carga.

**Condicion 3 (decision Owner sobre anglicismo "breaker"):** El uso de "breaker" en el tiro requiere confirmacion explicita del Owner de que el prestamo lingüistico naturalizado es aceptable en este contexto de empaque. Si el Owner requiere el equivalente en español formal, V3b es la alternativa directa con el mismo gate. Bruna no bloquea el anglicismo; declara la decision como del Owner.

**Rationale:** V3a es la condensacion del Claim G aprobado off-empaque (§2), que ya tiene antecedente de gate favorable con riesgo tecnico bajo. La migracion al tiro es valida en el contexto especifico de V3 porque el argumento del breaker es el eje semantico de V3, no un elemento secundario que complejiza el mensaje. El riesgo de Claim H es bajo porque el objeto del respaldo es el breaker (el ITM), no el equipo conectado. La emocionalidad es legitima y proporcional al hecho tecnico. El cuerpo del retiro §8.3 ya contiene el guardrail necesario.

**Clausula RISK-POLICY aplicada:** §3 — no afirmar datos falseables. "Respaldo termico ante el breaker" describe una funcion real verificada por Vera §1.3 y por el Claim G ya aprobado. No hay dato falseable en el badge.

**Evidencia consultada:** Vael VA-5 §Refresh 2026-05-06b Op. F; Bruna gate_empaque_v1 §2 Claim G y Claim H; Vera_brief_tecnico_v1 §1.3 y §1.4; BR-5 Precedentes #1 y #4.

---

## §11.2 — Sub-opcion V3b: "Respaldo termico ante fallas del termomagnetico*"

**Texto exacto del badge (tiro):** Respaldo termico ante fallas del termomagnetico*

**Origen:** Variante en español formal de V3a. No tenia entrada propia en el ranking de Vael — Vael la menciona como caveat de presentacion de Op. F ("si el Owner activa la politica de anglicismos, la version de respaldo es 'Respaldo termico ante el termomagnético*'"). El Owner instruyo a Bruna evaluarla como sub-opcion independiente para presentar a la Junta en un registro tecnico-formal diferenciado.

**Diferencias respecto a V3a:**
- Reemplaza "el breaker" (coloquial / anglicismo naturalizado) por "fallas del termomagnetico" (español tecnico formal)
- Añade "fallas del" — lo que precisa que el respaldo se activa ante una condicion de falla del ITM, no ante cualquier operacion del ITM
- Cuatro palabras adicionales (7 palabras totales vs. 5 de V3a)

### §11.2.1 — Riesgo Claim H

**Evaluacion:** BAJO — identico a V3a.

La sustitucion de "el breaker" por "fallas del termomagnetico" no cambia el objeto del respaldo ni abre interpretaciones de proteccion del equipo conectado. "Respaldo termico ante fallas del termomagnetico" es, si acaso, mas preciso que V3a porque especifica el contexto de activacion ("ante fallas") — lo que aclara que el sistema no actua siempre que hay un breaker presente, sino cuando ese breaker falla o es insuficiente. Esa precision reduce, no aumenta, el riesgo de interpretacion incorrecta.

**Frontera de extension prohibida:** identica a V3a. Ninguna afirmacion sobre el equipo conectado puede derivarse del badge sin gate adicional.

**Conclusion Claim H V3b:** Riesgo bajo. Aprobable.

### §11.2.2 — Emocionalidad / loss aversion controlada

**Activacion de loss aversion:** Legitima. Mismo fact tecnico que V3a.

La diferencia es de intensidad: "fallas del termomagnetico" es un registro tecnico que el instalador decodifica inmediatamente y con precision ("falla del ITM" = evento especifico de su practica profesional). El consumidor residencial puede decodificar "fallas del termomagnetico" como una amenaza real, aunque con menor inmediatez que "el breaker" (termino mas coloquial). El loss aversion se activa pero con menor intensidad emocional que V3a para el consumidor residencial promedio.

**Para el instalador tecnico:** V3b puede ser marginalmente mas convincente que V3a precisamente porque el registro formal ("termomagnetico") es el vocabulario de su profesion en documentos tecnicos y en el dialogo con clientes profesionales. El instalador que vende a un administrador de edificio o a un cliente corporativo puede preferir usar el termino tecnico.

**Sobre la politica de anglicismos:** V3b resuelve completamente la restriccion de anglicismos del Owner. "Termomagnetico" es la denominacion tecnica estandar en español para el interruptor termico y magnetico. No hay ambigüedad regulatoria ni de registro de marca en el termino.

**Calibracion segun BR-5:** Identica a V3a. La activacion emocional es proporcional al hecho tecnico real. No es sensacionalismo.

**Conclusion emocionalidad V3b:** Activacion legitima, de intensidad media-alta (ligeramente menor que V3a para consumidor residencial; equivalente o mayor para instalador tecnico formal). Aceptable bajo BR-5.

### §11.2.3 — Compatibilidad con cuerpo invariable §8.3 y headers propuestos

**Cuerpo del caveat:** El cuerpo invariable de §8.3 es compatible sin modificacion. La coherencia es identica a V3a: el retiro menciona "no reemplaza al interruptor termomagnetico de la instalacion" — el badge del tiro dice exactamente que el sistema actua ante fallas de ese mismo dispositivo. Coherencia perfecta.

**Version recomendada del retiro:** Version A (neutro funcional). Mismas razones que V3a.

**Header literal del bullet retiro CARACTERISTICAS:**

> Respaldo termico ante fallas del termomagnetico:

**Texto literal del caveat de retiro completo (Version A):**

> **Respaldo termico ante fallas del termomagnetico:** sensor de temperatura ubicado junto al rele de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se danen. Protege al protector mismo y a la instalacion electrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actua como proteccion de sobrecarga directa de la carga conectada. Funciona como capa adicional de proteccion termica; no reemplaza al interruptor termomagnetico de la instalacion.

**Nota de longitud para Oz y Atlas:** V3b tiene 7 palabras en el badge vs. 5 de V3a. En el blister de Alternativa B, la jerarquia visual del badge de velocidad ("El mas rapido ante parpadeos (< 0,03 s)") debe seguir siendo dominante. Oz y Atlas deben confirmar que 7 palabras caben sin comprimir esa jerarquia. Si el espacio es critico, V3a (5 palabras) es la alternativa directa.

### §11.2.4 — Decision BR-2

**Decision: APROBADO CON CAVEAT**

**Condicion 1 (caveat de retiro obligatorio):** Identica a V3a. Header literal: "Respaldo termico ante fallas del termomagnetico:". Cuerpo invariable §8.3 sin modificacion.

**Condicion 2 (extension prohibida):** Identica a V3a. Sin afirmaciones sobre el equipo conectado derivadas del badge.

**Condicion 3 (confirmacion de espacio de diseno):** 7 palabras en el badge requieren confirmacion de Oz / Atlas de que no compiten visualmente con el badge de velocidad.

**Rationale:** V3b es un claim tecnicamente honesto, con riesgo Claim H bajo (menor aun que V3a por la precision de "fallas del"), sin anglicismos, con activacion emocional legitima y con coherencia perfecta con el cuerpo del retiro §8.3. Es la variante de menor exposicion a cualquier objecion sobre el registro lingüistico. Su unico costo es la longitud (7 palabras) y la ligeramente menor intensidad emocional para el consumidor residencial respecto a V3a.

**Clausula RISK-POLICY aplicada:** §3 — no afirmar datos falseables. Identico a V3a.

**Evidencia consultada:** Vael VA-5 §Refresh 2026-05-06b (Op. F y caveat de presentacion sobre anglicismo); Bruna gate_empaque_v1 §2 Claim G y Claim H; Vera_brief_tecnico_v1 §1.3.

---

## §11.3 — Sub-opcion V3c: "Ultima linea de defensa electrica*"

**Texto exacto del badge (tiro):** Ultima linea de defensa electrica*

**Origen:** Finalista de respaldo de Vael VA-5 §Refresh 2026-05-06b (Op. B, score 4,85 — empate tecnico con Op. E). Vael la incluye como segunda opcion para el Owner si la prioridad es la activacion emocional maxima del consumidor final sobre la legibilidad tecnica del instalador. Flag de Vael: "defensa de que" queda implicito — riesgo Claim H medio.

**Contexto del origen:** La expresion "ultima linea de defensa" aparecio en el research de Perplexity aplicada al equipo conectado ("Sistema de Respaldo Termico: La ultima linea de defensa para tu aire acondicionado") — lo que cruza el Claim H directamente. Vael la redirige a "la instalacion electrica" como objeto de defensa. Esa redireccion es el punto critico que este gate evalua.

### §11.3.1 — Riesgo Claim H

**Evaluacion:** MEDIO. Aprobable con caveat reforzado — no rechazable, pero requiere condicion explicita adicional.

**El analisis del objeto de "defensa":** "Ultima linea de defensa electrica" sin objeto explicito del sustantivo "defensa" genera ambigüedad semantica en el tiro:
- Lectura A (instalador tecnico, contexto electrico profesional): "defensa electrica" = defensa del sistema electrico de la instalacion (cableado, bornes, el protector). Esta lectura es la que Vael propone y la que no cruza el Claim H.
- Lectura B (consumidor residencial sin contexto tecnico, especialmente el que tuvo una falla que daño un electrodomestico): "defensa electrica" = defensa de mis equipos electricos / de mis electrodomesticos. Esta lectura SI cruza el Claim H porque el consumidor puede interpretar que el badge promete proteccion de la carga conectada.

El adjetivo "electrica" no resuelve la ambigüedad: tanto la instalacion como los equipos conectados son parte del sistema electrico del hogar. Un consumidor que perdio un televisor o un compresor en una falla electrica leeran "defensa electrica" como "defensa de mis equipos electricos" — no como "defensa del cableado y del protector."

**La diferencia critica con V3a/V3b:** En V3a y V3b, el objeto del respaldo esta explicito: "ante el breaker" / "ante fallas del termomagnetico". El lector sabe que el respaldo es ante un dispositivo especifico de la instalacion, no ante amenazas generales a sus equipos. En V3c, el objeto de "defensa" no esta explicito — la metafora "ultima linea" opera emocionalmente sin anclar el objeto de defensa. Esa diferencia es la que crea el riesgo Claim H medio que Vael flago correctamente.

**La mitigacion posible:** El cuerpo del retiro §8.3 mitiga la interpretacion incorrecta en quien lee el retiro. Pero en el tiro solo — que es lo que el 80% del comprador promedio en el punto de venta experimenta — la ambigüedad subsiste. Para V3c, el caveat reforzado incluye una condicion de proximidad visual obligatoria: si el badge aparece en el tiro, debe haber en el mismo tiro un texto aclaratorio de no mas de 5 palabras que ancle el objeto de "defensa" a la instalacion electrica (no al equipo). Esa linea aclaratoria no es parte del badge — es un elemento de diseno del tiro que Atlas y Oz deben incorporar.

**Si la condicion de proximidad visual no puede implementarse por restriccion de espacio de diseno:** V3c se convierte en claim SOLO OFF-EMPAQUE (argumentario de ventas, QR, materiales internos) — identica restriccion al Claim G original. El badge no puede aparecer en el tiro del empaque sin esa condicion de diseño satisfecha.

**Conclusion Claim H V3c:** Riesgo medio. Aprobable bajo condicion de proximidad visual en el tiro. Sin esa condicion: aprobado solo off-empaque.

### §11.3.2 — Emocionalidad / loss aversion controlada

**Activacion de loss aversion:** Maxima del conjunto V3. Y esa es precisamente su fortaleza y su tension.

"Ultima linea de defensa" es la metafora de mayor carga emocional del set V3. El adjetivo "ultima" activa la idea de que no hay nada despues — si esto falla, no hay mas proteccion. Para el consumidor que ha experimentado fallas electricas en Venezuela (apagones, variaciones de voltaje, cortocircuitos, incendios de cableado), "ultima linea" es visceralmente real.

**La tension con BR-5:** El precedente de superlativos en BR-5 exige que la emocionalidad este sustentada en hecho factual. "Ultima" como superlativo de posicion es factualmente soportado — el NTC es efectivamente la ultima capa de proteccion termica del sistema antes de que la corriente excesiva dañe el cableado o el protector. El retiro §8.3 confirma esta posicion ("no reemplaza al interruptor termomagnetico de la instalacion" — es una capa adicional, no la primaria, lo que implica que es posterior en la cadena). Hasta ahi, el superlativo es defendible.

El riesgo de sensacionalismo no es en el superlativo "ultima" sino en el objeto implicito de la "defensa". Si el consumidor lee "ultima linea de defensa" como "lo ultimo que se interpone entre la corriente destructiva y MIS EQUIPOS", entonces la activacion emocional deja de ser proporcional al hecho tecnico y se convierte en una sobrepromesa de resultado — que es exactamente la zona del Claim H. La emocionalidad sin el anclaje del objeto de defensa es potencialmente sensacionalista para el segmento de consumidores que tienen expectativas de proteccion de sus equipos.

**Calibracion:** la activacion emocional de V3c es legitima cuando el comprador entiende que la "defensa" es de la instalacion electrica. La activacion emocional de V3c cruza el umbral cuando el comprador infiere que la "defensa" es de sus equipos conectados. El badge por si solo no garantiza cual de las dos lecturas prevalece en el punto de venta.

**Conclusion emocionalidad V3c:** Alta activacion emocional, legitima si el objeto de "defensa" queda anclado. Potencialmente sobrepromesa si el objeto queda implicito sin texto aclaratorio. La condicion de proximidad visual del §11.3.1 es el mecanismo de control.

### §11.3.3 — Compatibilidad con cuerpo invariable §8.3 y headers propuestos

**Cuerpo del caveat:** El cuerpo invariable de §8.3 es compatible. La frase "Funciona como capa adicional de proteccion termica; no reemplaza al interruptor termomagnetico de la instalacion" establece la posicion del sistema en la cadena y contextualiza la "ultima linea" de forma correcta. Sin embargo — y este es un punto critico para Solenne y Atlas — el cuerpo del retiro solo cumple esta funcion aclaratoria si el comprador lo lee. Para el comprador que no lee el retiro, el tiro con "Ultima linea de defensa electrica" sin texto aclaratorio queda con riesgo Claim H medio activo.

**Version recomendada del retiro:** Version A (neutro funcional). La Version A es la mas coherente con la metafora de "ultima linea de defensa" porque el cuerpo funcional describe la posicion del sistema (respaldo termico, no reemplazo del ITM) sin distraer con el nombre del componente. La Version C (con Escudo Termico) introduce confusion de naming con V2.

**Header literal del bullet retiro CARACTERISTICAS:**

> Ultima linea de defensa electrica:

**Texto literal del caveat de retiro completo (Version A):**

> **Ultima linea de defensa electrica:** sensor de temperatura ubicado junto al rele de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se danen. Protege al protector mismo y a la instalacion electrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actua como proteccion de sobrecarga directa de la carga conectada. Funciona como capa adicional de proteccion termica; no reemplaza al interruptor termomagnetico de la instalacion.

**Condicion de proximidad visual (condicion de diseno — obligatoria para uso en tiro del empaque):**

El badge "Ultima linea de defensa electrica*" debe ir acompañado en el tiro del empaque de un texto de anclaje de no mas de 5 palabras que identifique el objeto de la defensa como la instalacion electrica (no el equipo conectado). Propuesta de texto de anclaje:

> De tu instalacion electrica

Este texto va inmediatamente debajo o junto al badge, en un tamano de tipografia menor (subtexto del badge). El conjunto queda:

> **Ultima linea de defensa electrica*** (badge principal)
> *De tu instalacion electrica* (subtexto de anclaje)

Con ese subtexto, la lectura del consumidor queda anclada al objeto correcto y el riesgo Claim H se reduce a bajo. Sin el subtexto, el badge es rechazado para el tiro del empaque (pero aprobado off-empaque).

**Nota para Atlas y Oz:** La condicion de proximidad visual es una condicion de diseno, no un elemento de copy. El texto de anclaje propuesto por Bruna es el texto que deben integrar en el mockup. Si por restriccion de espacio el subtexto no puede implementarse en el tiro, notificar a Bruna antes de avanzar: sin ese texto, el badge de V3c no tiene sello para el tiro.

### §11.3.4 — Decision BR-2

**Decision: APROBADO CON CAVEAT (condicion de proximidad visual en tiro) — APROBADO OFF-EMPAQUE sin condicion adicional**

**Condicion 1 (caveat de retiro obligatorio):** Cuerpo invariable §8.3 con header "Ultima linea de defensa electrica:". Sin este texto en el retiro, el badge no se considera aprobado.

**Condicion 2 (proximidad visual — obligatoria para uso en tiro del empaque):** El badge en el tiro del empaque requiere el subtexto de anclaje "De tu instalacion electrica" inmediatamente adyacente. Sin ese subtexto, el badge del tiro no se considera aprobado para el empaque fisico. Si el espacio de diseno no permite el subtexto, el badge queda aprobado solo off-empaque (argumentario de ventas, QR, materiales internos).

**Condicion 3 (extension prohibida):** Ninguna frase adicional puede afirmar que la "defensa" incluye al equipo conectado. Ejemplos prohibidos: "Ultima linea de defensa electrica para tus equipos"; "Ultima linea de defensa electrica — protege tu compresor."

**Rationale:** V3c tiene la mayor activacion emocional del conjunto y cumple el argumento de Jesus Maria de forma directa e impactante — "ultima linea" es la imagen mas poderosa para el consumidor residencial que ha vivido fallas electricas graves. Sin embargo, la ambigüedad del objeto de "defensa" sin el subtexto de anclaje genera un riesgo Claim H medio que no puede ignorarse. La solucion no es rechazar el badge sino anclar el objeto de defensa en el tiro mediante el subtexto. Con ese anclaje, el riesgo Claim H cae a bajo y el badge es aprobable. Sin el anclaje, el badge en el tiro del empaque es un riesgo medio no mitigado — lo que en la politica de Bruna requiere restriccion de canal (off-empaque unicamente, como el Claim G original). La decision de proximidad visual es de diseno, no de claims conceptual: Bruna puede emitir el gate conceptual como aprobado con condicion; la condicion de diseno la resuelven Atlas y Oz.

**Clausula RISK-POLICY aplicada:** §3 — no afirmar datos falseables; §4 — reversibilidad: si el empaque se imprime con "Ultima linea de defensa electrica" sin subtexto de anclaje y un consumidor reclama que el badge prometia proteccion de sus equipos, el costo de correccion es alto. La condicion de proximidad visual es una medida de reversibilidad preventiva.

**Evidencia consultada:** Vael VA-5 §Refresh 2026-05-06b Op. B; Bruna gate_empaque_v1 §2 Claim H (rationale de rechazo — lectura del consumidor sin distincion de objeto); Vera_brief_tecnico_v1 §1.4; BR-5 Precedente #4 (garantia de resultado).

---

## §11.4 — Tabla comparativa final V3a / V3b / V3c

| Eje de evaluacion | V3a: "Respaldo termico ante el breaker*" | V3b: "Respaldo termico ante fallas del termomagnetico*" | V3c: "Ultima linea de defensa electrica*" |
|---|---|---|---|
| **Riesgo Claim H** | Bajo — objeto del respaldo es el breaker (ITM), no el equipo | Bajo — "fallas del termomagnetico" precisa aun mas el contexto; menor riesgo que V3a | Medio — "defensa electrica" sin objeto explicito; mitigable con subtexto de anclaje en tiro |
| **Activacion emocional** | Alta (tecnico) / Media-alta (consumidor) — "el breaker puede fallar" es experiencia cotidiana en VE | Media-alta (tecnico tecnico-formal) / Media (consumidor) — "termomagnetico" reduce levemente la activacion en consumidor residencial | Alta (consumidor) / Alta (tecnico) — "ultima linea" es la imagen de mayor carga emocional del set |
| **Diferenciacion V1/V2** | Maxima — ninguna de V1/V2 nombra al breaker; eje semantico completamente nuevo | Maxima — idem V3a | Maxima — "ultima linea" + posicion en cadena es eje semantico que V1/V2 no tienen |
| **Registro linguistico** | Coloquial-tecnico — "breaker" es prestamo naturalizado en jerga electrica venezolana | Formal-tecnico — "termomagnetico" es denominacion estandar; sin anglicismos | Emocional-metaforico — "ultima linea de defensa" es metafora universal de alto impacto |
| **Audiencia primaria** | Mixta (instalador + consumidor informado) | Instalador tecnico formal / consumidor de perfil exigente | Consumidor final (loss aversion intensa) + instalador (argumento de reputacion) |
| **Longitud del badge** | 5 palabras | 7 palabras | 5 palabras |
| **Condicion de diseño adicional** | Ninguna | Confirmacion de espacio (7 palabras) | Subtexto de anclaje obligatorio en tiro: "De tu instalacion electrica" |
| **Versión retiro recomendada** | Version A (neutro funcional) | Version A (neutro funcional) | Version A (neutro funcional) |
| **Decision BR-2** | APROBADO CON CAVEAT | APROBADO CON CAVEAT | APROBADO CON CAVEAT (con condicion de proximidad visual en tiro) |

---

## §11.5 — Recomendacion combinada

### Menor riesgo combinado: V3b — "Respaldo termico ante fallas del termomagnetico*"

V3b acumula el menor riesgo combinado (Claim H, linguistico, diseño):
- Riesgo Claim H: bajo — el objeto del respaldo esta explicito y el calificador "fallas del" precisa el contexto de activacion mejor que V3a
- Sin anglicismo — resuelve la restriccion del Owner sin condicion suspensiva sobre "breaker"
- Coherencia con retiro §8.3: perfecta — el retiro menciona el "interruptor termomagnetico" usando exactamente el vocabulario del badge
- Sin condicion de diseño de proximidad visual como V3c

El unico costo es la longitud (7 palabras) y la ligeramente menor intensidad emocional para el consumidor residencial respecto a V3a. Para la audiencia instalador tecnico formal, V3b puede ser la formulacion mas convincente del set.

### Mayor riesgo combinado: V3c — "Ultima linea de defensa electrica*"

V3c tiene el mayor riesgo individual del trio debido al riesgo Claim H medio por ambigüedad del objeto de "defensa". Ese riesgo es mitigable pero requiere una condicion de diseño adicional (subtexto de anclaje) que introduce dependencia operativa de Atlas / Oz. Si la condicion no puede cumplirse en el tiro, el badge cae a off-empaque unicamente.

### Las 3 son ejecutables: la Junta elige el registro tonal

Las tres sub-opciones son aprobables. No hay ninguna que deba descartarse como "evaluada y no viable." La Junta puede seleccionar en funcion del registro tonal que considere mas alineado con la estrategia de comunicacion de Exceline:

- **La Junta prioriza conexion coloquial y el argumento del instalador cotidiano:** V3a. El "breaker" es el mundo del instalador y del consumidor con experiencia electrica en Venezuela. Maximo equilibrio entre activacion emocional y riesgo bajo.
- **La Junta prioriza el registro formal y la ausencia de anglicismos para documentos y materiales profesionales:** V3b. La formulacion mas defendible en cualquier contexto de revision formal (cliente corporativo, ente regulatorio, abogado marcario).
- **La Junta prioriza la maxima activacion emocional del consumidor final como diferenciador de punto de venta:** V3c. La imagen de "ultima linea" es la mas poderosa del set. Requiere coordinacion de diseno adicional (subtexto de anclaje) pero es ejecutable.

**Las tres son complementarias, no mutuamente excluyentes a largo plazo:** V3a/V3b pueden coexistir segun el canal (V3a en empaque de consumo masivo, V3b en materiales de especificacion tecnica). V3c puede funcionar en el argumentario de ventas off-empaque sin necesidad del subtexto de anclaje (en ese contexto el vendedor provee el contexto verbal). La Junta elige el registro para el empaque fisico; el Owner puede asignar los otros registros a otros artefactos.

### Sub-opcion hibrida: "Respaldo termico ante fallas electricas graves*"

Durante el analisis, Bruna identifica una opcion hibrida que no fue propuesta por Vael como badge de V3 para este gate pero que combina atributos de V3a y V3c:

**Texto:** "Respaldo termico ante fallas electricas graves*"

Esta opcion nombra la amenaza ("fallas electricas graves") sin depender del "breaker" ni del "termomagnetico", activa la dimension de amenaza sin la ambigüedad del objeto de "defensa" de V3c, y es igualmente apta para el consumidor residencial y el instalador. El riesgo Claim H es bajo: "fallas electricas" ancla la proteccion al sistema electrico (no al equipo conectado). La activacion emocional es media-alta (comparable a V3a pero menor que V3c).

Bruna eleva esta opcion al Owner como candidata adicional por si la Junta considera que ninguna de las tres sub-opciones principales captura exactamente el registro deseado. Si el Owner quiere incluirla en la presentacion a la Junta, Bruna da gate provisional APROBADO CON CAVEAT bajo las mismas condiciones que V3a (cuerpo invariable §8.3, extension prohibida, sin condicion de diseno adicional). Score estimado en el ranking de Vael: ~4,75 (equivalente a Op. C que obtuvo ese score en el ranking ponderado). No alcanza la finalista principal (V3a/V3b) pero es ejecutable.

---

## §11.6 — Opciones V3 evaluadas y descartadas del proceso (referencia documental)

Las siguientes opciones del universo de 6 de Vael §Refresh 2026-05-06b fueron evaluadas por Vael pero no forman parte de las 3 sub-opciones instruidas por el Owner para presentacion a la Junta. Se documentan aqui como referencia del proceso, con la razon por la que no avanzan a este gate.

| Opcion Vael | Texto | Por que no avanza a la Junta |
|---|---|---|
| Op. A | "Capa adicional de proteccion electrica*" | Falla anti-pleonasmo critico: el cuerpo del retiro §8.3 ya usa la expresion "capa adicional de proteccion termica". Migrar esa frase al tiro es circularidad, no diferenciacion de V3. Score 3,15 — el mas bajo del set. |
| Op. D | "Escudo electrico de respaldo*" | Diferenciacion parcial de V2 ("Escudo Termico NTC*"): el consumidor puede confundir "Escudo electrico" con "Escudo Termico" — son variaciones del mismo concepto de marca para quien no tiene el contexto completo. Score 3,85. |
| Op. E | "Proteccion ante corrientes destructivas*" | Riesgo Claim H medio-alto: "proteccion ante corrientes destructivas" sin objeto explicito puede ser leido como proteccion del equipo conectado ante corrientes que lo destruirian. Aunque el activacion emocional es alta (score 4,85 empate con Op. B), el riesgo Claim H es el mas alto del set junto a su empate — Bruna lo descarta para la presentacion a la Junta. Disponible como argumento off-empaque con caveat explicito del objeto de defensa. |

Estas tres opciones son **evaluadas y descartadas del proceso de gate de empaque** — disponibles como referencia documental del proceso pero NO van a la Junta para seleccion de badge de empaque.

---

## §11.7 — Headers literales para Solenne y Atlas (sub-opciones aprobadas)

### V3a — Aprobada con caveat

**Texto exacto del badge tiro:**
> Respaldo termico ante el breaker*

(Con asterisco obligatorio. Sin TM. El Owner debe confirmar el anglicismo "breaker" como aceptable.)

**Texto exacto del header del bullet retiro CARACTERISTICAS:**
> Respaldo termico ante el breaker:

**Texto exacto del header del caveat de retiro:**
> Respaldo termico ante el breaker:

**Cuerpo del caveat:** Version A (neutro funcional). Texto literal completo del cuerpo (sin modificacion del §8.3):
> sensor de temperatura ubicado junto al rele de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se danen. Protege al protector mismo y a la instalacion electrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actua como proteccion de sobrecarga directa de la carga conectada. Funciona como capa adicional de proteccion termica; no reemplaza al interruptor termomagnetico de la instalacion.

**Version B del header (si Owner confirma NTC en el retiro):**
> Respaldo termico ante el breaker (sensor NTC):
seguido del mismo cuerpo invariable.

---

### V3b — Aprobada con caveat

**Texto exacto del badge tiro:**
> Respaldo termico ante fallas del termomagnetico*

(Con asterisco obligatorio. Sin TM. Sin anglicismo. Verificar espacio de diseno con Oz / Atlas.)

**Texto exacto del header del bullet retiro CARACTERISTICAS:**
> Respaldo termico ante fallas del termomagnetico:

**Texto exacto del header del caveat de retiro:**
> Respaldo termico ante fallas del termomagnetico:

**Cuerpo del caveat:** Version A (neutro funcional). Texto literal del cuerpo: idem V3a — cuerpo invariable §8.3 sin modificacion.

---

### V3c — Aprobada con caveat (condicion de proximidad visual)

**Texto exacto del badge tiro:**
> Ultima linea de defensa electrica*

(Con asterisco obligatorio. Sin TM. REQUIERE subtexto de anclaje adyacente en el tiro del empaque.)

**Texto exacto del subtexto de anclaje obligatorio (para tiro del empaque):**
> De tu instalacion electrica

(En tipografia menor adyacente al badge. Sin este subtexto, el badge no tiene sello para el tiro del empaque — aprobado solo off-empaque.)

**Texto exacto del header del bullet retiro CARACTERISTICAS:**
> Ultima linea de defensa electrica:

**Texto exacto del header del caveat de retiro:**
> Ultima linea de defensa electrica:

**Cuerpo del caveat:** Version A (neutro funcional). Texto literal del cuerpo: idem V3a — cuerpo invariable §8.3 sin modificacion.

---

## §11.8 — BR-2 Genteca — Entradas de gate §11

**Dominio:** Genteca
**Proyecto:** 2026-04_GSM-MB-RB-RF_empaque
**Fecha de decision:** 2026-05-06
**Documento de gate:** Bruna_gate_empaque_v1 §11
**Gatekeeping trigger:** Instruccion del Owner de gate de 3 sub-opciones de V3 "beneficio del beneficio" para presentacion a la Junta Directiva. Trigger conceptual: propuesta de Jesus Maria (miembro Junta Directiva).

| Sub-opcion gateada | Texto exacto del tiro | Decision | Condicion principal | Clausula RISK-POLICY | Precedente |
|---|---|---|---|---|---|
| V3a | Respaldo termico ante el breaker* | APROBADO CON CAVEAT | Caveat retiro §8.3 obligatorio; confirmacion Owner anglicismo "breaker"; sin extension sobre equipo conectado | §3 — no afirmar datos falseables | Claim G aprobado off-empaque §2 — antecedente directo |
| V3b | Respaldo termico ante fallas del termomagnetico* | APROBADO CON CAVEAT | Caveat retiro §8.3 obligatorio; confirmacion espacio de diseño Oz/Atlas (7 palabras); sin extension sobre equipo conectado | §3 | Claim G aprobado off-empaque §2 — variante formal |
| V3c | Ultima linea de defensa electrica* | APROBADO CON CAVEAT | Caveat retiro §8.3 obligatorio; subtexto de anclaje "De tu instalacion electrica" obligatorio en tiro del empaque; sin extension sobre equipo conectado; si subtexto no cabe: solo off-empaque | §3 + §4 (reversibilidad) | BR-5 Precedente #4 (garantia de resultado — frontera vigilada) |

**Evidencia consultada para este gate:**
- Vael_VA-5_naming-funcion-termica_v1.md §Refresh 2026-05-06b (evaluacion de 6 opciones, ranking, finalistas, compatibilidad con retiro)
- Bruna_gate_empaque_v1 §2 Claim G (aprobado off-empaque — antecedente directo de V3a/V3b) y Claim H (rechazado sin alternativa — frontera inamovible)
- Bruna_gate_empaque_v1 §8.3 / §8.4 (cuerpo invariable del retiro vigente)
- BR-5 transversal Precedentes #1, #2, #4 (superlativos, exclusion, garantia de resultado)
- RISK-POLICY.md v1.0 §3 y §4

---

## §11.9 — Condiciones suspensivas y proximos pasos

### Condiciones que aplican a las tres sub-opciones antes de produccion de imprenta

**Condicion compartida 1 — Vera P-5 (mecanismo NTC continuo vs. fusible unico):** Pendiente heredada de §8.1. Impacto en V3: bajo. Ninguna de las tres sub-opciones usa el adjetivo "activa" ni promete recurrencia de actuacion. Si Vera confirma fusible de corte unico, el cuerpo del retiro §8.3 puede requerir ajuste menor (no es condicion bloqueante del gate conceptual ni de la presentacion a la Junta).

**Condicion compartida 2 — Decision de la Junta sobre cual sub-opcion avanza:** Las tres estan gateadas. La Junta selecciona la variante (o confirma que avanza off-empaque como argumentario). Hasta esa decision, ninguna pasa a produccion de arte final.

**Condicion especifica V3a — Confirmacion Owner sobre "breaker":** Si el Owner requiere español formal, V3b es el reemplazo directo sin gate adicional.

**Condicion especifica V3b — Confirmacion de espacio de diseño:** Oz y Atlas verifican que 7 palabras caben en el tiro sin comprimir la jerarquia visual del badge de velocidad.

**Condicion especifica V3c — Subtexto de anclaje en tiro:** Atlas y Oz implementan "De tu instalacion electrica" como subtexto adyacente al badge. Sin ese subtexto, el badge no tiene sello para el tiro del empaque.

### Notificaciones de cascada post-decision de la Junta

**Para Solenne (SO-1 delta):** No actuar hasta que la Junta seleccione la sub-opcion. Cuando la decision llegue: el texto del badge, el header del retiro y el cuerpo invariable estan todos en §11.7 — la integracion es directa. Si la Junta selecciona V3c: coordinar con Atlas la implementacion del subtexto de anclaje antes de integrar en el copy del retiro.

**Para Atlas (mockups):** Preparar 3 mockups paralelos de tiro con V3a / V3b / V3c para presentacion a la Junta. Para V3c: el mockup debe incluir el subtexto "De tu instalacion electrica" adyacente al badge — esa es la condicion de diseño que la Junta debe evaluar.

**Para Aurelio (AU-1):** Si V3 avanza como argumento de empaque, el memo de AU-1 puede requerir una nota sobre la tercera variante. El Owner evalua si es necesario un AU-1 v3 o si la comunicacion de V3 a la Junta se integra en el mismo flujo de la decision en sesion.

**Para Vael (informacion):** V3a y V3b son aprobadas. V3c es aprobada con condicion de diseño. La recomendacion finalista de Vael (Op. F = V3a) se confirma como la de menor riesgo combinado entre las aprobadas con empaque fisico sin condicion de diseño adicional.

**Para Oz (redline arte):** No actuar hasta decision de la Junta. Cuando el Owner instruya: el asterisco en el tiro es obligatorio en las tres sub-opciones. El texto del retiro usa el header de la sub-opcion seleccionada + el cuerpo invariable de §8.3. Para V3c: incluir el subtexto de anclaje en el tiro antes de qualquier implementacion.

---

*Gate emitido: 2026-05-06*
*Estado V3: V3a APROBADO CON CAVEAT — V3b APROBADO CON CAVEAT — V3c APROBADO CON CAVEAT (condicion de proximidad visual en tiro del empaque).*
*Sub-opcion de menor riesgo combinado: V3b. Sub-opcion de mayor riesgo combinado: V3c.*
*Las 3 son presentables a la Junta. La Junta selecciona el registro tonal.*
*Proxima accion requerida: Owner presenta el menu de 3 sub-opciones a la Junta con mockups de Atlas. Decision de Junta determina cual sub-opcion avanza a produccion de arte final. Confirmacion Owner sobre anglicismo "breaker" requerida si la Junta selecciona V3a.*
