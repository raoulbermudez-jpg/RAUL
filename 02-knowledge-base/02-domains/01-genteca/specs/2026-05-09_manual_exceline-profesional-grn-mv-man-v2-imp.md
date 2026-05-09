```markdown
---
title: "Relé de Nivel para Líquidos Conductores GRN-MV"
type: Technical
source: "GRN-MV_MAN_V2_IMP.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GRN-MV"
date_processed: "2026-05-09"
---

# Manual de Instalación - Relé de Nivel para Líquidos Conductores GRN-MV

El GRN-MV es un relé electrónico, diseñado para el control de nivel de líquidos conductores.

## Partes y Piezas

- Orificio para montaje en superficie
- Contacto Común
- Contacto NC (normalmente cerrado)
- Contacto NA (normalmente abierto)
- Sonda de referencia (REF)
- Perilla de ajuste de Sensibilidad
- Ranura para montaje de Riel
- LED VERDE - Indicador del estado del relé
- LED ROJO - Indicador de encendido del producto
- Sonda nivel máximo (MAX) - A2
- Sonda nivel mínimo (MIN) - A1
- Gancho de sujeción para riel simétrico
- Orificio para montaje en superficie

## Instalación

### PASO 1 - FIJE MECÁNICAMENTE EL DISPOSITIVO

#### Montaje sobre Riel DIN

- Coloque el GRN-MV en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GRN-MV y retire el producto del riel.

#### Montaje sobre superficie plana

- Coloque el GRN-MV sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de máximo 4 mm ó 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".
- Dimensiones de montaje: 88 mm × 51 mm

### PASO 2 - REALICE LA INSTALACIÓN ELÉCTRICA DEL PRODUCTO

1. Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

2. Conecte los cables de alimentación en Conexión 120/220 V~ a los terminales A1 y A2.

3. Conecte la(s) sonda(s) según la aplicación:

#### Aplicación 1 Nivel - Vaciado

- Conecte en el terminal 1 la sonda de nivel máximo (MAX)
- Terminal 2 en corto con el terminal 1
- En el terminal 5 la sonda de referencia (REF)

#### Aplicación 2 Niveles - Vaciado

- Conecte en el terminal 1 la sonda de nivel máximo (MAX)
- En el terminal 2 la sonda de nivel mínimo (MIN)
- En el terminal 5 la sonda de referencia (REF)

4. Conecte el voltaje a controlar o interrumpir en el terminal 7 (contacto común) y la carga o salida al contactor en el terminal 8 (contacto NA).

5. Reconecte la energía eléctrica y verifique el funcionamiento del GRN-MV y del equipo controlado.

6. Ajuste la perilla de sensibilidad en función del líquido conductor de la aplicación.

## Indicadores Luminosos LED

Para Aplicación de Vaciado:
- LED VERDE: Estado del relé
- LED ROJO: Encendido del producto

*En la Aplicación de Llenado, la indicación del LED verde se invierte. Además, en la salida del GRN-MV, el voltaje que debe ser controlado o interrumpido se mantiene en el terminal 7 (contacto común), mientras que la carga a manejar cambia al terminal 6.*

## Diagrama de Conexión

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
```