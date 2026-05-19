"""Fase 1 v2: Mapea cada pregunta del cuestionario a sus columnas BBDD.
Output: questionnaire_map.json con metadata completa por pregunta.

Patrones en BBDD detectados:
- Formato col: " {Pxx} [Vyyy] descripcion - item_label"
- 292 cols con formato {Pxx}, 3 sin formato regular
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd
import re
import json
from collections import defaultdict

BBDD = r"G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\BBDD Notoriedad 2026.xlsx"
OUT = r"C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis\questionnaire_map.json"

df = pd.read_excel(BBDD)
print(f"BBDD: n={len(df)} x {len(df.columns)} cols")

# Regex robusto (acepta espacios leading + sub-ID con . o : )
# Match: {PD4}, {P21}, {P21.1}, {P23:1}, {P23:10}
RE_Q = re.compile(r'^\s*\{(P[FD]?\d+(?:[\.:]\d+)?)\}', re.I)
# Extraer descripcion + item (item = lo despues del ultimo " - ")
RE_DESC_ITEM = re.compile(r'^\s*\{[^}]+\}\s*\[V\d+\]\s*(.+)$', re.I)

def parse_col(col_name):
    s = str(col_name)
    q_match = RE_Q.match(s)
    q_code = q_match.group(1) if q_match else None
    desc_match = RE_DESC_ITEM.match(s)
    full_desc = desc_match.group(1).strip() if desc_match else s.strip()
    # Separar descripcion y item (sufijo " - X" al final)
    if ' - ' in full_desc:
        parts = full_desc.rsplit(' - ', 1)
        base_desc = parts[0].strip()
        item_label = parts[1].strip()
    else:
        base_desc = full_desc
        item_label = None
    return q_code, base_desc, item_label

# Agrupar columnas por pregunta + item
groups = defaultdict(list)
for col in df.columns:
    q_code, base_desc, item_label = parse_col(col)
    if not q_code:
        continue
    groups[q_code].append({
        'col_name': str(col),
        'base_desc': base_desc,
        'item_label': item_label,
        'dtype': str(df[col].dtype),
        'n_valid': int(df[col].notna().sum()),
        'n_unique': int(df[col].nunique()),
    })

print(f"\nPreguntas detectadas: {len(groups)}\n")

def infer_type(q_code, cols):
    """Infiere tipo de pregunta segun estructura."""
    n_cols = len(cols)
    sample_col_name = cols[0]['col_name']
    sample_col = df[sample_col_name]
    sample_vals = sample_col.dropna().astype(str).head(50).tolist()
    sample_lower = [v.lower() for v in sample_vals]
    n_unique = sample_col.nunique()

    # Numerica
    if pd.api.types.is_numeric_dtype(sample_col):
        return 'numerica'

    # Escala 1-5 (P22, P38, P41 con valores "Muy importante" etc)
    escala_kws = ['muy importante', 'algo importante', 'poco importante', 'nada importante',
                  'muy de acuerdo', 'algo de acuerdo', 'totalmente',
                  'me agrada mucho', 'no me agrada']
    if any(any(kw in v for kw in escala_kws) for v in sample_lower):
        return 'escala_1_5'

    # Si tiene 1 sola columna
    if n_cols == 1:
        # Abierta si muchos unicos y strings largos
        avg_len = sum(len(v) for v in sample_vals[:20]) / max(1, len(sample_vals[:20]))
        if n_unique > 30 and avg_len > 30:
            return 'abierta'
        return 'single_select'

    # Si tiene multi cols pero los items son cadenas (P16, P17, P19, P20)
    # Valores probables: nombre de cadena o "Si"/"No" o flag binario
    items = [c['item_label'] for c in cols if c['item_label']]
    if items:
        # P22 escala: items son atributos (Limpieza, Calidad, etc.)
        # Pero el VALOR es escala_1_5 — ya manejado arriba
        # P23 asociacion: items son atributos, valor = cadena elegida
        # P26 misiones: items son misiones, valor = cadena elegida
        # P30 habito categorias: items son categorias, valor = cadena elegida
        # P32 mejor precio: items son categorias, valor = cadena elegida
        # P16/P17/P19/P20: items son cadenas, valor = cadena o Si/No
        return 'multi_select'

    return 'multi_select'

# Construir el map
map_data = {}
for q in sorted(groups.keys(), key=lambda x: (x[0:2], int(re.findall(r'\d+', x)[0]))):
    cols = groups[q]
    tipo = infer_type(q, cols)

    # Distribution preview: depende de tipo
    distribution = None
    if tipo == 'single_select':
        vc = df[cols[0]['col_name']].value_counts().head(15)
        distribution = {str(k)[:60]: int(v) for k, v in vc.items()}
    elif tipo == 'escala_1_5':
        # Buscar valores únicos de escala
        all_vals = set()
        for c in cols[:3]:
            all_vals.update(df[c['col_name']].dropna().astype(str).unique())
        distribution = {'escala_unique_values': sorted(list(all_vals))[:10]}
    elif tipo == 'multi_select':
        # Distribución de primera col + items list
        vc = df[cols[0]['col_name']].value_counts().head(10)
        distribution = {
            'sample_col_values': {str(k)[:50]: int(v) for k, v in vc.items()},
            'items': [c['item_label'] for c in cols if c['item_label']][:20],
        }
    elif tipo == 'numerica':
        s = df[cols[0]['col_name']].dropna()
        distribution = {
            'min': float(s.min()),
            'max': float(s.max()),
            'mean': float(s.mean()),
        }
    elif tipo == 'abierta':
        vc = df[cols[0]['col_name']].value_counts().head(10)
        distribution = {'top_responses_textuales': {str(k)[:80]: int(v) for k, v in vc.items()}}

    # Base description (la primera col, sin sufijo item)
    base_desc = cols[0]['base_desc'] if cols else ''

    map_data[q] = {
        'question_code': q,
        'tipo': tipo,
        'n_cols': len(cols),
        'base_description': base_desc,
        'cols': cols,
        'distribution_preview': distribution,
    }

# Summary
print(f"Total preguntas: {len(map_data)}")
print("\nTipos:")
tipos_count = defaultdict(int)
for q, m in map_data.items():
    tipos_count[m['tipo']] += 1
for t, n in sorted(tipos_count.items()):
    print(f"  {t}: {n}")

print(f"\n{'='*80}")
print("MAPA DE PREGUNTAS")
print('='*80)
for q in sorted(map_data.keys(), key=lambda x: (x[0:2], int(re.findall(r'\d+', x)[0]))):
    m = map_data[q]
    print(f"\n{q} ({m['tipo']}, {m['n_cols']} col{'s' if m['n_cols']>1 else ''})")
    print(f"  Desc: {m['base_description'][:80]}")
    if m['tipo'] == 'multi_select':
        items_preview = [c['item_label'] for c in m['cols'] if c['item_label']][:8]
        print(f"  Items: {items_preview}")
    elif m['tipo'] == 'single_select':
        print(f"  Dist: {list(m['distribution_preview'].items())[:5]}")

# Export
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(map_data, f, ensure_ascii=False, indent=2, default=str)
print(f"\nExportado: {OUT}")
