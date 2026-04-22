# ROUTING GUIDE — Sistema Raul
**Versión:** 1.0 — post Grupos A–D
**Última actualización:** 2026-04-20
**Fuente:** CLAUDE.md · AGENT.md de todos los agentes · CHANGELOG_GrupoA/B/C/D.md

---

## 1. Principios Generales de Routing

### Arquitectura de capas

| Capa | Quién | Alcance |
|------|-------|---------|
| **Capa 1 — Orquestación** | Raul | Singleton. Recibe toda petición del Owner. Nunca ejecuta. Enruta, registra, entrega. |
| **Capa 2 — Servicios Globales** | Michelina, Paxs, Vivienne | Transversales a todos los dominios (Genteca, Finca, Plenus, futuros). |
| **Capa 3 — Especialistas Genteca** | Vera, Orlan, Solenne, Vael, Celeste, Renzo, Oz | Anclados a Genteca. Se clonan — no se reutilizan — para otros dominios. |

### Regla cardinal
**Raul nunca ejecuta.** Si la respuesta a una petición requiere investigar, escribir, diseñar o editar — eso lo hace un agente. Raul enruta, consolida y entrega.

### Pregunta diagnóstica antes de enrutar

Antes de delegar, Raul se hace estas preguntas en orden:

1. **¿Es un pedido de contratación o definición de rol?** → Michelina + Paxs.
2. **¿Es investigación pura sin dominio específico?** → Paxs.
3. **¿Es una presentación ejecutiva?** → Vivienne (global).
4. **¿Cruza más de un dominio?** → Raul descompone en sub-tareas por dominio; Vivienne integra si hay deck final.
5. **¿A qué dominio pertenece la tarea?** → Enrutar al especialista de ese dominio (Capa 3).
6. **¿Ningún agente la cubre?** → Michelina contrata antes de continuar.

---

## 2. Tabla de Routing por Tipo de Petición

### 2A — Casos de Contenido y Comunicación

*Para contenido multimodal específico (video/audio/visuales), ver §6 Content Supply Chain (Capas 2–5).*

| Petición del Owner | Dominio | Agente principal | Cadena / Notas |
|---|---|---|---|
| "¿Cómo debería comunicar el lanzamiento de [producto]?" | Genteca | **Vael** | Vael define el campaign brief → Solenne ejecuta las piezas |
| "Define el tono de voz / mensajes clave de Genteca" | Genteca | **Vael** | Vael produce el framework; Solenne lo usa luego |
| "Escríbeme un post de LinkedIn / carrusel / email / script" | Genteca | **Solenne** | Solo si ya existe framework de Vael. Si no existe → Vael primero |
| "Necesito un caso de estudio / white paper / descripción de producto" | Genteca | **Solenne** | Verificar si hay brief de Vael disponible |
| "Naming de nueva sub-línea / tagline / headline para web" | Genteca | **Vael** | Copy estratégico puntual — exclusivo de Vael |
| "Auditoría de cómo comunica la competencia (share-of-voice, percepción)" | Genteca | **Vael** | Vael hace percepción de marca; Orlan hace benchmarking de producto |
| "Campaña nueva — primera vez en este segmento o audiencia" | Genteca | **Vael primero** | Gate obligatorio Vael → Solenne (ver Sección 4) |
| "Web copy, press release, pieza de alto impacto" | Genteca | **Vael primero** | Gate obligatorio Vael → Solenne (ver Sección 4) |

### 2B — Casos Técnicos de Producto

| Petición del Owner | Dominio | Agente principal | Cadena / Notas |
|---|---|---|---|
| "¿Qué dispositivo uso para proteger este motor / bomba / compresor?" | Genteca | **Vera** | Vera selecciona. Si hay dudas de campo → también Renzo |
| "¿Esta selección técnica cumple la norma IEC/NEMA?" | Genteca | **Vera** | Vera interpreta la norma |
| "¿Cuál es el equivalente técnico de X en Siemens/Schneider para esta instalación?" | Genteca | **Vera** | Equivalencia técnico-aplicativa |
| "¿Cómo conecto / cableo este dispositivo? ¿Qué pasos sigue el técnico?" | Genteca | **Renzo** | Renzo lee diagramas y crea guía de campo |
| "¿Cómo interpreto / leo este diagrama de conexión?" | Genteca | **Renzo** | Renzo tiene visión nativa de imágenes |
| "¿Qué falla puede tener este equipo y cómo la resuelvo?" | Genteca | **Renzo** | Renzo crea árbol troubleshooting |
| "Necesito material de capacitación para técnicos / instaladores" | Genteca | **Renzo** | Renzo crea desde cero |
| "Nota de aplicación — cuándo y cómo usar este dispositivo" | Genteca | **Renzo** | Renzo crea; Oz puede pulir si va a publicarse |
| "Este spec sheet / manual necesita quedar listo para Ozwaldo" | Genteca | **Oz** | Oz redlinea / edita documento existente |
| "Tenemos cambios de especificación — necesito redlines para el diseñador" | Genteca | **Oz** | Oz produce PDF anotado + delta Markdown |
| "Hay inconsistencias de terminología entre documentos del mismo producto" | Genteca | **Oz** | Oz audita y produce delta de correcciones |
| "Tengo un borrador técnico en texto plano — quiero convertirlo en spec sheet" | Genteca | **Oz** | Oz formaliza; valores técnicos deben venir del Owner/Vera/I&D |
| Tarea mixta: nueva guía técnica + doc publicable | Genteca | **Renzo → Oz** | Renzo crea contenido; Oz refina y produce entregable para Ozwaldo |
| Tarea mixta: selección técnica + cumplimiento normativo | Genteca | **Vera** | Una sola tarea; Vera cubre ambas |

### 2C — Casos de Inteligencia Competitiva y Mercado

| Petición del Owner | Dominio | Agente principal | Cadena / Notas |
|---|---|---|---|
| "¿Cómo estamos frente a Schneider / Eaton / Siemens comercialmente?" | Genteca | **Orlan** | Benchmarking comercial y estratégico |
| "¿Qué están lanzando los competidores? ¿Qué hay en ferias / patentes?" | Genteca | **Orlan** | Radar de producto |
| "¿Cuánto vale el mercado de [segmento] en [región]?" | Genteca | **Orlan** | Market sizing |
| "¿Hacia dónde va el HMI / conectividad en protección industrial?" | Genteca | **Orlan** | Trend report |
| "Brief competitivo para lanzamiento de [producto]" | Genteca | **Orlan** | Output de Orlan alimenta brief de Vael |
| Tarea mixta: benchmarking competitivo + posicionamiento de marca | Genteca | **Orlan → Vael** | Orlan entrega brief; Vael construye el framework de comunicación |
| Tarea mixta: selección técnica + benchmarking competitivo | Genteca | **Vera → Orlan** | Vera hace la parte técnica primero; Orlan añade la capa estratégica |

### 2D — Casos de Knowledge Base y Documentos

| Petición del Owner | Dominio | Agente principal | Notas |
|---|---|---|---|
| "Tengo PDFs / Word / Excel para subir a la KB" | Genteca | **Celeste** | Celeste procesa RAG_SOURCES → KB/Technical o KB/Market |
| "Procesa este lote de documentos y clasifícalos" | Genteca | **Celeste** | Celeste clasifica; pregunta si hay ambigüedad |
| "¿Está este documento en la KB? ¿Cuál es la versión más reciente?" | Genteca | **Celeste** | Celeste audita índices |

### 2E — Casos de Investigación y Contratación

| Petición del Owner | Dominio | Agente principal | Cadena / Notas |
|---|---|---|---|
| "Investiga a fondo [cualquier tema]" | Global | **Paxs** | Paxs es agnóstico de dominio |
| "Necesito un experto en [capacidad que falta]" | Global | **Michelina** | Michelina → Paxs → nuevo AGENT.md |
| "Refina el prompt / rol de [agente existente]" | Global | **Michelina** | Michelina coordina; Paxs perfila si hace falta |

### 2F — Casos de Presentación (Global)

| Petición del Owner | Dominio | Agente principal | Notas |
|---|---|---|---|
| "Necesito un deck ejecutivo / pitch / results presentation" | Global | **Vivienne** | Vivienne es global — sirve a cualquier dominio |
| "Convierte este reporte / datos en un deck" | Global | **Vivienne** | Vivienne recibe el insumo; no genera los datos |
| "Deck que mezcla Genteca + Finca (o varios dominios)" | Global | **Vivienne** | Única agente que puede integrar cross-dominio |
| Tarea mixta: investigar + presentar | Global | **Paxs → Vivienne** | Paxs entrega investigación; Vivienne construye el deck |

---

## 3. Cadenas de Valor Típicas

### Cadena 1 — Documentación técnica completa + contenido de marketing

**Cuándo:** Lanzamiento de producto nuevo o actualización mayor de especificaciones.

```
Vera
  ↓ valida especificaciones técnicas, identifica gaps normativos
Renzo
  ↓ crea guía de instalación y nota de aplicación desde cero
Oz
  ↓ redlinea spec sheet con cambios confirmados; produce delta + PDF anotado para Ozwaldo
Ozwaldo (humano)
  ↓ ejecuta cambios en diseño gráfico
Vael
  ↓ produce campaign brief y messaging framework para el lanzamiento
Solenne
  ↓ escribe posts LinkedIn, emails, scripts con el framework de Vael
```

| Eslabón | Entrega |
|---------|---------|
| Vera | Brief técnico + comparativa de dispositivos + gaps normativos |
| Renzo | Guía de instalación + árbol de troubleshooting + nota de aplicación |
| Oz | PDF anotado redline + delta Markdown para Ozwaldo |
| Ozwaldo | Spec sheet / manual / empaque diseñado |
| Vael | Campaign brief + messaging framework por audiencia |
| Solenne | Piezas de contenido publicables (LinkedIn, email, script) |

---

### Cadena 2 — Inteligencia competitiva → estrategia → contenido

**Cuándo:** Se necesita posicionar un producto frente a la competencia y comunicarlo al mercado.

```
Orlan
  ↓ produce brief competitivo: benchmarking, gaps, señales de mercado
Vael
  ↓ produce campaign brief y messaging framework usando el brief de Orlan como input
Solenne
  ↓ escribe las piezas de contenido aplicando el framework de Vael
```

| Eslabón | Entrega |
|---------|---------|
| Orlan | Competitive snapshot + benchmarking table + Orlan's Call estratégico |
| Vael | Campaign brief + positioning statement + tone adaptado por audiencia |
| Solenne | Posts, emails, scripts, caso de estudio — listos para publicar |

---

### Cadena 3 — Investigación → contratación de nuevo agente

**Cuándo:** Una tarea no puede cubrirse con el equipo actual.

```
Raul
  ↓ identifica el gap y describe la necesidad a Michelina
Michelina
  ↓ encarga a Paxs el perfil del rol
Paxs
  ↓ investiga responsabilidades, skills, herramientas del rol en el mercado real
Michelina
  ↓ diseña nombre, personalidad, expertise, herramientas → escribe AGENT.md
Raul
  ↓ presenta al nuevo agente al Owner y delega la tarea original
```

| Eslabón | Entrega |
|---------|---------|
| Raul | Brief de necesidad para Michelina (qué falta, qué dominio, ejemplos de tareas) |
| Paxs | Perfil profesional estructurado del rol real |
| Michelina | AGENT.md completo en la ruta correcta de Capa 2 o Capa 3 |

---

### Cadena 4 — Deck multi-dominio o cross-funcional

**Cuándo:** El Owner necesita una presentación ejecutiva que combina datos de varios dominios o fuentes.

```
[Agentes de dominio relevantes: Vera, Orlan, Paxs, etc.]
  ↓ cada uno entrega su insumo (datos, análisis, brief)
Raul
  ↓ consolida los insumos y los entrega a Vivienne con brief claro
Vivienne
  ↓ produce deck (.pptx / Markdown / Google Slides)
```

| Eslabón | Entrega |
|---------|---------|
| Especialistas | Datos, análisis, comparativas — cada uno en su dominio |
| Raul | Brief consolidado para Vivienne: audiencia, propósito, formato |
| Vivienne | Deck final, listo para presentar |

---

### Cadena 5 — Redacción urgente con framework existente

**Cuándo:** Vael ya entregó el framework en una sesión anterior y el Owner solo quiere una pieza nueva.

```
Raul verifica: ¿existe framework de Vael para este producto/audiencia/canal?
  ↓ Sí → directo a Solenne
  ↓ No → Vael primero (ver Gate 1)
Solenne
  ↓ escribe la pieza aplicando el framework
```

---

## 4. Gates Obligatorios

### Gate 1 — Vael → Solenne

**Cuándo Solenne DEBE esperar a Vael:**

| Situación | Señal para Raul |
|-----------|----------------|
| Campaña o lanzamiento nuevo | No existe campaign brief de Vael para este producto |
| Cambio de posicionamiento | El Owner quiere un ángulo nuevo o una audiencia diferente |
| Pieza de alto impacto | Web copy, press release, white paper, documento que define thought leadership |
| Nueva audiencia o canal | Primera vez que Genteca se dirige a ese segmento |
| Inconsistencia de tono detectada | La pieza pedida contradice el tono o mensajes ya definidos |

**Orden:** Vael primero → Solenne después.
**Si Vael ya entregó:** Raul lo confirma a Solenne y ella procede directamente.

---

### Gate 2 — Vera ↔ Orlan

**Pregunta diagnóstica de Raul:**

> *"¿El Owner quiere saber qué usar técnicamente, o quiere saber cómo estamos frente a la competencia?"*

| Situación | Agente |
|-----------|--------|
| "¿Qué dispositivo uso para esta instalación / motor / bomba?" | **Vera primero** |
| "¿Esta selección cumple la norma?" | **Vera** |
| "Equivalente técnico de X en Siemens para este tablero" | **Vera** |
| "¿Cómo estamos vs. Schneider/Eaton en el mercado?" | **Orlan** |
| "¿Qué están lanzando los competidores?" | **Orlan** |
| "Market sizing, tendencias HMI, radar de producto" | **Orlan** |
| Tarea mixta: selección técnica + posicionamiento competitivo | **Vera primero → Orlan después** |

---

### Gate 3 — Renzo ↔ Oz

**Pregunta diagnóstica de Raul:**

> *"¿Existe ya el documento, o hay que crearlo desde cero?"*

| Situación | Agente |
|-----------|--------|
| Guía de instalación / troubleshooting / capacitación que NO existe | **Renzo** (crea) |
| Interpretación de diagrama → pasos de conexión | **Renzo** |
| Spec sheet / manual / guía existente que necesita quedar listo para Ozwaldo | **Oz** (transforma) |
| Cambios de especificación confirmados → redlines para diseñador | **Oz** |
| Borrador técnico en texto plano → spec sheet formal | **Oz** |
| Inconsistencias terminológicas en documentos KB | **Oz** |
| Nueva guía técnica + publicación editorial | **Renzo primero → Oz después** |

---

## 5. Cómo Debe Usar Raul Este Documento

- **Al recibir una petición del Owner**, consulta primero la Sección 2 buscando el tipo de petición más cercano. Si no aparece exactamente, aplica la pregunta diagnóstica de la Sección 1.

- **Si la tarea es compleja o multi-parte**, descompónla en sub-tareas antes de enrutar. Cada sub-tarea tiene su agente. Raul no asigna una tarea multi-parte a un solo agente si involucra más de un dominio de expertise.

- **Antes de enrutar a Solenne**, siempre verificar: *¿existe un framework de Vael para este producto/audiencia?* Si no → Vael primero (Gate 1).

- **Antes de enrutar a Orlan**, verificar: *¿el Owner quiere decidir qué usar, o quiere entender cómo compete?* Si quiere decidir → Vera (Gate 2).

- **Antes de enrutar a Oz**, verificar: *¿existe el documento o hay que crearlo?* Si hay que crearlo → Renzo (Gate 3).

- **Para tareas en cadena**, confirmar a cada agente qué insumo recibirá del agente anterior antes de iniciarlo. No activar el siguiente eslabón hasta que el anterior haya entregado.

- **Registrar en task-log.md** cada vez que Raul delega, con formato: `| YYYY-MM-DD | [Agente] | [Resumen en una línea] | delivered / pending / blocked |`. Nunca saltarse el registro.

---

## 6. Content Supply Chain (Capas 2–5)

Cuando trabajes con contenido (texto, audio, video, visuales) usa esta tabla como primer mapa de "situación → ruta". Las cadenas A/B/C/D siguen siendo la referencia estructural; aquí solo resolvemos a quién pedir qué.

| Situación | Ruta principal |
|-----------|----------------|
| 1. Necesito definir **por qué** hacemos una pieza y para quién | Aurelio (estrategia, objetivos, audiencia) → luego Nerea (guion/copy) |
| 2. Tengo claro el objetivo, pero falta **guion/copy ejecutable** | Nerea (guion/copy); si cita datos técnicos, valida con Vera/Orlan/Paxs antes de pasar a producción |
| 3. La pieza requiere **audio multi-voz / conversación** | Nerea ya entregó guion → Orfeo (estructura de turnos + producción audio multi-host) |
| 4. La pieza requiere **voz narrada voz única** | Nerea ya entregó guion → Vela (narración + pronunciación + pausas) |
| 5. La pieza requiere **video / motion / video-cast** | Guion y audio listos → Luma (montaje, motion, exports por canal) |
| 6. La pieza requiere **visuales estáticos** (carrusel, infografía, POP…) | Guion/copy y brand kit listos → Atlas (piezas visuales estáticas, sin motion) |
| 7. Tengo una pieza ya producida y necesito decidir si puede salir pública | Bruna (governance & release: revisa marca, claims, riesgo → sello, cambios o bloqueo) |
| 8. Tengo una pieza con sello de Bruna y quiero que salga al mundo | Ivo (channel & distribution: canales, horarios, metadatos, publicación, logs para Sira) |
| 9. Quiero asegurar que una pieza publicada no se pierda y sea reciclable | Sira (archivo + catálogo + clips reciclables; propone a Aurelio para nuevos planes) |
| 10. Necesito saber qué cadena base aplica (A/B/C/D) | Consultar `04-system/02-agents/content-supply-chain/ARCHITECTURE_Content-Supply-Chain.md` |
| 11. Duda transversal, conflicto entre capas o decisión de Owner | Raul (toma la decisión, ajusta plan con Aurelio y/o lineamientos con Vael y dominio correspondiente) |

### Reglas operativas de cambio (Capa 2–5)

1. **Pieza ya publicada con error**
   - Ivo detecta o recibe el reporte.
   - Bruna re-revisa la pieza y decide:
     - despublicar inmediato (riesgo alto) y devolver a Nerea/Capa 3, o
     - corregir y mantener activa.
   - Nerea/Capa 3 corrigen según el caso.
   - Bruna aprueba la versión corregida.
   - Ivo re-publica la versión corregida.
   - Sira versiona (v1 → v2) y actualiza catálogo.

2. **Guion cambia a mitad de producción**
   - Nerea hace re-baseline del guion.
   - Capa 3 (Orfeo/Vela/Luma/Atlas) se reinicia sobre el guion nuevo.
   - Si el cambio es sustantivo, Bruna revisa como si fuera pieza nueva.

3. **Canal rechaza formato ya exportado (specs)**
   - Ivo comunica el problema de specs a Luma/Atlas.
   - Luma/Atlas re-exportan ajustando a specs de canal.
   - Ivo re-programa publicación.
   - No vuelve a Bruna si el contenido no cambió (solo el contenedor técnico).

4. **Arranque de campaña nueva con foco en reciclaje**
   - Antes de brifar a Nerea, Aurelio consulta a Sira por piezas reciclables.
   - Sira propone candidatos y clips.
   - Aurelio decide qué reciclar y en qué formatos e incorpora eso en el brief.
