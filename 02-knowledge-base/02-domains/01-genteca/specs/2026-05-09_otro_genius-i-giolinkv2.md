---
title: "GIO-Link Manual de Instalación"
type: Technical
source: "I_GIOLINKv2.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GIO-Link"
date_processed: "2026-05-09"
---

# GIO-Link Manual de Instalación

## Descripción General

GIO-Link es un conjunto de dispositivos de comunicación previstos para que las familias de Relés (Relevadores) de Protección intercambien información con equipos terminales maestros y computadores compatibles, que dispongan un software de supervisión e interfaz al usuario (software a ser provisto por el cliente). Los dispositivos GIO-Link están diseñados con componentes que proveen aislación, permitiendo la interconexión de datos en condición de seguridad eléctrica entre los equipos y usuarios.

### Advertencias

**ALERTA:** Sólo personal técnico calificado con conocimientos en Relé (Relevadores) de protección y la carga asociada debería realizar la instalación, arranque y mantenimiento del sistema. Hacer caso omiso podría resultar en lesiones a personas y/o daños a los equipos conectados.

**ATENCIÓN:** Para la utilización adecuada de estos dispositivos, el usuario debe tener conocimientos de comunicación serial e integración de equipos, en específico de los estándares RS485 y RS232.

**ATENCIÓN:** Los equipos Terminales o de Computación, con los cuales se instalará la comunicación con los Relés (Relevadores) de Protección, deben disponer un puerto de comunicación serial, y tener un software de supervisión compatible con el Protocolo MODBUS RTU, en modo Maestro.

## Partes y Piezas Alternativas

### GIO-PLUG-USB
Conector que provee aislación eléctrica y comunica a un Relé (Relevador) de Protección directamente con un Terminal maestro o Computador, a través de su puerto USB.

### GIO-PLUG-RJ45
Conector que provee aislación eléctrica y conecta un Relé (Relevador) de Protección con un Adaptador o Concentrador intermedio del conjunto GIO-Link.

### GIO-A-RS485K
Conjunto de Adaptador que convierte señales de datos de los Relés (Relevadores) de Protección en señales compatibles con un Bus de Comunicación bajo estándar RS-485 (incluye cable GIO-Plug).

### GIO-A-RS232K
Conjunto de Adaptador que convierte señales de datos de los Relés (Relevadores) de Protección en señales compatibles con un Puerto de Comunicación bajo estándar RS-232 (incluye cable GIO-Plug).

## Montaje

**PRECAUCIÓN:** Los dispositivos deben ser instalados en lugar accesible, libre de polvo, sucio, humedad y vibraciones. SOLO DE USO INTERIOR.

Los dispositivos adaptadores y conectores de GIO-Link pueden ser montados en cualquier posición, sin restricciones en cuanto a orientación. No se requieren orificios ni tornillos para la fijación. El Instalador puede organizar y sujetar las piezas y cables mediante el uso de correas o cintas de nylon o similar.

## Dimensiones Generales

### Conectores GIO-PLUG
- Conector GIO-PLUG-RJ45: Cable 60 cm, Peso: 0,062 Kg
- Conector GIO-PLUG-USB: Cable 200 cm, Peso: 0,085 Kg

### Adaptadores

| Modelo | Dimensiones | Peso |
|--------|-------------|------|
| GIO-A-RS485K | 7,45 x 4,27 x 2,02 cm | 0,034 Kg |
| GIO-A-RS232K | 7,07 x 4,27 x 2,34 cm | 0,037 Kg |

## Configuraciones Alternativas para la Comunicación de Datos

### Sistema GIO-Link con Estándar RS-232

Alternativa para comunicar un (1) solo RELÉ (RELEVADOR) DE PROTECCIÓN por cada puerto serial tipo COM RS-232 disponible en un Terminal o Computadora.

**Componentes requeridos:**
- Adaptador modelo GIO-A-RS232K (una pieza)
- Conector modelo GIO-PLUG-RJ45 (una pieza)

### Sistema GIO-Link con Estándar RS-485

Alternativa para comunicar de uno (1) a treinta y dos (32) RELÉS (RELEVADORES) DE PROTECCIÓN a través de un Bus de Comunicación tipo RS-485, que se encuentre adaptado al Terminal o Computadora.

**Opción A: Mediante Adaptadores del conjunto GIO-Link**

Con esta opción, a cada Relé (Relevador) de Protección se asigna un Adaptador.

**Componentes requeridos:**
- Conector modelo GIO-PLUG-RJ45 (uno para cada Relé)
- Adaptador modelo GIO-A-RS485K
- Convertidor RS-232/RS-485 (uno por Computador) - Nota 1

### Sistema GIO-Link con Estándar USB

Alternativa para comunicar de uno a varios RELÉS (RELEVADORES) DE PROTECCIÓN a través de puertos USB mediante el siguiente adaptador acoplado al Terminal o Computadora:

**Componentes requeridos:**
- Conector modelo GIO-PLUG-USB

**Nota 1:** Software de Supervisión, Terminales o Computadores y Convertidores tipo RS-232/RS-485 son equipos y partes a ser provistas por el usuario.

## Diagramas de Conexión

**ATENCIÓN:** Verifique cuidadosamente las conexiones de los cables para asegurar que ninguno exceda el límite de voltaje nominal de operación (12 V c.d.). Errores en las conexiones pueden originar una operación incorrecta o daños a los dispositivos.

### Diagrama de Conexión para Sistema GIO-Link con Estándar RS-232

```
RELÉ (RELEVADOR)
        ↓
   GIO PORT
        ↓
CONECTOR GIO-PLUG-RJ45
        ↓
ADAPTADOR GIO-A-RS232K
        ↓
Cable de comunicación RS-232
        ↓
TERMINAL O COMPUTADOR
```

### Diagrama de Conexión para Sistema GIO-Link con Estándar RS-485

**Opción A: Mediante Adaptadores**

- Fuente de Poder (a ser provisto por el usuario): 12V
- Hasta 32 RELÉS (RELEVADORES), cada uno con:
  - UN CONECTOR GIO-PLUG-RJ45 por Relé
  - UN ADAPTADOR GIO-A-RS485K por Relé
- Impedancia de Terminación (120 Ω, 1nF) en ambos extremos del bus cableado
- Bus RS-485 conectado a Convertidor RS-485/RS232
- Conexión DB-9 al COMPUTADOR

**Pinout del Adaptador GIO-A-RS485K:**
1. PE (Tierra Protectora)
2. GND (0V)
3. S- (B)
4. S+ (A)
5. +12V

## Ajuste de Parámetros

Los conectores y adaptadores GIO-Link no requieren ajustes físicos ("hardware"). Para el funcionamiento, configure el software y/o manejador según corresponda.

## Especificaciones Técnicas

### Alimentación

(Sección incompleta en el documento fuente)