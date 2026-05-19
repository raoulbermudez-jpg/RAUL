---
doc_type: BR-2-approval-set
project_id: portfolio-naming-ip-2026
domain: genteca
version: v2.0
parent: Bruna_BR-2_approval-set_v1.md
re_gate_trigger: "Antequera 3 correcciones doctrinales 2026-05-18"
scope: "NODO-B FlickerGuard + NODO-C Thermo-Safe (subset operativo batch SAPI VE inicial)"
gates_preservados_en_v1: "Gate 1 (override), Gate 2 (ThermalCurve rechazo firme), Gate 4 (ForensLog), Gate 6 (TripleLock), Gate 7 (TaskMemory), Gate 8 (Ecosystem GIO)"
gates_re_evaluados: "Gate 3 (Thermo-Safe), Gate 5 (FlickerGuard)"
author: Bruna
fecha: 2026-05-19
downstream: Vivienne (Phase 5 — Deck v3 focused)
nota: >
  Re-gate fresh disparado por las 3 correcciones doctrinales de Antequera en la
  reunión 2026-05-18. NO reutiliza el gate previo: la corrección #1 (examinador
  traduce) y la corrección #3 (familia de marcas vs stand-alone) modifican la
  base sobre la cual se construyeron los gates 3 y 5 originales. Los demás gates
  del v1.0 quedan vigentes; serán re-evaluados en un batch posterior cuando se
  active la fase México u otros nodos. Fecha decisión: 2026-05-19.
---

# BR-2 v2.0 — Approval Set focused Thermo-Safe + FlickerGuard
## Re-gate Phase 3 post correcciones doctrinales Antequera

> Re-gate de los Gates 3 y 5 del BR-2 v1.0 a la luz de las 3 correcciones
> doctrinales recibidas de la abogada marcaria Antequera el 2026-05-18.
> Los demás gates (1, 2, 4, 6, 7, 8) permanecen vigentes en BR-2 v1.0 y se
> reservan para batch posterior (fase México u otros nodos).

---

## Nota de re-gate

**Qué cambia y por qué.**

El 2026-05-18 13:36, Raoul tuvo videollamada de 17 minutos con la abogada
marcaria Antequera (recomendada por contacto previo de Liliam Ramirez).
Antequera entregó tres correcciones doctrinales que modifican la base
sobre la cual se construyeron los gates Bruna v1.0 del 2026-05-13:

1. **Corrección #1 — Examinador SAPI traduce el anglicismo.** El examinador
   tiene el deber de buscar la traducción al español del anglicismo y, si la
   traducción es descriptiva o genérica del producto, puede negar la marca
   aunque esté en inglés. Implicación para Bruna: la doctrina de equivalencia
   perceptual (consagrada en `reference_sapi_venezuela_quick.md`) **no es
   escudo automático**. Hay que aplicar la prueba de traducción a cada anchor
   y verificar si el resultado es descriptor/genérico en español del producto
   correspondiente. Modifica directamente Gate 3 (Thermo-Safe) y Gate 5
   (FlickerGuard).

2. **Corrección #2 — Madrid Protocol no aplica como atajo + arranque solo
   Venezuela.** Madrid es costoso si los países objetivo son pocos; la
   recomendación de Antequera es ir país por país (Venezuela primero, México
   segundo como decisión separada). Implicación para Bruna: el scope de
   evaluación de este re-gate se reduce a **SAPI Venezuela exclusivamente**.
   Los caveats IMPI MX de los gates v1.0 se preservan pero quedan etiquetados
   "diferidos para batch 2". No se modifican; no se ejecutan.

3. **Corrección #3 — Familia de marcas vs stand-alone puro.** Antequera
   recomienda registrar las nuevas marcas tecnológicas a nombre del mismo
   titular que Exceline / Exceline Profesional / Genius, como "familia de
   marcas de la misma empresa". Esto sustenta los chances de registrabilidad
   sin importar el otro elemento que las acompañe. Implicación para Bruna:
   **el argumento de familia de marcas refuerza el perfil de fantasía
   defendible** porque convierte cada nuevo registro en parte de una marca
   compleja del mismo titular, lo cual ayuda específicamente a los anchors
   que tenían perfil de descriptividad medio-alto (Thermo-Safe Gate 3). Es
   un argumento estructural que entra en el deck del abogado como pilar de
   defensa transversal y se incorpora en los rationale de los gates re-
   evaluados.

**Qué se preserva del BR-2 v1.0.**

- Gate 1 (override curva inversa universal de facto) — sin cambios.
- Gate 2 (ThermalCurve rechazado firme) — sin cambios. La corrección de
  Antequera, en todo caso, refuerza el rechazo: el examinador traduce
  "ThermalCurve" → "Curva Térmica" → descriptor literal del mecanismo IEC
  60947-4-1. El rechazo del v1.0 era correcto y se mantiene con base nueva.
- Gate 4 (ForensLog Escenario A) — preservado, no se re-evalúa porque
  ForensLog no está en el batch SAPI VE inicial (los anchors batch 1 son
  exclusivamente Thermo-Safe y FlickerGuard según decisión Owner 2026-05-18).
- Gate 6 (TripleLock contingencia sectorial) — preservado, diferido.
- Gate 7 (TaskMemory diferenciado por jurisdicción) — preservado, diferido.
  Nota: la corrección #2 simplifica este gate porque el batch 1 es solo
  Venezuela; el caveat IMPI MX quedará para batch 2.
- Gate 8 (Ecosystem GIO sin términos de protocolo estándar) — preservado,
  diferido.

**Qué se re-evalúa en este documento.**

- **Re-Gate 3 — Thermo-Safe (NODO-C):** PRIORIDAD #1 del batch SAPI VE inicial.
- **Re-Gate 5 — FlickerGuard (NODO-B):** PRIORIDAD #2 del batch SAPI VE inicial.

---

## Re-Gate 3 — Thermo-Safe (NODO-C)

### Decisión

**APROBADO CON CAVEAT REFORZADO + ESCALACIÓN OWNER PARA CASO B.**

Thermo-Safe sobrevive como anchor principal de NODO-C, pero el perfil de
descriptividad sube de medio-alto a alto-tras-traducción bajo la doctrina
corregida de Antequera. La familia de marcas (corrección #3) compensa
parcialmente el riesgo, pero no lo elimina. Se recomienda activamente al
Owner activar Caso B (eliminar mención "PROTECCIÓN TÉRMICA" del empaque
antes de la solicitud SAPI FM-02) como medida proactiva de reducción de
riesgo de descriptividad.

### Rationale actualizado

**Paso 1 — Aplicación de la prueba de traducción del examinador (corrección
#1 de Antequera).**

El examinador SAPI hace la traducción mental del anglicismo al español
venezolano:
- "Thermo" → "Termo-" / "Térmico-" (prefijo culto reconocido)
- "Safe" → "Seguro"
- Combinación traducida: "Termo-Seguro" / "Térmico-Seguro"

Aplicación al producto (relé de protección monofásico GSM-MB/RB/RE con
sensor NTC integrado descrito en empaque como "PROTECCIÓN TÉRMICA"):
- "Termo-Seguro" en clase 9 para un protector con protección térmica = el
  examinador puede leer la traducción como descriptor del beneficio
  funcional del producto. El argumento de fantasía pierde la elasticidad
  que tenía bajo la lectura de equivalencia perceptual pura.
- Riesgo de objeción del examinador: **alto** (era medio-alto bajo doctrina
  v1.0). El examinador no necesita argumento técnico complejo para
  fundamentar la objeción — la traducción está a la vista.

**Paso 2 — Compensación por familia de marcas (corrección #3 de Antequera).**

Si Thermo-Safe se registra como parte de una **familia de marcas de Genteca
Exceline / Exceline Profesional / Genius** (mismo titular que el umbrella),
el examinador puede ponderar:

- Distintividad adquirida del titular en clase 9 protección eléctrica.
- Coherencia de portafolio: Thermo-Safe entra como una de varias marcas
  técnicas del titular (StaggerStart, FlickerGuard, ForensLog, TripleLock,
  TaskMemory, etc.), no como signo aislado.
- Doctrina de "secondary meaning" implícita: el titular ya tiene presencia
  comercial documentada en el segmento, lo cual sostiene la lectura de
  Thermo-Safe como nombre de fantasía del portafolio antes que descriptor
  funcional del producto.

Este argumento NO elimina la descriptividad pero la **modula**. La pelea ante
el examinador se vuelve defendible — no garantizada.

**Paso 3 — Activación de Caso B como mitigación proactiva.**

La nota original de v1.0 (Gate 3, nota sobre Caso B) anticipó que si Genteca
eliminaba la mención "PROTECCIÓN TÉRMICA" del empaque, el perfil de
descriptividad bajaría de medio-alto a medio. Bajo la doctrina corregida de
Antequera, ese movimiento ahora bajaría el perfil de **alto-tras-traducción a
medio**. Esto convierte una pelea defendible-pero-cuesta-arriba en una pelea
defendible-con-margen.

**Recomendación Bruna:** Owner debe activar Caso B antes de la solicitud
formal FM-02. La modificación del empaque GSM-MB/RB/RE no es bloqueante para
el inicio del proceso con Antequera (búsqueda fonética + propuesta de
honorarios), pero sí debe completarse antes de presentar el FM-02 al SAPI.
Esta es una **escalación Owner** que la nota de re-gate dispara.

**Paso 4 — Reevaluación de candidatos alternos del nodo bajo nueva doctrina.**

Bajo la prueba de traducción del examinador (corrección #1):

| Candidato | Traducción examinador | Perfil bajo nueva doctrina |
|---|---|---|
| **Thermo-Safe** | Termo-Seguro / Térmico-Seguro | Alto-tras-traducción. Defendible con familia + Caso B. |
| **CoreSafe** | Núcleo-Seguro / Centro-Seguro | Bajo. "Núcleo seguro" no es descriptor literal del mecanismo NTC; "núcleo" es metáfora del centro del motor protegido, no del sensor. Perfil de fantasía robusto incluso post-traducción. |
| **WarmWatch** | Vigilancia-Tibia / Vigilancia-Cálida | Bajo. La traducción produce una construcción extraña en español ("Vigilancia Tibia" no comunica protección de motor) — exactamente la condición que beneficia al solicitante: una traducción que el consumidor venezolano promedio no decodifica como descriptor funcional. |
| **HeatSeal** | Sellado-Calor / Sello-Térmico | Medio-alto. La traducción produce un compuesto comprensible ("Sello Térmico") que el examinador puede leer como descriptor de la función de protección contra el calor. Bajo nueva doctrina sube de moderado a medio-alto. |

**Conclusión del paso 4:** si Antequera rechaza Thermo-Safe en la búsqueda
inicial o si el examinador lo objeta, el orden de respaldo recomendado es:
**(1) CoreSafe → (2) WarmWatch → (3) HeatSeal**. HeatSeal pierde su posición
como candidato fuerte bajo la doctrina corregida — Bruna recomienda
considerarlo cuarto candidato de respaldo, no tercero.

### Caveat literal actualizado para integrar en deck v3 (notas del slide NODO-C)

> "Thermo-Safe es nombre de fantasía propuesto para el sensor NTC integrado
> del protector monofásico GSM-MB/RB/RE. Aplicando la doctrina de Antequera
> sobre la facultad del examinador SAPI de traducir el anglicismo al español,
> la traducción 'Termo-Seguro' / 'Térmico-Seguro' puede ser leída como
> descriptor del beneficio funcional del producto en clase 9. El argumento
> de fantasía bajo equivalencia perceptual SAPI se sostiene pero pierde
> elasticidad: el perfil de descriptividad es alto-tras-traducción, no
> medio-alto como se había estimado bajo la doctrina previa.
>
> Genteca propone defender el registro de Thermo-Safe con dos argumentos
> combinados: (a) **familia de marcas del mismo titular** — Thermo-Safe se
> presenta como una marca dentro de la familia técnica registrada a nombre
> del titular Exceline / Exceline Profesional / Genius, lo cual sustenta la
> distintividad del cluster y modula la lectura de descriptividad aislada;
> (b) **modificación del empaque (Caso B)** — Genteca evaluará retirar la
> mención literal 'PROTECCIÓN TÉRMICA' del empaque GSM-MB/RB/RE antes de la
> presentación de la solicitud FM-02, lo cual reduce el contraste entre la
> marca propuesta y la descripción funcional del producto en uso.
>
> Sin estos dos argumentos combinados, el riesgo de objeción de oficio del
> examinador es alto. Con los dos argumentos combinados, el registro es
> defendible.
>
> Candidatos de respaldo del nodo si la búsqueda fonética o el examen formal
> objeta Thermo-Safe, en orden recomendado bajo doctrina actualizada:
> (1) CoreSafe (perfil de fantasía robusto post-traducción), (2) WarmWatch
> (traducción produce construcción semánticamente extraña en español, lo cual
> favorece la registrabilidad), (3) HeatSeal (perfil más débil que en
> análisis previo; preferir CoreSafe o WarmWatch si Thermo-Safe cae)."

### Implicación específica para Antequera (instrucciones operativas al abogado)

1. **Búsqueda fonética prioritaria en SAPI Venezuela** de los 4 candidatos
   en clase 9 protección eléctrica: Thermo-Safe (anchor), CoreSafe,
   WarmWatch, HeatSeal.
2. **Verificación del titular** de Exceline / Exceline Profesional / Genius
   en SAPI Venezuela (pregunta abierta de Liliam) — necesario para alinear el
   campo titular de las nuevas marcas con la recomendación de familia.
3. **Dictamen sobre Caso B:** Antequera evalúa si la modificación de empaque
   (eliminar "PROTECCIÓN TÉRMICA" del front) reduce efectivamente el perfil
   de descriptividad para el examinador, o si el empaque del producto
   posterior al registro no entra en el análisis del examinador en el momento
   de la solicitud.
4. **Argumento de familia de marcas:** Antequera evalúa si el SAPI Venezuela
   reconoce explícitamente la doctrina de familia de marcas como elemento
   modulador del análisis de descriptividad (varía entre jurisdicciones).
5. **Propuesta de honorarios y cronograma** para el batch inicial (Thermo-
   Safe + FlickerGuard).

### Cláusula RISK-POLICY aplicada

RISK-POLICY v1.0 §3 (no afirmar como propio lo que no puede sostenerse) +
§4 (reversibilidad). El registro de Thermo-Safe es defendible bajo doctrina
corregida con las dos mitigaciones combinadas; si una de las dos falla
(familia de marcas no convence al examinador, Owner no activa Caso B), la
contingencia es activar el orden de respaldo de candidatos. La reversibilidad
está garantizada por los 3 candidatos alternos del nodo ya evaluados.

---

## Re-Gate 5 — FlickerGuard (NODO-B)

### Decisión

**APROBADO — perfil mejorado bajo doctrina corregida + familia de marcas.**

FlickerGuard pasa de "Aprobado con contingencia OMPI" en v1.0 a **"Aprobado
con argumento de distintividad reforzado"** en v2.0. La aplicación de la
prueba de traducción del examinador, combinada con la observación de uso
cotidiano del término "parpadeo" en español venezolano, mejora el perfil del
candidato. La contingencia OMPI (productos LED Australia/UK) se mantiene
viva — depende de la búsqueda fonética que ejecutará Antequera.

### Rationale actualizado

**Paso 1 — Aplicación de la prueba de traducción del examinador (corrección
#1 de Antequera).**

- "Flicker" → "Parpadeo" (traducción común venezolana/mexicana)
- "Guard" → "Guarda" / "Protector"
- Combinación traducida: "Guarda-Parpadeo" / "Protector-Parpadeo"

Aplicación al producto (supervisor de voltaje monofásico GSM-L con detección
sub-ciclo de flicker en 20 ms):
- En español venezolano cotidiano, "parpadeo" se asocia mayoritariamente con
  **iluminación** (focos que parpadean), no con perturbaciones eléctricas
  que afectan compresores. El consumidor venezolano promedio que compra un
  protector para AC o refrigerador no asocia "parpadeo" con el fenómeno
  eléctrico técnico (flicker IEC 61000-4-15) que protege el producto.
- La traducción "Guarda-Parpadeo" produce una construcción que, en el segmento
  específico de productos de protección eléctrica para motores residenciales,
  **no es descriptor literal de la función**. El examinador puede leer "Guarda-
  Parpadeo" como nombre de fantasía con anclaje técnico no evidente para el
  consumidor.
- Riesgo de objeción por descriptividad: **bajo a moderado** bajo nueva
  doctrina. Mejor que el perfil del v1.0 ("⚠ moderado por colisión OMPI
  potencial"). La traducción no agrava la descriptividad.

**Paso 2 — Refuerzo por familia de marcas (corrección #3 de Antequera).**

FlickerGuard, registrado a nombre del titular Exceline / Exceline Profesional
/ Genius como parte de la familia de marcas técnicas, hereda la coherencia
del cluster. El argumento es transversal y se incorpora en el mismo sentido
que para Thermo-Safe (ver Re-Gate 3 paso 2).

**Paso 3 — Status de la contingencia OMPI (productos LED Australia/UK).**

Esta contingencia no cambia con las correcciones de Antequera — sigue
siendo una verificación de búsqueda fonética en SAPI Venezuela exclusivamente
(batch 1 es solo VE; OMPI con designación VE específicamente). Status:
**mantenida viva**. Los candidatos de contingencia OMPI del v1.0 (SpikeShield
y SagGuard) permanecen disponibles si Antequera detecta colisión en VE.

**Paso 4 — Reevaluación de candidatos alternos del nodo bajo nueva doctrina.**

Bajo la prueba de traducción del examinador:

| Candidato | Traducción examinador | Perfil bajo nueva doctrina |
|---|---|---|
| **FlickerGuard** | Guarda-Parpadeo / Protector-Parpadeo | Bajo-moderado. "Parpadeo" en español VE asocia con luz, no con motor — favorece la fantasía. |
| **SagShield** | Escudo-Caída / Escudo-Hundimiento | Bajo. "Caída de voltaje" es término técnico que el consumidor no maneja; "Sag" en español es prácticamente intraducible al uso cotidiano. Perfil de fantasía alto. |
| **PulseBlock** | Bloqueo-Pulso / Bloquea-Impulso | Bajo. "Pulso" en español VE asocia con ritmo cardíaco o luz pulsante, no con perturbación eléctrica de un protector de motor. Construcción semánticamente alejada del descriptor funcional. |
| **SpurGuard** | Guarda-Espuela / Guarda-Espuria | Muy bajo. "Spur" en español tiene traducción doble (espuela / espuria) — ninguna de las dos comunica función eléctrica al consumidor. Perfil de fantasía muy robusto post-traducción. |
| **SpikeShield** (cont. OMPI) | Escudo-Pico / Escudo-Punta | Bajo. "Pico de voltaje" es término técnico; "Spike" en español VE asocia con punta/pico físico, no con perturbación. |
| **SagGuard** (cont. OMPI) | Guarda-Caída | Bajo. Mismo razonamiento que SagShield. |

**Conclusión del paso 4:** los 4 candidatos del nodo (más las 2 contingencias)
mantienen o mejoran su perfil bajo la doctrina corregida. SpurGuard sube en
perfil — la traducción produce una construcción tan extraña en español que
favorece la registrabilidad como fantasía pura. Si Antequera quiere recomendar
un candidato adicional fuerte además de FlickerGuard, SpurGuard es el más
diferenciado semánticamente del territorio descriptor.

### Caveat literal actualizado para integrar en deck v3 (notas del slide NODO-B)

> "FlickerGuard es nombre de fantasía propuesto para la función de detección
> sub-ciclo de perturbaciones de voltaje del supervisor monofásico GSM-L (20
> ms de detección de flicker — RTB único en el segmento, NODO-B verde en
> análisis competitivo). Aplicando la doctrina de Antequera sobre la facultad
> del examinador SAPI de traducir el anglicismo al español, la traducción
> 'Guarda-Parpadeo' / 'Protector-Parpadeo' no produce un descriptor literal
> de la función del producto para el consumidor venezolano promedio. En
> español VE cotidiano, 'parpadeo' se asocia mayoritariamente con
> iluminación, no con perturbaciones eléctricas que dañan compresores. La
> distancia semántica entre la traducción del anglicismo y el campo del
> producto favorece la registrabilidad como signo de fantasía.
>
> Genteca propone defender el registro de FlickerGuard con tres argumentos
> combinados: (a) **distancia semántica de la traducción** — la traducción
> al español no es descriptor funcional para el consumidor del producto;
> (b) **familia de marcas del mismo titular** — FlickerGuard entra como una
> marca técnica adicional dentro de la familia Exceline / Exceline Profesional
> / Genius del titular, lo cual sustenta la coherencia del portafolio
> registrable; (c) **RTB cuantitativo verificable** — la especificación de
> 20 ms en HDE GSM-L v10 (NODO-B verde en análisis competitivo) es el
> diferenciador técnico más sólido del portafolio.
>
> Contingencia OMPI activa: existe evidencia de productos de iluminación LED
> (Australia, UK) que usan el término 'Flicker Guard' como nombre de feature
> en clase 9 amplia. La búsqueda fonética en SAPI Venezuela debe verificar
> si algún titular tiene marca registrada con ese nombre en la subclase de
> dispositivos de protección y supervisión eléctrica con efectos en
> Venezuela. La distinción de producto entre supervisor de voltaje para
> protección de compresores y luminaria de iluminación LED es argumento
> navegable bajo doctrina de distinción de producto.
>
> Candidatos de respaldo del nodo si Antequera detecta colisión en SAPI VE,
> en orden de perfil de fantasía post-traducción: (1) SpurGuard (perfil de
> fantasía muy robusto — traducción extraña en español favorece la
> registrabilidad), (2) SagShield, (3) PulseBlock. Contingencias OMPI
> específicas: SpikeShield y SagGuard."

### Implicación específica para Antequera (instrucciones operativas al abogado)

1. **Búsqueda fonética prioritaria en SAPI Venezuela** de los 4 candidatos
   en clase 9 protección/supervisión eléctrica: FlickerGuard (anchor),
   SagShield, PulseBlock, SpurGuard. Más las 2 contingencias OMPI:
   SpikeShield, SagGuard.
2. **Búsqueda OMPI focused en VE:** verificar si existen titulares con marca
   registrada o solicitud en trámite que incluya "FlickerGuard" o "Flicker
   Guard" en clase 9 con designación de Venezuela, particularmente en
   subclases de iluminación LED y de protección eléctrica.
3. **Dictamen sobre argumento de distancia semántica de traducción:**
   Antequera evalúa si el argumento "parpadeo en español VE se asocia con
   luz, no con motor" es defendible ante un examinador SAPI o si el
   examinador puede objetar que la asociación es discutible.
4. **Argumento de familia de marcas:** mismo razonamiento que Re-Gate 3 —
   evaluar si SAPI Venezuela reconoce explícitamente la doctrina.

### Cláusula RISK-POLICY aplicada

RISK-POLICY v1.0 §3. El RTB del NODO-B (20 ms verificado en HDE GSM-L v10,
NODO-B verde en análisis competitivo) sostiene el nombre como diferenciador
cuantitativo. La doctrina corregida no debilita el caso — lo refuerza por la
distancia semántica entre la traducción del anglicismo y el campo del
producto.

---

## Cambio doctrinal #3 — Implicación transversal: familia de marcas como pilar de defensa

La corrección #3 de Antequera (registrar las nuevas marcas a nombre del
mismo titular del umbrella Exceline / Exceline Profesional / Genius como
familia de marcas) **no es un gate adicional sino un pilar estructural de
defensa del portafolio**. Implicaciones:

1. **Modifica decisión #3 del charter del proyecto.** El charter v1.0 decía
   "Stand-alone — cada nombre como marca independiente clase 9, sin depender
   de Exceline/Genius umbrella". La nueva decisión es: "**Stand-alone clase 9
   en nombre, registrado a nombre del mismo titular del umbrella (Exceline /
   Exceline Profesional / Genius) como familia de marcas técnicas — Antequera
   2026-05-18**". El nombre sigue siendo independiente (no depende
   visualmente del umbrella), pero el titular es el mismo. Es un cambio
   operativo de **titular**, no de naming.

2. **Cómo se incorpora al deck v3.** Vivienne debe incluir un **slide nuevo
   sobre familia de marcas** entre el slide de resumen ejecutivo del subset
   y los slides de NODO-C / NODO-B, para anclar el argumento de defensa
   antes de presentar cada candidato. El slide explica:
   - Por qué se registran a nombre del titular del umbrella (no del producto).
   - Cómo la familia de marcas sustenta la distintividad del cluster.
   - Cómo opera como argumento modulador ante el examinador SAPI para perfiles
     de descriptividad medios o altos.

3. **Pregunta abierta operativa.** Liliam debe confirmar quién es el titular
   actual registrado de Exceline / Exceline Profesional / Genius en SAPI
   Venezuela (persona natural, persona jurídica, qué razón social
   exactamente). Antequera necesita el dato para alinear el campo titular
   del FM-02 de las nuevas marcas. Esta pregunta queda como acción Owner
   pendiente y entra en el correo a Antequera + Liliam como punto a
   confirmar.

4. **Impacto en escalación Owner.** Si el titular actual de Exceline /
   Exceline Profesional / Genius en SAPI VE no es el titular esperado o si
   existen inconsistencias entre marcas del umbrella (titulares distintos
   entre Exceline, Exceline Profesional y Genius), Antequera deberá asesorar
   sobre cómo armar la familia operativamente. Esta es una escalación
   diferida — depende de la respuesta de Liliam.

---

## Resumen ejecutivo de sello Bruna — v2.0 focused

| Gate | Nombre anchor | Decisión v1.0 | Decisión v2.0 | Acción downstream |
|------|--------------|---------------|---------------|-------------------|
| Re-3 | Thermo-Safe (NODO-C) | Aprobado con caveat Caso A | **Aprobado con caveat reforzado + escalación Owner Caso B** | Vivienne integra caveat actualizado en deck v3 slide NODO-C. Owner activa Caso B antes de FM-02. |
| Re-5 | FlickerGuard (NODO-B) | Aprobado con contingencia OMPI | **Aprobado con argumento de distintividad reforzado** | Vivienne integra caveat actualizado en deck v3 slide NODO-B. Contingencia OMPI mantiene búsqueda Antequera. |
| Transversal | Familia de marcas | (no existía) | **Pilar de defensa estructural — modifica decisión #3 del charter** | Vivienne agrega slide específico en deck v3. Charter actualizado por Raul. Liliam confirma titular del umbrella. |

---

## Comparativa v1.0 → v2.0 (gates re-evaluados)

### Re-Gate 3 — Thermo-Safe

| Dimensión | v1.0 (2026-05-13) | v2.0 (2026-05-19) |
|---|---|---|
| Doctrina base | Equivalencia perceptual SAPI (escudo automático asumido) | Equivalencia perceptual + examinador traduce (no escudo automático) |
| Perfil de descriptividad | Medio-alto (Caso A) | Alto-tras-traducción (Caso A) / Medio (Caso B) |
| Argumento principal | Distinción semántica "Thermo-Safe" vs "PROTECCIÓN TÉRMICA" del empaque | Distinción semántica + familia de marcas + Caso B (mitigación proactiva) |
| Recomendación Caso B | "Opción que mejora el perfil si Owner la toma" | **Escalación Owner activa** — recomendación de activar antes de FM-02 |
| Orden de respaldo candidatos | CoreSafe / WarmWatch / HeatSeal (mismo orden) | **CoreSafe / WarmWatch / HeatSeal (HeatSeal degradado a cuarto)** |
| Status | Aprobado con caveat | Aprobado con caveat reforzado |

### Re-Gate 5 — FlickerGuard

| Dimensión | v1.0 (2026-05-13) | v2.0 (2026-05-19) |
|---|---|---|
| Doctrina base | Equivalencia perceptual SAPI | Equivalencia perceptual + traducción examinador favorable |
| Perfil de descriptividad | Moderado por colisión OMPI potencial | **Bajo-moderado** (traducción al español favorece registrabilidad) |
| Argumento principal | Fantasía + RTB 20 ms + contingencia lista | Distancia semántica traducción + familia + RTB 20 ms |
| Contingencia OMPI | Activa (búsqueda fonética pendiente) | Activa (sin cambios) |
| Candidato alterno destacado | (no había destacado especial) | **SpurGuard sube** — traducción extraña favorece fantasía |
| Status | Aprobado con contingencia | Aprobado con argumento reforzado |

---

## Escalaciones Owner que dispara este re-gate

1. **E-Caso-B (NODO-C) — Activación de Caso B para Thermo-Safe.** Bruna
   recomienda activamente que Owner evalúe y autorice antes de FM-02 SAPI la
   modificación de empaque GSM-MB/RB/RE para eliminar la mención literal
   "PROTECCIÓN TÉRMICA" del front. Sin esta mitigación, el perfil de
   descriptividad de Thermo-Safe bajo doctrina corregida es alto-tras-
   traducción, no medio-alto como se estimaba. Con la mitigación, el perfil
   baja a medio. La decisión es comercial-operativa (afecta empaque y
   posiblemente material PoS) y requiere coordinación con Oz / Producción.

2. **E-Titular (transversal) — Confirmación del titular registrado del
   umbrella Exceline / Exceline Profesional / Genius en SAPI Venezuela.**
   Liliam debe confirmar quién es el titular registrado (razón social,
   persona natural/jurídica) en cada uno de los 3 nombres del umbrella, y
   si hay coherencia entre los 3 o si los titulares son distintos. Antequera
   necesita el dato para alinear el campo titular del FM-02 de las nuevas
   marcas con la recomendación de familia de marcas. Esta pregunta entra en
   el correo a Antequera + Liliam.

---

*Bruna — BR-2 v2.0 re-gate focused Thermo-Safe + FlickerGuard. Fecha:*
*2026-05-19. Inputs: BR-2 v1.0 (2026-05-13), Nota de interacción Antequera*
*2026-05-18, Anexo Técnico v1.0 (RTBs NODO-B y NODO-C), Naming Bible v1.0,*
*Charter v1.0, reference_sapi_venezuela_quick.md.*

*Downstream: Vivienne (deck v3 focused), Raul (charter update + Naming Bible v2*
*focused + Anexo Técnico v2 focused + email draft + Ivo close).*
