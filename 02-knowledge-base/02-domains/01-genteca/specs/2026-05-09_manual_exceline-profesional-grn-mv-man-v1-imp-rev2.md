```markdown
---
title: "Relé de Nivel para Líquidos Conductores GRN-MV"
type: Technical
source: "GRN-MV_MAN_V1_IMP_REV2.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GRN-MV"
date_processed: "2026-05-09"
---

# Manual de Instalación - Relé de Nivel para Líquidos Conductores GRN-MV

## Descripción General

El GRN-MV de Exceline Profesional es un relé electrónico diseñado para el control de nivel de líquidos conductores.

## Partes y Piezas

- **Sonda de referencia**: Elemento de detección de referencia
- **Sonda nivel máximo (A2)**: Sensor para nivel máximo
- **Sonda nivel mínimo (A1)**: Sensor para nivel mínimo
- **Perilla de ajuste de Sensibilidad**: Control para calibración según tipo de líquido
- **LED VERDE**: Indicador del estado del relé (bomba encendida/apagada)
- **LED ROJO**: Indicador de encendido del producto
- **Contacto Común**: Terminal 7
- **Contacto NC**: Terminal 6 (Normalmente Cerrado)
- **Contacto NA**: Terminal 8 (Normalmente Abierto)
- **Gancho de sujeción para riel**: Para montaje en riel DIN
- **Orificios para montaje en superficie**: Fijación alternativa a panel plano

## Instalación

### Paso 1: Fijación Mecánica

Realice la fijación mecánica del dispositivo, la cual puede ser en montaje sobre riel DIN o sobre superficie plana.

#### Montaje sobre Riel DIN

- Coloque el GRN-MV en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel: con un destornillador plano, hale hacia abajo el gancho de retención que está ubicado en el dorso del GRN-MV y retire el producto del riel.

#### Montaje sobre Superficie Plana

- Coloque el GRN-MV sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de máximo 4 mm ó 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".
- Dimensiones de separación: 88 mm entre orificios, profundidad de montaje: 51 mm.

### Paso 2: Instalación Eléctrica

1. **Desconecte el breaker** antes de iniciar el trabajo eléctrico para evitar accidentes.

2. **Conecte los cables de alimentación** en conexión 120/220 V~

3. **Conecte la(s) sonda(s) según la aplicación**

#### Aplicación 1 Nivel (Vaciado)

- Conecte en el terminal 1 la sonda de nivel máximo (Max)
- Terminal 2 en corto con el terminal 1
- Terminal 5: sonda de referencia

#### Aplicación 2 Niveles (Vaciado)

- Terminal 1: sonda de nivel máximo (Max)
- Terminal 2: sonda de nivel mínimo (Min)
- Terminal 5: sonda de referencia

4. **Conecte el voltaje a controlar o interrumpir** en el terminal 7 (contacto común) y la carga o salida al contactor en el terminal 8 (contacto NA).

5. **Reconecte la energía eléctrica** y verifique el funcionamiento del GRN-MV y del equipo controlado.

6. **Ajuste la perilla de sensibilidad** en función del líquido conductor de la aplicación.

## Indicadores Luminosos LED

### LED VERDE (Indicador de estado del relé)
- **ON**: Bomba encendida
- **OFF**: Bomba apagada

### LED ROJO (Indicador de encendido del producto)
- **ON**: Producto encendido
- **OFF**: Producto apagado

## Diagrama de Conexión Estándar

Conexión típica con sonda de referencia, sonda nivel mínimo, sonda nivel máximo, voltaje a controlar o interrumpir (24-250 V~), y carga o bobina a controlar (120 ó 220 V~).

## Tabla de Terminales

| Terminal | Descripción |
|----------|-------------|
| 1 | Sonda nivel máximo |
| 2 | Sonda nivel mínimo |
| 3 | Entrada voltaje 1 (A1) |
| 4 | Entrada voltaje 2 (A2) |
| 5 | Sonda de referencia |
| 6 | Contacto normalmente cerrado (NC) |
| 7 | Contacto común |
| 8 | Contacto normalmente abierto (NA) |
```