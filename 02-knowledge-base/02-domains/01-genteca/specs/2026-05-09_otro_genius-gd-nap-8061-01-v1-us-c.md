---
title: "GIII+ Total Motor Protection Relay with External Current Transformers"
type: Technical
source: "GD-NAP-8061-01-V1-US-C.pdf"
product_line: "Genius"
document_type: "nota-aplicacion"
product_code: "GIII+208000, GIII+480000"
date_processed: "2026-05-09"
---

# GIII+ Application Note
## Total Motor Protection Relay with External Current Transformers

**Attention:** This application note complements the sheet of specifications and the installation manual of the product.

## 1. GIII+ Connection's Diagram with External Current Transformers

The GIII+ relay connects to external current transformers via three phases (L1, L2, L3) with auxiliary relay configuration and digital inputs. Wire gauge AWG 14 is specified for connections.

## 2. External CT Selection and Applicable Models

### Applicable Models
- GIII+208000
- GIII+480000 M

### Key Information

a) The models GIII+208000 and GIII+480000 are used exclusively with external CTs. These models protect motors up to 660A nominal current.

b) The user must specify the nominal motor current to select the appropriate current transformer rank according to the relation "/5".

c) The user must set up the GIII+ with external CT following the adjustment instructions in this application note. All other functions and protections remain as specified in the installation instructions for GIII+.

d) Calibration of the GIII+ remains warranted provided external CTs are commercial class 1 with secondary 5A.

### External CT Suggested According to Nominal Current

| Rank of Nominal Current | Current Transformers Relation /5 |
|-------------------------|----------------------------------|
| 150-200A | 600 |
| 190-250A | 750 |
| 200-260A | 800 |
| 250-330A | 1000 |
| 300-350A | 1200 |
| 375-500A | 1500 |
| 500-660A | 2000 |

**Example:** If a motor consumes a nominal current of 350 amperes, the external toroids to select will be a value of 1200/5.

## 3. Adjustment of the External CT and Nominal Current in the Current Protection Menu

### Step-by-Step Adjustment Procedure

**Steps a-f: Setting the CT Relation**

a) From the Operation screen, press Up & Down combination to navigate to the Current Adjustment menu.

b) Press Up or Down to get to CURRENT ADJUST option.

c) In CURRENT ADJUST, press SELECT.

d) In CT menu, press the SELECT button.

e) In CT, press Up or Down to get to the adequate /5 relation (see table above).
   - *Example:* For an engine with current FLA=350A, change relation to 1200/5.

f) After marking the desired relation, press SELECT.

**Steps g-k: Setting the Nominal Current**

g) Press Up & Down combination to navigate to NOMINAL I in the menu.

h) NOMINAL I appears on display (example shows 300A).

i) Press Up or DOWN to get to the desired value.
   - *Example:* Change value from 300A to 350A.

j) Adjust the desired value by pressing SELECT.

k) Return to Current Menu with the CT and NOMINAL I values properly set.

**Note:** Continue with other current adjustments or return to the MAIN MENU. All other functions are adjustable in a similar manner to the actions described in the installation manual.

---

**Manufacturer Information:**

Designed and made by Gente, Generación de Tecnología C.A.
- R.I.F.: J-00223173-4
- Address: Av. El Buen Pastor, cruce con Calle Vargas, Edificio Alba, Piso 1, Local 1-A, Boleíta Norte, Caracas, 1070, República Bolivariana de Venezuela
- Phone: +58-212-237.0711 (Master)
- Fax: +58-212-235.2497
- Email: genteven@genteca.com.ve
- Website: www.genteca.com.ve

Distributed in USA by Miami Breaker INC.
- Address: 7060 NW. 52nd Street, Miami, Florida 33166, USA
- Phone: +1-786-3365780