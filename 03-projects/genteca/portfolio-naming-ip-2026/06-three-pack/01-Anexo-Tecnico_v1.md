---
doc_type: anexo-tecnico
project_id: portfolio-naming-ip-2026
domain: genteca
version: v1.0
audience: Abogado marcario externo (TBD asignación legal)
compiled_by: Vera
fecha: 2026-05-13
related_files:
  - 02-Naming-Bible_v1.md
  - 03-Deck-lawyer-presentation_v1.md
---

# Anexo Técnico — Portafolio de Tecnologías Genteca
## Base técnica para registro de marcas IP — Clase 9 (SAPI Venezuela + IMPI México)

---

## Sección 1 — Introducción para el abogado

### Qué es este documento

Este documento describe el portafolio de tecnologías diferenciadoras de Genteca que sostiene los nombres candidatos para registro de marca presentados en el Naming Bible (archivo companion). Cada tecnología se presenta como un nodo independiente, con su mecanismo técnico, los datos cuantitativos verificables que lo distinguen, su posicionamiento frente a los competidores relevantes del segmento, y los caveats legales aplicables al nombre anchor o candidatos asociados.

El propósito del documento es dar al abogado marcario la base técnica suficiente para evaluar la registrabilidad de cada nombre en SAPI Venezuela (Ley de Propiedad Industrial 1955, LPI VE) y en IMPI México (Ley Federal de Protección a la Propiedad Industrial 2020, LFPPI MX), identificar qué documentación interna de Genteca puede pedirse como respaldo, y distinguir los nombres con perfil de signo de fantasía defendible de los que tienen riesgo de descriptividad o colisión que requieren argumento específico ante el examinador.

### Cómo navegarlo

El documento cubre **8 nodos tecnológicos (NODO-A a NODO-H)**, organizados de la siguiente manera:

- **Sección 2:** Tabla maestra de los 8 nodos para vista rápida.
- **Sección 3:** Detalle por nodo. Cada entrada incluye: mecanismo técnico con parámetros numéricos, productos donde vive, RTBs verificables con referencia documental, estado de diferenciación competitiva (Orlan), caveats legales aplicables (Bruna BR-2), y documentos internos que el abogado puede pedir.
- **Sección 4:** Lista consolidada de documentos internos que I+D debe ubicar o elaborar antes de la reunión con el abogado.
- **Sección 5:** Notas de discrepancia y pendientes técnicos.
- **Sección 6:** Mini-cover note.

El abogado puede leer la Tabla Maestra (Sección 2) en 5 minutos para orientarse y luego profundizar en los nodos con mayor riesgo o mayor prioridad de registro.

### Universo de productos cubierto

| Línea comercial | Productos cubiertos | Audiencia primaria |
|---|---|---|
| **Exceline** | GSM-MB (120B / 220B), GSM-RB (R120B / R220B), GSM-RE (RE120A / RE220M), GSM-NG (enchufable neveras alta gama), GSM-L | Residencial + comercios pequeños/medianos |
| **Exceline Profesional** | GRN-MV (relé de nivel), GSC-CR, GSC-MB, GSM-AV06, GSM-L (portador principal del RTB de 20ms) | Industria + comercio profesional, instaladores |
| **Genius** | GI+, GII+, GOCT, GUCT+, GSPT, GSPT-MV, GIII+, GIII+MV, GOC; accesorios GIO-Link (USB/RS-232/RS-485) y software GIO-Tool | Premium, especificadores, ingeniería de mantenimiento |

### Caveat estructural único — Override curva inversa (aplicable a NODO-B y NODO-D)

"La presencia de la curva inversa I-t cold/hot y de la curva inversa V-t algorítmica se indica como universal de facto para la gama Exceline / Exceline Profesional / Genius. La verificación producto por producto está pendiente de auditoría formal por I+D de Genteca y debe completarse antes de la primera publicidad comparativa externa que use la función como diferenciador. En el contexto de este proceso de registro de marca, la función se documenta con base en los productos Genius y Exceline Profesional en los que Vera la confirmó en HDE."

Este caveat aplica en su totalidad a las menciones de curva inversa V-t algorítmica (NODO-B) y curva inversa I-t cold/hot (NODO-D) en este documento. No se repite en cada nodo.

---

## Sección 2 — Tabla maestra de nodos

| Nodo | Título funcional | Anchor / Candidato 1 | Línea comercial primaria | Estado competitivo (Orlan) | Caveat Bruna (BR-2) |
|---|---|---|---|---|---|
| NODO-A | Reconexión temporal aleatoria post-falla | StaggerStart | Exceline / Exceline Profesional | Amarillo | Ninguno (nombre limpio) |
| NODO-B | Detección sub-ciclo de perturbaciones de voltaje (flicker + curva inversa V-t) | FlickerGuard | Exceline / Exceline Profesional | Verde | Aprobado con contingencia — verificar colisión OMPI/LED clase 9 |
| NODO-C | Modelo térmico NTC integrado en protector monofásico | Thermo-Safe | Exceline (GSM-MB/RB/RE) | Amarillo | Aprobado con caveat Caso A — argumento fantasía ante examinador |
| NODO-D | Curva inversa I-t diferenciada cold/hot (algoritmo imagen térmica) | ThermalCurve RECHAZADO — candidatos nuevos en Naming Bible | Exceline Profesional / Genius | Rojo | Nombre rechazado por descriptividad. Nodo sigue siendo registrable |
| NODO-E | Registro forense histórico de fallas con timestamp | ForensLog | Genius (GIII+MV primario) | Amarillo | Aprobado — postura Escenario A (RTB acotado a GIII+MV) |
| NODO-F | Bloqueo permanente tras tercera falla de corriente recurrente | TripleLock | Exceline Profesional / Genius | Amarillo | Aprobado con contingencia — verificar colisión seguridad física clase 9 |
| NODO-G | Memoria de estado y reanudación de tarea post-corte | TaskMemory | Exceline Profesional (GRN-MV) | Verde | Aprobado diferenciado por jurisdicción: VE principal, MX verificar software |
| NODO-H | Ecosystem GIO — conectividad industrial integrada (GIO PORT + GIO-Link + GIO-Tool) | Candidatos familia GIO-* en Naming Bible | Genius (gama completa) | Amarillo | Aprobado — instrucción explícita: NO usar "MODBUS" ni términos de protocolo estándar |

---

## Sección 3 — Detalle por nodo

---

### NODO-A: Reconexión temporal aleatoria post-falla

#### Mecanismo técnico

Cuando la tensión de alimentación retorna al rango normal tras un corte o evento de voltaje, el protector no reconecta la carga en el instante exacto de la recuperación. Ejecuta un retardo compuesto de dos componentes: (1) un tiempo mínimo configurable por el usuario que garantiza que el compresor completó su ciclo de presión antes del arranque, y (2) una componente aleatoria dentro de la ventana configurada que hace que dos o más protectores idénticos en la misma instalación no reconecten simultáneamente. El resultado es el escalonamiento automático del arranque entre cargas — sin coordinación externa ni red de comunicación.

- **Inputs:** señal de voltaje en rango (detección de restablecimiento)
- **Transformación:** generación de un retardo con componente aleatoria sobre el tiempo mínimo configurado
- **Outputs:** cierre del contacto de salida en momento escalonado y no predecible para el conjunto de dispositivos en la instalación
- **Parámetros:** ventana ajustable 5-180 s (GSM-MB v6); 180-300 s (GSM-RB); 3 min fijo (GSM-NG); 5-300 s (GSM-L)

#### Productos donde vive

- Exceline: GSM-MB (120B / 220B), GSM-RB (R120B / R220B), GSM-RE (RE120A / RE220M), GSM-NG
- Exceline Profesional: GSM-L
- Override Owner: función asumida presente en toda la gama Exceline / Exceline Profesional / Genius con función de temporizado post-falla

#### RTBs verificables

1. Componente aleatoria documentada en HDE GSM-MB v3-n, v4, v5, v6, v6-rv1: "sistema aleatorio para evitar que dos o más equipos protegidos arranquen en simultáneo".
2. Temporizado ajustable 5-180 s (GSM-MB v6, HDE); 3 min fijo (GSM-NG, HDE).
3. GSM-NG HDE: "temporizado aleatorio para evitar arranque simultáneo".
4. Función anti-demand-spike en instalaciones con múltiples protectores: inferida del mecanismo, implícita en documentación.
5. Normas verificadas: IEC 61000-4-x (EMC), COVENIN 3445.

#### Diferenciación competitiva (Orlan OL-1)

Estado: AMARILLO

- **Eaton C445:** implementa función equivalente bajo el nombre "Voltage Loss Restart" — nombre descriptivo funcional, no fantástico. Aplicación note Eaton ap042004en disponible públicamente. Orientado a motores industriales en MCC, configurado vía red EtherNet/IP o DeviceNet. No compite directamente en el segmento residencial/comercial de VE/MX.
- **Siemens:** función de "connection delay" o "start-up delay" configurable, sin nombre de fantasía identificado.
- **Rockwell E300:** "Start Delay" configurable post-falla, sin nombre de fantasía.
- **Chint / Lovato / LS:** tiempo de rearme ajustable sin branding de fantasía identificado.

Diferenciador real: la implementación Genteca opera en un protector enchufable de bajo costo para el segmento residencial/comercio pequeño, sin red de comunicación, en un punto de precio donde Eaton C445 no compite directamente en VE/MX. El diferenciador no es la función en abstracto; es la ejecución en el segmento + simplicidad + punto de precio.

#### Caveats legales aplicables (Bruna BR-2)

Ninguno. El nombre StaggerStart tiene perfil de signo de fantasía defendible: "Stagger" es técnico y raro en el vocabulario cotidiano del consumidor venezolano o mexicano, "Start" como sufijo solo es genérico. La combinación no describe literalmente el producto eléctrico para el consumidor promedio. El espacio semántico "Stagger" como raíz no tiene presencia de marcas de fantasía registradas en clase 9 en LatAm identificadas. Nota para el abogado: "Voltage Loss Restart" (Eaton) es un claim descriptivo, no una marca registrada — no constituye colisión con StaggerStart.

#### Documentos internos Genteca relevantes

- HDE GSM-MB versión vigente (v6 o posterior): especificación del algoritmo de temporizado aleatorio y rango de variación.
- HDE GSM-RB / GSM-RE: confirmación de la misma función.
- HDE GSM-NG: confirmación en formato enchufable.
- Manual de usuario (si existe separado): descripción del rango de variación aleatoria en segundos o como porcentaje del mínimo configurado.

---

### NODO-B: Detección sub-ciclo de perturbaciones de voltaje (flicker + curva inversa V-t)

#### Mecanismo técnico

El algoritmo de supervisión de voltaje tiene dos comportamientos integrados en el mismo dispositivo:

**(1) Detección de flicker:** el dispositivo muestrea el voltaje a frecuencia suficiente para detectar inestabilidad o parpadeo en ventana de 20 ms (GSM-L) o 150 ms (GSM-MB, GSM-RB). Si detecta variación sub-ciclo, desconecta la carga sin esperar que el voltaje salga del rango de ajuste estático.

- Inputs: señal de voltaje con variaciones rápidas
- Transformación: algoritmo de detección de pendiente o variación súbita en ventana menor a 1 ciclo de 60 Hz
- Outputs: desconexión inmediata

**(2) Curva inversa V-t algorítmica (override universal de facto — ver caveat Sección 1):** el tiempo de desconexión es inversamente proporcional a la desviación del voltaje respecto al umbral configurado. Una desviación extrema produce desconexión casi instantánea; una desviación marginal produce desconexión con retardo mayor.

- Parámetros documentados: 0,02 a 2 s según intensidad de falla (GSM-AV06 HDE); 0,4 a 3 s según intensidad (GSM-RB HDE); 20-30 ms para fallas extremas en GSM-AV06.

**Nota de denominación:** el comportamiento V-t proporcional está documentado en las HDEs con datos de tiempo específicos, pero la denominación formal "curva inversa V-t algorítmica" no aparece en los documentos Genteca actuales. Es la descripción técnica correcta del comportamiento subyacente. I+D debe confirmar si existe especificación interna con esa denominación (ver Sección 4, ítem 2).

#### Productos donde vive

- GSM-L: 20 ms de detección de flicker (dato explícito en HDE v10 — portador principal del RTB)
- GSM-MB, GSM-RB, GSM-RE: 150 ms por flicker/inestabilidad
- GSM-AV06: 0,02-2 s según intensidad
- GSM-NG: 150 ms
- Override Owner: gama completa Exceline / Exceline Profesional / Genius

#### RTBs verificables

1. Tiempo de detección de flicker: **20 ms** (GSM-L HDE v10 — dato explícito, único en la gama). Referencia: HDE GSM-L versión v10.
2. Tiempo de detección genérica de falla de voltaje (GSM-L): a partir de **60 ms**. Referencia: HDE GSM-L v10.
3. Tiempo de desconexión por flicker/inestabilidad (GSM-MB, GSM-RB, GSM-NG): **150 ms**. Referencia: HDEs respectivas.
4. Desconexión variable según intensidad: **0,02 a 2 s** (GSM-AV06 HDE); **0,4 a 3 s** (GSM-RB HDE).
5. Detección de parpadeos e inestabilidad como causa de desconexión: documentada en HDEs GSM-MB, GSM-RB, GSM-RE, GSM-L, GSM-NG.
6. Normas: IEC 61000-4-4 (transientes rápidas), IEC 61000-4-14 (fluctuaciones de voltaje), IEC 60947-1.

#### Diferenciación competitiva (Orlan OL-1)

Estado: VERDE

- **ABB CM-ESS:** supervisor de voltaje con delay mínimo "instantáneo" a 30 s. Datasheet CM-ESS.2 consultado: no especifica tiempo de detección de flicker en milisegundos.
- **Siemens 3RN2 / 3RU2:** relés térmicos y termistor. Flicker detection no identificado como feature nombrado.
- **Schneider TeSys LT3 / LTM:** sin flicker detection como feature diferenciador en gama de overload relays.
- **Eaton C440/C441:** sin flicker detection como feature nombrado.
- **Rockwell E300:** protección de voltaje con Trip Delay configurable; sin detección sub-ciclo de flicker documentada.
- **Chint NJYB2:** supervisor trifásico con OV/UV/pérdida de fase/desequilibrio. Sin detección de flicker como feature (fuente primaria consultada).
- **Lovato RF38:** motor protection relay. Sin flicker detection documentada (catálogo Lovato consultado).
- **Competencia residencial VE (genérica):** protección básica OV/UV con tiempo ajustable. Sin especificación de sub-ciclo en ms que compita con 20 ms del GSM-L.

Diferenciador real: 20 ms en datasheet HDE v10 del GSM-L es la especificación más agresiva identificada en el segmento de supervisores de voltaje monofásico de gama baja residencial/comercial. La competencia industrial de alta gama (analizadores de red, power quality analyzers) tiene detección sub-ciclo pero no es la misma categoría de producto, ni el mismo punto de precio, ni el mismo mercado.

#### Caveats legales aplicables (Bruna BR-2, Gate 5)

"FlickerGuard: nombre de fantasía en clase 9. Existe evidencia de productos de iluminación LED (Australia, UK) que usan el término 'Flicker Guard' como nombre de feature en el mismo segmento Niza Clase 9. La búsqueda fonética en SAPI Venezuela y en IMPI México debe verificar si hay marcas registradas o en trámite con ese nombre en la subclase de dispositivos de protección y supervisión eléctrica. La coexistencia entre un supervisor de voltaje para protección de compresores y una luminaria de iluminación LED puede ser navegable bajo argumento de distinción de producto."

Solenne tiene preparados candidatos alternativos (contingencia OMPI) con raíces Flicker+Trap, Flicker+Block, Flicker+Shield, PulseGuard, SagGuard — disponibles si la búsqueda formal confirma colisión activa.

#### Documentos internos Genteca relevantes

- HDE GSM-L versión vigente (v10 o posterior): dato explícito de 20 ms para detección de flicker. Documento primario del RTB de este nodo.
- HDE GSM-MB / GSM-RB / GSM-RE: datos de 150 ms para desconexión por inestabilidad.
- Especificación del algoritmo de detección de pendiente de voltaje (documento interno I+D): no confirmado en KB como doc independiente; puede no existir como HDE separada.

---

### NODO-C: Modelo térmico NTC integrado en protector monofásico

#### Mecanismo técnico

Sensor de temperatura NTC embebido en el protector monofásico GSM-MB/RB/RE. El sensor lee la temperatura real del entorno del compresor o del devanado (según instalación). La lógica interna compara la temperatura medida con umbrales configurados o fijos y actúa la desconexión si se detecta sobrecalentamiento. A diferencia del modelo I-t algorítmico del NODO-D, este nodo usa medición física de temperatura con un componente de hardware en el circuito de decisión — el sensor NTC.

- **Inputs:** lectura analógica del sensor NTC (resistencia variable con temperatura)
- **Transformación:** comparación de la temperatura medida contra umbral térmico de disparo
- **Outputs:** desconexión de la carga + indicación en LED del protector

**Nota de gap documental:** los parámetros técnicos del NTC (rango de temperatura de operación, umbral de disparo, histéresis, tiempo de respuesta, resistencia nominal a 25 °C) no están documentados en las HDEs actuales de la KB (versiones v6 y v6-rv1 del GSM-MB no incluyen sección NTC). La presencia del sensor se confirma por empaque pero los RTBs numéricos específicos del NTC no están disponibles en la documentación actual. Este gap es el más urgente del portafolio para el proceso IP (ver Sección 4, ítem 1).

#### Productos donde vive

GSM-MB (120B y 220B), GSM-RB (R120B y R220B), GSM-RE (RE120A y RE220M) — todos en versión actual con protección térmica ("AHORA CON PROTECCIÓN TÉRMICA", confirmado en etiqueta de empaque HDE GLA_T versiones V10/V9/V13).

#### RTBs verificables

1. Sensor NTC presente en hardware: confirmado en etiqueta de empaque GSM-MB (GLA_T V10), GSM-RB (GLA_T V9), GSM-RF (GLA_T V13).
2. Mención "PROTECCIÓN TÉRMICA" explícita en empaque versiones V10/V9/V13. Referencia: etiqueta empaque HDE GLA_T.
3. **Parámetros numéricos del NTC (rango de temperatura, umbral de disparo):** no disponibles en HDEs actuales de la KB. Requieren actualización de HDE o addendum de I+D antes de la reunión con el abogado.

#### Diferenciación competitiva (Orlan OL-1)

Estado: AMARILLO

- **Siemens SIMOCODE pro 3UF7:** soporta NTC, KTY83/84, PT100/PT1000 mediante "Temperature Module" — módulo separado, nombre descriptivo, no fantástico. Datasheet SIMOCODE consultado.
- **Schneider TeSys T LTMR:** soporta PTC Analog y NTC Analog. Denominado "Motor Temperature Sensing" function — descriptivo. User guide LTMR consultado.
- **Eaton C440/C441:** termistor como opción, sin nombre de fantasía identificado.
- **ABB / Siemens 3RN2:** termistor PTC dedicado, sin nombre de fantasía.
- **Genius GIII+/GIII+MV:** sensor PTC100 (platino, no NTC). Tecnología distinta al NTC del GSM-MB/RB.

Diferenciador real: el diferenciador no es el sensor NTC per se. Es la integración del NTC en un protector de voltaje monofásico para uso doméstico/comercial como feature estándar de serie (no módulo separado), a un punto de precio de mercado doméstico VE/MX. Siemens requiere módulo adicional con costo y cableado adicional. Ningún competidor identificado ofrece NTC integrado como feature estándar en protectores enchufables o de bornera para AC/refrigeración en el segmento residencial.

#### Caveats legales aplicables (Bruna BR-2, Gate 3)

"Thermo-Safe es nombre de fantasía que no deriva de la descripción funcional del producto. La combinación 'Thermo' (prefijo de origen griego, raíz técnica) + 'Safe' (beneficio de seguridad en inglés) no constituye una descripción literal de la función del producto para el consumidor venezolano o mexicano promedio. El empaque del producto usa la descripción 'PROTECCIÓN TÉRMICA', que es la descripción funcional en español; 'Thermo-Safe' es el nombre de fantasía de la función nombrada y es semánticamente distinto de la descripción funcional en uso. Solicitar registro de marca en Clase 9 con argumentación de signo de fantasía bajo doctrina de equivalencia perceptual."

Nota adicional: si Genteca elimina la mención de protección térmica del empaque antes del proceso de registro, el perfil de riesgo de descriptividad baja de medio-alto a medio. Esa es una decisión comercial/diseño del Owner, no un requisito de la presentación al abogado.

#### Documentos internos Genteca relevantes

- HDE GSM-MB en versión que incluya la sección de protección térmica NTC (versión posterior a v6, o addendum). Actualmente no disponible en KB. Documento más urgente del portafolio para el proceso IP.
- HDE GSM-RB y GSM-RE equivalentes con sección NTC.
- Especificación del sensor NTC: rango de temperatura, umbral de desconexión, tipo de sensor (resistencia nominal a 25 °C), longitud de cable si aplica.

---

### NODO-D: Curva inversa I-t diferenciada cold/hot (algoritmo imagen térmica)

#### Mecanismo técnico

Algoritmo de protección por sobrecarga basado en modelo de imagen térmica según IEEE C37.112 e IEC 60255-8. El relé calcula continuamente el "calor acumulado" del motor usando la corriente medida, la clase térmica seleccionada y el estado térmico anterior (frío o caliente). El tiempo de disparo ante una sobrecarga es inversamente proporcional al nivel de sobrecarga relativo al nominal.

La diferenciación cold/hot opera de la siguiente manera: si el motor arrancó en frío (energía térmica acumulada baja o nula), aplica la curva fría completa de la clase ajustada; si el motor ya estaba caliente (energía térmica acumulada alta por un ciclo reciente de trabajo), aplica la curva caliente = curva fría / 3. Esto significa que ante un arranque en caliente, el disparo ocurre hasta 3 veces más rápido para el mismo nivel de sobrecarga.

- **Inputs:** corriente medida por CT + estado térmico almacenado en memoria
- **Transformación:** cálculo de imagen térmica según clase IEC 60255-8; comparación contra umbral del 100 % de imagen térmica calculada
- **Outputs:** disparo por sobrecarga con tiempo inversamente proporcional a (I/Inom)
- **Parámetros:** curva caliente = curva fría / 3; tiempo máximo entre estados cold/hot: 2 horas; clase ajustable 5 a 30 en pasos de 1 (GUCT+, GIII+, GSPT-MV); clase 10 fija con curva fría 10, caliente 3 (GOCT, GOC)

#### Productos donde vive

GOCT (Clase 10 fija: curva fría 10, caliente 3); GUCT+ (Clase ajustable 5-30); GSPT / GSPT-MV (Clase 10 fija, cold/hot documentado con curva gráfica en HDE); GIII+ / GIII+MV (Clase ajustable 5-30, cold/hot documentado); GOC (Clase 10 fija, cold curve 10, hot curve 3). Override Owner: curva inversa I-t cold/hot asumida universal en gama Exceline / Exceline Profesional / Genius.

#### RTBs verificables

1. Relación curva caliente / curva fría: **Caliente = Fría / 3**. Referencia: GIII+ HDE sección E; GOC HDE sección E (explícito: cold curve 10, hot curve 3).
2. Tiempo máximo entre estados cold/hot: **2 horas**. Referencia: GIII+ HDE sección E.
3. Clase térmica ajustable: **5 a 30 en pasos de 1**. Referencia: GUCT+, GIII+, GSPT-MV (HDEs y catálogo).
4. Umbral de disparo por sobrecarga: **100 %** de la imagen térmica calculada. Referencia: HDEs individuales.
5. Implementación normativa: **IEC 60255-8-1990** e **IEEE C37.112-1996**. Citados en HDEs de GIII+, GSPT-MV, GOC.
6. Memoria térmica: retención del estado térmico al apagarse el equipo. Referencia: GOCT, GSPT, GIII+, GOC HDEs.

#### Diferenciación competitiva (Orlan OL-1)

Estado: ROJO

La curva inversa I-t cold/hot es función estándar de IEC 60947-4-1 / IEC 60255-8 / IEEE C37.112, presente y documentada en la competencia industrial relevante: Siemens 3RB3 (fuente primaria: manual SIRIUS consultado), Schneider TeSys T LTMR (fuente: user guide LTMR con thermal model), Rockwell E300 (fuente: E300 user manual con thermal memory), Eaton C441 (claim basado en documentación C441). La "Thermal Memory" como concepto es término genérico en múltiples fabricantes. El ratio cold/hot de la implementación Genteca (1:3) es la especificación del estándar IEC/IEEE, no un parámetro propietario.

Diferenciador real: no hay diferenciador genuinamente único en la función base con los RTBs disponibles. El override del Owner asume la función universal. Si I+D puede documentar un parámetro de implementación que exceda el estándar IEC (factor de enfriamiento diferencial propio, parámetro de memoria térmica con valor específico no derivado de la norma), ese RTB cambiaría el estado a amarillo o verde.

#### Caveats legales aplicables (Bruna BR-2, Gate 2)

**El nombre ThermalCurve fue RECHAZADO.** Describe literalmente el mecanismo técnico estándar de la categoría. En SAPI Venezuela (art. 34 LPI 1955) y IMPI México, una marca descriptiva de la función del producto en la misma clase Niza es causal de inadmisibilidad. La probabilidad de objeción por parte del examinador es alta.

**El NODO-D sigue siendo nodo registrable.** La decisión de rechazo es sobre el nombre ThermalCurve, no sobre el nodo. La curva cold/hot es un diferenciador de naming incluso siendo función estándar IEC, porque ningún competidor la tiene nombrada con fantasía. Los 4 candidatos alternativos para NODO-D se encuentran en el Naming Bible. La dirección semántica aprobada por Bruna: alejarse completamente del territorio "curva" y "térmica"; raíces que evoquen adaptación, estado, respuesta proporcional.

**Condición de reapertura para ThermalCurve:** si I+D puede documentar un parámetro propietario de la implementación Genteca que exceda el estándar IEC (factor de enfriamiento diferencial con especificación propia, parámetro de memoria térmica diferenciado, u otro aspecto del algoritmo no derivable directamente de la norma), Bruna puede revisar el rechazo con un VR-1 actualizado de Vera.

#### Documentos internos Genteca relevantes

- HDE GIII+ o GSPT-MV (versión vigente): contienen la gráfica de curva fría/caliente por clase. Documentos primarios del RTB de este nodo.
- HDE GOC / GOCT: confirman cold curve 10, hot curve 3 de forma explícita.
- Manual de usuario GIII+ (sección de algoritmos de protección): descripción del mecanismo de imagen térmica.
- Especificación de implementación del algoritmo IEEE C37.112 (si existe documento interno I+D separado de las HDEs).

---

### NODO-E: Registro forense histórico de fallas con timestamp

#### Mecanismo técnico

El relé registra en memoria no volátil cada evento de falla con cuatro campos: tipo de falla, valor medido al momento de la falla, hora y fecha del evento (timestamp), y duración del evento. El registro es circular: al alcanzar la capacidad máxima, el evento más antiguo es sobreescrito. El usuario puede consultar el registro mediante pantalla LCD o a través del puerto de comunicación MODBUS RTU. El GIII+MV además retiene los parámetros de configuración activos al momento de cada falla, permitiendo auditar si el disparo fue correcto dado el ajuste vigente.

- **Inputs:** evento de falla (cualquier protección activada)
- **Transformación:** indexación con timestamp de reloj interno + retención del valor medido y duración
- **Outputs:** registro consultable en pantalla o vía bus MODBUS RTU
- **Parámetros:** capacidad máxima 100 últimas fallas (GIII+MV); 20 últimas fallas (gama Genius estándar: GI+, GII+, GIII+, GUCT+, GSPT, GSPT-MV, GOC, GOCT)

#### Productos donde vive

- GIII+MV: **100 últimas fallas** (portador principal del RTB máximo — HDE GIII+MV-V1 y gd-he8003-ve-v1)
- GIII+, GUCT+, GSPT, GSPT-MV, GOC, GOCT, GI+, GII+: **20 últimas fallas** (catálogo Genius)
- El GIII+MV es el portador principal del nombre ForensLog según postura del deck (Escenario A aprobado por Bruna)

#### RTBs verificables

1. Capacidad máxima: **100 últimas fallas** (GIII+MV). Referencia: HDE GIII+MV-V1 versión inglés y español (gd-he8003-ve-v1). Dato verificado en fuente primaria.
2. Capacidad baseline gama Genius: **20 últimas fallas**. Referencia: HDE GIII+ biblioteca técnica; catálogo Genius 03/2025.
3. Campos por evento: tipo de falla + valor medido + hora + fecha + duración. Referencia: HDE GIII+ sección F.
4. Retención de parámetros activos al momento de falla: documentada en HDE GIII+MV sección comunicaciones.
5. Acceso dual: pantalla LCD + puerto MODBUS RTU.
6. Reloj con fecha integrado en GIII+ (programador horario documentado en HDE).
7. Comparativo competitivo verificado: Rockwell E300 tiene 5 trip records + 5 warning records = 10 registros totales (fuente: manual E300 193-UM015, ManualsLib). La diferencia es 10:1 respecto al GIII+MV.

#### Diferenciación competitiva (Orlan OL-1)

Estado: AMARILLO

- **Rockwell E300:** 5 trip history + 5 warning history = 10 registros totales. Fuente verificada: manual E300 193-UM015.
- **ABB REF615 (gama subestación):** 2048 audit trail events — pero es sistema de protección de subestación / media tensión, no relé de motor de baja tensión. No es competidor directo en VE/MX en la misma clase de producto.
- **Schneider TeSys T LTMR:** registros de diagnóstico mencionados en user guide; número exacto de registros no confirmado en fuente primaria.
- **Eaton C441 / Siemens SIMOCODE:** capacidad de registro de fallas no confirmada en datasheet primario en esta investigación.

Diferenciador real: 100 registros (GIII+MV) vs 10 registros (Rockwell E300, único competidor con dato verificado) = diferenciador cuantitativo 10:1 en el segmento de relés de motor de baja tensión. La capacidad diferenciadora (100 eventos) es exclusiva del GIII+MV dentro del portafolio Genteca; el baseline de la línea Genius es 20 fallas.

#### Caveats legales aplicables (Bruna BR-2, Gate 4)

"El RTB del nombre ForensLog descansa en el GIII+MV con capacidad de registro de 100 últimas fallas con timestamp. El baseline de la gama Genius es 20 últimas fallas. El nombre ForensLog se vincula a la tecnología de registro forense como concepto, no a un número específico de eventos — el abogado puede optar por vincular el nombre al GIII+MV como portador principal del RTB de máxima capacidad."

Nota al abogado: "Log" tiene presencia en software/apps en Clase 9 amplia. La búsqueda fonética debe incluir la subclase de software de diagnóstico industrial. Solenne tiene candidatos alternativos (ForensTrace, FaultVault, DiagLog) disponibles si la búsqueda encuentra colisión activa.

#### Documentos internos Genteca relevantes

- HDE GIII+MV (versión vigente): confirma 100 últimas fallas y campos de registro. Documento primario del RTB principal.
- Manual GIII+MV: sección de consulta de histórico de fallas.
- HDE GIII+ estándar: confirma 20 últimas fallas como baseline de la gama.

---

### NODO-F: Bloqueo permanente tras tercera falla de corriente recurrente

#### Mecanismo técnico

Si el relé detecta 3 fallas de corriente (sobrecarga, pérdida de fase por corriente, desbalance de corriente) dentro de una ventana de 30 minutos, ejecuta una desconexión permanente que requiere intervención manual explícita para restablecer la operación. Las dos primeras fallas permiten rearranque automático (modo Auto); la tercera dentro de la ventana activa el bloqueo. La lógica opera independientemente del tipo específico de falla de corriente: cualquier combinación de 3 eventos de corriente en la ventana activa el bloqueo.

- **Inputs:** contador de fallas de corriente + temporizador de ventana de 30 minutos
- **Transformación:** comparación del contador contra umbral 3 dentro de la ventana
- **Outputs:** desconexión permanente con indicación en pantalla o LEDs; requiere reset manual para restablecer
- **Parámetros:** ventana de tiempo = 30 minutos; umbral = 3 fallas de corriente; tiempo de disparo en tercera falla = < 1 s

#### Productos donde vive

- Genius: GOCT, GUCT+, GSPT, GSPT-MV, GIII+, GIII+MV, GOC
- Exceline Profesional: GSC-CR, GSC-MB (según catálogo trifásico)

Nota: el spec del GOC está marcado como "versión histórica" en la KB. I+D debe confirmar si el GOC está activo en el portafolio actual. Los demás portadores (GOCT, GUCT+, GSPT, GIII+) son suficientes para sostener el nodo independientemente del status del GOC.

#### RTBs verificables

1. Umbral de bloqueo: **3 fallas de corriente en menos de 30 minutos**. Referencia: GIII+ HDE sección E ("Detección de Tercera (3ª) Falla"); GOC HDE sección E; catálogo Genius tabla comparativa; catálogo trifásico Exceline Profesional.
2. Tiempo de disparo en tercera falla: **< 1 s**. Referencia: GOC HDE sección E ("Trip Delay because of 3 Current Failures: <1 sec in less than 30 min").
3. Reset manual requerido para restablecer operación tras bloqueo permanente: documentado en HDEs y manuales de la gama Genius.
4. Aplica a fallas de corriente de cualquier tipo: OL (sobrecarga), CUB (desbalance de corriente), CSP (pérdida de fase por corriente).

#### Diferenciación competitiva (Orlan OL-1)

Estado: AMARILLO

- **Schneider TeSys T LTMR:** función de "locked rotor" y protecciones con contadores; no se identificó "triple fault lockout" con nombre comercial propio.
- **Siemens 3RU/3RB:** reseteo manual tras sobrecargas; sin "triple fault" lockout con nombre de fantasía.
- **Eaton C440/C441:** funciones de trip inhibit; sin "triple fault" con nombre comercial.
- **Rockwell E300:** "Inhibit Restart" configurable; sin nombre de fantasía para la función triple-falla.
- **ABB / Chint / Lovato / LS:** función de restart inhibit presente en algunos modelos; sin nombre comercial de fantasía identificado.

Diferenciador real: la función existe en la competencia como parámetro ajustable o configurable, pero ningún fabricante identificado la tiene nombrada con fantasía. Genteca puede reclamar la función con nombre y posicionarla como feature premium visible, no como configuración oculta. La diferencia cualitativa es que el bloqueo es automático (no configurable por el usuario) y el nombre lo convierte en feature diferenciador.

#### Caveats legales aplicables (Bruna BR-2, Gate 6)

"TripleLock: nombre de fantasía en clase 9. La raíz 'Lock' tiene presencia en marcas de sistemas de seguridad física (cerraduras electrónicas, control de acceso) en Clase 9. La búsqueda fonética debe verificar si existen titulares activos con marcas que incluyan 'TripleLock' o 'Triple Lock' en la subclase de dispositivos de seguridad o protección en SAPI Venezuela y en IMPI México. La distinción de producto entre un relé de protección eléctrica para motores y un sistema de acceso físico es argumento disponible ante el examinador si hay coexistencia en la misma clase Niza."

Solenne tiene candidatos alternativos con raíces Gate, Hold, Block, Halt (contingencia sectorial) disponibles si la búsqueda confirma colisión activa.

#### Documentos internos Genteca relevantes

- HDE GIII+ / GIII+MV: sección E de funciones y algoritmos, parámetro "Detección de Tercera (3ª) Falla". Documento primario del RTB.
- HDE GOC: sección E, confirmación de < 1 s para el disparo en tercera falla.
- Manual de usuario de cualquier relé Genius con imagen térmica: sección de descripción del modo de rearme y bloqueo permanente.

---

### NODO-G: Memoria de estado y reanudación de tarea post-corte

#### Mecanismo técnico

El GRN-MV (relé de nivel para líquidos conductores) almacena en memoria no volátil el modo operativo activo al momento de un corte eléctrico. Los tres modos posibles son: vaciado de pozo (bomba activa drenando), llenado de tanque (bomba activa llenando), y espera (nivel alcanzado). Al restablecerse la alimentación, el relé retoma automáticamente la tarea que estaba ejecutando, sin requerir intervención del usuario. Adicionalmente, hay un tiempo de confirmación de 10 segundos antes de que el relé actúe la salida, para evitar actuaciones por microinterrupciones.

- **Inputs:** lectura de sondas de nivel (conductividad del líquido) + modo operativo almacenado en memoria no volátil
- **Transformación:** recuperación del modo almacenado + lectura del estado actual de sondas + decisión de actuación
- **Outputs:** activación del relé de control en el modo correspondiente (vaciado/llenado/espera)
- **Parámetros:** 3 modos de operación persistidos; tiempo de confirmación = 10 s (confirmado verbalmente por I+D, pendiente de actualización documental en HDE/manual — ver Sección 4, ítem 3); sensibilidad de activación ajustable por perilla

#### Productos donde vive

GRN-MV (Exceline Profesional, relé de nivel para líquidos conductores). Tecnología específica de este producto.

#### RTBs verificables

1. Modos de operación persistidos en memoria no volátil: vaciado de pozo, llenado de tanque, espera. Referencia: HDE GRN-MV v9, sección características generales.
2. Reanudación automática post-corte sin intervención del usuario: documentado en HDE GRN-MV v9. Texto literal: "Si el equipo se encontraba en proceso de vaciado o llenado al momento del corte, retoma automáticamente la última función al restablecerse la energía, sin requerir intervención del usuario."
3. Tiempo de confirmación de 10 segundos: confirmado verbalmente por I+D, no documentado en HDE v9 actual. Requiere actualización de HDE o addendum antes de la reunión con el abogado (ver Sección 4, ítem 3).
4. Normas verificadas: IEC 61000-4-x (EMC), IEC 60947-1.

#### Diferenciación competitiva (Orlan OL-1)

Estado: VERDE

No se identificó ningún fabricante de la lista obligatoria (ABB, Siemens, Schneider, Eaton, Rockwell, Chint, Lovato, LS) con función equivalente documentada y nombrada comercialmente en el segmento de controladores de nivel/bombeo residencial-comercial. Los controladores de bombeo de la competencia (donde existen) son PLCs o drives programables con memoria de estado implícita en el programa del usuario — no es una función diferenciadora nombrada en relés de nivel para bombeo básico. Los relés de nivel estándar de la competencia simplemente activan/desactivan según el nivel actual al restaurar la energía, sin recordar el modo previo.

Diferenciador real: la persistencia de modo operativo post-corte en un controlador de nivel/bombeo de gama media es una diferenciación real en el contexto de VE/MX, donde los cortes eléctricos son frecuentes. La función elimina la necesidad de supervisión humana en el reencendido.

#### Caveats legales aplicables (Bruna BR-2, Gate 7)

**Decisión diferenciada por jurisdicción:**

"TaskMemory: nombre de fantasía para controlador de nivel de bombeo (GRN-MV). La combinación 'Task' + 'Memory' tiene presencia en terminología de software de gestión de procesos en informática (Clase 9 amplia). La búsqueda fonética debe priorizar la subclase de software y aplicaciones en IMPI México para verificar si hay titulares activos con marcas similares. En SAPI Venezuela, la doctrina de equivalencia perceptual favorece la registrabilidad del nombre para el producto eléctrico (el consumidor de un relé de nivel de bombeo no percibe 'TaskMemory' como descriptor de software informático). Se sugiere que el abogado evalúe si presentar un candidato alternativo específico para IMPI MX si la búsqueda encuentra conflicto en la subclase software."

Postura Bruna: TaskMemory es el candidato principal para SAPI VE. Solenne tiene candidatos alternativos específicamente para IMPI MX si la búsqueda confirma colisión (ModeKeep, StateHold, CycleResume, RetainMode).

#### Documentos internos Genteca relevantes

- HDE GRN-MV versión vigente (v9 o posterior): sección de características generales con descripción del sistema de memoria de tarea. Documento primario del RTB.
- Addendum HDE o actualización que incluya el tiempo de confirmación de 10 s (actualmente ausente en HDE v9 — documento pendiente de I+D, urgente antes de reunión con abogado).
- Manual de usuario GRN-MV (si existe separado): sección de descripción de modos de operación post-corte.

---

### NODO-H: Ecosystem GIO — conectividad industrial integrada

#### Mecanismo técnico

Arquitectura de comunicación industrial embebida en los relés Genius que permite su integración en redes de supervisión y control. El protocolo de comunicación subyacente es MODBUS RTU (estándar abierto de la industria — Modbus Organization), operando a 9600 baud (todos los relés Genius) o 9600/19200/38400 baud (GIII+MV y modelos con RS-485 integrado). El ecosystem propietario Genteca se compone de tres elementos:

- **GIO PORT:** conector propietario integrado en todos los relés Genius. Permite conectar los accesorios GIO-Link.
- **GIO-Link:** familia de adaptadores (GIO-PLUG-USB, GIO-A-RS232K, GIO-A-RS485K) que conectan el GIO PORT a PC o red industrial RS-485.
- **GIO-Tool:** software propietario de Genteca. Monitorización gráfica en tiempo real, extracción de históricos, generación de reportes, exportación CSV.

A través del ecosystem, los relés exponen: corriente (I1/I2/I3), voltaje (L1/L2/L3), frecuencia, kW, kVA, kWh, factor de potencia, temperatura, histórico de fallas, estados de alarma, comandos de encendido/apagado remoto, y lectura/escritura de parámetros de protección (con contraseña). La red puede conectar hasta 32 relés en un bus RS-485.

- **Inputs:** petición MODBUS del maestro (PC con GIO-Tool u otro SCADA)
- **Transformación:** procesamiento de registro MODBUS RTU con mapeo de variables eléctricas y estados del relé
- **Outputs:** respuesta MODBUS + posibles acciones de control remoto

#### Productos donde vive

Toda la gama Genius: GI+, GII+, GOCT, GUCT+, GSPT, GSPT-MV, GIII+, GIII+MV, GOC (todos con GIO PORT + MODBUS RTU). GIII+ y GIII+MV adicionalmente con RS-485 integrado. Accesorios: GIO-PLUG-USB, GIO-A-RS232K, GIO-A-RS485K. Software: GIO-Tool.

#### RTBs verificables

1. Protocolo: **MODBUS RTU**, velocidades **9600 baud** (todos los Genius) / **9600-19200-38400 baud** (GIII+MV, RS-485 integrado). Referencia: HDEs individuales Genius; catálogo Genius 03/2025.
2. Capacidad de red: **hasta 32 relés** en bus GIO-A-RS485K. Referencia: HDE GIO-Link.
3. Variables accesibles vía bus: corriente (I1/I2/I3), voltaje (L1/L2/L3), frecuencia, kW, kVA, kWh, factor de potencia, temperatura, histórico de fallas, estados de alarma, encendido/apagado remoto. Referencia: catálogo Genius tabla comparativa + HDEs individuales.
4. Interfaces físicas propietarias: GIO PORT (todos los relés Genius), GIO-PLUG-USB, GIO-A-RS232K, GIO-A-RS485K. Referencia: HDE GIO-Link y catálogo Genius.
5. Software GIO-Tool: monitorización en tiempo real + extracción de históricos + gráficas de tendencias + exportación CSV. Referencia: HDE GIO-Tool.
6. Formato de palabra MODBUS: **8N1**. Referencia: HDEs individuales.
7. Rango de direcciones MODBUS: **1-127**. Referencia: GIII+ HDE sección F.

#### Diferenciación competitiva (Orlan OL-1)

Estado: AMARILLO

- **Siemens SIMOCODE 3UF7:** comunicación vía módulo separado (PROFIBUS, Ethernet — no MODBUS nativo). Catálogo SIMOCODE consultado.
- **Eaton C440/C441:** MODBUS disponible vía módulo C440/XTOE Modbus separado. Manual C440/XTOE consultado.
- **Rockwell E300:** EtherNet/IP, DeviceNet como protocolo primario. MODBUS no nativo.
- **Schneider TeSys T:** RS485 MODBUS disponible, integración nativa en modelos LTM. Dato parcialmente confirmado.
- **Chint/Lovato/LS:** en gamas superiores algunos modelos soportan comunicación; no estándar en gama básica.

Diferenciador real: el ecosystem GIO integra el GIO PORT (hardware propietario), los adaptadores GIO-Link y el software GIO-Tool como sistema cerrado diseñado específicamente para la gama Genius. La mayoría de competidores en gama media tienen MODBUS como módulo accesorio opcional, no integrado desde fábrica. En el mercado LatAm, el punto de diferencia es la conectividad nativa sin costo adicional de módulo y el software GIO-Tool disponible para el usuario final.

#### Caveats legales aplicables (Bruna BR-2, Gate 8)

"Los candidatos de naming del NODO-H se anclan en la denominación propietaria Ecosystem GIO (GIO PORT / GIO-Link / GIO-Tool) de Genteca. El protocolo de comunicación subyacente es MODBUS RTU (estándar abierto — Modbus Organization). Los nombres candidatos no contienen ni aluden a MODBUS ni a ninguna denominación de protocolo estándar. La documentación formal del Ecosystem GIO como sistema diferenciado del protocolo estándar subyacente es un documento interno que I+D debe elaborar antes de la reunión con el abogado (confirmado en Checkpoint 1 gap 4)."

Instrucción vinculante: MODBUS es marca registrada de tercero (Modbus Organization). Los candidatos de naming no pueden contener "MODBUS" ni derivados que lo evoquen. Los 4 candidatos del NODO-H en el Naming Bible están anclados en la familia GIO o crean nombres para el ecosystem propietario sin aludir al protocolo subyacente.

#### Documentos internos Genteca relevantes

- HDE GIO-Link (versión vigente): especificaciones de los adaptadores y capacidad de red. Referencia primaria del RTB de conectividad.
- HDE GIO-Tool: descripción del software.
- HDE GIII+ / GIII+MV (sección F de comunicaciones): confirma RS-485 integrado y velocidades disponibles.
- Documentación formal del Ecosystem GIO como sistema diferenciado (qué incluye exactamente, qué lo diferencia de una instalación MODBUS genérica): documento pendiente de elaboración por I+D. Urgente antes de reunión con abogado (ver Sección 4, ítem 4).
- Mapa de registros MODBUS RTU: si existe documento técnico separado, útil para el abogado para delimitar el alcance del sistema.

#### Notas especiales — NODO-H

MODBUS RTU es un estándar abierto de la industria. El nombre MODBUS es marca registrada de la Modbus Organization (originalmente Schneider Electric). Lo que Genteca registra no es el protocolo sino el **ecosystem propietario GIO** como sistema integrado: GIO PORT (hardware de interfaz en el relé) + adaptadores GIO-Link (hardware accesorio) + software GIO-Tool (aplicación de monitoreo). El argumento ante el examinador es que los nombres GIO-* son nombres de productos con uso comercial documentado en catálogos y HDEs de Genteca, y que el ecosystem como sistema integrado tiene una función diferenciadora que va más allá del protocolo subyacente.

---

## Sección 4 — Documentos internos pendientes que I+D debe ubicar o elaborar

Los siguientes documentos son necesarios para que el abogado pueda validar los RTBs declarados en este Anexo. La lista consolida los gaps identificados por Vera en VR-1, confirmados por Owner en Checkpoint 1, y los requerimientos adicionales de Bruna en BR-2.

---

**1. Parámetros NTC numéricos en HDE — NODO-C (Thermo-Safe)**

- **Qué es:** HDE GSM-MB (y equivalentes GSM-RB, GSM-RE) en versión que incluya la sección de protección térmica NTC: rango de temperatura de operación, umbral de disparo, histéresis, tiempo de respuesta del sensor, tipo de sensor (resistencia nominal a 25 °C), longitud de cable del NTC.
- **Para qué se usa:** sin estos parámetros, el claim de protección térmica del NODO-C no tiene RTBs numéricos verificables para el abogado. La presencia del sensor se confirma por empaque, pero los parámetros de funcionamiento no están en HDEs actuales (v6/v6-rv1).
- **Quién en I+D probablemente lo tiene:** el equipo de desarrollo del GSM-MB/RB/RE (la protección térmica es la adición más reciente a esta gama).
- **Urgencia:** antes de la reunión con el abogado. Es el gap documental más crítico del portafolio.

---

**2. Denominación formal de curva inversa V-t algorítmica en documentos Genteca — NODO-B (FlickerGuard)**

- **Qué es:** confirmación de si existe en I+D algún documento (especificación de algoritmo, nota técnica interna, protocolo de prueba) que describa formalmente el comportamiento de "tiempo de desconexión inversamente proporcional a la desviación de voltaje" y bajo qué nombre interno lo denomina Genteca.
- **Para qué se usa:** los datos de respuesta V-t están en las HDEs (GSM-AV06: "0,02 a 2 s según intensidad"; GSM-RB: "0,4 a 3 s según intensidad") pero el algoritmo como tal no tiene denominación formal en documentos actuales. El abogado puede preguntar por la especificación técnica del algoritmo si el nombre candidato para NODO-B hace referencia a la curva V-t. Si solo existen los tiempos de respuesta de las HDEs, el abogado debe saber que el sustento documental es el comportamiento medido, no una especificación de algoritmo formal.
- **Quién en I+D probablemente lo tiene:** diseñador del algoritmo de supervisión de voltaje para la gama GSM.
- **Urgencia:** antes de la reunión con el abogado.

---

**3. Addendum HDE GRN-MV con tiempo de confirmación de 10 s — NODO-G (TaskMemory)**

- **Qué es:** actualización de la HDE GRN-MV (actualmente v9) o addendum técnico que incluya formalmente el parámetro de tiempo de confirmación de 10 segundos antes de actuar la salida tras el restablecimiento de energía.
- **Para qué se usa:** el tiempo de 10 s está confirmado verbalmente por I+D pero no aparece en la HDE v9. Para que este parámetro sea defendible como RTB ante un examinador, debe estar en un documento formal (HDE o addendum). Sin documento, el claim existe pero no es verificable independientemente.
- **Quién en I+D probablemente lo tiene:** el diseñador del firmware del GRN-MV o el responsable de la documentación del producto.
- **Urgencia:** antes de la reunión con el abogado.

---

**4. Documentación formal del Ecosystem GIO — NODO-H**

- **Qué es:** documento técnico que describa formalmente el Ecosystem GIO como sistema integrado: qué componentes lo forman (GIO PORT, GIO-Link, GIO-Tool), cuál es la arquitectura de la red, qué lo diferencia técnicamente de una instalación MODBUS genérica, y cuáles son las capacidades específicas del sistema propietario más allá del protocolo subyacente.
- **Para qué se usa:** el abogado necesita entender qué es exactamente lo que Genteca registra en NODO-H. Los candidatos de naming se anclan en la familia GIO; el documento de I+D delimita el objeto del registro (el ecosystem, no el protocolo). Sin este documento, el argumento de registrabilidad del ecosystem como unidad diferenciada de MODBUS es difícil de construir.
- **Quién en I+D probablemente lo tiene:** el equipo técnico de la línea Genius, que diseñó el GIO PORT y los accesorios.
- **Urgencia:** antes de la reunión con el abogado. Confirmado como gap en Checkpoint 1 resolución.

---

**5. Confirmación del status de mercado del GOC — NODO-F (TripleLock)**

- **Qué es:** confirmación de I+D sobre si el GOC está activo en el portafolio comercial actual o si fue descontinuado. El spec del GOC en la KB está marcado como "versión histórica".
- **Para qué se usa:** si el GOC fue descontinuado, se retira de la lista de portadores del NODO-F en el deck (los demás portadores — GOCT, GUCT+, GSPT, GIII+, GIII+MV — son suficientes para sostener el nodo). Si está activo, se incluye. No frena el proceso; es una precisión documental.
- **Quién en I+D probablemente lo tiene:** equipo comercial o de producto Genius.
- **Urgencia:** baja. Puede resolverse en cualquier momento antes de la presentación; no afecta la registrabilidad del nodo ni el caveat del abogado.

---

## Sección 5 — Notas de discrepancia y pendientes técnicos

### Discrepancia 1 — ForensLog: 100 fallas (GIII+MV) vs 20 fallas (GIII+ estándar)

VR-1 de Vera documenta la discrepancia: GIII+MV = 100 últimas fallas; GIII+ estándar = 20 últimas fallas; GSPT-MV = 80 últimas fallas. El anchor ForensLog del proyecto previo referenciaba "100-Fault Forensic History" que corresponde específicamente al GIII+MV. OL-1 de Orlan confirma el hallazgo con fuentes primarias. Bruna en BR-2 (Gate 4) resuelve la discrepancia: postura del deck es Escenario A (acotado al GIII+MV como portador principal del RTB de máxima capacidad). La discrepancia está resuelta en el flujo del proyecto; se documenta aquí para que el abogado tenga contexto si pregunta por el alcance del nombre en la gama.

### Discrepancia 2 — Sensor de temperatura: NTC (GSM-MB/RB) vs PTC100 (GIII+/GIII+MV)

El GSM-MB/RB usa sensor NTC para protección térmica (NODO-C). El GIII+/GIII+MV usa sensor PTC100 (platino) — tecnología de sensor diferente. Orlan lo identifica en OL-1 como discrepancia que afecta el alcance del claim de "NTC" en el NODO-C. Vera resuelve en VR-1: el NODO-C (Thermo-Safe) describe el NTC del GSM-MB/RB exclusivamente. El GIII+/GIII+MV no forma parte del NODO-C. Para el abogado: el claim de protección NTC en NODO-C aplica al GSM-MB/RB/RE. El GIII+/GIII+MV tiene protección de temperatura con PTC100, que es un mecanismo distinto que puede ser relevante para otros nodos en revisiones futuras pero no forma parte de este portafolio de naming.

### Pendiente técnico — Claims marcados como CLAIM en OL-1 (Orlan)

Orlan identifica en su matriz de diferenciación un subconjunto de hallazgos sobre la competencia marcados como [CLAIM] (inferencias de conocimiento técnico general, no verificados contra datasheet primario en la sesión de investigación). Los claims de mayor impacto en el posicionamiento de este Anexo son:

- **Eaton C440/C441: capacidad de registro de fallas** — no verificado en datasheet primario. Si el abogado requiere comparativo verificado para NODO-E, el comparativo con Rockwell E300 (10 registros, fuente verificada: manual 193-UM015) es el más sólido disponible.
- **Siemens SIMOCODE: capacidad de registro de fallas** — no verificado en datasheet primario.
- **Siemens 3RU/3RB: curva inversa cold/hot** — claim basado en manual; presencia del mecanismo inferida del estándar IEC aplicable.

Los claims de Eaton y Siemens para NODO-C y NODO-D (soporte NTC/PTC) están marcados como HECHOS verificados en fuente primaria (catálogos SIMOCODE y user guide LTMR consultados respectivamente).

No se identificaron discrepancias entre VR-1 (Vera) y OL-1 (Orlan) ni entre BR-2 (Bruna) y los datos técnicos del inventario. Los gates de Bruna son consistentes con los RTBs documentados por Vera.

---

## Sección 6 — Mini-cover note

### Documento producido

`C:\Raul\03-projects\genteca\portfolio-naming-ip-2026\06-three-pack\01-Anexo-Tecnico_v1.md`

### Decisiones de compilación

1. **NODO-D / ThermalCurve rechazado:** el nodo se mantiene con plena descripción técnica porque sigue siendo registrable; el nombre rechazado se documenta en la tabla maestra y en la sección de detalle con explicación transparente de la causa del rechazo (descriptividad de función estándar IEC), la condición de reapertura (RTB propietario que exceda el estándar), y la ubicación de los candidatos alternativos (Naming Bible). El abogado puede evaluar los candidatos alternativos con el mismo contexto técnico del nodo.

2. **Override curva inversa:** el caveat estructural del Gate 1 (Bruna BR-2) se colocó una vez en la Sección 1 — Introducción, con el texto literal aprobado. No se repite en los nodos individuales. La mención en NODO-B y NODO-D del override ("universal de facto") remite explícitamente a ese caveat de Sección 1.

3. **Discrepancias VR-1 / OL-1:** dos discrepancias identificadas (ForensLog 100 vs 20 fallas; NTC vs PTC100) están documentadas en Sección 5 con su resolución. No quedan discrepancias abiertas sin resolución en este documento.

4. **Claims competitivos no verificados:** se preservan como información para el abogado con indicación explícita del nivel de verificación ("fuente verificada" vs "claim"). El abogado determina si necesita verificación adicional para su análisis de registrabilidad.

5. **NODO-H GIO ecosystem:** el nombre anchor no existe (nodo nuevo sin precedente en Top 7). La descripción técnica del nodo y el caveat del abogado están orientados a facilitar la evaluación de los candidatos de la familia GIO-* que Solenne generó en Phase 4.

6. **GOC status histórico:** anotado como pendiente de baja urgencia en Sección 4 ítem 5; no bloquea ninguna decisión del abogado.

### Confirmación de integración de caveats Bruna BR-2

Todos los caveats literales de los 8 gates de Bruna BR-2 están integrados en este documento:

- Gate 1 (override): Sección 1, caveat estructural único
- Gate 2 (ThermalCurve rechazado): NODO-D, sección de caveats + notas especiales implícitas en la sección de diferenciación
- Gate 3 (Thermo-Safe Caso A): NODO-C, caveat literal
- Gate 4 (ForensLog Escenario A): NODO-E, caveat literal
- Gate 5 (FlickerGuard contingencia OMPI): NODO-B, caveat literal
- Gate 6 (TripleLock contingencia sectorial): NODO-F, caveat literal
- Gate 7 (TaskMemory jurisdicción diferenciada): NODO-G, caveat literal
- Gate 8 (Ecosystem GIO sin términos de protocolo estándar): NODO-H, caveat literal

### Items abiertos al Owner / a I+D / al abogado

**Al Owner — sin items bloqueantes para Checkpoint 2.** El proyecto puede avanzar a Checkpoint 2 con este Anexo, el Naming Bible (Solenne) y el Deck (Vivienne).

**A I+D — 4 documentos urgentes antes de reunión con abogado:**
1. Parámetros NTC numéricos (HDE GSM-MB/RB/RE con sección térmica) — urgente crítico
2. Confirmación denominación formal curva inversa V-t en docs internos
3. Addendum HDE GRN-MV con 10 s de confirmación
4. Documentación formal Ecosystem GIO como sistema diferenciado de MODBUS

**Al abogado — 4 búsquedas que este Anexo anticipa:**
1. FlickerGuard: verificar colisión en clase 9 con productos LED Australia/UK en SAPI VE + IMPI MX
2. TripleLock: verificar colisión en subclase seguridad física clase 9 en SAPI VE + IMPI MX
3. TaskMemory: verificar colisión en subclase software/apps clase 9 en IMPI MX (prioritario para MX)
4. Candidatos NODO-H (familia GIO-*): verificar si algún nombre GIO está actualmente registrado como marca en clase 9 en VE o MX por terceros

---

*Vera — Anexo Técnico v1.0 compilado. Fecha: 2026-05-13.*
*Inputs: VR-1 (Vera), OL-1 (Orlan), BR-2 (Bruna), Checkpoint 1 resolution (Owner).*
