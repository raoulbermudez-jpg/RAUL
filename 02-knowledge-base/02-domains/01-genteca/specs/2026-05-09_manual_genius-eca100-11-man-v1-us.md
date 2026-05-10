---
title: "ECA100-11 Motor Protector Relay - Installation Instructions"
type: Technical
source: "ECA100-11_MAN_V1_US.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "ECA100-11"
date_processed: "2026-05-09"
---

# ECA100-11 MOTOR PROTECTOR RELAY

## General Description

ECA100-11 is an electronic three-phase relay specially designed to protect air conditioning and refrigeration compressors and ventilation motors from failure causes related to current and voltage.

### Warnings and Cautions

**WARNING:** Only qualified technicians with knowledge about protection relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in equipment damage and/or personal injury.

**CAUTION:** This product has been designed for industrial environment. Use of this product in residential environment may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

**CAUTION:** An incorrectly applied or installed ECA100-11 can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the ECA100-11.

**CAUTION:** ECA100-11 must be installed in an accessible position free from dust, dirt, dampness and vibrations. Allow enough space for air circulation around the enclosure and easy access to all operator controls. Indoors use only.

**WARNING:** (Risk of Electric Shock). Disconnect power supply before installing ECA100-11. Electric Shock will result in death or serious injury.

## Installation

### DIN Rail and Flat Surface Mounting

a) Take off the two (2) attachable mountings ears located at back side of ECA100-11, insert and slip both attachable mounting ears into the ECA100-11 back side grooves.

Place ECA100-11 at incline position with its back side placed toward the upper edge of the DIN Rail and push down ECA100-11 relay until it clicks on the rail.

**Recommendation for Flat Surface Mounting:** Make two (2) holes (5/32") on panel surface before installing. See as reference the Guide for Flat Surface Mounting shown in section 5 (ECA100-11 General Dimensions).

## Connection Diagram

**CAUTION:** Check that the voltage and current of the ECA100-11 model correspond to line voltage and motor current.

### Recommendations for Wiring

- Avoid over tightening the M3 screws upon terminals during wiring connection. Tightening Torque max. 4.4 Ibf-in (5.1 Kgf-cm).
- Wire Strip Length: 6-7 mm
- Terminal wiring size: Ø AWG 10 (4 mm²) to AWG 18
- Current Sensing Holes (conduits) wiring size: Ø AWG 4 (11 mm)
- Connect L1 L2 L3 terminal for Voltage input in parallel connection before line or chosen circuit through Contactor (as shown in Basic Diagram Installation)
- Use three Current Sensing Holes for passing wires before connection to 3 phases motor. Using less than three (3) wires shall cause current unbalance and wrong measures.

## ECA100-11 Adjustment

**ATTENTION:** Any accidental or intentional change of setting knobs positions after overload adjustment shall cause variation on ECA100-11 protective performance respect to previous setting up. In this case repeat procedure for ECA100-11 adjustment indicated in section 6.1.

### Adjustment Procedure

i) Using a flat screwdriver, turn the TC setting knob until you set the start delay desired (TC is the time between Voltage fault recovery and restart the system according to application needs).

g) Slowly turn right the current setting knob (FLA) up to desired protection level.

## Operation

**NOTICE:** In case the AUTO/MANUAL start mode slide-switch is set on MANUAL and the ECA100-11 relay trips due to any fault detection, you shall press START push button to re-activate the Contactor or Line Starter Circuit.

Although the AUTO/MANUAL start mode slide-switch is set on AUTO, pressing START push button is required if three (3) current failures have appeared in less than 30 minutes and qualified technicians have detected and solved causes of failures.

The ECA100-11 indicates any combination of fault conditions. Frequent relay trips may indicate mechanical problems such as the condensing unit does not dissipate the heat adequately, there is a problem in the wiring operation, or damage in the contactor.

## How to Order ECA100-11 According to Customer Needs

Available models with adjustable current ranges:

- **012** – 3.5-12.5 A* (*Available only for 208 VAC model)
- **032** – 10-32 A
- **080** – 25-80 A

### Cold-Hot Curves (Class 10)

After the first disconnection for current failures, the relay will disconnect sooner, according to the hot curve. I nom = Current value on ECA100-11 adjusted previously by the user. I nom term is referred to FLA (Full Load Amperage) adjustable on the product.

## Modbus Register Mapping

| Register Address | Name | Read/Write | Min | Max | Size | Units | Format | Factory Setting |
|---|---|---|---|---|---|---|---|---|
| 00000 | PRODUCT_ID | R | 16 | 16 | 1 | | F0 | 16 |
| 00001 | MODEL | R | 2 | 36 | 1 | | F1 | |
| 00002 | VERSION | R | 0 | 255 | 1 | | F2 | |
| 00003 | MODBUS ADDRESS | R/W | 1 | 127 | 1 | | F3 | 1 |
| 00010 | LAST_FAILURE_POINTER | R/W | 0 | 20 | 1 | | F6 | |
| 00011 | TOTAL_NUMBER_OF_FAULTS | R/W | 0 | 20 | 1 | | F6 | |
| 00012 | CONTROL_ON_OFF | R/W | 0 | 5 | 1 | | F10 | |
| 00014 | (TC) START UP DELAY | R | 0 | 202 | 1 | | F30 | |
| 00015 | ACCUMULATED_HEAT | R | 0 | 65530 | 1 | | F31 | |
| 00017 | FREQUENCY | R | 95 | 244 | 1 | | F32 | |
| 00018 | PHASE | R | 0 | 100 | 1 | % | F33 | |
| 00019 | VL3L1 | R | 0 | 255 | 1 | | F20 | |
| 00020 | VL1L2 | R | 0 | 255 | 1 | | F20 | |
| 00021 | VL2L3 | R | 0 | 255 | 1 | | F20 | |
| 00022 | IC | R | 0 | 255 | 1 | | F34 | |
| 00023 | IA | R | 0 | 255 | 1 | | F34 | |
| 00024 | IB | R | 0 | 255 | 1 | | F34 | |
| 00025 | (FLA) CURRENT SETTING | R | 18 | 73 | 1 | | F43 | |
| 00026 | (TC) START UP DELAY SETTING | R | 2 | 150 | 1 | | F29 | |
| 00027 | START MODE | R | 0 | 1 | 1 | | F19 | 0 |
| 00028 | MOTOR THERMAL CLASS | R | 3 | 10 | 1 | | F6 | |
| 0029-0049 | FAULT 01/20 - 20/20 | R | | | | | | |

---

**Document Date:** 25/01/2022