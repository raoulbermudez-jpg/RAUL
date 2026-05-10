```markdown
---
title: "COM-Link RS485 - Communication Adapter MPA2 to RS485"
type: Technical
source: "COM-LINK-RS485_MAN1_V4_US.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "COM-A-RS485K"
date_processed: "2026-05-09"
---

# COM-Link RS485 - Communication Adapter MPA2 to RS485

## 1. General Description

The Com-Link RS485 is a communication adapter that allows the exchange of information between MPA2 (Motor Performance Analyzer) and the RS485 communication bus. It's compatible with master computers and computer terminals, which have monitoring software and user interface (the software must be provided by the client). The COM-Link RS485 device is designed with components that provide isolation, allowing the interconnection of data, with safety electrical conditions between equipment and the users.

### Important Warnings

**WARNING:** Only qualified technicians with knowledge about protection relays and the associated equipment, should do the installation, programing, maintenance and operation of the system. Failure to comply this may result in equipment damages and/or injury persona.

**CAUTION:** For the proper use of this device, the user must have knowledge of serial communication, MODBUS protocol and equipment integration.

**CAUTION:** This equipment is for indoor use only.

**ATTENTION:** It is very important to verify that the voltage of the communication bus never exceeds 24 VDC, otherwise the adapters and the cables could severally damaged.

## 2. Parts

The kit COM-Link RS485 is composed of two parts:

- **COM-PLUG-RJ45:** Connector cable, with electrical isolation, to connect the MPA2 Relay with adapter COM-A-RS485.
- **COM-A-RS485:** Adapter to communicate the MPA2 Relay with a communication bus with the standard RS-485 (COM-PLUG-RJ45 connector cable is included).

## 3. Mounting

There is no any preferred orientation for the cables and/or adapters of the COM-Link RS485. It is allowed to route the cables as desired and use tie wraps or similar to fix them.

## 4. Configuration for Connections

### COM-Link RS485 with Standard RS-485

Allows the connection from 1 to 32 MPA2 Relays using a communication bus with the standard RS-485. This bus must be connected to a terminal or computer, using the appropriate converter.

**Equipment required:**
- Communication adapter COM-Link RS485
- Converter RS-485/USB (Note 1)

**Note 1:** Any required software, computers, terminals and adapters RS-485/USB must be provided by the user.

## 5. Connection Diagrams

The COM-Link RS485 could be connected as shown in the connection diagram for COM-Link with standard RS-485. The diagram shows:

- Connection of up to 32 MPA2 Relays
- RS-485/USB Converter to Computer
- 120 Ω Impedance Termination for both ends of the communication bus
- 1nF capacitor connections
- Power supply (to be provided by the user)

### Pin Configuration

**COM PLUG ADAPTER COM-A-RS485:**
1. PE
2. GND (0V)
3. S- (B)
4. S+ (A)
5. +12V or +24V

## 6. Parameters Adjustment

The COM-Link RS485 adapters and connectors do not required any adjustment. For the proper functioning just adjust the software and/or the drivers on the terminal or computer using the following parameters:

- **Protocol:** MODBUS RTU
- **Baud rate:** 9600
- **Number of data bits:** 8
- **Parity:** N
- **Number of stop bits:** 1

## 7. Operation

COM-Link RS485 connectors and adapters allow the communication of the MPA2 relays with other equipment, master terminals or supervisory computers, through the use of the MODBUS-RTU PROTOCOL and appropriate adapters.

Through the MODBUS-RTU protocol the MPA2 relays exchange information with other master devices, connected in a communication bus. The devices that monitor or control, such as Terminals or Computers are called MASTERS, while the relays are assigned as SLAVES.

The MPA2 relays communicate in a scheme called UNICAST. When a Master Terminal interrogates or forwards commands to the relay, after the instructions have been received and completed, the relay returns a confirmation response to the Master Terminal.

A communication bus with RS-485 standard can link up to 32 relays. If installations with larger quantities are required, a standard repeater devices can be applied to extend the coverage of the communication bus.

## 8. Technical Specifications

### A) Power

| Parameter | Value |
|-----------|-------|
| Model | COM-A-RS485K |
| Power Source | External power source 7-24 VDC |
| Input voltage range | 10 mA |
| Current consumption | Continuous |

### B) Electromagnetic Compatibility and Emissions Standards

- Electrostatic discharge Immunity test: IEC 61000-4-2
- Radiated electromagnetic field immunity test: IEC 61000-4-3
- Fast transients immunity test: IEC 61000-4-4
- Immunity to conducted disturbances: IEC 61000-4-6
- Power Frequency Magnetic Field Immunity Test: IEC 61000-4-8
- Electrical disturbance tests for measuring relays: IEC 60255-22-1
- Test for immunity to conducted, common mode disturbances (0-150 KHz): IEC 61000-4-16 / IEC 60255-22-7

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
| Mounting restrictions | None |
| Terminal Block Screw's type | Flat, M2.5 |
| Maximum torque | 0.4 N/m (4.0 Kgf/cm) |
| Allowed cable | AWG 14 to AWG 30 |

| Component | Dimensions | Weight |
|-----------|-----------|--------|
| Connector COM-PLUG-RJ45 Cable | 23.6 in | 0.14 lb |
| Adapter COM-A-RS485 | 2.9 x 1.7 x 0.8 in | 0.08 lb |

---

**Document Date:** 02/12/2020  
**Approved by:** Victor Blanco  
**Reviewed by:** Ana Mendez  
**Version:** 4
```