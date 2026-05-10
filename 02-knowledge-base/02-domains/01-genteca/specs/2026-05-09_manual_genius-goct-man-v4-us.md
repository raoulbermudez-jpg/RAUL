```markdown
---
title: "GOCT Manual - User Guide"
type: Technical
source: "GOCT_MAN_V4_US.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GOCT"
date_processed: "2026-05-09"
---

# GOCT Manual

**Date:** 27/01/2022  
**Approved by:** Liliam Ramirez  
**Reviewed by:** Ana Mendez  
**Version:** 4

## Safety Warnings and Cautions

**WARNING:** Only qualified technicians with knowledge about protection relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in equipment damage and/or personal injury.

**CAUTION:** This product has been designed for industrial environment. Use of this product in residential environment may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

**CAUTION:** Check that the voltage and current of chosen GOCT model correspond to line voltage and motor current.

## Recommendations for Wiring

- Avoid over tightening the M3 screws upon terminals during wiring connection. Tightening Torque max. 4.4 Ibf-in (5.1 Kgf-cm).
- Wire Strip Length: 6-7 mm
- Terminal wiring size: AWG 10 (4 mm²) to AWG 18
- Current Sensing Holes (conduits) wiring size: AWG 4 (11 mm)
- Connect L1, L2, L3 terminals for Voltage input in parallel connection before line starter circuit through Contactor (as shown in Basic Diagram Installation)
- Use three Current Sensing Holes for passing wires before connection to 3 phases motor. Using less than three (3) wires shall cause current unbalance and wrong measures.

## Current Setting Adjustment

Slowly turn right the current setting knob (FLA) up to desired protection level.

## Start Mode Operation

**NOTICE:** In case the AUTO/MANUAL start mode slide-switch is set on MANUAL and the GOCT relay trips due to any fault detection, you shall press START push button to re-activate the Contactor or Line Starter Circuit.

Although the AUTO/MANUAL start mode slide-switch is set on AUTO, pressing START push button is required if three (3) current failures have appeared in less than 30 minutes and qualified technicians have detected and solved causes of failures.

## Modbus Register Mapping

| Register Address | Name | R/W | Min | Max | Size | Units | Format | Factory Setting |
|---|---|---|---|---|---|---|---|---|
| 00000 | FAULT HISTORY | R | 10 | 10 | F0 | - | 10 |
| 00001 | - | R | 2 | 36 | 1 | - | F1 |
| 00002 | PRODUCT_ID | R | 0 | 255 | 1 | - | F2 |
| 00003 | MODEL | R/W | 1 | 127 | 1 | - | F3 | 1 |
| 00006 | - | R/W | 0 | 20 | 1 | - | F6 |
| 00007 | - | R/W | 0 | 20 | 1 | - | F6 |
| 00008 | LAST_FAILURE_POINTER | R/W | 0 | 5 | 1 | - | F10 |
| 00009 | TOTAL_NUMBER_OF_FAULTS | R | 0 | 150 | 1 | - | F29 |
| 00010 | CONTROL_ON_OFF | R | 0 | 202 | 1 | - | F30 |
| 00011 | (TC) START UP DELAY | R | 0 | 65530 | 1 | - | F31 |
| 00013 | FAULT | R | 95 | 244 | 1 | - | F32 |
| 00014 | ACUMULATED_HEAT | R | 0 | 100 | 1 | % | F33 |
| 00015 | FREQUENCY | R | 0 | 255 | 1 | - | F20 |
| 00016 | PHASE | R | 0 | 255 | 1 | - | F20 |
| 00017 | VL3L1 | R | 0 | 255 | 1 | - | F20 |
| 00018 | VL1L2 | R | 0 | 255 | 1 | - | F34 |
| 00019 | VL2L3 | R | 0 | 255 | 1 | - | F34 |
| 00020 | V AVERAGE | R | 0 | 255 | 1 | - | F34 |
| 00021 | IC | R | 18 | 73 | 1 | - | F43 |
| 00022 | IA | R | 2 | 150 | 1 | - | F29 |
| 00023 | IB | R | 0 | 1 | 1 | - | F19 | 0 |
| 00024 | I AVERAGE | R | 3 | 10 | 1 | - | F6 |
| 0025-0044 | SCHEDULE TIMER START MODE | R | 0 | 202 | 1 | - | F30 |

**WARNING:** These registers should not be modified by the user.

## Modbus Data Format

### F0 - Product ID
- Type: 8 bits
- Description: PRODUCT ID = 16 (GOC-T)

### F1 - Product Model
- Type: 8 bits
- Bits 2...0: VOLTAGE MODEL (1 to 4)
  - 2 = 208V
  - 4 = 480V
- Bits 4...3: Reserved
- Bits 6...5: Reserved
- Bit 7: Reserved
- Bits 5...3: CURRENT MODEL (1 to 4)
  - 2 = 12A@GOC
  - 3 = 32A@GOC
  - 4 = 80A@GOC

### F2 - Software Version
- Type: 8 bits
- Bits 4...0: Software Version - Minor Number (0 to 31)
- Bits 7...5: Software Version - Major Number (0 to 7)

### F3 - Model
- Type: 16 bits
- Byte 0: Address (1 to 127)
- Byte 1: Null (not used)

### F6 - Unsigned Char
- Type: 16 bits
- Byte 0: Value
- Byte 1: Null (not used)

### F10 - Adjustment Control On/Off
- Type: 16 bits
- 0 = ON
- 1 = OFF - FAILURE MODE
- 2 = OFF - TRIP DELAY BECAUSE OF VOLTAGE FAILURES
- 3 = OFF - MODBUS
- 4 = OFF - MANUAL MODE
- 5 = OFF - 3RD FAILURE

### F19 - Start Mode
- Type: 1 bit
- 0 = MANUAL
- 1 = AUTO

### F20 - Voltage Calculation (GOC)
- Type: 8 bits
- Formula: VOLTAGE = f_Vnom × (Value / 300 + 0.6) [V]
- f_Vnom = 214 @ Voltage Model = 208V
- f_Vnom = 460 @ Voltage Model = 480V

### F29 - Start Up Delay (GOC)
- Type: 16 bits
- Formula: START UP = ((2 × Value) + 1) [s]

### F30 - Fault History Register (GOC)
- Type: 8 bits
- Bit 0: OV - Over Voltage
- Bit 1: UV - Under Voltage
- Bit 2: CUB - Current Unbalance
- Bit 3: V