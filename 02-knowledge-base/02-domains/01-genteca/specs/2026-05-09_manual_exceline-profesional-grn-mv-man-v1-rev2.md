```markdown
---
title: "GRN-MV Manual de Instalación - Relé de Nivel para Líquidos Conductores"
type: Technical
source: "GRN-MV_MAN_V1_REV2.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GRN-MV"
date_processed: "2026-05-09"
---

# GRN-MV Manual de Instalación

## Descripción del Producto

El GRN-MV de Exceline Profesional es un relé (relevador) electrónico, diseñado para el control de nivel de líquidos conductores.

## Partes y Piezas

- **Sonda de referencia**: Conexión de referencia común
- **Sonda nivel máximo (A2)**: Sensor de nivel superior
- **Sonda nivel mínimo (A1)**: Sensor de nivel inferior
- **Perilla de ajuste de Sensibilidad**: Control de sensibilidad del relé
- **LED VERDE**: Indicador de estado del relé
- **LED ROJO**: Indicador de encendido del producto
- **Contacto Común**: Terminal de conexión común
- **Contacto NC**: Contacto normalmente cerrado
- **Contacto NA**: Contacto normalmente abierto
- **Orificio para montaje en superficie**: Agujeros de fijación (máximo 4 mm ó 5/32")
- **Ranura para montaje de riel**: Para montaje DIN
- **Gancho de sujeción para riel simétrico**: Mecanismo de fijación en riel

### Dimensiones

- Ancho: 51 mm
- Alto: 88 mm

## Paso 1: Fijación Mecánica del Dispositivo

### Montaje sobre Riel DIN

- Coloque el GRN-MV en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GRN-MV y retire el producto del riel.

### Montaje sobre Superficie Plana

- Coloque el GRN-MV sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de máximo 4 mm ó 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de máximo 4 mm ó 5/32".

## Paso 2: Instalación Eléctrica del Producto

### 2.1 Seguridad Eléctrica

Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

### 2.2 Conexión de Alimentación (120/220 V~)

- Identifique la fase 1 (A1) y la fase 2 (A2) o neutro (N) si la instalación es 120VAC.
- Conecte la fase 1 (A1) al terminal 3.
- Conecte la fase 2 (A2) o neutro (N) al terminal 4.

### 2.3 Conexión de Sondas según la Aplicación

#### Aplicación Vaciado 1 Nivel

- Conecte en el terminal 1 la sonda de nivel máximo (Max).
- Conecte en corto el terminal 2 con el terminal 1.
- Conecte en el terminal 5 la sonda de referencia.

#### Aplicación Vaciado 2 Niveles

- Conecte en el terminal 1 la electrosonda de nivel máximo (Max).
- Conecte en el terminal 2 la electrosonda de nivel mínimo (Min).
- Conecte en el terminal 5 la sonda de referencia (Com).

### 2.4 Conexión de Carga

- Conecte el voltaje a controlar o interrumpir en el terminal 7 (contacto común).
- Conecte la carga o salida al contactor en el terminal 8 (contacto NA).

**Nota para Aplicación de Llenado**: La indicación del LED verde se invierte. En la salida del GRN-MV se conecta el voltaje a controlar o interrumpir en el terminal 7 (contacto común) y la carga o salida al contactor en el terminal 6 (contacto NC).

### 2.5 Verificación de Funcionamiento

Reconecte la energía eléctrica y verifique el funcionamiento del GRN-MV y del equipo controlado.

### 2.6 Ajuste de Sensibilidad

Ajuste la perilla de sensibilidad en función del líquido conductor de la aplicación.

## Indicadores Luminosos en Aplicación de Vaciado

| Indicador | Estado | Significado |
|-----------|--------|-------------|
| LED Verde | ON | Bomba encendida |
| LED Verde | OFF | Bomba apagada |
| LED Rojo | ON | Producto encendido |
| LED Rojo | OFF | Producto apagado |

## Terminal de Conexión - Descripción

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

## Diagrama de Conexión Estándar de Vaciado

- **Voltaje a controlar o interrumpir**: 24-230 V~
- **Conexión de sonda de referencia**: Al terminal 5
- **Conexión de carga o bobina a controlar**: Desde terminal 7 (común) a terminal 8 (NA)

```
</answer_end>