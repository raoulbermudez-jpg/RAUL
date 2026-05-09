```markdown
---
title: "Relé de Nivel para Líquidos Conductores GRN-MV"
type: Technical
source: "GRN-MV_MAN_V3_IMP.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GRN-MV"
date_processed: "2026-05-09"
---

# Manual de Instalación - Relé de Nivel para Líquidos Conductores GRN-MV

## Descripción General

El GRN-MV es un relé electrónico diseñado para el control de nivel de líquidos conductores. Su sistema inteligente ante un apagón o parpadeo memoriza la tarea en ejecución (vaciado o llenado) y al restablecerse el servicio retornará con esta funcionalidad.

## Partes y Piezas

- **Sonda de referencia (REF)**: Elemento de detección de nivel
- **Sonda nivel máximo (MAX)**: Sonda A2
- **Sonda nivel mínimo (MIN)**: Sonda A1
- **Contacto Común**: Terminal de conexión
- **Contacto NC**: Contacto normalmente cerrado
- **Contacto NA**: Contacto normalmente abierto
- **Perilla de ajuste de Sensibilidad**: Control de sensibilidad
- **LED VERDE**: Indicador del estado del relé
- **LED ROJO**: Indicador de encendido del producto
- **Gancho de sujeción**: Para montaje en riel simétrico
- **Orificio para montaje**: En superficie o riel DIN

## Instalación

### Paso 1: Montaje Mecánico

#### Montaje sobre Riel DIN

- Coloque el GRN-MV en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel: con un destornillador plano hale hacia abajo el gancho de retención ubicado en el dorso del GRN-MV y retire el producto del riel.

#### Montaje sobre Superficie Plana

- Coloque el GRN-MV sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de máximo 4 mm ó 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".
- Separación entre orificios: 51 mm
- Profundidad de montaje: 8 mm

### Paso 2: Instalación Eléctrica

1. **Desconecte el breaker** antes de iniciar el trabajo eléctrico para evitar accidentes.

2. **Conecte los cables de alimentación** en conexión 120/220 V~

3. **Conecte la(s) sonda(s) según la aplicación:**

#### Aplicación 1 Nivel - Vaciado

- Terminal 1: Sonda de nivel máximo (MAX)
- Terminal 2: En corto con terminal 1
- Terminal 5: Sonda de referencia (REF)

#### Aplicación 2 Niveles - Vaciado

- Terminal 1: Sonda de nivel máximo (MAX)
- Terminal 2: Sonda de nivel mínimo (MIN)
- Terminal 5: Sonda de referencia (REF)

4. **Conexión de control y salida:**
   - Terminal 7 (contacto común): Voltaje de control
   - Terminal 8 (contacto NA): Carga o salida al contactor
   - Reconecte la energía eléctrica

### Paso 5: Ajuste de Sensibilidad

- Verifique que la perilla de sensibilidad esté alineada con el valor sugerido (punta de flecha blanca).
- Con las sondas ya cubiertas por el líquido, espere el tiempo de detección después de estabilizado el nivel (10 segundos).
- Si enciende el LED verde, deje el ajuste en el valor recomendado.
- De lo contrario, aumente la sensibilidad.

**IMPORTANTE:** Recuerde esperar 10 segundos cada vez que ajuste la sensibilidad.

## Indicadores Luminosos LED

En aplicación de vaciado:
- **LED verde encendido**: Nivel de líquido por encima del punto de referencia
- **LED rojo encendido**: Producto energizado

*Nota: En la Aplicación de Llenado, la indicación del LED verde se invierte.*

## Diagrama de Conexión

### Descripción de Terminales

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

### Consideraciones para Aplicación de Llenado

En la Aplicación de Llenado:
- La indicación del LED verde se invierte respecto a vaciado
- El voltaje a controlar o interrumpir se mantiene en el terminal 7 (contacto común)
- La carga a manejar cambia al terminal 6 (contacto NC)
```