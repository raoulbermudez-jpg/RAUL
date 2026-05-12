---
title: "GI General Description - Installation Manual"
type: Technical
source: "MANUAL DE INSTALACION GI - Tamaño Carta.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GI"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GI GENERAL DESCRIPTION

## Overview

GI is an electronic phase voltage relay that constantly supervises line voltage values, to protect electric loads and distribution power systems from failure and damage due to common voltage faults.

### Safety Warnings

**WARNING:** Only qualified technicians with knowledge about protection relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

**WARNING:** This product may start automatically, the user must take cautions to avoid hazards to people.

---

## GI PARTS AND PIECES

### Front Side Components

1. Indicator Lights (LED's)
   - Normal (ON) - Continuous green
   - Start Delay (TC) - Blinking green
   - Phase Reversal (PR) - Blinking red
   - Voltage Unbalance (VUB) - Continuous red
   - Single Phasing (VSP) - Blinking red
   - Overvoltage (OV) - Continuous red
   - Undervoltage (UV) - Blinking red

2. Minimum Voltage Setting Knob (VMIN)
3. Maximum Voltage Setting Knob (VMAX)
4. Back Groove for DIN RAIL Mounting
5. Attachable Mounting Ear for Flat Surface Mounting
6. Supporting Bracket
7. L1 L2 L3 Power Supply Voltage Input
8. Trip Relay (6-7); Aux. Relay (7-8)
9. GIO Port
10. AUTO / MANUAL Start Mode Slide-Switch
11. GIO PORT Cover
12. START Push Button
13. Start Delay Setting Knob (TC)
14. Trip Delay Setting Knob (TD)

---

## INSTALLATION

### 3.1 DIN RAIL MOUNTING

**CAUTION:** GI must be installed in an accessible position free from dust, dirt, dampness and vibration. Allow enough space for air circulation around the enclosure and easy access available to all operator controls. Indoors use only.

**CAUTION:** This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

**CAUTION:** An incorrectly applied or installed GI can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the GI.

#### Instructions for Mechanical Installation

a) Place GI at inclined position with its back side placed toward the upper edge of the DIN Rail and push down GI relay as shown in figure until it does CLICK on the rail.

### 4.1 FLAT SURFACE MOUNTING

#### Instructions for Mechanical Installation

a) Take off the two (2) mounting ears located at back side of GI, insert and slip both mounting ears into the GI back side grooves.

b) Place GI over flat surface panel and fix it handling a screwdriver suitable for screws 3/16" x 1/2".

**Recommendation for Flat Surface Mounting:** Make two (2) holes (5/32") on panel surface before installing.

---

## GI GENERAL DIMENSIONS

**Size:** Length = 105 mm, Width = 90 mm, Height = 68 mm

**Weight:** 215 g (0.47 lb)

---

## GI CONNECTION DIAGRAM

### 6.1 Terminal Designation

| Terminal | Description |
|----------|-------------|
| L1 | Voltage Input (Phase R) |
| L2 | Voltage Input (Phase S) |
| L3 | Voltage Input (Phase T) |
| 6 | Trip Relay |
| 7 | Common |
| 8 | Aux. Relay (Alarm) |

**Relay States:**
- 7-8 Connected: Tripped
- 7-8 Open: Normal
- 6-7 Open: Tripped
- 6-7 Connected: Normal

### 6.2 Basic Diagram Installation

**WARNING (Risk of Electric Shock):** Disconnect power line supply before installing GI. Electric shock will result in death or serious injury.

**CAUTION:** Check that the voltage of chosen GI model corresponds to line voltage.

#### Wiring Recommendations

- Avoid over tightening M3 screws upon terminals during wiring connection. Torque max. 4.4 Ib-in (5.06 Kgf-cm)
- Wire Strip Length: 6-7 mm
- Terminal wiring size: ≥ AWG10 (4 mm²) ≤ AWG18
- Connect L1 L2 L3 terminal for Voltage Input in parallel connection before starter circuit through Contactor

---

## ADJUSTMENT

**ATTENTION:** Any accidental or intentional change of setting knobs positions after they have been adjusted shall cause variation on GI protective performance respect to previous setting up. In this case repeat procedure for GI adjustment indicated in this section.

### Adjustment Procedure

a) Turn OFF the circuit breaker.

b) Slide the AUTO/MANUAL start mode slide-switch to MANUAL position.

**NOTE:** Make sure that wiring is according to connection diagram.

c) Turn the minimum (VMIN) and maximum (VMAX) voltage setting knobs to desired voltage threshold levels. Use a screwdriver.

d) Turn Trip Delay (TD) setting knob to the desired disconnection time (seconds) according to your application needs. TD is the time between voltage fault detection and tripping.

**NOTE:** Typical value: 3 seconds

e) Turn the Start Delay (TC) setting knob to the desired start up delay, according to your application needs. TC is the time between voltage fault recovery and restarting.

f) Use AUTO/MANUAL start mode slide-switch to select the desired start mode.

g) In case the AUTO/MANUAL start mode slide-switch is set on MANUAL, press START push button. In case the selected start mode is Automatic, wait for the Start up Delay and the load starting.

---

## GENIUS GI OPERATION

GI constantly supervises line voltages values; when any harmful condition occurs, the output is deactivated until the fault disappears and power line conditions return to acceptable levels. Start Up Delay (TC) and Trip Delay (TD) are incorporated to prevent nuisance tripping due to rapid power fluctuations.

GI provides four (4) setting knobs for adjustments in order to select maximum and minimum allowed voltage (VMAX and VMIN), the trip delay (TD) and the start delay (TC). One Start push-button (START) and one selectable AUTO/MANUAL start mode slide-switch are included, as well as a Communication Port with MODBUS RTU protocol.

### Failures Description and Indicator Lights

| Failure Type | Continuous Light | Blinking Light |
|--------------|------------------|----------------|
| Normal Conditions (ON) | Green Led | - |
| Phase Reversal (PR) | Red Led | - |
| Voltage Unbalance (VUB) | Red Led | - |
| Single Phasing (SP) | - | Red Led |
| Overvoltage (OV) | Red Led | - |
| Undervoltage (UV) | - | Red Led |
| Start Delay (TC) | - | Green Led |

**Note:** When the GI has been set on MANUAL start mode, the indicator lights (LED Red 1, LED Red 2, LED Red 3) will be scrolling sequentially, after the start up delay (TC) is over. This condition stays until the User presses the START Push Button.

---

## DISMOUNTING INSTRUCTIONS

**WARNING:** Disconnect power supply (Circuit Breaker OFF) and electrical wiring before dismounting GI. Electrical shock would result in death or serious injury.

### 9.1 Instructions for Mechanical Dismounting (DIN RAIL)

a) Handling a Flat Screwdriver, pull downward the mounting bracket that you can see at rear and down side of GI, as shown in figure.

**Recommendation for DIN Rail Dismounting:** Pull downward 2 mm with a soft movement when using screwdriver for dismounting. Strong movement could break the supporting bracket.

### 9.2 Instructions for Mechanical Dismounting (FLAT SURFACE)

a) Unscrew both screws fixed on Flat Surface through attachable mounting ears and then pull out the GI relay from flat surface.

---

## TECHNICAL SPECIFICATIONS

### A) Power Supply Circuit

| Parameter | Specification |
|-----------|--------------|
| Rated Voltage (Ue) | 120 / 208 / 220 / 380 / 440 / 480 VAC |
| Voltage Operation Limits (Ue) | 72→168 / 124→308 / 228→532 / 264→672 VAC |
| Average Consumption (In) | 44 mA |
| Frequency Operation Limits (Fn) | 42→70 Hz / 50/60 Hz |
| Rated Duty | Uninterrupted Duty |

### B) Application Data, Environmental Conditions, Operation Limits and Installing

| Parameter | Value | Standard |
|-----------|-------|----------|
| Designed according to European Standards | IEC60947-1 LVD & EMC | - |
| Designed according to US Standards | UL (pending), NKCR, Auxiliary Devices UL508 | - |
| CE Marking | CE (pending), Low Voltage Devices IEC60947-1 | - |
| Ambient Air Temperature (Operation) | -5°C to 55°C (23°F to 131°F) | - |
| Ambient Air Temperature (Storage) | -10°C to +70°C (14°F to 158°F) | - |
| Maximum Relative Humidity | 85% R.H. | - |
| Vibrations | Class 1, Amplitude <0.035 mm or 1G, 10Hz < f < 150Hz | IEC 60255-21-1 |
| Shocks | Class 1, <1560 m/s² | IEC 60255-21-2 |
| Seismic | Class 1, Amplitude <3.5 mm or 1G, 1Hz < f < 35Hz | IEC 60255-21-3 |
| Degree of Protection | IP20, Protected against objects > 12.5 mm, but no protection against water | IEC 60529 |
| Pollution Degree | Degree 3 | IEC 60255-5 |
| Overvoltage Category | Category III, 4KV | IEC 60255-5 |
| Rated Insulation Voltage | 500 V | IEC 60255-5 |
| Impulse Voltage Test | 5 KV | IEC 60255-5 |
| Impulse Dielectric Test | 2 KV 50/60 Hz @ 1 min | UL 508 |
| Flammability Rating of Enclosure | V0 | UL94 |
| Enclosure Material | Polymers: LEXAN 500R, ABS, Nylon | - |
| Mounting Position | Any Position | - |
| Mounting Features | Symmetrical DIN Rail / Flat surface mounting, screw 3/16" x 1/2" | DIN 43880 / NEMA Style |
| Terminals | Screw Type Flat M3, Torque 5.06 Kgf-cm / 4.4 Ib-in, Wire Size ≥10 AWG (4 mm²) ≤18 AWG | - |

### C) Control Characteristics

| Parameter | Specification | Standard |
|-----------|--------------|----------|
| Output Contact Rating | 3 A @ 240 VAC, 1.5 A @ 480 VAC | UL 508, Section 1391 |
| Electrical Life Expectancy | 100,000 Operations | - |
| Mechanical Life Expectancy | 10,000,000 Operations | - |
| Utilization Category | AC-15, Capacity for loads > 72 VA | IEC 60947-5-1 |

### D) Range Setting, Measuring

| Parameter | Voltage Model | Value | Unit |
|-----------|--------------|-------|------|
| Voltage Measurement Range (Um) | 120 | 72→163 | VAC |
| | 208/220 | 128→300 | VAC |
| | 380 | 228→532 | VAC |
| | 440/480 | 276→645 | VAC |
| Frequency Measurement Accuracy (Parameter available only through GIO Port) | All models | ±2% | - |

### E) Algorithms and Protection Functions

| Function | 120 VAC | 208/220 VAC | 380 VAC | 440/480 VAC | Unit |
|----------|---------|------------|---------|------------|------|
| Undervoltage (UV) | 80→115 | 145→200 | 260→370 | 300→420 | Settings Level |
| Overvoltage (OV) | 120→155 | 230→285 | 390→500 | 500→625 | Settings Level |
| Voltage Hysteresis Threshold | 3 | 6 | 10 | 12 | VAC |
| Voltage Unbalance Detection (VUB) | IN +/-8%, OUT +/-6% | - | - | - | - |
| Voltage Single Phasing (VSP) | IN VUB > 33%, OUT VUB < 28% | - | - | - | - |
| Phase Reversal (PR) | Normal Sequence ABC, reversal sequence CBA | - | - | - | - |
| Trip Delay because of Phase Reversal | < 1 sec | - | - | - | - |
| Trip Delay because of another voltage Failures (TD) | 0.55 sec | - | - | - | Settings Level |
| Start up Delay (TC) | 5→300 sec | - | - | - | Settings Level |
| Start Mode | Auto/Manual Switch selection | - | - | - | - |

### F) Communications and Other Special Functions

| Function | Specification |
|----------|--------------|
| Communication Protocol | MODBUS RTU @ 9600 8N1 |
| Communication Ports | GIO PORT (*) |
| History Buffer Memory | 20 last fault reports |

(*) GIO Plug is required for GIO Port communication. It is available by separated.

### G) Immunity and Emissions, Electromagnetic Compatibility (EMC) for Heavy Industrial Environment (B)

| Test | Standard |
|------|----------|
| Electrostatic Discharge | IEC 61000-4-2 |
| Immunity to Radio Frequency Test | IEC 61000-4-3 |
| Electrical Fast Transients | IEC 61000-4-4 |
| Surge Immunity Test | IEC 61000-4-5 |
| Radio-Frequency Continuous Conducted | IEC 61000-4-6 |
| Power Frequency Magnetic Field | IEC 61000-4-8 |
| Voltage Dips, Short Interruptions and Voltage Variations | IEC 61000-4-11 |
| Harmonics and Interharmonics | IEC 61000-4-13 |
| Voltage Fluctuation Immunity | IEC 61000-4-14 |
| Unbalance Immunity Test | IEC 61000-4-27 |
| Variation of Power Frequency | IEC 61000-4-28 |
| Electrical (Burst) Disturbance Test | IEC 60255-22-1 |
| Conducted Common Mode Disturbances (0→150 kHz) | IEC 61000-4-16 / IEC 60255-22-7 |
| Electromagnetic Disturbance Characteristics | CISPR 11 |
| Limits for Harmonic Current Emissions | IEC 61000-3-2 Table 1 |
| Limitation of Voltage Fluctuations and Flicker in low-voltage Supply Systems | IEC 61000-3-3 |

---

## HOW TO ORDER

**Product Code Format:** GI - [VOLTAGE] - [LANGUAGE]

### Voltage Options
- 120 — 120 VAC
- 208 — 208/220 VAC
- 380 — 380 VAC
- 480 — 440/480 VAC

### Language Options
- S — SPANISH
- E — ENGLISH
- P — PORTUGUESE

---

## MANUFACTURER INFORMATION

**Generación de Tecnología, c.a.**

**Headquarters:**
Av. El Buen Pastor c/c Vargas, Edif. Alba, Piso 1, Oficina 1-A, Boleíta Norte, Caracas - Venezuela

**Contact Information:**
- Telfs.: (0212) 237.0711 / 1151 / 3477 / 238.7006
- Fax: 235.2497
- E-mail: genteven@genteca.com.ve
- Website: www.genteca.com.ve

**USA Office:**
Buzzom ACSA 0158, P.O. Box 28537, Miami, FL 33102, USA
