---
title: "GENIUS GI Motor Protection Relay - Specification Sheet"
type: Technical
source: "HOJA DE ESPECIFICACION GI.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "GI"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GENIUS GI Motor Protection Relay

## Overview

GENIUS GI is a microcontrolled three-phase voltage relay specifically designed to protect electric loads and distribution power systems from failure and damage due to common voltage faults.

GENIUS GI constantly supervises line voltages values; when any harmful condition occurs, the output is deactivated until the fault disappears and power line conditions return to an acceptable level. Start Up and Trip Delay are incorporated to prevent nuisance tripping due to rapid power fluctuations.

The device provides four setting knobs for adjustments to select maximum and minimum allowed voltage, trip delay (TD), and start up delay (TC). Indicator lights (LED's) indicate output status. One Start push-button and one selectable Start Mode Slide-Switch are included, along with a Communication Port featuring MODBUS RTU protocol.

An innovative mechanical design allows two placement options: DIN-Rail mounting or Flat Surface mounting using an exclusive attachable mounting ear.

## Features

### Measurement Functions
- Voltage measurement
- Overvoltage/Undervoltage detection
- Voltage Unbalance detection
- Single Phasing detection
- Phase Reversal detection

### Protection Against
- Overvoltage
- Undervoltage
- Voltage Unbalance
- Single Phasing
- Phase Reversal

### Adjustable Parameters
- Overvoltage Threshold
- Undervoltage Threshold
- Trip Delay (TD)
- Start Up Delay (TC) after Voltage Fault Recovery

### Reports (via Communications)
- Voltage report
- Adjustment Values report
- Start Mode report
- 20 Last Fault report
- Power Frequency report

### Physical Features
- DIN-Rail or Flat Surface mounting options
- Four setting knobs for protection parameter adjustments
- Four indicator lights (LED's) for output status and fault indication
- AUTO/MANUAL Start Mode Slide-Switch
- Enclosure material: UL94V0

### Communications
- GIO Port (MODBUS RTU protocol on RS485 @ 9600 baud output)
- Remote On/Off capability

## Product Standards Applied

**European Standards (CE):**
- IEC 61010-1
- IEC 60255-6
- IEC 60947-1

**US Standards:**
- UL 508

## General Functions & Range of Applications

- **Overvoltage detection:** +5% up to +30% Rated Voltage
- **Undervoltage detection:** -30% up to -5% Rated Voltage
- **Voltage Unbalance detection:** IN +/-8%, OUT +/-6% Rated Voltage
- **Single Phasing detection:** IN VUB>33%, OUT VUB<28%
- **Trip Delay because of Single Phasing:** <1 sec
- **Start Up Delay after Voltage Fault Recovery:** adjustable 5 to 300 sec
- **Trip Delay because of Voltage Fault:** adjustable 0.5 to 5 sec

## Physical Features & Safety Information

### Dimensions and Weight
- Length: 105 mm
- Width: 90 mm
- Height: 68 mm
- Weight: 215 g (0.47 lb)

### Mounting
- Symmetrical DIN Rail (IEC 715, DIN 43880)
- Flat surface mounting with screw 3/16" x 1/2"

### Installation Requirements
- For terminal connection: use screwdriver suitable for M3 screws
- For flat surface mounting: use screwdriver suitable for screws (3/16" x 1/2")
- Voltmeter required
- Tightening Screw Torque: 5.06 Kgf-cm / 4.4 lb-in
- Wiring: >10 AWG (4 mm²) <18 AWG

### Safety Attention
Only qualified technicians with knowledge about voltage protection relays and associated connections should perform installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

### EMC Measures
This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances, in which case the user may be required to take adequate mitigation measures.

## Technical Specifications

### A) Power Supply Circuit
| Parameter | Specification |
|-----------|---------------|
| Rated Voltage, Ue | 120 / (208/220) / 380 / (440/480) VAC |
| Voltage Operation Limits, Ue | 72-168 / 124-308 / 228-532 / 264-672 VAC |
| Average Consumption, In | 44 mA |
| Frequency Operation Limits, Fn | 42-70 Hz / 50/60 Hz |
| Rated Duty | Uninterrupted Duty |

### B) Application Data, Environmental Conditions, Operation Limits and Installing

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| Designed according to European Standards | IEC 61010-1, IEC 60255-6, IEC 60947-1 (LVD & EMC) | — |
| Designed according to US Standards | UL 508 | — |
| CE Marking | CE (pending) | IEC 60947-1 |
| Ambient Air Temperature (Operation) | -5 °C to 55 °C (23 °F to 131 °F) | — |
| Ambient Air Temperature (Storage) | -10 °C to +70 °C (14 °F to 158 °F) | — |
| Maximum Relative Humidity | 85% R.H. | — |
| Vibrations | Class 1, Amplitude <0.035 mm or 1G, 10 Hz <f< 150 Hz | IEC 60255-21-1 |
| Shocks | Class 1, <15G, 16 ms | IEC 60255-21-2 |
| Seismic | Class 1, Amplitude <3.5 mm or 1G, 1 Hz <f< 35 Hz | IEC 60255-21-3 |
| Degree of Protection | IP20, Protected against objects >12.5 mm, but no protection against water | IEC 60529 |
| Pollution Degree | Degree 3 | IEC 60255-5 |
| Overvoltage Category | Category III, 4 KV | IEC 60255-5 |
| Rated Insulation Voltage | 500 V UL/IEC | IEC 60255-5 |
| Impulse Voltage Test | 5 KV | IEC 60255-5 |
| Impulse Dielectric Test | 2 KV 50/60 Hz @ 1 min | UL 508 |
| Flammability Rating of Enclosure | VO | UL-94 |
| Enclosure Material | Polymers: LEXAN 500R, ABS, Nylon | — |
| Mounting Position | Any Position | — |

### C) Control Characteristics

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| Output Contact Rating | 3 A @ 240 VAC, 1.5 A @ 480 VAC (Pilot Duty) | UL 508 Section 139.1 |
| Electrical Life Expectancy | 100,000 Operations | — |
| Mechanical Life Expectancy | 10,000,000 Operations | — |
| Utilization Category | AC-15, Capacity for loads > 72 VA | IEC 60947-5-1 |

### D) Range Setting, Measuring

| Parameter | 120 VAC | 208/220 VAC | 380 VAC | 440/480 VAC |
|-----------|---------|-------------|---------|------------|
| Voltage Measurement Range, Um | 80-155 | 145-285 | 260-500 | 300-625 |
| Frequency Measurement | +/- 2% Hz | +/- 2% Hz | +/- 2% Hz | +/- 2% Hz |

### E) Algorithms and Protection Functions

| Parameter | 120 VAC | 208/220 VAC | 380 VAC | 440/480 VAC | Unit |
|-----------|---------|-------------|---------|------------|------|
| Undervoltage (UV) Settings | 80-115 | 145-200 | 260-370 | 300-420 | Level |
| Overvoltage (OV) Settings | 120-155 | 230-285 | 390-500 | 500-625 | Level |
| Voltage Hysteresis Threshold | 3 | 6 | 10 | 12 | VAC |

| Function | Specification |
|----------|---------------|
| Voltage Unbalance Detection (VUB) | IN +/-8%, OUT +/-6% |
| Single Phasing (VSP) | IN VUB >33%, OUT VUB <28% |
| Phase Reversal (PR) | Normal Sequence ABC, reversal sequence CBA |
| Trip Delay because of Phase Reversal | <1 sec |
| Trip Delay because of another Voltage Failures (TD) | 0.5-5 sec (adjustable) |
| Start up Delay (TC) | 5-300 sec (adjustable) |
| Start Mode | Auto/Manual Switch selection |

### F) Communications and Other Special Functions

| Parameter | Specification |
|-----------|---------------|
| Communication Protocol | MODBUS RTU 9600 8N1 |
| Communication Ports | GIO PORT (*) |
| History Buffer Memory | 20 last fault report |

(*) GIO Plug is required for GIO Port communication. It is available separately.

### G) Immunity and Emissions, Electromagnetic Compatibility (EMC) for Heavy Industrial Environment (B)

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| Electrostatic Discharge | Level 3, contact 6 kV, air 8 kV | IEC 61000-4-2 |
| Immunity to Radio Frequency Test | Level 3, 10 V/m, 80-1000 MHz, 80% AM | IEC 61000-4-3 |
| Electrical Fast Transients | Level 4, 4.4 kV in source, 2 kV in I/O | IEC 61000-4-4 |
| Surge Immunity Test | Level X, 6 kV | IEC 61000-4-5 |
| Radio-Frequency Continuous Conducted | Level 3, 10 Vrms, 150 kHz > 80 MHz, 80% AM | IEC 61000-4-6 |
| Power Frequency Magnetic Field | Level 4, 30 A/m | IEC 61000-4-8 |
| Voltage Dips, Short Interruptions and Voltage Variations | Reduction 100%, 80-120 ms | IEC 61000-4-11 |
| Harmonics and Interharmonics Immunity Tests | Class 3, up to 12% of Harmonics | IEC 61000-4-13 |
| Voltage Fluctuation Immunity | Class 3, up to 12% of variation | IEC 61000-4-14 |
| Unbalance Immunity Test | Class 3, up to 25% of VUB | IEC 61000-4-27 |
| Variation of Power Frequency | Level 4, up to +/-15% of Fnom | IEC 61000-4-28 |
| Electrical (Burst) Disturbance Test | Class 3, 2.5 kV CM, 1 kV DM | IEC 60255-22-1 |
| Conducted Common Mode Disturbances (0>150 kHz) | Level 3, 10 Vrms / Class B, 300 Vrms CM, 100 Vrms DM | IEC 61000-4-16 / IEC 60255-22-7 |
| Electromagnetic Disturbance Characteristics | Class A, Group 1, 150 kHz-30 MHz, <60 dB (µV) | CISPR 11 |
| — | Class A, Group 1, 30 MHz-1000 MHz, <40 dB (µV) | CISPR 11 |
| Limits for Harmonic Current Emissions | Class A | IEC 61000-3-2 Table 1 |
| Limitation of Voltage Fluctuations and Flicker in Low-Voltage Supply Systems | Induced Variation <4% | IEC 61000-3-3 |

## How to Order

**Model Code Format:** GI-[VOLTAGE]-[LANGUAGE]

### Voltage Options
- 120 — 120 VAC
- 208 — 208/220 VAC
- 380 — 380 VAC
- 480 — 440/480 VAC

### Language Options
- S — Spanish
- E — English
- P — Portuguese

**Example:** GI-120-E (GENIUS GI, 120 VAC, English)

## Basic Wiring

Connection terminals:
- 1 = Live (L1)
- 2 = Neutral (N)
- 3 = Phase 2 (L2)
- 6-7 = Output contacts (open/closed for normal/tripped states)
- 7-8 = Output contacts (connected for normal, open for tripped)

For GIO Port serial communication, use GIO-Plug (optional, available separately).

Refer to user manual for further details about wiring diagrams for additional applications.
