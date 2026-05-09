# Logs y reportes runtime del sistema /RAUL/

Esta carpeta contiene artefactos machine-generated por scripts del sistema.
Para índices canónicos curados, ver `04-system/05-indexes/`.

Creado en separación física `05-indexes/` ↔ `06-logs/` (decisión 6 de SCRIPTS-DEPENDENCIES.md, ejecutada 2026-05-09).

## Tipos de archivo

| Patrón | Generador | Tracked en git? | Naturaleza |
|---|---|---|---|
| `*.log` | `fase4_kb_formatter`, `pendrive_pipeline` (timestamped) | NO (gitignored vía `*.log` global) | Logs accumulativos por run |
| `pendrive_pipeline_stdout.txt` | redirect manual | NO (gitignored explícito) | stdout dump |
| `fase4_progress.json` | `fase4_kb_formatter` | NO (gitignored explícito) | State file (overwrites) |
| `pendrive_D_inventory.json` | `pendrive_pipeline` | YES | Inventario actual del pendrive D |
| `pendrive_D_report.md` | `pendrive_pipeline` | YES | Reporte legible del pendrive D |
| `pendrive_D_assets_catalog.json` | `pendrive_pipeline` | YES | Catálogo machine-readable de assets |
| `pendrive_D_assets_catalog.md` | `pendrive_pipeline` | YES | Catálogo legible de assets |

## Política

- Los `.log` de runs antiguos pueden eliminarse libremente — son transient.
- Los `pendrive_D_*` reflejan el contenido actual del pendrive D. Cambios los reflejan ediciones del medio físico; commit cuando vale documentar nuevo estado.
- Si un `pendrive_D_*` se vuelve obsoleto (no hay pendrive D conectable o cambia de medio), archivar en `05-archive/`.

## Helper Python

Scripts Tier 1 acceden a esta ruta via `paths.LOGS_DIR` del helper `04-system/04-tools-and-scripts/raul_paths.py`. Ver `04-system/01-config/SCRIPTS-DEPENDENCIES.md` para detalles.
