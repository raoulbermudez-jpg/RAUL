---
title: "IO-Link RS485K Communication Adapter Installation Manual"
type: Technical
source: "IO-LINK-RS485_MAN_V2_US.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "IO-Link RS485K"
date_processed: "2026-05-09"
---

# IO-Link RS485K Communication Adapter for ECA100-11 Products

## 1 General Description

The IO-Link-RS485K is a communication adapter that provides connectivity between the ECA100-11 series of products and the RS485 communication bus. It is compatible with master computers and computer terminals which have monitoring software and user interface (software must be provided by the client). The IO-Link RS485K device is designed with components that provide isolation, allowing the interconnection of data with safe electrical conditions between equipment and users.

### Safety Warnings

**WARNING:** Only qualified electrical technicians with knowledge of overload relays and associated machinery should perform the installation, starting up, and maintenance of the system. Adhere to all local and national electric codes. Disconnect all electrical power at the source prior to any installation or maintenance work. Failure to comply could result in equipment damage, personal injury, or even death.

**CAUTION:** For the proper use of this device, the user must have knowledge of serial communication, MODBUS protocol and equipment integration. The terminal and/or computers to be used must have USB and/or Ethernet ports available and also compatible software with communication protocol.

## 2 IO-Link RS485K Parts

| Component | Description | Dimensions | Weight |
|-----------|-------------|------------|--------|
| IO-PLUG-RJ45 | Connector cable with electrical isolation to connect the ECA100-11 relay | 23.6 in | 0.14 lb |
| IO-A-RS485 | Adapter providing connectivity between ECA100-11 relay and RS485 communication bus | 2.9 x 1.7 x 0.8 in | 0.08 lb |

## 3 Mounting

**CAUTION:** This equipment is for indoor use only.

There is no preferred orientation for the cables and/or adapters of the IO-Link RS485K family. The cables can be routed as desired and affixed using tie wraps or similar.

## 4 General Dimensions

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

## 5 Configuration for Connections

Equipment required:
- Connector cable IO-PLUG-RJ45
- Adaptor, model IO-A-RS485, one for each ECA100-11 device
- Converter RS-485/USB (Note 1)

**Note 1:** Any required software, computers, terminals and adapters RS-485/USB must be provided by the user.

## 6 Connection Diagrams

### 6.1 Connection Diagram for IO-Link RS485K with Standard RS-485

**ATTENTION:** It is very important to verify that the voltage of the communication bus never exceeds 24 VDC, otherwise the adapters and the cables could be severely damaged.

The IO-Link RS485K could be connected with:
- Power supply (to be provided by the user): 120 Ω, 1nF
- BUS RS-485 configuration with IO-A-RS485 adapters
- Connector pins:
  - 1 PE
  - 2 GND (0V)
  - 3 S- (B)
  - 4 S+ (A)
  - 5 +12V or +24V
- USB Cable connection to Laptop
- RS-485/USB Converter
- Impedance termination (120 Ω, 1nF) required at both ends of the communication bus
- ECA100-11 relay connection through IO-PLUG RS485 and IO-A-RS485 adapter

## 7 Parameters Adjustment

The IO-Link RS485K adapters and connectors do not require any adjustment. For proper functioning, adjust the software and/or drivers on the terminal or computer using the following parameters:

| Parameter | Value |
|-----------|-------|
| Protocol | MODBUS RTU |
| Baud rate | 9600 |
| Number of data bits | 8 |
| Parity | None |
| Number of stop bits | 1 |

## 8 Operation

The IO-Link RS485K connectors and adapters allow communication of the ECA100-11 series of relays with other equipment, master terminals or supervisory computers through the use of the MODBUS-RTU protocol and appropriate adapters.

Through the MODBUS-RTU protocol, the ECA100-11 series of relays exchange information with other master devices connected in a communication bus. The devices that monitor or control, such as terminals or computers, are called MASTERS, while the relays are assigned as SLAVES.

The ECA100-11 series of relays communicate in a scheme called UNICAST. When a Master Terminal interrogates or forwards commands to the relay, after the instructions have been received and completed, the relay returns a confirmation response to the Master Terminal.

A communication bus with RS-485 standard can link up to 32 relays. If installations with larger quantities are required, a standard repeater device can be applied to extend the coverage of the communication bus.

## 9 Technical Specifications

### A) Power

| Parameter | Value |
|-----------|-------|
| Power Source | External power source |
| Input voltage range | 7-24 VDC |
| Current consumption | 10 mA |
| Operation mode | Continuous |

### B) Electromagnetic Compatibility and Emissions Standards

| Parameter | Standard |
|-----------|----------|
| Electrostatic discharge Immunity test | IEC 61000-4-2 |
| Radiated electromagnetic field immunity test | IEC 61000-4-3 |
| Fast transients immunity test | IEC 61000-4-4 |
| Immunity to conducted disturbances | IEC 61000-4-6 |
| Power Frequency Magnetic Field Immunity Test | IEC 61000-4-8 |

### D) Environmental Conditions, Operations Limits and Dimensions

| Parameter | Value |
|-----------|-------|
| Operation ambient temperature | -5 ºC to 55 ºC (23 ºF to 131 ºF) |
| Storage temperature | -10 ºC to +70 ºC (14 ºF to 158 ºF) |
| Maximum Relative Humidity | 85% R.H. |
| Allowed Pollution Level | Degree 3 IEC 60255-5 |
| Overvoltage category | Category III, 4KV IEC 60255-5 |
| Rated insulation voltage | 500V IEC 60255-5 |
| Impulse test voltage | 5 KV IEC 60255-5 |
| Dielectric test voltage | 2.5 KV 50/60 Hz @ 1 min US STANDARDS |
| Flammability grade | V0 US STANDARDS |
| Plastic case material | PC, ABS, NYLON |