# BR-1 — Argumentos de venta técnicos Genteca (extracción de atlas legacy 2026-03)

**Fecha:** 2026-05-07
**Trigger:** Gate previo a uso externo de argumentario técnico extraído por Vera de Atlas 4 legacy (mercado Venezuela, marzo 2026). Solicitud directa del Owner.
**Documento evaluado:** `wiki/tech/argumentos-venta-tecnicos-INTERNO-PENDIENTE-GATE.md`
**Autor:** Bruna — Risk & Claims Governance Lead
**Marco normativo aplicado:** RISK-POLICY.md v1.0 + BR-5 Precedente #3 (comparativos directos — Genteca, 2026-05-03)
**Insumos consultados:** Documento evaluado completo; BR-5 transversal (Precedentes #1–#6); BR-2 Genteca acumulativo (entradas #1–#21); DECISIONS.md entrada 2026-05-07 (D2 y D3); RISK-POLICY.md v1.0

---

## Resumen ejecutivo

El set de 8 argumentos técnicos extraídos por Vera del Atlas 4 es, en su mayoría, sólido. Vera hizo bien su trabajo de filtro: los argumentos comparativos contra marcas específicas ya quedaron en `legacy-atlas/` y lo que llega a este gate es predominantemente física verificable, normas IEC citables y especificaciones propias de producto.

**Resultado del gate: 3 VERDE / 3 AMARILLO / 1 NARANJA / 1 ROJO.**

Los argumentos VERDE (Coordinación Tipo 2, Clase 10 para bombas, Anti-short cycle en hardware) son usables externamente hoy con ajustes menores de redacción. Los AMARILLO (Monitor de red, Relé electrónico, PTC para sumergibles) necesitan un caveat específico antes de uso externo — nada mayor, pero el caveat es obligatorio. El NARANJA (Cable sumergible) tiene un dato de red CORPOELEC sin fuente que no pasa al exterior sin evidencia o reformulación. El ROJO (COVENIN 3445) está bloqueado hasta verificación documental de la certificación — sin eso el claim es un riesgo regulatorio real.

La sección de manejo de objeciones es VERDE/AMARILLO con una nota transversal: la calculadora de costo-beneficio con placeholder "Y%" no debe usarse externamente bajo ninguna circunstancia hasta tener fuente verificable.

**Recomendación al Owner:** liberar los VERDE y AMARILLO para uso externo con los caveats literales definidos abajo. Condicionar NARANJA a reformulación que elimine el dato "210V en muchas zonas". Bloquear ROJO hasta que el área legal/técnica confirme el número de certificado COVENIN 3445 vigente y su alcance sobre los productos Exceline Profesional.

---

## Tabla resumen

| # | Argumento | Veredicto | Acción requerida antes de uso externo |
|---|---|---|---|
| 1 | Monitor de red obligatorio Venezuela | AMARILLO | Eliminar referencia a "tres causas principales" como estadística; caveat literal obligatorio sobre rol complementario |
| 2 | Relé electrónico vs bimetálico | AMARILLO | Reformular "5% de desequilibrio frecuente en CORPOELEC" como condición técnica, no estadística; caveat de fuente en el diferencial de costo |
| 3 | Coordinación Tipo 2 | VERDE | Ninguna — argumento puramente técnico/normativo; listo para uso externo |
| 4 | PTC para sumergibles | AMARILLO | Reformular "marcha en seco es el problema más frecuente" como observación técnica de diseño; eliminar "3-10×" sin fuente citada en canal externo |
| 5 | Clase 10 para bombas | VERDE | Ninguna — argumento IEC sólido; listo para uso externo |
| 6 | Anti-short cycle en hardware (GST-RR / GSC-CR) | VERDE | Ninguna — spec verificable contra ficha técnica del producto; caveat menor sobre "otros protectores" (no nombrar marcas) ya está implícito en el texto actual |
| 7 | Cable sumergible correctamente dimensionado | NARANJA | Reformular o respaldar con evidencia el dato "210V en muchas zonas"; el resto del argumento es física sólida |
| 8 | COVENIN 3445 (Exceline Profesional) | ROJO | Bloqueo total hasta verificación documental: número de certificado vigente + alcance por modelo de producto |
| 9 | Manejo de objeciones | AMARILLO | Eliminar cualquier uso externo de la calculadora con "Y% probabilidad de falla"; las demás respuestas son usables con caveats menores |

---

## Análisis detallado por argumento

---

### Argumento 1 — Monitor de red obligatorio Venezuela

**Verificabilidad técnica:** Alta. El fundamento físico es correcto e irrefutable: el relé de sobrecarga actúa por corriente anormal; la falta de fase, el desequilibrio y la subtensión son condiciones que se detectan por voltaje antes de que la corriente de falla se establezca. Esta es física de redes trifásicas verificable en IEC 60947-4-1 y en cualquier manual de maniobra industrial. La distinción "última línea de defensa" vs "primera línea de defensa" es pedagógicamente precisa y no contiene sobrepromesa.

**Comparación con terceros:** No hay. El documento no nombra ninguna marca en este argumento. La analogía airbag/cinturón no invoca a ningún competidor. Conforme con BR-5 Precedente #3.

**Datos cuantitativos sin fuente:** El texto menciona "10-60s en bimetálico vs <500ms en monitor de red" para falta de fase. Estos son tiempos de respuesta conocidos y citables en especificaciones técnicas estándar de relés y monitores de red — son datos del producto, no datos de campo. Defendibles.

El problema identificado por Vera: "tres causas principales de quema en Venezuela" no tiene estadística publicable. La frase no aparece en la sección "frase utilizable internamente" — solo en el "pendiente para gate Bruna". Sin embargo, si el equipo comercial usa oralmente el argumento con la referencia implícita a "las tres causas principales", esa afirmación causal y cuantificada ("las tres principales") no es defendible externamente sin fuente.

**Aplicabilidad a Venezuela:** La referencia al contexto venezolano es estructuralmente necesaria para el argumento — los problemas de red (falta de fase, desequilibrio, subtensión) son comunes en la red CORPOELEC. El argumento no cuantifica frecuencia; describe vulnerabilidades técnicas del relé de sobrecarga ante condiciones de red que sí existen. El caveat de contexto es menor.

**Veredicto: AMARILLO con caveat**

**Justificación:** El argumento físico es sólido y usable. El único riesgo es el deslizamiento oral hacia "tres causas principales" como afirmación estadística. El caveat previene ese deslizamiento.

**Caveat literal obligatorio para uso externo:**
"El monitor de red y el relé de sobrecarga son complementarios — no sustitutos. El relé actúa cuando la corriente de falla ya se estableció; el monitor de red actúa antes, al detectar la condición de red que la causará (falta de fase, desequilibrio, subtensión). Los tiempos citados corresponden a especificaciones técnicas estándar de dispositivos de protección. La frecuencia de estas condiciones varía según la instalación y la zona de suministro."

---

### Argumento 2 — Relé electrónico vs bimetálico

**Verificabilidad técnica:** Alta en las tres limitaciones del bimetálico. Son especificaciones de diseño conocidas y verificables:
- La no detección de desequilibrio en el bimetálico clásico está documentada en su principio de operación (solo detecta pérdida total de fase en un tiempo significativo).
- La ausencia de memoria térmica real entre ciclos de arranque sucesivos es una limitación física del bimetal.
- Los tiempos de disparo en stall (30-90 s a 7×In) se encuentran en las curvas tiempo-corriente de los productos.

El diferencial de costo "5-15% sobre el costo total del conjunto" es un cálculo razonable (relé 2-4× más caro, peso 10-20% del conjunto → diferencial 5-15%). La aritmética es correcta y los rangos son conservadores.

**Comparación con terceros:** No hay marca nombrada. El argumento es "electrónico vs bimetálico" como tecnología, no como producto de competidor. Conforme con BR-5 Precedente #3.

**Datos cuantitativos sin fuente:** "5% de desequilibrio frecuente en CORPOELEC" es el dato de riesgo en este argumento. La consecuencia técnica (50% más de temperatura en el devanado ante 5% de desequilibrio) es verificable por fórmula estándar de motores trifásicos (pérdida de par varía con el cuadrado del desequilibrio de voltaje, y la temperatura sube proporcionalmente). Pero la afirmación de que el 5% de desequilibrio es "frecuente" en CORPOELEC no tiene fuente citable.

**Aplicabilidad a Venezuela:** Justificado el contexto venezolano como motivador de la elección de protección. El argumento no afirma estadísticas sobre Venezuela; describe escenarios técnicos que el instalador reconocerá de su experiencia.

**Veredicto: AMARILLO con caveat**

**Justificación:** Las tres limitaciones técnicas del bimetálico son hechos de especificación, no observaciones de campo — son usables externamente. El dato de desequilibrio CORPOELEC necesita reformulación que lo enmarque como condición técnica observable (no estadística). El diferencial de costo puede presentarse como referencia aproximada con la aclaración correspondiente.

**Caveat literal obligatorio para uso externo:**
"Las limitaciones descritas (detección de desequilibrio, memoria térmica, tiempo de disparo en stall) corresponden al diseño estándar del relé bimetálico clásico — verificables en las curvas tiempo-corriente de especificación del dispositivo. La condición de desequilibrio de red (en torno al 5%) es una condición técnica frecuente en redes con variabilidad de suministro, que el profesional puede verificar con un multímetro en su instalación. El diferencial de costo del 5-15% es una estimación de referencia; varía según el conjunto de maniobra específico."

---

### Argumento 3 — Coordinación Tipo 2

**Verificabilidad técnica:** Alta. La distinción Tipo 1 / Tipo 2 está codificada en IEC 60947-4-1 y es conocida por cualquier ingeniero eléctrico que especifique conjuntos de maniobra. El argumento no afirma nada más allá de lo que la norma define. El beneficio operacional descrito (solo fusibles como recambio vs contactor completo) es la consecuencia directa y verificable de esa especificación.

**Comparación con terceros:** No hay marca nombrada. El argumento compara Tipo 1 con Tipo 2 como categorías normativas, no como productos de competidores.

**Datos cuantitativos sin fuente:** "Diferencial de 15-25% del conjunto de maniobra" para Tipo 2 vs Tipo 1 es el único dato cuantitativo. Este diferencial es una estimación de referencia del mercado; no es una estadística que requiera fuente académica para un argumentario de ventas técnico. Es defendible como referencia aproximada con la aclaración de que varía según fabricante y diseño.

**Aplicabilidad a Venezuela:** No hay referencia específica a CORPOELEC o al contexto venezolano en este argumento — el beneficio operacional (rearranque rápido vs esperar repuesto) es universal y no requiere ningún caveat de contexto.

**Veredicto: VERDE**

**Justificación:** Argumento basado 100% en la norma IEC 60947-4-1. El diferencial de costo es una referencia aproximada estándar del sector, no una afirmación estadística. No hay comparativo con terceros. No hay dato de campo no verificable. El único refinamiento sugerido es presentar el diferencial de costo como "referencia aproximada" en canales donde la audiencia exija precisión (ficha técnica, especificación para licitación) — pero en argumentario de ventas el argumento está listo.

---

### Argumento 4 — PTC para sumergibles

**Verificabilidad técnica:** Alta en el mecanismo físico. La secuencia es correcta e irrefutable:
1. Marcha en seco → pérdida de refrigeración hidráulica → temperatura del devanado sube.
2. La corriente del motor baja (o se mantiene) porque la carga hidráulica cae — esto es contravintuito para el técnico no especializado pero es física real: sin agua que bombear, el motor trabaja en vacío.
3. El relé de sobrecarga calibrado para In no detecta la condición — la corriente está en rango normal.
4. El PTC mide temperatura real del devanado — detecta la condición que el relé no puede detectar.

La temperatura de disparo del PTC (150-160°C citada en el documento) corresponde a termistores PTC estándar para protección de motores — verificable en especificaciones de componentes.

**Comparación con terceros:** No hay.

**Datos cuantitativos sin fuente:** Dos problemas:
- "Marcha en seco es el problema más frecuente" en sumergibles: observación de campo sólida, ampliamente reconocida en la industria de bombeo, pero sin fuente estadística publicable.
- "3-10× más costoso que motor superficial equivalente": rango cualitativo razonable (los motores sumergibles son de diseño especial, con sellado y construcción específica), pero sin catálogo de precios citado.

**Aplicabilidad a Venezuela:** No hay referencia específica al contexto venezolano — el argumento es aplicable universalmente.

**Veredicto: AMARILLO con caveat**

**Justificación:** El mecanismo físico es el argumento fuerte y está intacto. Las dos afirmaciones sin fuente ("el problema más frecuente", "3-10× más costoso") pueden reformularse sin perder el argumento. El caveat también cubre la presentación del costo relativo como referencia, no como estadística.

**Caveat literal obligatorio para uso externo:**
"La marcha en seco es uno de los modos de falla más dañinos en bombas sumergibles, porque la corriente del motor — el parámetro que el relé de sobrecarga monitorea — no sube cuando falta el agua: la carga hidráulica desaparece y la corriente puede bajar o mantenerse. Solo el termistor PTC en el devanado detecta el calentamiento resultante. Los motores sumergibles tienen costos de reemplazo significativamente superiores a motores superficiales equivalentes por su diseño especial (sellado, construcción); el costo del PTC representa una fracción pequeña del valor del equipo protegido."

---

### Argumento 5 — Clase 10 para bombas

**Verificabilidad técnica:** Alta. La tabla Clase 10 / Clase 20 con tiempos de disparo a 7.2×In está codificada en IEC 60947-4-1 Tabla VIII. El tiempo de arranque de una bomba centrífuga (2-5 segundos) es un dato del equipo, verificable en la curva de arranque del motor acoplado. El razonamiento (Clase 20 diseñada para cargas de alta inercia; Clase 10 correcta para bombas centrífugas) es estándar en la ingeniería de selección de protecciones.

**Comparación con terceros:** No hay.

**Datos cuantitativos sin fuente:** Todos los datos cuantitativos citados provienen de la norma IEC o de la física del equipo. No hay estimaciones de campo no respaldadas.

**Aplicabilidad a Venezuela:** No hay referencia al contexto venezolano — el argumento es universal.

**Veredicto: VERDE**

**Justificación:** Argumento 100% normativo y técnico. Los tiempos de disparo son de especificación IEC. El tiempo de arranque de la bomba centrífuga es un dato del equipo. El riesgo de daño ante stall con Clase 20 es una consecuencia directa de la comparación de tiempos. No hay afirmación de campo sin fuente, no hay comparativo con marcas. Listo para uso externo, incluyendo fichas técnicas y especificaciones formales.

---

### Argumento 6 — Anti-short cycle en hardware (productos GENTECA)

**Verificabilidad técnica:** Alta, y este es el argumento diferenciador más sólido del set. El fundamento físico es correcto:
- Cada arranque de compresor genera calor proporcional a la energía disipada durante el período de corriente de arranque (5-7×In durante la aceleración) — verificable con cálculo de energía.
- Ciclos cortos repetidos acumulan calor más rápido de lo que el motor puede disipar.
- El tiempo mínimo de reconexión de 180 segundos restringido por hardware es un diferenciador verificable contra la ficha técnica del GST-RR y GSC-CR.

La afirmación sobre "otros protectores ajustables" que permiten configurar el temporizador desde 0 o 5 segundos es una descripción funcional de categorías de producto, no una afirmación sobre una marca específica. Es descriptiva del tipo de producto, no comparativa de marca.

**Comparación con terceros:** No hay marca nombrada. El texto dice "otros protectores ajustables" como categoría — conforme con BR-5 Precedente #3.

**Datos cuantitativos sin fuente:** "180 segundos restringido por hardware" es verificable contra la ficha técnica del producto. "15-30 segundos de operación a plena carga equivalente" por arranque es una estimación razonable de la energía disipada durante el período de corriente de arranque — no es una cifra de laboratorio, pero es del orden correcto y no se presenta como dato de precisión.

**Aplicabilidad a Venezuela:** No hay referencia al contexto venezolano en este argumento.

**Veredicto: VERDE**

**Justificación:** Argumento basado en spec de producto verificable (180 s por hardware en GST-RR/GSC-CR) + física del arranque de compresor. No hay comparativo con marcas. La referencia a "otros protectores ajustables" es una descripción de categoría funcional, no un comparativo de marca. El único refinamiento es verificar que el dato "180 s por hardware" esté efectivamente en la ficha técnica publicada del producto antes de usarlo en un canal donde la audiencia pueda verificarlo — pero Vera ya confirmó la atribuibilidad a la ficha técnica del producto.

**Nota:** Para canales donde se presente material impreso del producto, confirmar que la ficha técnica del GST-RR y GSC-CR sea la versión vigente (dado el aviso DECISIONS.md sobre GST-RD / GST-RG en estado incierto — los modelos RR y CR mencionados aquí son distintos de los RD y RG en estado incierto, pero verificar que no haya confusión de nomenclatura antes del uso externo).

---

### Argumento 7 — Cable sumergible correctamente dimensionado

**Verificabilidad técnica:** Alta en el núcleo físico. La fórmula ΔV = I × R_cable es física básica. Las consecuencias de subtensión (par ∝ V², corriente sube para compensar, sobrecalentamiento) son verificables. La norma de diseño (caída máxima 3% de Vn) es estándar en instalaciones eléctricas (IEC 60364 y equivalentes). El cálculo de sección mínima para 60 m / 5 HP / 220V (≥6 mm²) puede verificarse con tablas de sección vs caída de tensión para las condiciones dadas.

**Comparación con terceros:** No hay.

**Datos cuantitativos sin fuente:** El dato de riesgo principal: "CORPOELEC ya en 210V en muchas zonas". Esta afirmación es plausible y bien conocida en el sector eléctrico venezolano, pero "en muchas zonas" no tiene respaldo estadístico publicable. Es el mismo patrón del Argumento 1 (datos de campo sobre la red venezolana sin fuente formal) pero aquí el dato es estructuralmente más central al argumento — el ejemplo numérico (210V + 10V caída en cable = 200V → 91% Vn → par 83%) depende de ese supuesto de partida.

Si un técnico externo le pregunta al equipo comercial "¿en qué zonas exactamente?", no hay respuesta verificable.

**Aplicabilidad a Venezuela:** El argumento es inherentemente específico al contexto venezolano — ese es su valor. El problema es que la anchura de ese contexto ("muchas zonas") necesita acotarse o reformularse.

**Veredicto: NARANJA con condición**

**Justificación:** El argumento físico (la sección del cable como parámetro de diseño del sistema) es sólido y el cálculo de impacto de subtensión es correcto. El riesgo es el dato CORPOELEC "210V en muchas zonas" presentado como premisa sin fuente. Hay dos caminos para desbloquearlo:

**Opción A (reformulación, usable hoy):** Reformular eliminando el dato cuantitativo de CORPOELEC como premisa y convirtiendo el argumento en una recomendación de diseño para instalaciones en redes con variabilidad de tensión:

"En instalaciones donde la tensión de suministro puede estar por debajo del nominal (condición común en redes con variabilidad), una caída adicional de 10V en el cable puede dejar al motor a 91% de Vn. A esa tensión, el par de arranque es 83% del nominal (par ∝ V²) y la corriente sube para compensar. Diseñar siempre con la caída de tensión en cable dentro del 3% del nominal — para 60 metros de profundidad y 5 HP a 220V, eso implica sección mínima de 6 mm²."

**Opción B (con evidencia, más fuerte pero requiere acción):** Solicitar a Orlan una referencia verificable sobre tensión de suministro en la red CORPOELEC (puede ser un informe MPPEE, una norma COVENIN de calidad de energía, o datos de CORPOELEC mismo) que respalde el dato "210V en zonas de variabilidad". Si existe ese respaldo, el argumento con el dato cuantitativo específico pasa a AMARILLO.

**Condición para uso externo:** Opción A (reformulación) o Opción B (evidencia). Sin una de las dos, el argumento no pasa a uso externo en la formulación actual.

---

### Argumento 8 — COVENIN 3445 (Exceline Profesional)

**Verificabilidad técnica:** Media. La existencia de COVENIN 3445 como norma venezolana para dispositivos de supervisión y protección eléctrica es verificable en el catálogo FONDONORMA/SENCAMER. Sin embargo, el documento no presenta:
- Número de certificado o declaración de cumplimiento formal para los modelos Exceline Profesional específicos.
- Año de publicación / vigencia actual de COVENIN 3445 (las normas venezolanas pueden estar desactualizadas o en revisión).
- Alcance específico de la norma sobre los tipos de dispositivos en la línea Exceline Profesional.

El documento mismo lo señala como pendiente: "verificar vigencia COVENIN 3445 + verificar declaración formal de cumplimiento por parte de Genteca antes de uso externo."

**Comparación con terceros:** Hay un comparativo implícito en la frase "Los productos importados europeos cumplen IEC; los americanos cumplen UL. Para instalaciones formales en Venezuela, la especificación técnica local requiere COVENIN." Esta formulación implica que los productos europeos/americanos no cumplen COVENIN, lo cual puede ser factualmente incompleto (algunos productos importados pueden tener doble certificación o aceptación equivalente en Venezuela). El comparativo es suave pero necesita matizarse.

**Datos cuantitativos sin fuente:** No hay datos cuantitativos — el riesgo es regulatorio, no cuantitativo.

**Aplicabilidad a Venezuela:** El argumento es específico y valioso para el mercado venezolano. Su valor comercial es real — si la certificación es verificable, es un diferenciador legítimo frente a productos importados sin certificación local formal.

**Veredicto: ROJO**

**Justificación:** Hacer un claim de cumplimiento normativo (COVENIN) sin verificar que el certificado existe, está vigente y aplica a los modelos específicos del producto es el riesgo regulatorio más alto del set. La BR-2 entrada #13 establece precedente directo: "Bruna no puede gatear un claim de certificación sin verificar que la certificación existe, está vigente y aplica a los modelos específicos." Ese criterio sentado para la línea GSM aplica con igual fuerza a Exceline Profesional.

Si un distribuidor, especificador o cliente solicita el número de certificado COVENIN 3445 y Genteca no lo puede proveer, el claim genera un daño reputacional inmediato con ese cliente. Si la certificación no existe en la forma declarada, el claim tiene potencial regulatorio adverso bajo la Ley de Protección al Consumidor.

**Alternativa viable (condición para desbloquear):**
1. El área técnica/legal de Genteca verifica: (a) vigencia actual de COVENIN 3445, (b) número de certificado o declaración de conformidad formal para los modelos Exceline Profesional específicos, (c) si el certificado aplica a todos los modelos o solo a algunos.
2. Una vez verificado, el claim se reformula con precisión: "Exceline Profesional cumple con COVENIN 3445 [número de certificado]. Certificación verificada para los modelos [lista específica]."
3. El comparativo con IEC/UL se reformula como complementario: "Diseñado bajo norma venezolana COVENIN 3445, además de cumplir con los parámetros de desempeño de IEC [norma aplicable]."

**Flag para el Owner:** esta verificación no puede hacerla Bruna ni Vera internamente — requiere que el responsable técnico/legal de Genteca consulte el estado formal del certificado en SENCAMER/FONDONORMA.

---

### Argumento 9 — Manejo de objeciones (sección completa)

**Evaluación general:** La sección de manejo de objeciones contiene tres patrones de respuesta. Se evalúa el conjunto.

**Verificabilidad técnica:** Alta en las dos primeras objeciones. La respuesta a "Ya tengo relé térmico, es suficiente" es el Argumento 1 reformulado como objeción — mismos méritos (AMARILLO). La respuesta a "El precio es muy alto" es un reencuadre de valor sin afirmaciones técnicas arriesgadas: no cuantifica la protección, no promete resultado, no compara con marcas. El razonamiento "fracción pequeña del valor del equipo" es correcto y verificable en contexto.

**Comparación con terceros:** La respuesta a "Tengo experiencia con genéricos y no me han fallado" menciona "hardware genérico" como categoría — sin nombrar marcas, conforme con BR-5 Precedente #3. El propio documento ya marca en nota: evitar la calculadora "Y% probabilidad de falla" del Atlas 4 (con datos placeholder) — esta instrucción es correcta y debe reforzarse como regla absoluta.

**Datos cuantitativos sin fuente:** El aviso ya está en el documento: "Y% probabilidad de falla en 3 años" es placeholder, no dato real. Este placeholder NO pasa a uso externo bajo ninguna formulación. Tampoco debe circular internamente con la apariencia de dato real. La calculadora debe marcarse como herramienta en desarrollo hasta que exista fuente estadística verificable.

**Aplicabilidad a Venezuela:** La respuesta a genéricos incluye dos preguntas diagnósticas al cliente ("¿la red tiene desequilibrio medido?", "¿algún motor se quemó en 2 años?") — esto es técnicamente honesto y no hace afirmación estadística. Si la respuesta del cliente a la segunda es "sí", el equipo comercial puede usar los Argumentos 1 y 2 con sus respectivos caveats.

**Veredicto: AMARILLO con caveat transversal**

**Justificación:** Las respuestas son en su mayoría sólidas. El riesgo único y específico es la calculadora con placeholder. El caveat refuerza la instrucción ya presente en el documento y la hace obligatoria.

**Caveat literal obligatorio transversal para la sección de objeciones:**
"La calculadora de costo-beneficio del Atlas 4 que contiene 'Y% probabilidad de falla en 3 años' NO es un dato real — es un placeholder de la versión de marzo 2026. No usar ese cálculo ni esa cifra (en ninguna forma: oral, escrita o en material de presentación) hasta que exista una fuente estadística verificable (encuesta de campo documentada, informe de tasa de falla de un seguro o distribuidor, o estudio de campo propio). El uso de ese placeholder como dato de venta es una afirmación cuantitativa sin respaldo y puede generar reclamo de cliente por información engañosa."

---

## Riesgos transversales detectados

**1. Patrón "dato de campo venezolano sin fuente":** Afecta a los Argumentos 1, 2 y 7 (y en menor medida a 4). El patrón es: observación de campo sólida y reconocida por practicantes del sector (la red CORPOELEC tiene variabilidad, el desequilibrio es frecuente, los motores sumergibles se queman por marcha en seco) pero sin estadística publicable. Estos datos son valiosos en entrenamiento interno — el equipo comercial los reconoce porque los vive. El riesgo es que en uso externo con clientes formales o en material escrito, la ausencia de fuente los hace vulnerables.

**Regla transversal sugerida para el equipo comercial:** "Los datos sobre la red venezolana (CORPOELEC, tensión, desequilibrio, frecuencia de eventos) son argumentos de contexto, no de especificación. No presentarlos como estadísticas; presentarlos como condiciones técnicas observables que el profesional puede verificar en su propia instalación." Esta regla cubre los Argumentos 1, 2 y 7 con un solo principio.

**2. Distinguir "comparativo de tecnología" vs "comparativo de marca":** El set respeta el Precedente #3 (no nombra marcas). El riesgo es que en uso oral, el equipo comercial deslice al comparativo de marca (ej. "el electrónico de Schneider vs el bimetálico genérico"). Los caveats de los Argumentos 1 y 2 previenen este deslizamiento en material escrito; la formación interna debe reforzarlo para el uso oral.

**3. Certificaciones como claims de marketing:** El Argumento 8 (COVENIN) es el único del set con riesgo regulatorio real. El precedente establecido en BR-2 #13 (GSM) aplica directamente. La regla es simple: sin documento de certificación verificable con número y alcance específico, ningún claim de cumplimiento normativo sale al exterior.

---

## Recomendación al Owner

**Argumentos usables HOY externamente sin cambios adicionales:**
- Argumento 3 — Coordinación Tipo 2 (VERDE)
- Argumento 5 — Clase 10 para bombas (VERDE)
- Argumento 6 — Anti-short cycle en hardware GST-RR/GSC-CR (VERDE, con verificación de nomenclatura de modelos vs posible confusión con GST-RD/RG en estado incierto — acción menor del Owner)

**Argumentos usables HOY externamente CON los caveats literales definidos arriba:**
- Argumento 1 — Monitor de red (AMARILLO): usar caveat Arg. 1.
- Argumento 2 — Relé electrónico vs bimetálico (AMARILLO): usar caveat Arg. 2.
- Argumento 4 — PTC para sumergibles (AMARILLO): usar caveat Arg. 4.
- Argumento 9 — Manejo de objeciones (AMARILLO): aplicar caveat transversal sobre la calculadora "Y%".

**Argumentos que requieren acción del Owner antes de uso externo:**
- Argumento 7 — Cable sumergible (NARANJA): elegir entre Opción A (reformulación sin dato CORPOELEC) o Opción B (evidencia verificable del dato). Opción A no requiere trabajo adicional de Vera/Orlan — es solo una reformulación que elimina el dato cuantitativo sin fuente. Si el Owner opta por Opción A, Bruna puede gatear el argumento reformulado con un AMARILLO.
- Argumento 8 — COVENIN 3445 (ROJO): el Owner debe verificar con el área técnica/legal de Genteca el número de certificado y su vigencia. Bruna no puede proceder sin ese dato. Es el único bloqueo real del set.

**¿Se requiere BR-2 formal (decisión de gate) antes de uso externo?**
Sí. Este BR-1 es el assessment. Para que los argumentos AMARILLO y los VERDE sean formalmente usables en material externo (decks de ventas, fichas comerciales, material de distribuidor), el Owner debe autorizar el BR-2 correspondiente. Los argumentos VERDE pueden gatearse en el mismo BR-2. Los AMARILLO se gatean con los caveats literales ya definidos en este BR-1. Los NARANJA y ROJO permanecen bloqueados hasta las acciones descritas arriba.

---

## Precedente y referencia cruzada

**BR-5 Precedente #3 (gate GME — comparativos directos):** Aplicado transversalmente al set. Todos los argumentos evaluados están libres de comparativos de marca directos — Vera hizo correctamente el filtro previo. El Precedente #3 se confirma como criterio vigente; no se sienta precedente nuevo por este gate.

**BR-2 Genteca entrada #13 (claims de certificación):** Precedente directo para el Argumento 8 (COVENIN 3445). La regla es idéntica a la que aplica a la línea GSM.

**DECISIONS.md entrada 2026-05-07 (D2 — argumentos de venta):** Este BR-1 es la materialización del mandato de esa entrada: "Bruna delegada para BR-1 sobre los argumentos extraídos antes de cualquier uso externo."

**Nota sobre BR-5:** Este gate no sienta precedentes nuevos que requieran actualización del BR-5 transversal. Los casos aquí evaluados aplican criterios ya establecidos (Precedentes #1–#4). Si el Owner opta por formalizar la "regla de datos de campo sin fuente" como precedente transversal, Bruna puede producir una entrada nueva en BR-5 en el próximo ciclo.

---

## References

- RISK-POLICY.md v1.0 (2026-04-25) — gobernanza general: §2 clasificación de acciones, §3 manejo de errores
- DECISIONS.md entrada 2026-05-07 — integración atlas legacy, D2 (argumentos de venta) y D3 (GST-RD/RG)
- BR-5 transversal — `04-system/03-governance/BR-5_regla-claims-superlativos-mercados-opacos_2026-05-03.md`: Precedentes #1, #2, #3, #4, #5, #6
- BR-2 Genteca — `03-projects/genteca/_governance/2026-05-03_genteca_claim-approval-log_v1.md`: entradas #13 (certificaciones, precedente para Arg. 8), #1–#12 y #15–#21 (contexto de criterio)
- Documento evaluado: `02-knowledge-base/02-domains/01-genteca/wiki/tech/argumentos-venta-tecnicos-INTERNO-PENDIENTE-GATE.md` v0.1 (2026-05-07)
- IEC 60947-4-1 (referenciada en Argumentos 3 y 5 — citada en el documento fuente)
- COVENIN 3445 — verificación documental pendiente (bloqueo Argumento 8)

---

*Bruna — Risk & Claims Governance Lead — Sistema /RAUL/*
*BR-1 producido: 2026-05-07. Dominio: Genteca. Trigger: gate de argumentario de ventas técnicos extraído de Atlas 4 legacy (marzo 2026) por Vera en integración 2026-05-07.*
*Próxima acción: Owner autoriza BR-2 con decisiones formales de gate. Los VERDE y AMARILLO con caveats definidos en este BR-1 están listos para su registro en BR-2.*
