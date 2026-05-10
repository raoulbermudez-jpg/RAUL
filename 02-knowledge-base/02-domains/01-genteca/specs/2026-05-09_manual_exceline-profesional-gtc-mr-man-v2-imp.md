---
title: "Relé Temporizador Multifunción y Multirango GTC-MR"
type: Technical
source: "GTC-MR_MAN_V2_IMP.pdf"
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

## Instalación Mecánica

### Paso 1: Fijación del Dispositivo

**Montaje sobre Riel DIN**
- Coloque el GTC-MR en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GTC-MR y retire el producto del riel.

**Montaje sobre Superficie Plana**
- Coloque el GTC-MR sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".

**Dimensiones:** 51 mm x 88 mm

## Instalación Eléctrica

### Paso 2: Preparación

Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

### Paso 3A: Conexión para los Modos TC, CICLO y PULSO

Conecte los cables de alimentación en 120/220 V~. Conecte el voltaje a controlar o interrumpir al terminal 7 (Contacto Común) y la carga o la salida al contactor al terminal 8 (NA).

### Paso 3B: Conexión para el Modo TD (Temporizado a la Desconexión)

Realice la misma conexión indicada en el paso 3A, añadiendo una conexión adicional. El cable de control auxiliar debe conectarse al terminal 2 (AUX).

### Paso 4: Selección del Modo de Operación

Ajuste la perilla MODO de acuerdo a la forma de trabajo requerido:
- TC (Temporizado a la conexión)
- PULSO (Pulso o intervalo)
- CICLO (Ciclado simétrico)
- TD (Temporizado a la desconexión)

### Paso 5: Ajuste de la Base de Tiempo

Ajuste la perilla RANGO para seleccionar la unidad de tiempo en la que se desea trabajar:
- Segundos (seg)
- Minutos (min)
- Horas (horas)

### Paso 6: Configuración del Tiempo

Configure el tiempo en el que se requiere la temporización mediante el ajuste de la perilla TIEMPO. Observe que existen 2 escalas en esta perilla (naranja y blanca) relacionadas con el color de la base de tiempo de la perilla RANGO.

### Paso 7: Verificación

Reconecte la energía eléctrica y verifique el funcionamiento del GTC-MR y del equipo protegido.

## Modos de Operación

### Temporizado a la Conexión (TC)

Al aplicar la alimentación, el relé espera el tiempo programado (TR) en las perillas de tiempo y rango para luego activar la carga.

### Pulso o Intervalo (PULSO)

Al aplicar la alimentación, la carga se activa inmediatamente y permanece encendida durante el tiempo programado (TR) en las perillas de tiempo y rango. Pasado el tiempo, se desactiva.

### Ciclado Simétrico (CICLO)

La carga se activa y desactiva de forma cíclica, con tiempos (TR) iguales de encendido y apagado, según lo programado en las perillas de tiempo y rango.

### Temporizado a la Desconexión (TD)

La carga se activa con la presencia de la señal de control. Al desaparecer la señal, comienza la temporización (TR), según lo programado en las perillas de tiempo y rango. Al finalizar la misma, la carga se desactiva.

## Indicadores Luminosos LED

### LED Verde
- **ON:** Carga encendida
- **OFF:** Carga apagada

### LED Rojo
- **ON:** Producto encendido
- **OFF:** Producto apagado

## Tabla de Terminales

| Terminal | Descripción |
|----------|-------------|
| 1, 6 | No utilizado |
| 2 | Entrada de control auxiliar (AUX)* |
| 3 | Entrada de voltaje 1 (A1) |
| 4 | Entrada de voltaje 2 (A2) |
| 5 | Contacto normalmente cerrado (NC) |
| 7 | Contacto común (C) |
| 8 | Contacto normalmente abierto (NA) |

*Señal de control auxiliar (AUX) solo para el modo TD.

## Diagrama de Conexión Estándar

Voltaje a controlar o interrumpir: 120 ó 220 V~ (A1-A2)
Carga o Bobina del contactor: Conectada entre terminales 7 (C) y 8 (NA)