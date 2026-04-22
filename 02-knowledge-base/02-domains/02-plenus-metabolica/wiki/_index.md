# Plenus-metabólica — Wiki (index)

**Estado:** stub. Esta carpeta se poblará con artículos compilados sobre salud metabólica, fundamentos de alimentos funcionales, protocolos clínicos y patrones observados en casos reales. Primera fuente prevista de contenido: **consolidación del material histórico que vive en NotebookLM** (ver `_index.md` del dominio para contexto de "puerta abierta").

## Subcarpetas

- `market/` — Market intelligence específico de Plenus: competidores en alimentos funcionales y suplementos, tendencias en salud metabólica y longevidad, entorno regulatorio. Provisional bajo el dominio; se reevaluará promover a `03-cross-cutting/` si crece el marketing transversal.

## Qué va aquí (cuando se pueble)

Propuesta inicial de artículos — ajustable a medida que se compile desde NotebookLM o se documente desde proyectos cerrados:

- `01-fundamentos-salud-metabolica.md` — resistencia a la insulina, inflamación crónica de bajo grado, disfunción mitocondrial, disbiosis.
- `02-alimentos-funcionales-y-nutraceuticos.md` — categorías, principios activos, evidencia, claims defendibles.
- `03-protocolos-por-condicion.md` — patrones de intervención para las condiciones que Plenus aborda (ej. síndrome metabólico, sobrepeso inflamatorio, fatiga metabólica).
- `04-microbiota-y-fermentos.md` — intersección con temas del mismo autor en `03-cross-cutting/` (reutilizable transversalmente).
- `05-longevidad-saludable-marcos.md` — marcos de trabajo (healthspan vs lifespan, biomarcadores, intervenciones).
- `06-lecciones-de-casos-clinicos.md` — patrones observados en casos reales Plenus (con consentimiento).
- `07-consolidacion-notebooklm-YYYY-MM.md` — artículo(s) que recojan material consolidado desde colecciones específicas de NotebookLM, una vez que arranque la fase de sincronización.

## Qué NO va aquí

- Fichas de producto, composiciones, claims regulatorios → `specs/`.
- Material visual (fotos, infografías, packshots) → `assets/`.
- Documentos de un proyecto en curso (lanzamiento, campaña, funnel) → `/RAUL/03-projects/plenus-metabolica/<proyecto>/`.
- SOPs generales no específicos de Plenus (ej. cómo evaluar un paper) → `/RAUL/02-knowledge-base/04-sops-and-playbooks/`.
- Material de marketing transversal entre dominios (ej. temas que aplican también a Teca o marca personal) → `03-cross-cutting/`.

## Producción y consumo

- **Producido por:**
  - Paxs (research agnóstico sobre temas metabólicos cuando haga falta).
  - Agente "Vera-equivalente" en medicina funcional / ciencia metabólica, cuando se contrate (pendiente).
  - Celeste al normalizar contenido importado desde NotebookLM durante la futura fase de sincronización.
- **Consumido por:** todos los agentes que trabajen tareas Plenus — especialmente Aurelio (estrategia de contenido), Nerea (guiones), Vael del dominio (cuando exista) — como contexto persistente antes de ir a internet.

## Relación explícita con NotebookLM

- NotebookLM contiene la base de conocimiento histórica de Plenus generada antes del sistema /RAUL/.
- Esta wiki es la nueva fuente viva; lo compilado aquí es vendor-neutral (.md) y reutilizable por cualquier LLM.
- Cuando se active la fase de consolidación:
  1. Se revisarán las colecciones/libros de NotebookLM.
  2. Se priorizará por utilidad para proyectos activos y por densidad de conocimiento estable.
  3. Cada artículo resultante aquí cita su origen NotebookLM como fuente y queda catalogado en este índice.
- Hasta entonces, la wiki crece con contenido nuevo que se produzca desde el arranque de Fase 3 Plenus.

## Notas de versión

- **v1 — 2026-04-22** — stub inicial, alineado con plantilla wiki Genteca v1.
