---
title: "GIII General Description and Installation Manual"
type: Technical
source: "GIII_GD-MAN-052-01-V2-US-C.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GIII"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GIII General Description and Installation Manual

## GIII General Description

GIII is an electronic Total motor Protection Relay that constantly supervises the Motor Current and the main electrical parameters such as Voltage, Frequency, Power factor, Real power, Reactive power and Energy consumption, giving the most reliable protection against Overload, Phase failure, Phase reversal, single phasing and Unbalanced conditions.

### Warnings and Cautions

**WARNING:** Only qualified technicians with knowledge about overload relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

**WARNING:** This product may start automatically, the user must take cautions to avoid hazards to people.

**CAUTION:** This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

**CAUTION:** An incorrectly applied or installed GIII can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the GIII.

## GIII Parts and Pieces

### Back Side View Assembly Parts

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

**CAUTION:** Each set of GIII and attachable CT box is calibrated and have the same Factory Number. Before assembling the CT box verify that its factory number is the same as GIII one. Failure to comply may result in a bigger measure error.

a) Move the supporting brackets 2mm outside and push downward GIII to CT BOX until back groove of relay can insert into CT BOX guide rail, using Alignment Mark as reference.

b) From Alignment Mark, move GIII relay towards the left sliding through rail guide until it does Click, as shown in following picture.

c) Insert both CT Input Terminals connecting GIII and CT Box.

### 3.2 Instructions for GIII - CT BOX Dismounting

a) Disconnect both CT Input Terminal used for GIII and CT Box connection and pull down both supporting brackets by means of screwdrivers.

b) Move GIII towards the right sliding through CT Box guide rail until it gets to alignment mark.

c) Pull Out GIII upwards from CT Box.

## GIII DIN RAIL MOUNTING

**CAUTION:** GIII must be installed in an accessible position free from dust, dirt, dampness and vibration. Allow enough space for air circulation around the enclosure and easy access to all operator controls. Indoors use only.

### 4.1 Instructions for Mechanical Installation without CT BOX

a) Place GIII at inclined position and its back side must be placed toward the upper edge of the DIN Rail and then push down GIII relay until it does CLICK on the rail as shown in figures.

### 4.2 Instructions for Mechanical Installation with CT Box

Once you have assembled CT Box on GIII (See item 3.1) you shall follow these mounting instructions:

a) Place GIII at inclined position so that its back side (CT Box) must be placed toward the upper edge of the DIN Rail and then push down GIII relay until it does CLICK on the rail.

b) Place GIII with detachable CT Box over flat surface panel and fix it handling a screwdriver suitable for screws 3/16" x 1/2".

## GIII FLAT SURFACE MOUNTING

### 5.1 Instructions for Mechanical Installation without CT BOX

a) Take off the four (4) mounting ears at back side of GIII, insert and slip both mounting ears into the GIII back side grooves.

b) Place GIII over flat surface panel and fix it handling a screwdriver suitable for screws 3/16" x 1/2".

**Recommendation for Flat Surface Mounting:** Make four (4) holes (5/32") on panel surface before installing. See as reference the Guide for Flat Surface Mounting shown at item 6.1 (Dimensions GIII with Detachable CT Box).

### 5.2 Instructions for Mechanical Installation with CT BOX

Once you have assembled Detachable CT Box on GIII (Item 3.1):

a) Take off the four (4) mounting ears at back side of CT Box. Insert and slip both mounting ears into the CT Box back side grooves.

**Recommendation for Flat Surface Mounting:** Make four (4) holes (5/32") on panel surface before installing. See as reference the Guide for Flat Surface mounting as shown at Item 6.2 (Dimensions GIII without Detachable CT Box).

## GIII General Dimensions

- Height: 194.5 mm
- Width: 106.8 mm
- Depth: 175 mm

### 6.1 Guide for Flat Surface with CT Box

Hole diameter: 5/32"
Mounting hole spacing: 152 mm

### 6.2 Guide for Flat Surface without CT Box

Hole diameter: 5/32"
Mounting hole spacing: 100 mm and 152 mm

## GIII Connection Diagram

### WARNING

Disconnect power supply before installing GIII. Failure to comply may result in death or serious injury.

### CAUTION

Check that the voltage and current of chosen GIII model corresponds to line voltage and motor current.

### 7.1 Basic Diagram Installation

The connection diagram shows:
- 3~ 50/60 Hz three-phase power input from line starter circuits
- Any Listed Circuit Breaker or fuse (User-supplied)
- Control Relay connections (SPDT configuration)
- Auxiliary Relay connections
- Motor wiring through GIII CT Box
- PT100 Temperature Sensor connection
- Digital Input (Dry Contacts only)
- RS-485 Communication connection
- Any Listed fuses 5A 600V to be added

**Control Relay States:**
- Tripped: 8-10 CONNECTED, 6-8 OPEN
- Normal: 8-10 OPEN, 6-8 CONNECTED

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

- Avoid over tightening M 2.5 screws upon terminals during wiring connection. Torque max: 4.5 lb-in (5.18 kgf-cm).
- Wire Strip Length: 7-8 mm.
- Terminals wiring size: Between 12 AWG and 18 AWG.
- Maximum diameter of CT Box Holes wiring size: AWG 0 (18 mm).
- Use three CT holes for pass wiring to 3 phases motor. Using less than three wires may cause non-desired current unbalance.
- Connect L1 L2 L3 terminal for Voltage Input in parallel connection before line starter circuit through Contactor (as shown in Diagram Connection).

### Requirements for Surge Protective Device (User-supplied)

- UL Recognized SPDT Type 2
- Wiring configuration 3-phase (DELTA or WYE or arrangement of 3 x 1-Ph)
- AC Power Frequency: 50 or 60 Hz
- Voltage Protection Rating (VPR): < 1800V
- Nominal Discharge Current (In) ≥ 10kA
- Max. Continuous Voltage (MCOV): Any value between 1 and 1.4 Ue, where Ue is the nominal voltage of the installation
- Short-circuit current rating (SCCR): 10 kA min

**CAUTION:** In case of wiring configuration without Unground power, take in account that Ungrounded systems are inherently unstable and can produce excessively high line-to-ground voltages during fault conditions. During these fault conditions any electrical equipment, including an SPD, may be subjected to voltages which exceed their designated ratings. This information is being provided to the user so that an informed decision can be made before installing any electrical equipment on an ungrounded power system.

## GIII Operation

GIII constantly supervises current and voltage values; when any harmful condition occurs, the output connection is deactivated until the fault disappears and power line conditions returns to an acceptable level. Specific timing such as Start Up Delay and Fault Detection Delay are incorporated to prevent nuisance tripping due to rapid power fluctuations.

GIII provides LCD Display to indicate the output status (voltage, current, unbalance, frequency and load status). Also provides four (4) push buttons (On/Off, Up, Down and Select) for electrical parameter adjustment such as Voltage, Current, Frequency, Fault Detection Delay and others. Besides these mentioned advantages, a Communication Port with MODBUS RTU protocol is included in GIII.

## GIII+ Screen Adjustment

### Screen States and Indications

**1.1 Disconnected by MODBUS**
- Displays: 220 220 200, 0L0 0000010010000, 0

**1.2 Disconnected by off scheduling timer**
- Displays: OFF SCHEDUL TIMER
- Shows voltage readings

**1.3 Disconnected on MANUAL Mode**
- Shows: OFF MANUAL
- Main Screen displays V12, V23, V31, VUB, Al (A)

**1.4 Disconnected by 3rd. Failure**
- Displays: OFF 3RD FAILS

**1.5 Start Up Delay (TC)**
- Shows: START DELAY and countdown

**1.6 TC Because of Undercurrent**
- Displays voltage, frequency, and UC DELAY settings

**1.7 Undervoltage (UV)**
- Shows: UV 100v V12 with voltage readings

**1.8 Overvoltage (OV)**
- Displays: OV 280v V31 with voltage readings

**1.9 Voltage Unbalance (VUB)**
- Shows: VUB 10% with voltage readings

**1.10 Frequency Shift (FS)**
- Displays: FS 63.6Hz with frequency information

**1.11 Single Phasing (VSP)**
- Shows: VSP Yes/No indication

**1.12 Phase Reversal (PR)**
- Displays: PHASE REVERSAL status

**1.13 Accumulated Heat (%)**
- Shows: HEAT percentage (e.g., 90.4%)

**1.14 Overheating**
- Displays: OVERHEAT status

### Screen Menu Structure

**Initial Screen (0):** Shows basic motor parameters
- Motor model (e.g., GIII+ 208V 180A)
- Software version

**Fault Screens (1):** Display fault type and details
- Fault type, phase involved, and numerical values
- Undervoltage/Overvoltage: Voltage values (V12, V23, V31)
- Frequency and Heat: Voltage readings and percentage

**Main Adjustment Menu (7):** Accessed by pressing both push buttons simultaneously
- VOLTAGE ADJUST
- CURRENT ADJUST
- CLOCK ADJUSTMENT
- SCHEDULE TIMER
- CHANGE PASSWORD
- MODBUS ADDRESS
- AUX. RELAY MODE
- TEMPERATURE ADJ.
- DELETE HISTORY
- START MODE
- Submenu options for detailed configuration

**7.1 UNDERVOLT**
- Setting: 180v UND. CURR TYPE mb
- UND. CURR: 600"

**7.2 NOMINAL I**
- TRIP CLASS UND. CURR In 40%
- UND. CURR TYPE
- UND. CURR PF
- 3 FAILS OFF

**7.2.1 OVERLOAD Configuration**
- NOMINAL I
- TRIP CLASS
- UND. CURR In threshold

**7.2.2 STARTING TIME**
- Configurable delay settings

**7.3 Measurements Display**
- kW-kVA-PF-kWH values
- Example: 110.0kVA, 100.0kw, 0.95PF, 290000kWH

**7.4 Password and Time Settings**
- PASSWORD TIME display (HH:MM format)
- DATE display (MM/DD/YY format)

**7.4.1 Schedule Timer Configuration**
- ON/OFF times
- SCHEDULE TIMER: YES/NO
- TASK settings
- HOLIDAY settings with dates (MM/DD)
- DAY and MONTH selectors

**7.4.2 Day and Holiday Schedule**
- Individual day selection (MTWTFSS)
- Holiday date entry

**7.5 Start Mode**
- AUTO/MANUAL selection

**7.6 Password Management**
- PASSWORD VERIFY screen
- WRONG PASSWORD notification

**7.6.1 Password Entry**
- Four-digit numeric entry (0000)

**7.7 Motor Temperature Display**
- MOTOR TEMP: 2000 (in selected units)

**7.8 MODBUS Configuration**
- MODBUS ADDRESS entry

**7.8.1 AUX RELAY MODE**
- Selection: WHILE FAILURE

**7.8.2 AUX RELAY MODE Selection**
- REMOTE MODBUS option
- TEMP. BIAS: YES
- TEMP. Ti: 55°C
- PTEMP Tn: 777777 (or 20°C threshold)

**7.9 Special Functions**
- TRIP RELAY
- REARME
- PUEDATE
- START

**7.10 Factory Recovery**
- DELETING... indication
- RECOVER FACTORY VALUES: YES/NO

**7.11.1 Factory Recovery Confirmation**
- RECOVERING FACTORY VALUES process

### Fault Screen Description

**Fault Type Abbreviations:**
- OL = OVERLOAD
- UC = UNDERCURRENT
- CSP = CURRENT SINGLE PHASE
- CUB = CURRENT UNBALANCE
- FS = FREQUENCY SHIFT
- PR = PHASE REVERSAL
- VSP = VOLTAGE SINGLE PHASE
- LR = LOCKED ROTOR
- VUB = VOLTAGE UNBALANCE
- UV = UNDERVOLTAGE
- OV = OVERVOLTAGE

**Fault History Screen Description:**
- Fault Type (e.g., UV for Undervoltage)
- Fault Number
- Phase involved in fault
- Fault Value indication
- Maximum or Minimum value during fault
- Voltage values during fault conditions
- Voltage Unbalance percentage
- Phases involved in fault

Example fault display:
- Fault Number: 18
- Fault Type: UV
- Fault Value: 200v
- Phase: V12

### Glossary and Abbreviations

**Abbreviations:**
- UND.CURR = UNDERCURRENT
- AUX. = AUXILIARY RELAY
- PTA = (Temperature parameter)
- TD = TRIP DELAY
- TC = START UP DELAY
- TRE = (Temperature-related)
- I0 = (Current parameter)
- V = VOLTAGE
- I = CURRENT
- PF = POWER FACTOR
- UNDERVOLT. = UNDERVOLTAGE

### Operating Instructions

**To Access Adjustment Menu:**
Press both push buttons at the same time in order to get the Adjustment Menu (Screen 7). If access to screen is locked, you must enter the password required.

**To Get Quick Exit Option:**
Press both push buttons at the same time in order to get Quick Exit option.

**To Enter Adjustment Values:**
Press SELECT to enter the chosen Adjusting Value.

**To Return to Initial Screen:**
Press both push buttons at the same time in order to get the Initial Screen (0).
