---
doc_type: IV-4-celeste-feed
project_id: portfolio-naming-ip-2026
domain: genteca
version: v1.0
author: Ivo
fecha: 2026-05-13
destinatario: Celeste (KB Librarian — decide estructura y ubicación en KB)
nota: >
  Este feed propone candidatos a conocimiento de largo plazo para la KB de Genteca.
  Celeste decide si integrar, cómo estructurar y dónde ubicar en la KB.
  Ivo propone; Celeste decide. Ivo no modifica la KB.
---

# IV-4 — Celeste Feed
## Portfolio Naming IP 2026 (Genteca) — Candidatos a KB largo plazo

---

## Contexto para Celeste

El proyecto `portfolio-naming-ip-2026` generó conocimiento corporativo de Genteca que no existía estructurado antes: la política de naming explícita, el mapping de tecnologías diferenciadoras actualizado, el patrón de gobernanza legal de naming, y la doctrina jurídica aplicada con casos reales. Los 4 bloques a continuación son los candidatos de mayor valor para la KB de largo plazo. Cada uno incluye la fuente primaria dentro del proyecto y la propuesta de ubicación en KB.

---

## Candidato KB-1 — Política de Naming Genteca (conocimiento corporativo)

**Qué es:** El conjunto de decisiones implícitas y explícitas sobre cómo Genteca nombra sus tecnologías, emergidas durante este proyecto y en el proyecto predecesor `2026-05-07_marcas-anglicismos-junta`.

**Fuente primaria:** Charter `_governance/00-project-charter.md` §3 (8 decisiones estructurales), VA-6 `05-solenne-vael-naming/Vael_VA-6_naming-family-rules_v1.md` §2 y §3, SO-1 (patrón estético de la familia).

**Contenido a extraer para KB:**

| Principio | Descripción | Fuente |
|-----------|-------------|--------|
| Portafolio 100% anglicismos | Todos los nombres del portafolio IP de Genteca son en inglés — decisión estratégica Owner, no solo para NODO específicos | Charter §3 decisión 5 |
| Stand-alone clase 9 | Cada nombre es marca independiente, sin depender del umbrella de línea (Exceline / Genius) | Charter §3 decisión 3 |
| Family-first morfología CamelCase | El estándar morfológico del portafolio es CamelCase sin espacio; guión solo para familia GIO-* y prefijo Thermo- en NODO-C | VA-6 §2.5 |
| Potencia comercial antes que factibilidad | El filtro de curación es primero impacto de audiencia, luego factibilidad SAPI/IMPI — un nombre registrable débil no entra | Charter §2; AU-1 §3 |
| Raíz exclusiva por nodo | Cada nodo tecnológico tiene raíz exclusiva en la familia; no se repiten raíces entre nodos distintos | VA-6 §3.3 |
| Sufijos prohibidos universales | -Pro, -Plus, -Max, -Smart, -Tech, -Stop — lista de sufijos genéricos sin valor diferenciador en clase 9 | VA-6 §2.2 |
| Anti-mensajes por nodo (lo que no se dice) | Lista de claims que no pueden sostenerse aunque suenen bien — incluye "único", "exclusivo", "propietario" sin RTB | VA-1 §3 |

**Propuesta de ubicación en KB Genteca:** `02-knowledge-base/03-genteca/ip-naming/politica-naming-genteca.md` (nuevo documento) o integración en el KB entry de naming existente si Celeste tiene una.

---

## Candidato KB-2 — Mapping de tecnologías diferenciadoras Genteca (actualizado 2026-05-13)

**Qué es:** El inventario más completo y actualizado de los 8 nodos tecnológicos diferenciadores del portafolio Exceline / Exceline Profesional / Genius, con mecanismo técnico, RTBs verificables, diferenciación competitiva, y productos donde vive. Representa el estado del arte del conocimiento técnico de Genteca actualizado a la fecha.

**Fuente primaria:** VR-1 `02-vera-orlan/Vera_VR-1_tech-inventory-hybrid_v1.md` (mecanismos + RTBs), OL-1 `02-vera-orlan/Orlan_OL-1_differentiation-matrix_v1.md` (diferenciación competitiva), 01-Anexo-Tecnico `06-three-pack/01-Anexo-Tecnico_v1.md` (versión integrada final).

**Los 8 nodos a catalogar:**

| Nodo | Tecnología | Línea primaria | Estado competitivo (Orlan) | RTB clave |
|------|-----------|----------------|---------------------------|-----------|
| NODO-A | Reconexión temporal aleatoria post-falla | Exceline / Exceline Profesional | Amarillo | Retardo ajustable 5-300 s con componente aleatoria documentada; previene pico de demanda simultáneo |
| NODO-B | Detección sub-ciclo de perturbaciones de voltaje (flicker + curva inversa V-t) | Exceline / Exceline Profesional | Verde | 20 ms de detección de flicker (GSM-L HDE v10) — sin equivalente publicado en segmento residencial/comercial |
| NODO-C | Modelo térmico NTC integrado en protector monofásico | Exceline | Amarillo | NTC embebido en GSM-MB/RB/RE como feature estándar de serie sin módulo adicional; parámetros cuantitativos pendientes I+D |
| NODO-D | Curva inversa I-t diferenciada cold/hot (imagen térmica) | Exceline Profesional / Genius | Rojo (función IEC estándar) | Curva caliente = fría/3; clase ajustable 5-30; memoria térmica 2 h; IEC 60255-8 / IEEE C37.112 |
| NODO-E | Registro forense histórico de fallas con timestamp | Genius (GIII+MV primario) | Amarillo | 100 últimas fallas (GIII+MV, verificado HDE primaria); 20 fallas gama Genius estándar; 10× más que Rockwell E300 |
| NODO-F | Bloqueo permanente tras tercera falla de corriente recurrente | Exceline Profesional / Genius | Amarillo | 3 fallas de corriente en < 30 min → desconexión permanente + reset manual; disparo < 1 s (GOC HDE); documentado en toda la gama Genius |
| NODO-G | Memoria de estado y reanudación de tarea post-corte | Exceline Profesional (GRN-MV) | Verde | Texto literal HDE GRN-MV v9: "retoma automáticamente la última función al restablecerse la energía, sin requerir intervención del usuario"; sin equivalente nombrado en competencia directa |
| NODO-H | Ecosystem GIO (conectividad industrial integrada) | Genius (gama completa) | Amarillo | GIO PORT en todos los relés Genius; hasta 32 relés en bus RS-485; GIO-Tool (software propietario); MODBUS RTU sin módulo adicional en segmento LatAm |

**Nota de actualización:** La KB Genteca estaba en 2,237 specs al inicio del proyecto. Los 8 nodos aquí capturan el conocimiento sintetizado derivado de esas specs. La KB no cambia — este es el conocimiento derivado (interpretado y diferenciador), no la documentación primaria.

**Propuesta de ubicación en KB Genteca:** `02-knowledge-base/03-genteca/portafolio-tecnologias/nodos-registrables-2026.md` (nuevo documento que complementa las HDEs existentes con la capa de diferenciación competitiva y naming IP).

---

## Candidato KB-3 — Patrón de gates Bruna para naming IP (clase 9 vs software vs sectorial)

**Qué es:** El framework de 8 gates de Bruna para evaluar riesgos de naming en clase 9 (descriptividad, colisión por sector, diferenciación por jurisdicción), derivado del BR-2 y BR-3 de este proyecto. Es conocimiento de gobernanza legal transversal al sistema /RAUL/.

**Fuente primaria:** `04-bruna/Bruna_BR-2_approval-set_v1.md` y `04-bruna/Bruna_BR-3_policy-application_v1.md`.

**Los 3 patrones de riesgo a catalogar:**

**Clase 9 amplia — riesgo de colisión por sub-sector:**
- Software/apps: vocabulario de tecnología de la información en clase 9 puede colisionar con el mismo nombre en software (caso TaskMemory → IMPI MX)
- Seguridad física: raíces "Lock", "Safe", "Guard" tienen presencia en cerraduras electrónicas y sistemas de acceso físico en clase 9
- Iluminación/LED: nombres relacionados con calidad de energía pueden colisionar con productos LED en la misma clase (caso FlickerGuard)

**Clase 9 — riesgo de descriptividad por función estándar IEC:**
- Cuando el nombre describe literalmente el mecanismo de una norma IEC/IEEE universalmente implementada (caso ThermalCurve → IEC 60947-4-1), la descriptividad es causal de inadmisibilidad en SAPI VE (art. 34 LPI 1955) e IMPI MX
- El override del Owner no ayuda en este caso: confirmar que la función existe en toda la gama refuerza el argumento de descriptividad, no lo contrarresta
- La salida es: (a) documentar un RTB propietario que diferencie la implementación del estándar, o (b) cambiar el nombre por uno que no describa el mecanismo

**Diferenciación por jurisdicción VE/MX:**
- SAPI Venezuela aplica doctrina de equivalencia perceptual (consumidor venezolano promedio como estándar)
- IMPI México aplica criterios más cercanos a USPTO, especialmente para clase 9 con vocabulario de software
- La decisión de Bruna puede ser diferenciada por jurisdicción para el mismo nombre (caso TaskMemory: aprobado SAPI VE / contingencia IMPI MX)
- Candidato a BR-5 Precedente #8 si Owner lo ratifica

**Propuesta de ubicación en KB sistema /RAUL/:** `02-knowledge-base/03-genteca/governance/bruna-naming-ip-gates.md` — o en la KB transversal del sistema si Celeste considera que el patrón aplica a todos los dominios.

---

## Candidato KB-4 — Doctrina equivalencia perceptual SAPI aplicada en casos reales

**Qué es:** La doctrina de equivalencia perceptual de SAPI Venezuela (art. 34 LPI 1955) aplicada a casos concretos del portafolio Genteca. Antes de este proyecto, la referencia era teórica (`reference_sapi_venezuela_quick.md`). Ahora hay 7 casos de aplicación con razonamiento de Bruna documentado.

**Fuente primaria:** `04-bruna/Bruna_BR-1_risk-notes_v1.md` (Gates 3, 5, 6, 7), `04-bruna/Bruna_BR-2_approval-set_v1.md` (decisiones formales), `04-bruna/Bruna_BR-3_policy-application_v1.md`.

**Los 7 casos de aplicación:**

| Caso | Nombre | Resultado | Razonamiento de equivalencia perceptual |
|------|--------|-----------|----------------------------------------|
| Caso 1 | Thermo-Safe | Aprobado con caveat (Caso A) | "Thermo-Safe" ≠ "PROTECCION TERMICA". "Safe" no es el traductor literal de "Proteccion" en uso cotidiano venezolano. La combinación crea signo de fantasía distinto de la descripción funcional en español del empaque. |
| Caso 2 | FlickerGuard | Aprobado con contingencia | "Flicker" es técnico (IEC 61000-4-15), no uso cotidiano en español venezolano ("parpadeo" es el término cotidiano). "Guard" no describe el mecanismo específico. El consumidor venezolano no percibe FlickerGuard como descriptor del producto. |
| Caso 3 | TripleLock | Aprobado con contingencia | "Lock" no es uso cotidiano en español venezolano para bloqueo eléctrico de relé. La combinación "TripleLock" no es percibida como descriptor de "bloqueo eléctrico tras triple falla" por el consumidor venezolano. El riesgo es colisión sectorial, no descriptividad del producto eléctrico. |
| Caso 4 | TaskMemory | Aprobado para VE (diferenciado para MX) | Consumidor venezolano de un GRN-MV (relé de nivel de bombeo) no asocia "TaskMemory" con software de gestión de procesos informáticos. La percepción es "memoria de tareas" en sentido amplio, no en sentido informático. Aplica para SAPI VE; riesgo mayor en IMPI MX. |
| Caso 5 | ForensLog | Aprobado | "Forensic" no es uso cotidiano venezolano/mexicano para el producto eléctrico. "Log" en español no es término cotidiano para el consumidor no técnico de la función del relé. La combinación tiene perfil de fantasía bajo equivalencia perceptual. |
| Caso 6 | StaggerStart | Aprobado (limpio) | "Stagger" es técnicamente específico y raramente usado en nombres de clase 9 en LatAm. No es descriptivo para el consumidor venezolano o mexicano promedio. |
| Caso 7 | ThermalCurve | RECHAZADO | La equivalencia perceptual NO protege cuando un examinador técnico de SAPI (no el consumidor promedio) evalúa la solicitud FM-02 para un dispositivo de protección en Clase 9 y tiene criterio suficiente para identificar que "Thermal" + "Curve" describe el mecanismo primario del producto. La descriptividad se evalúa también desde la perspectiva del examinador especializado. |

**Lección clave:** La equivalencia perceptual SAPI protege nombres que el consumidor promedio venezolano no percibe como descriptivos. Pero cuando el examinador tiene conocimiento técnico del sector (caso relés de protección eléctrica), la evaluación incluye la perspectiva del técnico, no solo del consumidor final. Este matiz no estaba documentado en `reference_sapi_venezuela_quick.md` — es conocimiento nuevo derivado de este proyecto.

**Propuesta de ubicación en KB sistema /RAUL/:** Actualización de `reference_sapi_venezuela_quick.md` con sección nueva "Casos de aplicación práctica — portfolio-naming-ip-2026" o documento separado `sapi-venezuela-equivalencia-perceptual-casos.md`.

---

*Ivo — IV-4 Phase 8. Feed entregado a Celeste. Fecha: 2026-05-13.*
*Celeste decide estructura e integración en KB. Ivo no modifica la KB.*
