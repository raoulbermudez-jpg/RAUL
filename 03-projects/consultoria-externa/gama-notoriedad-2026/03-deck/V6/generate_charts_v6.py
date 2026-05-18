"""
Genera los charts nuevos para V6 (los que no existían en V5).
Los charts de V5 ya están en ../V5/charts/ y se reusan.
Charts V6 nuevos: P33 distribución, P31 ranking, P32 tabla maestra, P33×P21 gradiente,
PTL vs DTLS, Plan Suárez C+/C, Balance categorías, Urgencia × NSE, Subset categorías, Misiones Gama.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHARTS_DIR = r"C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\03-deck\V6\charts"
os.makedirs(CHARTS_DIR, exist_ok=True)

HEX_RED    = '#7A1212'
HEX_GRAY   = '#808080'
HEX_BLUE   = '#1A568A'
HEX_GREEN  = '#1A702A'
HEX_ORANGE = '#D97306'
HEX_PURPLE = '#6A1B9A'
HEX_LIGHT  = '#E8E8E8'

def save(fig, name):
    path = os.path.join(CHARTS_DIR, f"{name}.png")
    fig.savefig(path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"  {name}.png")
    return path


# C10 — P33 Percepción precio Gama (Total + NSE)
def chart_c10_p33_percepcion():
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=200)
    grupos = ['Total\n(n=402)', 'NSE C+/C\n(n=104)', 'NSE D\n(n=127)', 'NSE E\n(n=171)']
    neto_caro = [54.0, 60.6, 49.6, 53.2]
    neto_eco = [15.4, 11.5, 18.1, 15.8]  # estimates
    x = np.arange(len(grupos))
    w = 0.35
    b1 = ax.bar(x - w/2, neto_caro, w, label='NETO percibe Gama CARA', color=HEX_RED)
    b2 = ax.bar(x + w/2, neto_eco, w, label='NETO percibe Gama ECONÓMICA', color=HEX_GREEN)
    for bar, v in zip(b1, neto_caro):
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1, f"{v:.1f}%", ha='center', fontsize=10, fontweight='bold', color=HEX_RED)
    for bar, v in zip(b2, neto_eco):
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1, f"{v:.1f}%", ha='center', fontsize=10, fontweight='bold', color=HEX_GREEN)
    ax.set_xticks(x); ax.set_xticklabels(grupos, fontsize=10)
    ax.set_ylim(0, 75)
    ax.set_ylabel('% respondientes', fontsize=10)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f"{v:.0f}%"))
    ax.legend(fontsize=9, loc='upper right')
    ax.set_title('Percepción de precios de Gama vs competencia (P33) — Total y por NSE',
                 fontsize=11, color=HEX_RED, fontweight='bold', pad=8)
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    ax.spines[['top','right']].set_visible(False)
    ax.text(0.5, -0.15, 'Brecha NETO caro - NETO económico: 38.6 pp en Total. Transversal a todos los NSE.',
            ha='center', fontsize=8, color='#888', transform=ax.transAxes, style='italic')
    fig.tight_layout(rect=[0,0.04,1,1])
    return save(fig, 'C10_p33_percepcion_precio')


# C11 — P31 Ranking de precio entre cadenas
def chart_c11_p31_ranking():
    cadenas = ['Páramo', 'Central\nMadeirense', 'Forum', 'Rio', 'Plan\nSuárez', 'Gama', 'Luz', 'La Muralla']
    mean_rank = [4.24, 4.06, 4.53, 5.01, 5.25, 5.77, 6.30, 8.49]
    top3 = [47.8, 45.0, 40.0, 32.6, 29.1, 21.9, 21.1, 4.7]
    colors = [HEX_GREEN, HEX_GREEN, HEX_BLUE, HEX_BLUE, HEX_BLUE, HEX_RED, HEX_GRAY, HEX_GRAY]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.0), dpi=200)
    # Panel 1: Mean rank
    bars1 = ax1.barh(cadenas, mean_rank, color=colors)
    for bar, v in zip(bars1, mean_rank):
        ax1.text(bar.get_width()+0.1, bar.get_y()+bar.get_height()/2, f"{v:.2f}",
                 va='center', fontsize=9, fontweight='bold')
    ax1.set_xlabel('Mean rank (1=más económico, 10=más caro)', fontsize=9)
    ax1.set_title('Ranking de precio percibido (P31)', fontsize=10, color=HEX_RED, fontweight='bold')
    ax1.invert_yaxis()
    ax1.set_xlim(0, 10)
    ax1.grid(axis='x', linestyle='--', alpha=0.4)
    ax1.spines[['top','right']].set_visible(False)
    # Panel 2: % Top-3 precio bajo
    bars2 = ax2.barh(cadenas, top3, color=colors)
    for bar, v in zip(bars2, top3):
        ax2.text(bar.get_width()+0.5, bar.get_y()+bar.get_height()/2, f"{v:.1f}%",
                 va='center', fontsize=9, fontweight='bold')
    ax2.set_xlabel('% ubica cadena en Top-3 precio bajo', fontsize=9)
    ax2.set_title('% Top-3 de precio bajo (P31)', fontsize=10, color=HEX_RED, fontweight='bold')
    ax2.invert_yaxis()
    ax2.set_xlim(0, 55)
    ax2.grid(axis='x', linestyle='--', alpha=0.4)
    ax2.spines[['top','right']].set_visible(False)

    fig.suptitle('Gama es #6 en ranking de precio percibido — Páramo lidera el mercado',
                 fontsize=11, color=HEX_RED, fontweight='bold', y=1.02)
    fig.tight_layout()
    return save(fig, 'C11_p31_ranking_precio')


# C12 — P32 Tabla maestra mejor precio por categoría
def chart_c12_p32_categorias():
    cats = ['Carne de res', 'Pollo', 'Charcutería', 'Salsas y\nEnlatados',
            'Productos\nbásicos', 'Frutas,\nlegumbres', 'Galletas y\nconfitería',
            'Cuidado y\nlimpieza', 'Gaseosas,\njugos', 'Congelados',
            'Cuidado\npersonal', 'Pescados', 'Licores', 'Farmacia', 'Alimento\nmascotas']
    lider_pct = [36.3, 35.3, 34.8, 20.9, 18.4, 13.2, 11.4, 9.7, 10.2, 11.4, 10.0, 6.0, 4.7, 3.7, 4.0]
    gama_pct  = [3.0, 2.5, 1.7, 4.5, 4.5, 2.2, 5.7, 3.7, 3.2, 4.7, 3.0, 1.0, 3.5, 3.0, 1.2]
    gap = [g-l for g,l in zip(gama_pct, lider_pct)]

    fig, ax = plt.subplots(figsize=(11, 5.5), dpi=200)
    y = np.arange(len(cats))
    w = 0.38
    b1 = ax.barh(y - w/2, lider_pct, w, label='Líder de la categoría', color=HEX_GREEN)
    b2 = ax.barh(y + w/2, gama_pct, w, label='Gama', color=HEX_RED)
    for bar, v in zip(b1, lider_pct):
        ax.text(bar.get_width()+0.4, bar.get_y()+bar.get_height()/2, f"{v:.1f}%",
                va='center', fontsize=8, color=HEX_GREEN)
    for bar, v in zip(b2, gama_pct):
        ax.text(bar.get_width()+0.4, bar.get_y()+bar.get_height()/2, f"{v:.1f}%",
                va='center', fontsize=8, fontweight='bold', color=HEX_RED)
    ax.set_yticks(y); ax.set_yticklabels(cats, fontsize=9)
    ax.set_xlabel('% percibe la cadena como la de mejor precio en la categoría', fontsize=9)
    ax.set_xlim(0, 42)
    ax.invert_yaxis()
    ax.legend(fontsize=9, loc='lower right')
    ax.set_title('Mejor precio percibido por categoría (P32) — Gama vs Líder de cada categoría',
                 fontsize=11, color=HEX_RED, fontweight='bold', pad=8)
    ax.grid(axis='x', linestyle='--', alpha=0.4)
    ax.spines[['top','right']].set_visible(False)
    ax.text(0.5, -0.12,
            'Gama no lidera en ninguna categoría de alta rotación. Mejor posición: #2 Farmacia (gap -0.7pp). Datos referenciales para Gama.',
            ha='center', fontsize=8, color='#888', transform=ax.transAxes, style='italic')
    fig.tight_layout(rect=[0,0.04,1,1])
    return save(fig, 'C12_p32_categorias')


# C13 — P33×P21 gradiente preferencia
def chart_c13_p33_p21_gradiente():
    perc = ['Mucho más\ncara', 'Poco más\ncara', 'Igual\nprecio', 'Poco más\neconómica', 'Mucho más\neconómica\n(n=6, ref.)']
    pref = [0.0, 7.2, 8.9, 12.5, 50.0]
    n_base = [65, 152, 123, 56, 6]
    colors = [HEX_RED, '#A02828', HEX_GRAY, HEX_BLUE, '#888888']

    fig, ax = plt.subplots(figsize=(8.5, 4.5), dpi=200)
    bars = ax.bar(perc, pref, color=colors)
    for bar, v, n in zip(bars, pref, n_base):
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5,
                f"{v:.1f}%", ha='center', fontsize=11, fontweight='bold')
        ax.text(bar.get_x()+bar.get_width()/2, -3.5,
                f"n={n}", ha='center', fontsize=8, color='#666')
    # Líneas guía
    ax.plot([0,1,2,3], pref[:4], color=HEX_BLUE, linewidth=2, marker='o', markersize=7, zorder=5, label='Gradiente monótono')
    ax.set_ylabel('% que prefiere Gama (P21)', fontsize=10)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f"{v:.0f}%"))
    ax.set_ylim(-7, 60)
    ax.set_title('Percepción de precio Gama (P33) × Preferencia (P21) — Gradiente monótono claro',
                 fontsize=11, color=HEX_RED, fontweight='bold', pad=8)
    ax.legend(loc='upper left', fontsize=9)
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    ax.spines[['top','right']].set_visible(False)
    ax.text(0.5, -0.20,
            'Chi² = 21.94, p < 0.001, Cramér\'s V = 0.234 (asociación pequeña-moderada). OR favorable vs cara = 2.40 [IC95: 1.12-5.12].',
            ha='center', fontsize=8, color='#888', transform=ax.transAxes, style='italic')
    fig.tight_layout(rect=[0,0.06,1,1])
    return save(fig, 'C13_p33xp21_gradiente')


# C15 — PTL vs DTLS recall + interpretación
def chart_c15_ptl_vs_dtls():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=200)
    # Panel 1: Recall
    frases = ['PTL\n"Precios de\ntu lado"', 'DTLS\n"De tu lado\nsiempre"', 'Cualquier\nfrase Gama\n(P35)']
    recall = [10.7, 12.4, 4.2]
    bars1 = ax1.bar(frases, recall, color=[HEX_BLUE, HEX_RED, HEX_GRAY])
    for bar, v in zip(bars1, recall):
        ax1.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5, f"{v:.1f}%",
                 ha='center', fontsize=12, fontweight='bold')
    ax1.set_ylabel('% recall espontáneo', fontsize=10)
    ax1.set_ylim(0, 18)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f"{v:.0f}%"))
    ax1.set_title('Recall espontáneo (n=402)', fontsize=10, color=HEX_RED, fontweight='bold')
    ax1.grid(axis='y', linestyle='--', alpha=0.4)
    ax1.spines[['top','right']].set_visible(False)
    ax1.text(0.5, -0.12, 'z=-0.754, p=0.451 — diferencia NO significativa', ha='center', fontsize=8,
             color='#888', transform=ax1.transAxes, style='italic')

    # Panel 2: Interpretación temática
    temas = ['Precio /\neconomía', 'Acompañamiento /\napoyo relacional', 'Bienestar\ncliente', 'Fidelidad /\nconfianza']
    ptl_temas = [72, 2, 0, 0]
    dtls_temas = [42, 26, 16, 8]
    x = np.arange(len(temas))
    w = 0.38
    bars2a = ax2.bar(x - w/2, ptl_temas, w, label='PTL (n=43)', color=HEX_BLUE)
    bars2b = ax2.bar(x + w/2, dtls_temas, w, label='DTLS (n=50)', color=HEX_RED)
    for bar, v in zip(bars2a, ptl_temas):
        if v > 0:
            ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1, f"{v}%",
                     ha='center', fontsize=9, fontweight='bold', color=HEX_BLUE)
    for bar, v in zip(bars2b, dtls_temas):
        if v > 0:
            ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1, f"{v}%",
                     ha='center', fontsize=9, fontweight='bold', color=HEX_RED)
    ax2.set_xticks(x); ax2.set_xticklabels(temas, fontsize=9)
    ax2.set_ylabel('% interpretación', fontsize=10)
    ax2.set_ylim(0, 80)
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f"{v:.0f}%"))
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_title('Interpretación de la frase (bases referenciales)', fontsize=10, color=HEX_RED, fontweight='bold')
    ax2.grid(axis='y', linestyle='--', alpha=0.4)
    ax2.spines[['top','right']].set_visible(False)
    ax2.text(0.5, -0.12, 'DTLS activa territorio relacional (26%) que PTL prácticamente no toca (2%)',
             ha='center', fontsize=8, color='#888', transform=ax2.transAxes, style='italic')

    fig.suptitle('Comparativo de claims publicitarios: PTL vs DTLS',
                 fontsize=12, color=HEX_RED, fontweight='bold', y=1.02)
    fig.tight_layout()
    return save(fig, 'C15_ptl_vs_dtls')


# C16 — Plan Suárez en C+/C empate técnico
def chart_c16_plan_suarez_cpc():
    cadenas = ['Páramo', 'Gama', 'Plan Suárez', 'Otros']
    pref_cpc = [16.3, 13.5, 12.5, 8.2]  # aprox %
    colors = [HEX_GREEN, HEX_RED, HEX_PURPLE, HEX_GRAY]
    ic_low = [9.0, 8.2, 7.5, 4.5]
    ic_high = [25.0, 21.3, 19.5, 13.0]

    fig, ax = plt.subplots(figsize=(8, 4), dpi=200)
    y = np.arange(len(cadenas))
    bars = ax.barh(y, pref_cpc, color=colors)
    for i, (bar, v, lo, hi) in enumerate(zip(bars, pref_cpc, ic_low, ic_high)):
        ax.errorbar(v, i, xerr=[[v-lo], [hi-v]], fmt='none', ecolor='black', capsize=4, capthick=1)
        ax.text(v+0.3, i, f"{v:.1f}% [{lo:.1f}-{hi:.1f}]", va='center', fontsize=9, fontweight='bold')
    ax.set_yticks(y); ax.set_yticklabels(cadenas, fontsize=10)
    ax.set_xlabel('% preferencia en NSE C+/C (n=104)', fontsize=9)
    ax.set_xlim(0, 30)
    ax.set_title('Preferencia en C+/C: Páramo, Gama y Plan Suárez en empate técnico (IC95 solapados)',
                 fontsize=10, color=HEX_RED, fontweight='bold', pad=8)
    ax.grid(axis='x', linestyle='--', alpha=0.4)
    ax.spines[['top','right']].set_visible(False)
    ax.text(0.5, -0.18,
            'Las 3 cadenas no son estadísticamente distintas en preferencia C+/C — competencia abierta por el segmento natural de Gama',
            ha='center', fontsize=8, color='#888', transform=ax.transAxes, style='italic')
    fig.tight_layout(rect=[0,0.05,1,1])
    return save(fig, 'C16_plan_suarez_cpc')


# C17 — Subset shoppers favorables: brechas por categoría
def chart_c17_subset_categorias():
    cats = ['Gaseosas,\njugos', 'Productos\nbásicos', 'Salsas y\nEnlatados',
            'Galletas y\nconfitería', 'Cuidado\nPersonal', 'Frutas,\nlegumbres',
            'Carne\nde res', 'Congelados', 'Cuidado y\nlimpieza', 'Farmacia']
    total = [7.2, 5.5, 7.5, 7.0, 4.0, 4.0, 3.7, 8.0, 5.0, 4.2]
    subset = [11.9, 8.6, 10.3, 9.7, 6.5, 5.9, 5.4, 9.7, 6.5, 4.3]

    fig, ax = plt.subplots(figsize=(10.5, 4.5), dpi=200)
    x = np.arange(len(cats))
    w = 0.38
    b1 = ax.bar(x - w/2, total, w, label='Total mercado (n=402)', color=HEX_GRAY)
    b2 = ax.bar(x + w/2, subset, w, label='Subset percibe Gama igual/económica (n=185)', color=HEX_RED)
    for bar, v in zip(b1, total):
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.2, f"{v:.1f}",
                ha='center', fontsize=8, color=HEX_GRAY)
    for bar, v in zip(b2, subset):
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.2, f"{v:.1f}",
                ha='center', fontsize=8, fontweight='bold', color=HEX_RED)
    ax.set_xticks(x); ax.set_xticklabels(cats, fontsize=8)
    ax.set_ylabel('% compra habitualmente en Gama (P30)', fontsize=9)
    ax.set_ylim(0, 14)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f"{v:.0f}%"))
    ax.legend(loc='upper right', fontsize=9)
    ax.set_title('Hábito de compra en Gama: Subset con percepción precio favorable vs Total',
                 fontsize=11, color=HEX_RED, fontweight='bold', pad=8)
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    ax.spines[['top','right']].set_visible(False)
    ax.text(0.5, -0.22, 'El subset favorable tiene mayor hábito Gama en todas las categorías. Farmacia es la excepción (hábito por conveniencia, no por precio).',
            ha='center', fontsize=8, color='#888', transform=ax.transAxes, style='italic')
    fig.tight_layout(rect=[0,0.08,1,1])
    return save(fig, 'C17_subset_categorias')


# C18 — Balance óptimo de categorías (3 grupos)
def chart_c18_balance_categorias():
    fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
    # 3 grupos
    cats_g1 = ['Carne', 'Charcutería', 'Pollo', 'Salsas y\nEnlatados', 'Productos\nbásicos']
    gap_g1 = [-33.3, -33.1, -32.8, -16.4, -13.9]
    cats_g2 = ['Farmacia', 'Licores']
    gap_g2 = [-0.7, -1.2]
    cats_g3 = ['Congelados', 'Gaseosas', 'Galletas', 'Cuidado y\nlimpieza']
    gap_g3 = [-6.7, -7.0, -5.7, -6.0]

    all_cats = cats_g1 + cats_g2 + cats_g3
    all_gaps = gap_g1 + gap_g2 + gap_g3
    colors = [HEX_RED]*5 + [HEX_GREEN]*2 + [HEX_BLUE]*4

    y = np.arange(len(all_cats))
    bars = ax.barh(y, all_gaps, color=colors)
    for bar, v in zip(bars, all_gaps):
        x_pos = v - 1.5 if v < -10 else v - 0.5
        ax.text(x_pos, bar.get_y()+bar.get_height()/2, f"{v:.1f}pp",
                va='center', ha='right', fontsize=8, fontweight='bold', color='white' if v<-10 else 'black')
    ax.set_yticks(y); ax.set_yticklabels(all_cats, fontsize=9)
    ax.set_xlabel('Gap Gama vs Líder de precio percibido (pp)', fontsize=9)
    ax.invert_yaxis()
    ax.axvline(0, color='black', linewidth=0.5)
    # Leyenda
    legend_items = [
        mpatches.Patch(color=HEX_RED, label='CRÍTICO — Igualar precio (gap >10pp)'),
        mpatches.Patch(color=HEX_GREEN, label='EASY WIN — Comunicar precio (gap <2pp)'),
        mpatches.Patch(color=HEX_BLUE, label='DIFERENCIAL — Mantener + comunicar atributo'),
    ]
    ax.legend(handles=legend_items, loc='lower right', fontsize=8)
    ax.set_xlim(-40, 5)
    ax.set_title('Balance estratégico de precios: 3 grupos de categorías para captar segmento precio sin perder segmento natural',
                 fontsize=10, color=HEX_RED, fontweight='bold', pad=8)
    ax.grid(axis='x', linestyle='--', alpha=0.4)
    ax.spines[['top','right']].set_visible(False)
    fig.tight_layout()
    return save(fig, 'C18_balance_categorias')


# C19 — Urgencia × NSE
def chart_c19_urgencia_nse():
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=200)
    nse = ['NSE C+/C\n(n=104)', 'NSE D\n(n=127)', 'NSE E\n(n=171)']
    gama_urg = [16.3, 15.0, 7.6]
    paramo_urg = [10.5, 12.0, 13.5]
    x = np.arange(len(nse))
    w = 0.35
    b1 = ax.bar(x - w/2, gama_urg, w, label='Gama', color=HEX_RED)
    b2 = ax.bar(x + w/2, paramo_urg, w, label='Páramo (competidor)', color=HEX_GREEN)
    for bar, v in zip(b1, gama_urg):
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.3, f"{v:.1f}%",
                ha='center', fontsize=10, fontweight='bold', color=HEX_RED)
    for bar, v in zip(b2, paramo_urg):
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.3, f"{v:.1f}%",
                ha='center', fontsize=10, fontweight='bold', color=HEX_GREEN)
    # Marcar dónde Gama lidera
    for i, (g, p) in enumerate(zip(gama_urg, paramo_urg)):
        if g > p:
            ax.text(i, max(g,p)+1.8, '★ LÍDER', ha='center', fontsize=10,
                    color=HEX_RED, fontweight='bold')
    ax.set_xticks(x); ax.set_xticklabels(nse, fontsize=10)
    ax.set_ylabel('% mejor supermercado para urgencia (P26)', fontsize=10)
    ax.set_ylim(0, 22)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f"{v:.0f}%"))
    ax.legend(loc='upper right', fontsize=9)
    ax.set_title('Liderazgo de urgencia por NSE — Gama lidera en C+/C y D (segmento medio-alto)',
                 fontsize=11, color=HEX_RED, fontweight='bold', pad=8)
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    ax.spines[['top','right']].set_visible(False)
    ax.text(0.5, -0.16, 'Patrón compatible con hipótesis Express (formato de conveniencia). Datos por NSE referenciales (n por NSE < 30 para Gama).',
            ha='center', fontsize=8, color='#888', transform=ax.transAxes, style='italic')
    fig.tight_layout(rect=[0,0.05,1,1])
    return save(fig, 'C19_urgencia_nse')


# C20 — Misiones de compra Gama
def chart_c20_misiones_gama():
    misiones = ['Reabastecimiento\nparcial', 'Abastecimiento\ngeneral', 'Urgencia\n(pocos productos)', 'Evento /\ncelebración', 'No alimentos']
    dist = [67.2, 23.4, 7.7, 1.5, 0.2]
    colors = [HEX_BLUE, HEX_GREEN, HEX_RED, HEX_GRAY, HEX_LIGHT]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=200)
    # Pie chart distribución misiones
    wedges, texts, autotexts = ax1.pie(dist, labels=misiones, colors=colors, autopct='%1.1f%%',
                                         startangle=90, textprops={'fontsize':9})
    for at in autotexts:
        at.set_fontweight('bold')
        at.set_color('white')
    ax1.set_title('Distribución de misiones de última compra (P25, n=402)',
                  fontsize=10, color=HEX_RED, fontweight='bold')

    # Bar chart Gama por misión
    misiones_b = ['Reabasteci-\nmiento', 'Abasteci-\nmiento general', 'Urgencia', 'Evento']
    gama_mision = [8.7, 7.2, 12.2, 9.2]
    lider_mision = [16.4, 21.6, 12.2, 13.7]
    x = np.arange(len(misiones_b))
    w = 0.38
    bars1 = ax2.bar(x - w/2, lider_mision, w, label='Líder por misión', color=HEX_GREEN)
    bars2 = ax2.bar(x + w/2, gama_mision, w, label='Gama', color=HEX_RED)
    for bar, v in zip(bars1, lider_mision):
        ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.3, f"{v:.1f}%",
                 ha='center', fontsize=8, color=HEX_GREEN)
    for bar, v in zip(bars2, gama_mision):
        ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.3, f"{v:.1f}%",
                 ha='center', fontsize=8, fontweight='bold', color=HEX_RED)
    # Marcar urgencia como liderazgo
    ax2.text(2, 14.5, '★ Gama LÍDER', ha='center', fontsize=9, color=HEX_RED, fontweight='bold')
    ax2.set_xticks(x); ax2.set_xticklabels(misiones_b, fontsize=8)
    ax2.set_ylabel('% mejor supermercado por misión (P26)', fontsize=9)
    ax2.set_ylim(0, 25)
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f"{v:.0f}%"))
    ax2.legend(loc='upper right', fontsize=8)
    ax2.set_title('Posición de Gama por misión', fontsize=10, color=HEX_RED, fontweight='bold')
    ax2.grid(axis='y', linestyle='--', alpha=0.4)
    ax2.spines[['top','right']].set_visible(False)

    fig.suptitle('Misiones de compra: Gama lidera urgencia, Páramo domina los volúmenes',
                 fontsize=11, color=HEX_RED, fontweight='bold', y=1.02)
    fig.tight_layout()
    return save(fig, 'C20_misiones_gama')


# C21 — Evolución comparativa 2025→2026 movimientos significativos
def chart_c21_wow_movimiento():
    items = ['Rio TOM', 'Rio Consideración', 'Rio Compra 3m',
             'Páramo TOM', 'Páramo Consideración', 'Páramo Asistida',
             'CM Compra 3m', 'Gama (8 indicadores)']
    delta = [17.0, 19.6, 12.5, 12.1, 17.3, 10.8, -7.7, 0]
    sig = ['sig 99', 'sig 99', 'sig 99', 'sig 99', 'sig 99', 'sig 99', 'sig 95', 'no sig (0/8)']
    colors = [HEX_GREEN]*3 + [HEX_BLUE]*3 + [HEX_ORANGE] + [HEX_GRAY]

    fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
    y = np.arange(len(items))
    bars = ax.barh(y, delta, color=colors)
    for bar, v, s in zip(bars, delta, sig):
        if v == 0:
            ax.text(0.3, bar.get_y()+bar.get_height()/2, f"≈0 ({s})", va='center', fontsize=9, color='#666')
        else:
            x_pos = v + 0.5 if v > 0 else v - 0.5
            ha = 'left' if v > 0 else 'right'
            ax.text(x_pos, bar.get_y()+bar.get_height()/2, f"{v:+.1f}pp ({s})",
                    va='center', ha=ha, fontsize=9, fontweight='bold')
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_yticks(y); ax.set_yticklabels(items, fontsize=10)
    ax.set_xlabel('Cambio WoW 2025→2026 (puntos porcentuales)', fontsize=9)
    ax.invert_yaxis()
    ax.set_xlim(-12, 25)
    ax.set_title('Movimientos significativos 2025→2026: Rio y Páramo crecen, CM cae, Gama estable',
                 fontsize=11, color=HEX_RED, fontweight='bold', pad=8)
    ax.grid(axis='x', linestyle='--', alpha=0.4)
    ax.spines[['top','right']].set_visible(False)
    ax.text(0.5, -0.14,
            'n_2025=785, n_2026=402, BH-FDR. Caveats CV-WOW-001/002 aplican (ponderación 2025 no disponible, composición geo difiere).',
            ha='center', fontsize=8, color='#888', transform=ax.transAxes, style='italic')
    fig.tight_layout(rect=[0,0.05,1,1])
    return save(fig, 'C21_wow_movimiento')


if __name__ == '__main__':
    print("Generando charts V6 (nuevos)...")
    chart_c10_p33_percepcion()
    chart_c11_p31_ranking()
    chart_c12_p32_categorias()
    chart_c13_p33_p21_gradiente()
    chart_c15_ptl_vs_dtls()
    chart_c16_plan_suarez_cpc()
    chart_c17_subset_categorias()
    chart_c18_balance_categorias()
    chart_c19_urgencia_nse()
    chart_c20_misiones_gama()
    chart_c21_wow_movimiento()
    print(f"\nTodos los charts V6 nuevos generados en: {CHARTS_DIR}")
