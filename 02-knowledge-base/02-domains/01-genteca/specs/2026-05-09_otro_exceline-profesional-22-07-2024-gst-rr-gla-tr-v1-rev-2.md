```markdown
---
title: "Supervisor Trifásico GST-RR para Refrigeración y Aire Acondicionado"
type: Technical
source: "22-07-2024_GST-RR_GLA_TR_V1_Rev 2.pdf"
product_line: "Exceline Profesional"
document_type: "hoja-especificaciones"
product_code: "GST-RR"
date_processed: "2026-05-09"
---

# Supervisor Trifásico para Refrigeración y Aire Acondicionado

## Descripción del Producto

El Supervisor Trifásico para Refrigeración y Aire Acondicionado GST-RR es un relé electrónico de protección, diseñado para evitar los daños que ocasionan las Fluctuaciones de Voltaje, Desbalance de Voltaje, Pérdidas de Fase, y Corrimiento de Frecuencia en las cargas y compresores trifásicos.

## Aplicaciones

- Aires Acondicionados trifásicos
- Equipos de refrigeración trifásicos

## Protecciones

El GST-RR proporciona protección por:

- Bajo voltaje
- Pérdida de fase
- Desbalance de voltaje
- Sobre voltaje
- Fase invertida
- Corrimiento de frecuencia

## Funciones del Supervisor GST-RR

Si el voltaje trifásico permanece sin fallas y ha transcurrido el temporizado de conexión, el indicador verde se encenderá fijamente señalizando CONECTADO, permitiendo que la carga o circuito de arranque pueda operar.

## Ajustes

Los siguientes ajustes se realizan mediante las perillas. Coloque los valores deseados, tomando en consideración cualquier especificación que indique el fabricante sobre el equipo a proteger:

**Perilla de BAJO VOLTAJE:**
Ajuste el valor del voltaje mínimo permitido para la carga.

**Perilla de ALTO VOLTAJE:**
Ajuste el valor del voltaje máximo permitido para la carga.

**Perilla de TEMPORIZADO A LA CONEXIÓN:**
Ajuste el valor del temporizado de conexión que el supervisor deberá esperar cada vez que se restituye la energía para conectar la carga. Durante este tiempo, el indicador verde estará encendiendo intermitentemente señalizando TEMPORIZADO.

## Descripción de Protecciones

### Protección de Sobre Voltaje
Cuando el voltaje del suministro sea superior al máximo permitido, el indicador de SOBRE VOLTAJE se encenderá fijamente y la carga a proteger permanecerá apagada.

### Protección de Bajo Voltaje
Cuando el voltaje del suministro sea inferior al mínimo permitido, el indicador de BAJO VOLTAJE se encenderá intermitente y la carga a proteger permanecerá apagada.

### Protección de Desbalance de Voltaje
Cuando los voltajes de línea son diferentes entre sí y el porcentaje de desviación con respecto al promedio es mayor al permitido, el indicador de DESBALANCE se encenderá de forma pulsante y la carga a proteger permanecerá apagada.

### Protección de Fase Perdida
Si una de las tres fases se pierde, el indicador de PÉRDIDA DE FASE se encenderá fijamente y la carga a proteger permanecerá apagada.

### Protección de Secuencia Invertida
Si eventualmente las fases llegan en sentido reverso, el indicador FASE INVERTIDA se encenderá intermitente y la carga a proteger permanecerá apagada hasta que se corrija la secuencia entre los cables de las fases.

### Protección por Corrimiento de Frecuencia
Cuando la frecuencia de la línea está fuera de rango, el indicador de CORRIMIENTO DE FRECUENCIA se encenderá de forma pulsante y la carga a proteger permanecerá apagada.

## Especificaciones Técnicas

| Parámetro | GST-RR220 | GST-RR440 |
|-----------|-----------|-----------|
| Voltaje nominal | 208/220 V~ | 440/480 V~ |
| Bajo voltaje permitido, ajustable | 165 - 200 V~ | 350 - 420 V~ |
| Sobre voltaje permitido, ajustable | 230 - 270 V~ | 495 - 575 V~ |
| Pérdida de fase de voltaje | Dispara encima de 33%, restaura debajo de 28% | Dispara encima de 33%, restaura debajo de 28% |
| Desbalance de voltaje | IN ±8%, OUT ±6% | IN ±8%, OUT ±6% |
| Corrimiento de Frecuencia | IN ±3% fn, OUT ±2% fn | IN ±3% fn, OUT ±2% fn |
| Fase invertida | Secuencias: ABC_Normal; CBA_Invertida | Secuencias: ABC_Normal; CBA_Invertida |
| Retardo para desconexión por fase invertida y fase perdida | 0,5 s | 0,5 s |
| Frecuencia de la línea (fn) | 60 Hz | 60 Hz |
| Temporizado de desconexión | 3 s | 3 s |
| Temporizado a la conexión ajustable | 180 a 600 s | 180 a 600 s |
| Capacidad de los contactos de relé SPDT | 3,5 A @ 250 V~ / 1,5 A @ 480 V~ | 3,5 A @ 250 V~ / 1,5 A @ 480 V~ |
| Cableado | 12 a 24 AWG | 12 a 24 AWG |
| Material de la carcasa | ABS y Nylon | ABS y Nylon |
| Temperatura ambiental, límite de operación | -5 a +55 ºC (23° a 131 °F) | -5 a +55 ºC (23° a 131 °F) |
| Humedad relativa máxima | 85% | 85% |
| Dimensiones | 80 mm x 100 mm x 38 mm | 80 mm x 100 mm x 38 mm |
| Peso | 0,116 Kg (0,25 Lb) | 0,116 Kg (0,25 Lb) |

*Nota: El temporizado de desconexión aplica para fallas de voltaje alto, voltaje bajo, desbalance de voltaje y corrimiento de frecuencia.

## Instalación

1. Desconecte el interruptor o fusibles de alimentación.
2. Atornille el GST-RR sobre superficie o móntelo en un riel simétrico.
3. Conecte los cables según el diagrama de conexión.
4. Ajuste las perillas tomando en cuenta las especificaciones del equipo a proteger.
5. Reconecte el interruptor o fusibles de alimentación.

## Diagrama de Conexión

| Condición | Estado 98-95 | Estado 96-95 |
|-----------|-------------|-------------|
| Normal | Conectado | Abierto |
| Falla | Abierto | Conectado |

**Conexión:** L1, L2, L3 conectados al equipo a proteger a través del contactor.

## Aviso de Instalación

Requiere de un contactor para el manejo de la carga (no incluido).

## Alerta de Seguridad

**RIESGO DE CHOQUE ELÉCTRICO: ATENCIÓN**

Antes de cualquier reparación o mantenimiento por parte del personal técnico calificado, se tiene que desconectar de la red de suministro el Supervisor y el equipo.

Para su seguridad y efectos de la garantía, no