# Contexto del Proyecto — Raul Workspace

> **⚠ COMPANION DOC — LEGACY PRE-MIGRACIÓN (congelado 2026-04-25)**
> Este archivo describe la infraestructura y flujos del sistema **anterior a 2026-04-21** (`C:\WorkspaceIA\...`, estructura WIP/ForReview/Approved, InboxBot viejo).
> **Ya no se auto-carga** en sesiones — el `@CONTEXT.md` fue removido de `CLAUDE.md`.
> Consultar solo como referencia histórica. El contexto activo vive en `CONTEXT_core.md`.

---

## Quién es el dueño

**Raoul Bermudez** (`raoul.bermudez@gmail.com`) es asesor independiente de múltiples proyectos y tiene sus propias empresas. Trabaja desde Caracas, Venezuela. Es el único usuario de este sistema.

## Qué es este workspace

Este es el workspace principal de **Genteca** — empresa fabricante venezolana de dispositivos de protección eléctrica. Es el primer proyecto activo del sistema Raul. En el futuro habrá proyectos separados para otras empresas y áreas (alimentos, ganadería, etc.).

## Genteca — Contexto de negocio

**Website:** www.genteca.com.ve
**Actividad:** Fabricación y distribución de protectores eléctricos para el mercado venezolano y latinoamericano.

**Tres líneas de productos:**
- **Exceline** — Línea residencial/comercial: protectores de voltaje (neveras, A/A, TV, equipos electrónicos), regletas, programadores, fotocontroles, flotadores, bombas
- **Exceline Profesional** — Línea profesional: supervisores monofásicos y trifásicos, temporizadores, fotocontroles industriales, breakers y fusibles
- **Genius** — Línea industrial: relés de protección trifásica (GI+, GII+, GIII+), relés para motores (GOCT, GUCT+), relés para bombas sumergibles (GSPT, GSPT-MV), accesorios de comunicación GIO-Link (MODBUS RTU)

**Mercados de aplicación:** refrigeración comercial, motores industriales y domésticos, bombas hidráulicas, sistemas hidroneumáticos, ascensores, iluminación exterior, CCTV, sistemas VRF.

**Enfoque técnico del owner:** protectores eléctricos para motores, bombas y equipos de refrigeración. Investigación técnica y de mercado, NO diseño. Reportes técnicos, comparativas de productos, análisis de competidores, HMI.

## El equipo Raul

Raul es el orquestador — nunca ejecuta tareas directamente, siempre delega.

### Agentes globales (disponibles en todos los proyectos)
Ubicación: `C:\Users\User\.claude\agents\`

| Agente | Rol |
|--------|-----|
| **Michelina** | Head of HR — contrata nuevos agentes vía Paxs |
| **Paxs** | Senior Researcher — investiga cualquier tema, perfila roles para hiring |

### Agentes de este proyecto
Ubicación: `.claude/agents/`

| Agente | Rol | Especialidad |
|--------|-----|-------------|
| **Vera** | Technical Researcher | Protectores eléctricos, relés, IEC/NEMA, selección de equipos |
| **Orlan** | Market Intelligence Analyst | Competidores, HMI, benchmarking, tendencias de mercado |
| **Solenne** | B2B Content Creator | Posts, LinkedIn, email, copy técnico, scripts |
| **Vael** | Branding & Communication Strategist | Messaging, posicionamiento, tono de marca, campañas |
| **Vivienne** | Presentation Designer | PowerPoint (.pptx), Google Slides, decks ejecutivos |
| **Celeste** | Knowledge Base & Assets Librarian | Intake de documentos, conversión PDF/Word/Excel → Markdown, indexado |
| **Renzo** | Application Engineer | Lectura e interpretación de diagramas eléctricos (unifilares, trifilares), guías para técnicos |

## Infraestructura

### Rutas locales
```
c:\WorkspaceIA\
    Staging\                            ← inputs crudos por proyecto/fecha (espejo en Drive)
        Genteca\2026-04-19\             ← carpeta del día (eliminar si vacía al EOD)
        Finca\  Plenus\  Teak4Food\
    PROJECTS\
        Claude code\                    ← sistema Raul (KB, Assets, agents)
            CLAUDE.md  CONTEXT.md
            .claude/agents/
            02-knowledge-base/02-domains/01-genteca/specs/  Market/
            02-knowledge-base/02-domains/01-genteca/assets/products/ Packaging/ Diagrams/ Uncoded/
            04-system/02-agents/conceptual/_roster.md  task-log.md
            Team inbox/    Owner Inbox/
        Genteca\                        ← proyecto activo
            Work In Progress\           ← papeles de trabajo activos
            For Review\                 ← versiones para aprobación del owner
            Approved\                   ← definitivos aprobados (candidatos a KB)
        Finca\  Plenus\  Teak4Food\     ← misma estructura (WIP/For Review/Approved)
    RAG_SOURCES\                        ← solo docs curados → Celeste → KB
    Team Inbox\  Owner Inbox\           ← InboxBot y sesiones remotas
    TRIGGERS\  TEMP\  _ARCHIVE\
```

### Flujo de documentos
```
Staging/[proyecto]/[fecha]/  →  (Raul triage)  →  Team Inbox/
        ↓ archivos de trabajo                       ↓ resultado
  PROJECTS/[proyecto]/Work In Progress/        Owner Inbox/
        ↓ owner aprueba
  For Review/  →  Approved/
        ↓ owner decide que pasa a KB
  RAG_SOURCES/  →  Celeste  →  Knowledge Base/
```

### Google Drive (sync en `G:\Mi unidad\RAUL\`)
```
Staging/          ← espejo de C:\RAUL\01-inbox\03-raw-sources\ (acceso remoto/celular)
RAG_SOURCES/      ← docs curados listos para Celeste → KB
Team Inbox/       ← mirror del inbox local (acceso remoto)
Owner Inbox/      ← mirror del inbox local (resultados remotos)
Knowledge Base/   ← mirror de la KB local
Assets/           ← mirror de Assets local
```

### GitHub
Repo: `https://github.com/raoulbermudez-jpg/raul-workspace`
Rama: `master`
Los archivos binarios (imágenes, PDFs) NO se versionan — viven en Google Drive.

## Ritmo de trabajo

- **Al iniciar sesión:** Raul escanea ambos Team Inboxes (local + Drive) antes de cualquier otra tarea
- **Cada tarea delegada:** Raul escribe una entrada en `04-system/03-governance/task-log.md`
- **Resultados:** Se entregan a ambos Owner Inboxes (local + Drive)
- **Formato de presentaciones:** Raul siempre pregunta el formato antes de que Vivienne entregue la versión final (PowerPoint .pptx / Google Slides / Markdown)
- **Todas las tareas pasan por Raul** — incluso cuando el owner se dirige a un agente por nombre

## Estado actual (2026-04-20)

### Completado
- Sistema Raul configurado y operativo
- 11 agentes activos (2 globales, 9 de proyecto — incluye Oz, Technical Documentation Editor)
- **KB/Technical cargada: 192 documentos Markdown** (Lote B: 25 + Lote C: 167)
- Tesseract v5.4.0 instalado — OCR disponible
- PyMuPDF (fitz), pdfplumber, pytesseract — stack de procesamiento PDF completo
- Assets estructura creada (pendiente carga de imágenes y diagramas)
- Inboxes operativos (local + Google Drive mirror)
- Git inicializado + repo GitHub conectado
- **InboxBot operativo** — trigger `trig_01RgGGbpCvckUzSwkyGMDNtm`, cada 4h, Drive + Gmail drafts, marcadores DONE_
- **Estructura de trabajo implementada**: `Staging/[proyecto]/[fecha]/` → `WIP/` → `For Review/` → `Approved/` → `RAG_SOURCES/` → KB
- **Primera tarea real de Oz completada**: delta v3 + PDFs anotados (tiro + retiro) GSM-MB/RB/RF empaque — esperando aprobación Keiddys
- **Script PPTX→Markdown validado**: python-pptx extrae texto completo con acentos; listo para uso en Staging
- **Nueva línea GST-R definida y documentada** (2026-04-20):
  - 4 productos: GST-RT (ProTransfer/verde), GST-RD (ProDigital/negro-dorado), GST-RM (ProMotor/gris), GST-RR (ProFrio/azul)
  - Brief técnico Vera v1: comparativa completa, gaps identificados
  - Presentación JD V3 procesada: 16 slides → Markdown en `Staging/Genteca/2026-04-19/`
  - Copy etiquetas Oz v2 + PDF brief (9 páginas) + PPTX editable (10 slides) → listos para Ozwaldo
  - Dimensiones casing confirmadas: **80 × 100 × 38 mm** (todos los modelos GST-R)
  - Etiqueta recomendada: **70 × 90 mm**; fuente: Montserrat

### Pendiente inmediato (próxima sesión)
1. **Keiddys aprueba copy GSM-MB/RB/RF** → mover `Work In Progress/GSM-MB-RB-RF_*` a `For Review/` → luego `Approved/`
2. **Correcciones ortográficas retiro Ozwaldo**: "circuíto" → "circuito" (3 productos), "Proteccion" → "Protección" (GSM-MB)
3. **I&D confirma TD curva inversa GST-RM/RR** (0,5–3 s) — antes de imprimir etiquetas
4. **Ozwaldo recibe brief GST-R**: enviar `Owner Inbox/2026-04-20-gst-r-etiquetas-brief-ozwaldo-v2.pptx`
5. **Phase 2A** — owner sube brand manual + logos + Pantone → Staging → Celeste → KB/Market

### Pendiente futuro
- **Phase 2B**: Vael define messaging framework (requiere Phase 2A completa)
- **Phase 2C**: exploración Canva MCP + posible agente multimedia vía Michelina
- Cargar Assets: imágenes de productos, empaques, diagramas de conexión → `Assets/` subcarpetas
- **Nota PyMuPDF**: ñ y tildes se pierden en anotaciones PDF — revisar fix Unicode antes de próxima tarea Oz
- **Staging preprocessor**: estandarizar conversión PPTX→MD como paso automático (ampliar mandato Celeste o trigger)
- **GST-R gaps pendientes**: sobrevoltaje GST-RT ¿fijo o ajustable?; GIO-Link en GST-RD ¿mención opcional?; Pantone azul GST-RR

### Proyectos futuros planificados
- **Alimentos y Ganadería** — proyecto separado, mismo modelo Raul, equipo especializado via Michelina
- Otras empresas del owner — estructura replicable por proyecto

## Reglas de comportamiento de Raul

1. **Nunca ejecuta tareas directamente** — siempre delega
2. **Todas las tareas pasan por Raul** — incluso si el owner menciona a un agente por nombre
3. **Log obligatorio** — cada delegación genera una entrada en task-log.md
4. **Formato de presentación** — siempre preguntar antes de la entrega final
5. **Hiring on-demand** — si no hay agente para la tarea, llamar a Michelina → Paxs → nuevo agente
6. **Refinamiento continuo** — después de cada tarea real, Michelina puede afinar el AGENT.md del agente involucrado

## Equipo humano de Marca y Comunicaciones (Genteca)

Los agentes colaboran con este equipo — deben conocerlos para dirigir entregables correctamente.

| Nombre | Rol | Recibe |
|--------|-----|--------|
| **Keiddys** | Gerente de Marca y Comunicaciones | Aprobaciones, estrategia, decisiones finales |
| **Valeria** | Experta en lenguaje, comunicación y contenido; edita videos | Textos, scripts, copy para revisión y edición |
| **Oscar** | Experto en audiovisuales, videos y grabaciones; usa IA para generación de imágenes/videos | Material audiovisual, briefs de producción de video |
| **Ozwaldo** | Especialista en diseño gráfico | PDFs anotados con cambios, briefs de diseño, manuales, hojas de especificaciones, empaques, etiquetas |

**Regla para agentes:** Oz dirige sus entregables a Ozwaldo. Solenne y Vael pueden dirigir copy a Valeria. Vivienne entrega decks a Keiddys. Oscar es el puente para producción audiovisual con IA.

## Notas importantes

- El owner habla español e inglés — acepta ambos idiomas
- La empresa fabrica los productos pero no hace diseño técnico — el foco es investigación, documentación y marketing
- Los diagramas de conexión son PNG/JPG/PDF escaneado — Renzo los puede leer con visión nativa
- Las imágenes de productos están mayormente codificadas con el código del producto; las que no tienen código van a `02-knowledge-base/02-domains/01-genteca/assets/uncoded/` para revisión
