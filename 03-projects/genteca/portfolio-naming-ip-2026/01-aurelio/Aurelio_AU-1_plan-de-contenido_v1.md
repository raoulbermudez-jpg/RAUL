---
doc_type: AU-1
project_id: portfolio-naming-ip-2026
domain: genteca
version: v1.0
fecha: 2026-05-13
author: Aurelio
predecessor_project: 2026-05-07_marcas-anglicismos-junta
charter_version: v1.0 (2026-05-13)
---

# AU-1 — Plan de Contenido
## Proyecto: Portfolio Naming IP 2026 (Genteca)

---

## 1. Objetivo medible

Entregar a Raul (Owner) un **three-pack** listo para presentar a abogado marcario externo, que le permita ejecutar el paso siguiente (búsqueda fonética SAPI VE + equivalente IMPI MX) sin necesidad de pedir clarificaciones adicionales a Genteca.

El three-pack comprende:

| Entregable | Productor | Formato |
|---|---|---|
| Anexo Técnico | Vera + Orlan | Markdown integrado |
| Naming Bible | Solenne | Markdown (fila por candidato) |
| Deck Vivienne | Vivienne | Markdown SSOT + PPTX derivado (≈25-30 slides) |

**Criterio de "listo":** el abogado tiene todo lo que necesita para iniciar sin requerir aclaraciones — incluyendo inventario de tecnologías, 24-36 candidatos evaluados, factibilidad VE+MX por candidato, arquitectura internacional en slide única, proceso de registro paso a paso y lista de documentos internos que Genteca deberá proveer.

---

## 2. Audiencias

### 2.1 Audiencia primaria del three-pack
**Abogado marcario externo (TBD — asignación legal Owner).**

Perfil: profesional en propiedad intelectual, conoce el proceso SAPI Venezuela y el equivalente mexicano (IMPI / LFPPI 2020), no necesita que le expliquemos el valor de las marcas en términos de negocio Genteca. Necesita: precisión técnica, candidatos limpios con perfil registral claro, y una lista de lo que podría pedirle a I&D si el proceso avanza.

### 2.2 Audiencias del proceso (consumidores del AU-1 y outputs intermedios)

| Rol | Qué consume | En qué fase |
|---|---|---|
| Owner (Raul) | AU-1 (este doc) + Checkpoint 1 + Checkpoint 2 + three-pack final | Fases 0, 1, 5 |
| Junta Genteca (eventual) | Three-pack en modo sumario o deck Vivienne solo | Post-entrega, decisión Owner |
| Especificadores técnicos / I&D interno | Lista de documentos internos (embebida en deck) | Phase 6-7 |

---

## 3. Mensajes centrales

Ancla del proyecto: **potencia comercial primero, factibilidad después.** Un candidato que no sostiene el valor de la tecnología no entra al filtro de factibilidad — no importa si registra fácil.

Cadena de 3 niveles por tecnología (ver charter §6):

1. **L0 — Tecnología:** qué hace el algoritmo / función.
2. **L1 — Beneficio técnico:** qué protege o resuelve para el equipo.
3. **L2 — Beneficio del beneficio:** consecuencia palpable para el comprador.

Cuando L2 existe y es claro, se incluye en la línea de beneficio comercial del slide del deck. No es relleno — es la razón por la que el nombre importa al comprador, no al instalador.

El segundo mensaje central es **stand-alone marks**: cada nombre es una marca independiente clase 9 Niza. No es un sub-feature de Exceline ni de Genius. El nombre carga por sí mismo.

Estos dos mensajes son los filtros de curación para Vael (Phase 2) y Solenne (Phase 4). Un candidato débil en cualquiera de los dos se descarta — no se llena la tabla con nombres mediocres.

---

## 4. Mix de formatos y ruta de producción declarada

### 4.1 Tabla de formatos por pieza

| Pieza | Formato | Audiencia | Productor inicial | Productor final | Notas |
|---|---|---|---|---|---|
| Inventario de tecnologías | Markdown estructurado | Owner (Checkpoint 1) + Orlan + Vael + Solenne | Vera | Vera | Hybrid granularity; 6-9 nodos registrables. Override curva inversa asumido universal. No auditar producto por producto |
| Differentiation matrix | Markdown tabla (verde/amarillo/rojo) | Owner + Solenne + Vivienne | Orlan | Orlan | Por tecnología, no por producto. Competidores: ABB/Siemens/Schneider/Eaton/Rockwell/Chint/LS/Lovato |
| Messaging architecture + guardrails | VA-2 + VA-5 | Vael, consumido por Bruna + Solenne | Vael | Vael | Audiencia primaria por línea + L2 cuando aplica. Sin multiplicación de caveats |
| Gate Bruna — claims + override | BR-2 entrada portfolio-naming | Bruna | Bruna | Bruna | Foco: defendibilidad override curva inversa universal + claims que sostienen cada candidato. Gate, no detención |
| Naming family rules | Output Vael Phase 4 | Solenne | Vael | Vael | Reglas de construcción para los 4 candidatos por tech |
| Naming Bible (24-36 candidatos) | Markdown (fila por candidato) | Abogado + Owner | Solenne | Solenne | Top 7 mapeados primero; completa hasta 4/tech. Filtro: impacto > SAPI VE > IMPI MX |
| Anexo Técnico | Markdown integrado | Abogado + Owner | Vera + Orlan | Vera + Orlan | Descripción mecanismo + algoritmo + diferenciación + RTBs verificables |
| Deck Vivienne (SSOT) | Markdown + PPTX derivado | Abogado marcario (primario) | Vivienne | Vivienne | ≈25-30 slides. Una sola slide estructural US+Madrid. Sin caveats por candidato. Audiencia: abogado, no Junta |

### 4.2 Lo que Aurelio NO produce

Aurelio orquesta. Cero copy editorial, cero redacción de candidatos, cero slides. Si la línea entre "asignación de pieza" y "wording de candidato" se difumina durante la coordinación: Solenne decide el wording; Vael decide los guardrails.

---

## 5. Cadencia y fases

El cronograma es secuencial con dos ventanas paralelas. Las fases no arrancan sin el output de la fase anterior, salvo las paralelas explícitas indicadas abajo.

```
PHASE 0 — Aurelio
  Output: AU-1 (este doc) + AU-1 mapping top 7 (archivo 2)
  Duración: sesión única (2026-05-13)
  Dependencia saliente: Phase 1 necesita AU-1 cerrado

PHASE 1 — Vera (inventario hybrid) // Orlan (differentiation matrix)
  [PARALELO: Vera y Orlan trabajan con el mismo charter + AU-1 como base]
  Output: Inventario 6-9 nodos + Differentiation matrix
  CHECKPOINT 1 — Owner revisa y aprueba inventario antes de continuar
  Dependencia: override curva inversa universal (charter §3 decisión 4)
  Dependencia: docs HDE/specs Genteca accesibles a Vera

PHASE 2 — Vael
  Input: Inventario Vera + Differentiation matrix Orlan + AU-1 mapping Top 7
  Output: VA-2 (messaging arch por audiencia / línea) + VA-5 (guardrails)
  Dependencia: Checkpoint 1 Owner cerrado

PHASE 3 — Bruna  [GATE OBLIGATORIO]
  Input: VA-5 (guardrails) + Inventario Vera + override curva inversa
  Output: BR-2 entrada portfolio-naming-ip-2026
  Foco: claims que sostienen cada candidato + defendibilidad override universal
  Nota: Gate no bloquea, pero cualquier caveat ⚠ o ❌ de Bruna reserva ventana
        de ajuste ANTES de que Solenne produzca candidatos en Phase 4

PHASE 4 — Vael (naming family rules) // Solenne (4 candidatos/tech)
  [PARALELO: Vael cierra reglas; Solenne trabaja con Top 7 mapeados + reglas]
  Input: VA-2/VA-5 + BR-2 + AU-1 mapping Top 7
  Output: Naming family rules + Naming Bible (24-36 candidatos)
  Filtro operativo Solenne: impacto → SAPI VE → IMPI MX

PHASE 5 — Vera+Orlan (Anexo Técnico) // Solenne (Naming Bible final) // Vivienne (Deck)
  [PARALELO: los tres trabajan sobre el mismo inventario validado]
  Output: three-pack completo (Anexo Técnico + Naming Bible + Deck SSOT+PPTX)
  CHECKPOINT 2 — Owner revisa three-pack completo antes de entregar al abogado

PHASE 6/7 — Embebido en deck (no fase separada de producción):
  Proceso paso a paso con abogado (LPI VE 1955 + LFPPI MX 2020)
  Lista documentos internos para I&D
  [Estos outputs los genera Vivienne durante Phase 5, no requieren fase propia]

PHASE 8 — Ivo
  Cierre estándar IV-1 / IV-2 / IV-3 / IV-4 / IV-5
```

### 5.1 Gates críticos en cronograma

| Gate | Responsable | Posición en cadena | Qué bloquea si falla |
|---|---|---|---|
| Checkpoint 1 Owner | Owner (Raul) | Tras Phase 1 | Phase 2 no arranca sin inventario aprobado |
| Gate Bruna Phase 3 | Bruna | Tras Phase 2 | Cualquier candidato con claim ⚠/❌ no entra a Phase 4 sin ajuste |
| Checkpoint 2 Owner | Owner (Raul) | Tras Phase 5 (three-pack) | Three-pack no sale al abogado sin aprobación Owner |

---

## 6. Métricas de éxito

| Métrica | Valor objetivo | Quién la verifica |
|---|---|---|
| Nodos registrables identificados | 6-9 | Vera + Owner en Checkpoint 1 |
| Candidatos generados | 24-36 (4 por nodo) | Solenne + Owner en Checkpoint 2 |
| Candidatos aprobados gate Bruna | 100% de los candidatos en Naming Bible tienen BR-2 status (✅ / ⚠ con condición documentada) | Bruna |
| Calidad de deck | Abogado puede ejecutar paso siguiente (búsqueda fonética + solicitud FM-02) sin pedir aclaraciones | Owner (juicio tras Checkpoint 2) |
| Top 7 preservados en portafolio | Los 7 anchor del proyecto previo aparecen en Naming Bible (posiblemente en distintas techs del nuevo inventario) | Solenne |
| Slide US+Madrid | Una sola slide estructural; cero análisis individual por candidato en esa sección | Vivienne |

---

## 7. Capacidad estimada por agente productor

Esta estimación es orientativa. Los agentes producen en sesiones convocadas por Owner; no hay carga semanal acumulativa en este proyecto (es producción por evento, no editorial periódica).

| Agente | Fases donde produce | Carga estimada por convocatoria |
|---|---|---|
| Vera | 1 + 5 | Phase 1: 1 sesión (inventario). Phase 5: 1 sesión (Anexo Técnico, parte Vera) |
| Orlan | 1 + 5 | Phase 1: 1 sesión (matrix). Phase 5: 1 sesión (Anexo Técnico, parte Orlan) |
| Vael | 2 + 4 | Phase 2: 1 sesión (messaging + guardrails). Phase 4: 1 sesión (naming family rules) |
| Bruna | 3 | 1 sesión (gate claims + override) |
| Solenne | 4 + 5 | Phase 4: 1 sesión (mapping Top 7 + candidatos nuevos). Phase 5: 1 sesión (Naming Bible final) |
| Vivienne | 5 | 1 sesión (deck SSOT + PPTX) |
| Ivo | 8 | 1 sesión (cierre) |

Total sesiones: 9-11 (algunas paralelas). Bottleneck más probable: Checkpoint 1 Owner (si demora, bloquea Phase 2 en adelante).

---

## 8. Reutilización (AU-5 check)

Consultado catálogo antes de producción. Piezas reciclables del proyecto predecesor `2026-05-07_marcas-anglicismos-junta`:

| Pieza preexistente | Estatus en este proyecto |
|---|---|
| Top 7 candidatos (Vael + Bruna BR-2) | Preservados como anchor. Solenne re-mapea y completa en Phase 4 |
| VA-2 + VA-5 previos (messaging deck Junta) | NO reutilizables directamente — ese messaging era para Junta; este es para abogado marcario. Vael produce nuevo VA-2/VA-5 |
| BR-2 previos por candidato | Carry-over como input informativo. Bruna en Phase 3 produce BR-2 formal para este proyecto con scope extendido |
| Research SAPI/IMPI (Paxs) | Reutilizable como referencia. Bruna y Solenne consumen `reference_sapi_venezuela_quick.md` y `DEC-2026-05-08-001/context.md` |
| Análisis de diferenciación Orlan previo | Referencia, no reutilización directa — scope era "deck Junta estrategia IP"; ahora es "inventario para abogado" |

---

## 9. Lo que este proyecto NO hace

Referencia directa al charter §7 (anti-ruido):

- No incluye las 3 escalaciones internas Owner previas (verificar SAPI Exceline, addendum HDE Vera, presupuesto IP) — son tema interno Genteca, no para el abogado.
- No cubre patentes de invención.
- No produce análisis individual por candidato para US/Madrid — una sola slide estructural.
- No audita producto por producto el override curva inversa — es universal de facto.
- No incluye desglose de audiencias por slide del deck — solo nota corta + audiencia primaria en cada slide de tecnología; desglose completo vive en Anexo Técnico.

---

## 10. Supuestos y limites

### Insumos aguas arriba con version

| Insumo | Version / fecha | Usado en |
|---|---|---|
| Charter portfolio-naming-ip-2026 | v1.0 (2026-05-13) | Todo el plan |
| Memoria project_marcas_anglicismos_junta.md | 2026-05-07, marcada 4 days old | Top 7 mapping + BR-2 status previos |
| reference_sapi_venezuela_quick.md | 2026-05-07 | Marco legal VE + costos |
| DEC-2026-05-08-001 context.md | Migrado 2026-05-09 | Estado actual decision madre |
| KB Genteca | 2,237 specs (referencia general) | Vera y Orlan la navegan en Phase 1 |

### Overrides Owner (charter §3)

- **Override curva inversa V-t algorítmica + I-t cold/hot:** asumida universal de facto en gama Exceline / Exceline Profesional / Genius. Ningún agente audita producto por producto. Si Vera encuentra en KB alguna excepción documentada, la reporta al Owner en Checkpoint 1, no la propaga como caveat al deck.
- **Docs internas Genteca (HDE, especificaciones):** asumidas disponibles para Vera en Phase 1. Si hay brecha documental específica (una tecnología sin HDE), Vera la lista como item en la "lista de documentos internos" del deck (Phase 6/7), no como bloqueante de Phase 1.

### Validez temporal

- Reference SAPI: costos en tabla son 2024-2025, fluctúan con BCV. El abogado marcario deberá confirmar tasas vigentes al momento de la solicitud FM-02.
- Estado de "Exceline" en SAPI no verificado — escalación pendiente (Owner). No bloquea producción del three-pack, pero el deck no usa ® para Exceline hasta que Owner confirme certificado.

### Gates Vael / Bruna pendientes

- VA-2 / VA-5 de este proyecto: no existen aún. Phase 2 los produce.
- BR-2 formal de este proyecto: no existe aún. Phase 3 lo produce. Los BR-2 previos del proyecto marcas-anglicismos son carry-over informativo, no sello formal para este three-pack.

### Decisiones Owner pendientes

- Asignacion del abogado marcario externo (charter: stakeholder_primario TBD). No bloquea fases 1-5; necesario para entrega final.
- Timing de Checkpoint 1: Owner define cuándo está disponible para revisar el inventario Vera/Orlan. Es el único cuello de botella con fecha abierta.

### Riesgos de capacidad

- Las fases 1, 4 y 5 tienen paralelismo. Si Owner convoca los agentes en lotes separados el cronograma se extiende; si los convoca en paralelo el bottleneck real es el Checkpoint 1 Owner (no la producción).
- Bruna Phase 3: si el override curva inversa requiere más que un ajuste simple (Bruna detecta que hay claim estructural indefendible), reservar ventana de re-trabajo Vera antes de Phase 4. Improbable dado el override explícito del Owner, pero nombrado.

### Claims sin sello formal en este AU-1

- Los 7 candidatos anchor tienen BR-2 status carry-over (ver archivo 2, columna Bruna BR-2 previo). Ninguno tiene sello formal para este proyecto hasta que Bruna cierre Phase 3.
- Candidatos en ⚠ (FlickerGuard, TripleLock, TaskMemory, ThermalCurve) requieren atención especial en Phase 3. ThermalCurve (⚠⚠ riesgo descriptividad alto) es el candidato de mayor riesgo; si Bruna lo degrada a ❌ en este proyecto, Solenne genera un candidato de reemplazo en Phase 4.
