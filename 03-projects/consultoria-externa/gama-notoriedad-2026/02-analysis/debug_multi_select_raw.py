"""Investiga formato REAL de columnas multi-select en BBDD."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd

BBDD = r"G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\BBDD Notoriedad 2026.xlsx"
df = pd.read_excel(BBDD)

# Buscar cols P16 (TOM)
p16_cols = [c for c in df.columns if str(c).strip().startswith('{P16}')]
print(f"P16 cols: {len(p16_cols)}")

for col in p16_cols[:5]:
    print(f"\n--- {col[:80]} ---")
    vc = df[col].value_counts(dropna=False).head(10)
    print(f"  Tipo: {df[col].dtype}, n_valid: {df[col].notna().sum()}")
    print("  Valores únicos top 10:")
    for v, n in vc.items():
        repr_v = repr(v)[:50]
        print(f"    {repr_v:55s}  n={n}")

# Mismo para P30 (categorías)
print("\n\n" + "="*80)
print("P30 cols (categorías hábito)")
print("="*80)
p30_cols = [c for c in df.columns if str(c).strip().startswith('{P30}')]
for col in p30_cols[:3]:
    print(f"\n--- {col[:80]} ---")
    vc = df[col].value_counts(dropna=False).head(10)
    print(f"  Tipo: {df[col].dtype}, n_valid: {df[col].notna().sum()}")
    print("  Valores únicos top 10:")
    for v, n in vc.items():
        repr_v = repr(v)[:50]
        print(f"    {repr_v:55s}  n={n}")
