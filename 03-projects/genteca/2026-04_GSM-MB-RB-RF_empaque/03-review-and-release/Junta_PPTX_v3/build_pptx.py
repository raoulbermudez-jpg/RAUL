"""
build_pptx.py
Generador de presentacion ejecutiva — Junta Directiva Genteca
Proyecto: 2026-04_GSM-MB-RB-RF_empaque
Fecha: 2026-05-06
Fuente principal: AU-1 v2.2 (dual-variantes) + AU-1 v2.1 (caveats invariables)
v3 cambios: paleta V1 verde -> gris neutro; caveats divididos en 1 slide compartida
            + 2 slides termico especificas; anexo IP defensiva (A1-A5).
"""

import sys
sys.stdout.reconfigure(encoding="utf-8")

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt
import os

# ---------------------------------------------------------------------------
# PALETA CORPORATIVA — Genteca / Exceline
# Sin brand kit oficial disponible: paleta industrial profesional
# Azul oscuro institucional + gris plata + blanco + acento amarillo/ambar
# ---------------------------------------------------------------------------
C_AZUL_OSCURO  = RGBColor(0x1A, 0x2E, 0x4A)   # #1A2E4A — fondo portada / headers
C_AZUL_MEDIO   = RGBColor(0x1F, 0x4E, 0x79)   # #1F4E79 — acento secundario
C_AZUL_CLARO   = RGBColor(0xD6, 0xE4, 0xF0)   # #D6E4F0 — fondo cajas contenido
C_AMBAR        = RGBColor(0xF5, 0xA6, 0x23)   # #F5A623 — acento Exceline
C_GRIS_OSCURO  = RGBColor(0x40, 0x40, 0x40)   # #404040 — cuerpo texto
C_GRIS_MEDIO   = RGBColor(0x80, 0x80, 0x80)   # #808080 — texto secundario / caveat
C_GRIS_LINEA   = RGBColor(0xC8, 0xC8, 0xC8)   # #C8C8C8 — lineas separadoras
C_BLANCO       = RGBColor(0xFF, 0xFF, 0xFF)

# V1: gris neutro carbon — reemplaza verde (#1E6B4A) que transmitia "aprobado"
# Eleccion editorial: #5A6470 (gris carbon medio) + #E5E7EA (gris claro)
# Contrasta limpiamente con azul oscuro institucional (#1A2E4A) y ambar (#F5A623)
# sin crear nueva jerarquia cromatica ni confundir con el ambar de acento Exceline.
C_GRIS_V1      = RGBColor(0x5A, 0x64, 0x70)   # #5A6470 — identidad visual V1
C_GRIS_V1_CLR  = RGBColor(0xE5, 0xE7, 0xEA)   # #E5E7EA — fondo suave V1

C_AZUL_V2      = RGBColor(0x1F, 0x4E, 0x79)   # #1F4E79 — identidad visual V2
C_AZUL_V2_CLR  = RGBColor(0xD6, 0xE4, 0xF0)   # #D6E4F0 — fondo suave V2

# Paleta ANEXO — neutra, diferenciada del cuerpo principal
C_ANEXO_HDR    = RGBColor(0x2E, 0x2E, 0x2E)   # #2E2E2E — casi negro, distinto de azul institucional
C_ANEXO_ACENTO = RGBColor(0x8A, 0x6E, 0x3C)   # #8A6E3C — dorado opaco (distinto del ambar brillante Exceline)
C_ANEXO_FONDO  = RGBColor(0xF2, 0xF0, 0xEB)   # #F2F0EB — crema calida — diferencia visual del cuerpo

# Dimensiones slide 16:9
W = Inches(13.333)
H = Inches(7.5)

# ---------------------------------------------------------------------------
# TEXTOS LITERALES DEL EMPAQUE (fuente: AU-1 v2.1 + v2.2)
# ---------------------------------------------------------------------------

# --- TIRO COMPARTIDO ---
TIRO_LENGUETA = "NUEVO\nLA PROTECCION MAS COMPLETA"
TIRO_CLAIM1   = "El mas rapido ante parpadeos (< 0,03 s)"

# --- TIRO diferenciado por variante ---
TIRO_CLAIM2_V1 = "Autoproteccion termica activa*"
TIRO_CLAIM2_V2 = "Escudo Termico NTC*"

# --- RETIRO: CARACTERISTICAS bullets comunes ---
CARACT_COMUNES = [
    "- El mas rapido ante parpadeos: tiempo de respuesta < 30 ms (< 0,03 s),\n"
    "  especialmente adecuado para equipos con tecnologia inverter y cargas de arranque corto.",
    "- Protege tecnologia Inverter: la velocidad de respuesta de < 0,03 s minimiza la exposicion\n"
    "  de la electronica de control inverter a condiciones de inestabilidad de red.",
    # bullet termico va aqui segun variante
    "- Curva de disparo de tiempo inverso: respuesta mas rapida ante mayor sobrecarga --\n"
    "  configuracion tecnica complementaria al breaker termomagnetico del circuito.",
    "- Protege contra sobre voltaje, bajo voltaje, parpadeos e inestabilidad de la red electrica.",
    "- Supresor de picos incorporado.",
    "- Temporizado inteligente de reconexion.",
]

CARACT_TERMICO_V1 = (
    "- Autoproteccion termica activa*: autoproteccion del protector y del cableado de la\n"
    "  instalacion ante corrientes excesivas o conexiones deficientes."
)
CARACT_TERMICO_V2 = (
    "- Escudo Termico NTC*: autoproteccion del protector y del cableado de la\n"
    "  instalacion ante corrientes excesivas o conexiones deficientes."
)

INFO_SEGURIDAD = "No reemplaza los breakers termomagneticos de la instalacion electrica."

# --- CAVEATS INVARIABLES (AU-1 v2.1 §5 — texto literal Bruna) ---
CAVEAT_VELOCIDAD = (
    "*El tiempo de desconexion de menos de 30 milisegundos (< 0,03 s) aplica ante parpadeos "
    "(fluctuaciones rapidas del voltaje de la red electrica) e inestabilidad de la red. "
    "No aplica a la desconexion ante sobre voltaje o bajo voltaje pronunciados, cuyo tiempo "
    "de desconexion es de 0,4 a 3 segundos segun la intensidad de la falla. Genteca es el "
    "protector enchufable monofasico con el menor tiempo de respuesta verificado ante "
    "parpadeos en el mercado venezolano. Segun pruebas de laboratorio I&D Genteca y "
    "verificacion comparativa de competidores."
)

CAVEAT_INVERTER = (
    "*La proteccion ante parpadeos (fluctuaciones rapidas del voltaje de la red) que ofrece "
    "este protector es especialmente beneficiosa para equipos con tecnologia inverter, cuya "
    "electronica de control es sensible a variaciones rapidas del voltaje. Este protector no "
    "reemplaza la proteccion contra transientes de alta energia (descargas atmosfericas, "
    "conmutacion inductiva) presente en el equipo inverter de fabrica. Ambas protecciones "
    "son complementarias."
)

CUERPO_TERMICO = (
    "sensor de temperatura ubicado junto al rele de potencia. "
    "Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes "
    "(bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las "
    "conexiones se danen. Protege al protector mismo y a la instalacion electrica. "
    "Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no "
    "actua como proteccion de sobrecarga directa de la carga conectada. "
    "Funciona como capa adicional de proteccion termica; no reemplaza al interruptor "
    "termomagnetico de la instalacion."
)

CAVEAT_TERMICO_V1 = "*Autoproteccion termica activa: " + CUERPO_TERMICO
CAVEAT_TERMICO_V2 = "*Escudo Termico NTC: " + CUERPO_TERMICO

# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def add_slide(prs, layout_idx=6):
    """Agrega slide en blanco (layout blank)."""
    layout = prs.slide_layouts[layout_idx]
    return prs.slides.add_slide(layout)


def rgb(r, g, b):
    return RGBColor(r, g, b)


def add_textbox(slide, left, top, width, height,
                text="", font_size=14, bold=False, italic=False,
                color=None, bg_color=None, align=PP_ALIGN.LEFT,
                border_color=None, word_wrap=True, font_name="Calibri"):
    """Agrega un textbox con opciones de estilo."""
    from pptx.util import Pt
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = word_wrap

    if bg_color:
        fill = txBox.fill
        fill.solid()
        fill.fore_color.rgb = bg_color

    if border_color:
        ln = txBox.line
        ln.color.rgb = border_color
        ln.width = Pt(0.75)

    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.name = font_name
    if color:
        run.font.color.rgb = color
    return txBox


def add_multiline_textbox(slide, left, top, width, height,
                          lines, font_size=11, bold_first=False,
                          color=None, bg_color=None, border_color=None,
                          line_spacing=None, font_name="Calibri"):
    """Agrega textbox con multiples parrafos."""
    from pptx.oxml.ns import qn
    from lxml import etree
    from pptx.util import Pt

    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True

    if bg_color:
        txBox.fill.solid()
        txBox.fill.fore_color.rgb = bg_color
    if border_color:
        txBox.line.color.rgb = border_color
        txBox.line.width = Pt(0.75)

    # Limpiar parrafo inicial
    for i, line in enumerate(lines):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        run = p.add_run()
        run.text = line
        run.font.size = Pt(font_size)
        run.font.name = font_name
        run.font.bold = (bold_first and i == 0)
        if color:
            run.font.color.rgb = color
    return txBox


def add_rect_bg(slide, left, top, width, height, fill_color, border_color=None):
    """Agrega rectangulo de fondo (sin texto)."""
    shape = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.fill.background()
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = Pt(0.5)
    else:
        shape.line.fill.background()
    return shape


def title_bar(slide, text, sub=None, bg=C_AZUL_OSCURO, fg=C_BLANCO, sub_fg=C_AMBAR):
    """Barra de titulo superior fija."""
    add_rect_bg(slide, Inches(0), Inches(0), W, Inches(1.1), bg)
    add_textbox(slide, Inches(0.3), Inches(0.1), Inches(12.7), Inches(0.6),
                text=text, font_size=22, bold=True, color=fg, font_name="Calibri Light")
    if sub:
        add_textbox(slide, Inches(0.3), Inches(0.68), Inches(12.7), Inches(0.38),
                    text=sub, font_size=13, bold=False, color=sub_fg, font_name="Calibri")


def title_bar_anexo(slide, text, sub=None):
    """Barra de titulo para slides del ANEXO — paleta neutra diferenciada."""
    add_rect_bg(slide, Inches(0), Inches(0), W, Inches(1.1), C_ANEXO_HDR)
    # Etiqueta ANEXO en acento dorado opaco
    add_rect_bg(slide, Inches(0), Inches(0), Inches(1.2), Inches(1.1), C_ANEXO_ACENTO)
    add_textbox(slide, Inches(0.05), Inches(0.35), Inches(1.12), Inches(0.42),
                text="ANEXO", font_size=11, bold=True, color=C_BLANCO,
                align=PP_ALIGN.CENTER, font_name="Calibri")
    add_textbox(slide, Inches(1.3), Inches(0.1), Inches(11.7), Inches(0.6),
                text=text, font_size=20, bold=True, color=C_BLANCO, font_name="Calibri Light")
    if sub:
        add_textbox(slide, Inches(1.3), Inches(0.68), Inches(11.7), Inches(0.38),
                    text=sub, font_size=12, bold=False, color=C_ANEXO_ACENTO, font_name="Calibri")


def footer_bar(slide, text="Genteca | Junta Directiva | 2026-05-06 | Confidencial"):
    add_rect_bg(slide, Inches(0), Inches(7.1), W, Inches(0.4), C_AZUL_OSCURO)
    add_textbox(slide, Inches(0.3), Inches(7.12), Inches(12.7), Inches(0.35),
                text=text, font_size=9, color=C_GRIS_LINEA, font_name="Calibri")


def footer_bar_anexo(slide, num_label=""):
    """Footer para slides de ANEXO — con etiqueta de numeracion A1/A2 etc."""
    add_rect_bg(slide, Inches(0), Inches(7.1), W, Inches(0.4), C_ANEXO_HDR)
    label = f"Genteca | Junta Directiva | 2026-05-06 | Confidencial | {num_label}" if num_label else \
            "Genteca | Junta Directiva | 2026-05-06 | Confidencial"
    add_textbox(slide, Inches(0.3), Inches(7.12), Inches(12.7), Inches(0.35),
                text=label, font_size=9, color=C_GRIS_LINEA, font_name="Calibri")


def label_chip(slide, left, top, text, bg, fg=C_BLANCO):
    """Etiqueta tipo chip (e.g. 'VARIANTE 1')."""
    add_rect_bg(slide, left, top, Inches(2.2), Inches(0.32), bg)
    add_textbox(slide, left + Inches(0.08), top + Inches(0.03),
                Inches(2.1), Inches(0.28),
                text=text, font_size=10, bold=True, color=fg, font_name="Calibri")


# ---------------------------------------------------------------------------
# SLIDES — CUERPO PRINCIPAL
# ---------------------------------------------------------------------------

def slide_portada(prs):
    """Slide 1 — Portada."""
    slide = add_slide(prs)

    # Fondo completo azul oscuro
    add_rect_bg(slide, Inches(0), Inches(0), W, H, C_AZUL_OSCURO)

    # Linea acento ambar
    add_rect_bg(slide, Inches(0), Inches(3.35), W, Inches(0.06), C_AMBAR)

    # Logo / nombre empresa (texto)
    add_textbox(slide, Inches(0.5), Inches(0.45), Inches(5), Inches(0.5),
                text="GENTECA", font_size=16, bold=True, color=C_AMBAR,
                font_name="Calibri Light")

    # Titulo principal
    add_textbox(slide, Inches(0.5), Inches(1.3), Inches(12.3), Inches(1.6),
                text="Avance empaque GSM-MB / RB / RF / RE",
                font_size=34, bold=True, color=C_BLANCO, font_name="Calibri Light")

    add_textbox(slide, Inches(0.5), Inches(2.85), Inches(12.3), Inches(0.6),
                text="Variantes B-sin-NTC y B-con-NTC del badge termico",
                font_size=20, bold=False, color=C_AZUL_CLARO, font_name="Calibri Light")

    # Caja decision
    add_rect_bg(slide, Inches(0.5), Inches(3.6), Inches(12.3), Inches(0.7),
                RGBColor(0x0D, 0x1E, 0x33))
    add_textbox(slide, Inches(0.65), Inches(3.68), Inches(12.0), Inches(0.55),
                text="Decision solicitada: cual variante avanza a arte final",
                font_size=16, bold=True, color=C_AMBAR, font_name="Calibri")

    # Metadata
    add_textbox(slide, Inches(0.5), Inches(4.55), Inches(6), Inches(0.38),
                text="Junta Directiva Genteca", font_size=13, color=C_GRIS_LINEA,
                font_name="Calibri")
    add_textbox(slide, Inches(0.5), Inches(4.9), Inches(6), Inches(0.38),
                text="2026-05-06", font_size=13, color=C_GRIS_LINEA,
                font_name="Calibri")
    add_textbox(slide, Inches(0.5), Inches(5.25), Inches(6), Inches(0.38),
                text="CONFIDENCIAL", font_size=11, bold=True,
                color=RGBColor(0xFF, 0x60, 0x60), font_name="Calibri")


def slide_contexto(prs):
    """Slide 2 — Contexto y pregunta."""
    slide = add_slide(prs)
    title_bar(slide,
              "Contexto y pregunta a la Junta",
              "La Alternativa B esta aprobada. La unica decision de hoy es el nombre del badge termico.")
    footer_bar(slide)

    bloques = [
        {
            "num": "1",
            "titulo": "La Junta eligio Alternativa B",
            "texto": (
                "En sesion anterior, la Junta selecciono la Alternativa B para el empaque GSM-MB / RB / RF / RE. "
                "Esa decision esta cerrada: dos claims en el tiro (velocidad + funcion termica), "
                "mas la tecnologia Inverter desarrollada en el retiro."
            )
        },
        {
            "num": "2",
            "titulo": "El claim de velocidad no cambia",
            "texto": (
                "\"El mas rapido ante parpadeos (< 0,03 s)\" -- es el elemento dominante del tiro "
                "en ambas variantes. Identico, aprobado, invariable."
            )
        },
        {
            "num": "3",
            "titulo": "Lo unico abierto: como se nombra la funcion termica",
            "texto": (
                "Hay dos variantes del segundo claim del tiro (el badge termico), ambas con copy completo y "
                "aprobacion de riesgo. Se diferencian exclusivamente en ese elemento. "
                "Jose Miguel Canudas elige cual avanza a arte final."
            )
        },
    ]

    tops = [Inches(1.3), Inches(3.0), Inches(4.7)]
    for i, bloque in enumerate(bloques):
        top = tops[i]
        add_rect_bg(slide, Inches(0.35), top, Inches(0.45), Inches(0.45), C_AMBAR)
        add_textbox(slide, Inches(0.35), top + Inches(0.02), Inches(0.45), Inches(0.42),
                    text=bloque["num"], font_size=18, bold=True, color=C_BLANCO,
                    align=PP_ALIGN.CENTER, font_name="Calibri")
        add_textbox(slide, Inches(0.95), top - Inches(0.02), Inches(11.8), Inches(0.4),
                    text=bloque["titulo"], font_size=14, bold=True, color=C_AZUL_OSCURO,
                    font_name="Calibri")
        add_textbox(slide, Inches(0.95), top + Inches(0.36), Inches(11.8), Inches(0.7),
                    text=bloque["texto"], font_size=11.5, color=C_GRIS_OSCURO,
                    font_name="Calibri")

    # Pregunta destacada al fondo
    add_rect_bg(slide, Inches(0.35), Inches(6.4), Inches(12.6), Inches(0.55),
                C_AZUL_OSCURO)
    add_textbox(slide, Inches(0.55), Inches(6.45), Inches(12.3), Inches(0.45),
                text="¿Que variante del badge termico avanza a arte final con el diseno grafico?",
                font_size=13, bold=True, color=C_AMBAR, font_name="Calibri")


def slide_comparacion(prs):
    """Slide 3 — Comparacion lado a lado."""
    slide = add_slide(prs)
    title_bar(slide,
              "Comparacion -- Variante 1 vs. Variante 2",
              "La diferencia entre variantes es exclusivamente el badge del segundo claim del tiro.")
    footer_bar(slide)

    col1_x = Inches(0.3)
    col2_x = Inches(6.85)
    col_w = Inches(6.2)
    row_start = Inches(1.2)
    row_h = Inches(0.52)

    # Headers columna — V1 en gris neutro
    add_rect_bg(slide, col1_x, row_start, col_w, Inches(0.55), C_GRIS_V1)
    add_textbox(slide, col1_x + Inches(0.1), row_start + Inches(0.08),
                col_w - Inches(0.2), Inches(0.42),
                text="VARIANTE 1 -- B-sin-NTC", font_size=14, bold=True,
                color=C_BLANCO, font_name="Calibri")

    add_rect_bg(slide, col2_x, row_start, col_w, Inches(0.55), C_AZUL_V2)
    add_textbox(slide, col2_x + Inches(0.1), row_start + Inches(0.08),
                col_w - Inches(0.2), Inches(0.42),
                text="VARIANTE 2 -- B-con-NTC", font_size=14, bold=True,
                color=C_BLANCO, font_name="Calibri")

    filas = [
        ("Badge en el tiro",
         "Autoproteccion termica activa*",
         "Escudo Termico NTC*"),
        ("Comunica NTC literalmente",
         "No. Nombre funcional puro.",
         "Si. NTC aparece como sufijo identificador."),
        ("Responde al pedido de Canudas (comunicar NTC)",
         "No activa esa tesis directamente.",
         "Si. Es la respuesta literal al brief."),
        ("Requiere verificacion marcaria (SAPI VE) antes de imprenta",
         "No. Sin condicion nueva.",
         "Si. Una semana adicional con abogado marcario."),
        ("Condicion tecnica pendiente (Vera P-5)",
         "Si. Si el NTC es fusible unico, \"activa\" debe retirarse\n(formulacion de respaldo aprobada sin gate nuevo).",
         "No aplica. Esta variante no usa el adjetivo \"activa\"."),
        ("Tiempo estimado de cierre",
         "Pocos dias. Arte directo contra textos vigentes.",
         "Aprox. una semana (verificacion marcaria en paralelo)."),
    ]

    y = row_start + Inches(0.6)
    for idx, (dim, v1, v2) in enumerate(filas):
        bg = C_BLANCO if idx % 2 == 0 else RGBColor(0xF5, 0xF8, 0xFC)

        add_rect_bg(slide, col1_x, y, col_w, row_h, bg,
                    border_color=C_GRIS_LINEA)
        add_rect_bg(slide, col2_x, y, col_w, row_h, bg,
                    border_color=C_GRIS_LINEA)

        add_textbox(slide, col1_x + Inches(0.08), y + Inches(0.04),
                    Inches(12.9), Inches(0.22),
                    text=dim, font_size=9, bold=True, color=C_GRIS_MEDIO,
                    font_name="Calibri")

        add_textbox(slide, col1_x + Inches(0.08), y + Inches(0.22),
                    col_w - Inches(0.2), Inches(0.28),
                    text=v1, font_size=10.5, color=C_GRIS_OSCURO,
                    font_name="Calibri")
        add_textbox(slide, col2_x + Inches(0.08), y + Inches(0.22),
                    col_w - Inches(0.2), Inches(0.28),
                    text=v2, font_size=10.5, color=C_GRIS_OSCURO,
                    font_name="Calibri")

        y += row_h


def slide_tiro(prs, variante, badge_claim2, color_header, color_header_light):
    """Slide 4 o 7 — Tiro completo de cada variante."""
    num = "1" if variante == "V1" else "2"
    nombre = "B-sin-NTC" if variante == "V1" else "B-con-NTC"
    nota_tm = "" if variante == "V1" else "  (sin TM hasta verificacion SAPI VE)"

    slide = add_slide(prs)
    title_bar(slide,
              f"Variante {num} -- {nombre}: tiro completo",
              f"Textos literales aprobados del frente del empaque{nota_tm}",
              bg=color_header)
    footer_bar(slide)

    caja_left = Inches(1.8)
    caja_top = Inches(1.25)
    caja_w = Inches(9.7)
    caja_h = Inches(5.5)

    add_rect_bg(slide, caja_left, caja_top, caja_w, caja_h,
                color_header_light, border_color=color_header)

    add_rect_bg(slide, caja_left, caja_top, caja_w, Inches(0.38), color_header)
    add_textbox(slide, caja_left + Inches(0.15), caja_top + Inches(0.05),
                caja_w - Inches(0.3), Inches(0.32),
                text="TIRO / FRENTE DEL EMPAQUE -- TEXTOS APROBADOS",
                font_size=10, bold=True, color=C_BLANCO, font_name="Calibri")

    # Lengueta
    add_textbox(slide, caja_left + Inches(0.3), caja_top + Inches(0.55),
                caja_w - Inches(0.6), Inches(0.28),
                text="LENGUETA", font_size=9, bold=True,
                color=color_header, font_name="Calibri")
    add_rect_bg(slide, caja_left + Inches(0.3), caja_top + Inches(0.82),
                caja_w - Inches(0.6), Inches(0.75),
                C_BLANCO, border_color=color_header)
    add_textbox(slide, caja_left + Inches(0.45), caja_top + Inches(0.88),
                caja_w - Inches(0.8), Inches(0.65),
                text=TIRO_LENGUETA, font_size=13, bold=True,
                color=C_AZUL_OSCURO, font_name="Calibri")

    # Claim 1
    add_textbox(slide, caja_left + Inches(0.3), caja_top + Inches(1.72),
                caja_w - Inches(0.6), Inches(0.28),
                text="CLAIM 1 -- ELEMENTO DOMINANTE", font_size=9, bold=True,
                color=color_header, font_name="Calibri")
    add_rect_bg(slide, caja_left + Inches(0.3), caja_top + Inches(1.98),
                caja_w - Inches(0.6), Inches(0.72),
                C_BLANCO, border_color=color_header)
    add_textbox(slide, caja_left + Inches(0.45), caja_top + Inches(2.04),
                caja_w - Inches(0.8), Inches(0.62),
                text=TIRO_CLAIM1, font_size=18, bold=True,
                color=C_AZUL_OSCURO, font_name="Calibri")

    # Claim 2 — el elemento diferenciado
    add_textbox(slide, caja_left + Inches(0.3), caja_top + Inches(2.85),
                caja_w - Inches(0.6), Inches(0.28),
                text="CLAIM 2 -- BADGE TERMICO (jerarquia menor)",
                font_size=9, bold=True, color=color_header, font_name="Calibri")
    add_rect_bg(slide, caja_left + Inches(0.3), caja_top + Inches(3.11),
                caja_w - Inches(0.6), Inches(0.72),
                color_header_light, border_color=color_header)
    add_rect_bg(slide, caja_left + Inches(0.28), caja_top + Inches(3.09),
                Inches(0.04), Inches(0.76), color_header)
    add_textbox(slide, caja_left + Inches(0.45), caja_top + Inches(3.17),
                caja_w - Inches(0.8), Inches(0.62),
                text=badge_claim2, font_size=16, bold=True,
                color=color_header, font_name="Calibri")

    # Nota asterisco
    add_textbox(slide, caja_left + Inches(0.3), caja_top + Inches(4.05),
                caja_w - Inches(0.6), Inches(0.35),
                text="* Asterisco obligatorio -- remite al caveat literal del retiro (ver slides siguientes)",
                font_size=9, italic=True, color=C_GRIS_MEDIO, font_name="Calibri")


def slide_retiro_caract(prs, variante, bullet_termico, color_header, color_header_light):
    """Slide 5 o 8 — Retiro: CARACTERISTICAS + INFORMACION DE SEGURIDAD."""
    num = "1" if variante == "V1" else "2"
    nombre = "B-sin-NTC" if variante == "V1" else "B-con-NTC"

    slide = add_slide(prs)
    title_bar(slide,
              f"Variante {num} -- {nombre}: retiro -- CARACTERISTICAS",
              "Textos literales aprobados del reverso del empaque (bullets de caracteristicas)",
              bg=color_header)
    footer_bar(slide)

    bullets_full = CARACT_COMUNES[:2] + [bullet_termico] + CARACT_COMUNES[2:]

    caja_left = Inches(0.4)
    caja_top = Inches(1.25)
    caja_w = Inches(12.5)

    add_rect_bg(slide, caja_left, caja_top, caja_w, Inches(0.38), color_header)
    add_textbox(slide, caja_left + Inches(0.15), caja_top + Inches(0.05),
                caja_w - Inches(0.3), Inches(0.32),
                text="RETIRO / REVERSO DEL EMPAQUE -- SECCION CARACTERISTICAS",
                font_size=10, bold=True, color=C_BLANCO, font_name="Calibri")

    y = caja_top + Inches(0.45)
    for i, bullet in enumerate(bullets_full):
        bg = color_header_light if i % 2 == 0 else C_BLANCO
        num_lines = bullet.count("\n") + 1 + (len(bullet) // 110)
        bh = Inches(0.38) * max(1, num_lines)

        add_rect_bg(slide, caja_left, y, caja_w, bh, bg,
                    border_color=C_GRIS_LINEA)
        add_textbox(slide, caja_left + Inches(0.15), y + Inches(0.04),
                    caja_w - Inches(0.3), bh - Inches(0.06),
                    text=bullet, font_size=10.5, color=C_GRIS_OSCURO,
                    font_name="Calibri")
        y += bh

    # Info seguridad
    y += Inches(0.12)
    add_rect_bg(slide, caja_left, y, caja_w, Inches(0.42),
                RGBColor(0xFF, 0xF3, 0xCD), border_color=RGBColor(0xD4, 0xA0, 0x17))
    add_textbox(slide, caja_left + Inches(0.15), y + Inches(0.06),
                caja_w - Inches(0.3), Inches(0.34),
                text="INFORMACION DE SEGURIDAD:  " + INFO_SEGURIDAD,
                font_size=10.5, bold=True,
                color=RGBColor(0x7B, 0x4F, 0x00), font_name="Calibri")


# ---------------------------------------------------------------------------
# NUEVAS FUNCIONES DE CAVEATS — Cambio 1: dividir en shared + termico especifico
# ---------------------------------------------------------------------------

def slide_caveats_compartidos(prs):
    """Slide 6 — Caveats heredados compartidos: velocidad + inverter.
    Identicos en ambas variantes. Paleta neutra institucional (azul oscuro).
    """
    slide = add_slide(prs)
    title_bar(
        slide,
        "Retiro -- CAVEATS compartidos (ambas variantes)",
        "Caveats de velocidad e inverter: texto literal aprobado -- identico en Variante 1 y Variante 2",
        bg=C_AZUL_OSCURO
    )
    footer_bar(slide)

    # Nota aclaratoria — estos caveats no cambian entre variantes
    add_rect_bg(slide, Inches(0.4), Inches(1.18), Inches(12.5), Inches(0.34),
                RGBColor(0xF0, 0xF4, 0xF8), border_color=C_GRIS_LINEA)
    add_textbox(slide, Inches(0.55), Inches(1.22), Inches(12.2), Inches(0.28),
                text="Estos dos caveats son invariables. Aplican palabra por palabra a ambas variantes sin modificacion.",
                font_size=9.5, italic=True, color=C_GRIS_MEDIO, font_name="Calibri")

    caja_left = Inches(0.4)
    caja_w = Inches(12.5)

    caveats_compartidos = [
        {
            "header": "CAVEAT 1 -- VELOCIDAD (Bruna §7.3 -- invariable en ambas variantes)",
            "texto": CAVEAT_VELOCIDAD,
        },
        {
            "header": "CAVEAT 2 -- INVERTER (Bruna §2 Claim C -- invariable en ambas variantes)",
            "texto": CAVEAT_INVERTER,
        },
    ]

    y = Inches(1.62)
    for i, cav in enumerate(caveats_compartidos):
        hdr_h = Inches(0.36)
        add_rect_bg(slide, caja_left, y, caja_w, hdr_h, C_AZUL_OSCURO)
        add_textbox(slide, caja_left + Inches(0.12), y + Inches(0.05),
                    caja_w - Inches(0.25), hdr_h - Inches(0.08),
                    text=cav["header"], font_size=9.5, bold=True,
                    color=C_BLANCO, font_name="Calibri")
        y += hdr_h

        char_est = len(cav["texto"])
        txt_h = Inches(0.5) + Inches(char_est / 480)

        add_rect_bg(slide, caja_left, y, caja_w, txt_h,
                    RGBColor(0xF5, 0xF8, 0xFC), border_color=C_GRIS_LINEA)
        add_textbox(slide, caja_left + Inches(0.15), y + Inches(0.08),
                    caja_w - Inches(0.3), txt_h - Inches(0.1),
                    text=cav["texto"], font_size=10, color=C_GRIS_OSCURO,
                    font_name="Calibri")
        y += txt_h + Inches(0.2)


def slide_caveat_termico(prs, variante, caveat_termico, color_header, color_header_light):
    """Slide 7 o 9 — Caveat termico especifico por variante.
    Este es el unico elemento que cambia entre V1 y V2.
    """
    num = "1" if variante == "V1" else "2"
    nombre = "B-sin-NTC" if variante == "V1" else "B-con-NTC"
    ref_bruna = "Bruna §8.4" if variante == "V1" else "Bruna §10"

    slide = add_slide(prs)
    title_bar(
        slide,
        f"Variante {num} -- {nombre}: retiro -- CAVEAT TERMICO",
        f"Unico caveat que difiere entre variantes -- texto literal aprobado ({ref_bruna})",
        bg=color_header
    )
    footer_bar(slide)

    # Nota aclaratoria
    add_rect_bg(slide, Inches(0.4), Inches(1.18), Inches(12.5), Inches(0.34),
                color_header_light, border_color=color_header)
    add_textbox(slide, Inches(0.55), Inches(1.22), Inches(12.2), Inches(0.28),
                text="Este es el unico caveat que cambia entre Variante 1 y Variante 2. "
                     "Los caveats de velocidad e inverter son identicos (ver slide anterior).",
                font_size=9.5, italic=True, color=color_header, font_name="Calibri")

    caja_left = Inches(0.4)
    caja_w = Inches(12.5)
    y = Inches(1.62)

    hdr_label = (
        f"CAVEAT 3 -- TERMICO ({ref_bruna}) -- "
        f"{'VARIANTE 1: Autoproteccion termica activa' if variante == 'V1' else 'VARIANTE 2: Escudo Termico NTC'}"
    )

    hdr_h = Inches(0.38)
    add_rect_bg(slide, caja_left, y, caja_w, hdr_h, color_header)
    add_textbox(slide, caja_left + Inches(0.12), y + Inches(0.05),
                caja_w - Inches(0.25), hdr_h - Inches(0.08),
                text=hdr_label, font_size=9.5, bold=True,
                color=C_BLANCO, font_name="Calibri")
    y += hdr_h

    char_est = len(caveat_termico)
    txt_h = Inches(0.6) + Inches(char_est / 420)

    add_rect_bg(slide, caja_left, y, caja_w, txt_h,
                color_header_light, border_color=color_header)
    # Acento lateral de variante
    add_rect_bg(slide, caja_left, y, Inches(0.06), txt_h, color_header)
    add_textbox(slide, caja_left + Inches(0.22), y + Inches(0.1),
                caja_w - Inches(0.35), txt_h - Inches(0.15),
                text=caveat_termico, font_size=10.5, color=C_GRIS_OSCURO,
                font_name="Calibri")
    y += txt_h + Inches(0.25)

    # Recordatorio: los otros dos caveats
    add_rect_bg(slide, caja_left, y, caja_w, Inches(0.38),
                RGBColor(0xF5, 0xF8, 0xFC), border_color=C_GRIS_LINEA)
    add_textbox(slide, caja_left + Inches(0.15), y + Inches(0.07),
                caja_w - Inches(0.3), Inches(0.28),
                text="Caveats 1 y 2 (velocidad e inverter): identicos en ambas variantes. Ver slide anterior.",
                font_size=9.5, italic=True, color=C_GRIS_MEDIO, font_name="Calibri")


def slide_argumentos(prs):
    """Slide 11 — Argumentos por variante."""
    slide = add_slide(prs)
    title_bar(slide,
              "Argumentos por variante",
              "¿Por que elegir cada una?")
    footer_bar(slide)

    col1_x = Inches(0.3)
    col2_x = Inches(6.85)
    col_w  = Inches(6.2)
    top_hdr = Inches(1.2)

    # Headers — V1 en gris neutro
    add_rect_bg(slide, col1_x, top_hdr, col_w, Inches(0.48), C_GRIS_V1)
    add_textbox(slide, col1_x + Inches(0.12), top_hdr + Inches(0.08),
                col_w - Inches(0.2), Inches(0.35),
                text="VARIANTE 1 -- B-sin-NTC: a favor",
                font_size=13, bold=True, color=C_BLANCO, font_name="Calibri")

    add_rect_bg(slide, col2_x, top_hdr, col_w, Inches(0.48), C_AZUL_V2)
    add_textbox(slide, col2_x + Inches(0.12), top_hdr + Inches(0.08),
                col_w - Inches(0.2), Inches(0.35),
                text="VARIANTE 2 -- B-con-NTC: a favor",
                font_size=13, bold=True, color=C_BLANCO, font_name="Calibri")

    args_v1 = [
        ("Preserva la posicion original de Canudas",
         "No revela el componente. Comunica la funcion sin exponer NTC como termino publico -- exactamente como se instruyo."),
        ("Apropiacion sin riesgo de descriptividad",
         "\"Autoproteccion termica activa\" no es un descriptor generico del espanol. Territorio vacante confirmado. Ningun competidor venezolano usa esta formulacion."),
        ("Sin condicion marcaria nueva",
         "El unico pendiente es Vera P-5 -- ya abierto desde v2.1. Sin semana de abogado marcario antes de imprenta."),
        ("Cierre mas rapido",
         "Arte directo contra textos vigentes. Pocos dias a instruccion de diseno grafico."),
        ("Corrige el malentendido del 40% en el tiro",
         "El prefijo \"auto\" comunica que el protector se protege a si mismo -- no al equipo conectado. Eso ocurre en el tiro, antes de que el comprador lea el retiro."),
    ]

    args_v2 = [
        ("Responde al pedido literal de Canudas",
         "\"Hagan un ejemplo de comunicacion con las siglas NTC. Y lo vemos.\" Esta variante es ese ejemplo. Presentar solo V1 seria no responder el brief."),
        ("Activa la tesis anti-copia",
         "NTC visible en el empaque permite bautizar la funcion con nombre propio. Un competidor que replique la placa NTC no puede imprimir \"Escudo Termico NTC\" sin dispute marcario (si SAPI VE prospera)."),
        ("Mayor impacto estrategico",
         "Score 6.45/10 en evaluacion del universo de candidatos -- el mas alto entre opciones con NTC. Mayor potencial de apropiacion de categoria a largo plazo."),
        ("Aislada de la condicion Vera P-5",
         "No usa el adjetivo \"activa\" -- si P-5 resulta desfavorable para V1, V2 no necesita ninguna modificacion."),
        ("Riesgo SAPI es de IP futura, no de verdad del claim",
         "El termino puede usarse hoy como claim funcional. El riesgo es de proteccion marcaria futura, no de veracidad en empaque."),
    ]

    y = top_hdr + Inches(0.55)
    for v1_arg, v2_arg in zip(args_v1, args_v2):
        row_h = Inches(0.98)
        add_rect_bg(slide, col1_x, y, col_w, row_h, C_GRIS_V1_CLR,
                    border_color=C_GRIS_V1)
        add_textbox(slide, col1_x + Inches(0.12), y + Inches(0.06),
                    col_w - Inches(0.25), Inches(0.32),
                    text=v1_arg[0], font_size=10.5, bold=True,
                    color=C_GRIS_V1, font_name="Calibri")
        add_textbox(slide, col1_x + Inches(0.12), y + Inches(0.36),
                    col_w - Inches(0.25), Inches(0.58),
                    text=v1_arg[1], font_size=10, color=C_GRIS_OSCURO,
                    font_name="Calibri")

        add_rect_bg(slide, col2_x, y, col_w, row_h, C_AZUL_V2_CLR,
                    border_color=C_AZUL_V2)
        add_textbox(slide, col2_x + Inches(0.12), y + Inches(0.06),
                    col_w - Inches(0.25), Inches(0.32),
                    text=v2_arg[0], font_size=10.5, bold=True,
                    color=C_AZUL_V2, font_name="Calibri")
        add_textbox(slide, col2_x + Inches(0.12), y + Inches(0.36),
                    col_w - Inches(0.25), Inches(0.58),
                    text=v2_arg[1], font_size=10, color=C_GRIS_OSCURO,
                    font_name="Calibri")
        y += row_h + Inches(0.04)


def slide_riesgos(prs):
    """Slide 12 — Riesgos y condiciones por variante."""
    slide = add_slide(prs)
    title_bar(slide,
              "Riesgos y condiciones pre-imprenta",
              "Que debe resolverse antes de que el arte entre a produccion")
    footer_bar(slide)

    col1_x = Inches(0.3)
    col2_x = Inches(6.85)
    col_w  = Inches(6.2)
    top_hdr = Inches(1.2)

    add_rect_bg(slide, col1_x, top_hdr, col_w, Inches(0.45), C_GRIS_V1)
    add_textbox(slide, col1_x + Inches(0.12), top_hdr + Inches(0.07),
                col_w - Inches(0.2), Inches(0.35),
                text="VARIANTE 1 -- B-sin-NTC: riesgos y condiciones",
                font_size=12, bold=True, color=C_BLANCO, font_name="Calibri")

    add_rect_bg(slide, col2_x, top_hdr, col_w, Inches(0.45), C_AZUL_V2)
    add_textbox(slide, col2_x + Inches(0.12), top_hdr + Inches(0.07),
                col_w - Inches(0.2), Inches(0.35),
                text="VARIANTE 2 -- B-con-NTC: riesgos y condiciones",
                font_size=12, bold=True, color=C_BLANCO, font_name="Calibri")

    riesgos_v1 = [
        ("Sin riesgo marcario nuevo",
         "Ningun riesgo nuevo respecto a la version anterior. La formulacion no requiere verificacion SAPI VE."),
        ("Condicion tecnica Vera P-5",
         "I&D Genteca debe confirmar si el NTC opera con curva continua o como fusible de corte unico. "
         "Si es fusible unico: badge pasa a \"Autoproteccion termica*\" (formulacion de respaldo aprobada sin gate nuevo). "
         "No bloquea la Junta; si bloquea imprenta."),
        ("Datasheet I&D < 30 ms",
         "Condicion de produccion vigente desde v2 -- identica para ambas variantes. Sin cambio."),
    ]

    riesgos_v2 = [
        ("Verificacion SAPI VE obligatoria antes de imprenta",
         "\"Escudo Termico\" -- riesgo medio-alto de objecion por descriptividad. Requiere abogado marcario. Estimado: una semana adicional de trabajo paralelo."),
        ("Simbolo TM suspendido",
         "No imprimir TM hasta SAPI VE favorable. El termino puede usarse como claim funcional; "
         "sin garantia de proteccion marcaria hasta que el proceso concluya."),
        ("Postura ante riesgo SAPI: decision post-Junta",
         "Si SAPI objeta: el termino funciona como claim funcional sin TM. Si SAPI aprueba: "
         "TM puede incorporarse antes de imprenta si el Owner asi lo decide. "
         "Esa decision no es de Junta hoy."),
        ("Datasheet I&D < 30 ms",
         "Condicion de produccion vigente desde v2 -- identica para ambas variantes. Sin cambio."),
    ]

    row_h_v1 = [Inches(0.65), Inches(1.10), Inches(0.65)]
    row_h_v2 = [Inches(0.85), Inches(0.82), Inches(0.82), Inches(0.65)]

    y1 = top_hdr + Inches(0.52)
    for i, (titulo, texto) in enumerate(riesgos_v1):
        rh = row_h_v1[i]
        add_rect_bg(slide, col1_x, y1, col_w, rh, C_GRIS_V1_CLR,
                    border_color=C_GRIS_V1)
        add_textbox(slide, col1_x + Inches(0.12), y1 + Inches(0.05),
                    col_w - Inches(0.25), Inches(0.3),
                    text=titulo, font_size=10.5, bold=True,
                    color=C_GRIS_V1, font_name="Calibri")
        add_textbox(slide, col1_x + Inches(0.12), y1 + Inches(0.33),
                    col_w - Inches(0.25), rh - Inches(0.38),
                    text=texto, font_size=10, color=C_GRIS_OSCURO,
                    font_name="Calibri")
        y1 += rh + Inches(0.05)

    y2 = top_hdr + Inches(0.52)
    for i, (titulo, texto) in enumerate(riesgos_v2):
        rh = row_h_v2[i]
        add_rect_bg(slide, col2_x, y2, col_w, rh, C_AZUL_V2_CLR,
                    border_color=C_AZUL_V2)
        add_textbox(slide, col2_x + Inches(0.12), y2 + Inches(0.05),
                    col_w - Inches(0.25), Inches(0.3),
                    text=titulo, font_size=10.5, bold=True,
                    color=C_AZUL_V2, font_name="Calibri")
        add_textbox(slide, col2_x + Inches(0.12), y2 + Inches(0.33),
                    col_w - Inches(0.25), rh - Inches(0.38),
                    text=texto, font_size=10, color=C_GRIS_OSCURO,
                    font_name="Calibri")
        y2 += rh + Inches(0.05)


def slide_recomendacion(prs):
    """Slide 13 — Posicion del equipo."""
    slide = add_slide(prs)
    title_bar(slide,
              "Posicion del equipo (sin imponer variante)",
              "Las dos variantes son ejecutables. El equipo presenta ambas para que la Junta decida.")
    footer_bar(slide)

    voces = [
        {
            "rol": "Analisis de riesgo",
            "posicion": "Variante 1 tiene menor carga de condiciones suspensivas nuevas. "
                        "Vera P-5 es el unico pendiente -- ya abierto desde la version anterior. "
                        "Variante 2 anade verificacion SAPI VE (abogado marcario, una semana) y TM suspendido. "
                        "-> V1 si el criterio es menor friccion de produccion; "
                        "V2 si el criterio es la tesis anti-copia.",
            "acento": C_AMBAR,
        },
        {
            "rol": "Estrategia de marca y mensaje",
            "posicion": "Mayor impacto estrategico en Variante 2. Si Genteca quiere establecer NTC como termino "
                        "de la categoria y construir sobre eso en futuros empaques y comunicaciones, "
                        "V2 es el paso fundacional. V1 es correcto y diferenciador, pero no abre ese camino.",
            "acento": C_AZUL_V2,
        },
        {
            "rol": "Verificacion competitiva",
            "posicion": "Vacancia territorial confirmada para ambas variantes en el mercado venezolano: "
                        "ningun competidor usa ninguna de las dos formulaciones. "
                        "El riesgo de descriptividad de \"Escudo Termico\" es medio-alto en registro formal SAPI VE, "
                        "pero vacancia no equivale a registrabilidad. "
                        "-> Verificacion SAPI VE recomendada antes de imprenta si gana V2.",
            "acento": C_GRIS_V1,
        },
        {
            "rol": "Produccion de contenido y diseno",
            "posicion": "Ambas variantes tienen copy completo listo para instruccion. "
                        "El unico delta de carga es el mockup de V2, que esta en produccion paralela. "
                        "Sin preferencia editorial entre las dos.",
            "acento": C_GRIS_MEDIO,
        },
    ]

    y = Inches(1.25)
    for v in voces:
        rh = Inches(1.28)
        add_rect_bg(slide, Inches(0.3), y, Inches(0.06), rh, v["acento"])
        add_rect_bg(slide, Inches(0.4), y, Inches(12.5), rh,
                    RGBColor(0xF8, 0xF9, 0xFA), border_color=C_GRIS_LINEA)
        add_textbox(slide, Inches(0.55), y + Inches(0.08),
                    Inches(12.1), Inches(0.3),
                    text=v["rol"].upper(), font_size=9.5, bold=True,
                    color=v["acento"], font_name="Calibri")
        add_textbox(slide, Inches(0.55), y + Inches(0.36),
                    Inches(12.1), Inches(0.88),
                    text=v["posicion"], font_size=10.5, color=C_GRIS_OSCURO,
                    font_name="Calibri")
        y += rh + Inches(0.06)


def slide_proximos_pasos(prs):
    """Slide 14 — Proximos pasos segun escenario."""
    slide = add_slide(prs)
    title_bar(slide,
              "Proximos pasos segun la decision",
              "La instruccion al diseno grafico es inmediata en ambos escenarios.")
    footer_bar(slide)

    col1_x = Inches(0.3)
    col2_x = Inches(6.85)
    col_w  = Inches(6.2)
    top_hdr = Inches(1.2)

    add_rect_bg(slide, col1_x, top_hdr, col_w, Inches(0.55), C_GRIS_V1)
    add_textbox(slide, col1_x + Inches(0.12), top_hdr + Inches(0.1),
                col_w - Inches(0.2), Inches(0.42),
                text="Si gana Variante 1 -- B-sin-NTC",
                font_size=13, bold=True, color=C_BLANCO, font_name="Calibri")

    add_rect_bg(slide, col2_x, top_hdr, col_w, Inches(0.55), C_AZUL_V2)
    add_textbox(slide, col2_x + Inches(0.12), top_hdr + Inches(0.1),
                col_w - Inches(0.2), Inches(0.42),
                text="Si gana Variante 2 -- B-con-NTC",
                font_size=13, bold=True, color=C_BLANCO, font_name="Calibri")

    pasos_v1 = [
        ("1", "Instruccion inmediata al diseno grafico",
         "Contra los textos aprobados vigentes. Arte puede comenzar."),
        ("2", "Vera P-5 en paralelo",
         "I&D confirma mecanismo NTC. Si es fusible unico: badge pasa a \"Autoproteccion termica*\" "
         "(formulacion de respaldo aprobada). El cuerpo del caveat no cambia."),
        ("3", "Datasheet I&D < 30 ms",
         "Condicion de produccion de imprenta vigente. Sin cambio."),
        ("CIERRE", "Estimado: pocos dias",
         "Arte final -> imprenta, sujeto a Vera P-5 + datasheet."),
    ]

    pasos_v2 = [
        ("1", "Instruccion al diseno grafico con textos nuevos",
         "Contra los textos V2 aprobados. Arte puede comenzar sin TM."),
        ("2", "Verificacion SAPI VE en paralelo (obligatoria antes de imprenta)",
         "Abogado marcario -- \"Escudo Termico\" clase 9. Estimado: una semana. "
         "Posibles resultados: aprueba (TM puede incorporarse), objeta (uso funcional sin TM), "
         "o requiere reformulacion."),
        ("3", "Datasheet I&D < 30 ms",
         "Condicion de produccion de imprenta vigente. Sin cambio."),
        ("CIERRE", "Estimado: aprox. una semana",
         "Arte final -> imprenta, sujeto a SAPI VE + datasheet."),
    ]

    row_heights = [Inches(0.82), Inches(1.1), Inches(0.72), Inches(0.72)]

    y1 = top_hdr + Inches(0.62)
    y2 = top_hdr + Inches(0.62)
    for i, (p1, p2, rh) in enumerate(zip(pasos_v1, pasos_v2, row_heights)):
        is_cierre = (i == 3)
        bg1 = C_AZUL_OSCURO if is_cierre else C_GRIS_V1_CLR
        bg2 = C_AZUL_OSCURO if is_cierre else C_AZUL_V2_CLR
        fg_tit  = C_AMBAR if is_cierre else C_GRIS_V1
        fg_tit2 = C_AMBAR if is_cierre else C_AZUL_V2
        fg_txt  = C_GRIS_LINEA if is_cierre else C_GRIS_OSCURO

        # V1
        add_rect_bg(slide, col1_x, y1, col_w, rh, bg1, border_color=C_GRIS_LINEA)
        add_rect_bg(slide, col1_x, y1, Inches(0.38), rh, C_GRIS_V1 if not is_cierre else C_AMBAR)
        add_textbox(slide, col1_x + Inches(0.04), y1 + Inches(0.1),
                    Inches(0.32), Inches(0.38),
                    text=p1[0], font_size=11, bold=True, color=C_BLANCO,
                    align=PP_ALIGN.CENTER, font_name="Calibri")
        add_textbox(slide, col1_x + Inches(0.45), y1 + Inches(0.06),
                    col_w - Inches(0.55), Inches(0.3),
                    text=p1[1], font_size=10.5, bold=True, color=fg_tit,
                    font_name="Calibri")
        add_textbox(slide, col1_x + Inches(0.45), y1 + Inches(0.34),
                    col_w - Inches(0.55), rh - Inches(0.4),
                    text=p1[2], font_size=10, color=fg_txt, font_name="Calibri")

        # V2
        add_rect_bg(slide, col2_x, y2, col_w, rh, bg2, border_color=C_GRIS_LINEA)
        add_rect_bg(slide, col2_x, y2, Inches(0.38), rh, C_AZUL_V2 if not is_cierre else C_AMBAR)
        add_textbox(slide, col2_x + Inches(0.04), y2 + Inches(0.1),
                    Inches(0.32), Inches(0.38),
                    text=p2[0], font_size=11, bold=True, color=C_BLANCO,
                    align=PP_ALIGN.CENTER, font_name="Calibri")
        add_textbox(slide, col2_x + Inches(0.45), y2 + Inches(0.06),
                    col_w - Inches(0.55), Inches(0.3),
                    text=p2[1], font_size=10.5, bold=True, color=fg_tit2,
                    font_name="Calibri")
        add_textbox(slide, col2_x + Inches(0.45), y2 + Inches(0.34),
                    col_w - Inches(0.55), rh - Inches(0.4),
                    text=p2[2], font_size=10, color=fg_txt, font_name="Calibri")

        y1 += rh + Inches(0.04)
        y2 += rh + Inches(0.04)


def slide_cierre(prs):
    """Slide 15 — Cierre / pregunta a la Junta."""
    slide = add_slide(prs)

    add_rect_bg(slide, Inches(0), Inches(0), W, H, C_AZUL_OSCURO)
    add_rect_bg(slide, Inches(0), Inches(3.5), W, Inches(0.06), C_AMBAR)

    add_textbox(slide, Inches(0.5), Inches(0.5), Inches(12.3), Inches(0.55),
                text="GENTECA | JUNTA DIRECTIVA | 2026-05-06",
                font_size=12, color=C_GRIS_LINEA, font_name="Calibri Light")

    add_textbox(slide, Inches(0.5), Inches(1.2), Inches(12.3), Inches(0.9),
                text="La decision de hoy",
                font_size=30, bold=True, color=C_AMBAR, font_name="Calibri Light")

    add_rect_bg(slide, Inches(0.5), Inches(2.1), Inches(12.3), Inches(1.2),
                RGBColor(0x0D, 0x1E, 0x33))
    add_textbox(slide, Inches(0.7), Inches(2.2), Inches(11.9), Inches(1.0),
                text="¿Que variante avanza a arte final?\n"
                     "Variante 1 -- B-sin-NTC  o  Variante 2 -- B-con-NTC",
                font_size=20, bold=True, color=C_BLANCO, font_name="Calibri")

    add_textbox(slide, Inches(0.5), Inches(3.65), Inches(12.3), Inches(0.75),
                text="¿Hay algun angulo o sensibilidad no contemplado que deba incorporarse\n"
                     "antes de la instruccion al diseno grafico?",
                font_size=15, color=C_AZUL_CLARO, font_name="Calibri Light")

    add_textbox(slide, Inches(0.5), Inches(4.6), Inches(12.3), Inches(0.35),
                text="Lo que NO decide la Junta hoy:",
                font_size=11, bold=True, color=C_GRIS_MEDIO, font_name="Calibri")
    no_decide = [
        "Vera P-5 (mecanismo NTC): tarea tecnica paralela de I&D Genteca",
        "Verificacion SAPI VE: aplica solo si gana V2; carga externa al equipo de contenido",
        "Datasheet I&D < 30 ms: condicion de imprenta vigente, sin cambio",
    ]
    for i, item in enumerate(no_decide):
        add_textbox(slide, Inches(0.7), Inches(4.95 + i * 0.38), Inches(12.0), Inches(0.36),
                    text="-- " + item, font_size=10.5, color=C_GRIS_LINEA,
                    font_name="Calibri")

    footer_bar(slide, "Genteca | Junta Directiva | 2026-05-06 | Confidencial")


# ---------------------------------------------------------------------------
# SLIDES — ANEXO (A1–A5)
# Paleta neutra: C_ANEXO_HDR (casi negro) + C_ANEXO_ACENTO (dorado opaco)
# Sin codigo de color de variante. Marcado visualmente como sección separada.
# ---------------------------------------------------------------------------

def slide_anexo_apertura(prs):
    """Slide A1 — Apertura del anexo."""
    slide = add_slide(prs)

    # Fondo crema calido — diferencia visual del cuerpo principal
    add_rect_bg(slide, Inches(0), Inches(0), W, H, C_ANEXO_FONDO)

    title_bar_anexo(
        slide,
        "Bautizado en anglicismos como estrategia de IP defensiva",
        "Analisis exploratorio para discusion posterior"
    )
    footer_bar_anexo(slide, "A1 de 5")

    # Linea acento dorado opaco
    add_rect_bg(slide, Inches(0), Inches(3.2), W, Inches(0.05), C_ANEXO_ACENTO)

    # Texto de apertura
    add_rect_bg(slide, Inches(0.5), Inches(1.35), Inches(12.3), Inches(1.65),
                C_BLANCO, border_color=C_ANEXO_ACENTO)
    add_textbox(slide, Inches(0.7), Inches(1.5), Inches(11.9), Inches(1.4),
                text=(
                    "Las opciones presentadas en el cuerpo principal no incluyen este enfoque. "
                    "Esta seccion es un abreboca a discusiones futuras sobre como blindar legalmente "
                    "cada innovacion tecnica de Genteca."
                ),
                font_size=15, color=C_GRIS_OSCURO, font_name="Calibri Light")

    # Tres proposiciones clave en columnas
    props = [
        ("Registro mas probable",
         "SAPI VE registra con mayor probabilidad palabras inventadas o anglicismos no descriptivos "
         "que descriptores comunes en espanol."),
        ("Barrera competitiva real",
         "Si Genteca registra la marca en angliсismo, la competencia que copie la placa nunca podra "
         "usar ese nombre en su empaque -- aunque tenga el componente."),
        ("Posicionamiento premium",
         "Los anglicismos transmiten estandar internacional. Refuerzan el posicionamiento "
         "Exceline Profesional en el canal ferretero VE."),
    ]

    col_w = Inches(3.8)
    col_xs = [Inches(0.5), Inches(4.65), Inches(8.8)]

    for col_x, prop in zip(col_xs, props):
        add_rect_bg(slide, col_x, Inches(3.45), col_w, Inches(2.9),
                    C_BLANCO, border_color=C_GRIS_LINEA)
        add_rect_bg(slide, col_x, Inches(3.45), col_w, Inches(0.06), C_ANEXO_ACENTO)
        add_textbox(slide, col_x + Inches(0.15), Inches(3.6), col_w - Inches(0.3), Inches(0.42),
                    text=prop[0], font_size=12, bold=True, color=C_ANEXO_ACENTO,
                    font_name="Calibri")
        add_textbox(slide, col_x + Inches(0.15), Inches(4.08), col_w - Inches(0.3), Inches(2.1),
                    text=prop[1], font_size=10.5, color=C_GRIS_OSCURO, font_name="Calibri")


def slide_anexo_por_que(prs):
    """Slide A2 — Por que los anglicismos: 3 razones."""
    slide = add_slide(prs)
    add_rect_bg(slide, Inches(0), Inches(0), W, H, C_ANEXO_FONDO)

    title_bar_anexo(
        slide,
        "Por que registrar en anglicismos",
        "Tres razones estructurales -- no es estetica, es estrategia de IP"
    )
    footer_bar_anexo(slide, "A2 de 5")

    razones = [
        {
            "num": "1",
            "titulo": "Mayor probabilidad de registro exitoso en SAPI VE",
            "texto": (
                "El SAPI Venezuela registra con mayor facilidad palabras inventadas o anglicismos no descriptivos "
                "que descriptores comunes en espanol. \"Escudo Termico\" es descriptivo puro -- riesgo medio-alto "
                "de objecion. \"Thermo-Safe\" o \"Thermal Shield\" no describen el mecanismo del producto: "
                "perfil mas limpio para registro formal."
            ),
        },
        {
            "num": "2",
            "titulo": "La marca registrada en anglicismo blinda a Genteca frente a copias",
            "texto": (
                "Si un competidor replica la placa NTC -- situacion hipotetica pero plausible dado el costo bajo "
                "del componente --, jamas podra usar el nombre registrado de Genteca en su empaque. "
                "El producto puede ser fisicamente identico; el nombre no puede copiarse sin exposicion legal. "
                "Esto convierte el bautizado en una barrera competitiva que el hardware solo no puede proveer."
            ),
        },
        {
            "num": "3",
            "titulo": "Sofisticacion percibida: anglicismos = estandar internacional",
            "texto": (
                "En el canal ferretero VE, los instaladores tecnicos -- prescriptores del 80% de la decision "
                "de compra -- asocian anglicismos en empaque electrico con calidad tecnica superior. "
                "\"Inverter\", \"digital\", \"smart\" ya circulan sin friccion. \"Thermo-Safe\" sigue ese patron. "
                "Refuerza el posicionamiento Exceline Profesional sin costo adicional."
            ),
        },
    ]

    y = Inches(1.28)
    colors_num = [C_ANEXO_ACENTO, C_AZUL_OSCURO, C_GRIS_OSCURO]
    for i, r in enumerate(razones):
        rh = Inches(1.68)
        add_rect_bg(slide, Inches(0.35), y, Inches(12.6), rh,
                    C_BLANCO, border_color=C_GRIS_LINEA)
        # Numero en acento
        add_rect_bg(slide, Inches(0.35), y, Inches(0.55), rh, colors_num[i])
        add_textbox(slide, Inches(0.35), y + Inches(0.55), Inches(0.55), Inches(0.5),
                    text=r["num"], font_size=20, bold=True, color=C_BLANCO,
                    align=PP_ALIGN.CENTER, font_name="Calibri")
        # Titulo
        add_textbox(slide, Inches(1.02), y + Inches(0.1), Inches(11.7), Inches(0.38),
                    text=r["titulo"], font_size=12, bold=True, color=C_ANEXO_HDR,
                    font_name="Calibri")
        # Texto
        add_textbox(slide, Inches(1.02), y + Inches(0.48), Inches(11.7), Inches(1.1),
                    text=r["texto"], font_size=10.5, color=C_GRIS_OSCURO, font_name="Calibri")
        y += rh + Inches(0.07)


def slide_anexo_candidatos(prs):
    """Slide A3 — Candidatos en anglicismos para proteccion termica."""
    slide = add_slide(prs)
    add_rect_bg(slide, Inches(0), Inches(0), W, H, C_ANEXO_FONDO)

    title_bar_anexo(
        slide,
        "Candidatos en anglicismos -- proteccion termica",
        "Territorio competitivo VE -- snapshot Orlan OL-1 §Refresh 2026-05-06"
    )
    footer_bar_anexo(slide, "A3 de 5")

    # Encabezado de tabla
    cols = [Inches(2.8), Inches(3.2), Inches(3.2), Inches(2.8)]
    headers = ["Candidato", "Vacancia VE (clase 9)", "Conflicto detectado", "Perfil de riesgo IP"]
    col_xs = [Inches(0.4), Inches(3.25), Inches(6.5), Inches(9.75)]

    y_hdr = Inches(1.22)
    for i, (hdr, cw, cx) in enumerate(zip(headers, cols, col_xs)):
        add_rect_bg(slide, cx, y_hdr, cw, Inches(0.44), C_ANEXO_HDR)
        add_textbox(slide, cx + Inches(0.1), y_hdr + Inches(0.08), cw - Inches(0.2), Inches(0.32),
                    text=hdr, font_size=10, bold=True, color=C_BLANCO, font_name="Calibri")

    candidatos = [
        ("Thermo-Safe",
         "Vacante -- ningún uso en protectores electricos VE",
         "Sin conflicto detectado (preliminar)",
         "Bajo -- perfil mas limpio del grupo"),
        ("Thermal Shield",
         "Vacante -- ningún uso en protectores electricos VE",
         "Sin conflicto detectado en clase 9 (preliminar)",
         "Bajo -- uso en otros rubros (embalajes, tejados), no eléctrico"),
        ("Thermo-Shield",
         "Vacante -- ningún uso en protectores electricos VE",
         "Sin conflicto detectado en clase 9 (preliminar)",
         "Bajo -- situacion similar a Thermal Shield"),
        ("Escudo Termico",
         "Vacante en protectores electricos VE",
         "Sin conflicto en clase 9 -- pero uso extenso en espanol como generico",
         "Medio-alto -- descriptor puro en espanol, riesgo de objecion SAPI por descriptividad"),
    ]

    y = y_hdr + Inches(0.44)
    for j, (nombre, vacancia, conflicto, riesgo) in enumerate(candidatos):
        rh = Inches(0.92)
        bg = C_BLANCO if j % 2 == 0 else RGBColor(0xF7, 0xF5, 0xF0)
        for i, (texto, cw, cx) in enumerate(zip([nombre, vacancia, conflicto, riesgo], cols, col_xs)):
            add_rect_bg(slide, cx, y, cw, rh, bg, border_color=C_GRIS_LINEA)
            is_name = (i == 0)
            add_textbox(slide, cx + Inches(0.1), y + Inches(0.1),
                        cw - Inches(0.2), rh - Inches(0.15),
                        text=texto, font_size=10, bold=is_name,
                        color=C_ANEXO_ACENTO if is_name else C_GRIS_OSCURO,
                        font_name="Calibri")
        y += rh

    # Nota obligatoria
    y += Inches(0.12)
    add_rect_bg(slide, Inches(0.4), y, Inches(12.5), Inches(0.5),
                RGBColor(0xFF, 0xF8, 0xE8), border_color=C_ANEXO_ACENTO)
    add_textbox(slide, Inches(0.55), y + Inches(0.08), Inches(12.2), Inches(0.38),
                text=(
                    "Nota obligatoria: Cualquiera de estas opciones requiere verificacion SAPI VE con abogado marcario "
                    "antes de imprenta. Los datos de Orlan son orientativos, no sustituto de consulta registral formal."
                ),
                font_size=9.5, italic=True, color=RGBColor(0x6B, 0x4E, 0x10), font_name="Calibri")


def slide_anexo_expansivo(prs):
    """Slide A4 — Aplicacion expansiva: mas alla de la proteccion termica."""
    slide = add_slide(prs)
    add_rect_bg(slide, Inches(0), Inches(0), W, H, C_ANEXO_FONDO)

    title_bar_anexo(
        slide,
        "Aplicacion expansiva: cada innovacion es un activo comercial",
        "El patron de bautizado puede aplicarse a toda la cartera de IP de Genteca"
    )
    footer_bar_anexo(slide, "A4 de 5")

    # Caja concepto
    add_rect_bg(slide, Inches(0.4), Inches(1.25), Inches(12.5), Inches(0.72),
                C_BLANCO, border_color=C_ANEXO_ACENTO)
    add_rect_bg(slide, Inches(0.4), Inches(1.25), Inches(0.08), Inches(0.72), C_ANEXO_ACENTO)
    add_textbox(slide, Inches(0.6), Inches(1.35), Inches(12.1), Inches(0.55),
                text=(
                    "Si Genteca adopta el habito de bautizar cada innovacion tecnica con nombre de marca propio, "
                    "cada avance de I&D se convierte en un activo comercial blindado -- no solo una caracteristica del producto."
                ),
                font_size=12, color=C_GRIS_OSCURO, font_name="Calibri")

    # Grid de ejemplos
    ejemplos = [
        {
            "innovacion": "Proteccion termica (NTC)",
            "aplicacion": "Thermo-Safe / Thermal Shield / Thermo-Shield",
            "efecto": "Competidor con NTC no puede usar el nombre registrado en su empaque.",
            "estado": "En evaluacion hoy",
        },
        {
            "innovacion": "Curva inversa de voltaje",
            "aplicacion": "Nombre de marca para el algoritmo de disparo (ej. VoltCurve)",
            "efecto": "Diferencia a Genteca como empresa de software de proteccion, no solo hardware.",
            "estado": "Exploratorio",
        },
        {
            "innovacion": "Algoritmo del microcontrolador",
            "aplicacion": "Nombre de firmware / motor de decision (ej. ProGuard Engine)",
            "efecto": "El 'cerebro' del protector se vuelve activo con nombre y barrera de marca.",
            "estado": "Exploratorio",
        },
        {
            "innovacion": "Software de control / UI",
            "aplicacion": "Nombre comercial propietario para la plataforma de gestion",
            "efecto": "Cada version del software puede tener numero de version y nombre de marca.",
            "estado": "Exploratorio",
        },
    ]

    y = Inches(2.12)
    col_xs = [Inches(0.4), Inches(3.5), Inches(7.3), Inches(10.5)]
    col_ws = [Inches(3.05), Inches(3.75), Inches(3.15), Inches(2.4)]
    col_hdrs = ["Innovacion", "Aplicacion de bautizado", "Efecto de barrera", "Estado"]

    # Headers
    for cx, cw, hdr in zip(col_xs, col_ws, col_hdrs):
        add_rect_bg(slide, cx, y, cw, Inches(0.36), C_ANEXO_HDR)
        add_textbox(slide, cx + Inches(0.08), y + Inches(0.06), cw - Inches(0.15), Inches(0.26),
                    text=hdr, font_size=9.5, bold=True, color=C_BLANCO, font_name="Calibri")
    y += Inches(0.36)

    for k, ej in enumerate(ejemplos):
        rh = Inches(0.96)
        bg = C_BLANCO if k % 2 == 0 else RGBColor(0xF7, 0xF5, 0xF0)
        valores = [ej["innovacion"], ej["aplicacion"], ej["efecto"], ej["estado"]]
        for cx, cw, val in zip(col_xs, col_ws, valores):
            add_rect_bg(slide, cx, y, cw, rh, bg, border_color=C_GRIS_LINEA)
            is_estado = (val == ej["estado"])
            fc = C_ANEXO_ACENTO if ej["estado"] == "En evaluacion hoy" and is_estado else C_GRIS_OSCURO
            add_textbox(slide, cx + Inches(0.08), y + Inches(0.08),
                        cw - Inches(0.15), rh - Inches(0.12),
                        text=val, font_size=9.5,
                        bold=(is_estado and ej["estado"] == "En evaluacion hoy"),
                        color=fc, font_name="Calibri")
        y += rh

    # Nota aclaratoria
    y += Inches(0.1)
    add_textbox(slide, Inches(0.4), y, Inches(12.5), Inches(0.32),
                text="Nota: los nombres de ejemplo (VoltCurve, ProGuard Engine) son ilustrativos. "
                     "Este anexo no propone nombres especificos -- establece el patron.",
                font_size=9, italic=True, color=C_GRIS_MEDIO, font_name="Calibri")


def slide_anexo_pregunta(prs):
    """Slide A5 — Pregunta abierta a Junta."""
    slide = add_slide(prs)
    add_rect_bg(slide, Inches(0), Inches(0), W, H, C_ANEXO_HDR)

    # Franja acento dorado opaco
    add_rect_bg(slide, Inches(0), Inches(3.6), W, Inches(0.06), C_ANEXO_ACENTO)

    footer_bar_anexo(slide, "A5 de 5")

    # Etiqueta ANEXO
    add_rect_bg(slide, Inches(0.5), Inches(0.5), Inches(1.6), Inches(0.38), C_ANEXO_ACENTO)
    add_textbox(slide, Inches(0.55), Inches(0.55), Inches(1.5), Inches(0.3),
                text="ANEXO", font_size=11, bold=True, color=C_BLANCO,
                align=PP_ALIGN.CENTER, font_name="Calibri")

    add_textbox(slide, Inches(0.5), Inches(1.08), Inches(12.3), Inches(0.75),
                text="Preguntas abiertas para la Junta",
                font_size=28, bold=True, color=C_ANEXO_ACENTO, font_name="Calibri Light")

    add_textbox(slide, Inches(0.5), Inches(1.82), Inches(12.3), Inches(0.48),
                text="Estas preguntas no demandan decision hoy. Son semilla para conversacion posterior.",
                font_size=13, italic=True, color=C_GRIS_LINEA, font_name="Calibri Light")

    preguntas = [
        ("¿Vale la pena explorar este enfoque sistematico de bautizado de innovaciones?",
         "El cuerpo principal de hoy ya abre esa puerta con el badge termico. "
         "La pregunta es si Genteca lo adopta como habito sistematico para toda la cartera de IP."),
        ("¿Para que innovaciones de Genteca tendria mas sentido empezar?",
         "La curva inversa de voltaje, el algoritmo del microcontrolador, el software de control: "
         "cada uno es candidato a bautizado. ¿Cual tiene mayor prioridad comercial?"),
        ("¿Que presupuesto comercial-legal considerar para implementarlo?",
         "Cada bautizado formal requiere consulta con abogado marcario y registro SAPI VE. "
         "La economia de escala favorece registrar varios en un mismo proceso."),
    ]

    y = Inches(2.5)
    for i, (pregunta, contexto) in enumerate(preguntas):
        rh = Inches(1.42)
        add_rect_bg(slide, Inches(0.4), y, Inches(0.06), rh, C_ANEXO_ACENTO)
        add_rect_bg(slide, Inches(0.5), y, Inches(12.4), rh,
                    RGBColor(0x1A, 0x1A, 0x1A), border_color=RGBColor(0x3A, 0x3A, 0x3A))
        add_textbox(slide, Inches(0.68), y + Inches(0.1), Inches(12.1), Inches(0.42),
                    text=pregunta, font_size=13, bold=True, color=C_BLANCO, font_name="Calibri")
        add_textbox(slide, Inches(0.68), y + Inches(0.54), Inches(12.1), Inches(0.82),
                    text=contexto, font_size=10.5, color=C_GRIS_LINEA, font_name="Calibri")
        y += rh + Inches(0.06)


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def build():
    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H

    # --- CUERPO PRINCIPAL ---
    # Slide 1 — Portada
    slide_portada(prs)

    # Slide 2 — Contexto y pregunta
    slide_contexto(prs)

    # Slide 3 — Comparacion lado a lado
    slide_comparacion(prs)

    # Slide 4 — Variante 1: tiro completo
    slide_tiro(prs, "V1", TIRO_CLAIM2_V1, C_GRIS_V1, C_GRIS_V1_CLR)

    # Slide 5 — Variante 1: retiro CARACTERISTICAS
    slide_retiro_caract(prs, "V1", CARACT_TERMICO_V1, C_GRIS_V1, C_GRIS_V1_CLR)

    # Slide 6 — CAVEATS COMPARTIDOS (velocidad + inverter — identicos en V1 y V2)
    slide_caveats_compartidos(prs)

    # Slide 7 — Variante 1: caveat termico especifico
    slide_caveat_termico(prs, "V1", CAVEAT_TERMICO_V1, C_GRIS_V1, C_GRIS_V1_CLR)

    # Slide 8 — Variante 2: tiro completo
    slide_tiro(prs, "V2", TIRO_CLAIM2_V2, C_AZUL_V2, C_AZUL_V2_CLR)

    # Slide 9 — Variante 2: retiro CARACTERISTICAS
    slide_retiro_caract(prs, "V2", CARACT_TERMICO_V2, C_AZUL_V2, C_AZUL_V2_CLR)

    # Slide 10 — Variante 2: caveat termico especifico
    slide_caveat_termico(prs, "V2", CAVEAT_TERMICO_V2, C_AZUL_V2, C_AZUL_V2_CLR)

    # Slide 11 — Argumentos por variante
    slide_argumentos(prs)

    # Slide 12 — Riesgos y condiciones
    slide_riesgos(prs)

    # Slide 13 — Posicion del equipo
    slide_recomendacion(prs)

    # Slide 14 — Proximos pasos
    slide_proximos_pasos(prs)

    # Slide 15 — Cierre
    slide_cierre(prs)

    # --- ANEXO ---
    # Slide A1 — Apertura del anexo
    slide_anexo_apertura(prs)

    # Slide A2 — Por que los anglicismos
    slide_anexo_por_que(prs)

    # Slide A3 — Candidatos anglicismos
    slide_anexo_candidatos(prs)

    # Slide A4 — Aplicacion expansiva
    slide_anexo_expansivo(prs)

    # Slide A5 — Pregunta abierta
    slide_anexo_pregunta(prs)

    out_path = (
        "C:/Raul/03-projects/genteca/2026-04_GSM-MB-RB-RF_empaque"
        "/03-review-and-release/Junta_PPTX_v3"
        "/Avance_dual-variantes_GSM-empaque_2026-05-06.pptx"
    )
    prs.save(out_path)
    print(f"Archivo generado: {out_path}")
    return out_path


if __name__ == "__main__":
    build()
