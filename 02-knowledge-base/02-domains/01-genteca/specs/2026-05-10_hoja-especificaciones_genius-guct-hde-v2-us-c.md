---
title: "GUCT - Integral Motor Protection Relay"
type: Technical
source: "GUCT_HDE-V2_US_c.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "GUCT"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GUCT - Integral Motor Protection Relay

## Overview

GUCT is a microcontrolled based three-phase Integral Motor Protection Relay, specifically designed to protect electric loads and motors from failure and damage due to common current and voltage faults.

GUCT constantly supervises current and voltage values; when any harmful condition occurs, the output connection is deactivated until the fault disappears, power line conditions return to an acceptable level and the motor has been totally cooled. Specific timing such as Start Up Delay (TC) and Trip Delay (TD) are incorporated to prevent nuisance tripping due to rapid power fluctuations.

## Features

### Measurement of:
* Current
* Voltage
* Frequency
* Power Factor (PF), Reactive Power (KVA), Real Power (KW)
* Energy Consumption (KWH)
* Temperature

### Reports:
* Voltage & Current report
* PE KVA, KWH, KW report
* Adjusted Values report
* Total Motor Running Time report
* Start Mode report
* 20 Last Fault report
* Power Frequency report
* Motor Temperature report

### Adjustments of:
* Overload
* Undercurrent
* Overvoltage
* Undervoltage
* Current Unbalance
* Voltage Unbalance
* Frequency
* Trip Delay
* Start Up Delay after Voltage Fault Recovery
* Motor Thermal Class
* Clock Adjustment
* Control of Motor High-Inertia Load
* Schedule Timer
* AUTO / MANUAL Restart Mode
* Password

### Protection against:
* Overload / Undercurrent
* Overvoltage / Undervoltage
* Frequency Shift
* Voltage Unbalance
* Current Unbalance
* Single Phasing
* Phase Reversal
* Locked Rotor

### Physical Features:
* Din-Rail, Flat Surface or Flush mounting
* 16x2 LCD Display with current values, voltage values and load report information on screen
* Four (4) push buttons for operation and protection parameter adjustments
* Enclosure material UL94V0
* Thermal memory

### Communications:
* GIO Port or RS485 @ 9600 baud output available (MODBUS RTU protocol)

## Product Standards Applied

Designed according to CE Standards (LVD and EMC):
* IEC 61010-1
* IEC 60255-6
* IEC 60255-8
* IEC 60947-1

Designed according to:
* UL 508
* IEEE C37.112

## General Functions & Range of Applications

The GUCT provides electrical protection through the following general functions and setting ranges:

* Overvoltage detection: 5% up to 20% rated voltage
* Undervoltage detection: -20% up to -5% rated voltage
* Voltage Unbalance detection: 2% up to 10% rated voltage
* Single Phasing voltage detection: IN 33% - OUT 28%
* Phase Reversal detection time: <1 sec
* Start Up Delay after voltage fault recovery: 0 to 600 seg
* Voltage Fault detection time: 1 to 30 sec
* Frequency Shift detection: +/-2% up to +/-10% rated frequency
* Overcurrent level setting: 5% up to 50%
* Undercurrent detection: Adjustable by PF or by nominal
* Current Unbalance detection: CUB > 48%
* Single Phasing current detection: CUB > 60%
* Power Factor detection: 0.0 up to 1.0
* Thermal Class IEC 60255-8: in step of one by one

## Physical Features

The GUCT features an innovative mechanical design allowing three placement options:
* Symmetrical Din-Rail mounting
* Flat Surface mounting, using an exclusive attachable mounting ear
* Flush mounting

The relay includes:
* Current sensing holes for motor wiring
* Back groove for DIN rail mounting
* 16x2 LCD Display with indicator lights
* Three push buttons (START, ADJUST, SELECT)
* GIO Port for optional serial communication

## Installation

### Connection Diagram

Power supply from 3-phase 50/60 Hz line and starter circuits. Power supply wires must pass through GUCT holes before connecting to motor.

Optional GIO PLUG available for serial communication with other devices.

**Output Contact Status:**
* Tripped: 95-96 closed, 97-98 open
* Normal: 95-96 open, 97-98 closed

### Connection Diagram for External Toroids

External toroids may be connected at the input (Before line starter circuits) for current sensing.

**Output Contact Status:**
* Tripped: 95-96 closed, 97-98 open
* Normal: 95-96 open, 97-98 closed

## Safety Information

Only qualified technicians with knowledge about overload protection relay and associated machinery should perform installation, starting up, and maintenance of the system. Failure to comply may result in equipment damage and/or personal injury.

### EMC Considerations

This product has been designed for industrial environment. Use of this product in residential environment may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

## Special Tools for Installation or Connection

* Screwdriver suitable for M2.5 screws (for terminal connection)
* Screwdriver suitable for screws 3/16" x 1/2" (for flat surface mounting)
* Ammeter

## How to Order

GUCT configuration follows this nomenclature:

**GUCT + Number of Phases + Control Voltage + Amperage + Language**

* Number of Phases:
  - T = 3 PHASES
  - 80 = SCHEDULE TIMER

* Control Voltage:
  - 208 = 208V
  - 480 = 440/480V

* Amperage:
  - 04 = 1-4A
  - 2 = 3-5 A
  - 80 = 25-80A
  - 00 = CT EXTERNAL

* Language:
  - S = SPANISH
  - E = ENGLISH

## Technical Specifications

### A) Power Supply Circuit

| Parameter | Value |
|-----------|-------|
| Rated Voltage, Ue | 208/220/240 or 440/480 V |
| Voltage Operation Limits, Ue | 145-312 V or 264-672 V |
| Average Consumption, In | 45 mA |
| Rated Frequency, Fn | 50/60 Hz |
| Frequency Operation Limits, Fn | 42→70 Hz |
| Rated Duty | Uninterrupted Duty |

### B) Environmental Conditions, Operation Limits and Installing

| Parameter | Value | Standard |
|-----------|-------|----------|
| Designed according to European Standards (LVD & EMC) | IEC 61010-1 | |
| Designed according to US Standards | UL 508, NKCR, Auxiliary Devices, Low Voltage Devices | UL 508, IEC60947-1 |
| CE Marking | CE (pending) | |
| Ambient Air Temperature (Operation) | -5°C to 55°C (23°F to 131°F) | |
| Ambient Air Temperature (Storage) | -10°C to +70°C (14°F to 158°F) | |
| Maximum Relative Humidity | 85% R.H. | |
| Vibrations | Class 1, Amplitude <0.035mm or 1G, 10Hz < f < 150Hz | IEC 60255-21-1 |
| Degree of Protection | IP20, Protected against objects > 12.5mm, but no protection against water | IEC 60529 |
| Pollution Degree | Degree 3 | IEC 60255-5 |
| Overvoltage Category | Category III | IEC 60255-5 |
| Rated Insulation Voltage | 500V | IEC 60255-5 |
| Impulse Voltage Test | 5 KV | IEC 60255-5 |
| Impulse Dielectric Test | 2.5 KV 50/60 Hz @ 1min | UL-508 |
| Flammability Rating of Enclosure | V-0 | UL-94 |
| Enclosure Material | Polymers: PC, ABS, NYLON | |
| Mounting Position | Any Position | |
| Mounting Features | Flat surface mounting, screw 3/16" x 1/2" | NEMA Style, IEC 715 |
| Terminal Screw Type | Flat M3 | |
| Tightening Screw Torque | 5.1 Kgf x cm (4.4 Ib x in) | |
| Terminals Wiring | 10-18 WG | |
| Current Sensing holes for Motor Wiring | O < 11mm AWG 4 | |
| Dimensions | 92 x 91 x 96 (L x W x H) mm | |
| Weight | 494 g (1.09 lb) | |

### C) Control Characteristics

| Parameter | Value |
|-----------|-------|
| Output Contact Rating | 8 A @ 300 V Pilot Duty, 9 A @ 1A 0 240 VAC / 0.5 A @ 480 VAC |
| Electrical Life Expectancy | 100,000 Operations |
| Mechanical Life Expectancy | 10,000,000 Operations |
| Utilization Category | AC-15, Capacity for loads > 72 VA |
| Standard | IEC60947-5-1 |

### D) Range Setting, Measuring

#### According to Voltage Model (208/280 VAC):
* Voltage Measurement Range, Um: 0-312 VAC ± 2% accuracy

#### According to Voltage Model (280-672 VAC):
* Voltage Measurement Range, Um: 0-672 VAC ± 2% accuracy

#### According to Current Model:
* Current Measurement Range, Im: 15→40 / 0.3→125 / 1→320 / 25→800 / 5%→33CT / 900 (5% accuracy)

### Another Measured Parameters

| Parameter | Range | Accuracy |
|-----------|-------|----------|
| Frequency Range | 45.0→70.0 Hz | 1% |
| Instantaneous Power Factor | 0.00→1.00 | 8% |
| Instantaneous Reactive Power KVA | 0.0→999.9 KVA | 4% |
| Instantaneous Real Power KW | 0.0→999.9 KW | 4% |
| Energy KWH | 0→999999 KWH | 4% |
| Total Motor Running Time (hours) | 0→999999 H | 1% |

### E) Algorithms and Protection Functions

#### According to Operation Voltage:

| Function | Setting Range (208-280V) | Setting Range (280-672V) |
|----------|--------------------------|--------------------------|
| Undervoltage (UV) @ Imotor=0 or OL | 165→225 | 350→460 |
| Overvoltage (OV) @ Imotor=0 or OL | 215→270 | 460→580 |
| Voltage Hysteresis Threshold | 6 | 12 VAC |

#### Voltage Unbalance Detection (VUB):
* Range: 2%→10% Level settings
* Single Phasing (VSP): IN VUB > 33%, OUT VUB < 28%

#### Rated Frequency:
* 50/60 Hz Level settings

#### Tolerance for Frequency Shift (FS):
* Range: 2%→10% Level settings

#### Phase Reversal (PR):
* Normal Phase Sequence: A>B>C
* Reversed Phase Sequence: C>B>A
* Trip Delay: <1 sec

#### Trip Delay because of Another Voltage Failures (TD):
* Range: 1→30 sec Level settings

#### Start Up Delay (TC):
* Range: 0→600 sec Level settings

#### Trip Delay because of VSP:
* Value: 3 sec

#### Start Mode:
* Auto/Manual selection

#### Minimum Time Between Two Start Up:
* Value: 50 x Thermal Class Sec

#### According to Operation Current:
| Amperage Class | Nominal Current Setting |
|----------------|------------------------|
| 04 | 1→4 A |
| 12 | 3→5 A |
| 32 | 1→32 A |
| 80 | 25→80 A |
| EXT (CTI5) | 25→33 CT |

#### Overload Level Setting (OL):
* Range: 5%→50% In Level settings

#### Thermal Class Setting:
* Range: 5→35 Level settings

#### Dynamic Setting of Motor Thermal Class:
* Varies from 1→1/3 of adjusted class according to start up time and motor load level

#### Maximum Time Between Cold/Hot Curve:
* Value: 2 Hours (from 1 to 1/3 or from 1/3 to 1)
* Standard: IEC 60255-8-1990, IEEE C37.112-1996

#### Trip Delay because of Overload:
* According to Overload Level and Adjusted Class

#### Heat Threshold because of Overload Failure:
* Value: 100%

#### Current Unbalance (CUB):
* Value: CUB > 48%

#### Current Stall Phase (CSP):
* Value: CUB > 60%

#### Accelerated Locked Rotor Detection (LR):
* Value: YES/NO Heat setting

#### Trip delay because of CSP:
* Value: 1 sec

#### Trip Delay because of CUB:
* Value: 2 Sec

#### High-Inertia Load Option:
* Value: YES/NO selection

#### High-Inertia Load Heat Threshold:
* Value: 400%

#### High-Inertia Load Start up Delay:
* Range: 20→120 Sec Level settings

#### Thermal Machine Cooling Time:
* Value: 50 x Thermal Class Sec

#### Undercurrent:
* Value: YES/NO

#### Undercurrent Disconnection Type (UC):
* Options: % Inom / Power Factor (PF)

#### Undercurrent Adjusting (% Inom):
* Range: 30%→90% Inom Level settings

#### Undercurrent Adjusting (PF):
* Range: 0.3→0.9 Level settings

#### Trip Delay because of UC:
* Range: 5→600 Sec Level settings

#### Start Up Delay because of UC:
* Range: 2→500 Min Level settings

#### Third Failure Detection:
* Value: YES/NO Level settings

#### Permanent disconnection because of Third Failure:
* Criteria: 3 Current failures in less than 105 min

#### Trip delay because of Accelerated Locked Rotor:
* Value: 3 Sec
* Standards: IEEE Std C37.112-1996

### Events Control Characteristics

| Parameter | Format | Specifications |
|-----------|--------|-----------------|
| Real Time Clock | hh:mm mm/dd/yy UMT | For Heavy Industrial Environment |
| Load Control by Events (schedule) | YES/NO | User selection |

### F) Communications and Other Special Functions

| Parameter | Value |
|-----------|-------|
| Communication Protocol | MODBUS RTU @ 9600 8N1 |
| Communication Ports | Port GIO PORT (*) |
| Address Range | 1→127 |
| History Buffer Memory | 20 last faults report (failure type, value, date, hour and time elapsed) |
| Parameters Block | 0000 Free, 0001→9999 Blocked |

(*) GIO Plug is required for GIO Port communication. It is available by separate order.

### G) Immunity and Emissions, Electromagnetic Interference (EMC)

#### For Heavy Industrial Environment:

| Test | Standard |
|------|----------|
| Immunity to Radio Frequency Test | EC 61000-4-3 |
| Electrical Fast Transients | EC 61000-4-4 |
| Surge Immunity Test | EC 61000-4-5 |
| Radio-Frequency Continuous Conducted | EC 61000-4-6 |
| Power Frequency Magnetic Field | EC 61000-4-8 |
| Voltage Dips, Short Interruptions and Voltage Variations | IEC 61000-4-11 |
| Harmonics and Interharmonics Immunity Tests | IEC 61000-4-13 |
| Voltage Fluctuation Immunity | IEC 61000-4-14 |
| Unbalance Immunity Test | IEC 61000-4-27 |
| Variation of Power Frequency | IEC 61000-4-28 |

## Thermal Class - Tripping Cold Curve

The GUCT supports the following thermal classes according to standards IEEE C37.112 and IEC 60255-8:

* Class 5
* Class 10
* Class 15
* Class 20
* Class 25
* Class 30

**Note:** Hot Curve = Cold Curve / 3

The tripping time is calculated based on the load current (I load / I nom) where I nom is the current value adjusted on GUCT by the user.

## Specifications Notes

Technical data are valid at the time of printing. The manufacturer reserves the right to subsequent alterations.

**Manufacturer:**
Gente, Generación de Tecnología C.A
R.I.F: J-00223173-4
Av. El Buen Pastor, cruce con Calle Vargas, Edificio Alba, Piso 1, Local 1-A, Boleita Norte, Caracas, 1070, República Bolivariana de Venezuela
Phone: +58-212-237.0711 (Master)
Fax: +58-212-235.2497
E-mail: genteven@genteca.com.ve
Website: www.genteca.com.ve
