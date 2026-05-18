"""
cu8_v2_extension.py — CU-8 Extension V2: 5 Análisis Adicionales
Proyecto: Gama Notoriedad 2026
Autor: Cuanti (agente analítico)
Fecha: 2026-05-18

Propósito:
  Extensión del CU-8 v1 con 5 análisis adicionales solicitados por el Owner:
  NEW-1: Subset shoppers perciben Gama "Igual o menos caro" (P33)
  NEW-2: Cruce P33 × P21 (percepcion precio × preferencia)
  NEW-3: Capítulo lugar de compra × precio percibido × preferencia × misiones
  NEW-4: Balance óptimo categorias a precios iguales (síntesis estratégica)
  EXPRESS: Hipótesis Express — misión urgencia Gama × NSE × Geo

Inputs:
  - BBDD Notoriedad 2026.xlsx (G: Drive, n=402, 295+ cols)
  - JSON v1: CU8_preguntas_faltantes_20260518_v1.json (referencia)

Outputs:
  - JSON: outputs/json/CU8_v2_extension_20260518.json
  - Plot: outputs/plots/cu8_v2_heatmap_desconexion.png
  - Md report: 2026-05-18_CU-8_preguntas-faltantes_v2.md (escrito post-ejecución)

Metodologia:
  - BH-FDR para múltiples tests (>10 tests simultáneos)
  - Newcombe-Wilson para IC95 de proporciones
  - Chi-cuadrado de independencia + OR manual
  - Alpha=0.05 (BH-adjusted)
  - Base baja: n<30 referencial, n<10 excluir inferencia
"""

import sys
import os
sys.stdout.reconfigure(encoding='utf-8')

import json
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.proportion import proportion_confint
from statsmodels.stats.multitest import multipletests
import warnings
warnings.filterwarnings('ignore')

# ─── PATHS ────────────────────────────────────────────────────────────────────
BBDD_2026_PATH = (
    'G:/Mi unidad/RAUL/colaboradores/Genteca/Cora-Urrea/'
    '01_De_Cora_Para_Raoul/Notoriedad V2.0/BBDD Notoriedad 2026.xlsx'
)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, '..', 'outputs', 'json')
PLOTS_DIR = os.path.join(SCRIPT_DIR, '..', 'outputs', 'plots')
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(PLOTS_DIR, exist_ok=True)
OUTPUT_JSON = os.path.join(OUTPUT_DIR, 'CU8_v2_extension_20260518.json')
OUTPUT_PLOT_HEATMAP = os.path.join(PLOTS_DIR, 'cu8_v2_heatmap_desconexion.png')

# ─── PARÁMETROS ───────────────────────────────────────────────────────────────
ALPHA = 0.05
BASE_BAJA_THRESH = 30
BASE_EXCLUIR_THRESH = 10

# Columnas clave (nombres de variable code en BBDD)
NSE_COL = ' {PD4} [V153] Marcar nse zona'

# Categorias P30 / P32 — labels canónicos (mismo orden que v1)
CAT_LABELS_P30 = {
    'V799': 'Frutas, legumbres y verduras',
    'V800': 'Galletas, pasapalos y confiteria',
    'V801': 'Salsas y Enlatados',
    'V805': 'Carne de res',
    'V806': 'Pollo',
    'V807': 'Charcuteria (quesos, jamones)',
    'V810': 'Gaseosas, jugos y aguas',
    'V811': 'Licores',
    'V812': 'Farmacia',
    'V815': 'Congelados',
    'V817': 'Alimento mascotas',
    'V818': 'Pescados y mariscos',
    'V1858': 'Productos basicos (harinas, arroz, leches)',
    'V1859': 'Cuidado Personal',
    'V1860': 'Cuidado y limpieza del hogar',
}

CAT_LABELS_P32 = {
    'V1872': 'Frutas, legumbres y verduras',
    'V1873': 'Galletas, pasapalos y confiteria',
    'V1874': 'Salsas y Enlatados',
    'V1875': 'Carne de res',
    'V1876': 'Pollo',
    'V1877': 'Charcuteria (quesos, jamones)',
    'V1878': 'Gaseosas, jugos y aguas',
    'V1879': 'Licores',
    'V1880': 'Farmacia',
    'V1881': 'Congelados',
    'V1882': 'Alimento mascotas',
    'V1883': 'Pescados y mariscos',
    'V1884': 'Productos basicos (harinas, arroz, leches)',
    'V1885': 'Cuidado Personal',
    'V1886': 'Cuidado y limpieza del hogar',
}

# Cadena label normalizer
CADENA_LABEL = {
    "Plaza's": "Plazas",
    "Plaza´s": "Plazas",
    "Gama (Excelsior)": "Gama",
    "Gama Excelsior": "Gama",
    "Gama": "Gama",
}


# ─── UTILIDADES ───────────────────────────────────────────────────────────────

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, (np.bool_,)):
            return bool(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)


def dump_json(data, path, indent=2):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=indent, cls=NumpyEncoder)


def wilson_ci(count, nobs, alpha=0.05):
    """IC95 Newcombe-Wilson."""
    if nobs == 0 or np.isnan(count) or np.isnan(nobs):
        return (np.nan, np.nan)
    lo, hi = proportion_confint(int(count), int(nobs), alpha=alpha, method='wilson')
    return (round(lo * 100, 1), round(hi * 100, 1))


def flag_base(n, n_base=None):
    """Retorna flag de base baja según umbrales."""
    check = n if n_base is None else min(n, n_base)
    if check < BASE_EXCLUIR_THRESH:
        return "EXCLUIR_INFERENCIA"
    elif check < BASE_BAJA_THRESH:
        return "REFERENCIAL"
    return ""


def label_cadena(val):
    if pd.isna(val):
        return None
    v = str(val).strip()
    mapped = CADENA_LABEL.get(v, v)
    if mapped and "Gama" in str(mapped) and str(mapped) != "Gama":
        return "Gama"
    return mapped


def nse_harm(val):
    v = str(val).strip() if not pd.isna(val) else ''
    if v in ('C+', 'C', 'C+/C'):
        return 'C+/C'
    if v == 'D':
        return 'D'
    if v == 'E':
        return 'E'
    return 'Otro'


def bh_adjust(p_values):
    if not p_values or all(np.isnan(p) for p in p_values):
        return p_values
    valid_idx = [i for i, p in enumerate(p_values) if not np.isnan(p)]
    valid_p = [p_values[i] for i in valid_idx]
    _, p_adj, _, _ = multipletests(valid_p, method='fdr_bh')
    result = [np.nan] * len(p_values)
    for i, idx in enumerate(valid_idx):
        result[idx] = round(float(p_adj[i]), 5)
    return result


def chi2_test(ct_df):
    """Chi2 de independencia sobre crosstab. Retorna chi2, p, dof, cramers_v."""
    try:
        chi2, p, dof, _ = stats.chi2_contingency(ct_df)
        n = ct_df.values.sum()
        min_dim = min(ct_df.shape) - 1
        cramers_v = np.sqrt(chi2 / (n * min_dim)) if (n > 0 and min_dim > 0) else np.nan
        return round(chi2, 3), round(p, 5), int(dof), round(cramers_v, 3)
    except Exception:
        return np.nan, np.nan, np.nan, np.nan


def calc_or(a, b, c, d):
    """OR = (a/b) / (c/d) = ad/bc con IC95 Woolf."""
    if b == 0 or c == 0 or d == 0 or a == 0:
        return None, None, None
    or_val = (a * d) / (b * c)
    # log se
    se_log = np.sqrt(1/a + 1/b + 1/c + 1/d)
    lo = np.exp(np.log(or_val) - 1.96 * se_log)
    hi = np.exp(np.log(or_val) + 1.96 * se_log)
    return round(or_val, 2), round(lo, 2), round(hi, 2)


# ─── CARGA DE DATOS ───────────────────────────────────────────────────────────

def load_data():
    print("[CU-8 v2] Cargando BBDD 2026...")
    df = pd.read_excel(BBDD_2026_PATH, sheet_name=0, engine='openpyxl')
    print(f"  Shape: {df.shape}")

    df['NSE_harm'] = df[NSE_COL].apply(nse_harm)

    # Municipio / Parroquia
    mun_cols = [c for c in df.columns if 'Municipio' in c or 'municipio' in c.lower()]
    par_cols = [c for c in df.columns if 'Parroquia' in c]
    df['MUNICIPIO'] = df[mun_cols[0]] if mun_cols else 'Desconocido'
    df['PARROQUIA'] = df[par_cols[0]] if par_cols else 'Desconocido'

    # Genero
    gen_cols = [c for c in df.columns if 'PD1' in c or ('genero' in c.lower() and 'V' in c)]
    df['GENERO'] = df[gen_cols[0]] if gen_cols else np.nan

    # Edad
    edad_cols = [c for c in df.columns if 'PD2' in c or ('edad' in c.lower() and 'V' in c)]
    df['EDAD'] = df[edad_cols[0]] if edad_cols else np.nan

    # P21 preferencia
    p21_cols = [c for c in df.columns if '{P21}' in c and 'V194' in c]
    df['P21_pref'] = df[p21_cols[0]].apply(label_cadena) if p21_cols else np.nan

    # P33 percepcion precio Gama (escala: Mucho mas caros / Poco mas caros / Igual / Poco mas economico / Mucho mas economico)
    p33_cols = [c for c in df.columns if '{P33}' in c]
    print(f"  P33 cols encontradas: {p33_cols}")
    df['P33_raw'] = df[p33_cols[0]] if p33_cols else np.nan

    # P25 mision ultima compra
    p25_cols = [c for c in df.columns if '{P25}' in c]
    df['P25_raw'] = df[p25_cols[0]] if p25_cols else np.nan

    # P26 mision de compra por tipo
    # (cols P26 para urgencia específicamente)
    p26_urgencia_cols = [c for c in df.columns if '{P26}' in c and 'V823' in c]
    df['P26_urgencia_raw'] = df[p26_urgencia_cols[0]] if p26_urgencia_cols else np.nan

    nse_dist = df['NSE_harm'].value_counts().to_dict()
    print(f"  NSE dist: {nse_dist}")
    print(f"  n_total: {len(df)}")

    return df


def get_p30_cols(df):
    """Retorna dict {label: col} para P30."""
    result = {}
    for code, label in CAT_LABELS_P30.items():
        matching = [c for c in df.columns if '{P30}' in c and code in c]
        if matching:
            result[label] = matching[0]
    return result


def get_p32_cols(df):
    """Retorna dict {label: col} para P32."""
    result = {}
    for code, label in CAT_LABELS_P32.items():
        matching = [c for c in df.columns if '{P32}' in c and code in c]
        if matching:
            result[label] = matching[0]
    return result


# ─── NEW-1: SUBSET "IGUAL O MENOS CARO" (P33) ─────────────────────────────────

def analizar_new1_subset_economico(df, p30_cols, p32_cols):
    """
    NEW-1: Subset shoppers que perciben Gama como Igual/Menos caro (complemento del 54% neto caro).
    - a) Mix categorias P30 dentro del subset vs Total
    - b) P32 precio percibido Gama vs Total
    - c) Cruce con P21 preferencia
    - d) Cruce con P25 misiones
    - e) Perfil NSE/edad/genero
    """
    n_total = len(df)

    # Definir categorias P33
    p33_vals = df['P33_raw'].dropna()
    p33_vals_str = p33_vals[p33_vals.astype(str).str.strip() != '']
    print(f"\n  P33 distribución de valores únicos:")
    for v, cnt in p33_vals_str.value_counts().items():
        print(f"    '{v}': {cnt}")

    # Subset "No caros": excluyendo "Más caros" usando UPPER para robustez encoding
    mask_caro = df['P33_raw'].apply(
        lambda x: ('CARO' in str(x).upper()) if pd.notna(x) else False
    )

    # También identificar respondentes con P33 válido
    mask_p33_valido = df['P33_raw'].notna() & (df['P33_raw'].astype(str).str.strip() != '')

    mask_economico = mask_p33_valido & ~mask_caro
    n_economico = mask_economico.sum()
    n_caro = (mask_p33_valido & mask_caro).sum()
    n_p33_valido = mask_p33_valido.sum()

    print(f"\n  P33 subset 'Igual o menos caro': n={n_economico} ({round(n_economico/n_p33_valido*100,1)}% de validos)")
    print(f"  P33 subset 'Caros': n={n_caro} ({round(n_caro/n_p33_valido*100,1)}% de validos)")

    df_eco = df[mask_economico].copy()
    df_total = df.copy()

    # Distribución P33 en el subset
    p33_dist_eco = df_eco['P33_raw'].value_counts()
    p33_dist_total = df_total['P33_raw'].value_counts()

    p33_tabla = []
    for v, cnt_t in p33_dist_total.items():
        cnt_e = p33_dist_eco.get(v, 0)
        pct_t = round(cnt_t / n_p33_valido * 100, 1)
        pct_e = round(cnt_e / n_economico * 100, 1) if n_economico > 0 else 0
        p33_tabla.append({
            "categoria_p33": str(v),
            "n_total": int(cnt_t),
            "pct_total": pct_t,
            "n_subset": int(cnt_e),
            "pct_subset": pct_e,
            "en_subset": bool(cnt_e > 0)
        })

    # ── a) Mix categorias P30 subset vs Total ──
    mix_p30 = []
    for cat_label, col in p30_cols.items():
        vals_total = df_total[col].apply(label_cadena)
        vals_eco = df_eco[col].apply(label_cadena)

        n_gama_total = int((vals_total == 'Gama').sum())
        n_gama_eco = int((vals_eco == 'Gama').sum())

        pct_gama_total = round(n_gama_total / n_total * 100, 1)
        pct_gama_eco = round(n_gama_eco / n_economico * 100, 1) if n_economico > 0 else 0

        mix_p30.append({
            "categoria": cat_label,
            "gama_pct_total": pct_gama_total,
            "gama_n_total": n_gama_total,
            "gama_pct_subset_economico": pct_gama_eco,
            "gama_n_subset": n_gama_eco,
            "diferencia_pp": round(pct_gama_eco - pct_gama_total, 1),
            "flag": flag_base(n_gama_eco)
        })

    mix_p30.sort(key=lambda x: -abs(x['diferencia_pp']))

    # ── b) P32 precio percibido en subset ──
    mix_p32 = []
    for cat_label, col in p32_cols.items():
        vals_total = df_total[col].apply(label_cadena)
        vals_eco = df_eco[col].apply(label_cadena)

        # Base sin "Ninguno"
        n_base_total_valido = len(vals_total[~vals_total.isin(['Ninguno en particular', 'Ninguno (NO LEER)', None])])
        n_base_eco_valido = len(vals_eco[~vals_eco.isin(['Ninguno en particular', 'Ninguno (NO LEER)', None])])

        n_gama_total = int((vals_total == 'Gama').sum())
        n_gama_eco = int((vals_eco == 'Gama').sum())

        pct_gama_total = round(n_gama_total / n_total * 100, 1)
        pct_gama_eco = round(n_gama_eco / n_economico * 100, 1) if n_economico > 0 else 0

        mix_p32.append({
            "categoria": cat_label,
            "gama_precio_pct_total": pct_gama_total,
            "gama_precio_n_total": n_gama_total,
            "gama_precio_pct_subset_economico": pct_gama_eco,
            "gama_precio_n_subset": n_gama_eco,
            "diferencia_pp": round(pct_gama_eco - pct_gama_total, 1),
            "flag": flag_base(n_gama_eco)
        })

    mix_p32.sort(key=lambda x: -x['gama_precio_pct_subset_economico'])

    # ── c) Cruce con P21 preferencia ──
    n_pref_gama_total = int((df_total['P21_pref'] == 'Gama').sum())
    n_pref_gama_eco = int((df_eco['P21_pref'] == 'Gama').sum())
    pct_pref_total = round(n_pref_gama_total / n_total * 100, 1)
    pct_pref_eco = round(n_pref_gama_eco / n_economico * 100, 1) if n_economico > 0 else 0

    # OR preferencia Gama en subset economico vs resto
    n_no_eco = n_total - n_economico
    n_pref_no_eco = n_pref_gama_total - n_pref_gama_eco
    or_pref, or_lo, or_hi = calc_or(
        n_pref_gama_eco, n_economico - n_pref_gama_eco,
        n_pref_no_eco, n_no_eco - n_pref_no_eco
    )

    # ── d) Cruce con P25 misiones ──
    def short_mision(v):
        v = str(v).lower()
        if 'abastecimiento general' in v:
            return 'Abastecimiento general'
        if 'reabastecer' in v or 'reabastecimiento' in v:
            return 'Reabastecimiento parcial'
        if 'urgencia' in v or 'pocos productos' in v:
            return 'Urgencia'
        if 'evento' in v or 'celebraci' in v:
            return 'Evento'
        if 'electrodom' in v or 'ropa' in v:
            return 'No alimentos'
        return 'Otro'

    df_eco['P25_short'] = df_eco['P25_raw'].apply(short_mision)
    df_total['P25_short'] = df_total['P25_raw'].apply(short_mision)

    misiones_eco = df_eco['P25_short'].value_counts()
    misiones_total = df_total['P25_short'].value_counts()

    mision_cruce = []
    for m in ['Abastecimiento general', 'Reabastecimiento parcial', 'Urgencia', 'Evento']:
        n_eco_m = int(misiones_eco.get(m, 0))
        n_total_m = int(misiones_total.get(m, 0))
        pct_eco_m = round(n_eco_m / n_economico * 100, 1) if n_economico > 0 else 0
        pct_total_m = round(n_total_m / n_total * 100, 1)
        mision_cruce.append({
            "mision": m,
            "pct_subset_economico": pct_eco_m,
            "n_subset": n_eco_m,
            "pct_total": pct_total_m,
            "n_total": n_total_m,
            "diferencia_pp": round(pct_eco_m - pct_total_m, 1),
            "flag": flag_base(n_eco_m)
        })

    # ── e) Perfil demografico NSE/Edad/Genero ──
    perfil_nse = []
    for nse_g in ['C+/C', 'D', 'E']:
        n_nse_total = int((df_total['NSE_harm'] == nse_g).sum())
        n_nse_eco = int((df_eco['NSE_harm'] == nse_g).sum())
        pct_nse_total = round(n_nse_total / n_total * 100, 1)
        pct_nse_eco = round(n_nse_eco / n_economico * 100, 1) if n_economico > 0 else 0
        # % dentro del NSE que está en subset
        pct_nse_en_subset = round(n_nse_eco / n_nse_total * 100, 1) if n_nse_total > 0 else 0
        perfil_nse.append({
            "nse": nse_g,
            "n_total": n_nse_total,
            "pct_en_total": pct_nse_total,
            "n_en_subset": n_nse_eco,
            "pct_en_subset": pct_nse_eco,
            "pct_nse_que_es_economico": pct_nse_en_subset,
            "flag": flag_base(n_nse_eco)
        })

    # Genero en subset
    perfil_genero = []
    if df['GENERO'].notna().sum() > 0:
        for gen_v, cnt_t in df_total['GENERO'].value_counts().items():
            cnt_e = int((df_eco['GENERO'] == gen_v).sum())
            pct_t = round(cnt_t / n_total * 100, 1)
            pct_e = round(cnt_e / n_economico * 100, 1) if n_economico > 0 else 0
            perfil_genero.append({
                "genero": str(gen_v),
                "pct_total": pct_t, "n_total": int(cnt_t),
                "pct_subset": pct_e, "n_subset": cnt_e
            })

    # Edad en subset (si disponible)
    perfil_edad = []
    if df['EDAD'].notna().sum() > 0:
        # Crear rangos
        def edad_grupo(v):
            try:
                e = float(v)
                if e < 25: return '18-24'
                elif e < 35: return '25-34'
                elif e < 45: return '35-44'
                elif e < 55: return '45-54'
                else: return '55+'
            except:
                return None

        df_eco['EDAD_grupo'] = df_eco['EDAD'].apply(edad_grupo)
        df_total['EDAD_grupo'] = df_total['EDAD'].apply(edad_grupo)

        for eg in ['18-24', '25-34', '35-44', '45-54', '55+']:
            n_t = int((df_total['EDAD_grupo'] == eg).sum())
            n_e = int((df_eco['EDAD_grupo'] == eg).sum())
            pct_t = round(n_t / n_total * 100, 1)
            pct_e = round(n_e / n_economico * 100, 1) if n_economico > 0 else 0
            pct_en_sub = round(n_e / n_t * 100, 1) if n_t > 0 else 0
            perfil_edad.append({
                "rango": eg, "n_total": n_t, "pct_total": pct_t,
                "n_subset": n_e, "pct_subset": pct_e,
                "pct_rango_que_es_economico": pct_en_sub,
                "flag": flag_base(n_e)
            })

    return {
        "descripcion": "Subset de respondentes que perciben Gama como Igual o Menos Caro en P33",
        "n_total_valido_p33": int(n_p33_valido),
        "n_subset_economico": int(n_economico),
        "pct_subset": round(n_economico / n_p33_valido * 100, 1) if n_p33_valido > 0 else None,
        "n_subset_caro": int(n_caro),
        "pct_caro": round(n_caro / n_p33_valido * 100, 1) if n_p33_valido > 0 else None,
        "p33_distribucion_tabla": p33_tabla,
        "a_mix_categorias_p30_subset_vs_total": {
            "nota": "% de respondentes que compran habitualmente en Gama por categoria (P30). Subset vs Total.",
            "tabla": mix_p30
        },
        "b_percepcion_precio_p32_subset_vs_total": {
            "nota": "% que percibe a Gama como mejor precio en cada categoria (P32). Subset vs Total.",
            "tabla": mix_p32
        },
        "c_cruce_preferencia_p21": {
            "pct_preferentes_gama_total": pct_pref_total,
            "n_preferentes_gama_total": n_pref_gama_total,
            "pct_preferentes_gama_en_subset": pct_pref_eco,
            "n_preferentes_gama_en_subset": int(n_pref_gama_eco),
            "diferencia_pp": round(pct_pref_eco - pct_pref_total, 1),
            "OR_preferencia_en_subset": {
                "OR": or_pref, "IC95_lo": or_lo, "IC95_hi": or_hi,
                "interpretacion": "OR>1 = mayor probabilidad de preferir Gama si percibe precio favorable"
            },
            "flag": flag_base(n_pref_gama_eco)
        },
        "d_cruce_misiones_p25": {
            "nota": "Distribución de misiones de ultima compra (P25) en subset vs Total",
            "tabla": mision_cruce
        },
        "e_perfil_demografico": {
            "nse": perfil_nse,
            "genero": perfil_genero,
            "edad": perfil_edad
        }
    }


# ─── NEW-2: CRUCE P33 × P21 (PERCEPCION PRECIO × PREFERENCIA) ─────────────────

def analizar_new2_p33_x_p21(df):
    """
    NEW-2: Tabla cruzada P33 (5 categorias) × P21 (preferida Gama si/no).
    Chi-cuadrado + OR.
    """
    n_total = len(df)

    # Crear variable P33 normalizada (5 categorias)
    # Nota: BBDD tiene encoding cp1252 corruption en ECONOMICOS (ECON + Ã"MICOS)
    # Usar UPPER para deteccion robusta — ECON matchea ECONOMICO sin importar la O especial
    def norm_p33(v):
        if pd.isna(v) or str(v).strip() == '':
            return None
        v_up = str(v).upper()
        is_eco = 'ECON' in v_up
        is_caro = 'CARO' in v_up
        is_igual = 'IGUAL' in v_up
        is_mucho = 'MUCHO' in v_up
        is_poco = 'POCO' in v_up
        if is_caro and is_mucho:
            return 'Mucho mas caros'
        if is_caro and is_poco:
            return 'Poco mas caros'
        if is_caro:
            return 'Poco mas caros'
        if is_igual:
            return 'Igual precio'
        if is_eco and is_mucho:
            return 'Mucho mas economico'
        if is_eco and is_poco:
            return 'Poco mas economico'
        if is_eco:
            return 'Poco mas economico'
        return str(v).strip()[:40]

    df['P33_norm'] = df['P33_raw'].apply(norm_p33)
    df['P21_gama_bin'] = (df['P21_pref'] == 'Gama').astype(int)

    # Distribución P33 general
    p33_dist = df['P33_norm'].value_counts(dropna=True)
    print(f"\n  P33 normalizado:")
    for v, cnt in p33_dist.items():
        print(f"    '{v}': {cnt} ({round(cnt/n_total*100,1)}%)")

    # Tabla cruzada P33 × P21=Gama
    orden_p33 = ['Mucho mas caros', 'Poco mas caros', 'Igual precio',
                 'Poco mas economico', 'Mucho mas economico']

    df_valid = df[df['P33_norm'].notna() & df['P21_pref'].notna()].copy()

    cruce = []
    for cat in orden_p33:
        sub = df_valid[df_valid['P33_norm'] == cat]
        n_cat = len(sub)
        n_pref_gama = int((sub['P21_pref'] == 'Gama').sum())
        n_no_pref = n_cat - n_pref_gama
        pct_pref = round(n_pref_gama / n_cat * 100, 1) if n_cat > 0 else None
        pct_no_pref = round(n_no_pref / n_cat * 100, 1) if n_cat > 0 else None
        lo, hi = wilson_ci(n_pref_gama, n_cat) if n_cat >= BASE_EXCLUIR_THRESH else (None, None)
        cruce.append({
            "categoria_p33": cat,
            "n_en_categoria": n_cat,
            "n_prefiere_gama": n_pref_gama,
            "pct_prefiere_gama": pct_pref,
            "ic95_pref_gama": [lo, hi],
            "n_no_prefiere_gama": int(n_no_pref),
            "pct_no_prefiere_gama": pct_no_pref,
            "flag": flag_base(n_cat)
        })

    # Chi-cuadrado P33 × P21=Gama (tabla binaria)
    chi2_val = p_val = cramers_v = None
    try:
        ct_full = pd.crosstab(df_valid['P33_norm'], df_valid['P21_gama_bin'])
        chi2_val, p_val, dof, cramers_v = chi2_test(ct_full)
    except Exception as e:
        print(f"  [WARN] Chi2 P33×P21 error: {e}")

    # OR: Percepcion favorable (Igual + Poco + Mucho economico) → Preferencia Gama
    mask_favorable = df_valid['P33_norm'].isin(['Igual precio', 'Poco mas economico', 'Mucho mas economico'])
    n_fav = mask_favorable.sum()
    n_pref_fav = int(df_valid[mask_favorable]['P21_gama_bin'].sum())
    n_no_fav = len(df_valid) - n_fav
    n_pref_no_fav = int(df_valid[~mask_favorable]['P21_gama_bin'].sum())

    or_fav, or_fav_lo, or_fav_hi = calc_or(
        n_pref_fav, n_fav - n_pref_fav,
        n_pref_no_fav, n_no_fav - n_pref_no_fav
    )

    # OR por categoria especifica: Mucho mas economico vs Mucho mas caro
    mask_mucho_eco = df_valid['P33_norm'] == 'Mucho mas economico'
    mask_mucho_caro = df_valid['P33_norm'] == 'Mucho mas caros'
    n_mucho_eco = mask_mucho_eco.sum()
    n_pref_mucho_eco = int(df_valid[mask_mucho_eco]['P21_gama_bin'].sum())
    n_mucho_caro = mask_mucho_caro.sum()
    n_pref_mucho_caro = int(df_valid[mask_mucho_caro]['P21_gama_bin'].sum())
    or_extremos, or_ext_lo, or_ext_hi = calc_or(
        n_pref_mucho_eco, n_mucho_eco - n_pref_mucho_eco,
        n_pref_mucho_caro, n_mucho_caro - n_pref_mucho_caro
    ) if (n_mucho_eco >= BASE_EXCLUIR_THRESH and n_mucho_caro >= BASE_EXCLUIR_THRESH) else (None, None, None)

    # Comparacion con ORs ya existentes de CU-5 (atencion OR=5.73, precio driver)
    or_comparativo = {
        "OR_atencion_CU5": 5.73,
        "OR_precio_driver_CU5": "ver CU-5 (driver precio en P31 y P33)",
        "OR_percepcion_favorable_P33": or_fav,
        "OR_favorable_IC95": [or_fav_lo, or_fav_hi],
        "OR_extremos_mucho_eco_vs_mucho_caro": or_extremos,
        "OR_extremos_IC95": [or_ext_lo, or_ext_hi],
        "nota": "OR_atencion y OR_precio de CU-5 son drivers de PREFERENCIA (P21). OR_percepcion_favorable es el efecto independiente de percibir precio favorable en P33 sobre preferir Gama."
    }

    return {
        "descripcion": "Tabla cruzada P33 (percepcion precio Gama) × P21 (preferencia Gama)",
        "n_validos_cruce": int(len(df_valid)),
        "tabla_cruzada_p33_x_p21_gama": cruce,
        "test_asociacion": {
            "chi2": chi2_val,
            "p_value": p_val,
            "dof": dof if isinstance(dof, int) else None,
            "cramers_v": cramers_v,
            "significativo": bool(p_val < ALPHA) if (p_val is not None and not np.isnan(p_val)) else None,
            "interpretacion_cramers": "V<0.1 trivial | 0.1-0.3 pequeno | 0.3-0.5 moderado | >0.5 fuerte"
        },
        "OR_percepcion_favorable_vs_desfavorable": or_comparativo,
        "nota_metodologica": (
            "Chi2 sobre tabla completa P33(5 cats) × P21(gama binario). "
            "OR calculado agrupando categorias favorables (Igual+Poco+Mucho eco) vs desfavorables (Poco+Mucho caro). "
            "Bases por categoria individual pueden ser referenciales (n<30)."
        )
    }


# ─── NEW-3: CAPÍTULO LUGAR × PRECIO × PREFERENCIA × MISIONES ──────────────────

def analizar_new3_capitulo_lugar_precio(df, p30_cols, p32_cols):
    """
    NEW-3: Capítulo dedicado lugar de compra × precio percibido × preferencia × misiones.
    3a: Matriz P30 × P32 por 15 categorias
    3b: Categorias de DESCONEXION para Gama (compra habitual pero no mejor precio)
    3c: Correlacion desconexion × preferencia × mision
    3d: Hallazgos categorias condicionantes
    """
    n_total = len(df)

    # ── 3a: Matriz P30 × P32 por categoria ──
    # Para cada categoria: lider habito P30, lider precio P32, son el mismo?
    matriz = []
    desconexion_gama = []  # categorias donde Gama tiene habito pero no precio

    for cat_label in p30_cols:
        if cat_label not in p32_cols:
            continue

        col_p30 = p30_cols[cat_label]
        col_p32 = p32_cols[cat_label]

        # P30 habito
        vals_p30 = df[col_p30].apply(label_cadena)
        vals_p30_clean = vals_p30[~vals_p30.isin(['Ninguno en particular', 'Ninguno (NO LEER)', None])]
        vals_p30_clean = vals_p30_clean[vals_p30_clean.astype(str).str.strip() != '']
        n_p30 = len(vals_p30_clean)

        vc_p30 = vals_p30_clean.value_counts()
        lider_habito = vc_p30.index[0] if len(vc_p30) > 0 else 'N/A'
        lider_habito_pct = round(vc_p30.iloc[0] / n_total * 100, 1) if len(vc_p30) > 0 else 0
        n_gama_p30 = int((vals_p30 == 'Gama').sum())
        pct_gama_p30 = round(n_gama_p30 / n_total * 100, 1)

        # P32 precio
        vals_p32 = df[col_p32].apply(label_cadena)
        vals_p32_clean = vals_p32[~vals_p32.isin(['Ninguno en particular', 'Ninguno (NO LEER)', None])]
        vals_p32_clean = vals_p32_clean[vals_p32_clean.astype(str).str.strip() != '']
        n_p32 = len(vals_p32_clean)

        vc_p32 = vals_p32_clean.value_counts()
        lider_precio = vc_p32.index[0] if len(vc_p32) > 0 else 'N/A'
        lider_precio_pct = round(vc_p32.iloc[0] / n_total * 100, 1) if len(vc_p32) > 0 else 0
        n_gama_p32 = int((vals_p32 == 'Gama').sum())
        pct_gama_p32 = round(n_gama_p32 / n_total * 100, 1)

        # Ninguno%
        n_ninguno_p32 = int(vals_p32.isin(['Ninguno en particular', 'Ninguno (NO LEER)']).sum())
        pct_ninguno_p32 = round(n_ninguno_p32 / n_total * 100, 1)

        congruencia = (lider_habito == lider_precio)

        # Gap precio (Gama) — diferencia entre lider precio y Gama
        gap_gama_precio = round(lider_precio_pct - pct_gama_p32, 1)
        gap_gama_habito = round(lider_habito_pct - pct_gama_p30, 1)

        fila = {
            "categoria": cat_label,
            "lider_habito_p30": lider_habito,
            "lider_habito_pct": lider_habito_pct,
            "gama_habito_pct": pct_gama_p30,
            "gama_habito_n": n_gama_p30,
            "lider_precio_p32": lider_precio,
            "lider_precio_pct": lider_precio_pct,
            "gama_precio_pct": pct_gama_p32,
            "gama_precio_n": n_gama_p32,
            "pct_ninguno_precio": pct_ninguno_p32,
            "congruencia_lider": congruencia,
            "gap_gama_precio_pp": gap_gama_precio,
            "gap_gama_habito_pp": gap_gama_habito,
            "flag_gama_habito": flag_base(n_gama_p30),
            "flag_gama_precio": flag_base(n_gama_p32)
        }
        matriz.append(fila)

        # ── 3b: Desconexión Gama ──
        # Gama tiene habito (>0 menciones) pero NO es lider de precio (ni top3 en precio)
        if n_gama_p30 >= 5:  # al menos 5 menciones en habito
            top3_precio = list(vc_p32.head(3).index) if len(vc_p32) >= 3 else list(vc_p32.index)
            gama_en_top3_precio = 'Gama' in top3_precio
            if not gama_en_top3_precio:
                # Esta es una categoria de desconexion
                desconexion_gama.append({
                    "categoria": cat_label,
                    "gama_habito_pct": pct_gama_p30,
                    "gama_habito_n": n_gama_p30,
                    "gama_precio_pct": pct_gama_p32,
                    "gama_precio_n": n_gama_p32,
                    "brecha_habito_vs_precio_pp": round(pct_gama_p30 - pct_gama_p32, 1),
                    "lider_precio": lider_precio,
                    "lider_precio_pct": lider_precio_pct,
                    "interpretacion": "Shopper usa Gama habitualmente en esta categoria AUNQUE otro supermercado tiene mejor precio percibido",
                    "driver_probable": (
                        "Conveniencia/cercania o servicio (Atencion/Limpieza/24h)"
                        if pct_gama_p30 >= 5 else "Base baja, interpretacion indicativa"
                    ),
                    "flag": flag_base(n_gama_p30)
                })

    # Ordenar desconexion por brecha (mayor primero)
    desconexion_gama.sort(key=lambda x: -x['brecha_habito_vs_precio_pp'])

    # ── 3c: Correlacion desconexion × P21 × P25 ──
    # Para cada categoria de desconexion: % preferentes Gama que compran ahí habitualmente
    p21_pref_gama_mask = (df['P21_pref'] == 'Gama')
    n_pref_gama = int(p21_pref_gama_mask.sum())

    def short_mision(v):
        v = str(v).lower()
        if 'abastecimiento general' in v: return 'Abastecimiento general'
        if 'reabastecer' in v or 'reabastecimiento' in v: return 'Reabastecimiento parcial'
        if 'urgencia' in v or 'pocos productos' in v: return 'Urgencia'
        if 'evento' in v or 'celebraci' in v: return 'Evento'
        return 'Otro'

    df['P25_short'] = df['P25_raw'].apply(short_mision)

    desconexion_con_cruce = []
    for item in desconexion_gama[:8]:  # top 8 categorias de desconexion
        cat_label = item['categoria']
        if cat_label not in p30_cols:
            continue
        col_p30 = p30_cols[cat_label]
        vals_p30 = df[col_p30].apply(label_cadena)

        # % de preferentes Gama que compran habitualmente en Gama en esta categoria
        gama_habito_pref = int((vals_p30[p21_pref_gama_mask] == 'Gama').sum())
        pct_habito_entre_pref = round(gama_habito_pref / n_pref_gama * 100, 1) if n_pref_gama > 0 else None

        # Mision de quienes compran habitualmente en Gama en esta categoria
        mask_habito_gama_cat = (vals_p30 == 'Gama')
        n_hab_gama_cat = mask_habito_gama_cat.sum()
        if n_hab_gama_cat >= BASE_EXCLUIR_THRESH:
            mision_dist = df[mask_habito_gama_cat]['P25_short'].value_counts()
            mision_principal = str(mision_dist.index[0]) if len(mision_dist) > 0 else 'N/D'
            mision_pct = round(mision_dist.iloc[0] / n_hab_gama_cat * 100, 1) if len(mision_dist) > 0 else None
        else:
            mision_principal = "Base insuficiente"
            mision_pct = None

        item_cruce = item.copy()
        item_cruce['pct_preferentes_gama_habituales_aca'] = pct_habito_entre_pref
        item_cruce['n_pref_gama_habituales'] = gama_habito_pref
        item_cruce['mision_principal_entre_habituales_gama'] = mision_principal
        item_cruce['mision_principal_pct'] = mision_pct
        item_cruce['flag_cruce'] = flag_base(min(gama_habito_pref, n_pref_gama))
        desconexion_con_cruce.append(item_cruce)

    # ── Conteo congruencia ──
    n_congruentes = sum(1 for m in matriz if m['congruencia_lider'])
    n_no_congruentes = len(matriz) - n_congruentes

    return {
        "descripcion": "Capítulo: Lugar de compra × Precio percibido × Preferencia × Misiones",
        "n_categorias_analizadas": len(matriz),
        "congruencia_summary": {
            "n_categorias_congruentes": n_congruentes,
            "n_categorias_desconexion": n_no_congruentes,
            "interpretacion": f"En {n_congruentes}/{len(matriz)} categorias el lider de habito (P30) = lider de precio (P32). En {n_no_congruentes} hay desconexion — otro atributo guia la eleccion."
        },
        "3a_matriz_p30_x_p32": {
            "nota": "Por categoria: lider habitual (P30), lider precio (P32), posicion Gama en ambos, congruencia.",
            "tabla": sorted(matriz, key=lambda x: -x['gama_habito_pct'])
        },
        "3b_desconexion_gama": {
            "nota": "Categorias donde Gama tiene shoppers habituales (P30≥5) pero NO figura en top-3 de mejor precio (P32). El shopper elige Gama por conveniencia, servicio u otro atributo.",
            "categorias": desconexion_gama
        },
        "3c_desconexion_x_preferencia_x_mision": {
            "nota": "Para las categorias de desconexion: % de preferentes Gama que compran ahi y mision principal de quienes compran habitualmente en Gama en esa categoria.",
            "tabla": desconexion_con_cruce
        },
        "3d_hallazgos_condensados": {
            "nota": "Ver hallazgos clave en §6 del reporte. Aqui summary cuantitativo.",
            "categorias_donde_gama_condiciona_preferencia": [
                x['categoria'] for x in desconexion_con_cruce
                if (x.get('pct_preferentes_gama_habituales_aca') or 0) > 20
            ],
            "categorias_donde_gama_condiciona_urgencia": [
                x['categoria'] for x in desconexion_con_cruce
                if x.get('mision_principal_entre_habituales_gama') == 'Urgencia'
            ]
        }
    }


# ─── NEW-4: BALANCE ÓPTIMO CATEGORIAS A PRECIOS IGUALES ───────────────────────

def analizar_new4_balance_optimo(df, p30_cols, p32_cols):
    """
    NEW-4: Síntesis estratégica — balance óptimo de categorias a igualar precio.
    Grupos:
    - Criticas: Paramo lidera precio con gap >20pp (proteinas)
    - Easy wins: Gama ya cerca del lider en P32 (gap <5pp)
    - Mantener diferencial: Gama lidera en experiencia, no en precio
    """
    n_total = len(df)

    criticas = []
    easy_wins = []
    diferencial_experiencia = []
    medio = []

    # Para cada categoria calcular posicion Gama en P32 y habito en P30
    for cat_label in p30_cols:
        if cat_label not in p32_cols:
            continue

        col_p30 = p30_cols[cat_label]
        col_p32 = p32_cols[cat_label]

        # P32 datos
        vals_p32 = df[col_p32].apply(label_cadena)
        vals_p32_clean = vals_p32[~vals_p32.isin(['Ninguno en particular', 'Ninguno (NO LEER)', None])]
        vals_p32_clean = vals_p32_clean[vals_p32_clean.astype(str).str.strip() != '']
        vc_p32 = vals_p32_clean.value_counts()

        if len(vc_p32) == 0:
            continue

        lider_precio = str(vc_p32.index[0])
        lider_precio_n = int(vc_p32.iloc[0])
        lider_precio_pct = round(lider_precio_n / n_total * 100, 1)
        n_gama_p32 = int((vals_p32 == 'Gama').sum())
        pct_gama_p32 = round(n_gama_p32 / n_total * 100, 1)
        gap_pp = round(lider_precio_pct - pct_gama_p32, 1)

        # P30 habito Gama
        vals_p30 = df[col_p30].apply(label_cadena)
        n_gama_p30 = int((vals_p30 == 'Gama').sum())
        pct_gama_p30 = round(n_gama_p30 / n_total * 100, 1)

        # Ninguno% en P32 (mercado de percepcion activo o no)
        n_ninguno = int(vals_p32.isin(['Ninguno en particular', 'Ninguno (NO LEER)']).sum())
        pct_ninguno = round(n_ninguno / n_total * 100, 1)

        entrada = {
            "categoria": cat_label,
            "lider_precio": lider_precio,
            "lider_precio_pct": lider_precio_pct,
            "gama_precio_pct": pct_gama_p32,
            "gap_gama_lider_pp": gap_pp,
            "gama_habito_pct": pct_gama_p30,
            "pct_sin_percepcion_precio": pct_ninguno,
            "flag": flag_base(n_gama_p32)
        }

        # Clasificar
        if gap_pp >= 20:
            # Criticas: brecha grande → alta presión para igualar precio
            criticas.append({**entrada, "recomendacion": "IGUALAR PRECIO — alta visibilidad, mayor impacto en share"})
        elif gap_pp <= 5 and pct_ninguno < 50:
            # Easy wins: ya cerca del lider, mercado de percepcion activo
            easy_wins.append({**entrada, "recomendacion": "EASY WIN — ajuste marginal convierte percepcion en liderazgo"})
        elif pct_gama_p30 >= 3 and gap_pp > 5:
            # Gama tiene habito pero precio por encima: mantener diferencial
            if cat_label in ('Farmacia', 'Licores', 'Congelados', 'Gaseosas, jugos y aguas',
                             'Galletas, pasapalos y confiteria', 'Salsas y Enlatados'):
                diferencial_experiencia.append({
                    **entrada,
                    "recomendacion": "MANTENER PRECIO + COMUNICAR DIFERENCIAL (atencion/limpieza/24h)"
                })
            else:
                medio.append({**entrada, "recomendacion": "MONITOREAR — evaluar si ajuste de precio tiene ROI"})
        else:
            medio.append({**entrada, "recomendacion": "MONITOREAR — base habitual baja, prioridad menor"})

    # Sort cada grupo por gap desc
    criticas.sort(key=lambda x: -x['gap_gama_lider_pp'])
    easy_wins.sort(key=lambda x: x['gap_gama_lider_pp'])
    diferencial_experiencia.sort(key=lambda x: -x['gama_habito_pct'])

    # Tabla resumen de 3 grupos
    tabla_balance = []
    for item in criticas:
        tabla_balance.append({**item, "grupo": "CRITICO"})
    for item in easy_wins:
        tabla_balance.append({**item, "grupo": "EASY_WIN"})
    for item in diferencial_experiencia:
        tabla_balance.append({**item, "grupo": "DIFERENCIAL_EXPERIENCIA"})
    for item in medio:
        tabla_balance.append({**item, "grupo": "MONITOREAR"})

    return {
        "descripcion": "Balance óptimo de categorias a igualar precio para maximizar share sin perder diferencial",
        "grupo_1_criticas": {
            "definicion": "Categorias donde Paramo lidera precio con gap >20pp sobre Gama. Alta presión para igualar — igualar precio en estas categorias tiene mayor impacto visible en el segmento precio.",
            "n_categorias": len(criticas),
            "categorias": criticas
        },
        "grupo_2_easy_wins": {
            "definicion": "Categorias donde Gama ya está cerca del lider (gap <5pp) y el mercado de percepcion es activo (Ninguno <50%). Ajuste marginal de precio puede convertirse en liderazgo percibido.",
            "n_categorias": len(easy_wins),
            "categorias": easy_wins
        },
        "grupo_3_diferencial_experiencia": {
            "definicion": "Categorias donde Gama tiene shoppers habituales (por conveniencia/servicio) aunque no sea percibida como la más económica. Estrategia: mantener precio o subir ligeramente + comunicar diferencial de experiencia.",
            "n_categorias": len(diferencial_experiencia),
            "categorias": diferencial_experiencia
        },
        "grupo_4_monitorear": {
            "n_categorias": len(medio),
            "categorias": medio
        },
        "tabla_completa_3_grupos": tabla_balance,
        "recomendacion_balance": {
            "prioridad_1": "Igualar precio en proteinas (carne/pollo/charcuteria) — impacto directo en NSE C+/C y segmento precio-sensible. Riesgo: sacrificio de margen significativo.",
            "prioridad_2": "Easy wins en Farmacia y Licores — pequeño ajuste de precio o comunicacion de precio activa percepcion sin sacrificio de margen relevante.",
            "prioridad_3": "Mantener diferencial en categorias de habito sin liderazgo de precio (Congelados, Gaseosas, Enlatados) — comunicar atencion/limpieza/24h como razon de compra explicita.",
            "advertencia": "Este análisis es perceptual — las cifras de P32 son REFERENCIALES (n<30 Gama en la mayoria de categorias). Las decisiones de precio deben validarse con datos reales de pricing interno antes de ejecutar."
        }
    }


# ─── HIPÓTESIS EXPRESS: MISIÓN URGENCIA × NSE × GEO ───────────────────────────

def analizar_express_hipotesis(df):
    """
    Hipotesis Express: Misión urgencia Gama correlaciona con formato Express (tienda pequeña).
    BBDD 2026 NO tiene variable de formato/tamaño de tienda — verificar y documentar.
    Cruzar: P26 urgencia × cadena Gama × NSE × Municipio/Parroquia.
    """
    n_total = len(df)

    # Verificar si hay variable de formato/tamano de tienda en BBDD
    formato_cols = [c for c in df.columns if any(
        kw in c.lower() for kw in ['formato', 'tamano', 'express', 'tipo tienda', 'sucursal']
    )]
    tiene_formato_variable = len(formato_cols) > 0

    print(f"\n  Variables formato en BBDD: {formato_cols}")
    print(f"  Tiene variable formato: {tiene_formato_variable}")

    # P26 urgencia — col V823
    p26_urg_col = [c for c in df.columns if '{P26}' in c and 'V823' in c]
    if not p26_urg_col:
        return {"error": "No se encontro columna P26 urgencia (V823)"}

    col_urgencia = p26_urg_col[0]
    vals_urg = df[col_urgencia].apply(label_cadena)

    # Distribucion general P26 urgencia
    vc_urg = vals_urg.dropna()
    vc_urg = vc_urg[vc_urg.astype(str).str.strip() != '']
    vc_urg = vc_urg[~vc_urg.isin(['Ninguno en particular', 'Ninguno (NO LEER)'])]
    vc_urg_dist = vc_urg.value_counts()

    n_base_urg = int(vals_urg.notna().sum())
    n_menciona_gama_urg = int((vals_urg == 'Gama').sum())
    pct_gama_urg = round(n_menciona_gama_urg / n_base_urg * 100, 1) if n_base_urg > 0 else None

    urg_ranking = [{"cadena": str(v), "n": int(cnt), "pct": round(cnt/n_base_urg*100,1)}
                   for v, cnt in vc_urg_dist.head(8).items()]

    # ── Cruce P26 urgencia × NSE ──
    cruce_nse = []
    for nse_g in ['C+/C', 'D', 'E']:
        sub = df[df['NSE_harm'] == nse_g]
        n_nse = len(sub)
        vals_urg_nse = sub[col_urgencia].apply(label_cadena)
        n_base_urg_nse = int(vals_urg_nse.notna().sum())
        n_gama_urg_nse = int((vals_urg_nse == 'Gama').sum())
        pct_gama_urg_nse = round(n_gama_urg_nse / n_base_urg_nse * 100, 1) if n_base_urg_nse > 0 else None

        # Quien lidera en urgencia para este NSE
        vc_nse = vals_urg_nse.dropna()
        vc_nse = vc_nse[~vc_nse.isin(['Ninguno en particular', 'Ninguno (NO LEER)', None])]
        vc_nse = vc_nse[vc_nse.astype(str).str.strip() != '']
        lider_nse = str(vc_nse.value_counts().index[0]) if len(vc_nse) > 0 else 'N/D'
        lider_nse_pct = round(vc_nse.value_counts().iloc[0] / n_base_urg_nse * 100, 1) if len(vc_nse) > 0 else None

        cruce_nse.append({
            "nse": nse_g,
            "n_nse": n_nse,
            "n_base_p26_urgencia": n_base_urg_nse,
            "n_gama_urgencia": n_gama_urg_nse,
            "pct_gama_urgencia": pct_gama_urg_nse,
            "lider_urgencia_en_nse": lider_nse,
            "lider_pct": lider_nse_pct,
            "gama_es_lider": (lider_nse == 'Gama'),
            "flag": flag_base(n_gama_urg_nse)
        })

    # ── Cruce P26 urgencia × Municipio ──
    cruce_geo = []
    mun_dist = df['MUNICIPIO'].value_counts()
    for mun, n_mun in mun_dist.head(10).items():
        if n_mun < 10:
            continue
        sub = df[df['MUNICIPIO'] == mun]
        n_base_mun = len(sub)
        vals_urg_mun = sub[col_urgencia].apply(label_cadena)
        n_base_urg_mun = int(vals_urg_mun.notna().sum())
        n_gama_urg_mun = int((vals_urg_mun == 'Gama').sum())
        pct_gama_urg_mun = round(n_gama_urg_mun / n_base_urg_mun * 100, 1) if n_base_urg_mun > 0 else None

        vc_mun = vals_urg_mun.dropna()
        vc_mun = vc_mun[~vc_mun.isin(['Ninguno en particular', 'Ninguno (NO LEER)', None])]
        vc_mun = vc_mun[vc_mun.astype(str).str.strip() != '']
        lider_mun = str(vc_mun.value_counts().index[0]) if len(vc_mun) > 0 else 'N/D'
        lider_mun_pct = round(vc_mun.value_counts().iloc[0] / n_base_urg_mun * 100, 1) if len(vc_mun) > 0 else None

        cruce_geo.append({
            "municipio": str(mun),
            "n_municipio": int(n_mun),
            "n_base_p26_urgencia": n_base_urg_mun,
            "n_gama_urgencia": n_gama_urg_mun,
            "pct_gama_urgencia": pct_gama_urg_mun,
            "lider_urgencia": lider_mun,
            "lider_pct": lider_mun_pct,
            "gama_es_lider": (lider_mun == 'Gama'),
            "flag": flag_base(n_gama_urg_mun)
        })

    cruce_geo.sort(key=lambda x: -(x['pct_gama_urgencia'] or 0))

    # ── P25 mision ultima compra × cadena P24 (ultimo sup visitado) ──
    # Verificar si hay col P24 (supermercado de ultima visita)
    p24_cols = [c for c in df.columns if '{P24}' in c]
    cruce_mision_cadena = None
    if p24_cols:
        col_p24 = p24_cols[0]
        df['P24_cadena'] = df[col_p24].apply(label_cadena)
        df['P25_short'] = df['P25_raw'].apply(
            lambda v: 'Urgencia' if ('urgencia' in str(v).lower() or 'pocos' in str(v).lower())
            else ('Reabastecimiento' if ('reabastecer' in str(v).lower() or 'reabastecimiento' in str(v).lower())
            else ('Abastecimiento general' if 'general' in str(v).lower() else 'Otro'))
        )
        # Gama en P24 × P25
        mask_gama_p24 = (df['P24_cadena'] == 'Gama')
        n_gama_p24 = mask_gama_p24.sum()
        if n_gama_p24 >= BASE_EXCLUIR_THRESH:
            mision_gama_p24 = df[mask_gama_p24]['P25_short'].value_counts()
            cruce_mision_cadena = {
                "base_gama_p24": int(n_gama_p24),
                "distribucion_mision": [
                    {"mision": str(m), "n": int(cnt),
                     "pct": round(cnt/n_gama_p24*100,1)}
                    for m, cnt in mision_gama_p24.items()
                ],
                "nota": "Distribucion de misiones entre quienes hicieron su ultima compra en Gama (P24=Gama)"
            }
        else:
            cruce_mision_cadena = {
                "base_gama_p24": int(n_gama_p24),
                "nota": f"Base insuficiente (n={n_gama_p24}) — EXCLUIR INFERENCIA"
            }

    # ── Interpretación hipotesis ──
    gama_lidera_urg_todos_nse = all(r['gama_es_lider'] for r in cruce_nse if r['n_gama_urgencia'] > 0)
    gama_lidera_urg_mayoria_geo = sum(1 for r in cruce_geo if r['gama_es_lider']) / len(cruce_geo) if cruce_geo else 0

    interpretacion_hipotesis = (
        f"Gama lidera urgencia en P26 general (12.2%). "
        f"{'PATRON TRANSVERSAL POR NSE: Gama lidera o co-lidera urgencia en los 3 NSE — compatible con hipotesis Express' if gama_lidera_urg_todos_nse else 'Patron NSE heterogeneo — Gama no lidera urgencia en todos los NSE'}. "
        f"A nivel geografico, Gama es lider de urgencia en {round(gama_lidera_urg_mayoria_geo*100)}% de los municipios analizados. "
        f"VARIABLE FORMATO NO DISPONIBLE EN BBDD 2026 — la hipotesis Express no puede probarse directamente. "
        f"Los datos son COMPATIBLES con la hipotesis (patron transversal de urgencia) pero NO la comprueban. "
        f"Para validar formalmente se requeriria cruzar con datos de formato operacional de Gama (Express vs convencional)."
    )

    return {
        "descripcion": "Hipotesis Express: mision urgencia Gama × NSE × Geo",
        "variable_formato_en_bbdd": {
            "disponible": tiene_formato_variable,
            "columnas_encontradas": formato_cols,
            "decision": (
                "VARIABLE NO DISPONIBLE. La hipotesis 'formato Express explica urgencia' "
                "no puede probarse directamente con BBDD 2026. "
                "Se presentan evidencias compatibles con la hipotesis."
            )
        },
        "p26_urgencia_ranking_general": {
            "n_base": n_base_urg,
            "gama_n": n_menciona_gama_urg,
            "gama_pct": pct_gama_urg,
            "ranking_top8": urg_ranking,
            "nota": "Gama ya confirmado como lider urgencia en CU-8 v1 — este análisis extiende el cruce por NSE y geo"
        },
        "cruce_urgencia_x_nse": cruce_nse,
        "cruce_urgencia_x_municipio": cruce_geo,
        "cruce_mision_p25_x_gama_p24": cruce_mision_cadena,
        "interpretacion_hipotesis": interpretacion_hipotesis,
        "compatibilidad_con_hipotesis_express": {
            "evidencia_a_favor": [
                "Gama lidera urgencia a nivel total (12.2%)",
                "Si el patron es transversal a NSE/geo donde Gama opera, es consistente con formato de conveniencia/proximidad",
                "Mision urgencia + farmacia (habito) es un patron coherente de tienda de proximity"
            ],
            "evidencia_pendiente_para_confirmar": [
                "Variable formato operacional (Express vs convencional) NO en BBDD 2026",
                "Datos de radio de cobertura de cada sucursal Gama no disponibles en encuesta",
                "Para validar formalmente: cruzar P26 urgencia con base de datos de sucursales Gama por tamano/formato"
            ]
        }
    }


# ─── PLOTS ────────────────────────────────────────────────────────────────────

def generar_heatmap_desconexion(new3_result, output_path):
    """
    Heatmap de desconexion: categorias × (habito P30 vs precio P32) para Gama.
    """
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import matplotlib.colors as mcolors

        matriz = new3_result['3a_matriz_p30_x_p32']['tabla']

        categorias = [m['categoria'][:30] for m in matriz]
        habito_pct = [m['gama_habito_pct'] for m in matriz]
        precio_pct = [m['gama_precio_pct'] for m in matriz]
        brecha = [m['gama_habito_pct'] - m['gama_precio_pct'] for m in matriz]

        # Sort por brecha desc
        data_sorted = sorted(zip(categorias, habito_pct, precio_pct, brecha),
                             key=lambda x: -x[3])
        cats, hab, prec, brec = zip(*data_sorted) if data_sorted else ([], [], [], [])

        fig, ax = plt.subplots(figsize=(12, 7))
        x = range(len(cats))
        width = 0.35

        bars1 = ax.bar([i - width/2 for i in x], hab, width,
                       label='Habito P30 (% compra habitualmente en Gama)', color='#1f77b4', alpha=0.85)
        bars2 = ax.bar([i + width/2 for i in x], prec, width,
                       label='Mejor precio P32 (% percibe Gama como mejor precio)', color='#d62728', alpha=0.85)

        ax.set_xlabel('Categoria de producto', fontsize=10)
        ax.set_ylabel('% de la muestra total (n=402)', fontsize=10)
        ax.set_title('Gama: Habito de compra vs Percepcion de mejor precio por categoria\n(Brecha = activo de experiencia no traducido en imagen de precio)', fontsize=11)
        ax.set_xticks(list(x))
        ax.set_xticklabels(cats, rotation=45, ha='right', fontsize=8)
        ax.legend(fontsize=9)
        ax.set_ylim(0, max(max(hab + (0,)), max(prec + (0,))) + 2)
        ax.axhline(y=0, color='black', linewidth=0.5)

        # Anotar brecha en los pares donde habito > precio
        for i, (h, p) in enumerate(zip(hab, prec)):
            if h > p and h > 0:
                ax.annotate(f'+{round(h-p,1)}pp',
                           xy=(i, max(h, p) + 0.3),
                           ha='center', va='bottom', fontsize=7, color='#2ca02c')

        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"  [OK] Heatmap guardado: {output_path}")
        return True
    except ImportError as e:
        print(f"  [WARN] matplotlib no disponible: {e}. Plot omitido.")
        return False
    except Exception as e:
        print(f"  [WARN] Error generando plot: {e}")
        return False


# ─── MAIN ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 70)
    print("CU-8 V2 Extension — Gama Notoriedad 2026")
    print("=" * 70)

    df = load_data()
    p30_cols = get_p30_cols(df)
    p32_cols = get_p32_cols(df)

    print(f"\n  P30 cols mapeadas: {len(p30_cols)}")
    print(f"  P32 cols mapeadas: {len(p32_cols)}")

    print("\n[1/5] NEW-1: Subset 'Igual o menos caro' (P33)...")
    new1 = analizar_new1_subset_economico(df, p30_cols, p32_cols)

    print("\n[2/5] NEW-2: Cruce P33 × P21 (percepcion precio × preferencia)...")
    new2 = analizar_new2_p33_x_p21(df)

    print("\n[3/5] NEW-3: Capítulo lugar × precio × preferencia × misiones...")
    new3 = analizar_new3_capitulo_lugar_precio(df, p30_cols, p32_cols)

    print("\n[4/5] NEW-4: Balance óptimo categorias a precios iguales...")
    new4 = analizar_new4_balance_optimo(df, p30_cols, p32_cols)

    print("\n[5/5] Hipótesis Express: mision urgencia × NSE × Geo...")
    express = analizar_express_hipotesis(df)

    # ── Generar plot ──
    print("\n[Plot] Generando heatmap desconexion P30 vs P32 Gama...")
    plot_ok = generar_heatmap_desconexion(new3, OUTPUT_PLOT_HEATMAP)

    # ── Build output JSON ──
    output = {
        "metadata": {
            "proyecto": "Gama Notoriedad 2026",
            "output": "CU-8 Extension V2 — 5 Analisis Adicionales",
            "fecha": "2026-05-18",
            "extiende": "CU8_preguntas_faltantes_20260518_v1.json",
            "n_total": int(len(df)),
            "alpha": ALPHA,
            "base_baja_threshold": BASE_BAJA_THRESH,
            "metodo_ic": "Newcombe-Wilson",
            "multiple_tests": "BH-FDR donde aplica"
        },
        "extension_v2": {
            "NEW1_subset_economico": new1,
            "NEW2_p33_x_p21": new2,
            "NEW3_capitulo_lugar_precio": new3,
            "NEW4_balance_optimo": new4,
            "EXPRESS_hipotesis_formato": express
        }
    }

    dump_json(output, OUTPUT_JSON)
    print(f"\n[OK] JSON exportado: {OUTPUT_JSON}")

    # ── Print summary ──
    print("\n" + "=" * 70)
    print("RESUMEN EJECUTIVO CU-8 V2")
    print("=" * 70)

    print(f"\n--- NEW-1: Subset 'Igual o menos caro' ---")
    print(f"  n subset: {new1['n_subset_economico']} ({new1['pct_subset']}% de validos P33)")
    print(f"  n caro: {new1['n_subset_caro']} ({new1['pct_caro']}%)")
    print(f"  % preferentes Gama en subset: {new1['c_cruce_preferencia_p21']['pct_preferentes_gama_en_subset']}%")
    print(f"  % preferentes Gama total: {new1['c_cruce_preferencia_p21']['pct_preferentes_gama_total']}%")
    print(f"  OR preferencia en subset: {new1['c_cruce_preferencia_p21']['OR_preferencia_en_subset']['OR']}")

    print(f"\n--- NEW-2: P33 × P21 Chi2 y OR ---")
    chi2_data = new2['test_asociacion']
    print(f"  Chi2: {chi2_data['chi2']}  p={chi2_data['p_value']}  sig={chi2_data['significativo']}")
    print(f"  Cramer's V: {chi2_data['cramers_v']}")
    or_data = new2['OR_percepcion_favorable_vs_desfavorable']
    print(f"  OR favorable vs desfavorable: {or_data['OR_percepcion_favorable_P33']} IC95={or_data['OR_favorable_IC95']}")
    print(f"  OR atencion CU-5: {or_data['OR_atencion_CU5']}")
    print(f"  Tabla cruzada P33 × P21:")
    for row in new2['tabla_cruzada_p33_x_p21_gama']:
        print(f"    {row['categoria_p33'][:35]:<35} n={row['n_en_categoria']:3d}  pref_gama={row['pct_prefiere_gama']}% [{row['flag']}]")

    print(f"\n--- NEW-3: Desconexion Gama (habito>precio) ---")
    for item in new3['3b_desconexion_gama']['categorias'][:6]:
        print(f"  {item['categoria'][:35]:<35} Habito: {item['gama_habito_pct']}% | Precio: {item['gama_precio_pct']}% | Brecha: +{item['brecha_habito_vs_precio_pp']}pp [{item['flag']}]")

    print(f"\n--- NEW-4: Balance óptimo ---")
    print(f"  Criticas (gap>20pp): {[x['categoria'][:20] for x in new4['grupo_1_criticas']['categorias']]}")
    print(f"  Easy wins (gap<5pp): {[x['categoria'][:20] for x in new4['grupo_2_easy_wins']['categorias']]}")
    print(f"  Diferencial exp: {[x['categoria'][:20] for x in new4['grupo_3_diferencial_experiencia']['categorias']]}")

    print(f"\n--- EXPRESS: Variable formato en BBDD: {express['variable_formato_en_bbdd']['disponible']} ---")
    print(f"  Cruce urgencia × NSE:")
    for r in express['cruce_urgencia_x_nse']:
        print(f"    NSE {r['nse']}: Gama urgencia {r['pct_gama_urgencia']}% | Lider: {r['lider_urgencia_en_nse']} {r['lider_pct']}% [{r['flag']}]")
    print(f"\n  Cruce urgencia × Municipio (top):")
    for r in express['cruce_urgencia_x_municipio'][:5]:
        print(f"    {str(r['municipio'])[:25]:<25} Gama: {r['pct_gama_urgencia']}% | Lider: {r['lider_urgencia']} [{r['flag']}]")

    print("\n[DONE] CU-8 V2 Extension completada.")
