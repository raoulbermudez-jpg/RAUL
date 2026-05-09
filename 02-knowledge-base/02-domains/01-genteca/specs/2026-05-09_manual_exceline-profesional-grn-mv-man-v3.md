```markdown
---
title: "Manual de Instalación - Relé de Nivel para Líquidos Conductores GRN-MV"
type: Technical
source: "GRN-MV_MAN_V3.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GRN-MV"
date_processed: "2026-05-09"
---

# Manual de Instalación - Relé de Nivel para Líquidos Conductores GRN-MV

## Descripción del Producto

El GRN-MV es un relé electrónico diseñado para el control de nivel de líquidos conductores. Su sistema inteligente ante un apagón o parpadeo memoriza la tarea en ejecución (vaciado o llenado) y al restablecerse el servicio retorna con esta funcionalidad.

## Partes y Piezas

- **Orificio para montaje en superficie**: ubicado en la parte inferior del dispositivo
- **Contacto Común (C)**: terminal 7
- **Contacto NC**: terminal 6
- **Contacto NA**: terminal 8
- **Sonda de referencia (REF)**: terminal 5
- **Perilla de ajuste de Sensibilidad**: control manual para calibración
- **Ranura para montaje de Riel DIN**: para instalación en riel estándar
- **LED VERDE**: Indicador del estado del relé
- **LED ROJO**: Indicador de encendido del producto
- **Gancho de sujeción para riel simétrico**: ubicado en el dorso del dispositivo
- **Sonda nivel máximo (MAX)**: terminal 1
- **Sonda nivel mínimo (MIN)**: terminal 2

## Instalación

### Paso 1: Fijación Mecánica del Dispositivo

#### Montaje sobre Riel DIN

- Coloque el GRN-MV en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GRN-MV y retire el producto del riel.

#### Montaje sobre Superficie Plana

- Coloque el GRN-MV sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de máximo 4 mm ó 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".
- Distancia entre orificios: 88 mm (ancho total: 51 mm)

### Paso 2: Instalación Eléctrica del Producto

**IMPORTANTE**: Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

#### Conexión en 120/220 V~

Conecte los cables de alimentación en los terminales A1 (entrada voltaje 1) y A2 (entrada voltaje 2).

#### Conexión de Sondas según la Aplicación

**Aplicación Vaciado 1 Nivel:**
- Conecte en el terminal 1 la sonda de nivel máximo (MAX)
- Terminal 2 en corto con el terminal 1
- Terminal 5 la sonda de referencia (REF)

**Aplicación Vaciado 2 Niveles:**
- Conecte en el terminal 1 la sonda de nivel máximo (MAX)
- En el terminal 2 la sonda de nivel mínimo (MIN)
- En el terminal 5 la sonda de referencia (REF)

#### Conexión de Salida

Conecte el voltaje de control en el terminal 7 (contacto común) y la carga o salida al contactor en el terminal 8 (contacto NA).

Reconecte la energía eléctrica.

## Ajuste de Sensibilidad

1. Verifique que la perilla de sensibilidad esté alineada con el valor sugerido (punta de flecha blanca).
2. Con las sondas ya cubiertas por el líquido, espere el tiempo de detección después de estabilizado el nivel (10 segundos).
3. Si enciende el LED verde, deje el ajuste en el valor recomendado.
4. De lo contrario, aumente la sensibilidad.

**IMPORTANTE**: Recuerde esperar 10 segundos cada vez que ajuste la sensibilidad.

## Indicadores Luminosos LED

### Indicador LED Verde

| Estado | Aplicación |
|--------|-----------|
| ON | Bomba encendida |
| OFF | Bomba apagada |

**Nota**: En la Aplicación de Llenado, la indicación del LED verde se invierte.

### Indicador LED Rojo

| Estado | Significado |
|--------|------------|
| ON | Producto encendido |
| OFF | Producto apagado |

## Diagrama de Conexión para Aplicación de Vaciado

```
Sonda de referencia (REF) ─── Terminal 5
Sonda nivel mínimo (MIN) ─── Terminal 2
Sonda nivel máximo (MAX) ─── Terminal 1

120 ó 220 V~ ─┬─ A1 (Terminal 3)
              └─ A2 (Terminal 4)

Voltaje a controlar o interrumpir (24-250 V~) ─── Terminal 7 (Contacto común)
Carga o bobina a controlar ─── Terminal 8 (Contacto NA)
```

**Nota para Aplicación de Llenado**: En la salida del GRN-MV, el voltaje que debe ser controlado o interrumpido se mantiene en el terminal 7 (contacto común), mientras que la carga a manejar cambia al terminal 6 (contacto NC).

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
```