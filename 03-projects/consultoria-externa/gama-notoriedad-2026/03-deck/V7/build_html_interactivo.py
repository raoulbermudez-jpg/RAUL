"""HTML interactivo simple — Notoriedad Gama 2026 V7
Extrae BBDD 2026 a JSON, embebe en HTML standalone con JS vanilla.
Variables de cruce: NSE (con C+/C agrupado), Género, Edad, Marca preferida, Municipio.
Métricas: TOM Gama, Consideración, Preferida, Compra 3m, Habitual, Percepción precio.
Sin librerías externas — funciona offline.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

import os
import json
import pandas as pd

BBDD = r"G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\BBDD Notoriedad 2026.xlsx"
OUT_HTML = r"C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\03-deck\V7\2026-05-18_Notoriedad-Gama-2026_V7_Tabla-Interactiva.html"

print("Cargando BBDD 2026...")
df = pd.read_excel(BBDD)
print(f"  n={len(df)} filas, {len(df.columns)} columnas")

# Identificar columnas relevantes por nombre fuzzy (la BBDD tiene nombres largos)
def find_col(df, *keywords):
    """Encuentra columna que contenga TODOS los keywords (case insensitive)."""
    for col in df.columns:
        col_lower = str(col).lower()
        if all(k.lower() in col_lower for k in keywords):
            return col
    return None

# Variables de cruce — usar regex estricta para NSE (buscar literal \bNSE\b o PD4)
import re
def find_col_strict(df, *patterns):
    """Encuentra columna con literal NSE (word boundary) o PD4."""
    for col in df.columns:
        s = str(col)
        for p in patterns:
            if re.search(r'\b' + p + r'\b', s, re.I):
                return col
    return None
col_nse = find_col_strict(df, 'PD4', 'NSE')
col_genero = find_col(df, 'genero') or find_col(df, 'género') or find_col(df, 'sexo')
col_edad = find_col(df, 'edad') or find_col(df, 'pf7') or find_col(df, 'grupo', 'edad')
col_pref = find_col(df, 'P21', 'preferido') or find_col(df, 'p21', 'cuál es su preferido')
col_muni = find_col(df, 'municipio') or find_col(df, 'PF2')

# Variables métricas
col_tom = find_col(df, 'P16') or find_col(df, 'top', 'mind') or find_col(df, 'p16')
col_consid = find_col(df, 'P19') or find_col(df, 'consider')
col_compra = find_col(df, 'P20') or find_col(df, 'compra', '3 meses')
col_habit = find_col(df, 'P30') or find_col(df, 'habitual')
col_p33 = find_col(df, 'P33') or find_col(df, 'precios', 'gama')

print("\nColumnas detectadas:")
for name, col in [('NSE', col_nse), ('Género', col_genero), ('Edad', col_edad),
                   ('Preferido', col_pref), ('Municipio', col_muni),
                   ('TOM', col_tom), ('Consideración', col_consid),
                   ('Compra 3m', col_compra), ('Habitual', col_habit), ('P33 precio', col_p33)]:
    print(f"  {name}: {col[:60] if col else 'NO ENCONTRADA'}...")

# Subset de columnas que sí encontramos
cols_keep = {
    'nse_raw': col_nse,
    'genero': col_genero,
    'edad': col_edad,
    'pref': col_pref,
    'muni': col_muni,
    'p33_raw': col_p33,
}
cols_keep = {k: v for k, v in cols_keep.items() if v is not None}

df_clean = df[list(cols_keep.values())].copy()
df_clean.columns = list(cols_keep.keys())

# Normalizar NSE: C+/C combinado como "clase media"
def norm_nse(x):
    if pd.isna(x):
        return 'NS/NC'
    s = str(x).strip().upper().replace(' ', '')
    if s in ('C+/C', 'C+', 'C'):
        return 'C+/C (clase media)'
    if s == 'D':
        return 'D'
    if s == 'E':
        return 'E'
    return s

if 'nse_raw' in df_clean.columns:
    df_clean['nse'] = df_clean['nse_raw'].apply(norm_nse)
    df_clean = df_clean.drop(columns=['nse_raw'])

# Normalizar P33 percepción precio
def norm_p33(x):
    if pd.isna(x):
        return 'NS/NC'
    s = str(x).strip().lower()
    if 'mucho' in s and ('econ' in s or 'baj' in s):
        return 'Mucho más económico'
    if 'poco' in s and ('econ' in s or 'baj' in s):
        return 'Poco más económico'
    if 'igual' in s:
        return 'Igual'
    if 'poco' in s and ('car' in s or 'alt' in s):
        return 'Poco más caro'
    if 'mucho' in s and ('car' in s or 'alt' in s):
        return 'Mucho más caro'
    return 'NS/NC'

if 'p33_raw' in df_clean.columns:
    df_clean['p33'] = df_clean['p33_raw'].apply(norm_p33)
    df_clean = df_clean.drop(columns=['p33_raw'])

# Normalizar marca preferida (extraer nombre limpio)
def norm_marca(x):
    if pd.isna(x):
        return 'NS/NC'
    s = str(x).strip()
    # Mapeos comunes
    mapping = {
        'gama': 'Gama',
        'excels': 'Gama',
        'paramo': 'Páramo',
        'páramo': 'Páramo',
        'rio': 'Rio',
        'río': 'Rio',
        'central mad': 'Central Madeirense',
        'madeirense': 'Central Madeirense',
        'plan suarez': 'Plan Suárez',
        'plan suárez': 'Plan Suárez',
        'forum': 'Forum',
        'plazas': 'Plazas',
        'luz': 'Luz',
        'hiper': 'Hiper Líder',
        'muralla': 'La Muralla',
        'granja': 'La Granja',
    }
    s_lower = s.lower()
    for k, v in mapping.items():
        if k in s_lower:
            return v
    return s.title()[:30]

if 'pref' in df_clean.columns:
    df_clean['pref_marca'] = df_clean['pref'].apply(norm_marca)
    df_clean = df_clean.drop(columns=['pref'])

# Variables de TOM/Consideración/Compra/Habitual: en la BBDD pueden estar como columnas multi-mention.
# Para HTML simple, sólo necesitamos flag binario "menciona Gama" para cada métrica.
# Heurística: si la columna existe, marcar "Gama" si aparece en la respuesta.
def flag_gama(row, col_name):
    val = row.get(col_name)
    if pd.isna(val):
        return 0
    s = str(val).lower()
    return 1 if ('gama' in s or 'excels' in s) else 0

for var_name, src_col in [('tom_gama', col_tom), ('consid_gama', col_consid),
                          ('compra_gama', col_compra), ('habit_gama', col_habit)]:
    if src_col:
        df_clean[var_name] = df[src_col].apply(lambda v: 1 if pd.notna(v) and ('gama' in str(v).lower() or 'excels' in str(v).lower()) else 0)

# Normalizar género
def norm_genero(x):
    if pd.isna(x):
        return 'NS/NC'
    s = str(x).strip().lower()
    if 'fem' in s or 'm' == s.strip() == 'm' or 'mujer' in s:
        return 'Femenino'
    if 'mas' in s or 'h' == s.strip() or 'hombre' in s:
        return 'Masculino'
    if s in ('1', '2'):
        return 'Femenino' if s == '2' else 'Masculino'
    return s.title()

if 'genero' in df_clean.columns:
    df_clean['genero'] = df_clean['genero'].apply(norm_genero)

# Normalizar edad — la BBDD tiene PD2 sin codificar (descubierto en CU-8 v2)
# Usar PF7 grupo de edad si existe
def norm_edad(x):
    if pd.isna(x):
        return 'NS/NC'
    s = str(x).strip()
    # Mapeo basado en valores reales BBDD: "18 a 24 años", "25 a 34 años", etc.
    if '18' in s and '24' in s: return '18-24'
    if '25' in s and '34' in s: return '25-34'
    if '35' in s and '44' in s: return '35-44'
    if '45' in s and '54' in s: return '45-54'
    if '55' in s and '64' in s: return '55-64'
    if '65' in s or '+' in s: return '65+'
    return s[:20]

if 'edad' in df_clean.columns:
    df_clean['edad_grupo'] = df_clean['edad'].apply(norm_edad)
    df_clean = df_clean.drop(columns=['edad'])

# Normalizar municipio
def norm_muni(x):
    if pd.isna(x):
        return 'NS/NC'
    s = str(x).strip()
    mapping = {
        'baruta': 'Baruta',
        'libertador': 'Libertador',
        'sucre': 'Sucre',
        'chacao': 'Chacao',
        'hatillo': 'El Hatillo',
        'mirandinos': 'Altos Mirandinos',
    }
    s_lower = s.lower()
    for k, v in mapping.items():
        if k in s_lower:
            return v
    return s[:25]

if 'muni' in df_clean.columns:
    df_clean['municipio'] = df_clean['muni'].apply(norm_muni)
    df_clean = df_clean.drop(columns=['muni'])

print(f"\nDataset limpio: {len(df_clean)} filas x {len(df_clean.columns)} columnas")
print(df_clean.head(3))

# Exportar a JSON-lite (solo las columnas necesarias)
records = df_clean.to_dict('records')
data_json = json.dumps(records, ensure_ascii=False, default=str)

print(f"\nTamaño JSON: {len(data_json):,} chars")

# Generar HTML
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Notoriedad Gama 2026 — Tabla Interactiva V7</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: Calibri, Arial, sans-serif; background: #f7f7f7; color: #333; padding: 24px; }
  h1 { color: #7A1212; font-size: 22px; margin-bottom: 4px; }
  .subtitle { color: #666; font-size: 12px; margin-bottom: 20px; font-style: italic; }
  .controls {
    background: white; padding: 16px; border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 20px;
    display: flex; gap: 16px; flex-wrap: wrap; align-items: flex-end;
  }
  .control-group { display: flex; flex-direction: column; gap: 4px; }
  .control-group label { font-size: 11px; color: #555; font-weight: bold; text-transform: uppercase; }
  .control-group select {
    padding: 6px 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 13px;
    background: white; cursor: pointer; min-width: 180px;
  }
  .control-group select:hover { border-color: #7A1212; }
  .btn-reset {
    padding: 8px 16px; background: #7A1212; color: white; border: none; border-radius: 4px;
    cursor: pointer; font-size: 12px; font-weight: bold;
  }
  .btn-reset:hover { background: #4A0A0A; }
  .summary {
    background: #f0eaea; padding: 10px 16px; border-left: 4px solid #7A1212; margin-bottom: 16px;
    font-size: 13px;
  }
  table {
    width: 100%; background: white; border-collapse: collapse;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05); border-radius: 8px; overflow: hidden;
  }
  th { background: #7A1212; color: white; padding: 10px 14px; text-align: center; font-size: 12px; }
  th:first-child { text-align: left; }
  td { padding: 8px 14px; border-bottom: 1px solid #eee; font-size: 12px; text-align: center; }
  td:first-child { text-align: left; font-weight: bold; color: #555; }
  tr:nth-child(even) { background: #fafafa; }
  tr:hover { background: #fff3e0; }
  .footer { color: #888; font-size: 10px; margin-top: 20px; text-align: center; font-style: italic; }
  .nota { background: #fff3e0; padding: 10px 16px; border-left: 4px solid #D97306; margin-top: 16px; font-size: 11px; color: #D97306; }
  .metric-positive { color: #1A702A; font-weight: bold; }
  .base-low { color: #D97306; font-style: italic; }
</style>
</head>
<body>
<h1>Notoriedad y Preferencia de Marca — Gama 2026 · V7 Tabla Interactiva</h1>
<div class="subtitle">Explore los datos con cruces dinámicos. Base muestral: n=402. C+/C combinado como "clase media". Fecha: 2026-05-18.</div>

<div class="controls">
  <div class="control-group">
    <label>Métrica a mostrar</label>
    <select id="metric">
      <option value="tom_gama">% TOM Gama (Top of Mind)</option>
      <option value="consid_gama">% Consideración Gama</option>
      <option value="compra_gama">% Compra Gama (últimos 3m)</option>
      <option value="habit_gama">% Habitual Gama</option>
      <option value="pref_gama">% Preferencia Gama</option>
      <option value="p33_caro">% Percibe Gama CARO (NETO)</option>
      <option value="p33_economico">% Percibe Gama ECONÓMICO (NETO)</option>
    </select>
  </div>
  <div class="control-group">
    <label>Variable de cruce</label>
    <select id="cross">
      <option value="nse">NSE (clase social)</option>
      <option value="genero">Género</option>
      <option value="edad_grupo">Edad (grupo)</option>
      <option value="pref_marca">Marca preferida</option>
      <option value="municipio">Municipio</option>
    </select>
  </div>
  <div class="control-group">
    <label>Filtro adicional NSE</label>
    <select id="filter_nse">
      <option value="">— Sin filtro —</option>
      <option value="C+/C (clase media)">Solo C+/C (clase media)</option>
      <option value="D">Solo D</option>
      <option value="E">Solo E</option>
    </select>
  </div>
  <div class="control-group">
    <label>Filtro adicional Género</label>
    <select id="filter_genero">
      <option value="">— Sin filtro —</option>
      <option value="Femenino">Solo Femenino</option>
      <option value="Masculino">Solo Masculino</option>
    </select>
  </div>
  <button class="btn-reset" onclick="reset()">Resetear filtros</button>
</div>

<div class="summary" id="summary">Cargando datos...</div>
<div id="table_container"></div>
<div class="nota">
  Nota: las celdas con base n&lt;30 se marcan como REFERENCIAL — interpretar como tendencia, no como dato proyectable.
  Pref-Gama (n=32 total) es REFERENCIAL en todos los cruces.
</div>

<div class="footer">
  Notoriedad Gama 2026 · V7 · Tabla Interactiva · Datos al 2026-05-18 · Confidencial NDA<br>
  Producido por equipo Raoul Bermúdez + Cora Urrea
</div>

<script>
const DATA = __DATA_JSON__;

function calcMetric(row, metric) {
  if (metric === 'tom_gama') return row.tom_gama || 0;
  if (metric === 'consid_gama') return row.consid_gama || 0;
  if (metric === 'compra_gama') return row.compra_gama || 0;
  if (metric === 'habit_gama') return row.habit_gama || 0;
  if (metric === 'pref_gama') return (row.pref_marca === 'Gama') ? 1 : 0;
  if (metric === 'p33_caro') {
    return (row.p33 === 'Poco más caro' || row.p33 === 'Mucho más caro') ? 1 : 0;
  }
  if (metric === 'p33_economico') {
    return (row.p33 === 'Poco más económico' || row.p33 === 'Mucho más económico') ? 1 : 0;
  }
  return 0;
}

function metricLabel(metric) {
  return document.getElementById('metric').options[document.getElementById('metric').selectedIndex].text;
}

function render() {
  const metric = document.getElementById('metric').value;
  const cross = document.getElementById('cross').value;
  const fNse = document.getElementById('filter_nse').value;
  const fGen = document.getElementById('filter_genero').value;

  // Filter
  let filtered = DATA.filter(r => {
    if (fNse && r.nse !== fNse) return false;
    if (fGen && r.genero !== fGen) return false;
    return true;
  });

  // Group by cross
  const groups = {};
  filtered.forEach(r => {
    const k = r[cross] || 'NS/NC';
    if (!groups[k]) groups[k] = { n: 0, metric_sum: 0 };
    groups[k].n += 1;
    groups[k].metric_sum += calcMetric(r, metric);
  });

  // Sort by % desc (puts most relevant on top)
  const rows = Object.entries(groups)
    .map(([k, v]) => ({ label: k, n: v.n, pct: v.n > 0 ? (v.metric_sum / v.n * 100) : 0 }))
    .filter(x => x.label !== 'NS/NC' || x.n > 0)
    .sort((a, b) => b.pct - a.pct);

  // Total
  const total_n = filtered.length;
  const total_sum = filtered.reduce((s, r) => s + calcMetric(r, metric), 0);
  const total_pct = total_n > 0 ? (total_sum / total_n * 100) : 0;

  // Update summary
  let summaryHtml = `<b>Base seleccionada: n=${total_n}</b>`;
  if (fNse) summaryHtml += ` · NSE=${fNse}`;
  if (fGen) summaryHtml += ` · Género=${fGen}`;
  summaryHtml += ` · ${metricLabel(metric)} total: <b>${total_pct.toFixed(1)}%</b>`;
  document.getElementById('summary').innerHTML = summaryHtml;

  // Build table
  let html = '<table>';
  html += `<tr><th>${crossLabel(cross)}</th><th>n</th><th>${metricLabel(metric)}</th><th>Flag</th></tr>`;
  rows.forEach(r => {
    const flag = r.n < 30 ? '<span class="base-low">REFERENCIAL</span>' : 'OK';
    const pctClass = r.pct > total_pct ? 'metric-positive' : '';
    html += `<tr><td>${r.label}</td><td>${r.n}</td><td class="${pctClass}">${r.pct.toFixed(1)}%</td><td>${flag}</td></tr>`;
  });
  html += `<tr style="background:#f0eaea;font-weight:bold;"><td>TOTAL</td><td>${total_n}</td><td>${total_pct.toFixed(1)}%</td><td>${total_n < 30 ? 'REF.' : 'OK'}</td></tr>`;
  html += '</table>';
  document.getElementById('table_container').innerHTML = html;
}

function crossLabel(c) {
  return document.getElementById('cross').options[document.getElementById('cross').selectedIndex].text;
}

function reset() {
  document.getElementById('metric').value = 'tom_gama';
  document.getElementById('cross').value = 'nse';
  document.getElementById('filter_nse').value = '';
  document.getElementById('filter_genero').value = '';
  render();
}

document.getElementById('metric').addEventListener('change', render);
document.getElementById('cross').addEventListener('change', render);
document.getElementById('filter_nse').addEventListener('change', render);
document.getElementById('filter_genero').addEventListener('change', render);

render();
</script>
</body>
</html>
"""

html_final = HTML_TEMPLATE.replace('__DATA_JSON__', data_json)

with open(OUT_HTML, 'w', encoding='utf-8') as f:
    f.write(html_final)

print(f"\nHTML interactivo generado: {OUT_HTML}")
print(f"Tamaño: {os.path.getsize(OUT_HTML):,} bytes")
