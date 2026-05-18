"""
cu10_v8_e3_fix.py — Recalculo E3 Mundo de marca con estructura P23 correcta.
Extiende el JSON CU10 con E3 recalculado y E1/E2 del JSON existente.

Estructura P23 real (verificada 2026-05-18):
  Patron col: ' {P23:N} [VXXX] Descripcion atributo - NombreCadena'
  Hay 11 cols por atributo: una por cadena + Ninguno en particular
  La col tiene NaN si el respondente NO escoge esa cadena para ese atributo.
  La col tiene el nombre de la cadena si el respondente SI la escoge.
  Denominador correcto: n total muestra (cualquiera pudo mencionar cualquier cadena).

P24 real: '{P24} [V242] Donde realizo su ultima compra' — una sola col, valor = nombre cadena.
P25 real: '{P25} [V249] Razon ultima compra' — razon/mision, no cadena actual.
P26 real: Mision de compra por tipo de mision, valor = nombre cadena.
  Experiencia de marca usada aqui = P24 (ultima compra = experiencia real reciente)
  P26 = cadena habitual por mision = experiencia habitual (complemento).

Nota: no hay columna 'alguna vez ha comprado' separada en esta BBDD.
Se usan como proxies de experiencia:
  exp_reciente: P24 == cadena (ultima compra en esa cadena)
  exp_habitual: alguna P26 == cadena (cadena habitual para alguna mision)
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
warnings.filterwarnings('ignore')

# ─── CONSTANTES ──────────────────────────────────────────────────────────────

BBDD_PATH = (
    'G:/Mi unidad/RAUL/colaboradores/Genteca/Cora-Urrea/'
    '01_De_Cora_Para_Raoul/Notoriedad V2.0/BBDD Notoriedad 2026.xlsx'
)

INPUT_JSON = (
    'C:/rAUL/03-projects/consultoria-externa/gama-notoriedad-2026/'
    '02-analysis/cuanti/outputs/json/CU10_v8_analisis_20260518.json'
)

OUTPUT_JSON = INPUT_JSON  # Sobreescribir con datos correctos

OUTPUT_PLOTS_DIR = (
    'C:/rAUL/03-projects/consultoria-externa/gama-notoriedad-2026/'
    '02-analysis/cuanti/outputs/plots/'
)

BASE_BAJA = 30
BASE_EXCLUIR = 10
ALPHA = 0.05

GAMA_RED = '#E30613'
GAMA_BLACK = '#1A1A1A'
GAMA_GRAY_MID = '#6B6B6B'
GAMA_GRAY_LIGHT = '#E5E5E5'
GAMA_AMBER = '#F2A900'

COMP_COLORS = {
    'Paramo': '#4A6FA5', 'Rio': '#7C8B9B', 'Plan Suarez': '#9CAEC0',
    'Central Madeirense': '#5B7090', 'Forum': '#8FA3B8',
    'Plazas': '#6D8499', 'Luz': '#A8B9C7', 'La Muralla': '#BCC9D4',
}

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Open Sans', 'Calibri', 'Arial', 'DejaVu Sans'],
    'font.size': 10, 'axes.titlesize': 12, 'axes.titleweight': 'bold',
    'figure.facecolor': 'white', 'axes.facecolor': 'white',
    'grid.color': GAMA_GRAY_LIGHT,
})

CADENAS_PRINCIPALES = [
    'Gama', 'Paramo', 'Rio', 'Plan Suarez',
    'Central Madeirense', 'Forum', 'Plazas', 'Luz'
]

ATRIBUTO_NOMBRES = {
    'limpieza': 'Limpieza/orden', 'surtido': 'Mayor surtido',
    'seguro': 'Seguro', 'rapidez': 'Rapidez caja',
    'menor_precio': 'Menor precio', 'atractiva': 'Tienda atractiva',
    'promociones': 'Promociones', 'calidad': 'Mayor calidad',
    'atencion': 'Mejor atencion', 'valer_dinero': 'Valer dinero',
}

# Numeros de pregunta P23 por atributo
P23_ATTR_NUMS = {
    'surtido': '{P23:1}', 'calidad': '{P23:2}', 'menor_precio': '{P23:3}',
    'atencion': '{P23:4}', 'promociones': '{P23:5}', 'atractiva': '{P23:6}',
    'limpieza': '{P23:8}', 'seguro': '{P23:12}', 'rapidez': '{P23:13}',
    'valer_dinero': '{P23:21}',
}

# Alias de cadenas para matching de valores en cols P23
CADENA_ALIASES_P23 = {
    'Gama': ['gama', 'excelsior'], 'Paramo': ['paramo'], 'Rio': ['rio'],
    'Plan Suarez': ['plan suarez'], 'Central Madeirense': ['central madeirense'],
    'Forum': ['forum'], 'Plazas': ["plaza's", 'plazas', "plaza´s"],
    'Luz': ['luz marina', 'luz'], 'La Muralla': ['la muralla'],
    'Hiper Lider': ['hiper lider'],
}

def _cadena_std_from_val(val):
    v = str(val).strip().lower()
    for cstd, aliases in CADENA_ALIASES_P23.items():
        if any(a == v or a in v for a in aliases):
            return cstd
    return None

# P23_ATTR_PREFIXES alias for backward compat (used in varianza loop)
P23_ATTR_PREFIXES = P23_ATTR_NUMS

P21_COL = ' {P21} [V194] Preferido'
NSE_COL = ' {PD4} [V153] Marcar nse zona'
P24_COL = ' {P24} [V242] Donde realizo su ultima compra'

# Misiones de compra P26 (para experiencia habitual)
P26_COLS = [
    ' {P26} [V819] MISION DE COMPRA Hacer abastecimiento general y completo de mi hogar (todo tipo de víveres y productos de aseo)',
    ' {P26} [V820] MISION DE COMPRA Realizar algunas compras para reabastecer mi hogar antes de volver a hacer un mercado grande (frutas, verduras, leche u otro tipo de productos perecederos)',
    ' {P26} [V821] MISION DE COMPRA Comprar electrodomesticos, ropa, muebles, ferretería, jardinería o productos de tecnología',
    ' {P26} [V822] MISION DE COMPRA Comprar viveres para un evento, una fiesta, una celebración o una ocasión especial:',
    ' {P26} [V823] MISION DE COMPRA Comprar unos pocos productos con urgencia (comidas preparadas o para llevar, ingrediente faltante en una receta, medicamento para el dolor de cabeza, etc:)',
]

# ─── UTILS ──────────────────────────────────────────────────────────────────

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer,)): return int(obj)
        if isinstance(obj, (np.floating,)): return float(obj) if not np.isnan(obj) else None
        if isinstance(obj, (np.bool_,)): return bool(obj)
        if isinstance(obj, np.ndarray): return obj.tolist()
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

def flag_n(n): return 'EXCLUIR' if n < BASE_EXCLUIR else ('REFERENCIAL' if n < BASE_BAJA else 'OK')
def pct(k, n): return round(100 * k / n, 1) if n > 0 else 0.0

def is_gama(val):
    if pd.isna(val): return False
    return 'gama' in str(val).lower() or 'excelsior' in str(val).lower()

def nse_harm(v):
    v = str(v).strip()
    if v in ('C+', 'C', 'C+/C'): return 'C+/C'
    return v if v in ('D', 'E') else 'Otro'

def cadena_match_p21(p21_val, cadena_name):
    """True si P21 preferido matchea la cadena."""
    if pd.isna(p21_val): return False
    v = str(p21_val).strip().lower()
    aliases = {
        'gama': ['gama', 'excelsior'],
        'central madeirense': ['central madeirense', 'central'],
        'plan suarez': ['plan suarez', 'plan su'],
        'plazas': ["plaza´s", "plazas", "plaza's"],
        'luz': ['luz marina', 'luz'],
    }
    terms = aliases.get(cadena_name.lower(), [cadena_name.lower()])
    return any(t in v for t in terms)


# ─── IDENTIFICAR COLUMNAS P23 POR ATRIBUTO Y CADENA ────────────────────────

def build_p23_index(df):
    """
    Construye indice: {attr_key: {cadena_name: col_name}}
    Estrategia robusta: identifica la cadena por el VALOR UNICO de la columna.
    Cada col P23 contiene solo el nombre de una cadena si hay mencion, NaN si no.
    """
    index = {ak: {} for ak in P23_ATTR_NUMS}

    for col in df.columns:
        if '{P23:' not in col:
            continue
        # Identificar atributo por numero
        attr_k = None
        for ak, pnum in P23_ATTR_NUMS.items():
            if pnum in col:
                attr_k = ak
                break
        if attr_k is None:
            continue
        # Identificar cadena por valor unico de la columna
        unique_vals = df[col].dropna().unique()
        if len(unique_vals) == 1:
            cadena_std = _cadena_std_from_val(unique_vals[0])
            if cadena_std:
                index[attr_k][cadena_std] = col

    # Validar
    for attr_k, cadena_dict in index.items():
        missing = [c for c in CADENAS_PRINCIPALES if c not in cadena_dict]
        if missing:
            print(f"  WARN P23 {attr_k}: cadenas no encontradas: {missing}")

    return index



def _normalize_cadena_name(suffix):
    """Mapea el sufijo de columna al nombre estandar de cadena."""
    s = suffix.strip()
    norm_map = {
        'Gama': 'Gama',
        'Paramo': 'Paramo',
        'Rio': 'Rio',
        'Plan Suarez': 'Plan Suarez',
        'Central Madeirense': 'Central Madeirense',
        'Forum': 'Forum',
        "Plaza´s": 'Plazas',
        "Plaza's": 'Plazas',
        'Plazas': 'Plazas',
        'Luz': 'Luz',
        'Luz Marina': 'Luz',
        'La Muralla': 'La Muralla',
        'Hiper Lider': 'Hiper Lider',
        'Ninguno en particular': None,
    }
    return norm_map.get(s, None)


# ─── CARGAR BBDD ─────────────────────────────────────────────────────────────

def load_bbdd():
    print("Cargando BBDD 2026...")
    df = pd.read_excel(BBDD_PATH, engine='openpyxl')
    df['NSE_harm'] = df[NSE_COL].apply(nse_harm)
    df['P21_val'] = df[P21_COL].astype(str).str.strip()
    df['pref_gama'] = df['P21_val'].apply(is_gama)

    # P24 — ultima compra (experiencia reciente)
    p24_col_real = None
    for c in df.columns:
        if '{P24}' in c and 'V242' in c:
            p24_col_real = c
            break
    if not p24_col_real:
        for c in df.columns:
            if '{P24}' in c:
                p24_col_real = c
                break

    if p24_col_real:
        df['P24_cadena'] = df[p24_col_real].astype(str).str.strip()
        print(f"  P24 col: {p24_col_real[:60]}")
        print(f"  P24 top valores: {df['P24_cadena'].value_counts().head(5).to_dict()}")
    else:
        df['P24_cadena'] = ''
        print("  WARN: P24 col no encontrada")

    # P26 — mision de compra habitual (experiencia habitual por mision)
    p26_cols_real = [c for c in df.columns if '{P26}' in c]
    print(f"  P26 cols encontradas: {len(p26_cols_real)}")

    n_total = len(df)
    n_cc = int((df['NSE_harm'] == 'C+/C').sum())
    n_pg = int(df['pref_gama'].sum())
    print(f"  Total n={n_total} | C+/C n={n_cc} | Pref-Gama n={n_pg}")

    return df, p24_col_real, p26_cols_real


# ─── E3 CORRECTO: MUNDO DE MARCA ─────────────────────────────────────────────

def e3_mundo_marca(df, p24_col_real, p26_cols_real):
    """
    E3 con estructura P23 correcta.
    Para cada cadena:
      1. Perfil P23 Total (% que asocia cada atributo con esa cadena, base = n total)
      2. Perfil P23 entre sus PREFERENTES (P21 == esa cadena)
      3. Brecha preferentes vs total (diferencia pp)
      4. Perfil P23 entre quienes tuvieron experiencia reciente (P24 == esa cadena)
      5. Brecha experiencia vs total
      6. Perfil P23 entre quienes la mencionan como habitual en alguna mision (P26)
    """
    print("\nE3 (correcto): Mundo de marca con P23 indexado...")

    p23_index = build_p23_index(df)
    n_total = len(df)

    # Flags de experiencia por cadena
    for cadena in CADENAS_PRINCIPALES:
        # Experiencia reciente = ultima compra ahi (P24)
        df[f'exp_reciente_{cadena}'] = df['P24_cadena'].apply(
            lambda v: cadena_match_p21(v, cadena)
        )
        # Experiencia habitual = mencionada en alguna mision P26
        hab_mask = pd.Series(False, index=df.index)
        for p26c in p26_cols_real:
            if p26c in df.columns:
                hab_mask = hab_mask | df[p26c].astype(str).str.strip().apply(
                    lambda v: cadena_match_p21(v, cadena)
                )
        df[f'exp_habitual_{cadena}'] = hab_mask

    # Calcular asociacion P23 por atributo x cadena x segmento
    resultados = {}

    for cadena in CADENAS_PRINCIPALES:
        print(f"  {cadena}...")
        mask_pref = df['P21_val'].apply(lambda v: cadena_match_p21(v, cadena))
        mask_exp_rec = df[f'exp_reciente_{cadena}']
        mask_exp_hab = df[f'exp_habitual_{cadena}']
        mask_exp_alguna = mask_exp_rec | mask_exp_hab

        n_pref = int(mask_pref.sum())
        n_exp_rec = int(mask_exp_rec.sum())
        n_exp_hab = int(mask_exp_hab.sum())
        n_exp_alguna = int(mask_exp_alguna.sum())

        print(f"    n_pref={n_pref} | n_exp_reciente={n_exp_rec} | n_exp_habitual={n_exp_hab}")

        grupos = {
            'Total': (df, n_total),
            'Pref': (df[mask_pref], n_pref),
            'Exp_reciente': (df[mask_exp_rec], n_exp_rec),
            'Exp_habitual': (df[mask_exp_hab], n_exp_hab),
            'Exp_alguna': (df[mask_exp_alguna], n_exp_alguna),
        }

        atributos = {}
        pcts_total = {}

        for attr_k in P23_ATTR_PREFIXES:
            col = p23_index[attr_k].get(cadena)
            if col is None:
                atributos[attr_k] = {g: {'pct': None, 'flag': 'COL_NF'} for g in grupos}
                pcts_total[attr_k] = 0.0
                continue

            por_grp = {}
            for grp_name, (df_grp, n_grp) in grupos.items():
                if n_grp < BASE_EXCLUIR:
                    por_grp[grp_name] = {'pct': None, 'n': n_grp, 'flag': 'EXCLUIR'}
                    continue
                # La col tiene el nombre de cadena si hay mencion, NaN si no
                n_ment = int(df_grp[col].notna().sum())
                p = pct(n_ment, n_grp)
                ci_lo, ci_hi = newcombe_ci(n_ment, n_grp)
                por_grp[grp_name] = {
                    'pct': p,
                    'n_ment': n_ment,
                    'n_base': n_grp,
                    'ic95_lo': round(ci_lo * 100, 1),
                    'ic95_hi': round(ci_hi * 100, 1),
                    'flag': flag_n(n_grp),
                }
            atributos[attr_k] = por_grp
            pcts_total[attr_k] = por_grp.get('Total', {}).get('pct') or 0.0

        # Top atributos por asociacion total
        top_atr_sorted = sorted(pcts_total.items(), key=lambda x: x[1], reverse=True)

        # Brechas
        brechas_pref_vs_total = {}
        brechas_exp_vs_total = {}
        for attr_k in P23_ATTR_PREFIXES:
            t_pct = atributos[attr_k].get('Total', {}).get('pct')
            p_pct = atributos[attr_k].get('Pref', {}).get('pct') if n_pref >= BASE_EXCLUIR else None
            e_pct = atributos[attr_k].get('Exp_alguna', {}).get('pct') if n_exp_alguna >= BASE_EXCLUIR else None
            if t_pct is not None and p_pct is not None:
                brechas_pref_vs_total[attr_k] = round(p_pct - t_pct, 1)
            if t_pct is not None and e_pct is not None:
                brechas_exp_vs_total[attr_k] = round(e_pct - t_pct, 1)

        # Atributo sombra: atributo con mayor brecha positiva entre preferentes
        sombra = None
        top3_names = [ATRIBUTO_NOMBRES.get(a, a) for a, _ in top_atr_sorted[:3]]
        if brechas_pref_vs_total:
            positivas = {k: v for k, v in brechas_pref_vs_total.items() if v > 5}
            positivas_excl_top3 = {k: v for k, v in positivas.items()
                                   if ATRIBUTO_NOMBRES.get(k, k) not in top3_names}
            if positivas_excl_top3:
                sombra_k = max(positivas_excl_top3, key=positivas_excl_top3.get)
                sombra = f'{ATRIBUTO_NOMBRES.get(sombra_k, sombra_k)} (+{positivas_excl_top3[sombra_k]:.0f}pp en preferentes)'

        resultados[cadena] = {
            'n_pref': n_pref,
            'n_pref_flag': flag_n(n_pref),
            'n_exp_reciente': n_exp_rec,
            'n_exp_habitual': n_exp_hab,
            'n_exp_alguna': n_exp_alguna,
            'atributos': atributos,
            'top5_por_asociacion_total': [(a, round(v, 1)) for a, v in top_atr_sorted[:5]],
            'brechas_pref_vs_total': brechas_pref_vs_total,
            'brechas_exp_vs_total': brechas_exp_vs_total,
        }

    # ── Tabla comparativa (7 atributos con mayor varianza inter-cadena) ──────
    atrs_var = {}
    for attr_k in P23_ATTR_PREFIXES:
        vals = [resultados[c]['atributos'].get(attr_k, {}).get('Total', {}).get('pct') or 0
                for c in CADENAS_PRINCIPALES]
        atrs_var[attr_k] = float(np.std(vals))

    top_diff = sorted(atrs_var.items(), key=lambda x: x[1], reverse=True)[:7]
    top_diff_keys = [a for a, _ in top_diff]

    tabla_total = {}
    tabla_exp = {}
    for cadena in CADENAS_PRINCIPALES:
        tabla_total[cadena] = {}
        tabla_exp[cadena] = {}
        for attr_k in top_diff_keys:
            v_tot = resultados[cadena]['atributos'].get(attr_k, {}).get('Total', {})
            v_exp = resultados[cadena]['atributos'].get(attr_k, {}).get('Exp_alguna', {})
            tabla_total[cadena][attr_k] = {
                'pct': v_tot.get('pct'), 'flag': v_tot.get('flag', 'N/D')
            }
            tabla_exp[cadena][attr_k] = {
                'pct': v_exp.get('pct'), 'flag': v_exp.get('flag', 'N/D')
            }

    # Z-scores inter-cadena
    zscores = {}
    for attr_k in top_diff_keys:
        vals = [resultados[c]['atributos'].get(attr_k, {}).get('Total', {}).get('pct') or 0
                for c in CADENAS_PRINCIPALES]
        m, s = np.mean(vals), np.std(vals)
        if s < 0.01: s = 0.01
        zscores[attr_k] = {c: round((vals[i] - m) / s, 2) for i, c in enumerate(CADENAS_PRINCIPALES)}

    # Mundos de marca: top3 + cuarto + sombra
    mundos = {}
    for cadena in CADENAS_PRINCIPALES:
        top_a = resultados[cadena]['top5_por_asociacion_total']
        top3 = [ATRIBUTO_NOMBRES.get(a, a) for a, _ in top_a[:3]]
        cuarto = ATRIBUTO_NOMBRES.get(top_a[3][0], '') if len(top_a) > 3 else ''
        brechas = resultados[cadena]['brechas_pref_vs_total']
        sombra = None
        if brechas:
            top3_keys = [a for a, _ in top_a[:3]]
            excl = {k: v for k, v in brechas.items() if v > 5 and k not in top3_keys}
            if excl:
                sk = max(excl, key=excl.get)
                sombra = f'{ATRIBUTO_NOMBRES.get(sk, sk)} (+{excl[sk]:.0f}pp en preferentes)'
        mundos[cadena] = {
            'top3_atributos': top3,
            'cuarto_atributo': cuarto,
            'atributo_sombra': sombra,
            'n_pref': resultados[cadena]['n_pref'],
            'flag': resultados[cadena]['n_pref_flag'],
        }

    # ── Plots ─────────────────────────────────────────────────────────────────
    os.makedirs(OUTPUT_PLOTS_DIR, exist_ok=True)
    _plot_heatmap(tabla_total, top_diff_keys, 'Total', n_total)
    _plot_heatmap(tabla_exp, top_diff_keys, 'Experiencia', None)
    _plot_gama_vs_mercado(resultados)
    _plot_brechas_gama(resultados)

    return {
        'analisis': 'E3',
        'descripcion': 'Mundo de marca por cadena: P21 x P23 x Experiencia (P24 ultima compra + P26 mision habitual)',
        'nota_p24_p25': (
            'P24 = ultima cadena de compra (experiencia reciente). '
            'P25 = razon de la ultima compra (no cadena). '
            'P26 = cadena habitual por tipo de mision (experiencia habitual). '
            'No existe col "alguna vez ha comprado" separada en esta BBDD. '
            'Exp_reciente = P24 == cadena. Exp_habitual = alguna P26 == cadena.'
        ),
        'atributos_diferenciadores': top_diff_keys,
        'varianza_por_atributo': {a: round(v, 2) for a, v in top_diff},
        'resultados_cadenas': resultados,
        'tabla_total': tabla_total,
        'tabla_exp_alguna': tabla_exp,
        'zscores_intercadena': zscores,
        'mundos_de_marca': mundos,
        'caveat': (
            'La mayoria de cadenas tienen n_pref < 30 — todas las cifras por preferentes son REFERENCIALES. '
            'Gama n_pref=32 REFERENCIAL. Paramo n_pref=85 OK. '
            'Experiencia reciente (P24) n variable por cadena. '
            'Tablas son descriptivas — no usar para inferencia sin validacion Bruna.'
        ),
    }


def _plot_heatmap(tabla, attr_keys, label, n):
    """Heatmap cadenas x atributos diferenciadores."""
    attr_nombres = [ATRIBUTO_NOMBRES.get(a, a) for a in attr_keys]
    data = []
    for cadena in CADENAS_PRINCIPALES:
        row = [tabla[cadena].get(ak, {}).get('pct') or 0 for ak in attr_keys]
        data.append(row)

    Z = np.array(data, dtype=float)
    fig, ax = plt.subplots(figsize=(14, 6))
    cmap = LinearSegmentedColormap.from_list('gama', ['#FFFFFF', '#F5C8C8', GAMA_RED])
    im = ax.imshow(Z, aspect='auto', cmap=cmap, vmin=0, vmax=50)
    ax.set_xticks(range(len(attr_nombres)))
    ax.set_xticklabels(attr_nombres, rotation=30, ha='right', fontsize=9)
    ax.set_yticks(range(len(CADENAS_PRINCIPALES)))
    ax.set_yticklabels(CADENAS_PRINCIPALES, fontsize=10)

    for i, cadena in enumerate(CADENAS_PRINCIPALES):
        for j, attr_k in enumerate(attr_keys):
            v = Z[i, j]
            flag = tabla[cadena].get(attr_k, {}).get('flag', 'OK')
            txt = f'{v:.0f}%' + ('*' if flag in ('REFERENCIAL', 'EXCLUIR') else '')
            ax.text(j, i, txt, ha='center', va='center',
                    fontsize=8, color='white' if v > 28 else GAMA_BLACK)

    plt.colorbar(im, ax=ax, shrink=0.7, label='% asociacion P23')
    n_txt = f'(n={n})' if n else ''
    ax.set_title(
        f'Mundo de marca: P23 asociacion cadena x atributo — {label} {n_txt}\n'
        'Atributos con mayor varianza inter-cadena | * = base referencial',
        fontsize=11
    )
    plt.tight_layout()
    safe = label.lower().replace(' ', '_')
    fpath = os.path.join(OUTPUT_PLOTS_DIR, f'cu10_heatmap_mundo_{safe}.png')
    plt.savefig(fpath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot: {fpath}")


def _plot_gama_vs_mercado(resultados):
    """Tornado: Gama vs media mercado en todos los atributos P23."""
    gama_r = resultados['Gama']
    attr_keys = list(P23_ATTR_PREFIXES.keys())
    gama_pcts, market_means, labels = [], [], []

    for ak in attr_keys:
        g_pct = gama_r['atributos'].get(ak, {}).get('Total', {}).get('pct')
        if g_pct is None: continue
        mkt_vals = []
        for c in CADENAS_PRINCIPALES:
            v = resultados[c]['atributos'].get(ak, {}).get('Total', {}).get('pct')
            if v is not None: mkt_vals.append(v)
        gama_pcts.append(g_pct)
        market_means.append(np.mean(mkt_vals) if mkt_vals else 0)
        labels.append(ATRIBUTO_NOMBRES.get(ak, ak))

    pairs = sorted(zip(labels, gama_pcts, market_means), key=lambda x: x[1], reverse=True)
    labels_s, gama_s, mkt_s = zip(*pairs)

    x = np.arange(len(labels_s))
    w = 0.35
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.barh(x + w/2, gama_s, w, label='Gama', color=GAMA_RED, alpha=0.9)
    ax.barh(x - w/2, mkt_s, w, label='Media mercado (8 cadenas)', color=GAMA_GRAY_MID, alpha=0.7)
    ax.set_yticks(x)
    ax.set_yticklabels(labels_s, fontsize=9)
    ax.set_xlabel('% que asocia el atributo con la cadena — Total n=402')
    ax.set_title('DNA de Gama vs media de mercado (P23)', fontsize=12, color=GAMA_RED)
    ax.legend(fontsize=9)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    plt.tight_layout()
    fpath = os.path.join(OUTPUT_PLOTS_DIR, 'cu10_gama_vs_mercado_p23.png')
    plt.savefig(fpath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot: {fpath}")


def _plot_brechas_gama(resultados):
    """Brechas P23 Gama: Pref vs Total vs Experiencia."""
    gama_r = resultados['Gama']
    attr_keys = list(P23_ATTR_PREFIXES.keys())
    rows = []
    for ak in attr_keys:
        t = gama_r['atributos'].get(ak, {}).get('Total', {}).get('pct')
        p = gama_r['atributos'].get(ak, {}).get('Pref', {}).get('pct')
        e = gama_r['atributos'].get(ak, {}).get('Exp_reciente', {}).get('pct')
        if t is not None:
            rows.append((ATRIBUTO_NOMBRES.get(ak, ak), t, p, e))

    rows_s = sorted(rows, key=lambda x: x[1], reverse=True)
    labels = [r[0] for r in rows_s]
    totals = [r[1] for r in rows_s]
    prefs = [r[2] if r[2] is not None else 0 for r in rows_s]
    exps = [r[3] if r[3] is not None else 0 for r in rows_s]

    x = np.arange(len(labels))
    w = 0.25
    fig, ax = plt.subplots(figsize=(13, 6))
    ax.barh(x + w, totals, w, label='Total (n=402)', color=GAMA_GRAY_MID, alpha=0.8)
    ax.barh(x, prefs, w, label='Preferentes Gama (n=32, REFRC)', color=GAMA_RED, alpha=0.9)
    ax.barh(x - w, exps, w, label='Exp. reciente (P24)', color=GAMA_AMBER, alpha=0.9)
    ax.set_yticks(x)
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlabel('% asociacion P23 con Gama')
    ax.set_title('Gama — Asociacion P23: Total vs Preferentes vs Experiencia reciente', fontsize=11)
    ax.legend(fontsize=8)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    plt.tight_layout()
    fpath = os.path.join(OUTPUT_PLOTS_DIR, 'cu10_gama_brechas_segmentos.png')
    plt.savefig(fpath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot: {fpath}")


# ─── MAIN ────────────────────────────────────────────────────────────────────

def main():
    df, p24_col_real, p26_cols_real = load_bbdd()

    e3 = e3_mundo_marca(df, p24_col_real, p26_cols_real)

    # Cargar JSON existente y reemplazar E3
    print(f"\nCargando JSON existente: {INPUT_JSON}")
    with open(INPUT_JSON, encoding='utf-8') as f:
        existing = json.load(f)

    existing['E3_mundo_marca'] = e3
    existing['metadata']['e3_corregido'] = True
    existing['metadata']['e3_fix_fecha'] = '2026-05-18'

    dump_json(existing, OUTPUT_JSON)
    print(f"JSON actualizado: {OUTPUT_JSON}")

    # Resumen E3
    print("\n=== RESUMEN E3 ===")
    for cadena, mundo in e3['mundos_de_marca'].items():
        top3 = ', '.join(mundo['top3_atributos'])
        print(f"  {cadena:<25} n_pref={mundo['n_pref']} {mundo['flag']} | {top3} | sombra: {mundo['atributo_sombra']}")

    print("\n=== Tabla P23 Total (%) ===")
    print(f"  {'Cadena':<25}", end='')
    for ak in e3['atributos_diferenciadores'][:5]:
        print(f"  {ATRIBUTO_NOMBRES.get(ak,ak)[:12]:<13}", end='')
    print()
    for cadena in CADENAS_PRINCIPALES:
        print(f"  {cadena:<25}", end='')
        for ak in e3['atributos_diferenciadores'][:5]:
            v = e3['resultados_cadenas'][cadena]['atributos'].get(ak, {}).get('Total', {}).get('pct')
            print(f"  {str(v)+'%':<13}", end='')
        print()

    return e3


if __name__ == '__main__':
    main()
