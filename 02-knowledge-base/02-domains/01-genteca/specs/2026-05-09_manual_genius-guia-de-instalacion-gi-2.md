---
title: "GI+ Guía de Instalación"
type: Technical
source: "Guia de Instalacion GI+ (2).pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GI+"
date_processed: "2026-05-09"
---

# GI+ GUÍA DE INSTALACIÓN

## ALERTA DE SEGURIDAD

Solo personal técnico calificado con conocimientos en relés (relevadores) de protección y la carga asociada debería realizar la instalación, arranque y mantenimiento del sistema. Hacer caso omiso podría resultar en lesiones a personas y/o daños a los equipos conectados.

## GI+ PARTES Y PIEZAS

### Vista Frontal
1. **Indicadores Luminosos (LEDs)**
   - Luz Fija - CONECTADO (ON)
   - Luz Intermitente - TEMPORIZADO (TC) a la Conexión
   - LED Verde
   - LED Rojo - Luz Fija - FALLA

2. **Pantalla LCD**

3. **Botón Pulsador de Rearme (Arranque)**

4. **Botones Pulsadores para Ajustes**

5. **Botón Pulsador para Selección**

6. **Frontal Insertable para Flush Mounting**

7. **Gancho Sujetador para Frontal**

### Vista Posterior
8. **Ranura posterior para montaje en Riel simétrico**

9. **Sujetador Insertable para Montaje en Superficie Plana**

10. **Gancho de Retención para montaje en Riel simétrico**

11. **Terminales Enchufables**

12. **GIO PORT (Puerto de Comunicación)**

13. **Cubierta plástica protectora del GIO PORT**

(*) Accesorio se vende por separado.

## GI+ DIMENSIONES GENERALES

- **Largo:** 105 mm
- **Ancho:** 90 mm (85 mm para Guía para Superficie Plana)
- **Alto:** 86 mm (99 mm para Guía para Superficie Plana)

## CARACTERÍSTICAS PRINCIPALES

GI+ está provisto de pantalla LCD para indicar las fallas, el estado de la salida (voltaje, desbalance, frecuencia y estado de la carga) y el registro histórico de las últimas 20 fallas detectadas. También dispone de cuatro (4) botones pulsadores (Rearme, Ajuste (2) y Selección) para el ajuste de parámetros eléctricos tales como Voltaje Máximo, Voltaje Mínimo, Variación de Frecuencia, Temporizado a la Desconexión y Temporizado a la Conexión. GI+ está provisto de un puerto de Comunicación para lectura de datos por medio de sistemas computarizados (GIO Port, protocolo MODBUS RTU).

## GI+ ESPECIFICACIONES TÉCNICAS

### A) Fuente de Poder

| Parámetro | Valor |
|-----------|-------|
| Voltaje de Operación, Ue | 120 / 208/220 / 440/480 V~ |
| Límite de Operación de Voltaje, Ue | 72-168 / 145-312 / 264-672 V~ |
| Consumo Promedio, In | 44 mA |
| Frecuencia de Operación | 42-70 Hz |
| Modo de Operación | Continuo |

### B) Condiciones Ambientales, Límites de Operación e Instalación

| Parámetro | Valor | Norma |
|-----------|-------|-------|
| Temperatura Ambiental (Almacenaje) | -10 ºC a +70 ºC (14 ºF a 158 ºF) | |
| Humedad Relativa Máxima | 85% R.H. | |
| Protección a Objetos/Agua | IP20, Protegido contra objetos > 12.5 mm, ninguna protección contra agua | IEC 60529 |
| Nivel de Contaminación | Grado 3 | IEC 60255-5 |
| Protección contra Exceso de Voltaje | Categoría III, 4 KV | IEC 60255-5 |
| Voltaje de Aislamiento Nominal | 500 V | UL IEC 60255-5 |
| Prueba de Impulso | 5 KV | IEC 60255-5 |
| Prueba Dieléctrica | 2.5 KV 50/60 Hz @ 1 min | UL 508 |
| Grado de Protección al Fuego de la Carcaza | 5 VA | UL-94 |
| Material de la Carcaza | Polímeros: LEXAN 500R, ABS, Nylon | |
| Tipos de Montaje | Riel DIN Simétrico, Superficie Plana, Empotrable (Flush Mounting) | IEC 715, DIN 43880, NEMA |
| Tipo de Tornillo de Borneras | Plano M2.5 | |
| Torque de Apretado de Borneras | 5.2 Kg-cm (4.5 lb-in) | |
| Medidas | 105 x 90 x 68 (L x A x H) mm | |
| Peso | 0.23 kg (0.506 lb) | |

### C) Características de Control

| Parámetro | Valor | Norma |
|-----------|-------|-------|
| Capacidad de los Contactos | 3 A @ 240 V~, 1.5 A @ 480 V~ (para Circuitos de Control) Pilot Duty | UL 508 Sección 139.1 |
| Expectativa de vida Eléctrica | 100.000 Operaciones | |
| Expectativa de vida Mecánica | 10.000.000 Operaciones | |

### D) Ajustes de Rango, Mediciones

| Parámetro | Valor |
|-----------|-------|
| Rango de Medición de Voltaje, Um (Modelo de Voltaje: 120 / 208 / 480 V~) | 0-168 / 0-300 / 0-672 V~, ±2% |
| Rango de Frecuencia | 45.0-70.0 Hz, ±1% Precisión |

### F) Comunicaciones y Otras Funciones Especiales

| Parámetro | Valor |
|-----------|-------|
| Protocolo de Comunicaciones | MODBUS RTU @ 9600 8N1 |
| Puerto de Comunicación | GIO PORT (*) |
| Reporte Histórico de Fallas | Reporte de últimas 20 fallas, tipo de falla y valor |
| Bloqueo de Parámetros (Clave) | 0000 Libre, 0001-9999 Bloqueado - Selección del Usuario |

(*) Se requiere GIO-PLUG para la comunicación a través de GIO Port. El GIO-PLUG se suministra por separado.

## COMO ORDENAR GI+

Formato: **GI+L[VOLTAJE][IDIOMA]**

### Voltaje
- 120 – 120 V~
- 208 – 208/220 V~
- 480 – 440/480 V~

### Idioma
- S – ESPAÑOL
- E – INGLÉS
- P – PORTUGUÉS

## GI+ AJUSTES DE PANTALLA - GUÍA RÁPIDA DE PROGRAMACIÓN

### Estados de Operación
1.1 Conectado bajo Modo AUTO
1.2 Desconectado bajo Modo MANUAL
1.3 Desconectado