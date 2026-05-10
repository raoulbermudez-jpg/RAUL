```markdown
---
title: "GIII Total Motor Protection Relay - Application Notes"
type: Technical
source: "NOTAS DE APLICACIONES GIII-Ingles.pdf"
product_line: "Genius"
document_type: "nota-aplicacion"
product_code: "GIII"
date_processed: "2026-05-09"
---

# GIII Total Motor Protection Relay - Examples of Typical Applications

## Terminal Designation

### Voltage and Control Inputs
- **B1**: Voltage Input L1 (R)
- **B3**: Voltage Input L2 (S)
- **B5**: Voltage Input L3 (T)

### Control Relay Terminals
- **B6**: Control Relay for Contactor activation and Line Starter Circuit
- **B8**: Control Relay Common for Contactor activation or for closing of Line Starter Circuit
- **B10**: Control Relay for Contactor Supervision or for fault indication by means of Pilot Alarm

### Auxiliary Relay Terminals
- **B11**: Auxiliary Relay Contact Normally Open (N.O) (according to User Instructions)
- **B13**: Auxiliary Relay Common Contact
- **B15**: Auxiliary Relay Contact Normally Closed (N.C)

### Current Transformer (CT) Inputs
- **B16**: Input CT-A Secondary of Current Transformer - Motor current I1 (line L1 or U)
- **B17**: Input CT-B Secondary of Current Transformer - Motor current I2 (line L2 or V)
- **B18**: Input CT-C Secondary of Current Transformer - Motor current I3 (line L3 or W)
- **B19**: Input CT-D Common of Secondary of Current Transformer
- **B20**: Input CT-D Common of Secondary of Current Transformer

### Temperature Sensor (PT100)
- **A8**: Temperature Sensor PT100, Terminal "A" connector
- **A9**: Temperature Sensor PT100, Terminal "B" connector
- **A10**: Temperature Sensor PT100, Terminal "B sensing" connector

### Digital Inputs
- **A11**: Digital Input 1 Common
- **A12**: Digital Input 1 (for Dry Contact use only)
- **A14**: Digital Input 2 Common
- **A15**: Digital Input 2 (for Dry Contact use only)

### RS-485 Communication
- **A18**: RS-485 S- Negative Polarity signal for Serial Communication
- **A19**: RS-485 S+ Positive Polarity signal for Serial Communication
- **A20**: RS-485 SG Negative of signals for Serial Communication

### Unused Terminals
- A1...A7, A13, A17, A21...A40
- B2, B4, B7, B9, B12, B14, B21...B40

## Recommended Parameter Adjustment Values for GIII Relay

### Undervoltage (UV) & Overvoltage (OV)
Manufacturers offer motors with limited range of voltage operation (within ±10% of nominal value).

**Example for a 220V motor:**
- **UV (Undervoltage)**: 220 × 90% = 198 V
- **OV (Overvoltage)**: 220 × 110% = 242 V

### Voltage Unbalance (VUB)
According to NEMA MG1 standard, motors should operate with voltage values where VUB is less than 5%.
- **Recommended VUB range**: 2% to 5%

### Overload (OL)
Recommended setting range: 110% to 120% of Nominal Current (In) or Full Load Amperage (FLA) indicated at motor nameplate.
- **Induction motors sized according to application**: 110% to 120% × FLA
- **Induction motors oversized to application**: 110% to 120% × In

### Undercurrent (UC) by %In
When undercurrent protection is chosen by Current In measurement:
- **Recommended default value**: 80% × FLA

### Undercurrent (UC) by Power Factor (PF)
Applicable to oversized motors requiring undercurrent protection during starting cycle (e.g., submersible pumps for gas stations).

When undercurrent protection is chosen by Power Factor measurement:
- **Recommended setting**: above 0.3
- **Factory default setting**: 0.5
- **Available range**: 0.1 to 0.9
- **Desired limit value**: corresponds to motor curves; Power Factor should be equivalent to 20% of nominal current

### Motor Trip Class Selection

**Class 5**: Small motors with fast acceleration requiring fast trip response for overload protection

**Class 10 (fast trip)**: Motor applications such as compressors, refrigeration systems, submersible pumps and general purposes rated according to IEC Standards, with time less than 4 seconds required to reach nominal speed (rpm). Motors for specialized applications

**Class 15**: Motors for general purpose rated according to NEMA Standards

**Class 20 (standard response)**: Motors for HIGH INERTIA LOAD (Long Acceleration, over 10 seconds)

**Class 30 (slow)**: Motors for HIGH INERTIA LOAD applications

## Motor Protection - Example 1

### Application Description
The GIII relay protects motors in a three-phase system with main disconnector and circuit breaker protection. The relay includes PT100 temperature sensing, digital inputs, GIO port, RS-485 communication, and both control and auxiliary relays.

### Protection Features
- **Voltage Input**: L1, L2, L3 (terminals B1, B3, B5)
- **Current Input**: I1, I2, I3 via Current Transformers (terminals B16, B17, B18)
- **Temperature Monitoring**: PT100 sensor capability
- **Output Control**: Contactor control via Control Relay (terminals B6, B8)
- **Supervision**: Contactor supervision or fault indication via Control Relay (terminal B10)
- **Alarm Capability**: Optional alarm output via Auxiliary Relay

### Operating Notes
- **GIII deactivates the CONTACTOR** (terminals B6 and B8) when any failure of voltage, current unbalance, or overload appears
- **Voltage Input Terminals** L1-L2-L3 (terminals B1, B3, B5) must be connected before Contact Input and associated line start circuit

### Start Mode Options

#### MANUAL Start Mode
- AUTO/MANUAL Start Mode Slide Switch set to MANUAL position
- Start Push button required to activate the Contactor after a failure and its corresponding time delay of protection
- See User Manual for details

#### AUTO Start Mode
- AUTO/MANUAL Start Mode Slide Switch set to AUTO position
- GIII automatically activates the Contactor after a failure and its corresponding time delay of protection
- **Lockout condition**: If three failures occur in less than 30 minutes, GIII will not activate for a fourth automatic attempt
- See User Manual for details

## Electrical Protection

### Short Circuit Protection
The electrical installation should include any of the following components for short circuit protection:

- **Time Delay Fuses (Dual-Element)**: 1.75 to 2.25 times Full Load Amperage (FLA)
- **Non-Time Delay Fuses (Class CC)**: 3 to 4 times FLA
```