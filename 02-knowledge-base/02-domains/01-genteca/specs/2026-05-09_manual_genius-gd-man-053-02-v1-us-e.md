```markdown
---
title: "Relayne GSPT Installation Instructions"
type: Technical
source: "GD-MAN-053-02-V1-US-E.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GSPT"
date_processed: "2026-05-09"
---

# Relayne GSPT Installation Instructions

## 1 GSPT General Description

GSPT is an electronic Submersible Pump Integral Protection Relay that constantly supervises the Motor Current and the main electrical parameters such as Voltage, Frequency, Power factor, Real power, Reactive power and Energy consumption, giving the most reliable protection against Overload, Phase failure, Phase reversal, Single phasing, Unbalanced conditions, Overtemperature and excessive Starts per hour.

### Warnings and Cautions

**WARNING:** Only qualified technicians with knowledge about overload relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

**WARNING:** This product may start automatically, the user must take cautions to avoid hazards to people.

**CAUTION:** This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

**CAUTION:** An incorrectly applied or installed GSPT can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the GSPT.

## 2 GSPT Parts and Pieces

1. LCD display
2. Indicator light (LED): Status Relay, Failure
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

### Instructions for Mechanical Installation

**CAUTION:** GSPT must be installed in an accessible position free from dust, dirt, dampness and vibration. Allow enough space for air circulation around the enclosure and easy access to all operator controls. Indoors use only.

Place GSPT at inclined position with its back side placed toward the upper edge of the DIN Rail and push down GSPT relay until it does CLICK on the rail.

## 4 GSPT Flat Surface Mounting

### Instructions for Mechanical Installation

a) Take off the two (2) attachable mountings ears located at back side of GSPT, insert and slip both attachable mounting ears into the GSPT back side grooves.

b) Place GSPT over flat surface panel and fix it handling a screwdriver suitable for screws 3/16" x 1/2".

**Recommendation for Flat Surface Mounting:** Make two (2) holes (5/32") on panel surface before installing. Reference the Guide for Flat Surface Mounting shown in point 5 (GSPT General Dimensions).

## 5 GSPT General Dimensions

- Height: 92 mm
- Width: 72 mm
- Depth: 69 mm
- Mounting hole diameter: 5/32"
- Mounting hole spacing: 19 mm (vertical reference)

## 6 GSPT Connection Diagram

### Warning

**WARNING (Risk of Electric Shock):** Disconnect power supply before installing GSPT. Electric Shock will result in death or serious injury.

### Terminal Description

| Terminal | Description |
|----------|-------------|
| L1 | Voltage Input (Phase R) |
| L2 | Voltage Input (Phase S) |
| L3 | Voltage Input (Phase T) |
| 95 | Contact for Auxiliary Relay |
| 96 | Contact for Auxiliary Relay |
| 97 | Contact for Trip Relay |
| 98 | Contact for Trip Relay |

### Relay Contact Status

| Condition | 95-96 | 97-98 |
|-----------|-------|-------|
| Tripped | Connected | Open |
| Normal | Open | Connected |

### Recommendations for Wiring

- Avoid over tightening the M3 screws upon terminals during wiring. Tightening Torque: 4.4 lbf-in, 5.1 Kgf-cm
- Wire Strip Length: 6-7 mm
- Terminal wiring size: ≥ AWG 10 (4mm²) ≤ AWG 18
- Current Sensing Holes (conduits) wiring size: ≥ AWG 4 (11mm)
- Connect L1 L2 L3 terminal for Voltage Input in parallel connection before line starter circuit through Contactor (as shown in Basic Diagram Installation)
- Use three Current Sensing Holes for passing wires before connection to 3 phases motor. Using less than three (3) wires shall cause current unbalance wrong measures

### 6.1 Basic Diagram Installation

Connection through Circuit Breaker, Contactor, Fuses (5A, 600V options), and GSPT to submersible pump motor. Alarm light connections available as options.

### 6.2 Caution

**CAUTION:** Check that the voltage and current of chosen GSPT model correspond to line voltage and motor current.

## 7 GSPT Operation

GSPT constantly supervises current and voltage values; when any harmful condition occurs, the output connection is deactivated until the fault disappears and power line conditions returns to an acceptable level and system gets cool. Specific timing such as Start Up Delay and Fault Detection Delay are incorporated to prevent nuisance tripping due to rapid power fluctuations.

GSPT provides LCD Display to indicate the output status (voltage, current, unbalance, frequency and load status). Also provides four (4) push buttons (On/Off, Up, Down and Select) for electrical parameter adjustment such as Voltage, Current, Frequency, Fault Detection Delay and others. A Communication Port with MODBUS RTU protocol is included in GSPT.

If any fault repeats 3 or more times within 30 minutes GSPT disconnects output connection and only will be re-activated by pressing REARM pushbutton manually. It is recommended to verify the cause of faults before trying to rearm system.

## 8 GSPT Dismounting

### 8.1 Instructions for Mechanical Dismounting (DIN Rail)

a) Handling a Flat Screwdriver, pull downward the mounting bracket that you can see at rear and down side of GSPT.

b) With screwdriver at position (2), pull out GSPT from DIN Rail as shown in figure.

**Recommendation for DIN Rail Dismounting:** Pull downward 2 mm with a soft movement when using screwdriver for dismounting. Strong movement could break the supporting bracket.

### 8.2 Instructions for Mechanical Dismounting (Flat Surface)

Unscrew bolts securing GSPT to flat surface panel.
```