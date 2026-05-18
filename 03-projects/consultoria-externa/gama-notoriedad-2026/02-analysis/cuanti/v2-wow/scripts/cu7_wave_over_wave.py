"""
cu7_wave_over_wave.py — CU-7 Wave-over-Wave Analysis 2025 vs 2026
Proyecto: Gama Notoriedad 2026
Autor: Cuanti (agente analitico)
Fecha: 2026-05-17

Proposito:
  Ejecuta el analisis wave-over-wave 2025 vs 2026 segun protocolo ME-5.
  Pasos 0-8: mapping items, comparabilidad muestral, ponderacion,
  Newcombe-Wilson, BH-FDR, subgrupos, forest plot, caveats para Bruna.

Inputs:
  - BBDD 2026: G:/Mi unidad/.../BBDD Notoriedad 2026.xlsx
  - BBDD 2025: G:/Mi unidad/.../Notoriedad 2025.xlsx  hoja NotoriedadVF2V23_SPSS2
  - utils.py en cuanti/scripts/

Outputs:
  - v2-wow/outputs/json/CU7_wow_results_20260517_v1.json
  - v2-wow/plots/wow_top_changes_20260517_v1.png
  - v2-wow/mapping_2025_2026.csv   (escrito desde este script tambien)

Notas metodologicas clave (segun ME-5):
  - @PONDERAR_1 en 2025 = todo cero -> excepcion ME-5 S2.4: sin ponderacion,
    documentado como decision in-flight D-CU7-001.
  - Test comparabilidad muestral: chi2 alpha=0.10.
  - Test WoW: Newcombe-Wilson (statsmodels proportion_confint wilson).
  - Correccion multiple: Benjamini-Hochberg FDR q<0.05.
  - Subgrupos solo n>=50 en AMBAS olas.
"""

import sys
import os
import json
import csv
import datetime

sys.stdout.reconfigure(encoding='utf-8')

import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.proportion import proportion_confint
from statsmodels.stats.multitest import multipletests
import warnings
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

warnings.filterwarnings('ignore')

# ─── CONSTANTES CONFIGURABLES ───────────────────────────────────────────────
ALPHA_WOW      = 0.05    # significancia analisis sustantivo WoW
ALPHA_SAMP     = 0.10    # umbral comparabilidad muestral (ME-5 S2.3)
ALPHA_TEND     = 0.10    # tendencia 90%
BASE_BAJA      = 30      # n < 30 = referencial
BASE_MIN_SGR   = 50      # minimo n subgrupo para test WoW (ME-5 S2.7)
BASE_EXC       = 10      # n < 10 = excluir inferencia
FDR_Q          = 0.05    # FDR threshold BH
FECHA          = "20260517"
VERSION        = "v1"

# Paths
BBDD_2026 = "G:/Mi unidad/RAUL/colaboradores/Genteca/Cora-Urrea/01_De_Cora_Para_Raoul/Notoriedad V2.0/BBDD Notoriedad 2026.xlsx"
BBDD_2025 = "G:/Mi unidad/RAUL/colaboradores/Genteca/Cora-Urrea/01_De_Cora_Para_Raoul/Notoriedad V2.0/Notoriedad 2025.xlsx"
SHEET_2025 = "NotoriedadVF2V23_SPSS2"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WOW_DIR    = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))
OUT_JSON   = os.path.join(WOW_DIR, 'outputs', 'json')
OUT_PLOTS  = os.path.join(WOW_DIR, 'plots')
UTILS_DIR  = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..', '..', '..', '02-analysis', 'cuanti', 'scripts'))

# Ensure output dirs exist
os.makedirs(OUT_JSON, exist_ok=True)
os.makedirs(OUT_PLOTS, exist_ok=True)

# Add utils path
sys.path.insert(0, UTILS_DIR)
from utils import NumpyEncoder, dump_json

print(f"[CU-7 WoW] Iniciando — {datetime.datetime.now().isoformat()}")
print(f"  pandas {pd.__version__} | numpy {np.__version__}")
print()

# ─── DECISION IN-FLIGHT REGISTRY ────────────────────────────────────────────
decisions_inflight = []

def reg_decision(code, descripcion, razon, accion):
    decisions_inflight.append({
        "codigo": code,
        "descripcion": descripcion,
        "razon": razon,
        "accion": accion
    })
    print(f"  [DECISION {code}] {descripcion}")

# ─── HELPER FUNCTIONS ────────────────────────────────────────────────────────

def base_flag(n):
    if n < BASE_EXC:   return "EXCLUIR"
    if n < BASE_BAJA:  return "REFERENCIAL"
    return "OK"

def newcombe_wilson_ci(p1, n1, p2, n2, alpha=ALPHA_WOW):
    """
    Newcombe-Wilson interval for difference of two independent proportions.
    Newcombe (1998) Statistics in Medicine 17(8).
    Uses proportion_confint(method='wilson') for each prop individually.
    Returns: delta_pp, ci_low_delta, ci_high_delta, p_value, sig_flag
    """
    if n1 < BASE_EXC or n2 < BASE_EXC:
        return None, None, None, None, "base_insuficiente"

    x1 = p1 * n1
    x2 = p2 * n2

    # Wilson CI for each proportion
    lo1, hi1 = proportion_confint(x1, n1, alpha=alpha, method='wilson')
    lo2, hi2 = proportion_confint(x2, n2, alpha=alpha, method='wilson')

    delta = p1 - p2  # positive = increase 2025->2026 (note: 2026 is p1)

    # Newcombe (1998) eq 10: score interval for difference
    ci_low  = delta - np.sqrt((p1 - lo1)**2 + (hi2 - p2)**2)
    ci_high = delta + np.sqrt((hi1 - p1)**2 + (p2 - lo2)**2)

    # p-value via chi2 (2x2 table)
    # Build 2x2: [x1, n1-x1; x2, n2-x2]
    try:
        ct = np.array([[round(x1), round(n1 - x1)],
                       [round(x2), round(n2 - x2)]])
        # Use continuity correction if any cell < 5
        if ct.min() < 5:
            chi2_val, p_val = stats.chi2_contingency(ct, correction=True)[:2]
        else:
            chi2_val, p_val = stats.chi2_contingency(ct, correction=False)[:2]
    except Exception:
        p_val = 1.0

    delta_pp   = round(delta * 100, 2)
    ci_low_pp  = round(ci_low * 100, 2)
    ci_high_pp = round(ci_high * 100, 2)

    sig_flag = ("sig_99" if p_val < 0.01 else
                "sig_95" if p_val < 0.05 else
                "tendencia_90" if p_val < 0.10 else
                "no_sig")

    return delta_pp, ci_low_pp, ci_high_pp, round(float(p_val), 6), sig_flag


def sig_symbol(sig_flag):
    """Return deck symbol for significance level."""
    return {"sig_99": "↑↑/↓↓", "sig_95": "↑/↓",
            "tendencia_90": "↑°/↓°", "no_sig": "≈",
            "base_insuficiente": "n/a"}.get(sig_flag, "?")


def count_brand_in_cols(df, cols, brand_str):
    """Count rows where brand_str appears in ANY of cols."""
    if not cols:
        return 0
    hits = pd.Series(False, index=df.index)
    for c in cols:
        hits |= df[c].astype(str).str.contains(brand_str, case=False, na=False)
    return int(hits.sum())


def prop_brand_in_cols(df, cols, brand_str, mask=None):
    """Proportion of rows (in mask) that mention brand_str in any col."""
    if mask is None:
        mask = pd.Series(True, index=df.index)
    n = int(mask.sum())
    if n == 0:
        return 0.0, n
    x = count_brand_in_cols(df[mask], cols, brand_str)
    return x / n, n


# ════════════════════════════════════════════════════════════════════════════
# CARGA DE DATOS
# ════════════════════════════════════════════════════════════════════════════
print("[0/8] Cargando BBDD 2026 y 2025...")

df26 = pd.read_excel(BBDD_2026, engine='openpyxl')
df25 = pd.read_excel(BBDD_2025, sheet_name=SHEET_2025, engine='openpyxl')

n26 = len(df26)
n25 = len(df25)
print(f"  BBDD 2026: n={n26}, cols={len(df26.columns)}")
print(f"  BBDD 2025: n={n25}, cols={len(df25.columns)}")

# ─── COLUMNAS DEMOGRAFICAS 2026 ─────────────────────────────────────────────
COL_MUN_26  = ' {PF2} [V535] Municipio'
COL_GEN_26  = ' {PF5} [V150] Genero'
COL_EDAD_26 = ' {PF7} [V152] Grupo edad'
COL_NSE_26  = ' {PD4} [V153] Marcar nse zona'

# ─── COLUMNAS DEMOGRAFICAS 2025 ─────────────────────────────────────────────
COL_MUN_25  = 'V535'
COL_GEN_25  = 'GEN'
COL_EDAD_25 = 'EDAD'
COL_NSE_25  = 'NSE'

# ─── VERIFICACION PONDERACION @PONDERAR_1 ────────────────────────────────────
print()
print("[PASO 3] Verificando @PONDERAR_1 en BBDD 2025...")
w_col = df25['@PONDERAR_1']
w_min = float(w_col.min())
w_max = float(w_col.max())
w_mean = float(w_col.mean())
print(f"  @PONDERAR_1: min={w_min} max={w_max} mean={w_mean}")
pondera_2025 = False
deff_nota = None
if w_max == 0.0 and w_min == 0.0:
    reg_decision(
        "D-CU7-001",
        "@PONDERAR_1 = todo cero en BBDD 2025",
        (
            "La columna @PONDERAR_1 tiene todos los valores en 0.0 (int64, sin variacion). "
            "Esto NO es un factor de expansion continuo — es un campo vacio o sin calcular. "
            "Aplicar como peso produciria estimados de 0% en todas las variables (peso=0 anula todas las obs). "
            "ME-5 S2.4 excepcion: 'si todos los valores son 1.0 la ponderacion es trivial; si es flag binario o "
            "ausente, documentar y proceder sin ajuste'. La situacion aqui es mas grave: el campo esta vacio. "
        ),
        (
            "NO aplicar @PONDERAR_1. Todos los analisis 2025 usan datos sin ponderar. "
            "Reportar como caveat de nivel MEDIO: los estimados 2025 asumen diseno muestral auto-ponderado, "
            "lo cual puede no ser correcto si existia un diseno muestral complejo. "
            "DEFF = 1.0 por construccion (sin ponderacion)."
        )
    )
    deff_nota = "DEFF=1.0 (sin ponderacion — @PONDERAR_1 vacia en BBDD 2025)"
else:
    pondera_2025 = True
    print(f"  @PONDERAR_1 es factor valido. Aplicando en analisis 2025.")

print()

# ─── COLUMNAS EMBUDO 2026 ────────────────────────────────────────────────────
p16_cols_26 = [c for c in df26.columns if '{P16}' in c]
p17_cols_26 = [c for c in df26.columns if '{P17}' in c]
p19_cols_26 = [c for c in df26.columns if '{P19}' in c]
p20_cols_26 = [c for c in df26.columns if '{P20}' in c]
col_p21_26  = ' {P21} [V194] Preferido'

# ─── COLUMNAS EMBUDO 2025 ────────────────────────────────────────────────────
p16_cols_25 = [c for c in df25.columns if c.startswith('P16')]
p17_cols_25 = [c for c in df25.columns if c.startswith('P17')]
p19_cols_25 = [c for c in df25.columns if c.startswith('P19')]
p20_cols_25 = [c for c in df25.columns if c.startswith('P20')]
col_p21_25  = 'P21O'

# P26 misiones
p26_cols_26 = [c for c in df26.columns if '{P26}' in c]
p26_cols_25 = [c for c in df25.columns if c.startswith('P26_') and c != 'P26_PRE']

# P30 supermercado habitual
p30_cols_26 = [c for c in df26.columns if '{P30}' in c]
p30_cols_25 = [c for c in df25.columns if c.startswith('P30_') and c != 'P30_PRE']

# P22 importancia atributos (solo 10 comunes)
# 2026: cols with {P22}
p22_cols_26 = [c for c in df26.columns if '{P22}' in c]
# 2025: P22_1..P22_20 — see mapping below
p22_cols_25_all = [f'P22_{i}' for i in range(1, 21) if f'P22_{i}' in df25.columns]

# P23 asociacion Gama (10 atributos comunes en 2026)
# 2026: cols with {P23:X} and 'Gama' — already found above
p23_gama_cols_26 = [c for c in df26.columns if '{P23:' in c and 'Gama' in c]

# P24 ultima compra
col_p24_26 = [c for c in df26.columns if '{P24}' in c]
col_p24_25 = ['P24'] if 'P24' in df25.columns else []

# P31 ranking
p31_cols_26 = [c for c in df26.columns if '{P31}' in c]
p31_cols_25 = [f'P31_{i}' for i in range(1, 7) if f'P31_{i}' in df25.columns]

# ─── NSE HARMONIZATION ───────────────────────────────────────────────────────
# 2025: C+, C, D, E  |  2026: C+/C, D, E
def harmonize_nse_25(s):
    """Map 2025 NSE (C+/C/D/E) to 2026 categories (C+/C, D, E)."""
    s = str(s).strip()
    if s in ('C+', 'C'):
        return 'C+/C'
    elif s == 'D':
        return 'D'
    elif s == 'E':
        return 'E'
    else:
        return 'Otro'

df25['NSE_harm'] = df25[COL_NSE_25].apply(harmonize_nse_25)
df26['NSE_harm'] = df26[COL_NSE_26].astype(str).str.strip()

# ─── EDAD AGRUPADA ───────────────────────────────────────────────────────────
# Both 2025 and 2026 have "25 a 34", "35 a 44", "45 a 54", "55 a 64"
# Remap to 3 groups: 18-34, 35-50, 51+
def harmonize_edad(s):
    s = str(s).strip()
    if '25 a 34' in s:
        return '25-34'
    elif '35 a 44' in s:
        return '35-44'
    elif '45 a 54' in s:
        return '45-54'
    elif '55' in s or '64' in s:
        return '55-64'
    else:
        return 'Otro'

df25['EDAD_harm'] = df25[COL_EDAD_25].apply(harmonize_edad)
df26['EDAD_harm'] = df26[COL_EDAD_26].apply(harmonize_edad)

# ─── MUNICIPIO HARMONIZATION ─────────────────────────────────────────────────
# 2025: Baruta, Libertador, Sucre, Chacao, FORANEOS, El Hatillo
# 2026: Baruta, Libertador, Sucre, Chacao, El Hatillo, FORANEOS
def harmonize_mun(s):
    s = str(s).strip()
    mapping = {
        'Baruta': 'Baruta', 'Sucre': 'Sucre', 'Chacao': 'Chacao',
        'Libertador': 'Libertador', 'El Hatillo': 'El Hatillo',
        'FORANEOS': 'FORANEOS', 'Foraneos': 'FORANEOS'
    }
    return mapping.get(s, 'Otro')

df25['MUN_harm'] = df25[COL_MUN_25].apply(harmonize_mun)
df26['MUN_harm'] = df26[COL_MUN_26].apply(harmonize_mun)

print(f"  NSE 2025 (harmonized): {df25['NSE_harm'].value_counts().to_dict()}")
print(f"  NSE 2026: {df26['NSE_harm'].value_counts().to_dict()}")
print()


# ════════════════════════════════════════════════════════════════════════════
# PASO 0 + 1: MAPPING_2025_2026.CSV
# ════════════════════════════════════════════════════════════════════════════
print("[PASO 0+1] Construyendo mapping_2025_2026.csv...")

# The 10 common P22/P23 attributes between 2025 and 2026 (per ME-5 §2.2 Case A)
# 2026 P22/P23 labels from BBDD headers -> match with 2025 P22_X by description
# Decision D-CU7-002: P22 mapping 2025->2026
# 2025 P22_1..20 have no labels in BBDD. The 10 common attributes in 2026 are:
# {P23:1}=mayor_categorias, {P23:2}=mayor_calidad, {P23:3}=menor_precio,
# {P23:4}=mejor_atienden, {P23:5}=promociones, {P23:6}=atractiva,
# {P23:8}=limpio_ordenado, {P23:12}=seguro, {P23:13}=rapidez_caja,
# {P23:21}=hacer_valer
# For P22, the same 10 attributes. In 2025, P22_1..10 are the base set (10 core attrs)
# and P22_11..20 are additional attrs. Based on T2B ordering and ME-5 §2.2 Case A
# which says "the Guide marks in black the 10 attributes that are maintained",
# we apply D-CU7-002: cannot map P22_1..20 to specific 2026 labels without the
# original questionnaire labels. Mark as comparable_con_caveat using T2B ranks.
reg_decision(
    "D-CU7-002",
    "P22 atributos: BBDD 2025 tiene P22_1..P22_20 sin etiquetas de texto en la BBDD",
    (
        "La BBDD 2025 codifica P22 como P22_1..P22_20 (numericos) sin labels de texto en las columnas. "
        "No es posible mapear con certeza cuales P22_X en 2025 corresponden a cuales de los 10 atributos comunes "
        "de 2026 sin el diccionario de codigos o el cuestionario con orden de preguntas. "
        "El cuestionario .xls tiene datos de campo (no labels). "
        "El mapping P22 requeriria: (a) diccionario de variables 2025, o (b) confirmacion del equipo de campo. "
    ),
    (
        "Para P22 importancia: NO comparar a nivel de atributo individual. Comparar solo el T2B promedio "
        "de los 10 atributos vs el T2B promedio de los 10 comparables en 2026 "
        "(assuming P22_1..P22_10 = los 10 atributos base en 2025, que es la hipotesis mas conservadora). "
        "Marcar todas las comparaciones P22 individuales como 'comparable_con_caveat' = NO comparable individualmente. "
        "Reportar solo nivel agregado con caveat ALTO."
    )
)

# For P23 association: P23_[atrib]_[slot] in 2025 where atrib = 1..20.
# In 2025, P23_[atrib] maps to same 10 common attributes by number IF the numbering is consistent.
# P23 numbering in 2026: {P23:1,2,3,4,5,6,8,12,13,21}
# In 2025, P23_1..P23_20 — atrib numbers appear consistent with 2026 numbering.
# P23:1-6, 8, 12, 13 are present in both olas. P23:21 is new in 2026 (V1857 = "hacer valer dinero").
reg_decision(
    "D-CU7-003",
    "P23:21 (hacer valer mi dinero) es nuevo en 2026 — no comparable",
    "La columna {P23:21} [V1857] no existe en el cuestionario 2025. El maximo numero de atributo en 2025 es 20.",
    "Excluir P23:21 del analisis WoW. Comparable a nivel P23: atributos 1,2,3,4,5,6,8,12,13 (9 comunes)."
)

# P24 habitual: in 2026 is a multi-select; in 2025 is P24 (single marca)
p24_col_26 = [c for c in df26.columns if '{P24}' in c]

# P30 habitual supermercado: similar logic
p30_col_26 = [c for c in df26.columns if '{P30}' in c]

# Build mapping CSV
BRANDS_COMMON = [
    'Gama (Excelsior)', 'Paramo', 'Forum', 'Central Madeirense',
    'Plazas', 'Rio', 'Luz', 'Plan Suarez', 'Hiper Lider'
]
BRAND_SEARCH = {
    'Gama (Excelsior)': 'Gama',
    'Paramo': 'Paramo',
    'Forum': 'Forum',
    'Central Madeirense': 'Central Madeirense',
    'Plazas': 'Plazas',
    'Rio': 'Rio',
    'Luz': 'Luz',
    'Plan Suarez': 'Plan Suarez',
    'Hiper Lider': 'Hiper Lider',
}

# P26 mission labels in 2026
p26_labels_26 = {}
for c in p26_cols_26:
    # Extract mission short label
    if 'MISION' in c.upper() or 'MISIÓN' in c.upper():
        label = c.split(']')[-1].strip()[:80] if ']' in c else c[:80]
        p26_labels_26[c] = label

mapping_rows = []

# EMBUDO variables (P16,P17,P19,P20,P21) by brand
for brand in BRANDS_COMMON:
    brand_search = BRAND_SEARCH.get(brand, brand)
    # P16 TOM
    mapping_rows.append({
        'pregunta_id_2025': 'P16',
        'nombre_columna_2025': 'P16O_*/P16_1 (multi-slot)',
        'pregunta_id_2026': 'P16',
        'nombre_columna_2026': f'{{P16}} - {brand}',
        'tipo_variable': 'binaria_multiselect',
        'marcado_guia': 'negro',
        'enunciado_identico': 'si',
        'n_opciones_2025': 'multi-slot texto',
        'n_opciones_2026': 'binaria por marca',
        'estrategia_reconciliacion': 'CasoC_union_slots',
        'notas': f'Brand={brand_search}. 2026 es col binaria; 2025 es texto en slots multi-mention.'
    })
    # P17 Asistida
    mapping_rows.append({
        'pregunta_id_2025': 'P17',
        'nombre_columna_2025': 'P17O_* (multi-slot)',
        'pregunta_id_2026': 'P17',
        'nombre_columna_2026': f'{{P17}} - {brand}',
        'tipo_variable': 'binaria_multiselect',
        'marcado_guia': 'negro',
        'enunciado_identico': 'si',
        'n_opciones_2025': 'multi-slot texto',
        'n_opciones_2026': 'binaria por marca',
        'estrategia_reconciliacion': 'CasoC_union_slots',
        'notas': f'Brand={brand_search}.'
    })
    # P19 Consideracion
    mapping_rows.append({
        'pregunta_id_2025': 'P19',
        'nombre_columna_2025': 'P19O_* (multi-slot)',
        'pregunta_id_2026': 'P19',
        'nombre_columna_2026': f'{{P19}} - {brand}',
        'tipo_variable': 'binaria_multiselect',
        'marcado_guia': 'negro',
        'enunciado_identico': 'si',
        'n_opciones_2025': 'multi-slot texto',
        'n_opciones_2026': 'binaria por marca',
        'estrategia_reconciliacion': 'CasoC_union_slots',
        'notas': f'Brand={brand_search}.'
    })
    # P20 Compra 3m
    mapping_rows.append({
        'pregunta_id_2025': 'P20',
        'nombre_columna_2025': 'P20O_* (multi-slot)',
        'pregunta_id_2026': 'P20',
        'nombre_columna_2026': f'{{P20}} - {brand}',
        'tipo_variable': 'binaria_multiselect',
        'marcado_guia': 'negro',
        'enunciado_identico': 'si',
        'n_opciones_2025': 'multi-slot texto',
        'n_opciones_2026': 'binaria por marca',
        'estrategia_reconciliacion': 'CasoC_union_slots',
        'notas': f'Brand={brand_search}.'
    })
    # P21 Preferida
    mapping_rows.append({
        'pregunta_id_2025': 'P21',
        'nombre_columna_2025': 'P21O',
        'pregunta_id_2026': 'P21',
        'nombre_columna_2026': ' {P21} [V194] Preferido',
        'tipo_variable': 'categorica_unica',
        'marcado_guia': 'negro',
        'enunciado_identico': 'si',
        'n_opciones_2025': 'texto libre (marca)',
        'n_opciones_2026': 'texto libre (marca)',
        'estrategia_reconciliacion': 'CasoC_match_texto',
        'notas': f'Brand={brand_search}. Ambas olas texto. Match por string contains.'
    })

# P22 importancia (nivel agregado, no individual)
mapping_rows.append({
    'pregunta_id_2025': 'P22_1-10',
    'nombre_columna_2025': 'P22_1..P22_20 (sin etiquetas)',
    'pregunta_id_2026': 'P22',
    'nombre_columna_2026': '{P22} 10 atributos',
    'tipo_variable': 'likert_5',
    'marcado_guia': 'negro_10_comunes',
    'enunciado_identico': 'parcial_sin_labels_2025',
    'n_opciones_2025': '20 atributos',
    'n_opciones_2026': '10 atributos',
    'estrategia_reconciliacion': 'CasoA_T2B_agregado_solo',
    'notas': (
        '[DECISION D-CU7-002] BBDD 2025 no tiene labels P22. '
        'Solo se compara T2B promedio agrupado. NO comparacion individual. Caveat ALTO.'
    )
})

# P23 asociacion Gama x 9 atributos comunes
for atrib_id, atrib_label in [
    ('1', 'mayor_categorias'), ('2', 'mayor_calidad'), ('3', 'menor_precio'),
    ('4', 'mejor_atienden'), ('5', 'promociones'), ('6', 'atractiva'),
    ('8', 'limpio_ordenado'), ('12', 'seguro'), ('13', 'rapidez_caja')
]:
    col26 = next((c for c in df26.columns if f'{{P23:{atrib_id}}}' in c and 'Gama' in c), None)
    mapping_rows.append({
        'pregunta_id_2025': f'P23_{atrib_id}',
        'nombre_columna_2025': f'P23_{atrib_id}_1..10 (multi-slot)',
        'pregunta_id_2026': f'P23:{atrib_id}',
        'nombre_columna_2026': col26 or f'{{P23:{atrib_id}}} Gama',
        'tipo_variable': 'binaria_multiselect',
        'marcado_guia': 'negro',
        'enunciado_identico': 'si',
        'n_opciones_2025': 'multi-slot texto',
        'n_opciones_2026': 'binaria_por_marca',
        'estrategia_reconciliacion': 'CasoB_union_slots_gama',
        'notas': f'Atributo {atrib_id} ({atrib_label}) — Gama. 2026 binaria; 2025 multi-slot texto.'
    })

# P23:21 hacer_valer — EXCLUIDO (new in 2026)
mapping_rows.append({
    'pregunta_id_2025': 'N/A',
    'nombre_columna_2025': 'NO_EXISTE',
    'pregunta_id_2026': 'P23:21',
    'nombre_columna_2026': '{P23:21} [V1857] hacer valer dinero - Gama',
    'tipo_variable': 'binaria',
    'marcado_guia': 'rojo_2026_only',
    'enunciado_identico': 'no',
    'n_opciones_2025': '0',
    'n_opciones_2026': 'binaria',
    'estrategia_reconciliacion': 'EXCLUIR_wow',
    'notas': '[DECISION D-CU7-003] Atributo nuevo en 2026. No comparable.'
})

# P24 ultima compra
mapping_rows.append({
    'pregunta_id_2025': 'P24',
    'nombre_columna_2025': 'P24',
    'pregunta_id_2026': 'P24',
    'nombre_columna_2026': '{P24} cols',
    'tipo_variable': 'categorica_unica/multiselect',
    'marcado_guia': 'negro',
    'enunciado_identico': 'si',
    'n_opciones_2025': 'texto_libre',
    'n_opciones_2026': 'multi-select',
    'estrategia_reconciliacion': 'CasoC_match_texto_gama',
    'notas': '2025=texto marca; 2026=multi-select. Comparable para Gama solo.'
})

# P26 misiones (por marca)
for brand in ['Gama (Excelsior)', 'Paramo', 'Forum', 'Central Madeirense']:
    brand_search = BRAND_SEARCH.get(brand, brand)
    mapping_rows.append({
        'pregunta_id_2025': 'P26',
        'nombre_columna_2025': 'P26_1..P26_5 (multi-slot)',
        'pregunta_id_2026': 'P26',
        'nombre_columna_2026': '{P26} misiones',
        'tipo_variable': 'binaria_multiselect',
        'marcado_guia': 'negro',
        'enunciado_identico': 'verificar_contenido_misiones',
        'n_opciones_2025': '5 misiones',
        'n_opciones_2026': 'misiones_verificar',
        'estrategia_reconciliacion': 'CasoC_union_slots',
        'notas': f'Brand={brand_search}. Misiones en 2025 son: abastecimiento/reposicion/compras_puntuales/compras_paseo/otros.'
    })

# Demograficas (CasoE)
for demo, col25, col26_label in [
    ('NSE', 'NSE', 'NSE_harm'), ('Municipio', 'V535', 'MUN_harm'),
    ('Genero', 'GEN', COL_GEN_26), ('Edad', 'EDAD', COL_EDAD_26)
]:
    mapping_rows.append({
        'pregunta_id_2025': demo,
        'nombre_columna_2025': col25,
        'pregunta_id_2026': demo,
        'nombre_columna_2026': col26_label,
        'tipo_variable': 'categorica',
        'marcado_guia': 'negro',
        'enunciado_identico': 'si',
        'n_opciones_2025': '—',
        'n_opciones_2026': '—',
        'estrategia_reconciliacion': 'CasoE_comparabilidad_muestral',
        'notas': 'Solo para test homogeneidad muestral (Paso 2).'
    })

# Write CSV
csv_path = os.path.join(WOW_DIR, 'mapping_2025_2026.csv')
fieldnames = ['pregunta_id_2025','nombre_columna_2025','pregunta_id_2026','nombre_columna_2026',
              'tipo_variable','marcado_guia','enunciado_identico','n_opciones_2025',
              'n_opciones_2026','estrategia_reconciliacion','notas']
with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(mapping_rows)

print(f"  mapping_2025_2026.csv: {len(mapping_rows)} filas -> {csv_path}")
print()


# ════════════════════════════════════════════════════════════════════════════
# PASO 2: COMPARABILIDAD MUESTRAL (chi2 alpha=0.10)
# ════════════════════════════════════════════════════════════════════════════
print("[PASO 2] Tests de comparabilidad muestral (chi2 alpha=0.10)...")

comparabilidad = {}

def test_homogeneidad(ser25, ser26, label, alpha=ALPHA_SAMP):
    """Chi2 de homogeneidad entre dos series categoricas."""
    cats = sorted(set(ser25.dropna().unique()) | set(ser26.dropna().unique()))
    cats = [c for c in cats if c not in ('Otro', 'nan', 'None', '')]
    if len(cats) < 2:
        return {"error": "menos de 2 categorias comparables", "comparable": True}
    ct25 = ser25.value_counts().reindex(cats, fill_value=0)
    ct26 = ser26.value_counts().reindex(cats, fill_value=0)
    ct = np.array([ct25.values, ct26.values])
    # Check min expected frequency
    row_totals = ct.sum(axis=1, keepdims=True)
    col_totals = ct.sum(axis=0, keepdims=True)
    expected = row_totals * col_totals / ct.sum()
    if (expected < 5).any():
        # Use Fisher exact if 2x2
        if ct.shape == (2, 2):
            _, p = stats.fisher_exact(ct)
            method = 'Fisher exact'
        else:
            chi2v, p, dof, _ = stats.chi2_contingency(ct, correction=True)
            method = 'chi2_continuity_correction'
    else:
        chi2v, p, dof, _ = stats.chi2_contingency(ct)
        method = 'chi2'

    comparable = p > alpha
    result = {
        "label": label,
        "method": method,
        "n_25": int(ser25[ser25.isin(cats)].count()),
        "n_26": int(ser26[ser26.isin(cats)].count()),
        "p_value": round(float(p), 4),
        "alpha_threshold": alpha,
        "comparable": comparable,
        "flag": "comparable" if comparable else "ajuste_recomendado",
        "distribucion_25": {str(c): int(ct25[c]) for c in cats},
        "distribucion_26": {str(c): int(ct26[c]) for c in cats},
    }
    flag_str = "OK p>{:.2f}".format(alpha) if comparable else "DIFERENCIA p<={:.2f}".format(alpha)
    print(f"  {label:20s}: p={p:.4f} [{flag_str}]")
    return result

comparabilidad['NSE'] = test_homogeneidad(
    df25['NSE_harm'], df26['NSE_harm'], 'NSE')
comparabilidad['Municipio'] = test_homogeneidad(
    df25['MUN_harm'], df26['MUN_harm'], 'Municipio')
comparabilidad['Genero'] = test_homogeneidad(
    df25[COL_GEN_25].astype(str).str.strip(),
    df26[COL_GEN_26].astype(str).str.strip(), 'Genero')
comparabilidad['Edad'] = test_homogeneidad(
    df25['EDAD_harm'], df26['EDAD_harm'], 'Edad')

n_fail = sum(1 for v in comparabilidad.values() if not v.get('comparable', True))
print(f"  Resultado: {n_fail}/4 variables fallan (p<=0.10)")
if n_fail >= 2:
    reg_decision(
        "D-CU7-004",
        f"{n_fail}/4 variables demograficas fallan test homogeneidad (p<=0.10)",
        (
            "Multiple demographic variables show distributional differences between 2025 and 2026. "
            "This increases the risk that observed WoW differences partially reflect composition "
            "rather than real market changes. ME-5 §2.3 mandates a ALTO caveat level when multiple fail."
        ),
        (
            "Todos los resultados WoW se presentan con CAVEAT ALTO de comparabilidad muestral. "
            "Los deltas deben interpretarse con cautela. No aplicar post-stratification formal "
            "dado que @PONDERAR_1 esta vacia."
        )
    )
print()


# ════════════════════════════════════════════════════════════════════════════
# PASO 4: NEWCOMBE-WILSON POR ITEM COMPARADO
# ════════════════════════════════════════════════════════════════════════════
print("[PASO 4] Newcombe-Wilson por item (embudo + P23 Gama)...")

wow_items = []

def make_wow_item(var_id, label, p26_prop, n26, p25_prop, n25, weighted_2025,
                  comparability_caveat=None, caso=None):
    """Build WoW item dict and compute Newcombe-Wilson."""
    delta_pp, ci_low, ci_high, p_val, sig_flag = newcombe_wilson_ci(
        p26_prop, n26, p25_prop, n25
    )
    item = {
        "variable_id": var_id,
        "label": label,
        "caso": caso,
        "estimate_2026": round(float(p26_prop), 4),
        "n_2026": int(n26),
        "estimate_2025": round(float(p25_prop), 4),
        "n_2025": int(n25),
        "delta_pp": delta_pp,   # positive = 2026 > 2025
        "ci_95_low_delta": ci_low,
        "ci_95_high_delta": ci_high,
        "p_value": p_val,
        "sig_flag": sig_flag,
        "sig_symbol": sig_symbol(sig_flag),
        "method": "Newcombe-Wilson",
        "weighted_2025": weighted_2025,
        "comparability_caveat": comparability_caveat,
        "flag_n26": base_flag(n26),
        "flag_n25": base_flag(n25),
    }
    return item

# EMBUDO por marca
print("  Embudo por marca...")
for brand, brand_search in BRAND_SEARCH.items():
    for etapa, cols26, cols25, is_p21 in [
        ('TOM_P16', p16_cols_26, p16_cols_25, False),
        ('Asistida_P17', p17_cols_26, p17_cols_25, False),
        ('Consideracion_P19', p19_cols_26, p19_cols_25, False),
        ('Compra3m_P20', p20_cols_26, p20_cols_25, False),
        ('Preferida_P21', None, None, True),
    ]:
        if is_p21:
            p26_x = df26[col_p21_26].astype(str).str.contains(brand_search, case=False, na=False).sum()
            p26_prop = p26_x / n26
            p25_x = df25[col_p21_25].astype(str).str.contains(brand_search, case=False, na=False).sum()
            p25_prop = p25_x / n25
        else:
            p26_x = count_brand_in_cols(df26, cols26, brand_search)
            p26_prop = p26_x / n26
            p25_x = count_brand_in_cols(df25, cols25, brand_search)
            p25_prop = p25_x / n25

        var_id = f"{etapa}_{brand.replace(' ', '_').replace('(', '').replace(')', '')}"
        label  = f"{etapa} — {brand}"
        item = make_wow_item(
            var_id, label, p26_prop, n26, p25_prop, n25,
            weighted_2025=False,
            caso='C_embudo'
        )
        wow_items.append(item)

# P23 asociacion Gama x 9 atributos comunes
print("  P23 asociacion Gama x 9 atributos...")
ATRIB_MAP = {
    '1': 'mayor_categorias', '2': 'mayor_calidad', '3': 'menor_precio',
    '4': 'mejor_atienden', '5': 'promociones', '6': 'atractiva',
    '8': 'limpio_ordenado', '12': 'seguro', '13': 'rapidez_caja'
}

for atrib_id, atrib_label in ATRIB_MAP.items():
    # 2026: binary col for Gama
    col26 = next((c for c in df26.columns if f'{{P23:{atrib_id}}}' in c and 'Gama' in c), None)
    if col26 is None:
        print(f"    [WARN] P23:{atrib_id} col not found in 2026")
        continue
    p26_x = df26[col26].notna().sum()  # binary: non-null = 1
    p26_prop = p26_x / n26

    # 2025: P23_[atrib]_1..10 multi-slot — count Gama mentions
    p23_cols_atrib_25 = [c for c in df25.columns if c.startswith(f'P23_{atrib_id}_')]
    if not p23_cols_atrib_25:
        print(f"    [WARN] P23_{atrib_id}_* cols not found in 2025")
        continue
    p25_x = count_brand_in_cols(df25, p23_cols_atrib_25, 'Gama')
    p25_prop = p25_x / n25

    item = make_wow_item(
        f"P23_atrib{atrib_id}_Gama",
        f"P23 Asociacion Gama — {atrib_label}",
        p26_prop, n26, p25_prop, n25,
        weighted_2025=False,
        caso='B_asociacion_p23'
    )
    wow_items.append(item)

# P24 ultima compra (Gama)
print("  P24 ultima compra Gama...")
if col_p24_26:
    p24_gama_26 = count_brand_in_cols(df26, col_p24_26, 'Gama')
    p24_prop_26 = p24_gama_26 / n26
    # 2025: P24 is single text
    if 'P24' in df25.columns:
        p24_gama_25 = df25['P24'].astype(str).str.contains('Gama', case=False, na=False).sum()
        p24_prop_25 = p24_gama_25 / n25
        item = make_wow_item(
            "P24_Gama", "P24 Ultima compra — Gama",
            p24_prop_26, n26, p24_prop_25, n25,
            weighted_2025=False, caso='C_comportamiento'
        )
        wow_items.append(item)

# P26 misiones (Gama)
print("  P26 misiones Gama...")
if p26_cols_26 and p26_cols_25:
    p26_gama_26 = count_brand_in_cols(df26, p26_cols_26, 'Gama')
    p26_prop_26 = p26_gama_26 / n26
    p26_gama_25 = count_brand_in_cols(df25, p26_cols_25, 'Gama')
    p26_prop_25 = p26_gama_25 / n25
    item = make_wow_item(
        "P26_misiones_Gama", "P26 Misiones (cualquier mision) — Gama",
        p26_prop_26, n26, p26_prop_25, n25,
        weighted_2025=False, caso='C_comportamiento'
    )
    wow_items.append(item)

# P30 supermercado habitual (Gama)
print("  P30 supermercado habitual Gama...")
if p30_cols_26 and p30_cols_25:
    p30_gama_26 = count_brand_in_cols(df26, p30_cols_26, 'Gama')
    p30_prop_26 = p30_gama_26 / n26
    p30_gama_25 = count_brand_in_cols(df25, p30_cols_25, 'Gama')
    p30_prop_25 = p30_gama_25 / n25
    item = make_wow_item(
        "P30_habitual_Gama", "P30 Supermercado habitual — Gama",
        p30_prop_26, n26, p30_prop_25, n25,
        weighted_2025=False, caso='C_comportamiento'
    )
    wow_items.append(item)

print(f"  Total items WoW: {len(wow_items)}")
print()


# ════════════════════════════════════════════════════════════════════════════
# PASO 5: CORRECCION BH-FDR
# ════════════════════════════════════════════════════════════════════════════
print("[PASO 5] Correccion Benjamini-Hochberg FDR...")

# Only items with valid p-values
valid_idx = [i for i, item in enumerate(wow_items) if item['p_value'] is not None]
p_values_raw = [wow_items[i]['p_value'] for i in valid_idx]

if p_values_raw:
    reject, p_adjusted, _, _ = multipletests(p_values_raw, method='fdr_bh', alpha=FDR_Q)
    for j, idx in enumerate(valid_idx):
        wow_items[idx]['p_adjusted'] = round(float(p_adjusted[j]), 6)
        wow_items[idx]['reject_bh'] = bool(reject[j])
        # Override sig_flag with adjusted p
        p_adj = p_adjusted[j]
        adj_flag = ("sig_99" if p_adj < 0.01 else
                    "sig_95" if p_adj < 0.05 else
                    "tendencia_90" if p_adj < 0.10 else
                    "no_sig")
        wow_items[idx]['sig_flag_adjusted'] = adj_flag
        wow_items[idx]['sig_symbol_adjusted'] = sig_symbol(adj_flag)

# For items without p_value (base_insuficiente)
for item in wow_items:
    if 'p_adjusted' not in item:
        item['p_adjusted'] = None
        item['reject_bh'] = False
        item['sig_flag_adjusted'] = item.get('sig_flag', 'base_insuficiente')
        item['sig_symbol_adjusted'] = 'n/a'

n_sig = sum(1 for item in wow_items if item.get('reject_bh', False))
print(f"  {n_sig}/{len(wow_items)} items significativos tras BH-FDR q<0.05")
print()


# ════════════════════════════════════════════════════════════════════════════
# PASO 6: SUBGRUPOS NSE
# ════════════════════════════════════════════════════════════════════════════
print("[PASO 6] Subgrupos NSE (n>=50 en ambas olas)...")

subgroup_results = {}

nse_cats = ['C+/C', 'D', 'E']
for nse_cat in nse_cats:
    mask26 = df26['NSE_harm'] == nse_cat
    mask25 = df25['NSE_harm'] == nse_cat
    n26_s = int(mask26.sum())
    n25_s = int(mask25.sum())

    if n26_s < BASE_MIN_SGR or n25_s < BASE_MIN_SGR:
        print(f"  NSE {nse_cat}: n26={n26_s}, n25={n25_s} — SKIP (n<{BASE_MIN_SGR} en alguna ola)")
        subgroup_results[nse_cat] = {
            "n_26": n26_s, "n_25": n25_s,
            "status": "INSUFICIENTE",
            "nota": f"n<{BASE_MIN_SGR} en al menos una ola. Solo descriptivo."
        }
        continue

    print(f"  NSE {nse_cat}: n26={n26_s}, n25={n25_s} — OK, ejecutando tests...")
    sg_items = []

    for brand, brand_search in BRAND_SEARCH.items():
        # P21 preferida
        p26_x = df26[mask26][col_p21_26].astype(str).str.contains(brand_search, case=False, na=False).sum()
        p26_p = p26_x / n26_s
        p25_x = df25[mask25][col_p21_25].astype(str).str.contains(brand_search, case=False, na=False).sum()
        p25_p = p25_x / n25_s
        sg_item = make_wow_item(
            f"P21_Pref_{brand.replace(' ','_')}_NSE_{nse_cat}",
            f"P21 Preferida {brand} — NSE {nse_cat}",
            p26_p, n26_s, p25_p, n25_s,
            weighted_2025=False, caso='subgrupo_NSE'
        )
        sg_items.append(sg_item)

        # P16 TOM
        p26_x2 = count_brand_in_cols(df26[mask26], p16_cols_26, brand_search)
        p26_p2 = p26_x2 / n26_s
        p25_x2 = count_brand_in_cols(df25[mask25], p16_cols_25, brand_search)
        p25_p2 = p25_x2 / n25_s
        sg_item2 = make_wow_item(
            f"P16_TOM_{brand.replace(' ','_')}_NSE_{nse_cat}",
            f"P16 TOM {brand} — NSE {nse_cat}",
            p26_p2, n26_s, p25_p2, n25_s,
            weighted_2025=False, caso='subgrupo_NSE'
        )
        sg_items.append(sg_item2)

    # BH-FDR within subgroup
    valid_sg = [i for i, it in enumerate(sg_items) if it['p_value'] is not None]
    if valid_sg:
        p_sg = [sg_items[i]['p_value'] for i in valid_sg]
        rej_sg, p_adj_sg, _, _ = multipletests(p_sg, method='fdr_bh', alpha=FDR_Q)
        for j, idx in enumerate(valid_sg):
            sg_items[idx]['p_adjusted'] = round(float(p_adj_sg[j]), 6)
            sg_items[idx]['reject_bh'] = bool(rej_sg[j])
            p_a = p_adj_sg[j]
            af = ("sig_99" if p_a < 0.01 else "sig_95" if p_a < 0.05
                  else "tendencia_90" if p_a < 0.10 else "no_sig")
            sg_items[idx]['sig_flag_adjusted'] = af
            sg_items[idx]['exploratorio'] = True

    for item in sg_items:
        if 'p_adjusted' not in item:
            item['p_adjusted'] = None
            item['reject_bh'] = False
            item['sig_flag_adjusted'] = item.get('sig_flag', 'base_insuficiente')
            item['exploratorio'] = True

    n_sg_sig = sum(1 for it in sg_items if it.get('reject_bh', False))
    print(f"    {n_sg_sig}/{len(sg_items)} sig BH-FDR")
    subgroup_results[nse_cat] = {
        "n_26": n26_s, "n_25": n25_s,
        "status": "EJECUTADO",
        "nota_exploratoria": "Subgrupo no pre-registrado 2025. Interpretar como hipotesis para ola 2027.",
        "items": sg_items
    }

print()


# ════════════════════════════════════════════════════════════════════════════
# PASO 7: FOREST PLOT
# ════════════════════════════════════════════════════════════════════════════
print("[PASO 7] Forest plot de deltas significativos...")

# Filter to Gama items with valid delta
gama_items = [it for it in wow_items
              if 'Gama' in it['label'] and it['delta_pp'] is not None]

# Sort by abs delta, take top 15
gama_sorted = sorted(gama_items, key=lambda x: abs(x['delta_pp']), reverse=True)[:15]

if gama_sorted:
    labels_plot = []
    deltas = []
    ci_lows = []
    ci_highs = []
    colors = []
    sig_markers = []

    for it in gama_sorted:
        # Shorten label
        lbl = it['label'].replace('Gama (Excelsior)', 'Gama').replace(' — Gama', '')
        labels_plot.append(lbl[:55])
        deltas.append(it['delta_pp'])
        ci_lows.append(it['ci_95_low_delta'] if it['ci_95_low_delta'] is not None else it['delta_pp'])
        ci_highs.append(it['ci_95_high_delta'] if it['ci_95_high_delta'] is not None else it['delta_pp'])
        sig = it.get('sig_flag_adjusted', 'no_sig')
        if sig in ('sig_99', 'sig_95'):
            colors.append('#d62728')  # red = significant
        elif sig == 'tendencia_90':
            colors.append('#ff7f0e')  # orange = tendency
        else:
            colors.append('#1f77b4')  # blue = not sig

    n_plot = len(labels_plot)
    fig, ax = plt.subplots(figsize=(12, max(6, n_plot * 0.5 + 2)))

    y_pos = range(n_plot - 1, -1, -1)
    for i, (y, d, lo, hi, c) in enumerate(zip(y_pos, deltas, ci_lows, ci_highs, colors)):
        ax.errorbar(d, y, xerr=[[d - lo], [hi - d]],
                    fmt='o', color=c, capsize=4, linewidth=1.5, markersize=5)

    ax.axvline(0, color='black', linewidth=0.8, linestyle='--', alpha=0.6)
    ax.set_yticks(list(y_pos))
    ax.set_yticklabels(labels_plot, fontsize=8)
    ax.set_xlabel('Delta 2026 vs 2025 (pp)', fontsize=10)
    ax.set_title('Forest Plot — Top cambios WoW Gama 2025↔2026\n(Rojo=sig BH-adj p<0.05, Naranja=tendencia p<0.10, Azul=no sig)',
                 fontsize=10)

    # Legend
    patches = [
        mpatches.Patch(color='#d62728', label='Sig BH-adj p<0.05'),
        mpatches.Patch(color='#ff7f0e', label='Tendencia p<0.10'),
        mpatches.Patch(color='#1f77b4', label='No significativo'),
    ]
    ax.legend(handles=patches, loc='lower right', fontsize=8)
    ax.grid(axis='x', alpha=0.3)

    plt.tight_layout()
    plot_path = os.path.join(OUT_PLOTS, f'wow_top_changes_{FECHA}_{VERSION}.png')
    plt.savefig(plot_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Forest plot guardado: {plot_path}")
else:
    print("  [WARN] No hay items Gama con delta valido para el forest plot.")
    plot_path = None
print()


# ════════════════════════════════════════════════════════════════════════════
# PASO 8: CAVEATS PARA BRUNA
# ════════════════════════════════════════════════════════════════════════════
print("[PASO 8] Generando caveats para Bruna...")

# Collect significant items for hallazgos
sig_items_sorted = sorted(
    [it for it in wow_items if it.get('reject_bh', False) and it['delta_pp'] is not None],
    key=lambda x: abs(x['delta_pp']), reverse=True
)

# Top hallazgos
hallazgos_principales = []
for it in sig_items_sorted[:10]:
    direction = "aumento" if it['delta_pp'] > 0 else "disminucion"
    hallazgos_principales.append({
        "item": it['label'],
        "delta_pp": it['delta_pp'],
        "p_adjusted": it.get('p_adjusted'),
        "sig": it.get('sig_flag_adjusted'),
        "direction": direction,
        "ci_95": [it['ci_95_low_delta'], it['ci_95_high_delta']],
        "est_2026": round(it['estimate_2026'] * 100, 1),
        "est_2025": round(it['estimate_2025'] * 100, 1),
        "nivel_evidencia": "alto" if it.get('sig_flag_adjusted') in ('sig_99', 'sig_95') else "medio",
    })

# Non-sig Gama funnel items (important strategically)
gama_pref_item = next((it for it in wow_items if it['variable_id'] == 'Preferida_P21_Gama_(Excelsior)'), None)
gama_tom_item = next((it for it in wow_items if it['variable_id'] == 'TOM_P16_Gama_(Excelsior)'), None)

# Build caveats list
caveats_bruna = [
    {
        "codigo": "CV-WOW-001",
        "tema": "Ponderacion 2025 no disponible",
        "descripcion": (
            "@PONDERAR_1 en BBDD 2025 = todos ceros. Analisis 2025 es sin ponderar. "
            "Si existia un diseno muestral complejo en 2025, los estimados pueden tener sesgo de diseno."
        ),
        "impacto": "MEDIO",
        "nivel_evidencia": "medio",
        "caveat_deck": (
            "Los resultados 2025 se presentan sin ponderacion muestral (factor de ponderacion no disponible en BBDD)."
        ),
        "claim_permitido": False
    },
    {
        "codigo": "CV-WOW-002",
        "tema": "Comparabilidad muestral",
        "descripcion": (
            f"{n_fail}/4 variables demograficas muestran diferencias estadisticas entre 2025 y 2026 (chi2 p<=0.10). "
            "Los cambios WoW pueden reflejar parcialmente diferencias en composicion muestral."
        ),
        "impacto": "ALTO" if n_fail >= 2 else "MEDIO",
        "nivel_evidencia": "medio",
        "caveat_deck": (
            "Las comparaciones wave-over-wave deben interpretarse con cautela dada la diferencia de "
            "composicion muestral entre olas (n2025=785 vs n2026=402; distribuciones demograficas heterogeneas)."
        ),
        "claim_permitido": False
    },
    {
        "codigo": "CV-WOW-003",
        "tema": "P22 importancia: no comparable a nivel de atributo",
        "descripcion": (
            "BBDD 2025 codifica P22 como P22_1..P22_20 sin etiquetas de texto. "
            "No es posible mapear atributos individuales 2025<->2026 sin diccionario de variables. "
            "Solo se puede comparar T2B promedio agrupado."
        ),
        "impacto": "ALTO",
        "nivel_evidencia": "bajo",
        "caveat_deck": (
            "La comparacion de importancia de atributos (P22) entre 2025 y 2026 no es "
            "posible a nivel de atributo individual. Solo se reporta tendencia general."
        ),
        "claim_permitido": False
    },
    {
        "codigo": "CV-WOW-004",
        "tema": "P23:21 'hacer valer dinero' — nuevo en 2026",
        "descripcion": "El atributo 21 no existe en 2025. No incluir en comparativas WoW.",
        "impacto": "BAJO",
        "nivel_evidencia": "bajo",
        "caveat_deck": "El atributo 'hacer valer mi dinero' fue introducido en 2026. No tiene par en 2025.",
        "claim_permitido": False
    },
    {
        "codigo": "CV-WOW-005",
        "tema": "Analisis de subgrupos es exploratorio",
        "descripcion": (
            "Los subgrupos NSE no fueron pre-registrados en ola 2025. "
            "Interpretar como hipotesis a confirmar en ola 2027."
        ),
        "impacto": "MEDIO",
        "nivel_evidencia": "bajo",
        "caveat_deck": (
            "Los analisis por NSE son exploratorios (no pre-registrados en diseno 2025). "
            "Requieren confirmacion en ola 2027."
        ),
        "claim_permitido": True  # allowed as hypothesis
    },
    {
        "codigo": "CV-WOW-006",
        "tema": "n2026=402 vs n2025=785 — asimetria de precision",
        "descripcion": (
            "La ola 2026 tiene aproximadamente la mitad del n de 2025. "
            "Los IC95 de los estimados 2026 son mas amplios, reduciendo el poder estadistico para detectar cambios."
        ),
        "impacto": "MEDIO",
        "nivel_evidencia": "medio",
        "caveat_deck": (
            "La diferencia de tamanio muestral (2025: n=785; 2026: n=402) implica menor precision "
            "en los estimados 2026. Cambios menores de 5pp pueden no ser detectables."
        ),
        "claim_permitido": True
    },
    {
        "codigo": "CV-WOW-007",
        "tema": "Causalidad no inferible",
        "descripcion": (
            "Los cambios WoW son correlacionales en un diseno cross-sectional. "
            "No se puede atribuir ningun cambio observado a acciones especificas de Gama."
        ),
        "impacto": "MEDIO",
        "nivel_evidencia": "medio",
        "caveat_deck": (
            "Los cambios entre olas son observacionales. No implican causalidad. "
            "No atribuir cambios a acciones especificas sin un diseno cuasi-experimental."
        ),
        "claim_permitido": True
    }
]

print(f"  Caveats para Bruna: {len(caveats_bruna)} items")
print()


# ════════════════════════════════════════════════════════════════════════════
# SERIALIZAR JSON COMPLETO
# ════════════════════════════════════════════════════════════════════════════
print("[Serializando] CU7_wow_results...")

# Compute some summary stats
n_total_items = len(wow_items)
n_sig_items = sum(1 for it in wow_items if it.get('reject_bh', False))
n_tendencia = sum(1 for it in wow_items if it.get('sig_flag_adjusted') == 'tendencia_90')

# P22 T2B summary
likert_map = {'Muy Importante': 5, 'Importante': 4, 'Algo importante': 3, 'Poco importante': 2, 'Nada Importante': 1}
p22_t2b_2026 = {}
for c in p22_cols_26:
    label = c.split('IMPORTANCIA')[-1].strip()[:50] if 'IMPORTANCIA' in c else c[:50]
    t2b = df26[c].astype(str).str.contains('Muy Importante|Importante', na=False).sum() / n26 * 100
    mean = df26[c].map(likert_map).mean()
    p22_t2b_2026[label] = {"t2b_pct": round(t2b, 1), "mean": round(mean, 2)}

p22_t2b_2025 = {}
for i in range(1, 11):  # first 10 as proxy for comparable set
    col = f'P22_{i}'
    if col in df25.columns:
        t2b = df25[col].astype(str).str.contains('Muy Importante|Importante', na=False).sum() / n25 * 100
        mean = df25[col].map(likert_map).mean()
        p22_t2b_2025[f'P22_{i}'] = {"t2b_pct": round(t2b, 1), "mean": round(mean, 2)}

p22_t2b_avg_26 = round(np.mean([v['t2b_pct'] for v in p22_t2b_2026.values()]), 1)
p22_t2b_avg_25 = round(np.mean([v['t2b_pct'] for v in p22_t2b_2025.values()]), 1)

result = {
    "metadata": {
        "proyecto": "Gama Notoriedad 2026",
        "tipo": "CU-7 Wave-over-Wave Analysis",
        "olas_comparadas": "2025 vs 2026",
        "fecha_ejecucion": datetime.datetime.now().isoformat(),
        "n_2026": n26,
        "n_2025": n25,
        "protocolo": "ME-5 Methodology Plan V4 — Methos 2026-05-17",
        "librerias": {
            "pandas": pd.__version__, "numpy": np.__version__,
            "scipy": stats.__version__ if hasattr(stats, '__version__') else "OK",
            "statsmodels": sm.__version__
        }
    },
    "parametros": {
        "alpha_wow": ALPHA_WOW,
        "alpha_comparabilidad_muestral": ALPHA_SAMP,
        "fdr_q": FDR_Q,
        "base_baja": BASE_BAJA,
        "base_min_subgrupo": BASE_MIN_SGR,
        "test_wow": "Newcombe-Wilson (proportion_confint method=wilson + chi2)",
        "correccion_multiple": "Benjamini-Hochberg FDR",
        "ponderacion_2025": pondera_2025,
    },
    "decisions_inflight": decisions_inflight,
    "paso2_comparabilidad_muestral": comparabilidad,
    "paso3_ponderacion": {
        "ponderar_1_min": w_min,
        "ponderar_1_max": w_max,
        "ponderar_1_mean": w_mean,
        "aplicada": pondera_2025,
        "deff_nota": deff_nota
    },
    "paso4_5_wow_items": wow_items,
    "paso5_resumen_bh": {
        "total_items_tested": len(p_values_raw),
        "n_sig_bh_fdr_q05": n_sig_items,
        "n_tendencia_90": n_tendencia,
        "n_no_sig": n_total_items - n_sig_items - n_tendencia
    },
    "paso6_subgrupos": subgroup_results,
    "paso7_forest_plot": {
        "path": str(plot_path) if plot_path else None,
        "n_items_plotted": len(gama_sorted) if gama_sorted else 0,
        "criterio": "Top 15 items con 'Gama' en label, sorted by |delta_pp|"
    },
    "paso8_caveats_bruna": caveats_bruna,
    "hallazgos_principales": hallazgos_principales,
    "p22_importancia_t2b": {
        "nota": "[DECISION D-CU7-002] Solo comparacion agregada T2B — no comparacion individual",
        "t2b_avg_2026": p22_t2b_avg_26,
        "t2b_avg_2025_proxy": p22_t2b_avg_25,
        "delta_avg_pp": round(p22_t2b_avg_26 - p22_t2b_avg_25, 1),
        "detalle_2026": p22_t2b_2026,
        "detalle_2025_P22_1a10": p22_t2b_2025
    },
    "flags": [
        {"codigo": "FLAG-WOW-001", "descripcion": "@PONDERAR_1 = 0 en BBDD 2025. Sin ponderacion.", "severidad": "MEDIO"},
        {"codigo": "FLAG-WOW-002", "descripcion": f"Comparabilidad muestral: {n_fail}/4 variables demograficas difieren (p<=0.10).", "severidad": "ALTO" if n_fail >= 2 else "MEDIO"},
        {"codigo": "FLAG-WOW-003", "descripcion": "P22 atributos individuales NO comparables (sin labels en BBDD 2025).", "severidad": "ALTO"},
        {"codigo": "FLAG-WOW-004", "descripcion": "P23:21 excluido de WoW (nuevo en 2026).", "severidad": "BAJO"},
        {"codigo": "FLAG-WOW-005", "descripcion": "Subgrupos NSE son exploratorios, no pre-registrados.", "severidad": "MEDIO"},
    ]
}

json_path = os.path.join(OUT_JSON, f'CU7_wow_results_{FECHA}_{VERSION}.json')
dump_json(result, json_path, indent=2)
print(f"  JSON: {json_path}")
print()

print(f"[CU-7 WoW] COMPLETADO — {datetime.datetime.now().isoformat()}")
print(f"  Items WoW: {n_total_items} | Sig BH-FDR: {n_sig_items} | Tendencia: {n_tendencia}")
print(f"  Outputs:")
print(f"    JSON  -> {json_path}")
print(f"    Plot  -> {plot_path}")
print(f"    CSV   -> {csv_path}")

if __name__ == "__main__":
    pass
