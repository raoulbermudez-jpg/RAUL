```markdown
---
title: "COM-Link RS485 Communication Adapter MPA2 to RS485"
type: Technical
source: "COM-LINK-RS485_MAN1_V3_US.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "COM-A-RS485K"
date_processed: "2026-05-09"
---

# COM-Link RS485 - Communication Adapter MPA2 to RS485

## 1. General Description

The COM-Link RS485 is a communication adapter that allows the exchange of information between MPA2 (Motor Performance Analyzer) and the RS485 communication bus. It is compatible with master computers and computer terminals which have monitoring software and user interface (the software must be provided by the client). The COM-Link RS485 device is designed with components that provide isolation, allowing the interconnection of data with safety electrical conditions between equipment and users.

## 2. Parts

The kit COM-Link RS485 is composed of two parts:

- **COM-PLUG-RJ45**: Connector cable with electrical isolation to connect the MPA2 Relay with adapter COM-A-RS485
- **COM-A-RS485**: Adapter to communicate the MPA2 Relay with a communication bus with the standard RS-485 (COM-PLUG-RJ45 connector cable is included)

## 3. Mounting

**CAUTION: THIS EQUIPMENT IS FOR INDOOR USE ONLY**

**ALERT:** Only qualified technicians with knowledge about protection relays and the associated equipment should do the installation, programming, maintenance and operation of the system. Failure to comply may result in equipment damages and/or personal injury.

There is no preferred orientation for the cables and/or adapters of the COM-Link RS485. It is allowed to route the cables as desired and use tie wraps or similar to fix them.

## 4. Configuration for Connections

COM-Link RS485 with standard RS-485 allows the connection from 1 to 32 MPA2 Relays using a communication bus with the standard RS-485. This bus must be connected to a terminal or computer using the appropriate converter.

**Equipment required:**
- Communication adapter COM-Link RS485
- Converter RS-485/USB (Note 1)

**Note 1:** Any required software, computers, terminals and adapters RS-485/USB must be provided by the user.

**ATTENTION:** It is very important to verify that the voltage of the communication bus never exceeds 12 VDC, otherwise the adapters and the cables could be severely damaged.

## 5. Connection Diagrams

The COM-Link RS485 could be connected as shown in the connection diagram for COM-Link with standard RS-485, utilizing:

- 120 Ω impedance termination for both ends of the communication bus
- 1nF capacitors
- Power supply (to be provided by the user)
- RS-485/USB converter to computer
- Up to 32 MPA2 Relays

**Adapter pin configuration:**
- Pin 1: PE
- Pin 2: GND (0V)
- Pin 3: S- (B)
- Pin 4: S+ (A)
- Pin 5: +12V

## 6. Parameters Adjustment

The COM-Link RS485 adapters and connectors do not require any adjustment. For proper functioning, adjust the software and/or drivers on the terminal or computer using the following parameters:

- **Protocol:** MODBUS RTU
- **Baud rate:** 9600
- **Number of data bits:** 8
- **Parity:** N
- **Number of stop bits:** 1

## 7. Operation

COM-Link RS485 connectors and adapters allow the communication of the MPA2 relays with other equipment, master terminals or supervisory computers through the use of the MODBUS-RTU PROTOCOL and appropriate adapters.

Through the MODBUS-RTU protocol, the MPA2 relays exchange information with other master devices connected in a communication bus. Devices that monitor or control, such as terminals or computers, are called MASTERS, while the relays are assigned as SLAVES.

The MPA2 relays communicate in a scheme called UNICAST. When a Master Terminal interrogates or forwards commands to the relay, after the instructions have been received and completed, the relay returns a confirmation response to the Master Terminal.

A communication bus with RS-485 standard can link up to 32 relays. If installations with larger quantities are required, standard repeater devices can be applied to extend the coverage of the communication bus.

## 8. Technical Specifications

### A) Power
- **Models:** COM-A-RS485K
- **Power Source:** External power source 7-12 VDC
- **Input voltage range:** 10 mA
- **Current consumption:** Continuous

### B) Electromagnetic Compatibility and Emissions Standards
- **Electrostatic discharge immunity test:** IEC 61000-4-2
- **Radiated electromagnetic field immunity test:** IEC 61000-4-3
- **Fast transients immunity test:** IEC 61000-4-4
- **Immunity to conducted disturbances:** IEC 61000-4-6
- **Power frequency magnetic field immunity test:** IEC 61000-4-8
- **Electrical disturbance tests for measuring relays:** IEC 60255-22-1
- **Test for immunity to conducted, common mode disturbances (0-150 KHz):** IEC 61000-4-16, IEC 60255-22-7

### D) Environmental Conditions, Operations Limits and Dimensions
- **Operation ambient temperature:** -5 °C to 55 °C (23 °F to 131 °F)
- **Storage temperature:** -10 °C to +70 °C (14 °F to 158 °F)
- **Maximum relative humidity:** 85% R.H.
- **Allowed pollution level:** Degree 3 IEC 60255-5
- **Overvoltage category:** Category III, 4KV IEC 60255-5
- **Rated insulation voltage:** 500V IEC 60255-5
- **Impulse test voltage:** 5 KV IEC 60255-5
- **Dielectric test voltage:** 2.5 KV 50/60 Hz @ 1 min US STANDARDS
- **Flammability grade:** V0 US STANDARDS
- **Plastic case material:** PC, ABS, NYLON
- **Mounting restrictions:** None
- **Terminal block screw type:** Flat, M2.5
- **Maximum torque:** 0.4 N/m (4.0 Kgf/cm)
- **Allowed cable:** AWG 14 to AWG 30

### Model Dimensions and Weight
- **Connector COM-PLUG-RJ45 Cable:** 23.6 in, 0.14 lb
- **Adapter COM-A-RS485:** 2.9 x 1.7 x 0.8 in, 0.08 lb

## How to Order

**COM-A-RS485K** - Adapter to communicate the MPA2 Relay with RS-485 communication bus
```