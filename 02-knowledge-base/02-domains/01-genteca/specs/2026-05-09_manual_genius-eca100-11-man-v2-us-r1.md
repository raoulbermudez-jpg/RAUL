---
title: "ECA100-11 Motor Protection Relay - Installation Instructions"
type: Technical
source: "ECA100-11_MAN_V2_US_R1.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "ECA100-11"
date_processed: "2026-05-09"
---

# ECA100-11 Motor Protection Relay Installation Instructions

## General Description

ECA100-11 is an electronic three-phase relay specially designed to protect air conditioning and refrigeration compressors and ventilation motors from failure causes related to current and voltage.

### Warnings and Cautions

**WARNING:** Only qualified electrical technicians with knowledge of overload relays and associated machinery should perform the installation, starting up, and maintenance of the system. Adhere to all local and national electric codes. Disconnect all electrical power at the source prior to any installation or maintenance work. Failure to comply could result in equipment damage, personal injury, or even death.

**CAUTION:** This product has been designed for industrial environment use only. Use in residential environments may cause unwanted electromagnetic disturbances, in which case the user may be required to take adequate mitigation measures.

**CAUTION:** An incorrectly applied or installed ECA100-11 can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the ECA100-11.

**CAUTION:** ECA100-11 must be installed in an accessible position free from dust, dirt, dampness and vibrations. Allow enough space for air circulation around the enclosure and easy access to all operator controls. Indoors use only.

## Installation

### DIN Rail and Flat Surface Mounting

**DIN Rail Mounting:**
a) Take off the two (2) attachable mounting ears located at back side of ECA100-11, insert and slip both attachable mounting ears into the ECA100-11 back side grooves.

Place ECA100-11 at an inclined position with its back side placed toward the upper edge of the DIN Rail and push down ECA100-11 relay until it clicks on the rail.

**Flat Surface Mounting:**
Mount using two (2) #8 x 1/2 screws. Make two (2) holes (5/32") on panel surface before installing. Refer section 5 for dimensions.

## Connection Diagram and Wiring Recommendations

**WARNING:** Risk of Electric Shock. Disconnect power supply before installing ECA100-11. Electric shock will result in death or serious injury.

**CAUTION:** Check that the rated voltage and current of the selected ECA100-11 model corresponds to line voltage and motor current.

### Wiring Specifications

- Avoid over tightening the M3 screws upon terminals during wiring connection. Tightening Torque max. 4.4 lbf-in (5.1 kgf-cm).
- Wire Strip Length: 6-7 mm
- Terminal wiring size: AWG 10 (4 mm²) to AWG 18
- Current Sensing Holes (conduits) wiring size: AWG 4 (11 mm)
- Connect L1 L2 L3 terminal for Voltage input in parallel connection before line starter circuit through Contactor
- Feed the three phases going to the motor through the three current sensing holes. Using less than three (3) wires may cause undesired current unbalance.

## Adjustment

**ATTENTION:** Any accidental or intentional change of setting knob positions after overload adjustment will cause variations in the ECA100-11 protective performance from previous setup. In this case repeat the adjustment procedure indicated in section 6.1.

### Adjustment Procedure

g) Slowly turn right the current setting knob (FLA) up to desired protection level.

i) Using a flat screwdriver, turn the TC setting knob until you set the desired start delay (TC is the time between Voltage fault recovery and restart the system according to application needs).

**NOTICE:** In case the AUTO/MANUAL start mode slide-switch is set on MANUAL and the ECA100-11 relay trips due to any fault detection, you shall press START push button to re-activate the Contactor or Line Starter Circuit.

Although the AUTO/MANUAL start mode slide-switch is set on AUTO, pressing START push button is required if three (3) current failures have appeared in less than 30 minutes and qualified technicians have detected and solved causes of failures.

## Operation

### LED Diagnostics and Fault Conditions

ECA100-11 indicates any combination of fault conditions via LED diagnostics.

Frequent motor trips may indicate mechanical problems such as the condensing unit not being able to dissipate heat adequately, wiring operation problems, or damage to the contactor.

## Cold-Hot Curves

**Class 10** - Motor protector cold-hot curves available.

After the first stall/trip of the motor due to a fault condition, the protective relay will disconnect sooner, according to the hot curve.

*Inom term is referred to FLA (Full Load Amperage) adjustable on the product.

## How to Order ECA100-11

Available current range models:
- **012** – 3.5-12.5 A* (*Available only for 208 VAC model)
- **032** – 10-32 A
- **080** – 25-80 A

## Technical Specifications

| Parameter | 012 Model | 032 Model | 080 Model |
|-----------|-----------|-----------|-----------|
| Current measurement range, In | 0.7 - 125 | 2.0 - 320 | 4.0 - 800 |
| Operating voltage | 10 - 32 | — | — |

### Physical Specifications

- Material: PC, ABS, NYLON
- Enclosure rating: IP32
- IO Link RS485 communication available (purchased separately)

## Modbus Register Mapping

| Register Address | Name | Read/Write | Min | Max | Size | Format | Factory Setting |
|-----------------|------|-----------|-----|-----|------|--------|-----------------|
| 00000 | PRODUCT_ID | R | — | — | 16 | F0 | 16 |
| 00001 | MODEL | R | 2 | 36 | 1 | F1 | — |
| 00002 | VERSION | R | 0 | 255 | 1 | F2 | — |
| 00003 | MODBUS ADDRESS | R/W | 1 | 127 | 1 | F3 | 1 |
| 00010 | LAST_FAILURE_POINTER | R/W | 0 | 20 | 1 | F6 | — |
| 00011 | TOTAL_NUMBER_OF_FAULTS | R/W | 0 | 20 | 1 | F6 | — |
| 00012 | CONTROL_ON_OFF | R/W | 0 | 5 | 1 | F10 | — |
| 00013 | (TC) START UP DELAY | R | 0 | 150 | 1 | F29 | — |
| 00014 | FAULT | R | 0 | 202 | 1 | F30 | — |
| 00015 | OUTPUT | — | — | — | — | — | — |