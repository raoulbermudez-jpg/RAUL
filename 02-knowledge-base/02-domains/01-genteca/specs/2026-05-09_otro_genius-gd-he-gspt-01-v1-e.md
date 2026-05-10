```markdown
---
title: "Relé de Protección para Bombas Sumergibles GSPT"
type: Technical
source: "GD-HE-GSPT-01-V1-E.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "GSPT"
date_processed: "2026-05-09"
---

# Relé de Protección para Bombas Sumergibles GSPT

## Características Generales

GSPT es un Relé (Relevador) trifásico para Protección de Bombas Sumergibles basado en tecnología de microcontroladores, diseñado especialmente para proteger motores con clase térmica 10, contra los daños ocasionados por fallas comunes de corriente y voltaje.

GSPT supervisa constantemente la Corriente de Consumo del Motor y los principales parámetros eléctricos tales como el Voltaje de Línea, Frecuencia de Red, Potencia Aparente, Potencia Real, Factor de Potencia y Consumo de energía. En caso de presentarse una condición anormal de falla, GSPT desactivará su salida hasta que la falla desaparezca y el motor se haya enfriado completamente. Temporizadores a la Conexión y a la Desconexión por Falla están incorporados a este relé para prevenir disparos innecesarios debido a las rápidas fluctuaciones del sistema.

GSPT excede la protección convencional de Bombas Sumergibles, proporcionando las siguientes prestaciones:

- Provee protección fija contra eventos de Rotor Bloqueado acelerado.
- Posibilita al usuario ajustar el Temporizado de Conexión, después de Sobrecarga.
- Limita la cantidad máxima de arranques falsos permitidos, por hora de servicio, según la capacidad del motor en HP.

GSPT está provisto de una Pantalla de Cristal Líquido (LCD) que indica el estado de los parámetros eléctricos de corriente y voltaje del motor así como la indicación de fallas por variaciones de corriente, voltaje, frecuencia, desbalances, pérdidas de fase, fase invertida, etc. Dispone de cuatro (4) botones pulsadores (1 de Rearme, 2 de Ajustes y 1 de Selección) para el ajuste de parámetros eléctricos de protección y operación así como un puerto de comunicaciones con Protocolo MODBUS RTU.

Un diseño mecánico innovador permite dos (2) opciones de montaje:

- Montaje en Riel Simétrico DIN.
- Montaje en Superficie Plana utilizando sujetadores insertables.

GSPT ha sido desarrollado usando la más avanzada tecnología, diseñado de acuerdo a las normas para protección IEEE, IEC y NEMA.

## Medición de

- Corriente
- Voltaje
- Frecuencia
- Factor de Potencia (PF)
- Potencia Aparente (kVA)
- Potencia Real (kW)
- Consumo de Energía (kWH)

## Protección Contra

- Excesos de arranques falsos (Límite de veces según la potencia del motor)
- Sobrecarga
- Subcarga
- Sobre Voltaje / Bajo Voltaje
- Variación de Frecuencia
- Desbalance de Voltaje
- Desbalance de Corriente
- Pérdida de Fase
- Fase Invertida
- Rotor Bloqueado
- Temporizado a la Desconexión por Falla
- Temporizado a la Conexión después de Falla de Voltaje

## Ajuste de

- Sobrecarga
- Subcarga por límite inferior de corriente
- Sobre Voltaje
- Bajo Voltaje
- Desbalance de Corriente
- Frecuencia

## Características Físicas

- Montaje sobre Superficie Plana, Montaje sobre Din-Rail o Montaje Empotrable en Panel (Flush Mounting)
- Pantalla Cristal Líquido (LCD) 16x2, para indicación de valores de corriente y voltaje así como reportes del estado de la carga
- Cuatro (4) botones pulsadores para ajustes de parámetros de operación y de protección (uno de REARME, dos de AJUSTE y uno de SELECCIÓN)
- Modo de Rearme AUTO/MANUAL
- Material de la Carcasa UL94V0
- Dos (2) salidas de relé contrapuestas, DPST 1.0A@240V~ / 0.5A@480V~
- Disponibles con CT Interno

## Comunicación

- GIO Port (Protocolo MODBUS RTU)
- Encendido/Apagado Remoto
- Retención de parámetros configurados, al generarse fallas, con posibilidad de ser vistos en un computador PC

## Reportes

- Reporte de Voltaje y Corriente
- Reporte de PF, KVA, KWH y KW
- Reporte de Valores Ajustados
- Reporte de Tiempo acumulado de trabajo del Motor
- Reporte del Modo de Encendido
- Reporte de Últimas 80 Fallas
- Reporte de Frecuencia de Red

## Otros

- Memoria Térmica

## Normas de Diseño

**Conforme a las Normas CE (LVD y EMC):**
- IEC 61010-1
- IEC 60255-6
- IEC 60255-8
- IEC 60947-1

**Diseñado según Norma:**
- UL 508
- IEEE C37.112
- NEMA MG10

## Funciones Generales & Rango de Aplicaciones

El GSPT proporciona protección eléctrica por medio de las funciones generales y rangos de ajustes indicados a continuación:

| Función | Rango |
|---------|-------|
| Sobre Voltaje | 5% a 20% del Voltaje Nominal |
| Bajo Voltaje | -20% al -5% del Voltaje Nominal |
| Desbalance de Voltaje | 2% al 10% del Voltaje Nominal |
| Pérdida de Fase por Voltaje | IN 33% - OUT 28% |
| Temporizado a la Desconexión por Fase Invertida | < 1 s |
| Temporizado a la Conexión, después de Falla de Voltaje | 0 a 600 s |
| Temporizado a la Desconexión por Falla de Voltaje | 1 a 30 s |
| Detección Variación de Frecuencia | +/-2% al +/-10% Frecuencia Nominal |
| Ajuste Nivel de Sobrecarga | 5% al 50% |
| Detección de Subcarga | Límite inferior ajustable, relativo a I nominal |
| Temporizado a la conexión, después de Sobrecarga | 10 a 60 min., ajustable por el usuario |
| Desbalance de Corriente | CUB > 48% |
| Pérdida de Fase por Corriente | CUB > 60% |
| Clase Térmica IEC 60255-8 | 10 |
```