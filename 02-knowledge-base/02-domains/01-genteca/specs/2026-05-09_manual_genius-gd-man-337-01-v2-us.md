```markdown
---
title: "GIO-Link RS485 Installation Manual"
type: Technical
source: "GD-MAN-337-01-V2-US.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GIO-A-RS485K"
date_processed: "2026-05-09"
---

# GIO-Link RS485 Installation Manual

## 1. General Description

GIO-Link RS485 is intended for the exchange of information between the MPA2 (Motor Performance Analyzer) and compatible master computers and computer terminals, which have monitoring software and user interface. The GIO-Link RS485 devices are designed with components that provide isolation, allowing the interconnection of data with safe electrical conditions between equipment and users.

**ALERT:** Only qualified technicians with knowledge about protection relays and associated equipment should perform installation, programming, maintenance and operation of the system. Failure to comply may result in personal injury and/or equipment damages.

**ATTENTION:** For proper use of this device, the user must have knowledge of serial communication, MODBUS protocol and equipment integration.

**ATTENTION:** There is no preferred orientation for the cables and/or adapters of the GIO-Link RS485 family. It is allowed to route the cables as desired and use tie wraps or similar to fix them.

**CAUTION:** THIS EQUIPMENT IS FOR INDOOR USE ONLY

The terminal and/or computers to be used must have USB and/or Ethernet ports available and also compatible software with communication protocol.

## 2. Parts

### GIO-PLUG-USB
Connector cable, with electrical isolation, to connect the GENIUS Relay and the Terminal and/or computer, using a USB Port.

### GIO-PLUG-RJ45
Connector cable, with electrical isolation, to connect the GENIUS Relay with an adapter of the GIO-Link family.

### GIO-A-RS485K
Adapter to communicate the GENIUS Relay with a communication bus with the standard RS-485 (GIO-PLUG-RJ45 connector cable is included).

## 3. Mounting

**CAUTION:** THIS EQUIPMENT IS FOR INDOOR USE ONLY

## 4. General Dimensions

### 4.1 GIO-PLUG Connectors Cables Dimensions

- Height: 0.09 in
- Width: 0.24 in
- Depth: 0.16 in
- Additional measurements: 0.12 in, 0.13 in

### 4.2 GIO-A-RS485 Adapters Dimensions

- Height: 0.29 in
- Width: 0.17 in
- Depth: 0.08 in

### Specifications Table

| MODEL | DIMENSIONS | WEIGHT |
|-------|-----------|--------|
| Connector GIO-PLUG-RJ45 Cable | 23.6 in | 0.14 lb |
| Adaptor GIO-A-RS485 | 2.9 x 1.7 x 0.8 in | 0.08 lb |

## 5. Configuration for Connections

### 5.1 GIO-Link RS485 with Standard RS-485

Allows the connection from 1 to 32 MPA2 Relays using a communication bus with the standard RS-485. This bus must be connected to a terminal or computer using the appropriate converter.

**Equipment required:**
- Connector cable GIO-PLUG-RJ45
- Adaptor, model GIO-A-RS485, one for each MPA2 Relay
- Converter RS-485/USB (Note 1)

**Note 1:** Any required software, computers, terminals and adapters RS-485/USB must be provided by the user.

## 6. Connection Diagrams

**ATTENTION:** It is very important to verify that the voltage of the communication bus never exceeds 12 VDC, otherwise the adapters and the cables could be severely damaged.

### 6.1 Connection Diagram for GIO-Link with Standard RS-485

The GIO-Link RS485 connection diagram shows:
- Power supply (to be provided by the user)
- GIO PLUG ADAPTER with GIO-A-RS485
- BUS RS-485 with impedance termination (120 Ω, 1nF) at both ends
- Connection to computer via RS-485/USB Converter
- Support for up to 32 MPA2 Relays

**Pin Configuration:**
1. PE
2. GND (0V)
3. S- (B)
4. S+ (A)
5. +12V

## 7. Parameters Adjustment

The GIO-Link RS485 adapters and connectors do not require any adjustment. For proper functioning, adjust the software and/or drivers on the terminal or computer using the following parameters:

### 7.1 GIO-PLUG-RJ45 and GIO-A-RS485

| Parameter | Value |
|-----------|-------|
| Protocol | MODBUS RTU |
| Baud rate | 9600 |
| Number of data bits | 8 |
| Parity | N |
| Number of stop bits | 1 |

## 8. Operation

### 8.1 General Operation

GIO-Link RS485 connectors and adapters allow the communication of the MPA2 relays with other equipment, master terminals or supervisory computers, through the use of the MODBUS-RTU PROTOCOL and appropriate adapters.

Through the MODBUS-RTU protocol, the MPA2 relays exchange information with other master devices connected in a communication bus. The devices that monitor or control, such as Terminals or Computers, are called MASTERS, while the relays are assigned as SLAVES.

The MPA2 relays communicate in a scheme called UNICAST. When a Master Terminal interrogates or forwards commands to the relay, after the instructions have been received and completed, the relay returns a confirmation response to the Master Terminal.

A communication bus with RS-485 standard can link up to 32 relays. If installations with larger quantities are required, standard repeater devices can be applied to extend the coverage of the communication bus.

## Technical Specifications

### A. Environmental Conditions, Operations Limits and Dimensions

| Parameter | Value | Standard |
|-----------|-------|----------|
| Operation ambient temperature | (See MPA2 c.1 and c.2) | - |
| Storage temperature | 14 ºF to 158 ºF | - |
| Maximum Relative Humidity | 85% R.H. | - |
| Allowed Pollution Level | Degree 3 | IEC 60255-5 |
| Overvoltage category | Category III, 4KV | IEC 60255-5 |
| Rated insulation voltage | 500V | IEC 60255-5 |
| Impulse test voltage | 5 KV | IEC 60255-5 |
| Dielectric test voltage | 2.5 KV 50/60 Hz @ 1 min | US STANDARDS |
| Flammability grade | V0 | US STANDARDS |
| Plastic case material | PC, ABS, NYLON | - |
| Mounting restrictions | None | - |
| Terminal Block Screw type | Flat, M2.5 | - |
| Maximum torque | 0.4 N/m (4.0 Kgf/cm) | - |
| Allowed cable | AWG 14 to AWG 30 | - |
| Connector | GIO-PLUG-RJ45 | - |

### B. Communications and Other Functions

| Parameter | Value |
|-----------|-------|
| Communication port | GIO-A-RS485K |
| Connector type | Screwed terminals |
| Maximum number of units connected | 32 |
| Protocol | MODBUS RTU, 9600, 8,N,1 |

## How to Order

**GIO-A-RS485K** - Adapter to communicate the MPA2 Relay with a communication bus with the standard RS-485 (GIO-PLUG-RJ45 connector cable is included).
```