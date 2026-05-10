```markdown
---
title: "GII+ Relé Digital para Protección contra Fallas de Fase"
type: Technical
source: "GD-MAN-195-01-V4-E.docx"
product_line: "Genius"
document_type: "manual"
product_code: "GII+"
date_processed: "2026-05-09"
---

# GII+ DESCRIPCIÓN GENERAL

GII+ es un Relé (Relevador) digital para Protección contra Fallas de Fase diseñado para proteger la carga conectada a la red de distribución contra daños ocasionados por fallas comunes de voltaje. Provee una pantalla LCD para indicar el estado de la salida.

## PARTES Y PIEZAS

### Montaje sobre Riel Simétrico DIN

Instrucciones para Montaje Mecánico:

Coloque el GII+ en posición inclinada enganchando la ranura posterior con el Riel, luego empuje presionando el GII+ hasta que haga CLICK.

### Montaje sobre Superficie Plana

Instrucciones para Montaje Mecánico:

a) Saque los dos (2) sujetadores insertables localizados en la parte posterior del GII+, e insértelos dentro de las ranuras verticales que también se encuentran en la parte posterior del GII+.

b) Coloque el GII+ sobre la superficie plana del panel y fíjelo usando tornillos 3/16 x 1/2 pulgadas, empleando un destornillador adecuado.

### Montaje Empotrable (Flush Mounting)

Instrucciones para Montaje Mecánico:

1. Realice el corte del panel de acuerdo a las dimensiones especificadas (Tolerancia: +/-2mm).

2. Remueva los Ganchos Sujetadores para Frontal y el Frontal Insertable. Para remover los Ganchos Sujetadores levántelos suavemente y deslice.

3. Inserte el Frontal del GII+ en el panel.

4. Coloque el GII+ desde la parte posterior y use los Ganchos Sujetadores para Frontal para fijar el GII+ hasta que haga CLICK.

## DIAGRAMA DE CONEXIÓN

### Designación de Terminales

El GII+ cuenta con conexión para:
- 3 fases ~ 50/60 Hz
- Interruptor
- Contactor
- Fusible 5A, 6

## OPERACIÓN

El GII+ supervisa constantemente los valores de voltaje de línea. Cuando una condición de falla dañina ocurre, su salida se desactiva, manteniéndose así hasta que la falla desaparezca totalmente. El GII+ dispone de Temporizador a la Conexión (TC) y a la Desconexión (TD), para prevenir falsos disparos en casos de rápidas y eventuales fluctuaciones de la red.

### Pantalla LCD

GII+ está provisto de pantalla LCD para indicar:
- Las fallas detectadas
- El estado de la salida (voltaje, desbalance, frecuencia y estado de la carga)
- El registro histórico de las últimas 20 fallas detectadas

### Botones Pulsadores

El GII+ dispone de cuatro (4) botones pulsadores:
- Rearme
- Ajuste (2)
- Selección

Estos permiten el ajuste de parámetros eléctricos tales como:
- Voltaje Máximo
- Voltaje Mínimo
- Variación de Frecuencia
- Temporizado a la Desconexión
- Temporizado a la Conexión

### Comunicación

GII+ está provisto de un puerto de Comunicación para lectura de datos por medio de sistemas computarizados (GIO Port, protocolo MODBUS RTU).

## INICIALIZACIÓN

Durante la inicialización de GII+ aparecerá una pantalla de inicio por pocos segundos. Esto permite identificar la versión del firmware.

## AJUSTE DE PANTALLA

### Guía Rápida de Programación para GII+

El dispositivo presenta los siguientes estados operacionales:

- Conectado bajo Modo AUTO
- Desconectado bajo Modo MANUAL
- Desconectado por MODBUS
- Desconectado por Temporizado a la Conexión (TC)
- Desconectado por programación horario

### Pantalla Principal

La Pantalla Principal (N° 1) puede mostrar el estado según el estado de la carga, del GII+ o la existencia de alguna falla, mostrando:
- Valores de voltaje línea a línea (VL1-L2, VL2-L3, VL3-L1)
- Porcentaje de desbalance
- Frecuencia
- Estado de la carga
- Modo de operación (MANUAL/AUTO)

### Tipos de Fallas Detectadas

El GII+ detecta y registra los siguientes tipos de fallas:

- **Bajo Voltaje (UV)**: Voltaje por debajo del valor mínimo configurado
- **Sobre Voltaje (OV)**: Voltaje por encima del valor máximo configurado
- **Desbalance de Voltaje (VUB)**: Desbalance entre fases
- **Pérdida de Fase (VSP)**: Ausencia de una o más fases
- **Fase Invertida (PR)**: Inversión de fase
- **Variación de Frecuencia (FS)**: Desviación de la frecuencia nominal

### Histórico de Fallas

El GII+ mantiene registro de las últimas 20 fallas con:
- Número de la falla
- Fecha de la falla
- Hora de inicio de la falla
- Tipo de falla
- Fases involucradas
- Valor extremo registrado
- Duración de la falla (en minutos)

### Configuración de Botones Pulsadores

**Funciones Especiales:**

- Presione simultáneamente los botones AJUSTE+SELECCIÓN para entrar al menú (pantalla 5). Si el producto está protegido, introduzca la Clave.
- Presione simultáneamente los botones AJUSTE+REARME para activar la opción de Salida Rápida.
- Presione SELECCIÓN para validar el Valor de Ajuste a seleccionar.
- Presione simultáneamente REARME+AJUSTE para activar la Pantalla 0 de Inicio.

### Menú Principal de Ajustes

Acceda a las siguientes opciones:

- AJUSTE VOLTAJE
- AJUSTE RELOJ
- PROG. HORARIO
- MODO DE REARME
- CAMBIO DE CLAVE
- DIRECCIÓN MODBUS
- BORRAR HISTÓRICO
- SALIR

### Guía de Ajustes de Programación Horaria

Solo los modelos GII+ con programación de eventos tienen las opciones de menú "AJUSTE RELOJ" y "PROG. HORARIO" que permiten configurar eventos y días feriados.
```