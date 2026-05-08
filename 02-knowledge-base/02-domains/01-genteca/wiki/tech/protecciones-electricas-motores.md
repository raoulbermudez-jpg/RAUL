# Protecciones eléctricas de motores trifásicos — Tecnologías y selección

**Audiencia:** Vera, Orlan, Solenne y agentes que necesitan contexto técnico sobre protección de motores antes de seleccionar productos o redactar contenido.
**Origen:** integrado desde Atlas 2 legacy (marzo 2026), curado por Vera 2026-05-07.
**Normas de referencia:** IEC 60947-4-1, IEC 60947-2, IEC 60947-5-1, NEMA ICS 2, IEEE Std 3004.8, COVENIN 159.

> **Caveat:** los rangos de corriente de cortocircuito (Icc) por punto de instalación son estimaciones para tableros venezolanos típicos. Cualquier proyecto formal requiere cálculo de Icc específico para la instalación.

---

## 1. Conceptos fundamentales

### Niveles de protección

| Nivel | Función | Tiempo actuación |
|---|---|---|
| 1 | Cortocircuito (fusibles, interruptores) | milisegundos |
| 2 | Sobrecarga (relés térmicos o electrónicos) | segundos a minutos |
| 3 | Condiciones de red (monitor de red: desequilibrio, falta de fase, sub/sobre-tensión, secuencia) | 0.1-5 segundos |
| 4 | Proceso (sensores externos: presión, caudal, temperatura proceso, vibración) | variable |

**Coordinación correcta:**
- Ante cortocircuito → dispara solo Nivel 1 (rápido, local).
- Ante sobrecarga → dispara solo Nivel 2 (curva I²t).
- Ante condición de red → dispara Nivel 3 sin interferir con 1 o 2.

Falta de coordinación = disparos en elemento equivocado o daño antes de que actúe la protección correcta.

### Corriente de cortocircuito prospéctica (Icc)

Corriente máxima si ocurriera cortocircuito trifásico franco en el punto.

**Cálculo simplificado:** Icc ≈ V / (√3 × Z_total)

Valores típicos en instalaciones venezolanas (estimación):

| Punto | Icc estimada |
|---|---|
| Tablero principal alimentado desde transformador 300 kVA | 8-12 kA |
| Tablero secundario (con cable de alimentación) | 3-8 kA |
| Bornes del motor (con cable largo) | 1-5 kA |

**Crítico:** la capacidad de ruptura (breaking capacity) del dispositivo de protección debe ser ≥ Icc del punto. Error frecuente en instalaciones viejas: fusibles de bajo breaking capacity (1-3 kA) en tableros que hoy tienen Icc mucho mayor por crecimiento de la red → fusible explota sin interrumpir falla.

### Curva de disparo tiempo-corriente

Representación gráfica de la relación entre corriente y tiempo de operación del dispositivo. Escala logarítmica en ambos ejes.

Componentes para protección de motor:
- Zona de no-disparo (operación normal incluyendo arranque)
- Zona de disparo (protección actúa)
- Zona de daño del motor (curva del fabricante) — la curva de protección debe estar por DEBAJO

**Zona de arranque:** 5-7 × In durante 2-15s. Curva de disparo debe pasar por encima.
**Zona de stall:** misma corriente, tiempo indefinido. Curva debe interceptar antes del tiempo de daño térmico.

### Clases de disparo IEC 60947-4-1

Tiempo máximo de disparo desde frío con 7.2 × In:

| Clase | Tiempo | Aplicación |
|---|---|---|
| 10A | < 2s | Motores con arranque muy corto |
| 10 | 2-10s | Cargas baja inercia (bombas, ventiladores) |
| **20** (más común Venezuela) | 10-20s | Compresores, transportadores |
| 30 | 20-30s | Molinos, prensas, centrífugas alta masa |

**Criterio:** elegir la clase más baja posible que permita completar arranque sin disparo intempestivo. Clase 10 es mejor que Clase 30 porque actúa más rápido ante stall o sobrecarga.

> **Nota:** Vera ha observado que Clase 20 es frecuentemente especificada como "default" en Venezuela. Esto es **incorrecto para bombas centrífugas y ventiladores axiales** (inercia baja, arranque corto 2-5s). Para estas aplicaciones usar Clase 10.

### Coordinación Tipo 1 vs Tipo 2 (IEC 60947-4-1)

**Tipo 1 — básica:**
Tras cortocircuito, el conjunto puede no estar en condición de operar. Posible reemplazo de relé y contactor.
- Ventaja: menor costo inicial.
- Uso: aplicaciones no críticas, paradas prolongadas aceptables.

**Tipo 2 — mejorada:**
Tras cortocircuito, el conjunto opera sin reemplazo (excepto fusibles). Contactor y relé no se dañan.
- Ventaja: rearranque rápido sin mantenimiento mayor.
- Uso: procesos críticos (bombas continuas, refrigeración industrial, ventilación zonas calientes).
- Costo: 15-25% mayor que Tipo 1 sobre el conjunto.

**Recomendación Venezuela:** especificar Tipo 2 en todas las instalaciones críticas. El diferencial de costo es mínimo vs costo de parada de proceso.

---

## 2. Tecnologías de protección

### Relé térmico bimetálico

Dispositivo electromecánico que dispara mediante deflexión de láminas bimetálicas calentadas por la corriente.

**Funciones incluidas:**
- ✓ Sobrecarga (curva I²t)
- ✓ Compensación de temperatura ambiente (parcial)
- ✓ Detección falta de fase (en modelos con diseño asimétrico)
- ✓ Reset manual o automático
- ✓ Contactos auxiliares NC + NO

**Funciones NO incluidas:**
- ✗ Desequilibrio de fases (solo detecta pérdida total)
- ✗ Sub/sobre-tensión
- ✗ Secuencia de fases
- ✗ Memoria térmica precisa (bimetálico se enfría sin corriente)
- ✗ Función locked rotor dedicada
- ✗ Registro de eventos
- ✗ Comunicación

**Parámetros:**
- Rango de ajuste: ±20-30% del valor central de la referencia
- Clases disponibles: 10 y 20 más comunes; algunos 10A
- Precisión: ±10-15% del punto de disparo

**Pros:** bajo costo, sin alimentación auxiliar, simple instalación, alta confiabilidad mecánica, amplia disponibilidad Venezuela.

**Contras:** precisión moderada, temperatura ambiente afecta disparo, no detecta desequilibrio (solo pérdida total de fase), tiempo de disparo en stall puede ser demasiado largo para motores pequeños, sin memoria térmica real → puede no proteger correctamente arranques sucesivos.

**Aplicación:** motores uso general hasta ~75 kW, no críticos, presupuesto limitado.

### Relé electrónico de sobrecarga

Estado sólido. Mide corrientes trifásicas, modela matemáticamente la temperatura del motor, dispara cuando el modelo predice temperatura excesiva.

**Funciones estándar (modelos básicos a intermedios):**
- ✓ Sobrecarga (modelo térmico I²t con memoria)
- ✓ Falta de fase (<1s)
- ✓ Desequilibrio (umbral ajustable)
- ✓ Memoria térmica real (modelo continúa con motor parado)
- ✓ Locked rotor / stall (1-5s)
- ✓ Autoprotección
- ✓ Reset automático con temporizador o manual
- ✓ Clase ajustable (10/20/30 en el mismo relé)
- ✓ Contactos auxiliares múltiples

**Funciones avanzadas (modelos superiores):**
- ✓ Sub/sobre-tensión
- ✓ Secuencia de fases
- ✓ Entrada PTC externo
- ✓ Contador de arranques
- ✓ Registro últimas N fallas con causa
- ✓ Comunicación Modbus RTU / PROFIBUS / Ethernet
- ✓ Display local
- ✓ Anti-jogging

**Parámetros:**
- Precisión: ±2-5% (vs ±10-15% bimetálico)
- Requiere alimentación auxiliar (24VDC, 110/220VAC)
- Costo: 2-5× relé térmico equivalente

**Aplicación:** motores proceso crítico, arranques frecuentes, donde se requiere diagnóstico, redes con desequilibrio conocido, integración SCADA.

### Monitor de red

Supervisa parámetros de la red (V, secuencia, desequilibrio, frecuencia) y actúa sobre el circuito de control.

**Parámetros supervisados (según modelo):**
- Sub/sobre-tensión (umbral ajustable)
- Secuencia de fases (RST vs RTS), disparo instantáneo
- Falta de fase (<500ms típico)
- Desequilibrio de tensión (umbral ajustable)
- Frecuencia (algunos modelos)
- Temporización de rearranque

**Pros:**
- Protege contra las causas de falla más comunes en Venezuela (falta de fase, desequilibrio, subtensión)
- Bajo costo (similar a relé térmico básico)
- No requiere transformadores de corriente
- Función de retardo de rearranque

**Contras:**
- No protege contra sobrecarga (no mide corriente)
- **Debe combinarse siempre con relé de sobrecarga**

**Aplicación recomendada Venezuela:** complemento obligatorio del relé de sobrecarga en cualquier motor de proceso. Especialmente crítico en bombas continuas, compresores de refrigeración, motores en zonas con red inestable.

### Guardamotor magnetotérmico (MPCB)

Dispositivo combinado: interruptor de potencia + protección magnetotérmica de sobrecarga + protección electromagnética de cortocircuito.

**Norma:** IEC 60947-2 (interruptor) + IEC 60947-4-1 (arrancador).

**Pros vs combinación fusible+contactor+relé térmico:**
- Menos espacio en tablero
- Sin necesidad de fusibles de repuesto
- Apertura manual integrada (función seccionador)
- Menor costo total en potencias medias
- Coordinación Tipo 1 o Tipo 2 garantizada por fabricante

**Contras:**
- No detecta falta de fase en todos los modelos
- No detecta desequilibrio (requiere monitor de red)
- Rango de ajuste más limitado
- Capacidad de ruptura limitada en modelos económicos (3-10 kA típico)

**Rango aplicación:** motores 0.1 kW a 45-75 kW según fabricante.

### Termistor PTC + relé amplificador

Termistores PTC embebidos en devanados del motor + relé que interpreta resistencia.

**Principio:** PTC tiene resistencia muy baja (100-1000 Ω) a T normal y se dispara abruptamente (R → ∞) al alcanzar la temperatura nominal.

**Configuración:** 3 PTC en serie (uno por bobina) → relé amplificador → contacto de salida.

**Temperaturas estándar:**

| Tn PTC | Aplicación |
|---|---|
| 110°C | Clase A/B (disparo antes del límite) |
| 130°C | Clase B (disparo en el límite) |
| 150°C | Clase F (disparo conservador) |
| 160°C | Clase F (disparo en el límite) |
| 180°C | Clase H |

**Pros:**
- Mide temperatura REAL (no modelada)
- No afectado por T ambiente, ciclo de carga, velocidad
- Detecta condiciones que los relés de corriente no detectan: motor parado en ambiente caliente, motor con ventilación obstruida, **motor sumergible operando en seco**
- Bajo costo

**Contras:**
- Requiere que el motor tenga PTC instalados (de fábrica o durante rebobinado)
- Sistema binario (dispara o no — no T en tiempo real)

**Aplicación crítica:** bombas sumergibles (única protección que detecta marcha en seco efectivamente), motores en ambientes calientes, motores con arranque frecuente.

### Relé diferencial de motor

Compara corrientes de entrada y salida (o suma de las tres fases). Detecta corrientes de falla internas.

**Funciones:**
- ✓ Cortocircuito entre fases en devanado
- ✓ Cortocircuito fase-tierra (fuga a tierra)
- ✓ Cortocircuito entre espiras (alta sensibilidad)

**Limitaciones:**
- Alto costo (motores >75-100 kW o críticos)
- TCs de alta precisión (clase 5P)
- Configuración compleja
- No común en Venezuela fuera de plantas industriales mayores

---

## 3. Mecanismos de detección

### Detección de sobrecarga

**Bimetálico:**
Calor acumulado ∝ I² × t. La lámina bimetálica integra físicamente el calor (condensador térmico analógico). La curva I²t aproxima la curva de daño térmico para sobrecarga estable.
**Limitación:** pierde memoria al enfriarse. Tras un arranque, si el motor se detiene y el bimetálico se enfría, el siguiente arranque parte de cero — pero el rotor del motor retiene calor por más tiempo.

**Electrónico:**
Modelo digital: θ_motor(t) = θ_ambiente + K × I².
La memoria térmica se mantiene incluso con I = 0. El modelo puede incluir:
- Constante térmica del estátor τ_s
- Constante térmica del rotor τ_r (diferente, generalmente mayor)
- Factor de derating por clase de aislamiento
- Factor de corrección por desequilibrio

### Detección de falta de fase

| Tecnología | Tiempo detección |
|---|---|
| Bimetálico trifásico (asimétrico) | 10-60s |
| Relé electrónico | <1s |
| Monitor de red | 100-500ms |

**Mejor práctica:** combinar relé electrónico de sobrecarga + monitor de red. El monitor detecta la falta ANTES de que las corrientes del motor suban (al detectar la falta de tensión en la red).

### Detección de desequilibrio

**Voltimétrico (monitor de red):**
%D_V = (máx |V_Li - Vprom|) / Vprom × 100%
- Umbral típico: 2-10%
- Recomendación Venezuela: 3-5% (ajuste <2% genera disparos por variaciones normales; >8% no protege)

**Amperimétrico (relé electrónico):**
%D_I = (máx |I_Li - Iprom|) / Iprom × 100%
- Umbral típico: 10-30%
- Mayor numéricamente porque desequilibrio I es 6-10× mayor que el de V

### Detección de locked rotor

**Distinción crítica:**
- Arranque normal: I = 5-7 × In durante 2-15s → cae a In
- Stall: I = 5-7 × In indefinidamente

La protección no puede distinguir SOLO por magnitud (es la misma). Necesita elemento temporal.

**Función locked rotor (relé electrónico):**
1. Mide corriente de arranque
2. Activa temporizador (Tiempo de Arranque ajustable, típico 2-30s)
3. Si la corriente no baja al valor de plena carga al vencer el temporizador → dispara (1-4s)

**Ajuste correcto:** Tiempo arranque = t_aceleración real × 1.25.

> **Error frecuente:** configurar tiempo de arranque demasiado largo (>30s) para evitar disparos → motor sin protección efectiva en stall real.

### Sobre-tensión transitoria (no función de relé estándar)

Picos de microsegundos a milisegundos, 3-10 × Vn. Causados por maniobras de red, descargas atmosféricas, arranque/parada de grandes cargas, resonancia con VFD.

**Protección:** varistores (MOV) o supresores (SPD) en acometida o bornes del motor. Capa complementaria crítica en Venezuela.

---

## 4. Comparativa rápida bimetálico vs electrónico

| Criterio | Bimetálico | Electrónico |
|---|---|---|
| Costo inicial | ★★★★★ bajo | ★★★ medio-alto |
| Precisión disparo | ±10-15% | ±2-5% |
| Memoria térmica real | ✗ parcial | ✓ completa |
| Detección falta de fase | ✓ lenta (10-60s) | ✓ rápida (<1s) |
| Detección desequilibrio | ✗ | ✓ ajustable |
| Función locked rotor | ✗ básica vía I²t | ✓ dedicada |
| Clase ajustable | Fija | 10/20/30 seleccionable |
| Diagnóstico de fallas | ✗ | ✓ registro eventos |
| Comunicación | ✗ | ✓ Modbus/Profibus |
| Alimentación auxiliar | No requiere | Requiere |
| Arranque frecuente | ★★ no apto | ★★★★★ óptimo |
| Sumergible (con PTC) | ★★ | ★★★★ |
| Disponibilidad Venezuela | ★★★★★ | ★★★ |

**Recomendación:**
- Motores proceso crítico → electrónico
- Motores uso general no crítico → bimetálico + monitor de red

---

## 5. Niveles de protección por criticidad

### Nivel básico (motores no críticos, fácil reposición)
Fusible + Contactor AC-3 + Relé térmico bimetálico
- Protege: sobrecarga (básica) + cortocircuito
- No protege: desequilibrio, falta de fase (adecuada), sub/sobretensión
- Costo relativo: 1.0×

### Nivel estándar (motores de proceso, parada costosa)
Guardamotor MPCB + Contactor AC-3 + Relé electrónico de sobrecarga + Monitor de red
- Protege: todo lo anterior + falta de fase + desequilibrio + sub/sobretensión + secuencia
- No protege: temperatura real devanado, fallas internas bobinado
- Costo relativo: 2.5-3.5×

### Nivel premium (proceso continuo, alto costo de parada)
Interruptor motor + Contactor AC-3 + Relé electrónico avanzado + Monitor de red + Termistor PTC + Sensor vibración
- Protege: todo + temperatura real + vibración + diagnóstico completo + comunicación SCADA
- Costo relativo: 5-8×

> **Recomendación Venezuela:** para bombas de agua potable, refrigeración industrial y ventilación crítica, mínimo Nivel Estándar. El costo de rebobinado o reposición del motor supera varias veces el diferencial.

---

## 6. Hallazgos clave

> Caveat: los datos cualitativos sobre Venezuela (calidad de red CORPOELEC, prácticas de instalación) se basan en observación de campo y reportes de mantenimiento; no hay registros oficiales accesibles que permitan cuantificación estadística rigurosa.

- **Monitor de red obligatorio Venezuela.** Con un costo similar a un relé térmico básico, protege contra las tres causas más frecuentes (falta de fase, desequilibrio, subtensión). Todo motor de proceso debería tener un monitor de red.
- **Error común estrella-triángulo:** ajustar el relé térmico para In de línea cuando la conexión se hace a los devanados (configuración Δ permanente). Debe ajustarse para In/√3.
- **Clase 20 default es incorrecto** para bombas centrífugas y ventiladores axiales (inercia baja, arranque corto 2-5s). Para estas aplicaciones usar Clase 10.
- **Tipo 2 se paga sola** en el primer evento de cortocircuito en motores críticos. Diferencial 15-25%; ahorro evita reemplazo de contactor + relé (50-80% del conjunto).
- **Tiempo de disparo real vs nominal:** los tiempos de clase IEC son DESDE FRÍO. Si el relé está caliente, el tiempo real es significativamente menor. Compensación parcial en bimetálicos; mejor en electrónicos.
- **PTC único para sumergibles.** Para detectar marcha en seco, el PTC es la única tecnología efectiva. La corriente baja, no sube, cuando la bomba opera sin agua.
- **Capacidad de ruptura subestimada en tableros viejos.** Ante ampliación de instalaciones o cambio de transformador, recalcular Icc y verificar dispositivos.

---

**Última actualización:** 2026-05-07. Versión 1.0, integración inicial.
