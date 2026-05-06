# Spec — Atlas Mockup Frente Alternativa C
**Documento:** Atlas_mockup_frente_C_spec
**Fecha:** 2026-05-03
**Proyecto:** 2026-04_GSM-MB-RB-RF_empaque
**Output:** AT-2 Static Key Visual — Arte casi final para presentación a Junta Directiva
**Modelo de referencia:** GSM-RB (los otros 3 modelos — MB, RF, RE — siguen mismo layout con paleta correspondiente)
**Archivo de mockup:** Atlas_mockup_frente_C.svg

---

## 1. Copy aplicado (literal Solenne SO-1 Alternativa C, sin modificación)

| Elemento | Texto exacto aplicado |
|---|---|
| Lengüeta línea 1 | NUEVO |
| Lengüeta línea 2 | EL MÁS RÁPIDO DE LA CATEGORÍA |
| Frase dominante — versión completa | Actúa en <0,03 s antes de que la fluctuación llegue a tu equipo |
| Sub-texto compacto | Sensor NTC* + Protección Inverter incluidos |
| Asterisco — remisión | Ver información del Sensor NTC al reverso del empaque. |

**Confirmación de uso de versión completa:** Se usó la versión íntegra del Claim K (Bruna_gate_empaque_v1 §2 Claim K aprobado). No fue necesario recurrir a la versión reducida "Actúa en < 0,03 s antes de que la fluctuación dañe tu equipo". Ver §2.1 para la verificación de espacio.

---

## 2. Decisiones de diseño clave

### 2.1 Verificación de espacio — CONFIRMACIÓN REQUERIDA POR SOLENNE SO-1

**Pregunta de Solenne:** ¿Cabe la frase dominante completa en tipografía legible en el área disponible del blíster?

**Análisis de Atlas:**

- Frase completa: "Actúa en < 0,03 s antes de que la fluctuación llegue a tu equipo"
- Conteo de caracteres (con espacios): aproximadamente 65 caracteres
- Ancho útil del tiro en el mockup: 680px (800px total - márgenes de 60px cada lado)
- Tipografía aplicada: Montserrat Bold 24px
- Estimación de ancho por carácter en Montserrat Bold 24px: ~13-14px promedio
- Ancho de línea a 24px y ~65 caracteres: ~845-910px → no cabe en una línea
- División natural en 2 líneas de ~32-33 caracteres cada una:
  - Línea 1: "Actúa en <0,03 s antes de que" — ~32 chars → ~416-448px — CABE
  - Línea 2: "la fluctuación llegue a tu equipo" — ~34 chars → ~442-476px — CABE
- Altura total en 2 líneas (24px + interlineado 28px + segunda línea 24px): ~76px
- Espacio disponible en la zona de frase dominante: 148px
- Margen sobrante vertical: ~72px — espacio suficiente para el sub-texto

**VEREDICTO: LA FRASE DOMINANTE COMPLETA ES VIABLE en este formato de blíster.**

**Condición:** La tipografía mínima debe ser 20px para garantizar legibilidad en el blíster físico impreso. En el mockup digital se usa 24px. Oz verifica en el redline que en el tamaño físico real del blíster el cuerpo mínimo de 20px se mantiene.

**Si Oz detecta restricción de espacio en el blíster físico real**, la versión reducida aprobada es: "Actúa en < 0,03 s antes de que la fluctuación dañe tu equipo" (Solenne SO-1, Bruna Claim K — no hay cambio de sello de gate con ese argumento). Atlas informa este resultado a Solenne y Aurelio: la frase completa es viable en el mockup y presumiblemente en el blíster estándar; la confirmación final es de Oz sobre el arte en tamaño real.

### 2.2 Estructura de zonas

1. **Logo Exceline Profesional** (placeholder para vectorial de Oz)
2. **Lengüeta naranja** — diferente a A y B: "EL MÁS RÁPIDO DE LA CATEGORÍA" (Claim J)
3. **Imagen del producto** (placeholder para foto oficial)
4. **Ícono narrativo** — cadena fluctuación → respuesta → equipo intacto
5. **Bloque de frase dominante** — con "<0,03 s" en naranja dentro de la frase + sub-texto compacto
6. **Asterisco de remisión**
7. **Franja specs + QR + barcode**

### 2.3 Ícono narrativo — elemento de mayor libertad creativa

**Propuesta de Solenne:** "una flecha de alta velocidad que intercepta una onda de red antes de llegar a un símbolo de equipo inverter."

**Implementación de Atlas:** Se construyó una representación de tres elementos en línea horizontal:

- **Elemento 1 — Fluctuación:** Onda sinusoidal distorsionada con pico de tensión (trazo gris/blanco, tensión visual). Etiqueta: "Fluctuación".
- **Flecha de transición 1→2:** Naranja, discreta, conecta los tres elementos.
- **Elemento 2 — El protector actuando:** Círculo de acción con rayo interceptor en #FF8200, glow pronunciado. El dato "<0,03 s" aparece embebido en este elemento como leyenda. Es el elemento de mayor escala visual del ícono — el protagonista del ícono narrativo.
- **Flecha de transición 2→3:** Naranja, discreta.
- **Elemento 3 — Equipo intacto:** Rectángulo estilizado con símbolo AC interno + checkmark naranja en la esquina superior derecha. Etiqueta: "Equipo intacto". El checkmark en naranja establece la resolución positiva de la narrativa.

**Por qué este diseño:** El contraste visual entre los tres elementos comunica la narrativa sin texto: izquierda = amenaza (tensión, gris), centro = respuesta (energía, naranja, mayor escala), derecha = resolución (calma, checkmark). El comprador que no lee la frase entiende el argumento por el ícono. Esto complementa la frase dominante sin repetirla.

**Oz ajusta:** Los elementos esquemáticos del mockup (onda sinusoidal, rayo, rectángulo) deben reemplazarse por ilustraciones vectoriales finales en el redline. Oz tiene libertad creativa para refinar la representación siempre que el argumento narrativo en 3 pasos se mantenga.

### 2.4 Tratamiento del dato cuantitativo en la frase dominante

El dato "<0,03 s" se aplica en color #FF8200 a 28px dentro de una frase en #ffffff a 24px. Esto destaca el dato cuantitativo sin romper la continuidad de lectura narrativa. El lector procesa la frase como unidad y el dato se registra como ancla de credibilidad en color naranja.

**Resultado:** la conexión visual "<0,03 s ↔ equipo" está explícita en el copy (es la frase completa), no depende del diseño gráfico. Es la ventaja estructural de C sobre A y B.

### 2.5 Sub-texto compacto

"Sensor NTC* + Protección Inverter incluidos" se coloca en 15px color #888 bajo la frase dominante, con separador de línea de 1px. Es visualmente subordinado — no compite con la frase dominante. Su función es informativa, no de atracción de atención. Oz puede ajustar tipografía pero debe mantener la diferencia jerárquica: mínimo 30% menor en puntos que la frase dominante.

### 2.6 Lengüeta diferenciadora

"EL MÁS RÁPIDO DE LA CATEGORÍA" (Claim J, Bruna §2) diferencia la lengüeta de C respecto a A y B. Para la presentación a Junta, esta diferencia en la lengüeta es un marcador visual inmediato de que C es una propuesta genuinamente distinta. En la comparación side by side, las tres lengüetas son: "LA PROTECCIÓN MÁS COMPLETA" (A y B) vs. "EL MÁS RÁPIDO DE LA CATEGORÍA" (C).

### 2.7 Respiro visual — argumento de C

Con 1 frase dominante + sub-texto, C tiene la mayor área de espacio visual en blanco del set. El espacio entre el bloque de frase dominante y la franja de specs es generoso. Atlas preserva este espacio deliberadamente — llenarlo con elementos adicionales destruiría el argumento visual de la alternativa. Si Oz tiene presión de colocar más elementos, la recomendación es no hacerlo en el tiro de C.

### 2.8 QR — candidata de Solenne para C

Para C se usa la candidata 2 de Solenne: "Descubre cómo protege tu equipo" — más coherente con el tono accesible de esta alternativa. Las candidatas 1 y 3 son más técnicas y van mejor con A y B.

---

## 3. Condiciones de Bruna respetadas

| Condición | Origen | Estado en mockup |
|---|---|---|
| Frase dominante "Actúa en <0,03 s..." (Claim K) | Bruna §2 Claim K | CUMPLIDA — versión completa, sin modificación |
| Lengüeta C "El más rápido de la categoría" (Claim J) | Bruna §2 Claim J | CUMPLIDA — texto literal |
| Asterisco NTC* visible y con remisión al retiro | Bruna §2 Claim D | CUMPLIDA |
| "Protección Inverter" en sub-texto (Claim C) | Bruna §2 Claim C | CUMPLIDA — en sub-texto compacto; el caveat al retiro aplica igualmente |
| Nada con "garantiza la protección" / "evita daños" | Bruna §2 Claim L | CUMPLIDA — "antes de que la fluctuación llegue" no garantiza resultado; describe acción del protector |
| Nada con "protege al motor" / "protege a la carga" | Bruna §2 Claim H | CUMPLIDA |

---

## 4. Riesgos identificados

### 4.1 Riesgo estructural — menor credibilidad para el instalador técnico (PROBLEMA VISUAL ESTRUCTURAL, no táctico)

**Atlas reporta honestamente:** La arquitectura narrativa de C es la más accesible para el consumidor final, pero puede generar fricción con el instalador técnico que evalúa el empaque en punto de venta. La frase dominante "Actúa en < 0,03 s antes de que la fluctuación llegue a tu equipo" es convincente como afirmación de beneficio pero se siente más como promesa de marketing que como especificación técnica. El instalador que ha leído fichas técnicas busca el dato aislado ("< 30 ms") y puede no encontrarlo de inmediato en la estructura narrativa.

**Impacto:** Para el segmento de consumidor final residencial, C es la más fuerte del set. Para el instalador técnico (audiencia primaria del GSM), C puede necesitar validación adicional al voltear el empaque. Esto no es un problema si el retiro presenta las especificaciones claramente, pero el tiro solo tiene el dato embebido en la frase.

**¿Es esto un problema de diseño?** No completamente — Solenne y Vael eligieron la arquitectura narrativa conscientemente. Atlas lo documenta como riesgo estructural de comunicación, no como error de diseño. La Junta debe sopesar si la audiencia primaria del GSM es el instalador técnico o el consumidor final antes de elegir C.

**Severidad:** Estructural de comunicación — relevante para la decisión de Junta. No es un defecto del diseño.

### 4.2 Ícono narrativo requiere refino significativo para el arte final

El ícono narrativo del mockup es funcional como referencia visual para la Junta, pero requiere trabajo de ilustración significativo para alcanzar calidad de imprenta. Es el elemento más elaborado del set de tres mockups. Oz necesita tiempo adicional para el redline de C comparado con A o B.

**Severidad:** Táctico de producción.

### 4.3 Lengüeta "El más rápido de la categoría" — expectativa más amplia

Como Solenne documenta en SO-1, esta lengüeta genera expectativa de velocidad en cualquier contexto (sobre/subtensión severa), mientras que la acotación a parpadeos desaparece del tiro. El caveat al retiro lo corrige, pero el tiro genera una promesa más general. El instalador técnico puede notar la diferencia. Para el consumidor final, esto no es problema.

**Severidad:** Táctico de comunicación. Documentado en SO-1 y en este spec.

### 4.4 Sub-texto compacto puede quedar invisible en blíster real

"Sensor NTC* + Protección Inverter incluidos" en 15px y color #888 es visible en el mockup digital a 800px. En el blíster físico a tamaño real, 15px puede ser demasiado pequeño para consumidores mayores o en condiciones de iluminación de ferretería. Oz debe verificar legibilidad en prueba de impresión antes de aprobar. Si no es legible, el cuerpo mínimo del sub-texto es 12px sin reducción de color.

**Severidad:** Táctico de producción.

### 4.5 Adaptación a otros 3 modelos

Idéntico a A: mismo layout para GSM-MB / RF / RE, paleta y datos de HDE por modelo.

---

## 5. Pendientes para Oz (redline final)

1. Igual que A y B: logo, imagen de producto, tipografía Futura si aplica, datos de specs, adaptación 4 modelos, CMYK + sangrado.
2. **Específico C:** Refinar el ícono narrativo de 3 elementos (onda → rayo → equipo intacto). Oz tiene libertad creativa para el estilo ilustrativo siempre que la narrativa de 3 pasos se mantenga. Sugerencia: ícono en trazo fino estilo técnico-limpio, coherente con el lenguaje visual del brand kit Exceline Profesional.
3. **Específico C:** Verificar legibilidad del sub-texto compacto en blíster físico a tamaño real.
4. **Específico C:** Confirmar que en el blíster físico real la frase dominante en tipografía mínima 20px se mantiene íntegra en 2 líneas. Si no, usar la versión reducida "dañe" aprobada por Bruna — notificar a Solenne y Aurelio si se produce ese ajuste.
5. Para el QR de C: usar la candidata de Solenne 2 "Descubre cómo protege tu equipo" (más coherente con el tono de la alternativa).

---

## 6. Notas de producción

- Condición de datasheet I&D idéntica a A y B (ver A_spec §6).
- La frase "Actúa en < 0,03 s antes de que la fluctuación llegue a tu equipo" usa el verbo "llegar" en lugar de "dañar". Oz no puede cambiar este texto por la versión "dañe" sin que Solenne y Bruna confirmen el cambio — aunque Bruna ha indicado que el argumento no cambia, el texto exacto debe ser autorizado antes de imprimir.

---

*Atlas — Static Visual Production Lead — Sistema /RAUL/*
*Spec emitido: 2026-05-03*
