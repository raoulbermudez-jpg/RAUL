# Agent Taxonomy — Clases canónicas del sistema /RAUL/

**Aplica a:** todo agente del repo. Toda contratación nueva (vía Michelina)
y toda migración asigna al agente una clase de las definidas aquí.

> Este documento define **qué clases existen**. La lista de **quién está**
> en cada clase vive en `_roster.md`.

---

## Clases canónicas

Seis clases. Nombres con guion para consistencia en tablas, frontmatter y grep.

### `orchestration`

**Definición:** agente que recibe toda petición del Owner, identifica el
tipo y dominio, rutea al especialista correcto, revisa el output y lo
devuelve. No ejecuta tareas.

**Criterios de membresía:**
- Es punto de entrada único del sistema.
- No produce deliverables propios.
- Toma decisiones de routing pero nunca de contenido.

**Ejemplos vigentes:** `raul` (singleton).

---

### `governance`

**Definición:** agente que gobierna **estructura del sistema** o
**aprobación de outputs** antes de su salida pública. Custodia reglas,
gates y composición del equipo.

**Criterios de membresía:**
- Su rol es aprobar, gatear o estructurar — no producir.
- Su intervención es obligatoria en algún punto del flujo (gate
  irrenunciable).
- Custodia un dominio de reglas (composición del equipo, marca, riesgo,
  cumplimiento).

**Ejemplos vigentes:**
- `michelina` — gobernanza de composición del equipo (hiring).
- `bruna` — gobernanza de outputs públicos (brand & risk approval).

---

### `global-service`

**Definición:** agente transversal que sirve a cualquier dominio cuando se
le invoca. No está anclado a un dominio específico.

**Criterios de membresía:**
- Servicio invocable on-demand desde cualquier dominio.
- No requiere conocimiento especializado de un dominio para operar bien.
- Recibe contexto de dominio vía brief de Raul.

**Ejemplos vigentes:**
- `paxs` — investigación transversal.
- `vivienne` — diseño de presentaciones transversal.

---

### `domain-specialist`

**Definición:** agente anclado a un dominio específico (Genteca, Plenus,
Finca, Teca, marca-personal). Conoce productos, terminología, stakeholders
y reglas internas del dominio.

**Criterios de membresía:**
- Su trabajo requiere conocimiento profundo de un dominio.
- Consulta la KB de su dominio (`02-knowledge-base/02-domains/<dominio>/`).
- No se reusa entre dominios — cada dominio tiene su propio set.

**Ejemplos vigentes (todos Genteca):**
- `vera` — technical research, electrical protection.
- `orlan` — market intelligence, electrical protection.
- `solenne` — B2B content creator.
- `vael` — branding & communication strategy.
- `celeste` — knowledge base librarian.
- `renzo` — application engineer.
- `oz` — technical documentation editor.

---

### `content-supply-chain`

**Definición:** agente que forma parte de la cadena transversal de
producción de contenido (Capa 2b en la nomenclatura previa). Opera en una
posición específica del pipeline estrategia → script → producción →
gobernanza → distribución → memoria.

**Criterios de membresía:**
- Forma parte de un pipeline secuencial coreografiado, no se invoca aislado
  como global-service.
- Sirve a todos los dominios.
- Su rol está documentado en
  `04-system/02-agents/content-supply-chain/ARCHITECTURE_Content-Supply-Chain.md`.

**Ejemplos vigentes:**
- `aurelio` — Estrategia (content strategist).
- `nerea` — Estrategia (script & narrative architect).
- `orfeo` — Producción (audio & multi-voice conversation).
- `luma` — Producción (video & motion).
- `vela` — Producción (narration & voiceover).
- `atlas` — Producción (static visual).
- `bruna` — Gobernanza de output (también `governance` — ver nota abajo).
- `ivo` — Distribución (channel & metadata).
- `sira` — Memoria (archive, version & recycling).

**Nota sobre Bruna:** Bruna pertenece tanto a `governance` (rol funcional)
como a `content-supply-chain` (posición en el pipeline). En el roster se
clasifica primariamente como `governance` con anotación de pertenencia al
pipeline CSC. Esta es la única doble-pertenencia permitida hoy.

---

### `execution-utility`

**Definición:** agente de infraestructura que ejecuta una función mecánica
del sistema, sin tomar decisiones de contenido ni de routing.

**Criterios de membresía:**
- Función mecánica reproducible (mensajería, sincronización, scheduling).
- No emite juicio sobre contenido.
- Suele invocarse vía trigger automático (cron, schedule, webhook), no por
  un humano.

**Ejemplos vigentes:**
- `inboxbot` — mensajero entre canales remotos y Raul.

---

## Reglas de gestión de la taxonomía

### Crear una clase nueva

Una clase nueva se crea solo cuando:

1. Existen al menos **dos agentes** que claramente no encajan en ninguna
   clase actual.
2. Los criterios de membresía son distinguibles (no solapan con clases
   existentes).
3. La decisión se registra en `04-system/03-governance/DECISIONS.md`.

### Eliminar una clase

Una clase se elimina solo cuando:

1. **Cero agentes** la habitan en el roster.
2. Se documenta en `DECISIONS.md` la razón y el estado de los agentes que
   la habitaron previamente.

### Mover un agente entre clases

Cambio de clase de un agente requiere:

1. Actualizar `_roster.md`.
2. Actualizar el footer del conceptual del agente (`*<Class>.*`).
3. Actualizar `Class:` field en cualquier anuncio de contratación
   referenciando ese agente.
4. Si el cambio es estructural (no menor), entrada en `DECISIONS.md`.

---

*Taxonomía vigente desde 2026-05-01. Cualquier cambio requiere entrada en
`DECISIONS.md`.*
