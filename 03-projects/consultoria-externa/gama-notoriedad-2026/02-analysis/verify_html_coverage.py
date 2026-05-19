"""Verifica cobertura HTML vs cuestionario completo."""
import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

# Preguntas declaradas en guia_preguntas_2026.md (cuestionario oficial)
CUESTIONARIO = {
    'PF2': 'Ubicación (Municipio + Parroquia)',
    'PF5': 'Género',
    'PF7': 'Grupo de edad',
    'PF8': 'Relación con la zona',
    'PF9': 'Rol en toma de decisiones de compra',
    'PF10': 'Dónde suele hacer compras de mercado',
    'P16': 'Supermercados conoce/oído (TOM espontánea)',
    'P17': 'Conoce o ha oído (asistida)',
    'P19': 'Consideraría hacer compras',
    'P20': 'Compras últimos 3 meses',
    'P21': 'Preferido',
    'P21.1': 'Por qué razón es su preferido (espontánea)',
    'P22': 'Importancia de atributos (10)',
    'P23': 'Asociación marca x atributo (10 atributos)',
    'P24': 'Dónde realizó última compra',
    'P25': 'Razón última compra',
    'P26': 'Mejor lugar por categoría / misión (5 misiones)',
    'P30': 'Lugar habitual por categoría (15 categorías)',
    'P31': 'Ranking precios entre cadenas',
    'P32': 'Mejor precio por categoría (15 categorías)',
    'P33': 'Nivel precio Gama (caro/igual/económico)',
    'P34': 'Evolución precios Gama 6 meses',
    'P35': 'Recuerda frase publicidad Gama (espontánea)',
    'P36': 'Cuál frase recuerda',
    'P37': 'Recuerda PTL (Precios de tu lado)',
    'P38': 'Le agrada PTL',
    'P39': 'Qué le quiso decir PTL',
    'P40': 'Recuerda DTLS (De tu lado siempre)',
    'P41': 'Le agrada DTLS',
    'P42': 'Qué le quiso decir DTLS',
    'P43': 'SOLO PARA MUESTRA EL RECREO (filtro especial)',
    'P44': 'Gama comparado con otros supermercados',
    'P45': 'Disponibilidad a comprar en Gama si abre sucursal',
    'PD4': 'NSE',
    # Operacionales que NO son analíticas:
    'PD5': 'Nombre encuestador (operacional)',
    'PD6': 'Nombre supervisor (operacional)',
    'PD7': 'Tipo de supervisión (operacional)',
    'P48': 'Comentarios (texto libre operacional)',
    'P49': 'Tipo de campo (operacional)',
}

# Cargar preguntas en el HTML (de all_tables.json)
data = json.load(open(r'C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis\all_tables.json', encoding='utf-8'))
html_questions = [k for k in data.keys() if not k.startswith('_')]

# Normalizar las sub-preguntas P23:N a P23
html_base_qs = set()
for q in html_questions:
    if ':' in q:
        html_base_qs.add(q.split(':')[0])
    else:
        html_base_qs.add(q)

# Quitar P21.1 (es sub) y agregar P21.1 separado
# Las preguntas BASE del cuestionario son las del dict CUESTIONARIO

# Comparación
en_cuestionario = set(CUESTIONARIO.keys())
en_html_normalizadas = html_base_qs | {q for q in html_questions if q == 'P21.1'}

faltantes = en_cuestionario - en_html_normalizadas
extras = en_html_normalizadas - en_cuestionario

print("="*80)
print("VERIFICACION COBERTURA HTML vs CUESTIONARIO")
print("="*80)
print(f"\nPreguntas en cuestionario (oficial): {len(en_cuestionario)}")
print(f"Preguntas en HTML (normalizadas): {len(en_html_normalizadas)}")
print(f"Total tablas en HTML (incluye P23 desglosado): {len(html_questions)}")

print(f"\n--- INCLUIDAS EN HTML ({len(en_cuestionario - faltantes)}) ---")
incluidas = sorted(en_cuestionario - faltantes, key=lambda x: (x[0:2], int(re.findall(r'\d+', x)[0])))
for q in incluidas:
    print(f"  ✓ {q:6s} {CUESTIONARIO[q]}")

print(f"\n--- FALTANTES EN HTML ({len(faltantes)}) ---")
for q in sorted(faltantes, key=lambda x: (x[0:2], int(re.findall(r'\d+', x)[0]))):
    desc = CUESTIONARIO[q]
    razon = ''
    if 'operacional' in desc.lower():
        razon = ' [excluida intencionalmente — operacional]'
    elif q == 'P43':
        razon = ' [excluida intencionalmente — filtro especial El Recreo]'
    print(f"  ✗ {q:6s} {desc}{razon}")

print(f"\n--- EXTRAS EN HTML (no en cuestionario formal) ---")
for q in sorted(extras):
    print(f"  + {q}")

# Verificar P23 desglosado
p23_subs = [q for q in html_questions if q.startswith('P23:')]
print(f"\n--- P23 DESGLOSADO EN HTML ---")
print(f"  P23 viene como {len(p23_subs)} sub-preguntas (P23:N por cada atributo):")
for q in sorted(p23_subs, key=lambda x: int(x.split(':')[1])):
    print(f"    {q}")
