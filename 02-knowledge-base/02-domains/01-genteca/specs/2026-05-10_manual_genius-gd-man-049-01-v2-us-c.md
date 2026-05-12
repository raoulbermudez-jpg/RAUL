---
title: "Genius GII Installation Manual"
type: Technical
source: "GD-MAN-049-01-V2-US-C.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GII"
version_status: "vigente"
date_processed: "2026-05-10"
---

# Genius GII Installation Manual

## GII General Description

Relayne GII is an electronic Phase Voltage Relay that constantly supervises line voltage values to protect electric loads and distribution power systems from failure and damage due to common voltage faults. Provides LCD Display to indicate the output status.

**WARNING:** Only qualified technicians with knowledge about protection relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

**WARNING:** This product may start automatically. The user must take precautions to avoid hazards to people.

## GII Parts and Pieces

### Front Side View
1. Indicator Lights (LED's)
   - Normal (ON) - Continuous Green
   - Start Delay (TC) - Blinking Green
   - Fault - Continuous Red
2. LCD Display
3. Start Push Button
4. Adjustment Push Buttons
5. Select Push Button
6. Flush Mounting Attachment

### Back Side View
7. Flush Mounting Bracket
8. Back Groove for DIN RAIL Mounting
9. Attachable Mounting Ear for Flat Surface Mounting
10. Supporting Bracket
11. Plug In Terminals
12. GIO PORT (Communication Port)
13. GIO PORT cover

## Instructions for Mechanical Installation

### DIN Rail Mounting

**CAUTION:** GII must be installed in an accessible position free from dust, dirt, dampness and vibration. Allow enough space for air circulation around the enclosure and easy access available to all operator controls. Indoors use only.

**CAUTION:** This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

**CAUTION:** An incorrectly applied or installed GII can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the GII.

a) Place GII at inclined position with its back side placed toward the upper edge of the DIN Rail and push down GII relay until it clicks on the rail.

### Flat Surface Mounting

a) Take off the two (2) mounting ears located at back side of GII and remove the flush mounting attachment and flush mounting bracket. Insert and slip both mounting ears into the GII back side grooves.

c) Place GII over flat surface panel and fix it using a screwdriver suitable for screws 3/16" x 1/2".

**Recommendation for Flat Surface Mounting:** Make two (2) holes (5/32") on panel surface before installing.

### Flat Surface Mounting Dimensions
- Width: 111 mm
- Height: 64.5 mm
- Tolerance: +/- 2 mm

### Flush Mounting

a) Cutout the panel surface according to shape and size:
   - Width: 111 mm
   - Height: 64.5 mm
   - Tolerance: +/- 2 mm

b) Remove the flush mounting brackets and flush mounting attachment by pulling out and sliding them.

c) Insert the GII flush mounting attachment into the panel.

d) Place the Genius GII in the backside of the panel and use the flush mounting brackets to fix GII until it clicks.

### General Dimensions
- Total Height: 90 mm
- Total Width: 124 mm
- Depth: 8 mm
- Width: 85 mm
- Hole diameter: 0 5/32"

## GII Connection Diagram

**WARNING (Risk of Electric Shock):** Disconnect power supply before installing GII. Electric shock will result in death or serious injury.

**CAUTION:** Check that the voltage of chosen GII model corresponds to line voltage.

### Terminal Designation

| Terminal | Description |
|----------|-------------|
| L1 | Voltage Input (Phase R) |
| L3 | Voltage Input (Phase S) |
| L5 | Voltage Input (Phase T) |
| 2, 4, 6, 7, 9, 11 | Not used |
| 8 | Trip Relay |
| 10 | Common |
| 12 | Aux. Relay (Alarm) |

**Normal:** 10-12 open, 8-10 connected
**Tripped:** 10-12 connected, 8-10 open

### Basic Diagram Installation

Connect L1, L2, L3 terminals for Voltage Input in parallel connection before line starter circuit through Contactor.

#### Recommendations for Wiring
- Avoid over tightening M2.5 screws upon terminals during wiring connection. Torque max. 4.5 Ib-in (5.18 Kgf-cm)
- Terminals wiring size: > AWG10 (4mm²) < AWG8
- Wire Strip Length: 6-7 mm
- Connect L1 L2 L3 terminal for Voltage Input in parallel connection before line starter circuit through Contactor

## Genius GII Operation

Genius GII constantly supervises line voltages values. When any harmful condition occurs, the output is deactivated until the fault disappears and power line condition returns to acceptable levels. Start Up Delay (TC) and Trip Delay (TD) are incorporated to prevent nuisance tripping due to rapid power fluctuations.

Genius GII provides LCD Display to indicate the output status and failure (voltage, unbalance, frequency load status) and historical registration of the last twenty detected failures. It also provides four (4) push buttons (Start, Adjustment and Select) for electrical parameter adjustments.

### Parameters Adjustment

Description of Genius GII push buttons:

| Push Button | Label | Function |
|-------------|-------|----------|
| START | - | Activation of restart when GII the relay is in Manual Mode |
| ADJUSTMENT | - | Browse up and down on any screen of quick exit from it |
| SELECT | - | Select or setup of the options |

## GII Adjustment Quick Guide

### Relay Status Screens

**1.1 Connected on AUTO Start Mode**
- Display shows voltage values
- Status: AUTO
- Frequency: 60.0 Hz
- Unbalance: 0%

**1.2 Disconnected on MANUAL Start Mode**
- Display shows voltage values
- Status: OFF MANUAL

**1.3 Disconnected by MODBUS**
- Display shows voltage values
- Status: OFF MODBUS

**1.4 Start up Delay (TC)**
- Shows delay time in seconds

### Fault Screens

**1.5 Undervoltage (UV)**
- Displays voltage values during fault
- Shows phase involved in fault
- Minimum value during fault

**1.6 Overvoltage (OV)**
- Displays voltage values during fault
- Shows phase involved in fault
- Maximum value during fault

**1.7 Voltage Single Phasing (VSP)**
- Displays voltage unbalance percentage
- Shows phases involved in fault

**1.8 Phase Reversal (PR)**
- Indicates phase sequence fault

**1.9 Frequency Shift (FS)**
- Shows frequency value during fault
- Frequency shift percentage

**1.10 Voltage Unbalance (VUB)**
- Shows unbalance percentage
- Phases involved in fault

### Main Adjustment Menu (Screen 4)

- VOLTAGE ADJUST
- START MODE
- FAULT HISTORY
- CHANGE PASSWORD
- MODBUS ADDRESS
- PUSH BUTTONS CONFIGURATION
- SPECIAL FUNCTIONS

### Fault History Screen Description (Nr. 2)

- Fault Type (UV for Undervoltage, OV for Overvoltage, etc.)
- Fault Number
- Fault registered value
- Phases involved in fault

### Push Buttons Configuration

- Press both push buttons (ADJUST and SELECT) at the same time to get the Adjustment Menu (Screen 4). If access to screen is locked, you must enter the password.
- Press both push buttons at the same time to get Quick Exit option
- Press SELECT to enter the chosen Adjusting Value
- Press both push buttons at the same time to get the Initial Screen 0

## GII+ Adjustment Quick Guide

GII+ models include "CLOCK ADJUST" and "SCHEDULE TIMER" options.

### Additional Relay Status Screens

**1.5 Disconnected by Schedule Timer**
- Display shows voltage values
- Status: OFF SCHEDL TIMER

### Main Adjustment Menu (Screen 5)

- VOLTAGE ADJUST
- CLOCK ADJUST
- SCHEDULE TIMER
- START MODE
- CHANGE PASSWORD
- MODBUS ADDRESS
- DELETE HISTORY
- EXIT

### Schedule Timer Features

GII+ includes:
- Clock Adjust with time and date display
- Schedule Timer with event and holiday adjustment capabilities
- Up to 20 events and 20 holidays can be configured
- Events can be set for specific days and times
- Holiday adjustment for special dates

### Fault History Screen Description (GII+)

- Fault date and starting time
- Fault number
- Duration time of fault (in minutes)
- Fault Type
- Fault value indication
- Phases involved in fault

## GII Dismounting Instructions

**WARNING:** Disconnect power supply (Circuit Breaker OFF) and electrical wiring before dismounting GII. Electrical shock would result in death or serious injury.

### Instructions for Mechanical Dismounting (DIN RAIL)

a) Using a Flat Screwdriver, pull downward the mounting bracket at the rear and down side of GII.

b) With screwdriver position (2), pull out GII from DIN Rail.

**Recommendation for DIN Rail Dismounting:** Pull downward 2mm with a soft movement when using screwdriver for dismounting. Strong movement could break the supporting bracket.

### Instructions for Mechanical Dismounting (FLAT SURFACE)

a) Unscrew both M6 screws fixed on Flat Surface through attachable mounting ears. Then pull out the GII relay from flat surface.

### Instructions for Mechanical Dismounting (FLUSH MOUNTING)

a) Remove the Flush Mounting Brackets. Pull out the indicated point and slide backward the piece.

b) Remove the Flush Mounting Attachment and GII.

## GII Technical Specifications

### A) Power Supply Circuit

**Rated Voltage, Ue:**
- 120 VAC
- 208/220/240 VAC
- 440/480 VAC

**Frequency Rated Duty:** Uninterrupted Duty 50/60 Hz

### B) Application Data, Environmental Conditions, Operation Limits and Installation

**b.1** Designed according to European Standards IEC61010-1, IEC60255-6, IEC60947-1 LVD & EMC

**b.2** UL Listing Certified for Canada

**b.3** CE Marking CE (pending), Low Voltage Devices IEC60947-1

**b.4** Ambient Air Temperature (Operation): -5 °C to 55 °C (23 °F to 131 °F)

**b.5** Ambient Air Temperature (Storage): -10 °C to + 70 °C (14 °F to 158 °F)

**b.6** Maximum Relative Humidity: 85% R.H.

**b.7** Vibrations: Class 1, Amplitude <0.035mm or 1G, 10Hz < f < 150Hz

**b.8** Degree of Protection: IP20, Protected against objects > 12.5mm

**b.9** Pollution Degree: Degree 3

**b.10** Overvoltage Category: Category III, 4KV

**b.11** Rated Insulation Voltage: 500V UL/IEC 60255-5

**b.12** Impulse Voltage Test: 5 KV IEC 60255-5

**b.13** Dielectric Voltage Withstand Test: 2.5 KV 50/60 Hz@1min UL508

**b.14** Flammability Rating of Enclosure: 5VA UL-94

**b.15** Enclosure Material: Polymers: PC, ABS, NYLON; PU, ABS

**b.16** Mounting Position: Symmetrical

**b.17** Mounting Features: Flat surface mounting with screw 3/16" x 1/2", Flush mounting

**b.18** Terminal Screw Type: Flat M2.5, Tightening Screw Torque: 5.20 Kgf-cm / 4.5 Ibf-in
Terminals Wiring: 12-18 AWG, L=7-8mm (5/16")

**b.19** Dimensions: 105, 90, 68 (LxWxH mm)

### C) Control Characteristics

**c.1** Output Contact Rating:
- Pilot Duty A300 seconds
- 128.1

**c.2** Utilization Category: AC-15, Capacity for loads> 72 VA IEC60947-5-1

**c.3** Electrical Life Expectancy: 100,000 Operations

**c.4** Mechanical Life Expectancy: 10,000,000 Operations

### D) Range Setting, Measuring (According to Voltage Model)

**Voltage Models:** 120/208/220/240, 440/480 VAC

**d.1** Voltage Measurement Range, Um: 0>168, 0+300, 0>532, 0>672 VAC, 2% Unbalance

**d.2** Frequency threshold: 45.0—70.0 Hz, 1% accuracy

### E) Algorithms and Protection Functions

**e.1** Undervoltage (UV): 95>115, 165>225, 350>460 Level settings

**e.2** Overvoltage (OV): 125→145, 215, 270/460>580 Level settings

**e.3** Voltage Hysteresis Threshold: 3, 6, 12 VAC

**e.4** Voltage Unbalance Detection (VUB): 2%>10% Level settings

**e.5** Voltage Single Phasing (VSP): INV VUB > 33%, OUT VUB < 28%

**e.6** Nominal Frequency: 50 or 60 Hz Level settings

**e.7** Frequency Shift (FREC): 2%>10% Level settings

**e.8** Phase Reversal (PR): Normal Sequence ABC, reversal sequence CBA

**e.9** Trip Delay because of Phase Reversal: <1sec

**e.10** Trip Delay because of another Voltage Failures: 1+ 30 sec

**e.11** Start up Delay (TC): 0>600 sec Level settings

**e.12** Start Mode: Auto/Manual User selection

**e.13** Clock and Calendar (Only GII+): hh:mm mm/dd/yy

**e.14** Load control by events (schedule): YES / NO User selection

**e.15** Schedule timer (events): 20 User selection

**e.16** Schedule timer (holidays): 20 User selection

### F) Communications and Other Special Functions

**f.1** Communication Protocol: MODBUS RTU 29600 8N1

**f.2** Communication Ports: GIO PORT

**f.3** History Buffer Memory:
- GII: 20 last faults report
- GII+: failure type, value, date, hour and time elapse

**f.4** Parameters Block: 0000 Free, 0001—9999 Blocked Level settings

**Note:** GIO Plug is required for GIO PORT communication. It is available by separate order.

### G) Immunity and Emissions, Electromagnetic Compatibility (EMC) for Heavy Industrial Environment (B)

**g.1** Electrostatic Discharge: IEC 61000-4-2

**g.2** Immunity to Radio Frequency Test: IEC 61000-4-3

**g.3** Electrical Fast Transients: IEC 61000-4-4

**g.4** Surge Immunity Test: IEC 61000-4-5

**g.5** Radio-Frequency Continuous Conducted: IEC 61000-4-6

**g.6** Power Frequency Magnetic Field: IEC 61000-4-8

**g.7** Voltage Dips, Short Interruptions and Voltage Variations: IEC 61000-4-11

**g.8** Harmonics and Interharmonics Immunity Tests: IEC 61000-4-13

**g.9** Voltage Fluctuation Immunity: IEC 61000-4-14

**g.10** 2% Unbalance Immunity Test: IEC 61000-4-27

**g.11** Variation of Power Frequency: IEC 61000-4-28

## How to Order

**GII** — **[SCHEDULE TIMER OPTION]** — **[CONNECTION]** — **[VOLTAGE]** — **[LANGUAGE]**

**Schedule Timer Option:**
- S — Standard
- + — Schedule Timer

**Line Connection:**
- L — Line to Line

**Voltage:**
- 120 — 120 VAC
- 208 — 208/220/240 VAC
- 480 — 440/480 VAC

**Language:**
- S — Spanish
- E — English
- P — Portuguese

## Manufacturer Information

Made and designed by Genteca, Generación de Tecnología C.A.
- R.L.F: J-00223173-4
- Address: Av. El Buen Pastor, cruce con Calle Vargas, Edificio Alba, Piso 1, Local I-A, Boleita Norte, Caracas, 1070, República Bolivariana de Venezuela
- Phone: +58-212-237.071 (Master)
- Fax: +58-212-235.2497
- E-mail: genteven@genteca.com.ve
- Website: www.genteca.com.ve

**Distributed in USA by:** Miami Breaker INC. 7060 Nw. 52nd Street, Miami-Florida 33166, USA. Phone: +1-786-3365780

**NOTE:** Technical data are valid at the time of printing. Genteca reserves the right to subsequent alterations.

## Glossary

| Abbreviation | Definition |
|--------------|-----------|
| FS | Frequency Shift |
| VSP | Voltage Single Phasing |
| PR | Phase Reversal |
| UV | Undervoltage |
| OV | Overvoltage |
| VUB | Voltage Unbalance |
| TD | Trip Delay |
| TC | Start Up Delay |
| PROG. | Programmer |
| VOLT. | Voltage |
