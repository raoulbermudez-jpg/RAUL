```markdown
---
title: "GUCT Installation Instructions"
type: Technical
source: "GD-MAN-051-01-V2-US-C.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GUCT"
date_processed: "2026-05-09"
---

# GUCT Installation Instructions

## 1. GUCT General Description

GUCT is an electronic Motor Protection Integral Relay that constantly supervises motor current and power supply voltage, using a thermal model algorithm to protect your motor against undercurrent and overload conditions and voltage failures (see more details in User Manual).

### Warnings and Cautions

**WARNING:** Only qualified technicians with knowledge about overload relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

**WARNING:** (Risk of Electric Shock). Disconnect power supply before installing GUCT. Electric Shock will result in death or serious injury.

**CAUTION:** This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

**CAUTION:** An incorrectly applied or installed GUCT can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the GUCT.

**CAUTION:** This product may start automatically; the user must take cautions to avoid hazards to people.

**CAUTION:** GUCT must be installed in an accessible position free from dust, dirt, dampness and vibration. Allow enough space for air circulation around the enclosure and easy access to all operator controls. Indoors use only.

## 2. GUCT Parts and Pieces

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

**95-96 connected / 97-98 open** = Tripped

**95-96 open / 97-98 connected** = Normal

## 3. GUCT DIN Rail Mounting

### Instructions for Mechanical Installation

Place GUCT at inclined position with its back side placed toward the upper edge of the DIN Rail and push down GUCT relay until it CLICKS on the rail.

## 4. GUCT Flat Surface Mounting

### Instructions for Mechanical Installation

a) Take off the two (2) attachable mounting ears located at back side of GUCT, insert and slip both attachable mounting ears into the GUCT back side grooves.

b) Place GUCT over flat surface panel and fix it handling a screwdriver suitable for screws 3/16" x 1/2".

### Recommendation for Flat Surface Mounting

Make two (2) holes (5/32") on panel surface before installing. Refer to the Guide for Flat Surface Mounting shown in section 5 (GUCT General Dimensions).

Guide dimensions:
- Panel width: 72 mm
- Panel height: 92 mm
- Hole diameter: 5/32"
- Mounting hole spacing: 69 mm (vertical)

## 5. GUCT General Dimensions

Panel mounting hole specifications:
- Hole diameter: 5/32"
- Panel width: 72 mm
- Panel height: 92 mm
- Vertical hole spacing: 69 mm
- Horizontal hole spacing: 19 mm

## 6. GUCT Connection Diagram

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

### Relay Contact Configuration

- **95-96 Connected / 97-98 Open** = Tripped
- **95-96 Open / 97-98 Connected** = Normal

### Recommendations for Wiring

- Avoid over tightening the M3 screws upon terminals during wiring connection. Tightening Torque: 4.4 lbf-in, 5.1 Kgf-cm.
- Wire Strip Length: 6-7 mm
- Terminal wiring size: ≥ AWG 10 (4 mm²) ≤ AWG 18
- Current Sensing Holes (conduits) wiring size: ≥ AWG 4 (11 mm)
- Connect L1 L2 L3 terminals for Voltage Input in parallel connection before line starter circuit through Contactor (as shown in Basic Diagram Installation)
- Use three Current Sensing Holes for passing wires before connection to 3 phases motor. Using less than three (3) wires shall cause current unbalance and wrong measures

**CAUTION:** Check that the voltage and current of chosen GUCT model correspond to line voltage and motor current.

### 6.2 Basic Diagram Installation

The installation diagram shows GUCT connected with:
- Circuit Breaker (5A, 600V options)
- Contactor with coil
- Three-phase motor (3~)
- Current sensing through holes I1, I2, I3
- Voltage inputs L1, L2, L3
- Relay contacts 95, 96, 97, 98
- GIO Port for communications
- Optional alarm light connection

### 6.3 Diagram Installation for External Toroids

[External toroids diagram reference provided in source document]

## 7. GUCT Operation

GUCT constantly supervises current and voltage values; when any harmful condition occurs, the output connection is deactivated until the fault disappears and power line conditions returns to an acceptable level. Specific timing such as Start Up Delay and Fault Detection Delay are incorporated to prevent nuisance tripping due to rapid power fluctuations.

GUCT provides LCD Display to indicate the output status (voltage, current, unbalance, frequency and load status). Also provides four (4) push buttons (On/Off, Up, Down and Select) for electrical parameter adjustment such as Voltage, Current, Frequency, Fault Detection Delay and others. Besides these mentioned advantages, a Communication Port with MODBUS RTU protocol is included in GUCT.

## 8. GUCT Dismounting Instructions

### 8.1 Instructions for Mechanical Dismounting (DIN Rail)

a) Handling a Flat Screwdriver, pull downward the mounting bracket that you can see at rear and down side of GUCT.

b) With screwdriver at position (2), pull out GUCT from DIN Rail.

**Recommendation for DIN Rail Dismounting:** Pull downward 2 mm with a soft movement when using screwdriver for dismounting. Strong movement could break the supporting bracket.

### 8.2 Instructions for Mechanical Dismounting (Flat Surface)

Unscrew both screws fixed on Flat Surface through attachable mounting ears and then pull out the GUCT relay from flat surface.
```