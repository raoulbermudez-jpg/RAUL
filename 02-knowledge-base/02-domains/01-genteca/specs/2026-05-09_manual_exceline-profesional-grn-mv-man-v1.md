---
title: "GRN-MV - Relé de Nivel para Líquidos Conductores"
type: Technical
source: "GRN-MV_MAN_V1.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GRN-MV"
date_processed: "2026-05-09"
---

# Manual de Instalación - Relé de Nivel para Líquidos Conductores GRN-MV

## Descripción del Producto

El GRN-MV es un relé electrónico diseñado para el control de nivel de líquidos conductores de la línea Exceline Profesional.

## Partes y Piezas

- **Sonda de referencia (REF)**: Sonda de nivel
- **Sonda nivel máximo (MAX)**: Control de nivel superior
- **Sonda nivel mínimo (MIN)**: Control de nivel inferior
- **Perilla de ajuste de Sensibilidad**: Regulación según tipo de líquido
- **LED VERDE**: Indicador del estado del relé (bomba)
- **LED ROJO**: Indicador de encendido del producto
- **Contacto Común (C)**: Terminal 7
- **Contacto NC**: Terminal 6 (normalmente cerrado)
- **Contacto NA**: Terminal 8 (normalmente abierto)
- **Gancho de sujeción para riel simétrico**: Fijación en riel DIN
- **Orificio para montaje en superficie**: Alternativa de fijación
- **Ranura para montaje de Riel DIN**: Instalación sobre carril

## Instalación

### PASO 1: Fijación Mecánica del Dispositivo

#### Montaje sobre Riel DIN

- Coloque el GRN-MV en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GRN-MV y retire el producto del riel.

#### Montaje sobre Superficie Plana

- Coloque el GRN-MV sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de máximo 4 mm ó 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".

**Dimensiones de montaje:** 51 mm × 88 mm

### PASO 2: Instalación Eléctrica del Producto

#### Precauciones

- Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

#### Conexión en 120/220 V~

Conecte los cables de alimentación a los terminales A1 y A2.

#### Conexión de Sondas según Aplicación

**Aplicación Vaciado 1 Nivel:**
- Conecte en el terminal 1 la sonda de nivel máximo (MAX)
- Terminal 2 en corto con el terminal 1
- Terminal 5 la sonda de referencia (REF)

**Aplicación Vaciado 2 Niveles:**
- Conecte en el terminal 1 la sonda de nivel máximo (MAX)
- Terminal 2 la sonda de nivel mínimo (MIN)
- Terminal 5 la sonda de referencia (REF)

#### Conexión de Carga

- Conecte el voltaje a controlar o interrumpir en el terminal 7 (contacto común)
- Conecte la carga o salida al contactor en el terminal 8 (contacto NA)

#### Finalización

- Reconecte la energía eléctrica y verifique el funcionamiento del GRN-MV y del equipo controlado.
- Ajuste la perilla de sensibilidad en función del líquido conductor de la aplicación.

## Indicadores Luminosos LED

### Indicador LED Verde

| Estado | Significado |
|--------|------------|
| ON | Bomba encendida |
| OFF | Bomba apagada |

### Indicador LED Rojo

| Estado | Significado |
|--------|------------|
| ON | Producto encendido |
| OFF | Producto apagado |

**Nota:** En la Aplicación de Llenado, la indicación del LED verde se invierte. Además, en la salida del GRN-MV, el voltaje que debe ser controlado o interrumpido se mantiene en el terminal 7 (contacto común), mientras que la carga a manejar cambia al terminal 6.

## Descripción de Terminales

| Terminal | Descripción |
|----------|------------|
| 1 | Sonda nivel máximo (MAX) |
| 2 | Sonda nivel mínimo (MIN) |
| 3 | Entrada voltaje 1 (A1) |
| 4 | Entrada voltaje 2 (A2) |
| 5 | Sonda de referencia (REF) |
| 6 | Contacto normalmente cerrado (NC) |
| 7 | Contacto común (C) |
| 8 | Contacto normalmente abierto (NA) |

## Diagrama de Conexión para Aplicación de Vaciado

- Sonda de referencia (REF)
- Sonda nivel mínimo (MIN)
- Sonda nivel máximo (MAX)
- Voltaje a controlar o interrumpir (24-250 V~)
- Carga o bobina a controlar
- Entrada voltaje: 120 ó 220 V~