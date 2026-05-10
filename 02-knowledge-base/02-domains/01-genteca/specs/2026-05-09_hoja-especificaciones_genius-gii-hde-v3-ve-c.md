```markdown
---
title: "GII+ Relé de Falla de Fase"
type: Technical
source: "GII_HDE_V3_VE_C.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "GII+"
date_processed: "2026-05-09"
---

# GII+ Relé de Falla de Fase

## Descripción General

GII+ es un relé trifásico para Protección contra Fallas de Fase, basado en tecnología de microcontroladores, diseñado específicamente para proteger la carga conectada a la red de distribución contra los daños ocasionados por fallas comunes de voltaje.

GII+ supervisa constantemente los valores de voltaje de la línea; en caso que se presente una condición anormal, el GII+ desactivará la salida hasta que la falla desaparezca y las condiciones del suministro eléctrico se hayan restablecido a niveles aceptables de operación. Temporizadores a la Conexión y a la Desconexión por falla están incorporados a este relé, para prevenir disparos innecesarios debido a las rápidas fluctuaciones del sistema.

## Características Principales

### Medición
- Voltaje
- Frecuencia

### Protección Contra
- Sobre Voltaje/Bajo Voltaje
- Variación de Frecuencia
- Desbalance de Voltaje
- Pérdida de Fase
- Fase Invertida
- Ciclado Corto

### Ajuste de Parámetros
- Sobre Voltaje
- Bajo Voltaje
- Desbalance de Voltaje
- Variación de Frecuencia
- Temporizado a la Desconexión por Falla
- Temporizado a la Conexión después de Falla de Voltaje
- Programador de Horario (Disponible para modelo GII+)
- Modo de Rearme AUTO/MANUAL
- Clave secreta (password)

### Interfaz y Visualización
- Pantalla LCD 16x2 con valores de voltaje
- Cuatro (4) botones pulsadores para el ajuste de Parámetros de Protección (Rearme, Ajuste (2) y Selección)
- Dos (2) Indicadores Luminosos (LED's) para el estado de las salidas e indicación de fallas

### Comunicación
- GIO Port (Protocolo MODBUS RTU, RS485@ 9600 baud)
- Encendido/Apagado Remoto

### Reportes
- Reporte de Voltaje
- Reporte de Valores Ajustados
- Reporte de Modo de Encendido
- Reporte de Ultimas 20 Fallas
- Reporte de Desbalance de Voltaje
- Reporte de Frecuencia de Red

## Funciones y Rangos de Aplicación

| Función | Rango |
|---------|-------|
| Sobre Voltaje | 5% a 20% del Voltaje Nominal |
| Bajo Voltaje | -20% a -5% del Voltaje Nominal |
| Temporizado a la Desconexión por Falla de Voltaje | Ajustable 1 a 30 seg |
| Desbalance de Voltaje | 2% a 20% Voltaje Nominal |
| Pérdida de Fase por Voltaje | IN VUB > 33%, - OUT VUB < 28% |
| Temporizado a la Desconexión por Fase Invertida | < 1 seg |
| Temporizado a la Conexión después de Falla de Voltaje | 0 a 600 seg |
| Variación de Frecuencia | +/-2% a +/-10% de la Frecuencia Nominal |

## Características Físicas

### Opciones de Montaje
- Montaje en Riel Simétrico DIN
- Montaje sobre Superficie Plana, utilizando sujetadores insertables
- Montaje Empotrable (Flush Mounting)

### Especificaciones Constructivas
- Material de la Carcaza: UL94V0
- Una (1) salida de relé SPDT (3A@240 V~ / 1.5A@480 V~)

## Normas Aplicadas

Diseñado conforme a las normas CE (LVD y EMC):
- IEC 61010-1
- IEC 60255-6
- IEC 60947-1
- UL 508

GII+ ha sido desarrollado utilizando la tecnología más avanzada y de acuerdo a las normas para protección IEEE, IEC y NEMA; verificado en conformidad con las normas de compatibilidad electromagnética IEC, por lo que trabaja de manera segura bajo las más severas condiciones eléctricas.

## Información de Seguridad

**ATENCIÓN:** Solamente personal técnico calificado con conocimientos en relés de protección contra fallas de fase y de las conexiones asociadas, debería realizar la instalación, arranque y mantenimiento del sistema. Hacer caso omiso podría resultar en lesiones a personas y/o daños a los equipos conectados.

## Consideraciones de Compatibilidad Electromagnética

**NOTA:** Este producto ha sido diseñado para Ambiente Industrial Severo. De ser utilizado en Ambiente Residencial el usuario podría requerir algunas medidas adicionales.

Se recomienda usar GIO Plug (adaptador opcional) en el GIO PORT.

## Información de Fabricación y Distribución

Fabricado en la REPÚBLICA BOLIVARIANA DE VENEZUELA

**Distribuidor Principal:**
GENTE, GENERACIÓN DE TECNOLOGÍA, C.A.
- R.I.F.: J-00223173-4
- Av. El Buen Pastor, Cruce con Calle Vargas, Edificio Alba, Piso 1, Local 1-A, Boleíta Norte, Caracas, Zona Postal 1070
- Tlf.: +(58)(212) 237.0711 (Master)
- Fax: +(58)(212) 235.2497
- e-mail: genteven@genteca.com.ve
- página web: www.genteca.com.ve

**Distribuidor México:**
PROTECTORES EXCELINE S.A. DE C.V.
- R.F.C.: PEX1806124Y5
- Fernando Zárraga 55, Ciudad Satélite, Naucalpan de Juárez, Edo. de México, C.P. 53100
- Tlf.: +(55) 5572-9200
- e-mail: contacto@exceline.com.mx
- página web: www.exceline.com.mx

**Distribuidor Panamá:**
COMAR TRADING INC.
- R.U.C.: 319589-50908-21 DV-06
- Final Calle 18, Edif. 44, local 4, Zona Libre de Colón, Apartado Postal 030200900
- Tlf.: +(507) 433-1043
- Fax: +(507) 433-2837

---

Modelo: GII+ MV-01-0017-B.01-S
```