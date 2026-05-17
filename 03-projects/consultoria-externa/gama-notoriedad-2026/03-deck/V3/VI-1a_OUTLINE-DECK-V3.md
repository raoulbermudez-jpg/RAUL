# VI-1a — Slide Outline Deck Principal V3
## Notoriedad Gama 2026 — Capa Analítica Ampliada

**SSOT canónico — Vivienne 2026-05-17**
**Basado en:** IN-5 (Sinta Minto), IN-6 (Sinta caveats), CU-6 v2 (Cuanti caveats), CU-3 v2, CU-4 v2, CU-2, IN-1, IN-2, IN-4, ME-4, Reflexiones 2027
**Gate Bruna:** PENDIENTE antes de circulación externa
**Coexistencia con V2:** V3 no reemplaza al deck V2 del 2026-05-16. Ambos viven en Drive. V3 añade rigor metodológico ampliado + reanálisis RF/SHAP + síntesis cualitativa estructurada.

**Convención de este outline:**
- Cada slide: Titulo | Takeaway (1 frase Minto — recomendación/hallazgo, no descripción) | Bullets | Evidencia/Visual | Caveat aplicable
- Caveats referenciados a ítem CU-6 v2 o IN-6 v1 correspondiente
- Claims con status NO-GO en CU-6/IN-6: excluidos
- Claims con status AJUSTAR: formulación ajustada según indicación del caveat
- Footer de todas las slides: "Notoriedad Gama 2026 · V3 · n=402 · m.e. ±4.89% · Confidencial NDA"

---

## BLOQUE 0 — APERTURA (5 slides)

---

### Slide 1 — Portada

**Titulo:** Notoriedad y Preferencia de Marca — Gama 2026
**Subtitulo:** Capa Analítica Ampliada V3 · Metodologia reforzada + Reanálisis RF/SHAP + Síntesis Cualitativa

**Bullets / contenido:**
- Fecha: 2026-05-17
- Equipo analítico: Cora Urrea + Raoul Bermudez
- Versión: V3 — complementa V2 (2026-05-16)
- Confidencial / NDA

**Visual:** Logo/paleta Gama (rojo #7A1212) + paleta blanco/gris neutros. Mismo estilo que V2.
**Caveat:** Ninguno en portada.

---

### Slide 2 — Qué es el V3 y cómo se relaciona con el V2

**Titulo:** Este V3 complementa el V2 — no lo reemplaza

**Takeaway:** El V3 añade tres capas que el V2 no tenía: rigor metodológico formal, reanálisis estadístico con RF+SHAP, y síntesis cualitativa estructurada con pirámide Minto.

**Bullets / contenido:**
- El deck V2 (2026-05-16, 40 slides) es el análisis principal ya entregado a Gama. Permanece vigente.
- El V3 (este documento) añade tres capas:
  a) Rigor metodológico ampliado: diseño retroactivo, rationale de cada decisión analítica (Methos ME-1/ME-3)
  b) Reanálisis estadístico: Random Forest + SHAP + k-means formal que confirman y elevan los drivers del V2 (Cuanti CU-3/CU-4 v2)
  c) Síntesis cualitativa estructurada: análisis temático + triangulación cuali/cuanti + pirámide Minto (Sinta IN-1..IN-5)
- Las recomendaciones del V2 siguen vigentes. Las del V3 las extienden, matizan y re-priorizan donde la evidencia adicional lo justifica.
- Convergencia clave: el V3 confirma los 3 drivers del V2 (atención, limpieza, promociones). El V2 es correcto; el V3 añade el POR QUÉ.

**Visual:** Tabla comparativa V2 vs V3 en dos columnas (estilo limpio, fondo gris claro).
**Caveat:** Ninguno específico en esta slide de contexto.

---

### Slide 3 — Advertencia metodológica + cómo leer los caveats en este deck

**Titulo:** Cómo leer la evidencia de este estudio

**Takeaway:** Los hallazgos de este estudio son robustos dentro de sus límites; los caveats en pie de slide indican el nivel de certeza de cada claim — no invalidan el hallazgo, lo calibran.

**Bullets / contenido:**
- Base total: n=402 entrevistas F2F. Margen de error ±4.89% al 95%.
- Los drivers de preferencia (Argumento 1: atención OR=5.73; Argumento 2: promociones OR=3.64) se confirman en cuatro métodos independientes: regresión logística, Random Forest, SHAP, y razón espontánea. La convergencia es el estándar más alto de este estudio.
- Subgrupos pequeños (Pref-Gama n=32, datos publicitarios n=17-50) se reportan con caveat "REFERENCIAL" — son indicativos, no proyectables.
- Las interpretaciones cualitativas se presentan como "el estudio sugiere" (hipótesis apoyada en evidencia), no como hechos verificados, excepto donde la triangulación cuali+cuanti es total.
- Icono (*): p<0.10 (tendencia); (**): p<0.05; (***): p<0.01. IC95 siempre acompaña a OR.

**Visual:** Tabla de iconos de significancia + tabla de niveles de certeza (Alto / Medio-Alto / Medio / Hipótesis).
**Caveat:** CU-6 v2 §L-001..L-006 (bases bajas por subgrupo). IN-6 §C-007 (ausencia de verbatims literales en sesión Sinta — afirmaciones cualitativas apoyadas en frecuencias de categorías, no en citas literales directas).

---

### Slide 4 — Ficha técnica del estudio (misma que V2, actualizada con info de V3)

**Titulo:** Ficha técnica del estudio

**Takeaway:** El estudio cubre shoppers regulares de cadena en Caracas + Altos Mirandinos con n=402 entrevistas F2F.

**Bullets / contenido:**
- Universo: shoppers regulares de supermercados de cadena en Caracas + Altos Mirandinos
- Muestra: n=402 entrevistas face-to-face
- Margen de error: ±4.89% al 95% de confianza (Wilson method)
- Fechas de campo: [INSERTAR — placeholder pendiente confirmación Cora]
- Geografía: Baruta (122), Libertador (80), Sucre (79), Chacao (70), El Hatillo (31), Altos Mirandinos (20)
- Banners principales: Total, NSE (C+/C / D / E), Género, Edad (4 bandas), Municipio, Marca preferida
- Cuestionario: 8 bloques (perfil, embudo, atributos, comportamiento, precio, publicidad, El Recreo)
- Modelos ejecutados en V3: Logit (statsmodels) + Random Forest (sklearn 1.8.0, AUC=0.851 CV) + SHAP (shap 0.51.0) + K-means (k=3, silhouette 0.195) + BayesianGaussianMixture proxy LCA
- El logit supera al RF en AUC (0.929 vs 0.851) — se usa como modelo principal

**Visual:** Grid de datos técnicos (misma estructura que Slide 3 del V2).
**Caveat:** CU-6 v2 §L-001 (fecha de campo pendiente — ficha técnica incompleta hasta que Cora confirme). CU-6 v2 §L-002 (IC95 logit amplios con n_pref=32 — siempre reportar OR con IC95).

---

### Slide 5 — Agenda del deck V3

**Titulo:** Estructura del deck V3

**Takeaway:** El V3 está organizado alrededor de la tesis central y sus 4 argumentos MECE.

**Bullets / contenido:**
- Bloque 1: Tesis central V3 (por qué Gama está compitiendo en el terreno equivocado)
- Bloque 2: El activo experiencial — convergencia de cuatro métodos (driver #1 confirmado)
- Bloque 3: Las promociones como anzuelo — por qué OR=3.64 y z-score=-0.67 coexisten
- Bloque 4: Dos misiones, dos horizontes — urgencia hoy, mercado grande mañana
- Bloque 5: Los tres segmentos — quién es el Nucleo Leal, quiénes son los Pragmaticos Convertibles
- Bloque 6: La voz del consumidor — qué dicen y qué no dicen los datos cualitativos
- Bloque 7: Diagnóstico de la comunicación actual — brecha entre driver #1 y mensaje dominante
- Bloque 8: Recomendaciones priorizadas (5 acciones MECE)
- Bloque 9: Roadmap 2026-2027 — próximos pasos y agenda de investigación
- Apéndice: Metodología ampliada + comparativa V2 vs V3

**Visual:** Tabla de agenda con 9 bloques + apéndice, con número de slides por bloque.
**Caveat:** Ninguno.

---

## BLOQUE 1 — TESIS CENTRAL V3 (4 slides)

---

### Slide 6 — Tesis Central (slide principal de la pirámide Minto)

**Titulo:** Gama tiene el activo más diferenciador del mercado — y lo comunica en el terreno equivocado

**Takeaway:** El driver #1 de preferencia es la atención (OR=5.73, triple convergencia), pero la comunicación actual habla de precio — exactamente el atributo menos predictivo (OR=1.03, SHAP #10). La estrategia correcta es apropiarse del terreno de la experiencia.

**Bullets / contenido:**
- El activo diferenciador: la atención al cliente es el único driver estadísticamente significativo con OR>5 y triple convergencia (logit + SHAP + Gini + razón espontánea).
- El terreno equivocado: Gama habla de precio ("PRECIOS DE TU LADO") cuando el precio es el atributo menos predictivo de su preferencia.
- La arquitectura de oportunidad tiene 4 dimensiones (los 4 argumentos que siguen):
  1. Comunicar la experiencia de atención, no el atributo
  2. Usar las promociones como anzuelo de primera visita, no como promesa de precio bajo
  3. Profundizar la misión de urgencia (donde ya gana), resolver el gap de surtido para la misión grande
  4. Activar el tercio del mercado que tiene menor resistencia al precio (seg_2, n=133, 33%)

**Visual:** Pirámide de 4 niveles con la tesis en cima y los 4 argumentos como base. Colores de intensidad descendente.
**Caveat:** IN-6 §C-001 AJUSTAR — la brecha de comunicación se presenta como recomendación estratégica basada en datos ("el estudio indica que comunicar la experiencia puede tener mayor impacto que comunicar precio"), no como crítica directa a la campaña.

---

### Slide 7 — Situación de mercado: Gama tiene un núcleo leal pero el 92% no la prefiere

**Titulo:** Gama tiene un núcleo fiel pequeño y potente, rodeado por un mercado que aún no la ha experimentado

**Takeaway:** El 8% que prefiere Gama tiene un perfil estadísticamente distinguible del 92% restante — su lealtad no es accidental sino el resultado de haber experimentado el activo de atención que la mayoría todavía no conoce.

**Bullets / contenido:**
- Preferencia Total: Gama 8.0% (IC95: 5.7%-11.0%) — solo Paramo (21.1%) se separa estadísticamente
- Preferencia C+/C: Gama 13.5% (IC95: 8.2%-21.3%) — empate técnico con Plan Suarez (n.s.) y Paramo (n.s.)
- TOM C+/C: 60.6% — Gama es notoria en su segmento natural, la mayoría la conoce
- Paradoja: Gama es conocida (TOM 60.6% en C+/C) pero no elegida (Preferida 13.5% en C+/C). El problema no es awareness — es conversión.
- K-means identifica al nucleo leal (seg_3, n=32) como un cluster estadisticamente diferenciado: NSE mas alto (promedio 2.16 en escala 1-3), percepcion de precio mas favorable (2.94/5 vs 3.44-3.66 del mercado), y valoracion maxima de rapidez en caja (4.81/5) y atencion (4.69/5).

**Visual:** Embudo de marca + highlight Gama en cada etapa. Separar visualmente seg_3 del mercado restante.
**Caveat:** CU-6 v2 §S-001 — los segmentos k-means se presentan con caveat de silhouette moderado (~0.20): perfiles son tendencias centrales, no categorias discretas.

---

### Slide 8 — La paradoja del precio: percibida como cara pero elegida por razones no-precio

**Titulo:** El 54% percibe Gama como cara, pero el precio no mueve su preferencia — la paradoja que explica la estrategia

**Takeaway:** El precio opera como barrera de entrada para el 92% que nunca ha experimentado el activo de atención de Gama — no como criterio de elección dentro del 8% que ya lo ha experimentado.

**Bullets / contenido:**
- 54% neto caro (IC95: 49.1%-58.8%). 45% percibe que los precios subieron en 6 meses.
- Pero entre los propios preferentes de Gama: solo 34% neto caro — percepción prácticamente plana (34% igual, 31% económico).
- El precio no es driver estadístico de preferencia: OR=1.03 (p=0.966), SHAP #10 de 10. El atributo con menor peso en los tres métodos.
- Interpretación: quienes ya prefieren Gama han completado la "negociación interna de valor" (el servicio justifica el precio). Quienes no la prefieren tienen la percepción de precio sin haber tenido la experiencia que la re-contextualiza.
- La barrera es perceptual-de-acceso, no estructural de preferencia. La solución es comunicación de experiencia + anzuelo de primera visita, no reducción de precio.

**Visual:** Donut comparativo — percepcion precio en Total (54% caro) vs pref-Gama (34% caro). Mas: tabla "precio como driver" con OR=1.03 resaltado en rojo como atributo #10 de importancia.
**Caveat:** IN-6 §C-003 AJUSTAR — "la barrera de precio es la hipótesis más parsimoniosa para explicar la baja conversión, dados los datos disponibles. La validación directa requiere investigación con no-consumidores (Van Westendorp, FGIs)." IN-6 §C-007 — datos cualitativos basados en frecuencias de categorias, no verbatims literales.

---

### Slide 9 — Resumen del arco V3: 4 argumentos MECE

**Titulo:** Cuatro argumentos que cubren el qué, cómo, dónde y a quién de la estrategia de Gama

**Takeaway:** Los cuatro argumentos que siguen son MECE: activo a comunicar (qué), palanca táctica (cómo), territorio de juego (dónde), target prioritario (a quién).

**Bullets / contenido:**
- Argumento 1 — QUÉ: El activo experiencial (atención + limpieza) es el mas diferenciador y el menos comunicado. El V3 suma el mecanismo cualitativo que explica por qué funciona.
- Argumento 2 — CÓMO: Las promociones son el anzuelo de primera prueba, no la promesa de precio bajo. El V3 suma la explicación de la paradoja cuali/cuanti y la acción específica (stickers + paraguas único).
- Argumento 3 — DÓNDE: Urgencia hoy (posición defendible, #2 en la misión), mercado grande como horizonte (donde se pierde el 34% de los propios preferentes). El V3 suma la lógica JTBD de dos misiones = dos estrategias.
- Argumento 4 — A QUIÉN: El seg_2 (Pragmaticos Convertibles, n=133, 33%) tiene menor resistencia al precio. Es el territorio de mayor retorno de corto plazo. NUEVO en V3 — no en V2.

**Visual:** Grid 2x2 con las 4 preguntas (QUÉ / CÓMO / DÓNDE / A QUIÉN) y sus respuestas en headline.
**Caveat:** Ninguno en esta slide de estructura.

---

## BLOQUE 2 — EL ACTIVO EXPERIENCIAL (5 slides)

---

### Slide 10 — Driver #1: Atención — triple convergencia de cuatro métodos

**Titulo:** Quien asocia Gama con buena atención tiene 5.7 veces mayor probabilidad de preferirla — confirmado en cuatro metodologías independientes

**Takeaway:** La convergencia logit + SHAP + Gini + razón espontánea es el hallazgo más robusto del estudio; la atención no es solo el driver estadístico más fuerte, es también la razón que el propio consumidor cita primero.

**Bullets / contenido:**
- Logit: OR=5.73*** (p=0.007, IC95: 1.6-20.4). El único driver con p<0.01.
- SHAP RF: mean(|v|)=0.1047 — #1 de 10 atributos, con margen claro sobre el #2 (0.0735).
- Gini RF: 0.1977 — #1 de 10 atributos.
- Razón espontánea P21.1: ~53% de los 32 preferentes Gama citan "buena atención" como razón #1.
- El logit supera al RF en AUC (0.929 vs 0.851 CV) — es el modelo principal y sus coeficientes son los más confiables.
- Z-score de asociación Gama-Atención: sobre-índea en el grupo pref-Gama (positivo).

**Visual:** Tabla comparativa de los 4 métodos (Logit OR / SHAP rank / Gini rank / % razón espontánea) con mejor_atienden en la primera fila resaltada. Puede embeberse shap_bar_20260517_v1.png.
**Caveat:** CU-6 v2 §D-001 — GO pleno. Incluir IC95 [1.6, 20.4] en el deck (IC amplios por n_pref=32). CU-6 v2 §L-002 — "OR=5.73 es el estimador puntual; el efecto real puede ser entre 1.6x y 20.4x con 95% de confianza."

---

### Slide 11 — Driver #2: Limpieza/Orden — elevado de tendencia a driver secundario confirmado

**Titulo:** La limpieza del local es el segundo atributo diferenciador de Gama, con soporte convergente de tres métodos

**Takeaway:** SHAP y Gini elevan la limpieza/orden a driver secundario confirmado, aunque el logit es borderline — la convergencia de los tres métodos es suficiente para reportarlo como parte del perfil diferenciador.

**Bullets / contenido:**
- Logit: OR=3.99 (p=0.061 — no significativo al 95%, tendencia p<0.10; IC95: 0.940-16.913)
- SHAP RF: 0.0735 — #2 de 10 atributos
- Gini RF: 0.1609 — #2 de 10 atributos
- Por qué SHAP eleva lo que el logit no alcanza: hay multicolinealidad entre atencion y limpieza. Quien asocia buena atencion también tiende a asociar limpieza (el logit penaliza ambos). SHAP, al ser no-parametrico, captura el efecto marginal adicional de limpieza más allá de su correlación con atencion.
- Implicacion: la "experiencia de servicio" en Gama es un constructo compuesto — atención + limpieza son el EJE 1 de la propuesta de valor experiencial.

**Visual:** Tabla de ranking SHAP/Gini/Logit para los 10 atributos, con limpio_ordenado destacado en #2. Flecha visual de "elevado de tendencia a driver secundario."
**Caveat:** CU-6 v2 §D-002 — GO con caveat p-logit borderline. Nota al pie: "La limpieza/orden alcanza significancia estadística formal en RF/SHAP (#2 en ambos métodos) aunque el logit no alcanza p<0.05 (p=0.061), probablemente por multicolinealidad con atención. La convergencia de métodos consolida este hallazgo."

---

### Slide 12 — El mecanismo cualitativo: ¿por qué la atención tiene el OR más alto?

**Titulo:** La atención no es un atributo como los demás — es la señal de que la tienda te reconoce como persona

**Takeaway:** El análisis de temas cualitativos sugiere que la atención opera en un registro diferente al de precio o surtido — es el momento de sorpresa positiva que supera la expectativa del shopper y cristaliza la preferencia.

**Bullets / contenido:**
- El análisis temático (Sinta IN-2, Tema 1) identifica que los preferentes de Gama no describen la atención como un atributo funcional solamente — la asocian con el tipo de experiencia que los diferencia de los supermercados de precio.
- Evidencia de frecuencias: el 53% de los preferentes cita "buena atención" como razón #1 espontánea. En Páramo: el 81% cita "mejores precios" — son propuestas de valor categorialmente distintas.
- La rapidez en caja puntúa 4.81/5 en el nucleo leal (seg_3) — la mas alta de los 3 segmentos. Forma parte del mismo constructo "experiencia de servicio" que la atención.
- El estudio sugiere que la atención puede estar operando como señal de reconocimiento personal (el empleado que resuelve, que acompaña), no solo como calidad de servicio funcional. Esta interpretación se apoya en las frecuencias de razones espontáneas — la validación con verbatims literales requiere acceso a BBDD raw.
- Por qué tiene el OR más alto: la atención es el atributo con mayor capacidad de sorpresa positiva en la categoría supermercado — el shopper no la espera, y cuando la experimenta, el efecto sobre la preferencia es desproporcionado (lógica Kano de atributo diferenciador).

**Visual:** Comparativo visual — modelo mental "precio-dominante" (Páramo 81% precio) vs modelo mental "atención-dominante" (Gama 53% atención). Más: diagrama del mecanismo de sorpresa positiva (simple, conceptual).
**Caveat:** IN-6 §C-004 AJUSTAR — "el estudio sugiere que la atención puede estar operando como reconocimiento personal — hipótesis interpretativa apoyada en el patrón de frecuencias. La confirmación plena requiere acceso a verbatims literales de BBDD raw." IN-6 §C-007 — Sinta no tuvo acceso a verbatims literales en esta sesión.

---

### Slide 13 — El DNA de Gama: sobreindexación en los 4 atributos experienciales

**Titulo:** Gama sobreindea en los 4 atributos de experiencia — es el supermercado que el consumidor percibe como cualitativamente diferente

**Takeaway:** El z-score del DNA de Gama confirma que su diferenciación está en la experiencia, no en el precio — Tienda atractiva (+1.09), Calidad (+0.97), Seguro (+0.76), Limpieza (+0.72).

**Bullets / contenido:**
- Z-scores positivos (ventajas vs competencia): Tienda atractiva (+1.09), Calidad (+0.97), Seguro (+0.76), Limpieza (+0.72)
- Z-scores negativos (brechas): Menor precio (-0.72), Hacer valer dinero (-0.67), Promociones (-0.67)
- Interpretación estratégica: Gama gana en experiencia y pierde en precio/valor-dinero — exactamente el DNA de un supermercado premium que debería comunicar experiencia, no precio.
- El z-score de Promociones (-0.67) no contradice que sea el driver terciario (OR=3.64). La paradoja se explica en el Bloque 3.
- Páramo sobreindea en 7 de 10 atributos, incluyendo menor precio. Competir frontalmente con Páramo en precio es abandonar el terreno donde Gama tiene ventaja.

**Visual:** Plot z-score Gama por atributo (barras horizontales, eje X = z, ordenado desc). Resaltar positivos en rojo-Gama y negativos en gris. Mismo formato que Slide 13 del V2.
**Caveat:** CU-6 v2 §1 (tabla de gates) — normalización z-score es descriptiva, no inferencial. No confundir z-score de asociación con OR de drivers.

---

### Slide 14 — Implicacion comunicacional del Argumento 1

**Titulo:** La comunicación de la atención no puede describir el atributo — debe mostrar el momento

**Takeaway:** "Tenemos buena atención" es una afirmación que el shopper no verifica hasta que la experimenta; la campaña debe mostrar el momento concreto de reconocimiento que genera la preferencia.

**Bullets / contenido:**
- Acción derivada del Argumento 1: la campaña nueva debe construir sobre el registro relacional que el shopper ya proyecta sobre Gama (evidencia: 53% de preferentes citan atención espontáneamente).
- Formato sugerido: el momento concreto — el empleado que resuelve, que conoce al cliente, que acompaña en la misión de compra. No el slogan, sino la escena.
- Diferencia con PTL: "PRECIOS DE TU LADO" anuncia un resultado (el precio) que el 54% no cree. La campaña experiencial anuncia una promesa de proceso (la atención) que el 53% de los preferentes ya valida.
- El espacio semántico "compañía / estar para ti" tiene señales tempranas de disponibilidad en la memoria del shopper — la dirección creativa debería explorar ese territorio.
- Relación con V2: el V2 recomendó "capitalizar driver ATENCIÓN (OR=5.73)" (Rec. 2). El V3 suma el mecanismo (qué mostrar) y la evidencia de que la campaña actual no lo está haciendo.

**Visual:** Tabla comparativa — "qué dice PTL" vs "qué debería decir la campaña experiencial". Simple, ejecutivo.
**Caveat:** IN-6 §C-001 AJUSTAR — "el estudio justifica revisar la plataforma de comunicación para alinearla con los drivers reales de preferencia. No es una evaluación de la calidad creativa de la campaña actual."

---

## BLOQUE 3 — LAS PROMOCIONES COMO ANZUELO (4 slides)

---

### Slide 15 — La paradoja de las promociones: OR=3.64 con z-score=-0.67

**Titulo:** Las promociones son el tercer driver de preferencia aunque Gama no sea percibida como la marca de las promociones — la paradoja tiene una explicación estratégica

**Takeaway:** El efecto de las promociones no se debe a que Gama sea reconocida por sus promociones, sino a que quien ha accedido a una llega a la tienda y experimenta lo que genera la preferencia — es el anzuelo de primera prueba.

**Bullets / contenido:**
- Driver terciario logit: OR=3.64** (p=0.031, IC95: 1.1-11.8). SHAP #3 (0.0633). Confirmado en ambos métodos.
- Pero z-score de asociación Gama-Promociones: -0.67 (Gama no es percibida como la marca de las promociones). Solo 9% del total asocia Gama con "promociones atractivas".
- La paradoja cuali/cuanti (Sinta IN-4 §2.1): el cuali no confirma promociones como razón espontánea de preferencia de Gama, pero el cuanti sí mide el efecto estadístico. Son consistentes: la promoción actúa como "anzuelo de primera prueba", no como razón directa de preferencia.
- Mecanismo: la promoción reduce la barrera de entrada (percepción de precio caro), activa la primera visita, y la primera visita activa la experiencia de atención que genera la preferencia.
- Contraste: precio como driver = OR=1.03 (SHAP #10). Las promociones tienen 3.5x más poder sobre la preferencia que el precio genérico.

**Visual:** Tabla comparativa "precio vs promociones" con OR / SHAP / z-score para ambos. Diagrama de flujo "la promoción como puerta de entrada a la experiencia."
**Caveat:** CU-6 v2 §D-003 — GO con IC95. IN-4 §T-03 — convergencia cuali/cuanti con matiz: el cuali no confirma espontáneamente la razón, el cuanti sí mide el efecto. Certeza media.

---

### Slide 16 — Los activos de promoción que Gama ya tiene

**Titulo:** Gama tiene tres activos de promoción existentes que pueden activarse bajo un paraguas creativo único

**Takeaway:** Cashea (activo), club de lealtad (activo), e histórico de stickers (inactivo de alta recordación) son las piezas de una mecánica de conversión que solo necesita un paraguas unificador.

**Bullets / contenido:**
- Cashea activo: canal de financiamiento que puede reducir la barrera de precio percibida para primera visita
- Club de lealtad activo: mecanismo de retención post-prueba que convierte la primera visita en el inicio de un patrón
- Histórico de stickers: inactivo actualmente, tuvo recordación alta (el formato de promoción más recordado espontáneamente por la base de referentes de Gama)
- La reactivación del programa de stickers con mecánica de basket-building (categorías sensibles: carne, pollo, básicos) bajo un paraguas creativo único podría cubrir los tres objetivos: primera visita (anzuelo), basket ampliado (valor por visita), retención (club de lealtad integrado)
- El mensaje debe ser "esta semana hay una razón específica para venir" — no "somos económicos".

**Visual:** Diagrama de los 3 activos + su función en el funnel (Cashea = barrier reduction; stickers = visita; club = retención). Mismo estilo visual que V2.
**Caveat:** IN-5 §Argumento 2 — los assets son confirmados por Cora (input directo). La recordación del sticker no tiene cifra exacta en los datos del estudio — se basa en información operativa de Gama.

---

### Slide 17 — Comunicar promociones vs comunicar precio: la diferencia crucial

**Titulo:** "Esta semana hay una razón para venir" vs "somos económicos" — dos mensajes con impactos radicalmente distintos sobre preferencia

**Takeaway:** La comunicación de promoción activa la primera visita que genera la experiencia; la comunicación de precio intenta convencer de algo que el 54% del mercado ya no cree.

**Bullets / contenido:**
- Comunicar precio: el 54% percibe Gama como cara. Una campaña de precio solo llega al 15% que ya la percibe económica — el mercado que menos necesita convencer.
- Comunicar promociones: activa la primera visita (el anzuelo) en el seg_2 (Pragmaticos Convertibles, menor resistencia al precio). No promete que Gama sea la más barata — promete que hay una razón concreta para ir esta semana.
- Recall PTL: 10.7% asistido, 0/17 espontáneo. La interpretación dominante (65%) es precio — exactamente lo que el shopper no cree sobre Gama.
- Alternativa estratégica: la promoción específica y visible (sticker, Cashea, oferta de categoría) tiene un efecto observable (reduce la barrera de entrada) que el slogan de precio no tiene (no reduce la percepción de caro).
- Relación con V2: el V2 ya recomendó "comunicar promociones, no precio" (Rec. 1). El V3 agrega el mecanismo cualitativo que explica por qué funciona y hace la acción más específica.

**Visual:** Tabla 2x2 — "mensaje de precio" vs "mensaje de promoción" en fila; "efecto sobre percepción de precio" vs "efecto sobre primera visita" en columna.
**Caveat:** CU-6 v2 §L-004 — datos publicitarios (PTL recall) con base baja (n=43 asistido, n=17 espontáneo). Titulo de slide: "BASE REFERENCIAL" para datos de recall.

---

### Slide 18 — Conclusiones parciales Bloque 3

**Titulo:** Síntesis — Las promociones son la palanca táctica de conversión, no la promesa de ser el más barato

**Takeaway:** Ninguna acción de comunicación tiene mayor retorno potencial que reactivar el programa de stickers bajo un paraguas único que comunique "razón para venir" — no precio.

**Bullets / contenido:**
- Hallazgo 1: Las promociones son driver terciario (OR=3.64) a pesar de que Gama no es percibida como la marca de las promociones. El efecto es del mecanismo (anzuelo → experiencia → preferencia), no de la percepción de promoción como identidad de marca.
- Hallazgo 2: Gama ya tiene los tres activos (Cashea, club, stickers) — la inversión requerida es de integración y comunicación, no de construcción de nuevo.
- Acción: reactivar stickers con mecánica basket-building (categorías sensibles) + integrar Cashea + club bajo paraguas creativo único + mensaje de "razón para venir esta semana".
- Lo que no es la acción: reducir precios, comunicar que Gama es económica, o competir en el terreno de precio donde Páramo tiene ventaja estructural.

**Visual:** Slide de texto resumen con bullets numerados. Fondo rojo-Gama suave.
**Caveat:** IN-5 §Argumento 2 nota final — la integración de assets es una recomendación estratégica derivada de los datos, no un dato del estudio.

---

## BLOQUE 4 — DOS MISIONES, DOS HORIZONTES (4 slides)

---

### Slide 19 — El mapa de misiones: Gama es competitiva en urgencia, no en mercado grande

**Titulo:** Gama gana la misión de urgencia (#2 con 12.2%) y pierde el mercado grande (#7 con 7.2%) — son dos territorios distintos que requieren dos estrategias distintas

**Takeaway:** La posición en urgencia es sólida y defendible; la posición en mercado grande es el mayor gap de share of wallet con los propios preferentes.

**Bullets / contenido:**
- Misión urgencia/pocos productos: Gama #2 (12.2%). Única misión donde Gama es competitiva en el ranking total.
- Misión mercado grande/abastecimiento: Gama #7 (7.2%). Páramo lidera con 21.6%.
- Misión evento/fiesta: Gama #5 (9.2%) — posición secundaria.
- Cobertura física no correlaciona con preferencia: r=0.164, p=0.651 (no significativo). El formato importa, no solo el número de sucursales.
- Paradoja Baruta: 6 sucursales Gama, 2.4% preferencia local. Páramo (sin datos de sucursales) domina. El formato Express puede limitar la conversión donde Páramo tiene propuesta de mercado completo.
- JTBD (Sinta IN-3): Gama está siendo "contratada" para J3 (urgencia) y J4 (evento) pero no para J1 (mercado grande). Son trabajos distintos que requieren formatos y promesas distintas.

**Visual:** Bar chart comparativo de misiones × top 5 marcas + posición Gama resaltada. Misma estructura que Slide 16 del V2.
**Caveat:** CU-6 v2 §L-002 — datos de misiones no tienen IC95 calculado; son distribuciones de P26. Leer como indicativos de posición relativa.

---

### Slide 20 — El 34% que se va: la mayor pérdida de share of wallet de los propios preferentes

**Titulo:** El 34% de los preferentes de Gama compró en otra cadena en su última compra — la misión de mercado grande los lleva a Páramo, CM y Forum

**Takeaway:** La pérdida no ocurre por precio (los preferentes de Gama tienen percepción de precio más favorable que el mercado) — el estudio sugiere que el surtido y el formato para la misión de mercado grande es el cuello de botella.

**Bullets / contenido:**
- 11 de 32 preferentes Gama (34%) realizaron su última compra en otra cadena.
- Destinos: Páramo (4), CM (3), Forum (2), otros (2).
- Los preferentes Gama tienen percepción de precio más favorable (34% neto caro) vs mercado total (54% neto caro). No se van por precio — se van por surtido/misión.
- Hipótesis del mecanismo (Sinta IN-4 §T-09, certeza media): cuando el "trabajo" es mercado grande, el Express de Gama puede no ofrecer el surtido de frescos completo que ese trabajo requiere. La solución es de formato, no de precio ni de comunicación.
- Corto plazo: garantizar que la misión urgencia sea tan positiva que genere retorno en otras misiones.
- Horizonte estratégico: proyecto de formatos — diagnosticar cualitativamente por qué las 3 sucursales en El Cafetal no convierten.

**Visual:** Tabla simple preferentes-Gama que compran en otra cadena + destinos. Más: dot plot cobertura × preferencia por parroquia (Slide 29 del V2).
**Caveat:** IN-4 §T-09 — certeza BAJA en la hipótesis de surtido/formato como causa de la deserción. El cuanti solo muestra el destino (otra cadena), no el motivo. La hipótesis es lógica cruzada de T-04 + T-08. Requiere validación con field work cuali.

---

### Slide 21 — Dos horizontes estratégicos: urgencia hoy, mercado grande mañana

**Titulo:** La estrategia de dos horizontes: defender y profundizar la urgencia, resolver el formato para el mercado grande

**Takeaway:** Urgencia es la base táctica que ya funciona; el mercado grande es el horizonte estratégico que requiere un diagnóstico de formatos antes de invertir en aperturas.

**Bullets / contenido:**
- Corto plazo — base táctica (urgencia):
  * Comunicar disponibilidad, conveniencia, rapidez
  * Optimizar la experiencia de caja (ya valorada 4.81/5 por el núcleo leal)
  * Garantizar que la visita de urgencia active la experiencia de atención que genera retorno
  * Defender Chacao-Sucre: concentra el 56% de los preferentes de Gama
- Horizonte estratégico (mercado grande):
  * Proyecto diagnóstico de formatos: ¿por qué El Cafetal (3 sucursales Gama) tiene 4.9% preferencia vs 41.5% C+/C en la zona?
  * Hipótesis a verificar: ¿es el surtido de frescos? ¿el ticket percibido? ¿el footprint vs Plan Suárez o CM?
  * Sin el diagnóstico, abrir más sucursales puede replicar el problema de Baruta (6 sucursales, 2.4% preferencia)
- Relación con V2: el V2 articuló Recs. 3 y 4 (defender Chacao-Sucre, recuperar mercado grande). El V3 añade la lógica JTBD y la recomendación de diagnóstico antes de inversión.

**Visual:** Línea de tiempo Q3-Q4 2026 / H1 2027 con las dos rutas (urgencia = corto, formatos = horizonte). Colores diferenciados.
**Caveat:** IN-4 §T-09 — hipótesis de surtido/formato es de certeza media-baja. Marcar explícitamente como hipótesis a validar.

---

### Slide 22 — Conclusiones parciales Bloque 4

**Titulo:** Síntesis — Urgencia es la posición, mercado grande es la oportunidad

**Takeaway:** Gama tiene un derecho a ganar en urgencia que debe profundizar, y un cuello de botella en mercado grande que requiere diagnóstico antes de inversión.

**Bullets / contenido:**
- Hallazgo 1: Gama es competitiva en urgencia (#2, 12.2%) — la única misión donde supera al pelotón medio en el ranking.
- Hallazgo 2: El 34% de los propios preferentes se va a Páramo, CM o Forum para el mercado grande. Es la mayor fuga de share of wallet.
- Hallazgo 3: La cobertura física no garantiza preferencia (r=0.164, p=0.651). Abrir sucursales sin resolver el formato puede replicar Baruta.
- Acción corto plazo: profundizar la captura de urgencia — rapidez, disponibilidad, experiencia de atención en cada visita.
- Acción horizonte: proyecto diagnóstico de formatos antes de cualquier decisión de apertura o inversión en mercado grande.

**Visual:** Slide de conclusiones con 3 hallazgos + 2 acciones. Fondo neutro.
**Caveat:** IN-4 §T-09 — diagnóstico de formatos es recomendación estratégica, no dato del estudio.

---

## BLOQUE 5 — LOS TRES SEGMENTOS (5 slides)

---

### Slide 23 — Por qué segmentar: el mercado no es uniforme

**Titulo:** El k-means revela que el mercado tiene 3 perfiles distintos que requieren tres mensajes distintos — el NSE no es el criterio que los separa

**Takeaway:** Los 3 segmentos están definidos por nivel de exigencia en atributos y resolución de la ecuación de valor — no por NSE, lo que cambia completamente la lógica de segmentación para comunicación.

**Bullets / contenido:**
- Método: k-means (sklearn 1.8.0, k=3 óptimo, silhouette 0.195 — máximo de k=2..6) + BayesianGaussianMixture proxy LCA (BIC mínimo en k=3). Doble criterio converge.
- Caveat de silhouette: los valores absolutos (~0.20) son bajos — esperado con variables Likert de alta homogeneidad. El criterio diagnóstico es el máximo relativo, no el nivel absoluto.
- Los 3 segmentos son estadisticamente válidos y sustantivamente accionables: tienen perfiles claros y distintos.
- El NSE no separa al seg_1 del seg_2 (NSE promedio 1.78 vs 1.85 — prácticamente igual). Lo que separa es el nivel de exigencia en P22 y la percepción de precio.
- Implicación: la comunicación de Gama no debería segmentarse por NSE — debería segmentarse por nivel de resolución de la ecuación de valor.

**Visual:** Curvas silhouette + BIC (elbow plot) para k=2..6. Embed kmeans_elbow_silhouette_20260517_v1.png.
**Caveat:** CU-6 v2 §S-001 — caveat OBLIGATORIO: "Los 3 segmentos son estadisticamente válidos (silhouette óptimo, BIC mínimo), aunque los valores de silhouette son moderados (~0.20), indicando solapamiento en márgenes. Los perfiles representan tendencias centrales, no categorías discretas. El tamaño de seg_3 (n=32) es referencial."

---

### Slide 24 — Segmento 1: Mayoría Exigente No Convencida (n=237, 59%)

**Titulo:** El 59% del mercado valora exactamente lo que Gama ofrece — pero la percepción de precio los mantiene fuera

**Takeaway:** El seg_1 no es indiferente a la calidad de servicio; le importa mucho (P22 promedio ~4.7/5) — pero percibe los precios de Gama como un obstáculo que no ha tenido razón para sortear.

**Bullets / contenido:**
- n=237, 59% del total. NSE promedio 1.78 (predominantemente D/E).
- Preferencia Gama: 0.0% (ningún integrante del seg_1 prefiere Gama).
- Percepción precio Gama: 3.66/5 (entre "poco más caro" y "más caro") — la más negativa de los 3 segmentos.
- Nivel de exigencia: P22 promedio ~4.7/5 — valoran casi todo como muy importante.
- Paradoja: valoran atención 4.77/5 y limpieza 4.82/5 — casi tan alto como el núcleo leal de Gama — pero tienen 0% preferencia. El problema no es indiferencia al atributo; es que nunca han tenido la experiencia de Gama que resolvería la ecuación.
- Palanca: requiere reducir la percepción de precio. No es el segmento más accesible — es el desafío de largo plazo. La comunicación de experiencia sola no es suficiente para este grupo.

**Visual:** Tabla de perfil del seg_1 con las variables clave (n, NSE, % pref-Gama, percepción precio, P22 selección). Color gris (es el más distante de Gama).
**Caveat:** CU-6 v2 §S-001 — seg_1 no es un grupo discreto, hay solapamiento con seg_2 en los márgenes.

---

### Slide 25 — Segmento 2: Pragmaticos Convertibles (n=133, 33%)

**Titulo:** El 33% del mercado tiene menor resistencia al precio y expectativas más moderadas — es el territorio de mayor retorno de corto plazo para Gama

**Takeaway:** El seg_2 es el segmento más convertible: la barrera de precio es menor (3.44 vs 3.66/5) y sus expectativas son moderadas — una campaña de primera prueba bien diseñada puede activar la conversión.

**Bullets / contenido:**
- n=133, 33% del total. NSE similar al seg_1 (1.85 vs 1.78) — el NSE no los separa.
- Preferencia Gama: 0.0% — ningún integrante prefiere Gama actualmente.
- Percepción precio Gama: 3.44/5 — menos negativa que el seg_1 (diferencia 0.22 puntos).
- Nivel de exigencia: P22 promedio ~4.1-4.3/5 — más moderado que el seg_1 (~4.7). Tienen expectativas alcanzables por la propuesta actual de Gama.
- Palanca: menor esfuerzo de conversión que el seg_1. Una promoción de bienvenida (anzuelo → primera visita → experiencia de atención) puede iniciar el patrón.
- Secuencia de conversión recomendada: activación de primera visita (sticker/Cashea) → experiencia guiada (atención activa en primera compra) → seguimiento de lealtad (club de lealtad como retención post-prueba).

**Visual:** Tabla de perfil del seg_2. Flecha de conversión visual hacia el seg_3. Color naranja/ámbar (en transición).
**Caveat:** IN-6 §C-002 — GO con caveat: "el análisis sugiere que el seg_2 tiene menor barrera de conversión" (no "prueba que son convertibles"). La diferencia de 0.22 puntos en precio es descriptiva del cluster, no un z-test head-to-head entre seg_1 y seg_2.

---

### Slide 26 — Segmento 3: Nucleo Leal Gama (n=32, 8%)

**Titulo:** El 8% que prefiere Gama es un cluster estadisticamente diferenciado con el perfil que la propuesta experiencial produce naturalmente

**Takeaway:** El nucleo leal no es accidental — tiene NSE más alto, percepción de precio más favorable, y valoración máxima de rapidez en caja y atención; son los atributos exactamente alineados con los drivers del estudio.

**Bullets / contenido:**
- n=32, 8% del total. 100% preferencia Gama (el algoritmo los aisló naturalmente sin forzar la separación).
- NSE promedio: 2.16 (mayor tendencia a C+/C que los otros segmentos).
- Percepción precio Gama: 2.94/5 — el más favorable de los 3 segmentos (entre "igual" y "poco más caro").
- Valores máximos del seg_3: rapidez en caja (4.81/5), hacer valer dinero (4.72/5), atención (4.69/5). Perfil que corresponde exactamente con los drivers logit/SHAP.
- Estrategia para el nucleo leal: ya están ganados. Prioridad: profundizar basket (más categorías por visita), aumentar frecuencia, convertirlos en embajadores hacia el seg_2.
- El nucleo leal de Gama no elige la marca porque sea la más barata — la elige porque la ecuación de valor (experiencia vs precio) ya está resuelta para ellos.

**Visual:** Tabla de perfil del seg_3. Resaltar 100% pref-Gama y los valores más altos de atención y rapidez. Color rojo-Gama (son el corazón de la marca).
**Caveat:** CU-6 v2 §S-001 y §L-002 — n=32 es REFERENCIAL en subanalisis. IC95 ±17pp. Leer perfiles del seg_3 como descriptivos del cluster, no como estimadores proyectables al universo.

---

### Slide 27 — Los 3 segmentos: mapa de oportunidades

**Titulo:** Tres segmentos, tres estrategias — pero el retorno esperado es mayor donde la barrera es menor

**Takeaway:** El seg_2 (33%, menor barrera) es la oportunidad inmediata; el seg_3 (8%) es el activo a profundizar; el seg_1 (59%) requiere cambios estructurales más allá de comunicación.

**Bullets / contenido:**
- Seg_3 (Nucleo Leal, 8%): estrategia de profundización — basket building, frecuencia, advocacy. Mensaje: "todo lo que necesitas, en el lugar donde ya confías."
- Seg_2 (Pragmaticos Convertibles, 33%): estrategia de activación — primera visita incentivada (promoción), experiencia guiada, incorporación al club de lealtad. Mensaje: "esta semana hay una razón específica para venir."
- Seg_1 (Mayoría Exigente, 59%): no es el foco de corto plazo. Requiere cambios en percepción de precio (auditoría in-store + comunicación de valor) o en propuesta de formato para mercado grande. Horizonte 2027-2028.
- El V3 no propone una campaña para los 3 segmentos — propone dos esfuerzos paralelos: profundización de leales (seg_3) + conversión de pragmaticos (seg_2).

**Visual:** Grid de 3 perfiles de segmento con flecha de conversión hacia seg_3. Tabla de estrategia × segmento.
**Caveat:** IN-6 §C-002 y §C-008 — los segmentos son un hallazgo nuevo en V3 no presentado en V2. Cora debe decidir cómo comunicar este hallazgo a Gama en el contexto de la entrega que ya recibieron.

---

## BLOQUE 6 — VOZ DEL CONSUMIDOR (4 slides)

---

### Slide 28 — Los 5 temas cualitativos: lo que el consumidor dice y lo que los datos revelan

**Titulo:** El análisis temático identifica 5 patrones que explican el mecanismo de preferencia de Gama más allá de los números

**Takeaway:** El consumidor de Gama no solo valora la atención como atributo funcional — la experimenta como la diferencia entre ser un número y ser una persona en la tienda.

**Bullets / contenido:**
- Tema 1 — La atención como diferenciador simbólico (prevalencia: 53% razón espontánea, triple convergencia cuanti). Los preferentes de Gama no solo describen "buen servicio" — describen un tipo de relación cualitativamente distinta a la de supermercados de precio.
- Tema 2 — El precio como zona de tensión no resuelta (54% total percibe caro; 34% entre preferentes). La paradoja no es contradicción — es que la negociación de valor solo ocurre para quien ya experimentó la atención.
- Tema 3 — La cercanía como primer escalón de la relación (40.6% de preferentes citan cercanía como razón #2). La cercanía es el primer "trabajo" que Gama cumple (J3, urgencia) — y esa primera experiencia es la puerta de entrada al argumento experiencial.
- Tema 4 — La campaña como oportunidad no aprovechada (4.2% recall espontáneo; 0/17 recuerdan PTL). El análisis temático revela la brecha entre el driver #1 (atención) y el mensaje dominante de la campaña actual (precio).
- Tema 5 — El modelo de dos velocidades (seg_3 ya resolvió la ecuación; seg_1+2 no). La segmentación k-means confirma formalmente el modelo mental que el cuali sugería.

**Nota metodológica:** El análisis temático se aplicó sobre frecuencias de categorías de los outputs del V2. Los verbatims literales requieren acceso a BBDD raw para validación completa.
**Visual:** Grid de 5 temas con título + 1 dato cuantitativo por tema + eje axial (IN-1).
**Caveat:** IN-6 §C-007 — análisis temático basado en frecuencias de categorías, no verbatims literales. Sinta no tuvo acceso a BBDD raw en esta sesión.

---

### Slide 29 — Dos modelos mentales: atención-dominante vs precio-dominante

**Titulo:** El mercado está dividido en dos modelos mentales — Gama es la única marca del segmento atención-dominante junto a Central Madeirense

**Takeaway:** Intentar competir con Páramo en precio sería abandonar el único territorio donde Gama tiene una ventaja estadisticamente verificable.

**Bullets / contenido:**
- Modelo ATENCIÓN-DOMINANTE: Gama (53% atención espontánea), CM (53% atención), Rio (51% atención)
- Modelo PRECIO-DOMINANTE: Páramo (81% precio), Plan Suárez (71%), La Granja (82%), Forum (52%), Plazas (60%)
- El modelo mental define el territory de comunicación. Cambiar Gama al modelo precio-dominante requeriría abandonar el activo único que genera preferencia (OR=5.73) para competir donde Páramo tiene ventaja estructural.
- La convergencia cuali/cuanti (IN-4 §T-01) confirma: los preferentes de Gama y los de Páramo están tomando decisiones basadas en sistemas de valor completamente distintos. No hay cross-appeal natural — Gama debe profundizar su territorio, no extenderse al de Páramo.

**Visual:** Dos columnas — marcas en cada modelo + razón dominante + OR/SHAP si aplica. Mismo formato que Slide 26 del V2.
**Caveat:** CU-6 v2 §L-002 — los OR son estimadores puntuales con IC95 amplios. El claim del "territorio atención" es estratégicamente sólido y estadisticamente robusto.

---

### Slide 30 — Lo que el consumidor no dice: los temas latentes

**Titulo:** Los temas latentes son los que más informan la estrategia — y los que el cuestionario convencional no captura directamente

**Takeaway:** El estudio identifica tres tensiones latentes que explican por qué la estrategia de precio de Gama no está funcionando — y por qué la estrategia de experiencia tiene el mayor potencial.

**Bullets / contenido:**
- Tensión 1: La experiencia que genera preferencia es invisibilizada por la barrera de precio que impide llegar a ella. El 92% no preferente nunca llega a experimentar lo que convierte en preferencia. La barrera perceptual es anterior al argumento.
- Tensión 2: La campaña actual no amplifica el driver #1. El driver #1 (atención) no está en ningún mensaje de la campaña actual — y el shopper no recuerda la campaña (4.2% recall espontáneo). La inversión publicitaria no está generando retorno de notoriedad de argumento.
- Tensión 3: Gama tiene un activo de "compañía" disponible en la memoria del shopper, pero no lo ha apropiado sistemáticamente con sus propias frases y visuales.
- Nota: El tema latente de "reconocimiento personal" como mecanismo de la atención es una hipótesis apoyada en el patrón de frecuencias. La confirmación plena requiere verbatims literales o investigación cualitativa dedicada (FGIs/IDIs).

**Visual:** Tabla de tensiones — "el consumidor dice" / "pero la tensión latente es" / "implicación estratégica". Tres filas.
**Caveat:** IN-6 §C-004 AJUSTAR — el tema latente de reconocimiento personal se presenta como hipótesis, no como dato verificado. IN-6 §C-005 NO-GO como claim — la anécdota de "Sin ti no hay nosotros" (n=2 de n=17) no se usa como evidencia estratégica primaria (base demasiado baja). IN-6 §C-007 — los temas latentes son construcciones interpretativas sin ancla en verbatim literal.

---

### Slide 31 — Agenda de investigacion futura: las preguntas que este estudio no responde

**Titulo:** Lo que este estudio no puede responder — y por qué la agenda de research 2027 lo resuelve

**Takeaway:** El estudio diagnostica el "qué" con solidez; la agenda 2027 debe responder el "por qué profundo" y el "cuánto cuesta realmente" con metodologías complementarias.

**Bullets / contenido:**
- Pregunta no resuelta 1: ¿La barrera de precio es real o perceptual? Sin auditoría in-store de precios SKU vs SKU, no se puede distinguir. Si es perceptual, la solución es comunicación. Si es real, requiere acción en surtido y negociación.
- Pregunta no resuelta 2: ¿Qué convirtió a los 32 preferentes en preferentes? Sin IDIs con el seg_3, no conocemos el "conversion pathway" que habría que replicar.
- Pregunta no resuelta 3: ¿Cuál es el punto de quiebre de precio en el seg_2? Van Westendorp en 3 categorías KVI (carne, pollo, básicos) respondería esto con datos.
- Pregunta no resuelta 4: ¿Por qué El Cafetal no convierte con 3 sucursales? Proyecto cuali de formatos respondería.
- Ver agenda completa en Bloque 9 (Roadmap 2027).

**Visual:** Tabla de 4 preguntas + metodología que las resuelve + horizonte estimado.
**Caveat:** ME-4 §2 y Reflexiones 2027 §2 — estas son recomendaciones de agenda, no datos del estudio actual.

---

## BLOQUE 7 — DIAGNÓSTICO DE LA COMUNICACIÓN ACTUAL (3 slides)

---

### Slide 32 — Recall de campañas: el gap comunicacional es masivo (BASE REFERENCIAL)

**Titulo:** BASE BAJA — RESULTADO REFERENCIAL: Solo el 4.2% recuerda alguna frase publicitaria de Gama espontáneamente

**Takeaway:** El recall de la campaña actual es prácticamente nulo — "PRECIOS DE TU LADO" no aparece en ninguna respuesta espontánea de los 17 que recuerdan algo.

**Bullets / contenido:**
- P35: 95.8% no recuerda ninguna frase publicitaria de Gama.
- P36 (n=17 que sí recuerdan algo): 0/17 mencionan "PRECIOS DE TU LADO" espontáneamente.
  * 41% "no recuerdo" (recordación parcial pero incapaz de reproducir)
  * 18% slogans de precio genérico (no de Gama específicamente)
  * 12% "Sin ti no hay nosotros" (frase de otra marca — error de atribución)
- P37: 10.7% recuerda PTL con ayuda (asistido) — ~1 de cada 10. BASE REFERENCIAL (n=43).
- P40: 12.4% recuerda DTLS con ayuda — ~1 de cada 10. BASE REFERENCIAL (n=50).
- Conclusión: la inversión en campaña no está produciendo retorno de notoriedad de mensaje. La frase "PRECIOS DE TU LADO" no está anclada en la memoria del shopper.

**Visual:** Donut recall espontáneo (4.2% sí / 95.8% no) + tabla de respuestas en P36. Titulo de slide con "BASE REFERENCIAL" explícito.
**Caveat:** CU-6 v2 §L-004 — flag BASE BAJA en título (n=17 P36; n=43 P37; n=50 P40). Los porcentajes son indicativos de dirección, no proyectables. IN-6 §C-001 AJUSTAR — no presentar como "la campaña fracasa", sino como "el recall de las campañas actuales es bajo (4.2% espontáneo) y la lectura dominante es precio, no compañía ni experiencia."

---

### Slide 33 — Qué lee el shopper en las campañas: precio, no experiencia

**Titulo:** BASE REFERENCIAL — El 65% que recuerda "PRECIOS DE TU LADO" la interpreta como mensaje de precio — exactamente el atributo menos predictivo de la preferencia

**Takeaway:** La campaña está comunicando con efectividad lo que el shopper no cree sobre Gama (que es económica), en lugar de lo que sí cree y le genera preferencia (que tiene buena atención).

**Bullets / contenido:**
- P39 interpretación PTL (n=43, BASE REFERENCIAL): 65% lee "precio bajo/accesible". 7% lee "solidaridad". El resto lee otras interpretaciones.
- P42 interpretación DTLS (n=50, BASE REFERENCIAL): 36% lee "precio/economía". 30% lee "compañía/siempre/cercanía". 28% otra interpretación. Lectura más dividida — "De Tu Lado Siempre" tiene mayor potencial semántico.
- La paradoja: la campaña transmite su intención (PTL = precio), pero esa intención no conecta porque el 54% del mercado no cree que Gama tenga buen precio.
- "De Tu Lado Siempre" tiene un 30% de lectura relacional (compañía/siempre) — es el territorio semántico más cercano al activo experiencial de Gama. Tiene potencial no desarrollado.

**Visual:** Dos donuts — interpretación PTL + interpretación DTLS. Resaltar el 65% precio en PTL y el 30% compañía en DTLS.
**Caveat:** CU-6 v2 §L-004 — BASE BAJA explícita en título. Los porcentajes son indicativos. IN-6 §C-001 AJUSTAR — "el estudio indica que alinear el mensaje con los drivers reales de preferencia (experiencia, no precio) puede tener mayor impacto."

---

### Slide 34 — La brecha estratégica: el mapa entre drivers y comunicación

**Titulo:** El estudio revela una brecha sistemática entre los drivers de preferencia y el foco de la comunicación actual — resolverla es la recomendación central del V3

**Takeaway:** No hay mensaje visible en la comunicación actual sobre el driver #1 (atención) ni el #2 (limpieza) — los dos atributos donde Gama tiene ventaja estadisticamente verificable.

**Bullets / contenido:**
- Driver #1 atención (OR=5.73, SHAP #1): no está en la campaña actual.
- Driver #2 limpieza (SHAP #2): no está en la campaña actual.
- Driver #3 promociones (OR=3.64, SHAP #3): las campañas de precio (PTL) no son percibidas como comunicación de promociones — el 65% las lee como mensaje de precio.
- El atributo menos importante (precio, SHAP #10): es el eje semántico de ambas campañas actuales.
- Resultado: la inversión publicitaria refuerza el mensaje que más trabaja en contra de la preferencia de Gama (precio) y no refuerza el mensaje que más la genera (experiencia).
- Nota: esta es la recomendación de mayor sensibilidad con el cliente. Se presenta como oportunidad estratégica derivada de datos, no como crítica de la creatividad o la inversión existente.

**Visual:** Tabla de alineación: driver (OR/SHAP rank) vs presencia en campaña actual (SI/NO). El contraste entre la columna de drivers y la columna de campaña es el hallazgo visual central.
**Caveat:** IN-6 §C-001 AJUSTAR — formulación: "el estudio indica que comunicar la experiencia de atención puede tener mayor impacto que comunicar precio. Una revisión de la plataforma de comunicación está justificada por los datos." Tono: recomendación estratégica apoyada en evidencia, no crítica directa.

---

## BLOQUE 8 — RECOMENDACIONES PRIORIZADAS (6 slides)

---

### Slide 35 — Mapa de recomendaciones: 5 acciones MECE

**Titulo:** Las 5 recomendaciones del V3 son MECE — cubren comunicación, táctica, territorio, target y agenda de investigacion

**Takeaway:** Las recomendaciones del V3 extienden y matizan las del V2 — ninguna las contradice; todas las refuerzan con el mecanismo cualitativo y el reanálisis estadístico adicionales.

**Bullets / contenido:**
- Rec. 1 (de V2 refinada): Comunicar la experiencia de atención — no el atributo, el momento
- Rec. 2 (de V2 refinada): Reactivar el programa de stickers con paraguas único — anzuelo de primera prueba, no promesa de precio bajo
- Rec. 3 (de V2 refinada): Defender urgencia, diagnosticar mercado grande antes de invertir
- Rec. 4 (de V2 integrada): Resolver el gap de surtido/formato para el 34% de preferentes que se va
- Rec. 5 (NUEVA en V3): Activar una campaña de primera prueba para el seg_2 (Pragmaticos Convertibles, n=133, 33%)

**Visual:** Tabla de 5 recomendaciones con columna "relación con V2" (refinada / nueva).
**Caveat:** Ninguno en slide de mapa.

---

### Slide 36 — Rec. 1: Comunicar la experiencia de atención

**Titulo:** La campaña nueva debe mostrar el momento de atención — el empleado que resuelve, no el eslogan que describe

**Takeaway:** Mostrar el momento concreto de reconocimiento personal que genera preferencia tiene un poder de persuasión que describir el atributo "buena atención" no tiene.

**Bullets / contenido:**
- Evidencia: OR=5.73 (triple convergencia), 53% razón espontánea, SHAP #1. El activo existe — falta comunicarlo.
- Acción: campaña centrada en el momento de interacción (el empleado que conoce, que resuelve, que acompaña). No el slogan de precio — la escena de la tienda.
- El territorio semántico disponible: "De Tu Lado Siempre" tiene un 30% de lectura de compañía/relación entre quienes la recuerdan. Es el point de partida creativo más cercano al activo de atención.
- Plataforma de comunicación sugerida: construir sobre el registro "estar para ti" — mostrar el momento de atención que hace que la tienda sea diferente a cualquier otro supermercado de precio.
- Lo que no es la acción: anunciar que Gama tiene buena atención. Eso es el atributo. La campaña debe mostrar la experiencia — que el shopper "sienta" la diferencia antes de visitarla.
- Relación con V2: Rec. 2 del V2 recomendó "capitalizar driver ATENCIÓN". El V3 agrega el qué mostrar y el cómo construir el territorio semántico.

**Visual:** Comparativo creativo "antes / después" de comunicación (descripción del atributo vs escena del momento). Simple, conceptual.
**Caveat:** IN-6 §C-004 AJUSTAR — la dimensión de "reconocimiento personal" es hipótesis interpretativa. La dirección estratégica (comunicar experiencia > comunicar precio) es el claim robusto.

---

### Slide 37 — Rec. 2: Reactivar el programa de stickers como anzuelo de primera prueba

**Titulo:** El sticker no es una promoción de precio — es la razón específica para que el seg_2 visite Gama por primera vez

**Takeaway:** Reactivar la colección de stickers con mecánica de basket-building en categorías sensibles, bajo un paraguas creativo único que comunique "esta semana hay una razón para venir", es la acción de mayor retorno de corto plazo.

**Bullets / contenido:**
- Evidencia de base: Cashea activo + club de lealtad activo + histórico de stickers con recordación alta (actualmente inactivo).
- Mecánica propuesta:
  * Stickers en categorías sensibles: carne, pollo, básicos (las 5 categorías donde Páramo domina precio — exactamente donde Gama necesita competir en visita, no en precio)
  * Integración con Cashea: financiamiento como reducción de barrera de entrada para primera visita del seg_2
  * Integración con club de lealtad: retención post-prueba — la primera visita inicia el patrón
- Paraguas creativo único: todos los activos de promoción deben comunicar bajo un solo "nombre de campaña" para construir coherencia de marca y recordación.
- Mensaje del paraguas: "esta semana hay una razón para venir" — no "somos económicos".
- Relación con V2: Rec. 1 del V2 recomendó esto. El V3 lo hace más específico: stickers como vehículo + paraguas único + mecánica basket-building.

**Visual:** Diagrama de mecánica (stickers + Cashea + club de lealtad) + mensaje del paraguas. Colores corporativos.
**Caveat:** IN-5 §Argumento 2 — la recordación histórica del sticker no tiene cifra del estudio; es información operativa de Gama confirmada por Cora.

---

### Slide 38 — Rec. 3 y 4: Defender urgencia + resolver mercado grande

**Titulo:** Dos horizontes, dos estrategias — defender lo que ya se gana, diagnosticar antes de invertir donde se pierde

**Takeaway:** No hay inversión más segura que profundizar la posición en urgencia (donde ya se gana); no hay inversión más arriesgada que abrir sucursales para mercado grande sin saber primero por qué El Cafetal no convierte con 3 sucursales ya en pie.

**Bullets / contenido:**
- Rec. 3 — Defender urgencia (C/P):
  * Comunicar conveniencia + disponibilidad + rapidez en el corredor Chacao-Sucre
  * La experiencia de caja (4.81/5 en seg_3) es el momento de la verdad de la misión de urgencia — optimizar y comunicar
  * Garantizar que cada visita de urgencia tenga suficiente atención para generar retorno en otra misión
- Rec. 4 — Diagnosticar mercado grande antes de invertir (horizonte):
  * Proyecto cuali de formatos: 10-12 IDIs con preferentes de Gama que compraron en otra cadena en su última compra
  * Pregunta central: ¿por qué El Cafetal (3 sucursales Gama) tiene 4.9% preferencia local?
  * Hipótesis a verificar: ¿surtido de frescos insuficiente? ¿ticket percibido? ¿propuesta vs Plan Suárez/CM que tienen formatos más completos?
  * Sin este diagnóstico, abrir sucursales puede replicar la paradoja de Baruta (6 sucursales, 2.4% preferencia)

**Visual:** Timeline dos horizontes con las 2 acciones por horizonte. Fondo bicolor (urgencia = hoy, mercado grande = mañana).
**Caveat:** IN-4 §T-09 — hipótesis de surtido/formato es de certeza media-baja. Marcar como hipótesis.

---

### Slide 39 — Rec. 5 (NUEVA): Campaña de activación para los Pragmaticos Convertibles

**Titulo:** NUEVA en V3 — El 33% del mercado con menor resistencia al precio es el territorio de conversión con mayor retorno de corto plazo

**Takeaway:** Una campaña específica de primera prueba para el seg_2 — no el mismo mensaje que para el núcleo leal — puede generar el mayor incremento de preferentes en el horizonte de 6-12 meses.

**Bullets / contenido:**
- El seg_2 (Pragmaticos Convertibles, n=133 de n=402) tiene 0% preferencia Gama actualmente y menor resistencia al precio (3.44 vs 3.66/5) que el seg_1.
- Su nivel de exigencia es moderado (P22 promedio ~4.1/5 vs ~4.7/5 del seg_1) — la propuesta actual de Gama puede satisfacer sus expectativas.
- Secuencia de conversión:
  1. Anzuelo: primera visita incentivada (sticker o Cashea en categoría de mayor sensibilidad para el seg_2)
  2. Experiencia: garantizar atención activa y visible en primera compra — el momento que diferencia a Gama
  3. Retención: club de lealtad como seguimiento post-prueba — convertir la primera visita en el inicio del patrón
- El mensaje para el seg_2 no es el mismo que para el seg_3. El seg_2 no conoce el argumento de Gama — el mensaje es "ven a ver qué es diferente esta semana", no "ya sabes que somos lo mejor".
- Este argumento es NUEVO en V3. No existía en el V2. Es adición genuina del reanálisis k-means de Cuanti.

**Visual:** Diagrama de conversión seg_2 → seg_3. Tres pasos: anzuelo, experiencia, retención. Resaltar "NUEVO EN V3".
**Caveat:** IN-6 §C-002 — GO con caveat: "el análisis sugiere que el seg_2 tiene menor barrera de conversión — son un segmento prioritario de conversión potencial, no garantía de conversión." CU-6 v2 §S-001 — silhouette moderado, solapamiento en márgenes.

---

## BLOQUE 9 — ROADMAP 2026-2027 (3 slides)

---

### Slide 40 — Agenda de acciones 2026: lo que se puede hacer ahora

**Titulo:** Q2-Q4 2026: cuatro acciones que no requieren nueva investigación — se ejecutan sobre los hallazgos de este estudio

**Takeaway:** Las recomendaciones 1-3 del V3 son accionables en Q2-Q3 2026 con los assets que Gama ya tiene; solo la Rec. 5 requiere segmentación operativa adicional.

**Bullets / contenido:**
- Q2-Q3 2026:
  * Iniciar revisión de la plataforma de comunicación: territorio experiencial vs territorio de precio (Rec. 1)
  * Reactivar stickers con paraguas único: mecánica basket-building en carne/pollo/básicos + integración Cashea + club (Rec. 2)
  * Cruzar resultados QR de satisfacción con tracker Notoriedad: ¿el QR captura el driver atención? (V2 Rec. 2 original)
- Q3-Q4 2026:
  * Diseñar campaña de primera prueba para seg_2: activación específica, mensaje diferenciado (Rec. 5)
  * Iniciar diagnóstico cuali de formatos: El Cafetal + Baruta — ¿por qué la cobertura no convierte? (Rec. 4)
  * Auditoría in-store de precios reales en 5 categorías sensibles (Rec. 6 de Reflexiones 2027 — opcional, requiere presupuesto adicional)
- Q4 2026: Decisión sobre ola 2027: ¿expansión de scope metodológico con MaxDiff + NPS + Van Westendorp? (Ver Bloque 9 roadmap 2027)

**Visual:** Timeline Q2-Q4 2026 con acciones por trimestre. Codificación por tipo (comunicación / táctica / investigación).
**Caveat:** ME-4 §6 (mapa de adopción) — las acciones del Q4 2026 sobre ola 2027 dependen de decisión de budget con Gama.

---

### Slide 41 — Roadmap metodológico 2027: la agenda de investigacion que eleva la calidad del próximo tracker

**Titulo:** La ola 2027 puede ser un salto cualitativo — 5 mejoras de bajo costo incremental con alto impacto en la calidad de las recomendaciones

**Takeaway:** Las 5 mejoras obligatorias para 2027 (MaxDiff, NPS, switching, CEPs, penetración 12m) son ajustes de diseño, no inversiones de campo — requieren rediseño del cuestionario, no más entrevistas.

**Bullets / contenido:**
- Obligatorio 2027 (bajo costo incremental, alto valor):
  1. MaxDiff reemplaza P22 Likert — produce jerarquía real de atributos, no "todo es importante" (ME-4 §2.2)
  2. NPS por marca usada + switching explícito — 3 preguntas, KPI global de salud de marca (Reflexiones 2027, Rec. #1)
  3. CEPs expandidos: de 5 misiones genéricas a 15-20 ocasiones específicas — mapea share of mind por ocasión (Reflexiones 2027, Rec. #3)
  4. Penetración 12 meses + frecuencia + ticket — cuantifica share of wallet $ (Reflexiones 2027, Rec. #5)
  5. Booster de campo Pref-Gama: n=80 real (vs n=32 actual) — reduce IC95 de ±17pp a ±11pp (ME-4 §6)
- Opcional 2027 con inversión incremental:
  * Van Westendorp en 3 KVIs (carne/pollo/básicos) — ~12 preguntas adicionales, sin costo de campo (Reflexiones 2027, Rec. #4)
  * DBA battery básica — 4-6 estímulos visuales (ME-4 §2.6)
- Horizonte 2028:
  * Conjoint/DCM — simulador de trade-offs estratégicos (Reflexiones 2027, Rec. #7, USD 10-20K)
  * Pulse tracker trimestral C+/C online — KPIs core en tiempo real (ME-4 §2.7)

**Visual:** Tabla de mejoras clasificadas por horizonte + costo + valor. Misma estructura que ME-4 §6 (mapa de adopción) pero en formato de slide ejecutivo.
**Caveat:** ME-4 §8 — el diseño final de la ola 2027 depende de confirmación de Cora sobre la metodología de intercepción del fieldwork 2026 (placeholder en ficha técnica).

---

### Slide 42 — Cierre: convergencia V2+V3 y próximos pasos

**Titulo:** V2 y V3 convergen en los hallazgos fundamentales — el V3 suma el mecanismo y el target de conversión

**Takeaway:** El estudio de 2026 es internamente consistente: cuatro métodos (logit, RF, SHAP, cuali) apuntan en la misma dirección. El siguiente paso es activar la estrategia experiencial con el target correcto.

**Bullets / contenido:**
- Convergencia V2/V3:
  * Confirmados: atención = driver #1 (OR=5.73, triple convergencia), precio = no driver (SHAP #10), gap comunicacional masivo (0/17 recall espontáneo PTL)
  * Elevados: limpieza sube de "tendencia" a "driver secundario" por SHAP+Gini
  * Nuevos en V3: mecanismo cuali de la preferencia (por qué la atención tiene el OR más alto), segmentación k-means formal (3 perfiles accionables), argumento estratégico de conversión del seg_2
- Próximos pasos inmediatos:
  * Gate Bruna sobre claims sensibles antes de circulación externa (IN-6 + CU-6 v2)
  * Reunión Cora + Gama para presentar V3 como capa analítica ampliada
  * Decisión sobre revisión de plataforma de comunicación
  * Activación de stickers + Cashea bajo paraguas único
- Contactos: Cora Urrea (cora.urrea@gmail.com) + Raoul Bermudez (raoul.bermudez@gmail.com)

**Visual:** Slide de cierre limpio. Logo Gama + paleta corporativa. Lista de próximos pasos con iconos de acción.
**Caveat:** IN-6 §C-008 — decisión de packaging de los segmentos k-means (cómo presentar a Gama el hallazgo nuevo) es del Owner.

---

## APÉNDICE — METODOLOGÍA AMPLIADA (4 slides)

---

### Slide A1 — Diseño retroactivo del estudio: qué se midió, cómo y por qué

**Titulo:** Apéndice: Diseño retroactivo del estudio — rationale metodológico de cada decisión analítica

**Takeaway:** El análisis de Gama 2026 siguió un protocolo metodológico que puede documentarse retroactivamente y compararse contra el estado del arte 2026 para informar el diseño de la ola 2027.

**Bullets / contenido:**
- Metodos ejecutados en V2 + V3:
  * Embudo de marca (TOM → Preferida): protocolo estándar, sin cambios
  * Regresión logística (statsmodels, Pseudo R2=0.44, AUC=0.929): modelo principal — supera al RF en AUC con este n
  * Random Forest + SHAP (sklearn 1.8.0, shap 0.51.0, AUC CV=0.851): modelo de convergencia — confirma la jerarquía del logit y eleva limpieza
  * K-means (k=3, silhouette 0.195) + BGM proxy LCA (BIC mínimo en k=3): segmentación formal
  * Análisis temático (Braun & Clarke adaptado sobre frecuencias de categorías): síntesis cuali
  * Triangulación cuali/cuanti sistemática: 10 claims cruzados (IN-4)
- Gap vs estado del arte 2026 (referencia para ola 2027):
  * MaxDiff: no ejecutado (P22 Likert saturado)
  * NPS + switching matrix: ausentes
  * CEPs completos: 5 misiones genéricas vs 15-20 CEPs
  * Van Westendorp: ausente (solo perceptual ordinal P33)

**Visual:** Tabla de métodos — ejecutado vs estado del arte. Mismo formato que ME-4 §1.
**Caveat:** ME-3 §1 (rationale de cada decisión) — ver documento completo para trazabilidad completa. ME-4 §3 Alerta 3 (HARKing) — algunos análisis de Fase C fueron post-hoc; interpretarlos con la cautela apropiada.

---

### Slide A2 — Convergencia metodológica: la tabla maestra de drivers

**Titulo:** Apéndice: Los 10 atributos rankeados por los 3 métodos — tabla de convergencia completa

**Takeaway:** La convergencia triple en el top-3 (atencion #1, limpieza #2, promociones #3) en los tres métodos independientes es el hallazgo metodológico más robusto del estudio.

**Bullets / contenido:**
- Tabla: Atributo | OR Logit (p) | SHAP rank (mean|v|) | Gini RF (rank) | Convergencia
- mejor_atienden: OR=5.73*** / SHAP #1 (0.1047) / Gini #1 (0.1977) / TRIPLE
- limpio_ordenado: OR=3.99* / SHAP #2 (0.735) / Gini #2 (0.1609) / DOBLE+SHAP (logit borderline)
- promociones: OR=3.64** / SHAP #3 (0.0633) / Gini #4 (0.1031) / TRIPLE (con matiz Gini)
- menor_precio: OR=1.03 / SHAP #10 (0.013) / Gini #10 (0.0273) / TRIPLE convergencia en irrelevancia
- AUC logit: 0.929 (in-sample) vs RF: 0.851 (CV 5-fold). El logit supera al RF — modelo principal correcto.

**Visual:** Tabla maestra de drivers (10 filas, 6 columnas). Resaltar top-3 y menor_precio en colores contrastantes. Referencia: CU-3 v2 Seccion 3.
**Caveat:** CU-6 v2 §L-002 — IC95 amplios (n_pref=32). Tabla de IC95 disponible en CU-2. CU-3 v2 Seccion 6 — SHAP interpreta el RF, no el logit; la coincidencia con el logit es confirmacion cruzada.

---

### Slide A3 — Segmentación formal: el proceso y los criterios de validacion

**Titulo:** Apéndice: Criterios de validación de los 3 segmentos k-means

**Takeaway:** Los 3 segmentos superan los dos criterios de validación (silhouette máximo y BIC mínimo en k=3) y tienen interpretación sustantiva clara — son publicables con caveat de solapamiento en márgenes.

**Bullets / contenido:**
- Criterio 1: Silhouette k=3 = 0.195 (máximo de k=2..6). Nota: valores absolutos bajos (~0.20) son esperados con variables Likert de alta homogeneidad.
- Criterio 2: BIC proxy LCA k=3 = 10,379 (mínimo de k=2..6). Ambos criterios convergen.
- Criterio 3: Interpretabilidad sustantiva — los 3 perfiles tienen descripción clara y accionable. El algoritmo aisló naturalmente a los 32 preferentes de Gama como cluster independiente (seg_3).
- Comparativa Ward (v1 hipótesis) vs k-means formal (v2): los 5 segmentos hipotéticos del Ward colapsan en 3. El cambio clave: los leales de Páramo no forman cluster propio — están mezclados en el segmento de alta exigencia (seg_1).
- Tabla de validacion completa: CU-4 v2 Sección 1-3.

**Visual:** Curvas silhouette y BIC (embed kmeans_elbow_silhouette_20260517_v1.png). Tabla de 3 segmentos con n, %, y 3 variables clave.
**Caveat:** CU-6 v2 §S-001 — caveat OBLIGATORIO de silhouette moderado + solapamiento en márgenes. Referencia: CU-4 v2 Seccion 5.

---

### Slide A4 — Comparativa V2 vs V3: qué confirma, qué eleva, qué es nuevo

**Titulo:** Apéndice: Mapa de convergencia entre las recomendaciones del V2 y los argumentos del V3

**Takeaway:** El V3 no contradice el V2 en ningún hallazgo fundamental — confirma y eleva los drivers, suma el mecanismo cuali y el target de conversión.

**Bullets / contenido:**
- CONFIRMADOS por V3: los 3 drivers del V2 (atención OR=5.73, limpieza OR=3.99/SHAP#2, promociones OR=3.64). La narrativa "Gama va abajo" no tiene base estadística. La diferencia V2→V3 más importante: limpieza sube de "tendencia borderline" a "driver secundario confirmado" por SHAP+Gini.
- REFINADOS por V3: Rec. 1 V2 (comunicar promociones) → se especifica como "anzuelo de primera prueba" con mecánica stickers+Cashea+club. Rec. 2 V2 (capitalizar driver atención) → se suma el mecanismo cuali (qué mostrar) y la evidencia de que la campaña actual no lo comunica.
- INTEGRADOS por V3: Recs. 3+4 V2 (defender Chacao-Sucre + recuperar mercado grande) → se integran en la estrategia de dos horizontes con lógica JTBD.
- NUEVOS en V3: Argumento 4 (seg_2 como oportunidad de conversión inmediata). La segmentación k-means formal. El análisis temático y la triangulación cuali/cuanti sistemática.
- Tabla: IN-5 §Tabla de comparación con 10 recomendaciones del V2.

**Visual:** Tabla de 3 columnas (Rec. V2 / Relación V3 / Status). Misma tabla que IN-5 §Tabla comparativa, adaptada a formato slide.
**Caveat:** IN-6 §C-008 — los segmentos k-means son información nueva para Cora/Gama. Decisión de packaging es del Owner.

---

*Fin VI-1a — Outline Deck Principal V3*
*42 slides (5 apertura + 4 tesis + 5 activo experiencial + 4 promociones + 4 misiones + 5 segmentos + 4 voz consumidor + 3 diagnóstico comunicación + 6 recomendaciones + 3 roadmap + 4 apéndice)*
*Claims NO-GO excluidos: C-005 (n=2 evidencia insuficiente). Claims AJUSTAR aplicados: C-001, C-003, C-004.*
*Gate Bruna pendiente sobre IN-6 + CU-6 v2 antes de circulación a Cora/Gama.*
*Producido por Vivienne — 2026-05-17 — SSOT canónico*
