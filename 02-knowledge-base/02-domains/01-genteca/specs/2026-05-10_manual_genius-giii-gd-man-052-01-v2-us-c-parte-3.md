---
title: "GIII Installation Manual - Technical Specifications and Ordering Guide"
type: Technical
source: "GIII_GD-MAN-052-01-V2-US-C.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GIII"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GIII Installation Manual - Technical Specifications and Ordering Guide

## Temperature Sensor Characteristics

| Parameter | Setting | Range | Unit |
|-----------|---------|-------|------|
| Trip Delay (Accelerated Locked Rotor for Heavy Industrial Environment) | 3 Sec | - | - |
| Compensation by Temperature (Bias) | YES/NO | User selection | - |
| Initial Temperature Setting (Ti) | 20 | >150 | Degrees |
| Maximum Motor Temperature (Tm) | 50 | >200 | Degrees |
| Sensor Type | Platinum 100 Ohm, 3 Wires (PTC 100) | Compatible with 2 and 4 wires | - |

## Events Control Characteristics

| Parameter | Setting | Range | Unit |
|-----------|---------|-------|------|
| Real Time Clock | hh:mm mm/dd/yy | UMT | - |
| Load Control by Events (schedule) | YES/NO | User selection | - |
| Schedule Timer (events) | 60 | User selection | - |
| Schedule Timer (holidays) | 2 | User selection | - |

## Communications and Other Special Functions

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Communication Protocol | MODBUS RTU @ 9600 8N1 | - |
| Communication Ports | GIO PORT (*) / RS-485 | (*) GIO Plug is required for GIO Port communication. Available separately. |
| Address Range | 1 - 127 | - |
| History Buffer Memory | 20 last faults report | Includes failure type, value, date, hour and time elapsed |
| Parameters Block | 0000 Free, 0001 - 9999 Blocked | User selection |

## Immunity and Emissions - Electromagnetic Interference (EMC)

### EMC Standards Compliance

| Standard | Test Description |
|----------|------------------|
| EC 61000-4-2 | Electrostatic Discharge |
| EC 61000-4-3 | Immunity to Radio Frequency Test |
| EC 61000-4-4 | Electrical Fast Transients |
| EC 61000-4-5 | Surge Immunity Test |
| EC 61000-4-6 | Radio-Frequency Continuous Conducted |
| EC 61000-4-8 | Power Frequency Magnetic Field |
| IEC 61000-4-11 | Voltage Dips, Short Interruptions and Voltage Variations |
| IEC 61000-4-13 | Harmonics and Interharmonics Immunity Tests |
| IEC 61000-4-14 | Voltage Fluctuation Immunity |
| IEC 61000-4-27 | Unbalance Immunity Test |
| IEC 61000-4-28 | Variation of Power Frequency |

## Tripping Curve Standards

- IEEE C37-112
- IEC 60255-8

### Tripping Curve Classes

The device supports the following tripping curve classes with cold curve characteristics:

- Class 5
- Class 10
- Class 15
- Class 20
- Class 25
- Class 30

**Notes:**
- Hot Curve = Cold Curve / 3
- Inom = Current value on GIII adjusted previously by the user

The tripping curve operates across a load range from 0 to 16.0 times Inom (Current Load / Inom).

## How to Order GIII According to Customer Needs

### Configuration Format
**GIII + [VOLTAGE] + [AMPERAGE] + [LANGUAGE]**

### Voltage Options
- 208 — 208/220/240 VAC
- 480 — 440/480 VAC
- 180 — 55 to 180 A
- 000 — CT EXTERNAL

### Amperage Options
- 050 — 15 to 50 A
- 100 — 30 to 100 A

### Language Options
- S — SPANISH
- E — ENGLISH
- P — PORTUGUESE

## Manufacturer Information

**Made and designed by:**
Genteca, Generación de Tecnología C.A.
RIF: J-00223173-4
Av. El Buen Pastor, cruce con Calle Vargas
Edificio Alba, Piso 1, Local 1-A
Boleíta Norte, Caracas, 1070
República Bolivariana de Venezuela

**Contact:**
- Phone: +58-212-237.071 (Master)
- Fax: +58-212-235.2497
- Email: genteven@genteca.com.ve
- Website: www.genteca.com.ve

**Distributor (US):**
Miami Breaker INC.
2060 NW 52nd Street
Miami, Florida 33142-6605
Phone: +1-786-336-5780

---

**Note:** Technical data are valid at the time of printing. The manufacturer reserves the right to subsequent alterations.
