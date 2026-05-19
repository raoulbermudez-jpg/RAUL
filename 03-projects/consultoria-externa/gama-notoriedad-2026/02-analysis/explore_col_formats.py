"""Explora los patrones de formato de columna en BBDD."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd
import re
from collections import Counter

BBDD = r"G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\BBDD Notoriedad 2026.xlsx"
df = pd.read_excel(BBDD)

print(f"Total columnas: {len(df.columns)}\n")

# Clasificar formatos
formatos = Counter()
for col in df.columns:
    s = str(col).strip()
    if s.startswith('{'):
        formatos['{Pxx} format'] += 1
    elif re.match(r'^P[FD]?\d', s):
        formatos['Pxx direct'] += 1
    elif re.match(r'^V\d+', s):
        formatos['Vxxx only'] += 1
    elif re.match(r'^\w', s):
        formatos['other word'] += 1
    else:
        formatos['weird'] += 1

print("Formatos detectados:")
for f, n in formatos.most_common():
    print(f"  {f}: {n}")

print("\n\nMuestra primeras 30 columnas:")
for i, col in enumerate(df.columns[:30]):
    print(f"  [{i:3d}] {col[:90]}")

print("\n\nMuestra columnas 30-60:")
for i, col in enumerate(df.columns[30:60]):
    print(f"  [{i+30:3d}] {col[:90]}")

print("\n\nMuestra columnas 60-90:")
for i, col in enumerate(df.columns[60:90]):
    print(f"  [{i+60:3d}] {col[:90]}")
