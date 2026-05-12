---
title: "GSPT General Description and Installation Manual"
type: Technical
source: "GD-MAN-054-01-V2-US-C.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GSPT"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GSPT General Description and Installation Manual

## GSPT GENERAL DESCRIPTION

GSPT is an electronic Submersible Pump Total Protection Relay that constantly supervises the Motor Current and the main electrical parameters such as Voltage, Frequency, Power factor, Real power, Reactive power and Energy consumption, giving the most reliable protection against Overload, Phase failure, Phase reversal, Single phasing, Unbalanced conditions, Overtemperature, excessive Starts per hour.

### WARNING

Only qualified technicians with knowledge about overload relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

This product may start automatically, the user must take cautions to avoid hazards to people.

### CAUTION

This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

An incorrectly applied or installed GSPT can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the GSPT.

## GSPT PARTS AND PIECES

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

### Frontside View General and Control Parts

11. LCD Display
12. GIO PORT
13. START Push Button
14. ADJUST Push Buttons (UP & DOWN)
15. SELECT Push Button
16. Indicator Light (LED) for STATUS RELAY (ON: Connected; BLINK during tripping, or delaying to connect or output relay externally bypassed)
17. Indicator Light (LED) for FAILURE (ON: Abnormal condition in progress, like overload, phase failure, etc., or cooling of thermal protection)

**Note:** Parts Nr4 shall be used only for Flat Surface Mounting option. Parts Nr5 shall be used only for DIN RAIL Mounting option. Parts Nr1,2,3 shall be used only for Flush Mounting option.

## GSPT DETACHABLE CT BOX MOUNTING

### CAUTION

Each set of GSPT and attachable CT box is calibrated and have the same Factory Number. Before assembling the CT box verify that its factory number is the same than GSPT one. Failure to comply may result in a bigger measure error.

### 3.1 Instructions for GSPT - CT BOX Assembly

a) Move the supporting brackets 2mm outside and push downward GSPT to CT BOX until back groove of relay can insert into CT BOX guide rail, using Alignment Mark as reference.

b) From Alignment Mark, move GSPT relay towards the left sliding through rail guide until it does Click.

c) Insert both CT Input Terminals connecting GSPT and CT Box.

### 3.2 Instructions for GSPT - CT BOX Dismounting

a) Disconnect both CT Input Terminal used for GSPT and CT Box connection and pull down both supporting brackets by means of screwdrivers.

b) Move GSPT towards the right sliding through CT Box guide rail until it gets to alignment mark.

## GSPT DIN RAIL MOUNTING

### CAUTION

GSPT must be installed in an accessible position free from dust, dirt, dampness and vibration. Allow enough space for air circulation around the enclosure and easy access to all operator controls. Indoors use only.

### 4.1 Instructions for Mechanical Installation without CT BOX

a) Place GSPT at inclined position and its back side must be placed toward the upper edge of the DIN Rail and then push down GSPT relay until it does CLICK on the rail.

### 4.2 Instructions for Mechanical Installation with CT Box

Once you have assembled CT Box on GSPT (See item 3.1) you shall follow these mounting instructions:

a) Place GSPT at inclined position so that its back side (CT Box) must be placed toward the upper edge of the DIN Rail and then push down GSPT relay until it does CLICK on the rail.

## GSPT FLAT SURFACE MOUNTING

### 5.1 Instructions for Mechanical Installation without CT BOX

a) Take off the four (4) mounting ears at back side of GSPT, insert and slip both mounting ears into the GSPT back side grooves.

b) Place GSPT over flat surface panel and fix it handling a screwdriver suitable for screws 3/16" x 2".

**Recommendation for Flat Surface Mounting:** Make four (4) holes (5/32") on panel surface before installing. See as reference The Guide for Flat Surface mounting as shown at Item 7.2 (Dimensions GSPT without Detachable CT Box).

### 5.2 Instructions for Mechanical Installation with CT BOX

Once you have assembled Detachable CT Box on GSPT (Item 3.1):

a) Take off the four (4) mounting ears at back side of CT Box. Insert and slip both mounting ears into the CT Box back side grooves.

b) Place GSPT with detachable CT Box over flat surface panel and fix it handling a screwdriver suitable for screws 3/16" x 2".

**Recommendation for Flat Surface Mounting:** Make four (4) holes (5/32") on panel surface before installing. See as reference the Guide for Flat Surface Mounting shown at item 7.1 (Dimensions GSPT with Detachable CT Box).

## GSPT GENERAL DIMENSIONS

- Height: 218 mm
- Width: 194.5 mm
- Depth: 175 mm
- Guide for Flat Surface with CT Box: 152 mm width x 100 mm height
- Guide for Flat Surface without CT Box: 152 mm width x 100 mm height (with 105/32" measurement noted)

## GSPT CONNECTION DIAGRAM

### WARNING

Disconnect power supply before installing GSPT. Failure to comply may result in death or serious injury.

### CAUTION

Check that the voltage and current of chosen GSPT model corresponds to line voltage and motor current.

### 7.1 Basic Diagram Installation

The connection diagram includes:
- Any Listed Circuit Breaker or fuse (User-supplied)
- 3-phase 50/60 Hz power supply (0.1 to 1.0A)
- PT100 temperature sensor connection
- Motor wiring through GIO Port with CT holes
- Control relay outputs with SPDT configuration
- Contactor and motor connections

## 7.2 Terminal Designation

| TERMINAL | DESCRIPTION |
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

### Recommendation for Wiring

- Avoid over tightening M 2.5 screws upon terminals during wiring connection. Torque max: 4.5 lb-in (5.18 kgf-cm)
- Wire Strip Length: 7-8 mm
- Terminal wiring size: Between 12 AWG to 18 AWG
- Maximum CT Hole wiring size: AWG 0 (18 mm)
- Use three CT holes for pass wiring to 3 phases motor. Using less than three wires may cause non-desired current unbalanced wrong detection
- Connect LI L2 L3 terminal for Voltage Input in parallel connection before line starter circuit through Contactor

## REQUIREMENTS FOR SURGE PROTECTIVE DEVICE (User-supplied)

- UL Recognized SPDT Type 2
- Wiring configuration 3-phase (DELTA or WYE or arrangement of 3 x 1-Ph)
- AC Power Frequency: 50 or 60 Hz
- Voltage Protection Rating (VPR): < 1800V
- Nominal Discharge Current (In) 210 kA
- Max. Continuous Voltage (MCOV): Any value between 1.1 and 1.4 Ue, where Ue is the nominal voltage of the installation
- Short-circuit current rating (SCCR): 10 kA min

### CAUTION

In case of wiring configuration without Unground power, take in account that Ungrounded systems are inherently unstable and can produce excessively high line-to-ground voltages during fault conditions. During these fault conditions any electrical equipment, including an SPD, may be subjected to voltages which exceed their designated ratings. This information is being provided to the user so that an informed decision can be made before installing any electrical equipment on an ungrounded power system.

## GSPT OPERATION

GSPT constantly supervises current and voltage values; when any harmful condition occurs, the output connection is deactivated until the fault disappears and power line conditions returns to an acceptable level. Specific timing such as Start Up Delay and Fault Detection Delay are incorporated to prevent nuisance tripping due to rapid power fluctuations.

GSPT provides LCD Display to indicate the output status (voltage, current, unbalance, frequency and load status). Also provides four (4) push buttons (On/Off, Up, Down and Select) for electrical parameter adjustment such as Voltage, Current, Frequency, Fault Detection Delay and others. Besides these mentioned advantages, a Communication Port with MODBUS RTU protocol is included in GSPT.

GSPT increases protection for Submersible Pumps: It limits the amount of allowed starting during continuous hour of operation, according to the capacity of the motor given in HP power. It protects continuously against events of Locked Rotor Accelerated. It provides adjustable timing to connection, after Overload. It automatically adapts the operational limits allowed of Over voltage and Under voltage according to nominal voltage of the lines.

## GSPT SCREEN ADJUSTMENT

### Adjustment Quick Guide

#### Initial Screen States

**1.1 Disconnected by MODBUS**
- Display: 220 220 200 7% 0.1
- Status: OFF MODBUS
- Nominal Voltage: 220V
- Version: v1.10 EN

**1.2 Disconnected on MANUAL MODE**
- Display: 220 220 200 7%
- Status: OFF MANUAL
- Voltage readings: V12 V23 V31 VUB

**1.3 Disconnected by 3rd. Failure**
- Display: 220 220 200 7%
- Secondary Display: 220 220 200 7%
- Reading: 40 40 40 20%
- Status: OFF 3rd FAILS

**1.4 Start up Delay (TC)**
- Display: 220 220 200 7%
- START DELAY: 15"

**1.5 Measure kW-kVA-PF-kWH**
- Display: 220 220 200 7%
- Power Factor: 0.95 PF
- Reactive Power: 110.0 kVA, 100.0 KW
- Energy: 290000 kwh

**1.6 Trip test sar oy cusRENT_ADSUST**
- Display: 220 220 200 7%
- UC DELAY: 100°

**1.7 Min Delay**
- Display: 220 220 200 7%
- MIN DELAY: 40"
- Duration: 1750' 2000'

**1.8 Start hour (sph)**
- Display: 220 220 200 7%
- sph DELAY: 60"

**1.9 Undervoltage (UN)**
- Display: 100 220 280 73%
- UV: 100v V12

**1.10 Overvoltage (OV)**
- Display: 220 220 280 7%
- OV: 280V V31

**1.11 Voltage Unbalance (VUB)**
- Display: 220 220 200 10%
- CUB: 54
- Tolerance: MT20%c

**1.12 Frequency Shift (FS)**
- Display: 220 220 200 78%
- FS: 63.642

**1.13 Single Phasing (VSP)**
- Display: 120 100 200 7%
- VSP L2

**1.14 Phase Reversal (PR)**
- Display: 220 220 200 7%
- PHASE REVERSAL: (0)

**1.15 Accumulated Heat (%)**
- Display: 220 220 200 7%
- HEAT: 50.4%

**1.16 Overheating**
- Display: 220 220 200 7%
- Status: OVERHEAT

**1.17 Maximum Temperature**
- Display: 220 220 200 7%
- OT: 60°C

**1.18 Bypass Relay**
- Display: 220 220 200 7%
- Status: BYPASS RELAY

#### Menu Functions (7.2 - 7.9)

**7.2 Main Screen - Parameter Adjustment**
- UNDERVOLT: 180v
- UNBALANCE: 103
- POWER FREO: 6082
- FS: 10%
- SD OFF: MIN. 107
- TRIP DELAY: 30"
- START DELAY: 600"
- NOMINAL I: 100A
- OVERLOAD: 203
- OVERLOAD: 10
- UND. CURR: NO (with value 32)
- UND. CURR In: 40%
- FAILS OFF: NO
- TD: UND. CURR: 600"
- PASSWORD: UND. CURR: 107
- TEMP: 0000
- EXIT: EXIT

**7.2.1 - Undercurrent Settings**
- UND. CURR In: 40%
- UND. CURR: 600" (time delay)
- UND. CURR: 107

**7.2.2 - Maximum Starts Per Hour**
- MAX STARTS/h: 15

**7.3 - Voltage Adjust**
- VOLTAGE ADJUST

**7.4 - Current Adjustment**
- START MODE: CHANGE PASSWORD

**7.5 - Temperature Adjustment**
- TEMPERATURE ADJ.
- DELETE HISTORY

**7.5.1 - Password Verification**
- VERIFY PASSWORD: (entry field)
- RESTART PASSWORD: EXIT

**7.6 - Motor Hours Counter**
- TOTAL HRS: 000025
- Date: 31/07/03 14:34
- Motor hours counter value

**7.7 - Motor Temperature Reading**
- FREQUENCY and START Mode: 60.0 HZ AUTO
- MOTOR TEMP: 22°C
- TEMP. BIAS: YES
- TEMP. Ti: 55°C
- TEMP. Tm: 120°C
- PASSWORD: EXIT

**7.8 - Start Motor Confirmation**
- START MOTOR?: YES / NO

**7.9 - Delete History / Factory Recovery**
- DELETING... (process indicator)

**7.9.1 - Recover Factory Values**
- RECOVERING FACTORY VALUES: YES / NO

### Special Functions Keyboard

To Activate adjust screen press Up & Down combination. If the product is protected, introduce password. In another case, it will go directly to adjustment's menu.

To exit from any screen press Up & Down.

To activate init screen press Up & Select combination.

To activate the TEST screen press Down while the product show the init screen.

To adjust any parameter press Select.

To accept any adjust press Select.

### Fault Screen Description

**Fault Type Indicators:**
- Undervoltage / Overvoltage (Nr. 1.6 and Nr. 1.7): Voltage Values during fault conditions
- Voltage Unbalance (%): Unbalance percentage during fault
- Voltage, Frequency and Heat (Nr. 1.8 to 1.13): Voltage values during fault conditions

**Fault Number:** Phases involved in fault

**Fault Type:**
- OL - OVERLOAD
- UV - UNDER VOLTAGE
- OV - OVER VOLTAGE
- VUB - VOLTAGE UNBALANCED
- FS - FREQUENCY SHIFT
- VSP - VOLTAGE SINGLE PHASE
- CSP - CURRENT SINGLE PHASE
- PR - PHASE REVERSAL
- UC - UNDERCURRENT
- LR - LOCKED ROTOR
- 3F - THIRD FAILURE
- BR - BYPASS RELAY
- OT - OVER TEMP
- SM - START MOTOR
- TEF - TOTAL ENERGY FAULT

### Fault History Screen Description

**Fault Numb:** Fault Number

**Phases involved in Fault**

**Fault Type and Value indication**

### Glossary and Abbreviations

- SPHA - STARTS PER HOUR
- 3F - THIRD FAILURE
- BR - BYPASS RELAY
- OT - OVER TEMP
- TEF - TOTAL ENERGY FAULT
- FS - FREQUENCY SHIFT
- LR - LOCKED ROTOR
- PF - POWER FACTOR
- UC - UNDERCURRENT
- OL - OVERLOAD
- OV - OVER VOLTAGE
- VSP - VOLTAGE SINGLE PHASE
- CSP - CURRENT SINGLE PHASE
- PR - PHASE REVERSAL
- UV - UNDER VOLTAGE
- CUB - CURRENT UNBALANCED
- TEMP - TEMPERATURE
- VUB - VOLTAGE UNBALANCED
- OVERVOLT - OVERVOLTAGE
- UNDERVOLT - UNDERVOLTAGE
- UND. CURR - UNDERCURRENT
- TD - TRIP DELAY
- SD - START DELAY
- MT - MOTOR TEMPERATURE
