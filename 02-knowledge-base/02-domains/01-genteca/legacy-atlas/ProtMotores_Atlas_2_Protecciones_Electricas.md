# ATLAS 2 — PROTECCIONES ELÉCTRICAS DE MOTORES TRIFÁSICOS

**Base de Conocimiento:** Protecciones Eléctricas para Motores Trifásicos
**Proyecto:** ProtMotores | Carril 2 — Técnico/Industrial
**Mercado:** Venezuela | Normas: COVENIN + IEC 60947 + NEMA MG1
**Versión:** 1.0 | Marzo 2026
**Prefijos RAG:** INGLÉS | Contenido: ESPAÑOL

---

## SECCIÓN 1 — CONCEPTOS FUNDAMENTALES DE PROTECCIÓN

### CONCEPT: Sistema_de_Proteccion_Motor
Definición: Conjunto coordinado de dispositivos cuyo objetivo es detectar condiciones de operación anormales en un motor trifásico y en su circuito de alimentación, y responder mediante apertura del circuito (disparo), señalización de alarma, o registro del evento, antes de que ocurra un daño irreversible al motor, a la carga, o al sistema eléctrico.
Niveles de protección:
- **Nivel 1 — Protección contra cortocircuito:** Dispositivos de apertura rápida (fusibles, interruptores automáticos). Tiempos de actuación: milisegundos.
- **Nivel 2 — Protección contra sobrecarga:** Relés térmicos o electrónicos. Tiempos de actuación: segundos a minutos según nivel de sobrecarga.
- **Nivel 3 — Protección contra condiciones de red:** Monitor de red (desequilibrio, falta de fase, sub/sobre-tensión, secuencia). Tiempos: 0.1-5 segundos.
- **Nivel 4 — Protección de proceso:** Sensores externos (presión, caudal, temperatura de proceso, vibración). Integración vía controlador o relé multipropósito.
Concepto de coordinación: Los tres primeros niveles deben coordinarse para que:
a) Ante cortocircuito → dispara solo el Nivel 1 (rápido, local al circuito).
b) Ante sobrecarga → dispara solo el Nivel 2 (curva I²t).
c) Ante condición de red → dispara el Nivel 3 sin interferir con Nivel 1/2.
La falta de coordinación provoca disparos en el elemento equivocado o daño al equipo antes de que actúe la protección correcta.

### CONCEPT: Corriente_de_Cortocircuito_Prospectica
Definición: Corriente máxima que fluiría en un punto del circuito si ocurriera un cortocircuito trifásico franco (resistencia de falla = cero) en ese punto.
Símbolo: Icc o Isc (short-circuit current).
Importancia para selección de protecciones: Todo dispositivo de protección (fusible, interruptor, relé) debe tener capacidad de ruptura (breaking capacity) mayor a la Icc prospéctica del punto donde se instala.
Cálculo simplificado: Icc ≈ V / (√3 × Z_total)
Donde Z_total = impedancia total del circuito desde la fuente hasta el punto.
Valores típicos Venezuela (aproximados):
- En tablero principal alimentado desde transformador 300 kVA: Icc ≈ 8-12 kA
- En tablero secundario (con cable de alimentación): Icc ≈ 3-8 kA
- En bornes del motor (con cable largo): Icc ≈ 1-5 kA
Nota práctica: Los fusibles y contactores especificados para un circuito de motor deben tener capacidad de ruptura ≥ Icc del punto. Error frecuente en instalaciones venezolanas: usar fusibles de bajo breaking capacity (1-3 kA) en tableros con Icc alta → explosión del fusible sin interrumpir la falla.

### CONCEPT: Curva_de_Disparo_Tiempo_Corriente
Definición: Representación gráfica de la relación entre la corriente que fluye por un dispositivo de protección y el tiempo máximo que tarda en operar (disparar o fundir) para esa corriente.
Formato estándar: Escala logarítmica en ambos ejes. Eje X = múltiplos de corriente nominal (I/In). Eje Y = tiempo (segundos).
Componentes de la curva para protección de motor:
- Zona de no-disparo: Por debajo de la curva → protección no actúa (operación normal incluyendo arranque).
- Zona de disparo: Por encima de la curva → protección actúa.
- Zona de daño del motor: Curva de daño térmico del motor (proporcionada por el fabricante del motor). La curva de protección debe estar POR DEBAJO de la curva de daño del motor para garantizar protección efectiva.
Zona de arranque: Entre 5-7 × In durante 2-15 segundos. La curva de disparo debe pasar por encima de este punto (no disparar en arranque normal).
Zona de stall: Igual corriente que arranque pero tiempo indefinido. La curva de disparo debe interceptar esta zona en tiempo menor al tiempo de daño del motor en stall.

### CONCEPT: Clases_de_Disparo_IEC
Definición: IEC 60947-4-1 clasifica los relés de sobrecarga según el tiempo máximo de disparo desde frío con 7.2 × In (triplo de la corriente de arranque típica 2.4× × 3 = 7.2×).
Clases y tiempos de disparo (desde frío, con 7.2 × Ie):
- **Clase 10A:** < 2 segundos. Motores con arranque muy corto.
- **Clase 10:** 2 - 10 segundos. Cargas de baja inercia (bombas, ventiladores).
- **Clase 20:** 10 - 20 segundos. Cargas de inercia media (compresores, algunos transportadores). LA MÁS COMÚN en Venezuela.
- **Clase 30:** 20 - 30 segundos. Cargas de alta inercia (molinos, prensas, centrífugas de alta masa).
Selección de clase: Elegir la clase más baja posible que permita completar el arranque sin disparo intempestivo. Clase 10 es mejor que Clase 30 porque actúa más rápido ante stall o sobrecarga.
Nota: El tiempo de disparo con corriente de sobrecarga (1.2-1.5 × In) es mucho mayor que el de la definición de clase. La Clase 20 puede tardar varios minutos en disparar con 1.2 × In. Esto es normal e intencional.

### CONCEPT: Coordinacion_Tipo_1_y_Tipo_2
Definición: IEC 60947-4-1 define dos tipos de coordinación entre protección contra cortocircuito (fusible o interruptor) y relé de sobrecarga + contactor:

**TIPO 1 — Coordinación básica:**
Después de un cortocircuito, el conjunto puede no estar en condición de operar y puede requerir inspección y posible reemplazo de piezas. El usuario acepta que puede haber daño en el relé o el contactor.
Ventaja: Menor costo inicial (fusibles más económicos, contactores más pequeños).
Uso: Aplicaciones no críticas donde la parada prolongada es aceptable.

**TIPO 2 — Coordinación mejorada:**
Después de un cortocircuito, el conjunto debe poder operar sin reemplazo de piezas (excepto posible sustitución de fusibles). El contactor y el relé no deben dañarse.
Ventaja: Rearranque rápido después de la falla sin mantenimiento mayor.
Uso: Aplicaciones críticas de proceso (bombas de proceso continuo, compresores de refrigeración, motores de ventilación en zonas calientes).
Costo: Mayor → fusibles de mayor breaking capacity, contactores más robustos.

Nota Venezuela: En instalaciones críticas (bombeo de agua potable, refrigeración industrial, etc.) se debe especificar siempre Tipo 2. El costo diferencial es mínimo vs el costo de parada de proceso.

---

## SECCIÓN 2 — TECNOLOGÍAS DE PROTECCIÓN: ENTRADAS DETALLADAS

### TECH_PRODUCT: Rele_Termico_Bimetalico
Descripción: Dispositivo electromecánico de protección contra sobrecarga que opera mediante el principio de deflexión de láminas bimetálicas calentadas por la corriente del motor (directamente o a través de transformadores de corriente integrados).
Principio de operación: La corriente calienta las láminas bimetálicas. Cada lámina está formada por dos metales con diferente coeficiente de dilatación térmica. Al calentarse, la lámina se curva. Cuando la curvatura alcanza el umbral de ajuste, acciona un mecanismo de disparo que abre el circuito de control (bobina del contactor).
Funciones estándar incluidas:
- ✓ Protección de sobrecarga (curva I²t)
- ✓ Compensación de temperatura ambiente (ajuste automático)
- ✓ Detección de falta de fase (en modelos trifásicos con diseño asimétrico)
- ✓ Reset manual o automático
- ✓ Contacto auxiliar de señalización (normalmente cerrado NC + normalmente abierto NO)
Funciones NO incluidas en relé térmico estándar:
- ✗ Protección de desequilibrio de fases (solo detecta pérdida total de fase)
- ✗ Protección de sub/sobre-tensión
- ✗ Protección de secuencia de fases
- ✗ Memoria térmica precisa (el bimetálico se enfría cuando no hay corriente)
- ✗ Función locked rotor dedicada (tiempo de disparo en stall puede ser largo)
- ✗ Registro de eventos
- ✗ Comunicación
Rango de ajuste: Típicamente ±20-30% del valor central de la referencia. Ejemplo: Referencia 25 A → rango ajustable 18-32 A aproximado.
Clases IEC disponibles: Clase 10 y Clase 20 son las más comunes. Algunos modelos ofrecen Clase 10A.
Ventajas:
- Bajo costo (el dispositivo de protección más económico para motores)
- Sin necesidad de alimentación auxiliar
- Simple instalación y ajuste
- Alta confiabilidad mecánica
- Amplia disponibilidad en Venezuela
Limitaciones:
- Precisión moderada (±10-15% del punto de disparo)
- La temperatura ambiente afecta el disparo (compensación parcial)
- No detecta desequilibrio por debajo de la pérdida total de fase
- Tiempo de disparo en stall puede ser demasiado largo para motores pequeños
- Sin memoria térmica real → puede no proteger correctamente en arranques frecuentes sucesivos
Aplicaciones típicas: Motores de uso general hasta ~75 kW, aplicaciones no críticas de proceso, cuando el presupuesto es limitado.
Selección: Elegir referencia cuyo rango de ajuste cubra In del motor. Ajuste final: dial al valor de In exacto de la placa del motor. Si motor tiene FS=1.15: ajustar a 1.15 × In para aprovechar el factor.

### TECH_PRODUCT: Rele_Electronico_Sobrecarga
Descripción: Dispositivo de estado sólido que mide las corrientes de las tres fases mediante transformadores de corriente integrados o externos, modela matemáticamente la temperatura del motor mediante algoritmos térmicos, y dispara el circuito de control cuando el modelo predice que la temperatura del motor superará el límite térmico.
Principio de operación: Medición digital de I_L1, I_L2, I_L3 → cálculo del modelo térmico → comparación con límite ajustado → disparo o alarma.
Funciones estándar (modelos básicos a intermedios):
- ✓ Protección de sobrecarga (modelo térmico I² × t con memoria térmica)
- ✓ Protección de falta de fase (detección en < 1 segundo)
- ✓ Protección de desequilibrio de fases (umbral ajustable)
- ✓ Memoria térmica real (el modelo sigue corriendo cuando no hay corriente)
- ✓ Función locked rotor / stall (disparo en 1-5 segundos)
- ✓ Autoprotección (se bloquea si la temperatura del modelo alcanza el límite)
- ✓ Reset automático con temporizador ajustable o reset manual
- ✓ Clase de disparo seleccionable (10/20/30 en el mismo relé)
- ✓ Contactos auxiliares múltiples (alarma + disparo)
Funciones avanzadas (modelos superiores):
- ✓ Protección de sub/sobre-tensión
- ✓ Protección de secuencia de fases
- ✓ Entrada para termistor PTC externo (temperatura real del devanado)
- ✓ Contador de arranques
- ✓ Registro de últimas N fallas con causa
- ✓ Comunicación Modbus RTU / PROFIBUS / Ethernet
- ✓ Display local con valores en tiempo real (I, V, potencia, temperatura modelo)
- ✓ Función anti-jogging (bloqueo si hay demasiados arranques en poco tiempo)
Ventajas vs relé térmico bimetálico:
- Mayor precisión (±2-5% típico vs ±10-15% del bimetálico)
- Modelo térmico con memoria → protección correcta en arranques frecuentes
- Detección de desequilibrio (no solo pérdida total de fase)
- Función locked rotor rápida → mayor protección en stall
- Clase ajustable en el mismo relé
- Diagnóstico de fallas → menos tiempo de parada en mantenimiento
- Comunicación → integración con SCADA, automatización
Limitaciones:
- Requiere alimentación auxiliar (24VDC, 110VAC o 220VAC según modelo)
- Mayor costo inicial (2-5× vs relé térmico equivalente)
- Requiere personal con mayor nivel técnico para configuración
- Disponibilidad en Venezuela más limitada que relés bimetálicos
Aplicaciones: Motores de proceso crítico, aplicaciones con arranques frecuentes, donde se requiere diagnóstico, donde hay desequilibrio de red conocido, integración con sistemas de automatización.

### TECH_PRODUCT: Monitor_de_Red_Motor
Descripción: Dispositivo que supervisa permanentemente los parámetros de la red eléctrica de alimentación del motor (tensión, secuencia, desequilibrio, frecuencia) y actúa sobre el circuito de control cuando detecta condiciones fuera de rango.
También denominado: Relé de control de fase, guardamotor de red, monitor de tensión trifásico, relé de secuencia y falta de fases.
Parámetros supervisados (según modelo):
- Tensión de red: Mínima (subtensión) y máxima (sobretensión) — umbral ajustable.
- Secuencia de fases: Correcta (RST) vs incorrecta (RTS). Disparo instantáneo.
- Falta de fase: Ausencia de cualquiera de las tres fases. Disparo rápido.
- Desequilibrio de tensión: Diferencia porcentual entre fases — umbral ajustable.
- Frecuencia: Variación sobre/bajo frecuencia nominal (algunos modelos).
- Temporización: Retardo a la conexión (función de reinicio con retardo) — evita rearranques inmediatos después de un corte de red.
Funcionamiento: El monitor energiza su relé interno cuando la red está dentro de parámetros. Si detecta falla → desenergiza el relé → abre el circuito de control del contactor → el motor se para.
Ventajas:
- Protege contra las causas de falla más comunes en Venezuela (falta de fase, desequilibrio, subtensión)
- Bajo costo (similar a un relé térmico básico)
- Sin conexión a la línea de potencia del motor (solo mide tensión)
- Función de temporización de rearranque (evita arranques inmediatos)
- No requiere transformadores de corriente adicionales
Limitaciones:
- No protege contra sobrecarga (no mide corriente del motor)
- Debe combinarse siempre con relé de sobrecarga
- Algunos modelos tienen ajuste de umbral limitado
Aplicaciones: Complemento obligatorio del relé de sobrecarga en Venezuela. Especialmente importante en: bombas de proceso continuo, compresores de refrigeración, motores en zonas con red inestable.
Instalación: Entre la alimentación trifásica y el circuito de control. El contacto de salida del monitor se conecta en serie con el contacto de control del relé de sobrecarga y el paro de emergencia.

### TECH_PRODUCT: Guardamotor_Magnetotermico
Descripción: Dispositivo combinado (también llamado "motor protector circuit breaker" o MPCB — Motor Protective Circuit Breaker) que integra en un solo aparato la función de:
- Interruptor de potencia (apertura/cierre manual del circuito)
- Protección magnetotérmica de sobrecarga (elemento térmico bimetálico)
- Protección electromagnética de cortocircuito (disparador magnético)
Norma: IEC 60947-2 (como interruptor) + IEC 60947-4-1 (como arrancador).
Ventajas vs combinación fusible + contactor + relé térmico:
- Ocupa menos espacio en el tablero (un solo aparato vs tres)
- Eliminación de fusibles (sin necesidad de repuestos en almacén)
- Apertura manual del circuito integrada (función de seccionador)
- Menor costo total del conjunto en potencias medias
- Fácil coordinación (Tipo 1 o Tipo 2 garantizada por el fabricante)
Limitaciones:
- No detecta falta de fase en todos los modelos
- No detecta desequilibrio (requiere monitor de red adicional)
- Rango de ajuste de corriente más limitado que relé térmico independiente
- En cortocircuito severo, puede requerir inspección antes de rearrancar
- Capacidad de ruptura limitada en modelos económicos (3-10 kA típico)
- Requiere complemento (monitor de red) para protección completa
Rango de aplicación: Típicamente motores de 0.1 kW a 45-75 kW según fabricante.
Ajuste: Dial de corriente ajustable al In del motor. Curva de disparo fija (definida por el fabricante para la referencia seleccionada).
Selección: Elegir referencia cuyo rango de ajuste cubra In del motor. Si In está en el límite superior del rango, elegir la siguiente referencia.

### TECH_PRODUCT: Rele_Termistor_PTC
Descripción: Sistema de protección que utiliza termistores PTC (Positive Temperature Coefficient) embebidos en los devanados del motor como sensores de temperatura directa, conectados a un relé amplificador que interpreta la resistencia del termistor y dispara cuando supera el umbral de temperatura.
Principio: Un termistor PTC tiene resistencia muy baja (100-1000 Ω) a temperatura normal y se dispara abruptamente (resistencia → ∞) al alcanzar la temperatura nominal de disparo (Tn del PTC = temperatura de disparo de clase).
Configuración típica:
- 3 termistores PTC en serie (uno por bobina principal, devanados A-B-C)
- Circuito serie conectado a relé amplificador externo
- El relé amplificador energiza/desenergiza su contacto de salida
Temperaturas de disparo PTC estándar:
- PTC 110°C: Para motores Clase A/B (disparo antes de límite térmico)
- PTC 130°C: Para motores Clase B (disparo al límite)
- PTC 150°C: Para motores Clase F (disparo conservador)
- PTC 160°C: Para motores Clase F (disparo al límite)
- PTC 180°C: Para motores Clase H
Ventajas:
- Mide temperatura REAL del devanado (no modelo basado en corriente)
- No afectado por temperatura ambiente, ciclo de carga, ni velocidad
- Protege condiciones que los relés de corriente no detectan:
  - Motor parado en ambiente muy caliente
  - Motor con ventilación obstruida
  - Motor sumergible que opera en seco (sin fluido refrigerante)
- Bajo costo del sistema completo (termistores son muy baratos)
Limitaciones:
- Requiere que el motor tenga termistores instalados desde fábrica (o instalación durante rebobinado)
- El relé amplificador requiere alimentación auxiliar
- No reemplaza la protección de cortocircuito ni la de desequilibrio
- Sistema binario (dispara o no dispara → no da temperatura en tiempo real)
Aplicaciones críticas:
- Motores sumergibles (bombas de pozo profundo): protección marcha en seco
- Motores en ambientes de alta temperatura (hornos, plantas cementeras)
- Motores con arranque frecuente donde la temperatura de rotor no es representada correctamente por la corriente del estátor

### TECH_PRODUCT: Rele_de_Proteccion_Diferencial_Motor
Descripción: Relé que compara las corrientes de entrada y salida del motor (o las corrientes de las tres fases en la conexión interna) para detectar corrientes de falla internas al motor. Actúa cuando la diferencia (corriente diferencial) supera un umbral ajustable.
Principio (diferencial de fase a fase en motor):
- Se instalan TCs (transformadores de corriente) en la alimentación del motor
- Se compara la suma fasorial de las tres corrientes (que debe ser = 0 en condiciones normales por simetría trifásica)
- Cualquier fuga a tierra o cortocircuito interno genera una corriente diferencial no nula → disparo
Funciones detectadas:
- ✓ Cortocircuito entre fases en el devanado
- ✓ Cortocircuito de fase a tierra (fuga a tierra)
- ✓ Cortocircuito entre espiras del mismo bobinado (con alta sensibilidad)
Limitaciones:
- Alto costo → reservado para motores de alta potencia (>75-100 kW) o críticos
- Requiere TCs de alta precisión (clase 5P o mejor)
- Configuración compleja
- No común en Venezuela fuera de plantas industriales mayores
Aplicaciones Venezuela: Motores de bombas de agua potable de alta potencia, compresores de refrigeración industrial, motores en procesos continuos donde la parada no planificada tiene costo muy alto.

---

## SECCIÓN 3 — MECANISMOS DE DETECCIÓN Y PROTECCIÓN

### MECHANISM: Deteccion_Sobrecarga_Modelo_Termico
**Cómo funciona la detección de sobrecarga:**

**RELÉ BIMETÁLICO:**
Calor_acumulado ∝ I² × t (relación fundamental)
La lámina bimetálica integra físicamente el calor (actúa como condensador térmico analógico). A mayor corriente, mayor calor, mayor deflexión, disparo más rápido. La curva I²t del bimetálico aproxima la curva de daño térmico del motor para sobrecarga estable.
Limitación: El bimetálico pierde memoria al enfriarse. Después de un arranque, si el motor se detiene y el bimetálico se enfría, el siguiente arranque parte de cero. Pero el rotor del motor retiene calor por más tiempo.

**RELÉ ELECTRÓNICO:**
Modelo térmico digital: θ_motor(t) = θ_ambiente + K × I²
Donde K es una constante que incluye la constante de tiempo térmica del motor.
La memoria térmica se mantiene incluso cuando I = 0 (motor parado).
El modelo puede incluir:
- Constante de tiempo térmica del estátor τ_s
- Constante de tiempo térmica del rotor τ_r (diferente, generalmente mayor)
- Factor de derating por clase de aislamiento
- Factor de corrección por desequilibrio

### MECHANISM: Deteccion_Falta_de_Fase
**RELÉ BIMETÁLICO TRIFÁSICO (método asimétrico):**
En modelos con diseño asimétrico para detección de falta de fase: cuando una fase falta, las corrientes de las otras dos suben. Pero el bimetálico de la fase perdida se enfría → la asimetría entre láminas acciona el disparo.
Tiempo de detección: 10-60 segundos → lento para motores pequeños.

**RELÉ ELECTRÓNICO:**
Compara I_L1, I_L2, I_L3. Si cualquiera cae a cero o < umbral mínimo (típico 10-20% de In) → detección de falta de fase.
Tiempo de detección: < 1 segundo (configurable).

**MONITOR DE RED:**
Mide V_L1, V_L2, V_L3. Si cualquier tensión cae > umbral (típico <50% de Vn) o desaparece → detección de falta de fase.
Tiempo de detección: 100-500 ms (más rápido aún que el relé de corriente).

Mejor práctica: Combinar relé de sobrecarga electrónico + monitor de red. El monitor detecta la falta de fase ANTES de que las corrientes del motor suban significativamente (al detectar la falta de tensión en la red).

### MECHANISM: Deteccion_Desequilibrio
**MÉTODO VOLTIMÉTRICO (monitor de red):**
Mide V_L1, V_L2, V_L3.
Calcula: Vprom = (V_L1 + V_L2 + V_L3) / 3
Calcula: %D = (máx|V_Li - Vprom|) / Vprom × 100%
Si %D > umbral ajustado → disparo o alarma.
Umbral típico ajustable: 2-10%.
Recomendación Venezuela: Ajustar a 3-5% dado que el sistema puede oscilar. Ajuste demasiado bajo (1-2%) → disparos frecuentes por variaciones normales. Ajuste demasiado alto (>8%) → no protege contra desequilibrios dañinos.

**MÉTODO AMPERIMÉTRICO (relé electrónico de sobrecarga):**
Mide I_L1, I_L2, I_L3.
Calcula: Iprom = (I_L1 + I_L2 + I_L3) / 3
Calcula: %D_I = (máx|I_Li - Iprom|) / Iprom × 100%
Umbral típico: 10-30% de desequilibrio de corriente.
Nota: El desequilibrio de corriente es 6-10× mayor que el de tensión. Un 3% de desequilibrio de tensión puede producir 20-30% de corriente. Por esto los umbrales amperimétricos son más altos numéricamente.

### MECHANISM: Deteccion_Locked_Rotor
**DISTINCIÓN CRÍTICA: Arranque normal vs. rotor bloqueado:**
- Arranque normal: I = 5-7 × In durante 2-15 segundos → luego cae a In.
- Rotor bloqueado (stall): I = 5-7 × In indefinidamente (el motor no arranca).

PROBLEMA: La protección no puede distinguir entre las dos condiciones SOLO por la magnitud de la corriente (es la misma). Necesita elemento temporal.

**RELÉ ELECTRÓNICO — FUNCIÓN LOCKED ROTOR:**
El relé mide la corriente de arranque y activa un temporizador. Si la corriente de arranque no baja al valor de plena carga en el tiempo configurado (Tiempo de Arranque) → dispara por locked rotor.
Tiempo de arranque ajustable: Típico 2-30 segundos.
Tiempo de disparo por locked rotor: 1-4 segundos después de vencido el tiempo.

**AJUSTE CORRECTO DEL TIEMPO DE ARRANQUE:**
Medir el tiempo real de aceleración del motor con carga nominal. Configurar tiempo de arranque = t_aceleración × 1.25 (margen del 25%). Error frecuente: Configurar tiempo de arranque muy largo (>30 s) para evitar disparos → el motor no queda protegido contra stall real.

### MECHANISM: Proteccion_Sobretension_Transitoria
Descripción: Picos de tensión de muy corta duración (microsegundos a milisegundos) que superan ampliamente la tensión nominal y pueden dañar el aislamiento del motor.
Causas en Venezuela:
- Maniobras de interruptores en la red de distribución CORPOELEC
- Descargas atmosféricas (rayos) en líneas aéreas
- Arranque/parada de grandes cargas en el mismo transformador
- Efecto de resonancia en cables largos (especialmente con VFD)
Característica: La tensión transitoria puede ser 3-10 × Vn con duración de 1 μs a 100 ms. Los relés de protección normales son demasiado lentos para detectar estos picos.
Protección correcta: Varistores (MOV — Metal Oxide Varistor) o supresores de transitorios (SPD — Surge Protection Devices) instalados en la acometida del tablero o directamente en bornes del motor.
Nota: Esta no es función de los relés de motor pero es una capa de protección complementaria crítica en instalaciones venezolanas.

---

## SECCIÓN 4 — COMPARACIONES Y RANKINGS

### COMPARISON: Rele_Termico_vs_Rele_Electronico
Criterio comparativo para selección según aplicación:

| Criterio                  | Relé Bimetálico    | Relé Electrónico         |
|---------------------------|---------------------|---------------------------|
| Costo inicial             | ★★★★★ (bajo)       | ★★★ (medio-alto)         |
| Precisión de disparo      | ★★★ (±10-15%)      | ★★★★★ (±2-5%)            |
| Memoria térmica real      | ✗ (parcial)        | ✓ (completa)             |
| Detección falta de fase   | ✓ (lenta 10-60s)   | ✓ (rápida < 1s)          |
| Detección desequilibrio   | ✗                  | ✓ (ajustable)            |
| Función locked rotor      | ✗ (básica via I²t) | ✓ (dedicada, ajustable)  |
| Clase de disparo          | Fija (referencia)  | Seleccionable 10/20/30   |
| Diagnóstico de fallas     | ✗                  | ✓ (registro de eventos)  |
| Comunicación              | ✗                  | ✓ (Modbus, Profibus)     |
| Alimentación auxiliar     | No requiere        | Requiere (24V o 110/220V)|
| Arranque frecuente        | ★★ (no apto)       | ★★★★★ (óptimo)           |
| Protección sumergible     | ★★ (sin PTC)       | ★★★★ (con entrada PTC)   |
| Disponibilidad Venezuela  | ★★★★★ (alta)       | ★★★ (media)              |

Recomendación: Para motores de proceso crítico → Relé electrónico. Para motores de uso general no crítico → Relé bimetálico + monitor de red.

### COMPARISON: Fusible_vs_Guardamotor_vs_Interruptor_Motor
Comparación de la protección contra cortocircuito:

| Criterio                  | Fusible NH/BT      | Guardamotor (MPCB)      | Interruptor Motor     |
|---------------------------|---------------------|---------------------------|----------------------|
| Costo inicial             | ★★★★★ (muy bajo)   | ★★★★ (bajo-medio)       | ★★★ (medio)           |
| Costo operativo           | ★★★ (repuestos)    | ★★★★★ (sin repuestos)   | ★★★★★ (sin repuestos)|
| Breaking capacity         | ★★★★★ (hasta 120kA)| ★★★ (3-50 kA típico)    | ★★★★ (hasta 85 kA)   |
| Selectividad              | ★★★★★ (excelente)  | ★★★ (limitada)          | ★★★★ (buena)          |
| Función seccionador       | ✗ (no)             | ✓ (integrado)           | ✓ (integrado)         |
| Curva ajustable           | ✗ (fija por tipo)  | ✓ (rango limitado)      | ✓ (ajuste fino)       |
| Protección sobrecarga     | ✗ (requiere relé)  | ✓ (integrado básico)    | ✓ (integrado)         |
| Disponibilidad Venezuela  | ★★★★★ (muy alta)   | ★★★★ (alta)             | ★★★ (media)           |

### COMPARISON: Niveles_de_Proteccion_por_Criticidad
Según la criticidad del motor en el proceso, el nivel de protección recomendado:

**NIVEL BÁSICO (motores no críticos, fácil reposición):**
Fusible + Contactor AC-3 + Relé térmico bimetálico
Protege: Sobrecarga (básica) + Cortocircuito
No protege: Desequilibrio, falta de fase (adecuada), sub/sobretensión
Costo relativo: Base 1.0×

**NIVEL ESTÁNDAR (motores de proceso, parada costosa):**
Guardamotor MPCB + Contactor AC-3 + Relé electrónico de sobrecarga + Monitor de red
Protege: Sobrecarga + Cortocircuito + Falta de fase + Desequilibrio + Sub/sobretensión + Secuencia de fases
No protege: Temperatura real devanado, fallas internas bobinado
Costo relativo: 2.5-3.5×

**NIVEL PREMIUM (motores críticos, proceso continuo, alto costo de parada):**
Interruptor motor + Contactor AC-3 + Relé electrónico avanzado + Monitor de red + Termistor PTC + Sensor de vibración
Protege: Todas las condiciones anteriores + temperatura real + vibración + diagnóstico completo + comunicación SCADA
Costo relativo: 5-8×

NOTA VENEZUELA: Para motores de bombas de proceso de agua potable, compresores de refrigeración industrial y motores de ventilación crítica, se recomienda mínimo Nivel Estándar. El costo de rebobinado o reposición del motor supera varias veces el diferencial de costo de protección.

---

## SECCIÓN 5 — HALLAZGOS CLAVE

### FINDING: Monitor_de_Red_Obligatorio_Venezuela
En el contexto venezolano (red CORPOELEC con desequilibrios frecuentes, falta de fase por fusibles quemados o contactores deteriorados, y subtensiones recurrentes), el monitor de red es la protección con MEJOR relación costo-beneficio para motores trifásicos. Con un costo similar a un relé térmico básico, protege contra las tres causas más frecuentes de falla de motores en Venezuela: falta de fase, desequilibrio y subtensión. Todo motor de proceso debería tener un monitor de red, independientemente del tipo de relé de sobrecarga seleccionado.

### FINDING: Error_Comun_Ajuste_Estrella_Triangulo
El error más frecuente en la protección de arranque estrella-triángulo en Venezuela es ajustar el relé térmico para la corriente de línea In en lugar de la corriente de fase In/√3 = 0.577 × In. Cuando la protección se conecta a los devanados del motor (no en la línea principal), debe ajustarse para In/√3. Un relé ajustado para In no protegerá el devanado en la configuración triángulo de operación permanente.

### FINDING: Clase_20_Default_Incorrecto
La Clase 20 es frecuentemente especificada como "default" para todos los motores en Venezuela, independientemente de la aplicación. Esto es incorrecto para motores de bombas centrífugas y ventiladores axiales, cuya inercia de carga es baja y cuyos tiempos de arranque son cortos (2-5 segundos). Para estas aplicaciones, la Clase 10 ofrece mayor protección (disparo más rápido en stall) sin riesgo de disparo intempestivo en el arranque. La Clase 20 debe reservarse para compresores de pistón, molinos y cargas de alta inercia.

### FINDING: Coordinacion_Tipo_2_Rentable
El diferencial de costo entre una coordinación Tipo 1 y Tipo 2 en un conjunto guardamotor + contactor + relé electrónico es típicamente 15-25% del costo total del conjunto de maniobra. Sin embargo, un evento de cortocircuito con coordinación Tipo 1 puede requerir la sustitución del contactor y del relé (50-80% del costo del conjunto). Para motores de proceso crítico con fácil acceso a la red, la coordinación Tipo 2 se paga sola en el primer evento de cortocircuito.

### FINDING: Tiempo_Disparo_Real_vs_Nominal
El tiempo de disparo de un relé de sobrecarga depende de la temperatura inicial del relé. Los tiempos de clase IEC (Clase 10/20/30) se definen DESDE FRÍO. Si el relé ya está caliente (arranque reciente, temperatura ambiente alta), el tiempo de disparo REAL es significativamente menor. Esto puede causar disparos intempestivos en motores que realizan arranques sucesivos o que operan en ambientes calientes, incluso con corriente dentro del rango normal. La compensación de temperatura en los relés bimetálicos es parcial. Los relés electrónicos con modelo térmico manejan esto con mayor precisión.

### FINDING: PTC_Unico_Para_Sumergibles
Para motores de bombas sumergibles, el termistor PTC es la única tecnología de protección que detecta eficazmente la marcha en seco. Un motor sumergible que opera sin agua se recalentará incluso con corriente nominal o inferior (porque el agua es su sistema de refrigeración). Un relé de sobrecarga bimetálico o electrónico calibrado para In NO detectará esta condición hasta que la corriente suba significativamente, momento en el que el motor puede ya estar dañado. El PTC responde a la temperatura real del devanado independientemente de la corriente.

### FINDING: Capacidad_Ruptura_Subestimada
Un problema frecuente en tableros de distribución venezolanos construidos hace 10-20 años es que los fusibles y contactores fueron seleccionados con capacidad de ruptura basada en la potencia de cortocircuito disponible en ese momento. El crecimiento de la red, nuevas subestaciones o cambios de transformadores pueden haber aumentado la Icc prospéctica del punto. Un fusible de 25 kA de breaking capacity en un punto donde hoy la Icc es de 35 kA puede explotar en lugar de interrumpir la falla. Ante cualquier ampliación de instalaciones o cambio de transformador, recalcular la Icc y verificar los dispositivos.

---

## SECCIÓN 6 — NORMAS Y FUENTES

### SOURCE: IEC_60947_4_1
IEC 60947-4-1: Low-voltage switchgear and controlgear. Part 4-1: Contactors and motor starters. Electromechanical contactors and motor starters. Ginebra: IEC. Edición vigente 2018.
Contenido: Definición de categorías de utilización AC-2/3/4, clases de disparo 10A/10/20/30, coordinación Tipo 1 y Tipo 2, requisitos de ensayo, modos de protección de sobrecarga.

### SOURCE: IEC_60947_2
IEC 60947-2: Low-voltage switchgear and controlgear. Part 2: Circuit-breakers. Ginebra: IEC.
Contenido: Requisitos para interruptores automáticos incluyendo guardamotores (motor protective circuit breakers). Breaking capacity, curvas de disparo.

### SOURCE: IEC_60947_5_1
IEC 60947-5-1: Low-voltage switchgear and controlgear. Part 5-1: Control circuit devices and switching elements. Electromechanical control circuit devices.
Contenido: Relés de control, contactos auxiliares, dispositivos de monitoreo.

### SOURCE: NEMA_ICS_2
NEMA ICS 2: Industrial Control and Systems: Controllers, Contactors, and Overload Relays Rated 600V. Rosslyn (VA): NEMA.
Contenido: Especificaciones americanas de contactores, relés de sobrecarga, arrancadores de motor. Equivalente NEMA de IEC 60947-4-1.

### SOURCE: IEEE_Std_3004_8
IEEE 3004.8: IEEE Recommended Practice for Motor Protection in Industrial and Commercial Power Systems. Nueva York: IEEE.
Contenido: Guía completa de protección de motores para ingenieros: métodos de detección, coordinación, selección de dispositivos, casos especiales.
Disponibilidad: IEEE Xplore (algunos accesos abiertos para miembros IEEE).

### SOURCE: COVENIN_159
FONDONORMA/COVENIN. COVENIN 159: Instalaciones Eléctricas en Edificaciones. Caracas: FONDONORMA.
Contenido: Código eléctrico venezolano para instalaciones en edificaciones. Referencia complementaria para requisitos locales de protección.

### SOURCE: Schneider_Motor_Protection_Guide
Schneider Electric. Cahier Technique No. 211: Protection of Electrical Networks. Rueil-Malmaison: Schneider Electric.
Disponibilidad: Libre descarga en schneider-electric.com (Cahiers Techniques).
Contenido: Guía técnica completa de protección de redes y motores.
RECOMENDADO: Material técnico de primera calidad, gratuito, aplicable directamente.

### SOURCE: ABB_Motor_Protection
ABB Ltd. Technical Guide No. 8: Electrical Motor Control Systems. Helsinki: ABB.
Disponibilidad: Libre descarga en new.abb.com.
Contenido: Protección y control de motores, selección de dispositivos, coordinación, curvas de disparo.

### SOURCE: WEG_Motor_Application_Guide
WEG Equipamentos Elétricos S.A. Manual de Aplicación de Motores Eléctricos. Jaraguá do Sul: WEG.
Disponibilidad: Libre descarga en weg.net (en español).
Contenido: Guía de aplicación de motores WEG, selección, protección, instalación. Referencia práctica en español.

---

**FIN DEL ATLAS 2 — PROTECCIONES ELÉCTRICAS DE MOTORES**
Proyecto ProtMotores | Versión 1.0 | Marzo 2026
Siguiente: Atlas 3 — Aplicaciones: Bombeo, Refrigeración y Máquinas Rotativas
