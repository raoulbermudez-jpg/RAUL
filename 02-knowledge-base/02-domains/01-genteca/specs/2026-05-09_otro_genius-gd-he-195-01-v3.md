```markdown
---
title: "Genius GII - Relé de Falla de Fase"
type: Technical
source: "GD-HE-195-01-V3.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "GII"
date_processed: "2026-05-09"
---

# Genius GII - Relé de Falla de Fase

## Descripción General

Genius GII es un relé trifásico para Protección contra Fallas de Fase, basado en tecnología de microcontroladores, diseñado específicamente para proteger la carga conectada a la red de distribución contra los daños ocasionados por fallas comunes de voltaje.

Genius GII supervisa constantemente los valores de voltaje de la línea; en caso que se presente una condición anormal, el Genius GII desactivará la salida hasta que la falla desaparezca y las condiciones del suministro eléctrico se hayan restablecido a niveles aceptables de operación. Temporizadores a la Conexión y a la Desconexión por falla están incorporados a este relé, para prevenir disparos innecesarios debido a las rápidas fluctuaciones del sistema.

## Características Principales

### Medición de:
- Voltaje
- Frecuencia

### Protección contra:
- Sobre Voltaje / Bajo Voltaje
- Variación de Frecuencia
- Desbalance de Voltaje
- Pérdida de Fase
- Fase Invertida
- Ciclado Corto

### Ajuste de:
- Sobre Voltaje
- Bajo Voltaje
- Desbalance de Voltaje
- Variación de Frecuencia
- Temporizado a la Desconexión por Falla
- Temporizado a la Conexión después de Falla de Voltaje
- Programador de Horario (Disponible para modelo GII+)
- Modo de Rearme AUTO/MANUAL
- Clave secreta (password)

### Comunicación:
- GIO Port (Protocolo MODBUS RTU, RS485 @ 9600 baud)
- Encendido/Apagado Remoto

### Reportes:
- Reporte de Voltaje
- Reporte de Valores Ajustados
- Reporte de Modo de Encendido
- Reporte de Ultimas 20 Fallas
- Reporte de Desbalance de Voltaje
- Reporte de Frecuencia de Red

## Funciones y Rangos de Protección

| Función | Rango |
|---------|-------|
| Sobre Voltaje | 5% a 20% del Voltaje Nominal |
| Bajo Voltaje | -20% a -5% del Voltaje Nominal |
| Temporizado a la Desconexión por Falla de Voltaje | Ajustable 1 a 30 seg |
| Desbalance de Voltaje | 2% a 20% Voltaje Nominal |
| Pérdida de Fase por Voltaje | IN VUB > 33%, OUT VUB < 28% |
| Temporizado a la Desconexión por Fase Invertida | < 1 seg |
| Temporizado a la Conexión después de Falla de Voltaje | 0 a 600 seg |
| Variación de Frecuencia | +/-2% a +/-10% de la Frecuencia Nominal |

## Características Físicas

- **Montaje:** Tres opciones disponibles
  - Montaje en Riel Simétrico DIN
  - Montaje sobre Superficie Plana, utilizando sujetadores insertables
  - Montaje Empotrable (Flush Mounting)

- **Pantalla:** LCD 16x2 con valores de voltaje

- **Controles:** Cuatro (4) botones pulsadores para el ajuste de Parámetros de Protección (Rearme, Ajuste (2) y Selección)

- **Indicadores:** Dos (2) Indicadores Luminosos (LED's) para el estado de las salidas e indicación de fallas

- **Material de la Carcaza:** UL94V0

- **Salida:** Una (1) salida de relé SPDT (3A @ 240 VAC / 1.5A @ 480 VAC)

## Normas de Producto Aplicadas

Diseñado conforme a las normas CE (LVD y EMC):
- IEC 61010-1
- IEC 60255-6
- IEC 60947-1
- UL 508

Genius GII ha sido desarrollado de acuerdo a las normas para protección IEEE, IEC y NEMA; verificado en conformidad con las normas de compatibilidad electromagnética IEC, por lo que trabaja de manera segura bajo las más severas condiciones eléctricas.

## Información de Seguridad

**ATENCIÓN:** Solamente personal técnico calificado con conocimientos en relés de protección contra fallas de fase y de las conexiones asociadas, debería realizar la instalación, arranque y mantenimiento del sistema. Hacer caso omiso podría resultar en lesiones a personas y/o daños a los equipos conectados.

## Notas Adicionales

- Este producto ha sido diseñado para Ambiente Industrial Severo
- Usar GIO Plug (adaptador opcional) para GIO PORT si es necesario
- Genius GII está provisto de pantalla LCD para indicar el estado de la salida (voltaje, desbalance, frecuencia y status de la carga)
- Incluye un puerto de comunicaciones con protocolo MODBUS RTU

---

**Fabricante:** GENTE, GENERACIÓN DE TECNOLOGÍA, C.A. (República Bolivariana de Venezuela)

**Distribuidores:**
- México: PROTECTORES EXCELINE S.A. DE C.V.
- Panamá: COMAR TRADING INC.
```