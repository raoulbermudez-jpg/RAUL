```markdown
---
title: "GIO-Link RS485 Installation Instructions"
type: Technical
source: "GIO-LINKRS485_MAN_V3_US_c.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GIO-A-RS485"
date_processed: "2026-05-09"
---

# GIO-Link RS485 Installation Instructions

## 1 General Description

GIO-Link RS485 is an adapter to communicate the Relayne Relay with a communication bus using the RS485 standard. It is intended for the exchange of information between the Relayne relays family and compatible master computers or computer terminals which have monitoring software and user interface (software must be provided by the client).

The GIO-Link RS485 device is designed with components that provide isolation, allowing safe electrical interconnection.

**CAUTION: THIS EQUIPMENT IS FOR INDOOR USE ONLY**

**ALERT:** Only qualified technicians with knowledge about protection relays and associated equipment should do the installation, programming, maintenance and operation of the system. Failure to comply may result in personal injury and/or equipment damages.

## 2 Parts

- **GIO-PLUG-RJ45:** Connector cable with electrical isolation to connect the Relayne Relay with an adapter GIO-A-RS485
- **GIO-A-RS485:** Converter RS-485/USB (Note 1)
- **Connector cable GIO-PLUG-RJ45** (included)

Note 1: Any required software, computers, terminals and adapters must be provided by the user.

## 3 Mounting

There is no preferred orientation for the cables and/or adapters of the GIO-Link RS485. It is allowed to route the cables as desired and use tie wraps or similar to fix them.

## 4 Configuration for Connections

GIO-Link RS485 with standard RS-485 allows the connection from 1 to 32 Relayne Relay using a communication bus with the standard RS-485. This bus must be connected to a terminal or computer using the appropriate converter.

**ATTENTION:** The terminal and/or computers to be used with GIO-Link RS485 must have USB and/or serial ports available and also compatible software with communication protocol.

**ATTENTION:** It is very important to verify that the voltage of the communication bus never exceeds 12 VDC, otherwise the adapters and cables could be severely damaged.

## 5 Connection Diagrams

### 5.1 Connection Diagram for GIO-Link RS485 with Standard RS-485

The diagram shows:
- **GIO PLUG:** Connector with pins 1-5 (PE, GND (0V), S- (B), S+ (A), +12V)
- **ADAPTER GIO-A-RS485:** Converter with corresponding pins
- **BUS RS-485:** 120 Ω impedance termination and 1nF capacitor at both ends
- **Power Supply:** To be provided by the user (7-12 VDC)
- **RS-485/USB CONVERTER:** Connected to computer via USB cable
- **Up to 32 Relayne Relay:** Can be connected to the bus

## 7 Parameters Adjustment

The GIO-Link RS485 adapters and connectors do not require any adjustment. For proper functioning, adjust the software and/or drivers on the terminal or computer using the following parameters:

- **Protocol:** MODBUS RTU
- **Baud rate:** 9600
- **Number of data bits:** 8
- **Parity:** N
- **Number of stop bits:** 1

## 8 Operation

GIO-Link RS485 connectors and adapters allow communication of the Relayne Relay with other equipment, master terminals or supervisory computers through the MODBUS-RTU protocol and appropriate adapters.

Through the MODBUS-RTU protocol, the Relayne Relay exchanges information with other master devices connected in a communication bus. Devices that monitor or control (Terminals or Computers) are called MASTERS, while the relays are assigned as SLAVES.

The Relayne Relay communicates in a scheme called UNICAST. When a Master Terminal interrogates or forwards commands to the relay, after instructions have been received and completed, the relay returns a confirmation response to the Master Terminal.

A communication bus with RS-485 standard can link up to 32 relays. For installations requiring larger quantities, standard repeater devices can be applied to extend the coverage of the communication bus.

## 9 Technical Specifications

### A) Power

- **Models:** GIO-A-RS485K
- **Power Source:** External power source 7-12 VDC
- **Input voltage range:** 10 mA
- **Current consumption:** Continuous

### B) Electromagnetic Compatibility and Emissions Standards

- **b.1** Electrostatic discharge Immunity test: IEC 61000-4-2
- **b.2** Radiated electromagnetic field immunity test: IEC 61000-4-3
- **b.3** Fast transients immunity test: IEC 61000-4-4
- **b.4** Immunity to conducted disturbances: IEC 61000-4-6
- **b.5** Power Frequency Magnetic Field Immunity Test: IEC 61000-4-8
- **b.6** Electrical disturbance tests for measuring relays: IEC 60255-22-1
- **b.7** Test for immunity to conducted, common mode disturbances (0-150 KHz): IEC 61000-4-16, IEC 60255-22-7

### C) Communications and Other Functions

- **c.1** Communication port: GIO-A-RS485K
- **c.2** Connector type: Screwed terminals
- **c.3** Max. number of units to be connected: 32
- **c.4** Protocol: MODBUS RTU, 9600, 8,N,1

### D) Environmental Conditions, Operations Limits and Dimensions

- **d.1** Operation ambient temperature: -5 ºC to 55 ºC (23 ºF to 131 ºF)
- **d.2** Storage temperature: -10 ºC to +70 ºC (14 ºF to 158 ºF)
- **d.3** Maximum Relative Humidity: 85% R.H.
- **d.4** Allowed Pollution Level: Degree 3 IEC 60255-5
- **d.5** Overvoltage category: Category III, 4KV IEC 60255-5
- **d.6** Rated insulation voltage: 500V IEC 60255-5
- **d.7** Impulse test voltage: 5 KV IEC 60255-5
- **d.8** Dielectric test voltage: 2.5 KV 50/60 Hz @ 1 min US STANDARDS
- **d.9** Flammability grade: V0 US STANDARDS
- **d.10** Plastic case material: PC, ABS, NYLON
- **d.11** Mounting restrictions: None
- **d.12** Terminal Block Screw type: Flat, M2.5
- **d.13** Maximum torque: 0.4 N/m (4.0 Kgf/cm)
- **d.14** Allowed cable: AWG 14 to AWG 30

| Component | Dimensions | Weight |
|-----------|-----------|--------|
| Connector GIO-PLUG-RJ45 Cable | 23.6 in | 0.14 lb |
| Adapter GIO-A-RS485 | 2.9 x 1.7 x 0.8 in | 0.08 lb |

## How to Order

**GIO-A-RS485K:** Adapter to communicate the Relayne Relay with a communication RS485 bus.

---

Made and designed by Genteca, Generación de Tecnología
```