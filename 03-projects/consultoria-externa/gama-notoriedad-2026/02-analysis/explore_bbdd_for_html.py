"""Exploracion BBDD 2026 para construir el HTML de tablas cruzadas.
- Lista columnas, identifica BKs y preguntas
- Para cada BK reporta valores unicos
- Mapea cuestionario (guia_preguntas) a columnas BBDD
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd
import re
import json
from collections import Counter

BBDD = r"G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\BBDD Notoriedad 2026.xlsx"

df = pd.read_excel(BBDD)
print(f"BBDD: n={len(df)} filas x {len(df.columns)} columnas")
print()

# ===== BREAK-DOWNS (BKs) =====
print("="*80)
print("EXPLORACION DE BREAK-DOWNS (BKs)")
print("="*80)

BK_PATTERNS = {
    'NSE':              [r'\bPD4\b', r'\bNSE\b'],
    'Genero':           [r'\bPF5\b', r'\bsexo\b', r'\bgenero\b'],
    'Edad (grupos)':    [r'\bPF7\b', r'grupo.*edad', r'edad.*grupo'],
    'Edad (raw)':       [r'\bPF6\b', r'^edad$'],
    'Municipio':        [r'\bPF2.*municip', r'^municip', r'\bmunicipio\b'],
    'Marca preferida':  [r'\bP21\b(?!\.1)', r'P21$'],
    'Mision (P25)':     [r'\bP25\b'],
    'Mision (P26)':     [r'\bP26\b'],
}

bks_found = {}
for bk_name, patterns in BK_PATTERNS.items():
    print(f"\n[{bk_name}]")
    for col in df.columns:
        s = str(col).strip()
        for p in patterns:
            if re.search(p, s, re.I):
                vals = df[col].dropna()
                unique_vals = vals.value_counts().head(10)
                print(f"  Col: '{s[:60]}'")
                print(f"    Tipo: {vals.dtype}, n_valid: {len(vals)}, n_unique: {vals.nunique()}")
                print(f"    Top valores: {dict(unique_vals)}")
                bks_found[bk_name] = {'col': s, 'unique_vals': dict(unique_vals)}
                break

# ===== PREGUNTAS DEL CUESTIONARIO =====
print("\n" + "="*80)
print("PREGUNTAS Pxx EN BBDD (codigos de columna que empiezan con P o PF)")
print("="*80)

# Agrupar columnas por prefijo de pregunta
question_groups = {}
for col in df.columns:
    s = str(col).strip()
    # Match: P16, PF5, P21.1, PD4, etc.
    m = re.match(r'^(P[FD]?\d+(?:\.\d+)?)', s)
    if m:
        prefix = m.group(1)
        question_groups.setdefault(prefix, []).append(s)

print(f"\nTotal preguntas/codigos detectados: {len(question_groups)}")
print(f"\nDistribucion por codigo (top 50, ordenados):")
sorted_qs = sorted(question_groups.items(), key=lambda x: (x[0][0:2], int(re.findall(r'\d+', x[0])[0])))
for q, cols in sorted_qs[:50]:
    n = len(cols)
    sample = cols[0][:70] if cols else '(vacio)'
    print(f"  {q:10s} ({n} col{'s' if n>1 else ''}): {sample}")

print(f"\nResto: {len(sorted_qs) - 50} codigos mas")

# ===== EXPORT JSON =====
out = {
    'meta': {
        'n_rows': len(df),
        'n_cols': len(df.columns),
        'fecha': '2026-05-18',
    },
    'bks_detected': bks_found,
    'questions_detected': {q: [c for c in cols] for q, cols in sorted_qs},
}
out_path = r"C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis\bbdd_exploration.json"
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2, default=str)
print(f"\nJSON exportado: {out_path}")
