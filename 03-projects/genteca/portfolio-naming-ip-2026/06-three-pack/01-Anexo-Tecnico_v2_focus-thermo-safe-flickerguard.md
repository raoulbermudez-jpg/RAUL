---
doc_type: anexo-tecnico
project_id: portfolio-naming-ip-2026
domain: genteca
version: v2_focus-thermo-safe-flickerguard
parent_full: 01-Anexo-Tecnico_v1.md
parent_distribution: 01-Anexo-Tecnico_v2.md
audience: Abogada marcaria Antequera + Liliam Ramirez
fecha: 2026-05-19
scope_batch: "SAPI Venezuela — batch inicial 2 nodos"
nodo_prioridad_1: "NODO-C — Thermo-Safe (sensor NTC integrado)"
nodo_prioridad_2: "NODO-B — FlickerGuard (detección sub-ciclo de flicker)"
gates_referenciados: "Bruna_BR-2_approval-set_v2_focus-thermo-safe-flickerguard.md (re-gate 2026-05-19)"
correcciones_doctrinales_aplicadas:
  - "C1: examinador SAPI traduce el anglicismo"
  - "C2: solo Venezuela en este batch"
  - "C3: familia de marcas vs stand-alone puro"
---

# Anexo Técnico v2 focused — Thermo-Safe + FlickerGuard
## Base técnica para registro de marcas IP — Clase 9 SAPI Venezuela (batch inicial)

---

## Sección 1 — Introducción para Antequera

### Qué es este documento

Este Anexo Técnico es una **vista filtrada** del Anexo Técnico v1.0 / v2.0
del proyecto Portfolio Naming IP 2026 de Genteca, acotado a los **2 nodos
tecnológicos del batch SAPI Venezuela inicial** acordado en la reunión del
2026-05-18: NODO-B (FlickerGuard) y NODO-C (Thermo-Safe).

Cada nodo se presenta con: mecanismo técnico verificable, productos donde
vive, RTBs documentables en HDEs Genteca, análisis competitivo frente a
fabricantes de la lista relevante (ABB, Siemens, Schneider, Eaton, Rockwell,
Chint, Lovato, LS), normas IEC aplicables, gaps documentales que I+D Genteca
debe completar antes de la solicitud FM-02, y caveats legales actualizados
bajo el re-gate Bruna v2.0 que incorpora las 3 correcciones doctrinales de
Antequera del 2026-05-18.

El propósito del documento es dar a Antequera la base técnica suficiente
para evaluar la registrabilidad de Thermo-Safe y FlickerGuard en SAPI
Venezuela bajo la doctrina corregida, identificar la documentación interna
de Genteca que puede pedir como respaldo, y ejecutar la búsqueda fonética
con la información técnica completa de cada candidato.

### Universo de productos cubierto (acotado al batch)

| Línea comercial | Productos relevantes para el batch |
|---|---|
| **Exceline residencial** | GSM-MB (120B / 220B), GSM-RB (R120B / R220B), GSM-RE (RE120A / RE220M) — portadores del NTC integrado (NODO-C) |
| **Exceline Profesional** | GSM-L — portador principal del RTB de detección de flicker en 20 ms (NODO-B) |
| **Exceline residencial extendido** | GSM-MB, GSM-RB, GSM-RE, GSM-NG — portadores del comportamiento V-t algorítmico con tiempos de respuesta documentados |

### Caveat estructural — Override curva inversa V-t algorítmica

Aplicable a NODO-B (Bruna BR-2 v1.0 Gate 1 — preservado vigente).

> "La presencia de la curva inversa V-t algorítmica se indica como universal
> de facto para la gama Exceline / Exceline Profesional / Genius. La
> verificación producto por producto está pendiente de auditoría formal por
> I+D de Genteca y debe completarse antes de la primera publicidad
> comparativa externa que use la función como diferenciador. En el contexto
> de este proceso de registro de marca, la función se documenta con base en
> los productos en los que Vera la confirmó en HDE."

---

## Sección 2 — NODO-C: Modelo térmico NTC integrado — **PRIORIDAD #1**

### Mecanismo técnico

Sensor de temperatura NTC embebido físicamente en el protector monofásico
GSM-MB/RB/RE. El sensor lee la temperatura real del entorno del compresor
(o del devanado, según instalación). La lógica interna compara la
temperatura medida con umbrales configurados o fijos y actúa la
desconexión si se detecta sobrecalentamiento. A diferencia del modelo I-t
algorítmico estándar IEC (que calcula temperatura implícita a partir de la
corriente sin sensor físico), este nodo usa **medición física directa de
temperatura con un componente de hardware** (NTC) en el circuito de
decisión.

- **Inputs:** lectura analógica del sensor NTC (resistencia variable con
  temperatura)
- **Transformación:** comparación de la temperatura medida contra umbral
  térmico de disparo
- **Outputs:** desconexión de la carga + indicación en LED del protector

### Productos donde vive

GSM-MB (120B y 220B), GSM-RB (R120B y R220B), GSM-RE (RE120A y RE220M) —
todos en versión actual con protección térmica ("AHORA CON PROTECCIÓN
TÉRMICA", confirmado en etiqueta de empaque HDE GLA_T versiones V10/V9/V13).

### RTBs verificables

1. **Sensor NTC presente en hardware** — confirmado en etiqueta de empaque
   GSM-MB (HDE GLA_T V10), GSM-RB (HDE GLA_T V9), GSM-RE (HDE GLA_T V13).
2. **Mención "PROTECCIÓN TÉRMICA" explícita en empaque** versiones V10/V9/
   V13 — referencia: etiqueta de empaque HDE GLA_T. **Nota crítica:** la
   mención literal en el empaque es la razón principal por la que Bruna v2.0
   eleva el perfil de descriptividad de Thermo-Safe a alto-tras-traducción
   y recomienda activación del Caso B (escalación Owner).
3. **Integración estándar de serie:** sin módulo adicional ni cableado
   externo (a diferencia de SIMOCODE y LTMR que requieren módulo separado).
4. **Parámetros numéricos del NTC** (umbral de disparo, rango de
   temperatura, histéresis, tiempo de respuesta, resistencia nominal a 25 °C,
   longitud de cable si aplica): **NO disponibles en HDEs actuales de la
   KB**. Gap documental crítico G1 — ver Sección 4.

### Diferenciación competitiva (Orlan OL-1)

**Estado: AMARILLO.**

| Competidor | Función equivalente | Diferencia |
|---|---|---|
| **Siemens SIMOCODE pro 3UF7** | Soporta NTC, KTY83/84, PT100/PT1000 mediante "Temperature Module" | Módulo separado, mayor costo, aplicación industrial trifásica |
| **Schneider TeSys T LTMR** | Soporta PTC Analog y NTC Analog ("Motor Temperature Sensing") | Módulo separado, denominación descriptiva no fantástica |
| **Eaton C440/C441** | Termistor como opción | Sin nombre de fantasía identificado, opción no estándar |
| **ABB / Siemens 3RN2** | Termistor PTC dedicado | Sin nombre de fantasía, dedicado a aplicación industrial |
| **Competencia residencial VE** | Sin NTC integrado identificado en protectores enchufables | Genteca tiene el diferenciador real en el segmento |

**Diferenciador real:** integración del NTC en un protector de voltaje
monofásico de uso doméstico/comercial como **feature estándar de serie** (no
módulo separado), al punto de precio del segmento residencial venezolano.
Ningún competidor identificado ofrece esta integración en el mismo segmento.

### Normas IEC aplicables

- IEC 60947-1 (low-voltage switchgear and controlgear — general rules)
- IEC 60730 (automatic electrical controls — applicable a sensores de
  temperatura para uso doméstico)
- IEC 60751 (industrial platinum resistance thermometers — referencia
  comparativa al PTC100 de la gama Genius, no aplicable directamente al
  NTC del GSM-MB/RB/RE)

### Caveat legal actualizado (Bruna BR-2 v2.0 Re-Gate 3)

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
> combinados: (a) familia de marcas del mismo titular — Thermo-Safe se
> presenta como una marca dentro de la familia técnica registrada a nombre
> del titular Exceline / Exceline Profesional / Genius, lo cual sustenta la
> distintividad del cluster y modula la lectura de descriptividad aislada;
> (b) modificación del empaque (Caso B) — Genteca evaluará retirar la
> mención literal 'PROTECCIÓN TÉRMICA' del empaque GSM-MB/RB/RE antes de la
> presentación de la solicitud FM-02, lo cual reduce el contraste entre la
> marca propuesta y la descripción funcional del producto en uso.
>
> Sin estos dos argumentos combinados, el riesgo de objeción de oficio del
> examinador es alto. Con los dos argumentos combinados, el registro es
> defendible."

### Documentos internos Genteca relevantes

- HDE GSM-MB versión vigente que incluya sección de protección térmica NTC
  (actualmente no disponible en KB — gap G1).
- HDE GSM-RB versión vigente equivalente con sección NTC (gap G1).
- HDE GSM-RE versión vigente equivalente con sección NTC (gap G1).
- Especificación del sensor NTC: rango de temperatura, umbral de
  desconexión, tipo de sensor (resistencia nominal a 25 °C), longitud de
  cable si aplica (gap G1).

---

## Sección 3 — NODO-B: Detección sub-ciclo de perturbaciones de voltaje — **PRIORIDAD #2**

### Mecanismo técnico

El algoritmo de supervisión de voltaje del supervisor monofásico GSM-L
tiene dos comportamientos integrados en el mismo dispositivo:

**(1) Detección de flicker (sub-ciclo):** el dispositivo muestrea el voltaje
a frecuencia suficiente para detectar inestabilidad o parpadeo en ventana
de 20 ms (GSM-L) o 150 ms (GSM-MB, GSM-RB, GSM-NG). Si detecta variación
sub-ciclo, desconecta la carga sin esperar que el voltaje salga del rango
de ajuste estático.

- Inputs: señal de voltaje con variaciones rápidas
- Transformación: algoritmo de detección de pendiente o variación súbita en
  ventana menor a 1 ciclo de 60 Hz
- Outputs: desconexión inmediata

**(2) Curva inversa V-t algorítmica** (override universal de facto — ver
caveat Sección 1): el tiempo de desconexión es inversamente proporcional a
la desviación del voltaje respecto al umbral configurado. Una desviación
extrema produce desconexión casi instantánea; una desviación marginal
produce desconexión con retardo mayor.

- Parámetros documentados: 0,02 a 2 s según intensidad de falla (GSM-AV06
  HDE); 0,4 a 3 s según intensidad (GSM-RB HDE); 20-30 ms para fallas
  extremas en GSM-AV06.

**Nota de denominación:** el comportamiento V-t proporcional está documentado
en las HDEs con datos de tiempo específicos, pero **la denominación formal
"curva inversa V-t algorítmica" no aparece en los documentos Genteca
actuales**. Es la descripción técnica correcta del comportamiento subyacente.
I+D debe confirmar si existe especificación interna con esa denominación
(gap G2 — ver Sección 4).

### Productos donde vive

- **GSM-L:** 20 ms de detección de flicker (dato explícito en HDE v10 —
  portador principal del RTB único del nodo)
- GSM-MB, GSM-RB, GSM-RE: 150 ms por flicker/inestabilidad
- GSM-AV06: 0,02-2 s según intensidad
- GSM-NG: 150 ms

### RTBs verificables

1. **Tiempo de detección de flicker: 20 ms** (GSM-L HDE v10 — dato
   explícito, único en la gama). Referencia: HDE GSM-L versión v10.
2. Tiempo de detección genérica de falla de voltaje (GSM-L): a partir de
   **60 ms**. Referencia: HDE GSM-L v10.
3. Tiempo de desconexión por flicker/inestabilidad (GSM-MB, GSM-RB, GSM-NG):
   **150 ms**. Referencia: HDEs respectivas.
4. Desconexión variable según intensidad: **0,02 a 2 s** (GSM-AV06 HDE);
   **0,4 a 3 s** (GSM-RB HDE).
5. Detección de parpadeos e inestabilidad como causa de desconexión:
   documentada en HDEs GSM-MB, GSM-RB, GSM-RE, GSM-L, GSM-NG.

### Diferenciación competitiva (Orlan OL-1)

**Estado: VERDE — diferenciador más fuerte del portafolio.**

| Competidor | Detección de flicker en milisegundos | Notas |
|---|---|---|
| **ABB CM-ESS** | No especificado en datasheet CM-ESS.2 | Delay mínimo "instantáneo" a 30 s, sin granularidad sub-ciclo |
| **Siemens 3RN2 / 3RU2** | No identificado como feature nombrado | Relés térmicos y termistor, sin detección de flicker |
| **Schneider TeSys LT3 / LTM** | Sin flicker detection | Sin feature diferenciador en gama de overload relays |
| **Eaton C440/C441** | Sin flicker detection | Sin feature nombrado |
| **Rockwell E300** | Trip Delay configurable | Sin detección sub-ciclo de flicker documentada |
| **Chint NJYB2** | Supervisor trifásico OV/UV/pérdida de fase/desequilibrio | Sin detección de flicker |
| **Lovato RF38** | Motor protection relay | Sin flicker detection |
| **Competencia residencial VE genérica** | Protección básica OV/UV con tiempo ajustable | Sin especificación de sub-ciclo en ms |

**Diferenciador real:** 20 ms en datasheet HDE v10 del GSM-L es la
especificación más agresiva identificada en el segmento de supervisores de
voltaje monofásico de gama baja residencial/comercial. La competencia
industrial de alta gama (analizadores de red, power quality analyzers) tiene
detección sub-ciclo pero no es la misma categoría de producto, ni el mismo
punto de precio, ni el mismo mercado.

### Normas IEC aplicables

- IEC 61000-4-4 (transientes eléctricas rápidas — EFT/B)
- IEC 61000-4-14 (fluctuaciones de voltaje — voltage fluctuations)
- IEC 61000-4-15 (flicker meter — functional and design specifications)
- IEC 60947-1 (low-voltage switchgear and controlgear — general rules)

### Caveat legal actualizado (Bruna BR-2 v2.0 Re-Gate 5)

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
> combinados: (a) distancia semántica de la traducción — la traducción al
> español no es descriptor funcional para el consumidor del producto;
> (b) familia de marcas del mismo titular — FlickerGuard entra como una
> marca técnica adicional dentro de la familia Exceline / Exceline Profesional
> / Genius del titular, lo cual sustenta la coherencia del portafolio
> registrable; (c) RTB cuantitativo verificable — la especificación de 20 ms
> en HDE GSM-L v10 (NODO-B verde en análisis competitivo) es el
> diferenciador técnico más sólido del portafolio.
>
> Contingencia OMPI activa: existe evidencia de productos de iluminación LED
> (Australia, UK) que usan el término 'Flicker Guard' como nombre de feature
> en clase 9 amplia. La búsqueda fonética en SAPI Venezuela debe verificar
> si algún titular tiene marca registrada con ese nombre en la subclase de
> dispositivos de protección y supervisión eléctrica con efectos en
> Venezuela."

### Documentos internos Genteca relevantes

- HDE GSM-L versión vigente (v10 o posterior): dato explícito de 20 ms para
  detección de flicker. **Documento primario del RTB de este nodo.**
- HDE GSM-MB / GSM-RB / GSM-RE: datos de 150 ms para desconexión por
  inestabilidad.
- Especificación del algoritmo de detección de pendiente de voltaje
  (documento interno I+D): denominación formal pendiente de confirmación
  (gap G2).

---

## Sección 4 — Documentos internos pendientes que I+D Genteca debe completar

Para el batch inicial SAPI Venezuela (Thermo-Safe + FlickerGuard), hay **2
gaps documentales activos** que I+D Genteca debe ubicar o elaborar antes de
la presentación de la solicitud formal FM-02.

---

### Gap G1 — Parámetros NTC numéricos en HDE (NODO-C / Thermo-Safe)

- **Qué es:** HDE GSM-MB (y equivalentes GSM-RB, GSM-RE) en versión que
  incluya la sección de protección térmica NTC con: rango de temperatura
  de operación, umbral de disparo, histéresis, tiempo de respuesta del
  sensor, tipo de sensor (resistencia nominal a 25 °C), longitud de cable
  del NTC.
- **Para qué se usa:** sin estos parámetros, el claim de protección
  térmica del NODO-C no tiene RTBs numéricos verificables para Antequera.
  La presencia del sensor se confirma por empaque, pero los parámetros de
  funcionamiento no están en HDEs actuales (versiones v6 y v6-rv1 del
  GSM-MB no incluyen sección NTC).
- **Quién en I+D probablemente lo tiene:** el equipo de desarrollo del
  GSM-MB/RB/RE (la protección térmica es la adición más reciente a esta
  gama).
- **Urgencia:** antes de la solicitud FM-02 SAPI. No bloquea el inicio del
  trabajo con Antequera (búsqueda fonética + propuesta de honorarios), pero
  sí bloquea la presentación formal de la solicitud.

---

### Gap G2 — Denominación formal de curva inversa V-t algorítmica (NODO-B / FlickerGuard)

- **Qué es:** confirmación de si existe en I+D algún documento
  (especificación de algoritmo, nota técnica interna, protocolo de prueba)
  que describa formalmente el comportamiento de "tiempo de desconexión
  inversamente proporcional a la desviación de voltaje" y bajo qué nombre
  interno lo denomina Genteca.
- **Para qué se usa:** los datos de respuesta V-t están en las HDEs
  (GSM-AV06: "0,02 a 2 s según intensidad"; GSM-RB: "0,4 a 3 s según
  intensidad") pero el algoritmo como tal no tiene denominación formal en
  documentos actuales. Antequera puede preguntar por la especificación
  técnica del algoritmo si el nombre candidato hace referencia a la curva
  V-t. Si solo existen los tiempos de respuesta de las HDEs, Antequera debe
  saber que el sustento documental es el comportamiento medido, no una
  especificación de algoritmo formal.
- **Quién en I+D probablemente lo tiene:** diseñador del algoritmo de
  supervisión de voltaje para la gama GSM.
- **Urgencia:** antes de la solicitud FM-02 SAPI. Misma criticidad que G1.

---

## Sección 5 — Mini-cover note

### Documento producido

`C:\RAUL\03-projects\genteca\portfolio-naming-ip-2026\06-three-pack\01-Anexo-Tecnico_v2_focus-thermo-safe-flickerguard.md`

### Decisiones de compilación

1. **Scope reducido a 2 nodos:** solo NODO-B y NODO-C del Anexo Técnico
   v1.0. Los otros 6 nodos quedan en el Anexo Técnico v1.0 / v2.0
   completos como referencia para batches posteriores.

2. **Caveats Bruna actualizados:** los caveats integrados son los del
   re-gate Bruna v2.0 (2026-05-19), no los del v1.0 (2026-05-13). Las
   3 correcciones doctrinales de Antequera del 2026-05-18 están
   incorporadas en los rationale.

3. **IMPI México diferido:** se preservan las menciones de productos
   donde vive cada tecnología, pero el análisis de factibilidad en IMPI
   México queda fuera de scope. Diferido para batch México futuro.

4. **Gaps documentales:** solo G1 (NTC) y G2 (curva V-t) son activos para
   este batch. Los gaps G3 (10s TaskMemory) y G4 (Ecosystem GIO) del Anexo
   v1.0 son de los nodos diferidos y no aplican aquí.

5. **Override curva inversa universal:** se preserva el caveat estructural
   del Bruna BR-2 v1.0 Gate 1 porque aplica al NODO-B (y la decisión Gate 1
   no cambió en el re-gate v2.0).

### Items abiertos al Owner / a I+D / a Antequera

**Al Owner:**

- **Escalación E-Caso-B** (NODO-C): activar Caso B (modificación de empaque
  GSM-MB/RB/RE para eliminar "PROTECCIÓN TÉRMICA" del front) antes de la
  solicitud FM-02 SAPI. Decisión comercial-operativa que requiere
  coordinación con Oz / Producción.
- **Escalación E-Titular** (transversal): confirmar con Liliam quién es el
  titular registrado actual de Exceline / Exceline Profesional / Genius en
  SAPI Venezuela.

**A I+D:**

- **Gap G1:** parámetros NTC numéricos en HDE GSM-MB/RB/RE — urgente antes
  de FM-02.
- **Gap G2:** denominación formal de curva inversa V-t en docs internos —
  urgente antes de FM-02.

**A Antequera (resumen — ver detalle en Naming Bible v2 focused):**

- Búsqueda fonética prioritaria de los 10 candidatos del batch inicial.
- Búsqueda OMPI específica para FlickerGuard con designación VE.
- Dictamen sobre Caso B para Thermo-Safe.
- Dictamen sobre reconocimiento explícito de doctrina de familia de marcas
  en SAPI Venezuela.
- Propuesta de honorarios y cronograma del batch inicial.

---

*Anexo Técnico v2 focused — 2 nodos, batch SAPI Venezuela inicial. Compilado*
*por Raul (Genteca IP) sobre Bruna BR-2 v2.0 re-gate. Fecha: 2026-05-19.*
*Documento companion del Deck v3 focused y de la Naming Bible v2 focused.*
