# ATLAS 3 — APLICACIONES: BOMBEO, REFRIGERACIÓN Y MÁQUINAS ROTATIVAS

**Base de Conocimiento:** Protecciones Eléctricas para Motores Trifásicos
**Proyecto:** ProtMotores | Carril 2 — Técnico/Industrial
**Mercado:** Venezuela | Normas: COVENIN + IEC 60947 + NEMA MG1
**Versión:** 1.0 | Marzo 2026
**Prefijos RAG:** INGLÉS | Contenido: ESPAÑOL

---

## SECCIÓN 1 — CONCEPTOS FUNDAMENTALES DE APLICACIONES

### CONCEPT: Par_de_Carga_vs_Par_Motor
Definición: El par de carga (T_carga) es la resistencia mecánica que la máquina accionada impone sobre el eje del motor. La condición de operación estable requiere que el par motor sea igual al par de carga en la velocidad de operación: T_motor(Nr) = T_carga(Nr).
Tipos de curva de par de carga (relevantes para protección):

**PAR CONSTANTE:** T_carga = constante independientemente de la velocidad.
- Ejemplos: Transportadores horizontales de banda, bombas de desplazamiento positivo, compresores de pistón a velocidad fija.
- Implicación protección: Si el motor se frena (↓Nr → ↑deslizamiento → ↑corriente), el par de carga no cede → condición de stall posible.

**PAR CUADRÁTICO (PAR VENTILADOR):** T_carga ∝ Nr².
- Ejemplos: Bombas centrífugas, ventiladores centrífugos y axiales.
- Implicación protección: A velocidad reducida, el par de carga es muy bajo → el motor arranca con facilidad incluso con tensión reducida.
- Con VFD: La reducción de velocidad reduce drásticamente el par de carga → gran ahorro energético y menor estrés del arranque.

**PAR LINEAL:** T_carga ∝ Nr.
- Ejemplos: Algunos generadores, laminadoras.

**PAR CON PICO EN ARRANQUE:** T_carga tiene un pico estático (mayor que el de operación) que debe superarse para poner en marcha la carga.
- Ejemplos: Compresores de pistón con válvulas cerradas, transportadores cargados en parada.
- Implicación protección: El motor necesita suficiente par de arranque → diseño NEMA C o D. El relé debe tolerar la corriente de arranque más larga.

### CONCEPT: Inercia_de_la_Carga
Definición: La inercia (momento de inercia J, en kg·m²) representa la resistencia de la masa giratoria a cambiar su velocidad de rotación.
Fórmula básica: J = m × r² (masa × radio al cuadrado)
Relación con el arranque: T_neto = J × dω/dt → a mayor inercia, más tiempo se tarda en acelerar → mayor duración del arranque → mayor calor acumulado en el rotor durante el arranque.
Clasificación práctica:
- **BAJA INERCIA:** Bombas centrífugas de rotor pequeño, ventiladores axiales. Tiempo de arranque típico: 1-5 segundos. Clase 10.
- **INERCIA MEDIA:** Compresores de pistón, bombas de mayor tamaño, sopladores. Tiempo de arranque típico: 3-10 segundos. Clase 10 o 20.
- **ALTA INERCIA:** Molinos, prensas, centrifugadoras, volantes de inercia. Tiempo de arranque típico: 10-30 segundos. Clase 20 o 30.
- **MUY ALTA INERCIA:** Grandes ventiladores industriales, molinos de bolas. Tiempo de arranque típico: 15-45 segundos. Clase 30. Posible arrancador suave o VFD para reducir el calor de arranque.

### CONCEPT: Curva_Sistema_Hidraulico
Aplicable a: Bombas centrífugas y sistemas de bombeo.
Definición: La curva del sistema hidráulico describe la presión (cabeza) que el sistema requiere a cada caudal. Resulta de la suma de:
H_sistema = H_estática + H_dinámica(Q)
Donde:
- H_estática: Diferencia de altura geométrica + presión estática en puntos de succión y descarga (no depende del caudal).
- H_dinámica: Pérdidas por fricción en tuberías, accesorios, válvulas (proporcional al cuadrado del caudal: H_din ∝ Q²).
Punto de operación: Intersección entre la curva de la bomba y la curva del sistema. En este punto: Q_operación y H_operación (caudal y cabeza de trabajo).
Implicación para protección:
- Si H_estática aumenta (nivel del depósito sube, válvula parcialmente cerrada) → el punto de operación se desplaza a menor Q y mayor H → la bomba trabaja con más carga → corriente del motor puede aumentar.
- Si el sistema tiene problemas (tubería obstruida, válvula cerrada) → la bomba trabaja contra H máxima → corriente mínima pero posible sobrecalentamiento por recirculación interna en la bomba.
- Bomba operando a caudal cero (válvula cerrada) = "shutoff head" → corriente del motor es MENOR que a plena carga pero la bomba se calienta. El monitor de caudal (o presión) es más efectivo que el relé de corriente para proteger esta condición.

---

## SECCIÓN 2 — APLICACIONES: BOMBEO SUPERFICIAL Y SUMERGIBLE

### TECH_APPLICATION: Bombas_Centrifugas_Superficiales
Descripción: Motores trifásicos acoplados a bombas centrífugas instaladas sobre la superficie, con tubería de succión (generalmente bajo nivel del agua) y tubería de descarga. Las más comunes en Venezuela para: suministro de agua potable, sistemas de riego, recirculación de agua de procesos industriales, elevación de aguas residuales.
Configuraciones típicas:
- Monoblock horizontal: Motor y bomba en un solo conjunto horizontal.
- Acoplamiento directo: Motor horizontal acoplado a bomba a través de flexible.
- Motor vertical sobre carcasa de bomba: Instalación compacta en pozos o tanques superficiales.
Perfil de par de carga: Cuadrático (T ∝ N²). Fácil arranque.
Inercia: Baja a media.
Modo de operación típico Venezuela: Ciclos continuos o con arranques frecuentes según control de nivel (boya, sensor de presión, control de presión constante).

**FALLAS TÍPICAS Y PROTECCIONES REQUERIDAS:**

1. **MARCHA EN SECO:** La bomba arranca pero no hay agua en la succión (cisterna vacía, válvula de succión cerrada, cavitación severa). La corriente del motor BAJA (no sube) porque la bomba no trabaja contra carga. Un relé de sobrecarga NO detecta esta condición.
   - Protección requerida: Sensor de presión de succión (mínima presión) o sensor de caudal o presostato de baja presión conectado al circuito de control. Como segunda opción: relé de baja potencia o relé de baja carga.

2. **SOBRECARGA POR EXCESO DE CAUDAL:** La bomba trabaja a caudal mayor al nominal (válvula de descarga muy abierta, presión de descarga muy baja). La corriente del motor puede superar In → sobrecarga real.
   - Protección requerida: Relé de sobrecarga (bimetálico o electrónico).

3. **DESEQUILIBRIO Y FALTA DE FASE:** Muy frecuente en instalaciones venezolanas con suministro irregular de CORPOELEC.
   - Protección requerida: Monitor de red trifásico.

4. **INUNDACIÓN DEL MOTOR:** En instalaciones donde el motor puede quedar sumergido por crecida (sótanos, fosas). La humedad degrada el aislamiento.
   - Protección complementaria: Detector de humedad (flotador de nivel alto) que detenga el motor antes de inundación.

**CONFIGURACIÓN DE PROTECCIÓN RECOMENDADA:**
- Nivel mínimo: Guardamotor MPCB + Contactor AC-3 + Relé térmico bimetálico + Monitor de red + Presostato de baja presión en succión.
- Nivel recomendado: Guardamotor MPCB + Contactor AC-3 + Relé electrónico + Monitor de red + Sensor de presión analógico + Clase 10.

CLASE DE DISPARO: Clase 10 (inercia baja, arranque corto).
FACTOR DE SERVICIO: Usar FS = 1.0 para ajuste del relé (bombas no tienen margen).

### TECH_APPLICATION: Bombas_Sumergibles_Pozo_Profundo
Descripción: Motor y bomba forman una unidad sellada instalada dentro de un pozo perforado, sumergida en el agua que bombea. El agua es simultáneamente el fluido bombeado y el refrigerante del motor.
Características especiales del motor sumergible:
- Motor totalmente encapsulado: IP68 (sumergible permanente).
- Refrigeración: Por el agua que circula alrededor de la carcasa del motor.
- Sin ventilador exterior: La refrigeración depende completamente del flujo de agua.
- Cables especiales: Resistentes a la humedad, flexibles, con terminaciones impermeables.
- Arranque: Directo (DOL) generalmente. El conductor largo entre el tablero superficial y el motor introduce caída de tensión adicional.
Profundidades típicas Venezuela: 20-200 metros de pozo. Motor sumergido 1-3 metros sobre el fondo del pozo.

**FALLAS TÍPICAS Y PROTECCIONES REQUERIDAS:**

1. **MARCHA EN SECO (la más crítica y frecuente en Venezuela):** El nivel del agua baja hasta descubrir la bomba o la entrada de succión. Sin agua circulando, el motor se recalienta RÁPIDAMENTE (en minutos, no horas) porque pierde toda su refrigeración. La corriente puede no subir significativamente → el relé de sobrecarga NO protege esta condición.
   - Protección OBLIGATORIA: Sonda de nivel de agua en el pozo (electrónica o flotador) que detenga la bomba cuando el nivel baja del mínimo. Como segunda línea: termistor PTC en el devanado del motor.

2. **ARENA Y ABRASIVOS:** El bombeo de agua con arena desgasta el impulsor y los sellos. El motor puede no verse afectado eléctricamente hasta que el desgaste sea severo.
   - Detección: Incremento gradual de corriente, reducción de caudal/presión.
   - Protección preventiva: Monitoreo periódico de corriente + reemplazo programado de partes mecánicas.

3. **CAÍDA DE TENSIÓN POR CABLE LARGO:** El cable entre el tablero superficial y el motor sumergible tiene resistencia significativa. A 50 metros de profundidad con cable 4mm², la caída puede ser 5-10V → subtensión en el motor.
   - Efecto: Corriente más alta, calentamiento adicional, riesgo de stall en arranques con agua viscosa o fría.
   - Corrección: Seleccionar cable de mayor sección (6mm² o 10mm²). Calcular caída de tensión antes de la instalación. La protección de subtensión en el tablero superficial detecta este problema.

4. **DESEQUILIBRIO DE FASES EN CABLE LARGO:** Un cable largo con una fase de mayor resistencia (empalme deficiente, corrosión en conector) produce desequilibrio. Combinado con el desequilibrio de la red → efecto acumulado.
   - Protección: Monitor de red en el tablero + medición periódica de corrientes de las tres fases en el tablero (comparar I_L1, I_L2, I_L3).

5. **CONDENSACIÓN AL ARRANCAR:** Si el pozo está seco y el motor frío, puede condensarse humedad cuando se energiza. En motores sin PTC, esto puede generar fuga a tierra.
   - Protección: Relé diferencial de tierra (GFCI/RCD) en el tablero superficial.

**CONFIGURACIÓN DE PROTECCIÓN RECOMENDADA:**
- MÍNIMO OBLIGATORIO: Guardamotor + Contactor + Relé electrónico con entrada PTC + Monitor de red + Sonda de nivel de pozo.
- RECOMENDADO: Lo anterior + Relé diferencial de tierra (RCD 30-300 mA) + Indicador de corriente de las tres fases + Temporizador de rearranque (espera 10-15 minutos antes de rearrancar después de paro por nivel bajo).

### TECH_APPLICATION: Bombas_Sumergibles_Aguas_Residuales
Descripción: Bombas sumergibles para elevación de aguas residuales domésticas o industriales en fosas sépticas, plantas de tratamiento, bombas de achique.
Diferencias vs. bomba de pozo profundo:
- El fluido bombeado es agresivo (corrosivo, abrasivo, con sólidos).
- Las bombas están diseñadas para pasar sólidos (impulsor tipo vórtex o semi-abierto).
- El nivel de la fosa varía: la bomba arranca y para frecuentemente (control por flotadores de nivel alto/bajo).

**FALLAS TÍPICAS:**

1. **ATASCO DEL IMPULSOR:** Material sólido (trapos, plásticos) atasca el impulsor.
   - Efecto: Corriente sube a 5-7 × In (stall) → disparo por locked rotor o sobrecarga severa.
   - Protección: Relé electrónico con función locked rotor (disparo en 2-5s).

2. **ARRANQUES FRECUENTES:** El ciclo de nivel puede producir 10-30 arranques/hora en horas pico. Acumulación térmica en el motor.
   - Protección: Relé electrónico con memoria térmica y función anti-jogging. Ajuste de flotadores para maximizar el intervalo entre arranques.

3. **FUNCIONAMIENTO SUMERGIDO SIN AGUA (fosa vacía en mantenimiento):** Similar a marcha en seco. Protección por flotador de nivel mínimo.

CLASE DE DISPARO: Clase 10 (tiempo arranque corto, inercia baja).

---

## SECCIÓN 3 — APLICACIONES: COMPRESORES DE REFRIGERACIÓN

### TECH_APPLICATION: Compresores_Hermeticos_Semiermeticos
Descripción: Compresores de refrigeración donde el motor y el compresor están en la misma carcasa sellada (hermético) o en carcasa desmontable (semiermético). El refrigerante enfría el motor directamente.
Tipos más comunes en Venezuela:
- **Compresor hermético** (reciprocante o scroll): Unidades pequeñas y medianas (hasta ~20 TR — toneladas de refrigeración). Uso en aires acondicionados residenciales y comerciales, cámaras frigoríficas pequeñas.
- **Compresor semiermético** (reciprocante): Unidades medianas a grandes (2-100 TR). Plantas de refrigeración industrial, cámaras frigoríficas de supermercados, procesadoras de alimentos.
- **Compresor de tornillo** (screw): Unidades grandes (>20 TR). Refrigeración industrial, proceso de aire comprimido.
Característica especial: El gas refrigerante es también el refrigerante del motor. Si hay pérdida de refrigerante o si el compresor opera sin cargar el circuito, el motor se recalienta.

**FALLAS TÍPICAS Y PROTECCIONES REQUERIDAS:**

1. **ARRANQUE CON ALTA PRESIÓN DE DESCARGA (LIQUID SLUGGING):** Si el compresor arranca con líquido refrigerante acumulado en la cámara (por migración en el paro), el par de arranque requerido puede ser muy alto. Riesgo de stall o daño mecánico al compresor (golpe de líquido).
   - Protección: Calentador de cárter (crankcase heater) para evaporar el líquido antes del arranque. Temporizador de retardo en el arranque (15-30 min después de paro prolongado).

2. **CORTE DE FASE (el más destructivo para compresores):** El compresor puede continuar operando en monofásico → corriente muy alta → daño en minutos. El compresor hermético no es rebobinable (hay que cambiarlo).
   - Protección OBLIGATORIA: Monitor de red con falta de fase. Relé de secuencia.

3. **ALTA TEMPERATURA DE DESCARGA:** Si el refrigerante es insuficiente o hay alta relación de compresión, la temperatura de descarga del gas sube. El motor se recalienta.
   - Protección: Termostato de alta temperatura de descarga (klixon) + termistor PTC en el devanado del motor (en compresores que lo incluyen).

4. **PRESIÓN ALTA / BAJA ANORMAL:** Alta presión de condensación (condensador sucio, temperatura ambiente muy alta, ventilador de condensador fallido) o baja presión de evaporación (sistema sin refrigerante).
   - Protección: Presostato de alta y baja presión en el circuito de refrigerante (no en el circuito eléctrico del motor, sino en la línea de refrigerante). El presostato corta el circuito de control del contactor del compresor.

5. **ARRANQUES FRECUENTES (ciclos cortos):** Control de temperatura muy ajustado → arranques cada 1-3 minutos. El motor de compresor se recalienta por acumulación térmica de arranques.
   - Protección: Temporizador de tiempo mínimo entre arranques (anti-short cycle timer). Mínimo 3-5 minutos entre arranques para permitir enfriamiento.

6. **INVERSIÓN DE FASE:** Un compresor de pistón girando al revés no comprime. Puede dañar válvulas y el conjunto mecánico rápidamente.
   - Protección: Monitor de red con detección de secuencia de fases.

**CONFIGURACIÓN PROTECCIÓN COMPRESOR HERMÉTICO/SEMIERMÉTICO:**
- OBLIGATORIO: Guardamotor + Contactor AC-3 + Relé electrónico (o bimetálico de alta calidad) + Monitor de red (falta de fase + secuencia + subtensión) + Temporizador de mínimo tiempo entre arranques.
- RECOMENDADO: Agregar termistor PTC (si el motor lo incluye) + presostato alta y baja presión + sensor de temperatura de descarga.
- CLASE DE DISPARO: Clase 20 (par de arranque alto, algo de inercia).

### TECH_APPLICATION: Compresores_de_Aire
Descripción: Compresores para aire comprimido industrial: de pistón (reciprocante), tornillo (rotativo) o centrífugo. Motores trifásicos de inducción acoplados directamente o por fajas.

**FALLAS TÍPICAS:**

1. **ARRANQUE CON PRESIÓN RESIDUAL:** Compresores de pistón que arrancan sin descargar la presión residual en el cabezal → alto par de arranque inicial.
   - Protección mecánica: Válvula de descarga (unloader) que descarga el cabezal antes del arranque. La protección eléctrica debe tolerar la Icc de arranque más larga.

2. **SOBRECALENTAMIENTO POR VENTILACIÓN INSUFICIENTE:** El motor y el compresor generan calor. En salas de compresores mal ventiladas en Venezuela (45-55°C), el motor se sobrecalienta aun con carga normal.
   - Protección: Termistor PTC + buena ventilación del cuarto de máquinas.

3. **CORREA ROTA (transmisión por fajas):** Si la correa se rompe, el motor gira sin carga → corriente baja (subvoltaje de carga). El compresor no comprime → el presostato no apaga el motor → motor gira en vacío indefinidamente. Esto no daña el motor inmediatamente pero es ineficiencia operativa.
   - Protección: Sensor de presión o presostato que verifique que el compresor está produciendo presión. Si la presión no sube en X minutos → alarma.

CLASE DE DISPARO: Clase 20 (compresores de pistón) / Clase 10 (tornillo).

---

## SECCIÓN 4 — APLICACIONES: VENTILADORES Y TRANSPORTADORES

### TECH_APPLICATION: Ventiladores_Axiales_y_Centrifugos
Descripción: Motores trifásicos accionando ventiladores para movimiento de aire: ventilación de edificios, refrigeración de procesos (torres de enfriamiento, condensadores evaporativos, intercambiadores), extracción de gases industriales.
Perfil de par: Cuadrático (T ∝ N²). El ventilador es la aplicación de par cuadrático por excelencia → el motor arranca con carga mínima.
Inercia: Variable. Ventiladores pequeños: baja. Ventiladores grandes industriales (>5000 m³/h): puede ser alta inercia.

**FALLAS TÍPICAS:**

1. **INVERSIÓN DE SENTIDO DE GIRO:** El ventilador gira al revés → caudal de aire casi nulo (el impulsor genera presión en sentido opuesto al diseñado). El motor no se daña pero la aplicación falla → sistema refrigerado se sobrecalienta.
   - Detección: Ausencia de caudal de aire (sensor de presión diferencial o termómetro en el espacio ventilado). Protección preventiva: verificar sentido de giro en comisionamiento.

2. **ASPA TRABADA O DESEQUILIBRADA:** Un objeto bloquea el aspa → stall del motor. O el aspa pierde un elemento → vibración severa → daño mecánico.
   - Protección: Relé de sobrecarga + detector de vibración (en ventiladores grandes industriales). Protección contra stall con función locked rotor.

3. **POLVO Y SUCIEDAD EN EL MOTOR:** En aplicaciones de extracción de polvo o gases con partículas, el motor acumula suciedad → obstrucción de ventilación → sobrecalentamiento.
   - Protección: Motor IP54 o IP55 mínimo. Termistor PTC. Programa de limpieza.

4. **FRECUENTES ARRANQUES EN VENTILADORES DE GRAN INERCIA:** Un ventilador industrial grande puede tardar 15-30 segundos en acelerar. Arranques frecuentes acumulan calor en el rotor.
   - Protección: Relé electrónico con memoria térmica + clase 30.

CLASE DE DISPARO: Clase 10 (ventiladores pequeños y medianos) / Clase 20-30 (ventiladores de gran inercia).
TIPO DE ARRANQUE: DOL para pequeños. Estrella-triángulo o arrancador suave para ventiladores grandes (para reducir el golpe de arranque en la red y el estrés mecánico del sistema de transmisión).

### TECH_APPLICATION: Transportadores_de_Banda
Descripción: Motores trifásicos accionando bandas transportadoras: industria alimentaria, minería, cementeras, plantas de distribución. Pueden ser horizontales, inclinados, o combinados.
Perfil de par:
- Transportador horizontal en vacío: Par casi constante bajo.
- Transportador inclinado con carga: Par constante alto (≈ m × g × sen(θ) × r).
- Arranque con carga: Par de arranque alto → posible diseño NEMA C.
Inercia: Variable. Bandas largas con mucha masa: alta inercia.

**FALLAS TÍPICAS:**

1. **BANDA ATASCADA (STALL CON CARGA):** Material atasca la banda → motor en stall. Corriente = 5-7 × In de forma inmediata y sostenida.
   - Protección: Relé electrónico con función locked rotor. Tiempo de disparo 1-5 segundos. Protección mecánica: cordón de parada de emergencia a lo largo de la banda (norma de seguridad).

2. **SOBRECARGA POR EXCESO DE MATERIAL:** Más material del diseñado → par de carga mayor al nominal → corriente > In.
   - Protección: Relé de sobrecarga ajustado correctamente.

3. **BANDA ROTA O DESLIZANTE:** La banda se rompe o desliza sobre los rodillos → el motor gira sin carga → corriente baja.
   - Protección: Sensor de velocidad de banda (tacómetro o encoder) que detecte discrepancia entre velocidad del motor y velocidad de la banda.

4. **ARRANQUE CON CARGA EN TRANSPORTADOR INCLINADO:** Si el transportador se para con carga y debe arrancar cargado, el par de arranque requerido es muy alto (par estático de la carga inclinada + fricción de arranque).
   - Protección/solución: Motor con FS = 1.15 o 1.25. Diseño NEMA C. En bandas grandes: Arrancador suave con rampa de par controlada.

5. **FRENADO BRUSCO (FRENO MECÁNICO):** En transportadores inclinados, al parar el motor, si no hay freno mecánico, la carga puede hacer retroceder la banda.
   - Protección mecánica: Trinquete (backstop) o freno electromagnético. El relé de protección no actúa en esta condición pero puede coordinarse con el freno.

CLASE DE DISPARO: Clase 10 (transportadores horizontales ligeros) / Clase 20 (transportadores con carga pesada o inclinados).
CATEGORÍA DE UTILIZACIÓN: AC-3 para operación normal. AC-4 si hay jogging frecuente o frenado por inversión.

### TECH_APPLICATION: Motores_en_Aplicaciones_Especiales
Descripción: Otras aplicaciones de motores trifásicos con características particulares de protección:

**BOMBAS DE DESPLAZAMIENTO POSITIVO (engranajes, lóbulos, pistón):**
- Par: Constante. No depende cuadráticamente de N.
- Riesgo principal: Si la válvula de descarga está cerrada, la presión sube hasta el límite mecánico de la bomba y de la tubería → riesgo de rotura. La corriente del motor también sube (par constante = corriente constante al disminuir N → corriente de stall si se detiene completamente).
- Protección obligatoria: Válvula de alivio de presión en la descarga (mecánica) + relé de sobrecarga (protege el motor en stall).

**MOLINOS Y TRITURADORES:**
- Par: Alto en arranque, variable en operación (según dureza del material).
- Inercia: Alta a muy alta.
- Riesgo: Sobrecarga por material duro o exceso de alimentación. Stall si el material atasca el molino.
- Protección: Clase 30 + función locked rotor + sensor de vibración.

**AGITADORES Y MEZCLADORES:**
- Par: Constante (resistencia del fluido al agitador).
- Riesgo: Aumento de viscosidad del fluido (frío, cambio de producto) → aumento de par de carga → sobrecarga.
- Protección: Relé de sobrecarga + monitor de red.

**BOMBAS DE CALOR / CHILLER:**
- Igual a compresores de refrigeración pero con requerimientos más estrictos por el mayor costo del equipo.
- Protección: Nivel premium recomendado.

---

## SECCIÓN 5 — CRITERIOS DE SELECCIÓN POR APLICACIÓN

### COMPARISON: Matriz_Seleccion_Proteccion_Por_Aplicacion
Guía de selección rápida del nivel de protección según aplicación:

| Aplicación                    | Clase IEC | Monitor Red | Relé Tipo  | PTC | Nivel Prot. |
|-------------------------------|-----------|-------------|------------|-----|-------------|
| Bomba centrífuga superficial  | 10        | ✓ Oblig     | Electrón.  | No  | Estándar    |
| Bomba sumergible pozo profundo| 10        | ✓ Oblig     | Electrón.  | ✓   | Premium     |
| Bomba sumergible aguas resid. | 10        | ✓ Oblig     | Electrón.  | No  | Estándar    |
| Compresor hermético A/C       | 20        | ✓ Oblig     | Bimetál.\* | ✓\* | Estándar    |
| Compresor semiermético refrig.| 20        | ✓ Oblig     | Electrón.  | ✓   | Premium     |
| Compresor de aire pistón      | 20        | ✓ Oblig     | Electrón.  | No  | Estándar    |
| Compresor de aire tornillo    | 10        | ✓ Oblig     | Electrón.  | No  | Estándar    |
| Ventilador axial pequeño      | 10        | Recomen     | Bimetál.   | No  | Básico      |
| Ventilador centrífugo grande  | 20-30     | ✓ Oblig     | Electrón.  | No  | Estándar    |
| Transportador horizontal      | 10-20     | Recomen     | Bimetál.   | No  | Básico      |
| Transportador inclinado carga | 20        | ✓ Oblig     | Electrón.  | No  | Estándar    |
| Molino / Triturador           | 30        | ✓ Oblig     | Electrón.  | No  | Estándar    |
| Motor proceso continuo crítico| 20        | ✓ Oblig     | Electrón.  | ✓   | Premium     |

(\*) Los compresores herméticos de A/C típicamente incluyen protector interno (klixon) y a veces PTC. El relé externo es complemento.

### COMPARISON: Clase_de_Disparo_Por_Tiempo_Arranque
Guía para seleccionar la clase de disparo según el tiempo de arranque real del motor con su carga:

| Tiempo de arranque (medido) | Clase recomendada | Margen seguridad |
|------------------------------|-------------------|------------------|
| < 2 segundos                 | Clase 10A         | 20%              |
| 2 - 4 segundos               | Clase 10          | 25%              |
| 4 - 8 segundos               | Clase 10 o 20     | 25-30%           |
| 8 - 15 segundos              | Clase 20          | 30%              |
| 15 - 25 segundos             | Clase 30          | 30%              |
| > 25 segundos                | Clase 30 + arrancador suave | Evaluar |

Nota: Si el tiempo de arranque supera los 25 segundos con DOL, considerar arrancador suave o VFD para reducir el calor de arranque y proteger el motor.

### COMPARISON: Recomendacion_Cable_Sumergible_Por_Profundidad
Caída de tensión máxima admisible en cable de motor sumergible: 3% de Vn.
(Venezuela: 3% × 220V = 6.6V máximo o 3% × 440V = 13.2V máximo)

| Potencia Motor | Profundidad (m) | Sección cable 220V | Sección cable 440V |
|----------------|-----------------|---------------------|---------------------|
| 1 - 3 HP       | 30 m            | 2.5 mm²             | 1.5 mm²             |
| 1 - 3 HP       | 60 m            | 4 mm²               | 2.5 mm²             |
| 3 - 7.5 HP     | 30 m            | 4 mm²               | 2.5 mm²             |
| 3 - 7.5 HP     | 60 m            | 6 mm²               | 4 mm²               |
| 7.5 - 15 HP    | 30 m            | 6 mm²               | 4 mm²               |
| 7.5 - 15 HP    | 60 m            | 10 mm²              | 6 mm²               |
| 15 - 30 HP     | 30 m            | 10 mm²              | 6 mm²               |
| 15 - 30 HP     | 60 m            | 16 mm²              | 10 mm²              |

Nota: Siempre calcular para la potencia y profundidad específicas. Usar cable especial para sumergibles (flexible, resistente a agua, con cubierta especial).

---

## SECCIÓN 6 — HALLAZGOS CLAVE

### FINDING: Marcha_En_Seco_Principal_Causa_Venezuela
En el contexto venezolano, la marcha en seco de bombas (superficiales y sumergibles) es la causa más frecuente de daño de motores de bombeo, seguida de cerca por la falta de fase. Las sequías recurrentes, los cortes de agua potable y los niveles bajos en cisternas hacen que las bombas operen sin agua con frecuencia. Esta condición NO es detectada por el relé de sobrecarga estándar, ya que la corriente del motor baja (no sube) cuando no hay carga. La protección correcta es el sensor de presión de succión o nivel de cisterna.

### FINDING: Compresores_Hermeticos_No_Rebobinables
A diferencia de un motor estándar que puede rebobinarse a un costo de 30-60% del precio de uno nuevo, los compresores herméticos de refrigeración no pueden rebobinarse ni repararse en campo: cuando el motor interno falla, se reemplaza el compresor completo. El costo de un compresor hermético quemado es 3-10× el costo de un compresor estándar equivalente. Esto justifica una inversión en protección superior a la que se haría para un motor estándar equivalente.

### FINDING: Ventilador_De_Motor_Ineficaz_A_Baja_Velocidad
El ventilador de refrigeración del motor (solidario al eje) reduce su caudal de forma cuadrática con la velocidad: a 50% de la velocidad nominal, el caudal de refrigeración es solo 25% del nominal. Esto es crítico en motores accionados por VFD que operan a velocidades reducidas de forma continua. Un motor estándar operando a 30 Hz (50% de velocidad) en un VFD tiene refrigeración de solo 25%, por lo que puede sobrecalentarse incluso con carga nominal. Para esta aplicación se requieren motores INVERTER-DUTY con ventilación forzada externa independiente del eje, o una reducción de la carga admisible a velocidades bajas.

### FINDING: Arrancador_Suave_No_Reemplaza_Proteccion
Un error frecuente en Venezuela es asumir que la presencia de un arrancador suave o un VFD elimina la necesidad de protección eléctrica externa. Los arrancadores suaves y VFD incluyen protecciones integradas, pero estas protegen principalmente el propio dispositivo electrónico, no el motor de forma exhaustiva. Es obligatorio mantener la protección externa (fusibles o interruptor + relé de sobrecarga) incluso con arrancador suave o VFD, especialmente para la protección de cortocircuito y la protección de la red de alimentación.

### FINDING: Tiempo_Minimo_Entre_Arranques_Critico
La falla de no respetar el tiempo mínimo entre arranques es la causa más común de quema de motores de compresores de refrigeración en Venezuela. Las unidades de aire acondicionado con termostatos mal calibrados o termostatos defectuosos pueden generar ciclos de 30 segundos on / 30 segundos off → el motor no alcanza a enfriarse entre arranques → falla térmica acumulativa. Un anti-short cycle timer de $5-15 USD previene esta falla que puede costar $200-2000 USD en reposición de compresor.

### FINDING: Seleccion_Cable_Sumergible_Subestimada
La selección de cables subterráneos o sumergibles en instalaciones venezolanas frecuentemente subestima la caída de tensión a plena carga por el uso de tablas diseñadas para factores de potencia y corrientes nominales ideales. En la práctica, con la red CORPOELEC ya con subtensión (210-215V en vez de 220V), más la caída en el cable, el motor sumergible puede estar recibiendo 190-200V (86-91% de Vn). Esto representa una subtensión severa que aumenta la corriente, reduce el par, y puede causar fallos de arranque o sobrecalentamiento.

---

## SECCIÓN 7 — NORMAS Y FUENTES

### SOURCE: HI_Pump_Standards
Hydraulic Institute. HI 9.6.5: Pump Piping. Parsippany (NJ): HI.
Contenido: Estándares de instalación de bombas, condiciones de operación, protección contra operación fuera de rango. Referencia técnica para aplicaciones de bombeo.

### SOURCE: ASHRAE_Handbook_HVAC
ASHRAE. ASHRAE Handbook — HVAC Systems and Equipment. Atlanta (GA): ASHRAE.
Contenido: Sistemas de refrigeración y aire acondicionado, compresores, protección de equipos de refrigeración. Referencia estándar del sector HVAC.

### SOURCE: IEEE_Std_3004_8_Applications
IEEE 3004.8 (ya referenciado en Atlas 2). Sección específica sobre protección por tipo de carga (bombas, compresores, ventiladores, transportadores).

### SOURCE: WEG_Motor_Application_Guide
WEG Equipamentos Elétricos S.A. Manual de Aplicación de Motores Eléctricos. Sección: Selección de motores por aplicación, protección por tipo de carga.
Descarga gratuita: weg.net (en español).

### SOURCE: Schneider_Resi9_Irama
Schneider Electric. Catálogo de productos de protección de motores Tesys. Rueil-Malmaison: Schneider Electric.
Contenido: Guardamotores, relés térmicos, relés electrónicos, monitores de red de la gama Tesys. Incluye tablas de coordinación Tipo 1 y Tipo 2.
Disponibilidad: Libre en se.com.

### SOURCE: Grundfos_Motor_Book
Grundfos. The Centrifugal Pump (Grundfos Motor Book). Bjerringbro: Grundfos.
Contenido: Referencia completa sobre bombas centrífugas, curvas de sistema, selección, operación, protección. Disponible en inglés, descarga gratuita.
URL: grundfos.com (buscar "The Centrifugal Pump").

### SOURCE: COVENIN_2238
FONDONORMA/COVENIN. COVENIN 2238: Tableros eléctricos de distribución y mando para aplicaciones industriales.
Contenido: Requisitos de tableros eléctricos industriales en Venezuela, incluyendo requisitos de protección de motores.

---

**FIN DEL ATLAS 3 — APLICACIONES: BOMBEO, REFRIGERACIÓN Y MÁQUINAS ROTATIVAS**
Proyecto ProtMotores | Versión 1.0 | Marzo 2026
Siguiente: Atlas 4 — Mercado y Diferenciación Venezuela
