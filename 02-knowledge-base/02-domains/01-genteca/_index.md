# Genteca — Dominio

**Alcance:** Genteca es empresa venezolana fabricante y distribuidora de dispositivos de protección eléctrica para el mercado latinoamericano. Es el dominio con mayor actividad del sistema /RAUL/.

**Website:** www.genteca.com.ve

## Marcas implicadas

| Línea | Segmento | Productos típicos |
|---|---|---|
| **Exceline** | Residencial / comercial | Protectores de voltaje (neveras, A/A, TV), regletas, programadores, fotocontroles, flotadores, bombas |
| **Exceline Profesional** | Profesional | Supervisores monofásicos/trifásicos, temporizadores, fotocontroles industriales, breakers, fusibles |
| **Genius** | Industrial | Relés trifásicos (GI+, GII+, GIII+), relés para motores (GOCT, GUCT+), relés para bombas sumergibles (GSPT, GSPT-MV), GIO-Link (MODBUS RTU) |

**Mercados de aplicación:** refrigeración comercial, motores industriales y domésticos, bombas hidráulicas, hidroneumáticos, ascensores, iluminación exterior, CCTV, sistemas VRF.

## Estructura del dominio

```text
01-genteca/
  _index.md              ← este documento
  wiki/                  ← artículos compilados (fundamentos, patrones, lecciones)
    _index.md
    brand/               ← identidad de marca y estrategia digital — poblado 2026-04-30
    market/              ← market intelligence específico de Genteca (provisional bajo dominio)
      _index.md
  specs/                 ← hojas de especificación, catálogos, manuales, datasheets
    _index-specs.md
    <192 documentos .md de producto>
  assets/                ← material visual específico Genteca
    _index.md
    products/            ← fotos de producto (codificadas por código de producto)
    packaging/           ← imágenes de empaque
    diagrams/
      Unifilares/        ← diagramas unifilares (PNG/JPG/PDF)
      Trifilares/        ← diagramas trifilares
    uncoded/             ← imágenes sin código — revisión del Owner pendiente
```

## Tipos de proyectos típicos

- **Etiquetas y empaque:** campañas de actualización visual de línea (ej. GST-R, GSM-MB/RB/RF) — viven en `/RAUL/03-projects/genteca/<proyecto>/`.
- **Briefs técnicos y comparativas:** entregables de Vera (selección de productos, gaps, standards IEC/NEMA).
- **Market intelligence:** benchmarking de competidores (ABB, Eaton, Schneider, Siemens y competidores locales definidos explícitamente por el Owner), tendencias HMI, radar de lanzamientos — entregables de Orlan. Ver también `wiki/market/`.
- **Content B2B:** LinkedIn, blog, email, case studies — entregables de Solenne.
- **Branding y campañas:** messaging, tono, launch kits — entregables de Vael.

## Equipo humano de Marca y Comunicaciones (Genteca)

| Nombre | Rol | Recibe |
|---|---|---|
| **Keiddys** | Gerente de Marca y Comunicaciones | Aprobaciones, estrategia, decisiones finales |
| **Valeria** | Experta en lenguaje y contenido; edita videos | Textos, scripts, copy |
| **Oscar** | Audiovisuales, IA para imágenes/videos | Briefs de producción de video |
| **Ozwaldo** | Diseño gráfico | PDFs anotados, briefs de diseño, manuales, empaques, etiquetas |

## Proyectos activos (snapshot)

Ver `04-system/05-indexes/projects-index.md` como fuente autoritativa. Al cierre de Fase 3:

- `03-projects/genteca/2026-04_GSM-MB-RB-RF_empaque/` — Empaque GSM-MB/RB/RF (pendiente aprobación Keiddys)
- `03-projects/genteca/2026-04_GST-R_etiquetas/` — Etiquetas nueva línea GST-R (pendiente confirmación I&D + brief a Ozwaldo)

## Agentes anclados al dominio

`Vera`, `Orlan`, `Solenne`, `Vael`, `Celeste`, `Renzo`, `Oz`. Sus fichas conceptuales viven en `/RAUL/04-system/02-agents/conceptual/`.
