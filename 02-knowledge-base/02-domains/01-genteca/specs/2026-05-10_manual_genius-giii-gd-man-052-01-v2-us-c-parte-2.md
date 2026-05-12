---
title: "GIII Installation Manual - Schedule Timer and Dismounting Instructions"
type: Technical
source: "GIII_GD-MAN-052-01-V2-US-C.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GIII"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GIII Installation Manual

## 9.1 GIII Recommended Values for Adjustable Parameters

### Undervoltage (UV) and Overvoltage (OV)

Manufacturers usually offer motors with limited range of operation voltage inside of ±10% of nominal value.

**Example:** A protector installed for a motor of 220V should be adjusted in:
- UV = 220 × 90% = 198V (Undervoltage)
- OV = 220 × 110% = 242V (Overvoltage)

### Voltage Unbalance

According to NEMA MG1 standard, it is recommended that motors operate with an unbalance voltage less than 5%.

### Overload (OL)

The recommended value for protection against overload is inside the range of 110% to 120% of nominal current (In) or the current specified in the motor nameplate at maximum charge (FLA).

- IN = FLA motor nameplate
- OL = Service factor motor nameplate

### Underload by Current (%In)

When chosen to protect against charge loss through current monitoring, a value by defect of 80% of the current at maximum charge (FLA) specified by the manufacturer is recommended.

### Underload by Power Factor (PF)

- Applicable to motors over dimensioned that require protection against charge loss during startup (Example: submersible pumps at gas stations, etc.)
- When chosen to protect against charge loss through monitoring the power factor (PF), the GIII comes adjusted from factory with 0.5. Although the protection can be adjusted in a range of 0.1 to 0.9 FP, adjustment above 0.3 FP is recommended.

### Selection of the Thermal Class of the Motor

- **Class 5:** Little motors with fast acceleration, that require faster detection of overload failure.
- **Class 10 (Fast):** Motors used in compressors, refrigeration equipment, submersible pumps and motors of general purpose usually classified under standard IEC, that reach continual operation speed in less than 4 seconds.
- **Class 15:** Motors for specialized applications.
- **Class 20 (Standard):** Motors of general purpose qualified under NEMA standard.
- **Class 30 (Slow):** Motors for charge of high inertia (HIGH INERTIA, times that exceed 10 seconds).

## 9.2 GIII+ Schedule Timer Adjustment Guide

The GIII+ includes "CLOCK ADJUSTMENTS" and "SCHEDULE TIMER" for EVENT and HOLIDAY adjustments.

### EVENT 01 (Example)

From Tuesday to Saturday and Holiday HOLIDAY 01
- **June 24th**
- ON: 7:30 hrs
- OFF: 16:45 hrs

The adjustment guide provides step-by-step navigation through the device display to configure:
- Individual day selection (Monday through Sunday)
- Holiday date setup with day and month entry
- ON/OFF time configuration in hours and minutes
- Event and Holiday assignment

### HOLIDAY 01 Adjustment (Example)

- DAY: 24
- MONTH: 6
- ON: 07:30
- OFF: 16:45

**Note:** If you require to adjust a new EVENT or HOLIDAY, press (A) or (Y) to look for the number to assign and then press to enter it. If you want to exit, press (D) and you will go to screen 7.4.

## 10 GIII DISMOUNTING INSTRUCTIONS

### WARNING
Disconnect power supply (Circuit Breaker OFF) and electrical wiring before dismounting GIII. Electrical shock will result in death or serious injury.

### 10.1.1 DIN Rail Dismounting Without CT Box

a) Handling a flat screwdriver, pull downward the mounting bracket that you can see at rear and down side of GIII as shown in figure.

b) With screwdriver position (2) pull out GIII from DIN Rail as shown in figure.

### 10.1.2 DIN Rail Dismounting With CT Box

a) Handling a flat screwdriver, pull downward the mounting bracket that you can see at rear and down side of GIII as shown in figure.

b) With screwdriver position (2) pull out GIII from DIN Rail as shown in figure.

### Recommendation for DIN Rail Mounting

Pull downward 2 mm with a soft movement when using screwdriver for dismounting. Strong movement could break the supporting bracket.

### 10.2.1 Flat Surface Dismounting Without CT Box

a) Unscrew both screws fixed on flat surface through attachable mounting ears and then pull out GIII relay from flat surface as shown in figure.

b) With screwdriver position (2) pull out GIII from DIN Rail as shown in figure.

### 10.2.2 Flat Surface Dismounting With CT Box

a) Unscrew both screws fixed on flat surface through attachable mounting ears and then pull out GIII relay from flat surface as shown in figure.

## 11 GIII Technical Specifications

### A) Power Supply Circuit

| Parameter | Values |
|-----------|--------|
| a.1 Rated Voltage, Ue | 120/208/220/240 480 (440/480) VAC |
| a.2 Voltage Operation Limits, Ue | 72>168 145>312/228>532 264>672 VAC |
| a.3 Average Consumption, In | 38 mA |
| a.4 Frequency Operation Limits, Fn | 42>70 Hz / 50/60 Hz |
| a.5 Rated Duty | Uninterrupted Duty |

### B) Application Data, Environmental Conditions, Operation Limits and Installing

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| b.1 Designed according to European Standards | IEC61010-1, IEC60255-6 LVD & EMC, IEC60947-1 | - |
| b.2 UL Listing | Aux. Device NKCR Certified for USA, Aux. Device NKCR7 Certified for Canada | 00908 |
| b.3 CE Marking | CE (pending), Low Voltage Devices | IEC60947-1 |
| b.4 Ambient Air Temperature (Operation) | -5 °C to 55 °C (23 °F to 131 °F) | - |
| b.5 Ambient Air Temperature (Storage) | -10 °C to +70 °C (14 °F to 158 °F) | - |
| b.6 Maximum Relative Humidity | 85% R.H. | - |
| b.7 Vibrations | Class 1, Amplitude <0.035mm or 1G, 10Hz <f < 150Hz | IEC 60255-21-1 |
| b.8 Shocks | Class 1, <15G@16 ms | IEC 60255-21-2 |
| b.9 Seismic | Class 1, Amplitude < 3.5mm or 1G, 1Hz <f < 35Hz | IEC 60255-21-3 |
| b.10 Degree of Protection | IP20, Protected against objects > 12.5mm, but no protection against water | IEC 60529 |
| b.11 Pollution Degree | Degree 3 | IEC 60255-5 |
| b.12 Overvoltage Category | Category III, 4KV | IEC 60255-5 |
| b.13 Rated Insulation Voltage | 500V | UL-IEC 60255- |
| b.14 Impulse Voltage Test | 5 KV | IEC 60255-5 |
| b.15 Impulse Dielectric Test | 2 KV 50/60 Hz@1min | UL-508 |
| b.16 Flammability Rating of Enclosure | V-0 | UL-94 |
| b.17 Enclosure Material | Polymers: PC, ABS, NYLON | - |
| b.18 Mounting Position | Any Position | - |
| b.19 Mounting Features | Symmetrical DIN Rail, DIN 43680, Flat surface mounting, screw 3/16" x 1/2" NEMA Style | - |
| b.20 Terminal Screw Type / Tightening Screw Torque | Flat M2.5 / <5.2 Kgf.cm (4.5 Ibf.in) | - |
| b.21 Terminals Wiring | AWG 30-12, L=7-8mm (5/16"), Detachable CT Box @<18mm maximum AWG 0 | - |
| b.22 Dimensions GIII | 175 x 90 x 78.0 (LxWxH) mm | - |
| b.23 Dimensions Detachable CT Box | 175 x 90 x 79.8 (LxWxH) mm | - |
| b.24 Dimensions GIII+CT Box | 175 x 90 x 157.8 (LxWxH) mm | - |
| b.25 Weight | GIII: 482g (1.604Ib), Detachable CT box: 882 g (1.9401b), GIII+ with Detachable CT Box: 1364 g (3ib) | - |

### C) Control Characteristics

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| c.1 Output Contact Rating | 3 A@240 VAC, 1.5 A@480 VAC Pilot Duty Section 1391 | UL 508 |
| c.2 Electrical Life Expectancy | 100,000 Operations | - |
| c.3 Mechanical Life Expectancy | 10,000,000 Operations | - |
| c.4 Utilization Category | AC-15, Capacity for loads> 72 VA (According to Voltage Model) 208/220/240 VAC + 2% | IEC60947-5-1 |
| c.5 Voltage Measurement Range, Um | 0 >168/0 > 300 0 >%32 accuracy (According to Current Model) 15-50 30-100 55:480 EXT (CT/5) | - |
| c.6 Current Measurement Range, Im | 1.5 > 350/3.0>700 15.5 1100 5% >388%cT A, 42% accuracy | - |

### D) Another Measured Parameters

| Parameter | Range | Accuracy |
|-----------|-------|----------|
| d.3 Frequency Range | 45.0–70.0 Hz | 1% |
| d.4 Instantaneous Power Factor | 0.00–1.00 Hz | 8% |
| d.5 Instantaneous Power KVA | 0.0–999.9 KVA | 4% |
| d.6 Instantaneous Power KW | 0.0–999.9 Hz | 4% |
| d.7 Energy | 0–999999 KW/H | 4% |
| d.8 Total Motor Running Time (hours) | 0–999999 H | 1% |
| d.9 Digital Input 1 | R<10K->ON / 0>1 R>100K->OFF Dry Contact | - |
| d.10 Digital Input 2 | R<10K->ON / 0>1 R>100K->OFF Dry Contact | - |
| d.11 Temperature Input | -20°C >200°C | 1% J |

### E) Algorithms and Protection Functions

| Parameter | PT (120)/208/220/240 | 480 | 440/480 VAC | Standard/Notes |
|-----------|---------------------|-----|------------|-----------------|
| e.1 Undervoltage (UV) @ Imotor= 0 or OL | 95>115 | 165>225 | 320-2380 350>460 | Level settings |
| e.2 Overvoltage (OV) @ Imotor=0 or OL | 125>145 | 215>270 | 420>480 460>580 | Level settings |
| e.3 Voltage Hysteresis Threshold | 3 | 6 | 12 | VAC |
| e.4 Voltage Unbalance Detection (VUB) | 2%>20% | - | - | Level settings |
| e.5 Single Phasing (VSP) | INV VUB > 33%, OUT VUB < 28% | - | - | - |
| e.6 Nominal Frequency | 50 or 60 Hz | - | - | Level settings |
| e.7 Tolerance for Frequency Shift (FS) | 2%>10% | - | - | Level settings |
| e.8 Phase Reversal (PR) | Normal Sequence ABC, Reversal Sequence CBA | - | - | - |
| e.9 Trip Delay because of Phase Reversal | <1 sec | - | - | - |
| e.10 Trip Delay because of Another Voltage Failures (TD) | 1>30 sec | - | - | Level settings |
| e.11 Start Up Delay (TC) | 0>600 sec | - | - | Level settings |
| e.12 Start Mode | Auto/Manual selection | - | - | User |
| e.13 Minimum Time Between Two Start Up | 50 x Thermal Class Sec | - | - | - |
| e.14 Nominal Current Setting (According to Operation Current) 15-50 | 30-100 | 55-180 | EXT (CT/5) 25%>33 cr [(A) Level setting | - |
| e.15 Overload Level Setting (OL) | 5%>50% (Ino) | - | - | Level setting |
| e.16 Thermal Class Setting | Class 5>Class 30 | - | - | Level settings |
| e.17 Dynamic Setting of Motor Model (Cold Curve/Hot Curve) | Thermal class varies from 1->1/3 of adjusted class according to start up time and motor load level | - | - | IEC 60255-5 |
| e.18 Maximum Time Between Cold/Hot Curve | 2 Hours (from 1 to 1/3 or from 1/3 to 1) | - | - | IEC-60255-8-1990 |
| e.19 Trip Delay because of Overload | According to Overload Level and Adjusted Class | - | - | - |
| e.20 Heat Threshold because of Overload Failure | 100% | - | - | - |
| e.21 Current Unbalance (CUB) | CUB > 48% | - | - | - |
| e.22 Current Stall Phase (CSP) | CUB>60% | - | - | - |
| e.23 Underload Detection (LA) | YES/NO | - | - | - |
| e.24 Trip Delay because of CUB | 3 Sec | - | - | - |
| e.25 Trip Delay because of CSP | 4 Sec | - | - | - |
| e.26 High-Inertia Load Option | YES/NO | - | - | User selection |
| e.27 High-Inertia Load Heat Threshold | 400% | - | - | - |
| e.28 High-Inertia Load Start up Delay | 20>120 Sec | - | - | Level setting |
| e.29 Thermal Machine Cooling Time | 50 x Thermal Class | - | - | - |
| e.30 Undercurrent Disconnection Type (UC) | %Inom / Power Factor (PF) | - | - | - |
| e.31 Undercurrent Adjusting (by Inom) | 40%>80% Inom | - | - | Level setting |
| e.32 Undercurrent Adjusting (by PF) | 0.3>0.9 | - | - | Level settings |
| e.33 Trip Delay because of UC | 5>600 Sec | - | - | Level setting |
| e.34 Start Up Delay because of UC | 5+500 Min | - | - | Level settings |
| e.35 Third Failure Detection | YES/NO | - | - | Level settings |
| e.36 Permanent disconnection because of Third Failure | 3 Current failures in less than 30 minutes | - | - | - |
