```markdown
---
title: "GTC-MR - Relé Temporizador Multifunción y Multirango"
type: Technical
source: "GTC-MR_MAN_V3_IMP.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GTC-MR"
date_processed: "2026-05-09"
---

# Manual de Instalación
## Relé Temporizador Multifunción y Multirango GTC-MR

El GTC-MR es un temporizador con múltiples rangos ajustables y cuatro modos de operación seleccionables: ciclado simétrico (CICLO), pulso o intervalo (PULSO), temporizado a la conexión (TC) y temporizado a la desconexión (TD). En todos los casos, excepto TD, la función se activa al energizar el temporizador. Para TD, se requiere una señal auxiliar para el control de la temporización. Este dispositivo es compatible con voltajes nominales de 120/220 V~.

## INSTALACIÓN

### PASO 1: Montaje mecánico

Fije mecánicamente el dispositivo mediante montaje en riel DIN o sobre superficie plana.

#### Montaje sobre Riel DIN

- Coloque el GTC-MR en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GTC-MR y retire el producto del riel.

#### Montaje sobre superficie plana

- Coloque el GTC-MR sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".

### PASO 2: Instalación eléctrica

1. Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

2. Conecte los cables de alimentación en 120/220 V~ de acuerdo a esto siga el paso 3A o 3B.

3. Verifique el modo de operación requerido y de acuerdo a esto siga el paso 3A o 3B.

#### Paso 3A: Conexión para los modos de operación

- Temporizado a la conexión (TC)
- Ciclado simétrico (CICLO)
- Pulso o intervalo (PULSO)

Conecte el voltaje a controlar o interrumpir al terminal 7 (Contacto Común) y la carga o la salida al contactor al terminal 8 (NA).

#### Paso 3B: Conexión para el modo de operación Temporizado a la desconexión (TD)

Realice la misma conexión indicada en el paso anterior, añadiendo una conexión adicional. En este caso, el cable de control auxiliar debe conectarse al terminal 2 (AUX).

### PASO 4: Ajuste del modo de operación

Realice el ajuste a la perilla MODO de acuerdo a la forma de trabajo requerido.

### PASO 5: Ajuste de base de tiempo

Ajuste la base de tiempo en la que se desea trabajar, mediante la perilla RANGO. Se puede seleccionar en segundos, minutos u horas.

### PASO 6: Configuración del tiempo

Configure el tiempo en el que se requiere la temporización, mediante el ajuste de la perilla TIEMPO. Observe que existen 2 escalas en esta perilla (naranja y blanca) relacionadas con el color de la base de tiempo de la perilla RANGO.

### PASO 7: Verificación final

Reconecte la energía eléctrica y verifique el funcionamiento del GTC-MR y del equipo protegido.

## MODOS DE OPERACIÓN

### Temporizado a la Conexión (TC)

Al aplicar la alimentación, el relé espera el tiempo de retardo (TR) programado en las perillas de tiempo y rango para luego activar la carga. (Conexión según el punto 3A).

**Indicador LED Verde:**
- ON: Carga encendida
- OFF: Carga apagada

### Pulso o Intervalo (PULSO)

Al aplicar la alimentación, la carga se activa inmediatamente y permanece encendida durante el tiempo de retardo (TR) programado. Luego se desactiva y permanece apagada según lo programado en el rango y las perillas de tiempo. (Conexión según el punto 3A).

**Indicador LED Rojo:**
- ON: Producto encendido
- OFF: Producto apagado

### Ciclado Simétrico (CICLO)

La carga se activa y desactiva de forma cíclica, con tiempos de retardo (TR) iguales de encendido y apagado, según lo programado en las perillas de tiempo y rango. (Conexión según el punto 3A).

### Temporizado a la Desconexión (TD)

La carga se activa con la presencia de la señal de control. Al desaparecer la señal, comienza la temporización de retardo (TR), según lo programado en las perillas de tiempo y rango. Al finalizar la misma, la carga se desactiva. (Conexión según el punto 3B).

## DESCRIPCIÓN DE TERMINALES

| Terminal | Descripción |
|----------|-------------|
| 1, 6 | No utilizado |
| 2 | Entrada de control auxiliar (AUX) * |
| 3 | Entrada de voltaje 1 (A1) |
| 4 | Entrada de voltaje 2 (A2) |
| 5 | Contacto normalmente cerrado (NC) |
| 7 | Contacto común (C) |
| 8 | Contacto normalmente abierto (NA) |

*Solo para el modo TD.

## INDICADORES LUMINOSOS LED

| Indicador | Estado | Significado |
|-----------|--------|-------------|
| LED Verde | ON | Carga encendida |
| LED Verde | OFF | Carga apagada |
| LED Rojo | ON | Producto encendido |
| LED Rojo | OFF | Producto apagado |

## DIAGRAMA DE CONEXIÓN ESTÁNDAR

Conexión de voltaje de alimentación (120 ó 220 V~) a terminales A1 y A2, voltaje a controlar o interrumpir a terminal 7 (Contacto Común), y carga o bobina del contactor a terminal 8 (Contacto Normalmente Abierto).
```