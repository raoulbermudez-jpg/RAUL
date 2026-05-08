# Motores trifásicos de inducción — Fundamentos

**Audiencia:** Vera, Orlan, Solenne y agentes que necesitan contexto técnico antes de seleccionar productos, comparar competidores o redactar contenido sobre motores y protecciones.
**Origen:** integrado desde Atlas 1 legacy (marzo 2026), curado y actualizado por Vera 2026-05-07.
**Normas de referencia:** IEC 60034-1, IEC 60034-5, NEMA MG1, COVENIN 3028.

> **Caveat operativo:** las tablas de corriente nominal por HP en este documento son aproximaciones útiles para selección preliminar. **Para calibrar protecciones siempre usar el valor de placa del motor (nameplate).**

---

## 1. Conceptos fundamentales

### Motor trifásico de inducción

Máquina eléctrica rotativa que convierte energía eléctrica trifásica en mecánica por inducción electromagnética. Representa más del 70% del consumo eléctrico industrial mundial. Sin conexión eléctrica directa al rotor: extremadamente robusto, bajo mantenimiento.

Partes: estátor (devanados trifásicos en hierro laminado), rotor (jaula de ardilla o bobinado), eje, rodamientos, carcasa, ventilador, caja de bornes.

Principio: el estátor crea un campo magnético giratorio a velocidad sincrónica que induce corrientes en el rotor (efecto transformador). La interacción genera el par motor.

### Velocidad sincrónica

Velocidad a la que gira el campo magnético del estátor.

**Fórmula:** Ns = (120 × f) / P
Donde Ns = velocidad sincrónica (RPM), f = frecuencia (Hz), P = número de polos.

Valores típicos a 60 Hz (Venezuela):

| Polos | Ns (RPM) |
|---|---|
| 2 | 3600 |
| 4 | 1800 |
| 6 | 1200 |
| 8 | 900 |

**Nota Venezuela:** la frecuencia nominal CORPOELEC es 60 Hz según COVENIN. Variaciones reales 59-61 Hz afectan velocidad y par.

### Deslizamiento

Diferencia porcentual entre velocidad sincrónica y velocidad real del rotor bajo carga. Condición fundamental para la inducción.

**Fórmula:** s = (Ns - Nr) / Ns × 100%

Valores típicos:
- En vacío: 0.1% - 0.5%
- A plena carga: 2% - 8% (motores estándar)
- En arranque (rotor parado): 100%

**Implicación protección:** deslizamiento >8-10% en operación indica sobrecarga o problema mecánico.

### Par motor (torque)

Fuerza de giro en el eje. Parámetro central para selección y diseño de protecciones.

| Tipo | Magnitud típica | Relevancia |
|---|---|---|
| Par nominal (Tn) | Referencia operación normal | Base de comparación |
| Par de arranque (Ta) | 1.5 × Tn a 3.0 × Tn | Define si el motor puede arrancar la carga |
| Par máximo (Tmax) | 2.5 × Tn a 3.5 × Tn | Si la carga supera Tmax → stall |
| Par de stall | = Par de arranque | Corriente 5-8 × In, destrucción en segundos sin protección |

**Fórmula potencia-par-velocidad:** P = T × ω = T × (2π × Nr / 60)

### Corriente nominal

Corriente que consume el motor a plena carga, tensión y frecuencia nominales. Parámetro más importante para selección de protecciones.

**Fuente del dato:** placa del motor.
**Aproximación práctica:** In ≈ P / (√3 × V × FP × η)

Ejemplo motor 15 kW, 220V, FP=0.85, η=0.90:
In ≈ 15000 / (1.732 × 220 × 0.85 × 0.90) ≈ 51.5 A

**Regla:** siempre usar el valor de placa. La diferencia entre cálculo y placa indica calidad real del diseño.

### Factor de servicio (FS)

Multiplicador sobre potencia nominal que indica capacidad de operación continua a carga aumentada sin degradación prematura.

| FS | Significado |
|---|---|
| 1.0 | Sin margen — operar solo a Pn |
| 1.15 | 115% de Pn continuo (estándar NEMA) |
| 1.25 | Diseño especial para sobrecarga frecuente |

**Implicación protección:** si FS = 1.15, ajuste hasta 1.15 × In sin riesgo. Algunos relés permiten ingresar FS como parámetro.

### Clase de aislamiento

Temperatura máxima de operación continua del devanado sin degradación acelerada.

| Clase | Tmax | Estándar hoy |
|---|---|---|
| A | 105°C | Antiguo |
| B | 130°C | |
| F | 155°C | **Estándar industrial moderno** |
| H | 180°C | Aplicaciones especiales |

**Práctica común:** muchos fabricantes usan aislamiento Clase F pero declaran límites de Clase B para margen térmico ("rated Class B, insulated Class F").

**Implicación Venezuela:** ambientes industriales 35-55°C consumen significativamente el margen térmico. Un motor Clase F a 50°C ambiente tiene 105°C de margen real vs 115°C de diseño teórico → reducción de capacidad ~9%.

### Grado de protección IP

Código IEC 60034-5 / ISO 20653 para protección contra ingreso de sólidos y líquidos.

**Formato:** IP XY donde X = sólidos (0-6), Y = líquidos (0-9).

Grados comunes en aplicaciones industriales venezolanas:

| IP | Descripción | Uso |
|---|---|---|
| IP21 | Gotas verticales | Interior limpio |
| IP44 | Salpicaduras | Interior o exterior cubierto |
| IP54 | Polvo (limitado) + salpicaduras | Industrial general |
| IP55 | Polvo (completo) + chorros de agua | Exterior |
| IP65 | A prueba de polvo + chorros directos | Ambientes severos |
| IP68 | Sumergible permanente | Bombas sumergibles |

**Implicación protección:** IP68 (motor sumergible) disipa calor solo por el fluido bombeado. Operación en seco → sobrecalentamiento muy rápido.

### Régimen de servicio (IEC 60034-1)

| Régimen | Descripción | Aplicaciones |
|---|---|---|
| S1 | Continuo | Bombas centrífugas, compresores, ventiladores |
| S2 | Corta duración | Poco común industrial continuo |
| S3 | Intermitente periódico | Transportadores ciclados, prensas, grúas |
| S4 | S3 + arranque | Muchos arranques por hora |
| S5 | S3 + freno eléctrico | Elevadores |

**Implicación:** regímenes S3, S4, S5 generan ciclos térmicos complejos. La protección debe tener memoria térmica.

---

## 2. Tensiones nominales en Venezuela

### Sistema CORPOELEC industrial

**Baja tensión (BT):**
- 208V 3Ø 60Hz (industrial, distribución secundaria — menos común)
- 220V 3Ø 60Hz (BT más común — motores hasta ~75 kW)
- 230V 3Ø 60Hz (sistemas más recientes)
- 440V 3Ø 60Hz (BT elevada — plantas industriales, compresores, bombas grandes)
- 460V/480V 3Ø 60Hz (NEMA, equipos importados de EE.UU.)

**Media tensión (MT):**
- 2400V, 4160V, 13800V 3Ø 60Hz (industria pesada y distribución primaria)

### Calidad de suministro real

> **Caveat:** datos cualitativos basados en observación de campo y reportes de mantenimiento industrial venezolano. No hay registros oficiales de CORPOELEC accesibles que permitan cuantificación estadística rigurosa.

| Parámetro | Norma IEC | Norma NEMA | Realidad Venezuela |
|---|---|---|---|
| Variación de tensión | ±5% | ±10% | ±10-20% (subtensión crónica común: 200-210V en sistemas 220V) |
| Variación de frecuencia | ±1% | ±5% | ±1-2 Hz |
| Desequilibrio de fases | <1% | <1% | 3-8% frecuente |

**Consecuencia:** muchos motores en Venezuela operan fuera de los rangos de tolerancia de norma. Causa principal de falla prematura.

---

## 3. Tablas de referencia rápida — corriente nominal por potencia

### Motor 220V 3Ø 60Hz

**Asunciones:** FP ≈ 0.85, η ≈ 0.88-0.92 (valores típicos industriales).

| HP | kW | In aprox (A) | Icc arranque (A, 5-7×) |
|---|---|---|---|
| 1 | 0.75 | 3.2 | 16-22 |
| 2 | 1.5 | 6.0 | 30-42 |
| 3 | 2.2 | 8.5 | 43-60 |
| 5 | 3.7 | 14.0 | 70-98 |
| 7.5 | 5.5 | 20.5 | 103-144 |
| 10 | 7.5 | 27.0 | 135-189 |
| 15 | 11.0 | 39.5 | 198-277 |
| 20 | 15.0 | 52.0 | 260-364 |
| 25 | 18.5 | 64.0 | 320-448 |
| 30 | 22.0 | 76.0 | 380-532 |
| 40 | 30.0 | 101 | 505-707 |
| 50 | 37.0 | 124 | 620-868 |
| 60 | 45.0 | 149 | 745-1043 |
| 75 | 55.0 | 181 | 905-1267 |
| 100 | 75.0 | 242 | 1210-1694 |

### Motor 440V 3Ø 60Hz

| HP | kW | In aprox (A) |
|---|---|---|
| 5 | 3.7 | 7.0 |
| 10 | 7.5 | 13.5 |
| 20 | 15.0 | 26.0 |
| 30 | 22.0 | 38.0 |
| 50 | 37.0 | 62.0 |
| 75 | 55.0 | 90.5 |
| 100 | 75.0 | 121 |
| 150 | 110.0 | 177 |
| 200 | 150.0 | 235 |

> **Recordatorio crítico:** estos valores son aproximaciones. Para calibrar una protección, **siempre** usar el valor In de la placa del motor.

---

## 4. Mecanismos de falla

### Sobrecarga térmica

Causa más frecuente de falla. Operación a I > In durante tiempo suficiente para superar el límite térmico del aislamiento.

Causas: carga mecánica excesiva, tensión baja (más corriente para mantener el par), frecuencia baja, temperatura ambiente elevada, ventilación insuficiente, altitud alta.

**Regla de Arrhenius:** por cada 10°C sobre el límite de la clase de aislamiento, la vida útil del aislamiento se reduce a la mitad.

Ejemplo Clase F (límite 155°C):
- 165°C → vida 50% nominal
- 175°C → vida 25%
- 185°C → vida 12.5%

**Característica térmica:** I² × t = constante. Define la curva de disparo del relé térmico.

### Desequilibrio de fases

Tensiones o corrientes desiguales entre fases. Muy común en sistema venezolano y especialmente destructivo.

**Daño:** desequilibrio de tensión X% produce desequilibrio de corriente 6X-10X%.

**Fórmula NEMA:** %D = (Vmax_desv / Vprom) × 100%

Efecto térmico (NEMA MG1 Table 10-1):

| Desequilibrio V (%) | Incremento temperatura |
|---|---|
| 1 | ~0% |
| 2 | ~5% |
| 3 | ~25% |
| 5 | ~50% |

**Protección requerida:** monitor de red o relé con detección de desequilibrio (umbral 2-3%).

### Pérdida de fase

Una fase se interrumpe mientras el motor opera (single phasing). Condición de desequilibrio máximo.

Causas: fusible quemado, contactor con contacto dañado, conexión floja, cortes selectivos CORPOELEC.

Comportamiento:
- Si parado: NO arranca, zumbido, corriente 3-5 × In en fases restantes, daño en minutos.
- Si operando: continúa por inercia, corriente 200-300% × In, motor pequeño (<5 kW) destruido en 30-60 segundos sin protección.

**Indicador eléctrico:** I=0 en una fase, I ≥ 1.5-2.0 × In en las otras dos.
**Protección:** relé de falta de fase (voltimétrico o amperimétrico) o relé de desequilibrio.

### Inversión de fase

Orden de secuencia invertido (RST→RTS). El motor gira en dirección opuesta.

Consecuencias por aplicación:
- Bomba centrífuga: caudal cero, riesgo cavitación
- Bomba sumergible: puede desenroscar impulsor (rosca de retención) → falla mecánica grave
- Compresor: válvulas en sentido incorrecto → daño mecánico
- Transportador: invierte dirección → accidente o daño de producto

**Protección:** relé de secuencia de fases. Bajo costo, previene daños catastróficos por error humano.

### Subtensión / sobretensión

Tensión fuera de límites operacionales.

**Subtensión:** par ∝ V², a V=90% Vn → Tmax = 81% Tmax_nominal. Para mantener par necesario, motor toma más corriente → sobrecalentamiento. Subtensión grave puede llevar al motor a stall.

**Sobretensión:** mayor flujo magnético → saturación del núcleo → pérdidas en hierro adicionales. Aislamiento sometido a mayor estrés dieléctrico. Superar 115-120% Vn daña aislamiento a largo plazo.

**Protección:** relé de mínima/máxima tensión o monitor de red.

### Rotor bloqueado / stall

Rotor deja de girar mientras motor sigue energizado. Corriente = corriente de arranque (5-7 × In) indefinidamente. Calor: P_calor = I² × R; con I = 6 × In → 36 × P_calor_nominal. Devanado alcanza temperatura destructiva muy rápido.

**Protección:** relé electrónico con función "locked rotor" (1-4 segundos). El relé bimetálico clásico puede tardar 30-90 segundos, demasiado para motores pequeños.

### Sobretemperatura ambiente

Temperatura ambiente >40°C reduce vida útil del aislamiento.

**Derating típico:** por cada 1°C sobre 40°C → reducir capacidad ~1%.

A 50°C ambiente: motor al 90% de Pn.
A 55°C ambiente: motor al 85% de Pn.

**Protección ideal:** sensor de temperatura en devanado (PTC o RTD).

### Arranque frecuente

Más arranques por hora de los especificados. Cada arranque genera calor adicional en el rotor.

| Tamaño | Arranques/hora máx (S1) |
|---|---|
| <5 kW | 10-15 |
| 5-30 kW | 4-6 |
| >30 kW | 1-3 |

**Protección:** relé electrónico con memoria térmica + contador de arranques (función anti-jogging).

### Cortocircuito interno

Falla dieléctrica del aislamiento entre espiras o entre fases dentro del bobinado.

Causas: degradación térmica acumulada, humedad, contaminación química, sobre-tensiones transitorias, envejecimiento natural.

**Protección:** relé diferencial de motor (más eficaz para fallas internas). Sin diferencial: fusible + relé térmico cubre cortocircuitos fase-fase graves pero puede no detectar cortocircuitos entre espiras.

---

## 5. Diseños NEMA y curvas característica

| Diseño | Par arranque | Par máx | Icc arranque | Deslizamiento | Aplicaciones |
|---|---|---|---|---|---|
| A | 1.5-2.0 × Tn | 2.5-3.0 × Tn | 5-7 × In | 2-5% | Par constante, arranques infrecuentes |
| **B** (más común) | 1.5-2.0 × Tn | 2.0-2.5 × Tn | 4-5.5 × In | 2-5% | Uso general — bombas, compresores, ventiladores |
| C | 2.0-2.5 × Tn | 2.0 × Tn | 4-5 × In | 2-5% | Compresores pistón, bombas desplazamiento positivo, trituradoras |
| D | 2.5-3.0 × Tn | = arranque | 3-4.5 × In | 5-13% | Punzones, prensas, elevadores |

---

## 6. Categorías de utilización IEC 60947-4-1

| Categoría | Aplicación |
|---|---|
| AC-2 | Motores anillo rozante (rotor bobinado). Menos común hoy. |
| **AC-3** (estándar) | Jaula ardilla. Arranque directo + parada en plena velocidad. Bombas, compresores, ventiladores. |
| AC-4 | Jaula ardilla. Arranque + frenado por contracorriente + jogging. Transportadores con frenado, prensas. Requiere contactor de mayor capacidad. |

---

## 7. Tipos de arranque y efecto en protección

### Arranque directo (DOL)

| Parámetro | Valor |
|---|---|
| Icc arranque | 5-7 × In |
| Tiempo aceleración | 2-10 segundos típico |
| Golpe de tensión en red | Alto |
| Aplicación | Motores hasta 15-22 kW en redes con buena capacidad |

**Crítico:** la protección debe tolerar 5-7 × In durante el tiempo de arranque sin disparar. Curva de arranque correctamente configurada es lo que determina si funciona.

### Arranque estrella-triángulo (Y-Δ)

- Icc arranque en Y: 1.5-2.5 × In (1/3 del DOL)
- Tiempo aceleración: mayor que DOL (dos etapas)
- Transitorio de conmutación Y→Δ: pico de corriente al cambiar (puede ser > DOL)
- Aplicación: motores 15-75 kW, baja inercia
- **Error frecuente:** calibrar el relé térmico para In de línea cuando va en los devanados (triángulo) — debe ser **In/√3 = 0.577 × In**.

### Arrancador suave (soft starter)

- Icc arranque: 2-4 × In (controlada por SCR)
- Aplicación: bombas con golpe de ariete, transportadores con carga frágil, compresores sensibles
- **No reemplaza** el relé de sobrecarga ni los fusibles de cortocircuito

### Variador de frecuencia (VFD)

- Icc arranque: 100-150% In (arranque suave inherente)
- Control de velocidad continuo
- Aplicación: cargas con par cuadrático (bombas, ventiladores) — gran ahorro energético
- **Cuidado:** modifica la forma de onda; cables largos pueden requerir motores INVERTER-DUTY y protección diferencial

---

## 8. Hallazgos clave

> Estos hallazgos son síntesis técnica del Atlas legacy validada por Vera. Los datos cualitativos sobre Venezuela (CORPOELEC, temperaturas) no tienen fuente estadística publicable; se basan en observación de campo y reportes de mantenimiento industrial.

- **Pérdida de fase es la condición de falla más frecuente y destructiva** en motores venezolanos. Costo marginal de protección ≪ costo de rebobinado.
- **El ajuste de la curva de arranque** (tiempo de arranque en relé térmico/electrónico) es la causa más común de disparos intempestivos. Ajuste = tiempo real de aceleración + 20-30% margen.
- **Regla de Arrhenius (10°C):** la protección térmica correcta no solo evita la falla catastrófica — protege la vida útil total del motor.
- **Corriente no es temperatura.** Los relés bimetálicos modelan T a través de I asumiendo relación directa. Pero T real depende de ambiente, velocidad, refrigerante, ciclo de carga. Relés electrónicos con modelos térmicos avanzados son superiores. Para motores críticos de proceso, relé con RTD/PTC externo es la solución más precisa.
- **Stall en arranque > stall en operación.** El arranque es justo cuando hay más corriente y menos refrigeración. Bimetálico 30-90s; electrónico con "locked rotor" 1-4s.
- **Tablas de corriente típica vs placa real.** Las tablas son aproximaciones — siempre la placa.

---

**Última actualización:** 2026-05-07. Versión 1.0, integración inicial.
