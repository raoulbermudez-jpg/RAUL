# Plan: Mejora de Agentes y Flujos de Trabajo Genteca
**Creado:** 2026-04-29  
**Estado:** EN ESPERA — retomar próxima sesión  
**Contexto base:** Análisis completo Ene-Abr 2026 (Gmail + Calendar + One Pager)

---

## Qué ya está hecho

- ✅ `One pager enero - Abril 2026_V01.pptx` actualizado (slides 3, 5, 6, 7, 8, 9 con datos de abril)
- ✅ Directorio de contactos Genteca guardado en memoria (`reference_genteca_contacts.md`) — 26 personas con emails y roles
- ✅ 6 hipótesis de mejora de flujos guardadas en memoria (`project_genteca_workflow_hypotheses.md`)

---

## Hipótesis validadas (resumen ejecutivo)

| # | Hipótesis | Prioridad | Agente(s) a mejorar |
|---|---|---|---|
| H1 | One Pager mensual: 100% automatizable (ya validado en sesión) | ALTA | InboxBot + Vivienne + Sira |
| H2 | Briefs para Oz: falta plantilla estructurada por tipo de asset | ALTA | Oz + Atlas |
| H3 | Videos ML: compuerta de aprobación pre-producción | MEDIA | Nerea |
| H4 | BBDD Cora: latencia 4-6 días evitable con trigger InboxBot | MEDIA | InboxBot |
| H5 | Reuniones recurrentes: sin pre-brief estructurado | BAJA-MEDIA | InboxBot + Sira |
| H6 | Encuestas simultáneas: riesgo de fatiga en BBDD técnicos | BAJA | Aurelio |

---

## Opciones de próximas acciones (decidir al retomar)

### Opción A — Programar One Pager mensual automático
- Usar `/schedule` para crear rutina que se ejecute el día 25 de cada mes
- El agente buscará emails Genteca del mes, extraerá reuniones del Calendar, actualizará el PPTX base
- Raoul solo revisa 30 minutos en lugar de 3-4 horas
- **Prerequisito:** Tener el PPTX base de `One pager enero - Abril 2026_V01.pptx` como template

### Opción B — Plantillas de brief para Oz (impacto inmediato en GST julio 2026)
- Crear plantillas estructuradas en el agent file de Oz para cada tipo de asset:
  - `brief_etiqueta_frontal.md` — campos: dimensiones, colores Pantone, jerarquía badges, diferenciadores
  - `brief_etiqueta_lateral.md` — campos: voltajes, especificaciones técnicas, normativas
  - `brief_HDE.md` — campos: modelo, especificaciones, tabla de características, notas técnicas
  - `brief_guia_rapida.md` — campos: pasos, imágenes requeridas, QR destino
- Añadir checklist de entrega (qué Raoul debe proveer antes de que Oz pueda empezar)
- **Impacto directo:** reduce rondas de corrección GST de 4+ emails a 1-2

### Opción C — Enriquecer Vael con contexto de marca Exceline
- Añadir a Vael:
  - Líneas de producto actuales: GST-R (trifásico), GSM (monofásico), GCT (controladores), GME (app)
  - Audiencias: técnicos de refrigeración, instaladores, supervisores de voltaje
  - Tono de marca: técnico pero accesible, diferenciador NTC ("Protección Térmica")
  - Decisores clave: Kike (estrategia) → Keiddys (aprobación materiales)
- Esto garantiza que todos los agentes de contenido (Nerea, Atlas, Luma, Solenne) hablen el mismo lenguaje de marca

---

## Contexto técnico disponible en memoria

Al iniciar la próxima sesión, estos archivos estarán disponibles:

```
memory/reference_genteca_contacts.md       — 26 contactos con emails y roles
memory/project_genteca_workflow_hypotheses.md — 6 hipótesis detalladas
memory/feedback_genteca_brief_style.md     — 7 reglas de comunicación externa Genteca
memory/project_gst_labels_july_deadline.md — Estado etiquetas GST (deadline julio 2026)
memory/reference_gst_contacts_files.md     — Rutas de archivos y contactos de diseño
```

---

## Archivos clave del proyecto

```
C:\RAUL\01-inbox\01-owner-to-raul\One pager enero - Abril 2026_V01.pptx  — One Pager actualizado
C:\RAUL\01-inbox\03-raw-sources\genteca\gst-labels\                        — Artes GST originales + redlines
C:\RAUL\03-projects\genteca\                                               — Este plan
C:\RAUL\04-system\02-agents\                                               — Agent files del repo
```

---

## Para retomar esta sesión

1. Abrir Claude Code en `C:\RAUL`
2. El contexto de personas, hipótesis y archivos ya estará en memoria
3. Decir: "retomemos el plan de mejora de agentes Genteca" o elegir directamente A, B o C
