---
title: "ECA500-11 Total Motor Protection Relay - Installation Instructions"
type: Technical
source: "ECA500-11_MAN_V3_US.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "ECA500-11"
date_processed: "2026-05-09"
---

# ECA500-11 Total Motor Protection Relay
## Installation Instructions

## General Description

The ECA500-11 is an electronic Total Motor Protection Relay that constantly supervises the motor current and the main electrical parameters such as voltage, power factor, real power, reactive power and energy consumption, giving the most reliable protection against overload, phase failure, phase reversal, single phasing and unbalanced conditions.

## Safety Warnings

**WARNING:** Only qualified electrical technicians with knowledge of overload relays and associated machinery should perform the installation, starting up, and maintenance of the system. Adhere to all local and national electric codes. Disconnect all electrical power at the source prior to any installation or maintenance work. Failure to comply could result in equipment damage, personal injury, or even death.

**WARNING:** This product may start automatically. The user must take cautions to avoid hazards to people.

**WARNING:** Disconnect power supply before installing ECA500-11. Failure to comply may result in death or serious injury.

## Cautions

**CAUTION:** This product has been designed for industrial environment. Use of this product in residential environment may cause unwanted electromagnetic disturbances, in which case the user may be required to take adequate mitigation measures.

**CAUTION:** An incorrectly applied or installed ECA500-11 can result in damage to the components or reduction in product life. Wiring or application errors, or operating/storing in excessive ambient temperatures may result in malfunction of the ECA500-11.

**CAUTION:** Each set of ECA500-11 and detachable CT box is calibrated and have the same model number. Before assembling the CT box, verify that its factory number is the same as the ECA500-11 one. Failure to comply may result in measurement error and a loss of protection.

**CAUTION:** Check that the voltage and current chosen of ECA500-11 model corresponds to line voltage and motor current.

## Mechanical Installation Instructions

### 4.1 Installation without CT Box

a) Place ECA500-11 at inclined position so that its back side must be placed toward the upper edge of the DIN Rail and then push down ECA500-11 relay as shown in figure until it does CLICK on the rail.

### 4.2 Installation with CT Box

Once you have assembled CT Box on ECA500-11, follow these mounting instructions:

a) Place ECA500-11 at inclined position so that its back side (CT Box) must be placed toward the upper edge of the DIN Rail and then push down ECA500-11 relay as shown in figure until it does CLICK on the rail.

### 5.1 Flat Surface Mounting

a) Take off the four (4) mounting ears at back side of ECA500-11, insert and slip both mounting ears into the ECA500-11 back side grooves.

**Recommendation for Flat Surface Mounting:**
- Make four (4) holes (5/32") on panel surface before installing
- Reference Section 6.1 for dimensions (without CT Box)
- Reference Section 6.2 for dimensions (with CT Box)

## Wiring Instructions

### Wiring Diagram

The ECA500-11 includes a wiring diagram for proper connection to the motor protection circuit.

### Recommendations for Wiring

- Avoid over-tightening M2.5 screw terminals during wiring of connections. Maximum torque: 4.5 lb-in (5.18 kgf-cm)
- Wire Strip Length: 7-8 mm
- Screw Terminal wire size: Between 12 AWG and 18 AWG
- Maximum diameter of CT Box holes wiring size: AWG 0 (18 mm)
- Feed the three phases going to the motor through the three CT holes. Using less than three wires may cause undesired current unbalance
- Connect L1L2L3 terminal for Voltage Input in parallel connection before line starter circuit through Contactor (as shown in Connection Diagram)
- UL Recognized SPD Type 2

## Features and Display

The ECA500-11 provides:
- LCD Display to indicate the output status (voltage, current, unbalance, frequency and load status)
- Four (4) push buttons (ON/Off, Up, Down and Select) for electrical parameter adjustment such as Voltage, Current, Frequency, Fault Detection Delay and others
- Communication Port with MODBUS RTU protocol

The ECA500-11 constantly supervises current and voltage values. When any harmful condition occurs, the output connection is deactivated until the fault disappears and power line conditions return to an acceptable level. Specific timing such as Start Up Delay and Fault Detection Delay are incorporated to prevent nuisance tripping due to rapid power fluctuations.

## Setup Menu and Navigation

### Main Menu Access

Press both push buttons at the same time in order to access the Main Menu (Screen #7). If access to screen is locked, you must enter the required password.

### Navigation Controls

- Press SELECT to enter the chosen value
- Press both push buttons at the same time to navigate to the initial screen
- Press both push buttons again to exit the Setup Menu

## Recommended Values for Adjustable Parameters

### Undervoltage (UV) and Overvoltage (OV)

Manufacturers usually offer motors with limited range of operation voltage inside of ±10% of nominal value. Example: a protector installed for a motor of 220V should operate within this range.

### Power Factor (PF) Protection

The ECA500-11 is factory set to 0.5 PF to protect against low load or dry running conditions through monitoring power factor (example: submersible pumps of gas stations, etc.). Although this protection setting can be configured for a value in the range 0.1 to 0.9 PF, it is recommended to set the threshold above 0.3 PF.

### Phase Reversal (PR) Protection

Protection setting available for Phase Reversal conditions.