```markdown
---
title: "Relé de Nivel para Líquidos Conductores GRN-MV"
type: Technical
source: "GRN-MV_MAN_V1_IMP.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GRN-MV"
date_processed: "2026-05-09"
---

# Manual de Instalación - Relé de Nivel para Líquidos Conductores GRN-MV

## Descripción del Producto

El GRN-MV de Exceline Profesional es un relé electrónico diseñado para el control de nivel de líquidos conductores.

## Partes y Piezas

- **Sonda de referencia (REF)**: Elemento sensor de referencia
- **Sonda nivel máximo (MAX)**: Sensor A2 para nivel alto
- **Sonda nivel mínimo (MIN)**: Sensor A1 para nivel bajo
- **Perilla de ajuste de Sensibilidad**: Control de sensibilidad
- **LED VERDE**: Indicador del estado del relé
- **LED ROJO**: Indicador de encendido del producto
- **Gancho de sujeción para riel simétrico**: Fijación en riel DIN
- **Ranura para montaje de Riel**: Montaje en riel DIN
- **Orificio para montaje en superficie**: Fijación en panel

## Instalación

### Paso 1: Fijación Mecánica

Realice la fijación mecánica del dispositivo, la cual puede ser en montaje sobre riel DIN o sobre superficie plana.

#### Montaje sobre Riel DIN

- Coloque el GRN-MV en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GRN-MV y retire el producto del riel.

#### Montaje sobre Superficie Plana

- Coloque el GRN-MV sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de máximo 4 mm ó 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".
- Dimensiones: 51 mm de altura, 88 mm de ancho.

### Paso 2: Instalación Eléctrica

1. Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

2. Conecte los cables de alimentación en 120/220 V~.

3. Conecte la(s) sonda(s) según la aplicación:

#### Aplicación 1 Nivel - Vaciado con Sonda de Referencia

- Conecte en el terminal 1 la sonda de nivel máximo (MAX)
- El terminal 2 en corto con el terminal 1
- En el terminal 5 la sonda de referencia (REF)

#### Aplicación 2 Niveles - Vaciado con Sonda de Referencia

- Conecte en el terminal 1 la sonda de nivel máximo (MAX)
- En el terminal 2 la sonda de nivel mínimo (MIN)
- En el terminal 5 la sonda de referencia (REF)

4. Conecte el voltaje a controlar o interrumpir en el terminal 7 (contacto común) y la carga o salida al contactor en el terminal 8 (contacto NA).

5. Reconecte la energía eléctrica y verifique el funcionamiento del GRN-MV y del equipo controlado.

6. Ajuste la perilla de sensibilidad en función del líquido conductor de la aplicación.

## Indicadores Luminosos LED

### Indicador LED Verde
- **ON**: Bomba encendida
- **OFF**: Bomba apagada

*Nota: En la Aplicación de Llenado, la indicación del LED verde se invierte.*

### Indicador LED Rojo
- **ON**: Producto encendido
- **OFF**: Producto apagado

## Diagrama de Conexión para Aplicación de Vaciado

### Terminales

| Terminal | Descripción |
|----------|-------------|
| 1 | Sonda nivel máximo (MAX) |
| 2 | Sonda nivel mínimo (MIN) |
| 3 | Entrada voltaje 1 (A1) |
| 4 | Entrada voltaje 2 (A2) |
| 5 | Sonda de referencia (REF) |
| 6 | Contacto normalmente cerrado (NC) |
| 7 | Contacto común (C) |
| 8 | Contacto normalmente abierto (NA) |

### Conexión

- **Sonda de referencia (REF)**: Conexión a terminal 5
- **Voltaje a controlar o interrumpir (24-250 V~)**: A1 y A2 (120 ó 220 V~)
- **Sonda nivel mínimo (MIN)**: Conexión a terminal 2
- **Sonda nivel máximo (MAX)**: Conexión a terminal 1
- **Carga o bobina a controlar**: Conexión a terminal 8 (contacto NA)

*Nota: En la salida del GRN-MV para aplicación de llenado, el voltaje que debe ser controlado o interrumpido se mantiene en el terminal 7 (contacto común), mientras que la carga a manejar cambia al terminal 6 (contacto NC).*
```