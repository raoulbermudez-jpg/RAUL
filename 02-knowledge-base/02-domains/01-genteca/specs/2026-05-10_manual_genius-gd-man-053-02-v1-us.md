---
title: "GSPT General Description and Installation Manual"
type: Technical
source: "GD-MAN-053-02-V1-US.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GSPT"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GSPT General Description and Installation Manual

## General Description

GSPT is an electronic Submersible Pump Integral Protection Relay that constantly supervises the Motor Current and the main electrical parameters such as Voltage, Frequency, Power factor, Real power, Reactive power and Energy consumption, giving the most reliable protection against Overload, Phase failure, Phase reversal, Single phasing, Unbalanced conditions, Overtemperature, and excessive Starts per hour.

### WARNING
Only qualified technicians with knowledge about overload relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

This product may start automatically; the user must take cautions to avoid hazards to people.

## GSPT Parts and Pieces

### Front Side View Components:
1. LCD display
2. Indicator light (LED): Status Relay and Failure
3. START Push Button
4. ADJUST Push Buttons (Up & Down)
5. SELECT Push Button
6. Back Groove for DIN Rail mounting
7. Attachable Mounting Ears
8. Supporting Bracket
9. Holes with current sensors, to pass power cables to the motor
10. L1 L2 L3 input
11. Control Relay (95-96) and (97-98)
12. GIO PORT
13. Protective plastic cover of the GIO PORT

## Mechanical Installation

### DIN Rail Mounting Instructions

Place GSPT at inclined position with its back side placed toward the upper edge of the DIN Rail and push down GSPT relay until it clicks on the rail.

### CAUTION
GSPT must be installed in an accessible position free from dust, dirt, dampness and vibration. Allow enough space for air circulation around the enclosure and easy access to all operator controls. Indoors use only.

This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

An incorrectly applied or installed GSPT can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the GSPT.

### Flat Surface Mounting Instructions

a) Take off the two (2) attachable mounting ears located at back side of GSPT, insert and slip both attachable mounting ears into the GSPT back side grooves.

b) Place GSPT over flat surface panel and fix it using a screwdriver suitable for screws 3/16" x 1/2".

**Recommendation for Flat Surface Mounting:**
Make two (2) holes (5/32") on panel surface before installing.

## GSPT General Dimensions

- Length: 111 mm
- Width: 100 mm
- Height: 96 mm
- Hole diameter for flat mounting: 5/32"

## Electrical Connection

### WARNING
Risk of Electric Shock. Disconnect power supply before installing GSPT. Electric Shock will result in death or serious injury.

Check that the voltage and current of chosen GSPT model correspond to line voltage and motor current.

### Terminal Designation

| TERMINAL | DESCRIPTION |
|----------|-------------|
| L1 | Voltage Input (Phase R) |
| L2 | Voltage Input (Phase S) |
| L3 | Voltage Input (Phase T) |
| 95-96 | Auxiliary Relay Contact: Tripped / Normal |
| 97-98 | Trip Relay Contact: Connected / Open |

**Status:**
- Tripped: 95-96 connected, 97-98 open
- Normal: 95-96 open, 97-98 connected

### Basic Diagram Installation

Connect L1 L2 L3 terminal for Voltage Input in parallel connection before line starter circuit through Contactor. Use three Current Sensing Holes for passing wires before connection to 3 phases motor. Using less than three (3) wires shall cause current unbalance and wrong measures.

### Wiring Recommendations

- Avoid over tightening the M3 screws upon terminals during wiring connection
  - Tightening Torque: 4.4 lbf-in, 5.1 Kgf-cm
- Wire Strip Length: 6-7 mm
- Terminal wiring size: 2 AWG 10 (4mm²) to AWG 18
- Current Sensing Holes (conduits) wiring size: 2 AWG 4 (11mm)

### External Toroids Diagram Installation

For external toroids connection, reference the communication protocol with MODBUS RTU protocol through GIO PORT.

## GSPT Operation

GSPT constantly supervises current and voltage values; when any harmful condition occurs, the output connection is deactivated until the fault disappears and power line conditions returns to an acceptable level. Specific timing such as Start Up Delay and Fault Detection Delay are incorporated to prevent nuisance tripping due to rapid power fluctuations.

GSPT provides LCD Display to indicate the output status (voltage, current, unbalance, frequency and load status). It also provides four (4) push buttons (On/Off, Up, Down and Select) for electrical parameter adjustment such as Voltage, Current, Frequency, Fault Detection Delay and others. A Communication Port with MODBUS RTU protocol is included in GSPT.

## Screen Adjustment and Display

### Initial Screen
The LCD displays:
- Phase-to-phase voltages (V12, V23, V31)
- Voltage Unbalance (VUB) percentage
- Status: OFF or ON
- Operating Mode: MODBUS or MANUAL
- Power parameters
- Frequency

### Fault Screen Description

Various fault conditions are displayed with specific information:
- Undervoltage (UV) / Overvoltage (OV): Voltage values during fault conditions
- Voltage Unbalance (VUB): Percentage of unbalance
- Frequency Shift (FS): Frequency value in Hz
- Phase Reversal (PR): Detection indication
- Voltage Single Phase (VSP): Phase identification
- Overload (OL): Current level
- Undercurrent (UC): Current condition
- Locked Rotor (LR): Rotor status

### Main Adjustment Menu (Screen 7)

Press both push buttons at the same time to access the Adjustment Menu. If access is locked, enter the required password.

Available adjustments:
- VOLTAGE ADJUST
- CURRENT ADJUST
- CLOCK ADJUST
- SCHEDULE TIMER
- START MODE
- CHANGE PASSWORD
- MODBUS ADDRESS
- DELETE HISTORY
- RESTART

## Schedule Timer Adjustment Guide

The GSPT models with Schedule Timer feature allow configuration of:

### EVENT Configuration
- Days of operation (Monday to Sunday)
- Holiday inclusion option
- ON/OFF times (hours and minutes)
- Multiple events support (up to EVENT 60)

### HOLIDAY Configuration
- Specific dates for holidays
- Date format: DD/MM
- Integration with schedule events

## Abbreviations and Glossary

| Abbreviation | Meaning |
|--------------|---------|
| OL | OVERLOAD |
| UC | UNDERCURRENT |
| CSP | CURRENT SINGLE PHASE |
| CUB | CURRENT UNBALANCE |
| FS | FREQUENCY SHIFT |
| PR | PHASE REVERSAL |
| VSP | VOLTAGE SINGLE PHASE |
| LR | LOCKED ROTOR |
| VUB | VOLTAGE UNBALANCE |
| UV | UNDERVOLTAGE |
| OV | OVERVOLTAGE |
| AUX | AUXILIARY RELAY |
| ADJ | ADJUST |
| HRS | HOURS |
| PF | POWER FACTOR |
| TD | TRIP DELAY |
| TC | STARTUP DELAY |
| TEF | TOTAL ENERGY FAULT |
| SM | START MOTOR |

## GSPT Dismounting Instructions

### WARNING
Disconnect power supply (Circuit Breaker OFF) and electrical wiring before dismounting GSPT. Electrical shock will result in death or serious injury.

### DIN Rail Dismounting

a) Using a flat screwdriver, pull downward the mounting bracket located at rear and down side of GSPT.

b) With screwdriver at position (2), pull out GSPT from DIN Rail.

**Recommendation:** Pull downward 2 mm with a soft movement when using screwdriver for dismounting. Strong movement could break the supporting bracket.

### Flat Surface Dismounting

Unscrew both screws fixed on Flat Surface through attachable mounting ears and then pull out the GSPT relay from flat surface.

## Technical Specifications

### A) Power Supply Circuit

| Parameter | Value |
|-----------|-------|
| Rated Voltage, Ue | 208/220/240 VAC or 440/480 VAC |
| Voltage Operation Limits, Ue | 145→312 VAC or 264→672 VAC |
| Average Consumption, In | 45 mA |
| Rated Frequency, Fn | 50/60 Hz |
| Frequency Operation Limits, Fr | 42→70 Hz |
| Rated Duty | Uninterrupted Duty |

### B) Environmental Conditions, Operation Limits and Installing

| Parameter | Value | Standard |
|-----------|-------|----------|
| European Standards | IEC61010-1, IEC60255-6, IEC60947-1 LVD & EMC | — |
| US Standards | UL (pending), NFPA, NEMA | — |
| CE Marking | CE (pending), Low Voltage Devices IEC60947-1 | — |
| Ambient Air Temperature (Operation) | -5°C to 55°C (23°F to 131°F) | — |
| Ambient Air Temperature (Storage) | -10°C to +70°C (14°F to 158°F) | — |
| Maximum Relative Humidity | 85% R.H. | — |
| Vibrations | Class 1, Amplitude <0.035mm or 1G, 10Hz <f< 150Hz | IEC 60255-21-1 |
| Degree of Protection | IP20, Protected against objects >12.5mm, but no protection against water | IEC 60529 |
| Pollution Degree | Degree 3 | IEC 60255-5 |
| Overvoltage Category | Category III | IEC 60255-5 |
| Rated Insulation Voltage | 500V | IEC 60255-5 |
| Impulse Voltage Test | 5 kV | IEC 60255-5 |
| Impulse Dielectric Test | 2.5 kV 50/60 Hz @ 1 min | — |
| Flammability Rating of Enclosure | V-0 | US STANDARDS |
| Enclosure Material | SNA ABS | — |
| Mounting Position | Any Position | — |
| Mounting Features | Symmetrical DIN Rail DIN 43880, Flat surface mounting screw 3/16" x 1/2" | NEMA Style |
| Terminal Screw Type | Flat M3 | — |
| Tightening Screw Torque | 5.1 Kgf×cm (4.4 lb×in) | — |
| Terminal Wiring | 10-18 AWG | — |
| Current Sensing holes for Motor Wiring | Ø=11mm AWG 4 | — |
| Dimensions | 92×91×96 (L×W×H) mm | — |
| Weight | 494 g (1.09 lb) | — |

### C) Control Characteristics

| Parameter | Value | Standard |
|-----------|-------|----------|
| Output Contact Rating | 8 A 300V Pilot Duty, 1 A @240 VAC / 0.5 A @480 VAC | UL 508 Section 139.1 |
| Electrical Life Expectancy | 100,000 Operations | — |
| Mechanical Life Expectancy | 10,000,000 Operations | — |
| Utilization Category | AC-15, Capacity for loads >72 VA | IEC60947-5-1 |

### D) Range Setting, Measuring

#### Voltage Measurement
| Model | Range | Accuracy |
|-------|-------|----------|
| 208/220/240 VAC | 0→312 VAC | ±2% |
| 440/480 VAC | 0→672 VAC | ±2% |

#### Frequency Range
| Parameter | Value | Tolerance |
|-----------|-------|-----------|
| Frequency Range | 45.0→70.0 Hz | ±1% |

#### Current Measurement (According to Model)
| Model | Range | Accuracy |
|-------|-------|----------|
| 04 A | 1.5→40 A | ±5% |
| 12 A | 0.3→125 A | ±5% |
| 32 A | 1→320 A | ±5% |
| 80 A | 25→800 A | ±5% |
| EXT (CT I5) | 5→383% CT | ±5% |

#### Other Measured Parameters

| Parameter | Range | Tolerance |
|-----------|-------|-----------|
| Instantaneous Power Factor | 0.00→1.00 | ±8% |
| Instantaneous Reactive Power | 0.0→999.9 KVA | ±4% |
| Instantaneous Real Power | 0.0→999.9 KW | ±4% |
| Energy | 0→999999 KWH | ±4% |
| Total Motor Running Time (hours) | 0→999999 H | ±1% |

### E) Algorithms and Protection Functions

#### Undervoltage (UV)
| Voltage Model | Setting Range |
|---------------|----------------|
| 208 VAC | 165→225 VAC |
| 480 VAC | 350→460 VAC |

#### Overvoltage (OV)
| Voltage Model | Setting Range |
|---------------|----------------|
| 208 VAC | 215→270 VAC |
| 480 VAC | 460→580 VAC |

#### Voltage Hysteresis Threshold
| Voltage Model | Value |
|---------------|-------|
| 208 VAC | 6 VAC |
| 480 VAC | 12 VAC |

#### Voltage Unbalance Detection (VUB)
- Detection Range: 2%→10%
- Hysteresis: IN VUB >33%, OUT VUB <28%

#### Single Phasing (VSP)
- Detection: 0.0 Rated Frequency

#### Frequency Shift (FS) Tolerance
- Range: 2%→10%

#### Phase Reversal (PR)
- Normal Phase Sequence: A→B→C
- Reversed Phase Sequence: C→B→A
- Trip Delay: <1 sec

#### Trip Delay because of Other Voltage Failures (TD)
- Range: 1→30 sec

#### Start Up Delay (TC)
- Range: 0→600 sec

#### Trip Delay because of VSP
- Value: 3 sec

#### Start Mode
- Selection: Auto/Manual

#### Minimum Time Between Two Start Up
- Duration: 50×Thermal Class Sec

#### Nominal Current Setting
| Current Model | Setting Range |
|---------------|----------------|
| 04 A | 1.5→40 A |
| 12 A | 0.5→125 A |
| 32 A | 10→320 A |
| 80 A | 25→800 A |
| EXT (CT I5) | 25→383% CT |

Tolerance: ±25%

#### Overload Level Setting (OL)
- Range: 5%→50%

#### Thermal Class Setting
- Range: 5→35

#### Dynamic Setting of Motor Model (Cold Curve / Hot Curve)
- Thermal class varies from 1→1/3 of adjusted class according to start up time and motor load level
- Standard: IEC 60255.3

#### Maximum Time Between Cold/Hot Curve
- Duration: 2 Hours (from 1 to 1/3 or from 1/3 to 1)
- Standard: IEC 60266-8-1990, IEEE Std 97-770-1996

#### Trip Delay because of Overload
- Duration: According to Overload Level and Adjusted Class

#### Heat Threshold because of Overload Failure
- Value: 100%

#### Current Unbalance (CUB)
- Threshold: CUB >48%
- Trip Delay: 2 Sec

#### Current Stall Phase (CSP)
- Threshold: CUB >60%
- Trip Delay: 1 Sec

#### Locked Rotor (LR)
- User selection: YES/NO
- Heat setting: 0→100%

#### High-Inertia Load Option
- Selection: YES/NO
- Heat Threshold: 400%
- Start up Delay Range: 20→120 Sec

#### Thermal Machine Cooling Time
- Duration: 50×Thermal Class Sec

#### Undercurrent (UC)
- Selection: YES/NO
- Disconnection Type: %Inom / Power Factor (PF)
- Adjusting Range (%Inom): 30%→90% Inom
- Adjusting Range (PF): 0.3→0.9
- Trip Delay Range: 5→600 Sec
- Start Up Delay Range: 2→500 Min

#### Third Failure Detection
- Selection: YES/NO
- Condition: 3 Current failures in less than 105 min
- Permanent disconnection due to Third Failure

#### Accelerated Locked Rotor
- Trip Delay: 3 Sec

#### Maximum Starts per Hour
- Selection: YES/NO
- Limit of allowable starts per hour (minimum value selectable by user)
- Constraint: Maximum automatic starts until 12 according to HP NEMA MG10

#### Time Between Starts
- Range: 1→10 min

### F) Communications and Other Special Functions

| Feature | Specification |
|---------|---------------|
| Communication Protocol | MODBUS RTU @ 9600 8N1 |
| Communication Ports | GIO PORT (*) |
| Address Range | 1→127 |
| History Buffer Memory | 80 last faults report (failure type, value, date, hour and time elapsed) |
| Parameters Block | 0000 Free, 0001→9999 Blocked |

(*) GIO Plug is required for GIO Port communication. Available by separate order.

### G) Immunity and Emissions, Electromagnetic Interference (EMC) for Heavy Industrial Environment (B)

| Test | Standard |
|------|----------|
| Electrostatic Discharge | IEC 61000-4-2 |
| Immunity to Ratio Frequency Test | IEC 61000-4-3 |
| Electrical Fast Transients | IEC 61000-4-4 |
| Surge Immunity Test | IEC 61000-4-5 |
| Ratio-Frequency Continuous Conducted | IEC 61000-4-6 |
| Power Frequency Magnetic Field | IEC 61000-4-8 |
| Voltage Dips, Short Interruptions and Voltage Variations | IEC 61000-4-11 |
| Harmonics and Interharmonics Immunity Tests | IEC 61000-4-13 |
| Voltage Fluctuation Immunity | IEC 61000-4-14 |
| Unbalance Immunity Test | IEC 61000-4-27 |
| Variation of Power Frequency | IEC 61000-4-28 |

## Cold-Hot Curves

The GSPT provides dynamic thermal protection with adjustable cold and hot curves. The cold curve is used when the motor is cold (starting), while the hot curve is used after the motor has been running and heated. The curves are temperature-dependent and automatically adjust based on the start-up time and motor load level.

## Maximum Allowable Starts per Hour (NEMA MG10)

| HP | Starts/Hour |
|----|-------------|
| 1 | 12 |
| 2 | 12 |
| 3 | 12 |
| 5 | 7 |
| 7.5 | 7 |
| 10 | 5 |
| 15 | 5 |
| 20 | 4 |
| 25 | 4 |
| 30 | 4 |
| 40 | 3 |
| 50 | 3 |
| 60 | 3 |
| 75 | 3 |
| 100 | 2 |
| 125 | 2 |
| 150 | 2 |
| 200 | 2 |
| 250 | 2 |

**Note:** Maximum allowable starts per hour depend on the settings according to the maximum power of the motor. Values shown are approximations to standard NEMA MG10.

## How to Order According to Customer Needs

### GSPT Order Code Format

**GSPT - [VOLTAGE] - [AMPERAGE] - [LANGUAGE]**

#### Voltage Options
- 208: 208/220/240 V~
- 480: 440/480 V~

#### Amperage Options
- 04: 1.5-4 A
- 12: 3.5-125 A
- 32: 10-32 A
- 80: 25-80 A
- 00: CT EXTERNAL

#### Language Options
- S: SPANISH
- E: ENGLISH
- P: PORTUGUESE

### Example
GSPT-208-12-E (GSPT for 208/220/240 VAC, 3.5-125A, English Language)

## Manufacturer Information

Made and designed by GENTE, Generación de Tecnología, C.A.
- RIF: J-00223173-4
- Address: Av. El Buen Pastor cruce con calle Vargas, Edif. Alba, Piso 1, Local 1-A, Boleíta Norte, Caracas - Venezuela, Zona Postal 1070
- Phone: +(58-212) 237.07.11 (Master)
- Fax: +(58-212) 235.24.97
- E-mail: genteven@genteca.com.ve
- Website: www.genteca.com.ve

**NOTE:** Technical data are valid at the time of printing. Manufacturer reserves the right to subsequent alterations.
