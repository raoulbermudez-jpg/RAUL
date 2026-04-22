"""
OCR processing script for FLAG stubs — Celeste KB Lote C
Processes 22 image-only PDF stubs and replaces them with full Markdown text.
"""

import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import os
import re
from datetime import datetime

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

KB_PATH = r"c:\WorkspaceIA\PROJECTS\Claude code\Knowledge Base\Technical"
RAG_PATH = r"G:\Mi unidad\WorkspaceIA\RAG_SOURCES"

# Map: (stub_filename, pdf_source_path)
STUB_MAP = [
    # Priority 1: Genius Catalog (largest/most critical)
    (
        "2026-04-18_catalogo_generales-catalogo-genius.md",
        os.path.join(RAG_PATH, "09_Catalogos_Generales_catalogo-genius.pdf"),
    ),
    # Hojas de especificaciones — Agua
    (
        "2026-04-18_hoja-especificaciones_agua-e-gfe-mv.md",
        os.path.join(RAG_PATH, "06_Manejo_Agua_E_GFE-MV.pdf"),
    ),
    (
        "2026-04-18_hoja-especificaciones_agua-gbs-la-750-hde-v2-c.md",
        os.path.join(RAG_PATH, "06_Manejo_Agua_GBS-LA-750_HDE_V2_C.pdf"),
    ),
    (
        "2026-04-18_hoja-especificaciones_agua-gfa-pp-filtro-de-agua-con-cartucho-de-polipropileno.md",
        os.path.join(RAG_PATH, "06_Manejo_Agua_GFA-PP-Filtro-de-Agua-con-Cartucho-de-Polipropileno.pdf"),
    ),
    (
        "2026-04-18_hoja-especificaciones_agua-gvf-hi-100-200-flotante-mecanico.md",
        os.path.join(RAG_PATH, "06_Manejo_Agua_GVF-HI-100-200-Flotante-mecanico.pdf"),
    ),
    # Hojas de especificaciones — Tecnica
    (
        "2026-04-18_hoja-especificaciones_tecnica-e-gfe-mv.md",
        os.path.join(RAG_PATH, "11_Biblioteca_Tecnica_E_GFE-MV.pdf"),
    ),
    (
        "2026-04-18_hoja-especificaciones_tecnica-gsm-tg-hde-v1-c.md",
        os.path.join(RAG_PATH, "11_Biblioteca_Tecnica_GSM-TG_HDE_V1_C.pdf"),
    ),
    # Hoja especificaciones — Trifasica
    (
        "2026-04-18_hoja-especificaciones_trifasica-u-giotool.md",
        os.path.join(RAG_PATH, "04_Proteccion_Trifasica_U_GIOTOOL.pdf"),
    ),
    # Manuales
    (
        "2026-04-18_manual_tecnica-i-giii-p.md",
        os.path.join(RAG_PATH, "11_Biblioteca_Tecnica_I_GIII_P.pdf"),
    ),
    (
        "2026-04-18_manual_tecnica-i-gspt-mv.md",
        os.path.join(RAG_PATH, "11_Biblioteca_Tecnica_I_GSPT-MV.pdf"),
    ),
    (
        "2026-04-18_manual_tecnica-i-gspt.md",
        os.path.join(RAG_PATH, "11_Biblioteca_Tecnica_I_GSPT.pdf"),
    ),
    # Notas de aplicacion
    (
        "2026-04-18_nota-aplicacion_tecnica-arg-gst-rc.md",
        os.path.join(RAG_PATH, "11_Biblioteca_Tecnica_arg_GST-RC.pdf"),
    ),
    (
        "2026-04-18_nota-aplicacion_tecnica-computadoras.md",
        os.path.join(RAG_PATH, "11_Biblioteca_Tecnica_COMPUTADORAS.pdf"),
    ),
    (
        "2026-04-18_nota-aplicacion_tecnica-flotante.md",
        os.path.join(RAG_PATH, "11_Biblioteca_Tecnica_FLOTANTE.pdf"),
    ),
    (
        "2026-04-18_nota-aplicacion_tecnica-g-goct-1.md",
        os.path.join(RAG_PATH, "11_Biblioteca_Tecnica_G_GOCT_1.pdf"),
    ),
    (
        "2026-04-18_nota-aplicacion_tecnica-hidroneumatico-racionamiento-v1-rev-mf.md",
        os.path.join(RAG_PATH, "11_Biblioteca_Tecnica_Hidroneumatico-Racionamiento-V1-REV-MF.pdf"),
    ),
    (
        "2026-04-18_nota-aplicacion_tecnica-na-giii-p-2.md",
        os.path.join(RAG_PATH, "11_Biblioteca_Tecnica_NA_GIII_P_2.pdf"),
    ),
    (
        "2026-04-18_nota-aplicacion_tecnica-na-goct-1.md",
        os.path.join(RAG_PATH, "11_Biblioteca_Tecnica_NA_GOCT_1.pdf"),
    ),
    (
        "2026-04-18_nota-aplicacion_tecnica-r-gtc-o-mr.md",
        os.path.join(RAG_PATH, "11_Biblioteca_Tecnica_R_GTC_O-MR.pdf"),
    ),
    (
        "2026-04-18_nota-aplicacion_tecnica-sistema-aire-acondicionado-goc-t-y-gtp-a.md",
        os.path.join(RAG_PATH, "11_Biblioteca_Tecnica_Sistema-Aire-Acondicionado-GOC-T-y-GTP-A.pdf"),
    ),
    # Documentos tecnicos
    (
        "2026-04-18_otro_instructivos-s-cp001.md",
        os.path.join(RAG_PATH, "10_FAQ_Instructivos_S_CP001.pdf"),
    ),
    (
        "2026-04-18_otro_tecnica-s-cp001.md",
        os.path.join(RAG_PATH, "11_Biblioteca_Tecnica_S_CP001.pdf"),
    ),
]


def ocr_pdf(pdf_path, lang='eng'):
    """Extract text from image-only PDF using OCR."""
    doc = fitz.open(pdf_path)
    full_text = []
    for page_num, page in enumerate(doc):
        mat = fitz.Matrix(2, 2)  # 2x zoom for better OCR quality
        pix = page.get_pixmap(matrix=mat)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        text = pytesseract.image_to_string(img, lang=lang)
        if text.strip():
            full_text.append(f"<!-- Page {page_num + 1} -->\n{text}")
    doc.close()
    return '\n\n'.join(full_text)


def clean_ocr_text(text):
    """Basic cleanup of OCR output."""
    # Remove excessive blank lines (more than 2 consecutive)
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    # Strip trailing whitespace per line
    lines = [line.rstrip() for line in text.split('\n')]
    return '\n'.join(lines)


def read_stub_title(stub_path):
    """Read the first non-empty heading from existing stub."""
    try:
        with open(stub_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('#'):
                    return line
    except Exception:
        pass
    return None


def process_stub(stub_filename, pdf_path):
    """Process one stub: OCR the PDF and write the full markdown."""
    stub_path = os.path.join(KB_PATH, stub_filename)

    # Read original stub to preserve its header
    original_title = read_stub_title(stub_path)

    if not os.path.exists(pdf_path):
        return {
            'file': stub_filename,
            'status': 'ERROR',
            'reason': f'Source PDF not found: {pdf_path}',
            'pages': 0,
            'chars': 0,
        }

    try:
        raw_text = ocr_pdf(pdf_path, lang='eng')
        cleaned = clean_ocr_text(raw_text)
        char_count = len(cleaned.strip())

        # Determine the document type from stub filename for header
        doc_date = "2026-04-18"
        source_pdf = os.path.basename(pdf_path)

        # Build the markdown content
        header = original_title if original_title else f"# Documento — {stub_filename}"
        # Remove the IMAGE-ONLY/FLAG note from the header if present
        header = header.replace(' (IMAGE-ONLY/FLAG)', '')

        content = f"""{header}

> **Fuente:** {source_pdf}
> **OCR procesado:** {doc_date} | Motor: Tesseract v5.4.0 (eng)
> **Estado:** Texto extraído por OCR — puede contener imprecisiones en caracteres especiales

---

{cleaned}
"""

        with open(stub_path, 'w', encoding='utf-8') as f:
            f.write(content)

        status = 'OK' if char_count > 200 else 'LOW'
        return {
            'file': stub_filename,
            'status': status,
            'reason': f'{char_count} chars extracted',
            'pages': raw_text.count('<!-- Page '),
            'chars': char_count,
        }

    except Exception as e:
        return {
            'file': stub_filename,
            'status': 'ERROR',
            'reason': str(e),
            'pages': 0,
            'chars': 0,
        }


def update_index(results):
    """Remove IMAGE-ONLY/FLAG from index entries for successfully processed files."""
    index_path = os.path.join(KB_PATH, '_index.md')
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    updated = content
    for r in results:
        if r['status'] in ('OK', 'LOW'):
            fname = r['file']
            # Replace the IMAGE-ONLY/FLAG marker in both doc type and description columns
            # Pattern matches the full row containing the filename
            # We'll do a targeted replacement on the document type column
            old_type_pattern = r'(IMAGE-ONLY/FLAG) '
            # For each row containing this file, remove IMAGE-ONLY/FLAG from type column
            # Use a line-by-line approach
            lines = updated.split('\n')
            new_lines = []
            for line in lines:
                if fname in line and 'IMAGE-ONLY/FLAG' in line:
                    # Remove IMAGE-ONLY/FLAG from the document type column
                    line = line.replace('(IMAGE-ONLY/FLAG) ', '')
                    line = line.replace('(IMAGE-ONLY/FLAG)', '')
                new_lines.append(line)
            updated = '\n'.join(new_lines)

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(updated)


def main():
    print(f"Starting OCR processing of {len(STUB_MAP)} stubs")
    print(f"Tesseract: {pytesseract.get_tesseract_version()}")
    print(f"Language: eng only (spa data not available)")
    print("=" * 60)

    results = []
    for stub_filename, pdf_path in STUB_MAP:
        print(f"Processing: {stub_filename[:60]}...", end=' ', flush=True)
        result = process_stub(stub_filename, pdf_path)
        results.append(result)
        print(f"[{result['status']}] {result['reason']}")

    print("\n" + "=" * 60)
    ok = [r for r in results if r['status'] == 'OK']
    low = [r for r in results if r['status'] == 'LOW']
    errors = [r for r in results if r['status'] == 'ERROR']

    print(f"OK (>200 chars): {len(ok)}")
    print(f"LOW (<200 chars): {len(low)}")
    print(f"ERRORS: {len(errors)}")

    if low:
        print("\nLOW quality:")
        for r in low:
            print(f"  - {r['file']}: {r['reason']}")
    if errors:
        print("\nERRORS:")
        for r in errors:
            print(f"  - {r['file']}: {r['reason']}")

    # Update index
    print("\nUpdating _index.md...")
    update_index(results)
    print("Index updated.")

    return results


if __name__ == '__main__':
    results = main()
