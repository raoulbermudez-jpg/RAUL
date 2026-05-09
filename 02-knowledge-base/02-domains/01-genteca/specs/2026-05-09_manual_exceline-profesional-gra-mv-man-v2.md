```markdown
---
title: "Manual de Instalación - Relé Alternador GRA-MV"
type: Technical
source: "GRA-MV_MAN_V2.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GRA-MV"
date_processed: "2026-05-09"
---

# Manual de Instalación - Relé Alternador GRA-MV

## Descripción del Producto

El GRA-MV es un dispositivo electrónico de control que opera activando dos cargas eléctricas en forma alterna. Diseñado para ser usado en cualquier aplicación de automatismo y principalmente para alternar entre dos bombas de sistemas hidroneumáticos.

El producto cuenta con una perilla que permite seleccionar:
- **Modo AUTO**: El relé alterna la salida de forma automática mediante el cambio eléctrico en la señal de control
- **Modo MANUAL**: Selección directa de EQUIPO 1 o EQUIPO 2

## Partes y Piezas

- Contacto NA (Normalmente Abierto)
- Contacto Común
- Contacto NC (Normalmente Cerrado)
- Perilla de modo (EQUIPO 1 / AUTO / EQUIPO 2)
- LED VERDE - Indicador de equipo 1 conectado
- LED VERDE - Indicador de equipo 2 conectado
- Señal de control (CONTROL)
- Gancho de sujeción para riel simétrico
- Orificios para montaje en superficie
- Ranura para montaje de Riel DIN

## Instalación

### PASO 1: Montaje del Dispositivo

#### Montaje sobre Riel DIN

- Coloque el GRA-MV en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GRA-MV y retire el producto del riel.

#### Montaje sobre Superficie Plana

- Coloque el GRA-MV sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de máximo 4 mm ó 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".

### PASO 2: Instalación Eléctrica

**IMPORTANTE:** Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

#### Conexión en 120/220 V~

1. **Conecte los cables de alimentación**: Terminal A1 y A2
2. **Conecte el voltaje a controlar o interrumpir**: Al terminal 7 (Contacto Común)
3. **Conecte EQUIPO 1 o salida al contactor 1**: Al terminal 6 (NC)
4. **Conecte EQUIPO 2 o salida al contactor 2**: Al terminal 8 (NA)
5. **Conecte la señal de control**: Al terminal 2 (CONTROL)

### PASO 3: Configuración de Modo de Operación

- **EQUIPO 1 o EQUIPO 2 (Modo MANUAL)**: Permite activar directamente uno de los dos equipos
- **AUTO (Modo AUTOMÁTICO)**: El relé alternador cambia automáticamente entre ambos equipos según las condiciones de operación, activada por la señal de CONTROL

### PASO 4: Verificación

Reconecte la energía eléctrica y verifique el funcionamiento del GRA-MV y del equipo controlado.

## Diagrama de Conexión Estándar

- **Señal de control** → Terminal 2 (CONTROL)
- **Voltaje de alimentación** → Terminales A1 y A2 (120/220 V~)
- **Bobina Contactor EQUIPO 1** → Terminales 7-6 (Salida Relé NC)
- **Bobina Contactor EQUIPO 2** → Terminales 7-8 (Salida Relé NA)

## Modo de Operación Automático

El ciclo de operación automática responde a la presencia y ausencia de la señal de control:

| Intervalo | Descripción |
|-----------|-------------|
| T0 – T1 | Señal de control desactivada. Salida relé activa: NC (7-6). Ambos equipos apagados. |
| T1 – T2 | Señal de control activa. Salida relé activa: NC (7-6). EQUIPO 1 encendido. |
| T2 | Alternancia: Flanco de bajada. Salida relé cambia a NA (7-8). |
| T2 – T3 | Señal de control desactivada. Salida relé activa: NA (7-8). Ambos equipos apagados. |
| T3 – T4 | Señal de control activa. Salida relé activa: NA (7-8). EQUIPO 2 encendido. |
| T4 | Alternancia: Flanco de bajada. Salida relé cambia a NC (7-6). |
| T4 – T5 | Se inicia el ciclo nuevamente. |

## Descripción de Terminales

| Terminal | Descripción |
|----------|-------------|
| 1, 5 | No utilizado |
| 2 | Entrada de control (CONTROL) |
| 3 | Entrada de voltaje 1 (A1) |
| 4 | Entrada de voltaje 2 (A2) |
| 6 | Contacto normalmente cerrado (NC) |
| 7 | Contacto común (C) |
| 8 | Contacto normalmente abierto (NA) |

## Indicadores Luminosos LED

- **LED VERDE (EQUIPO 1)**: Indica que el equipo 1 se encuentra conectado
- **LED VERDE (EQUIPO 2)**: Indica que el equipo 2 se encuentra conectado
```