# Vael — Templates & Special Protocols

> Templates, casos típicos y protocolos especiales del agente
> `vael` (companion document). **Load on-demand:** cargar
> explícitamente solo cuando la tarea actual requiera aplicar un
> patrón canónico documentado aquí.
>
> Documento companion del conceptual SSOT principal en
> `04-system/02-agents/conceptual/vael.md` (§1-§10). El conceptual
> principal lleva pointer a este archivo en §11.

---

## 11. Tareas tÃ­picas / Templates & Special Protocols


### 11.1 Tareas tÃ­picas (referencia para inducciÃ³n)

1. **Framework de mensajes para lanzamiento de un nuevo protector
   Genteca:** el Owner anuncia un lanzamiento. Vael toma OL-2 (comparison
   table) y OL-5 (claim feasibility) de Orlan + spec sheet validado de
   Vera + brand wiki Genteca, y produce VA-1 (Messaging Framework) + VA-2
   (Positioning Statement Pack) + VA-4 (Content Brief para CSC). VA-5
   (Guardrails) se construye en paralelo y pasa por gate de Bruna antes
   de cerrar el set. Solenne y la cadena ejecutan; Bruna gatea claims
   sensibles antes de publicaciÃ³n.

2. **RedefiniciÃ³n de posicionamiento de familia existente tras hallazgo
   competitivo:** Orlan entrega OL-3 (Differentiation Memo) que muestra
   que una familia Genteca ya no es tan diferenciada como se creÃ­a. Vael
   produce VA-2 actualizado + VA-1 con pilares ajustados, identifica quÃ©
   claims previos hay que retirar (VA-5 con categorÃ­a âŒ explÃ­cita para
   los claims obsoletos) y prepara VA-4 con instrucciones para Solenne
   sobre cÃ³mo migrar la narrativa sin romper continuidad de marca. El
   Owner aprueba el cambio de pilares antes de pasar a producciÃ³n.

3. **Message map de campaÃ±a B2B por segmento:** el Owner pide campaÃ±a
   para OEMs de bombas industriales. Vael toma OL-1 (Landscape Brief
   Orlan) + insumos tÃ©cnicos de Vera + brand wiki, y produce VA-3
   (Campaign Message Map) con mensajes por etapa de funnel (awareness /
   consideration / decision) y por audiencia (compras, ingenierÃ­a,
   mantenimiento). VA-4 acompaÃ±a con brief para que Solenne escriba las
   piezas correspondientes. Aurelio integra VA-1 + VA-3 + VA-4 al plan
   CSC multi-formato.

4. **Translation de innovaciÃ³n tÃ©cnica a narrativas comprensibles:**
   Vera valida una nueva curva de protecciÃ³n o feature HMI. Vael toma la
   spec validada y produce VA-1 con tres niveles de narrativa: tÃ©cnica
   (para ingenierÃ­a), funcional (para mantenimiento), de valor (para
   compras). Cada nivel preserva la verdad tÃ©cnica de Vera; solo cambia
   el Ã©nfasis y el lenguaje. Bruna gatea claims comparativos si la
   innovaciÃ³n se posiciona contra competencia.

5. **Refresh trimestral de Guardrails (VA-5) post-Innovation Radar de
   Orlan:** cuando Orlan publica OL-4 trimestral, Vael revisa VA-5
   vigente para detectar claims que dejaron de ser defendibles (porque
   un competidor igualÃ³ la feature, porque una certificaciÃ³n cambiÃ³ de
   estado, porque un OL-3 reclasificÃ³ un atributo). Produce VA-5
   actualizado + nota a Solenne sobre claims a retirar de piezas en
   producciÃ³n + escalaciÃ³n a Bruna si hay claim publicado que ya no
   sostiene gate.

### 11.2 Workflow Vera + Orlan â†’ Vael â†’ Solenne / Aurelio / Nerea (cadena de mensaje)

1. Vera entrega spec validada + brief tÃ©cnico (verdad tÃ©cnica).
2. Orlan entrega OL-1 a OL-5 segÃºn corresponda (verdad de mercado).
3. Vael consume ambos + brand wiki + brief estratÃ©gico del Owner.
4. Vael produce VA-1 (framework) + VA-5 (guardrails) en paralelo.
5. VA-5 pasa por gate de Bruna **antes** de cerrar VA-1 / VA-3 / VA-4.
6. Vael produce VA-2 (positioning) + VA-3 (message map) + VA-4 (content
   brief CSC) sobre la base aprobada.
7. Aurelio integra VA-1 + VA-4 al plan CSC multi-formato (si aplica).
8. Solenne / Nerea / Atlas / Luma / Vela ejecutan segÃºn VA-4.
9. Bruna gatea outputs pÃºblicos finales antes de Ivo.
10. Sira mantiene referencia cruzada al framework como linaje del output
    publicado.

### 11.3 Workflow Vael â†’ Bruna (gate de claims)

1. Vael identifica claims candidatos en VA-5 categorizados âœ… / âš  / âŒ.
2. Para cada âš  o âŒ: Vael escala a Bruna vÃ­a Raul con: claim propuesto,
   RTB disponible, riesgo identificado, alternativa sugerida.
3. Bruna gatea: aprueba con caveat / rechaza / pide refresh de evidencia
   a Orlan o Vera.
4. Vael ajusta VA-1 / VA-3 / VA-4 con la decisiÃ³n de Bruna.
5. Sin gate explÃ­cito de Bruna, los claims sensibles **no pasan a
   ejecuciÃ³n**.

### 11.4 Workflow refresh de framework (cuando insumos aguas arriba cambian)

1. Trigger: Vera actualiza spec / Orlan publica OL-3 nuevo / Bruna
   cambia polÃ­tica de claims / Owner ajusta pilares.
2. Vael recibe el cambio y revisa quÃ© VA-X vigentes se invalidan
   (consultando "Supuestos y lÃ­mites" Â§7.2 de cada uno).
3. Para cada VA-X afectado: producir versiÃ³n nueva con `_vN+1`,
   referenciando el cambio aguas arriba como trigger.
4. Notificar a Solenne / Aurelio / agentes en ejecuciÃ³n: piezas en
   producciÃ³n que deben ajustarse, claims a retirar.
5. Si la pieza ya estÃ¡ publicada y el claim ya no sostiene gate de
   Bruna: escalar a Bruna + Ivo para evaluar retirada / correcciÃ³n.