"""Extrae imágenes de los 3 docx en carpetas img_<app>/."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
import zipfile, shutil

BASE = Path(r'C:\RAUL\03-projects\genteca\2025-04_GME_estudios-mercado')
files = {
    'R': 'R-pantallas para consulta.docx',
    'B': 'B-pantallas para consulta.docx',
    'M': 'M-pantallas para consulta.docx',
}

for app, fname in files.items():
    out = BASE / f'_img_{app}'
    if out.exists():
        shutil.rmtree(out)
    out.mkdir()
    p = BASE / fname
    with zipfile.ZipFile(p, 'r') as z:
        names = [n for n in z.namelist() if n.startswith('word/media/')]
        names.sort()
        for n in names:
            data = z.read(n)
            target = out / Path(n).name
            target.write_bytes(data)
            print(f'  {app}/{target.name}: {len(data)} bytes')
    print(f'{app} -> {len(names)} imágenes en {out}')
    print()
