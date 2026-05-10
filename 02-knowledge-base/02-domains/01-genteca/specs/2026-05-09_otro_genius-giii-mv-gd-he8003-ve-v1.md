```markdown
---
title: "Relé de Protección GIII+MV - Total de Motores"
type: Technical
source: "GIII+MV GD-HE8003-VE-V1.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "GIII+MV"
date_processed: "2026-05-09"
---

# Relé de Protección GIII+MV - Total de Motores

## Descripción General

GIII+MV es un Relé (Relevador) trifásico para Protección Total de Motores basado en tecnología de microcontroladores, diseñado especialmente para proteger motores contra los daños ocasionados por fallas comunes de corriente y voltaje.

Este dispositivo supervisa constantemente la Corriente de consumo del Motor y los principales parámetros eléctricos tales como el Voltaje de Línea, Frecuencia de Red, Potencia Aparente, Potencia Real, Factor de Potencia y consumo de Energía. En caso de presentarse una condición anormal de falla, el GIII+MV desactivará su salida hasta que la falla desaparezca y el motor se haya enfriado completamente. 

Temporizadores a la Conexión y a la Desconexión por Falla están incorporados a este relé (relevador) para prevenir disparos innecesarios debido a las rápidas fluctuaciones del sistema.

## Esquema de Medición Multivoltaje

GIII+MV contiene un esquema de medición multivoltaje, mediante el cual un mismo modelo permite ser configurado para operar con diferentes suministros nominales:

**Voltajes estándares:** 208, 220, 230, 240, 400, 440, 480 V~

**Voltajes especiales:** 200, 420, 460 V~

El dispositivo limita la cantidad máxima de arranques falsos permitidos, por hora de servicio, según la capacidad del motor en HP.

## Características de Visualización y Control

GIII+MV está provisto de una Pantalla de Cristal Líquido (LCD) que indica el estado de los parámetros eléctricos de corriente y voltaje del motor así como la indicación de fallas por variaciones de corriente, voltaje, frecuencia, desbalances, pérdidas de fase, fase invertida, etc. 

Dispone de cuatro (4) botones pulsadores (1 de Rearme, 2 de Ajustes y 1 de Selección) para el ajuste de parámetros eléctricos de protección y operación, así como un puerto de comunicaciones con Protocolo MODBUS RTU.

## Opciones de Montaje

Un diseño mecánico innovador permite tres (3) opciones de montaje:

- Montaje en Riel Simétrico DIN
- Montaje en Superficie Plana utilizando sujetadores insertables
- Montaje Empotrable (Flush Mounting)

## Conformidad Normativa

GIII+MV ha sido desarrollado usando la más avanzada tecnología, diseñado de acuerdo a las normas para protección IEEE, IEC y NEMA; verificado en conformidad con las normas de compatibilidad electromagnética IEC, por lo que trabaja de manera segura en ambientes con las más severas condiciones eléctricas.

## Características Generales

### Medición

- Corriente
- Voltaje
- Frecuencia
- Factor de Potencia (PF)
- Potencia Aparente (kVA)
- Potencia Real (kW)
- Consumo de Energía (kWH)
- Temperatura
- Desbalance de Voltaje
- Desbalance de Corriente
- Pérdida de Fase

### Protección Contra

- Excesos de arranques falsos (Límite de veces según la potencia del motor)
- Sobrecarga / Subcarga
- Sobre Voltaje / Bajo Voltaje
- Variación de Frecuencia
- Desbalance de Voltaje
- Fase Invertida
- Rotor Bloqueado
- Relé desviado
- Desbalance de Corriente

### Ajustes

- Sobrecarga
- Subcarga
- Sobre Voltaje
- Bajo Voltaje
- Temperatura
- Desbalance de Corriente
- Desbalance de Voltaje
- Frecuencia
- Temporizado a la Desconexión por Falla
- Temporizado a la Conexión después de Falla de Voltaje
- Temporizado a la Conexión después de Sobrecarga
- Clase Térmica del Motor
- Ajuste de Reloj
- Ajuste para cargas de Alta Inercia
- Programador Horario (eventos semanales & días especiales)
- Modo de Rearme AUTO/MANUAL
- Clave Secreta (Password)

### Características Físicas

- Montaje sobre Superficie Plana, Montaje sobre Din-Rail o Montaje Empotrable en Panel (Flush Mounting)
- Pantalla Cristal Líquido (LCD), 16x2, para indicación de valores de corriente y voltaje así como reportes del estado de la carga
- Cuatro (4) botones pulsadores para ajustes de parámetros de operación y de protección (uno de REARME, dos de AJUSTE y uno de SELECCIÓN)
- Material de la Carcaza UL94V0
- Dos (2) salidas de Relé tipo SPDT (3A@240V~ / 1.5A@480 V~)
- Dos (2) Entradas tipo Digital
- Una (1) Entrada tipo Analógica para temperatura (sensor PTC100)
- Disponibles con CT Interno ó para conexión con CT externos

### Comunicación

- GIO Port ó Salida RS485@ 9600, 19200, 38400 baud (Protocol MODBUS RTU)

### Reportes

- Reporte de Voltaje y Corriente
- Reporte de PF, KVA, KWH y KW
- Reporte de Valores Ajustados
- Reporte de Tiempo acumulado de trabajo del Motor
- Reporte del Modo de Encendido
- Reporte de Últimas 100 Fallas
- Reporte de Frecuencia de Red
- Reporte de Temperatura del Motor
- Estado de las Entradas Digitales
- Encendido/Apagado Remoto
- Memoria Térmica

## Normas de Producto Aplicadas

**Diseñado conforme a las Normas CE (LVD y EMC):**
- IEC 61010-1
- IEC 60255-6
- IEC 60255-8
- IEC 60947-1

**Diseñado según Norma:**
- UL 508
- IEEE C37.112

## Funciones Generales de Protección

El GIII+MV proporciona protección eléctrica por medio de las siguientes funciones y rangos de ajustes:

| Función | Rango |
|---------|-------|
| Sobre Voltaje | 5% a 20% del Voltaje Nominal |
| Bajo Voltaje | -20% al -5% del Voltaje Nominal |
| Desbalance de Voltaje | 2% al 10% del Voltaje Nominal |
| Pérdida de Fase por Voltaje | Falla VUB> 33% - Acepta VUB < 28% |
| Temporizado a la Desconexión por Fase Invertida | < 1 s |
| Temporizado a la Conexión, después de Falla de Voltaje | 0 a 600 s |
| Temporizado a la Desconexión por Falla de Voltaje | 1 a 30 s |
| Detección Variación de Frecuencia | +/-2%