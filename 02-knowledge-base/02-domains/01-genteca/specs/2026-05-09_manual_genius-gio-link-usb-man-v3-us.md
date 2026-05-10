---
title: "GIO-Link USB Installation Instructions"
type: Technical
source: "GIO-LINK-USB_MAN_V3_US.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GIO-PLUG-USB"
date_processed: "2026-05-09"
---

# GIO-Link USB Installation Instructions

## 1. General Description

The GIO-Link USB is intended for the exchange of information using USB communication protocol between the Relayne relays family and compatible master computers or computer terminals, which have monitoring software and user interface (The software must be provided by the client). The GIO-Link USB device is designed with components that provide isolation, allowing the interconnection with safety electrical conditions.

**ALERT:** Only qualified technicians with knowledge about protection relays and the associated equipment should do the installation, programming, maintenance and operation of the system. Failure to comply may result in personal injury and/or equipment damages.

**ATTENTION:** The terminal and/or computers to be used must have USB port available and also compatible software with communication protocol.

## 2. GIO-Link USB - Part

**GIO-PLUG-USB:** Connector cable with electrical isolation to connect the GENIUS Relay and the Terminal and/or computer using a USB Port.

## 3. GIO-Link USB - Mounting

**CAUTION:** THIS EQUIPMENT IS FOR INDOOR USE ONLY

The GIO-PLUG USB should be connected to any USB port on the terminal and/or computer. Just be sure that the driver is properly installed and updated.

There is no preferred orientation for the cables and/or adapters of the GIO-Link USB. It is allowed to route the cables as desired and use tie wraps or similar to fix them.

## 4. GIO-Link USB - Configuration for Connections

### GIO-Link with standard USB (See Diagram No. 5.1):

Allows the connection from one Relayne Relay using a conventional USB Port. It is required one USB Port in the terminal or computer for every relay to be supervised.

**Equipment required:**
- Connector cable GIO-PLUG-USB

**Note 1:** Any required software, computers, terminals and adapters RS-485/USB must be provided by the user.

## 5. GIO-Link USB - Connection Diagrams

### 5.1 Connection diagram for GIO-Link with standard USB

```
GENIUS RELAYNE ——— GIO-PORT CONNECTOR
                          |
                    GIO-PLUG-USB
                          |
                     USB Port
                          |
                TERMINAL OR COMPUTER
```

## 7. GIO-Link USB - Parameters

The GIO-Link USB adapters and connectors do not require any adjustment. For proper functioning, adjust the software and/or drivers on the terminal or computer using the following parameters:

- Protocol: MODBUS RTU
- Baud rate: 9600
- Number of data bits: 8
- Parity: N
- Number of stop bits: 1

## 8. GIO-Link USB - Operation

GIO-Link USB adapter allows the communication of a Relayne Relay with other equipment, master terminals or supervisory computers through the use of the MODBUS-RTU PROTOCOL.

Through the MODBUS-RTU protocol, the Relayne Relay exchanges information with a master device. The devices that monitor or control, such as Terminals or Computers are called MASTERS, while the relays are assigned as SLAVES.

The Relayne Relay communicates in a scheme called UNICAST. When a Master Terminal interrogates or forwards commands to the relay, after the instructions have been received and completed, the relay returns a confirmation response to the Master Terminal.

## 9. GIO-Link USB Technical Specifications

### A) Power
- **Model:** GIO-PLUG-USB
- **Power Source:** USB port
- **Input voltage range:** 2 mA
- **Current consumption:** Continuous

### B) Electromagnetic Compatibility and Emissions Standards
- **Electrostatic discharge immunity test:** IEC 61000-4-2
- **Radiated electromagnetic field immunity test:** IEC 61000-4-3
- **Fast transients immunity test:** IEC 61000-4-4
- **Immunity to conducted disturbances:** IEC 61000-4-6
- **Power Frequency Magnetic Field Immunity Test:** IEC 61000-4-8
- **Electrical disturbance tests for measuring relays:** IEC 60255-22-1
- **Test for immunity to conducted, common mode disturbances (0-150 KHz):** IEC 61000-4-16, IEC 60255-22-7

### C) Communications and Other Functions
- **Communication port:** USB
- **Protocol:** MODBUS RTU, 9600, 8,N,1

### D) Environmental Conditions, Operations Limits and Dimensions
- **Operation ambient temperature:** -5 ºC to 55 ºC (23 ºF to 131 ºF)
- **Storage temperature:** -10 ºC to +70 ºC (14 ºF to 158 ºF)
- **Maximum Relative Humidity:** 85% R.H.
- **Allowed Pollution Level:** Degree 3 IEC 60255-5
- **Overvoltage category:** Category III, 4KV IEC 60255-5
- **Rated insulation voltage:** 500V IEC 60255-5
- **Impulse test voltage:** 5 KV IEC 60255-5
- **Dielectric test voltage:** 2.5 KV 50/60 Hz @ 1 min US STANDARDS
- **Flammability grade:** V0 US STANDARDS
- **Plastic case material:** PC, ABS, NYLON
- **Mounting restrictions:** None
- **Terminal Block Screw type:** Flat, M2.5
- **Maximum torque:** 0.4 N/m (4.0 Kgf/cm)
- **Allowed cable:** AWG 14 to AWG 30
- **Model Dimensions Weight:** Connector GIO-PLUG-USB Cable 78.8 in, 0.19 lb

## How to Order

**GIO-PLUG USB:** Adapter to communicate the Relayne Relay with USB port.

---

**Manufacturer:**
Gente, Generación de Tecnología C.A.
R.I.F.: J-00223173-4
Av. El Buen Pastor, cruce con Calle Vargas, Edificio Alba, Piso 1, Local 1-A
Boleíta Norte, Caracas, 1070, República Bolivariana de Venezuela
Phone: +58-212-237.0711 (Master)
Fax: +58-212-235.2497
E-mail: genteven@genteca.com.ve
Website: www.genteca.com.ve

**NOTE:** The specifications and/or functions could be changed without any previous announcement.