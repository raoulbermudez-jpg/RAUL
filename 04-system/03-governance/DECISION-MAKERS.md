---
document_id: "DECISION-MAKERS"
document_type: "governance-registry"
author: "Claude Opus 4.7 + Owner"
creation_date: "2026-05-09"
last_updated: "2026-05-09"
purpose: "Registro central de decisores con autoridad para aprobar/rechazar/condicionar decisiones en el flujo de trabajo del sistema /RAUL/. Consultado por agentes que llegan a decision gate para identificar a quién enrutar y por qué canal."
audience: ["Agentes productores y de gates (Bruna, Aurelio, Vael, Vera, Orlan, InboxBot, Raul orchestrator)", "Owner"]
status: "active"
ssot_for: ["decision-makers-registry"]
depends_on: ["GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md", "DECISIONS.md"]
version: "1.0"
how_to_use: "Cuando un agente llega a un decision gate (información insuficiente para producir output sin riesgo, claim que requiere validación externa, propuesta que requiere voto, etc.), consultar esta tabla para identificar decisor + canal correcto + SLA esperable. Si el decisor no está aquí, escalar a Owner para definir entrada nueva ANTES de proceder."
---

# DECISION-MAKERS — Registro de decisores del Sistema /RAUL/

## Cómo se usa este registro

Cuando un agente del sistema (Bruna, Aurelio, Vael, Vera, Orlan, etc.) llega a un punto donde no puede continuar sin input de un humano externo a la cadena, consulta este registro para:

1. **Identificar decisor correcto** según el scope de la decisión.
2. **Determinar canal de comunicación** (carpeta del filesystem, email mediado, presentación física, etc.).
3. **Estimar SLA típico** para planificar continuidad o pause.
4. **Conocer ruta de escalación** si el decisor no responde dentro del SLA.

El **ID corto** sirve como referencia rápida en `PENDING-DECISIONS-REGISTRY.md` y en el filename de packages (ej. `JUNTA-GENT_2026-05-09_NNN.md`).

---

## Tabla de decisores activos

| ID | Decisor | Tipo | Scope | Canal preferido | SLA típico | Escalación si timeout/no-response | Notas / anti-patterns |
|----|---------|------|-------|-----------------|------------|------------------------------------|----------------------|
| `OWNER` | Raoul Bermúdez | Humano-individual | Decisiones arquitectónicas, estratégicas, scope de proyectos, override de cualquier otro decisor. Aprobación final de claims sensibles, presupuesto, timing de lanzamientos, dirección estratégica de cualquier dominio. | `01-inbox/01-owner-to-raul/` (entrada) + `01-inbox/02-deliverables-to-owner/` (salida) | <24h cuando online; pausa cuando offline | N/A — Owner es máxima autoridad interna | NO usar para decisiones puramente técnicas que Vera/Orlan resuelven; NO usar para pricing/positioning táctico que Aurelio puede decidir |
| `JUNTA-GENT` | Junta Directiva Genteca | Humano-grupo | Decisiones estratégicas Genteca (lanzamiento productos nuevos, cierre líneas, capital, partnerships, cambios marca, fusiones). Aprobación de campañas de lanzamiento mayores. | Presentación física en reunión + `01-inbox/05-from-junta/` (respuestas formales en filesystem) | 2-4 semanas (cadencia reuniones mensuales) | Owner mediates si urgente; puede convocar reunión extraordinaria con justificación | NO usar para tácticas (eso lo decide equipo Genteca); NO usar para campañas pequeñas (Aurelio + Owner basta) |
| `IND-GENT` | Equipo I&D Genteca (Kike + Liliam principalmente) | Humano-grupo | Decisiones técnicas dispositivos, validación specs, escalación de riesgo de diseño, confirmación de comportamiento bajo condiciones extremas, especificaciones de fabricación | Email/whatsapp directo Owner-mediated. Future channel: `colaboradores/Genteca/I-D/` con estructura inbox/outbox | 1-7 días | Owner si urgente | NO usar para mercadeo o positioning; NO sustituye a Vera (Vera consulta I&D, no al revés) |
| `COMERCIAL-GENT` | Equipo comercial Genteca (Kike + ML + MPR vendedores) | Humano-grupo | Pricing definitivo, positioning final, decisiones de canal comercial, prioridades de catálogo, relaciones con distribuidores | Similar a I&D (email/whatsapp future channel) | 3-7 días | Owner | NO usar para validación técnica (eso es I&D / Vera) |
| `SAPI-VE` | SAPI Venezuela (Servicio Autónomo de la Propiedad Intelectual) | Organismo-gov | Registro/oposición de marcas, clearances IP, oposiciones a terceros | Web SAPI sapi.gob.ve (fuera del sistema RAUL); submissions vía abogado IP | Meses (típico 6-12 para registro completo; 1-3 meses primera respuesta) | Legal externo cuando casos contenciosos | Tener legal externo involucrado SIEMPRE para submissions formales; NO presentar sin clearance previo de Vael+Bruna sobre claim |
| `SENCAMER` | Servicio Autónomo Nacional de Normalización, Calidad, Metrología y Reglamentos Técnicos | Organismo-gov | Normas técnicas COVENIN, certificaciones de cumplimiento, validación de procesos productivos | Web SENCAMER (paralelo al sistema) | Meses | Legal externo + I&D Genteca para casos técnicos | NO confundir con FONDONORMA (FONDONORMA elabora normas, SENCAMER las certifica) |
| `FONDONORMA` | Fondo para la Normalización y Certificación de la Calidad | Organismo-norm | Verificación de normas, auditorías de sistemas de gestión de calidad | Web FONDONORMA | Meses | Legal externo | NO usar para registro de marca (eso es SAPI) |
| `LEGAL-EXT` | Legal externo (estudio jurídico) | Humano-individual | Casos sensibles claims, IP contencioso, contratos importantes, response a demandas, asesoría regulatoria | Email vía Owner (no acceso directo del sistema) | 3-7 días para asesoría; semanas para casos contenciosos | N/A (Owner decide cuándo escalar y a quién más) | NO usar para preguntas legales rutinarias que la propia política RISK-POLICY ya cubre; usar solo para casos no cubiertos |
| `PANAMA-CONTRA` | Contrapartes de Panamá (varios — inmobiliaria, contratistas, vecinos Embassy Club) | Humano-individual | Negociaciones apartamento, contratos de alquiler/hipoteca, mantenimiento, pagos a terceros | Email/WhatsApp; future channel `01-inbox/07-from-third-parties/Panama/` | Variable (horas a días según contraparte) | Owner | Caso por caso; algunos requieren legal externo (contratos), otros no |
| `PLENUS-ASESOR` | Asesores científicos Plenus (futuro — TBD) | Humano-grupo | Decisiones científicas/nutricionales sobre formulación de alimentos funcionales, validación de claims metabólicos, dirección de I+D Plenus | (canal sin definir aún) | TBD | Owner | Pending: Owner debe identificar asesores específicos antes de activar dominio Plenus |
| `MERCADO-PROXY` | Audiencia / mercado (no es decisor, es proxy via investigación) | Humano-grupo (proxy) | Validación empírica de mensaje, test de aceptación de productos, pricing studies (ej. Van Westendorp GME) | Estudios de mercado encargados (encuestas online, focus groups) | Semanas-meses | N/A — datos, no decisión | NO es decisor en sentido estricto; los datos informan a Owner/junta para que ELLOS decidan. Distinguir entre "mercado dijo X" (dato) y "junta decide Y basado en X" (decisión) |

---

## Reglas de uso

1. **Cuando un agente identifica decision gate, primero busca aquí.** No improvisar canales.
2. **Si el decisor existe pero el canal "future" no está activo**, usar canal informal (email vía Owner) y registrar en `PENDING-DECISIONS-REGISTRY.md` con nota.
3. **Si el decisor NO existe en este registro**, escalar a Owner para que decida si:
   - (a) Agregar decisor nuevo a este registro.
   - (b) Mapear la decisión a un decisor existente.
   - (c) Dejar como decisión Owner-only.
4. **Cualquier modificación a esta tabla** se registra en `DECISIONS.md` con razón.
5. **Cuando un decisor se vuelve obsoleto** (ej. cambio de organigrama Genteca, cierre de relación con asesor externo), NO se borra: se mueve a sección "Histórico" abajo con fecha y razón.

---

## Histórico de decisores (ya no activos)

(Vacío al inicio — se llena cuando un decisor sale del registro activo)

| ID | Decisor | Fecha activo | Razón cierre | Decisor sucesor (si aplica) |
|----|---------|--------------|--------------|------------------------------|

---

## Multi-decision-maker convergence

Algunos casos requieren **aprobación combinada** de múltiples decisores. Patrón típico:

| Tipo de decisión | Decisores requeridos | Lógica |
|------------------|----------------------|--------|
| Lanzamiento producto nuevo Genteca | OWNER + JUNTA-GENT + IND-GENT + COMERCIAL-GENT | Todos deben aprobar; cualquier rechazo bloquea |
| Claim regulatorio sensible (ej. COVENIN) | OWNER + LEGAL-EXT + SENCAMER/FONDONORMA | Validación legal y certificación regulatoria antes de uso |
| Marca registrada nueva | OWNER + LEGAL-EXT + SAPI-VE | Owner aprueba propuesta, legal externo prepara filing, SAPI registra |
| Compra/venta inmueble Panama | OWNER + LEGAL-EXT + PANAMA-CONTRA | Owner decide intención, legal revisa contrato, contraparte firma |

Ver patrón "Multi-decision-maker convergence" en `GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md` sección A.4.

---

## Referencias

- [`GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md`](GOVERNANCE-PROPOSAL-PHASE2-2026-05-09.md) — propuesta arquitectónica completa.
- [`GOVERNANCE-DIAGNOSTIC-2026-05-09.md`](GOVERNANCE-DIAGNOSTIC-2026-05-09.md) — diagnóstico que originó este registro.
- [`PENDING-DECISIONS-REGISTRY.md`](PENDING-DECISIONS-REGISTRY.md) — kanban acumulativo de decisiones in-flight (referencia este registro vía ID).
- [`RISK-POLICY.md`](RISK-POLICY.md) — política de riesgo Bruna.
- [`DECISIONS.md`](DECISIONS.md) — log de decisiones arquitectónicas.

---

**Estado:** activo desde 2026-05-09. Update cuando emerjan decisores nuevos o cambios estructurales en organizaciones existentes.
