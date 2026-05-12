---
title: "GIII+MV Manual de Instalación - Guía Rápida de Ajuste y Desmontaje"
type: Technical
source: "GD-MAN-8003-01-V1-US-C.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GIII+MV"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GIII+MV Adjustment Quick Guide and Dismounting Instructions

## Software Version 3.02

### 1. State Relay Screens - Failure Screens

#### 1.1 Disconnected by MODBUS
- Voltage: 220 218 222 V
- Status: OFF MODBUS
- Load: 1%

#### 1.2 Disconnected on SCHEDL Timer
- Voltage: 220 218 222 V
- Status: OFF SCHEDL TIMER
- Load: 1%

#### 1.3 Disconnected on Manual Mode
- Voltage: 220 218 222 V
- Status: OFF MANUAL
- Load: 1%

#### 1.4 Disconnected 3rd_Failure
- Voltage: 220 218 222 V
- Status: OFF 3RD FAILS
- Load: 1%

#### 1.5 Startup Delay (SD)
- Voltage: 220 220 200 V
- Status: START DELAY 15"
- Load: 7%

#### 1.6 Because Of Under Current
- Voltage: 220 220 200 V
- Status: MIN DELAY
- Time: 40"
- Load: 7%

#### 1.7 Time Between Starts
- Voltage: 220 220 200 V
- Load: 7%

#### 1.8 Starts Hour
- Voltage: 220 220 200 V
- Status: SPH DELAY 10"
- Load: 7%

#### 1.9 Under Voltage (UV)
- Voltage: 100 220 200 V
- Status: UV 100V V12
- Load: 7%

#### 1.10 Over Voltage (OV)
- Nominal: 220 V
- Over Voltage: 280 V
- Status: OV 280V V31
- Load: 7%

#### 1.11 Voltage Unbalance (VUB)
- Voltage: 221 267 264 V
- Status: VUB 11%
- Load: 11%

#### 1.12 Frequency Shift (FS)
- Voltage: 220 218 222 V
- Status: FS 63.6 Hz
- Load: 0%

#### 1.13 Single Phasing (VSP)
- Voltage: 107 105 214 V
- Phase: L2
- Status: VSP
- Load: 50%

#### 1.14 Phase Reversal (PR)
- Voltage: 220 222 218 V
- Status: PHASE REVERSAL
- Load: 0%

#### 1.15 Accumulated Heat (%)
- Voltage: 220 218 222 V
- Status: HEAT 50.4%
- Load: 0%

#### 1.16 Overheating
- Voltage: 220 218 222 V
- Status: OVERHEAD
- Load: 0%

#### 1.17 Maximum Temperature
- Temperature: 60°C

#### 1.18 Bypass Relay
- Voltage: 220 220 200 V
- Load: 7%

### 2. Main Screen Information

#### Initial Screen (Screen 0)
- Voltages: V12, V23, V31
- Reading: 220 220 200 V
- VUB: 7%
- Load: 30
- Offset: 0%

#### Measurements (Screen 2)
- Power: 110.0 kVA
- Active Power: 100.0 kW
- Power Factor: 0.95 PF
- Energy: 290000 kWH

#### Faults Historical Register (Screen 3)
- Date: 19 17/05 20:50
- Event: 2000" UV 100V V12

#### Motor Hours Counter (Screen 4)
- Date/Time: 31/07/03 14:34
- Total Hours: 000025

#### Motor Temperature, Frequency and START Mode (Screen 5)
- Frequency: 60.0 Hz
- Start Mode: AUTO
- Motor Temperature: 20°C

### 3. Configuration Menu

#### Push Button Operations

**Adjustment Select:** Press both push buttons simultaneously to access the Adjustment Menu (Screen 7). If access is locked, enter the required password.

**Quick Exit:** Press both push buttons simultaneously to return to the Quick Exit option.

**Special Functions:**
- BYPASS RELAY available with configurations shown

### 4. Adjustment Value Selection

- Press SELECT to enter the chosen adjustment
- Press both push buttons simultaneously to return to the Initial Screen

### 5. Settings Main Menu (Screen 7)

- VOLTAGE ADJUST
- CURRENT ADJUST
- Clock ADJUST
- SCHEDULE TIMER
- START MODE
- CHANGE PASSWORD
- COMP. PORT
- AUX. RELAY MODE
- TEMP BIAS
- DELETE HISTORY
- RESTART

### 6. Nominal Multivoltage Settings (Screen 7.1)

**Available Voltage Options:** 200, 208, 220, 230, 240, 400, 420, 440, 460, 480 V~

**Power Frequency:** 60 Hz

**Trip Delay:** 30"

**Start Delay:** 600"

**Overvoltage Setting:** 242 V

**Unbalance Setting:** 10%

### 7. Current Adjust Settings (Screen 7.2)

#### CT Settings (for external CT models)
- **CT Ratio:** 400/5
- **Nominal Current:** 100 A
- **Trip Class:** 16
- **Overload:** 20%
- **SD Overload:** 10"

#### Under Current Settings (Screen 7.2.1)
- **Undercurrent Type:** IN
- **Undercurrent Delay:** 30"
- **Undercurrent Value:** 10%
- **Undercurrent Time:** 40"

#### Under Current Power Factor (Screen 7.2.1.2)
- **Power Factor:** 0.5

#### Motor Starting Parameters (Screen 7.2.2)
- **SD OFF:** MIN SB
- **Wrong Inertia:** YES
- **Acceleration:** YES
- **Starting Time:** ≥ 20"

#### Maximum Starts per Hour (Screen 7.2.3)
- **SPH:** 15 starts/hour

### 8. Schedule Timer Settings (Screen 7.4)

**Weekly Schedule:** MTWTFSSH

**Time Format:** ON 00:00 / OFF 00:00

**Event Adjustment:** 01/60

**Holiday Adjustment:** YES

**Exit:** Available

#### EVENT 01 Example
- **Days:** Tuesday to Saturday and Holiday
- **ON Time:** 7:30 hrs
- **OFF Time:** 16:45 hrs
- **Configuration:** NNN NNO

#### HOLIDAY 01 Example
- **Date:** June 24th
- **Configuration:** YN NN YN

### 9. Start Mode Settings (Screen 7.6.1)

- **AUTO**
- **MANUAL**
- **VERIFY PASSWORD:** 0000

### 10. MODBUS Settings (Screen 7.7)

#### MODBUS Address (Screen 7.7.1)
- **Default Address:** 001

#### Baud Rate (Screen 7.7.2)
- **Baud Rate:** 9600

#### AUX RELAY MODE (Screen 7.8)
- **Mode 1:** TRIP RELAY AUX. RELAY MODE WHILE FAILURE
- **Mode 2:** REMOTE MODBUS

### 11. Temperature Bias Settings (Screen 7.8.2)

- **Temperature Bias:** YES
- **Temperature T1:** 55°C
- **Temperature TM:** 120°C

### 12. Fault Screen Descriptions

#### Undervoltage / Overvoltage (Screens 1.9 and 1.10)

**Fault Type Indicators:**
- UV = Undervoltage
- OV = Overvoltage

**Display Information:**
- Voltage values during fault conditions
- Voltage unbalance percentage
- Phases involved in fault
- Maximum or minimum value during fault

**Example - Undervoltage:**
- Voltage: 169 168 167 V
- Phase: V12
- Fault Type: UV

**Example - Overvoltage:**
- Voltage: 267 264 V
- Unbalance: 11%
- Fault Type: VUB

#### Voltage, Frequency and Heat Displays (Screens 1.11 to 1.15)

**Fault Type Indicators:**
- VUB = Voltage Unbalance
- FS = Frequency Shift
- VSP = Single Phasing
- PHASE REVERSAL

**Display Information:**
- Voltage values during fault conditions
- Voltage unbalance percentage
- Fault indication
- Phases involved in fault
- Centigrade degree measurement
- Measured value

#### Fault History Screen Description

**Display Format:**
- Fault Number
- Fault Type
- Fault Value Indication
- Phase Involved in Fault

**Example:**
- Entry 18: UV 200V V12
- Entry 17: FS 68.0 Hz

### 13. Glossary of Terms

#### Fault Codes
- **OL** = Overload
- **UC** = Undercurrent
- **CSP** = Current Single Phase
- **CUB** = Current Unbalance
- **FS** = Frequency Shift
- **PR** = Phase Reversal
- **VSP** = Voltage Single Unbalance
- **RL** = Locked Rotor
- **VUB** = Voltage Unbalance
- **UV** = Undervoltage
- **OV** = Overvoltage
- **PF** = Power Factor
- **SM** = Start Motor
- **TEF** = Total Energy Fault
- **SPH** = Start Per Hour
- **3F** = Third Failure
- **BR** = Bypass Relay
- **OT** = Overtemperature
- **LR** = Locked Rotor

#### Electrical Abbreviations
- **V** = Voltage
- **I** = Current
- **TD** = Trip Delay
- **SD** = Start Up Delay
- **TM** = Motor Temperature
- **SCHEDL** = Schedule
- **COM** = Communication
- **AUX** = Auxiliary
- **UNDERVOLT** = Undervoltage
- **OVERVOLT** = Overvoltage
- **FREQ** = Frequency
- **UND** = Under
- **ACCEL** = Acceleration

### 14. GIII+MV Schedule Timer Adjustment Guide

This section applies only to GIII+MV models ordered with "+" which include Clock Adjustments and Schedule Timer options.

#### EVENT Configuration Process

**Example: EVENT 01**
- **Days:** Tuesday to Saturday and Holiday
- **ON Time:** 7:30 hrs
- **OFF Time:** 16:45 hrs

**Steps:**
1. Press SELECT to change to next day (Tuesday)
2. Continue through days: Tuesday (T), Wednesday (W), Thursday (T), Friday (F), Saturday (S), Sunday (S), Holiday (H)
3. Configure ON time: Press D or Y until finding hour desired, press SELECT to enter
4. Configure ON minutes: Press D or Q until finding minutes desired, press SELECT to enter
5. Configure OFF time using same process
6. Press A or Y to find EVENT ADJUST option
7. Press SELECT on YES option to confirm
8. Screen shows: TWIFS-H ON 07:30 / OFF 16:45

#### HOLIDAY Configuration Process

**Example: HOLIDAY 01 - June 24th**

**Steps:**
1. Press A or Y to find HOLIDAY ADJUST option
2. Press SELECT to enter
3. Configure Day: Press D or Y until finding day 24, press SELECT to enter
4. Configure Month: Press D or Q until finding month 6, press SELECT to enter
5. Screen shows: HOLIDAY 01/20 / DAY: 24 / MONTH: 6

**To Add Additional Events or Holidays:**
- Press A or D to look for available event/holiday number
- Press SELECT to enter configuration
- Follow indicated example steps above
- To exit, press N/Y to return to screen 7.4

### 15. GIII+MV Dismounting Instructions

**WARNING:** Disconnect power supply (Circuit Breaker OFF) and electrical wiring before dismounting GIII+MV. Electrical shock will result in death or serious injury.

#### 11.1.1 DIN Rail Dismounting Without CT Box

1. Using a flat screwdriver, pull downward the mounting bracket located at the rear and bottom side of GIII+MV
2. With screwdriver in position (2), pull out GIII+MV from DIN Rail

**Mounting Recommendation:** Pull downward 2 mm with a soft movement when using screwdriver. Strong movement could break the supporting bracket.

#### 11.1.2 DIN Rail Dismounting With CT Box

1. Using a flat screwdriver, pull downward the mounting bracket located at the rear and bottom side of GIII+MV
2. With screwdriver in position (2), pull out GIII+MV from DIN Rail

#### 11.2.1 Flat Surface Dismounting Without CT Box

1. Unscrew both screws fixed on flat surface through attachable mounting ears
2. Pull out GIII+MV relay from flat surface

#### 11.2.2 Flat Surface Dismounting With CT Box

1. Unscrew both screws fixed on flat surface through attachable mounting ears
2. Pull out GIII+MV relay from flat surface

#### 11.3.1 Flush Mount Dismounting

1. Remove the Flush Mounting Brackets:
   - Pull out the point indicated in the figure
   - Slide backward the piece
2. Remove the Flush Mounting Attachment and the GIII+MV relay

---

**Document Information:**
- Product: GIII+MV Motor Protection Relay
- Manufacturer: Genteca (Generación de Tecnología)
- Voltage Range: 200-480 V~
- Power Frequency: 60 Hz
- CT Ratio: 400/5
- Nominal Current: 100 A
