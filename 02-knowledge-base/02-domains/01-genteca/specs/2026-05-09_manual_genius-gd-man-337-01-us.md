---
title: "GIO-Link Installation Manual"
type: Technical
source: "GD-MAN-337-01-US.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GIO-PLUG-USB, GIO-PLUG-RJ45, GIO-A-RS485K"
date_processed: "2026-05-09"
---

# GIO-Link Installation Manual

## 1 GIO-Link General Description

GIO-Link is a set of communication devices intended for the exchange of information between the GENIUS relays family and compatible master computers and computer terminals, which have monitoring software and user interface (The software must be provided by the client). The GIO-Link devices are designed with components that provide isolation, allowing the interconnection of data, with safety electrical conditions between equipment and the users.

**ALERT:** Only qualified technicians with knowledge about protection relays and the associated equipment, should do the installation, programming, maintenance and operation of the system.

**ATTENTION:** For the proper use of these devices, the user must have knowledge of serial communication, MODBUS protocol and equipment integration. Failure to comply this may result in personal injury and/or equipment damages.

**ATTENTION:** The terminal and/or computers to be used must have USB and/or Ethernet ports available and also a compatible software with communication protocol.

## 2 GIO-Link Parts

- **GIO-PLUG-USB:** Connector cable, with electrical isolation, to connect the GENIUS Relay and the Terminal and/or computer, using a USB Port.
- **GIO-PLUG-RJ45:** Connector cable, with electrical isolation, to connect the GENIUS Relay with an adapter of the GIO-Link family.
- **GIO-A-RS485K:** Adapter to communicate the GENIUS Relay with a communication bus with the standard RS-485 (GIO-PLUG-RJ45 connector cable is included).

## 3 GIO-Link Mounting

**CAUTION:** ALL THESE EQUIPMENT IS FOR INDOOR USE ONLY

There is no any preferred orientation for the cables and/or adapters of the GIO-Link family. It is allowed to route the cables as desired and use tie wraps or similar to fix them.

## 4 GIO-Link General Dimensions

### 4.1 GIO-PLUG Connectors Cables Dimensions

| Model | Dimensions | Weight |
|-------|-----------|--------|
| Connector GIO-PLUG-RJ45 Cable | 23.6 in | 0.14 lb |
| Connector GIO-PLUG-USB Cable | 78.7 in | 0.19 lb |
| Adapter GIO-A-RS485K | 2.9 x 1.7 x 0.8 in | 0.08 lb |

### 4.2 Adapters Dimensions

Model GIO-A-RS485K:
- Height: 0.17 in
- Width: 0.29 in
- Depth: 0.24 in
- Additional measurements: 0.09 in, 0.16 in, 0.08 in, 0.12 in, 0.13 in

## 5 GIO-Link Configuration for Connections

### 5.1 GIO-Link with Standard RS-485

Allows the connection from 1 to 32 GENIUS Relays using a communication bus with the standard RS-485. This bus must be connected to a terminal or computer, using the appropriate converter.

**Equipment required:**
- Connector cable GIO-PLUG-RJ45
- Adapter, model GIO-A-RS485K, one for each GENIUS Relay
- Converter RS-232/USB (Note 1)

### 5.2 GIO-Link with Standard USB

Allows the connection from one to several GENIUS Relays using a conventional USB Port. It is required one USB Port in the terminal or computer for every relay to be supervised.

**Equipment required:**
- Connector cable GIO-PLUG-USB

**Note 1:** Any required software, computers, terminals and adapters RS-485/USB must be provided by the user.

## 6 GIO-Link Connection Diagrams

**ATTENTION:** It is very important to verify that the voltage of the communication bus never exceeds 12 VDC, otherwise the adapters and the cables could be severely damaged.

### 6.1 Connection Diagram for GIO-Link System with Standard USB

Direct connection between GIO PORT (GENIUS relay), GIO-PLUG-USB connector cable, and USB Port on Terminal or Computer.

### 6.2 Connection Diagram for GIO-Link System with Standard RS-485

Configuration for multiple relays (up to 32) connected via RS-485 bus:
- Power Supply: 120V (provided by user)
- GIO PORT connection to GIO-A-RS485K Adapter
- Adapter pin configuration:
  - Pin 1: PE
  - Pin 2: GND (0V)
  - Pin 3: S- (B)
  - Pin 4: S+ (A)
  - Pin 5: +12V
- 1nF capacitor for impedance termination at both ends of communication bus
- RS-485/USB Converter to Computer

## 7 GIO-Link Parameters Adjustment

The GIO-Link adapters and connectors do not require any adjustment. For proper functioning, adjust the software and/or the drivers on the terminal or computer using the following parameters:

### 7.1 GIO-PLUG-RJ45 and GIO-A-RS485K

- Protocol: MODBUS RTU
- Baud rate: 9600
- Number of data bits: 8
- Parity: N
- Number of stop bits: 1

### 7.2 GIO-PLUG-USB

The GIO-PLUG-USB should be connected to any USB port on the terminal and/or computer. Just be sure that the driver is properly installed and updated.

## 8 GIO-Link Operation

GIO-Link connectors and adapters allow the communication of the GENIUS relays with other equipment, master terminals or supervisory computers, through the use of the MODBUS-RTU PROTOCOL and appropriate adapters. Through the MODBUS-RTU protocol the GENIUS relays exchange information with other master devices, connected in a communication network.

## 9 GIO-Link Technical Specifications

### A) Power

| Parameter | GIO-A-RS232K | GIO-A-RS485K |
|-----------|--------------|--------------|
| Power Source | No needed | External power source 7-12 VDC |
| Input voltage range | - | 2 mA to 10 mA |
| Current consumption | - | Continuous |
| Operation mode | MODBUS RTU | MODBUS RTU |

### B) Environmental Conditions, Operations Limits and Dimensions

| Parameter | Specification |
|-----------|---------------|
| Operation ambient temperature | 23 °F to 131 °F |
| Storage temperature | 14 °F to 158 °F |
| Maximum Relative Humidity | 85% R.H. |
| Allowed Pollution Level | Grade 3 IEC 60255-5 |
| Overvoltage category | Category III, 4KV IEC 60255-5 |
| Rated insulation voltage | 500V UL IEC 60255-5 |
| Impulse test voltage | 5 KV IEC 60255-5 |
| Dielectric test voltage | 2.5 KV 50/60 Hz @ 1 min UL 508 |
| Flammability grade | VO UL-94 |
| Plastic case material | Polycarbonate: LEXAN 500R |
| Mounting restrictions | None |
| Terminal Block Screw's type | Flat, M2.5 |
| Maximum torque | 0.4 N/m (4.0 Kgf/cm) |
| Allowed cable | AWG 14 to AWG 30 |

| Model | Dimensions | Weight |
|-------|-----------|--------|
| Connector GIO-PLUG-RJ45 Cable | 23.6 in | 0.14 lb |
| Connector GIO-PLUG-USB Cable | 78.8 in | 0.19 lb |
| Adapter GIO-A-RS485K | 2.9 x 1.7 x 0.8 in | 0.08 lb |