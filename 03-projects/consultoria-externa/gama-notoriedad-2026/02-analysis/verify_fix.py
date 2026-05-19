"""Verifica fix: ahora las tablas multi_select NO dan 100% donde no deberían."""
import sys, json
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open(r'C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis\all_tables.json', encoding='utf-8'))

print("="*80)
print("VERIFICACION POST-FIX")
print("="*80)

CASES = [
    ('P16', 'NSE', 'multi_select_flags', 'TOM cadenas — debería ser ~40-60% por cadena'),
    ('P19', 'NSE', 'multi_select_flags', 'Consideración'),
    ('P30:1', 'NSE', 'single_select', 'P30 sub-pregunta 1 — Galletas - distribución cadenas'),
    ('P30:2', 'NSE', 'single_select', 'P30 sub-pregunta 2'),
    ('P26:1', 'NSE', 'single_select', 'P26 misión 1 — Abastecimiento'),
    ('P32:1', 'NSE', 'single_select', 'P32 mejor precio categoria 1'),
    ('P23:1', 'Marca preferida', 'multi_select_flags', 'P23 asociación atributo 1 cross marca preferida'),
]

for q_code, bk, expected_type, descripcion in CASES:
    print(f"\n--- {q_code} x {bk} ({descripcion}) ---")
    if q_code not in data:
        print(f"  NO existe pregunta {q_code}")
        continue
    q = data[q_code]
    if bk not in q['tables_by_bk']:
        print(f"  NO existe BK {bk}")
        continue
    table = q['tables_by_bk'][bk]
    print(f"  Tipo: {q['tipo']} -> table.type={table['type']}")
    print(f"  Base total: {table['base_total']}, BK levels: {table['base_bk_levels']}")
    for row in table['rows'][:5]:
        cells = ' | '.join(f"{c['level']}: {c['pct']}%" for c in row['bk_cells'])
        flag = ' ⚠ TODOS 100%' if all(c['pct'] == 100.0 for c in row['bk_cells']) and row['total']['pct'] == 100.0 else ''
        print(f"    {row['category'][:40]:42s}  T:{row['total']['pct']}%  {cells}{flag}")
