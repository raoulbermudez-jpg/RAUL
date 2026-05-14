# Team Roster — /RAUL/

**Catálogo del equipo de agentes.** Quién está, en qué clase y de qué
dominio. La definición de **clases** vive en `_taxonomy.md`. El
comportamiento de cada agente vive en `conceptual/<agente>.md`.

---

## Tabla resumen

| Agente | Clase | Dominio | Rol principal | Conceptual |
|---|---|---|---|---|
| **Raul** | `orchestration` | transversal | Chief of Staff / Orchestrator | `conceptual/raul.md` |
| **Michelina** | `governance` | transversal | Head of HR | `conceptual/michelina.md` |
| **Bruna** | `governance` *(+ content-supply-chain)* | transversal | Brand & Risk Governance | `conceptual/bruna.md` |
| **Paxs** | `global-service` | transversal | Senior Researcher | `conceptual/paxs.md` |
| **Vivienne** | `global-service` | transversal | Presentation Designer | `conceptual/vivienne.md` |
| **Aurelio** | `content-supply-chain` | transversal | Content Strategist CSC (AU-1..AU-5) | `conceptual/aurelio.md` |
| **Nerea** | `content-supply-chain` | transversal | Script & Narrative Architect CSC (NE-1..NE-5) | `conceptual/nerea.md` |
| **Orfeo** | `content-supply-chain` | transversal | Motion Graphics & Visual Systems Production Lead (OR-1..OR-5) | `conceptual/orfeo.md` |
| **Luma** | `content-supply-chain` | transversal | Video & Motion Producer (Producción) | `conceptual/luma.md` |
| **Vela** | `content-supply-chain` | transversal | Narration & Voiceover (Producción) | `conceptual/vela.md` |
| **Atlas** | `content-supply-chain` | transversal | Static Visual Producer (Producción) | `conceptual/atlas.md` |
| **Ivo** | `content-supply-chain` | transversal | Distribution & Channel Strategist | `conceptual/ivo.md` |
| **Sira** | `content-supply-chain` | transversal | Archive, Version & Recycling — single source of truth para reciclaje (AU-5) | `conceptual/sira.md` |
| **Vera** | `domain-specialist` | Genteca | Technical Researcher (Electrical Protection) | `conceptual/vera.md` |
| **Orlan** | `domain-specialist` | Genteca | Market Intelligence Analyst | `conceptual/orlan.md` |
| **Solenne** | `domain-specialist` | Genteca | Copy & Editorial Execution Lead | `conceptual/solenne.md` |
| **Vael** | `domain-specialist` | Genteca | Branding & Communication Strategist | `conceptual/vael.md` |
| **Celeste** | `domain-specialist` | Genteca | Knowledge Base Librarian + KB Curator (estrategia/narrativa) | `conceptual/celeste.md` |
| **Renzo** | `domain-specialist` | Genteca | Application Engineer | `conceptual/renzo.md` |
| **Oz** | `domain-specialist` | Genteca | Technical Documentation Editor | `conceptual/oz.md` |
| **InboxBot** | `execution-utility` | transversal | Capture & Queue utility | `conceptual/inboxbot.md` |

---

## Por clase

### `orchestration`

- **Raul** *(singleton)* — único punto de entrada. Recibe, decide, delega,
  revisa, devuelve. No ejecuta.

### `governance`

- **Michelina** — gobernanza de composición del equipo. Hiring de nuevos
  agentes vía Paxs. Gate obligatorio cuando ningún agente cubre una
  necesidad.
- **Bruna** — gobernanza de outputs públicos. Aprueba o bloquea cualquier
  pieza antes de que Ivo la publique. Gate obligatorio en CSC. *(También
  posición en `content-supply-chain`.)*

### `global-service`

- **Paxs** — investigador senior transversal. Cubre temas multi-dominio o
  no-cubiertos por especialistas. También perfila roles humanos para
  Michelina.
- **Vivienne** — diseñadora de presentaciones transversal. Toma contenido
  ya trabajado y lo convierte en decks ejecutivos.

### `content-supply-chain`

Pipeline transversal de producción de contenido. Detalle de la arquitectura
en `content-supply-chain/ARCHITECTURE_Content-Supply-Chain.md`.

**Estrategia:**
- **Aurelio** — content strategist CSC transversal (AU-1..AU-5: plan
  por campaña, mapa trimestral, briefs a Nerea / Solenne,
  reciclaje).
- **Nerea** — script & narrative architect CSC transversal (NE-1..NE-5:
  guion largo, corto / reel, carrusel narrativo, audio / conversación,
  narrative map).

**Producción:**
- **Orfeo** — motion graphics & visual systems production lead
  (OR-1..OR-5: motion specs, animated asset packs, scene motion
  maps, format adaptation, handoff a Luma/Ivo). Audio multi-voz /
  podcast pasa a Vela vía NE-4 con turnos etiquetados.
- **Luma** — video & motion producer (shorts, reels, largo, motion graphics).
- **Vela** — narration & voiceover (voz única narrativa).
- **Atlas** — static visual producer (carruseles, infografías, POP).

**Distribución:**
- **Ivo** — channel & distribution strategist (publica solo lo aprobado por
  Bruna).

**Memoria:**
- **Sira — Archive, Version & Recycling Librarian.** Archiva cada pieza
  publicada, mantiene el catálogo versionado transversal y propone
  reciclajes. Es la memoria viva del CSC y la **fuente única de
  reciclaje estructurado**: **AU-5 (Recomendación de Reciclaje) de
  Aurelio se basa exclusivamente en su catálogo**. Mantiene el árbol
  canónico de índices en `04-system\05-indexes\`; lo que no esté ahí
  no existe como memoria reciclable.

### `domain-specialist` — Genteca

- **Vera** — technical research (relés, protectores, IEC/NEMA).
- **Orlan** — market intelligence (benchmarking ABB/Eaton/Schneider/Siemens).
- **Solenne** — copy & editorial execution lead (consume VA-X / BR-X; SO-1..SO-5).
- **Vael** — branding & communication strategy.
- **Celeste — Knowledge Base Librarian (Genteca).** Clasifica y normaliza
  fuentes crudas (PDF, DOCX, XLSX, transcripts) entre Technical KB y
  Market KB, mantiene naming y versiones, y actúa como **curadora del
  KB de estrategia y narrativa**: decide qué AU-1/AU-2 de Aurelio, qué
  NE-X de Nerea y qué frameworks VA-X / BR-2 / BR-5 pasan a ser patrones
  de referencia de largo plazo, y con qué path, nombre y estructura
  viven en el KB.
- **Renzo** — application engineer (diagramas, instalación, troubleshooting).
- **Oz** — technical documentation editor (redlines, delta docs para Ozwaldo).

*(Otros dominios — Plenus, Finca, Teca, marca-personal — sin especialistas
activos al cierre de esta versión del roster.)*

### `execution-utility`

- **InboxBot** — utilidad capture-only (v5.0): captura ítems de los
  canales remotos (Drive) y los encola como tickets para Raul-desktop. No
  procesa. Trigger cada 2h, ventana 6:00–23:00 Caracas.

---

## Reglas operativas del roster

- **Actualización:** Michelina actualiza el roster en cada contratación o
  refinement (paso 4 de su Operating Protocol).
- **Clase única por agente** (excepción documentada: Bruna).
- **Domain "transversal"** se usa cuando el agente sirve a todos los
  dominios; si está anclado a uno, se nombra explícitamente
  (`Genteca`, `Plenus`, etc.).
- Si un agente está en este roster, debe existir su `conceptual/<agente>.md`.
  La inversa también: todo conceptual debe figurar aquí.

---

*Roster vigente desde 2026-05-01. Refleja la migración a taxonomía nominal
de 6 clases registrada en `04-system/03-governance/DECISIONS.md`.*
