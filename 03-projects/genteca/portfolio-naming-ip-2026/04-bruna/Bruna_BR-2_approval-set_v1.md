---
doc_type: BR-2-approval-set
project_id: portfolio-naming-ip-2026
domain: genteca
version: v1.0
author: Bruna
fecha: 2026-05-13
referencia_notas: Bruna_BR-1_risk-notes_v1.md (razonamiento completo por gate)
downstream: Solenne (Phase 4), Vivienne (Phase 5)
nota: >
  Este es el documento de decision formal. Las decisiones aqui son vinculantes para
  Phase 4 en adelante. Ningun claim marcado con seal Bruna pendiente en VA-5 pasa
  a produccion (Solenne, Vivienne, deck) sin referencia a este documento.
  Fecha de decision: 2026-05-13.
---

# BR-2 — Approval Set
## Portfolio Naming IP 2026 (Genteca) — Phase 3

> Decisiones formales por gate. Estructura: decision + rationale + clausula RISK-POLICY
> + precedente BR-5 si aplica + caveat literal cuando corresponde + implicacion para
> Solenne (Phase 4).

---

### Gate 1 — Override curva inversa universal de facto

- **Decision:** APROBADO CON CAVEAT (aplicacion acotada)
- **Rationale:** El override del Owner (charter §3 decision 4) es operativamente valido
  para el proposito de este proyecto (generacion de candidatos de nombre para registro
  IP). El override no crea un claim de diferenciacion — confirma la presencia de la funcion
  en la gama para que los nombres no sean rechazados por ausencia de sustento tecnico.
  Para el deck del abogado, el override es aceptable con la siguiente acotacion: se
  describe como "funcion presente en la gama Exceline / Exceline Profesional / Genius
  segun los productos verificados en HDEs consultadas" — no como "funcion auditada
  producto por producto". Esta distincion evita el riesgo de credibilidad si el abogado
  o un especificador pide HDE de un producto especifico que no haya sido auditado.
  En publicidad o empaque, el override NO aplica como claim externo sin auditoria I+D.
  En el deck del abogado (audiencia: abogado marcario evaluando registrabilidad), el
  override es funcional.
- **Clausula RISK-POLICY:** RISK-POLICY v1.0 §3 (no afirmar datos que puedan ser falsos
  si son verificables). El override se opera como asuncion de parte del Owner, no como
  afirmacion de Genteca ante terceros sin corroboracion.
- **Precedente BR-5 aplicado:** BR-5 Precedente #1 (superlativo con dato cuantitativo
  en mercado opaco) — analogia de principio: cuando el hecho tecnico es plausible y el
  Owner lo avala, el claim es aprobable con caveat. El override es el mecanismo analogico.
- **Caveat literal a integrar en deck del abogado:**
  "La presencia de la curva inversa I-t cold/hot y de la curva inversa V-t algorítmica
  se indica como universal de facto para la gama Exceline / Exceline Profesional / Genius.
  La verificacion producto por producto esta pendiente de auditoria formal por I+D de
  Genteca y debe completarse antes de la primera publicidad comparativa externa que use
  la funcion como diferenciador. En el contexto de este proceso de registro de marca,
  la funcion se documenta con base en los productos Genius y Exceline Profesional en
  los que Vera la confirmo en HDE."
- **Implicacion para Solenne (Phase 4):** Sin impacto en la generacion de candidatos.
  Los nombres de NODO-B y NODO-D pueden usarse para toda la gama sin restriccion
  en Phase 4 y en el deck para el abogado, con el caveat de deck integrado. Si Solenne
  genera nombres para publicidad futura (mas alla del deck del abogado), el caveat
  se activa como restriccion de uso externo hasta que I+D complete la auditoria.

---

### Gate 2 — ThermalCurve (NODO-D) descriptividad critica

- **Decision:** RECHAZADO — el nombre ThermalCurve no es viable para registro en SAPI
  Venezuela ni en IMPI Mexico con los RTBs disponibles en VR-1 de Vera.
- **Rationale:** La curva inversa I-t cold/hot (mecanismo que ThermalCurve nombra) es
  funcion estandar de IEC 60947-4-1 / IEC 60255-8 / IEEE C37.112 presente y documentada
  en toda la competencia industrial relevante (Siemens 3RB3, Eaton C441, Schneider LTMR,
  Rockwell E300 — todos con fuentes verificadas o parcialmente verificadas en OL-1).
  "ThermalCurve" describe literalmente el mecanismo tecnico estandar de la categoria.
  Vera VR-1 no documenta ningun parametro propietario de la implementacion Genteca
  mas alla del estandar IEC/IEEE. La razon "Caliente = Fria / 3" es la especificacion del
  estandar, no un algoritmo propietario. El ajuste de clase 5-30 es una decision de
  implementacion que otros fabricantes pueden igualar. Sin RTB diferenciador propietario,
  el nombre describe la funcion estandar de la industria. En SAPI Venezuela (art. 34 LPI
  1955) y en IMPI Mexico, una marca descriptiva de la funcion del producto en la misma
  clase Niza es causal de inadmisibilidad. La probabilidad de objecion es alta, no media.
- **Clausula RISK-POLICY:** RISK-POLICY v1.0 §3 (no afirmar como propio lo que no puede
  sostenerse). El nombre ThermalCurve no puede sostenerse como fantasia ante un examinador
  tecnico de SAPI/IMPI con el material de Vera disponible hoy.
- **Precedente BR-5 aplicado:** BR-5 Precedente #2 (superlativo de exclusion sin evidencia
  de ausencia del atributo en competidores — rechazado). Analogia inversa: cuando el
  atributo nombrado esta presente en toda la competencia, el nombre que lo describe
  literalmente tiene el mismo problema que un claim de exclusividad sin evidencia — el
  nombre no puede reclamar como propio (o como distinguible) algo que es comun a la
  categoria.
- **Caveat literal:** No aplica — decision es rechazo, no condicionamiento.
- **Declaracion critica para Solenne (Phase 4):**
  **El NODO-D sigue siendo nodo registrable.** La decision es sobre el nombre, no sobre
  el nodo. La curva cold/hot es un diferenciador de naming incluso siendo funcion estandar
  IEC, porque ningun competidor la tiene nombrada con fantasia. El nombre anchor
  ThermalCurve no puede registrarse con los RTBs actuales; Solenne debe generar
  **4 candidatos nuevos para NODO-D** en Phase 4. La direccion semantica: alejarse
  completamente del territorio "curva" y "termica". El beneficio real del nodo es la
  adaptacion al estado real del motor (motor en frio vs motor en caliente). Territorio
  disponible segun VA-1 notas Vael: raices que evoquen adaptacion, estado, respuesta
  proporcional. Evitar "Curve", "Thermal", "Therm-" como componentes del nuevo nombre.
- **Condicion de reapertura (si aplica):** Si Vera puede documentar un parametro
  propietario de la implementacion Genteca que excede el estandar IEC (por ejemplo,
  un factor de enfriamiento diferencial con especificacion propia, un parametro de
  memoria termica con valor diferente a lo que IEC define, o cualquier aspecto de
  algoritmo que no sea derivacion directa de la norma) — la reapertura de este gate
  requiere un nuevo VR-1 actualizado de Vera con ese RTB especifico, y Bruna revisa.
  Sin ese RTB adicional, el rechazo es firme.

---

### Gate 3 — Thermo-Safe Caso A/B

- **Decision:** APROBADO CON CAVEAT — Caso A asumido como postura del deck. Thermo-Safe
  sobrevive como nombre anchor de NODO-C con caveat estructural para el abogado.
- **Rationale:** El empaque actual de GSM-MB/RB/RE (versiones V10/V9/V13) incluye mencion
  de proteccion termica ("AHORA CON PROTECCION TERMICA") confirmada en VR-1 Vera
  (fuente primaria: etiqueta empaque HDE GLA_T). Esta es Caso A — no hay evidencia de
  una version del empaque sin esa mencion. El deck del abogado trabaja sobre la realidad
  actual, que es Caso A. En Caso A, el riesgo de descriptividad de "Thermo-Safe" es
  medio-alto (no bloqueante) por la siguiente razon: "Thermo-Safe" como combinacion
  tiene fantasia suficiente para distinguirse de "PROTECCION TERMICA" del empaque —
  "Safe" no es el traductor literal de "Proteccion" en el uso cotidiano venezolano o
  mexicano. El consumidor no percibe "Thermo-Safe" como descriptor de la funcion
  termica de la misma forma en que percibe "PROTECCION TERMICA". La doctrina de
  equivalencia perceptual SAPI (confirmada en reference_sapi_venezuela_quick.md)
  favorece esta lectura. La memoria SAPI previa confirma que "Thermo-Safe" tiene mejor
  perfil de registro que alternativas como "ThermoShield", "EscudoTermico" o
  "ThermoProtect". La aprobacion es condicionada a que el abogado reciba la distincion
  semantica como argumento de fantasia — no que el nombre se presente como evidentemente
  fantastico sin argumento.
- **Clausula RISK-POLICY:** RISK-POLICY v1.0 §3 y principio de caveats literales:
  cuando el riesgo es medio-alto pero no bloqueante, el caveat especifico es la
  herramienta correcta — no el rechazo.
- **Precedente BR-5 aplicado:** BR-5 Precedente #1 (claim con dato cuantitativo aprobado
  con caveat en mercado con opacidad competitiva). Analogia de estructura: el nombre
  tiene perfil de fantasia bajo doctrina de equivalencia perceptual, pero el abogado
  necesita el argumento explicito — no asumir que el examinador lo vera sin guia.
- **Caveat literal a integrar en deck del abogado (Caso A):**
  "Thermo-Safe es nombre de fantasia que no deriva de la descripcion funcional del
  producto. La combinacion 'Thermo' (prefijo de origen griego, raiz tecnica) + 'Safe'
  (beneficio de seguridad en ingles) no constituye una descripcion literal de la funcion
  del producto para el consumidor venezolano o mexicano promedio. El empaque del producto
  usa la descripcion 'PROTECCION TERMICA', que es la descripcion funcional en espanol;
  'Thermo-Safe' es el nombre de fantasia de la funcion nombrada y es semanticamente
  distinto de la descripcion funcional en uso. Solicitar registro de marca en Clase 9
  con argumentacion de signo de fantasia bajo doctrina de equivalencia perceptual."
- **Nota sobre Caso B:** Si Genteca decide eliminar la mencion de proteccion termica del
  empaque antes del registro, el perfil baja a "medio" y el argumento ante el abogado
  es mas limpio. Esa es una decision comercial/disenio del Owner — Bruna la nota como
  opcion que mejora el perfil de registro si se toma antes de la solicitud FM-02.
- **Implicacion para Solenne (Phase 4):** Thermo-Safe sigue como anchor de NODO-C.
  Solenne genera los 3 candidatos adicionales para NODO-C con la instruccion de que
  las alternativas deben alejarse del espacio semantico Thermo- + descriptor si hay
  colision en busqueda del abogado. El caveat literal arriba es el que Vivienne integra
  en el deck, en el slide correspondiente a NODO-C.

---

### Gate 4 — ForensLog RTB calibration

- **Decision:** APROBADO — el nombre ForensLog se sella con el escenario de acotacion
  a GIII+MV como postura principal del deck. El escenario ampliado (toda la gama Genius)
  queda como decision operativa de Solenne en Phase 4.
- **Rationale:** El RTB "100 ultimas fallas con timestamp" del GIII+MV esta verificado en
  HDE primaria (GIII+MV-V1 ingles y espanol). El comparativo con Rockwell E300 (10
  registros) es HECHO verificado segun tabla Fact/Claim de OL-1. La diferencia 10:1
  es un diferenciador cuantitativo valido bajo BR-5 Precedente #1. Acotar el nombre al
  GIII+MV produce el argumento mas solido ante el abogado: RTB unico, dato cuantitativo
  verificable, comparativo documentado. El escenario ampliado (20-100 fallas segun
  producto) produce ambiguedad en el RTB que el abogado puede cuestionar. Bruna aprueba
  ForensLog con postura Escenario A como recomendacion de riesgo al abogado y deja la
  decision final de escenario a Solenne segun el mejor encaje del nombre, conforme a
  lo asignado en Checkpoint 1 Decision 3.
- **Clausula RISK-POLICY:** RISK-POLICY v1.0 §3. El RTB verificado del Escenario A
  (100 fallas GIII+MV) es dato que puede sostenerse con fuente primaria. El Escenario B
  no tiene RTB unico — debilita la posicion del deck sin ventaja de naming.
- **Precedente BR-5 aplicado:** BR-5 Precedente #1 — superlativo con dato cuantitativo
  verificado en mercado con opacidad competitiva es aprobable. El comparativo "10 veces
  mas registros que el competidor directo identificado" cumple las tres condiciones del
  precedente: dato propio verificado, ningun competidor con dato publicado igual o
  superior al dato propio en el segmento, formulacion con superlativo + dato cuantitativo.
- **Caveat literal a integrar en deck del abogado:**
  "El RTB del nombre ForensLog descansa en el GIII+MV con capacidad de registro de 100
  ultimas fallas con timestamp. El baseline de la gama Genius es 20 ultimas fallas. El
  nombre ForensLog se vincula a la tecnologia de registro forense como concepto, no a
  un numero especifico de eventos — el abogado puede optar por vincular el nombre al
  GIII+MV como portador principal del RTB maxima capacidad."
- **Implicacion para Solenne (Phase 4):** ForensLog es anchor valido de NODO-E. Solenne
  genera los 3 candidatos adicionales. En la Naming Bible, ForensLog se presenta con
  el RTB del GIII+MV como postura principal. Si Solenne, al evaluar el encaje del nombre
  con el portafolio completo, decide ampliar al escenario gama Genius, lo hace con el
  caveat de que el RTB declarado en el deck debe ser "hasta 100 fallas en GIII+MV /
  hasta 20 fallas en gama Genius" — formulacion mas debil. La recomendacion de riesgo
  de Bruna es Escenario A.

---

### Gate 5 — FlickerGuard OMPI / colision productos LED

- **Decision:** APROBADO CON CONTINGENCIA — proceder con FlickerGuard como candidato
  principal; Solenne prepara candidatos alternativos en Phase 4 como contingencia para
  el caso de que la busqueda formal del abogado encuentre conflicto real.
- **Rationale:** El nombre FlickerGuard tiene buen perfil semantico: raiz "Flicker" es
  especificidad tecnica (IEC 61000-4-15, fenomeno de calidad de energia), no es uso
  cotidiano del consumidor venezolano o mexicano promedio — aplica equivalencia
  perceptual. El RTB subyacente (deteccion en 20ms, NODO-B verde en OL-1) es el
  diferenciador mas solido del portafolio. El riesgo de colision con productos LED
  australianos/britanicos es real pero navegable: los sistemas SAPI Venezuela y IMPI
  Mexico no tienen vision directa de marcas australianas no registradas en OMPI con
  designacion sobre esas jurisdicciones. Si el titular LED no tiene registro OMPI que
  designe Venezuela o Mexico, no hay base de oposicion en esas jurisdicciones. La
  distincion de producto (supervisor de voltaje para proteccion de compresores vs
  luminaria de iluminacion) es argumentable ante el examinador. El path de FlickerGuard
  en SAPI/IMPI es viable si la busqueda formal del abogado no encuentra conflicto activo.
- **Clausula RISK-POLICY:** RISK-POLICY v1.0 §4 (reversibilidad): la aprobacion es
  condicionada a la busqueda formal del abogado. Si la busqueda confirma colision activa
  en SAPI o IMPI, los candidatos alternativos de Solenne toman el lugar sin reiniciar
  Phase 4 completa.
- **Precedente BR-5 aplicado:** BR-5 Precedente #1 — el RTB del NODO-B (20ms, sin
  equivalente publicado en el segmento directo) cumple las condiciones para sostener el
  nombre como diferenciador cuantitativo.
- **Caveat literal a integrar en deck del abogado:**
  "FlickerGuard: nombre de fantasia en clase 9. Existe evidencia de productos de
  iluminacion LED (Australia, UK) que usan el termino 'Flicker Guard' como nombre de
  feature en el mismo segmento Niza Clase 9. La busqueda fonética en SAPI Venezuela y
  en IMPI Mexico debe verificar si hay marcas registradas o en tramite con ese nombre
  en la subclase de dispositivos de proteccion y supervision electrica. La coexistencia
  entre un supervisor de voltaje para proteccion de compresores y una luminaria de
  iluminacion LED puede ser navegable bajo argumento de distincion de producto."
- **Implicacion para Solenne (Phase 4):** FlickerGuard es el anchor principal de NODO-B.
  Solenne genera los 3 candidatos adicionales. Solenne debe incluir en la Naming Bible
  una fila de candidatos alternativos para NODO-B, marcada como "contingencia OMPI",
  con raices semanticas del territorio: Flicker+Trap, Flicker+Block, Flicker+Shield,
  PulseGuard, SagGuard. Estos son candidatos de respaldo — no reemplazan a FlickerGuard
  en el deck principal a menos que el abogado confirme colision.

---

### Gate 6 — TripleLock colision sectorial seguridad fisica

- **Decision:** APROBADO CON CONTINGENCIA — proceder con TripleLock como candidato
  principal; Solenne prepara candidatos alternativos como contingencia.
- **Rationale:** El nombre TripleLock tiene el riesgo de "Lock" como raiz con alta
  presencia en seguridad fisica (clase 9 amplia). Sin embargo, (a) la funcion de bloqueo
  electronico de un rele de proteccion de motores es producte distinto de una cerradura
  o sistema de acceso; (b) el componente "Triple" lo especifica dentro de la logica de
  proteccion multifalla — contexto que no es propio de cerraduras; (c) la doctrina de
  equivalencia perceptual puede proteger la combinacion para equipo electrico si la
  busqueda no encuentra conflicto activo. El riesgo es real pero no alto suficiente para
  rechazar preventivamente sin busqueda formal. El path correcto es: flagear al abogado
  para busqueda prioritaria en subclase seguridad fisica clase 9, y tener candidatos
  alternativos listos.
- **Clausula RISK-POLICY:** RISK-POLICY v1.0 §4 (reversibilidad): mismo razonamiento que
  Gate 5 — la contingencia de candidatos alternativos de Solenne garantiza que si hay
  colision, el deck no se detiene.
- **Precedente BR-5 aplicado:** No hay precedente BR-5 especifico para colision de clase
  sectorial. Se aplica principio general: decision de riesgo no paralizante cuando el
  riesgo es navegable con contingencia.
- **Caveat literal a integrar en deck del abogado:**
  "TripleLock: nombre de fantasia en clase 9. La raiz 'Lock' tiene presencia en marcas
  de sistemas de seguridad fisica (cerraduras electronicas, control de acceso) en Clase 9.
  La busqueda fonética debe verificar si existen titulares activos con marcas que incluyan
  'TripleLock' o 'Triple Lock' en la subclase de dispositivos de seguridad o proteccion
  en SAPI Venezuela y en IMPI Mexico. La distincion de producto entre un rele de
  proteccion electrica para motores y un sistema de acceso fisico es argumento disponible
  ante el examinador si hay coexistencia en la misma clase Niza."
- **Implicacion para Solenne (Phase 4):** TripleLock es anchor de NODO-F. Solenne genera
  3 candidatos adicionales. Solenne debe incluir una fila de candidatos alternativos para
  NODO-F marcada como "contingencia sectorial", con raices que eviten "Lock": Gate,
  Hold, Block, Halt en el contexto de proteccion multifalla. Estos son candidatos de
  respaldo unicamente.

---

### Gate 7 — TaskMemory colision software clase 9

- **Decision:** APROBADO DIFERENCIADO POR JURISDICCION — candidato principal para
  SAPI Venezuela; Solenne prepara candidatos alternativos especificamente para IMPI
  Mexico donde el riesgo de colision con software es mas alto.
- **Rationale:** En SAPI Venezuela, la doctrina de equivalencia perceptual protege
  "TaskMemory" para el GRN-MV: el consumidor venezolano promedio que adquiere un
  rele de nivel de bombeo no asocia "TaskMemory" con software de gestion de procesos
  informaticos. El nodo NODO-G es verde en OL-1 (diferenciador sin equivalente en la
  competencia directa para el segmento) — el nombre tiene el soporte de un RTB real.
  En IMPI Mexico, el ecosistema tecnologico tiene mayor presencia de software y apps
  con nombres que pueden incluir "Task" y "Memory" en Clase 9 amplia. El riesgo de
  colision con marcas de software en IMPI es mayor que en SAPI. La estrategia correcta
  es diferenciar: usar TaskMemory como candidato principal para registro VE, y proveer
  candidatos alternativos sin la combinacion Task+Memory para registro MX. El abogado
  puede asesorar si presentar el mismo nombre en ambas jurisdicciones o candidatos
  distintos segun los resultados de busqueda.
- **Clausula RISK-POLICY:** RISK-POLICY v1.0 §3 y principio de no bloquearse por riesgo
  especulativo cuando existe RTB solido. El RTB del NODO-G (confirmado verde por Orlan,
  texto literal de HDE GRN-MV v9) es el mas limpio del portafolio para su segmento.
- **Precedente BR-5 aplicado:** No hay precedente BR-5 especifico para colision de
  jurisdiccion diferenciada. Se aplica principio de riesgo graduado por contexto regulatorio:
  misma marca puede tener distinto perfil de riesgo en diferentes jurisdicciones.
- **Caveat literal a integrar en deck del abogado:**
  "TaskMemory: nombre de fantasia para controlador de nivel de bombeo (GRN-MV). La
  combinacion 'Task' + 'Memory' tiene presencia en terminologia de software de gestion
  de procesos en informatica (class 9 amplia). La busqueda fonética debe priorizar la
  subclase de software y aplicaciones en IMPI Mexico para verificar si hay titulares activos
  con marcas similares. En SAPI Venezuela, la doctrina de equivalencia perceptual favorece
  la registrabilidad del nombre para el producto electrico (el consumidor de un rele de
  nivel de bombeo no percibe 'TaskMemory' como descriptor de software informatico). Se
  sugiere que el abogado evalúe si presentar un candidato alternativo especifico para
  IMPI MX si la busqueda encuentra conflicto en la subclase software."
- **Implicacion para Solenne (Phase 4):** TaskMemory es anchor de NODO-G para SAPI VE.
  Solenne genera 3 candidatos adicionales para el nodo. Adicionalmente, Solenne debe
  generar al menos 2 candidatos alternativos especificamente etiquetados "para IMPI MX
  si hay colision software" — con raices que eviten la combinacion Task+Memory: ModeKeep,
  StateHold, CycleResume, RetainMode. Estos no son candidatos de reemplazo para VE;
  son candidatos de contingencia para MX segun busqueda del abogado.

---

### Gate 8 — NODO-H Ecosystem GIO — candidatos sin terminos de protocolo estandar

- **Decision:** APROBADO — la instruccion de naming del Checkpoint 1 (no MODBUS, no
  terminos de protocolo estandar) es correcta y suficiente. La familia GIO es el territorio
  semantico mas limpio para los 4 candidatos del nodo. Bruna la confirma y sella.
- **Rationale:** El Ecosystem GIO (GIO PORT + GIO-Link + GIO-Tool) como denominacion
  propietaria es la distincion registrable en NODO-H. MODBUS RTU es protocolo abierto
  (Modbus Organization / Schneider Electric) — su uso en un nombre de marca es prohibicion
  absoluta. La familia GIO tiene fantasia establecida en el portafolio Genteca con uso
  comercial documentado en HDE y catalogos. Los 4 candidatos de Solenne anclados en
  la familia GIO-* tienen el mejor perfil de registro disponible para este nodo. Candidatos
  sin raiz GIO son posibles pero deben verificar que no usan terminologia de protocolo
  estandar (RS, SPI, I2C, Modbus, fieldbus, DeviceNet, EtherNet/IP, PROFIBUS, IO-Link).
- **Clausula RISK-POLICY:** RISK-POLICY v1.0 §3 (no afirmar como propio lo estandar).
  El nombre MODBUS es marca registrada de tercero. Derivados o combinaciones que
  evoquen MODBUS son prohibicion sin excepcion en este dominio.
- **Precedente BR-5 aplicado:** No hay precedente BR-5 especifico. El principio general
  de no usar marcas de tercero en nombres propios (equivalente semantico de BR-5 Precedente
  #3: no denigrar ni apropiar lo que pertenece a otro) aplica aqui.
- **Caveat literal a integrar en deck del abogado:**
  "Los candidatos de naming del NODO-H se anclan en la denominacion propietaria
  Ecosystem GIO (GIO PORT / GIO-Link / GIO-Tool) de Genteca. El protocolo de
  comunicacion subyacente es MODBUS RTU (estandar abierto — Modbus Organization).
  Los nombres candidatos no contienen ni aluden a MODBUS ni a ninguna denominacion
  de protocolo estandar. La documentacion formal del Ecosystem GIO como sistema
  diferenciado del protocolo estandar subyacente es un documento interno que I+D debe
  elaborar antes de la reunion con el abogado (confirmado en Checkpoint 1 gap 4)."
- **Implicacion para Solenne (Phase 4):** Los 4 candidatos del NODO-H deben anclar en
  la familia GIO o crear nombres para el ecosystem propietario sin aludir al protocolo
  subyacente. Instruccion del Checkpoint 1 Decision 1 es vinculante. Solenne tiene
  libertad de generacion dentro de ese espacio.

---

## Resumen ejecutivo de sello Bruna — Phase 3

| Gate | Nombre anchor | Decision | Accion para Solenne |
|------|--------------|----------|---------------------|
| 1 | Override gama | Aprobado con caveat de deck | Sin impacto en Phase 4 |
| 2 | ThermalCurve (NODO-D) | **RECHAZADO** | Generar 4 candidatos nuevos NODO-D |
| 3 | Thermo-Safe (NODO-C) | Aprobado con caveat Caso A | Generar 3 candidatos adicionales NODO-C |
| 4 | ForensLog (NODO-E) | Aprobado — postura Escenario A | Generar 3 candidatos adicionales NODO-E |
| 5 | FlickerGuard (NODO-B) | Aprobado con contingencia | Generar candidatos alt NODO-B marcados "contingencia OMPI" |
| 6 | TripleLock (NODO-F) | Aprobado con contingencia | Generar candidatos alt NODO-F marcados "contingencia sectorial" |
| 7 | TaskMemory (NODO-G) | Aprobado diferenciado por jurisdiccion | Generar 2 candidatos alt especificos para IMPI MX |
| 8 | Ecosystem GIO (NODO-H) | Aprobado — instruccion Checkpoint 1 confirmada | 4 candidatos anclados en familia GIO |

**Conteo de candidatos que Solenne genera en Phase 4:**
- 8 nodos x 4 candidatos = 32 candidatos base
- ThermalCurve rechazado: los 4 candidatos del NODO-D son todos nuevos (ninguno es anchor)
- Contingencias adicionales para Gates 5, 6, 7: Solenne genera las contingencias como
  filas extra en la Naming Bible — no aumentan el conteo base de 32

**Nombres anchor que pasan a Phase 4 confirmados:**
StaggerStart (NODO-A), FlickerGuard (NODO-B, con contingencia), Thermo-Safe (NODO-C,
con caveat Caso A), ForensLog (NODO-E), TripleLock (NODO-F, con contingencia),
TaskMemory (NODO-G, diferenciado por jurisdiccion).

**Nombre rechazado:** ThermalCurve (NODO-D). Solenne genera 4 candidatos nuevos.

---

*Bruna — BR-2 Phase 3 decision formal. Fecha: 2026-05-13.*
*Downstream: Solenne Phase 4 lee este documento como instruccion vinculante.*
*Carry-forward al deck: Vivienne integra los caveats literales de cada gate en los slides
correspondientes. El caveat del Gate 1 (override) va en la slide de metodologia o en nota
al pie del deck. Los caveats de Gates 3, 4, 5, 6, 7, 8 van en las notas del slide de cada
nodo — no en el cuerpo visible del slide.*
