---
doc_type: OL-1-differentiation-matrix
project_id: portfolio-naming-ip-2026
domain: genteca
version: v1.0
author: Orlan
fecha: 2026-05-13
base_docs:
  - 00-project-charter.md (v1.0 2026-05-13)
  - AU-1 plan-de-contenido_v1.md
  - AU-1 top7-mapping-preliminar_v1.md
  - reference_sapi_venezuela_quick.md
  - KB Genteca: GSM-L HDE v10, GIII+MV spec sheet, GSM-MB/RB/RF HDE, Genius catalog 03/2025, proteccion trifasica catalog
override_activo: curva inversa V-t algorítmica + I-t cold/hot asumida universal de facto (charter §3 decision 4)
---

# Differentiation Matrix — Genteca Portfolio vs Competencia
## Proyecto: Portfolio Naming IP 2026

> Posicionamiento competitivo por nodo tecnológico para el proyecto de naming portfolio IP 2026.
> Verde = Genteca única o primera en clase con implementación distintiva. Amarillo = paridad, pero bien ejecutada o con aspecto superior. Rojo = gap o paridad débil.
>
> **Nota de alcance:** Vera trabaja en paralelo. Esta matrix arranca de la hipótesis de nodos A-I del AU-1 mapping (Aurelio). Reconciliación formal en Phase 5.

---

## Resumen ejecutivo

| Estado | Nodos | Comentario breve |
|--------|-------|------------------|
| Verde | 2 (B, G) | Genteca claramente diferenciada: detección 20ms es spec documentada sin equivalente publicado en supervisores del segmento; TaskMemory sin equivalente en controladores de bombeo/nivel de la competencia |
| Amarillo | 4 (A, C, E, F) | Genteca bien posicionada pero la función existe en competencia, a veces bajo nombre comercial propio |
| Rojo | 1 (D) | ThermalCurve — la curva inversa I-t cold/hot es universal IEC 60947 y está en todos los grandes; el nombre es descriptivo del mecanismo estándar |
| Slots abiertos evaluados | 2 (H, I) | H: supervisión trifásica integral monobloc — amarillo. I: Modbus nativo en gama baja — sin diferenciador claro |

**Espacio semántico ya nombrado por competencia (lista preliminar para Solenne):**
"Voltage Loss Restart" (Eaton C445), "Temperature Module" (Siemens SIMOCODE 3UF7), "Motor Insight" (Eaton C441), "TeSys T" (Schneider LTMR), "SIMOCODE" (Siemens), "E300" (Rockwell), "Smart Motor Control" (Rockwell), "Power Xpert" (Eaton), "EKIP" (ABB), "Thermal Memory" (term genérico en múltiples fabricantes).

---

## Matriz por nodo

---

### NODO A — Lógica de reconexión inteligente / escalonamiento aleatorio post-evento

**Anchor Top 7:** StaggerStart

- **Estado competitivo Genteca:** Amarillo
- **Quién más lo tiene:** Eaton (Power Xpert C445), Rockwell (posiblemente en E300 via Start Delay configurable), Siemens (SIPROTEC, SIMOCODE — función de start delay post-falla)
- **Cómo lo nombran ellos:**
  - Eaton C445: **"Voltage Loss Restart"** — nombre descriptivo funcional, no fantástico. Publicado en application note oficial. La función implementa staggered restart aleatorio tras pérdida de voltaje. [HECHO VERIFICADO: application note Eaton ap042004en disponible públicamente]
  - Siemens: sin nombre comercial de fantasía identificado — se describe como "connection delay" o "start-up delay" ajustable. [CLAIM: basado en conocimiento de producto; no verificado en datasheet específico para esta sesión]
  - Rockwell E300: "Start Delay" configurable post-falla — no tiene nombre comercial de fantasía. [CLAIM: basado en documentación general E300; no verificado el parámetro específico en esta sesión]
  - Chint / Lovato / LS: sin nombre comercial identificado para esta función. Sus relés ofrecen tiempo de rearme ajustable pero sin branding de fantasía. [CLAIM: basado en portafolio general de producto; no verificado en datasheet sesión]

- **Diferenciador real Genteca:** La implementación Genteca en GSM-MB/RB/RE aplica un retardo aleatorio dentro de una ventana configurable — el objetivo es prevenir el pico de demanda simultáneo en instalaciones residenciales/comerciales con múltiples unidades. Eaton C445 implementa el mismo concepto pero está orientado a motores industriales en MCC (Motor Control Center) y se configura vía red de comunicación (EtherNet/IP, DeviceNet). La diferencia de Genteca es la ejecución en un protector enchufable de bajo costo, sin red de comunicación, para el segmento residencial/comercio pequeño — segmento donde Eaton C445 no compite directamente en VE/MX. El diferenciador no es la función; es el segmento + punto de precio + simplicidad.

- **Riesgo descriptividad SAPI/IMPI:** Bajo para "StaggerStart". El nombre combina "Stagger" (técnico, no cotidiano en español) + "Start" (genérico solo). La combinación no es descriptiva literal del producto eléctrico para el consumidor venezolano o mexicano promedio — encaja en el perfil de signo de fantasía bajo la doctrina de equivalencia perceptual SAPI.

- **Notas para Solenne:** "Voltage Loss Restart" de Eaton es descriptivo y no tiene perfil de marca. El espacio semántico "restart", "reconnect", "soft start" está menos saturado en marcas de fantasía que en claims funcionales genéricos. "Stagger" como raíz es técnicamente específica y raramente usada en nombres registrados en clase 9 LatAm. Espacio disponible para variantes con raíz Stagger, Stage, Cascade, Seq (sequence), Relay. Evitar combinaciones con "Voltage" + "Restart" (demasiado descriptivo).

---

### NODO B — Protección por voltaje / detección de perturbaciones rápidas (flicker)

**Anchor Top 7:** FlickerGuard (sub-ciclo 20ms, producto: GSM-L)

- **Estado competitivo Genteca:** Verde
- **Quién más lo tiene y cómo:** Todos los grandes fabricantes tienen protección de voltaje y algunos tienen detección de flicker o "sag" rápido. Sin embargo, la especificación publicada de 20ms en un supervisor de voltaje monofásico de gama baja residencial/comercial no tiene equivalente identificado.
  - ABB CM-ESS series: supervisores de voltaje mono/trifásico con delay mínimo "instantáneo" a 30s. No publican tiempo de detección de flicker en milisegundos en sus datasheets de la gama CM. [HECHO: datasheet CM-ESS.2 consultado; no especifica ms de detección de flicker]
  - Siemens 3RN2 / 3RU2: relés térmicos y termistor. No tienen función de detección de flicker como feature nombrado. [CLAIM: basado en documentación de serie; no verificado datasheet completo]
  - Schneider TeSys LT3 / LTM: no mencionan flicker detection como feature diferenciador en gama de overload relays. [CLAIM]
  - Eaton C440/C441: no tiene flicker detection como feature nombrado. [CLAIM]
  - Rockwell E300: protección de voltaje con Trip Delay configurable; no menciona sub-ciclo flicker detection. [CLAIM]
  - Chint NJYB2: supervisor de voltaje trifásico — protección de sobrevoltaje, bajovoltaje, pérdida de fase, desequilibrio. Sin detección de flicker como feature documentado. [HECHO: producto consultado vía web]
  - Lovato RF38: motor protection relay, fase perdida/asimetría. Sin detección de flicker documentada. [HECHO: catálogo Lovato consultado]
  - Otros protectores residenciales de marca china (Chint GSM equivalente): protección básica OV/UV con tiempo de disparo ajustable. Sin detección de flicker sub-ciclo publicada. [CLAIM general]
  - Otros protectores residenciales VE: "Actuación instantánea contra parpadeos" es claim genérico en la categoría pero sin especificación en ms que compita con 20ms del GSM-L. Los propios GSM-RB/RE/N120 de Genteca tienen 150ms — solo el GSM-L alcanza 20ms [HECHO verificado en HDE v10 GSM-L].

- **Diferenciador real Genteca:** 20ms de tiempo de detección de flicker publicado en datasheet HDE v10, GSM-L. Es la especificación más agresiva identificada en el segmento de supervisores de voltaje mono/bifásico en esta gama de precio y clase de producto. La competencia industrial (ABB, Siemens, Schneider) tiene productos de protección de calidad de energía de alta gama (analizadores de red, power quality analyzers) con detección de eventos sub-ciclo, pero no son la misma categoría de producto ni el mismo punto de precio ni el mismo mercado (no son protectores enchufables para usuario final residencial). En el segmento directo (supervisor residencial/comercial bajo costo para VE/MX), 20ms es una especificación sin comparativo publicado verificado.

- **Riesgo descriptividad SAPI/IMPI:** Medio. "FlickerGuard" — "Flicker" es término técnico (IEC 61000-4-15 define flicker como fenómeno de calidad de energía); sin embargo, el consumidor venezolano o mexicano promedio no usa "flicker" como descripción del producto — lo llama "parpadeo". "Guard" es un sufijo de protección no descriptivo del mecanismo específico. Bajo doctrina de equivalencia perceptual SAPI, el anglicismo "FlickerGuard" probablemente no es percibido como descriptivo por consumidor promedio. Riesgo medio principalmente porque "guard" aparece en nombres de protectores de otras marcas y hay productos de iluminación LED (Australianos y UK) que usan "Flicker Guard" o "FlickerGuard" como nombre de feature. El charter previo marcó ⚠ búsqueda OMPI ampliada pendiente — esto persiste.

- **Notas para Solenne:** Verificar en bases USPTO/WIPO/IMPI si existe "FlickerGuard" registrado en clase 9 por fabricante de iluminación antes de asumir espacio limpio. La coexistencia con productos LED "flicker guard" en otra subclase puede ser navegable si Genteca registra en la subclase de protección eléctrica para motores/refrigeración. Raíces a explorar si FlickerGuard tiene colisión: Flicker+Trap, Flicker+Block, Flicker+Shield, PulseGuard, SagGuard. Evitar "SagStop", "FlickerStop" — demasiado descriptivo.

---

### NODO C — Modelo térmico integrado NTC (sensor de temperatura en motor)

**Anchor Top 7:** Thermo-Safe

- **Estado competitivo Genteca:** Amarillo
- **Quién más lo tiene:**
  - Siemens SIMOCODE pro 3UF7: módulo de temperatura opcional, soporta NTC, KTY83/84, PT100/PT1000 — llamado "Temperature Module" (nombre descriptivo, no fantástico). [HECHO: catalog SIMOCODE consultado]
  - Schneider TeSys T LTMR: soporta PTC Analog y NTC Analog para temperatura de motor. Sin nombre comercial de fantasía — se llama "Motor Temperature Sensing" function. [HECHO: user guide LTMR consultado]
  - Eaton C440 / C441 Motor Insight: termistor como opción — sin nombre comercial de fantasía identificado. [CLAIM: basado en documentación C440/C441; no confirmado en datasheet específico sesión]
  - ABB REM615 / 3RN2: Siemens 3RN2 dedicado para termistor (PTC). ABB REM615 soporta temperatura. Sin nombre de fantasía en ninguno de los dos. [HECHO parcial: Siemens 3RN2 consultado]
  - Genius GIII / GIII+MV: sensor PTC100 (no NTC) para temperatura. [HECHO: HDE GIII+MV consultado]
  - GSM-MB / RB: la "Protección Térmica" con NTC es la novedad mencionada en el empaque (v10 del label tiene "AHORA CON PROTECCIÓN TÉRMICA"). [HECHO: GSM-MB HDE consultado]

- **Diferenciador real Genteca:** El diferenciador no es el sensor NTC per se — ese hardware lo tienen todos los grandes, aunque en gamas industriales de mayor costo y con configuración separada. El diferenciador de Genteca es la integración del NTC en un protector de voltaje monofásico de uso doméstico/comercial (GSM-MB/RB) como feature estándar (no módulo separado), a un punto de precio de mercado doméstico VE/MX. Siemens requiere un módulo adicional (3UF7 + Temperature Module) que implica costo y cableado adicional. En el segmento de protectores enchufables o de bornera para AC/refrigeración, ningún competidor identificado ofrece NTC integrado como feature estándar de serie. El algoritmo cold/hot que lo complementa es el diferenciador algorítmico (Nodo D).

- **Riesgo descriptividad SAPI/IMPI:** Medio. "Thermo-Safe" — "Thermo" es prefijo genérico en la categoría eléctrica/de protección. "Safe" no es descriptor específico del mecanismo, pero la combinación "Thermo" + "Safe" puede ser percibida como descriptiva de "protección térmica segura" — lo cual describe literalmente la función. La referencia SAPI previa indica que "Thermo-Safe" tiene mejor perfil que "Escudo Térmico NTC" porque "Safe" no es uso cotidiano para protector eléctrico. El BR-2 previo marca ⚠⚠ si NTC aparece en el empaque (el Caso A del proyecto previo), ⚠ si no aparece. Esta distinción persiste en este proyecto.

- **Notas para Solenne:** El espacio "Thermo-" como prefijo está moderadamente saturado en clase 9 (equipos industriales, cables, protectores). Evitar "ThermoGuard", "ThermoShield", "ThermoProtect" — las tres raíces tienen presencia en nombres de productos o marcas europeas. "Thermo-Safe" tiene mejor perfil de registro que esas alternativas, según doctrina SAPI previa. Si Bruna en Phase 3 degrada Thermo-Safe por el Caso A, las alternativas de reemplazo deben partir de raíces no descriptivas: "CoreTemp", "TempCore", "WatchTemp" — aunque todas tienen menor potencia comercial.

---

### NODO D — Modelo térmico algorítmico: curva inversa I-t cold/hot

**Anchor Top 7:** ThermalCurve

- **Estado competitivo Genteca:** Rojo
- **Quién más lo tiene:** Todos los fabricantes industriales relevantes. La curva de disparo inversa I-t (tiempo de disparo inversamente proporcional a la magnitud de la sobrecorriente) es la base normativa de IEC 60947-4-1 (relés de sobrecarga) y IEEE C37.112-1996. La distinción cold/hot (motor frío vs motor caliente al momento del arranque) está documentada en múltiples relés.
  - Siemens 3RB3 (solid-state overload): curva inversa Class 10/20/30 con compensación de temperatura. [HECHO: manual SIRIUS consultado]
  - Eaton C441 Motor Insight: curva inversa I-t, clase térmica ajustable. [CLAIM: basado en documentación C441]
  - Schneider TeSys T LTMR: curva inversa I-t con clase térmica ajustable y thermal memory. [HECHO: user guide LTMR consultado menciona thermal model]
  - Rockwell E300: curva de sobrecarga inversa con thermal memory. [HECHO: E300 user manual referenciado]
  - ABB REM615 / EKIP: imagen térmica con curva inversa. [CLAIM parcial]
  - Genius GIII / GUCT / GOCT: "Thermal Memory" como feature documentado + "thermal model algorithm" en manual GUCT. [HECHO: specs consultadas]
  - Genius GIII+MV: "Thermal memory" — feature documentado. [HECHO: spec sheet consultado]

- **Diferenciador real Genteca:** No hay diferenciador genuinamente único en la función base. Todos los relés industriales de gama media-alta tienen curva inversa I-t y distinción cold/hot o su equivalente funcional. El override del Owner (charter §3 decisión 4) asume que Exceline / Exceline Profesional / Genius tienen esta función universal. El diferenciador de Genteca, si existe, está en el algoritmo específico (no en la curva estándar IEC) — pero ese detalle requiere documentación técnica interna que valide que la implementación tiene algo registrable por encima del estándar. Eso es trabajo de Vera en Phase 1, no trabajo de Orlan.

- **Riesgo descriptividad SAPI/IMPI:** Alto. "ThermalCurve" describe literalmente el mecanismo técnico que cualquier relé de sobrecarga con curva inversa implementa. SAPI puede considerar que el nombre describe una característica técnica estándar de la categoría. El BR-2 previo marca ⚠⚠. Este riesgo se mantiene o aumenta con este análisis — la ubiquidad de la función en la competencia refuerza el argumento de descriptividad.

- **Notas para Solenne:** El espacio "Curve" como sufijo aplicado a protección eléctrica está vacío de marcas de fantasía registradas — pero "ThermalCurve" como combinación es demasiado cercana a la descripción técnica. Si Bruna no puede defender ThermalCurve en Phase 3, las alternativas deben alejarse del espacio semántico de "curva" y "térmica". Posibles territorios: AdaptGuard, ThermoAdapt, SmartClass, MotorState — ninguno tan potente comercialmente como ThermalCurve, pero registrables. La nota al Owner: si la implementación algorítmica de Genteca tiene algo propietario más allá del estándar IEC (por ejemplo, un parámetro de enfriamiento diferencial o un factor cold/hot propio), eso es el RTB que Vera debe documentar para que Bruna pueda defender el nombre. Sin ese RTB, ThermalCurve tiene probabilidad alta de ser rechazado o cuestionado en búsqueda fonética por SAPI.

---

### NODO E — Diagnóstico forense y registro histórico de fallas

**Anchor Top 7:** ForensLog

- **Estado competitivo Genteca:** Amarillo
- **Quién más lo tiene:**
  - Rockwell E300: Trip History de 5 eventos (Parameters 127-131) + Warning History de 5 eventos. Total: 10 registros. [HECHO VERIFICADO: manual E300 193-UM015, ManualsLib]
  - Schneider TeSys T LTMR: registros de fallas (contadores y diagnóstico). El user guide menciona fault statistics y diagnostic fault counters, pero no especifica una capacidad de "últimas N fallas" comparable. [CLAIM parcial: user guide LTMR consultado; número exacto de registros no confirmado en esta sesión]
  - ABB REF615 (gama alta, no motor relay directo): 2048 audit trail events + 1024 process events. Esto es gama de subestación, no motor relay de baja tensión. [HECHO: library.abb.com]
  - ABB REM615 / gama Relion motor: registro de eventos. Número exacto de últimas fallas para motor relay LV no confirmado en esta sesión. [CLAIM]
  - Siemens SIMOCODE 3UF7 / SIPROTEC: registro de eventos vía PROFIBUS. Sin capacidad publicada de "N últimas fallas" en datasheet básico de motor relay. [CLAIM]
  - Eaton C441 Motor Insight: registro de fallas y diagnóstico. Número exacto no confirmado en esta sesión. [CLAIM]
  - Genius GIII (HDE original): "Reporte de Últimas 20 Fallas" — documentado en HDE. [HECHO: spec sheet GIII consultado]
  - Genius GIII+MV: **"100 Last Fault report"** — documentado en spec sheet GIII+MV-V1. [HECHO VERIFICADO: fuente primaria consultada]
  - Genius GSPT-MV (manual): "Histórico de Fallas — Reporte de 80 últimas fallas". [HECHO: manual tecnica-i-gspt-mv consultado]

- **Diferenciador real Genteca:** En el segmento directo de motor relay de baja tensión, 100 registros de fallas (GIII+MV) es el número más alto documentado en esta investigación. Rockwell E300 tiene 5 trips + 5 warnings = 10 registros — una décima parte. El GSPT-MV de Genteca tiene 80. El GIII+MV con 100 es el más completo del portafolio propio y aventaja significativamente al competidor directo identificado (E300). La competencia de gama alta (ABB REF615, Siemens SIPROTEC) tiene más capacidad pero son sistemas de protección de subestación / media tensión, no relés de motor en MCC de baja tensión — no son competidores directos en VE/MX en la misma clase de producto.

- **Riesgo descriptividad SAPI/IMPI:** Bajo-medio. "ForensLog" — "Forensic" + "Log". "Forensic" no es descriptor literal del producto eléctrico. "Log" en español no es término cotidiano. La combinación no describe el producto para el consumidor promedio venezolano o mexicano. Bajo la doctrina de equivalencia perceptual, "ForensLog" tiene perfil de signo de fantasía. El riesgo medio proviene de que "Log" tiene uso creciente en software / apps y podría crear colisión en clase 9 amplia (software).

- **Notas para Solenne:** Verificar si existe "ForensLog" como marca registrada en clase 9 (software, apps de diagnóstico industrial). El concepto forense aplicado a equipo eléctrico es un territorio semántico sin saturación de nombres comerciales en la competencia directa — es espacio disponible. Variantes a explorar si hay colisión: FaultLog, EventLog son demasiado genéricos. Mejores alternativas: ForensTrace, AuditLog (riesgo software también), FaultIndex, DiagLog, FaultVault. Todos tienen menor potencia que ForensLog.

---

### NODO F — Lógica de protección multi-falla / bloqueo escalonado

**Anchor Top 7:** TripleLock

- **Estado competitivo Genteca:** Amarillo
- **Quién más lo tiene:**
  - Genius GSPT / GSC-MB: "3 fallas en menos de 30 min → desconexión permanente (requiere reset manual)". Referenciado en catálogo protección trifásica y manual GSPT. [HECHO: specs consultadas]
  - Schneider TeSys T LTMR: tiene función de "locked rotor" y protecciones con counters, pero no se identificó una función de "tres fallas en ventana de tiempo → bloqueo permanente" con nombre propio. [CLAIM: basado en user guide LTMR]
  - Siemens 3RU/3RB: reseteo manual después de sobrecargas. Sin "triple fault lockout" como feature nombrado. [CLAIM]
  - Eaton C440/C441: trip inhibit functions, pero no se identificó "triple fault" lockout con nombre comercial. [CLAIM]
  - Rockwell E300: Overcurrent Trip Count / "Inhibit Restart" configurable. Sin nombre de fantasía para función triple-falla. [CLAIM basado en E300 user manual general]
  - ABB: función de restart inhibit en algunos relés. Sin nombre comercial de fantasía identificado. [CLAIM]
  - Chint/Lovato/LS: relés básicos con reseteo manual automático, sin función de conteo de fallas con bloqueo escalonado documentada con nombre comercial. [CLAIM general]

- **Diferenciador real Genteca:** La función de "3 fallas en ventana de tiempo corta → desconexión permanente que requiere intervención técnica deliberada" existe en Genteca y protege contra ciclos destructivos de falla-rearranque. En la competencia industrial, una función equivalente existe como "inhibit restart" o "trip counter" configurable, pero sin nombre de fantasía propio — es solo un parámetro ajustable, no un feature diferenciador con identidad de marca. Genteca puede reclamar la función con nombre y posicionarla como feature premium en la gama Genius. La diferencia cualitativa de Genteca es que el bloqueo es automático y el nombre lo convierte en feature visible, no en configuración oculta.

- **Riesgo descriptividad SAPI/IMPI:** Medio. "TripleLock" — "Triple" es número descriptor (tres), "Lock" es cierre/bloqueo. La combinación es moderadamente descriptiva de "bloqueo tras tres eventos". No es una descripción literal que el consumidor promedio usaría, pero un examinador técnico podría argumentar que describe la función. El riesgo es mayor que ForensLog pero menor que ThermalCurve. El BR-2 previo marca ⚠ búsqueda sectorial seguridad física — esto persiste porque "lock" en seguridad física es espacio saturado.

- **Notas para Solenne:** Verificar colisión de "TripleLock" en clase 9 con fabricantes de sistemas de seguridad física (candados electrónicos, cerraduras digitales). Si hay colisión, alternativas: SequenceLock, FaultGate, SafeStop (demasiado genérico), TripBlock, SafeHold, LockSequence. La raíz "Lock" es el problema — explorar alternativas con "Gate", "Hold", "Block" que tienen menos presencia en seguridad física.

---

### NODO G — Memoria de estado y recuperación de tarea

**Anchor Top 7:** TaskMemory

- **Estado competitivo Genteca:** Verde
- **Quién más lo tiene:** No se identificó ningún fabricante de la lista obligatoria con una función equivalente documentada con nombre comercial en el segmento de controladores de nivel/bombeo residencial-comercial.
  - Catálogo comercial Genteca: "GRN-MV — Relé de nivel para líquidos conductores. Memoriza tarea al ocurrir falla." [HECHO: catálogo comercial consultado]
  - HDE GRN-MV v9: "retoma automáticamente la última tarea" post-corte. [HECHO: HDE consultada]
  - ABB / Siemens / Schneider / Eaton: sus controladores de bombeo (si los tienen) son PLCs o drives programables con memoria de estado implícita en el programa del usuario — no es una función diferenciadora nombrada en relés de nivel para bombeo básico. [CLAIM general]
  - Rockwell / Chint / Lovato: no tienen equivalente identificado de "task memory" en controladores de nivel residencial/comercial. [CLAIM]
  - Controladores de bombeo asiáticos básicos: típicamente no tienen esta función — el relé de nivel estándar simplemente activa/desactiva según el nivel actual al restaurar la energía, sin recordar el modo previo. [CLAIM basado en conocimiento del segmento]

- **Diferenciador real Genteca:** La función de persistencia de modo operativo post-corte en un controlador de nivel/bombeo de gama media es una diferenciación real. El GRN-MV tiene 3 modos (vaciado pozo / llenado tanque / vaciado tanque) y recuerda en cuál estaba cuando hubo el corte. Esto elimina la necesidad de supervisión humana en el reencendido — el beneficio del beneficio L2 del AU-1 mapping es preciso: el proceso no pierde el ciclo. En VE/MX donde los cortes eléctricos son frecuentes, esto es un diferenciador operativo real. La competencia no tiene un equivalente nombrado en este tipo de producto.

- **Riesgo descriptividad SAPI/IMPI:** Medio-alto. "TaskMemory" — "Task" es tarea (descriptor funcional) y "Memory" es memoria (descriptor del mecanismo). Ambas palabras son descriptivas en inglés del mecanismo técnico. El riesgo proviene de que la combinación describe bastante literalmente la función para un hablante de inglés técnico. Sin embargo, bajo la doctrina SAPI de equivalencia perceptual, el consumidor venezolano promedio (audiencia: dueño de equipo de riego/bombeo, no ingeniero) no necesariamente percibe "TaskMemory" como descriptor literal — puede funcionar como signo de fantasía. El riesgo mayor identificado en el BR-2 previo es de colisión con clase 9 software/apps: "task memory manager" es término de gestión de procesos en informática. Verificación de colisión en clase 9 sofware es crítica.

- **Notas para Solenne:** La colisión con software (clase 9 amplia) es el riesgo más relevante, no la descriptividad del producto eléctrico. En SAPI VE la doctrina de equivalencia perceptual puede protegerlo para el producto eléctrico. En IMPI MX la búsqueda debe verificar colisión con apps o software de gestión de tareas con "Task Memory" como feature. Si hay colisión, alternativas con raíces más distanciadas del vocabulario software: ModeKeep, CycleMemory (similar riesgo), StateHold, CycleResume, RetainMode, ResumeMode. Ninguna tan potente como TaskMemory pero más limpias en clase 9 software.

---

### NODO H — Supervisión trifásica integral monobloc para motores/sistemas

*[Slot abierto — evaluado como candidato de Orlan]*

**Función:** Los productos GST-RR y GST-RM de Genteca (Exceline Profesional) supervisan 8 tipos de falla trifásica (OV/UV/desbalance/pérdida de fase/fase invertida/variación de frecuencia) en un solo dispositivo de riel DIN.

- **Estado competitivo Genteca:** Amarillo
- **Quién más lo tiene:** Todos los grandes tienen supervisores trifásicos equivalentes:
  - ABB CM-MPN / CM-MPS: monitoreo trifásico. [HECHO: familia CM-range consultada]
  - Siemens GI+ equivalente: la línea GI+/GII+ de Genius de Genteca ya cubre este espacio. En la competencia, Siemens 3UF7 SIMOCODE y los supervisores CM de ABB son el equivalente.
  - Schneider GST-RR equivalente: múltiples productos en la familia TeSys.
  - Chint NJYB2: supervisor trifásico OV/UV/fase perdida/secuencia. [HECHO: producto consultado]

- **Evaluación como nodo independiente:** Esta función no tiene diferenciador suficiente para ser un nodo registrable independiente en el inventario de naming. Es la base del portafolio trifásico, no un algoritmo propietary. **Recomendación Orlan: no registrar como nodo independiente H.** Si Vera identifica un algoritmo específico dentro de la supervisión trifásica (por ejemplo, la velocidad de detección de pérdida de fase o un parámetro de desequilibrio diferenciado), eso podría ser un nodo. Pero la función genérica de "supervisión trifásica" no lo es.

- **Riesgo descriptividad SAPI/IMPI:** Alto. Cualquier nombre para esta función sería descriptivo de la categoría.

- **Notas para Solenne:** No se recomienda un candidato de naming para este nodo hasta que Vera identifique un algoritmo o parámetro específico diferenciador dentro de la supervisión trifásica. Si Vera lo fusiona con otro nodo, este slot H se cierra.

---

### NODO I — Comunicación Modbus RTU nativa en gama media (sin módulo adicional)

*[Slot abierto — evaluado como candidato de Orlan]*

**Función:** Los productos Genius GI+/GII+/GIII+/GSPT tienen comunicación Modbus RTU integrada de serie (no módulo separado). En la competencia, Modbus generalmente requiere módulo adicional.

- **Estado competitivo Genteca:** Amarillo (en declive)
- **Quién más lo tiene:**
  - Siemens SIMOCODE 3UF7: comunicación via módulo separado (PROFIBUS, Ethernet — no Modbus nativo de base). [HECHO: catalog SIMOCODE consultado]
  - Eaton C440/C441: Modbus disponible pero vía módulo C440/XTOE Modbus. [HECHO: user manual C440/XTOE Modbus consultado]
  - Rockwell E300: EtherNet/IP, DeviceNet — Modbus no es su protocolo primario. [CLAIM]
  - Schneider TeSys T: RS485 Modbus disponible. Integración nativa en modelos LTM. [CLAIM parcial]
  - Chint/Lovato/LS: en sus relés básicos, Modbus no es estándar. En gamas superiores, algunos modelos soportan comunicación. [CLAIM]

- **Evaluación como nodo independiente:** La presencia de Modbus nativo en Genius es un diferenciador del segmento LatAm donde la conectividad en relés básicos no está dada por sentado, pero en el mercado global es un feature que la competencia también ofrece. No tiene suficiente diferenciación registrable para un nodo de naming. **Recomendación Orlan: no registrar como nodo independiente I.** Si Vera identifica un algoritmo de comunicación propietario (por ejemplo, protocolo GIO-Link) que sea diferenciador registrable, podría ser candidato. GIO-Link ya es un nombre de producto en uso — verificar si está registrado como marca.

- **Riesgo descriptividad SAPI/IMPI:** Alto para cualquier nombre relacionado con comunicación/conectividad en clase 9.

- **Notas para Solenne:** GIO-Link existe como nombre de producto Genteca (accesorio para comunicación). Verificar si está o puede registrarse como marca de componente. Si está en uso comercial, TM puede aplicarse desde ya.

---

## Espacio semántico saturado (resumen para Solenne)

### Raíces y combinaciones a evitar o navegar con cuidado

| Raíz / combinación | Razón de precaución | Alternativa viable |
|--------------------|---------------------|-------------------|
| "Thermal" + [sufijo] | Saturado en clase 9 industrial (ThermoShield, ThermoGuard, etc. en equipos EU/USA) | Nombres con raíz no térmica para NODO C |
| "Curve" aplicado a relés | Descriptivo del mecanismo IEC estándar | Alejarse de "Curve" para NODO D |
| "Restart" / "Reconnect" solo | Descriptivo funcional puro | Combinar con raíz no inglesa cotidiana |
| "Lock" (seguridad física) | Saturado en apps y cerraduras digitales clase 9 | "Gate", "Hold", "Block" menos saturados |
| "Log" solo | Término genérico de software en clase 9 | Combinar con raíz no software (ForensLog es viable; LogSafe no) |
| "Voltage Loss Restart" | Nombre Eaton — descriptivo, no registrado como fantasía pero potencial claim de prioridad de uso | Sin riesgo de colisión de marca; es claim funcional genérico |
| "Temperature Module" | Nombre Siemens SIMOCODE — descriptivo, no de fantasía | No registrado como marca registrada |
| "Motor Insight" | Nombre comercial Eaton C441 | Evitar combinaciones con "Insight" en clase 9 |
| "SIMOCODE" | Marca Siemens registrada | No usar raíz "SIMO" |
| "TeSys" | Marca Schneider registrada | No usar raíz "TeSys" |
| "EcoStruxure" | Marca Schneider registrada | No usar "Eco" + "Strux" combinado |
| "Power Xpert" | Marca Eaton registrada | No usar "Xpert" en combinación con "Power" |

### Observación de conjunto

Ninguno de los 7 anchor names de Genteca (StaggerStart, ForensLog, FlickerGuard, Thermo-Safe, TripleLock, TaskMemory, ThermalCurve) es nombre comercial de ningún competidor identificado en la investigación de esta sesión. El espacio semántico de fantasía para los 7 está técnicamente disponible en cuanto a colisión con marcas de la competencia directa. Los riesgos son de:
1. Colisión con marcas de otros sectores en clase 9 (software, seguridad física, iluminación)
2. Descriptividad de la propia función en SAPI/IMPI (aplica principalmente a ThermalCurve y en menor grado a TripleLock y TaskMemory)

---

## Notas de discrepancia y pendientes

### Discrepancia importante para Vera

El GIII+ estándar tiene "Reporte de Últimas 20 Fallas" (HDE biblioteca técnica). El GIII+MV tiene "100 Last Fault report" (spec sheet GIII+MV-V1). El GSPT-MV tiene 80 fallas (manual). Los tres son productos Genius distintos. El anchor ForensLog menciona "100-Fault Forensic History" — esto es correcto solo para GIII+MV, no para todos los GIII+. **Vera debe confirmar si el inventario híbrido especifica GIII+MV como el portador del nodo ForensLog, o si GIII+ (con solo 20) también se incluye bajo el mismo nombre.** Si se incluyen ambos, el RTB "100 fallas" no es universal para el nodo.

### Discrepancia en sensor de temperatura

El GIII+ y GIII+MV usan sensor PTC100 (platino), no NTC. El GSM-MB/RB usa NTC. Son dos familias con distinto hardware de sensor de temperatura. Vera debe definir si Thermo-Safe (NODO C) describe el NTC del GSM-MB/RB únicamente, o incluye también la protección de temperatura del GIII+ (PTC). Si los fusiona, el claim de "NTC" debe ser del GSM-MB/RB exclusivamente para ser factual.

### Slots H e I

Orlan recomienda no registrar nodos H e I como candidatos independientes con los datos disponibles. Si Vera identifica en el inventario híbrido un algoritmo diferenciador dentro de supervisión trifásica o de comunicación que cambie esta evaluación, Orlan ajusta en Phase 5.

### Datos marcados como CLAIM

Varios hallazgos de la competencia en esta matrix están marcados [CLAIM] — son inferencias de conocimiento técnico general o de documentación de alto nivel, no verificaciones contra datasheet primario en esta sesión. Para el Anexo Técnico de Phase 5, estos claims deben convertirse en verificaciones contra fuente primaria (datasheet o manual) o eliminarse. Se listan explícitamente para que Vera / Owner sepan qué necesita refuerzo antes de presentar al abogado.

Los Claims que tienen mayor impacto en el posicionamiento:
- Rockwell E300: 5 trip records (impacto NODO E) — [HECHO verificado, sí confiable]
- Schneider LTMR NTC/PTC support — [HECHO verificado, sí confiable]
- Siemens SIMOCODE NTC module — [HECHO verificado, sí confiable]
- Eaton C445 staggered restart — [HECHO verificado, nombre "Voltage Loss Restart" confirmado]
- Eaton C440/C441 fault log capacity — [CLAIM, no confirmado en esta sesión]
- Siemens SIMOCODE fault log capacity — [CLAIM, no confirmado en esta sesión]

---

## Mini-cover note

### Archivos producidos

`C:\Raul\03-projects\genteca\portfolio-naming-ip-2026\02-vera-orlan\Orlan_OL-1_differentiation-matrix_v1.md`

### Hallazgos críticos para el Owner

1. **ThermalCurve (NODO D) es rojo — confirmado.** La ubiquidad de la curva inversa I-t en toda la competencia industrial refuerza el riesgo de descriptividad del nombre. Sin RTB algorítmico específico que Vera documente, ThermalCurve tiene probabilidad alta de rechazo o cuestionamiento en SAPI/IMPI. Bruna debe considerar esto en Phase 3 con postura fuerte de "ajustar o reemplazar".

2. **FlickerGuard (NODO B) es verde, pero hay una colisión potencial a verificar.** La especificación 20ms del GSM-L es única en el segmento identificado. Sin embargo, en Australia y UK existen productos LED con el nombre "FlickerGuard" / "Flicker Guard". No están en clase 9 de protección eléctrica para motores, pero la coexistencia debe ser evaluada por el abogado marcario. La búsqueda OMPI que el proyecto previo marcó como pendiente sigue siendo crítica.

3. **ForensLog: 100 fallas es hecho verificado solo para GIII+MV, no para todos los GIII+.** Esta distinción afecta el RTB del claim "100-Fault". Vera debe confirmar el alcance del nodo.

4. **Eaton tiene un nombre para la función StaggerStart:** "Voltage Loss Restart". No es una marca de fantasía registrada — es un claim descriptivo. Esto confirma que el espacio de fantasía para "StaggerStart" está limpio de colisión con nombres de competencia. Ventaja para Solenne.

5. **Nodos H e I no se recomiendan como candidatos independientes** con los datos actuales. El portafolio queda en 7 nodos (A-G), dentro del rango objetivo de 6-9.

### Inputs que pasan a Vael / Bruna / Solenne

- **A Vael (Phase 2):** Los nodos verdes (B, G) tienen el diferenciador más fuerte — el messaging debe construirse sobre la especificación verificable (20ms para B, memoria de tarea post-corte para G). Los nodos amarillos (A, C, E, F) requieren messaging que enfatice la ejecución en el segmento, no la función per se.
- **A Bruna (Phase 3):** NODO D (ThermalCurve) requiere atención prioritaria — el gate de Bruna debe ser específico sobre si el override universal del Owner es suficiente para sostener el nombre o si se necesita RTB diferenciador de Vera. NODO C (Thermo-Safe) tiene el Caso A/B pendiente de resolver (NTC en empaque o no).
- **A Solenne (Phase 4):** Espacio limpio para los 7 anchor names — ninguno colisiona con nombres de la competencia directa (ABB/Siemens/Schneider/Eaton/Rockwell/Chint/Lovato/LS). Los riesgos son de otros sectores en clase 9. Ver tabla de espacio saturado. ThermalCurve tiene el riesgo más alto; si Bruna lo degrada a ❌, el reemplazo debe partir de raíz no descriptiva.

### Fact vs Claim

| Dato | Status |
|------|--------|
| GSM-L: 20ms flicker detection | HECHO — HDE v10 fuente primaria |
| GIII+MV: 100 Last Fault report | HECHO — spec sheet GIII+MV-V1 fuente primaria |
| GIII+: 20 Last Fault (estándar) | HECHO — HDE biblioteca técnica |
| GSPT-MV: 80 fallas | HECHO — manual tecnica-i-gspt-mv |
| GSM-MB/RB: NTC integrado | HECHO — label/empaque v10 |
| GRN-MV: memoriza tarea post-corte | HECHO — catálogo comercial + HDE v9 |
| Genius GUCT/GIII: thermal model algorithm | HECHO — manual GUCT consultado |
| Eaton C445: "Voltage Loss Restart" staggered | HECHO — application note oficial Eaton |
| Rockwell E300: 5 trip records + 5 warning records | HECHO — manual E300 193-UM015 |
| Siemens SIMOCODE 3UF7: Temperature Module (NTC/KTY/PT100) | HECHO — catalog SIMOCODE consultado |
| Schneider LTMR: NTC/PTC support | HECHO — user guide LTMR consultado |
| Eaton C441: fault log capacity | CLAIM — no verificado en datasheet primario esta sesión |
| Siemens SIMOCODE: fault log capacity | CLAIM — no verificado |
| Siemens 3RU/3RB: curva inversa cold/hot | CLAIM basado en manual; IEC estándar asumido |
| Chint/Lovato/LS: sin staggered reconnect nombrado | CLAIM general |

### Preguntas abiertas al Owner

Cero preguntas abiertas que bloqueen Phase 1. Las discrepancias (ForensLog 20 vs 100 fallas, sensor NTC vs PTC) se resuelven en la reconciliación Vera+Orlan de Phase 5 o en la confirmación de Vera al cerrar su inventario en Checkpoint 1.

---

*Orlan — Phase 1 completa. Listo para Checkpoint 1 Owner junto con output de Vera.*
