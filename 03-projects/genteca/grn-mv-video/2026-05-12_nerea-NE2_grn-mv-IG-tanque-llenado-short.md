---
title: "GRN-MV — Reel Instagram, Llenado de Tanque (Bomba a la Entrada), Short NE-2 v1.2"
type: Script
agent: Nerea
version: v1.2
product_code: GRN-MV
product_line: Exceline Profesional
aplicacion: Llenado de tanque, bomba a la entrada, lógica inversa al vaciado
duracion_objetivo: 90–110 s (<2:00 min)
audiencia_primaria: Técnico instalador (sistemas residenciales, condominios, tanques elevados)
audiencia_secundaria: Administradores de condominio / cliente final
formato: "9:16 Instagram Reel"
date: 2026-05-12
deriva_de: "2026-05-12_nerea-NE2_grn-mv-IG-pozo-vaciado-short.md (NE-2 V1 Pozo); 2026-04-18_nota-aplicacion_tecnica-llenado-tanque-y-vaciadopozo-con-proteccionvoltaje-y-opcionalarma.md"
status_documental: "GUION COMPLETO — Lógica de LED verde corregida según clarificación verbal de I&D Genteca (2026-05-12): LED verde indica señal permisiva al motor → LED ON cuando la bomba tiene permiso para funcionar (vaciado: nivel suficiente para extraer; llenado: nivel insuficiente, hay que llenar). La frase del MAN 'la indicación del LED verde se invierte' refleja la inversión de la condición permisiva subyacente, no la semántica al usuario. 10 s anti-falsos-positivos confirmados verbalmente por I&D; doc oficial pendiente de actualización por Genteca."
replaces: "v1.1 (interpretación errónea de la inversión LED — preservada en historial git)"
---

# GRN-MV — Reel Instagram v1 (NE-2)
## Llenado de Tanque con Bomba a la Entrada — Short 9:16

---

> **Nota de producción general:** Formato 9:16 vertical. Captions on-screen en TODAS las escenas (audio off por defecto en Instagram). Fuente de call-outs: Futura Bold, mínimo 28 pt. Paleta: fondo neutro gris/blanco; naranja Exceline solo en call-outs y nombre de producto.
>
> **Trazabilidad — Flags C-1 y C-2 RESUELTOS — REFRAME I&D (2026-05-12):** La lógica de la inversión del LED queda reencuadrada por clarificación verbal de I&D Genteca transmitida por el Owner (2026-05-12). El MAN V2 IMP Rev RB3, página 2, nota al pie, dice: "En la Aplicación de Llenado, la indicación del LED verde se invierte." I&D aclara que el LED verde indica la **señal permisiva al motor**, no el estado del contacto eléctrico visto por el usuario. La semántica al usuario es idéntica en ambos modos: **LED ON = bomba con permiso para operar; LED OFF = bomba sin permiso.** Lo que se invierte es la condición física subyacente: en vaciado, el permisivo es "hay nivel suficiente para extraer" (LED ON cuando el pozo o tanque tiene agua); en llenado, el permisivo es "le falta nivel al tanque" (LED ON cuando el tanque necesita llenarse). (C-2) la bomba va en T6 (NC) para llenado — confirmado por el manual y por Owner Override Q5. Las animaciones de LED en sub-beats 4A, 4B, 4C y E5 han sido corregidas en esta versión v1.2 para reflejar LED ON = bomba en operación en ambos modos. **Pendiente: aprobación final de Ingeniería Genteca antes de grabar locución (estándar).** Ver mini-cover note actualizada.

---

## ESCENA 1 — HOOK (Beat: Problema real del instalador)
**Duración estimada:** 8–10 s

**Voz en off:**
"Una bomba que sigue llenando el tanque cuando ya está lleno desborda el agua. Una bomba que trabaja con el tanque sin agua se quema. El GRN-MV lo controla automáticamente."

**Caption on-screen (sincronizado con voz):**
- Línea 1: "TANQUE LLENO + BOMBA ENCENDIDA = REBOSE" — texto grande, primeros 3 s.
- Línea 2 (segundo beat): "TANQUE VACÍO + BOMBA SIN AGUA = DAÑO"
- Línea 3 (tercero): "El GRN-MV lo controla solo."

**Descripción visual:**
Secuencia rápida de 2 fotogramas:
1. Tanque elevado desbordando agua — bomba en la entrada encendida.
2. Bomba a la entrada del tanque sin agua en la tubería de succión, ícono de temperatura/calor.
Fondo neutro, estilo técnico. Ritmo de corte: cada 3–4 s.

**Beat narrativo:** Doble problema específico del instalador de llenado. Sin "¿Sabías que…?". Directo a la consecuencia técnica.

---

## ESCENA 2 — IDENTIFICACIÓN DEL PRODUCTO (Beat: Presentación)
**Duración estimada:** 6–7 s

**Voz en off:**
"GRN-MV. Relé de Nivel para Líquidos Conductores. Exceline Profesional."

**Caption on-screen:**
- "GRN-MV" en tipografía Handel BT, tamaño grande, centrado.
- "Exceline Profesional" debajo.
- Eslogan: "Garantiza confianza y duración."

**Descripción visual:**
Render o fotografía del producto sobre fondo blanco/gris, centrado en frame 9:16. Logo Exceline Profesional con fade-in. No usar logo Genteca en este plano.

---

## ESCENA 3 — LAYOUT EN CAMPO: DIAGRAMA COMPRIMIDO (Beat: Contexto técnico)
**Duración estimada:** 12–15 s

**Voz en off:**
"El tanque tiene tres sondas. La bomba está a la entrada, subiendo agua desde una fuente externa. El GRN-MV está en el tablero, conectado al contactor de la bomba. Cuando el tanque está bajo de agua, la bomba llena. Cuando el tanque alcanza el nivel máximo, la bomba se detiene."

**Caption on-screen (call-outs sincrónicos):**
- "Tanque (residencial / condominio)"
- "Sonda común / REF (T5) — referencia eléctrica"
- "Sonda MIN (T2) — arranque de bomba (nivel bajo)"
- "Sonda MAX (T1) — corte de bomba (nivel lleno)"
- "Bomba a la ENTRADA → desde fuente externa"
- "GRN-MV → Contactor → Bomba"

**Descripción visual:**
Diagrama vectorial comprimido para 9:16:
- Tanque en sección transversal, ocupando el 50–60 % del frame.
- Tres sondas dentro del tanque: común/REF en el punto más bajo (siempre sumergida cuando hay agua mínima), sonda MIN a altura media, sonda MAX en la parte superior.
- Bomba monofásica conectada a la tubería de ENTRADA del tanque; la tubería de entrada entra por arriba o por el lateral del tanque; la fuente (pozo, red, suministro externo) queda fuera del frame o indicada como etiqueta.
- Tablero lateral con GRN-MV y contactor.
- El nivel del agua en el estado de reposo inicial se muestra por DEBAJO de la sonda MIN (tanque bajo, en espera de llenado) para ilustrar el estado de partida del ciclo.

**Diferencia visual clave respecto a la versión vaciado:** En llenado, el nivel del agua SUBE durante la operación y la bomba se APAGA al alcanzar MAX. En vaciado, el nivel BAJA durante la operación y la bomba se apaga al perder MIN. El diagrama de este reel muestra el nivel subiendo con la bomba activa.

---

## ESCENA 4 — CICLO COMPLETO: MIN SIN CONTACTO → BOMBA ON / MAX CUBIERTA → BOMBA OFF (Beat: Demo central)
**Duración estimada:** 35–40 s

### Sub-beat 4A — Nivel por debajo de MIN → 10 s → Bomba ON (12–14 s)

**Voz en off:**
"El nivel del tanque cae por debajo de la sonda mínima. El GRN-MV detecta que la sonda mínima está sin contacto. Espera diez segundos para descartar turbulencia o salpicaduras. Cumplido ese retardo, activa la bomba. El LED verde se enciende: la señal permisiva al motor está activa porque el tanque necesita llenarse."

**Caption on-screen:**
- Destello / cambio de color en la punta de la sonda MIN al perder el contacto con el agua.
- Contador regresivo grande: "10… 9… 8… → 0" visible sobre la sonda MIN.
- "Validación anti-falsos-positivos: 10 s"
- Al llegar a 0: "LED VERDE — ON (señal permisiva activa — tanque sin nivel suficiente, bomba arrancando para llenar)"
- Flecha en tubería de entrada: "Agua entra al tanque →"

**Descripción visual:**
El nivel del agua está por debajo de la sonda MIN (sonda MIN fuera del agua). Contador regresivo sobre MIN. Al completarse: contactor cierra; flujo en la tubería de entrada se activa; el nivel del agua comienza a subir. LED verde del relé se ENCIENDE al completarse el retardo y permanece ENCENDIDO durante todo el llenado (señal permisiva activa, bomba operando). Sin parpadeo durante el conteo.

**Nota para producción — semántica del LED verde (confirmada por MAN V2 IMP RB3 + I&D Genteca 2026-05-12):** El LED verde indica la señal permisiva al motor: ON cuando la bomba tiene permiso para funcionar; OFF cuando no. En vaciado (pozo o tanque), permisivo = "hay nivel suficiente para extraer". En llenado, permisivo = "el tanque necesita llenarse". La semántica para el instalador es la misma en ambos modos (LED ON = bomba en operación), aunque la condición física subyacente es opuesta. La frase del MAN "la indicación del LED verde se invierte" se refiere a esta inversión de condición subyacente, no a la semántica al usuario. Animar el LED verde encendido durante toda la fase activa de llenado.

---

### Sub-beat 4B — Llenado en curso (6–8 s)

**Voz en off:**
"La bomba sube agua al tanque. El nivel asciende. La bomba continúa llenando mientras la sonda máxima no esté cubierta."

**Caption on-screen:**
- Flecha de ascenso del nivel del agua.
- Flecha en tubería de entrada: "Agua entrando →"
- Etiqueta: "Bomba activa — tanque llenándose"
- "LED VERDE — ON — señal permisiva sostenida mientras la bomba llena."

**Descripción visual:**
El nivel del agua sube desde por debajo de MIN, pasa por MIN (MIN vuelve a estar sumergida), y continúa subiendo hacia MAX. Bomba activa todo el tiempo. Flujo visible en la tubería de entrada.

---

### Sub-beat 4C — MAX cubierta → 10 s → Bomba OFF (14–16 s)

**Voz en off:**
"Cuando el tanque se llena, el LED verde se apaga: la señal permisiva al motor se retira porque el tanque ya alcanzó el nivel suficiente. La bomba se apaga."

**Caption on-screen:**
- Destello / cambio de color en la punta de la sonda MAX al quedar cubierta.
- Contador regresivo: "10… 9… 8… → 0" visible sobre la sonda MAX.
- "Validación: 10 s"
- Al llegar a 0: "LED VERDE — OFF (tanque cubrió MAX — señal permisiva lifted — bomba se apaga)"
- Texto breve superpuesto: "Protección contra rebose del tanque."

**Descripción visual:**
El nivel del agua sube hasta cubrir la sonda MAX. Contador regresivo sobre MAX. Al llegar a 0: el relé corta la bomba; flujo en tubería de entrada se detiene; el nivel queda justo en MAX o ligeramente sobre MAX — el tanque está lleno, sin desbordar. El nivel NO debe verse desbordando en el diagrama.

---

## ESCENA 5 — DIFERENCIADOR: MEMORIA DE ESTADO (Beat: Diferenciador)
**Duración estimada:** 18–22 s

**Voz en off:**
"Corte de luz: el GRN-MV memoriza el estado de su salida. Al retornar la energía, revalida las sondas y retoma la operación automáticamente. Sin intervención manual."

**Caption on-screen:**
- Ícono de relámpago cruzado sobre el tablero: "Corte eléctrico."
- LEDs apagados (rojo y verde).
- Ícono de relámpago activo al retorno: "Retorno de energía."
- "GRN-MV revalida sondas → reanudación automática."

**Descripción visual:**
Estado activo: bomba llenando el tanque, nivel subiendo, LED rojo encendido (equipo energizado). Corte: ícono de relámpago, LEDs apagan. Retorno: LED rojo enciende primero; breve animación de pulso en las sondas (revalidación de estado); la bomba reanuda si corresponde según el nivel real. Secuencia lineal, sin parpadeo de LEDs durante la revalidación.

**Nota para producción — LED verde en memoria de estado (llenado):** En llenado, el LED verde indica la señal permisiva al motor. Al retorno de energía, tras revalidación de sondas: si el estado memorizado indica bomba llenando (nivel bajo de tanque, señal permisiva activa), el LED verde vuelve a ON; si el estado memorizado indica bomba en standby (MAX ya estaba cubierta, señal permisiva retirada), el LED verde permanece OFF. La semántica al usuario es idéntica a la del vaciado: LED ON = bomba con permiso para operar. Asegurar que la animación del retorno de energía refleje LED verde ON cuando la bomba reanuda el llenado — fuente: MAN V2 IMP Rev RB3, página 2, nota al pie + clarificación I&D Genteca 2026-05-12.

---

## ESCENA 6 — SPECS Y CIERRE (Beat: Cierre profesional)
**Duración estimada:** 10–12 s

**Voz en off:**
"Opera en redes de 85 a 305 voltios. Sondas hasta 300 metros del tablero. Consulte el manual o comuníquese con su distribuidor autorizado."

**Caption on-screen:**
- Strip de specs: "85 – 305 V~" | "Sondas hasta 300 m" | "Salida 3,5 A @ 250 V~"
- Logo Exceline Profesional centrado.
- "GRN-MV" en Handel BT.
- Web: www.genteca.com.ve / www.exceline.com.mx (según mercado objetivo).
- Eslogan: "Garantiza confianza y duración."

**Descripción visual:**
Render de producto centrado en 9:16 con fade a fondo neutro. Strip de specs (3 s), luego web y logo. Fade out. Sin música de cierre estridente.

---

## RESUMEN DE ESTRUCTURA Y TIMING

| Escena | Beat | Duración est. |
|--------|------|---------------|
| 1 | Hook — doble problema llenado | 8–10 s |
| 2 | Identificación de producto | 6–7 s |
| 3 | Diagrama de campo comprimido (tanque, bomba entrada) | 12–15 s |
| 4A | MIN sin contacto → 10 s → Bomba ON | 12–14 s |
| 4B | Llenado en curso | 6–8 s |
| 4C | MAX cubierta → 10 s → Bomba OFF | 14–16 s |
| 5 | Diferenciador: memoria de estado | 18–22 s |
| 6 | Specs + cierre profesional | 10–12 s |
| **Total** | | **86–104 s (1:26 – 1:44 min)** |

Dentro del objetivo <2:00 min.

---

# MINI-COVER NOTE — NE-2 Versión 3 (Tanque / Llenado)

## 1. Trazabilidad de insumos

| Insumo | Documento consumido | Ruta |
|--------|---------------------|------|
| NE-1 v2.2 | 2026-05-11_nerea-NE1_grn-mv-video-script-v2.2.md | `C:\Raul\03-projects\genteca\grn-mv-video\` |
| NE-2 V1 (Pozo) | 2026-05-12_nerea-NE2_grn-mv-IG-pozo-vaciado-short.md | Idem — estructura base y beats |
| Vera Technical Verification + Owner Override | 2026-05-10_vera-technical-verification_grn-mv-video.md | `C:\Raul\03-projects\genteca\grn-mv-video\` — Q5 Owner Override: "En vaciado la carga va en T8 (NA). En llenado la carga va en T6 (NC)." Alineado con footnote literal de MAN V2 IMP Rev RB3. |
| Spec llenado-tanque-y-vaciadopozo | 2026-04-18_nota-aplicacion_tecnica-llenado-tanque-y-vaciadopozo... | `C:\Raul\02-knowledge-base\02-domains\01-genteca\specs\` — confirma GRN-MV usado para llenado de tanque con 3 sondas (MAX1, MIN1, común); no detalla el mecanismo de inversión |
| HDE V7 Rev RB3 | Consumido vía NE-1 v2.2 | Specs: 85–305 V~, 300 m, 3,5 A @ 250 V~ |
| MAN V2 IMP Rev RB3 | Consumido vía NE-1 v2.2 + verificación directa Owner 2026-05-12 | Terminales, LEDs — **nota al pie del diagrama de conexión y de indicadores LED para aplicación de vaciado (página 2):** "En la Aplicación de Llenado, la indicación del LED verde se invierte. Además, en la salida del GRN-MV, el voltaje que debe ser controlado o interrumpido se mantiene en el terminal 7 (contacto común), mientras que la carga a manejar cambia al terminal 6." — Ruta: `G:\Mi unidad\RAUL\colaboradores\Genteca\Ana-Mendez\01_De_Ana_Para_Raoul\20250714_GRN-MV_MAN_V2_IMP_Rev RB3.pdf` |
| Clarificación verbal I&D Genteca (2026-05-12) | Owner transmitió directamente — sin documento escrito disponible | Owner transmitió: "el LED verde indica la señal permisiva al motor, ON cuando la bomba tiene permiso para operar; la inversión del MAN se refiere a la condición permisiva subyacente, no a la semántica al usuario." + "10 s de validación confirmados como comportamiento real del producto; documentación HDE/MAN pendiente de actualizar por Genteca." |

## 2. Diferencias respecto a NE-2 Versión 1 (Pozo) — cambios narrativos y eléctricos

| Elemento | Versión 1 (Pozo / Vaciado) | Versión 3 (Tanque / Llenado) |
|----------|---------------------------|-------------------------------|
| Dirección del ciclo | Nivel BAJA durante operación | Nivel SUBE durante operación |
| Bomba ON cuando... | MAX queda sumergida | MIN deja de estar sumergida (nivel bajo) |
| Bomba OFF cuando... | MIN deja de estar sumergida | MAX queda sumergida (nivel lleno) |
| Contacto de carga | T8 (NA) — cierra al activar relé | T6 (NC) — abre al activar relé |
| Hook narrativo | Bomba en seco en el pozo | Rebose + bomba sin agua en llenado |
| Contexto visual | Pozo subterráneo | Tanque con bomba de entrada |
| Beneficio central | Protección contra trabajo en seco | Protección contra rebose + trabajo en seco en llenado |

## 3. Claims con caveat literal integrados

| Claim usado | Texto literal fuente | Ubicación |
|-------------|----------------------|-----------|
| LED verde ON = señal permisiva al motor (vaciado: nivel suficiente para extraer; llenado: tanque necesita llenarse) | MAN V2 IMP RB3, página 2, nota al pie "la indicación del LED verde se invierte" + clarificación I&D 2026-05-12 que aclara que la inversión es de condición subyacente, no de semántica al usuario | E4A, 4B, 4C, E5 |
| LED rojo ON = producto energizado | MAN V2 IMP RB3, sección INDICADORES | E5 |
| 10 s retardo operativo simétrico | Owner Override 2026-05-10 (Corrección 1) + confirmación verbal I&D Genteca 2026-05-12 | Sub-beats 4A y 4C |
| Memoria del estado de salida de activación | Owner Override 2026-05-10/11 (Corrección 2) | E5 |
| 85–305 V~ rango de operación | HDE V7 RB3, tabla de especificaciones | E6 |
| Sondas hasta 300 m del tablero | HDE V7 RB3, tabla de especificaciones | E6 |
| 3,5 A @ 250 V~ capacidad de contactos | HDE V7 RB3, tabla de especificaciones | E6 |
| Mecanismo de inversión llenado/vaciado: T6 (NC) vs T8 (NA) | Texto literal de MAN V2 IMP Rev RB3, página 2, nota al pie: "la carga a manejar cambia al terminal 6" | E3, sub-beats 4A, 4C |

## 4. Flags — estado actualizado tras verificación con MAN V2 IMP RB3 (2026-05-12)

### FLAG C-1 — RESUELTO
**Comportamiento del LED verde en llenado — reencuadre definitivo I&D (2026-05-12).**

Cita literal de MAN V2 IMP Rev RB3, página 2, nota al pie: "En la Aplicación de Llenado, la indicación del LED verde se invierte."

Reencuadre I&D confirmado por Owner (2026-05-12): la "inversión" es de la condición permisiva subyacente, no de la semántica al usuario. El LED verde indica la señal permisiva al motor: ON cuando la bomba tiene permiso para operar; OFF cuando no. En vaciado, el permisivo es "hay nivel suficiente para extraer" (LED ON = nivel ok = bomba extrayendo). En llenado, el permisivo es "le falta nivel al tanque" (LED ON = nivel bajo = bomba llenando). La animación del LED en llenado replica la semántica de vaciado: LED ON cuando la bomba debe estar trabajando. Captions y animaciones corregidos en v1.2.

### FLAG C-2 — RESUELTO
**Confirmación de la inversión vía T6 (NC) en MAN.**

Cita literal de MAN V2 IMP Rev RB3, página 2, nota al pie: "en la salida del GRN-MV, el voltaje que debe ser controlado o interrumpido se mantiene en el terminal 7 (contacto común), mientras que la carga a manejar cambia al terminal 6."

El Owner Override Q5 (Vera Technical Verification 2026-05-10) y el texto del manual son coherentes. El guion v1.1 refleja esta lógica en todos los sub-beats y notas para producción.

### FLAG C-3 — CERRADO (informativo)
La spec "llenado-tanque-y-vaciadopozo" menciona explícitamente 3 sondas para el control del tanque en llenado (MAX1, MIN1, común), lo cual es consistente con el diagrama de este guion. Confirmado por spec. La animación de este reel solo muestra el relé de tanque (GRN-MV 1) — el GRN-MV 2 del pozo (alarma) no es parte de este video y no debe incluirse en el diagrama.

## 5. Supuestos narrativos

- El LED verde indica la señal permisiva al motor, no el estado eléctrico del coil del relé. La semántica al usuario es consistente en los tres reels de la serie: LED ON = bomba con permiso para operar; LED OFF = bomba sin permiso. La condición física que activa el permisivo cambia entre modos (nivel suficiente para extraer en vaciado; nivel insuficiente para retener en llenado), pero la lectura visual para el instalador es la misma. Fuente: MAN V2 IMP Rev RB3, página 2, nota al pie + clarificación I&D Genteca 2026-05-12.
- El 10 s simétrico aplica tanto a la transición MIN-sin-contacto (arranque) como a la transición MAX-cubierta (corte), por el mismo mecanismo de anti-falsos-positivos confirmado verbalmente por I&D Genteca (2026-05-12) y por Owner Override (Corrección 1). Documentación HDE/MAN pendiente de actualización oficial por Genteca.
- La memoria de estado en llenado memoriza la señal permisiva al momento del corte: si el permisivo estaba activo (nivel bajo de tanque, bomba llenando), al retorno de energía el LED verde vuelve a ON y la bomba reanuda; si el permisivo estaba retirado (MAX cubierta, bomba en standby), el LED verde permanece OFF.

## 6. Dudas abiertas para escalación

1. **Mercado objetivo** (Venezuela / México / ambos) — determina URL de cierre en E6.
2. **Aprobación final de Ingeniería Genteca** sobre la lógica completa del ciclo de llenado antes de grabar locución (estándar para toda pieza técnica). Flags C-1 y C-2 ya no son bloqueantes para esta aprobación — el manual es la fuente.
3. **BD-1 CONFIRMADO verbalmente, doc pendiente:** retardo de 10 s anti-falsos-positivos confirmado verbalmente por I&D Genteca (2026-05-12). El Owner aguarda la próxima revisión de documentación oficial de Genteca para que los 10 s queden incorporados en HDE y MAN. Hasta entonces, el respaldo es: confirmación verbal I&D + Owner Override 2026-05-10. El guion usa los 10 s tal como están; no requiere ajuste.
