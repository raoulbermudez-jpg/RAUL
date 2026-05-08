# Aplicaciones — Bombeo, refrigeración, ventiladores y transportadores

**Audiencia:** Vera, Orlan, Solenne y agentes que necesitan referencia operativa rápida sobre aplicación-protección.
**Origen:** integrado desde Atlas 3 legacy (marzo 2026), curado por Vera 2026-05-07. Tablas extraídas; texto operativo conservado.

> **Caveat:** las observaciones específicas sobre Venezuela (sequías, marcha en seco frecuente, instalaciones sin supervisión) son cualitativas, basadas en campo. Sin estadísticas oficiales publicables.

---

## 1. Tabla maestra — Selección de protección por aplicación

| Aplicación | Clase IEC | Monitor red | Relé tipo | PTC | Nivel protección |
|---|---|---|---|---|---|
| Bomba centrífuga superficial | 10 | ✓ obligatorio | Electrónico | No | Estándar |
| Bomba sumergible pozo profundo | 10 | ✓ obligatorio | Electrónico | ✓ | Premium |
| Bomba sumergible aguas residuales | 10 | ✓ obligatorio | Electrónico | No | Estándar |
| Compresor hermético A/C | 20 | ✓ obligatorio | Bimetálico\* | ✓\* | Estándar |
| Compresor semiermético refrigeración | 20 | ✓ obligatorio | Electrónico | ✓ | Premium |
| Compresor de aire pistón | 20 | ✓ obligatorio | Electrónico | No | Estándar |
| Compresor de aire tornillo | 10 | ✓ obligatorio | Electrónico | No | Estándar |
| Ventilador axial pequeño | 10 | Recomendado | Bimetálico | No | Básico |
| Ventilador centrífugo grande | 20-30 | ✓ obligatorio | Electrónico | No | Estándar |
| Transportador horizontal | 10-20 | Recomendado | Bimetálico | No | Básico |
| Transportador inclinado con carga | 20 | ✓ obligatorio | Electrónico | No | Estándar |
| Molino / Triturador | 30 | ✓ obligatorio | Electrónico | No | Estándar |
| Motor proceso continuo crítico | 20 | ✓ obligatorio | Electrónico | ✓ | Premium |

(\*) Compresores herméticos A/C típicamente incluyen protector interno (klixon) y a veces PTC. El relé externo es complemento.

---

## 2. Selección de clase IEC por tiempo de arranque

| Tiempo arranque medido | Clase recomendada | Margen seguridad |
|---|---|---|
| < 2s | Clase 10A | 20% |
| 2-4s | Clase 10 | 25% |
| 4-8s | Clase 10 o 20 | 25-30% |
| 8-15s | Clase 20 | 30% |
| 15-25s | Clase 30 | 30% |
| > 25s | Clase 30 + arrancador suave/VFD | Evaluar |

**Regla:** si el tiempo de arranque supera 25s con DOL, considerar arrancador suave o VFD para reducir el calor de arranque y proteger el motor.

---

## 3. Cable sumergible — sección por potencia y profundidad

**Criterio:** caída de tensión máxima admisible 3% de Vn.
- 220V → 6.6V máximo
- 440V → 13.2V máximo

| Potencia | Profundidad | Sección 220V | Sección 440V |
|---|---|---|---|
| 1 - 3 HP | 30 m | 2.5 mm² | 1.5 mm² |
| 1 - 3 HP | 60 m | 4 mm² | 2.5 mm² |
| 3 - 7.5 HP | 30 m | 4 mm² | 2.5 mm² |
| 3 - 7.5 HP | 60 m | 6 mm² | 4 mm² |
| 7.5 - 15 HP | 30 m | 6 mm² | 4 mm² |
| 7.5 - 15 HP | 60 m | 10 mm² | 6 mm² |
| 15 - 30 HP | 30 m | 10 mm² | 6 mm² |
| 15 - 30 HP | 60 m | 16 mm² | 10 mm² |

**Regla:** siempre calcular para la potencia y profundidad específicas. Usar cable especial sumergible (flexible, resistente a agua, cubierta especial).

> **Caveat Venezuela:** con la red CORPOELEC ya con subtensión (210-215V típico en sistemas 220V), una caída adicional en el cable deja al motor a 91% Vn. Este efecto acumulativo justifica calcular siempre con holgura en cable sumergible.

---

## 4. Patrones de falla por aplicación

### Bombas centrífugas superficiales

Perfil de par: cuadrático (T ∝ N²). Inercia baja-media. Fácil arranque.

**Fallas típicas:**

1. **Marcha en seco** — bomba sin agua en succión. Corriente BAJA (no sube). Relé sobrecarga NO detecta.
   - Protección: presostato baja presión en succión, sensor de caudal, o relé de baja corriente/potencia.

2. **Sobrecarga por exceso de caudal** — válvula descarga muy abierta. Corriente sube > In.
   - Protección: relé sobrecarga.

3. **Desequilibrio y falta de fase** — frecuente en CORPOELEC.
   - Protección: monitor de red obligatorio.

4. **Inundación del motor** — humedad degrada aislamiento.
   - Protección: detector de humedad (flotador nivel alto).

### Bombas sumergibles pozo profundo

Motor encapsulado IP68. Refrigeración por el agua bombeada. Sin ventilador externo.

**Fallas típicas:**

1. **Marcha en seco — la más crítica.** Sin agua, motor pierde refrigeración. T sube en minutos. La corriente puede no subir → relé sobrecarga NO protege.
   - **Protección obligatoria:** sonda de nivel en el pozo + termistor PTC en devanado.

2. **Arena y abrasivos** — desgaste impulsor y sellos. Sin efecto eléctrico hasta desgaste severo.
   - Detección: incremento gradual de corriente, reducción caudal.
   - Protección preventiva: monitoreo periódico + reemplazo programado.

3. **Caída de tensión por cable largo** — 50m con cable insuficiente puede causar 5-10V de caída.
   - Corrección: dimensionar cable correctamente (ver tabla §3) + protección de subtensión en tablero superficial.

4. **Desequilibrio en cable largo** — empalme deficiente o corrosión genera desequilibrio.
   - Protección: monitor de red + medición periódica de corrientes en las tres fases.

5. **Condensación al arrancar** — pozo seco + motor frío puede generar fuga a tierra.
   - Protección: relé diferencial (RCD/GFCI) en tablero superficial.

**Configuración recomendada (mínimo obligatorio):**
Guardamotor + Contactor + Relé electrónico con entrada PTC + Monitor de red + Sonda de nivel.

### Bombas sumergibles aguas residuales

Fluido agresivo, con sólidos. Impulsor tipo vórtex o semi-abierto. Arranques frecuentes por control de nivel.

**Fallas:**

1. **Atasco del impulsor** — material sólido bloquea. Stall (5-7 × In).
   - Protección: relé electrónico con función locked rotor (2-5s).

2. **Arranques frecuentes** — 10-30/hora en horas pico. Acumulación térmica.
   - Protección: relé electrónico con memoria térmica + anti-jogging. Ajustar flotadores para maximizar intervalo entre arranques.

3. **Operación sumergida sin agua** — durante mantenimiento.
   - Protección: flotador nivel mínimo.

### Compresores herméticos / semi-ermeticos de refrigeración

Motor y compresor en carcasa sellada. Refrigerante = refrigerante del motor.

**Fallas típicas:**

1. **Liquid slugging en arranque** — líquido refrigerante acumulado. Par de arranque muy alto. Riesgo stall o daño mecánico.
   - Protección: calentador de cárter (crankcase heater) + temporizador de retardo en arranque (15-30 min tras paro prolongado).

2. **Corte de fase** — el más destructivo. Compresor hermético no rebobinable: se reemplaza completo. Corriente alta + daño en minutos.
   - **Protección obligatoria:** monitor de red con falta de fase + relé secuencia.

3. **Alta temperatura de descarga** — refrigerante insuficiente o alta relación de compresión.
   - Protección: termostato klixon + PTC en devanado.

4. **Presión alta/baja anormal** — condensador sucio, T ambiente alta, ventilador fallido / sistema sin refrigerante.
   - Protección: presostatos en circuito de refrigerante (no en circuito eléctrico). Cortan circuito de control del contactor.

5. **Arranques frecuentes (ciclos cortos)** — termostato mal calibrado puede causar ciclos de 1-3 minutos. Acumulación térmica.
   - **Protección:** anti-short cycle timer (mínimo 3-5 min entre arranques).

6. **Inversión de fase** — compresor pistón girando al revés no comprime. Daño mecánico rápido.
   - Protección: monitor de red con detección de secuencia.

**Configuración obligatoria:**
Guardamotor + Contactor AC-3 + Relé electrónico (o bimetálico de calidad) + Monitor de red (falta fase + secuencia + subtensión) + Anti-short cycle timer.

### Compresores de aire (pistón / tornillo / centrífugo)

**Fallas:**

1. **Arranque con presión residual** (compresores pistón) — sin descarga del cabezal. Alto par de arranque.
   - Protección mecánica: válvula descarga (unloader) + protección eléctrica que tolere Icc más larga.

2. **Sobrecalentamiento por ventilación insuficiente** — salas de compresores 45-55°C en Venezuela.
   - Protección: PTC + buena ventilación.

3. **Correa rota** (transmisión por fajas) — motor gira sin carga, corriente baja. Compresor no comprime → motor en vacío indefinidamente.
   - Protección: sensor de presión que verifique producción de presión. Si no sube en X minutos → alarma.

### Ventiladores axiales y centrífugos

Perfil de par: cuadrático. Arranque con carga mínima. Inercia variable.

**Fallas:**

1. **Inversión de sentido de giro** — caudal casi nulo. Motor no se daña pero la aplicación falla.
   - Detección: sensor presión diferencial o termómetro en espacio ventilado. Verificar sentido en comisionamiento.

2. **Aspa trabada o desequilibrada** — stall del motor o vibración severa.
   - Protección: relé sobrecarga + detector vibración (industriales grandes) + locked rotor.

3. **Polvo en motor** — extracción de polvo o gases con partículas. Obstrucción de ventilación.
   - Protección: motor IP54-IP55 + PTC + programa de limpieza.

4. **Arranques frecuentes en gran inercia** — 15-30s para acelerar. Acumulación de calor en rotor.
   - Protección: relé electrónico con memoria + Clase 30. Considerar arrancador suave.

### Transportadores de banda

Perfil de par variable: horizontal vacío bajo / inclinado con carga alto / arranque cargado muy alto.

**Fallas:**

1. **Banda atascada (stall)** — material atasca. Corriente 5-7 × In sostenida.
   - Protección: relé electrónico con locked rotor (1-5s) + cordón de parada de emergencia (norma seguridad).

2. **Sobrecarga por exceso material** — más material del diseñado.
   - Protección: relé sobrecarga ajustado.

3. **Banda rota o deslizante** — motor gira sin carga. Corriente baja.
   - Protección: sensor velocidad de banda (tacómetro/encoder) que detecte discrepancia.

4. **Arranque con carga inclinada** — par estático muy alto.
   - Solución: motor FS=1.15 o 1.25, diseño NEMA C; en grandes, arrancador suave con rampa de par.

5. **Frenado brusco con freno mecánico** — carga inclinada puede retroceder al parar.
   - Protección mecánica: trinquete (backstop) o freno electromagnético.

### Aplicaciones especiales

**Bombas de desplazamiento positivo:** par constante. Riesgo si válvula descarga cerrada → presión sube hasta el límite mecánico.
- Protección: válvula de alivio de presión (mecánica) + relé de sobrecarga (motor en stall).

**Molinos y trituradores:** par alto en arranque, alta inercia.
- Protección: Clase 30 + locked rotor + sensor vibración.

**Agitadores y mezcladores:** par constante. Riesgo por aumento de viscosidad (frío, cambio producto).
- Protección: relé sobrecarga + monitor de red.

**Bombas de calor / chillers:** análogos a compresores refrigeración. Premium recomendado.

---

## 5. Hallazgos clave

> Cualquier afirmación cuantitativa sobre Venezuela (sequías, daño de motores en bombeo) es estimación cualitativa de campo, no estadística publicable.

- **Marcha en seco es la causa más frecuente de daño de motores de bombeo en Venezuela** (sequías, cortes de agua, niveles bajos en cisternas). NO detectada por relé sobrecarga estándar (corriente baja, no sube). La protección correcta es sensor de presión de succión o nivel de cisterna.
- **Compresores herméticos NO se rebobinan** — se reemplazan completos. Costo 3-10× motor estándar equivalente. Justifica inversión en protección superior.
- **Ventilador del motor a baja velocidad:** caudal cuadrático con velocidad. A 50% velocidad (VFD), refrigeración 25% nominal. Motores INVERTER-DUTY o ventilación forzada externa para operación continua a baja velocidad.
- **Arrancador suave / VFD NO reemplaza la protección externa.** Sus protecciones internas protegen al propio dispositivo, no al motor exhaustivamente. Mantener fusibles + relé sobrecarga + monitor de red.
- **Tiempo mínimo entre arranques crítico para refrigeración.** Termostatos defectuosos pueden generar ciclos de 30s on/30s off. Anti-short cycle timer ($10-20 USD) previene falla de compresor ($500-3000 USD).
- **Cable sumergible subestimado en Venezuela.** Subtensión CORPOELEC + caída en cable insuficiente = motor a 91% Vn. Calcular siempre con holgura.

---

**Última actualización:** 2026-05-07. Versión 1.0, integración inicial.
