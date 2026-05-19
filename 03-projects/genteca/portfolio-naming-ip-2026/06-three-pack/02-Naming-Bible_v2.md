---
doc_type: naming-bible
project_id: portfolio-naming-ip-2026
domain: genteca
version: v2.0
author: Equipo IP Genteca
fecha: 2026-05-13
total_candidates: 32 base + 7 contingencias (2 NODO-B OMPI, 2 NODO-F sectorial, 3 NODO-G IMPI MX)
---

# Naming Bible — Portfolio IP 2026 (Genteca)

**Fecha:** 2026-05-13

---

## Sección 1 — Resumen ejecutivo

### 1.1 Candidatos generados

- **32 candidatos base** (8 nodos × 4 candidatos)
- **7 candidatos de contingencia:**
  - 2 para NODO-B (contingencia OMPI colisión FlickerGuard con productos LED)
  - 2 para NODO-F (contingencia sectorial colisión TripleLock en seguridad física)
  - 3 para NODO-G (candidatos alternativos específicamente para IMPI MX)
- **Total en documento:** 39 entradas

### 1.2 Anchors Top 7 post-revisión interna de propiedad intelectual

| Anchor | Nodo | Estado |
|--------|------|--------|
| StaggerStart | NODO-A | Preservado — carry-over sin modificación. Candidato 1 de NODO-A. |
| FlickerGuard | NODO-B | Preservado — candidato principal. Contingencia OMPI lista. |
| Thermo-Safe | NODO-C | Preservado — caveat Caso A integrado. Candidato 1 de NODO-C. |
| ForensLog | NODO-E | Preservado — Escenario A (GIII+MV como RTB principal). Candidato 1 de NODO-E. |
| TripleLock | NODO-F | Preservado — candidato principal. Contingencia sectorial lista. |
| TaskMemory | NODO-G | Preservado para SAPI VE. Contingencia IMPI MX lista. |
| ThermalCurve | NODO-D | **RECHAZADO en revisión interna de propiedad intelectual.** 4 candidatos nuevos generados. |

**6 de 7 anchors sobreviven.** ThermalCurve cae. NODO-D tiene 4 candidatos completamente nuevos. NODO-H (Ecosystem GIO) tampoco tiene anchor previo — 4 candidatos nuevos en familia GIO.

### 1.3 Decisión ForensLog — Escenario A vs B

**Postura adoptada en revisión interna: Escenario A — acotar el RTB del nombre al GIII+MV.**

Rationale: el equipo de propiedad intelectual interno adopta el Escenario A porque el argumento es sólido: el RTB "100 fallas con timestamp" del GIII+MV es verificado en HDE primaria, el comparativo 10:1 vs Rockwell E300 es hecho confirmado, y el argumento ante el abogado es limpio y cuantificable. El Escenario B (ampliar a gama Genius entera con RTB "hasta 100 fallas / 20 fallas según producto") debilita la posición sin ventaja de naming equivalente: el nombre ForensLog no gana potencia al ampliarse y el RTB declarado se vuelve ambiguo para el examinador. El nombre ForensLog evoca registro forense — esa connotación es suficientemente específica para el GIII+MV sin necesitar extenderse a toda la gama. Si en el futuro toda la gama Genius sube a 100 fallas, el nombre aplica naturalmente.

**Impacto en messaging:** La celda C de NODO-E en el documento de arquitectura de mensajes permanece con "hasta 100 últimas fallas (GIII+MV)". No se requiere actualización — el Escenario A es compatible con el texto vigente.

### 1.4 Distribución por línea comercial

| Línea | Nodos | Candidatos base |
|-------|-------|----------------|
| Exceline residencial + comercio | NODO-A (StaggerStart), NODO-B (FlickerGuard), NODO-C (Thermo-Safe) | 12 |
| Exceline Profesional / industrial | NODO-D (curva cold/hot), NODO-F (TripleLock), NODO-G (TaskMemory) | 12 |
| Genius premium / especificadores | NODO-D (también), NODO-E (ForensLog), NODO-H (Ecosystem GIO) | 8 |
| Total | 8 nodos | 32 |

*Nota: NODO-D tiene audiencia primaria Exceline Profesional/Genius; NODO-E y NODO-H son Genius/especificadores.*

---

## Sección 2 — Tabla maestra

> **Factibilidad:** ✅ limpia / ⚠ moderada con caveat (causa en 1 línea) / ❌ no recomendable.
> **Status:** `anchor` (carry-over Top 7 confirmado en revisión interna de propiedad intelectual) / `nuevo` (generado en revisión interna) / `contingencia` (alternativa por colisión — no parte de los 32 base).

| # | Nodo | Candidato | Status | Audiencia primaria | Beneficio comercial clave | Beneficio del beneficio (L2) | Sufijo / patrón morfológico | Factibilidad SAPI VE | Factibilidad IMPI MX | Racional anglicismo | Riesgo identificado |
|---|------|-----------|--------|-------------------|--------------------------|-----------------------------|-----------------------------|----------------------|----------------------|--------------------|--------------------|
| 1 | NODO-A | **StaggerStart** | anchor | Exceline residencial + Profesional | Retardo de reconexión aleatorio — previene pico de demanda simultáneo | El compresor no recibe el golpe eléctrico junto con todos los demás | Raíz técnica (Stagger) + acción (Start) | ✅ | ✅ | "Stagger" evoca escalonamiento técnico; raramente usado en nombres clase 9 LatAm; "Start" cierra con la acción de reconexión. Combinación no descriptiva para consumidor venezolano promedio. | Ninguno identificado. |
| 2 | NODO-A | **CascadeStart** | nuevo | Exceline residencial + Profesional | Reconexión ordenada en cascada — múltiples unidades no arrancan juntas | El sistema de AC de la instalación no colapsa en el reencendido post-apagón | Raíz de flujo ordenado (Cascade) + acción (Start) | ✅ | ✅ | "Cascade" evoca secuencia ordenada sin ser descriptor literal; "Start" anclado en la acción. Pronunciable en español (cas-keid). Espacio semántico no saturado en clase 9 protección. | Bajo. "Cascade" tiene uso en electrónica pero no como nombre de marca registrada en protectores. |
| 3 | NODO-A | **SeqGuard** | nuevo | Exceline Profesional + Exceline residencial | Secuenciamiento controlado del arranque — sin pico de demanda | El equipo industrial no cicla entre arranques desordenados post-falla | Raíz de secuencia (Seq) + defensiva (Guard) | ✅ | ✅ | "Seq" abrevia sequence — término técnico de control de procesos. "Guard" cierra con rol defensivo. Brevedad fonética: 3 sílabas. No descriptivo para consumidor no técnico. | Bajo. Verificar que "Seq" no esté registrado como marca de software (contexto de secuenciamiento de tareas en SW). |
| 4 | NODO-A | **PhaseStart** | nuevo | Exceline Profesional + especificadores | Arranque por fases temporales — prevención de sobrecarga en reconexión | Los equipos de una instalación no saturan la red eléctrica en el reencendido conjunto | Raíz de distribución temporal (Phase) + acción (Start) | ⚠ | ⚠ | "Phase" tiene uso doble: fase eléctrica (descriptor técnico) y fase temporal (menos descriptivo). Como nombre de marca, la combinación "PhaseStart" evoca arranque por fases en el tiempo, no la medición de fase eléctrica. Riesgo descriptividad moderado porque "phase" aparece en muchos productos eléctricos. | Descriptividad moderada: "phase" en eléctrico puede ser interpretado como descriptor. Evaluar si el abogado prefiere candidato con menor riesgo. |
| 5 | NODO-B | **FlickerGuard** | anchor | Exceline residencial | Detección de flicker en 20ms antes de que el estrés llegue al motor | El compresor del AC o refrigerador no se daña por arranques forzados por parpadeo eléctrico | Raíz del fenómeno (Flicker) + defensiva (Guard) | ⚠ | ⚠ | "Flicker" es técnico (IEC 61000-4-15), no cotidiano venezolano/mexicano. "Guard" evoca defensa sin describir el mecanismo. Bajo doctrina equivalencia perceptual SAPI, la combinación funciona como fantasía. | Colisión potencial con productos LED (Australia/UK) usando "FlickerGuard" como nombre de feature — búsqueda OMPI pendiente (caveat en deck). Si búsqueda confirma conflicto activo en SAPI/IMPI, activar contingencias. |
| 6 | NODO-B | **SagShield** | nuevo | Exceline residencial | Protección ante caídas de voltaje sub-ciclo — el equipo no absorbe el estrés de eventos rápidos | El compresor no opera bajo tensión eléctrica anormal sin protección | Raíz del fenómeno (Sag = caída de voltaje) + defensiva (Shield) | ✅ | ✅ | "Sag" es término técnico de calidad de energía (voltage sag — IEC 61000-4-11); "Shield" evoca escudo de protección. Combinación técnica sin saturación en clase 9 para protectores de motor residencial. | Bajo. "Shield" tiene presencia en clase 9 pero no en combinación con "Sag" en el segmento de protectores de motor residencial. |
| 7 | NODO-B | **PulseBlock** | nuevo | Exceline Profesional + residencial | Bloqueo ante pulsos eléctricos anómalos — detección de perturbaciones transitorias | El motor no absorbe el impacto de transitorios eléctricos rápidos | Raíz de señal eléctrica (Pulse) + defensiva (Block) | ✅ | ✅ | "Pulse" evoca señal eléctrica impulsiva (transitorio); "Block" evoca bloqueo activo de ese evento. Más técnico que FlickerGuard pero con potencia fonética similar. 3 sílabas, consonantes duras. | Bajo. Verificar "PulseBlock" en clase 9 software (aplicaciones de síntesis de audio usan "pulse" — contexto muy distinto). |
| 8 | NODO-B | **SpurGuard** | nuevo | Exceline residencial + Profesional | Defensa ante perturbaciones eléctricas transitorias de alta frecuencia | El motor protegido no sufre el desgaste eléctrico de los transitorios no detectados | Raíz técnica de transitorio (Spur = perturbación eléctrica espuria) + defensiva (Guard) | ✅ | ✅ | "Spur" en electrónica describe señal espuria o perturbación indeseada; evoca con precisión las perturbaciones sub-ciclo sin ser término cotidiano. "Guard" cierra con rol defensivo. | Bajo. "Spur" tiene uso en contexto mecánico (piñón) y electrónico; ninguna colisión identificada en nombres de protectores clase 9. |
| 9 | NODO-B | **SpikeShield** | contingencia OMPI | Exceline residencial | Protección ante picos de voltaje transitorios | El compresor del AC no se daña por la energía acumulada en el pico eléctrico | Raíz del evento (Spike = pico eléctrico) + defensiva (Shield) | ✅ | ✅ | "Spike" es ampliamente reconocido en electrónica como evento de pico de voltaje; "Shield" es defensa. Combinación sin saturación como marca en protectores de motor clase 9. Activar si FlickerGuard tiene colisión confirmada en SAPI/IMPI. | Contingencia — no evaluar como candidato principal. |
| 10 | NODO-B | **SagGuard** | contingencia OMPI | Exceline residencial | Protección ante caídas de voltaje que provocan arranque forzado del motor | El refrigerador no se daña por los arranques en tensión insuficiente | Raíz del fenómeno (Sag) + defensiva (Guard) | ✅ | ✅ | "Sag" como raíz de caída de voltaje es más limpia en OMPI que "Flicker" (menor presencia en iluminación). "Guard" compatible. Activar si FlickerGuard tiene colisión confirmada. | Contingencia — activar solo si búsqueda confirma colisión activa de FlickerGuard. |
| 11 | NODO-C | **Thermo-Safe** | anchor | Exceline residencial + Profesional | Sensor NTC embebido en el protector — sin módulo adicional | El motor no se quema por sobrecalentamiento encubierto que la protección normal no detecta | Prefijo del dominio físico (Thermo-) + atributo de estado (Safe) | ⚠ | ⚠ | "Thermo" como prefijo es raíz técnica de temperatura; "Safe" evoca protección sin ser descriptor de mecanismo. Bajo doctrina equivalencia perceptual SAPI, la combinación es fantasía — el consumidor no percibe "Thermo-Safe" como descriptor de "protección térmica". | Descriptividad moderada (Caso A asumido). El abogado lleva argumento de distinción semántica vs descripción funcional en empaque. Caveat aplicable más abajo. |
| 12 | NODO-C | **CoreSafe** | nuevo | Exceline residencial + Profesional | Protección del núcleo térmico del motor — integrada en el protector | El motor no pierde vida útil por ciclos de temperatura no detectada | Raíz de completitud/núcleo (Core) + atributo de estado (Safe) | ✅ | ✅ | "Core" evoca núcleo, centro, el corazón del sistema — aplicado a protección sugiere que la protección llega hasta el núcleo del motor. Sin "Thermo" no crea riesgo de descriptividad térmica. Alejado del territorio rechazado. | Bajo. "Core" tiene saturación como prefijo genérico en software pero como raíz de nombre en hardware eléctrico la combinación "CoreSafe" está limpia. |
| 13 | NODO-C | **WarmWatch** | nuevo | Exceline residencial | Vigilancia activa de la temperatura del motor | El motor de la nevera o el AC no se sobrecalienta silenciosamente — el protector está mirando | Raíz del fenómeno (Warm = calor moderado antes del daño) + diagnóstico (Watch) | ✅ | ✅ | "Warm" evoca temperatura en ascenso antes del daño (no el daño en sí) — connotación de prevención activa. "Watch" implica vigilancia continua sin prometer precisión cuantitativa (compatible con gap NTC en HDE). Pronunciable en español. | Bajo. La combinación WarmWatch no aparece en nombres de marcas clase 9 en protectores de motor. Verificar apps de monitoreo térmico en clase 9 software. |
| 14 | NODO-C | **HeatSeal** | nuevo | Exceline residencial + Profesional | Sellado de la protección contra el calor excesivo del motor | El motor no entra en zona de daño por temperatura porque el protector sella la fuga térmica | Raíz del fenómeno (Heat = calor) + acción de cierre (Seal) | ⚠ | ⚠ | "Heat" describe el fenómeno físico pero "Seal" lo convierte en nombre de acción, no de función técnica. "HeatSeal" evoca protección de integridad ante calor — no descriptor literal del mecanismo NTC. Riesgo moderado porque "heat" es cotidiano y puede rozar la descriptividad. | "Heat" como raíz puede ser objetado como descriptivo del fenómeno físico en un protector térmico. La cercanía semántica con el territorio de NODO-D hace aconsejable que el abogado evalúe. Preferir CoreSafe o WarmWatch si hay duda. |
| 15 | NODO-D | **StateGuard** | nuevo | Exceline Profesional + especificadores Genius | Protección adaptada al estado térmico real del motor — frío o caliente al arranque | El motor industrial no dispara de forma prematura en arranque en caliente ni queda desprotegido en arranque en frío | Raíz del estado (State = condición del motor) + defensiva (Guard) | ✅ | ✅ | "State" evoca el estado actual del sistema (estado frío vs caliente del motor), no el mecanismo IEC. "Guard" cierra con rol defensivo. La combinación "StateGuard" no nombra la curva algorítmica — nombra la respuesta al estado. | Ninguno identificado en el territorio de protección de motores. Verificar clase 9 software (gestión de estados de sistemas — "state guard" puede existir en contextos de máquinas de estado finito). |
| 16 | NODO-D | **AdaptShield** | nuevo | Exceline Profesional + especificadores Genius | Protección que se adapta al punto de operación del motor | El motor no recibe la misma curva de protección en frío y en caliente — el disparo llega cuando el motor lo necesita | Raíz de adaptación (Adapt) + defensiva (Shield) | ✅ | ✅ | "Adapt" como raíz evoca respuesta proporcional al estado sin nombrar el mecanismo IEC. En combinación "Adapt+Shield" la raíz no está sola — aplica la función defensiva. Distingue la función como adaptativa, no como curva estándar. | Bajo. Verificar que "AdaptShield" no colisione con marcas de protección industrial en clase 9 (campo de ropa protectora usa "Adapt" pero en clase diferente). |
| 17 | NODO-D | **MotorState** | nuevo | Especificadores técnicos + Exceline Profesional | El algoritmo opera sobre el estado real del motor, no sobre un patrón fijo | Los ciclos de trabajo del motor industrial son respetados por una protección que sabe si el motor arrancó en frío o en caliente | Raíz del objeto (Motor) + estado (State) | ⚠ | ⚠ | "MotorState" es técnicamente preciso para especificadores: describe que la protección opera sobre el estado del motor, no sobre la corriente sola. Riesgo moderado: "Motor" puede ser considerado descriptor de la categoría del producto (protector de motor). Bajo doctrina equivalencia perceptual puede ser fantasía, pero el abogado debe evaluarlo. | "Motor" como componente de nombre en clase 9 de protección de motores puede ser objetado como descriptivo de la categoría. Alternativa más limpia: StateGuard. Si StateGuard es preferido, MotorState es backup. |
| 18 | NODO-D | **RunState** | nuevo | Exceline Profesional + especificadores | Protección calibrada según el estado de operación del motor al arranque | El motor de planta no corre el riesgo de un disparo inadecuado porque la protección sabe si arrancó en frío o en caliente | Raíz de operación (Run = funcionamiento / ciclo de operación) + estado (State) | ✅ | ✅ | "Run" evoca ciclo de operación activa del motor; "State" refuerza la lectura de estado operativo. La combinación es técnicamente evocadora sin ser un descriptor literal del mecanismo IEC. CamelCase limpio, 3 sílabas, consonantes duras. | Bajo. Verificar "RunState" en clase 9 software (existe como término en programación de máquinas de estado, pero no como nombre de marca registrado en protección eléctrica identificado). |
| 19 | NODO-E | **ForensLog** | anchor | Exceline Profesional + especificadores Genius | Registro de hasta 100 eventos de falla con timestamp, valor medido y parámetros activos (GIII+MV) | El técnico reconstruye el historial de fallas exacto sin depender del operador — diagnóstico preciso, menos tiempo fuera de servicio | Raíz conceptual de análisis (Forens = forense) + soporte de registro (Log) | ✅ | ⚠ | "Forensic" en naming evoca análisis de evidencia — no uso cotidiano venezolano/mexicano. "Log" es registro; no descriptor para el consumidor no técnico de la función del relé. Combinación con perfil de fantasía bajo equivalencia perceptual. | IMPI MX: "Log" en clase 9 software puede crear colisión. Escenario A (RTB anclado en GIII+MV) reduce la ambigüedad del claim. |
| 20 | NODO-E | **FaultVault** | nuevo | Especificadores Genius + Exceline Profesional | Vault de fallas — registro seguro e inviolable de los eventos de falla con timestamp | El auditor técnico accede al historial completo de eventos del motor sin que ningún dato haya podido perderse | Raíz del evento (Fault = falla técnica) + contenedor seguro (Vault) | ✅ | ✅ | "Vault" evoca almacenamiento seguro, inaccesible, valioso — la connotación de evidencia protegida es más fuerte que "Log". "Fault" es término técnico de ingeniería eléctrica no cotidiano para el consumidor promedio. Combinación potente para especificadores. | Bajo. "Vault" tiene uso en ciberseguridad y banca pero no como componente de nombre en protectores de motor clase 9. |
| 21 | NODO-E | **DiagTrace** | nuevo | Exceline Profesional + especificadores | Trazabilidad diagnóstica de cada evento de falla — registro con cadena de datos por evento | El ingeniero de mantenimiento tiene la traza completa del comportamiento del relé antes y durante cada falla | Raíz de diagnóstico (Diag) + registro de trazabilidad (Trace) | ✅ | ✅ | "Diag" es abreviación técnica de diagnóstico reconocida en ingeniería; "Trace" evoca trazabilidad, registro detallado de un evento. Combinación técnicamente densa — correcta para audiencia especificador. | Bajo. "DiagTrace" no aparece como nombre de marca en protectores de motor. Verificar clase 9 software de diagnóstico industrial. |
| 22 | NODO-E | **AuditLog** | nuevo | Especificadores Genius | Log de auditoría de fallas — campo por campo, evento por evento, con acceso dual LCD/bus | El proceso de certificación o auditoría técnica del equipo tiene el registro completo ya en el relé | Raíz de auditoría (Audit) + registro (Log) | ⚠ | ⚠ | "AuditLog" evoca registro formal de auditoría — potente para especificadores pero ambos componentes son términos de software/gestión ("audit log" es nombre genérico en sistemas de información). Riesgo de descriptividad o genericidad en clase 9 amplia. | Riesgo moderado: "AuditLog" es término genérico en software/ERP. En el contexto específico de relé de protección de motores puede ser defendible como fantasía bajo equivalencia perceptual, pero el riesgo es más alto que FaultVault o DiagTrace. Usar como cuarto candidato de respaldo. |
| 23 | NODO-F | **TripleLock** | anchor | Exceline Profesional + Genius | Bloqueo permanente tras 3 fallas de corriente recurrente en ventana de 30 minutos | El motor industrial no entra en el ciclo destructivo de falla-rearranque-falla | Cuantificador (Triple) + consecuencia de bloqueo (Lock) | ⚠ | ⚠ | "Triple" cuantifica el umbral de falla (exacto, documentado en HDE). "Lock" evoca cierre permanente. Para audiencia técnica la precisión del cuantificador es un diferenciador. No es descriptor para consumidor promedio de NODO-F. | Colisión potencial en clase 9 seguridad física por raíz "Lock" — búsqueda sectorial pendiente (caveat en deck). Si búsqueda confirma conflicto activo, activar contingencias. |
| 24 | NODO-F | **TripleGate** | nuevo | Exceline Profesional + Genius | Control de paso permanente tras acumulación de fallas — el equipo no rearranque sin intervención técnica | El motor industrial no cicla entre falla y arranque destructivo porque la lógica controla el paso de la señal | Cuantificador (Triple) + control de flujo lógico (Gate) | ✅ | ✅ | "Gate" en electrónica evoca control de paso de señal — técnicamente correcto para una función de bloqueo en lógica de control. Evita la raíz "Lock" que motiva la contingencia. Pronunciable en español. | Bajo. "Gate" tiene menor presencia en seguridad física que "Lock". La combinación "TripleGate" no colisiona con denominaciones de cerraduras. |
| 25 | NODO-F | **FaultHold** | nuevo | Exceline Profesional | Retención permanente del estado de falla hasta intervención técnica deliberada | El proceso industrial no rearranque automáticamente tras una secuencia crítica de fallas | Raíz del evento (Fault) + retención (Hold) | ✅ | ✅ | "FaultHold" describe la acción del sistema (retener ante falla) sin ser descriptor de la función completa. "Hold" evoca retención deliberada, espera hasta intervención. Más directo semánticamente que TripleGate. | Bajo. Verificar "FaultHold" en clase 9 software de gestión de errores. |
| 26 | NODO-F | **CycleBlock** | nuevo | Exceline Profesional + especificadores | Bloqueo del ciclo destructivo de falla-rearranque-falla | El motor no entra en el ciclo que lo daña — el bloqueo del ciclo es la función diferenciadora | Raíz del proceso (Cycle) + bloqueo (Block) | ✅ | ✅ | "CycleBlock" evoca el bloqueo del ciclo operativo destructivo — captura el beneficio del beneficio directamente en el nombre. "Block" evita la saturación de "Lock" en seguridad física. | Bajo. "Cycle" tiene uso en software de ciclos de desarrollo pero no en nombres de protectores de motor en clase 9. |
| 27 | NODO-F | **FaultGate** | contingencia sectorial | Exceline Profesional + Genius | Puerta que cierra el paso al rearranque tras secuencia crítica de fallas | La intervención técnica deliberada es el único camino para reabrir la operación | Raíz del evento (Fault) + control de paso (Gate) | ✅ | ✅ | Alternativa a TripleLock si búsqueda confirma colisión en seguridad física. "Gate" evoca control de acceso en contexto lógico. Activar si TripleLock tiene conflicto activo. | Contingencia. |
| 28 | NODO-F | **TripleHold** | contingencia sectorial | Exceline Profesional + Genius | Retención permanente tras tercera falla de corriente | El motor no puede rearranque hasta intervención técnica — el hold dura hasta que alguien lo levanta | Cuantificador (Triple) + retención (Hold) | ✅ | ✅ | Mantiene el cuantificador "Triple" (que el abogado puede preferir por precisión del RTB) pero reemplaza "Lock" con "Hold". Activar si TripleLock tiene conflicto activo. | Contingencia. |
| 29 | NODO-G | **TaskMemory** | anchor | Exceline Profesional (GRN-MV) | El GRN-MV almacena el modo operativo activo al corte y lo retoma automáticamente al restablecer la energía | El proceso de bombeo o riego no requiere supervisión humana en el reencendido — el equipo sigue desde donde estaba | Objeto de persistencia (Task) + mecanismo (Memory) | ✅ | ⚠ | "Task" y "Memory" son términos funcionales del dispositivo; bajo equivalencia perceptual SAPI el consumidor de un relé de nivel de bombeo no los asocia con software informático. Potencia comercial alta. | IMPI MX: riesgo colisión con clase 9 software (gestión de procesos informáticos — "task memory" es término de informática). Búsqueda en subclase software de IMPI MX es crítica (caveat en deck). Candidatos alternativos para MX en filas 37-39. |
| 30 | NODO-G | **StateHold** | nuevo | Exceline Profesional | Retención del estado operativo del sistema — el modo configurado persiste ante corte de energía | El proceso no necesita ser reiniciado manualmente — el estado anterior se retoma | Raíz de estado (State) + retención (Hold) | ✅ | ✅ | "StateHold" evoca retención del estado operativo sin vocabulario software. "State" aquí es el modo de operación del proceso físico (bombeo/riego). "Hold" connota que el estado no se pierde. Alejado de la combinación Task+Memory. | Bajo. Compatible tanto con SAPI VE como con IMPI MX. |
| 31 | NODO-G | **ModeTrace** | nuevo | Exceline Profesional + industria | El relé registra y recupera el modo de operación tras el corte | El técnico confirma qué modo tenía el relé cuando se fue la luz — y el relé lo retomó solo | Raíz del modo operativo (Mode) + rastreo de estado (Trace) | ✅ | ✅ | "ModeTrace" combina modo de operación + trazabilidad del estado. Evoca memoria de estado de forma técnicamente precisa sin ser descriptor literal. "Trace" añade connotación de registro que lo aleja del vocabulario software convencional. | Bajo. |
| 32 | NODO-G | **CycleResume** | nuevo | Exceline Profesional + industria | El ciclo de operación se retoma automáticamente al restablecer la energía | El proceso de bombeo o llenado de tanque no se interrumpe por el corte — el ciclo continúa | Raíz del proceso (Cycle) + continuación (Resume) | ✅ | ✅ | "CycleResume" describe la retoma del ciclo operativo — captura el L2 del beneficio del beneficio directamente. "Resume" evoca continuación sin intervención. Potente para audiencia industrial que gestiona ciclos de proceso. | Bajo. Verificar "CycleResume" en clase 9 software (gestión de ciclos de proceso en automatización industrial — es término técnico pero no nombre de marca identificado). |
| 33 | NODO-G | **RetainMode** | contingencia IMPI MX | Exceline Profesional | El modo de operación del relé se retiene entre cortes | La instalación de riego no necesita reconfiguración tras cada apagón | Raíz de retención (Retain) + modo operativo (Mode) | ✅ | ✅ | Candidato específico para IMPI MX donde TaskMemory puede colisionar con clase 9 software. "Retain" evoca persistencia sin uso en software de gestión de procesos informáticos. "Mode" es modo operativo. Completamente alejado de la combinación Task+Memory. | Contingencia IMPI MX. |
| 34 | NODO-G | **ModeKeep** | contingencia IMPI MX | Exceline Profesional | Retención del modo operativo del dispositivo ante interrupciones | El proceso de vaciado o llenado no se pierde | Raíz del modo (Mode) + retención activa (Keep) | ✅ | ✅ | "Keep" evoca retener algo activamente — más cotidiano que "Retain" pero no descriptivo en el contexto de relé de nivel industrial. La combinación "ModeKeep" no aparece en software de gestión de procesos. | Contingencia IMPI MX. |
| 35 | NODO-G | **ProcessHold** | contingencia IMPI MX | Exceline Profesional | Retención del proceso activo ante corte — el proceso se mantiene en el estado que estaba | El sistema de bombeo retoma sin intervención porque el proceso estaba retenido | Raíz del proceso (Process) + retención (Hold) | ✅ | ✅ | "ProcessHold" evoca que el proceso físico (bombeo, vaciado, llenado) queda retenido y disponible para retomarse. Alejado completamente del vocabulario informático Task+Memory. | Contingencia IMPI MX. Verificar "ProcessHold" en clase 9 software de gestión de procesos industriales. |
| 36 | NODO-H | **GIO-Net** | nuevo | Especificadores Genius + ingeniería de mantenimiento | Red propietaria de hasta 32 relés Genius en bus RS-485 bajo el Ecosystem GIO | El ingeniero de mantenimiento administra toda la instalación de relés desde un punto de acceso | GIO- (familia propietaria) + Red (Net) | ✅ | ✅ | "GIO" está establecido en el portafolio Genteca como denominación propietaria (GIO PORT, GIO-Link, GIO-Tool). "Net" evoca red de dispositivos — añade la dimensión de ecosystem multi-nodo que es el diferenciador de NODO-H. | Bajo. "-Net" tiene saturación en software pero en combinación con "GIO-" la especificidad de la familia propietaria reduce el riesgo. |
| 37 | NODO-H | **GIO-Mesh** | nuevo | Especificadores Genius | Red de topología propietaria para la gama Genius — conectividad integrada sin módulos adicionales | El especificador diseña instalaciones industriales con todos los relés en un solo bus de supervisión | GIO- (familia propietaria) + topología de red (Mesh) | ✅ | ✅ | "Mesh" evoca topología de malla — red de nodos interconectados. En la práctica el Ecosystem GIO usa topología de bus, no malla, pero "Mesh" evoca la idea de conectividad total sin que el nombre sea un descriptor técnico del protocolo. | Bajo. Verificar si "GIO-Mesh" colisiona con denominaciones de redes industriales de terceros. |
| 38 | NODO-H | **GIO-Bus** | nuevo | Especificadores técnicos + ingeniería | Bus propietario del Ecosystem GIO — conexión directa de hasta 32 relés Genius | El técnico de mantenimiento conecta todos los relés al bus y los administra con GIO-Tool | GIO- (familia propietaria) + arquitectura (Bus) | ⚠ | ⚠ | "Bus" en el contexto de comunicación industrial es término técnico estándar (fieldbus, bus industrial). "GIO-Bus" describe el bus del sistema GIO — moderadamente descriptivo de la función técnica del accesorio. | "Bus" como componente de nombre puede ser interpretado como descriptor técnico del tipo de conexión. Si el abogado considera que debilita la fantasía, preferir GIO-Net o GIO-Core. |
| 39 | NODO-H | **GIO-Core** | nuevo | Especificadores Genius + industria | El núcleo del Ecosystem GIO — la arquitectura de conectividad propietaria que unifica toda la gama Genius | El especificador tiene un solo sistema de monitoreo para todos los relés — no hay infraestructura paralela | GIO- (familia propietaria) + núcleo integrado (Core) | ✅ | ✅ | "Core" evoca el corazón o núcleo de un sistema — aplicado al Ecosystem GIO sugiere que es la base de la conectividad propietaria, no un accesorio. "GIO-Core" como nombre de la plataforma propietaria es potente para el abogado: es el ecosystem completo, no solo el protocolo. | Bajo. "Core" no describe el protocolo subyacente (MODBUS RTU). La combinación con GIO- mantiene la fantasía propietaria. |

---

## Sección 3 — Detalle por nodo

---

### NODO-A: Reconexión temporal aleatoria post-falla

- **Anchor del Top 7:** StaggerStart — preservado sin modificación.
- **Tecnología:** Algoritmo de retardo de reconexión post-falla con componente aleatoria dentro de una ventana ajustable (5-180 s GSM-MB; 180-300 s GSM-RB; 3 min fijo GSM-NG). La componente aleatoria evita que dos o más equipos en la misma instalación reconecten simultáneamente. Override Owner: universal en gama Exceline/Exceline Profesional/Genius.
- **Diferenciador competitivo:** Amarillo. Eaton C445 tiene función equivalente ("Voltage Loss Restart") pero orientada a motores industriales en MCC con configuración vía red. El diferenciador de Genteca es la ejecución en protector enchufable de bajo costo para segmento residencial/comercial — no la unicidad de la función.
- **Audiencia primaria:** Exceline residencial + comercio pequeño/mediano. Secundario: Exceline Profesional (instaladores).
- **Layer 2 (beneficio del beneficio):** El compresor y el equipo downstream no reciben el golpe de corriente del reencendido simultáneo de toda la instalación — vida útil preservada, menos fallas post-apagón.
- **Observación legal aplicable:** Override universal — sin impacto directo en naming de NODO-A. El caveat de deck aplica al override general y va en slide de metodología.

**4 candidatos:**

1. **StaggerStart** (anchor, candidato 1): raíz técnica de escalonamiento (Stagger) + acción de arranque (Start). "Stagger" es raramente usado en nombres clase 9 LatAm — espacio limpio. La combinación no es descriptiva para consumidor venezolano o mexicano promedio. Potencia alta: la raíz técnica le da credibilidad ante especificadores y la acción "Start" la hace comprensible para instaladores. SAPI/IMPI: ✅. Ningún riesgo identificado.

2. **CascadeStart** (nuevo, candidato 2): "Cascade" evoca flujo ordenado y secuenciado — captura la esencia del algoritmo de escalonamiento sin ser descriptor literal. Más visual que StaggerStart para audiencia residencial. SAPI/IMPI: ✅. Riesgo bajo.

3. **SeqGuard** (nuevo, candidato 3): "Seq" como abreviación técnica de secuencia, "Guard" como rol defensivo. Más compacto que los anteriores — 3 sílabas totales. Apela a especificadores de procesos de control. SAPI/IMPI: ✅. Verificar clase 9 software por el uso de "Seq" en contextos de secuenciamiento de tareas.

4. **PhaseStart** (nuevo, candidato 4): "Phase" en contexto de reconexión evoca arranque por fases temporales. Ambigüedad controlada: "phase" tiene doble lectura eléctrica/temporal, lo que puede ser tanto activo (evocación técnica) como pasivo (riesgo de descriptividad). Es el candidato más débil del nodo por esa ambigüedad. SAPI/IMPI: ⚠. Si el abogado prefiere candidatos más limpios, SeqGuard o CascadeStart son superiores.

---

### NODO-B: Detección sub-ciclo de perturbaciones de voltaje (FlickerGuard)

- **Anchor del Top 7:** FlickerGuard — aprobado con contingencia OMPI.
- **Tecnología:** Detección de flicker en 20ms (GSM-L, dato explícito en HDE v10) y curva inversa V-t algorítmica (override universal). Detección de falla de voltaje genérica a partir de 60ms (GSM-L). Desconexión proporcional a la intensidad de la desviación (0,02-2 s en GSM-AV06; 0,4-3 s en GSM-RB).
- **Diferenciador competitivo:** Verde. La especificación de 20ms en supervisor de voltaje monofásico de gama baja residencial/comercial no tiene equivalente publicado identificado en la competencia directa. La competencia industrial de alta gama tiene detección sub-ciclo pero en otra categoría de producto y punto de precio.
- **Audiencia primaria:** Exceline residencial (dueños de hogar — AC, refrigerador como equipos a proteger).
- **Layer 2:** El compresor del AC o refrigerador no se daña por los arranques forzados por parpadeo eléctrico.
- **Observación legal aplicable:** FlickerGuard lleva caveat en deck del abogado — existe evidencia de productos LED (Australia/UK) con el término "Flicker Guard" como feature en clase 9. La búsqueda fonética debe verificar conflicto activo en SAPI/IMPI. Si hay conflicto, activar candidatos de contingencia.

**4 candidatos principales:**

1. **FlickerGuard** (anchor, candidato 1): el nombre más potente del portafolio para audiencia residencial. "Flicker" es técnicamente preciso (IEC 61000-4-15) y no cotidiano para el consumidor venezolano — funciona como fantasía bajo equivalencia perceptual SAPI. "Guard" evoca defensa activa. RTB sólido: 20ms es el diferenciador más agresivo del portafolio (NODO-B verde en análisis competitivo). SAPI/IMPI: ⚠ (colisión potencial LED pendiente de búsqueda).

2. **SagShield** (nuevo, candidato 2): "Sag" (caída de voltaje) es técnicamente más preciso que "Flicker" para el fenómeno de base pero menos evocador para el consumidor. "Shield" diferencia de "Guard" morfológicamente. Perfil de fantasía alto — "sag" no es cotidiano. SAPI/IMPI: ✅.

3. **PulseBlock** (nuevo, candidato 3): "Pulse" como perturbación eléctrica impulsiva; "Block" como bloqueo activo. Cubre el espacio de transitorios rápidos con nombre diferente al anchor. Pronunciable. SAPI/IMPI: ✅.

4. **SpurGuard** (nuevo, candidato 4): "Spur" en electrónica describe perturbación espuria — técnicamente preciso para las perturbaciones sub-ciclo que caracterizan NODO-B. "Guard" como rol defensivo. El nombre aporta la densidad técnica que especificadores valoran. SAPI/IMPI: ✅.

**Candidatos de contingencia OMPI (activar solo si búsqueda confirma colisión activa de FlickerGuard):**

- **SpikeShield** (contingencia OMPI): "Spike" = pico eléctrico reconocido en electrónica; "Shield" = protección. Perfil de fantasía alto en clase 9 protectores de motor. ✅/✅.
- **SagGuard** (contingencia OMPI): "Sag" tiene menor presencia en productos de iluminación que "Flicker" — limpia la raíz de la colisión LED. Mantiene el patrón morfológico de FlickerGuard. ✅/✅.

---

### NODO-C: Modelo térmico NTC integrado en protector monofásico (Thermo-Safe)

- **Anchor del Top 7:** Thermo-Safe — aprobado con caveat Caso A.
- **Tecnología:** Sensor NTC embebido en protector monofásico GSM-MB/RB/RE. Lee temperatura real del entorno del compresor. A diferencia del modelo I-t (NODO-D), usa medición física de temperatura con hardware físico (NTC) en el circuito de decisión. Gap documental: parámetros técnicos NTC (umbral, rango, histéresis) no en HDE actual.
- **Diferenciador competitivo:** Amarillo. El diferenciador de Genteca es la integración del NTC en el protector enchufable monofásico como feature estándar de serie (no módulo separado), al punto de precio doméstico VE/MX.
- **Audiencia primaria:** Exceline residencial + comercio pequeño/mediano.
- **Layer 2:** El motor no se quema por sobrecalentamiento encubierto que la protección por corriente sola no detecta.
- **Observación legal aplicable (Caso A):** "Thermo-Safe es nombre de fantasía que no deriva de la descripción funcional del producto. La combinación 'Thermo' (prefijo de origen griego, raíz técnica) + 'Safe' (beneficio de seguridad en inglés) no constituye una descripción literal de la función del producto para el consumidor venezolano o mexicano promedio. El empaque del producto usa la descripción 'PROTECCION TERMICA', que es la descripción funcional en español; 'Thermo-Safe' es el nombre de fantasía de la función nombrada y es semánticamente distinto de la descripción funcional en uso."

**4 candidatos:**

1. **Thermo-Safe** (anchor, candidato 1): el nombre más potente disponible para este nodo. El argumento de fantasía ante el abogado está construido y disponible. La distinción entre "PROTECCION TERMICA" (descripción en empaque) y "Thermo-Safe" (nombre de fantasía) es el argumento central. SAPI/IMPI: ⚠ (Caso A, caveat activo, argumento disponible).

2. **CoreSafe** (nuevo, candidato 2): aleja del territorio Thermo- sin perder la evocación de protección profunda. "Core" como núcleo del motor protegido; "Safe" como estado seguro. Perfil de fantasía más alto que Thermo-Safe — sin componente térmica explícita en el nombre. SAPI/IMPI: ✅.

3. **WarmWatch** (nuevo, candidato 3): "Warm" evoca temperatura en ascenso antes del daño — compatible con el beneficio del beneficio L2 (el motor no se quema). "Watch" evoca vigilancia continua sin prometer precisión cuantitativa, compatible con el gap documental NTC. Nombre más evocador para audiencia residencial que Thermo-Safe. SAPI/IMPI: ✅.

4. **HeatSeal** (nuevo, candidato 4): "HeatSeal" captura la idea de que el protector sella el motor de la amenaza del calor excesivo. "Heat" es descriptivo pero "Seal" lo convierte en acción. Riesgo moderado: "heat" puede rozar descriptividad en un protector térmico. Es el candidato con mayor riesgo del nodo después de Thermo-Safe. SAPI/IMPI: ⚠. Preferir CoreSafe o WarmWatch si el abogado considera que el nombre es más limpio.

---

### NODO-D: Curva inversa I-t diferenciada cold/hot (sin anchor — ThermalCurve rechazado)

- **Anchor del Top 7:** ThermalCurve — **RECHAZADO** en revisión interna de propiedad intelectual. Sin anchor. Los 4 candidatos son nuevos.
- **Tecnología:** Algoritmo de imagen térmica según IEC 60255-8 / IEEE C37.112. El tiempo de disparo ante sobrecarga es inversamente proporcional al nivel de sobrecarga. La curva caliente = curva fría / 3 — el motor que arrancó en caliente dispara hasta 3 veces más rápido para el mismo nivel de sobrecarga. Memoria térmica hasta 2 horas. Clase térmica ajustable 5-30.
- **Diferenciador competitivo:** Rojo. La curva inversa I-t cold/hot es función estándar IEC presente en toda la competencia industrial relevante. No hay diferenciador propietario documentado.
- **Audiencia primaria:** Exceline Profesional + especificadores técnicos (Genius).
- **Layer 2:** El motor industrial no dispara prematuro en arranque en caliente ni queda desprotegido en arranque en frío — la curva se adapta al estado real del motor, no a un patrón fijo.
- **Observación legal aplicable:** No hay caveat específico para los candidatos nuevos. Aplica el caveat de override universal si algún candidato nuevo apoya claims sobre la universalidad de la función.

**Nota de dirección semántica:** La dirección semántica correcta es la adaptación al estado real del motor, no la curva algorítmica. El territorio vedado es amplio: Thermal-, Thermo-, -Curve, Curve-, Heat-, Hot-, Cold-, IEC, IEEE. El beneficio del beneficio es que el motor no dispara de forma inadecuada según su estado de arranque.

**4 candidatos:**

1. **StateGuard** (nuevo, candidato 1): "State" como estado real del motor (frío o caliente al arranque); "Guard" como rol defensivo proporcional a ese estado. El nombre evoca que la protección es función del estado del motor, no de un umbral fijo. Técnicamente preciso para especificadores sin nombrar el mecanismo IEC. SAPI/IMPI: ✅. Ningún riesgo significativo identificado. Es el candidato más fuerte del nodo.

2. **AdaptShield** (nuevo, candidato 2): "Adapt" como adaptación al punto de operación; "Shield" como defensa. La función del nodo es precisamente la adaptación de la curva según el estado térmico acumulado. SAPI/IMPI: ✅.

3. **MotorState** (nuevo, candidato 3): más técnico y denso — útil para el especificador que entiende "motor state" como estado del motor en operación. Riesgo moderado porque "Motor" puede ser interpretado como descriptor de la categoría de producto en clase 9. Bajo equivalencia perceptual puede sostenerse, pero el abogado debe evaluarlo. SAPI/IMPI: ⚠.

4. **RunState** (nuevo, candidato 4): "Run" como ciclo de operación activa del motor; "State" como estado del ciclo en curso. Evoca que la protección opera sobre el estado del ciclo de operación, no sobre una curva fija. 3 sílabas, CamelCase limpio. SAPI/IMPI: ✅. Riesgo bajo; verificar en clase 9 software.

---

### NODO-E: Registro forense histórico de fallas (ForensLog)

- **Anchor del Top 7:** ForensLog — aprobado, Escenario A (RTB anclado en GIII+MV). Decisión del equipo IP interno confirma Escenario A.
- **Tecnología:** Registro en memoria no volátil de cada evento de falla con tipo, valor medido, hora, fecha, duración y parámetros activos al momento de la falla. Capacidad máxima: 100 últimas fallas (GIII+MV, HDE primaria). Baseline gama Genius: 20 últimas fallas. Acceso dual: pantalla LCD + MODBUS RTU. Registro circular.
- **Diferenciador competitivo:** Amarillo. En el segmento directo, 100 registros (GIII+MV) aventaja significativamente a Rockwell E300 (10 registros — HECHO verificado en manual E300 193-UM015). La competencia de subestación (ABB REF615) tiene más registros pero no es la misma categoría de producto.
- **Audiencia primaria:** Exceline Profesional + especificadores técnicos Genius.
- **Layer 2:** El técnico de mantenimiento reconstruye el historial exacto de fallas sin depender del operador — diagnóstico preciso, menos tiempo fuera de servicio, menos costo de visita técnica.
- **Observación legal aplicable:** "El RTB del nombre ForensLog descansa en el GIII+MV con capacidad de registro de 100 últimas fallas con timestamp. El baseline de la gama Genius es 20 últimas fallas. El nombre ForensLog se vincula a la tecnología de registro forense como concepto, no a un número específico de eventos."

**4 candidatos:**

1. **ForensLog** (anchor, candidato 1 — Escenario A): el nombre más potente del portafolio para audiencia de mantenimiento industrial. "Forensic" evoca análisis de evidencia con rigor técnico — no es uso cotidiano venezolano/mexicano. "Log" es registro. RTB verificado (100 fallas GIII+MV) es el diferenciador cuantitativo más sólido del portafolio. SAPI: ✅. IMPI MX: ⚠ (Log en clase 9 software — contexto suficientemente distante al de un relé de motor, pero verificar).

2. **FaultVault** (nuevo, candidato 2): "Vault" eleva la connotación de ForensLog — no solo registra fallas, las guarda en bóveda inviolable. Potente para el especificador que valora la integridad del registro. "Fault" es término técnico de ingeniería eléctrica, no cotidiano. SAPI/IMPI: ✅. Es el candidato alternativo más fuerte del nodo — si ForensLog tiene colisión en clase 9 software, FaultVault es el reemplazo natural.

3. **DiagTrace** (nuevo, candidato 3): "Diag" como abreviación de diagnóstico (reconocida en ingeniería), "Trace" como trazabilidad del evento. Más técnico que FaultVault, más acotado semánticamente. Útil si el abogado prefiere nombre sin connotación forense por alguna razón. SAPI/IMPI: ✅.

4. **AuditLog** (nuevo, candidato 4): el más débil del nodo — ambos componentes son términos de software/gestión. En el contexto específico de un relé de protección de motores puede sostenerse por equivalencia perceptual, pero el riesgo de genericidad en clase 9 amplia es el más alto del nodo. Usar como cuarto candidato de respaldo si los tres anteriores tienen problemas. SAPI/IMPI: ⚠.

---

### NODO-F: Bloqueo permanente tras tercera falla de corriente recurrente (TripleLock)

- **Anchor del Top 7:** TripleLock — aprobado con contingencia sectorial.
- **Tecnología:** Si el relé detecta 3 fallas de corriente (sobrecarga, pérdida de fase por corriente, desbalance) dentro de 30 minutos, ejecuta desconexión permanente que requiere reset manual para restablecer operación. Tiempo de disparo en tercera falla: < 1 segundo (GOC HDE sección E). Aplica en GOCT, GUCT+, GSPT/GSPT-MV, GIII+/GIII+MV, GOC (Genius) y GSC-CR/GSC-MB (Exceline Profesional).
- **Diferenciador competitivo:** Amarillo. La función existe en competencia como parámetro configurable sin identidad de feature. Genteca tiene la función nombrada con identidad propia — el naming lo diferencia.
- **Audiencia primaria:** Exceline Profesional + Genius.
- **Layer 2:** El motor industrial no entra en el ciclo destructivo de falla-rearranque-falla que destruye el bobinado antes de que alguien intervenga.
- **Observación legal aplicable:** "TripleLock: nombre de fantasía en clase 9. La raíz 'Lock' tiene presencia en marcas de sistemas de seguridad física (cerraduras electrónicas, control de acceso) en Clase 9. La búsqueda fonética debe verificar si existen titulares activos con marcas que incluyan 'TripleLock' o 'Triple Lock' en la subclase de dispositivos de seguridad o protección en SAPI Venezuela y en IMPI Mexico."

**4 candidatos:**

1. **TripleLock** (anchor, candidato 1): el cuantificador "Triple" es el RTB exacto (3 fallas en 30 minutos — documentado en HDE). "Lock" evoca bloqueo permanente con necesidad de intervención para desbloquear. Alta potencia para audiencia técnica — la precisión del cuantificador transmite credibilidad de especificación. SAPI/IMPI: ⚠ (búsqueda sectorial en seguridad física pendiente).

2. **TripleGate** (nuevo, candidato 2): mantiene el cuantificador RTB "Triple" y reemplaza "Lock" con "Gate" — control de paso de señal, no cerradura física. Evita completamente el territorio de seguridad física. Funcionalmente equivalente a TripleLock pero con raíz que evoca lógica de control eléctrico. SAPI/IMPI: ✅.

3. **FaultHold** (nuevo, candidato 3): "Fault" como falla técnica + "Hold" como retención permanente hasta intervención. Captura el beneficio del beneficio del nodo: el equipo se mantiene detenido hasta que alguien lo libera deliberadamente. Pierde el cuantificador "Triple" — el RTB numérico no está en el nombre, pero la función de retención sí. SAPI/IMPI: ✅.

4. **CycleBlock** (nuevo, candidato 4): "CycleBlock" es el nombre que más captura el L2 del beneficio del beneficio — bloquea el ciclo destructivo de falla-rearranque. "Block" es defensivo sin la connotación de cerradura física de "Lock". SAPI/IMPI: ✅.

**Candidatos de contingencia sectorial (activar si búsqueda confirma colisión activa de TripleLock):**

- **FaultGate** (contingencia sectorial): "Fault" + "Gate" — control de acceso lógico ante falla. Completamente alejado de seguridad física. ✅/✅.
- **TripleHold** (contingencia sectorial): preserva el cuantificador "Triple" (que el abogado puede querer mantener por la precisión del RTB) pero reemplaza "Lock" con "Hold". ✅/✅.

---

### NODO-G: Memoria de estado y reanudación de tarea post-corte (TaskMemory)

- **Anchor del Top 7:** TaskMemory — aprobado para SAPI VE; candidatos alternativos para IMPI MX generados.
- **Tecnología:** El GRN-MV almacena en memoria no volátil el modo operativo activo al corte (vaciado de pozo, llenado de tanque, espera) y lo retoma automáticamente al restablecer la energía. Texto literal de HDE: "retoma automáticamente la última función al restablecerse la energía, sin requerir intervención del usuario." Tiempo de confirmación 10s post-restablecimiento: confirmado por I+D verbalmente, no en HDE v9 — gap documental.
- **Diferenciador competitivo:** Verde. Ningún fabricante de la lista obligatoria tiene función equivalente nombrada en controladores de nivel/bombeo residencial-comercial identificada. El diferenciador es real en el segmento.
- **Audiencia primaria:** Exceline Profesional (GRN-MV — instalaciones de riego, bombeo industrial).
- **Layer 2:** El proceso de bombeo o riego no requiere supervisión humana en el reencendido post-corte — el equipo retoma solo donde estaba, sin perder el ciclo.
- **Observación legal aplicable:** "TaskMemory: nombre de fantasía para controlador de nivel de bombeo (GRN-MV). La combinación 'Task' + 'Memory' tiene presencia en terminología de software de gestión de procesos en informática (clase 9 amplia). La búsqueda fonética debe priorizar la subclase de software y aplicaciones en IMPI Mexico para verificar si hay titulares activos con marcas similares. En SAPI Venezuela, la doctrina de equivalencia perceptual favorece la registrabilidad del nombre para el producto eléctrico."

**4 candidatos (incluyendo anchor):**

1. **TaskMemory** (anchor, candidato 1 — SAPI VE): nombre con la mayor potencia comercial del portafolio para audiencia industrial. La precisión semántica (tarea + memoria) captura exactamente el beneficio del L2. Bajo equivalencia perceptual SAPI VE es nombre de fantasía para el consumidor de un relé de nivel. SAPI VE: ✅. IMPI MX: ⚠ — usar candidatos alternativos para MX si búsqueda confirma colisión.

2. **StateHold** (nuevo, candidato 2): "State" como modo operativo del proceso; "Hold" como retención de ese estado entre cortes. Completamente alejado del vocabulario software. Válido tanto para VE como MX. SAPI/IMPI: ✅.

3. **ModeTrace** (nuevo, candidato 3): "Mode" como modo de operación configurado; "Trace" como registro y recuperación del estado. La connotación de trazabilidad del modo es técnicamente precisa para especificadores. SAPI/IMPI: ✅.

4. **CycleResume** (nuevo, candidato 4): captura directamente el L2 del beneficio del beneficio — el ciclo de operación se retoma (resume) automáticamente. "Resume" evoca continuación sin intervención. Potente para audiencia industrial. SAPI/IMPI: ✅.

**Candidatos alternativos para IMPI MX (activar si búsqueda confirma colisión software en MX):**

- **RetainMode** (contingencia IMPI MX): "Retain" como persistencia activa; "Mode" como modo operativo. Sin vocabulario software. ✅/✅.
- **ModeKeep** (contingencia IMPI MX): "Mode" + "Keep" — retener el modo de operación activo. Cotidiano sin ser descriptor. ✅/✅.
- **ProcessHold** (contingencia IMPI MX): "Process" como proceso físico de bombeo; "Hold" como retención del estado. Completamente alejado de Task+Memory. ✅/✅.

---

### NODO-H: Ecosystem GIO — Conectividad industrial integrada

- **Anchor del Top 7:** ninguno (nodo reformulado en revisión interna). Los 4 candidatos son nuevos dentro de la familia GIO-*.
- **Tecnología:** Arquitectura de comunicación industrial embebida en relés Genius — GIO PORT + accesorios GIO-Link (USB/RS-232/RS-485) + software GIO-Tool + protocolo MODBUS RTU. Red: hasta 32 relés en bus RS-485 (GIO-A-RS485K). Variables accesibles: corriente, voltaje, frecuencia, kW/kVA/kWh, FP, temperatura, histórico de fallas, on/off remoto, parámetros con contraseña. GIO-Tool: monitorización en tiempo real + CSV.
- **Diferenciador competitivo:** Amarillo. El diferenciador es la integración desde el diseño sin módulos adicionales en el segmento Genius de VE/MX. En el mercado global, la competencia también ofrece MODBUS, pero frecuentemente vía módulo separado.
- **Audiencia primaria:** Especificadores técnicos (transversal Genius) + ingeniería de mantenimiento industrial.
- **Layer 2:** El técnico de mantenimiento accede a lecturas en tiempo real y al historial de fallas desde un punto sin instalar hardware adicional.
- **Instrucción vinculante:** Los 4 candidatos anclan en la familia GIO-* o crean nombres para el ecosystem propietario. Ninguno puede contener MODBUS, RS-485, IO-Link, PROFIBUS, DeviceNet, EtherNet/IP ni ningún término de protocolo estándar. GIO-Link, GIO-Tool y GIO-Port ya son denominaciones de producto en uso — no duplicar.
- **Observación legal aplicable:** "Los candidatos de naming del NODO-H se anclan en la denominación propietaria Ecosystem GIO (GIO PORT / GIO-Link / GIO-Tool) de Genteca. El protocolo de comunicación subyacente es MODBUS RTU (estándar abierto — Modbus Organization). Los nombres candidatos no contienen ni aluden a MODBUS ni a ninguna denominación de protocolo estándar."

**4 candidatos:**

1. **GIO-Net** (nuevo, candidato 1): "GIO-" como raíz propietaria establecida en el portafolio + "Net" como red de dispositivos. Evoca el ecosystem de hasta 32 relés en bus — la red propietaria del sistema. SAPI/IMPI: ✅. Riesgo bajo. El candidato más limpio morfológicamente para el abogado: GIO es denominación propietaria verificada, "Net" no alude al protocolo subyacente.

2. **GIO-Mesh** (nuevo, candidato 2): "Mesh" evoca topología de malla — red de nodos interconectados con múltiples puntos de acceso. Más evocador que "Net" para el especificador que diseña instalaciones industriales. SAPI/IMPI: ✅. Verificar que "GIO-Mesh" no colisione con denominaciones de redes industriales de terceros.

3. **GIO-Bus** (nuevo, candidato 3): "Bus" es término técnico estándar de arquitectura de red industrial — técnicamente correcto para el Ecosystem GIO (que usa bus RS-485). Riesgo moderado: "bus" puede ser interpretado como descriptor del tipo de conexión. Si el abogado lo considera debilitante, GIO-Net o GIO-Core son superiores. SAPI/IMPI: ⚠.

4. **GIO-Core** (nuevo, candidato 4): "Core" como núcleo del ecosystem propietario — la plataforma de conectividad que unifica toda la gama Genius. La connotación es sistémica y propietaria, no de protocolo. Para el abogado: GIO-Core como nombre de la plataforma propietaria (el núcleo del sistema, no el cable ni el protocolo) tiene el perfil de fantasía más alto del nodo. SAPI/IMPI: ✅. Candidato más fuerte para posicionamiento del ecosystem como plataforma completa.

---

## Sección 4 — Decisiones adoptadas

### 4.1 ForensLog — Escenario A (decisión principal, §1.3)

Decisión del equipo IP interno: Escenario A — RTB del nombre anclado en el GIII+MV con capacidad de 100 últimas fallas con timestamp. El Escenario B (ampliar a gama Genius entera) debilita el RTB sin ventaja de naming. El análisis competitivo interno sostiene Escenario A y el argumento ante el abogado es más limpio con RTB cuantitativo único (100 fallas GIII+MV vs 10 en Rockwell E300). Esta decisión es consistente con el documento de arquitectura de mensajes vigente en NODO-E — sin necesidad de actualización.

### 4.2 NODO-D — Cuatro candidatos nuevos, ninguno rescata territorio de ThermalCurve

La evaluación interna rechazó ThermalCurve. La dirección semántica correcta del nodo es la adaptación al estado real del motor, no la curva algorítmica. Los 4 candidatos nuevos (StateGuard, AdaptShield, MotorState, RunState) abordan ese territorio semántico sin tocar Thermal-, -Curve, Heat-, Hot-, Cold-.

Candidato más fuerte: **StateGuard** — captura el diferenciador real (la protección responde al estado del motor) con un nombre técnico sin riesgo de descriptividad. Candidato con mayor riesgo: **MotorState** — "Motor" puede ser objetado como descriptor de la categoría del producto en clase 9 de protectores de motor.

Condición de reapertura (nota al Owner / equipo técnico): Si I+D documenta un parámetro propietario de la implementación Genteca que excede el estándar IEC (factor cold/hot diferencial con valor específico, parámetro de memoria térmica con característica propia, o similar), el equipo de propiedad intelectual interno puede revisar esta postura y abrir espacio para nombres con raíz térmica más directa. Sin ese RTB, los 4 candidatos nuevos son la postura definitiva.

### 4.3 NODO-H — Familia GIO-* seleccionada como arquitectura de naming

La instrucción de no usar términos de protocolo estándar y anclar en la familia GIO está ratificada en revisión interna. La decisión de usar GIO-* como prefijo es la correcta: GIO tiene uso comercial documentado en el portafolio Genteca (GIO PORT, GIO-Link, GIO-Tool), tiene historia de uso que refuerza la fantasía ante el examinador, y define el ecosystem propietario diferenciándolo del protocolo subyacente. Los 4 candidatos (GIO-Net, GIO-Mesh, GIO-Bus, GIO-Core) son todos nuevos. GIO-Core es el candidato más fuerte para posicionar el ecosystem como plataforma completa.

### 4.4 Candidato PhaseStart (NODO-A, candidato 4) — aceptado con advertencia

"PhaseStart" tiene riesgo de descriptividad moderado porque "phase" en eléctrico puede leerse como descriptor técnico de la categoría. Se incluye como candidato 4 de NODO-A porque los tres candidatos anteriores son sólidos y el cuarto slot permite una opción exploratoria que el abogado puede evaluar. Si el abogado lo descarta, StaggerStart, CascadeStart y SeqGuard son suficientes para el nodo.

### 4.5 Candidatos descartados durante evaluación interna

Los siguientes candidatos se evaluaron y descartaron antes de entrar al documento:

| Candidato descartado | Nodo | Razón de descarte |
|---------------------|------|-------------------|
| ThermalState | NODO-D | Raíz "Thermal-" prohibida para NODO-D (territorio rechazado en evaluación interna) |
| ColdGuard | NODO-D | Raíz "Cold-" prohibida para NODO-D |
| HotShield | NODO-D | Raíz "Hot-" prohibida para NODO-D |
| SmartLock | NODO-F | Sufijo "-Smart" excluido por guardrail de naming |
| ThermoGuard | NODO-C | Presencia en marcas europeas (análisis competitivo + reglas de familia) |
| ThermoShield | NODO-C | Presencia en marcas europeas (análisis competitivo) |
| GIO-Link (nuevo) | NODO-H | Ya existe como denominación de producto Genteca |
| GIO-Port (nuevo) | NODO-H | Ya existe como denominación física Genteca |
| FlickerShield | NODO-B (contingencia) | Raíz Flicker- reservada para NODO-B; la contingencia debe diferenciarse fonéticamente de FlickerGuard |
| FaultLock | NODO-F | "Lock" es precisamente la raíz problemática en las contingencias — candidato de contingencia no puede reintroducir el riesgo |
| DataTrace | NODO-E | "Data" es demasiado genérico — sin raíz que aporte la connotación forense que le da potencia a ForensLog |
| StateMemory | NODO-G (MX) | Riesgo de colisión software en IMPI MX similar a TaskMemory — la combinación State+Memory replica el problema aunque no sea Task+Memory literal |
| AutoResume | NODO-G | "Auto-" + "Resume" — "Auto" puede crear confusión de categoría con clase 9 automotriz; además "AutoResume" describe literalmente la función de reanudación automática |
| ThermoCore | NODO-C | "ThermoCore" entra en conflicto interno de familia — Thermo- es prefijo de NODO-C pero "-Core" es el sufijo usado en CoreSafe para el mismo nodo; la combinación como candidato distinto generaría confusión |
| LogVault | NODO-E | Invierte el orden de ForensLog sin aportar potencia adicional; "Log" como primer componente baja el perfil de fantasía |
| TripleBlock | NODO-F | Válido morfológicamente pero CycleBlock y FaultHold cubren mejor el beneficio del beneficio del nodo; TripleBlock queda redundante con TripleGate |

### 4.6 Observación sobre PhaseStart y AuditLog como candidatos más débiles

PhaseStart (NODO-A candidato 4) y AuditLog (NODO-E candidato 4) son los candidatos con mayor riesgo de descriptividad en sus respectivos nodos. Se incluyen en cumplimiento del objetivo de generar 4 candidatos por nodo, pero con la recomendación explícita de que son los últimos a considerar si los tres anteriores son viables. La filosofía de base del proyecto ("pocos fuertes vs muchos con caveats") aplica en cascada dentro del nodo: candidatos 1-3 son los fuertes; candidato 4 es el de respaldo explorado.

---

## Sección 5 — Notas de cierre y pendientes

**Total candidatos producidos:** 32 candidatos base + 7 contingencias = **39 entradas en documento**

**Decisiones críticas adoptadas:**

1. ForensLog — Escenario A confirmado: RTB del GIII+MV como postura principal. Argumento ante el abogado más limpio y cuantificable.

2. NODO-D — 4 candidatos completamente nuevos: StateGuard (candidato más fuerte), AdaptShield, MotorState, RunState. Ninguno roza el territorio Thermal-/Curve-. La condición de reapertura (RTB propietario de I+D) queda documentada.

3. NODO-H — Familia GIO-* seleccionada: GIO-Core es el candidato más estratégico (ecosystem como plataforma), GIO-Net es el más limpio para el abogado.

4. NODO-G — TaskMemory para SAPI VE; 3 candidatos alternativos (RetainMode, ModeKeep, ProcessHold) para IMPI MX si búsqueda confirma colisión.

5. NODO-B y NODO-F — FlickerGuard y TripleLock como candidatos principales; contingencias (SpikeShield/SagGuard y FaultGate/TripleHold) listas para activar sin necesidad de reiniciar la evaluación.

**Slots fuertes vs débiles para el deck del abogado:**

- **Slots fuertes (candidatos 1-2 de cada nodo):** StaggerStart, CascadeStart, FlickerGuard, SagShield, Thermo-Safe, CoreSafe, StateGuard, AdaptShield, ForensLog, FaultVault, TripleLock, TripleGate, TaskMemory, StateHold, GIO-Core, GIO-Net.
- **Slots de respaldo exploratorio (candidatos 3-4):** SeqGuard, PhaseStart, PulseBlock, SpurGuard, WarmWatch, HeatSeal, MotorState, RunState, DiagTrace, AuditLog, FaultHold, CycleBlock, ModeTrace, CycleResume, GIO-Mesh, GIO-Bus.
- **Contingencias activables:** Los 7 candidatos de contingencia están listos para reemplazar candidatos principales si búsquedas confirman colisiones activas. No requieren nueva iteración de evaluación.

**Esta Naming Bible es el input directo para el deck del abogado.** La estructura de 8 nodos × 4 candidatos más contingencias es el insumo para construir el bloque de slides por tecnología. Los caveats literales de cada nodo van en las notas de los slides correspondientes (no en el cuerpo visible). El candidato 1 de cada nodo es el candidato principal del slide; los candidatos 2-4 son los alternativos.

**Si I+D reabre NODO-D:**

Si I+D documenta RTB propietario para el algoritmo I-t de Genteca (parámetro fuera del estándar IEC), la secuencia sugerida es: I+D actualiza HDE → equipo técnico evalúa si cambia el estado de rojo → equipo de propiedad intelectual interno revisa postura sobre naming de NODO-D → se generan candidatos adicionales. Los 4 candidatos nuevos actuales no se invalidan — se añaden opciones.

**Preguntas abiertas al Owner:**

1. ¿Se confirma StateGuard como el candidato principal de NODO-D para la presentación al abogado, o el Owner prefiere que se presenten los 4 con el mismo peso? Recomendación del equipo IP interno: en el slide de NODO-D, indicar que StateGuard y AdaptShield son los candidatos de mayor potencia, dado que el anchor ThermalCurve fue rechazado.

2. Para NODO-H: ¿GIO-Core o GIO-Net como candidato 1 del slide? GIO-Core tiene mayor potencia para posicionar el ecosystem como plataforma; GIO-Net es morfológicamente más limpio para el abogado. Recomendación del equipo IP interno: GIO-Core como candidato 1 para el slide (el argumento de plataforma integrada es el diferenciador del nodo), GIO-Net como candidato 2.

3. Ninguna pregunta bloquea la preparación del deck. El trabajo puede arrancar con este documento tal como está.

**Items abiertos pendientes:**

1. Búsqueda fonética formal del abogado (SAPI/IMPI) para FlickerGuard, TripleLock, TaskMemory — determina si contingencias se activan.
2. I+D: HDE GSM-MB actualizada con parámetros NTC (gap documental crítico para NODO-C).
3. I+D: addendum GRN-MV con confirmación de 10s (gap documental NODO-G).
4. I+D: documentación formal del Ecosystem GIO diferenciado de MODBUS RTU (gap NODO-H).
5. Equipo técnico: reapertura opcional de NODO-D si documenta RTB propietario más allá de IEC — ver §4.2 de este documento.

---

*Naming Bible — Portfolio IP 2026 (Genteca) — v2.0 — 2026-05-13*
