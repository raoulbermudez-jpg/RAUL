---
doc_type: VA-1-messaging-architecture
project_id: portfolio-naming-ip-2026
domain: genteca
version: v1.0
author: Vael
fecha: 2026-05-13
inputs:
  - 00-project-charter.md (v1.0)
  - 01-checkpoint-1-resolution.md
  - Aurelio_AU-1_top7-mapping-preliminar_v1.md
  - Vera_VR-1_tech-inventory-hybrid_v1.md
  - Orlan_OL-1_differentiation-matrix_v1.md
outputs_downstream:
  - Phase 3: Bruna (gate de claims)
  - Phase 4: Solenne (naming, dirección semántica)
  - Phase 5: Vivienne (deck), Vera+Orlan (Anexo Técnico)
---

# VA-1 — Messaging Architecture
## Portfolio Naming IP 2026 (Genteca)

> Arquitectura de mensajes para el portafolio de tecnologías diferenciadoras Genteca. No es messaging de campaña — es el marco que sostiene la identidad de cada nodo tecnológico ante audiencias, alimenta los candidatos de nombre (Phase 4) y prepara los claims para el gate de Bruna (Phase 3).
>
> Los beneficios del beneficio (Layer 2) de este documento son la versión consolidada y confirmada que sobreescribe la columna L2 del AU-1 para todos los efectos de producción posterior (Solenne, Vivienne).

---

## 1. Pilares de messaging del portafolio

El inventario de Vera arroja 8 nodos. Orlan identifica 2 verdes (diferenciadores únicos verificados), 4 amarillos (bien ejecutados en el segmento) y 1 rojo (función estándar sin diferenciador propietario documentado). Orlan recomendó no registrar H e I como nodos; el Owner en Checkpoint 1 reformuló NODO-H como Ecosystem GIO.

De ese mapa emergen 3 pilares de messaging que organizan el portafolio tecnológico completo. Un cuarto pilar cubre el Ecosystem GIO. Los pilares son de plataforma — articulan qué tipo de empresa tecnológica es Genteca, no qué hace cada producto.

---

### Pilar 1 — Inteligencia anticipatoria

**Premisa:** Genteca no espera que el daño ocurra para actuar. Sus algoritmos detectan el evento antes de que el equipo lo sienta.

**Qué nodos sostienen este pilar:**
- NODO-B (FlickerGuard): detección de flicker en 20ms — el equipo reacciona antes de que el compresor procese el estrés eléctrico.
- NODO-A (StaggerStart): la reconexión aleatoria es una decisión tomada en el tiempo de retardo — el sistema previene el pico de demanda antes de que ocurra.
- NODO-D (ThermalCurve): la curva cold/hot actúa sobre el estado térmico proyectado, no sobre el daño ya consumado. [Supeditado a gate Bruna Phase 3]

**RTB técnico (Vera):**
- 20ms de detección de flicker documentados en GSM-L HDE v10 — el umbral más agresivo identificado en el segmento residencial/comercial.
- Componente aleatoria del retardo de reconexión documentada en HDEs GSM-MB v3-n, v4, v5, v6, v6-rv1.
- Curva caliente = curva fría / 3 — el sistema ajusta el tiempo de disparo según el estado térmico histórico del motor (IEEE C37.112 / IEC 60255-8).

**RTB competitivo (Orlan):**
- En el segmento residencial/comercial de bajo costo para VE/MX, no hay equivalente publicado de la especificación 20ms.
- La competencia industrial (ABB, Siemens) tiene detección sub-ciclo, pero no en la categoría de supervisor enchufable residencial ni en el mismo punto de precio.
- La función staggered restart de Eaton se llama "Voltage Loss Restart" — nombre descriptivo sin branding de fantasía. Genteca tiene naming diferenciador donde Eaton solo tiene un parámetro configurable.

**Cómo se dice ante cada audiencia:**
- Residencial (Exceline): "El equipo actúa antes de que el daño llegue."
- Industrial/Profesional (Exceline Profesional): "Ventana de detección sub-ciclo: 20ms."
- Especificadores (Genius): "Algoritmo de decisión anticipatoria — respuesta proporcional a la desviación, no binaria."

---

### Pilar 2 — Memoria operativa que elimina la intervención humana

**Premisa:** En ambientes donde el corte eléctrico es rutinario, la diferencia entre un equipo inteligente y uno básico es si el proceso continúa solo o requiere un operador que lo reinicie.

**Qué nodos sostienen este pilar:**
- NODO-G (TaskMemory): el GRN-MV memoriza el modo operativo activo al momento del corte y lo retoma al restablecer la energía.
- NODO-A (StaggerStart): la reconexión automática escalonada aplica sin intervención del usuario — el retardo es un parámetro configurado una vez, no una acción repetida.

**RTB técnico (Vera):**
- "Retoma automáticamente la última función al restablecerse la energía, sin requerir intervención del usuario" — texto literal de HDE GRN-MV v9.
- Tres modos persistidos: vaciado de pozo, llenado de tanque, espera (HDE GRN-MV v9).
- Tiempo de confirmación 10s post-restablecimiento: confirmado verbalmente por I+D [RTB pendiente de actualización en HDE — gap documental conocido].
- Ventana de temporizado ajustable en StaggerStart: 5-180s (GSM-MB v6), 180-300s (GSM-RB), 3 min fijo (GSM-NG).

**RTB competitivo (Orlan):**
- No se identificó ningún fabricante con función equivalente de memoria de modo operativo en controladores de nivel/bombeo residencial-comercial.
- La competencia (ABB, Siemens, Rockwell) tiene memoria de estado en PLCs programables por el usuario — no es un feature diferenciador nombrado, es una capacidad del programa. El GRN-MV la entrega como feature estándar sin programación adicional.
- Orlan califica NODO-G como verde — el diferenciador más limpio del portafolio para su segmento.

**Cómo se dice ante cada audiencia:**
- Industrial/Profesional (Exceline Profesional GRN-MV): "El proceso retoma solo. Sin llamar al operador."
- Residencial (Exceline): "El sistema vuelve a funcionar donde lo dejaste — sin que hagas nada."

---

### Pilar 3 — Diagnóstico que cierra el ciclo de mantenimiento

**Premisa:** Cuando un equipo falla repetidamente, el costo no es el fallo en sí — es el tiempo perdido reconstruyendo qué pasó. Genteca cierra ese ciclo con registro forense y lógica de bloqueo que obliga la intervención técnica deliberada.

**Qué nodos sostienen este pilar:**
- NODO-E (ForensLog): registro de hasta 100 eventos de falla con timestamp, valor medido, duración y parámetros activos al momento de la falla.
- NODO-F (TripleLock): bloqueo permanente tras tercera falla de corriente recurrente en ventana de 30 minutos — el equipo no puede rearrancar sin intervención técnica explícita.

**RTB técnico (Vera):**
- 100 últimas fallas con timestamp: documentado en HDE GIII+MV-V1 (español e inglés). Baseline de la gama Genius: 20 últimas fallas.
- Acceso dual al registro: pantalla LCD + MODBUS RTU.
- Bloqueo tras 3 fallas de corriente en menos de 30 minutos: documentado en GIII+ HDE sección E, GOC HDE sección E, catálogo Genius, catálogo trifásico GSC.
- Tiempo de disparo en tercera falla: menos de 1 segundo (GOC HDE sección E).
- Reset manual obligatorio para restablecer operación tras bloqueo permanente.

**RTB competitivo (Orlan):**
- Rockwell E300 tiene 5 registros de trip + 5 de warning = 10 registros totales (verificado en manual E300 193-UM015). El GIII+MV tiene 100 — 10 veces más que el competidor más cercano identificado en la misma clase de producto.
- TripleLock: la competencia tiene "inhibit restart" como parámetro configurable, sin identidad de feature. Genteca tiene la función nombrada y diferenciada como lógica de bloqueo automático visible.

**Cómo se dice ante cada audiencia:**
- Industrial/Profesional (Exceline Profesional / Genius): "El historial de fallas está en el relé — sin depender del operador que recuerde qué pasó."
- Especificadores (Genius): "100 eventos con timestamp, valor medido y parámetros activos. Diagnóstico en campo, sin especulación."
- Residencial/comercio (Exceline): menos relevante para este pilar — no aplica como mensaje primario.

---

### Pilar 4 — Ecosystem industrial integrado desde el diseño

**Premisa:** La conectividad en Genteca no es un accesorio posterior. La arquitectura GIO (GIO PORT + GIO-Link + GIO-Tool) está embebida en toda la gama Genius desde el diseño del producto.

**Qué nodos sostienen este pilar:**
- NODO-H reformulado (Ecosystem GIO): GIO PORT en todos los relés Genius + accesorios GIO-Link (USB/RS-232/RS-485) + software GIO-Tool + MODBUS RTU hasta 32 relés en bus.

**RTB técnico (Vera):**
- MODBUS RTU integrado: 9600 baud en todos los relés Genius; 9600/19200/38400 baud en GIII+MV (RS-485 integrado).
- Capacidad de red: hasta 32 relés en bus RS-485 vía GIO-A-RS485K.
- Variables accesibles vía bus: corriente, voltaje, frecuencia, kW/kVA/kWh, factor de potencia, temperatura, histórico de fallas, comandos encendido/apagado remoto, lectura/escritura de parámetros con contraseña.
- GIO-Tool: monitorización en tiempo real + extracción de históricos + gráficas de tendencias + exportación CSV.

**RTB competitivo (Orlan):**
- Siemens SIMOCODE 3UF7: comunicación vía módulo separado (PROFIBUS, Ethernet — no MODBUS nativo de base).
- Eaton C440/C441: MODBUS disponible vía módulo adicional C440/XTOE.
- Rockwell E300: EtherNet/IP, DeviceNet — MODBUS no es el protocolo primario.
- En el segmento Genius de VE/MX, el Ecosystem GIO entrega conectividad industrial sin módulos adicionales ni programación especializada. Orlan califica este nodo como amarillo — el diferenciador es la ejecución para el segmento, no la función global.
- Nota de Orlan: "en el segmento LatAm donde la conectividad en relés básicos no está dada por sentada, el Ecosystem GIO puede ser sorprendentemente verde".

**Cómo se dice ante cada audiencia:**
- Especificadores (transversal Genius): "32 relés en un bus. Configuración, monitorización y diagnóstico desde un punto."
- Industrial/Profesional: "El relé ya trae el puerto. Solo necesitas el adaptador."

---

## 2. Matriz de mensajes: nodo × audiencia × beneficio

> Celdas con Layer 1 (beneficio técnico) y Layer 2 (beneficio del beneficio) cuando existe. Layer 2 es el mensaje que prima para audiencia residencial. Layer 1 es el mensaje que prima para especificadores.
>
> Audiencias según charter §5: (A) Exceline residencial/comercio pequeño, (B) Exceline Profesional industrial/comercio profesional, (C) Genius premium/especificadores, (D) Especificadores técnicos transversal.
>
> Columna "Flag" marca si el claim requiere gate de Bruna o tiene gap documental conocido.

---

### NODO-A — StaggerStart (Reconexión temporal aleatoria post-falla)

| Audiencia | Layer 1 (beneficio técnico) | Layer 2 (beneficio del beneficio) | Flag |
|-----------|----------------------------|-----------------------------------|------|
| A — Exceline residencial | El equipo espera el momento correcto para reconectar — no arranca de golpe junto a todos los demás | Tu compresor y el de tu vecino no reciben el mismo golpe de corriente al mismo tiempo — el sistema de la instalación no colapsa en el reencendido | — |
| B — Exceline Profesional | Retardo configurable 5-300s con componente aleatoria — previene pico de demanda simultáneo en instalaciones con múltiples unidades | El compresor industrial no cicla entre apagado y arranque forzado repetido — menos desgaste mecánico por arranques en secuencia desordenada | — |
| C — Genius premium | Algoritmo de escalonamiento aleatorio documentado — ventana configurable, cumple función anti-demand-spike en MCC | — | — |
| D — Especificadores técnicos | Ventana ajustable 5-300s + componente aleatoria — normas IEC 61000-4-x / COVENIN 3445 verificadas | — | — |

**Nota de pilar:** NODO-A ancla Pilar 1 (anticipatoria) y Pilar 2 (sin intervención humana).

---

### NODO-B — FlickerGuard (Detección sub-ciclo de perturbaciones de voltaje)

| Audiencia | Layer 1 | Layer 2 | Flag |
|-----------|---------|---------|------|
| A — Exceline residencial | Detecta el parpadeo de la corriente en 20ms — desconecta el equipo antes de que el estrés eléctrico llegue al motor | El compresor del AC o del refrigerador no se daña por el estrés de los arranques forzados por parpadeo eléctrico | — |
| B — Exceline Profesional | Ventana de detección 20ms (GSM-L) — la especificación más agresiva en supervisores de voltaje monofásico del segmento residencial/comercial en VE/MX | El motor no absorbe el golpe mecánico del arranque forzado por evento sub-ciclo | — |
| C — Genius premium | Detección sub-ciclo documentada en HDE v10 — sin equivalente publicado en la competencia directa para esta clase de producto y punto de precio | — | ⚠ Búsqueda OMPI ampliada pendiente (ver VA-5) |
| D — Especificadores técnicos | 20ms para GSM-L; 150ms para GSM-MB/RB/RE/NG — tiempo de desconexión proporcional a la intensidad (0,02-2s GSM-AV06; 0,4-3s GSM-RB) — IEC 61000-4-4 / IEC 61000-4-14 | — | — |

**Nota de pilar:** NODO-B es el nodo más fuerte del portafolio en Pilar 1 (Inteligencia anticipatoria). Es el único nodo verde de una categoría diferenciadora en el segmento residencial.

---

### NODO-C — Thermo-Safe (Modelo térmico NTC integrado)

| Audiencia | Layer 1 | Layer 2 | Flag |
|-----------|---------|---------|------|
| A — Exceline residencial | El protector tiene un sensor de temperatura integrado que mide el calor real del motor — no solo la corriente | Tu motor no se quema por sobrecalentamiento silencioso que la protección normal no ve | ⚠ RTBs numéricos NTC no en HDE actual (ver VA-5) |
| B — Exceline Profesional | Sensor NTC embebido en el protector monofásico — sin módulo adicional ni cableado externo | El motor industrial no pierde ciclos por temperatura no detectada — la protección térmica real desconecta antes del daño | ⚠ RTBs numéricos NTC pendientes de I+D |
| C — Genius premium | Integración NTC estándar de serie en GSM-MB/RB/RE — feature que la competencia ofrece como módulo separado a mayor costo | — | ⚠ Caso A/B pendiente Bruna |
| D — Especificadores técnicos | Sensor NTC integrado — lectura directa de temperatura real vs modelo I-t puro de NODO-D. Complementario, no sustituto | — | ⚠ Parámetros técnicos NTC (umbral, rango, histéresis) no confirmados en HDE |

**Nota de pilar:** NODO-C ancla Pilar 1 (anticipatoria) en la dimensión térmica. El mensaje de L2 para residencial es el más importante de este nodo.

**Nota de carry-forward:** El gap documental NTC (Vera NOTA-2) limita la profundidad de claims técnicos hasta que I+D provea la HDE actualizada. El messaging se construye sobre los hechos disponibles (presencia del NTC confirmada por empaque, función de protección documentada), sin atributos numéricos que hoy no tienen soporte en HDE.

---

### NODO-D — ThermalCurve (Curva inversa I-t cold/hot)

> **Nota de estado:** NODO-D tiene gate crítico de Bruna en Phase 3. El messaging aquí se construye asumiendo que Bruna aprueba el diferenciador algorítmico propietario. Si Bruna lo rechaza, el nodo sigue existiendo pero el nombre anchor cambia — el messaging de L1/L2 aplica igual con el nombre de reemplazo.

| Audiencia | Layer 1 | Layer 2 | Flag |
|-----------|---------|---------|------|
| A — Exceline residencial | Menos relevante como mensaje primario — la audiencia residencial consume Thermo-Safe (NODO-C), no la curva algorítmica | — | — |
| B — Exceline Profesional | El relé calcula el estado térmico del motor según la historia de carga — el tiempo de disparo es proporcional al estado real, no a un umbral fijo | El motor que arrancó en caliente no recibe la misma curva de protección que el que arrancó en frío — el disparo llega cuando el motor lo necesita, no antes ni después | ⚠ Defendibilidad del diferenciador algorítmico propietario: gate Bruna |
| C — Genius premium | Curva fría vs curva caliente: curva caliente = curva fría / 3. Clase térmica ajustable 5-30 en pasos de 1. Implementado según IEEE C37.112 / IEC 60255-8. Memoria térmica: hasta 2 horas | — | ⚠ Gate Bruna: diferenciador propietario o nombre estándar |
| D — Especificadores técnicos | Imagen térmica con estado cold/hot: curva fría clase hasta 30, caliente hasta 3 veces más rápido. Memoria térmica de hasta 2 horas documentada. Clases: 5, 10, 15, 20, 25, 30 | — | ⚠ Gate Bruna — funcionalidad IEC estándar ubiqua en competencia |

**Nota de pilar:** NODO-D ancla Pilar 1 (anticipatoria) solo si el diferenciador algorítmico propietario puede documentarse más allá del estándar IEC. Sin ese RTB, el pilar se sostiene igual sobre NODO-A y NODO-B, y NODO-D aporta profundidad técnica pero sin diferenciador de naming.

---

### NODO-E — ForensLog (Registro forense histórico de fallas)

| Audiencia | Layer 1 | Layer 2 | Flag |
|-----------|---------|---------|------|
| A — Exceline residencial | Menos relevante — la audiencia residencial no diagnostica fallas con historial. No es el mensaje primario para Exceline. | — | — |
| B — Exceline Profesional | El relé registra las últimas fallas con hora, fecha, valor medido y duración — el técnico consulta el historial sin depender del operador que recuerde qué pasó | El diagnóstico es preciso desde el primer minuto de intervención — menos tiempo fuera de servicio, menos costo de visita técnica | — |
| C — Genius premium | Hasta 100 últimas fallas (GIII+MV) con timestamp completo, valor medido, duración y parámetros activos al momento — acceso vía pantalla LCD o MODBUS RTU | — | ⚠ RTB "100 fallas" acotado a GIII+MV; baseline gama Genius = 20 fallas (ver nota ForensLog en VA-5) |
| D — Especificadores técnicos | 100 eventos (GIII+MV) vs 5 trips + 5 warnings en Rockwell E300 (verificado). Campos por evento: tipo, valor, hora, fecha, duración, parámetros activos. Acceso dual LCD + bus | — | — |

**Nota de pilar:** NODO-E ancla Pilar 3 (diagnóstico que cierra el ciclo). Es el mensaje más relevante para especificadores e industria.

**Nota ForensLog RTB (Checkpoint 1 Decisión 3):** el messaging se construye en dos escenarios según la decisión de Solenne en Phase 4:
- Escenario A (acotar a GIII+MV): claim "100 fallas" limpio, sin matiz. RTB sólido.
- Escenario B (ampliar a gama Genius): claim "hasta 100 fallas en GIII+MV / 20 fallas en gama Genius" — el mensaje pierde potencia pero gana amplitud de producto.
- El messaging de L2 (diagnóstico preciso, menos tiempo fuera de servicio) aplica en ambos escenarios sin cambio.

---

### NODO-F — TripleLock (Bloqueo permanente tras tercera falla recurrente)

| Audiencia | Layer 1 | Layer 2 | Flag |
|-----------|---------|---------|------|
| A — Exceline residencial | Menos relevante como mensaje primario — la audiencia residencial no gestiona ciclos de falla recurrente. | — | — |
| B — Exceline Profesional | Tres fallas de corriente en menos de 30 minutos activan bloqueo permanente — el equipo no rearranque solo hasta que un técnico lo examine | El equipo industrial no entra en el ciclo destructivo de falla-rearranque-falla que destruye el motor antes de que alguien intervenga | — |
| C — Genius premium | Bloqueo automático ante tercera falla de corriente en ventana de 30 min. Disparo < 1 segundo en tercera falla. Reset manual obligatorio. Aplica a sobrecarga, desbalance y pérdida de fase por corriente | — | — |
| D — Especificadores técnicos | Contador de fallas de corriente (cualquier tipo): sobrecarga, desbalance, pérdida de fase. Ventana: 30 min. Umbral: 3. Disparo permanente < 1s. Reset: manual obligatorio (documentado en GIII+, GOC, GSPT, GUCT+, GOCT, GSC-CR, GSC-MB) | — | ⚠ Verificar colisión clase 9 seguridad física (búsqueda BR-2 previo) |

**Nota de pilar:** NODO-F ancla Pilar 3 (diagnóstico y cierre del ciclo). El mensaje de L2 para audiencia B es el más importante.

---

### NODO-G — TaskMemory (Memoria de estado y reanudación de tarea post-corte)

| Audiencia | Layer 1 | Layer 2 | Flag |
|-----------|---------|---------|------|
| A — Exceline residencial | Menos relevante en uso residencial puro — más alineado con GRN-MV en instalaciones de riego o bombeo domiciliario. | Si el equipo de riego del jardín estaba vaciando el tanque cuando se fue la luz, retoma solo cuando vuelve | — |
| B — Exceline Profesional | El GRN-MV almacena el modo operativo activo al momento del corte (vaciado pozo / llenado tanque / espera) y lo retoma automáticamente al restablecer la energía | El proceso de bombeo o riego no pierde el ciclo ni requiere supervisión humana en el reencendido — el equipo sigue desde donde estaba | — |
| C — Genius premium | Función diferenciadora en controladores de nivel: memoria de modo operativo persistida sin intervención de usuario. Sin equivalente nombrado en la competencia para esta clase de producto. | — | — |
| D — Especificadores técnicos | Tres modos persistidos (vaciado pozo / llenado tanque / espera) — lectura de sondas de conductividad + recuperación de estado almacenado. Confirmación 10s post-restablecimiento antes de actuar salida [RTB pendiente actualización HDE] | — | ⚠ RTB 10s pendiente actualización HDE/MAN |

**Nota de pilar:** NODO-G ancla Pilar 2 (memoria operativa) como el nodo más fuerte. Es el único nodo verde con beneficio del beneficio L2 claro para todas las audiencias relevantes.

---

### NODO-H — Ecosystem GIO (Conectividad industrial integrada)

> **Nota de alcance:** el messaging de NODO-H se construye sobre el Ecosystem GIO (GIO PORT + GIO-Link + GIO-Tool) como denominación propietaria. Los candidatos de naming de Solenne no deben contener MODBUS ni términos de protocolo estándar (Checkpoint 1, Decisión 1).

| Audiencia | Layer 1 | Layer 2 | Flag |
|-----------|---------|---------|------|
| A — Exceline residencial | No aplica — conectividad industrial no es mensaje para audiencia residencial. | — | — |
| B — Exceline Profesional | El GIO PORT integrado en todos los relés Genius permite conexión directa a red industrial sin módulos adicionales | El técnico de mantenimiento accede a lecturas en tiempo real y al historial de fallas desde un punto — sin instalar hardware adicional | — |
| C — Genius premium | GIO PORT + GIO-Link: red de hasta 32 relés en bus RS-485. Variables accesibles: I, V, frecuencia, kW/kVA/kWh, FP, temperatura, histórico de fallas, comandos on/off remoto, parámetros con contraseña | — | ⚠ Confirmar que candidatos de naming no usan MODBUS ni términos de protocolo estándar (Bruna gate NODO-H) |
| D — Especificadores técnicos | MODBUS RTU: 9600 baud estándar / 9600-38400 baud GIII+MV. Protocolo 8N1. Direcciones 1-127. GIO-Tool: monitorización en tiempo real + históricos + CSV. Red: hasta 32 relés. Interfaces: USB, RS-232, RS-485 | — | — |

**Nota de pilar:** NODO-H ancla Pilar 4 (Ecosystem industrial integrado). El diferenciador no es la conectividad — es la integración desde el diseño para el segmento de la gama media Genius en VE/MX.

---

## 3. Anti-mensajes por nodo

Lo que NO se debe decir, aunque suene bien. Alimenta directamente el gate de Bruna en Phase 3.

| Nodo | Anti-mensaje | Por qué no |
|------|-------------|------------|
| NODO-A (StaggerStart) | "Protección inteligente única en la categoría" | La función de staggered restart la tiene Eaton C445 — el diferenciador es el segmento y punto de precio, no la unicidad de la función |
| NODO-A | "Tecnología exclusiva Genteca de reconexión aleatoria" | Exclusividad no sostenida — el mecanismo existe en la competencia industrial |
| NODO-B (FlickerGuard) | "El único protector que detecta flicker" | No se puede sostener "único" sin búsqueda OMPI confirmada y sin descartar todos los competidores posibles en el segmento |
| NODO-B | "Protección contra parpadeos en tiempo real" | "Tiempo real" es ambiguo — el RTB específico es 20ms, que es el claim defendible |
| NODO-C (Thermo-Safe) | "Protección térmica inteligente con datos NTC en tiempo real" | Los parámetros técnicos del NTC (umbral, rango, histéresis) no están en HDE actual — no se puede hacer claim cuantitativo |
| NODO-C | "Temperatura exacta del motor, siempre" | Exactitud no documentada cuantitativamente — el claim de temperatura real vs modelo I-t es correcto, pero "exacta" agrega precisión que no tiene soporte documental hoy |
| NODO-D (ThermalCurve) | "Algoritmo térmico propietario de Genteca" | Propietariedad no documentada hasta que Vera lo confirme y Bruna lo gate — la curva inversa I-t es estándar IEC |
| NODO-D | "Tecnología exclusiva de protección térmica adaptativa" | La adaptación cold/hot es ubiqua en la competencia industrial — no es exclusiva |
| NODO-D | "La protección térmica más avanzada del mercado" | NODO-D es rojo en la matriz de Orlan — este claim no tiene base competitiva |
| NODO-E (ForensLog) | "Registro de 100 fallas — toda la línea Genius" | "100 fallas" aplica solo a GIII+MV. El baseline gama Genius es 20 fallas. Decirlo como universal del nodo sin matiz es incorrecto. |
| NODO-E | "Diagnóstico completo sin herramientas externas" | El acceso vía bus MODBUS requiere software/hardware GIO-Link — no es completamente autónomo |
| NODO-F (TripleLock) | "Sistema de bloqueo único para protección de motores" | La función de bloqueo tras fallas recurrentes existe en competencia como parámetro configurable — el diferenciador es el naming y la ejecución, no la unicidad de la función |
| NODO-G (TaskMemory) | "Memoria inteligente que recuerda todo" | El scope de la memoria es específico: modo operativo del GRN-MV. No aplica a toda la gama ni a todos los parámetros — el claim genérico es sobredimensionado |
| NODO-G | "El sistema aprende tu rutina de riego" | "Aprender" implica IA/ML — lo que hace TaskMemory es persistir el modo activo al momento del corte, no aprender patrones |
| NODO-H (Ecosystem GIO) | "Conectividad sin límites para toda la gama Genteca" | La conectividad GIO aplica a la gama Genius, no a Exceline residencial. Y MODBUS RTU tiene límites de red (32 nodos, velocidad) |
| NODO-H | "Tecnología de comunicación propietaria Genteca" | MODBUS RTU es protocolo estándar abierto — solo el ecosystem GIO (GIO PORT, GIO-Link, GIO-Tool) es denominación propietaria |

---

## 4. Notas para Solenne (Phase 4) — Dirección semántica por nodo

> Estas notas orientan la dirección semántica del naming. No dictan nombres específicos — eso es territorio de Solenne. Cuando el beneficio del beneficio (Layer 2) es fuerte, el nombre debería evocar la consecuencia palpable. Cuando el diferenciador es técnico, el nombre debería evocar el mecanismo.

**NODO-A — StaggerStart:**
Anchor tiene buen perfil semántico — la raíz "Stagger" es técnicamente específica, raramente usada en nombres registrados clase 9 en LatAm, y evoca el escalonamiento sin ser descriptiva literal para el consumidor. El Layer 2 (el compresor no recibe el golpe) es un beneficio de instalación / protección sistémica, no individual. El nombre puede ir hacia el mecanismo (escalonamiento, secuencia) o hacia el beneficio sistémico (estabilidad del arranque conjunto). Evitar raíces "Restart" o "Reconnect" — demasiado descriptivo. Territorio disponible: raíces Stagger, Stage, Cascade, Seq.

**NODO-B — FlickerGuard:**
El Layer 2 (el compresor no se daña) es el mensaje más fuerte para audiencia residencial. El nombre debería evocar protección de lo que importa (el equipo downstream), no el fenómeno eléctrico. Sin embargo, "Flicker" como raíz es técnicamente precisa y diferenciadora en el naming — la audiencia residencial no necesita entender el nombre técnico para asociarlo con la marca. Si FlickerGuard supera la búsqueda OMPI limpiamente, mantenerlo es la decisión correcta — tiene potencia y raíz limpia. Si hay colisión, el espacio semántico de reemplazo está en protección sub-ciclo: raíces Pulse, Surge, Spike, Sag (menos potentes comercialmente pero más limpias).

**NODO-C — Thermo-Safe:**
El Layer 2 (el motor no se quema por sobrecalentamiento encubierto) es muy potente para residencial. El nombre debería evocar protección térmica activa, no medición. "Thermo-Safe" tiene ese perfil — pero el riesgo de descriptividad obliga a considerar raíces que se alejen de la combinación Thermo+Safe si Bruna lo degrada. El diferenciador de Genteca en este nodo es la integración de hardware (NTC en el protector, sin módulo externo) — el nombre puede evocar integración o completitud. Si Bruna fuerza reemplazo: alejarse del territorio semántico "temperatura + seguridad" hacia territorio de "completitud de protección" (CoreProtect, FullGuard — evitar estos ejemplos; son solo orientación de dirección).

**NODO-D — ThermalCurve:**
El Layer 2 (el motor no dispara prematuro en caliente ni queda desprotegido en frío) es el argumento real de valor. Pero el nombre de este nodo tiene riesgo alto de descriptividad — "ThermalCurve" describe literalmente el mecanismo IEC estándar. Si Bruna lo aprueba con RTB propietario documentado, el nombre se sostiene con ese diferenciador. Si Bruna lo rechaza, la dirección semántica del reemplazo debería alejarse completamente de "curva" y "térmica" — no son territorios disponibles. El beneficio real es la adaptación al estado real del motor, no la curva en sí. Territorios disponibles: raíces que evoquen adaptación, estado, estado de arranque (AdaptShield, StateGuard — evitar estos ejemplos; solo indican dirección).

**NODO-E — ForensLog:**
El Layer 2 (diagnóstico preciso desde el primer minuto, sin depender del operador) es el mensaje más potente para la audiencia técnica. El nombre debería evocar registro con connotación de auditoría o forense — que transmita "evidencia" más que "datos". "ForensLog" lo logra bien: "forense" en el nombre activa la connotación de reconstrucción técnica. El espacio de naming de reemplazo (si hay colisión en clase 9 software) debe ir hacia lo forense-técnico: evidencia, registro, historial técnico. Evitar raíces puramente genéricas de software (Log, Data, Event). La dirección correcta está en FaultVault, DiagTrace — solo como orientación de territorio.

**NODO-F — TripleLock:**
El Layer 2 (el equipo no entra en el ciclo destructivo de falla-rearranque-falla) es el argumento de valor real. El nombre evoca la acción (bloqueo tras triple evento) — funciona bien para audiencia técnica. El riesgo de colisión en clase 9 seguridad física obliga a verificar si "Lock" como raíz tiene espacio limpio en SAPI/IMPI para equipo eléctrico. Si hay colisión, la dirección semántica del reemplazo debería ir hacia "bloqueo de ciclo" o "control de secuencia", no hacia cierre físico. El mecanismo es la interrupción deliberada del ciclo — raíces con "Gate", "Hold", "Block" en el contexto de fallas recurrentes.

**NODO-G — TaskMemory:**
El Layer 2 (el proceso no pierde el ciclo, el operador no tiene que hacer nada) es el más potente de todos los nodos en claridad de beneficio para audiencia B. El nombre "TaskMemory" captura el mecanismo pero tiene riesgo de colisión con clase 9 software (gestión de tareas en informática). Si hay colisión, la dirección de reemplazo debería alejarse del vocabulario software y acercarse a la continuidad del proceso físico. El beneficio real es la continuidad sin intervención — raíces que evoquen retomar, continuar, persistir en el contexto de proceso industrial (ModeKeep, CycleResume — solo para indicar dirección, no nombres propuestos).

**NODO-H — Ecosystem GIO:**
Los candidatos de naming deben anclar en la familia GIO o construir nombres alternativos para el ecosystem propietario. La instrucción del Checkpoint 1 es clara: no contener "MODBUS" ni términos descriptivos de protocolo estándar. El diferenciador a evocar es la integración sistémica — no la conectividad genérica, sino el ecosystem de herramientas y puertos propios que funcionan juntos. La dirección semántica es el ecosystem como denominación de sistema integrado, no de protocolo. Raíces candidatas: GIO-*, nombres que evoquen red, enlace, sistema integrado — siempre anclados en el ecosystem propietario, no en el estándar subyacente.

---

## Supuestos y límites

**Insumos aguas arriba:**
- Vera VR-1 (tech inventory hybrid v1.0, 2026-05-13): RTBs técnicos verificables por nodo. Gaps documentales conocidos: NODO-C (parámetros NTC no en HDE), NODO-G (10s no en HDE), NODO-B (denominación curva inversa V-t no en HDEs).
- Orlan OL-1 (differentiation matrix v1.0, 2026-05-13): mapa verde/amarillo/rojo. Varios datos de competencia marcados [CLAIM] — no verificados contra datasheet primario en Phase 1. Requieren refuerzo antes del Anexo Técnico (Phase 5).
- AU-1 (top7 mapping v1.0, 2026-05-13): Layer 2 preliminar por anchor. Este VA-1 sobreescribe esa columna para todos los efectos de producción posterior.
- Charter §3 decisión 4: override curva inversa universal de facto asumido — no auditado producto por producto.
- Checkpoint 1 Resolución: 8 nodos confirmados, NODO-H reformulado como Ecosystem GIO, ForensLog RTB decisión diferida a Solenne, ThermalCurve gate diferido a Bruna.

**Validez temporal:** Este messaging es válido mientras los insumos de Vera y Orlan no cambien. Si Vera actualiza RTBs del NODO-C (NTC) o confirma el RTB diferenciador algorítmico del NODO-D, este VA-1 debe actualizarse en la sección de pilares y en la matriz antes de Phase 5.

**Triggers de invalidación:**
- Bruna rechaza ThermalCurve en Phase 3: el messaging del NODO-D en Pilar 1 debe ajustarse (el pilar sigue en pie con NODO-A y NODO-B).
- I+D provee HDE con parámetros NTC: actualizar NODO-C en matriz (especialmente columnas B y D) para incluir claims cuantitativos ahora ausentes.
- Solenne en Phase 4 decide ForensLog en escenario B (ampliar a gama Genius): actualizar la celda C de NODO-E para reflejar "hasta 100 fallas en GIII+MV / 20 fallas en gama Genius".
- Búsqueda OMPI confirma colisión FlickerGuard: el nodo B mantiene el messaging; cambia el anchor del naming.

**Claims con gate Bruna pendiente (para Phase 3):**
1. ThermalCurve — diferenciador algorítmico propietario vs. estándar IEC (crítico)
2. Override curva inversa universal de facto — defendibilidad en publicidad sin auditoría producto por producto
3. Thermo-Safe Caso A/B — si NTC aparece en empaque, impacto en claims
4. FlickerGuard — colisión potencial en clase 9 con productos LED (búsqueda OMPI pendiente)
5. TaskMemory — colisión potencial en clase 9 software
6. TripleLock — colisión potencial en clase 9 seguridad física
7. NODO-H — confirmar que candidatos no usan términos de protocolo estándar

**Decisiones Owner pendientes:** ninguna que bloquee Phase 3.

---

*Vael — VA-1 Phase 2 completa. Listo para Phase 3 (Bruna).*
