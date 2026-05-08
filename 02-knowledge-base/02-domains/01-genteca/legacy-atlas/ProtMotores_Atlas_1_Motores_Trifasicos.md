# ATLAS 1 — MOTORES TRIFÁSICOS DE INDUCCIÓN

**Base de Conocimiento:** Protecciones Eléctricas para Motores Trifásicos
**Proyecto:** ProtMotores | Carril 2 — Técnico/Industrial
**Mercado:** Venezuela | Normas: COVENIN + IEC 60947 + NEMA MG1
**Versión:** 1.0 | Marzo 2026
**Prefijos RAG:** INGLÉS | Contenido: ESPAÑOL

---

## SECCIÓN 1 — CONCEPTOS FUNDAMENTALES

### CONCEPT: Motor_Trifasico_Induccion
Definición: Máquina eléctrica rotativa que convierte energía eléctrica trifásica en energía mecánica por el principio de inducción electromagnética. Es la máquina más utilizada en la industria mundial: representa más del 70% del consumo eléctrico industrial. Opera sin conexión eléctrica directa al rotor (a diferencia del motor de CC o el motor síncrono), lo que lo hace extremadamente robusto y de bajo mantenimiento.
Partes principales: Estátor (devanados trifásicos en hierro laminado) | Rotor (jaula de ardilla o bobinado) | Eje | Rodamientos | Carcasa | Ventilador | Caja de bornes.
Principio: El estátor crea un campo magnético giratorio a velocidad sincrónica. Este campo induce corrientes en el rotor (efecto transformador). La interacción entre campo estátor y corrientes rotor genera el par motor (torque).

### CONCEPT: Velocidad_Sincronica
Definición: Velocidad a la que gira el campo magnético del estátor.
Fórmula: Ns = (120 × f) / P
Donde: Ns = velocidad sincrónica (RPM) | f = frecuencia de red (Hz) | P = número de polos del motor.
Valores típicos Venezuela (f=60Hz):
- 2 polos → Ns = 3600 RPM
- 4 polos → Ns = 1800 RPM
- 6 polos → Ns = 1200 RPM
- 8 polos → Ns = 900 RPM
Nota Venezuela: La frecuencia nominal es 60 Hz según COVENIN. Variaciones de frecuencia (59-61 Hz típico CORPOELEC) afectan la velocidad sincrónica y el par.

### CONCEPT: Deslizamiento
Definición: Diferencia porcentual entre velocidad sincrónica y velocidad real del rotor bajo carga. Es la condición fundamental para que exista inducción y, por tanto, par motor.
Fórmula: s = (Ns - Nr) / Ns × 100%
Donde: s = deslizamiento (%) | Ns = velocidad sincrónica | Nr = velocidad real.
Valores típicos:
- En vacío (sin carga): s ≈ 0.1% - 0.5%
- A plena carga: s = 2% - 8% (motores estándar)
- En arranque (rotor parado): s = 100%
Implicación para protección: El deslizamiento excesivo en operación (>8-10%) indica sobrecarga o problema mecánico. La protección debe detectar esta condición antes de que el calentamiento sea destructivo.

### CONCEPT: Par_Motor_Torque
Definición: Fuerza de giro que produce el motor en el eje. Es el parámetro mecánico central en la selección de motores y en el diseño de protecciones.
Unidad: N·m (Newton-metro) o lb·ft según norma.
Tipos de par relevantes para protección:
- Par_nominal (Tn): par a plena carga — referencia base de operación normal.
- Par_de_arranque (Ta): par al inicio del arranque (Nr=0, s=100%). Típico: 1.5 × Tn a 3.0 × Tn según diseño del rotor.
- Par_máximo (Tmax): par pico de la curva torque-velocidad. Típico: 2.5 × Tn a 3.5 × Tn. Si la carga exige más de Tmax, el motor se para (stall).
- Par_de_stall (bloqueo): par con rotor bloqueado = par de arranque. La corriente de bloqueo puede ser 5-8 × In. Si se mantiene, destruye el motor en segundos.
Fórmula potencia-par-velocidad: P = T × ω = T × (2π × Nr/60)
Donde: P = potencia (W) | T = par (N·m) | Nr = velocidad (RPM).

### CONCEPT: Corriente_Nominal
Definición: Corriente que consume el motor a plena carga, tensión y frecuencia nominales. Es el parámetro más importante para la selección de protecciones.
Símbolo: In o Ie (corriente asignada según IEC 60947-4-1).
Fuente del dato: Placa de características del motor (nameplate).
Aproximación práctica (Venezuela, 3Ø, 60Hz, tensión nominal):
P(kW) ≈ √3 × V(kV) × In(A) × FP × η
Despejando In ≈ P / (√3 × V × FP × η)
Ejemplo: Motor 15 kW, 220V, FP=0.85, η=0.90:
In ≈ 15000 / (1.732 × 220 × 0.85 × 0.90) = 51.5 A
Nota: Este cálculo es aproximación. Siempre usar el valor de placa. La diferencia entre el valor calculado y el de placa indica la calidad real del diseño del motor.

### CONCEPT: Factor_de_Servicio
Definición: Multiplicador aplicado a la potencia nominal que indica la capacidad del motor para operar de forma continua a carga aumentada sin degradación prematura.
Símbolo: FS o SF (Service Factor).
Valores típicos:
- FS = 1.0: Sin margen adicional — operar solo a potencia nominal.
- FS = 1.15: Puede operar al 115% de Pn de forma continua (estándar NEMA).
- FS = 1.25: Motores de diseño especial para sobrecarga frecuente.
Implicación para protección: Si FS = 1.15, la protección puede ajustarse hasta 1.15 × In sin que el motor esté en riesgo. Algunos relés permiten ingresar el FS como parámetro de ajuste.

### CONCEPT: Clase_de_Aislamiento
Definición: Clasificación del sistema de aislamiento del devanado del estátor según temperatura máxima de operación continua sin degradación acelerada.
Norma de referencia: IEC 60085 / NEMA MG1.
Clases y temperaturas máximas:
- Clase A: 105°C (temperatura ambiente 40°C + elevación 65°C)
- Clase B: 130°C (temperatura ambiente 40°C + elevación 90°C)
- Clase F: 155°C (temperatura ambiente 40°C + elevación 115°C) — ESTÁNDAR HOY
- Clase H: 180°C (temperatura ambiente 40°C + elevación 140°C)
Nota práctica: La mayoría de los motores industriales modernos son Clase F. Muchos fabricantes usan aislamiento Clase F pero declaran límites de Clase B para dar margen térmico adicional. Esto se llama "rated Class B, insulated Class F".
Implicación Venezuela: Las temperaturas ambientes venezolanas (28-45°C en zonas industriales) recortan significativamente el margen de elevación permisible. Un motor Clase F en ambiente de 45°C tiene margen real de 155-45=110°C elevación vs 115°C teórico → apenas 5°C de margen. Esto hace crítica la protección térmica.

### CONCEPT: Grado_de_Proteccion_IP
Definición: Código que indica el nivel de protección de la carcasa del motor contra ingreso de sólidos y líquidos.
Norma: IEC 60034-5 / ISO 20653.
Formato: IP XY donde X = protección sólidos (0-6) | Y = protección líquidos (0-9).
Grados más comunes en aplicaciones industriales Venezuela:
- IP21: Protegido vs gotas verticales. Uso interior limpio.
- IP44: Protegido vs salpicaduras. Uso interior o exterior cubierto.
- IP54: Protegido vs polvo (limitado) y salpicaduras. Uso industrial general.
- IP55: Protegido vs polvo (completo) y chorros de agua. Uso exterior.
- IP65: A prueba de polvo y chorros directos. Ambientes severos.
- IP68: Sumergible a presión especificada. Motores de bombas sumergibles.
Implicación para protección: El grado IP afecta la disipación térmica. Un motor IP68 (totalmente encapsulado) disipa calor solo por el fluido que bombea. Si la bomba opera en seco (sin agua), la temperatura sube muy rápidamente. La protección contra marcha en seco es crítica en bombas sumergibles venezolanas.

### CONCEPT: Regimen_de_Servicio
Definición: Clasificación de la secuencia de cargas, arranques y paradas a la que se somete el motor durante su operación.
Norma: IEC 60034-1.
Regímenes más relevantes para protección:
- S1 (Continuo): Carga constante por tiempo suficiente para alcanzar equilibrio térmico. Bombas centrífugas, compresores, ventiladores.
- S2 (Corta duración): Carga a potencia nominal por tiempo definido, luego parada hasta enfriamiento. Poco común en aplicaciones industriales continuas.
- S3 (Intermitente periódico): Ciclos de carga y parada. La temperatura nunca llega a equilibrio. Factor de marcha (DC%) = t_trabajo / t_ciclo × 100%. Transportadores con ciclos de carga, prensas, grúas.
- S4 (Intermitente periódico con arranque): Incluye el calor generado por el arranque. Relevante cuando hay muchos arranques por hora.
- S5 (Intermitente periódico con freno eléctrico): Incluye frenado. Elevadores.
Implicación para protección: Los regímenes S3, S4, S5 generan ciclos térmicos complejos. El relé de protección debe tener memoria térmica para acumular el calor de arranques sucesivos. Los relés electrónicos avanzados modelan esto con precisión.

---

## SECCIÓN 2 — PARÁMETROS NOMINALES Y DATOS DE PLACA

### SPECIFICATION: Placa_de_Caracteristicas_Motor
Datos obligatorios según IEC 60034-1 y NEMA MG1:

| Parámetro            | Símbolo  | Unidad   | Descripción                         |
|----------------------|----------|----------|-------------------------------------|
| Potencia nominal     | Pn / HP  | kW / HP  | Potencia mecánica en el eje a Tn    |
| Tensión nominal      | Vn       | V        | Tensión de línea a línea            |
| Corriente nominal    | In       | A        | Corriente de línea a plena carga    |
| Frecuencia           | f        | Hz       | 60 Hz Venezuela                     |
| Velocidad nominal    | Nr       | RPM      | Velocidad a plena carga             |
| Factor de potencia   | FP / cosφ| —        | A plena carga                       |
| Rendimiento          | η        | %        | A plena carga                       |
| Clase de aislamiento | —        | A/B/F/H  | Temperatura máx. devanado           |
| Grado de protección  | IP       | —        | IP44, IP54, IP55, IP68              |
| Régimen de servicio  | S        | —        | S1, S3, S4…                         |
| Factor de servicio   | FS / SF  | —        | 1.0 / 1.15 / 1.25                   |
| Conexión             | —        | —        | Estrella (Y) / Delta (Δ)            |
| Temperatura ambiente | Ta       | °C       | Máxima del entorno de instalación   |
| Peso                 | —        | kg       | Peso del motor                      |
| Tipo de rotor        | —        | —        | Jaula ardilla / Bobinado            |

### SPECIFICATION: Tensiones_Nominales_Venezuela
Sistema eléctrico venezolano CORPOELEC (industrial):
Baja tensión (BT):
- 208V 3Ø 60Hz (industrial, distribución secundaria — menos común)
- 220V 3Ø 60Hz (tensión BT más común Venezuela — motores hasta ~75 kW)
- 230V 3Ø 60Hz (algunos sistemas más recientes)
- 440V 3Ø 60Hz (BT elevada — plantas industriales, compresores, bombas grandes)
- 460V 3Ø 60Hz (NEMA, equipos importados de EE.UU.)
- 480V 3Ø 60Hz (NEMA, equipos importados de EE.UU.)
Media tensión (MT):
- 2400V 3Ø 60Hz (sistemas industriales propios, menos frecuente)
- 4160V 3Ø 60Hz (industria pesada, motores >200 kW)
- 13800V 3Ø 60Hz (distribución primaria, no motores industriales normales)
Nota crítica: La inestabilidad del sistema CORPOELEC produce variaciones frecuentes de ±10% a ±15% sobre la tensión nominal. Muchos motores operan en Venezuela fuera de los rangos de tolerancia IEC (±5%) y NEMA (±10%). Esta es una causa principal de falla prematura que la protección debe contemplar.

### SPECIFICATION: Corrientes_Tipicas_Por_Potencia_220V_3f_60Hz
Motor 220V 3Ø 60Hz, FP≈0.85, η≈0.88-0.92 (valores típicos industriales):

| Potencia (HP) | Potencia (kW) | In aprox (A) | Icc_arranque aprox (A) |
|---------------|---------------|--------------|------------------------|
| 1 HP          | 0.75 kW       | 3.2 A        | 16-22 A (5-7 × In)     |
| 2 HP          | 1.5 kW        | 6.0 A        | 30-42 A                |
| 3 HP          | 2.2 kW        | 8.5 A        | 43-60 A                |
| 5 HP          | 3.7 kW        | 14.0 A       | 70-98 A                |
| 7.5 HP        | 5.5 kW        | 20.5 A       | 103-144 A              |
| 10 HP         | 7.5 kW        | 27.0 A       | 135-189 A              |
| 15 HP         | 11.0 kW       | 39.5 A       | 198-277 A              |
| 20 HP         | 15.0 kW       | 52.0 A       | 260-364 A              |
| 25 HP         | 18.5 kW       | 64.0 A       | 320-448 A              |
| 30 HP         | 22.0 kW       | 76.0 A       | 380-532 A              |
| 40 HP         | 30.0 kW       | 101 A        | 505-707 A              |
| 50 HP         | 37.0 kW       | 124 A        | 620-868 A              |
| 60 HP         | 45.0 kW       | 149 A        | 745-1043 A             |
| 75 HP         | 55.0 kW       | 181 A        | 905-1267 A             |
| 100 HP        | 75.0 kW       | 242 A        | 1210-1694 A            |

Nota: Icc_arranque = 5 a 7 × In (arranque directo). La protección debe tolerar esta corriente durante el tiempo de arranque sin disparar (curva de arranque).

### SPECIFICATION: Corrientes_Tipicas_Por_Potencia_440V_3f_60Hz
Motor 440V 3Ø 60Hz (misma potencia, corriente aprox. mitad de 220V):

| Potencia (HP) | Potencia (kW) | In aprox (A) |
|---------------|---------------|--------------|
| 5 HP          | 3.7 kW        | 7.0 A        |
| 10 HP         | 7.5 kW        | 13.5 A       |
| 20 HP         | 15.0 kW       | 26.0 A       |
| 30 HP         | 22.0 kW       | 38.0 A       |
| 50 HP         | 37.0 kW       | 62.0 A       |
| 75 HP         | 55.0 kW       | 90.5 A       |
| 100 HP        | 75.0 kW       | 121 A        |
| 150 HP        | 110.0 kW      | 177 A        |
| 200 HP        | 150.0 kW      | 235 A        |

---

## SECCIÓN 3 — MECANISMOS DE FALLA DEL MOTOR

### MECHANISM: Sobrecarga_Termica
Descripción: La sobrecarga es la causa más frecuente de falla en motores trifásicos. Ocurre cuando el motor opera a corriente superior a In durante tiempo suficiente para elevar la temperatura del devanado más allá del límite de su clase de aislamiento.
Causas principales:
- Carga mecánica excesiva (bomba con cabeza mayor a la diseñada, compresor con presión de descarga elevada, correa de ventilador mal tensada)
- Tensión de alimentación baja (a menor tensión, mayor corriente para mantener el par)
- Frecuencia de red baja (afecta velocidad y par)
- Temperatura ambiente elevada (reduce la disipación)
- Ventilación insuficiente (filtros obstruidos, carcasa sucia)
- Operación a altitud elevada (menos densidad de aire, menos enfriamiento)
Efecto en aislamiento — regla de Arrhenius:
Por cada 10°C de incremento sobre la temperatura límite de la clase de aislamiento, la vida útil del aislamiento se REDUCE A LA MITAD.
Ejemplo: Motor Clase F (límite 155°C) operando a 165°C → vida útil = 50% de la nominal. A 175°C → vida útil = 25%. A 185°C → vida útil = 12.5%.
Característica térmica: I² × t = constante (para el mismo calor disipado). Esto define la curva de disparo del relé térmico: a mayor corriente, menor tiempo de disparo admisible.
Indicador eléctrico: I > In (corriente supera la nominal). El nivel de sobrecarga se expresa como: % sobrecarga = (I - In) / In × 100%.

### MECHANISM: Desequilibrio_de_Fases
Descripción: Las tres fases de alimentación presentan tensiones o corrientes diferentes entre sí. Es una condición muy común en el sistema venezolano y especialmente destructiva para motores trifásicos.
Causa del daño: Un desequilibrio de tensión del X% produce un desequilibrio de corriente de 6X a 10X%. Es decir, un desequilibrio de tensión del 2% puede generar hasta 20% de desequilibrio de corriente, provocando sobrecalentamiento severo en la fase más cargada.
Fórmula NEMA desequilibrio de tensión:
%D = (Vmax_desv / Vprom) × 100%
Donde Vmax_desv = máxima desviación de cualquier fase respecto al promedio.
Límites de operación:
- NEMA MG1: máximo 1% de desequilibrio para operación continua sin derating.
- IEC: similar restricción.
- Venezuela real: desequilibrios de 3-8% son comunes en sistemas CORPOELEC.
Efecto térmico del desequilibrio (NEMA MG1 Table 10-1):
- 1% desequilibrio → incremento temperatura ~0%
- 2% desequilibrio → incremento temperatura ~5%
- 3% desequilibrio → incremento temperatura ~25%
- 5% desequilibrio → incremento temperatura ~50%
Consecuencias: El devanado de la fase más cargada se degrada aceleradamente. En casos severos, el motor falla en horas o días (no meses o años).
Protección requerida: Relé de desequilibrio de fases o monitor de red que detecte desequilibrio > 2-3% y dispare o alarme.

### MECHANISM: Perdida_de_Fase
Descripción: Una de las tres fases de alimentación se interrumpe mientras el motor sigue funcionando (condición monofásica — "single phasing"). Es la condición de desequilibrio máximo y la más destructiva.
Causas:
- Fusible quemado en una fase
- Contactor con un contacto dañado o soldado
- Conexión floja en bornes o empalmes
- Protección unipolar mal ajustada que abre solo una fase
- Cortes selectivos de CORPOELEC
Comportamiento del motor:
- Si está parado: El motor NO arranca. Se escucha zumbido. La corriente en las dos fases restantes es muy alta (3-5 × In). Sin protección, el motor se daña en minutos.
- Si estaba operando: Continúa girando (inercia). Las dos fases restantes asumen toda la carga. La corriente sube al 200-300% de In. En motores pequeños (<5 kW) el daño puede ocurrir en 30-60 segundos sin protección. En motores grandes, algo más de tiempo pero siempre destructivo.
Indicador eléctrico:
Corriente = 0 en una fase | Corriente ≥ 1.5-2.0 × In en las otras dos fases. Desequilibrio de tensión severo si la pérdida es en el tablero.
Protección: Relé de falta de fase (voltimétrico o amperimétrico) o relé de desequilibrio con umbral de detección ≥50% desequilibrio.

### MECHANISM: Inversion_de_Fase
Descripción: El orden de secuencia de las tres fases se invierte (RST → RTS o equivalente). El campo magnético giratorio del estátor cambia de sentido → el motor gira en dirección opuesta a la diseñada.
Causas:
- Reconexión incorrecta después de mantenimiento
- Cambio de acometida o interruptor con fases invertidas
- Empalmes incorrectos en instalación
Consecuencias según aplicación:
- Bomba centrífuga: Gira al revés → caudal cero o muy reducido → no succiona. Riesgo de cavitación. No destruye el motor inmediatamente pero sí la bomba.
- Bomba sumergible: Gira al revés → puede desenroscar el impulsor del eje (si tiene rosca izquierda de retención) → falla mecánica grave.
- Compresor: Gira al revés → valvas en sentido incorrecto → daño mecánico grave.
- Transportador: Invierte la dirección → accidente o daño de producto/equipo.
- Ventilador: Reduce drásticamente el caudal de aire. No destruye el ventilador pero falla en su función (sobrecalentamiento del sistema refrigerado).
Protección: Relé de secuencia de fases (voltimétrico). Es una protección de bajo costo que previene daños catastróficos por error humano.

### MECHANISM: Subtension_Sobretension
Descripción: La tensión de alimentación cae por debajo o sube por encima de los límites de operación normal del motor.
Límites normativos:
- IEC 60034-1: ±5% de la tensión nominal.
- NEMA MG1: ±10% de la tensión nominal.
- Venezuela real: variaciones de ±15% a ±20% en muchas zonas son comunes.
Efectos de la SUBTENSIÓN (tensión baja):
- El par es proporcional al cuadrado de la tensión: T ∝ V². Ejemplo: V = 90% Vn → T_max = 81% de T_max_nominal.
- Para mantener el par necesario, el motor toma más corriente → sobrecalentamiento.
- En motores de bombas: si la tensión es muy baja, el motor no puede arrancar (par de arranque insuficiente vs par de carga).
- Subtensión grave: puede llevar al motor a la zona de stall (par < par de carga).
Efectos de la SOBRETENSIÓN (tensión alta):
- Mayor flujo magnético → mayor corriente magnetizante → saturación del núcleo.
- Incremento de pérdidas en el hierro → calentamiento adicional.
- Aislamiento sometido a mayor estrés dieléctrico → reducción de vida útil.
- En general, la sobretensión es menos destructiva que la subtensión, pero superar 115-120% Vn puede dañar el aislamiento a largo plazo.
Protección: Relé de mínima/máxima tensión o monitor de red con umbrales ajustables.

### MECHANISM: Rotor_Bloqueado_Stall
Descripción: El rotor deja de girar mientras el motor sigue energizado. Puede ocurrir en arranque (si el par de arranque es insuficiente) o durante operación (si la carga mecánica supera el par máximo del motor).
Causas:
- Cuerpo extraño atascado en la bomba o compresor
- Rodamiento destruido (rotor toca estátor)
- Carga mecánica repentina muy elevada (golpe de ariete, bloqueo de válvula)
- Tensión de red muy baja en el arranque (par de arranque insuficiente)
Corriente en stall: Es igual a la corriente de arranque = 5-7 × In. Esta corriente fluye indefinidamente si no hay protección → el motor se destruye en segundos (pequeños) a minutos (grandes).
Calor generado: P_calor = I² × R. Con I = 6 × In → P_calor = 36 × P_calor_nominal. El devanado alcanza temperatura destructiva muy rápidamente.
Protección: El relé térmico clásico protege el stall en motores pequeños, pero el tiempo de disparo puede ser demasiado largo para motores grandes. Los relés electrónicos tienen función específica "locked rotor" o "stall protection" con tiempo de disparo muy corto (1-4 segundos).

### MECHANISM: Sobretemperatura_Ambiente
Descripción: La temperatura del ambiente donde opera el motor supera los 40°C de referencia para los que fue diseñado, reduciendo la vida útil del aislamiento.
Condiciones Venezuela:
- Plantas industriales en interiores sin A/C: 35-45°C todo el año.
- Exteriores zona costera/llanos: 38-48°C en época de calor.
- Equipos de bombeo bajo techo metálico: 45-55°C en horas pico.
- Cuartos eléctricos mal ventilados: 40-50°C.
Derating por temperatura: Los fabricantes especifican el factor de reducción de potencia para temperaturas superiores a 40°C.
Ejemplo típico: Por cada 1°C sobre 40°C → reducir capacidad en ~1%. A 50°C ambiente: Motor debe operarse al 90% de su potencia nominal. A 55°C ambiente: Motor debe operarse al 85% de su potencia nominal.
Protección ideal: Sensor de temperatura en el devanado (termistor PTC o RTD) conectado a relé de temperatura. Segunda línea de defensa vs. relé térmico de corriente (que no mide temperatura directamente).

### MECHANISM: Arranque_Frecuente
Descripción: El motor realiza más arranques por hora de los especificados en su diseño. Cada arranque genera calor adicional en el rotor por las corrientes de arranque elevadas (5-7 × In durante 2-15 segundos según motor y carga).
Límites típicos:
- Motores pequeños (< 5 kW): Hasta 10-15 arranques/hora en S1.
- Motores medianos (5-30 kW): Hasta 4-6 arranques/hora.
- Motores grandes (> 30 kW): 1-3 arranques/hora máximo.
- Motores de arranque frecuente (S4): Diseño especial para más ciclos.
Acumulación térmica: El calor de cada arranque se suma al calor de operación. Si no hay tiempo suficiente de enfriamiento entre arranques, la temperatura del rotor puede superar el límite antes de que el relé térmico clásico lo detecte (porque el relé mide I del estátor, no temperatura del rotor).
Protección: Relé electrónico con memoria térmica y contador de arranques. El relé puede bloquear el siguiente arranque si la temperatura acumulada es demasiado alta (función anti-jogging).

### MECHANISM: Cortocircuito_Interno
Descripción: Fallo dieléctrico del aislamiento entre espiras del mismo devanado (cortocircuito entre espiras) o entre fases (cortocircuito fase-fase) dentro del bobinado del estátor.
Causas:
- Degradación térmica del aislamiento (consecuencia de sobrecargas acumuladas)
- Humedad o condensación dentro del motor
- Contaminación química (aceite, disolventes, polvo conductor)
- Sobre-tensiones transitorias (picos de tensión, rayos, maniobras de red)
- Envejecimiento natural del aislamiento
Indicadores eléctricos:
- Asimetría de corrientes entre fases (el devanado afectado toma más corriente).
- En cortocircuito grave entre fases: corriente de cortocircuito muy elevada.
- Temperatura localizada en zona del fallo.
Protección: La protección diferencial de motor (relé diferencial) es la más eficaz para cortocircuitos internos al bobinado. En instalaciones sin diferencial, la coordinación fusible + relé térmico cubre cortocircuitos fase-fase graves pero puede no detectar cortocircuitos entre espiras (fallo incipiente).

---

## SECCIÓN 4 — CURVAS CARACTERÍSTICAS Y PARÁMETROS DE SELECCIÓN

### COMPARISON: Curvas_Par_Velocidad_por_Diseno_NEMA
Los diseños de rotor NEMA definen el perfil torque-velocidad del motor. Esto determina qué tipo de carga puede manejar y cómo debe ajustarse la protección.

**DISEÑO A (Design A):**
- Par arranque: 1.5-2.0 × Tn | Par máximo: 2.5-3.0 × Tn
- Icc arranque: 5-7 × In (alta corriente de arranque)
- Deslizamiento plena carga: 2-5%
- Aplicaciones: Cargas de par constante con arranques infrecuentes.
- Nota protección: Alta Icc requiere tiempo de arranque configurado correctamente.

**DISEÑO B (Design B) — EL MÁS COMÚN:**
- Par arranque: 1.5-2.0 × Tn | Par máximo: 2.0-2.5 × Tn
- Icc arranque: 4-5.5 × In (corriente de arranque moderada)
- Deslizamiento plena carga: 2-5%
- Aplicaciones: Uso general — bombas centrífugas, compresores, ventiladores, transportadores de baja inercia. El estándar de facto en la industria.
- Nota protección: Icc moderada facilita coordinación fusible-relé.

**DISEÑO C (Design C):**
- Par arranque: 2.0-2.5 × Tn (alto par de arranque) | Par máximo: 2.0 × Tn
- Icc arranque: 4-5 × In
- Deslizamiento plena carga: 2-5%
- Aplicaciones: Cargas de alta inercia o alto par estático de arranque: compresores de pistón, bombas de desplazamiento positivo, trituradoras.
- Nota protección: El alto par de arranque reduce el tiempo de aceleración → menor energía térmica acumulada en el arranque.

**DISEÑO D (Design D):**
- Par arranque: 2.5-3.0 × Tn (muy alto par) | Par máximo: igual al de arranque
- Icc arranque: 3-4.5 × In (menor corriente)
- Deslizamiento plena carga: 5-13% (alto)
- Aplicaciones: Cargas de muy alta inercia, punzones, prensas, elevadores.
- Nota protección: Alto deslizamiento = temperatura de rotor más alta en operación normal → ajuste de protección más delicado.

### COMPARISON: Categorias_de_Utilizacion_Motores_IEC
IEC 60947-4-1 define la categoría de utilización del circuito de arranque:

**AC-2:** Motores de anillo rozante (rotor bobinado). Arranque y parada de motores de deslizamiento. Par alto en arranque. Menos común hoy.

**AC-3:** Motores jaula de ardilla. Arranque directo y parada con motor a plena velocidad (apertura en vacío para el contactor). La categoría estándar para la mayoría de aplicaciones: bombas, compresores, ventiladores. El contactor cierra contra la corriente de arranque (alta) pero abre con motor a velocidad (corriente baja o normal).

**AC-4:** Motores jaula de ardilla. Arranque, frenado por contracorriente (plugging) y marcha pulsante (jogging). El contactor debe abrir con corriente de arranque. Aplicaciones más severas: transportadores con frenado eléctrico, prensas. Requiere contactor de mayor capacidad que AC-3 para la misma potencia de motor.

### COMPARISON: Tipos_de_Arranque_y_Efecto_en_Proteccion
El método de arranque determina la corriente de arranque y el tiempo de aceleración, dos parámetros críticos para el ajuste de la protección.

**ARRANQUE DIRECTO (DOL — Direct On Line):**
- Icc arranque: 5-7 × In | Tiempo aceleración: 2-10 segundos típico
- Simplicidad: máxima | Golpe de tensión en red: alto
- Protección: relé térmico + fusibles + contactor AC-3
- Aplicaciones: Motores hasta 15-22 kW en redes con buena capacidad.
- Nota: La protección debe tolerar 5-7 × In durante el tiempo de arranque sin disparar. Curva de arranque correctamente configurada = crítica.

**ARRANQUE ESTRELLA-TRIANGULO (Y-Δ):**
- Icc arranque en Y: 1.5-2.5 × In (reducida a 1/3 vs DOL)
- Tiempo aceleración: Mayor que DOL (dos etapas)
- Transiente de conmutación Y→Δ: Pico de corriente al cambiar (puede ser > DOL)
- Aplicaciones: Motores 15-75 kW, cargas de baja inercia (bombas centrífugas).
- Protección: Dos contactores + temporizador + relé térmico calibrado para In_Δ.
- Nota: El relé térmico debe calibrarse para In/√3 en la parte de la protección que va en los devanados (conexión triángulo). Error común = calibrar para In.

**ARRANCADOR SUAVE (Soft Starter):**
- Icc arranque: 2-4 × In (controlada por ángulo de disparo SCR)
- Rampa de tensión configurable | Sin transiente de conmutación
- Protecciones integradas típicas: sobrecarga, falta de fase, subtensión, PTC.
- Aplicaciones: Motores donde el golpe de arranque daña la carga (bombas con golpe de ariete, transportadores con carga frágil, compresores sensibles).
- Nota: El arrancador suave incluye protecciones propias pero NO reemplaza el relé de sobrecarga ni los fusibles de protección contra cortocircuito.

**VARIADOR DE FRECUENCIA (VFD — Variable Frequency Drive):**
- Icc arranque: 100-150% In (arranque suave inherente)
- Control de velocidad continuo | Arranque y parada con torque controlado
- Protecciones integradas: completas (sobrecarga, falta de fase, cortocircuito, etc.)
- Aplicaciones: Bombas con demanda variable, compresores con control de presión, ventiladores con control de caudal. Ahorro energético significativo en cargas con par cuadrático (bombas y ventiladores).
- Nota: El VFD modifica la forma de onda de alimentación del motor → puede requerir motores de clase INVERTER-DUTY y protección diferencial en cables largos por tensiones parasitas.

---

## SECCIÓN 5 — HALLAZGOS CLAVE

### FINDING: Venezuela_Desequilibrio_Critico
El sistema eléctrico venezolano CORPOELEC presenta desequilibrios de tensión de 3-8% como condición habitual en muchas zonas industriales. Según NEMA MG1, un desequilibrio de 3% genera un incremento de temperatura del motor de ~25% y un desequilibrio de 5% genera ~50% de incremento. Esto reduce drásticamente la vida útil del motor y hace obligatoria la protección de desequilibrio en cualquier motor de proceso crítico instalado en Venezuela.

### FINDING: Temperatura_Ambiente_Factor_Limitante
Las temperaturas ambientes típicas en instalaciones industriales venezolanas (35-55°C) consumen una fracción significativa del margen térmico de la clase de aislamiento. Un motor Clase F (límite 155°C) en ambiente de 50°C tiene solo 105°C de margen de elevación vs los 115°C de diseño estándar. Esto equivale a una reducción de capacidad del ~9% que la protección debe compensar con ajustes de umbral más conservadores que los típicos IEC/NEMA.

### FINDING: Perdida_de_Fase_Riesgo_Principal
La pérdida de fase es la condición de falla más frecuente y más destructiva en motores venezolanos, asociada a fusibles quemados, contactores con contacto dañado o cortes selectivos de CORPOELEC. Un motor de 5 kW sin protección de falta de fase puede destruirse en menos de 2 minutos de monofásico. La protección de falta de fase tiene un costo marginal mínimo vs el costo de rebobinado (~30-60% del valor del motor) o reposición del motor.

### FINDING: Curva_de_Arranque_Ajuste_Critico
El ajuste incorrecto de la curva de arranque (tiempo de arranque en el relé térmico o electrónico) es la causa más común de disparos intempestivos en motores de bombas y compresores. Un tiempo de arranque demasiado corto hace que el relé dispare durante el arranque legítimo. Un tiempo demasiado largo deja al motor sin protección durante stall o arranque fallido. El ajuste debe basarse en el tiempo real de aceleración medido + 20-30% de margen.

### FINDING: Regla_10_Grados_Arrhenius
Por cada 10°C de operación sobre el límite de clase de aislamiento, la vida útil del aislamiento se reduce a la mitad. La implicación práctica es que operar un motor a 120°C en vez de 100°C (en aislamiento Clase A, límite 105°C) no reduce la vida en un 15% sino que la reduce al 50%. La protección térmica correcta no solo evita la falla catastrófica inmediata: protege la vida útil total del motor, que en un motor de proceso puede representar 10-20 años de operación.

### FINDING: Corriente_No_es_Temperatura
Los relés térmicos bimetálicos clásicos modelan la temperatura del motor a través de la corriente, asumiendo una relación directa. Pero la temperatura real depende también de: temperatura ambiente, velocidad de rotación, fluido refrigerante (bombas sumergibles), ciclo de carga real vs ciclo de corriente. Los relés electrónicos modernos con modelos térmicos avanzados son superiores precisamente porque modelan la temperatura con más variables. Para motores críticos de proceso, un relé con RTD o PTC externo es la solución más precisa.

### FINDING: Stall_Mas_Peligroso_En_Arranque
El stall durante el arranque es más peligroso que el stall durante la operación porque ocurre justo cuando el motor tiene más corriente (5-7 × In) y menos refrigeración (el ventilador interno aún no gira a velocidad plena). Un relé térmico clásico puede tardar 30-90 segundos en disparar con corriente de arranque, tiempo suficiente para destruir un motor pequeño (<5 kW). Los relés electrónicos con función "locked rotor" disparan en 1-4 segundos.

---

## SECCIÓN 6 — FUENTES Y NORMAS DE REFERENCIA

### SOURCE: IEC_60034_1
International Electrotechnical Commission. IEC 60034-1: Rotating electrical machines — Part 1: Rating and performance. Ginebra, IEC.
Contenido: Definiciones de parámetros nominales, clases de aislamiento, temperatura de referencia, grados de protección, regímenes de servicio.
Disponibilidad: IEC.ch (pago) | Versiones académicas en IEEE Xplore.

### SOURCE: IEC_60034_5
International Electrotechnical Commission. IEC 60034-5: Degrees of protection provided by the integral design of rotating electrical machines (IP Code).
Contenido: Definición y clasificación de grados de protección IP para motores.

### SOURCE: NEMA_MG1
National Electrical Manufacturers Association. NEMA MG1: Motors and Generators. Roslyn (VA), NEMA.
Contenido: Clasificación de diseños A-D, corrientes de arranque, pares, derating por temperatura y altitud, tablas de corrientes nominales.
Nota: Referencia estándar para equipos importados de EE.UU. y Canadá.

### SOURCE: IEC_60947_4_1
International Electrotechnical Commission. IEC 60947-4-1: Low-voltage switchgear and controlgear — Part 4-1: Contactors and motor-starters. Electromechanical contactors and motor-starters.
Contenido: Categorías de utilización AC-2/3/4, requisitos de contactores y arrancadores, clasificación de relés de sobrecarga (Clase 10/20/30).

### SOURCE: COVENIN_3028
FONDONORMA / COVENIN. COVENIN 3028: Motores eléctricos de corriente alterna. Motores trifásicos de inducción de jaula. Caracas, FONDONORMA.
Contenido: Requisitos mínimos para motores de inducción trifásicos en el contexto eléctrico venezolano.

### SOURCE: Arrhenius_Thermal_Degradation
Dakin, T.W. (1948). Electrical Insulation Deterioration Treated as a Chemical Rate Phenomenon. AIEE Transactions. Vol. 67, pp. 113-122.
Contenido: Fundamento científico de la regla de los 10°C para degradación de aislamiento. Base de todos los modelos de vida útil de motores eléctricos.

### SOURCE: NEMA_MG1_Voltage_Unbalance
National Electrical Manufacturers Association. NEMA MG1-2016, Section 12.45: Effect of Unbalanced Voltages.
Contenido: Tablas de incremento de temperatura por porcentaje de desequilibrio de tensión. Referencia estándar para protección de desequilibrio.

### SOURCE: Chapman_Electric_Machinery
Chapman, S.J. (2012). Máquinas Eléctricas (5ta edición). McGraw-Hill.
Contenido: Referencia didáctica completa de motores trifásicos: principio de operación, circuito equivalente, curvas par-velocidad, eficiencia, arranque.
Disponibilidad: Texto universitario, disponible en bibliotecas técnicas.

---

**FIN DEL ATLAS 1 — MOTORES TRIFÁSICOS**
Proyecto ProtMotores | Versión 1.0 | Marzo 2026
Siguiente: Atlas 2 — Protecciones Eléctricas de Motores
