# 15 Preguntas para el equipo de Engineering / Firmware del GME

**De**: Owner (Raoul Bermúdez) — Genteca / Exceline
**Para**: Equipo de desarrollo GME
**Fecha**: 2026-05-06
**Lanzamiento previsto**: octubre 2026
**Origen**: validación técnica Vera (`_intel/Vera_validacion_tecnica_GME_2026-05-06.md`) cruzada con encuesta UI mayo 2026 (n=29 técnicos) y análisis competitivo Orlan OL-3.

---

## Por qué necesitamos estas respuestas

Cada pregunta cierra un gap entre **lo que muestran los mockups de la UI** y **lo que efectivamente hace el firmware**. Las respuestas habilitan o bloquean los claims que Marketing puede usar al lanzar el producto, y definen los riesgos de responsabilidad civil que Riesgo (Bruna) debe gestionar antes del lanzamiento.

**Convención sugerida de respuesta**: agregar la respuesta debajo de cada pregunta y devolver el archivo completo. Si una respuesta requiere conversación, marcar con `[discutir]` y avanzar con las demás.

---

## Prioridades

| Prioridad | Preguntas | Por qué |
|---|---|---|
| 🔴 **Alta — gate del lanzamiento** | Q2, Q3, Q7, Q8, Q9, Q11, Q14, Q15 | Bloquean claims principales o son seguridad |
| 🟡 **Media — refinan messaging** | Q1, Q4, Q5, Q6, Q12 | Definen profundidad de diferenciación y manejo de riesgo |
| 🟢 **Baja — roadmap** | Q10, Q13 | Pueden esperar a v2 si no están |

---

## Bloque A — Arquitectura y seguridad (gate del Claim "Sin app, sin cloud")

### 🔴 Q2. Operación offline (WiFi caído)

¿El GME protege activamente (actúa el contactor) si **no hay ninguna red WiFi** activa? ¿La lógica de protección es **independiente** del webserver WiFi?

**Esto es el gate del claim "Sin app, sin cloud requerida"**. Si la respuesta es no, es un gap de arquitectura crítico que debe resolverse antes del lanzamiento — un protector que deja de proteger porque se cayó el WiFi de la casa es un riesgo de responsabilidad civil.

**Respuesta esperada**:
- [ ] Sí, protege completamente sin WiFi
- [ ] No, requiere WiFi activo para protección
- [ ] Parcial — explicar:

---

### 🔴 Q3. Arquitectura MCU — separación protección / webserver

¿El procesamiento de la lógica de protección y el servidor web HTTP corren en el **mismo microcontrolador** o en **unidades separadas**? ¿Hay watchdog dedicado para la función de protección, independiente del sistema operativo del webserver? ¿Un cuelgue del webserver (overflow, bug, ataque de red) puede inhibir la protección?

**Por qué importa**: si ambos corren en el mismo MCU sin watchdog separado, un ataque de denegación de servicio sobre el puerto 80 podría dejar el equipo sin protección. Es una vulnerabilidad de seguridad relevante.

**Respuesta esperada** (formato libre):

---

### 🔴 Q15. Lógica "tres intentos" para subcarga y sobrecarga

El log de fallas muestra "Off **Tercera falla** de Sobrecarga" y "Off **Tercera falla** de Subcarga". ¿El firmware hace tres intentos de rearranque antes de bloquear definitivamente?

- ¿Cuándo se resetea el contador de intentos? (¿al cabo de cuánto tiempo sin nuevas fallas?)
- ¿El número de intentos es configurable o está fijo en 3?
- ¿Se aplica solo a sobrecarga/subcarga o también a otros tipos de falla?

**Por qué importa**: este comportamiento debe ser comunicado explícitamente en la documentación de producto. Un técnico que no lo conoce podría no entender por qué el equipo intentó arrancar tres veces antes de bloquear — y en aplicaciones críticas (compresor de refrigeración con subcarga), el tercer intento sin la condición resuelta puede causar daño.

**Respuesta esperada** (formato libre):

---

## Bloque B — Capacidad y rango (gate del Claim "Protección integral")

### 🔴 Q8. Rango de medición de corriente

Para cada variante del producto (R220 / B220 / M220):
- Corriente **mínima confiable** (A) — por debajo de este valor la medición es ruido
- Corriente **máxima sin saturación** (A) — el techo del circuito de medición
- **Exactitud declarada** (±% de full scale o ±% de lectura)
- ¿El rango es el mismo para los tres modelos o hay diferencias de hardware?

**Por qué importa**: sin este dato no podemos hacer ningún claim de aplicabilidad ("protege motores de hasta X HP / Y A"). El benchmark Littelfuse 77C declara ±1% I.

**Respuesta esperada**:

| Variante | I mín. confiable | I máx. saturación | Exactitud |
|---|---|---|---|
| GME-R220 |  |  |  |
| GME-B220 |  |  |  |
| GME-M220 |  |  |  |

---

### 🔴 Q9. Corriente máxima del contactor integrado

- ¿Capacidad en **AC-3** (motor en marcha normal)?
- ¿Capacidad en **AC-4** (arranque con rotor bloqueado)?
- La pantalla de Reporte de Fallas muestra "Sobrecarga 40 A" — ¿40 A es el **límite del contactor** o solo un valor de ejemplo del mockup?
- Vida eléctrica declarada (número de operaciones a I nominal).

**Respuesta esperada**:

---

### 🔴 Q7. Clase de disparo IEC para la lógica de sobrecarga

¿El GME implementa una curva de disparo compatible con **IEC 60947-4-1 Class 10, 10A, 20 o 30**? ¿O es una lógica propia de umbral fijo + temporizador?

- Para refrigeración (compresores herméticos): **Class 10A** es la clase recomendada (tolera arranque en caliente).
- Para bombas y motores de arranque rápido: **Class 10** es estándar.
- ¿El firmware diferencia la clase entre modos R / B / M?

**Por qué importa**: define si el GME puede certificarse bajo IEC 60947-4-1 y si el claim "tres modos en un protector" tiene fundamento técnico real (clase distinta por modo) o solo cosmético (mismos parámetros, defaults distintos).

**Respuesta esperada**:

---

### 🔴 Q11. Detección de pico de arranque diferenciado de régimen

¿El firmware implementa una ventana de **inhibición de disparo durante el arranque** (análoga al "starting inhibit" del Littelfuse 77C) que tolera corriente >I_nominal durante los primeros N segundos?

- Duración de la ventana de inhibición (s)
- ¿Es configurable o fija?
- ¿Cambia entre modos R / B / M?

**Por qué importa**: sin esta función, el GME puede disparar falsamente durante arranque de motores de alta inercia o compresores fríos. Es una solicitud explícita de los técnicos en la encuesta.

**Respuesta esperada**:

---

## Bloque C — Lógica de protección activa

### 🔴 Q14. Protección de frecuencia — activa o diagnóstica

La pantalla de fallas muestra "Inestabilidad: 54 Hz". ¿Esta detección **activa el corte** del contactor o solo registra el evento?

- Umbrales configurados: Hz mín / Hz máx
- Tiempo de detección requerido para disparar
- ¿Es ajustable por usuario?

**Por qué importa**: en mercados con red eléctrica inestable (Venezuela, Caribe), la protección de frecuencia es un diferenciador real **si es activa**. Si solo es diagnóstica, no debe usarse como claim de protección.

**Respuesta esperada**:

---

### 🟡 Q1. Sampling rate del ADC de medición

- Frecuencia de muestreo del ADC (Hz o kHz) para V e I
- Muestras por ciclo de 60 Hz
- Filtrado aplicado antes del display (media móvil, RMS sobre ventana, etc.)
- Filtrado aplicado antes del umbral de disparo

**Por qué importa**: el técnico de refrigeración en la encuesta señaló sensibilidad <1 s como crítica. Un sampling lento implica que fluctuaciones cortas pasan sin detección.

**Respuesta esperada**:

---

### 🟡 Q6. Detección de contactor soldado (welded contact)

¿El GME tiene algún mecanismo para detectar que el contactor de salida ha quedado **soldado en posición cerrada** tras un evento de sobrecorriente o cortocircuito?

- ¿Realimentación de estado del contactor desde su contacto auxiliar?
- ¿Comparación entre orden de apertura y corriente medida?
- Si no hay detección: ¿qué se documenta para el técnico de instalación?

**Por qué importa**: si el contactor queda soldado, la lógica de "desconexión" del GME no funciona — el equipo conectado queda sin protección sin que nadie se entere. Es un modo de falla silencioso y peligroso.

**Respuesta esperada**:

---

## Bloque D — Trazabilidad de eventos (gate de competitividad vs Wagner / Franklin)

### 🟡 Q4. Profundidad real del log de fallas

La UI muestra **última ocurrencia por cada tipo** (9 tipos: Off Manual, Tercera Sobrecarga, Tercera Subcarga, Arranques/h, Sobrecarga A, Subcarga A, V bajo, V alto, Inestabilidad Hz).

- ¿Existe en el firmware un **buffer circular de eventos cronológicos** con más entradas?
- Si existe: ¿cuántos eventos guarda?
- Si no existe: ¿hay plan en el roadmap de implementarlo? ¿v1 o v2?

**Por qué importa**: ≥6 técnicos en la encuesta abierta pidieron explícitamente "log de eventos / historial de fallas con últimas N fallas". Wagner DSP-1 (competidor LATAM) guarda 25 eventos. Franklin SubMonitor guarda log con fecha/hora. Es el gap funcional más visible vs competidores de precio medio.

**Respuesta esperada**:

---

### 🟡 Q5. RTC (Real Time Clock) y timestamp

- ¿El GME tiene **RTC interno con batería de respaldo**?
- ¿Sincroniza con servidor NTP cuando tiene acceso a internet?
- Si **no** hay RTC: ¿los eventos se registran con tiempo relativo (segundos desde arranque) o sin timestamp?

**Por qué importa**: condición previa para Q4 (log cronológico). Sin RTC no hay timestamp confiable, lo que limita la utilidad del log.

**Respuesta esperada**:

---

## Bloque E — Certificaciones (gate Bruna / mercado externo)

### 🟡 Q12. Estado de certificaciones

Estado **actual** (no proyectado) de cada certificación. Marcar: emitida ✅ / en proceso 🟡 / no aplicada todavía ⚪ / descartada ❌.

| Certificación | Aplicación | Estado | Fecha estimada |
|---|---|---|---|
| **CE + LVD 2014/35/EU** | Mercado europeo |  |  |
| **CE + EMC 2014/30/EU** | Mercado europeo |  |  |
| **RED 2014/53/EU** | WiFi en EU |  |  |
| **IEC 60947-4-1** | Contactor (universal) |  |  |
| **IEC 61000-4-X** | EMC (componentes) |  |  |
| **UL 508** | Mercado norteamericano |  |  |
| **UL 60947-4-1** | Mercado norteamericano armonizado |  |  |
| **FCC Part 15** | WiFi en EE.UU. |  |  |
| **NOM-001-SCFI** | Mercado mexicano |  |  |
| **RETIE** | Mercado colombiano |  |  |

**Adicional**: si el módulo WiFi usado es estándar (ESP32, ESP-WROOM-32 u otro), ¿qué FCC ID / CE certifications hereda automáticamente el producto final?

---

## Bloque F — Roadmap / hardware

### 🟢 Q10. Multivoltaje 120V / 220V

- ¿El hardware actual soporta operación a 120 Vac, o solo a 220 Vac?
- ¿Hay plan de variante 120V para mercado donde la red residencial es 120V (México, parte de Centroamérica, EE.UU.)?
- Si requiere cambio: ¿es variante de PCB completa, o solo cambio de transformador de alimentación + rango del CT de medición?

**Por qué importa**: encuesta capturó la solicitud explícita. Decide si "multivoltaje" puede ser claim diferenciador (auto-rango como Littelfuse 77C: 100–240 V) o si requieren dos SKUs físicos.

**Respuesta esperada**:

---

### 🟢 Q13. NFC — estado en hardware

- ¿El hardware del GME incluye antena / controlador NFC?
- Si **sí**: ¿activado por firmware o requiere desarrollo?
- Si **no**: ¿está en roadmap de hardware futuro o se descartó por costo / complejidad?

**Por qué importa**: OL-3 (Orlan) identificó NFC como tendencia emergente para pairing simplificado. Un técnico HVAC en la encuesta lo propuso explícitamente. Si está en roadmap, es claim a futuro.

**Respuesta esperada**:

---

## Cierre

Una vez recibidas las respuestas:

1. **Vael** activa los claims que estén destrabados (especialmente C — "Sin app, sin cloud" — depende de Q2/Q3).
2. **Bruna** evalúa los riesgos regulatorios y aprueba/rechaza claims con caveats.
3. **Vera** actualiza tabla side-by-side de specs con valores definitivos.
4. **Owner** decide pricing final cruzando Van Westendorp con BOM real.

**Si alguna pregunta no aplica a tu equipo o requiere coordinación con otra área (mecánica, ME, certificaciones externas), márcala así y la routamos correspondientemente.**

---

*Archivo origen del análisis: `_intel/Vera_validacion_tecnica_GME_2026-05-06.md` — sección 5.*
