# Incident — Raul misclassified domain from collaborator Drive location

**Fecha:** 2026-05-13
**Severidad:** Baja (entregable fantasma, no produjo trabajo real persistido — corregido antes de impacto a cliente)
**Detectado por:** Owner durante revisión manual de carpeta colaborador Cora
**Status:** Resuelto (regla añadida a Raul + InboxBot, memoria de contactos actualizada)

## Qué pasó

1. 2026-05-13 mañana: Cora deposita 3 archivos de un estudio de notoriedad de **Gama supermercados** en `G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad\`.
2. InboxBot remoto detecta los archivos en su barrido programado e invoca a Raul con la tarea.
3. Raul infiere que el dominio del proyecto es **Genteca** porque la carpeta padre del colaborador en Drive es `colaboradores/Genteca/`.
4. Raul produce un análisis preliminar y declara `Destino: 03-projects/genteca/2026-05_notoriedad-supermercados/`. InboxBot deja markers `DONE_*.txt` (en inbound) y `EN-PROCESO.md` (en outbound) referenciando ese path.
5. **Los archivos en el repo nunca se crearon** — InboxBot remoto corre en entorno cloud sin filesystem persistente del repo local, así que la "Fase 1" quedó fantasma.
6. Owner manual abre el ticket en sesión interactiva con Claude, define correctamente que es **consultoria-externa** (cliente final: Gama, no Genteca; Cora trae trabajo para múltiples dominios).

## Causa raíz

La conceptual de Raul (`04-system/02-agents/conceptual/raul.md` §2) listaba dominios conocidos pero NO incluía `consultoria-externa` ni `research-generic`, y NO contenía regla explícita sobre cómo inferir el dominio cuando un colaborador trae tareas. Por defecto, Raul tomó la ubicación del colaborador en Drive como proxy del dominio del proyecto. Esto es incorrecto: un colaborador puede traer trabajos para múltiples dominios.

Caso específico Cora-Urrea: vive en `colaboradores/Genteca/Cora-Urrea/` por historia (originalmente entró al sistema vía un proyecto Genteca), pero su clasificación primaria es `consultoria-externa` — trabaja con Owner en múltiples proyectos para clientes terceros (Gama es uno de ellos).

## Fix aplicado

1. **Raul conceptual (`04-system/02-agents/conceptual/raul.md` §2):**
   - Añadidos `consultoria-externa` y `research-generic` a la lista de dominios conocidos.
   - Añadida regla dura: ubicación del colaborador en Drive NO es proxy del dominio del proyecto. Domain del proyecto se infiere del contenido (cliente final + naturaleza del trabajo).
   - Añadido protocolo: si la tarea crea un proyecto nuevo (no existe `03-projects/<dominio>/<slug>/`), pausar y confirmar con Owner el dominio.

2. **InboxBot runtime adapter (`.claude/agents/inboxbot/AGENT.md` §"Estructura de colaboradores"):**
   - Aclaración: `<dominio>` en el path de Drive es organización de archivos, no clasificación autoritativa del proyecto.
   - Adición de `consultoria-externa/` (Cora-Urrea primaria) a la estructura actual de dominios.

3. **Memoria de contactos (`reference_genteca_contacts.md`):**
   - Cora reclasificada: clasificación primaria = `consultoria-externa`. Nota explícita que la carpeta Drive vive bajo Genteca por historia pero su dominio canónico es otro.

## Acciones pendientes (no críticas)

- **Decisión Owner: ¿mover físicamente la carpeta Drive de Cora** de `colaboradores/Genteca/Cora-Urrea/` a `colaboradores/consultoria-externa/Cora-Urrea/`? Pros: alinea path con dominio. Contras: rompe referencias existentes (incluyendo el proyecto Notoriedad Gama en flight con deadline 16/06). **Recomendación: no mover ahora**, ejecutar después de 16/06 cuando termine el proyecto en flight.
- **Borrar archivos fantasma InboxBot en Drive:**
  - `G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad\DONE_instrucciones-ia-notoriedad.txt`
  - `G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\02_De_Raoul_Para_Cora\2026-05-13_Raul_instrucciones-ia-notoriedad_EN-PROCESO.md`
  - Bloqueado por classifier en sesión interactiva 2026-05-13. Pendiente acción manual del Owner o autorización explícita.

## Lecciones

1. **El path no es contrato.** La organización de carpetas en Drive es para conveniencia humana; no debe ser fuente autoritativa para decisiones de clasificación automatizada.
2. **Proyectos nuevos requieren gate explícito.** Cuando Raul recibe una tarea que crea un proyecto en domain previamente inexistente, debe pausar y confirmar antes de escribir.
3. **InboxBot fantasma sin filesystem genera output engañoso.** El marker `EN-PROCESO.md` referenciaba archivos en el repo que no existían. Considerar añadir validación: InboxBot remoto que no puede commitear al repo NO debe declarar paths del repo como `Destino` — debe entregar el output completo en su outbox y dejar al Owner la decisión de dónde persistirlo.

## Referencias cruzadas

- [[project_consultoria_externa_gama_notoriedad_2026]] — proyecto afectado, ahora correctamente bajo consultoria-externa.
- [[reference_genteca_contacts]] — Cora reclasificada.
- `04-system/02-agents/conceptual/raul.md` §2 — regla añadida.
- `.claude/agents/inboxbot/AGENT.md` §"Estructura de colaboradores" — aclaración añadida.
