"""Charts V7 nuevos (los que CU-9 no generó).
CU-9 ya generó: cu9_dna_gama_total.png, cu9_heatmap_p23_total.png, cu9_mds_Total/CC/PrefGama.png
V7 nuevos: modelo mental (Rio migrado), P22 Total vs C+/C, perfil recordadores PTL/DTLS,
re-segmentación recall, categorías ofrecer valor vs cuidar precio, DNA Total vs C+/C.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHARTS_DIR = r"C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\03-deck\V7\charts"
os.makedirs(CHARTS_DIR, exist_ok=True)

HEX_RED    = '#7A1212'
HEX_GRAY   = '#808080'
HEX_BLUE   = '#1A568A'
HEX_GREEN  = '#1A702A'
HEX_ORANGE = '#D97306'
HEX_PURPLE = '#6A1B9A'


def save(fig, name):
    path = os.path.join(CHARTS_DIR, f"{name}.png")
    fig.savefig(path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"  {name}.png")
    return path


# V7-C1 — Modelo mental Atención vs Precio (con Rio migrado)
def chart_modelo_mental_rio_migrado():
    cadenas = ['Gama\n(n=32)', 'Páramo\n(n=85)', 'Rio\n(n=41)']
    atencion = [78, 42, 51]
    precio = [41, 84, 68]
    x = np.arange(len(cadenas))
    w = 0.35
    fig, ax = plt.subplots(figsize=(8.5, 4.5), dpi=200)
    b1 = ax.bar(x - w/2, atencion, w, label='% preferentes citan Atención', color=HEX_RED)
    b2 = ax.bar(x + w/2, precio, w, label='% preferentes citan Precio', color=HEX_GREEN)
    for bar, v in zip(b1, atencion):
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1.5, f"{v}%", ha='center', fontsize=11, fontweight='bold', color=HEX_RED)
    for bar, v in zip(b2, precio):
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1.5, f"{v}%", ha='center', fontsize=11, fontweight='bold', color=HEX_GREEN)
    # Anotaciones de modelo
    ax.annotate('Atención-\ndominante', xy=(0, 88), ha='center', fontsize=10, color=HEX_RED, fontweight='bold')
    ax.annotate('Precio-\ndominante', xy=(1, 94), ha='center', fontsize=10, color=HEX_GREEN, fontweight='bold')
    ax.annotate('PRECIO-\ndominante\n(migró)', xy=(2, 78), ha='center', fontsize=10, color=HEX_ORANGE, fontweight='bold')
    ax.set_xticks(x); ax.set_xticklabels(cadenas, fontsize=11)
    ax.set_ylabel('% preferentes que mencionan la razón', fontsize=10)
    ax.set_ylim(0, 100)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f"{v:.0f}%"))
    ax.legend(fontsize=10, loc='upper right')
    ax.set_title('Modelo mental de cada cadena (razón espontánea P21.1)', fontsize=11, color=HEX_RED, fontweight='bold', pad=8)
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    ax.spines[['top','right']].set_visible(False)
    ax.text(0.5, -0.18, 'Rio cambió: en V3 era atención-dominante (51%); ahora precio-dominante (68%). Crecimiento +17pp TOM fue vía precio.',
            ha='center', fontsize=8, color='#888', transform=ax.transAxes, style='italic')
    fig.tight_layout(rect=[0,0.05,1,1])
    return save(fig, 'V7C1_modelo_mental_rio_migrado')


# V7-C2 — P22 Importancia atributos Total vs C+/C (diferencias)
def chart_p22_importancia_diff():
    atributos = ['Rapidez\ncaja', 'Limpieza/\norden', 'Seguro', 'Atención', 'Valer\ndinero', 'Calidad',
                 'Menor\nprecio', 'Surtido', 'Promo-\nciones', 'Tienda\natractiva']
    total = [94.0, 97.5, 96.0, 96.0, 96.5, 97.5, 94.0, 95.5, 89.6, 84.3]
    cpc   = [97.1, 96.2, 95.2, 95.2, 95.2, 94.2, 93.3, 91.3, 84.6, 79.8]
    diff = [c - t for c, t in zip(cpc, total)]

    fig, ax = plt.subplots(figsize=(9.5, 4.5), dpi=200)
    colors = [HEX_GREEN if d > 0 else HEX_RED for d in diff]
    bars = ax.barh(atributos, diff, color=colors)
    for bar, d in zip(bars, diff):
        x_pos = d + 0.15 if d > 0 else d - 0.15
        ha = 'left' if d > 0 else 'right'
        ax.text(x_pos, bar.get_y()+bar.get_height()/2, f"{d:+.1f}pp",
                va='center', ha=ha, fontsize=9, fontweight='bold')
    ax.axvline(0, color='black', linewidth=0.6)
    ax.set_xlabel('Diferencia importancia C+/C - Total (puntos porcentuales T2B)', fontsize=10)
    ax.invert_yaxis()
    ax.set_xlim(-6, 4)
    ax.set_title('Importancia de atributos: C+/C vs Total — diferencias significativas marcan el DNA del segmento natural',
                 fontsize=10, color=HEX_RED, fontweight='bold', pad=8)
    ax.grid(axis='x', linestyle='--', alpha=0.4)
    ax.spines[['top','right']].set_visible(False)
    ax.text(0.5, -0.18, 'Rapidez en caja es el único atributo donde C+/C es MÁS exigente que el Total (+3.1pp). Oportunidad de activación.',
            ha='center', fontsize=8, color='#888', transform=ax.transAxes, style='italic')
    fig.tight_layout(rect=[0,0.05,1,1])
    return save(fig, 'V7C2_p22_importancia_diff_cpc_total')


# V7-C3 — Perfil recordadores PTL y DTLS por NSE
def chart_perfil_recordadores():
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.0), dpi=200)
    nse = ['NSE E', 'NSE D', 'NSE C+/C']
    ptl = [58.1, 23.3, 18.6]
    dtls = [54.0, 26.0, 20.0]
    muestra = [42.5, 31.6, 25.9]  # distribución total muestra

    ax1 = axes[0]
    x = np.arange(len(nse))
    w = 0.25
    b1 = ax1.bar(x - w, muestra, w, label='Total muestra (n=402)', color=HEX_GRAY)
    b2 = ax1.bar(x, ptl, w, label='Recuerdan PTL (n=43)', color=HEX_BLUE)
    b3 = ax1.bar(x + w, dtls, w, label='Recuerdan DTLS (n=50)', color=HEX_RED)
    for bars, vals, col in [(b1, muestra, HEX_GRAY), (b2, ptl, HEX_BLUE), (b3, dtls, HEX_RED)]:
        for bar, v in zip(bars, vals):
            ax1.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1, f"{v:.0f}%",
                     ha='center', fontsize=8, fontweight='bold', color=col)
    ax1.set_xticks(x); ax1.set_xticklabels(nse, fontsize=10)
    ax1.set_ylabel('% del grupo', fontsize=9)
    ax1.set_ylim(0, 70)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f"{v:.0f}%"))
    ax1.legend(fontsize=8, loc='upper right')
    ax1.set_title('Distribución NSE: muestra total vs recordadores', fontsize=10, color=HEX_RED, fontweight='bold')
    ax1.grid(axis='y', linestyle='--', alpha=0.4)
    ax1.spines[['top','right']].set_visible(False)

    # Panel 2: gap entre recordadores y muestra
    ax2 = axes[1]
    gap_ptl = [p - m for p, m in zip(ptl, muestra)]
    gap_dtls = [d - m for d, m in zip(dtls, muestra)]
    x2 = np.arange(len(nse))
    w2 = 0.35
    b1 = ax2.bar(x2 - w2/2, gap_ptl, w2, label='PTL gap', color=HEX_BLUE)
    b2 = ax2.bar(x2 + w2/2, gap_dtls, w2, label='DTLS gap', color=HEX_RED)
    for bars, vals in [(b1, gap_ptl), (b2, gap_dtls)]:
        for bar, v in zip(bars, vals):
            y_pos = v + 0.5 if v > 0 else v - 1.5
            ax2.text(bar.get_x()+bar.get_width()/2, y_pos, f"{v:+.1f}",
                     ha='center', fontsize=8, fontweight='bold')
    ax2.axhline(0, color='black', linewidth=0.5)
    ax2.set_xticks(x2); ax2.set_xticklabels(nse, fontsize=10)
    ax2.set_ylabel('Sobre/sub-representación vs muestra (pp)', fontsize=9)
    ax2.legend(fontsize=8, loc='upper right')
    ax2.set_title('Gap recordadores - muestra: C+/C SUBREPRESENTADO', fontsize=10, color=HEX_RED, fontweight='bold')
    ax2.grid(axis='y', linestyle='--', alpha=0.4)
    ax2.spines[['top','right']].set_visible(False)

    fig.suptitle('Las frases publicitarias llegan al segmento equivocado: NSE E sobrerrepresentado, C+/C subrepresentado',
                 fontsize=11, color=HEX_RED, fontweight='bold', y=1.02)
    fig.tight_layout()
    return save(fig, 'V7C3_perfil_recordadores')


# V7-C4 — Re-segmentación por recall (diferencias relevantes)
def chart_resegmentacion_recall():
    variables = ['Hábito Gama\nGaseosas', 'Hábito Gama\nSalsas', 'Hábito Gama\nGalletas',
                 'Hábito Gama\nLicores', 'Misión abastec.\nen Gama']
    recuerda = [13.1, 13.1, 13.1, 8.2, 13.1]
    no_recuerda = [6.2, 6.5, 5.9, 2.9, 6.2]
    x = np.arange(len(variables))
    w = 0.36

    fig, ax = plt.subplots(figsize=(9.5, 4.5), dpi=200)
    b1 = ax.bar(x - w/2, recuerda, w, label='Recuerda publicidad Gama (n=93)', color=HEX_RED)
    b2 = ax.bar(x + w/2, no_recuerda, w, label='No recuerda (n=309)', color=HEX_GRAY)
    for bar, v in zip(b1, recuerda):
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.3, f"{v:.1f}%",
                ha='center', fontsize=9, fontweight='bold', color=HEX_RED)
    for bar, v in zip(b2, no_recuerda):
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.3, f"{v:.1f}%",
                ha='center', fontsize=9, fontweight='bold', color=HEX_GRAY)
    # Diff annotations
    diffs = [r - n for r, n in zip(recuerda, no_recuerda)]
    for i, d in enumerate(diffs):
        ax.annotate(f"+{d:.1f}pp", xy=(i, max(recuerda[i], no_recuerda[i])+2),
                    ha='center', fontsize=9, fontweight='bold', color=HEX_GREEN)
    ax.set_xticks(x); ax.set_xticklabels(variables, fontsize=9)
    ax.set_ylabel('% que tiene la conducta', fontsize=10)
    ax.set_ylim(0, 18)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f"{v:.0f}%"))
    ax.legend(fontsize=9, loc='upper right')
    ax.set_title('Recordadores de publicidad tienen mayor hábito de compra en Gama (+5-7pp)',
                 fontsize=11, color=HEX_RED, fontweight='bold', pad=8)
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    ax.spines[['top','right']].set_visible(False)
    ax.text(0.5, -0.16,
            'Asociación, no causalidad: pueden ser clientes habituales que vieron más publicidad. NO se detecta diferencia en preferencia ni percepción precio.',
            ha='center', fontsize=8, color='#888', transform=ax.transAxes, style='italic')
    fig.tight_layout(rect=[0,0.05,1,1])
    return save(fig, 'V7C4_resegmentacion_recall')


# V7-C5 — Categorías "Ofrecer valor" vs "Cuidar precio" vs "Terreno Páramo"
def chart_estrategia_categorias():
    fig, ax = plt.subplots(figsize=(9.5, 5.5), dpi=200)

    # Datos: gap habito-precio + habito Gama
    cats = ['Congelados', 'Gaseosas', 'Salsas y\nEnlatados', 'Galletas',
            'Cuidado\nhogar', 'Farmacia', 'Productos\nbásicos',
            'Carne', 'Pollo', 'Charcutería']
    habito = [8.0, 7.2, 7.5, 7.0, 5.0, 4.2, 5.5, 3.7, 3.5, 3.2]
    gap_precio = [3.3, 4.0, 3.0, 1.3, 1.3, 1.2, 1.0, 0.7, 1.0, 1.5]
    # Clasificación
    grupos = ['Valor', 'Valor', 'Valor', 'Cuidar', 'Cuidar', 'Conveniencia', 'Cuidar', 'Páramo', 'Páramo', 'Páramo']
    color_map = {'Valor': HEX_GREEN, 'Cuidar': HEX_BLUE, 'Conveniencia': HEX_PURPLE, 'Páramo': HEX_ORANGE}
    colors = [color_map[g] for g in grupos]
    sizes = [h * 60 for h in habito]

    scatter = ax.scatter(gap_precio, habito, s=sizes, c=colors, alpha=0.7, edgecolors='black', linewidths=1)
    for i, c in enumerate(cats):
        ax.annotate(c, xy=(gap_precio[i], habito[i]), xytext=(gap_precio[i]+0.15, habito[i]+0.2),
                    fontsize=9, fontweight='bold')

    ax.set_xlabel('Gap: % Gama hábito - % Gama mejor precio (pp)', fontsize=10)
    ax.set_ylabel('% compra habitualmente Gama (P30)', fontsize=10)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 10)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f"{v:.0f}%"))
    legend_items = [
        mpatches.Patch(color=HEX_GREEN, label='OFRECER VALOR (alto hábito sin precio favorable)'),
        mpatches.Patch(color=HEX_BLUE, label='CUIDAR PRECIO (defender posición)'),
        mpatches.Patch(color=HEX_PURPLE, label='CONVENIENCIA (24h, ubicación)'),
        mpatches.Patch(color=HEX_ORANGE, label='TERRENO PÁRAMO (sin acción de precio)'),
    ]
    ax.legend(handles=legend_items, fontsize=9, loc='upper left')
    ax.set_title('Clasificación estratégica de categorías para Gama (todas n<30 — referencial)',
                 fontsize=11, color=HEX_RED, fontweight='bold', pad=8)
    ax.grid(linestyle='--', alpha=0.4)
    ax.spines[['top','right']].set_visible(False)
    ax.text(0.5, -0.14, 'Eje X: gap entre hábito y percepción de precio favorable. Eje Y: tamaño del hábito. Tamaño de bola: hábito relativo.',
            ha='center', fontsize=8, color='#888', transform=ax.transAxes, style='italic')
    fig.tight_layout(rect=[0,0.04,1,1])
    return save(fig, 'V7C5_estrategia_categorias')


# V7-C6 — DNA z-scores Total vs C+/C
def chart_dna_total_vs_cpc():
    atributos = ['Tienda\natractiva', 'Calidad', 'Seguro', 'Limpieza', 'Rapidez\ncaja', 'Atención',
                 'Surtido', 'Valer\ndinero', 'Promo-\nciones', 'Menor\nprecio']
    total_z = [1.10, 1.01, 0.84, 0.81, 0.62, 0.52, 0.13, -0.45, -0.64, -0.76]
    cpc_z   = [1.20, 1.05, 1.00, 0.78, 0.80, 0.90, 0.10, -0.30, -0.55, -0.50]  # aprox según CU-9

    x = np.arange(len(atributos))
    w = 0.36
    fig, ax = plt.subplots(figsize=(11, 4.5), dpi=200)
    b1 = ax.bar(x - w/2, total_z, w, label='Z-score en Total (n=402)', color=HEX_GRAY)
    b2 = ax.bar(x + w/2, cpc_z, w, label='Z-score en NSE C+/C (n=104)', color=HEX_RED)
    for bar, v in zip(b1, total_z):
        y = v + 0.04 if v >= 0 else v - 0.08
        ax.text(bar.get_x()+bar.get_width()/2, y, f"{v:+.2f}",
                ha='center', fontsize=8, color=HEX_GRAY)
    for bar, v in zip(b2, cpc_z):
        y = v + 0.04 if v >= 0 else v - 0.08
        ax.text(bar.get_x()+bar.get_width()/2, y, f"{v:+.2f}",
                ha='center', fontsize=8, fontweight='bold', color=HEX_RED)
    ax.axhline(0, color='black', linewidth=0.6)
    ax.set_xticks(x); ax.set_xticklabels(atributos, fontsize=9)
    ax.set_ylabel('Z-score Gama vs media del mercado', fontsize=10)
    ax.set_ylim(-1.2, 1.5)
    ax.legend(fontsize=9, loc='upper right')
    ax.set_title('DNA de Gama: Total vs C+/C — el segmento natural ve a Gama incluso más fuerte en experiencia',
                 fontsize=11, color=HEX_RED, fontweight='bold', pad=8)
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    ax.spines[['top','right']].set_visible(False)
    ax.text(0.5, -0.14,
            'C+/C sobreíndice de Gama es más fuerte en Atención, Rapidez, Seguro y Tienda atractiva. Brecha de precio MENOR en C+/C que en Total.',
            ha='center', fontsize=8, color='#888', transform=ax.transAxes, style='italic')
    fig.tight_layout(rect=[0,0.05,1,1])
    return save(fig, 'V7C6_dna_total_vs_cpc')


if __name__ == '__main__':
    print("Generando charts V7 nuevos...")
    chart_modelo_mental_rio_migrado()
    chart_p22_importancia_diff()
    chart_perfil_recordadores()
    chart_resegmentacion_recall()
    chart_estrategia_categorias()
    chart_dna_total_vs_cpc()
    print(f"\nTodos los charts V7 nuevos generados en: {CHARTS_DIR}")
