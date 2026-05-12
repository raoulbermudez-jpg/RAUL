---
title: "GSPT General Description and Installation Manual"
type: Technical
source: "GD-MAN-053-01-V2-US-C.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GSPT"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GSPT General Description and Installation Manual

## GSPT General Description

GSPT is an electronic Submersible Pump Total Protection Relay that constantly supervises the Motor Current and the main electrical parameters such as Voltage, Frequency, Power factor, Real power, Reactive power and Energy consumption, giving the most reliable protection against Overload, Phase failure, Phase reversal, Single phasing, Unbalanced conditions, Overtemperature, excessive Starts per hour.

### WARNING
Only qualified technicians with knowledge about overload relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

This product may start automatically; the user must take cautions to avoid hazards to people.

### CAUTION
This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

An incorrectly applied or installed GSPT can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the GSPT.

## GSPT Parts and Pieces

### Backside View Assembly Parts

1. Lateral Supporting Grooves (for Flush Mounting)
2. Attachable Mounting Ears
3. Supporting Bracket
4. Back Groove (for DIN RAIL Mounting)
5. PTI00 Temperature Sensor Terminal
6. LI L2 L3 Voltage Terminal
7. Control Relay Terminal
8. Integrated CT, input terminal
9. Detachable CT Box
10. CT Box Guide Rail

### Frontside View - General and Control Parts

11. LCD Display
12. GIO PORT
13. START Push Button
14. ADJUST Push Buttons (UP & DOWN)
15. SELECT Push Button
16. Indicator Light (LED) for STATUS RELAY (ON: Connected; BLINK during tripping, or delaying to connect or output relay externally bypassed)
17. Indicator Light (LED) for FAILURE (ON: Abnormal condition in progress, like overload, phase failure, etc., or cooling of thermal protection)

**Note:** Parts Nr4 shall be used only for Flat Surface Mounting option. Parts Nr5 shall be used only for DIN RAIL Mounting option. Parts Nr1, 2, 3 shall be used only for Flush Mounting option.

## GSPT Detachable CT Box Mounting

### CAUTION
Each set of GSPT and attachable CT box is calibrated and have the same Factory Number. Before assembling the CT box verify that its factory number is the same as the GSPT one. Failure to comply may result in a bigger measure error.

### Instructions for GSPT - CT BOX Assembly

a) Move the supporting brackets 2mm outside and push downward GSPT to CT BOX until back groove of relay can insert into CT BOX guide rail, using Alignment Mark as reference.

b) From Alignment Mark, move GSPT relay towards the left sliding through rail guide until it does click.

c) Insert both CT Input Terminals connecting GSPT and CT Box.

### Instructions for GSPT - CT BOX Dismounting

a) Disconnect both CT Input Terminal used for GSPT and CT Box connection and pull down both supporting brackets by means of screwdrivers.

b) Move GSPT towards the right sliding through CT Box guide rail until it gets to alignment mark.

## GSPT DIN RAIL Mounting

### CAUTION
GSPT must be installed in an accessible position free from dust, dirt, dampness and vibration. Allow enough space for air circulation around the enclosure and easy access to all operator controls. Indoors use only.

### Instructions for Mechanical Installation without CT BOX

a) Place GSPT at inclined position and its back side must be placed toward the upper edge of the DIN Rail and then push down GSPT relay until it does CLICK on the rail.

### Instructions for Mechanical Installation with CT Box

Once you have assembled CT Box on GSPT (See section 3.1) you shall follow these mounting instructions:

a) Place GSPT at inclined position so that its back side (CT Box) must be placed toward the upper edge of the DIN Rail and then push down GSPT relay until it does CLICK on the rail.

## GSPT Flat Surface Mounting

### Instructions for Mechanical Installation without CT BOX

a) Take off the four (4) mounting ears at back side of GSPT, insert and slip both mounting ears into the GSPT back side grooves.

b) Place GSPT over flat surface panel and fix it handling a screwdriver suitable for screws 3/16" x 2".

**Recommendation for Flat Surface Mounting:** Make four (4) holes (5/32") on panel surface before installing.

### Instructions for Mechanical Installation with CT BOX

Once you have assembled Detachable CT Box on GSPT:

a) Take off the four (4) mounting ears at back side of CT Box. Insert and slip both mounting ears into the CT Box back side grooves.

b) Place GSPT with detachable CT Box over flat surface panel and fix it handling a screwdriver suitable for screws 3/16" x 2".

## GSPT Connection Diagram

### WARNING
Disconnect power supply before installing GSPT. Failure to comply may result in death or serious injury.

### CAUTION
Check that the voltage and current of chosen GSPT model corresponds to line voltage and motor current.

### Basic Diagram Installation

The GSPT connection diagram includes:
- Any Listed Circuit Breaker or fuse (User-supplied)
- 3-phase 50/60 Hz power supply
- PT100 temperature sensor connection
- Motor wiring through CT Box
- Control relay connections (SPDT)
- Contactor connections
- GIO Port for external communication
- Any Listed fuses 5A 600V to be added

Row B terminal connections: 1, 3, 5, 8, 10, 16/17, 18, 19/20

Circuit operation:
- Normal: 8-10 OPEN
- Connected: 6-8 CONNECTED

## GSPT General Dimensions

- Overall height: 218 mm
- Overall width: 175 mm
- Overall depth: 194.5 mm
- Guide for Flat Surface with CT Box: 152 mm × 100 mm
- Guide for Flat Surface without CT Box: 152 mm × 100 mm

## Terminal Designation

| Terminal | Description |
|----------|-------------|
| B1 | Voltage Input L1 (Phase R) |
| B3 | Voltage Input L2 (Phase S) |
| B5 | Voltage Input L3 (Phase T) |
| B6 | Control Relay (Closed when normally) |
| B8 | Control Relay (common) |
| B10 | Control Relay (Closed when Tripped) |
| B16 | CT-A Input |
| B17 | CT-B Input |
| B18 | CT-C Input |
| B19-B20 | CT-D (Common secondary) |
| A8-A9-A10 | PT100 (Terminal A-B-B Sensor) |

### Recommendations for Wiring

- Avoid over tightening M 2.5 screws upon terminals during wiring connection. Torque max: 4.5 Ib-in (5.18 kgf-cm).
- Wire Strip Length: 7-8 mm.
- Terminal wiring size: Between 12 AWG to 18 AWG.
- Maximum CT Hole wiring size: AWG 0 (18 mm).
- Use three CT holes for pass wiring to 3 phases motor. Using less than three wires may cause non-desired current unbalanced wrong detection.
- Connect LI L2 L3 terminal for Voltage Input in parallel connection before line starter circuit through Contactor.

## Requirements for Surge Protective Device (User-supplied)

- UL Recognized SPDT Type 2
- Wiring configuration 3-phase (DELTA or WYE or arrangement of 3 × 1-Ph)
- AC Power Frequency: 50 or 60 Hz
- Voltage Protection Rating (VPR): < 1800V
- Nominal Discharge Current (In): ≥10kA
- Max. Continuous Voltage (MCOV): Any value between 1.1 and 1.4 Ue, where Ue is the nominal voltage of the installation
- Short-circuit current rating (SCCR): 10 kA min

### CAUTION on Ungrounded Systems
In case of wiring configuration without Unground power, take in account that Ungrounded systems are inherently unstable and can produce excessively high line-to-ground voltages during fault conditions. During these fault conditions any electrical equipment, including an SPD, may be subjected to voltages which exceed their designated ratings.

## GSPT Operation

GSPT constantly supervises current and voltage values; when any harmful condition occurs, the output connection is deactivated until the fault disappears and power line conditions returns to an acceptable level. Specific timing such as Start Up Delay and Fault Detection Delay are incorporated to prevent nuisance tripping due to rapid power fluctuations.

GSPT provides LCD Display to indicate the output status (voltage, current, unbalance, frequency and load status). Also provides four (4) push buttons (On/Off, Up, Down and Select) for electrical parameter adjustment such as Voltage, Current, Frequency, Fault Detection Delay and others. A Communication Port with MODBUS RTU protocol is included in GSPT.

GSPT increases protection for Submersible Pumps by:
- Limiting the amount of allowed starting during continuous hour of operation, according to the capacity of the motor given in HP power
- Protecting continuously against events of Locked Rotor Accelerated
- Providing adjustable timing to connection, after Overload
- Automatically adapting the operational limits allowed of Over voltage and Under voltage according to nominal voltage of the lines

## GSPT Screen Adjustment and Quick Guide

### Initial Screen States

**1.1 Disconnected by MODBUS**
- Voltage display: 220, 220, 200 with 7%, 0.1
- Mode: OFF MODBUS

**1.2 Disconnected on MANUAL MODE**
- Voltage display: 220, 220, 200 with 7%
- Mode: OFF MANUAL
- Voltage readings: V12, V23, V31, VUB

**1.3 Disconnected by 3rd Failure**
- Voltage display: 220, 220, 200 with 7%, 6
- Current readings: 220, 220, 200 with 40, 40, 40, 20%, 3
- Mode: OFF 3rd FAILS

**1.4 Start up Delay (TC)**
- Voltage display: 220, 220, 200 with 7%
- START DELAY: 15"

**1.5 Because of undercurrent**
- Voltage display: 220, 220, 200 with 7%
- Power measurements: 110.0 kVA, 100.0 kW, 0.95 PF, 290000 kWh

**1.6 Time last fault**
- Voltage display: 220, 220, 200 with 7%
- MIN DELAY: 40", 175 s, 2000'

**1.7 Start hour**
- Voltage display: 220, 220, 200 with 7%
- SPH DELAY: 60"

**1.8 Undervoltage (UN)**
- Voltage display: 100, 220, 280, 73%, 31/07/03, 14:34
- UV: 100V, V12

**1.9 Overvoltage (OV)**
- Voltage display: 220, 220, 280 with 7%
- OV: 280V, V31

**1.10 Voltage Unbalance (VUB)**
- Voltage display: 220, 220, 200 with 10%
- CUB: 54

**1.11 Frequency Shift (FS)**
- Voltage display: 220, 220, 200 with 78%
- FS: 63.642

**1.12 Single Phasing (VSP)**
- Voltage display: 120, 100, 200 with 7%
- VSP L2

**1.13 Phase Reversal (PR)**
- Voltage display: 220, 220, 200 with 7%
- PHASE REVERSAL (0)

**1.14 Accumulated Heat (%)**
- Voltage display: 220, 220, 200 with 7%
- HEAT: 50.4%

**1.15 Overheating**
- Status display: OVERHEAT

**1.16 Maximum Temperature**
- Voltage display: 220, 220, 200 with 7%
- OT: 60°C

**1.17 Bypass Relay**

### Main Screen Menu Structure

**2. Measure kW-kVA-PF-kWH**
- Time: 13:50
- Date: 07/31/03
- Measurements displayed

**3. Faults Historical Register**
- Displays fault history with date, time, and fault type

**4. Motor hours counter**
- Total hours: 000025
- Date format: 31/07/03 14:34

**5. Motor Temperature**
- Frequency: 60.0 HZ
- START Mode: AUTO
- Temperature display: MT20°C

**6. Frequency and START Mode**
- Password protected access (0000)

**7. Adjustment Menu Screen**

**7.1 Adjustment Quick Guide**
The following parameters are adjustable:

- UNDERVOLT: 180V
- UNBALANCE: 103
- POWER FREO.: 6082
- FS: 10%
- SD: OFF
- MIN.: 107
- TRIP DELAY: 30"
- START DELAY: 600"
- NOMINAL I: 100A
- OVERLOAD: 203
- OVERLOAD: 10
- UND. CURR: NO (IN: 40%)
- FAILS: OFF
- TD: NO
- STARTS/h: YES
- SD: UND. CURR
- TEMP: 0000

**7.2 Main Screen Parameters**

**7.2.1 Undercurrent Settings**
- UND. CURR In: 40%
- UND. CURR: 600"
- UND. CURR: 107

**7.2.2 Voltage Adjustment and Start Mode**
- MAX STARTS/h: 15
- START MODE: AUTO/MANUAL
- CHANGE PASSWORD

**7.3 Current Adjust**
- VOLTAGE ADJUST
- CURRENT ADJUST
- START MODE switching between AUTO and MANUAL
- MODBUS ADDRESS

**7.5 Password Management**
- CHANGE PASSWORD
- VERIFY PASSWORD
- Password display: 0000

**7.6 Motor Hours and Modbus Address Display**

**7.8 Start Motor Confirmation**
- Prompt: START MOTOR? YES / NO

**7.9 Factory Settings Recovery**
- DELETING... progress display
- RECOVER FACTORY VALUES YES / NO

**7.9.1 Recovery in Progress**
- RECOVERING FACTORY VALUES display

### Push Button Configuration

- **START ADJUST:** Press Up & Down combination to activate adjust screen. If product is protected, introduce password.
- **EXIT:** Press Up & Down combination to exit from any screen
- **INIT SCREEN:** Press Up & Select combination to activate initial screen
- **TEST SCREEN:** Press Down while product shows initial screen
- **ADJUST PARAMETER:** Press Select to adjust any parameter
- **ACCEPT ADJUST:** Press Select to accept any adjustment

### Special Functions Keyboard

To activate adjust screen press Up & Down combination. If the product is protected, introduce password. In another case, it will go directly to adjustment's menu.

To exit from any screen press Up & Down.

To activate initial screen press Up & Select combination.

To activate the TEST screen press Down while the product shows the initial screen.

To adjust any parameter press Select.

To accept any adjust press Select.

## Fault Screen Description

### Voltage Values During Fault Conditions
- Display shows voltage values with fault phase indication
- Example: 167 169 168 with 0% and UV 167V V12

### Voltage Unbalance (%)
- Shows unbalance percentage during fault
- Example: 221, 11, 264 with 11% and UND.CURR indicator

### Fault Indication
- Phase involved in fault
- Unbalance percent (%)
- Fault Type notation (VUB for Voltage Unbalance, FS for Frequency Shift, VSP for Voltage Single Phasing, PHASE REVERSAL)
- Measured value indication

## Fault History Screen Description

- **Fault Type:** OL, UV, OV, FS, VSP, CSP, PR, LR, OT, BR, 3F, etc.
- **Fault Number:** Sequential numbering
- **Phase involved in fault:** Specific phase identification
- **Fault Value indication:** Voltage, current, temperature, or frequency reading during fault

## Glossary and Abbreviations

| Abbreviation | Definition |
|--------------|-----------|
| SPH | Starts Per Hour |
| 3F | Third Failure |
| BR | Bypass Relay |
| OT | Over Temp |
| TEF | Total Energy Fault |
| UC | Undercurrent |
| FS | Frequency Shift |
| LR | Locked Rotor |
| PF | Power Factor |
| OL | Overload |
| VSP | Voltage Single Phase |
| CSP | Current Single Phase |
| PR | Phase Reversal |
| UV | Under Voltage |
| OV | Over Voltage |
| CUB | Current Unbalanced |
| TEMP. | Temperature |
| VUB | Voltage Unbalanced |
| TD | Trip Delay |
| SD | Start Delay |
| MT | Motor Temperature |
