---
title: "GUCT Integral Motor Protection Relay - Technical Specifications"
type: Technical
source: "GD-HE-051-01-V1-US-C.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "GUCT"
version_status: "historica"
date_processed: "2026-05-10"
---

# GUCT Integral Motor Protection Relay

## Overview

GUCT is a microcontrolled based three-phase Integral Motor Protection Relay, specifically designed to protect electric loads and motors from failure and damage due to common current and voltage faults.

GUCT constantly supervises current and voltage values; when any harmful condition occurs, the output connection is deactivated until the fault disappears, power line conditions returns to an acceptable level and the motor has been totally cooled. Specific timing such as Start Up Delay (TC) and Trip Delay (TD) are incorporated to prevent nuisance tripping due to rapid power fluctuations.

## Features

### Measurement of:
- Current
- Voltage
- Frequency
- Power Factor (PF), Reactive Power (KVA), Real Power (KW)
- Energy Consumption (KWH)
- Temperature

### Reports:
- Voltage & Current report
- PE KVA, KWH, KW report
- Adjusted Values report
- Total Motor Running Time report
- Start Mode report
- 20 Last Fault report
- Power Frequency report
- Motor Temperature report

### Adjustments of:
- Overload
- Undercurrent
- Overvoltage
- Undervoltage
- Current Unbalance
- Voltage Unbalance
- Frequency
- Trip Delay
- Start Up Delay after Voltage Fault Recovery
- Motor Thermal Class
- Clock Adjustment
- Control of Motor High-Inertia Load
- Schedule Timer
- AUTO / MANUAL Restart Mode
- Password

### Protection Against:
- Overload / Undercurrent
- Overvoltage / Undervoltage
- Frequency Shift
- Voltage Unbalance
- Current Unbalance
- Single Phasing
- Phase Reversal
- Locked Rotor

### Physical Features:
- Din-Rail, Flat Surface or Flush mounting
- 16x2 LCD Display with current values, voltage values and load report information on screen
- Four (4) push buttons for operation and protection parameter adjustments

### Communications:
- GIO Port or RS485 @ 9600 baud output available (MODBUS RTU protocol)
- Digital Inputs Status

### Others:
- Enclosure material UL94V0
- Thermal memory

## Product Standards Applied

Designed according to CE Standards (LVD and EMC):
- IEC 61010-1
- IEC 60255-6
- IEC 60255-8
- IEC 60947-1

Designed according to:
- UL 508
- IEEE C37.112

## General Functions & Range of Applications (Intended Use)

The GUCT provides electrical protection through the following setting ranges:

- Overvoltage detection: 5% up to 20% rated voltage
- Undervoltage detection: -20% up to -5% rated voltage
- Voltage Unbalance detection: 2% up to 10% rated voltage
- Single Phasing voltage detection: IN 33% - OUT 28%
- Phase Reversal detection time: <1 sec
- Start Up Delay after voltage fault recovery: 0 to 600 sec
- Voltage Fault detection time: 1 to 30 sec
- Frequency Shift detection: +/-2% up to +/-10% rated frequency
- Overcurrent level setting: 5% up to 50%
- Undercurrent detection: Adjustable by PF or by I nominal
- Current Unbalance detection: CUB > 48%
- Single Phasing current detection: CUB > 60%
- Power Factor detection: 0.0 up to 1.0
- Thermal Class IEC 60255-8: 5 to 35 (in step of one by one)

## Physical Features

The GUCT features:
- Current sensing holes for motor wiring
- Attachable mounting ear for flat surface mounting
- Back groove for DIN rail mounting
- 16x2 LCD Display with indicator lights
- Four push buttons: START, ADJUST (2), and SELECT
- Model designation: GUCT+20880€

## Safety Information

**ATTENTION:** Only qualified technicians with knowledge about overload protection relay and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

### Measures to Be Taken into Consideration with Regards to EMC

**NOTICE:** This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

## Installation

### Connection Diagram

Three-phase, 50/60 Hz starter circuit wires must pass through GUCT holes before connecting to motor. GIO PLUG (Optional) available for serial communication with other devices.

Output contact configuration:
- Tripped: 95-96 connected, 97-98 open
- Normal: 95-96 open, 97-98 connected

GIO Port available for communications.

### Connection Diagram for External Toroids

Three-phase, 50/60 Hz starter circuit connections available for external toroid configurations. GIO PLUG (Optional) available for serial communication.

Output contact configuration:
- Tripped: 95-96 connected, 97-98 open
- Normal: 95-96 open, 97-98 connected

### Special Tools for Installation or Connection

- For terminal connection: screwdriver suitable for M2.5 screws
- For flat surface mounting: screwdriver suitable for 3/16" x 1/2" screws
- Ammeter

### How to Order GUCT

Selection parameters:
- NUMBER OF TIMER: 480, 32, 80, 00 (CT EXTERNAL)
- CONTROL VOLTAGE: 440/480V=
- AMPERAGE: 10-32A, 25-80A, or CT EXTERNAL
- LANGUAGE: E (ENGLISH), P (PORTUGUESE)

## Technical Specifications

### A) Power Supply Circuit

| Parameter | Value | Notes |
|-----------|-------|-------|
| Rated Voltage, Ue | 208/220/240 or 440/480 VAC | - |
| Voltage Operation Limits, Ue | 145-312 or 264-672 VAC | - |
| Average Consumption, In | 45 mA = | - |
| Rated Frequency, Fn | 50/60 Hz | - |
| Frequency Operation Limits, Fx | 42-70 Hz | - |
| Rated Duty | Uninterrupted Duty | - |

### B) Environmental Conditions, Operation Limits and Installing

| Parameter | Value | Standard |
|-----------|-------|----------|
| Designed according to European Standards | LVD & EMC | IEC 61010-1 |
| Designed according to US Standards | UL (pending), NKCR, Auxiliary Devices | UL 508 |
| CE Marking | CE (pending) | IEC 60947-1 |
| Ambient Air Temperature (Operation) | 5°C to 55°C (23°F to 131°F) | - |
| Ambient Air Temperature (Storage) | -10°C to +70°C (14°F to 158°F) | - |
| Maximum Relative Humidity | 85% R.H. | - |
| Vibrations | Class 1, Amplitude <0.035mm or 1G, 10Hz <f < 150Hz | IEC 60255-21-1 |
| Degree of Protection | IP20, Protected against objects > 12.5mm, but no protection against water | IEC 60529 |
| Pollution Degree | Degree 3 | IEC 60255-5 |
| Overvoltage Category | Category III | IEC 60255-5 |
| Rated Insulation Voltage | 500V | IEC 60255-5 |
| Impulse Voltage Test | 5 KV | IEC 60255-5 |
| Impulse Dielectric Test | 2.5 KV 50/60 Hz, 1 min | UL-508 |
| Flammability Rating of Enclosure | V-0 | UL-94 |
| Enclosure Material | Polymers: PC, ABS, NYLON | - |
| Mounting Position | Any Position | - |
| Mounting Features | Symmetrical DIN Rail, Flat surface mounting with screw 3/16" x 1/2" | DIN 43880, NEMA Style |
| Terminal Screw Type | Flat M3 | - |
| Tightening Screw Torque | 5.1 Kgf x cm (4.4 Ib x in) | - |
| Terminals Wiring | 10-18 WG | - |
| Current Sensing holes for Motor Wiring | Ø < 11mm | AWG 4 |
| Dimensions GUCT | 92 x 91 x 96 (LxWxH) | - |
| Weight GUCT | 494 g (1.09 lb) | - |

### C) Control Characteristics

| Parameter | Rating | Standard |
|-----------|--------|----------|
| Output Contact Rating | 8 A 300 Pilot Duty, 1A @ 240VAC, 1A @ 480 VAC | UL 50 |
| Electrical Life Expectancy | 100,000 Operations | - |
| Mechanical Life Expectancy | 10,000,000 Operations | - |
| Utilization Category | AC-15, Capacity for loads > 72 VA | IEC 60947-5-1 |

### D) Range Setting, Measuring

According to Voltage Model (208/480 VAC):

| Parameter | 208 VAC | 480 VAC | Accuracy |
|-----------|---------|---------|----------|
| Voltage Measurement Range, Um | 0-312 | 0-672 | +/- 2% VAC |

According to Current Model (04/12/32/80/EXT(CT15) A):

| Parameter | 04 | 12 | 32 | 80 | EXT(CT15) | Unit |
|-----------|----|----|----|----|-----------|------|
| Current Measurement Range, Im | 1.5-40 | 03-125 | 1-320 | 25-800 | 5%-383%CT | A |

### Another Measured Parameters

| Parameter | Range | Accuracy |
|-----------|-------|----------|
| Frequency Range | 45.0-70.0 Hz | 1% |
| Instantaneous Power Factor | 0.00-1.00 | 8% |
| Instantaneous Reactive Power KVA | 0.0-999.9 KVA | 4% |
| Instantaneous Real Power KW | 0.0-999.9 KW | 4% |
| Energy KWH | 0-999999 KW/H | 4% |
| Total Motor Running Time (hours) | 0-999999 H | 1% |

### E) Algorithms and Protection Functions

According to Operation Voltage (208/480 VAC):

| Function | Setting | Notes |
|----------|---------|-------|
| Undervoltage (UV) @ Imotor=0 or OL | 165-225 / 350-460 VAC | Settings |
| Overvoltage (OV) @ Imotor=0 or OL | 215-270 / 460-580 VAC | Settings |
| Voltage Hysteresis Threshold | 6-12 VAC | - |
| Voltage Unbalance Detection (VUB) | 2%-10% | Level settings |
| Single Phasing (VSP) | IN VUB > 33%, OUT VUB < 28% | - |
| Rated Frequency | 50/60 Hz | Level settings |
| Tolerance for Frequency Shift (FS) | +/-2% to +/-10% | Level settings |
| Phase Reversal (PR) | Normal: A>B>C, Reversed: C>B>A | - |
| Trip Delay because of Phase Reversal | < 1 sec | - |
| Trip Delay because of Other Voltage Failures (TD) | 1-30 sec | Settings |
| Start Up Delay (TC) Delay | 0-600 sec | Level settings |
| Trip Delay because of VSP | 3 sec | - |
| User Start Mode | Auto/Manual selection | - |
| Minimum Time Between Two Start Up | 50 x Thermal Class Sec | - |

According to Operation Current (04/12/32/80/EXT(CT15) A):

| Function | Setting | Notes |
|----------|---------|-------|
| Nominal Current Setting | 1.5-40 / 03-125 / 1-320 / 25-800 / 25%-93 CT | A |
| Overload Level Setting (OL) | 5%-50% Inom | Level settings |
| Thermal Class Setting | - | Level settings |
| Dynamic Setting of Motor Model (Cold Curve/Hot Curve) | Thermal class varies from 1->1/8 of adjusted class according to start up time and motor load level | IEC 60255-8, IEEE Std 242 C37.112 |
| Maximum Time Between Cold/Hot Curve | 2 Hours (from 1 to 1/3 or from 1/3 to 1) | - |
| Trip Delay because of Overload | According to Overload Level and Adjusted Class | IEEE Std 242 C37.112 |
| Heat Threshold because of Overload Failure | 100% | - |
| Current Unbalance (CUB) | CUB > 48% | - |
| Current Stall Phase (CSP) | CUB > 60% | - |
| Accelerated Locked Rotor Detection (LR) | YES/NO User selection, 100% Heat setting | - |
| Trip delay because of CSP | 1 Sec | - |
| Trip Delay because of CUB | 2 Sec | - |
| High-Inertia Load Option | YES/NO | - |
| High-Inertia Load Heat Threshold | 400% | - |
| High-Inertia Load Start up Delay | 20-120 Sec | Level settings |
| Thermal Machine Cooling Time | 50 x Thermal Class Sec | - |
| Undercurrent | YES/NO | - |
| Undercurrent Disconnection Type (UC) | %Inom / Power Factor (PF) | - |
| Undercurrent Adjusting (%Inom) | 30%-90% Inom | Level settings |
| Undercurrent Adjusting (PF) | 0.3-0.9 | Level settings |
| Trip Delay because of UC | 5-600 Sec | Level settings |
| Start Up Delay because of UC | 2-500 Min | Level settings |
| Third Failure Detection | YES/NO | Level settings |
| Permanent disconnection duration because of Third Failure | 3 Current failures in less than 105 min | IEEE Std 242 C37.112 |
| Trip delay because of accelerated locked rotor | 3 Sec | - |
| Real Time Clock | hh:mm_mm/dd/yy | UMT |
| Load Control by Events (schedule) | YES/NO | User selection |

### F) Communications and Other Special Functions

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Communication Protocol | MODBUS RTU @ 9600 8N1 | See User Manual |
| Communication Ports | Port GIO PORT (*) | See User Manual |
| Address Range | 1-127 | - |
| History Buffer Memory | 20 last faults report (failure type, value, date, hour and time elapsed) | See User Manual |
| Parameters Block | 0000 Free, 0001-9999 Blocked | User selection |

(*) GIO Plug is required for GIO Port communication. It is available separately.

### G) Immunity and Emissions, Electromagnetic Interference (EMC)

For Heavy Industrial Environment (B):

| Test | Standard |
|------|----------|
| Immunity to Radio Frequency Test | EC 61000-4-3 |
| Electrical Fast Transients | EC 61000-4-4 |
| Surge Immunity Test | EC 61000-4-5 |
| Radio-Frequency Continuous Conducted | EC 61000-4-6 |
| Power Frequency Magnetic Field | EC 61000-4-8 |
| Voltage Dips, Short Interruptions and Voltage Variations | EC 61000-4-11 |
| Harmonics and Interharmonics | EC 61000-4-13 |
| Voltage Fluctuation Immunity | EC 61000-4-14 |
| Unbalance Immunity Test | EC 61000-4-27 |
| Variation of Power Frequency | EC 61000-4-28 |

## Tripping Cold Curve

The device includes thermal protection according to IEC 60255-8 and IEEE C37.112 standards with the following thermal classes:

- Class 5
- Class 10
- Class 15
- Class 20
- Class 25
- Class 30

Hot Curve = Cold Curve / 3

where I nom = Current value on GUCT adjusted previously by the user.

---

**NOTE:** Technical data are valid at the time of printing. We reserve the right to subsequent alterations.

Manufactured and designed by Genteca, Generación de Tecnología C.A., R.I.F: J-00223173-4, Av. El Buen Pastor, cruce con Calle Vargas, Edificio Alba, Piso 1, Local 1-A, Boleita Norte, Caracas, 1070, República Bolivariana de Venezuela. Phone: +58-212-237.0711 (Master), Fax: +58-212-235.2497, E-mail: genteven@genteca.com.ve, Website: www.genteca.com.ve. Distributed in USA by Miami Breaker INC. 7060 Nw. 52nd Street. Miami-Florida 33166, USA. Phone: +1-786-3365780.
