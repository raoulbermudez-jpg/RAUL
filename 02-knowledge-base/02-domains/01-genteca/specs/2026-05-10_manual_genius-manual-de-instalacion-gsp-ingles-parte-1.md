---
title: "GSPT Manual de Instalación - General Description and Installation Guide"
type: Technical
source: "MANUAL DE INSTALACION GSP-Ingles.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GSPT"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GSPT General Description

GSPT is an electronic Submersible Pump Total Protection Relay that constantly supervises the Motor Current and the main electrical parameters such as Voltage, Frequency, Power factor, Real power, Reactive power and Energy consumption, giving the most reliable protection against Overload, Phase failure, Phase reversal, Single phasing, Unbalanced conditions, Overtemperature, excessive Starts per hour.

## WARNING AND CAUTIONS

**WARNING:** Only qualified technicians with knowledge about overload relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

**WARNING:** This product may start automatically, the user must take cautions to avoid hazards to people.

**CAUTION:** This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

**CAUTION:** An incorrectly applied or installed GSPT can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the GSPT.

**CAUTION:** Each set of GSPT and detachable CT box is calibrated and have the same Factory Number. Before assembling the CT box verify that its factory number is the same as GSPT one. Failure to comply may result in a bigger measure error.

# GSPT Parts and Pieces

## Assembly Parts Description

**Parts Nr1, 2, 3:** Shall be used only for Flat Surface Mounting option.

**Parts Nr5:** Shall be used only for DIN RAIL Mounting option.

### Backside View Assembly Parts

1. Lateral Supporting Grooves (for Flush Mounting)
2. Attachable Mounting Ears
3. Supporting Bracket
4. Back Groove (for DIN RAIL Mounting)
5. PT100 Temperature Sensor Terminal
6. L1 L2 L3 Voltage Terminal
7. Control Relay Terminal
8. Integrated CT input terminal
9. Detachable CT Box
10. CT Box Guide Rail

### Frontside View - General and Control Parts

11. LCD Display
12. GIO PORT
13. START Push Button
14. ADJUST Push Buttons (UP & DOWN)
15. SELECT Push Button
16. Indicator Light (LED) for STATUS RELAY
    - ON: Connected
    - BLINK: during tripping, or delaying to connect or output relay externally bypassed
17. Indicator Light (LED) for FAILURE
    - ON: Abnormal condition in progress, like overload, phase failure, etc., or cooling of thermal protection

## GSPT Detachable CT Box Mounting

### Instructions for GSPT - CT BOX Assembly

a) Move the supporting brackets 2mm outside and push downward GSPT to CT BOX until back groove of relay can insert into CT BOX guide rail, using Alignment Mark as reference.

b) From Alignment Mark, move GSPT relay towards the left sliding through rail guide until it does Click.

c) Insert both CT Input Terminals connecting GSPT and CT Box.

### Instructions for GSPT - CT BOX Dismounting

a) Disconnect both CT Input Terminal used for GSPT and CT Box connection and pull down both supporting brackets by means of screwdrivers.

b) Move GSPT towards the right sliding through CT Box guide rail until it gets to alignment mark.

# GSPT Mechanical Installation

## DIN RAIL MOUNTING

**CAUTION:** GSPT must be installed in an accessible position free from dust, dirt, dampness and vibration. Allow enough space for air circulation around the enclosure and easy access to all operator controls. Indoors use only.

### Instructions for Mechanical Installation without CT BOX

a) Place GSPT at inclined position and its back side must be placed toward the upper edge of the DIN Rail and then push down GSPT relay until it does CLICK on the rail.

### Instructions for Mechanical Installation with CT Box

Once you have assembled CT Box on GSPT (See item 3.1) you shall follow these mounting instructions:

a) Place GSPT at inclined position so that its back side (CT Box) must be placed toward the upper edge of the DIN Rail and then push down GSPT relay until it does CLICK on the rail.

## FLAT SURFACE MOUNTING

### Instructions for Mechanical Installation without CT BOX

a) Take off the four (4) mounting ears at back side of GSPT, insert and slip both mounting ears into the GSPT back side grooves.

b) Place GSPT over flat surface panel and fix it handling a screwdriver suitable for screws 3/16" x 2".

**Recommendation for Flat Surface Mounting:** Make four (4) holes (5/32") on panel surface before installing.

### Instructions for Mechanical Installation with CT BOX

Once you have assembled Detachable CT Box on GSPT:

a) Take off the four (4) mounting ears at back side of CT Box. Insert and slip both mounting ears into the CT Box back side grooves.

b) Place GSPT with detachable CT Box over flat surface panel and fix it handling a screwdriver suitable for screws 3/16" x 2".

**Recommendation for Flat Surface Mounting:** Make four (4) holes (5/32") on panel surface before installing.

# GSPT General Dimensions

- **With CT Box:** 157.8 mm (width) × 175 mm (height) × 100 mm (depth), with mounting holes at 152 mm spacing
- **Without CT Box:** 100 mm (width) × 152 mm (height), with 5/32" mounting holes

# GSPT Connection Diagram

**WARNING:** Disconnect power supply before installing GSPT. Failure to comply may result in death or serious injury.

**CAUTION:** Check that the voltage and current of chosen GSPT model corresponds to line voltage and motor current.

## Basic Diagram Installation

The installation diagram shows:
- 3-phase 50/60 Hz power supply connection through Any Listed Circuit Breaker or fuse (User-supplied)
- Motor wiring passes through CT Box holes
- Control Relay connection with SPDT configuration
- GIO Port connection
- PT100 Temperature Sensor terminal
- Listed fuses (5A 600V) to be added by user
- Contactor and circuit breaker configuration for motor protection

**Relay States:**
- **Normal:** 8-10 OPEN, 6-8 CONNECTED
- **Tripped:** 8-10 CONNECTED, 6-8 OPEN

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

## Wiring Recommendations

- Avoid over tightening M 2.5 screws upon terminals during wiring connection. Torque max: 4.5 lb-in (5.18 kgf-cm).
- Wire Strip Length: 7-8 mm
- Terminal wiring size: Between 12 AWG to 18 AWG
- Maximum CT Hole wiring size: AWG 0 (18 mm)
- Use three CT holes for pass wiring to 3 phases motor. Using less than three wires may cause non-desired current unbalanced wrong detection.
- Connect L1L2L3 terminal for Voltage Input in parallel connection before line starter circuit through Contactor.

## Requirements for Surge Protective Device (user-supplied)

- UL Recognized SPDT Type 2
- Wiring configuration 3-phase (DELTA or WYE or arrangement of 3 x 1-Ph)
- AC Power Frequency: 50 or 60 Hz
- Voltage Protection Rating (VPR): < 1800V
- Nominal Discharge Current (In): ≥ 10 kA
- Max. Continuous Voltage (MCOV): Any value between 1.1 and 1.4 Ue, where Ue is the nominal voltage of the installation
- Short-circuit current rating (SCCR): 10 kA min

**CAUTION:** In case of wiring configuration without Unground power, take in account that Ungrounded systems are inherently unstable and can produce excessively high line-to-ground voltages during fault conditions. During these fault conditions any electrical equipment, including an SPD, may be subjected to voltages which exceed their designated ratings.

# GSPT Operation

GSPT constantly supervises current and voltage values; when any harmful condition occurs, the output connection is deactivated until the fault disappears and power line conditions returns to an acceptable level. Specific timing such as Start Up Delay and Fault Detection Delay are incorporated to prevent nuisance tripping due to rapid power fluctuations.

GSPT provides LCD Display to indicate the output status (voltage, current, unbalance, frequency and load status). Also provides four (4) push buttons (On/Off, Up, Down and Select) for electrical parameter adjustment such as Voltage, Current, Frequency, Fault Detection Delay and others. Besides these mentioned advantages, a Communication Port with MODBUS RTU protocol is included in GSPT.

## Key Protection Features

GSPT increases protection for Submersible Pumps by:
- Limiting the amount of allowed starting during continuous hour of operation, according to the capacity of the motor given in HP power
- Protecting continuously against events of Locked Rotor Accelerated
- Providing adjustable timing to connection, after Overload
- Automatically adapting the operational limits allowed of Over voltage and Under voltage according to nominal voltage of the lines

# GSPT Screen Adjustment - Quick Guide

## Default Parameter Values

- NOMINAL: 220V / 100A
- OVERVOLT: 280V
- UNDERVOLT: 180V
- UNBALANCE: 10%
- POWER FREQ.: 60 Hz
- Generación FS: 10%
- SD: OFF MIN. 10'
- TRIP DELAY: 30"
- START DELAY: 600"

## Screen Navigation

To Activate adjust screen: press Up & Down combination. If the product is protected, introduce password. Otherwise, it will go directly to adjustment's menu.

To exit from any screen: press Up & Down

To activate init screen: press Up & Select combination.

To activate the TEST screen: press Down while the product show the init screen.

To adjust any parameter: press Select.

To accept any adjust: press Select.

## Fault Screen Descriptions

### Voltage Fault Screens (Undervoltage/Overvoltage)

- **Fault Indication:** Voltage Values during fault conditions
- **Fault Number:** Phases involved in fault
- **Fault Type:** UV for Undervoltage or OV for Overvoltage
- **Value:** Maximum or Minimum value during fault

### Current Unbalance Fault Screens

- **Fault Indication:** Undercurrent (UND. CURR) percentage value
- **Fault Number:** Phases involved in fault
- **Fault Type:** UC for Undercurrent

### Voltage Unbalance Fault Screens

- **Fault Indication:** Voltage Unbalance (%) percentage value
- **Fault Type:** VUB for Voltage Unbalance

### Temperature, Frequency and Heat Fault Screens

- **Voltage Values during fault conditions**
- **Voltage Unbalance (%)** percentage value
- **Fault Type:** VSP for Voltage Single Phasing, PHASE REVERSAL for Phase Reversal
- **Measured Value:** Centigrade Degree

## Fault History Screen Description

| Element | Description |
|---------|-------------|
| Fault Type | OL (Overload), UV (Under Voltage), OV (Over Voltage), VSP (Voltage Single Phase), CSP (Current Single Phase), PR (Phase Reversal), VUB (Voltage Unbalanced), UC (Undercurrent), FS (Frequency Shift), LR (Locked Rotor), OT (Over Temp), BR (Bypass Relay), 3F (Third Failure), TEF (Total Energy Fault), SM (Start Motor) |
| Fault Number | Number indicating phases involved in fault |
| Fault Value indication | Voltage, Current or Temperature values during fault |
| Phase involved in fault | Phases affected by the fault condition |

## Abbreviations and Glossary

- **3F** - THIRD FAILURE
- **BR** - BYPASS RELAY
- **CSP** - CURRENT SINGLE PHASE
- **CUB** - CURRENT UNBALANCED
- **FS** - FREQUENCY SHIFT
- **LR** - LOCKED ROTOR
- **MT** - MOTOR TEMPERATURE
- **OL** - OVERLOAD
- **OT** - OVER TEMP
- **OV** - OVER VOLTAGE
- **OVERVOLT.** - OVERVOLTAGE
- **PF** - POWER FACTOR
- **PR** - PHASE REVERSAL
- **SD** - START DELAY
- **SM** - START MOTOR
- **TEMP.** - TEMPERATURE
- **TEF** - TOTAL ENERGY FAULT
- **TD** - TRIP DELAY
- **UC** - UNDERCURRENT
- **UND. CURR** - UNDERCURRENT
- **UNDERVOLT.** - UNDERVOLTAGE
- **UV** - UNDER VOLTAGE
- **VUB** - VOLTAGE UNBALANCED
- **VSP** - VOLTAGE SINGLE PHASE
