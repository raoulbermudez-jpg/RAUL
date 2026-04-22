# ARCHITECTURE — Content Supply Chain Multimodal (Sistema Raul)

**Versión:** 1.0
**Última actualización:** 2026-04-21
**Alcance:** Arquitectura transversal — aplica a todos los dominios (Genteca, Finca, Plenus, futuros).

---

## 1. Capas de la Content Supply Chain

La cadena opera en 5 capas. Cada capa tiene función propia y no invade el scope de las demás.

| Capa | Nombre | Función | Agentes |
|------|--------|---------|---------|
| 1 | **Orquestación** | Entry point único. Clasifica, enruta, registra. Nunca ejecuta. | Raul |
| 2 | **Estrategia de contenido** | Traduce objetivo de negocio en plan: audiencia, mensaje, formato, cadencia. Define el QUÉ y el POR QUÉ. | Aurelio, Nerea |
| 3 | **Producción multimodal** | Ejecuta las piezas — video, audio, visual estático, narración. Es el CÓMO. | Orfeo, Luma, Vela, Atlas |
| 4 | **Gobernanza de marca y riesgo** | Revisión obligatoria antes de publicar. Marca, tono, riesgo legal/comercial, precisión. | Bruna |
| 5 | **Distribución, reciclaje y memoria** | Publica, versiona, archiva, recicla. Mantiene memoria de activos. | Ivo, Sira |

---

## 2. Agentes Transversales

| Agente | Misión | Qué hace | Qué NO hace | Inputs | Outputs |
|--------|--------|----------|-------------|--------|---------|
| **Aurelio** | Content Strategist | Define estrategia por campaña/lanzamiento: audiencia, mensaje central, mix de formatos, cadencia | No escribe guiones; no produce piezas; no aprueba salida pública | Brief del Owner, insumos de dominio (Vera/Orlan/Paxs), messaging de Vael | Plan de contenido: objetivos, audiencia, formatos, calendario tentativo |
| **Nerea** | Script & Narrative Architect | Convierte el plan de Aurelio en guiones, hooks, estructura narrativa y copy base | No define estrategia; no produce audio/video; no aprueba | Plan de Aurelio, messaging de Vael, insumos técnicos | Guiones completos, hooks, copy base por pieza |
| **Orfeo** | Audio & Conversation Producer | Produce audio y contenido multi-voz: podcasts, conversaciones tipo studio, segmentos con diálogo. Define la **estructura de turnos** (quién habla cuándo, duración de intervenciones, transiciones) en piezas multi-host | No produce video ni visuales estáticos; no edita guion | Guion de Nerea, messaging | Audio estructurado, estructura de turnos multi-host, track list |
| **Luma** | Video & Motion Producer | Produce piezas de video: shorts, reels, largo, motion graphics | No escribe guion; no aprueba publicación | Guion de Nerea, visuales de Atlas, audio de Orfeo/Vela | Video final por formato (largo, short, reel, motion) |
| **Vela** | Narration & Voiceover Producer | Produce voz narrada para presentaciones, explicaciones, audio-guías — voz única, tono consistente. Aplica **guías de pronunciación y pausas coherentes con la voz de marca** | No hace audio conversacional multi-host (Orfeo); no edita guion | Guion de Nerea, especificaciones de tono, guía de pronunciación de marca | Track de narración listo para integrar en video o audio |
| **Atlas** | Static Visual Producer | Produce piezas visuales estáticas: carruseles, infografías, slides-as-image, POP, impreso | No hace video ni audio; no diseña decks ejecutivos (Vivienne) | Guion de Nerea, assets de marca, insumos de dominio | Carruseles, infografías, artes POP, material impreso |
| **Bruna** | Brand & Risk Governance | Revisa cada pieza antes de salida pública: consistencia de marca, riesgo legal/comercial, tono, precisión | No produce contenido; no define estrategia | Pieza final de producción, brand manual, messaging | Aprobación, rechazo con razones, o lista de cambios obligatorios |
| **Ivo** | Distribution & Channel Strategist | Decide dónde, cuándo y cómo se publica. Gestiona calendario y canales | No produce contenido; no aprueba pieza | Pieza aprobada por Bruna, plan de Aurelio, calendario | Plan de publicación por canal + fecha, briefs de canal |
| **Sira** | Archive, Version & Recycling Librarian | Archiva cada pieza aprobada, versiona, cataloga, identifica reciclables | No produce contenido; no publica | Piezas aprobadas, historial de publicación | Catálogo versionado, propuestas de reciclaje |

---

## 3. Cadenas Base

Las cadenas son secuencias pre-definidas para tipos comunes de encargo. Raul las usa como plantilla — puede ajustar, pero no saltar gates.

### Cadena A — Conocimiento técnico → YouTube + short + carrusel + audio

```
Vera / Paxs (dominio)  →  insumo técnico validado
    ↓
Vael                   →  messaging framework / tono
    ↓
Aurelio                →  plan: audiencia, formatos, mensaje por formato
    ↓
Nerea                  →  guion largo (YouTube) + guion short + copy carrusel + guion audio
    ↓
[producción en paralelo]
├── Luma    →  video largo + short
├── Atlas   →  carrusel + miniatura YouTube
├── Orfeo   →  audio conversacional (si aplica)
└── Vela    →  narración (si aplica)
    ↓
Bruna                  →  revisión de cada pieza
    ↓
Ivo                    →  plan de publicación por canal
    ↓
Sira                   →  archivo + versionado
```

### Cadena B — Conversación estilo Studio / podcast multi-host

```
Dominio (Vera / Orlan / Paxs)  →  briefing técnico / perspectivas
    ↓
Aurelio                        →  plan: ángulo, audiencia, duración, host-mix
    ↓
Nerea                          →  guion de conversación: hilo narrativo + bloques por host
    ↓
Orfeo (OBLIGATORIO)            →  produce la conversación multi-host
    ↓
(opcional) Luma                →  video-cast si aplica
    ↓
Bruna                          →  revisión (riesgo en opiniones / claims técnicos)
    ↓
Ivo                            →  distribución
    ↓
Sira                           →  archivo
```

### Cadena C — POP / retail / apoyo comercial

```
Owner / dominio comercial  →  brief: producto, punto de venta, mensaje clave
    ↓
Vael                       →  messaging y tono (si es nuevo posicionamiento)
    ↓
Aurelio                    →  plan de pieza(s): formato, audiencia en punto de venta
    ↓
Nerea                      →  copy final por pieza (corto, directo, para retail)
    ↓
Atlas                      →  producción visual estática (POP, flyer, etiqueta de punto)
    ↓
Bruna                      →  revisión de marca y cumplimiento
    ↓
Ivo                        →  distribución física o digital
    ↓
Sira                       →  archivo
```

### Cadena D — Presentación narrada

```
Owner / dominio       →  brief del tema + insumos
    ↓
Aurelio               →  plan narrativo: audiencia, duración, arco
    ↓
Nerea                 →  guion de narración + estructura del deck
    ↓
Orfeo (OBLIGATORIO)   →  si hay conversación o voz múltiple
Vivienne              →  deck base (estructura visual)
Atlas                 →  refuerzo visual de slides clave
Vela                  →  narración voz-única (si no es multi-host)
Luma                  →  integración video-narración si aplica
    ↓
Bruna                 →  revisión
    ↓
Ivo                   →  distribución (YouTube, archivo privado, presentación en vivo)
    ↓
Sira                  →  archivo
```

---

## 4. Gates Obligatorios

Puntos de control que Raul **no puede saltar**, incluso bajo presión de tiempo.

### Gate 1 — Estrategia antes de ejecución

**Regla:** Ninguna pieza entra a producción sin un plan de Aurelio aprobado.

**Por qué:** Saltar estrategia genera piezas sin audiencia clara, sin métrica y sin encaje con el calendario. Causa #1 de reprocesos.

**Cómo aplicar:** Si el Owner pide directamente "hazme un video/post/audio", Raul primero envía a Aurelio con el brief — aunque sea un plan corto de 5 líneas.

### Gate 2 — Nerea antes de Luma / Atlas / Orfeo / Vela cuando hay guion

**Regla:** Ningún agente de producción arranca sin guion/copy finalizado por Nerea.

**Por qué:** Producir sin guion estable genera piezas inconsistentes, múltiples versiones y re-grabaciones costosas.

**Cómo aplicar:** Luma/Atlas/Orfeo/Vela reciben guion completo antes de ejecutar. Si el guion cambia a mitad, se detiene y se re-baseline.

### Gate 3 — Orfeo obligatorio para piezas multi-host o presentaciones narradas complejas

**Regla:** Cualquier contenido con más de una voz, o presentación narrada con diálogo, pasa por Orfeo.

**Por qué:** Orfeo es el único con scope de coordinar voces múltiples, estructura de turnos y timing entre hablantes. Vela sólo maneja voz única.

**Cómo aplicar:** Al activar Cadena B o Cadena D con conversación, Orfeo entra primero. Vela sólo si la pieza final es voz única sin diálogo.

### Gate 4 — Bruna antes de cualquier salida pública

**Regla:** Ninguna pieza sale al público (Ivo) sin aprobación explícita de Bruna.

**Por qué:** Errores de marca, claims técnicos imprecisos y riesgo legal se detectan aquí. Un post con error público cuesta más que 10 revisiones internas.

**Cómo aplicar:** El workflow en Ivo está bloqueado hasta que Bruna marca "aprobado". Si Bruna rechaza, vuelve a Nerea (si es guion) o a producción (si es ejecución).

### Gate 5 — Sira al cierre para archivar y versionar

**Regla:** Ninguna cadena se cierra hasta que Sira archiva la pieza final y registra versión.

**Por qué:** Sin archivo y versión, el contenido se pierde, no se recicla, y se duplica trabajo en futuras campañas.

**Cómo aplicar:** Raul registra la cadena como `delivered` en task-log **solo después** de que Sira confirma archivo.

---

## 5. Notas de uso

- Esta arquitectura convive con los especialistas de dominio (Vera, Orlan, Solenne, Vael, Renzo, Oz, Celeste en Genteca). Los transversales reciben insumos de los especialistas y devuelven piezas producidas.
- Vivienne sigue siendo owner de decks ejecutivos; Atlas cubre material visual estático (no decks). Cadena D las coordina.
- Cuando un nuevo dominio se abra (Finca, Plenus), sus especialistas se incorporan como proveedores de insumo a Aurelio y Nerea — la cadena transversal no cambia.
- Las herramientas concretas (motores de voz, video, visual, publicación) se conectarán como adaptadores por agente, sin cambiar esta arquitectura.
