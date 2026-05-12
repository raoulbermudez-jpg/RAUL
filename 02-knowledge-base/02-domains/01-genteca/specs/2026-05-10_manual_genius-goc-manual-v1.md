---
title: "GOCT General Description and Installation Manual"
type: Technical
source: "GOC MANUAL V1.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GOCT"
version_status: "historica"
date_processed: "2026-05-10"
---

# GOCT General Description

GOCT is an electronic Motor Protection Relay that constantly supervises motor current and power supply voltage, using a thermal model algorithm to protect your motor against overload conditions and voltage failures (see more details in User Manual).

**WARNING:** Only qualified technicians with knowledge about overload relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

**CAUTION:** This product may start automatically, the user must take cautions to avoid hazards to people.

## GOCT Parts and Pieces

### Front Side View

1. Indicator Lights (LED's)
   - Normal (ON) - Continuous Green
   - Start Delay (TC) - Blinking Green
   - Overload (OL) - Continuous Red
   - Phase Reversal (PR) - Blinking Red
   - Unbalance (UB) - Continuous Red
   - Single Phasing (SP) - Blinking Red
   - Overvoltage (OV) - Continuous Red
   - Undervoltage (UV) - Blinking Red

2. Current (FLA) Setting Knob
3. Start Delay (TC) Setting Knob
4. Back Groove for DIN Rail mounting
5. Attachable Mounting Ear for Flat Surface mounting
6. Supporting Brackets for DIN Rail mounting
7. Current Sensing Holes for motor wiring
8. Power Supply Voltage Input (L1 L2 L3)
9. Contacts for Relay (95-96) and (97-98)
10. GIO Port (for Serial Communication)
11. AUTO / MANUAL Start Mode Slide-Switch
12. START Push Button
13. GIO PORT cover

### Relay Contact Configuration

- 95-96 connected / 97-98 open: Tripped
- 95-96 open / 97-98 connected: Normal

## GOCT DIN Rail Mounting

**CAUTION:** GOCT must be installed in an accessible position free from dust, dirt, dampness and vibration. Allow enough space for air circulation around the enclosure and easy access to all operator controls. Indoors use only.

### Instructions for Mechanical Installation

Place GOCT at inclined position with its back side placed toward the upper edge of the DIN Rail and push down GOCT relay until it clicks on the rail.

**CAUTION:** This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

**CAUTION:** An incorrectly applied or installed GOCT can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the GOCT.

## GOCT Flat Surface Mounting

### Instructions for Mechanical Installation

a) Take off the two (2) attachable mounting ears located at back side of GOCT, insert and slip both attachable mounting ears into the GOCT back side grooves.

b) Place GOCT over flat surface panel and fix it using a screwdriver suitable for screws 3/16" x 1/2".

**Recommendation for Flat Surface Mounting:** Make two (2) holes (5/32") on panel surface before installing.

## GOCT General Dimensions

- Height: 91 mm
- Width: 11 mm
- Depth: 96 mm (total dimensions: 92 x 91 x 96 mm L x W x H)

Guide for flat surface mounting shows mounting ear positions on 72 mm x 92 mm reference grid.

## GOCT Connection Diagram

**WARNING:** (Risk of Electric Shock). Disconnect power supply before installing GOCT. Electric shock will result in death or serious injury.

**CAUTION:** Check that the voltage and current of chosen GOCT model correspond to line voltage and motor current.

### 6.1 Terminal Designation

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
- 95-96 Connected / 97-98 Open: Tripped
- 95-96 Open / 97-98 Connected: Normal

### 6.2 Basic Diagram Installation

#### 6.2.1 208/220 VAC Models

Connection diagram shows:
- Three-phase input (L1, L2, L3)
- Circuit breaker
- Contactor with fuses (5A, 600V recommended)
- GOCT relay with manual/auto mode selection
- GIO port connection
- Alarm output

#### 6.2.2 440/480 VAC Models

Requires auxiliary control voltage from 24 to 250 VAC connected to the GOCT relay circuit.

### Recommendations for Wiring

- Avoid over tightening the M3 screws upon terminals during wiring connection. Tightening Torque: 4.4 Ibf-in, 5.1 Kgf-cm
- Wire Strip Length: 6-7 mm
- Terminal wiring size: > AWG 10 (4mm²) < AWG 18
- Current Sensing Holes (conduits) wiring size: 2 AWG 4 (11mm)
- Connect L1L2L3 terminal for Voltage Input in parallel connection before line starter circuit through Contactor
- Use three Current Sensing Holes for passing wires before connection to 3-phase motor. Using less than three (3) wires shall cause current unbalance and wrong measures.

## Adjustment

### Procedure for Overload Adjustment

**CAUTION:** By means of an Ammeter, make sure that the Operational Current (I) is less than FLA (Full Load Amperes) indicated at the motor nameplate. Failure to comply may result in damage to the motor.

**ATTENTION:** Any accidental or intentional change of setting knobs positions after overload adjustment, shall cause variation on GOCT protective performance respect to previous setting up. In this case repeat procedure for GOCT adjustment.

**ATTENTION:** You should follow this procedure with the motor running at full load conditions, according to the rated values indicated on Motor Name Plate.

**Procedure Steps:**

a) Turn OFF the circuit breaker.

b) Slide the AUTO/MANUAL start mode slide-switch to MANUAL position.

c) Turn ON the circuit breaker. (The motor remains OFF due to Contactor being open by means of GOCT deactivation).

d) Press the START push button and hold it pressed (motor starts running and reaches steady-state operation) while you execute steps (f) and (g).

e) Slowly turn left the Current setting knob (FLA) until the green LED turns ON. At this point, the adjusted level is the actual Motor Operational Current.

f) Slowly turn right the Current setting knob (FLA) up to desired protection level:
   - Green LED ON = In adjustment
   - Red LED 1 ON = Overload 10%
   - Red LED 2 ON = Overload 15%
   - Red LED 3 ON = Overload 20%

g) Use AUTO/MANUAL start mode slide-switch to select the desired motor start mode.

**NOTICE:**

In case the AUTO/MANUAL start mode slide-switch is set on MANUAL and the GOCT relay trips due to any fault detection, you shall press START push button to re-activate the Contactor or Line Starter Circuit.

Although the AUTO/MANUAL start mode slide-switch is set on AUTO, pressing START push button is required if three (3) current failures have appeared in less than 30 minutes and qualified technicians have detected and solved causes of failures.

### Procedure for TC Adjustment

Using a flat screwdriver, turn the TC setting knob until you set the start delay desired (TC is the time between Voltage fault recovery and restart the system according to application needs).

## GOCT Operation

Relayne GOCT constantly supervises motor current and line voltage. When any harmful condition occurs, the output is deactivated until the fault disappears and the motor has completely cooled. Specific timing such as Start Up Delay (TC) are incorporated for automatic restart mode, to prevent nuisance tripping due to rapid power fluctuations. In the event of three current failures occurs in less than 30 minutes, the output is deactivated until manual restart is done. Checking causes of three successive failures is recommended before restarting.

Relayne GOCT provides:
- Two (2) setting knobs to select the maximum allowed current (FLA) and the start up delay (TC)
- One START push-button
- One selectable AUTO/MANUAL Start Mode Slide-Switch
- Communication Port with ModBus RTU protocol
- Indicator lights (LEDs) to indicate faults and load status

### Failures Description and Indicator Lights

| Fault Condition | Continuous Light | Blinking Light |
|-----------------|------------------|-----------------|
| Normal operation | Green LED | - |
| Start Delay | - | Green LED (TC) |
| Overload | Red LED 1 | Phase Reversal |
| Voltage Unbalance / Current Unbalance | Red LED 2 | Single Phasing |
| Overvoltage | Red LED 3 | Undervoltage |

Relayne GOCT also indicates any combination of fault conditions. For more information see Relayne GOCT User Manual.

**NOTICE:** When GOCT has been set on MANUAL Start Mode or the GOCT has stopped because of the event of three current failures in less than 30 minutes, the indicator lights (Red LED 1, Red LED 2, Red LED 3) will be scrolling sequentially after the START DELAY (TC) is over. This condition stays until user presses the START Push button in order to restarting.

## GOCT Dismounting Instructions

**WARNING:** Disconnect power supply (Circuit Breaker OFF) and electrical wiring before dismounting GOCT. Electrical shock will result in death or serious injury.

### 9.1 Instructions for Mechanical Dismounting (DIN Rail)

a) Using a Flat Screwdriver, pull downward the mounting bracket that you can see at rear and down side of GOCT.

b) With screwdriver at position (2), pull out GOCT from DIN Rail.

**Recommendation for DIN Rail Dismounting:** Pull downward 2 mm with a soft movement when using screwdriver for dismounting. Strong movement could break the supporting bracket.

### 9.2 Instructions for Mechanical Dismounting (Flat Surface)

a) Unscrew both screws fixed on Flat Surface through attachable mounting ears and then pull out the GOCT relay from flat surface.

## GOCT Technical Specifications

### A) Power Supply Circuit

| Parameter | Specification |
|-----------|---------------|
| Rated Voltage, Ue | 208/220 VAC, 440/480 VAC |
| Voltage Operation Limits, Ue | 124-300 VAC (208/220) / 264-672 VAC (440/480) |
| Average Consumption, In | 38 mA |
| Normal Frequency | 50/60 Hz |
| Frequency Operation Limit | 42-70 Hz |
| Rated Duty | Uninterrupted Duty |

### B) Application Data, Environmental Conditions, Operation Limits and Installing

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| Designed according to | IEC61010-1, IEC60255-6, IEC60255-8-1990, IEC60947-1 | - |
| UL Listing Aux. Device NKCR | Certified for USA E300908 | - |
| UL Listing Aux. Device NKCR7 | Certified for CANADA | - |
| CE Marking | CE (pending), Low Voltage Devices | IEC60947-1 |
| Ambient Air Temperature (Operation) | -5 °C to 55 °C (23 °F to 131 °F) | - |
| Ambient Air Temperature (Storage) | -10 °C to +70 °C (14 °F to 158 °F) | - |
| Maximum Relative Humidity | 85% R.H. | - |
| Vibrations | Class 1, Amplitude <0.035mm or 1G, 10Hz <f <150Hz | IEC 54 |
| Degree of Protection | IP20, Protected against objects > 12.5mm | IEC 60529 |
| Pollution Degree | Degree 3 | IEC 60255-5 |
| Overvoltage Category | Category II | IEC 60255-5 |
| Rated Insulation Voltage | 500V | According to UL |
| Impulse Voltage Test | 5 KV | IEC 60255-5 |
| Dielectric Voltage-Withstand Test | 2.5 KV 50/60 Hz@1min | UL 508 |
| Flammability Rating of Enclosure | V0 | UL-94 |
| Enclosure Material | Polymers: LEXAN 915R, Noryl HS 2000X or ABS AF 305, VYDYNE 21X | - |
| Mounting Position | Any Position | - |
| Mounting Features | Symmetrical DIN Rail (ECTS), Flat surface mounting, screw 3/16"x1/2" | - |
| Terminals | Screw Type Flat M3 | - |
| Tightening Screw Torque | 5.1 Kgf-cm / 4.4 Ibf-in | - |
| Terminals Wiring | >10 AWG (4mm²) <18 AWG | - |
| Current Sensing Holes for Motor Wiring | < 11mm, AWG 4 | - |
| Dimensions | 92 x 91 x 96 (L x W x H) mm | - |
| Weight | 398 g (0.87 lb) | - |

### C) Control Characteristics

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| Auxiliary Relay Contact Rating | 8300 Pilot Duty, 10A General Use, 277 VAC | UL 508, Section 139.1 |
| Electrical Life Expectancy | 100,000 Operations | - |
| Mechanical Life Expectancy | 10,000,000 Operations | - |
| Utilization Category | AC-15, Capacity for loads > 72 VA | IEC60947-5-1 |

### D) Range Setting, Measuring and Voltage Variations

| Parameter | 208 VAC | 480 VAC | Unit |
|-----------|---------|---------|------|
| Voltage Measurement Range, Um | 145-285 | 300-625 | VAC |
| Current Adjust (FLA) by Model | 1-4, 35-125 | 10-32, 25-80 | A |

**Frequency Measurement Accuracy:** ± 2% (Parameter available only through GIO Port)

### E) Algorithms and Protection Functions

| Protection Function | Specification | Standard |
|-------------------|---------------|----------|
| Undervoltage (UV) @ Imotor=0 or OL | 187 VAC (208) / 396 VAC (480) | IEC 60255-8-1990 |
| Overvoltage (OV) @ Imotor=0 or OL | 254 VAC (208) / 528 VAC (480) | - |
| Voltage Hysteresis Threshold | 6 VAC (208) / 12 VAC (480) | - |
| Voltage Unbalance Detection (VUB) | IN ±8%, OUT ±6% | - |
| Single Phasing (VSP) | IN VUB > 33%, OUT VUB < 28% | - |
| Phase Reversal (PR) | Normal Sequence ABC, reversal sequence CBA | - |
| Current Unbalance (CUB) | CUB > 48% | - |
| Current Single Phasing (CSP) | CUB > 60% | - |
| Thermal Class | Cold Curve: 10, Hot Curve: 3 | IEC 60255-8-1990, IEEE 37.112-1996 |
| Trip Delay because of Overload (OL) | According to Overload Level (Inverse Time Current) | IEC60947-1 |
| Permanent disconnection because of Third Current Failure | 3 Current Failures in less than 30 min | - |
| Trip Delay because of Phase Reversal | < 1 sec | - |
| Trip Delay because of Another Voltage Failures | 2 sec | - |
| Start Up Delay because of Cooling Level (Thermal Model) | 480 sec settings | - |
| Start Up Delay (TC) | 5 - 300 sec | - |
| Start Mode | Auto/Manual selection | - |

### F) Communications and Other Special Functions

| Feature | Specification | Reference |
|---------|---------------|-----------|
| Communication Protocol | MODBUS RTU @9600 8N1 | Manual |
| Communication Ports | GIO PORT (*) | Manual |
| History Buffer Memory | 20 last fault report | Manual |
| Allow Modbus Address | 1-127 | - |

(*) GIO Plug is required for GIO Port communication. It is an accessory available separately.

### G) Immunity and Emissions, Electromagnetic Compatibility (EMC) for Heavy Industrial Environment (B)

| Test | Standard |
|------|----------|
| Electrostatic Discharge | IEC 61000-4-2 |
| Immunity to Radio Frequency Test | IEC 61000-4-3 |
| Electrical Fast Transients | IEC 61000-4-4 |
| Surge Immunity Test | IEC 61000-4-5 |
| Radio-Frequency Continuous Conducted | IEC 61000-4-6 |
| Power Frequency Magnetic Field | IEC 61000-4-8 |
| Voltage Dips, Short Interruptions | IEC 61000-4-11 |
| Harmonics and Interharmonics Immunity Tests | IEC 61000-4-13 |
| Voltage Fluctuation Immunity | IEC 61000-4-14 |
| Unbalance Immunity Test | IEC 61000-4-27 |
| Variation of Power Frequency | IEC 61000-4-28 |

## GOCT Cold-Hot Curves

The thermal protection curves are graphically represented showing:
- Cold Curve: 10 seconds
- Hot Curve: 3 seconds

Where I load / I nom is the ratio of load current to nominal (adjusted FLA) current. I nom term is referred to FLA (Full Load Amperage) adjustable on the product.

## How to Order

**Model Code:** GOC-[Number of Phases]-[Voltage]-[Amperage]-[Language]

| Parameter | Code | Description |
|-----------|------|-------------|
| Number of Phases | T | 3 PHASES |
| Voltage | 208 | 208/220 VAC |
| | 480 | 440/480 VAC |
| Amperage | 04 | 1-4A |
| | 5 | 35-125A |
| | 30 | 10-32A |
| | 2A | 25-80A |
| Language | S | SPANISH |
| | E | ENGLISH |
| | P | PORTUGUESE |

---

**Manufacturer Information:**

Buzzom ACSA 0158, P.O. Box 28537 Miami, FL 33102, USA

Av. El Buen Pastor c/c Vargas, Edif. Alba, Piso 1, Oficina 1-A, Boleíta Norte, Caracas - Venezuela

Telfs.: (0212) 237.0711 / 1151 / 3477 / 238.7006 / Fax: 235.2497

e-mail: genteven@genteca.com.ve

*Note: Technical data are valid at the time of printing. The manufacturer reserves the right to subsequent alterations.*
