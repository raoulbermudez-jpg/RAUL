---
title: "GIII+MV Technical Specifications and Installation Manual"
type: Technical
source: "GD-MAN-8003-01-V1-US-C.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "GIII+MV"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GIII+MV TECHNICAL SPECIFICATIONS

## A) Power Supply Circuit

| Parameter | Value | Unit |
|-----------|-------|------|
| Rated Voltage, Ue | 200, 208, 220, 230, 240, 400, 420, 440, 460, 480 | VAC |
| Voltage Operation Limits, Ue | 72 → 672 | VAC |
| Average Consumption, In | 38 | mA |
| Rated Frequency, Fw | 50/60 | Hz |
| Frequency Operation Limits, Fn | 42 → 70 | Hz |
| Rated Duty | Uninterrupted Duty | — |

## B) Environmental Conditions, Operation Limits and Installing

| Parameter | Value | Standard |
|-----------|-------|----------|
| Ambient Air Temperature (Operation) | -5°C a 55°C (23°F a 131°F) | — |
| Ambient Air Temperature (Storage) | -10°C a +70°C (14°F a 158°F) | — |
| Maximum Relative Humidity | 85% R.H. | — |
| Vibrations | Class 1, Amplitude <0.035mm or 1G, <f< 150Hz | IEC 60255-21-1 |
| Degree of Protection | IP20, Protected against objects > 12.5mm, but no protection against water | IEC 60529 |
| Pollution Degree | Degree 3 | IEC 60255-5 |
| Overvoltage Category | Category III, 4KV | IEC 60255-5 |
| Rated Insulation Voltage | 500V | IEC 60255-5 |
| Impulse Voltage Test | 5 KV | IEC 60255-5 |
| Impulse Dielectric Test | 2.5 KV 50/60 Hz @ 1min | UL-508 |
| Flammability Rating of Enclosure | V-0 | UL-94 |
| Enclosure Material | Polymers: LEXAN, ABS, VYDYNE | — |
| Mounting Position | Any Position | — |
| Mounting Features | Symmetrical DIN Rail bias, Flat surface mounting, screw 3/16" x 1/2" NEMA Style, Flush Mounting | — |
| Terminal Screw Type | Flat M2.5 | — |
| Tightening Screw Torque | 5.2 kgf·cm (4.5 lb·in) | — |
| Terminals Wiring | 12 AWG to 18 | — |
| Detachable CT Box | @ < 18 mm maximum AWG0 | — |
| Dimensions GIII+MV | 175 x 90 x 78.0 (L x W x H) | mm |
| Dimensions Detachable CT Box | 175 x 90 x 79.8 (L x A x H) | mm |
| Dimension GIII+MV CT Box | 175 x 90 x 157.8 (L x A x H) | mm |
| Weight GIII+MV | 0.482 | Kg (1.60 lb) |
| Weight GIII+MV Detachable CT Box | 1.364 | Kg (3.00 lb) |

## C) Control Characteristics

| Parameter | Value | Standard |
|-----------|-------|----------|
| Designed according to European Standards | IEC61010-1, IEC60255-6, IEC60947-1 | LVD & EMC |
| Designed according to US Standards | UL (pending), NKCR, Auxiliary Devices UL508 | — |
| CE Marking | CE (pending), Low Voltage Devices | IEC60947-1 |

## D) Range Setting, Measuring

### According to Voltage Model

| Parameter | Value | Accuracy | Unit |
|-----------|-------|----------|------|
| Voltage Measurement Range, Um | 0 → 672 | +2% | V~ |

### According to Current Model

| Model | Current Measurement Range, Im | Tolerance |
|-------|-------------------------------|-----------|
| 050 | 3 → 500 A | 5% → 333% CT |
| 100 | 6 → 1000 A | +2% accuracy |
| 180 | 11 → 1800 A | — |
| EXT (CT/5) | — | — |

### Output Contact Rating

| Specification | Value | Standard |
|---------------|-------|----------|
| Pilot Duty | A300 | UL 508 Section 199.1 |
| — | 3 AQ240 V- / 1.5 AQ480 V- | — |
| Electrical Life Expectancy | 100,000 Operations | — |
| Mechanical Life Expectancy | 10,000,000 Operations | — |

### Another Measured Parameters

| Parameter | Range | Tolerance |
|-----------|-------|-----------|
| Frequency Range | 45.0 → 70.0 | 1% |
| Instantaneous Power Factor | 0.00 → 1.00 | 8% |
| Instantaneous Reactive Factor | 0.0 → 999.9 | 4% kVA |
| Instantaneous Real Power | 0.0 → 999.9 | 4% kW |
| Energy | 0 → 999999 | 4% kWh |
| Total Motor Running Time (hours) | 0 → 999999 | 1% h |
| Digital Input 1 (Dry Contact) | R > 100K OFF, R < 10K ON | 0 → 1 |
| Digital Input 2 (Dry Contact) | R > 100K OFF, R < 10K ON | 0 → 1 |
| Temperature Input | -20°C → 200°C | 1% |

## E) Algorithms and Protection Functions

| Parameter | Description | Setting |
|-----------|-------------|---------|
| Undervoltage (UV) | -20% > -5% of Nominal Voltage | Default Parameter = -10%, Imotor = 0 & OL |
| Overvoltage (OV) | +5% → +20% of Nominal Voltage | Default Parameter = +10%, Imotor = 0 & OL |
| Voltage Hysteresis threshold | +/- 3% Nominal Voltage | V~ |
| Voltage Unbalance Detection (VUB) | 2% > 10% | Level Settings |
| Single Phasing (VSP) | IN VUB > 33%, OUT VUB < 28% | — |
| Rated Frequency | 50 & 60 | Hz Level Settings |
| Tolerance for Frequency Shift (FS) | 2% > 10% | Level Settings |
| Phase Reversal (PR) | Normal Phase Sequence A>B>C, Reversed Phase Sequence C>B>A | — |
| Trip Delay Because of Phase Reversal (PR) | — | 4 s |
| Trip Delay Because of Voltage Failures (TD) | 1 → 30 | s Level Settings |
| Start Up Delay (SD) | 0 → 600 | s Level Settings |
| Trip Delay Because of VSP (TD) | — | 3.5 s |
| Start Mode | Auto / Manual | Selection |
| Minimum Time Between Start Up | 1 → 10 | min |
| Nominal Current Setting | 050: 400, 500, 600, 750, 800, 1550 | A |
| — | 100: 30 → 100 A | — |
| — | 180: 55 → 180 A | — |
| — | EXT: 50 → 991200 A | — |
| Overload Level Setting (OL) | 5% > 50% | Level Settings |
| Thermal Class Setting | 5 → 30 | Level Settings |
| Dynamic Setting of Motor Model (Cold Curve / Hot Curve) | Thermal Class varies from 1⅛/8⅜ of Adjusted class according to start up time and motor load level | IEC 60255-8 |
| Maximum Time Between Cold / Hot Curve | 2 Hours (from 1 to 1/3 ó de 1/3 a 1) | IEC 60255-3-1990 |
| Trip Delay Because of Overload | According to Overload Level and Adjusted Class | IEEE Std. C37.112-1996 |
| Heat Threshold Because of Overload Failure | 100% | — |
| Current Unbalance (CUB) | CUB > 48% | — |
| Current Stall Phase (CSP) | CUB > 60% | — |
| Accelerated Locked Rotor Detection (LR) | Use selection Heat YES/NO | — |
| Trip Delay Because of CSP | — | 3 s |
| Trip Delay Because of CUB | — | 4 s |
| High-Inertia Load Option | YES/NO | Selection |
| High-Inertia Load Heat Threshold | 400% | — |
| High-Inertia Load Start up Delay | 20 → 120 | s Level Settings |
| Thermal Machine Cooling Time | 50 x Thermal class | s |
| Start Up Delay after Overload (SD) | 10 - 60 | min Level Settings |
| Undercurrent | YES/NO | Selection |
| Undercurrent Disconnection (UC) | % Inom & FP (Power Factor) | — |
| Undercurrent Disconnection (%Inom) | 30% > 90% | Level Settings |
| Undercurrent Adjusting (PF) | 0.3 → 0.9 | Level Settings |
| Trip Delay Because of (UC) | 5 → 600 | Level Settings |
| Start Up Delay Because of (UC) | 2 → 500 | Level Settings |
| Third Failure Detection | YES/NO | Sets |
| Permanent Disconnection Because of Third Failure | 3 Current Failures in less Than 30 minutes | IEEE Std. C37.112-1996 |
| Trip Delay Because of Accelerated Locked Rotor | — | 3 s |

### Temperature Sensor Characteristics

| Parameter | Value | Unit |
|-----------|-------|------|
| Compensation by Temperature (bias) | YES/NO | User Selection for Heavy Industrial Environment (B) |
| Inicial Temperature Setting (Ti) | 20 → 150 | °C Degrees |
| Maximum Motor Temperature (Tm) | 50 → 200 | °C Degrees |
| Sensor Type | Pt100 RTD | — |
| Temperature for Disconnection | Setting of maximum level, Tm | — |
| Temperatura de Conexión | (Tm - Ti) / 6 + Ti | — |
| Maximum Starts per Hour | YES / NO | User Selection |
| Limit of Allowable Starts per Hour | Automatic, until 12 according HP; Minimum value can be selected by the user | NEMA MG10 |
| Real Time Clock | hh:mm dd/mm/aa | — |
| Load Control by Events (schedule) | YES/NO | User Selection |
| Schedule Timer (events) | 60 | User Selection |
| Schedule Timer (holidays) | 20 | User Selection |

### Tripping Cold Curve

| Thermal Class | HP | Sph |
|---------------|-----|------|
| Class 5 | 1 | 12 |
| Class 10 | 1.5 | 12 |
| Class 15 | 2 | 12 |
| Class 20 | 3 | 12 |
| Class 25 | 5 | — |
| Class 30 | 7.5 | 7 |
| — | 10 | 5 |
| — | 15 | — |
| — | 20 | 4 |
| — | 25 | 4 |
| — | 30 | 4 |
| — | 40 | 3 |
| — | 50 | 3 |
| — | 60 | 3 |
| — | 75 | 3 |
| — | 100 | 2 |
| — | 125 | 2 |
| — | 150 | 2 |
| — | 200 | 2 |

**Note:** Hot Curve = Cold Curve / 3

**Note:** For motors greater than 250 HP the maximum number of starts per hour is 2.

## F) Communications and Special Functions

| Parameter | Specification | — |
|-----------|---------------|---|
| Communication Protocol | MODBUS RTU @ 9600 - 19200 - 38400 8N1 | — |
| Communication Ports | GIO PORT (*) & Port RS-485 | — |
| Address Range | 1 → 127 | — |
| History Buffer Memory | 100 last faults report (failure type, value, date, hours and time elapsed) | — |
| Memory of Settings | Memory of settings for operational limits on Voltages, Currents, Temperatures, Auto/Manual restart Mode | — |
| Parameters Block | 0000 Free, 0001 → 9999 Blocked | User Selection |

(*) GIO PLUG is required for GIO Port communication. It is available separately.

## G) Immunity and Emissions, Electromagnetic Interference (EMC)

| Parameter | Standard |
|-----------|----------|
| Electrostatic Discharge | IEC 61000-4-2 |
| Immunity to Radio Frequency Test | IEC 61000-4-3 |
| Electrical Fast Transients | IEC 61000-4-4 |
| Surge Immunity Test | IEC 61000-4-5 |
| Radio-Frequency Continuous Conducted | IEC 61000-4-6 |
| Power Frequency Magnetic Field | IEC 61000-4-8 |
| Voltage Dips, Short Interruptions and Voltage Variations | IEC 61000-4-11 |
| Harmonics and Interharmonics | IEC 61000-4-18 |
| Immunity Tests | IEC 61000-4-18 |
| Voltage Fluctuation Immunity | IEC 61000-4-14 |
| Unbalance Immunity Test | IEC 61000-4-27 |
| Variation of Power Frequency | IEC 61000-4-28 |

## Current Rating for External CTs

| CT Model | Current Range | A |
|----------|---------------|---|
| CT 600/5 | 150 a 200 | A |
| CT 750/5 | 190 a 250 | A |
| CT 800/5 | 200 a 260 | A |
| CT 1000/5 | 250 a 330 | A |
| CT 1200/5 | 300 a 400 | A |
| CT 1500/5 | 375 a 500 | A |
| CT 2000/5 | 500 a 660 | A |

## Maximum Allowable Starts per Hour

The GIII+MV provides the following parameters, depending on the maximum power of the motor.

**Nominal Power of Motor:** Defined by the user

**Sph:** Maximum number of starts allowed per hour

*This Feature is provided according to recommendations of NEMA MG10*

## How to Order GIII+MV

**GIII+MV - MULTIVOLTAGE AMPERAGE LANGUAGE**

- **Voltage Options:** 400, 440, 480 V~ or 200, 420, 460 V~ (Special Voltage)
- **Amperage Options:** 050-15-504 S / 100-30-100A / 180-55-180A / EXT.CTS
- **Language:** S — SPANISH / E — ENGLISH

## Manufacturer Information

**GENTE Generación de Tecnología, C.A.**

- RIF: J-00223173-4
- Address: Av. El Buen Pastor cruce con calle Vargas, Edif. Alba, Piso I, Local I-A, Boleita Norte, Caracas - República Bolivariana de Venezuela
- Postal Code: 1070
- Telephone: ++(58 212) 237.07.11
- Fax: ++(58 212) 235.24.97
- Email: genteven@genteca.com.ve
- Website: www.genteca.com.ve

---

**NOTE:** Technical data are valid at the time of printing. We reserve the right to subsequent alterations.
