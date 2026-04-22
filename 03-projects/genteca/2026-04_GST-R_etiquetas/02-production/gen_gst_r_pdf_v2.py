"""
Generador PDF — GST-R Brief de Etiquetas v2
Para Ozwaldo (Diseñador Gráfico) — Genteca / Exceline Profesional
Nota: fuente del cuerpo es Helvetica (sustituto PDF de Montserrat).
      La fuente final en los artes es Montserrat (tipografía oficial Exceline Profesional).
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame
from reportlab.lib.colors import HexColor
import os

# ─── Rutas de salida ──────────────────────────────────────────────────────────
OUT_WIP   = r"C:\WorkspaceIA\PROJECTS\Genteca\Work In Progress\GST-R_etiquetas_brief_v2.pdf"
OUT_INBOX = r"C:\WorkspaceIA\Owner Inbox\2026-04-20-gst-r-etiquetas-brief-ozwaldo-v2.pdf"

# ─── Colores ──────────────────────────────────────────────────────────────────
COL_GREEN  = HexColor("#2E7D32")   # verde industrial (placeholder — Ozwaldo usa Pantone)
COL_BLACK  = HexColor("#1A1A1A")   # negro encabezado ProDigital
COL_GOLD   = HexColor("#B8960C")   # dorado oscuro elegante ProDigital
COL_GRAY   = HexColor("#424242")   # gris oscuro industrial ProMotor
COL_BLUE   = HexColor("#0D47A1")   # azul refrigeración ProFrio (placeholder — Pantone línea monofásica)
COL_ORANGE = HexColor("#E65100")   # naranja acento (misma línea monofásica)
COL_WHITE  = colors.white
COL_LIGHT  = HexColor("#F5F5F5")   # fondo sección claro
COL_COVER_BG = HexColor("#212121") # fondo portada

PAGE_W, PAGE_H = A4  # 210 × 297 mm

# ─── Estilos ──────────────────────────────────────────────────────────────────
def make_styles():
    s = {}
    # Body base
    s["body"] = ParagraphStyle("body",
        fontName="Helvetica", fontSize=9, leading=13, textColor=colors.black,
        spaceAfter=4)
    s["body_white"] = ParagraphStyle("body_white",
        fontName="Helvetica", fontSize=9, leading=13, textColor=COL_WHITE,
        spaceAfter=4)
    s["bold"] = ParagraphStyle("bold",
        fontName="Helvetica-Bold", fontSize=9, leading=13, textColor=colors.black,
        spaceAfter=4)
    s["bold_white"] = ParagraphStyle("bold_white",
        fontName="Helvetica-Bold", fontSize=9, leading=13, textColor=COL_WHITE,
        spaceAfter=4)
    # Section header (A, B, C)
    s["sec_head"] = ParagraphStyle("sec_head",
        fontName="Helvetica-Bold", fontSize=11, leading=15, textColor=COL_ORANGE,
        spaceBefore=10, spaceAfter=4, borderPad=2)
    # Product name big
    s["prod_name"] = ParagraphStyle("prod_name",
        fontName="Helvetica-Bold", fontSize=26, leading=30, textColor=COL_WHITE,
        alignment=TA_LEFT, spaceAfter=2)
    s["prod_code"] = ParagraphStyle("prod_code",
        fontName="Helvetica", fontSize=11, leading=14, textColor=COL_WHITE,
        alignment=TA_LEFT, spaceAfter=2)
    # Cover styles
    s["cover_title"] = ParagraphStyle("cover_title",
        fontName="Helvetica-Bold", fontSize=22, leading=28, textColor=COL_WHITE,
        alignment=TA_CENTER, spaceAfter=6)
    s["cover_sub"] = ParagraphStyle("cover_sub",
        fontName="Helvetica", fontSize=12, leading=16, textColor=HexColor("#BDBDBD"),
        alignment=TA_CENTER, spaceAfter=4)
    s["cover_product"] = ParagraphStyle("cover_product",
        fontName="Helvetica-Bold", fontSize=13, leading=17, textColor=COL_WHITE,
        alignment=TA_LEFT, spaceAfter=2)
    s["cover_note"] = ParagraphStyle("cover_note",
        fontName="Helvetica-Oblique", fontSize=8, leading=11,
        textColor=HexColor("#9E9E9E"), alignment=TA_CENTER, spaceAfter=2)
    # Footer / note
    s["footer_note"] = ParagraphStyle("footer_note",
        fontName="Helvetica-Oblique", fontSize=7.5, leading=10,
        textColor=HexColor("#757575"), alignment=TA_CENTER)
    s["label_body"] = ParagraphStyle("label_body",
        fontName="Courier", fontSize=8.5, leading=12, textColor=colors.black,
        spaceAfter=2, leftIndent=6)
    s["pending"] = ParagraphStyle("pending",
        fontName="Helvetica", fontSize=8.5, leading=12,
        textColor=HexColor("#B71C1C"), spaceAfter=3, leftIndent=6)
    s["resolved"] = ParagraphStyle("resolved",
        fontName="Helvetica", fontSize=8.5, leading=12,
        textColor=HexColor("#1B5E20"), spaceAfter=3, leftIndent=6)
    return s

ST = make_styles()

# ─── Helpers ──────────────────────────────────────────────────────────────────

def hr(color=HexColor("#BDBDBD"), thickness=0.5):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=4, spaceBefore=4)

def spacer(h_mm=3):
    return Spacer(1, h_mm * mm)

def header_table(product_name, product_code, descriptor, bg_color, text_color=None,
                 accent_color=None, gold_border=False):
    """Builds the colored header block for each product page."""
    if text_color is None:
        text_color = COL_WHITE

    name_p = Paragraph(product_name, ParagraphStyle("hn",
        fontName="Helvetica-Bold", fontSize=28, leading=32,
        textColor=text_color, alignment=TA_LEFT))
    code_p = Paragraph(product_code, ParagraphStyle("hc",
        fontName="Helvetica-Bold", fontSize=12, leading=15,
        textColor=text_color, alignment=TA_LEFT))
    desc_p = Paragraph(descriptor, ParagraphStyle("hd",
        fontName="Helvetica", fontSize=9.5, leading=13,
        textColor=text_color, alignment=TA_LEFT))
    brand_p = Paragraph("EXCELINE PROFESIONAL  |  Genteca",
        ParagraphStyle("hbrand",
            fontName="Helvetica-Bold", fontSize=9, leading=12,
            textColor=accent_color or COL_ORANGE if bg_color not in [COL_BLACK] else COL_GOLD,
            alignment=TA_RIGHT))

    inner = [[name_p, brand_p],
             [code_p, ""],
             [desc_p, ""]]

    t = Table(inner, colWidths=[130*mm, 55*mm])
    style = [
        ("BACKGROUND", (0,0), (-1,-1), bg_color),
        ("TOPPADDING",   (0,0), (-1,-1), 10),
        ("BOTTOMPADDING",(0,0), (-1,-1), 10),
        ("LEFTPADDING",  (0,0), (-1,-1), 14),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("VALIGN",       (0,0), (-1,-1), "MIDDLE"),
        ("SPAN",         (0,1), (0,2)),   # code spans rows
        ("SPAN",         (0,2), (0,2)),
        ("ALIGN",        (1,0), (1,0), "RIGHT"),
    ]
    if gold_border:
        style += [
            ("BOX",       (0,0), (-1,-1), 2.5, COL_GOLD),
            ("LINEBELOW", (0,0), (-1,0),  1.5, COL_GOLD),
        ]
    t.setStyle(TableStyle(style))
    return t

def section_header(letter, title):
    return Paragraph(f"<b>SECCIÓN {letter} — {title}</b>", ST["sec_head"])

def bullet_line(text, style=None):
    if style is None:
        style = ST["body"]
    return Paragraph(f"&#x2022;  {text}", style)

def label_copy_block(lines):
    """Renders the copy block in monospace (simulating label layout)."""
    items = []
    items.append(Spacer(1, 2*mm))
    for line in lines:
        if line.startswith("━"):
            items.append(hr(color=HexColor("#455A64"), thickness=1))
        elif line == "":
            items.append(Spacer(1, 1*mm))
        else:
            items.append(Paragraph(line, ST["label_body"]))
    items.append(Spacer(1, 2*mm))
    # wrap in light-bg table
    t = Table([[items]], colWidths=[185*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND",   (0,0), (-1,-1), HexColor("#ECEFF1")),
        ("BOX",          (0,0), (-1,-1), 0.5, HexColor("#90A4AE")),
        ("TOPPADDING",   (0,0), (-1,-1), 6),
        ("BOTTOMPADDING",(0,0), (-1,-1), 6),
        ("LEFTPADDING",  (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
    ]))
    return t

def footer_text():
    return "Brief de Etiquetas GST-R — v2 — Confidencial Genteca"

# ─── Page templates ──────────────────────────────────────────────────────────

class GSTDoc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        super().__init__(filename, pagesize=A4,
                         leftMargin=12*mm, rightMargin=12*mm,
                         topMargin=12*mm, bottomMargin=18*mm, **kw)
        frame = Frame(self.leftMargin, self.bottomMargin,
                      self.width, self.height, id="main")
        self.addPageTemplates([PageTemplate(id="default", frames=[frame],
                                            onPage=self._draw_footer)])

    def _draw_footer(self, canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica-Oblique", 7)
        canvas.setFillColor(HexColor("#9E9E9E"))
        canvas.drawCentredString(PAGE_W / 2, 10*mm, footer_text())
        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(HexColor("#BDBDBD"))
        canvas.drawRightString(PAGE_W - 12*mm, 10*mm, f"Pág. {doc.page}")
        canvas.restoreState()


# ─── Cover page ───────────────────────────────────────────────────────────────

def build_cover():
    story = []

    # Big dark background via table trick
    cover_rows = [
        [Paragraph("Brief de Diseño", ParagraphStyle("ct1",
            fontName="Helvetica", fontSize=14, leading=18,
            textColor=HexColor("#BDBDBD"), alignment=TA_CENTER))],
        [Paragraph("Etiquetas GST-R — Nueva Línea Trifásica", ParagraphStyle("ct2",
            fontName="Helvetica-Bold", fontSize=20, leading=26,
            textColor=COL_WHITE, alignment=TA_CENTER))],
        [Spacer(1, 4*mm)],
        [Paragraph("EXCELINE PROFESIONAL  |  Genteca", ParagraphStyle("ct3",
            fontName="Helvetica-Bold", fontSize=11, leading=15,
            textColor=COL_ORANGE, alignment=TA_CENTER))],
        [Spacer(1, 2*mm)],
        [Paragraph("Versión 2  |  Fecha: 2026-04-20", ParagraphStyle("ct4",
            fontName="Helvetica", fontSize=10, leading=13,
            textColor=HexColor("#9E9E9E"), alignment=TA_CENTER))],
        [Spacer(1, 10*mm)],
        [hr(color=HexColor("#424242"), thickness=1)],
        [Spacer(1, 6*mm)],
        [Paragraph("Productos incluidos en este brief:", ParagraphStyle("cp0",
            fontName="Helvetica-Bold", fontSize=11, leading=14,
            textColor=HexColor("#BDBDBD"), alignment=TA_LEFT))],
        [Spacer(1, 3*mm)],
    ]

    # Product cards
    products = [
        ("GST-RT · ProTransfer", "Supervisor Trifásico de Voltaje para Tableros y Transferencias",
         COL_GREEN, "VERDE"),
        ("GST-RD · ProDigital",  "Supervisor Trifásico Digital de Voltaje",
         COL_BLACK, "NEGRO + DORADO OSCURO"),
        ("GST-RM · ProMotor",    "Supervisor Trifásico de Voltaje para Motores y Bombas",
         COL_GRAY, "GRIS"),
        ("GST-RR · ProFrio",     "Supervisor Trifásico de Voltaje para Refrigeración y A/A",
         COL_BLUE, "AZUL"),
    ]
    for (pname, pdesc, pcol, pcolor_name) in products:
        prow = Table([[
            Paragraph(f"<b>{pname}</b>", ParagraphStyle("pp1",
                fontName="Helvetica-Bold", fontSize=12, leading=15,
                textColor=COL_WHITE)),
            Paragraph(pdesc, ParagraphStyle("pp2",
                fontName="Helvetica", fontSize=8.5, leading=12,
                textColor=HexColor("#BDBDBD"))),
            Paragraph(pcolor_name, ParagraphStyle("pp3",
                fontName="Helvetica-Bold", fontSize=8, leading=11,
                textColor=COL_ORANGE, alignment=TA_RIGHT)),
        ]], colWidths=[58*mm, 90*mm, 37*mm])
        prow.setStyle(TableStyle([
            ("BACKGROUND",   (0,0), (-1,-1), pcol),
            ("TOPPADDING",   (0,0), (-1,-1), 8),
            ("BOTTOMPADDING",(0,0), (-1,-1), 8),
            ("LEFTPADDING",  (0,0), (0,-1),  10),
            ("LEFTPADDING",  (1,0), (1,-1),   6),
            ("RIGHTPADDING", (-1,0),(-1,-1), 10),
            ("VALIGN",       (0,0), (-1,-1), "MIDDLE"),
            ("BOX",          (0,0), (-1,-1), 0.5, HexColor("#424242")),
        ]))
        cover_rows.append([prow])
        cover_rows.append([Spacer(1, 2*mm)])

    cover_rows += [
        [Spacer(1, 8*mm)],
        [hr(color=HexColor("#424242"), thickness=1)],
        [Spacer(1, 4*mm)],
        [Paragraph(
            "Dirigido a: Ozwaldo (Diseñador Gráfico) · Keiddys (aprobación)<br/>"
            "Preparado por: Oz — Technical Documentation Editor",
            ParagraphStyle("cfooter",
                fontName="Helvetica", fontSize=8.5, leading=12,
                textColor=HexColor("#9E9E9E"), alignment=TA_CENTER))],
        [Spacer(1, 4*mm)],
        [Paragraph(
            "<i>NOTA TIPOGRAFÍA: Este PDF usa Helvetica como sustituto de cuerpo. "
            "La tipografía oficial para los artes finales es <b>Montserrat</b> "
            "(tipografía oficial Exceline Profesional).</i>",
            ParagraphStyle("cnote",
                fontName="Helvetica-Oblique", fontSize=7.5, leading=11,
                textColor=HexColor("#757575"), alignment=TA_CENTER))],
    ]

    cover_t = Table(cover_rows, colWidths=[185*mm])
    cover_t.setStyle(TableStyle([
        ("BACKGROUND",   (0,0), (-1,-1), COL_COVER_BG),
        ("TOPPADDING",   (0,0), (-1,-1), 3),
        ("BOTTOMPADDING",(0,0), (-1,-1), 3),
        ("LEFTPADDING",  (0,0), (-1,-1), 16),
        ("RIGHTPADDING", (0,0), (-1,-1), 16),
        ("BOX",          (0,0), (-1,-1), 1, HexColor("#424242")),
    ]))
    story.append(cover_t)
    story.append(PageBreak())
    return story


# ─── Product pages ────────────────────────────────────────────────────────────

def build_product_page(product_name, product_code, descriptor,
                       bg_color, gold_border,
                       copy_lines, app_bullets, char_bullets,
                       data_tech, models,
                       design_notes,
                       resolved_items, pending_items,
                       add_page_break=True):
    story = []

    # Header
    story.append(header_table(
        product_name, product_code, descriptor,
        bg_color, gold_border=gold_border,
        accent_color=COL_GOLD if gold_border else COL_ORANGE))
    story.append(spacer(3))

    # ── SECCIÓN A ──────────────────────────────────────────────
    story.append(section_header("A", "Copy listo para Ozwaldo"))
    story.append(spacer(1))

    all_copy_lines = (
        ["━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
         f"[ENCABEZADO — color según instrucciones]",
         product_name,
         f"{product_code} — {descriptor}",
         "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
         "",
         "[APLICACIONES]"] +
        [f"• {a}" for a in app_bullets] +
        ["",
         "[CARACTERÍSTICAS CLAVE]"] +
        [f"• {c}" for c in char_bullets] +
        ["", "[DATOS TÉCNICOS]",
         data_tech,
         "",
         "[MODELOS]",
         models,
         "",
         "[PIE]",
         "[Logo Exceline Profesional]   [Logo Genteca]",
         "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"]
    )
    story.append(label_copy_block(all_copy_lines))
    story.append(spacer(3))

    # ── SECCIÓN B ──────────────────────────────────────────────
    story.append(section_header("B", "Notas de diseño para Ozwaldo"))
    story.append(spacer(1))
    for note in design_notes:
        if note.startswith("**") and note.endswith("**"):
            story.append(Paragraph(note[2:-2], ST["bold"]))
        elif note.startswith("  •"):
            story.append(Paragraph("    &#x25E6;  " + note[3:], ST["body"]))
        elif note.startswith("•"):
            story.append(bullet_line(note[1:].strip()))
        else:
            story.append(Paragraph(note, ST["body"]))
    story.append(spacer(3))

    # ── SECCIÓN C ──────────────────────────────────────────────
    story.append(section_header("C", "Decisiones resueltas y pendientes"))
    story.append(spacer(1))

    story.append(Paragraph("<b>Resueltas en esta sesión:</b>", ST["bold"]))
    for r in resolved_items:
        story.append(Paragraph("&#x2713;  " + r, ST["resolved"]))
    story.append(spacer(2))

    story.append(Paragraph("<b>Pendientes de confirmar:</b>", ST["bold"]))
    for i, p in enumerate(pending_items, 1):
        story.append(Paragraph(f"{i}.  {p}", ST["pending"]))

    if add_page_break:
        story.append(PageBreak())
    return story


# ─── Data definitions ─────────────────────────────────────────────────────────

PRODUCTS = [
    {
        "product_name": "ProTransfer",
        "product_code": "GST-RT",
        "descriptor":   "Supervisor Trifásico de Voltaje para Tableros y Transferencias",
        "bg_color":     COL_GREEN,
        "gold_border":  False,
        "app_bullets": [
            "Transferencias automáticas (ATS)",
            "Tableros generales de distribución",
            "Generadores de respaldo",
        ],
        "char_bullets": [
            "TD AJUSTABLE: 0,5–10 s",
            "TC MÍNIMO GARANTIZADO: 5 s",
            "IDEAL PARA ATS / TRANSFERENCIAS AUTOMÁTICAS",
        ],
        "data_tech": "TD: 0,5–10 s  |  TC: 5–600 s  |  Voltaje: 208/220 V~ (mod. 220) · 440/480 V~ (mod. 440)",
        "models":    "GST-RT220: 208/220 V~     GST-RT440: 440/480 V~",
        "design_notes": [
            "**Dimensiones:** 70 × 90 mm (punto de partida — ajustar según cara del producto). Casing: 80 × 100 × 38 mm.",
            "**Color dominante:** Verde — mismos Pantone de la línea monofásica Exceline Profesional (Ozwaldo los conoce). Texto: blanco. Acento: naranja (mismo de la línea monofásica).",
            "**Tipografía:** Montserrat — tipografía oficial Exceline Profesional.",
            "**Elemento visual prioritario:** Badge 'IDEAL PARA ATS / TRANSFERENCIAS' — segundo elemento de mayor peso después de ProTransfer.",
            "**Diales gráficos (2 diales):**",
            "  • Dial 1 — BAJO VOLTAJE (ajustable): rango 165–200 V~, zona naranja en rango sugerido ~185–195 V~",
            "  • Dial 2 — RECONEXIÓN TC (ajustable): rango 5–600 s, zona naranja en rango sugerido ~30–60 s",
            "  • Sobre voltaje fijo (264 V~) — valor en tabla, NO como dial.",
            "**Terminales:** Lateral izq.: L1, L2, L3  |  Lateral der.: 95 (COM), 96 (NC), 98 (NA)",
            "**Íconos sugeridos:** Tablero eléctrico / rack · Símbolo de transferencia (flecha bidireccional). NO incluir curva inversa.",
            "**Jerarquía visual (70 × 90 mm):** 1) ProTransfer (dominante) · 2) GST-RT + descriptor · 3) Aplicaciones (3 max) · 4) Bullets (3 max) · 5) Datos técnicos · 6) Modelos · 7) Logos (pie)",
        ],
        "resolved_items": [
            "Dimensiones casing confirmadas: 80 × 100 × 38 mm → etiqueta 70 × 90 mm sugerida.",
            "Sin frases comparativas ni referencias a competidores.",
            "Colores: mismos Pantone línea monofásica (Ozwaldo los maneja).",
            "Fuente confirmada: Montserrat.",
        ],
        "pending_items": [
            "¿El sobre voltaje del GST-RT es fijo (264 V~) o ajustable? Si ajustable → añadir tercer dial MÁXIMO V.",
            "Confirmación Pantone verde exacto con Keiddys (en caso de diferenciarse de la línea monofásica).",
            "¿La frase de argumento va impresa en la etiqueta o solo en material POP?",
        ],
    },
    {
        "product_name": "ProDigital",
        "product_code": "GST-RD",
        "descriptor":   "Supervisor Trifásico Digital de Voltaje",
        "bg_color":     COL_BLACK,
        "gold_border":  True,
        "app_bullets": [
            "Variadores de frecuencia y arrancadores suaves",
            "Subtableros industriales con equipos sensibles",
            "Controladores lógicos (PLC) y salas de control",
        ],
        "char_bullets": [
            "PANTALLA LCD DESMONTABLE — se monta en la puerta del tablero sin abrir el tablero",
            "HISTORIAL 20 FALLAS — tipo, valor, fase, fecha y hora",
            "REARME MANUAL / AUTO SELECCIONABLE",
        ],
        "data_tech": "TD: 1–30 s  |  TC: 0–600 s  |  Voltaje: 120 V~ · 208/220 V~ · 440/480 V~  |  Desbalance: 2–10%  |  IP20",
        "models":    "GST-RD120: 120 V~     GST-RD220: 208/220 V~     GST-RD440: 440/480 V~",
        "design_notes": [
            "**Tratamiento visual diferenciado:** Etiqueta NEGRA con BORDES DORADOS OSCUROS ELEGANTES — identidad exclusiva para ProDigital, diferente al resto de la línea. Negro + dorado oscuro = premium, digital, industrial de alta gama.",
            "**Dimensiones:** A definir por Ozwaldo según cara del producto. Punto de partida: 85 × 110 mm (casing 105 × 90 × 68 mm).",
            "**Tipografía:** Montserrat — tipografía oficial Exceline Profesional. Texto blanco sobre negro.",
            "**Elemento visual prioritario:** Pantalla LCD desmontable — representación gráfica de la pantalla mostrando valores de voltaje de las 3 fases (ej: VL1-L2: 218V / VL2-L3: 221V / VL3-L1: 219V). Incluir ícono o ilustración del concepto de pantalla separable del cuerpo del equipo → montaje en puerta de tablero.",
            "**SIN DIALES gráficos:** Ajuste digital por botones. NO incluir diales analógicos — confundirían al instalador.",
            "**Terminales:** Lateral izq.: L1, L2, L3  |  Lateral der.: 95 (COM), 96 (NC), 98 (NA)",
            "  • Nota: Puerto GIO para GIO-Link (Modbus RTU) disponible como accesorio opcional — mencionar si hay espacio.",
            "**Íconos sugeridos:** Pantalla LCD desmontable · Candado/contraseña · Historial/log de fallas · Rearme (flecha circular) · Montaje en puerta de tablero.",
            "**NOTA GIO-Link/Modbus:** El módulo GIO-Link (Modbus RTU/RS485) se vende por separado. NO incluir en bullets base. Si Keiddys lo decide: pequeña leyenda 'Compatible con GIO-Link Modbus RTU (accesorio opcional)' en pie.",
            "**Colores:** Usar mismos Pantone base de la línea monofásica adaptados al tratamiento negro/dorado. Ozwaldo los conoce.",
            "**Jerarquía visual:** 1) ProDigital (dominante) · 2) GST-RD + descriptor · 3) Aplicaciones (3 max) · 4) Bullets (3 max — pantalla desmontable + historial + rearme) · 5) Datos técnicos · 6) Modelos (3: 120/220/440) · 7) Logos (pie)",
        ],
        "resolved_items": [
            "Modbus eliminado del copy base — GIO-Link se vende por separado. Bullet reemplazado por 'REARME MANUAL / AUTO SELECCIONABLE'.",
            "Tres modelos confirmados: GST-RD120 / GST-RD220 / GST-RD440.",
            "Diferenciador visual principal: pantalla LCD desmontable (concepto de montaje en puerta de tablero sin abrir el tablero).",
            "Sin referencias comparativas — copy enfocado en características propias.",
            "Tratamiento visual: negro con bordes dorados oscuros elegantes.",
        ],
        "pending_items": [
            "Confirmación código de pedido GST-RD con I&D (nomenclatura final).",
            "¿Se añade mención al GIO-Link como accesorio opcional en el pie? Decisión de Keiddys.",
            "Dimensión exacta de la etiqueta: Ozwaldo ajusta según cara real del producto.",
        ],
    },
    {
        "product_name": "ProMotor",
        "product_code": "GST-RM",
        "descriptor":   "Supervisor Trifásico de Voltaje para Motores y Bombas",
        "bg_color":     COL_GRAY,
        "gold_border":  False,
        "app_bullets": [
            "Motores industriales de inducción",
            "Bombas centrífugas y sumergibles",
            "Sistemas hidroneumáticos",
        ],
        "char_bullets": [
            "CURVA INVERSA DE VOLTAJE — reacción proporcional a la falla",
            "TD 0,5–3 s AUTOMÁTICO según severidad del voltaje",
            "RECONEXIÓN DESDE 5 s — rearranque rápido de motores",
        ],
        "data_tech": "TD: 0,5–3 s (curva inv. auto)  |  TC: 5–300 s  |  Voltaje: 208/220 V~ (mod. 220) · 440/480 V~ (mod. 440)",
        "models":    "GST-RM220: 208/220 V~     GST-RM440: 440/480 V~",
        "design_notes": [
            "**Dimensiones:** 70 × 90 mm (punto de partida — casing 80 × 100 × 38 mm, igual que GST-RT y GST-RR).",
            "**Color dominante:** Gris oscuro — mismos Pantone de la línea monofásica Exceline Profesional (Ozwaldo los conoce). Texto: blanco. Acento (badge CURVA INVERSA): naranja.",
            "**Tipografía:** Montserrat — tipografía oficial Exceline Profesional.",
            "**Elemento visual prioritario:** Badge 'CURVA INVERSA DE VOLTAJE' — diferenciador absoluto. Badge rectangular naranja con texto blanco, inmediatamente debajo del nombre ProMotor.",
            "**Símbolo de curva inversa:** Línea curva descendente (tiempo en eje Y, desviación de voltaje en eje X) — representación estándar en relés de protección.",
            "**Diales gráficos (2 diales):**",
            "  • Dial 1 — BAJO VOLTAJE (ajustable): rango 165–200 V~, zona naranja en rango sugerido.",
            "  • Dial 2 — RECONEXIÓN TC (ajustable): rango 5–300 s.",
            "  • NO HAY DIAL DE TD — la curva inversa es automática. El TD es un valor mostrado, no un ajuste del usuario.",
            "**Terminales:** Lateral izq.: L1, L2, L3  |  Lateral der.: 95 (COM), 96 (NC), 98 (NA)",
            "**Íconos sugeridos:** Símbolo de curva inversa · Motor eléctrico (M en círculo) · Bomba hidráulica.",
            "**CRÍTICO:** NO incluir íconos de compresor ni refrigeración — ese es el GST-RR (ProFrio, azul). Evitar iconografía que genere confusión en el canal.",
            "**Jerarquía visual (70 × 90 mm):** 1) ProMotor (dominante) · 2) GST-RM + descriptor · 3) Aplicaciones (3 max) · 4) Bullets (3 max — curva inversa primero) · 5) Datos técnicos · 6) Modelos · 7) Logos (pie)",
        ],
        "resolved_items": [
            "Nomenclatura confirmada: GST-RM (no GST-RG). Modelos: GST-RM220 / GST-RM440.",
            "Sin referencias comparativas — copy enfocado en características propias.",
            "Dimensiones casing confirmadas: 80 × 100 × 38 mm → etiqueta 70 × 90 mm.",
            "Colores: mismos Pantone línea monofásica (Ozwaldo los maneja). Fuente: Montserrat.",
        ],
        "pending_items": [
            "¿TD exacto de curva inversa (0,5–3 s) es publicable como especificación oficial? I&D debe confirmar.",
            "¿El sobre voltaje del GST-RM es fijo o ajustable? Impacta número de diales.",
            "¿Hay perilla de TD en la versión con curva inversa? Si no existe, reflejar en diseño.",
        ],
    },
    {
        "product_name": "ProFrio",
        "product_code": "GST-RR",
        "descriptor":   "Supervisor Trifásico de Voltaje para Refrigeración y Aire Acondicionado",
        "bg_color":     COL_BLUE,
        "gold_border":  False,
        "app_bullets": [
            "Compresores de A/A central y sistemas VRF",
            "Cuartos fríos y cámaras frigoríficas",
            "Chillers y equipos industriales de refrigeración",
        ],
        "char_bullets": [
            "PROTECCIÓN DE CICLADO CORTO — ciclo de espera 3 min obligatorio",
            "CURVA INVERSA DE VOLTAJE — reacción proporcional a la falla",
            "VOLTAJE ALTO Y BAJO AJUSTABLES — control independiente por perilla",
        ],
        "data_tech": "TD: 0,5–3 s (curva inv. auto)  |  TC: 180–600 s (mín. 3 min)  |  Voltaje: 208/220 V~ (mod. 220) · 440/480 V~ (mod. 440)",
        "models":    "GST-RR220: 208/220 V~     GST-RR440: 440/480 V~",
        "design_notes": [
            "**Dimensiones:** 70 × 90 mm (punto de partida — casing 80 × 100 × 38 mm). Si 3 diales + doble badge requieren más espacio: ajustar a 70 × 95 mm.",
            "**Color dominante:** Azul — mismos Pantone de la línea monofásica de refrigeración (GSM-R120B/R150B). Crear coherencia visual entre línea monofásica y trifásica de refrigeración. Texto: blanco. Acento: naranja.",
            "**Tipografía:** Montserrat — tipografía oficial Exceline Profesional.",
            "**Elemento visual prioritario:** Badge 'PROTECCIÓN DE CICLADO CORTO' con '3 MIN' en número grande — diferenciador exclusivo de toda la línea GST-R. Primer elemento después de ProFrio. Badge de mayor tamaño que los demás.",
            "**Íconos sugeridos:** Cronómetro/reloj mostrando 3 minutos · Símbolo de curva inversa (posición secundaria) · Compresor / copo de nieve · Split A/A.",
            "**Diales gráficos (3 diales — único producto de la línea con 3 diales):**",
            "  • Dial 1 — BAJO VOLTAJE (ajustable): rango 165–200 V~, zona naranja.",
            "  • Dial 2 — ALTO VOLTAJE (ajustable): rango 230–270 V~ — diferenciador vs. GST-RT y GST-RM. Destacar visualmente.",
            "  • Dial 3 — RECONEXIÓN TC (ajustable): rango 180–600 s. El mínimo de 180 s (3 min) es restricción de HARDWARE — el técnico NO puede bajar de ese valor. Indicar zona prohibida o tope visual antes de 180 s.",
            "**Terminales:** Lateral izq.: L1, L2, L3  |  Lateral der.: 95 (COM), 96 (NC), 98 (NA)",
            "**Jerarquía visual (70 × 90 mm):** 1) ProFrio (dominante) · 2) GST-RR + descriptor · 3) Aplicaciones (3 max) · 4) Bullets (3 max — ciclado corto primero) · 5) Datos técnicos · 6) Modelos · 7) Logos (pie)",
        ],
        "resolved_items": [
            "Sin referencias comparativas — copy enfocado en características propias del GST-RR.",
            "Dimensiones casing confirmadas: 80 × 100 × 38 mm → etiqueta 70 × 90 mm (o 70 × 95 mm si Ozwaldo necesita espacio).",
            "Colores: mismos Pantone línea monofásica de refrigeración (Ozwaldo los maneja).",
            "TC mínimo 180 s (3 min) confirmado como restricción de hardware.",
        ],
        "pending_items": [
            "¿TD exacto de curva inversa (0,5–3 s) es publicable? Mismo gap que GST-RM. I&D debe confirmar.",
            "¿El Pantone azul se unifica con GSM-R120B monofásico o se diferencia para la línea trifásica? Keiddys decide.",
            "¿El sobre voltaje del GST-RR sigue siendo ajustable con la adición de curva inversa? I&D debe validar.",
        ],
    },
]

# ─── Build & save ─────────────────────────────────────────────────────────────

def build_pdf(output_path):
    doc = GSTDoc(output_path)
    story = []

    # Cover
    story += build_cover()

    # Product pages
    for idx, p in enumerate(PRODUCTS):
        is_last = (idx == len(PRODUCTS) - 1)
        story += build_product_page(
            product_name=p["product_name"],
            product_code=p["product_code"],
            descriptor=p["descriptor"],
            bg_color=p["bg_color"],
            gold_border=p["gold_border"],
            copy_lines=[],
            app_bullets=p["app_bullets"],
            char_bullets=p["char_bullets"],
            data_tech=p["data_tech"],
            models=p["models"],
            design_notes=p["design_notes"],
            resolved_items=p["resolved_items"],
            pending_items=p["pending_items"],
            add_page_break=not is_last,
        )

    doc.build(story)
    print(f"PDF generado: {output_path}")

if __name__ == "__main__":
    import shutil
    build_pdf(OUT_WIP)
    # Copy to Owner Inbox
    os.makedirs(os.path.dirname(OUT_INBOX), exist_ok=True)
    shutil.copy2(OUT_WIP, OUT_INBOX)
    print(f"Copiado a Owner Inbox: {OUT_INBOX}")
