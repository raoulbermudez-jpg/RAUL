---
title: "Relé Alternador GRA-MV - Sistemas Hidroneumáticos de Dos Bombas"
type: Technical
source: "GRA-MV_MAN_V1_REV1.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GRA-MV"
date_processed: "2026-05-09"
---

# Relé Alternador GRA-MV

## Descripción General

El GRA-MV es un dispositivo electrónico de control que opera activando dos cargas eléctricas en forma alterna. Diseñado para ser usado en cualquier aplicación de automatismo y principalmente para alternar entre dos bombas de sistemas hidroneumáticos.

## Modos de Operación

El producto cuenta con una perilla que permite seleccionar:

- **EQUIPO 1 o EQUIPO 2 (Modo MANUAL)**: Permite activar directamente uno de los dos equipos.
- **AUTO (Modo AUTOMÁTICO)**: El relé alternador cambia automáticamente entre ambos equipos según las condiciones de operación, activada por la señal de CONTROL.

## Conexiones

- **Terminal 7 (Contacto Común)**: Conecte el voltaje a controlar o interrumpir
- **Terminal 8 (NA)**: EQUIPO 1 o salida al contactor 1
- **Terminal 6 (NC)**: EQUIPO 2 o salida al contactor 2
- **Terminal 2 (CONTROL)**: Conecte la señal de control

## Dimensiones de la Caja

- Ancho: 84,4 mm
- Alto: 31,4 mm

## Modo de Operación Automático

### Intervalo T0 – T1
- La señal de control se encuentra desactivada
- La salida del relé activa es NC (terminales 7-6 conectados)
- Los dos equipos se encuentran apagados

### Intervalo T1 – T2
- La señal de control se encuentra activa
- La salida del relé activa es NC (terminales 7-6 conectados)
- Permanece encendido el EQUIPO 1

### Instante T2
- Se produce la alternancia en el flanco de bajada
- Ahora la salida del relé activa es NA (terminales 7-8 conectados)

### Intervalo T2 – T3
- La señal de control se encuentra desactivada
- La salida del relé activa es NA (terminales 7-8 conectados)
- Los dos equipos se encuentran apagados

### Intervalo T3 – T4
- La señal de control se encuentra activa
- La salida del relé activa es NA (terminales 7-8 conectados)
- Permanece encendido el EQUIPO 2

### Instante T4
- Se produce la alternancia en el flanco de bajada
- Ahora la salida del relé activa es NC (terminales 7-6 conectados)

### Intervalo T4 – T5
- Se inicia el ciclo nuevamente como en el intervalo T0-T1

## Nota Importante

Cuando la señal de control está desactivada, ambos indicadores LED permanecen apagados, ya que los equipos no están en funcionamiento.