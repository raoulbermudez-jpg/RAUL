```markdown
---
title: "Manual de Instalación - Relé Alternador GRA-MV"
type: Technical
source: "GRA-MV_MAN_V2_IMP.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GRA-MV"
date_processed: "2026-05-09"
---

# Manual de Instalación - Relé Alternador GRA-MV

## Descripción General

El GRA-MV es un dispositivo electrónico de control que opera activando dos cargas eléctricas en forma alterna. Diseñado para ser usado en cualquier aplicación de automatismo y principalmente para alternar entre dos bombas de sistemas hidroneumáticos. El producto tiene una perilla que permite seleccionar:

- **Modo AUTO**: Alterna la salida del relé de forma automática mediante el cambio eléctrico en la señal de control
- **Modo MANUAL**: Selección directa de EQUIPO 1 o EQUIPO 2

## Partes y Piezas

- Contacto NA (Normalmente Abierto)
- Contacto NC (Normalmente Cerrado)
- Contacto Común
- Perilla de modo (EQUIPO 1 / AUTO / EQUIPO 2)
- LED VERDE - Indicador de equipo 1 conectado
- LED VERDE - Indicador de equipo 2 conectado
- Señal de control (CONTROL) A1 A2
- Gancho de sujeción para riel simétrico
- Ranura para montaje de riel DIN
- Orificios para montaje en superficie

## Instalación

### PASO 1: Fijación Mecánica

Fije mecánicamente el dispositivo mediante montaje en riel DIN o sobre superficie plana.

#### Montaje sobre Riel DIN

- Coloque el GRA-MV en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GRA-MV y retire el producto del riel

#### Montaje sobre Superficie Plana

- Coloque el GRA-MV sobre la superficie plana del panel donde desea realizar la instalación
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de máximo 4 mm ó 5/32"
- Utilice ramplugs en caso de que realice la instalación sobre una pared

### PASO 2: Instalación Eléctrica

1. **Desconecte el breaker** antes de iniciar el trabajo eléctrico para evitar accidentes

2. **Conecte los cables de alimentación**: Conexión en 120/220 V~

3. **Conecte el voltaje a controlar o interrumpir** al terminal 7 (Contacto Común)

4. **Conecte las salidas**:
   - EQUIPO 1 o salida al contactor 1 al terminal 6 (NC)
   - EQUIPO 2 o salida al contactor 2 al terminal 8 (NA)

5. **Conecte la señal de control** al terminal 2 (CONTROL)

6. **Ajuste el modo de operación**:
   - EQUIPO 1 o EQUIPO 2 (modo MANUAL): Permite activar directamente uno de los dos equipos
   - AUTO: El relé alternador cambia automáticamente entre ambos equipos según las condiciones de operación, activada por la señal de CONTROL

7. **Reconecte la energía eléctrica** y verifique el funcionamiento del GRA-MV y del equipo controlado

## Descripción de Terminales

| Terminal | Descripción |
|----------|-------------|
| 1, 5 | No utilizado |
| 2 | Entrada de control (CONTROL) |
| 3 | Entrada de voltaje 1 (A1) |
| 4 | Entrada voltaje 2 (A2) |
| 6 | Contacto normalmente cerrado (NC) |
| 7 | Contacto común (C) |
| 8 | Contacto normalmente abierto (NA) |

## Modo de Operación Automático

### Ciclo de Funcionamiento

**T0 – T1**: La señal de control se encuentra desactivada. La salida del relé activa es NC (terminales 7-6 conectados). En este intervalo los dos equipos se encuentran apagados.

**T1 – T2**: La señal de control se encuentra activa. La salida del relé activa es NC (terminales 7-6 conectados). En este intervalo permanece encendido el EQUIPO 1.

**T2**: En este instante (en el flanco de bajada) se alterna la salida del relé. Ahora la salida del relé activa es NA (terminales 7-8 conectados).

**T2 – T3**: La señal de control se encuentra desactivada. La salida del relé activa es NA (terminales 7-8 conectados). En este intervalo los dos equipos se encuentran apagados.

**T3 – T4**: La señal de control se encuentra activa. La salida del relé activa es NA (terminales 7-8 conectados). En este intervalo permanece encendido el EQUIPO 2.

**T4**: En este instante (en el flanco de bajada) se alterna la salida del relé. Ahora la salida del relé activa es NC (terminales 7-6 conectados).

**T4 – T5**: Se inicia el ciclo nuevamente como en el intervalo T0-T1.

## Diagrama de Conexión Estándar

El diagrama estándar muestra:
- Alimentación: 120/220 V~
- Bobina del Contactor Equipo 1 conectada a terminales 7-6 (NC)
- Bobina del Contactor Equipo 2 conectada a terminales 7-8 (NA)
- Señal de control conectada a terminal 2
- LEDs indicadores de EQUIPO 1 y EQUIPO 2

## Indicadores Luminosos LED

- **LED EQUIPO 1**: Verde, indica cuando el equipo 1 se encuentra conectado
- **LED EQUIPO 2**: Verde, indica cuando el equipo 2 se encuentra conectado
```