---
doc_type: BR-1-risk-notes
project_id: portfolio-naming-ip-2026
domain: genteca
version: v1.0
author: Bruna
fecha: 2026-05-13
inputs_consultados:
  - 00-project-charter.md v1.0
  - 01-checkpoint-1-resolution.md
  - Vael_VA-1_messaging-architecture_v1.md
  - Vael_VA-5_guardrails_v1.md
  - Vera_VR-1_tech-inventory-hybrid_v1.md
  - Orlan_OL-1_differentiation-matrix_v1.md
  - RISK-POLICY.md v1.0 (2026-04-25)
  - BR-5 transversal (precedentes #1-#7, ultima actualizacion 2026-05-08)
  - BR-2 Genteca claim-approval-log v1 (entradas #1-#14, 2026-05-03/05-05)
  - reference_sapi_venezuela_quick.md
estado: notas_de_analisis — decision formal en BR-2
nota: >
  Este documento es analisis razonado gate por gate. No constituye decision formal.
  Las decisiones vinculantes estan en Bruna_BR-2_approval-set_v1.md.
  Ningun claim marcado como gate aqui pasa a produccion sin el sello del BR-2.
---

# BR-1 — Risk Notes
## Portfolio Naming IP 2026 (Genteca) — Phase 3

> Notas de analisis por gate. No son decisiones — son el razonamiento previo que
> fundamenta las decisiones del BR-2. El proposito es mostrar el trabajo de evaluacion
> y dejar trazabilidad para auditoria futura.

---

## Gate 1 — Override curva inversa universal de facto

**Claim objeto:** "La curva inversa I-t cold/hot y la curva inversa V-t algorítmica están
presentes en toda la gama Exceline / Exceline Profesional / Genius" — utilizado como base
para sostener que los nodos NODO-B y NODO-D aplican universalmente sin auditoría
producto por producto.

### Analisis de defendibilidad

El override es una decision estructural del Owner (charter §3 decision 4). Su proposito
operativo es evitar la paralizacion del proceso de naming por falta de auditoría exhaustiva
de HDE por producto — un costo de eficiencia razonable cuando el patron tecnico general
es coherente en la gama.

**Lo que el override NO hace:**

El override no convierte un claim descriptivo en claim diferenciador. Asumir que la
curva inversa I-t cold/hot existe en toda la gama no le da a Genteca diferenciacion sobre
la competencia, porque la misma funcion existe en Siemens 3RB3, Eaton C441, Schneider
LTMR y Rockwell E300 (todos verificados con fuente primaria o fuente primaria parcial
segun OL-1). El override es un shortcut para la auditoria interna; no es un argumento de
diferenciacion externo.

**Escenario 1: Override como base de naming de marca (no publicidad)**

Para el proposito de este proyecto — generar candidatos de nombre para registro ante
SAPI/IMPI — el override es funcionalmente suficiente. El examinador de SAPI/IMPI no
verifica si cada producto de la gama implementa la funcion. Lo que verifica es si el nombre
es o no descriptivo del producto, y si hay colision con marcas existentes. El override no
agrava ni mejora ese riesgo. En este escenario, el override es operativamente aceptable.

**Escenario 2: Override como claim en publicidad o en el deck del abogado**

Si Genteca publica en publicidad, empaque, o material comercial que "la curva inversa
esta presente en toda la gama", y luego hay un producto especifico de la gama en que
Vera no puede confirmar la funcion, el claim es factualmente incompleto. El riesgo no es
legal (no hay norma regulatoria venezolana que penalice el claim), sino de credibilidad:
un competidor o un especificador puede pedir la especificacion del producto especifico
y encontrar que el HDE no confirma la funcion.

**Escenario 3: Override en el contexto del deck para el abogado**

El deck de este proyecto es para un abogado marcario, no para publicidad. El abogado
no evalua si cada producto implementa la funcion; evalua si el nombre es registrable.
En este contexto, el override es irrelevante para el riesgo marcario. Lo que el abogado
evaluara es el nombre en si, no la cobertura de producto.

**Conclusion del analisis:**

El override es defendible para el proposito especifico de este proyecto (naming/IP).
No es defendible como claim de publicidad universal sin acotacion. La distincion es critica:
el deck para el abogado puede afirmar "la funcion esta presente en los productos Genius
verificados" sin reclamar universalidad. Si el deck quiere afirmar universalidad de gama,
necesita la acotacion "segun override Owner — pendiente auditoria producto por producto
por I+D".

**Riesgo de oposicion:**

En el contexto de registro de marca, ningun competidor puede oponerse al override porque
el override no es el nombre — es el RTB que el nombre describe. Si un competidor objeta
"ThermalCurve" por descriptividad, el argumento no es sobre si la funcion esta en toda
la gama, sino sobre si el nombre ThermalCurve describe literalmente la funcion estandar
IEC. El override no ayuda ni perjudica ese argumento.

---

## Gate 2 — ThermalCurve (NODO-D) descriptividad critica

**Nombre objeto:** ThermalCurve
**Nodo:** NODO-D — Curva inversa I-t diferenciada cold/hot
**Flag Orlan:** Rojo — funcion estandar IEC ubiqua en competencia industrial
**Flag Vael VA-5:** Gate critico — diferenciador algoritmico propietario o reemplazo del nombre

### Analisis de descriptividad

"ThermalCurve" = "Thermal" (termico, temperatura, calor) + "Curve" (curva). En el contexto
de relacion de proteccion de motores electricos, "curva termica" o "thermal curve" es la
denominacion tecnica estandar del mecanismo IEC 60947-4-1. No es metafora, no es
fantasia, no es neologismo: describe literalmente el mecanismo.

**Bajo doctrina SAPI (art. 34 LPI Venezuela):**

Una marca descriptiva del producto es inadmisible. "ThermalCurve" para un rele de
proteccion con curva inversa I-t es un caso de alta exposicion al rechazo por descriptividad.
El consumidor venezolano promedio puede no percibir "ThermalCurve" como descriptor
literal — aplica equivalencia perceptual. Pero un examinador tecnico de SAPI, al evaluar
la solicitud FM-02 para un dispositivo de proteccion en Clase 9, tiene criterio suficiente
para identificar que "Thermal" + "Curve" describe el mecanismo primario del producto.
La probabilidad de objecion es alta, no media.

**Bajo doctrina IMPI (Mexico):**

IMPI aplica criterios similares a los de SAPI para descriptividad. El riesgo es comparable
o mayor en Mexico porque el portfolio tecnico de la competencia es mas denso y hay mas
marcas en clase 9 de proteccion industrial que podrian ser referidas para comparacion.

**Pregunta critica: puede Vera documentar un diferenciador algoritmico propietario?**

Vera VR-1 documenta los RTBs tecnicos verificables de NODO-D:
- Curva caliente = curva fria / 3 (documentado en GIII+ HDE y relacion con IEC 60255-8)
- Clase termica ajustable 5-30 en pasos de 1 (documentado en GUCT+, GIII+, GSPT-MV)
- Memoria termica hasta 2 horas (documentado)
- Implementacion segun IEC 60255-8-1990 e IEEE C37.112-1996

El problema es que todos esos RTBs son especificaciones de la norma IEC/IEEE, no
parametros propietarios de Genteca. La razon "Caliente = Fria / 3" no es un algoritmo
propietario — es la forma estandar en que la norma define la curva caliente. El ajuste
de clase 5-30 es la clase de proteccion definida por IEC; el paso de 1 es una decision de
implementacion que otros fabricantes pueden tener igual. Vera no identifica ningun
parametro fuera del estandar IEC en VR-1. Orlan confirma el rojo.

**El override no ayuda en este gate:**

El override del Owner dice que la curva inversa I-t cold/hot se asume universal de facto en
la gama. Eso no crea un diferenciador — confirma que es una funcion estandar que todos
tienen. Para el gate de descriptividad, eso es un argumento en contra del nombre, no a favor.

**Alternativa: puede el nombre sobrevivir con una estrategia de marca?**

En teoria, una marca descriptiva puede igualmente registrarse si ha adquirido secondary
meaning — si el publico ya la asocia exclusivamente con Genteca. Pero "ThermalCurve"
no tiene uso previo publico documentado; no hay campana de marca que cree ese secondary
meaning. Esta salida no es viable en este proyecto.

**Conclusion del analisis:**

Vera VR-1 no documenta un diferenciador algoritmico propietario de NODO-D mas alla del
estandar IEC/IEEE. El checkpoint 1 deferia a Bruna exactamente esta decision. Sin RTB
propietario adicional que Vera pueda confirmar antes del cierre de Phase 3, el nombre
ThermalCurve tiene probabilidad alta de objecion por descriptividad en SAPI y en IMPI.

El nodo NODO-D sigue siendo un nodo registrable: la decision de reemplazar el nombre no
elimina el nodo. La curva inversa cold/hot es un nodo valido del portafolio (aunque sea
funcion estandar IEC — otros fabricantes no la tienen nombrada con fantasia). El nombre
es el problema, no el nodo.

---

## Gate 3 — Thermo-Safe Caso A/B

**Nombre objeto:** Thermo-Safe
**Nodo:** NODO-C — Modelo termico NTC integrado en protector monofasico
**Casos:** Caso A = empaque actual menciona NTC o proteccion termica visiblemente;
Caso B = empaque sin mencion NTC visible

### Analisis Caso A (empaque menciona NTC/proteccion termica)

El empaque actual de GSM-MB/RB/RE version V10/V9/V13 incluye "AHORA CON PROTECCION
TERMICA" confirmado en etiqueta empaque (Vera VR-1 §NODO-C). Esto es Caso A.

En Caso A, el empaque ya comunica la funcion termica. Si Thermo-Safe se registra como
marca de esa funcion, el examinador SAPI puede argumentar que el nombre coincide con
la funcion ya comunicada en el empaque — reforzando el argumento de descriptividad
("Thermo" = termico = lo que el empaque ya llama "PROTECCION TERMICA").

Sin embargo, "Thermo-Safe" como combinacion no es "Proteccion Termica": "Safe" no
es "Protection" ni es "Termica" — la combinacion tiene fantasia suficiente para distinguirla
de la descripcion funcional literal. La doctrina de equivalencia perceptual SAPI favorece
esta lectura: el consumidor venezolano promedio no percibe "Thermo-Safe" como
"Proteccion Termica Segura" de forma inmediata. La memoria SAPI confirma que Thermo-Safe
tiene mejor perfil que alternativas como "ThermoShield" (mas saturado) o "Escudo Termico
NTC" (directamente descriptivo).

Impacto del Caso A en el riesgo: incrementa el riesgo de descriptividad a nivel
"medio-alto" (vs "medio" en Caso B). No lo hace indefendible, pero obliga a que el
argumento ante el abogado incluya la distincion semantica entre el claim del empaque y
el nombre de fantasia.

### Analisis Caso B (empaque sin mencion NTC visible)

En Caso B, el nombre Thermo-Safe no tiene el empaque como evidencia corroborativa de
descriptividad. El perfil baja a "medio". El argumento de fantasia del nombre es mas limpio.

### Situacion real de evidencia disponible

Vera VR-1 confirma que el empaque actual ES Caso A (menciona proteccion termica). No
hay evidencia de una version del empaque sin esa mencion. Por tanto, la hipotesis Caso B
es teorica — la realidad operativa del proyecto es Caso A.

**Consecuencia practica:**

El deck del abogado debe trabajar sobre Caso A. No hay fundamento para asumir Caso B
a menos que Genteca cambie el empaque antes del registro. Esa decision es del Owner,
no de Bruna. Bruna da su sello sobre Caso A y lo anota como postura; si el Owner decide
cambiar el empaque (eliminando la mencion), la postura puede revisarse.

---

## Gate 4 — ForensLog RTB calibration

**Nombre objeto:** ForensLog
**Nodo:** NODO-E — Registro forense historico de fallas con timestamp
**Cuestion:** el nombre "ForensLog" se sostiene mejor acotado a GIII+MV (100 fallas, RTB
limpio) o ampliado a toda la gama Genius (20-100 fallas segun producto).

### Analisis de riesgo por escenario

**Escenario A: ForensLog acotado a GIII+MV**

- RTB: "100 ultimas fallas con timestamp" — dato verificado en HDE GIII+MV-V1 (HDE
  ingles y espanol). Unico producto de la competencia con registro comparable identificado:
  Rockwell E300 con 10 registros (5 trips + 5 warnings) — la diferencia de 10:1 es
  defendible como claim cuantitativo superior (aplica BR-5 Precedente #1: superlativo con
  dato cuantitativo en mercado con opacidad).
- Riesgo de naming: bajo. El nombre ForensLog no afirma "toda la gama Genius" — solo
  nombra la funcion. El registro de 100 fallas es el RTB del nombre, no del nombre de
  la gama.
- Riesgo de colisión de nombre en clase 9: el riesgo existe (software, apps de diagnostico
  — ver Gate 7 de este analisis) pero es independiente del RTB de 100 fallas.
- Recomendacion de riesgo: escenario A es el mas limpio desde el punto de vista de
  defensa del RTB ante el abogado.

**Escenario B: ForensLog ampliado a gama Genius**

- RTB: "hasta 100 fallas en GIII+MV / 20 fallas en gama Genius" — pierde la potencia del
  claim de 100 fallas como diferenciador del nombre. El claim se fragmenta.
- Riesgo de naming: el nombre ForensLog no tiene un RTB unico defendible. El abogado
  puede preguntar: ¿cuantas fallas exactamente? La respuesta "depende del producto"
  debilita el argumento de que el nombre tiene un RTB especifico y propietario.
- Riesgo de colision de nombre en clase 9: identico al Escenario A.
- El escenario B no produce nombres diferentes para la decision de registro; produce el
  mismo nombre con un RTB mas debil.

**Conclusion del analisis:**

El Escenario A (acotar a GIII+MV) produce el argumento mas solido ante el abogado
marcario. El nombre ForensLog descansa sobre un RTB cuantitativo unico (100 fallas en
GIII+MV) que tiene comparativo verificado con la competencia. El Escenario B no tiene
esa ventaja y produce ambiguedad en el deck.

Sin embargo, la decision de que nombre usar para el nodo (y si acotarlo a GIII+MV o
ampliar a la gama) es una decision de posicionamiento comercial que el charter asigno
a Solenne en Phase 4, con el contexto de este analisis de riesgo de Bruna. Bruna da su
postura de riesgo; Solenne decide el nombre.

---

## Gate 5 — FlickerGuard OMPI / colision productos LED

**Nombre objeto:** FlickerGuard
**Nodo:** NODO-B — Deteccion sub-ciclo de perturbaciones de voltaje
**Flag BR-2 previo:** Busqueda OMPI ampliada pendiente (proyectos marcas-anglicismos)
**Producto colisionante potencial:** productos LED (iluminacion) en Australia y UK con
nombre "FlickerGuard" o "Flicker Guard"

### Analisis del riesgo de colision

**Clase 9 es la clase correcta para Genteca.** Los supervisores de voltaje y relaciones de
proteccion electrica caen en Clase 9 Niza (confirmado en reference_sapi_venezuela_quick.md
y en el charter §1). Los productos LED tambien pueden caer en Clase 9 Niza (aparatos e
instrumentos electricos). El solapamiento de subclase existe en teoria.

**Sin embargo, la doctrina SAPI y la practica IMPI para coexistencia:**

La Ley de Propiedad Industrial venezolana y la legislacion mexicana de marcas no utilizan
el concepto de subclase con la rigidez que el sistema de la Union Europea aplica. En SAPI
Venezuela, la coexistencia de dos marcas identicas o similares en la misma clase Niza puede
ocurrir si los productos son suficientemente distintos en naturaleza y en el tipo de
consumidor (distincion de segmento). Un producto LED para control de flicker en iluminacion
y un supervisor de voltaje monofasico para proteccion de compresores son productos distintos
en naturaleza, en canal de distribucion, y en audiencia. El riesgo de confusion del consumidor
es bajo.

**Riesgo real:**

El riesgo no es que el consumidor venezolano o mexicano confunda un protector de compresor
con una luminaria LED australiana. El riesgo es que el titular australiano o britanico del nombre
"FlickerGuard" en clase 9 tenga registro OMPI (Sistema de Madrid) que incluya a Venezuela
o Mexico, y presente oposicion al momento de la solicitud.

**Evaluacion practica:**

- Si el titular LED tiene registro OMPI que designa Venezuela o Mexico: hay base de oposicion
  aunque sea debil por distincion de producto.
- Si el titular LED no tiene registro OMPI que designa Venezuela o Mexico: no hay base de
  oposicion en esas jurisdicciones. El nombre esta disponible.
- Si el titular LED tiene registro en Australia/UK pero NO en SAPI/IMPI: Genteca puede
  registrar en VE y MX sin conflicto inmediato.

Esta evaluacion requiere busqueda formal en el sistema WEBPI SAPI y en el sistema IMPI
de Mexico, mas consulta OMPI para designaciones. Esa busqueda es trabajo del abogado
marcario, no de Bruna. Bruna evalua el riesgo conceptual y la estrategia; el abogado
confirma la busqueda.

**Conclusion del analisis:**

El riesgo de colision de FlickerGuard con productos LED es real pero navegable. La
coexistencia en clase 9 entre un protector de voltaje y una luminaria LED es un caso de
distincion de producto que los sistemas SAPI/IMPI pueden resolver. El path correcto es:
(a) proceder con FlickerGuard como candidato, (b) flagear al abogado la existencia de
productos LED con nombre similar para que busqueda OMPI lo priorice, (c) si la busqueda
encuentra conflicto real, Solenne tiene candidatos alternativos en territorio semantico
adyacente. Solenne debe preparar candidatos alternativos en Phase 4 como contingencia.

---

## Gate 6 — TripleLock colision sectorial seguridad fisica

**Nombre objeto:** TripleLock
**Nodo:** NODO-F — Bloqueo permanente tras tercera falla de corriente recurrente
**Flag BR-2 previo:** Busqueda sectorial seguridad fisica pendiente

### Analisis del riesgo de colision

"TripleLock" tiene dos componentes semanticos:
- "Triple": descriptor numerico (tres). Descriptivo de la funcion (tres fallas = bloqueo).
- "Lock": termino con alta presencia en seguridad fisica (cerraduras electronicas, antirrobo,
  sistemas de acceso, software de seguridad). En clase 9 Niza: cerraduras electronicas,
  dispositivos de seguridad fisica, software de seguridad — todos clase 9.

**Riesgo de descriptividad del nombre para el producto electrico:**

"Triple" es un numero — en SAPI, los numerales descriptivos del producto tienen riesgo
de rechazo (el nombre describe que el bloqueo ocurre tres veces). Sin embargo, la combinacion
"TripleLock" no es inmediatamente descriptiva para el consumidor promedio venezolano: "lock"
no es uso cotidiano en espanol para bloqueo electrico de rele. La doctrina de equivalencia
perceptual puede proteger la combinacion.

**Riesgo de colision con marcas de seguridad fisica:**

"Lock" como raiz tiene presencia elevada en nombres de cerraduras electronicas, dispositivos
anti-robo, y software de seguridad — todos en clase 9 Niza. La busqueda OMPI/SAPI puede
encontrar marcas como "TripleLock" o similares en ese espacio. Si hay un titular de cerradura
electronica o sistema de acceso con marca "TripleLock" registrada en clase 9, hay base de
oposicion incluso si los productos son distintos, porque la clase Niza es la misma.

**Distincion de producto como argumento:**

La distincion de producto entre un rele de proteccion de motores y una cerradura electronica
es clara. Sin embargo, en jurisdicciones con aplicacion estricta de unicidad de clase, la
distincion de producto no siempre es argumento suficiente si la marca es identica o muy
similar. El resultado dependera de si hay titulares activos en SAPI/IMPI con ese nombre
en clase 9.

**Conclusion del analisis:**

El riesgo de TripleLock no es el mas alto del portafolio (ese es ThermalCurve) pero es
real. La estrategia correcta es: (a) proceder con TripleLock como candidato, (b) flagear
al abogado la necesidad de busqueda en subclase de seguridad fisica clase 9, (c) Solenne
prepara candidatos alternativos en Phase 4 con raices que eviten "Lock" (Gate, Hold, Block,
Halt) como contingencia.

---

## Gate 7 — TaskMemory colision software clase 9

**Nombre objeto:** TaskMemory
**Nodo:** NODO-G — Memoria de estado y reanudacion de tarea post-corte
**Flag BR-2 previo:** Colision con clase 9 software/apps critica (marcas-anglicismos)

### Analisis del riesgo de colision

"Task Memory" es un termino tecnico en informatica: la memoria asignada a un proceso o
tarea en un sistema operativo. "Task memory management" es concepto estandar en OS
design (Windows Task Manager, Linux task scheduler). Si existe software en clase 9 con
ese nombre o similar, el riesgo de oposicion es alto.

**En SAPI Venezuela:**

La doctrina de equivalencia perceptual puede proteger "TaskMemory" para un rele de nivel
de bombeo: el consumidor venezolano promedio que compra un GRN-MV no asocia "Task
Memory" con software de gestion de procesos. La percepcion seria mas cercana a "memoria
de tareas" en sentido amplio, no en sentido informatico especifico.

**En IMPI Mexico:**

Mexico tiene un ecosistema tecnologico mas robusto. La presencia de software de gestion
de proyectos y aplicaciones con nombres que incluyan "Task" y "Memory" es mas probable.
El riesgo de colision con marcas de software en clase 9 es mayor en Mexico que en Venezuela.
IMPI tiende a aplicar criterios mas cercanos a los de USPTO que SAPI.

**El riesgo principal es de colision, no de descriptividad:**

Para el producto electrico (GRN-MV), "TaskMemory" no es descriptivo desde la perspectiva
del consumidor venezolano promedio (cumple equivalencia perceptual). El problema no es
que el nombre describa el producto electrico de forma obvia — es que puede chocar con
software ya registrado bajo ese nombre en clase 9 amplia.

**Conclusion del analisis:**

TaskMemory es un candidato que puede sobrevivir en SAPI Venezuela con argumento de
equivalencia perceptual y distincion de producto. En IMPI Mexico el riesgo de colision con
software es mayor. La estrategia correcta es: (a) proceder con TaskMemory como candidato
primario para SAPI VE, (b) Solenne genera candidatos alternativos para IMPI MX en Phase 4
que eviten la combinacion Task+Memory, (c) flagear al abogado para busqueda prioritaria
en subclase software clase 9 en ambas jurisdicciones.

---

## Gate 8 — NODO-H Ecosystem GIO / candidatos sin terminos de protocolo estandar

**Nodo:** NODO-H — Ecosystem GIO (Conectividad industrial integrada)
**Cuestion:** que tipo de nombre alrededor de GIO es defendible como marca vs descriptivo,
dado que el protocolo subyacente (MODBUS RTU) es estandar abierto no registrable.

### Analisis de la distincion registrable / descriptivo en NODO-H

**Lo que es estandar y no registrable:**
- MODBUS, MODBUS RTU, RS-485, RS-232: protocolos y estandares de la industria.
  El nombre MODBUS es marca registrada de Schneider Electric / Modbus Organization.
  Usarlo en un nombre de marca es prohibicion absoluta.
- "Industrial connectivity", "remote monitoring", "fieldbus": descriptivos genericos.

**Lo que es propiedad de Genteca:**
- GIO PORT: interfaz fisica propietaria de conexion en los reles Genius.
- GIO-Link: familia de accesorios (adaptadores USB/RS-232/RS-485) propietarios.
- GIO-Tool: software propietario de monitoreo.
- "Ecosystem GIO": denominacion propietaria del conjunto (confirmada en Checkpoint 1).

**Perfil de registro del ecosistema GIO:**

La familia "GIO" ya tiene uso comercial documentado (GIO PORT, GIO-Link, GIO-Tool aparecen
en HDEs y catalogos Genteca). Si GIO-Link y GIO-Tool tienen uso comercial previo sostenido,
Genteca puede aplicar TM desde ya (no requiere certificado SAPI para el simbolo TM).
Para el registro formal (certificado), la familia GIO tiene buen perfil:
- "GIO" es signo de fantasia (no es descriptor del producto electrico en espanol).
- Las combinaciones GIO-Port, GIO-Link, GIO-Tool son nombres de fantasia con raiz
  compartida — estructura de familia de marcas que SAPI y IMPI reconocen.

**Riesgo de descriptividad para candidatos del NODO-H:**

Un candidato que use "Connect", "Net", "Link" + descripcion de la red puede caer en
descriptividad. Un candidato que use "GIO" como raiz compartida tiene el perfil mas
limpio porque "GIO" ya tiene fantasia establecida en el portafolio Genteca.

**Candidatos con raiz GIO:**

Cualquier combinacion GIO-[sufijo fantastico] es defendible porque la raiz "GIO" ya tiene
el perfil de fantasia y uso previo. El sufijo no debe describir el protocolo estandar.

**Candidatos sin raiz GIO:**

Si Solenne propone candidatos alternativos sin raiz GIO, deben evitar todo el espacio
semantico de protocolo estandar (MODBUS, fieldbus, RS, SPI, I2C, etc.) y todo descriptor
de red industrial (IndustrialLink, NetRelay, RemoteRelay — todos tienen riesgo de
descriptividad).

**Conclusion del analisis:**

Los 4 candidatos de Solenne para NODO-H tienen el path mas limpio si anclan en la familia
GIO. Candidatos sin raiz GIO son posibles pero requieren mas cuidado. La instruccion del
Checkpoint 1 Decision 1 es precisa y correcta: no MODBUS, no terminos de protocolo
estandar. La raiz GIO es la via de menor riesgo.

---

## Nota sobre precedentes BR-5 buscados y no encontrados

El brief de esta asignacion menciona "3 precedentes nuevos del proyecto marcas-anglicismos
previo (BR-5 #7, #8, #9)". El archivo BR-5 consultado
(`04-system/03-governance/BR-5_regla-claims-superlativos-mercados-opacos_2026-05-03.md`,
ultima actualizacion 2026-05-08) contiene precedentes #1 a #7 inclusive. No se encontraron
entradas #8 y #9 en ese archivo. El BR-2 Genteca (`2026-05-03_genteca_claim-approval-log_v1.md`)
llega hasta entrada #14 (2026-05-05). Si los precedentes #8 y #9 existen, estan en un
documento no encontrado en esta sesion. Bruna aplica los precedentes #1-#7 disponibles.
Ninguna decision de este BR-1/BR-2/BR-3 queda sin fundamento por esa ausencia — los
precedentes disponibles son suficientes para todos los gates.

---

*Bruna — BR-1 Phase 3 completo. Decisiones formales en BR-2. Fecha: 2026-05-13.*
