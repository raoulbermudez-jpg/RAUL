# Messaging Framework + Guardrails de Claims — GSM-MB / GSM-RB / GSM-RF / GSM-RE
**Documento:** Vael_messaging_framework_v1 (VA-1 + VA-5 integrados)
**Fecha:** 2026-05-03
**Scope:** Empaque (tiro + retiro) — cuatro modelos, copy base idéntico
**Audiencias cubiertas:** Instalador técnico (primario), consumidor final residencial (secundario), Junta Directiva (interna — sustento)
**Workstream:** WORKSTREAM_v5_innovaciones — Paso 4 del pipeline CSC
**Insumos aguas arriba:** Vera_brief_tecnico_v1.md · Orlan_competencia_v1.md · WORKSTREAM_v5_innovaciones.md · delta_v4_NTC-inverter.md · WhatsApp Canudas 02-05-2026 · brand wiki 01-identidad-de-marca.md

---

## Parte I — VA-1: Messaging Framework

---

### §1. Los cinco pilares y sus RTBs

---

#### Pilar 1 — Velocidad ante parpadeos: el dato cuantitativo que define la generación

**Eje narrativo:** El GSM nueva generación responde ante parpadeos en menos de 30 ms. Eso no es una mejora incremental: es un salto de una orden de magnitud sobre la generación anterior (150 ms) y sobre cualquier competidor venezolano publicado. La velocidad es la innovación central y el argumento técnico que sostiene todo lo demás.

**RTBs:**
- Vera §2.2: mejora documentada de 150 ms a < 30 ms en tiempo de desconexión ante parpadeos/inestabilidad. El dato es el umbral de spec de I&D.
- Vera §2.3: las dos formulaciones "< 30 ms" y "< 0,03 s" son equivalentes; la segunda fue acordada por Canudas y el Owner como formulación para empaque.
- Orlan Sección 1 + Sección 7: ningún competidor venezolano publica un tiempo de desconexión ante parpadeos igual o inferior a 30 ms. WellSpec, el competidor más agresivo, publica 200-300 ms como "el más rápido de Venezuela". Powest: 1.000 ms. Breakermatic: 1.000-1.500 ms.
- Orlan Sección 2: el claim "El más rápido ante parpadeos (< 0,03 s)" es la formulación más defendible porque combina superlativo + dato cuantitativo propio verificable.

**Categoría diferenciación (OL-3):** Diferenciado

**Por qué este pilar es defendible:** El dato cuantitativo propio existe, fue medido por I&D (pendiente formalización documental — ver §7 Supuestos), y ningún competidor rastreado publica un valor comparable. El superlativo está respaldado por ausencia de contraejemplos verificables, no por afirmación vacía.

---

#### Pilar 2 — Protección de tecnología inverter: el pilar técnico con razón causal

**Eje narrativo:** El GSM protege equipos con tecnología inverter específicamente porque su respuesta ultra-rápida ante parpadeos minimiza la exposición de la electrónica de control inverter a condiciones de inestabilidad de red. No es un claim de aplicación genérico: es el argumento técnico que los competidores que dicen "para inverter" no pueden dar.

**RTBs:**
- Vera §2.4: los equipos inverter necesitan estabilidad en el bus de continua interno; una caída brusca de voltaje puede causar errores o disparos del sistema de protección del inverter; la respuesta de < 30 ms garantiza apertura del circuito antes de dos ciclos de red (1 ciclo 60 Hz = ~16,7 ms).
- Orlan Sección 4: Avtek y Breakermatic dicen "para inverter" como segmentación de aplicación, sin sustento cuantitativo. Genteca es el único que puede vincular el claim inverter a un dato de velocidad de respuesta.
- Orlan Sección 4, hallazgo: "el diferenciador es el porqué (velocidad), no el claim en sí".

**Categoría diferenciación (OL-3):** Diferenciado (por razón causal cuantificada, aunque el claim de aplicación inverter per se es Paridad)

**Por qué este pilar es defendible:** El claim "Protege tecnología Inverter" no es nuevo en el mercado, pero el argumento que lo sostiene sí lo es. Sin la velocidad de < 30 ms como RTB, este pilar se degrada a paridad. Los dos pilares 1 y 2 deben mantenerse conectados causalmente: si se separan, el Pilar 2 pierde su ventaja diferencial.

**Nota arquitectónica para Atlas y Oz (brief visual en §4):** la conexión causal velocidad-inverter es el vínculo gráfico que el Owner solicita explícitamente. Esta nota sirve de base para ese brief.

---

#### Pilar 3 — Autoprotección térmica NTC: territorio en blanco de comunicación

**Eje narrativo:** El GSM nueva generación incorpora un sensor NTC junto al relé de potencia que detecta calentamiento excesivo y desconecta la carga antes de que el relé se destruya. Ningún competidor venezolano comunica esta tecnología. El término NTC crea distinción técnica real y efecto de curiosidad que activa el escaneo del QR y la lectura del retiro.

**RTBs:**
- Vera §1.1 y §1.2: el NTC es un termistor de coeficiente negativo ubicado junto al relé de potencia; cuando el relé se calienta más allá del umbral de diseño, la caída de resistencia del NTC activa la desconexión.
- Vera §1.3(a): función primaria = autoprotección del protector mismo (relé de potencia).
- Vera §1.3(b): función secundaria = protección indirecta del cableado ante sobrecorrientes prolongadas.
- Vera §1.6: temperatura de operación hasta 55 °C respaldada por datasheets GSM-RE y GSM-RECS.
- Orlan Sección 3: cero competidores venezolanos o regionales comunican NTC, protección térmica o tecnología equivalente en empaque ni datasheet público.
- WhatsApp Canudas 02-05-2026: "protege al protector y al cableado de una condición de trabajo para la cual no fueron diseñados: un calor excesivo que puede llevar a la destrucción de estos."

**Categoría diferenciación (OL-3):** Diferenciado (espacio en blanco de comunicación)

**Por qué este pilar es defendible:** La tecnología existe, su mecanismo es técnicamente correcto, y el término NTC es verificable. El asterisco obligatorio limita el riesgo de sobrepromesa al derivar la explicación completa al retiro y al QR.

---

#### Pilar 4 — Completitud de la protección: el marco que da sentido a los tres

**Eje narrativo:** La nueva generación del GSM no suma una función a lo ya existente: suma dos capas de protección que cubren amenazas específicas del sistema eléctrico venezolano (parpadeos + calentamiento excesivo) que la generación anterior no cubría. "La protección más completa" tiene sustento en esa acumulación real de capas.

**RTBs:**
- Vera §3.1: las tres frases de la Alternativa A (< 0,03 s, Protege Inverter, Sensor NTC) son todas innovaciones reales sobre los datasheets previos.
- Brand wiki: los atributos compartidos de Exceline son "Confiable · Robusto · Duradero"; el eslogan de Exceline Residencial es "La ÚNICA protección confiable en Venezuela". El claim de completitud es coherente con ese eje de marca.
- WORKSTREAM_v5 §Decisiones cerradas: el claim "Nuevo" tiene sustento en dos innovaciones medibles que no existían en versiones anteriores.

**Categoría diferenciación (OL-3):** Paridad → Diferenciado por acumulación (el claim "más completa" en solitario es Paridad; sustentado por los tres sub-claims de los pilares 1-3, se convierte en Diferenciado)

**Punto débil estructural marcado abiertamente:** "La protección más completa" en solitario, sin los tres sub-claims que la sustentan, sería un superlativo cualitativo difícil de defender. Su coherencia depende de que el empaque desarrolle explícitamente qué hace de ella "la más completa". La Alternativa A funciona exactamente así: la lengüeta enuncia el superlativo y el frente lo justifica con tres frases concretas. Esa dependencia estructural es una fortaleza de arquitectura, no una debilidad — pero solo si los tres sub-claims sobreviven al gate de Bruna y no se recortan por restricciones de espacio.

---

#### Pilar 5 — Honestidad técnica: el argumento que gana la confianza del instalador

**Eje narrativo:** El GSM dice lo que hace y delimita lo que no hace. El asterisco de NTC, el caveat de parpadeos (no de sobre/subtensión), la acotación al retiro — todo eso es señal de marca para el instalador técnico que sabe distinguir entre un fabricante que sobreafirma y uno que puede respaldar lo que dice.

**RTBs:**
- Vera §4: caveats literales listos para retiro que delimitan cada claim con precisión técnica.
- Orlan §6.3: el técnico es la audiencia primaria para GSM-RB/RF; el claim de "nuevo" debe ser creíble para un profesional que conoce el producto hace décadas.
- Orlan §6.3: "las dos innovaciones son el sustento de credibilidad del claim nuevo".

**Categoría diferenciación (OL-3):** Diferenciado (en un mercado donde los competidores no publican datos medibles, la honestidad técnica cuantificada es diferenciación)

**Por qué este pilar es defendible:** No es un pilar de comunicación directa al consumidor final. Es el pilar de arquitectura que respalda la credibilidad de todos los demás. Para la Junta Directiva, es la garantía de que Genteca puede defender cada claim si alguien lo reta.

---

### §2. Mensajes base por audiencia

---

#### Audiencia: Instalador técnico (primario — compra, recomienda, instala)

**Mensaje principal:** El nuevo GSM responde en menos de 30 milisegundos ante parpadeos — una mejora de 5 veces sobre la versión anterior — con sensor NTC que protege al propio protector y protección específica para tecnología inverter.

**Tono:** Técnico-directo. Sin adjetivos vacíos. El dato cuantitativo es el argumento. La especificación técnica (ms, NTC, inverter) es el idioma del instalador.

**RTBs primarios:** Pilar 1 (< 30 ms medido por I&D), Pilar 3 (NTC junto al relé), Pilar 2 (inverter + velocidad como causa-efecto)

**Pilares que activa:** Pilares 1, 2, 3, 5

**Qué le importa al instalador que este mensaje resuelve:** Tiene clientes con equipos inverter que se dañan con parpadeos; necesita un argumento técnico concreto para recomendar el cambio al cliente que ya tiene un protector anterior. El dato de < 30 ms vs. 150 ms es ese argumento.

**Qué evitar con el instalador:** Frases de marketing sin respaldo numérico ("el mejor", "incomparable", "revolucionario"). Afirmar que protege el motor directamente. Equiparar el NTC con un térmico electromecánico completo.

---

#### Audiencia: Consumidor final residencial (secundario — compra en ferretería o tienda)

**Mensaje principal:** El GSM nuevo es el más rápido ante los parpadeos que dañan los equipos modernos, y trae un sensor especial que protege al propio protector para que no se destruya con el calor.

**Tono:** Cercano-pragmático. Sin tecnicismos innecesarios. El beneficio se enuncia en términos de lo que pasa en casa: el equipo se protege mejor, el protector dura más.

**RTBs primarios:** Pilar 1 (rápido ante parpadeos — imagen de la velocidad), Pilar 3 (sensor especial = tranquilidad de que el protector también se protege), Pilar 4 (más completo que el anterior)

**Pilares que activa:** Pilares 1, 3, 4

**Qué le importa al consumidor que este mensaje resuelve:** No sabe qué es NTC ni qué son los parpadeos, pero sabe que sus equipos se dañan con las fluctuaciones eléctricas y que los protectores "se queman". El mensaje debe conectar la velocidad con protección y el NTC con durabilidad del propio aparato.

**Alerta de insight de consumidor (Orlan §6.3):** Aproximadamente el 40% del mercado entiende "protección térmica" como protección del motor. El copy que llegue a este segmento debe usar "autoprotección" (el protector se cuida a sí mismo) o "sensor NTC incorporado" (enigmático pero no confuso) en lugar de "protección térmica" a secas.

**Qué evitar con el consumidor final:** "Sensor NTC" sin asterisco ni explicación de retiro (genera confusión o expectativa incorrecta). "Protege al motor" o "protege a la carga" (prohibido por Vera). Tecnicismos sin ancla visual o de contexto.

---

#### Audiencia: Junta Directiva (interna — necesita el sustento para aprobar la propuesta)

**Mensaje principal:** Las dos innovaciones (NTC + < 30 ms) están respaldadas técnicamente, son verificables por el laboratorio propio, no tienen equivalente publicado en el mercado venezolano, y se comunican con un copy que es honesto, acotado y defendible ante cualquier cuestionamiento de consumidor o distribuidor.

**Tono:** Ejecutivo-estratégico. Datos, riesgos identificados, mitigaciones. Sin retórica de marketing.

**RTBs primarios:** Vera (brief técnico consolidado, caveats listos), Orlan (landscape competitivo, ningún competidor publica < 30 ms), WORKSTREAM_v5 §Regla de gateo (decisión Owner: el laboratorio puede refutar), Bruna (gate de claims pendiente — ver §6).

**Pilares que activa:** Pilares 1, 2, 3, 4, 5

**Qué le importa a la Junta que este mensaje resuelve:** ¿Es el claim "el más rápido" sostenible si alguien lo reta? ¿Hay riesgo de sobrepromesa con el NTC? ¿Las alternativas A y B son genuinamente distintas o solo cosméticas?

**Lo que el framework entrega a la Junta:** Respuesta estructurada a esas tres preguntas — con arquitectura de claims, diferenciación entre alternativas y riesgos explícitos.

---

### §3. Jerarquía de mensajes: qué va dónde

---

#### Jerarquía en tiro (frente del empaque)

**Central — siempre presente en el tiro:**
- Dato de velocidad: "El más rápido ante parpadeos (< 0,03 s)" — es el claim diferenciador número uno, el que tiene RTB más sólido y el que ningún competidor puede igualar con dato publicado.
- Claim de inverter: "Protege tecnología Inverter" — segundo en jerarquía; su fuerza depende de estar en proximidad al dato de velocidad (son causa-efecto).
- Claim NTC: "Sensor NTC incorporado*" — tercero; activa curiosidad técnica y actúa como señal de innovación adicional para el instalador.

**Lengüeta:**
- "Nuevo. La Protección más completa" — funciona como sobre-título que enmarca los tres sub-claims. Su credibilidad depende de que los tres sub-claims estén visibles en el tiro; sin ellos, quedaría como superlativo vacío.

**Secundario (en el tiro si el espacio lo permite, de lo contrario en retiro):**
- Dato de temperatura de operación hasta 55 °C — relevante para mercado venezolano pero no es una innovación nueva; pertenece al retiro.
- Supresor de picos — función existente, no nueva; no debe competir con los tres claims de innovación.

#### Jerarquía en retiro

**Obligatorio en retiro:**
- Nota de asterisco NTC (caveats de Vera §4, Caveat 1 + Caveat 2 combinados): delimitar que NTC protege al protector y a la instalación, no directamente a la carga pequeña.
- Acotamiento del tiempo < 30 ms a parpadeos (Caveat 3 de Vera): distinguir del tiempo de desconexión ante sobre/subtensión (que sigue siendo 0,4-3 s).
- Referencia al QR: vía de ampliación técnica para todos los claims.

**Complementario en retiro:**
- Bullet de características con dato de tiempo de respuesta < 30 ms (delta v4, Sección D) — para el lector técnico que busca la especificación.
- Caveat de cableado (Vera §4, Caveat 4) — relevante para el instalador, no para el consumidor final.

**Solo off-empaque (QR / web / argumentario de ventas — no en empaque):**
- Comparativo explícito vs. competencia (150 ms → < 30 ms es el delta propio; mencionar competidores por nombre está prohibido en empaque).
- Explicación del mecanismo del bus de continua inverter (demasiado técnico para empaque; pertinente para el QR y el argumentario).
- Caveat sobre protección de cargas pequeñas (Vera §4, Caveat 2) — necesario en sustento y en QR; en empaque podría generar confusión en lugar de claridad.
- Umbral de temperatura de disparo del NTC (dato no formalizado aún — Vera Pendiente P-5).
- Respaldo del termomagnético (Vera §4, Caveat 1): pertinente en argumentario de instaladores, sobrecomplica el mensaje de empaque.
- Datos comparativos de tiempo vs. competidores específicos (TQ, WellSpec) — exclusivamente para argumentario de ventas; nunca en empaque.

---

### §4. Anti-mensaje: qué NO debe sugerir el copy del empaque

Los siguientes mensajes son prohibidos o deben evitarse activamente, aunque parezcan "naturales" en el contexto de las innovaciones:

1. **"Protege al motor" / "Protege a la carga"** — Prohibido por Vera §1.4 y delta v4 §4. El NTC protege al protector y a la instalación; la carga pequeña no queda protegida térmicamente. Este es el anti-mensaje más crítico.

2. **"Protección térmica"** (sin "auto") — Evitar. El 40% del mercado lo interpreta como protección del motor (Orlan §6.3). La formulación correcta es "Autoprotección térmica" o "Sensor NTC incorporado*".

3. **"El más rápido de Venezuela"** — No usar esta formulación específica, que es precisamente el claim de WellSpec. Usar "El más rápido ante parpadeos (< 0,03 s)" que añade el dato cuantitativo propio y supera la afirmación de WellSpec en especificidad y sustento.

4. **"Uno de los más rápidos"** — Prohibido por decisión Owner 2026-05-03 (WORKSTREAM_v5 §Regla de gateo). Formulación prohibida explícitamente.

5. **"Protege ante picos de alta energía" / "Protege ante rayos"** — No atribuir esta función a la velocidad de < 30 ms. Esa función pertenece al supresor de 410 J (existente, no nuevo). Confundir parpadeos con transientes de alta energía es una sobrepromesa técnica concreta (Vera §2.1).

6. **"Reemplaza al breaker termomagnético"** — Prohibido por Vera §1.3. El NTC actúa como respaldo del termomagnético, nunca como sustituto.

7. **Afirmaciones sobre la temperatura de disparo del NTC** sin valor formalizado por I&D (Vera Pendiente P-5). El umbral de disparo no está en los datasheets actuales; afirmarlo en empaque o QR antes de que I&D lo documente es un claim sin RTB verificable.

8. **Cualquier referencia comparativa de marca** en empaque — no mencionar TQ, WellSpec, Avtek ni ningún competidor por nombre. El comparativo es para el argumentario de ventas y la comunicación interna, nunca para el empaque.

---

### §5. Brief para Atlas — articulación del vínculo visual < 0,03 s ↔ inverter

El Owner pide explícitamente que el empaque transmita visualmente que el dato cuantitativo de velocidad y el claim de tecnología inverter están conectados causalmente, no como dos badges independientes.

**El argumento que Atlas debe lograr transmitir en menos de 2 segundos de lectura visual:**

La velocidad de < 0,03 s no es un dato abstracto: es la causa directa de que el equipo inverter quede protegido. El lector debe percibir que el número lleva al beneficio, o que el beneficio necesita el número para existir. La relación es causa-efecto lineal: red inestable → parpadeo → el GSM corta en < 0,03 s → la electrónica inverter no ve la inestabilidad → el equipo no sufre ciclos de arranque destructivos.

**Sugerencias de lógica del vínculo para Atlas (argumento, no diseño):**

- **Unidad visual causa-efecto:** si los dos claims aparecen en el empaque como un bloque integrado (no como dos badges separados al mismo nivel jerárquico), el lector los lee como una idea, no como dos afirmaciones distintas. La secuencia "< 0,03 s" + [conector visual] + "Protege tecnología Inverter" logra esto.
- **El número como antecedente:** colocar el dato cuantitativo antes (o arriba) del claim de inverter establece lectura en orden causal: primero el hecho, luego la consecuencia.
- **Color o forma compartidos:** si < 0,03 s y "Protege tecnología Inverter" comparten un elemento visual (color de fondo, borde, ícono conectivo) que no comparten con "Sensor NTC incorporado*", se establece que los primeros dos son un par causalmente vinculado y el tercero es una capa adicional independiente.
- **Un solo ícono que represente ambos:** el ícono de "parpadeo" ya existe en el sistema de íconos de Exceline (brand wiki §Íconos de Fallas). Un parpadeo representado gráficamente junto al dato de < 0,03 s y al símbolo de inverter puede unificar los tres elementos en un solo argumento visual sin necesitar texto conector.

---

### §6. Brief para Aurelio — tensión estratégica que la Junta debe resolver

La decisión entre Alternativa A y Alternativa B (o C si existe) no es solo estética. Hay una tensión estratégica de fondo que Aurelio debe articular en AU-1 para que la Junta tome una decisión informada:

**Tensión 1 — Densidad de claims vs. respiro visual:**
La Alternativa A tiene cuatro elementos en el tiro (lengüeta + 3 frases). Para un blister pequeño, esto puede ser denso. El riesgo es que ninguno de los cuatro retenga atención porque compiten entre sí. La pregunta para la Junta: ¿cuántas ideas puede procesar un comprador en el punto de venta en 3-5 segundos?

**Tensión 2 — Superlativo anclado vs. dato cuantitativo anclado:**
"El más rápido ante parpadeos (< 0,03 s)" combina superlativo + dato. Si Bruna limita el superlativo, el dato sobrevive y sigue siendo un argumento técnico. Si Bruna aprueba el conjunto, el superlativo amplifica el dato. La Junta debe saber que el dato (< 0,03 s) puede pararse solo si el superlativo genera riesgo.

**Tensión 3 — Innovación visible vs. continuidad de marca:**
El técnico que conoce el GSM-RB "hace décadas" necesita que el claim "Nuevo" sea creíble. Las dos innovaciones reales (NTC + < 30 ms) son el sustento. Si la Alternativa B reduce a dos frases, eliminar la que sea más débil en credibilidad de "nuevo" (NTC o velocidad) puede traicionar el propósito del relanzamiento.

**Tensión 4 — Emoción vs. arquitectura técnica:**
Una alternativa con jerarquía emocional (beneficio primero, dato segundo) puede ser más accesible para el consumidor final pero menos convincente para el instalador. La Junta debe definir a cuál audiencia prioriza en el frente del empaque.

---

## Parte II — Arquitectura de Alternativas A, B y C

---

### §7. Alternativa A — análisis de coherencia arquitectónica

**Estructura propuesta (Canudas + Owner, ratificada):**
- Lengüeta: "Nuevo. La Protección más completa"
- Frase 1: "El más rápido ante parpadeos (< 0,03 s)"
- Frase 2: "Protege tecnología Inverter"
- Frase 3: "Sensor NTC incorporado*"

**Qué hace de A una arquitectura coherente:**
- La lengüeta es un sobre-título que los tres sub-claims justifican concretamente. Sin los tres, "más completa" quedaría en el aire; con los tres, cada uno aporta una dimensión diferente de completitud (velocidad, aplicación, tecnología interna).
- El orden de las frases sigue lógica de valor decreciente para la audiencia técnica: el instalador prioriza velocidad (Frase 1), luego verifica aplicación (Frase 2), luego nota la innovación adicional (Frase 3).
- "Sensor NTC incorporado*" al final es correcto: es el claim más enigmático y el que más necesita el retiro para completarse; ponerlo al final guía al lector a buscar el asterisco.

**Qué le falta o qué tiene como punto débil:**
- La conexión causal entre Frase 1 y Frase 2 (velocidad → protección inverter) no es explícita en el texto. Depende del diseño gráfico (Atlas) para crear esa lectura. Si el diseño no lo logra, las tres frases pueden leerse como tres afirmaciones desconectadas.
- "La Protección más completa" es un superlativo cualitativo que requiere el gate de Bruna. Si Bruna lo limita a "Una protección más completa", la lengüeta pierde fuerza pero sigue siendo defendible.
- La densidad de cuatro elementos en un blister pequeño es un riesgo real de dilución de atención. Atlas debe resolverlo con jerarquía visual clara (no es problema del copy, pero el copy debe funcionar incluso si la jerarquía visual no es perfecta).

---

### §8. Ejes posibles para Alternativa B — para que Solenne elija

Alternativa B debe ser genuinamente distinta, no cosmética. Los siguientes ejes son propuestas de diferenciación real:

**Eje B-1 — Mono-claim cuantitativo con dato dominante:**
Reducir el frente a un solo claim principal que ocupe toda la atención visual, con los demás como secundarios visuales o en el retiro.
- Estructura sugerida: Lengüeta: "El más rápido ante parpadeos" / Dato dominante: "< 0,03 s" (en tipografía grande, el número como protagonista visual) / Sub-claims en retiro: "Protege tecnología Inverter" + "Sensor NTC incorporado*"
- Razón de ser: el dato cuantitativo es el argumento más sólido y más difícil de igualar. Una alternativa que lo pone como protagonista único renuncia a la densidad de A pero maximiza el impacto del diferenciador más fuerte. Es la apuesta por la recordación de un solo dato vs. la promesa de "completitud" de A.
- Diferencia real: A promete completitud (cuatro ideas); B-1 promete velocidad suprema (una idea con número).

**Eje B-2 — Jerarquía emocional: beneficio antes que dato:**
Empezar por el beneficio percibido (protección del equipo) y llegar al dato técnico como respaldo, en lugar del orden inverso de A.
- Estructura sugerida: Lengüeta: "Nuevo. Protege lo que más importa" / Frase 1: "Protege tecnología Inverter" / Frase 2: "El más rápido ante parpadeos (< 0,03 s)" / Frase 3: "Sensor NTC incorporado*"
- Razón de ser: el consumidor final residencial (audiencia secundaria, pero relevante en ferretería) toma decisiones de compra emocionalmente más que técnicamente. "Protege lo que más importa" conecta con el miedo a perder el equipo caro; luego el dato técnico respalda esa promesa emocional.
- Diferencia real: A habla al técnico que evalúa primero el dato; B-2 habla al comprador que evalúa primero el beneficio. Son dos jerarquías de audiencia distintas.
- Nota de riesgo: "Protege lo que más importa" es un claim que Bruna debe gatear — podría leerse como protección del equipo (que el NTC no garantiza para cargas pequeñas). Solenne debe redactar este claim con cuidado.

**Eje B-3 — Dos frases + mayor respiro visual (reducción y precisión):**
Eliminar una de las tres frases de A para dar más peso visual a las dos que quedan, priorizando los dos diferenciadores más únicos.
- Estructura sugerida: Lengüeta: "Nuevo. La protección más completa" / Frase única principal: "El más rápido ante parpadeos (< 0,03 s)" / Frase secundaria: "Sensor NTC incorporado*" (inverter va al retiro con el bullet de características)
- Razón de ser: la combinación velocidad + NTC es la más diferenciada de todo el portafolio. "Protege tecnología Inverter" tiene paridad competitiva (Avtek y Breakermatic ya lo dicen); retirarla del tiro y desplazarla al retiro reduce el riesgo de dilución y concentra el frente en los dos diferenciadores sin equivalente en el mercado.
- Diferencia real: A comunica tres innovaciones completas; B-3 jerarquiza las dos más únicas y acepta que "inverter" no necesita estar en el tiro para cumplir su función diferenciadora.

---

### §9. Propuesta Alternativa C — si surge idea fuera de A y B

El Owner abrió la puerta a una Alternativa C si hay una idea genuinamente distinta. Vael propone la siguiente:

**Alternativa C — El dato como argumento único, en lenguaje cotidiano:**

La premisa: en lugar de tres claims técnicos que requieren lectura, una sola afirmación que traduce toda la innovación a consecuencia percibida por el consumidor no técnico, respaldada por el dato cuantitativo como anclaje de credibilidad.

- Lengüeta: "Nuevo. El más rápido de la categoría"
- Frase dominante: "Actúa en < 0,03 s antes de que la fluctuación llegue a tu equipo"
- Sub-texto: "Sensor NTC + Protección Inverter incluidos*"
- Asterisco al retiro: explicación de NTC + acotamiento de parpadeos

**Razón de ser de C:**
- A y B son construcciones de badges técnicos (tres o dos frases autónomas). C es una construcción narrativa: enuncia un hecho y su consecuencia en una sola frase legible por cualquier audiencia.
- "Actúa en < 0,03 s antes de que la fluctuación llegue a tu equipo" es la primera formulación del set que le dice al consumidor final qué significa el número en términos de su vida.
- "NTC + Protección Inverter incluidos*" colapsa los otros dos claims en un sub-texto compacto que no compite con la frase principal.
- Diferencia real con A y B: C abandona la estructura de badges múltiples y apuesta por una narrativa de causa-efecto comprimida en una sola oración.

**Riesgo de C:** La frase dominante es más larga que las frases de A o B; en un blister pequeño puede quedar apretada tipográficamente. Oz/Atlas deben evaluar factibilidad de espacio antes de comprometerse con esta opción. Además, "El más rápido de la categoría" en la lengüeta requiere gate de Bruna igual que "El más rápido ante parpadeos".

**Recomendación de Vael para Aurelio sobre C:** presentarla a la Junta como opción de reserva — si A o B generan objeciones sobre densidad o complejidad técnica, C ofrece una salida de síntesis. No es la apuesta principal, pero puede ser la correcta si la Junta no es un panel de técnicos.

---

## Parte III — VA-5: Guardrails de Claims

---

### §10. Claims candidatos categorizados

---

#### Claim: "El más rápido ante parpadeos (< 0,03 s)"

**Categoría: Defendible con caveat**

**RTB:** Dato de I&D medido por laboratorio; spec de < 30 ms / < 0,03 s acordada por Canudas y Owner (WORKSTREAM_v5 §Decisiones). Ningún competidor venezolano publica dato comparable (Orlan Sección 1). WellSpec, el más agresivo, publica 200-300 ms.

**Por qué no Defendible sin caveat:** El dato "< 30 ms" existe como declaración de I&D pero no está todavía en ningún datasheet publicado (Vera Pendiente P-2). La formalización del protocolo de medición está pendiente (Vera Pendiente P-2). Canudas mismo anotó "verificar con fuentes técnicas" en su mensaje. El superlativo está respaldado por evidencia competitiva sólida pero la nota de Canudas y la ausencia de datasheet actualizado son condiciones previas que Bruna debe verificar antes de aprobar.

**Caveat literal obligatorio (para gate de Bruna):**
> *Tiempo de desconexión ante parpadeos (fluctuaciones rápidas del voltaje de red) inferior a 30 milisegundos, según especificación técnica del laboratorio I&D Genteca. Aplica exclusivamente a parpadeos e inestabilidad de red. El tiempo de desconexión ante sobre voltaje o bajo voltaje es de 0,4 a 3 segundos según la intensidad de la falla. Condición de gate previa a producción: I&D debe haber emitido datasheet actualizado con el valor < 30 ms documentado.*

**Items de gate para Bruna:** (1) Confirmar que el dato < 30 ms está medido bajo protocolo reproducible documentado (Vera Pendiente P-2). (2) Evaluar si la nota de Canudas "verificar con fuentes técnicas" es suficiente como respaldo interno o si se requiere documento formal de laboratorio antes de imprimir el claim en el empaque.

---

#### Claim: "El único en proteger tecnología inverter"

**Categoría: No usar**

**Razón:** Es un superlativo categórico falso. Avtek, Breakermatic y JVTRONIC ya comunican "para tecnología inverter" en sus empaques y fichas (Orlan Sección 4). El claim "único" en este atributo no se sostiene. Si Bruna lo recibe, la respuesta esperada es rechazo.

**Alternativa recomendada:** "Protege tecnología Inverter" (sin "único") vinculado en diseño gráfico al dato de velocidad, que sí es diferenciador único.

---

#### Claim: "Protege tecnología Inverter" (sin superlativo)

**Categoría: Defendible con caveat**

**RTB:** El tiempo de respuesta de < 30 ms garantiza apertura del circuito antes de dos ciclos de red (Vera §2.4), minimizando la exposición de la electrónica de control inverter a condiciones de inestabilidad. El argumento técnico de causa-efecto velocidad→inverter es verificable.

**Por qué no Defendible sin caveat:** El claim per se no es exclusivo de Genteca (Avtek y Breakermatic lo usan). Su fuerza diferenciadora depende de estar en proximidad visual y conceptual al dato de velocidad. Aislado en el empaque, sin el dato, se degrada a paridad competitiva. Además, la protección es específica ante parpadeos, no ante todos los fenómenos que pueden afectar a equipos inverter.

**Caveat literal obligatorio (para gate de Bruna):**
> *La protección ante parpadeos (flickers) e inestabilidad de red que ofrece este protector es especialmente beneficiosa para equipos con tecnología inverter, cuya electrónica de control es sensible a variaciones rápidas del voltaje. Este protector no reemplaza la protección contra transientes de alta energía (descargas atmosféricas, conmutación inductiva) presente en el equipo inverter de fábrica. Ambas protecciones son complementarias.*

**Condición de uso en empaque:** Este claim solo debe aparecer en el tiro si está en proximidad visual (diseño gráfico) con el dato "< 0,03 s". Sin esa proximidad, debería moverse al retiro como bullet de características.

---

#### Claim: "Sensor NTC incorporado*" (con asterisco)

**Categoría: Defendible**

**RTB:** El sensor NTC existe, está ubicado junto al relé de potencia, su mecanismo de protección térmica es técnicamente correcto (Vera §1.1 y §1.2), y Canudas lo confirma (WhatsApp 02-05-2026). Ningún competidor venezolano lo comunica (Orlan Sección 3).

**Condición de uso:** Asterisco obligatorio. La nota de retiro del asterisco debe incluir, mínimo: (a) NTC = sensor de temperatura, (b) protege al protector mismo y al cableado, (c) sin afirmar protección del motor ni de la carga conectada en todos los casos.

**Caveat literal de retiro para Bruna (texto de asterisco):**
> *Sensor NTC: sensor de temperatura incorporado junto al relé de potencia. Detecta calentamiento excesivo y desconecta la carga para proteger al protector mismo y al cableado de la instalación ante corrientes excesivas. Para cargas de baja demanda de corriente, el sensor NTC protege al protector y al cableado, pero no actúa como protección de sobrecarga directa de la carga conectada.*

---

#### Claim: "Autoprotección térmica"

**Categoría: Defendible**

**RTB:** Vera §1.3(a) confirma que la función primaria del NTC es autoproteger al protector mismo. El prefijo "auto" corrige el malentendido del 40% del mercado que interpreta "protección térmica" como protección del motor (Orlan §6.3).

**Nota de uso:** Esta formulación es correcta para badges en el tiro, pero es más difusa que "Sensor NTC incorporado*" — menos técnica para el instalador y menos enigmática para el consumidor curioso. Puede usarse como alternativa o complemento a "Sensor NTC incorporado*" en versiones B o C.

**Sin caveat adicional** al que ya aplica a "Sensor NTC incorporado*" — mismo hecho, formulación diferente.

---

#### Claim: "Nuevo. La Protección más completa" (lengüeta)

**Categoría: Defendible con caveat**

**RTB:** "Nuevo" se sustenta en las dos innovaciones reales (NTC + < 30 ms) — Vera confirma que ninguna de las dos estaba en los datasheets anteriores. "La protección más completa" es un superlativo cualitativo que se sustenta en la acumulación de tres capas de protección comunicadas en el tiro: velocidad ante parpadeos (no igualada en mercado), protección inverter con razón causal, y autoprotección NTC.

**Por qué no Defendible sin caveat:** "La protección más completa" es un superlativo relativo que compara contra alternativas del mercado. Su fuerza depende de que los tres sub-claims que lo sustentan sobrevivan al gate de Bruna. Si alguno de los tres sub-claims es limitado o retirado, la lengüeta puede quedarse sin sustento suficiente.

**Caveat literal y opciones para Bruna:**
> *Opción A (superlativo relativo — más conservadora): "Nueva. Una protección más completa" — elimina el superlativo absoluto, conserva el eje de "más completa que la versión anterior".*
> *Opción B (superlativo delimitado): "Nuevo. La protección más completa para equipos modernos" — delimita el campo de comparación a equipos con tecnología inverter o similares, donde el argumento técnico es más sólido.*
> *Opción C (sin cambio — aprobación del superlativo absoluto): "Nuevo. La Protección más completa" — Bruna aprueba si considera que los tres sub-claims del tiro constituyen sustento suficiente.*

---

#### Claim: "Respaldo del breaker termomagnético"

**Categoría: Defendible con caveat — solo off-empaque**

**RTB:** Vera §1.3, Canudas WhatsApp: el NTC actúa como capa adicional que respalda al interruptor termomagnético de la instalación; no lo reemplaza.

**Por qué no en empaque:** La frase introduce al breaker termomagnético como actor, lo cual complejiza el mensaje para el consumidor final. Para el instalador técnico, en el argumentario de ventas o en el QR, es un argumento valioso y técnicamente preciso. En el empaque, el espacio no lo justifica y el consumidor residencial no lo necesita para tomar la decisión de compra.

**Caveat para off-empaque (sustento de Junta / argumentario):**
> *El Sensor NTC actúa como una capa adicional de protección térmica que respalda al interruptor termomagnético de la instalación. No reemplaza al breaker ni a ninguna protección de sobrecorriente del circuito. La correcta selección y calibración del breaker termomagnético por parte del instalador sigue siendo indispensable.*

---

#### Claims: "Protege al motor" / "Protege a la carga"

**Categoría: No usar**

**Razón:** Prohibidos explícitamente por Vera §1.4 y delta v4 §4. El NTC no protege a la carga directamente en todos los casos: solo cuando la corriente de la carga se aproxima a los nominales del protector (~20 A). Para cargas pequeñas, el NTC protege al protector y a la instalación pero no actúa como protección de sobrecarga de la carga. Afirmar "protege al motor" o "protege a la carga" sin esta distinción es una sobrepromesa técnica verificablemente incorrecta. Prohibición sin excepciones.

---

#### Claim: "Uno de los más rápidos"

**Categoría: No usar**

**Razón:** Prohibido por decisión explícita del Owner 2026-05-03 (WORKSTREAM_v5 §Regla de gateo). Formulación no permitida bajo ninguna circunstancia. La alternativa correcta es "el más rápido" o "el único" — no "uno de los más rápidos".

---

### §11. Temas sensibles

**Comparativos directos con competencia:**
No mencionar marcas competidoras por nombre en empaque ni en materiales de punto de venta. Los comparativos directos (WellSpec 200-300 ms vs. Genteca < 30 ms) son para argumentario de ventas interno y para el Memo AU-1 a la Junta Directiva. El claim superlativo "El más rápido" es la forma correcta de comunicar diferenciación sin comparativo directo de marca.

**Garantías:**
No hay en el copy propuesto ningún claim de garantía sobre resultados de protección al equipo. Si en alguna versión de Solenne aparece una afirmación del tipo "garantiza la protección del equipo" o "evita daños", Bruna debe gatear esa formulación — es una garantía de resultado que puede generar obligaciones legales.

**Claims regulatorios (IEC/COVENIN):**
El copy no incluye claims de certificación específica. Si en cualquier versión se cita "certificado IEC" o "aprobado COVENIN", Bruna debe verificar que los números de norma y estado de certificación son vigentes y aplicables a los modelos GSM-MB/RB/RF/RE específicamente (Orlan §8 Expuesto: el dato de certificaciones no está completamente verificado).

**Afirmaciones absolutas:**
- "Siempre protege" — evitar. La protección es condicional a que el evento sea del tipo que el producto cubre (parpadeos, no todos los fenómenos eléctricos).
- "100% de protección" — evitar. Sin RTB que lo respalde.
- "Nunca falla" — evitar. Sin RTB ni evidencia certificada de MTBF.

---

### §12. Gate de Bruna

**Estado:** Pendiente — este VA-5 es la propuesta de Vael para el gate de Bruna (BR-1 + BR-2). Ningún claim ⚠ o ❌ pasa a producción sin gate explícito de Bruna.

**Items que requieren gate explícito de Bruna antes de pasar a Solenne / Oz:**

| # | Claim | Categoría Vael | Condición previa al gate |
|---|---|---|---|
| 1 | "El más rápido ante parpadeos (< 0,03 s)" | Defendible con caveat | I&D debe emitir datasheet con < 30 ms documentado (Vera P-2) |
| 2 | "Protege tecnología Inverter" | Defendible con caveat | Confirmar que aparece en diseño en proximidad al dato de velocidad |
| 3 | "Sensor NTC incorporado*" | Defendible | Confirmar texto literal del asterisco de retiro |
| 4 | "Nuevo. La Protección más completa" | Defendible con caveat | Bruna elige entre Opción A / B / C del caveat |
| 5 | "Autoprotección térmica" | Defendible | Sin gate adicional si se usa como alternativa a NTC (mismo hecho) |

**Item bloqueante:** El gate del Claim 1 depende de la formalización del dato de I&D. Si I&D no emite el datasheet actualizado antes de que el empaque entre en artes finales, el superlativo no puede usarse aunque Bruna lo apruebe conceptualmente.

---

## Parte IV — Cover Note de Trazabilidad

---

### §13. Qué se usó de cada insumo aguas arriba

**De Vera_brief_tecnico_v1:**
- §1.1 - §1.4: mecanismo del NTC, qué protege y qué no protege. Base de los Pilares 3 y 5, del anti-mensaje §4, y de la clasificación de los claims de NTC en VA-5.
- §2.2 - §2.4: mejora 150 ms → < 30 ms, distinción parpadeos vs. sobre/subtensión, por qué la velocidad importa para inverter. Base de los Pilares 1 y 2.
- §4: caveats literales listos para retiro — usados textualmente para los caveats de empaque y para la formulación de los ⚠ claims en VA-5.
- §5: pendientes P-1 a P-6 — incorporados como condiciones previas en gate de Bruna y en sección de Supuestos.

**De Orlan_competencia_v1:**
- Sección 1 + tabla de competidores: ningún competidor venezolano publica < 30 ms. WellSpec: 200-300 ms. Powest: 1.000 ms. Breakermatic: 1.000-1.500 ms. Base del RTB del Pilar 1 y del claim superlativo.
- Sección 3: cero competidores comunican NTC. Base del RTB del Pilar 3 (territorio en blanco).
- Sección 4: tres competidores dicen "para inverter" sin dato cuantitativo. Base del matiz del Pilar 2 (paridad en aplicación, diferenciación en razón causal).
- Sección 7 (OL-5): categorización de claims candidatos — alineada con VA-5 §10.
- §6.3: insight de consumidor ~40% interpreta "protección térmica" como protección del motor. Base del anti-mensaje §4 punto 2 y de la nota de audiencia en §2.

**De WORKSTREAM_v5_innovaciones:**
- §Regla de gateo de claims superlativos: "uno de los más rápidos" prohibido; "el más rápido" / "el único" permitidos con condición de ausencia de contraejemplo verificado. Incorporado en VA-5 §10.
- §Vinculación gráfica < 0,03 s ↔ inverter: base del brief para Atlas §5.
- §Libertad creativa: sustento para proponer Alternativa C en §9.
- §Decisiones cerradas — estatus de productos nuevos no publicados: incorporado como mitigación del riesgo de discrepancia empaque vs. datasheets actuales.
- §QR ampliado a 6 temas: notado como contexto; no es scope de este VA-1/VA-5 sino del memo lateral a Aurelio.

**De delta_v4_NTC-inverter:**
- Textos prohibidos §4: incorporados en anti-mensaje §4 y en VA-5 §10.
- Estructura de secciones propuestas: punto de partida de la jerarquía de mensajes §3.

**De WhatsApp Canudas 02-05-2026:**
- Explicación técnica del NTC y confirmación de la Alternativa A como copy ancla.
- RTB literal ("protege al protector y al cableado de una condición de trabajo para la cual no fueron diseñados") — incorporado en RTBs del Pilar 3.
- Nota "verificar con fuentes técnicas" — incorporada como condición previa del gate del Claim 1.

**De brand wiki 01-identidad-de-marca.md:**
- Eslogan Exceline Residencial: "La ÚNICA protección confiable en Venezuela" — RTB de Pilar 4 (coherencia de eje "completitud" con la identidad previa).
- Atributos compartidos Exceline: "Confiable · Robusto · Duradero" — guía de tono para todas las audiencias.
- Íconos de fallas del sistema eléctrico venezolano: "Parpadeos" ya existe como concepto visual. Base de la sugerencia en brief para Atlas §5.
- Tipografía y paleta de color: nota de restricción implícita para Oz / Atlas (Montserrat para empaques según brand wiki).

---

### §14. Supuestos y límites

**Insumos aguas arriba que sostienen este framework:**
- Vera: Vera_brief_tecnico_v1.md — 2026-05-03
- Orlan: Orlan_competencia_v1.md (OL-1/2/3/5 combinados) — 2026-05-03
- Brand wiki: 01-identidad-de-marca.md — versión 2026-04-30
- WORKSTREAM_v5_innovaciones.md — 2026-05-03 (última actualización)
- WhatsApp Canudas: 02-05-2026 (confirmación directa del Owner + JMC)

**Validez temporal:** Q2 2026. Este framework es válido mientras:
- El dato < 30 ms no sea modificado por I&D.
- El landscape competitivo de Orlan no cambie (ningún competidor publique dato < 30 ms).
- La política de claims del Owner (WORKSTREAM_v5 §Regla de gateo) se mantenga vigente.

**Cambios aguas arriba que invalidarían este framework:**
- Si I&D modifica el dato de < 30 ms a un valor distinto (sube o baja el umbral): requiere refresh de Pilar 1, VA-5 §10 Claim 1, y brief para Atlas.
- Si un competidor venezolano publica un dato de < 30 ms o menor en fuentes verificables: invalida el superlativo "El más rápido" — requiere refresh urgente de VA-5 y notificación a Bruna.
- Si Bruna (BR-2) emite decisión que cambia la categoría de algún claim ⚠ a ❌ o viceversa: el framework debe actualizarse y Solenne debe recibir la notificación de refresh.
- Si I&D formaliza el umbral de temperatura de disparo del NTC (Vera Pendiente P-5): abre posibilidad de un nuevo RTB para el Pilar 3 y nueva formulación en el QR.
- Si Orlan actualiza el análisis competitivo (Paxs desbloquea datasheets TQ, JVTRONIC): puede cambiar la solidez del superlativo si se encuentra dato < 30 ms no publicado previamente.

**Decisiones del Owner pendientes:**
- Elección final de Alternativa A, B o C — post Junta Directiva.
- Confirmación de si el QR en empaque va como elemento constante en A y B o como variable independiente (WORKSTREAM_v5 §QR — evaluación a producir; este VA-1/VA-5 no incluye esa decisión).

**Claims con gate pendiente de Bruna:**
Ver VA-5 §12: Claims 1, 2, 3 y 4 tienen gate pendiente. El Claim 1 ("El más rápido ante parpadeos < 0,03 s") tiene además condición previa bloqueante de I&D (datasheet actualizado con < 30 ms documentado).

**Pendientes que este framework no puede resolver y que escala a Bruna / I&D / Raul:**
- Vera Pendiente P-2: datasheet actualizado con < 30 ms. Bloqueante para producción del empaque.
- Vera Pendiente P-1: datasheets de GSM-MB y GSM-RF no verificados. Si sus nominales difieren de los RE, los caveats del retiro deben ajustarse por modelo.
- Vera Pendiente P-4: trazabilidad documental del claim "Protege tecnología Inverter" en etiqueta 2018 — Bruna la necesitará para el gate.
- Orlan pendiente: .docx de market research no pudo procesarse (Orlan §6.1). Si contienen hallazgos sobre comprensión de claims distintos a lo capturado en las transcripciones, el framework podría requerir ajuste de mensajes por audiencia.
- Paxs background: investigación del OEM de TQ (WORKSTREAM_v5 §TQ). No bloquea este framework; si TQ resulta publicar un dato < 30 ms en fuentes no rastreadas aún, invalida el Pilar 1 y requiere refresh urgente.

**Notificaciones de refresh pendientes post-gate de Bruna:**
Una vez que Bruna emita BR-2 con la decisión sobre los claims de este VA-5, Vael notificará en cascada:
- A Solenne: claims aprobados vs. limitados para SO-1 (copy A y B).
- A Aurelio: pilares y tensiones estratégicas confirmados para AU-1 (memo a Junta).
- A Oz: formulaciones exactas de claims aprobados para implementación en redline.

---

*domain-specialist. Genteca.*
*Vael — Brand & Messaging Strategist*
*Este documento es arquitectura de mensaje, no copy publicable. Los claims están categorizados como propuesta; la aprobación es de Bruna (BR-1/BR-2). El copy final es de Solenne (SO-1).*
