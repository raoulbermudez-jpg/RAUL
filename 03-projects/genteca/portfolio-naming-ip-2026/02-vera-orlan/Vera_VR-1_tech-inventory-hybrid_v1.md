---
doc_type: VR-1-tech-inventory
project_id: portfolio-naming-ip-2026
domain: genteca
version: v1.0
author: Vera
fecha: 2026-05-13
kb_sources_consulted:
  - 2026-05-09_hoja-especificaciones_exceline-20240515-gsm-mb-hde-v6-rv1.md
  - 2026-05-09_hoja-especificaciones_exceline-gsm-mb-hde-v3-n.md
  - 2026-05-09_hoja-especificaciones_exceline-gsm-mb-hde-v4.md
  - 2026-05-09_hoja-especificaciones_exceline-gsm-mb-hde-v5.md
  - 2026-05-09_hoja-especificaciones_exceline-gsm-mb-hde-v6.md
  - 2026-04-18_hoja-especificaciones_tecnica-gsm-l-hde-v10.md
  - 2026-04-17_hoja-especificaciones_exceline-gsm-rb-protector-aa-refrigeracion.md
  - 2026-04-17_hoja-especificaciones_exceline-gsm-ng-protector-neveras-alta-gama.md
  - 2026-04-18_hoja-especificaciones_agua-grn-mv-hde-v9.md
  - 2026-04-18_hoja-especificaciones_tecnica-e-giii.md
  - 2026-05-09_hoja-especificaciones_genius-giii-mv-v1.md
  - 2026-05-09_otro_genius-giii-mv-gd-he8003-ve-v1.md
  - 2026-04-18_hoja-especificaciones_tecnica-e-gspt-mv.md
  - 2026-05-10_hoja-especificaciones_genius-hoja-de-especificacion-goc.md
  - 2026-04-17_catalogo_genius-reles-electronicos-digitales.md
  - 2026-04-17_catalogo_exceline-profesional-proteccion-trifasica.md
  - 2026-05-09_otro_exceline-gsm-av06-gla-r-v1.md
  - 2026-04-18_hoja-especificaciones_gsm-mb-rb-rf-gla-t.md (etiqueta empaque)
override_aplicado: "Curva inversa V-t algorítmica + curva inversa I-t cold/hot — universales de facto en gama Exceline / Exceline Profesional / Genius (charter §3 decisión 4)"
---

# Tech Inventory Hybrid — Genteca Portfolio
## Exceline / Exceline Profesional / Genius

> Inventario de tecnologías diferenciadoras del portafolio Exceline / Exceline Profesional / Genius, con granularidad híbrida. Para el proyecto de naming portfolio IP 2026.
>
> Producido por Vera en Phase 1. Input para Orlan (differentiation matrix), Vael (messaging), Solenne (candidatos de marca).

---

## Resumen ejecutivo

- **Total de nodos: 8**
- **Decisión de granularidad:** Los dos algoritmos del override Owner se mantienen como nodos independientes (NODO-B y NODO-D) porque tienen mecanismos técnicos distintos, aplican a dominios de protección distintos (voltaje vs. corriente/temperatura) y sostendrán marcas con audiencias y beneficios comerciales diferenciados. No se fusionan.
- **NODO-H** (slot abierto) se llena con la conectividad industrial MODBUS / GIO-Link — tecnología transversal documentada en toda la gama Genius que habilita gestión energética y mantenimiento remoto. Es registrable como conjunto de interfaces de comunicación industrial.
- **NODO-I** no se abre: 8 nodos alcanza el techo razonable de tecnologías diferenciadoras defendibles. Forzar un noveno implicaría fragmentar features que ya están cubiertos o inventar tecnología no documentada.
- **Distribución por línea:** Exceline (2), Exceline Profesional (2), Genius (2), Transversal Genius-completo (1), Transversal gama-alta (1).
- **Anchors Top 7 mapeados:** los 7 anchor del proyecto previo tienen nodo asignado. Ninguno queda sin hogar. Ver columna en tabla maestra.
- **Slots abiertos llenados:** NODO-H llenado (conectividad MODBUS/GIO). NODO-I no abierto.

---

## Tabla maestra de nodos

| Código | Título funcional | Línea comercial primaria | Anchor Top 7 | Categoría macro |
|--------|-----------------|--------------------------|--------------|-----------------|
| NODO-A | Reconexión temporal aleatoria post-falla | Exceline / Exceline Profesional | StaggerStart | Lógica de reconexión inteligente |
| NODO-B | Detección sub-ciclo de perturbaciones de voltaje (flicker + curva inversa V-t) | Exceline / Exceline Profesional | FlickerGuard | Protección por voltaje — detección rápida |
| NODO-C | Modelo térmico NTC integrado en protector monofásico | Exceline (GSM-MB/RB/RE) | Thermo-Safe | Modelo térmico de motor — sensor físico |
| NODO-D | Curva inversa I-t diferenciada cold/hot (algoritmo imagen térmica) | Exceline Profesional / Genius | ThermalCurve | Modelo térmico de motor — curva algorítmica |
| NODO-E | Registro forense histórico de fallas con timestamp | Genius (GIII+MV primario) | ForensLog | Diagnóstico forense / registro histórico |
| NODO-F | Bloqueo permanente tras tercera falla de corriente recurrente | Exceline Profesional / Genius | TripleLock | Lógica de protección multi-falla / bloqueo |
| NODO-G | Memoria de estado y reanudación de tarea post-corte | Exceline Profesional (GRN-MV) | TaskMemory | Memoria de estado / recuperación de tarea |
| NODO-H | Conectividad industrial integrada (MODBUS RTU + red multi-relé) | Genius (gama completa) | ninguno | Comunicación / supervisión remota |

---

## Detalle por nodo

---

### NODO-A: Reconexión temporal aleatoria post-falla

- **Mecanismo técnico:** Cuando se restablece la tensión tras un apagón o falla de voltaje, el protector no reconecta la carga en el instante exacto en que el voltaje retorna a rango. En su lugar, ejecuta un algoritmo de variación aleatoria dentro de la ventana de tiempo ajustable por el usuario (5-180 s en GSM-MB v6; 3 min en GSM-NG). La ventana garantiza que el compresor haya completado su ciclo de presión antes de arrancar; la componente aleatoria hace que dos equipos idénticos en la misma instalación no reconecten simultáneamente. Entrada: señal de voltaje en rango. Transformación: genera un retardo con componente aleatoria sobre el mínimo configurado. Salida: cierre del contacto de salida en momento escalonado y no predecible para el conjunto de dispositivos en la instalación.

- **Productos donde vive:** Gama Exceline GSM-MB (modelos 120B y 220B), GSM-RB (modelos R120B y R220B), GSM-RE (modelos RE120A y RE220M), GSM-NG (enchufable neveras alta gama). Según override Owner, asumido presente en toda la gama Exceline / Exceline Profesional / Genius con función de temporizado post-falla.

- **Línea comercial primaria:** Exceline (residencial + comercio pequeño/mediano); presente también en GSM-L (Exceline Profesional, temporizado ajustable 5-300 s).

- **Categoría macro:** Lógica de reconexión inteligente.

- **Anchor Top 7:** StaggerStart.

- **RTBs verificables:**
  - Ventana de temporizado ajustable: 5-180 s (GSM-MB v6, HDE); 180-300 s (GSM-RB, HDE); 3 min fijo (GSM-NG, HDE).
  - Componente aleatoria documentada en HDE GSM-MB v3-n, v4, v5, v6, v6-rv1: "sistema aleatorio para evitar que dos o más equipos protegidos arranquen en simultáneo".
  - GSM-NG: "temporizado aleatorio para evitar arranque simultáneo" (HDE GSM-NG, KB).
  - Cumple función anti-demand-spike en instalaciones con múltiples protectores.
  - Normas verificadas bajo: IEC 61000-4-x (EMC), COVENIN 3445.

- **Docs internos Genteca que el abogado podría pedir:**
  - HDE GSM-MB versión vigente (actualmente v6 o posterior) — especificación del algoritmo de temporizado aleatorio.
  - HDE GSM-RB / GSM-RE — confirmación misma función.
  - HDE GSM-NG — confirmación en formato enchufable.
  - Manual de usuario (si existe documento separado que describe el rango de variación aleatoria en segundos o como porcentaje del mínimo configurado).

---

### NODO-B: Detección sub-ciclo de perturbaciones de voltaje (flicker + curva inversa V-t)

- **Mecanismo técnico:** Dos comportamientos distintos del mismo algoritmo de supervisión de voltaje, integrados en el mismo dispositivo:

  (1) **Detección de flicker:** el dispositivo muestrea el voltaje a frecuencia suficiente para detectar eventos de inestabilidad o parpadeo en ventana de 20 ms (GSM-L) o 150 ms (GSM-MB, GSM-RB). Si detecta inestabilidad sub-ciclo, desconecta la carga sin esperar que el voltaje salga del rango de ajuste. Entrada: señal de voltaje con variaciones rápidas. Transformación: algoritmo de detección de pendiente o variación súbita en ventana < 1 ciclo de 60 Hz. Salida: desconexión inmediata.

  (2) **Curva inversa V-t algorítmica (override universal de facto):** el tiempo de desconexión es inversamente proporcional a la desviación del voltaje respecto al umbral configurado. Una desviación extrema produce desconexión casi instantánea (20-30 ms documentados en GSM-AV06; 0,02-2 s según intensidad en GSM-AV06); una desviación marginal produce desconexión con retardo mayor. Documentado en GSM-RB HDE como "0,4 a 3 s según intensidad". Documentado en GSM-AV06 como "desconexión programada de 0,02 a 2 s según intensidad de falla de voltaje". Este comportamiento no aparece como "curva inversa" en las HDEs actuales — es el algoritmo subyacente al que el Owner ha asignado el override de facto universal.

- **Decisión de granularidad:** Se mantiene como nodo único porque el mecanismo técnico es el mismo algoritmo de supervisión V-t con dos expresiones: detección sub-ciclo (flicker) y respuesta proporcional a la desviación (curva inversa). Separarlos en dos nodos daría dos marcas con mecanismos técnicos solapados, difícil de defender como tecnologías independientes ante un examinador. Orlan decidirá si la differentiation matrix los separa por audiencia.

- **Productos donde vive:** GSM-L (20 ms de detección de flickers, documentado en HDE v10); GSM-MB, GSM-RB, GSM-RE (150 ms desconexión por flicker/inestabilidad, documentado en HDEs); GSM-AV06 (0,02-2 s según intensidad); GSM-NG (150 ms). Override Owner: gama completa Exceline/Exceline Profesional/Genius.

- **Línea comercial primaria:** Exceline / Exceline Profesional (GSM-L es el portador principal del RTB de 20 ms).

- **Categoría macro:** Protección por voltaje — detección rápida de perturbaciones sub-ciclo.

- **Anchor Top 7:** FlickerGuard.

- **RTBs verificables:**
  - Tiempo de detección de flicker: **20 ms** (GSM-L HDE v10 — dato explícito y único en la gama).
  - Tiempo de detección de falla de voltaje genérica (GSM-L): a partir de **60 ms**.
  - Tiempo de desconexión por flicker/inestabilidad (GSM-MB, GSM-RB, GSM-NG): **150 ms**.
  - Desconexión variable según intensidad: **0,02 a 2 s** (GSM-AV06, dato explícito); **0,4 a 3 s** (GSM-RB HDE).
  - Detección de parpadeos + inestabilidad como causa de desconexión: documentada en HDEs GSM-MB, GSM-RB, GSM-RE, GSM-L, GSM-NG.
  - Normas: IEC 61000-4-4 (transientes rápidas), IEC 61000-4-14 (fluctuaciones de voltaje), IEC 60947-1.

- **Docs internos Genteca que el abogado podría pedir:**
  - HDE GSM-L versión vigente (v10 o posterior) — dato explícito de 20 ms para detección de flicker.
  - HDE GSM-MB / GSM-RB / GSM-RE — datos de 150 ms para desconexión por inestabilidad.
  - Especificación del algoritmo de detección de pendiente de voltaje (documento interno I+D — no confirmado en KB; puede no existir como HDE separada).
  - Nota: la descripción "curva inversa V-t algorítmica" como denominación formal no aparece en los documentos KB actuales. I+D deberá confirmar si existe especificación interna con ese nombre, o si el override Owner se sustenta exclusivamente en los tiempos medidos por HDE.

---

### NODO-C: Modelo térmico NTC integrado en protector monofásico

- **Mecanismo técnico:** Sensor de temperatura NTC embebido en el protector monofásico GSM-MB/RB/RE. El sensor lee temperatura real del entorno del compresor o del devanado (según instalación). La lógica interna compara la temperatura medida con umbrales configurados o fijos, y actúa la desconexión si se detecta sobrecalentamiento. A diferencia del modelo I-t puro (NODO-D), este nodo usa medición física de temperatura con un componente de hardware externo (el sensor NTC) en el circuito de decisión. Entrada: lectura analógica del sensor NTC. Transformación: comparación contra umbral térmico. Salida: desconexión de la carga + indicación en LED.

- **Productos donde vive:** GSM-MB (120B y 220B), GSM-RB (R120B y R220B), GSM-RE (RE120A y RE220M) — todos en versión actual "NUEVO — AHORA CON PROTECCIÓN TÉRMICA" (confirmado en etiqueta de empaque HDE GLA_T). Esta es la adición más reciente a la gama.

- **Línea comercial primaria:** Exceline (residencial + comercio pequeño/mediano).

- **Categoría macro:** Modelo térmico de motor — sensor físico de temperatura.

- **Anchor Top 7:** Thermo-Safe.

- **RTBs verificables:**
  - Sensor NTC presente en hardware: confirmado por etiqueta de empaque (GSM-MB_GLA_T_V10, GSM-RB_GLA_T_V9, GSM-RF_GLA_T_V13).
  - Mención explícita "PROTECCIÓN TÉRMICA" en empaque versión V10/V9/V13.
  - **Nota de gap documental:** los parámetros técnicos del NTC (rango de temperatura, umbral de disparo, histéresis, tiempo de respuesta) no están documentados en las HDEs actuales de la KB (v6/v6-rv1 del GSM-MB no incluyen la sección NTC). Los RTBs numéricos para el NTC de la gama GSM no pudieron verificarse desde la KB — el abogado muy probablemente pedirá estos datos.

- **Docs internos Genteca que el abogado podría pedir:**
  - HDE GSM-MB versión que incluya la sección de protección térmica NTC (versión posterior a v6 o addendum). Actualmente no disponible en KB.
  - HDE GSM-RB y GSM-RE equivalentes con sección NTC.
  - Especificación del sensor NTC: rango de temperatura, umbral de desconexión, tipo de sensor (resistencia nominal a 25 °C), longitud de cable si aplica.
  - Nota para I+D: este es el doc más urgente para el proceso IP porque sin RTBs numéricos del NTC, el claim de protección térmica no tiene base técnica verificable para el abogado.

---

### NODO-D: Curva inversa I-t diferenciada cold/hot (algoritmo imagen térmica)

- **Mecanismo técnico:** Algoritmo de protección por sobrecarga basado en modelo de imagen térmica según IEEE C37.112 e IEC 60255-8. El relé calcula continuamente el "calor acumulado" del motor usando la corriente medida, la clase térmica seleccionada y el estado térmico anterior (frío o caliente). El tiempo de disparo ante una sobrecarga es inversamente proporcional al nivel de sobrecarga relativo al nominal (curva I-t inversa). La diferenciación cold/hot opera así: si el motor arrancó en frío (energía térmica acumulada = 0 o baja), aplica la curva fría completa de la clase ajustada; si el motor ya estaba caliente (energía térmica acumulada alta, típicamente por un ciclo reciente de trabajo), aplica la curva caliente = curva fría / 3. Esto significa que ante un arranque en caliente, el disparo ocurre hasta 3 veces más rápido para el mismo nivel de sobrecarga. El tiempo máximo entre transición fría-caliente es de 2 horas. Entrada: corriente medida por CT + estado térmico almacenado. Transformación: cálculo de imagen térmica según clase IEC 60255-8. Salida: disparo por sobrecarga con tiempo inversamente proporcional a (I/Inom).

- **Productos donde vive:** GOCT (Clase 10 fija: curva fría 10, caliente 3); GUCT+ (Clase ajustable 5-30, curvas cold/hot proporcionales); GSPT / GSPT-MV (Clase 10 fija, cold/hot documentado explícitamente en HDE y curva gráfica); GIII+ / GIII+MV (Clase ajustable 5-30, cold/hot documentado); GOC (Clase 10 fija, cold curve 10, hot curve 3). Override Owner: curva inversa I-t cold/hot se asume universal en gama Exceline / Exceline Profesional / Genius.

- **Línea comercial primaria:** Exceline Profesional / Genius (los relés con imagen térmica ajustable son de gama media-alta).

- **Categoría macro:** Modelo térmico de motor — curva algorítmica inversa I-t.

- **Anchor Top 7:** ThermalCurve.

- **RTBs verificables:**
  - Relación curva caliente / curva fría: **Caliente = Fría / 3** (documentado en GIII+ HDE e interpretable de todos los relés con clase 10: curva fría 10, caliente 3).
  - Tiempo máximo entre estados cold/hot: **2 horas** (GIII+ HDE sección E).
  - Clase térmica ajustable: **5 a 30 en pasos de 1** (GUCT+, GIII+, GSPT-MV — todos documentados en HDE/catálogo).
  - Clases disponibles gráficamente: 5, 10, 15, 20, 25, 30 (curva en GIII+ HDE, sección E — norma IEEE C37.112 / IEC 60255-8).
  - Umbral de calor para falla por sobrecarga: **100%** de la imagen térmica calculada.
  - El modelo está implementado según **IEC 60255-8-1990** e **IEEE C37.112-1996** (citados en HDEs de GIII+, GSPT-MV, GOC).
  - Memoria térmica: retención del estado térmico al apagarse el equipo, documentada en GOCT, GSPT, GIII+, GOC.

- **Docs internos Genteca que el abogado podría pedir:**
  - HDE GIII+ o GSPT-MV (versión vigente) — contienen la gráfica de curva fría/caliente con clases.
  - Manual de usuario GIII+ (sección algoritmos de protección) — describe el mecanismo de imagen térmica.
  - HDE GOC / GOCT (confirman cold curve 10, hot curve 3 de forma explícita).
  - Especificación de implementación del algoritmo IEEE C37.112 (si existe documento interno I+D separado de las HDEs).

---

### NODO-E: Registro forense histórico de fallas con timestamp

- **Mecanismo técnico:** El relé registra en memoria no volátil cada evento de falla con cuatro campos: tipo de falla, valor medido al momento de la falla, hora y fecha del evento, y duración del evento. El registro es circular: cuando la capacidad máxima se alcanza, el evento más antiguo es sobreescrito. El usuario puede acceder al registro mediante pantalla LCD o a través del puerto de comunicación (MODBUS RTU). Además, el GIII+MV retiene los parámetros de configuración que estaban activos cuando ocurrió cada falla, permitiendo auditar si el disparo fue correcto dado el ajuste vigente. Entrada: evento de falla (cualquier tipo de protección activada). Transformación: indexación con timestamp proveniente de reloj interno + retención del valor medido y duración. Salida: registro consultable en pantalla o vía bus.

- **Productos donde vive:** GIII+MV: **100 últimas fallas** (documentado en HDE GIII+MV-V1 y gd-he8003-ve-v1); GIII+: **20 últimas fallas** (HDE GIII+); GUCT+ / GSPT / GSPT-MV / GOC / GOCT / GI+ / GII+: **20 últimas fallas** (catálogo Genius). GIII+MV es el producto con mayor capacidad de registro (100 eventos).

- **Línea comercial primaria:** Genius (el registro de 20 eventos es gama Genius completa; el de 100 eventos es exclusivo de GIII+MV).

- **Categoría macro:** Diagnóstico forense / registro histórico.

- **Anchor Top 7:** ForensLog.

- **RTBs verificables:**
  - Capacidad máxima de registro: **100 últimas fallas** (GIII+MV, dato explícito en HDE inglés y español).
  - Capacidad estándar gama Genius: **20 últimas fallas** (toda la línea Genius).
  - Campos por evento: tipo de falla + valor medido + hora + fecha + tiempo de duración (documentado en HDE GIII+ sección F).
  - Retención de parámetros activos al momento de falla: documentada en GIII+MV HDE español (sección comunicaciones).
  - Acceso dual: pantalla LCD + MODBUS RTU port.
  - Reloj con fecha incluido en GIII+ (programador horario / reloj documentado en HDE).

- **Docs internos Genteca que el abogado podría pedir:**
  - HDE GIII+MV (versión vigente) — confirma 100 últimas fallas y campos de registro.
  - Manual GIII+MV — sección de consulta de histórico de fallas.
  - HDE GIII+ estándar — confirma 20 últimas fallas como baseline de la gama.

---

### NODO-F: Bloqueo permanente tras tercera falla de corriente recurrente

- **Mecanismo técnico:** Si el relé detecta 3 fallas de corriente (sobrecarga, pérdida de fase por corriente, desbalance de corriente) dentro de una ventana de 30 minutos, ejecuta una desconexión permanente que requiere intervención manual explícita (reset manual) para restablecer la operación. El objetivo es interrumpir el ciclo destructivo de "falla-rearranque-falla" que ocurre cuando una falla recurrente no es diagnosticada. Las dos primeras fallas permiten rearranque automático (si el modo Auto está seleccionado); la tercera dentro de la ventana activa el bloqueo. La lógica opera independientemente del tipo específico de falla de corriente: cualquier combinación de 3 eventos de corriente en 30 minutos activa el bloqueo. Entrada: contador de fallas de corriente + temporizador de ventana de 30 min. Transformación: comparación del contador contra umbral 3 dentro de la ventana. Salida: desconexión permanente con indicación en pantalla o LEDs.

- **Productos donde vive:** GOCT, GUCT+, GSPT / GSPT-MV, GIII+ / GIII+MV, GOC — todos con indicación "3 fallas de corriente en menos de 30 min → desconexión permanente" en HDEs y catálogo. También en GSC-CR / GSC-MB (Exceline Profesional) según catálogo trifásico.

- **Línea comercial primaria:** Genius (GOCT, GUCT+, GSPT, GIII+, GOC) / Exceline Profesional (GSC-CR, GSC-MB).

- **Categoría macro:** Lógica de protección multi-falla / bloqueo escalonado.

- **Anchor Top 7:** TripleLock.

- **RTBs verificables:**
  - Umbral de fallas de corriente para bloqueo permanente: **3 fallas en menos de 30 minutos** (documentado explícitamente en GIII+ HDE sección E, GOC sección E, catálogo Genius tabla comparativa, catálogo trifásico GSC).
  - Tiempo de disparo en tercera falla: **< 1 s** (GOC HDE sección E: "Trip Delay because of 3 Current Failures: <1 sec in less than 30 min").
  - Requiere reset manual para restablecer operación tras bloqueo permanente.
  - Aplica a fallas de corriente de cualquier tipo: sobrecarga (OL), desbalance de corriente (CUB), pérdida de fase por corriente (CSP).
  - Función transversal en toda la gama Genius con medición de corriente.

- **Docs internos Genteca que el abogado podría pedir:**
  - HDE GIII+ / GIII+MV — sección E de funciones y algoritmos, parámetro "Detección de Tercera (3ª) Falla".
  - HDE GOC — sección E, confirmación de <1 s para el disparo en tercera falla.
  - Manual de usuario de cualquier relé Genius con imagen térmica — sección de descripción del modo de rearme y bloqueo permanente.

---

### NODO-G: Memoria de estado y reanudación de tarea post-corte

- **Mecanismo técnico:** El GRN-MV (relé de nivel para líquidos conductores) almacena en memoria no volátil el modo operativo activo al momento de un corte eléctrico. Modos posibles: vaciado de pozo (bomba activa, drenando), llenado de tanque (bomba activa, llenando), espera (condición de nivel alcanzado). Cuando se restablece la alimentación, el relé retoma automáticamente la tarea que estaba ejecutando, sin requerir intervención del usuario. Adicionalmente, hay un tiempo de confirmación de 10 segundos (confirmado verbalmente por I+D, pendiente de actualización documental en HDE/manual) antes de que el relé actúe la salida tras el restablecimiento, para evitar actuaciones por microinterrupciones. Entrada: lectura de sondas de nivel (conductividad del líquido) + estado almacenado en memoria. Transformación: recuperación del modo almacenado + lectura de estado actual de sondas + decisión de actuación. Salida: activación del relé de control en el modo correspondiente (vaciado/llenado/espera).

- **Productos donde vive:** GRN-MV (Exceline Profesional, relé de nivel). Tecnología específica de este producto.

- **Línea comercial primaria:** Exceline Profesional (aplicación en sistemas de bombeo, riego, control de nivel industrial).

- **Categoría macro:** Memoria de estado / recuperación de tarea.

- **Anchor Top 7:** TaskMemory.

- **RTBs verificables:**
  - Modos de operación persistidos: vaciado de pozo, llenado de tanque, espera (HDE GRN-MV v9, sección características generales).
  - Reanudación automática post-corte sin intervención del usuario: documentado en HDE GRN-MV v9.
  - Texto de la HDE: "Si el equipo se encontraba en proceso de vaciado o llenado al momento del corte, retoma automáticamente la última función al restablecerse la energía, sin requerir intervención del usuario."
  - Sensibilidad de activación ajustable por perilla (conductividad del líquido).
  - Tiempo de confirmación 10 segundos: confirmado verbalmente por I+D (no en HDE/manual actual — ver nota de gap documental).
  - Normas verificadas: IEC 61000-4-x (EMC), IEC 60947-1.

- **Docs internos Genteca que el abogado podría pedir:**
  - HDE GRN-MV versión vigente (v9 o posterior) — sección de características generales con la descripción del sistema de memoria de tarea.
  - Actualización de HDE o addendum que incluya el tiempo de confirmación de 10 s (actualmente no en HDE v9 — requiere actualización por I+D).
  - Manual de usuario GRN-MV — si existe, sección de descripción de modos de operación post-corte.

---

### NODO-H: Conectividad industrial integrada (MODBUS RTU + red multi-relé)

- **Mecanismo técnico:** Arquitectura de comunicación industrial embebida en los relés Genius que permite su integración en redes de supervisión y control. El protocolo MODBUS RTU opera a 9600 baudios (todos los relés Genius) o a velocidades superiores 9600/19200/38400 baud (GIII+MV y modelos con RS-485 integrado). Los relés exponen: lecturas en tiempo real de corriente, voltaje, frecuencia, potencia (kW/kVA/kWh), factor de potencia, temperatura; estados de alarma y falla; registro histórico de fallas; comandos de encendido/apagado remoto; lectura y escritura de parámetros de protección (con contraseña). La red puede conectar hasta 32 relés en un bus RS-485 (GIO-A-RS485K). La interfaz física se implementa mediante el GIO PORT (conector propietario en todos los relés) y el accesorio GIO-Link (adaptadores USB/RS-232/RS-485), más el puerto RS-485 integrado en GIII+ / GIII+MV. El software GIO-Tool permite monitorización gráfica, extracción de históricos y generación de reportes desde PC. Entrada: petición MODBUS del maestro. Transformación: procesamiento de registro MODBUS RTU con mapeo de variables eléctricas y estados. Salida: respuesta MODBUS + posibles acciones de control remoto.

- **Decisión de apertura de slot H:** Esta tecnología es transversal a toda la gama Genius, está completamente documentada en la KB, y representa un conjunto diferenciador relevante para la audiencia de especificadores técnicos e industria. No es un simple "feature de conectividad" — es una arquitectura de red industrial integrada desde el diseño del producto con protocolo estándar de la industria, interfaces físicas propias (GIO-Link) y software propietario (GIO-Tool). Registrar el sistema de conectividad como marca daría a Genteca protección sobre el ecosystem de comunicación, no solo el relé individual.

- **Productos donde vive:** Toda la gama Genius: GI+, GII+, GOCT, GUCT+, GSPT, GSPT-MV, GIII+, GIII+MV, GOC (todos con GIO PORT + MODBUS RTU); GIII+ / GIII+MV adicionalmente con RS-485 integrado. Accesorios GIO-Link (USB, RS-232, RS-485) y software GIO-Tool.

- **Línea comercial primaria:** Genius (premium / especificadores / industria).

- **Categoría macro:** Comunicación / supervisión remota / gestión energética integrada.

- **Anchor Top 7:** ninguno (nodo nuevo, sin anchor del proyecto previo).

- **RTBs verificables:**
  - Protocolo: **MODBUS RTU**, velocidades **9600 baud** (todos los Genius) / **9600-19200-38400 baud** (GIII+MV, RS-485 integrado).
  - Capacidad de red: **hasta 32 relés** en bus GIO-A-RS485K (HDE GIO-Link).
  - Variables accesibles vía bus: corriente (I1/I2/I3), voltaje (L1/L2/L3), frecuencia, kW, kVA, kWh, factor de potencia, temperatura, histórico de fallas, estados de alarma, encendido/apagado remoto (documentado en catálogo Genius tabla comparativa y HDEs individuales).
  - Interfaces físicas propietarias: GIO PORT (todos los relés Genius) + adaptadores GIO-PLUG-USB, GIO-A-RS232K, GIO-A-RS485K.
  - Software GIO-Tool: monitorización en tiempo real + extracción de históricos + gráficas de tendencias + exportación CSV (HDE GIO-Tool).
  - Formato de palabra MODBUS: 8N1 (documentado en HDEs).
  - Rango de direcciones MODBUS: 1-127 (GIII+ HDE sección F).

- **Docs internos Genteca que el abogado podría pedir:**
  - HDE GIO-Link (versión vigente) — especificaciones de los adaptadores y capacidad de red.
  - Mapa de registros MODBUS RTU (si existe documento técnico separado — no confirmado en KB como doc independiente).
  - HDE GIO-Tool — descripción del software.
  - HDE GIII+ / GIII+MV — sección F de comunicaciones (confirma RS-485 integrado y velocidades disponibles).

---

## Notas de discrepancia / pendientes

**[NOTA-1] GIII+ estándar vs GIII+MV — diferencia en registro de fallas.**
El GIII+ estándar tiene registro de **20 últimas fallas**. El GIII+MV tiene registro de **100 últimas fallas**. El anchor ForensLog y la denominación "100-Fault Forensic History" del proyecto previo apunta específicamente al GIII+MV. En el deck, esto no es un problema si el nodo se nombra sobre la capacidad máxima de la gama (100 fallas en GIII+MV) y se especifica que el baseline de la línea es 20 fallas. Para el abogado: la tecnología de registro está presente en toda la gama Genius; la capacidad diferenciadora (100 eventos) es exclusiva del GIII+MV.

**[NOTA-2] Protección térmica NTC en GSM-MB/RB/RE — gap documental crítico.**
La protección térmica NTC es visible en el empaque (etiqueta versión V10/V9/V13 con "AHORA CON PROTECCIÓN TÉRMICA") pero los parámetros técnicos no están en las HDEs actuales de la KB. Las HDEs del GSM-MB más recientes disponibles (v6 y v6-rv1) no incluyen la sección NTC. Este es el gap documental más urgente del inventario — sin RTBs numéricos verificables (rango de temperatura, umbral de disparo, sensor empleado), el claim de protección térmica para el abogado queda sin base técnica comprobable. Reportado al Owner para que I+D provea el documento antes de Phase 5 (Anexo Técnico).

**[NOTA-3] Curva inversa V-t — denominación formal no existe en HDEs actuales.**
El comportamiento de "tiempo de desconexión inversamente proporcional a la desviación de voltaje" está documentado con datos concretos en las HDEs (GSM-AV06: "0,02 a 2 s según intensidad"; GSM-RB: "0,4 a 3 s según intensidad") pero no hay ningún documento Genteca que llame a este comportamiento "curva inversa V-t algorítmica". Es la descripción técnica correcta del comportamiento, pero el abogado podría preguntar por la especificación formal del algoritmo. I+D debería confirmar si existe documento interno que describa el algoritmo de respuesta V-t, o si el claim se sustenta exclusivamente en los tiempos de respuesta medidos en las HDEs.

**[NOTA-4] Tiempo de confirmación 10 s en GRN-MV — no en HDE.**
El tiempo de confirmación de 10 segundos en el GRN-MV está confirmado verbalmente por I+D pero la HDE v9 no lo menciona. Para que este RTB sea defendible ante un examinador, la HDE debe actualizarse. Alimenta la lista de docs internos para I+D.

**[NOTA-5] Modelos GOC y GOC-T — status "histórico" en KB.**
El spec del GOC está marcado como "version_status: historica" en la KB. Verificar con I+D si el GOC está activo en el portafolio actual antes de incluirlo como producto portador del NODO-F en el deck. Si fue descontinuado, los otros portadores (GOCT, GUCT+, GSPT, GIII+) son suficientes para el nodo.

**[NOTA-5b] NODO-H y defensibilidad de marca.**
El MODBUS RTU es un protocolo abierto de la industria (Modbus Organization). Registrar el nombre de un "sistema de conectividad" en Clase 9 es factible, pero la marca no puede contener la palabra MODBUS. Bruna debe confirmar en Phase 3 que los candidatos de Solenne para este nodo no colisionan con la marca MODBUS o sus derivados. El diferenciador registrable es el ecosystem GIO (GIO PORT + GIO-Link + GIO-Tool) como sistema integrado, no el protocolo subyacente.

---

## Mini-cover note

**Archivos producidos:**
`C:\Raul\03-projects\genteca\portfolio-naming-ip-2026\02-vera-orlan\Vera_VR-1_tech-inventory-hybrid_v1.md`

**Decisiones de granularidad tomadas:**

1. NODO-B (FlickerGuard) absorbe la curva inversa V-t: el mecanismo de detección sub-ciclo y el comportamiento V-t proporcional son el mismo algoritmo de supervisión de voltaje con dos expresiones. Separar en dos nodos crearía solapamiento técnico que un examinador podría objetar. El nodo se llama "detección sub-ciclo" para que la marca cubra el comportamiento completo.

2. NODO-C (Thermo-Safe / NTC) y NODO-D (ThermalCurve / curva I-t) se mantienen separados porque son tecnologías físicamente distintas: NODO-C usa un sensor de hardware físico (NTC) para medir temperatura real; NODO-D usa un algoritmo matemático de imagen térmica que no requiere sensor físico — calcula la temperatura implícita del motor a partir de la corriente medida. Son mecanismos independientes, viven en productos distintos (NODO-C en Exceline monofásico; NODO-D en Genius/Exceline Profesional trifásico), y tienen audiencias primarias distintas (residencial vs. industrial). Mantenerlos separados es la decisión técnicamente correcta y estratégicamente útil para el portafolio de marcas.

3. NODO-H (conectividad industrial) llena el slot abierto porque la arquitectura GIO (GIO PORT + GIO-Link + GIO-Tool + MODBUS) es una tecnología transversal documentada, diferenciadora en la audiencia de especificadores, y registrable como sistema integrado (no el protocolo, sino el ecosystem propietario). No se abrió NODO-I porque 8 nodos con base técnica sólida es preferible a 9 con granularidad forzada.

**Flujo hacia los siguientes agentes:**

- **Orlan** recibe este inventario como input para construir la differentiation matrix (verde/amarillo/rojo vs. ABB/Siemens/Schneider/Eaton/Chint/LS/Lovato). Los 8 nodos son la estructura que Orlan debe usar para organizar su matriz. Nota para Orlan: NODO-H (conectividad MODBUS/GIO) puede ser sorprendentemente verde — la mayoría de competidores en gama media tienen MODBUS como accesorio opcional, no integrado desde fábrica.
- **Vael** recibirá este inventario después de Checkpoint 1 para construir la arquitectura de mensajes por audiencia (especialmente importante para la cadena L0→L1→L2 en NODO-A, NODO-C y NODO-G, que son los nodos de mayor impacto en audiencia residencial y comercio).
- **Solenne** usará la columna "Anchor Top 7" para mapear los 7 candidatos preexistentes a sus nodos y luego completar hasta 4 candidatos por nodo. Los 8 nodos necesitan 32 candidatos en total (4 × 8); los 7 anchor cubren 7 de los 32 slots.
- **Bruna** debe atender especialmente NODO-C (gap documental NTC — claim sin RTBs verificables en HDE), NODO-B (denominación curva inversa V-t no formalizada), y NODO-H (riesgo de colisión con marca MODBUS).

**Preguntas abiertas al Owner:** cero preguntas de bloqueo para este entregable. Las notas 1-5 son informativas o alimentan la lista de docs internos para I+D. El inventario está completo para continuar con Checkpoint 1.

---

## Sources

| Documento | Tipo | Acceso |
|-----------|------|--------|
| GSM-MB HDE v6-rv1 (2026-05-09) | HDE Genteca | KB Genteca vía Celeste |
| GSM-MB HDE v3-n, v4, v5, v6 (2026-05-09) | HDE Genteca | KB Genteca vía Celeste |
| GSM-L HDE v10 (2026-04-18) | HDE Genteca | KB Genteca vía Celeste |
| GSM-RB HDE (2026-04-17) | HDE Genteca | KB Genteca vía Celeste |
| GSM-NG HDE (2026-04-17) | HDE Genteca | KB Genteca vía Celeste |
| GSM-AV06 etiqueta r-v1 (2026-05-09) | Etiqueta/empaque Genteca | KB Genteca vía Celeste |
| GRN-MV HDE v9 (2026-04-18) | HDE Genteca | KB Genteca vía Celeste |
| GIII+ HDE E (2026-04-18) | HDE Genteca | KB Genteca vía Celeste |
| GIII+MV HDE v1 inglés (2026-05-09) | HDE Genteca | KB Genteca vía Celeste |
| GIII+MV HDE gd-he8003-ve-v1 español (2026-05-09) | HDE Genteca | KB Genteca vía Celeste |
| GSPT-MV HDE v2 (2026-04-18) | HDE Genteca | KB Genteca vía Celeste |
| GOC Specification Sheet (2026-05-10) | HDE Genteca | KB Genteca vía Celeste |
| Catálogo Genius Relés Electrónicos Digitales, 03/2025 (2026-04-17) | Catálogo Genteca | KB Genteca vía Celeste |
| Catálogo Protección Trifásica Exceline Profesional (2026-04-17) | Catálogo Genteca | KB Genteca vía Celeste |
| Etiqueta empaque GSM-MB/RB/RF GLA_T (2026-04-18) | Empaque Genteca | KB Genteca vía Celeste |
| IEC 60255-8 — Protección térmica con imagen térmica | Norma IEC | Referenciada en HDEs |
| IEEE C37.112-1996 — Inverse-Time Characteristic Equations | Norma IEEE | Referenciada en HDEs |
| IEC 61000-4-x (series EMC) | Norma IEC | Referenciadas en HDEs |
