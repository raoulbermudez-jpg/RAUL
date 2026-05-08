# Protocolo de selección de producto Genteca — Protección de motores trifásicos

**Audiencia:** Vera, Solenne, Orlan, ingenieros de mantenimiento, técnicos comerciales que necesitan resolver casos de selección de producto.
**Origen:** integrado desde RAG Integrador v2 legacy (marzo 2026), curado por Vera 2026-05-07. Secciones 4 (Q&A) y 5 (Protocolo) del RAG; con neutralización de productos cuyo estado no está confirmado.

> **Notas operativas:**
> - **Estado de productos:** este documento describe productos GENTECA confirmados como activos en el portafolio. Los GST-RD (supervisor con LCD e histórico) y GST-RG (curva inversa tiempo-voltaje) figuraban en marzo 2026 como "en desarrollo próximo"; al 2026-05-07 **su estado de disponibilidad NO está confirmado** — pendiente aclaración con engineering antes de mencionarlos a clientes.
> - **Argumentos de venta:** las frases que pueden usarse con clientes están marcadas como "uso interno verificable"; las que requieren validación adicional están marcadas como "pendiente gate Bruna" — ver `argumentos-venta-tecnicos-INTERNO-PENDIENTE-GATE.md`.

---

## 1. Familia de productos GENTECA — mapa actual

### Exceline Profesional — solo voltaje

| Modelo | Variantes | Aplicación |
|---|---|---|
| GST-RM | 220V, 440V | Motores, transferencias, distribución |
| GST-RR | 220V, 440V | Refrigeración y A/A; anti-short cycle 180s en hardware |

### Exceline Profesional — voltaje + corriente

| Modelo | Variantes | Aplicación |
|---|---|---|
| GSC-MB | 220V (12/32/80A), 440V (32/80A) | Motores y bombas — uso general |
| GSC-CR | 220V (12/32/80A), 440V (32/80A) | Compresores refrigeración / A/A; anti-short cycle 180s en hardware |

### Genius — solo voltaje

| Modelo | Variantes | Aplicación |
|---|---|---|
| GII+ | 120V, 208/220V, 440/480V; con o sin programador horario | Cargas trifásicas con diagnóstico LCD + MODBUS |

### Genius — voltaje + corriente

| Modelo | Variantes | Aplicación |
|---|---|---|
| GUCT+ | 208V/480V × 04/12/32/80A; con o sin horario | Motores con clase térmica ajustable, MODBUS |
| GIII | 120/208/480V × 050/100/180A o CT externos; con o sin horario | Alta potencia, RS-485 nativo, integración SCADA |
| GSPT | 208V/480V × 04/12/32/80A | Bombas — clase 10 fija + límite arranques NEMA MG10 |
| GSPT-MV | Multivoltaje × 050/100/180A | Bombas grandes / sumergibles con PT100 |

> **Productos pendientes de confirmar disponibilidad** (no usar con cliente sin verificar con engineering): GST-RD, GST-RG.

---

## 2. Protocolo de selección paso a paso

### PASO 1 — ¿Cuál es la aplicación?

| Aplicación | Rama |
|---|---|
| Compresor de refrigeración o A/A | Rama A: Compresor |
| Bomba (superficial o sumergible) | Rama B: Bomba |
| Motor de uso general | Rama C: Motor general |

### PASO 2A — Rama compresor

¿Solo protección de voltaje (contactor externo)?
→ **GST-RR** (220V o 440V según sistema).

¿Protección voltaje + corriente + anti-short cycle?
→ **GSC-CR** (modelo según voltaje y corriente del compresor).

¿Doble capa de protección (recomendado para herméticos)?
→ **GSC-CR + GST-RR** — ambos con anti-short cycle de 180s en hardware. Si uno se ajusta mal, el otro lo cubre.

¿Se requiere MODBUS o clase térmica ajustable?
→ **GUCT+ (Genius) + GST-RR (Exceline Profesional)**.

### PASO 2B — Rama bomba

**¿Bomba superficial, corriente ≤80A?**

| Sub-criterio | Producto |
|---|---|
| Sin diagnóstico avanzado | **GSC-MB** |
| Con diagnóstico, MODBUS, límite arranques | **GSPT** (Genius) |

**¿Bomba sumergible (riesgo marcha en seco)?**

| Sub-criterio | Producto |
|---|---|
| ≤50HP@440V o ≤25HP@220V, motor con termistor instalado | **GSPT** + PT100 externo |
| ≤50HP@440V o ≤25HP@220V, motor sin termistor instalado | **GSPT-MV** + PT100 integrado |
| >50HP@440V o necesidad multivoltaje | **GSPT-MV** (050/100/180 según corriente) |

¿Además se requiere supervisor de red (doble capa)?
→ Agregar **GST-RM** (220V o 440V).

### PASO 2C — Rama motor general

| Sub-criterio | Producto |
|---|---|
| ≤50HP@440V, sin requisitos avanzados | **GSC-MB** |
| Red CORPOELEC particularmente inestable | **GSC-MB + GST-RM** |
| Clase térmica ajustable requerida (arranque largo >8s) | **GUCT+** |
| Alta potencia (>50HP@440V o >25HP@220V) | **GUCT+480-80** o **GIII** según necesidad de PT100/RS485/entradas digitales |
| Integración SCADA intensiva | **GIII** (RS-485 nativo + entradas digitales) |

### PASO 3 — Calidad de la red

Si la instalación tiene historial de desequilibrios >5%, subtensiones frecuentes o cortes selectivos frecuentes:
- Agregar capa de supervisión voltaje: **GST-RM** (motores) o **GST-RR** (compresores)
- Alternativa: producto Genius con GII+ integrado para visualización local de calidad de red

### PASO 4 — Verificar la corriente del modelo

1. Obtener In del motor de la placa.
2. Verificar que In esté dentro del rango ajustable del modelo seleccionado.
3. Para GSC-MB/CR: ajustar perilla FLA exactamente al In.
4. Para GUCT+/GSPT: configurar parámetro de corriente nominal al In.
5. Si motor tiene FS=1.15: ajustar al valor In × 1.15 para aprovechar el FS.

> **Margen:** si In está cerca del límite superior del rango del modelo, elegir el siguiente modelo mayor. Ejemplo: motor 12A → GSC-MB22012 va justo en el límite; considerar GSC-MB22032.

---

## 3. Rutas técnicas — falla → producto Genteca

### Ruta: Falta de fase

**Mecanismo:** motor monofásico → corriente 200-300% en fases restantes → daño rápido.
**Detección estándar:** monitor de red (<500ms) o relé electrónico (<1s).
**Aplicaciones críticas:** compresores herméticos (no rebobinables), sumergibles.

| Producto | Detección |
|---|---|
| GST-RM / GST-RR | VSP por voltaje (IN>33%, OUT<28%) en <0.5s |
| GSC-MB / GSC-CR | Pérdida de fase por corriente (CUB>60%) en 3s |
| GII+ | VSP en <1s; reporte histórico + MODBUS |
| GUCT+ / GSPT / GIII | CSP (IN>60%) en <3s + VSP por voltaje |

**Combinación óptima:** GSC-MB + GST-RM = doble detección (voltaje + corriente).

### Ruta: Desequilibrio

**Mecanismo:** desequilibrio típico Venezuela 3-8% → temperatura motor +25-50%.
**Detección:** voltimétrica (monitor de red) o amperimétrica (relé electrónico).

| Producto | Detección |
|---|---|
| GST-RM / GST-RR | VUB IN ±8%, OUT ±6% — detecta desequilibrio >8% |
| GSC-MB / GSC-CR | CUB IN >48% — desequilibrio de corriente severo |
| GII+ | VUB ajustable 2-10%; reporte de % de desbalance en LCD |
| GUCT+ / GIII / GSPT | VUB + CUB — doble detección |

**Nota:** los GST detectan desbalance antes que los GSC (voltaje antes que corriente).

### Ruta: Marcha en seco

**Mecanismo crítico:** corriente puede BAJAR cuando bomba opera sin agua. Relé corriente NO detecta.
**Detección:** PTC o sensor de proceso (presostato, sensor de caudal). Relé de sobrecarga estándar no detecta.
**Aplicaciones críticas:** sumergibles y superficiales con cisterna vacía.

| Producto | Detección directa marcha en seco |
|---|---|
| GSC-MB | No directa. Complementar con presostato baja presión en succión. |
| GSC-CR | No directa (aplicación compresor, no bomba de agua). |
| GSPT | Detecta subcarga como precursor. No mide temperatura. |
| **GSPT-MV** | **DETECCIÓN DIRECTA con sensor PT100.** Mide temperatura real del devanado. |
| GIII | También incluye entrada PT100. |

**Recomendación:** para bombas sumergibles, GSPT-MV con PT100 es la única protección Genteca que detecta marcha en seco directamente.

### Ruta: Short cycling de compresor

**Mecanismo:** cada arranque = calor extra. Compresores herméticos: arranque contra presión alta → falla mecánica.

| Producto | Anti-short cycle |
|---|---|
| **GST-RR** | TC mínimo **180s en hardware** — no configurable por debajo. |
| **GSC-CR** | TC mínimo **180s en hardware** — mismo principio por corriente. |
| GUCT+ | TC configurable. Puede ajustarse a 180s pero depende del usuario. |
| GSPT | Función de límite de arranques/hora NEMA MG10 (complementaria). |
| GIII | TC configurable + PT100 para temperatura real. |

**Combinación óptima compresores:** GSC-CR + GST-RR = protección completa con doble garantía de anti-short cycle.

### Ruta: Subtensión Venezuela

**Mecanismo:** tensión baja → par reducido (T∝V²) → corriente mayor → calentamiento. CORPOELEC: 200-210V en sistemas 220V es frecuente.

| Producto | Rango UV |
|---|---|
| GST-RM 220V / GST-RR 220V | 165-200V |
| GSC-MB 220V | 145-285V |
| GII+ L208 | 165-225V |
| GUCT+ 208V | 165-225V |
| GSPT-MV | -20% a -5% del voltaje nominal configurado |

### Ruta: Rotor bloqueado

**Mecanismo:** I = 5-7 × In indefinidamente → destrucción en segundos a minutos.
**Detección estándar:** relé bimetálico 30-90s (insuficiente); electrónico 3s.

| Producto | Función locked rotor |
|---|---|
| GSC-MB / GSC-CR | Clase caliente = 3 → tiempo disparo en caliente = 1/3 del frío. Sin función dedicada con timer configurable. |
| GUCT+ / GIII / GSPT / GSPT-MV | **3 segundos fijos** ante rotor bloqueado. Independiente de la clase térmica configurada. |

### Ruta: Sobrecarga

**Mecanismo:** I > In → calor acumulado → degradación aislamiento (Arrhenius).
**Detección:** curva I²t (clase 10/20/30) define el tiempo de disparo admisible.

| Producto | Característica sobrecarga |
|---|---|
| GSC-MB / GSC-CR | Curva fría clase 10 / curva caliente clase 3. Ajuste por perilla FLA. CT integrado (±2% vs ±10-15% del bimetálico). |
| GUCT+ / GIII | Clase térmica AJUSTABLE 5-30. |
| GSPT / GSPT-MV | Clase 10 fija + curva caliente clase 3. Óptimo para bombas. |
| Todos electrónicos | Memoria térmica real (modelo continúa con motor parado). |

---

## 4. Q&A técnicos

### Q1: ¿Qué producto recomiendo para proteger un compresor de refrigeración de 5 HP a 220V?

**A:** Para compresor trifásico de 5 HP a 220V, la recomendación óptima combina dos productos Exceline Profesional:

1. **GSC-CR22032** (Protector de Sobrecarga Trifásico para Compresores, modelo 220V, 10-32A) — protege contra sobrecarga, rotor trancado, falta de fase, desbalance de corriente y voltaje. Característica crítica: anti-short cycle 180s en hardware.

2. **GST-RR220** (Supervisor Trifásico para Refrigeración) — primera línea de detección de condiciones de red (falta de fase en <0.5s, vs los 3s del GSC-CR). También con anti-short cycle 180s en hardware.

La combinación da doble protección de red + protección de corriente + doble garantía anti-short cycle.

**Alternativa con MODBUS:** si se requiere registro de fallas e integración con SCADA, el **GUCT+208-32** (Genius) cubre ambas funciones en un solo dispositivo con clase térmica ajustable.

### Q2: ¿Cuál es la diferencia entre GSC-MB y GSC-CR?

**A:** Son físicamente casi idénticos y ofrecen las mismas funciones de protección (sobrecarga, rotor trancado, falta de fase, desbalance, sub/sobretensión, fase invertida, apagones).

**La diferencia crítica:** tiempo mínimo de conexión después de falla de voltaje.

| Modelo | Tiempo mínimo |
|---|---|
| GSC-MB | Ajustable de 5 a 600 segundos |
| GSC-CR | Restringido de 180 a 600 segundos — no puede configurarse por debajo de 3 minutos |

Esto convierte al **GSC-CR en el correcto para compresores de refrigeración**, donde reconectar antes de 3 minutos puede causar liquid slugging. **GSC-MB es el correcto para motores de bombas, ventiladores y uso general.**

La selección depende únicamente de la aplicación, no del precio ni del tamaño.

### Q3: ¿Para qué sirve el sensor PT100 en el GSPT-MV y cuándo es necesario?

**A:** El PT100 mide la temperatura real del devanado del motor a través de un sensor instalado en los bobinados. Es necesario cuando el motor puede sobrecalentarse sin que la corriente lo refleje.

**Caso crítico: marcha en seco de bombas sumergibles.** Cuando una bomba sumergible opera sin agua, el motor pierde su refrigerante (el agua). La temperatura del devanado sube rápidamente. La corriente puede bajar (sin carga hidráulica) o mantenerse normal — ningún relé de corriente lo detecta.

El PT100 lo detecta directamente. Cuando se alcanza Tm configurada, el GSPT-MV dispara. La reconexión solo ocurre cuando T baja a un valor calculado.

**Para bombas sumergibles en pozos con nivel variable**, GSPT-MV con PT100 es la protección más efectiva del portafolio.

### Q4: ¿Cuándo usar GUCT+ vs GSPT?

**A:** Depende de la aplicación específica.

**Usar GUCT+ cuando:**
- El motor no es de bomba (compresor de tornillo, ventilador industrial, transportador, máquina con inercia variable)
- Se requiere clase térmica ajustable (arranque largo, Clase 20 o 30)
- Se necesita la función de alta inercia
- Integración con SCADA via MODBUS

**Usar GSPT cuando:**
- La aplicación es bomba (centrífuga, pozo, aguas residuales)
- Tiempo de arranque corto (2-5s — Clase 10 correcta)
- Se requiere control del número de arranques/hora (NEMA MG10)
- Se necesita mayor historial de fallas (80 vs 20)

**Usar GSPT-MV cuando:**
- Bomba sumergible (necesita PT100 para marcha en seco)
- Potencia supera 80A de los GSPT estándar
- Multivoltaje configurable para mismo SKU en mercados con tensiones distintas

### Q5: ¿Qué diferencia al GII+ del GST-RM?

**A:** Ambos son supervisores de voltaje trifásico sin medición de corriente, pero tienen diferencias significativas.

| Característica | GST-RM | GII+ |
|---|---|---|
| Interfaz | Perillas manuales + LEDs | Pantalla LCD |
| Información en tiempo real | LEDs | Voltajes 3 fases, % desbalance, frecuencia |
| Comunicación | — | MODBUS RTU |
| Registro histórico | — | Últimas 20 fallas (tipo, valor, fecha, hora, duración) |
| Programador horario | — | 20 eventos semanales + 20 feriados (modelo opcional) |
| Ajuste TD | 0.5-10s | 1-30s |
| Costo relativo | Más económico | Más alto |

**Elegir GST-RM cuando:** presupuesto limitado, instalación simple sin requisitos de diagnóstico ni comunicación.
**Elegir GII+ cuando:** se necesita diagnóstico de fallas, integración MODBUS, control horario o visualización local.

### Q6: ¿Cuándo GSC-MB vs GUCT+?

**A:** La elección depende del nivel de diagnóstico y control requerido, no del nivel de protección.

**Usar GSC-MB cuando:**
- Instalación simple, presupuesto ajustado
- No se necesita MODBUS ni diagnóstico
- Motor de uso general sin requisitos especiales de clase térmica
- Corriente entre 3.5A y 80A a 220V o entre 10A y 80A a 440V

**Usar GUCT+ cuando:**
- Se requiere clase térmica ajustable (motores con arranque largo, Clase 20 o 30)
- Se necesita subcarga configurable (correa rota, bomba sin caudal por FP o %In)
- Integración SCADA/PLC via MODBUS
- Historial de fallas necesario
- Visualización de corriente, voltaje, FP en LCD

GUCT+ no reemplaza al GSC-MB en coste-efectividad para aplicaciones simples, pero lo supera claramente cuando hace falta diagnóstico y control.

### Q7: ¿Cuántos modelos de protectores trifásicos tiene Genteca?

**A:** Aproximadamente 40 referencias activas trifásicas, organizadas en dos marcas:

**EXCELINE PROFESIONAL:**
- Solo voltaje: GST-RM (2 modelos: 220V, 440V), GST-RR (2 modelos: 220V, 440V)
- Voltaje + corriente: GSC-MB (5 modelos: 220V en 3 rangos + 440V en 2 rangos), GSC-CR (misma estructura para compresores)

**GENIUS:**
- Solo voltaje: GII+ en 3 tensiones (120V, 208/220V, 440/480V), con y sin programador
- Voltaje + corriente: GUCT+ (8 modelos: 4 rangos × 2 tensiones), GIII (hasta 18 modelos: 3 rangos × 3 tensiones × CT externos + horario), GSPT (8 modelos), GSPT-MV (3 modelos: 050/100/180A multivoltaje)

> Productos pendientes de confirmar disponibilidad comercial: GST-RD, GST-RG.

---

**Última actualización:** 2026-05-07. Versión 1.0, integración inicial.
