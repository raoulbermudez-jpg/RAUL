```markdown
---
title: "Relé de Nivel para Líquidos Conductores GRN-MV"
type: Technical
source: "GRN-MV_MAN_V2.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GRN-MV"
date_processed: "2026-05-09"
---

# Manual de Instalación - Relé de Nivel para Líquidos Conductores GRN-MV

El GRN-MV es un relé electrónico, diseñado para el control de nivel de líquidos conductores.

## Partes y Piezas

- **Orificio para montaje en superficie**: Ubicado en ambos extremos del dispositivo
- **Contacto Común (C)**: Terminal 7
- **Contacto NC**: Terminal 6 (Normalmente Cerrado)
- **Contacto NA**: Terminal 8 (Normalmente Abierto)
- **Sonda de referencia (REF)**: Terminal 5
- **Sonda nivel máximo (MAX)**: Terminal 1, A2
- **Sonda nivel mínimo (MIN)**: Terminal 2, A1
- **Perilla de ajuste de Sensibilidad**: Control manual para ajustar según el líquido conductor
- **Ranura para montaje de Riel DIN**: Permite instalación en riel simétrico
- **Gancho de sujeción para riel**: Ubicado en el dorso del dispositivo
- **LED VERDE**: Indicador del estado del relé
- **LED ROJO**: Indicador de encendido del producto

## Instalación

### PASO 1: Fijación Mecánica del Dispositivo

El dispositivo debe fijarse mediante montaje en riel DIN o sobre superficie plana.

#### Montaje sobre Riel DIN

- Coloque el GRN-MV en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GRN-MV y retire el producto del riel.

#### Montaje sobre Superficie Plana

- Coloque el GRN-MV sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de máximo 4 mm ó 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".
- Dimensiones: 51 mm x 88 mm

### PASO 2: Instalación Eléctrica del Producto

**Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.**

#### Conexión en 120/220 V~

Conecte los cables de alimentación en los terminales A1 y A2.

#### Conexión de Sondas según la Aplicación

**Aplicación Vaciado 1 Nivel:**
- Conecte en el terminal 1 la sonda de nivel máximo (MAX)
- Terminal 2 en corto con el terminal 1
- Terminal 5 la sonda de referencia (REF)

**Aplicación Vaciado 2 Niveles:**
- Terminal 1: Sonda de nivel máximo (MAX)
- Terminal 2: Sonda de nivel mínimo (MIN)
- Terminal 5: Sonda de referencia (REF)

#### Conexión de Carga

- Conecte el voltaje a controlar o interrumpir en el terminal 7 (contacto común)
- Conecte la carga o salida al contactor en el terminal 8 (contacto NA)

### PASO 3: Verificación y Ajuste

- Reconecte la energía eléctrica y verifique el funcionamiento del GRN-MV y del equipo controlado.
- Ajuste la perilla de sensibilidad en función del líquido conductor de la aplicación.

## Indicadores Luminosos LED

### Indicador LED Verde (Para Aplicación de Vaciado)

- **ON**: Bomba encendida
- **OFF**: Bomba apagada

*Nota: En la Aplicación de Llenado, la indicación del LED verde se invierte.*

### Indicador LED Rojo

- **ON**: Producto encendido
- **OFF**: Producto apagado

## Descripción de Terminales

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

## Notas Sobre Aplicaciones

En la Aplicación de Llenado, además de la inversión del LED verde, en la salida del GRN-MV el voltaje que debe ser controlado o interrumpido se mantiene en el terminal 7 (contacto común), mientras que la carga a manejar cambia al terminal 6.
```