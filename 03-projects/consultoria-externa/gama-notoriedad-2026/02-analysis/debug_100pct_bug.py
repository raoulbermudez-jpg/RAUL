"""Debug: investiga por qué las tablas muestran 100% por todas partes."""
import sys, json
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open(r'C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis\all_tables.json', encoding='utf-8'))

# Casos a inspeccionar
CASES = [
    ('P21', 'NSE'),       # single_select básico — Marca preferida x NSE
    ('P22', 'NSE'),       # escala_1_5
    ('P16', 'NSE'),       # multi_select cadenas (TOM)
    ('P30', 'NSE'),       # multi_select categorías
    ('P33', 'NSE'),       # single_select escala caro/económico
    ('PF5', 'NSE'),       # single género x NSE
]

for q_code, bk in CASES:
    print(f"\n{'='*80}")
    print(f"  {q_code} x {bk}")
    print('='*80)
    if q_code not in data:
        print(f"  NO existe pregunta {q_code}")
        continue
    q = data[q_code]
    if bk not in q['tables_by_bk']:
        print(f"  NO existe BK {bk}")
        continue
    table = q['tables_by_bk'][bk]
    print(f"  Tipo: {q['tipo']}")
    print(f"  Base total: {table['base_total']}")
    print(f"  BK levels y bases: {table['base_bk_levels']}")
    print(f"  Rows (primeras 5):")
    for row in table['rows'][:5]:
        cells_str = ' | '.join(f"{c['level']}: {c['pct']}% n={c['n']}" for c in row['bk_cells'])
        print(f"    {row['category'][:40]:42s}  Total: {row['total']['pct']}% n={row['total']['n']}  |  {cells_str}")
