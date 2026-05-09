"""
render_B_v2.py
Atlas — Static Visual Production Lead — Sistema /RAUL/
2026-05-05

Propósito:
  Rasterizar Atlas_mockup_frente_B_v2.svg → Atlas_mockup_frente_B_v2.png (800x1200 px)
  Copiar PNG nuevo a Junta_PPTX_v2/ (sobreescribir Atlas_mockup_frente_B.png)
  Preservar PNG anterior como Atlas_mockup_frente_B_v1.png en Junta_PPTX_v2/

Dependencia: cairosvg
  pip install cairosvg
  (Si cairosvg no está disponible, instalar con GTK runtime en Windows — ver documentación cairosvg)

Ejecución:
  cd C:\\RAUL\\03-projects\\genteca\\2026-04_GSM-MB-RB-RF_empaque\\02-production\\Atlas_mockups_v1
  python render_B_v2.py
"""

import sys
import os
import shutil

sys.stdout.reconfigure(encoding='utf-8')

# ── Rutas ────────────────────────────────────────────────────────────────────
BASE_PROD   = r'C:\RAUL\03-projects\genteca\2026-04_GSM-MB-RB-RF_empaque\02-production\Atlas_mockups_v1'
PPTX_DIR    = r'C:\RAUL\03-projects\genteca\2026-04_GSM-MB-RB-RF_empaque\03-review-and-release\Junta_PPTX_v2'

SVG_IN      = os.path.join(BASE_PROD, 'Atlas_mockup_frente_B_v2.svg')
PNG_OUT     = os.path.join(BASE_PROD, 'Atlas_mockup_frente_B_v2.png')

PPTX_B_CURRENT  = os.path.join(PPTX_DIR, 'Atlas_mockup_frente_B.png')
PPTX_B_V1_COPY  = os.path.join(PPTX_DIR, 'Atlas_mockup_frente_B_v1.png')

# ── Paso 1: Preservar PNG v1 en Junta_PPTX_v2 ──────────────────────────────
if os.path.exists(PPTX_B_CURRENT) and not os.path.exists(PPTX_B_V1_COPY):
    shutil.copy2(PPTX_B_CURRENT, PPTX_B_V1_COPY)
    print(f'[OK] PNG v1 preservado → {PPTX_B_V1_COPY}')
elif os.path.exists(PPTX_B_V1_COPY):
    print(f'[INFO] PNG v1 ya existe en destino, se preserva sin sobreescribir: {PPTX_B_V1_COPY}')
else:
    print(f'[WARN] No se encontró PNG actual en {PPTX_B_CURRENT} — omitiendo preservación de v1.')

# ── Paso 2: Rasterizar SVG → PNG ────────────────────────────────────────────
try:
    import cairosvg
    cairosvg.svg2png(
        url=SVG_IN,
        write_to=PNG_OUT,
        output_width=800,
        output_height=1200,
    )
    print(f'[OK] PNG v2 generado → {PNG_OUT}')
except ImportError:
    print('[ERROR] cairosvg no está instalado.')
    print('        Instalar con: pip install cairosvg')
    print('        En Windows puede requerir GTK runtime — ver https://cairosvg.org/documentation/')
    sys.exit(1)

# ── Paso 3: Copiar PNG v2 a Junta_PPTX_v2 ───────────────────────────────────
shutil.copy2(PNG_OUT, PPTX_B_CURRENT)
print(f'[OK] PNG v2 copiado a Junta_PPTX_v2 → {PPTX_B_CURRENT}')

print()
print('render_B_v2.py completado sin errores.')
print(f'  SVG fuente : {SVG_IN}')
print(f'  PNG v2     : {PNG_OUT}')
print(f'  PPTX dir   : {PPTX_B_CURRENT}')
print(f'  Backup v1  : {PPTX_B_V1_COPY}')
