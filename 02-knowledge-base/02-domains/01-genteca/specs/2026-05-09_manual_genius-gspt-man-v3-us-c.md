---
title: "GSPT Installation Instructions"
type: Technical
source: "GSPT_MAN_V3_US_c.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GSPT"
date_processed: "2026-05-09"
---

# GSPT Installation Instructions

## 1 GSPT General Description

GSPT is an electronic Submersible Pump Integral Protection Relay that constantly supervises the Motor Current and the main electrical parameters such as Voltage, Frequency, Power factor, Real power, Reactive power and Energy consumption, giving the most reliable protection against Overload, Phase failure, Phase reversal, Single phasing, Unbalanced conditions, Overtemperature, and excessive Starts per hour.

**WARNING:** Only qualified technicians with knowledge about protection relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in equipment damage and/or personal injury.

**WARNING:** This product may Start automatically; the user must take cautions to avoid hazards to people.

**CAUTION:** This product has been designed for industrial environment. Use of this product in residential environment may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

**CAUTION:** An incorrectly applied or installed GSPT can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the GSPT.

## 2 GSPT Parts and Pieces

1. LCD display
2. Indicator light (LED):
   - Status Relay
   - Failure
3. START Push Button
4. ADJUST Push Buttons (Up & Down)
5. SELECT Push Button
6. Back Groove for DIN Rail mounting
7. Attachable Mounting Ears
8. Supporting Bracket
9. Holes with current sensors, to pass power cables to the motor
10. L1 L2 L3 input
11. Control Relay (95-96) & (97-98)
12. GIO PORT
13. Protective plastic cover of the GIO PORT

## 3 GSPT DIN Rail Mounting

**Instructions for Mechanical Installation**

**CAUTION:** GSPT must be installed in an accessible position free from dust, dirt, dampness and vibration. Allow enough space for air circulation around the enclosure and easy access to all operator controls. Indoors use only.

Place GSPT at inclined position with its back side placed toward the upper edge of the DIN Rail and push down GSPT relay until it CLICKS on the rail.

## 4 GSPT Flat Surface Mounting

**Instructions for Mechanical Installation**

a) Take off the two (2) attachable mounting ears located at back side of GSPT, insert and slip both attachable mounting ears into the GSPT back side grooves.

b) Place GSPT over flat surface panel and fix it using a screwdriver suitable for screws 3/16" x 1/2".

**Recommendation for Flat Surface Mounting:** Make two (2) holes (5/32") on panel surface before installing.

## 5 GSPT General Dimensions

- Width: 72 mm
- Height: 92 mm
- Guide for Flat Surface Mounting: 69 mm width reference

## 6 GSPT Connection Diagram

**WARNING:** (Risk of Electric Shock). Disconnect power supply before installing GSPT. Electric Shock will result in death or serious injury.

### 6.1 Terminal Designation

| Terminal | Description |
|----------|-------------|
| L1 | Voltage Input (Phase R) |
| L2 | Voltage Input (Phase S) |
| L3 | Voltage Input (Phase T) |
| 95 | Contact for Auxiliary Relay |
| 96 | Contact for Auxiliary Relay |
| 97 | Contact for Trip Relay |
| 98 | Contact for Trip Relay |

**Relay Status:**
- 95-96: Normal (Closed), Tripped (Open)
- 97-98: Normal (Open), Tripped (Closed)

### 6.2 Basic Diagram Installation

Connection includes Circuit Breaker, Contactor, Fuses (5A, 600V options), GSPT unit with L1 L2 L3 inputs, Control Coil connections, and Alarm Light output.

### Recommendations for Wiring

- Avoid over tightening the M3 screws upon terminals during wiring connection. Tightening Torque max. 4.4 Ibf-in (5.1 Kgf-cm).
- Wire Strip Length: 6-7 mm
- Terminal wiring size: AWG 10 (4 mm²) to AWG 18
- Current Sensing Holes (conduits) wiring size: AWG 4 (11 mm)
- Connect L1 L2 L3 terminal for Voltage input in parallel connection before line starter circuit through Contactor (as shown in Basic Diagram Installation)
- Use three Current Sensing Holes for passing wires before connection to 3 phases motor. Using less than three (3) wires shall cause current unbalance and wrong measures.
- Check that the voltage and current of chosen GSPT model correspond to line voltage and motor current.

## 7 GSPT Operation

GSPT constantly supervises current and voltage values; when any harmful condition occurs, the output connection is deactivated until the fault disappears and power line conditions returns to an acceptable level. Specific timing such as Start Up Delay and Fault Detection Delay are incorporated to prevent nuisance tripping due to rapid power fluctuations.

GSPT provides LCD Display to indicate the output status (voltage, current, unbalance, frequency and load status). Also provides four (4) push buttons (On/Off, Up, Down and Select) for electrical parameter adjustment such as Voltage, Current, Frequency, Fault Detection Delay and others. Besides these mentioned advantages, a Communication Port with MODBUS RTU protocol is included in GSPT.

## 8 GSPT Dismounting Instructions

**WARNING:** Disconnect power supply (Circuit Breaker OFF) and electrical connections before dismounting.

### 8.1 Instructions for Mechanical Dismounting (DIN Rail)

a) Using a Flat Screwdriver, pull downward the mounting bracket that can be seen at rear and down side of GSPT.

b) With screwdriver at position (2), pull out GSPT from DIN Rail as shown in figure.

**Recommendation for DIN Rail Dismounting:** Pull downward 2 mm with a soft movement when using screwdriver for dismounting. Strong movement could break the supporting bracket.

### 8.2 Instructions for Mechanical Dismounting (Flat Surface)

Unscrew both screws fixed on Flat Surface through attachable mounting ears and then pull out the GSPT relay from flat surface as shown in figure.