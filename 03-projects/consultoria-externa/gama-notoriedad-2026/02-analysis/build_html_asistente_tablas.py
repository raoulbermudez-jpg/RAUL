"""Fase 4: HTML interactivo standalone - Asistente de Tablas Notoriedad Gama 2026.

Genera un HTML self-contained con:
- Sidebar: 42 preguntas agrupadas por sección
- Dropdown BK: 6 break-downs (NSE / Género / Edad / Municipio / Marca preferida / Misión)
- Main: tabla cruzada con N + % + letras SPSS sig + colores
- Botón export Excel maestro (42 hojas, una por pregunta, con las 6 tablas BK lado a lado)
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import json
import os

ALL_TABLES_JSON = r"C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis\all_tables.json"
OUT_HTML = r"C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\03-deck\V8\2026-05-18_Notoriedad-Gama-2026_V8_Asistente-Tablas.html"

with open(ALL_TABLES_JSON, encoding='utf-8') as f:
    data = json.load(f)

questions = {k: v for k, v in data.items() if not k.startswith('_')}
meta = data.get('_meta', {})

# ===== Agrupación por sección (DINAMICA — matchea prefijos) =====
SECTION_PREFIXES = {
    'Perfil del entrevistado': ['PF2', 'PF5', 'PF7', 'PF8', 'PF9', 'PF10', 'PD4'],
    'Embudo de marca': ['P16', 'P17', 'P19', 'P20', 'P21', 'P21.1', 'P24'],
    'Atributos: importancia y asociación': ['P22', 'P23'],
    'Misiones de compra (P26 desglosado por misión)': ['P25', 'P26'],
    'Hábitos por categoría (P30 desglosado por categoría)': ['P30'],
    'Precio (P32 desglosado por categoría)': ['P31', 'P32', 'P33', 'P34'],
    'Recall publicitario': ['P35', 'P36', 'P37', 'P38', 'P39', 'P40', 'P41', 'P42'],
    'Post-ola': ['P44', 'P45'],
}

def matches_prefix(q_code, prefix):
    """Matchea exacta o como prefijo de sub-pregunta (P30 matchea P30:1, P30:2...)."""
    return q_code == prefix or q_code.startswith(prefix + ':') or q_code.startswith(prefix + '.')

# Construir SECTIONS dinámicamente
import re as _re
def sort_key(q):
    """Ordena por prefijo alfa + número."""
    m = _re.match(r'^(P[FD]?\d+)([.:]?\d*)$', q)
    if m:
        base = m.group(1)
        sub = m.group(2)
        sub_num = int(_re.sub(r'[^\d]', '', sub) or 0) if sub else 0
        base_num = int(_re.findall(r'\d+', base)[0])
        return (base[0:2], base_num, sub_num)
    return ('Z', 0, 0)

SECTIONS = {}
for section_name, prefixes in SECTION_PREFIXES.items():
    matching_qs = []
    for q_code in questions.keys():
        for p in prefixes:
            if matches_prefix(q_code, p):
                matching_qs.append(q_code)
                break
    matching_qs.sort(key=sort_key)
    if matching_qs:
        SECTIONS[section_name] = matching_qs

# Labels más legibles para preguntas
P23_LABELS = {
    'P23:1': 'P23.1 — Mayor cantidad de categorías',
    'P23:2': 'P23.2 — Mayor calidad de productos',
    'P23:3': 'P23.3 — Atención al cliente',
    'P23:4': 'P23.4 — Precios accesibles',
    'P23:5': 'P23.5 — Ofertas/promociones',
    'P23:6': 'P23.6 — Tienda atractiva',
    'P23:8': 'P23.8 — Limpieza/orden',
    'P23:12': 'P23.12 — Seguridad',
    'P23:13': 'P23.13 — Rapidez en caja',
    'P23:21': 'P23.21 — Valer el dinero',
}

def get_label(q_code, q_data):
    if q_code in P23_LABELS:
        return P23_LABELS[q_code]
    desc = q_data.get('base_description', '')[:90]
    # Si es sub-pregunta (P30:1, P26:1, etc.) usar la desc que ya incluye el item
    if ':' in q_code and q_data.get('parent_question'):
        return f"{q_code} — {desc}"
    return f"{q_code} — {desc}" if desc else q_code

# ===== Generar HTML =====
sections_html = ""
for section_name, q_codes in SECTIONS.items():
    valid_qs = [q for q in q_codes if q in questions]
    if not valid_qs:
        continue
    sections_html += f'<div class="section"><div class="section-title">{section_name}</div>'
    for q_code in valid_qs:
        label = get_label(q_code, questions[q_code])
        sections_html += f'  <div class="q-item" data-q="{q_code}">{label}</div>\n'
    sections_html += '</div>\n'

# JSON embebido
data_json = json.dumps(data, ensure_ascii=False, separators=(',', ':'))

html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Asistente de Tablas — Notoriedad Gama 2026</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 14px;
    color: #1a1a1a;
    background: #f4f4f4;
    height: 100vh;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }}
  header {{
    background: #E30613;
    color: white;
    padding: 12px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }}
  header h1 {{ font-size: 18px; font-weight: 600; }}
  header .meta {{ font-size: 12px; opacity: 0.9; }}
  .toolbar {{
    background: white;
    padding: 10px 20px;
    border-bottom: 1px solid #e5e5e5;
    display: flex;
    align-items: center;
    gap: 16px;
  }}
  .toolbar label {{ font-weight: 600; font-size: 13px; }}
  .toolbar select {{
    padding: 6px 10px;
    border: 1px solid #d0d0d0;
    border-radius: 4px;
    font-size: 13px;
    background: white;
    cursor: pointer;
  }}
  .toolbar button {{
    margin-left: auto;
    padding: 7px 14px;
    background: #2D8F47;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
  }}
  .toolbar button:hover {{ background: #246e38; }}
  .main-container {{
    display: flex;
    flex: 1;
    overflow: hidden;
  }}
  .sidebar {{
    width: 320px;
    background: white;
    border-right: 1px solid #e5e5e5;
    overflow-y: auto;
    padding: 12px 0;
  }}
  .section {{ margin-bottom: 12px; }}
  .section-title {{
    font-size: 11px;
    font-weight: 700;
    color: #6b6b6b;
    padding: 6px 16px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-bottom: 1px solid #f0f0f0;
    margin-bottom: 4px;
  }}
  .q-item {{
    padding: 7px 16px;
    font-size: 12px;
    color: #333;
    cursor: pointer;
    border-left: 3px solid transparent;
    line-height: 1.35;
  }}
  .q-item:hover {{ background: #f8f8f8; border-left-color: #d0d0d0; }}
  .q-item.active {{
    background: #ffe9eb;
    border-left-color: #E30613;
    font-weight: 600;
  }}
  .content {{
    flex: 1;
    overflow: auto;
    padding: 20px 28px;
  }}
  .placeholder {{
    color: #6b6b6b;
    font-style: italic;
    padding: 40px 20px;
    text-align: center;
  }}
  .q-header {{
    margin-bottom: 16px;
  }}
  .q-header h2 {{
    font-size: 18px;
    color: #1a1a1a;
    margin-bottom: 6px;
  }}
  .q-header .q-meta {{
    font-size: 12px;
    color: #6b6b6b;
  }}
  table {{
    border-collapse: collapse;
    width: 100%;
    background: white;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    margin-bottom: 16px;
  }}
  th {{
    background: #1a1a1a;
    color: white;
    padding: 8px 10px;
    text-align: center;
    font-size: 12px;
    font-weight: 600;
    border-right: 1px solid #333;
  }}
  th.col-letter {{
    background: #6b6b6b;
    font-size: 11px;
    padding: 4px 10px;
    font-weight: 500;
    color: #f4f4f4;
  }}
  th:first-child {{ text-align: left; padding-left: 14px; }}
  td {{
    padding: 7px 10px;
    text-align: center;
    border-bottom: 1px solid #f0f0f0;
    border-right: 1px solid #f0f0f0;
    font-size: 12px;
    line-height: 1.3;
  }}
  td.row-label {{
    text-align: left;
    padding-left: 14px;
    font-weight: 500;
    background: #fafafa;
    max-width: 280px;
    word-wrap: break-word;
  }}
  td.total-col {{
    background: #f4f4f4;
    font-weight: 600;
  }}
  td.cell-pos {{ background: #e8f5ec; }}
  td.cell-neg {{ background: #ffe9eb; }}
  td.cell-neutral {{ }}
  td .sig-letters {{
    font-size: 10px;
    color: #555;
    vertical-align: super;
    margin-left: 2px;
    font-weight: 700;
  }}
  td .n-value {{
    display: block;
    font-size: 10px;
    color: #6b6b6b;
    margin-top: 2px;
  }}
  .table-footer {{
    font-size: 11px;
    color: #6b6b6b;
    margin-top: 8px;
    line-height: 1.5;
    padding: 10px 14px;
    background: #fafafa;
    border-left: 3px solid #d0d0d0;
  }}
  .legend {{
    margin-top: 20px;
    padding: 12px 14px;
    background: white;
    border: 1px solid #e5e5e5;
    border-radius: 4px;
    font-size: 12px;
    color: #333;
  }}
  .legend-item {{ display: inline-block; margin-right: 16px; }}
  .legend-swatch {{
    display: inline-block;
    width: 14px;
    height: 14px;
    vertical-align: middle;
    margin-right: 4px;
    border-radius: 2px;
    border: 1px solid #d0d0d0;
  }}
</style>
</head>
<body>
<header>
  <h1>Asistente de Tablas — Notoriedad Gama 2026</h1>
  <span class="meta">n = {meta.get('n_total', 402)} · BBDD 2026 · α = {meta.get('alpha', 0.05)}</span>
</header>
<div class="toolbar">
  <label>Break-down:</label>
  <select id="bk-select">
    <option value="NSE">NSE</option>
    <option value="Genero">Género</option>
    <option value="Edad">Edad (grupos)</option>
    <option value="Municipio">Municipio</option>
    <option value="Marca preferida">Marca preferida (Top 8 + Otros)</option>
    <option value="Mision">Misión de compra (P25)</option>
  </select>
  <span id="current-question" style="font-size:12px;color:#6b6b6b;font-style:italic;">Selecciona una pregunta del menú →</span>
  <button onclick="exportToExcel()">📥 Descargar TODAS las tablas (Excel)</button>
</div>
<div class="main-container">
  <div class="sidebar">
    {sections_html}
  </div>
  <div class="content" id="content">
    <div class="placeholder">
      <p>👈 Selecciona una pregunta del menú lateral para ver su tabla cruzada.</p>
      <p style="margin-top:8px; font-size:13px;">42 preguntas disponibles, 6 break-downs cada una = 252 tablas pre-computadas.</p>
    </div>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js"></script>
<script>
const DATA = {data_json};

const sidebarItems = document.querySelectorAll('.q-item');
const bkSelect = document.getElementById('bk-select');
const content = document.getElementById('content');
const currentQ = document.getElementById('current-question');

let selectedQ = null;

sidebarItems.forEach(item => {{
  item.addEventListener('click', () => {{
    sidebarItems.forEach(i => i.classList.remove('active'));
    item.classList.add('active');
    selectedQ = item.dataset.q;
    renderTable();
  }});
}});

bkSelect.addEventListener('change', renderTable);

function renderTable() {{
  if (!selectedQ) return;
  const q = DATA[selectedQ];
  if (!q) {{
    content.innerHTML = '<div class="placeholder">Pregunta no disponible.</div>';
    return;
  }}
  const bk = bkSelect.value;
  const table = q.tables_by_bk[bk];
  if (!table) {{
    content.innerHTML = '<div class="placeholder">No hay tabla para este cruce.</div>';
    return;
  }}
  currentQ.textContent = `${{selectedQ}} — ${{q.base_description.substring(0, 70)}}`;

  const letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'];
  const bkLevels = table.bk_levels;
  const basesBK = table.base_bk_levels;

  let html = `
    <div class="q-header">
      <h2>${{selectedQ}} — ${{q.base_description.substring(0, 100)}}</h2>
      <div class="q-meta">Tipo: ${{q.tipo}} · Cruce: ${{bk}} · Base total: n=${{table.base_total}}</div>
    </div>
    <table>
      <thead>
        <tr>
          <th>${{q.tipo === 'multi_select' ? 'Ítem' : (q.tipo === 'escala_1_5' ? 'Atributo' : 'Categoría')}}</th>
          <th>Total<br><span style="font-size:10px;font-weight:400;opacity:0.8;">n=${{table.base_total}}</span></th>
  `;
  bkLevels.forEach((lvl, i) => {{
    html += `<th>${{lvl}}<br><span style="font-size:10px;font-weight:400;opacity:0.8;">n=${{basesBK[lvl]}}</span></th>`;
  }});
  html += `</tr>
        <tr>
          <th class="col-letter"></th>
          <th class="col-letter">—</th>
  `;
  bkLevels.forEach((lvl, i) => {{
    html += `<th class="col-letter">(${{letters[i]}})</th>`;
  }});
  html += `</tr>
      </thead>
      <tbody>
  `;

  table.rows.forEach(row => {{
    html += `<tr>`;
    html += `<td class="row-label">${{row.category}}</td>`;
    html += `<td class="total-col">${{row.total.pct}}${{q.tipo==='numerica'?'':'%'}}<span class="n-value">n=${{row.total.n}}</span></td>`;
    row.bk_cells.forEach(cell => {{
      const colorClass = cell.color === 'pos' ? 'cell-pos' : (cell.color === 'neg' ? 'cell-neg' : 'cell-neutral');
      const sig = cell.sig_letters ? `<span class="sig-letters">${{cell.sig_letters}}</span>` : '';
      html += `<td class="${{colorClass}}">${{cell.pct}}${{q.tipo==='numerica'?'':'%'}}${{sig}}<span class="n-value">n=${{cell.n}}</span></td>`;
    }});
    html += `</tr>`;
  }});

  html += `</tbody></table>`;

  if (table.note) {{
    html += `<div class="table-footer">📌 ${{table.note}}</div>`;
  }}

  html += `<div class="legend">
    <strong>Cómo leer:</strong> &nbsp;
    <span class="legend-item"><span class="legend-swatch" style="background:#e8f5ec"></span> Sig. <strong>mayor</strong> al Total (α=0.05)</span>
    <span class="legend-item"><span class="legend-swatch" style="background:#ffe9eb"></span> Sig. <strong>menor</strong> al Total</span>
    <span class="legend-item"><strong>ᴬᴮᶜ</strong> = celda sig. mayor a columnas A/B/C (estilo SPSS/Wincross)</span>
  </div>`;

  content.innerHTML = html;
}}

function exportToExcel() {{
  const wb = XLSX.utils.book_new();
  const qCodes = Object.keys(DATA).filter(k => !k.startsWith('_'));

  qCodes.forEach(qCode => {{
    const q = DATA[qCode];
    if (!q.tables_by_bk) return;
    const rows = [];
    rows.push([`Pregunta: ${{qCode}} — ${{q.base_description}}`]);
    rows.push([`Tipo: ${{q.tipo}}`]);
    rows.push([]);
    // Para cada BK, agregar tabla
    Object.entries(q.tables_by_bk).forEach(([bkName, table]) => {{
      rows.push([`Break-down: ${{bkName}} (base total n=${{table.base_total}})`]);
      const header = ['Categoría', `Total (n=${{table.base_total}})`];
      table.bk_levels.forEach(lvl => header.push(`${{lvl}} (n=${{table.base_bk_levels[lvl]}})`));
      rows.push(header);
      table.rows.forEach(row => {{
        const r = [row.category, `${{row.total.pct}}% (n=${{row.total.n}})`];
        row.bk_cells.forEach(cell => {{
          r.push(`${{cell.pct}}%${{cell.sig_letters ? ' [' + cell.sig_letters + ']' : ''}} (n=${{cell.n}})`);
        }});
        rows.push(r);
      }});
      rows.push([]);
    }});
    const ws = XLSX.utils.aoa_to_sheet(rows);
    // Limitar nombre hoja a 31 chars (Excel limit)
    const sheetName = qCode.substring(0, 31);
    XLSX.utils.book_append_sheet(wb, ws, sheetName);
  }});

  XLSX.writeFile(wb, 'Notoriedad-Gama-2026_Tablas-completas.xlsx');
}}
</script>
</body>
</html>
"""

with open(OUT_HTML, 'w', encoding='utf-8') as f:
    f.write(html)

size_mb = os.path.getsize(OUT_HTML) / 1024 / 1024
total_tables = sum(len(q.get('tables_by_bk', {})) for q in questions.values())
print(f"HTML generado: {OUT_HTML}")
print(f"Tamaño: {size_mb:.2f} MB")
print(f"Preguntas (incluye sub-preguntas pivot): {len(questions)}")
print(f"BKs: 6")
print(f"Tablas embebidas totales: {total_tables}")
print(f"Secciones en sidebar: {len(SECTIONS)}")
for sec, qs in SECTIONS.items():
    print(f"  {sec}: {len(qs)} preguntas")
