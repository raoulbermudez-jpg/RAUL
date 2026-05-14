---
tipo: nota-de-interaccion
fecha: YYYY-MM-DD
canal:                # human↔human: conversacion | llamada | reunion | email | whatsapp | videollamada | nota-manuscrita
participantes: []
dominio: []           # genteca | plenus | finca | teca | marca-personal | transversal
artefacto_crudo:      # ruta al crudo en 01-inbox/04-interactions/_procesadas/, si existe
estado: capturada     # capturada → triada → accionada → archivada (ver criterios abajo)
---

# Nota de Interacción — <título corto>

> Plantilla de la capa de captura de interacciones (fase mínima, 2026-05-14).
> Ver `02-knowledge-base/01-foundations/PROPUESTA_capa-de-captura-de-interacciones_v1.md`.
>
> Una Nota de Interacción es una **destilación**, no un acta ni un transcript.
> 5-10 líneas. Si se siente como trabajo pesado, está mal hecha — o la
> interacción no ameritaba una nota.
>
> **Alcance:** solo interacciones **human↔human**. Las decisiones tomadas en
> sesión con el PKA (Owner↔sistema) van a `DECISIONS.md` o a memoria, no aquí.
>
> **Estados:** `capturada` = artefacto crudo en el canal, sin destilar ·
> `triada` = destilada y su contenido enrutado (puede tener acciones abiertas) ·
> `accionada` = todas las acciones ejecutables cerradas · `archivada` = sin
> acciones abiertas ni valor de consulta activa.
>
> La nota destilada se guarda en `01-inbox/04-interactions/_notas/`. Al destilar,
> el artefacto crudo se mueve de la raíz del canal a `01-inbox/04-interactions/_procesadas/`
> — la raíz queda solo con lo pendiente de destilar.

## Qué pasó

<2-3 frases de contexto mínimo. Suficiente para entender la nota dentro de seis meses.>

## Lo que quedó

<Usar solo las categorías que apliquen. Si nada cae en ninguna, esta interacción
no necesitaba una nota — el formato mismo es el filtro.>

- **Definición:** <algo quedó definido — un spec, un alcance, un criterio, un nombre, un precio>
- **Solicitud / compromiso:** <alguien pidió algo concreto, o alguien se comprometió a algo>
- **Cambio:** <algo que YA estaba definido cambió — la categoría de mayor valor y mayor decaimiento; los conflictos "pero tú dijiste..." nacen de aquí>
- **Decisión:** <se eligió entre alternativas>
- **Señal de relación:** <cambió algo en cómo trabajar con esta persona — una fricción, una preferencia de canal, un estilo, un límite>

## Acciones ejecutables

<Si las hay. No toda interacción produce una tarea — algunas solo producen una
definición que va al conocimiento, o una señal que va a la memoria de personas.>

- [ ] <acción — responsable — fecha si aplica>

## Preguntas abiertas

- <lo que quedó sin resolver>
