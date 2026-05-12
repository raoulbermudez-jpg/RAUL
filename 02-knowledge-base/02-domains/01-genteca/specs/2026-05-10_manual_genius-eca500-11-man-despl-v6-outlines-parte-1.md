---
title: "ECA500-11 Total Motor Protection Relay - Installation Instructions"
type: Technical
source: "ECA500-11_MAN_DESPL_V6 OUTLINES.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "ECA500-11"
version_status: "historica"
date_processed: "2026-05-10"
---

# ECA500-11 Total Motor Protection Relay Installation Instructions

## General Description

The ECA500-11 is an electronic Total Motor Protection Relay that constantly supervises motor current and main electrical parameters such as voltage, power factor, real power, reactive power, and energy consumption. It provides reliable protection against overload, phase failure, phase reversal, single phasing, and unbalanced conditions.

## Specifications

**Rated Voltage, Ue:** 208/240/440/480 VAC

**Voltage Operation Limits, Ue:** 145>312 V / 264>672 V

## Safety Warnings

**WARNING:** Only qualified electrical technicians with knowledge of overload relays and associated machinery should perform installation, starting up, and maintenance. Adhere to all local and national electric codes. Disconnect all electrical power at the source prior to any installation or maintenance work. Failure to comply could result in equipment damage, personal injury, or death.

**WARNING:** This product may start automatically. The user must take caution to avoid hazards to people.

**WARNING:** Disconnect power supply before installing ECA500-11. Failure to comply may result in death or serious injury.

**CAUTION:** This product has been designed for industrial environment. Use in residential environment may cause unwanted electromagnetic disturbances.

**CAUTION:** An incorrectly applied or installed ECA500-11 can result in damage to components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction.

**CAUTION:** ECA500-11 must be installed in an accessible position free from dust, dirt, dampness, and vibration. Allow enough space for air circulation and easy access to operator controls. Indoor use only.

## Parts and Components

- Detachable CT Box
- CT Holes for load wiring
- Voltage Input terminals
- Trip Relay (Control)
- Auxiliary Relay
- Temperature Sensor Input
- Digital Input
- Indicator Lights
- Push Buttons (Start, Select, Adjust)
- Basic Wiring Label

## Detachable CT Box Mounting

**CAUTION:** Each set of ECA500-11 and detachable CT box is calibrated and have the same Model Number. Before assembling the CT box, verify that its factory number is the same as the ECA500-11 one. Failure to comply may result in measurement error and loss of protection.

### Assembly Instructions

1. Move the supporting brackets 2mm outside and push downward ECA500-11 to CT BOX until the back groove of relay can insert into CT BOX guide rail, using Alignment Mark as reference.

2. From Alignment Mark, move ECA500-11 relay towards the left sliding through rail guide until it clicks.

### Dismounting Instructions

1. Disconnect both CT Input Terminal used for ECA500-11 and CT Box connection and pull down both supporting brackets using screwdrivers.

2. Move ECA500-11 towards the right sliding through CT Box guide rail until it gets to alignment mark.

3. Pull out ECA500-11 upwards from CT Box.

## DIN Rail Mounting

### Installation Without CT Box

1. Place ECA500-11 at inclined position with its back side placed toward the upper edge of the DIN Rail.

2. Push down ECA500-11 relay until it clicks on the rail.

### Installation With CT Box

1. Assemble CT Box on ECA500-11 (See detachable CT Box section).

2. Place ECA500-11 at inclined position so that its back side (CT Box) is placed toward the upper edge of the DIN Rail.

3. Push down ECA500-11 relay until it clicks on the rail.

### DIN Rail Dismounting Without CT Box

1. Using a flat screwdriver, pull downward the mounting bracket at rear and down side of ECA500-11.

2. With screwdriver at position (2), pull out ECA500-11 from DIN Rail.

### DIN Rail Dismounting With CT Box

1. Using a flat screwdriver, pull downward the mounting bracket at rear and down side of ECA500-11.

2. With screwdriver at position (2), pull out ECA500-11 from DIN Rail.

**Recommendation:** Pull downward 2 mm with a soft movement when using screwdriver for dismounting. Strong movement could break the supporting bracket.

## Flat Surface Mounting

### Installation Without CT Box

1. Take off the four (4) mounting ears at back side of ECA500-11 and insert both mounting ears into the back side grooves.

2. Place ECA500-11 over a flat surface panel and mount using (2) #8 x 1/2" screws.

**Recommendation:** Make four (4) holes (5/32") on panel surface before installing. Refer to dimensions section.

### Installation With CT Box

1. Assemble Detachable CT Box on ECA500-11.

2. Take off the four (4) mounting ears at back side of CT Box and insert both mounting ears into the back side grooves.

3. Place ECA500-11 over a flat surface panel and mount using (2) #8 x 1/2" screws.

**Recommendation:** Make four (4) holes (5/32") on panel surface before installing.

### Flat Surface Dismounting Without CT Box

Unscrew both screws fixed on flat surface through attachable mounting ears and pull out ECA500-11 relay from flat surface.

### Flat Surface Dismounting With CT Box

Unscrew both screws fixed on flat surface through attachable mounting ears and pull out ECA500-11 relay from flat surface.

## Connection Diagram and Terminal Designation

### Terminal Description

| Terminal | Description |
|----------|-------------|
| B1 | Voltage Input L1 (Phase R) |
| B2 | Voltage Input L2 (Phase S) |
| B3 | Voltage Input L3 (Phase T) |
| C1 | Control Relay (Closed when normal) |
| C2 | Control Relay (Common) |
| C3 | Control Relay (Closed when tripped) |
| A1 | Auxiliary Relay (Closed when normally) |
| A2 | Auxiliary Relay (Common) |
| A3 | Auxiliary Relay (Closed when tripped) |
| CTA | CT-A Input |
| CTB | CT-B Input |
| CTC | CT-C Input |
| CT-D | CT-D (Common secondary) |
| A9, A10 | PT100 (Terminal A-B-B Sensor) |
| A13 | Digital Input 1 (Dry Contacts only) |
| A14-A15 | Digital Input 2 (Dry Contacts only) |
| S- | RS485 S- (Negative Serial Comm) |
| S+ | RS485 S+ (Positive Serial Comm) |
| SG | RS485SG (Ground for Serial Comm) |

## Wiring Requirements

**Surge Protective Device (SPD) Requirements (User-supplied):**
- UL Recognized SPD Type 2
- Voltage Protection Rating (VPR): = 1800V
- Nominal Discharge Current (In) = 10kA
- Max. Continuous Voltage (MCOV): Any value between 1.1 and 1.4 Ue (where Ue is the nominal voltage of the installation)
- Short-circuit current rating (SCR): 10 KA min

**Wiring Recommendations:**

- Avoid over-tightening M25 screw terminals during wiring connection. Torque maximum: 4.5 lb-in (5.18 kg-cm).

- Feed the three phases going to the motor through the three holes. Using less than three wires may cause undesired current unbalance.

- Screw Terminal wire size: Between 12 AWG and 18 AWG.

- Maximum diameter of CT Box Holes wiring size: AWG 0 (18 mm).

- Connect L1-L2-L3 terminal for Voltage Input in parallel connection before line starter circuit contactor (as shown in Connection Diagram).

- Wire Strip Length: 7-8 mm.

**Important Note:** CAUTION in case of wiring configuration with ungrounded power. Ungrounded systems are inherently unstable and can produce 6% voltage during fault conditions. During these fault conditions, any SPD may be subjected to voltages which exceed manufacturer design ratings.

## Operation

ECA500-11 constantly supervises current and voltage values. When any harmful condition occurs, the output connection is deactivated until the fault clears and power line conditions return to an acceptable level. Specific timing such as Start Up Delay and Fault Detection Delay are incorporated to prevent nuisance tripping due to rapid power action.

ECA500-11 provides LCD Display to indicate output status (voltage, current, unbalance, frequency, and load status). It includes four (4) push buttons (ON/OFF, Up, Down, and Select) for electrical parameter adjustment such as voltage, current, frequency, fault detection delay, and others. A Communication Port with MODBUS RTU protocol is included in ECA500-11.

## Recommended Values for Adjustable Parameters

### Undervoltage (UV) and Overvoltage (OV)

Manufacturers usually offer motors with limited range of operation voltage inside ±10% of nominal value.

**Example:** A protector installed for a motor of 220V should be adjusted in:
- UV = 220 × 90% = 198V (Undervoltage)
- OV = 220 × 110% = 242V (Overvoltage)

### Voltage Unbalance

According to NEMA MG1 standards, it is recommended that motors operate with unbalance voltage less than 5%.

### Overload (OL)

The recommended value for protection against overload is inside the range of 110% to 120% of nominal current (In) or the current specified in the motor nameplate at maximum rated load (FLA).

IN = FLA motor nameplate  
OL = Service factor motor nameplate

### Underload by Current (%In)

The recommended threshold value to protect from underload fault condition through current monitoring is 80% of the maximum rated load current (FLA) specified by the manufacturer.

### Underload by Power Factor (PF)

Indicator applicable to motors that are oversized, contributing to loss in efficiencies or running at low load or without load (dry running).

**Example:** Submersible pumps of gas stations, etc.

To protect against low load or dry running through monitoring of power factor (PF), the ECA500-11 is factory set to 0.5. Although this protection setting can be configured for a value in the range 0.1 to 0.9 PF, it is recommended to set the threshold to above 0.3 PF.

### Selection of Thermal Class of the Motor

- **Class 5:** Smaller motors with fast acceleration, requiring extremely fast tripping in the event of overload.

- **Class 10 (Fast):** Motors used in compressor, refrigeration equipment, submersible pumps, and motors of general purpose usually classified under IEC standard that reach continual operation in less than 4 seconds.

- **Class 15:** Motors for specialized applications.

- **Class 20 (Standard):** Motors of general purpose qualified under NEMA standard.

- **Class 30 (Slow):** Industrial motors for high inertia loads with tripping time that exceeds 10 seconds.

## Schedule Timer Adjustment Guide

ECA500-11 includes "CLOCK ADJUSTMENTS" and "SCHEDULE TIMER" options. Timer can be configured to handle EVENTS and HOLIDAYS adjustments.

**Holiday Example:**
Configure specific dates (e.g., June 24th) with custom ON/OFF schedules to control motor protection parameters on designated holidays.

## Connections with External Current Transformers

**Note:** Models identified as ECA500-11-480000 and ECA500-11-208000 are used exclusively with external CTs. These models protect motors up to 640A range of nominal current.

### External CT Selection

The user must specify the nominal motor current. With this information, the user can check the nominal current range from the provided table and identify the corresponding CT relation required for installation.

| Nominal Current | CT Relation |
|-----------------|------------|
| 150 | 200/5 |
| 200 | 300/5 |
| 250 | 400/5 |
| 300 | 500/5 |
| 350 | 600/5 or 1200/5 |
| 400 | 500/5 or 600/5 |
| 500 | 600/5 or 750/5 |

**Example:** If a motor consumes a nominal current of 350 amperes, the external toroid to select will be a value of 1200/5.

### External CT Configuration

The user must supply the ECA500-11 with external CT using the instructions of adjustments contained in the application note. All other functions and protections will remain as specified in the installation instructions.

### Warranty Consideration

The calibration of the ECA500-11 will remain under warranty, as long as the external CTs are of commercial grade and rated Class 1 secondary 5A.
