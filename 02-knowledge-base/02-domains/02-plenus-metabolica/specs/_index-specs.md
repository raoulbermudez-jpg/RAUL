# Plenus-metabólica — Specs (index)

**Estado:** stub. Esta carpeta albergará fichas técnicas de productos Plenus (alimentos funcionales, suplementos, nutracéuticos), composiciones, tablas nutricionales, claims de salud documentados, etiquetas técnicas y material regulatorio.

## Qué va aquí (cuando se pueble)

- **Fichas de producto** — una por SKU: nombre comercial, composición cualitativa y cuantitativa, presentación, forma farmacéutica/alimentaria, vida útil, condiciones de almacenamiento.
- **Claims respaldados** — afirmaciones de salud asociadas al producto, con fuentes científicas y cumplimiento regulatorio por geografía.
- **Etiquetas técnicas** — tabla nutricional, ingredientes, alérgenos, advertencias, sello regulatorio.
- **Certificaciones** — si aplica (buenas prácticas de manufactura, orgánico, non-GMO, etc.).
- **Manuales de uso profesional** — para canal clínico: protocolos de administración, interacciones, contraindicaciones.

## Qué NO va aquí

- Artículos educativos o marcos conceptuales → `wiki/`.
- Material visual (packshot, mockups de etiqueta) → `assets/`.
- Documentos de un lanzamiento en curso → `/RAUL/03-projects/plenus-metabolica/<proyecto>/`.
- Claims sin respaldo formal → no se archivan como specs; se marcan como draft en el proyecto y se escalan a Bruna antes de publicar.

## Convención de nombres

- Preferente: `YYYY-MM-DD_tipo_slug-producto.md`
  - Ejemplos: `2026-05-01_ficha-producto_plenus-metabolix-60caps.md`, `2026-05-01_claims-respaldados_plenus-metabolix.md`, `2026-05-01_etiqueta-tecnica_plenus-metabolix.md`.

## Productor / consumidor

- **Productor:**
  - Celeste al procesar PDFs, Word, Excel recibidos del formulador/área regulatoria.
  - "Vera-equivalente" Plenus (cuando se contrate) al validar composición y claims.
  - Oz-equivalente editorial si se adopta un agente análogo para Plenus (decisión futura).
- **Consumidor:**
  - Bruna (validación de claims en piezas públicas).
  - Aurelio/Nerea (estrategia y copy).
  - Agentes de canal profesional (formación, materiales clínicos).

## Índice de documentos

| Filename | Date Added | Document Type | Description |
|----------|-----------|---------------|-------------|
| _(pendiente)_ | — | — | Primer intake de ficha de producto. |

## Notas de versión

- **v1 — 2026-04-22** — stub inicial. Se poblará cuando el Owner entregue el primer catálogo de producto Plenus o cuando arranque la consolidación de NotebookLM (si NotebookLM contiene fichas técnicas formales).
