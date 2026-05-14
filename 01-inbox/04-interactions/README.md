# 01-inbox/04-interactions/

**Canal de captura de interacciones humanas multicanal.** Drop zone único para
artefactos **crudos** de interacción: notas de voz, transcripciones (Tactiq /
Zoom / Meet), chats exportados, screenshots de WhatsApp, fotos de notas
manuscritas.

Creado 2026-05-14 — fase mínima de la capa de captura de interacciones. Ver
`02-knowledge-base/01-foundations/PROPUESTA_capa-de-captura-de-interacciones_v1.md`
y la entrada 2026-05-14 en `04-system/03-governance/DECISIONS.md`.

## Qué va aquí

Artefactos crudos de cualquier interacción humana que **no pasó por el canal de
archivos** (Drive de colaboradores, `01-owner-to-raul/`): una conversación, una
llamada, una reunión, un WhatsApp, una videollamada, una nota a mano. Se suelta
el artefacto tal cual — la destilación se hace después, en sesión desktop.

## Qué NO va aquí

- Archivos que ya llegaron por la carpeta de un colaborador o por
  `01-owner-to-raul/` — no dupliques.
- La **Nota de Interacción** destilada — esa no es cruda; vive donde su contenido
  la lleve tras el triaje (tarea, KB de dominio, memoria de personas, o archivada).
- Pensamiento propio en voz alta sin otro humano involucrado — eso es tarea o
  memoria, no interacción.

## Flujo

1. **Capturas** el artefacto crudo aquí (Tier 0/1 — fricción casi cero).
2. **Se encola** en sesión desktop. (En Fase 1 de la propuesta, InboxBot extiende
   su escaneo a este canal; en fase mínima el Owner lo trae a colación al abrir
   sesión.)
3. **Se destila** → Nota de Interacción (plantilla en
   `04-system/04-tools-and-scripts/templates/interaction-note-template.md`).
4. **Triaje:** el contenido destilado se enruta a su destino. El artefacto crudo
   permanece aquí como fuente referenciada por la nota.

## Filtro de señal — qué amerita destilarse

Solo lo que **creó o cambió**: una definición, una solicitud/compromiso, un
**cambio** (lo más valioso y lo de mayor decaimiento), una decisión, o una señal
de relación. La mayoría de las interacciones del día no necesitan nota — y eso es
correcto. Detalle en §7 de la propuesta.

## Privacidad

Este canal es **gitignored**. Los artefactos crudos involucran a otras personas:
no se versionan, no se comparten, no se citan en contenido publicado. Las Notas
de Interacción destiladas son introspección operativa del Owner.
