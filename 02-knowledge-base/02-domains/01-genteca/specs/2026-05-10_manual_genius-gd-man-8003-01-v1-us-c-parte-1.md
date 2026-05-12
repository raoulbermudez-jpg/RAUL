---
title: "GIII+MV Installation Manual"
type: Technical
source: "GD-MAN-8003-01-V1-US-C.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GIII+MV"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GIII+MV Installation Manual

## General Description

GIII+MV is an electronic Total motor Protection Relay that constantly supervises the Motor Current and the main electrical parameters such as Voltage, Frequency, Power factor, Real power, Reactive power and Energy consumption, giving the most reliable protection against Overload, Underload, Phase failure, Phase reversal, single phasing and Unbalanced conditions over temperature, excessive starts.

### Safety Warnings

**WARNING:** Only qualified technicians with knowledge about overload relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

**WARNING:** This product may start automatically, the user must take cautions to avoid hazards to people.

**WARNING:** Disconnect power supply before installing GIII+MV. Failure to comply may result in death or serious injury.

## GIII+MV Parts and Pieces

### Assembly Parts

1. Flush Mounting Attachment
2. Lateral Supporting Grooves (for Flush Mounting)
3. Flush Mounting Bracket
4. Attachable Mounting Ears
5. Supporting Bracket
6. Back Groove (for DIN RAIL Mounting)
7. PT100 Temperature Sensor Terminal
8. Digital Input Terminal
9. Communication RS-485 Terminal
10. L1 L2 L3 Voltage Terminal
11. Control Relay Terminal
12. Auxiliary Relay Terminal
13. CT Input Terminal

### General and Control Parts

14. Detachable CT Box
15. CT Box Guide Rail
16. LCD Display
17. GIO PORT
18. START Push Button
19. ADJUST Push Buttons (UP & DOWN)
20. SELECT Push Button
21. Indicator Light (LED) for Control Relay (Control ON)
22. Indicator Light (LED) for Auxiliary Relay (Aux. ON)

### Mounting Options

- Parts Nr. 1, 2, 3 shall be used only for Flush Mounting option
- Parts Nr. 4 shall be used only for Flat Surface Mounting option
- Parts Nr. 5 shall be used only for DIN RAIL Mounting option

## GIII+MV - CT BOX Assembly

### Caution

Each set of GIII+MV and attachable CT box is calibrated and have the same Factory Number. Before assembling the CT box verify that its factory number is the same as GIII+MV one. Failure to comply may result in a bigger measure error.

### Instructions for Assembly

a) Move the supporting brackets 2mm outside and push downward GIII+MV to CT BOX until back groove of relay can insert into CT BOX guide rail, using Alignment Mark as reference.

b) From Alignment Mark, move GIII+MV relay towards the left sliding through rail guide until it does Click.

### Instructions for Dismounting

a) Disconnect both CT Input Terminal used for GIII+MV and CT Box connection and pull down both supporting brackets by means of screwdrivers.

b) Move GIII+MV towards the right sliding through CT Box guide rail until it gets to alignment mark.

## DIN RAIL Mounting

### Caution

GIII+MV must be installed in an accessible position free from dust, dirt, dampness and vibration. Allow enough space for air circulation around the enclosure and easy access to all operator controls. Indoors use only.

### Instructions for Mechanical Installation without CT BOX

a) Place GIII+MV at inclined position and its back side must be placed toward the upper edge of the DIN Rail and then push down GIII+MV relay until it does CLICK on the rail.

### Instructions for Mechanical Installation with CT Box

Once you have assembled CT Box on GIII+MV (See Assembly section) you shall follow these mounting instructions:

a) Place GIII+MV at inclined position so that its back side (CT Box) must be placed toward the upper edge of the DIN Rail and then push down GIII+MV relay until it does CLICK on the rail.

## Flat Surface Mounting

### Instructions for Mechanical Installation without CT BOX

a) Take off the four (4) mounting ears at back side of GIII+MV, insert and slip both mounting ears into the GIII+MV back side grooves.

b) Place GIII+MV over flat surface panel and fix it handling a screwdriver suitable for screws 3/16" x 1/2".

**Recommendation for Flat Surface Mounting:**
Make four (4) holes (5/32") on panel surface before installing. Reference the Guide for Flat Surface mounting (Dimensions GIII+MV without Detachable CT Box).

### Instructions for Mechanical Installation with CT BOX

Once you have assembled Detachable CT Box on GIII+MV:

a) Take off the four (4) mounting ears at back side of CT Box. Insert and slip both mounting ears into the CT Box back side grooves.

b) Place GIII+MV with detachable CT Box over flat surface panel and fix it handling a screwdriver suitable for screws 3/16" x 1/2".

**Recommendation for Flat Surface Mounting:**
Make four (4) holes (5/32") on panel surface before installing. Reference the Guide for Flat Surface Mounting (Dimensions GIII+MV with Detachable CT Box).

## Flush Mounting

### Caution

For Flush Mounting option, Detachable CT Box shall not be assembled directly to GIII+MV but it can be installed into the panel and connected to GIII+MV through internal wiring. The maximum length for internal wiring should be 2 meters.

**ATTENTION:** Before you start with GIII+MV Flush mounting procedure, first follow the steps for the Detachable CT Box dismounting.

### Instructions for Mechanical Installation

a) Cutout the panel surface according to shape and size:
   - Width: 181.8 mm (Tolerance: ±2mm)
   - Height: 64.5 mm

b) Insert the GIII+MV Flush Mounting Attachment into the Panel Cutout from the Front position.

c) Move GIII+MV relay from back position toward the panel Cutout and insert its Flush Mount Attachment into the GIII+MV Lateral supporting grooves until it does click.

d) Insert both Lateral Brackets into the Flush Mounting Attachment until it does Click and GIII+MV has been fixed.

**Note:** GIII+MV factory serial must be identical to detachable CT box serial.

## General Dimensions

- Overall Height: 194.5 mm
- Overall Width: 157.8 mm
- Overall Depth: 106.8 mm
- Reference Height: 175 mm

### Guide for Flat Surface with CT Box

- Hole diameter: 5/32"
- Horizontal spacing: 152 mm
- Vertical spacing: 100 mm

### Guide for Flat Surface without CT Box

- Hole diameter: 5/32"
- Horizontal spacing: 152 mm
- Vertical spacing: 100 mm

## Connection Diagram

### Basic Installation Diagram

The circuit includes:
- Any Listed Circuit Breaker or fuse (User-supplied)
- 3-phase 50/60 Hz power input
- PT100 Temperature Sensor
- Digital Input connections
- RS-485 Communication
- Control Relay (normally closed, open when tripped)
- Auxiliary Relay (normally open, closed when tripped)
- Motor wiring through GIII+MV CT Box

### Terminal Designation

| Terminal | Description |
|----------|-------------|
| B1 | Voltage Input L1 (Phase R) |
| B3 | Voltage Input L2 (Phase S) |
| B5 | Voltage Input L3 (Phase T) |
| B6 | Control Relay (Closed when normally) |
| B8 | Control Relay (common) |
| B10 | Control Relay (Closed when tripped) |
| B11 | Auxiliary Relay (Closed when normally) |
| B13 | Auxiliary Relay (common) |
| B15 | Auxiliary Relay (Closed when tripped) |
| B16 | CT-A Input |
| B17 | CT-B Input |
| B18 | CT-C Input |
| B19-B20 | CT-D (Common secondary) |
| A8-A9-A10 | PT100 (Terminal A-B-B Sensor) |
| A11-A12 | Digital Input 1 (Dry Contacts only) |
| A14-A15 | Digital Input 2 (Dry Contacts only) |
| A18 | RS-485 S- (Negative Serial Comm) |
| A19 | RS-485 S+ (Positive Serial Comm) |
| A20 | RS-485 SG (Negative Signals for Serial Comm) |

### Wiring Recommendations

- Avoid over tightening M 2.5 screws upon terminals during wiring connection. Torque max: 4.5 lb-in (5.18 kgf-cm)
- Wire Strip Length: 7-8 mm
- Terminals wiring size: Between 12 AWG to 18 AWG
- Maximum diameter of CT Box Holes wiring size: AWG 0 (18 mm)
- Use three CT holes for pass wiring to 3 phases motor. Using less than three wires may cause non-desired current unbalance
- Connect L1 L2 L3 terminal for Voltage Input in parallel connection before line starter circuit through Contactor

### Surge Protective Device Requirements (User-supplied)

- UL Recognized SPDT Type 2
- Wiring configuration: 3-phase (DELTA or WYE or arrangement of 3 x 1-Ph)
- AC Power Frequency: 50 or 60 Hz
- Voltage Protection Rating (VPR): < 1800V
- Nominal Discharge Current (In): > 10 kA
- Max. Continuous Voltage (MCOV): Any value between 1.1 and 1.4 Ue, where Ue is the nominal voltage of the installation
- Short-circuit current rating (SCCR): 10 kA min

### Caution for Ungrounded Power Systems

In case of wiring configuration without Unground power, take in account that Ungrounded systems are inherently unstable and can produce excessively high line-to-ground voltages during fault conditions. During these fault conditions any electrical equipment, including an SPD, may be subjected to voltages which exceed their designated ratings.

## Operation

GIII+MV constantly supervises current and voltage values; when any harmful condition occurs, the output connection is deactivated until the fault disappears and power line conditions returns to an acceptable level. Specific timing such as Start Up Delay and Fault Detection Delay are incorporated to prevent nuisance tripping due to rapid power fluctuations.

GIII+MV provides LCD Display to indicate the output status (voltage, current, unbalance, frequency and load status). Also provides four (4) push buttons (On/Off, Up, Down and Select) for electrical parameter adjustment such as Voltage, Current, Frequency, Fault Detection Delay and others. Besides these mentioned advantages, a Communication Port with MODBUS RTU protocol is included in GIII+MV.

## Environmental Cautions

**CAUTION:** This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

**CAUTION:** An incorrectly applied or installed GIII+MV can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the GIII+MV.

**CAUTION:** Check that the voltage and current of chosen GIII+MV model corresponds to line voltage and motor current.
