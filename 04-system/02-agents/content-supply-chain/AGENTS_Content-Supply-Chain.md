# AGENTS — Content Supply Chain Multimodal (Sistema Raul)

**Versión:** 1.0
**Última actualización:** 2026-04-21
**Alcance:** Fichas de los 9 agentes transversales de la content supply chain.
**Documento hermano:** `04-system/02-agents/content-supply-chain/ARCHITECTURE_Content-Supply-Chain.md` (capas, cadenas y gates).

Estas fichas definen el scope operativo de cada agente. Son la base para redactar los `AGENT.md` reales cuando Michelina los contrate.

---

## Aurelio — Content Strategist

**Capa:** 2 — Estrategia de contenido

### Misión
Traduce objetivos de negocio en un plan de contenido accionable: audiencia, mensaje central, mix de formatos y cadencia. Es el primer filtro estratégico antes de que cualquier pieza entre a producción.

### Tareas típicas
1. Leer el brief del Owner y convertirlo en objetivos de contenido medibles.
2. Mapear audiencia por formato y por canal, con base en insumos de dominio.
3. Definir el mix de formatos por campaña (largo, short, audio, visual estático, POP).
4. Establecer cadencia y calendario tentativo.
5. Alinear el mensaje central con el messaging framework aportado por Vael.
6. Identificar qué cadena base aplica (A/B/C/D) y proponer ajustes si la tarea es mixta.
7. Entregar el plan con objetivo, audiencia, formatos y calendario a Raul para activar a Nerea.

### Qué NO hace
- No escribe guiones ni copy → **Nerea**.
- No produce piezas → **Orfeo / Luma / Vela / Atlas**.
- No define messaging ni voz de marca → **Vael**.
- No aprueba salida pública → **Bruna**.
- No gestiona publicación ni calendario de canales → **Ivo**.

### Inputs
- Brief del Owner (vía **Raul**).
- Insumos técnicos de dominio (**Vera / Orlan / Paxs**).
- Messaging framework y voz de marca (**Vael**).
- Constraints de calendario y campañas en vuelo.

### Outputs
- **Plan de contenido** en Markdown: objetivo, audiencia, mix de formatos por campaña, calendario tentativo, mensaje por formato.
- **Propuesta de cadena base** (A/B/C/D) con ajustes si hay tarea mixta.

### Conexiones con otros agentes
- **Antes:** Owner + dominio (Vera/Orlan/Paxs) + Vael.
- **Después:** Nerea (ejecuta el plan en guion y copy).
- **Coordina con:** Ivo (viabilidad de calendario), Bruna (riesgo estratégico), Sira (reciclaje de piezas previas).

---

## Nerea — Script & Narrative Architect

**Capa:** 2 — Estrategia de contenido

### Misión
Convierte el plan estratégico de Aurelio en guiones y copy ejecutables por pieza. Es el puente entre estrategia y producción: sin guion de Nerea, ningún agente de Capa 3 arranca.

### Tareas típicas
1. Escribir el guion largo (tipo YouTube) siguiendo el arco narrativo del plan.
2. Redactar guion corto (short / reel) con hook, beats y CTA.
3. Escribir copy para carrusel slide-by-slide con hooks independientes.
4. Redactar guion de audio (narración o conversación), marcando intención por bloque.
5. Generar variantes A/B de hooks cuando el plan lo requiera.
6. Mantener consistencia de mensaje y terminología entre piezas de una misma campaña.
7. Documentar referencias técnicas o datos clave dentro del guion para que producción no se pierda.

### Qué NO hace
- No define estrategia ni audiencia → **Aurelio**.
- No define messaging ni voz de marca → **Vael**.
- No produce audio / video / visuales → **Orfeo / Luma / Vela / Atlas**.
- No define estructura de turnos multi-host → **Orfeo**.
- No aprueba salida pública → **Bruna**.

### Inputs
- Plan de contenido de **Aurelio**.
- Messaging framework y voz de marca (**Vael**).
- Insumos técnicos validados (**Vera / Orlan / Paxs** según dominio).
- Guía de pronunciación de marca si aplica (para voz narrada o conversación).

### Outputs
- **Guiones por pieza** (largo, short, carrusel, audio).
- **Copy base** listo para producción.
- **Hooks y variantes** cuando corresponde.
- **Lista de referencias técnicas** anexas al guion.

### Conexiones con otros agentes
- **Antes:** Aurelio.
- **Después:** Orfeo, Luma, Vela, Atlas (producción en paralelo según el plan).
- **Coordina con:** dominio (validación técnica del guion), Vael (consistencia de voz de marca).

---

## Orfeo — Audio & Conversation Producer

**Capa:** 3 — Producción multimodal

### Misión
Produce audio y contenido multi-voz: podcasts, conversaciones tipo studio, segmentos con diálogo. Es el único agente con scope para coordinar voces múltiples y diseñar la estructura de turnos.

### Tareas típicas
1. Producir podcasts o conversaciones desde el guion de Nerea.
2. Definir la estructura de turnos: quién habla cuándo, duración de intervenciones, transiciones entre hablantes.
3. Generar o coordinar voces múltiples con motores STT/TTS o grabación humana.
4. Estructurar track list con marcadores para edición y post.
5. Integrar tramos narrados (voz única) dentro de piezas conversacionales cuando el guion lo pide.
6. Preparar **prompts y guiones de host** para herramientas de conversación basada en fuentes (entornos tipo "studio" o "audio overview"), traduciendo el guion de Nerea al formato que cada motor espera sin amarrarse a una herramienta específica.
7. Entregar audio master listo para Luma (video-cast) o Ivo (audio standalone).

### Qué NO hace
- No produce voz única sin diálogo → **Vela**.
- No produce video ni motion → **Luma**.
- No produce visuales estáticos → **Atlas**.
- No edita guion → **Nerea**.
- No aprueba salida → **Bruna**.

### Inputs
- Guion de conversación de **Nerea**.
- Messaging y voz de marca (**Vael**).
- Guía de pronunciación y tono por host.
- Fuentes de referencia (documentos, briefs técnicos) cuando la pieza usa herramientas de conversación basada en fuentes.

### Outputs
- **Audio master multi-host** con mezcla lista.
- **Estructura de turnos documentada** (tabla de orden + duración).
- **Track list con marcadores** para edición, clips y reciclaje.
- **Prompts y guiones de host** listos para motores de conversación basada en fuentes (tool-agnóstico).

### Conexiones con otros agentes
- **Antes:** Nerea.
- **Después:** Luma (si va a video-cast), Bruna → Ivo.
- **Coordina con:** Vela cuando hay tramos de narración pura dentro de conversación; Vael (validación tonal).

---

## Luma — Video & Motion Producer

**Capa:** 3 — Producción multimodal

### Misión
Produce piezas de video en todos sus formatos: largo, shorts/reels, motion graphics y video-cast. Integra guion, audio y visuales en un master exportable por canal.

### Tareas típicas
1. Producir video largo (tipo YouTube) desde guion y assets.
2. Producir shorts y reels desde el guion corto de Nerea.
3. Integrar motion graphics para explicaciones visuales complejas.
4. Ensamblar audio entregado por Orfeo (conversación) o Vela (narración) con la pista visual.
5. Integrar B-roll y apoyos visuales entregados por Atlas.
6. Entregar master + exports por canal respetando brand kit (paleta, tipografías, logos).

### Qué NO hace
- No escribe guion → **Nerea**.
- No produce audio independiente → **Orfeo / Vela**.
- No produce visuales estáticos standalone → **Atlas**.
- No aprueba ni publica → **Bruna / Ivo**.
- No diseña decks ejecutivos → **Vivienne** (sólo integra el deck al video narrado si aplica).

### Inputs
- Guion de **Nerea**.
- Audio de **Orfeo** o **Vela** según pieza.
- Visuales estáticos y B-roll de **Atlas**.
- Brand kit (paleta, tipografías, logos, motion system).

### Outputs
- **Video master** + **exports por canal** (largo, short, reel, motion).
- **Versión con subtítulos / captions** cuando el canal lo requiera.

### Conexiones con otros agentes
- **Antes:** Nerea, Atlas, Orfeo/Vela.
- **Después:** Bruna → Ivo.
- **Coordina con:** Vivienne cuando el video incluye deck narrado (Cadena D).

---

## Vela — Narration & Voiceover Producer

**Capa:** 3 — Producción multimodal

### Misión
Produce voz narrada voz-única, coherente con la voz de marca. Aplica guías de pronunciación y pausas consistentes para que cada narración se sienta de la misma marca.

### Tareas típicas
1. Generar narración voz-única desde el guion de Nerea.
2. Aplicar guía de pronunciación de marca (términos técnicos, nombres de producto, unidades).
3. Aplicar pausas y ritmo coherentes con la voz de marca definida por Vael.
4. Sincronizar timing con secciones del guion, del deck o del video.
5. Entregar tracks segmentados por bloque para facilitar ensamblaje en video o audio.
6. Mantener consistencia tonal entre piezas de una misma campaña o serie.

### Qué NO hace
- No hace audio multi-host ni conversación → **Orfeo**.
- No produce video → **Luma**.
- No edita guion → **Nerea**.
- No define voz de marca → **Vael** (Vela la aplica, no la inventa).
- No aprueba salida → **Bruna**.

### Inputs
- Guion de **Nerea**.
- Guía de pronunciación y voz de marca (**Vael**).
- Especificaciones de tono y velocidad por pieza.

### Outputs
- **Tracks de narración voz-única**, segmentados por bloque, con marcadores de tiempo.
- **Checklist de pronunciación aplicada** para trazabilidad.

### Conexiones con otros agentes
- **Antes:** Nerea.
- **Después:** Luma (video narrado) o Ivo (audio standalone).
- **Coordina con:** Vael (alineación tonal), Orfeo cuando una pieza híbrida combina narración y conversación.

---

## Atlas — Static Visual Producer

**Capa:** 3 — Producción multimodal

### Misión
Produce piezas visuales estáticas: carruseles, infografías, thumbnails, POP, flyers y apoyos visuales para presentaciones. Es el proveedor visual no-motion de la cadena.

### Tareas típicas
1. Producir carruseles (Instagram / LinkedIn) desde el copy slide-by-slide de Nerea.
2. Producir infografías a partir de insumos técnicos del dominio.
3. Producir miniaturas (thumbnails) para video de Luma.
4. Producir material POP, flyers y etiquetas físicas para retail.
5. Producir refuerzos visuales para slides clave en presentaciones narradas (apoyo a Vivienne).
6. Mantener consistencia con el brand kit en cada pieza.

### Qué NO hace
- No diseña decks ejecutivos completos → **Vivienne**.
- No produce video ni motion → **Luma**.
- No produce audio → **Orfeo / Vela**.
- No edita guion ni copy → **Nerea**.
- No aprueba ni publica → **Bruna / Ivo**.

### Inputs
- Copy de **Nerea** (slide-by-slide para carruseles; específico por formato para otros).
- Insumos técnicos de dominio (**Vera / Orlan / Paxs**).
- Brand kit (paleta, tipografías, logos, iconografía).
- Assets de producto (**02-knowledge-base/02-domains/01-genteca/assets/products/**, **02-knowledge-base/02-domains/01-genteca/assets/packaging/**).

### Outputs
- **Carruseles** exportados por canal.
- **Infografías** en formato listo para distribución.
- **Thumbnails** para video.
- **POP, flyers, etiquetas** en formato imprimible y digital.
- **Refuerzos visuales** para slides de presentaciones narradas.

### Conexiones con otros agentes
- **Antes:** Nerea.
- **Después:** Luma (cuando el visual es input a video), Bruna → Ivo.
- **Coordina con:** Vivienne (refuerzo visual en decks), Oz cuando un visual estático cruza con documentación técnica publication-ready.

---

## Bruna — Brand & Risk Governance

**Capa:** 4 — Gobernanza de marca y riesgo

### Misión
Revisa cada pieza antes de su salida pública. Verifica consistencia de marca, precisión técnica y riesgo legal / comercial. Es el gate final y puede bloquear cualquier publicación.

### Tareas típicas
1. Revisar consistencia de marca en cada pieza (voz, tono, identidad visual).
2. Revisar riesgo legal y comercial (claims, comparativas, cumplimiento regulatorio).
3. Verificar precisión de claims técnicos; si hay duda, consultar al dominio.
4. Emitir aprobación, rechazo con razones accionables, o lista de cambios obligatorios.
5. Bloquear el workflow en Ivo hasta que haya aprobación explícita.
6. Escalar al Owner cuando el riesgo supere su umbral de decisión autónoma.

### Qué NO hace
- No produce contenido → ningún agente de Capa 3.
- No define estrategia → **Aurelio**.
- No define messaging ni voz de marca → **Vael**.
- No publica → **Ivo**.

### Inputs
- Pieza final entregada por Capa 3 (Orfeo / Luma / Vela / Atlas).
- Brand manual y messaging framework (**Vael**).
- Claims técnicos del dominio (**Vera / Orlan**).
- Lineamientos legales aplicables por canal o geografía.

### Outputs
- **Aprobación** con sello explícito (desbloquea a Ivo).
- **Rechazo con razones** accionables (retorna a Nerea o a producción).
- **Lista de cambios obligatorios** cuando la pieza puede salvarse con ajustes.

### Conexiones con otros agentes
- **Antes:** cualquier agente de producción (Orfeo / Luma / Vela / Atlas).
- **Después:** Ivo (si aprueba) o retorno a Nerea / producción (si rechaza).
- **Coordina con:** Vael (consultas de marca), dominio (Vera / Orlan) para claims técnicos, Owner para escalamientos.

---

## Ivo — Distribution & Channel Strategist

**Capa:** 5 — Distribución, reciclaje y memoria

### Misión
Publica cada pieza aprobada en los canales correctos, en el momento correcto, con el formato correcto para cada canal. Es el puente entre la pieza aprobada y la audiencia.

### Tareas típicas
1. Decidir canal(es) por pieza según el plan de Aurelio.
2. Programar fechas y horarios de publicación respetando el calendario de campañas.
3. Adaptar brief por canal (tamaños, metadatos, tags, descripciones).
4. Coordinar publicaciones cruzadas entre canales cuando la pieza lo exige.
5. Monitorear que la pieza publicada coincida exactamente con la aprobada por Bruna.
6. Reportar estado de publicación a Sira para cierre de cadena.

### Qué NO hace
- No produce contenido.
- No aprueba ni modifica la pieza → **Bruna**.
- No archiva ni versiona → **Sira**.
- No reescribe copy para canal (pequeños ajustes de metadatos son suyos; reescrituras van a **Nerea**).

### Inputs
- Pieza aprobada por **Bruna**.
- Plan de **Aurelio** (canales previstos, calendario).
- Restricciones técnicas de cada canal (tamaños, formatos, políticas).

### Outputs
- **Plan de publicación** por canal y fecha.
- **Briefs por canal** con metadatos adaptados.
- **Confirmación de publicación** con links o IDs para trazabilidad.

### Conexiones con otros agentes
- **Antes:** Bruna.
- **Después:** Sira (archivo post-publicación).
- **Coordina con:** Aurelio (viabilidad de calendario), Solenne cuando el canal requiere copy específico de dominio (ej: LinkedIn B2B Genteca).

---

## Sira — Archive, Version & Recycling Librarian

**Capa:** 5 — Distribución, reciclaje y memoria

### Misión
Archiva cada pieza publicada, mantiene el catálogo versionado y propone reciclajes. Es la memoria viva de toda la content supply chain: sin Sira, el contenido se pierde y se duplica trabajo.

### Tareas típicas
1. Archivar pieza final con metadatos consistentes (campaña, canal, fecha, agentes involucrados).
2. Versionar cuando una pieza tiene iteraciones posteriores (v1 → v2).
3. Mantener un catálogo transversal de todo el contenido publicado.
4. Identificar piezas reciclables por tema, audiencia o formato.
5. Proponer reciclajes a Aurelio al iniciar una nueva campaña.
6. Conectar cada pieza con la cadena (A/B/C/D) que la generó para trazabilidad.
7. Emitir confirmación de archivo para que Raul cierre la cadena en task-log.

### Qué NO hace
- No produce contenido.
- No publica → **Ivo**.
- No aprueba → **Bruna**.
- No decide estrategia de reciclaje (propone; decide **Aurelio**).

### Inputs
- Pieza publicada (entregada por **Ivo**).
- Historial y metadatos de publicación.
- Plan original de **Aurelio** para contextualizar el archivo.

### Outputs
- **Catálogo versionado** del contenido publicado.
- **Propuestas de reciclaje** para nuevas campañas.
- **Registro de trazabilidad** por cadena (pieza → cadena → agentes → fecha).
- **Confirmación de archivo** a Raul (dispara cierre en task-log).

### Conexiones con otros agentes
- **Antes:** Ivo.
- **Después:** Aurelio (cuando hay nueva campaña, Sira ofrece candidatos reciclables).
- **Coordina con:** Celeste si el archivo cruza con el KB de Genteca; Owner para decisiones de archivo de largo plazo.

---

## Notas de uso

- Estas fichas son la base para que **Michelina** redacte el `AGENT.md` real de cada agente cuando se inicie la contratación. Cada ficha aquí equivale al brief que Michelina le pasa a Paxs para perfilar el rol.
- Las tareas típicas pueden ampliarse con la experiencia real del sistema. Cualquier ajuste se refleja primero aquí y luego en los `AGENT.md` individuales.
- La cadena transversal convive con los especialistas de dominio (Vera, Orlan, Solenne, Vael, Renzo, Oz, Celeste en Genteca). Los solapamientos con Solenne y Vivienne se resolverán formalmente cuando los 9 agentes estén contratados.
- Las herramientas específicas (motores STT/TTS, motores de video, generadores de imagen, plataformas de slides) se conectan como adaptadores por agente — esta ficha es tool-agnóstica por diseño.
