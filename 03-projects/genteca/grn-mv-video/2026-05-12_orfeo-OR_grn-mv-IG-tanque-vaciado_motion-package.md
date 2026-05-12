---
title: "GRN-MV — Motion Package, Reel IG Vaciado de Tanque (v2)"
type: Motion Package
agent: Orfeo
version: v2
replaces: "v1 (3 electrodos — DEPRECATED)"
product_code: GRN-MV
product_line: Exceline Profesional
aplicacion: "Vaciado de tanque, 1 nivel, bomba a la salida — residencial/condominio"
configuracion_terminales: "T1 = sonda de nivel | T2 = puenteado a T1 | T5 = electrodo común (REF) | T7 = voltaje común (NA) | T8 = carga al contactor"
electrodos: 2
formato_primario: "9:16 — 1080×1920 px"
formatos_secundarios: "1:1 — 1080×1080 px | 16:9 — 1920×1080 px"
guion_fuente: "2026-05-12_nerea-NE2_grn-mv-IG-tanque-vaciado-short.md (NE-2 v2)"
guion_referencia_rica: "2026-05-11_nerea-NE1_grn-mv-video-script-v2.2.md"
motion_package_hermano: "2026-05-12_orfeo-OR_grn-mv-IG-pozo-vaciado_motion-package.md (V1 Pozo)"
date: 2026-05-12
contiene: "OR-1 Motion System Spec | OR-2 Animated Asset Pack | OR-3 Scene Motion Map | OR-4 Format Adaptation Plan | OR-5 Handoff Bundle"
---

# Motion Package — GRN-MV Reel v2: Vaciado de Tanque Residencial con Bomba a la Salida

---

## COVER NOTE DE ORFEO

### Por qué existe esta v2

La v1 de este paquete fue producida antes de que se confirmara la configuración de electrodos de la aplicación residencial. Asumía 3 electrodos (REF + MIN + MAX, idéntico al pozo) con un flag de escalación bloqueante. El Owner confirmó el 2026-05-12, con 3 notas de aplicación del KB alineadas, que el caso residencial/condominio usa **2 electrodos**: una sonda de nivel única (T1, con T2 en puente hacia T1) y un electrodo común REF (T5) en la parte baja del tanque. Nerea actualizó el guion a NE-2 v2 en consecuencia. Este paquete de motion refleja esa decisión cerrada.

**Cambios sustantivos respecto a v1 DEPRECATED:**

| Elemento | v1 DEPRECATED | v2 (ESTE ARCHIVO) |
|----------|--------------|-------------------|
| Diagrama base (ASSET 01-T) | 3 electrodos (REF + MIN + MAX) con flag bloqueante | 2 electrodos: sonda única (T1/T2 puenteado) + electrodo común REF (T5) — CERRADO |
| Etiquetas de call-out de sondas | "MAX", "MIN", "REF" | "Sonda de nivel (T1, T2 puenteado)" + "Electrodo común / REF (T5)" |
| Nivel del agua animable (ASSET 02-T) | Descendía de estado A (sobre MAX) → B (entre MAX/MIN) → C (bajo MIN, sobre REF) — 3 estados | Desciende de estado A (sonda sumergida) → B (sonda sin contacto, REF aún sumergida) — 2 estados. Sin zona de histéresis |
| Sondas animables (ASSET 03-T) | 3 variantes: REF + MIN + MAX | 2 variantes: sonda de nivel (la única que cambia de estado) + electrodo común REF (siempre sumergido) |
| ASSET 10-T (call-outs de terminales) | Etiquetas "MAX", "MIN" | Etiquetas "Sonda de nivel (T1, T2 puenteado)" y "Electrodo común / REF (T5)" |
| Sub-beat 4B | Incluía evento "MAX pierde contacto durante vaciado en curso" | Eliminado: sin MAX, no hay evento intermedio; el nivel desciende directo hacia la sonda |
| Estructura de escenas | 6 escenas + 3 sub-beats (4A/4B/4C) — flag de densidad abierto | 7 escenas autónomas: E1 Hook / E2 Producto / E3 Diagrama / E4 Arranque / E5 Corte / E6 Memoria de estado / E7 Cierre |
| Flag de escalación bloqueante | ACTIVO — "confirmar 2 o 3 electrodos antes de producir" | CERRADO — configuración documental definitiva |
| Scene Motion Map | OR-3 con sub-beats 4A/4B/4C | OR-3 con 7 escenas autónomas; E4 = arranque, E5 = corte, sin sub-beat de vaciado intermedio |
| Memoria de estado (antes E5, ahora E6) | Revalidación lineal única | Bifurcación explícita: camino A (nivel sobre sonda al retorno → bomba reanuda) / camino B (nivel bajo sonda al retorno → bomba inhibida) |
| Posición de la bomba en diagrama | Indicada como "a la salida" pero con ambigüedad geométrica | Clarificada: bomba en tubería de SALIDA, parte inferior/lateral del tanque, tubería hacia red residencial o hidroneumático |

**Assets que NO cambian (reutilización directa desde V1 Pozo):**

- ASSET 04 — LEDs del tablero (rojo + verde): idéntico.
- ASSET 05 — Flechas de flujo en tubería: idéntico (trayecto adapta a la geometría del tanque).
- ASSET 06 — Contador regresivo 10 s: idéntico.
- ASSET 07 — Etiqueta de validación "10 s": idéntico.
- ASSET 08 — Iconos de corte / retorno de energía: idéntico.
- ASSET 09 — Icono de flecha circular: idéntico.
- ASSET 11 — Strip de specs: idéntico (mismas specs del GRN-MV).
- ASSET 12 — Render / fotografía de producto: idéntico.

**Assets que cambian sustantivamente en v2:**

- ASSET 01-T — Diagrama base del tanque: rediseñado para 2 electrodos, sin sonda MAX.
- ASSET 02-T — Nivel del agua: 2 estados en lugar de 3; sin zona de histéresis intermedia.
- ASSET 03-T — Sondas animables: 2 variantes en lugar de 3; "sonda de nivel" reemplaza a MAX/MIN.
- ASSET 10-T — Call-outs de terminales: etiquetas actualizadas a T1/T2 puenteado y T5.

**Defaults del sistema (sin cambios respecto a V1 Pozo):**

- Formato principal: 9:16 (1080×1920 px). Adaptaciones secundarias 1:1 y 16:9 en OR-4.
- Paleta: fondo gris cálido neutro (#F2F0ED) o blanco (#FFFFFF); naranja Exceline (#E8650A, confirmar con brand wiki) exclusivamente en call-outs de acción y nombre de producto.
- Tipografía: Futura Bold mínimo 28 pt en call-outs de 9:16; Handel BT para "GRN-MV" y nombre de producto; en cierre, strip de specs en Futura Regular.
- Estilo: vectorial limpio, técnico, anti-spectacle. Movimiento al servicio del mensaje.
- Logo Exceline Profesional versión positivo/negro. Logo Genteca ausente en planos de producto.
- Semántica LED verde: ON = bomba en operación (confirmado I&D Genteca 2026-05-12). Sin inversión visual.
- El 10 s anti-falsos-positivos está confirmado por Owner (Owner Override 2026-05-10/11) e I&D verbalmente (2026-05-12). No publicado en HDE V7 RB3 a esta fecha. Si la pieza se usa como spec técnica oficial ante regulador o cliente corporativo, gatear con Bruna antes de publicar.

**Coherencia visual V1 Pozo–v2 Tanque:** el instalador que vea ambos reels debe percibir continuidad inmediata. Misma paleta, mismas formas de sondas, mismo LED, mismo contador, mismo estilo de diagrama técnico. Lo que distingue V2 es el contenedor físico (tanque rectangular elevado vs pozo subterráneo), la posición de la bomba (salida del tanque vs sumergible en el fondo del pozo), y los 2 electrodos en lugar de 3.

---

# OR-1 — MOTION SYSTEM SPEC (v2 Tanque Vaciado)

## 1. Jerarquía visual (tres planos en 9:16)

Idéntica a V1 Pozo:

| Plano | Contenido | Comportamiento |
|-------|-----------|----------------|
| Primer plano | Diagrama de tanque o render de producto | Estático durante cada escena; anima solo elementos específicos (nivel agua, LEDs, sondas, contador) |
| Segundo plano | Call-outs, contadores, etiquetas con flechas | Aparecen y desaparecen en sincronía con voz; nunca más de 2 call-outs simultáneos |
| Tercer plano | Fondo neutro sólido | Estático. Sin gradientes animados, sin texturas en movimiento |

Regla de ancla visual: el diagrama del tanque es el único elemento que llena el espacio central. Nada compite con él. Los call-outs orbitan el borde del diagrama sin tapar la sonda de nivel, el electrodo común REF, ni los LEDs del tablero.

## 2. Transiciones entre escenas

- **Corte seco estándar:** cambio de escena sin dissolve. Aplica en la mayoría de los cortes.
- **Bumper semántico de 100 ms:** insertar un frame negro de 100 ms solo en las dos transiciones de mayor peso narrativo: (a) E1-Hook → E2-Producto, (b) E2-Producto → E3-Diagrama.
- **Fade in inicial:** 200 ms en el primer frame de la pieza completa (E1).
- **Fade out final:** 400 ms al salir del último frame de E7.
- E3, E4 y E5 son continuidad sobre el mismo diagrama base: el nivel del agua desciende de E3 a E5 sin corte ni bumper entre E4 y E5, solo el movimiento del nivel. Corte seco al entrar a E6.

## 3. Timing de animaciones de elementos

Idéntico a V1 Pozo:

| Elemento | Ease | Duración |
|----------|------|----------|
| Entrada/salida de call-outs (fade) | ease-in-out | 200 ms entrada / 300 ms salida |
| Transición estándar de escena | — | Corte seco (0 ms) |
| LED verde encendido (al completarse contador) | ease-out | 200 ms |
| LED verde apagado (al completarse contador) | ease-in | 200 ms |
| LED rojo encendido (retorno de energía en E6) | ease-out | 200 ms |
| Descenso del nivel del agua en tanque (vaciado activo) | ease-in | Continuo; 6–8 s para el rango sonda sumergida → sonda sin contacto |
| Sonda sin contacto — destello de pérdida | ease-out | 300 ms destello, luego color de "sin contacto" sostenido |
| Pulso de revalidación en sonda (E6) | ease-in-out | 400 ms, un solo pulso suave |
| Contador regresivo: cada dígito | Corte directo entre números | 1 número por segundo exacto |
| Flecha de flujo en tubería de salida | Bucle continuo | Velocidad constante mientras bomba ON |

## 4. Reglas del contador regresivo 10 s

- Tipografía: Futura Bold. Tamaño: 96 pt mínimo en 9:16. Color: blanco con halo negro de 4 px para contraste sobre cualquier fondo del diagrama.
- Posición: centrado sobre la sonda de nivel (la única sonda operativa en esta aplicación). Offset vertical de 80 px hacia arriba respecto a la punta de la sonda.
- Secuencia: "10" → "9" → "8" → "7" → "6" → "5" → "4" → "3" → "2" → "1" → "0". Cada número permanece exactamente 1 s en pantalla; corte directo al siguiente.
- Sin sonido de tick.
- **E4 (arranque):** LED verde permanece APAGADO durante los 10 s del contador. El LED verde enciende solo cuando el contador llega a 0.
- **E5 (corte):** LED verde permanece ENCENDIDO durante los 10 s del contador. El LED verde se apaga solo cuando el contador llega a 0.
- El contador desaparece con fade-out de 200 ms simultáneo al encendido/apagado del LED al llegar a 0.

## 5. Reglas de call-outs (captions)

- Máximo 2 call-outs activos simultáneamente en pantalla.
- Cada call-out tiene: fondo semitransparente (negro 60 % opacidad), padding 8 px, esquinas 4 px de radio, flecha de punta hacia el elemento señalado.
- Texto en Futura Bold 28 pt mínimo (9:16). Naranja Exceline solo para el nombre del producto y valores de specs; el resto en blanco.
- Un call-out desaparece antes de que aparezca el siguiente si ya hay 2 activos.
- Caption de estado estático sostenido (ej. "LED VERDE — ON" persistente durante E4) permitido como indicador de estado; no flota ni se mueve.
- **Terminología obligatoria en v2:** usar "Sonda de nivel" (nunca "MIN" ni "MAX") y "Electrodo común / REF" (nunca solo "REF"). La terminología de 2 niveles (MAX/MIN) está reservada para la aplicación pozo.

## 6. Reglas específicas de semántica LED en esta pieza

- E4 (arranque): LED verde apagado durante 10 s → enciende al llegar contador a 0 → permanece encendido.
- E5 (corte): LED verde sostenido encendido durante 10 s → se apaga al llegar contador a 0.
- E6 (memoria de estado): LEDs rojo y verde se apagan simultáneamente al corte. Al retorno: LED rojo enciende primero (ease-out 200 ms); pulso en sonda de nivel (no en LEDs); bifurcación: si la sonda está sumergida → LED verde enciende; si la sonda está sin contacto → LED verde permanece apagado. Sin parpadeo de LEDs en ningún momento.
- Prohibido: parpadear cualquier LED durante cualquier contador o durante la revalidación de E6.

## 7. Reglas de safe area y zonas exclusivas (9:16)

Idénticas a V1 Pozo:
- Zona superior reservada: 0–150 px (UI Instagram: notch, hora, barra de progreso). Ningún elemento crítico en esta franja.
- Zona inferior reservada: 1770–1920 px (UI Instagram: barra de interacción, CTA, perfil). Ningún elemento crítico salvo strip de specs de cierre en E7, que debe quedar entre px 1650–1770 con margen de seguridad.
- Zona segura de contenido: 150–1770 px verticalmente; 60–1020 px horizontalmente (márgenes laterales de 60 px mínimo).
- El diagrama del tanque ocupa preferentemente px 400–1750 verticalmente, centrado horizontalmente. El tanque es más compacto verticalmente que el pozo; el espacio libre adicional en la parte inferior puede usarse para call-outs sin superponerlos sobre el diagrama.

---

# OR-2 — ANIMATED ASSET PACK (v2 Tanque Vaciado)

Los assets de v2 comparten el mismo sistema de diseño que V1 Pozo. Los assets de LEDs, contador, call-outs de estado, strip de specs, iconos de corte/retorno y flecha circular se reutilizan directamente. Solo los 4 assets del diagrama cambian sustantivamente.

**Resumen de reutilización:**

| Asset | Decisión v2 |
|-------|-------------|
| ASSET 01-T — Diagrama base del tanque | NUEVO — reemplaza ASSET 01 de v1 (2 electrodos, sin MAX) |
| ASSET 02-T — Nivel del agua en tanque | NUEVO — 2 estados en lugar de 3 |
| ASSET 03-T — Sondas animables | NUEVO — 2 variantes: sonda de nivel + electrodo común REF |
| ASSET 04 — LEDs | REUTILIZAR de V1 Pozo |
| ASSET 05 — Flechas de flujo | REUTILIZAR de V1 Pozo (adaptar trayecto a tubería de salida del tanque) |
| ASSET 06 — Contador regresivo 10 s | REUTILIZAR de V1 Pozo |
| ASSET 07 — Etiqueta de validación "10 s" | REUTILIZAR de V1 Pozo |
| ASSET 08 — Iconos corte / retorno de energía | REUTILIZAR de V1 Pozo |
| ASSET 09 — Icono de flecha circular | REUTILIZAR de V1 Pozo |
| ASSET 10-T — Lower thirds / call-outs de terminales | NUEVO — etiquetas actualizadas para 2 electrodos |
| ASSET 11 — Strip de specs | REUTILIZAR de V1 Pozo |
| ASSET 12 — Render / fotografía de producto | REUTILIZAR de V1 Pozo |

---

## ASSET 01-T — Diagrama base del tanque (nuevo — reemplaza ASSET 01 de v1)

**Descripción:** Corte transversal del tanque elevado residencial. Estilo vectorial técnico, líneas limpias, vista frontal plana. Coherente visualmente con el diagrama del pozo de V1 Pozo (mismo grosor de líneas, mismo estilo de rellenos, mismo tratamiento de sondas).

**Composición del diagrama (capas separadas en el archivo fuente):**

- Capa: paredes del tanque (rectángulo con sección transversal visible; incluye tapa superior desde donde cuelgan los electrodos). Indicación sutil de entrada de agua desde flotante mecánico en la parte superior — elemento secundario, no protagonista.
- Capa: electrodo común REF (T5) — cable + punta conductora en posición baja del tanque, cerca del fondo. Siempre sumergido mientras haya cualquier volumen de agua operativo. Cableado desde la tapa hacia abajo.
- Capa: sonda de nivel (T1, con T2 en puente a T1) — cable + punta conductora, posicionada más arriba que el electrodo REF; es la sonda operativa única. Cableada desde la tapa hacia abajo. Esta es la única sonda que cambia de estado en esta pieza.
- Capa: nivel del agua (forma vectorial rellena — ASSET 02-T). Esta capa es la única que se anima verticalmente.
- Capa: tablero (parte superior o lateral del frame; contiene relé GRN-MV vectorial y contactor). Posicionado en el tercio superior del frame.
- Capa: cables de sondas al tablero (líneas finas desde la tapa del tanque hasta el tablero).
- Capa: bomba monofásica a la SALIDA del tanque (en la parte inferior o lateral del tanque, en la tubería que va hacia la red de la residencia o el sistema hidroneumático). La bomba NO está en el fondo del tanque ni es sumergible.
- Capa: tubería de salida del tanque (va desde la parte inferior del tanque hacia la red residencial / hidroneumático). Incluye las flechas de flujo animadas (ASSET 05).
- Capa: indicación de tubería / suministro externo y flotante mecánico (entrada de agua al tanque — sutil, no protagonista).

**Estado inicial (E3 diagrama comprimido):** nivel del agua claramente por encima de la sonda de nivel (ambos electrodos — sonda y REF — sumergidos). El tanque no está a tope; hay espacio visible sobre el nivel del agua.

**Posicionamiento en 9:16:** el tanque ocupa preferentemente px 450–1700 verticalmente, centrado horizontalmente. El tablero se sitúa en el tercio superior del frame (px 150–500), con cables bajando hacia el tanque. La bomba se representa en la parte inferior del diagrama con la tubería de salida saliendo hacia el lateral.

**Nota crítica de geometría (diferencia con V1 Pozo):** la bomba está a la SALIDA del tanque, no sumergida. El instalador debe ver claramente que el flujo va del tanque hacia la red; la bomba es el componente que impulsa ese flujo y cuya protección es el objeto del GRN-MV. No usar la geometría del pozo (bomba en el fondo, tubería de descarga subiendo verticalmente).

## ASSET 02-T — Nivel del agua en tanque (nuevo — 2 estados)

**Descripción:** Forma vectorial de relleno que representa la superficie del agua dentro del tanque. Se anima como una sola capa que baja en el eje Y.

**Estados:**
- Estado A: nivel sobre la sonda de nivel (ambos electrodos sumergidos). Estado inicial en E3, E4 y al inicio de E5.
- Estado B: nivel entre la sonda de nivel y el electrodo REF (sonda de nivel sin contacto, REF aún sumergida). Estado final en E5. El tanque nunca se muestra absolutamente vacío.

**Animación:** el descenso de A → B es continuo durante E4 (arranque y vaciado en curso) y el inicio de E5 (hasta que la sonda pierde contacto). Ease-in. Velocidad promedio: el recorrido sonda sumergida → sonda sin contacto tarda aproximadamente 6–8 s en la animación.

**Ondulación:** igual que V1 Pozo — ondulación muy sutil (amplitud 2–3 px, periodo 2 s) solo cuando la bomba está activa y vaciando. Sin ondulación cuando la bomba está apagada.

**Color:** azul claro técnico #A8D5E2 con opacidad 80 % — idéntico a V1 Pozo para continuidad visual entre los dos reels.

**Nota de producción:** a diferencia de V1 Pozo (que tenía 3 estados: sobre MAX → entre MAX/MIN → bajo MIN), v2 tiene solo 2 estados. No hay zona intermedia de vaciado en curso con una sonda seca y otra sumergida. El nivel desciende directamente desde "sonda sumergida" hasta "sonda sin contacto" sin evento visual intermedio.

## ASSET 03-T — Sondas animables (nuevo — 2 variantes)

**Sonda de nivel (T1, T2 puenteado) — sonda operativa única:**

Estado "sumergida":
- Punta conductora: círculo de 12 px, color base técnico #5B8FB9.
- Sin animación adicional.

Estado "sin contacto":
- Punta conductora: círculo de 12 px, color #9E9E9E (gris neutro).
- Al transicionar de "sumergida" a "sin contacto": destello blanco en la punta (ease-out, 300 ms) seguido de fade a gris (#9E9E9E).
- Aplica al inicio de E5 cuando el nivel cae por debajo de la sonda.

Estado "revalidación" (solo en E6, camino A y camino B):
- Pulso suave en la punta: escala de 1x a 1.15x y vuelta a 1x, ease-in-out, 400 ms, una sola vez.
- En camino A: color permanece en "sumergida" (la sonda está cubierta al retorno de energía).
- En camino B: color permanece en "sin contacto" (la sonda está descubierta al retorno de energía).

**Electrodo común REF (T5) — siempre sumergido:**
- Estado: punta conductora 12 px, color base técnico #5B8FB9.
- No cambia de estado en ningún punto de esta pieza.
- Nota: la REF permanece sumergida incluso en Estado B (nivel entre sonda y REF); visualmente refuerza que hay agua residual en el tanque y que el circuito tiene referencia eléctrica.

Los estados visuales son idénticos a los del ASSET 03 de V1 Pozo para que el instalador reconozca el sistema al ver los dos reels.

## ASSET 04 — LEDs del tablero (rojo + verde)

**Reutilizar directamente de V1 Pozo (ASSET 04).** Mismas propiedades visuales, mismas transiciones, misma semántica.

**LED ROJO:**
- Estado ON: círculo rojo sólido #D32F2F con halo difuso de 6 px mismo color, opacidad 50 %.
- Estado OFF: círculo gris oscuro #424242, sin halo.
- Transición ON→OFF y OFF→ON: ease-out / ease-in, 200 ms.
- En esta pieza: el LED rojo está ON durante toda la operación normal (equipo energizado). Se apaga solo en E6 durante el corte eléctrico. Reaparece primero al retorno de energía.

**LED VERDE:**
- Estado ON: círculo verde #388E3C con halo difuso de 6 px mismo color, opacidad 50 %.
- Estado OFF: círculo gris oscuro #424242, sin halo.
- Transición ON→OFF y OFF→ON: ease-out / ease-in, 200 ms.
- Comportamiento detallado en OR-1 §6.

**Prohibido:** ningún estado intermedio, parpadeo, ni animación de brillo pulsante durante la operación normal ni durante los contadores.

## ASSET 05 — Flechas de flujo en tubería de salida

**Reutilizar de V1 Pozo (ASSET 05).** El trayecto de las flechas se adapta a la geometría de la tubería de salida del tanque (horizontal o diagonal hacia el lateral), no a la tubería de descarga vertical del pozo. La semántica es la misma: activo cuando la bomba está ON, inactivo cuando la bomba está OFF.

- Flechas activas: naranja Exceline (#E8650A), 14 px, bucle continuo.
- Flechas inactivas: fade-out 300 ms → no se animan.

## ASSET 06 — Contador regresivo 10 s

**Reutilizar directamente de V1 Pozo (ASSET 06).** Mismas propiedades tipográficas (Futura Bold 96 pt mínimo, blanco con halo 2 px, sobre fondo circular negro 60 % de radio 60 px) y de animación.

En v2 hay dos instancias del contador en escenas distintas:
- E4 (arranque): contador posicionado sobre la sonda de nivel (sonda sumergida, espera 10 s, bomba ON).
- E5 (corte): contador posicionado sobre la sonda de nivel (sonda sin contacto, espera 10 s, bomba OFF).

Ambas instancias van sobre la misma sonda (la única sonda de nivel de esta aplicación).

## ASSET 07 — Etiqueta de validación "10 s"

**Reutilizar directamente de V1 Pozo (ASSET 07).** Texto "Anti-falsos-positivos: 10 s" / "Confirmación: 10 s" en Futura Bold 28 pt blanco sobre fondo negro 60 %, inmediatamente debajo del ASSET 06. Aparece y desaparece con el contador.

## ASSET 08 — Iconos de corte / retorno de energía

**Reutilizar directamente de V1 Pozo (ASSET 08).** Mismos íconos, mismas propiedades de animación. Aparecen sobre el tablero en E6.

## ASSET 09 — Icono de flecha circular (loop / ciclo)

**Reutilizar directamente de V1 Pozo (ASSET 09).** Solo presente en E6 al cierre de la revalidación (camino A).

## ASSET 10-T — Lower thirds / call-outs de terminales (nuevo — etiquetas v2)

**Descripción:** Mismas reglas visuales que ASSET 10 de V1 Pozo. Solo cambia el contenido de las etiquetas para reflejar la aplicación de tanque con 2 electrodos.

**Reglas visuales:** fondo semitransparente negro 60 %, texto Futura Bold 28 pt blanco (terminal en naranja Exceline), flecha indicadora hacia el elemento. Padding 8 px, esquinas 4 px.

**Lista de instancias necesarias (config. 2 electrodos — DEFINITIVA):**
- "Tanque elevado (residencial / condominio)"
- "Sonda de nivel (T1, T2 puenteado) — punto de operación"
- "Electrodo común / REF (T5) — referencia eléctrica"
- "Suministro externo → flotante mecánico"
- "Bomba a la SALIDA → Hidroneumático / Acometida"
- "GRN-MV → Contactor → Bomba"

**Prohibido:** no usar las etiquetas "MAX", "MIN" ni "Sonda MIN" ni "Sonda MAX" en ningún call-out de esta pieza. Esa terminología corresponde a la aplicación de 2 niveles (V1 Pozo). La terminología correcta para 1 nivel es "Sonda de nivel" y "Electrodo común / REF".

## ASSET 11 — Strip de specs (cierre E7)

**Reutilizar directamente de V1 Pozo (ASSET 11).** Las specs del GRN-MV son idénticas para ambas aplicaciones.

Composición: fondo gris oscuro (#2C2C2C) 90 % opacidad, ancho completo (1080 px en 9:16), alto 80 px. Tres bloques:
- "85 – 305 V~"
- "Sondas hasta 300 m"
- "Salida 3,5 A @ 250 V~"

## ASSET 12 — Render / fotografía de producto

**Reutilizar directamente de V1 Pozo (ASSET 12).** El GRN-MV es el mismo producto. La diferencia está solo en el diagrama de aplicación. No duplicar el render.

---

# OR-3 — SCENE MOTION MAP (v2 Tanque Vaciado)

7 escenas autónomas. Para sincronía de voz en off, referencia a VE-X de Vela cuando se entregue.

---

## E1 — HOOK (8–10 s)

**Elemento central:** fotogramas esquemáticos rápidos del tanque en problema — bomba activa con tanque sin agua + ícono de daño.

| Tiempo | Elemento | Acción | Timing |
|--------|----------|--------|--------|
| 0:00 | Frame completo | Fade-in 200 ms | ease-in-out |
| 0:00–0:03 | Fotograma 1: tanque sin agua, bomba a la salida encendida, ícono de temperatura/calor sobre la bomba | Estático. Esquema técnico, sin producto | — |
| 0:03 | Corte seco | → Fotograma 2 | 0 ms |
| 0:03–0:06 | Fotograma 2: misma bomba, ícono de daño mecánico (burbujas en tubería de salida — cavitación) | Estático | — |
| ~0:02 | Caption "TANQUE VACÍO + BOMBA ENCENDIDA = QUEMADA" | Fade-in 200 ms, fondo semitransparente oscuro | ease-in-out |
| ~0:04 | Caption anterior desaparece → "ARRANQUE SIN AGUA = CAVITACIÓN" | fade-out 300 ms / fade-in 200 ms | ease-in-out |
| ~0:07 | Caption "El GRN-MV lo evita." | Ídem | ease-in-out |

**Diferencia respecto a V1 Pozo:** los dos fotogramas muestran el tanque en sección esquemática (no el pozo). La bomba está en la salida del tanque. El ícono de calor y el ícono de cavitación van sobre la bomba a la salida.

**Ancla visual:** los captions grandes son el ancla en E1. El diagrama de tanque en problema es el contexto visual. No hay producto todavía.

---

## E2 — IDENTIFICACIÓN DEL PRODUCTO (6–7 s)

**Elemento central:** render/fotografía del GRN-MV (ASSET 12). Idéntico a V1 Pozo.

| Tiempo relativo | Elemento | Acción | Timing |
|---------|----------|--------|--------|
| 0:00 | Bumper semántico | Frame negro 100 ms | — |
| +0.10 s | Render de producto | Fade-in 300 ms, centrado | ease-in-out |
| +0.5 s | "GRN-MV" (Handel BT, grande) | Fade-in 200 ms | ease-in-out |
| +0.8 s | "Exceline Profesional" | Fade-in 200 ms | ease-in-out |
| +1.2 s | Logo Exceline Profesional | Fade-in 300 ms | ease-in-out |
| +1.5 s | "Garantiza confianza y duración." | Fade-in 200 ms | ease-in-out |

**Ancla visual:** el render del producto. Los textos orbitan sin tapar el producto.

---

## E3 — DIAGRAMA COMPRIMIDO DE CAMPO (12–15 s)

**Elemento central:** ASSET 01-T (diagrama base del tanque) en estado inicial — nivel sobre la sonda de nivel, ambos electrodos sumergidos, bomba a la salida visible, tablero en el tercio superior.

| Tiempo relativo | Elemento | Acción | Timing |
|---------|----------|--------|--------|
| 0:00 | Bumper semántico | Frame negro 100 ms | — |
| +0.10 s | Diagrama base del tanque completo | Fade-in 300 ms | ease-in-out |
| +1.0 s | Call-out "Tanque elevado (residencial / condominio)" | Fade-in 200 ms | ease-in-out |
| +3.0 s | → "Electrodo común / REF (T5) — referencia eléctrica" | Anterior desaparece (fade-out 300 ms) / nuevo aparece (fade-in 200 ms) — flecha apuntando al electrodo REF en la parte baja del tanque | ease-in-out |
| +5.5 s | → "Sonda de nivel (T1, T2 puenteado) — punto de operación" | Ídem — flecha apuntando a la sonda de nivel | ease-in-out |
| +7.5 s | → "Bomba a la SALIDA → Hidroneumático / Acometida" | Ídem — flecha apuntando a la bomba en la tubería de salida | ease-in-out |
| +9.5 s | → "GRN-MV → Contactor → Bomba" | Ídem — flecha apuntando al tablero | ease-in-out |
| +11.0 s | Caption wiring literal (2 s sobre el diagrama del tablero): "T1 = sonda | T2 → puente a T1 | T5 = electrodo común" | Fade-in 200 ms | ease-in-out |
| +13.0 s | Todos los call-outs salen | Fade-out 300 ms | ease-in-out |

**Ancla visual:** el diagrama completo del tanque. Los call-outs aparecen uno a uno; el diagrama no se mueve.

**Nota:** este diagrama BASE se reutiliza en E4 y E5. El motion designer debe estructurarlo como composición pre-comp en After Effects (o equivalente) para que las capas animables (nivel del agua, LEDs, sonda de nivel) se activen sobre la misma base sin rehacer el diagrama.

---

## E4 — CICLO DE ARRANQUE: SONDA SUMERGIDA → 10 s → BOMBA ON (12–15 s)

**Elemento central:** ASSET 01-T + ASSET 02-T (nivel sobre sonda) + ASSET 06 (contador sobre sonda) + ASSET 04 (LED verde OFF → ON).

**Secuencia de animación — ORDEN ESTRICTO:**

| Paso | Tiempo relativo | Elemento | Acción | Timing |
|------|---------|----------|--------|--------|
| 1 | 0:00 | Diagrama base del tanque (continuación desde E3) | Nivel sobre la sonda de nivel. Ambos electrodos sumergidos (sonda y REF). | Estático |
| 2 | 0:00 | LED verde | Estado OFF (apagado). Confirmado visualmente. | Estático |
| 3 | +0.5 s | Caption "Anti-falsos-positivos: 10 s" (ASSET 07) | Fade-in 200 ms | ease-in-out |
| 4 | +0.5 s | Contador "10" sobre sonda de nivel (ASSET 06) | Fade-in 200 ms, inicia conteo | ease-in-out |
| 5 | +0.5 s a +10.5 s | Contador 10 → 9 → … → 0. LED verde NO cambia durante este período. | Corte directo 1 s/número | — |
| 6 | +10.5 s | Contador "0" | Permanece 200 ms | — |
| 7 | +10.5 s | LED verde: OFF → ON | ease-out 200 ms. SIMULTÁNEO con fin del contador. | ease-out |
| 8 | +10.5 s | ASSET 05 (flechas de flujo en tubería de salida) | Fade-in 300 ms → inicia bucle | ease-out |
| 9 | +10.7 s | Contador y etiqueta "10 s" desaparecen | Fade-out 200 ms | ease-in-out |
| 10 | +11.0 s | Caption "LED VERDE — BOMBA ON" | Fade-in 200 ms | ease-in-out |
| 11 | +11.5 s | Caption "Agua → Red residencial" sobre tubería de salida | Fade-in 200 ms | ease-in-out |
| 12 | +12.0 s | Nivel del agua comienza a descender (inicio de vaciado activo hacia E5) | ease-in, continuo | ease-in |

**Ancla visual:** el contador sobre la sonda de nivel es el ancla temporal. El diagrama del tanque es el ancla de fondo. El LED verde es el ancla de estado.

**Nota para el motion designer:** no hay evento visual intermedio entre "LED verde ON" y el inicio del descenso. El nivel empieza a bajar inmediatamente después del arranque de la bomba; no hay sub-beat separado de "vaciado en curso" como en V1 Pozo. E4 y E5 son continuidad sobre el mismo diagrama base.

---

## E5 — CICLO DE CORTE: SONDA SIN CONTACTO → 10 s → BOMBA OFF (15–18 s)

**Elemento central:** nivel del agua descendiendo hasta perder contacto con la sonda. Contador sobre la sonda. LED verde se apaga.

**Estado de entrada:** continúa directamente desde el descenso iniciado al final de E4. El nivel está bajando; la bomba está ON (LED verde ON, flechas de flujo activas).

**Secuencia de animación — ORDEN ESTRICTO:**

| Paso | Tiempo relativo | Elemento | Acción | Timing |
|------|---------|----------|--------|--------|
| 1 | 0:00 | Nivel del agua descendiendo | Continúa el descenso desde E4. ASSET 05 activo. LED verde ON. | ease-in continuo |
| 2 | ~2–4 s (al perder contacto) | Sonda de nivel: punta sale del agua | Nivel cae bajo la sonda. Punta de la sonda queda fuera del agua. | ease-in continuo |
| 3 | ~2–4 s | Sonda de nivel: estado → "sin contacto" | Destello blanco ease-out 300 ms → color gris #9E9E9E. PRIMER EVENTO. El electrodo REF sigue sumergido (sin cambio visual). | ease-out |
| 4 | +0.5 s post-destello | Contador "10" sobre sonda de nivel (ASSET 06) | Fade-in 200 ms | ease-in-out |
| 5 | +0.5 s post-destello | Caption "Confirmación: 10 s" (ASSET 07) | Fade-in 200 ms | ease-in-out |
| 6 | +0.5 s a +10.5 s post-destello | Contador 10 → 9 → … → 0. LED verde permanece ON durante todo el conteo. ASSET 05 sigue activo. | Corte directo 1 s/número | — |
| 7 | +10.5 s | LED verde: ON → OFF | ease-in 200 ms. SIMULTÁNEO con fin del contador. | ease-in |
| 8 | +10.5 s | ASSET 05 flechas de flujo | Fade-out 300 ms → detenidas. SIMULTÁNEO. | ease-in |
| 9 | +10.7 s | Contador y etiqueta desaparecen | Fade-out 200 ms | ease-in-out |
| 10 | +11.0 s | Caption "LED VERDE — BOMBA OFF" | Fade-in 200 ms, permanece 1.5 s | ease-in-out |
| 11 | +12.0 s | Caption "Protección contra trabajo en vacío." | Fade-in 200 ms | ease-in-out |
| 12 | +12.5 s | Nivel del agua se detiene (fijo entre sonda y REF) | Estático. El tanque no se vacía totalmente. | — |

**Caveats literales on-screen (E5 — obligatorios, 2 s cada uno, sincronizados con la voz):**

| # | Texto literal | Timing | Fuente |
|---|--------------|--------|--------|
| 1 | "Si el líquido está por debajo del electrodo de nivel bajo, el relé no va a permitir el encendido de la bomba." | Aparece sincronizado con la frase "La bomba nunca trabaja con el tanque vacío" | Specs residenciales del KB — wording idéntico en las 3 notas de aplicación |
| 2 | "La bomba sólo podrá ser alimentada si hay líquido en el tanque." | Aparece justo después del caveat 1 (2 s posteriores) | Idem |

**Nota de diagrama (estado final de E5):** el nivel final del agua queda entre la sonda de nivel (sin contacto) y el electrodo REF (aún sumergido). Visualmente: el tanque está casi vacío pero hay un volumen residual mínimo por encima del REF — técnicamente correcto porque la bomba se corta antes de que REF pierda contacto eléctrico.

**Ancla visual:** la sonda de nivel y su pérdida de contacto es el ancla narrativa. El contador es el ancla temporal. El diagrama como ancla de fondo.

---

## E6 — MEMORIA DE ESTADO ANTE CORTE ELÉCTRICO (12–15 s)

**Elemento central:** diagrama base del tanque en estado activo (bomba enviando agua, nivel descendiendo, sonda de nivel aún sumergida, LED rojo ON, LED verde ON). Bifurcación visual explícita al retorno de energía.

**Secuencia de animación — ORDEN ESTRICTO:**

| Paso | Tiempo relativo | Elemento | Acción | Timing |
|------|---------|----------|--------|--------|
| 1 | 0:00 | Estado activo: diagrama completo | ASSET 05 activo. LED rojo ON. LED verde ON. Nivel sobre la sonda de nivel. | Estático |
| 2 | ~2 s | Caption "Corte eléctrico." | Fade-in 200 ms | ease-in-out |
| 3 | ~2.5 s | ÍCONO CORTE (ASSET 08) sobre tablero | Escala 0.5x→1x, ease-out 300 ms | ease-out |
| 4 | ~2.5 s | LED rojo: ON → OFF | ease-in 200 ms | ease-in |
| 5 | ~2.5 s | LED verde: ON → OFF | ease-in 200 ms | ease-in |
| 6 | ~2.5 s | ASSET 05 flechas de flujo | Fade-out 200 ms | ease-in |
| 7 | ~4 s | Pausa visual breve (1–2 s) | Frame gris suave sobre tablero; diagrama quieto | — |
| 8 | ~6 s | ÍCONO CORTE desaparece / ÍCONO RETORNO (ASSET 08) aparece | Fade-out / Escala 0.5x→1x | ease-out |
| 9 | ~6 s | Caption "Retorno de energía." | Fade-in 200 ms | ease-in-out |
| 10 | ~6.2 s | LED rojo: OFF → ON | ease-out 200 ms. PRIMER LED en encenderse. | ease-out |
| 11 | ~7 s | Caption "GRN-MV revalida sonda → operación automática." | Fade-in 200 ms | ease-in-out |
| 12 | ~7.5 s | Sonda de nivel: pulso de revalidación (ASSET 03-T estado revalidación) | Escala 1x→1.15x→1x, ease-in-out, 400 ms, UNA SOLA VEZ. Sin cambio de LED aún. | ease-in-out |

**Bifurcación visual (después del pulso de revalidación):**

El diagrama se divide en dos caminos visuales superpuestos o secuenciales (el motion designer elige la composición más legible; se recomienda mostrar los dos caminos en paralelo dentro del mismo frame, con un divisor visual sutil, en lugar de hacer un corte entre dos frames diferentes):

| Camino | Estado de la sonda al retorno | Acción sobre LED verde | Caption |
|--------|-------------------------------|------------------------|---------|
| Camino A | Nivel sobre la sonda (sonda sumergida) | LED verde: OFF → ON ease-out 200 ms | "LED VERDE — ON / Bomba reanuda" |
| Camino B | Nivel bajo la sonda (sonda sin contacto al retorno) | LED verde permanece apagado | "LED VERDE — OFF / Bomba en espera" |

| Paso | Tiempo relativo | Elemento | Acción | Timing |
|------|---------|----------|--------|--------|
| 13a | ~8.5 s | Camino A — LED verde: OFF → ON | ease-out 200 ms | ease-out |
| 13a | ~8.5 s | Camino A — ASSET 05 flechas | Fade-in 300 ms → inicia bucle | ease-out |
| 13a | ~9.0 s | Camino A — Caption "LED VERDE — ON / Bomba reanuda" | Fade-in 200 ms | ease-in-out |
| 13b | ~8.5 s | Camino B — LED verde permanece apagado | Sin acción | — |
| 13b | ~8.5 s | Camino B — Caption "LED VERDE — OFF / Bomba en espera" | Fade-in 200 ms | ease-in-out |
| 14 | ~10 s | ÍCONO RETORNO desaparece | Fade-out 200 ms | ease-in-out |

**Nota crítica sobre LEDs en E6:** en ningún momento parpadea ningún LED. La secuencia es siempre: apagan juntos → espera → rojo enciende → pulso en sonda → bifurcación A/B. Sin variaciones.

**Nota sobre la bifurcación:** la bifurcación narrativa es el diferenciador de esta pieza respecto al reel de pozo (V1). En el tanque, el corte eléctrico puede coincidir con un ciclo de vaciado activo — cuando la energía regresa, el tanque puede haber terminado de vaciarse, por lo que la revalidación automática de la sonda tiene especial relevancia para proteger la bomba. El camino B es el escenario de mayor valor demostrativo para el instalador.

**Ancla visual:** el tablero con los LEDs es la ancla narrativa de E6. La bifurcación A/B es el elemento diferenciador.

---

## E7 — SPECS Y CIERRE (10–12 s)

**Elemento central:** render de producto (ASSET 12) + ASSET 11 (strip de specs) + logo Exceline. Idéntico a E6 de V1 Pozo.

| Tiempo relativo | Elemento | Acción | Timing |
|---------|----------|--------|--------|
| 0:00 | Render de producto | Fade-in 400 ms sobre fondo neutro | ease-in-out |
| +0.5 s | Logo Exceline Profesional | Fade-in 300 ms | ease-in-out |
| +1.0 s | "GRN-MV" (Handel BT) | Fade-in 200 ms | ease-in-out |
| +2.0 s | ASSET 11 Strip de specs | Entra desde abajo, ease-out 300 ms | ease-out |
| +5.0 s | Strip de specs sale | Fade-out 400 ms | ease-in-out |
| +5.5 s | Web: www.genteca.com.ve / www.exceline.com.mx (según mercado objetivo — pendiente decisión Owner) | Fade-in 200 ms | ease-in-out |
| +6.5 s | "Garantiza confianza y duración." | Fade-in 200 ms | ease-in-out |
| +8.0 s | Todo el frame | Fade-out 400 ms (cierre de pieza) | ease-in-out |

---

# OR-4 — FORMAT ADAPTATION MOTION PLAN (v2 Tanque Vaciado)

## Formato primario: 9:16 — 1080×1920 px (Instagram Reel)

Todas las especificaciones de OR-1, OR-2 y OR-3 corresponden al formato 9:16. Este es el formato master.

**Safe areas (9:16 Instagram Reel):**
- Franja superior reservada: 0–150 px (UI: hora, íconos de señal, barra de progreso).
- Franja inferior reservada: 1770–1920 px (UI: barra de perfil, CTA, descripción de audio).
- Zona central segura: 150 px–1770 px verticalmente; 60 px–1020 px horizontalmente.
- El strip de specs de E7 se posiciona entre px 1650–1770 (margen de 100 px sobre la zona reservada inferior).
- El contador regresivo se posiciona siempre dentro de la zona segura central.
- El logo Exceline en E2 y E7 se posiciona en la zona central superior (px 250–450).

**Nota específica de v2:** el diagrama del tanque es más compacto verticalmente que el pozo de V1. Esto deja más espacio libre en el frame 9:16, especialmente en la parte inferior. El motion designer puede usar ese espacio para posicionar los call-outs de E3 sin superponerlos sobre el diagrama, mejorando la legibilidad. Aprovechar esta ventaja en lugar de comprimir el tanque.

**Nota sobre la bifurcación de E6:** la visualización de dos caminos (A/B) en 9:16 requiere cuidado para no saturar el frame. Recomendación: dividir el frame verticalmente por la mitad con un separador sutil (línea de 1 px, 60 % opacidad) y presentar Camino A en la mitad superior y Camino B en la mitad inferior del diagrama del tanque. Los captions de cada camino van en su respectiva mitad. No intentar mostrar los dos estados del tanque completo uno al lado del otro (no hay ancho suficiente en 9:16). Alternativa aceptable: mostrar primero el camino A completo (2–3 s) y luego el camino B completo (2–3 s) en la misma zona, sin corte de escena.

## Formato secundario: 1:1 — 1080×1080 px (Feed Instagram)

**Estrategia:** usar el rango px 450–1530 del master 9:16 (centro de la acción), igual que V1 Pozo.

**Ajustes específicos:**
- El tanque es más compacto que el pozo; cabe mejor en el cuadrado 1:1 sin recortar elementos críticos. Verificar que el tablero (en el tercio superior) no quede parcialmente fuera del frame.
- Los call-outs de E3 deben reposicionarse hacia el interior del frame si originalmente señalaban hacia los bordes del 9:16.
- El strip de specs en E7 se posiciona entre px 900–980 (zona segura 1:1).
- La bifurcación de E6 en 1:1 se trata igual que en 9:16 (mitad superior/inferior o secuencial).
- Las animaciones son idénticas al master. Sin re-timing.

## Formato terciario: 16:9 — 1920×1080 px (YouTube/web)

**Estrategia:** el tanque se posiciona en el centro-izquierda del frame. El tablero y los call-outs se expanden hacia el lado derecho.

**Ajustes específicos:**
- El tanque en formato horizontal puede mostrarse con más contexto del entorno (ej. la bomba conectada al sistema hidroneumático a la derecha del tanque), mejorando la legibilidad técnica para pantallas de escritorio.
- La bifurcación de E6 en 16:9 tiene espacio para presentar los dos caminos uno al lado del otro (camino A a la izquierda, camino B a la derecha) con el diagrama del tanque repetido. Esta es la versión más legible de la bifurcación; aprovechar el espacio horizontal disponible.
- Call-outs que en 9:16 se superponían sobre el diagrama pueden expandirse hacia el margen derecho.
- El contador regresivo puede reducirse a 72 pt (legible en pantalla 16:9 a distancia normal).
- El strip de specs de E7 mantiene posición inferior (px 950–1030 en 1080 px de alto).
- Sin re-timing de animaciones.

**Nota para Luma:** las adaptaciones 1:1 y 16:9 son re-comps del master 9:16 en After Effects. Los assets compartidos con V1 Pozo (LEDs, contador, flechas de flujo, strip de specs, iconos corte/retorno) deben ser los mismos archivos / instancias exactos en ambos proyectos para garantizar coherencia visual entre los dos reels. No crear versiones paralelas independientes.

---

# OR-5 — HANDOFF BUNDLE PARA LUMA E IVO (v2 Tanque Vaciado)

## Inventario de archivos a entregar al motion designer

| # | Documento | Ruta absoluta | Propósito |
|---|-----------|---------------|-----------|
| 1 | Este motion package completo OR-1 a OR-5 (v2) | `C:\Raul\03-projects\genteca\grn-mv-video\2026-05-12_orfeo-OR_grn-mv-IG-tanque-vaciado_motion-package.md` | Spec master de motion v2 — tanque vaciado |
| 2 | Motion package V1 Pozo — referencia de coherencia y assets compartidos | `C:\Raul\03-projects\genteca\grn-mv-video\2026-05-12_orfeo-OR_grn-mv-IG-pozo-vaciado_motion-package.md` | Sistema compartido; assets reutilizables definidos en V1 |
| 3 | Guion NE-2 v2 (fuente de escenas y captions — AUTORITATIVO) | `C:\Raul\03-projects\genteca\grn-mv-video\2026-05-12_nerea-NE2_grn-mv-IG-tanque-vaciado-short.md` | Copy aprobado, voz en off, captions, caveats literales de E5 |
| 4 | Guion NE-1 v2.2 (referencia rica de intent visual) | `C:\Raul\03-projects\genteca\grn-mv-video\2026-05-11_nerea-NE1_grn-mv-video-script-v2.2.md` | Descripciones visuales detalladas por escena (lógica operativa del GRN-MV) |

**Archivos de brand y assets de producto (requieren entrega separada por Raoul / Genteca):**
- Logo Exceline Profesional (versión positivo/negro, SVG o AI).
- Archivo de código / fuente "Handel BT" (confirmar licencia para uso en video).
- Render o fotografía del GRN-MV sobre fondo blanco/gris (mismo que V1 Pozo; no duplicar).
- Paleta de color oficial Exceline con valores exactos (hex + Pantone si aplica).
- Futura Bold (confirmar licencia para uso en video).

## Resumen ejecutivo para Luma (menor de 200 palabras)

Reel Instagram 9:16 de 75–92 s para el GRN-MV de Exceline Profesional, aplicación vaciado de tanque residencial con bomba a la salida. Hermano del reel V1 Pozo; misma paleta, mismo sistema de LEDs y contadores, misma lógica narrativa, mismos assets animados compartidos.

El diagrama base es nuevo: tanque elevado en sección transversal con 2 electrodos — sonda de nivel única (T1/T2 puenteados) y electrodo común REF (T5) en la parte baja. La bomba está en la tubería de salida, no sumergida.

La pieza tiene 7 escenas autónomas. Las escenas centrales son E4 (arranque: sonda sumergida → contador 10 s → LED verde ON → flechas de flujo) y E5 (corte: sonda sin contacto → contador 10 s → LED verde OFF). No hay sub-beat de vaciado en curso ni zona de histéresis. E6 tiene bifurcación explícita: al retorno de energía, si el nivel bajó durante el corte la bomba queda inhibida; si el nivel es suficiente, reanuda automáticamente. Esta bifurcación es el diferenciador visual de v2 respecto a V1 Pozo.

Los assets ASSET 04 a ASSET 09, ASSET 11 y ASSET 12 son reutilizados de V1 Pozo; solo se construyen ASSET 01-T, 02-T, 03-T y 10-T.

## Decisiones diferidas al motion designer / studio

1. **Composición de la bifurcación en E6 (9:16):** dos opciones aceptables — (a) divisor vertical sutil con camino A arriba y camino B abajo sobre el mismo frame de tanque, o (b) secuencial: mostrar camino A durante 2–3 s y luego camino B durante 2–3 s sin corte de escena. La opción (b) es más legible y más fácil de producir; la opción (a) es más impactante si el motion designer tiene experiencia con divisiones de pantalla. Someter opción al Owner antes de ejecutar.
2. **Estilo de ilustración del diagrama del tanque:** se recomienda vectorial plano técnico (líneas limpias, sin degradados). Si el motion designer propone shading leve para distinguir el tanque del pozo, someter a aprobación de Owner antes de ejecutar.
3. **Render vs fotografía de producto (E2, E7):** mismo asset que V1 Pozo. No duplicar ni producir nueva sesión fotográfica.
4. **Mercado objetivo (web en E7):** pendiente decisión Owner — Venezuela (genteca.com.ve) o México (exceline.com.mx) o ambas URLs. Producir con espacio para las dos opciones.
5. **Locución / VE-X de Vela:** el timing de los captions debe ajustarse a la pista de voz en off una vez producida por Vela. Los timings de OR-3 son estimados desde la voz; el motion designer ajusta contra el audio real.

## Flags de escalación antes de producción

- **Flag 1 — 10 s en spec oficial (brecha BD-1 heredada):** el retardo de 10 s anti-falsos-positivos está confirmado por Owner (Override 2026-05-10) e I&D Genteca verbalmente (2026-05-12) pero NO aparece en HDE V7 RB3 ni en MAN V2 IMP Rev RB3. El uso en E4 y E5 está respaldado por Owner Override. Si este reel se usa como material de spec técnica oficial ante regulador o cliente corporativo, gatear con Bruna antes de publicar. Señalar en créditos internos si aplica.
- **Flag 2 — Mercado objetivo:** sin resolver. Producción debe confirmar qué URL(s) van en E7.
- **Flag 3 — Aprobación de ingeniería Genteca:** pendiente antes de grabar locución (especialmente E4, E5 y la bifurcación de E6 — mayor carga técnica del guion).
- **Flag 4 — Caveats literales de E5:** los dos caveats on-screen ("Si el líquido está por debajo del electrodo de nivel bajo..." y "La bomba sólo podrá ser alimentada si hay líquido en el tanque.") son texto literal de las specs residenciales del KB. No acortar, parafrasear ni animar de forma que reduzca el tiempo de exposición por debajo de 2 s cada uno. Si el ritmo de la pieza lo requiere, dar prioridad al caveat sobre cualquier otro elemento visual simultáneo.
- **Flag 5 — Coherencia visual V1 Pozo / v2 Tanque:** los assets compartidos (ASSET 04 a ASSET 09, ASSET 11, ASSET 12) deben ser los mismos archivos exactos en los dos proyectos de After Effects. No crear versiones paralelas independientes que puedan diverjar visualmente en futuras ediciones.
