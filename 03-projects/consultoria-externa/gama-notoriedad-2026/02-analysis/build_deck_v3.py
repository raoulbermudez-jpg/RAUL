"""
Build PPTX V3 — Notoriedad Gama 2026 — Deck Principal (Capa Analítica Ampliada)
Renderiza VI-1a outline en 42+4 slides usando _deck_v3_common.render_slide().
"""
import sys
from pathlib import Path
sys.path.insert(0, r'C:\Raul\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis')

from _deck_v3_common import (
    render_portada, render_slide, render_cover_table_slide,
    PLOTS_DIR, new_presentation,
)

sys.stdout.reconfigure(encoding='utf-8')

OUT = Path(r"C:\Raul\03-projects\consultoria-externa\gama-notoriedad-2026\03-deck\V3\2026-05-17_Notoriedad-Gama-2026_V3.pptx")
OUT.parent.mkdir(parents=True, exist_ok=True)

prs = new_presentation('Notoriedad Gama 2026 V3 — Capa Analitica Ampliada')

# ============================================================
# BLOQUE 0 — APERTURA (5 slides)
# ============================================================

render_portada(
    prs, 1,
    'Notoriedad y Preferencia de Marca — Gama 2026',
    'Capa Analítica Ampliada V3 · Metodologia reforzada + Reanálisis RF/SHAP + Síntesis Cualitativa',
    [
        'Fecha: 2026-05-17',
        'Equipo analítico: Cora Urrea + Raoul Bermudez',
        'Versión: V3 — complementa V2 (2026-05-16)',
        'Confidencial / NDA',
    ],
    version_label='V3',
)

render_slide(prs, dict(
    n=2, bloque='Bloque 0',
    title='Este V3 complementa el V2 — no lo reemplaza',
    takeaway='El V3 añade tres capas que el V2 no tenía: rigor metodológico formal, reanálisis estadístico con RF+SHAP, y síntesis cualitativa estructurada con pirámide Minto.',
    bullets=[
        'El deck V2 (2026-05-16, 40 slides) es el análisis principal entregado a Gama. Permanece vigente.',
        ('a) Rigor metodológico ampliado:', 'diseño retroactivo, rationale de cada decisión analítica (Methos ME-1/ME-3).'),
        ('b) Reanálisis estadístico:', 'Random Forest + SHAP + k-means formal que confirman y elevan los drivers del V2 (Cuanti CU-3/CU-4 v2).'),
        ('c) Síntesis cualitativa estructurada:', 'análisis temático + triangulación cuali/cuanti + pirámide Minto (Sinta IN-1..IN-5).'),
        'Las recomendaciones del V2 siguen vigentes. Las del V3 las extienden, matizan y re-priorizan donde la evidencia adicional lo justifica.',
        'Convergencia clave: el V3 confirma los 3 drivers del V2 (atención, limpieza, promociones). El V2 es correcto; el V3 añade el POR QUÉ.',
    ],
    table=dict(
        headers=['Aspecto', 'V2 (2026-05-16)', 'V3 (2026-05-17)'],
        rows=[
            ['Análisis principal', '40 slides + RE + Doc Técnico', 'Capa ampliada (este deck)'],
            ['Modelos drivers', 'Logit', 'Logit + RF + SHAP + Gini'],
            ['Segmentación', 'Banners cruzados', 'K-means formal (k=3)'],
            ['Síntesis cuali', 'Frecuencias', 'Análisis temático + Minto'],
            ['Caveats', 'Por bloque', 'Por claim + gate Bruna'],
        ],
    ),
    caveat='V3 NO reemplaza al V2 — coexisten en Drive de Cora. Ver Slide 42 (cierre) para mapa de convergencia.',
))

render_slide(prs, dict(
    n=3, bloque='Bloque 0',
    title='Cómo leer la evidencia de este estudio',
    takeaway='Los hallazgos son robustos dentro de sus límites; los caveats en pie de slide indican el nivel de certeza — no invalidan el hallazgo, lo calibran.',
    bullets=[
        ('Base total:', 'n=402 entrevistas F2F. Margen de error ±4.89% al 95%.'),
        ('Drivers de preferencia confirmados:', 'atención (OR=5.73) y promociones (OR=3.64) — convergen en 4 métodos independientes (logit, RF, SHAP, razón espontánea). Convergencia = estándar más alto del estudio.'),
        ('Subgrupos pequeños:', 'Pref-Gama n=32, datos publicitarios n=17-50 → caveat "REFERENCIAL". Indicativos, no proyectables.'),
        ('Interpretaciones cualitativas:', '"el estudio sugiere" (hipótesis apoyada) cuando triangulación es parcial; afirmativas cuando triangulación es total.'),
        ('Iconos de significancia:', '(*) p<0.10 tendencia · (**) p<0.05 · (***) p<0.01. IC95 acompaña a todo OR.'),
    ],
    table=dict(
        headers=['Nivel de certeza', 'Criterio'],
        rows=[
            ['Alta', '≥3 métodos convergentes + p<0.05'],
            ['Media-Alta', '2 métodos convergentes o p<0.05 con IC95 amplio'],
            ['Media', 'Hipótesis con evidencia parcial'],
            ['Hipótesis', 'Lógica cruzada sin validación directa — requiere fieldwork'],
        ],
    ),
    caveat='CU-6 v2 §L-001..L-006 (bases bajas por subgrupo). IN-6 §C-007 (ausencia de verbatims literales en sesión Sinta).',
))

render_cover_table_slide(
    prs, 'Ficha técnica del estudio', 'Bloque 0',
    'El estudio cubre shoppers regulares de cadena en Caracas + Altos Mirandinos con n=402 entrevistas F2F.',
    ['Dimensión', 'Especificación'],
    [
        ['Universo', 'Shoppers regulares de supermercados de cadena en Caracas + Altos Mirandinos'],
        ['Muestra', 'n=402 entrevistas face-to-face'],
        ['Margen de error', '±4.89% al 95% de confianza (Wilson)'],
        ['Fechas de campo', '[INSERTAR — placeholder pendiente confirmación Cora]'],
        ['Geografía', 'Baruta (122) · Libertador (80) · Sucre (79) · Chacao (70) · El Hatillo (31) · A. Mirandinos (20)'],
        ['NSE', 'C+/C combinado (104) · D (127) · E (171)'],
        ['Banners', 'Total · NSE · Género · Edad (4 bandas) · Municipio · Marca preferida'],
        ['Modelos V3', 'Logit (Pseudo R²=0.4371, AUC=0.929) · RF (sklearn 1.8.0, AUC CV=0.851) · SHAP (shap 0.51.0) · K-means k=3 (silhouette 0.195) · BGM proxy LCA'],
        ['Modelo principal', 'Logit (supera AUC del RF) — RF/SHAP confirman convergencia'],
        ['Pruebas estadísticas', 'z-test diferencia proporciones · Chi² independencia · IC95 Wilson · k-fold CV'],
    ],
    caveat='CU-6 v2 §L-001 (fecha campo pendiente). CU-6 v2 §L-002 (IC95 amplios con n_pref=32 — siempre reportar OR con IC95).',
    n=4,
)

render_cover_table_slide(
    prs, 'Estructura del deck V3', 'Bloque 0',
    'El V3 está organizado alrededor de la tesis central y sus 4 argumentos MECE.',
    ['Bloque', 'Contenido', 'Slides'],
    [
        ['1', 'Tesis central V3 — por qué Gama está en el terreno equivocado', '6-9'],
        ['2', 'Activo experiencial — convergencia 4 métodos', '10-14'],
        ['3', 'Promociones como anzuelo — la paradoja OR=3.64 vs z=-0.67', '15-18'],
        ['4', 'Dos misiones, dos horizontes — urgencia hoy, mercado grande mañana', '19-22'],
        ['5', 'Tres segmentos — Nucleo Leal, Pragmaticos Convertibles, Mayoría Exigente', '23-27'],
        ['6', 'Voz del consumidor — análisis temático + tensiones latentes', '28-31'],
        ['7', 'Diagnóstico comunicación actual — brecha driver #1 vs mensaje', '32-34'],
        ['8', 'Recomendaciones priorizadas (5 acciones MECE)', '35-39'],
        ['9', 'Roadmap 2026-2027', '40-42'],
        ['A', 'Apéndice metodológico ampliado', 'A1-A4'],
    ],
    n=5,
)

# ============================================================
# BLOQUE 1 — TESIS CENTRAL V3 (4 slides: 6-9)
# ============================================================

render_slide(prs, dict(
    n=6, bloque='Bloque 1 — Tesis V3',
    title='Gama tiene el activo más diferenciador — y lo comunica en el terreno equivocado',
    takeaway='El driver #1 es la atención (OR=5.73, triple convergencia). La comunicación habla de precio — el atributo MENOS predictivo (OR=1.03, SHAP #10).',
    bullets=[
        ('El activo diferenciador:', 'la atención al cliente es el único driver con OR>5 y triple convergencia (logit + SHAP + Gini + razón espontánea).'),
        ('El terreno equivocado:', 'Gama habla de precio ("PRECIOS DE TU LADO") cuando el precio es el atributo menos predictivo de su preferencia.'),
        'La arquitectura de oportunidad tiene 4 dimensiones:',
        '   1. Comunicar la experiencia de atención, no el atributo',
        '   2. Usar las promociones como anzuelo de primera visita, no como promesa de precio bajo',
        '   3. Profundizar la misión de urgencia (donde gana), resolver el gap de surtido para misión grande',
        '   4. Activar el tercio del mercado con menor resistencia al precio (seg_2, n=133, 33%)',
    ],
    table=dict(
        headers=['Atributo', 'OR Logit [IC95]', 'SHAP rank'],
        rows=[
            ['Atención', '5.73 *** [1.6-20.4]', '#1'],
            ['Limpieza/orden', '3.99 * [0.94-16.91]', '#2'],
            ['Promociones', '3.64 ** [1.1-11.8]', '#3'],
            ['Menor precio', '1.03 (n.s.)', '#10'],
        ],
    ),
    caveat='IN-6 §C-001 AJUSTAR — formulación como recomendación estratégica derivada de datos, no como crítica directa a la campaña actual.',
))

render_slide(prs, dict(
    n=7, bloque='Bloque 1 — Tesis V3',
    title='Gama tiene un núcleo fiel pequeño y potente, rodeado por un mercado que aún no la ha experimentado',
    takeaway='El 8% que prefiere Gama tiene un perfil estadísticamente distinguible del 92% restante — su lealtad es resultado de haber experimentado el activo de atención que la mayoría no conoce.',
    bullets=[
        ('Preferencia Total:', 'Gama 8.0% (IC95: 5.7%-11.0%). Solo Paramo (21.1%) se separa estadísticamente.'),
        ('Preferencia C+/C:', 'Gama 13.5% (IC95: 8.2%-21.3%). Empate técnico con Plan Suarez (n.s.) y Paramo (n.s.).'),
        ('TOM C+/C:', '60.6% — Gama es notoria en su segmento natural.'),
        ('Paradoja:', 'conocida pero no elegida. El problema NO es awareness — es conversión.'),
        ('Núcleo leal (seg_3, n=32):', 'NSE más alto (2.16/3), percepción precio más favorable (2.94/5), rapidez en caja 4.81/5, atención 4.69/5.'),
    ],
    caveat='CU-6 v2 §S-001 — los segmentos k-means se presentan con caveat de silhouette moderado (~0.20): perfiles son tendencias centrales, no categorías discretas.',
))

render_slide(prs, dict(
    n=8, bloque='Bloque 1 — Tesis V3',
    title='El 54% percibe Gama como cara — pero el precio NO mueve su preferencia',
    takeaway='El precio opera como barrera de entrada para el 92% que nunca ha experimentado la atención de Gama — no como criterio de elección dentro del 8% que ya la ha experimentado.',
    bullets=[
        ('Percepción precio Total:', '54% neto caro (IC95: 49.1%-58.8%). 45% percibe subida en 6 meses.'),
        ('Entre preferentes Gama:', 'solo 34% neto caro — percepción plana (34% igual, 31% económico).'),
        ('Precio como driver:', 'OR=1.03 (p=0.966), SHAP #10. El atributo con menor peso en los 3 métodos.'),
        ('Interpretación:', 'quienes prefieren Gama han completado la negociación interna de valor (el servicio justifica el precio). El resto tiene la percepción sin haber tenido la experiencia que la re-contextualiza.'),
        ('Implicación:', 'la barrera es perceptual-de-acceso, no estructural de preferencia. Solución: comunicación de experiencia + anzuelo de primera visita, no reducción de precio.'),
        ('⚠ Nota metodológica:', 'el mecanismo de no-conversión es la hipótesis más parsimoniosa dados los datos disponibles. La validación directa requiere investigación con no-consumidores (Van Westendorp, FGIs).'),
    ],
    table=dict(
        headers=['Atributo', 'Importancia (SHAP)'],
        rows=[
            ['Atención', '#1 (0.105)'],
            ['Limpieza', '#2 (0.074)'],
            ['Promociones', '#3 (0.063)'],
            ['…', '…'],
            ['Menor precio', '#10 (0.013)'],
        ],
    ),
    caveat='IN-6 §C-003 AJUSTAR — "barrera de precio es la hipótesis más parsimoniosa. La validación directa requiere investigación con no-consumidores (Van Westendorp, FGIs)." IN-6 §C-007.',
))

render_slide(prs, dict(
    n=9, bloque='Bloque 1 — Tesis V3',
    title='Cuatro argumentos que cubren el qué, cómo, dónde y a quién',
    takeaway='Los cuatro argumentos siguientes son MECE: activo a comunicar (qué), palanca táctica (cómo), territorio de juego (dónde), target prioritario (a quién).',
    bullets=[
        ('Arg. 1 — QUÉ:', 'El activo experiencial (atención + limpieza) es el más diferenciador y el menos comunicado. V3 suma el mecanismo cualitativo.'),
        ('Arg. 2 — CÓMO:', 'Las promociones son anzuelo de primera prueba, no promesa de precio bajo. V3 suma explicación de la paradoja cuali/cuanti y acción específica (stickers + paraguas único).'),
        ('Arg. 3 — DÓNDE:', 'Urgencia hoy (posición defendible #2), mercado grande como horizonte (donde se pierde el 34% de propios preferentes). V3 suma lógica JTBD.'),
        ('Arg. 4 — A QUIÉN:', 'El seg_2 (Pragmaticos Convertibles, n=133, 33%) tiene menor resistencia al precio. Territorio de mayor retorno de corto plazo. NUEVO en V3.'),
    ],
    caveat='Slide de estructura — sin caveat específico.',
))

# ============================================================
# BLOQUE 2 — EL ACTIVO EXPERIENCIAL (5 slides: 10-14)
# ============================================================

render_slide(prs, dict(
    n=10, bloque='Bloque 2 — Activo experiencial',
    title='Driver #1: Atención — triple convergencia de cuatro métodos',
    takeaway='La convergencia logit + SHAP + Gini + razón espontánea es el hallazgo más robusto del estudio.',
    bullets=[
        ('Logit:', 'OR=5.73*** (p=0.007, IC95: 1.6-20.4). Único driver con p<0.01.'),
        ('SHAP RF:', 'mean(|v|)=0.1047 — #1 de 10, margen claro sobre #2 (0.0735).'),
        ('Gini RF:', '0.1977 — #1 de 10.'),
        ('Razón espontánea P21.1:', '~53% de los 32 preferentes citan "buena atención" como razón #1.'),
        ('AUC:', 'logit 0.929 vs RF CV 0.851 → logit es modelo principal.'),
        ('Z-score Gama-Atención:', 'sobre-indexa en el grupo pref-Gama.'),
    ],
    image=str(PLOTS_DIR / 'shap_bar_20260517_v1.png'),
    caveat='CU-6 v2 §D-001 GO pleno. Incluir IC95 [1.6, 20.4]. "OR=5.73 es el estimador puntual; el efecto real está entre 1.6x y 20.4x con 95% de confianza."',
))

render_slide(prs, dict(
    n=11, bloque='Bloque 2 — Activo experiencial',
    title='Driver #2: Limpieza/Orden — elevado de tendencia a driver secundario confirmado',
    takeaway='SHAP y Gini elevan la limpieza/orden a driver secundario confirmado, aunque el logit es borderline — la convergencia es suficiente.',
    bullets=[
        ('Logit:', 'OR=3.99 (p=0.061, tendencia p<0.10; IC95: 0.94-16.91).'),
        ('SHAP RF:', '0.0735 — #2 de 10.'),
        ('Gini RF:', '0.1609 — #2 de 10.'),
        ('Por qué SHAP eleva lo que el logit no alcanza:', 'multicolinealidad entre atención y limpieza. Quien asocia atención también asocia limpieza → el logit penaliza ambos.'),
        ('SHAP no-paramétrico:', 'captura el efecto marginal adicional de limpieza más allá de su correlación con atención.'),
        ('Implicación:', 'la "experiencia de servicio" en Gama es un constructo compuesto — atención + limpieza son el EJE 1 de la propuesta de valor experiencial.'),
    ],
    image=str(PLOTS_DIR / 'shap_beeswarm_20260517_v1.png'),
    caveat='CU-6 v2 §D-002 — GO con caveat p-logit borderline. "La limpieza/orden alcanza significancia formal en RF/SHAP (#2 en ambos) aunque el logit no alcanza p<0.05 (p=0.061), por multicolinealidad con atención."',
))

render_slide(prs, dict(
    n=12, bloque='Bloque 2 — Activo experiencial',
    title='El estudio sugiere que la atención opera como señal de reconocimiento personal — no solo como calidad funcional',
    takeaway='El análisis temático es consistente con la hipótesis de que la atención opera en un registro diferente al precio o surtido — es el momento que cristaliza la preferencia.',
    bullets=[
        ('Análisis temático (Sinta IN-2, Tema 1):', 'los preferentes describen la atención como tipo de experiencia categóricamente distinta a la del supermercado de precio.'),
        ('Evidencia de frecuencias:', '53% de los preferentes cita "buena atención" como razón #1 espontánea. En Páramo: 81% cita "mejores precios". Propuestas de valor categorialmente distintas.'),
        ('Rapidez en caja:', '4.81/5 en el núcleo leal (seg_3) — la más alta de los 3 segmentos. Forma parte del mismo constructo "experiencia de servicio".'),
        ('⚠ El estudio sugiere que', 'la atención puede estar operando como señal de reconocimiento personal (el empleado que resuelve, que acompaña). El análisis temático es CONSISTENTE CON esta hipótesis — no la prueba.'),
        ('⚠ Ausencia de verbatims literales:', 'Sinta no tuvo acceso a la BBDD raw en esta sesión. Los temas se construyen sobre frecuencias de categorías. Confirmación plena requiere FGIs/IDIs en ola futura.'),
        ('Por qué tiene el OR más alto (hipótesis):', 'la atención es el atributo con mayor capacidad de SORPRESA POSITIVA en la categoría supermercado (lógica Kano de atributo diferenciador).'),
    ],
    caveat='IN-6 §C-004 AJUSTAR — "el estudio sugiere que la atención puede estar operando como reconocimiento personal — hipótesis interpretativa apoyada en frecuencias. Confirmación plena requiere verbatims literales." IN-6 §C-007.',
))

render_slide(prs, dict(
    n=13, bloque='Bloque 2 — Activo experiencial',
    title='El DNA de Gama: sobreindexación en los 4 atributos experienciales',
    takeaway='El z-score confirma que su diferenciación está en la experiencia, no en el precio — Tienda atractiva (+1.09), Calidad (+0.97), Seguro (+0.76), Limpieza (+0.72).',
    bullets=[
        ('Ventajas (z>0):', 'Tienda atractiva +1.09, Calidad +0.97, Seguro +0.76, Limpieza +0.72.'),
        ('Brechas (z<0):', 'Menor precio -0.72, Hacer valer dinero -0.67, Promociones -0.67.'),
        ('Interpretación estratégica:', 'Gama gana en experiencia, pierde en precio/valor-dinero — DNA de supermercado premium que debe comunicar experiencia, no precio.'),
        ('Z-score Promociones (-0.67) NO contradice OR=3.64:', 'la paradoja se explica en Bloque 3 (las promociones operan como anzuelo, no como identidad de marca).'),
        ('Páramo:', 'sobreindexa en 7 de 10 atributos incluyendo menor precio. Competir frontalmente en precio = abandonar terreno donde Gama tiene ventaja.'),
    ],
    table=dict(
        headers=['Atributo', 'Z-score Gama'],
        rows=[
            ['Tienda atractiva', '+1.09'],
            ['Calidad', '+0.97'],
            ['Seguro', '+0.76'],
            ['Limpieza', '+0.72'],
            ['Menor precio', '-0.72'],
            ['Valor dinero', '-0.67'],
            ['Promociones', '-0.67'],
        ],
    ),
    caveat='CU-6 v2 §1 — z-score es descriptiva, no inferencial. No confundir z-score de asociación con OR de drivers.',
))

render_slide(prs, dict(
    n=14, bloque='Bloque 2 — Activo experiencial',
    title='El estudio indica que comunicar la experiencia puede tener mayor impacto que comunicar el atributo',
    takeaway='Mostrar el momento concreto de reconocimiento que genera preferencia tiene un potencial de persuasión que el estudio justifica explorar — una revisión de la plataforma de comunicación está respaldada por los datos.',
    bullets=[
        ('Acción derivada del análisis:', 'una campaña construida sobre el registro relacional que el shopper ya proyecta (53% de preferentes citan atención espontáneamente) puede tener mayor tracción.'),
        ('Formato sugerido por el análisis:', 'el momento concreto — el empleado que resuelve, conoce, acompaña. La escena más que el slogan.'),
        ('Lectura de las campañas actuales:', '"PRECIOS DE TU LADO" comunica un resultado (precio) que el 54% del mercado no asocia con Gama; la campaña experiencial trabajaría sobre un proceso (atención) que el 53% de preferentes ya valida.'),
        ('Espacio semántico disponible:', '"compañía / estar para ti" tiene señales tempranas de disponibilidad en la memoria del shopper (30% lectura relacional en DTLS).'),
        ('Relación con V2:', 'Rec. 2 V2 → "capitalizar driver ATENCIÓN". V3 suma el mecanismo (qué mostrar) y la evidencia que justifica la revisión.'),
    ],
    table=dict(
        headers=['Eje semántico actual', 'Eje semántico que el estudio respalda'],
        rows=[
            ['Anuncia precio bajo', 'Muestra el momento de atención'],
            ['Resultado de baja credibilidad (54% percibe caro)', 'Proceso validado por preferentes (53%)'],
            ['Slogan abstracto', 'Escena concreta de tienda'],
            ['Territorio compartido con líderes de precio', 'Territorio propio diferenciado'],
        ],
    ),
    caveat='IN-6 §C-001 AJUSTAR aplicado — formulación como oportunidad estratégica derivada de datos, no como evaluación de la creatividad o inversión actual de Gama.',
))

# ============================================================
# BLOQUE 3 — PROMOCIONES COMO ANZUELO (4 slides: 15-18)
# ============================================================

render_slide(prs, dict(
    n=15, bloque='Bloque 3 — Promociones',
    title='Las promociones son el tercer driver — aunque Gama no sea percibida como la marca de las promociones',
    takeaway='El efecto no se debe a que Gama sea reconocida por sus promociones — quien ha accedido a una llega a la tienda y experimenta lo que genera preferencia.',
    bullets=[
        ('Driver terciario:', 'OR=3.64** (p=0.031, IC95: 1.1-11.8). SHAP #3 (0.0633).'),
        ('Z-score Gama-Promociones:', '-0.67 (NO es percibida como marca de promociones). Solo 9% del total asocia Gama con "promociones atractivas".'),
        ('Paradoja cuali/cuanti (IN-4 §2.1):', 'el cuali no confirma promociones como razón espontánea, pero el cuanti sí mide el efecto. Son consistentes: anzuelo de primera prueba, no razón directa.'),
        ('Mecanismo:', 'promoción → reduce barrera de entrada (percepción de caro) → activa primera visita → experiencia de atención → preferencia.'),
        ('Contraste:', 'precio como driver = OR=1.03 (SHAP #10). Las promociones tienen 3.5x más poder sobre preferencia que el precio genérico.'),
    ],
    table=dict(
        headers=['Métrica', 'Precio', 'Promociones'],
        rows=[
            ['OR Logit', '1.03', '3.64'],
            ['p-value', '0.966', '0.031'],
            ['SHAP rank', '#10', '#3'],
            ['Z-score', '-0.72', '-0.67'],
        ],
    ),
    caveat='CU-6 v2 §D-003 — GO con IC95 [1.1, 11.8]. IN-4 §T-03 — convergencia cuali/cuanti con matiz; certeza media.',
))

render_slide(prs, dict(
    n=16, bloque='Bloque 3 — Promociones',
    title='Tres activos de promoción que se activan bajo paraguas único',
    takeaway='Cashea (activo), club de lealtad (activo), e histórico de stickers (inactivo, alta recordación) son las piezas de una mecánica de conversión.',
    bullets=[
        ('Cashea activo:', 'canal de financiamiento que reduce la barrera de precio percibida para primera visita.'),
        ('Club de lealtad activo:', 'mecanismo de retención post-prueba que convierte primera visita en patrón.'),
        ('Histórico de stickers:', 'inactivo actualmente; recordación alta (formato más recordado espontáneamente entre referentes de Gama).'),
        ('Reactivar con basket-building:', 'categorías sensibles (carne, pollo, básicos) → primera visita + basket ampliado + retención.'),
        ('Mensaje del paraguas:', '"esta semana hay una razón específica para venir" — NO "somos económicos".'),
    ],
    table=dict(
        headers=['Asset', 'Función en funnel'],
        rows=[
            ['Cashea', 'Barrier reduction (entrada)'],
            ['Stickers', 'Primera visita (anzuelo)'],
            ['Club lealtad', 'Retención post-prueba'],
        ],
    ),
    caveat='IN-5 §Argumento 2 — los assets son confirmados por Cora (input directo). La recordación del sticker es información operativa de Gama, no cifra del estudio.',
))

render_slide(prs, dict(
    n=17, bloque='Bloque 3 — Promociones',
    title='"Esta semana hay una razón para venir" vs "somos económicos"',
    takeaway='La comunicación de promoción activa la primera visita que genera la experiencia; la comunicación de precio intenta convencer de algo que el 54% del mercado ya no cree.',
    bullets=[
        ('Comunicar precio:', 'el 54% percibe Gama como cara. La campaña solo conecta con el 15% que ya la percibe económica — el mercado que menos necesita convencer.'),
        ('Comunicar promociones:', 'activa la primera visita en el seg_2 (menor resistencia al precio). No promete ser la más barata — promete una razón concreta para ir.'),
        ('Recall PTL:', '10.7% asistido, 0/17 espontáneo. Interpretación dominante (65%) = precio → exactamente lo que el shopper NO cree sobre Gama.'),
        ('Alternativa estratégica:', 'promoción específica y visible (sticker, Cashea, oferta de categoría) reduce barrera de entrada → efecto observable que el slogan de precio no tiene.'),
        ('Relación con V2:', 'Rec. 1 V2 → "comunicar promociones, no precio". V3 agrega el mecanismo cualitativo + acción más específica.'),
    ],
    caveat='CU-6 v2 §L-004 — datos publicitarios con base baja (n=43 asistido, n=17 espontáneo). Titulo de slide: "BASE REFERENCIAL".',
))

render_slide(prs, dict(
    n=18, bloque='Bloque 3 — Promociones',
    title='Síntesis Bloque 3 — Las promociones son la palanca táctica de conversión',
    takeaway='Ninguna acción de comunicación tiene mayor retorno potencial que reactivar el programa de stickers bajo un paraguas único que comunique "razón para venir" — no precio.',
    bullets=[
        ('Hallazgo 1:', 'Las promociones son driver terciario (OR=3.64) a pesar de que Gama no sea percibida como marca de promociones. El efecto es del mecanismo (anzuelo → experiencia), no de la percepción.'),
        ('Hallazgo 2:', 'Gama ya tiene los 3 assets (Cashea, club, stickers) — la inversión requerida es de integración y comunicación, no de construcción.'),
        ('Acción:', 'reactivar stickers con basket-building (categorías sensibles) + integrar Cashea + club bajo paraguas creativo único + mensaje "razón para venir esta semana".'),
        ('Lo que NO es la acción:', 'reducir precios, comunicar que Gama es económica, competir en el terreno donde Páramo tiene ventaja estructural.'),
    ],
    caveat='IN-5 §Argumento 2 nota final — la integración de assets es recomendación estratégica derivada de datos, no dato del estudio.',
))

# ============================================================
# BLOQUE 4 — DOS MISIONES (4 slides: 19-22)
# ============================================================

render_slide(prs, dict(
    n=19, bloque='Bloque 4 — Dos horizontes',
    title='Gama gana la urgencia (#2 con 12.2%) y pierde el mercado grande (#7 con 7.2%)',
    takeaway='La posición en urgencia es sólida y defendible; la posición en mercado grande es el mayor gap de share of wallet con los propios preferentes.',
    bullets=[
        ('Misión urgencia:', 'Gama #2 (12.2%). Única misión donde es competitiva.'),
        ('Misión mercado grande:', 'Gama #7 (7.2%). Páramo lidera con 21.6%.'),
        ('Misión evento/fiesta:', 'Gama #5 (9.2%).'),
        ('Cobertura física NO correlaciona con preferencia:', 'r=0.164, p=0.651 (no significativo). El formato importa, no solo número de sucursales.'),
        ('Paradoja Baruta:', '6 sucursales Gama, 2.4% preferencia local. El formato Express puede limitar conversión donde Páramo tiene propuesta completa.'),
        ('JTBD (IN-3):', 'Gama es "contratada" para J3 (urgencia) y J4 (evento), no para J1 (mercado grande). Trabajos distintos = formatos y promesas distintos.'),
    ],
    table=dict(
        headers=['Misión', 'Pos. Gama', '% Gama'],
        rows=[
            ['Urgencia', '#2', '12.2%'],
            ['Mercado grande', '#7', '7.2%'],
            ['Evento/fiesta', '#5', '9.2%'],
        ],
    ),
    caveat='CU-6 v2 §L-002 — datos de misiones sin IC95 calculado; distribuciones de P26. Leer como indicativos de posición relativa.',
))

render_slide(prs, dict(
    n=20, bloque='Bloque 4 — Dos horizontes',
    title='El 34% que se va: la mayor pérdida de share of wallet de los propios preferentes',
    takeaway='La pérdida no ocurre por precio (los preferentes Gama tienen percepción más favorable que el mercado) — la hipótesis: el surtido/formato para mercado grande es el cuello de botella.',
    bullets=[
        ('11 de 32 preferentes Gama (34%):', 'realizaron su última compra en otra cadena.'),
        ('Destinos:', 'Páramo (4), CM (3), Forum (2), otros (2).'),
        ('Percepción precio entre preferentes:', '34% neto caro vs 54% mercado total. NO se van por precio.'),
        ('Hipótesis (IN-4 §T-09, certeza media):', 'cuando el trabajo es mercado grande, el Express de Gama puede no ofrecer surtido frescos completo. Solución de formato, no de precio ni de comunicación.'),
        ('Corto plazo:', 'garantizar que la misión urgencia sea tan positiva que genere retorno en otras misiones.'),
        ('Horizonte:', 'proyecto cuali de formatos — ¿por qué El Cafetal (3 sucursales) no convierte?'),
    ],
    caveat='IN-4 §T-09 — certeza BAJA en hipótesis de surtido/formato. El cuanti solo muestra destino (otra cadena), no motivo. Requiere validación cuali.',
))

render_slide(prs, dict(
    n=21, bloque='Bloque 4 — Dos horizontes',
    title='Estrategia de dos horizontes: defender urgencia, diagnosticar mercado grande',
    takeaway='Urgencia es la base táctica que ya funciona; el mercado grande es el horizonte que requiere diagnóstico de formatos antes de invertir.',
    bullets=[
        ('CORTO PLAZO — Urgencia:',),
        '   · Comunicar disponibilidad, conveniencia, rapidez',
        '   · Optimizar experiencia de caja (4.81/5 en seg_3)',
        '   · Garantizar que la visita de urgencia active la atención que genera retorno',
        '   · Defender Chacao-Sucre: concentra el 56% de preferentes Gama',
        ('HORIZONTE — Mercado grande:',),
        '   · Proyecto diagnóstico de formatos: ¿por qué El Cafetal (3 suc.) tiene 4.9% vs 41.5% C+/C en la zona?',
        '   · Hipótesis a verificar: surtido frescos / ticket percibido / footprint vs Plan Suárez/CM',
        '   · Sin diagnóstico, abrir más sucursales puede replicar Baruta (6 suc., 2.4% pref).',
        ('Relación V2:', 'Recs. 3+4 V2 (defender Chacao-Sucre, recuperar mercado grande). V3 añade JTBD + recomendación de diagnóstico antes de inversión.'),
    ],
    caveat='IN-4 §T-09 — hipótesis surtido/formato es de certeza media-baja. Marcar como hipótesis a validar.',
))

render_slide(prs, dict(
    n=22, bloque='Bloque 4 — Dos horizontes',
    title='Síntesis Bloque 4 — Urgencia es la posición, mercado grande es la oportunidad',
    takeaway='Gama tiene un derecho a ganar en urgencia que debe profundizar, y un cuello de botella en mercado grande que requiere diagnóstico antes de inversión.',
    bullets=[
        ('Hallazgo 1:', 'Gama es competitiva en urgencia (#2, 12.2%) — única misión donde supera el pelotón medio.'),
        ('Hallazgo 2:', 'El 34% de propios preferentes se va a Páramo, CM o Forum para mercado grande. Mayor fuga de share of wallet.'),
        ('Hallazgo 3:', 'Cobertura física NO garantiza preferencia (r=0.164, p=0.651). Abrir sucursales sin resolver formato puede replicar Baruta.'),
        ('Acción C/P:', 'profundizar captura de urgencia — rapidez, disponibilidad, experiencia de atención en cada visita.'),
        ('Acción horizonte:', 'proyecto diagnóstico de formatos antes de cualquier decisión de apertura o inversión en mercado grande.'),
    ],
    caveat='IN-4 §T-09 — diagnóstico de formatos es recomendación estratégica, no dato del estudio.',
))

# ============================================================
# BLOQUE 5 — TRES SEGMENTOS (5 slides: 23-27)
# ============================================================

render_slide(prs, dict(
    n=23, bloque='Bloque 5 — Tres segmentos',
    title='K-means revela 3 perfiles distintos — el NSE NO es el criterio que los separa',
    takeaway='Los 3 segmentos están definidos por nivel de exigencia en atributos y resolución de la ecuación de valor — no por NSE; cambia la lógica de segmentación para comunicación.',
    bullets=[
        ('Método:', 'k-means (sklearn 1.8.0, k=3 óptimo, silhouette 0.195 máximo de k=2..6) + BGM proxy LCA (BIC mínimo en k=3). Doble criterio converge.'),
        ('Caveat silhouette:', 'valores absolutos (~0.20) son bajos — esperable con variables Likert de alta homogeneidad. Criterio diagnóstico = máximo relativo.'),
        ('Validez:', '3 segmentos estadísticamente válidos y sustantivamente accionables.'),
        ('NSE NO separa seg_1 de seg_2:', '1.78 vs 1.85 — prácticamente igual. Lo que separa es nivel de exigencia P22 y percepción de precio.'),
        ('Implicación:', 'la comunicación NO debería segmentarse por NSE — debería segmentarse por nivel de resolución de la ecuación de valor.'),
    ],
    image=str(PLOTS_DIR / 'kmeans_elbow_silhouette_20260517_v1.png'),
    caveat='CU-6 v2 §S-001 — OBLIGATORIO: "Los 3 segmentos son estadísticamente válidos (silhouette óptimo, BIC mínimo), aunque silhouette es moderado (~0.20). Perfiles son tendencias centrales. Tamaño seg_3 (n=32) es referencial."',
))

render_slide(prs, dict(
    n=24, bloque='Bloque 5 — Tres segmentos',
    title='Seg_1: Mayoría Exigente No Convencida (n=237, 59%)',
    takeaway='Valoran exactamente lo que Gama ofrece — pero la percepción de precio los mantiene fuera; nunca tuvieron la experiencia que resolvería la ecuación.',
    bullets=[
        ('Tamaño:', 'n=237, 59% del total. NSE promedio 1.78 (predominantemente D/E).'),
        ('Preferencia Gama:', '0.0%.'),
        ('Percepción precio Gama:', '3.66/5 — la más negativa de los 3 segmentos.'),
        ('Exigencia:', 'P22 promedio ~4.7/5 — valoran casi todo como muy importante.'),
        ('Paradoja:', 'valoran atención 4.77/5 y limpieza 4.82/5 — casi tan alto como el núcleo leal — pero 0% preferencia. El problema NO es indiferencia al atributo; es que nunca tuvieron la experiencia.'),
        ('Palanca:', 'requiere reducir percepción de precio. Desafío de largo plazo. Comunicación de experiencia sola NO es suficiente.'),
    ],
    table=dict(
        headers=['Variable', 'Seg_1'],
        rows=[
            ['n', '237 (59%)'],
            ['NSE prom.', '1.78'],
            ['% pref-Gama', '0.0%'],
            ['Precio Gama', '3.66/5'],
            ['Exigencia P22', '~4.7/5'],
        ],
    ),
    caveat='CU-6 v2 §S-001 — seg_1 no es grupo discreto, hay solapamiento con seg_2 en márgenes.',
))

render_slide(prs, dict(
    n=25, bloque='Bloque 5 — Tres segmentos',
    title='Seg_2: Pragmaticos Convertibles (n=133, 33%) — el territorio de mayor retorno C/P',
    takeaway='Menor resistencia al precio (3.44 vs 3.66/5) y expectativas más moderadas — una campaña de primera prueba bien diseñada puede activar la conversión.',
    bullets=[
        ('Tamaño:', 'n=133, 33% del total. NSE similar al seg_1 (1.85 vs 1.78) — NO los separa el NSE.'),
        ('Preferencia Gama:', '0.0%.'),
        ('Percepción precio Gama:', '3.44/5 — menos negativa que seg_1 (diferencia 0.22 puntos).'),
        ('Exigencia:', 'P22 promedio ~4.1-4.3/5 — más moderado que seg_1 (~4.7). Expectativas alcanzables por la propuesta actual.'),
        ('Palanca:', 'menor esfuerzo de conversión. Una promoción de bienvenida (anzuelo → primera visita → experiencia de atención) puede iniciar el patrón.'),
        ('Secuencia recomendada:', 'activación (sticker/Cashea) → experiencia guiada (primera compra con atención activa) → retención (club).'),
    ],
    table=dict(
        headers=['Variable', 'Seg_2'],
        rows=[
            ['n', '133 (33%)'],
            ['NSE prom.', '1.85'],
            ['% pref-Gama', '0.0%'],
            ['Precio Gama', '3.44/5'],
            ['Exigencia P22', '~4.1/5'],
        ],
    ),
    caveat='IN-6 §C-002 — "el análisis sugiere que el seg_2 tiene menor barrera de conversión" (no "prueba"). La diferencia 0.22 es descriptiva del cluster, no z-test head-to-head.',
))

render_slide(prs, dict(
    n=26, bloque='Bloque 5 — Tres segmentos',
    title='Seg_3: Nucleo Leal Gama (n=32, 8%) — perfil que la propuesta experiencial produce',
    takeaway='El núcleo leal no es accidental — tiene NSE más alto, percepción de precio más favorable, y valoración máxima de rapidez en caja y atención.',
    bullets=[
        ('Tamaño:', 'n=32, 8% del total. 100% preferencia Gama (algoritmo los aisló naturalmente).'),
        ('NSE promedio:', '2.16 (mayor tendencia C+/C).'),
        ('Percepción precio Gama:', '2.94/5 — el más favorable de los 3 segmentos.'),
        ('Valores máximos:', 'rapidez en caja 4.81/5, hacer valer dinero 4.72/5, atención 4.69/5. Alineados con drivers logit/SHAP.'),
        ('Estrategia:', 'ya están ganados. Prioridad: profundizar basket (más categorías por visita), aumentar frecuencia, convertirlos en embajadores hacia seg_2.'),
        ('Clave:', 'el núcleo leal NO elige Gama por ser la más barata — la elige porque la ecuación de valor ya está resuelta.'),
    ],
    table=dict(
        headers=['Variable', 'Seg_3'],
        rows=[
            ['n', '32 (8%)'],
            ['NSE prom.', '2.16'],
            ['% pref-Gama', '100%'],
            ['Precio Gama', '2.94/5'],
            ['Atención', '4.69/5'],
            ['Rapidez caja', '4.81/5'],
        ],
    ),
    caveat='CU-6 v2 §S-001 y §L-002 — n=32 REFERENCIAL en subanálisis. IC95 ±17pp. Perfiles del seg_3 descriptivos del cluster, no proyectables al universo.',
))

render_slide(prs, dict(
    n=27, bloque='Bloque 5 — Tres segmentos',
    title='Tres segmentos, tres estrategias — el retorno esperado es mayor donde la barrera es menor',
    takeaway='Seg_2 (33%, menor barrera) = oportunidad inmediata. Seg_3 (8%) = activo a profundizar. Seg_1 (59%) = cambios estructurales más allá de comunicación.',
    bullets=[
        ('Seg_3 — Profundización:', 'basket building, frecuencia, advocacy. Mensaje: "todo lo que necesitas, donde ya confías."'),
        ('Seg_2 — Activación:', 'primera visita incentivada (promoción), experiencia guiada, club de lealtad. Mensaje: "esta semana hay una razón específica para venir."'),
        ('Seg_1 — Horizonte:', 'NO es el foco C/P. Requiere cambios en percepción de precio o propuesta de formato para mercado grande. Horizonte 2027-2028.'),
        ('El V3 NO propone una campaña para los 3 segmentos:', 'propone DOS esfuerzos paralelos — profundización de leales (seg_3) + conversión de pragmaticos (seg_2).'),
    ],
    table=dict(
        headers=['Segmento', 'Estrategia', 'Mensaje'],
        rows=[
            ['Seg_3 (8%)', 'Profundización', 'Donde ya confías'],
            ['Seg_2 (33%)', 'Activación', 'Razón para venir'],
            ['Seg_1 (59%)', 'Horizonte', '— (no C/P)'],
        ],
    ),
    caveat='IN-6 §C-002 y §C-008 — los segmentos son hallazgo nuevo en V3 no presentado en V2. Cora decide cómo comunicarlo a Gama en contexto de entrega previa.',
))

# ============================================================
# BLOQUE 6 — VOZ DEL CONSUMIDOR (4 slides: 28-31)
# ============================================================

render_slide(prs, dict(
    n=28, bloque='Bloque 6 — Voz del consumidor',
    title='Los 5 temas cualitativos — lo que el consumidor dice y lo que los datos revelan',
    takeaway='El consumidor de Gama no solo valora la atención como atributo funcional — la experimenta como la diferencia entre ser un número y ser una persona en la tienda.',
    bullets=[
        ('Tema 1 — Atención como diferenciador simbólico:', '53% razón espontánea, triple convergencia cuanti. Los preferentes describen relación cualitativamente distinta a supermercados de precio.'),
        ('Tema 2 — Precio como zona de tensión no resuelta:', '54% total percibe caro; 34% entre preferentes. La negociación de valor solo ocurre para quien ya experimentó la atención.'),
        ('Tema 3 — Cercanía como primer escalón:', '40.6% de preferentes citan cercanía como razón #2. Cercanía = primer "trabajo" (J3, urgencia) → puerta de entrada al argumento experiencial.'),
        ('Tema 4 — Campaña como oportunidad no aprovechada:', '4.2% recall espontáneo; 0/17 recuerdan PTL. Brecha entre driver #1 y mensaje dominante.'),
        ('Tema 5 — Modelo de dos velocidades:', 'seg_3 ya resolvió la ecuación; seg_1+2 no. La segmentación k-means confirma formalmente lo que el cuali sugería.'),
    ],
    caveat='IN-6 §C-007 — análisis temático basado en frecuencias de categorías, no verbatims literales. Sinta no tuvo acceso a BBDD raw en esta sesión.',
))

render_slide(prs, dict(
    n=29, bloque='Bloque 6 — Voz del consumidor',
    title='Dos modelos mentales — Gama es del modelo ATENCIÓN-DOMINANTE, no PRECIO-DOMINANTE',
    takeaway='Intentar competir con Páramo en precio sería abandonar el único territorio donde Gama tiene una ventaja estadísticamente verificable.',
    bullets=[
        ('Modelo ATENCIÓN-DOMINANTE:', 'Gama (53% atención espontánea), CM (53%), Rio (51%).'),
        ('Modelo PRECIO-DOMINANTE:', 'Páramo (81% precio), Plan Suárez (71%), La Granja (82%), Forum (52%), Plazas (60%).'),
        ('Implicación:', 'el modelo mental define el territorio de comunicación. Cambiar Gama al modelo precio = abandonar OR=5.73 para competir donde Páramo tiene ventaja estructural.'),
        ('Convergencia cuali/cuanti (IN-4 §T-01):', 'los preferentes de Gama y Páramo toman decisiones basadas en sistemas de valor completamente distintos. NO hay cross-appeal natural.'),
        ('Conclusión:', 'Gama debe profundizar su territorio, no extenderse al de Páramo.'),
    ],
    table=dict(
        headers=['Modelo mental', 'Marcas dominantes'],
        rows=[
            ['ATENCIÓN', 'Gama (53%), CM (53%), Rio (51%)'],
            ['PRECIO', 'Páramo (81%), P. Suárez (71%), Forum (52%)'],
        ],
    ),
    caveat='CU-6 v2 §L-002 — OR son estimadores puntuales con IC95 amplios. Claim del "territorio atención" es estratégicamente sólido y estadísticamente robusto.',
))

render_slide(prs, dict(
    n=30, bloque='Bloque 6 — Voz del consumidor',
    title='Lo que el consumidor no dice: los temas latentes',
    takeaway='El estudio identifica 3 tensiones latentes que explican por qué la estrategia de precio no funciona — y por qué la estrategia de experiencia tiene el mayor potencial.',
    bullets=[
        ('Tensión 1:', 'la experiencia que genera preferencia es invisibilizada por la barrera de precio que impide llegar a ella. El 92% no preferente nunca llega a experimentar. La barrera perceptual es anterior al argumento.'),
        ('Tensión 2:', 'la campaña NO amplifica el driver #1. El driver (atención) no está en ningún mensaje actual — y el shopper no recuerda la campaña (4.2% recall). La inversión publicitaria no genera retorno de argumento.'),
        ('Tensión 3:', 'Gama tiene un activo de "compañía" disponible en la memoria del shopper, pero no lo ha apropiado sistemáticamente con sus propias frases y visuales.'),
        ('Nota metodológica:', 'el tema latente de "reconocimiento personal" es hipótesis interpretativa. La confirmación plena requiere verbatims literales o investigación cuali dedicada (FGIs/IDIs).'),
    ],
    caveat='IN-6 §C-004 AJUSTAR — tema latente como hipótesis, no dato verificado. IN-6 §C-005 NO-GO — anécdota "Sin ti no hay nosotros" (n=2 de n=17) NO se usa como evidencia primaria. IN-6 §C-007.',
))

render_slide(prs, dict(
    n=31, bloque='Bloque 6 — Voz del consumidor',
    title='Lo que este estudio no puede responder — y por qué la agenda 2027 lo resuelve',
    takeaway='El estudio diagnostica el "qué" con solidez; la agenda 2027 debe responder el "por qué profundo" y el "cuánto cuesta realmente" con metodologías complementarias.',
    bullets=[
        ('Pregunta 1:', '¿La barrera de precio es real o perceptual? Sin auditoría in-store de precios SKU vs SKU, no se distingue. Si perceptual → comunicación. Si real → acción en surtido/negociación.'),
        ('Pregunta 2:', '¿Qué convirtió a los 32 preferentes en preferentes? Sin IDIs con seg_3, desconocemos el conversion pathway a replicar.'),
        ('Pregunta 3:', '¿Cuál es el punto de quiebre de precio en seg_2? Van Westendorp en 3 categorías KVI (carne/pollo/básicos) lo responde.'),
        ('Pregunta 4:', '¿Por qué El Cafetal no convierte con 3 sucursales? Proyecto cuali de formatos lo responde.'),
        ('Ver agenda completa:', 'Bloque 9 (Roadmap 2027).'),
    ],
    table=dict(
        headers=['Pregunta', 'Método 2027'],
        rows=[
            ['Barrera precio real/perceptual', 'Auditoría in-store + VW'],
            ['Conversion pathway seg_3', '10-12 IDIs con preferentes'],
            ['Punto de quiebre precio seg_2', 'Van Westendorp 3 KVIs'],
            ['Por qué El Cafetal no convierte', 'Cuali de formatos'],
        ],
    ),
    caveat='ME-4 §2 y Reflexiones 2027 §2 — recomendaciones de agenda, no datos del estudio actual.',
))

# ============================================================
# BLOQUE 7 — DIAGNÓSTICO COMUNICACIÓN (3 slides: 32-34)
# ============================================================

render_slide(prs, dict(
    n=32, bloque='Bloque 7 — Diagnóstico comunicación',
    title='BASE REFERENCIAL (n=17 espontáneo / n=43 asistido) — Solo el 4.2% recuerda alguna frase publicitaria de Gama espontáneamente',
    takeaway='El recall de la campaña actual es prácticamente nulo — "PRECIOS DE TU LADO" no aparece en ninguna respuesta espontánea de los 17 que recuerdan algo.',
    bullets=[
        ('P35:', '95.8% NO recuerda ninguna frase publicitaria de Gama.'),
        ('P36 (n=17 que sí recuerdan):', '0/17 mencionan PTL espontáneamente.'),
        '   · 41% "no recuerdo" (recordación parcial)',
        '   · 18% slogans de precio genérico (no de Gama)',
        '   · 12% "Sin ti no hay nosotros" (frase de otra marca — error de atribución)',
        ('P37 (asistido):', '10.7% recuerda PTL con ayuda. BASE REFERENCIAL (n=43).'),
        ('P40 (asistido):', '12.4% recuerda DTLS con ayuda. BASE REFERENCIAL (n=50).'),
        ('Conclusión:', 'la inversión en campaña NO produce retorno de notoriedad de mensaje.'),
    ],
    caveat='CU-6 v2 §L-004 — BASE BAJA explícita (n=17 P36, n=43 P37, n=50 P40). Porcentajes indicativos, no proyectables. IN-6 §C-001 AJUSTAR — "el recall de las campañas actuales es bajo (4.2% espontáneo) y la lectura dominante es precio."',
))

render_slide(prs, dict(
    n=33, bloque='Bloque 7 — Diagnóstico comunicación',
    title='BASE REFERENCIAL (n=43 PTL / n=50 DTLS) — El 65% que recuerda PTL la interpreta como mensaje de precio',
    takeaway='La campaña comunica con efectividad lo que el shopper NO cree sobre Gama (que es económica), en lugar de lo que sí cree y le genera preferencia (atención).',
    bullets=[
        ('P39 interpretación PTL (n=43, BASE REFERENCIAL):', '65% lee "precio bajo/accesible". 7% lee "solidaridad". Resto: otras interpretaciones.'),
        ('P42 interpretación DTLS (n=50, BASE REFERENCIAL):', '36% precio/economía. 30% compañía/siempre/cercanía. 28% otra. Lectura más dividida — "De Tu Lado Siempre" tiene mayor potencial semántico.'),
        ('La paradoja:', 'la campaña transmite su intención (PTL = precio), pero no conecta porque el 54% del mercado NO cree que Gama tenga buen precio.'),
        ('"De Tu Lado Siempre" tiene 30% lectura relacional:', 'territorio semántico más cercano al activo experiencial. Potencial NO desarrollado.'),
    ],
    table=dict(
        headers=['Campaña', '% Precio', '% Relacional'],
        rows=[
            ['PTL', '65%', '7%'],
            ['DTLS', '36%', '30%'],
        ],
    ),
    caveat='CU-6 v2 §L-004 — BASE BAJA explícita. IN-6 §C-001 AJUSTAR — "el estudio indica que alinear el mensaje con drivers reales (experiencia, no precio) puede tener mayor impacto."',
))

render_slide(prs, dict(
    n=34, bloque='Bloque 7 — Diagnóstico comunicación',
    title='El estudio indica una oportunidad de alineación entre drivers de preferencia y eje de comunicación',
    takeaway='El estudio indica que comunicar la experiencia de atención puede tener mayor impacto que comunicar precio. Una revisión de la plataforma de comunicación está justificada por los datos.',
    bullets=[
        ('Driver #1 atención (OR=5.73 [IC95 1.6-20.4], SHAP #1):', 'no presente como eje visible en la comunicación actual identificada por el estudio.'),
        ('Driver #2 limpieza (SHAP #2):', 'no presente como eje visible en la comunicación actual identificada por el estudio.'),
        ('Driver #3 promociones (OR=3.64 [IC95 1.1-11.8], SHAP #3):', 'las campañas de precio son leídas por el 65% como mensaje de precio, no de promociones.'),
        ('Atributo menos importante (precio, SHAP #10):', 'es el eje semántico dominante identificado en la lectura de las campañas actuales.'),
        ('Oportunidad estratégica:', 'realinear la inversión publicitaria hacia los drivers reales (experiencia) puede generar mayor retorno de notoriedad de argumento.'),
        ('⚠ Marco interpretativo:', 'oportunidad derivada de los datos del estudio. No es una evaluación de la calidad creativa ni de la inversión publicitaria existente; es input para futuras decisiones de plataforma.'),
    ],
    table=dict(
        headers=['Driver', 'Rank', 'En campaña?'],
        rows=[
            ['Atención', '#1 (OR=5.73)', 'NO'],
            ['Limpieza', '#2 (SHAP)', 'NO'],
            ['Promociones', '#3 (OR=3.64)', 'Sí, leído como precio'],
            ['Precio', '#10 (SHAP)', 'EJE DOMINANTE'],
        ],
    ),
    caveat='IN-6 §C-001 AJUSTAR — "el estudio indica que comunicar experiencia puede tener mayor impacto que comunicar precio. Una revisión de la plataforma está justificada por los datos."',
))

# ============================================================
# BLOQUE 8 — RECOMENDACIONES (6 slides: 35-39 + 1 mapa)
# ============================================================

render_cover_table_slide(
    prs, 'Las 5 recomendaciones V3 son MECE — extienden y matizan las del V2', 'Bloque 8 — Recomendaciones',
    'Ninguna recomendación V3 contradice al V2 — todas las refuerzan con el mecanismo cualitativo y el reanálisis estadístico adicionales.',
    ['#', 'Recomendación', 'Relación con V2'],
    [
        ['1', 'Comunicar la experiencia de atención — no el atributo, el momento', 'V2 Rec.2 refinada (mecanismo cuali)'],
        ['2', 'Reactivar stickers con paraguas único — anzuelo de primera prueba, no precio', 'V2 Rec.1 refinada (mecánica específica)'],
        ['3', 'Defender urgencia, diagnosticar mercado grande antes de invertir', 'V2 Recs.3+4 integradas (lógica JTBD)'],
        ['4', 'Resolver gap de surtido/formato para el 34% de preferentes que se va', 'V2 integrada (cuali surtido)'],
        ['5', 'Activar campaña de primera prueba para el seg_2 (Pragmaticos)', 'NUEVA en V3 (k-means)'],
    ],
    n=35,
)

render_slide(prs, dict(
    n=36, bloque='Bloque 8 — Recomendaciones',
    title='Rec. 1: Comunicar la experiencia de atención — mostrar el momento, no describir el atributo',
    takeaway='Mostrar el momento concreto de reconocimiento personal que genera preferencia tiene poder de persuasión que describir "buena atención" no tiene.',
    bullets=[
        ('Evidencia:', 'OR=5.73 [IC95 1.6-20.4] (triple convergencia), 53% razón espontánea, SHAP #1. El activo existe — falta comunicarlo.'),
        ('Acción:', 'campaña centrada en el momento de interacción (el empleado que conoce, resuelve, acompaña). NO slogan de precio — escena de tienda.'),
        ('Territorio semántico disponible:', '"De Tu Lado Siempre" tiene 30% de lectura compañía/relación entre quienes la recuerdan. Point de partida creativo más cercano al activo.'),
        ('Plataforma sugerida:', 'construir sobre el registro "estar para ti" — mostrar el momento de atención que hace la tienda diferente.'),
        ('Lo que NO es la acción:', 'anunciar que Gama tiene buena atención. Eso es el atributo. La campaña debe mostrar la experiencia — que el shopper "sienta" la diferencia antes de visitarla.'),
        ('Relación V2:', 'Rec. 2 V2 → "capitalizar driver ATENCIÓN". V3 suma qué mostrar y cómo construir territorio semántico.'),
    ],
    caveat='IN-6 §C-004 AJUSTAR — dimensión de "reconocimiento personal" es hipótesis interpretativa. La dirección estratégica (experiencia > precio) es el claim robusto.',
))

render_slide(prs, dict(
    n=37, bloque='Bloque 8 — Recomendaciones',
    title='Rec. 2: Reactivar stickers — anzuelo, no promesa de precio bajo',
    takeaway='Reactivar stickers con basket-building en categorías sensibles, bajo paraguas creativo único que comunique "esta semana hay una razón para venir", es la acción de mayor retorno C/P.',
    bullets=[
        ('Evidencia:', 'Cashea + club lealtad activos + histórico de stickers con recordación alta (actualmente inactivo).'),
        ('Mecánica propuesta:',),
        '   · Stickers en categorías sensibles: carne, pollo, básicos (donde Páramo domina precio)',
        '   · Cashea: financiamiento como reducción de barrera de entrada para primera visita del seg_2',
        '   · Club lealtad: retención post-prueba — primera visita inicia el patrón',
        ('Paraguas único:', 'todos los activos comunican bajo un "nombre de campaña" único para coherencia y recordación.'),
        ('Mensaje:', '"esta semana hay una razón para venir" — NO "somos económicos".'),
        ('Relación V2:', 'Rec. 1 V2 lo recomendó. V3 lo hace específico: stickers como vehículo + paraguas + basket-building.'),
    ],
    caveat='IN-5 §Argumento 2 — recordación histórica del sticker NO tiene cifra del estudio; información operativa de Gama confirmada por Cora.',
))

render_slide(prs, dict(
    n=38, bloque='Bloque 8 — Recomendaciones',
    title='Recs. 3 y 4: Defender urgencia + diagnosticar mercado grande',
    takeaway='No hay inversión más segura que profundizar urgencia (donde ya gana); no hay inversión más arriesgada que abrir sucursales para mercado grande sin saber por qué El Cafetal no convierte con 3 ya en pie.',
    bullets=[
        ('Rec. 3 — Defender urgencia (C/P):',),
        '   · Comunicar conveniencia + disponibilidad + rapidez en corredor Chacao-Sucre',
        '   · Optimizar experiencia de caja (4.81/5 en seg_3) — momento de la verdad de urgencia',
        '   · Garantizar que la visita de urgencia tenga atención suficiente para generar retorno',
        ('Rec. 4 — Diagnosticar mercado grande (horizonte):',),
        '   · Proyecto cuali de formatos: 10-12 IDIs con preferentes Gama que compraron en otra cadena',
        '   · Pregunta central: ¿por qué El Cafetal (3 sucursales Gama) tiene 4.9% preferencia local?',
        '   · Hipótesis a verificar: ¿surtido frescos insuficiente? ¿ticket percibido? ¿propuesta vs P. Suárez/CM?',
        '   · Sin diagnóstico, abrir sucursales puede replicar paradoja Baruta (6 suc., 2.4% pref).',
    ],
    caveat='IN-4 §T-09 — hipótesis de surtido/formato es certeza media-baja. Marcar como hipótesis.',
))

render_slide(prs, dict(
    n=39, bloque='Bloque 8 — Recomendaciones',
    title='Rec. 5 (NUEVA en V3): Campaña de activación para Pragmaticos Convertibles',
    takeaway='Una campaña específica de primera prueba para el seg_2 — NO el mismo mensaje que para el núcleo leal — puede generar el mayor incremento de preferentes en 6-12 meses.',
    bullets=[
        ('Seg_2:', 'n=133, 33% del total. 0% preferencia Gama actual. Menor resistencia al precio (3.44 vs 3.66/5).'),
        ('Exigencia moderada:', 'P22 ~4.1/5 vs ~4.7/5 del seg_1 → la propuesta actual puede satisfacer sus expectativas.'),
        ('Secuencia de conversión:',),
        '   1. Anzuelo: primera visita incentivada (sticker o Cashea)',
        '   2. Experiencia: atención activa y visible en primera compra',
        '   3. Retención: club de lealtad como seguimiento — convertir primera visita en patrón',
        ('Mensaje para seg_2 ≠ seg_3:', 'el seg_2 no conoce el argumento. Mensaje: "ven a ver qué es diferente esta semana", no "ya sabes que somos lo mejor".'),
        ('NUEVA en V3:', 'no existía en V2. Adición genuina del reanálisis k-means de Cuanti.'),
    ],
    caveat='IN-6 §C-002 — "el análisis sugiere que el seg_2 tiene menor barrera — son prioritario de conversión potencial, no garantía." CU-6 v2 §S-001 — silhouette moderado.',
))

# ============================================================
# BLOQUE 9 — ROADMAP (3 slides: 40-42)
# ============================================================

render_slide(prs, dict(
    n=40, bloque='Bloque 9 — Roadmap',
    title='Q2-Q4 2026: cuatro acciones que no requieren nueva investigación',
    takeaway='Las recs. 1-3 V3 son accionables en Q2-Q3 2026 con los assets que Gama ya tiene; solo la Rec. 5 requiere segmentación operativa adicional.',
    bullets=[
        ('Q2-Q3 2026:',),
        '   · Iniciar revisión plataforma de comunicación: territorio experiencial vs precio (Rec. 1)',
        '   · Reactivar stickers con paraguas único + Cashea + club (Rec. 2)',
        '   · Cruzar resultados QR satisfacción con Notoriedad: ¿el QR captura el driver atención? (V2 Rec. 2)',
        ('Q3-Q4 2026:',),
        '   · Diseñar campaña de primera prueba para seg_2 — activación específica (Rec. 5)',
        '   · Iniciar diagnóstico cuali de formatos: El Cafetal + Baruta (Rec. 4)',
        '   · Auditoría in-store de precios en 5 categorías sensibles (opcional, requiere presupuesto)',
        ('Q4 2026:',),
        '   · Decisión sobre ola 2027: expansión scope (MaxDiff + NPS + Van Westendorp)',
    ],
    caveat='ME-4 §6 — las acciones Q4 2026 sobre ola 2027 dependen de decisión de budget con Gama.',
))

render_slide(prs, dict(
    n=41, bloque='Bloque 9 — Roadmap',
    title='Roadmap metodológico 2027 — 5 mejoras obligatorias de bajo costo, alto impacto',
    takeaway='Las 5 mejoras obligatorias para 2027 (MaxDiff, NPS, switching, CEPs, penetración 12m) son ajustes de diseño, no más inversión de campo.',
    bullets=[
        ('OBLIGATORIO 2027:',),
        '   1. MaxDiff reemplaza P22 Likert — jerarquía real de atributos (ME-4 §2.2)',
        '   2. NPS por marca + switching explícito — 3 preguntas, KPI global salud de marca',
        '   3. CEPs expandidos: 5 misiones → 15-20 ocasiones específicas',
        '   4. Penetración 12 meses + frecuencia + ticket — share of wallet $',
        '   5. Booster Pref-Gama: n=80 real (vs n=32) — IC95 de ±17pp a ±11pp',
        ('OPCIONAL 2027 con inversión incremental:',),
        '   · Van Westendorp en 3 KVIs (carne/pollo/básicos) — ~12 preguntas adicionales',
        '   · DBA battery básica — 4-6 estímulos visuales',
        ('HORIZONTE 2028:',),
        '   · Conjoint/DCM — simulador de trade-offs (USD 10-20K)',
        '   · Pulse tracker trimestral C+/C online',
    ],
    caveat='ME-4 §8 — diseño final ola 2027 depende de confirmación Cora sobre metodología fieldwork 2026 (placeholder en ficha técnica).',
))

render_slide(prs, dict(
    n=42, bloque='Bloque 9 — Cierre',
    title='V2 y V3 convergen en los hallazgos fundamentales — el V3 suma el mecanismo y el target',
    takeaway='El estudio 2026 es internamente consistente: cuatro métodos (logit, RF, SHAP, cuali) apuntan en la misma dirección. Próximo paso: activar la estrategia experiencial con el target correcto.',
    bullets=[
        ('Convergencia V2/V3:',),
        '   · Confirmados: atención = driver #1 (OR=5.73, triple), precio = no driver (SHAP #10), gap masivo (0/17 PTL)',
        '   · Elevados: limpieza sube de "tendencia" a "driver secundario" por SHAP+Gini',
        '   · Nuevos en V3: mecanismo cuali (por qué atención #1), k-means formal (3 perfiles), arg. conversión seg_2',
        ('Próximos pasos:',),
        '   · Gate Bruna sobre claims sensibles antes de circulación externa (IN-6 + CU-6 v2)',
        '   · Reunión Cora + Gama: presentar V3 como capa analítica ampliada',
        '   · Decisión sobre revisión plataforma de comunicación',
        '   · Activación stickers + Cashea bajo paraguas único',
        ('Contactos:', 'Cora Urrea (cora.urrea@gmail.com) · Raoul Bermudez (raoul.bermudez@gmail.com)'),
    ],
    caveat='IN-6 §C-008 — decisión de packaging de los segmentos k-means (cómo presentar a Gama el hallazgo nuevo) es del Owner.',
))

# ============================================================
# APÉNDICE — METODOLOGÍA AMPLIADA (4 slides: A1-A4)
# ============================================================

render_slide(prs, dict(
    n='A1', bloque='Apéndice',
    title='Apéndice: Diseño retroactivo — rationale metodológico de cada decisión',
    takeaway='El análisis de Gama 2026 sigue un protocolo documentable retroactivamente y comparable contra el estado del arte 2026.',
    bullets=[
        ('Métodos ejecutados V2 + V3:',),
        '   · Embudo de marca (TOM → Preferida): protocolo estándar',
        '   · Regresión logística (statsmodels, Pseudo R²=0.44, AUC=0.929): modelo principal',
        '   · Random Forest + SHAP (sklearn 1.8.0, shap 0.51.0, AUC CV=0.851): modelo de convergencia',
        '   · K-means (k=3, silhouette 0.195) + BGM proxy LCA (BIC mínimo k=3): segmentación formal',
        '   · Análisis temático (Braun & Clarke adaptado): síntesis cuali',
        '   · Triangulación cuali/cuanti sistemática: 10 claims cruzados (IN-4)',
        ('Gap vs estado del arte 2026:',),
        '   · MaxDiff: no ejecutado (P22 Likert saturado)',
        '   · NPS + switching matrix: ausentes',
        '   · CEPs completos: 5 misiones genéricas vs 15-20 CEPs',
        '   · Van Westendorp: ausente (solo perceptual ordinal P33)',
    ],
    caveat='ME-3 §1 (rationale completo). ME-4 §3 Alerta 3 (HARKing) — algunos análisis Fase C fueron post-hoc; cautela apropiada.',
))

render_slide(prs, dict(
    n='A2', bloque='Apéndice',
    title='Apéndice: Convergencia metodológica — los 10 atributos rankeados por 3 métodos',
    takeaway='La convergencia triple en el top-3 (atención #1, limpieza #2, promociones #3) es el hallazgo metodológico más robusto.',
    bullets=[
        'Convergencia "TRIPLE" = ranking coincidente en logit + SHAP + Gini',
        'Convergencia "DOBLE+" = 2 métodos + matiz en el tercero',
        'AUC logit (0.929 in-sample) supera RF (0.851 CV) → logit es modelo principal correcto',
    ],
    table=dict(
        headers=['Atributo', 'OR [IC95]', 'SHAP', 'Gini', 'Conv.'],
        rows=[
            ['mejor_atienden', '5.73*** [1.6-20.4]', '#1 (0.105)', '#1 (0.20)', 'TRIPLE'],
            ['limpio_ordenado', '3.99* [0.94-16.91]', '#2 (0.074)', '#2 (0.16)', 'DOBLE+'],
            ['promociones', '3.64** [1.1-11.8]', '#3 (0.063)', '#4 (0.10)', 'TRIPLE'],
            ['menor_precio', '1.03 (n.s.)', '#10 (0.013)', '#10 (0.03)', 'TRIPLE (en irrel.)'],
        ],
    ),
    caveat='CU-6 v2 §L-002 — IC95 amplios (n_pref=32). CU-3 v2 §6 — SHAP interpreta el RF; coincidencia con logit = confirmación cruzada.',
))

render_slide(prs, dict(
    n='A3', bloque='Apéndice',
    title='Apéndice: Criterios de validación de los 3 segmentos k-means',
    takeaway='Los 3 segmentos superan los 2 criterios (silhouette máximo + BIC mínimo en k=3) y tienen interpretación sustantiva clara.',
    bullets=[
        ('Criterio 1:', 'Silhouette k=3 = 0.195 (máximo de k=2..6). Valores bajos esperables con Likert de alta homogeneidad.'),
        ('Criterio 2:', 'BIC proxy LCA k=3 = 10,379 (mínimo de k=2..6). Ambos criterios convergen.'),
        ('Criterio 3:', 'Interpretabilidad sustantiva — 3 perfiles con descripción clara y accionable. El algoritmo aisló a los 32 preferentes Gama como cluster independiente.'),
        ('Comparativa Ward (v1) vs k-means (v2):', 'los 5 segmentos hipotéticos del Ward colapsan en 3. Cambio clave: los leales Páramo NO forman cluster propio — están mezclados en seg_1.'),
    ],
    image=str(PLOTS_DIR / 'kmeans_elbow_silhouette_20260517_v1.png'),
    caveat='CU-6 v2 §S-001 — caveat OBLIGATORIO de silhouette moderado + solapamiento en márgenes. Referencia: CU-4 v2 §5.',
))

render_slide(prs, dict(
    n='A4', bloque='Apéndice',
    title='Apéndice: Mapa de convergencia V2 vs V3 — qué confirma, qué eleva, qué es nuevo',
    takeaway='El V3 NO contradice el V2 en ningún hallazgo fundamental — confirma y eleva drivers, suma mecanismo cuali y target de conversión.',
    bullets=[
        ('CONFIRMADOS por V3:', '3 drivers V2 (atención OR=5.73, limpieza OR=3.99/SHAP#2, promociones OR=3.64). Cambio más importante: limpieza sube de "borderline" a "driver secundario confirmado".'),
        ('REFINADOS por V3:',),
        '   · Rec. 1 V2 (comunicar promociones) → especificada como "anzuelo de primera prueba" con stickers+Cashea+club',
        '   · Rec. 2 V2 (capitalizar atención) → suma mecanismo cuali (qué mostrar) y evidencia gap actual',
        ('INTEGRADOS por V3:', 'Recs. 3+4 V2 (defender Chacao-Sucre + recuperar mercado grande) → estrategia dos horizontes con JTBD.'),
        ('NUEVOS en V3:', 'Argumento 4 (seg_2 = oportunidad de conversión inmediata). Segmentación k-means formal. Análisis temático + triangulación sistemática.'),
    ],
    caveat='IN-6 §C-008 — los segmentos k-means son información nueva para Cora/Gama. Decisión de packaging es del Owner.',
))

# ============================================================
# SAVE
# ============================================================

prs.save(str(OUT))
print(f'OK · saved {OUT.name} · {len(prs.slides)} slides · {OUT.stat().st_size:,} bytes')
