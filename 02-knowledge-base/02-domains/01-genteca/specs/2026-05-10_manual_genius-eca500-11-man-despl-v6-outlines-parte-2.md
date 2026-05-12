---
title: "ECA500-11 Manual de Despliegue - Registro de Mapeo MODBUS"
type: Technical
source: "ECA500-11_MAN_DESPL_V6 OUTLINES.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "ECA500-11"
version_status: "historica"
date_processed: "2026-05-10"
---

# ECA500-11 Manual de Despliegue - Registro de Mapeo MODBUS

## 11.1 AJUSTE DEL CT EXTERNO Y CORRIENTE NOMINAL EN EL MENÚ DE PROTECCIÓN DE CORRIENTE

### Procedimiento de Ajuste

a) Presione los botones de combinación Up & Down para llegar a la pantalla de inicio.

b) Presione Up o Down para llegar a la pantalla CURRENT ADJUST.

c) En la pantalla CT, presione el botón SELECT para configurar el valor NOMINAL.

d) En la pantalla CURRENT ADJUST NOMINAL, obtenga el valor deseado y presione SELECT.

e) En la pantalla CT, presione Up o Down para desplazarse hasta la relación requerida (consulte la tabla para la relación térmica recomendada según Nominal).

f) Presione SELECT para establecer la relación CT requerida o regrese al MENÚ PRINCIPAL.

## 12 MAPEO DE REGISTRO MODBUS

### 12.1 FORMATO DE DATOS MODBUS

| Grupo | Dirección | Nombre | Tipo | Rango Mín | Rango Máx | Tamaño | Unidades | Formato | Configuración |
|-------|-----------|--------|------|-----------|-----------|--------|----------|---------|---------------|
| PRODUCT ID | 00000 | PRODUCT ID | R | - | - | 2 | - | - | - |
| - | 0001 | MODEL | R | - | - | 1 | - | - | - |
| - | 00002 | VERSION | R | 0 | 1 | 1 | - | - | - |
| - | 00003 | MODBUS ADDRESS | Rw | 1 | 127 | 1 | - | - | - |
| SECURITY | 00004 | ACCESS PASSWORD | Rw | 0 | 65535 | 1 | - | - | - |
| SCHEDULE TIMER | 00023 | SCHEDULE TIMER | Rw | 0 | 1 | 1 | - | - | - |
| ADJUSTMENTS | 00025 | (UV) UNDER VOLTAGE SETTING | Rw | 95 | 110 | 1 | VAC | - | - |
| - | 00026 | (OV) OVER VOLTAGE SETTING | Rw | 125 | 155 | 1 | VAC | - | - |
| - | 00027 | (VUB) VOLTAGE UNBALANCE SETTING | Rw | 2 | 10 | 1 | % | - | - |
| - | 00028 | AC POWER FREQUENCY SETTING | Rw | 0 | 1 | 1 | - | - | - |
| - | 00029 | FREQUENCY SHIFT SETTING | Rw | - | - | 1 | - | - | - |
| - | 00030 | (TD) TRIP DELAY SETTING | Rw | 30 | - | 1 | - | - | - |
| - | 00031 | (10) START UP DELAY SETTING | Rw | 0 | - | 1 | - | - | - |
| - | 00033 | CT SETTING | Rw | 0 | 8 | 1 | - | - | - |
| - | 00035 | MOTOR THERMAL CLASS SETTING | Rw | 5 | 30 | 1 | - | - | - |
| - | 00036 | (OL) OVERLOAD LEVEL SETTING | Rw | 5 | - | 1 | % | - | - |
| - | 00037 | UNDERCURRENT DETECTION | Rw | 0 | 1 | 1 | - | - | - |
| - | 00038 | HIGH-INERTIA LOAD DETECTION | Rw | 0 | 1 | 1 | - | - | - |
| - | 00039 | (R) ACCEL LOCKED ROTOR DETECTION | Rw | 0 | 1 | 1 | - | - | - |
| - | 00040 | (3F) THIRD FAILURE DETECTION | Rw | 0 | 1 | 1 | - | - | - |
| - | 00042 | UNDERCURRENT TYPE SETTING | Rw | 0 | 1 | 1 | - | - | - |
| - | 00043 | TRIP DELAY BECAUSE OF UC | Rw | 5 | 500 | 1 | - | - | - |
| - | 00044 | START UP DELAY AFTER UC | Rw | 2 | - | 1 | - | - | - |
| - | 00046 | (PF) UNDERCURRENT PF | Rw | 7 | 90 | 1 | - | - | - |
| - | 00047 | (IN) UNDERCURRENT IN | Rw | 30 | 30 | 1 | % | - | - |
| - | 00048 | TRIP DELAY BECAUSE OF IR | Rw | 20 | - | 1 | - | - | - |
| - | 00049 | COMPENSATION BY TEMPERATURE | Rw | 0 | 1 | 1 | - | - | - |
| - | 00050 | (Ti) INITIAL TEMPERATURE SETTING | Rw | 20 | 150 | 1 | °C | - | - |
| - | 00051 | (Tm) MAXIMUM MOTOR TEMPERATURE | Rw | 50 | 200 | 1 | °C | - | - |
| - | 00053 | DIGITAL INPUT | R | - | - | 1 | - | - | - |
| - | 00054 | DIGITAL INPUT 2 | R | - | - | 1 | - | - | - |
| ACCUMULATOR | 00055 | TOTAL HRS | R | 0 | 59999940 | 1 | min | - | - |
| - | 00056 | HOUR | Rw | 0 | 23 | 1 | - | - | - |
| - | 00057 | MINUTE | Rw | 0 | 59 | 1 | - | - | - |
| - | 00058 | SOFTWARE VERSION | R | - | - | 1 | - | - | - |
| - | 00059 | DAY | Rw | 1 | 31 | 1 | - | - | - |
| - | 00061 | MONTH | Rw | 1 | 12 | 1 | - | - | - |
| - | 00062 | YEAR | Rw | 0 | - | 1 | - | - | - |
| - | 00063 | START MODE | Rw | 0 | 1 | 1 | - | - | - |
| - | 00064 | TEMPERATURE INPUT | Rw | 20 | 200 | 1 | °C | - | - |
| - | 00067 | THERMAL CAPACITY | R | - | - | 1 | - | - | - |
| - | 00068 | CONTROL_ON_OFF | Rw | 0 | 1 | 1 | - | - | - |
| - | 00069 | AUX RELAY MODE | Rw | 0 | 1 | 1 | - | - | - |
| OUTPUT | 00070 | CONTROL RELAY | R | - | - | 1 | - | - | - |
| - | 00072 | AUX RELAY | R | - | - | 1 | - | - | - |
| - | 0007A | (10) START UP DELAY | R | 30000 | - | 1 | - | - | - |
| MEASUREMENT | 00075 | V LINE | R | 0 | - | 1 | - | - | - |
| - | 00078 | V AVERAGE | R | 0 | - | 1 | - | - | - |
| - | 00079 | IU | R | 0 | - | 1 | - | - | - |
| - | 00087 | REACTIVE POWER (A) | R | 0 | 9999 | 1 | - | - | - |
| - | 00088 | ENERGY CONSUMPTION (GWH) | R | - | - | 1 | - | - | - |
| - | 00090 | (PF) POWER FACTOR | R | 0 | 100 | 1 | - | - | - |
| - | 00091 | DYNAMIC THERMAL CLASS | R | 0 | 20 | 1 | - | - | - |
| - | 00092 | TOTAL NUMBER OF STARTS | R | - | - | 1 | - | - | - |
| - | 00093 | CONTADOR_DE_AF | R | 0 | 65535 | 1 | - | - | - |

### Campos de Formato de Datos MODBUS

#### Evento de Cronograma Temporizador (Schedule Timer)

| Bits | Descripción |
|------|-------------|
| bits 10...6 | ON Hour - 0 a 23 - Hora para iniciar el evento |
| bits 16...11 | ON Minute - 0 a 59 - Minuto para iniciar el evento |
| bits 21...17 | OFF Hour - 0 a 23 - Hora para detener el evento |
| bits 23...22 | OFF Minute - 0 a 59 - Minuto para detener el evento |
| bit 24 | Día de la semana - LUNES |
| bit 25 | MARTES |
| bit 26 | MIÉRCOLES |
| bit 27 | JUEVES |
| bit 28 | VIERNES |
| bit 29 | SÁBADO |
| bit 30 | DOMINGO |
| bits 31 | FERIADO |

#### Registro de Fallas (Fault Register)

| Bits | Descripción |
|------|-------------|
| bits 4...0 | Tipo de falla |
| bytes 1...0 | Indicación de valor de falla |
| byte 3 | Fase involucrada en la falla |
| byte 4 | DÍA: 1 a 31 |
| byte 5 | MES: 1 a 12 |
| byte 6 | HORA: 0 a 23 |
| byte 7 | MINUTOS: 0 a 59 |
| bytes 9...8 | Duración: 0 a 9999 min |

#### Códigos de Tipo de Falla

| Código | Descripción |
|--------|-------------|
| FS | Fail - FS (Frequency Shift) |
| PR | Fail - PR (Phase Reversal) |
| VSP | Fail - VSP (Single Phase Unbalance) |
| VUB | Fail - VUB (Voltage Unbalance) |
| UV | Fail - UV (Undervoltage) |
| OV | Fail - OV (Overvoltage) |
| RL | Fail - RL (Locked Rotor) |
| PF | Fail - PF (Power Factor) |
| CUB | Fail - CUB (Current Unbalance) |
| UC | Fail - UC (Undercurrent) |
| OL | Fail - OL (Overload) |
| CSP | Fail - CSP (Current Single Phase) |

### Modo de Control (Control ON/OFF)

| Valor | Descripción |
|-------|-------------|
| 0 | ON |
| 1 | OFF - TRIP DELAY BECAUSE OF VOLTAGE FAILURES |
| 2 | OFF - MODBUS |
| 3 | OFF - MANUAL MODE |
| 4 | OFF - 3RD FAILURE |
| 5 | OFF - SCHEDULER TIMER (Solo productos con Schedule Timer) |
| 6 | OFF - TRIP DELAY BECAUSE OF CURRENT FAILURES |
| 7 | OFF - TRIP DELAY BECAUSE OF (UC) |

## Especificaciones Técnicas ECA500-11

### A) Circuito de Alimentación

- **Frecuencia de Rango**: 45.0 - 70.0 Hz ±1%
- **Tensión de Alimentación Nominal**: Según modelo configurado

### B) Ambiente de Operación

- **Humedad Relativa Máxima**: 95% sin condensación
- **Temperatura Ambiente**: -10°C a +60°C
- **Posición de Montaje**: Cualquier posición
- **Material de Caja**: Tipos PC, ABS, NYLON, etc.

### C) Características de Control

- **Clasificación de Contacto de Salida**: 8A, 250V AC en categoría de utilización AC-15
- **Característica de Dispersión térmica**: Según carga
- **Algoritmo y Funciones de Protección**: Múltiples protecciones configurables

### D) Rango de Configuración y Mediciones

#### Configuración de Tensión Nominal (según modelo)
- **Modelo 120V**: Configuración de fábrica = 108V, Mín = 95V, Máx = 115V
- **Modelo 208/220V**: Configuración de fábrica = 187V, Mín = 165V, Máx = 225V
- **Modelo 380V**: Configuración de fábrica = 360V, Mín = 320V, Máx = 380V
- **Modelo 480V**: Configuración de fábrica = 432V, Mín = 350V, Máx = 460V

#### Configuración de Corriente Nominal

- **Modelo 50A**: Configuración de fábrica = 25A, Mín = 15A, Máx = 50A
- **Modelo 100A**: Configuración de fábrica = 45A, Mín = 30A, Máx = 100A
- **Modelo 180A**: Configuración de fábrica = 60A, Mín = 55A, Máx = 180A
- **Con CTs EXT**: Rangos adicionales disponibles hasta 2000/5

#### Rango de Medición de Corriente

- **Im**: 1.5 a 380 (según modelo de CT)

#### Detección de Desequilibrios y Fases

- **Desequilibrio de Voltaje (VUB)**: 2%
- **Fase Única (VSP)**: 33%
- **Frecuencia Nominal**: 50 o 60 Hz ±2%
- **Variación de Voltaje**: 10%

### E) Algoritmos y Funciones de Protección

- **Detección de Inversión de Fase (PR)**: Disponible
- **Detección de Falla de Fase Única (VSP)**: 33%
- **Detección de Desequilibrio de Corriente (CUB)**: CUB > 48%
- **Detección de Rotor Bloqueado Acelerado (LA)**: Disponible
- **Detección de Carga de Alta Inercia**: Disponible
- **Detección de Corriente Insuficiente**: Configurable

### F) Comunicaciones y Funciones Especiales

- **Protocolo de Comunicación**: MODBUS RTU @ 9600 baud
- **Puertos de Comunicación**: Dual (RS485 K-Link)
- **Historial de Buffer de Memoria**: 20 últimos informes de fallas (tipo de falla, valor de configuración, fecha, hora y tiempo transcurrido)
- **Reloj en Tiempo Real**: mm/dd/yyyy y hh:mm
- **Control de Carga por Eventos (cronograma)**: SÍ/NO (según selección del usuario)
- **Temporizador de Cronograma (eventos)**: 60
- **Temporizador de Cronograma (vacaciones)**: 20

### G) Características Mecánicas

- **Tipo de Montaje**: Riel DIN simétrico 11145880
- **Tipo de Terminal de Entrada**: Bloques de tornillos extraíbles
- **Torque de Apriete de Tornillo**: 2 Kgf·cm (4.51 lbf·in)
- **Cableado**: AWG 30-12, L = 7-8 mm (5/16")
- **Caja CT Desmontable**: 0 < 18 mm máximo AWG 10

### H) Dimensiones

- **Dimensiones Principales**: 120 x 788 (CMA) mm
- **Dimensiones (CTBox)**: 175 x 90 x 1578 (Lal) mm
- **Peso**: 364 g (12 oz) a 2.9 kg (6.4 lbs) según configuración

### I) Protección Contra Sobrecorriente

#### Curva Fría (Cold Curve)

| Carga / Nominal | 50% | 100% | 150% | 200% |
|-----------------|-----|------|------|------|
| Tiempo a viaje | - | - | - | 2 Horas |

Nota: Curva Caliente = Curva Fría / 3 (*1)

### J) Inmunidad y Emisiones, Interferencia Electromagnética (EMC) para Ambiente Industrial Pesado

- **9.1** Descarga Electrostática - IEC 61000-4-2
- **9.2** Inmunidad Radiada - IEC 61000-3-2
- **9.3** Transitorios Rápidos Eléctricos - IEC 61000-4-4
- **9.4** Prueba de Inmunidad de Sobretensión - IEC 61000-4-5
- **9.5** Inmunidad Conducida - IEC 61000-4-6
- **9.6** Campo Magnético de Frecuencia - IEC 61000-8-2
- **9.7** Caídas de Tensión, Interrupciones Breves
- **9.8** Variaciones de Tensión
- **9.9** Armónicos e Interarmónicos - IEC 61000-4-13
- **9.10** Pruebas de Inmunidad
- **9.11** Inmunidad a Fluctuación de Voltaje - IEC 61000-4-14
- **9.12** Prueba de Inmunidad de Desequilibrio - IEC 61000-4-28
- **9.13** Variación de Potencia de Corta Duración - IEC 61000-2-2

### K) Cómo Ordenar ECA500-11

**Modelo Base**: ECA500-11

Contacto:
William Barry Blvd.
North Syracuse, NY 13212
United States

---

**Nota**: Los datos técnicos son válidos al momento de la impresión. Nos reservamos el derecho de realizar alteraciones posteriores.
