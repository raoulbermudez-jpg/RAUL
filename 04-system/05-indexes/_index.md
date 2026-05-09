# Índices canónicos del sistema /RAUL/

Esta carpeta contiene los índices SSOT del sistema, curados y estables.
Para artefactos machine-generated (logs, reportes de scans), ver `04-system/06-logs/`.

## Índices vigentes

- [`projects-index.md`](projects-index.md) — proyectos activos por dominio + estado.
- [`domains-index.md`](domains-index.md) — dominios activos del sistema.
- [`kb-index-by-domain.md`](kb-index-by-domain.md) — inventario de KB por dominio.
- [`research-index.md`](research-index.md) — líneas de investigación abiertas.
- [`companion-docs-index.md`](companion-docs-index.md) — companion docs (sufijo PERPLEXITY).

## Política

- Los índices son SSOT — la realidad del repo debe reflejarlos y vice-versa.
- Cada índice define su cadencia de actualización en su propio header/frontmatter.
- Cambios estructurales que afectan a un índice se registran en `04-system/03-governance/DECISIONS.md`.
- Si emergen índices auto-generados o drafts en el futuro, considerar subdivisión (ej. `canonical/`, `generated/`). Por ahora, todos los archivos aquí son canónicos curados.

## Helper Python

Scripts Tier 1 acceden a esta ruta via `paths.INDEXES_DIR` del helper `04-system/04-tools-and-scripts/raul_paths.py`. Ver `04-system/01-config/SCRIPTS-DEPENDENCIES.md` para detalles.
