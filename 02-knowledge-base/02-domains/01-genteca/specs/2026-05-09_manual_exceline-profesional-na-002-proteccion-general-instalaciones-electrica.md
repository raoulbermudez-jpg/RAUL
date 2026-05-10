---
title: "¿Cómo proteger tu planta eléctrica ante las fallas en la red eléctrica?"
type: Technical
source: "NA-002-Proteccion-General-Instalaciones-Electrica.pdf"
product_line: "Exceline Profesional"
document_type: "nota-aplicacion"
product_code: "GST, GSML, GMP5-3540"
date_processed: "2026-05-09"
---

# ¿Cómo proteger tu planta eléctrica ante las fallas en la red eléctrica?

## Introducción

Las plantas eléctricas son equipos de respaldo, de uso cada vez más frecuente, que garantizan el suministro eléctrico en caso de que ocurra un corte en la red eléctrica, el cual puede ser programado o consecuencia de una falla eléctrica como apagones, flickers, voltajes altos y bajos, entre otras. 

Este tipo de dispositivos cuentan con un componente llamado Automatic Transfer Switch (ATS) o transferencia para el arranque automático, que detecta cuando hay una interrupción en el suministro eléctrico y genera la instrucción para activar la planta eléctrica. Asimismo, el ATS se encarga del proceso de retorno, es decir, identificar cuando la red eléctrica se ha reestablecido para generar la instrucción para el cambio de suministro a la red convencional y el apagado de la planta eléctrica. 

Estos sistemas de control son susceptibles a dañarse debido a las fallas del servicio eléctrico, tanto en la detección como en el retorno de la energía eléctrica.

## Solución Propuesta

Esta solución se basa en el monitoreo constante de la red eléctrica mediante supervisores de voltaje monofásicos (GSML) o trifásicos (GST), para evitar que señales fuera de los límites aceptables de bajo voltaje y sobre voltaje lleguen al sistema de control.

Se plantean dos opciones para instalar los supervisores:

1. Señal de control del supervisor conectada al sistema de control de la planta eléctrica.
2. El supervisor controlando la entrada de la energía eléctrica, esto se realiza con un contactor antes del ATS.

## Descripción de los Productos

**GST:** Supervisor de trifásico para sistemas eléctricos. Protege contra voltaje alto y bajo, desbalance, fase perdida y fase invertida. Permite configurar el umbral de detección de voltaje alto y bajo, como el tiempo de conexión y desconexión.

**GSML:** Supervisor para sistemas eléctricos monofásicos. Protege contra voltaje alto y bajo. Permite configurar el umbral de detección de voltaje bajo con tiempo de conexión fijo en 3 min.

**GMP5-3540:** Supresor de picos de alta energía producidas tanto por descargas atmosféricas como internas por la conexión y desconexión de subestaciones eléctricas o grandes máquinas eléctricas. Corriente máxima de descarga 70 kA, con tiempo de respuesta menor a 25 ns. Indicador de estatus.

## Opciones de Instalación

### Opción 1: Supervisión del Sistema Eléctrico Integrada al Sistema de Control de la Planta Eléctrica

En este caso, es importante contar con la experticia del personal técnico de la planta eléctrica ya que conoce el funcionamiento del Automatic Transfer Switch, e identificará la señal de control a intervenir. 

El planteamiento es colocar la salida de control del o los supervisores (GSML o GST) en serie con el sistema de control de la planta. Esto habilitará el funcionamiento de la planta eléctrica en función de las fallas eléctricas, y solo permitirá la desconexión cuando las condiciones del voltaje eléctrico regresen a la normalidad y se mantengan estables por un periodo aceptable.

- **a. Plantas eléctricas bifásicas**
- **b. Plantas eléctricas trifásicas**

### Opción 2: Sistema de Protección en la Entrada de la Red Eléctrica (Caja de Protección)

En este caso, se propone un sistema de supervisión en la entrada de la red eléctrica, el cual solo permitirá el paso de la energía eléctrica al ATS con valores aceptables para el funcionamiento y desconectará esta cuando exista una falla eléctrica. 

Es importante definir el contactor apropiado de acuerdo a la carga máxima que soporta el sistema respaldado. Adicionalmente, se considera pertinente incluir la supresión de picos con los módulos GMP-5-35 conectados entre fase y tierra, uno por fase. Esto evitará que el ATS o la planta eléctrica se vea afectada por las descargas atmosféricas o por el pico que se genera con conexión y desconexión de las subestaciones eléctricas.

- **a. Plantas eléctricas bifásicas - Caja de protección**
- **b. Plantas eléctricas trifásicas - Caja de protección**

## Recomendaciones

Para sistemas trifásicos supervisados con GST, asegúrese de que las perillas del equipo estén configuradas de la siguiente manera:

| Parámetro | Valor |
|-----------|-------|
| Voltaje Bajo | 10% menos del voltaje nominal |
| Voltaje Alto | 10% más del voltaje nominal |
| Tiempo de detección | 0,5 segundos (mínimo) |
| Tiempo de conexión | 20 segundos |

## Información Adicional

En caso de cualquier inquietud, contactar directamente a través del correo: info@genteca.com.ve