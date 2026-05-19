# TOOLS-REQUIREMENTS.md
## Herramientas CORE requeridas por el sistema /RAUL/

**Versión:** 1.1
**Última actualización:** 2026-05-18
**Propósito:** inventario de herramientas CLI y librerías Python necesarias para operar los scripts del sistema. Consultar antes de instalar algo nuevo — puede que ya esté disponible.

> **Nota de scope (desde 2026-05-18):** este archivo lista **solo tools CORE** — open-source, requeridas para que el sistema funcione en cualquier clon del repo. Las tools **Owner-selected** (paid / account-based, sustituibles: Claude Code CLI, Anthropic API, claude.ai MCPs, Canva Pro, Google Drive personal, OneDrive backup, etc.) viven en `TOOLS-OWNER-SELECTED.md` como información para clonadores. El split formaliza el principio vendor-neutral del norte arquitectónico §0. Ver `04-system/03-governance/2026-05-18_tools-split-policy_canva-pro-adoption.md`.

---

## Entorno base

| Herramienta | Versión confirmada | Verificar con |
|---|---|---|
| Python | 3.14.4 (disponible como `python`, NO `python3`) | `python --version` |
| pip | incluido en Python 3.14 | `pip --version` |
| Git | instalado | `git --version` |
| Pandoc | instalado | `pandoc --version` |

**Nota Windows:** En esta máquina, el intérprete es `python`, no `python3`. Scripts y comandos deben usar `python`.

---

## Librerías Python instaladas

| Librería | Versión confirmada | Instalación | Usada por |
|---|---|---|---|
| `PyMuPDF` (fitz) | 1.27.2.2 | `pip install pymupdf` | `gsm_empaque_redlines_v4.py`, agente Oz |
| `anthropic` | instalada | `pip install anthropic` | Scripts de integración API |
| `python-pptx` | instalada | `pip install python-pptx` | Vivienne, scripts de build PPTX en proyectos genteca |
| `python-docx` | instalada | `pip install python-docx` | Celeste, scripts de intake |
| `reportlab` | instalada | `pip install reportlab` | Generación PDF alternativa |
| `Pillow` | instalada | `pip install Pillow` | Procesamiento de imágenes |
| `pytesseract` | instalada (con Tesseract 5.4.0) | `pip install pytesseract` | OCR — Celeste Lote C |

---

## Scripts activos y sus dependencias

| Script | Ruta | Dependencias | Propósito |
|---|---|---|---|
| `gsm_empaque_redlines_v4.py` | `03-projects/genteca/2026-04_GSM-MB-RB-RF_empaque/03-review-and-release/` | PyMuPDF | Redlines PDF anotados empaque GSM — tiro y retiro |
| `fase4_kb_formatter.py` | `04-tools-and-scripts/` | (verificar) | Formatter de KB para fase 4 |
| `pendrive_pipeline.py` | `04-tools-and-scripts/` | (verificar) | Pipeline de inventario pendrive D |
| `raul_paths.py` | `04-tools-and-scripts/` | (stdlib) | Helper canónico de paths via RAUL_ROOT; también runnable como self-test |

**Scripts archivados:** ver `05-archive/03-system-history/legacy-scripts/_index.md` (Tier 3 abandonados en commit 52d7e9b: `descargar_genteca`, `descargar_genteca_v2`, `celeste_screening_loteC`, `ocr_stubs`, `gen_gst_r_pdf_v2`, `gen_gst_r_pptx_v2`).

---

## Encoding en Windows

Scripts Python que imprimen caracteres no-ASCII (acentos, ñ, símbolos técnicos) deben incluir al inicio:

```python
import sys
sys.stdout.reconfigure(encoding='utf-8')
```

Sin esta línea, Python en Windows usa cp1252 y falla al imprimir cualquier carácter fuera del ASCII básico. Error típico: `UnicodeEncodeError: 'charmap' codec can't encode character`.

---

## Notas de instalación

- **Tesseract OCR**: instalado a nivel sistema (no pip). Verificar disponibilidad con `tesseract --version`. Requerido por `pytesseract`.
- **Pandoc**: instalado a nivel sistema. Verificar con `pandoc --version`. Usado para conversiones MD ↔ DOCX cuando Celeste lo necesita.
- **Pillow vs PIL**: usar siempre `Pillow` (no `PIL`). `from PIL import Image` es la sintaxis correcta con Pillow instalado.

---

## Cómo actualizar este archivo

Cada vez que se instale una nueva librería o herramienta para un script del sistema:
1. Agregar fila en la tabla de librerías
2. Agregar fila en la tabla de scripts si hay un script nuevo
3. Anotar la versión si es relevante (especialmente para PyMuPDF — sus APIs cambian entre versiones)
