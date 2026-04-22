# Plenus-metabólica — Dominio

**Alcance:** Plenus es la marca de productos del Owner (Raoul's Products) dedicada a **alimentos funcionales, salud metabólica y longevidad saludable**. El dominio cubre el diseño, formulación, comunicación y distribución de productos de consumo orientados a resolver problemas metabólicos específicos (resistencia a la insulina, inflamación de bajo grado, disbiosis, sobrepeso metabólico, etc.).

**Distinción con otros dominios del sistema /RAUL/:**

- **Plenus-metabólica ≠ Teca/Teak4Food:** Teak4Food es la marca agro; Plenus es marca de alimentos funcionales con enfoque clínico-metabólico.
- **Plenus-metabólica ≠ Marca personal Raoul:** la marca personal vehicula a Raoul como experto/asesor; Plenus vehicula el producto.
- **Plenus-metabólica ≠ Genteca:** Genteca es protección eléctrica; no hay solapamiento de producto, aunque sí pueden compartirse piezas de content supply chain por vía de `03-cross-cutting/`.

## Marcas implicadas

| Marca / Línea | Segmento | Notas |
|---|---|---|
| **Plenus** (marca paraguas) | Alimentos funcionales y suplementos con enfoque metabólico | _por definir subsegmentación (ej. "Plenus Pro" para canal clínico vs. "Plenus Home" para consumo final)_ |

_(Esta sección se completará a medida que el Owner formalice la arquitectura de marca Plenus. Hoy es stub estructural.)_

## Mercados y audiencias de aplicación

- **Consumidor final** con interés en salud metabólica: adultos 35-65 con síntomas tempranos de disfunción metabólica, interés en longevidad, perfil educado.
- **Profesional de salud** (médicos, nutricionistas, coaches de salud): canal B2B donde Plenus se integra como herramienta dentro de protocolos clínicos.
- **Retail especializado**: tiendas naturistas, farmacias premium, e-commerce de salud.

_(Owner: esta triple segmentación es hipótesis inicial derivada del posicionamiento "alimentos funcionales / metabólica". Ajustar cuando se formalice el GTM de Plenus.)_

## Estructura del dominio

```text
02-plenus-metabolica/
  _index.md              ← este documento
  wiki/                  ← artículos compilados (fundamentos metabólicos, protocolos, patrones) — pendiente de poblar
    _index.md
    market/              ← market intelligence específico Plenus (provisional bajo dominio)
      _index.md
  specs/                 ← fichas de producto, composiciones, claims, etiquetas técnicas
    _index-specs.md      ← stub inicial
  assets/                ← material visual específico Plenus
    _index.md
    products/            ← fotos de producto (packshot, detalle, estilo de vida)
    packaging/           ← mockups de empaque y etiquetas
    infographics/        ← infografías científicas (mecanismo, beneficios, studies)
    uncoded/             ← imágenes sin código — revisión del Owner pendiente
```

## Tipos de proyectos típicos

- **Lanzamiento de producto:** desde formulación a go-to-market. Incluye packaging, claims regulatorios, funnel comercial.
- **Protocolos clínicos:** guías para profesionales de salud que usan producto(s) Plenus dentro de intervenciones metabólicas.
- **Materiales educativos:** artículos, infografías, video para consumidor final y para canal profesional.
- **Funnels comerciales:** email series, landing pages, secuencias de nurturing por condición metabólica.
- **Estudios de caso / testimoniales:** documentación de resultados clínicos reales (con consentimiento), útil para comunicación B2B y B2C.
- **Formación de canal profesional:** webinars, talleres, certificaciones cortas para prescriptores.
- **Compliance y claims:** revisión de afirmaciones de salud, respaldo científico, cumplimiento regulatorio por geografía.

## Equipo humano Plenus

_(Sección stub — pendiente que el Owner formalice quiénes integran el equipo Plenus: formulador científico, médico/nutricionista asesor, responsable de producción, canal B2B, marketing, diseño.)_

| Nombre | Rol | Recibe |
|---|---|---|
| _(pendiente)_ | — | — |

## Agentes del sistema /RAUL/ implicados

- **Transversales (content supply chain):** Aurelio, Nerea, Orfeo, Luma, Vela, Atlas, Bruna, Ivo, Sira — se usan sin cambios para producir contenido Plenus.
- **Globales:** Paxs (research agnóstico), Michelina (HR), Celeste (intake documental), Vivienne (decks ejecutivos).
- **Anchored a Plenus:** _(pendientes de contratar cuando crezca la carga)_. Plausibles: un "Vera-equivalente" en medicina funcional / ciencia metabólica; un "Orlan-equivalente" en market intelligence de suplementos y alimentos funcionales. Hasta entonces, Paxs asume investigación puntual y se escala vía Michelina cuando se justifique contratar.
- **NO aplican:** Vera, Orlan, Oz, Renzo, Solenne, Vael están anchored a Genteca y no operan directamente en Plenus (aunque su patrón de diseño puede clonarse por Michelina).

## Relación con base de conocimiento existente en NotebookLM

Existe una base de conocimiento histórica de Plenus en **NotebookLM** (anterior al sistema /RAUL/). Decisiones de arquitectura:

- **/RAUL/ es la LLM wiki + proyectos activos** para Plenus de aquí en adelante. La wiki Plenus se poblará reescribiendo, consolidando y normalizando los materiales de NotebookLM bajo el enfoque /RAUL/ (artículos compilados en `.md`, vendor-neutral).
- **No se migra automáticamente** desde NotebookLM. Se diseñará una fase específica de sincronización/reinterpretación cuando el Owner dé luz verde — esa fase quedará registrada en `04-system/03-governance/DECISIONS.md`.
- **Puerta abierta:** la estructura de `wiki/` y `specs/` está lista para recibir contenido consolidado desde NotebookLM. Cada pieza importada nacerá como artículo wiki con fuente explícita (ej. "consolidado desde colección X de NotebookLM, 2026-04-22") y seguirá las mismas convenciones de `02-knowledge-base/` que el resto del sistema.
- Mientras la sincronización no ocurra, NotebookLM sigue siendo la fuente histórica; /RAUL/ es la fuente viva de lo que se compile y produzca desde el arranque de Fase 3 Plenus.

## Proyectos activos (snapshot)

Ver `04-system/05-indexes/projects-index.md` como fuente autoritativa cuando exista. Al cierre de Fase 3 Plenus:

- `03-projects/plenus-metabolica/` — carpeta creada, sin proyectos activos aún.

## Notas de versión

- **v1 — 2026-04-22** — alta del dominio Plenus-metabólica siguiendo plantilla conceptual Genteca v1. Stub inicial de equipo humano, marcas y agentes anclados (se completará con la operación real).
