---
title: "GI Phase Voltage Relay - Application Notes"
type: Technical
source: "NOTAS DE APLICACIONES GI - Ingles.pdf"
product_line: "Genius"
document_type: "nota-aplicacion"
product_code: "GI"
date_processed: "2026-05-09"
---

# GI Phase Voltage Relay - Examples of Typical Applications

## Terminal Designation

| Terminal | Designation |
|----------|-------------|
| 1 | VOLTAGE INPUT L1 (Phase R) |
| 2 | VOLTAGE INPUT L2 (Phase S) |
| 3 | VOLTAGE INPUT L3 (Phase T) |
| 4 | NOT USED |
| 5 | NOT USED |
| 6 | TRIP RELAY (Contactor or line starter circuit) |
| 7 | COMMON |
| 8 | AUXILIARY RELAY (Alarm) |

### Start Mode Configuration

- **MANUAL**: Press Start push button to activate the relay after a failure
- **AUTO**: Automatic activation after voltage failure detection

### Relay States

**Tripped:**
- 7 - 8 connected
- 6 - 7 open

**Normal:**
- 7 - 8 connected
- 6 - 7 open

## Three Phase Load Protection (Example 1)

**Configuration:** Place start mode slide-switch in AUTO position

**Application:** Use with external switches or contacts (manual or remote) for start and stop control

**Notes:**
- The Voltage Input terminals L1-L2-L3 must be connected in parallel before the Contactor inputs and its associated line starter circuit
- External switches control load stopping or starting when AUTO mode is selected

## Three Phase Load Protection (Example 2)

**Configuration:** Place start mode slide-switch according to application (AUTO or MANUAL)

**Manual Start Mode Option:**
- Slide-switch set to MANUAL position
- START Push Button required to activate CONTACTOR after a failure and corresponding start-up delay

**Auto Start Mode Option:**
- Slide-switch set to AUTO position
- GI automatically activates CONTACTOR after a failure and corresponding start-up delay

**Notes:**
- GI disconnects the CONTACTOR when voltage failures occur
- The Voltage Input terminals L1-L2-L3 must be connected in parallel before the Contactor inputs and its associated line starter circuit

## HVAC / Central Air Conditioned (Split Systems)

**Configuration:** Place start mode slide-switch in AUTO position

**Application:** Indoor installation with thermostat control

**Features:**
- Control voltage interrupted when circuit voltage failure occurs
- Primary Circuit of Control Transformer deactivated by GI during any voltage failure
- Integration with Fan Relay and Compressor Contactor

**Notes:**
- The Voltage Input terminals L1-L2-L3 must be connected in parallel before the Contactor inputs and its associated line starter circuits

## Industrial Applications - Motor Protection Against Voltage Failures

### Without Disconnecting Switch

- Circuit Breaker
- Contactor
- Thermal Protection
- Connection in series to contactor coil and its associated control circuit/Starter line circuit

### With GI

- Circuit Breaker
- GI relay
- Contactor
- Thermal Protection
- Connection in series to contactor coil and its associated control circuit/Starter line circuit

**Notes:**
- The Voltage Input terminals L1-L2-L3 must be always connected in parallel before the Contactor inputs and its associated line starter circuit

## Motor Control Center

**Configuration:** Multiple GI relays in a distributed control setup

**Network Features:**
- GIO Link / RS485 communication protocol
- ModBUS RTU Protocol support
- Network connectivity: LAN, WAN, etc.
- Optional GIO Plug adapter for serial communication

**System Capabilities:**
- Remote configuration of each relay via user-friendly software
- Supervision of each protection relay (measurements, internal status review, history data)
- Remote control of the load by activation or deactivation of output contacts
- Connection to PC through optional adapter "GIO Plug"

**Network Capacity:**
- GIO Link Network connects PC to protection relays
- 1 to 32 devices connectable (or up to 126 devices using up to 3 repeaters of expansion)

**Notes:**
- Each GI and other protection relays from the GENIUS series can be connected to a PC through the optional adapter "GIO Plug", which converts digital signals to RS485 standard (MODBUS RTU protocol)
- For detailed information refer to User Manual