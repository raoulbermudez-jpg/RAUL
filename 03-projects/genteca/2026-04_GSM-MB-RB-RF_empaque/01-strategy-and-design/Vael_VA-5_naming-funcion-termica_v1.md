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

---

# §Refresh 2026-05-06 — Variante CON NTC (escenario abierto por Canudas + Kike)

**Documento:** Vael_VA-5_naming-funcion-termica_v1 §Refresh 2026-05-06
**Fecha:** 2026-05-06
**Trigger:** WhatsApp Kike → Canudas 2026-05-05. Kike argumenta que el NTC es innovación real, que no comunicarlo permite que competidores chinos copien la placa y lo cacareen primero, y que Exceline quedaría como rezagada. Canudas responde: "Hagan un ejemplo de comunicación con las siglas NTC. Y lo vemos." Esa respuesta es una apertura a evaluar — no una aprobación. El Owner instruye producir una variante B-CON-NTC (v2.2) paralela a B-sin-NTC (v2.1 vigente) para presentar a Canudas como contrapropuesta en reunión posterior.
**Status de v2.1:** VIGENTE. Este documento no la sustituye. v2.2 es escenario paralelo — los dos coexisten hasta decisión de Canudas.
**Para:** Bruna (gate posterior), Owner (decisión de presentar v2.2 a Canudas), Orlan (riesgo IP — ver notas en celdas correspondientes).

---

## §R6-1 — Criterios reformulados para el escenario CON NTC

Los 7 criterios del VA-5 v1 prohibían revelar el componente (Criterio 1). En el escenario B-sin-NTC esa prohibición era correcta: Canudas la formuló en la Junta de 2026-05-05. En el escenario CON NTC, ese criterio se convierte en análisis de costo-beneficio: el argumento de Kike (innovación visible, defensa anti-copia, liderazgo de categoría) es un beneficio potencial que Canudas abrió a evaluar.

Los criterios que siguen aplican **únicamente a este §Refresh**. Los criterios del VA-5 v1 siguen vigentes para la variante v2.1.

| # | Criterio reformulado | Diferencia respecto a v1 |
|---|---|---|
| 1 | Revelar "NTC" en el tiro es una decisión de costo-beneficio, no una prohibición. Se evalúa en cada opción. | CAMBIA: de "prohibición absoluta" a "análisis costo-beneficio por opción" |
| 2 | Lenguaje de función O de componente nombrado, según cuál sirva mejor al argumento de innovación de la opción. | CAMBIA: se admite lenguaje de componente cuando el argumento de marca lo justifica |
| 3 | Compatible con el cuerpo invariable del caveat de retiro (Bruna §8.3 — texto corregido sin temperaturas numéricas). Solo el header del retiro cambia según el badge del tiro. | IGUAL |
| 4 | Audiencia mixta B: instalador técnico (primario — lee retiro, entiende NTC) + consumidor residencial (secundario — solo ve tiro). Para opciones con NTC visible, el instalador técnico es beneficiario neto. | IGUAL — pero el instalador técnico pasa a ser audiencia con ventaja en opciones CON NTC |
| 5 | Preferible 4 palabras o menos. Jerarquía visual con "El más rápido ante parpadeos" en el blister de B. | IGUAL |
| 6 | Coherencia con VA-1 Pilar 3 (NTC como territorio en blanco de comunicación — Orlan §3) y con el argumento de innovación pionera que Kike articuló a Canudas. | CAMBIA: agrega el argumento "Exceline hace que NTC se conozca; el que lo copie es seguidor, no líder" |
| 7 | CERO promesa de protección del motor / la carga (prohibición Vera §1.4 + Bruna Claim H — sin excepciones). Este criterio es inamovible en ambos escenarios. | IGUAL — no se negocia |

**Nota sobre el Criterio 7:** Algunas formulaciones del research de Perplexity que el Owner obtuvo ("Doble vida útil: protege la integridad del propio protector y salvaguarda su electrodoméstico ante fallas eléctricas graves", "Sistema de Respaldo Térmico: La última línea de defensa para tu aire acondicionado") invocan protección del equipo conectado. Esas formulaciones están en zona roja de Claim H. Vael no las propone y las marca explícitamente. El Owner consultó Perplexity como insumo de inspiración; los textos de Perplexity no son claims aprobados y varios de ellos serían rechazados por Bruna sin modificación.

---

## §R6-2 — Evaluación de las 7 opciones

---

### Opción 1 — "Sensor NTC incorporado*" ⚠

**Texto exacto para tiro:** Sensor NTC incorporado*

**Contexto:** Esta es la opción original aprobada por Bruna (Claim D, BR-2 §2, 2026-05-03) y rechazada por Canudas en Junta por revelar "secreto industrial sin agregar beneficio percibido al comprador." Canudas abrió el 2026-05-05 a revisitar esta decisión si el ejemplo de comunicación lo convence. Esta opción recupera exactamente ese texto, que ya tiene gate de Bruna vigente.

**Texto del asterisco para retiro (cuerpo invariable Bruna §8.3 — solo header cambia):**

> **Sensor NTC incorporado:** sensor de temperatura ubicado junto al relé de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se dañen. Protege al protector mismo y a la instalación eléctrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actúa como protección de sobrecarga directa de la carga conectada. Funciona como capa adicional de protección térmica; no reemplaza al interruptor termomagnético de la instalación.

**Evaluación por criterios reformulados:**

| Criterio | Cumple | Nota |
|---|---|---|
| 1 — Revelar NTC: análisis costo-beneficio | Neutral | Revela el componente por nombre. Beneficio: argumento de innovación de Kike se comunica directamente. Costo: el que Canudas señaló — ¿agrega beneficio percibido al comprador medio? Depende de cuánto evangelización haga Exceline sobre NTC. |
| 2 — Función o componente | Componente | Nombra el componente. No habla de función. El instalador técnico lo entiende; el consumidor residencial no. |
| 3 — Caveat de retiro compatible | Sí | Cuerpo invariable §8.3 aplica. Header = "Sensor NTC incorporado:" |
| 4 — Audiencia mixta | Tenso | Instalador técnico: ventaja (NTC le dice todo). Consumidor residencial: "NTC" es opaco sin contexto. |
| 5 — Longitud | Sí | 3 palabras. |
| 6 — Coherencia VA-1 + argumento Kike | Sí | VA-1 Pilar 3 ya tenía NTC como eje. Kike lo defiende explícitamente. |
| 7 — Cero Claim H | Sí | No promete protección del motor ni de la carga. |

**Pros:**
- Gate de Bruna ya existe (Claim D aprobado con caveat). Ruta más rápida a producción si Canudas aprueba.
- El instalador técnico entiende NTC: es la señal técnica más directa de sofisticación de componente.
- La tesis de Kike es que NTC irá ganando significado a medida que Exceline lo comunique: "cualquier otro competidor que lo incorpore va a estar siguiendo al líder." Esta opción es la apuesta más directa para esa tesis.
- Compatible con argumento anti-copia: si los chinos copian la placa con NTC y lo comunican, Exceline ya lo habrá comunicado primero.

**Contras:**
- Es exactamente la opción que Canudas rechazó en Junta. La presentación como "el mismo badge" puede no pasar la revisión si no va acompañada de un contexto narrativo que el tiro solo no puede dar.
- "NTC" en el tiro sin evangelización previa es opaco para el consumidor residencial — el asterisco hace todo el trabajo explicativo.
- No comunica función ni beneficio. Solo nombra componente. Para el consumidor que no sabe qué es NTC (mayoría en el punto de venta), es igual que si dijera "Sensor X23B incorporado".

**Riesgo IP:** ver Orlan §Refresh — la opción original ya fue evaluada. NTC está en la Decisión Canudas como "secreto industrial". La reapertura de Canudas sugiere que el debate no está cerrado, pero la evaluación de si revelar NTC habilita copia china sigue pendiente en Orlan. Orlan debe confirmar si NTC es un término de dominio público en fichas técnicas de proveedores OEM o si es propiedad operativa de Genteca. Ver Orlan §Refresh.

**Riesgo Claim H:** Nulo. El texto del retiro no promete protección del equipo conectado.

**Defensa anti-copia china (argumento Kike):** Media. Si Exceline comunica NTC primero, los competidores que copien la placa y lo comuniquen después quedan como seguidores. Pero si la copia se da antes de que la comunicación de Exceline haya calado, el argumento se invierte. La eficacia de esta defensa depende de la velocidad de la campaña de Exceline, no del badge en sí.

**Compatibilidad caveat Bruna §8.3:** Sí. Cuerpo invariable; solo header cambia.

---

### Opción 2 — "Escudo Térmico Integrado*" ⚠

**Texto exacto para tiro:** Escudo Térmico Integrado*

**Contexto:** Propuesta #1 de Perplexity ("Con Escudo Térmico Integrado"). Perplexity la destacó como la opción con mayor gancho comercial combinada con "Previene sobrecalentamientos y riesgo de incendio." Vael adopta la primera parte como badge; la segunda parte está en zona roja de Claim H y se descarta.

**Texto del asterisco para retiro (cuerpo invariable Bruna §8.3):**

> **Escudo Térmico Integrado:** sensor de temperatura ubicado junto al relé de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se dañen. Protege al protector mismo y a la instalación eléctrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actúa como protección de sobrecarga directa de la carga conectada. Funciona como capa adicional de protección térmica; no reemplaza al interruptor termomagnético de la instalación.

**Evaluación por criterios reformulados:**

| Criterio | Cumple | Nota |
|---|---|---|
| 1 — Revelar NTC: análisis costo-beneficio | No revela NTC | NTC solo aparece en retiro si se explicita; el badge es metáfora visual. Costo: no comunica el componente que Canudas abrió a evaluar. Beneficio: sí comunica la función con potencia visual. |
| 2 — Función o componente | Función + metáfora | "Escudo" = protección activa; "Térmico" = del calor; "Integrado" = parte del diseño. No nombra NTC. |
| 3 — Caveat de retiro compatible | Sí | Cuerpo invariable §8.3 aplica. |
| 4 — Audiencia mixta | Fuerte | "Escudo" funciona para ambas audiencias. El consumidor residencial visualiza una barrera. El instalador técnico entiende la función pero no recibe la señal técnica de componente. |
| 5 — Longitud | Sí | 3 palabras. |
| 6 — Coherencia VA-1 + argumento Kike | Parcial | VA-1 Pilar 3 tenía NTC como eje. Este badge no menciona NTC — debilita el argumento de Kike sobre comunicar la innovación por nombre. |
| 7 — Cero Claim H | Condicional | Si se usa solo "Escudo Térmico Integrado*", el Claim H está protegido. Si se añade la frase de Perplexity "riesgo de incendio" o "protege tu electrodoméstico", el Claim H entra en zona roja. Solenne no puede extender este badge con esas frases sin nuevo gate de Bruna. |

**Pros:**
- La palabra "Escudo" genera visualización inmediata: barrera física, protección robusta. Perplexity señala que el cerebro procesa imágenes antes que texto. En punto de venta de ferretería, el atributo visual es una ventaja.
- No revela NTC como componente. Si el debate de IP no está resuelto, esta opción elimina ese riesgo.
- "Integrado" comunica que no es add-on sino parte del diseño. Coherente con "La protección más completa."
- Compatible con la apertura de Canudas: es un "ejemplo de comunicación" que no reproduce el texto que rechazó.

**Contras:**
- No satisface el pedido literal de Canudas ("con las siglas NTC"). Si Canudas quería ver NTC visible, esta opción no lo da. Puede ser rechazada en la revisión por no responder a lo que pidió.
- La metáfora "Escudo" es genérica: cualquier competidor puede usar "Escudo Térmico" sin tener un NTC. No hay defensa técnica de la formulación.
- Para el instalador técnico que conoce NTC, "Escudo Térmico Integrado" es menos informativo que "Sensor NTC incorporado." Puede percibirse como marketingese.
- Perplexity combinó el badge con "Previene sobrecalentamientos y riesgo de incendio" — esa cola de frase está en zona roja de Claim H (Bruna). Si el Owner o Oz la añaden en el redline sin gate, el claim queda fuera de spec.

**Riesgo IP:** ver Orlan §Refresh. "Escudo Térmico Integrado" no revela componente. El nombre puede ser apropiado como lenguaje de marca. Orlan debe confirmar si hay precedente en la categoría regional.

**Riesgo Claim H:** Bajo en el badge solo. Riesgo medio si se extiende con frases del research de Perplexity. La instrucción literal a Solenne y Oz es: badge solo, sin frases adicionales sobre protección del equipo o riesgo de incendio.

**Defensa anti-copia china:** Baja. "Escudo Térmico Integrado" describe una función genérica. Cualquier competidor con NTC (o incluso sin NTC, con un bimetal) puede reclamarlo. No tiene la especificidad técnica que da el nombre del componente.

**Compatibilidad caveat Bruna §8.3:** Sí. Cuerpo invariable; solo header cambia.

---

### Opción 3 — "Tecnología NTC EscudoTérmico™" (combinación bilingüe) ⚠

**Texto exacto para tiro:** Tecnología NTC EscudoTérmico™*

**Contexto:** El Owner aceptó anglicismos temporalmente con alternativa española o combinación bilingüe en la misma frase. Perplexity propuso "Tecnología Thermo-Safe™" como bautizo comercial del NTC. Vael propone en cambio la fórmula bilingüe obligatoria: "NTC" (componente técnico, siglas universales) + "EscudoTérmico™" (nombre de marca en español). Esta construcción cumple la instrucción del Owner (español obligatorio, anglicismo aceptado solo en combinación) y responde al pedido de Canudas de ver "las siglas NTC" mientras añade identidad de marca.

**Formulación alternativa en español puro (obligatoria per instrucción Owner):** Tecnología NTC EscudoTérmico™* — ya es bilingüe por construcción. Si se requiere versión sin anglicismo: "Tecnología Sensor-Térmico NTC™*" — menos elegante. Vael recomienda la versión bilingüe.

**Nota sobre la marca™:** el símbolo ™ implica una aspiración de apropiación de marca. La decisión de usar ™ vs ® corresponde al Owner y al asesor legal. Vael lo incluye como indicador de intención de naming de tecnología; el Owner decide si la marca se registra o si el ™ se usa como señal no registrada.

**Texto del asterisco para retiro (cuerpo invariable Bruna §8.3):**

> **Tecnología NTC EscudoTérmico™:** sensor de temperatura ubicado junto al relé de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se dañen. Protege al protector mismo y a la instalación eléctrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actúa como protección de sobrecarga directa de la carga conectada. Funciona como capa adicional de protección térmica; no reemplaza al interruptor termomagnético de la instalación.

**Evaluación por criterios reformulados:**

| Criterio | Cumple | Nota |
|---|---|---|
| 1 — Revelar NTC: análisis costo-beneficio | Revela NTC | Beneficio: cumple el pedido de Canudas; activa la tesis de Kike; el instalador técnico recibe señal precisa. Costo: 4 palabras más símbolo, posible saturación visual en blister pequeño. |
| 2 — Función o componente | Componente + nombre de marca | NTC nombra el componente; "EscudoTérmico" nombra la función con metáfora. Doble canal. |
| 3 — Caveat de retiro compatible | Sí | Cuerpo invariable §8.3 aplica. |
| 4 — Audiencia mixta | Fuerte | Instalador técnico: lee NTC, entiende. Consumidor residencial: lee "EscudoTérmico", visualiza protección. Cada audiencia recibe su señal. |
| 5 — Longitud | Tenso | 4 palabras + símbolo. Puede ser la formulación más larga del set. En blister con badge de velocidad, requiere verificación de espacio con Atlas/Oz. |
| 6 — Coherencia VA-1 + argumento Kike | Sí | Comunica NTC (innovación que Exceline bautiza) + función (EscudoTérmico como lenguaje de marca propio). Kike quedaría satisfecho: las siglas están, y están en un contexto de naming de tecnología. |
| 7 — Cero Claim H | Sí | Ninguna promesa de protección del equipo conectado. |

**Pros:**
- Es la única opción del set que da al mismo tiempo: NTC visible (argumento Kike + pedido Canudas) + nombre de función comprensible para el consumidor + aspiración de apropiación de marca a largo plazo.
- Si la marca "EscudoTérmico" se establece, Exceline tiene un activo de naming registrable. Un competidor que copie la placa no puede usar "EscudoTérmico™" — eso es la defensa real de marca que Perplexity señaló para "Thermo-Safe™".
- El doble canal técnico/emocional ("NTC" para el técnico, "EscudoTérmico" para el comprador) maximiza la cobertura de audiencias en una sola frase.
- Responde exactamente al pedido de Canudas ("con las siglas NTC") y va más allá: lo integra en un concepto de marca.

**Contras:**
- Longitud: 4 palabras + símbolo. En el blister de B donde "El más rápido ante parpadeos (< 0,03 s)" ya ocupa espacio dominante, la saturación visual es un riesgo real. Oz y Atlas deben verificar.
- La marca™ implica compromiso de naming a largo plazo. Si la empresa no va a defender el nombre en el mercado (campañas, refuerzo en otros canales), el ™ es aspiracional pero vacío.
- Pronunciabilidad: "NTC EscudoTérmico" es una cadena de cinco sílabas técnicas + cuatro sílabas de función. En venta oral (el instalador recomendando el producto), la frase es larga.
- La combinación bilingüe puede percibirse como indefinida: ¿es el nombre "NTC EscudoTérmico" o son dos elementos separados? La puntuación y el diseño tipográfico son críticos para que funcione visualmente.

**Riesgo IP:** ver Orlan §Refresh. Si "EscudoTérmico" se registra como marca, la protección es alta. Si no se registra, cualquier competidor puede usar el término. Orlan debe confirmar disponibilidad del nombre como marca en Venezuela y región.

**Riesgo Claim H:** Nulo. El badge no invoca protección del equipo.

**Defensa anti-copia china:** Alta. Esta es la lógica exacta que Perplexity articuló para "Thermo-Safe™": si la competencia copia la placa, no puede poner "EscudoTérmico™" en la caja si Exceline lo ha registrado. La copia física del componente no implica la copia del naming de marca.

**Compatibilidad caveat Bruna §8.3:** Sí. Cuerpo invariable; solo header cambia.

---

### Opción 4 — "Sensor NTC · Escudo Térmico*" ⚠

**Texto exacto para tiro:** Sensor NTC · Escudo Térmico*

**Contexto:** Híbrido propuesto por el Owner. El interpunto (·) separa el componente de la función en una sola línea. Alternativa española pura ya está presente por construcción.

**Texto del asterisco para retiro (cuerpo invariable Bruna §8.3):**

> **Sensor NTC · Escudo Térmico:** sensor de temperatura ubicado junto al relé de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se dañen. Protege al protector mismo y a la instalación eléctrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actúa como protección de sobrecarga directa de la carga conectada. Funciona como capa adicional de protección térmica; no reemplaza al interruptor termomagnético de la instalación.

**Evaluación por criterios reformulados:**

| Criterio | Cumple | Nota |
|---|---|---|
| 1 — Revelar NTC: análisis costo-beneficio | Revela NTC | Igual que Op. 1 y 3. |
| 2 — Función o componente | Ambos | "Sensor NTC" = componente; "Escudo Térmico" = función/metáfora. |
| 3 — Caveat de retiro compatible | Sí | |
| 4 — Audiencia mixta | Fuerte | Cada audiencia lee lo suyo. |
| 5 — Longitud | Tenso | 4 palabras + interpunto. Similar a Op. 3 en carga visual. |
| 6 — Coherencia VA-1 + argumento Kike | Sí | NTC visible + función metafórica. |
| 7 — Cero Claim H | Sí | |

**Pros:**
- El interpunto crea una lectura en dos tiempos: el técnico se detiene en "Sensor NTC" y el comprador continúa hacia "Escudo Térmico". Es una arquitectura tipográfica que permite el doble canal.
- Más legible que la Opción 3 porque evita el nombre de marca™ (sin la carga de comprometerse a un naming registrable).
- Responde al pedido de Canudas ("siglas NTC") y al argumento de Kike.
- En español puro sin anglicismo.

**Contras:**
- El interpunto es un dispositivo tipográfico. En un blister de ferretería, la reproducción de ese carácter depende del sistema de tipografía de Oz. Si el interpunto no se imprime correctamente, se lee como "Sensor NTC Escudo Térmico" (posible confusión con que el sensor se llama "Escudo Térmico").
- La frase como nombre de función es ambigua en la segunda lectura: "Escudo Térmico" como subtítulo de "Sensor NTC" puede parecer una descripción del sensor, no de la función del sistema. La relación lógica entre las dos partes no está explícita.
- Sin ™, la defensa anti-copia es igual a la de Op. 1 (el que copie la placa puede decir "Sensor NTC · Escudo Térmico" si el término no está registrado).

**Riesgo IP:** ver Orlan §Refresh. Sin registro de "Escudo Térmico" como marca, la protección es la misma que para Op. 1.

**Riesgo Claim H:** Nulo.

**Defensa anti-copia china:** Media. Superior a Op. 1 si "Escudo Térmico" se registra; igual a Op. 1 si no se registra.

**Compatibilidad caveat Bruna §8.3:** Sí.

---

### Opción 5 — "Tecnología NTC: Previene Sobrecalentamiento*" ⚠

**Texto exacto para tiro:** Tecnología NTC: Previene Sobrecalentamiento*

**Contexto:** Storytelling antifuego propuesto por el Owner. El colon construye una relación causa-efecto: la tecnología NTC es la causa; prevenir el sobrecalentamiento es el efecto.

**Texto del asterisco para retiro (cuerpo invariable Bruna §8.3):**

> **Tecnología NTC — Previene Sobrecalentamiento:** sensor de temperatura ubicado junto al relé de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se dañen. Protege al protector mismo y a la instalación eléctrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actúa como protección de sobrecarga directa de la carga conectada. Funciona como capa adicional de protección térmica; no reemplaza al interruptor termomagnético de la instalación.

**Evaluación por criterios reformulados:**

| Criterio | Cumple | Nota |
|---|---|---|
| 1 — Revelar NTC: análisis costo-beneficio | Revela NTC | NTC visible. "Tecnología" eleva el registro. |
| 2 — Función o componente | Componente + verbo de acción | "NTC" = componente; "Previene Sobrecalentamiento" = acción funcional. |
| 3 — Caveat de retiro compatible | Sí | |
| 4 — Audiencia mixta | Parcial | El consumidor residencial entiende "Previene Sobrecalentamiento". El instalador técnico preferiría más especificidad técnica. |
| 5 — Longitud | Fuera del rango preferido | 4 palabras + signo de puntuación. El colon y la longitud total hacen que sea la formulación más larga del set. |
| 6 — Coherencia VA-1 + argumento Kike | Sí | NTC visible + beneficio antifuego. Kike argumentó el riesgo de incendio implícito en falsos contactos. |
| 7 — Cero Claim H | Zona gris | "Previene Sobrecalentamiento" sin calificador puede interpretarse como prevención del sobrecalentamiento del equipo conectado (Claim H). Si el lector infiere que previene el sobrecalentamiento del aire acondicionado, el claim croza la línea de Bruna. El asterisco mitiga pero no elimina esa interpretación. Bruna debe evaluar. |

**Pros:**
- "Previene Sobrecalentamiento" comunica la acción directa en lenguaje de beneficio accesible para el consumidor residencial. Es la formulación más directamente conectada con el argumento emocional de Perplexity (miedo al calor excesivo y al daño del equipo).
- "Tecnología NTC" eleva el componente a categoría de innovación ("tecnología", no "sensor"). Esto refuerza el argumento de Kike.
- Estructura causa-efecto clara: el colon hace explícita la relación.

**Contras:**
- Criterio 7 en zona gris: "Previene Sobrecalentamiento" sin calificador (¿sobrecalentamiento de qué?) puede activar la interpretación de protección del equipo conectado. El asterisco solo mitiga si el comprador lo lee. En el tiro solo, el claim puede ser interpretado como Claim H por Bruna. Requiere gate específico.
- Longitud: es la opción más larga del set, incluyendo el colon. En el blister de B, la competencia visual con "El más rápido ante parpadeos (< 0,03 s)" es la más difícil de resolver.
- "Previene Sobrecalentamiento" como badge no tiene potencial de apropiación de marca: es una descripción de acción genérica que cualquier fabricante con cualquier mecanismo de protección térmica puede usar.

**Riesgo IP:** ver Orlan §Refresh. Término funcional genérico, sin ventaja de naming propietario.

**Riesgo Claim H:** ALTO. Requiere gate específico de Bruna sobre si "Previene Sobrecalentamiento" sin calificador cruza la línea de protección implícita de la carga conectada. Vael categoriza esta opción como ⚠ con flag de Claim H. No avanza sin gate explícito de Bruna.

**Defensa anti-copia china:** Muy baja. "Tecnología NTC: Previene Sobrecalentamiento" describe componente + función genérica. Sin naming de marca, la copia es trivial.

**Compatibilidad caveat Bruna §8.3:** Sí en el cuerpo. El header en el retiro debería leer "Tecnología NTC — Previene Sobrecalentamiento:" (con guión en lugar de colon para distinguir del texto del cuerpo).

---

### Opción 6 — "NTC ThermoShield™ / NTC EscudoTérmico™*" (combinación bilingüe compacta) ⚠

**Texto exacto para tiro — versión bilingüe:** NTC ThermoShield™*
**Alternativa española obligatoria (instrucción Owner):** NTC EscudoTérmico™*
**Formulación bilingüe en misma frase (preferida por Vael):** NTC EscudoTérmico / ThermoShield™*

**Contexto:** Aportación creativa de Vael. En lugar de construir una frase larga, se usa la sigla NTC como prefijo de un nombre de tecnología bautizado. La diferencia con la Opción 3 es la compacidad: dos o tres elementos, no cuatro palabras. El ™ señala intención de naming propietario.

**Nota de anglicismo:** La instrucción del Owner es que los anglicismos son aceptados temporalmente pero con alternativa española o combinación bilingüe en la misma frase. Por tanto:
- Si se usa "NTC ThermoShield™": debe aparecer en el mismo artefacto visual "NTC EscudoTérmico™" como alternativa o subtítulo.
- Si el espacio del blister no permite ambos: usar "NTC EscudoTérmico™" como única versión (español puro).
- Vael recomienda: "NTC EscudoTérmico™" como nombre principal del badge, con "ThermoShield" como subtexto de diseño si el espacio lo permite.

**Texto del asterisco para retiro (cuerpo invariable Bruna §8.3):**

> **NTC EscudoTérmico™:** sensor de temperatura ubicado junto al relé de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se dañen. Protege al protector mismo y a la instalación eléctrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actúa como protección de sobrecarga directa de la carga conectada. Funciona como capa adicional de protección térmica; no reemplaza al interruptor termomagnético de la instalación.

**Evaluación por criterios reformulados:**

| Criterio | Cumple | Nota |
|---|---|---|
| 1 — Revelar NTC: análisis costo-beneficio | Revela NTC | Directamente. |
| 2 — Función o componente | Componente + nombre de marca | NTC = componente; EscudoTérmico = naming de función. |
| 3 — Caveat de retiro compatible | Sí | |
| 4 — Audiencia mixta | Fuerte | NTC al técnico; EscudoTérmico al consumidor. |
| 5 — Longitud | Sí | 2 elementos. Es el badge más compacto del set CON-NTC. |
| 6 — Coherencia VA-1 + argumento Kike | Sí | NTC visible + naming de marca. |
| 7 — Cero Claim H | Sí | |

**Pros:**
- Es la versión más compacta de la combinación componente + nombre de marca. Dos elementos, un solo badge.
- La compacidad resuelve el problema de longitud que afecta a las Opciones 3, 4 y 5. En el blister de B, "NTC EscudoTérmico™" compite visualmente mejor con el badge de velocidad.
- "NTC EscudoTérmico™" como nombre tiene el mayor potencial de apropiación de marca del set: es corto, es registrable, y combina la señal técnica (NTC) con la identidad de función (EscudoTérmico).
- La lógica anti-copia de Perplexity aplica en su versión más fuerte: si se registra "EscudoTérmico™" o "ThermoShield™", el competidor que copie la placa no puede usar el nombre.
- Responde al pedido de Canudas ("siglas NTC") y al argumento de Kike (NTC como innovación bautizada por Exceline).

**Contras:**
- "NTC EscudoTérmico" sin "Tecnología" o "Sensor" delante es una frase de naming puro: el comprador que no sabe qué es NTC recibe una cadena sin verbo ni sustantivo claro. El retiro hace todo el trabajo explicativo.
- El ™ implica un compromiso de naming que la empresa debe sostener en el tiempo: si el nombre no se usa consistentemente en todos los canales (packaging, QR, argumentario ESC, publicidad), el valor del naming se diluye.
- Como todas las opciones CON-NTC: si la aprobación de Canudas no llega, este badge queda archivado.

**Riesgo IP:** ver Orlan §Refresh. Esta es la opción con mayor potencial de protección via naming registrado. Orlan debe confirmar disponibilidad de "EscudoTérmico" y/o "ThermoShield" como marcas en Venezuela/región.

**Riesgo Claim H:** Nulo.

**Defensa anti-copia china:** Alta. La más alta del set si el naming se registra.

**Compatibilidad caveat Bruna §8.3:** Sí. Cuerpo invariable; header = "NTC EscudoTérmico™:".

---

### Opción 7 — "Primer protector con NTC en Venezuela*" ✅ (claim de pionero) — solo si se confirma hecho

**Texto exacto para tiro:** Primer protector con NTC en Venezuela*

**Contexto:** Aportación creativa de Vael. El argumento de Kike es exactamente este: Exceline fue primero. Si Exceline comunica NTC antes que cualquier competidor venezolano, puede reclamar el pionerismo en la categoría. Orlan §3 confirma que a 2026-05-03 ningún competidor venezolano comunica NTC en empaque ni datasheet. El claim de pionero convierte el argumento de Kike en texto de tiro.

**Condición de uso:** Este claim solo es válido si Orlan puede confirmar que ningún competidor venezolano ha comunicado NTC en empaque, POP o publicidad **antes del lanzamiento de Exceline**. Si esa condición se verifica al momento del lanzamiento, el claim es defendible. Si un competidor se adelanta (el escenario exacto que Kike quiere evitar), el claim queda inválido. Es el claim más arriesgado del set en términos de ventana temporal, y el más poderoso si se lanza a tiempo.

**Texto del asterisco para retiro (cuerpo invariable Bruna §8.3):**

> **Primer protector con NTC en Venezuela:** sensor de temperatura ubicado junto al relé de potencia. Detecta calentamiento excesivo causado por sobrecorrientes o por conexiones deficientes (bornes flojos o falsos contactos) y desconecta la carga antes de que el cableado o las conexiones se dañen. Protege al protector mismo y a la instalación eléctrica. Para cargas de baja demanda de corriente, protege al protector y al cableado, pero no actúa como protección de sobrecarga directa de la carga conectada. Funciona como capa adicional de protección térmica; no reemplaza al interruptor termomagnético de la instalación.

**Evaluación por criterios reformulados:**

| Criterio | Cumple | Nota |
|---|---|---|
| 1 — Revelar NTC: análisis costo-beneficio | Revela NTC | Completamente. Además, lo posiciona como innovación pionera en el mercado venezolano. |
| 2 — Función o componente | Componente + posicionamiento de liderazgo | Menciona componente + reclama primer mover en el mercado. |
| 3 — Caveat de retiro compatible | Sí | Cuerpo invariable §8.3. El header indica la función del NTC. |
| 4 — Audiencia mixta | Fuerte para el instalador técnico | "NTC" al técnico + "Primero en Venezuela" a ambos. El consumidor residencial entiende el pionerismo aunque no entienda NTC. |
| 5 — Longitud | Fuera del rango preferido | 6 palabras. La más larga del set. Requiere decisión de diseño: si cabe en el blister de B sin comprimir el badge de velocidad. |
| 6 — Coherencia VA-1 + argumento Kike | Perfecta | Esta opción ES el argumento de Kike convertido en texto de empaque. |
| 7 — Cero Claim H | Sí | No promete protección del equipo. |

**Pros:**
- Es el único badge del set que convierte el argumento estratégico de Kike (innovación pionera, liderazgo de categoría) en claim de tiro directo. No hay traducción ni pérdida de fuerza argumentativa.
- "Primero en Venezuela" es el claim de diferenciación más fuerte del set en términos de posicionamiento. Si se lanza antes que cualquier competidor, es un claim verificable y memorable.
- El claim de pionero tiene efecto permanente: incluso si los competidores copian el NTC después, el hecho de que Exceline fue primero no cambia. "El primero" es un atributo temporal irreversible.
- Compatible con la tesis de Bruna BR-5 Precedente #2 invertido: en lugar de "el único", se dice "el primero" — que es un claim de liderazgo temporal más honesto y más difícil de refutar.

**Contras:**
- Longitud: 6 palabras. La más larga del set. El espacio en el blister de B puede ser un bloqueante operativo. Atlas y Oz deben confirmar viabilidad antes de que el claim avance en el proceso.
- El claim de pionero tiene una ventana de validez: es válido mientras ningún competidor lo haya comunicado antes. Si un competidor se adelanta en el lapso entre la decisión de Junta y el lanzamiento del empaque, el claim queda inválido. Es el claim con mayor exposición a la variable tiempo.
- Bruna necesita verificación activa de Orlan antes de aprobar: el claim "Primero en Venezuela" es un superlativo de orden temporal que requiere evidencia de que ningún competidor lo comunicó antes. Sin ese gate, Bruna no puede aprobarlo.
- Para el consumidor residencial sin contexto técnico, "NTC" en el badge sigue siendo opaco. La fuerza del claim descansa en el "Primero en Venezuela", no en NTC en sí.

**Riesgo IP:** ver Orlan §Refresh. Orlan debe confirmar que el claim de "primero en Venezuela" es verificable al momento del lanzamiento. Esta es la opción que más depende de la confirmación de Orlan.

**Riesgo Claim H:** Nulo.

**Defensa anti-copia china:** La más alta del set. Si se lanza a tiempo, el registro histórico de primacía queda en el mercado. La copia confirma el liderazgo de Exceline.

**Compatibilidad caveat Bruna §8.3:** Sí. Cuerpo invariable; solo header cambia.

---

## §R6-3 — Tabla resumen comparativa

| # | Texto tiro | Palabras | NTC visible | Lenguaje | Riesgo Claim H | Defensa anti-copia | Apropiación marca | Riesgo gate Bruna | Responde pedido Canudas |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Sensor NTC incorporado* | 3 | Sí | Componente | Nulo | Media | Nula | Bajo (ya aprobado) | Sí (recupera el original) |
| 2 | Escudo Térmico Integrado* | 3 | No | Función+metáfora | Bajo (badge solo) | Baja | Media | Bajo | Parcial (no tiene NTC) |
| 3 | Tecnología NTC EscudoTérmico™* | 4+™ | Sí | Comp.+naming™ | Nulo | Alta (si se registra) | Alta | Medio (naming nuevo + ™) | Sí |
| 4 | Sensor NTC · Escudo Térmico* | 4+· | Sí | Comp.+metáfora | Nulo | Media-alta | Media | Bajo-medio | Sí |
| 5 | Tecnología NTC: Previene Sobrecalentamiento* | 4+ | Sí | Comp.+acción | ALTO (zona gris) | Muy baja | Nula | Alto (flag Claim H) | Sí |
| 6 | NTC EscudoTérmico™* | 2+™ | Sí | Naming compacto | Nulo | Alta (si se registra) | Alta | Medio (naming + ™) | Sí |
| 7 | Primer protector con NTC en Venezuela* | 6 | Sí | Pionero | Nulo | La más alta | Alta | Alto (requiere gate Orlan) | Sí — la más directa |

**Nota columna "Responde pedido Canudas":** la apertura de Canudas fue "hagan un ejemplo con las siglas NTC." Las opciones 2 no incluye NTC en el tiro — responde a la función pero no a la instrucción literal. Las demás incluyen NTC en el tiro.

---

## §R6-4 — Ranking por impacto estimado (4 ejes ponderados)

Ejes y pesos asignados por instrucción del Owner:

| Eje | Peso asignado (Vael) |
|---|---|
| Diferenciación competitiva (anti-copia china) | 30% |
| Comprensión audiencia mixta (instalador + consumidor) | 25% |
| Apropiación de marca a largo plazo | 25% |
| Riesgo gate Bruna | 20% |

Puntuaciones de 1 (más débil) a 7 (más fuerte) por eje. Riesgo Bruna: puntuación inversa (1 = más arriesgado, 7 = más limpio para gate).

| # | Opción | Diferenciación (30%) | Comprensión (25%) | Apropiación marca (25%) | Riesgo Bruna (20%) | Score ponderado |
|---|---|---|---|---|---|---|
| 6 | NTC EscudoTérmico™* | 7 | 6 | 7 | 5 | **6,45** |
| 3 | Tecnología NTC EscudoTérmico™* | 7 | 7 | 7 | 4 | **6,35** |
| 7 | Primer protector con NTC en Venezuela* | 7 | 5 | 6 | 2 | **5,35** |
| 1 | Sensor NTC incorporado* | 4 | 5 | 2 | 7 | **4,45** |
| 4 | Sensor NTC · Escudo Térmico* | 5 | 6 | 4 | 5 | **5,00** |
| 2 | Escudo Térmico Integrado* | 3 | 6 | 4 | 6 | **4,55** |
| 5 | Tecnología NTC: Previene Sobrecalentamiento* | 2 | 4 | 1 | 1 | **2,00** |

**Ranking final por impacto estimado:**

1. **Op. 6 — "NTC EscudoTérmico™*"** — 6,45
2. **Op. 3 — "Tecnología NTC EscudoTérmico™*"** — 6,35
3. **Op. 7 — "Primer protector con NTC en Venezuela*"** — 5,35
4. **Op. 4 — "Sensor NTC · Escudo Térmico*"** — 5,00
5. **Op. 2 — "Escudo Térmico Integrado*"** — 4,55
6. **Op. 1 — "Sensor NTC incorporado*"** — 4,45
7. **Op. 5 — "Tecnología NTC: Previene Sobrecalentamiento*"** — 2,00

---

## §R6-5 — Recomendación finalista

### Finalista principal: Opción 6 — "NTC EscudoTérmico™*"

**Argumento decisivo:** La Opción 6 es la única del set que resuelve los cuatro ejes simultáneamente sin comprometer ninguno. Responde al pedido literal de Canudas (NTC visible), activa la tesis de Kike (nombre de marca propietario que los competidores no pueden copiar aunque copien la placa), es compacta (2 elementos — la más corta del set CON-NTC), y tiene el mayor potencial de apropiación de marca a largo plazo si "EscudoTérmico™" se registra. Para el instalador técnico, NTC es señal directa de componente sofisticado. Para el consumidor residencial, EscudoTérmico es una imagen de protección sin necesidad de entender el componente. Riesgo de Claim H: nulo. Riesgo de gate Bruna: medio (el naming nuevo requiere gate del nombre, no del claim funcional).

**Diferencia crítica con la Opción 3:** La Opción 3 ("Tecnología NTC EscudoTérmico™*") tiene casi el mismo score (6,35 vs 6,45) pero agrega la palabra "Tecnología" y el colon, lo que aumenta la longitud en dos elementos. "Tecnología" eleva el registro retórico (útil para el consumidor) pero en un blister de ferretería con espacio ya ocupado por el badge de velocidad, cada palabra extra tiene un costo real de diseño. La Opción 6 logra el mismo efecto con menos palabras.

### Finalista de respaldo: Opción 3 — "Tecnología NTC EscudoTérmico™*"

**Cuándo preferir Op. 3 sobre Op. 6:** si Oz y Atlas confirman que el espacio del blister de B permite 4 palabras + ™ sin comprimir el badge de velocidad. En ese caso, "Tecnología" añade el registro de innovación que refuerza el argumento de Kike sin costo de comprensión. Si el espacio es el factor limitante, Op. 6 es la alternativa directa.

### Criterio de elección entre Op. 6 y Op. 3

El Owner y Atlas/Oz deciden según maqueta real. La pregunta concreta: ¿cabe "Tecnología NTC EscudoTérmico™*" en el blister de B sin comprimir la jerarquía visual del badge de velocidad? Si sí: Op. 3. Si no: Op. 6. Ambas van a Bruna con el mismo texto de retiro; el gate es idéntico salvo por el header.

### Nota sobre la Opción 7

La Opción 7 ("Primer protector con NTC en Venezuela*") es la más poderosa estratégicamente si se lanza antes que cualquier competidor. Vael la incluye en el top 3 del ranking y recomienda que el Owner la considere para el lanzamiento completo si Orlan puede confirmar la vacancia del claim en el momento de producción del arte. No es adecuada para la reunión con Canudas como "ejemplo de comunicación" (es demasiado larga para un badge de tiro y requiere gate de Orlan que no está disponible hoy). Es un claim para la campaña de lanzamiento, no solo para el empaque.

---

## §R6-6 — Nota sobre anglicismos (instrucción Owner)

El Owner instruyó que los anglicismos son aceptados temporalmente pero SIEMPRE con alternativa española o combinación bilingüe en la misma frase.

| Opción | Anglicismo presente | Alternativa española | Fórmula bilingüe disponible |
|---|---|---|---|
| 2 | No | N/A | N/A |
| 3 | "Tecnología" (pseudoanglicismo naturalizado) | Ídem en español | No aplica |
| 5 | No aplica | No aplica | No aplica |
| 6 — versión ThermoShield™ | Sí ("ThermoShield") | "EscudoTérmico™" | "NTC EscudoTérmico / ThermoShield™" |
| 6 — versión EscudoTérmico™ | No | Es la alternativa española | N/A |

**Instrucción para Solenne y Oz:** para las opciones finalistas (6 y 3), la versión española "EscudoTérmico™" es la principal. "ThermoShield" puede aparecer como subtexto de diseño o en el QR, pero el badge del tiro va en español o bilingüe español-primero. Esta instrucción es por diseño de marca (VA-1 §3 — coherencia con pilares de marca Exceline para el mercado venezolano).

---

## §R6-7 — Supuestos y límites — Refresh 2026-05-06

**Insumos consumidos en este refresh:**

- `00-brief/whatsapp/Kike conversando con Jose Miguel Canudas.txt` (2026-05-05): apertura de Canudas a evaluar variante con NTC; argumento de Kike sobre innovación, copia china y pionerismo. Insumo primario de este §Refresh.
- `00-brief/market-research/Consulta a perplexity sobre el NTC.txt` (fecha implícita: previa a 2026-05-05, generada por el Owner): formulaciones de Perplexity (Escudo Térmico Integrado, Tecnología Thermo-Safe™, opciones de copy). Insumo de inspiración — los textos de Perplexity son candidatos de partida, no claims aprobados. Varios cruzan el Claim H de Bruna.
- `Vael_VA-5_naming-funcion-termica_v1.md` (2026-05-05): VA-5 v1 + §Refresh 2026-05-05. Criterios 1–7 originales, top 3 previo, finalista única B-sin-NTC. Leído completo antes de añadir este §Refresh.
- `_governance/Bruna_gate_empaque_v1.md` §2 (Claims D y E), §7.1 (bloque NTC corregido sin temperaturas), §8 (gate "Autoprotección térmica activa*"): estado de aprobaciones vigentes, texto literal del caveat de retiro invariable, condición suspensiva Pendiente P-5 sobre "activa".
- `Vael_messaging_framework_v1.md` (VA-1): Pilar 3, §4 anti-mensajes, §1 audiencias.

**Insumos NO consultados por no estar disponibles o no ser necesarios para este §Refresh:**
- Orlan §Refresh paralelo (en producción en este mismo turno): las celdas de "Riesgo IP" en este documento quedan marcadas como "ver Orlan §Refresh." Orlan debe responder sobre: (a) disponibilidad de "EscudoTérmico" y/o "ThermoShield" como marcas registrables en Venezuela/región; (b) si "Primer protector con NTC en Venezuela" es un claim verificable a la fecha de lanzamiento; (c) si el término NTC es de dominio público en el mercado o si su comunicación por Exceline constituye genuina apertura de territorio.
- Vera: no hay nuevo insumo de Vera en este refresh. El mecanismo del NTC no cambia. La condición suspensiva del Pendiente P-5 (Bruna §8.1) sobre monitoreo continuo vs. fusible de corte único sigue pendiente e independiente de este §Refresh.
- DECISIONS.md: consultado implícitamente a través de WORKSTREAM_v5 y Bruna gate. Sin nueva decisión del Owner registrada que afecte este scope más allá de la instrucción de producir v2.2.

**Validez temporal:** Este §Refresh produce la variante B-CON-NTC (v2.2) para presentación a Canudas en reunión posterior a la Junta de hoy 2026-05-06. La Junta de hoy cerró con v2.1 (B-sin-NTC) vigente. v2.2 no reemplaza a v2.1 hasta decisión explícita de Canudas + Owner. Triggers de invalidación:
- Si Orlan confirma que un competidor venezolano ya comunicó NTC antes del lanzamiento de Exceline: la Op. 7 queda inválida y el argumento de pionero de la Op. 6 se debilita (pero no se elimina — Exceline sigue siendo el primer comunicador activo de NTC en su categoría si actúa a tiempo).
- Si Canudas rechaza la variante CON-NTC en la reunión de revisión: este §Refresh se archiva y v2.1 queda como única variante.
- Si Vera cierra Pendiente P-5 con resultado "fusible de corte único": no afecta directamente a este §Refresh (las opciones CON-NTC no usan el adjetivo "activa" de la v2.1), pero sí afecta la variante v2.1 en paralelo.

**Claims con gate pendiente de Bruna (todos los de este §Refresh):**
- Op. 1: gate mínimo (Claim D ya aprobado — verificar que recuperar el badge original con el mismo texto del retiro §8.3 no requiere nuevo gate por el cambio de contexto de decisión). Bajo riesgo.
- Op. 2: gate nuevo sobre "Escudo Térmico Integrado" como badge. Evaluar si "Escudo" + "Integrado" sin NTC visible introduce algún riesgo de interpretación. Bajo riesgo anticipado.
- Op. 3: gate sobre naming "Tecnología NTC EscudoTérmico™" — el nombre comercial ™ requiere aval del Owner sobre la decisión de naming de tecnología antes del gate de Bruna sobre el claim.
- Op. 4: gate sobre "Sensor NTC · Escudo Térmico" como formulación híbrida. El claim funcional está dentro del rango del Claim D aprobado. Bajo-medio riesgo.
- Op. 5: GATE PRIORITARIO antes de cualquier otro — Claim H en zona gris por "Previene Sobrecalentamiento" sin calificador. Vael recomienda que si Op. 5 no recibe gate limpio de Bruna, se retire del set antes de presentar a Canudas.
- Op. 6: gate sobre naming "NTC EscudoTérmico™" — mismo criterio que Op. 3. El naming es la decisión principal; el claim funcional está dentro del rango del Claim D. Medio riesgo (por naming nuevo, no por riesgo de claim).
- Op. 7: gate de Orlan requerido antes de Bruna. Sin confirmación de Orlan sobre vacancia del claim "Primero en Venezuela" al momento del lanzamiento, Bruna no puede gatear. Este claim es el más poderoso del set si la confirmación llega; es el más arriesgado si no llega.

**Ningún claim de este §Refresh está aprobado.** Todos son propuesta de Vael. La decisión de cuáles llegan a Canudas como "ejemplo de comunicación" es del Owner. El gate de Bruna se da después de la selección del Owner.

**Notificaciones de refresh pendientes post-decisión del Owner:**
- A Orlan: solicitar §Refresh sobre disponibilidad de naming "EscudoTérmico™" / "ThermoShield™" como marca + verificación de vacancia del claim "Primero en Venezuela."
- A Bruna: gate de la(s) opción(es) que el Owner seleccione para presentar a Canudas.
- A Aurelio: si Canudas aprueba la variante CON-NTC, Aurelio necesita actualizar el memo de seguimiento de Junta para reflejar el cambio de badge en v2.2.
- A Solenne: si Bruna aprueba alguna opción CON-NTC, Solenne emite delta de SO-1 con el nuevo badge y el mismo cuerpo de retiro.
- A Oz: si Solenne emite delta, Oz actualiza redline con el header del retiro correspondiente a la opción aprobada.

---

*Refresh emitido por Vael — 2026-05-06. Domain-specialist. Genteca.*
*Variante B-CON-NTC (v2.2): propuesta, no aprobada. Gate de Bruna requerido en todas las opciones. Op. 5 tiene flag de Claim H prioritario. v2.1 vigente hasta decisión de Canudas. Riesgo IP: pendiente Orlan §Refresh.*
