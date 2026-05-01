# TOOLS-REQUIREMENTS.md
## Herramientas externas requeridas por el sistema /RAUL/

**Versión:** 1.0
**Última actualización:** 2026-05-01
**Propósito:** inventario de herramientas CLI y librerías Python necesarias para operar los scripts del sistema. Consultar antes de instalar algo nuevo — puede que ya esté disponible.

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
| `python-pptx` | instalada | `pip install python-pptx` | `gen_gst_r_pptx_v2.py`, Vivienne |
| `python-docx` | instalada | `pip install python-docx` | Celeste, scripts de intake |
| `reportlab` | instalada | `pip install reportlab` | Generación PDF alternativa |
| `Pillow` | instalada | `pip install Pillow` | Procesamiento de imágenes |
| `pytesseract` | instalada (con Tesseract 5.4.0) | `pip install pytesseract` | OCR — Celeste Lote C |

---

## Scripts activos y sus dependencias

| Script | Ruta | Dependencias | Propósito |
|---|---|---|---|
| `gsm_empaque_redlines_v4.py` | `04-tools-and-scripts/` | PyMuPDF | Redlines PDF anotados empaque GSM — tiro y retiro |
| `fase4_kb_formatter.py` | `04-tools-and-scripts/` | (verificar) | Formatter de KB para fase 4 |
| `pendrive_pipeline.py` | `04-tools-and-scripts/` | (verificar) | Pipeline de inventario pendrive D |
| `gen_gst_r_pptx_v2.py` | `03-projects/genteca/2026-04_GST-R_etiquetas/02-production/` | python-pptx | Brief PPTX etiquetas GST-R |
| `descargar_genteca_v2.py` | `04-tools-and-scripts/scripts/` | requests (verificar) | Descarga masiva PDFs genteca.com.ve |
| `celeste_screening_loteC.py` | `04-tools-and-scripts/scripts/` | PyMuPDF, pytesseract | Pre-screening + OCR Lote C KB |
| `ocr_stubs.py` | `04-tools-and-scripts/scripts/` | pytesseract, Pillow | OCR de imágenes para stubs KB |

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
