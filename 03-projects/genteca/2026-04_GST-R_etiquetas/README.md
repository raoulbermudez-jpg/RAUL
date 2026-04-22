# Proyecto: Etiquetas nueva línea GST-R

**Dominio:** Genteca
**Período:** 2026-04
**Estado:** `03-review-and-release/` — brief Oz v2 (PDF 9 páginas + PPTX 10 slides) listo para enviar a Ozwaldo; 04 bloqueado por pendientes I&D.

## Objetivo

Definir copy, layout e identidad visual de las etiquetas de la nueva línea Exceline Profesional **GST-R**, compuesta por 4 modelos:

| Modelo | Nombre comercial | Color | Aplicación |
|---|---|---|---|
| **GST-RT** | ProTransfer | Verde | Transferencia automática |
| **GST-RD** | ProDigital | Negro-dorado | Supervisor digital multifunción |
| **GST-RM** | ProMotor | Gris | Protector de motor |
| **GST-RR** | ProFrio | Azul | Protector para refrigeración |

**Dimensiones confirmadas:** casing 80 × 100 × 38 mm (todos los modelos) · etiqueta recomendada 70 × 90 mm · fuente **Montserrat**.

## Stakeholders

| Rol | Persona |
|---|---|
| Aprobación final | Keiddys |
| Diseño gráfico | Ozwaldo |
| Brief técnico | Vera (agente) |
| Redacción copy etiqueta | Oz (agente) |
| Confirmación técnica pendiente | I&D |
| Owner del sistema | Raoul |

## Organización

| Carpeta | Qué contiene |
|---|---|
| `00-brief/` | `GST-R_nueva_linea_brief_tecnico_v1.md` — brief técnico Vera v1 (comparativa, gaps). |
| `01-strategy-and-design/` | _(sin contenido — no aplica esta campaña)_ |
| `02-production/` | Copy etiquetas v1 y v2 (Oz) + scripts ad-hoc generadores (`gen_gst_r_pdf_v2.py`, `gen_gst_r_pptx_v2.py`). |
| `03-review-and-release/` | Brief Ozwaldo v2: `GST-R_etiquetas_brief_v2.pdf` (9 páginas) + `GST-R_etiquetas_brief_v2.pptx` (10 slides) listos para envío. |
| `04-published-and-hand-off/` | _(vacío — pendiente confirmaciones técnicas antes de imprimir)_ |

## Pendientes inmediatos

1. **I&D confirma TD curva inversa GST-RM/RR** (0,5–3 s) — requisito antes de imprimir etiquetas.
2. **Envío a Ozwaldo:** el brief v2 está listo (ver `03-review-and-release/`) — ya existe una copia espejo en `01-inbox/02-deliverables-to-owner/` (Fase 4 gestionará limpieza de rutas antiguas).
3. **Gaps pendientes a cerrar:**
   - Sobrevoltaje GST-RT: ¿fijo o ajustable?
   - GIO-Link en GST-RD: ¿mención opcional?
   - Pantone azul definitivo GST-RR.

## Enlaces a KB

- Brief técnico de referencia: `00-brief/GST-R_nueva_linea_brief_tecnico_v1.md` (compilable a `wiki/` cuando el proyecto cierre).
- Specs de línea Exceline Profesional relacionadas: `/RAUL/02-knowledge-base/02-domains/01-genteca/specs/`.

## Decisiones clave

- Scripts ad-hoc (`gen_gst_r_pdf_v2.py`, `gen_gst_r_pptx_v2.py`) se mantienen dentro del proyecto (Fase 3, MIGRATION-PLAN §3.4): son específicos de esta campaña, no reutilizables.
- Presentación JD V3 (16 slides) procesada por Celeste como fuente → vive en `/RAUL/01-inbox/03-raw-sources/genteca/2026-04-19/GST_Exceline_Presentacion_JuntaDirectiva_V3_texto.md`.
