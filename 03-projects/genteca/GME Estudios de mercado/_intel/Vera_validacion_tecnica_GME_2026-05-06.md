# Memo técnico — Validación técnica GME (Exceline)
**Autor:** Vera — Technical Researcher, Protección Eléctrica (Genteca)
**Fecha:** 2026-05-06
**Para:** Owner / Vael / Bruna / Engineering GME
**Insumos consultados:** OL-3 Orlan (2026-05-06), mockups GME-R220/B220/M220 (18 pantallas), Informe Van Westendorp, búsquedas normativas y de fabricantes (fuentes al cierre)
**Nota de alcance:** Este memo es insumo técnico crudo. No contiene copy publicable ni recomendaciones de pricing. Los claims son evaluaciones técnicas internas para uso de Vael y Bruna — no lenguaje para consumo externo.

---

## Sección 1 — Standards mapping

### 1.1 Árbol normativo aplicable al GME

El GME es un **relé de protección con contactor de salida integrado**, interfaz WiFi y lógica configurable por aplicación. Esa arquitectura lo hace caer bajo tres familias normativas simultáneas, con distintos grados de obligatoriedad según mercado destino.

#### IEC 60947-4-1 — Contactores y arrancadores de motor (Ed. 4.0: 2018; Ed. 5.0: 2023)

**Relevancia:** directa. El GME incluye un contactor de salida que abre y cierra el circuito de la carga. El contactor en sí debe cumplir IEC 60947-4-1 para ser certificado como "arrancador de motor". La norma define:

- **Categorías de utilización:** AC-1 (cargas resistivas/inductivas poco perturbadoras), AC-3 (motores en jaula de ardilla DOL, la más común), AC-4 (motores con inversión, arranque con rotor bloqueado). Para refrigeración/bombas en DOL, AC-3 es la categoría correcta; arranque directo con alta inercia puede requerir AC-4.
- **Clases de disparo (Trip Class):** definen el tiempo máximo de actuación a 7.2 × I_nominal. La norma reconoce: Class 5, 10, 10A, 20, 30.
  - **Class 10:** disparo en ≤ 10 s a 7.2 × In. Estándar para motores de arranque rápido (bombas centrífugas, fans).
  - **Class 10A:** subclase de Class 10 específica para compresores herméticos y semi-herméticos. Permite mayor tiempo de no-disparo en arranque en caliente (hot restart) que Class 10 pura, reconociendo que el compresor parte desde presiones no igualadas y la corriente de arranque es más alta por más tiempo. Relevante directamente para GME-R220.
  - **Class 20:** para motores de alto momento de inercia (compresores de tornillo, molinos). Dispara en ≤ 20 s a 7.2 × In.
  - **Class 30:** maquinaria muy pesada.
- **Requisito de no-disparo en arranque:** la norma exige que el relé no dispare durante el período de arranque legítimo. Para Class 10A, la curva de no-disparo es más permisiva que Class 10 para la zona de 3–6 s / 3–7 × In.
- **Tests obligatorios para certificación:** verificación de la curva de disparo (frío y caliente), categoría de utilización, ensayo de corto circuito coordinado, durabilidad de contactos, IP rating.

**Standard requirement (GME):** Si el GME se certifica bajo IEC 60947-4-1 como "motor starter", el contactor interno debe superar los ensayos de la categoría AC-3 como mínimo. La lógica de disparo de sobrecarga debe ser verificable contra la curva de la Clase declarada.

**Gap identificado:** La UI del GME muestra "Sobrecarga 40 A" como valor de última falla. El tiempo de detección de sobrecarga configurable aparece solo en GME-M220 (imagen4: "Tiempo de detección 1.0 s, Rango 0.1–5 s"). En GME-R220 y GME-B220 este parámetro no es visible en los mockups. [pendiente engineering: ¿cuál es la curva de disparo implementada? ¿Clase 10, 10A o lógica propia?]

#### IEC 60255-1 / IEC 60255-127 — Relés de medida y protección

**Relevancia:** media-alta. El GME mide V, I y Hz para determinar la actuación del contactor. Cuando un dispositivo toma decisiones de protección basadas en medición, cae dentro del alcance conceptual de IEC 60255. La versión 2022 de la norma es la vigente (cancela ed. 2009).

- **Clases de exactitud de medición (IEC 60255-1:2022 §6):**
  - Clase 0.2: error ≤ 0.2% del valor nominal. Instrumentación de laboratorio/facturación.
  - Clase 0.5: error ≤ 0.5%. Medidores de energía precisos (clase típica de relés industriales de calidad como Littelfuse 77C que declara ±1% V y ±1% I).
  - Clase 1: error ≤ 1%. Suficiente para protección. Clase mínima razonable para un dispositivo que activa un contactor basándose en la medición.
  - Clase 3–5: relés de protección sin requisito de precisión en medición (solo importa que actúen en el umbral, no que midan con exactitud).

**Standard requirement (GME):** Para justificar el valor medido que se muestra al usuario en la UI (228 V, 15.6 A, 59.8 Hz), el GME debería declarar una clase de exactitud. Un display de "15.6 A" sin tolerancia documentada es un riesgo de credibilidad técnica. Para protección funcional (dispara o no dispara), Clase 3 es suficiente normativamente. Para display informativo confiable, Clase 1 es el mínimo defendible frente a un técnico exigente.

**Gap identificado:** No hay dato de exactitud de medición en ninguna pantalla del GME. [pendiente engineering: exactitud de medición de V, I y Hz — clase y tolerancia]

#### IEC 61000-4-X — Compatibilidad electromagnética (EMC), inmunidad

**Relevancia:** crítica para dispositivos con WiFi en entornos industriales/comerciales. Un dispositivo que opera en el mismo recinto que motores, variadores y compresores está expuesto a los peores escenarios de EMC. La presencia del módulo WiFi (2.4 GHz) agrega el eje de emisión.

Los tests de inmunidad obligatorios para obtener marcado CE (Directiva EMC 2014/30/EU) en este tipo de equipo son:

| Test | Norma | Nivel típico para equipo industrial | Relevancia para GME |
|---|---|---|---|
| Descarga electrostática (ESD) | IEC 61000-4-2 | Level 3: contacto 6 kV / aire 8 kV | Alta: manejo manual, perillas físicas |
| Inmunidad a campo radiado | IEC 61000-4-3 | Level 3: 10 V/m, 80–1000 MHz | Crítica: WiFi 2.4 GHz puede afectar propio circuito de medición |
| Transitorio rápido / Burst | IEC 61000-4-4 | Level 3: 2 kV en línea de alimentación | Crítica: arranque de motores genera burst |
| Surges (sobretensión transitoria) | IEC 61000-4-5 | Level 3: 1 kV diferencial, 2 kV común | Crítica: fallas de red en Venezuela/Caribe son frecuentes |
| Inmunidad a RF conducida | IEC 61000-4-6 | Level 3: 10 V, 150 kHz–80 MHz | Alta: en instalaciones con variadores VFD |
| Emisiones: EN 55032 Clase B (residencial) o A (industrial) | EN 55032 | Clase A menos restrictiva | GME con WiFi debe pasar test de emisiones |
| Radio Equipment Directive (RED) 2014/53/EU | — | Para el módulo WiFi | Obligatorio para CE en Europa |

**Nota crítica:** Un dispositivo con WiFi 2.4 GHz **no puede obtener marcado CE** solo con la Directiva EMC. Requiere adicionalmente la Directiva RED 2014/53/EU. Para FCC (mercado norteamericano), el módulo WiFi debe estar certificado FCC Part 15 Subpart C (o el fabricante puede usar un módulo ya certificado).

**Standard requirement (GME):** Para mercado LATAM sin requisito regulatorio formal (Venezuela, por ejemplo), los tests de EMC no son legalmente obligatorios. Para Colombia, Caribe (certificación FCC), y exportación a Europa (CE + RED), son gates de entrada.

**Gap identificado:** No se puede confirmar si el módulo WiFi del GME usa un componente ya certificado (ESP32, módulo ESP-WROOM, similar) o solución propia. Si usa ESP32/ESP-WROOM-32 estándar, la certificación FCC del módulo ya existe como base. [pendiente engineering: identificar el módulo WiFi — ¿tiene FCC ID propio? ¿Número de certificación?]

#### UL 508 — Standard for Industrial Control Equipment (norteamericano)

**Relevancia:** media. Requerido para vender en EE.UU. como "industrial control equipment". El GME, si pretende el canal HVAC norteamericano o distribución en el Caribe anglófono, necesita UL 508 Listing para el conjunto (relé + contactor integrado).

- UL 508 cubre: overload relays (relés de sobrecarga), motor controllers, disconnect switches.
- Un dispositivo que integra contactor + lógica de protección + display en un solo enclosure entra bajo "motor controller" en UL 508.
- **Tests must-have UL 508:** ensayo de temperatura, aislamiento dieléctrico, corte bajo carga, resistencia a corto circuito coordinado, marcado.
- Nota: UL 60947-4-1 (versión UL del IEC 60947-4-1) es la ruta de certificación armonizada. Reducción del burden de tests si ya se tiene IEC 60947-4-1.

**Standard requirement (GME):** UL 508 Listing no es requerido para mercado venezolano. Para distribuidor norteamericano (Florida, Texas, Caribe), es el gate de entrada estándar.

#### UL 1053 — Ground Fault Sensing and Relaying Equipment

**Relevancia:** baja para el GME tal como está descrito. UL 1053 aplica cuando el dispositivo tiene función de detección de falla a tierra (ground fault). Las pantallas del GME no muestran esta función. Si en versiones futuras se agrega detección de fuga a tierra, vuelve a ser relevante.

**Veredicto:** No aplica a la versión descrita del GME.

#### NEC / NEMA (norteamericano)

- **NEC Art. 430:** define requisitos de protección de motores en instalaciones eléctricas USA. Exige protección de sobrecarga continua. Un protector como el GME podría calificar como "motor running overload protection" bajo NEC 430.32, pero necesita UL 508 Listing para ser aceptado por inspectores.
- **NEMA ICS 2:** estándar para "Industrial Control and Systems: Controllers, Contactors, and Overload Relays rated not more than 2000 Volts AC." Relevante si se busca distribuir en canal industrial USA.

**Standard requirement (GME):** Para mercado venezolano/LATAM inmediato, ni NEC ni NEMA son requerimientos. Para exportación a EE.UU., son referencias de diseño y UL 508 es el gate práctico.

### 1.2 Resumen de rutas de certificación por mercado

| Mercado | Normativa gate | Estado GME | Prioridad |
|---|---|---|---|
| Venezuela (mercado principal) | No hay organismo de certificación activo exigiendo IEC/UL | [pendiente engineering] | Baja (comercial) — pero riesgo de responsabilidad civil si falla |
| Colombia | RETIE (Reglamento Técnico de Instalaciones Eléctricas) — exige producto certificado IEC o UL en instalaciones reguladas | [pendiente engineering] | Media |
| Caribe anglófono / exportación informal USA | FCC Part 15 (WiFi), UL 508 o equivalente | [pendiente engineering] | Alta si se quiere canal formal |
| Europa (potencial futuro) | CE = Directiva EMC + Directiva RED + (LVD si >50V) | [pendiente engineering] | Alta si se busca exportación |

---

## Sección 2 — Tabla side-by-side specs técnicas

**Nota metodológica:** Los valores del GME provienen exclusivamente de los mockups de UI (fuente primaria interna). Donde hay ambigüedad o ausencia de dato, se marca `[pendiente engineering]`. Los valores de competidores vienen de OL-3 de Orlan, búsquedas web y fuentes citadas al cierre. Datos de competidores marcados `[fuente única]` o `[estimado]` donde aplica.

| Parámetro | **GME-R220** (Refrig.) | **GME-B220** (Bombas) | **GME-M220** (Motores) | Littelfuse 77C | Littelfuse MP8000 | Franklin SubMonitor Connect | ICM492 | ICM493 | Wagner DSP-1 | TOMZN TOMPD 63A | Shelly Pro 1PM | Liyuan C1-S2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Voltaje nominal** | 220 Vac | 220 Vac | 220 Vac | 100–240 Vac | 90–690 Vac | 200–575 Vac (3F) | 80–300 Vac | 195–264 Vac | 90–300 Vac | 80–300 Vac | 100–240 Vac | 220 Vac |
| **Monofásico / 3F** | Monofásico | Monofásico | Monofásico | Monofásico | Mono + 3F | 3F principal; mono via firmware | Monofásico | Monofásico | Monofásico | Monofásico / 2P | Monofásico | Monofásico |
| **Rango corriente nominal** | [pendiente engineering] | [pendiente engineering] | [pendiente engineering] | 2–800 A (CT externo >90 A) | 0.5–1000 A | 24–135 A (varias versiones) | No mide I | No mide I | No mide I | 1–63 A | ≤ 16 A | ≤ ~10 A (2.2 kW / 220V) |
| **Método medición corriente** | [pendiente engineering] | [pendiente engineering] | [pendiente engineering] | CT interno (≤90A) / CT externo | CT interno + externo | CT interno | N/A | N/A | N/A | Shunt / sensor interno | Sensor interno | CT interno |
| **Tipo medición corriente** | [pendiente engineering] | [pendiente engineering] | [pendiente engineering] | RMS verdadero declarado (±1% acc.) | RMS verdadero | RMS [no confirmado en fuente] | N/A | N/A | N/A | No declarado explícitamente | No declarado (W derivado) | No declarado |
| **Exactitud V** | [pendiente engineering] | [pendiente engineering] | [pendiente engineering] | ±0.5% nominal | [pendiente engineering] | [no disponible públicamente] | [no disponible] | True RMS calibrable | No declarado | No declarado | No declarado | No declarado |
| **Exactitud I** | [pendiente engineering] | [pendiente engineering] | [pendiente engineering] | ±1% (directo <100 A) | [pendiente engineering] | [no disponible] | N/A | N/A | N/A | No declarado | No declarado | No declarado |
| **Sampling rate / ADC** | [pendiente engineering] | [pendiente engineering] | [pendiente engineering] | No declarado públicamente | No declarado | No declarado | N/A | N/A | N/A | No declarado | ~100 ms temperatura; I no declarado | No declarado |
| **Tiempo respuesta a sobre/sub voltaje** | [pendiente engineering] | [pendiente engineering] | [pendiente engineering] | 5% + 1 s (spec timing) | [pendiente engineering] | [no disponible] | Ajustable 2 s default | Ajustable | 2 s default (ajustable) | Ajustable (no cuantificado) | No declarado | No declarado |
| **Tiempo respuesta a sobrecarga I** | [pendiente engineering] | GME-M: 0.1–5 s (Tiempo de detección) | 0.1–5 s rango | Dependiente de clase (IEC 60947-4-1 curva) | Dependiente de clase | [no disponible] | N/A | N/A | N/A | No orientado a motor | No orientado a motor | No declarado |
| **Detección de subcarga / dry run** | Sí — 60% I_nom, t=10 s (default R) | Sí — 70% I_nom, t=5 s (default B) | Sí — 60% I_nom, t=5 s (default M) | Sí — underload configurable | Sí — underload | Sí — 75% SFA (default); 30–100% adj. | No | No | No | No — overload sí; underload no | No — overpower sí; underload no | Sí (sensor-free) |
| **Detección pico arranque diferenciado** | [pendiente engineering] | [pendiente engineering] | [pendiente engineering] | Sí — start inhibit period | Sí | Sí | No | No | No | No | No | [no declarado] |
| **Protección de arranques máx/hora** | Toggle (desactivado en R default) | Toggle (desactivado en B default) | Toggle (desactivado en M default) | Sí — max starts/hour configurable | Sí | [no confirmado] | No | No | No | No | No | No |
| **Medición de frecuencia** | Sí — 59.8 Hz en UI | Sí | Sí | No declarado | No declarado | No declarado | No | No | No | 50/60 Hz fijo | No declarado | No |
| **Protección activa por frecuencia** | UI muestra "Inestabilidad: 54 Hz" en fallas [pendiente: ¿activa o diagnóstica?] | Igual | Igual | No declarado | No declarado | No declarado | No | No | No | No | No | No |
| **Profundidad log de fallas** | Última ocurrencia por tipo (9 tipos) — sin timestamp cronológico | Igual | Igual | Últimas 4 fallas + timestamp (con comms) | [pendiente engineering] | Log con fecha/hora (FE Connect app) | No log | 5 eventos (no timestamp) | 25 eventos (sin timestamp confirmado) | [no disponible] | No declarado | 5 registros |
| **RTC / timestamp real** | [pendiente engineering] | [pendiente engineering] | [pendiente engineering] | Sí (con módulo de comms) | [pendiente engineering] | Sí | No | No | No | No | Sí (sincroniza con NTP vía red) | No |
| **Conectividad** | WiFi local (webserver 192.168.0.21) | WiFi local | WiFi local | RS-485 / Modbus (módulo externo) | Bluetooth + Ethernet Modbus TCP | Bluetooth (FE Connect app) | Ninguna | Ninguna | Ninguna | WiFi 2.4G (Tuya/Smart Life cloud) | WiFi + LAN + BT | Ninguna |
| **App requerida** | No — browser nativo | No — browser nativo | No — browser nativo | PC software (RS-485) | App iOS/Android Littelfuse | App iOS/Android FE Connect | No | No | No | Sí — Smart Life / Tuya (cloud) | Opcional — API abierta | No |
| **Dependencia cloud** | [pendiente engineering — crítico] | Igual | Igual | No — standalone | No — standalone | Bluetooth local (sin cloud para control) | No | No | No | Sí — funcionalidad plena requiere cloud Tuya | No — API local disponible | No |
| **Configurabilidad por aplicación (R/B/M)** | Sí — radio selector R/B/M | Sí | Sí | No — genérico | No | No — solo bombas | No | No | No | No | No | No — solo bombas |
| **Etiquetado equipo + GPS** | Sí (UI Pantalla 1: nombre + pin) | Sí | Sí | No | No | No (nombre en app) | No | No | No | No | No (nombre posible) | No |
| **Certificaciones declaradas** | [pendiente engineering] | Igual | Igual | UL 508, UL 1053, UL 60947, CE, CSA, FCC | IEC 60947-1, UL 1053, UL 60947, CE, CSA, FCC | [no confirmado públicamente] | UL Listed | UL Listed (NEMA 3R enclosure) | [no confirmado] | CE | CE (EU DoC 2025) | CE + ISO 9001 (fabricante declara) |
| **Precio público referencia** | ~$35 target (OPP Van Westendorp) | Igual (hardware común) | Igual | ~$552 USD (distribuidor) | ~$806 USD (distribuidor) / MSRP ~$1,305 | No público (alto) | ~$50–80 USD est. | No público (incluye contactor 40A) | ~$40–60 USD est. regional LATAM | ~$35–50 USD (Amazon/AliExpress) | ~$35–45 USD (Shelly store) | ~$18–22 USD OEM |

**Observaciones críticas de la tabla:**

1. **El rango nominal de corriente del GME es el gap técnico más urgente.** Los mockups muestran 15.5 A como corriente nominal en Ajustes Físicos y 40 A en el reporte de última falla de sobrecarga. Esto sugiere que el contactor tiene capacidad al menos hasta 40 A pero no confirma si es el máximo de operación normal o solo el valor registrado en la falla mostrada en el ejemplo. Sin saber el FLA máximo, la tabla comparativa no puede completarse y los claims de "aplicable a motores hasta X HP" son imposibles.

2. **El tiempo de respuesta del GME a sobrevoltaje/subvoltaje no está declarado en la UI.** El técnico de refrigeración que señaló sensibilidad <1 s tiene razón en preguntarlo — este dato es operativamente relevante para decidir si el GME protege contra fluctuaciones rápidas (p.ej. arranque de otro equipo en la misma fase).

3. **El método de medición de corriente (CT interno, CT externo, shunt) no es visible en los mockups.** Determina directamente la exactitud de la medición y el rango máximo sin accesorios adicionales.

4. **TOMZN TOMPD y Shelly Pro 1PM son el benchmark real de funciones básicas a ese precio.** Sin protecciones de motor, pero con V+I+WiFi. La superioridad del GME es la capa de protección motor-específica (subcarga, arranques/hora, modos R/B/M), no la medición en sí.

---

## Sección 3 — Diferenciación técnica entre modos R / B / M

### 3.1 Análisis de qué cambia entre modos (basado en pantallas)

Comparando los ajustes digitales de los tres modos directamente desde las pantallas:

| Parámetro | GME-R220 (Refrigeración) | GME-B220 (Bombas) | GME-M220 (Motores) |
|---|---|---|---|
| Tiempo de Conexión (reconexión tras falla) | 300 s (rango 180–600 s) | 120 s (rango 5–300 s) | 60 s (rango 5–300 s) |
| Activación de subcarga | Sí (activado por default) | Sí (activado por default) | Sí (activado por default) |
| % de Subcarga | 60% | 70% | 60% |
| Tiempo de detección de subcarga | 10 s | 5 s | 5 s |
| Tiempo para el reintento | 240 s | 20 min | 240 s |
| Protección arranques máx/hora | Toggle (desactivado default) | Toggle (desactivado default) | Toggle (desactivado default) |
| Maniobra diaria | No visible en R | Visible y activada en B | No visible en M |
| Tiempo de detección (sobrecarga) | No visible en R/B mockup | No visible en B mockup | 1.0 s (rango 0.1–5 s) |
| Umbral subcarga I< | 9.30 A | 10.85 A | 9.30 A |

**Hallazgo central para el claim E:** Los tres modos cambian principalmente **valores default**, no lógica de protección diferente. La arquitectura es: un motor de protección único con parámetros que se precargan según la aplicación seleccionada. Esto es **correcto y válido**, pero tiene implicaciones para el claim.

### 3.2 ¿Qué debería hacer técnicamente cada modo? — Comparación con práctica del segmento

#### Modo Refrigeración (GME-R220)

**Fundamento técnico del segmento:**

Los compresores herméticos y semi-herméticos (Copeland Scroll, Danfoss TL, Tecumseh AE) tienen requisitos específicos derivados de la mecánica del ciclo de refrigeración:

- **Tiempo de reconexión largo:** tras un disparo, las presiones de alta y baja deben igualarse antes del rearranque. Tiempo típico recomendado por fabricantes: 3–5 minutos (180–300 s). Copeland recomienda mínimo 3 min entre intentos de arranque para permitir igualación de presiones en sus scrolls. El tiempo de 240–300 s del GME-R220 es **correcto y alineado con la práctica del segmento** (Copeland Application Engineering Bulletin AE4-1365).
- **Prioridad subcarga:** un compresor que pierde carga de refrigerante opera con corriente baja (subcarga), señal de pérdida de carga o falla de válvula. La detección de subcarga en refrigeración es el mecanismo de protección más importante después del voltaje. El GME-R220 activa subcarga por default a 60% con t=10 s — razonable, aunque algunos compresores requieren confirmación más rápida.
- **Clase de disparo para compresores herméticos:** Class 10A (IEC 60947-4-1). Esta clase es la que reconoce el arranque en caliente del compresor y su corriente de arranque elevada-y-sostenida. [pendiente engineering: ¿el GME-R220 implementa una curva equivalente a Class 10A para la lógica de sobrecarga?]

**Diferenciación visible en GME-R220 vs otros modos:**
- Tiempo de reconexión más largo (300 s vs 60–120 s) — correcto.
- Tiempo de detección de subcarga más largo (10 s vs 5 s) — conservador y correcto: en refrigeración hay transitorios de baja corriente durante el ciclo de descarga que no deben provocar falsos trips.
- Threshold subcarga más bajo (9.30 A vs 10.85 A en bombas) — menor sensibilidad relativa.

**Gap técnico en modo R:** No se observa en los mockups una lógica específica de "pump-down protection" (protección de cierre de válvula de solenoide antes de stop) ni de temperatura de descarga. Esto es avanzado y no esperado en este rango de precio, pero vale señalarlo.

#### Modo Bombas (GME-B220)

**Fundamento técnico del segmento:**

Las bombas sumergibles y centrífugas tienen el modo de falla más peligroso en operación en seco (dry run): la bomba opera sin líquido, la corriente cae significativamente (no hay carga hidráulica), y el impulsor/cojinetes se dañan en segundos/minutos.

- **Detección rápida de subcarga:** la práctica del segmento (Franklin SubMonitor: default 75% SFA, t=varios segundos; Pumptec: detección en <1 ciclo en algunos modelos) prioriza velocidad de detección de dry run. El GME-B220 usa 70% y t=5 s — más agresivo que GME-R220, lo cual es correcto.
- **Threshold subcarga más alto (10.85 A vs 9.30 A):** en bombas, la corriente sin carga hidráulica es más distintiva de la corriente normal, por lo que el threshold relativo puede ser más alto.
- **Tiempo de reintento largo (20 min):** en bombas sumergibles, si la detección de dry run ocurrió porque el pozo se vació, el tiempo de recuperación del nivel freático puede ser de decenas de minutos. Franklin SubMonitor permite 10–120 min de pausa, default 30 min. El GME-B220 usa 20 min — dentro del rango práctico.
- **Maniobra diaria:** el GME-B220 muestra este toggle (activado por default). Este parámetro no aparece en R ni M. **Esto SÍ es una diferencia de lógica, no solo de valores.** La "maniobra diaria" implica un ciclo de test o arranque programado — práctica común en bombas de agua potable para verificar disponibilidad. Es el único indicador visible de lógica diferente entre modos.
- **Anti-short-cycle:** el tiempo de conexión corto (120 s con rango 5–300 s) en modo bomba sugiere recuperación más rápida — consistente con arranques frecuentes en sistemas de presurización.

**Gap técnico en modo B:** No se observa protección de "high-cycle lockout" explícita (aunque el toggle de "arranques por hora" existe). En bombas de alta ciclicidad (sistemas hidroneumáticos), el limite de arranques/hora es crítico para la durabilidad del bobinado y del contactor.

#### Modo Motores (GME-M220)

**Fundamento técnico del segmento:**

Motores en general (fans, trituradoras, compresores de aire, transportadores) tienen el riesgo primario de rotor trancado (locked rotor): corriente de 5–7 × In sostenida que daña el bobinado en segundos.

- **Tiempo de detección rápido (0.1–5 s):** El parámetro "Tiempo de detección" visible solo en GME-M220 es fundamental. Un rotor trancado a 7 × In durante más de la curva de Class 10 daña el motor. Con t=1 s default, el GME-M220 puede actuar dentro del período crítico. Esto es **la diferencia de lógica más importante** del modo M frente a R y B.
- **Tiempo de reconexión corto (60 s default):** motores en general pueden reintentar arrancar más rápido que compresores.
- **Clase de disparo implicada:** con tiempo de detección ajustable 0.1–5 s y sobrecarga, la lógica se acerca a Class 10 o Class 10A. [pendiente engineering: confirmar]

**Síntesis para el claim E:**

Los tres modos tienen **diferencias reales** en al menos tres dimensiones:
1. **Valores default distintos** en todos los parámetros de tiempo y umbral — esto solo ya justifica el claim de "configurado para cada aplicación".
2. **Lógica de maniobra diaria** presente solo en modo B — esta SÍ es diferencia de lógica.
3. **Tiempo de detección de sobrecarga** visible en modo M (0.1–5 s) pero no en R/B — puede ser que en R/B esté oculto o fijo. [pendiente engineering: confirmar si el tiempo de detección de sobrecarga es configurable en todos los modos o solo en M]

**Riesgo de debilitamiento del claim E:** Si el firmware revela que los modos R/B/M solo cambian valores default y el código de protección es idéntico, el claim "tres modos" es verdad comercial pero reducida en profundidad técnica. Si maniobra diaria y tiempo de detección son funciones exclusivas de sus modos respectivos, el claim tiene sustancia técnica sólida.

---

## Sección 4 — Evaluación técnica de los 5 claims candidatos

### Metodología de dictamen

Cuatro fuentes distintas en cada evaluación:
- **Standard requirement:** lo que la norma exige (normativo, objetivo)
- **Typical practice:** lo que el segmento hace (descriptivo, informativo)
- **GME claim / UI evidence:** lo que las pantallas muestran (verificable en mockup)
- **GME unknown:** lo que no puede conocerse sin ver firmware/hardware real

---

#### Claim A — "Primer protector monofásico V+I+WiFi <$X"

| | |
|---|---|
| **Categoría** | Claim de mercado, no técnico |
| **Veredicto Vera** | Fuera de scope — es pregunta de mercado que corresponde a Orlan. OL-3 ya emitió su veredicto: "defendible con caveat" regional/precio. No la retomo aquí. |
| **Condición técnica** | El claim solo es técnicamente válido si las funciones V+I+WiFi están implementadas y funcionan correctamente. Las pantallas lo muestran, pero la implementación en firmware de producción es [pendiente engineering]. |

---

#### Claim B — "Protección integral: V + I + subcarga + arranques/hora"

| | |
|---|---|
| **Veredicto Vera** | **Técnicamente plausible, con condiciones** |
| **Standard requirement** | No hay norma que defina qué funciones mínimas constituye "protección integral". El término es descriptivo, no normativo. |
| **Typical practice** | La combinación V+I+subcarga+arranques/hora existe en protectores industriales (Littelfuse 77C, MP8000). Es un conjunto reconocido por el segmento como "protección completa de motor". |
| **GME UI evidence** | Las pantallas muestran todos los elementos: U>/U< (V), I>/I< (I), activación de subcarga + % + tiempo de detección (subcarga), toggle de arranques máx/hora. Los 9 tipos de falla en el reporte cubren todas las funciones declaradas. |
| **GME unknown** | (1) ¿La lógica de sobrecarga activa el contactor basándose en I medida en tiempo real, o solo en umbral fijo? (2) ¿El contador de arranques/hora es por hora rodante (sliding window) o por hora calendario? La diferencia importa. (3) ¿La subcarga dispara el contactor tras t=10 s de corriente continua por debajo del threshold, o aplica algún filtrado adicional? |
| **Condición técnica** | El equipo de firmware debe confirmar que cada función activa físicamente el contactor y no solo registra el evento. Una UI que muestra "tercera falla de subcarga" sin probar que la tercera ocurrencia realmente bloquea el equipo no sostiene el claim. |
| **Riesgo técnico elevado** | El log de fallas muestra "Off Tercera falla de Sobrecarga" y "Off Tercera falla de Subcarga" — esto implica que el equipo tolera dos fallas antes de bloquear. Esta lógica de "tres intentos" debe estar explícita en la comunicación: el GME no es un "trip al primer evento" sino un sistema con tolerancia de reintentos. Para compresores de refrigeración que ya tuvieron dos arranques fallidos, un tercer intento puede ser destructivo. [Esta lógica necesita revisión con el equipo de producto antes de comunicar.] |

---

#### Claim C — "Sin app que instalar, sin cloud requerida"

| | |
|---|---|
| **Veredicto Vera** | **Técnicamente plausible para la interfaz — condición crítica pendiente para la protección** |
| **Standard requirement** | No normativo. Es un claim de arquitectura. |
| **Typical practice** | Los mejores protectores standalone (77C, ICM493) operan completamente offline. Los smart devices IoT (Tuya, Shelly dependiendo de config) tienen distintos grados de dependencia cloud. |
| **GME UI evidence** | La URL 192.168.0.21 es una IP local de clase C (red privada). Un dispositivo que sirve una UI en su propia IP local no requiere cloud para la interfaz de usuario. La configuración y el monitoreo son locales. |
| **GME unknown** | **Este es el gap más crítico del memo.** La pregunta es: ¿si el WiFi cae (o si nunca se conecta el dispositivo a una red WiFi), el GME sigue midiendo y actuando el contactor? Si la respuesta es no — si la lógica de protección requiere que el MCU del webserver esté activo y conectado a red — el claim "sin cloud" pasa a ser "sin cloud pero con WiFi obligatorio". Para la mayoría de los técnicos esto es aceptable, pero para instalaciones sin WiFi disponible (sala de máquinas remota, pozo de bomba rural) es un gap real. |
| **Riesgo de arquitectura** | Si el MCU de protección y el MCU del webserver son el mismo chip, un cuelgue del webserver (por stack overflow, bug, ataque de red) podría dejar la protección inactiva. Este es el riesgo de arquitectura que más preocupa técnicamente. La pregunta directa al equipo de firmware está en §5. |
| **Condición técnica** | El claim "sin cloud requerida" es defendible si: (a) la protección activa funciona sin red WiFi, y (b) el procesamiento de protección no comparte runtime con el webserver en el mismo hilo/tarea crítica. |

---

#### Claim D — "Diagnóstico desde el teléfono"

| | |
|---|---|
| **Veredicto Vera** | **Técnicamente defendible — con alcance acotado a red local** |
| **Standard requirement** | No normativo. |
| **Typical practice** | El diagnóstico local (en red WiFi del sitio) es el caso de uso esperado en esta categoría. El diagnóstico remoto (desde fuera del sitio) requiere VPN, port forwarding, o relay cloud — ninguno está confirmado en el GME. |
| **GME UI evidence** | La pantalla de mediciones muestra V, I, Hz, estado del relé, entrada digital, y última falla. Esto es suficiente para diagnóstico funcional básico desde cualquier browser en la misma red WiFi. |
| **GME unknown** | ¿Existe algún mecanismo de acceso remoto (notificación push, relay cloud, MQTT)? Las pantallas no lo muestran. |
| **Condición técnica** | El claim es verdad en red local. Si se usa lenguaje como "desde tu teléfono" sin aclarar "en la misma red", se abre a interpretación de acceso remoto. Vael debe acotar el claim a "en la misma red WiFi" o confirmar si hay acceso remoto planeado. |

---

#### Claim E — "Tres modos en un protector: Refrigeración, Bombas, Motores"

| | |
|---|---|
| **Veredicto Vera** | **Técnicamente defendible, con matiz** |
| **Standard requirement** | No hay norma que defina qué constituye un "modo" de protección diferente. El claim es descriptivo de una funcionalidad de producto. |
| **Typical practice** | No existe en el mercado a este precio un protector configurable por aplicación. El claim es genuinamente diferenciador. |
| **GME UI evidence** | La Pantalla de Configuración muestra el radio selector Motores / Bombas / Refrigeración. Los ajustes digitales son visiblemente distintos entre los tres modos (ver §3). La "maniobra diaria" en modo Bombas sugiere que hay al menos una función de lógica exclusiva de ese modo. |
| **Condición técnica** | El claim es más fuerte si el firmware confirma que: (a) la maniobra diaria es lógica exclusiva del modo B, (b) el tiempo de detección de sobrecarga es configurable independientemente en cada modo, (c) el rearranque tras subcarga tiene comportamiento diferente (con recuperación de nivel en B vs igualación de presiones en R). Si solo cambian defaults, el claim sigue siendo verdad funcional pero el dictamen debe decir "configura parámetros, no cambia lógica". |
| **Riesgo técnico** | El riesgo no es la veracidad del claim sino su debilidad si un técnico exigente pregunta "¿qué cambia exactamente en el firmware entre modos?". Si la respuesta es "los defaults", el técnico puede quedar insatisfecho. |

### Resumen de dictámenes

| Claim | Veredicto Vera | Condición técnica requerida |
|---|---|---|
| A — "Primero monofásico V+I+WiFi <$X" | Fuera de scope técnico (Orlan) | Confirmar implementación en firmware de producción |
| **B — "Protección integral V+I+subcarga+arranques/h"** | Plausible con condiciones | Confirmar que cada función activa el contactor (no solo log). Revisar lógica "tercera falla" con equipo producto. |
| **C — "Sin app, sin cloud"** | Plausible con condición crítica | Confirmar que protección activa opera sin WiFi. Confirmar separación MCU protección vs webserver. |
| D — "Diagnóstico desde el teléfono" | Defendible — acotar a red local | Especificar alcance "misma red WiFi" |
| **E — "Tres modos en un protector"** | Defendible, con matiz | Confirmar si maniobra diaria y tiempo detección sobrecarga son lógica exclusiva por modo o solo defaults |

---

## Sección 5 — Preguntas estructuradas para el equipo de engineering / firmware GME

Lista cerrada numerada. El Owner puede enviar al equipo de desarrollo directamente.

**1. Sampling rate del ADC de medición:**
¿A qué frecuencia muestrea el ADC los valores de voltaje y corriente? ¿Cuántas muestras por ciclo de 60 Hz? ¿Hay filtro de media móvil, RMS ventana, u otro procesamiento antes de la pantalla y antes del umbral de disparo? Esto define si la protección puede responder a fluctuaciones <1 s (solicitado por técnico de refrigeración en encuesta).

**2. Operación offline (WiFi caído):**
¿El GME protege activamente (actúa el contactor) si no hay ninguna red WiFi activa? ¿La lógica de protección es independiente del webserver WiFi? Esto es el gate del claim C. Si la respuesta es no, es un gap de arquitectura crítico que debe resolverse antes del lanzamiento.

**3. Arquitectura MCU — separación protección / webserver:**
¿El procesamiento de la lógica de protección y el servidor web HTTP corren en el mismo microcontrolador o en unidades separadas? ¿Hay watchdog dedicado para la función de protección independiente del sistema operativo del webserver? ¿Un cuelgue del webserver puede inhibir la protección?

**4. Profundidad real del log de fallas:**
La UI muestra la última ocurrencia por cada tipo (9 tipos). ¿Existe en el firmware un buffer circular de eventos cronológicos con más entradas? ¿Hay plan de implementar log de N eventos con timestamp? (Franklin SubMonitor y Wagner DSP-1 guardan 25–indefinido eventos con fecha/hora — este es el gap funcional más visible frente a competidores de precio medio).

**5. RTC (Real Time Clock) y timestamp:**
¿El GME tiene un RTC interno con batería de respaldo? ¿Sincroniza con servidor NTP cuando tiene acceso a internet? Si no hay RTC, ¿los eventos se registran con timestamp relativo (segundos desde arranque) o sin timestamp?

**6. Contactor soldado (welded contact):**
¿El GME tiene algún mecanismo para detectar que el contactor de salida ha quedado soldado (welded) en posición cerrada tras un evento de sobrecorriente o cortocircuito? Si el contactor queda soldado, la lógica de "desconexión" del GME no funciona. ¿Hay detección de realimentación de estado del contactor?

**7. Clase de disparo IEC para la lógica de sobrecarga:**
¿El GME implementa una curva de disparo compatible con IEC 60947-4-1 Class 10, 10A, 20 o 30? ¿O es una lógica propia de umbral fijo + temporizador? Para refrigeración (Class 10A) y motores generales (Class 10), las curvas son distintas — confirmar si el firmware diferencia esto entre modos.

**8. Rango de medición de corriente:**
¿Cuál es el rango operativo nominal del circuito de medición de corriente? Especificar: mínimo confiable (en A), máximo sin saturación (en A), y exactitud declarada (±% de full scale o ±% de lectura). ¿El rango es el mismo para los tres modelos R/B/M o hay variantes de hardware?

**9. Corriente máxima del contactor:**
¿Cuál es la corriente máxima conmutable del contactor integrado? ¿En AC-3 (motor en marcha normal)? ¿En AC-4 (arranque con rotor bloqueado)? La pantalla de reporte muestra "Sobrecarga 40 A" como valor de última falla — ¿40 A es el límite del contactor o solo un valor de ejemplo en el mockup?

**10. Multivoltaje 120V/220V:**
¿El hardware actual soporta operación a 120 Vac o solo a 220 Vac? ¿Hay plan de variante 120V para el mercado donde la red residencial es 120V? La encuesta capturó esta solicitud de forma explícita. Si el hardware requiere cambio para 120V (transformador de alimentación, rango del CT de medición), esto define si es una variante de PCB o solo firmware.

**11. Detección de pico de arranque diferenciado de régimen:**
¿El firmware implementa una ventana de inhibición de disparo durante el arranque (análoga al "starting inhibit" del Littelfuse 77C) que tolera corriente >I_nominal durante los primeros N segundos? Si no, el GME podría disparar falsamente durante arranque de motores de alta inercia o compresores fríos. El técnico de la encuesta señaló esto como requerimiento.

**12. Estado de certificaciones:**
¿Cuál es el estado actual de: (a) CE + RED (para WiFi), (b) IEC 60947-4-1 (para el contactor), (c) IEC 61000-4-X (para EMC), (d) UL 508 (para mercado norteamericano)? ¿Emitidas, en proceso, no aplicadas todavía, o descartadas? Este dato es gate para exportación y es requerido por Bruna para la evaluación de riesgo de claims.

**13. NFC — estado en hardware:**
El OL-3 de Orlan mencionó NFC como señal de tendencia en el segmento. ¿El hardware del GME incluye antena / controlador NFC, está en roadmap de hardware futuro, o se descartó?

**14. Protección de frecuencia — activa o diagnóstica:**
La pantalla de fallas muestra "Inestabilidad: 54 Hz". ¿Esta detección activa el corte del contactor? ¿Cuáles son los umbrales de frecuencia configurados (Hz mín / Hz máx) y el tiempo de detección? En mercados con red eléctrica inestable (Venezuela, partes del Caribe), la protección de frecuencia es diferenciador real si es activa.

**15. Lógica "tres intentos" para subcarga y sobrecarga:**
El log de fallas muestra "Off Tercera falla de Sobrecarga" y "Off Tercera falla de Subcarga". ¿El firmware hace tres intentos de rearranque antes de bloquear definitivamente? ¿Cuándo se resetea el contador de intentos? ¿Se puede configurar el número de intentos? Este comportamiento debe ser comunicado explícitamente en la documentación de producto — un técnico que no lo sabe podría no entender por qué el equipo no se desconectó al primer evento de subcarga.

---

## Supuestos y límites

**Supuesto 1:** Las 18 pantallas de mockup (6 por variante) representan la funcionalidad real del firmware en estado avanzado de desarrollo, no pantallas conceptuales sin código atrás. Si son conceptos, los claims de diferenciación no pueden evaluarse hasta ver el firmware.

**Supuesto 2:** El hardware es el mismo para los tres variantes (R220 / B220 / M220), con diferenciación solo por firmware y etiqueta. La UI es idéntica en estructura; solo cambian los valores y el color del badge (azul R220, azul B220, gris M220). Este supuesto es consistente con el planteamiento del Van Westendorp (Escenario A).

**Supuesto 3:** El valor "15.5 A" en la pantalla de Ajustes Físicos (Corriente Nominal) del GME-R220 es un valor de configuración del ejemplo, no el FLA máximo del producto. La corriente nominal ajustable por perilla física define el punto de trabajo del usuario, no el límite del hardware.

**Supuesto 4:** El contactor integrado tiene capacidad al menos equivalente al valor de "Sobrecarga 40 A" mostrado en el Reporte de Fallas. Este valor puede ser el de la última falla registrada en el mockup y no el límite de producto.

**Límite 1:** No se tuvo acceso al datasheet oficial del Littelfuse 77C (403 en el servidor del fabricante). Los datos de accuracy (±1% V, ±1% I) provienen de distribuidores verificados. Si el datasheet oficial difiere, la tabla §2 debe actualizarse.

**Límite 2:** Los modos de falla relacionados con el contactor (soldadura de contactos, degradación por ciclado) no pueden evaluarse sin datos del fabricante del contactor integrado. Este límite afecta la pregunta Q6 del §5.

**Límite 3:** La evaluación de exposición a la patente US 20240332944 es preliminar. La patente cubre dispositivos con tres entradas trifásicas que operan en modo motor o modo circuit breaker. La arquitectura del GME (monofásico, con tres modos de aplicación distintos, no motor vs. breaker) es materialmente diferente. No hay evidencia de solapamiento directo en la reivindicación principal, pero se requiere revisión por abogado de propiedad intelectual si el GME busca exportación a EE.UU.

**Límite 4:** Los valores de tiempo de respuesta del GME a sobre/sub voltaje no están visibles en ninguna pantalla. Toda la sección de respuesta temporal está marcada [pendiente engineering]. Este es el gap técnico más urgente para la tabla side-by-side.

---

## Próximos pasos

### Le toca al equipo de firmware / engineering GME

Responder las 15 preguntas del §5. La prioridad alta es: Q2 (operación offline), Q3 (arquitectura MCU), Q7 (clase de disparo), Q8-Q9 (rangos de corriente), Q11 (inhibición de arranque), Q14 (protección frecuencia activa o no), Q15 (lógica de tres intentos).

Sin estas respuestas, los claims B, C y E no pueden considerarse técnicamente validados para uso comercial. El Owner debería pedir al equipo una respuesta en formato tabla dentro del sprint actual.

### Le toca a Vael

1. **Claim C y Claim E** son los más listos para trabajar — sujetos a confirmación de Q2 para C, y Q3/Q7 para E. Vael puede preparar la arquitectura de mensaje con caveat interno "sujeto a confirmación de firmware" y activarlos cuando lleguen las respuestas de engineering.
2. **Claim D** puede usarse ya, acotando explícitamente "desde tu teléfono mientras estés en la misma red WiFi". No requiere más confirmación técnica para esa versión del claim.
3. **Claim B** requiere que antes de usarlo se resuelva la pregunta sobre la lógica "tres intentos antes de bloquear". Si esa lógica es real, debe comunicarse como feature ("reintentos inteligentes antes del bloqueo de seguridad") no ocultarla — un técnico que la descubra sin haberla entendido generará objeción.
4. El hallazgo de §3 sobre modos R/B/M: si engineering confirma que maniobra diaria (modo B) y tiempo de detección de sobrecarga (modo M) son lógica exclusiva por modo, Vael tiene sustancia técnica para el claim E con profundidad. Si solo son defaults, el claim sigue siendo verdad pero más débil — Vael debe ajustar el nivel de la afirmación.

### Le toca a Bruna

1. **Certificaciones (Q12):** Este es el riesgo regulatorio primario. Si el GME no tiene CE ni UL ni IEC 60947-4-1 al momento del lanzamiento, cualquier claim que implique "calidad industrial" o "protección certificada" es expuesto. Bruna debe establecer qué lenguaje de calidad puede usarse sin certificación formal — y qué queda bloqueado hasta que la certificación esté emitida.
2. **Claim B:** La lógica "tercera falla" es un riesgo de responsabilidad. Si un compresor sufre daño durante el segundo intento fallido de rearranque y el usuario no sabía que el GME reintentaba, hay exposición. El manual debe ser explícito. Bruna debe revisar si el claim "protección integral" implica trip en primer evento o no.
3. **Claim A ("primero"):** Bruna ya fue alertada por Orlan. Vera confirma: no usar este claim en ningún canal hasta que Orlan complete la investigación de mercado chino OEM (Señal de OL-3 §6) y Bruna establezca el scope geográfico exacto del claim.
4. **Módulo WiFi:** Si el GME usa un módulo WiFi (ESP32 o similar) que ya tiene FCC ID, el camino a certificación parcial es más corto. Bruna debe verificar qué certificaciones del componente son heredables por el producto final y cuáles requieren tests a nivel sistema.

### Le toca a Orlan en fase 2 del OL-3

1. **Mercado chino OEM profundo:** La búsqueda en AliExpress/Alibaba con términos "single phase motor protector WiFi underload dry run 220V" fue superficial en OL-3 (límite explícito en sus supuestos). Esta es la amenaza competitiva más probable al claim A. Una sesión de búsqueda directa en AliExpress en español (términos: "protector motor monofasico subcarga WiFi 220V") y en chino simplificado podría revelar si existe un OEM sin marca a $20–30 con estas funciones.
2. **PrevenIng (Paraguay):** Pendiente de verificación desde OL-3. Si mide corriente, cambia el mapa competitivo en LATAM.
3. **Pricing ICM493 en Venezuela:** Dato pendiente para completar la columna de precio de la tabla §2.

---

## Sources

| # | Fuente | URL / Referencia | Acceso | Confianza |
|---|---|---|---|---|
| S1 | OL-3 Orlan — Innovation Radar GME 2026-05-06 | `C:\RAUL\03-projects\genteca\GME Estudios de mercado\_intel\OL-3_GME_innovation_radar_2026-05-06.md` | Directo | Confirmed (interna) |
| S2 | Mockups GME-R220 (6 pantallas) | `C:\RAUL\03-projects\genteca\GME Estudios de mercado\_img_R\` | Directo | Confirmed (fuente primaria) |
| S3 | Mockups GME-B220 (6 pantallas) | `C:\RAUL\03-projects\genteca\GME Estudios de mercado\_img_B\` | Directo | Confirmed (fuente primaria) |
| S4 | Mockups GME-M220 (6 pantallas) | `C:\RAUL\03-projects\genteca\GME Estudios de mercado\_img_M\` | Directo | Confirmed (fuente primaria) |
| S5 | Informe Van Westendorp GME | `C:\RAUL\03-projects\genteca\GME Estudios de mercado\Informe_Van_Westendorp.md` | Directo | Confirmed (interna) |
| S6 | IEC 60947-4-1 — Contactors and motor starters (Ed. 4:2018, Ed. 5:2023) | https://webstore.iec.ch/en/publication/74487 | Web (paywall — abstract accedido) | Confirmed (norma vigente) |
| S7 | IEC 60255-1:2022 — Measuring relays and protection equipment | https://webstore.iec.ch/en/publication/59762 | Web (paywall — abstract accedido) | Confirmed (norma vigente) |
| S8 | Trip Class description — Schneider Electric TeSys GV5/GV6 | https://www.productinfo.schneider-electric.com/gv5pbgv6pbdocumentation/doca0161-tesys-gv5pb-gv6pb-user-guide | Web | Confirmed |
| S9 | Trip Class guide — VIOX Electric | https://viox.com/what-is-trip-class-motor-protection-guide/ | Web | Probable |
| S10 | UL 508 — Standard for Industrial Control Equipment | https://standardscatalog.ul.com/standards/en/standard_508_18 | Web (abstract) | Confirmed |
| S11 | UL 508A summary — UL Solutions | https://www.ul.com/resources/ul-508a-third-edition-summary-requirements | Web | Confirmed |
| S12 | Littelfuse 77C — accuracy ±1% I, ±0.5% V, timing 5%+1s | https://www.littelfuse.com/products/relays-contactors-transformers/protection-relays/motor-pump-protection/77c/77c | Web (página producto, 403 en install guide) | Probable |
| S13 | Littelfuse 77C installation manual (PDF 403) | https://www.littelfuse.com/assetdocs/77c-b-pdf-installation-instructions | Web — 403 bloqueado | Bloqueado — ver Protocolo Paxs para acceso |
| S14 | Franklin SubMonitor — underload default 75% SFA, 30 min restart | https://franklinaid.wordpress.com/2012/10/26/submonitor-overunderload-detection/ | Web | Probable |
| S15 | ICM493 — 5 fault events, UL Listed, 195–264 Vac | https://www.icmcontrols.com/product/icm493/ | Web (fabricante) | Confirmed |
| S16 | ICM493 installation manual PDF | https://econtent.adhq.com/dam/Original/10000/ICM_Controls_ICM493_Installation_Manual.pdf | Web | Confirmed |
| S17 | Wagner DSP-1 — 25 fault events, 2 s response default, 90–300 V | https://www.eproteca.com/wp-content/uploads/Manual-usuario-DSP1-WAGNER-EPROTECA.pdf | Web (PDF — encoding issues al leer, datos confirmados por búsqueda) | Probable |
| S18 | TOMZN TOMPD — CE, voltage 80–300V, 63A, WiFi Tuya, no underload | https://www.tomznelectric.com/product-tomzn-63a-80a-wifi-smart-energy-meter-kwh-metering-circuit-breaker-timer-with-voltage-current-and-leakage-protection-tuya-tompd | Web (fabricante) | Confirmed |
| S19 | Shelly Pro 1PM — max 16A, CE (EU DoC 2025), no fault log, no motor underload | https://kb.shelly.cloud/knowledge-base/shelly-pro-1pm-v1 | Web | Confirmed |
| S20 | Copeland AE4-1365 — tiempos de reconexión de compresores scroll | https://webapps.copeland.com/online-product-information/Publication/LaunchPDF?Index=aeb&PDF=AE4-1365_R6.pdf | Web | Confirmed |
| S21 | Patent US 20240332944 — Multi-mode load protection device (3F, motor vs breaker) | https://patents.justia.com/patent/20240332944 | Web | Confirmed |
| S22 | IEC 61000-4 series — EMC immunity tests overview | https://www.academyofemc.com/emc-standards | Web | Probable |
| S23 | EU EMC Directive 2014/30/EU + Radio Equipment Directive 2014/53/EU | https://infinitalab.com/blog/electromagnetic-compatibility-emc-testing-2/ | Web | Confirmed |
| S24 | EN 61000-6-4 — industrial environment emissions | https://www.dlsemc.com/iec-en-61000-6-4-emission-standard-for-industrial-environments/ | Web | Confirmed |
| S25 | Liyuan C1-S2 — CE, ISO 9001, ~$18–22 OEM, 5 fault records, no WiFi | https://jmlypump.en.made-in-china.com/product/SOXGihCuGwVk/ (via OL-3) | Web (via Orlan) | Probable |

---

*Vera — Technical Researcher, Protección Eléctrica | Dominio Genteca | 2026-05-06*
*Output VE-1 v1 — Memo técnico validación GME*
*Candidato a archivar en KB Genteca — Celeste decide filename y clasificación final*
