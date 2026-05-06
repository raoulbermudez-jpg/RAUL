# VA-5 Update Flash — Naming Función Térmica (Alternativa B sin NTC)
**Documento:** Vael_VA-5_naming-funcion-termica_v1
**Fecha:** 2026-05-05
**Tipo de output:** VA-5 update flash — tabla de naming + texto de asterisco para retiro
**Scope:** Alternativa B del empaque Exceline GSM-MB / GSM-RB / GSM-RF / GSM-RE, tiro (badge de función térmica) + retiro (asterisco)
**Trigger:** Decisión de Junta Directiva a favor de Alternativa B (dos claims en tiro: velocidad + función térmica). Observación de José Miguel Canudas: "Sensor NTC incorporado" revela secreto industrial sin agregar beneficio percibido al comprador.
**Insumos consumidos:** Vael_messaging_framework_v1 (VA-1 + VA-5, 2026-05-03) · Bruna_gate_empaque_v1 §2 Claim D/E + §7.1 Refresh (2026-05-04) · Aurelio_AU-1_memo_junta_v2 §2 Alt B (2026-05-04) · Vera_brief_tecnico_v1 §1.1–§1.4 + §4 (2026-05-03)
**Para:** Bruna (gate), Solenne (ejecución SO-1 delta), Aurelio (update AU para Junta)
**Status:** PROPUESTA — ningún claim aquí aprobado. Gate de Bruna requerido antes de pasar a Solenne / Oz.

---

## Contexto de la solicitud

La Junta elige Alternativa B. El tiro de B tiene dos claims:
1. "El más rápido ante parpadeos (< 0,03 s)" — sello BR-2 vigente.
2. Badge de función térmica — **a reemplazar**. El badge original ("Sensor NTC incorporado*") está aprobado por Bruna (Claim D, §2) pero la observación de Canudas en Junta abre una vía de mejora legítima: no mencionar el componente por nombre, sino la función o el beneficio.

El Owner acepta como piso "sensor de temperatura" o "sensor digital", pero pide explorar formulaciones que revelen menos tecnología interna y hablen más de función / beneficio.

---

## Criterios aplicados a cada alternativa

| # | Criterio |
|---|---|
| 1 | Cero revelación del componente específico (NTC, termistor, termoresistencia) |
| 2 | Lenguaje de función / beneficio, no de componente |
| 3 | Compatible con el asterisco de retiro actualizado (Bruna §7.1 — sin temperatura numérica) |
| 4 | Audiencia primaria B: instalador técnico (lee retiro) + consumidor residencial (solo ve tiro) |
| 5 | ≤ 4 palabras preferible — jerarquía con "El más rápido ante parpadeos" |
| 6 | Sin introducir tono nuevo — coherencia con VA-1 y lengüeta "Nuevo / La protección más completa" |
| 7 | Cero promesa de protección del motor / la carga (prohibición Vera §1.4 + Bruna Claim H) |

---

## Tabla de finalistas (5 opciones)

---

### Opción 1 — "Autoprotección térmica activa" ⚠

**Texto exacto para tiro:** Autoprotección térmica activa*

**Texto del asterisco para retiro:**

> Sensor de temperatura ubicado junto al relé de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se dañen. Protege al protector mismo y a la instalación eléctrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actúa como protección de sobrecarga directa de la carga conectada. No reemplaza al interruptor termomagnético de la instalación.

**Pros:**
- "Auto" preserva la idea central del VA-1 Pilar 3: el protector se protege a sí mismo. Esa semántica es la que corrige el malentendido del 40% del mercado (Orlan §6.3).
- "Activa" añade una dimensión de dinamismo (no es una protección pasiva). Diferencia perceptualmente de "protección térmica" genérica.
- No revela componente. Ningún competidor usa esta formulación (Orlan Sección 3).
- Compatible directamente con el Claim E de Bruna ya aprobado ("Autoprotección térmica" — aprobado sin gate adicional), que solo requiere adaptación menor del texto de retiro conforme §7.1.
- Cuatro palabras. Encaja en jerarquía con el badge de velocidad.

**Contras:**
- "Activa" como adjetivo de función puede parecer un pleonasmo técnico para el instalador experto (¿qué protección térmica no es activa?). Riesgo bajo pero presente.
- "Autoprotección" sigue siendo un término semi-técnico que el consumidor residencial puede no decodificar de inmediato. Requiere que el asterisco haga todo el trabajo explicativo para ese perfil.

**Riesgo de uso por competencia:** Bajo. El término "autoprotección térmica" no describe el componente; describe la función. Un competidor que lo copiara tendría que implementar la función para sostenerlo — lo cual es el escenario deseable (eleva el estándar de la categoría, no regala un secreto industrial).

**Nivel de revelación tecnológica:** Nulo — función declarada, componente omitido.

---

### Opción 2 — "Detección térmica integrada" ⚠

**Texto exacto para tiro:** Detección térmica integrada*

**Texto del asterisco para retiro:**

> Sistema de detección de temperatura incorporado junto al relé de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes y desconecta la carga antes de que el cableado o las conexiones se dañen. Protege al protector mismo y a la instalación eléctrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actúa como protección de sobrecarga directa de la carga conectada. No reemplaza al interruptor termomagnético de la instalación.

**Pros:**
- "Detección" es precisa funcionalmente: el sistema detecta, no solo reacciona. Comunica que hay un proceso activo de vigilancia.
- "Integrada" comunica que no es una protección externa o añadida después: es parte del diseño. Refuerza la narrativa de producto completo ("La protección más completa").
- Formulación limpia: sin "sensor" en el nombre, sin "NTC", sin termistor. No revela componente ni arquitectura.
- Tres palabras — más compacta que la Opción 1. Da más respiro visual al badge de velocidad en un blister pequeño.

**Contras:**
- "Detección" sin acción puede dejar la pregunta "¿y qué hace cuando detecta?" — el asterisco lo responde, pero el consumidor que no lee el retiro queda con un claim incompleto.
- No tiene el prefijo "auto" que corrige activamente el malentendido de protección del motor. El instalador técnico entiende la diferencia; el consumidor residencial podría no distinguir.
- Más abstracta que la Opción 1. Para el instalador técnico que valora datos concretos, es menos convincente que "autoprotección térmica activa".

**Riesgo de uso por competencia:** Bajo-medio. "Detección térmica integrada" como frase es genérica y podría ser copiada sin implementar la función real. Sin embargo, en el contexto de empaque venezolano donde ningún competidor comunica nada térmico (Orlan Sección 3), cualquier competidor que la copie estaría entrando en el terreno de Genteca, no al revés.

**Nivel de revelación tecnológica:** Nulo — no describe arquitectura ni componente.

---

### Opción 3 — "Protección térmica inteligente" ⚠

**Texto exacto para tiro:** Protección térmica inteligente*

**Texto del asterisco para retiro:**

> Sistema de protección que monitorea la temperatura del relé de potencia en tiempo real. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se dañen. Protege al protector mismo y a la instalación eléctrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actúa como protección de sobrecarga directa de la carga conectada. No reemplaza al interruptor termomagnético de la instalación.

**Pros:**
- "Inteligente" comunica que el sistema responde de forma adaptativa — habla de la curva de tiempo inverso del NTC (a mayor calor, actuación más rápida) sin nombrarlo. Para el consumidor residencial, "inteligente" es un atributo aspiracional y positivo.
- "Protección térmica inteligente" es una frase que funciona para ambas audiencias: el instalador la lee como un sistema con lógica de control; el consumidor la lee como un feature moderno.
- Sin prefijo "auto" pero con "inteligente" hay implícita la idea de respuesta autónoma.
- Sin revelación de componente.

**Contras:**
- "Inteligente" como adjetivo en marketing es un comodín que varias marcas usan con o sin sustento. Para el instalador técnico riguroso puede sonar a marketing más que a especificación.
- "Protección térmica" sin "auto" mantiene el riesgo del 40% del mercado (Orlan §6.3) que lo interpreta como protección del motor. El asterisco mitiga pero no elimina ese riesgo perceptual.
- Tres palabras — igual que la Opción 2, pero "inteligente" podría considerarse un adjetivo vacío si el asterisco no es leído.

**Riesgo de uso por competencia:** Medio. "Protección térmica inteligente" es una frase genérica que podría ser copiada sin implementar el sistema. El término "inteligente" aplicado a hardware puede prestarse a uso sin sustento técnico real por parte de competidores.

**Nivel de revelación tecnológica:** Nulo.

---

### Opción 4 — "Termoprotección integrada" ⚠

**Texto exacto para tiro:** Termoprotección integrada*

**Texto del asterisco para retiro:**

> Sistema de protección térmica incorporado en el circuito de control. Detecta calentamiento excesivo junto al relé de potencia — causado por sobrecorrientes, rotor trabado o conexiones deficientes — y desconecta la carga antes de que el cableado o el protector se dañen. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actúa como protección de sobrecarga directa de la carga conectada. No reemplaza al interruptor termomagnético de la instalación.

**Pros:**
- "Termoprotección" es un sustantivo-concepto que funciona como nombre propio de la función. No es una frase descriptiva: es un término que Genteca puede apropiarse como lenguaje de marca propio.
- La construcción como una sola palabra ("termoprotección") tiene más potencial de recordación y de apropiación de marca que una frase de dos o tres palabras.
- "Integrada" refuerza que no es un add-on externo sino parte del diseño del producto.
- Dos palabras — la más compacta del set. Máximo respiro visual en el blister.
- Sin revelación de componente ni arquitectura.

**Contras:**
- "Termoprotección" es un neologismo técnico que puede sonar a jerga sin anclaje para el consumidor residencial. Sin el asterisco leído, el comprador no sabe qué es.
- Para el instalador técnico, la compactación puede interpretarse como menos información en lugar de más elegancia. El instalador que sabe de NTC puede no encontrar en "termoprotección" la misma señal de sofisticación que en "Sensor NTC incorporado".
- El término carece de la carga semántica de "auto" que protege contra el malentendido de protección del motor.

**Riesgo de uso por competencia:** Bajo. "Termoprotección integrada" describe función sin componente. El beneficio de apropiación como lenguaje de marca supera el riesgo de copia si Genteca establece el término primero en la comunicación de la categoría.

**Nivel de revelación tecnológica:** Nulo.

---

### Opción 5 — "Sensor de temperatura incorporado" ✅ (floor del Owner)

**Texto exacto para tiro:** Sensor de temperatura incorporado*

**Texto del asterisco para retiro:**

> Sensor de temperatura ubicado junto al relé de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se dañen. Protege al protector mismo y a la instalación eléctrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actúa como protección de sobrecarga directa de la carga conectada. No reemplaza al interruptor termomagnético de la instalación.

**Pros:**
- Es el floor explícito del Owner. Si hay cualquier duda en el gate de Bruna, esta es la alternativa sin riesgo conceptual adicional al que ya corría "Sensor NTC incorporado*".
- Completamente literal e inambigua: cualquier audiencia entiende que hay un sensor que mide temperatura. Sin tecnicismo de componente.
- Sin revelación de arquitectura interna. "Sensor de temperatura" puede ser un NTC, un termistor PTC, un bimetal, un termopar o cualquier otro componente — no da pistas al competidor.
- La cadena Bruna ya aprobó la función descrita (Claim D, §2): el cambio es solo de nombre del componente a nombre de la función. Riesgo de gate adicional mínimo.

**Contras:**
- Cuatro palabras — igual que la Opción 1. No es la más compacta.
- "Sensor de temperatura incorporado" es descriptivo pero genérico. No tiene la energía semántica de "autoprotección" ni el carácter de marca de "termoprotección". Es claro pero no memorable.
- Sin el prefijo "auto" ni la carga de "inteligente", este badge no corrige el malentendido del 40% del mercado (Orlan §6.3). El asterisco sigue siendo la única barrera contra esa interpretación incorrecta.
- Es la opción menos diferenciadora en lenguaje: describe el componente genérico, no la función única.

**Riesgo de uso por competencia:** Muy bajo — demasiado genérico para ser imitado con valor diferenciador. Cualquier fabricante puede decir "sensor de temperatura incorporado" sin implementar nada equivalente.

**Nivel de revelación tecnológica:** Nulo en componente, pero implica que existe un sensor activo en el circuito — información mínima y pública por definición.

---

## Tabla resumen de los 5 finalistas

| # | Texto tiro | Palabras | Semántica primaria | Corrige malentendido motor | Revelación tecnológica | Apropiación de marca | Nivel riesgo gate |
|---|---|---|---|---|---|---|---|
| 1 | Autoprotección térmica activa* | 4 | Función autónoma de protección | Sí ("auto") | Nula | Media | Bajo |
| 2 | Detección térmica integrada* | 3 | Vigilancia activa integrada | Parcial | Nula | Baja-media | Bajo |
| 3 | Protección térmica inteligente* | 3 | Feature moderno / adaptativo | Parcial | Nula | Media-baja | Medio |
| 4 | Termoprotección integrada* | 2 | Concepto-marca compacto | No | Nula | Alta | Bajo |
| 5 | Sensor de temperatura incorporado* | 4 | Descripción funcional plana | No | Nula | Nula | Mínimo |

---

## Ranking de Vael (top 3)

### #1 — Opción 1: "Autoprotección térmica activa*"

**Razón:** Mejor equilibrio entre precisión técnica para el instalador y comprensión para el consumidor. El prefijo "auto" es el único elemento semántico que resuelve activamente el malentendido del 40% del mercado sin necesidad de que el asterisco sea leído. "Activa" no es pleonasmo en el contexto del blister: diferencia de protecciones pasivas (como el supresor de picos MOV que absorbe el transiente) frente a una protección que monitorea y actúa. Compatible sin gate adicional con el Claim E de Bruna ya aprobado ("Autoprotección térmica" — aprobado §2). El ajuste de "activa" como adjetivo requiere confirmación mínima de Bruna pero no cambia la categoría del claim.

### #2 — Opción 4: "Termoprotección integrada*"

**Razón:** Si el objetivo es apropiación de marca a largo plazo, "termoprotección" como sustantivo-concepto es la apuesta más rentable. Dos palabras liberan espacio visual para que el dato "< 0,03 s" domine visualmente en el blister de B (eje de la arquitectura visual que pide AU-1 v2). La compacidad tiene costo: requiere que el retiro haga más trabajo explicativo para el consumidor residencial. Para la audiencia primaria de B (instalador técnico que lee retiro), ese costo es tolerable.

### #3 — Opción 5: "Sensor de temperatura incorporado*"

**Razón:** Floor explícito del Owner. Requiere el menor esfuerzo de gate porque es la opción con menor ambigüedad interpretativa y con la función ya aprobada por Bruna (Claim D). Si el tiempo antes de la Junta de mañana no permite un gate completo de las opciones 1 a 4, la Opción 5 puede avanzar con certeza. Es conservadora pero honesta y defendible.

---

## Opciones descartadas del análisis previo del Owner (con razón)

| Formulación | Por qué descartada |
|---|---|
| "Sensor NTC incorporado*" | Revela componente (NTC). Origen del problema. |
| "Sensor digital incorporado*" | "Digital" sugiere componente de procesamiento específico — puede ser más revelador que NTC para un competidor técnicamente competente. Descartado por criterio del Owner. |
| "Protección térmica" (sin calificador) | Anti-mensaje explícito en VA-1 §4 punto 2: el 40% del mercado lo interpreta como protección del motor. Descartado sin excepciones. |
| "Cuida tu equipo del calor" | Lenguaje de beneficio que sugiere protección de la carga — límite peligroso con Claim H rechazado (Bruna). Demasiado cercano a "protege al motor". |
| "Apaga ante calor extremo" | Describe la acción correctamente pero "apaga" puede confundirse con la función de desconexión por voltaje (que ya es la función base del protector). Ambigüedad funcional. |

---

## Gate de Bruna requerido antes de producción

| # | Opción | Categoría propuesta Vael | Condición de gate |
|---|---|---|---|
| 1 | "Autoprotección térmica activa*" | Defendible con caveat | Bruna confirma que añadir "activa" al Claim E aprobado no cambia la categoría de riesgo. Texto de retiro §7.1 Refresh Bruna aplica intacto. |
| 2 | "Detección térmica integrada*" | Defendible con caveat | Claim nuevo. Bruna evalúa si "detección" sin "autoprotección" introduce riesgo de interpretación de protección del motor. |
| 3 | "Protección térmica inteligente*" | Defendible con caveat — riesgo medio | Bruna evalúa "inteligente" como adjetivo (¿sustentable técnicamente?). Evalúa riesgo del 40% de malentendido de protección del motor por ausencia de "auto". |
| 4 | "Termoprotección integrada*" | Defendible con caveat | Neologismo. Bruna evalúa si requiere más explicación en retiro para ser sostenible como claim en empaque. |
| 5 | "Sensor de temperatura incorporado*" | Defendible (floor Owner) | Mínimo. Bruna confirma que sustitución de "NTC" por "de temperatura" no afecta la categoría del Claim D previamente aprobado. |

**Prioridad de gate:** si el tiempo es restringido antes de la Junta de mañana, la secuencia mínima es:
- Gate rápido de Opción 5 (floor Owner, extensión de Claim D ya aprobado) — desbloqueante mínimo.
- Gate de Opción 1 (top ranking Vael, extensión de Claim E ya aprobado) — desbloqueante preferido.

---

## Texto del asterisco de retiro — versión unificada para todas las opciones

El texto del asterisco es funcionalmente idéntico para las cinco opciones (el hecho técnico no cambia; solo cambia el badge del tiro). Se presenta en dos variantes según el espacio disponible en retiro.

### Versión condensada (empaque — mínimo obligatorio)

El texto siguiente es la adaptación de Bruna §7.1 Refresh (texto corregido, sin temperaturas numéricas), ajustado para que no mencione "NTC" en el badge del retiro. Es compatible con todas las opciones de naming y reemplaza al §3.3 original de Bruna para la arquitectura B.

> **[Badge elegido — ver tiro]:** sensor de temperatura ubicado junto al relé de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que cables o conexiones de los bornes se dañen por calentamiento. Protege al protector mismo y a la instalación eléctrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actúa como protección de sobrecarga directa de la carga conectada. Funciona como capa adicional de protección térmica; no reemplaza al interruptor termomagnético de la instalación.

**Nota de implementación para Oz / Solenne:** reemplazar "[Badge elegido — ver tiro]" por la formulación exacta que Bruna apruebe para el tiro. El resto del texto es invariable.

### Versión completa (retiro amplio / QR / argumentario)

Si el retiro tiene espacio, usar la versión §3.4 corregida de Bruna (§7.1 Refresh), adaptando únicamente la primera línea para no mencionar "NTC" como nombre del componente — sino como "sensor de temperatura junto al relé de potencia". El cuerpo de §3.4 Refresh es completamente válido sin modificación adicional.

---

## Supuestos y límites

**Insumos aguas arriba que sostienen este documento:**

- Vera: Vera_brief_tecnico_v1.md — §1.1–§1.4 (mecanismo y alcance del NTC), §4 (caveats de retiro). Fecha: 2026-05-03. Ningún pendiente de Vera afecta este documento: el mecanismo técnico del sensor no cambia con el cambio de nombre.
- Orlan: Orlan_competencia_v1.md — Sección 3 (ningún competidor comunica función térmica en empaque). Fecha: 2026-05-03.
- Bruna: Bruna_gate_empaque_v1 — §2 Claim D ("Sensor NTC incorporado*": aprobado con caveat) y Claim E ("Autoprotección térmica": aprobado), §7.1 Refresh (bloque asterisco NTC corregido, sin temperaturas numéricas). Fecha: gate 2026-05-03, Refresh 2026-05-04.
- Aurelio: AU-1 v2 — §2 Alternativa B (arquitectura aprobada dos claims: velocidad + función térmica). Fecha: 2026-05-04.
- VA-1: Vael_messaging_framework_v1 — Pilar 3 (autoprotección térmica NTC) y §4 anti-mensaje (prohibición de "protección térmica" sin calificador y de "protege al motor"). Fecha: 2026-05-03.
- Decisión de Junta: Junta Directiva eligió Alternativa B. Observación Canudas: "NTC no dice nada, además le estás dando en este caso tu secreto industrial a la competencia."

**Brand wiki vigente al momento de redacción:** 01-identidad-de-marca.md — versión 2026-04-30. No consultada para esta tarea específica de naming de componente (no afecta pilares de marca Exceline existentes).

**Validez temporal:** Este documento es válido para el proceso de decisión de la Junta de mañana (2026-05-06) y la producción del arte final que le siga. Invalidado si:
- Vera actualiza la descripción del mecanismo del sensor (nuevo fact técnico que cambia el texto de retiro).
- Bruna emite decisión sobre algún claim de esta tabla que cambie su categoría.
- El Owner modifica la instrucción de no revelar componentes (en cuyo caso "Sensor NTC incorporado*" podría recuperar su estatus de opción válida).

**Cambios aguas arriba que invalidarían este documento:**
- Si I&D formaliza el umbral de temperatura de disparo del NTC (Vera Pendiente P-5): podría abrir formulaciones de retiro más específicas sin violar la instrucción de no comunicar temperaturas en empaque (Bruna §7.1 — decisión Owner). Requiere nueva evaluación de Bruna antes de incorporar.
- Si Orlan detecta que un competidor venezolano ha adoptado una de las formulaciones de esta tabla: el argumento de diferenciación de ese badge se debilita y requiere refresh de ranking.

**Decisiones del Owner pendientes:**
- Elección de la formulación final de entre las 5 opciones (top ranking Vael: Opción 1, seguida de Opción 4 y Opción 5).
- Confirmación del gate de Bruna sobre la opción elegida antes de pasar instrucción a Solenne y Oz.

**Claims con gate pendiente de Bruna:**
- Opciones 1 a 4: gate requerido antes de producción. Ver tabla de gate anterior.
- Opción 5: gate mínimo (extensión directa de Claim D ya aprobado). Puede avanzar más rápido si el tiempo es crítico.

**Notificaciones de refresh pendientes post-gate Bruna:**
- A Solenne: formulación exacta aprobada para delta de SO-1 / SO-1 v3.
- A Oz: texto del badge de tiro + texto del asterisco de retiro para implementación en redline.
- A Aurelio: confirmación de la formulación para AU-1 v3 o nota de cierre de AU-1 v2.

---

*domain-specialist. Genteca.*
*Vael — Brand & Messaging Strategist*
*Este documento es arquitectura de mensaje, no copy publicable. Las opciones están categorizadas como propuesta; la aprobación es de Bruna (BR-2). El copy final para el blister es de Solenne (SO-1 delta).*

---

# §Refresh 2026-05-05 — Opciones del Owner

**Trigger:** El Owner añade dos formulaciones al universo de candidatos: "Protección por calentamiento" y "Sensor de calentamiento". Eje semántico: la palabra "calentamiento" en lugar de "térmica/o". Hipótesis del Owner: mayor accesibilidad para consumidor residencial; posible pérdida de registro profesional para el instalador técnico.

**Insumos adicionales consultados:** Orlan_OL-1_competencia-naming-termico_v1.md §3 (territorios vacantes) y §4 (recomendaciones a Vael/Bruna). VA-5 v1 previo (criterios 1–7 y tabla de 5 finalistas). No se dispone de nuevo insumo de Vera ni de Bruna para este refresh: la evaluación parte de los mismos hechos técnicos.

---

## Evaluación de las 2 opciones del Owner contra los 7 criterios

### Opción A — "Protección por calentamiento" ⚠

**Texto exacto para tiro:** Protección por calentamiento*

**Texto del asterisco para retiro:**

> Sensor de temperatura ubicado junto al relé de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se dañen. Protege al protector mismo y a la instalación eléctrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actúa como protección de sobrecarga directa de la carga conectada. No reemplaza al interruptor termomagnético de la instalación.

**Evaluación por criterio:**

| Criterio | Cumple | Nota |
|---|---|---|
| 1 — Cero revelación de componente (NTC, termistor) | Sí | "Calentamiento" no nombra ningún componente. |
| 2 — Lenguaje de función / beneficio | Parcial | "Calentamiento" describe el fenómeno que activa la protección, no la función del sistema. Es más un descriptor del problema que del beneficio. |
| 3 — Compatible con caveat de retiro (sin temperatura numérica) | Sí | El texto de retiro estándar aplica sin modificación. |
| 4 — Audiencia mixta B (instalador + consumidor residencial) | Tenso | Para el consumidor residencial: "calentamiento" es cotidiano y concreto — ventaja. Para el instalador técnico: "protección por calentamiento" no es un término de la industria eléctrica; puede sonar informal o impreciso comparado con "protección térmica" o "protección por sobretemperatura". |
| 5 — ≤ 4 palabras | Sí | 3 palabras. |
| 6 — Coherencia con VA-1 y lengüeta "La protección más completa" | Tenso | VA-1 usa "protección térmica" y "autoprotección térmica" como lenguaje de marca establecido. "Calentamiento" introduce un registro nuevo que no tiene anclaje en el framework previo. |
| 7 — Cero promesa de protección del motor / la carga | Riesgo alto | "Protección por calentamiento" sin calificador es la formulación más susceptible de ser interpretada como protección del equipo conectado contra el calor. El consumidor puede leer: "protege mi equipo del calentamiento" — que es exactamente lo que Claim H rechazado de Bruna prohíbe. |

**Pros:**
- "Calentamiento" es la palabra más coloquial del universo de candidatos. El consumidor residencial sin formación técnica la entiende de forma inmediata y sin fricción.
- Tres palabras — compacta. No compite visualmente con el badge de velocidad.
- No revela componente ni arquitectura interna.

**Contras:**
- Criterio 7 en rojo: el mayor riesgo de todos los candidatos. La formulación "protección por calentamiento" en un protector de voltaje evoca protección del equipo conectado — interpretación que Bruna rechazó explícitamente (Claim H). El asterisco mitiga pero no elimina ese riesgo: muchos compradores no leen el retiro.
- El prefijo "por" construye una relación causal inversa problemática: "se protege [algo] porque hay calentamiento" — pero ¿qué protege? El badge no lo dice. La ambigüedad referencial (¿protege al protector? ¿al equipo conectado?) es la que Bruna necesita resolver en gate.
- "Calentamiento" como eje de naming no tiene precedente en el VA-1 framework. Introducirlo ahora rompe la coherencia terminológica del sistema de mensajes establecido.
- Orlan §4 señala que el naming ideal "no puede ser copiado trivialmente con un fusible simple" — "protección por calentamiento" es igual o más copiable que "protección térmica" a secas.

**Riesgo IP (Orlan OL-1 §3):** Término vacante en competencia VE. Pero la vacancia aquí no es ventaja — ningún competidor lo usa porque es una formulación funcionalmente débil para el segmento técnico, no porque sea un insight diferencial de Genteca.

**Nivel de revelación tecnológica:** Nulo en componente. Pero introduce riesgo semántico de confusión con protección de carga (Claim H Bruna).

**Categoría propuesta Vael:** ⚠ — Gate de Bruna requerido con foco específico en el riesgo Claim H (protección del equipo conectado). Vael no recomienda esta opción para finalista pero la somete al criterio de Bruna.

---

### Opción B — "Sensor de calentamiento" ⚠

**Texto exacto para tiro:** Sensor de calentamiento*

**Texto del asterisco para retiro:**

> Sensor de temperatura ubicado junto al relé de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se dañen. Protege al protector mismo y a la instalación eléctrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actúa como protección de sobrecarga directa de la carga conectada. No reemplaza al interruptor termomagnético de la instalación.

**Evaluación por criterio:**

| Criterio | Cumple | Nota |
|---|---|---|
| 1 — Cero revelación de componente (NTC, termistor) | Sí | "Sensor de calentamiento" no nombra el tipo de sensor. |
| 2 — Lenguaje de función / beneficio | Parcial | Nombra el sensor (componente) con descriptor funcional del fenómeno ("calentamiento"), no del beneficio final. Es un paso por encima del componente puro ("Sensor NTC") pero un paso por debajo del beneficio ("Autoprotección térmica"). |
| 3 — Compatible con caveat de retiro (sin temperatura numérica) | Sí | Aplica el texto estándar de retiro. |
| 4 — Audiencia mixta B | Tenso | Para el consumidor: "calentamiento" es comprensible; "sensor de calentamiento" suena a dispositivo cotidiano (como el sensor de humo). Para el instalador técnico: "sensor de calentamiento" es una denominación informal — en la industria eléctrica se dice "sensor térmico", "sensor de temperatura", "NTC" o "termistor". Puede reducir credibilidad técnica. |
| 5 — ≤ 4 palabras | Sí | 3 palabras. |
| 6 — Coherencia con VA-1 y lengüeta "La protección más completa" | Bajo | El VA-1 usa "sensor de temperatura" como floor del Owner (Opción 5 del VA-5 original). "Sensor de calentamiento" es una variante menos técnica del mismo concepto. No tiene anclaje en el framework previo; no rompe el sistema pero tampoco lo refuerza. |
| 7 — Cero promesa de protección del motor / la carga | Sí (por omisión) | "Sensor de calentamiento" no promete protección de nada: describe el componente. Riesgo Claim H bajo — más bajo que "Protección por calentamiento". |

**Pros:**
- Nombra el sensor sin nombrar el tipo: más coloquial que "Sensor de temperatura" (versión técnica, Opción 5 del VA-5 original) pero sin la imprecisión funcional de "Protección por calentamiento".
- Riesgo Claim H bajo: no promete proteger al equipo conectado.
- Compatible con el texto de retiro estándar sin modificación.
- Tres palabras — compacto.

**Contras:**
- "Calentamiento" como descriptor del sensor es lingüísticamente informal: un sensor no "detecta calentamiento" en la jerga técnica — detecta temperatura o cambios de temperatura. "Sensor de calentamiento" tiene baja precisión técnica.
- Para el instalador técnico, "Sensor de calentamiento" registra por debajo del floor que el Owner ya tenía aprobado ("Sensor de temperatura incorporado*" — Opción 5 del VA-5). Si el floor ya era una opción conservadora y menos diferenciadora, esta variante está aún más abajo en la escala de credibilidad técnica.
- No resuelve el problema central de naming: el instalador técnico no obtiene más información útil de "calentamiento" que de "temperatura", y el consumidor residencial que sí se beneficia del lenguaje coloquial no recibe ningún beneficio funcional adicional (no sabe qué hace el sensor con esa detección).
- Igual copiabilidad que la Opción 5 o mayor — "sensor de calentamiento" es más genérico que "sensor de temperatura incorporado".

**Riesgo IP (Orlan OL-1 §3):** Vacante en competencia VE. Igual que la Opción A, la vacancia refleja baja adopción del término por razones de registro profesional, no porque sea un hallazgo diferencial.

**Nivel de revelación tecnológica:** Nulo.

**Categoría propuesta Vael:** ⚠ — Defendible con caveat de registro técnico. No recomendada como finalista por debajo del floor ya establecido (Opción 5 del VA-5 original). Sometida a criterio de Bruna.

---

## Tabla comparativa de 5 opciones (top 3 original + 2 del Owner)

| # | Texto tiro | Palabras | Lenguaje comprador | Corrige malentendido motor | Riesgo Claim H (protección carga) | Credibilidad técnica instalador | Revelación IP | Apropiación de marca | Riesgo gate Bruna |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Autoprotección térmica activa* | 4 | Semi-técnico | Sí (prefijo "auto") | Bajo | Alto | Nulo | Media | Bajo |
| 4 | Termoprotección integrada* | 2 | Técnico-compacto | No | Bajo | Alto | Nulo | Alta | Bajo |
| 5 | Sensor de temperatura incorporado* | 4 | Neutral | No | Bajo | Alto | Nulo | Nula | Mínimo |
| A | Protección por calentamiento* | 3 | Coloquial | No | **Alto** | Bajo | Nulo | Nula | Alto |
| B | Sensor de calentamiento* | 3 | Coloquial | No | Bajo | Bajo-medio | Nulo | Nula | Bajo-medio |

**Nota columna "Riesgo Claim H":** Claim H de Bruna rechaza cualquier promesa de protección directa del equipo o motor conectado. "Protección por calentamiento" (Opción A) tiene el mayor riesgo de ser interpretada como "protege a mi equipo del calor".

---

## Re-ranking del top 3 final — 5 opciones consideradas

### #1 — Opción 1: "Autoprotección térmica activa*" — SE MANTIENE

Las dos opciones del Owner no desplazan a la Opción 1. La razón estructural: el eje "calentamiento" gana en coloquialidad pero pierde en los dos criterios más críticos para el contexto de este empaque — credibilidad técnica con el instalador (audiencia primaria de B que lee el retiro) y corrección activa del malentendido del 40% del mercado. La Opción 1 es el único candidato del universo de 5 que resuelve ese malentendido en el tiro, antes de que el consumidor llegue al asterisco.

Adicionalmente, el prefijo "auto" es el argumento diferenciador más defendible frente a la competencia: ningún competidor VE lo usa (Orlan §3), y un competidor que lo copie tendría que implementar la función para sostenerlo.

### #2 — Opción 4: "Termoprotección integrada*" — SE MANTIENE

Las opciones del Owner tampoco desplazan a la Opción 4. "Termoprotección" como sustantivo-concepto tiene un potencial de apropiación de marca que "calentamiento" no tiene: "calentamiento" es un descriptor cotidiano imposible de apropiarse; "termoprotección" como término compacto puede ser lenguaje de marca Genteca a largo plazo. Para la Junta de mañana, donde el espacio visual del blister es crítico, la compacidad de dos palabras sigue siendo un argumento operativo.

### #3 — Opción B: "Sensor de calentamiento*" DESPLAZA a Opción 5: "Sensor de temperatura incorporado*"

Este es el único desplazamiento que registran las opciones del Owner — y es marginal. La Opción B desplaza a la Opción 5 en el tercer puesto únicamente por compacidad (3 palabras vs. 4) y accesibilidad para el consumidor residencial. Sin embargo, la diferencia es estrecha y el desplazamiento no cambia la recomendación de finalista: ambas son opciones conservadoras por debajo del top 2, y la Opción B tiene menor credibilidad técnica que la Opción 5 para el instalador.

**Conclusión del desplazamiento:** las opciones del Owner aportan el vector "calentamiento" como dato útil (confirma que hay demanda de lenguaje coloquial) pero no producen un candidato superior al top 2 existente en ninguno de los criterios críticos. La Opción A queda descartada por riesgo Claim H. La Opción B ocupa el tercer puesto compartido con la Opción 5, sin desplazar al #1 ni al #2.

---

## Finalista única recomendada para gate de Bruna

### "Autoprotección térmica activa*"

**Texto de tiro:** Autoprotección térmica activa*

**Texto exacto de retiro (caveat adaptado — versión para empaque):**

> **Autoprotección térmica activa:** sensor de temperatura ubicado junto al relé de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se dañen. Protege al protector mismo y a la instalación eléctrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actúa como protección de sobrecarga directa de la carga conectada. Funciona como capa adicional de protección térmica; no reemplaza al interruptor termomagnético de la instalación.

**Argumento de cierre para Bruna:** la base ya existe en BR-2 — Claim E ("Autoprotección térmica") está aprobado. El gate requerido es de alcance mínimo: confirmar que añadir "activa" como adjetivo no cambia la categoría de riesgo del claim aprobado. El texto de retiro es funcional con la versión §7.1 Refresh de Bruna, sin temperaturas numéricas y sin mención de NTC.

**Duda crítica para Owner (marcada, no bloqueante):** ¿El Owner confirma que el NTC del GSM actúa como sensor activo de monitoreo continuo (no solo como fusible térmico de corte único)? Orlan OL-1 §4 señala que este punto debe confirmar Vera (Pendiente P-5). Si la respuesta de Vera es "solo actúa como fusible térmico", el adjetivo "activa" se debilita y la Opción 4 ("Termoprotección integrada*") se convierte en la alternativa de respaldo. El Owner autorizó proceder sin confirmación intermedia — esta nota es trazabilidad, no un bloqueo.

---

## Supuestos y límites — Refresh 2026-05-05

**Insumos consumidos en este refresh:**
- VA-5 v1 (2026-05-05): top 3, criterios 1–7, texto de retiro vigente, gate de Bruna pendiente.
- Orlan_OL-1_competencia-naming-termico_v1.md (2026-05-05): §3 territorios vacantes, §4 recomendaciones naming.
- Instrucción directa del Owner (2026-05-05): añadir "Protección por calentamiento" y "Sensor de calentamiento" al universo de candidatos.

**Insumos NO actualizados en este refresh (sin nueva información de aguas arriba):**
- Vera_brief_tecnico_v1: sin cambio. Los hechos técnicos del sensor son los mismos.
- Bruna_gate_empaque_v1: sin nueva decisión. El Claim E sigue aprobado; el gate de "activa" sigue pendiente.
- DECISIONS.md / RISK-POLICY.md: no consultados para este refresh de naming de función (sin cambio de política desde VA-5 v1).

**Validez temporal:** Refresh vigente para la Junta de mañana (2026-05-06). Invalidado si Bruna emite BR-2 que rechace "activa" como adjetivo del Claim E, o si Vera actualiza el mecanismo del NTC (Pendiente P-5 resuelto con resultado "solo fusible térmico").

**Claims con gate pendiente de Bruna post-refresh:**
- Finalista única "Autoprotección térmica activa*": gate mínimo sobre adjetivo "activa" respecto a Claim E ya aprobado. Prioridad: antes del memo flash de Aurelio a Junta.
- Opciones A y B del Owner: sometidas a criterio de Bruna. Opción A requiere evaluación específica de riesgo Claim H.

**Notificaciones de refresh — sin cambio respecto a VA-5 v1:**
- A Solenne: formulación exacta aprobada por Bruna para SO-1 delta.
- A Oz: texto de badge tiro + texto asterisco retiro.
- A Aurelio: formulación finalista para AU-1 memo flash a Junta.

---

*Refresh emitido por Vael — 2026-05-05. Domain-specialist. Genteca.*
*Finalista única propuesta: "Autoprotección térmica activa*". Decisión final: Bruna (BR-2). Copy publicable: Solenne (SO-1 delta). Memo Junta: Aurelio.*
