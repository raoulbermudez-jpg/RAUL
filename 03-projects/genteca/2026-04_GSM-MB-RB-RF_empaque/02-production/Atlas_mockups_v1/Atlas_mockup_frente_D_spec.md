# Spec de Mockup — Alternativa D (Frente GSM)

**Documento:** Atlas_mockup_frente_D_spec
**Fecha:** 2026-05-04
**Proyecto:** 2026-04_GSM-MB-RB-RF_empaque
**Elaborado por:** Atlas — Static Visual Production Lead — Sistema /RAUL/
**Archivo de mockup:** `Atlas_mockup_frente_D.svg`
**Fuente de copy:** Solenne_SO-1_alternativas_v2 §Alternativa D
**Gate de claims:** Bruna_gate_empaque_v1 §7.2 (10x) + §7.1 (NTC) + §2 Claim C (Inverter) + §2 Claim A + §7.3

---

## §1 — Resumen de la alternativa

La Alternativa D organiza el frente del empaque como una propuesta de curiosidad + conversión al QR. La lengüeta abandona el superlativo cualitativo de A/B ("La Protección más completa") y adopta una invitación directa: "NUEVO / AVERÍGUALO". El dato protagonista del tiro es "Hasta 10 veces más rápido" en tipografía notoriamente mayor que los otros dos claims. Los tres claims se unen mediante flechas conectoras gráficas que hacen explícita la cadena causal: velocidad → protección inverter → protección térmica. El QR se posiciona en la zona de títulos (parte derecha del bloque unitario de claims), al mismo nivel jerárquico que los tres claims.

---

## §2 — Anatomía del frente (zonas del SVG)

| Zona | Contenido | Posición SVG |
|---|---|---|
| 1 — Logo | Placeholder EXCELINE PROFESIONAL | y=28 a y=84 |
| 2 — Lengüeta | "NUEVO" + "AVERÍGUALO" + flecha indicadora al QR | y=110 a y=190 |
| 3 — Foto producto | Placeholder imagen GSM-RB (Oz inserta oficial) | y=208 a y=488 |
| 4 — Bloque unitario | 3 claims + flechas conectoras + QR en zona de títulos | y=508 a y=898 |
| 5 — Asterisco remisión | Nota * al retiro + nota caveat velocidad | y=900 a y=964 |
| 6 — Specs técnicas | Franja con datos de HDE (placeholders) | y=966 a y=1085 |
| 7 — Barra inferior | QR secundario opcional + código de barras | y=1086 a y=1192 |

---

## §3 — Decisiones de diseño y justificaciones

### §3.1 Lengüeta "NUEVO + AVERÍGUALO"

- "NUEVO" en Montserrat Black 22px, tracking 6px, fill #0d0d0d sobre fondo #FF8200.
- "AVERÍGUALO" en Montserrat Bold 17px, tracking 2px — tipografía menor que "NUEVO" porque es invitación funcional, no afirmación de marca.
- Flecha indicadora pequeña apuntando hacia el QR integrado en el mismo bloque derecho — el sistema lengüeta → QR funciona como un movimiento de lectura único.
- Diferencia clave respecto a A/B/C: la lengüeta de D no afirma un posicionamiento de calidad ("más completa", "más rápida de la categoría"). Dice que algo cambió y pide al comprador que lo descubra. Esto reduce la información que el comprador sin escanear recibe, pero es la apuesta diseñada para canales donde el instalador técnico ya conoce el GSM-RB como referencia y se pregunta qué cambió.
- Riesgo documentado (Solenne): el comprador que decide en 3 segundos sin escanear recibe menos posicionamiento explícito que con A o B.

**GATE PENDIENTE:** "AVERÍGUALO" no tiene sello explícito de Bruna. Solenne lo clasifica como claim editorial de bajo riesgo (no es claim de performance). Bruna debe confirmar antes de arte final.

### §3.2 Bloque visual unitario — claims + QR

El bloque ocupa y=508 a y=898 (390px). Contiene:

- Fondo: gradiente naranja translúcido (#FF8200 de 15% a 4% de opacidad) + borde izquierdo naranja sólido de 6px — señaliza que los tres claims son parte de un sistema, no una lista de specs aisladas.
- Layout horizontal: claims a la izquierda (x=54 a x=630), QR a la derecha (x=640 a x=748).

### §3.3 Claim protagonista: "Hasta 10 veces más rápido"

- Tipografía: Montserrat Black 52px, fill URL(gradienteDato) naranja #FF8200 → #FF9B33, filtro glow.
- Ocupa dos líneas: "Hasta 10 veces" / "más rápido" — ambas al mismo cuerpo 52px.
- Es notoriamente mayor que los claims 2 y 3 (22px y 18px respectivamente), cumpliendo la instrucción del brief de D: "tipografía notoriamente mayor que los otros dos claims".
- Sub-dato técnico: "< 0,03 s ante parpadeos — verificado I&D Genteca" en 15px blanco/gris claro, inmediatamente debajo. Ancla la credibilidad del ratio sin competir visualmente con el dato visceral.
- Fundamento del claim: Bruna_gate_empaque_v1 §7.2. El "hasta" hace la formulación defensible como máximo (comparación con competidores de mayor latencia). Caveat obligatorio al retiro (Bruna §7.2 texto literal).

### §3.4 Flechas conectoras gráficas

- Se implementan como línea vertical naranja + punta de flecha triangular + etiqueta de causalidad.
- Flecha 1 (velocidad → inverter): etiqueta "por eso..." — explicita la relación causal sin texto adicional en el claim.
- Flecha 2 (inverter → NTC): etiqueta "además..." — señala que el claim 3 es una capa adicional, no consecuencia directa del claim 2.
- Color: #FF8200, opacidad 85% y 70% respectivamente — la segunda flecha es levemente más tenue para no competir con la primera.
- Alternativa para Oz si prefiere elemento más sofisticado: conector curvo del sistema visual Exceline. La función (causalidad visible, arriba-abajo) es condición inamovible — la forma de ejecución es flexible.

### §3.5 Claim 2: "Protege tecnología Inverter"

- Montserrat Bold 22px, fill #ffffff.
- Icono conector onda→flecha→símbolo inverter (tomado de Alt. A, reducido en escala para no competir con el dato protagonista).
- Gate: Bruna §2 Claim C. Sin "auténticamente" en el frente — ese argumento va al QR (Bruna §7.4, Solenne SO-1 v2 decisión editorial).

### §3.6 Claim 3: "Sensor NTC: protege contra calentamiento*"

- Montserrat SemiBold 18px, fill #cccccc — jerarquía visualmente menor que el Claim 2.
- Asterisco * en naranja 22px, claramente separado del texto para legibilidad.
- Sub-línea: "Autoprotección térmica del protector y del cableado" en 12px gris — contextualiza el claim sin sobrepasar la aprobación de Bruna (no dice "protege al motor" ni "protege a la carga").
- Icono termómetro/sensor NTC: idéntico al de A y B para reconocimiento consistente entre alternativas.
- Formulación adaptada de D respecto al Claim D aprobado: "protege contra calentamiento" describe la consecuencia causal (encaja en la arquitectura de flecha); la formulación canónica del gate es "Sensor NTC incorporado*". 

**GATE PENDIENTE:** esta reformulación específica requiere confirmación explícita de Bruna antes de arte final (Solenne SO-1 v2 notas operativas).

### §3.7 QR en zona de títulos

- Posición: x=640 a x=748, y=520 a y=628 — parte derecha del bloque unitario.
- Tamaño en SVG: 108 × 108 px.
- Tamaño físico estimado: el SVG tiene 800px de ancho. En un blíster físico de 100mm de ancho (referencia GSM-RB), la proporción es 108/800 × 100mm = 13.5mm. Si el blíster real del GSM-RB es de 120mm o más (probable para modelo con cables/base), supera el mínimo de 15mm exigido. Oz verifica en el redline con las dimensiones reales del blíster.
- El QR recibe un borde naranja de 3px y filtro de sombra naranja sutil — eleva el QR de elemento de servicio a elemento de comunicación activa.
- Etiqueta bajo el QR: "[QR dinámico]" — recordatorio para Oz de que la URL de destino es editable post-impresión.

---

## §4 — Consistencia con las decisiones de diseño comunes

Las siguientes decisiones son transversales y se mantienen en D sin excepción:

| Decisión | Valor aplicado en D |
|---|---|
| Fondo | Gradiente #1a1a1a → #0d0d0d — idéntico a A/B/C |
| Franja marco | 8px naranja #FF8200 en borde superior e inferior — idéntica a A/B/C |
| Paleta | Naranja #FF8200, gris #737578, blanco #ffffff, secundarios #cccccc/#aaa/#888 |
| Tipografía | Montserrat en pesos 400–900. Futura Bold/Heavy: alternativa canónica para Oz |
| Franja specs técnicas | Zona inferior con placeholders voltaje/corriente/potencia/T°respuesta/origen |
| Asterisco NTC | Visible, legible, remite al retiro. Condición Bruna §2 Claim D cumplida |
| Modelo de referencia | GSM-RB. MB/RF/RE: mismo layout, paleta específica por modelo |
| Ícono parpadeo/rayo | Sistema íconos Exceline (placeholder esquemático; Oz sustituye con vectorial oficial) |

---

## §5 — Decisión recomendada sobre el QR existente del empaque

Bruna_gate_empaque_v1 §7.2 + Solenne SO-1 v2 Brief Atlas punto 5 documentan tres opciones para el QR de la Alternativa D. Atlas presenta las tres y emite recomendación.

### Opción A (recomendada): Redirigir el QR dinámico existente + moverlo a zona de títulos

- El QR existente del empaque es dinámico (URL editable post-impresión). Su destino actual se redirige a la nueva landing de innovaciones.
- El QR se migra de su posición inferior actual a la zona de títulos del tiro (la del bloque unitario de D).
- La zona inferior del blíster queda libre de QR de innovaciones — solo código de barras.
- Si el QR existente cumplía una función secundaria activa (manual técnico, registro de garantía), esa función puede mantenerse en un QR secundario en la zona inferior o canalizarse al mismo destino de la landing (tema 7 o sección separada dentro de la landing).

**Por qué Atlas recomienda Opción A:** es la solución operativamente más limpia. Usa la infraestructura existente (QR dinámico ya impreso en lotes actuales si aplica), evita la saturación de dos QRs prominentes en el tiro, y concentra el argumento de innovaciones en un único punto de escaneo. La migración de posición al tiro de D es la apuesta visual de D — tiene que ser el mismo QR, con el mismo peso.

### Opción B: QR nuevo en zona de títulos + QR existente abajo como secundario

- Se añade un QR nuevo para la landing de innovaciones en la zona de títulos.
- El QR existente permanece en posición inferior con su función actual.
- Riesgo: saturación visual con dos QRs; el comprador puede confundirse sobre cuál escanear.
- Ventaja: no interrumpe la función del QR existente sin conocer su función actual.

### Opción C: Reemplazar el QR existente en posición inferior con el QR de innovaciones (sin migrar a zona de títulos)

- El QR de innovaciones va en la posición baja del blíster (misma posición que en A/B/C).
- No se cumple el concepto de D: "QR en la zona de títulos, mismo nivel que los claims".
- Esta opción produce una versión degradada de D — no es D propiamente dicho.
- Solo válida si el blíster físico no tiene espacio suficiente para el QR en la zona de títulos.

**Condición de cierre:** Atlas no puede resolver entre Opción A y B sin saber qué función cumple hoy el QR existente del empaque (¿manual técnico? ¿garantía? ¿sin función activa?). Esta decisión es de Raul (Solenne SO-1 v2 notas operativas §Cascada de acciones).

---

## §6 — Trazabilidad de claims

| Claim en tiro | Sello BR-2 | Ruta Bruna | Caveat al retiro |
|---|---|---|---|
| "Hasta 10 veces más rápido" | APROBADO CON CAVEAT | Bruna_gate_empaque_v1 §7.2 | Texto literal §7.2 — exclusivo de D |
| "< 0,03 s ante parpadeos" (sub-dato) | APROBADO CON CAVEAT | Bruna §2 Claim A + §7.3 | Texto literal §7.3 |
| "Protege tecnología Inverter" | APROBADO CON CAVEAT | Bruna §2 Claim C | Texto literal §2 Claim C |
| "Sensor NTC: protege contra calentamiento*" | APROBADO CON CAVEAT (reformulación pendiente gate) | Bruna §2 Claim D + §7.1 | Texto literal §7.1 |
| "NUEVO / AVERÍGUALO" (lengüeta) | PENDIENTE GATE BRUNA | — | "NUEVO" aprobado en A/B/C; "AVERÍGUALO" requiere confirmación |

---

## §7 — Condiciones de producción

1. Datasheet actualizado de I&D Genteca con < 30 ms documentado — antes de imprimir (igual que A/B/C).
2. Decisión de Raul sobre función del QR existente — antes de cerrar el mockup final (desbloquea la elección entre Opción A y B del §5).
3. Confirmación de Bruna: (a) lengüeta "AVERÍGUALO" — sello explícito; (b) formulación "Sensor NTC: protege contra calentamiento*" — confirmación de que la adaptación editorial está dentro del gate del Claim D.
4. Contenidos del destino QR producidos y publicados antes de impresión (o landing temporal de lanzamiento activa). Sin contenidos, D es una invitación a un destino vacío.
5. Verificación de Oz del tamaño físico del QR en las dimensiones reales del blíster GSM-RB: debe superar los 15mm × 15mm en impresión final.

---

## §8 — Pendientes para Oz (redline arte final D)

Los pendientes de A/B/C (README §Pendientes globales) aplican igualmente a D. Los específicos de D:

1. Verificar tamaño físico del QR en el blíster real (mínimo 1,5 cm × 1,5 cm en impresión).
2. Implementar la opción de QR elegida por Raul (Opción A recomendada vs. Opción B).
3. Refinar la flecha conectora con el sistema visual Exceline si existe elemento canónico de flujo/conector en el brand kit. La forma es flexible; la función de causalidad es inamovible.
4. Aplicar el gradiente del dato protagonista ("Hasta 10 veces más rápido") en el sistema tipográfico final — en SVG se usa gradiente vectorial; Oz adapta en el software de arte.
5. Confirmar que "AVERÍGUALO" tiene sello de Bruna antes de producir el arte final de D.
6. Implementar los tres caveats obligatorios al retiro: §7.2 (10x) + §7.3 (velocidad) + §2 Claim C (inverter) + §7.1 (asterisco NTC). D tiene el mayor número de caveats de las cuatro alternativas.

---

## §9 — Nota final

Este mockup se entrega como wireframe estructurado SVG — fidelidad suficiente para evaluación de Junta. La arquitectura de composición (bloque unitario izquierda-QR derecha, flechas conectoras, protagonismo del dato visceral) está completamente representada. Oz toma el SVG de D como referencia de estructura si esta alternativa resulta ganadora y produce el arte final en CMYK + sangrado 3mm para imprenta.

---

*Atlas — Static Visual Production Lead — Sistema /RAUL/*
*Spec emitido: 2026-05-04*
*Estado: COMPLETO — listo para Aurelio (AU-1 v2) y para Junta Directiva*
