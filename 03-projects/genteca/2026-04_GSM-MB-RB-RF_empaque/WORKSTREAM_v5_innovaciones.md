# Workstream v5 — Definición final de empaque GSM (innovaciones NTC + < 30 ms)

**Abierto:** 2026-05-03
**Última actualización:** 2026-05-03 (post-carga de materia prima + decisiones Owner sobre claims, QR, mockups)
**Owner del workstream:** Raoul Bermúdez
**Estado:** materia prima cargada en `00-brief/`. Listo para despacho Vera + Orlan.

---

## Scope

Cerrar la definición del empaque GSM-MB / GSM-RB / GSM-RF / GSM-RE en cuanto a **qué beneficios y características se colocan**. El desarrollo de comunicación para otros medios (post, video, ficha técnica, argumentario de ventas, campaña trifásica) queda **fuera de este workstream** — se atiende después con sus propios proyectos.

## Decisión a producir

**Dos alternativas A / B de copy + arte de empaque** que la Junta Directiva pueda comparar y elegir, cada una sustentada con ventajas y desventajas explícitas.

- **Alternativa A (ancla)** — propuesta cerrada por José Miguel Canudas + Raoul vía WhatsApp 02-05-2026:
  - Lengüeta tiro: **"Nuevo. La Protección más completa"**
  - Frase 1: **"El más rápido ante parpadeos (< 0,03 s)"**
  - Frase 2: **"Protege tecnología Inverter"**
  - Frase 3: **"Sensor NTC incorporado*"** (asterisco con explicación al retiro)
- **Alternativa B (contrastante)** — Solenne la construye con un eje diferenciador (jerarquía distinta, una frase reemplazada por opción más emocional, o reducción a 2 frases para mayor respiro visual). Debe ser genuinamente distinta, no cosmética.

Ambas alternativas deben comunicar las dos innovaciones decididas en la reunión Junta previa al 29-04-2026:

1. **Sensor NTC incorporado** — autoprotección térmica.
2. **Tiempo de desconexión < 30 ms** (mejorado desde 150 ms) — fortaleza para proteger equipos inverter.

**Output final esperado para Junta:**

- Memo ejecutivo (Aurelio AU-1) con A vs B + ventajas/desventajas + recomendación.
- Mockup de **arte final** del frente (tiro) para A y para B — prioridad alta.
- Mockup de arte final del retiro para A y para B — preferible. Si la producción de arte demora, retiro puede entregarse como **layout de copy estructurado** (texto sobre wireframe) y dejar arte final pendiente para post-decisión Junta.
- Memo lateral evaluando idea del QR (ver §QR abajo).

## Encuadre técnico (insumo Vera + Bruna — no es copy de empaque)

El equipo tiene dos innovaciones que se suman a sus funciones tradicionales. Para no sobreprometer ni confundir al consumidor técnico, el copy de empaque debe respetar este encuadre:

### Innovación 1 — Sensor NTC (autoprotección térmica)

- **Qué hace:** protege al circuito y al protector mismo de la circulación de corrientes excesivas por encima de los valores nominales del protector, de la carga para la que está diseñado, y de los cables (que deberían estar dimensionados para la carga nominal más el overload normal).
- **Posición frente a otras protecciones del circuito:**
  - El **interruptor termomagnético** sigue siendo la protección del circuito.
  - El **protector de voltaje** sigue siendo el que protege la calidad del voltaje que llega a la carga (aire acondicionado / compresor / motor).
  - El supervisor con NTC actúa como **respaldo** (no reemplazo) del termomagnético: una corriente excesiva dispara la protección por calentamiento → protege al protector mismo y a la instalación (cables, conexiones).
- **Límite explícito a comunicar (no en empaque, sí en sustento):** una carga pequeña que no genera mucha corriente de consumo **no queda protegida térmicamente** por este NTC, porque no alcanza los valores de corriente excesiva que dispararían el calentamiento. Si esa carga pequeña es vulnerable (ej. un equipo de aire), el NTC no la salva del daño por otras causas.

**Implicación para copy:**
- "Autoprotección térmica" es la formulación técnicamente honesta (el NTC protege al equipo mismo).
- Cualquier afirmación de que "protege al motor" o "protege a la carga" es **rechazada** (ya está en v4 §4 textos prohibidos).
- "Respaldo del termomagnético" puede mencionarse en sustento de Junta y en argumentario de ventas, pero **no en empaque** (sobrecomplica el mensaje al consumidor).

### Innovación 2 — Tiempo de respuesta < 30 ms

- Mejora de 150 ms → < 30 ms.
- Diferenciador real frente a competencia (TQ, Protector — pendiente confirmar con Víctor / Luis González).
- Especialmente relevante para equipos con tecnología inverter y cargas de arranque corto: respuesta más rápida = mejor protección sin disparos falsos en arranques de ciclo corto.

**Implicación para copy:**
- Dato cuantitativo verificable (< 30 ms / < 0,03 s) puede ir en empaque sin asterisco si I&D lo respalda con dato medido.
- Vínculo con "inverter" es el ángulo más diferenciador para segmento técnico.

---

## Regla de gateo de claims superlativos (Bruna + Orlan)

Decisión Owner 2026-05-03 — aplica a este workstream y se eleva como precedente:

- Si Orlan **no encuentra evidencia firme** de competidor venezolano con tiempo de respuesta verificablemente < 30 ms → asumir que **Genteca es el único / el más rápido**. Razonamiento Owner: muchos competidores publican valores no verificados; Genteca tiene laboratorio para refutar si alguien reta el claim.
- Las dos formulaciones permitidas son **"el único"** o **"el más rápido"**.
- Formulación **prohibida**: "uno de los más rápidos" — Owner: "eso es ser uno del montón y somos los líderes en innovación".
- "El más rápido ante parpadeos (< 0,03 s)" combina superlativo + dato cuantitativo: aceptable en empaque si Orlan no halla contradicción. El dato cuantitativo respalda y puede defenderse incluso si el superlativo se cuestiona.
- Bruna emite BR-2 con esta política y registra precedente en `04-system/03-governance/`.

---

## QR dinámico — alcance ampliado y evaluación a producir

Idea Owner 2026-05-03 (ampliada): el QR no se limita a explicar NTC. El QR es la **vía única para explicar todas las innovaciones del producto** — funciona como puerta de entrada al ecosistema completo de información del lanzamiento.

**Temas que debe cubrir el destino del QR (landing / video / sección web Genteca):**

1. **Tiempo de respuesta < 0,03 s** — qué es un parpadeo, por qué la velocidad importa, comparación contra el estándar previo de 150 ms.
2. **Protege tecnología inverter** — por qué la electrónica inverter es sensible, cómo la respuesta ultra-rápida la protege.
3. **Sensor NTC incorporado** — qué es, dónde está ubicado, qué detecta.
4. **Protección térmica del protector y la instalación** — calentamiento por sobrecorriente, bornes flojos, falsos contactos.
5. **Protección de cables** — el dimensionamiento del cableado y por qué el NTC lo respalda.
6. **Protección de cargas grandes** — el matiz técnico del rango ≈ 20 A donde el NTC también respalda al equipo, y la honestidad de que para cargas pequeñas no.

**Restricción técnica resuelta:** los QR son **dinámicos** (URL de destino editable post-impresión). El destino puede arrancar como landing temporal de lanzamiento y migrar a la web general de Genteca cuando el lanzamiento cierre. Sin riesgo de QR roto.

**Lo que el pipeline debe evaluar (memo lateral, no decisión ejecutada):**

1. **¿QR específico nuevo o aprovechar el QR existente del empaque?** — el empaque ya trae un QR genérico. Opciones:
   - (a) Añadir QR nuevo con frase llamativa al lado ("Conoce las innovaciones", "Descubre por qué", etc.) — más visible, riesgo de saturación.
   - (b) Mantener el QR existente y agregarle una frase llamativa que indique que ahora lleva al material de innovaciones — sin saturación visual, riesgo de confundir si el QR existente ya cumplía otra función.
   - (c) Reemplazar el destino del QR existente por la nueva landing (uso de su naturaleza dinámica) — limpio operativamente, depende de qué cumple hoy.
2. **Posición y tamaño** — si se opta por (a), tamaño mínimo legible y posición que no compita con los claims principales.
3. **Frase de invitación** — Solenne propone 2-3 candidatas para acompañar al QR (ej. "Conoce las innovaciones", "Descubre el porqué", "Tecnología explicada aquí").
4. **Impacto sobre A vs B** — ¿el QR va en ambas alternativas (constante), solo en una para diferenciar, o se entrega como variable independiente que Junta decide aparte del copy?
5. **Riesgos** — saturación visual del frente · usuario escanea QR equivocado · vida útil de la landing temporal antes de migrar a web Genteca · gobernanza del destino dinámico (quién puede cambiar la URL y bajo qué control).

**Output:** memo de Aurelio + Vael con recomendación clara. Bruna comenta riesgo si aplica.

---

## Pipeline CSC para este workstream

| Paso | Agente | Output | Estado |
|---|---|---|---|
| 1 | Owner (Raoul) | Carga materia prima en `00-brief/` (innovaciones, transcripciones, WhatsApp, mercado, specs I&D). | 🔄 EN CURSO |
| 2 | Vera | Brief técnico consolidado de las dos innovaciones — qué se puede afirmar con qué evidencia, qué no. Output a `00-brief/` o `01-strategy-and-design/`. | ⏳ PENDIENTE |
| 3 | Orlan | Análisis competencia tiempo de respuesta + mensaje NTC en mercado venezolano. Output a `01-strategy-and-design/`. | ⏳ PENDIENTE |
| 4 | Vael | VA-1 messaging framework + VA-5 guardrails (claims defendibles ✅ / con caveat ⚠ / prohibidos ❌). Output a `01-strategy-and-design/`. | ⏳ PENDIENTE |
| 5 | Bruna | BR-1 risk note sobre el set de claims propuesto + BR-2 decisión de gate. Output a `_governance/`. | ⏳ PENDIENTE |
| 6 | Solenne | SO-1 dos alternativas A / B de copy de empaque con ventajas/desventajas. Output a `02-production/`. | ⏳ PENDIENTE |
| 7 | Aurelio | AU-1 nota ejecutiva para Junta Directiva: dos alternativas + recomendación. Output a `03-review-and-release/`. | ⏳ PENDIENTE |
| 8 | Owner | Lleva a Junta. | ⏳ PENDIENTE |
| 9 | Solenne / Oz | Aplicar decisión de Junta → delta v5 + email a Ozwaldo. Output a `03-review-and-release/`. | ⏳ PENDIENTE |
| 10 | Ozwaldo | Implementa en arte. PDFs revisados. | ⏳ PENDIENTE |
| 11 | Keiddys | Aprobación final. Mover a `04-published-and-hand-off/`. | ⏳ PENDIENTE |

## Libertad creativa para los agentes (decisión Owner 2026-05-03)

Aunque la entrega comprometida a Junta Directiva son **dos alternativas A / B**, los agentes del pipeline tienen libertad para proponer **más allá de A y B** si surge una idea creativa que valga la pena. Owner: "necesitamos que los agentes también sean creativos. Aunque pedimos dos propuestas, pueden sentirse en libertad de proponer para que la creatividad no se corte". Aplica especialmente a Vael (jerarquía / framing), Solenne (formulación de frases), Atlas (composición visual), Oz (redline final).

Si surge propuesta extra:
- Va clara y separada como **Alternativa C** (o más).
- Cada alternativa adicional debe argumentar su razón de ser distinta a A y B.
- Aurelio decide en AU-1 si la lleva a Junta como tercera opción o la guarda como reserva.

## Vinculación gráfica creativa < 0,03 s ↔ tecnología inverter (decisión Owner 2026-05-03)

Owner pide explícitamente: "que en el empaque, de alguna forma gráfica creativa, podamos vincular lo de < 0,03 segundos con protección ideal para tecnología inverter".

- Es brief para **Atlas** (composición visual) y **Oz** (redline final): el frente del empaque debe transmitir visualmente que el dato cuantitativo y el claim de inverter están conectados — no como dos badges sueltos al lado uno del otro.
- Solenne puede proponer frases conectivas si el copy lo necesita.
- Vael construye el message framework asumiendo esta conexión como pilar central.

## TQ — investigación complementaria no bloqueante

Owner 2026-05-03: vale la pena que Paxs investigue si el OEM real detrás de TQ publica algún dato de < 30 ms. **No bloquea el pipeline.** Si TQ publica un valor menor, no cambia la decisión Owner de comunicarnos como "el más rápido / único" — cambia el riesgo defensivo si alguien reta. Despacho Paxs en background.

## Datos técnicos confirmados por Owner / I&D (2026-05-03)

Insumo crítico para gate Bruna y para Solenne:

1. **Tiempo de respuesta < 30 ms — medición formal:** confirmado por I&D Genteca como medición formal del laboratorio. El claim "< 0,03 s" tiene respaldo técnico documentado. Cierra la condición bloqueante P-2 de Vera.
2. **Hojas de especificación de los 4 modelos** disponibles en `00-brief/specs-i-d/`:
   - `20240515_GSM-MB_HDE_V7.pdf`
   - `20240515_GSM-RB_HDE_V7.pdf`
   - `GSM-RF_HDE_V8.pdf`
   - `GSM-RE_HDE_V8.pdf`
   - **Caveat Owner:** el tiempo de respuesta a parpadeos publicado en estas HDE es de los **modelos anteriores** (150 ms). El valor real medido para los modelos nuevos es < 30 ms, ya corroborado con I&D pero aún no actualizado en HDE pública. Cierra la condición bloqueante P-1 de Vera (nominales por modelo). Pendiente operativo: I&D actualiza HDE en paralelo al lanzamiento del empaque.
3. **Temperatura de disparo del NTC = 60 °C:**
   - El relé de salida es el elemento más sensible y 60 °C es suficiente para protegerlo.
   - Temperatura ambiente máxima de instalación: 55 °C.
   - Mecanismo: si la temperatura interna se eleva a 60 °C por alto nivel de corriente o por contactos deficientes (puntos calientes en conexiones), el NTC abre el circuito.
   - Este es el dato cuantitativo defensivo del asterisco NTC.
4. **Alternativa C confirmada por Owner.** A la entrega de Junta van **A (Canudas / ratificada Owner) + B (Solenne contrastante) + C (Vael narrativa causa-efecto)**. Aurelio AU-1 las presenta en paralelo, no como ranking.

## Disclaimer breaker termomagnético — ya implementado + venta cruzada Exceline (aclaración Owner 2026-05-03 post-Bruna)

Aclaración Owner: el disclaimer **"No reemplaza los breakers termomagnéticos de la instalación eléctrica"** ya está incorporado en INFORMACIÓN DE SEGURIDAD del retiro desde delta v3 (ratificado sin cambio en delta v4). Texto literal verificado.

Implicación para la cadena:
- **Solenne (SO-1):** preserva ese texto literal en ambas alternativas A / B / C. No lo reescribe. Es disclaimer aprobado en rondas anteriores y buena práctica de instalación eléctrica.
- **Bruna:** el flag de "redacción del bloque del retiro / asterisco NTC" sigue vigente para la parte NTC, pero la cláusula del breaker está cerrada upstream y solo debe respetarse.

**Dimensión estratégica nueva — venta cruzada Exceline Profesional:**

Exceline Profesional tiene **breakers termomagnéticos** en catálogo. Esto convierte el disclaimer "no reemplaza al breaker termomagnético" de defensa legal en **palanca comercial**: el consumidor que lee la advertencia descubre que la marca cubre ambos productos. Implicaciones:

- **Para Aurelio (AU-1 a Junta):** la regla de gateo Bruna sobre "respaldo del breaker termomagnético solo off-empaque" gana fuerza estratégica — el QR / landing del lanzamiento puede incluir un módulo de "instalación completa con Exceline" que vincule supervisor + breaker + (otros productos línea). Es venta cruzada documentada.
- **Para el QR ampliado (los 6 temas):** añadir tema 7 — "Instalación completa con Exceline Profesional: breaker termomagnético + supervisor de voltaje GSM" — mostrando cómo se complementan.
- **Para Solenne / Vael off-empaque:** en argumentario de ventas y video explicativo, el caveat técnico ("no reemplaza al breaker, lo respalda") cierra con "y si necesitas el breaker, también lo hacemos en línea Exceline Profesional".
- **No para empaque (frente):** sigue prohibido por Bruna (B descartado, "el único en proteger inverter" descartado, comparativos de marca prohibidos). El frente del empaque mantiene foco en innovaciones GSM.

Esta aclaración no cambia el gate de Bruna de los claims del frente — refuerza la decisión de mantener el "respaldo del termomagnético" off-empaque y abre dimensión comercial que Aurelio debe presentar a Junta.

## Refresh 2026-05-04 — datos nuevos de Canudas, Liliam I&D, reunión Kike

Insumos nuevos:
- `00-brief/whatsapp/Chat con Jose Miguel Canudas 2.txt` (refinamiento técnico NTC).
- `00-brief/whatsapp/Chat con Liliam I&D.txt` (corrige umbral NTC, aporta dato verificado de Breakermatic).
- `00-brief/transcripts/Meeting Transcription 04-05-2026.txt` (reunión Kike — ideas para Alternativa D).

### Correcciones técnicas que se aplican a las 4 alternativas (A, B, C, D)

1. **Asterisco NTC reescrito (fix técnico obligatorio):**
   - **Olvidar** "60 °C internos" del bloque Bruna §3.3 — ese dato fue error de comunicación del Owner, no confirmado por Liliam I&D.
   - Owner explícito: **no comunicar temperaturas en empaque**.
   - El NTC dispara cerca de 132 °C internos junto al pin del relé; el relé se daña a 140-145 °C; a 132 °C la instalación (cables y bornera) se mantiene segura.
   - Reformulación del asterisco: el sensor NTC ubicado junto al relé de potencia detecta calentamiento por sobrecorriente o conexiones deficientes y desconecta la carga **antes de que cables o conexiones de los bornes se dañen**. Protege al protector mismo y a la instalación. Para cargas pequeñas no actúa como protección de sobrecarga directa de la carga. No reemplaza al interruptor termomagnético.
   - Cables THW se dañan a partir de 75 °C, TW a 60 °C — la T° crítica se alcanza **en el área de los bornes de conexión** (no del relé directamente) por corriente alta o falsos contactos. El NTC abre antes.

2. **Curva de tiempo inverso:** el NTC arma una curva de disparo de tiempo inverso similar a un breaker pero un poco más lenta — esto refuerza que el termomagnético queda como último elemento de maniobra. Va al sustento técnico del QR, no al frente del empaque.

### Datos competitivos actualizados (corrige Orlan v1)

Liliam I&D confirma (verificado en laboratorio Genteca):
- **Breakermatic: 32-64 ms (50 ms típico)** — la competencia más cercana.
- Genteca: **20-30 ms en laboratorio** (16-32 ms teórico).

Esto cambia el panorama:
- **"El más rápido del mercado" sigue defendible** (somos más rápidos que Breakermatic).
- **"10 veces más rápido" no es universalmente defendible** — contra Breakermatic somos ~2x. Contra el resto del mercado (WellSpec 200-300 ms, Powest 1.000 ms, etc.) sí 10x o más.
- **Owner decisión 2026-05-04:** usar formulación **"Hasta 10 veces más rápido"** (es máximo, no promedio — defendible).
- **Argumento "competidores con tiempos > 100 ms no protegen auténticamente inverter":** queda **off-empaque**, en argumentario de la fuerza de ventas. No es claim defensible en empaque por riesgo comparativo, pero sí es munición legítima para ESC en campo donde la guerra competitiva del día a día permite argumentación más libre.

### Pilar "auténticamente inverter" — flickers vs picos (refresh Vael)

Argumento Owner reunión Kike + Liliam: la electrónica inverter ya trae supresores para picos de alta energía de fábrica. **Lo que daña la electrónica inverter son los flickers** (voltaje cero / arriba / cero / arriba en fracciones de segundo), no los picos. Solo respuesta sub-30 ms corta el flicker antes de daño. Genteca es el único con < 30 ms verificable → único que protege auténticamente inverter.

Acción: Paxs investiga características técnicas de equipos inverter (supresores de pico de fábrica, sensibilidad a flickers, qué exactamente daña la electrónica) para fundamentar narrativa honesta del QR + argumentario ESC.

### Alternativa D (nueva, no sustituye A/B/C)

Destila ideas de la reunión Kike 04-05-2026:
- **QR arriba**, no abajo, junto a los 3 claims principales.
- **Lengüeta:** "Nuevo. Averígualo" (curiosidad activada por la palabra "nuevo" + invitación a escanear).
- **3 claims con flecha conectora gráfica** que muestre cadena causal: < 0,03 s (o "Hasta 10 veces más rápido") → auténticamente protege inverter → además protege contra calentamiento (NTC).
- "Hasta 10 veces más rápido" como claim distintivo de D (eje propio — no se aplica a A/B/C salvo que Junta lo elija).
- QR como puerta a 7 temas + nuevo tema 8: argumento flickers vs picos + por qué somos los únicos que protegen auténticamente inverter.

### QR — destino mínimo garantizado (aclaración Owner 2026-05-04 post-Atlas v2)

Aclaración Owner: el QR **nunca apuntará a un lugar vacío**. Destino mínimo garantizado: **sección de productos GSM en genteca.com.ve** (página web institucional vigente, ya tiene contenido sobre la línea). Como el QR es dinámico, en cualquier momento posterior al lanzamiento puede redirigirse a:
- Landing dedicada del lanzamiento (con material destilado de Paxs sobre flickers vs picos).
- Video explicativo en YouTube.
- Recurso técnico específico para ESC.
- O combinación de ellos.

**Resuelve flag operativo bloqueante de D** que Atlas v2 marcó: la decisión sobre el destino del QR no bloquea la imprenta. Si Junta elige D, el QR puede ir a producción con destino inicial = página web Genteca, y migrar a landing dedicada cuando esté lista — sin necesidad de re-imprimir empaque.

### Estrategia QR ampliado — ESC + audiencias técnicas

Decisión Owner 2026-05-04: el QR es la vía principal para comunicar lo que no cabe en el empaque. Especialmente:
- Para **ESC (fuerza de ventas)** y audiencias técnicas, el QR debe llevar argumentos sin restricciones legales del empaque — la guerra competitiva del día a día permite mayor libertad argumentativa.
- Lo que sea fácil de comunicar en empaque, repetir en QR.
- Lo que no sea fácil de comunicar en empaque, **es obligatorio** preparar argumentos completos detrás del QR.

## Decisiones cerradas

- Scope productos: **GSM-MB, GSM-RB, GSM-RF, GSM-RE** (4 modelos, copy idéntico salvo color/aplicación).
- Innovaciones a comunicar: **NTC + < 30 ms** (decisión 29-04-2026).
- "NTC" siempre con asterisco si aparece textual en empaque (decisión v4).
- Ningún claim del tipo "protege al motor" o "protege a la carga".
- **Estatus de mercado de los productos con innovaciones (aclaración Owner 2026-05-03 post-Vera/Orlan):** los productos con sensor NTC y < 30 ms son **nuevos y aún no están publicados** en la página web de Genteca ni en datasheets públicos. Por lo tanto:
  - No existe discrepancia real entre el dato de empaque (< 30 ms) y datos publicados (que dicen 150 ms): los datasheets vigentes corresponden a versiones anteriores del producto.
  - El pendiente "P-2 actualizar datasheets antes del lanzamiento" (Vera) sigue siendo válido como acción coordinada con I&D para que datasheets nuevos se publiquen en paralelo al empaque, pero **no es un riesgo activo de exposición de claim** mientras el producto nuevo no esté en mercado.
  - El claim "< 0,03 s" en empaque puede formularse sin temor a contradecir información pública previa, porque la información pública previa es de productos viejos.

## Pendientes de afuera del CSC (no bloqueantes para este workstream)

- Datos comparativos de tiempo de respuesta vs competencia (Víctor, Luis González) → alimenta argumentario de ventas, **no** este workstream.
- Concepto de campaña línea trifásica (Alberto) → workstream nuevo separado.

## Cierre del workstream

Este workstream cierra cuando:
1. La Junta Directiva elige una de las dos alternativas (o pide ajuste).
2. La alternativa elegida se traduce en delta v5 + arte aprobado por Keiddys.
3. Los archivos finales están en `04-published-and-hand-off/`.
4. README del proyecto se actualiza marcando empaque como cerrado.
