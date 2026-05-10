```markdown
---
title: "GIII+ Electronic Total Motor Protection Relay - Manual"
type: Technical
source: "GIII-MAN-V3-US.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GIII+"
date_processed: "2026-05-09"
---

# GIII+ Electronic Total Motor Protection Relay

## Overview

GIII+ is an electronic Total Motor Protection Relay that constantly supervises the Motor Current and the main electrical parameters such as Voltage, Power Factor, Real power, Reactive power and Energy consumption, giving the most reliable protection against Overload, Phase failure, Phase reversal, Single phasing and Unbalanced conditions.

### Design Environment

This product has been designed for industrial environment. Use of this product in residential environment may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

### Safety Warnings

**WARNING:** Only qualified technicians with knowledge about overload relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in equipment damage and/or personal injury.

**WARNING:** This product may start automatically; the user must take cautions to avoid hazards to people.

## 4.2 Instructions for Mechanical Installation with CT Box

Once you have assembled CT Box on GIII, follow these mounting instructions:

a) Place GIII at inclined position so that its back side (CT Box) must be placed toward the upper edge of the DIN Rail and then push down GIII relay as shown in figure until it does CLICK on the rail.

## Recommendation for Wiring

- Avoid over tightening M 2.5 screws upon terminals during wiring connection. Torque max: 4.5 Ib-in (5.18 kgf-cm).
- Wire Strip Length: 7-8 mm.
- Terminals wiring size: Between 12 AWG and 18 AWG.
- Maximum diameter of CT Box Holes wiring size: AWG 0 (18 mm).
- Use three CT holes for pass wiring to 3 phases motor. Using less than three wires may cause undesired current unbalance.
- Connect L1L2L3 terminal for Voltage Input in parallel connection before line starter circuit through Contactor (as shown in Connection Diagram).

## 7. Main Adjustment Menu

Phase Reversal (PR) adjustment available in main menu.

Additional menu options: DAY, MONTH adjustments.

## 9.1 GIII Recommended Values for Adjustable Parameters

### Selection of the Thermal Class of the Motor

**Class 5:** Little motors with fast acceleration, that requires been protected by faster detection of overload.

**Class 10 (Fast):** Motors used in compressor, refrigeration equipment, submersible pumps and motors of general purpose usually classified under standard IEC, that reach continual operation speed in less than 4 seconds.

**Class 15:** Motors for specialized applications.

**Class 20 (standard):** Motors of general purpose qualified under NEMA standard.

**Class 30 (slow):** Motors for charge of high inertia (times that exceed 10 seconds).

### Undervoltage (UV) and Overvoltage (OV)

Manufacturers usually offer motors with limited range of operation voltage inside of ±10% of nominal value.

Example: a protector installed for a motor of 220V should be adjusted in:
- UV = 220 × 90% = 198V (Undervoltage)
- OV = 220 × 110% = 242V (Overvoltage)

### Voltage Unbalance

According to NEMA MG1 standard, it is recommended that motors operate with an unbalance voltage less than 5%.

### Overload (OL)

The recommended value for the protection against the overload is inside the range of 110% to 120% of nominal current (In) or the current specified in the motor nameplate at maximum charge (FLA).

- IN = FLA motor nameplate
- OL = Service factor motor nameplate

### Underload by Current (%In)

When chosen to protect against the charge loss through current monitoring, a recommended value by default of 80% of the current at maximum charge (FLA) specified by the manufacturer is suggested.

### Underload by Power Factor (PF)

- Applicable to motors over dimensioned that requires protection against charge loss during the startup.
- Example: submersible pumps of gas stations, etc.
- When chosen to protect against charge loss through monitoring the power factor (PF), the GIII comes adjusted from factory with 0.5. (Although the protection can be adjusted in a range of 0.1 to 0.9 FP, adjustment above 0.3 FP is recommended).

## 11 GIII+ Connection Diagram with External Current Transformers

**Applicable Models:**
- GIII+208000
- GIII+480000

### Notes on External Current Transformers

a) The models identified as GIII+208000 and GIII+480000 are used exclusively with external CT. These models are designed to protect motors up to 660A nominal current.

b) The user must specify the nominal motor current. With this information, select the rank of current according to the attached table, in which you will find the relation "/5" required to select the CT to install.

c) The user must set up the GIII+ with external CT adding the instructions of adjustments contained in this application note. All other functions and protections will remain as specified in the installation instructions for GIII+.

d) The calibration of the GIII+ remains warrantee, as long as the external CT are commercial units of class 1, secondary 5A.

### Current Transformer Selection Table

| Rank of Nominal Current Min. | Max. | Relation /5 |
|-----|-----|-----|
| 150 | 200 | 600 |
| 190 | 250 | 750 |
| 200 | 260 | 800 |
| 250 | 330 | 1000 |
| 300 | 350 | 1200 |
| 375 | 500 | 1500 |
| 500 | 660 | 2000 |

**Example:** If a motor consumes a nominal current of 350 amperes, the external toroids to select will be a value of 1200/5.

## 11.1 Adjustment of the External CT and Nominal Current in the Current Protection Menu

a) Press Up & Down Combination since the Operation screen to access adjustment menus.

g) Press Up & Down combination to get to NOMINAL I setting (e.g., 300A).

Current display example:
- VL1L2, VL2L3, VL3L1, VUB voltage readings
- I1, I2, I3, CUB current readings
- CT ratio selection (e.g., CT 1200/5)

```