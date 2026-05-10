```markdown
---
title: "Relayne GII - Phase Voltage Relay"
type: Technical
source: "GII+V1.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "GII"
date_processed: "2026-05-09"
---

# Relayne GII Phase Voltage Relay

## Features

Relayne GII is a microcontrolled based three Phase Voltage Relay, specifically designed to protect electric loads and distribution power systems from failure and damage due to common voltage faults.

### Measurement of:
- Voltage
- Frequency

### Protection Against:
- Overvoltage/Undervoltage
- Frequency Variation
- Voltage Unbalance
- Single Phasing
- Phase Reversal

GII constantly supervises line voltages values; when any harmful condition occurs, the output is deactivated until the fault disappears and power line condition returns to an acceptable level. Start Up and Trip Delay are incorporated to prevent nuisance tripping due to rapid power fluctuations.

## Adjustments Available

- Overvoltage threshold
- Undervoltage threshold
- Voltage Unbalance threshold
- Frequency Shift threshold
- Trip Delay
- Start Up Delay after Voltage Fault Recovery
- Schedule Timer (weekly & holidays - available only for GII+ models)

## Physical Features

- 16x2 LCD Display with voltage values on screen
- Four (4) push buttons for parameters adjustment (Start, Adjustment (2) and Select)
- Two (2) indicator lights (LEDs) for control and fault indication
- One (1) relay SPDT contact (3A@240 VAC / 1.5A@480 VAC)
- Enclosure material UL94V0
- Din-Rail, Flat Surface or Flush mounting options

An innovative mechanical design allows three (3) placement options:
- DIN-Rail mounting
- Flat Surface mounting, using an exclusive attachable mounting ear
- Flush mounting

## Communications & Features

- AUTO/MANUAL Restart Mode
- Password protection
- GIO Port (MODBUS RTU protocol, 9600 baud output, 8N1)
- Remote On/Off
- Communication Port with MODBUS RTU protocol

### Reports Available:
- Voltage report
- Adjustment Values report
- Start Mode report
- 20 Last Fault report
- Voltage unbalance report
- Power Line Frequency report

## Product Standards Applied

Designed according to CE Standards (LVD and EMC):
- IEC 61010-1
- IEC 60255-6
- IEC 60947-1
- Listed by Underwriters Laboratories Inc. E300908

## General Functions & Range of Applications

The Relayne GII provides electrical protection through the following general functions and setting ranges:

| Function | Range |
|----------|-------|
| Overvoltage detection | 10% up to -5% Rated Voltage |
| Undervoltage detection | 5% up to 20% Rated Voltage |
| Voltage Fault detection time | 1 to 30 sec |
| Voltage Unbalance detection | IN VUB > 33%, - OUT VUB < 28% |
| Voltage Single Phasing detection | 2% up to 10% Rated Voltage |
| Frequency Shift detection | +/-2% up to +/-10% rated Frequency |
| Trip Delay / Start Up Delay | 1 sec to 600 sec |

## Physical Dimensions and Weight

- Weight: 230 g (0.506 lb)
- Height: 68 mm

## Special Tools for Installation or Connection

- For terminal connection use screwdriver suitable for M2.5 screws
- For flat surface mounting use screwdriver suitable for screws (3/16" x 1/2")
- Voltmeter

## How to Order - Model Configuration

**GII [+] [S/blank] – [L] [Voltage] [Language]**

- **+** – Schedule Timer (Optional)
- **S** – Standard Connection
- **L** – Line to Line voltage measurement
- **Voltage Options:**
  - 120 – 120 VAC
  - 208 – 208/220/240 VAC
  - 480 – 440/480 VAC
- **Language:**
  - S – Spanish
  - E – English
  - P – Portuguese

## Technical Specifications

### A) Power Supply Circuit
(According to Voltage Model)

| Specification | 120 VAC | 208/220/240 VAC | 440/480 VAC |
|---------------|---------|-----------------|-------------|
| Supply Voltage Range | 95-125 VAC | 165-270 VAC | 350-580 VAC |

### E) Algorithms and Protection Functions

| Function | Level Settings |
|----------|-----------------|
| e.1 Undervoltage (UV) | 95, 115, 165, 225, 350, 460 |
| e.2 Overvoltage (OV) | 125, 145, 215, 270, 460, 580 |
| e.3 Voltage Hysteresis Threshold | 3, 6, 12 VAC |
| e.4 Voltage Unbalance Detection | (See detailed specifications) |

## Safety Information

**ATTENTION:** Only qualified technicians with knowledge about voltage protection relays and associated connections should do the installation, starting up, and maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

### Measures to be Taken into Consideration with Regards to EMC

**NOTICE:** This product has been designed for environment A. Use of this product in environment B may cause unwanted electromagnetic disturbances in which case the user may be required to take adequate mitigation measures.

## Connection Diagram

The relay provides connections for:
- L1, L2, L3 (Voltage Input - Line to Line)
- Control Relay Output (SPDT contact)

Use GIO PLUG (Optional) for serial communication with other devices.

### Output Status Indication:
- **Normal:** open/connected
- **Tripped:** connected/open

---

**Manufactured by:** Relayne / Genteca
**Headquarters:** Av. El Buen Pastor c/c Vargas, Edif. Alba, Piso 1, Oficina 1-A, Boleíta Norte, Caracas - Venezuela
**Contact:** Telfs.: (0212) 237.0711/1151/3477 / 238.7006 | Fax: 235.2497
**Email:** genteven@genteca.com.ve
**Website:** www.genteca.com.ve
**USA Office:** Buzzom ACSA 0158, P.O. Box 28537, Miami, FL 33102, USA

Document: MV-01-0017-B.03-E
```