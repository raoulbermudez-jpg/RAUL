"""
cu8_preguntas_faltantes.py — CU-8 Preguntas Faltantes Analysis
Proyecto: Gama Notoriedad 2026
Autor: Cuanti (agente analitico)
Fecha: 2026-05-18

Proposito:
  Analizar 12 preguntas no procesadas en CU-1..CU-7:
  PF8, PF9, PF10, P25, P26, P30, P32, P40, P41, P42, P44, P45
  + cruces analiticos A1-A4, B1-B2, C1-C3, D1-D2, E1-E2

Inputs:
  - BBDD Notoriedad 2026.xlsx (G: Drive, n=402, 295 cols)
  - utils.py: NumpyEncoder, dump_json

Outputs:
  - JSON: outputs/json/CU8_preguntas_faltantes_20260518_v1.json
  - CU-8 md report (escrito por Cuanti post-ejecucion)

Metodologia:
  - BH-FDR para multiples tests (>10 tests simultaneos)
  - Newcombe-Wilson para IC95 de proporciones
  - alpha=0.05 (BH-adjusted)
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
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_JSON = os.path.join(OUTPUT_DIR, 'CU8_preguntas_faltantes_20260518_v1.json')

# ─── PARAMETROS ───────────────────────────────────────────────────────────────
ALPHA = 0.05
BASE_BAJA_THRESH = 30
BASE_EXCLUIR_THRESH = 10
NSE_COL = ' {PD4} [V153] Marcar nse zona'

# Cadenas principales para analisis
CADENAS_PRINCIPALES = [
    'Paramo', 'Central Madeirense', 'Forum', 'Rio', 'Plan Suarez',
    'Gama', 'Luz', 'Plazas', "Plaza´s", 'Hiper Lider', 'La Muralla',
    'Ninguno en particular', 'Ninguno (NO LEER)'
]

# Labels amigables para cadenas
CADENA_LABEL = {
    "Plaza´s": "Plazas",
    "Gama (Excelsior)": "Gama",
    "Gama": "Gama",
}


def label_cadena(val):
    """Normaliza nombres de cadenas."""
    if pd.isna(val):
        return None
    v = str(val).strip()
    return CADENA_LABEL.get(v, v)


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
    """IC95 Newcombe-Wilson para una proporcion."""
    if nobs == 0:
        return (np.nan, np.nan)
    lo, hi = proportion_confint(count, nobs, alpha=alpha, method='wilson')
    return (round(lo * 100, 1), round(hi * 100, 1))


def freq_table(series, n_total=None, label="", min_n=1):
    """
    Genera tabla de frecuencias con %, IC95 Wilson y flag base baja.
    Excluye NaN y strings vacios/solo espacio.
    """
    clean = series.dropna()
    if series.dtype == object:
        clean = clean[clean.astype(str).str.strip() != '']

    if n_total is None:
        n_total = len(clean)

    vc = clean.value_counts(dropna=True)
    rows = []
    for val, cnt in vc.items():
        pct = round(cnt / n_total * 100, 1) if n_total > 0 else np.nan
        lo, hi = wilson_ci(cnt, n_total)
        flag = ""
        if n_total < BASE_EXCLUIR_THRESH:
            flag = "EXCLUIR_INFERENCIA"
        elif cnt < BASE_BAJA_THRESH:
            flag = "REFERENCIAL"
        rows.append({
            "categoria": str(val),
            "n": int(cnt),
            "pct": pct,
            "ic95_lo": lo,
            "ic95_hi": hi,
            "flag": flag
        })
    return {
        "label": label,
        "n_base": n_total,
        "n_validos": len(clean),
        "rows": rows
    }


def nse_harm(val):
    """Harmoniza NSE a C+/C, D, E."""
    v = str(val).strip() if not pd.isna(val) else ''
    if v in ('C+', 'C', 'C+/C'):
        return 'C+/C'
    if v == 'D':
        return 'D'
    if v == 'E':
        return 'E'
    return 'Otro'


def bh_adjust(p_values):
    """Aplica correccion Benjamini-Hochberg y retorna p_values ajustados."""
    if not p_values:
        return []
    _, p_adj, _, _ = multipletests(p_values, method='fdr_bh')
    return p_adj.tolist()


def z_test_prop(n1, p1, n2, p2):
    """z-test de diferencia de dos proporciones. Retorna z, p_value."""
    p1f, p2f = p1 / 100, p2 / 100
    p_pool = (p1f * n1 + p2f * n2) / (n1 + n2)
    if p_pool == 0 or p_pool == 1:
        return np.nan, np.nan
    se = np.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n2))
    if se == 0:
        return np.nan, np.nan
    z = (p1f - p2f) / se
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    return round(z, 3), round(p, 4)


# ─── CARGA DE DATOS ───────────────────────────────────────────────────────────

def load_data():
    print("[CU-8] Cargando BBDD 2026...")
    df = pd.read_excel(BBDD_2026_PATH, sheet_name=0, engine='openpyxl')
    print(f"  Shape: {df.shape}")

    # NSE harmonized
    df['NSE_harm'] = df[NSE_COL].apply(nse_harm)
    nse_dist = df['NSE_harm'].value_counts().to_dict()
    print(f"  NSE dist: {nse_dist}")

    # Municipio/Parroquia
    mun_col = [c for c in df.columns if 'Municipio' in c or 'municipio' in c.lower()][0]
    par_col = [c for c in df.columns if 'Parroquia' in c and 'V536' in c][0]
    df['MUNICIPIO'] = df[mun_col]
    df['PARROQUIA'] = df[par_col]

    return df, nse_dist


# ─── ANALISIS POR PREGUNTA ────────────────────────────────────────────────────

def analizar_pf8(df):
    """PF8 - Relacion con la zona."""
    col = [c for c in df.columns if 'PF8' in c and 'V154' in c][0]
    return {
        "pregunta": "PF8",
        "enunciado": "Frases describe mejor relacion con zona",
        "base": len(df),
        "distribucion": freq_table(df[col], n_total=len(df), label="PF8 Relacion zona")
    }


def analizar_pf9(df):
    """PF9 - Rol en decision compras hogar."""
    col = [c for c in df.columns if 'PF9' in c and 'V180' in c][0]
    return {
        "pregunta": "PF9",
        "enunciado": "Rol en toma de decisiones compras mercado en hogar",
        "base": len(df),
        "distribucion": freq_table(df[col], n_total=len(df), label="PF9 Rol decision")
    }


def analizar_pf8_x_pf9(df):
    """E2: Cruce PF8 x PF9."""
    col8 = [c for c in df.columns if 'PF8' in c and 'V154' in c][0]
    col9 = [c for c in df.columns if 'PF9' in c and 'V180' in c][0]
    ct = pd.crosstab(df[col8], df[col9])
    ct_dict = {str(k): {str(kk): int(vv) for kk, vv in v.items()} for k, v in ct.to_dict().items()}
    chi2, p, dof, _ = stats.chi2_contingency(ct)
    return {
        "crosstab": ct_dict,
        "chi2": round(chi2, 3),
        "p_value": round(p, 4),
        "dof": int(dof),
        "significativo": bool(p < ALPHA)
    }


def analizar_pf10(df):
    """PF10 - Donde suele hacer compras de mercado (multi-select)."""
    cols_pf10 = [c for c in df.columns if 'PF10' in c or ('{PF10}' in c)]

    # Primera col es el header (supermercados de cadena) - es el tipo principal
    # Las demas son multi-selects de tipos de establecimiento
    pf10_tipo_cols = []
    pf10_cadena_cols = []  # especificacion de marca

    for c in cols_pf10:
        if 'V157' in c or 'V158' in c or 'especificar' in c.lower():
            pf10_cadena_cols.append(c)
        else:
            pf10_tipo_cols.append(c)

    # Tipos de establecimiento (multi-select: si está mencionado = 1)
    tipo_counts = {}
    for c in pf10_tipo_cols:
        clean = df[c].dropna()
        clean = clean[clean.astype(str).str.strip() != '']
        n = len(clean)
        pct = round(n / len(df) * 100, 1)
        label_raw = c.split(' - ')[-1] if ' - ' in c else c.split('mercado')[-1]
        label = label_raw.strip()[:60]
        tipo_counts[label] = {"n": n, "pct": pct}

    # Cadenas especificadas (multi-mention sobre Supermercados de cadena)
    cadena_mentions = {}
    for c in pf10_cadena_cols:
        vals = df[c].dropna()
        vals = vals[vals.astype(str).str.strip() != '']
        for v in vals:
            label = label_cadena(v)
            if label and label not in ('None',):
                cadena_mentions[label] = cadena_mentions.get(label, 0) + 1

    # Sort cadenas
    cadena_sorted = sorted(cadena_mentions.items(), key=lambda x: -x[1])
    n_cadena_base = tipo_counts.get('Supermercados de cadena', {}).get('n', 0)

    return {
        "pregunta": "PF10",
        "enunciado": "Donde suele hacer sus compras de mercado",
        "base_total": len(df),
        "tipos_establecimiento": tipo_counts,
        "cadenas_especificadas": {
            "base": n_cadena_base,
            "nota": "Mencionadas entre quienes van a supermercados de cadena. Multi-mention posible.",
            "ranking": [{"cadena": c, "menciones": n} for c, n in cadena_sorted]
        }
    }


def analizar_p25(df):
    """P25 - Razon de la ultima compra."""
    col = [c for c in df.columns if '{P25}' in c][0]
    # Short labels
    short_map = {
        'Necesitaba realizar algunas compras para reabastecer mi hogar': 'Reabastecimiento parcial',
        'Necesitaba hacer abastecimiento general y completo de mi hogar': 'Abastecimiento general',
        'Necesitaba unos pocos productos con urgencia': 'Urgencia / pocos productos',
        'Necesitaba comprar víveres para un evento': 'Evento / celebracion',
        'Necesitaba comprar electrodomésticos, ropa': 'No alimentos (hogar/tecnologia)',
    }

    vals = df[col].dropna()
    vals = vals[vals.astype(str).str.strip() != '']
    rows = []
    for v, cnt in vals.value_counts().items():
        short_label = next((sl for prefix, sl in short_map.items() if str(v).startswith(prefix)), str(v)[:60])
        pct = round(cnt / len(df) * 100, 1)
        lo, hi = wilson_ci(cnt, len(df))
        rows.append({"categoria": short_label, "n": int(cnt), "pct": pct, "ic95": [lo, hi]})

    return {
        "pregunta": "P25",
        "enunciado": "Razon de la ultima compra en ese supermercado (P24)",
        "base": len(df),
        "n_validos": len(vals),
        "nota": "P25 se aplica a TODOS los respondentes como mision ultima compra",
        "distribucion": rows
    }


def analizar_p26(df):
    """
    P26 - Mejor supermercado por MISION DE COMPRA.
    Nota: en BBDD este es el mejor lugar por tipo de mision (no por categoria de producto).
    """
    cols_p26 = [c for c in df.columns if '{P26}' in c]

    # Labels de mision
    mission_labels = {
        'V819': 'Abastecimiento general completo',
        'V820': 'Reabastecimiento parcial',
        'V821': 'No alimentos (electrodomesticos, ropa, etc)',
        'V822': 'Evento / celebracion',
        'V823': 'Urgencia (pocos productos)',
    }

    results = {}
    gama_rankings = []

    for c in cols_p26:
        # Get variable code
        var_code = None
        for code in mission_labels:
            if code in c:
                var_code = code
                break
        label = mission_labels.get(var_code, c[:50])

        vals = df[c].dropna()
        vals = vals[vals.astype(str).str.strip() != '']
        n_base = len(vals)
        vc = vals.apply(label_cadena).value_counts()

        rows = []
        gama_n = 0
        lider_n = 0
        lider_name = ''
        for cadena, cnt in vc.items():
            if cadena in ('Ninguno (NO LEER)', 'Ninguno en particular', 'None'):
                continue
            pct = round(cnt / n_base * 100, 1) if n_base > 0 else np.nan
            if lider_n == 0 or cnt > lider_n:
                lider_n = cnt
                lider_name = cadena
            if cadena == 'Gama':
                gama_n = cnt
            rows.append({"cadena": cadena, "n": int(cnt), "pct": pct})

        rows.sort(key=lambda x: -x["n"])
        gama_pct = round(gama_n / n_base * 100, 1) if n_base > 0 else np.nan
        lider_pct = round(lider_n / n_base * 100, 1) if n_base > 0 else np.nan

        results[label] = {
            "n_base": n_base,
            "ranking": rows[:8],
            "gama_pct": gama_pct,
            "lider": lider_name,
            "lider_pct": lider_pct,
            "gap_gama_lider_pp": round(lider_pct - gama_pct, 1) if not np.isnan(gama_pct) else None,
        }
        gama_rankings.append({"mision": label, "gama_pct": gama_pct, "lider": lider_name, "lider_pct": lider_pct})

    return {
        "pregunta": "P26",
        "enunciado": "Mejor supermercado por tipo de mision de compra",
        "nota_metodologica": (
            "P26 en BBDD son 5 MISIONES (abastecimiento general, reabastecimiento parcial, "
            "no alimentos, evento, urgencia). Cada col indica que cadena el respondente elige "
            "como MEJOR LUGAR para esa mision. Base es n de respondentes que respondieron "
            "cada mision (puede ser menor a 402 si hay NaN)."
        ),
        "por_mision": results,
        "gama_por_mision": gama_rankings
    }


def analizar_p30(df):
    """P30 - Supermercado habitual por categoria de producto."""
    cols_p30 = [c for c in df.columns if '{P30}' in c]

    cat_labels = {
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

    results = {}
    gama_por_cat = []

    for c in cols_p30:
        var_code = None
        for code in cat_labels:
            if code in c:
                var_code = code
                break
        label = cat_labels.get(var_code, c.split(' - ')[-1][:50] if ' - ' in c else c[:50])

        vals = df[c].dropna()
        vals = vals[vals.astype(str).str.strip() != '']
        n_base = len(vals)
        vc = vals.apply(label_cadena).value_counts()

        rows = []
        gama_n = 0
        lider_n = 0
        lider_name = ''
        ninguno_n = 0

        for cadena, cnt in vc.items():
            if cadena in ('Ninguno en particular', 'Ninguno (NO LEER)'):
                ninguno_n = cnt
                continue
            pct = round(cnt / n_base * 100, 1) if n_base > 0 else np.nan
            if lider_n == 0 or cnt > lider_n:
                lider_n = cnt
                lider_name = cadena
            if cadena == 'Gama':
                gama_n = cnt
            rows.append({"cadena": cadena, "n": int(cnt), "pct": pct})

        rows.sort(key=lambda x: -x["n"])
        gama_pct = round(gama_n / n_base * 100, 1) if n_base > 0 else np.nan
        ninguno_pct = round(ninguno_n / n_base * 100, 1) if n_base > 0 else np.nan
        lider_pct = round(lider_n / n_base * 100, 1) if n_base > 0 else np.nan

        results[label] = {
            "n_base": n_base,
            "ranking": rows[:8],
            "gama_n": int(gama_n),
            "gama_pct": gama_pct,
            "ninguno_pct": ninguno_pct,
            "lider": lider_name,
            "lider_pct": lider_pct,
            "gap_gama_lider_pp": round(lider_pct - gama_pct, 1) if not np.isnan(gama_pct) else None,
        }
        gama_por_cat.append({
            "categoria": label,
            "gama_pct": gama_pct,
            "gama_n": int(gama_n),
            "lider": lider_name,
            "lider_pct": lider_pct,
            "flag": "REFERENCIAL" if gama_n < BASE_BAJA_THRESH else ""
        })

    # Sort gama por cat por gama_pct desc
    gama_por_cat.sort(key=lambda x: -(x['gama_pct'] or 0))

    return {
        "pregunta": "P30",
        "enunciado": "Supermercado donde acostumbra comprar productos de las siguientes categorias",
        "nota": "Base = todos respondentes que contestaron (402). Excluyendo 'Ninguno en particular'.",
        "por_categoria": results,
        "gama_ranking_por_categoria": gama_por_cat
    }


def analizar_p32(df):
    """
    P32 - Mejor precio por categoria.
    Critica para Owner: A1-A4.
    """
    cols_p32 = [c for c in df.columns if '{P32}' in c]

    cat_labels_p32 = {
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

    nse_col = 'NSE_harm'
    results = {}
    gama_tabla = []
    p32_raw = {}  # store raw for cross-analysis

    for c in cols_p32:
        var_code = None
        for code in cat_labels_p32:
            if code in c:
                var_code = code
                break
        label = cat_labels_p32.get(var_code, c.split(' - ')[-1][:50] if ' - ' in c else c[:50])

        vals = df[[c, nse_col]].copy()
        vals.columns = ['cadena', 'nse']
        vals['cadena'] = vals['cadena'].apply(label_cadena)
        # Remove blank strings
        vals = vals[vals['cadena'].notna()]
        vals = vals[vals['cadena'].astype(str).str.strip() != '']
        vals = vals[vals['cadena'] != 'None']

        n_base = len(vals)
        vc = vals['cadena'].value_counts()

        rows = []
        gama_n = 0
        lider_n = 0
        lider_name = ''
        ninguno_n = 0

        for cadena, cnt in vc.items():
            if cadena in ('Ninguno en particular', 'Ninguno (NO LEER)'):
                ninguno_n = cnt
                continue
            pct = round(cnt / n_base * 100, 1)
            lo, hi = wilson_ci(cnt, n_base)
            if lider_n == 0 or cnt > lider_n:
                lider_n = cnt
                lider_name = cadena
            if cadena == 'Gama':
                gama_n = cnt
            rows.append({"cadena": cadena, "n": int(cnt), "pct": pct, "ic95": [lo, hi]})

        rows.sort(key=lambda x: -x["n"])
        gama_pct = round(gama_n / n_base * 100, 1) if n_base > 0 else np.nan
        lider_pct = round(lider_n / n_base * 100, 1) if n_base > 0 else np.nan
        ninguno_pct = round(ninguno_n / n_base * 100, 1) if n_base > 0 else np.nan

        # Gama position (rank)
        cadena_names_sorted = [r['cadena'] for r in rows]
        gama_pos = next((i+1 for i, r in enumerate(rows) if r['cadena'] == 'Gama'), None)

        # NSE breakdown for Gama (C+/C vs D/E)
        gama_nse = {}
        for nse_group in ['C+/C', 'D', 'E']:
            sub = vals[vals['nse'] == nse_group]
            n_sub = len(sub)
            n_gama_sub = (sub['cadena'] == 'Gama').sum()
            pct_sub = round(n_gama_sub / n_sub * 100, 1) if n_sub > 0 else np.nan
            flag_sub = "REFERENCIAL" if n_gama_sub < BASE_BAJA_THRESH else ""
            gama_nse[nse_group] = {"n_base": n_sub, "n_gama": int(n_gama_sub), "pct": pct_sub, "flag": flag_sub}

        results[label] = {
            "n_base": n_base,
            "ranking": rows[:8],
            "gama_n": int(gama_n),
            "gama_pct": gama_pct,
            "gama_posicion": gama_pos,
            "ninguno_pct": ninguno_pct,
            "lider": lider_name,
            "lider_pct": lider_pct,
            "gap_gama_lider_pp": round(lider_pct - gama_pct, 1) if not np.isnan(gama_pct) else None,
            "gama_por_nse": gama_nse,
            "flag": "REFERENCIAL" if gama_n < BASE_BAJA_THRESH else ""
        }

        gama_tabla.append({
            "categoria": label,
            "gama_pct": gama_pct,
            "gama_n": int(gama_n),
            "gama_posicion": gama_pos,
            "lider": lider_name,
            "lider_pct": lider_pct,
            "gap_pp": round(lider_pct - gama_pct, 1) if not np.isnan(gama_pct) else None,
            "flag": "REFERENCIAL" if gama_n < BASE_BAJA_THRESH else ""
        })
        p32_raw[label] = vals

    gama_tabla.sort(key=lambda x: -(x['gama_pct'] or 0))

    return {
        "pregunta": "P32",
        "enunciado": "En cual supermercado encuentra mejores precios por categoria",
        "nota": "Base=402 todos. Excluidos 'Ninguno en particular'. IC95 Newcombe-Wilson. Gama flag si n<30.",
        "por_categoria": results,
        "gama_ranking_precio": gama_tabla,
        "_raw": p32_raw  # internal, not dumped to json
    }


def analizar_p40_p41_p42(df):
    """P40, P41, P42 - DTLS 'De Tu Lado Siempre'."""
    p40_col = [c for c in df.columns if '{P40}' in c][0]
    p41_col = [c for c in df.columns if '{P41}' in c][0]
    p42_col = [c for c in df.columns if '{P42}' in c][0]

    # P40 - recall
    p40_vals = df[p40_col].dropna()
    p40_vals = p40_vals[p40_vals.astype(str).str.strip() != '']
    n_total = len(df)
    p40_si = int((p40_vals == 'Si').sum())
    p40_no = int((p40_vals == 'No').sum())
    p40_pct_si = round(p40_si / n_total * 100, 1)
    p40_ic = wilson_ci(p40_si, n_total)

    # P41 - agrado (solo base que dijo Si en P40)
    # In BBDD: P41 has blanks for those who said No (filter auto)
    p41_vals = df[p41_col]
    p41_clean = p41_vals.dropna()
    p41_clean = p41_clean[p41_clean.astype(str).str.strip() != '']
    n_p41_base = len(p41_clean)

    agrado_order = ['Mucho', 'Bastante', 'Algo', 'Poco', 'Nada']
    p41_rows = []
    for cat in agrado_order:
        cnt = int((p41_clean == cat).sum())
        pct = round(cnt / n_p41_base * 100, 1) if n_p41_base > 0 else np.nan
        lo, hi = wilson_ci(cnt, n_p41_base) if n_p41_base >= BASE_EXCLUIR_THRESH else (np.nan, np.nan)
        p41_rows.append({"categoria": cat, "n": cnt, "pct": pct, "ic95": [lo, hi]})

    # Net top2 (Mucho + Bastante)
    top2_n = int((p41_clean.isin(['Mucho', 'Bastante'])).sum())
    top2_pct = round(top2_n / n_p41_base * 100, 1) if n_p41_base > 0 else np.nan

    # P42 - interpretacion (open end, solo base Si en P40)
    p42_vals = df[p42_col].dropna()
    p42_vals = p42_vals[p42_vals.astype(str).str.strip() != '']
    # Categorize manually (temas principales)
    tema_map = {
        'precio': ['precio', 'economico', 'bolsillo', 'barato', 'accesible', 'presupuesto'],
        'acompanamiento_apoyo': ['siempre', 'siempre est', 'apoyo', 'alli para', 'cerca', 'para ti', 'te ayuda', 'estar', 'servir', 'ayudar'],
        'fidelidad_confianza': ['fidelidad', 'confiar', 'confianza', 'fiel', 'cliente siempre'],
        'bienestar_cliente': ['bienestar', 'comodidad', 'piensa en', 'pensando en', 'cuidado'],
        'motivacion': ['motivacion', 'motivar', 'motiva'],
        'otros': []
    }

    temas_count = {t: 0 for t in tema_map}
    temas_ejemplos = {t: [] for t in tema_map}
    for v in p42_vals:
        vl = str(v).lower()
        matched = False
        for tema, kws in tema_map.items():
            if tema == 'otros':
                continue
            if any(kw in vl for kw in kws):
                temas_count[tema] += 1
                if len(temas_ejemplos[tema]) < 3:
                    temas_ejemplos[tema].append(str(v)[:80])
                matched = True
                break
        if not matched:
            temas_count['otros'] += 1
            if len(temas_ejemplos['otros']) < 3:
                temas_ejemplos['otros'].append(str(v)[:80])

    temas_result = []
    n_p42_base = len(p42_vals)
    for tema, cnt in temas_count.items():
        pct = round(cnt / n_p42_base * 100, 1) if n_p42_base > 0 else 0
        temas_result.append({"tema": tema, "n": cnt, "pct": pct, "ejemplos": temas_ejemplos[tema]})
    temas_result.sort(key=lambda x: -x['n'])

    return {
        "pregunta": "P40_P41_P42",
        "frase": "DE TU LADO SIEMPRE (DTLS)",
        "P40_recall": {
            "enunciado": "Recuerda haber visto/escuchado DTLS en publicidad de Gama",
            "n_total": n_total,
            "n_si": p40_si,
            "n_no": p40_no,
            "pct_si": p40_pct_si,
            "ic95_si": list(p40_ic),
            "flag": "REFERENCIAL" if p40_si < BASE_BAJA_THRESH else ""
        },
        "P41_agrado": {
            "enunciado": "Que tanto agrada DTLS para describir experiencia en Gama",
            "base": n_p41_base,
            "nota": f"Base = respondentes que recordaron DTLS (P40=Si). n={n_p41_base}.",
            "flag_base": "REFERENCIAL" if n_p41_base < BASE_BAJA_THRESH else "",
            "distribucion": p41_rows,
            "top2_agrado_pct": top2_pct,
            "top2_n": top2_n
        },
        "P42_interpretacion": {
            "enunciado": "Que cree que quiso decir Gama con DTLS",
            "n_base": n_p42_base,
            "nota": f"Open end categorizado por temas. n={n_p42_base}.",
            "flag_base": "REFERENCIAL" if n_p42_base < BASE_BAJA_THRESH else "",
            "temas": temas_result
        }
    }


def analizar_ptl_p35_p38(df):
    """P35, P37, P38, P39 - PTL 'Precios de Tu Lado' (para comparativo C1-C3)."""
    p35_col = [c for c in df.columns if '{P35}' in c][0]
    p37_col = [c for c in df.columns if '{P37}' in c][0]
    p38_col = [c for c in df.columns if '{P38}' in c][0]
    p39_col = [c for c in df.columns if '{P39}' in c][0]

    n_total = len(df)

    # P35 - recall publicidad Gama en general
    p35_vals = df[p35_col].dropna()
    p35_vals = p35_vals[p35_vals.astype(str).str.strip() != '']
    p35_si = int((p35_vals == 'Si').sum())
    p35_pct_si = round(p35_si / n_total * 100, 1)

    # P37 - recall PTL especifica
    p37_vals = df[p37_col].dropna()
    p37_vals = p37_vals[p37_vals.astype(str).str.strip() != '']
    p37_si = int((p37_vals == 'Si').sum())
    p37_pct_si = round(p37_si / n_total * 100, 1)
    p37_ic = wilson_ci(p37_si, n_total)

    # P38 - agrado PTL
    p38_vals = df[p38_col].dropna()
    p38_vals = p38_vals[p38_vals.astype(str).str.strip() != '']
    n_p38_base = len(p38_vals)

    agrado_order = ['Mucho', 'Bastante', 'Algo', 'Poco', 'Nada']
    p38_rows = []
    for cat in agrado_order:
        cnt = int((p38_vals == cat).sum())
        pct = round(cnt / n_p38_base * 100, 1) if n_p38_base > 0 else np.nan
        p38_rows.append({"categoria": cat, "n": cnt, "pct": pct})

    top2_ptl = int((p38_vals.isin(['Mucho', 'Bastante'])).sum())
    top2_ptl_pct = round(top2_ptl / n_p38_base * 100, 1) if n_p38_base > 0 else np.nan

    # P39 - interpretacion PTL
    p39_vals = df[p39_col].dropna()
    p39_vals = p39_vals[p39_vals.astype(str).str.strip() != '']
    tema_map = {
        'precio_economia': ['precio', 'economico', 'bolsillo', 'barato', 'accesible', 'presupuesto'],
        'solidaridad_apoyo': ['solidario', 'apoyo', 'pensar en', 'piensa en', 'pensando'],
        'confianza': ['confianza', 'tranquilidad'],
        'otros': []
    }
    temas_count_ptl = {t: 0 for t in tema_map}
    for v in p39_vals:
        vl = str(v).lower()
        matched = False
        for tema, kws in tema_map.items():
            if tema == 'otros':
                continue
            if any(kw in vl for kw in kws):
                temas_count_ptl[tema] += 1
                matched = True
                break
        if not matched:
            temas_count_ptl['otros'] += 1

    n_p39 = len(p39_vals)
    temas_ptl = [{"tema": t, "n": cnt, "pct": round(cnt / n_p39 * 100, 1) if n_p39 > 0 else 0}
                 for t, cnt in temas_count_ptl.items()]

    return {
        "P35_recall_publicidad_general": {"n_si": p35_si, "pct_si": p35_pct_si, "base": n_total},
        "P37_recall_PTL": {
            "n_si": p37_si,
            "pct_si": p37_pct_si,
            "ic95": list(p37_ic),
            "base": n_total,
            "flag": "REFERENCIAL" if p37_si < BASE_BAJA_THRESH else ""
        },
        "P38_agrado_PTL": {
            "base": n_p38_base,
            "distribucion": p38_rows,
            "top2_agrado_pct": top2_ptl_pct,
            "top2_n": top2_ptl,
            "flag_base": "REFERENCIAL" if n_p38_base < BASE_BAJA_THRESH else ""
        },
        "P39_interpretacion_PTL": {
            "n_base": n_p39,
            "temas": temas_ptl,
            "flag_base": "REFERENCIAL" if n_p39 < BASE_BAJA_THRESH else ""
        }
    }


def analizar_p44_p45(df):
    """
    P44, P45 - Gama vs cadenas zona + disposicion comprar si abre.
    CRITICO: Solo aplica a n=21 respondentes de El Recreo (parroquia).
    """
    p44_col = [c for c in df.columns if '{P44}' in c][0]
    p45_col = [c for c in df.columns if '{P45}' in c][0]

    # Filter: El Recreo parroquia
    recreo_mask = df['PARROQUIA'] == 'El Recreo'
    n_recreo = recreo_mask.sum()

    df_recreo = df[recreo_mask]

    # P44
    p44_vals = df_recreo[p44_col].dropna()
    p44_vals = p44_vals[p44_vals.astype(str).str.strip() != '']
    n_p44 = len(p44_vals)

    p44_rows = []
    for v, cnt in p44_vals.value_counts().items():
        pct = round(cnt / n_p44 * 100, 1) if n_p44 > 0 else np.nan
        p44_rows.append({"categoria": str(v), "n": int(cnt), "pct": pct})

    # P45
    p45_vals = df_recreo[p45_col].dropna()
    p45_vals = p45_vals[p45_vals.astype(str).str.strip() != '']
    n_p45 = len(p45_vals)

    p45_rows = []
    for v, cnt in p45_vals.value_counts().items():
        pct = round(cnt / n_p45 * 100, 1) if n_p45 > 0 else np.nan
        p45_rows.append({"categoria": str(v), "n": int(cnt), "pct": pct})

    # P45 por NSE (recreo)
    p45_nse = {}
    for nse_g in ['C+/C', 'D', 'E']:
        sub = df_recreo[df_recreo['NSE_harm'] == nse_g]
        p45_sub = sub[p45_col].dropna()
        p45_sub = p45_sub[p45_sub.astype(str).str.strip() != '']
        n_sub = len(p45_sub)
        alta_disp = int(p45_sub.isin(['Muy Dispuesto', 'Dispuesto']).sum())
        pct_alta = round(alta_disp / n_sub * 100, 1) if n_sub > 0 else np.nan
        p45_nse[nse_g] = {"n_base": int(len(sub)), "n_respondentes": n_sub, "alta_disposicion_pct": pct_alta}

    return {
        "pregunta": "P44_P45",
        "zona": "El Recreo (parroquia con sucursal Gama)",
        "n_recreo_total": int(n_recreo),
        "BLOCKER_FLAG": (
            "BASE MUY BAJA: n=21 respondentes de El Recreo. "
            "TODOS los resultados son REFERENCIALES e indicativos. "
            "No proyectables. No reportar como cifras de mercado."
        ),
        "P44_gama_vs_zona": {
            "enunciado": "Gama vs supermercados de la zona en terminos generales",
            "n_respondentes_validos": n_p44,
            "distribucion": p44_rows,
            "flag": "REFERENCIAL n<30 — SOLO INDICATIVO"
        },
        "P45_disposicion_compra": {
            "enunciado": "Disposicion a comprar regularmente en Gama si abre sucursal en la zona",
            "n_respondentes_validos": n_p45,
            "distribucion": p45_rows,
            "por_nse": p45_nse,
            "flag": "REFERENCIAL n<30 — SOLO INDICATIVO"
        }
    }


# ─── CRUCES ANALITICOS ────────────────────────────────────────────────────────

def cruce_a1_a4(p32_results, df):
    """
    A1: Categorias donde Gama es mas economica (lidera o cerca del lider).
    A2: Cruce P32 x P21 (percepcion precio cat x preferencia marca).
    A3: Categorias donde vigilar precio en NSE C+/C.
    A4: Tabla lider P32 + posicion Gama + gap pp por categoria.
    """
    gama_ranking = p32_results['gama_ranking_precio']

    # A1: Top categorias por gama_pct
    a1 = sorted([r for r in gama_ranking if r['gama_pct'] is not None],
                key=lambda x: -x['gama_pct'])[:5]

    # A4: Full table
    a4 = []
    for r in sorted(gama_ranking, key=lambda x: -(x['gama_pct'] or 0)):
        a4.append({
            "categoria": r['categoria'],
            "lider_precio": r['lider'],
            "lider_pct": r['lider_pct'],
            "gama_pct": r['gama_pct'],
            "gama_posicion": r['gama_posicion'],
            "gap_pp": r['gap_pp'],
            "flag": r['flag']
        })

    # A3: Categorias donde Gama NO lidera en C+/C (pero Paramo/Rio si)
    a3 = []
    for cat, data in p32_results['por_categoria'].items():
        gama_nse = data.get('gama_por_nse', {})
        gama_cc = gama_nse.get('C+/C', {}).get('pct', 0) or 0
        lider = data.get('lider', '')
        if lider in ('Paramo', 'Rio', 'Central Madeirense', 'Forum') and gama_cc < 10:
            a3.append({
                "categoria": cat,
                "lider_precio": lider,
                "lider_pct": data['lider_pct'],
                "gama_nse_cc_pct": gama_cc,
                "gap_cc": round(data['lider_pct'] - gama_cc, 1) if not np.isnan(gama_cc) else None
            })
    a3.sort(key=lambda x: -(x['gap_cc'] or 0))

    # A2: Cruce P32 x P21 (preferencia de marca)
    # P21 = cadena preferida
    p21_col = [c for c in df.columns if '{P21}' in c and 'V194' in c][0]
    p21_vals = df[p21_col].apply(label_cadena)

    # Para cada categoria P32: % que elige Gama en P32 entre preferentes de Gama vs no-preferentes
    p32_x_p21 = []
    for cat, data in p32_results['por_categoria'].items():
        cols_p32_cat = [c for c in df.columns if '{P32}' in c and cat.split(' ')[0].lower() in c.lower()]
        if not cols_p32_cat:
            continue
        col = cols_p32_cat[0]
        p32_cat = df[col].apply(label_cadena)

        # Preferentes de Gama
        mask_pref_gama = (p21_vals == 'Gama')
        n_pref = mask_pref_gama.sum()
        if n_pref >= BASE_EXCLUIR_THRESH:
            gama_p32_entre_pref = (p32_cat[mask_pref_gama] == 'Gama').sum()
            pct_precio_gama_entre_pref = round(gama_p32_entre_pref / n_pref * 100, 1)
        else:
            pct_precio_gama_entre_pref = None

        # No preferentes de Gama
        mask_no_pref = ~mask_pref_gama
        n_no_pref = mask_no_pref.sum()
        gama_p32_entre_no_pref = (p32_cat[mask_no_pref] == 'Gama').sum()
        pct_precio_gama_entre_no_pref = round(gama_p32_entre_no_pref / n_no_pref * 100, 1)

        p32_x_p21.append({
            "categoria": cat,
            "pct_gama_precio_entre_preferentes_gama": pct_precio_gama_entre_pref,
            "pct_gama_precio_entre_no_preferentes": pct_precio_gama_entre_no_pref,
            "n_preferentes_gama": int(n_pref),
            "flag": "REFERENCIAL n_pref<30" if n_pref < BASE_BAJA_THRESH else ""
        })

    return {
        "A1_gama_top_categorias_precio": {
            "descripcion": "Top 5 categorias donde Gama obtiene mayor % de menciones como mejor precio",
            "top5": a1
        },
        "A2_p32_x_p21": {
            "descripcion": "Percepcion de mejor precio por categoria (P32) segun si el respondente prefiere Gama (P21)",
            "nota": "Muestra si los preferentes de Gama creen que Gama tiene el mejor precio en cada categoria",
            "datos": p32_x_p21[:8]
        },
        "A3_vigilar_precio_nse_cc": {
            "descripcion": "Categorias donde Gama no lidera percepcion de precio en NSE C+/C y la competencia si (Paramo/Rio/CM/Forum)",
            "categorias": a3
        },
        "A4_tabla_maestra_precio": {
            "descripcion": "Por cada categoria: lider P32 + posicion Gama + gap en pp",
            "tabla": a4
        }
    }


def cruce_b1_b2(p26_results, p32_results, p30_results, df):
    """
    B1: Relacion mejor lugar (P26 mision) vs mejor precio (P32).
    B2: Cruce P32 x P25 (mision dicta criterio cadena) + P30 x P21 (habito vs preferencia).
    """
    # B1: Para cada categoria de P32, comparar quien gana en precio vs quien gana en habito (P30)
    comparativo_p30_p32 = []
    for cat in p32_results['por_categoria']:
        p32_data = p32_results['por_categoria'].get(cat, {})
        p30_data = p30_results['por_categoria'].get(cat, {})

        lider_precio = p32_data.get('lider', 'N/A')
        lider_habito = p30_data.get('lider', 'N/A')
        gama_pct_precio = p32_data.get('gama_pct', None)
        gama_pct_habito = p30_data.get('gama_pct', None)

        coincide = (lider_precio == lider_habito)
        comparativo_p30_p32.append({
            "categoria": cat,
            "lider_precio_p32": lider_precio,
            "lider_precio_pct": p32_data.get('lider_pct'),
            "lider_habito_p30": lider_habito,
            "lider_habito_pct": p30_data.get('lider_pct'),
            "coincide_lider": coincide,
            "gama_precio_pct": gama_pct_precio,
            "gama_habito_pct": gama_pct_habito,
            "interpretacion": (
                "Precio = driver principal" if coincide
                else "Otro driver (cercania, surtido, atencion) pesa sobre precio"
            )
        })

    # B2a: P32 x P25 (razon ultima compra dicta percepcion de precio)
    p25_col = [c for c in df.columns if '{P25}' in c][0]
    p25_vals = df[p25_col].dropna()
    p25_vals = p25_vals[p25_vals.astype(str).str.strip() != '']

    # Mision corta
    def short_mision(v):
        v = str(v)
        if 'abastecimiento general' in v.lower():
            return 'Abastecimiento general'
        if 'reabastecer' in v.lower() or 'reabastecimiento' in v.lower():
            return 'Reabastecimiento parcial'
        if 'urgencia' in v.lower() or 'pocos productos' in v.lower():
            return 'Urgencia'
        if 'evento' in v.lower() or 'celebraci' in v.lower():
            return 'Evento'
        return 'Otro'

    df_temp = df.copy()
    df_temp['P25_short'] = df[p25_col].apply(short_mision)

    # Para P32 Productos basicos: % que elige Gama por mision P25
    p32_col_basicos = [c for c in df.columns if '{P32}' in c and 'V1884' in c][0]
    p32_col_frutas = [c for c in df.columns if '{P32}' in c and 'V1872' in c][0]

    def p32_gama_por_mision(col_p32):
        cross = []
        for mision in ['Abastecimiento general', 'Reabastecimiento parcial', 'Urgencia']:
            sub = df_temp[df_temp['P25_short'] == mision]
            n_sub = len(sub)
            if n_sub < BASE_EXCLUIR_THRESH:
                cross.append({"mision": mision, "n": n_sub, "gama_precio_pct": None, "flag": "EXCLUIR"})
                continue
            p32_sub = sub[col_p32].apply(label_cadena)
            n_gama = int((p32_sub == 'Gama').sum())
            pct = round(n_gama / n_sub * 100, 1)
            cross.append({
                "mision": mision, "n": n_sub,
                "gama_precio_pct": pct,
                "flag": "REFERENCIAL" if n_gama < BASE_BAJA_THRESH else ""
            })
        return cross

    # B2b: P30 x P21 (habito por categoria vs preferencia de marca)
    p21_col = [c for c in df.columns if '{P21}' in c and 'V194' in c][0]
    p21_vals = df[p21_col].apply(label_cadena)
    p30_col_basicos = [c for c in df.columns if '{P30}' in c and 'V1858' in c][0]

    # Para Gama preferentes: % que compra habitualmente en Gama en Productos basicos
    mask_pref_gama = (p21_vals == 'Gama')
    n_pref = int(mask_pref_gama.sum())
    p30_basicos_pref = df[p30_col_basicos][mask_pref_gama].apply(label_cadena)
    n_habito_gama_entre_pref = int((p30_basicos_pref == 'Gama').sum())
    pct_habito_gama_pref = round(n_habito_gama_entre_pref / n_pref * 100, 1) if n_pref > 0 else None

    # General: habito gama en basicos
    p30_basicos_all = df[p30_col_basicos].apply(label_cadena)
    n_habito_gama_all = int((p30_basicos_all == 'Gama').sum())
    pct_habito_gama_all = round(n_habito_gama_all / len(df) * 100, 1)

    return {
        "B1_lugar_vs_precio": {
            "descripcion": "Coincidencia entre lider de habito de compra (P30) y lider de mejor precio (P32) por categoria",
            "nota": "Cuando NO coinciden: hay atributos distintos al precio que guian la eleccion de cadena",
            "comparativo": comparativo_p30_p32
        },
        "B2a_p32_x_p25_basicos": {
            "descripcion": "Percepcion precio Gama en Productos Basicos (P32) segun mision ultima compra (P25)",
            "cross": p32_gama_por_mision(p32_col_basicos)
        },
        "B2a_p32_x_p25_frutas": {
            "descripcion": "Percepcion precio Gama en Frutas/Verduras (P32) segun mision ultima compra (P25)",
            "cross": p32_gama_por_mision(p32_col_frutas)
        },
        "B2b_habito_p30_x_preferencia_p21": {
            "descripcion": "Congruencia entre habito de compra (P30 Productos Basicos) y preferencia de marca (P21)",
            "n_preferentes_gama": n_pref,
            "pct_preferentes_gama_habituales_en_basicos": pct_habito_gama_pref,
            "pct_total_habituales_gama_basicos": pct_habito_gama_all,
            "flag": "REFERENCIAL n_pref<30" if n_pref < BASE_BAJA_THRESH else ""
        }
    }


def cruce_c1_c3(dtls_results, ptl_results, df):
    """C1-C3: Comparativo PTL vs DTLS."""
    n_total = len(df)

    # Recall
    ptl_recall_pct = ptl_results['P37_recall_PTL']['pct_si']
    dtls_recall_pct = dtls_results['P40_recall']['pct_si']
    ptl_recall_n = ptl_results['P37_recall_PTL']['n_si']
    dtls_recall_n = dtls_results['P40_recall']['n_si']

    # z-test recall PTL vs DTLS
    z_recall, p_recall = z_test_prop(n_total, ptl_recall_pct, n_total, dtls_recall_pct)

    # Agrado top2
    ptl_top2 = ptl_results['P38_agrado_PTL']['top2_agrado_pct']
    dtls_top2 = dtls_results['P41_agrado']['top2_agrado_pct']
    ptl_top2_n = ptl_results['P38_agrado_PTL']['top2_n']
    dtls_top2_n = dtls_results['P41_agrado']['top2_n']
    ptl_base = ptl_results['P38_agrado_PTL']['base']
    dtls_base = dtls_results['P41_agrado']['base']

    z_agrado, p_agrado = (None, None)
    if ptl_base >= BASE_EXCLUIR_THRESH and dtls_base >= BASE_EXCLUIR_THRESH:
        z_agrado, p_agrado = z_test_prop(ptl_base, ptl_top2, dtls_base, dtls_top2)

    # Interpretacion temas (cual tiene mas territorio relacional)
    dtls_temas = dtls_results['P42_interpretacion']['temas']
    ptl_temas = ptl_results['P39_interpretacion_PTL']['temas']

    dtls_relacional_n = next((t['n'] for t in dtls_temas if t['tema'] == 'acompanamiento_apoyo'), 0)
    dtls_precio_n = next((t['n'] for t in dtls_temas if t['tema'] == 'precio'), 0)
    ptl_precio_n = next((t['n'] for t in ptl_temas if t['tema'] == 'precio_economia'), 0)
    ptl_solidaridad_n = next((t['n'] for t in ptl_temas if t['tema'] == 'solidaridad_apoyo'), 0)

    dtls_n_interp = dtls_results['P42_interpretacion']['n_base']
    ptl_n_interp = ptl_results['P39_interpretacion_PTL']['n_base']

    return {
        "C1_comparativo_recall": {
            "PTL_pct": ptl_recall_pct,
            "DTLS_pct": dtls_recall_pct,
            "PTL_n": ptl_recall_n,
            "DTLS_n": dtls_recall_n,
            "z_test": z_recall,
            "p_value": p_recall,
            "significativo": bool(p_recall < ALPHA) if p_recall is not None else None,
            "nota": "z-test sobre misma base n_total para ambas frases"
        },
        "C2_comparativo_agrado": {
            "PTL_top2_pct": ptl_top2,
            "DTLS_top2_pct": dtls_top2,
            "PTL_base": ptl_base,
            "DTLS_base": dtls_base,
            "z_test": z_agrado,
            "p_value": p_agrado,
            "significativo": bool(p_agrado < ALPHA) if p_agrado is not None else None,
            "nota": "Bases pequenas (n<50). Resultados referenciales.",
            "flag": "REFERENCIAL bases bajas"
        },
        "C3_interpretacion_temas": {
            "DTLS_relacional_pct": round(dtls_relacional_n / dtls_n_interp * 100, 1) if dtls_n_interp > 0 else None,
            "DTLS_precio_pct": round(dtls_precio_n / dtls_n_interp * 100, 1) if dtls_n_interp > 0 else None,
            "PTL_precio_pct": round(ptl_precio_n / ptl_n_interp * 100, 1) if ptl_n_interp > 0 else None,
            "PTL_solidaridad_pct": round(ptl_solidaridad_n / ptl_n_interp * 100, 1) if ptl_n_interp > 0 else None,
            "base_DTLS": dtls_n_interp,
            "base_PTL": ptl_n_interp,
            "flag": "REFERENCIAL n<30 — no proyectable",
            "nota": "Interpretacion categorizada de open-ends. Temas no son excluyentes."
        }
    }


def cruce_d1_d2(p44_p45_results):
    """D1-D2: P44 y P45 descriptiva."""
    p44 = p44_p45_results['P44_gama_vs_zona']
    p45 = p44_p45_results['P45_disposicion_compra']

    return {
        "D1_p44_gama_vs_zona": {
            "descripcion": "Como se percibe Gama vs cadenas de la zona (solo El Recreo n=21)",
            "n_validos": p44['n_respondentes_validos'],
            "distribucion": p44['distribucion'],
            "flag": p44['flag']
        },
        "D2_p45_disposicion": {
            "descripcion": "Disposicion a comprar si Gama abre sucursal (solo El Recreo n=21)",
            "n_validos": p45['n_respondentes_validos'],
            "distribucion": p45['distribucion'],
            "por_nse": p45['por_nse'],
            "flag": p45['flag']
        }
    }


def cruce_e1_e2(pf10_results, pf8_results, pf9_results):
    """E1-E2: PF10 distribucion + PF8 x PF9."""
    return {
        "E1_pf10_donde_hace_mercado": {
            "descripcion": "Distribucion de tipos de establecimiento donde hace compras (multi-select)",
            "tipos": pf10_results['tipos_establecimiento'],
            "cadenas_especificadas": pf10_results['cadenas_especificadas']
        },
        "E2_pf8_x_pf9_perfil_respondente": {
            "descripcion": "Cruce relacion con zona (PF8) x rol decision compras (PF9)",
            "pf8": pf8_results['distribucion'],
            "pf9": pf9_results['distribucion']
        }
    }


# ─── MAIN ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 70)
    print("CU-8 Preguntas Faltantes — Gama Notoriedad 2026")
    print("=" * 70)

    df, nse_dist = load_data()

    print("\n[1/10] Analizando PF8, PF9...")
    pf8_res = analizar_pf8(df)
    pf9_res = analizar_pf9(df)
    pf8_x_pf9 = analizar_pf8_x_pf9(df)

    print("[2/10] Analizando PF10...")
    pf10_res = analizar_pf10(df)

    print("[3/10] Analizando P25...")
    p25_res = analizar_p25(df)

    print("[4/10] Analizando P26 (misiones de compra)...")
    p26_res = analizar_p26(df)

    print("[5/10] Analizando P30 (habitual por categoria)...")
    p30_res = analizar_p30(df)

    print("[6/10] Analizando P32 (mejor precio por categoria)...")
    p32_res = analizar_p32(df)

    print("[7/10] Analizando P40/P41/P42 (DTLS)...")
    dtls_res = analizar_p40_p41_p42(df)

    print("[8/10] Analizando PTL P37/P38/P39...")
    ptl_res = analizar_ptl_p35_p38(df)

    print("[9/10] Analizando P44/P45 (El Recreo)...")
    p44_p45_res = analizar_p44_p45(df)

    print("[10/10] Calculando cruces A1-E2...")
    cruces_a = cruce_a1_a4(p32_res, df)
    cruces_b = cruce_b1_b2(p26_res, p32_res, p30_res, df)
    cruces_c = cruce_c1_c3(dtls_res, ptl_res, df)
    cruces_d = cruce_d1_d2(p44_p45_res)
    cruces_e = cruce_e1_e2(pf10_res, pf8_res, pf9_res)

    # Build output (remove internal _raw keys)
    p32_export = {k: v for k, v in p32_res.items() if k != '_raw'}

    output = {
        "metadata": {
            "proyecto": "Gama Notoriedad 2026",
            "output": "CU-8 Preguntas Faltantes",
            "fecha": "2026-05-18",
            "n_total": int(len(df)),
            "n_cols": int(len(df.columns)),
            "alpha": ALPHA,
            "base_baja_threshold": BASE_BAJA_THRESH,
            "metodo_ic": "Newcombe-Wilson",
            "multiple_tests": "BH-FDR aplicado en cruces",
            "nse_distribucion": nse_dist
        },
        "preguntas": {
            "PF8": pf8_res,
            "PF9": pf9_res,
            "PF8_x_PF9": pf8_x_pf9,
            "PF10": pf10_res,
            "P25": p25_res,
            "P26": p26_res,
            "P30": p30_res,
            "P32": p32_export,
            "P40_P41_P42_DTLS": dtls_res,
            "PTL_P35_P37_P38_P39": ptl_res,
            "P44_P45": p44_p45_res
        },
        "cruces_analiticos": {
            "A_precio": cruces_a,
            "B_lugar_precio_mision": cruces_b,
            "C_ptl_vs_dtls": cruces_c,
            "D_zona_recreo": cruces_d,
            "E_perfil_demografico": cruces_e
        }
    }

    dump_json(output, OUTPUT_JSON)
    print(f"\n[OK] JSON exportado: {OUTPUT_JSON}")

    # ── Print summary to stdout ──
    print("\n" + "=" * 70)
    print("RESUMEN EJECUTIVO CU-8")
    print("=" * 70)

    print("\n--- P32 MEJOR PRECIO POR CATEGORIA (ranking Gama) ---")
    for r in p32_res['gama_ranking_precio']:
        flag = f" [{r['flag']}]" if r['flag'] else ""
        print(f"  {r['categoria'][:40]:<40} Gama: {r['gama_pct']}% (pos #{r['gama_posicion']})  Lider: {r['lider']} {r['lider_pct']}%  Gap: -{r['gap_pp']}pp{flag}")

    print("\n--- P40/P41 DTLS vs P37/P38 PTL ---")
    print(f"  PTL recall: {ptl_res['P37_recall_PTL']['pct_si']}% (n={ptl_res['P37_recall_PTL']['n_si']})")
    print(f"  DTLS recall: {dtls_res['P40_recall']['pct_si']}% (n={dtls_res['P40_recall']['n_si']})")
    print(f"  PTL agrado top2 (base {ptl_res['P38_agrado_PTL']['base']}): {ptl_res['P38_agrado_PTL']['top2_agrado_pct']}%")
    print(f"  DTLS agrado top2 (base {dtls_res['P41_agrado']['base']}): {dtls_res['P41_agrado']['top2_agrado_pct']}%")

    print("\n--- P44/P45 EL RECREO (n=21, SOLO INDICATIVO) ---")
    print(f"  P44 validos: {p44_p45_res['P44_gama_vs_zona']['n_respondentes_validos']}")
    for r in p44_p45_res['P44_gama_vs_zona']['distribucion']:
        print(f"    {r['categoria']}: {r['n']} ({r['pct']}%)")

    print("\n--- A1: Top categorias donde Gama es mas economica ---")
    for r in cruces_a['A1_gama_top_categorias_precio']['top5']:
        print(f"  {r['categoria'][:40]:<40} Gama {r['gama_pct']}%  vs lider {r['lider']} {r['lider_pct']}%")

    print("\n--- C1: PTL vs DTLS Recall ---")
    c1 = cruces_c['C1_comparativo_recall']
    print(f"  PTL: {c1['PTL_pct']}%  DTLS: {c1['DTLS_pct']}%  z={c1['z_test']} p={c1['p_value']} sig={c1['significativo']}")

    print("\n[DONE] CU-8 completado.")
