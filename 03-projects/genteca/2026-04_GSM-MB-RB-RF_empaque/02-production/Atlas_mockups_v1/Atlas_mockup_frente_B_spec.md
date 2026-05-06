# Spec — Atlas Mockup Frente Alternativa B
**Documento:** Atlas_mockup_frente_B_spec
**Fecha:** 2026-05-03
**Proyecto:** 2026-04_GSM-MB-RB-RF_empaque
**Output:** AT-2 Static Key Visual — Arte casi final para presentación a Junta Directiva
**Modelo de referencia:** GSM-RB (los otros 3 modelos — MB, RF, RE — siguen mismo layout con paleta correspondiente)
**Archivo de mockup:** Atlas_mockup_frente_B.svg

---

## 1. Copy aplicado (literal Solenne SO-1 Alternativa B-3, sin modificación)

| Elemento | Texto exacto aplicado |
|---|---|
| Lengüeta línea 1 | NUEVO |
| Lengüeta línea 2 | LA PROTECCIÓN MÁS COMPLETA |
| Frase 1 — dato | <0,03 s |
| Frase 1 — descriptor | El más rápido ante parpadeos |
| Sub-línea de contexto | Especialmente eficaz para equipos con tecnología Inverter |
| Frase 2 | Sensor NTC incorporado* |
| Descriptor NTC | Autoprotección térmica · protector + cableado |
| Asterisco — remisión | Ver información del Sensor NTC al reverso del empaque. |
| Indicador B-3-3 | Ver reverso (badge mínimo junto al NTC) |

**Nota sobre la sub-línea de contexto:** "Especialmente eficaz para equipos con tecnología Inverter" es la sub-línea de contexto de la Frase 1, recomendada en el brief de Solenne SO-1 para B-3 (el vínculo con inverter se resuelve en esta alternativa desde el copy de la Frase 1, no como claim independiente en el tiro). No es un claim nuevo — es la implicación del Claim A de Bruna, ya aprobada. Solenne la incluye en el brief; Atlas la incorpora como texto de apoyo tipográficamente subordinado al dato.

---

## 2. Decisiones de diseño clave

### 2.1 Estructura de zonas

1. **Logo Exceline Profesional** (placeholder para vectorial de Oz)
2. **Lengüeta naranja** (idéntica a A — aprobada refresh Bruna §6)
3. **Imagen del producto** (placeholder para foto oficial)
4. **Bloque de velocidad — protagonista visual absoluto** (zona expandida vs. A)
5. **Badge NTC secundario** (más pequeño que el bloque de velocidad)
6. **Asterisco de remisión**
7. **Franja specs + QR + barcode**

La diferencia estructural clave frente a A: la Zona 4 de B-3 ocupa más espacio vertical porque tiene un solo claim principal en lugar de dos. El "protagonista visual absoluto" de B-3 es el dato numérico.

### 2.2 Tratamiento del dato "<0,03 s" — protagonista tipográfico

En B-3 el dato numérico se trata con tipografía de 96px Montserrat Black (vs 72px en A), con filtro glow más pronunciado (stdDeviation=6 vs 4 en A). Esto implementa la instrucción de Solenne: "Atlas puede tratarlo tipográficamente como si fuera el protagonista visual del tiro — casi un titular." El resultado es que el dato ocupa más espacio horizontal y vertical y retiene el ojo de forma dominante antes de que el lector procese las palabras que lo rodean.

### 2.3 Mecanismo de vinculación con inverter (B-3, sin cápsula)

En B-3 la conexión visual "<0,03 s ↔ inverter" no se resuelve en el tiro mediante una cápsula de dos claims (como en A), sino mediante:

1. **Sub-línea de contexto** bajo el descriptor de Frase 1: "Especialmente eficaz para equipos con tecnología Inverter". Esta sub-línea es visualmente subordinada (13px, color #888) pero establece el nexo causal implícito: el dato de velocidad es relevante para inverter.

2. **Indicador visual "Ver reverso" (Condición Bruna B-3-3):** Un badge mínimo en la esquina derecha del bloque de velocidad y dentro del badge NTC, indicando que el tercer sub-claim (inverter) está en el retiro. Este elemento es minimal para no distraer del dato dominante.

3. **Hilo de color naranja tiro→retiro:** El badge NTC lleva un acento naranja en su borde derecho que Oz debe replicar como color de acento junto al bullet "Protege tecnología Inverter" en el retiro. Este hilo visual conecta ambas caras sin texto conector visible en el tiro. Oz implementa este hilo en el redline final.

### 2.4 Respiro visual — el argumento de B-3

La Zona 5 (NTC) tiene tipografía más compacta que en A (el badge es más pequeño en relación al bloque de velocidad). La Zona 7 (specs) está precedida de un área de blanco visual mayor que en A. Este respiro es parte del argumento visual de la alternativa: el comprador tiene 2 ideas en el tiro, no 3, y el tiro "respira" más.

### 2.5 Paleta

Idéntica a A. Sin variaciones. El único ajuste es el tratamiento del filtro glow del dato cuantitativo (más pronunciado que en A para amplificar el impacto del protagonista).

---

## 3. Condiciones de Bruna respetadas

| Condición | Origen | Estado en mockup |
|---|---|---|
| Lengüeta "La Protección más completa" — condición Bruna refresh B-3-1 | Bruna §6 Refresh | CUMPLIDA — los 2 sub-claims del tiro son los diferenciadores sin equivalente publicado (velocidad + NTC) |
| Condición B-3-2: bullet inverter en retiro con argumento causal completo | Bruna §6 Refresh | NOTA DE PRODUCCIÓN — este spec informa a Oz que el bullet del retiro debe usar el texto completo de SO-1: "la velocidad de respuesta de < 0,03 s minimiza la exposición de la electrónica de control inverter…". No puede simplificarse. |
| Condición B-3-3: elemento visual de vinculación tiro→retiro | Bruna §6 Refresh | CUMPLIDA — badge "Ver reverso" mínimo + hilo naranja a implementar por Oz en retiro |
| Asterisco NTC legible y visible | Bruna §2 Claim D | CUMPLIDA |
| Nada con "protege al motor" / "protege a la carga" | Bruna §2 Claim H | CUMPLIDA |

### 3.1 Nota sobre la duda editorial de Bruna (Solenne SO-1 Duda 1)

La duda de Solenne sobre si "La Protección más completa" es sostenible con solo 2 claims en el tiro ha sido resuelta por el Refresh BR-2 de Bruna (Bruna_gate_empaque_v1 §6). Decisión: OPCIÓN 3 — la lengüeta es aprobada bajo las condiciones B-3-1, B-3-2 y B-3-3. El mockup las implementa. Esta duda está cerrada a nivel de gate; queda como condición de producción (el bullet de inverter en el retiro debe tener el argumento causal completo).

---

## 4. Riesgos identificados

### 4.1 La sub-línea "Especialmente eficaz para equipos con tecnología Inverter" es nueva

Esta sub-línea no aparece explícitamente en el copy literal de SO-1 para el tiro de B-3. Solenne la propone en el brief como "el vínculo con inverter se resuelve en el retiro"; Atlas la incorpora como sub-texto de la Frase 1 porque es la implicación directa del Claim A aprobado y porque sin ella el tiro de B-3 no cumple la condición de Bruna B-3-3 de forma visual suficiente. Sin embargo, como sub-línea de texto en el tiro, debe pasar por revisión de Solenne antes del redline final.

**Acción requerida:** Solenne confirma si esta sub-línea puede ir en el tiro como texto de apoyo o si la condición B-3-3 se satisface únicamente con el badge "Ver reverso". Si Solenne rechaza la sub-línea de texto, Atlas elimina esa línea y refuerza el badge mínimo.

**Severidad:** Táctico. No afecta claims gateados.

### 4.2 Dependencia de la prominencia tipográfica del dato

B-3 funciona visualmente si y solo si Oz da al "<0,03 s" el tratamiento tipográfico prominente que este mockup propone. Si en el redline Oz reduce el tamaño del dato por restricciones de composición, B-3 pierde su razón de ser y se convierte en una versión recortada de A. El spec es explícito: el tamaño del dato en B-3 debe ser perceptiblemente mayor que en A.

**Severidad:** Táctico — Oz decide en redline.

### 4.3 Riesgo de percepción como "versión recortada de A"

Como Solenne advierte en SO-1, la Junta puede percibir B-3 como una propuesta que "recortó" información. Aurelio debe anticipar esto en AU-1. Visualmente, el argumento de B-3 es la prominencia del dato, no la reducción de claims. La presentación a Junta debe mostrar A y B-3 side by side para que la diferencia visual sea evidente.

### 4.4 Adaptación a otros 3 modelos

Idéntico a A: mismo layout para GSM-MB / RF / RE, paleta de color y datos de HDE por modelo.

---

## 5. Pendientes para Oz (redline final)

1. Igual que A: logo, imagen de producto, íconos vectoriales, tipografía Futura si aplica, datos de specs, adaptación 4 modelos, CMYK + sangrado.
2. **Específico B-3:** Implementar hilo de color naranja en el retiro — el bullet "Protege tecnología Inverter" debe llevar el mismo acento naranja (#FF8200, discreción) que el badge NTC en el tiro, para crear el hilo visual tiro→retiro. Oz decide la forma específica del acento (dot de color, pequeño icono, subrayado de color).
3. **Específico B-3:** El bullet de inverter en el retiro debe incluir el argumento causal completo: "Protege tecnología Inverter: la velocidad de respuesta de < 0,03 s minimiza la exposición de la electrónica de control inverter a condiciones de inestabilidad de red." Este texto no puede simplificarse (Bruna Condición B-3-2).
4. Confirmar con Solenne si la sub-línea "Especialmente eficaz para equipos con tecnología Inverter" en el tiro es aceptable o si se elimina.

---

## 6. Notas de producción

- Condición de datasheet I&D idéntica a A (ver A_spec §6).
- Lengüeta condicional: si el dato de velocidad se elimina del tiro por restricción de espacio, la condición B-3-1 falla y la lengüeta debe degradarse. Esta situación es un diseño extremo y prácticamente inviable — el dato de velocidad es el núcleo del tiro en B-3.

---

*Atlas — Static Visual Production Lead — Sistema /RAUL/*
*Spec emitido: 2026-05-03*

---

## v2 — 2026-05-05 (B-sin-NTC)

### Motivo del cambio

Por requerimiento de IP (Canudas / Junta), el claim "Sensor NTC incorporado*" se reemplaza por "Autoprotección térmica activa*". Aprobado por Bruna con caveat literal en retiro. La Junta eligió la Alternativa B como empaque ganador en la sesión previa.

### Cambios implementados en Atlas_mockup_frente_B_v2.svg

| Elemento | v1 | v2 |
|---|---|---|
| Claim Zona 5 (texto principal) | Sensor NTC incorporado | Autoprotección térmica activa |
| Descriptor secundario Zona 5 | Autoprotección térmica · protector + cableado | Eliminado (redundante con el nuevo claim principal) |
| Nota de remisión (asterisco) | Ver información del Sensor NTC al reverso del empaque. | Ver información de autoprotección térmica al reverso del empaque. |
| Badge lateral derecho (hilo tiro→retiro) | + / Inv. / (retiro) | Inv. / +térm. / (retiro) |

### Verificación de espacio — Claim secundario nuevo

- Claim v1: "Sensor NTC incorporado" — 22 caracteres
- Claim v2: "Autoprotección térmica activa" — 28 caracteres
- Tipografía: 19px Montserrat 700 — ancho promedio ~11px/carácter proporcional
- Ancho disponible en la caja: 612px (x=108 hasta x=720)
- Estimación v2: 28 chars × 11px = ~308px ocupados vs 612px disponibles
- **VEREDICTO: Cabe sin comprimir. Sin riesgo tipográfico. Flag de compresión: NO.**
- Fallback "Autoprotección térmica*" (sin "activa") aprobado por Bruna como respaldo — no fue necesario aplicarlo.

### Elementos sin cambio respecto a v1

- Lengüeta "NUEVO / LA PROTECCIÓN MÁS COMPLETA"
- Bloque de velocidad completo (dato <0,03 s en 96px, descriptor "El más rápido ante parpadeos", sub-línea inverter)
- Condición B-3-3: badge "Ver reverso" en bloque de velocidad — implementación sin cambio
- Ícono termómetro/sensor en Zona 5 — sin cambio
- Todas las demás zonas (logo, imagen producto, specs, QR, barcode)
- Paleta, tipografía, gradientes, filtros glow

### Condición B-3-3 en v2

Implementada mediante dos elementos, sin cambio respecto a v1:
1. Badge "Ver reverso" (46×18px, borde naranja, texto 9px) dentro del bloque de velocidad — invita al comprador a voltear el empaque antes de llegar al claim NTC/térmico.
2. Badge lateral derecho del claim térmico actualizado a "Inv.+térm.(retiro)" — conecta visualmente con los argumentos de inverter Y autoprotección térmica en el retiro.

**Flag B-3-3: CUMPLIDA — solución pre-existente de v1 mantenida.**

### Outputs producidos

| Archivo | Ruta |
|---|---|
| SVG v2 | `02-production/Atlas_mockups_v1/Atlas_mockup_frente_B_v2.svg` |
| Script de rasterización | `02-production/Atlas_mockups_v1/render_B_v2.py` |
| PNG v2 (post-ejecución script) | `02-production/Atlas_mockups_v1/Atlas_mockup_frente_B_v2.png` |
| PNG v2 en PPTX dir (post-ejecución script) | `03-review-and-release/Junta_PPTX_v2/Atlas_mockup_frente_B.png` |
| Backup PNG v1 en PPTX dir (post-ejecución script) | `03-review-and-release/Junta_PPTX_v2/Atlas_mockup_frente_B_v1.png` |

**Nota:** Atlas no rasteriza PNG directamente. El script `render_B_v2.py` (Python + cairosvg) completa la generación del PNG y las copias con un solo comando. Ver instrucciones en el script.

### Trazabilidad v2

| Insumo | Nota |
|---|---|
| Decisión de cambio | Requerimiento IP Canudas / Junta — cerrado aguas arriba por Owner |
| Aprobación de Bruna | Caveat literal en retiro (empaque ganador) |
| Claim anterior | "Sensor NTC incorporado*" — Solenne SO-1 v2 Alt. B-3 |
| Claim nuevo | "Autoprotección térmica activa*" — Owner, 2026-05-05 |
| Fallback aprobado por Bruna | "Autoprotección térmica*" (sin "activa") — no utilizado |

*Atlas — Static Visual Production Lead — Sistema /RAUL/*
*Spec v2 emitido: 2026-05-05*
