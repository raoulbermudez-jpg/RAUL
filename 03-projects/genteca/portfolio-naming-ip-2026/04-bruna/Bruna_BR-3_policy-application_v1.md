---
doc_type: BR-3-policy-application
project_id: portfolio-naming-ip-2026
domain: genteca
version: v1.0
author: Bruna
fecha: 2026-05-13
referencia_notas: Bruna_BR-1_risk-notes_v1.md
referencia_decisiones: Bruna_BR-2_approval-set_v1.md
nota: >
  Este documento es el dossier de auditoria. Explica que clausula de RISK-POLICY se aplic
  en cada gate con decision condicionada o rechazada, y por que. Si el Owner o un abogado
  externo cuestiona una decision despues, este doc da el rationale completo.
---

# BR-3 — Policy Application Notes
## Portfolio Naming IP 2026 (Genteca) — Phase 3

> Dossier de aplicacion de RISK-POLICY y precedentes BR-5 por gate.
> Solo se documentan los gates con decision condicionada (con caveat) o rechazada.
> Gate 8 (NODO-H, aprobado limpio con instruccion Checkpoint 1) no requiere entrada
> en este documento porque no hay clausula de riesgo que lo condicione.

---

## Entrada 1 — Gate 1: Override curva inversa universal de facto

**Decision:** Aprobado con caveat (aplicacion acotada)

**Clausula RISK-POLICY aplicada:**

RISK-POLICY v1.0 §3 — Manejo de errores y afirmaciones sostenibles. Aunque §3 describe
errores de ejecucion, el principio subyacente ("no afirmar datos que puedan ser falsos si son
verificables") se extiende a claims de cobertura de funcion tecnica. El override es una
asuncion del Owner, no una verificacion de Vera por cada producto. Afirmar en un documento
externo que la curva inversa es "universal de gama" sin la verificacion producto por producto
crea el riesgo de que el abogado, ante la pregunta del examinador SAPI, no pueda proveer
la HDE de un producto especifico que confirme la funcion. Eso no es un riesgo legal — es un
riesgo de credibilidad y de proceso de registro.

**Razonamiento de aplicacion:**

El charter §3 decision 4 es una decision estructural del Owner que Bruna no puede revertir.
Lo que Bruna puede hacer es acotar la afirmacion en el deck del abogado para que el abogado
no la presente como hecho auditado cuando no lo es. La clausula §3 de RISK-POLICY exige
que los errores (en este caso, la brecha entre la asuncion y la auditoria formal) se
transparenten al Owner y no se traten como estado resuelto cuando no lo estan. La forma
de cumplir este requisito sin frenar el proyecto es el caveat de deck: el abogado recibe
la informacion precisa sobre el estado de la auditoria y puede gestionar la presentacion
ante el examinador SAPI/IMPI con esa distincion.

**Por que no se rechazo:**

El override no compromete la registrabilidad de los nombres. El examinador SAPI/IMPI no
verifica si cada producto de la gama implementa la funcion nombrada. El riesgo del override
es en publicidad futura, no en el proceso de registro actual. Rechazar el override como
herramienta del deck habria paralizado el proyecto sin beneficio proporcional.

**Precedente BR-5 analogia aplicada:**

BR-5 Precedente #1 (claim con dato cuantitativo en mercado opaco aprobado con caveat):
la logica es que cuando el Owner avala el hecho tecnico y el riesgo de que ese hecho sea
incorrecto esta acotado (el riesgo del override es operativo/credibilidad, no legal), el
claim es aprobable con caveat que aclara el estado de la auditoria. Misma estructura: dato
aceptado con caveat de condicion de verificacion pendiente.

---

## Entrada 2 — Gate 2: ThermalCurve rechazado

**Decision:** Rechazado

**Clausula RISK-POLICY aplicada:**

RISK-POLICY v1.0 §3 — Manejo de afirmaciones sostenibles. El principio de no afirmar como
propio (o como distinguible) lo que es estandar de industria aplica en forma directa. Registrar
ThermalCurve como marca de Genteca cuando el nombre describe literalmente el mecanismo
IEC estandar que todos los relaciones de sobrecarga implementan es equivalente a afirmar
propiedad sobre terminologia estandar de la industria. Aunque eso es legalmente posible en
teoria (las marcas pueden ser descriptivas si adquieren secondary meaning), no es sostenible
en la practica en este proyecto porque no hay secondary meaning previo y el mecanismo es
ubiquo en la competencia.

**Razonamiento de aplicacion:**

La norma IEC 60947-4-1 define la curva de disparo inversa I-t como el mecanismo estandar
de relaciones de proteccion de sobrecarga. La norma IEC 60255-8 / IEEE C37.112 define los
parametros del algoritmo de imagen termica con distincion cold/hot. Todos los fabricantes
relevantes (Siemens 3RB3, Eaton C441, Schneider LTMR, Rockwell E300) implementan esta
funcion. El nombre "ThermalCurve" describe literalmente ese mecanismo: "Thermal" = termico
= propiedad termica de la curva; "Curve" = la curva I-t de disparo. Un examinador tecnico
de SAPI que evalua una solicitud de marca para un rele de proteccion en Clase 9 tiene
criterio suficiente para identificar que "ThermalCurve" describe el mecanismo primario del
producto que la marca pretende distinguir. El art. 34 LPI Venezuela (causales de
inadmisibilidad por descriptividad) es el argumento de oposicion disponible al examinador.

Vera VR-1 no identifico ningun parametro de la implementacion Genteca que exceda el
estandar IEC: la relacion "caliente = fria / 3" es la especificacion del estandar; el ajuste
de clase 5-30 es decision de implementacion estandar; la memoria termica de 2 horas es
parametro del estandar. Sin RTB propietario que diferencie la implementacion Genteca del
estandar IEC, no hay argumento para defender el nombre ante un examinador que objete
por descriptividad.

**Por que no se condiciono (en lugar de rechazar):**

El camino de condicionamiento hubiera requerido que Vera pueda documentar un diferenciador
propietario antes del cierre de Phase 3. El checkpoint 1 ya deferia a Bruna exactamente
esta decision. Vael VA-5 identifica el gate como "critico". No hay RTB adicional disponible
en VR-1. Condicionar sin RTB seria diferir la decision a Phase 4 o 5, lo que no tiene
ventaja: Solenne no puede generar los 4 candidatos del NODO-D sin saber si ThermalCurve
sigue como anchor o no. La decision de rechazo permite a Solenne arrancar Phase 4 con
claridad. La condicion de reapertura esta definida en BR-2 Gate 2 si Vera eventualmente
confirma un RTB propietario — pero ese evento no puede bloquear Phase 4 hoy.

**Precedente BR-5 aplicado:**

BR-5 Precedente #2 (superlativo de exclusion rechazado por ausencia de verificacion de
ausencia del atributo en competidores). Analogia: el nombre ThermalCurve implicitamente
"reclamaría" el mecanismo de curva termica como distintivo de Genteca. Pero el mecanismo
esta presente y documentado en toda la competencia relevante. La analogia con el Precedente
#2 es directa: no se puede reclamar como distinguible (o potencialmente exclusivo en el
naming) algo cuya presencia en la competencia esta verificada.

---

## Entrada 3 — Gate 3: Thermo-Safe Caso A con caveat

**Decision:** Aprobado con caveat (Caso A asumido)

**Clausula RISK-POLICY aplicada:**

RISK-POLICY v1.0 §3 (no afirmar datos que puedan ser falsos) + principio de caveat literal
cuando el riesgo es medio-alto pero no bloqueante. El riesgo de descriptividad de Thermo-Safe
es medio-alto en Caso A (el empaque ya comunica "PROTECCION TERMICA") — no bloqueante
porque la combinacion "Thermo-Safe" tiene fantasia suficiente bajo doctrina de equivalencia
perceptual. Sin embargo, afirmar ante el abogado que el nombre no tiene riesgo de
descriptividad en Caso A seria incorrecto. El caveat proporciona al abogado la distincion
semantica precisa que necesita para construir su argumento ante SAPI.

**Razonamiento de aplicacion:**

El riesgo de descriptividad de "Thermo-Safe" en Caso A se origina en que el empaque del
producto usa "PROTECCION TERMICA" como descriptor funcional visible, y un examinador
tecnico podria argumentar que el nombre de marca describe la misma funcion que el empaque
ya comunica como descripcion funcional. La contra-argumentacion disponible: "Thermo-Safe"
no es la traduccion al ingles de "PROTECCION TERMICA" — "Safe" no equivale a "Proteccion";
la combinacion crea un signo de fantasia distinto de la descripcion funcional en espanol.
Esta distincion semantica es el argumento de defensa ante SAPI bajo art. 34 LPI Venezuela
(no es descriptiva si no describe literalmente el producto en el idioma de uso comun del
consumidor venezolano). El caveat formaliza ese argumento para el abogado.

La decision de no rechazar descansa en: (a) la memoria SAPI previa confirma que Thermo-Safe
tiene mejor perfil de registro que alternativas mas descriptivas; (b) en el BR-2 Genteca
previo (entradas #4 y #5, 2026-05-03) la funcion termica NTC fue aprobada con caveats para
empaque; (c) el charter §2 filosofia del proyecto especifica "documento limpio sobre
completitud defensiva" — un rechazo preventivo de Thermo-Safe sin RTB que lo requiera
contradice esa filosofia.

**Precedente BR-5 aplicado:**

BR-5 Precedente #1 (claim aprobado con caveat cuando el RTB propio es sostenible y el
mercado no tiene comparativo que lo refute). La equivalencia: Thermo-Safe tiene perfil de
fantasia sostenible bajo doctrina de equivalencia perceptual; el mercado no tiene una marca
equivalente que cree confusion directa (Orlan OL-1 confirma que ninguna de las marcas de
la competencia usa "Thermo-Safe"). El caveat es el instrumento correcto.

---

## Entrada 4 — Gate 4: ForensLog con caveat de RTB

**Decision:** Aprobado con caveat (postura Escenario A recomendada)

**Clausula RISK-POLICY aplicada:**

RISK-POLICY v1.0 §3 (no afirmar datos que puedan ser falsos). El RTB "100 fallas" es
verdadero para el GIII+MV; no es verdadero como RTB universal de "toda la gama Genius".
Si el deck del abogado presenta ForensLog con el claim "registro de hasta X fallas en toda
la gama Genius" sin acotacion por producto, y el abogado pregunta sobre la gama completa,
la respuesta correcta seria "20 fallas en la mayoria de productos, 100 fallas en el GIII+MV"
— lo cual debilita el argumento de diferenciacion. La clausula §3 obliga a que el dato
presentado al abogado sea el dato correcto: el claim de ForensLog descansa sobre el GIII+MV.

**Razonamiento de aplicacion:**

El charter §2 filosofia del proyecto dice "pocos nombres fuertes con alta probabilidad de
registro, no muchos con muchas advertencias." El Escenario A (ForensLog acotado a GIII+MV)
es la formulacion mas fuerte porque el RTB es inequivoco: 100 fallas, dato verificado en
HDE primaria, comparativo verificado con Rockwell E300 (10 registros). El Escenario B
(ampliar a gama Genius) produce un RTB fragmentado que el abogado debe matizar — lo que
va en contra de la filosofia del proyecto. RISK-POLICY §3 y la filosofia del charter apuntan
en la misma direccion: usar el dato mas solido y mas especifico.

**Precedente BR-5 aplicado:**

BR-5 Precedente #1 (superlativo con dato cuantitativo verificado aprobado en mercado con
opacidad). Las tres condiciones del precedente se cumplen para ForensLog en Escenario A:
(1) el dato de 100 fallas en GIII+MV esta verificado en HDE primaria; (2) ningun competidor
tiene dato publicado igual o superior en el segmento directo (Rockwell E300 tiene 10 — la
diferencia es documentada); (3) la formulacion combina el nombre con el RTB cuantitativo.

---

## Entrada 5 — Gate 5: FlickerGuard con contingencia OMPI

**Decision:** Aprobado con contingencia (candidatos alternativos obligatorios)

**Clausula RISK-POLICY aplicada:**

RISK-POLICY v1.0 §4 — Reversibilidad. Antes de ejecutar una accion con riesgo (en este
caso, presentar FlickerGuard como candidato principal sin contingencia), el principio de
reversibilidad requiere evaluar: ¿es reversible? Si la busqueda OMPI del abogado confirma
colision activa y no hay candidatos alternativos listos, el deck requiere una nueva vuelta de
Phase 4 — que es costosa en tiempo. La contingencia de candidatos alternativos preparados
por Solenne en Phase 4 garantiza la reversibilidad: si hay colision, los alternativos toman
el lugar sin reabrir el proceso. La clausula §4 se aplica como instruccion de mitigacion, no
como razon de rechazo.

**Razonamiento de aplicacion:**

El riesgo de colision de FlickerGuard con productos LED es real (evidencia de nombres similares
en Australia/UK segun OL-1 Orlan y BR-2 previo del proyecto marcas-anglicismos). Sin
embargo, el riesgo no es certeza de colision — depende de si el titular LED tiene registro
OMPI que designe Venezuela o Mexico. La busqueda formal del abogado es el paso que resuelve
la incertidumbre. Rechazar el nombre preventivamente por un riesgo que puede no materializarse
seria excesivamente restrictivo y contradice el charter §2 y la instruccion del Owner a Bruna
("no detengas — ajusta / condiciona").

La contingencia no es un rechazo diferido; es la accion que garantiza que el proyecto no se
frena si la busqueda confirma el riesgo. RISK-POLICY §4 y el charter estan alineados: preparar
la contingencia es la respuesta correcta.

**Precedente BR-5 aplicado:**

BR-5 Precedente #1 (superlativo con RTB cuantitativo verificado aprobado). El RTB del
NODO-B (20ms, spec única verificada en segmento directo segun OL-1 verde) es el diferenciador
mas solido del portafolio. FlickerGuard descansa sobre ese RTB. La aprobacion con contingencia
preserva ese RTB en el deck mientras la incertidumbre de colision se resuelve con busqueda
formal.

---

## Entrada 6 — Gate 6: TripleLock con contingencia sectorial

**Decision:** Aprobado con contingencia

**Clausula RISK-POLICY aplicada:**

Identica a Gate 5: RISK-POLICY v1.0 §4 — Reversibilidad. La presencia de "Lock" en nombres
de seguridad fisica en clase 9 es un riesgo documentado en OL-1 y en el BR-2 previo del
proyecto marcas-anglicismos. Sin busqueda formal en SAPI/IMPI por el abogado, la colision
es posibilidad, no certeza. La contingencia de candidatos alternativos preparados por Solenne
(con raices Gate, Hold, Block, Halt) garantiza reversibilidad sin frenar Phase 4.

**Razonamiento de aplicacion:**

TripleLock tiene RTB solido en NODO-F: el bloqueo tras tres fallas de corriente en 30 minutos
esta verificado en multiples HDEs (GIII+ seccion E, GOC seccion E, catalogos Genius y
trifasico). El nombre tiene fantasia para el consumidor del producto electrico (la funcion
de bloqueo de un rele no es percibida como "cerradura" por el instalador venezolano o
mexicano). El riesgo no es de descriptividad del producto electrico — es de colision con
titulares de marcas en seguridad fisica que usen "Lock" como raiz. La busqueda del abogado
es el paso que resuelve. Mientras tanto, la contingencia protege la continuidad del proyecto.

**Precedente BR-5 aplicado:**

No hay precedente BR-5 especifico para colision de clase sectorial. Se aplica el principio
general de RISK-POLICY §4: la contingencia de candidatos alternativos es la accion de
mitigacion correcta ante riesgo de colision no confirmado.

---

## Entrada 7 — Gate 7: TaskMemory diferenciado por jurisdiccion

**Decision:** Aprobado diferenciado por jurisdiccion (candidatos alternativos para IMPI MX)

**Clausula RISK-POLICY aplicada:**

RISK-POLICY v1.0 §3 (no afirmar como aprobado para todas las jurisdicciones lo que tiene
riesgo diferenciado por jurisdiccion) + §4 (reversibilidad: preparar candidatos alternativos
para la jurisdiccion de mayor riesgo). En SAPI Venezuela el riesgo de colision software es
bajo (doctrina de equivalencia perceptual). En IMPI Mexico el riesgo es mayor (ecosistema
tecnologico mas denso, criterio IMPI mas cercano a USPTO para software en clase 9). Aplicar
la misma decision para ambas jurisdicciones sin distinguir seria impreciso — una aprobacion
plana para "SAPI + IMPI" con el mismo nivel de riesgo seria incorrecta para IMPI Mexico.

**Razonamiento de aplicacion:**

La doctrina SAPI de equivalencia perceptual es un criterio especifico de Venezuela que no
opera de forma identica en Mexico. IMPI Mexico aplica criterios mas conservadores para
nombres que pueden ser confusamente similares con software en clase 9. La combinacion
Task + Memory puede encontrar conflicto con apps o software de gestion de tareas en el
registro IMPI — un riesgo que SAPI puede absorber con el argumento de equivalencia
perceptual para el consumidor venezolano del GRN-MV, pero que IMPI puede no absorber
de la misma manera.

La solucion no es rechazar TaskMemory — el NODO-G tiene el RTB mas limpio del portafolio
(verde en OL-1, texto literal de HDE, sin equivalente nombrado en la competencia). Es
aprobar con la distincion de jurisdiccion y preparar la contingencia para Mexico. Eso
cumple RISK-POLICY §3 (la decision es precisa para cada contexto) y §4 (hay candidatos
alternativos si Mexico requiere nombre diferente).

**Precedente BR-5 aplicado:**

No hay precedente BR-5 especifico para riesgo diferenciado por jurisdiccion. Se establece
aqui como criterio aplicado en este caso: cuando dos jurisdicciones del mismo proyecto
tienen perfiles de riesgo diferentes para el mismo nombre, la decision de Bruna puede ser
diferenciada por jurisdiccion — no requiere una sola decision para ambas. El abogado
marcario recibe la distincion y asesora sobre si presentar el mismo nombre en ambas
(con el argumento de equivalencia perceptual en MX) o candidatos distintos por jurisdiccion.
Este criterio es candidato a precedente BR-5 futuro si el Owner lo ratifica.

---

## Nota de auditoria sobre RISK-POLICY aplicada

RISK-POLICY v1.0 (2026-04-25) fue concebida como politica de gestion de riesgos
operativos del sistema /RAUL/ (acciones de agentes sobre archivos, scripts, servicios
externos). No fue concebida como politica de claims de marketing o de registrabilidad
de marcas.

Sin embargo, sus principios subyacentes son aplicables analogicamente a este dominio:
- §3 (no afirmar datos falsos o no verificados) aplica a claims de RTB en naming.
- §4 (reversibilidad antes de ejecutar acciones de riesgo) aplica a la estrategia de
  contingencia ante colisiones de marca no confirmadas.
- El principio de escalar al Owner cuando el caso excede la capacidad interna (escalacion
  a asesoria legal externa si el riesgo supera lo que Bruna puede evaluar) aplica como
  principio de gobernanza incluso si no esta en §3 o §4 explicitos.

Ningun gate de este proyecto requirio escalacion a asesoria legal externa: ninguno cruza
el umbral de publicidad comparativa con consecuencias legales, marco regulatorio nuevo
sin precedente, o garantia con potencial litigio. Los gates de colision de marca (Gates 5,
6, 7) son navegables con busqueda formal del abogado — ese es el paso de asesoria externa
natural del proceso de registro. La escalacion ya esta integrada en el proceso.

---

*Bruna — BR-3 Phase 3 dossier de auditoria completo. Fecha: 2026-05-13.*
*Referencia cruzada: Bruna_BR-2_approval-set_v1.md para las decisiones formales.*
