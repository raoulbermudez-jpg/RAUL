"""Verificación rápida para Cora — V7
1. Plan Suárez % preferencia en C+/C (Cora dice >15%)
2. Hipótesis DNA: ¿categoría completa se mueve a precio?
   - P22 importancia de precio 2026 vs 2025
   - P21.1 razón espontánea precio por cadena 2026 vs 2025
   - ¿Otros competidores (no solo Rio) migraron a precio?
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd
import re
from collections import Counter

BBDD_2026 = r"G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\BBDD Notoriedad 2026.xlsx"
BBDD_2025 = r"G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\Notoriedad 2025.xlsx"

print("="*60)
print("VERIFICACION 1 — PLAN SUAREZ en C+/C 2026")
print("="*60)

df = pd.read_excel(BBDD_2026)
print(f"BBDD 2026: n={len(df)}")

# Buscar columnas NSE y P21
def find_strict(df, *patterns):
    for col in df.columns:
        s = str(col)
        for p in patterns:
            if re.search(r'\b' + p + r'\b', s, re.I):
                return col
    return None

col_nse = find_strict(df, 'PD4', 'NSE')
col_pref = find_strict(df, 'P21')
# P21 puede ser "preferido" o variantes
if not col_pref or 'preferid' not in str(col_pref).lower():
    for c in df.columns:
        s = str(c).lower()
        if 'p21' in s and 'preferid' in s and 'razon' not in s:
            col_pref = c
            break

print(f"Columna NSE: {col_nse}")
print(f"Columna P21 preferida: {col_pref}")

if col_nse and col_pref:
    # Filtrar C+/C
    df['nse_norm'] = df[col_nse].astype(str).str.strip().str.upper().str.replace(' ', '')
    cpc = df[df['nse_norm'].isin(['C+/C', 'C+', 'C'])]
    print(f"\nN total C+/C: {len(cpc)}")

    # Distribución P21 en C+/C
    print(f"\nDistribución P21 (Preferida) en C+/C:")
    counts = cpc[col_pref].value_counts()
    total_cpc = len(cpc)
    for marca, n in counts.head(15).items():
        pct = n/total_cpc*100
        flag = '  ★★★' if 'plan' in str(marca).lower() else ('  ★' if 'gama' in str(marca).lower() or 'param' in str(marca).lower() else '')
        print(f"  {str(marca)[:40]:<42} n={n:3}  {pct:5.1f}%{flag}")

    # Específico Plan Suárez
    plan_mask = cpc[col_pref].astype(str).str.lower().str.contains('plan|suarez|suárez', na=False)
    plan_n = plan_mask.sum()
    plan_pct = plan_n / total_cpc * 100 if total_cpc else 0
    print(f"\n>>> PLAN SUAREZ en C+/C: n={plan_n} de {total_cpc} = {plan_pct:.1f}%")
    if plan_pct >= 15:
        print(f"    ✅ CONFIRMA hipótesis Cora (Plan Suárez >15% en C+/C)")
    elif plan_pct >= 10:
        print(f"    ⚠ NO llega a 15% pero está cerca ({plan_pct:.1f}%) — Cora puede estar pensando en otro corte")
    else:
        print(f"    ❌ Plan Suárez NO tiene 15%+ en C+/C según estos datos")

print("\n" + "="*60)
print("VERIFICACION 2 — HIPOTESIS DNA: ¿categoría se mueve a precio?")
print("="*60)

# 2a. P22 importancia de Menor precio en 2026 vs 2025
print("\n2a. P22 importancia 'Menor precio' 2026 vs 2025:")
col_p22_precio_2026 = None
for c in df.columns:
    s = str(c).lower()
    if 'p22' in s and ('menor precio' in s or 'precio' in s and 'menor' in s):
        col_p22_precio_2026 = c
        break
if col_p22_precio_2026:
    print(f"  Columna 2026: {str(col_p22_precio_2026)[:80]}")
    vals_2026 = df[col_p22_precio_2026].dropna()
    print(f"  Distribución 2026 (n={len(vals_2026)}):")
    print(vals_2026.value_counts().head(7).to_string())

# 2025
df25 = pd.read_excel(BBDD_2025, sheet_name='NotoriedadVF2V23_SPSS2')
print(f"\nBBDD 2025: n={len(df25)}")
# Buscar P22_8 o similar para "menor precio" (V3 contexto: P22 tenía 20 atributos en 2025)
col_p22_precio_2025 = None
for c in df25.columns:
    s = str(c).lower()
    if ('p22' in s) and ('menor' in s and 'precio' in s):
        col_p22_precio_2025 = c
        break
if col_p22_precio_2025:
    print(f"  Columna 2025: {str(col_p22_precio_2025)[:80]}")
    vals_2025 = df25[col_p22_precio_2025].dropna()
    print(f"  Distribución 2025 (n={len(vals_2025)}):")
    print(vals_2025.value_counts().head(7).to_string())

# 2b. P21.1 razón espontánea — análisis cross-cadena
print("\n2b. P21.1 razón espontánea — % personas que mencionan 'precio' por cadena (2026)")
# P21 preferida + P21.1 razón abierta
col_p211 = None
for c in df.columns:
    s = str(c).lower()
    if 'p21.1' in s or ('p21' in s and 'razon' in s):
        col_p211 = c
        break
# P21.1 puede estar como una sola columna con texto, o multi-columna por opción
if col_p211:
    print(f"  Columna P21.1 detectada: {str(col_p211)[:80]}")
else:
    # Buscar columnas multi: V210...V225 por ejemplo (16 slots de razón)
    p211_cols = [c for c in df.columns if 'p21.1' in str(c).lower() or 'razon' in str(c).lower() and 'preferid' in str(c).lower()]
    print(f"  Columnas P21.1 multi-slot detectadas: {len(p211_cols)}")
    if p211_cols:
        print(f"  Ejemplo: {p211_cols[0][:80]}")

# Cruce P21 preferida x razón precio
if col_pref:
    cadenas = ['Gama', 'Páramo', 'Rio', 'Central', 'Plan', 'Forum', 'Plazas', 'Luz']
    print(f"\n  Análisis por cadena 2026:")
    print(f"  {'Cadena':<20} {'n pref':<8} {'% menciona precio*':<22}")
    print(f"  {'-'*55}")

    # Para cada cadena, buscar sus preferentes y revisar todas las columnas P21.1
    p211_cols = [c for c in df.columns if 'p21.1' in str(c).lower()]
    if not p211_cols:
        # Alternativa: buscar columnas que mencionen "razon" después de preferida
        for c in df.columns[df.columns.get_loc(col_pref):][:30] if col_pref in df.columns else []:
            s = str(c).lower()
            if 'razon' in s or 'porque' in s:
                p211_cols.append(c)

    if p211_cols:
        # Heurística: concat de todas las respuestas P21.1 por persona, buscar 'precio'
        df['todas_razones'] = df[p211_cols].fillna('').astype(str).agg(' | '.join, axis=1).str.lower()
        for cad in cadenas:
            mask_cad = df[col_pref].astype(str).str.lower().str.contains(cad.lower(), na=False)
            n_cad = mask_cad.sum()
            if n_cad >= 10:
                menciona_precio = df.loc[mask_cad, 'todas_razones'].str.contains('precio|barato|econom|cashea', regex=True).sum()
                pct = menciona_precio / n_cad * 100 if n_cad else 0
                print(f"  {cad:<20} n={n_cad:<6} {pct:5.1f}%")
            else:
                print(f"  {cad:<20} n={n_cad:<6} (base baja, omitir)")
    else:
        print("  No se encontraron columnas P21.1 — verificar nombres")

print("\n" + "="*60)
print("INTERPRETACION PRELIMINAR")
print("="*60)
print("""
Sobre hipótesis Cora 'categoría se mueve a precio':
- Si % menciona precio AUMENTÓ en TODAS las cadenas (Gama incluido) entre 2025 y 2026 →
  Cora tiene razón: tendencia categorial generalizada.
- Si % menciona precio SOLO aumentó en algunas cadenas (Rio, Páramo) pero Gama
  se mantuvo en atención → mi narrativa V7 era correcta: vacío en cuadrante experiencial.

(Comparativo 2025-2026 requeriría replicar este cálculo en BBDD 2025 — pendiente.)
""")
