```markdown
---
title: "Relayne GUCT Installation Instructions"
type: Technical
source: "GUCT INSTALLATION INSTRUCTIONS END.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GUCT"
date_processed: "2026-05-09"
---

# Relayne GUCT Installation Instructions

## 1 GUCT General Description

GUCT is an electronic Integral Motor Protection Relay that constantly supervises motor current and power supply voltage, using a thermal model algorithm to protect your motor against undercurrent and overload conditions and voltage failures.

**WARNING:** Only qualified technicians with knowledge about overload relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

**CAUTION:** This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

**CAUTION:** This product may start automatically. The user must take cautions to avoid hazards to people.

**CAUTION:** An incorrectly applied or installed GUCT can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the GUCT.

**CAUTION:** GUCT must be installed in an accessible position free from dust, dirt, dampness and vibration. Allow enough space for air circulation around the enclosure and easy access to all operator controls.

## 2 GUCT Parts and Pieces

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

### Relay Contact Status:
- **95-96 connected, 97-98 open:** Tripped
- **95-96 open, 97-98 connected:** Normal

## 3 GUCT DIN Rail Mounting

**Instructions for Mechanical Installation:**

Place GUCT at inclined position with its back side placed toward the upper edge of the DIN Rail and push down GUCT relay until it CLICKS on the rail.

## 4 GUCT Flat Surface Mounting

**Instructions for Mechanical Installation:**

a) Take off the two (2) attachable mounting ears located at back side of GUCT, insert and slip both attachable mounting ears into the GUCT back side grooves.

b) Place GUCT over flat surface panel and fix it handling a screwdriver suitable for screws 3/16" x 1/2".

**Recommendation for Flat Surface Mounting:** Make two (2) holes (5/32") on panel surface before installing. Refer to the Guide for Flat Surface Mounting shown in section 5.

## 5 GUCT General Dimensions

Mounting reference dimensions:
- Width: 92 mm
- Height: 111 mm
- Depth: 72 mm
- Flat surface mounting hole diameter: 5/32"

Guide for Flat Surface Mounting hole spacing: 69 mm vertical, 19 mm horizontal reference points.

## 6 GUCT Connection Diagram

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

**Relay Contact Status:**
- **95-96 Connected, 97-98 Open:** Tripped
- **95-96 Open, 97-98 Connected:** Normal

### 6.2 Basic Diagram Installation

**WARNING:** Risk of Electric Shock. Disconnect power supply before installing GUCT. Electric Shock will result in death or serious injury.

**Recommendations for Wiring:**

- Avoid over tightening the M3 screws upon terminals during wiring connection. Tightening Torque: 4.4 lbf-in, 5.1 Kgf-cm.
- Wire Strip Length: 6-7 mm
- Terminal wiring size: ≥ AWG 10 (4 mm²) ≤ AWG 18
- Current Sensing Holes (conduits) wiring size: ≥ AWG 4 (11 mm)
- Connect L1 L2 L3 terminal for Voltage Input in parallel connection before line starter circuit through Contactor (as shown in Basic Diagram Installation)
- Use three Current Sensing Holes for passing wires before connection to 3 phases motor. Using less than three (3) wires shall cause current unbalance and wrong measures.

**CAUTION:** Check that the voltage and current of chosen GUCT model correspond to line voltage and motor current.

**Basic Diagram Components:**
- Circuit Breaker
- Fuses (Optional) 5A, 600V
- Contactor with coil
- Three-phase motor (3~)
- GUCT with L1, L2, L3 voltage inputs and I1, I2, I3 current sensing inputs
- Relay contacts (95, 96, 97, 98)
- GIO Port for communication

## 7 GUCT Operation

GUCT constantly supervises current and voltage values; when any harmful condition occurs, the output connection is deactivated until the fault disappears and power line conditions returns to an acceptable level. Specific timing such as Start Up Delay and Fault Detection Delay are incorporated to prevent nuisance tripping due to rapid power fluctuations.

GUCT provides LCD Display to indicate the output status (voltage, current, unbalance, frequency and load status). Also provides four (4) push buttons (On/Off, Up, Down and Select) for electrical parameter adjustment such as Voltage, Current, Frequency, Fault Detection Delay and others. Besides these mentioned advantages, a Communication Port with MODBUS RTU protocol is included in GUCT.

## 8 GUCT Dismounting Instructions

**WARNING:** Disconnect power supply (Circuit Breaker OFF) and electrical wiring before dismounting.

### 8.1 Instructions for Mechanical Dismounting (DIN Rail)

a) Handling a Flat Screwdriver, pull downward the mounting bracket that you can see at rear and down side of GUCT.

b) With screwdriver at position (2), pull out GUCT from DIN Rail as shown in figure.

**Recommendation for DIN Rail Dismounting:** Pull downward 2 mm with a soft movement when using screwdriver for dismounting. Strong movement could break the supporting bracket.

### 8.2 Instructions for Mechanical Dismounting (Flat Surface)

Unscrew both screws fixed on Flat Surface through attachable mounting ears and then pull out the GUCT relay from flat surface as shown in figure.
```