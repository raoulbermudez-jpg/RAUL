# ARCHITECTURE — Content Supply Chain Multimodal (Sistema Raul)

**Versión:** 1.1
**Última actualización:** 2026-05-03
**Alcance:** Arquitectura transversal — aplica a todos los dominios (Genteca, Finca, Plenus, futuros).

---

## 1. Capas de la Content Supply Chain

La cadena opera en 5 capas. Cada capa tiene función propia y no invade el scope de las demás.

| Capa | Nombre | Función | Agentes |
|------|--------|---------|---------|
| 1 | **Orquestación** | Entry point único. Clasifica, enruta, registra. Nunca ejecuta. | Raul |
| 2 | **Estrategia de contenido** | Traduce objetivo de negocio en plan: audiencia, mensaje, formato, cadencia. Define el QUÉ y el POR QUÉ. | Aurelio, Nerea |
| 3 | **Producción multimodal** | Ejecuta las piezas — visual estático, video, audio (single y multi-voz), motion graphics. Es el CÓMO. | Atlas, Luma, Vela, Orfeo |
| 4 | **Gobernanza de marca y riesgo** | Revisión obligatoria antes de publicar. Marca, tono, riesgo legal/comercial, precisión. | Bruna |
| 5 | **Distribución, reciclaje y memoria** | Publica, versiona, archiva, recicla. Mantiene memoria de activos. | Ivo, Sira |

---

## 2. Agentes Transversales

| Agente | Misión | Qué hace | Qué NO hace | Inputs | Outputs |
|--------|--------|----------|-------------|--------|---------|
| **Aurelio** | Content Strategist | Define estrategia por campaña/lanzamiento: audiencia, mensaje central, mix de formatos, cadencia | No escribe guiones; no produce piezas; no aprueba salida pública | Brief del Owner, insumos de dominio (Vera/Orlan/Paxs), messaging de Vael | Plan de contenido: objetivos, audiencia, formatos, calendario tentativo |
| **Nerea** | Script & Narrative Architect | Convierte el plan de Aurelio en guiones, hooks, estructura narrativa y copy base | No define estrategia; no produce audio/video; no aprueba | Plan de Aurelio, messaging de Vael, insumos técnicos | Guiones completos, hooks, copy base por pieza |
| **Vela** | Voiceover & Audio Production Lead (VE-1..VE-5) | **Único productor de audio del CSC**: produce voiceover single-voice y conversaciones de una o dos voces (diálogo / podcast corto) ejecutando NE-4 con turnos etiquetados (Voz A, Voz B). Aplica guías de pronunciación, pausas y notas de tono por voz | No inventa diálogos multi-voz; no reasigna turnos; no produce video ni visuales | Guion de Nerea (NE-1 / NE-4 single o multi-voz), copy de Solenne, VA-X, BR-X | VE-1 Voiceover Execution Script (etiquetas hablante en multi-voz), VE-2 Timing & Pacing Map, VE-3 Audio Direction Notes, VE-4 Voice Bundle, VE-5 Handoff a Luma e Ivo |
| **Luma** | Video Production Lead (LU-1..LU-5) | Produce piezas de video: shorts, reels, largo. Integra guion + audio + visuales estáticos + motion graphics | No escribe guion; no produce audio (Vela); no produce visuales estáticos (Atlas) ni motion (Orfeo); no aprueba publicación | NE-1 / NE-2 de Nerea, audio de Vela (single o multi-voz), visuales de Atlas, motion de Orfeo | LU-1 Video Spec, LU-2 Cut List, LU-3 Multi-Format Adaption, LU-4 Caption & On-Screen Text, LU-5 Handoff a Ivo |
| **Orfeo** | Motion Graphics & Visual Systems Production Lead (OR-1..OR-5) | Convierte sistemas visuales y layouts estáticos en motion graphics, overlays, transiciones, composiciones animadas y assets reutilizables para integrar en video | No produce audio (Vela); no produce visuales estáticos base (Atlas); no edita video final (Luma); no inventa contenido | NE-X de Nerea, SO-X de Solenne, VA-X, BR-X, AT-X de Atlas, visual system de Oz | OR-1 Motion System Spec, OR-2 Animated Asset Pack, OR-3 Scene Motion Map, OR-4 Format Adaptation Plan, OR-5 Handoff a Luma / Ivo |
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
├── Vela    →  audio (single-voice o multi-voz desde NE-4 etiquetado)
└── Orfeo   →  motion graphics / overlays (si aplica)
    ↓
Bruna                  →  revisión de cada pieza
    ↓
Ivo                    →  plan de publicación por canal
    ↓
Sira                   →  archivo + versionado
```

### Cadena B — Conversación estilo Studio / podcast de una o dos voces

```
Dominio (Vera / Orlan / Paxs)  →  briefing técnico / perspectivas
    ↓
Aurelio                        →  plan: ángulo, audiencia, duración, host-mix
    ↓
Nerea                          →  NE-4 multi-voz con turnos etiquetados
                                  (Voz A, Voz B, etc.) + bloques temáticos
    ↓
Solenne                        →  SO-X copy editorial / on-screen / captions
    ↓
Vela (OBLIGATORIO)             →  ejecuta audio multi-voz desde NE-4
                                  etiquetado (ver Gate 3)
    ↓
(opcional) Luma                →  video-cast si aplica (puede integrar
                                  motion de Orfeo si la pieza lo requiere)
    ↓
Bruna                          →  revisión (riesgo en opiniones / claims técnicos)
    ↓
Ivo                            →  distribución (IV-1..IV-5)
    ↓
Sira                           →  archivo + reciclaje vía AU-5
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
                        (NE-1 narrado o NE-4 single/multi-voz según pieza)
    ↓
Vivienne              →  deck base (estructura visual)
Atlas                 →  refuerzo visual de slides clave (estático)
Orfeo                 →  motion graphics / overlays si la pieza lo requiere
Vela                  →  audio: voz-única o multi-voz (una o dos voces)
                        ejecutando NE-4 etiquetado
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

### Gate 2 — Nerea antes de Atlas / Luma / Vela / Orfeo cuando hay guion

**Regla:** Ningún agente de producción arranca sin guion/copy finalizado por Nerea.

**Por qué:** Producir sin guion estable genera piezas inconsistentes, múltiples versiones y re-grabaciones costosas.

**Cómo aplicar:** Atlas/Luma/Vela/Orfeo reciben guion completo antes de ejecutar. Si el guion cambia a mitad, se detiene y se re-baseline.

### Gate 3 — Vela obligatorio para audio multi-voz (una o dos voces)

**Regla:** Cualquier contenido con audio (voz única o conversación de hasta dos voces) pasa por Vela. Para multi-voz, Vela ejecuta NE-4 con turnos **etiquetados** (Voz A, Voz B) entregado por Nerea.

**Por qué:** Vela es el único productor de audio del CSC. Centralizar voz única + multi-voz en Vela garantiza coherencia de pronunciación, voz de marca y trazabilidad de claims/caveats. Ningún otro agente del CSC produce audio.

**Cómo aplicar:** Al activar Cadena B o cualquier pieza con audio multi-voz, Nerea entrega NE-4 con turnos etiquetados; Vela ejecuta sin reasignar turnos ni inventar diálogos. Si la ejecución revela fricción (densidad verbal, caveat que no encaja), Vela escala a Nerea + Solenne; no improvisa.

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
