import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open(r'C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis\questionnaire_map.json', encoding='utf-8'))
print(f'Total preguntas: {len(data)}\n')
for q in sorted(data.keys(), key=lambda x: (x[0:2], int(re.findall(r'\d+', x)[0]))):
    m = data[q]
    base_n_max = max(c['n_valid'] for c in m['cols'])
    base_n_min = min(c['n_valid'] for c in m['cols'])
    filt_flag = ' [FILTRADA]' if base_n_min < 200 else ''
    print(f"{q:8s}  {m['tipo']:14s}  {m['n_cols']:3d} cols  base={base_n_min}-{base_n_max}{filt_flag}")
