---
title: "GSPT - Submersible Pump Total Protection Relay"
type: Technical
source: "GSPT_HDE_V3_US_c.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "GSPT"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GSPT - Submersible Pump Total Protection Relay

## PRODUCT DESCRIPTION

Relayne GSPT is a microcontrolled based three-phase Integral Motor Protection Relay, specifically designed to protect electric loads and motors from failure and damage due to common current and voltage faults.

Relayne GSPT constantly supervises current and voltage values; when any harmful condition occurs, the output connection is deactivated until the fault disappears, power line conditions return to an acceptable level and the motor has been totally cooled. Specific timing such as Start Up Delay (TC) and Trip Delay (TD) are incorporated to prevent nuisance tripping due to rapid power fluctuations.

Relayne GSPT increases protection for submersible pumps by limiting the amount of allowed starting during continuous hours of operation according to the motor capacity in HP. It protects continuously against events of Locked Rotor Acceleration and provides adjustable timing for connection after overload.

## FEATURES

### Measurement of:
- Current
- Voltage
- Frequency
- Frequency Shift
- Voltage Unbalance
- Current Unbalance
- Single Phasing
- Phase Reversal
- Locked Rotor
- Power Factor (PF), Reactive Power (KVA), Real Power (KW)
- Energy Consumption (KWH)
- Temperature

### Protection against:
- Limits of maximum starts per hour
- Overload / Undercurrent
- Overvoltage / Undercurrent
- Limits of maximum starts per hours

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
- Timer to connection after Current Overload restore
- AUTO / MANUAL Restart Mode
- Password

### Physical Features:
- Din-Rail, Flat Surface mounting
- 16x2 backlight LCD Display with current values, voltage values and load report information on screen
- Four (4) push buttons for operation and protection parameter adjustments (1 for START, 2 for ADJUST and 1 for SELECT)
- Enclosure material UL 94V0

### Reports:
- Voltage & Current report
- PEKVA, KWH, KW report
- Adjusted Values report
- Total Motor Running Timer report
- Start Mode report
- 20 Last Fault report
- Power Frequency report
- Thermal memory

### Communications:
- GIO Port or RS485 @ 9600 baud output available (MODBUS RTU protocol)

## PRODUCT STANDARDS APPLIED

### Designed according to CE Standards (LVD and EMC):
- IEC 61010-1
- IEC 60255-6
- IEC 60255-8
- IEC 60947-1

### Designed according to:
- UL 508
- IEEE 37.112
- NEMA MG110

## GENERAL FUNCTIONS & RANGE OF APPLICATIONS (INTENDED USE)

The Relayne GSPT provides electrical protection through the following general functions and setting ranges:

- **Overvoltage detection**: 5% up to 50%
- **Undervoltage detection**: -20% up to -5% rated voltage
- **Voltage Unbalance detection**: 2% up to 10% rated voltage
- **Single Phasing voltage detection**: IN 33% - OUT 28%
- **Phase Reversal detection time**: < sec
- **Start Up Delay after voltage fault recovery**: 0 to 600 sec
- **Voltage Fault detection time**: 1 to 30 sec
- **Frequency Shift detection**: +/-2% up to +/-10% rated frequency
- **Overcurrent level setting**: Adjust of low limit relative to nominal current
- **Undercurrent detection**: CUB > 48%
- **Current Unbalance detection**: CUB > 60%
- **Single Phasing current detection**
- **Thermal Class IEC 60255-8**

## TECHNICAL SPECIFICATIONS

### A) Power Supply Circuit

| Parameter | 208/220/240 V | 440/480 V | Unit |
|-----------|---------------|-----------|------|
| Rated Voltage, Ue | 208/220/240 | 440/480 | VAC |
| Voltage Operation Limits, Ue | 145 → 312 | 264 → 672 | VAC |
| Average Consumption, In | 45 | — | mA |
| Rated Frequency, Fn | 50/60 | — | Hz |
| Frequency Operation Limits, Fn | 42 → 70 | — | Hz |
| Rated Duty | Uninterrupted Duty | — | — |

### B) Environmental Conditions, Operation Limits and Installation

| Parameter | Value | Standard |
|-----------|-------|----------|
| Ambient Air Temperature (Operation) | -5 °C to 55 °C (23 °F to 131 °F) | — |
| Ambient Air Temperature (Storage) | -10 °C to +70 °C (14 °F to 158 °F) | — |
| Maximum Relative Humidity | 85% RH | — |
| Vibrations | Class 1, Amplitude <0.035mm or 1G; 10Hz <f < 150Hz | IEC 60255-21-1 |
| Degree of Protection | IP20, Protected against objects > 12.5mm, no protection against water | IEC 60529 |
| Pollution Degree | Degree 3 | IEC 60255-5 |
| Overvoltage Category | Category III | IEC 60255-5 |
| Rated Insulation Voltage | 500V | IEC 60255-5 |
| Impulse Voltage Test | 5KV | IEC 60255-5 |
| Impulse Dielectric Test | 2.5 KV 50/60 Hz, 1 min | UL-508 |
| Flammability Rating of Enclosure | V-0 | UL-94 |
| Enclosure Material | NE ABS | — |
| Mounting Position | Any Position | — |
| Mounting Features | Symmetrical DIN Rail DIN 43880; Flat surface mounting, screw 3/16" x 1/2" | NEMA Style |
| Terminal Screw Type | Flat M3 | — |
| Tightening Screw Torque | 5.1 Kgf × cm (4.4 lb × in) | — |
| Terminals Wiring | 10-18 WG | — |
| Current Sensing holes for Motor Wiring | Ø < 11mm AWG 4 | — |
| Dimensions | 92 × 91 × 96 (L×W×H) | mm |
| Weight | 494 (1.09) | g (lb) |

### C) Control Characteristics

| Parameter | Value | Standard |
|-----------|-------|----------|
| Output Contact Rating | 1 A @ 240 VAC / 0.5 A @ 480 VAC | UL 508 Section 139.1 |
| Electrical Life Expectancy | 100,000 Operations | — |
| Mechanical Life Expectancy | 10,000,000 Operations | — |
| Utilization Category | AC-15, Capacity for loads > 72 VA | IEC 60947-5-1 |

### D) Range Settings, Measuring and Other Measured Parameters

#### According to Voltage Model:

| Parameter | 208 VAC | 480 VAC | Accuracy |
|-----------|---------|---------|----------|
| Voltage Measurement, ER U | VAC | — | +2% |
| Voltage Measurement range, Um | 0 → 312 | 0 → 672 | — |

#### According to Current Model:

| Parameter | 04 A | 12 A | 32 A | 80 A | Accuracy |
|-----------|------|------|------|------|----------|
| Current Measurement Range, Im | 1-5 | 40 | 0-3 → 125 | 1 → 320 | +2% |

#### Frequency Range:
- 45.0 → 70.0 Hz

#### Power Measurements:
- **Instantaneous Power Factor**: 0.00 – 1.00
- **Instantaneous Reactive Power KVA**: 0.0 → 999.9 KVA
- **Instantaneous Real Power KW**: 0.0 → 999.9 KW
- **Energy KWH**: 0 → 999999 KW/H
- **Total Motor Running Time (hours)**: 0 → 999999 H

### E) Algorithms and Protection Functions (According to Operation Voltage)

| Function | 208 VAC | 480 VAC | Level Settings | Standard |
|----------|---------|---------|-----------------|----------|
| Undervoltage (UV) @Imotor = 0 or OL | 165 → 225 | 350 → 460 | 5 Level settings | IEC 61010-1, IEC 60255-6, IEC 60947-1 |
| Overvoltage (OV) @Imotor = 0 or OL | 215 → 270 | 460 → 580 | 5 Level settings | — |
| Voltage Hysteresis Threshold | 6 | 12 | VAC | — |
| Voltage Unbalance Detection (VUB) | — | — | a = 10% | — |
| Single Phasing (VSP) | IN VUB > 33%, OUT VUB < 28% | — | — | — |
| Rated Frequency | 50 & 60 | — | Hz | — |
| Tolerance for Frequency Shift (FS) | 2% – 10% | — | Level settings | — |
| Phase Reversal (PR) | Normal: A > B > C; Reversed: C > B > A | — | — | — |
| Trip Delay because of VSP | < 1 | 8 sec | — | — |
| Trip Delay because of Other Voltage Failures (TD) | 1 → 30 | sec | Level settings | — |
| Start Up Delay (TC) | 0 → 600 | sec | Level settings | — |

#### According to Operation Current:

| Parameter | 04 A | 12 A | 32 A | 80 A | Standard |
|-----------|------|------|------|------|----------|
| Nominal Current Setting | 3-5 | 35-125 | 10-32 | 25-80 | A |
| Overload Level Setting (OL) | 5% → 50% Inom | — | Level settings | — |
| Thermal Class Setting | 5 → 35 | — | Level settings | IEC 60255-8 |
| Dynamic Setting of Motor | Thermal class varies from 1 → 1/3 of adjusted class according to start up time and motor load level | — | — | IEC 60255-8 |
| Maximum Time Between Cold/Hot Curve | 2 Hours (from 1 to 1/3 or from 1/3 to 1) | — | — | IEC 60255-8-1990 |
| Trip Delay because of Overload | According to Overload Level and Adjusted Class | — | — | — |
| Heat Threshold because of Overload Failure | 100% | — | — | — |
| Current Unbalance (CUB) | CUB > 48% | — | — | — |
| Current Stall Phase (CSP) | CUB > 60% | — | — | — |
| Trip delay because of CSP | 1 sec | — | — | — |
| Trip Delay because of CUB | 2 sec | — | — | — |
| Thermal Machine Cooling Time | 50 × Thermal Class | — | — | — |
| Undercurrent | YES/NO | — | — | — |
| Undercurrent Adjusting (% Inom) | 30% → 90% Inom | — | Level settings | — |
| Trip Delay because of UC | 2 → 500 | Min | Level settings | — |
| Start Up Delay because of UC | 2 → 500 | Min | Level settings | — |
| Third Failure Detection | YES/NO | — | Level settings | IEEE Std 27.45 1995 |
| Permanent disconnection because of Third Failure | 3 Current failures in less than 105 min | — | — | — |
| Trip delay because of accelerated locked rotor | 7 | sec | — | — |
| Additional protection for submersible pump | — | — | — | — |
| Maximum starts per hour | YES/NO | — | User selection | NEMA MG10 |
| Limit of allowable starts per hour | Minimum value can be selected by the user | — | — | — |
| Maximum Automatic | until 12 according HP | — | Settings | — |
| Time between starts | 1 to 10 | min | — | NEMA MG10 |

### F) Communications and Other Special Functions

| Parameter | Specification |
|-----------|---------------|
| Communication Protocol | MODBUS RTU @ 9600 8N1 |
| Communication Ports | Port GIO PORT (*) |
| Address Range | +127 |
| History Buffer Memory | 80 last faults report (failure type, value, date, hour and time elapsed) |
| Parameters Block | 0000 Free, 0001 → 9999 Blocked |

(*) GIO Plug is required for GIO Port communication. It is available separately.

### G) Immunity and Emissions, Electromagnetic Interference (EMC)

| Parameter | Standard |
|-----------|----------|
| Electrostatic Discharge | IEC 61000-4-2 |
| Immunity to Radio Frequency Test | IEC 61000-4-3 |
| Electrical Fast Transients | IEC 61000-4-4 |
| Surge Immunity Test | IEC 61000-4-5 |
| Radio-Frequency Continuous Conducted | IEC 61000-4-6 |
| Power Frequency Magnetic Field | IEC 61000-4-8 |
| Voltage Dips, Short Interruptions and Voltage Variations | IEC 61000-4-11 |
| Harmonics and Interharmonics Immunity Tests | IEC 61000-4-13 |
| Voltage Fluctuation Immunity | IEC 61000-4-14 |
| Unbalance Immunity Test | IEC 61000-4-27 |
| Variation of Power Frequency | IEC 61000-4-28 |

## MAXIMUM ALLOWABLE STARTS PER HOUR

| HP | Sph |
|----|-----|
| 1 | 12 |
| 1.5 | 12 |
| 2 | 12 |
| 3 | 12 |
| 5 | — |
| 7.5 | — |
| 10 | — |
| 15 | — |
| 20 | — |

**Notes:**
- HP = Nominal Power of motor, defined by the user
- Sph = Maximum allowable starts per hour, in approximation to standard NEMA MG10
- Inom = Current value on GSPT adjusted previously by the user
- Inom term is referred to FLA (Full Load Amperage) adjustable on the product

## GSPT COLD-HOT CURVES

Thermal curves are provided to determine tripping times based on motor load and operating conditions.

**Cold Curve**: Initial operation conditions  
**Hot Curve**: Extended operation conditions with accumulated thermal stress  
**Maximum Time Between Cold/Hot Curve**: 2 Hours (from 1 to 1/3 or from 1/3 to 1)

## INSTALLATION

### Safety Information

Only qualified technicians with knowledge about overload protection relay and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in equipment damage and/or personal injury.

### Special Tools for Installation or Connection

- For terminal connection use screwdriver suitable for M2.5 screws
- For flat surface mounting use screwdriver suitable for screws (3/16" × 1/2")
- Ammeter

### Connection Diagram

The GSPT features:
- Current sensing holes for motor wiring (three-phase 50/60 Hz starter circuits)
- Power supply connection points
- GIO Port (optional) for serial communication with other devices
- Output contact terminals with two states:
  - Normal: 95-96 open, 97-98 closed
  - Tripped: 95-96 closed, 97-98 open

### Mounting Options

1. **Symmetrical DIN Rail mounting** (DIN 43880)
2. **Flat Surface mounting** using exclusive attachable mounting ear with screws (3/16" × 1/2")

### Terminal Specifications

- **Screw Type**: Flat M3
- **Tightening Torque**: 5.1 Kgf × cm (4.4 lb × in)
- **Wiring**: 10-18 WG
- **Current Sensing holes**: Ø < 11mm AWG 4

## MEASURES TO BE TAKEN INTO CONSIDERATION WITH REGARDS TO EMC

### Notice

This product has been designed for industrial environment. Use of this product in residential environment may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

## HOW TO ORDER ACCORDING TO CUSTOMER NEEDS

**Model Code Format: GSPT-[Voltage]-[Amperage]-[Language]**

### Voltage Options:
- **480**: 440/480 V~
- **208**: 208/220/240 V~

### Number of Phases:
- **T**: 3 PHASES

### Amperage:
- **04**: 1-4A
- **12**: 35-125A
- **32**: 10-32A
- **80**: 25-80A

### Language:
- **S**: SPANISH
- **E**: ENGLISH

## MANUFACTURER INFORMATION

**Made and designed by:**  
Genteca, Generación de Tecnología C.A.  
R.I.F: J-00223173-4  
Av. El Buen Pastor, cruce con Calle Vargas  
Edificio Alba, Piso 1, Local 1-A  
Boleíta Norte, Caracas, 1070  
República Bolivariana de Venezuela

**Contact:**
- Phone: +58-212-237-0711 (Master)
- Fax: +58-212-235.2497
- Email: genteven@genteca.com.ve
- Website: www.genteca.com.ve

---

**NOTE:** Technical data are valid at the time of printing. Genteca reserves the right to subsequent alterations.
