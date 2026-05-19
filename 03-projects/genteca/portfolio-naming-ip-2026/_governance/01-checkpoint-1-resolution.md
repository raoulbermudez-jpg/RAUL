---
doc_type: checkpoint-resolution
project_id: portfolio-naming-ip-2026
checkpoint: 1
fecha: 2026-05-13
decisor: Owner (Raul)
inputs_revisados:
  - 02-vera-orlan/Vera_VR-1_tech-inventory-hybrid_v1.md
  - 02-vera-orlan/Orlan_OL-1_differentiation-matrix_v1.md
---

# Checkpoint 1 — Resolución Owner

## Contexto

Vera entregó inventario híbrido de 8 nodos. Orlan entregó differentiation matrix recomendando 7 nodos (sin H). Owner revisó ambos en Checkpoint 1.

## Decisiones Owner

### Decisión 1 — Cantidad final de nodos: **8 nodos (A-H)**

**NODO-H reformulado:** No es "Conectividad MODBUS/GIO ecosystem" (lectura inicial Vera). Es **"Ecosystem GIO" como denominación propietaria Genteca** — nombres de fantasía GIO-Tool / GIO-Port / GIO-Link son los que se registran, NO el protocolo MODBUS (industria estándar, no registrable).

**Implicación para Solenne (Phase 4):** los 4 candidatos del NODO-H no deben contener "MODBUS" ni términos descriptivos de protocolo estándar. Deben anclarse en la familia GIO-* o crear nombres alternativos para el ecosystem propietario.

### Decisión 2 — NODO-D ThermalCurve: **Mantener y diferir a Phase 3 Bruna**

Orlan flagea ThermalCurve como rojo (riesgo descriptividad alto vs IEC 60947-4-1). Owner acepta el flag y mantiene el nodo en cartera. **Bruna en Phase 3 decide:**

- Si Vera puede documentar diferenciador algorítmico propietario en Phase 3 — sobrevive ThermalCurve
- Si no — Bruna rechaza el nombre y Solenne genera 4 candidatos alternativos para el nodo (que sigue siendo nodo registrable, solo cambia el nombre anchor)

### Decisión 3 — ForensLog RTB: **Solenne decide según mejor encaje del nombre**

Orlan identificó que "100 fallas" aplica solo a GIII+MV (GIII+ estándar = 20, GSPT-MV = 80). Owner deja la decisión a Solenne en Phase 4:

- Solenne evalúa si el nombre ForensLog se sostiene mejor acotando a GIII+MV (con RTB claro 100 fallas)
- O si se sostiene mejor con un nuevo nombre que abarque toda la gama Genius con RTB "20-100 fallas según producto"
- O si genera candidatos diferentes que encajen mejor con uno u otro perfil de RTB

Vael en Phase 2 considera ambos escenarios al armar el messaging del nodo.

## Carry-forward a las fases siguientes

Para Vael (Phase 2):
- 8 nodos con A-G del Top 7 anchor + H reformulado a "Ecosystem GIO"
- ThermalCurve sigue siendo anchor de NODO-D hasta Phase 3
- ForensLog RTB queda abierto a decisión Solenne — Vael arma messaging para ambos perfiles

Para Bruna (Phase 3):
- **Gate crítico ThermalCurve:** diferenciador algorítmico propietario o reemplazo
- Gate estándar sobre claims de los otros 7 nodos
- Override curva inversa universal de facto — defendibilidad
- NODO-H: confirmar que candidatos no usan términos de protocolo estándar

Para Solenne (Phase 4):
- 4 candidatos por nodo (8 × 4 = 32 candidatos totales)
- ThermalCurve sobrevive como anchor o se reemplaza según Bruna
- ForensLog: decidir entre acotar a GIII+MV vs ampliar a gama Genius
- NODO-H: candidatos anclados en familia GIO-* o nombres alternativos del ecosystem propietario, NO MODBUS

Para Vivienne (Phase 5):
- Deck refleja 8 nodos en bloque principal
- Si ThermalCurve cae en Phase 3, ese slot se llena con candidatos alternativos del mismo nodo (no cambia el conteo)

## Gaps de documentación interna que I&D debe cerrar (carry a lista final)

Vera flagea 4 gaps. Owner los confirma para incluir en sección final del deck "Documentos internos que I&D debe ubicar o elaborar":

1. **NODO-C Thermo-Safe** — parámetros NTC numéricos en HDE actual
2. **Curva inversa V-t algorítmica** — denominación formal en docs Genteca; especificación interna
3. **NODO-G TaskMemory** — 10 s de confirmación pendiente HDE
4. **NODO-H Ecosystem GIO** — documentación formal del ecosystem propietario (qué incluye, cómo se diferencia técnicamente de MODBUS puro)

Estos NO frenan el deck (asunción Owner: docs internas listas). Aparecen como lista al final del deck para que I&D los tenga ubicados o elaborados antes de la reunión con abogado.

## Estado del proyecto post-Checkpoint 1

- Phase 0 ✅ Completa (Aurelio)
- Phase 1 ✅ Completa (Vera + Orlan)
- Checkpoint 1 ✅ Resuelto (este documento)
- Phase 2 ⏳ Pendiente arrancar (Vael)
