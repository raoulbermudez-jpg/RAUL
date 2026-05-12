---
title: "IO-Link RS485K Communication Adapter for ECA100-II Products"
type: Technical
source: "IO-LINK-RS485_MAN_US_V3_OUTLINES.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "IO-LINK-RS485K"
version_status: "historica"
date_processed: "2026-05-10"
---

# IO-Link RS485K Communication Adapter for ECA100-II Products

## General Description

The IO-Link-RS485K is a communication adapter that provides connectivity between the ECA100-II series of products and the RS485K communication bus. It is compatible with master computers and computer terminals, which have monitoring software and user interface (The software must be provided by the client). The IO-Link RS485K device is designed with components that provide isolation, allowing the interconnection of data, with safe electrical conditions between equipment and the users.

### Warnings and Cautions

**WARNING:** Only qualified technicians with knowledge about protection relays and the associated equipment, should do the installation, programing, maintenance and operation of the system. Failure to comply this may result in personal injury and/or equipment damages.

**CAUTION:** For the proper use of this device, the user must have knowledge of serial communication, MODBUS protocol and equipment integration.

**ATTENTION:** The terminal and/or computers to be used must have USB and/or Ethernet ports available and also a compatible software with communication protocol.

## Parts

### IO-PLUG-RJ45
Connector cable with electrical isolation to connect the ECA100-II relay to the adapter IO-A-RS485K.

### IO-A-RS485K
Adapter that provides connectivity between the ECA100-II relay and the communication bus over the RS485K standard.

## Mounting

**CAUTION:** THIS EQUIPMENT IS FOR INDOOR USE ONLY

There isn't a preferred orientation for the cables and/or adapters of the IO-Link RS485 family. The cables can be routed as desired and affixed using tie wraps or similar.

## General Dimensions

### IO-PLUG Connectors Cables Dimensions
- Cable length: 23.6 in
- Width: 0.24 in
- Height: 0.16 in
- Depth: 0.12 in to 0.13 in

### IO-A-RS485K Adapters Dimensions

| Model | Dimensions | Weight |
|-------|-----------|--------|
| Connector IO-PLUG-RJ45 Cable | 23.6 in | 0.14 lb |
| Adapter IO-A-RS485 | 2.9 × 1.7 × 0.8 in | 0.08 lb |

## Configuration for Connections

Allows the connection to ECA100-II devices using a communication bus with the standard RS-485. This bus must be connected to a terminal or computer, using the appropriate converter.

### Equipment Required
- Connector cable IO-PLUG-RJ45
- Adapter, model IO-A-RS485, one for each ECA100-II device
- Converter RS-485/USB (Note 1)

**Note 1:** Any required software, computers, terminals and adapters RS-485/USB must be provided by the user.

## Connection Diagrams

**ATTENTION:** It is very important to verify that the voltage of the communication bus never exceeds 24VDC. Otherwise, the adapters and the cables could be severely damaged.

### Connection Diagram for IO-Link with Standard RS-485K

The IO-Link RS485K could be connected with the following configuration:
- Multiple ECA100-II relays connected via IO-A-RS485 adapters
- IO-PLUG-RJ45 connectors linking adapters to the communication bus
- RS-485/USB converter connecting to master terminal or computer
- Power supply (7-24 VDC) provided by user
- Impedance termination (1 nF) at both ends of the communication bus
- Bus lines: PE (ground), GND (0V), S- (B), S+ (A)

## Parameters Adjustment

The IO-Link RS485K adapters and connectors do not require any adjustment. For the proper functioning just adjust the software and/or the drivers on the terminal or computer using the following parameters:

| Parameter | Value |
|-----------|-------|
| Protocol | MODBUS RTU |
| Baud rate | 9600 |
| Number of data bits | 8 |
| Parity | None |
| Number of stop bits | 1 |

## Operation

IO-Link RS485K connectors and adapters allow the communication of the ECA100-II series of relays with other equipment, master terminals or supervisory computers, through the use of the MODBUS-RTU PROTOCOL and appropriate adapters.

Through the MODBUS-RTU protocol the ECA100-II series relays exchange information with other master devices, connected in a communication bus. The devices that monitor or control, such as Terminals or Computers are called MASTERS, while the relays are assigned as SLAVES.

The ECA100-II series of products communicate in a scheme called UNICAST. When a Master Terminal interrogates or forwards commands to the relay, after the instructions have been received and completed, the relay returns a confirmation response to the Master Terminal.

A communication bus with RS-485 standard can link up to 32 relays. If installations with larger quantities are required, a standard repeater devices can be applied to extend the coverage of the communication bus.

## Technical Specifications

### A) Power
- Power Source: External power source
- Input voltage range: 7-24 VDC
- Current consumption: 10 mA
- Operation mode: Continuous

### B) Electromagnetic Compatibility and Emissions Standards
- Electrostatic discharge Immunity test: IEC 61000-4-2
- Radiated electromagnetic field immunity test: IEC 61000-4-3
- Fast transients immunity test: IEC 61000-4-4
- Immunity to conducted disturbances: IEC 61000-4-6
- Power Frequency Magnetic Field Immunity: IEC 61000-4-8
- Electrical disturbance tests for measuring relays: IEC 60255-22-1, IEC 61000-4-16, IEC 60255-22-7
- Test for immunity to conducted, common mode disturbances (0-150 KHz)

### C) Environmental Conditions, Operations Limits and Dimensions
- Operation ambient temperature: -5 °C to 55 °C (23 °F to 131 °F)
- Storage temperature: -10 °C to +70 °C (14 °F to 158 °F)
- Maximum Relative Humidity: 85% R.H.
- Allowed Pollution Level: Degree 3 (IEC 60255-5)
- Overvoltage category: Category III, 4KV (IEC 60255-5)
- Rated insulation voltage: 500V (IEC 60255-5)
- Impulse test voltage: 5 KV (IEC 60255-5)
- Dielectric test: 2.5 KV 50/60 Hz @ 1 min (US STANDARDS)
- Flammability grade: V0 (US STANDARDS)
- Plastic case material: PC, ABS, NYLON
- Mounting restrictions: None
- Terminal Block Screw type: Flat, M2.5, 0.4 N/m (4.0 Kgf/cm)
- Allowed cable: AWG 14 to AWG 30

### D) Communications and Other Functions
- Communication port: RS485
- Connector type: Screwed terminals
- Max. number of units to be connected: 32
- Protocol: MODBUS RTU, 9600, 8, N, 1

## How to Order

**IO-LINK-RS485K**

Communication Adapter to connect the ECA100-II to the RS485 communication bus

## Dimensions and Weight Reference

| Model | Dimensions | Weight |
|-------|-----------|--------|
| Connector IO-PLUG-RJ45 Cable | 23.6 in | 0.14 lb |
| Adapter IO-A-RS485 | 2.9 × 1.7 × 0.8 in | 0.08 lb |

---

**NOTE:** Technical data is valid at the time of printing. ECA Products reserve the right to subsequent alterations.

**Manufacturer:** ECA Products, 7313 William Barry Blvd North, Syracuse, NY 13212, United States.
