---
title: "Relayne GOC - Electronic Motor Protection Relay Installation Manual"
type: Technical
source: "GD-MAN-050-01-V2-US-C.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GOC"
version_status: "historica"
date_processed: "2026-05-10"
---

# Relayne GOC Electronic Motor Protection Relay

## General Description

GOC is an electronic Motor Protection Relay that constantly supervises motor current and power supply voltage, using a thermal model algorithm to protect your motor against overload conditions and voltage failures.

**WARNING:** Only qualified technicians with knowledge about overload relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

**WARNING:** This product may start automatically; the user must take cautions to avoid hazards to people.

## GOC Parts and Pieces

### Indicator Lights (LED's)
- Normal (ON) - Continuous Green
- Start Delay (TC) - Blinking Green
- Overload (OL) - Continuous Red
- Phase Reversal (PR) - Blinking Red
- Unbalance (UB) - Continuous Red
- Single Phasing (SP) - Blinking Red
- Overvoltage (OV) - Continuous Red
- Undervoltage (UV) - Blinking Red

### Components
1. Current (FLA) Setting Knob
2. Start Delay (TC) Setting Knob
3. Back Groove for DIN Rail mounting
4. Attachable Mounting Ear for Flat Surface mounting
5. Supporting Brackets for DIN Rail mounting
6. Current Sensing Holes for motor wiring
7. Power Supply Voltage Input (L1 L2 L3)
8. Contacts for Relay (95-96) and (97-98)
   - 95-96 connected / 97-98 open (Tripped)
   - 95-96 open / 97-98 connected (Normal)
9. GIO Port (for Serial Communication)
10. AUTO / MANUAL Start Mode Slide-Switch
11. START Push Button
12. GIO PORT cover

## DIN Rail Mounting

**CAUTION:** GOC must be installed in an accessible position free from dust, dirt, dampness and vibration. Allow enough space for air circulation around the enclosure and easy access to all operator controls. Indoors use only.

### Instructions for Mechanical Installation

a) Place GOC at inclined position with its back side placed toward the upper edge of the DIN Rail and push down GOC relay until it does CLICK on the rail.

**CAUTION:** This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

**CAUTION:** An incorrectly applied or installed GOC can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the GOC.

## Flat Surface Mounting

### Instructions for Mechanical Installation

a) Take off the two (2) attachable mounting ears located at back side of GOC, insert and slip both attachable mounting ears into the GOC back side grooves.

b) Place GOC over flat surface panel and fix it handling a screwdriver suitable for screws 3/16" x 1/2".

**Recommendation for Flat Surface Mounting:** Make two (2) holes (5/32") on panel surface before installing.

## GOC General Dimensions

- Height: 92 mm
- Width: 72 mm
- Depth: dimensions shown in reference guide for flat surface mounting

## Connection Diagrams

### 6.2.1 208/220 VAC Models

```
L1 L2 L3
RST
CIRCUIT
BREAKER
CONTACTOR
FUSES: 5A, 600V
GOC
Auto/Manual Mode Selection
GIO Port
Alarm output terminals (95-96, 97-98)
```

### 6.2.2 440/480 VAC Models

Requires auxiliary control voltage from 24 to 250 VAC.

```
Li L2 L3
Auxiliary Control Voltage: 24 to 250 VAC
CIRCUIT BREAKER
FUSES: 5A, 600V
GOC
Auto/Manual Mode Selection
GIO Port
Alarm output terminals
```

## Terminal Designation

| Terminal | Description |
|----------|-------------|
| L1 | Voltage Input (Phase R) |
| L2 | Voltage Input (Phase S) |
| L3 | Voltage Input (Phase T) |
| 95 | Contact for Auxiliary Relay |
| 96 | Auxiliary Relay |
| 97 | Contact for Trip Relay |
| 98 | Trip Relay |

**Contact States:**
- 95-96 Connected / 97-98 Open (Tripped)
- 95-96 Open / 97-98 Connected (Normal)

### Wiring Recommendations

- *Avoid over tightening the M3 screws upon terminals during wiring connection. Torque max. 4.4 Ib-in (5.1 Kgf-cm).
- Wire Strip Length: 6-7 mm
- Terminal wiring size: >AWG 10 (4mm²) <AWG 18
- Current Sensing Holes (conduits) wiring size: > AWG 4 (11mm)
- Connect L1 L2 L3 terminal for Voltage Input in parallel connection before line starter circuit through Contactor
- Use three Current Sensing Holes for passing wires before connection to 3 phases motor. Using less than three (3) wires shall cause current unbalance wrong measures.

## Adjustment Procedure

### 7.1 Procedure for Overload Adjustment

a) Turn OFF the circuit breaker.

**CAUTION:** By means of an Ammeter, make sure that the Operational Current (I) is less than FLA (Full Load Amperes) indicated at the motor nameplate. Failure to comply may result in damage to the motor.

**ATTENTION:** Any accidental or intentional change of setting knobs positions after overload adjustment, shall cause variation on GOC protective performance respect to previous setting up. In this case repeat procedure for GOC adjustment.

**ATTENTION:** You should follow this procedure with the motor running at full load conditions, according to the rated values indicated on Motor Name Plate.

**NOTE:** Make sure that wiring is according to connection diagram.

b) Slide the AUTO/MANUAL start mode slide-switch to MANUAL position.

c) Turn ON the circuit breaker. (The motor remains OFF due to Contactor is open by means of GOC deactivation).

e) Press the START push button and hold it pressed (motor starts running and reach to steady-state operation) while you execute steps (f) and (g).

f) Slowly turn left the Current setting knob (FLA) until the green LED turns ON. At this point, the adjusted level is the actual Motor Operational Current.

g) Slowly turn right the Current setting knob (FLA) up to desired protection level:
- Green Led ON = In → 0A 225%
- Red Led 1 ON = Overload 10%
- Red Led 2 ON = Overload 15%
- Red Led 3 ON = Overload 20%

h) Use AUTO/MANUAL start mode slide-switch to select the desired motor start mode.

**NOTICE:**

In case the AUTO/MANUAL start mode slide-switch is set on MANUAL and the GOC relay trips due to any fault detection, you shall press START push button to re-activate the Contactor or Line Starter Circuit.

Although the AUTO/MANUAL start mode slide-switch is set on AUTO, pressing START push button is required if three (3) current failures have appeared in less than 30 minutes and qualified technicians have detected and solved causes of failures.

i) Using a flat screwdriver, turn the TC setting knob until you set the start delay desired (TC is the time between Voltage fault recovery and restart the system according to application needs).

## Relayne GOC Operation

Relayne GOC constantly supervises motor current and line voltage. When any harmful condition occurs, the output is deactivated until the fault disappears and the motor has completely cooled. Specific timing such as Start Up Delay (TC) are incorporated for automatic restart mode, to prevent nuisance tripping due to rapid power fluctuations. In the event of three current failures occurs in less than 30 minutes, the output is deactivated until manual restart is done. Checking causes of three successive failures is recommended before restarting.

Relayne GOC provides two (2) setting knobs to select the maximum allowed current (FLA) and the start up delay (TC) once the voltage fault and/or overload disappears. One START push-button and one selectable AUTO/MANUAL Start Mode Slide-Switch are included as well as a Communication Port with ModBus RTU protocol.

### Failures Description and Indicator Lights

| Condition | Continuous Light | Blinking Light |
|-----------|------------------|----------------|
| Normal (ON) | Green Led | - |
| Start Delay (TC) | - | Green Led |
| Overload failure (OL) | Red Led 1 | - |
| Phase Reversal failure (PR) | - | Red Led 1 |
| Voltage Unbalance or Current Unbalance failure (UB) | Red Led 2 | - |
| Voltage Single Phasing or Current Single Phasing failure (SP) | - | Red Led 2 |
| Overvoltage failure (OV) | Red Led 3 | - |
| Undervoltage failure (UV) | - | Red Led 3 |

**NOTICE:** When GOC has been set on MANUAL Start Mode, the indicator lights (Red LED 1, Red LED 2, Red LED 3) will be scrolling sequentially after the Start Delay (TC) is over. This condition stays until User presses the START Push button in order to restarting.

## GOC Dismounting Instructions

**WARNING:** Disconnect power supply (Circuit Breaker OFF) and electrical wiring before dismounting GOC. Electrical shock will result in death or serious injury.

### 9.1 Instructions for Mechanical Dismounting (DIN RAIL)

a) Handling a Flat Screwdriver, pull downward the mounting bracket that you can see at rear and down side of GOC.

b) With screwdriver at position (2), pull out GOC from DIN Rail.

**Recommendation for DIN Rail Dismounting:** Pull downward 2 mm with a soft movement when using screwdriver for dismounting. Strong movement could break the supporting bracket.

### 9.2 Instructions for Mechanical Dismounting (FLAT SURFACE)

a) Unscrew both screws fixed on Flat Surface through attachable mounting ears and then pull out the GOC relay from flat surface.

## GOC Technical Specifications

### A) Power Supply Circuit

| Parameter | 208/220 VAC | 440/480 VAC |
|-----------|------------|-----------|
| Rated Voltage, Ue | 208/220 | 440/480 VAC |
| Voltage Operation Limits, Ue | 124→300 | 264→672 VAC |
| Average Consumption, In | 38 mA | - |
| Frequency Operation Limits, Fu | 42→70 Hz | 50/60 Hz |
| Rated Duty | Uninterrupted Duty | - |

### B) Application Data, Environmental Conditions, Operation Limits and Installing

| Item | Specification | Standard |
|------|---------------|----------|
| b.1 | Designed according to IEC61010-1, IEC60255-6 LVD & EMC European Standards IEC60947-1 | - |
| b.2 | UL Listing: Aux. Device NKCR Certified for USA; Aux. Device NKCR7 Certified for Canada | 800808 |
| b.3 | CE Marking CE (pending), Low Voltage Devices | IEC60947-1 |
| b.4 | Ambient Air Temperature (Operation) | -5 °C to 55 °C (23 °F to 131 °F) |
| b.5 | Ambient Air Temperature (Storage) | -10 °C to +70 °C (14 °F to 158 °F) |
| b.6 | Maximum Relative Humidity | 85% R.H. |
| b.7 | Vibrations | Class 1, in accordance with 1G soon |
| b.8 | Degree of Protection | IP20, Protected against objects > 12.5 mm | IEC 60529 |
| b.9 | Pollution Degree | Degree 3 | IEC 60255-5 |
| b.10 | Overvoltage Category | Category III | IEC 60255-5 |
| b.11 | Rated Insulation Voltage | 500V | According to UL |
| b.12 | Impulse Voltage Test | 5 KV | IEC 60255-5 |
| b.13 | Dielectric Voltage-Withstand Test | 2.5 KV 50/60 Hz @ 1 min | UL 508 |
| b.14 | Flammability Rating of Enclosure | V0 | UL-94 |
| b.15 | Enclosure Material | Polymers: PC, ABS, NYLON | - |
| b.16 | Mounting Position | Any Position | - |
| b.17 | Mounting Features | Symmetrical DIN Rail, Flat surface mounting, screw 3/16" x 1/2" | NEMA Style |
| b.18 | Tightening Screw Torque | 5.1 Kgf-cm / 4.4 Ib-in | - |
| b.19 | Terminals Wiring | >10 AWG (4mm²) <18 AWG | - |
| b.20 | Current Sensing Holes for Motor Wiring | < 11 mm, AWG 4 | - |

### C) Control Characteristics

| Item | Parameter | Value | Standard |
|------|-----------|-------|----------|
| c.1 | Auxiliary Relay Contact Rating | Pilot Duty | - |
| c.2 | Electrical Life Expectancy | 100,000 Operations | - |
| c.3 | Mechanical Life Expectancy | 10,000,000 Operations | - |
| c.4 | Utilization Category | AC-15, Capacity for loads > 72 VA | IEC60947-5-1 |

### D) Range Setting, Measuring (available only through GIO Port)

| Item | Parameter | 208 VAC | 480 VAC |
|------|-----------|---------|---------|
| d.1 | Voltage Measurement Range, Um | 145-285 | 300-625 VAC |
| d.2 | Current Adjust (FLA) by Model | 1-4, 5-3, 10-32, 25-80 | A (Level settings) |
| d.3 | Frequency Measurement | Parameter Accuracy +/- 2% | Hz |

### E) Algorithms and Protection Functions (According to Voltage Model)

| Function | Specification | Standard |
|----------|---------------|----------|
| Undervoltage (UV) @ Imotor=0 or OL | VAC value | - |
| Overvoltage (OV) @ Imotor=0 or OL | VAC value | - |
| Voltage Hysteresis Threshold | 12 VAC | - |
| Current Adjust (FLA) by Model | 1-4, 5-3, 10-32, 25-80 A (Level settings) | - |
| Voltage Unbalance Detection (VUB) | IN +/-8%, OUT +/-6% | - |
| Single Phasing (VSP) | INV VUB > 33%, OUT VUB < 28% | - |
| Phase Reversal (PR) | Normal Sequence ABC, reversal sequence CBA | - |
| Current Unbalance (CUB) | CUB > 48% | - |
| Current Single Phasing (CSP) | CUB > 60% | - |
| Thermal Class | Cold Curve: 10, Hot Curve: 3 According to the previous level of load and time of operation | IEC 60255-8-1990 |
| Trip Delay because of Overload (OL) | According to Overload Level (Inverse Time Current) | IEC 60255-8-1990 |
| Permanent disconnection because of Third Current Failure | 3 Current Failures in less than 30 min | IEEE Std. 037.112-1996 |
| Trip Delay because of Phase Reversal | <1 sec | - |
| Trip Delay because of Another Voltage Failures | 3 sec | - |
| Start Up Delay because of Cooling (Thermal Mode) | 480 sec | - |
| Start Up Delay (TC) | 5 – 300 sec Level settings | - |
| Start Mode | Auto/Manual | - |

### F) Communications and Other Special Functions

| Item | Parameter | Specification |
|------|-----------|---------------|
| f.1 | Communication Protocol | MODBUS RTU @ 9600 8N1 |
| f.2 | Communication Ports | GIO PORT (*) |
| f.3 | History Buffer Memory | 20 last fault report |

(*) GIO Plug is required for GIO Port communication. It is available by separated.

### G) Immunity and Emissions, Electromagnetic Compatibility (EMC) for Heavy Industrial Environment (B)

| Item | Test | Standard |
|------|------|----------|
| g.1 | Electrostatic Discharge | IEC 61000-4-2 |
| g.2 | Immunity to Radio Frequency Test | IEC 61000-4-3 |
| g.3 | Electrical Fast Transients | IEC 61000-4-4 |
| g.4 | Surge Immunity Test | IEC 61000-4-5 |
| g.5 | Radio-Frequency Continuous Conducted | IEC 61000-4-6 |
| g.6 | Power Frequency Magnetic Field | IEC 61000-4-8 |
| g.7 | Voltage Dips, Short Interruptions and Voltage Variations | IEC 61000-4-11 |
| g.8 | Harmonics and Interharmonics Immunity Tests | IEC 61000-4-13 |
| g.9 | Voltage Fluctuation Immunity | IEC 61000-4-14 |
| g.10 | Unbalance Immunity Test | IEC 61000-4-27 |
| g.11 | Variation of Power Frequency | IEC 61000-4-28 |

## GOC Cold-Hot Curves

The trip time characteristics follow thermal curves according to IEC 60255-8-1990:
- **Cold Curve:** Class 10
- **Hot Curve:** Class 3

Trip time varies based on the ratio of load current (I load) to nominal current (I nom), which is the current value on GOC adjusted previously by the user. The I nom term is referred to FLA (Full Load Amperage) adjustable on the product.

## How to Order

**GOC MODEL CODE FORMAT:**

| Position | Parameter | Options |
|----------|-----------|---------|
| 1 | Number of Phases | T = 3 Phases |
| 2-3 | Voltage | 208 = 208/220 VAC; 480 = 440/480 VAC |
| 4 | Amperage | 04 = 1-4A; 5 = 5-3OOA; 50 = 10-32A; 80 = 25-80A |
| 5 | Language | S = Spanish; E = English; P = Portuguese |

## Manufacturer Information

Made and designed by Genteca, Generación de Tecnología C.A.  
R.I.F: J-00223173-4  
Av. El Buen Pastor, cruce con Calle Vargas, Edificio Alba, Piso 1, Local 1-A  
Boleita Norte, Caracas, 1070, República Bolivariana de Venezuela  
Phone: +58-212-237.071 (Master)  
Fax: +58-212-235.2497  
E-mail: genteven@genteca.com.ve  
Website: www.genteca.com.ve

**Distributed in USA by:**  
Miami Breaker INC.  
7060 Nw. 52nd Street  
Miami-Florida 33166, USA  
Phone: +1-786-3365780

**Note:** Technical data are valid at the time of printing. We reserve the right to subsequent alterations.
