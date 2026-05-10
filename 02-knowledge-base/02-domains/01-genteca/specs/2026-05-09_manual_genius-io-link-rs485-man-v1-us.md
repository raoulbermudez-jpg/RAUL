---
title: "IO-Link RS485 Communication Adapter Installation Manual"
type: Technical
source: "IO-LINK-RS485_MAN_V1_US.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "IO-PLUG-RJ45, IO-A-RS485"
date_processed: "2026-05-09"
---

# IO-Link RS485 Communication Adapter Installation Manual

**Document Information:**
- Date: 24/09/2021
- Version: 1
- Approved by: Liliam Ramirez
- Reviewed by: Ana Mendez

## 1 IO-Link RS485 - General Description

IO-Link RS485 is designed for the exchange of information between the RBK11000 or RBK11001 relays and compatible master computers and computer terminals equipped with monitoring software and user interface (software to be provided by the client). The IO-Link RS485 devices are engineered with components that provide isolation, allowing safe electrical interconnection of data between equipment and users.

**WARNING:** Only qualified technicians with knowledge about protection relays and associated equipment should perform installation, programming, maintenance, and operation of the system. Failure to comply may result in personal injury and/or equipment damage.

**CAUTION:** Users must have knowledge of serial communication, MODBUS protocol, and equipment integration for proper use of this device.

**ATTENTION:** Terminal and/or computers must have USB and/or Ethernet ports available with compatible communication protocol software.

## 2 IO-Link RS485 - Parts

| Component | Model | Dimensions | Weight |
|-----------|-------|-----------|--------|
| Connector cable | IO-PLUG-RJ45 | 23.6 in | 0.14 lb |
| Adapter | IO-A-RS485 | 2.9 x 1.7 x 0.8 in | 0.08 lb |

### IO-PLUG-RJ45
Connector cable with electrical isolation to connect the RBK11000 or RBK11001 relay with an IO-Link RS485 adapter. Allows connection of 1 to RBK11000 or RBK11001 using a standard RS-485 communication bus connected to a terminal or computer using the appropriate converter.

### IO-A-RS485
Adapter to communicate the RBK11000 or RBK11001 with a standard RS-485 communication bus.

## 3 IO-Link RS485 - Mounting

**CAUTION:** THIS EQUIPMENT IS FOR INDOOR USE ONLY

There is no preferred orientation for cables and/or adapters of the IO-Link RS485 family. Cables may be routed as desired and secured using tie wraps or similar methods.

## 4 IO-Link RS485 - General Dimensions

### 4.1 IO-PLUG Connectors Cable Dimensions
- 0.09 in
- 0.24 in
- 0.16 in
- 0.12 in
- 0.13 in

### 4.2 IO-A-RS485 Adapters Dimensions
- 0.17 in
- 0.29 in
- 0.08 in

## 5 IO-Link RS485 - Configuration for Connections

**Equipment Required:**
- Connector cable IO-PLUG-RJ45
- Adapter, model IO-A-RS485 (one for each RBK11000 or RBK11001)
- Converter RS-485/USB (Note 1)

**Note 1:** Any required software, computers, terminals, and RS-485/USB adapters must be provided by the user.

## 6 IO-Link RS485 - Connection Diagrams

**ATTENTION:** It is very important to verify that the voltage of the communication bus never exceeds 24 VDC, otherwise the adapters and cables could be severely damaged.

### 6.1 Connection Diagram for IO-Link with Standard RS-485

The IO-Link RS485 can be connected with the following configuration:

- Power supply (7-24 VDC, to be provided by the user)
- Multiple IO-A-RS485 adapters connected to IO-PLUG RS485 connectors
- RS-485 communication bus with standard impedance termination (120 Ω, 1nF) at both ends
- Connection to laptop via RS-485/USB converter
- Signal lines: PE (Pin 1), GND (Pin 2), S- (Pin 3 - B), S+ (Pin 4 - A), +12V or +24V (Pin 5)

## 7 IO-Link RS485 - Parameters Adjustment

The IO-Link RS485 adapters and connectors do not require any adjustment. For proper functioning, adjust the software and/or drivers on the terminal or computer using the following parameters:

| Parameter | Value |
|-----------|-------|
| Protocol | MODBUS RTU |
| Baud rate | 9600 |
| Number of data bits | 8 |
| Parity | None |
| Number of stop bits | 1 |

## 8 IO-Link RS485 - Operation

IO-Link RS485 connectors and adapters enable communication of the RBK11000 or RBK11001 relays with other equipment, terminals, or supervisory computers through the MODBUS-RTU protocol and appropriate adapters.

Through the MODBUS-RTU protocol, RBK11000 or RBK11001 relays exchange information with other master devices connected in a communication bus. Devices that monitor or control (terminals or computers) are called MASTERS, while relays are assigned as SLAVES.

The relays communicate in a UNICAST scheme. When a Master Terminal interrogates or forwards commands to the relay, after instructions are received and completed, the relay returns a confirmation response to the Master Terminal.

A standard RS-485 communication bus can link up to 32 relays. For installations requiring larger quantities, standard repeater devices can be applied to extend the coverage of the communication bus.

## 9 IO-Link RS485 - Technical Specifications

### A) Power
- **a.1** Power Source: External power source
- **a.2** Input voltage range: 7-24 VDC
- **a.3** Current consumption: 10 mA
- **a.4** Operation mode: Continuous

### B) Electromagnetic Compatibility and Emissions Standards
- **b.1** Electrostatic discharge immunity test: IEC 61000-4-2
- **b.2** Radiated electromagnetic field immunity test: IEC 61000-4-3
- **b.3** Fast transients immunity test: IEC 61000-4-4
- **b.4** Immunity to conducted disturbances: IEC 61000-4-6
- **b.5** Power frequency magnetic field immunity test: IEC 61000-4-8
- **b.6** Electrical disturbance tests for measuring rel: (continued in document)

### C) Environmental Conditions, Operations Limits and Dimensions
- **c.1** Operation ambient temperature: -5 ºC to 55 ºC (23 ºF to 131 ºF)
- **c.2** Storage temperature: -10 ºC to +70 ºC (14 ºF to 158 ºF)
- **c.3** Maximum relative humidity: 85% R.H.
- **c.4** Allowed pollution level: Degree 3 IEC 60255-5
- **c.5** Overvoltage category: Category III, 4KV IEC 60255-5
- **c.6** Rated insulation voltage: 500V IEC 60255-5
- **c.7** Impulse test voltage: 5 KV IEC 60255-5
- **c.8** Dielectric test voltage: 2.5 KV 50/60 Hz @ 1 min US STANDARDS
- **c.9** Flammability grade: V0 US STANDARDS
- **c.10** Plastic case material: PC, ABS, NYLON
- **c.11** Mounting restrictions: None