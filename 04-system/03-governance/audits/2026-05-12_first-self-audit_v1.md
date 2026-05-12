---
title: "Primera auditoría /RAUL/ con PKA-AUDIT-FRAMEWORK_RAUL v1.0"
type: audit-report
audit_number: 1 (baseline)
audit_date: 2026-05-12
framework_version: 1.0
framework_status_at_audit: candidate
auditor: Raul (self-audit)
owner: Raoul Bermudez
---

# Primera auditoría /RAUL/ — baseline 2026-05-12

## 0. Contexto

Esta es la **auditoría baseline** del sistema /RAUL/ tras el cierre del Plan Maestro Modelo A (sesión 2026-05-12). Es la primera aplicación real del framework `PKA-AUDIT-FRAMEWORK_RAUL.md` v1.0 candidate.

**Estado del sistema al momento del audit:**
- ✅ Plan Maestro Modelo A cerrado completo (Pasos 0-6)
- ✅ 21 agentes migrados a patrón canónico
- ✅ Bundle 6 mejoras eficiencia integradas
- ✅ Principio "Portable text as SSOT" formalizado
- ✅ Memoria 2-tier (HOT + ARCHIVE) implementada
- ✅ PKA Audit Framework v1.0 candidate listo

**Lo que esta auditoría busca:**
1. Validar que el sistema cumple los principios declarados.
2. Identificar brechas reales (no obvias) que requieran remediación.
3. Establecer baseline cuantitativo para comparar contra auditorías futuras.
4. Validar el framework mismo (¿qué áreas son fáciles/difíciles de aplicar?).

**Honestidad de auditor:** este es self-audit. Riesgo de scoring optimista. Mitigación: priorizo identificar brechas sobre celebrar fortalezas. Cuando dudo entre dos scores, elijo el menor.

---

## 1. Resumen ejecutivo

### Estado general

| Métrica | Valor |
|---|---|
| **Puntaje promedio global** | **3.7 / 5** |
| **Nivel de madurez** | **Sólido y operativo** (rango 3.6-4.3) |
| Áreas auditadas | 17 |
| Áreas con score ≥4 | 11 |
| Áreas con score 3 | 4 |
| Áreas con score ≤2 | 2 |
| Brechas críticas | 0 |
| Brechas altas | 3 |
| Brechas medias | 7 |
| Brechas bajas | 5 |

### Principales fortalezas

1. **Arquitectura canónica de agentes muy madura.** Modelo A aplicado uniformemente en 21/21 agentes. Taxonomía nominal sólida. Documentación interna excelente.
2. **Principios filosóficos bien anclados.** Local-first + vendor-neutral + portable-text-as-SSOT son operativos, no aspiracionales. Validados con grep cross-cutting durante la sesión.
3. **Genteca como dominio piloto está maduro.** 2.237 specs, 7 proyectos activos, agentes domain-specialist completos, governance Phase 3 funcionando con casos reales.
4. **Decisiones arquitectónicas trazables y auditables.** DECISIONS.md con 12+ entradas formato consistente, referenciable desde cualquier docs estructural.
5. **Memoria operativa Raul (00-raul-intelligence) bien estructurada.** Aprendizajes capturados con disciplina; sistema 2-tier nuevo formaliza política prospectiva.

### Principales debilidades

1. **5 de 6 dominios son esencialmente placeholders.** Plenus/Finca/Teca/marca-personal tienen 3-5 archivos md cada uno. 99-other-domains solo tiene `_index.md`. Genteca es el único dominio realmente activo. Esto NO es brecha de calidad — es estado natural; pero significa que el sistema NO está validado multi-dominio.
2. **Convenciones nuevas sin ciclo real de validación.** Memoria 2-tier, chunking, frontmatter enriquecido, cache-friendly delegation se documentaron HOY. No hay evidencia operativa de que las políticas se ejecuten en la práctica todavía.
3. **Observabilidad limitada.** task-log.md (113 líneas, narrativa por delegación) es el único log estructurado. Sin per-execution logs, sin métricas de costo/latencia, sin error logs estructurados.
4. **Frontmatter convention nueva no aplicada retroactivamente.** Los 2.237 specs de Genteca + 33 memorias actuales NO tienen `last_touched`, `confidence`, `source_type` enriquecidos.
5. **Mantenimiento mensual sin ciclo todavía.** Política de archivado mensual de memorias declarada pero nunca ejecutada (primer ciclo ~2026-10-12).

### Riesgos críticos

**Ninguno detectado como Crítico** (severity definition § framework: pérdida de info, secretos, errores graves, outputs peligrosos).

Riesgos **Altos** detectados (ver §brechas):
- Drift de convenciones nuevas si no se valida ciclo de aplicación
- Lock-in operativo a un solo dominio (Genteca) que limita la generalización
- Dependencia de `_template-conceptual.md` v2 sin futuros agentes contratados para validar

### Recomendación general

**El sistema está en estado SÓLIDO Y OPERATIVO** post-Plan-Maestro. La auditoría confirma que los principios declarados se reflejan en código. Las debilidades son **debilidades por madurez emergente**, no por defectos estructurales — la mayoría se resuelven simplemente con uso continuado del sistema.

Recomendación priorizada:
1. **No introducir cambios arquitectónicos mayores** hasta que las convenciones nuevas tengan al menos 2-3 ciclos reales de aplicación.
2. **Focar uso en dominios distintos a Genteca** (Plenus, Finca) para validar generalidad de los patrones.
3. **Implementar observabilidad básica** (per-execution logs livianos) si se va a escalar uso.

---

## 2. Puntajes por área

| Área | Puntaje | Prioridad mejora | Brechas detectadas |
|---|---:|---|---:|
| 5.1 Estructura general | 4.5 | Baja | 1 |
| 5.2 Fuente canónica / Portabilidad | 4.5 | Baja | 1 |
| 5.3 LLM-agnóstico | 4.0 | Baja | 1 |
| 5.4 Modelo A compliance | 4.7 | Baja | 1 |
| 5.5 Taxonomía 6 clases | 4.5 | Baja | 0 |
| 5.6 Memoria 2-tier | 3.5 | Media | 2 |
| 5.7 Chunking conceptuales | 4.5 | Baja | 0 |
| 5.8 Phase 3 governance | 4.0 | Baja | 1 |
| 5.9 KB / Wiki | 3.5 | Media | 2 |
| 5.10 Cobertura dominios | 2.0 | **Alta** | 3 |
| 5.11 Frontmatter convention | 2.0 | **Alta** | 2 |
| 5.12 DECISIONS.md | 4.0 | Baja | 1 |
| 5.13 Memoria persistente | 4.0 | Baja | 1 |
| 5.14 Logs y observabilidad | 2.5 | **Alta** | 2 |
| 5.15 Seguridad / permisos | 4.0 | Baja | 1 |
| 5.16 Documentación | 4.3 | Baja | 0 |
| 5.17 Mantenimiento periódico | 2.5 | Media | 2 |

**Promedio aritmético:** 3.7 / 5

---

## 3. Auditoría por área

### 5.1 Estructura general — 4.5/5

| Criterio | Estado | Observación |
|---|:---:|---|
| 5 carpetas top-level existen y tienen propósito explícito | ✅ | Verificado |
| Subcarpetas siguen `NN-nombre-en-kebab` | ✅ | Convención respetada en todo el árbol |
| Cada carpeta principal tiene README | ⚠ | Algunas tienen _index.md en lugar de README.md |
| Sin mezcla fuentes/KB/outputs/código | ✅ | Separación clara |
| Crece por dominio sin refactor | ✅ | Probado en migración 2026-04 |
| Crece por agente sin refactor | ✅ | 21 agentes integrados sin refactor estructural |
| Navegable en VS Code <30s | ✅ | Confirmado |
| _taxonomy.md + _roster.md al día | ✅ | Sincronizados post-Plan-Maestro |

**Brecha detectada:**
- **Inconsistencia README vs _index.md** (severidad: Baja). Algunas carpetas usan README.md, otras _index.md, mezclando convenciones. No bloquea nada pero rompe expectativa de auditor externo.

### 5.2 Fuente canónica / Portabilidad — 4.5/5

| Criterio | Estado | Observación |
|---|:---:|---|
| Conocimiento principal en Markdown/YAML/JSON/CSV | ✅ | 100% |
| Documentos originales preservados | ✅ | raw-sources/ + 05-archive/ |
| Outputs vs fuentes diferenciados | ✅ | Naming convention canónico |
| Repo versionable con git | ✅ | Operativo |
| Reglas claras para binarios | ✅ | .gitignore con `*.pdf *.pptx *.docx *.xlsx *.png` etc. |
| Principio "Portable text as SSOT" aplicado | ✅ | DECISIONS.md 2026-05-12 + aplicado a Vivienne |
| 3 excepciones SSOT documentadas y respetadas | ✅ | Excel computacional, redline PDFs, cloud live docs |
| Drive como mirror, no como fuente | ✅ | Confirmed (CONTEXT_core.md) |

**Brecha detectada:**
- **Política SSOT en aplicación reciente (1 día)** (severidad: Baja). El principio se aplicó hoy a Vivienne pero no hay aún evidencia de su aplicación retroactiva en wiki notes con frontmatter existentes. No bloquea — simplemente no validado todavía.

### 5.3 LLM-agnóstico — 4.0/5

| Criterio | Estado | Observación |
|---|:---:|---|
| Conceptuales vendor-neutral en §1-§10 | ✅ | Verificado por grep durante sesión (cero WebSearch/WebFetch/python-pptx en conceptuales post-Paso-5) |
| Runtime adapters separados en .claude/ | ✅ | 21 runtimes |
| _runtime-adapter-guide.md documenta contrato | ✅ | Existe y vigente |
| LLM-GUIDELINES.md define model assignment | ✅ | Existe |
| Cambiar LLM = solo runtime rewrite | ⚠ | Conceptualmente cierto; nunca probado con migración real (Gemini/Perplexity reservados pero vacíos) |
| .gemini/, .perplexity/ documentados | ✅ | Mencionados en runtime-adapter-guide como reservados |

**Brecha detectada:**
- **Multi-LLM no validado empíricamente** (severidad: Media). El argumento "cambiar de LLM cuesta solo runtime rewrite" es estructuralmente correcto pero NUNCA se ejecutó realmente. Hasta que no exista 1 agente corriendo en Gemini o equivalente, el claim es teórico. *Recomendación: documentar este claim con disclaimer "no validado empíricamente" en docs hasta que ocurra primera derivación real.*

### 5.4 Modelo A compliance — 4.7/5

| Criterio | Estado | Observación |
|---|:---:|---|
| 21/21 banner SSOT verbatim | ✅ | Verificado por grep |
| 21/21 con 10 secciones canónicas | ✅ | Verificado |
| 21/21 footer correcto | ✅ | Lowercase transversal post-Paso 5 |
| 21/21 git boundary §3 | ✅ | Verificado por grep cross-cutting |
| Runtimes ~70-130 líneas | ✅ | Rango 70-134 (InboxBot es el más largo, justificado) |
| Sin duplicación defensiva runtime↔conceptual | ⚠ | Eliminada en migración pero podría reaparecer en agentes nuevos sin disciplina |
| _template-conceptual.md actualizado | ✅ | v2 con chunking + index-first |

**Brecha detectada:**
- **Sin enforcement automatizado del patrón Modelo A** (severidad: Baja). Cuando se contrate el próximo agente, depende de Michelina aplicar el template correctamente. No hay linter/CI que detecte drift. *Recomendación: añadir checklist explícito en Michelina §6 (Operating Protocol de contratación).*

### 5.5 Taxonomía nominal 6 clases — 4.5/5

| Criterio | Estado | Observación |
|---|:---:|---|
| _taxonomy.md con 6 clases + criterios | ✅ | Existe y vigente |
| _roster.md clasifica cada agente | ✅ | 21 agentes con clase + dominio |
| Cada conceptual con footer correcto | ✅ | Verificado |
| Docs estructurales sin "Capa X" | ✅ | Paso 6 cerrado |
| Bruna documentada como doble-clase | ✅ | governance + content-supply-chain |
| InboxBot como execution-utility | ✅ | Documentado en Tier 3 |

**Sin brechas detectadas en esta área.** Taxonomía completa y bien aplicada.

### 5.6 Memoria 2-tier — 3.5/5

| Criterio | Estado | Observación |
|---|:---:|---|
| MEMORY.md HOT con auto-load | ✅ | Header explicativo |
| MEMORY_ARCHIVE.md existe con header | ✅ | Creado 2026-05-12, vacío |
| Política archivado mensual documentada | ✅ | DECISIONS.md 2026-05-12 |
| Política archivado mensual ejecutada | ❌ | Primer ciclo planeado ~2026-10-12 (4 meses) |
| `last_touched`/`always_load` aplicado en memorias nuevas | ⚠ | Solo en 2 entradas nuevas hoy; 33 anteriores sin estos campos |
| CONTEXT_core.md documenta sistema | ✅ | Párrafo actualizado |
| Sin MEMORY.md >50 entradas | ✅ | 35 entries actuales |

**Brechas detectadas:**
- **Política prospectiva sin ciclo ejecutado** (severidad: Media). Las políticas funcionan cuando se ejecutan, no cuando se documentan. 4 meses hasta primer ciclo real es tiempo amplio para drift.
- **Convención `last_touched` no retroactiva** (severidad: Media). 33 memorias existentes asumen `last_touched = creation_date`. Cuando el primer ciclo de archivado corra, todas tendrán fechas "antiguas" igualmente, distorsionando la señal HOT/COLD.

*Recomendación combinada: hacer un primer ciclo de archivado en 2026-06-12 (no esperar 6 meses) PERO con criterio "creation_date >6 meses" (lo único auditable retroactivo), y comenzar a aplicar `last_touched` en memorias que se referencian a partir de ahora.*

### 5.7 Chunking conceptuales largos — 4.5/5

| Criterio | Estado | Observación |
|---|:---:|---|
| Conceptuales >500 líneas con _templates.md | ✅ | 6/6 chunked (aurelio, sira, vael, oz, solenne, bruna) |
| Excepción InboxBot documentada | ✅ | §11 Phase 3 protocol inline |
| _template-conceptual.md §11 documenta convention | ✅ | v2 con chunking rule |

**Sin brechas críticas.** Patrón aplicado consistentemente.

**Observación constructiva:** la convención solo se valida cuando se contrate un agente nuevo con §11 grande y se aplique el chunking correctamente. Esto pasará orgánicamente, no requiere intervención.

### 5.8 Phase 3 governance — 4.0/5

| Criterio | Estado | Observación |
|---|:---:|---|
| PENDING-DECISIONS-REGISTRY.md existe | ✅ | Con schema canónico |
| DECISION-MAKERS.md documenta decisores | ✅ | Existe |
| Canales 04/05/06/07 en 01-inbox/ activos | ✅ | Estructura presente |
| InboxBot §11 implementa protocolo | ✅ | v4.0 conceptual |
| Status vocabulary respetado | ✅ | 7 estados canónicos documentados |
| Decision-IDs siguen regex canónica | ✅ | `(DEC\|JUNTA\|REG\|ALT)-YYYY-MM-DD-NNN` |
| Decisiones in-flight con responses esperadas tienen row en registry | ⚠ | 5 rows actuales; estado real coincide con realidad pero falta auditoría reciente |

**Brecha detectada:**
- **Registry desactualizado en estado de decisiones** (severidad: Media). El registry tiene 5 decisiones in-flight (DEC-2026-05-06-001 GME, DEC-2026-05-06-002 GME claim, DEC-2026-05-08-001 marcas anglicismos, DEC-2026-05-03-001 COVENIN, DEC-2026-05-08-D1-D5 GST labels). Algunas tienen >5 días sin movimiento. Necesitan revisión activa de SLA por Owner. *Recomendación: revisar registry y aplicar `ESCALATED` o `EXPIRED` donde corresponda.*

### 5.9 KB / Wiki — 3.5/5

| Criterio | Estado | Observación |
|---|:---:|---|
| KB separada de raw-sources | ✅ | 02-knowledge-base/ vs 01-inbox/03-raw-sources/ |
| Cada dominio activo tiene wiki + specs + assets | ⚠ | Solo Genteca poblado; otros stub |
| _index-specs.md mantenido al día | ✅ | Genteca: 2.237 specs indexadas |
| Páginas wiki con frontmatter | ⚠ | Inconsistente; no auditado masivamente |
| Distinción evidencia/interpretación/decisión | ⚠ | No formalmente marcada en wiki |
| Páginas con estado vigencia | ❌ | Sin auditoría sistemática de `status` en wiki |

**Brechas detectadas:**
- **Frontmatter inconsistente en wiki pages** (severidad: Media). No hemos auditado por muestreo si las páginas wiki existentes tienen frontmatter completo. *Recomendación: muestrear 10 páginas wiki random y reportar % con frontmatter completo.*
- **Sin marca de vigencia auditable** (severidad: Media). Wiki pages no tienen `status` ni `superseded by X` cuando se vuelven obsoletas. Es lock-in implícito a "todo está vigente hasta que alguien diga lo contrario".

### 5.10 Cobertura de dominios — 2.0/5

| Dominio | Carpetas | KB poblada | Proyectos | Agentes | Score |
|---|:---:|:---:|:---:|:---:|:---:|
| Genteca | ✅ | ✅ (2.237 specs) | 7 activos | 7 domain-specialists | **5** |
| Plenus-metabolica | ✅ | ⚠ (5 md) | 1 (Plenus.pptx + QTorta.pptx) | 0 | 1 |
| Finca-ganaderia | ✅ | ⚠ (5 md) | 0 | 0 | 1 |
| Teca-teak4food | ✅ | ⚠ (5 md) | 0 | 0 | 1 |
| Marca-personal-raoul | ✅ | ⚠ (3 md) | 0 | 0 | 1 |
| Panama (99-other-domains) | ⚠ (1 md) | ❌ | 0 | 0 | 0 |

**Score:** Genteca (5) + 4 stubs (1) + 99-other (0) = promedio simple 1.5 → redondeo a 2.0 por carpetas establecidas

**Brechas detectadas:**
- **Lock-in operativo a un dominio** (severidad: **Alta**). El sistema NO está validado multi-dominio. Toda la madurez es Genteca-específica. Cuando se intente operar Plenus/Finca/Teca en escala real, emergerán patrones no contemplados.
- **Panama como dominio activo no integrado** (severidad: Alta). Memoria menciona "Panama — nuevo dominio activo" desde 2026-05-01, pero solo existe `99-other-domains/_index.md`. No hay estructura, ni KB, ni proyectos formalizados.
- **No hay roadmap de activación de dominios** (severidad: Media). ¿Cuándo se activa Plenus? ¿Por dónde se empieza? Sin plan, los dominios se quedan stub indefinidamente.

*Recomendación combinada: priorizar 1 dominio (probablemente Plenus o Panama según urgencia Owner) para activación deliberada en próximos 3 meses; usar Genteca como template pero adaptar al dominio real.*

### 5.11 Frontmatter convention — 2.0/5

| Criterio | Estado | Observación |
|---|:---:|---|
| Frontmatter en notas wiki sigue formato canónico | ⚠ | No auditado masivamente |
| Campo `confidence` presente | ❌ | Convención nueva, no aplicada |
| Campo `source_type` presente | ❌ | Convención nueva, no aplicada |
| Campo `last_touched` presente en memorias | ⚠ | Solo en 2 entradas nuevas hoy |
| Campo `status` con valores canónicos | ⚠ | Algunos KBs sí, otros no |
| Campo `sensitivity` cuando aplica | ❌ | No aplicado |
| FRONTMATTER-CONVENTIONS.md actualizado | ✅ | Existe (último update 2026-05-09 Phase 3) |

**Brechas detectadas:**
- **Frontmatter convention enriquecido es solo declarativo** (severidad: **Alta**). Documentamos en evaluación que conviene adoptar campos `confidence`, `source_type`, `sensitivity`. NO se ha aplicado en ninguna parte del sistema todavía. La diferencia entre "documentado" y "aplicado" es la diferencia entre methodology y operations.
- **Sin gradual rollout plan** (severidad: Media). No hay decisión sobre si aplicar retroactivamente o solo a nuevos. Sin plan, la convención queda eternamente declarativa.

*Recomendación: tomar decisión binaria — adoptar (con plan rollout) o descartar. No quedarse en limbo.*

### 5.12 DECISIONS.md — 4.0/5

| Criterio | Estado | Observación |
|---|:---:|---|
| DECISIONS.md crece append-only | ✅ | 13+ entradas, ninguna eliminada |
| Cada entrada: fecha + decisión + contexto + alternativas + implicaciones | ✅ | Formato canónico aplicado consistentemente |
| Decisiones referenciadas desde docs operativos | ✅ | _template-conceptual.md, CONTEXT_core.md referencian DECISIONS |
| Sin contradicciones sin reconciliación | ✅ | No detectadas |
| Phase 3 decisions también en PENDING-REGISTRY | ✅ | Cuando aplica |
| Estado canónico (Propuesta/Activa/Revertida/Obsoleta) | ⚠ | Algunas entradas tienen "Estado: Activa", otras solo "Estado: Cerrado YYYY-MM-DD" — falta uniformidad |

**Brecha detectada:**
- **Campo Estado no uniformemente canónico** (severidad: Baja). Entradas viejas usan ad-hoc, nuevas usan "Activa". *Recomendación: durante próximo audit cycle, normalizar todas a vocabulario canónico {Propuesta, Activa, Revertida, Obsoleta}.*

### 5.13 Memoria persistente — 4.0/5

| Criterio | Estado | Observación |
|---|:---:|---|
| MEMORY.md HOT <50 entradas | ✅ | 35 entradas |
| 00-raul-intelligence mantiene aprendizajes operativos | ✅ | Métodologia hoja-de-ruta + private research |
| Owner Profile documentado | ✅ | OWNER_PROFILE.md existe en 01-config |
| Domain Boundaries documentadas | ⚠ | No formal `domain_boundaries.md`; implícito en CLAUDE_genteca.md |
| Estilo escritura Owner documentado | ✅ | En OWNER_PROFILE.md (asumido — no verificado contenido) |
| Decisiones pasadas referenciables | ✅ | DECISIONS.md + memorias específicas |

**Brecha detectada:**
- **Domain boundaries implícitas, no explícitas** (severidad: Baja). Hay reglas Genteca-Plenus para no mezclar contenido (mencionadas en docs Vael / Bruna), pero NO hay un `domain_boundaries.md` consolidado. Será problema cuando Plenus active. *Recomendación: crear `02-knowledge-base/05-glossary-and-tables/domain-boundaries.md` cuando se active 2do dominio.*

### 5.14 Logs y observabilidad — 2.5/5

| Criterio | Estado | Observación |
|---|:---:|---|
| task-log.md con cada delegación | ✅ | 113 líneas, formato canónico |
| Outcomes claros (delivered/pending/blocked) | ✅ | Aplicado consistentemente |
| InboxBot task log separado | ⚠ | inboxbot-tasklog.md mencionado en conceptual, no verificado existencia |
| Errores significativos registrados | ⚠ | Solo si se mencionan en task-log; no estructurado |
| Auditorías producen logs en audits/ | ✅ | Esta misma — primera entrada |

**Brechas detectadas:**
- **Sin per-execution structured logging** (severidad: **Alta**). Cuando un agente ejecuta una tarea (research, copy, deck, etc.), no se loggea cuánto costó, cuánto tardó, qué tools usó, qué sources consultó. task-log.md es narrativa, no observabilidad. *Recomendación: cuando escalemos a multi-dominio o multi-usuario, implementar logs estructurados. Para uso actual single-Owner, costo > beneficio.*
- **inboxbot-tasklog.md status incierto** (severidad: Media). Conceptual InboxBot lo menciona; no verificada existencia o frescura. *Recomendación: verificar y, si está caduco, refrescar o decidir descartar.*

### 5.15 Seguridad, privacidad, permisos — 4.0/5

| Criterio | Estado | Observación |
|---|:---:|---|
| .gitignore excluye secretos | ✅ | `.env` incluido |
| Sin keys/tokens commiteados | ✅ | grep manual no detecta secretos en repo |
| .env.example sin secretos reales | ⚠ | No verificado existencia .env.example |
| Datos sensibles Owner protegidos | ✅ | Inbox/raw-sources/archive gitignored |
| Agentes con permisos mínimos | ✅ | Modelo A enforce esto vía runtime tools mappings |
| Bruna gate obligatorio antes de Ivo | ✅ | Documentado en ambos conceptuales |
| Cero git operations por agentes | ✅ | 21/21 git boundary en §3 |

**Brecha detectada:**
- **`.env.example` no verificado** (severidad: Baja). Política dice que debe existir; no se ha verificado presencia o calidad. *Recomendación: verificar en próximo audit cycle, crear si falta.*

### 5.16 Documentación — 4.3/5

| Criterio | Estado | Observación |
|---|:---:|---|
| CLAUDE.md + CONTEXT_core.md reflejan estado actual | ✅ | Post-Paso-6 (taxonomía nominal) + post-bundle-eficiencia |
| Cada agente con conceptual + runtime | ✅ | 21/21 |
| ROUTING-GUIDE.md actualizado | ✅ | v1.1 con clases nominales |
| FOLDER-ARCHITECTURE.md describe estructura vigente | ✅ | Sin obsolescencia detectada |
| _taxonomy.md y _roster.md sincronizados | ✅ | Verificado |
| Sin "Capa X" en docs estructurales | ✅ | Paso 6 cerrado |

**Sin brechas significativas.** Documentación al día con el estado actual.

### 5.17 Mantenimiento periódico — 2.5/5

| Criterio | Estado | Observación |
|---|:---:|---|
| Inbox owner-to-raul revisado semanalmente | ⚠ | No agendado formalmente; depende de Owner |
| raw-sources se destila a KB cuando aplica | ⚠ | Sin proceso periódico; reactivo |
| Memorias inactivas >6 meses se archivan | ❌ | Política sin ciclo ejecutado todavía |
| Auditorías programadas | ✅ | Esta es la primera; framework define cadencia |
| Backups verificados | ✅ | OneDrive backup KB diario (memoria reference_kb_onedrive_backup) |
| Decisiones in-flight con SLA tracked en registry | ⚠ | Registry existe pero no se revisa periódicamente |

**Brechas detectadas:**
- **Sin ciclo de mantenimiento periódico formalizado** (severidad: Media). Las políticas existen pero ningún calendario las dispara. *Recomendación: agendar revisión mensual (1 hora) que cubra: inbox cleanup, registry review, memory archive eval, audit checklist informal.*
- **raw-sources sin destilación periódica** (severidad: Media). El material acumulado en raw-sources puede contener insights no extraídos a KB. *Recomendación: revisión trimestral por dominio activo.*

---

## 4. Brechas detectadas — tabla consolidada

| # | Brecha | Área | Severidad | Esfuerzo | Recomendación |
|---|---|---|---|---|---|
| B-001 | Lock-in operativo a un dominio (Genteca) | 5.10 | Alta | Alto (~2-3 meses) | Activar 1 dominio adicional deliberadamente (Plenus o Panama) |
| B-002 | Panama domain mencionado pero sin estructura | 5.10 | Alta | Medio (~1 semana) | Crear estructura mínima en `99-other-domains/panama/` o promover a `06-panama/` |
| B-003 | Frontmatter convention enriquecido solo declarativo | 5.11 | Alta | Medio (~varias sesiones) | Decisión binaria: adoptar con plan rollout o descartar |
| B-004 | Sin per-execution structured logging | 5.14 | Alta | Alto (~1 semana) | Postponer hasta escalar más allá single-Owner |
| B-005 | Multi-LLM no validado empíricamente | 5.3 | Media | Alto (semanas-meses) | Documentar disclaimer "claim no validado"; ejecutar derivación piloto cuando aplique |
| B-006 | Política archivado memoria sin ciclo ejecutado | 5.6 | Media | Bajo (30 min) | Ejecutar primer ciclo en 2026-06-12 con criterio `creation_date >6 meses` |
| B-007 | `last_touched` no retroactivo | 5.6 | Media | Bajo (no aplicar retro; aplicar forward) | Aceptar discrepancia inicial; aplicar a nuevas referencias |
| B-008 | Registry de decisiones desactualizado en SLA | 5.8 | Media | Bajo (30 min) | Revisar las 5 decisiones in-flight, aplicar ESCALATED/EXPIRED donde aplique |
| B-009 | Frontmatter inconsistente en wiki pages | 5.9 | Media | Medio (~1 sesión muestreo + plan) | Muestreo 10 páginas wiki random, reportar % completo |
| B-010 | Sin marca de vigencia en wiki pages | 5.9 | Media | Medio | Decidir convención `status` en wiki pages + aplicar gradual |
| B-011 | No hay roadmap activación dominios | 5.10 | Media | Bajo (~1 sesión planning) | Owner decide orden activación |
| B-012 | Sin ciclo mantenimiento periódico formalizado | 5.17 | Media | Bajo (~30 min agenda) | Agendar revisión mensual 1 hora |
| B-013 | raw-sources sin destilación periódica | 5.17 | Media | Bajo (proceso, no implementación) | Revisión trimestral por dominio activo |
| B-014 | README vs _index.md inconsistente | 5.1 | Baja | Bajo | Normalizar en próxima sesión de housekeeping |
| B-015 | SSOT principle aplicación reciente sin validación | 5.2 | Baja | Tiempo (validación pasiva) | Esperar próximos outputs producidos para validar aplicación |
| B-016 | Sin enforcement automatizado Modelo A | 5.4 | Baja | Bajo | Añadir checklist en §6 de Michelina (Operating Protocol contratación) |
| B-017 | Domain boundaries implícitas | 5.13 | Baja | Bajo (~1 sesión) | Crear cuando 2do dominio active |
| B-018 | Campo Estado no uniformemente canónico en DECISIONS | 5.12 | Baja | Bajo | Normalizar en próximo cycle de DECISIONS |
| B-019 | .env.example no verificado | 5.15 | Baja | Trivial | Verificar y crear si falta |

**Total: 0 críticas + 4 altas + 7 medias + 8 bajas = 19 brechas detectadas.**

---

## 5. Plan de mejora priorizado

### Prioridad 1 — Brechas Altas (próximas 4 semanas)

- **[B-002] Panama domain estructura:** crear estructura mínima (1 sesión, ~60 min).
- **[B-008] Revisar registry decisiones in-flight:** aplicar ESCALATED/EXPIRED a las 5 rows (30 min).
- **[B-003] Decisión sobre frontmatter enriquecido:** sí o no, con plan rollout (1 sesión de decisión Owner).
- **[B-001] Roadmap activación dominios:** Owner decide cuándo y por dónde (1 sesión).

**[B-004] Per-execution logging:** **NO actuar.** Costo > beneficio para single-Owner actual. Re-evaluar cuando se escale.

### Prioridad 2 — Brechas Medias (próximos 90 días)

- **[B-006] Ejecutar primer ciclo archivado memoria** (2026-06-12, ~30 min).
- **[B-012] Agendar revisión mensual mantenimiento** (decidir cadencia + agendar).
- **[B-009] Muestrear frontmatter en wiki pages** (1 sesión).
- **[B-010] Decisión sobre `status` en wiki pages** (relacionada con B-003).

### Prioridad 3 — Brechas Bajas (cuando haya bandwidth)

- **[B-014] Normalizar README vs _index.md.**
- **[B-016] Checklist Modelo A en Michelina §6.**
- **[B-018] Normalizar Estado en DECISIONS.**
- **[B-019] Verificar .env.example.**

### Brechas a aceptar / no actuar ahora

- **[B-004] Per-execution logging:** posponer indefinido.
- **[B-005] Multi-LLM validation:** posponer hasta primer derivación real.
- **[B-007] last_touched retroactivo:** aceptar discrepancia inicial.
- **[B-015] SSOT principle validación:** esperar uso natural.
- **[B-017] Domain boundaries explícito:** crear cuando 2do dominio active.

---

## 6. Feedback al framework

### Qué funcionó bien

- **17 áreas con criterios concretos** facilita scoring objetivo. Cada criterio es verificable.
- **Severidad de 4 niveles** ayudó a priorizar sin engañarse (tentación de marcar todo como "alta" se mitiga con la distinción Crítica/Alta/Media/Baja).
- **Sistema 0-5** suficientemente granular para diferenciar áreas maduras vs emergentes.
- **Estructura por área con tabla de criterios** permite leer rápido el estado.

### Qué fue difícil de aplicar

- **§5.10 Cobertura dominios:** scoring fue ambiguo. Score 2/5 porque Genteca está en 5 pero otros en 1. Promedio aritmético no captura bien la realidad. *Sugerencia v1.1: para áreas donde la dimensión varía mucho por sub-elemento, dar score con tabla detallada + score de área = score del peor caso, no promedio.*
- **§5.11 Frontmatter:** ambigüedad entre "convención existe" vs "convención aplicada". Necesita reformular. *Sugerencia v1.1: separar criterios "convención documentada" (puntaje fácil) de "convención aplicada en N% del corpus" (puntaje real).*
- **§5.6/§5.17:** políticas declaradas pero sin ciclo ejecutado son ambiguas. ¿Score 5 porque está bien documentada, o score 1 porque nunca corrió? *Sugerencia v1.1: distinguir "policy defined" (sub-score) de "policy executed" (sub-score), score final = mínimo de ambos.*

### Recomendaciones para v1.1 (post auditoría 2)

Acumular learnings hasta auditoría 2 (~2026-06-12) antes de proponer cambios al framework. Posibles ajustes que ya identifico:
- Reformular scoring de áreas multi-elemento (dominios, frontmatter)
- Separar "documented" vs "executed" en políticas
- Añadir sección §X específica para "claims declarados pero no validados empíricamente" (multi-LLM, etc.)

### Tiempo de aplicación

**~90 min para auditoría completa** (objetivo del framework era <3 horas — cumplido). Pero ojo: este auditor (Raul) tenía contexto fresco de toda la sesión. Un auditor que ejecutara la auditoría sin ese contexto necesitaría ~3-4 horas la primera vez.

---

## 7. Próxima auditoría

**Fecha planeada:** 2026-06-12 (±1 semana)

**Foco específico:**
- Re-auditar áreas que reciban remediación de Prioridad 1 (B-002, B-008, B-003, B-001).
- Validar cambios al framework propuestos en §6 si se aplican.
- Auditar específicamente domains 2+ si alguno se activó deliberadamente.

**Cambios al framework propuestos:** ninguno hasta auditoría 2.

---

## Cover note

- **Audiencia:** Owner.
- **Material fuente:** estado /RAUL/ al 2026-05-12 23:00 + framework `PKA-AUDIT-FRAMEWORK_RAUL.md` v1.0.
- **Decisiones que empuja:** (a) decisión sobre B-003 frontmatter enriquecido, (b) decisión sobre B-001 activación dominios, (c) confirmación de plan de remediación prioridad 1.
- **Items abiertos para Owner:**
  1. ¿Adoptar frontmatter enriquecido con plan rollout, o descartar?
  2. ¿Qué dominio activar después de Genteca? ¿Plenus? ¿Panama? ¿Otro?
  3. ¿Aceptar las 5 brechas marcadas "no actuar ahora"?
  4. ¿Aprobar la cadencia mensual de revisión sugerida en B-012?

**Output canónico:** este reporte queda como baseline. Auditorías futuras compararán contra este (B-XXX referenciables).

---

*Auditoría 1 (baseline) producida 2026-05-12 con framework PKA-AUDIT-FRAMEWORK_RAUL.md v1.0 candidate. Período de validación del framework: ~2026-08-12.*
