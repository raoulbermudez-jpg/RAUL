# Scripts legacy movidos — 2026-05-08

Cuatro scripts de esta carpeta fueron archivados a `05-archive/03-system-history/legacy-scripts/`:

- `descargar_genteca.py`
- `descargar_genteca_v2.py`
- `celeste_screening_loteC.py`
- `ocr_stubs.py`

**Razón:** paths hardcoded a `WorkspaceIA` (era pre-/RAUL/). Decisión #2 documentada en [SCRIPTS-DEPENDENCIES.md](../../01-config/SCRIPTS-DEPENDENCIES.md) sección Tier 3.

**NO restaurar.** Si necesitás funcionalidad equivalente, partir de cero usando `RAUL_ROOT` y el helper `_lib/raul_paths.py` (planificado en Paso 3d).

Ver [_index.md](../../../05-archive/03-system-history/legacy-scripts/_index.md) en el archivo para inventario completo.
