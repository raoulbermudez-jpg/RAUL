---
title: "Genius GIII+ Installation Manual - Technical Specifications and Ordering Guide"
type: Technical
source: "GD-MAN-052-01-V2-US-C.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GIII+"
version_status: "vigente"
date_processed: "2026-05-10"
---

# Genius GIII+ Installation Manual

## Temperature Sensor Characteristics

| Parameter | Range | Unit | Notes |
|-----------|-------|------|-------|
| Compensation by Temperature (Bias) | YES/NO | — | User selection |
| Initial Temperature Setting (Ti) | 20 > 150 | °C | — |
| Maximum Motor Temperature (Tm) | 50 > 200 | °C | — |
| Sensor Type | Platinum 100 Ohm, 3 Wires (PTC 100) | — | Compatible with 2 and 4 wires |

## Events Control Characteristics

| Parameter | Range/Value | Unit |
|-----------|-------------|------|
| Real Time Clock | hh:mm_mm/dd/yy | UMT |
| Load Control by Events (schedule) | YES/NO | User selection |
| Schedule Timer (events) | 60 | User selection |
| Schedule Timer (holidays) | 20 | User selection |
| Trip Delay because of Accelerated Locked Rotor | 3 | Sec. |

## Communications and Other Special Functions

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Communication Protocol | MODBUS RTU @ 9600 8N1 | — |
| Communication Ports | GIO PORT (*) RS-485 | See User Manual |
| Address Range | 1 > 127 | — |
| History Buffer Memory | 20 last faults report (failure type, value, date, hour and time elapsed) | See User Manual |
| Parameters Block | 0000 Free, 0001–9999 Blocked | User selection |

(*) GIO Plug is required for GIO Port communication. It is available by separated.

## Immunity and Emissions - Electromagnetic Interference (EMC)
### Heavy Industrial Environment (B)

| Test Parameter | Standard |
|---|---|
| Electrostatic Discharge | EC 61000-4-2 |
| Immunity to Radio Frequency Test | EC 61000-4-3 |
| Electrical Fast Transients | EC 61000-4-4 |
| Surge Immunity Test | EC 61000-4-5 |
| Radio-Frequency Continuous Conducted | EC 61000-4-6 |
| Power Frequency Magnetic Field | EC 61000-4-8 |
| Voltage Dips, Short Interruptions and Voltage Variations | IEC 61000-4-11 |
| Harmonics and Interharmonics | IEC 61000-4-13 |
| Immunity Tests | IEC 61000-4-14, IEC 61000-4-27, IEC 61000-4-28 |
| Voltage Fluctuation Immunity | — |
| Unbalance Immunity Test | — |
| Variation of Power Frequency | — |

## Tripping Cold Curve

**Standards:** IEEE C37-112, IEC 60255-8

**Trip Classes:** 5, 10, 15, 20, 25, 30

**Notes:**
- Hot Curve = Cold Curve / 3
- Inom = Current value on GIII+ adjusted previously by the user
- Curve operates across load current range of 0 to 16.0 × Inom
- Trip time range spans from 0.1 to 100000 seconds

## How to Order GIII+

### Voltage
- **208** — 208/220/240 VAC
- **480** — 440/480 VAC

### Amperage
- **050** — 15 to 50 A
- **100** — 30 to 100 A
- **180** — 55 to 180 A
- **000** — CT EXTERNAL

### Language
- **S** — SPANISH
- **E** — ENGLISH
- **P** — PORTUGUESE

## Manufacturer Information

**Made and designed by:** Genteca, Generación de Tecnología C.A.

**Address:** Av. El Buen Pastor, cruce con Calle Vargas, Edificio Alba, Piso I, Local I-A, Boleita Norte, Caracas, 1070, República Bolivariana de Venezuela

**RLF:** J-00223173-4

**Contact:**
- Phone: +58-212-237.071 (Master)
- Fax: +58-212-235.2497
- E-mail: genteven@genteca.com.ve
- Website: www.genteca.com.ve

**USA Distribution:** Miami Breaker INC., 7060 NW. 52nd Street, Miami-Florida 33166, USA
- Phone: +1-786-3365780

---

**Note:** Technical data are valid at the time of printing. Manufacturer reserves the right to subsequent alterations.
