"""Fix aspect ratio 4:3 -> 16:9 en scripts V8.2 -> V8.3.
- Cambia slide_width 10 -> 13.333 (16:9)
- Cambia Inches(10) full-width refs -> Inches(13.333)
- Escala invocaciones make_chart_* por factor 1.3333 en width (left queda igual)
- Output: build_deck_v8.3.py + build_resumen_ejecutivo_v8.3.py + PPTX nuevos
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import re
import os

V8_DIR = r"C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\03-deck\V8"
SCALE = 13.333 / 10  # 1.3333

def fix_script(src_path, dst_path):
    print(f"\nProcesando: {src_path}")
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    n_changes = 0

    # 1. Cambiar slide_width assignment
    new_content, n = re.subn(
        r'prs\.slide_width\s*=\s*Inches\(10\)',
        'prs.slide_width  = Inches(13.333)',
        content
    )
    n_changes += n
    print(f"  - slide_width Inches(10) -> Inches(13.333): {n} cambios")

    # 2. Cambiar TODOS los Inches(10) restantes (backgrounds, stripes full-width)
    new_content, n = re.subn(
        r'Inches\(10\)',
        'Inches(13.333)',
        new_content
    )
    n_changes += n
    print(f"  - Inches(10) full-width -> Inches(13.333): {n} cambios")

    # 3. Escalar widths de invocaciones make_chart_*
    def scale_width(match):
        full = match.group(0)
        w_str = match.group(1)
        try:
            w_old = float(w_str)
            w_new = round(w_old * SCALE, 2)
            return full.replace(f"width={w_str}", f"width={w_new}")
        except ValueError:
            return full

    new_content, n = re.subn(
        r'make_chart_c\d+\([^)]*width=(\d+\.?\d*)[^)]*\)',
        scale_width,
        new_content
    )
    print(f"  - make_chart_* width escalado x{SCALE:.4f}: {n} cambios")
    n_changes += n

    # 4. Escalar left de invocaciones make_chart_* opcionalmente (centrar)
    # Si left era pequeño (<1) lo mantengo, si era >=1 lo escalo
    def scale_left(match):
        full = match.group(0)
        l_str = match.group(1)
        try:
            l_old = float(l_str)
            if l_old < 1.0:
                # Margen pequeño, mantener
                return full
            l_new = round(l_old * SCALE, 2)
            return full.replace(f"left={l_str}", f"left={l_new}")
        except ValueError:
            return full

    new_content, n = re.subn(
        r'make_chart_c\d+\([^)]*left=(\d+\.?\d*)[^)]*\)',
        scale_left,
        new_content
    )
    print(f"  - make_chart_* left ajustado: {n} cambios")
    n_changes += n

    # 5. Cambiar referencia al output filename V8.2 -> V8.3
    new_content = new_content.replace('V8.2.pptx', 'V8.3.pptx')
    new_content = new_content.replace('V8.2_Resumen', 'V8.3_Resumen')

    # 6. Banner en docstring
    if 'V8.3' not in new_content[:300]:
        new_content = new_content.replace('V8.2', 'V8.3', 1)

    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"  Output escrito: {dst_path}")
    print(f"  Total cambios: {n_changes}")
    return n_changes

def main():
    pairs = [
        ('build_deck_v8.2.py', 'build_deck_v8.3.py'),
        ('build_resumen_ejecutivo_v8.2.py', 'build_resumen_ejecutivo_v8.3.py'),
    ]
    total = 0
    for src, dst in pairs:
        src_full = os.path.join(V8_DIR, src)
        dst_full = os.path.join(V8_DIR, dst)
        n = fix_script(src_full, dst_full)
        total += n
    print(f"\n{'='*60}")
    print(f"TOTAL cambios aplicados: {total}")
    print(f"Scripts V8.3 listos para ejecutar.")
    print(f"Aspect ratio: 10x7.5 (4:3) -> 13.333x7.5 (16:9)")

if __name__ == '__main__':
    main()
