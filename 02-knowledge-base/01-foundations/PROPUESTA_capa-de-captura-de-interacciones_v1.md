# Propuesta — Capa de captura de interacciones multicanal

**Versión:** v1.2 — aprobada y calibrada
**Fecha:** 2026-05-14
**Tipo:** propuesta de asesoría — aprobada e implementada (fase mínima)
**Estado:** **APROBADA** por el Owner el 2026-05-14 (ver `DECISIONS.md`). Fase mínima implementada y calibrada tras el dry-run del mismo día (ver Changelog). Pendiente: integrar como §14 de la metodología (`Hoja_De_Ruta_Raul.md`) tras 2-4 semanas de uso real.
**Origen:** solicitada por el Owner el 2026-05-14 como asesoría para implementación posterior.

---

## 1. Resumen ejecutivo

El sistema /RAUL/ hoy captura bien **un** canal de interacción humana: el intercambio de archivos por Drive. Pero la mayoría del insumo de valor — definiciones, solicitudes, decisiones, cambios de opinión — nace en canales que el sistema no ve: conversaciones, llamadas, reuniones, WhatsApp, notas manuscritas. Ese insumo se pierde, se degrada en la memoria humana, o genera malentendidos meses después.

Esta propuesta plantea una **capa de captura de interacciones**: no un sistema de grabación total, sino una **disciplina de triaje** con tres componentes — un canal de entrada único para artefactos crudos, un artefacto canónico ligero (la *Nota de Interacción*), y un modelo de captura por niveles que ajusta la fricción al canal. El principio rector es el mismo que ya rige el modo remoto: **capturar es barato y tonto; procesar es caro y se hace donde hay tooling.** La propuesta es portable como patrón: carpeta + plantilla + filtro + modelo por niveles, todo en texto plano, vendor-neutral.

---

## 2. El problema

### 2.1 La interacción humana es el insumo más rico y el peor capturado

Los humanos interactuamos por muchos canales a la vez: hablamos, nos miramos, nos escribimos correos, intercambiamos archivos, nos reunimos (a veces con transcripción automática, a veces con notas a mano, a veces sin nada), llamamos por teléfono, usamos WhatsApp, hacemos videollamadas en plataformas distintas.

Cada una de esas interacciones puede generar **definiciones, solicitudes, ideas, proyectos, especificaciones, ajustes, cambios de idea, opiniones**. Algunas se convierten en acciones ejecutables. Otras se ignoran. Otras se olvidan. El problema no es que se ignoren algunas — eso es triaje sano. El problema es que **no decidimos qué se ignora**: simplemente se pierde, sin registro de que existió.

### 2.2 La memoria humana no es la solución — es parte del problema

La memoria humana es selectiva y poco confiable a seis meses. Esto es *eficiente* desde el punto de vista de la energía: recordarlo todo costaría demasiado, así que el cerebro descarta. Pero el costo es real: con el tiempo, la calidad de los fragmentos se degrada, y eso genera confusiones y malentendidos. Además la memoria **difiere entre humanos** — dos personas salen de la misma reunión con dos versiones distintas de lo acordado.

La metodología del PKA ya lo dice explícitamente (`Hoja_De_Ruta_Raul.md` §2.10, anti-patrón): *"depender de la memoria del operador para no repetir errores. La memoria humana es poco confiable a 6 meses; el sistema debe materializar el aprendizaje."* Esta propuesta extiende ese principio del *aprendizaje* a la *interacción*: lo que se definió o cambió en una conversación debe materializarse, no quedar en la cabeza de nadie.

### 2.3 Dos modos de falla — y por qué no basta con "grabar todo"

| Modo de falla | Qué pasa | Resultado |
|---|---|---|
| **Sub-captura** | La interacción nunca entra al sistema (el brief verbal, la decisión por WhatsApp, el cambio acordado en la llamada). | Se pierde. Reaparece como "pero tú dijiste..." meses después. |
| **Sobre-captura** | Se captura todo — transcripts completos de cada llamada, cada chat entero. | El sistema se vuelve un pantano. La señal queda enterrada bajo el ruido. Nadie consulta un archivo de 5.000 palabras. |

La tentación natural ante la sub-captura es "entonces grabemos todo". Es un error. La sobre-captura no resuelve el problema, lo desplaza: pasas de *no encontrar la información porque no existe* a *no encontrarla porque está sepultada*. La solución no es más volumen — es **triaje**.

---

## 3. Principio rector: capturar es triaje, no grabación

La capa de captura no es un sistema de grabación. Es una **disciplina de destilación**. Su trabajo es convertir interacción cruda en un artefacto pequeño, estructurado y trazable que el PKA pueda razonar.

Tres sub-principios, todos heredados de patrones ya validados en /RAUL/:

1. **Capturar y procesar son cosas distintas** (lección InboxBot v5.0). La captura en el momento de la interacción debe ser casi de fricción cero. La destilación — convertir el artefacto crudo en algo útil — se hace después, en sesión desktop, donde está el tooling.
2. **El filtro es por valor, no por volumen.** No se captura "la conversación". Se captura **lo que la conversación creó o cambió**. Ver §7.
3. **Lo crudo es fuente; lo destilado es memoria.** Un transcript de Tactiq es `raw-source`. La memoria es la Nota de Interacción de 5 líneas que se destila de él. Nunca se confunde una con la otra (es la separación cinco-capas de la metodología, §2.4).

---

## 4. El modelo propuesto: captura por niveles

No todos los canales tienen la misma fricción de captura ni la misma densidad de señal. Forzar un solo mecanismo para todos garantiza que se abandone. La propuesta usa **tres niveles**, y el Owner elige el nivel según el canal y el momento.

### Tier 0 — Canales que ya producen texto (fricción casi nula)

El artefacto ya existe; capturar = enrutarlo al canal de entrada.

| Canal | Artefacto nativo | Mecanismo de captura |
|---|---|---|
| Email | El correo ya es texto | Reenviar / BCC a una dirección de captura, o etiqueta de Gmail con barrido periódico |
| Intercambio de archivos Drive | El archivo | **Ya resuelto** — InboxBot lo captura hoy |
| Reuniones con transcripción (Tactiq, Zoom, Meet) | El transcript | Soltar el transcript en el canal de entrada |

Tier 0 se puede semi-automatizar. Es la fruta baja.

### Tier 1 — Captura rápida estructurada (fricción baja, 30-60 segundos)

El canal no produce texto solo, pero la captura cruda toma menos de un minuto.

| Canal | Mecanismo de captura |
|---|---|
| Llamada telefónica | Nota de voz de 30 s justo al colgar, soltada en el canal de entrada |
| Conversación presencial | Nota de voz, o foto de lo que se anotó a mano |
| WhatsApp | Reenviar los mensajes clave, o exportar el fragmento de chat, o screenshot |
| Videollamada sin transcripción | Igual que llamada: nota de voz al cerrar |

El punto clave: en Tier 1 **no se destila en el momento**. Se suelta el artefacto crudo y se sigue con la vida. La destilación viene después.

### Tier 2 — La Nota de Interacción (la disciplina deliberada)

Después de una interacción con peso — una reunión donde se definió un alcance, una llamada donde algo cambió — el Owner (o el PKA en sesión desktop, a partir del artefacto crudo) produce una **Nota de Interacción**: 5-10 líneas estructuradas. Esto es la disciplina que no se puede automatizar del todo, pero que **sí debe ser mínima**. Ver §5 para el formato.

**Regla de oro del modelo:** la fricción se paga en el momento más barato posible. En Tier 0 y Tier 1, el momento de la interacción cuesta casi nada (soltar un archivo, grabar 30 s). El trabajo cognitivo — destilar — se difiere a la sesión desktop. Esto replica exactamente el split capturar/procesar del modo remoto, y por la misma razón: el momento de la interacción no es el momento de tener tooling.

---

## 5. El artefacto canónico: la Nota de Interacción

Una Nota de Interacción es un Markdown pequeño. No es un acta. No es un transcript. Es la **destilación trazable** de lo que una interacción dejó.

```markdown
---
fecha: YYYY-MM-DD
canal: conversacion | llamada | reunion | email | whatsapp | videollamada | nota-manuscrita
participantes: [nombres]
dominio: [genteca | plenus | ... | transversal]
artefacto_crudo: [ruta al crudo en 01-inbox/04-interactions/_procesadas/, si existe]
estado: capturada | triada | accionada | archivada
---

## Qué pasó (2-3 frases)
Contexto mínimo. Suficiente para entender la nota dentro de seis meses.

## Lo que quedó
(usar solo las categorías que apliquen — ver §7)
- **Definición:** algo quedó definido (un spec, un alcance, un criterio).
- **Solicitud / compromiso:** alguien pidió algo, o alguien se comprometió a algo.
- **Cambio:** algo que ya estaba definido cambió. ← la categoría más importante.
- **Decisión:** se eligió entre alternativas.
- **Señal de relación:** algo cambió en cómo trabajar con esta persona (una fricción, una preferencia, un canal).

## Acciones ejecutables (si las hay)
- [ ] ...

## Preguntas abiertas
- ...
```

**Estados de una Nota** (campo `estado` del frontmatter): `capturada` (artefacto crudo en el canal, sin destilar) → `triada` (destilada y su contenido enrutado; puede tener acciones abiertas) → `accionada` (todas las acciones cerradas) → `archivada` (sin acciones abiertas ni valor de consulta activa). La nota destilada se guarda en `01-inbox/04-interactions/_notas/`.

**Por qué este formato y no otro:**

- **Frontmatter trazable** — fecha, canal, participantes, dominio, estado. Cumple el principio de trazabilidad obligatoria (§2.5 de la metodología): de cualquier nota se sabe de dónde salió, cuándo, con quién y en qué estado está.
- **"Lo que quedó" con categorías cerradas** — fuerza el triaje. Si nada cae en ninguna categoría, la interacción no necesitaba una nota. El formato mismo es el filtro.
- **Separa destilación de acción** — no toda interacción produce una tarea. Algunas solo producen una definición que va al conocimiento, o una señal de relación que va a `people.md`. La nota lo captura aunque no haya acción.
- **`artefacto_crudo` apunta, no incrusta** — el transcript de 5.000 palabras vive en `04-interactions/` como fuente; la nota lo referencia. Lo crudo es fuente, lo destilado es memoria.

---

## 6. Arquitectura propuesta

### 6.1 Nuevo canal de entrada: `01-inbox/04-interactions/`

Un canal hermano de `03-raw-sources/`, dedicado a artefactos crudos de interacción: notas de voz, transcripts, chats exportados, fotos de notas manuscritas, screenshots. Gitignored, igual que los demás buzones. Es el "drop zone" único para los tres niveles de captura.

**Estructura interna — división por estado, no por tipo:** la raíz del canal recibe los artefactos **crudos pendientes de destilar** (la raíz siempre muestra solo lo que falta procesar — escala a cualquier volumen de reuniones); el subfolder **`_procesadas/`** recibe los crudos **ya destilados** (fuente dormida, referenciada por su nota); el subfolder **`_notas/`** guarda las **Notas de Interacción destiladas**. El prefijo `_` mantiene ambos subfolders fuera del escaneo de InboxBot, de modo que ni una nota destilada ni un crudo ya procesado se re-encolan como ticket. Se eligió división por **estado** (pendiente / procesado) y no por **tipo de artefacto** (`transcripciones/`, `notas-voz/`, ...): a volumen alto el problema es saber qué falta destilar, no de qué tipo es cada cosa — y dividir por tipo reintroduce la proliferación de carpetas que el rediseño de InboxBot v5.0 eliminó.

### 6.2 El flujo: crudo → destilado → triaje → destino

```
Interacción humana
   │
   ▼
[Tier 0/1] artefacto crudo  ──────►  01-inbox/04-interactions/
   │
   ▼
[modo remoto] InboxBot lo captura como ticket  ──►  00-cola/
   │
   ▼
[sesión desktop] el Owner (con ayuda del PKA) destila
   │                    │
   ▼                    ▼
Nota de Interacción     artefacto crudo → _procesadas/ (fuente dormida)
   │
   ▼
[triaje] el contenido destilado se enruta a su destino:
   ├─ Acción ejecutable  ──►  tarea / cola de trabajo
   ├─ Definición / spec  ──►  02-knowledge-base/ (dominio correspondiente)
   ├─ Decisión           ──►  DECISIONS.md (si es arquitectónica) o KB de dominio
   ├─ Señal de relación  ──►  memoria de personas (people.md)
   └─ Solo registro      ──►  la nota se archiva — y eso también es valor
```

La Nota de Interacción destilada se guarda en `01-inbox/04-interactions/_notas/`; el artefacto crudo se mueve a `01-inbox/04-interactions/_procesadas/` como fuente referenciada — la raíz del canal queda solo con lo pendiente de destilar.

El último ramal es importante: **una interacción capturada que no se acciona no es desperdicio.** Quedó registrada, fechada, trazable. Si dentro de seis meses surge "pero acordamos X", la nota existe. El registro *es* el valor, aunque no haya acción.

### 6.3 Qué se automatiza y qué NO — la lección InboxBot

| Se automatiza | No se automatiza (es disciplina humana) |
|---|---|
| Captura de artefactos Tier 0 (barrido de etiqueta Gmail, carpeta de auto-guardado de transcripts) | La nota de voz tras una llamada — el sistema no sabe que la llamada ocurrió |
| InboxBot escanea `04-interactions/` y encola, igual que los demás buzones | El juicio de qué interacción merece Nota de Interacción y qué no |
| El PKA *asiste* la destilación en sesión desktop (transcribe la nota de voz, propone el borrador de la Nota de Interacción) | La validación de esa destilación — el Owner confirma que la nota refleja lo que pasó |

**Regla dura, heredada del incidente de escrituras fantasma:** el sistema **no debe fingir** que capturó una interacción que nunca vio. Una llamada telefónica que el Owner no grabó ni anotó no existe para el PKA, y está bien que así sea. Pretender lo contrario es el mismo error que motivó el rediseño de InboxBot a capture-only. El diseño honesto acepta que hay canales que solo la disciplina humana puede capturar.

### 6.4 Agente futuro: "Escriba de Interacciones" (diferido)

Eventualmente — Fase 5+ de la metodología, no antes — un agente dedicado (clase `execution-utility` o `global-service`) puede:

- Tomar el artefacto crudo de `04-interactions/` en sesión desktop.
- Transcribir notas de voz, parsear chats exportados.
- Proponer un borrador de Nota de Interacción aplicando el filtro de señal.
- Sugerir el enrutamiento del contenido destilado.

Pero esto es optimización, no fundamento. **El día uno no necesita un agente.** Necesita la carpeta, la plantilla y la disciplina del filtro. El agente se justifica solo cuando el volumen de interacciones capturadas haga que la destilación manual sea fricción real — y no antes (anti-patrón de la metodología §10.5: "diseñar el agente perfecto en el papel antes de probarlo").

---

## 7. El filtro de señal: qué capturar y qué dejar pasar

El corazón de la propuesta. Sin un filtro claro, la capa de captura colapsa en sobre-captura.

**Captura cuando una interacción produce una de estas cinco cosas:**

1. **Una definición** — algo quedó definido: un spec, un alcance, un criterio, un nombre, un precio.
2. **Una solicitud o compromiso** — alguien pidió algo concreto, o alguien (incluido tú) se comprometió a algo.
3. **Un cambio** — algo que *ya estaba definido* cambió. Esta es la categoría de mayor valor y mayor decaimiento: los conflictos "pero tú dijiste..." nacen casi siempre de un cambio que nadie capturó.
4. **Una decisión** — se eligió entre alternativas.
5. **Una señal de relación** — cambió algo en cómo trabajar con esa persona: una fricción, una preferencia de canal, un estilo, un límite.

**No captures:**

- Cortesías, saludos, charla sin compromiso.
- Actualizaciones de estado que no cambian nada ("voy avanzando bien").
- Cosas que ya están capturadas en otro canal (no dupliques el archivo de Drive en una nota).
- **Interacciones Owner↔sistema** — las decisiones que tomas en sesión con el PKA no son human↔human; van a `DECISIONS.md` o a la memoria de governance, no a una Nota de Interacción. El alcance de la capa es **estrictamente human↔human**.
- Tu propio pensamiento en voz alta que no involucró a otro humano — eso es otra cosa (va a tareas o a memoria, no a Notas de Interacción).

**Test operativo:** ¿esta interacción creó o cambió un compromiso, una definición, un plan, una decisión o una relación? Si no, no necesita Nota de Interacción. La mayoría de las interacciones de un día **no** la necesitan — y eso es correcto. El filtro protege contra la fatiga de captura tanto como contra el pantano.

---

## 8. Privacidad y límites

Capturar interacciones involucra a otras personas. Reglas no negociables:

- **Las Notas de Interacción son introspección operativa del Owner.** No se comparten, no se citan en contenido publicado, no salen del sistema. Misma regla que el observation log del operador (`Hoja_De_Ruta_Raul.md` §10.6: "propiedad del operador").
- **`04-interactions/` es gitignored.** Artefactos crudos — notas de voz, chats, transcripts — nunca van al repositorio versionado ni a GitHub.
- **Consentimiento donde la ley o la cortesía lo pidan.** Grabar una llamada o una reunión puede requerir avisar a los participantes según jurisdicción. La captura por nota de voz *propia tras* la interacción no graba al otro — destila lo que el Owner recuerda — y es la opción por defecto más segura.
- **Datos sensibles de terceros** (salud, finanzas, legal de otra persona) no van a Notas de Interacción genéricas; van a folders dedicados con el tratamiento que corresponda.

---

## 9. Trade-offs y riesgos honestos

| Riesgo | Mitigación |
|---|---|
| **Fatiga de la disciplina.** Si la captura se siente como trabajo, el Owner la abandona en dos semanas. | El filtro de §7 hace que la mayoría de interacciones *no* necesiten nota. Tier 0/1 cuestan casi nada. La Nota de Interacción es 5-10 líneas, no un acta. Si se siente pesada, se rediseña — no se tolera. |
| **El pantano de la sobre-captura.** Capturar todo entierra la señal. | El filtro por valor (no por volumen). Lo crudo se separa de lo destilado. La nota es chica por diseño. |
| **La trampa del transcript.** Tratar un transcript de 5.000 palabras como "la memoria". | Lo crudo es `raw-source`, la destilación es memoria. El transcript se referencia, no se incrusta. Regla explícita en §5. |
| **Tentación de automatizar lo inautomatizable.** Creer que un día el sistema "capturará solo" las llamadas. | Aceptación de diseño: hay canales que solo la disciplina humana captura. El sistema no finge capacidades que su entorno no le da (lección InboxBot). |
| **Scope creep del agente futuro.** Que el "Escriba de Interacciones" se vuelva un procesador que decide por el Owner. | Diferido a Fase 5+. Cuando llegue, su boundary es *asistir la destilación*, no decidir el triaje. El Owner valida cada nota. |
| **Privacidad de terceros.** Capturar interacciones es capturar a otras personas. | §8. Gitignored, no compartido, no citado. Nota de voz propia tras la interacción como default seguro. |

---

## 10. Cómo se migra como patrón

Toda la propuesta es portable a cualquier PKA clonado del patrón, porque todo es texto plano y vendor-neutral:

- **El canal** `01-inbox/04-interactions/` — una carpeta. Se crea igual en cualquier clon.
- **La plantilla** de Nota de Interacción — un Markdown con frontmatter. Se copia tal cual.
- **El filtro de señal** (§7) — cinco categorías. Es metodología, no código.
- **El modelo por niveles** (§4) — un criterio de decisión. Portable.
- **El agente** (§6.4, diferido) — cuando exista, será un conceptual SSOT + thin-adapter, como cualquier otro agente del patrón Modelo A.

Si se aprueba, la recomendación es **integrar esta propuesta como §14 de la `Hoja_De_Ruta_Raul.md`** ("Captura de interacciones multicanal") — así cualquier persona que use la metodología para construir su PKA la recibe como parte del patrón, no como un añadido suelto.

---

## 11. Plan de implementación por fases

| Fase | Qué se hace | Esfuerzo | Cuándo |
|---|---|---|---|
| **Mínima (día 1)** | Crear `01-inbox/04-interactions/`. Adoptar la plantilla de Nota de Interacción. Adoptar la disciplina del filtro de §7. **Cero automatización, cero agentes.** | Bajo — una carpeta, una plantilla, un hábito | Inmediato si se aprueba |
| **Fase 1** | InboxBot extiende su escaneo a `04-interactions/`. Rutas semi-automáticas para Tier 0 (etiqueta Gmail con barrido, carpeta de auto-guardado de transcripts). | Medio — ajuste a InboxBot + configuración Gmail/Drive | Tras 2-4 semanas de uso de la fase mínima, con fricciones reales detectadas |
| **Fase 2** | Agente "Escriba de Interacciones": asiste la destilación crudo → Nota de Interacción y propone enrutamiento. | Alto — research + hire + conceptual + thin-adapter + smoke test | Fase 5+ de la metodología, solo si el volumen lo justifica |
| **Fase 3** | Integración con memoria de governance: "señales de relación" → `people.md`; "definiciones" → KB de dominio; "cambios" se cruzan con lo ya definido y levantan flags de conflicto. | Alto | Después de Fase 2 estable |

**Recomendación:** aprobar y arrancar solo la **fase mínima**. Es de bajo costo, reversible, y las dos a cuatro semanas de uso real revelarán si el filtro de §7 está bien calibrado antes de invertir en automatización. El anti-patrón a evitar es construir las cuatro fases en abstracto: solo el uso real revela los gaps.

---

## 12. Decisión del Owner

**Aprobada íntegramente el 2026-05-14.** Las tres preguntas — (1) el principio de captura como disciplina de triaje, (2) el arranque de la fase mínima, (3) la integración futura como §14 de la metodología — fueron aprobadas. Registro en `DECISIONS.md` (entrada 2026-05-14).

**Fase mínima implementada el 2026-05-14:** canal `01-inbox/04-interactions/` (+ subfolder `_notas/`), plantilla en `04-system/04-tools-and-scripts/templates/interaction-note-template.md`, entrada en `.gitignore` y en `DECISIONS.md`. Calibrada el mismo día tras un dry-run con dos Notas de Interacción reales (ver Changelog).

**Pendiente:** 2-4 semanas de uso real para calibrar el filtro de señal antes de autorizar la Fase 1; luego integrar como §14 de `Hoja_De_Ruta_Raul.md`.

---

*Propuesta elaborada como asesoría. Aprobada e implementada en fase mínima el 2026-05-14.*

---

## Changelog

### v1.2 — 2026-05-14 (estructura por estado)

- **Subfolder `_procesadas/` añadido.** Calibración tras el Owner confirmar que las transcripciones de reuniones serán su modo de captura **dominante** (verbal interaction → decisiones y solicitudes). A volumen alto, el diseño "el crudo permanece en la raíz como fuente" no escala: la raíz se vuelve ruidosa y se pierde la señal de qué falta destilar.
- **División por estado, no por tipo.** La raíz = crudos **pendientes** de destilar; `_procesadas/` = crudos **ya destilados** (fuente dormida); `_notas/` = notas destiladas. Se descartó dividir por tipo de artefacto (`transcripciones/`, `notas-voz/`, ...) porque reintroduce proliferación de carpetas y no resuelve el problema real (saber qué falta procesar). El patrón coincide con `_archived/` / `03_Archivo/` del resto del sistema.
- Actualizado §6.1, §6.2, §5 (campo `artefacto_crudo`) + README del canal.

### v1.1 — 2026-05-14 (aprobada y calibrada)

- Estado: PROPUESTA → APROBADA por el Owner. Fase mínima implementada el mismo día.
- Calibración tras un dry-run con dos Notas de Interacción reales (la aprobación de esta propuesta + el handoff a Valeria del 2026-05-13):
  - **Alcance confirmado estrictamente human↔human.** Las interacciones Owner↔sistema (decisiones tomadas en sesión con el PKA) quedan explícitamente fuera — van a `DECISIONS.md`. Añadido a §7 y al README del canal. El enum `canal` no necesita un valor para sesiones Owner↔sistema.
  - **Subfolder `_notas/`.** Las Notas de Interacción destiladas viven en `01-inbox/04-interactions/_notas/`, separadas de los artefactos crudos en la raíz del canal. El prefijo `_` las mantiene fuera del escaneo de InboxBot. Añadido a §6.1 y §6.2.
  - **Criterios de `estado` definidos.** `capturada` → `triada` → `accionada` → `archivada`, cada uno con criterio explícito. Añadido a §5 y a la plantilla.
- Ningún hallazgo del dry-run fue bloqueante: calibración, no defecto.

### v1 — 2026-05-14 (propuesta)

- Versión inicial, solicitada por el Owner como asesoría. Modelo de captura por niveles + Nota de Interacción como artefacto canónico + filtro de señal de 5 categorías.
