# Owner Decision — Escalaciones BR-2 (E-1, E-2, E-3)

**Proyecto:** consultoria-externa / gama-notoriedad-2026
**Documento gateado:** Deck V3 Gama Notoriedad 2026 + Resumen Ejecutivo V3
**Fecha de decisión:** 2026-05-17
**Owner:** Raoul Bermúdez
**Insumo:** `_governance/2026-05-17_BR-2_gate-V3-deck_v1.md` (Bruna, sección "ESCALACIONES AL OWNER", líneas 117-135)
**Contexto adicional:** Cora dejó archivos nuevos en `01_De_Cora_Para_Raoul/Notoriedad V2.0/` (BBDD idéntico al original + guía con preguntas marcadas wave-over-wave 2025↔2026). Owner confirmó tratamiento de las 3 escalaciones como independiente de esa nueva ola.

---

## Resumen de decisiones

| Escalación | Tema | Decisión Owner | Acción derivada |
|---|---|---|---|
| **E-1** | Segunda sesión Sinta con BBDD raw | **NO ahora — GO condicional si se confirma presentación presencial a Gama** | Stand-by. Re-evaluar cuando Cora confirme si Gama pidió presencial. |
| **E-2** | Cómo presentar 3 segmentos k-means a Gama | **(a) Proactivo — framing de evolución metodológica, no omisión** | Owner aprueba párrafo redactado abajo. Pasarlo a Cora cuando aplique. |
| **E-3** | Lenguaje para Cora si Gama compara V2 vs V3 sobre "limpieza" | **Aprueba frase propuesta literal** | Incorporar a la nota interna para Cora cuando se cierre la fase actual. |

---

## E-1 — Decisión detallada

**Decisión:** NO ahora; GO condicional si Cora confirma que habrá presentación presencial a Gama en la cual ella defienda el deck oralmente.

**Rationale:**
1. Cora todavía no ha confirmado modalidad de presentación a Gama (entrega de deck vs presencial).
2. La nueva ola wave-over-wave 2025↔2026 puede redefinir scope y orden de prioridades — meter una pasada de Sinta ahora arriesga re-trabajo si la nueva fase la invalida.
3. El claim C-004 ya está integrado en el deck como **hipótesis** (ajuste obligatorio #5 de Bruna ya aplicado en slide 12) — el deck es honesto sin la pasada adicional.

**Trigger para activar GO:**
- Cora confirma presentación presencial agendada con Gama.
- En ese caso: arrancar segunda sesión Sinta con acceso controlado a BBDD raw (respetando NDA) **antes** de la fecha presencial, no antes.

**Si nunca se activa el trigger:** la decisión NO se mantiene permanente — el deck V3 ya es entregable defendible.

---

## E-2 — Decisión detallada

**Decisión:** Opción (a) — presentar segmentos proactivamente con framing de evolución metodológica.

**Rationale:**
1. Los 3 segmentos son el contenido más accionable del V3 (especialmente seg_2 Pragmáticos Convertibles como target de conversión de corto plazo).
2. Reservarlos como info de backup arriesga interpretación defensiva ("¿por qué se escondieron?").
3. El framing de "evolución metodológica → mismo dato, lente más fina" cierra la pregunta antes de que se haga.
4. Le da a Cora la línea editorial para liderar la conversación, no esperarla.

**Párrafo aprobado para Cora (puede leerlo literal o parafrasear ajustando a su voz):**

> *"Una nota antes de entrar al bloque de segmentación: este análisis no estaba en el V2 — lo construimos en el V3, una capa que sumamos esta semana cuando se amplió el equipo de análisis con una corrida formal de k-means. Mismo dataset, lente analítica más fina. Identificamos 3 grupos: una Mayoría Exigente que es el 59% del mercado, un grupo de Pragmáticos Convertibles del 33% que vale la pena destacar — son los que están a menor distancia de elegir Gama si se les baja la barrera de prueba — y un Núcleo Leal del 8%. El segundo grupo es probablemente el de mayor retorno de corto plazo para una campaña de primera prueba."*

**Cuándo usarlo:** abrir el bloque de segmentación cuando Cora presente el V3 a Gama (presencial o asincrónico con nota acompañante).

**Cuándo NO usarlo:** si Gama recibe solo el Resumen Ejecutivo V3 sin presentación y sin discusión — el RE ya tiene su propio framing.

---

## E-3 — Decisión detallada

**Decisión:** Aprueba frase propuesta literal.

**Frase aprobada para Cora (oral o por escrito si Gama compara V2 vs V3 sobre "limpieza"):**

> *"En el V2 reportamos limpieza como tendencia estadística — alcanzaba significancia borderline en el modelo principal (logit, p=0.061). En el V3 ampliamos con dos métodos adicionales — Random Forest con SHAP y Gini — que la ponen en el segundo lugar de importancia, con margen claro. Los datos son los mismos; la lente analítica es más completa. La recomendación no cambia: limpieza es palanca prioritaria. Lo que el V3 añade es certeza."*

**Cuándo usarla:** solo si Gama pregunta o si Cora detecta confusión por la comparación V2/V3 sobre este punto específico. No proactiva — agregarla solo si surge.

---

## Trazabilidad

Esta decisión NO modifica el deck V3 entregado (ya cumple Bruna BR-2 con los 5 ajustes obligatorios aplicados). Lo que añade son **3 líneas operativas para Cora**:

1. (E-1) Mensaje pendiente a Cora cuando confirme modalidad: "si Gama pidió presencial, te aviso, podemos hacer una pasada adicional de codificación cualitativa antes."
2. (E-2) Párrafo aprobado para que Cora abra el bloque de segmentación.
3. (E-3) Frase de respuesta lista si Gama pregunta sobre el cambio de lenguaje en "limpieza".

Los puntos 2 y 3 se consolidan en una nota interna corta para Cora cuando se cierre la fase actual (post-respuesta de Cora sobre la nueva ola wave-over-wave). El punto 1 queda como condición observable, no acción inmediata.

---

## Estado de las 3 líneas operativas

| ID | Trigger | Acción cuando dispara |
|---|---|---|
| E-1 | Cora confirma presentación presencial a Gama | Arrancar segunda sesión Sinta con acceso BBDD raw |
| E-2 | Cora presenta V3 a Gama (en cualquier modalidad con discusión) | Pasarle el párrafo aprobado para abrir bloque de segmentos |
| E-3 | Gama pregunta sobre "limpieza" comparando V2 vs V3 | Cora usa frase aprobada |

---

*Owner Decision — 2026-05-17 — v1*
*Dominio: consultoria-externa / proyecto: gama-notoriedad-2026*
*Responde a: `_governance/2026-05-17_BR-2_gate-V3-deck_v1.md` (Bruna)*
*Las 3 escalaciones quedan resueltas. E-1 es condicional (trigger observable); E-2 y E-3 tienen artefactos listos para entregar a Cora cuando aplique.*
