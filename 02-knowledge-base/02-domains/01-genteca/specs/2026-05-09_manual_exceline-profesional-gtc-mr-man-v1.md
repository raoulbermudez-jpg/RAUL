```markdown
---
title: "Manual de Instalación - Relé Temporizador Multifunción y Multirango GTC-MR"
type: Technical
source: "GTC-MR_MAN_V1_.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GTC-MR"
date_processed: "2026-05-09"
---

# Manual de Instalación
## Relé Temporizador Multifunción y Multirango GTC-MR

El GTC-MR es un temporizador con múltiples rangos ajustables y cuatro modos de operación seleccionables: ciclado simétrico (CICLO), pulso o intervalo (PULSO), temporizado a la conexión (TC) y temporizado a la desconexión (TD). En todos los casos, excepto TD, la función se activa al energizar el temporizador. Para TD, se requiere una señal auxiliar para el control de la temporización. Este dispositivo es compatible con voltajes nominales de 120/220 V~.

## Partes y Piezas

- **Contacto NA**: Contacto normalmente abierto
- **Contacto Común**: Terminal común del relé
- **Contacto NC**: Contacto normalmente cerrado
- **Perilla de Tiempo**: Control de duración de la temporización
- **Perilla de Rango**: Selector de base de tiempo (segundos, minutos, horas)
- **Perilla de Modo**: Selector del modo de operación
- **LED VERDE**: Indicador de carga conectada
- **LED ROJO**: Indicador de producto encendido
- **Entrada de Control Auxiliar (AUX)**: Terminal 2 para señal de control auxiliar
- **Ranura para Montaje de Riel**: Para instalación en riel DIN
- **Gancho de Sujeción para Riel Simétrico**: Para retención en riel
- **Orificio para Montaje en Superficie**: Para instalación en panel plano

## Instalación

### PASO 1: Fijación Mecánica del Dispositivo

#### Montaje sobre Riel DIN

- Coloque el GTC-MR en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GTC-MR y retire el producto del riel.

#### Montaje sobre Superficie Plana

- Coloque el GTC-MR sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".

Dimensiones: 51 mm × 88 mm

### PASO 2: Instalación Eléctrica del Producto

1. Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

2. Conecte los cables de alimentación en 120 V~ /220 V~.

3. Verifique el modo de operación requerido y de acuerdo a esto siga el paso 3A o 3B.

#### Paso 3A: Conexión para los Modos de Operación (TC, CICLO, PULSO)

- Temporizado a la conexión (TC)
- Ciclado simétrico (CICLO)
- Pulso o intervalo (PULSO)

Conecte el voltaje a controlar o interrumpir al terminal 7 (Contacto Común) y la carga o la salida al contactor al terminal 8 (NA).

#### Paso 3B: Conexión para el Modo de Operación Temporizado a la Desconexión (TD)

Para el modo de Operación Temporizado a la Desconexión (TD), se debe realizar la misma conexión indicada en el paso anterior, añadiendo una conexión adicional. El cable de control auxiliar debe conectarse al terminal 2 (AUX).

4. Realice el ajuste a la perilla MODO de acuerdo a la forma de trabajo requerido.

5. Ajuste la base de tiempo en la que se desea trabajar, mediante la perilla RANGO. Se puede seleccionar en segundos, minutos u horas.

6. Configure el tiempo en el que se requiere la temporización, mediante el ajuste de la perilla TIEMPO. Observe que existen 2 escalas en esta perilla (naranja y blanca) relacionadas con el color de la base de tiempo de la perilla RANGO.

7. Reconecte la energía eléctrica y verifique el funcionamiento del GTC-MR y del equipo protegido.

## Modos de Operación

### Temporizado a la Conexión (TC)

Al aplicar la alimentación, el relé espera el tiempo programado (TR) en las perillas de tiempo y rango para luego activar la carga.

### Pulso o Intervalo (PULSO)

Al aplicar la alimentación, la carga se activa inmediatamente y permanece encendida durante el tiempo programado (TR) en las perillas de tiempo y rango. Luego de transcurrido se desactiva.

### Ciclado Simétrico (CICLO)

La carga se activa y desactiva de forma cíclica, con tiempos (TR) iguales de encendido y apagado, según lo programado en las perillas de tiempo y rango.

### Temporizado a la Desconexión (TD)

La carga se activa con la presencia de la señal de control. Al desaparecer la señal, comienza la temporización (TR), según lo programado en las perillas de tiempo y rango. Al finalizar la misma, la carga se desactiva.

## Indicadores Luminosos LED

### Indicador LED Verde

- **ON**: Carga encendida
- **OFF**: Carga apagada

### Indicador LED Rojo

- **ON**: Producto encendido
- **OFF**: Producto apagado

## Descripción de Terminales

| Terminal | Descripción |
|----------|-------------|
| 1, 6 | No utilizados |
| 2 | Entrada de control auxiliar (AUX) |
| 3 | Entrada de voltaje 1 (A1) |
| 4 | Entrada de voltaje 2 (A2) |
| 5 | Contacto normalmente cerrado (NC) |
| 7 | Contacto común (C) |
| 8 | Contacto normalmente abierto (NA) |

## Diagrama de Conexión Estándar

Voltaje a controlar o interrumpir: 120 ó 220 V~ (Terminales A1 y A2)
Carga o Bobina del contactor: Terminal 7 (Común) y Terminal 8 (NA)
```