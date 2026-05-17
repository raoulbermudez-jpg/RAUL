"""
Build PPTX V3 — Notoriedad Gama 2026 — Resumen Ejecutivo (7 slides)
Renderiza VI-1b outline.
"""
import sys
from pathlib import Path
sys.path.insert(0, r'C:\Raul\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis')

from _deck_v3_common import (
    render_portada, render_slide, render_cover_table_slide,
    PLOTS_DIR, new_presentation,
)

sys.stdout.reconfigure(encoding='utf-8')

OUT = Path(r"C:\Raul\03-projects\consultoria-externa\gama-notoriedad-2026\03-deck\V3\2026-05-17_Notoriedad-Gama-2026_Resumen-Ejecutivo-V3.pptx")
OUT.parent.mkdir(parents=True, exist_ok=True)

prs = new_presentation('Notoriedad Gama 2026 V3 — Resumen Ejecutivo')

# ============================================================
# RE-1 — Portada
# ============================================================
render_portada(
    prs, 1,
    'Notoriedad y Preferencia de Marca — Gama 2026',
    'Resumen Ejecutivo V3 · Capa Analítica Ampliada',
    [
        'Fecha: 2026-05-17',
        'Equipo analítico: Cora Urrea + Raoul Bermudez',
        'Versión: V3 Resumen Ejecutivo — complementa RE del V2',
        'Confidencial / NDA',
        'Acompaña al Deck Principal V3 (46 slides).',
    ],
    version_label='V3 · RE',
)

# ============================================================
# RE-2 — Tesis Central
# ============================================================
render_slide(prs, dict(
    n=2, bloque='Resumen Ejecutivo',
    title='V3 en una oración — y qué lo diferencia del V2',
    takeaway='Gama tiene el activo más diferenciador y lo comunica en el terreno equivocado; el V3 confirma el V2 y suma mecanismo, segmentación y target de conversión.',
    bullets=[
        ('Tesis central V3:', '"Gama posee el activo experiencial más diferenciador del mercado: la atención al cliente es el único driver estadísticamente significativo con OR=5.73 y triple convergencia (logit + SHAP + Gini + razón espontánea). Pero Gama lo comunica en el terreno equivocado: habla de precio cuando el precio es el atributo menos predictivo (OR=1.03, SHAP #10). La estrategia correcta es apropiarse del terreno de la experiencia, usar las promociones como anzuelo de primera visita, y resolver el gap de surtido/formato que le hace perder el 34% de sus propios preferentes en mercado grande."'),
        ('Relación V2 — Confirmado:', 'los 3 drivers V2 (atención, limpieza, promociones) son correctos. La narrativa "Gama va abajo" no tiene base estadística.'),
        ('Relación V2 — Elevado:', 'limpieza sube de "tendencia" a "driver secundario" por SHAP+Gini. El mecanismo cuali explica el POR QUÉ de cada driver.'),
        ('Relación V2 — Nuevo:', 'k-means formal identifica 3 segmentos (8% nucleo leal, 33% convertibles, 59% exigentes). El seg de Pragmaticos Convertibles (33%) es oportunidad nueva sin precedente en V2.'),
    ],
    caveat='IN-6 §C-001 AJUSTAR — tono estratégico, no crítica de campaña. CU-6 v2 §L-002 — OR=5.73 siempre con IC95 [1.6, 20.4] en presentación oral.',
))

# ============================================================
# RE-3 — Los 4 Argumentos MECE
# ============================================================
render_slide(prs, dict(
    n=3, bloque='Resumen Ejecutivo',
    title='Cuatro argumentos que justifican la tesis — cada uno con evidencia cuanti+cuali',
    takeaway='La convergencia de cuatro métodos independientes sobre el mismo ranking de drivers es el mayor respaldo de solidez que un estudio de este tipo puede ofrecer.',
    bullets=[
        ('Arg. 1 — Activo que Gama tiene y no comunica:', 'Atención OR=5.73*** [IC95: 1.6-20.4], SHAP #1, 53% razón espontánea. Limpieza OR=3.99* [IC95: 0.94-16.91], SHAP #2 (logit borderline p=0.061). El estudio sugiere que la atención opera como señal de reconocimiento personal — hipótesis interpretativa.'),
        ('Arg. 2 — Palanca táctica (promociones como anzuelo):', 'Promociones OR=3.64** (IC95: 1.1-11.8), SHAP #3. Precio OR=1.03 (n.s.), SHAP #10. El efecto es del mecanismo anzuelo → primera visita → atención → preferencia. Assets: stickers + Cashea + club.'),
        ('Arg. 3 — Territorio (urgencia hoy, mercado grande mañana):', 'Gama #2 en urgencia (12.2%), #7 en mercado grande (7.2%). 34% de propios preferentes se va a Páramo/CM/Forum. Cobertura física NO correlaciona con preferencia.'),
        ('Arg. 4 — Target (tercio convertible, NUEVO EN V3):', 'K-means k=3. Seg_2 Pragmaticos Convertibles n=133 (33%) tiene menor resistencia al precio (3.44 vs 3.66/5) + expectativas moderadas + 0% pref-Gama actual = mayor retorno C/P.'),
    ],
    caveat='CU-6 v2 §S-001 — silhouette moderado (~0.20), solapamiento en márgenes. IN-6 §C-004 AJUSTAR — mecanismo cuali = hipótesis. IN-4 §T-09 — hipótesis surtido/formato es certeza media-baja.',
))

# ============================================================
# RE-4 — Top 3 Recomendaciones
# ============================================================
render_slide(prs, dict(
    n=4, bloque='Resumen Ejecutivo',
    title='Las 3 acciones de mayor retorno — accionables Q2-Q3 2026 con assets que Gama ya tiene',
    takeaway='Ninguna requiere nueva investigación ni inversión de capital significativa — requieren redirección de plataforma de comunicación y reactivación de activos existentes.',
    bullets=[
        ('Rec. TOP 1 — Comunicar experiencia, no precio:',),
        '   · Qué: revisar plataforma hacia registro experiencial (momento de reconocimiento personal)',
        '   · Cómo: escena de tienda donde el empleado resuelve — no slogan de precio',
        '   · Por qué: driver #1 (atención OR=5.73) no está en campaña; driver #10 (precio) es eje dominante',
        '   · Relación V2: Rec. 2 V2 + mecanismo cuali V3',
        ('Rec. TOP 2 — Reactivar stickers como anzuelo de primera prueba:',),
        '   · Qué: stickers basket-building (carne/pollo/básicos) + Cashea + club bajo paraguas único',
        '   · Mensaje: "esta semana hay una razón para venir" — no "somos económicos"',
        '   · Por qué: promoción convierte primera visita en experiencia de atención (OR=3.64)',
        '   · Relación V2: Rec. 1 V2 + especificación de mecánica V3',
        ('Rec. TOP 3 — Campaña específica para Pragmaticos Convertibles (NUEVA V3):',),
        '   · Qué: anzuelo (sticker/Cashea) → experiencia guiada → retención (club)',
        '   · A quién: seg_2, n=133, 33% del mercado — menor barrera + expectativas alcanzables',
        '   · NUEVA en V3 — no existía en V2',
    ],
    caveat='IN-6 §C-001 AJUSTAR — Rec. 1 como "oportunidad estratégica" derivada de datos, no crítica. IN-6 §C-002 — Rec. 3 como "el análisis sugiere menor barrera", no garantía.',
))

# ============================================================
# RE-5 — Roadmap
# ============================================================
render_cover_table_slide(
    prs, 'Q2 2026 a H1 2027 — acciones, diagnósticos y upgrade metodológico', 'Resumen Ejecutivo',
    'Acciones de comunicación/táctica son para hoy; diagnóstico de formatos para Q3-Q4 2026; upgrade ola 2027 es la inversión de mayor retorno sobre el tracker.',
    ['Horizonte', 'Acción', 'Tipo'],
    [
        ['Q2-Q3 2026', 'Revisión plataforma comunicación → registro experiencial (Rec. 1)', 'Comunicación'],
        ['Q2-Q3 2026', 'Reactivar stickers + Cashea + club bajo paraguas único (Rec. 2)', 'Táctica'],
        ['Q2-Q3 2026', 'Diseñar activación seg_2 — primera prueba incentivada (Rec. 3)', 'Táctica'],
        ['Q2-Q3 2026', 'Cruzar QR satisfacción con drivers Notoriedad', 'Investigación'],
        ['Q3-Q4 2026', 'Proyecto cuali formatos — 10-12 IDIs (Rec. 4)', 'Investigación'],
        ['Q3-Q4 2026', 'Auditoría in-store precios 5 categorías (opcional)', 'Investigación'],
        ['Q1 2027', 'Ola 2027: MaxDiff + NPS + switching + CEPs expandidos + n=80 Pref-Gama', 'Metodología'],
        ['Q2 2027 opcional', 'Van Westendorp 3 KVIs + DBA battery básica', 'Metodología'],
    ],
    caveat='ME-4 §8 — diseño ola 2027 depende de confirmación Cora sobre metodología fieldwork 2026. ME-4 §6 — Conjoint/DCM como horizonte 2028 (USD 10-20K).',
    n=5,
)

# ============================================================
# RE-6 — Límites + cómo leer V2+V3
# ============================================================
render_slide(prs, dict(
    n=6, bloque='Resumen Ejecutivo',
    title='Lo que el estudio puede afirmar y lo que requiere validación — el V3 es una capa, no una conclusión cerrada',
    takeaway='Conclusiones de alta certeza (drivers, modelo mental, gap comunicacional) están confirmadas por convergencia múltiple; conclusiones de certeza media requieren investigación dedicada.',
    bullets=[
        ('CLAIMS DE ALTA CERTEZA (GO pleno):',),
        '   · Atención = driver #1 (OR=5.73, SHAP #1, Gini #1, 53% razón espontánea)',
        '   · Precio = no driver (OR=1.03, SHAP #10, Gini #10)',
        '   · 3 segmentos k-means (silhouette óptimo + BIC mínimo)',
        '   · Gap comunicacional (0/17 recall espontáneo PTL; 65% lo interpreta como precio)',
        ('CLAIMS CON CAVEAT (GO con calificación):',),
        '   · Limpieza = driver secundario (SHAP #2 pero logit p=0.061)',
        '   · Seg_2 = convertibles (diferencia 0.22 descriptiva, no z-test)',
        '   · Barrera de precio es hipótesis más parsimoniosa — no verificada directamente',
        ('NO se puede afirmar con estos datos:',),
        '   · "Gama tiene X% de share de mercado" → "8% de preferencia en muestra cuotada"',
        '   · "La atención CAUSA preferencia" → "atención = atributo más fuertemente asociado"',
        '   · "Segmentos son grupos discretos" → "perfiles con solapamiento (silhouette ~0.20)"',
        '   · "Gama debe cambiar de campaña" → "el estudio justifica revisar la plataforma"',
        ('Cómo leer V2 + V3 juntos:', 'V2 es la entrega principal (análisis completo). V3 es capa analítica ampliada (hallazgos estratégicos + rigor). NO hay contradicciones entre V2 y V3.'),
    ],
    caveat='IN-6 §C-007 — análisis cuali Sinta basado en frecuencias de categorías, no verbatims literales. Temas latentes = hipótesis interpretativas; confirmación plena requiere FGIs/IDIs.',
))

# ============================================================
# RE-7 — Cierre
# ============================================================
render_slide(prs, dict(
    n=7, bloque='Resumen Ejecutivo',
    title='Próximos pasos para Cora y Gama — el V3 abre tres conversaciones',
    takeaway='El V3 justifica tres conversaciones con Gama: revisar plataforma de comunicación, activar stickers con paraguas único, y explorar proyecto de formatos antes de invertir en mercado grande.',
    bullets=[
        ('Conversación 1 — Plataforma de comunicación (estratégica):',),
        '   · El estudio justifica revisar el eje semántico hacia "experiencia de atención"',
        '   · Próximo paso: reunión con equipo de comunicación/agencia de Gama',
        ('Conversación 2 — Activación táctica (inmediata):',),
        '   · Reactivar stickers + Cashea + club bajo paraguas único. Basket-building en categorías sensibles.',
        '   · Próximo paso: validar assets disponibles (sticker artwork, acuerdos Cashea, mecánica de club)',
        ('Conversación 3 — Formatos y mercado grande (con diagnóstico previo):',),
        '   · Antes de invertir en apertura o ampliar surtido, diagnosticar por qué El Cafetal no convierte',
        '   · Próximo paso: scoping del proyecto cuali (10-12 IDIs, presupuesto a confirmar)',
        ('Gate pendiente:', 'Bruna debe revisar claims sensibles (IN-6 + CU-6 v2) antes de circulación externa. Owner decide timing de presentación a Gama.'),
    ],
    caveat='IN-6 §C-008 — Owner decide cómo presentar los segmentos k-means a Gama (información nueva no presente en V2).',
))

# ============================================================
# SAVE
# ============================================================
prs.save(str(OUT))
print(f'OK · saved {OUT.name} · {len(prs.slides)} slides · {OUT.stat().st_size:,} bytes')
