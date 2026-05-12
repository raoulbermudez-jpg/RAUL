---
title: "GRN-MV — Video Production Package, Reel IG Vaciado de Tanque (v2)"
type: Video Production Package
agent: Luma
version: v2
replaces: "v1 (3 electrodos — DEPRECATED junto con NE-2 v1 y VE/OR v1)"
product_code: GRN-MV
product_line: Exceline Profesional
aplicacion: "Vaciado de tanque, 1 nivel, bomba a la salida — residencial/condominio (2 electrodos)"
configuracion_terminales: "T1 = sonda de nivel | T2 = puenteado a T1 | T5 = electrodo común (REF) | T7 = voltaje común (NA) | T8 = carga al contactor"
electrodos: 2
formato_master: "9:16 — 1080×1920 px (Instagram Reel)"
duracion_estimada: "75–92 s (1:15–1:32 min)"
audiencia_primaria: Técnico instalador (sistemas residenciales, condominios, hidroneumáticos)
audiencia_secundaria: Administradores de condominio / cliente final
date: 2026-05-12
insumos:
  - "NE-2 v2: 2026-05-12_nerea-NE2_grn-mv-IG-tanque-vaciado-short.md"
  - "VE v2 (Vela): 2026-05-12_vela-VE_grn-mv-IG-tanque-vaciado_voice-package.md"
  - "OR v2 (Orfeo): 2026-05-12_orfeo-OR_grn-mv-IG-tanque-vaciado_motion-package.md"
  - "NE-1 v2.2 (referencia): 2026-05-11_nerea-NE1_grn-mv-video-script-v2.2.md"
  - "Paquete hermano V1 Pozo: 2026-05-12_luma-LU_grn-mv-IG-pozo-vaciado_video-package.md"
contiene: "LU-1 Video Spec | LU-2 Cut List | LU-3 Multi-Format Adaption Plan | LU-4 Caption & On-Screen Text Package | LU-5 Handoff Package"
---

# COVER NOTE — Paquete v2 Vaciado de Tanque

**Campaña / proyecto:** GRN-MV Reel Instagram Serie 2026 — v2 Vaciado de Tanque Residencial  
**Canal:** Instagram Reel (primario) + derivados 1:1 feed y 16:9 YouTube/web  
**Insumos base:** NE-2 v2 (Nerea) + VE v2 paquete completo (Vela) + OR motion package v2 (Orfeo)  
**Duración estimada del master:** 75–92 s (rango confortablemente dentro de <2:00 min IG)  
**Tipo de output:** LU-1 + LU-2 + LU-3 + LU-4 + LU-5

**Defaults Owner aplicados (declarados aquí, no requieren justificación adicional):**
- Mercado VE primario: genteca.com.ve, teléfono Caracas. MX como adaptación posterior por edición.
- Voz masculina neutro latinoamericano 35–45 a, 145–155 wpm, anti-hype.
- Sin música sobre voz; ambient técnico sub-volumen (-20 dB o menor) permitido en escenas sin voz.
- Producto: render existente (fotografía sobre fondo blanco/gris aceptable); no producción de producto real.
- Aprobación final Ingeniería Genteca pendiente antes de grabar locución (gate estándar de cadena).
- 10 s anti-falsos-positivos confirmados verbalmente por I&D Genteca el 2026-05-12; documentación HDE/MAN pendiente de actualización (brecha BD-1 abierta — ver LU-5).

**Nota de versión crítica:** este paquete v2 corresponde al guion NE-2 v2 que usa 2 electrodos (sonda de nivel + electrodo común REF), sin histéresis MAX-MIN. El paquete v1 DEPRECATED (que asumía 3 electrodos con terminología MIN/MAX) fue reemplazado tras confirmarse con 3 specs del KB que la aplicación residencial estándar usa 2 electrodos. No usar material del paquete v1 DEPRECATED.

**Coherencia con V1 Pozo:** misma identidad visual y sonora que el reel de pozo. Misma paleta (#F2F0ED / #FFFFFF fondo, #E8650A naranja Exceline), misma tipografía (Futura Bold, Handel BT), mismos LEDs, mismo contador. Lo que cambia: contenedor físico (tanque elevado vs pozo subterráneo), posición de bomba (salida del tanque vs sumergible en fondo), 2 electrodos en lugar de 3, ausencia de sub-beat de histéresis, bifurcación explícita en E6 (memoria de estado).

**Regla de fidelidad:** todo el voiceover, captions y motion en este paquete proviene literalmente de NE-2 v2, VE v2 y OR v2. Luma no reescribió ni interpretó ningún insumo. Si hay fricción entre insumos, se documenta en LU-5 §Dudas sin modificar la fuente.

**Terminología obligatoria en este paquete:** "sonda de nivel" y "electrodo común" / "electrodo común REF". PROHIBIDO usar "sonda mínima", "sonda máxima", "MIN", "MAX" — esa terminología pertenece a la Aplicación 2 Niveles (V1 Pozo).

---

# LU-1 — VIDEO SPEC POR PIEZA (v2 Vaciado de Tanque)

Documento maestro para editor externo. Integra timing, voiceover literal, captions on-screen, motion notes y cues de audio por escena. El editor abre este documento y produce el reel sin ambigüedad.

**Estructura de escenas:**

| Escena | Beat | Duración absoluta | Acumulado |
|--------|------|--------------------|-----------|
| E1 | Hook — problema: vacío + cavitación | 0:00–0:09 (8–10 s) | 0:09 |
| E2 | Identificación de producto | 0:09–0:16 (6–7 s) | 0:16 |
| E3 | Diagrama de campo comprimido (tanque, 2 electrodos) | 0:16–0:31 (12–15 s) | 0:31 |
| E4 | Arranque: sonda sumergida → 10 s → Bomba ON | 0:31–0:46 (12–15 s) | 0:46 |
| E5 | Corte: sonda sin contacto → 10 s → Bomba OFF | 0:46–1:04 (15–18 s) | 1:04 |
| E6 | Diferenciador: memoria de estado + bifurcación | 1:04–1:19 (12–15 s) | 1:19 |
| E7 | Specs + cierre profesional | 1:19–1:31 (10–12 s) | 1:31 |

**Duración total estimada: 75–92 s.** Editor puede ajustar ±10 % en ritmo de narración y animación.

**Nota de simplificación respecto a V1 Pozo:** no existe sub-beat de vaciado en curso (equivalente al E4B del pozo). La Aplicación 1 Nivel no tiene zona de histéresis narrable; el nivel desciende directamente desde "sonda sumergida" hasta "sonda sin contacto". E4 y E5 son continuidad sobre el mismo diagrama base, igual que los sub-beats del pozo pero sin el intermediario.

---

## E1 — HOOK (0:00–0:09, 8–10 s)

**VISUAL:**
- Fade-in inicial 200 ms en frame 0:00.
- Fotograma 1 (0:00–0:03): tanque elevado en corte esquemático — sin agua; bomba monofásica en la tubería de salida del tanque activa, ícono de temperatura/calor sobre la bomba. Fondo neutro gris (#F2F0ED). Estilo vectorial técnico.
- Corte seco a fotograma 2 (0:03–0:06): misma bomba con ícono de daño mecánico — burbujas en tubería de salida (indicación visual de cavitación).
- Sin producto en esta escena.
- Sin nombrar el GRN-MV todavía.

**DIFERENCIA vs. V1 Pozo:** los fotogramas muestran el tanque en sección esquemática (no el pozo). La bomba está en la salida del tanque (no sumergida). El ícono de calor y el ícono de cavitación van sobre la bomba a la salida.

**ANIMACIÓN:**
- Fade-in inicial de pieza (200 ms, ease-in-out).
- Captions de hook aparecen secuencialmente sincronizados con la voz (ver LU-4).
- Ritmo de corte: cada 3–4 s. Fondo neutro, estilo técnico.

**VOICEOVER (literal de VE-1 v2):**
> "Una **bomba** que sigue corriendo con el tanque **vacío** [.] se quema. [..]
> Una bomba que arranca **sin suficiente agua** [.] puede **cavitar** y dañarse. [..]
> El **GRN-MV** lo evita."

**CAPTIONS ON-SCREEN (sincronizados con voz):**
- Línea 1: "TANQUE VACÍO + BOMBA ENCENDIDA = QUEMADA" — texto grande, 0:00–0:03, fondo semitransparente oscuro.
- Línea 2: "ARRANQUE SIN AGUA = CAVITACIÓN" — al segundo beat (~0:03–0:04); anterior desaparece.
- Línea 3: "El GRN-MV lo evita." — al tercer beat (~0:07); anterior desaparece.

**AUDIO:**
- Sin música de apertura sobre la voz.
- Silencio o ambient técnico suave a -20 dB máximo.
- Archivo de referencia: `GRNMV-TANQUE_E1-hook_SELECTED.wav`

**NOTAS DE EJECUCIÓN (de VE-3 v2):**
- "se quema": peso factual. La brevedad del texto ("se quema") sin "en minutos" requiere que el actor no compense con drama.
- "puede cavitar y dañarse": técnico, no alarmista. El término "cavitar" se pronuncia completo y claro.
- "El GRN-MV lo evita.": declarativo, tres palabras, sin subida de tono al final.
- Diferencia vs. V1 Pozo: el hook de v2 nombra dos vectores de daño (quemado por vacío + cavitación). No dramatizar ninguno.

---

## E2 — IDENTIFICACIÓN DEL PRODUCTO (0:09–0:16, 6–7 s)

**VISUAL:**
- Bumper semántico 100 ms (frame negro) al inicio de E2, en la transición E1→E2.
- Render o fotografía del GRN-MV sobre fondo blanco/gris, centrado en frame 9:16.
- Logo Exceline Profesional con fade-in 300 ms.
- NO usar logo Genteca en este plano.
- Idéntico en composición, tipografía y logo al reel de pozo (V1).

**ANIMACIÓN:**
- Render de producto: fade-in 300 ms.
- "GRN-MV" (Handel BT, tamaño grande): fade-in 200 ms a +0.5 s.
- "Exceline Profesional": fade-in 200 ms a +0.8 s.
- Logo Exceline Profesional: fade-in 300 ms a +1.2 s.
- "Garantiza confianza y duración.": fade-in 200 ms a +1.5 s.
- Asset de referencia: OR-2 ASSET 12 (render de producto — el mismo que V1 Pozo; no duplicar).

**VOICEOVER (literal de VE-1 v2 — texto idéntico a V1 Pozo):**
> "**GRN-MV**. [..] Relé de Nivel para Líquidos Conductores. [.] **Exceline Profesional**."

**CAPTIONS ON-SCREEN:**
- "GRN-MV" — Handel BT, grande (mínimo 48 pt), centrado.
- "Exceline Profesional" — debajo.
- "Garantiza confianza y duración." — eslogan.

**AUDIO:**
- Volumen puede bajar 5–10 % respecto a E1.
- Archivo de referencia: `GRNMV-TANQUE_E2-producto_SELECTED.wav`
- **Nota de eficiencia:** si V1 Pozo y v2 Tanque se graban en la misma sesión, el take de E2 puede ser el mismo para ambas piezas (texto idéntico). Confirmar nivelación y ecualización consistentes antes de reutilizar.

**PRONUNCIACIÓN CRÍTICA:** "GRN-MV" = "ge-ere-ene — eme-uve". Tres beats separados.

---

## E3 — DIAGRAMA DE CAMPO COMPRIMIDO (0:16–0:31, 12–15 s)

**VISUAL:**
- Bumper semántico 100 ms en la transición E2→E3.
- Diagrama vectorial comprimido para 9:16 (ASSET 01-T de Orfeo): tanque elevado en corte transversal.
  - El tanque ocupa 50–60 % del frame vertical (px 450–1700 verticalmente), centrado horizontalmente.
  - Sonda de nivel (T1, T2 puenteado) colgando desde la tapa, en la altura del nivel mínimo operativo — en naranja Exceline.
  - Electrodo común REF (T5) en la parte baja del tanque, siempre sumergido cuando hay agua por encima de la sonda.
  - Bomba monofásica en la tubería de salida (parte inferior lateral del tanque), con tubería hacia red o hidroneumático.
  - Tablero en tercio superior del frame (px 150–500), con cables bajando hacia la tapa del tanque.
  - Nivel del agua en reposo claramente por encima de la sonda de nivel (ambos electrodos sumergidos).
- Diagrama en fade-in 300 ms al inicio.
- Este diagrama BASE se reutiliza en E4 y E5 (pre-comp After Effects).

**ANIMACIÓN:**
- Call-outs secuenciales sincronizados con la voz (OR-3 E3):
  - +1.0 s: "Tanque elevado (residencial / condominio)" — apuntando al tanque
  - +3.0 s: → "Electrodo común / REF (T5) — referencia eléctrica" — apuntando a REF en la parte baja
  - +5.5 s: → "Sonda de nivel (T1, T2 puenteado) — punto de operación" — apuntando a la sonda
  - +7.5 s: → "Bomba a la SALIDA → Hidroneumático / Acometida" — apuntando a la bomba en tubería de salida
  - +9.5 s: → "GRN-MV → Contactor → Bomba" — apuntando al tablero
  - +11.0 s: caption wiring literal (2 s sobre diagrama del tablero): "T1 = sonda | T2 → puente a T1 | T5 = electrodo común"
  - +13.0 s: todos los call-outs salen fade-out 300 ms

**VOICEOVER (literal de VE-1 v2):**
> "El tanque recibe agua de forma externa. [.]
> La **bomba** está a la salida, [.] enviando agua hacia la residencia o el sistema **hidroneumático**. [..]
> (RESPIRA)
> Dentro del tanque: [.] dos electrodos — [.]
> el **electrodo de nivel**, [.] que marca el punto mínimo de operación, [.]
> y el **electrodo común**, [.] siempre en la parte baja. [..]
> El **GRN-MV** está en el tablero, [.] conectado al **contactor** de la bomba."

**CAPTIONS ON-SCREEN:**
- Call-outs secuenciales listados en §ANIMACIÓN arriba.
- Caption wiring: "T1 = sonda | T2 → puente a T1 | T5 = electrodo común" (aparece 2 s sobre diagrama del tablero a +11.0 s).
- Texto Futura Bold 28 pt mínimo, blanco. Valores de terminales en naranja Exceline.

**AUDIO:**
- Ambient técnico sub-volumen permitido.
- Escena de mayor densidad verbal del reel v2 — ritmo 140 wpm. Actor debe pronunciar "hidroneumático", "electrodo de nivel" y "electrodo común" completos; sin atropello.
- Archivo de referencia: `GRNMV-TANQUE_E3-diagrama_SELECTED.wav` (recomendado 4 takes mínimo)

**ALERTA TERMINOLÓGICA:** el actor NO puede decir "sonda mínima", "sonda máxima", "MIN" ni "MAX" en esta escena ni en ninguna escena de este reel. Solo "electrodo de nivel" y "electrodo común".

---

## E4 — CICLO DE ARRANQUE: SONDA SUMERGIDA → 10 s → BOMBA ON (0:31–0:46, 12–15 s)

**VISUAL:**
- Continuación del diagrama base de E3 (sin corte ni bumper entre E3 y E4). Mismo pre-comp.
- Estado de entrada: nivel del agua sobre la sonda de nivel (ambos electrodos — sonda y REF — sumergidos). LED verde APAGADO — confirmar visualmente.
- Al completarse el contador: LED verde enciende (ease-out 200 ms). Flechas de flujo en tubería de salida inician (ASSET 05, naranja Exceline, bucle continuo).
- Nivel del agua comienza a descender inmediatamente después del arranque (inicio del vaciado activo hacia E5).

**ANIMACIÓN — ORDEN ESTRICTO (OR-3 E4):**
- Paso 1 (0:00): diagrama estático. Nivel sobre sonda. LED verde OFF confirmado.
- Paso 2 (+0.5 s): etiqueta "Anti-falsos-positivos: 10 s" (ASSET 07) — fade-in 200 ms.
- Paso 3 (+0.5 s): contador "10" sobre sonda de nivel (ASSET 06, Futura Bold 96 pt min., fondo circular negro 60 %) — fade-in 200 ms.
- Paso 4 (+0.5 s a +10.5 s): contador 10→9→8→...→0 (corte directo, 1 s/número, sin tick). LED verde NO cambia durante el conteo.
- Paso 5 (+10.5 s): "0" permanece 200 ms → LED verde OFF→ON (ease-out 200 ms) SIMULTÁNEO con fin del contador.
- Paso 6 (+10.5 s): ASSET 05 flechas de flujo en tubería de salida — fade-in 300 ms → inicia bucle.
- Paso 7 (+10.7 s): contador y etiqueta desaparecen (fade-out 200 ms).
- Paso 8 (+11.0 s): caption "LED VERDE — BOMBA ON" — fade-in 200 ms.
- Paso 9 (+11.5 s): caption "Agua → Red residencial" sobre tubería de salida — fade-in 200 ms.
- Paso 10 (+12.0 s): nivel del agua comienza a descender (inicio de vaciado activo, continúa en E5).

**Nota para el motion designer:** no hay evento visual intermedio entre "LED verde ON" y el inicio del descenso. El nivel empieza a bajar inmediatamente. E4 y E5 son continuidad sobre el mismo diagrama base.

**VOICEOVER (literal de VE-1 v2 — esquema de micro-bloques):**

*Micro-bloque E4-pre (~5–6 s):*
> "El tanque tiene agua. [.]
> La **sonda de nivel** está **sumergida**. [..]
> El **GRN-MV** espera **diez segundos** [.] para descartar falsas lecturas."

→ *Silencio VO (~4–5 s): contador corre de ~7 a 0. B-roll visual silencioso.*

*Micro-bloque E4-post (~3–4 s):*
> "(RESPIRA) Transcurrido ese retardo, [.] **activa la bomba**. [.]
> **LED verde** encendido: [.] la bomba envía agua hacia la residencia."

**Archivos fuente de audio (dos takes separados):**
- `GRNMV-TANQUE_E4-arranque-pre_SELECTED.wav`
- `GRNMV-TANQUE_E4-arranque-post_SELECTED.wav`

**CAPTIONS ON-SCREEN:**
- Contador regresivo "10…9…8…→0" visible sobre la sonda de nivel durante el conteo.
- "Anti-falsos-positivos: 10 s" — debajo del contador.
- Al llegar a 0: "LED VERDE — BOMBA ON".
- "Agua → Red residencial" — sobre tubería de salida.

**AUDIO:**
- "sonda de nivel": usar siempre esta denominación; nunca "sonda máxima" ni "sonda mínima".
- "diez segundos": articular completo. Claim técnico diferenciador.
- "para descartar falsas lecturas": texto literal del guion v2 (distinto a "turbulencia o salpicaduras" de V1 Pozo — respetar diferencia).
- "LED verde encendido:": confirmación, no entusiasmo. Los dos puntos orales significan que viene un estado consecuente.

---

## E5 — CICLO DE CORTE: SONDA SIN CONTACTO → 10 s → BOMBA OFF (0:46–1:04, 15–18 s)

**VISUAL:**
- Continuación del mismo diagrama base. Sin corte ni bumper entre E4 y E5.
- Estado de entrada: continúa directamente desde el descenso iniciado al final de E4. El nivel está bajando; la bomba está ON (LED verde ON, flechas de flujo activas).
- El nivel desciende hasta quedar por debajo de la sonda de nivel.
- El electrodo REF sigue sumergido (sin cambio visual) — refuerza que hay agua residual y que el circuito tiene referencia eléctrica.
- Al completarse el contador: LED verde ON→OFF. Flechas de flujo se detienen.
- Estado final: nivel del agua fijo entre la sonda (sin contacto) y el electrodo REF (aún sumergido). El tanque está casi vacío pero hay un volumen residual mínimo por encima del REF.

**ANIMACIÓN — ORDEN ESTRICTO (OR-3 E5):**
- Paso 1 (0:00): nivel del agua descendiendo. ASSET 05 activo. LED verde ON.
- Paso 2 (~2–4 s al perder contacto): nivel cae bajo la sonda. Punta de la sonda queda fuera del agua.
- Paso 3 (~2–4 s): sonda de nivel → "sin contacto": destello blanco ease-out 300 ms → color gris #9E9E9E. PRIMER EVENTO. REF sigue sumergida, sin cambio.
- Paso 4 (+0.5 s post-destello): contador "10" sobre sonda de nivel (ASSET 06) — fade-in 200 ms.
- Paso 5 (+0.5 s): caption "Confirmación: 10 s" (ASSET 07) — fade-in 200 ms.
- Paso 6 (+0.5 s a +10.5 s): contador 10→0. LED verde permanece ON. ASSET 05 sigue activo.
- Paso 7 (+10.5 s): LED verde ON→OFF (ease-in 200 ms). SIMULTÁNEO con fin del contador.
- Paso 8 (+10.5 s): ASSET 05 flechas fade-out 300 ms → detenidas.
- Paso 9 (+10.7 s): contador y etiqueta desaparecen (fade-out 200 ms).
- Paso 10 (+11.0 s): "LED VERDE — BOMBA OFF" — fade-in 200 ms, permanece 1.5 s.
- Paso 11 (+12.0 s): "Protección contra trabajo en vacío." — fade-in 200 ms.
- Paso 12 (+12.5 s): nivel del agua se detiene (fijo entre sonda y REF).
- **CAVEATS LITERALES OBLIGATORIOS (post-VO, visuales puros):**
  - Caveat 1 aparece sincronizado con "La bomba nunca trabaja con el tanque vacío": "Si el líquido está por debajo del electrodo de nivel bajo, el relé no va a permitir el encendido de la bomba." — permanece 2 s.
  - Caveat 2 aparece inmediatamente después: "La bomba sólo podrá ser alimentada si hay líquido en el tanque." — permanece 2 s.

**VOICEOVER (literal de VE-1 v2 — micro-bloques):**

*Micro-bloque E5-pre (~5–6 s):*
> "El nivel del tanque baja. [.]
> Cuando cae **por debajo** de la **sonda de nivel**, [.] el electrodo pierde contacto con el agua. [..]
> El **GRN-MV** espera nuevamente **diez segundos** para confirmar."

→ *Silencio VO (~4–5 s): contador corre de ~7 a 0. B-roll visual silencioso.*

*Micro-bloque E5-post (~4–5 s):*
> "(RESPIRA) Luego **corta la bomba**. [...]
> La bomba **nunca trabaja** con el tanque **vacío**."

→ *B-roll silencioso post-VO (~4 s): caveats literales on-screen aparecen solos.*

**Archivos fuente de audio (dos takes separados):**
- `GRNMV-TANQUE_E5-corte-pre_SELECTED.wav`
- `GRNMV-TANQUE_E5-corte-post_SELECTED.wav`

**CAPTIONS ON-SCREEN:**
- Destello en punta de sonda de nivel al perder contacto.
- Contador "10…→0" sobre sonda de nivel.
- "Confirmación: 10 s".
- "LED VERDE — BOMBA OFF" al llegar a 0.
- "Protección contra trabajo en vacío."
- **Caveat literal 1 (obligatorio — texto literal del KB):** "Si el líquido está por debajo del electrodo de nivel bajo, el relé no va a permitir el encendido de la bomba." — 2 s de exposición mínima. NO acortar ni parafrasear.
- **Caveat literal 2 (obligatorio — texto literal del KB):** "La bomba sólo podrá ser alimentada si hay líquido en el tanque." — 2 s de exposición mínima inmediatamente posterior al caveat 1. NO acortar ni parafrasear.

**REGLA DE CAVEATS:** los dos caveats son texto literal de las 3 notas de aplicación del KB y deben aparecer exactamente como están escritos. Si el ritmo de la pieza requiere ajuste, dar prioridad a los caveats sobre cualquier otro elemento visual simultáneo.

**AUDIO:**
- "por debajo de la sonda de nivel": articular sin comprimir.
- "espera nuevamente diez segundos": "nuevamente" lleva el peso de simetría del sistema.
- Pausa larga `[...]` antes de "La bomba nunca trabaja con el tanque vacío" — setup del argumento de protección.
- Los caveats on-screen aparecen DESPUÉS de que la voz termina E5 — el actor no los lee en voz.

---

## E6 — DIFERENCIADOR: MEMORIA DE ESTADO (1:04–1:19, 12–15 s)

**VISUAL:**
- Corte seco al entrar a E6. El diagrama base del tanque (pre-comp) persiste.
- Estado de entrada: bomba enviando agua, ambos LEDs encendidos, nivel sobre la sonda de nivel.
- Secuencia: corte eléctrico → LEDs se apagan → espera → retorno → LED rojo primero → pulso en sonda → bifurcación A/B.
- **Bifurcación visual explícita (diferenciador de v2 vs V1 Pozo):**
  - Camino A (nivel sobre sonda al retorno): LED verde enciende → bomba reanuda.
  - Camino B (nivel bajo sonda al retorno): LED verde permanece apagado → bomba en espera.

**ANIMACIÓN — ORDEN ESTRICTO (OR-3 E6):**
- Paso 1 (0:00): estado activo. ASSET 05 activo. LED rojo ON. LED verde ON.
- Paso 2 (~2 s): caption "Corte eléctrico." — fade-in 200 ms.
- Paso 3 (~2.5 s): ícono corte (ASSET 08) sobre tablero — escala 0.5x→1x, ease-out 300 ms.
- Paso 4 (~2.5 s): LED rojo ON→OFF (ease-in 200 ms). LED verde ON→OFF (ease-in 200 ms). ASSET 05 fade-out 200 ms. SIMULTÁNEOS.
- Paso 5 (~4 s): pausa visual breve (1–2 s). Frame gris suave sobre tablero.
- Paso 6 (~6 s): ícono corte desaparece. Ícono retorno (ASSET 08) aparece — escala 0.5x→1x, ease-out.
- Paso 7 (~6 s): caption "Retorno de energía." — fade-in 200 ms.
- Paso 8 (~6.2 s): LED rojo OFF→ON — ease-out 200 ms. PRIMER LED.
- Paso 9 (~7 s): caption "GRN-MV revalida sonda → operación automática." — fade-in 200 ms.
- Paso 10 (~7.5 s): sonda de nivel — pulso de revalidación (ASSET 03-T): escala 1x→1.15x→1x, ease-in-out, 400 ms, UNA SOLA VEZ. Sin cambio de LED durante el pulso.
- **Bifurcación A/B (pasos 11a/11b — simultáneos pero en distintos "caminos" visuales):**
  - Paso 11a (~8.5 s): Camino A — LED verde OFF→ON (ease-out 200 ms). ASSET 05 flechas fade-in 300 ms. Caption "LED VERDE — ON / Bomba reanuda" (fade-in 200 ms, a ~9.0 s).
  - Paso 11b (~8.5 s): Camino B — LED verde permanece apagado. Caption "LED VERDE — OFF / Bomba en espera" (fade-in 200 ms).
- Paso 12 (~10 s): ícono retorno desaparece — fade-out 200 ms.

**NOTA SOBRE LA BIFURCACIÓN (decisión diferida al motion designer):** dos opciones aceptables: (a) divisor vertical sutil con Camino A en mitad superior y Camino B en mitad inferior del frame, o (b) mostrar Camino A durante 2–3 s y luego Camino B durante 2–3 s en la misma zona, sin corte de escena. Opción (b) es más legible y más fácil de producir. Opción (a) es más impactante. Someter al Owner antes de ejecutar.

**REGLA CRÍTICA DE LEDs:** ningún LED parpadea en ningún momento de E6. Secuencia siempre lineal: apagan juntos → espera → rojo enciende → pulso en sonda → bifurcación A/B. Sin variaciones.

**VOICEOVER (literal de VE-1 v2):**
> "**Corte de luz**: [..] el **GRN-MV** memoriza el estado de su salida. [..]
> (RESPIRA)
> Al retornar la energía, [.] **revalida** la sonda [.]
> y reanuda la operación **automáticamente**. [..]
> Si el nivel cayó durante el corte, [.] la bomba queda **apagada** [.] hasta que haya nivel suficiente."

**Archivo de referencia audio:** `GRNMV-TANQUE_E6-memoria_SELECTED.wav`

**CAPTIONS ON-SCREEN:**
- "Corte eléctrico." — con ícono sobre tablero.
- LEDs apagados.
- "Retorno de energía." — con ícono de retorno.
- "GRN-MV revalida sonda → operación automática."
- Camino A: "LED VERDE — ON / Bomba reanuda"
- Camino B: "LED VERDE — OFF / Bomba en espera"

**AUDIO:**
- "revalida": término técnico preciso, no suavizar.
- "automáticamente": lleva el beneficio. Énfasis moderado.
- "Si el nivel cayó durante el corte...": frase condicional real; el "si" no es retórico. Tono condicional con pausa después de "corte".
- La voz narra solo el camino B porque es el diferenciador; el camino A es el comportamiento normal ya explicado en E4. El visual hace el trabajo de mostrar ambos caminos.

---

## E7 — SPECS Y CIERRE (1:19–1:31, 10–12 s)

**VISUAL:**
- Corte seco desde E6. Render de producto centrado en 9:16 (ASSET 12) con fade-in 400 ms sobre fondo neutro.
- Logo Exceline Profesional: fade-in 300 ms a +0.5 s.
- "GRN-MV" (Handel BT): fade-in 200 ms a +1.0 s.
- Strip de specs (ASSET 11): entra desde abajo ease-out 300 ms a +2.0 s; permanece 3 s; sale fade-out 400 ms a +5.0 s.
  - Bloque 1: "85 – 305 V~" | Bloque 2: "Sondas hasta 300 m" | Bloque 3: "Salida 3,5 A @ 250 V~"
  - Valores numéricos en naranja Exceline; unidades en blanco. Futura Bold 28 pt.
- Web: www.genteca.com.ve — fade-in 200 ms a +5.5 s. (La voz NO lee la web; visual solamente.)
- "Garantiza confianza y duración." — fade-in 200 ms a +6.5 s.
- Fade-out 400 ms (cierre de pieza) a +8.0 s.
- Idéntico en composición al cierre del reel de pozo (V1).

**VOICEOVER (literal de VE-1 v2):**
> "Opera en redes de **ochenta y cinco** a **trescientos cinco voltios**. [.]
> Sondas hasta **trescientos metros** del tablero. [..]
> Consulte el manual [.] o comuníquese con su **distribuidor autorizado**."

**[CORTE LIMPIO]** al final de "distribuidor autorizado". El visual con web y logo cierra en silencio.

**Archivo de referencia audio:** `GRNMV-TANQUE_E7-cierre_SELECTED.wav`

**CAPTIONS ON-SCREEN:**
- Strip de specs (ASSET 11): "85 – 305 V~" | "Sondas hasta 300 m" | "Salida 3,5 A @ 250 V~"
- Web: www.genteca.com.ve (visual solamente; voz no la lee)
- Logo Exceline Profesional centrado.
- "GRN-MV" en Handel BT.
- "Garantiza confianza y duración."

**AUDIO:**
- Valores de voltaje y distancia leídos completos, despacio.
- "85 a 305 voltios" → "ochenta y cinco a trescientos cinco voltios".
- "300 metros" → "trescientos metros".
- "Consulte el manual" → tono genuino, no legal-obligatorio.
- Corte limpio en post; no se escucha el exhale final.

---

# LU-2 — CUT LIST / EDICIÓN BASE (v2 Vaciado de Tanque)

## Línea de tiempo maestra 9:16

| TC Inicio | TC Fin | Dur. | Track Video | Track Animación | Track Audio (VO) | Track Captions | Transición entrada |
|-----------|--------|------|-------------|-----------------|------------------|----------------|--------------------|
| 0:00.0 | 0:00.2 | 0.2 s | — | Fade-in 200 ms (pieza) | — | — | Fade-in 200 ms |
| 0:00 | 0:03 | 3 s | E1 Fotograma 1: tanque sin agua, bomba a la salida activa, ícono calor | Estático | VO E1 (continuo) | Caption L1 "TANQUE VACÍO + BOMBA ENCENDIDA = QUEMADA" | — |
| 0:03 | 0:06 | 3 s | E1 Fotograma 2: bomba con ícono cavitación (burbujas) | Estático | VO E1 (continuo) | Caption L2 "ARRANQUE SIN AGUA = CAVITACIÓN" | Corte seco |
| 0:06 | 0:09 | 3 s | E1 Fotograma 2 (continúa) | — | VO E1 (continuo) | Caption L3 "El GRN-MV lo evita." | — |
| 0:09 | 0:09.1 | 0.1 s | — | Bumper negro 100 ms | — | — | Bumper semántico |
| 0:09 | 0:16 | 7 s | E2 Render GRN-MV sobre fondo blanco/gris | Fade-in producto → texto → logo → eslogan (OR-3 E2) | VO E2 | "GRN-MV" / "Exceline Profesional" / "Garantiza confianza y duración." | Corte tras bumper |
| 0:16 | 0:16.1 | 0.1 s | — | Bumper negro 100 ms | — | — | Bumper semántico |
| 0:16 | 0:31 | 15 s | E3 Diagrama de tanque (ASSET 01-T, estado inicial: nivel sobre sonda) | Call-outs secuenciales + caption wiring (OR-3 E3) | VO E3 | Call-outs: Tanque / REF / Sonda nivel / Bomba salida / GRN-MV→Contactor + wiring T1/T2/T5 | Corte tras bumper |
| 0:31 | 0:46 | 15 s | E4 (continuación E3) Diagrama con nivel sobre sonda → contador → LED ON | Contador 10→0 sobre sonda + LED verde OFF→ON + flechas ON + nivel comienza a descender (OR-3 E4) | VO E4 (micro-bloques pre + silencio + post) | "Anti-falsos-positivos 10 s" / Contador / "LED VERDE — BOMBA ON" / "Agua → Red residencial" | Continuidad (sin corte) |
| 0:46 | 1:04 | 18 s | E5 (continuación) Nivel cae bajo sonda → contador → LED OFF + caveats on-screen | Destello sonda sin contacto + contador 10→0 + LED verde ON→OFF + flechas OFF + caveats literales (OR-3 E5) | VO E5 (micro-bloques pre + silencio + post) + B-roll silencioso post-VO para caveats | "Confirmación 10 s" / Contador / "LED VERDE — BOMBA OFF" / "Protección contra trabajo en vacío." / Caveat 1 / Caveat 2 | Continuidad |
| 1:04 | 1:19 | 15 s | E6 Diagrama estado activo → corte eléctrico → retorno → pulso sonda → bifurcación A/B | LEDs apagan / ícono corte / ícono retorno / LED rojo / pulso sonda nivel / bifurcación A/B (OR-3 E6) | VO E6 | "Corte eléctrico." / "Retorno de energía." / "GRN-MV revalida sonda → operación automática." / Camino A / Camino B | Corte seco |
| 1:19 | 1:31 | 12 s | E7 Render producto fondo neutro | Fade-in render → logo → nombre → strip specs → web → eslogan → fade-out cierre | VO E7 + [CORTE LIMPIO] | Strip specs "85–305 V~" / web genteca.com.ve / "Garantiza confianza y duración." | Corte seco |
| 1:31 | 1:31.4 | 0.4 s | — | Fade-out 400 ms (cierre de pieza) | — | — | Fade-out 400 ms |

**Duración total estimada: 75–92 s.**

---

## Tabla de marcadores de transición

| TC | Tipo de transición | Justificación |
|----|-------------------|---------------|
| 0:00 | Fade-in 200 ms | Apertura de pieza |
| 0:09 | Bumper negro 100 ms | Hook → Producto (transición narrativa de mayor peso) |
| 0:16 | Bumper negro 100 ms | Producto → Diagrama técnico (segunda transición de peso) |
| 0:31 | Continuidad sobre diagrama | E3→E4 (mismo diagrama base del tanque, sin corte) |
| 0:46 | Continuidad sobre diagrama | E4→E5 (el nivel continúa descendiendo sin corte) |
| 1:04 | Corte seco | E5→E6 (cambio de contexto narrativo — inicia diferenciador) |
| 1:19 | Corte seco | E6→E7 (corte a cierre visual) |
| 1:31 | Fade-out 400 ms | Cierre de pieza |

---

## Tabla resumen final

| Parámetro | Valor |
|-----------|-------|
| Duración total estimada | 75–92 s (1:15–1:32 min) |
| Margen bajo límite IG (2:00 min) | 28–45 s |
| Escenas | 7 (E1, E2, E3, E4, E5, E6, E7) |
| Bumpers semánticos | 2 (E1→E2, E2→E3) |
| Segmentos de continuidad | 2 (E3→E4→E5) |
| Escenas con contador regresivo | 2 (E4, E5) |
| B-roll silencioso de VO (counters) | ~4–5 s × 2 = ~8–10 s |
| B-roll silencioso post-VO (caveats E5) | ~4 s (2 s + 2 s para los dos caveats) |
| Archivos VO | 7 takes seleccionados (9 con micro-bloques pre/post de E4 y E5) |
| Ajuste editorial disponible | ±10 % en ritmo de narración y animación |

---

## Puntos de decisión editorial

1. **Sincronía de counters (E4 y E5):** misma operación crítica que en V1 Pozo pero sobre una sola sonda (la sonda de nivel). "activa la bomba" en E4 y "Luego corta la bomba" en E5 deben alinearse con el frame "0" del contador y el cambio de estado del LED.

2. **Caveats literales de E5:** los dos caveats on-screen deben permanecer en pantalla 2 s cada uno y no pueden solaparse con la pista de voz. El editor debe confirmar que la pista de VO termina antes de que comiencen los caveats.

3. **Bifurcación de E6:** el motion designer presenta la propuesta de composición (opción a — divisor vertical / opción b — secuencial) al Owner antes de ejecutar. El editor no puede proceder con E6 hasta que el Owner apruebe la opción.

4. **Mercado objetivo en E7:** misma situación que V1 Pozo. Producir con espacio para www.genteca.com.ve y www.exceline.com.mx; la actualización es una operación de texto en capa de captions.

5. **Reutilización del take de E2:** si el take de E2 de V1 Pozo se reutiliza en esta pieza, el editor debe confirmar que los niveles de audio son consistentes entre los dos reels antes de aceptar la reutilización.

---

# LU-3 — MULTI-FORMAT ADAPTION PLAN (v2 Vaciado de Tanque)

## Estrategia general

Idéntica al reel de pozo (V1): producir el master 9:16 una sola vez; los formatos 1:1 y 16:9 se derivan como re-comps del mismo proyecto After Effects. Los assets compartidos con V1 Pozo (ASSET 04 a ASSET 09, ASSET 11, ASSET 12) deben ser los mismos archivos exactos en ambos proyectos — no crear versiones paralelas independientes.

---

## Formato Master: 9:16 — 1080×1920 px (Instagram Reels)

**Safe areas (9:16 Instagram Reel):** idénticas al reel de pozo.

| Zona | Rango vertical | Rango horizontal | Descripción |
|------|---------------|------------------|-------------|
| Reservada superior | 0–150 px | Todo el ancho | UI Instagram: hora, señal, barra de progreso. Sin elementos críticos. |
| Segura de contenido | 150–1770 px | 60–1020 px | Zona activa principal. |
| Segura inferior (strip specs) | 1650–1770 px | Todo el ancho | Strip de specs E7 con margen de 100 px. |
| Reservada inferior | 1770–1920 px | Todo el ancho | UI Instagram. Sin elementos críticos. |

**Posicionamiento de elementos clave en 9:16:**
- Diagrama del tanque: px 450–1700 verticalmente, centrado horizontalmente. Más compacto que el pozo; deja más espacio libre en la parte inferior del frame para call-outs sin superposición.
- Tablero: px 150–500 verticalmente, con cables bajando hacia la tapa del tanque.
- Contador regresivo: centrado sobre la sonda de nivel, dentro de la zona segura de contenido.
- Logo Exceline (E2, E7): px 250–450 verticalmente.
- Strip de specs (E7): px 1650–1770 verticalmente.

**Nota específica de v2:** el diagrama del tanque es más compacto verticalmente que el pozo de V1. Esto deja más espacio libre en el frame 9:16, especialmente en la parte inferior. Aprovechar ese espacio para posicionar los call-outs de E3 sin superponerlos sobre el diagrama, mejorando la legibilidad.

---

## Derivado 1: 1:1 — 1080×1080 px (Instagram Feed Cuadrado)

**Estrategia:** usar el rango px 450–1530 del master 9:16.

**Ajustes específicos por escena:**

| Escena | Ajuste en 1:1 |
|--------|--------------|
| E1 Hook | Los captions grandes son el ancla; el tanque esquemático debe caber en el cuadrado. Verificar que la bomba a la salida sea visible. |
| E2 Producto | Render centrado funciona bien en 1:1 sin modificaciones. |
| E3 Diagrama | El tanque es más compacto que el pozo; cabe mejor en 1:1. Verificar que el tablero (tercio superior) no quede parcialmente fuera. Reposicionar call-outs que señalen hacia bordes del 9:16. |
| E4, E5 | Verificar que la sonda de nivel, el electrodo REF y el tablero quepan dentro del cuadrado. El contador sobre la sonda debe quedar dentro de la zona segura. |
| E5 — caveats | Los dos caveats literales deben ser legibles en 1:1. Si el texto es muy largo para la caja de captions en 1:1, escalar el tamaño del fondo del caption pero NO acortar el texto. |
| E6 Bifurcación | La bifurcación en 1:1 se trata igual que en 9:16 (mitad superior/inferior o secuencial). |
| E7 Cierre | Strip de specs: px 900–980. Render del producto centrado sin modificación. |

**Safe areas (1:1):**
- Zona reservada inferior: px 980–1080.
- Strip de specs: px 900–980.

---

## Derivado 2: 16:9 — 1920×1080 px (YouTube / Web)

**Estrategia:** el tanque se posiciona en el centro-izquierda del frame. El tablero y los call-outs se expanden hacia el lado derecho.

**Ajustes específicos:**

| Elemento | Ajuste en 16:9 |
|----------|---------------|
| Tanque | Centro-izquierda (~55 % del ancho). |
| Tablero | Tercio derecho del frame. |
| Call-outs E3 | Pueden expandirse hacia el margen derecho con líneas de referencia más largas. El tanque tiene menos elementos que el pozo; el diagrama en 16:9 puede mostrar más contexto del entorno (sistema hidroneumático, red residencial). |
| Bifurcación E6 | En 16:9 hay espacio para presentar los dos caminos uno al lado del otro (Camino A a la izquierda, Camino B a la derecha) con el diagrama del tanque repetido. Esta es la versión más legible de la bifurcación; aprovechar el espacio horizontal. |
| Caveats E5 | En 16:9 los caveats pueden mostrarse como texto más expandido con mayor tiempo de exposición, mejorando la accesibilidad. |
| Contador | Reducir a 72 pt (legible en pantalla 16:9). |
| Strip de specs | Posición inferior: px 950–1030. |

**Safe areas (16:9):**
- Zona segura general: 5 % de margen en todos los bordes.
- Zona de contenido activo: 192–1728 px horizontalmente; 96–984 px verticalmente.

---

## Tabla resumen de adaptaciones

| Formato | Resolución | Canal | Estrategia | Re-timing | Captions quemados |
|---------|-----------|-------|-----------|-----------|-------------------|
| 9:16 (master) | 1080×1920 px | Instagram Reels | Master original | — | Sí (audio-off por defecto) |
| 1:1 (derivado) | 1080×1080 px | Instagram Feed | Re-comp, recorte vertical px 450–1530 | No | Sí |
| 16:9 (derivado) | 1920×1080 px | YouTube / web | Re-comp, expansión lateral, reposicionamiento + bifurcación E6 lado a lado | No | Opcional + .srt |

---

# LU-4 — CAPTION & ON-SCREEN TEXT PACKAGE (v2 Vaciado de Tanque)

## Especificaciones tipográficas

Idénticas al paquete V1 Pozo:

| Parámetro | Valor |
|-----------|-------|
| Fuente principal (call-outs y captions) | Futura Bold |
| Tamaño mínimo en 9:16 | 28 pt |
| Fuente producto/nombre | Handel BT |
| Color base texto | Blanco (#FFFFFF) |
| Color énfasis (producto, valores numéricos, specs) | Naranja Exceline (#E8650A — confirmar con brand wiki) |
| Fondo captions | Negro 60 % opacidad, padding 8 px, esquinas redondeadas 4 px |
| Posición por defecto | Zona segura central, no superponer sobre sonda de nivel ni LEDs del tablero |

**Terminología obligatoria:** "Sonda de nivel" (no "MIN" ni "MAX") y "Electrodo común / REF" (no solo "REF"). La terminología de 2 niveles está reservada para V1 Pozo.

---

## Captions literales por escena

### E1 — HOOK (0:00–0:09)

| Línea | Texto | Timing aprox. | Sincronía con VO |
|-------|-------|--------------|-----------------|
| L1 | TANQUE VACÍO + BOMBA ENCENDIDA = QUEMADA | 0:00 entrada, 0:03 salida | Al inicio del primer beat |
| L2 | ARRANQUE SIN AGUA = CAVITACIÓN | ~0:03 entrada, ~0:07 salida | "Una bomba que arranca sin suficiente agua..." |
| L3 | El GRN-MV lo evita. | ~0:07 entrada, 0:09 salida | "El GRN-MV lo evita." |

*Tipografía:* Futura Bold, mínimo 40 pt en 9:16, fondo semitransparente oscuro.

---

### E2 — IDENTIFICACIÓN DEL PRODUCTO (0:09–0:16)

| Elemento | Texto | Tipografía | Posición |
|----------|-------|-----------|---------|
| Nombre | GRN-MV | Handel BT, grande (mínimo 48 pt) | Centrado en frame |
| Línea | Exceline Profesional | Futura Bold 28 pt | Debajo del nombre |
| Eslogan | Garantiza confianza y duración. | Futura Regular 24 pt | Debajo de "Exceline Profesional" |

---

### E3 — DIAGRAMA DE CAMPO (0:16–0:31)

| Call-out | Texto | Timing aprox. | Elemento señalado |
|----------|-------|--------------|-------------------|
| CO-1 | Tanque elevado (residencial / condominio) | ~0:17 entrada / ~0:19 salida | Cuerpo del tanque |
| CO-2 | Electrodo común / REF (T5) — referencia eléctrica | ~0:19 entrada / ~0:21 salida | Punta del electrodo REF en parte baja |
| CO-3 | Sonda de nivel (T1, T2 puenteado) — punto de operación | ~0:21 entrada / ~0:23 salida | Punta de la sonda de nivel |
| CO-4 | Bomba a la SALIDA → Hidroneumático / Acometida | ~0:23 entrada / ~0:25 salida | Bomba en tubería de salida |
| CO-5 | GRN-MV → Contactor → Bomba | ~0:25 entrada / ~0:27 salida | Tablero |
| CO-6 (wiring) | T1 = sonda \| T2 → puente a T1 \| T5 = electrodo común | ~0:27, permanece 2 s | Sobre diagrama del tablero |

*Nota:* los tiempos exactos se ajustan contra el audio real. El editor sincroniza cada call-out con la palabra correspondiente en VE-1 E3.

---

### E4 — ARRANQUE: SONDA SUMERGIDA → BOMBA ON (0:31–0:46)

| Caption | Texto | Timing | Notas |
|---------|-------|--------|-------|
| Contador | 10 / 9 / 8 / 7 / 6 / 5 / 4 / 3 / 2 / 1 / 0 | +0.5 s a +10.5 s desde entrada E4 | 1 número/s exacto. Futura Bold 96 pt min. Sobre sonda de nivel. |
| Etiqueta | Anti-falsos-positivos: 10 s | Con el contador | Futura Bold 28 pt. Debajo del contador. |
| Estado | LED VERDE — BOMBA ON | +11.0 s desde entrada E4 | Al encenderse el LED verde. |
| Flujo | Agua → Red residencial | +11.5 s desde entrada E4 | Sobre tubería de salida. |

---

### E5 — CORTE: SONDA SIN CONTACTO → BOMBA OFF (0:46–1:04)

| Caption | Texto | Timing | Notas |
|---------|-------|--------|-------|
| Contador | 10 / 9 / … / 0 | +0.5 s desde pérdida de contacto de sonda | 1 número/s exacto. Sobre sonda de nivel. |
| Etiqueta | Confirmación: 10 s | Con el contador | Futura Bold 28 pt. |
| Estado | LED VERDE — BOMBA OFF | +11.0 s desde pérdida de contacto | Al apagarse el LED verde. |
| Protección | Protección contra trabajo en vacío. | +12.0 s desde pérdida de contacto | |
| **CAVEAT OBLIGATORIO 1** | **Si el líquido está por debajo del electrodo de nivel bajo, el relé no va a permitir el encendido de la bomba.** | Sincronizado con "La bomba nunca trabaja con el tanque vacío" — permanece **2 s mínimo** | **Texto literal del KB. No acortar. No parafrasear. Prioridad sobre cualquier otro elemento visual simultáneo.** |
| **CAVEAT OBLIGATORIO 2** | **La bomba sólo podrá ser alimentada si hay líquido en el tanque.** | 2 s inmediatamente después del Caveat 1 — permanece **2 s mínimo** | **Texto literal del KB. No acortar. No parafrasear.** |

---

### E6 — MEMORIA DE ESTADO (1:04–1:19)

| Caption | Texto | Timing | Notas |
|---------|-------|--------|-------|
| Evento | Corte eléctrico. | ~1:06 | Con ícono de corte sobre tablero. |
| Retorno | Retorno de energía. | ~1:10 | Con ícono de retorno. |
| Proceso | GRN-MV revalida sonda → operación automática. | ~1:11 | Durante animación de revalidación. |
| Camino A | LED VERDE — ON / Bomba reanuda | ~1:13.5 | Solo si la sonda estaba sumergida al retorno. |
| Camino B | LED VERDE — OFF / Bomba en espera | ~1:13.5 | Solo si la sonda estaba sin contacto al retorno. |

---

### E7 — SPECS Y CIERRE (1:19–1:31)

| Elemento | Texto | Timing | Notas |
|----------|-------|--------|-------|
| Spec 1 | 85 – 305 V~ | +2.0 s desde inicio E7 (parte del strip) | Naranja Exceline. Futura Bold 28 pt. |
| Spec 2 | Sondas hasta 300 m | Simultáneo (bloque del strip) | Blanco. |
| Spec 3 | Salida 3,5 A @ 250 V~ | Simultáneo (bloque del strip) | Naranja Exceline. |
| Web | www.genteca.com.ve | +5.5 s desde inicio E7 | SOLO VISUAL. La voz NO la lee. |
| Eslogan | Garantiza confianza y duración. | +6.5 s desde inicio E7 | Futura Regular. |

---

## Versión accesible — Descripción de audio para usuarios sordos / duros de oído

| Escena | Descripción adicional para audio-off |
|--------|--------------------------------------|
| E1 | Los captions explican los dos vectores de daño (vacío + cavitación) sin voz. |
| E2 | "GRN-MV" y "Exceline Profesional" en pantalla. |
| E3 | Call-outs secuenciales explican el diagrama con 2 electrodos y posición de la bomba a la salida. |
| E4 | Contador visible + "LED VERDE — BOMBA ON" permiten seguir sin audio. |
| E5 | Contador + "LED VERDE — BOMBA OFF" + "Protección contra trabajo en vacío." + los dos caveats literales del KB. |
| E6 | "Corte eléctrico." + "Retorno de energía." + "GRN-MV revalida sonda → operación automática." + bifurcación A/B. |
| E7 | Strip de specs completo + web + eslogan. |

**Evaluación de versión "audio off":** el reel es comprensible sin sonido. Los dos caveats literales de E5 son especialmente importantes para la versión audio-off porque contienen la promesa de protección en texto literal aprobado.

---

# LU-5 — HANDOFF PACKAGE PARA IVO (v2 Vaciado de Tanque)

## Inventario completo de archivos

### Documentos de spec y guion (listos — entregados)

| # | Archivo | Ruta absoluta | Estado |
|---|---------|---------------|--------|
| 1 | NE-2 v2 (guion short tanque) | `C:\Raul\03-projects\genteca\grn-mv-video\2026-05-12_nerea-NE2_grn-mv-IG-tanque-vaciado-short.md` | Entregado |
| 2 | VE voice package v2 tanque | `C:\Raul\03-projects\genteca\grn-mv-video\2026-05-12_vela-VE_grn-mv-IG-tanque-vaciado_voice-package.md` | Entregado |
| 3 | OR motion package v2 tanque | `C:\Raul\03-projects\genteca\grn-mv-video\2026-05-12_orfeo-OR_grn-mv-IG-tanque-vaciado_motion-package.md` | Entregado |
| 4 | NE-1 v2.2 (referencia visual rica) | `C:\Raul\03-projects\genteca\grn-mv-video\2026-05-11_nerea-NE1_grn-mv-video-script-v2.2.md` | Entregado |
| 5 | Paquete hermano LU V1 Pozo | `C:\Raul\03-projects\genteca\grn-mv-video\2026-05-12_luma-LU_grn-mv-IG-pozo-vaciado_video-package.md` | Entregado |
| 6 | Este paquete LU v2 (LU-1 a LU-5) | `C:\Raul\03-projects\genteca\grn-mv-video\2026-05-12_luma-LU_grn-mv-IG-tanque-vaciado_video-package.md` | Entregado |

### Archivos de audio (pendientes de producción)

| # | Archivo | Ruta absoluta | Estado |
|---|---------|---------------|--------|
| 7 | Takes de voz por escena / micro-bloque (v2) | `C:\Raul\03-projects\genteca\grn-mv-video\audio-assets\tanque-vaciado\takes\` | Pendiente (actor/TTS) |
| 8 | Takes seleccionados | `C:\Raul\03-projects\genteca\grn-mv-video\audio-assets\tanque-vaciado\seleccionados\` | Pendiente (selección) |
| 9 | VO concatenado (opcional) | `C:\Raul\03-projects\genteca\grn-mv-video\audio-assets\tanque-vaciado\concatenado\GRNMV-TANQUE_VO-FULL_v2.wav` | Pendiente |

**Naming de audio:** todos los archivos de audio de este paquete usan sufijo `_v2_` (ejemplo: `GRNMV-TANQUE_E1-hook_v2_take01.wav`). Los takes del paquete v1 DEPRECATED deben archivarse antes de la sesión de grabación.

### Archivos de video (pendientes de producción)

| # | Archivo | Ruta absoluta | Estado |
|---|---------|---------------|--------|
| 10 | Master 9:16 | `C:\Raul\03-projects\genteca\grn-mv-video\exports\GRNMV-TANQUE_master-9x16_v2.mp4` | Pendiente (editor externo) |
| 11 | Derivado 1:1 | `C:\Raul\03-projects\genteca\grn-mv-video\exports\GRNMV-TANQUE_feed-1x1_v2.mp4` | Pendiente |
| 12 | Derivado 16:9 | `C:\Raul\03-projects\genteca\grn-mv-video\exports\GRNMV-TANQUE_youtube-16x9_v2.mp4` | Pendiente |
| 13 | Proyecto After Effects | `C:\Raul\03-projects\genteca\grn-mv-video\project-files\GRNMV-TANQUE_v2.aep` | Pendiente (motion designer) |

### Assets de brand y producto (mismos que V1 Pozo — no duplicar)

| # | Asset | Formato requerido | Notas |
|---|-------|------------------|-------|
| B1 | Logo Exceline Profesional | SVG o AI | Mismo que V1 Pozo. No duplicar. |
| B2 | Fuente Handel BT | Archivo de fuente + licencia | Mismo que V1 Pozo. |
| B3 | Futura Bold | Archivo de fuente + licencia | Mismo que V1 Pozo. |
| B4 | Render o fotografía GRN-MV | PNG/JPG, alta resolución | Mismo que V1 Pozo. No producir nueva sesión fotográfica. |
| B5 | Paleta de color oficial Exceline | Hex + Pantone | Confirmar #E8650A. |

### Assets de motion exclusivos de v2 (nuevos — no existen en V1 Pozo)

| # | Asset | Descripción | Notas |
|---|-------|-------------|-------|
| M1 | ASSET 01-T — Diagrama base del tanque | Tanque elevado en corte transversal, 2 electrodos, bomba a la salida | Nuevo. Ver OR-2 ASSET 01-T para especificación completa. |
| M2 | ASSET 02-T — Nivel del agua tanque | 2 estados (sonda sumergida / sonda sin contacto) | Nuevo. Ver OR-2 ASSET 02-T. |
| M3 | ASSET 03-T — Sondas animables tanque | 2 variantes: sonda de nivel + electrodo REF | Nuevo. Ver OR-2 ASSET 03-T. |
| M4 | ASSET 10-T — Call-outs de terminales | Etiquetas actualizadas para 2 electrodos: "Sonda de nivel (T1, T2 puenteado)", "Electrodo común / REF (T5)" | Nuevo. Ver OR-2 ASSET 10-T. |

### Assets de motion reutilizados de V1 Pozo (no construir de nuevo)

ASSET 04 (LEDs), ASSET 05 (flechas de flujo), ASSET 06 (contador 10 s), ASSET 07 (etiqueta validación), ASSET 08 (iconos corte/retorno), ASSET 09 (flecha circular), ASSET 11 (strip de specs), ASSET 12 (render de producto) — todos reutilizar directamente de V1 Pozo. Los archivos deben ser los mismos archivos exactos en ambos proyectos de After Effects para garantizar coherencia visual entre los dos reels.

---

## Miniaturas / Thumbnails sugeridos para Instagram

**Recomendación 1 (frame de producto + hook):**
- Render del GRN-MV centrado en 9:16 sobre fondo blanco/gris.
- Texto superpuesto: "TANQUE VACÍO + BOMBA = QUEMADA" en Futura Bold, naranja Exceline.
- Logo Exceline Profesional en esquina superior derecha.

**Recomendación 2 (frame del contador sobre sonda):**
- Diagrama del tanque con el contador regresivo visible ("5" o "3") sobre la sonda de nivel.
- LED verde apagado, indicando la espera.
- Texto superpuesto: "10 s de protección" en Futura Bold.
- Justificación: muestra el mecanismo diferenciador del producto con claridad inmediata.

**Recomendación de producción:** renderizar ambas opciones como JPG 1080×1920 px y presentar al Owner para selección.

---

## Canal previsto

- **Primario:** Instagram @genteca o @exceline — Reel 9:16.
- **Secundario:** Instagram Feed @genteca — derivado 1:1.
- **Terciario:** YouTube / web Genteca — derivado 16:9.

---

## Resumen ejecutivo para Ivo (≤200 palabras)

Reel Instagram 9:16 de 75–92 s para el GRN-MV de Exceline Profesional, aplicación vaciado de tanque residencial/condominio con bomba a la salida. La pieza es el segundo reel de la serie GRN-MV (hermano del reel de pozo V1), con misma identidad visual y sonora.

El diagrama central muestra un tanque elevado en corte transversal con 2 electrodos (sonda de nivel T1/T2 + electrodo común REF T5) y bomba en la salida. Las escenas centrales son E4 (arranque: sonda sumergida → contador 10 s → LED verde ON) y E5 (corte: sonda sin contacto → contador 10 s → LED verde OFF), seguidas de E6 con bifurcación explícita de memoria de estado ante corte eléctrico. Los dos caveats literales del KB aparecen en E5 como captions on-screen (texto inmutable del fabricante).

Los documentos de spec (NE-2 v2, VE v2, OR v2, LU-1 a LU-4) están completos. Los assets de motion exclusivos de v2 son 4 (ASSET 01-T a 03-T y 10-T); el resto se reutiliza de V1 Pozo. Pendientes antes de publicar: audio, video, decisión sobre bifurcación E6, mercado, y tres gates de aprobación listados abajo.

---

## Aprobaciones pendientes antes de publicar

| Gate | Descripción | Tipo | Bloqueante para publicar |
|------|-------------|------|--------------------------|
| Gate 1 — Ingeniería Genteca | Aprobación técnica sobre E4, E5 y E6 (especialmente: la bifurcación de E6 — nivel cayó durante el corte → bomba inhibida — debe confirmarse como comportamiento documentado, no solo razonado). | Governance | SÍ — gate previo a grabar locución |
| Gate 2 — Bruna (BD-1) | El retardo de 10 s anti-falsos-positivos NO aparece en HDE V7 RB3 ni en MAN V2 IMP Rev RB3. Respaldado por Owner Override (2026-05-10) e I&D verbal (2026-05-12). Owner decide si bloquea publicación hasta que HDE/MAN se actualice o si publica. | Claims / Bruna | CONDICIONAL — Owner decide |
| Gate 3 — Decisión de mercado | Confirmar www.genteca.com.ve (Venezuela) o www.exceline.com.mx (México) o ambas para E7. Default asumido: Venezuela (genteca.com.ve). | Owner | SÍ para arte final de E7 |
| Gate 4 — Composición bifurcación E6 | El motion designer debe presentar la opción de composición para la bifurcación (divisor vertical vs. secuencial) al Owner antes de ejecutar el motion de E6. | Owner / motion designer | SÍ para E6 |

---

## Dudas abiertas (sin modificar insumos aguas arriba)

1. **BD-1 (10 s en HDE/MAN):** misma situación que V1 Pozo. El Owner debe decidir si publica inmediatamente con el respaldo verbal de I&D o espera la actualización documental. Luma no toma esta decisión; escala al Owner a través de Bruna.

2. **Comportamiento de bifurcación E6 (BD-nueva para v2):** la bifurcación narrativa de E6 (si el nivel bajó durante el corte de luz, la bomba queda inhibida hasta que haya nivel suficiente) es narrativamente correcta y fue razonada por Nerea sobre la lógica del sistema. Sin embargo, NE-2 v2 §7 duda 2 abre explícitamente la pregunta de si esta bifurcación es un comportamiento documentado en HDE/MAN. Gate 1 de Ingeniería Genteca debe confirmar esto antes de publicar.

3. **Caveats literales de E5 — tamaño de caja:** los dos caveats del KB son textos de largo considerable para captions on-screen en 9:16. El motion designer debe verificar que el texto sea legible en pantalla de móvil a 28 pt sin superponer otros elementos. Si el texto no cabe legiblemente, escalar a Raul — no acortar el texto del caveat.

4. **Coherencia de nomenclatura terminológica con V1 Pozo:** si los dos reels se publican en la misma cuenta de Instagram, el instalador que vea los dos debe percibir consistencia. La diferencia terminológica ("sonda máxima/mínima/REF" en Pozo vs. "sonda de nivel/electrodo común" en Tanque) es técnicamente correcta pero puede parecer discordante. El Owner puede querer revisar los captions de los dos reels en paralelo antes de publicar para evaluar la consistencia de marca.

5. **Reutilización del take de E2 de V1 Pozo:** si los dos reels se graban en la misma sesión, el take de E2 puede ser el mismo (texto idéntico). Coordinar con el productor de audio antes de la sesión y confirmar que los niveles de audio son consistentes entre ambos reels antes de aceptar la reutilización.

---

## Versiones de exportación y nomenclatura sugerida

| Archivo | Descripción | Formato | Resolución |
|---------|-------------|---------|-----------|
| `GRNMV-TANQUE_master-9x16_v2.mp4` | Master Instagram Reel | H.264/H.265 | 1080×1920 px |
| `GRNMV-TANQUE_feed-1x1_v2.mp4` | Instagram Feed cuadrado | H.264/H.265 | 1080×1080 px |
| `GRNMV-TANQUE_youtube-16x9_v2.mp4` | YouTube / web | H.264/H.265 | 1920×1080 px |
| `GRNMV-TANQUE_thumb-9x16_v2.jpg` | Thumbnail Instagram Reel | JPG | 1080×1920 px |
| `GRNMV-TANQUE_thumb-1x1_v2.jpg` | Thumbnail Feed | JPG | 1080×1080 px |
| `GRNMV-TANQUE_captions-es_v2.srt` | Subtítulos en español (accesibilidad) | .srt | — |

Rutas de exportación: `C:\Raul\03-projects\genteca\grn-mv-video\exports\`
