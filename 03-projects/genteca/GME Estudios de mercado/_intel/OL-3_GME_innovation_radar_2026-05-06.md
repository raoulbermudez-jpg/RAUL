# OL-3 Innovation Radar — GME (Protector Monofásico Inteligente Exceline)

**Fecha:** 2026-05-06
**Tipo de output:** OL-3 (Differentiation Memo + Innovation Radar integrado)
**Scope:** Competidores del GME en su nicho exacto — protector monofásico + medición V+I simultánea + conectividad móvil + multi-aplicación (refrigeración / bombas / motores) + rango objetivo USD 30–60
**Geografía:** Global con énfasis HVAC-R (NAM), bombas (NAM + LATAM), IoT genérico (global), regional LATAM
**Horizonte:** Snapshot 2024–2026 (innovation signals 2024–2026)
**Audiencia primaria:** Owner + Vael (feasibility de claims) + Vera (gaps técnicos) + Bruna (risk de claims)
**Basado en:** Pantallas GME (_img_R/, _img_B/, _img_M/), Informe_Van_Westendorp.md, búsqueda web 2026-05-06

---

## Resumen ejecutivo (5 líneas)

El GME compite en un nicho cruzado muy específico — protección monofásica + medición simultánea de V e I + conectividad móvil consumer-friendly + multi-aplicación — donde ningún competidor global de relevancia coincide con el perfil completo al rango de precio objetivo ($30–40). Los competidores más cercanos en funcionalidad (Littelfuse 77C, Littelfuse MP8000, Franklin Electric SubMonitor Connect) son industriales de alto precio ($100–$800+), sin interfaz web local ni posicionamiento multi-aplicación por firmware. Los competidores más cercanos en precio ($18–$40) son supervisores de voltaje sin medición de corriente (ICM492, Wagner DSP-1) o smart breakers genéricos (TOMZN Tuya) sin protección orientada a motor/bomba/compresor. La categoría IoT genérico (Tuya, Shelly Pro 1PM) ofrece medición V+I + WiFi pero carece de protecciones específicas de motor (subcarga, arranques/hora, rotor trancado). El hallazgo más relevante para posicionamiento: en el segmento monofásico multi-aplicación con WiFi y rango <$60, el espacio está materialmente vacío en fuentes verificables a mayo 2026.

---

## Sección 1 — Mapa competitivo del nicho

### 1.1 Marcas globales de protección industrial — ¿compiten en este nicho?

| Marca | Producto / Línea relevante | Monofásico | Mide V+I | WiFi/App | Rango precio aprox. | Veredicto de nicho |
|---|---|---|---|---|---|---|
| **Littelfuse SymCom** | 77C Series (PumpSaver) | Sí — 100–240 VAC, 2–800 FLA | Sí — V + I + underload | No — RS-485 / Modbus opcional (módulo externo) | ~$552 (distribuidor) | Funcionalidad más cercana al GME; precio 15x superior; sin app móvil; sin webserver local; foco industrial/pump |
| **Littelfuse SymCom** | MP8000 Bluetooth Overload | Sí + 3F — 90–690 VAC, 0.5–1000 A | Sí — V + I + underload | Bluetooth solamente (app Littelfuse) | ~$806 (dist.) MSRP ~$1,305 | Bluetooth no WiFi; precio 20x+; industrial heavy; no multi-aplicación configurable |
| **Franklin Electric** | SubMonitor Connect | 3F primario; monofásico vía firmware seleccionable | Sí — V + I + dry run | Bluetooth (FE Connect app iOS/Android) | No disponible públicamente | Especializado en bombas sumergibles; 3F principalmente; precio alto; no refrigeración |
| **ICM Controls** | ICM492 (voltage monitor) | Sí — 80–300 VAC | Solo V | No | ~$50–80 est. (distribuidor HVAC) [fuente única — pendiente verificación cruzada] | Solo voltaje — no mide corriente; HVAC-focused; precio competitivo pero funcionalidad reducida |
| **ICM Controls** | ICM493 (motor protection + contactor 40A) | Sí — 200–240 VAC, 50/60 Hz | Solo V (más surge) | No | No disponible públicamente | Solo voltaje + surge; enclosure NEMA 3R; incluye contactor integrado 40A; más caro por incluir hardware |
| **Wagner / Diversitech** | DSP-1 (line voltage monitor) | Sí — 90–300 VAC | Solo V (voltímetro digital integrado) | No | ~$40–60 est. regional LATAM [fuente única — pendiente verificación cruzada] | Distribuido en LATAM/Venezuela; solo voltaje; fault memory 25 eventos; anti-short cycle; sin corriente |
| **Siemens** | 3RB / 3RU overload relays | 3F principalmente; algunos admiten 1F wiring | Sí — I (sobrecarga) | IO-Link (no WiFi consumer) | >$100 | Industrial trifásico; no posicionado para monofásico residencial-comercial ligero; sin app |
| **Schneider Electric** | TeSys Deca GV2/GV3 | Manual starters, admiten 1F | Solo I (térmica) | No WiFi; SmartWire-DT bus industrial | >$100 | Manual starters industriales; sin voltaje + corriente simultáneo; sin app |
| **Eaton** | XT / PKE manual starters | 1F posible | Solo I (sobrecarga) | SmartWire-DT industrial | >$80 | Industrial; sin WiFi; sin voltaje |
| **Rockwell (Allen-Bradley)** | 825-P (descontinuado) | 3F | Sí | DeviceNet; sin WiFi | Descontinuado | No compiten en este nicho; segmento industrial PLC-based |
| **ABB** | Manual motor starters | 3F predominante | Solo I | No WiFi | >$80 | No nicho directo |
| **Chint / LS Electric** | NVR / GMR series | 3F predominante; algunos 1F | Solo I | No WiFi | $20–60 | Competidores de precio en manual starters; sin app; sin voltaje integrado |
| **GEYA** | GRV8-01/02 (voltage relay) | Sí — 12–240 VAC | Solo V | No | ~$8–15 (Amazon) | Solo voltaje; sin corriente; sin app; muy bajo precio; china commodity |

**Lectura clave:** Las marcas globales industriales (ABB, Siemens, Schneider, Eaton, Rockwell) **no compiten en este nicho**. Juegan en trifásico industrial con buses de campo (IO-Link, SmartWire-DT, DeviceNet). El único competidor global que combina monofásico + V + I + underload es Littelfuse 77C/MP8000, pero a precio entre 15x y 30x el objetivo GME, en formato industrial, sin app WiFi, y sin posicionamiento multi-aplicación.

---

### 1.2 Marcas HVAC-específicas (cluster refrigeración — crítico: 52% de muestra survey)

| Marca | Producto | Protege V+I | Conectividad | Precio aprox. | Notas |
|---|---|---|---|---|---|
| **Copeland (Emerson)** | ComfortAlert Diagnostic Module | Solo monitoreo diagnóstico (no contactor de protección activa); mide corriente de compresor como señal de diagnóstico | LED flash codes; sin WiFi ni app standalone | ~$50–100 est. [fuente única — pendiente verificación cruzada] | Diseñado para Copeland Scroll específicamente; no es protector universal; no configurable por usuario; sin displayapp |
| **ICM Controls** | ICM492 | Solo V | Sin conectividad | Ver arriba | Ver arriba |
| **ICM Controls** | ICM493 | Solo V + surge | Sin conectividad | Ver arriba | Ver arriba |
| **ICM Controls** | Sentry3N1 (2024) | Solo V + surge (ICM517A integrado) | Sin conectividad | No disponible públicamente | Claim: protege "HVAC/R equipment single-phase 208/240 VAC"; no mide corriente |
| **Supco (Sealed Unit Parts)** | APP120 (surge protector) | No — solo surge | No | ~$30 | Solo supresión de pico; no monitoreo ni protección activa; no mide V ni I |
| **Supco** | SPP5/SPP6 (hard start kits) | No — solo arranque | No | ~$20–30 | Hard start capacitors; no protección |
| **Wagner / Diversitech** | DSP-1 | Solo V | No | Ver arriba | Ver arriba |

**Lectura clave para el nicho HVAC-R:** No existe en el mercado HVAC-R un protector monofásico de aplicación general con medición simultánea de V+I + WiFi + configuración por app en el rango $30–60. Las soluciones disponibles son: (a) protectores de voltaje básicos sin corriente (ICM492, Wagner DSP-1), (b) módulos de diagnóstico propietarios para compresores específicos (Copeland ComfortAlert), o (c) protectores de surge sin monitoreo activo (Supco, ICM517A). Este es el gap más significativo del mercado desde la perspectiva del GME-R220.

---

### 1.3 Marcas bomba-específicas

| Marca | Producto | Protege V+I | Underload / Dry run | Conectividad | Precio aprox. | Notas |
|---|---|---|---|---|---|---|
| **Littelfuse SymCom** | 77C / 77C-LR | Sí — V+I simultánea | Sí — underload explícito | RS-485 Modbus (sin WiFi) | ~$550+ | El más cercano en funcionalidad; precio industrial prohibitivo para el nicho |
| **Franklin Electric** | SubMonitor Connect | Sí (3F; 1F vía firmware) | Sí — dry run (underload + low-flow) | Bluetooth + FE Connect app | No público | Especializado bombas sumergibles; Bluetooth no WiFi; 3F principalmente; alta gama |
| **Liyuan Pump (China)** | C1-S2 220V Protector | Sí parcialmente — dry run sensor-free; sobre/bajo voltaje; sobrecarga | Sí — dry run sin sensor | No | ~$18–22 OEM | Sin app ni WiFi; LCD display; fault history 5 registros; CE ISO 9001; pump-only; sin multiaplicación |
| **Wagner DSP-1** | DSP-1 | Solo V | No | No | Ver arriba | Sin corriente |
| **Square D Pumptrol / Schneider** | Pressure switches | No (presión, no eléctrico) | No aplicable | No | ~$30–60 | Presostatos, no protector eléctrico; diferente categoría |
| **Proindecsa Safematic** | Protector bombas (España/LATAM) | Sí — corriente + detección vacío (sensor) | Sí — dry run con sensor | No | No disponible públicamente [fuente única] | Requiere sensor externo; monofásico; sin WiFi; distribuido en España y LATAM agrícola |

**Lectura clave para el nicho bombas:** El único competidor con underload (dry run) + V+I a precio accesible es el OEM chino tipo Liyuan C1-S2 (~$18–22), pero carece de WiFi, app, y multi-aplicación. Franklin Electric SubMonitor Connect tiene las funciones pero es Bluetooth, 3F-primario, y precio alto. El gap WiFi + underload + precio $30–50 está vacío en fuentes verificables.

---

### 1.4 Marcas regionales LATAM (Venezuela, Colombia, México, Brasil)

| Marca / Distribuidor | Producto | País | Protege V+I | WiFi/App | Notas |
|---|---|---|---|---|---|
| **Exceline / Genteca** | GAM-B220 (producto existente) | Venezuela | Sí — V + I (sobrecarga, bajo/alto V, rotor bloqueado) | No | Protector integral bombas monofásico 220V; $57 precio lista; contactor+térmica+voltaje integrado; SIN corriente en tiempo real ni app — este es el producto que GME reemplazaría/complementaría |
| **PC Shop VZla** | Protector Integral Bombas 220V (3 años garantía) | Venezuela | No especificado | No | Producto de tercero sin marca clara en listado; [fuente única] |
| **PrevenIng (Paraguay)** | Protector Voltaje Monofásico Smart WiFi | Paraguay | Solo V (no confirma I) | WiFi | Precio ~260,000 Gs (~$35 USD est.); MAX 63A; "protección baja y sobre tensión"; sin evidencia de medición corriente ni protecciones motor-específicas [fuente única — pendiente verificación cruzada] |
| **Wagner / Diversitech (dist. regional)** | DSP-1 | México, Venezuela, Colombia | Solo V | No | Distribuido por Eproteca (Colombia/Ecuador), Diversitech (NAM); visto en Venezuela |
| **Eproteca** | Línea propia (Colombia) | Colombia | Solo V (varios modelos) | No | Distribuidor/importador; no fabricante; catálogo tradicional |
| **No encontrado** | Fabricante LATAM con V+I+WiFi+motor | — | — | — | **No se encontró competidor relevante en LATAM fabricando protector monofásico con V+I simultáneo + WiFi en múltiples búsquedas con términos: "protector monofasico inteligente app WiFi corriente subcarga", "guardamotor WiFi Venezuela Colombia Mexico", "protector monofasico IoT LATAM 2024 2025".** Esto es hallazgo, no ausencia de búsqueda. |

**Lectura clave:** El GAM-B220 de Exceline es el precedente de portafolio más directo del GME (bomba monofásica 220V, contactor + térmica + voltaje). Su gap vs. GME es: no mide corriente en tiempo real, no tiene app/WiFi, no es multi-aplicación. El GME es, en esencia, la evolución conectada y multi-aplicación de la línea GAM-B.

---

### 1.5 Categoría IoT genérico / smart breakers con app WiFi

| Marca | Producto | V+I medición | Underload/motor | WiFi | Precio aprox. | Veredicto |
|---|---|---|---|---|---|---|
| **TOMZN (China)** | TOMPD 63A Tuya WiFi Smart Breaker | Sí — V + I + kWh en tiempo real + app Tuya | No — overcurrent sí, underload/subcarga no; sin dry run, sin arranques/hora, sin rotor trancado | Sí — 2.4G WiFi, Smart Life/Tuya app | ~$35–50 (Amazon/AliExpress) | El competidor más relevante en precio-conectividad. Falla: no tiene protecciones motor-específicas (subcarga, arranques/hora, rotor trancado, reintento programado). Es un smart circuit breaker genérico, no un guardamotor. |
| **Shelly Pro 1PM** | Smart relay DIN rail + power metering | Sí — V + W + kWh (I derivada de W) | No — overload/overpower sí; no underload motor-específico | Sí — WiFi + LAN + BT | ~$35–45 (Shelly store) | Ecosistema abierto rico (Modbus, MQTT, webhooks, Home Assistant); pero no es un protector motor; sin GUI app de configuración simplificada para técnicos no-IT |
| **Shelly Pro EM-50** | Energy meter DIN + contactor control | Sí — I hasta 50A (clamp) | No | Sí | ~$45–55 | Monitoreo energético; no protector motor |
| **Generic Tuya / ESP32-based** | Varios (Alibaba, OEM anónimo) | Varía | No | Sí | ~$10–25 | Punto de referencia citado por técnico en encuesta ("ESP32 a $10"); commodity sin protecciones motor; sin marca, sin garantía, sin certificación |

**Lectura clave:** El TOMZN Tuya y el Shelly Pro 1PM son los competidores indirectos más peligrosos desde la percepción del técnico sofisticado que ya conoce IoT. Ofrecen WiFi + V+I + app a precio similar al GME. La diferencia es que son circuit breakers genéricos sin protecciones orientadas a motor/bomba/compresor. Pero el técnico promedio que los compre podría pensar que "hace lo mismo" — esa confusión es el riesgo principal de messaging que necesita atención de Vael.

---

## Sección 2 — Innovation Signals 2024–2026

### Señal 1 — Littelfuse MP8000 con Bluetooth + monofásico (Confirmed)
- **Detalle:** El MP8000 fue actualizado con soporte explícito monofásico + 3F, Bluetooth nativo, app iOS/Android Littelfuse, y Ethernet Modbus TCP/IP. Protege V+I+underload simultáneamente en single-phase 90–690 VAC, 0.5–1000 A FLA. Certificaciones: IEC 60947-1, UL 1053, UL 60947, CE, CSA, FCC.
- **Evidencia:** Littelfuse product page + distribuidor electricmotorwholesale.com (accedido 2026-05-06)
- **Confianza:** Confirmed
- **Relevancia para Genteca:** Alta — prueba técnica de que la combinación V+I+underload+app en single-phase es alcanzable y ya existe; el gap es el precio ($806 vs $35 target GME) y la interfaz (industrial vs consumer/técnico)
- **Implicación:** Flag para Vera — confirmar si los mismos principios técnicos (CT interno para medición de I + supervisión V + lógica de underload) son los que el GME implementa. Si sí, hay precedente técnico sólido.

### Señal 2 — Franklin Electric SubMonitor Connect con soporte monofásico vía firmware (Confirmed)
- **Detalle:** El SubMonitor Connect lanzó soporte monofásico como "software-selectable configuration" que se activó vía firmware en unidades existentes. Combina dry run (underload) + V + I + Bluetooth + FE Connect app iOS/Android. Especializado en bombas sumergibles.
- **Evidencia:** franklinwater.com + Automation.com press release (accedido 2026-05-06)
- **Confianza:** Confirmed
- **Relevancia para Genteca:** Media-Alta — competidor directo en bombas con Bluetooth + dry run + app; pero el precio es alto, 3F es el modo principal, y no tiene refrigeración ni motores generales
- **Implicación:** Flag para Owner — Franklin Electric es el precedente más cercano en la combinación dry-run + app + single-phase para bombas. Si GME logra el mismo feature set a <$40, la diferenciación de precio es de 10x+.

### Señal 3 — TOMZN Tuya TOMPD lanzamiento activo 2023–2025 en mercado masivo (Confirmed)
- **Detalle:** Familia de smart circuit breakers con WiFi (Smart Life/Tuya app), medición V+I+kWh en tiempo real, over/undervoltage ajustable, overcurrent ajustable, leakage protection, precio $35–50. Disponibles en Amazon, AliExpress. Sin underload/motor protections específicas.
- **Evidencia:** tomznelectric.com + Amazon listings (accedido 2026-05-06)
- **Confianza:** Confirmed
- **Relevancia para Genteca:** Alta como amenaza de confusión en la mente del técnico — mismo precio, mismo WiFi, similar app, pero distinto propósito
- **Implicación:** Flag para Vael — el mensaje GME debe diferenciar explícitamente el "protector integral de motor/bomba/compresor" del "smart breaker genérico". El técnico que ya conoce Tuya necesita entender que subcarga, arranques/hora y lógica de reintento no están en el Tuya.

### Señal 4 — Shelly Pro 1PM / Gen4 consolidando DIN rail + WiFi + power metering en canal técnico (Confirmed)
- **Detalle:** Shelly Pro 1PM y Gen4 son relays DIN rail WiFi + LAN + Bluetooth con medición de potencia activa (V, W, kWh). API abierta, compatible con Home Assistant, MQTT, Modbus. Precio $35–45. Sin protecciones motor-específicas (underload, arranques/hora, lógica de reintento).
- **Evidencia:** shelly.com + distribuidores (accedido 2026-05-06)
- **Confianza:** Confirmed
- **Relevancia para Genteca:** Media como competidor indirecto en técnicos con perfil IoT. Alta como señal de que el mercado técnico ya acepta DIN rail WiFi como estándar.
- **Implicación:** Flag para Vael — GME debe posicionarse como "protector de motor especializado" no como "smart relay". La distinción es aplicación-específica.

### Señal 5 — Copeland (Emerson) lanzando soluciones de diagnóstico móvil para compresores scroll (Confirmed)
- **Detalle:** Copeland tiene app móvil y ComfortAlert para diagnóstico de compresores Copeland Scroll. No es un protector configurable por usuario; es un módulo propietario. El movimiento de Copeland/Emerson hacia diagnóstico móvil en HVAC-R muestra la dirección del mercado.
- **Evidencia:** copeland.com (accedido 2026-05-06)
- **Confianza:** Confirmed
- **Relevancia para Genteca:** Media — confirma que el técnico HVAC-R ya espera conectividad en herramientas de diagnóstico; GME puede posicionarse como el equivalente universal (no-Copeland-specific)
- **Implicación:** Flag para Vael — ángulo de mensaje: "para cualquier compresor, bomba o motor, no solo para la marca X".

### Señal 6 — Patent filing: "Multiple-Mode Load Protection Device" (US 20240332944, oct 2024) (Signal — directional)
- **Detalle:** Aplicación publicada octubre 2024 (presentada marzo 2023) describe un dispositivo de protección configurable para operar como "motor protection mode" o "circuit breaker mode", con análisis de desequilibrio de fase. No menciona WiFi ni app explícitamente en el abstract.
- **Evidencia:** patents.justia.com (accedido 2026-05-06)
- **Confianza:** Signal (directional — no confirmado como producto comercial)
- **Relevancia para Genteca:** Media — señal de que el concepto de multi-modo (motor / breaker) es terreno activo de R&D y patente
- **Implicación:** Flag para Vera — revisar si el GME tiene exposición a esta patente o si su arquitectura es diferenciada.

### Señal 7 — AHR Expo 2025 (febrero 2025, Orlando): sin lanzamientos relevantes confirmados en este nicho específico (Signal — ausencia confirmatoria)
- **Detalle:** AHR Expo 2025 dominado por compresores VRF (LG, Danfoss), calor bomba, IAQ. No se encontró evidencia de lanzamiento de protector monofásico universal con WiFi por marcas HVAC establecidas.
- **Evidencia:** Cobertura AHR Expo 2025 (refindustry.com, pmmag.com, achrnews.com) — accedido 2026-05-06
- **Confianza:** Signal (ausencia en cobertura pública — no garantiza que no hubo exhibición menor)
- **Relevancia para Genteca:** Media — la ausencia de un competidor HVAC establecido lanzando este tipo de producto en la feria más importante del sector es favorable para el window de entrada del GME
- **Implicación:** Flag para Owner — la ventana de entrada parece abierta en el canal HVAC-R para un producto con estas características.

### Señal 8 — PrevenIng (Paraguay) con "Protector de voltaje monofásico Smart WiFi" (Signal — fuente única, no verificable)
- **Detalle:** Producto listado en Paraguay con WiFi, 63A, "protección baja y sobre tensión". No queda claro si mide corriente. Precio ~$35 USD est. Fabricante PrevenIng — sin datasheet disponible públicamente.
- **Evidencia:** parecebuenaidea.com.py (accedido 2026-05-06) [fuente única — pendiente verificación cruzada]
- **Confianza:** Signal (fuente única, datos incompletos)
- **Relevancia para Genteca:** Media — si este producto mide corriente + subcarga, sería el competidor regional más directo en precio. Necesita verificación.
- **Implicación:** Flag para Owner — investigar PrevenIng: fabricante local, importador, o marca blanca de producto chino? ¿Mide corriente o solo voltaje? Paxs puede acceder si el sitio bloquea.

---

## Sección 3 — Posicionamiento de Exceline GME (lectura preliminar para Vael — no claims)

### Diferenciado ✅

- **Medición simultánea V + I + Hz en tiempo real con setpoints configurables en la misma pantalla principal:** Ningún competidor en el rango $30–60 ofrece esta combinación. Los smart breakers Tuya/Shelly miden V+I pero sin setpoints orientados a motor. Los protectores motor (Littelfuse 77C, Franklin SubMonitor) tienen esta funcionalidad pero a 15x–25x el precio.
  - Evidencia: Pantalla 2 (Mediciones) del GME-R220, cross-referenced con catálogos de competidores.

- **Interfaz web local (webserver en IP local 192.168.0.21) accesible desde cualquier browser sin instalación de app:** Ningún competidor relevante a este precio usa este modelo de UI. Tuya/Shelly usan app propietaria con dependencia de cloud. Littelfuse 77C usa RS-485 + PC software. El GME corre una UI completa en el browser del teléfono sin app store.
  - Evidencia: URL 192.168.0.21 visible en todas las capturas de pantalla del GME.
  - Nota para Vera: confirmar si hay dependencia de cloud para funcionalidad crítica (protección activa debe funcionar sin WiFi/internet).

- **Configuración multi-aplicación (Motores/Bombas/Refrigeración) en un solo hardware:** Ningún competidor a este precio segmenta por aplicación con perfil de protección diferente. El GME adapta sus umbrales y lógica (subcarga en %, arranques/hora, tiempo de reintento) al tipo de carga seleccionada.
  - Evidencia: Pantalla de Configuración (Pantalla 5) con radio Motores/Bombas/Refrigeración.

- **Protección de subcarga configurable (% de subcarga, tiempo de detección, reintento) en este rango de precio:** La detección de bomba en vacío o compresor descargado es funcionalidad de sistemas industriales de $400+. El GME la ofrece con control por app a $35.
  - Evidencia: Pantalla 4 (Ajustes Digitales) del GME-R220: "Activación de la subcarga", "% de Subcarga 60%", "Tiempo de detección de subcarga 10s", "Tiempo para el reintento 240s".

- **Etiquetado de equipo + GPS desde la app:** Ningún competidor en este nicho identificado ofrece etiquetado por nombre de equipo + geolocalización. Pantalla 1 muestra "Motor #2 de la sala de máquinas #1" con ícono de pin de ubicación.
  - Evidencia: Pantalla principal GME (todas las variantes).

### Paridad ⚖

- **Protección de alto/bajo voltaje ajustable:** Standard en protectores de voltaje desde ~$15. Paridad total con Wagner DSP-1, ICM492, GEYA GRV8, y similares.

- **Protección de sobrecarga de corriente:** Standard en guardamotores de cualquier precio. El GME comparte esta funcionalidad con Liyuan C1-S2, GAM-B220, Littelfuse 77C, ICM493.

- **Protección de rotor trancado:** Funcionalidad presente en guardamotores básicos y en productos de precio medio-alto. Paridad con 77C, Franklin SubMonitor, Liyuan C1-S2.

- **Retardo de reconexión / anti-short cycle:** Presente en ICM492, Wagner DSP-1, ICM493, y Littelfuse 77C. Paridad.

- **Reporte de fallas por tipo:** El GME muestra última falla por tipo en la pantalla (sin timestamp cronológico). Wagner DSP-1 tiene 25 fault events. ICM493 tiene fault history de 5 eventos. Littelfuse 77C tiene log con timestamp. GME está en el nivel básico del segmento — paridad con el extremo inferior.

### Expuesto ⚠

- **Historial de fallas cronológico (con timestamp de fecha/hora):** El GME muestra última falla por tipo pero no un log cronológico con fecha y hora. Wagner DSP-1 guarda 25 eventos. Franklin SubMonitor Connect guarda log con fecha/hora real (real date and time-stamped). Littelfuse 77C tiene log con timestamp. Este gap fue identificado en la encuesta interna como hallazgo.
  - Gap comercial: el técnico que regresa a un equipo necesita saber cuándo ocurrió la falla, no solo qué tipo. Este gap abre una objeción en clientes exigentes.
  - Implicación: Flag para Vera (¿es implementable en firmware V1.x o en roadmap?) + Flag para Owner (prioridad de roadmap).

- **Certificaciones formales (UL, CE, IEC):** No se pudo confirmar certificación del GME en la información disponible. Competidores relevantes: Littelfuse 77C tiene UL508 + UL1053 + CE (IEC 60947) + CSA. ICM493 tiene UL. Liyuan C1-S2 tiene CE + ISO 9001.
  - Implicación: Flag para Vera — confirmar estado de certificaciones del GME. En mercados de exportación (EE.UU., Caribe, Colombia) las certificaciones son gate de entrada. Sin CE o UL, el claim "de calidad industrial" tiene debilidad estructural.

- **Medición de frecuencia con protección activa (inestabilidad de frecuencia):** El GME muestra frecuencia en tiempo real (59.8 Hz en pantalla de Mediciones). La Pantalla 5 (Reporte de Fallas) muestra "Inestabilidad: 54 Hz". Esto sugiere protección activa por frecuencia. No se pudo confirmar en otros competidores del rango de precio. Potencial ventaja pero necesita confirmación de spec.
  - Nota: Si el GME protege activamente contra inestabilidad de frecuencia (no solo la muestra), esto es diferenciador en mercados con red eléctrica inestable (Venezuela, el Caribe). Pendiente confirmación técnica.
  - Implicación: Flag para Vera — ¿la protección de frecuencia en el GME es activa (dispara contactor) o solo diagnóstica (muestra pero no actúa)?

- **Capacidad de corriente máxima confirmada públicamente:** Las pantallas muestran valores de hasta 40A (sobrecarga en reporte de fallas), 15.6A en tiempo real, y perillas físicas en pantalla 3. No se pudo determinar el rango máximo certificado de corriente del GME (en FLA). Competidores están claramente especificados (77C: 2–800A; MP8000: 0.5–1000A; Liyuan C1-S2: hasta 2.2 kW / ~10A). Esto puede ser un gap de comunicación técnica, no de producto.
  - Implicación: Flag para Vera — definir y publicar rango de corriente nominal del GME por variante (R/B/M).

- **Compatibilidad multivoltaje (120/220V):** La encuesta capturó comentarios de técnicos que piden soporte 120V/220V dual. El GME aparece como "220" en el SKU. Si solo soporta 220V, pierde parte del mercado de bombas en zonas residenciales con instalación 120V. Competidores: ICM493 acepta 200–264V; Wagner DSP-1 acepta 90–300V; Liyuan C1-S2 es 220V solamente.
  - Implicación: Flag para Vera — ¿hay variante 120V planificada? ¿El hardware ya puede soportar 120V con cambio de firmware/componentes?

---

## Sección 4 — Claim Feasibility Notes

### Claim candidato A: "Primer protector monofásico con medición simultánea de voltaje y corriente + configuración WiFi por menos de $X"

- **Evidencia que lo respalda:** No se encontró ningún producto en el rango $30–60 con medición V+I simultánea + WiFi en múltiples búsquedas. Los productos con V+I+WiFi (Littelfuse MP8000) están en $800+. Los productos con WiFi a precio similar (TOMZN Tuya, Shelly Pro 1PM) no tienen protección motor-específica.
- **Riesgo de over-claim:** Medio-alto. El claim "primer" requiere confirmación exhaustiva de que ningún producto en Alibaba, marcas chinas B2B, o fabricantes regionales LATAM tiene este combo. La búsqueda cubrió las fuentes principales pero no es exhaustiva de todo el mercado chino OEM.
- **Categoría:** ⚠ Defendible con caveat
- **Caveat sugerido:** Acotar geografía (Venezuela / LATAM) y/o acotar precio explícitamente ("en el rango de precio X"). El claim global "primer" es más difícil de defender. Regional LATAM o "en su rango de precio" es más sólido.
- **Nota para Bruna:** Este claim necesita gate antes de uso público. Requiere que Vera confirme specs técnicas del GME y que se defina el benchmark de precio para la comparación.

### Claim candidato B: "Protección integral: voltaje + corriente + subcarga + arranques por hora en monofásico a precio accesible"

- **Evidencia que lo respalda:** Ningún competidor identificado en el rango $30–60 tiene la combinación completa subcarga + arranques/hora + V + I. El Tuya TOMPD y Shelly Pro 1PM tienen V+I pero no subcarga ni arranques/hora. El 77C tiene todo pero a $550+.
- **Riesgo de over-claim:** Bajo-medio. El claim es descriptivo de funcionalidad verificable (las pantallas del GME lo muestran). El riesgo es si "subcarga" está implementada correctamente en el firmware final — no solo mostrada en UI de prototipo.
- **Categoría:** ⚠ Defendible con caveat
- **Caveat sugerido:** "Sujeto a confirmación de que las funciones mostradas en la UI están implementadas en firmware de producción." Vera debe validar que subcarga, arranques/hora, y reintento están activos y probados.
- **Nota para Bruna:** Claim funcional sólido una vez Vera confirme la implementación. Este es probablemente el claim más defendible del portafolio del GME.

### Claim candidato C: "Interfaz web local — sin app que instalar, sin cloud requerida"

- **Evidencia que lo respalda:** El GME corre un webserver local (IP 192.168.0.21 visible en capturas). Competidores Tuya/Shelly requieren app propietaria y tienen dependencia de cloud para funcionalidad completa.
- **Riesgo de over-claim:** Bajo — si el GME realmente opera sin cloud para las funciones de protección. Nota crítica: si la protección activa (disparar el contactor) requiere WiFi conectado o servidor cloud, el claim se debilita significativamente.
- **Categoría:** ✅ Defendible — con confirmación técnica de operación standalone
- **Caveat sugerido:** Confirmar con Vera que la protección activa funciona sin WiFi y sin internet. Si el GME desconecta el equipo ante falla incluso sin conexión, el claim "sin cloud requerida" es plenamente defendible y es diferenciador real vs. Tuya.
- **Nota para Bruna:** Este es un claim técnico de arquitectura — necesita confirmación de Vera antes de uso.

### Claim candidato D: "Diagnóstico a distancia — conoce el estado de tu equipo desde el teléfono"

- **Evidencia que lo respalda:** La UI del GME muestra V, I, Hz, estado de relé, entrada digital, última falla, y nombre del equipo en tiempo real desde cualquier browser en la red local.
- **Riesgo de over-claim:** Bajo si se acota a "red local (WiFi)". Alto si se interpreta como "desde cualquier lugar del mundo" (requeriría túnel VPN, port forwarding, o relay cloud que no está confirmado).
- **Categoría:** ⚠ Defendible con caveat
- **Caveat sugerido:** Especificar "mientras estés en la misma red WiFi" o "desde la red local". Si en versiones futuras se agrega acceso remoto (VPN o relay), el claim puede ampliarse.

### Claim candidato E: "Para neveras, bombas y motores — un solo protector, tres modos de aplicación"

- **Evidencia que lo respalda:** Pantalla 5 (Configuración) muestra selector Motores/Bombas/Refrigeración. Esta funcionalidad multi-aplicación no existe en ningún competidor identificado en este rango de precio.
- **Riesgo de over-claim:** Bajo si los tres modos están implementados con lógicas diferenciadas en firmware de producción (no solo en la UI de la encuesta).
- **Categoría:** ✅ Defendible — con confirmación técnica
- **Nota para Bruna:** Uno de los claims más únicos y diferenciadores. Verificar con Vera que cada modo tiene lógica de protección diferenciada (no solo un label).

---

## Próximas indagaciones

1. **Verificar PrevenIng (Paraguay):** ¿Es fabricante local, importador de producto chino, o marca blanca? ¿Mide corriente además de voltaje? Este es el único competidor regional LATAM identificado con "Smart WiFi" a precio similar. Si mide V+I + tiene protecciones motor, sería el competidor regional más directo.
   - Acción: Paxs (si el sitio bloquea) o búsqueda directa en LinkedIn/registros comerciales Paraguay.

2. **Confirmar rango de corriente y voltaje del GME por variante (R/B/M):** Las pantallas muestran ejemplos (15.6A, 40A en falla, perillas) pero no el rango máximo nominal. Necesario para tabla comparativa OL-2 y para claims técnicos.
   - Acción: Vera / Owner.

3. **Estado de certificaciones del GME:** UL, CE, IEC 60947, NEMA — ¿cuál tiene, cuál está en proceso, cuál no está planeada? Crítico para mercados de exportación y para claims de calidad.
   - Acción: Vera / Owner.

4. **Confirmar que la protección activa del GME opera sin WiFi / sin internet:** Si el relé de corte funciona offline (solo requiere alimentación AC), el claim "sin dependencia de cloud" es defendible. Si requiere WiFi activo para la lógica de protección, es un gap de arquitectura crítico.
   - Acción: Vera (spec de firmware).

5. **Confirmar implementación de frecuencia como protección activa:** La pantalla muestra "Inestabilidad: 54 Hz" en el reporte de fallas. ¿Es una falla que dispara el contactor o solo un evento diagnóstico sin acción? Si es activa, es diferenciador relevante para mercados con red inestable.
   - Acción: Vera.

6. **Investigar mercado chino OEM más en profundidad:** Las búsquedas cubrieron Made in China y Alibaba superficialmente. Puede existir un producto chino sin nombre en AliExpress con V+I+WiFi+motor protections a $20–30 que no apareció en los queries. Búsqueda recomendada: AliExpress directo con términos "single phase motor protector WiFi underload dry run 220V" + filtro China.
   - Acción: Orlan segunda iteración o Paxs para búsqueda profunda en plataformas chinas.

7. **Precio del ICM492 y ICM493 en mercado venezolano / LATAM:** Ambos son distribuidos en el sector HVAC venezolano (a través de distribuidores de Diversitech/ICM). Conocer el precio local anclaría mejor la comparativa de precio frente al GME.
   - Acción: Raul / Owner confirmar con distribuidores locales.

8. **Verificar Wagner DSP-1 precios actuales en Venezuela y Colombia:** Eproteca (Colombia) y distribuidores venezolanos lo tienen en catálogo. Precio observado en Colombia ~$40–60 USD. Confirmar precio Venezuela.
   - Acción: Raul / Owner.

---

## Recomendaciones para escalación

### Para Vael (mensaje / framework de positioning)
- El GME tiene tres diferenciadores primarios defendibles que Vael debe convertir en arquitectura de mensaje: (1) la combinación V+I+WiFi+motor protections en un solo producto a precio accesible, (2) interfaz web local sin app que instalar ni cloud, (3) configuración multi-aplicación (R/B/M). Ninguno de estos tres existe junto en un competidor del mismo rango de precio.
- El riesgo de confusión principal es con Tuya/Shelly: el mensaje debe explicar la diferencia entre "smart breaker genérico" y "guardamotor inteligente". El técnico que ya conoce Tuya es el más difícil de convencer y el más valioso de ganar.
- La presencia del GAM-B220 en el portafolio propio (protector bomba sin app, $57) es un anchor para comunicar la evolución: "la siguiente generación".

### Para Vera (técnica / specs)
- Verificar implementación activa de protecciones: subcarga, arranques/hora, rotor trancado, inestabilidad de frecuencia. Confirmar que cada función dispara el contactor y no solo muestra un evento en pantalla.
- Definir rango nominal de corriente por variante (FLA máximo para R220, B220, M220).
- Confirmar operación offline (protección activa sin WiFi).
- Revisar exposición a patent US 20240332944 (multi-mode load protection device).
- Evaluar roadmap de historial cronológico de fallas (timestamp): es el gap funcional más visible frente a competidores de precio medio (Wagner DSP-1 tiene 25 eventos con historial).
- Evaluar variante 120V / multivoltaje: comentarios de la encuesta lo demandan.

### Para Bruna (claims / risk gate)
- Los claims candidatos C ("sin cloud") y E ("tres modos, un protector") son los más defendibles. Prioritarios para Vael.
- El claim candidato A ("primero en el mercado") requiere investigación adicional antes de usarse. No usar sin confirmación de scope geográfico y sin búsqueda más profunda en mercado chino OEM.
- El claim candidato B ("protección integral") es sólido funcionalmente pero requiere que Vera confirme la implementación en firmware de producción.
- Ningún claim debe usarse hasta que Vera confirme specs finales del GME y hasta que Bruna revise el scope exacto del lenguaje.

### Para Owner (roadmap / estrategia)
- El gap de precio entre el GME ($35 target) y el competidor funcional más cercano (Littelfuse 77C ~$550, MP8000 ~$806) define un white space enorme. El riesgo no es un competidor directo existente, sino (a) un fabricante chino OEM que lance un producto similar antes del GME, o (b) que el técnico use un Tuya TOMPD como sustituto parcial.
- La ventana de entrada parece abierta (no hay competidor directo identificado en LATAM a mayo 2026).
- Certificaciones son el gate de entrada para mercados de exportación fuera de Venezuela. Priorizar al menos CE para el Caribe / Colombia.
- El historial cronológico de fallas (timestamp) es la mejora de roadmap de mayor impacto para la percepción de producto premium vs. competidores industriales.

---

## Supuestos y límites

**Supuesto 1:** Las pantallas del GME mostradas en la encuesta representan la funcionalidad real del producto en desarrollo o en producción cercana. Si son conceptos de UI sin implementación completa, los claims de diferenciación deben reconsiderarse.

**Supuesto 2:** El GME-R220 / B220 / M220 es un producto cuya arquitectura hardware ya está definida (perillas físicas visibles en Pantalla 3 confirman hardware físico real). El análisis asume que el firmware está en estado avanzado de desarrollo.

**Supuesto 3:** El precio target de $35 (OPP del Van Westendorp) es el escenario A (SKU único o pricing transversal). Las comparativas de precio de competidores se hacen contra este benchmark.

**Límite 1:** La búsqueda de competidores chinos OEM fue superficial. AliExpress y Alibaba contienen cientos de productos de nicho que no aparecen en Google convencional. No se puede afirmar con certeza absoluta que no existe un producto chino sin marca con V+I+WiFi+underload a $20–30. Este punto necesita investigación adicional antes de usar claims de "primero" o "único".

**Límite 2:** Los precios de distribuidores locales venezolanos para competidores (ICM492, Wagner DSP-1, GAM-B220) son estimaciones o valores únicos de sitios no verificados con cross-reference. Tomar como direccionales.

**Límite 3:** Las páginas de Littelfuse (77C, MP8000) retornaron 403 en algunos intentos. Las especificaciones técnicas de estos productos se obtuvieron de distribuidores (rcworst.com, electricmotorwholesale.com) — consideradas de alta confianza pero no son el datasheet oficial del fabricante.

**Límite 4:** El análisis no cubre el segmento trifásico industrial. Si el Owner desea expandir el GME a trifásico en el futuro, se necesitaría un OL-3 separado para ese sub-segmento.

**Límite 5:** Este análisis es snapshot a mayo 2026. El mercado de protectores IoT genéricos (Tuya, Shelly) evoluciona rápidamente. Un review trimestral (OL-4) está recomendado.

---

## Sources

| # | Fuente | URL | Fecha de acceso | Confianza | Notas |
|---|---|---|---|---|---|
| 1 | Littelfuse 77C Series — distribuidor rcworst | https://rcworst.com/products/littelfuse-77c-pump-monitor-overload-relay-100-240v-single-phase-2-800fla | 2026-05-06 | Probable | Precio $552.68 verificado; specs coinciden con búsqueda Littelfuse; no es datasheet oficial (Littelfuse retornó 403) |
| 2 | Littelfuse MP8000 — distribuidor electricmotorwholesale | https://www.electricmotorwholesale.com/MP8000 | 2026-05-06 | Probable | Precio $806.02 / MSRP $1,305.29; certifications confirmadas vía búsqueda Littelfuse.com |
| 3 | ICM Controls ICM493 — página oficial | https://www.icmcontrols.com/product/icm493/ | 2026-05-06 | Confirmed | Datasheet de fabricante; specs completas verificadas |
| 4 | ICM Controls ICM492 — supplyhouse.com | https://www.supplyhouse.com/ICM-Controls-ICM492-ICM492-Single-Phase-Motor-Protection-80-300-VAC | 2026-05-06 | Confirmed | Distribuidor HVAC autorizado; specs verificadas |
| 5 | Franklin Electric SubMonitor Connect | https://www.franklinwater.com/products/drives-starters-and-protection/protective-devices/submonitor-connect-three-phase-protection/ | 2026-05-06 | Confirmed | Página oficial fabricante; soporte monofásico confirmado |
| 6 | TOMZN TOMPD 63A WiFi Smart Breaker | https://www.tomznelectric.com/product-tomzn-63a-80a-wifi-smart-energy-meter-kwh-metering-circuit-breaker-timer-with-voltage-current-and-leakage-protection-tuya-tompd | 2026-05-06 | Confirmed | Página oficial fabricante TOMZN; specs completas |
| 7 | Shelly Pro 1PM — shelly.com | https://www.shelly.com/products/shelly-pro-1pm | 2026-05-06 | Confirmed | Página oficial Shelly |
| 8 | Wagner DSP-1 — eproteca.com (distribuidor Colombia) | https://www.eproteca.com/producto/protecciones-contra-variaciones-de-voltaje/protectores-de-voltaje/protector-monofasico-de-voltaje-mod-dsp-1/ | 2026-05-06 | Probable | Distribuidor autorizado; fabricante Wagner; origen no confirmado explícitamente [single-source para origen] |
| 9 | Copeland ComfortAlert | https://www.copeland.com/en-us/shop/1/copeland-comfortalert-for-residential-applications | 2026-05-06 | Confirmed | Página oficial Copeland/Emerson |
| 10 | Exceline GAM-B220 — comercialcaracas.com | https://comercialcaracas.com/productos/protector-integral-exceline-para-bombas-monofasicas-220v-gam-b220/ | 2026-05-06 | Confirmed | Distribuidor venezolano; precio $57 USD verificado; producto Exceline confirmado |
| 11 | Liyuan C1-S2 pump protector — made-in-china.com | https://jmlypump.en.made-in-china.com/product/SOXGihCuGwVk/China-C1-S2-220V-Single-Phase-Submersible-Pump-Overload-Under-Overvoltage-Motor-Stalled-Dry-Run-Sensor-Free-Controller-Control-Box-Protector.html | 2026-05-06 | Probable | Catálogo fabricante chino; precio $18–22 OEM; CE + ISO 9001 declarados por fabricante |
| 12 | PrevenIng Smart WiFi protector — parecebuenaidea.com.py | https://parecebuenaidea.com.py/producto/protector-de-voltaje-monofasico-smart-wifi/ | 2026-05-06 | Speculative | [Fuente única] Datos técnicos mínimos; precio ~$35 USD estimado; sin confirmación de medición de corriente |
| 13 | Patent US 20240332944 — Justia | https://patents.justia.com/patent/20240332944 | 2026-05-06 | Confirmed | Patent filing publicado octubre 2024; abstracto leído; claims completos no analizados |
| 14 | AHR Expo 2025 cobertura | https://refindustry.com/articles/articles/ahr-expo-2025-exploring-hvacr-innovations-from-featured-exhibitors/ | 2026-05-06 | Confirmed | Cobertura periodística; ausencia de lanzamiento relevante en el nicho — ausencia confirmatoria |
| 15 | Pantallas GME (fuente primaria interna) | C:\RAUL\03-projects\genteca\GME Estudios de mercado\_img_R\ | 2026-05-06 | Confirmed | Imágenes del producto Exceline GME; fuente primaria interna — máxima confianza para specs propias |
| 16 | Informe Van Westendorp GME | C:\RAUL\03-projects\genteca\GME Estudios de mercado\Informe_Van_Westendorp.md | 2026-05-06 | Confirmed | Análisis interno; n=29; contexto de precio y segmentación |
| 17 | GEYA GRV8-01 — geya.net | https://www.geya.net/product/single-phase-voltage-monitoring-relay-grv8-01/ | 2026-05-06 | Confirmed | Página oficial GEYA; solo voltaje sin corriente confirmado |
| 18 | Shelly Pro EM-50 — shelly.com | https://www.shelly.com/products/shelly-pro-em-50 | 2026-05-06 | Confirmed | Página oficial |

---

*Orlan — Market Intelligence Analyst | Dominio Genteca | 2026-05-06*
*Output OL-3 v1 — Innovation Radar + Differentiation Memo integrados*
*Candidato a archivar en Market KB — Celeste decide filename y clasificación final*
