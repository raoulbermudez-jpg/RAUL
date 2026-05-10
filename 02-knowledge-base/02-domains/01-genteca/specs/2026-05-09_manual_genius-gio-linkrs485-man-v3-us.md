```markdown
---
title: "GIO-Link RS485 Installation Instructions"
type: Technical
source: "GIO-LINKRS485_MAN_V3_US.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GIO-A-RS485"
date_processed: "2026-05-09"
---

# GIO-Link RS485 Installation Instructions

## 1 GIO-Link RS485 - General Description

GIO-A-RS485 Adapter to communicate the Relayne Relay with a communication bus.

GIO-Link RS485 is intended for the exchange of information using the RS485 with the standard RS-485 (GIO-PLUG-RJ45 connector cable is included). The communication protocol between the Relayne relays family and compatible master computers or computer terminals, which have monitoring software and user interface (The software must be provided by the client). The GIO-Link RS485 device is designed with components that provide isolation, allowing the interconnection with safety electrical conditions.

**ALERT:** Only qualified technicians with knowledge about protection relays and the associated equipment, should do the installation, programming, maintenance and operation of the system. Failure to comply may result in personal injury and/or equipment damages.

## 2 GIO-Link RS485 - Parts

- **Connector cable GIO-PLUG-RJ45:** Connector cable, with electrical isolation, to connect the Relayne Relay with an adapter GIO-A-RS485.
- **GIO-A-RS485 - Converter RS-485/USB** (Note 1)

**Note 1:** Any required software, computers, terminals and adapters must be provided by the user.

## 3 GIO-Link RS485 - Mounting

**CAUTION:** THIS EQUIPMENT IS FOR INDOOR USE ONLY

There is no preferred orientation for the cables and/or adapters of the GIO-Link RS485. It is allowed to route the cables as desired and use tie wraps or similar to fix them.

## 4 GIO-Link RS485 - Configuration for Connections

GIO-Link RS485 with standard RS-485 (See Diagram No. 5.1):

Allows the connection from 1 to 32 Relayne Relay using a communication bus with the standard RS-485. This bus must be connected to a terminal or computer, using the appropriate converter.

**Equipment required:**
- Connector cable GIO-PLUG-RJ45
- Adaptor, GIO-A-RS485, one for each Relayne Relay

**ATTENTION:** It is very important to verify that the voltage of the communication bus never exceeds 12 VDC, otherwise the adapters and the cables could be severely damaged.

## 5 GIO-Link RS485 - Connection Diagrams

### 5.1 Connection Diagram for GIO-Link with Standard RS-485

```
POWER SUPPLY
(To be provided by
the user)

120 Ω      1nF
      
GIO PLUG        ADAPTER
            GIO-A-RS485
BUS RS-485
1 PE
2 GND (0V)
3 S- (B)
4 S+ (A)
5 +12V

GIO PLUG        ADAPTER
            GIO-A-RS485
1 PE
2 GND (0V)
3 S- (B)              USB Cable
4 S+ (A)
5 +12V

[Up to 32 Relayne Relay]

120 Ω      1nF

RS-485/USB
CONVERTER      COMPUTER

IMPEDANCE TERMINATION FOR BOTH ENDS OF THE COMMUNICATION BUS
```

## 7 GIO-Link RS485 - Parameters Adjustment

The GIO-Link RS485 adapters and connectors do not require any adjustment. For proper functioning, adjust the software and/or the drivers on the terminal or computer using the following parameters:

- **Protocol:** MODBUS RTU
- **Baud rate:** 9600
- **Number of data bits:** 8
- **Parity:** N
- **Number of stop bits:** 1

## 8 GIO-Link RS485 - Operation

GIO-Link RS485 connectors and adapters allow the communication of the Relayne Relay with other equipment, master terminals or supervisory computers, through the use of the MODBUS-RTU PROTOCOL and appropriate adapters.

Through the MODBUS-RTU protocol, the Relayne Relay exchanges information with other master devices connected in a communication bus. The devices that monitor or control, such as Terminals or Computers, are called MASTERS, while the relays are assigned as SLAVES.

The Relayne Relay communicates in a scheme called UNICAST. When a Master Terminal interrogates or forwards commands to the relay, after the instructions have been received and completed, the relay returns a confirmation response to the Master Terminal.

A communication bus with RS-485 standard can link up to 32 relays. If installations with larger quantities are required, a standard repeater device can be applied to extend the coverage of the communication bus.

## 9 GIO-Link RS485 Technical Specifications

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
- **b.7** Test for immunity to conducted, common mode disturbances (0-150 KHz): IEC 61000-4-16 / IEC 60255-22-7

### C) Communications and Other Functions

- **c.1** Communication port: GIO-A-RS485K
- **c.2** Connector type: Screwed terminals
- **c.3** Max. number of units to be connected: 32
- **c.4** Protocol: MODBUS RTU, 9600, 8,N,1

### D) Environmental Conditions, Operations Limits and Dimensions

| Parameter | Specification |
|-----------|---------------|
| d.1 Operation ambient temperature | -5 ºC to 55 ºC (23 ºF to 131 ºF) |
| d.2 Storage temperature | -10 ºC to +70 ºC (14 ºF to 158 ºF) |
| d.3 Maximum Relative Humidity | 85% R.H. |
| d.4 Allowed Pollution Level | Degree 3 IEC 60255-5 |
| d.5 Overvoltage category | Category III, 4KV IEC 60255-5 |
| d.6 Rated insulation voltage | 500V IEC 60255-5 |
| d.7 Impulse test voltage | 5 KV IEC 60255-5 |
| d.8 Dielectric test voltage | 2.5 KV 50/60 Hz @ 1 min US STANDARDS |
| d.9 Flammability grade | V0 US STANDARDS |
| d.10 Plastic case material | PC, ABS, NYLON |
| d.11 Mounting restrictions | None |
| d.12 Terminal Block Screw's type | Flat, M2.5 |
| d.13 Maximum torque | 0.4 N/m (4.0 Kgf/cm) |
| d.14 Allowed cable | AWG 14 to AWG 30 |
| d.15 Connector GIO-PLUG-RJ45 Cable | 23.6 in, 0.14 lb |
| d.16 Adapter GIO-A-RS485 | 2.9 x 1.7 x 0.8 in, 0.08 lb |

## How to Order

**GIO-A-