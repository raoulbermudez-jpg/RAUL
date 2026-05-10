```markdown
---
title: "Relayne GII Installation Instructions"
type: Technical
source: "GII-MANUAL V1.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GII"
date_processed: "2026-05-09"
---

# Relayne GII Installation Instructions

## 1 GII General Description

GII is an electronic Phase Voltage Relay that constantly supervises line voltage values, to protect electric loads and distribution power systems from failure and damage due to common voltage faults. Provides LCD Display to indicate the output status (see more details in User Manual).

**WARNING:** Only qualified technicians with knowledge about protection relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

**WARNING:** This product may start automatically; the user must take cautions to avoid hazards to people.

**CAUTION:** This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

**CAUTION:** An incorrectly applied or installed GII can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the GII.

## 2 GII Parts and Pieces

### Front Side View
1. **Indicator Lights (LED's)**
   - Normal (ON) - Continuous Green
   - Start Delay (TC) - Blinking Green
   - Fault - Continuous Red
2. **LCD Display**
3. **Start Push Button**
4. **Adjustment Push Buttons**
5. **Select Push Button**
6. **Flush Mounting Attachment**
7. **Flush Mounting Bracket**
8. **Back Groove for DIN RAIL Mounting**
9. **Attachable Mounting Ear for Flat Surface Mounting**
10. **Supporting Bracket**
11. **Plug-In Terminals**
12. **GIO PORT (Communication Port)**
13. **GIO PORT cover**

## 3 GII DIN RAIL Mounting

**CAUTION:** GII must be installed in an accessible position free from dust, dirt, dampness and vibration. Allow enough space for air circulation around the enclosure and easy access available to all operator controls. Indoors use only.

### Instructions for Mechanical Installation

Place GII at inclined position with its back side placed toward the upper edge of the DIN Rail and push down GII relay until it does CLICK on the rail.

## 4 GII Flat Surface Mounting

### Instructions for Mechanical Installation

a) Take off the two (2) mounting ears located at back side of GII and remove the flush mounting attachment and flush mounting bracket. Insert and slip both mounting ears into the GII back side grooves.

b) Place GII over flat surface panel and fix it handling a screwdriver suitable for screws 3/16" x 1/2".

### Recommendation for Flat Surface Mounting

Make two (2) holes (5/32") on panel surface before installing. See as reference the Guide for Flat Surface Mounting shown in point 6 (GII General Dimensions).

## 5 GII General Dimensions

### GII Flush Mounting
- Width: 124 mm
- Height: 105 mm
- Depth: 86 mm

### Guide for Flat Surface Mounting
- Panel cutout width: 111 mm
- Panel cutout height: 64.5 mm
- Tolerance: +/- 2 mm
- Hole diameter: 5/32"
- Hole spacing vertical: 85 mm
- Hole spacing horizontal: 8.99 mm

## 6 GII Flush Mounting Installation

### Instructions for Mechanical Installation

a) Cutout the panel surface according to shape and size specified in the Guide for Flush Surface Mounting.

b) Remove the flush mounting brackets and flush mounting attachment. To remove the flush mounting brackets pull out and slide them as shown in the instructions.

c) Insert the Relayne GII flush mounting attachment into the panel.

d) Place the Relayne GII in the backside of the panel and use the flush mounting brackets to fix GII until it does CLICK.

**CAUTION:** Check that the voltage of chosen GII model corresponds to line voltage.

## 7 GII Connection Diagram

**WARNING:** (Risk of Electric Shock). Disconnect power supply before installing GII. Electric shock will result in death or serious injury.

### 7.1 Terminal Designation

| Terminal | Description |
|----------|-------------|
| L1 | Voltage Input (Phase R) |
| L3 | Voltage Input (Phase S) |
| L5 | Voltage Input (Phase T) |
| 2, 4, 6, 7, 9, 11 | Not used |
| 8 | Trip Relay |
| 10 | Common |
| 12 | Aux. Relay (Alarm) |

**Relay Output States:**
- Tripped: 10-12 connected, 8-10 open
- Normal: 10-12 open, 8-10 connected

### 7.2 Basic Diagram Installation

The GII is connected to a three-phase 50/60 Hz power supply (3~) with voltage inputs on L1, L2, and L3. The relay output controls a circuit breaker and contactor. An alarm output (optional) is available. Fusibles rated 5A, 600V are used for protection.

## 8 Relayne GII Operation

Relayne GII constantly supervises line voltages values; when any harmful condition occurs, the output is deactivated until the fault disappears and power line condition returns to acceptable levels. Start Up Delay (TC) and Trip Delay (TD) are incorporated to prevent nuisance tripping due to rapid power fluctuations.

Use Start push button for restart load when GII is set for Manual Mode.

Relayne GII provides LCD Display to indicate the output status and failure (voltage, unbalance, frequency load status) and historical registration of the last twenty detected failures. It also provides four (4) push buttons (Start, Adjustment and Select) for electrical parameter adjustments such as Maximum and Minimum allowed Voltage (OV and UV), Frequency Shift (FS), Trip Delay (TD), Start Up Delay (TC) and others. A Communication port with MODBUS RTU protocol is included in Relayne GII.

### 8.1 Parameters Adjustment

**Description of Relayne GII push buttons:**

| Push Button | Label | Function |
|-------------|-------|----------|
| START | START | Activation of the restart mode when GII is set for Manual Mode |
| ADJUSTMENT | ADJUSTMENT | Browse up and down on any screen of the menu. Pressed simultaneously are used to enter to the menu |
| SELECT | SELECT | (Function continued in full manual) |
```