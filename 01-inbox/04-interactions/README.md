# 01-inbox/04-interactions/

**Canal de captura de interacciones humanas multicanal.** Drop zone para
artefactos **crudos** de interacción: notas de voz, transcripciones (Tactiq /
Zoom / Meet), chats exportados, screenshots de WhatsApp, fotos de notas
manuscritas.

Creado 2026-05-14 — fase mínima de la capa de captura de interacciones. Ver
`02-knowledge-base/01-foundations/PROPUESTA_capa-de-captura-de-interacciones_v1.md`
y la entrada 2026-05-14 en `04-system/03-governance/DECISIONS.md`.

## Estructura

- **Raíz del canal** — artefactos **crudos**: notas de voz, transcripciones,
  chats exportados, screenshots, fotos de notas manuscritas.
- **`_notas/`** — las **Notas de Interacción** destiladas. El prefijo `_` las
  mantiene fuera del escaneo de InboxBot (Fase 1): una nota destilada no se
  re-encola como ticket.

## Qué va aquí (raíz)

Artefactos crudos de cualquier interacción humana que **no pasó por el canal de
archivos** (Drive de colaboradores, `01-owner-to-raul/`): una conversación, una
llamada, una reunión, un WhatsApp, una videollamada, una nota a mano. Se suelta
el artefacto tal cual — la destilación se hace después, en sesión desktop.

## Qué NO va aquí

- Archivos que ya llegaron por la carpeta de un colaborador o por
  `01-owner-to-raul/` — no dupliques.
- **Interacciones Owner↔sistema** — las decisiones que tomas en sesión con el
  PKA no son human↔human; van a `DECISIONS.md` o a la memoria de governance, no
  a una Nota de Interacción. El alcance de la capa es **estrictamente
  human↔human**.
- Pensamiento propio en voz alta sin otro humano involucrado — eso es tarea o
  memoria, no interacción.

## Flujo

1. **Capturas** el artefacto crudo en la raíz del canal (Tier 0/1 — fricción
   casi cero).
2. **Se encola** en sesión desktop. (En Fase 1 de la propuesta, InboxBot extiende
   su escaneo a este canal; en fase mínima el Owner lo trae a colación al abrir
   sesión.)
3. **Se destila** → Nota de Interacción en `_notas/` (plantilla en
   `04-system/04-tools-and-scripts/templates/interaction-note-template.md`).
4. **Triaje:** el contenido destilado se enruta a su destino. El artefacto crudo
   permanece en la raíz como fuente referenciada por la nota.

## Filtro de señal — qué amerita destilarse

Solo lo que **creó o cambió**: una definición, una solicitud/compromiso, un
**cambio** (lo más valioso y lo de mayor decaimiento), una decisión, o una señal
de relación. La mayoría de las interacciones del día no necesitan nota — y eso es
correcto. Detalle en §7 de la propuesta.

## Privacidad

Este canal es **gitignored**. Los artefactos crudos y las Notas de Interacción
involucran a otras personas: no se versionan, no se comparten, no se citan en
contenido publicado. Las Notas son introspección operativa del Owner.
