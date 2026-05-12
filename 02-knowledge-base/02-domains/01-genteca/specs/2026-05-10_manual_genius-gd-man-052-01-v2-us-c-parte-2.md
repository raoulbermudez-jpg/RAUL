---
title: "GIII+ Manual de Instalación - Ajustes de Parámetros y Especificaciones Técnicas"
type: Technical
source: "GD-MAN-052-01-V2-US-C.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GIII+"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GIII+ Manual de Instalación - Ajustes de Parámetros y Especificaciones Técnicas

## 9.1 GIII Recommended Values for adjustable parameters

### Undervoltage (UV) and Overvoltage (OV)

Manufacturers usually offer motors with limited range of operation voltage inside of ±10% of nominal value.

**Example:** a protector installed for a motor of 220V should be adjusted in:
- UV = 220 × 90% = 198V (Undervoltage)
- OV = 220 × 110% = 242V (Overvoltage)

### Voltage Unbalance

According to NEMA MGI standard, it is recommended that motors operate with an unbalance voltage less than 5%.

### Overload (OL)

The recommended value for the protection against the overload is inside the range of 110% to 120% of nominal current (In) or the current specified in the motor nameplate at maximum charge (FLA).

- IN = FLA motor nameplate
- OL = Service factor motor nameplate

### Underload by current (%In)

When chosen to protect against charge loss through current monitoring, a value by default of 80% of the current at maximum charge (FLA) specified by the manufacturer is recommended.

### Underload by Power Factor (PF)

- Applicable to motors over dimensioned that requires protection against charge loss during startup.
- Example: submergible pumps of gas stations, etc.
- When chosen to protect against charge loss through monitoring the power factor (PF), the GIII comes adjusted from factory with 0.5. (Although the protection can be adjusted in a range of 0.1 to 0.9 FP, adjustment above 0.3 FP is recommended).

### Selection of the Thermal class of the motor

| Class | Description |
|-------|-------------|
| Class 5 | Little motors with fast acceleration, that requires faster detection of overload failure. |
| Class 10 (Fast) | Motors used in compressor, refrigeration equipment, submergible pumps and motors of general purpose usually classified under standard IEC, that reach continual operation speed in less than 4 seconds. |
| Class 15 | Motors for specialized applications. |
| Class 20 (standard) | Motors of general purpose qualified under NEMA standard. |
| Class 30 (slow) | Motors for charge of high inertia (times that exceed 10 seconds). |

## 9.2 GIII+ Schedule Timer Adjustment Guide

Only GIII+ models (ordered with "+") include "CLOCK ADJUSTMENTS" and "SCHEDULE TIMER" options.

### EVENT 01 (example):
From Tuesday to Saturday and Holiday HOLIDAY 01

- ON: 7:30 hrs
- OFF: 16:45 hrs
- June 24th

The adjustment guide provides detailed screen-by-screen navigation instructions for setting events and holidays, including day selection (Monday through Sunday), time configuration, and event numbering.

## 10. GIII DISMOUNTING INSTRUCTIONS

### WARNING
Disconnect power supply (Circuit Breaker OFF) and electrical wiring before dismounting GIII. Electrical shock will result in death or serious injury.

### 10.1.1 DIN RAIL DISMOUNTING WITHOUT CT BOX

a) Handling a flat screwdriver, pull downward the mounting bracket that can be seen at rear and down side of GIII as shown in figure.

b) With screwdriver position (2) pull out GIII from DIN Rail.

**Recommendation:** Pull downward 2 mm with a soft movement when using screwdriver for dismounting. Strong movement could break the supporting bracket.

### 10.1.2 DIN RAIL DISMOUNTING WITH CT BOX

a) Handling a flat screwdriver, pull downward the mounting bracket that can be seen at rear and down side of GIII as shown in figure.

b) With screwdriver position (2) pull out GIII from DIN Rail as shown in figure.

### 10.2.1 FLAT SURFACE DISMOUNTING WITHOUT CT BOX

a) Unscrew both screws fixed on flat surface through attachable mounting ears and then pull out GIII relay from flat surface as shown in figure.

### 10.2.2 FLAT SURFACE DISMOUNTING WITH CT BOX

a) Unscrew both screws fixed on flat surface through attachable mounting ears and then pull out GIII relay from flat surface as shown in figure.

## 11. GIII Technical Specifications

### A) Power Supply Circuit

| Parameter | Values | Unit |
|-----------|--------|------|
| Rated Voltage, Ue PT | 120/208/220/240/400/440/480 | VAC |
| Voltage Operation Limits, Ue/72 | >168/145>312/228>532/264>672 | VAC |
| Average Consumption, In | 38 | mA |
| Frequency Operation Limits, Fn | 42—70 Hz; 50/60 Hz | Hz |
| Rated Duty | Uninterrupted Duty | — |

### B) Application Data, Environmental Conditions, Operation Limits and Installing

| Parameter | Value | Standard |
|-----------|-------|----------|
| Designed according to European Standards | IEC61010-1, IEC60255-6, IEC60947-1 | LVD & EMC |
| Aux. Device NKCR Certified | USA | UL Listing |
| Aux. Device NKCR7 Certified | Canada | £90008 |
| CE Marking | CE (pending), Low Voltage Devices | IEC60947-1 |
| Ambient Air Temperature (Operation) | -5 °C to 55 °C (23 °F to 131 °F) | — |
| Ambient Air Temperature (Storage) | -10 °C to +70 °C (14 °F to 158 °F) | — |
| Maximum Relative Humidity | 85% R.H. | — |
| Vibrations | Class 1, Amplitude <0.035mm or 1G; 10Hz <f < 150Hz | IEC 60255-21-1 |
| Shocks | Class 1, <15G@16 ms | IEC 60255-21-2 |
| Seismic | Class 1, Amplitude <3.5mm or 1G; 1Hz <f < 35Hz | IEC 60255-21-3 |
| Degree of Protection | IP20, Protected against objects >12.5mm, but no protection against water | IEC 60529 |
| Pollution Degree | Degree 3 | IEC 60255-5 |
| Overvoltage Category | Category III, 4KV | IEC 60255-5 |
| Rated Insulation Voltage | 500V | UL-IEC 60255- |
| Impulse Voltage Test | 5 KV | IEC 60255-5 |
| Impulse Dielectric Test | 2 KV 50/60 Hz@1min | UL-508 |
| Flammability Rating of Enclosure | V-0 | UL-94 |
| Enclosure Material | Polymers: PC, ABS, NYLON | — |
| Mounting Position | Any Position | — |
| Mounting Features | Symmetrical DIN Rail, DIN 43680; Flat surface mounting, screw 3/16" x 1/2" NEMA Style | — |
| Terminal Screw Type | Flat M2.5 | — |
| Tightening Screw Torque | <5.2 Kgf.cm (4.5 lbf.in) | — |
| Terminals Wiring | AWG 30-12, L=7-8mm (5/16); Detachable CT Box @<18mm maximum AWG 0 | — |
| Dimensions GIII | 175 x 90 x 78.0 (LxWxH) mm | — |
| Dimensions Detachable CT Box | 175 x 90 x 79.8 (LxWxH) mm | — |
| Dimensions GIII+CT Box | 175 x 90 x 157.8 (LxWxH) mm | — |
| Weight GIII | 482g (1.604 lb) | — |
| Weight Detachable CT box | 882 g (1.940 lb) | — |
| Weight GIII + Detachable CT box | 1364 g (3 lb) | — |

### C) Control Characteristics

#### Output Contact Rating

| Rating | Standard |
|--------|----------|
| 3 A @ 240 VAC, 1.5 A @ 480 VAC | UL 508 |
| Pilot Duty Section 139.1 | — |

#### Electrical Life Expectancy

| Parameter | Value |
|-----------|-------|
| Electrical Life Expectancy | 100,000 Operations |
| Mechanical Life Expectancy | 10,000,000 Operations |

#### Utilization Category (According to Voltage Model)

| Voltage Model | Rating | Standard |
|---------------|--------|----------|
| PT (120) 208/220/240, 400, 440/480 | AC-15, Capacity for loads > 72 VA | IEC60947-5-1 |

#### Voltage Measurement Range, Um

| Voltage Model | Range | Accuracy |
|---------------|-------|----------|
| PT (120) | 0 > 168 | ±2% |
| 208/220/240 | 0 > 300 | ±2% |
| 400 | 0 > 532 | ±2% |
| 440/480 | 0 > 672 VAC | ±2% |

#### Current Measurement Range, Im (According to Current Model)

| Current Model (EXT CT/5) | Range | Accuracy |
|--------------------------|-------|----------|
| 15-50 | 1.5 > 350 A | ±2% 5% > 383% CT |
| 30-100 | 3.0 > 700 A | ±2% 5% > 383% CT |
| 55-180 | 5.5 > 1100 A | ±2% 5% > 383% CT |

### D) Another measured parameters

| Parameter | Range | Tolerance |
|-----------|-------|-----------|
| Frequency Range | 45.0—70.0 Hz | 1% |
| Instantaneous Power Factor | 0.00—1.00 Hz | 8% |
| Instantaneous Power KVA | 0.0—999.9 KVA | 4% |
| Instantaneous Power KW | 0.0—999.9 Hz | 4% |
| Energy | 0—999999 KW/H | 4% |
| Total Motor Running Time (hours) | 0—999999 H | 1% |
| Digital Input 1 | 0—1 (Dry Contact) R<10K→ON; R>100K→OFF | — |
| Digital Input 2 | 0—1 (Dry Contact) R<10K→ON; R>100K→OFF | — |
| Temperature Input | -20°C > 200°C | 1% J |

### E) Algorithms and Protection Functions

#### Voltage-based Protection (According to Operation Voltage)

| Function | PT (120) | 208/220/240 | 400 | 440/480 | Unit | Notes |
|----------|----------|-------------|-----|---------|------|-------|
| Undervoltage (UV) @ Imotor = 0 or OL | 95—115 | 165—225 | 320—380 | 350—460 | Level | settings |
| Overvoltage (OV) @ Imotor = 0 or OL | 125—145 | 215—270 | 420—480 | 460—580 | Level | settings |
| Voltage Hysteresis Threshold | 3 | 6 | 10 | 12 | VAC | — |
| Voltage Unbalance Detection (VUB) | 2% > 20% | — | — | — | Level | settings |
| Single Phasing (VSP) | INV VUB > 33%, OUT VUB < 28% | — | — | — | — | — |
| Nominal Frequency | 50 or 60 Hz | — | — | — | Level | settings |
| Tolerance for Frequency Shift (FS) | 2% > 10% | — | — | — | Level | settings |
| Phase Reversal (PR) | Normal Sequence ABC, Reversal Sequence CBA | — | — | — | — | — |
| Trip Delay because of Phase Reversal | <1 sec | — | — | — | — | — |
| Trip Delay because of Another Voltage Failures (TD) | 1 > 30 sec | — | — | — | Level | settings |
| Start Up Delay (TC) | 0—600 sec | — | — | — | Level | settings |
| Start Mode | Auto/Manual selection | — | — | — | User | — |
| Minimum Time Between Two Start Up | 50 x Thermal Class Sec | — | — | — | — | — |

#### Current-based Protection (According to Operation Current)

| Function | 15-50 | 30-100 | 55-180 | EXT (CT/5) | Unit | Notes |
|----------|-------|--------|--------|-----------|------|-------|
| Nominal Current Setting (A) | 15—50 | 30—100 | 55—180 | 25% > 33 cr | Level | setting |
| Overload Level Setting (OL) | 5% > 50% (Ino) | — | — | — | Level | setting |
| Thermal Class Setting | Class 5 > Class 30 | — | — | — | Level | settings |
| Dynamic Setting of Motor (Cold Curve/Hot Curve) | Thermal class varies from 1→1/3 of adjusted class according to start up time and motor load level | — | — | — | — | IEC 60255-5 |
| Maximum Time Between Cold/Hot Curve | 2 Hours (from 1 to 1/3 or from 1/3 to 1) | — | — | — | — | IEC60255-8-1990 |
| Trip Delay because of Overload | According to Overload Level and Adjusted Class | — | — | — | — | — |
| Heat Threshold because of Overload Failure | 100% | — | — | — | — | — |
| Current Unbalance (CUB) | CUB > 48% | — | — | — | — | — |
| Current Stall Phase (CSP) | CUB > 60% | — | — | — | — | — |
| Trip Delay because of CUB | 3 Sec | — | — | — | — | — |
| Trip Delay because of CSP | 4 Sec | — | — | — | — | — |
| High-Inertia Load Option | YES/NO | — | — | — | User | selection |
| High-Inertia Load Heat Threshold | 400% | — | — | — | — | — |
| High-Inertia Load Start up Delay | 20—120 Sec | — | — | — | Level | setting |
| Thermal Machine Cooling Time | 50 x Thermal Class | — | — | — | — | — |

#### Undercurrent Protection

| Function | Value | Unit | Notes |
|----------|-------|------|-------|
| Undercurrent Disconnection Type (UC) | % Inom / Power Factor (PF) | — | — |
| Undercurrent Adjusting (by Inom) | 40% > 80% Inom | Level | setting |
| Undercurrent Adjusting (by PF) | 0.3 > 0.9 | Level | settings |
| Trip Delay because of UC | 5 > 600 Sec | Level | setting |
| Start Up Delay because of UC | 5 + 500 Min | Level | settings |
| Third Failure Detection | YES/NO | Level | settings |
| Permanent disconnection because of Third Failure | 3 Current failures in less than 30 minutes | — | — |
