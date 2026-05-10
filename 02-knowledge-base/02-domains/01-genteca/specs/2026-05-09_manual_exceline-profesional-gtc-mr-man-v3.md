```markdown
---
title: "Manual de Instalación - Relé Temporizador Multifunción y Multirango GTC-MR"
type: Technical
source: "GTC-MR_MAN_V3.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GTC-MR"
date_processed: "2026-05-09"
---

# Manual de Instalación
## Relé Temporizador Multifunción y Multirango GTC-MR

El GTC-MR es un temporizador con múltiples rangos ajustables y cuatro modos de operación seleccionables: ciclado simétrico (CICLO), pulso o intervalo (PULSO), temporizado a la conexión (TC) y temporizado a la desconexión (TD). En todos los casos, excepto TD, la función se activa al energizar el temporizador. Para TD, se requiere una señal auxiliar para el control de la temporización. Este dispositivo es compatible con voltajes nominales de 120/220 V~.

## Partes y Piezas

- **Orificio para montaje en superficie** (superior e inferior)
- **Contacto NA** (Normalmente Abierto)
- **Contacto Común**
- **Contacto NC** (Normalmente Cerrado)
- **Perilla de Tiempo**
- **Perilla de Rango**
- **Perilla de Modo**
- **LED VERDE** - Indicador de Carga Conectada
- **LED ROJO** - Indicador de Producto Encendido
- **Entrada de control auxiliar (AUX)** - Terminales A1, A2
- **Gancho de sujeción para riel** (dorso del dispositivo)
- **Ranura para montaje de Riel DIN**

## Instalación

### PASO 1: Montaje Mecánico

**Montaje sobre Riel DIN:**
- Coloque el GTC-MR en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GTC-MR y retire el producto del riel.

**Montaje sobre superficie plana:**
- Coloque el GTC-MR sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".
- Dimensiones: 88 mm × 51 mm

### PASO 2: Instalación Eléctrica

**Paso 2.1:** Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

**Paso 2.2:** Conecte los cables de alimentación en 120/220 V~.

**Paso 2.3A - Conexión para los modos de operación:**
- Temporizado a la conexión (TC)
- Ciclado simétrico (CICLO)
- Pulso o intervalo (PULSO)

Conecte el voltaje a controlar o interrumpir al terminal 7 (Contacto Común) y la carga o la salida al contactor al terminal 8 (NA).

**Paso 2.3B - Conexión para el modo de operación:**
- Temporizado a la desconexión (TD)

Para el modo de Operación Temporizado a la Desconexión (TD), se debe realizar la misma conexión indicada en el paso anterior, añadiendo una conexión adicional. El cable de control auxiliar debe conectarse al terminal 2 (AUX).

**Paso 2.4:** Realice el ajuste a la perilla MODO de acuerdo a la forma de trabajo requerida.

**Paso 2.5:** Ajuste la base de tiempo en la que se desea trabajar, mediante la perilla RANGO. Se puede seleccionar en segundos, minutos u horas.

**Paso 2.6:** Configure el tiempo en el que se requiere la temporización, mediante el ajuste de la perilla TIEMPO. Observe que existen 2 escalas en esta perilla (naranja y blanca) relacionadas con el color de la base de tiempo de la perilla RANGO.

**Paso 2.7:** Reconecte la energía eléctrica y verifique el funcionamiento del GTC-MR y del equipo protegido.

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

## Indicadores Luminosos LED

**INDICADOR LED VERDE:**
- **ON:** Carga encendida
- **OFF:** Carga apagada

**INDICADOR LED ROJO:**
- **ON:** Producto encendido
- **OFF:** Producto apagado

## Modos de Operación

### Temporizado a la Conexión (TC)
Al aplicar la alimentación, el relé espera el tiempo de retardo (TR) programado en las perillas de tiempo y rango para luego activar la carga. (Conexión según el punto 3A).

### Pulso o Intervalo (PULSO)
Al aplicar la alimentación, la carga se activa inmediatamente y permanece encendida durante el tiempo de retardo (TR) programado en las perillas de tiempo y rango; luego de transcurrido se desactiva. (Conexión según el punto 3A).

### Ciclado Simétrico (CICLO)
La carga se activa y desactiva de forma cíclica, con tiempos de retardo (TR) iguales de encendido y apagado, según lo programado en las perillas de tiempo y rango. (Conexión según el punto 3A).

### Temporizado a la Desconexión (TD)
La carga se activa con la presencia de la señal de control. Al desaparecer la señal, comienza la temporización de retardo (TR), según lo programado en las perillas de tiempo y rango. Al finalizar la misma, la carga se desactiva. (Conexión según el punto 3B).

*Señal de control auxiliar (AUX) solo para el modo TD.

## Diagrama de Conexión Estándar

- Voltaje a controlar o interrumpir: 120 ó 220 V~
- Conexión en terminales A1 y A2
- Carga o Bobina del contactor en terminal 8 (NA)
- Contacto Común en terminal 7
```