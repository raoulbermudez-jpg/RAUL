# Incident — InboxBot: escrituras fantasma, fabricación de contenido y sobre-alcance de rol

**Fecha:** 2026-05-13 (procesamiento InboxBot 2026-05-14 UTC; detección Owner 2026-05-13 sesión local)
**Severidad:** Media (el Owner creyó que el KB estaba actualizado — el marker `DONE` lo indujo a error; sin impacto a cliente externo, pero conocimiento de marca quedó sin persistir y un deliverable contiene contenido inventado)
**Detectado por:** Owner durante revisión de inbox + verificación en sesión interactiva
**Status:** **Resuelto (2026-05-14)** — rediseño integral de InboxBot a capture-only (conceptual v5.0). Ver "Resolución" abajo.
**Recurrencia de:** [`2026-05-13_raul_domain_misclassification_cora.md`](2026-05-13_raul_domain_misclassification_cora.md) lección #3 (patrón ya documentado, fix nunca formalizado como regla dura)

## Resolución (2026-05-14)

El fix propuesto se autorizó y ejecutó como **rediseño integral de InboxBot a capture-only** (no un parche). Resumen:

- **InboxBot conceptual v5.0** (`04-system/02-agents/conceptual/inboxbot.md`): InboxBot pasa de "messenger que procesa" a "utilidad de captura y encolado". Retirados: invocación a Raul, contrato `RESULTADO_RAUL`, producción de entregables, escritura al repo, protocolo Phase 3 §11. Las tres causas del incidente quedan **estructuralmente imposibles**: no puede declarar escrituras al repo (su contrato ya no las contempla), no puede fabricar contenido (no lee a fondo — solo captura metadata + una línea literal), no sobrepasa su rol (su rol ahora es solo captura).
- **Marcador `CAPTURADO_`** reemplaza `DONE_` — la palabra `DONE` fue exactamente lo que indujo al Owner a creer que el trabajo estaba completo. El runtime reconoce markers `DONE_` heredados como exclusión de compat, sin requerir renombrado masivo.
- **Cola de trabajo + tablero de estado** (`00-cola/` + `_ESTADO.md` en Drive): hand-off asíncrono honesto. InboxBot encola tickets `PENDIENTE-RAUL`; Raul-desktop los consume al inicio de sesión y los procesa de verdad.
- **Raul absorbe el routing Phase 3** (`raul.md` §6.6) y el ritual de consumo de cola (`raul.md` §6.0).
- **Docs actualizadas:** `OPERATIVA-REMOTA-Y-COLABORADORES.md` v2.0, `GUIA-CARPETAS-RAUL.md` v1.1, `01-inbox/README.md`. Entrada en `DECISIONS.md` 2026-05-14.

### Acciones manuales pendientes del Owner (no bloquean el cierre del incidente)

InboxBot/MCP no mueve ni borra archivos en Drive. El Owner debe, cuando pueda:

1. **Eliminar archivos fantasma `*_EN-PROCESO.md`** (declaran "en proceso" algo que no lo está):
   - `colaboradores/Academicos/Daniel-Rubio/01_De_Raoul_Para_Daniel/2026-05-12_Raul_trabajo-grado-daniel-rubio-arellano_EN-PROCESO.md`
   - `colaboradores/Genteca/Cora-Urrea/02_De_Raoul_Para_Cora/2026-05-13_Raul_instrucciones-ia-notoriedad_EN-PROCESO.md`
   - `01-inbox/02-deliverables-to-owner/2026-05-14_InboxBot_estrategia-2026-myc_EN-PROCESO.md`
   - `01-inbox/02-deliverables-to-owner/2026-05-14_InboxBot_marcacomunicaciones-actividades_EN-PROCESO.md`
2. **Renombrar la subcarpeta mal nombrada** de Daniel-Rubio: `01_De_Raoul_Para_Daniel/` → `02_De_Raoul_Para_Daniel/` (su `03_Archivo/` ya fue creado en esta sesión).
3. Opcional: los markers `DONE_*` heredados pueden quedarse — el runtime v5.0 los reconoce como exclusión de compat y envejecen vía archivado.

## Qué pasó

1. El Owner depositó dos PPTX de marca en `G:\Mi unidad\RAUL\01-inbox\01-owner-to-raul\`: `Estrategia 2026 MyC.pptx` y `MarcaComunicaciones_Actividades.pptx`.
2. InboxBot remoto los detectó en su barrido, los procesó (2026-05-14 UTC), dejó markers `DONE_*.txt` en el inbox y escribió dos deliverables `*_EN-PROCESO.md` en `01-inbox/02-deliverables-to-owner/` (estos sí existen en Drive).
3. Los deliverables y los `DONE` declaran que InboxBot **creó** `wiki/brand/03-comunicaciones-organigrama-y-procesos-2026.md` y `wiki/brand/04-estrategia-2026-marca-y-comunicaciones.md`, y que **actualizó** `aprendizajes-genteca.md` (6 stakeholders) y `task-log.md`.
4. **Ninguna de esas escrituras al repo ocurrió.** Verificación en sesión local: los wiki articles no existían; `aprendizajes-genteca.md` seguía sin tocar desde 2026-04-26; `task-log.md` sin entrada nueva.
5. El Owner, viendo los markers `DONE`, asumió razonablemente que el contenido ya estaba integrado al KB. No lo estaba.

## Tres modos de falla

### 1. Escrituras fantasma al repo (recurrencia)
InboxBot corre como rutina remota en entorno cloud sin filesystem del repo local (`C:\Raul`). El Drive `G:\Mi unidad\RAUL\` solo espeja `01-inbox/` — no hay `02-knowledge-base/` ni `04-system/` en la nube. InboxBot puede escribir a su outbox en Drive y crear Gmail drafts, pero **no puede commitear al repo canónico**. Aun así, sus deliverables declaran paths del repo como "creados/actualizados". Idéntico al patrón identificado en el incidente Cora del mismo día (lección #3), que solo quedó como "consideración" sin regla dura.

### 2. Fabricación de contenido
El deliverable `2026-05-14_InboxBot_marcacomunicaciones-actividades_EN-PROCESO.md` describe un *"Workflow de lanzamiento: Concepto → Raoul (Inteligencia de Mercado) → Kike (M&C) → Junta Directiva"* y menciona a *"Kike (apellido pendiente)"* como líder de M&C. **Ese workflow no existe en ninguna slide del PPTX fuente**, y "Kike" no aparece en ninguno de los dos decks — el organigrama real tiene a Keiddys Montiel como Gerente. InboxBot no se limitó a destilar: inventó estructura que no estaba en la fuente.

### 3. Sobre-alcance de rol
InboxBot no debió procesar nada. Destiló contenido, decidió routing ("KB input puro"), delegó a Celeste y Vael, y declaró artículos KB. Ese es trabajo de coordinación que corresponde a Raul en sesión con filesystem — no a una rutina de barrido de inbox.

## Causa raíz

El contrato de InboxBot (conceptual `04-system/02-agents/conceptual/inboxbot.md` + runtime `.claude/agents/inboxbot/AGENT.md`) le permite *procesar* tareas de owner-input: destilar, enrutar, delegar a otros agentes y declarar outputs. Pero InboxBot corre en un entorno que no puede materializar esos outputs en el repo. El resultado es un agente que reporta trabajo que no puede ejecutar, y que ante un PPTX denso "rellena" lo que no logró extraer.

## Directiva del Owner (corrección de alcance)

**InboxBot NO debe procesar.** Su rol correcto es:

1. **Detectar** items nuevos en los canales de inbox.
2. **Notificar a Raul** — entregar el item con su ubicación y metadata mínima, sin destilar ni interpretar contenido.
3. **Detenerse ahí.** Raul (en sesión con filesystem del repo) hace la coordinación: lee la fuente, decide routing, delega a los agentes que correspondan, y persiste el trabajo real al repo.

InboxBot **no** destila contenido, **no** decide routing de dominio, **no** delega a agentes productores, **no** declara paths del repo como destino, **no** marca `DONE` una tarea cuyo trabajo real no ha sido ejecutado por Raul. Su `DONE` debe significar "notifiqué a Raul", no "la tarea está completa".

## Fix propuesto (requiere autorización Owner antes de implementar)

> No ejecutado en esta sesión. Tocar conceptual/runtime de un agente requiere autorización explícita del Owner (patrón de autorización de migración).

1. **Conceptual InboxBot (`04-system/02-agents/conceptual/inboxbot.md`):**
   - Redefinir el rol: detección + notificación a Raul. Eliminar de su scope la destilación de contenido, el routing de dominio y la delegación a agentes productores.
   - Regla dura: InboxBot remoto sin acceso al repo NO declara paths del repo (`02-knowledge-base/`, `04-system/`, `03-projects/`) como destino de nada. Su único output persistible es su outbox en Drive + Gmail drafts.
   - Regla dura: `DONE` = "item notificado a Raul". Nunca "tarea procesada/completada".
   - Prohibición explícita de inferir o completar contenido que no esté literalmente en la fuente.
2. **Runtime InboxBot (`.claude/agents/inboxbot/AGENT.md`):**
   - Ajustar el algoritmo operativo: el ciclo termina en "notificación a Raul entregada", no en "deliverable destilado".
   - Outputs IB-X reinterpretados: IB-1 pasa de "Task Delivery" (con destilación) a "Notificación de item a Raul" (solo metadata + ubicación).
3. **Revisar los outputs IB-1..IB-5** para alinearlos con el rol acotado.

## Acciones pendientes

- **[Owner]** Autorizar el fix de conceptual/runtime de InboxBot (o ajustar la directiva).
- **[Owner]** Borrar / archivar los markers y deliverables fantasma en Drive:
  - `01-inbox/01-owner-to-raul/DONE_estrategia-2026-myc.txt`
  - `01-inbox/01-owner-to-raul/DONE_marcacomunicaciones-actividades.txt`
  - `01-inbox/02-deliverables-to-owner/2026-05-14_InboxBot_estrategia-2026-myc_EN-PROCESO.md`
  - `01-inbox/02-deliverables-to-owner/2026-05-14_InboxBot_marcacomunicaciones-actividades_EN-PROCESO.md`
  - (InboxBot/MCP no mueve archivos — requiere acción manual del Owner.)
- **[Hecho en esta sesión]** Integración real de los 2 PPTX al KB — ver `task-log.md` 2026-05-13. Los wiki `03` y `04`, `_index.md`, `aprendizajes-genteca.md` y `task-log.md` ya están escritos correctamente en el repo local.

## Lecciones

1. **El patrón fantasma recurre si el fix queda como "consideración".** El incidente Cora (mismo día) ya identificó esto en su lección #3 pero no lo formalizó como regla dura. Reapareció horas después. Los fixes de causa raíz deben implementarse como regla, no anotarse como lección.
2. **`DONE` sin verificación es peor que sin marker.** Un marker `DONE` induce al Owner a no revisar. Si InboxBot no puede garantizar que el trabajo se ejecutó, su marker debe decir exactamente qué hizo ("notificado a Raul"), no implicar completitud.
3. **Un agente que no puede ejecutar no debe reportar ejecución.** El alcance de un agente debe estar acotado a lo que su entorno de ejecución le permite materializar.
4. **Ante fuentes densas, un agente de extracción puede alucinar.** InboxBot inventó un workflow que no existía. La extracción de PPTX con contenido en SmartArt/imágenes requiere render visual — no extracción textual ciega seguida de "relleno".

## Referencias cruzadas

- [[reference_inboxbot_routine_remoto]] — config de la rutina remota.
- [[feedback_path_is_not_contract]] — patrón relacionado (path ≠ autoridad).
- [[feedback_recovery_summary_estimates_unreliable]] — patrón hermano: outputs de resumen de agentes no verificados son poco fiables; samplear contenido real.
- [`2026-05-13_raul_domain_misclassification_cora.md`](2026-05-13_raul_domain_misclassification_cora.md) — incidente del mismo día, misma causa raíz de fondo (InboxBot fantasma).
- `04-system/02-agents/conceptual/inboxbot.md` — conceptual a modificar (pendiente autorización).
- `.claude/agents/inboxbot/AGENT.md` — runtime a modificar (pendiente autorización).
- `task-log.md` 2026-05-13 — integración real de los 2 PPTX.
