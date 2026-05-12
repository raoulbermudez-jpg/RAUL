---
title: "Manual de Instalación GIII - Guía Técnica de Pantalla y Ajustes"
type: Technical
source: "MANUAL DE INSTALACION GIII Ingles pag. 4-7.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GIII, GIII+"
version_status: "vigente"
date_processed: "2026-05-10"
---

# Manual de Instalación GIII - Guía Técnica de Pantalla y Ajustes

## 6.1 Terminal Designation

| TERMINAL | DESCRIPCION |
|----------|-------------|
| B1 | Voltage Input L1 (Phase R) |
| B2 | Voltage Input L2 (Phase S) |
| B3 | Voltage Input L3 (Phase T) |
| B6 | Control Relay |
| B8 | Control Relay |
| B10 | Control Relay |
| B11 | Auxiliary Relay |
| B13 | Auxiliary Relay |
| B15 | Auxiliary Relay |
| B16 | CT-A Input |
| B17 | CT-B Input |
| B18 | CT-C Input |
| B19-B20 | CT-D (Common secondary) |
| A8-A9-A10 | PT 100 (Terminal A-B-B Sensor) |
| A11-A12 | Digital Input 1 (Dry Contacts only) |
| A14-A15 | Digital Input 2 (Dry Contacts only) |
| A16 | RS485 S- (Negative Serial Comm.) |
| A17 | RS485 S+ (Positive Serial Comm.) |
| A20 | RS485 SG (Negative Signals for Serial Comm.) |

## 7.1 Guide for Flat Surface without CT Box

Installation dimension: 152mm height, 5/32" terminals.

### Connection Diagram

WARNING: Disconnect power supply before installing GIII. Electrical shock will result in death or serious injury.

CAUTION: Check that the voltage and current of chosen GIII model correspond to line voltage and motor current.

## 8.1 Basic Diagram Installation

**Voltage Supply:** L1-L2-L3, 3-phase, 50/60 Hz (From line starter)

**Temperature Option:** PT100

**CT Box Configuration:** Rows A, B (sensors), G (common), D1, D2, FG, S-, S+, SG

### Recommendation for Wiring

- Avoid over tightening M 2.5 screws upon terminals during wiring connection.
- Torque max: 4.5 lb-in (5.18 kgf-cm).
- Wire Strip Length: 7-8 mm.
- Terminals wiring size: 30 AWG (1.5 mm²) up to 12 AWG.
- CT Box Holes wiring size: >0 AWG (18 mm).
- Use three CT holes for pass wiring to 3 phases motor. Using less than three wires may cause non-desired current unbalance.
- Connect L1-L2-L3 terminal for Voltage Input in parallel connection before line starter circuit through Contactor.

## GIII Operation

GI constantly supervises current and voltage values; when any harmful condition occurs, the output connection is deactivated until the fault disappears and power line conditions returns to an acceptable level. Specific timing such as Start Up Delay and Fault Detection Delay are incorporated to prevent nuisance tripping due to rapid power fluctuations.

GIII provides LCD Display to indicate the output status (voltage, current, unbalance, frequency and load status). Also provides four (4) push buttons (On/Off, Up, Down and Select) for electrical parameter adjustment such as Voltage, Current, Frequency, Fault Detection Delay and others. Besides these mentioned advantages, a Communication Port with MODBUS RTU protocol is included in GIII.

## 10.1 GIII Screen Adjustment - Quick Guide

### Screen 0 - Initial Screen
- OFF MODBUS GIII v2.00
- Displays voltage readings and operational status

### Screen 1 - Fault Screens

**1.1 Disconnected by MODBUS**
- OFF MODBUS

**1.2 Disconnected on MANUAL Mode**
- OFF MANUAL

**1.3 Disconnected by 3rd. Failure**
- OFF 3RD FAILS

**1.4 Start Up Delay (TC)**
- TC 100°
- TC UND.CURR 10"

**1.5 Undervoltage (UV)**
- UV 167V
- UV 100V

**1.6 Overvoltage (OV)**
- OV 241V

**1.7 Voltage Unbalance (VUB)**
- VUB 11%

**1.8 Frequency Shift (FS)**
- FS 63.6 Hz

**1.9 Single Phasing (VSP)**
- VSP L2

**1.10 Phase Reversal (PR)**
- PHASE REVERSAL

**1.11 Accumulated Heat (%)**
- HEAT 50.4%

**1.12 Overheating (Aft)**
- OVERHEAT

### Screen 2 - Motor Hours Counter
- TOTAL HRS 000025
- Date and time display

### Screen 3 - Fault History
- Displays up to 3 historical faults with date and time

### Screen 7 - Main Adjustment Menu

#### 7.1 Voltage Adjust
#### 7.2 Current Adjust
- NOMINAL I: 100A
- TRIP CLASS: oo 5
- ACCEL. ER: YES
- OVERLOAD: 20%
- UND.CURR TYPE: In
- UND.CURR In: 40%
- UND.CURR FP: 0.5
- HIGH INERTIA: YES
- TC UND.CURR: 10" 20"
- TD UND.CURR: 600"
- 3 FAILS: OFF NO

#### 7.3 Start Mode
- AUTO / MANUAL

#### 7.4 Password Verification
- Enter password: 0000

#### 7.5 Modbus Address

#### 7.6 Auxiliary Relay Mode

#### 7.7.1 Modbus Address Configuration

#### 7.8 Push Button Configuration
- START ADJUST
- SELECT

#### 7.8.1 While Failure
- AUX. RELAY MODE: TRIP RELAY

#### 7.8.2 Auxiliary Relay Mode

#### 7.9 Remote Modbus
- TEMP. BIAS: YES
- TEMP. Ti: 55°C
- TEMP. Tm: 120°C

#### 7.10 Deleting Screen

### Fault Screen Description

**Undervoltage / Overvoltage (Screens 1.5 and 1.6):**
- Voltage Values during fault conditions
- Phases involved in Fault
- Maximum or Minimum value during fault
- Fault Type: UV for Undervoltage, OV for Overvoltage

**Voltage, Frequency and Heat (Screens 1.7 to 1.11):**
- Voltage Values during fault conditions
- Voltage Unbalance (%)
- Phases involved in fault
- Unbalance Percent (%)
- Centigrade Degree
- Measured Value
- Fault Type: VUB for Voltage Unbalance, FS for Frequency Shift, VSP for Voltage Single Phasing, PHASE REVERSAL

### Fault History Screen Description (nr. 2)

- Fault Date
- Fault Number
- Fault Starting Time
- Duration Time of Fault (minutes)
- Fault Type
- Fault Value indication
- Phase Involved in Fault

## 10.2 GIII+ Adjustment Quick Guide

### Screen 0.1 - Initial Screen with Parameters
- UNDERVOLT.: 140V
- ER: 242
- UNBALANCE: 10%
- POWER FREQ.: 60Hz
- FS: 10%
- TRIP DELAY: 30"
- START DELAY: 600"

### Screen 1 - Fault Screens (GIII+)

**1.1 Disconnected by MODBUS**
- OFF MODBUS GIII+ v2.00

**1.2 Disconnected by Sched. Timer**
- OFF SCHEDL. TIMER

**1.3 Disconnected on Manual Mode**
- OFF MANUAL

**1.4 Disconnected by 3rd. Failure**
- OFF 3RD FAILS

**1.5 Start Up Delay (TC)**
- TC 100°

**1.6 Undervoltage (UV)**
- UV 100V

**1.7 Overvoltage (OV)**
- OV 241V

**1.8 Voltage Unbalance (VUB)**
- VUB 11%

**1.9 Frequency Shift (FS)**
- FS 63.6 Hz

**1.10 Single Phasing (VSP)**
- VSP L2

**1.11 Phase Reversal (PR)**
- PHASE REVERSAL

**1.12 Accumulated Heat (%)**
- HEAT 50.4%

**1.127 Overheating (Aft)**
- OVERHEAT

### Screen 7 - Main Adjustment Menu (GIII+)

#### 7.4 Schedule Timer Adjustment
- VOLTAGE ADJUST
- CURRENT ADJUST
- CLOCK ADJUST
- SCHEDULE TIMER
- START MODE
- CHANGE PASSWORD
- MODBUS ADDRESS
- AUX. RELAY MODE
- TEMPERATURE ADJ.
- DELETE HISTORY

#### 7.4.1 Event Adjust
- SCHEDULE TIMER: EVENT ADJUST
- HOLIDAY ADJUST
- EXIT

#### 7.4.2 Holiday Adjust
- HOLIDAY: 01/20
- DAY: 1
- MONTH: 1

#### 7.6 Start Mode
- AUTO / MANUAL

#### 7.8.1 Start Adjust Select

#### 7.8.2 Auxiliary Relay Mode - Trip Relay

#### 7.9 Remote Modbus
- TEMP. BIAS: YES
- TEMP. Ti: 55°C
- TEMP. Tm: 120°C

#### 7.10 Deleting Screen

## 10.3 GIII+ Schedule Timer Adjustment Guide

Only GIII+ models include "CLOCK ADJUST" and "SCHEDULE TIMER" options.

### Event Adjust Example

**EVENT 01:** From Tuesday to Saturday and Holiday
- ON: 7:30 hrs
- OFF: 16:45 hrs

Configuration steps:
1. Press SELECT for change to next day
2. Select desired days: T (Tuesday), W (Wednesday), T (Thursday), F (Friday), S (Saturday), S (Sunday), H (Holiday)
3. Press SELECT to enter time ON
4. Press (A) or (Y) until find Hour desired
5. Press SELECT to enter Hour desired
6. Press (A) or (Y) until find Minutes desired
7. Press SELECT to enter Minutes desired
8. Press (A) or (Y) until find Hour desired for OFF time
9. Press SELECT to enter Hour desired
10. Press (A) or (Y) until find Minutes desired for OFF time
11. Press SELECT to enter Minutes desired
12. Press (A) or (Y) until find Event Nr
13. Press SELECT to enter Event Nr

### Holiday Adjust Example

**HOLIDAY 01:** June 24th
- HOLIDAY: 01/20
- DAY: 24
- MONTH: 6

Configuration steps:
1. Press SELECT on HOLIDAY ADJUST
2. Press (A) or (Y) until find month desired
3. Press SELECT to enter month
4. Press (A) or (Y) until find day desired
5. Press SELECT to enter day

**Note:** If you require to adjust a new EVENT or HOLIDAY, press (A) to look for the number to assign and then press to enter it. It will take you to screen 7.4.1 (for Events) or 7.4.2 (for Holiday). If you want to exit, press (MD) and you will go to screen 7.4.

## Glossary of Abbreviations

| ABBREVIATION | MEANING |
|---------------|---------|
| OL | OVERLOAD |
| UC | UNDERCURRENT |
| CSP | CURRENT SINGLE PHASING |
| CUB | CURRENT UNBALANCE |
| FS | FREQUENCY SHIFT |
| PR | PHASE REVERSAL |
| VSP | VOLTAGE SINGLE PHASING |
| LR | LOCKED ROTOR |
| VUB | VOLTAGE UNBALANCE |
| UV | UNDERVOLTAGE |
| OV | OVERVOLTAGE |
| V | VOLTAGE |
| I | CURRENT |
| PF | POWER FACTOR |
| TD | TRIP DELAY |
| TC | START UP DELAY |
| SCHEDL. | SCHEDULE |
| TEMP. | TEMPERATURE |
| OVERVOLT. | OVERVOLTAGE |
| UNDERVOLT. | UNDERVOLTAGE |
| UND.CURR | UNDERCURRENT |
| AUX. | AUXILIARY RELAY |
| ADJ. | ADJUST |
| HRS | HOURS |
| ST. AE | START ACCELERATION |
