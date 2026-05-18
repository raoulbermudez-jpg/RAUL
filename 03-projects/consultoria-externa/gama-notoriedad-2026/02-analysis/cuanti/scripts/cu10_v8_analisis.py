"""
cu10_v8_analisis.py — CU-10 V8: TB puro P22 + Regresion logistica + Mundo de marca P21xP23xP24/P25
Proyecto: Gama Notoriedad 2026
Autor: Cuanti (agente analitico)
Fecha: 2026-05-18
Version: v1

Pedido de Cora Urrea (correo previo a aprobacion V7):
  E1 — P22 Top Box (Muy importante) puro por Total + C+/C + cada marca preferida
  E2 — Regresion logistica drivers de preferencia (evaluacion de viabilidad VIF primero)
  E3 — Mundo de marca P21 x P23 x P24/P25 (cruce con experiencia de marca)
  E4 — Sintesis integradora (producida en el reporte .md, no en este script)

Inputs:
  BBDD_2026: G:/Mi unidad/RAUL/colaboradores/Genteca/Cora-Urrea/01_De_Cora_Para_Raoul/
             Notoriedad V2.0/BBDD Notoriedad 2026.xlsx (n=403, 295 cols)
  CU9 JSON (referencia): outputs/json/CU9_v7_analisis_20260518.json

Outputs:
  JSON:  outputs/json/CU10_v8_analisis_20260518.json
  Plots: outputs/plots/cu10_*.png

Notas de codificacion BBDD 2026 (validadas en CU-9):
  - P22: texto ('Muy Importante'/'Importante'/'Algo importante'/'Poco importante'/'Nada Importante')
  - P23: cada col {P23:X} - nombre de cadena si hay mencion, vacia si no
  - P21: nombre de cadena preferida (col ' {P21} [V194] Preferido')
  - P24: ' {P24} [V...] Alguna vez ha comprado en...' (Si/No por cadena — verificar cols reales)
  - P25: ' {P25} [V...] Actualmente compra en...' (Si/No por cadena — verificar cols reales)
  - PD4: NSE zona con valores 'C+', 'C', 'C+/C', 'B', 'A', 'D', 'E'
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

import os
import json
import warnings
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy import stats
from scipy.stats import chi2_contingency
warnings.filterwarnings('ignore')

# ─── CONSTANTES CONFIGURABLES ────────────────────────────────────────────────

BBDD_PATH = (
    'G:/Mi unidad/RAUL/colaboradores/Genteca/Cora-Urrea/'
    '01_De_Cora_Para_Raoul/Notoriedad V2.0/BBDD Notoriedad 2026.xlsx'
)

OUTPUT_JSON = (
    'C:/rAUL/03-projects/consultoria-externa/gama-notoriedad-2026/'
    '02-analysis/cuanti/outputs/json/CU10_v8_analisis_20260518.json'
)

OUTPUT_PLOTS_DIR = (
    'C:/rAUL/03-projects/consultoria-externa/gama-notoriedad-2026/'
    '02-analysis/cuanti/outputs/plots/'
)

ALPHA = 0.05
BASE_BAJA = 30       # n < 30 → REFERENCIAL
BASE_EXCLUIR = 10    # n < 10 → EXCLUIR (no reportar)
VIF_THRESHOLD = 10   # VIF > 10 = multicolinealidad alta

# Brand kit Gama V0.1
GAMA_RED = '#E30613'
GAMA_BLACK = '#1A1A1A'
GAMA_GRAY_MID = '#6B6B6B'
GAMA_GRAY_LIGHT = '#E5E5E5'
GAMA_AMBER = '#F2A900'
GAMA_GREEN = '#2D8F47'

COMP_COLORS = {
    'Paramo': '#4A6FA5',
    'Rio': '#7C8B9B',
    'Plan Suarez': '#9CAEC0',
    'Central Madeirense': '#5B7090',
    'Forum': '#8FA3B8',
    'Plazas': '#6D8499',
    'Luz': '#A8B9C7',
    'La Muralla': '#BCC9D4',
    'Hiper Lider': '#C8D5DF',
}

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Open Sans', 'Calibri', 'Arial', 'DejaVu Sans'],
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.titleweight': 'bold',
    'axes.labelsize': 10,
    'axes.edgecolor': GAMA_GRAY_MID,
    'axes.linewidth': 0.8,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'grid.color': GAMA_GRAY_LIGHT,
    'grid.linewidth': 0.5,
})

# Escala P22 texto -> numero
P22_SCALE = {
    'Muy Importante': 5,
    'Importante': 4,
    'Algo importante': 3,
    'Poco importante': 2,
    'Nada Importante': 1,
}

# Columnas P22 (de cu9_v7_analisis.py, validadas contra BBDD real)
P22_COLS = {
    'limpieza':     ' {P22} [V209] IMPORTANCIA  Es un espacio limpio y ordenado',
    'surtido':      ' {P22} [V202] IMPORTANCIA Donde encuentro la mayor cantidad de categorias/productos que acostumbro a comprar',
    'seguro':       ' {P22} [V213]  IMPORTANCIA Es seguro',
    'rapidez':      ' {P22} [V214]  IMPORTANCIA Rapidez en la caja',
    'menor_precio': ' {P22} [V204]  IMPORTANCIA Donde encuentro los productos a menor precio',
    'atractiva':    ' {P22} [V207]  IMPORTANCIA La tienda es atractiva',
    'promociones':  ' {P22} [V206]  IMPORTANCIA Tienen promociones atractivas',
    'calidad':      ' {P22} [V203]  IMPORTANCIA Donde encuentro los productos de mayor calidad',
    'atencion':     ' {P22} [V205] IMPORTANCIA  Donde mejor me atienden',
    'valer_dinero': ' {P22} [V1856]  IMPORTANCIA Donde puedo hacer valer mi dinero',
}

ATRIBUTO_NOMBRES = {
    'limpieza':     'Limpieza/orden',
    'surtido':      'Mayor surtido',
    'seguro':       'Seguro',
    'rapidez':      'Rapidez caja',
    'menor_precio': 'Menor precio',
    'atractiva':    'Tienda atractiva',
    'promociones':  'Promociones',
    'calidad':      'Mayor calidad',
    'atencion':     'Mejor atencion',
    'valer_dinero': 'Valer dinero',
}

# Columnas P23
P23_COLS = {
    'surtido':      ' {P23:1} [V570] Donde encuentro la mayor cantidad de categorías/productos que acostumbro a comprar',
    'calidad':      ' {P23:2} [V923] Productos mayor calidad',
    'menor_precio': ' {P23:3} [V552] Donde encuentro los productos a menor precio',
    'atencion':     ' {P23:4} [V553] Donde mejor me atienden',
    'promociones':  ' {P23:5} [V554] Tienen promociones atractivas',
    'atractiva':    ' {P23:6} [V555] La tienda es atractiva-',
    'limpieza':     ' {P23:8} [V557] Es un espacio limpio y ordenado',
    'seguro':       ' {P23:12} [V561] Es seguro ',
    'rapidez':      ' {P23:13} [V562] Rapidez en caja',
    'valer_dinero': ' {P23:21} [V1857] Donde puedo hacer valer mi dinero',
}

P21_COL = ' {P21} [V194] Preferido'
NSE_COL = ' {PD4} [V153] Marcar nse zona'

# Las 8 cadenas de interes para E1 y E3
CADENAS_PRINCIPALES = [
    'Gama', 'Paramo', 'Rio', 'Plan Suarez',
    'Central Madeirense', 'Forum', 'Plazas', 'Luz'
]
CADENAS_ALL = CADENAS_PRINCIPALES + ['La Muralla', 'Hiper Lider']

# ─── UTILS ──────────────────────────────────────────────────────────────────

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer,)): return int(obj)
        if isinstance(obj, (np.floating,)): return float(obj)
        if isinstance(obj, (np.bool_,)): return bool(obj)
        if isinstance(obj, np.ndarray): return obj.tolist()
        if isinstance(obj, float) and np.isnan(obj): return None
        return super().default(obj)

def dump_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, cls=NumpyEncoder)

def newcombe_ci(k, n, alpha=0.05):
    if n == 0: return (0.0, 0.0)
    p = k / n
    z = stats.norm.ppf(1 - alpha / 2)
    c = p + z**2 / (2*n)
    h = z * np.sqrt(p*(1-p)/n + z**2/(4*n*n))
    d = 1 + z**2/n
    return (max(0.0, (c-h)/d), min(1.0, (c+h)/d))

def flag_n(n):
    if n < BASE_EXCLUIR: return 'EXCLUIR'
    if n < BASE_BAJA: return 'REFERENCIAL'
    return 'OK'

def pct(k, n):
    return round(100 * k / n, 1) if n > 0 else 0.0

def is_gama(val):
    if pd.isna(val): return False
    return 'gama' in str(val).lower() or 'excelsior' in str(val).lower()

def is_yes(val):
    if pd.isna(val): return False
    return str(val).strip().lower() in ('si', 'sí', 'yes', '1', '1.0')

def nse_harm(v):
    v = str(v).strip()
    if v in ('C+', 'C', 'C+/C'): return 'C+/C'
    if v == 'D': return 'D'
    if v == 'E': return 'E'
    if v in ('B', 'A'): return 'B/A'
    return 'Otro'

def p22_score(val):
    return P22_SCALE.get(str(val).strip(), None)

def p23_has_cadena(val, cadena_name):
    if pd.isna(val): return False
    v = str(val).strip().lower()
    search = cadena_name.lower()
    # Alias para busqueda
    aliases = {
        'central madeirense': ['central madeirense', 'central'],
        'plan suarez': ['plan suarez', 'plan su'],
        'plazas': ["plaza´s", "plazas", "plaza's"],
        'luz': ['luz marina', 'luz'],
    }
    terms = aliases.get(search, [search])
    return any(t in v for t in terms)

def cadena_match(p21_val, cadena_name):
    """True si P21 preferido matchea la cadena."""
    if pd.isna(p21_val): return False
    v = str(p21_val).strip().lower()
    search = cadena_name.lower()
    aliases = {
        'central madeirense': ['central madeirense', 'central'],
        'plan suarez': ['plan suarez', 'plan su'],
        'plazas': ["plaza´s", "plazas", "plaza's"],
        'luz': ['luz marina', 'luz'],
    }
    terms = aliases.get(search, [search])
    return any(t in v for t in terms)


# ─── CARGA ──────────────────────────────────────────────────────────────────

def load_bbdd():
    print("Cargando BBDD 2026...")
    df = pd.read_excel(BBDD_PATH, engine='openpyxl')
    df['NSE_harm'] = df[NSE_COL].apply(nse_harm)
    df['P21_val'] = df[P21_COL].astype(str).str.strip()
    df['pref_gama'] = df['P21_val'].apply(is_gama)

    n_total = len(df)
    n_cc = int((df['NSE_harm'] == 'C+/C').sum())
    n_pg = int(df['pref_gama'].sum())
    print(f"  Total n={n_total} | C+/C n={n_cc} | Pref-Gama n={n_pg} {'(REFERENCIAL)' if n_pg < BASE_BAJA else ''}")

    # Detectar columnas P24 y P25 (experiencia de marca)
    p24_cols = {c: c for c in df.columns if '{P24}' in c or 'alguna vez' in c.lower()}
    p25_cols = {c: c for c in df.columns if '{P25}' in c or 'actualmente compra' in c.lower()}
    print(f"  Cols P24 encontradas: {len(p24_cols)}")
    print(f"  Cols P25 encontradas: {len(p25_cols)}")

    # Imprimir una muestra para verificar encoding real
    if p24_cols:
        sample_col = list(p24_cols.keys())[0]
        print(f"  Muestra P24 col: {sample_col[:80]}")
        print(f"  Muestra P24 valores: {df[sample_col].value_counts().head(3).to_dict()}")

    return df, p24_cols, p25_cols


# ─── E1 — P22 TOP BOX (Muy Importante) PURO ────────────────────────────────

def e1_topbox(df):
    """
    Calcula % 'Muy Importante' (TB puro, valor 5) para cada atributo P22 en:
    - Total (n=403)
    - C+/C (~104)
    - Pref-Gama (~32)
    - Pref por cada una de las 8 cadenas
    Compara TB puro vs T2B (Top 2 Box = Importante + Muy Importante).
    """
    print("\nE1: P22 Top Box puro (Muy Importante)...")

    df_cc = df[df['NSE_harm'] == 'C+/C']

    # Subsets por marca preferida
    subsets = {'Total': df, 'C+/C': df_cc}
    for cadena in CADENAS_PRINCIPALES:
        mask = df['P21_val'].apply(lambda v: cadena_match(v, cadena))
        subsets[f'Pref-{cadena}'] = df[mask]

    results = {}
    tb_rankings = {}  # Para comparar ranking TB vs T2B

    for grp_name, df_grp in subsets.items():
        n = len(df_grp)
        flag_grp = flag_n(n)
        rows = []

        for attr_k, col in P22_COLS.items():
            if col not in df_grp.columns:
                rows.append({
                    'atributo': attr_k,
                    'nombre': ATRIBUTO_NOMBRES[attr_k],
                    'n_base': n,
                    'n_valid': 0,
                    'n_tb': 0,
                    'pct_tb': 0.0,
                    'n_t2b': 0,
                    'pct_t2b': 0.0,
                    'ic95_tb_lo': 0.0,
                    'ic95_tb_hi': 0.0,
                    'flag': 'COL_NF',
                })
                continue

            scores = df_grp[col].apply(p22_score).dropna()
            n_valid = len(scores)
            n_tb = int((scores == 5).sum())          # Muy Importante
            n_t2b = int((scores >= 4).sum())         # Importante + Muy Importante
            mean_v = float(scores.mean()) if n_valid > 0 else None
            pct_tb_v = pct(n_tb, n_valid)
            pct_t2b_v = pct(n_t2b, n_valid)
            ci_lo, ci_hi = newcombe_ci(n_tb, n_valid)

            rows.append({
                'atributo': attr_k,
                'nombre': ATRIBUTO_NOMBRES[attr_k],
                'n_base': n,
                'n_valid': n_valid,
                'n_tb': n_tb,
                'pct_tb': pct_tb_v,
                'n_t2b': n_t2b,
                'pct_t2b': pct_t2b_v,
                'diff_tb_vs_t2b_pp': round(pct_t2b_v - pct_tb_v, 1),  # gap entre T2B y TB
                'ic95_tb_lo': round(ci_lo * 100, 1),
                'ic95_tb_hi': round(ci_hi * 100, 1),
                'mean_score': round(mean_v, 2) if mean_v else None,
                'flag': flag_n(n_valid),
            })

        # Ranking por TB
        rows_sorted = sorted(rows, key=lambda x: x['pct_tb'], reverse=True)
        for rank_i, r in enumerate(rows_sorted, 1):
            r['ranking_tb'] = rank_i

        # Ranking por T2B (para comparar)
        rows_t2b_sorted = sorted(rows, key=lambda x: x['pct_t2b'], reverse=True)
        t2b_rank_map = {r['atributo']: i for i, r in enumerate(rows_t2b_sorted, 1)}
        for r in rows:
            r['ranking_t2b'] = t2b_rank_map.get(r['atributo'])
            r['rank_delta'] = r.get('ranking_t2b', 0) - r.get('ranking_tb', 0)

        results[grp_name] = {
            'n': n,
            'flag': flag_grp,
            'items': rows,
            'top5_tb': [r['atributo'] for r in rows_sorted[:5]],
            'top5_t2b': [r['atributo'] for r in rows_t2b_sorted[:5]],
            'top5_cambia': [r['atributo'] for r in rows_sorted[:5]] != [r['atributo'] for r in rows_t2b_sorted[:5]],
        }
        tb_rankings[grp_name] = {r['atributo']: r['ranking_tb'] for r in rows}

    # Analisis de re-ranking (cuanto cambia el top-5 al usar TB vs T2B)
    reranking_summary = {}
    total_items = results.get('Total', {}).get('items', [])
    if total_items:
        cambios = [(r['atributo'], r['ranking_tb'], r['ranking_t2b'], r['rank_delta'])
                   for r in total_items if r.get('rank_delta') != 0]
        cambios_sort = sorted(cambios, key=lambda x: abs(x[3]), reverse=True)
        reranking_summary['total_atributos_que_cambian_rank'] = len(cambios_sort)
        reranking_summary['mayor_subida_tb'] = [(a, dt) for a, rt, r2, dt in cambios_sort if dt < 0][:3]
        reranking_summary['mayor_bajada_tb'] = [(a, dt) for a, rt, r2, dt in cambios_sort if dt > 0][:3]
        reranking_summary['top5_mismo_en_tb_y_t2b'] = not results['Total']['top5_cambia']

    return {
        'analisis': 'E1',
        'descripcion': 'P22 Top Box puro (Muy Importante) por segmento y marca preferida',
        'metodo': 'TB = solo valor 5 (Muy Importante). T2B = valores 4+5. IC95 Newcombe-Wilson.',
        'grupos': results,
        'reranking_summary': reranking_summary,
    }


# ─── E2 — EVALUACION VIABILIDAD + REGRESION LOGISTICA ──────────────────────

def e2_regresion(df):
    """
    E2: Primero evalua viabilidad (VIF, tamanios muestrales), luego decide si
    correr regresion logistica o recomendar alternativa (Shapley/KDA).
    DV: preferencia binaria por cada cadena (0/1).
    IV: 20 importancias P22 (1-5).
    """
    print("\nE2: Evaluacion viabilidad + Regresion logistica...")

    try:
        from statsmodels.stats.outliers_influence import variance_inflation_factor
        from statsmodels.api import Logit, add_constant
        STATSMODELS_OK = True
    except ImportError:
        STATSMODELS_OK = False
        print("  WARN: statsmodels no disponible — solo evaluacion VIF basica")

    # Construir matriz X de importancias P22 (continuas 1-5)
    attr_keys = list(P22_COLS.keys())
    X_raw = pd.DataFrame()
    for ak, col in P22_COLS.items():
        if col in df.columns:
            X_raw[ak] = df[col].apply(p22_score)

    X_clean = X_raw.dropna()
    n_obs = len(X_clean)
    print(f"  Observaciones con P22 completo: {n_obs}")

    # ── 1. VIF entre las 10 importancias P22 ──────────────────────────────
    vif_results = {}
    vif_max = None
    vif_high_count = 0

    if STATSMODELS_OK and len(X_clean) > len(attr_keys) + 5:
        try:
            from statsmodels.stats.outliers_influence import variance_inflation_factor
            from statsmodels.api import add_constant
            X_const = add_constant(X_clean.values.astype(float))
            # VIF para cada predictor (indices 1..k, index 0 es la constante)
            for i, ak in enumerate(X_clean.columns):
                try:
                    vif_val = float(variance_inflation_factor(X_const, i + 1))
                    vif_results[ak] = {
                        'nombre': ATRIBUTO_NOMBRES.get(ak, ak),
                        'vif': round(vif_val, 2),
                        'flag': 'ALTO (>10)' if vif_val > VIF_THRESHOLD else 'MEDIO (5-10)' if vif_val > 5 else 'OK (<5)',
                    }
                    if vif_val > VIF_THRESHOLD:
                        vif_high_count += 1
                    if vif_max is None or vif_val > vif_max:
                        vif_max = vif_val
                except Exception:
                    vif_results[ak] = {'nombre': ATRIBUTO_NOMBRES.get(ak, ak), 'vif': None, 'flag': 'ERROR'}
        except Exception as e:
            print(f"  VIF error: {e}")
    else:
        # Alternativa: correlaciones de Pearson entre predictores
        corr_matrix = X_clean.corr()
        max_corr = corr_matrix.where(~np.eye(len(corr_matrix), dtype=bool)).abs().max().max()
        vif_results['_nota'] = {
            'statsmodels': 'no disponible',
            'max_correlacion_pearson': round(float(max_corr), 3) if not np.isnan(max_corr) else None,
        }
        vif_max = max_corr * 10  # estimacion aproximada — VIF ~ 1/(1-R^2)

    # ── 2. Tamanios muestrales por cadena ─────────────────────────────────
    n_por_cadena = {}
    REGRESION_MIN_N = 50  # minimo para regresion logistica confiable

    for cadena in CADENAS_PRINCIPALES:
        mask = df['P21_val'].apply(lambda v: cadena_match(v, cadena))
        n_c = int(mask.sum())
        n_por_cadena[cadena] = {
            'n_pref': n_c,
            'n_no_pref': int(len(df) - n_c),
            'flag': flag_n(n_c),
            'viable_regresion': n_c >= REGRESION_MIN_N,
            'nota': (
                f'VIABLE — n={n_c} >= {REGRESION_MIN_N}' if n_c >= REGRESION_MIN_N
                else f'INVIABLE — n={n_c} < {REGRESION_MIN_N} minimo'
            ),
        }

    cadenas_viables = [c for c, v in n_por_cadena.items() if v['viable_regresion']]
    cadenas_inviables = [c for c, v in n_por_cadena.items() if not v['viable_regresion']]

    # ── 3. Decision de viabilidad ─────────────────────────────────────────
    vif_problematico = vif_high_count > 3 if isinstance(vif_high_count, int) else (
        vif_max is not None and vif_max > VIF_THRESHOLD * 1.5
    )
    bases_insuficientes = len(cadenas_viables) == 0
    regresion_viable = not bases_insuficientes  # si hay al menos 1 cadena viable, corremos

    decision = {
        'regresion_viable': regresion_viable,
        'vif_max': round(float(vif_max), 2) if vif_max is not None and not np.isnan(vif_max) else None,
        'vif_alto_count': vif_high_count,
        'vif_problematico': vif_problematico,
        'cadenas_viables': cadenas_viables,
        'cadenas_inviables': cadenas_inviables,
        'razon': '',
    }

    if regresion_viable and not vif_problematico:
        decision['razon'] = (
            f'Regresion logistica viable para {len(cadenas_viables)} cadenas ({", ".join(cadenas_viables)}). '
            f'VIF maximo={decision["vif_max"]} — multicolinealidad manejable. '
            f'Para cadenas con n<{REGRESION_MIN_N} ({", ".join(cadenas_inviables)}): resultados EXCLUIDOS (bases insuficientes).'
        )
        decision['metodo_recomendado'] = 'Regresion logistica (DV binaria correcta para preferencia 0/1)'
        decision['nota_cora'] = (
            'La solicitud de Cora fue "regresion lineal" — se usa logistica porque la DV (preferencia si/no) '
            'es binaria. La regresion lineal con DV binaria produce probabilidades fuera de [0,1] y residuos '
            'no-normales. El metodo logistico es el correcto; los coeficientes se interpretan como odds ratios.'
        )
    elif vif_problematico and regresion_viable:
        decision['razon'] = (
            f'VIF alto en {vif_high_count} predictores (max={decision["vif_max"]}). '
            'Regresion clasica sesgada. Recomendamos Kruskal Driver Analysis (KDA) o Shapley Value Regression '
            'que manejan multicolinealidad correctamente.'
        )
        decision['metodo_recomendado'] = 'KDA (Kruskal Driver Analysis) o Shapley Value Regression'
        decision['nota_alternativa'] = (
            'KDA descompone R^2 en contribuciones orthogonalizadas de cada predictor. '
            'Shapley Values reasigna varianza explicada proporcionalmente entre predictores correlacionados. '
            'Ambos son preferibles cuando VIF > 5 en multiples predictores.'
        )
    else:
        decision['razon'] = (
            'Ninguna cadena tiene n >= 50. Regresion no producira resultados confiables. '
            'Alternativa: analisis descriptivo de importancia media por grupo de preferentes vs no-preferentes.'
        )
        decision['metodo_recomendado'] = 'Descriptivo — diferencias de medias de importancia TB entre preferentes y no-preferentes'

    print(f"  Decision: regresion_viable={regresion_viable}, VIF_problematico={vif_problematico}")
    print(f"  Cadenas viables: {cadenas_viables}")

    # ── 4. Correr regresion logistica (solo cadenas viables) ──────────────
    regresiones = {}

    if regresion_viable and STATSMODELS_OK:
        from statsmodels.api import Logit, add_constant

        idx_completo = X_clean.index.intersection(df.index)
        X_model = X_clean.loc[idx_completo].astype(float)

        for cadena in cadenas_viables:
            print(f"  Corriendo logistica para: {cadena}...")
            try:
                y = df.loc[idx_completo, 'P21_val'].apply(
                    lambda v: int(cadena_match(v, cadena))
                )
                n_pos = int(y.sum())
                n_neg = int((y == 0).sum())

                if n_pos < 10 or n_neg < 10:
                    regresiones[cadena] = {'flag': f'EXCLUIR — n_positivos={n_pos} < 10'}
                    continue

                Xc = add_constant(X_model)
                model = Logit(y, Xc)
                result = model.fit(disp=False, maxiter=200)

                coefs = []
                for j, ak in enumerate(X_model.columns):
                    coef = float(result.params[ak]) if ak in result.params else None
                    se = float(result.bse[ak]) if ak in result.bse else None
                    pval = float(result.pvalues[ak]) if ak in result.pvalues else None
                    odds = float(np.exp(coef)) if coef is not None else None
                    sig = pval is not None and pval < ALPHA
                    coefs.append({
                        'atributo': ak,
                        'nombre': ATRIBUTO_NOMBRES.get(ak, ak),
                        'coef': round(coef, 4) if coef is not None else None,
                        'se': round(se, 4) if se is not None else None,
                        'pval': round(pval, 4) if pval is not None else None,
                        'odds_ratio': round(odds, 4) if odds is not None else None,
                        'significativo_alpha05': sig,
                        'interpretacion': (
                            f'OR={round(odds,2)}: un punto mas en importancia de {ATRIBUTO_NOMBRES.get(ak,ak)} '
                            f'{"aumenta" if coef > 0 else "reduce"} odds de preferir {cadena} en {abs(round((odds-1)*100,1))}%'
                        ) if coef is not None and odds is not None else 'error',
                    })

                coefs_sig = [c for c in coefs if c['significativo_alpha05']]
                coefs_sig_sort = sorted(coefs_sig, key=lambda x: abs(x.get('coef', 0) or 0), reverse=True)

                regresiones[cadena] = {
                    'n_total': int(n_pos + n_neg),
                    'n_pref': n_pos,
                    'n_no_pref': n_neg,
                    'pseudo_r2_mcfadden': round(float(result.prsquared), 4),
                    'llr_pval': round(float(result.llr_pvalue), 4) if result.llr_pvalue is not None else None,
                    'modelo_significativo': result.llr_pvalue is not None and result.llr_pvalue < ALPHA,
                    'coeficientes': coefs,
                    'coefs_significativos': coefs_sig_sort,
                    'n_coefs_sig': len(coefs_sig),
                    'flag': flag_n(n_pos),
                    'convergencia': result.mle_retvals.get('converged', True) if hasattr(result, 'mle_retvals') else True,
                }

            except Exception as e:
                regresiones[cadena] = {'flag': f'ERROR: {str(e)[:100]}'}

    elif regresion_viable and not STATSMODELS_OK:
        # Fallback descriptivo: diferencia de medias TB entre preferentes vs no-preferentes
        for cadena in cadenas_viables:
            mask_pref = df['P21_val'].apply(lambda v: cadena_match(v, cadena))
            df_pref = df[mask_pref]
            df_nopref = df[~mask_pref]
            diffs = []
            for ak, col in P22_COLS.items():
                if col not in df.columns: continue
                m_pref = float(df_pref[col].apply(p22_score).dropna().mean())
                m_nopref = float(df_nopref[col].apply(p22_score).dropna().mean())
                diffs.append({
                    'atributo': ak,
                    'nombre': ATRIBUTO_NOMBRES.get(ak, ak),
                    'media_pref': round(m_pref, 2),
                    'media_nopref': round(m_nopref, 2),
                    'diff': round(m_pref - m_nopref, 2),
                })
            diffs.sort(key=lambda x: abs(x['diff']), reverse=True)
            regresiones[cadena] = {
                'metodo': 'descriptivo_diferencia_medias',
                'n_pref': int(mask_pref.sum()),
                'diferencias_importancia': diffs,
                'flag': flag_n(int(mask_pref.sum())),
            }

    # ── 5. Chart: coeficientes significativos para cadenas viables ────────
    if regresion_viable and STATSMODELS_OK and regresiones:
        _plot_coefs(regresiones, cadenas_viables)

    return {
        'analisis': 'E2',
        'descripcion': 'Evaluacion viabilidad VIF + Regresion logistica drivers de preferencia',
        'metodo_aplicado': decision.get('metodo_recomendado', 'descriptivo'),
        'decision_viabilidad': decision,
        'vif_por_atributo': vif_results,
        'n_por_cadena': n_por_cadena,
        'regresiones': regresiones,
        'n_obs_completo': n_obs,
        'caveat': (
            'Regresion cross-sectional — causalidad no inferible. '
            'Cadenas con n_pref < 50 EXCLUIDAS. '
            'Pseudo-R2 McFadden: <0.1 pobre, 0.1-0.2 aceptable, 0.2-0.4 bueno para datos de survey.'
        ),
    }


def _plot_coefs(regresiones, cadenas_viables):
    """Plot de coeficientes significativos por cadena."""
    fig_count = 0
    for cadena in cadenas_viables:
        reg = regresiones.get(cadena, {})
        coefs_sig = reg.get('coefs_significativos', [])
        if not coefs_sig:
            continue

        nombres = [c['nombre'] for c in coefs_sig]
        coefs_v = [c['coef'] for c in coefs_sig]
        colors = [GAMA_RED if cadena == 'Gama' else COMP_COLORS.get(cadena, GAMA_GRAY_MID)
                  for _ in coefs_sig]

        fig, ax = plt.subplots(figsize=(10, max(4, len(nombres) * 0.5 + 1)))
        bars = ax.barh(nombres, coefs_v, color=colors, height=0.6)
        ax.axvline(0, color=GAMA_BLACK, lw=0.8, ls='-')
        ax.set_xlabel('Coeficiente logistico (B)')
        r2 = reg.get('pseudo_r2_mcfadden', 0)
        ax.set_title(
            f'Drivers de preferencia — {cadena}\n'
            f'Coefs significativos (p<.05) | Pseudo-R2 McFadden={r2:.3f} | n_pref={reg.get("n_pref")}',
            fontsize=11
        )
        for bar, cv in zip(bars, coefs_v):
            ax.text(cv + (0.01 if cv >= 0 else -0.01), bar.get_y() + bar.get_height()/2,
                    f'{cv:+.3f}', va='center', ha='left' if cv >= 0 else 'right', fontsize=8)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.tight_layout()
        cadena_safe = cadena.replace(' ', '_').replace('/', '_').lower()
        fpath = os.path.join(OUTPUT_PLOTS_DIR, f'cu10_coefs_{cadena_safe}.png')
        plt.savefig(fpath, dpi=150, bbox_inches='tight')
        plt.close()
        fig_count += 1
        print(f"  Plot guardado: {fpath}")

    print(f"  Total plots coefs: {fig_count}")


# ─── E3 — MUNDO DE MARCA P21 x P23 x P24/P25 ───────────────────────────────

def e3_mundo_marca(df, p24_cols_dict, p25_cols_dict):
    """
    Para cada cadena:
    1. Perfil P23 Total (% que asocia cada atributo con esa cadena)
    2. Cruce con P21: quienes prefieren esa cadena, mismo perfil P23
    3. Validacion con P24/P25 experiencia: filtra por quienes han comprado (P24) o compran habitualmente (P25)
    4. Tabla matriz 8 cadenas x atributos diferenciadores
    """
    print("\nE3: Mundo de marca P21 x P23 x Experiencia...")

    # ── Construir flags de experiencia por cadena ─────────────────────────
    # Primero detectar columnas P24 y P25 por cadena
    experiencia = {}
    for cadena in CADENAS_PRINCIPALES:
        cadena_s = cadena.lower()
        # Buscar col P24 con el nombre de la cadena
        p24_col = None
        for col in df.columns:
            if '{P24}' in col and cadena_s in col.lower():
                p24_col = col
                break
            # Buscar por alias
            if cadena == 'Central Madeirense' and '{P24}' in col and 'central' in col.lower():
                p24_col = col
                break
            if cadena == 'Plan Suarez' and '{P24}' in col and 'plan' in col.lower():
                p24_col = col
                break
            if cadena == 'Plazas' and '{P24}' in col and 'plaza' in col.lower():
                p24_col = col
                break
            if cadena == 'Luz' and '{P24}' in col and ('luz' in col.lower()):
                p24_col = col
                break

        p25_col = None
        for col in df.columns:
            if '{P25}' in col and cadena_s in col.lower():
                p25_col = col
                break
            if cadena == 'Central Madeirense' and '{P25}' in col and 'central' in col.lower():
                p25_col = col
                break
            if cadena == 'Plan Suarez' and '{P25}' in col and 'plan' in col.lower():
                p25_col = col
                break
            if cadena == 'Plazas' and '{P25}' in col and 'plaza' in col.lower():
                p25_col = col
                break
            if cadena == 'Luz' and '{P25}' in col and ('luz' in col.lower()):
                p25_col = col
                break

        experiencia[cadena] = {'p24_col': p24_col, 'p25_col': p25_col}
        if p24_col:
            df[f'exp_p24_{cadena}'] = df[p24_col].apply(is_yes)
        else:
            df[f'exp_p24_{cadena}'] = False
        if p25_col:
            df[f'exp_p25_{cadena}'] = df[p25_col].apply(is_yes)
        else:
            df[f'exp_p25_{cadena}'] = False

    print(f"  Cols P24 por cadena: { {c: bool(experiencia[c]['p24_col']) for c in CADENAS_PRINCIPALES} }")
    print(f"  Cols P25 por cadena: { {c: bool(experiencia[c]['p25_col']) for c in CADENAS_PRINCIPALES} }")

    # ── Calcular asociacion P23 por cadena x atributo ─────────────────────
    def perfil_p23(df_grp, n_base_total):
        """Para cada atributo, % del n_base_total que asocia ese atributo con una cadena dada."""
        pass  # se calcula inline abajo

    n_total = len(df)
    resultados_cadenas = {}

    for cadena in CADENAS_PRINCIPALES:
        print(f"  Procesando {cadena}...")

        # Subsets
        mask_pref = df['P21_val'].apply(lambda v: cadena_match(v, cadena))
        mask_p24 = df[f'exp_p24_{cadena}']
        mask_p25 = df[f'exp_p25_{cadena}']
        mask_exp_alguna = mask_p24 | mask_p25
        mask_exp_habitual = mask_p25

        n_pref = int(mask_pref.sum())
        n_p24 = int(mask_p24.sum())
        n_p25 = int(mask_p25.sum())
        n_exp_alguna = int(mask_exp_alguna.sum())

        grupos_calc = {
            'Total': (df, n_total),
            'Pref': (df[mask_pref], n_pref),
            'Exp_alguna_vez': (df[mask_exp_alguna], n_exp_alguna),
            'Exp_habitual': (df[mask_p25], n_p25),
        }

        atributos_cadena = {}
        for attr_k, p23_prefix in P23_COLS.items():
            # Encontrar la columna real P23 para este atributo x cadena
            # La columna tiene el nombre de la cadena en ella, como en cu9
            p23_col_encontrada = None
            for col in df.columns:
                if p23_prefix.strip().lower()[:30] in col.strip().lower():
                    # Esta es la columna P23 para este atributo (una por atributo)
                    p23_col_encontrada = col
                    break

            if p23_col_encontrada is None:
                # buscar de forma mas flexible
                keywords = p23_prefix.strip().lower().split()[:4]
                for col in df.columns:
                    col_l = col.strip().lower()
                    if sum(1 for kw in keywords if kw in col_l) >= 3:
                        p23_col_encontrada = col
                        break

            if p23_col_encontrada is None:
                atributos_cadena[attr_k] = {g: None for g in grupos_calc}
                continue

            por_grupo = {}
            for grp_name, (df_grp, n_grp) in grupos_calc.items():
                if n_grp < BASE_EXCLUIR:
                    por_grupo[grp_name] = {'pct': None, 'n': n_grp, 'flag': 'EXCLUIR'}
                    continue
                # Contar menciones de esta cadena en esta col de atributo
                n_ment = int(df_grp[p23_col_encontrada].apply(
                    lambda v: p23_has_cadena(v, cadena)
                ).sum())
                p = pct(n_ment, n_grp)
                ci_lo, ci_hi = newcombe_ci(n_ment, n_grp)
                por_grupo[grp_name] = {
                    'pct': p,
                    'n_ment': n_ment,
                    'n_base': n_grp,
                    'ic95_lo': round(ci_lo * 100, 1),
                    'ic95_hi': round(ci_hi * 100, 1),
                    'flag': flag_n(n_grp),
                }
            atributos_cadena[attr_k] = por_grupo

        # Z-scores para identificar atributos diferenciadores de esta cadena (vs media de mercado)
        # Usamos los porcentajes Total de P23 de la BBDD entera (calculados sobre n_total)
        pcts_total = {}
        for attr_k, por_grp in atributos_cadena.items():
            v = por_grp.get('Total')
            pcts_total[attr_k] = v['pct'] if v and v.get('pct') is not None else 0.0

        # Media de mercado: promedio de % de asociacion de TODAS las cadenas por atributo
        # (necesitariamos calcular para todas las cadenas, usamos simplificacion:
        # el "z" de esta cadena vs las otras cadenas se calcula al final)

        # Hallazgos por cadena: top atributos, brecha pref vs total, brecha exp vs total
        top_atrs_total = sorted(pcts_total.items(), key=lambda x: x[1], reverse=True)[:5]

        brechas_pref_vs_total = {}
        for attr_k, por_grp in atributos_cadena.items():
            t = por_grp.get('Total')
            p = por_grp.get('Pref')
            if t and p and t.get('pct') is not None and p.get('pct') is not None and n_pref >= BASE_EXCLUIR:
                brechas_pref_vs_total[attr_k] = round(p['pct'] - t['pct'], 1)

        brechas_exp_vs_total = {}
        for attr_k, por_grp in atributos_cadena.items():
            t = por_grp.get('Total')
            e = por_grp.get('Exp_alguna_vez')
            if t and e and t.get('pct') is not None and e.get('pct') is not None and n_exp_alguna >= BASE_EXCLUIR:
                brechas_exp_vs_total[attr_k] = round(e['pct'] - t['pct'], 1)

        resultados_cadenas[cadena] = {
            'n_pref': n_pref,
            'n_pref_flag': flag_n(n_pref),
            'n_exp_p24': n_p24,
            'n_exp_p25': n_p25,
            'n_exp_alguna': n_exp_alguna,
            'p24_col_encontrada': bool(experiencia[cadena]['p24_col']),
            'p25_col_encontrada': bool(experiencia[cadena]['p25_col']),
            'atributos': atributos_cadena,
            'top5_por_asociacion_total': [(a, round(v, 1)) for a, v in top_atrs_total],
            'brechas_pref_vs_total': brechas_pref_vs_total,
            'brechas_exp_vs_total': brechas_exp_vs_total,
        }

    # ── Tabla matriz comparativa: 8 cadenas x 10 atributos ────────────────
    # Identificar 5-7 atributos mas diferenciadores (mayor varianza entre cadenas)
    atrs_varianza = {}
    for attr_k in list(P23_COLS.keys()):
        vals = []
        for cadena in CADENAS_PRINCIPALES:
            v = resultados_cadenas[cadena]['atributos'].get(attr_k, {}).get('Total')
            if v and v.get('pct') is not None:
                vals.append(v['pct'])
        if len(vals) >= 4:
            atrs_varianza[attr_k] = float(np.std(vals))

    top_diff_attrs = sorted(atrs_varianza.items(), key=lambda x: x[1], reverse=True)[:7]
    top_diff_attr_keys = [a for a, _ in top_diff_attrs]

    # Tabla Total
    tabla_total = _build_tabla(resultados_cadenas, top_diff_attr_keys, 'Total')
    tabla_exp = _build_tabla(resultados_cadenas, top_diff_attr_keys, 'Exp_alguna_vez')

    # Z-scores inter-cadena para cada atributo en la tabla total
    zscores_tabla = {}
    for attr_k in top_diff_attr_keys:
        vals = [resultados_cadenas[c]['atributos'].get(attr_k, {}).get('Total', {})
                for c in CADENAS_PRINCIPALES]
        pcts_v = [v.get('pct', 0) if v and v.get('pct') is not None else 0 for v in vals]
        m, s = np.mean(pcts_v), np.std(pcts_v)
        if s < 0.01: s = 0.01
        zscores_tabla[attr_k] = {
            c: round((pcts_v[i] - m) / s, 2)
            for i, c in enumerate(CADENAS_PRINCIPALES)
        }

    # Mundo de marca: top 3-4 atributos por cadena + atributo sombra
    mundos = {}
    for cadena in CADENAS_PRINCIPALES:
        top_atr = resultados_cadenas[cadena]['top5_por_asociacion_total']
        top3 = [ATRIBUTO_NOMBRES.get(a, a) for a, _ in top_atr[:3]]
        # Atributo sombra: atributo que para los PREFERENTES es mucho mas alto que para el total
        brechas_pref = resultados_cadenas[cadena]['brechas_pref_vs_total']
        if brechas_pref:
            sombra_k = max(brechas_pref, key=lambda x: brechas_pref[x])
            sombra_v = brechas_pref[sombra_k]
            if sombra_v > 5 and ATRIBUTO_NOMBRES.get(sombra_k, sombra_k) not in top3:
                sombra = f'{ATRIBUTO_NOMBRES.get(sombra_k, sombra_k)} (+{sombra_v:.0f}pp en preferentes)'
            else:
                sombra = None
        else:
            sombra = None

        mundos[cadena] = {
            'top3_atributos': top3,
            'cuarto_atributo': ATRIBUTO_NOMBRES.get(top_atr[3][0] if len(top_atr) > 3 else None, ''),
            'atributo_sombra': sombra,
            'n_pref': resultados_cadenas[cadena]['n_pref'],
            'flag': resultados_cadenas[cadena]['n_pref_flag'],
        }

    # ── Plots ─────────────────────────────────────────────────────────────
    _plot_heatmap_mundo(tabla_total, top_diff_attr_keys, 'Total')
    _plot_heatmap_mundo(tabla_exp, top_diff_attr_keys, 'Exp_alguna_vez')
    _plot_mundo_gama(resultados_cadenas, mundos)

    return {
        'analisis': 'E3',
        'descripcion': 'Mundo de marca por cadena: P21 x P23 x Experiencia (P24/P25)',
        'atributos_diferenciadores_usados': top_diff_attr_keys,
        'varianza_por_atributo': {a: round(v, 2) for a, v in top_diff_attrs},
        'resultados_cadenas': resultados_cadenas,
        'tabla_total': tabla_total,
        'tabla_exp_alguna_vez': tabla_exp,
        'zscores_intercadena': zscores_tabla,
        'mundos_de_marca': mundos,
        'caveat': (
            'n_pref < 30 en la mayoria de cadenas — REFERENCIAL. '
            'P24/P25: columnas detectadas automaticamente; verificar en .json campo p24_col_encontrada. '
            'Z-scores inter-cadena son descriptivos, no inferenciales.'
        ),
    }


def _build_tabla(resultados_cadenas, attr_keys, grupo):
    """Construye tabla diccionario: cadena -> {atributo: pct}."""
    tabla = {}
    for cadena in CADENAS_PRINCIPALES:
        tabla[cadena] = {}
        for attr_k in attr_keys:
            por_grp = resultados_cadenas[cadena]['atributos'].get(attr_k, {})
            v = por_grp.get(grupo)
            if v and v.get('pct') is not None:
                tabla[cadena][attr_k] = {
                    'pct': v['pct'],
                    'flag': v.get('flag', flag_n(v.get('n_base', 0))),
                }
            else:
                tabla[cadena][attr_k] = {'pct': None, 'flag': 'N/D'}
    return tabla


def _plot_heatmap_mundo(tabla, attr_keys, grupo_label):
    """Heatmap cadenas x atributos diferenciadores."""
    cadenas_plot = CADENAS_PRINCIPALES
    attr_nombres = [ATRIBUTO_NOMBRES.get(a, a) for a in attr_keys]

    data = []
    for cadena in cadenas_plot:
        row = []
        for attr_k in attr_keys:
            v = tabla[cadena].get(attr_k, {})
            row.append(v.get('pct') or 0)
        data.append(row)

    Z = np.array(data, dtype=float)

    fig, ax = plt.subplots(figsize=(14, 6))
    cmap = LinearSegmentedColormap.from_list('gama', ['#FFFFFF', '#F5C8C8', GAMA_RED])
    im = ax.imshow(Z, aspect='auto', cmap=cmap, vmin=0, vmax=50)

    ax.set_xticks(range(len(attr_nombres)))
    ax.set_xticklabels(attr_nombres, rotation=30, ha='right', fontsize=9)
    ax.set_yticks(range(len(cadenas_plot)))
    ax.set_yticklabels(cadenas_plot, fontsize=10)

    for i, cadena in enumerate(cadenas_plot):
        for j, attr_k in enumerate(attr_keys):
            v = Z[i, j]
            txt_col = 'white' if v > 30 else GAMA_BLACK
            ax.text(j, i, f'{v:.0f}%', ha='center', va='center', fontsize=8, color=txt_col)

    plt.colorbar(im, ax=ax, shrink=0.7, label='% asociacion')
    grp_title = 'Total n=403' if grupo_label == 'Total' else 'Filtrado por experiencia de compra'
    ax.set_title(
        f'Mundo de marca: Asociacion cadena x atributo (P23) — {grp_title}\n'
        'Atributos mas diferenciadores (mayor varianza inter-cadena)',
        fontsize=11
    )
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    grp_safe = grupo_label.replace('/', '_').lower()
    fpath = os.path.join(OUTPUT_PLOTS_DIR, f'cu10_heatmap_mundo_{grp_safe}.png')
    plt.savefig(fpath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot guardado: {fpath}")


def _plot_mundo_gama(resultados_cadenas, mundos):
    """Tornado chart: Gama vs mercado en atributos diferenciadores."""
    gama_data = resultados_cadenas.get('Gama', {})
    gama_attrs = gama_data.get('atributos', {})

    attr_keys = list(P23_COLS.keys())
    gama_pcts = []
    labels = []
    market_means = []

    for attr_k in attr_keys:
        grp = gama_attrs.get(attr_k, {}).get('Total', {})
        if grp and grp.get('pct') is not None:
            gama_pcts.append(grp['pct'])
            labels.append(ATRIBUTO_NOMBRES.get(attr_k, attr_k))
            # Media de mercado para este atributo
            vals = []
            for c in CADENAS_PRINCIPALES:
                v = resultados_cadenas[c]['atributos'].get(attr_k, {}).get('Total', {})
                if v and v.get('pct') is not None:
                    vals.append(v['pct'])
            market_means.append(np.mean(vals) if vals else 0)

    if not gama_pcts:
        return

    pairs = sorted(zip(labels, gama_pcts, market_means), key=lambda x: x[1], reverse=True)
    labels_s, gama_s, mkt_s = zip(*pairs)

    x = np.arange(len(labels_s))
    width = 0.35
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.barh(x + width/2, gama_s, width, label='Gama', color=GAMA_RED, alpha=0.9)
    ax.barh(x - width/2, mkt_s, width, label='Media mercado', color=GAMA_GRAY_MID, alpha=0.7)
    ax.set_yticks(x)
    ax.set_yticklabels(labels_s, fontsize=9)
    ax.set_xlabel('% asociacion P23 (Total n=403)')
    ax.set_title('Gama vs media de mercado — Asociacion atributos P23', fontsize=12, color=GAMA_RED)
    ax.legend(fontsize=9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    fpath = os.path.join(OUTPUT_PLOTS_DIR, 'cu10_gama_vs_mercado_p23.png')
    plt.savefig(fpath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot guardado: {fpath}")


# ─── E1 CHART: Heatmap TB puro por marca preferida ──────────────────────────

def plot_e1_heatmap(e1_results):
    """Heatmap: marcas preferidas (cols) x atributos P22 (filas) — % TB."""
    grupos = e1_results.get('grupos', {})
    cadenas_cols = ['Total', 'C+/C'] + [f'Pref-{c}' for c in CADENAS_PRINCIPALES]
    cadenas_cols = [g for g in cadenas_cols if g in grupos]
    attr_keys = list(P22_COLS.keys())
    attr_nombres = [ATRIBUTO_NOMBRES[a] for a in attr_keys]

    # Construir matriz
    data = []
    for attr_k in attr_keys:
        row = []
        for grp in cadenas_cols:
            items = grupos[grp].get('items', [])
            item = next((i for i in items if i['atributo'] == attr_k), None)
            row.append(item['pct_tb'] if item else 0)
        data.append(row)

    Z = np.array(data, dtype=float)
    fig, ax = plt.subplots(figsize=(16, 7))
    cmap = LinearSegmentedColormap.from_list('tb', ['#FFFFFF', '#FCE8E8', GAMA_RED])
    im = ax.imshow(Z, aspect='auto', cmap=cmap, vmin=0, vmax=100)

    ax.set_xticks(range(len(cadenas_cols)))
    col_labels = [g.replace('Pref-', '') for g in cadenas_cols]
    ax.set_xticklabels(col_labels, rotation=40, ha='right', fontsize=8)
    ax.set_yticks(range(len(attr_nombres)))
    ax.set_yticklabels(attr_nombres, fontsize=9)

    for i in range(len(attr_keys)):
        for j in range(len(cadenas_cols)):
            v = Z[i, j]
            flag = grupos[cadenas_cols[j]].get('flag', 'OK')
            txt = f'{v:.0f}%' + ('' if flag == 'OK' else '*')
            ax.text(j, i, txt, ha='center', va='center',
                    fontsize=7, color='white' if v > 60 else GAMA_BLACK)

    plt.colorbar(im, ax=ax, shrink=0.7, label='% Muy Importante (TB)')
    ax.set_title(
        'P22 Top Box puro (Muy Importante) por segmento y marca preferida\n'
        '* = base REFERENCIAL (n<30)',
        fontsize=11
    )
    plt.tight_layout()
    fpath = os.path.join(OUTPUT_PLOTS_DIR, 'cu10_heatmap_tb_puro.png')
    plt.savefig(fpath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot E1 guardado: {fpath}")


def plot_e1_reranking(e1_results):
    """Tornado: atributos por ranking TB vs T2B en Total."""
    grupos = e1_results.get('grupos', {})
    total_items = grupos.get('Total', {}).get('items', [])
    if not total_items:
        return

    items_sorted_tb = sorted(total_items, key=lambda x: x.get('ranking_tb', 99))
    nombres = [ATRIBUTO_NOMBRES[i['atributo']] for i in items_sorted_tb]
    tb_pcts = [i['pct_tb'] for i in items_sorted_tb]
    t2b_pcts = [i['pct_t2b'] for i in items_sorted_tb]

    x = np.arange(len(nombres))
    width = 0.35
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.barh(x + width/2, tb_pcts, width, label='Top Box (Muy Importante)', color=GAMA_RED, alpha=0.9)
    ax.barh(x - width/2, t2b_pcts, width, label='Top 2 Box (Importante + Muy Importante)',
            color=GAMA_GRAY_MID, alpha=0.7)
    ax.set_yticks(x)
    ax.set_yticklabels(nombres, fontsize=9)
    ax.set_xlabel('% respuestas')
    ax.set_title('P22 — Top Box puro vs Top 2 Box: ¿cambia el ranking?\nTotal n=403', fontsize=11)
    ax.legend(fontsize=9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    fpath = os.path.join(OUTPUT_PLOTS_DIR, 'cu10_tb_vs_t2b_reranking.png')
    plt.savefig(fpath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot E1 reranking guardado: {fpath}")


# ─── MAIN ────────────────────────────────────────────────────────────────────

def main():
    os.makedirs(OUTPUT_PLOTS_DIR, exist_ok=True)

    df, p24_cols_dict, p25_cols_dict = load_bbdd()

    # Imprimir columnas P22 disponibles para validar antes de correr
    print("\nValidando columnas P22...")
    for ak, col in P22_COLS.items():
        encontrada = col in df.columns
        if not encontrada:
            # Buscar alternativa flexible
            alt = [c for c in df.columns if 'P22' in c and ak in c.lower()]
            print(f"  {ak}: {'OK' if encontrada else 'NO ENCONTRADA'} {('-> alt: '+alt[0][:50]) if alt else ''}")
        else:
            sample = df[col].value_counts().head(3).to_dict()
            print(f"  {ak}: OK | vals={sample}")

    print("\nValidando columnas P23...")
    for ak, prefix in P23_COLS.items():
        matches = [c for c in df.columns if prefix.strip().lower()[:25] in c.strip().lower()]
        print(f"  {ak}: {'OK ('+str(len(matches))+' cols)' if matches else 'NO ENCONTRADA'}")

    print("\nMuestra P21_val:")
    print(df['P21_val'].value_counts().head(12).to_dict())

    print("\n--- Corriendo E1, E2, E3 ---")

    e1 = e1_topbox(df)
    plot_e1_heatmap(e1)
    plot_e1_reranking(e1)

    e2 = e2_regresion(df)

    e3 = e3_mundo_marca(df, p24_cols_dict, p25_cols_dict)

    output = {
        'metadata': {
            'proyecto': 'Gama Notoriedad 2026',
            'cu': 'CU-10',
            'version': 'v8',
            'fecha': '2026-05-18',
            'n_total': len(df),
            'n_cc': int((df['NSE_harm'] == 'C+/C').sum()),
            'n_pg': int(df['pref_gama'].sum()),
            'alpha': ALPHA,
            'base_baja': BASE_BAJA,
            'vif_threshold': VIF_THRESHOLD,
            'ic_method': 'Newcombe-Wilson',
            'script': 'cu10_v8_analisis.py',
        },
        'E1_topbox_puro': e1,
        'E2_regresion_logistica': e2,
        'E3_mundo_marca': e3,
    }

    dump_json(output, OUTPUT_JSON)
    print(f"\nJSON: {OUTPUT_JSON}")
    print(f"Plots: {OUTPUT_PLOTS_DIR}")
    print(f"\n=== RESUMEN ===")
    print(f"  n Total={len(df)} | C+/C={int((df['NSE_harm']=='C+/C').sum())} | Pref-Gama={int(df['pref_gama'].sum())} (REFERENCIAL)")
    reg_dec = e2.get('decision_viabilidad', {})
    print(f"  E2 regresion viable: {reg_dec.get('regresion_viable')} | VIF max: {reg_dec.get('vif_max')}")
    print(f"  Cadenas con regresion: {reg_dec.get('cadenas_viables', [])}")
    print(f"  E3 mundos calculados: {list(e3.get('mundos_de_marca', {}).keys())}")

    return output


if __name__ == '__main__':
    main()
