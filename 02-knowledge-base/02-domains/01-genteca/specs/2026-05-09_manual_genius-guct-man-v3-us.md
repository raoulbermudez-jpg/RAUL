```markdown
---
title: "GUCT Motor Protection Relay - User Manual"
type: Technical
source: "GUCT_MAN_V3_US.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GUCT"
date_processed: "2026-05-09"
---

# GUCT General Description

GUCT is an electronic Motor Protection Integral Relay that constantly supervises motor current and power supply voltage, using a thermal model algorithm to protect motor against undercurrent and overload conditions and voltage failures.

## Safety Warnings

**WARNING:** Only qualified technicians with knowledge about protection relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in equipment damage and/or personal injury.

**CAUTION:** This product has been designed for industrial environment. Use of this product in residential environment may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

**CAUTION:** An incorrectly applied or installed GUCT can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the GUCT.

**CAUTION:** This product may start automatically. The user must take cautions to avoid hazards to people.

## GUCT Parts and Pieces

1. LCD display
2. Indicator light (LEDs):
   - Status Relay
   - Failure
3. START Push Button
4. ADJUST Push Buttons (Up & Down)
5. SELECT Push Button
6. Back Groove for DIN Rail mounting
7. Attachable Mounting Ear for Flat Surface mounting
8. Supporting Brackets for DIN Rail mounting
9. Current Sensing Holes for motor wiring
10. Power Supply Voltage Input (L1 L2 L3)
11. Contacts for Relay (95-96) and (97-98)
12. GIO Port (for Serial Communication)
13. GIO PORT cover

### Relay Contact States

**Tripped:** 95-96 closed, 97-98 open

**Normal:** 95-96 open, 97-98 closed

# GUCT DIN Rail Mounting

## Instructions for Mechanical Installation

**CAUTION:** GUCT must be installed in an accessible position free from dust, dirt, dampness and vibration. Allow enough space for air circulation around the enclosure and easy access to all operator controls. Indoors use only.

Place GUCT at inclined position with its back side placed toward the upper edge of the DIN Rail and push down GUCT relay until it CLICK on the rail.

# GUCT Flat Surface Mounting

## Instructions for Mechanical Installation

a) Take off the two (2) attachable mounting ears located at back side of GUCT, insert and slip both attachable mounting ears into the GUCT back side grooves.

b) Place GUCT over flat surface panel and fix it handling a screwdriver suitable for screws 3/16" x 1/2".

### Recommendation for Flat Surface Mounting

Make two (2) holes (5/32") on panel surface before installing. See as reference the Guide for Flat Surface Mounting shown in GUCT General Dimensions section.

### General Dimensions

- Width: 72 mm
- Height: 92 mm
- Depth: 69 mm
- Mounting hole diameter: 5/32"

# GUCT Connection Diagram

**WARNING:** (Risk of Electric Shock). Disconnect power supply before installing GUCT. Electric Shock will result in death or serious injury.

## Terminal Description

| Terminal | Description |
|----------|-------------|
| L1 | Voltage Input (Phase R) |
| L2 | Voltage Input (Phase S) |
| L3 | Voltage Input (Phase T) |
| 95 | Contact for Auxiliary Relay |
| 96 | Contact for Auxiliary Relay |
| 97 | Contact for Trip Relay |
| 98 | Contact for Trip Relay |

## Basic Diagram Installation

GUCT connects in parallel with voltage input (L1 L2 L3) before the line starter circuit through a Contactor. Three Current Sensing Holes are used for passing motor phase wires.

Optional components include:
- Circuit Breaker (5A, 600V)
- Fuses (5A, 600V)
- GIO Port for serial communication
- Alarm light

## Terminal Designation and Wiring Recommendations

- Avoid over tightening the M3 screws upon terminals during wiring connection. Tightening Torque maximum: 4.4 lbf-in (5.1 kgf-cm).
- Wire Strip Length: 6-7 mm
- Terminal wiring size: AWG 10 (4 mm²) to AWG 18
- Current Sensing Holes (conduits) wiring size: AWG 4 (11 mm)
- Connect L1 L2 L3 terminal for Voltage input in parallel connection before line starter circuit through Contactor
- Use three Current Sensing Holes for passing wires before connection to 3 phases motor. Using less than three (3) wires shall cause current unbalance and wrong measures.

**CAUTION:** Check that the voltage and current of chosen GUCT model correspond to line voltage and motor current.

## Diagram Installation for External Toroids

External toroids can be connected via terminals X1 and H1 before line starter circuits for additional current sensing capability.

# GUCT Dismounting Instructions

**WARNING:** Disconnect power supply (Circuit Breaker OFF) and electrical wiring before dismounting GUCT. Electrical shock will result in death or serious injury.

## Instructions for Mechanical Dismounting (DIN Rail)

a) Handling a Flat Screwdriver, pull downward the mounting bracket that you can see at rear and down side of GUCT.

b) With screwdriver at position (2), pull out GUCT from DIN Rail.

### Recommendation for DIN Rail Dismounting

Pull downward 2 mm with a soft movement when using screwdriver for dismounting. Strong movement could break the supporting bracket.

## Instructions for Mechanical Dismounting (Flat Surface)

Unscrew both screws fixed on Flat Surface through attachable mounting ears and then pull out the GUCT relay from flat surface.

# GUCT Operation

GUCT constantly supervises current and voltage values; when any harmful condition occurs, the output connection is deactivated until the fault disappears and power line conditions return to an acceptable level. Specific timing such as Start Up Delay and Fault Detection Delay are incorporated to prevent nuisance tripping due to rapid power fluctuations.

GUCT provides LCD Display to indicate the output status (voltage, current, and protection status).

## Optional Features

Use GIO PLUG (Optional) for serial communication with other devices.
```