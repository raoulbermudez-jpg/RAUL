---
title: "GUCT General Description and Installation Manual"
type: Technical
source: "GD-MAN-051-02-V1-US.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GUCT"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GUCT General Description and Installation Manual

## GUCT General Description

GUCT is an electronic Motor Protection Integral Relay that constantly supervises motor current and power supply voltage, using a thermal model algorithm to protect your motor against undercurrent and overload conditions and voltage failures.

**WARNING:** Only qualified technicians with knowledge about overload relays and associated machinery should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

**CAUTION:** This product may start automatically; the user must take cautions to avoid hazards to people.

## GUCT Parts and Pieces

### Front Side View Components

1. LCD display
2. Indicator light (LEDs):
   - Status Relay
   - Failure
3. START Push Button
4. ADJUST Push Buttons (Up & Down)
5. SELECT Push Button
6. Back Groove for DIN Rail mounting
7. Attachable Mounting Ear for Flat Surface mounting
8. Supporting Brackets for DIN Rail mounting
9. Current Sensing Holes for motor wiring
10. Power Supply Voltage Input (L1, L2, L3)
11. Contacts for Relay (95-96) and (97-98)
12. GIO Port (for Serial Communication)
13. GIO PORT cover

### Relay Contact Configuration

- 95-96 connected / 97-98 open = Tripped
- 95-96 open / 97-98 connected = Normal

## Mechanical Installation

### GUCT DIN Rail Mounting

**CAUTION:** GUCT must be installed in an accessible position free from dust, dirt, dampness and vibration. Allow enough space for air circulation around the enclosure and easy access to all operator controls. Indoors Use only.

**Instructions for Mechanical Installation:**

Place GUCT at inclined position with its back side placed toward the upper edge of the DIN Rail and push down GUCT relay until it clicks on the rail.

### GUCT Flat Surface Mounting

**Instructions for Mechanical Installation:**

a) Take off the two (2) attachable mountings ears located at back side of GUCT, insert and slip both attachable mounting ears into the GUCT back side grooves.

b) Place GUCT over flat surface panel and fix it using a screwdriver suitable for screws 3/16" x 1/2".

**Recommendation for Flat Surface Mounting:** Make two (2) holes (5/32") on panel surface before installing.

### GUCT General Dimensions

- Length: 92 mm
- Width: 91 mm
- Height: 96 mm

**CAUTION:** This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

**CAUTION:** An incorrectly applied or installed GUCT can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the GUCT.

## Electrical Installation

### 6.1 Terminal Designation

| Terminal | Description |
|----------|-------------|
| L1 | Voltage Input (Phase R) |
| L2 | Voltage Input (Phase S) |
| L3 | Voltage Input (Phase T) |
| 95 | Contact for Auxiliary Relay |
| 96 | Contact for Auxiliary Relay |
| 97 | Contact for Trip Relay |
| 98 | Contact for Trip Relay |

### Relay Contact States

- 95-96 Connected > Tripped
- 95-96 Open > Normal
- 97-98 Connected > Trip Active

### 6.2 Basic Diagram Installation

The basic diagram shows connection of GUCT with circuit breaker, contactor, and fuses (5A, 600V options). Power supply (L1, L2, L3) connects in parallel before the line starter circuit through the contactor.

### 6.3 Diagram Installation for External Toroids

External toroids are available as optional equipment for serial communication with other devices via the GIO Port.

### Recommendations for Wiring

- Avoid over tightening the M3 screws upon terminals during wiring connection. Tightening Torque: 4.4 Ibf-in, 5.1 Kgf-cm
- Wire Strip Length: 6-7 mm
- Terminal wiring size: 2 AWG 10 (4 mm²) < AWG 18
- Current Sensing Holes (conduits) wiring size: 2 AWG 4 (11 mm)
- Connect L1L2L3 terminal for Voltage Input in parallel connection before line starter circuit through Contactor
- Use three Current Sensing Holes for passing wires before connection to 3 phases motor. Using less than three (3) wires shall cause current unbalance and wrong measures

**WARNING (Risk of Electric Shock):** Disconnect power supply before installing GUCT. Electric Shock will result in death or serious injury.

**CAUTION:** Check that the chosen GUCT model voltage and current correspond to line voltage and motor current.

## GUCT Operation

GUCT constantly supervises current and voltage values; when any harmful condition occurs, the output connection is deactivated until the fault disappears and power line conditions return to an acceptable level. Specific timing such as Start Up Delay and Fault Detection Delay are incorporated to prevent nuisance tripping due to rapid power fluctuations.

GUCT provides LCD Display to indicate the output status (voltage, current, unbalance, frequency and load status). It also provides four (4) push buttons (On/Off, Up, Down and Select) for electrical parameter adjustment such as Voltage, Current, Frequency, Fault Detection Delay and others.

A Communication Port with MODBUS RTU protocol is included in GUCT.

## Screen Adjustment and Display Screens

The GUCT LCD provides various screens for monitoring and adjusting the relay:

### Initial Screen (0)
- Displays voltage readings for three phases (V1, V2, V3)
- Shows status indicator (OFF/ON)
- Displays frequency (FREQ)

### Fault Screens (1.1-1.14)
Display conditions including:
- Disconnected by MODBUS Undervolt
- Disconnected on Manual Mode
- Disconnected by 3rd Failure
- Start Up Delay (TC)
- Undervoltage (UV)
- Overvoltage (OV)
- Voltage Unbalance (VUB)
- Frequency Shift (FS)
- Single Phasing (VSP)
- Phase Reversal (PR)
- Accumulated Heat (%)
- Overheating conditions

### Main Screen (1)
Shows:
- Voltage measurements (V12, V23, V31, VUB)
- Current measurements
- Power information (kVA, kW, PF, kWh, km/h)
- Motor hours counter
- Start delay information

### Configuration Menu (Screen 7)
Access by pressing both push buttons simultaneously. Options include:
- Voltage Adjust
- Current Adjust
- Clock Adjust
- Schedule Timer
- Start Mode (Auto/Manual)
- Change Password
- MODBUS Address
- Delete History
- Restart
- Recover Factory Values

## Schedule Timer Adjustment (GUCT+ Models)

Only GUCT+ models include "CLOCK ADJUSTMENTS" and "SCHEDULE TIMER" options.

### EVENT Adjustment Example
Configure ON/OFF times for specific days of the week. Settings available for:
- Individual days (Monday through Sunday)
- Holiday dates
- ON time (hours and minutes)
- OFF time (hours and minutes)

### HOLIDAY Adjustment Example
Configure special holiday dates with specific ON/OFF times.

### Navigation Instructions
- Use () or () buttons to navigate through menu options
- Press SELECT to enter or confirm selections
- Press both buttons simultaneously for menu access

## GUCT Dismounting Instructions

**WARNING:** Disconnect power supply (Circuit Breaker OFF) and electrical wiring before dismounting GUCT. Electrical shock will result in death or serious injury.

### 8.1 Instructions for Mechanical Dismounting (DIN RAIL)

a) Handling a Flat Screwdriver, pull downward the mounting bracket that you can see at rear and down side of GUCT.

b) With screwdriver at position (2), pull out GUCT from DIN Rail.

**Recommendation for DIN Rail Dismounting:** Pull downward 2 mm with a soft movement when using screwdriver for dismounting. Strong movement could break the supporting bracket.

### 8.2 Instructions for Mechanical Dismounting (FLAT SURFACE)

Unscrew both screws fixed on Flat Surface through attachable mounting ears and then pull out the GUCT relay from flat surface.

## Technical Specifications

### A) Power Supply Circuit

| Parameter | Specification |
|-----------|---------------|
| Rated Voltage, Ue | 208/220/240 or 440/480 VAC |
| Voltage Operation Limits, Ue | 145-312 VAC or 264-672 VAC |
| Average Consumption, In | 45 mA |
| Rated Frequency, Fn | 50/60 Hz |
| Frequency Operation Limits, Fn | 42-70 Hz |
| Rated Duty | Uninterrupted Duty |

### B) Environmental Conditions, Operation Limits and Installing

| Parameter | Specification |
|-----------|---------------|
| Designed according to European Standards | IEC61010-1, IEC60255-6, IEC60947-1 LVD & EMC |
| Designed according to US Standards | UL (pending), NKCR, Auxiliary Devices |
| CE Marking | CE (pending), Low Voltage Devices |
| Ambient Air Temperature (Operation) | -5 °C to 55 °C (23 °F to 131 °F) |
| Ambient Air Temperature (Storage) | -10 °C to +70 °C (14 °F to 158 °F) |
| Maximum Relative Humidity | 85% R.H. |
| Vibrations | Class 1, Amplitude <0.035mm or 1G, 10Hz << 150Hz |
| Degree of Protection | IP20, Protected against objects > 12.5mm, but no protection against water |
| Pollution Degree | Degree 3 |
| Overvoltage Category | Category III |
| Rated Insulation Voltage | 500V |
| Impulse Voltage Test | 5 kV |
| Impulse Dielectric Test | 2.5 kV 50/60 Hz @ 1 min |
| Flammability Rating of Enclosure | V-0 |
| Enclosure Material | Polymers: PC, ABS, NYLON |
| Mounting Position | Any Position |
| Mounting Features | Symmetrical DIN Rail, Flat surface mounting |
| Terminal Screw Type | Flat M3 |
| Tightening Screw Torque | 5.1 Kgf-cm (4.4 Ibf-in) |
| Terminals Wiring | 10-18 WG |
| Current Sensing holes for Motor Wiring | Ø < 11 mm AWG 4 |
| Dimensions GUCT | 92 x 91 x 96 mm (L x W x H) |
| Weight GUCT | 494 g (1.09 lb) |

### C) Control Characteristics

| Parameter | Specification |
|-----------|---------------|
| Output Contact Rating | 3A @ 240 VAC / 0.5A @ 480 VAC |
| Electrical Life Expectancy | 100,000 Operations |
| Mechanical Life Expectancy | 10,000,000 Operations |
| Utilization Category | AC-15, Capacity for loads > 72 VA |

### D) Range Setting, Measuring

#### According to Voltage Model (208/480 VAC)

| Parameter | 208 VAC | 480 VAC | Accuracy |
|-----------|---------|---------|----------|
| Voltage Measurement Range, Um | 0-312 VAC | 0-672 VAC | ±2% |

#### According to Current Model

| Parameter | 0-4 A | 12 A | 32 A | 80 A | EXT(CT15) |
|-----------|-------|------|------|------|-----------|
| Current Measurement Range, Im | 1.5-40 | 3.5-125 | 10-320 | 25-800 | 25%-383%CT |
| Accuracy | ±2% | ±2% | ±2% | ±2% | ±2% |

#### Other Measured Parameters

| Parameter | Range | Accuracy |
|-----------|-------|----------|
| Frequency Range | 45.0-70.0 Hz | ±1% |
| Instantaneous Power Factor | 0.00-1.00 | ±8% |
| Instantaneous Reactive Power KVA | 0.0-999.9 kVA | ±4% |
| Instantaneous Real Power KW | 0.0-999.9 kW | ±4% |
| Energy KWH | 0-999999 kW/H | ±4% |
| Total Motor Running Time (hours) | 0-999999 H | ±1% |

### E) Algorithms and Protection Functions

| Parameter | 208 VAC | 480 VAC | Specification |
|-----------|---------|---------|---------------|
| Undervoltage (UV) @ Imotor=0 or OL | 165-225 | 350-460 | Level settings |
| Overvoltage (OV) @ Imotor=0 or OL | 215-270 | 460-580 | Level settings |
| Voltage Hysteresis Threshold | 6 VAC | 12 VAC | — |
| Voltage Unbalance Detection (VUB) | 2%-10% | — | Level settings |
| Single Phasing (VSP) | IN: VUB > 33%, OUT: VUB < 28% | — | — |
| Rated Frequency | 50/60 Hz | — | Level settings |
| Tolerance for Frequency Shift (FS) | 2%-10% | — | Level settings |
| Phase Reversal (PR) | Normal: A>B>C, Reversed: C>B>A | — | — |
| Trip Delay because of Voltage Failures (TD) | <1 sec to 1750 sec | — | Level settings |
| Start Up Delay (TC) | 0-600 sec | — | Level settings |
| Trip Delay because of VSP | 3 sec | — | — |
| Start Mode | Auto/Manual selection | — | — |
| Minimum Time Between Two Start Up | 50 x Thermal Class Sec | — | — |

#### Current-Based Protection Functions

| Parameter | 0.4 A | 1.2 A | 3.2 A | 8.0 A | EXT(CT15) |
|-----------|-------|-------|-------|-------|-----------|
| Nominal Current Setting | 1.5-4 | 3.5-12.5 | 10-32 | 25-80 | 25%-333% CT |
| Overload Level Setting (OL) | 5%-50% Inom | — | — | — | — |
| Thermal Class Setting | 5-35 | — | — | — | — |

#### Additional Protection Parameters

| Parameter | Specification |
|-----------|---------------|
| Dynamic Setting of Motor Thermal class | varies from 1 to 1/8 of adjusted class according to start up time and motor load level |
| Maximum Time Between Cold/Hot Curve | 2 Hours (from 1 to 1/3 or from 1/3 to 1) |
| Trip Delay because of Overload | According to Overload Level and Adjusted Class |
| Heat Threshold because of Overload Failure | 100% |
| Current Unbalance (CUB) | CUB > 48% |
| Current Stall Phase (CSP) | CUB > 60% |
| Accelerated Locked Rotor Detection (LR) | User selection YES/NO |
| Trip delay because of CSP | 1 Sec |
| Trip Delay because of CUB | 2 Sec |
| High-Inertia Load Option | YES/NO |
| High-Inertia Load Heat Threshold | 400% |
| High-Inertia Load Start up Delay | 20-120 Sec |
| Thermal Machine Cooling Time | 50 x Thermal Class Sec |
| Undercurrent | YES/NO |
| Undercurrent Disconnection Type (UC) | % Inom / Power Factor (PF) |
| Undercurrent Adjusting (% Inom) | 30%-90% Inom |
| Undercurrent Adjusting (PF) | 0.3-0.9 |
| Trip Delay because of UC | 5-600 Sec |
| Start Up Delay because of UC | 2-500 Min |
| Third Failure Detection | YES/NO |
| Permanent disconnection because of Third Failure | 3 Current failures in less than 105 min |
| Trip delay because of Third Failure | 3 Sec |

#### Events Control Characteristics

| Parameter | Specification |
|-----------|---------------|
| Real Time Clock | hh:mm mm/dd/yy UMT |
| Load Control by Events (schedule) | YES/NO User selection |
| Schedule Timer (events) | 60 |
| Schedule Timer (holidays) | 20 |

### F) Communications and Other Special Functions

| Parameter | Specification |
|-----------|---------------|
| Communication Protocol | MODBUS RTU @ 9600 8N1 |
| Communication Ports | GIO PORT (*) |
| Address Range | 1-127 |
| History Buffer Memory | 20 last faults report (failure type, value, date, hour and time elapsed) |
| Parameters Block | 0000 Free, 0001-9999 Blocked |

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

## Thermal Class Tripping Curves

The relay supports multiple thermal classes (5, 10, 15, 20, 25, 30) for different motor protection requirements. The tripping time decreases as the current load (I load / Inom) increases.

**Note:** Hot Curve = Cold Curve / 3

Standards: IEEE C37-112, IEC 60255-8

## How to Order According to Customer Needs

### GUCT Model Configuration

| Parameter | Options |
|-----------|---------|
| Number of Phases | T - 3 PHASES |
| Control Voltage | 208 - 208/220/240V, 480 - 440/480V |
| Amperage | 04 - 1-4A, 12 - 3.5-12.5A, 32 - 10-32A, 80 - 25-80A, 00 - CT EXTERNAL |
| Language | S - SPANISH, E - ENGLISH, P - PORTUGUESE |
| Schedule Timer | (Optional) |

## Manufacturer Information

**Made and designed by:**
Genteca, Generación de Tecnología C.A.
R.I.F: J-00223173-4
Av. El Buen Pastor, cruce con Calle Vargas
Edificio Alba, Piso I, Local 1-A
Boleita Norte, Caracas, 1070
República Bolivariana de Venezuela

**Phone:** +58-212-237-0711 (Master)
**Fax:** +58-212-235-2497
**Email:** genteven@genteca.com.ve
**Website:** www.genteca.com.ve

**Distributed in USA by:**
Miami Breaker INC.
7060 NW 52nd Street
Miami, Florida 33166, USA
**Phone:** +1-786-336-5780

---

**NOTE:** Technical data are valid at the time of printing. We reserve the right to subsequent alterations.
