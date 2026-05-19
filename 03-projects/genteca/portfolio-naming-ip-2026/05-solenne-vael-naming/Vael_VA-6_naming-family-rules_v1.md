---
doc_type: VA-6-naming-family-rules
project_id: portfolio-naming-ip-2026
domain: genteca
version: v1.0
author: Vael
fecha: 2026-05-13
inputs:
  - 00-project-charter.md (v1.0)
  - Vael_VA-1_messaging-architecture_v1.md
  - Vael_VA-5_guardrails_v1.md
  - Bruna_BR-2_approval-set_v1.md
  - Orlan_OL-1_differentiation-matrix_v1.md
output_downstream:
  - Solenne Phase 4 (32 candidatos base + contingencias)
  - Vivienne Phase 5 (Deck — coherencia visual del portafolio)
---

# VA-6 — Naming Family Rules
## Portfolio Naming IP 2026 (Genteca)

> Reglas de familia para los 32 candidatos de nombre (8 nodos × 4 candidatos). Este
> documento no propone nombres — define el marco morfológico, fonético, semántico y
> de coherencia dentro del cual Solenne genera. Las reglas derivan del análisis del
> Top 7 anchor como estética de referencia, filtradas por las decisiones formales del
> BR-2 de Bruna y los guardrails del VA-5.

---

## 1. Aesthetic anchor del portafolio

Los 6 nombres anchor confirmados por Bruna son el espejo en el que deben verse todos
los candidatos nuevos. El Top 7 original tenía 7 nombres; con ThermalCurve rechazado,
el corpus estético de referencia es estos 6:

**StaggerStart — FlickerGuard — Thermo-Safe — ForensLog — TripleLock — TaskMemory**

### 1.1 Patrón morfológico

Los 6 anchor convergen en un mismo molde: **raíz evocadora + modificador funcional**.

- StaggerStart: raíz técnica (Stagger = escalonamiento) + acción primaria (Start)
- FlickerGuard: raíz del fenómeno (Flicker = perturbación sub-ciclo) + rol defensivo (Guard)
- Thermo-Safe: raíz del dominio físico (Thermo = temperatura) + atributo de estado (Safe)
- ForensLog: raíz conceptual (Forens = forense, registro con intención de análisis) + soporte (Log)
- TripleLock: cuantificador de evento (Triple = tercera falla) + consecuencia (Lock)
- TaskMemory: objeto de persistencia (Task = tarea operativa) + mecanismo (Memory)

El patrón no es siempre "raíz técnica + sufijo de protección". Es más amplio: una parte
del nombre carga el "qué ocurre o qué es" y la otra carga "qué hace el sistema con eso".
La segunda parte no siempre es defensiva — puede ser acción (Start), registro (Log),
persistencia (Memory).

La familia no tiene sufijo único dominante. Tiene sufijos de tres categorías:
- **Defensiva:** Guard, Safe, Lock
- **Operacional:** Start, Memory
- **De registro:** Log

### 1.2 Patrón fonético

Los 6 anchor cumplen tres condiciones fonéticas que deben sostenerse en la familia:

1. **Longitud:** 2 a 3 sílabas. Ningún anchor supera 3 sílabas. El rango óptimo es
   2 sílabas por parte (Fli-cker + Guard, Tri-ple + Lock). Nombres de 4+ sílabas
   en total se salen del registro.
2. **Consonantes duras:** todos los anchor tienen consonantes oclusivas o fricativas
   (k, g, t, r, s) que dan contundencia fonética. No hay nombres suaves o difusos.
   "FlickerGuard" tiene 3 consonantes duras; "TripleLock" tiene 2. La familia evita
   terminaciones en vocales abiertas o sílabas nasales finales débiles.
3. **Pronunciabilidad en español:** todos los anchor pueden pronunciarse sin
   ambigüedad en español venezolano o mexicano. No tienen dígrafos inusuales, no
   tienen secuencias de consonantes que no existan en español. Los candidatos nuevos
   deben pasar el mismo test.

### 1.3 Patrón semántico

Las 6 anchor evocan tres territorios semánticos que definen el portafolio:

- **Defensa activa** (no pasiva): el nombre evoca que el sistema hace algo —
  no solo protege. FlickerGuard "guarda" contra un evento en curso. TripleLock
  "cierra" ante acumulación de fallas. No son nombres de "protector genérico".
- **Precisión técnica nominativa**: el nombre usa vocabulario técnico en inglés que
  el especificador reconoce (Flicker, Stagger, Thermo, Forens) sin ser un descriptor
  funcional literal. La técnica es la raíz, no la descripción del mecanismo.
- **Consecuencia operativa**: varios anchor evocan el resultado del sistema, no el
  mecanismo interno (Safe, Lock, Memory, Start). El consumidor puede leer el nombre
  y entender "algo queda protegido" o "algo se recuerda" sin necesitar saber el
  algoritmo.

---

## 2. Reglas explícitas para Solenne

### 2.1 Sufijos aceptables (lista finita para la familia)

Los sufijos ya en uso en los anchor son el núcleo. Se admiten extensiones probadas
en la categoría eléctrica con perfil de fantasía. Lista completa:

| Sufijo | Categoría | Uso en anchor | Perfil de registro |
|--------|-----------|--------------|-------------------|
| **-Guard** | Defensiva | FlickerGuard | Medio — presente en clase 9, navegable con raíz específica |
| **-Safe** | Defensiva | Thermo-Safe | Medio-alto — ver Gate 3 Bruna; funciona con raíz no térmica |
| **-Lock** | Defensiva | TripleLock | Medio — ver contingencia Gate 6; con raíz no numérica sola, más limpio |
| **-Start** | Operacional | StaggerStart | Bajo riesgo — genérico solo, diferenciado con raíz técnica |
| **-Memory** | Operacional | TaskMemory | Medio — riesgo colisión software; con raíz no informática, navegable |
| **-Log** | Registro | ForensLog | Medio — genérico solo; diferenciado con raíz forense o técnica específica |
| **-Shield** | Defensiva | — | Aceptable — menos saturado que -Guard en clase 9 eléctrica |
| **-Hold** | Operacional | — | Aceptable — connota retención, compatible con nodos de persistencia o bloqueo |
| **-Watch** | Diagnóstico | — | Aceptable — connota monitoreo activo; útil para nodos de registro |
| **-Pulse** | Técnica | — | Aceptable — connota señal eléctrica; útil para nodos de detección |
| **-Gate** | Defensiva/lógica | — | Aceptable — connota control de flujo, compatible con bloqueo o lógica |
| **-Block** | Defensiva | — | Aceptable — alternativa a -Lock con menos saturación en seguridad física |
| **-Trace** | Registro | — | Aceptable — compatible con nodos de diagnóstico/registro |

### 2.2 Sufijos a evitar

Los siguientes sufijos están prohibidos o requieren revisión exhaustiva antes de usar:

| Sufijo | Razón |
|--------|-------|
| **-Pro** | Genérico de gama; no aporta diferenciación; saturado en toda la clase 9 |
| **-Plus** | Ídem —sufijo de versión, no de tecnología |
| **-Max** | Ídem — superlativo de relleno sin carga semántica específica |
| **-Smart** | Saturado como sufijo y prefijo en clase 9 global; riesgo alto de colisión |
| **-Tech** | Descriptor de categoría, no de tecnología específica |
| **-Net** | Saturado en software y redes; riesgo de colisión clase 9 alta |
| **-Link** | GIO-Link ya existe como nombre de producto Genteca (accesorio); no duplicar |
| **-Tool** | GIO-Tool ya existe como nombre de producto Genteca; no duplicar |
| **-Port** | GIO-Port ya existe como denominación Genteca; no duplicar |
| **-Stop** | Demasiado descriptivo de función de desconexión para clase 9 eléctrica |
| **-Guard** (solo, sin raíz específica) | Genérico sin raíz diferenciadora; solo funciona con raíz técnica |

### 2.3 Prefijos y raíces: reglas de uso

**Prefijos con guión admitidos:**
- **Thermo-** (ya en uso en Thermo-Safe): admitido con guión para NODO-C candidatos
  adicionales si Solenne lo considera coherente. No repetir en otros nodos — Thermo-
  es la raíz de NODO-C; usarla en otro nodo crea confusión de familia interna.
- **GIO-** (NODO-H): admitido y recomendado como prefijo con guión para los candidatos
  del ecosystem. GIO-* es el territorio más limpio y con mejor perfil de registro para
  ese nodo (BR-2 Gate 8 confirmado). Solenne tiene libertad plena dentro de GIO-*.

**Prefijos sin guión:**
- **Tri-** (ya en TripleLock como "Triple"): el cuantificador numérico es el patrón
  de NODO-F. Si Solenne genera candidatos adicionales para NODO-F con -Gate, -Block
  o -Hold como sufijo, puede mantener "Triple" como prefijo o buscarlo sin prefijo
  numérico si la búsqueda sectorial de TripleLock resulta problemática.
- **Auto-**: aceptable pero con precaución. "Auto-" tiene saturación en clase 9
  automotriz/automatización. Solo si la raíz que sigue es técnicamente específica
  y la combinación no es descriptiva de la función.
- **Stagger-** (ya en StaggerStart): raíz de NODO-A. No usar en otros nodos.
- **Flicker-** (ya en FlickerGuard): raíz de NODO-B. No usar en otros nodos.
- **Forens-** (ya en ForensLog): raíz de NODO-E. No usar en otros nodos.
- **Task-** (ya en TaskMemory): raíz de NODO-G. No usar en otros nodos excepto para
  los candidatos alternativos de IMPI MX del mismo nodo.

**Prefijos prohibidos sin excepción:**
- **MODBUS**, **Modbus**, **RS-485**, **RS485**, **IO-Link**, **EtherNet**, **DeviceNet**,
  **PROFIBUS**: protocolos estándar de terceros. Prohibición absoluta (BR-2 Gate 8).
- **SIMO**, **TeSys**, **EcoStruxure**, **Xpert** (en combinación con Power): marcas
  registradas de terceros.
- **Thermal-** como prefijo autónomo para cualquier nodo: territorio de descriptividad
  para NODO-D. Bruna rechazó ThermalCurve precisamente por la combinación de raíz
  térmica con descriptor de función. No reingresar Thermal- como prefijo en nombres
  de NODO-D.

### 2.4 Longitud objetivo

- **2-3 sílabas por parte del nombre.** El total del nombre compuesto no debe superar
  5-6 sílabas.
- Los anchor más cortos (TripleLock: 4 sílabas en total; FlickerGuard: 4 sílabas)
  son el referente de contundencia. Los más largos del corpus son StaggerStart (4) y
  TaskMemory (4). No superar ese límite.
- Nombres de una sola raíz sin sufijo (monopalabra corta) son aceptables si tienen
  fantasia clara y pronunciabilidad correcta — pero ningún anchor del portafolio usa
  ese patrón, así que es territorio no explorado; Solenne debe notar si lo usa.

### 2.5 Capitalización: estándar de la familia

**CamelCase interno sin espacio.** Ese es el estándar del portafolio:

- StaggerStart, FlickerGuard, ForensLog, TripleLock, TaskMemory → CamelCase, una palabra.
- Thermo-Safe es la única excepción: usa guión por decisión de naming del anchor.
  El guión en Thermo-Safe no crea precedente para el resto — es específico de ese nombre.

**Regla para candidatos nuevos:**
- CamelCase sin guión como default para nombres nuevos.
- Guión permitido solo para la familia GIO-* (NODO-H), donde el guión es parte
  establecida de la denominación propietaria (GIO-Link, GIO-Tool, GIO-Port ya lo usan).
- En candidatos de NODO-C adicionales que usen el prefijo Thermo-, se admite el guión
  para mantener coherencia con Thermo-Safe. Para cualquier otro prefijo, CamelCase
  sin guión.

---

## 3. Reglas de coherencia entre nodos

### 3.1 Agrupaciones semánticas y si deben expresarse visualmente en el nombre

Los 8 nodos se agrupan en 3 pilar-clusters según el VA-1:

| Pilar | Nodos | Tema común |
|-------|-------|------------|
| Pilar 1 — Inteligencia anticipatoria | A (StaggerStart), B (FlickerGuard), D (sin anchor) | El sistema actúa antes del daño |
| Pilar 2 — Memoria operativa | A (StaggerStart), G (TaskMemory) | El proceso continúa sin intervención |
| Pilar 3 — Diagnóstico y cierre | E (ForensLog), F (TripleLock) | El sistema registra y cierra el ciclo |
| Pilar 4 — Ecosystem integrado | H (Ecosystem GIO) | Conectividad propietaria como sistema |

**Regla de coherencia entre nodos del mismo pilar:**
Los nombres dentro del mismo pilar no necesitan un patrón morfológico visible
que los relacione. La coherencia es semántica (lo que evocan), no estructural
(no necesitan el mismo sufijo). FlickerGuard y StaggerStart comparten Pilar 1
sin compartir sufijo ni estructura — y funcionan.

Sin embargo, hay una regla negativa: **ningún par de nodos del mismo pilar
puede tener el mismo sufijo si eso crea confusión de qué protege qué**.
Ejemplo: si NODO-D usa -Guard, y NODO-B ya tiene FlickerGuard, Solenne debe
asegurarse de que el nombre de NODO-D con -Guard no se confunda con FlickerGuard
ante el abogado o ante el especificador.

### 3.2 Contingencias: coherencia de los candidatos alternativos

Los nodos NODO-B, NODO-F y NODO-G tienen contingencias explícitas por gates de
colisión (BR-2 Gates 5, 6, 7). Las reglas de coherencia para los candidatos de
contingencia son más estrictas que para los candidatos principales:

- **NODO-B contingencias (colisión OMPI FlickerGuard):** los candidatos alternativos
  deben mantener el mismo registro fonético y defensivo que FlickerGuard. Raíces
  en el territorio sub-ciclo/perturbación son el espacio correcto: Pulse-, Sag-,
  Surge-, Spike-. El sufijo puede ser -Guard, -Shield o -Block. Evitar candidatos
  de contingencia que suenen más débiles fonéticamente que FlickerGuard — si hay
  colisión, el reemplazo debe sostener el posicionamiento, no degradarlo.
- **NODO-F contingencias (colisión sectorial TripleLock):** los candidatos alternativos
  deben mantener la connotación de bloqueo deliberado tras acumulación de fallas.
  Sufijos aceptables: -Gate, -Hold, -Block. Evitar -Lock como raíz alternativa
  (el problema es precisamente "Lock"). El cuantificador "Triple" puede mantenerse
  o no según lo que la búsqueda del abogado confirme.
- **NODO-G contingencias IMPI MX (colisión software TaskMemory):** los candidatos
  alternativos para IMPI MX deben alejarse de la combinación Task+Memory pero
  preservar la evocación de continuidad del proceso sin intervención. Las raíces
  Mode-, State-, Cycle- son el territorio correcto.

### 3.3 No crear mini-sistemas de nombres internos

El portafolio es de nombres stand-alone independientes (charter §3 decisión 3). No
se deben crear nombres que parezcan "versiones" uno del otro (FlickerGuard / FlickerShield /
FlickerBlock para distintos nodos). Cada nodo tiene su raíz propia. La coherencia de
familia viene del patrón CamelCase + morfología raíz/sufijo + registro fonético, no de
raíces compartidas entre nodos distintos.

---

## 4. Reglas de territorio prohibido

### 4.1 NODO-D: todo lo que rodea a ThermalCurve

Bruna rechazó ThermalCurve por descriptividad de función estándar IEC. Los 4 candidatos
de NODO-D son todos nuevos. El territorio vedado para NODO-D es amplio:

| Territorio vedado | Razón |
|------------------|-------|
| Cualquier raíz con **Thermal-, Thermo-** (en NODO-D) | Raíz térmica en NODO-D recrea el problema de ThermalCurve. Thermo- está reservado para NODO-C (Thermo-Safe). |
| Sufijo o raíz **-Curve, Curve-** | El nombre rechazado; describe literalmente el mecanismo IEC. |
| **Thermic-, Heat-, Hot-, Cold-** como raíces autónomas para NODO-D | Todos son descriptores directos del estado del motor en el mecanismo cold/hot. |
| **Adapt-** como única raíz sin carga técnica adicional | Demasiado genérico — describe cualquier función adaptativa; sin especificidad de nodo. |
| **IEC, IEEE** o cualquier referencia a estándar en el nombre | Describe el origen normativo de la función, no la función Genteca. |

**Dirección positiva para NODO-D:** la dirección semántica correcta es la adaptación
al estado real del motor, no la curva algorítmica. El beneficio del beneficio es que
el motor no dispara prematuro en caliente ni queda desprotegido en frío. Los candidatos
deben evocar esa adaptación de estado, no el mecanismo IEC. Ver §6 (calibración por nodo)
para la dirección semántica completa.

### 4.2 NODO-H: protocolo estándar y denominaciones GIO ya en uso

| Territorio vedado | Razón |
|------------------|-------|
| **MODBUS, Modbus** (cualquier capitalización) | Marca registrada de tercero (Modbus Organization). Prohibición absoluta. |
| **IO-Link, IO Link** | Nombre de protocolo estándar de tercero (IFM, PROFIBUS International). |
| **PROFIBUS, DeviceNet, EtherNet/IP, RS-485, SPI, I2C** | Protocolos estándar de terceros. |
| **GIO-Link** | Nombre de producto Genteca ya en uso como accesorio. No usar como nombre de marca de tecnología nueva. |
| **GIO-Tool** | Ídem — software existente. |
| **GIO-Port** | Ídem — denominación de la interfaz física existente. |

**Sobre GIO como prefijo libre:** Solenne tiene plena libertad para crear nombres
GIO-* que no sean los tres ya en uso. GIO-Net, GIO-Mesh, GIO-Bus, GIO-Core u otros
son territorio disponible. Esta es la vía recomendada por Bruna (Gate 8). Candidatos
completamente nuevos sin raíz GIO también son posibles — pero deben pasar el filtro
de no aludir al protocolo subyacente.

### 4.3 Otros territorios vedados por precedentes de la familia

| Territorio vedado | Nodo afectado | Razón |
|------------------|--------------|-------|
| **"Insight", "Motor Insight"** | Todos | Nombre comercial registrado Eaton C441. |
| **"SIMOCODE", "SIMO-"** | Todos | Marca Siemens registrada. |
| **"TeSys", "TeSys-"** | Todos | Marca Schneider registrada. |
| **"EcoStruxure"** | Todos | Marca Schneider registrada. |
| **"Power Xpert", "Xpert"** (con Power) | Todos | Marca Eaton registrada. |
| **"Thermal Memory"** como combinación | NODO-D | Término genérico usado en múltiples fabricantes (Orlan OL-1). |
| **"Smart Motor Control"** | Todos | Nombre Rockwell. |
| **"Voltage Loss Restart"** | NODO-A | Nombre descriptivo Eaton — no es marca de fantasía registrada, pero evitar para no crear confusión de precedente. |

### 4.4 Territorio vedado por VA-5 (anti-mensajes de Vael)

Los anti-mensajes del VA-5 §3 tienen implicaciones directas para el naming:

- No usar raíces que impliquen **"único" o "exclusivo"** como componente semántico
  (el nombre no puede reclamar lo que el claim no puede sostener).
- No usar raíces que impliquen **"inteligencia artificial" o "aprendizaje automático"**
  (Genius/Smart/AI/Learn) en NODO-G: TaskMemory es persistencia de estado, no IA.
- No usar raíces que impliquen **precisión absoluta de temperatura** en NODO-C:
  los parámetros cuantitativos del NTC no están en HDE actual.

---

## 5. Patrón de "carga" del nombre por audiencia

### 5.1 La regla general

El portafolio es de marcas stand-alone clase 9 — el nombre existe para registro IP,
no para campaña de consumidor. El criterio primario es registrabilidad + potencia
ante el abogado marcario. El criterio secundario es que el nombre sostenga el valor
comercial de la tecnología ante la audiencia primaria del nodo.

No hay una regla que diga "nombres de NODO-A más expresivos, nombres de NODO-F más
técnicos". Los 6 anchor ya existentes mezclan ambos registros sin distinción de nodo.
La calibración por audiencia opera en el messaging (VA-1), no en la morfología del
nombre.

### 5.2 La excepción aplicable: Exceline residencial

Para los nodos cuya audiencia primaria es residencial (NODO-A, NODO-B, NODO-C),
hay una preferencia, no una regla estricta: los candidatos que priorizan la evocación
del beneficio del beneficio (lo que el consumidor siente, no el mecanismo) tienen
mayor potencia comercial en ese segmento.

- NODO-A (StaggerStart): el consumidor residencial no necesita entender "stagger".
  El anchor ya está fijado. Los 3 candidatos adicionales pueden explorar el beneficio
  del beneficio (el arranque coordinado, el sistema que no colapsa) con más libertad.
- NODO-B (FlickerGuard): el anchor ya está fijado con raíz técnica. Los candidatos
  adicionales pueden explorar nombres que evoquen la consecuencia (el equipo que no se
  daña por parpadeo) si hay colisión y FlickerGuard cae.
- NODO-C (Thermo-Safe): el anchor prioriza el atributo de estado (Safe). Los candidatos
  adicionales pueden explorar la integración (la completitud de la protección) o el
  resultado (el motor protegido).

Para los nodos cuya audiencia primaria es Exceline Profesional o Genius/Especificadores
(NODO-D, NODO-E, NODO-F, NODO-G, NODO-H), la raíz técnica es preferible: los
especificadores e instaladores valoran la precisión semántica. Eso no significa
que el nombre sea un descriptor funcional — significa que puede tener mayor densidad
técnica sin perjuicio comercial.

### 5.3 No es obligatorio diferenciar nombre por línea

Genteca puede usar el mismo nombre (ej. ForensLog) ante un especificador técnico y
en el deck para el abogado. No se generan versiones del nombre por audiencia. La carga
de audiencia va en el messaging y en el beneficio del beneficio que Vivienne incluye
en el slide — no en el nombre en sí.

---

## 6. Notas de calibración por nodo

Para cada nodo: anchor post-Bruna / dirección semántica primaria / territorio vedado /
audiencia primaria. Una línea operativa por dimensión.

---

### NODO-A — StaggerStart

- **Anchor:** StaggerStart (confirmado por Bruna, sin gate pendiente)
- **Dirección semántica primaria:** escalonamiento en el arranque como mecanismo que
  previene el pico de demanda simultáneo. El beneficio del beneficio para residencial:
  el compresor no recibe el golpe eléctrico junto con todos los demás. Los 3 candidatos
  adicionales pueden explorar la secuencia ordenada o la estabilidad del arranque conjunto.
- **Territorio vedado:** "Restart", "Reconnect", "Voltage Loss" (Eaton) como raíces
  autónomas. "Exclusive", "único" como connotación. No usar prefijo Stagger- en otros
  nodos.
- **Audiencia primaria:** Exceline residencial y Exceline Profesional (doble audiencia).
  Nombre debe funcionar para instaladores en campo y para el consumidor de AC en casa.

---

### NODO-B — FlickerGuard

- **Anchor:** FlickerGuard (aprobado con contingencia OMPI — anchor principal; Solenne
  genera candidatos alternativos marcados "contingencia OMPI")
- **Dirección semántica primaria:** protección ante perturbación sub-ciclo de voltaje
  antes de que el estrés llegue al motor. El RTB es 20ms. Los candidatos adicionales
  (incluyendo los de contingencia) permanecen en el territorio de detección-protección
  ante fenómenos eléctricos rápidos.
- **Territorio vedado:** "único protector que detecta flicker" como connotación. Raíces
  LED (Flicker en iluminación — riesgo OMPI que motiva la contingencia). "SagStop",
  "FlickerStop" (demasiado descriptivos). No usar raíz Flicker- en otros nodos.
- **Audiencia primaria:** Exceline residencial (el compresor del AC / del refrigerador).

---

### NODO-C — Thermo-Safe

- **Anchor:** Thermo-Safe (aprobado con caveat Caso A — nombre válido con argumento
  de fantasia para el abogado)
- **Dirección semántica primaria:** integración de protección térmica real (NTC hardware)
  en el protector — sin módulo adicional, sin cableado externo. El mensaje es la
  completitud de la protección en un solo dispositivo. Los 3 candidatos adicionales
  pueden explorar integración, completitud o la protección del motor ante calor no
  detectado.
- **Territorio vedado:** parámetros cuantitativos del NTC como raíz (umbral de temperatura,
  rango exacto — no están en HDE). "ThermoGuard", "ThermoShield", "ThermoProtect"
  (presencia en marcas europeas, OL-1). "Exacta", "precisa", "continua" como connotación.
  No usar prefijo Thermo- fuera de NODO-C para no crear confusión interna de familia.
- **Audiencia primaria:** Exceline residencial y Exceline Profesional.

---

### NODO-D — Sin anchor (ThermalCurve rechazado)

- **Anchor:** ninguno. Los 4 candidatos son todos nuevos.
- **Dirección semántica primaria:** adaptación al estado real del motor (motor en frío
  vs motor en caliente al momento del arranque). El disparo llega cuando el motor lo
  necesita — ni prematuro en caliente ni tardío en frío. Los candidatos deben evocar
  adaptación de estado, respuesta proporcional al estado real, o la inteligencia de
  distinción cold/hot — sin nombrar el mecanismo IEC.
- **Territorio vedado:** Thermal-, Thermo-, Heat-, Hot-, Cold- como raíces de nombre
  (describen el fenómeno, no la función diferenciadora). -Curve y Curve- (nombre
  rechazado). "Propietario", "exclusivo" como connotación del algoritmo (no documentado
  como propietario — Bruna Gate 2 fue explícito). "La protección térmica más avanzada"
  como carga semántica del nombre.
- **Audiencia primaria:** Exceline Profesional e Ingenieros especificadores (Genius).
  Nombre con densidad técnica es aceptable — el consumidor residencial no es la audiencia
  primaria de este nodo.

---

### NODO-E — ForensLog

- **Anchor:** ForensLog (aprobado, postura Escenario A — RTB anclado en GIII+MV)
- **Dirección semántica primaria:** registro forense de fallas con connotación de
  auditoría y reconstrucción técnica — "evidencia" más que "datos". Los 3 candidatos
  adicionales mantienen el territorio forense-técnico o de registro-diagnóstico.
- **Territorio vedado:** "100 fallas en toda la gama Genius" como connotación (el RTB
  de 100 es solo GIII+MV). "FaultLog", "EventLog", "DataLog" como candidatos (demasiado
  genéricos — menor potencia y riesgo de colisión en software). "El único relé con
  registro forense" como carga semántica.
- **Audiencia primaria:** Exceline Profesional y especificadores técnicos (Genius). El
  nombre no necesita resonar con el consumidor residencial.

---

### NODO-F — TripleLock

- **Anchor:** TripleLock (aprobado con contingencia sectorial — anchor principal; Solenne
  genera candidatos alternativos marcados "contingencia sectorial" con raíces -Gate,
  -Hold, -Block en lugar de -Lock)
- **Dirección semántica primaria:** bloqueo permanente y deliberado ante acumulación
  de fallas — el sistema no permite rearranque automático, obliga intervención técnica.
  La connotación correcta es control de ciclo destructivo, no cerradura física.
- **Territorio vedado:** "Lock" en el contexto de seguridad física (el riesgo de colisión
  que motiva la contingencia). "El único sistema de bloqueo" como carga. "Total" como
  atributo del bloqueo (no aplica a todos los escenarios de falla — VA-5 lo rechaza).
  No usar prefijo Triple- en otros nodos.
- **Audiencia primaria:** Exceline Profesional y Genius. El motor industrial no entra
  en ciclo destructivo de falla-rearranque-falla.

---

### NODO-G — TaskMemory

- **Anchor:** TaskMemory (aprobado para SAPI Venezuela; Solenne genera 2 candidatos
  alternativos adicionales etiquetados "para IMPI MX si colisión software")
- **Dirección semántica primaria:** continuidad del proceso operativo sin intervención
  humana post-corte. El GRN-MV recuerda en qué modo estaba y retoma. Los 3 candidatos
  adicionales (incluyendo los de contingencia MX) evocan retomar, persistir, continuar
  el proceso físico — alejados del vocabulario software.
- **Territorio vedado:** "Task" + "Memory" en combinación para candidatos MX (riesgo
  colisión software en IMPI — BR-2 Gate 7). "Aprender", "rutina", "IA", "inteligente"
  como connotación (el mecanismo es persistencia de modo, no aprendizaje). "Toda la
  gama Exceline Profesional" como alcance (es función específica del GRN-MV).
- **Audiencia primaria:** Exceline Profesional (GRN-MV, instalaciones de bombeo y riego).

---

### NODO-H — Ecosystem GIO

- **Anchor:** ninguno anchor previo (el nodo fue reformulado en Checkpoint 1). Los 4
  candidatos son nuevos. La familia GIO-* es el territorio recomendado.
- **Dirección semántica primaria:** ecosystem integrado desde el diseño — no conectividad
  genérica sino el sistema propietario (GIO PORT + GIO-Link + GIO-Tool + red hasta 32
  relés) como diferenciador de la gama Genius. Los nombres deben evocar sistema integrado,
  red propia, acceso a la información del relé — no el protocolo subyacente.
- **Territorio vedado:** MODBUS, RS-485, IO-Link, PROFIBUS, DeviceNet, EtherNet/IP y
  cualquier término de protocolo estándar (prohibición absoluta BR-2 Gate 8). GIO-Link,
  GIO-Tool, GIO-Port (nombres de producto ya en uso — no duplicar). "Conectividad sin
  límites", "para toda la gama Genteca" como carga (solo aplica a Genius).
- **Audiencia primaria:** Especificadores técnicos (transversal Genius) e Ingenieros de
  mantenimiento industrial.

---

## Cover note a Solenne

**De:** Vael
**Para:** Solenne, Phase 4
**Asunto:** Reglas firmes, libertades y territorios vedados para los 32 candidatos

---

**Estado de arranque:**
- 6 anchors confirmados por Bruna: StaggerStart (A), FlickerGuard (B), Thermo-Safe (C),
  ForensLog (E), TripleLock (F), TaskMemory (G).
- NODO-D: 0 anchors. Los 4 candidatos son completamente nuevos.
- NODO-H: 0 anchors previos. Los 4 candidatos son nuevos dentro del espacio GIO-*.
- Conteo base: 32 candidatos. Más contingencias para B (OMPI), F (sectorial), G (IMPI MX)
  como filas extra en la Naming Bible — no son parte de los 32 base.

**Reglas firmes (no negociables):**

1. CamelCase sin espacio como estándar. Guión solo para GIO-* y Thermo-* en NODO-C.
2. Longitud máxima: 5-6 sílabas en total por nombre.
3. Cero uso de: MODBUS, RS-485, IO-Link, PROFIBUS, DeviceNet, EtherNet/IP (protocolos de
   terceros) — ni como raíz, sufijo, ni evocación directa.
4. Cero uso de marcas de terceros: SIMOCODE, TeSys, EcoStruxure, Motor Insight, Xpert.
5. Cero nombres que repitan raíces entre nodos distintos (Stagger-, Flicker-, Thermo-,
   Forens-, Task- son raíces exclusivas de su nodo).
6. NODO-D: cero Thermal-, Thermo-, -Curve, Heat-, Hot-, Cold- como raíces de nombre.
7. NODO-H: los candidatos anclan en GIO-* o son nombres completamente nuevos sin aludir
   al protocolo subyacente. Ninguno puede contener GIO-Link, GIO-Tool, ni GIO-Port
   (ya existen como denominaciones de producto).
8. Sufijos prohibidos en toda la familia: -Pro, -Plus, -Max, -Smart, -Tech, -Stop.
9. Los candidatos de contingencia para B, F y G llevan etiqueta en la Naming Bible
   ("contingencia OMPI", "contingencia sectorial", "para IMPI MX si colisión software").
   No son candidatos principales.

**Libertades:**

- Dentro de los sufijos aceptables del §2.1, libertad total de combinación con nuevas
  raíces. No hay una lista cerrada de raíces.
- Para NODO-D, el espacio semántico de adaptación/estado/respuesta proporcional está
  completamente abierto — no hay anchor que herede, no hay restricciones morfológicas
  más allá de las reglas generales de la familia.
- Para NODO-H con prefijo GIO-, todo lo que no sea GIO-Link, GIO-Tool y GIO-Port es
  territorio libre.
- La profundidad técnica vs evocación de beneficio es decisión de Solenne nodo por nodo,
  dentro de la orientación de audiencia del §5. No hay regla que fuerce todos los nombres
  hacia un registro único.
- Los candidatos de contingencia tienen mayor libertad semántica que los candidatos
  principales — su función es proveer alternativas viables si hay colisión, no replicar
  la potencia del anchor.

**Territorios vedados principales (mapa rápido):**

| Nodo | Prohibición clave |
|------|------------------|
| A | Restart, Reconnect, Voltage Loss (Eaton) |
| B | LED + Flicker (OMPI), SagStop, FlickerStop |
| C | Parámetros cuantitativos NTC, ThermoGuard/Shield/Protect |
| D | Todo lo "Thermal-", "-Curve", "exclusivo", "propietario" sin RTB |
| E | FaultLog, EventLog, DataLog (genéricos), "100 fallas en gama completa" |
| F | -Lock en contexto seguridad física (contingencias), "Total" como atributo |
| G | Task+Memory en candidatos MX, "aprender", "IA", "toda la gama" |
| H | MODBUS y derivados, GIO-Link/Tool/Port (ya en uso), "toda la gama Genteca" |

Sin preguntas abiertas al Owner desde este documento. Todo lo necesario para generar
los 32 candidatos está aquí. Si Solenne encuentra al generar que alguna dirección
semántica de un nodo es insuficiente, el escalamiento es a Raul, no a Owner directamente.

---

## Supuestos y límites

**Insumos aguas arriba:**
- Vael VA-1 v1.0 (2026-05-13): arquitectura de mensajes y dirección semántica por nodo.
- Vael VA-5 v1.0 (2026-05-13): guardrails de claims por nodo.
- Bruna BR-2 v1.0 (2026-05-13): decisiones formales de gates 1-8. Este VA-6 implementa
  todas las implicaciones para Solenne del BR-2. No hay reinterpretación — las implicaciones
  para Phase 4 descritas en cada gate del BR-2 están directamente mapeadas a las reglas
  de §4 y §6 de este documento.
- Orlan OL-1 v1.0 (2026-05-13): espacio semántico saturado y notas por nodo para Solenne.
- Charter v1.0 (2026-05-13): §3 (arquitectura stand-alone, anglicismos, 4 candidatos), §5
  (audiencias por línea), §6 (beneficio del beneficio).

**Validez temporal:** Este VA-6 es válido mientras el BR-2 de Bruna no cambie y mientras
los nombres anchor confirmados no sean invalidados por la búsqueda formal del abogado.

**Triggers de invalidación:**
- Búsqueda formal del abogado confirma colisión activa en SAPI/IMPI para FlickerGuard:
  las contingencias de NODO-B pasan a candidatos principales; las reglas de §4 para
  ese nodo se mantienen.
- Búsqueda formal confirma colisión activa para TripleLock: contingencias de NODO-F
  pasan a principales.
- Búsqueda IMPI MX confirma colisión software para TaskMemory: los candidatos alternativos
  etiquetados "para IMPI MX" toman el lugar para esa jurisdicción.
- Vera actualiza VR-1 con RTB diferenciador propietario para NODO-D: este VA-6 debe
  actualizarse en §6 NODO-D y en §4.1 para reflejar la nueva dirección semántica
  disponible (si el RTB permite raíces hasta ahora prohibidas).
- Bruna emite BR-2 actualizado con algún gate adicional: actualizar §4 y §6 correspondientemente.

**Decisiones Owner pendientes:** ninguna que bloquee Phase 4. Los 8 nodos tienen instrucción
suficiente para que Solenne arranque.

**Claims con gate pendiente:** ninguno en este documento — los gates de VA-5 ya fueron
resueltos por Bruna en BR-2. Este VA-6 solo implementa las implicaciones de esas decisiones.

---

*Vael — VA-6 Phase 4 completo. Listo para Solenne.*
