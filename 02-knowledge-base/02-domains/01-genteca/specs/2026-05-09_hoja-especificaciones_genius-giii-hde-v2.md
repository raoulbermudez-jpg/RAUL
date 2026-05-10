```markdown
---
title: "Genius GIII - Relé de Protección Total de Motores"
type: Technical
source: "GIII_HDE_V2.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "GIII"
date_processed: "2026-05-09"
---

# Genius GIII - Relé de Protección Total de Motores

Genius GIII es un Relé trifásico para Protección Total de Motores basado en tecnología de microcontroladores, diseñado especialmente para proteger motores contra los daños ocasionados por fallas comunes de corriente y voltaje.

Genius GIII supervisa constantemente la Corriente de consumo del Motor y los principales parámetros eléctricos tales como el Voltaje de Línea, Frecuencia de Red, Potencia Aparente, Potencia Real, Factor de Potencia y Consumo de Energía. En caso de presentarse una condición anormal de falla, Genius GIII desactivará su salida hasta que la falla desaparezca y el motor se haya enfriado completamente. Temporizadores a la Conexión y a la Desconexión por Falla están incorporados a este relé para prevenir disparos innecesarios debido a las rápidas fluctuaciones del sistema.

Genius GIII está provisto de una Pantalla de Cristal Líquido (LCD) que indica el estado de los parámetros eléctricos de corriente y voltaje del motor así como la indicación de fallas por variaciones de corriente, voltaje, frecuencia, desbalances, pérdidas de fase, fase invertida, etc. Dispone de cuatro (4) botones pulsadores (1 de Rearme, 2 de Ajustes y 1 de Selección) para el ajuste de parámetros eléctricos de protección y operación así como un puerto de comunicaciones con Protocolo MODBUS RTU.

Un diseño mecánico innovador permite tres (3) opciones de montaje:
- Montaje en Riel Simétrico DIN
- Montaje en Superficie Plana utilizando sujetadores insertables
- Montaje Empotrable (Flush Mounting)

Genius GIII ha sido desarrollado usando la más avanzada tecnología, diseñado de acuerdo a las normas para protección IEEE, IEC y NEMA; verificado en conformidad con las normas de compatibilidad electromagnética IEC, por lo que trabaja de manera segura en ambientes con las más severas condiciones eléctricas.

## Características Generales

### Medición de:
- Corriente
- Voltaje
- Frecuencia
- Factor de Potencia (PF), Potencia Aparente (kVA), Potencia Real (kW) y Consumo de Energía (kWH)
- Temperatura

### Protección contra:
- Sobrecarga / Subcarga
- Sobre Voltaje / Bajo Voltaje
- Variación de Frecuencia
- Desbalance de Voltaje
- Desbalance de Corriente
- Pérdida de Fase
- Fase Invertida
- Rotor Bloqueado

### Ajuste de:
- Sobrecarga
- Subcarga
- Sobre Voltaje
- Bajo Voltaje
- Desbalance de Corriente
- Desbalance de Voltaje
- Frecuencia
- Temporizado a la Desconexión por Falla
- Temporizado a la Conexión después de Falla de Voltaje
- Clase Térmica del Motor
- Ajuste de Reloj
- Ajuste para cargas de Alta Inercia
- Programador de Horario (eventos semanales & días especiales)
- Modo de Rearme AUTO/MANUAL
- Clave Secreta (Password)

### Comunicación:
- GIO Port ó Salida RS485 @ 9600 baud (Protocol MODBUS RTU)
- Estado de las Entradas Digitales
- Encendido/Apagado Remoto

### Reportes:
- Reporte de Voltaje y Corriente
- Reporte de PF, KVA, KWH y KW
- Reporte de Valores Ajustados
- Reporte de Tiempo acumulado de trabajo del Motor
- Reporte del Modo de Encendido
- Reporte de Últimas 20 Fallas
- Reporte de Frecuencia de Red
- Reporte de Temperatura del Motor

### Características Físicas:
- Montaje sobre Superficie Plana, Montaje sobre Din-Rail o Montaje Empotrable en Panel (Flush Mounting)
- Pantalla Cristal Líquido (LCD), 16x2, para indicación de valores de corriente y voltaje así como reportes del estado de la carga
- Cuatro (4) botones pulsadores para ajustes de parámetros de operación y de protección (uno de REARME, dos de AJUSTE y uno de SELECCIÓN)
- Material de la Carcaza UL94V0
- Dos (2) salidas de Relé tipo SPDT (3A@240 VAC / 1.5A@480 VAC)
- Dos (2) Entradas tipo Digital
- Una (1) Entrada tipo Analógica para temperatura (sensor PTC100)
- Disponibles con CT Interno ó para conexión con CT externos

### Otros:
- Memoria Térmica

## Normas de Producto Aplicadas

Diseñado conforme a las Normas CE (LVD y EMC):
- IEC 61010-1
- IEC 60255-6
- IEC 60255-8
- IEC 60947-1

Diseñado según Norma:
- UL 508
- IEEE C37.112

## Funciones Generales & Rango de Aplicaciones

El GIII proporciona protección eléctrica por medio de las siguientes funciones generales y rangos de ajustes:

| Función | Rango |
|---------|-------|
| Sobre Voltaje | 5% a 20% del Voltaje Nominal |
| Bajo Voltaje | -20% al -5% del Voltaje Nominal |
| Desbalance de Voltaje | 2% al 10% del Voltaje Nominal |
| Pérdida de Fase por Voltaje | IN 33% - OUT 28% |
| Temporizado a la Desconexión por Fase Invertida | < 1 seg |
| Temporizado a la Conexión, después de Falla de Voltaje | 0 a 600 seg |
| Temporizado a la Desconexión por Falla de Voltaje | 1 a 30 seg |
| Detección Variación de Frecuencia | +/-2% al +/-10% Frecuencia Nominal |
| Ajuste Nivel de Sobrecarga | Ajustable |
| Detección de Subcarga | 5% al 50% |
| Desbalance de Corriente | Ajustable por PF o por I nominal |
| Pérdida de Fase por Corriente | CUB > 48% |
| Detección de Factor de Potencia | CUB > 60% |
| Clase Térmica IEC 60255-8 | 0.0 al 1.0 |
```