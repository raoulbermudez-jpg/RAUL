# BR-2 — Gate de Aprobación: Deck V3 Gama Notoriedad 2026

**Proyecto:** consultoria-externa / gama-notoriedad-2026
**Deliverable gateado:** Deck Principal V3 (VI-1a, ~42 slides) + Resumen Ejecutivo V3 (VI-1b, 7 slides)
**Fecha de decisión:** 2026-05-17
**Bruna (decisora):** gate aplicado con criterio de research integrity (no hay RISK-POLICY formal de consultoria-externa aún — se aplica criterio prudente según instrucción del Owner)
**Insumos leídos:**
- CU-6 v2 (Cuanti caveats, versión final con RF/SHAP resueltos)
- IN-6 v1 (Sinta caveats cualitativos)
- VI-1a Outline Deck Principal V3 (46 slides enumerados, leídos completos)
- VI-1b Outline Resumen Ejecutivo V3 (7 slides, leídos completos)
**Precedente:** Este es el primer archivo de governance del dominio consultoria-externa. Crea el directorio `_governance/` dentro del proyecto.
**Referencia RISK-POLICY:** No hay RISK-POLICY formal de consultoria-externa. Criterios aplicados: (1) bases bajas n<35 flagged REFERENCIAL, (2) claims causales con caveat si evidencia es asociacional, (3) tono crítico al cliente suavizado para que Cora pueda presentar sin conflicto, (4) hipótesis no presentadas como hechos.

---

## DECISION GLOBAL

**GO CON AJUSTES MENORES**

El V3 puede salir a Drive de Cora una vez aplicados los ajustes obligatorios listados más adelante. Los ajustes son editoriales y de caveat — ninguno requiere rehacer análisis ni retirar un bloque del deck. El edificio analítico es sólido. La decisión es GO con 5 ajustes antes del drop.

**Distribución de claims:**

| Status | Claims cuanti (CU-6 v2) | Claims cuali/estratégicos (IN-6 v1) | Total |
|---|---|---|---|
| GO pleno | 7 | 2 (C-006, C-008) | 9 |
| GO con caveat (ya incorporado en outline) | 3 | 1 (C-002) | 4 |
| AJUSTAR (requiere acción antes del drop) | 3 | 3 (C-001, C-003, C-004) | 6 |
| NO-GO (excluir del deck) | 0 | 1 (C-005) | 1 |
| Pendiente decisión Owner | 0 | 1 (C-007) | 1 |

---

## TABLA CLAIM-BY-CLAIM

### Claims cuantitativos (referencia CU-6 v2)

| ID | Claim | Decisión Bruna | Rationale | Acción exacta |
|---|---|---|---|---|
| D-001 | Atención = driver principal OR=5.73 (IC95: 1.6-20.4, p=0.007) | **GO pleno** | Convergencia logit + SHAP + Gini + razón espontánea. El claim más robusto del estudio. IC95 ya incluido en outline. | Ninguna. Verificar que el .pptx final incluya IC95 en las slides 6, 10 y A2. |
| D-002 | Limpieza/orden = driver secundario con soporte convergente (OR=3.99, p=0.061; SHAP #2; Gini #2) | **GO con caveat** | Cuanti justifica la elevación por multicolinealidad y convergencia triple. El caveat de p-logit borderline está correctamente incluido en el outline (slides 11, A2). | Verificar que la nota de pie del slide 11 en el .pptx diga literalmente: "La limpieza/orden alcanza significancia en RF/SHAP (n.° 2 en ambos métodos) aunque el logit no alcanza p<0.05 (p=0.061), probablemente por multicolinealidad con atención." |
| D-003 | Promociones = driver terciario (OR=3.64, IC95: 1.1-11.8, p=0.031; SHAP #3) | **GO pleno** | Confirmado en logit y SHAP. IC95 en outline. | Ninguna. |
| D-004 | El precio no es driver de preferencia (OR=1.03, p=0.966; SHAP #10) | **GO pleno** | Convergencia triple en irrelevancia. Claim estratégicamente importante para el posicionamiento. | Ninguna. |
| S-001 | 3 segmentos k-means publicables (silhouette 0.195, BIC mínimo) con caveat de solapamiento en márgenes | **GO con caveat** | Cuanti valida k=3 con doble criterio. Silhouette moderado ya documentado. Caveat obligatorio incorporado en outline (slides 23, 27, A3). | Verificar que el caveat del seg_3 (n=32, REFERENCIAL) aparezca explícitamente en el .pptx — no solo en el outline. |
| L-001 | Bug JSON faseA C+/C (n=0) — no afecta deck V3 | **GO** | Cuanti confirma que el deck V2 no está afectado. Tarea pendiente pre-ola 2027. | Ninguna para el drop. |
| L-002 | IC95 amplios por n_pref=32 — reportar siempre con OR | **AJUSTAR** | Los IC95 son obligatorios en cualquier OR del deck. El outline los menciona en varios slides. Riesgo: que el .pptx final los omita por diseño gráfico (slide congestionada). | **Ajuste obligatorio #1:** verificar slide por slide en el .pptx que ningún OR aparezca solo como número puntual. Si algún OR no tiene IC95, agregar entre paréntesis aunque sea en tamaño de letra reducido al pie. |
| L-004 | Slides publicidad P35-P42 — base baja (n=17, n=43, n=50) | **AJUSTAR** | Base crítica. CU-6 v2 es explícito: "BASE BAJA en título de slide, no solo al pie." El outline cumple (slides 32, 33 tienen "BASE REFERENCIAL" en el título). | **Ajuste obligatorio #2:** confirmar que en el .pptx los títulos de los slides 32 y 33 contienen la etiqueta "BASE REFERENCIAL" visible antes de leer el takeaway. No solo en footnote. |
| L-005 | El Recreo (P43-P45) — n=21 | **GO con caveat** | Footnote "solo indicativo" en outline. | Verificar que el footnote esté en el .pptx. |
| L-006 | Municipios pequeños (Altos Mirandinos n=20, El Hatillo n=31) | **GO con caveat** | Footnote de base referencial en outline. | Verificar que el footnote esté en el .pptx. |

### Claims cualitativos y estratégicos (referencia IN-6 v1)

| ID | Claim | Decisión Bruna | Rationale | Acción exacta |
|---|---|---|---|---|
| C-001 | "La campaña de Gama comunica precio cuando debería comunicar experiencia" | **AJUSTAR — tono** | El análisis es correcto y la evidencia es sólida (0/17 recall PTL espontáneo; 65% lee precio; OR precio=1.03). El problema es el tono de "debería" — leído directamente por Cora ante Gama, puede generar defensividad y bloquear la recepción del mensaje. El deck en su outline ya aplica el AJUSTAR de Sinta en varios slides (6, 14, 32, 33, 34), pero de forma inconsistente: algunos slides mantienen framing crítico y otros el framing de oportunidad. | **Ajuste obligatorio #3:** En los slides 14 y 34 del .pptx, verificar que el texto nunca diga "la campaña actual no está funcionando" ni "la campaña es un error". La formulación exacta aprobada es: "El estudio indica que comunicar la experiencia de atención (el driver más fuerte) puede tener mayor impacto que comunicar precio (el atributo menos predictivo de la preferencia). Una revisión de la plataforma de comunicación está justificada por los datos." Cualquier variante más crítica debe ajustarse a este registro. |
| C-002 | Seg_2 (Pragmáticos Convertibles, n=133) como oportunidad inmediata de conversión | **GO con caveat** | La descripción del seg_2 es accionable y honesta respecto a sus limitaciones. El outline incorpora correctamente el caveat de Sinta: "el análisis sugiere que el seg_2 tiene menor barrera de conversión" (no "prueba"). La diferencia de 0.22 puntos en precio es descriptiva de cluster, y así está formulada. | Ninguna acción adicional. El caveat está bien integrado en slides 25 y 39. |
| C-003 | "La barrera de precio es el obstáculo que impide que el 92% llegue a experimentar la propuesta de valor de Gama" | **AJUSTAR — nivel de certeza** | Es la hipótesis más parsimoniosa, pero el estudio no pregunta directamente "¿por qué no elige Gama?" a los no-preferentes. Pueden existir barreras alternativas (hábito con otra marca, ausencia de sucursal accesible, experiencia negativa previa). El slide 8 del outline ya lo formula como "hipótesis de mecanismo" — bien. El riesgo es que en la presentación oral Cora lo eleve a certeza. | **Ajuste obligatorio #4:** En el slide 8 del .pptx, agregar una línea visible en el cuerpo del slide (no solo en footnote): "Nota: el mecanismo de no-conversión es la hipótesis más parsimoniosa dados los datos disponibles — la validación directa requiere investigación con no-consumidores (Van Westendorp, FGIs)." Esto le da a Cora el lenguaje exacto para bajar las expectativas si alguien de Gama la presiona. |
| C-004 | "La atención opera como símbolo de reconocimiento personal, no solo como atributo funcional" | **AJUSTAR — formulación** | Sinta es explícita: no hay verbatims literales que soporten esta interpretación en esta sesión. Es una construcción inferida de patrones de frecuencia. El claim tiene valor estratégico alto, pero presentarlo como hallazgo verificado a una cliente externa es un riesgo de credibilidad si Gama pregunta "¿en qué cita exacta se basa eso?". El outline ya aplica el AJUSTAR de Sinta en slides 12 y 30. | **Ajuste obligatorio #5:** En el slide 12 del .pptx, el texto debe contener la frase "el estudio sugiere que" o "el análisis temático es consistente con la hipótesis de que" antes de cualquier afirmación sobre reconocimiento personal. La formulación exacta aprobada: "El análisis temático sugiere que la atención puede estar operando como señal de reconocimiento personal — hipótesis apoyada en el patrón de frecuencias. La confirmación requiere acceso a verbatims literales." |
| C-005 | "Sin ti no hay nosotros" como señal de espacio semántico disponible | **NO-GO** | n=2 de n=17. Dos observaciones no pueden soportar ningún claim estratégico. El riesgo de credibilidad es máximo: si alguien de Gama pregunta por la base estadística de esa afirmación, el número "2 personas" destruye la credibilidad de toda la presentación. La decisión es NO-GO como afirmación estratégica directa. El outline ya lo excluye correctamente del deck (nota al pie de VI-1a: "Claims NO-GO excluidos: C-005"). | Confirmar que C-005 no aparece en ningún slide del .pptx final, ni siquiera como anécdota de apoyo. Si se quiere mencionar el territorio semántico "compañía / estar de tu lado", hacerlo desde la interpretación de DTLS (30% lectura relacional, n=50, con caveat de base baja) — eso sí tiene respaldo suficiente. |
| C-006 | Limpieza como driver secundario — convergencia metodológica | **GO** | Delegado a decisión CU-6 v2 D-002. Sinta confirma coherencia con integración cuali. | Ninguna. |
| C-007 | Ausencia de verbatims literales en sesión Sinta | **Pendiente decisión Owner** | No bloquea el gate de los claims de alta certeza. Sí afecta el nivel de confianza de los temas latentes (especialmente C-004). Bruna aplica el ajuste de C-004 como solución operativa interim. La decisión estructural (segunda sesión de Sinta con acceso a BBDD raw) es del Owner. | Escalar al Owner — ver sección de Escalaciones. |
| C-008 | Segmentación k-means como contenido nuevo para Cora (no en V2) | **GO con caveat** | Los datos son publicables con caveat de silhouette. La decisión de packaging (cómo Cora presenta los segmentos a Gama en contexto del V2 ya entregado) es del Owner, no de Bruna. | Escalar al Owner — ver sección de Escalaciones. |

---

## CAMBIOS OBLIGATORIOS AL DECK ANTES DEL DROP (lista numerada)

Todos los ajustes son sobre el .pptx final — el outline VI-1a ya los incorpora conceptualmente. El riesgo es que la producción gráfica los diluya.

**Ajuste #1 — IC95 obligatorio en todos los OR (afecta slides 6, 10, 36 y A2 principalmente)**
Ningún odds ratio puede aparecer como número puntual solo. Verificar que OR=5.73 esté siempre acompañado de "(IC95: 1.6-20.4)" o equivalente. Si el diseño del slide no tiene espacio, usar nota al pie con asterisco.

**Ajuste #2 — Etiqueta "BASE REFERENCIAL" en título de slides 32 y 33**
La etiqueta debe estar en el título visible del slide, no solo en el footnote. Formulación aceptada: "BASE REFERENCIAL (n=17 / n=43)" en el título o subtítulo de la slide, antes del takeaway.

**Ajuste #3 — Tono de la brecha comunicacional en slides 14 y 34**
Eliminar cualquier framing que suene a "la campaña fracasó" o "la campaña es un error". La formulación aprobada (puede parafrasearse levemente manteniendo el registro): "El estudio indica que comunicar la experiencia de atención puede tener mayor impacto que comunicar precio. Una revisión de la plataforma de comunicación está justificada por los datos."

**Ajuste #4 — Nota de hipótesis visible en el cuerpo del slide 8**
Agregar en el cuerpo del slide (no en footnote): "Nota: el mecanismo de no-conversión es la hipótesis más parsimoniosa dados los datos disponibles. La validación directa requiere investigación con no-consumidores."

**Ajuste #5 — Formulación de reconocimiento personal en slide 12**
Toda referencia al mecanismo de "reconocimiento personal" debe ir precedida de "el estudio sugiere que" o "el análisis temático es consistente con la hipótesis de que". Texto aprobado para pie de slide o cuerpo: "Hipótesis apoyada en el patrón de frecuencias — la confirmación requiere acceso a verbatims literales."

**Verificación adicional (no bloquea, pero hacer antes del drop):**
- Confirmar que C-005 ("Sin ti no hay nosotros") no aparece en ningún slide ni en la sección de apéndice.
- Confirmar caveat de silhouette moderado (~0.20) en al menos el slide 23 del .pptx.
- Confirmar footnote "solo indicativo" en slides de El Recreo y municipios pequeños.

---

## NOTAS DE PRECEDENTE — Q4 2026 / OLA 2027

**Precedente P-CE-001: Primer gate consultoria-externa — criterio aplicable cross-proyecto**

Fecha: 2026-05-17. Proyecto: Gama Notoriedad 2026 V3.

*Criterios de research integrity validados para consultoria-externa (aplicar a proyectos futuros de terceros):*

1. **Bases bajas (n<35):** etiqueta "REFERENCIAL" obligatoria en el título del slide, no solo en footnote. El footnote no es suficiente — el receptor externo (cliente del cliente) lee el titular y puede no leer la nota. Validado en gate Gama: slides de publicidad n=17 y n=43.

2. **Claims causales vs asociacionales:** toda implicación de mecanismo (X causa Y) requiere calificación explícita de hipótesis si la evidencia es observacional/asociacional. La convergencia múltiple de métodos (logit + SHAP + Gini) eleva el nivel de confianza, pero no convierte asociación en causalidad. La calificación debe estar en el cuerpo del slide, no solo en el footnote. Validado en: C-003 (barrera de precio), C-004 (reconocimiento personal).

3. **Tono crítico al cliente:** en deliverables de consultoría hacia terceros, la distancia entre "hallazgo estratégico" y "crítica a la inversión del cliente" puede destruir la receptividad. El framing de "oportunidad apoyada en datos" es siempre preferible al framing de "error actual". La evidencia no cambia — el tono sí. Validado en: C-001 (campaña PTL). Regla operativa: nunca usar "fracasó", "no funciona", "es un error". Usar: "el estudio indica que", "los datos justifican revisar", "la oportunidad está en".

4. **Claims sin ancla en datos primarios:** interpretaciones derivadas de patrones de frecuencia (sin verbatims literales, sin acceso a BBDD raw) se presentan siempre como hipótesis marcadas. El valor estratégico puede ser alto — la formulación debe ser honesta sobre la certeza. Validado en: C-004, C-007 (ausencia de verbatims en sesión Sinta).

5. **NO-GO por base mínima:** n=2 es un umbral donde ningún claim estratégico es publicable. Validado en: C-005 (n=2 de n=17 para "Sin ti no hay nosotros"). Regla operativa: base mínima para mención en deck como "anécdota ilustrativa" = n≥5. Base mínima para claim estratégico = n≥30 (referencial) o n≥80 (proyectable).

6. **Retrofit V3 sobre V2 ya entregado:** cuando un análisis posterior (V3) eleva, ajusta o agrega hallazgos sobre un V2 ya entregado a cliente, el V3 debe: (a) confirmar explícitamente qué del V2 sigue vigente, (b) explicar qué se eleva y por qué, (c) nunca invalidar el V2 implícitamente. El deck V3 lo hace correctamente (slide 2). Patrón aprobado para futuros retakes.

7. **Gate Bruna en consultoria-externa = mismo rigor que interno.** La ausencia de RISK-POLICY formal no reduce el estándar. El criterio de research integrity aplica con la misma dureza. Diferencia operativa: el énfasis en tono (punto 3) es mayor que en proyectos internos porque el receptor final (cliente del cliente) no tiene el contexto del sistema de gobernanza interno.

---

## ESCALACIONES AL OWNER

**Escalación E-1 (C-007) — Decidir si se requiere segunda sesión de Sinta con verbatims literales**

Sinta no tuvo acceso a BBDD raw en esta sesión. El análisis temático (IN-1, IN-2) y los temas latentes (slides 28, 30) están basados en frecuencias de categorías — no en citas literales con ID de participante. Bruna aplica el ajuste de formulación (C-004: "hipótesis interpretativa") como solución operativa para el drop de V3. Pero si el siguiente paso es presentación en sala con Gama (no solo entrega de deck), la ausencia de verbatims literales puede ser un punto de ataque de credibilidad si alguien del equipo de Gama pregunta "¿en qué cita exacta se basa la afirmación de reconocimiento personal?"

Decisión requerida del Owner: ¿se autoriza una sesión adicional de Sinta con acceso controlado a BBDD raw (respetando NDA) antes de la presentación presencial a Gama? Esto no bloquea el drop del deck a Cora — bloquearía solo la presentación oral si se quiere sostener C-004 con mayor solidez.

**Escalación E-2 (C-008) — Packaging de segmentos k-means hacia Cora/Gama**

Los 3 segmentos k-means son un hallazgo nuevo en V3 que no existía en el V2 entregado a Cora el 2026-05-16. Gama recibió el V2 sin segmentación. Cuando reciba el V3, verá por primera vez los 3 perfiles. Esto puede generar la pregunta: "¿por qué no estaba en el análisis original?" La respuesta técnica es correcta (el k-means formal se ejecutó en V3, el V2 tenía solo análisis exploratorio). Pero la gestión de esa pregunta con Cora es una decisión del Owner — no de Bruna.

Decisión requerida del Owner: ¿cómo instrucciona a Cora para presentar los segmentos k-means? Opciones posibles: (a) presentarlos como "capa analítica adicional del V3 — la segmentación fue posible con la metodología ampliada", (b) presentarlos solo si Gama pregunta, (c) presentación diferenciada del V3 como deliverable separado con su propia reunión de presentación. Bruna no decide esto — es decisión estratégica de la relación con el cliente.

**Escalación E-3 — Nota de consistencia V2/V3 (no es invalidación — pero el Owner debe saberlo)**

El V3 eleva limpieza/orden de "tendencia" (el término usado en el V2) a "driver secundario confirmado". Esto no invalida el V2 — el cambio es de nomenclatura (se pasa de "tendencia estadística" a "driver secundario con soporte convergente"). Sin embargo, si alguien del equipo de Gama compara el V2 y el V3 en paralelo puede notar el cambio de lenguaje y preguntar. El deck V3 lo explica correctamente en el slide 2 ("el V3 eleva: limpieza sube de 'tendencia' a 'driver secundario'"). Esta escalación es informativa, no bloqueante — el Owner debe estar informado de que ese delta existe y que Cora puede necesitar el lenguaje para explicarlo.

---

*BR-2 producido por Bruna — 2026-05-17 — v1*
*Dominio: consultoria-externa / proyecto: gama-notoriedad-2026*
*Primer archivo de governance de consultoria-externa. Directorio `_governance/` creado en este acto.*
*Decisión global: GO CON AJUSTES MENORES — 5 ajustes obligatorios antes del drop a Drive de Cora.*
*Claims NO-GO: C-005 (n=2). Claims AJUSTAR: C-001, C-003, C-004, L-002, L-004 (formulación/caveat).*
*Escalaciones al Owner: E-1 (segunda sesión Sinta), E-2 (packaging segmentos k-means), E-3 (delta V2/V3 en limpieza).*
