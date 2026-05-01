"""
gsm_empaque_redlines_v4.py
Genera PDFs redline de tiro y retiro para empaque GSM-MB/RB/RF
con anotaciones delta v4 (NTC + Inverter).
Raoul Bermudez — 2026-04-30
"""

import fitz
import sys
sys.stdout.reconfigure(encoding='utf-8')

# ---------------------------------------------------------------------------
# Rutas
# ---------------------------------------------------------------------------
SRC_DIR  = r"C:\Raul\01-inbox\03-raw-sources\genteca\ntc-gsm-hojas-glase"
OUT_DIR  = r"C:\Raul\03-projects\genteca\2026-04_GSM-MB-RB-RF_empaque\03-review-and-release"
TIRO_SRC = SRC_DIR + r"\GSM-MB-RB-RF_GLA_T_ (1).pdf"
RETI_SRC = SRC_DIR + r"\GSM-MB-RB-RF_GLA_R_ (1).pdf"
TIRO_OUT = OUT_DIR + r"\GSM-MB-RB-RF-RE_GLA_T_redline_v4.pdf"
RETI_OUT = OUT_DIR + r"\GSM-MB-RB-RF-RE_GLA_R_redline_v4.pdf"

# ---------------------------------------------------------------------------
# Paleta de colores (RGB 0-1)
# ---------------------------------------------------------------------------
RED    = (0.82, 0.12, 0.12)   # CAMBIAR
ORANGE = (0.88, 0.46, 0.04)   # AGREGAR
GREEN  = (0.08, 0.58, 0.22)   # MANTENER
BLUE   = (0.08, 0.32, 0.78)   # VERIFICAR
WHITE  = (1.0,  1.0,  1.0)
BLACK  = (0.0,  0.0,  0.0)
LGRAY  = (0.92, 0.92, 0.92)

FONT = "helv"


def badge(page, cx, cy, letter, color):
    """Dibuja un circulo con letra de referencia."""
    r = 9
    rect = fitz.Rect(cx - r, cy - r, cx + r, cy + r)
    page.draw_circle(fitz.Point(cx, cy), r, color=color, fill=color, width=1)
    page.insert_text(
        fitz.Point(cx - (6 if len(letter) == 1 else 9), cy + 4),
        letter, fontname=FONT, fontsize=9, color=WHITE
    )


def outlined_rect(page, rect, color, width=2.2):
    """Dibuja rectangulo con borde de color y relleno semitransparente."""
    r = fitz.Rect(rect)
    # Relleno con opacidad simulada (fitz no soporta alpha directo en draw_rect)
    page.draw_rect(r, color=color, fill=None, width=width, dashes="[4 3]")


def callout_box(page, x0, y0, x1, y1, color, label, title, body_lines, font_size=6.8):
    """
    Dibuja caja de callout con fondo gris claro, borde de color,
    título en negrita y cuerpo de instrucciones.
    """
    r = fitz.Rect(x0, y0, x1, y1)
    page.draw_rect(r, color=color, fill=LGRAY, width=1.5)

    # Header strip
    header_h = 14
    hr = fitz.Rect(x0, y0, x1, y0 + header_h)
    page.draw_rect(hr, color=color, fill=color, width=0)
    page.insert_textbox(
        hr, f"  {label}  {title}",
        fontname=FONT, fontsize=7.5, color=WHITE,
        align=0
    )

    # Body
    body_rect = fitz.Rect(x0 + 3, y0 + header_h + 3, x1 - 3, y1 - 3)
    body_text = "\n".join(body_lines)
    page.insert_textbox(
        body_rect, body_text,
        fontname=FONT, fontsize=font_size, color=BLACK,
        align=0
    )


def legend_strip(page, annotations, y0=700):
    """Banda de leyenda al pie de la pagina."""
    x0, x1 = 60, 530
    y1 = y0 + len(annotations) * 22 + 30
    r = fitz.Rect(x0 - 5, y0 - 8, x1 + 5, y1 + 5)
    page.draw_rect(r, color=(0.3, 0.3, 0.3), fill=LGRAY, width=1)

    # Titulo
    page.insert_text(fitz.Point(x0, y0 + 5),
                     "LEYENDA DE CAMBIOS — delta v4 NTC + Inverter",
                     fontname=FONT, fontsize=7.5, color=BLACK)

    # Color key
    kx = x0
    ky = y0 + 14
    for col, lbl in [(RED, "CAMBIAR"), (ORANGE, "AGREGAR"), (GREEN, "MANTENER"), (BLUE, "VERIFICAR")]:
        page.draw_rect(fitz.Rect(kx, ky, kx + 10, ky + 8), color=col, fill=col)
        page.insert_text(fitz.Point(kx + 13, ky + 7), lbl, fontname=FONT, fontsize=6.5, color=BLACK)
        kx += 65

    # Annotations list
    for i, (letter, color, text) in enumerate(annotations):
        y = ky + 14 + i * 16
        badge(page, x0 + 8, y + 4, letter, color)
        page.insert_textbox(
            fitz.Rect(x0 + 22, y - 2, x1, y + 13),
            text, fontname=FONT, fontsize=6.8, color=BLACK, align=0
        )


# ===========================================================================
# TIRO  (frente del blister)
# ===========================================================================
# Coordenadas clave extraidas con get_text("blocks"):
#   Lengueta/cintilla:        y ~ 60-210  (zona vectorial, sin texto extraible)
#   Slogan superior:          y ~ 226-260
#   Tipo de producto:         y ~ 268-323
#   Small badges (texto):     y ~ 332-375
#   Large badge (blister):    y ~ 480-550
#   Info strip inferior:      y ~ 659-690

TIRO_ANNOTATIONS = [
    ("A", RED,    "CAMBIAR LENGUETA — Reemplazar 4 lineas por 2: (1) NUEVO  (2) LA PROTECCION MAS COMPLETA — mismo tamano de fuente ambas"),
    ("B", RED,    "CAMBIAR BADGE 'Bornera para cables hasta AWG 8' — Reemplazar con: 'Autoproteccion termica NTC*' (asterisco = nota al retiro)"),
    ("C", RED,    "CAMBIAR BADGE PRINCIPAL — GSM-MB: reemplazar BORNERA grande. GSM-RB/RF: mantener INVERTER COMPATIBLE, agregar badge 'Protege tecnologia inverter' en jerarquia visible"),
    ("D", BLUE,   "VERIFICAR — GSM-RE: este modelo no figura en el PDF fuente. Aplicar las mismas instrucciones A-B-C con el arte del GSM-RE cuando este disponible"),
]

RETIRO_ANNOTATIONS = [
    ("E", ORANGE, "AGREGAR en CARACTERISTICAS — nuevo bullet al final de la seccion: '• Tiempo de respuesta: < 30 ms — especialmente adecuado para equipos con tecnologia inverter y cargas de arranque corto.'"),
    ("F", ORANGE, "AGREGAR nota asterisco NTC — en area de notas (junto al '(*)' existente): '* Tecnologia NTC: sensor de temperatura incorporado junto al rele de potencia que protege al protector mismo ante calor excesivo.'"),
    ("G", GREEN,  "MANTENER sin cambio — FUNCIONAMIENTO: texto de v3 aprobado. No modificar."),
    ("H", GREEN,  "MANTENER sin cambio — ADVERTENCIA / INFORMACION DE SEGURIDAD: texto de v3 aprobado."),
]


def annotate_tiro_page(page, model_name, page_has_inverter_badge):
    """Anota una pagina del tiro."""
    W = page.rect.width
    H = page.rect.height

    # ------------------------------------------------------------------
    # A — Lengueta / cintilla (zona vectorial, y = 60-205)
    # ------------------------------------------------------------------
    leng_rect = (80, 60, 530, 210)
    outlined_rect(page, leng_rect, RED, width=2.5)
    badge(page, 88, 70, "A", RED)

    callout_box(
        page, 5, 60, 75, 180, RED, "A", "CAMBIAR LENGUETA",
        [
            "Reemplazar contenido actual",
            "de la cintilla por 2 lineas:",
            "",
            "Linea 1: NUEVO",
            "Linea 2: LA PROTECCION",
            "         MAS COMPLETA",
            "",
            "Mismo tamano de fuente",
            "en ambas lineas.",
        ]
    )

    # ------------------------------------------------------------------
    # B — Small badge "Bornera para cables..." (y ~ 340-375)
    # ------------------------------------------------------------------
    sb_y0 = 325
    sb_y1 = 375
    badge_rect = (95, sb_y0, 420, sb_y1)
    outlined_rect(page, badge_rect, RED, width=2.5)
    badge(page, 103, sb_y0 + 10, "B", RED)

    callout_box(
        page, 5, 370, 75, 480, RED, "B", "CAMBIAR BADGE",
        [
            "Reemplazar:",
            "'Bornera para cables',",
            "'Actuacion instantanea'",
            "",
            "Por:",
            "'Autoproteccion termica NTC*'",
            "(*) nota al retiro",
        ]
    )

    # ------------------------------------------------------------------
    # C — Large badge principal (y ~ 475-555)
    # ------------------------------------------------------------------
    lb_rect = (215, 475, 405, 555)
    outlined_rect(page, lb_rect, RED, width=2.5)
    badge(page, 223, 485, "C", RED)

    if page_has_inverter_badge:
        c_title = "MANTENER + AGREGAR"
        c_body = [
            "INVERTER COMPATIBLE",
            "se mantiene.",
            "",
            "Agregar badge adicional:",
            "'Protege tecnologia inverter'",
            "o combinar en el espacio",
            "con 'Autoproteccion termica NTC*'",
            "segun jerarquia visual.",
        ]
        c_color = ORANGE
    else:
        c_title = "CAMBIAR BADGE PRINCIPAL"
        c_body = [
            "Reemplazar BORNERA grande",
            "por 2 badges nuevos:",
            "",
            "Badge 1:",
            "'Autoproteccion termica NTC*'",
            "",
            "Badge 2:",
            "'Protege tecnologia inverter'",
        ]
        c_color = RED

    callout_box(
        page, 5, 480, 75, 600, c_color, "C", c_title, c_body
    )
    if page_has_inverter_badge:
        outlined_rect(page, lb_rect, ORANGE, width=2.5)
        badge(page, 223, 485, "C", ORANGE)

    # ------------------------------------------------------------------
    # Modelo label
    # ------------------------------------------------------------------
    page.insert_text(
        fitz.Point(W - 85, 20),
        f"REDLINE v4 — {model_name}",
        fontname=FONT, fontsize=7, color=RED
    )
    page.insert_text(
        fitz.Point(W - 85, 30),
        "TIRO (frente)",
        fontname=FONT, fontsize=7, color=RED
    )

    # ------------------------------------------------------------------
    # Leyenda
    # ------------------------------------------------------------------
    legend_strip(page, TIRO_ANNOTATIONS, y0=708)


def annotate_retiro_page(page, model_name):
    """Anota una pagina del retiro."""
    W = page.rect.width
    H = page.rect.height

    # ------------------------------------------------------------------
    # E — CARACTERISTICAS section (y ~ 210-270)
    # ------------------------------------------------------------------
    carac_rect = (74, 209, 345, 272)
    outlined_rect(page, carac_rect, ORANGE, width=2.5)
    badge(page, 82, 219, "E", ORANGE)

    callout_box(
        page, 5, 210, 72, 320, ORANGE, "E", "AGREGAR bullet",
        [
            "Al final de CARACTERISTICAS",
            "agregar nuevo bullet:",
            "",
            "Tiempo de respuesta:",
            "< 30 ms — especialmente",
            "adecuado para equipos",
            "con tecnologia inverter",
            "y cargas de arranque corto.",
        ]
    )

    # ------------------------------------------------------------------
    # F — Asterisco NTC — agregar junto al (*) existente (y ~ 240-280)
    # ------------------------------------------------------------------
    ast_rect = (74, 237, 345, 283)
    outlined_rect(page, ast_rect, ORANGE, width=2.0)
    badge(page, 82, 248, "F", ORANGE)

    callout_box(
        page, 5, 322, 72, 430, ORANGE, "F", "AGREGAR nota (*) NTC",
        [
            "En la zona de notas (*)",
            "agregar/ampliar:",
            "",
            "* Tecnologia NTC: sensor",
            "de temperatura junto al",
            "rele de potencia que",
            "protege al protector mismo",
            "ante calor excesivo.",
        ]
    )

    # ------------------------------------------------------------------
    # G — FUNCIONAMIENTO (y ~ 115-242, columna derecha x ~ 355-495)
    # ------------------------------------------------------------------
    func_rect = (352, 113, 498, 245)
    outlined_rect(page, func_rect, GREEN, width=2.0)
    badge(page, 360, 123, "G", GREEN)

    # ------------------------------------------------------------------
    # H — ADVERTENCIA (y ~ 287-365, columna derecha)
    # ------------------------------------------------------------------
    adv_rect = (344, 282, 498, 368)
    outlined_rect(page, adv_rect, GREEN, width=2.0)
    badge(page, 352, 292, "H", GREEN)

    callout_box(
        page, 500, 113, 580, 210, GREEN, "G", "MANTENER",
        [
            "FUNCIONAMIENTO",
            "sin cambio.",
            "Texto v3 aprobado.",
        ], font_size=6.5
    )

    callout_box(
        page, 500, 282, 580, 368, GREEN, "H", "MANTENER",
        [
            "ADVERTENCIA",
            "sin cambio.",
            "Texto v3 aprobado.",
        ], font_size=6.5
    )

    # ------------------------------------------------------------------
    # Modelo label
    # ------------------------------------------------------------------
    page.insert_text(
        fitz.Point(W - 85, 20),
        f"REDLINE v4 — {model_name}",
        fontname=FONT, fontsize=7, color=RED
    )
    page.insert_text(
        fitz.Point(W - 85, 30),
        "RETIRO (reverso)",
        fontname=FONT, fontsize=7, color=RED
    )

    # ------------------------------------------------------------------
    # Leyenda
    # ------------------------------------------------------------------
    legend_strip(page, RETIRO_ANNOTATIONS, y0=700)


# ===========================================================================
# MAIN — generar PDFs
# ===========================================================================

def add_gsm_re_note_page(doc, is_tiro):
    """Agrega pagina de nota para GSM-RE (no disponible en PDF fuente)."""
    page = doc.new_page(width=585.651, height=841.890)
    face = "TIRO (frente)" if is_tiro else "RETIRO (reverso)"

    page.draw_rect(fitz.Rect(40, 40, 545, 800), color=(0.3, 0.3, 0.3), fill=LGRAY, width=1.5)

    page.insert_text(fitz.Point(60, 80),
                     f"REDLINE v4 — GSM-RE — {face}",
                     fontname=FONT, fontsize=14, color=RED)
    page.insert_text(fitz.Point(60, 105),
                     "NOTA: El arte del GSM-RE no figura en el PDF fuente.",
                     fontname=FONT, fontsize=10, color=BLACK)
    page.insert_text(fitz.Point(60, 125),
                     "Instrucciones de cambio: identicas a GSM-RB y GSM-RF.",
                     fontname=FONT, fontsize=10, color=BLACK)

    lines = [
        "Aplicar exactamente las mismas modificaciones documentadas en las paginas anteriores:",
        "",
        "TIRO:",
        "  A. Reemplazar cintilla/lengüeta por: NUEVO / LA PROTECCION MAS COMPLETA",
        "  B. Reemplazar badge 'Bornera para cables...' por: 'Autoproteccion termica NTC*'",
        "  C. Badge principal: mantener INVERTER COMPATIBLE; agregar 'Protege tecnologia inverter'",
        "",
        "RETIRO:",
        "  E. Agregar bullet en CARACTERISTICAS: '< 30 ms — adecuado para equipos inverter'",
        "  F. Agregar nota (*) NTC en zona de notas",
        "  G. FUNCIONAMIENTO: mantener sin cambio (texto v3)",
        "  H. ADVERTENCIA: mantener sin cambio (texto v3)",
        "",
        "Cuando Ozwaldo cuente con el archivo fuente del GSM-RE,",
        "aplicar este delta usando las mismas posiciones de elementos",
        "que en el GSM-RB (modelo mas similar en layout).",
    ] if is_tiro else [
        "Aplicar exactamente las mismas modificaciones del RETIRO documentadas en paginas anteriores.",
        "",
        "Referencia de layout: usar GSM-RB como modelo mas similar.",
    ]

    y = 155
    for line in lines:
        page.insert_text(fitz.Point(70, y), line, fontname=FONT, fontsize=9, color=BLACK)
        y += 16


def generate_tiro():
    src = fitz.open(TIRO_SRC)
    out = fitz.open()

    models = ["GSM-MB", "GSM-RB", "GSM-RF"]
    has_inverter = [False, True, True]  # MB no tiene, RB y RF ya tienen badge inverter

    for i in range(len(src)):
        out.insert_pdf(src, from_page=i, to_page=i)
        page = out[-1]
        annotate_tiro_page(page, models[i], has_inverter[i])

    add_gsm_re_note_page(out, is_tiro=True)
    out.save(TIRO_OUT, garbage=4, deflate=True)
    src.close()
    out.close()
    print(f"Tiro OK -> {TIRO_OUT}")


def generate_retiro():
    src = fitz.open(RETI_SRC)
    out = fitz.open()

    models = ["GSM-MB", "GSM-RB", "GSM-RF"]

    for i in range(len(src)):
        out.insert_pdf(src, from_page=i, to_page=i)
        page = out[-1]
        annotate_retiro_page(page, models[i])

    add_gsm_re_note_page(out, is_tiro=False)
    out.save(RETI_OUT, garbage=4, deflate=True)
    src.close()
    out.close()
    print(f"Retiro OK -> {RETI_OUT}")


if __name__ == "__main__":
    generate_tiro()
    generate_retiro()
    print("Redlines v4 generados correctamente.")
