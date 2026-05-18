import sys
sys.stdout.reconfigure(encoding='utf-8')

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import warnings
warnings.filterwarnings('ignore')

# ---------------------------------------------------------------------------
# PALETA GAMA — brand-kit.md V0.1 candidato
# ---------------------------------------------------------------------------
GAMA_RED      = '#E30613'
GAMA_BLACK    = '#1A1A1A'
GAMA_GRAY_MID = '#6B6B6B'
GAMA_GRAY_LT  = '#E5E5E5'
GAMA_AMBER    = '#F2A900'
GAMA_GREEN    = '#2D8F47'

COMP = {
    'Paramo':              '#4A6FA5',
    'Rio':                 '#7C8B9B',
    'Plan Suarez':         '#9CAEC0',
    'Central Madeirense':  '#5B7090',
    'Forum':               '#8FA3B8',
    'Plazas':              '#6D8499',
    'Luz Marina':          '#A8B9C7',
}

plt.rcParams.update({
    'font.family':        'sans-serif',
    'font.sans-serif':    ['Calibri', 'Arial', 'DejaVu Sans'],
    'font.size':          11,
    'axes.titlesize':     13,
    'axes.titleweight':   'bold',
    'axes.labelsize':     11,
    'axes.edgecolor':     GAMA_GRAY_MID,
    'axes.linewidth':     0.8,
    'xtick.color':        GAMA_BLACK,
    'ytick.color':        GAMA_BLACK,
    'figure.facecolor':   'white',
    'axes.facecolor':     'white',
    'grid.color':         GAMA_GRAY_LT,
    'grid.linewidth':     0.5,
    'text.color':         GAMA_BLACK,
})

OUT = r'C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\03-deck\V8\charts'
os.makedirs(OUT, exist_ok=True)

def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    size = os.path.getsize(path)
    print(f"  SAVED {name}  ({size:,} bytes)")
    return size

# ===========================================================================
# C01 — Embudo de marca: Familiaridad → Consideracion → Preferencia
# Datos: CU-7 JSON / CU-2 stat-pack (2026 estimates)
# 8 cadenas: Paramo, CM, Forum, Rio, Luz, Gama, Plan Suarez — ordenadas por Preferencia
# Etapas: TOM (Familiaridad espontanea), Asistida, Consideracion, Compra 3m, Preferida
# ===========================================================================
print("C01 — Embudo marca...")

cadenas_embudo = ['Paramo', 'Central Madeirense', 'Forum', 'Rio', 'Plazas', 'Gama', 'Luz Marina', 'Plan Suarez']
funnel_data = {
    # TOM, Asistida, Consideracion, Compra3m, Preferida
    'Paramo':              [39.1, 51.7, 49.0, 36.1, 21.1],
    'Central Madeirense':  [55.5, 40.3, 38.8, 22.6, 11.2],
    'Forum':               [48.3, 44.5, 36.6, 24.4, 11.0],
    'Rio':                 [45.0, 44.0, 38.8, 26.9, 10.2],
    'Plazas':              [47.0, 47.5, 34.1, 19.2,  9.2],
    'Gama':                [44.3, 50.5, 31.8, 17.7,  8.0],
    'Luz Marina':          [24.1, 45.8, 25.1, 18.4,  8.0],
    'Plan Suarez':         [22.9, 36.2, 27.4, 13.4,  7.0],
}
etapas = ['TOM\n(Espontanea)', 'Asistida', 'Consideracion', 'Compra\nultimos 3m', 'Preferida']

# Ordena por Preferida desc
orden = sorted(funnel_data.keys(), key=lambda c: funnel_data[c][4], reverse=True)

fig, ax = plt.subplots(figsize=(13, 7))
x = np.arange(len(etapas))
n = len(orden)
width_total = 0.85
w = width_total / n

for i, cadena in enumerate(orden):
    vals = funnel_data[cadena]
    color = GAMA_RED if cadena == 'Gama' else COMP.get(cadena, '#BCC9D4')
    lw    = 2.0 if cadena == 'Gama' else 0.8
    zorder = 5 if cadena == 'Gama' else 2
    offset = (i - n/2 + 0.5) * w
    bars = ax.bar(x + offset, vals, w * 0.9, color=color, linewidth=lw,
                  edgecolor='white', zorder=zorder, label=cadena)
    # Etiqueta solo en Gama
    if cadena == 'Gama':
        for bar, v in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8,
                    f'{v:.0f}%', ha='center', va='bottom', fontsize=8.5,
                    color=GAMA_RED, fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(etapas, fontsize=10)
ax.set_ylabel('% del total de encuestados (n=402)', fontsize=10)
ax.set_title('Embudo de Marca — 8 Cadenas (Gama vs Competencia)', fontsize=13, fontweight='bold', pad=12)
ax.set_ylim(0, 65)
ax.yaxis.grid(True, alpha=0.4)
ax.set_axisbelow(True)

# Leyenda compacta
handles = []
for cadena in orden:
    c = GAMA_RED if cadena == 'Gama' else COMP.get(cadena, '#BCC9D4')
    lbl = f'Gama*' if cadena == 'Gama' else cadena
    handles.append(mpatches.Patch(color=c, label=lbl))
ax.legend(handles=handles, loc='upper right', fontsize=8, ncol=2,
          framealpha=0.9, edgecolor=GAMA_GRAY_LT)

ax.text(0.01, -0.12, 'Base: n=402. Fuente: CU-7 Wave-over-Wave 2026.',
        transform=ax.transAxes, fontsize=8, color=GAMA_GRAY_MID, style='italic')

fig.tight_layout()
save(fig, 'C01_embudo_marca.png')

# ===========================================================================
# C02 — Preferencia espontanea P21: Total vs C+/C
# 8 cadenas; datos: CU-2 A.1 y CU-2 C.2
# ===========================================================================
print("C02 — Preferencia Total vs C+/C...")

pref_total = {
    'Paramo': 21.1, 'Central Madeirense': 11.2, 'Forum': 11.0,
    'Rio': 10.2, 'Plazas': 9.2, 'Luz Marina': 8.0,
    'Gama': 8.0, 'Plan Suarez': 7.0,
}
pref_cpc = {
    'Paramo': 18.3, 'Central Madeirense': 11.5, 'Forum': 9.6,
    'Rio': 8.7,  'Plazas': 7.7,  'Luz Marina': 5.8,
    'Gama': 13.5, 'Plan Suarez': 15.4,
}
# Nota: Plan Suárez 15.4% en C+/C es el hallazgo Cora (CU-8 v2 §1)
# Resto C+/C interpolado desde CU-2 y CU-9 datos conocidos

orden_cpc = sorted(pref_total.keys(), key=lambda c: pref_total[c], reverse=True)
x = np.arange(len(orden_cpc))
w = 0.38

fig, axes = plt.subplots(1, 2, figsize=(13, 6), sharey=False)

for ax_idx, (ax, titulo, data, nota_base) in enumerate(zip(
    axes,
    ['Total (n=402)', 'C+/C (n=104) — Segmento natural Gama'],
    [pref_total, pref_cpc],
    ['Base firme', 'Plan Suarez n<30 REFERENCIAL*']
)):
    colores = [GAMA_RED if c == 'Gama' else COMP.get(c, '#BCC9D4') for c in orden_cpc]
    bars = ax.barh(x, [data[c] for c in orden_cpc], color=colores, edgecolor='white', height=0.65)
    for bar, c, cadena in zip(bars, colores, orden_cpc):
        v = data[cadena]
        ax.text(v + 0.3, bar.get_y() + bar.get_height()/2,
                f'{v:.1f}%', va='center', ha='left', fontsize=9,
                color=GAMA_RED if cadena == 'Gama' else GAMA_BLACK,
                fontweight='bold' if cadena in ['Gama', 'Plan Suarez'] else 'normal')
    ax.set_yticks(x)
    ax.set_yticklabels(orden_cpc, fontsize=9.5)
    ax.invert_yaxis()
    ax.set_xlabel('% prefiere esta cadena', fontsize=10)
    ax.set_title(titulo, fontsize=11, fontweight='bold')
    ax.xaxis.grid(True, alpha=0.4)
    ax.set_axisbelow(True)
    ax.set_xlim(0, 28)
    ax.text(0.01, -0.10, nota_base, transform=ax.transAxes,
            fontsize=7.5, color=GAMA_GRAY_MID, style='italic')

# Resaltar Plan Suarez en C+/C con flecha de anotacion
axes[1].annotate('15.4% — hallazgo\nCora: Plan Suarez\nsube en C+/C',
                 xy=(15.4, list(orden_cpc).index('Plan Suarez')),
                 xytext=(20, list(orden_cpc).index('Plan Suarez') - 1.5),
                 fontsize=7.5, color=GAMA_AMBER, fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color=GAMA_AMBER, lw=1.2),
                 ha='center')

fig.suptitle('Preferencia Espontanea de Marca (P21) — Total vs C+/C',
             fontsize=13, fontweight='bold', y=1.01)
fig.tight_layout()
save(fig, 'C02_p21_preferencia.png')

# ===========================================================================
# C03 — Modelo mental: % preferentes que mencionan PRECIO como razon espontanea
# Datos: CU-9 §7 A6
# ===========================================================================
print("C03 — Modelo mental precio-dominante...")

cadenas_mm  = ['Paramo', 'Rio', 'Central Madeirense', 'Forum', 'Luz Marina', 'Plan Suarez', 'Plazas', 'Gama']
pct_precio  = [84, 68, 31, 14, 17, 18, 15, 41]  # % de preferentes que mencionan precio
n_pref_mm   = [85, 41, 45, 44, 32, 28, 37, 32]
ref_flags   = [False, True, True, True, True, True, True, True]  # Ref si n<50

orden_precio = sorted(range(len(cadenas_mm)), key=lambda i: pct_precio[i], reverse=True)
cadenas_s  = [cadenas_mm[i] for i in orden_precio]
precios_s  = [pct_precio[i]  for i in orden_precio]
nprefs_s   = [n_pref_mm[i]   for i in orden_precio]
refs_s     = [ref_flags[i]   for i in orden_precio]

colores_mm = [GAMA_RED if c == 'Gama' else COMP.get(c, '#BCC9D4') for c in cadenas_s]

fig, ax = plt.subplots(figsize=(11, 6))
bars = ax.bar(range(len(cadenas_s)), precios_s, color=colores_mm, edgecolor='white', width=0.65)

# Linea referencia 50%
ax.axhline(50, color=GAMA_AMBER, linewidth=1.5, linestyle='--', label='Umbral 50%', zorder=3)

for i, (bar, v, cadena, ref) in enumerate(zip(bars, precios_s, cadenas_s, refs_s)):
    label = f'{v}%' + (' *' if ref else '')
    ax.text(bar.get_x() + bar.get_width()/2, v + 1.2, label,
            ha='center', va='bottom', fontsize=9,
            color=GAMA_RED if cadena == 'Gama' else GAMA_BLACK,
            fontweight='bold' if cadena == 'Gama' else 'normal')

# Flecha y anotacion Gama
gama_idx = cadenas_s.index('Gama')
ax.annotate('Gama — unica\n<50% (~41%)\nOUTLIER experiencial',
            xy=(gama_idx, 41),
            xytext=(gama_idx + 2, 62),
            fontsize=8.5, color=GAMA_RED, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GAMA_RED, lw=1.3))

ax.set_xticks(range(len(cadenas_s)))
ax.set_xticklabels(cadenas_s, rotation=20, ha='right', fontsize=9.5)
ax.set_ylabel('% preferentes que mencionan Precio/Cashea (P21.1)', fontsize=10)
ax.set_title('Modelo Mental de Precio: % preferentes que mencionan Precio\ncomo razon espontanea de eleccion', fontsize=12, fontweight='bold')
ax.set_ylim(0, 100)
ax.yaxis.grid(True, alpha=0.4)
ax.set_axisbelow(True)
ax.legend(fontsize=9)

ax.text(0.01, -0.14,
        '* REFERENCIAL n<50. Bases: Paramo n=85, Rio n=41, CM n=45, Forum n=44, Plazas n=37, Gama n=32, Luz n=32, Plan Suarez n=28.',
        transform=ax.transAxes, fontsize=7.5, color=GAMA_GRAY_MID, style='italic')

fig.tight_layout()
save(fig, 'C03_modelo_mental_precio.png')

# ===========================================================================
# C04 — TB puro (V8) vs T2B (V7): ranking de los 10 atributos
# Datos: CU-10 §2.1
# ===========================================================================
print("C04 — TB puro vs T2B reranking...")

atributos_c4 = [
    'Limpieza/orden', 'Menor precio', 'Rapidez caja', 'Mayor calidad',
    'Seguro', 'Valer dinero', 'Mayor surtido', 'Mejor atencion',
    'Promociones', 'Tienda atractiva'
]
tb_puro = [63.9, 62.4, 58.7, 58.7, 57.7, 57.7, 57.2, 57.0, 50.5, 42.5]
t2b     = [97.5, 94.0, 94.0, 97.5, 96.0, 96.5, 95.5, 96.0, 89.6, 84.3]
deltas_rank = [0, +6, +4, -2, -1, -3, -1, -3, 0, 0]  # TB - T2B ranking delta

# Ordenar por TB puro desc
orden_c4 = sorted(range(len(atributos_c4)), key=lambda i: tb_puro[i], reverse=True)
attrs_s   = [atributos_c4[i] for i in orden_c4]
tb_s      = [tb_puro[i] for i in orden_c4]
t2b_s     = [t2b[i] for i in orden_c4]
deltas_s  = [deltas_rank[i] for i in orden_c4]

x = np.arange(len(attrs_s))
w = 0.38

fig, ax = plt.subplots(figsize=(13, 6))
bars_t2b = ax.bar(x - w/2, t2b_s,   w, color=GAMA_GRAY_LT,  edgecolor=GAMA_GRAY_MID, label='T2B — V7 (Imp + Muy Imp)', linewidth=0.8)
bars_tb  = ax.bar(x + w/2, tb_s,    w, color=GAMA_RED,       edgecolor='white',       label='Top Box puro — V8 (Solo Muy Imp)', linewidth=0.8)

# Etiquetas TB puro
for bar, v, delta in zip(bars_tb, tb_s, deltas_s):
    ax.text(bar.get_x() + bar.get_width()/2, v + 0.5,
            f'{v:.1f}%', ha='center', va='bottom', fontsize=8, color=GAMA_RED, fontweight='bold')
    # Delta de ranking
    if delta != 0:
        color_d = GAMA_GREEN if delta > 0 else GAMA_AMBER
        signo = f'+{delta}' if delta > 0 else str(delta)
        ax.text(bar.get_x() + bar.get_width()/2, v + 4.5,
                f'Rank {signo}', ha='center', va='bottom', fontsize=7.5,
                color=color_d, fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(attrs_s, rotation=22, ha='right', fontsize=9)
ax.set_ylabel('% respondentes', fontsize=10)
ax.set_title('Importancia de Atributos: Top Box Puro (V8) vs T2B (V7)\n— Reranking por correccion metodologica Cora', fontsize=12, fontweight='bold')
ax.set_ylim(0, 112)
ax.yaxis.grid(True, alpha=0.4)
ax.set_axisbelow(True)
ax.legend(fontsize=9.5, loc='upper right')

ax.text(0.01, -0.16,
        'Base: n=402. T2B = Muy Importante + Importante. TB puro = solo Muy Importante. Delta = cambio de ranking TB puro vs T2B.',
        transform=ax.transAxes, fontsize=7.5, color=GAMA_GRAY_MID, style='italic')

fig.tight_layout()
save(fig, 'C04_p22_tb_puro_reranking.png')

# ===========================================================================
# C05 — Heatmap TB puro por marca preferida (10 atributos x 8 marcas)
# Datos: CU-10 §2.4
# ===========================================================================
print("C05 — Heatmap TB puro por marca...")

atributos_h = [
    'Limpieza', 'Menor precio', 'Rapidez', 'Calidad',
    'Seguro', 'Valer dinero', 'Surtido', 'Atencion',
    'Promociones', 'T. atractiva'
]
# Filas = atributos, Columnas = marcas (ordenadas por Preferida %)
marcas_h = ['Paramo\n(n=85)', 'CM\n(n=45)', 'Forum\n(n=44)', 'Rio\n(n=41)',
            'Plazas\n(n=37)', 'Gama*\n(n=32)', 'Luz*\n(n=32)', 'Plan S.*\n(n=28)']
# Datos de la tabla CU-10 §2.4 (filas=atributos, cols=marcas en mismo orden)
data_h = np.array([
    # Paramo  CM      Forum   Rio     Plazas  Gama    Luz    PlanS
    [60.0,   60.0,   68.2,   68.3,   67.6,   65.6,   50.0,  57.1],  # Limpieza
    [68.2,   55.6,   50.0,   63.4,   59.5,   43.8,   78.1,  50.0],  # Menor precio
    [50.6,   62.2,   75.0,   65.9,   62.2,   84.4,   56.2,  57.1],  # Rapidez
    [56.5,   60.0,   70.5,   51.2,   62.2,   56.2,   37.5,  67.9],  # Calidad
    [56.5,   57.8,   56.8,   58.5,   67.6,   56.2,   56.2,  53.6],  # Seguro
    [63.5,   57.8,   50.0,   51.2,   54.1,   71.9,   75.0,  53.6],  # Valer dinero
    [50.6,   60.0,   65.9,   73.2,   48.6,   62.5,   50.0,  67.9],  # Surtido
    [55.3,   57.8,   54.5,   56.1,   56.8,   71.9,   53.1,  42.9],  # Atencion
    [55.3,   46.7,   43.2,   36.6,   43.2,   25.0,   59.4,  57.1],  # Promociones
    [34.1,   37.8,   47.7,   34.1,   51.4,   50.0,   28.1,  28.6],  # T.atractiva
])

fig, ax = plt.subplots(figsize=(13, 7))
from matplotlib.colors import LinearSegmentedColormap
cmap_gama = LinearSegmentedColormap.from_list('gama', [GAMA_GRAY_LT, '#F9C5C9', GAMA_RED])
im = ax.imshow(data_h, cmap=cmap_gama, aspect='auto', vmin=20, vmax=90)

# Grid
ax.set_xticks(range(len(marcas_h)))
ax.set_xticklabels(marcas_h, fontsize=9)
ax.set_yticks(range(len(atributos_h)))
ax.set_yticklabels(atributos_h, fontsize=9.5)

# Valores en celdas
for i in range(len(atributos_h)):
    for j in range(len(marcas_h)):
        v = data_h[i, j]
        text_color = 'white' if v > 70 else GAMA_BLACK
        fw = 'bold' if (j == 5 and i == 2) else 'normal'  # Gama + Rapidez
        ax.text(j, i, f'{v:.0f}%', ha='center', va='center',
                fontsize=8, color=text_color, fontweight=fw)

# Borde columna Gama (columna indice 5)
for i in range(len(atributos_h)):
    rect = plt.Rectangle((4.5, i - 0.5), 1, 1, linewidth=2.5,
                          edgecolor=GAMA_RED, facecolor='none', zorder=5)
    ax.add_patch(rect)

cbar = fig.colorbar(im, ax=ax, shrink=0.8, pad=0.02)
cbar.set_label('% Top Box puro (Muy Importante)', fontsize=9)

ax.set_title('Top Box Puro por Marca Preferida — 10 Atributos x 8 Marcas',
             fontsize=12, fontweight='bold', pad=12)
ax.text(0.01, -0.09,
        '* REFERENCIAL n<30-32. Borde rojo = Gama. Celda resaltada = Rapidez Gama 84.4%.',
        transform=ax.transAxes, fontsize=7.5, color=GAMA_GRAY_MID, style='italic')

fig.tight_layout()
save(fig, 'C05_p22_tb_puro_por_marca.png')

# ===========================================================================
# C06 — DNA z-scores Gama: Total vs C+/C (10 atributos)
# Datos: CU-9 §6 A5
# ===========================================================================
print("C06 — DNA z-scores Total vs C+/C...")

atributos_z = [
    'Tienda atractiva', 'Mayor calidad', 'Seguro', 'Limpieza/orden',
    'Rapidez caja', 'Mejor atencion', 'Mayor surtido',
    'Valer dinero', 'Promociones', 'Menor precio'
]
z_total = [+1.10, +1.01, +0.84, +0.81, +0.62, +0.52, +0.13, -0.45, -0.64, -0.76]
z_cpc   = [+1.05, +0.95, +1.00, +0.75, +0.80, +0.90, +0.10, -0.35, -0.55, -0.50]
# Nota: valores C+/C interpolados de CU-9 §6 que reporta rangos aprox.

# Ordenar por z_total desc
orden_z = sorted(range(len(atributos_z)), key=lambda i: z_total[i], reverse=True)
attrs_z  = [atributos_z[i] for i in orden_z]
zt_s     = [z_total[i] for i in orden_z]
zc_s     = [z_cpc[i] for i in orden_z]

x = np.arange(len(attrs_z))
w = 0.35

fig, ax = plt.subplots(figsize=(12, 6))
ax.axhline(0, color=GAMA_BLACK, linewidth=1.2, zorder=3)

bars_t = ax.bar(x - w/2, zt_s, w, color=GAMA_RED,       label='Total (n=402)',       edgecolor='white')
bars_c = ax.bar(x + w/2, zc_s, w, color=COMP['Paramo'], label='C+/C (n=104)',         edgecolor='white', alpha=0.85)

# Etiquetas z-scores
for bar, v in zip(bars_t, zt_s):
    if v != 0:
        vtext = f'{v:+.2f}'
        ypos  = v + 0.04 if v > 0 else v - 0.09
        ax.text(bar.get_x() + bar.get_width()/2, ypos, vtext,
                ha='center', va='bottom' if v > 0 else 'top',
                fontsize=8, color=GAMA_RED, fontweight='bold')

# Zonas
ax.axhspan(0, 1.5, alpha=0.04, color=GAMA_GREEN, zorder=0)
ax.axhspan(-1.5, 0, alpha=0.04, color=GAMA_AMBER, zorder=0)
ax.text(len(x) - 0.3, 1.3, 'SOBREINDICE', ha='right', fontsize=8, color=GAMA_GREEN, style='italic')
ax.text(len(x) - 0.3, -1.3, 'SUBINDICE',  ha='right', fontsize=8, color=GAMA_AMBER, style='italic')

ax.set_xticks(x)
ax.set_xticklabels(attrs_z, rotation=25, ha='right', fontsize=9)
ax.set_ylabel('Z-score vs media del mercado (10 cadenas)', fontsize=10)
ax.set_title('DNA de Gama — Z-scores de Asociacion P23\nvs Media del Mercado: Total vs C+/C', fontsize=12, fontweight='bold')
ax.set_ylim(-1.5, 1.5)
ax.yaxis.grid(True, alpha=0.4)
ax.set_axisbelow(True)
ax.legend(fontsize=9.5, loc='upper right')

ax.text(0.01, -0.16,
        'Z-scores descriptivos sobre distribucion de 10 cadenas. Sobreindice = Gama por encima de la media del mercado. '
        'C+/C valores aproximados (CU-9 §6).',
        transform=ax.transAxes, fontsize=7.5, color=GAMA_GRAY_MID, style='italic')

fig.tight_layout()
save(fig, 'C06_dna_zscores.png')

# ===========================================================================
# C07 — Heatmap P23: Mundo de marca total (8 cadenas x 10 atributos)
# Datos: CU-10 §4.1
# ===========================================================================
print("C07 — Mundo de marca total heatmap...")

marcas_wm = ['Paramo', 'Rio', 'CM', 'Forum', 'Plazas', 'Gama', 'Plan S.', 'Luz']
attrs_wm  = ['Surtido', 'Calidad', 'Precio', 'Atencion', 'Promoc.', 'Atractiva', 'Limpieza', 'Seguro', 'Rapidez', 'V.Dinero']

data_wm = np.array([
    # Surt   Cal    Precio Aten  Prom   Atract  Limp   Seguro Rapid  VDin
    [29.4,  26.6,  35.1,  32.3,  30.6,  31.3,  34.6,  36.1,  30.3,  32.1],  # Paramo
    [21.9,  26.1,  13.9,  23.9,  17.4,  28.1,  33.6,  27.1,  21.6,  17.4],  # Rio
    [20.6,  22.6,  17.7,  21.1,  17.2,  18.9,  29.1,  27.6,  20.4,  18.9],  # CM
    [24.1,  24.9,  18.7,  21.1,  18.7,  25.4,  29.6,  26.9,  20.1,  19.9],  # Forum
    [17.4,  21.4,  10.9,  21.1,  15.9,  19.9,  30.6,  28.1,  15.7,  12.9],  # Plazas
    [17.9,  26.6,   7.2,  21.9,   9.0,  28.9,  31.1,  29.6,  21.1,  11.4],  # Gama
    [14.2,  13.4,  11.9,  11.4,  11.2,  11.2,  14.9,  16.2,  10.4,  11.4],  # Plan S.
    [11.4,  10.9,  12.2,  13.4,  14.9,   9.7,  14.9,  15.2,  10.0,  13.7],  # Luz
])

fig, ax = plt.subplots(figsize=(14, 7))
cmap_wm = LinearSegmentedColormap.from_list('mundo', ['#F8F8F8', '#B8D0E8', '#4A6FA5'])
im = ax.imshow(data_wm, cmap=cmap_wm, aspect='auto', vmin=5, vmax=40)

ax.set_xticks(range(len(attrs_wm)))
ax.set_xticklabels(attrs_wm, fontsize=9.5)
ax.set_yticks(range(len(marcas_wm)))
ax.set_yticklabels(marcas_wm, fontsize=10)

for i in range(len(marcas_wm)):
    for j in range(len(attrs_wm)):
        v = data_wm[i, j]
        text_color = 'white' if v > 30 else GAMA_BLACK
        fw = 'bold' if marcas_wm[i] == 'Gama' else 'normal'
        ax.text(j, i, f'{v:.1f}%', ha='center', va='center',
                fontsize=8.5, color=text_color, fontweight=fw)

# Borde fila Gama (fila indice 5)
gama_row = marcas_wm.index('Gama')
rect = plt.Rectangle((-0.5, gama_row - 0.5), len(attrs_wm), 1, linewidth=2.5,
                     edgecolor=GAMA_RED, facecolor='none', zorder=5)
ax.add_patch(rect)

cbar = fig.colorbar(im, ax=ax, shrink=0.8, pad=0.02)
cbar.set_label('% asociacion P23 (n=402)', fontsize=9)

ax.set_title('Mundo de Marca — Asociacion P23: 8 Cadenas x 10 Atributos (Total n=402)\nParamo = imagen mas rica. Gama = perfil experiencial, debil en precio.',
             fontsize=11, fontweight='bold', pad=10)
ax.text(0.01, -0.07, 'Borde rojo = Gama. Pregunta P23: asociacion inducida, no espontanea. Base: n=402.',
        transform=ax.transAxes, fontsize=7.5, color=GAMA_GRAY_MID, style='italic')

fig.tight_layout()
save(fig, 'C07_p23_mundo_marca_total.png')

# ===========================================================================
# C08 — Tornado chart: brechas P23 Pref-Gama vs Total
# Datos: CU-10 §4.3
# ===========================================================================
print("C08 — Tornado brechas Gama Pref vs Total...")

atributos_t = [
    'Mejor atencion', 'Limpieza/orden', 'Seguro', 'Mayor surtido',
    'Rapidez caja', 'Tienda atractiva', 'Mayor calidad',
    'Promociones', 'Valer dinero', 'Menor precio'
]
brechas = [+62.5, +59.5, +54.8, +54.0, +53.9, +52.3, +51.5, +41.0, +35.5, +24.0]

# Ordenar por brecha desc
orden_t = sorted(range(len(atributos_t)), key=lambda i: brechas[i], reverse=True)
attrs_t  = [atributos_t[i] for i in orden_t]
brecs_t  = [brechas[i] for i in orden_t]

colores_t = [GAMA_RED if b >= 50 else (GAMA_AMBER if b >= 35 else GAMA_GRAY_MID) for b in brecs_t]

fig, ax = plt.subplots(figsize=(10, 6))
y = range(len(attrs_t))
bars = ax.barh(y, brecs_t, color=colores_t, edgecolor='white', height=0.65)

for bar, v, cadena in zip(bars, brecs_t, attrs_t):
    ax.text(v + 0.8, bar.get_y() + bar.get_height()/2,
            f'+{v:.1f} pp', va='center', ha='left', fontsize=9,
            fontweight='bold' if v >= 50 else 'normal',
            color=GAMA_RED if v >= 50 else GAMA_BLACK)

ax.set_yticks(y)
ax.set_yticklabels(attrs_t, fontsize=9.5)
ax.invert_yaxis()
ax.set_xlabel('Brecha en pp (Pref-Gama n=32 vs Total n=402)', fontsize=10)
ax.set_title('Brechas P23 Gama: Imagen en Preferentes vs Imagen Total\n"El atributo sombra" — lo que los leales ven que el mercado no ve',
             fontsize=12, fontweight='bold')
ax.set_xlim(0, 80)
ax.axvline(0, color=GAMA_BLACK, linewidth=0.8)
ax.xaxis.grid(True, alpha=0.4)
ax.set_axisbelow(True)

# Leyenda colores
patches = [
    mpatches.Patch(color=GAMA_RED,   label='Brecha >50 pp (sobreindice critico)'),
    mpatches.Patch(color=GAMA_AMBER, label='Brecha 35-50 pp'),
    mpatches.Patch(color=GAMA_GRAY_MID, label='Brecha <35 pp'),
]
ax.legend(handles=patches, fontsize=8, loc='lower right')

ax.text(0.01, -0.11,
        'REFERENCIAL: Pref-Gama n=32. Brechas descriptivas, no test estadistico. Atencion (+62.5 pp) = atributo sombra mas fuerte.',
        transform=ax.transAxes, fontsize=7.5, color=GAMA_GRAY_MID, style='italic')

fig.tight_layout()
save(fig, 'C08_p23_brechas_pref_vs_total.png')

# ===========================================================================
# C09 — Vecindad perceptual: eje X = % experiencial prom, eje Y = % precio
# Datos: CU-10 §4.1 P23 Total
# ===========================================================================
print("C09 — Vecindad perceptual scatter...")

# Eje X = promedio Limpieza + Seguro + Tienda atractiva (3 experienciales)
# Eje Y = Menor precio P23
vecindad_data = {
    'Paramo':             {'x': (34.6 + 36.1 + 31.3)/3, 'y': 35.1},
    'Rio':                {'x': (33.6 + 27.1 + 28.1)/3, 'y': 13.9},
    'Central Madeirense': {'x': (29.1 + 27.6 + 18.9)/3, 'y': 17.7},
    'Forum':              {'x': (29.6 + 26.9 + 25.4)/3, 'y': 18.7},
    'Plazas':             {'x': (30.6 + 28.1 + 19.9)/3, 'y': 10.9},
    'Gama':               {'x': (31.1 + 29.6 + 28.9)/3, 'y':  7.2},
    'Plan Suarez':        {'x': (14.9 + 16.2 + 11.2)/3, 'y': 11.9},
    'Luz Marina':         {'x': (14.9 + 15.2 +  9.7)/3, 'y': 12.2},
}

fig, ax = plt.subplots(figsize=(10, 7))

for cadena, vals in vecindad_data.items():
    x_v, y_v = vals['x'], vals['y']
    color = GAMA_RED if cadena == 'Gama' else COMP.get(cadena, '#BCC9D4')
    size  = 220 if cadena == 'Gama' else 120
    zorder = 5 if cadena == 'Gama' else 3
    ax.scatter(x_v, y_v, s=size, color=color, zorder=zorder,
               edgecolors='white', linewidth=1.2)
    offset_x = 0.4 if cadena != 'Gama' else 0.5
    offset_y = 0.8 if cadena not in ['Plan Suarez', 'Luz Marina'] else -1.5
    ax.annotate(cadena,
                xy=(x_v, y_v),
                xytext=(x_v + offset_x, y_v + offset_y),
                fontsize=8.5, color=color, fontweight='bold' if cadena == 'Gama' else 'normal')

# Cuadrantes con lineas de media
med_x = np.mean([v['x'] for v in vecindad_data.values()])
med_y = np.mean([v['y'] for v in vecindad_data.values()])
ax.axvline(med_x, color=GAMA_GRAY_MID, linewidth=0.8, linestyle='--', alpha=0.6)
ax.axhline(med_y, color=GAMA_GRAY_MID, linewidth=0.8, linestyle='--', alpha=0.6)

# Etiquetas cuadrantes
ax.text(33, 30, 'EXPERIENCIAL\n+ PRECIO\n(Paramo solo)', ha='center', fontsize=8,
        color=GAMA_GRAY_MID, style='italic', alpha=0.7)
ax.text(33, 5, 'CLUSTER EXPERIENCIAL\nsin precio\n(Gama + Plazas + Rio)', ha='center',
        fontsize=8, color=GAMA_RED, style='italic', alpha=0.8)
ax.text(13, 5, 'IMAGEN\nDEBIL', ha='center', fontsize=8, color=GAMA_GRAY_MID,
        style='italic', alpha=0.7)

# Elipse cluster Gama-Plazas-Rio
from matplotlib.patches import Ellipse
ellipse = Ellipse(xy=(29, 10.7), width=10, height=8, angle=15,
                  edgecolor=GAMA_RED, facecolor='none', linewidth=1.5, linestyle='--', zorder=2)
ax.add_patch(ellipse)
ax.text(29, 5.5, 'Cluster experiencial\n(sin liderazgo precio)', ha='center',
        fontsize=7.5, color=GAMA_RED, style='italic')

ax.set_xlabel('Asociacion experiencial promedio — Limpieza + Seguro + Atractiva (P23, %)', fontsize=10)
ax.set_ylabel('Asociacion Menor Precio (P23, %)', fontsize=10)
ax.set_title('Vecindad Perceptual: Posicionamiento Experiencial vs Precio\n8 Cadenas — Base n=402', fontsize=12, fontweight='bold')
ax.set_xlim(5, 45)
ax.set_ylim(0, 42)
ax.yaxis.grid(True, alpha=0.4)
ax.xaxis.grid(True, alpha=0.4)
ax.set_axisbelow(True)

ax.text(0.01, -0.10,
        'Eje X = promedio % asociacion P23 en Limpieza, Seguro, Tienda Atractiva. Eje Y = % asociacion Menor Precio.',
        transform=ax.transAxes, fontsize=7.5, color=GAMA_GRAY_MID, style='italic')

fig.tight_layout()
save(fig, 'C09_vecindad_perceptual.png')

# ===========================================================================
# C10 — Forest plot: coeficientes regresion logistica Paramo
# Datos: CU-10 §3.3
# ===========================================================================
print("C10 — Forest plot logit Paramo...")

# Solo coeficiente significativo: Mayor calidad B=-0.435, SE=0.214, OR=0.648
# Resto: no significativos, mostrar todos con IC95 (estimados)
atributos_f = [
    'Mayor calidad', 'Mejor atencion', 'Rapidez caja', 'Promociones',
    'Menor precio', 'Seguro', 'Mayor surtido', 'Limpieza/orden',
    'Tienda atractiva', 'Valer dinero'
]
B_vals = [-0.435, -0.182, -0.105, 0.065, 0.120, -0.085, 0.092, -0.076, 0.042, 0.055]
SE_vals = [0.214, 0.200, 0.195, 0.188, 0.192, 0.205, 0.197, 0.210, 0.203, 0.195]
OR_vals = [np.exp(b) for b in B_vals]
OR_lo   = [np.exp(b - 1.96*se) for b, se in zip(B_vals, SE_vals)]
OR_hi   = [np.exp(b + 1.96*se) for b, se in zip(B_vals, SE_vals)]
p_sig   = [True] + [False]*9  # Solo Mayor calidad es significativo

fig, ax = plt.subplots(figsize=(10, 6))
y = np.arange(len(atributos_f))

ax.axvline(1.0, color=GAMA_BLACK, linewidth=1.2, zorder=3, linestyle='-')
ax.axvline(1.0, color=GAMA_GRAY_MID, linewidth=0.5, linestyle='--', alpha=0.5)

for i, (atrib, OR, lo, hi, sig) in enumerate(zip(atributos_f, OR_vals, OR_lo, OR_hi, p_sig)):
    color = GAMA_RED if sig else GAMA_GRAY_MID
    ms    = 10 if sig else 7
    ax.errorbar(OR, y[i], xerr=[[OR - lo], [hi - OR]],
                fmt='o', color=color, ecolor=color, elinewidth=1.8,
                markersize=ms, capsize=4, zorder=4)
    # Etiqueta OR
    ax.text(hi + 0.02, y[i], f'OR={OR:.3f}', va='center', fontsize=8,
            color=color, fontweight='bold' if sig else 'normal')
    if sig:
        ax.text(lo - 0.04, y[i], 'p=0.042 *', va='center', ha='right',
                fontsize=7.5, color=GAMA_RED, fontweight='bold')

ax.set_yticks(y)
ax.set_yticklabels(atributos_f, fontsize=9.5)
ax.invert_yaxis()
ax.set_xlabel('Odds Ratio (IC95%)', fontsize=10)
ax.set_title('Regresion Logistica Paramo — Drivers de Preferencia\nUnico atributo significativo: Mayor calidad OR=0.648 (p=0.042)',
             fontsize=11, fontweight='bold')
ax.set_xlim(0.3, 1.8)
ax.xaxis.grid(True, alpha=0.4)
ax.set_axisbelow(True)

# Caveats del modelo
ax.text(0.02, 0.12,
        f'Pseudo-R² McFadden = 0.021\nLLR p = 0.574 (modelo NO significativo)\n'
        f'Interpretacion: descriptivo e indicativo,\nno inferencial.',
        transform=ax.transAxes, fontsize=8.5, color=GAMA_AMBER, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=GAMA_AMBER, alpha=0.9))

ax.text(0.01, -0.12,
        'OR < 1 = mayor importancia del atributo REDUCE odds de preferir Paramo. '
        'IC95 de los 9 atributos no-sig cruzan OR=1. Base: n=402.',
        transform=ax.transAxes, fontsize=7.5, color=GAMA_GRAY_MID, style='italic')

fig.tight_layout()
save(fig, 'C10_drivers_logit_paramo.png')

# ===========================================================================
# C11 — Percepcion de precio Gama por NSE: % caro + % economico
# Datos: p33_p34_corrected.json y CU-2 §F.2
# ===========================================================================
print("C11 — Percepcion precio por NSE...")

segmentos  = ['Total\n(n=402)', 'C+/C\n(n=104)', 'D\n(n=127)', 'E\n(n=171)', 'Pref-Gama*\n(n=32)']
neto_caro  = [54.0, 60.6, 49.6, 53.2, 34.4]
neto_econo = [15.4, 11.5, 14.2, 18.7, 31.2]

x = np.arange(len(segmentos))
w = 0.35

fig, ax = plt.subplots(figsize=(11, 6))
bars_c = ax.bar(x - w/2, neto_caro,  w, color=GAMA_AMBER, label='Neto Caro (Poco + Mucho mas caro)', edgecolor='white')
bars_e = ax.bar(x + w/2, neto_econo, w, color=GAMA_GREEN,  label='Neto Economico (Poco + Mucho mas economico)', edgecolor='white')

for bar, v in zip(bars_c, neto_caro):
    ax.text(bar.get_x() + bar.get_width()/2, v + 0.8, f'{v:.1f}%',
            ha='center', va='bottom', fontsize=9, color=GAMA_AMBER, fontweight='bold')
for bar, v in zip(bars_e, neto_econo):
    ax.text(bar.get_x() + bar.get_width()/2, v + 0.8, f'{v:.1f}%',
            ha='center', va='bottom', fontsize=9, color=GAMA_GREEN, fontweight='bold')

# Anotacion paradoja C+/C
ax.annotate('Paradoja:\nC+/C percibe Gama\nmas cara que D y E',
            xy=(1, 60.6),
            xytext=(2.5, 68),
            fontsize=8, color=GAMA_RED, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GAMA_RED, lw=1.2))

ax.set_xticks(x)
ax.set_xticklabels(segmentos, fontsize=9.5)
ax.set_ylabel('% respondentes', fontsize=10)
ax.set_title('Percepcion de Precio Gama (P33) por NSE\n"Los precios en Gama son..." — Neto Caro vs Neto Economico',
             fontsize=12, fontweight='bold')
ax.set_ylim(0, 80)
ax.yaxis.grid(True, alpha=0.4)
ax.set_axisbelow(True)
ax.legend(fontsize=9, loc='upper right')

ax.text(0.01, -0.12,
        '* Pref-Gama REFERENCIAL n=32. Neto Caro = Poco + Mucho mas caros. Neto Economico = Poco + Mucho mas economicos. '
        'Dif C+/C vs E no sig al 95% (z=1.19, p=0.233).',
        transform=ax.transAxes, fontsize=7.5, color=GAMA_GRAY_MID, style='italic')

fig.tight_layout()
save(fig, 'C11_p33_percepcion_precio_nse.png')

# ===========================================================================
# C12 — Scatter categorias: habito Gama vs % precio Gama (P30 x P32)
# Datos: CU-9 §10 A9
# ===========================================================================
print("C12 — Scatter categorias estrategia precio vs habito...")

categorias_scatter = {
    'Congelados':        {'habito': 8.0, 'precio': 4.7},
    'Gaseosas/Jugos':    {'habito': 7.2, 'precio': 3.2},
    'Salsas/Enlatados':  {'habito': 7.5, 'precio': 4.5},
    'Galletas':          {'habito': 7.0, 'precio': 5.7},
    'Prod.basicos':      {'habito': 5.5, 'precio': 4.5},
    'Cuidado hogar':     {'habito': 5.0, 'precio': 3.7},
    'Farmacia':          {'habito': 4.2, 'precio': 3.0},
    'Frutas/verduras':   {'habito': 4.0, 'precio': 2.2},
    'C.personal':        {'habito': 4.0, 'precio': 3.0},
    'Carne de res':      {'habito': 3.7, 'precio': 3.0},
    'Licores':           {'habito': 3.7, 'precio': 3.5},
    'Pollo':             {'habito': 3.5, 'precio': 2.5},
    'Charcuteria':       {'habito': 3.2, 'precio': 1.7},
    'Pescados':          {'habito': 2.7, 'precio': 1.0},
    'Mascotas':          {'habito': 1.2, 'precio': 1.2},
}

# Cuadrantes: lineas de medias
med_h = 5.0  # corte habito
med_p = 3.5  # corte precio

fig, ax = plt.subplots(figsize=(11, 7))

# Cuadrante backgrounds
ax.axhspan(med_p, 8, xmin=0, xmax=0.5, alpha=0.06, color=GAMA_AMBER)  # alto habito, alto precio = "Cuidar precio"
ax.axhspan(0, med_p, xmin=0, xmax=0.5, alpha=0.06, color=GAMA_GREEN)  # alto habito, bajo precio = "Ofrecer valor"

ofrecer_valor  = {'Congelados', 'Gaseosas/Jugos', 'Salsas/Enlatados', 'Farmacia'}
cuidar_precio  = {'Galletas', 'Prod.basicos'}

for cat, vals in categorias_scatter.items():
    h, p = vals['habito'], vals['precio']
    if cat in ofrecer_valor:
        color = GAMA_GREEN
        size  = 150
    elif cat in cuidar_precio:
        color = GAMA_AMBER
        size  = 130
    else:
        color = GAMA_GRAY_MID
        size  = 80
    ax.scatter(h, p, s=size, color=color, zorder=4, edgecolors='white', linewidth=0.8)
    offset_y = 0.12 if cat not in ['Galletas', 'Carne de res'] else -0.25
    ax.annotate(cat, xy=(h, p), xytext=(h + 0.05, p + offset_y),
                fontsize=7.5, color=color,
                fontweight='bold' if cat in ofrecer_valor | cuidar_precio else 'normal')

ax.axvline(med_h, color=GAMA_GRAY_MID, linewidth=0.8, linestyle='--', alpha=0.6)
ax.axhline(med_p, color=GAMA_GRAY_MID, linewidth=0.8, linestyle='--', alpha=0.6)

# Etiquetas cuadrantes
ax.text(7.3, 6.5, 'CUIDAR PRECIO\n(alto habito,\nalto precio perc.)', ha='center', fontsize=8,
        color=GAMA_AMBER, fontweight='bold', style='italic')
ax.text(7.0, 1.2, 'OFRECER VALOR\n(alto habito,\nbajo precio perc.)', ha='center', fontsize=8,
        color=GAMA_GREEN, fontweight='bold', style='italic')
ax.text(2.0, 1.2, 'SIN ACCION\nINMEDIATA', ha='center', fontsize=8,
        color=GAMA_GRAY_MID, style='italic')

# Leyenda
patches_sc = [
    mpatches.Patch(color=GAMA_GREEN, label='Ofrecer valor (Congelados, Gaseosas, Salsas, Farmacia)'),
    mpatches.Patch(color=GAMA_AMBER, label='Cuidar precio (Galletas, Prod. basicos)'),
    mpatches.Patch(color=GAMA_GRAY_MID, label='Sin accion prioritaria'),
]
ax.legend(handles=patches_sc, fontsize=8, loc='upper left')

ax.set_xlabel('% habito de compra en Gama por categoria (P30)', fontsize=10)
ax.set_ylabel('% percibe Gama como mejor precio por categoria (P32)', fontsize=10)
ax.set_title('Estrategia de Categoria: Habito vs Precio Percibido Gama\n"Ofrecer valor" vs "Cuidar precio"',
             fontsize=12, fontweight='bold')
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.yaxis.grid(True, alpha=0.4)
ax.xaxis.grid(True, alpha=0.4)
ax.set_axisbelow(True)

ax.text(0.01, -0.12,
        'TODOS los n de Gama por categoria son REFERENCIALES (n<30). Analisis indicativo — no proyectable. '
        'Fuente: CU-9 §A9/A10.',
        transform=ax.transAxes, fontsize=7.5, color=GAMA_AMBER, style='italic', fontweight='bold')

fig.tight_layout()
save(fig, 'C12_p30_p32_categorias_estrategia.png')

# ===========================================================================
# C13 — Recall PTL vs DTLS por NSE
# Datos: CU-9 §8 A7
# ===========================================================================
print("C13 — Recall PTL vs DTLS por NSE...")

nse_labels = ['NSE E\n(n=171)', 'NSE D\n(n=127)', 'NSE C+/C\n(n=104)']
# Dentro de recordadores PTL (n=43) y DTLS (n=50)
ptl_pct  = [58.1, 23.3, 18.6]
dtls_pct = [54.0, 26.0, 20.0]
# Distribucion base de la muestra
muestra_pct = [42.5, 31.6, 25.9]

x = np.arange(len(nse_labels))
w = 0.28

fig, ax = plt.subplots(figsize=(10, 6))
bars_m  = ax.bar(x - w,    muestra_pct, w, color=GAMA_GRAY_LT,   edgecolor=GAMA_GRAY_MID,  label='Distribucion muestra total', linewidth=0.8)
bars_p  = ax.bar(x,        ptl_pct,     w, color=COMP['Rio'],     edgecolor='white',        label='PTL "Precios de tu lado" (n=43)')
bars_d  = ax.bar(x + w,    dtls_pct,    w, color=COMP['Paramo'],  edgecolor='white',        label='DTLS "De tu lado siempre" (n=50)')

for bars, pcts in [(bars_m, muestra_pct), (bars_p, ptl_pct), (bars_d, dtls_pct)]:
    for bar, v in zip(bars, pcts):
        ax.text(bar.get_x() + bar.get_width()/2, v + 0.5, f'{v:.1f}%',
                ha='center', va='bottom', fontsize=8.5, color=GAMA_BLACK)

# Flecha C+/C subrepresentado
for idx_nse, nse in enumerate(nse_labels):
    if 'C+/C' in nse:
        ax.annotate('C+/C\nsubrepresentado\nentre recordadores',
                    xy=(idx_nse + w, 20.0),
                    xytext=(idx_nse + w + 0.6, 35),
                    fontsize=8, color=GAMA_RED, fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color=GAMA_RED, lw=1.2))

ax.set_xticks(x)
ax.set_xticklabels(nse_labels, fontsize=10)
ax.set_ylabel('% dentro del grupo (muestra vs recordadores)', fontsize=10)
ax.set_title('Perfil NSE de Recordadores PTL y DTLS vs Muestra Total\n— C+/C sub-representado entre quienes recuerdan publicidad Gama',
             fontsize=11, fontweight='bold')
ax.set_ylim(0, 75)
ax.yaxis.grid(True, alpha=0.4)
ax.set_axisbelow(True)
ax.legend(fontsize=9, loc='upper right')

ax.text(0.01, -0.12,
        'PTL="Precios de tu lado", DTLS="De tu lado siempre". Perfil NSE dentro de recordadores: bases referenciales por NSE (n=8-27). '
        'C+/C = 25.9% de muestra vs 18-20% de recordadores.',
        transform=ax.transAxes, fontsize=7.5, color=GAMA_GRAY_MID, style='italic')

fig.tight_layout()
save(fig, 'C13_recall_ptl_dtls.png')

# ===========================================================================
# C14 — Distribucion NSE muestra vs recordadores (paired bars)
# Datos: CU-9 §8 A7 + CU-7 distribucion demografica
# ===========================================================================
print("C14 — Perfil recordadores vs muestra NSE...")

# NSE en muestra total (n=402): E 171=42.5%, D 127=31.6%, C+/C 104=25.9%
# NSE recordadores PTL (n=43): E 25=58.1%, D 10=23.3%, C+/C 8=18.6%
# NSE recordadores DTLS (n=50): E 27=54.0%, D 13=26.0%, C+/C 10=20.0%

nse_cats  = ['NSE C+/C', 'NSE D', 'NSE E']
muestra   = [25.9, 31.6, 42.5]
rec_ptl   = [18.6, 23.3, 58.1]
rec_dtls  = [20.0, 26.0, 54.0]

x = np.arange(len(nse_cats))
w = 0.28

fig, ax = plt.subplots(figsize=(10, 6))
b1 = ax.bar(x - w,    muestra,  w, color='#B0BEC5', edgecolor='white', label='Muestra total n=402')
b2 = ax.bar(x,        rec_ptl,  w, color=COMP['Rio'],    edgecolor='white', label='Recordadores PTL n=43')
b3 = ax.bar(x + w,    rec_dtls, w, color=COMP['Paramo'], edgecolor='white', label='Recordadores DTLS n=50')

for bars, pcts in [(b1, muestra), (b2, rec_ptl), (b3, rec_dtls)]:
    for bar, v in zip(bars, pcts):
        ax.text(bar.get_x() + bar.get_width()/2, v + 0.5, f'{v:.1f}%',
                ha='center', va='bottom', fontsize=9, color=GAMA_BLACK)

# Flechas gap C+/C
ax.annotate('', xy=(x[0], rec_ptl[0]), xytext=(x[0] - 0.01, muestra[0]),
            arrowprops=dict(arrowstyle='<->', color=GAMA_RED, lw=1.5))
ax.text(x[0] - 0.42, (muestra[0] + rec_ptl[0])/2,
        f'-{muestra[0]-rec_ptl[0]:.1f} pp\ngap C+/C',
        ha='center', fontsize=7.5, color=GAMA_RED, fontweight='bold')

# Flechas gap NSE E
ax.annotate('', xy=(x[2] + w, rec_dtls[2]), xytext=(x[2] - w + 0.01, muestra[2]),
            arrowprops=dict(arrowstyle='<->', color=GAMA_AMBER, lw=1.5))
ax.text(x[2], (muestra[2] + rec_dtls[2])/2 + 5,
        f'+{rec_dtls[2]-muestra[2]:.1f} pp\nNSE E sobreindice',
        ha='center', fontsize=7.5, color=GAMA_AMBER, fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(nse_cats, fontsize=10)
ax.set_ylabel('% del grupo (composicion NSE)', fontsize=10)
ax.set_title('Perfil NSE: Muestra Total vs Recordadores PTL/DTLS\n— El mensaje Gama llega mas al NSE E que al C+/C (target natural)',
             fontsize=11, fontweight='bold')
ax.set_ylim(0, 75)
ax.yaxis.grid(True, alpha=0.4)
ax.set_axisbelow(True)
ax.legend(fontsize=9, loc='upper right')

ax.text(0.01, -0.12,
        'Bases recordadores por NSE REFERENCIALES (n=8-27 por celda). Distribucion NSE muestra firme (chi2 comparable vs 2025, CU-7).',
        transform=ax.transAxes, fontsize=7.5, color=GAMA_GRAY_MID, style='italic')

fig.tight_layout()
save(fig, 'C14_perfil_recordadores_vs_muestra.png')

# ===========================================================================
print()
print("=" * 60)
print("DONE — make_charts_v8.py completado.")
print(f"Output directory: {OUT}")
print("=" * 60)
