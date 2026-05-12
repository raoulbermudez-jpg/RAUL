---
title: "Motor Protection Relay GOC - Specification Sheet"
type: Technical
source: "HOJA DE ESPECIFICACION GOC.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "GOC"
version_status: "historica"
date_processed: "2026-05-10"
---

# Motor Protection Relay GOC

Relayne GOC is a microcontrolled based three-phase Motor Protection Relay, specifically designed to protect electric motors from failure and damage due to common current and voltage faults.

Relayne GOC constantly supervises the motor current and line voltage. When any harmful condition occurs, the output is deactivated until the fault disappears and the motor has been totally cooled.

Relayne GOC provides two (2) setting knobs in order to select the maximum allowed current (FLA) and the start up delay (TC) once the voltage fault disappears. It also provides indicator lights (LEDs) for faults and output status. One Start push-button and one selectable Auto/Manual Start Mode Slide-Switch are included as well as a Communication Port with MODBUS RTU protocol.

An innovative mechanical design allows two (2) placement options:
- Symmetrical DIN-Rail mounting
- Flat Surface mounting, using an exclusive attachable mounting ear

Relayne GOC has been developed using the most advanced technology and designed in accordance with the IEEE, IEC and NEMA protection standards; and developed in compliance with IEC electromagnetic compatibility standards, working safely under hardest electrical environments.

## Features

**Measurement of:**
- Current
- Voltage

**Adjustments of:**
- Overload
- Start Up Delay after Voltage Fault Recovery
- Start Mode AUTO/MANUAL

**Communications:**
- GIO Port (MODBUS RTU protocol on RS485@9600 baud output)

**Protection against:**
- Overload
- Overvoltage / Undervoltage
- Voltage Unbalance
- Current Unbalance
- Single Phasing
- Phase Reversal

**Physical features:**
- DIN-Rail or Flat Surface mounting
- Two (2) setting knobs for Protection Parameter adjustment
- Four (4) indicator lights (LED's) for output status and faults indication
- Remote On/Off
- AUTO/MANUAL Start Mode Slide-Switch
- Enclosure material UL94V0

**Reports:**
- Voltage & Current report
- Adjustment Values report
- Start Mode report
- 20 Last Fault report
- Power Frequency report

**Others:**
- Thermal Memory

## Product Standards Applied

Designed according to CE Standards (LVD and EMC):
- IEC 61010-1
- IEC 60255-6
- IEC 60255-8
- IEC 60947-1

Designed according to:
- UL 508
- IEEE C37.112

## General Functions & Range of Applications (Intended USE)

The Relayne GOC provides electrical protection through general functions and setting ranges listed as follows:

- **Overload detection:** According to product model
- **Overvoltage detection:** See Technical Specifications (Section E)
- **Undervoltage detection:** See Technical Specifications (Section E)
- **Start Up Delay (TC) after Voltage Fault Recovery:** Adjustable 5 to 300 sec
- **Voltage Unbalance detection:** IN +/-8%, OUT +/- 6% Rated Voltage
- **Single Phasing detection:** IN VUB>33%, OUT VUB<28%
- **Current Unbalance detection:** CUB > 48%
- **Current Single Phasing detection:** CUB>60%
- **Thermal Class IEC 60255-8:** Cold Curve: 10, Hot Curve: 3

## Physical Features and Safety Information

### Physical Features

The GOC unit includes:
- Current sensing holes for motor wiring
- Attachable mounting ear for flat surface installation
- Indicator lights for status and fault indication
- Start push button
- Auto/Manual start mode slide-switch
- Back groove for DIN rail mounting
- GIO port for communications
- Basic wiring label
- Start up current setting knob (FLA)
- Start up delay setting knob

### Safety Information

**ATTENTION:**
Only qualified technicians with knowledge about overload protection relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

### Measures to Be Taken Into Consideration with Regards EMC

**NOTICE:**
This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

## Installation

### Connection Diagram

From line Power Supply (3- 50/60 Hz starter circuits) wires must pass through GOC holes before connecting to Motor.

The connection includes:
- L1, L2, L3 power supply connections
- Start push button connection
- Auto/Manual start mode selection
- GIO Port for serial communication

**Output Contact Status:**
- Tripped: 95-96 connected, 97-98 open
- Normal: 95-96 open, 97-98 connected

### Dimensions and Weight

- Dimensions: 92 x 91 x 96 mm (L x W x H)
- Weight: 398 g (0.87 lb)

### Special Tools for Installation or Connection

- For terminal connection use screwdriver suitable for M3 screws
- For flat surface mounting use screwdriver suitable for screws (3/16" x 1/2")
- Ammeter

## How to Order Relayne GOC According to Customer Needs

**Voltage Models:**
- 208 — 208/220 VAC
- 480 — 440/480 VAC

**Amperage Models:**
- 04 — 1-4 A
- 12 — 3.5-12.5 A
- 32 — 10-32 A
- 80 — 25-80 A

**Phases:**
- T — 3 PHASES

**Language:**
- S — SPANISH
- E — ENGLISH
- P — PORTUGUESE

## Technical Specifications

### A) Power Supply Circuit

| Parameter | Value |
|-----------|-------|
| Rated Voltage, Ue | 208/220 or 440/480 VAC (According to Voltage Model) |
| Voltage Operation Limits, Ue | 124-300 or 264-672 VAC |
| Average Consumption, In | 38 mA |
| Frequency Operation Limits, Fn | 42-70 Hz |
| Rated Duty | Uninterrupted Duty |

### B) Application Data, Environmental Conditions, Operation Limits and Installing

| Parameter | Value | Standard |
|-----------|-------|----------|
| Designed according to IEC Standards | IEC61010-1, IEC60255-6, IEC60947-1 | European Standards |
| Designed according to US Standards | UL (pending), NEMA, Auxiliary Devices UL508 | UL 508 |
| CE Marking | CE (pending), Low Voltage Devices | IEC60947-1 |
| Ambient Air Temperature (Operation) | -5 °C to 55 °C (23 °F to 131 °F) | |
| Ambient Air Temperature (Storage) | -10 °C to +70 °C (14 °F to 158 °F) | |
| Maximum Relative Humidity | 85% RH | |
| Vibrations | Class 1, Amplitude <0.035mm or 1G, 10Hz < f < 150Hz | IEC 60255-21-1 |
| Degree of Protection | IP20, Protected against objects > 12.5mm | IEC 60529 |
| Pollution Degree | Degree 3 | IEC 60255-5 |
| Overvoltage Category | Category III | IEC 60255-5 |
| Rated Insulation Voltage | 500V | According to UL |
| Impulse Voltage Test | 5 KV | IEC 60255-5 |
| Dielectric Voltage-Withstand Test | 2.5 KV 50/60 Hz @ 1min | UL 508 |
| Flammability Rating of Enclosure | UL-94 V0 | |
| Enclosure Material | Polymers: LEXAN 500R, ABS, Nylon | |
| Mounting Position | Any Position | IEC 715 |
| Mounting Features | Symmetrical DIN Rail, Flat surface mounting | DIN 43880, NEMA Style |
| Terminals | Screw Type Flat M3 | |
| Tightening Screw Torque | 5.1 kgf-cm / 4.4 lb-in | |
| Current Sensing Holes for Motor Wiring | <11mm, AWG 4 to 18 AWG (>10 AWG / 4mm²) | |
| Dimensions | 92 x 91 x 96 mm (L x W x H) | |
| Weight | 398 g (0.87 lb) | |

### C) Control Characteristics

| Parameter | Value | Standard |
|-----------|-------|----------|
| Auxiliary Relay Contact Rating | Pilot Duty | Section 139.1 B300 UL 508 |
| Electrical Life Expectancy | 100,000 Operations | |
| Mechanical Life Expectancy | 10,000,000 Operations | |
| Utilization Category | AC-15, Capacity for loads > 72 VA | IEC60947-5-1 |

### D) Range Setting, Measuring

**Voltage Measurement Range, Um (According to Voltage Model):**
- 208 VAC: 145-285 VAC
- 480 VAC: 300-625 VAC

**Current Range (According to Current Model):**
- 1-4 A
- 3.5-12.5 A
- 10-32 A
- 25-80 A

**Frequency Measurement (Parameter available only through GIO Port):**
- Accuracy: ± 2%

### E) Algorithms and Protection Functions

| Parameter | Specification |
|-----------|---------------|
| Undervoltage (UV) @ Imotor=0 or OL | 208 VAC: 187 VAC / 480 VAC: 396 VAC |
| Overvoltage (OV) @ Imotor=0 or OL | 208 VAC: 254 VAC / 480 VAC: 528 VAC |
| Voltage Hysteresis Threshold | 0-1 VAC (Level settings) |
| Current Range | 1-4, 3.5-12.5, 10-32, 25-80 A (settings) |
| Voltage Unbalance Detection (VUB) | IN +/-8%, OUT +/-6% |
| Single Phasing (VSP) | IN VUB > 33%, OUT VUB < 28% |
| Phase Reversal (PR) | Normal Sequence ABC, reversal sequence CBA |
| Current Unbalance (CUB) | CUB > 48% |
| Current Single Phasing (CSP) | CUB > 60% |
| Thermal Class | Cold Curve: 10, Hot Curve: 3 (According to IEC 60255-8-1990) |
| Trip Delay because of Overload (OL) | According to Overload Level (Inverse Time Current) (IEC 60255-8-1990) |
| Trip Delay because of 3 Current Failures | <1 sec (in less than 30 min) |
| Trip Delay because of Phase Reversal | 3 sec |
| Trip Delay because of Another Voltage Failures | Adjustable |
| Start Up Aberrant Cooling Level | 480 sec |
| Start Up Delay (TC) | 5 — 300 sec settings |
| Start Mode | Auto/Manual Switch selection |

### F) Communications and Other Special Functions

| Parameter | Specification |
|-----------|---------------|
| Communication Protocol | MODBUS RTU @9600 8N1 |
| Communication Ports | GIO PORT (*) |
| History Buffer Memory | 20 last fault report |

(*) GIO Plug is required for GIO Port communication. It is available by separated.

### G) Immunity and Emissions, Electromagnetic Compatibility (EMC) for Heavy Industrial Environment (B)

| Parameter | Level | Standard |
|-----------|-------|----------|
| Electrostatic Discharge | Level 3, contact 6 kV, air 8 kV | IEC 61000-4-2 |
| Immunity to Radio Frequency Test | Level 3, 10 V/m 80→1000MHz, 80% AM | IEC 61000-4-3 |
| Electrical Fast Transients | Level X, 4.4 kV in source, 2kV in I/O | IEC 61000-4-4 |
| Surge Immunity Test | Level X, 6kV | IEC 61000-4-5 |
| Radio-Frequency Continuous Conducted | Level 3, 10 Vrms, 150 kHz → 80MHz 80% AM | IEC 61000-4-6 |
| Power Frequency Magnetic Field | Level 4, 30 A/m | IEC 61000-4-8 |
| Voltage Dips, Short Interruptions and Voltage Variations | Reduction 100%, 120 → 150ms | IEC 61000-1 |
| Harmonics | Class 3, up to 12% of Harmonics | IEC 61000-4-13 |
| Voltage Fluctuation Immunity | Class 3, up to 12% of variation | IEC 61000-4-14 |
| Unbalance Immunity Test | Class 3, up to 25% of VUB | IEC 61000-1-1 |
| Variation of Power Frequency | Level 3, up to +4% -6% of Fnom | IEC 61000-1-1 |

## GOC Cold-Hot Curves

The cold-hot curves graph shows the tripping time (in seconds) versus the I load / I nom ratio, with separate curves for Cold Curve (10) and Hot Curve (3).

(*) Inom = Current value on GOC adjusted previously by the user. Inom term is referred to FLA (Full Load Amperage) adjustable on the product.

---

**Note:** Technical data are valid at the time of printing. We reserve the right to subsequent alterations.
