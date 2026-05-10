```markdown
---
title: "Relayne GOCT Motor Protection Relay"
type: Technical
source: "GOC-V1.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "GOCT"
date_processed: "2026-05-09"
---

# Relayne GOCT Motor Protection Relay

## Features

The Relayne GOCT is a microcontrolled based three-phase Motor Protection Relay, specifically designed to protect electric motors from failure and damage due to common current and voltage faults.

### Measurement of:
- Current
- Voltage

### Protection against:
- Overload
- Overvoltage / Undervoltage
- Voltage Unbalance
- Current Unbalance
- Single Phasing
- Current and Reverse Current

### Adjustments of:
- Overload
- Start Up Delay after Voltage Fault Recovery
- Start Mode AUTO/MANUAL

When any harmful condition occurs, the output is deactivated until the fault disappears and the motor has been totally cooled.

## Physical Features

- DIN-Rail or Flat Surface mounting
- Two (2) setting knobs for Protection Parameter adjustment
- Four (4) indicator lights (LEDs) for output status and faults indication
- One Start push-button and one selectable Auto/Manual Start Mode Slide-Switch
- Communication Port with MODBUS RTU protocol
- Enclosure material UL94V0
- Innovative mechanical design allows two (2) placement options:
  - Symmetrical DIN-Rail mounting
  - Flat Surface mounting, using an exclusive attachable mounting ear

## Communications

- GIO Port (MODBUS RTU protocol 9600 baud output, 8N1)
- Remote On/Off
- Thermal Memory

## Reports

- Voltage & Current report
- Adjustment Values report
- Start Mode report
- 20 Last Fault report
- Power Frequency report

## Product Standards Applied

Designed according to CE Standards (LVD and EMC):
- IEC 61010-1
- IEC 60255-6
- IEC 60255-8
- IEC 60947-1
- IEEE C37.112
- Listed by Underwriters Laboratories Inc. E300908

## General Functions & Range of Applications

The Relayne GOCT provides electrical protection through general functions and setting ranges listed as follows:

- **Overload detection**: According to product model
- **Overvoltage detection**: See Technical Specifications Section E
- **Undervoltage detection**: See Technical Specifications Section E
- **Start Up Delay (TC) after Voltage Fault Recovery**: adjustable 5 to 300 sec
- **Voltage Unbalance detection**: IN +/-8%, OUT +/- 6% Rated Voltage
- **Single Phasing detection**: IN VUB>33%, OUT VUB<28%
- **Current Unbalance detection**: CUB > 48%
- **Current Single Phasing detection**: CUB>60%
- **Thermal Class IEC 60255-8**: Cold Curve: 10, Hot Curve: 3

## Physical Specifications

### Dimensions
- Height: 92 mm
- Width: 91 mm
- Depth: 96 mm
- Front protrusion: 90 mm
- Weight: 398 g (0.87 lb)

### Features
- Current Sensing Holes for Motor Wiring
- Attachable Mounting Ear
- Indicator Lights
- Start Push Button
- Auto/Manual Start Mode Slide-Switch
- Back Groove for DIN Rail Mounting
- GIO Port
- Start Up Delay (TC) Setting Knob
- Current Setting Knob (FLA)

## Installation

**Power Supply Connection**: Power supply wires must pass through GOCT holes before connecting to 3-phase Motor.

**GIO Port**: Use GIO PLUG (Optional) for serial communication with other devices.

### Special Tools for Installation or Connection
- For terminal connection use screwdriver suitable for M3 screws
- For flat surface mounting use screwdriver suitable for screws (3/16" x 1/2")
- Ammeter

## Safety Information

**ATTENTION**: Only qualified technicians with knowledge about overload protection relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

### EMC Measures
This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

## How to Order Relayne GOCT

Order code format: GOC-[Number of Phases]-[Voltage]-[Amperage]-[Language]

**Number of Phases**:
- T = 3 Phases

**Voltage**:
- 208 = 208/220 VAC
- 480 = 440/480 VAC

**Amperage**:
- 04 = 1-4 A
- 12 = 3.5-12.5 A
- 32 = 10-32 A
- 80 = 25-80 A

**Language**:
- S = Spanish
- E = English
- P = Portuguese

## Technical Specifications

### A) Power Supply Circuit
- **a.1 Rated Voltage, Ue**: 208/220 VAC or 440/480 VAC (according to voltage model)
- **a.2 Voltage Operation Limits, Ue**: 124-300 VAC (208V model) / 264-672 VAC (480V model)
- **a.3 Average Consumption, In**: 38 mA
- **a.4 Normal Frequency**: 50/60 Hz
- **a.5 Frequency Operation Limit**: 42-70 Hz

### E) Algorithms and Protection Functions
- **e.1 Undervoltage (UV) @ Imotor=0 or OL**: 187 VAC (208V model) / 396 VAC (480V model)
- **e.2 Overvoltage (OV) @ Imotor=0 or OL**: 254 VAC (208V model) / 528 VAC (480V model)
- **e.3 Voltage Hysteresis Threshold**: 6 VAC (208V model) / 12 VAC (480V model)
```