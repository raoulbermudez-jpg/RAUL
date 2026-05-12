---
title: "GRN-MV — Motion Package, Reel IG Vaciado de Pozo (V1)"
type: Motion Package
agent: Orfeo
version: v1
product_code: GRN-MV
product_line: Exceline Profesional
aplicacion: Vaciado de pozo, 2 niveles, bomba sumergible
formato_primario: "9:16 — 1080×1920 px"
formatos_secundarios: "1:1 — 1080×1080 px | 16:9 — 1920×1080 px"
guion_fuente: "2026-05-12_nerea-NE2_grn-mv-IG-pozo-vaciado-short.md (NE-2 V1)"
guion_referencia_rica: "2026-05-11_nerea-NE1_grn-mv-video-script-v2.2.md"
date: 2026-05-12
contiene: "OR-1 Motion System Spec | OR-2 Animated Asset Pack | OR-3 Scene Motion Map | OR-4 Format Adaptation Plan | OR-5 Handoff Bundle"
---

# Motion Package — GRN-MV Reel V1: Vaciado de Pozo con Bomba Sumergible

---

## COVER NOTE DE ORFEO

Defaults aprobados por Owner aplicados en este paquete:

- Formato principal: 9:16 (1080×1920 px). Adaptaciones secundarias 1:1 y 16:9 en OR-4.
- Paleta: fondo gris cálido neutro (#F2F0ED) o blanco (#FFFFFF); naranja Exceline (#E8650A, confirmar con brand wiki) exclusivamente en call-outs de acción y nombre de producto.
- Tipografía: Futura Bold mínimo 28 pt en call-outs de 9:16; Handel BT para "GRN-MV" y nombre de producto; en cierre, strip de specs en Futura Regular.
- Estilo: vectorial limpio, técnico, anti-spectacle. Movimiento al servicio del mensaje.
- Logo Exceline Profesional versión positivo/negro según fondo. Logo Genteca ausente en planos de producto.
- Semántica LED verde: ON = bomba en operación (confirmado I&D Genteca 2026-05-12). Sin inversión visual.
- El 10 s anti-falsos-positivos está confirmado por Owner (Owner Override 2026-05-10/11) y por I&D verbalmente (2026-05-12). No publicado en HDE V7 RB3 a esta fecha; si la pieza se usa como spec técnica oficial ante regulador/cliente, gatear con Bruna antes de publicar.
- Flag técnico activo de NE-2 V1: posición física REF al nivel de la bomba (confirmado Owner, pendiente formalización en HDE/MAN — BD-6 abierta). El diagrama usa la verdad operativa confirmada.

---

# OR-1 — MOTION SYSTEM SPEC (V1 Pozo Vaciado)

## 1. Jerarquía visual (tres planos en 9:16)

| Plano | Contenido | Comportamiento |
|-------|-----------|----------------|
| Primer plano | Diagrama de pozo o render de producto | Estático durante cada escena; anima solo elementos específicos (nivel agua, LEDs, sondas, contador) |
| Segundo plano | Call-outs, contadores, etiquetas con flechas | Aparecen y desaparecen en sincronía con voz en off; nunca acumulan más de 2 call-outs simultáneos |
| Tercer plano | Fondo neutro sólido | Estático. Sin gradientes animados, sin texturas en movimiento |

Regla de ancla visual: el diagrama del pozo es el único elemento que ocupa el espacio completo. Nada compite con él. Los call-outs orbitan el borde del diagrama sin tapar las sondas ni los LEDs del tablero.

## 2. Transiciones entre escenas

- **Corte seco estándar:** cambio de escena sin dissolve. Aplica en la mayoría de los cortes.
- **Bumper semántico de 100 ms:** insertar un frame negro de 100 ms solo en las dos transiciones de mayor peso narrativo: (a) E1-Hook → E2-Producto, (b) E2-Producto → E3-Diagrama.
- **Fade in inicial:** 200 ms en el primer frame de la pieza completa (E1).
- **Fade out final:** 400 ms al salir del último frame de E6.
- Las transiciones entre sub-beats 4A, 4B, 4C son continuidad sobre el mismo diagrama; sin corte ni bumper, solo el movimiento del nivel del agua.

## 3. Timing de animaciones de elementos

| Elemento | Ease | Duración |
|----------|------|----------|
| Entrada/salida de call-outs (fade) | ease-in-out | 200 ms entrada / 300 ms salida |
| Transición estándar de escena | — | Corte seco (0 ms) |
| LED verde encendido (al completarse contador) | ease-out | 200 ms |
| LED verde apagado (al completarse contador) | ease-in | 200 ms |
| LED rojo encendido (retorno de energía en E5) | ease-out | 200 ms |
| Descenso del nivel del agua (vaciado activo) | ease-in | Continuo; 8–10 s para el rango MAX→MIN |
| Subida del nivel del agua (si aplica) | ease-out | Solo si se anima recarga; no aplica en V1 reel |
| Sonda sin contacto — destello de pérdida | ease-out | 300 ms destello, luego color de "sin contacto" sostenido |
| Pulso de revalidación en sonda (E5) | ease-in-out | 400 ms, un solo pulso suave |
| Contador regresivo: cada dígito | Corte directo entre números | 1 número por segundo exacto |
| Flecha de flujo en tubería | Bucle continuo | Velocidad constante mientras bomba ON |

## 4. Reglas del contador regresivo 10 s

- Tipografía: Futura Bold. Tamaño: 96 pt mínimo en 9:16. Color: blanco con halo negro de 4 px para contraste sobre cualquier fondo del diagrama.
- Posición: centrado sobre la sonda relevante (MAX en sub-beat 4A, MIN en sub-beat 4C), sin tapar la punta de la sonda. Offset vertical de 80 px hacia arriba respecto a la punta.
- Secuencia: "10" → "9" → "8" → "7" → "6" → "5" → "4" → "3" → "2" → "1" → "0". Cada número permanece exactamente 1 s en pantalla; corte directo al siguiente.
- Sin sonido de tick.
- El LED verde permanece APAGADO durante los 10 s del contador en 4A. El LED verde permanece ENCENDIDO durante los 10 s del contador en 4C (se apaga solo cuando el contador llega a 0).
- El contador desaparece con fade-out de 200 ms simultáneo al encendido/apagado del LED al llegar a 0.

## 5. Reglas de call-outs (captions)

- Máximo 2 call-outs activos simultáneamente en pantalla.
- Cada call-out tiene: fondo semitransparente (negro 60 % opacidad), padding 8 px, esquinas 4 px de radio, flecha de punta hacia el elemento señalado.
- Texto en Futura Bold 28 pt mínimo (9:16). Naranja Exceline solo para el nombre del producto y valores de specs; el resto en blanco.
- Un call-out desaparece antes de que aparezca el siguiente si ya hay 2 activos.
- Caption de estado estático (ej. "LED VERDE — ON" persistente en 4B): se permite como indicador de estado sostenido; no flota ni se mueve.

## 6. Reglas específicas de semántica LED en esta pieza

- Sub-beat 4A: LED verde apagado durante 10 s → se enciende al llegar contador a 0 → permanece encendido.
- Sub-beat 4B: LED verde sostenido encendido. Sin animación nueva.
- Sub-beat 4C: LED verde sostenido encendido durante 10 s → se apaga al llegar contador a 0.
- E5 (memoria de estado): LEDs rojo y verde se apagan simultáneamente al corte. Al retorno: LED rojo enciende primero (ease-out 200 ms); pulso en sonda MIN (no en LEDs); LED verde enciende (ease-out 200 ms). Sin parpadeo de LEDs en ningún momento.
- Prohibido: parpadear cualquier LED durante cualquier contador o durante la revalidación de E5.

## 7. Reglas de safe area y zonas exclusivas (9:16)

- Zona superior reservada: 0–150 px (UI Instagram: notch, hora, barra de progreso). Ningún elemento crítico en esta franja.
- Zona inferior reservada: 1770–1920 px (UI Instagram: barra de interacción, CTA, perfil). Ningún elemento crítico salvo strip de specs de cierre en E6, que debe quedar entre px 1650–1770 con margen de seguridad.
- Zona segura de contenido: 150–1770 px verticalmente; 60–1020 px horizontalmente (márgenes laterales de 60 px mínimo).
- El diagrama del pozo ocupa preferentemente px 300–1770 verticalmente, centrado horizontalmente.

---

# OR-2 — ANIMATED ASSET PACK (V1 Pozo Vaciado)

Lista de assets que el motion designer debe construir. Todos los assets son vectoriales (Illustrator / Adobe Animate / After Effects shapes). No se usan rasters salvo para el render/fotografía de producto en E2 y E6.

## ASSET 01 — Diagrama base del pozo (estático, con capas animables separadas)

**Descripción:** Corte transversal vertical del pozo. Estilo vectorial limpio, líneas técnicas. Sin perspectiva; vista frontal plana.

**Composición del diagrama (capas separadas en el archivo fuente):**
- Capa: paredes del pozo (rectángulo vertical, líneas de tierra a los lados — trazo técnico).
- Capa: bomba sumergible en el fondo (ícono vectorial de bomba; incluye tubería de descarga que sube por el lado del pozo y sale por la parte superior).
- Capa: sonda REF (cable + punta conductora en posición más baja, aproximadamente al nivel de la bomba, siempre sumergida en todos los estados de esta pieza).
- Capa: sonda MIN (cable + punta conductora, posición intermedia entre REF y MAX).
- Capa: sonda MAX (cable + punta conductora, posición más alta de las tres sondas).
- Capa: nivel del agua (forma vectorial rellena con color agua — azul claro técnico, no realista). Esta capa es la única que se anima verticalmente.
- Capa: tablero (rectángulo en la parte superior del frame, a la derecha del pozo; contiene relé GRN-MV vectorial y contactor).
- Capa: cables de sondas al tablero (líneas finas trazadas desde cada sonda hasta el tablero).
- Capa: tubería de descarga con flecha de flujo (la flecha es un asset animado separado — ASSET 05).

**Estado inicial (E3 diagrama comprimido):** nivel del agua claramente por encima de MAX (las tres sondas sumergidas, REF al nivel de la bomba).

**Posicionamiento en 9:16:** el pozo ocupa aproximadamente el 65 % inferior del frame (px 650–1770 verticalmente). El tablero se sitúa en el tercio superior-derecho (px 150–600 verticalmente, costado derecho). El nivel del agua en estado inicial (E3) llega al px 400 aproximadamente.

## ASSET 02 — Nivel del agua (capa animable)

**Descripción:** Forma vectorial de relleno que representa la superficie del agua dentro del pozo. Se anima como una sola capa que sube o baja en el eje Y.

**Estados:**
- Estado A: nivel sobre MAX (las tres sondas sumergidas). Color: azul claro técnico #A8D5E2 con opacidad 80 %.
- Estado B: nivel entre MAX y MIN (MAX sin contacto, MIN sumergida). Durante sub-beat 4B.
- Estado C: nivel por debajo de MIN pero por encima de REF y bomba. Estado final de sub-beat 4C.

**Animación:** el descenso de A → B → C es continuo durante los sub-beats 4B y 4C. Ease-in (acelera levemente al bajar). Velocidad promedio: el recorrido MAX→MIN tarda aproximadamente 8–10 s.

**Nota de producción:** la superficie del agua tiene una ondulación muy sutil (amplitud 2–3 px, periodo 2 s) solo cuando la bomba está activa y vaciando — indica movimiento. Sin ondulación cuando la bomba está apagada.

## ASSET 03 — Sondas animables (3 variantes)

Tres instancias del mismo asset base: REF, MIN, MAX. Cada sonda tiene dos estados visuales:

**Estado "sumergida":**
- Punta conductora: círculo de 12 px, color base técnico (#5B8FB9).
- Sin animación adicional.

**Estado "sin contacto":**
- Punta conductora: círculo de 12 px, color #9E9E9E (gris neutro).
- Al transicionar de "sumergida" a "sin contacto": destello blanco en la punta (ease-out, 300 ms) seguido de fade a gris (#9E9E9E).
- Aplica para sonda MAX al inicio de 4B y para sonda MIN al inicio de 4C.

**Estado "revalidación" (solo en E5, sonda MIN):**
- Pulso suave en la punta: escala de 1x a 1.15x y vuelta a 1x, ease-in-out, 400 ms, una sola vez. Color permanece en "sumergida".

**Nota:** la sonda REF nunca cambia de estado en esta pieza — siempre sumergida.

## ASSET 04 — LEDs del tablero (rojo + verde)

**Descripción:** Dos círculos de 20 px (o elipses según el render del relé) representando los indicadores LED sobre el relé en el tablero.

**LED ROJO:**
- Estado ON: círculo rojo sólido #D32F2F con halo difuso de 6 px mismo color, opacidad 50 %.
- Estado OFF: círculo gris oscuro #424242, sin halo.
- Transición ON→OFF y OFF→ON: ease-out / ease-in, 200 ms.
- En esta pieza (V1 Pozo): el LED rojo está ON durante toda la operación normal (equipo energizado). Se apaga solo en E5 durante el corte eléctrico. Reaparece primero al retorno de energía.

**LED VERDE:**
- Estado ON: círculo verde #388E3C con halo difuso de 6 px mismo color, opacidad 50 %.
- Estado OFF: círculo gris oscuro #424242, sin halo.
- Transición ON→OFF y OFF→ON: ease-out / ease-in, 200 ms.
- Comportamiento detallado en OR-1 §6.

**Prohibido:** ningún estado intermedio, parpadeo, ni animación de brillo pulsante durante la operación normal ni durante los contadores.

## ASSET 05 — Flechas de flujo en tubería de descarga

**Descripción:** Secuencia de 3 flechas triangulares que recorren la tubería de descarga indicando dirección del flujo.

**Animación:** bucle continuo. Cada flecha se desplaza a lo largo del trayecto de la tubería a velocidad constante. Cuando una flecha llega al extremo, se desvanece (fade-out 100 ms) y reaparece en el inicio (fade-in 100 ms). Las tres flechas están desfasadas en 33 % del ciclo.

**Estado activo:** flechas naranja Exceline (#E8650A), tamaño 14 px.
**Estado inactivo (bomba OFF):** las flechas desaparecen con fade-out 300 ms. No se animan cuando la bomba está apagada.

## ASSET 06 — Contador regresivo 10 s

**Descripción:** Texto tipográfico gigante (Futura Bold 96 pt mínimo en 9:16) que muestra el conteo de 10 a 0.

**Composición:** número sobre fondo circular semitransparente (negro 60 %, radio 60 px). Halo blanco en el texto de 2 px para contraste. Color del número: blanco.

**Dos instancias:** una para sonda MAX (sub-beat 4A) y una para sonda MIN (sub-beat 4C). Mismas propiedades visuales; solo cambia la posición en pantalla.

**Entrada:** fade-in 200 ms cuando aparece.
**Cada dígito:** corte directo, 1 s exacto por número.
**Salida:** al llegar a "0", el "0" permanece 200 ms y luego hace fade-out simultáneo con el cambio de estado del LED.

## ASSET 07 — Etiqueta de validación "10 s"

**Descripción:** Texto "Validación anti-falsos-positivos: 10 s" en Futura Bold 28 pt, blanco, sobre fondo semitransparente negro 60 %, aparece debajo del contador durante el conteo.

**Posición:** inmediatamente debajo del ASSET 06. Aparece con el contador y desaparece con él.

## ASSET 08 — Iconos de corte / retorno de energía

**ÍCONO CORTE:** relámpago con una X encima o barrado, color blanco (#FFFFFF), sobre fondo circular naranja Exceline (#E8650A), diámetro 64 px. Aparece sobre el tablero en E5.

**ÍCONO RETORNO:** relámpago simple, color blanco, mismo fondo verde (#388E3C), diámetro 64 px. Aparece sobre el tablero al retorno en E5.

**Animación de ícono:** entrada con escala desde 0.5x a 1x, ease-out, 300 ms. Salida con fade-out 200 ms.

## ASSET 09 — Icono de flecha circular (loop / ciclo)

**Descripción:** Flecha circular cerrada que indica automatización del ciclo. Solo presente en E5 al cierre de la revalidación.

**Tamaño:** 48 px. Color: blanco. Animación: rotación de 360° en 1.5 s, ease-in-out, una vez al aparecer. Luego estático.

## ASSET 10 — Lower thirds / call-outs de terminales

**Descripción:** Etiquetas de call-out para identificar terminales en el diagrama (cuando se muestran). Aplica principalmente en E3.

**Formato:** fondo semitransparente negro 60 %, texto Futura Bold 28 pt blanco (terminal en naranja Exceline), flecha indicadora hacia el elemento. Padding 8 px, esquinas 4 px.

**Lista de instancias necesarias:**
- "T5 — Sonda REF (siempre sumergida)"
- "T2 — Sonda MIN (corte de bomba)"
- "T1 — Sonda MAX (arranque de bomba)"
- "T3 / T4 — Alimentación"
- "T7 / T8 — Salida → Contactor"
- "GRN-MV → Contactor → Bomba" (etiqueta del tablero)
- "Bomba sumergible — fondo del pozo" (etiqueta de la bomba)

**Regla de aparición:** cada etiqueta aparece y desaparece individualmente sincronizada con la voz. Nunca más de 2 activas simultáneamente.

## ASSET 11 — Strip de specs (cierre E6)

**Descripción:** Barra horizontal en la parte inferior del frame (zona segura inferior) con tres bloques de specs.

**Composición:** fondo gris oscuro (#2C2C2C) al 90 % opacidad, ancho completo (1080 px en 9:16), alto 80 px. Tres bloques separados por líneas verticales finas:
- Bloque 1: "85 – 305 V~"
- Bloque 2: "Sondas hasta 300 m"
- Bloque 3: "Salida 3,5 A @ 250 V~"

**Tipografía:** Futura Bold 28 pt, blanco. Los valores numéricos en naranja Exceline. Las unidades en blanco.

**Animación:** la barra entra desde abajo (translateY de 80 px a 0) con ease-out 300 ms. Permanece 3 s. Sale con fade-out 400 ms.

## ASSET 12 — Render / fotografía de producto

**Descripción:** Imagen del GRN-MV (render o fotografía) sobre fondo neutro para E2 y E6.

**Notas para el motion designer:** este asset es raster, entregado por producción. Orfeo no produce el render; solo define cómo se usa en motion:
- E2: producto centrado en frame 9:16, fade-in 300 ms, ocupa aproximadamente el 50 % central del frame.
- E6: mismo render, fade-in 400 ms sobre fondo neutro. Strip de specs ASSET 11 aparece encima como overlay inferior.
- El logo Exceline Profesional se superpone sobre el render en ambas instancias.

---

# OR-3 — SCENE MOTION MAP (V1 Pozo Vaciado)

Tabla escena a escena. Para sincronía de voz en off, referencia a VE-X de Vela cuando se entregue (pendiente en producción).

---

## E1 — HOOK (8–10 s)

**Diagrama activo:** ninguno. Dos fotogramas esquemáticos rápidos.

| Tiempo | Elemento | Acción | Timing |
|--------|----------|--------|--------|
| 0:00 | Frame completo | Fade-in 200 ms | ease-in-out |
| 0:00–0:03 | Fotograma 1: pozo sin agua, bomba en seco | Estático. Ícono de temperatura sobre bomba | — |
| 0:03 | Corte seco | → Fotograma 2 | 0 ms |
| 0:03–0:06 | Fotograma 2: tablero con breaker caído | Estático | — |
| 0:06 | Caption "BOMBA EN SECO = QUEMADA" | Fade-in 200 ms | ease-in-out |
| ~0:03 | Caption "CORTE DE LUZ = REINICIO MANUAL" | Aparece al llegar la voz al segundo beat; anterior desaparece primero (fade-out 300 ms) | ease-in-out |
| ~0:07 | Caption "Hay un relé que resuelve ambos." | Aparece al tercer beat; anterior desaparece | ease-in-out |

**Ancla visual:** texto grande de caption es el ancla en E1; no hay diagrama de producto todavía.

**Nota de sincronía:** los tres captions se sincronizan con la voz en off (referencia VE-X de Vela). El segundo y tercer caption requieren ajuste de timing en edición.

---

## E2 — IDENTIFICACIÓN DEL PRODUCTO (6–7 s)

**Elemento central:** render/fotografía del GRN-MV (ASSET 12).

| Tiempo relativo | Elemento | Acción | Timing |
|---------|----------|--------|--------|
| 0:00 | Bumper semántico | Frame negro 100 ms | — |
| 0:10 | Render de producto | Fade-in 300 ms, centrado | ease-in-out |
| +0.5 s | "GRN-MV" (Handel BT, grande) | Fade-in 200 ms | ease-in-out |
| +0.8 s | "Exceline Profesional" | Fade-in 200 ms | ease-in-out |
| +1.2 s | Logo Exceline Profesional | Fade-in 300 ms | ease-in-out |
| +1.5 s | "Garantiza confianza y duración." | Fade-in 200 ms | ease-in-out |

**Ancla visual:** el render del producto es el ancla. Los textos orbitan sin tapar el producto.

---

## E3 — DIAGRAMA COMPRIMIDO DE CAMPO (12–15 s)

**Elemento central:** ASSET 01 (diagrama base del pozo) en estado inicial — nivel sobre MAX, todas las sondas sumergidas.

| Tiempo relativo | Elemento | Acción | Timing |
|---------|----------|--------|--------|
| 0:00 | Bumper semántico | Frame negro 100 ms | — |
| 0:10 | Diagrama base del pozo completo | Fade-in 300 ms | ease-in-out |
| +1.0 s | Call-out "Bomba sumergible — fondo del pozo" | Fade-in 200 ms | ease-in-out |
| +3.0 s | Call-out anterior desaparece → "Sonda REF (T5) — siempre sumergida" aparece | fade-out 300 ms / fade-in 200 ms | ease-in-out |
| +5.5 s | "Sonda MIN (T2) — corte de bomba" | Ídem | ease-in-out |
| +7.5 s | "Sonda MAX (T1) — arranque de bomba" | Ídem | ease-in-out |
| +9.5 s | "GRN-MV → Contactor → Bomba" | Ídem | ease-in-out |
| +11.5 s | Todos los call-outs salen | fade-out 300 ms | ease-in-out |

**Ancla visual:** el diagrama completo del pozo. Los call-outs aparecen uno a uno; el diagrama no se mueve.

**Nota:** este diagrama BASE se reutiliza en 4A, 4B, 4C y E5. El motion designer debe estructurarlo como composición pre-comp en After Effects (o equivalente) para que las capas animables (nivel del agua, LEDs, sondas) se activen sobre la misma base sin rehacer el diagrama.

---

## Sub-beat 4A — MAX SUMERGIDA → 10 s → BOMBA ON (12–14 s)

**Elemento central:** ASSET 01 + ASSET 02 (nivel sube hasta MAX) + ASSET 06 (contador sobre MAX) + ASSET 04 (LED verde).

**Secuencia de animación — ORDEN ESTRICTO:**

| Paso | Tiempo relativo | Elemento | Acción | Timing |
|------|---------|----------|--------|--------|
| 1 | 0:00 | Diagrama base (continuación desde E3) | Nivel del agua ya sobre MAX. Sondas REF, MIN, MAX sumergidas. | Estático |
| 2 | 0:00 | LED verde | Estado OFF (apagado). Se confirma visualmente que está apagado. | Estático |
| 3 | +0.5 s | Caption "Validación anti-falsos-positivos: 10 s" (ASSET 07) | Fade-in 200 ms | ease-in-out |
| 4 | +0.5 s | Contador "10" sobre sonda MAX (ASSET 06) | Fade-in 200 ms, luego cuenta regresiva | ease-in-out |
| 5 | +0.5 s a +10.5 s | Contador 10 → 9 → 8 → … → 0 | Corte directo, 1 s por número. LED verde NO cambia durante este período. | — |
| 6 | +10.5 s | Contador "0" (último frame del contador) | Permanece 200 ms | — |
| 7 | +10.5 s | LED verde: OFF → ON | ease-out 200 ms. SIMULTÁNEO con el fin del contador. | ease-out |
| 8 | +10.5 s | ASSET 05 (flechas de flujo en tubería) | Fade-in 300 ms → inicia bucle | ease-out |
| 9 | +10.7 s | Contador y etiqueta 10 s desaparecen | Fade-out 200 ms | ease-in-out |
| 10 | +11.0 s | Caption "LED VERDE — BOMBA ON" | Fade-in 200 ms | ease-in-out |
| 11 | +12.0 s | Nivel del agua comienza a descender (inicio sub-beat 4B) | ease-in, continuo | ease-in |

**Ancla visual:** el contador es el ancla durante el conteo. El diagrama es el ancla de fondo. El LED verde es el ancla de estado.

---

## Sub-beat 4B — VACIADO EN CURSO (8–10 s)

**Elemento central:** nivel del agua descendiendo de MAX hacia MIN. LED verde ON sostenido.

| Tiempo relativo | Elemento | Acción | Timing |
|---------|----------|--------|--------|
| 0:00 | Nivel del agua | Descenso continuo. Ease-in. Atraviesa el umbral de MAX durante este sub-beat. | ease-in |
| ~3–4 s (al pasar MAX) | Sonda MAX: estado → "sin contacto" | Destello blanco 300 ms → color gris #9E9E9E | ease-out |
| ~3–4 s | Caption "MAX sin contacto — la bomba continúa porque MIN sigue sumergida." | Fade-in 200 ms, permanece 3 s, fade-out 300 ms | ease-in-out |
| Continuo | ASSET 05 flechas de flujo | Bucle activo | — |
| Continuo | Caption "LED VERDE — ON" (estático) | Sostenido desde 4A | — |
| Continuo | Caption "Agua extraída →" sobre tubería | Aparece al pasar MAX; fade-in 200 ms | ease-in-out |

**Ancla visual:** el diagrama del pozo con el nivel descendiendo. El LED verde como ancla de estado.

---

## Sub-beat 4C — MIN SIN CONTACTO → 10 s → BOMBA OFF (12–14 s)

**Elemento central:** nivel del agua cae debajo de MIN. Contador sobre MIN. LED verde se apaga.

**Secuencia de animación — ORDEN ESTRICTO:**

| Paso | Tiempo relativo | Elemento | Acción | Timing |
|------|---------|----------|--------|--------|
| 1 | 0:00 | Sonda MIN: punta sale del agua | Nivel cae bajo MIN. Punta de MIN queda fuera del agua. | ease-in continuo |
| 2 | 0:00 | Sonda MIN: estado → "sin contacto" | Destello blanco ease-out 300 ms → color gris. PRIMER EVENTO. | ease-out |
| 3 | +0.5 s | Contador "10" sobre sonda MIN (ASSET 06) | Fade-in 200 ms | ease-in-out |
| 4 | +0.5 s | Caption "Validación: 10 s" (ASSET 07) | Fade-in 200 ms | ease-in-out |
| 5 | +0.5 s a +10.5 s | Contador 10 → 0. LED verde permanece ON durante todo el conteo. | Corte directo 1 s/número. ASSET 05 sigue activo. | — |
| 6 | +10.5 s | LED verde: ON → OFF | ease-in 200 ms. SIMULTÁNEO con fin del contador. | ease-in |
| 7 | +10.5 s | ASSET 05 flechas de flujo | Fade-out 300 ms → detenidas. SIMULTÁNEO. | ease-in |
| 8 | +10.7 s | Contador y etiqueta desaparecen | Fade-out 200 ms | ease-in-out |
| 9 | +11.0 s | Caption "LED VERDE — BOMBA OFF" | Fade-in 200 ms, permanece 1.5 s | ease-in-out |
| 10 | +12.0 s | Caption "Protección contra trabajo en seco." | Fade-in 200 ms | ease-in-out |
| 11 | +12.5 s | Nivel del agua se detiene (fijo entre MIN y bomba) | Estático. El nivel nunca llega a la bomba. | — |

**Ancla visual:** la sonda MIN y su estado de pérdida de contacto es el ancla narrativa. El contador es el ancla temporal. El diagrama como ancla de fondo.

---

## E5 — MEMORIA DE ESTADO (18–22 s)

**Elemento central:** diagrama base completo en estado activo (bomba extrayendo, nivel entre MAX y MIN, MIN sumergida, LED verde ON, LED rojo ON).

**Secuencia de animación — ORDEN ESTRICTO:**

| Paso | Tiempo relativo | Elemento | Acción | Timing |
|------|---------|----------|--------|--------|
| 1 | 0:00 | Estado activo: diagrama completo | Nivel entre MAX y MIN. ASSET 05 activo. LED rojo ON. LED verde ON. | Estático |
| 2 | ~2 s | Caption "Corte eléctrico." | Fade-in 200 ms | ease-in-out |
| 3 | ~2.5 s | ÍCONO CORTE (ASSET 08) sobre tablero | Escala 0.5x→1x, ease-out 300 ms | ease-out |
| 4 | ~2.5 s | LED rojo: ON → OFF | ease-in 200 ms | ease-in |
| 5 | ~2.5 s | LED verde: ON → OFF | ease-in 200 ms | ease-in |
| 6 | ~2.5 s | ASSET 05 flechas de flujo | Fade-out 200 ms | ease-in |
| 7 | ~4 s | Pausa visual breve (1–2 s) | Frame gris suave sobre tablero; diagrama quieto | — |
| 8 | ~6 s | ÍCONO CORTE desaparece / ÍCONO RETORNO (ASSET 08) aparece | Fade-out / Escala 0.5x→1x | ease-out |
| 9 | ~6 s | Caption "Retorno de energía." | Fade-in 200 ms | ease-in-out |
| 10 | ~6.2 s | LED rojo: OFF → ON | ease-out 200 ms. PRIMER LED en encenderse. | ease-out |
| 11 | ~7 s | Caption "GRN-MV revalida sondas → reanudación automática." | Fade-in 200 ms | ease-in-out |
| 12 | ~7.5 s | Sonda MIN: pulso de revalidación (ASSET 03 estado revalidación) | Escala 1x→1.15x→1x, ease-in-out, 400 ms, UNA SOLA VEZ. Sin cambio de LED. | ease-in-out |
| 13 | ~8.5 s | LED verde: OFF → ON | ease-out 200 ms. SEGUNDO LED en encenderse, DESPUÉS del pulso en sonda. | ease-out |
| 14 | ~8.7 s | ASSET 05 flechas de flujo | Fade-in 300 ms → inicia bucle | ease-out |
| 15 | ~9.5 s | Caption "LED VERDE — ON" | Fade-in 200 ms | ease-in-out |
| 16 | ~10 s | ÍCONO RETORNO desaparece | Fade-out 200 ms | ease-in-out |

**Nota crítica sobre LEDs:** en ningún momento de E5 parpadea ningún LED. La secuencia es siempre: apagan juntos → espera → rojo enciende → pulso en sonda → verde enciende. Sin variaciones.

**Ancla visual:** el tablero con los LEDs es la ancla narrativa de E5. El diagrama del pozo permanece visible como contexto.

---

## E6 — SPECS Y CIERRE (10–12 s)

**Elemento central:** render de producto (ASSET 12) + ASSET 11 (strip de specs) + logo Exceline.

| Tiempo relativo | Elemento | Acción | Timing |
|---------|----------|--------|--------|
| 0:00 | Render de producto | Fade-in 400 ms sobre fondo neutro | ease-in-out |
| +0.5 s | Logo Exceline Profesional | Fade-in 300 ms | ease-in-out |
| +1.0 s | "GRN-MV" (Handel BT) | Fade-in 200 ms | ease-in-out |
| +2.0 s | ASSET 11 Strip de specs | Entra desde abajo, ease-out 300 ms | ease-out |
| +5.0 s | Strip de specs sale | Fade-out 400 ms | ease-in-out |
| +5.5 s | Web: www.genteca.com.ve / www.exceline.com.mx | Fade-in 200 ms | ease-in-out |
| +6.5 s | "Garantiza confianza y duración." | Fade-in 200 ms | ease-in-out |
| +8.0 s | Todo el frame | Fade-out 400 ms (cierre de pieza) | ease-in-out |

---

# OR-4 — FORMAT ADAPTATION MOTION PLAN (V1 Pozo Vaciado)

## Formato primario: 9:16 — 1080×1920 px (Instagram Reel)

Todas las especificaciones de OR-1, OR-2 y OR-3 corresponden al formato 9:16. Este es el formato master.

**Safe areas (9:16 Instagram Reel):**
- Franja superior reservada: 0–150 px (UI: hora, íconos de señal, barra de progreso).
- Franja inferior reservada: 1770–1920 px (UI: barra de perfil, CTA, descripción de audio).
- Zona central segura: 150 px–1770 px verticalmente; 60 px–1020 px horizontalmente.
- El strip de specs de E6 se posiciona entre px 1650–1770 (margen de 100 px sobre la zona reservada inferior).
- El contador regresivo se posiciona siempre dentro de la zona segura central.
- El logo Exceline en E2 y E6 se posiciona en la zona central superior (px 250–450).

## Formato secundario: 1:1 — 1080×1080 px (Feed Instagram)

**Estrategia:** el diagrama del pozo se mantiene idéntico pero reposicionado. El frame recorta verticalmente: se usa el rango px 450–1530 del master 9:16 (el centro de la acción).

**Ajustes específicos:**
- El tablero, que en 9:16 está en el tercio superior-derecho, puede necesitar acercarse al cuerpo del diagrama en 1:1 para no quedar fuera de frame. El motion designer debe verificar y re-componer si el tablero queda parcialmente cortado.
- Los call-outs de terminales en E3 deben reposicionarse hacia el interior del frame si originalmente señalaban hacia los bordes del 9:16.
- El strip de specs en E6 mantiene su posición en el tercio inferior del cuadrado.
- La zona segura inferior en 1:1 es px 980–1080 (UI feed mínima). Strip de specs entre px 900–980.
- Las animaciones son idénticas al master. No se requiere re-timing.

## Formato terciario: 16:9 — 1920×1080 px (YouTube/web)

**Estrategia:** el diagrama del pozo se recompone con más aire lateral. El pozo en 9:16 es vertical; en 16:9 gana espacio a los lados que puede usarse para call-outs expandidos.

**Ajustes específicos:**
- El pozo se posiciona en el centro-izquierda del frame (aproximadamente 55 % del ancho).
- El tablero se posiciona en el tercio derecho del frame (más espacio que en 9:16).
- Los call-outs que en 9:16 aparecen superpuestos sobre el diagrama pueden expandirse hacia el margen derecho del frame, con líneas de referencia más largas. Esto mejora la legibilidad técnica para pantallas de escritorio.
- El contador regresivo puede reducirse a 72 pt (legible en pantalla 16:9 a distancia normal).
- El strip de specs de E6 mantiene su posición inferior (px 950–1030 en 1080 px de alto).
- Las animaciones son idénticas al master. No se requiere re-timing.

**Nota para Luma:** las adaptaciones 1:1 y 16:9 son derivadas del master 9:16 y no requieren reconstruir las animaciones desde cero. Se trabajan como versiones de composición (re-comp) del mismo proyecto After Effects, ajustando únicamente el encuadre y la posición de elementos.

---

# OR-5 — HANDOFF BUNDLE PARA LUMA E IVO (V1 Pozo Vaciado)

## Inventario de archivos a entregar al motion designer

| # | Documento | Ruta absoluta | Propósito |
|---|-----------|---------------|-----------|
| 1 | Este motion package completo (OR-1 a OR-5) | `C:\Raul\03-projects\genteca\grn-mv-video\2026-05-12_orfeo-OR_grn-mv-IG-pozo-vaciado_motion-package.md` | Spec master de motion |
| 2 | Guion NE-2 V1 (fuente de escenas y captions) | `C:\Raul\03-projects\genteca\grn-mv-video\2026-05-12_nerea-NE2_grn-mv-IG-pozo-vaciado-short.md` | Copy aprobado, voz en off, captions |
| 3 | Guion NE-1 v2.2 (referencia rica de intent visual) | `C:\Raul\03-projects\genteca\grn-mv-video\2026-05-11_nerea-NE1_grn-mv-video-script-v2.2.md` | Descripciones visuales detalladas por escena |

**Archivos de brand y assets de producto (requieren entrega separada por Raoul / Genteca):**
- Logo Exceline Profesional (versión positivo/negro, SVG o AI).
- Logo GRN-MV o archivo de código "Handel BT" (confirmar licencia).
- Render o fotografía del GRN-MV sobre fondo blanco/gris.
- Paleta de color oficial Exceline con valores exactos (hex + Pantone si aplica).
- Futura Bold (confirmar licencia para uso en video).

## Resumen ejecutivo para Luma (≤200 palabras)

Reel Instagram 9:16 de 90–110 s para el GRN-MV de Exceline Profesional, aplicación vaciado de pozo con bomba sumergible. La pieza explica en seis escenas cómo el relé protege la bomba del trabajo en seco y retoma automáticamente tras cortes eléctricos.

El elemento central es un diagrama vectorial técnico del pozo (corte transversal) que se mantiene como base estática en las escenas 3, 4A, 4B, 4C y 5 — solo se animan encima el nivel del agua, los LEDs del tablero y los contadores regresivos. La lógica de animación es precisa: en el arranque, el contador 10 s corre primero y el LED verde enciende al llegar a 0; en el corte, el contador corre sobre la sonda MIN y el LED verde se apaga al llegar a 0. En la escena de memoria de estado, la secuencia es: apagan ambos LEDs → retorno de energía → LED rojo primero → pulso en sonda MIN → LED verde. Sin parpadeos en ningún caso.

Paleta: fondo gris cálido / blanco, naranja Exceline en call-outs, vectorial técnico, sin spectacle. Adaptaciones 1:1 y 16:9 se producen como re-comp del master 9:16 sin rehacer animaciones.

## Decisiones diferidas al motion designer / studio

1. **Estilo de ilustración del diagrama:** se recomienda vectorial plano técnico (líneas limpias, sin degradados, sin sombras), pero el motion designer puede proponer un ligero shading en el cuerpo del pozo si mejora la lectura de profundidad. Someter a aprobación de Owner antes de ejecutar.
2. **Tratamiento del nivel del agua:** el spec define color azul claro técnico (#A8D5E2). Si el motion designer considera que otro tratamiento (ej. relleno semi-transparente con textura muy sutil) mejora la legibilidad, someter a aprobación.
3. **Render vs fotografía de producto (E2, E6):** si no hay render 3D disponible, fotografía sobre fondo blanco es aceptable. La calidad de la fotografía debe ser consistente con el estilo técnico del diagrama.
4. **Mercado objetivo (web en E6):** pendiente decisión Owner — Venezuela (genteca.com.ve) o México (exceline.com.mx) o ambas URLs. Producir con espacio para ambas opciones.
5. **Locución / VE-X de Vela:** el timing de los captions debe ajustarse a la pista de voz en off una vez producida por Vela. Los timings de OR-3 son estimados desde la voz; el motion designer ajusta contra el audio real.

## Flags de escalación antes de producción

- **Flag 1 — BD-6 abierta (posición REF en HDE/MAN):** el diagrama usa la posición confirmada por Owner (REF al nivel de la bomba, siempre sumergida). No está formalizado en HDE/MAN. Sin impacto en producción; documentar en créditos del video si se incluye nota técnica.
- **Flag 2 — 10 s en spec oficial:** el retardo de 10 s anti-falsos-positivos está confirmado por Owner e I&D verbalmente (2026-05-12) pero NO aparece en HDE V7 RB3. Si este reel se usa como material de spec técnica ante regulador o cliente corporativo, gatear con Bruna antes de publicar.
- **Flag 3 — Mercado objetivo:** sin resolver. Producción debe confirmar qué URL(s) van en E6.
- **Flag 4 — Aprobación de ingeniería Genteca:** pendiente antes de grabar locución (especialmente sub-beats 4A, 4B, 4C y E5).
