# Precedents & Guidelines Memo — Risk & Claims (transversal)
**Mantenido por:** Bruna — Risk & Claims Governance Lead
**Ubicacion canonica:** `04-system/03-governance/`
**Ultima actualizacion:** 2026-05-03

---

## Por tipo de claim

### Afirmaciones absolutas (superlativos: "el mas", "unico", "siempre")

#### Precedente #1 — 2026-05-03 — Superlativo de velocidad con dato cuantitativo en mercado con alta opacidad competitiva

**Dominio del caso original:** Genteca
**Caso original:** Bruna_gate_empaque_v1 §2 Claim A / BR-2 Genteca entrada #1
**Producto:** Exceline GSM-MB / GSM-RB / GSM-RF / GSM-RE (empaque, lanzamiento Q2 2026)
**Claim evaluado:** "El mas rapido ante parpadeos (< 0,03 s)"

**Decisión:** APROBADO CON CAVEAT

**Criterio sentado:**

Un superlativo de performance ("el mas rapido", "el mas veloz", "el de mayor potencia") combinado con un dato cuantitativo propio verificable es APROBABLE en un mercado con alta opacidad competitiva (competidores no publican el dato de forma sistematica) cuando se cumplen las tres condiciones siguientes:

1. El dato cuantitativo propio existe y esta medido bajo condicion reproducible (laboratorio interno o certificado externo). La declaracion del Owner o del responsable tecnico de I&D confirmatoria de la medicion es suficiente para el gate conceptual; el documento de laboratorio debe existir antes de la produccion final del material.

2. No existe competidor con dato PUBLICADO igual o superior al dato propio. La ausencia de publicacion del dato por parte de un competidor no equivale a que ese competidor tenga un dato mejor no comunicado — es evidencia de que ese competidor no puede o no quiere defender el atributo publicamente. Esa asimetria de informacion opera A FAVOR del claim superlativo del que si publica el dato.

3. La formulacion combina el superlativo con el dato cuantitativo en el mismo claim. Esa estructura es la mas defensible: si el superlativo es cuestionado, el dato cuantitativo sobrevive como afirmacion tecnica autonoma.

**Regla Owner aplicada (2026-05-03):** En mercados donde los competidores no publican el atributo de forma verificable, asumir que Genteca es el unico / el mas rapido. Nunca usar "uno de los mas rapidos" porque comunica mediocridad y es innecesariamente debil cuando la evidencia disponible respalda el superlativo.

**Riesgos asumidos con esta regla:**
- Un competidor puede tener un dato no publicado que eventualmente emerja. Mitigation: el laboratorio propio puede defender el dato ante cualquier reto.
- Un competidor puede publicar un dato mejor despues del lanzamiento. Mitigation: la condicion de revision (ver abajo) activa un BR-4 si eso ocurre.
- La ausencia de dato publicado por un competidor puede reflejar ausencia real del atributo o simplemente falta de comunicacion. La regla asume que si un competidor no lo comunica, no puede defenderlo — lo cual es razonable para la defensa legal del claim.

**Condicion de revision:**
Este criterio debe revisarse si:
- Un competidor venezolano publica (en datasheet oficial, no en material de distribuidor) un dato de velocidad de desconexion ante parpadeos igual o inferior al dato propio de Genteca. En ese caso: Orlan hace refresh de OL-5, Bruna reevalua el superlativo y puede emitir BR-4 si el material ya esta publicado.
- El laboratorio de I&D de Genteca modifica el dato oficial (hacia arriba o hacia abajo). En ese caso: Vera hace refresh de brief tecnico, Bruna reevalua.
- El claim ya esta publicado en empaque impreso y el competidor reta el superlativo con evidencia verificable. En ese caso: protocolo de incidente §6.7 de Bruna; decision de mantener / aclarar / corregir / retirar.

**Formulacion prohibida (ratificada como precedente):**
"Uno de los mas rapidos" — prohibida por decision Owner 2026-05-03, ratificada como norma de precedente. No usar en ningun dominio del sistema /RAUL/ para claims de performance en mercados donde el dato propio es el mas alto conocido.

**Casos posteriores que aplicaron este precedente:** (pendiente — actualizar cuando aplique)

---

#### Precedente #2 — 2026-05-03 — Superlativo de exclusion ("unico") requiere ausencia verificada del atributo en competidores

**Dominio del caso original:** Genteca
**Caso original:** Bruna_gate_empaque_v1 §2 Claim B / BR-2 Genteca entrada #2
**Claim evaluado:** "El unico en proteger tecnologia inverter"

**Decision:** RECHAZADO

**Criterio sentado:**

El superlativo de exclusion ("el unico", "la unica marca", "el unico producto") requiere evidencia de que NINGUN competidor relevante tiene el atributo nombrado. Cuando existen competidores que lo tienen y lo comunican, el claim "unico" es factualmente falso y debe rechazarse sin excepcion.

La alternativa correcta cuando el atributo no es exclusivo pero el ARGUMENTO TECNICO QUE LO SUSTENTA si lo es: formular el claim sin el superlativo de exclusion y dejar que el RTB diferenciador haga el trabajo. En el caso de inverter: "Protege tecnologia Inverter" no es exclusivo, pero "Protege tecnologia Inverter — tiempo de respuesta < 0,03 s" si lo es, porque ninguno de los competidores que usan el claim de inverter puede respaldar ese dato.

**Condicion de revision:**
Este criterio no tiene condicion de revision: es una regla absoluta. Si los competidores que tienen el atributo desaparecen del mercado, el claim "unico" puede reconsiderarse con refresh de Orlan.

**Casos posteriores que aplicaron este precedente:** (pendiente)

---

### Comparativos directos (vs marca tercero)

#### Precedente #3 — 2026-05-03 — Comparativos directos de marca prohibidos en empaque; permitidos en argumentario interno y sustento de Junta

**Dominio del caso original:** Genteca
**Caso original:** Bruna_gate_empaque_v1 §2 Claims A-C y temas sensibles Vael VA-5 §11
**Rango de aplicacion:** Empaques fisicos de producto y materiales de punto de venta publicos

**Criterio sentado:**

Los comparativos directos (mencionar marca o producto de un competidor por nombre en el claim) estan prohibidos en empaque fisico y en materiales de punto de venta publicos para el dominio Genteca (mercado venezolano). La razon no es solo legal (riesgo de publicidad comparativa bajo la Ley de Proteccion al Consumidor y al Usuario, Arts. relativos a publicidad engañosa y denigratoria) sino tambien estrategica: el empaque llega al distribuidor y al instalador antes que a la competencia, y un comparativo directo invita a la retaliacion.

El comparativo indirecto (superlativo + dato cuantitativo propio, sin nombrar al competidor) es la forma correcta de comunicar diferenciacion. "El mas rapido ante parpadeos (< 0,03 s)" es un comparativo indirecto — cualquier competidor puede verificarlo contra su propio dato, pero el empaque no denigra a nadie por nombre.

Los datos comparativos directos (ej. "WellSpec: 200-300 ms; Genteca: < 30 ms") son material de argumentario de ventas interno y de presentacion a Junta Directiva — no de empaque.

**Casos posteriores que aplicaron este precedente:** (pendiente)

---

### Claims sobre garantias y resultados

#### Precedente #4 — 2026-05-03 — Garantia de resultado de proteccion del equipo no usable sin RTB especifico y asuncion de obligacion legal

**Dominio del caso original:** Genteca
**Caso original:** Bruna_gate_empaque_v1 §2 Claim L (rechazo preventivo)

**Criterio sentado:**

Cualquier formulacion del tipo "garantiza la proteccion del equipo", "evita daños al equipo", "su equipo estara protegido" implica una garantia de resultado que, bajo la Ley de Proteccion al Consumidor y al Usuario venezolana (y equivalentes en Colombia/Mexico si el producto se exporta), puede generar obligacion legal de reparar o compensar al consumidor cuando el equipo resulta dañado pese al protector.

Esta clase de claims requiere:
1. Un RTB tecnico que demuestre que el equipo queda protegido en TODOS los casos de uso relevantes (no solo en los casos favorables).
2. Revision por asesorıa legal externa antes de aprobar.

Para la linea GSM: el protector protege ante parpadeos y fluctuaciones de voltaje, pero no ante todos los fenomenos electricos que pueden dañar un equipo (transientes de alta energia, fallas de ground, etc.). Por tanto, no existe RTB que sostenga una garantia de resultado universal. El claim es rechazado preventivamente en todas sus formulaciones.

**Condicion de revision:** Si Vera desarrolla un RTB tecnico especifico que demuestre proteccion verificada ante un tipo concreto de evento (ej. "protege el compresor ante parpadeos de red en el 100% de los casos bajo las condiciones de instalacion especificadas") y Owner decide asumir la obligacion legal correspondiente, el claim puede reconsiderarse con asesorıa legal. Bruna sola no puede aprobarlo.

**Casos posteriores que aplicaron este precedente:** (pendiente)

---

## References

- WORKSTREAM_v5_innovaciones.md §Regla de gateo de claims superlativos (2026-05-03)
- Bruna_gate_empaque_v1.md §2 Claims A, B, C, L (decisiones originales de este precedente)
- BR-2 Genteca — `03-projects/genteca/_governance/` (entradas #1 a #13)
- Vera_brief_tecnico_v1.md (facts tecnicos que sustentan los RTBs)
- Orlan_competencia_v1.md Secciones 1, 2, 4 (landscape competitivo Venezuela)
- RISK-POLICY.md v1.0 (2026-04-25) — gobernanza general del sistema
