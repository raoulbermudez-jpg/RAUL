# Bruna — Templates & Special Protocols

> Templates, casos típicos y protocolos especiales del agente
> `bruna` (companion document). **Load on-demand:** cargar
> explícitamente solo cuando la tarea actual requiera aplicar un
> patrón canónico documentado aquí.
>
> Documento companion del conceptual SSOT principal en
> `04-system/02-agents/conceptual/bruna.md` (§1-§10). El conceptual
> principal lleva pointer a este archivo en §11.

---

## 11. Tareas tÃ­picas / Templates & Special Protocols


### 11.1 Tareas tÃ­picas (referencia para inducciÃ³n)

1. **Gate de campaÃ±a nueva sobre VA-5 + OL-5:** Vael entrega VA-5 con
   claims candidatos categorizados âœ… / âš  / âŒ, sustentados explÃ­citamente
   en RTBs (specs de Vera y OL-5 de Orlan). Bruna revisa cada claim âš  y
   âŒ: para los âš  confirma o ajusta el caveat propuesto; para los âŒ
   confirma rechazo o propone alternativa aceptable. Sobre los âœ…
   realiza spot-check de consistencia contra RTBs. Bruna produce **BR-1
   Claim Risk Assessment Note** y actualiza **BR-2 Claim Approval /
   Rejection Log del dominio** con las decisiones. VA-5 cerrado y
   gateado pasa a Solenne para ejecuciÃ³n.

2. **RevisiÃ³n de claims vigentes tras cambio de spec o de mercado:**
   Vera publica spec actualizada que modifica un threshold relevante, o
   Orlan publica OL-3 donde un atributo pasa de âœ… Diferenciado a âš–
   Paridad. Bruna, apoyada en Sira, localiza piezas vigentes (sitio
   web, empaques, decks, redes) con claims afectados, evalÃºa quÃ© claims
   ya no sostienen la evidencia actual y produce **BR-4 Remediation
   Plan** con lista de claims y piezas, acciÃ³n requerida (retirar /
   corregir / aclarar), prioridad y plazo.

3. **DecisiÃ³n sobre claim comparativo directo vs marca global:** Vael
   propone en VA-3 un claim explÃ­citamente comparativo ("respuesta mÃ¡s
   rÃ¡pida que [competidor]" o "Ãºnica protecciÃ³n con [feature] en el
   mercado venezolano"). Bruna evalÃºa la exposiciÃ³n legal y reputacional
   (uso de marca de tercero, normativa sobre publicidad comparativa,
   exigencias de "Ãºnico"), consulta evidencia disponible (OL-X y specs)
   y aplica la clÃ¡usula pertinente de `RISK-POLICY.md`, ademÃ¡s de
   consultar precedentes en **BR-5 Precedents & Guidelines Memo
   transversal**. Bruna decide: aprueba / aprueba con caveat (acotando
   contexto o fuente de verificaciÃ³n) / rechaza con propuesta de claim
   alternativo no comparativo. Las decisiones quedan registradas en
   **BR-1**, **BR-2 del dominio** y en una nueva entrada de **BR-5**.

4. **AplicaciÃ³n de polÃ­tica a un caso concreto (superlativos,
   garantÃ­as, etc.):** Solenne consulta sobre uso de un superlativo
   ("el mÃ¡s confiable") en un blog B2B. Bruna interpreta cÃ³mo aplicar
   la secciÃ³n relevante de `RISK-POLICY.md` sobre afirmaciones
   absolutas al caso especÃ­fico: bajo quÃ© condiciones se permite el
   superlativo, quÃ© evidencia mÃ­nima requiere, quÃ© formularios de
   caveat lo harÃ­an defendible y cuÃ¡ndo debe evitarse. El resultado se
   documenta como **BR-3 Risk Policy Application Note**, que sienta
   criterio para futuros casos similares y se referencia en **BR-5
   transversal** como precedente.

5. **Protocolo de incidente (claim publicado con riesgo ex-post):** un
   claim ya publicado genera reclamo de cliente, comentario crÃ­tico
   pÃºblico o cuestionamiento tÃ©cnico validable. Bruna activa protocolo
   rÃ¡pido de incidente: evalÃºa exposiciÃ³n (tÃ©cnica, reputacional,
   regulatoria), revisa facts con Vera / Orlan si es necesario, decide
   acciÃ³n sobre el claim (mantener, aclarar, corregir, retirar) y
   elabora **BR-4 Remediation Plan acelerado** con responsables y
   tiempos. Cuando la gravedad lo justifica, Bruna escala al Owner
   para decisiones estratÃ©gicas (comunicados pÃºblicos, relaciÃ³n con
   agencias o distribuidores). El caso y su resoluciÃ³n se documentan
   en **BR-5 transversal** como precedente fuerte.

### 11.2 Workflow Vael â†’ Bruna â†’ Solenne / Ivo (cadena gate)

1. Vael produce VA-5 (Messaging Guardrails) con claims candidatos
   categorizados âœ… / âš  / âŒ.
2. Vael escala VA-5 a Bruna vÃ­a Raul para gate previo.
3. Bruna consulta evidencia + RISK-POLICY + BR-5 transversal; produce
   BR-1 (Assessment) en `03-projects/<dominio>/<proyecto>/03-review-and-release/`.
4. Bruna decide cada claim sensible: aprueba / aprueba con caveat /
   rechaza con alternativa / pide refresh.
5. Bruna documenta en BR-2 del dominio
   (`03-projects/<dominio>/_governance/`); sienta precedente en BR-5
   transversal (`04-system/03-governance/`) si aplica; formaliza
   interpretaciÃ³n en BR-3 si la clÃ¡usula necesita aclaraciÃ³n.
6. Vael recibe sello + caveats / alternativas; cierra VA-1 / VA-3 /
   VA-4 con claims aprobados.
7. Solenne ejecuta copy con caveats literales integrados.
8. Ivo verifica sello de Bruna antes de distribuir.
9. Sira archiva linaje: VA-X â†’ BR-2 â†’ pieza publicada.

### 11.3 Workflow revisiÃ³n retrospectiva (cambio aguas arriba)

1. Trigger: Vera spec update / Orlan OL-3 reclasificaciÃ³n /
   RISK-POLICY change.
2. Bruna revisa BR-2 del dominio vigente para identificar claims
   potencialmente afectados.
3. Sira localiza piezas vigentes que usaron esos claims.
4. Bruna re-evalÃºa cada claim contra evidencia nueva.
5. Bruna produce BR-4 (Remediation Plan) con piezas, acciones,
   responsables, prioridad, plazo.
6. Solenne / Oz / Ivo ejecutan segÃºn remediaciÃ³n.
7. Bruna actualiza BR-2 del dominio con cambios de estado y BR-5
   transversal si el caso sienta precedente nuevo.
8. Si la correcciÃ³n requiere comunicaciÃ³n pÃºblica: escalar a Owner.

### 11.4 Workflow protocolo de incidente (claim ex-post)

1. Trigger: reclamo cliente / comentario crÃ­tico pÃºblico /
   cuestionamiento tÃ©cnico verificable.
2. Triage rÃ¡pido (24h cuando es pÃºblico): evaluar exposiciÃ³n
   tÃ©cnica / reputacional / regulatoria.
3. Verificar facts con Vera / Orlan si el cuestionamiento tiene base.
4. Decidir acciÃ³n: mantener / aclarar / corregir / retirar.
5. Producir BR-4 acelerado con responsables y tiempos comprimidos.
6. Escalar a Owner si la decisiÃ³n es estratÃ©gica.
7. Documentar en BR-5 transversal como precedente fuerte.

### 11.5 CatÃ¡logo inicial de tipos de claim (semilla de BR-5 transversal)

Estructura inicial sugerida para BR-5 transversal al arrancar:

- **Comparativos directos** (vs marca tercero nombrada).
- **Comparativos indirectos** ("vs el promedio del mercado", "vs
  alternativas").
- **Superlativos absolutos** ("el mÃ¡s", "Ãºnico", "primero").
- **Afirmaciones temporales** ("siempre", "nunca", "100%",
  "garantizado").
- **Claims sobre garantÃ­as** (cobertura, plazos, condiciones).
- **Claims regulatorios** (CE / UL / IEC, certificaciones nuestras).
- **Claims sobre certificaciones de competidores** (mencionar /
  comparar con cumplimiento ajeno).
- **Claims de origen / made-in / industria nacional**.

Cada tipo se va poblando con precedentes a medida que aparecen casos.