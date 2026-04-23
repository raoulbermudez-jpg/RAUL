# CONTEXTO — /RAUL/ al 2026-04-22

## Repo y commits clave

Repositorio: `C:\RAUL` (git inicializado)

Commits relevantes (últimos):

- `6b18fbf` — **Fase 3 cross-dominios — Plenus-metabólica creada**  
  Estructura completa en `02-knowledge-base/02-domains/02-plenus-metabolica/` con:
  - `_index.md` (dominio Plenus-metabólica)
  - `wiki/_index.md` (wiki stub)
  - `wiki/market/_index.md` (market intelligence Plenus)
  - `specs/_index-specs.md` (fichas técnicas stub)
  - `assets/_index.md` (assets con products/packaging/infographics/uncoded)

- `8b4db53` — **Owner edits — plantillas Genteca v1 finales**  
  Ajustes finos en:
  - `02-knowledge-base/02-domains/01-genteca/_index.md`
  - `02-knowledge-base/02-domains/01-genteca/wiki/market/_index.md`  
  Cambios: “sistema /RAUL/” + bala de Market intelligence con competidores locales + secciones de alcance y tipos de competidor.

- `3893f73` — **Fase 3 — KB Genteca + assets + proyectos activos migrados**  
  Genteca KB (specs + assets + wiki stub) y proyectos Genteca 2026-04 migrados.

- `4e22861` — **Fase 2 — system migrado** (04-system/, agentes, etc.)  
- `54aac6e` — **Skeleton Raul 2026 — pre-migration**

## Dominios /KB ya activos

1. **Genteca (01-genteca/)**  
   - KB: `02-knowledge-base/02-domains/01-genteca/`
     - `_index.md` — dominio Genteca (alcance, marcas, mercados, estructura, tipos de proyecto, equipo humano, agentes).
     - `wiki/_index.md` — wiki stub (artículos futuros, qué va / qué no va).
     - `wiki/market/_index.md` — market intelligence Genteca:
       - Alcance de documentos de mercado/competidores.
       - “Alcance inicial de competidores” (no exhaustivo, Owner define foco).
       - Taxonomía de tipos de competidor (fabricante global, importador local, ensamblador local, marca white-label), productor/consumidor, índice de documentos.
     - `specs/` — 193 fichas técnicas migradas del repo viejo (protectores, SPDs, etc.).
     - `assets/` — estructura de products/packaging/diagrams/uncoded con index bien descrito.
   - Proyectos activos en `03-projects/genteca/`:
     - `2026-04_GSM-MB-RB-RF_empaque/` con README detallado (objetivo, stakeholders, organización, pendientes, enlaces a KB).
     - `2026-04_GST-R_etiquetas/` con README análogo.

2. **Plenus-metabólica (02-plenus-metabolica/)**  
   - KB: `02-knowledge-base/02-domains/02-plenus-metabolica/`
     - `_index.md` — dominio Plenus:
       - Alcance: alimentos funcionales, salud metabólica, longevidad.
       - Distinción respecto a Teca/Teak4Food, marca personal y Genteca.
       - Audiencias (consumidor, profesional de salud, retail especializado).
       - Tipos de proyectos (protocolos, materiales educativos, funnels, etc.).
       - Sección explícita de relación con NotebookLM (RAUL como LLM wiki + proyectos, futura consolidación documentada en DECISIONS).
     - `wiki/_index.md` — wiki stub:
       - Lista de artículos futuros (fundamentos metabólicos, protocolos, microbiota, longevidad, casos, consolidación NotebookLM).
       - Qué va / qué no va.
       - Sección “Relación explícita con NotebookLM” con plan de 3 pasos (revisar colecciones, priorizar, reescribir/citar origen).
     - `wiki/market/_index.md` — market intelligence Plenus:
       - Alcance específico al espacio alimentos funcionales/salud metabólica.
       - “Alcance inicial de competidores”.
       - Taxonomía de 5 tipos de competidor (los 4 análogos a Genteca + “programa/servicio clínico con oferta integrada de producto”).
       - Productor/consumidor.
     - `specs/_index-specs.md` — qué se espera en fichas técnicas (composición, claims, etiquetas, certificaciones, etc.).
     - `assets/_index.md` — estructura con `products/`, `packaging/`, `infographics/`, `uncoded/` y convención de nombres.
   - Proyectos Plenus: carpeta `03-projects/plenus-metabolica/` existe como placeholder (vacía por ahora).

## Estado de fases

- **Fase 1** — Skeleton /RAUL/ completo (estructura base, CONTEXT_core.md, etc.).  
- **Fase 2** — System + agentes migrados y validados.  
- **Fase 3 Genteca** — completada y validada (KB + proyectos + raw sources).  
- **Fase 3 Plenus-metabólica** — completada a nivel KB (estructura + índices).  
- **Fase 3 cross-dominios — resto**:
  - CONGELADOS: Teca/Teak4Food, marca-personal-raoul, research-generic, sandbox, Finca.
- **Fase 4 en adelante** — aún no iniciada (limpieza repo viejo, integración Drive, InboxBot, etc.).

## Decisiones abiertas

- Numeración de dominios: se está usando `02-plenus-metabolica/`, mientras FOLDER-ARCHITECTURE.md original listaba Plenus como 03. Opciones:
  - (i) Actualizar FOLDER-ARCHITECTURE.md + DECISIONS.md para reflejar Plenus=02 (orden por prioridad).
  - (ii) Explicar que la numeración no es secuencial.
  - (iii) Volver Plenus a 03 (NO recomendado).

- Integración con NotebookLM:
  - Puerta abierta ya documentada en índices Plenus.
  - No hay sincronización técnica todavía; se prevé futura fase para reescribir/consolidar contenidos NotebookLM como artículos wiki/specs.