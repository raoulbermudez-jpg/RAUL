---
title: "Relé Temporizador Multifunción y Multirango GTC-MR"
type: Technical
source: "GTC-MR_MAN_V1_REV1.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GTC-MR"
date_processed: "2026-05-09"
---

# Relé Temporizador Multifunción y Multirango GTC-MR

## Descripción General

El GTC-MR es un temporizador con múltiples rangos ajustables y cuatro modos de operación seleccionables:

- Ciclado simétrico (CICLO)
- Pulso o intervalo (PULSO)
- Temporizado a la conexión (TC)
- Temporizado a la desconexión (TD)

En todos los casos, excepto TD, la función se activa al energizar el temporizador. Para TD, se requiere una señal auxiliar para el control de la temporización. Este dispositivo es compatible con voltajes nominales de 120/220 V ̴.

## Configuración de Operación

### Selección del Modo de Operación

Verifique el modo de operación requerido y de acuerdo a esto siga el paso 3A o 3B.

**Modos disponibles:**
- Temporizado a la conexión (TC)
- Ciclado simétrico (CICLO)
- Pulso o intervalo (PULSO)
- Temporizado a la desconexión (TD)

### Conexiones por Modo de Operación

**Para TC, CICLO y PULSO:**
Realice la conexión según el punto 3A.

**Para Temporizado a la Desconexión (TD):**
Realice la misma conexión indicada en el paso anterior, añadiendo una conexión adicional. El cable de control auxiliar debe conectarse al terminal 2 (AUX).

## Ajuste de Parámetros

### Perilla MODO
Realice el ajuste de la perilla MODO de acuerdo a la forma de trabajo requerido.

### Perilla RANGO
Ajuste la base de tiempo en la que se desea trabajar. Se puede seleccionar en:
- Segundos
- Minutos
- Horas

### Perilla TIEMPO
Configure el tiempo en el que se requiere la temporización, mediante el ajuste de la perilla TIEMPO. Existen 2 escalas en esta perilla (naranja y blanca) que están relacionadas con el color de la base de tiempo de la perilla RANGO.

## Tabla de Modos de Operación

| Modo | Descripción | Conexión |
|------|-------------|----------|
| **TC - Temporizado a la Conexión** | Al aplicar la alimentación, el relé espera el tiempo programado (TR) en las perillas de tiempo y rango para luego activar la carga. | 3A |
| **TD - Temporizado a la Desconexión** | La carga se activa con la presencia de la señal de control. Al desaparecer la señal, comienza la temporización (TR), según lo programado en las perillas de tiempo y rango. Al finalizar la misma, la carga se desactiva. | 3B |
| **CICLO - Ciclado Simétrico** | La carga se activa y desactiva de forma cíclica, con tiempos (TR) iguales de encendido y apagado, según lo programado en las perillas de tiempo y rango. | 3A |
| **PULSO - Pulso o Intervalo** | Al aplicar la alimentación, la carga se activa inmediatamente y permanece encendida durante el tiempo programado (TR) en las perillas de tiempo y rango, luego de transcurrido se desactiva. | 3A |