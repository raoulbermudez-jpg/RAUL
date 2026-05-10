```markdown
---
title: "Manual de Instalación - Relé Temporizador Multifunción y Multirango GTC-MR"
type: Technical
source: "GTC-MR_MAN_V1_IMP.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GTC-MR"
date_processed: "2026-05-09"
---

# Manual de Instalación - Relé Temporizador Multifunción y Multirango GTC-MR

## Descripción General

El GTC-MR es un temporizador con múltiples rangos ajustables y cuatro modos de operación seleccionables:

- Ciclado simétrico (CICLO)
- Pulso o intervalo (PULSO)
- Temporizado a la conexión (TC)
- Temporizado a la desconexión (TD)

En todos los casos, excepto TD, la función se activa al energizar el temporizador. Para TD, se requiere una señal auxiliar para el control de la temporización. Este dispositivo es compatible con voltajes nominales de 120/220 V~.

## Partes y Piezas

- Contacto NA (normalmente abierto)
- Contacto Común
- Contacto NC (normalmente cerrado)
- Perilla de Tiempo
- Perilla de Rango
- LED VERDE - Indicador de Carga Conectada
- LED ROJO - Indicador de Producto Encendido
- Perilla de Modo
- Ranura para montaje de Riel
- Orificio para montaje en superficie
- Gancho de sujeción para riel simétrico
- Entrada de control auxiliar (AUX) A1 A2
- Orificio para montaje en superficie

## Instalación

### PASO 1: Fijación Mecánica del Dispositivo

La fijación mecánica puede realizarse en montaje sobre riel DIN o sobre superficie plana.

#### Montaje sobre Riel DIN

- Coloque el GTC-MR en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GTC-MR y retire el producto del riel.

#### Montaje sobre Superficie Plana

- Coloque el GTC-MR sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".

Dimensiones: 51 mm x 88 mm

### PASO 2: Instalación Eléctrica del Producto

1. **Desconecte el breaker** antes de iniciar el trabajo eléctrico para evitar accidentes.

2. **Conecte los cables de alimentación** en 120 V~ / 220 V~ de acuerdo al modo de operación requerido.

3. **Verifique el modo de operación requerido** y siga el paso 3A o 3B:

#### 3A: Conexión para los Modos de Operación:
- Temporizado a la conexión (TC)
- Ciclado simétrico (CICLO)
- Pulso o intervalo (PULSO)

Conecte el voltaje a controlar o interrumpir al terminal 7 (Contacto Común) y la carga o la salida al contactor al terminal 8 (NA).

#### 3B: Conexión para el Modo Temporizado a la Desconexión (TD)

Para el modo de Operación Temporizado a la Desconexión (TD), se debe realizar la misma conexión indicada en el paso anterior, añadiendo una conexión adicional. En este caso, el cable de control auxiliar debe conectarse al terminal 2 (AUX).

4. **Realice el ajuste** de la perilla base de tiempo bajo requerimiento.

5. **Ajuste la base de tiempo** en la que se desea trabajar, mediante la perilla RANGO. Se puede seleccionar en segundos, minutos u horas.

6. **Configure el tiempo** en el que se requiere la temporización, mediante el ajuste de la perilla TIEMPO. Observe que existen 2 escalas en esta perilla (naranja y blanca) relacionadas con el color de la base de tiempo de la perilla RANGO.

7. **Reconecte la energía eléctrica** y verifique el funcionamiento del GTC-MR y del equipo protegido.

## Modos de Operación

### Temporizado a la Conexión (TC)

Al aplicar la alimentación, el relé espera el tiempo programado (TR) en las perillas de tiempo y rango para luego activar la carga.

Conexión según el punto 3A.

### Pulso o Intervalo (PULSO)

Al aplicar la alimentación, la carga se activa inmediatamente y permanece encendida durante el tiempo programado (TR) en las perillas de tiempo y rango. Pasado este tiempo, se desactiva.

Conexión según el punto 3A.

### Ciclado Simétrico (CICLO)

La carga se activa y desactiva de forma cíclica, con tiempos (TR) iguales de encendido y apagado, según lo programado en las perillas de tiempo y rango.

Conexión según el punto 3A.

### Temporizado a la Desconexión (TD)

La carga se activa con la presencia de la señal de control. Al desaparecer la señal, comienza la temporización (TR), según lo programado en las perillas de tiempo y rango. Al finalizar la misma, la carga se desactiva.

Conexión según el punto 3B.

## Indicadores Luminosos LED

### LED VERDE

- **ON**: Carga encendida
- **OFF**: Carga apagada

### LED ROJO

- **ON**: Producto encendido
- **OFF**: Producto apagado

## Descripción de Terminales

| Terminal | Descripción |
|----------|-------------|
| 1, 6 | No utilizado |
| 2 | Entrada de control auxiliar (AUX) |
| 3 | Entrada de voltaje 1 (A1) |
| 4 | Entrada de voltaje 2 (A2) |
| 5 | Contacto normalmente cerrado (NC) |
| 7 | Contacto común (C) |
| 8 | Contacto normalmente abierto (NA) |

## Diagrama de Conexión Estándar

```
Voltaje a controlar          Carga o Bobina
o interrumpir                del contactor
     
     A1
     
120 ó 220 V~               
     
     A2
```
```