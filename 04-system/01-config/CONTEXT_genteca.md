# CONTEXT_genteca.md
## Contexto del dominio Genteca

**Versión:** 1.0
**Última actualización:** 2026-04-25
**Cargar junto con:** `CLAUDE_core.md` + `CLAUDE_genteca.md`

---

## Genteca — quién es y qué hace

Genteca es una empresa venezolana fabricante y distribuidora de dispositivos de protección eléctrica. Opera en el mercado latinoamericano con foco en Venezuela. Website: www.genteca.com.ve.

**Mercados de aplicación:** refrigeración comercial, motores industriales y domésticos, bombas hidráulicas e hidroneumáticos, ascensores, iluminación exterior, CCTV, sistemas VRF.

---

## Marcas y líneas de producto

### Exceline — segmento residencial / comercial

Protectores de voltaje para electrodomésticos y equipos del hogar y comercio.

| Familia | Producto típico |
|---------|----------------|
| GSM | Protectores monofásicos: neveras (GSM-N120), A/A consola (GSM-ASBS), aires inverter (GSM-MB/RB/RF) |
| GSM-NP/NG/RE/RB | Versiones con supresor de pico integrado |
| GFR | Fotocontroles (temporizadores de luz exterior) |
| GBH | Flotadores / bombas |
| GTC | Programadores horarios |

### Exceline Profesional — segmento profesional

Supervisores y protecciones para aplicaciones comerciales e industriales ligeras.

| Familia | Producto típico |
|---------|----------------|
| Supervisores monofásicos/trifásicos | Protección de tensión para equipos comerciales |
| Temporizadores industriales | Relés temporizadores |
| Fotocontroles industriales | Control de iluminación exterior profesional |

### Genius — segmento industrial

Relés y protectores para motores, bombas y aplicaciones industriales exigentes.

| Familia | Producto típico |
|---------|----------------|
| GI+, GII+, GIII+ | Relés de protección trifásica (sobrecarga, secuencia de fases) |
| GOCT, GUCT+ | Relés para motores con función de contactor integrado |
| GSPT, GSPT-MV | Relés para bombas sumergibles |
| GST-R | Nueva línea de 4 productos (en desarrollo/lanzamiento activo) |
| GIO-Link | Comunicación MODBUS RTU |
| GOCT2 | Relé trifásico para A/A y refrigeración comercial |

---

## Competidores relevantes

**Internacionales (referencia técnica):** ABB, Eaton, Schneider Electric, Siemens, Lovato.

**Competidores locales:** definidos explícitamente por el Owner (no suponer sin confirmación).

---

## Contexto de proyectos activos (snapshot 2026-05-06)

| Proyecto | Estado | Nota |
|----------|--------|------|
| Empaque GSM-MB / RB / RF / RE | 3 variantes listas para Junta Directiva | Alternativa B refinada con 3 ejes paralelos: V1 "Autoprotección térmica activa*" (sin NTC) — V2 "Escudo Térmico NTC*" (con NTC, post WhatsApp Kike-Canudas) — V3 "beneficio del beneficio" con 3 sub-opciones (V3a "Respaldo térmico ante el breaker*" / V3b "Respaldo térmico ante fallas del termomagnético*" / V3c "Última línea de defensa eléctrica*") propuesta por Jesús María. Memo AU-1 v2.3 + PPTX 23 slides listos. Esperando decisión Junta. Anexo SAPI bautizado IP en presentación |
| Etiquetas GST-R | Propuesta Oz v1 recibida 2026-05-04 | 3 productos visibles (RM/RR/RT) en 3 líneas de diseño. Línea 2 seleccionada Owner. GST-RD pendiente próxima entrega Oz + título "Supervisor Trifásico de Voltaje" + decisiones D1-D5 (color RM, indicadores superiores, badges, diales/datos técnicos, pantone azul). Brief técnico Vera v1 con gap curva inversa pendiente I&D |
| GME estudio de mercado | Activo 2026-05-06 | Nueva línea de producto. Encuesta UI + Van Westendorp pricing + OL-3 análisis de nicho vacío. Ver carpeta `03-projects/genteca/2025-04_GME_estudios-mercado/` |

---

## Vocabulario del sistema Genteca

- **Delta de cambios:** documento que describe solo las diferencias entre versión anterior y nueva de una ficha/empaque. Va a Ozwaldo.
- **Brief técnico:** documento que sintetiza especificaciones de un producto para guiar diseño o validación técnica.
- **Lote (A/B/C):** clasificación de grupos de PDFs procesados por Celeste en la migración KB.
- **RAG_SOURCES → 01-inbox/03-raw-sources/:** la carpeta de staging de documentos crudos antes de procesar a KB.
