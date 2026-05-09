```markdown
---
title: "GRN-MV Manual de Instalación - Relé de Nivel para Líquidos Conductores"
type: Technical
source: "GRN-MV_MAN_V1_REV1.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GRN-MV"
date_processed: "2026-05-09"
---

# GRN-MV - Manual de Instalación
## Relé de Nivel para Líquidos Conductores

El GRN-MV de Exceline Profesional es un relé (relevador) electrónico, diseñado para el control de nivel de líquidos conductores.

## Partes y Piezas

- **Sonda de referencia**
- **Sonda nivel máximo (A2)**
- **Sonda nivel mínimo (A1)**
- **Perilla de ajuste de Sensibilidad**
- **Contacto Común**
- **Contacto NC (Normalmente Cerrado)**
- **Contacto NA (Normalmente Abierto)**
- **LED VERDE**: Indicador de estado del relé
- **LED ROJO**: Indicador de encendido del producto
- **Orificio para montaje en superficie**
- **Ranura para montaje de riel**
- **Gancho de sujeción para riel simétrico**

### Dimensiones
- Altura: 88 mm
- Ancho: 51 mm

## Paso 1: Fijación Mecánica del Dispositivo

La fijación puede ser en montaje sobre riel DIN o sobre superficie plana.

### Montaje sobre Riel DIN

- Coloque el GRN-MV en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GRN-MV y retire el producto del riel.

### Montaje sobre Superficie Plana

- Coloque el GRN-MV sobre la superficie plana del panel donde desea realizar la instalación. Marque con un lápiz los orificios y con un taladro abra dos agujeros de máximo 4 mm ó 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de máximo 4 mm ó 5/32".

## Paso 2: Instalación Eléctrica del Producto

### 2.1 Precaución de Seguridad

Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

### 2.2 Conexión de Alimentación (120/220 V~)

- Identifique la fase 1 (A1) y la fase 2 (A2) o neutro (N) si la instalación es 120VAC, de la red eléctrica.
- Conéctelos a los terminales 3 y 4 respectivamente.

### 2.3 Conexión de Sondas según la Aplicación

#### Aplicación Vaciado 1 Nivel

- Conecte en el terminal 1 la sonda de nivel máximo (Max)
- Conecte el terminal 2 en corto con el terminal 1
- Conecte en el terminal 5 la sonda de referencia

#### Aplicación Vaciado 2 Niveles

- Conecte en el terminal 1 la electrosonda de nivel máximo (Max)
- Conecte en el terminal 2 la electrosonda de nivel mínimo (Min)
- Conecte en el terminal 5 la sonda de referencia (Com)

### 2.4 Conexión de Carga

- Conecte el voltaje a controlar o interrumpir en el terminal 7 (contacto común)
- Conecte la carga o salida al contactor en el terminal 8 (contacto NA)

*En la Aplicación de Llenado la salida del GRN-MV se conecta el voltaje a controlar o interrumpir en el terminal 7 (contacto común) y la carga o salida al contactor en el terminal 6 (contacto NC)

### 2.5 Verificación de Funcionamiento

Reconecte la energía eléctrica y verifique el funcionamiento del GRN-MV y del equipo controlado.

### 2.6 Ajuste de Sensibilidad

Ajuste la perilla de sensibilidad en función del líquido conductor de la aplicación.

## Tabla de Terminales

| Terminal | Descripción |
|----------|-------------|
| 1 | Sonda nivel máximo |
| 2 | Sonda nivel mínimo |
| 3 | Entrada voltaje fase 1 (A1) |
| 4 | Entrada voltaje fase 2 (A2) |
| 5 | Sonda de referencia |
| 6 | Contacto normalmente cerrado (NC) |
| 7 | Contacto común |
| 8 | Contacto normalmente abierto (NA) |

## Indicadores Luminosos en Aplicación de Vaciado

| LED Verde | Estado |
|-----------|--------|
| ON | Bomba encendida |
| OFF | Bomba apagada |

| LED Rojo | Estado |
|----------|--------|
| ON | Producto encendido |
| OFF | Producto apagado |

*En la Aplicación de Llenado la indicación del LED verde se invierte.
```