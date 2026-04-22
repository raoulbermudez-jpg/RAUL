"""
Celeste — Pre-screening diagnóstico Lote C
Analiza todos los PDFs en la raíz de RAG_SOURCES (sin subcarpetas)
"""

import os
import re
import fitz  # PyMuPDF
from pathlib import Path
from datetime import date

RAG_ROOT = Path("G:/Mi unidad/WorkspaceIA/RAG_SOURCES")
OUTPUT_PATH = Path("c:/WorkspaceIA/PROJECTS/Claude code/Owner Inbox/2026-04-18-celeste-lote-C-screening.md")

ALREADY_IN_KB = {
    "I_GSPT.pdf",
    "E_GST-RC.pdf",
    "GSM-N-Protector-Neveras.pdf",
    "10-GD-NA-Hidroneumatico-2-bombas.pdf",
    "catalogo-genius.pdf",
    "E_GFR-MV7H.pdf",
    "E_GSM-AS.pdf",
    "E_GSM-RB-AltaCarga.pdf",
    "GSM-NG_HDE_V2.pdf",
    "GSM-RE-Protector-AA.pdf",
    "GTC-B1C-MV-Programador.pdf",
    "GTC-B1L-MV-Programador.pdf",
    "C_003.pdf",
    "GRA-MV_HDE_V7.pdf",
    "GSC-MB-Sobrecarga-Trifasico.pdf",
    "GTC-MR_HDE_V6.pdf",
    "I_GMS-U.pdf",
    "01-GD-NA-Alternancia-3-cargas-v2.pdf",
    "NA-003-Sistemas-Iluminacion.pdf",
    "CAT_TRI_1_IMP.pdf",
    "CAT_BRE_1.pdf",
    "catalogo-comercial-exceline.pdf",
    "catalogo-control-y-distribucion.pdf",
}

def classify_type(filename):
    """Estimate document type from filename prefix."""
    name = filename.upper()
    if name.startswith("I_"):
        return "Manual"
    elif name.startswith("E_"):
        return "Spec/HDE"
    elif name.startswith("G_"):
        return "Imagen/Foto"
    elif name.startswith("GD-NA") or re.match(r"^\d+-GD-NA", name) or name.startswith("NA-"):
        return "Nota-Aplicacion"
    elif name.startswith("CAT"):
        return "Catalogo"
    elif name.startswith("C_"):
        return "Cert/Otro"
    elif name.startswith("GD-"):
        return "Doc-Genius"
    else:
        return "Otro"

def is_duplicate_probable(filename):
    """Check if filename matches (exact or close) something already in KB."""
    if filename in ALREADY_IN_KB:
        return True
    # Fuzzy: strip extension, lowercase, check if stem matches any KB stem
    stem = Path(filename).stem.lower().replace("-", "").replace("_", "")
    for kb_file in ALREADY_IN_KB:
        kb_stem = Path(kb_file).stem.lower().replace("-", "").replace("_", "")
        if stem == kb_stem:
            return True
        # Very similar: one contains the other (min 6 chars)
        if len(stem) >= 6 and len(kb_stem) >= 6:
            if stem in kb_stem or kb_stem in stem:
                return True
    return False

def analyze_pdf(pdf_path):
    """Analyze a single PDF. Returns dict with all columns."""
    filename = pdf_path.name
    size_kb = round(pdf_path.stat().st_size / 1024, 1)
    doc_type = classify_type(filename)
    dup = is_duplicate_probable(filename)

    result = {
        "filename": filename,
        "pages": 0,
        "pct_text": 0,
        "size_kb": size_kb,
        "tipo": doc_type,
        "estado": "",
        "notas": "",
    }

    if dup:
        result["estado"] = "duplicado-probable"

    try:
        doc = fitz.open(str(pdf_path))
        page_count = len(doc)
        result["pages"] = page_count

        if page_count == 0:
            result["estado"] = "corrupto"
            doc.close()
            return result

        pages_with_text = 0
        for page in doc:
            text = page.get_text("text")
            if len(text.strip()) > 50:
                pages_with_text += 1

        doc.close()

        pct = round(pages_with_text / page_count * 100)
        result["pct_text"] = pct

        if not dup:  # don't overwrite duplicado-probable
            if pct == 0:
                result["estado"] = "solo-imagen"
            elif pct >= 50:
                result["estado"] = "texto"
            else:
                result["estado"] = "mixto"

    except Exception as e:
        result["estado"] = "corrupto"
        result["notas"] = str(e)[:80]

    return result

def main():
    # Collect only files (no subdirs) with .pdf extension
    pdf_files = sorted(
        [f for f in RAG_ROOT.iterdir() if f.is_file() and f.suffix.lower() == ".pdf"]
    )

    print(f"Analizando {len(pdf_files)} PDFs...")
    rows = []
    for i, pdf_path in enumerate(pdf_files, 1):
        if i % 20 == 0:
            print(f"  {i}/{len(pdf_files)}...")
        row = analyze_pdf(pdf_path)
        rows.append(row)

    # Counters
    counts = {"texto": 0, "solo-imagen": 0, "corrupto": 0, "duplicado-probable": 0, "mixto": 0}
    for r in rows:
        estado = r["estado"]
        if estado in counts:
            counts[estado] += 1

    # Build markdown output
    lines = []
    lines.append(f"# Celeste — Pre-screening Diagnóstico Lote C")
    lines.append(f"**Fecha:** {date.today()}")
    lines.append(f"**Carpeta escaneada:** `G:/Mi unidad/WorkspaceIA/RAG_SOURCES/` (solo raíz)")
    lines.append(f"**Total archivos analizados:** {len(rows)}")
    lines.append("")

    # Summary first
    lines.append("## Resumen por estado")
    lines.append("")
    lines.append("| Estado | Cantidad |")
    lines.append("|--------|----------|")
    lines.append(f"| Texto (>=50% páginas extraíbles) | {counts['texto']} |")
    lines.append(f"| Mixto (1-49% páginas extraíbles) | {counts['mixto']} |")
    lines.append(f"| Solo-imagen (0% texto) | {counts['solo-imagen']} |")
    lines.append(f"| Duplicado-probable | {counts['duplicado-probable']} |")
    lines.append(f"| Corrupto / error | {counts['corrupto']} |")
    lines.append(f"| **TOTAL** | **{len(rows)}** |")
    lines.append("")

    # Type breakdown
    type_counts = {}
    for r in rows:
        t = r["tipo"]
        type_counts[t] = type_counts.get(t, 0) + 1

    lines.append("## Resumen por tipo estimado")
    lines.append("")
    lines.append("| Tipo | Cantidad |")
    lines.append("|------|----------|")
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        lines.append(f"| {t} | {c} |")
    lines.append("")

    # Full table
    lines.append("## Tabla completa")
    lines.append("")
    lines.append("| # | Nombre de archivo | Págs | % Texto | Tamaño KB | Tipo estimado | Estado |")
    lines.append("|---|-------------------|------|---------|-----------|---------------|--------|")

    for i, r in enumerate(rows, 1):
        notes = f" _{r['notas']}_" if r["notas"] else ""
        lines.append(
            f"| {i} | `{r['filename']}` | {r['pages']} | {r['pct_text']}% | {r['size_kb']} | {r['tipo']} | {r['estado']}{notes} |"
        )

    lines.append("")

    # Processing order recommendation
    lines.append("## Recomendación de orden de procesamiento")
    lines.append("")
    lines.append("### Prioridad 1 — Texto limpio, no duplicados")
    lines.append("Procesar primero: documentos con estado `texto` o `mixto`, ordenados por tipo.")
    lines.append("")

    prio1 = [r for r in rows if r["estado"] in ("texto", "mixto")]
    # Sort: manuals first, then specs, then notas, then catalogos, then otros
    type_order = {"Manual": 0, "Spec/HDE": 1, "Nota-Aplicacion": 2, "Catalogo": 3, "Doc-Genius": 4, "Cert/Otro": 5, "Otro": 6, "Imagen/Foto": 7}
    prio1_sorted = sorted(prio1, key=lambda r: type_order.get(r["tipo"], 99))

    lines.append(f"Total: {len(prio1_sorted)} archivos listos para procesamiento.")
    lines.append("")
    lines.append("| Tipo | Archivo | Págs | % Texto |")
    lines.append("|------|---------|------|---------|")
    for r in prio1_sorted:
        lines.append(f"| {r['tipo']} | `{r['filename']}` | {r['pages']} | {r['pct_text']}% |")

    lines.append("")
    lines.append("### Prioridad 2 — Solo-imagen (requieren OCR)")
    solo_img = [r for r in rows if r["estado"] == "solo-imagen"]
    lines.append(f"Total: {len(solo_img)} archivos. Requieren OCR (tesseract + pytesseract o similar) antes de convertir a Markdown.")
    lines.append("")
    if solo_img:
        lines.append("| Archivo | Págs | Tamaño KB | Tipo |")
        lines.append("|---------|------|-----------|------|")
        for r in solo_img:
            lines.append(f"| `{r['filename']}` | {r['pages']} | {r['size_kb']} | {r['tipo']} |")
        lines.append("")

    lines.append("### Prioridad 3 — Duplicados probables (revisar manualmente)")
    dups = [r for r in rows if r["estado"] == "duplicado-probable"]
    lines.append(f"Total: {len(dups)} archivos. Confirmar si son versiones actualizadas o copias exactas antes de procesar.")
    lines.append("")
    if dups:
        lines.append("| Archivo | Págs | Tamaño KB | Tipo |")
        lines.append("|---------|------|-----------|------|")
        for r in dups:
            lines.append(f"| `{r['filename']}` | {r['pages']} | {r['size_kb']} | {r['tipo']} |")
        lines.append("")

    lines.append("### Prioridad 4 — Corruptos (escalar a Raul)")
    corruptos = [r for r in rows if r["estado"] == "corrupto"]
    lines.append(f"Total: {len(corruptos)} archivos. No se pueden procesar sin intervención.")
    lines.append("")
    if corruptos:
        lines.append("| Archivo | Error |")
        lines.append("|---------|-------|")
        for r in corruptos:
            lines.append(f"| `{r['filename']}` | {r['notas'] or 'Sin páginas'} |")
        lines.append("")

    lines.append("---")
    lines.append("_Reporte generado por Celeste — Knowledge Base Librarian_")

    output_text = "\n".join(lines)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(output_text, encoding="utf-8")
    print(f"\nReporte guardado en: {OUTPUT_PATH}")

    # Print summary to console
    print(f"\nRESUMEN:")
    for k, v in counts.items():
        print(f"  {k}: {v}")
    print(f"  Total: {len(rows)}")

if __name__ == "__main__":
    main()
