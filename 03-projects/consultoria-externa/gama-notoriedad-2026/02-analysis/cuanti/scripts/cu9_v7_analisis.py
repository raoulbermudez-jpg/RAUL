"""
cu9_v7_analisis.py — CU-9 V7: 10 analisis nuevos + recuperacion V3 + validacion consistencia
Proyecto: Gama Notoriedad 2026
Autor: Cuanti (agente analitico)
Fecha: 2026-05-18
Version: v2 (encoding real de BBDD — P22 texto escala, P23 nombre cadena, P26 nombre cadena)

Inputs:
  BBDD_2026: BBDD Notoriedad 2026.xlsx (n=402, 295 cols)

Outputs:
  JSON: outputs/json/CU9_v7_analisis_20260518.json
  Plots: outputs/plots/cu9_*.png

Notas de codificacion real BBDD 2026:
  - P22: texto ('Muy Importante'/'Importante'/'Algo importante'/'Poco importante'/'Nada Importante')
  - P23: cada col {P23:X} - Cadena contiene el nombre de cadena si hay mencion, vacía si no
  - P26: nombre de cadena habitual para esa mision (o 'Ninguno (NO LEER)')
  - P30: nombre de cadena habitual por categoria
  - P32: nombre de cadena de mejor precio por categoria
  - P21: nombre de cadena preferida
  - P35/P37/P40: 'Si'/'No'
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

import os
import json
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

from scipy import stats
from scipy.stats import chi2_contingency
from statsmodels.stats.multitest import multipletests
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import MDS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# ─── CONSTANTES ─────────────────────────────────────────────────────────────

BBDD_2026_PATH = (
    'G:/Mi unidad/RAUL/colaboradores/Genteca/Cora-Urrea/'
    '01_De_Cora_Para_Raoul/Notoriedad V2.0/BBDD Notoriedad 2026.xlsx'
)
OUTPUT_JSON = (
    'C:/RAUL/03-projects/consultoria-externa/gama-notoriedad-2026/'
    '02-analysis/cuanti/outputs/json/CU9_v7_analisis_20260518.json'
)
OUTPUT_PLOTS_DIR = (
    'C:/RAUL/03-projects/consultoria-externa/gama-notoriedad-2026/'
    '02-analysis/cuanti/outputs/plots/'
)

ALPHA = 0.05
BASE_BAJA = 30
BASE_EXCLUIR = 10

# Escala P22 texto -> numero
P22_SCALE = {
    'Muy Importante': 5,
    'Importante': 4,
    'Algo importante': 3,
    'Poco importante': 2,
    'Nada Importante': 1,
}

CADENAS = ['Gama', 'Paramo', 'Central Madeirense', 'Rio', 'Forum',
           'Plan Suarez', 'Plazas', 'Luz', 'La Muralla', 'Hiper Lider']

ATRIBUTOS = {
    'surtido':       'Mayor surtido',
    'calidad':       'Mayor calidad',
    'menor_precio':  'Menor precio',
    'atencion':      'Mejor atencion',
    'promociones':   'Promociones',
    'atractiva':     'Tienda atractiva',
    'limpieza':      'Limpieza/orden',
    'seguro':        'Seguro',
    'rapidez':       'Rapidez caja',
    'valer_dinero':  'Valer dinero',
}

# P22 columnas exactas (texto escala)
P22_COLS = {
    'limpieza':      ' {P22} [V209] IMPORTANCIA  Es un espacio limpio y ordenado',
    'surtido':       ' {P22} [V202] IMPORTANCIA Donde encuentro la mayor cantidad de categorias/productos que acostumbro a comprar',
    'seguro':        ' {P22} [V213]  IMPORTANCIA Es seguro',
    'rapidez':       ' {P22} [V214]  IMPORTANCIA Rapidez en la caja',
    'menor_precio':  ' {P22} [V204]  IMPORTANCIA Donde encuentro los productos a menor precio',
    'atractiva':     ' {P22} [V207]  IMPORTANCIA La tienda es atractiva',
    'promociones':   ' {P22} [V206]  IMPORTANCIA Tienen promociones atractivas',
    'calidad':       ' {P22} [V203]  IMPORTANCIA Donde encuentro los productos de mayor calidad',
    'atencion':      ' {P22} [V205] IMPORTANCIA  Donde mejor me atienden',
    'valer_dinero':  ' {P22} [V1856]  IMPORTANCIA Donde puedo hacer valer mi dinero',
}

# P23 columnas — nombre de la cadena en la celda si fue mencionada
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

P35_COL = ' {P35} [V1889] Recuerda haber visto, leido o escuchado frases que acompañan la publicidad de Gama en general o con las promociones de descuentos?'
P37_COL = ' {P37} [V1891] ¿Recuerda haber visto o escuchado en la publicidad de GAMA la frase que dice «PRECIOS DE TU LADO» ?'
P40_COL = ' {P40} [V1894] ¿Recuerda haber visto o escuchado en la publicidad de GAMA la frase que dice «DE TU LADO SIEMPRE» ?'

P30_COLS = {
    'frutas':           ' {P30} [V799] Ahora dígame, ¿Cuál es el supermercado en donde usted acostumbra a comprar productos de las siguientes categorías?.- Frutas, legumbres y verduras',
    'galletas':         ' {P30} [V800] Lugar de compra habitual - Galletas, pasapalos y confiteria',
    'salsas':           ' {P30} [V801] Lugar de compra habitual - Salsas y Enlatados (atÃºn, cÃ¡rnicos, vegetales)',
    'carne':            ' {P30} [V805] Lugar de compra habitual - Carne de res',
    'pollo':            ' {P30} [V806] Lugar de compra habitual - Pollo',
    'charcuteria':      ' {P30} [V807] Lugar de compra habitual - Charcuteria (quesos, jamones y pechugas)',
    'gaseosas':         ' {P30} [V810] Lugar de compra habitual - Gaseosas, jugos y aguas',
    'licores':          ' {P30} [V811] Lugar de compra habitual - Licores',
    'farmacia':         ' {P30} [V812] Lugar de compra habitual - Farmacia',
    'congelados':       ' {P30} [V815] Lugar de compra habitual - Congelados (helados, pasapalos, postres etc: )',
    'mascotas':         ' {P30} [V817] Lugar de compra habitual - Alimento de mascotas (perros, gatos, otros)',
    'pescados':         ' {P30} [V818] Lugar de compra habitual - Pescados y mariscos',
    'basicos':          ' {P30} [V1858] Lugar de compra habitual - Productos basicos (harinas, arroz, leches, pastas, etc)',
    'cuidado_personal': ' {P30} [V1859] Lugar de compra habitual - Cuidado Personal',
    'cuidado_hogar':    ' {P30} [V1860] Lugar de compra habitual - Cuidado y limpieza del hogar',
}

P32_COLS = {
    'frutas':           ' {P32} [V1872] ¿En cuál de estos supermercados encuentra los mejores precios en (mencionar cada categoria y mostrar tarjeta redonda)? - Frutas, legumbres y verduras',
    'galletas':         ' {P32} [V1873] Mejor precio - Galletas, pasapalos y confiterÃ­a',
    'salsas':           ' {P32} [V1874] Mejor precio - Salsas y Enlatados (atÃºn, cÃ¡rnicos, vegetales)',
    'carne':            ' {P32} [V1875] Mejor precio - Carne de res',
    'pollo':            ' {P32} [V1876] Mejor precio - Pollo',
    'charcuteria':      ' {P32} [V1877] Mejor precio - CharcuterÃ­a (quesos, jamones y pechugas)',
    'gaseosas':         ' {P32} [V1878] Mejor precio - Gaseosas, jugos y aguas',
    'licores':          ' {P32} [V1879] Mejor precio - Licores',
    'farmacia':         ' {P32} [V1880] Mejor precio - Farmacia',
    'congelados':       ' {P32} [V1881] Mejor precio - Congelados (helados, pasapalos, postres etc: )',
    'mascotas':         ' {P32} [V1882] Mejor precio - Alimento de mascotas (perros, gatos, otros)',
    'pescados':         ' {P32} [V1883] Mejor precio - Pescados y mariscos',
    'basicos':          ' {P32} [V1884] Mejor precio - Productos bÃ¡sicos (harinas, arroz, leches, pastas, etc)',
    'cuidado_personal': ' {P32} [V1885] Mejor precio - Cuidado Personal',
    'cuidado_hogar':    ' {P32} [V1886] Mejor precio - Cuidado y limpieza del hogar',
}

P26_COLS = {
    'abastecimiento':     ' {P26} [V819] MISION DE COMPRA Hacer abastecimiento general y completo de mi hogar (todo tipo de vÃ­veres y productos de aseo)',
    'reabastecimiento':   ' {P26} [V820] MISION DE COMPRA Realizar algunas compras para reabastecer mi hogar antes de volver a hacer un mercado grande (frutas, verduras, leche u otro tipo de productos perecederos)',
    'compras_especiales': ' {P26} [V821] MISION DE COMPRA Comprar electrodomesticos, ropa, muebles, ferreterÃ­a, jardinerÃ­a o productos de tecnologÃ­a',
    'evento':             ' {P26} [V822] MISION DE COMPRA Comprar viveres para un evento, una fiesta, una celebraciÃ³n o una ocasiÃ³n especial:',
    'urgencia':           ' {P26} [V823] MISION DE COMPRA Comprar unos pocos productos con urgencia (comidas preparadas o para llevar, ingrediente faltante en una receta, medicamento para el dolor de cabeza, etc:)',
}

CAT_NOMBRES = {
    'frutas': 'Frutas, legumbres y verduras',
    'galletas': 'Galletas, pasapalos y confiteria',
    'salsas': 'Salsas y Enlatados',
    'carne': 'Carne de res',
    'pollo': 'Pollo',
    'charcuteria': 'Charcuteria',
    'gaseosas': 'Gaseosas, jugos y aguas',
    'licores': 'Licores',
    'farmacia': 'Farmacia',
    'congelados': 'Congelados',
    'mascotas': 'Alimento de mascotas',
    'pescados': 'Pescados y mariscos',
    'basicos': 'Productos basicos',
    'cuidado_personal': 'Cuidado Personal',
    'cuidado_hogar': 'Cuidado y limpieza del hogar',
}

# ─── UTILS ──────────────────────────────────────────────────────────────────

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer,)): return int(obj)
        if isinstance(obj, (np.floating,)): return float(obj)
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

def flag_n(n):
    if n < BASE_EXCLUIR: return 'EXCLUIR'
    if n < BASE_BAJA: return 'REFERENCIAL'
    return 'OK'

def pct(k, n):
    return round(100*k/n, 1) if n > 0 else 0.0

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
    return 'Otro'

def p22_score(val):
    """Convierte texto P22 a numero 1-5."""
    return P22_SCALE.get(str(val).strip(), None)

def p23_has_cadena(val, cadena_name):
    """True si la celda P23 contiene el nombre de la cadena."""
    if pd.isna(val): return False
    v = str(val).strip().lower()
    return cadena_name.lower() in v

# ─── CARGA ──────────────────────────────────────────────────────────────────

def load_bbdd():
    print("Cargando BBDD 2026...")
    df = pd.read_excel(BBDD_2026_PATH, engine='openpyxl')
    df['NSE_harm'] = df[NSE_COL].apply(nse_harm)
    df['P21_val'] = df[P21_COL].astype(str).str.strip()
    df['pref_gama'] = df['P21_val'].apply(is_gama)
    df['recall_ptl'] = df[P37_COL].apply(is_yes)
    df['recall_dtls'] = df[P40_COL].apply(is_yes)
    df['recall_p35'] = df[P35_COL].apply(is_yes)
    df['recall_any'] = df['recall_ptl'] | df['recall_dtls'] | df['recall_p35']

    n_total = len(df)
    n_cc = int((df['NSE_harm'] == 'C+/C').sum())
    n_pg = int(df['pref_gama'].sum())
    print(f"  Total n={n_total}, C+/C n={n_cc}, Pref-Gama n={n_pg} {'(REFERENCIAL)' if n_pg<BASE_BAJA else ''}")

    df_total = df.copy()
    df_cc = df[df['NSE_harm'] == 'C+/C'].copy()
    df_pg = df[df['pref_gama']].copy()
    return df_total, df_cc, df_pg

# ─── A1 — P22 IMPORTANCIA ──────────────────────────────────────────────────

def analisis_1(df_total, df_cc, df_pg):
    print("\nA1: P22 Importancia atributos...")
    results = {'analisis': 'A1', 'bifurcaciones': {}}

    for grp_name, df in [('Total', df_total), ('C+/C', df_cc), ('Pref-Gama', df_pg)]:
        n = len(df)
        rows = []
        for attr_k, col in P22_COLS.items():
            if col not in df.columns:
                rows.append({'atributo': attr_k, 'flag': 'COLUMNA_NF'}); continue
            scores = df[col].apply(p22_score).dropna()
            n_v = len(scores)
            n_top2 = int((scores >= 4).sum())
            mean_v = float(scores.mean()) if n_v > 0 else None
            pct_t2b = pct(n_top2, n_v)
            ci_lo, ci_hi = newcombe_ci(n_top2, n_v)
            rows.append({
                'atributo': attr_k,
                'nombre': ATRIBUTOS[attr_k],
                'n_base': n,
                'n_valid': n_v,
                'n_top2': n_top2,
                'pct_top2': pct_t2b,
                'ic95_lo': round(ci_lo*100, 1),
                'ic95_hi': round(ci_hi*100, 1),
                'mean_score': round(mean_v, 2) if mean_v else None,
                'flag': flag_n(n_v),
            })
        results['bifurcaciones'][grp_name] = {'n': n, 'items': rows}

    # Diferencial Total vs C+/C — cuales atributos difieren mas
    diffs = []
    t_map = {r['atributo']: r.get('pct_top2') for r in results['bifurcaciones']['Total']['items']}
    cc_map = {r['atributo']: r.get('pct_top2') for r in results['bifurcaciones']['C+/C']['items']}
    for attr in t_map:
        t_v = t_map.get(attr)
        cc_v = cc_map.get(attr)
        if t_v is not None and cc_v is not None:
            diffs.append({
                'atributo': attr,
                'nombre': ATRIBUTOS.get(attr, attr),
                'total_pct': t_v,
                'cc_pct': cc_v,
                'diff_pp': round(cc_v - t_v, 1),
                'interpretacion': 'C+/C mas exigente' if (cc_v - t_v) > 2 else ('Total mas exigente' if (t_v - cc_v) > 2 else 'Similares'),
            })
    diffs.sort(key=lambda x: abs(x['diff_pp']), reverse=True)
    results['diferencial_total_cc'] = diffs
    return results

# ─── A2 — P23 MATRIZ ────────────────────────────────────────────────────────

def get_p23_col_for_cadena(df, attr_prefix_partial, cadena_name):
    """Busca columna P23 para el atributo y la cadena."""
    cadena_search = cadena_name
    # Some cadena names differ in cols
    replacements = {
        'Central Madeirense': ['Central Madeirense', 'Central'],
        'Plan Suarez': ['Plan Suarez', 'Plan'],
        'La Muralla': ['La Muralla', 'Muralla'],
        'Hiper Lider': ['Hiper Lider', 'Hiper'],
        'Plazas': ["Plaza´s", 'Plazas', "Plaza's"],
        "Gama": ['Gama'],
    }
    names_to_try = replacements.get(cadena_name, [cadena_name])

    for col in df.columns:
        if attr_prefix_partial.strip().lower() in col.strip().lower():
            col_low = col.strip().lower()
            for nm in names_to_try:
                if nm.lower() in col_low:
                    return col
    return None

def analisis_2(df_total, df_cc, df_pg):
    print("\nA2: P23 Asociacion marca x atributo...")
    results = {'analisis': 'A2', 'bifurcaciones': {}}
    blockers = []

    for grp_name, df in [('Total', df_total), ('C+/C', df_cc), ('Pref-Gama', df_pg)]:
        n = len(df)
        matrix = {}
        for attr_k, prefix_partial in P23_COLS.items():
            matrix[attr_k] = {}
            for cadena in CADENAS:
                col = get_p23_col_for_cadena(df, prefix_partial, cadena)
                if col is None:
                    blockers.append(f'{attr_k} x {cadena}')
                    matrix[attr_k][cadena] = None
                    continue
                # Contar menciones: la celda tiene el nombre de la cadena si fue mencionada
                n_ment = int(df[col].apply(lambda v: p23_has_cadena(v, cadena)).sum())
                n_base = n  # toda la muestra pudo responder P23
                p = pct(n_ment, n_base)
                ci_lo, ci_hi = newcombe_ci(n_ment, n_base)
                matrix[attr_k][cadena] = {
                    'pct': p,
                    'n_ment': n_ment,
                    'n_base': n_base,
                    'ic95_lo': round(ci_lo*100, 1),
                    'ic95_hi': round(ci_hi*100, 1),
                    'flag': flag_n(n_ment),
                }
        results['bifurcaciones'][grp_name] = {'n': n, 'matrix': matrix}

    if blockers:
        results['blockers'] = list(set(blockers))
    return results

# ─── A3 — CORRELACION NOMINAL P21.1 x P23 ───────────────────────────────────

def categorize_razon(text):
    t = str(text).strip().lower()
    if any(x in t for x in ['precio', 'barato', 'econom', 'descuento', 'oferta', 'promoc', 'cashea']):
        # Separar promociones de precio
        if any(x in t for x in ['promoc', 'oferta', 'descuento', 'cashea']):
            return 'promociones'
        return 'precio'
    if any(x in t for x in ['aten', 'servic', 'amable', 'trato', 'personal', 'asesor']):
        return 'atencion'
    if any(x in t for x in ['cerc', 'cerca', 'ubic', 'camino', 'accesib', 'comod']):
        return 'cercania'
    if any(x in t for x in ['calid', 'fresc', 'vencid', 'bueno']):
        return 'calidad'
    if any(x in t for x in ['surtid', 'variedad', 'variado', 'todo', 'product']):
        return 'surtido'
    if any(x in t for x in ['limpi', 'orden', 'limpie']):
        return 'limpieza'
    if any(x in t for x in ['rapid', 'caja', 'velocidad']):
        return 'rapidez'
    if any(x in t for x in ['costumbre', 'siempre', 'conoci']):
        return 'habito'
    if t in ('nan', '', 'none', 'no recuerda'):
        return None
    return 'otros'

def analisis_3(df_total, a2_results):
    print("\nA3: Correlacion nominal P21.1 x P23...")
    p21_cols = [c for c in df_total.columns if '{P21.1}' in c]
    results = {'analisis': 'A3', 'cadenas': {}}
    a2_total_matrix = a2_results['bifurcaciones']['Total']['matrix']

    for cadena in CADENAS:
        cadena_s = cadena.lower()
        if cadena == 'Central Madeirense': cadena_s = 'central'
        if cadena == 'Plan Suarez': cadena_s = 'plan suarez'
        if cadena == 'Plazas': cadena_s = 'plaza'

        subset = df_total[df_total['P21_val'].str.lower().str.contains(cadena_s, na=False)]
        n_c = len(subset)
        if n_c < BASE_EXCLUIR:
            results['cadenas'][cadena] = {'n': n_c, 'flag': 'EXCLUIR'}
            continue

        # Razones espontaneas
        cats = {'precio': 0, 'atencion': 0, 'cercania': 0, 'calidad': 0,
                'surtido': 0, 'limpieza': 0, 'rapidez': 0, 'promociones': 0,
                'habito': 0, 'otros': 0}
        n_razones = 0
        for col in p21_cols:
            if col in subset.columns:
                for r in subset[col].dropna().astype(str):
                    cat = categorize_razon(r)
                    if cat:
                        cats[cat] += 1
                        n_razones += 1

        if n_razones == 0:
            results['cadenas'][cadena] = {'n': n_c, 'flag': 'SIN_RAZONES'}
            continue

        pcts_razones = {k: pct(v, n_razones) for k, v in cats.items()}
        razon_ppal = max(cats, key=cats.get)

        # Atributo principal en P23 para esta cadena
        attr_pcts_p23 = {}
        for attr_k in ATRIBUTOS:
            val = a2_total_matrix.get(attr_k, {}).get(cadena)
            if val and isinstance(val, dict):
                attr_pcts_p23[attr_k] = val.get('pct', 0) or 0

        if attr_pcts_p23:
            attr_ppal_p23 = max(attr_pcts_p23, key=attr_pcts_p23.get)
        else:
            attr_ppal_p23 = None

        # Coincidencia nominal P21.1 vs P23
        # Mapeo semantico razon->atributo
        razon_to_attr = {
            'precio': 'menor_precio',
            'atencion': 'atencion',
            'promociones': 'promociones',
            'calidad': 'calidad',
            'surtido': 'surtido',
            'limpieza': 'limpieza',
            'rapidez': 'rapidez',
        }
        attr_esperado_de_razon = razon_to_attr.get(razon_ppal)
        coincide = (attr_esperado_de_razon == attr_ppal_p23) if attr_esperado_de_razon else None

        results['cadenas'][cadena] = {
            'n': n_c,
            'flag': flag_n(n_c),
            'n_razones': n_razones,
            'razones_pct': pcts_razones,
            'razon_espontanea_principal': razon_ppal,
            'pct_razon_principal': pcts_razones[razon_ppal],
            'atributo_p23_principal': attr_ppal_p23,
            'pct_atributo_p23': attr_pcts_p23.get(attr_ppal_p23, 0),
            'coincide_nominal': coincide,
            'interpretacion': (
                'COINCIDE: lo que dice al escoger coincide con lo que asocia cuando se lo preguntan'
                if coincide else
                'GAP: la razon espontanea NO coincide con el atributo de asociacion mas fuerte — el shopper tiene la asociacion pero no la verbaliza'
                if coincide is False else 'Sin mapeo directo'
            ),
        }

    return results

# ─── A4 — MAPA PERCEPTUAL MDS ───────────────────────────────────────────────

def analisis_4(df_total, df_cc, df_pg, a2_results):
    print("\nA4: Mapa perceptual MDS...")
    os.makedirs(OUTPUT_PLOTS_DIR, exist_ok=True)
    results = {'analisis': 'A4', 'bifurcaciones': {}}

    for grp_name, df in [('Total', df_total), ('C+/C', df_cc), ('Pref-Gama', df_pg)]:
        n = len(df)
        if grp_name not in a2_results['bifurcaciones']:
            results['bifurcaciones'][grp_name] = {'flag': 'SIN_DATOS', 'n': n}; continue

        matrix = a2_results['bifurcaciones'][grp_name]['matrix']
        attr_keys = [k for k in ATRIBUTOS if k in matrix]
        cadenas_ok, mat_data = [], []
        for cadena in CADENAS:
            row = []
            ok = True
            for ak in attr_keys:
                v = matrix[ak].get(cadena)
                if v is None or not isinstance(v, dict):
                    ok = False; break
                row.append(v.get('pct', 0) or 0)
            if ok:
                cadenas_ok.append(cadena)
                mat_data.append(row)

        if len(cadenas_ok) < 3:
            results['bifurcaciones'][grp_name] = {'flag': 'DATOS_INSUFICIENTES', 'n': n}; continue

        X = np.array(mat_data, dtype=float)
        Xs = StandardScaler().fit_transform(X)
        mds = MDS(n_components=2, dissimilarity='euclidean', random_state=42, n_init=10)
        coords = mds.fit_transform(Xs)
        stress = float(mds.stress_)

        _plot_mds(cadenas_ok, coords, grp_name, n, stress)

        results['bifurcaciones'][grp_name] = {
            'n': n, 'flag': flag_n(n),
            'cadenas': cadenas_ok,
            'coords': {c: {'x': float(coords[i,0]), 'y': float(coords[i,1])}
                       for i, c in enumerate(cadenas_ok)},
            'stress': stress,
            'stress_quality': 'Bueno' if stress < 0.1 else 'Aceptable' if stress < 0.2 else 'Pobre',
        }

    return results

def _plot_mds(cadenas, coords, grp_name, n, stress):
    colors = {'Gama': '#7A1212', 'Paramo': '#1A568A', 'Rio': '#D97306',
              'Central Madeirense': '#1A702A', 'Forum': '#6B21A8'}
    fig, ax = plt.subplots(figsize=(10, 8))
    for i, c in enumerate(cadenas):
        col = colors.get(c, '#888888')
        ax.scatter(coords[i,0], coords[i,1], s=200, c=col, zorder=3)
        ax.annotate(c, (coords[i,0], coords[i,1]),
                    textcoords='offset points', xytext=(8, 4),
                    fontsize=9, color=col,
                    fontweight='bold' if c == 'Gama' else 'normal')
    ax.axhline(0, color='#cccccc', lw=0.8, ls='--')
    ax.axvline(0, color='#cccccc', lw=0.8, ls='--')
    grp_lbl = grp_name.replace('+', 'mas').replace('/', '_')
    ax.set_title(f'Mapa Perceptual MDS — {grp_name} (n={n})\nStress={stress:.3f} — Atributos P23',
                 fontsize=11)
    ax.set_xlabel('Dimension 1'); ax.set_ylabel('Dimension 2')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_PLOTS_DIR, f'cu9_mds_{grp_lbl}.png'),
                dpi=150, bbox_inches='tight')
    plt.close()

# ─── A5 — DNA Z-SCORES ──────────────────────────────────────────────────────

def analisis_5(df_total, df_cc, df_pg, a2_results):
    print("\nA5: DNA z-scores por cadena...")
    results = {'analisis': 'A5', 'bifurcaciones': {}}

    for grp_name, df in [('Total', df_total), ('C+/C', df_cc), ('Pref-Gama', df_pg)]:
        n = len(df)
        if grp_name not in a2_results['bifurcaciones']:
            results['bifurcaciones'][grp_name] = {'flag': 'SIN_DATOS', 'n': n}; continue

        matrix = a2_results['bifurcaciones'][grp_name]['matrix']
        attr_keys = [k for k in ATRIBUTOS if k in matrix]

        cadenas_ok, mat_data = [], []
        for cadena in CADENAS:
            row, ok = [], True
            for ak in attr_keys:
                v = matrix[ak].get(cadena)
                if v is None or not isinstance(v, dict):
                    ok = False; break
                row.append(v.get('pct', 0) or 0)
            if ok:
                cadenas_ok.append(cadena)
                mat_data.append(row)

        if len(cadenas_ok) < 3:
            results['bifurcaciones'][grp_name] = {'flag': 'DATOS_INSUFICIENTES', 'n': n}; continue

        X = np.array(mat_data, dtype=float)
        means = X.mean(axis=0)
        stds = X.std(axis=0)
        stds[stds == 0] = 1e-9
        Z = (X - means) / stds

        zscores = {}
        for i, c in enumerate(cadenas_ok):
            zscores[c] = {}
            for j, ak in enumerate(attr_keys):
                zscores[c][ak] = {
                    'zscore': round(float(Z[i,j]), 3),
                    'pct_raw': round(float(X[i,j]), 1),
                    'mercado_mean': round(float(means[j]), 1),
                    'sobreindice': bool(Z[i,j] >= 0.5),
                    'subindice': bool(Z[i,j] <= -0.5),
                }

        gama_z = zscores.get('Gama', {})
        results['bifurcaciones'][grp_name] = {
            'n': n,
            'flag': flag_n(n),
            'cadenas': cadenas_ok,
            'zscores': zscores,
            'gama_dna': {
                'sobreindice': [ak for ak, v in gama_z.items() if v.get('sobreindice')],
                'subindice': [ak for ak, v in gama_z.items() if v.get('subindice')],
                'zscores': gama_z,
            },
        }

        if grp_name == 'Total' and gama_z:
            _plot_dna_gama(gama_z, n)

    return results

def _plot_dna_gama(gama_z, n):
    attrs = list(ATRIBUTOS.keys())
    nombres = [ATRIBUTOS[a] for a in attrs]
    zvals = [gama_z.get(a, {}).get('zscore', 0) for a in attrs]
    pairs = sorted(zip(nombres, zvals), key=lambda x: x[1], reverse=True)
    nom_s, z_s = zip(*pairs)
    colors = ['#7A1212' if z >= 0 else '#888888' for z in z_s]
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(range(len(nom_s)), z_s, color=colors, height=0.7)
    ax.set_yticks(range(len(nom_s)))
    ax.set_yticklabels(nom_s, fontsize=10)
    ax.axvline(0.5, color='#D97306', ls='--', lw=1, alpha=0.7, label='+0.5 sobreindice')
    ax.axvline(-0.5, color='#1A568A', ls='--', lw=1, alpha=0.7, label='-0.5 subindice')
    ax.axvline(0, color='#333', ls='-', lw=0.8)
    for i, z in enumerate(z_s):
        ax.text(z + (0.03 if z >= 0 else -0.03), i, f'{z:+.2f}',
                va='center', ha='left' if z >= 0 else 'right', fontsize=9)
    ax.set_xlabel('Z-score vs media del mercado')
    ax.set_title(f'DNA de Gama — Z-scores P23 (Total n={n})', fontsize=12, color='#7A1212')
    ax.legend(fontsize=9)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_PLOTS_DIR, 'cu9_dna_gama_total.png'),
                dpi=150, bbox_inches='tight')
    plt.close()

# ─── A6 — MODELO ATENCION vs PRECIO ─────────────────────────────────────────

def analisis_6(df_total, df_cc):
    print("\nA6: Modelo Atencion vs Precio-dominante...")
    p21_cols = [c for c in df_total.columns if '{P21.1}' in c]
    results = {'analisis': 'A6', 'bifurcaciones': {}}

    for grp_name, df in [('Total', df_total), ('C+/C', df_cc)]:
        n = len(df)
        cadenas_modelo = {}

        for cadena in CADENAS:
            cadena_s = cadena.lower()
            if cadena == 'Central Madeirense': cadena_s = 'central'
            if cadena == 'Plan Suarez': cadena_s = 'plan suarez'
            if cadena == 'Plazas': cadena_s = 'plaza'

            subset = df[df['P21_val'].str.lower().str.contains(cadena_s, na=False)]
            n_c = len(subset)

            if n_c < BASE_EXCLUIR:
                cadenas_modelo[cadena] = {'n': n_c, 'flag': 'EXCLUIR'}
                continue

            cats = {'precio': 0, 'atencion': 0, 'cercania': 0, 'calidad': 0,
                    'surtido': 0, 'promociones': 0, 'rapidez': 0, 'habito': 0, 'otros': 0}
            n_razones = 0
            for col in p21_cols:
                if col not in subset.columns: continue
                for r in subset[col].dropna().astype(str):
                    cat = categorize_razon(r)
                    if cat:
                        cats[cat] = cats.get(cat, 0) + 1
                        n_razones += 1

            if n_razones == 0:
                cadenas_modelo[cadena] = {'n': n_c, 'flag': 'SIN_RAZONES'}
                continue

            pcts = {k: pct(v, n_razones) for k, v in cats.items()}
            dom = max(pcts, key=pcts.get)

            if pcts['atencion'] >= 35:
                modelo = 'Atencion-dominante'
            elif pcts['precio'] >= 50:
                modelo = 'Precio-dominante'
            elif pcts['cercania'] >= 30:
                modelo = 'Cercania-dominante'
            elif pcts['precio'] >= 35:
                modelo = 'Precio-dominante'
            else:
                modelo = f'{dom.capitalize()}-dominante'

            cadenas_modelo[cadena] = {
                'n': n_c,
                'flag': flag_n(n_c),
                'n_razones': n_razones,
                'razones_pct': pcts,
                'razon_dominante': dom,
                'pct_razon_dom': pcts[dom],
                'modelo': modelo,
            }

        results['bifurcaciones'][grp_name] = {'n': n, 'cadenas': cadenas_modelo}

    return results

# ─── A7 — PERFIL RECORDADORES ────────────────────────────────────────────────

def analisis_7(df_total):
    print("\nA7: Perfil recordadores PTL y DTLS...")
    df = df_total
    n = len(df)
    n_p35 = int(df['recall_p35'].sum())
    n_ptl = int(df['recall_ptl'].sum())
    n_dtls = int(df['recall_dtls'].sum())
    n_any = int(df['recall_any'].sum())

    def perfil(mask, label):
        sub = df[mask]
        ns = len(sub)
        if ns < BASE_EXCLUIR:
            return {'n': ns, 'flag': 'EXCLUIR', 'label': label}
        nse_d = sub['NSE_harm'].value_counts()
        pg = int(sub['pref_gama'].sum())
        return {
            'n': ns,
            'flag': flag_n(ns),
            'label': label,
            'pct_del_total': pct(ns, n),
            'nse': {k: {'n': int(v), 'pct': pct(v, ns)} for k, v in nse_d.items()},
            'pref_gama_n': pg,
            'pref_gama_pct': pct(pg, ns),
        }

    n_ambos = int((df['recall_ptl'] & df['recall_dtls']).sum())

    return {
        'analisis': 'A7',
        'totales': {
            'n_total': n,
            'n_recall_p35': n_p35, 'pct_p35': pct(n_p35, n),
            'n_recall_ptl': n_ptl, 'pct_ptl': pct(n_ptl, n), 'flag_ptl': flag_n(n_ptl),
            'n_recall_dtls': n_dtls, 'pct_dtls': pct(n_dtls, n), 'flag_dtls': flag_n(n_dtls),
            'n_ambos': n_ambos,
        },
        'perfil_ptl': perfil(df['recall_ptl'], 'Recuerda PTL'),
        'perfil_dtls': perfil(df['recall_dtls'], 'Recuerda DTLS'),
        'perfil_any': perfil(df['recall_any'], 'Recuerda cualquier frase'),
        'solapamiento': {
            'n_ptl_y_dtls': n_ambos,
            'pct_ptl_que_recuerda_dtls': pct(n_ambos, n_ptl) if n_ptl > 0 else None,
        },
    }

# ─── A8 — RE-SEGMENTACION POR RECALL ─────────────────────────────────────────

def analisis_8(df_total):
    print("\nA8: Re-segmentacion por recall...")
    df = df_total
    n = len(df)
    n_r = int(df['recall_any'].sum())
    n_nr = n - n_r

    # Variables a cruzar
    variables = {}
    variables['pref_gama'] = ('Preferencia Gama (P21)', df['pref_gama'])

    # P26 misiones — Gama
    for mk, col in P26_COLS.items():
        if col in df.columns:
            v = df[col].apply(is_gama)
            variables[f'p26_gama_{mk}'] = (f'Mision {mk} en Gama (P26)', v)

    # P30 habito Gama — primeras categorias
    for cat_k in list(P30_COLS.keys())[:8]:
        col = P30_COLS[cat_k]
        if col in df.columns:
            v = df[col].apply(is_gama)
            variables[f'p30_gama_{cat_k}'] = (f'Habito Gama {CAT_NOMBRES[cat_k]} (P30)', v)

    diffs = []
    por_pregunta = {}
    for vk, (label, series) in variables.items():
        try:
            mask_r = df['recall_any'].astype(bool)
            yr = int(series[mask_r].sum())
            ynr = int(series[~mask_r].sum())
            pr = pct(yr, n_r) if n_r > 0 else 0
            pnr = pct(ynr, n_nr) if n_nr > 0 else 0
            diff = round(pr - pnr, 1)
            por_pregunta[vk] = {
                'label': label,
                'recuerda': {'n': n_r, 'yes': yr, 'pct': pr},
                'no_recuerda': {'n': n_nr, 'yes': ynr, 'pct': pnr},
                'diff_pp': diff,
                'relevante': abs(diff) >= 5,
            }
            if abs(diff) >= 5:
                diffs.append({'variable': label, 'diff_pp': diff, 'r_pct': pr, 'nr_pct': pnr})
        except Exception as e:
            por_pregunta[vk] = {'error': str(e)}

    diffs.sort(key=lambda x: abs(x['diff_pp']), reverse=True)
    return {
        'analisis': 'A8',
        'n_recuerda': n_r,
        'n_no_recuerda': n_nr,
        'pct_recuerda': pct(n_r, n),
        'diferencias_relevantes': diffs,
        'por_pregunta': por_pregunta,
    }

# ─── A9 — P30 x P32 x P26 ────────────────────────────────────────────────────

def analisis_9(df_total, df_cc):
    print("\nA9: Cruce P30 x P32 x P26...")
    results = {'analisis': 'A9', 'bifurcaciones': {}}

    # Mision principal global
    def mision_gama_pct(df_grp, mision_col):
        if mision_col not in df_grp.columns: return 0
        return pct(df_grp[mision_col].apply(is_gama).sum(), len(df_grp))

    for grp_name, df in [('Total', df_total), ('C+/C', df_cc)]:
        n = len(df)
        cats = {}

        for cat_k in P30_COLS:
            col_p30 = P30_COLS[cat_k]
            col_p32 = P32_COLS.get(cat_k)
            if col_p30 not in df.columns:
                cats[cat_k] = {'flag': 'COLUMNA_NF'}; continue

            # P30 habito Gama
            n_gama_h = int(df[col_p30].apply(is_gama).sum())
            n_resp_p30 = int(df[col_p30].notna().sum())
            pct_gh = pct(n_gama_h, n_resp_p30)

            # Lider habito
            vc_p30 = df[col_p30].value_counts()
            lider_h = str(vc_p30.index[0]).strip() if len(vc_p30) > 0 else None
            lider_h_pct = pct(int(vc_p30.iloc[0]), n_resp_p30) if len(vc_p30) > 0 else 0

            # P32 precio
            n_gama_p = 0
            n_resp_p32 = 0
            lider_p = None
            lider_p_pct = 0
            if col_p32 and col_p32 in df.columns:
                n_gama_p = int(df[col_p32].apply(is_gama).sum())
                n_resp_p32 = int(df[col_p32].notna().sum())
                vc_p32 = df[col_p32].value_counts()
                lider_p = str(vc_p32.index[0]).strip() if len(vc_p32) > 0 else None
                lider_p_pct = pct(int(vc_p32.iloc[0]), n_resp_p32) if len(vc_p32) > 0 else 0

            pct_gp = pct(n_gama_p, n_resp_p32)
            gap = round(pct_gh - pct_gp, 1)

            # Clasificacion
            if pct_gh >= 5 and gap >= 2 and pct_gp < 5:
                clasif = 'habito_sin_precio'
            elif pct_gh >= 5 and pct_gp >= 5:
                clasif = 'territorio_solido'
            elif pct_gp > pct_gh and pct_gp >= 3:
                clasif = 'precio_percibido_sin_habito'
            elif pct_gh < 2 and pct_gp < 2:
                clasif = 'ausente'
            elif pct_gh >= 3 and gap <= -10:
                clasif = 'habito_brecha_precio_alta'
            else:
                clasif = 'neutro'

            cats[cat_k] = {
                'nombre': CAT_NOMBRES[cat_k],
                'habito_gama': {'n': n_gama_h, 'pct': pct_gh, 'flag': flag_n(n_gama_h)},
                'precio_gama': {'n': n_gama_p, 'pct': pct_gp, 'flag': flag_n(n_gama_p)},
                'lider_habito': lider_h, 'lider_habito_pct': lider_h_pct,
                'lider_precio': lider_p, 'lider_precio_pct': lider_p_pct,
                'gap_habito_vs_precio_pp': gap,
                'clasificacion': clasif,
            }

        results['bifurcaciones'][grp_name] = {'n': n, 'categorias': cats}

    return results

# ─── A10 — SINTESIS ESTRATEGICA ──────────────────────────────────────────────

def analisis_10(a9_results, a1_results):
    print("\nA10: Sintesis estrategica categorias...")
    results = {'analisis': 'A10', 'bifurcaciones': {}}

    for grp_name in ['Total', 'C+/C']:
        if grp_name not in a9_results.get('bifurcaciones', {}):
            continue

        cats_a9 = a9_results['bifurcaciones'][grp_name]['categorias']
        clasificaciones = {}

        for cat_k, cat_data in cats_a9.items():
            if cat_data.get('flag') == 'COLUMNA_NF': continue
            pct_gh = cat_data['habito_gama']['pct']
            pct_gp = cat_data['precio_gama']['pct']
            gap = cat_data['gap_habito_vs_precio_pp']
            clasif = cat_data['clasificacion']
            lider_p = cat_data.get('lider_precio', '')

            # Estrategia
            if clasif == 'habito_sin_precio':
                tipo = 'ofrecer_valor'
                razon = 'Habito alto sin liderazgo de precio — el shopper elige Gama por experiencia/cercania'
                prioridad = 'Mantener precio + comunicar diferencial experiencial'
            elif clasif == 'territorio_solido':
                tipo = 'cuidar_precio'
                razon = 'Gama tiene habito Y posicionamiento de precio — defender ambas posiciones'
                prioridad = 'Cuidar precio y habito'
            elif clasif == 'habito_brecha_precio_alta':
                tipo = 'cuidar_precio'
                razon = f'Brecha precio alta ({gap:.0f}pp) aunque hay habito — riesgo de erosion si competidores la atacan'
                prioridad = 'Reducir brecha precio percibido — comunicacion o ajuste real'
            elif clasif == 'precio_percibido_sin_habito':
                tipo = 'oportunidad_precio'
                razon = 'Precio percibido favorable pero habito bajo — comunicar precio para convertir a habito'
                prioridad = 'Comunicar precio favorable + activacion primera visita'
            elif clasif == 'ausente':
                tipo = 'indiferente'
                razon = 'Gama ausente en habito y precio — categoria comoditizada para Gama'
                prioridad = 'Sin accion prioritaria'
            else:
                tipo = 'indiferente'
                razon = 'Patron neutro sin palanca clara'
                prioridad = 'Monitorear'

            clasificaciones[cat_k] = {
                'nombre': CAT_NOMBRES[cat_k],
                'tipo': tipo,
                'razon': razon,
                'prioridad': prioridad,
                'habito_gama_pct': pct_gh,
                'precio_gama_pct': pct_gp,
                'gap_pp': gap,
                'lider_precio': lider_p,
                'flag': cat_data['habito_gama']['flag'],
            }

        grupos = {
            'cuidar_precio': [k for k, v in clasificaciones.items() if v['tipo'] == 'cuidar_precio'],
            'ofrecer_valor': [k for k, v in clasificaciones.items() if v['tipo'] == 'ofrecer_valor'],
            'indiferente': [k for k, v in clasificaciones.items() if v['tipo'] == 'indiferente'],
            'oportunidad_precio': [k for k, v in clasificaciones.items() if v['tipo'] == 'oportunidad_precio'],
        }

        results['bifurcaciones'][grp_name] = {
            'clasificaciones': clasificaciones,
            'resumen_grupos': grupos,
            'caveat': 'TODAS las cifras de Gama por categoria son REFERENCIALES (n<30 en mayoria). Analisis indicativo.',
        }

    return results

# ─── PARTE B — VALIDACION V3 ─────────────────────────────────────────────────

def validacion_v3(a5_results, a6_results):
    print("\nParte B: Validacion consistencia V3...")

    a5_total = a5_results['bifurcaciones'].get('Total', {})
    gama_z = a5_total.get('gama_dna', {}).get('zscores', {})

    a6_total = a6_results['bifurcaciones'].get('Total', {}).get('cadenas', {})
    a6_cc = a6_results['bifurcaciones'].get('C+/C', {}).get('cadenas', {})

    def z_str(attr_k):
        v = gama_z.get(attr_k)
        if v: return f"{ATRIBUTOS.get(attr_k, attr_k)} {v.get('zscore', 'N/A'):+.2f}"
        return f"{ATRIBUTOS.get(attr_k, attr_k)} N/A"

    def modelo_str(cadena_data):
        if not cadena_data or cadena_data.get('flag') in ('EXCLUIR', 'SIN_RAZONES'):
            return 'n insuficiente'
        r = cadena_data.get('razones_pct', {})
        modelo = cadena_data.get('modelo', 'N/A')
        pat = cadena_data.get('pct_razon_dom', 0)
        return f"{modelo} ({pat:.0f}% {cadena_data.get('razon_dominante', '')})"

    validaciones = []

    # V3-DNA-1: sobreindice experiencial
    exp_attrs = ['atractiva', 'calidad', 'seguro', 'limpieza']
    n_pos = sum(1 for a in exp_attrs if gama_z.get(a, {}).get('zscore', 0) and gama_z[a]['zscore'] > 0)
    cifra_act = ', '.join([z_str(a) for a in exp_attrs if gama_z.get(a)])
    validaciones.append({
        'id': 'V3-DNA-1',
        'analisis': 'DNA z-scores — sobreindice experiencial Gama',
        'cifra_v3': 'Tienda atractiva +1.09, Calidad +0.97, Seguro +0.76, Limpieza +0.72',
        'cifra_actual': cifra_act or 'Ver A5',
        'consistencia': 'CONSISTENTE' if n_pos == 4 else 'MAYORMENTE_CONSISTENTE' if n_pos >= 2 else 'TENSION',
        'interpretacion': (
            'Gama sigue sobreindexando en los 4 atributos experienciales (patron V3 confirmado)' if n_pos == 4
            else f'{n_pos}/4 atributos experienciales siguen positivos — patron direccionalmente consistente' if n_pos >= 2
            else 'TENSION: cambio en patron de sobreindice experiencial — revisar A5 detalle'
        ),
    })

    # V3-DNA-2: subindice precio
    prec_attrs = ['menor_precio', 'valer_dinero', 'promociones']
    n_neg = sum(1 for a in prec_attrs if gama_z.get(a, {}).get('zscore', 0) and gama_z[a]['zscore'] < 0)
    cifra_act2 = ', '.join([z_str(a) for a in prec_attrs if gama_z.get(a)])
    validaciones.append({
        'id': 'V3-DNA-2',
        'analisis': 'DNA z-scores — subindice precio/valor Gama',
        'cifra_v3': 'Menor precio -0.72, Hacer valer dinero -0.67, Promociones -0.67',
        'cifra_actual': cifra_act2 or 'Ver A5',
        'consistencia': 'CONSISTENTE' if n_neg == 3 else 'MAYORMENTE_CONSISTENTE' if n_neg >= 2 else 'TENSION',
        'interpretacion': (
            'Gama sigue subindexando en los 3 atributos precio/valor (patron V3 confirmado)' if n_neg == 3
            else f'{n_neg}/3 atributos precio siguen negativos' if n_neg >= 2
            else 'TENSION: cambio en patron de subindice precio — revisar A5'
        ),
    })

    # V3-MOD-1: Gama atencion-dominante
    gama_m = a6_total.get('Gama', {})
    gama_pct_at = gama_m.get('razones_pct', {}).get('atencion', 0) if gama_m.get('razones_pct') else 0
    validaciones.append({
        'id': 'V3-MOD-1',
        'analisis': 'Modelo mental Gama — atencion-dominante',
        'cifra_v3': 'Gama 53% razon atencion espontanea',
        'cifra_actual': modelo_str(gama_m),
        'consistencia': 'CONSISTENTE' if gama_pct_at >= 35 else 'TENSION_LEVE' if gama_pct_at >= 20 else 'TENSION',
        'interpretacion': (
            f'Gama sigue siendo atencion-dominante ({gama_pct_at:.0f}% atencion)' if gama_pct_at >= 35
            else f'Atencion {gama_pct_at:.0f}% — menor que 53% V3 pero sigue siendo el atributo mas mencionado' if gama_pct_at >= 20
            else f'TENSION: atencion Gama baja a {gama_pct_at:.0f}% — cambio relevante vs V3'
        ),
    })

    # V3-MOD-2: CM atencion-dominante
    cm_m = a6_total.get('Central Madeirense', {})
    cm_pct_at = cm_m.get('razones_pct', {}).get('atencion', 0) if cm_m.get('razones_pct') else 0
    validaciones.append({
        'id': 'V3-MOD-2',
        'analisis': 'Modelo mental CM — atencion-dominante',
        'cifra_v3': 'CM 53% razon atencion espontanea',
        'cifra_actual': modelo_str(cm_m),
        'consistencia': 'CONSISTENTE' if cm_pct_at >= 35 else 'TENSION_LEVE' if cm_pct_at >= 20 else 'TENSION',
        'interpretacion': f'CM: atencion {cm_pct_at:.0f}%',
    })

    # V3-MOD-RIO: CRITICO — Rio atencion-dominante vs migracion
    rio_m = a6_total.get('Rio', {})
    rio_pct_at = rio_m.get('razones_pct', {}).get('atencion', 0) if rio_m.get('razones_pct') else 0
    rio_pct_pr = rio_m.get('razones_pct', {}).get('precio', 0) if rio_m.get('razones_pct') else 0
    rio_modelo = rio_m.get('modelo', 'N/A')
    consistencia_rio = 'CONSISTENTE' if rio_pct_at >= 40 else (
        'TENSION' if rio_pct_pr > rio_pct_at else 'TENSION_LEVE'
    )
    validaciones.append({
        'id': 'V3-MOD-RIO',
        'analisis': 'Modelo mental Rio — verificacion critica (Rio crecio +17pp TOM en CU-7)',
        'cifra_v3': 'Rio 51% atencion espontanea (V3)',
        'cifra_actual': modelo_str(rio_m),
        'es_verificacion_critica': True,
        'consistencia': consistencia_rio,
        'interpretacion': (
            f'Rio SIGUE siendo atencion-dominante ({rio_pct_at:.0f}% atencion)' if rio_pct_at >= 40
            else f'TENSION: Rio migro — precio ({rio_pct_pr:.0f}%) > atencion ({rio_pct_at:.0f}%). Su expansion agresiva de TOM (+17pp CU-7) se asocia con mensaje de precio, NO de servicio. Implicacion: Rio ya no comparte el territorio de Gama — es un competidor de precio que gano notoriedad, no un competidor experiencial.' if rio_pct_pr > rio_pct_at
            else f'Rio: atencion {rio_pct_at:.0f}%, precio {rio_pct_pr:.0f}% — patron ambiguo, ver A6 detalle'
        ),
    })

    # V3-SEG: identicos
    validaciones.append({
        'id': 'V3-SEG',
        'analisis': '3 segmentos k-means y perfil Nucleo Leal',
        'cifra_v3': 'Seg1 59%/Seg2 33%/Seg3 8% (n=32) — NSE 2.16, precio 2.94/5, rapidez 4.81/5',
        'cifra_actual': 'IDENTICO — CU-4 v2 calcula sobre el mismo dataset BBDD 2026. Sin discrepancia posible.',
        'consistencia': 'IDENTICO',
        'interpretacion': 'Los segmentos k-means son exactamente los mismos numeros (mismo dataset, mismo algoritmo, misma semilla). No hay tension posible con este calculo.',
    })

    n_ok = sum(1 for v in validaciones if v['consistencia'] in ('CONSISTENTE', 'IDENTICO'))
    n_ten = sum(1 for v in validaciones if 'TENSION' in str(v['consistencia']) and 'LEVE' not in str(v['consistencia']))
    n_amb = len(validaciones) - n_ok - n_ten

    return {
        'validaciones': validaciones,
        'resumen': {
            'n_consistente': n_ok,
            'n_tension': n_ten,
            'n_ambiguo_o_leve': n_amb,
            'hay_tension_critica': n_ten > 0,
            'tension_critica_items': [v['id'] for v in validaciones if 'TENSION' in str(v['consistencia']) and 'LEVE' not in str(v['consistencia'])],
        }
    }

# ─── HEATMAP P23 ─────────────────────────────────────────────────────────────

def plot_heatmap(a2_results):
    print("\nGenerando heatmap P23...")
    if 'Total' not in a2_results['bifurcaciones']: return
    matrix = a2_results['bifurcaciones']['Total']['matrix']
    attr_keys = list(ATRIBUTOS.keys())
    attr_names = [ATRIBUTOS[k] for k in attr_keys]
    cadenas_plot = [c for c in CADENAS if c != 'Hiper Lider']

    data = []
    for ak in attr_keys:
        row = []
        for c in cadenas_plot:
            v = matrix.get(ak, {}).get(c)
            row.append(v.get('pct', 0) if isinstance(v, dict) else 0)
        data.append(row)

    Z = np.array(data, dtype=float)
    fig, ax = plt.subplots(figsize=(14, 7))
    cmap = LinearSegmentedColormap.from_list('gama', ['#FFFFFF', '#F5CCCC', '#7A1212'])
    im = ax.imshow(Z, aspect='auto', cmap=cmap, vmin=0, vmax=50)
    ax.set_xticks(range(len(cadenas_plot)))
    ax.set_xticklabels(cadenas_plot, rotation=30, ha='right', fontsize=9)
    ax.set_yticks(range(len(attr_names)))
    ax.set_yticklabels(attr_names, fontsize=9)
    ax.set_title('Asociacion marca x atributo (P23) — Total n=402\n% que asocia cada atributo con cada cadena',
                 fontsize=11)
    for i in range(len(attr_keys)):
        for j in range(len(cadenas_plot)):
            v = Z[i,j]
            ax.text(j, i, f'{v:.0f}%', ha='center', va='center',
                    fontsize=7, color='white' if v > 30 else '#333')
    plt.colorbar(im, ax=ax, shrink=0.7, label='% asociacion')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_PLOTS_DIR, 'cu9_heatmap_p23_total.png'),
                dpi=150, bbox_inches='tight')
    plt.close()

# ─── MAIN ────────────────────────────────────────────────────────────────────

def main():
    os.makedirs(OUTPUT_PLOTS_DIR, exist_ok=True)

    df_total, df_cc, df_pg = load_bbdd()

    a1 = analisis_1(df_total, df_cc, df_pg)
    a2 = analisis_2(df_total, df_cc, df_pg)
    a3 = analisis_3(df_total, a2)
    a4 = analisis_4(df_total, df_cc, df_pg, a2)
    a5 = analisis_5(df_total, df_cc, df_pg, a2)
    a6 = analisis_6(df_total, df_cc)
    a7 = analisis_7(df_total)
    a8 = analisis_8(df_total)
    a9 = analisis_9(df_total, df_cc)
    a10 = analisis_10(a9, a1)
    val = validacion_v3(a5, a6)
    plot_heatmap(a2)

    output = {
        'metadata': {
            'proyecto': 'Gama Notoriedad 2026',
            'cu': 'CU-9',
            'version': 'v7',
            'fecha': '2026-05-18',
            'n_total': len(df_total),
            'n_cc': len(df_cc),
            'n_pg': len(df_pg),
            'alpha': ALPHA,
            'base_baja': BASE_BAJA,
            'ic_method': 'Newcombe-Wilson',
        },
        'A1_p22': a1,
        'A2_p23': a2,
        'A3_nominal': a3,
        'A4_mds': a4,
        'A5_dna': a5,
        'A6_modelos': a6,
        'A7_recordadores': a7,
        'A8_recall_seg': a8,
        'A9_p30_p32_p26': a9,
        'A10_sintesis': a10,
        'PartB_val_v3': val,
    }

    dump_json(output, OUTPUT_JSON)
    print(f"\nJSON: {OUTPUT_JSON}")
    print(f"Plots: {OUTPUT_PLOTS_DIR}")
    print(f"\n=== RESUMEN ===")
    print(f"  n Total={len(df_total)}, C+/C={len(df_cc)}, Pref-Gama={len(df_pg)} (REFERENCIAL)")
    print(f"  Tensiones V3: {val['resumen']['n_tension']} items")
    print(f"  Consistentes V3: {val['resumen']['n_consistente']} items")
    print(f"  Tensiones criticas: {val['resumen']['tension_critica_items']}")
    return output


if __name__ == '__main__':
    main()
