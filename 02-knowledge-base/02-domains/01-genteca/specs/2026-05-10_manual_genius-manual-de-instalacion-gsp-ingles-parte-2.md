---
title: "GSPT Installation and Technical Specifications Manual"
type: Technical
source: "MANUAL DE INSTALACION GSP-Ingles.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GSPT"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GSPT Installation and Technical Specifications Manual

## Dismounting Instructions

### 10.1.1 DIN Rail Dismounting Without CT Box

**WARNING: Disconnect power supply (Circuit Breaker OFF) and electrical wiring before dismounting GSPT. Electrical shock will result in death or serious injury.**

a) Handling a flat screwdriver, pull downward the mounting bracket that you can see at rear and down side of GSPT as shown in figure.

b) With screwdriver position (2) pull out GSPT from DIN Rail as shown in figure.

### 10.1.2 DIN Rail Dismounting With CT Box

a) Handling a flat screwdriver, pull downward the mounting bracket that you can see at rear and down side of GSPT as shown in figure.

b) With screwdriver position (2) pull out GSPT from DIN Rail as shown in figure.

**Recommendation for DIN Rail Mounting:** Pull downward 2 mm with a soft movement when using screwdriver for dismounting. Strong movement could break the supporting bracket.

### 10.2.1 Flat Surface Dismounting Without CT Box

a) Unscrew both screws fixed on flat surface through attachable mounting ears and then pull out GSPT relay from flat surface as shown in figure.

### 10.2.2 Flat Surface Dismounting With CT Box

a) Unscrew both screws fixed on flat surface through attachable mounting ears and then pull out GSPT relay from flat surface as shown in figure.

## Technical Specifications

### A) Power Supply Circuit

| Parameter | Value |
|-----------|-------|
| Rated Voltage, Ue | 200, 208, 220, 230, 240, 400, 420, 440, 460, 480 VAC |
| Voltage Operation Limits, Ue | 72 → 672 VAC |
| Average Consumption, In | 38 mA |
| Rated Frequency, Fn | 50/60 Hz |
| Frequency Operation Limits, Fn | 42 → 70 Hz |
| Rated Duty | Uninterrupted Duty |

### B) Environmental Conditions, Operation Limits and Installing

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| Designed according to European Standards | IEC61010-1, IEC60255-6, IEC60947-1 | — |
| Designed according to US Standards | UL E300908, NKCR, Auxiliary Devices UL508 | — |
| CE Marking | CE (pending), Low Voltage Devices IEC60947-1 | — |
| Ambient Air Temperature (Operation) | -5 °C to 55 °C (23 °F to 131 °F) | — |
| Ambient Air Temperature (Storage) | -10 °C to +70 °C (14 °F to 158 °F) | — |
| Maximum Relative Humidity | 85% RH | — |
| Vibrations | Class 1, Amplitude <0.035 mm or 1G, 10 Hz < f < 150 Hz | IEC 60255-21-1 |
| Shocks | Class 1, < 15G @ 16 ms | IEC 60255-21-2 |
| Seismic | Class 1, Amplitude < 3.5 mm or 1G, 1 Hz < f < 35 Hz | IEC 60255-21-3 |
| Degree of Protection | IP20, Protected against objects > 12.5 mm, but no protection against water | — |
| Pollution Degree | Degree 3 | IEC 60255-5 |
| Overvoltage Category | Category III, 4 KV | IEC 60255-5 |
| Rated Insulation Voltage | 500 V | IEC 60255-5 |
| Impulse Voltage Test | 5 KV | IEC 60255-5 |
| Impulse Dielectric Test | 2.5 KV 50/60 Hz @ 1 min | UL-508 |
| Flammability Rating of Enclosure | V-0 | UL-94 |
| Enclosure Material | Polymers: LEXAN, ABS, VYDYNE | — |
| Mounting Position | Any Position | — |
| Mounting Features | Symmetrical DIN Rail, Flat surface mounting, screw 3/16" x 1/2" NEMA Style, Flush mounting | — |
| Terminal Screw Type | Flat M2.5 | — |
| Tightening Screw Torque | 5.2 Kgf/cm (4.5 lbf.in) | — |
| Terminals Wiring | AWG 12 to 18, L = 7-8 mm (5/16") | — |
| Detachable CT Box | < 18 mm, maximum AWG 0 | — |
| Dimensions GSPT | 175 x 90 x 78.0 (L x W x H) mm | — |
| Dimensions Detachable CT Box | 175 x 90 x 79.8 (L x W x H) mm | — |
| Dimensions GSPT + CT Box | 175 x 90 x 157.8 (L x W x H) mm | — |
| Weight GSPT | 463 g (1.53 lb) | — |
| Weight Detachable CT Box | 882 g (1.94 lb) | — |
| Weight GSPT + Detachable CT Box | 1345 g (2.95 lb) | — |

### C) Control Characteristics

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| Output Contact Rating | 3 A @ 240 VAC, 1.5 A @ 480 VAC, Pilot Duty | UL 508 Section 139.1 |
| Electrical Life Expectancy | 100,000 Operations | — |
| Mechanical Life Expectancy | 10,000,000 Operations | — |
| Utilization Category | AC-15, Capacity for loads > 72 VA | IEC60947-5-1 |

### D) Range Setting, Measuring

| Parameter | Specification | Accuracy |
|-----------|---------------|----------|
| Voltage Measurement Range, Um | 0 → 672 VAC | +2% |
| Current Measurement Range, Im | 3.0 → 1000 A | +2% |

### E) Algorithms and Protection Functions

| Code | Function | Specification |
|------|----------|---------------|
| e.1 | Undervoltage (UV) | -20% > -5% around nominal voltage (factory default = -10%) |
| e.2 | Overvoltage (OV) | +5% > +20% around nominal voltage (factory default = +10%) |
| e.3 | Voltage Hysteresis Threshold | +/-3% of nominal voltage VAC |
| e.4 | Voltage Unbalance Detection (VUB) | 2% > 10% |
| e.5 | Single Phasing (VSP) | IN VUB > 33%, OUT VUB < 28% |
| e.6 | Rated Frequency | 50/60 Hz |
| e.7 | Tolerance for Frequency Shift (FS) | 2% > 10% |
| e.8 | Phase Reversal (PR) | Normal Phase Sequence A>B>C, Reversed Phase Sequence C>B>A |
| e.9 | Trip Delay because of Phase Reversal (PR) | < 1 sec. |
| e.10 | Trip Delay because of Another Voltage Failures (TD) | 1 → 30 sec. |
| e.12 | Trip Delay because of VSP | 3 sec. |
| e.13 | Start Mode | Auto/Manual |
| e.14 | Nominal Current Setting | 30-100 A, 100-180 A, 55-180 A |
| e.15 | Overload Level Setting (OL) | 5% > 50% Inom |
| e.15a | Delay to Connection because of Overload (OC) | 10 to 60 Minutes Adjustable |
| e.16 | Thermal Class | 10 |
| e.17 | Dynamic Setting of Motor Model (Cold Curve/Hot Curve) | Thermal class varies from 1 → 1/3 of adjusted class according to start up time and motor load level | IEC 60255-8 |
| e.18 | Maximum Time Between Cold/Hot Curve | 9 Hours (from 1 to 1/3 or from 1/3 to 1) | IEC 60255-8-1990 |
| e.19 | Trip Delay because of Overload | According to Overload Level and Adjusted Class |
| e.20 | Heat Threshold because of Overload Failure | 100% |
| e.21 | Current Unbalance (CUB) | CUB > 48% |
| e.22 | Current Stall Phase (CSP) of Accelerated Locked Rotor | CUB > 60% |
| e.23 | Accelerated Locked Rotor Detection (LR) | Permanently Supervised to 100% |
| e.24 | Trip Delay because of CSP | 3 sec. |
| e.25 | Trip Delay because of CUB | 4 sec. |
| e.26 | Thermal Machine Cooling Time | 480 sec. |
| e.27 | Undercurrent | YES / NO |
| e.28 | Undercurrent Disconnection Type (UC) | % Inom |
| e.29 | Undercurrent Adjusting (% Inom) | Related to nominal current level, Inom |
| e.30 | Trip Delay because of UC | 5 → 600 sec. |
| e.31 | Start Up Delay because of UC | 2 → 500 min. |
| e.32 | Third Failure Detection | YES / NO |
| e.33 | Permanent Disconnection because of Third Failure | 3 Current failures in less than 30 minutes | IEEE Std 037.112-1996 |
| e.34 | Trip Delay because of Third Failure | 3 sec. |

### Temperature Sensor Characteristics

| Code | Parameter | Specification |
|------|-----------|---------------|
| e.35 | Compensation by Temperature (Bias) | YES / NO User selection |
| e.36 | Initial Temperature Setting (Ti) | 20 → 150 °C |
| e.37 | Maximum Motor Temperature (Tm) | 50 → 200 °C |
| e.38 | Sensor Type | Platinum 100 Ohm, 3 Wires (PTC 100) / compatible with 2 and 4 wires |
| e.39 | Advance Protection for Submersible Pumps | Setting as Tm |
| e.41 | Maximum Starts per Hour | YES / NO User selected |
| e.42 | Limit of Allowable Starts per Hour | Automatic, until 12 according HP. NEMA MG10, Minimum value can be selected by user |
| e.43 | Time Between Starts | 1 to 10 min. NEMA MG10 |

### D) Additional Measured Parameters

| Code | Parameter | Range | Accuracy |
|------|-----------|-------|----------|
| d.3 | Frequency Range | 45.0 → 70.0 Hz | 1% |
| d.4 | Instantaneous Power Factor | 0.00 → 1.00 | 8% |
| d.5 | Instantaneous Reactive Power | 0.0 → 999.9 KVA | 4% |
| d.6 | Instantaneous Real Power | 0.0 → 999.9 KW | 4% |
| d.7 | Energy | 0 → 999999 KWH | 4% |
| d.8 | Total Motor Running Time (hours) | 0 → 999999 H | 1% |
| d.9 | Temperature Input | -20 °C → 200 °C | 1% |

### G) Immunity and Emissions, Electromagnetic Interference (EMC)

User selection for Heavy Industrial Environment (B)

| Code | Test | Standard |
|------|------|----------|
| 9.1 | Electrostatic Discharge | IEC 61000-4-2 |
| 9.2 | Immunity to Radio Frequency Test | IEC 61000-4-3 |
| 9.3 | Electrical Fast Transients | IEC 61000-4-4 |
| 9.4 | Surge Immunity Test | IEC 61000-4-5 |
| 9.5 | Radio-Frequency Continuous Conducted | IEC 61000-4-6 |
| 9.6 | Power Frequency Magnetic Field | IEC 61000-4-8 |
| 9.7 | Voltage Dips, Short Interruptions and Voltage Variations | IEC 61000-4-11 |
| 9.8 | Harmonics and Interharmonics Immunity Tests | IEC 61000-4-13 |
| 9.9 | Voltage Fluctuation Immunity | IEC 61000-4-14 |
| 9.10 | Unbalance Immunity Test | IEC 61000-4-27 |
| 9.11 | Variation of Power Frequency | IEC 61000-4-28 |

### F) Communications and Other Special Functions

| Code | Feature | Specification |
|------|---------|---------------|
| f.1 | Communication Protocol | MODBUS RTU @ 9600 8N1 |
| f.2 | Communication Ports | Port GIO PORT (*) |
| f.3 | Address Range | 1 → 127 |
| f.4 | History Buffer Memory | 80 last faults report (failure type, value, date, hour and time elapsed) |
| f.5 | Memory of Settings | Memory of settings for operational limits on Voltages, Currents, Temperatures, Auto/Manual restart Mode |
| f.6 | Parameters Block | 0000 Free, 0001 - 9999 Blocked User selection |

(*) GIO Plug is required for GIO Port communication. It is available separately.

## Cold-Hot Curves Maximum Allowable Starts per Hour

According to the settings, the GSPT provides the following parameters, depending on the maximum power of the motor.

- **HP** = Nominal Power of motor, defined by the user
- **Sph** = Maximum allowable starts per hour, in approximation to standard NEMA MG10
- **Inom** = Current value on GSPT adjusted previously by the user (referred to FLA - Full Load Amperage adjustable on the product)

## How to Order Relayne GSPT According to Customer Needs

### Configuration Options

**Base Model:** GSPT MV

**Multivoltage (MV):**
- Standard Voltages: 208, 220, 230, 240, 400, 440, 480 VAC
- Special Voltages: 200, 420, 460 VAC

**Amperage:**
- 30 to 100 A
- 55 to 180 A

**Language:**
- S = Spanish
- E = English

### Manufacturer Information

**Relayne - Generación de Tecnología**

Miami Breaker INC.  
7060 Nw. 52nd Street  
Miami, FL 33166  
Phone: 001-786-3365780

Av. El Buen Pastor c/c Vargas, Edif. Alba, Piso 1, Oficina 1-A  
Boleita Norte  
Caracas - Venezuela  
Telfs: (0212) 237.0711 / 1151 / 3477 / (0212) 238.7006  
Fax: (0212) 235.2497

E-mail: genteven@genteca.com.ve  
Website: www.genteca.com.ve

---

*Note: Technical data are valid at the time of printing. We reserve the right to subsequent alterations.*
