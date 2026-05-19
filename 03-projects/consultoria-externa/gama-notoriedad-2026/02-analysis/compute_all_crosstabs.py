"""Fase 2+3: Backend cross-tab generator + pre-compute todas las tablas a JSON.

Para cada pregunta del cuestionario x cada BK, genera tabla con:
- Filas: códigos/categorías de respuesta
- Columnas: Total + niveles del BK
- Celdas: N, %, letras SPSS sig, color (verde sig+, rojo sig-)

Soporta: single_select, multi_select, escala_1_5, numerica, abierta
Significancia: Z-test column proportions vs Total + pairwise entre BK levels
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd
import numpy as np
import json
import re
from math import sqrt
from collections import defaultdict
from scipy.stats import norm

BBDD = r"G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\BBDD Notoriedad 2026.xlsx"
MAP_JSON = r"C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis\questionnaire_map.json"
OUT_JSON = r"C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis\all_tables.json"

ALPHA = 0.05  # nivel de significancia para tests

# Cargar BBDD + mapeo
df = pd.read_excel(BBDD)
print(f"BBDD cargada: n={len(df)} x {len(df.columns)} cols")
q_map = json.load(open(MAP_JSON, encoding='utf-8'))
print(f"Mapeo cargado: {len(q_map)} preguntas")

# ===== LIMPIEZA DE STRINGS BBDD =====
# Muchos valores tienen \xa0 (non-breaking space) o espacios extra
def clean_str(x):
    if pd.isna(x):
        return None
    s = str(x).replace('\xa0', ' ').strip()
    return s if s else None

# ===== CONFIGURACIÓN DE BREAK-DOWNS =====
BK_CONFIG = {
    'NSE': {
        'col': '{PD4} [V153] Marcar nse zona',
        'levels_order': ['C+/C', 'D', 'E'],
        'cleaner': clean_str,
    },
    'Genero': {
        'col': '{PF5} [V150] Genero',
        'levels_order': ['Femenino', 'Masculino'],
        'cleaner': clean_str,
    },
    'Edad': {
        'col': '{PF7} [V152] Grupo edad',
        'levels_order': ['25 a 34 años', '35 a 44 años', '45 a 54 años', '55 a 64 años'],
        'cleaner': clean_str,
    },
    'Municipio': {
        'col': ' {PF2} [V535] Municipio',
        'levels_order': ['Baruta', 'Chacao', 'El Hatillo', 'Libertador', 'Sucre', 'FORANEOS'],
        'cleaner': clean_str,
    },
    'Marca preferida': {
        'col': ' {P21} [V194] Preferido',
        'levels_order': ['Paramo', 'Central Madeirense', 'Forum', 'Rio', 'Plazas',
                         'Gama Excelsior', 'Luz', 'Plan Suarez', 'Otros'],
        'cleaner': clean_str,
        'group_other': True,  # agrupa las demás en "Otros"
    },
    'Mision': {
        'col': ' {P25} [V249] Razón última compra en ese supermercado',
        'levels_order_abbrev': {
            'Reabastecer': 'reabastecer',
            'Abastecimiento': 'abastecimiento general',
            'Urgencia': 'urgencia',
            # 'Evento' y 'Electrodomésticos' tienen n<10 — excluidos
        },
        'cleaner': clean_str,
    },
}

def find_bbdd_col(col_pattern):
    """Encuentra la col real en df.columns que matchea el patrón (caso de espacios leading)."""
    for c in df.columns:
        if str(c).strip() == col_pattern.strip():
            return c
    # Fallback: busca parcial
    for c in df.columns:
        if col_pattern.strip() in str(c):
            return c
    return None

# Resolver columnas BBDD reales para cada BK
for bk_name, cfg in BK_CONFIG.items():
    real_col = find_bbdd_col(cfg['col'])
    if real_col:
        cfg['col_real'] = real_col
    else:
        print(f"  WARNING: BK {bk_name} col no encontrada: {cfg['col']}")

# Validar BK cols
print("\nBKs configurados:")
for bk, cfg in BK_CONFIG.items():
    print(f"  {bk}: col='{cfg.get('col_real','MISSING')}'")

# ===== FUNCIONES DE SIGNIFICANCIA =====
def z_test_two_proportions(p1, n1, p2, n2):
    """Z-test para diferencia de 2 proporciones independientes.
    Returns z, p_value (two-tailed)."""
    if n1 == 0 or n2 == 0:
        return 0, 1.0
    p_pool = (p1*n1 + p2*n2) / (n1 + n2)
    if p_pool == 0 or p_pool == 1:
        return 0, 1.0
    se = sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))
    if se == 0:
        return 0, 1.0
    z = (p1 - p2) / se
    p = 2 * (1 - norm.cdf(abs(z)))
    return z, p

def assign_sig_letters(col_values, col_ns, alpha=ALPHA, min_n=30):
    """Para una fila dada, asigna letras superíndice de significancia entre columnas.

    Args:
        col_values: list de proporciones (0-1) por columna BK
        col_ns: list de bases (N) por columna BK
        alpha: nivel sig

    Returns:
        list de strings (letras superíndice por columna).
        Ej: ['BC', '', 'A'] = col 1 sig mayor que cols 2 y 3; col 3 sig mayor que col 1.
    """
    n_cols = len(col_values)
    letters_per_col = [[] for _ in range(n_cols)]
    col_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'][:n_cols]
    # Pairwise comparisons
    for i in range(n_cols):
        for j in range(n_cols):
            if i == j:
                continue
            if col_ns[i] < min_n or col_ns[j] < min_n:
                continue
            z, p = z_test_two_proportions(col_values[i], col_ns[i], col_values[j], col_ns[j])
            if p < alpha and col_values[i] > col_values[j]:
                # col i es sig mayor que col j: agrega letra de j a las letras de i
                letters_per_col[i].append(col_letters[j])
    return [''.join(sorted(set(L))) for L in letters_per_col]

def assign_color_vs_total(row_values, row_ns, total_value, total_n, alpha=ALPHA, min_n=30):
    """Para cada celda BK level, retorna color flag: 'pos', 'neg', 'neutral'.
    Compara la celda vs el TOTAL.
    """
    colors = []
    for v, n in zip(row_values, row_ns):
        if n < min_n or total_n < min_n:
            colors.append('neutral')
            continue
        z, p = z_test_two_proportions(v, n, total_value, total_n)
        if p < alpha:
            colors.append('pos' if v > total_value else 'neg')
        else:
            colors.append('neutral')
    return colors

# ===== FUNCIONES DE BUILD TABLE POR TIPO =====
def build_bk_filter(df_input, bk_name):
    """Retorna dict {level_label: boolean_mask} para el BK seleccionado."""
    cfg = BK_CONFIG[bk_name]
    col = cfg['col_real']
    series = df_input[col].apply(cfg['cleaner'])

    if bk_name == 'Marca preferida':
        # Aplicar agrupación top 8 + Otros
        top_brands = ['Paramo', 'Central Madeirense', 'Forum', 'Rio', 'Plazas',
                      'Gama Excelsior', 'Luz', 'Plan Suarez']
        mapped = series.apply(lambda x: x if x in top_brands else ('Otros' if pd.notna(x) else None))
        masks = {b: (mapped == b) for b in cfg['levels_order']}
    elif bk_name == 'Mision':
        # Agrupar P25 (textos largos) en 3 categorías
        masks = {}
        for label, keyword in cfg['levels_order_abbrev'].items():
            masks[label] = series.apply(lambda x: keyword in str(x).lower() if pd.notna(x) else False)
    else:
        masks = {lvl: (series == lvl) for lvl in cfg['levels_order']}

    # Filtra niveles con base muy baja
    return {lvl: m for lvl, m in masks.items() if m.sum() >= 5}

def crosstab_single_select(q_meta, bk_name, df_input):
    """Tabla single-select x BK."""
    col = q_meta['cols'][0]['col_name']
    series = df_input[col].apply(clean_str)
    base_mask = series.notna()
    df_filtered = df_input[base_mask]
    series = series[base_mask]

    bk_masks = build_bk_filter(df_filtered, bk_name)
    if not bk_masks:
        return None

    # Filas = categorías ordenadas por frecuencia Total
    categories = series.value_counts().head(20).index.tolist()
    bk_levels = list(bk_masks.keys())

    table_rows = []
    for cat in categories:
        cat_mask = (series == cat)
        n_total = base_mask.sum()
        v_total = cat_mask.sum() / n_total if n_total > 0 else 0

        col_ns = []
        col_values = []
        for lvl in bk_levels:
            m = bk_masks[lvl] & cat_mask
            n_lvl = bk_masks[lvl].sum()
            v_lvl = m.sum() / n_lvl if n_lvl > 0 else 0
            col_ns.append(n_lvl)
            col_values.append(v_lvl)

        sig_letters = assign_sig_letters(col_values, col_ns)
        colors = assign_color_vs_total(col_values, col_ns, v_total, n_total)

        table_rows.append({
            'category': str(cat)[:80],
            'total': {'n': int(cat_mask.sum()), 'pct': round(v_total*100, 1)},
            'bk_cells': [
                {
                    'level': lvl,
                    'n': int((bk_masks[lvl] & cat_mask).sum()),
                    'pct': round(v*100, 1),
                    'sig_letters': letters,
                    'color': color,
                }
                for lvl, v, letters, color in zip(bk_levels, col_values, sig_letters, colors)
            ],
        })

    return {
        'type': 'single_select',
        'base_total': int(base_mask.sum()),
        'base_bk_levels': {lvl: int(bk_masks[lvl].sum()) for lvl in bk_levels},
        'bk_levels': bk_levels,
        'rows': table_rows,
    }

NEGATIVE_VALUES = {'no', 'ninguno', 'ninguno (no leer)', 'ningun', '0', 'none', 'no recuerda',
                   'ninguno(*)', 'ninguno en particular'}

def detect_multi_subtype(cols, df_input):
    """Detecta sub-tipo de multi_select:
    - 'flags': cada col es un item, valor = name del item o nulo (P16, P17, P19, P20)
              → métrica: % que menciona cada item
    - 'pivot': cada col es un item, valor = cadena elegida (P23, P26, P30, P32)
              → desglosar en sub-preguntas single_select
    """
    sample_col = df_input[cols[0]['col_name']].apply(clean_str)
    unique_vals = [v for v in sample_col.dropna().unique() if v]
    if not unique_vals:
        return 'flags'
    # Heurística: si todos los valores no-vacios contienen el item_label en su texto
    # → flags (la celda tiene el nombre del propio item cuando está marcada)
    item_label = cols[0].get('item_label', '') or ''
    if item_label:
        item_words = [w for w in item_label.lower().split() if len(w) > 3]
        if item_words:
            matches = sum(1 for v in unique_vals[:10]
                          if any(w in str(v).lower() for w in item_words))
            if matches >= max(1, len(unique_vals[:10]) // 2):
                return 'flags'
    # Si la mayoría de valores únicos son nombres de cadenas conocidas
    BRANDS = {'paramo', 'forum', 'gama', 'rio', 'plazas', 'luz', 'plan suarez',
              'central madeirense', 'hiper lider', 'la muralla', 'la granja'}
    brand_matches = sum(1 for v in unique_vals[:15]
                        if any(b in str(v).lower() for b in BRANDS))
    if brand_matches >= len(unique_vals[:15]) * 0.6:
        return 'pivot'
    return 'flags'


def crosstab_multi_select_flags(q_meta, bk_name, df_input):
    """Multi-select 'flags' subtype: items son cadenas, valor = nombre cadena o nulo.
    Métrica: % personas que mencionan cada item (cadena). P16, P17, P19, P20."""
    cols = q_meta['cols']
    bk_masks = build_bk_filter(df_input, bk_name)
    if not bk_masks:
        return None
    bk_levels = list(bk_masks.keys())

    table_rows = []
    for col_meta in cols:
        col_name = col_meta['col_name']
        item_label = col_meta['item_label'] or col_meta['base_desc'][:60]
        series = df_input[col_name].apply(clean_str)
        is_positive = series.apply(
            lambda x: pd.notna(x) and str(x).strip().lower() not in NEGATIVE_VALUES
        )

        n_total = len(df_input)
        v_total = is_positive.sum() / n_total if n_total > 0 else 0

        col_ns, col_values = [], []
        for lvl in bk_levels:
            m = bk_masks[lvl] & is_positive
            n_lvl = bk_masks[lvl].sum()
            v_lvl = m.sum() / n_lvl if n_lvl > 0 else 0
            col_ns.append(n_lvl)
            col_values.append(v_lvl)

        sig_letters = assign_sig_letters(col_values, col_ns)
        colors = assign_color_vs_total(col_values, col_ns, v_total, n_total)

        table_rows.append({
            'category': item_label,
            'total': {'n': int(is_positive.sum()), 'pct': round(v_total*100, 1)},
            'bk_cells': [
                {'level': lvl, 'n': int((bk_masks[lvl] & is_positive).sum()),
                 'pct': round(v*100, 1), 'sig_letters': letters, 'color': color}
                for lvl, v, letters, color in zip(bk_levels, col_values, sig_letters, colors)
            ],
        })

    return {
        'type': 'multi_select_flags',
        'base_total': len(df_input),
        'base_bk_levels': {lvl: int(bk_masks[lvl].sum()) for lvl in bk_levels},
        'bk_levels': bk_levels,
        'rows': table_rows,
        'note': 'Multi-select: % personas que mencionan cada cadena. Filas no suman 100%.',
    }


def crosstab_multi_select_pivot_single_col(col_meta, bk_name, df_input, item_label):
    """Para UNA col individual de un multi-select 'pivot' (P23, P26, P30, P32):
    trata la col como single_select estándar (distribución de cadenas elegidas).
    """
    col_name = col_meta['col_name']
    series = df_input[col_name].apply(clean_str)
    base_mask = series.notna() & (series.str.strip().str.lower() != '')
    if base_mask.sum() == 0:
        return None
    df_filtered = df_input[base_mask]
    series = series[base_mask]

    bk_masks = build_bk_filter(df_filtered, bk_name)
    if not bk_masks:
        return None
    bk_levels = list(bk_masks.keys())

    categories = series.value_counts().head(15).index.tolist()
    n_total = base_mask.sum()

    table_rows = []
    for cat in categories:
        cat_mask = (series == cat)
        v_total = cat_mask.sum() / n_total if n_total > 0 else 0

        col_ns, col_values = [], []
        for lvl in bk_levels:
            m = bk_masks[lvl] & cat_mask
            n_lvl = bk_masks[lvl].sum()
            v_lvl = m.sum() / n_lvl if n_lvl > 0 else 0
            col_ns.append(n_lvl)
            col_values.append(v_lvl)

        sig_letters = assign_sig_letters(col_values, col_ns)
        colors = assign_color_vs_total(col_values, col_ns, v_total, n_total)

        table_rows.append({
            'category': str(cat)[:80],
            'total': {'n': int(cat_mask.sum()), 'pct': round(v_total*100, 1)},
            'bk_cells': [
                {'level': lvl, 'n': int((bk_masks[lvl] & cat_mask).sum()),
                 'pct': round(v*100, 1), 'sig_letters': letters, 'color': color}
                for lvl, v, letters, color in zip(bk_levels, col_values, sig_letters, colors)
            ],
        })

    return {
        'type': 'single_select',
        'base_total': int(base_mask.sum()),
        'base_bk_levels': {lvl: int(bk_masks[lvl].sum()) for lvl in bk_levels},
        'bk_levels': bk_levels,
        'rows': table_rows,
        'note': f'Sub-pregunta de pregunta pivot: {item_label}',
    }


def crosstab_multi_select(q_meta, bk_name, df_input):
    """Dispatcher según subtipo (flags vs pivot)."""
    cols = q_meta['cols']
    subtype = detect_multi_subtype(cols, df_input)
    if subtype == 'flags':
        return crosstab_multi_select_flags(q_meta, bk_name, df_input)
    # 'pivot' se maneja diferente: desglosa en sub-preguntas fuera de esta función
    return None  # Marca para desglose externo

def crosstab_escala_1_5(q_meta, bk_name, df_input):
    """Escala 1-5 (P22 importancia): para cada atributo muestra TB% y T2B%."""
    cols = q_meta['cols']
    bk_masks = build_bk_filter(df_input, bk_name)
    if not bk_masks:
        return None
    bk_levels = list(bk_masks.keys())

    SCALE_MAP = {
        'Muy importante': 5, 'Importante': 4, 'Algo importante': 3,
        'Poco importante': 2, 'Nada importante': 1,
        'Muy Importante': 5,
    }

    table_rows = []
    for col_meta in cols:
        col_name = col_meta['col_name']
        item_label = (col_meta['base_desc'].replace('IMPORTANCIA', '').strip() or col_meta['item_label'] or 'item')[:60]
        series_raw = df_input[col_name].apply(clean_str)
        numeric = series_raw.map(SCALE_MAP)
        base = numeric.notna()
        df_b = df_input[base]
        numeric_b = numeric[base]

        n_total = base.sum()
        if n_total == 0:
            continue
        v_total_tb = (numeric_b == 5).sum() / n_total

        col_ns = []
        col_values_tb = []
        for lvl in bk_levels:
            m_lvl = bk_masks[lvl] & base
            n_lvl = m_lvl.sum()
            tb = (numeric[m_lvl] == 5).sum() / n_lvl if n_lvl > 0 else 0
            col_ns.append(int(n_lvl))
            col_values_tb.append(tb)

        sig_letters = assign_sig_letters(col_values_tb, col_ns)
        colors = assign_color_vs_total(col_values_tb, col_ns, v_total_tb, n_total)

        table_rows.append({
            'category': item_label,
            'total': {'n': int((numeric_b == 5).sum()), 'pct': round(v_total_tb*100, 1)},
            'bk_cells': [
                {'level': lvl, 'n': int((bk_masks[lvl] & base & (numeric == 5)).sum()),
                 'pct': round(v*100, 1), 'sig_letters': letters, 'color': color}
                for lvl, v, letters, color in zip(bk_levels, col_values_tb, sig_letters, colors)
            ],
        })

    return {
        'type': 'escala_1_5',
        'base_total': len(df_input),
        'base_bk_levels': {lvl: int(bk_masks[lvl].sum()) for lvl in bk_levels},
        'bk_levels': bk_levels,
        'rows': table_rows,
        'note': 'Top Box puro (% "Muy importante"). Filas son los 10 atributos.',
    }

def crosstab_numerica(q_meta, bk_name, df_input):
    """Numérica (P31 ranking): muestra mean rank por cadena x BK."""
    cols = q_meta['cols']
    bk_masks = build_bk_filter(df_input, bk_name)
    if not bk_masks:
        return None
    bk_levels = list(bk_masks.keys())

    table_rows = []
    for col_meta in cols:
        col_name = col_meta['col_name']
        item_label = col_meta['item_label'] or col_meta['base_desc'][:60]
        series = pd.to_numeric(df_input[col_name], errors='coerce')
        base = series.notna()
        n_total = base.sum()
        mean_total = series[base].mean() if n_total > 0 else 0

        bk_cells = []
        for lvl in bk_levels:
            m = bk_masks[lvl] & base
            n_lvl = m.sum()
            mean_lvl = series[m].mean() if n_lvl > 0 else 0
            bk_cells.append({
                'level': lvl, 'n': int(n_lvl),
                'pct': round(mean_lvl, 2),  # 'pct' aquí es la media
                'sig_letters': '', 'color': 'neutral',
            })

        table_rows.append({
            'category': item_label,
            'total': {'n': int(n_total), 'pct': round(mean_total, 2)},
            'bk_cells': bk_cells,
        })

    return {
        'type': 'numerica',
        'base_total': len(df_input),
        'base_bk_levels': {lvl: int(bk_masks[lvl].sum()) for lvl in bk_levels},
        'bk_levels': bk_levels,
        'rows': table_rows,
        'note': 'Valores son MEDIA ranking (1=mejor, 10=peor). Sin test de sig por simplicidad.',
    }

def crosstab_abierta(q_meta, bk_name, df_input):
    """Abierta: top 10 respuestas textuales x BK."""
    col = q_meta['cols'][0]['col_name']
    series = df_input[col].apply(clean_str)
    base = series.notna()
    df_filtered = df_input[base]
    series = series[base]

    bk_masks = build_bk_filter(df_filtered, bk_name)
    if not bk_masks:
        return None
    bk_levels = list(bk_masks.keys())

    top_responses = series.value_counts().head(10).index.tolist()
    n_total = base.sum()

    table_rows = []
    for resp in top_responses:
        cat_mask = (series == resp)
        v_total = cat_mask.sum() / n_total if n_total > 0 else 0
        col_ns = []
        col_values = []
        for lvl in bk_levels:
            m_lvl = bk_masks[lvl]
            n_lvl = m_lvl.sum()
            n_match = (m_lvl & cat_mask).sum()
            v_lvl = n_match / n_lvl if n_lvl > 0 else 0
            col_ns.append(int(n_lvl))
            col_values.append(v_lvl)
        sig_letters = assign_sig_letters(col_values, col_ns, min_n=15)
        colors = assign_color_vs_total(col_values, col_ns, v_total, n_total, min_n=15)
        table_rows.append({
            'category': str(resp)[:100],
            'total': {'n': int(cat_mask.sum()), 'pct': round(v_total*100, 1)},
            'bk_cells': [
                {'level': lvl, 'n': int((bk_masks[lvl] & cat_mask).sum()),
                 'pct': round(v*100, 1), 'sig_letters': letters, 'color': color}
                for lvl, v, letters, color in zip(bk_levels, col_values, sig_letters, colors)
            ],
        })

    return {
        'type': 'abierta',
        'base_total': int(base.sum()),
        'base_bk_levels': {lvl: int(bk_masks[lvl].sum()) for lvl in bk_levels},
        'bk_levels': bk_levels,
        'rows': table_rows,
        'note': 'Top 10 respuestas textuales. Bases pequeñas en filtrada — interpretar con cuidado.',
    }

# Despachador por tipo
DISPATCHER = {
    'single_select': crosstab_single_select,
    'multi_select':  crosstab_multi_select,
    'escala_1_5':    crosstab_escala_1_5,
    'numerica':      crosstab_numerica,
    'abierta':       crosstab_abierta,
}

# Excluir preguntas operacionales / sin valor analítico
EXCLUDE_QUESTIONS = {'PD5', 'PD6', 'PD7', 'PD8', 'PD9', 'P43'}

# ===== PRE-COMPUTE TODAS LAS TABLAS =====
print(f"\n{'='*80}\nPRE-COMPUTANDO TABLAS\n{'='*80}")
all_tables = {'_meta': {'bk_list': list(BK_CONFIG.keys()),
                        'n_total': len(df),
                        'fecha': '2026-05-18',
                        'alpha': ALPHA}}

questions_processed = 0
tables_generated = 0
errors = []

for q_code, q_meta in q_map.items():
    if q_code in EXCLUDE_QUESTIONS:
        continue
    tipo = q_meta['tipo']
    func = DISPATCHER.get(tipo)
    if not func:
        errors.append(f"{q_code}: tipo desconocido {tipo}")
        continue

    # Caso especial: multi_select 'pivot' (P26, P30, P32) → desglosar en sub-preguntas
    is_pivot = False
    if tipo == 'multi_select':
        subtype = detect_multi_subtype(q_meta['cols'], df)
        if subtype == 'pivot':
            is_pivot = True

    if is_pivot:
        # Desglosar cada col en sub-pregunta P30:1, P30:2, ...
        for idx, col_meta in enumerate(q_meta['cols'], start=1):
            item_label = col_meta['item_label'] or col_meta['base_desc'][:50]
            sub_code = f"{q_code}:{idx}"
            sub_tables = {}
            for bk_name in BK_CONFIG.keys():
                try:
                    result = crosstab_multi_select_pivot_single_col(
                        col_meta, bk_name, df, item_label
                    )
                    if result:
                        sub_tables[bk_name] = result
                        tables_generated += 1
                except Exception as e:
                    errors.append(f"{sub_code} x {bk_name}: {type(e).__name__}: {str(e)[:80]}")
            if sub_tables:
                all_tables[sub_code] = {
                    'tipo': 'single_select',
                    'base_description': f"{q_meta['base_description'][:80]} — {item_label}",
                    'n_items': 1,
                    'parent_question': q_code,
                    'tables_by_bk': sub_tables,
                }
                questions_processed += 1
        continue

    # Caso normal
    q_tables = {}
    for bk_name in BK_CONFIG.keys():
        try:
            result = func(q_meta, bk_name, df)
            if result:
                q_tables[bk_name] = result
                tables_generated += 1
        except Exception as e:
            errors.append(f"{q_code} x {bk_name}: {type(e).__name__}: {str(e)[:80]}")

    if q_tables:
        all_tables[q_code] = {
            'tipo': tipo,
            'base_description': q_meta['base_description'][:120],
            'n_items': q_meta['n_cols'],
            'tables_by_bk': q_tables,
        }
        questions_processed += 1

print(f"\nPreguntas procesadas: {questions_processed}")
print(f"Tablas generadas: {tables_generated}")
print(f"Errores: {len(errors)}")
if errors:
    print("\nDetalle errores:")
    for e in errors[:20]:
        print(f"  - {e}")

# Export JSON
with open(OUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(all_tables, f, ensure_ascii=False, indent=1, default=str)
import os
size_mb = os.path.getsize(OUT_JSON) / 1024 / 1024
print(f"\nJSON exportado: {OUT_JSON} ({size_mb:.2f} MB)")
