---
doc_type: IV-3-sira-feed
project_id: portfolio-naming-ip-2026
domain: genteca
version: v1.0
author: Ivo
fecha: 2026-05-13
destinatario: Sira (Archive, Version & Recycling Librarian)
nota: >
  Este feed propone piezas reutilizables del proyecto para indexación en el catálogo
  de reciclaje. Sira decide estructura de catálogo y condiciones de reutilización.
  Ivo no indexa — solo entrega el feed con la propuesta.
---

# IV-3 — Sira Feed
## Portfolio Naming IP 2026 (Genteca) — Piezas reutilizables para futuros proyectos

---

## Contexto para Sira

El proyecto `portfolio-naming-ip-2026` es el primer proyecto de naming portfolio IP del sistema /RAUL/. Produjo 4 tipos de artefactos reutilizables en cualquier dominio que requiera un proceso similar: (a) un framework de decisiones estructurales para organizar un portafolio de naming, (b) reglas de familia de nombres, (c) un patrón de gates de colisión, y (d) la estructura del three-pack como entregable a abogado marcario. Las propuestas de reciclaje a continuación están organizadas por tipo de artefacto y dominio destino potencial.

Dominios que pueden activar reciclaje próximamente según estado del sistema /RAUL/:
- **Plenus** (2do dominio — activación pendiente per session handoff 2026-05-12)
- **Panama** (dominio nuevo activo — hipoteca, contratos, reparaciones; menos probable para naming IP pero posible si Plenus genera portafolio de productos)

---

## 1. Las 8 decisiones estructurales como template para naming portfolio

**Artefacto fuente:** `C:\Raul\03-projects\genteca\portfolio-naming-ip-2026\_governance\00-project-charter.md` §3

**Propuesta de reciclaje:** Las 8 decisiones del charter (`00-project-charter.md §3`) configuran un framework de arranque para cualquier proyecto de naming portfolio en cualquier dominio. Son parametrizables:

| Decisión | Parámetro adaptable por dominio |
|----------|--------------------------------|
| 1. Candidatos por tecnología | Número a fijar (4 es un valor probado; puede ser 3 o 5 según complejidad) |
| 2. Granularidad de nodos | Híbrida vs granular vs agregada — depende del portafolio de tecnologías del dominio |
| 3. Arquitectura de marca | Stand-alone vs familia umbrella — decisión estratégica por dominio |
| 4. Override de feature universal | Adaptable a cualquier decisión del Owner de asumir presencia universal de una función sin auditoría exhaustiva |
| 5. Preservación de nombres previos | Aplica si hay proyecto previo con nombres validados (como el batch 1 de Genteca) |
| 6. Jurisdicciones | VE + MX son el par base para Genteca; Plenus puede requerir US + MX o solo MX |
| 7. Audiencia del deck | Siempre definir: abogado marcario (no Junta, no marketing) |
| 8. Checkpoints Owner | Mínimo 2 (tras inventario + tras three-pack) — recomendado mantener sin excepción |

**Condición de uso:** Leer el charter completo de Genteca como referencia antes de configurar el charter de un nuevo dominio. No copiar literalmente — parametrizar.

**Nivel de reutilización estimado:** Alto. Este framework reduce el tiempo de arranque de un nuevo proyecto de naming portfolio de cero a ~30% del trabajo (el Owner responde 8 preguntas estructuradas en lugar de partir desde blanco).

---

## 2. VA-6 Naming Family Rules como patrón reutilizable

**Artefacto fuente:** `C:\Raul\03-projects\genteca\portfolio-naming-ip-2026\05-solenne-vael-naming\Vael_VA-6_naming-family-rules_v1.md`

**Propuesta de reciclaje:** El VA-6 de Genteca define el patrón morfológico CamelCase + reglas de sufijos + longitud fonética que caracterizan la familia de nombres del dominio. Para cualquier nuevo dominio, Vael produce un VA-6 equivalente. El VA-6 de Genteca es el referente estético de partida.

**Elementos directamente transferibles (con adaptaciones por dominio):**

| Elemento | Transferibilidad | Adaptación requerida |
|----------|-----------------|----------------------|
| Patrón morfológico CamelCase (raíz evocadora + modificador funcional) | Alta | Verificar que el patrón CamelCase aplica para el idioma y mercado del nuevo dominio |
| Categorías de sufijos (defensiva / operacional / registro) | Alta | Nuevo dominio puede ampliar las categorías según el tipo de tecnologías |
| Reglas de longitud (2-3 sílabas por parte, máx 5-6 sílabas total) | Alta | Parámetro fonético probado — conservar salvo excepción justificada |
| Pronunciabilidad en español como criterio base | Alta para dominios LatAm | Ajustar para dominios con audiencia primaria anglófona |
| Sufijos prohibidos (-Pro, -Plus, -Max, -Smart, -Tech) | Alta | Lista universal de sufijos genéricos sin valor diferenciador |
| Prohibición de protocolos estándar como raíces | Alta | El principio es universal; las marcas específicas a prohibir (MODBUS, etc.) dependen del dominio técnico |
| Regla de no repetir raíces entre nodos distintos | Alta | Universal — cada nodo tiene raíz exclusiva en la familia |

**Condición de uso:** El VA-6 de Genteca es input de referencia, no plantilla de copy-paste. El Aesthetic anchor (los 6 nombres confirmados de Genteca) es específico de ese dominio y no debe transplantarse.

---

## 3. Pattern de gates Bruna para naming IP

**Artefacto fuente:** `C:\Raul\03-projects\genteca\portfolio-naming-ip-2026\04-bruna\Bruna_BR-2_approval-set_v1.md`

**Propuesta de reciclaje:** Los 8 gates de Bruna en este proyecto mapean los riesgos recurrentes en naming IP clase 9 para mercados VE/MX. El patrón es reutilizable como checklist de arranque para cualquier gate Bruna de naming en cualquier dominio.

**Gates como checklist universal (orden de análisis):**

| Gate # | Tipo de riesgo | Aplica a cualquier dominio |
|--------|---------------|---------------------------|
| 1 | Override de cobertura universal sin auditoría | Sí — siempre que el Owner asuma presencia universal de una función |
| 2 | Descriptividad del nombre (mecanismo IEC/estándar nombrado directamente) | Sí — el riesgo más frecuente en naming de tecnología industrial |
| 3 | Caso A/B de empaque (el empaque actual menciona la función que el nombre nombra) | Sí para productos físicos con empaque visible |
| 4 | RTB calibration (el RTB que sostiene el nombre aplica a un producto específico, no a toda la línea) | Sí — siempre que el RTB cuantitativo sea exclusivo de un modelo |
| 5 | Colisión OMPI con productos de otros sectores en la misma clase Niza | Sí — clase 9 Niza es amplia; siempre verificar sectores no obvios |
| 6 | Colisión sectorial (raíz con saturación en sub-categoría distinta de la propia) | Sí — específicamente raíces como "Lock", "Guard", "Safe" tienen presencia en seguridad física |
| 7 | Colisión diferenciada por jurisdicción (SAPI VE vs IMPI MX tienen perfiles de riesgo distintos) | Sí — especialmente para nombres con vocabulario de software en clase 9 |
| 8 | Denominación propietaria vs protocolo estándar de tercero | Sí — aplica a cualquier dominio con tecnología de conectividad o comunicación |

**Decisión de precedente nuevo (Gate 7):** La decisión diferenciada por jurisdicción del Gate 7 es candidata a ser formalizada como BR-5 Precedente #8 si el Owner lo ratifica. Sira debe notar esta condición pendiente para que el Owner decida en la próxima revisión de gobernanza.

---

## 4. Estructura del three-pack como pattern reutilizable

**Artefacto fuente:** `C:\Raul\03-projects\genteca\portfolio-naming-ip-2026\06-three-pack\`

**Propuesta de reciclaje:** La estructura Anexo Técnico + Naming Bible + Deck (MD + PPTX) es el entregable canónico para presentar a un abogado marcario cualquier portafolio de naming IP. Los tres documentos tienen roles diferenciados y complementarios.

| Pieza | Rol | Qué lleva siempre |
|-------|-----|-------------------|
| Anexo Técnico | Base técnica verificable: mecanismo, RTBs con referencia documental, diferenciación competitiva, caveats Bruna, lista docs I+D | Tabla maestra de nodos; detalle por nodo con RTBs; sección de docs internos para I+D |
| Naming Bible | Racional completo por candidato | Tabla maestra con columnas: candidato / status / audiencia / beneficio L1 / L2 / factibilidad SAPI / factibilidad IMPI / racional anglicismo / riesgo identificado |
| Deck (MD SSOT + PPTX derivado) | Documento de trabajo para la reunión | Cover slide; objetivo de la reunión; metodología con caveat de override; slide estructural única de arquitectura internacional; bloque por nodo (4 candidatos + perfil); proceso de registro por jurisdicción; lista docs internos I+D; próximos pasos |

**Guía de escala para dominios futuros:**
- 6-9 nodos registrables → ≈20-25 slides de deck (Genteca: 8 nodos, 22 slides — dentro del rango)
- 4 candidatos por nodo → Naming Bible ≈ 32-36 entradas base + contingencias
- Contingencias: siempre generar para gates de colisión tipo OMPI y sectorial — evita reabrir Phase 4

---

## 5. Estado de publicación en catálogo Sira

| Artefacto | Propuesta de tag en catálogo | Dominio fuente | Dominios destino potenciales |
|-----------|------------------------------|----------------|------------------------------|
| 8 decisiones estructurales charter | `naming-ip-framework/charter-template` | genteca | plenus, panama (si aplica) |
| VA-6 Naming Family Rules | `naming-ip-framework/family-rules-pattern` | genteca | plenus |
| Gates Bruna naming IP (checklist 8 gates) | `naming-ip-framework/bruna-gate-checklist` | genteca | plenus, cualquier dominio |
| Three-pack structure | `naming-ip-framework/three-pack-pattern` | genteca | plenus, cualquier dominio |
| Doctrina equivalencia perceptual SAPI aplicada | `legal-ip/sapi-ve-doctrine-cases` | genteca | cualquier dominio con VE |
| Patrón RTB calibration (Escenario A vs B) | `naming-ip-framework/rtb-calibration-pattern` | genteca | cualquier dominio |

---

*Ivo — IV-3 Phase 8. Feed entregado a Sira. Fecha: 2026-05-13.*
*Sira indexa y decide estructura del catálogo. Ivo no indexa.*
