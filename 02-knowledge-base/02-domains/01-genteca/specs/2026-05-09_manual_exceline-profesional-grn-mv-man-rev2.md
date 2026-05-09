```markdown
---
title: "Manual de Instalación - Relé de Nivel para Líquidos GRN-MV"
type: Technical
source: "GRN-MV_MAN REV2.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GRN-MV"
date_processed: "2026-05-09"
---

# Manual de Instalación - Relé de Nivel para Líquidos GRN-MV

## Descripción del Producto

El GRN-MV de Exceline Profesional es un relé (relevador) electrónico, diseñado para el control de nivel de líquidos conductores.

## Partes y Piezas

- **Contacto Común**: Terminal de conexión común
- **Contacto NC**: Contacto normalmente cerrado
- **Contacto NA**: Contacto normalmente abierto
- **Electrosonda común**: Sonda de referencia común
- **Perilla de ajuste de Sensibilidad**: Control de sensibilidad del dispositivo
- **LED verde**: Indicador de estado del relé
- **LED rojo**: Indicador de encendido del producto
- **Electrosonda A1**: Nivel mínimo
- **Electrosonda A2**: Nivel máximo
- **Orificio para montaje en superficie**: Para fijación en panel
- **Ranura para montaje de riel**: Para instalación en riel DIN

## Paso 1: Fijación Mecánica del Dispositivo

### Montaje sobre Riel DIN

- Coloque el GSM-C en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GSM-C y retire el producto del riel.

### Montaje sobre Superficie Plana

- Coloque el GSM-C sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".

## Paso 2: Instalación Eléctrica del Producto

### 2.1 Precauciones de Seguridad

Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

### 2.2 Conecte los Cables de Alimentación

Conexión en 120/220 V~

- Identifique la fase (F) y el neutro (N) de la red eléctrica a supervisar.
- Conéctelos a los terminales 3 y 4 (A1 y A2).

### 2.3 Conecte la(s) Sonda(s) Según la Aplicación

#### Aplicación Vaciado 1 Nivel

- Conecte en el terminal 1 la sonda de nivel máximo (Max)
- El terminal 2 en corto con el terminal 1
- En el terminal 5 la electrosonda común

#### Aplicación Vaciado 2 Niveles

- Conecte en el terminal 1 la electrosonda de nivel máximo (Max)
- Conecte en el terminal 2 la electrosonda de nivel mínimo (Min)
- En el terminal 5 la electrosonda común

### 2.4 Conecte el Voltaje a Controlar o Interrumpir

- Terminal 7 (contacto común): Voltaje a controlar o interrumpir (24-230 V~)
- Terminal 8 (contacto NA): Carga o salida al contactor

### 2.5 Verificación de Funcionamiento

Reconecte la energía eléctrica y verifique el funcionamiento del GRN-MV y del equipo controlado.

### 2.6 Ajuste de Sensibilidad

Ajuste la perilla de sensibilidad en función del líquido conductor de la aplicación.

## Diagrama de Conexión Estándar de Vaciado

| Terminal | Descripción |
|----------|-------------|
| 1 | Electrosonda nivel máximo |
| 2 | Electrosonda nivel mínimo |
| 3 | Entrada voltaje fase 1 (A1) |
| 4 | Entrada voltaje fase 2 (A2) |
| 5 | Electrosonda común |
| 6 | Contacto normalmente cerrado (NC) |
| 7 | Contacto común |
| 8 | Contacto normalmente abierto (NA) |

## Indicadores Luminosos en Aplicación de Vaciado

| Indicador | Estado | Condición |
|-----------|--------|-----------|
| LED Verde | ON | Bomba encendida |
| LED Verde | OFF | Bomba apagada |
| LED Rojo | ON | Producto encendido |
| LED Rojo | OFF | Producto apagado |

## Nota Importante

En la Aplicación de Llenado la indicación del LED verde se invierte. En la salida del GRN-MV se conecta el voltaje a controlar o interrumpir en el terminal 7 (contacto común) y la carga o salida al contactor en el terminal 6 (contacto NC).
```