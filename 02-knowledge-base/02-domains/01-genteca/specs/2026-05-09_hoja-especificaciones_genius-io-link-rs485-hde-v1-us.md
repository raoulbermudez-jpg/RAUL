---
title: "IO-Link RS485 Communication Adapter"
type: Technical
source: "IO-LINK-RS485_HDE_V1_US.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "IO-LINK-RS485K"
date_processed: "2026-05-09"
---

# IO-Link RS485 Communication Adapter for ECA100-II Products

## Description

The IO-Link-RS485K is a communication adapter that provides IO-Link RS485 connectivity between the ECA100-II series of products and the RS485 communication bus. It is compatible with master computers and computer terminals which have monitoring software and user interface (software must be provided by the client). The IO-Link RS485 device is designed with components that provide isolation, allowing the interconnection of data with safety electrical conditions between equipment and users.

## Kit Components

The IO-Link RS485 kit is composed of two parts:

### IO-PLUG-RJ45
Connector cable with electrical isolation to connect the ECA100-II relay to the adapter IO-A-RS485.

### IO-A-RS485
Adapter that provides connectivity between the ECA100-II relay and the communication bus over the RS485 standard.

## Communication Protocol

IO-Link RS485 connectors and adapters allow communication of the ECA100-II series of products relays with other equipment, master terminals, or supervisory computers through the MODBUS-RTU protocol.

Through the MODBUS-RTU protocol, the ECA100-II series relays exchange information with other master devices connected in a communication bus. Devices that monitor or control (such as Terminals or Computers) are called MASTERS, while relays are assigned as SLAVES.

The ECA100-II series relays communicate in a scheme called UNICAST. When a Master Terminal interrogates or forwards commands to the relay, after instructions have been received and completed, the relay returns a confirmation response to the Master Terminal.

A communication bus with RS-485 standard can link up to 32 relays. For installations requiring larger quantities, standard repeater devices can be applied to extend the coverage of the communication bus.

## Technical Specifications

### A) Power
- **a.1** Power Source: External power source
- **a.2** Input voltage range: 7-24 VDC
- **a.3** Current consumption: 10 mA
- **a.4** Operation Mode: Continuous

### B) Electromagnetic Compatibility and Emissions Standards
- **b.1** Electrostatic discharge Immunity test: IEC 61000-4-2
- **b.2** Radiated electromagnetic field immunity test: IEC 61000-4-3
- **b.3** Fast transients immunity test: IEC 61000-4-4
- **b.4** Immunity to conducted disturbances: IEC 61000-4-6
- **b.5** Power Frequency Magnetic Field Immunity Test: IEC 61000-4-8
- **b.6** Electrical disturbance tests for measuring relays: IEC 60255-22-1
- **b.7** Test for immunity to conducted, common mode disturbances (0-150 KHz): IEC 61000-4-16

### C) Communications and Other Functions
- **c.1** Connector type: Screwed terminals
- **c.2** Max. number of units to be connected: 32
- **c.3** Protocol: MODBUS RTU, 9600, 8,N,1

### D) Environmental Conditions, Operation Limits and Dimensions
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
- **d.12** Terminal Block Screw's type: Flat, M2.5
- **d.13** Maximum torque: 0.4 N/m (4.0 Kgf / cm)
- **d.14** Allowed cable: AWG 14 to AWG 30

### Dimensions and Weight

| Model | Dimensions | Weight |
|-------|-----------|--------|
| IO-PLUG-RJ45 (Cable) | 23.6 in | 0.14 lb |
| IO-A-RS485 (Adapter) | 2.9 x 1.7 x 0.8 in | 0.08 lb |

## How to Order

**IO-LINK-RS485K** - Communication Adapter to connect the ECA100-II to the RS485 communication bus.

**Address:**
7313 William Barry Blvd North
Syracuse, NY 13212, United States

## Warnings and Cautions

**WARNING:** Only qualified electrical technicians with knowledge of overload relays and associated machinery should perform the installation, starting up, and maintenance of the system. Adhere to all local and national electric codes. Disconnect all electrical power at the source prior to any installation or maintenance work. Failure to comply could result in equipment damage, personal injury, or even death.

**CAUTION:** For the proper use of this device, the user must have knowledge of serial communication, MODBUS protocol, and equipment integration.

**NOTE:** Technical data is valid at the time of printing. The manufacturer reserves the right to subsequent alterations.

---
**Document Version:** 1  
**Date:** 24/09/2021  
**Approved by:** Liliam Ramirez  
**Reviewed by:** Ana Mendez