---
title: "GIII Installation Manual - DIN Rail and Flat Surface Mounting"
type: Technical
source: "GD-MAN-052-01-V2-US-C.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GIII"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GIII Installation Manual

## General Description

GIII is an electronic Total motor Protection Relay that constantly supervises the Motor Current and the main electrical parameters such as Voltage, Frequency, Power factor, Real power, Reactive power and Energy consumption, giving the most reliable protection against Overload, Phase failure, Phase reversal, single phasing and Unbalanced conditions.

### Safety Warnings

**WARNING:** Only qualified technicians with knowledge about overload relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

**CAUTION:** This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

**CAUTION:** An incorrectly applied or installed GIII can result in damage to the components or reduction in product life.

**WARNING:** This product may start automatically, the user must take cautions to avoid hazards to people. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the GIII.

## GIII Parts and Pieces

### Assembly Parts (Back Side View)

1. Attachable Mounting Ears
2. Supporting Bracket
3. Back Groove (for DIN RAIL Mounting)
4. PT100 Temperature Sensor Terminal
5. Digital Input Terminal
6. Communication RS-485 Terminal
7. L1 L2 L3 Voltage Terminal
8. Control Relay Terminal
9. Auxiliary Relay Terminal
10. CT Input Terminal

### General and Control Parts

11. Detachable CT Box
12. CT Box Guide Rail
13. LCD Display
14. GIO PORT
15. START Push Button
16. ADJUST Push Buttons (UP & DOWN)
17. SELECT Push Button
18. Indicator Light (LED) for Control Relay (Control)
19. Indicator Light (LED) for Auxiliary Relay (Aux.)

**Note:** Parts Nr 1 shall be used only for Flat Surface Mounting option. Parts Nr 2 shall be used only for DIN RAIL Mounting option.

## GIII Detachable CT Box Mounting

### 3.1 Instructions for GIII - CT BOX Assembly

a) Move the supporting brackets 2mm outside and push downward GIII to CT BOX until back groove of relay can insert into CT BOX guide rail, using Alignment Mark as reference.

**CAUTION:** Each set of GIII and attachable CT box is calibrated and have the same Factory Number. Before assembling the CT box verify that its factory number is the same as GIII one. Failure to comply may result in a bigger measure error.

b) From Alignment Mark, move GIII relay towards the left sliding through rail guide until it does Click.

c) Insert both CT Input Terminals connecting GIII and CT Box.

### 3.2 Instructions for GIII - CT BOX Dismounting

a) Disconnect both CT Input Terminal used for GIII and CT Box connection and pull down both supporting brackets by means of screwdrivers.

b) Pull Out GIII upwards from CT Box.

## GIII DIN RAIL MOUNTING

**CAUTION:** GIII must be installed in an accessible position free from dust, dirt, dampness and vibration. Allow enough space for air circulation around the enclosure and easy access to all operator controls. Indoors use only.

### 4.1 Instructions for Mechanical Installation without CT BOX

a) Place GIII at inclined position and its back side must be placed toward the upper edge of the DIN Rail and then push down GIII relay until it does CLICK on the rail.

### 4.2 Instructions for Mechanical Installation with CT Box

Once you have assembled CT Box on GIII (See item 3.1) you shall follow these mounting instructions:

a) Place GIII at inclined position so that its back side (CT Box) must be placed toward the upper edge of the DIN Rail and then push down GIII relay until it does CLICK on the rail.

## GIII FLAT SURFACE MOUNTING

### 5.1 Instructions for Mechanical Installation without CT BOX

a) Take off the four (4) mounting ears at back side of GIII, insert and slip both mounting ears into the GIII back side grooves.

**Recommendation for Flat Surface Mounting:** Make four (4) holes (5/32") on panel surface before installing. See as reference the Guide for Flat Surface Mounting shown at item 6.1 (Dimensions GIII with Detachable CT Box).

b) Place GIII over flat surface panel and fix it handling a screwdriver suitable for screws 3/16" x 1/2".

### 5.2 Instructions for Mechanical Installation with CT BOX

Once you have assembled Detachable CT Box on GIII (Item 3.1):

a) Take off the four (4) mounting ears at back side of CT Box. Insert and slip both mounting ears into the CT Box back side grooves.

**Recommendation for Flat Surface Mounting:** Make four (4) holes (5/32") on panel surface before installing. See as reference the Guide for Flat Surface mounting as shown at Item 6.2 (Dimensions GIII without Detachable CT Box).

## GIII General Dimensions

- Height: 194.5 mm
- Width: 175 mm
- Depth: 106.8 mm

## GIII CONNECTION DIAGRAM

**WARNING:** Disconnect power supply before installing GIII. Failure to comply may result in death or serious injury.

**CAUTION:** Check that the voltage and current of chosen GIII model corresponds to line voltage and motor current.

### 7.1 Basic Diagram Installation

The installation includes:
- 3-phase 50/60 Hz power supply from line starter circuits
- Any Listed Circuit Breaker or fuse (User-supplied)
- PT100 Temperature Sensor connection
- Digital Input connection (Dry Contacts only)
- RS-485 Communication connection
- Auxiliary Relay
- Control Relay
- Motor wiring through GIII CT Box

Control Relay States:
- Normal: 8-10 OPEN, 6-8 CONNECTED
- Tripped: 8-10 CONNECTED, 6-8 OPEN

### 7.2 Terminal Designation

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
| A18 | RS485 S- (Negative Serial Comm) |
| A19 | RS485 S+ (Positive Serial Comm) |
| A20 | RS485 SG (Negative Signals for Serial Comm.) |

### Recommendation for Wiring

- Avoid over tightening M 2.5 screws upon terminals during wiring connection. Torque max: 4.5 Ib-in (5.18 kgf-cm).
- Wire Strip Length: 7-8 mm.
- Terminals wiring size: Between 12 AWG and 18 AWG.
- Maximum diameter of CT Box Holes wiring size: AWG 0 (18 mm).
- Use three CT holes for pass wiring to 3 phases motor. Using less than three wires may cause non-desired current unbalance.
- Connect L1L2L3 terminal for Voltage Input in parallel connection before line starter circuit through Contactor.

### Requirements for Surge Protective Device (user-supplied)

- UL Recognized SPDT Type 2
- Wiring configuration 3-phase (DELTA or WYE or arrangement of 3 x 1-Ph)
- AC Power Frequency: 50 or 60 Hz
- Voltage Protection Rating (VPR): < 1800V
- Nominal Discharge Current (In) ≥10kA
- Max. Continuous Voltage (MCOV): Any value between 1 and 1.4 Ue, where Ue is the nominal voltage of the installation
- Short-circuit current rating (SCCR): 10 kA min

**CAUTION:** In case of wiring configuration without Unground power, take in account that Ungrounded systems are inherently unstable and can produce excessively high line-to-ground voltages during fault conditions. During these fault conditions any electrical equipment, including an SPD, may be subjected to voltages which exceed their designated ratings. This information is being provided to the user so that an informed decision can be made before installing any electrical equipment on an ungrounded power system.

## GIII OPERATION

GIII constantly supervises current and voltage values; when any harmful condition occurs, the output connection is deactivated until the fault disappears and power line conditions returns to an acceptable level. Specific timing such as Start Up Delay and Fault Detection Delay are incorporated to prevent nuisance tripping due to rapid power fluctuations.

GIII provides LCD Display to indicate the output status (voltage, current, unbalance, frequency and load status). Also provides four (4) push buttons (On/Off, Up, Down and Select) for electrical parameter adjustment such as Voltage, Current, Frequency, Fault Detection Delay and others. Besides these mentioned advantages, a Communication Port with MODBUS RTU protocol is included in GIII.

## GIII+ Screen Adjustment

### Initial Screen States

1.1 Disconnected by MODBUS
1.2 Disconnected by off scheduling timer
1.3 Disconnected on MANUAL Mode
1.4 Disconnected by 3rd. Failure
1.5 Start Up Delay (TC)
1.6 TC Because of Undercurrent
1.7 Undervoltage (UV)
1.8 Overvoltage (OV)
1.9 Voltage Unbalance (VUB)
1.10 Frequency Shift (FS)
1.11 Single Phasing (VSP)
1.12 Phase Reversal (PR)
1.13 Accumulated Heat(%)
1.14 Overheating

### Main Screen Display Information

The main screen displays:
- Three-phase voltage readings (V)
- Motor current (A)
- Frequency (Hz)
- Starting time indicator
- Measured power parameters: kVA, kW, PF, kWH

### Adjustment Menu Access

Press both push buttons at the same time in order to get the Adjustment Menu (Screen 7). If access to screen is locked, you must enter the password required.

### Fault Screen Description

**Undervoltage / Overvoltage (Nr. 1.6 and Nr. 1.7):**
- Voltage values during fault conditions
- Phases involved in fault
- Voltage Unbalance (%)

**Voltage, Frequency and Heat (Nr 1.8 to 1.13):**
- Voltage values during fault conditions
- Voltage Unbalance (%)
- Maximum or Minimum value

### Fault History Screen Description

- Fault Type
- Fault Number
- Phase involved in fault
- Fault Value indication

### Fault Type Abbreviations

- OL = OVERLOAD
- UC = UNDERCURRENT
- CSP = CURRENT SINGLE PHASE
- CUB = CURRENT UNBALANCE
- FS = FREQUENCY SHIFT
- PR = PHASE REVERSAL
- VSP = VOLTAGE SINGLE PHASE
- LR = LOCKED ROTOR
- VUB = VOLTAGE UNBALANCE

### Additional Abbreviations

- OVERVOLT. = OVERVOLTAGE
- UNDERVOLT. = UNDERVOLTAGE
- UND.CURR = UNDERCURRENT
- AUX. = AUXILIARY RELAY
- ADJ. = ADJUST
- HRS = HOURS
- UV = UNDERVOLTAGE
- OV = OVERVOLTAGE
- V = VOLTAGE
- I = CURRENT
- PF = POWER FACTOR
- TD = TRIP DELAY
- TC = START UP DELAY
