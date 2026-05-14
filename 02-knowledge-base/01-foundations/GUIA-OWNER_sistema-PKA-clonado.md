# Guía del Owner — Entender y operar un sistema PKA clonado de /RAUL/

**Versión:** v0.1 — semilla
**Última actualización:** 2026-05-14
**Tipo:** documento de onboarding para owner
**Estado:** **Documento semilla.** Es la primera versión de lo que será la *Guía de Usuarios Owner* completa. Cubre el modelo mental y las buenas prácticas esenciales; queda marcado para expansión — ver §8.
**Audiencia:** una persona que recibió permiso para clonar /RAUL/ y montar su propio PKA a partir de este patrón.

---

## 0. Para quién es este documento

Si estás leyendo esto, alguien te dio permiso de clonar /RAUL/ para construir tu propio Personal Knowledge Assistant. Este documento **no te enseña a construir un PKA desde cero** — eso lo hace la metodología (`Hoja_De_Ruta_Raul.md`). Este documento te explica, en términos prácticos, **qué acabas de recibir, cómo piensa el sistema, y cómo se opera** — para que el primer día no estés perdido.

Léelo completo una vez. Toma unos 15 minutos. Después vuelve a las secciones que necesites.

---

## 1. Qué acabas de clonar

Un **PKA (Personal Knowledge Assistant)** es un sistema de archivos + agentes LLM + gobernanza + workflows que asiste a **una sola persona** a:

- Capturar, organizar y recuperar conocimiento personal y profesional.
- Producir entregables de calidad consistente a través de múltiples dominios de su vida y trabajo.
- Mantener trazabilidad de lo que decidió, cuándo y por qué.
- Evolucionar sin reescribirse cuando cambian las herramientas debajo.

No es una app. No es un chatbot con memoria. Es una **arquitectura** — y su valor está en que sobrevive al cambio de herramientas. El conocimiento vive en texto plano (Markdown), portable y reconstruible.

**Tres documentos te dan el fondo completo** (no hace falta leerlos hoy, pero sábelos):

| Documento | Qué te da |
|---|---|
| `02-knowledge-base/00-raul-intelligence/methodology/Hoja_De_Ruta_Raul.md` | La metodología: por qué la arquitectura es como es. |
| `04-system/01-config/FOLDER-ARCHITECTURE.md` | El mapa detallado de carpetas. |
| `04-system/03-governance/OPERATIVA-REMOTA-Y-COLABORADORES.md` | Cómo se opera día a día, en local y en remoto. |

Esta guía vive **encima** de los tres: te orienta para que sepas a cuál ir y cuándo.

---

## 2. El modelo mental en cinco ideas

### 2.1 Un PKA sirve a UNA persona

No es un sistema de equipo. No tiene clientes externos, ni SLAs, ni un equipo de mantenimiento. Tú eres proveedor y consumidor al mismo tiempo. Esto cambia la métrica de éxito: no es "horas-equipo ahorradas", es **fricción reducida para ti**. Cualquier estructura que te sume fricción sin retorno claro es deuda neta — bórrala. Lo que para una empresa es "buen formalismo", para un individuo puede ser parálisis.

### 2.2 Cada humano tiene (o no) su propio PKA — y el sistema funciona igual

Esta es la idea más importante de toda la guía, y la más fácil de malentender.

/RAUL/ **no** es un sistema agéntico que un equipo humano comparte. Es un sistema que **una persona** usa para trabajar mejor. Cuando esa persona interactúa con otros humanos — su jefe, sus colaboradores, un proveedor, un cliente — esas interacciones **siguen siendo interacciones humanas normales**. No requieren que el otro tenga un PKA. No requieren que el otro entre a tu sistema. No requieren un sistema compartido entre ambos.

Tu colaborador te manda un archivo por Drive, te escribe un WhatsApp, te explica algo en una reunión. Para él, eso es trabajo normal — no cambió nada en su vida. Para tu PKA, eso es un **insumo que tú incorporas** desde tu lado, con tus herramientas, a tu ritmo.

**Por qué esto importa tanto:**

- Hace el patrón **trivial de adoptar persona a persona.** En una organización donde algunos tienen PKA y otros no, nadie tiene que esperar a nadie. No hay "migración de equipo", no hay "todos deben adoptar la herramienta primero".
- El PKA se inserta **por debajo** del flujo humano existente, no lo reemplaza. Las interacciones habituales entre personas se mantienen; cada PKA las absorbe sin fricción para el otro lado.
- Un sistema que exige que todos lo adopten para funcionar es un sistema que casi nunca se adopta. Este **no exige nada de nadie excepto de ti**.

Corolario para el diseño: cuando pienses en agregar una capacidad a tu PKA, pregúntate siempre "¿esto obliga a otro humano a cambiar cómo trabaja conmigo?". Si la respuesta es sí, probablemente lo estás diseñando mal. La carga de adaptación es tuya, no de ellos.

### 2.3 Dos modos: el desktop procesa, el remoto solo captura

El sistema tiene **dos entornos de ejecución distintos**, y entender la diferencia es la clave de toda la operación:

- **Modo desktop** — cuando abres una sesión en tu PC. El orquestador y los especialistas tienen acceso a todo el repositorio. Aquí se **procesa**: se delega, se produce, se escribe al conocimiento, se gobierna.
- **Modo remoto** — una rutina automática en la nube (en /RAUL/ se llama InboxBot). Solo alcanza la nube, no el repositorio. Aquí **solo se captura**: detecta lo que entró, lo encola, te notifica. No procesa nada.

Por qué la separación es así de estricta: el modo remoto corre en un entorno que honestamente *no puede* hacer el trabajo de fondo. Pretender que sí podía fue causa de errores reales (escrituras fantasma, mayo 2026). El rediseño lo acotó a lo que su entorno **sí** puede hacer con honestidad. **Lección portable:** nunca dejes que un componente finja una capacidad que su entorno no le da. Detalle en `OPERATIVA-REMOTA-Y-COLABORADORES.md`.

### 2.4 El sistema materializa la memoria que tú no deberías cargar

La memoria humana es selectiva y poco confiable a seis meses. Esto es *eficiente* para ti — recordarlo todo costaría demasiada energía — pero el costo es que los fragmentos se degradan con el tiempo y generan confusión y malentendidos. El PKA existe, en parte, para **sacarte ese peso de encima**: lo que se decidió, cuándo, por qué y con quién vive en el sistema — fechado y trazable — no en tu cabeza.

Corolario duro: **si una decisión importante solo existe en tu memoria, el sistema te falló — o tú no la capturaste.** La captura es responsabilidad compartida entre tú y el sistema. La sección §5 y la propuesta de captura de interacciones (`PROPUESTA_capa-de-captura-de-interacciones_v1.md`) tratan esto en profundidad.

### 2.5 Tú eres el último filtro en límites claros

El sistema opera solo en lo reversible y de bajo riesgo (leer, editar borradores, proponer, reorganizar dentro de scope). Para acciones de **alto blast radius** — publicar contenido externo, enviar mensajes, borrar información canónica, decisiones financieras/legales/médicas, tocar infraestructura compartida — tú confirmas explícitamente, siempre.

Pero ojo con el anti-patrón opuesto: **pedir confirmación para todo erosiona la confianza y te entrena a aprobar sin leer.** El sistema debe distinguir bien qué necesita tu firma y qué no. Si te está preguntando demasiado, eso es un bug de diseño, no prudencia.

---

## 3. Cómo fluyen las interacciones humanas — el modelo persona a persona

Esta sección operacionaliza la idea 2.2.

### 3.1 El colaborador no necesita saber nada de tu sistema

En /RAUL/, cada colaborador externo tiene una carpeta compartida en Drive con tres subcarpetas fijas, nombradas **desde la perspectiva del colaborador**:

```
<Nombre-Apellido>/
├── 01_De_<Nombre>_Para_Raoul/   ← el colaborador te deja cosas a ti
├── 02_De_Raoul_Para_<Nombre>/   ← tú le dejas cosas al colaborador
└── 03_Archivo/                   ← histórico ya procesado
```

Para el colaborador, esto es simplemente "una carpeta de Drive que compartimos". Sube archivos, baja archivos. No sabe que existe un PKA, no sabe que existe un orquestador, no le importa. **Toda la maquinaria es invisible para él** — y esa invisibilidad es una característica, no una carencia.

### 3.2 Tu PKA captura tu lado de la interacción

Cuando el colaborador deja un archivo, el modo remoto lo **captura** como un ítem en cola (igual que captura tus propias tareas). Cuando tú abres sesión desktop, el sistema lo procesa y, si hay respuesta, la deja en la subcarpeta `02_De_Raoul_Para_<X>/`. El colaborador la encuentra ahí, como siempre.

El intercambio de archivos por Drive es **un canal de interacción** — pero no es el único, ni el más rico. También conversas, llamas, te reúnes, te escriben por WhatsApp. Hoy el sistema captura bien el canal de archivos; los demás canales son el tema de la propuesta de captura de interacciones (§5 y el documento de propuesta dedicado).

### 3.3 Reglas de orden que vas a querer respetar

- Cada colaborador ve **solo su propia carpeta** — nunca el folder maestro ni el de dominio.
- No mezcles dominios dentro de la carpeta de un colaborador.
- La convención de nombres de subcarpeta es **contrato con la automatización** — el sistema las busca por nombre exacto. Renombrarlas rompe la captura.
- Cuando un colaborador trabaja en un sistema corporativo que tu PKA no puede leer (SharePoint, Box), **tú operas el puente manualmente**: descargas de su sistema y copias a la carpeta de Drive. Su sistema es la fuente de verdad; la copia en Drive es staging.

Detalle operativo completo en `OPERATIVA-REMOTA-Y-COLABORADORES.md` Parte 2.

---

## 4. Buenas prácticas: tú ↔ el sistema agéntico

Estos patrones están validados en uso real de /RAUL/. Adóptalos desde el día uno.

1. **Borradores en texto antes de escribir a disco.** Cuando el sistema vaya a producir un archivo no trivial, que primero te muestre el borrador. Validas o corriges. Solo después se escribe. Reduce reescrituras y "permission loops".
2. **Autorización literal para blast radius medio/alto.** Que el sistema espere un "ejecuta X" explícito, no un "tú decides" implícito.
3. **No auto-continuar después de validación parcial.** Si aprobaste una sub-tarea, el sistema no sigue solo con el resto del plan. Cada hito se reautoriza.
4. **Cierre en 1-2 frases.** Qué cambió y qué sigue. Si quieres detalle, lees el diff. Nada de reportes largos por defecto.
5. **El sistema te muestra la cola al abrir sesión.** Lo primero en cada sesión desktop es el digest de lo que se capturó desde la última vez. Si no lo menciona, recuérdaselo — es ritual, no opción.
6. **Toda memoria lleva fecha y estado.** Una nota sin fecha y sin estado ("vigente / obsoleto / en revisión") se vuelve ruido en seis meses. No acumules memoria evergreen.

### Errores que vas a querer evitar

- **Agentes con scope difuso ("el experto en X").** Sin lista explícita de outputs y límites, el agente termina haciendo de todo y nada bien.
- **Pedir confirmación para todo.** Fatiga, y te entrena a aprobar sin leer.
- **Documentación desincronizada.** Cuando el conceptual dice X, el runtime hace Y y el README dice Z — la verdad operativa es lo que el agente *ejecuta*. Cuando detectes divergencia, sincroniza todo el stack en una sola pasada.
- **Sobre-diseñar antes de tener trabajo real.** Estructura mínima viable primero; agregas cuando un boundary real lo justifica, nunca por anticipación.

---

## 5. Buenas prácticas: tú ↔ otros humanos (y cómo alimentan tu PKA)

El canal de archivos por Drive está resuelto. Pero la mayoría de tus interacciones de valor **no pasan por un archivo**: pasan por una conversación, una llamada, una reunión, un WhatsApp. Esas interacciones generan definiciones, solicitudes, ideas, cambios de opinión, decisiones — y se pierden si no entran al sistema.

Principios mientras la capa de captura completa se implementa (ver `PROPUESTA_capa-de-captura-de-interacciones_v1.md`):

1. **Captura decisiones y cambios, no conversaciones.** No necesitas grabar todo. Necesitas que entre al sistema lo que **creó o cambió** un compromiso, una definición, un plan o una decisión. Lo demás es ruido.
2. **El cambio de opinión es lo más peligroso de perder.** "Pero tú dijiste..." nace de un cambio que nadie capturó. Cuando algo que ya estaba definido cambia en una conversación, eso *tiene* que entrar al sistema.
3. **Captura crudo en el momento, destila después.** En el momento de la interacción, la fricción debe ser casi cero — una nota de voz, una foto de la hoja, reenviar el mensaje clave. La destilación (convertir eso en una nota estructurada) se hace después, en sesión desktop, donde tienes el tooling. Mismo principio que el modo remoto: capturar es barato y tonto; procesar es caro y se hace donde se puede.
4. **El transcript no es la memoria.** Un transcript de Tactiq/Zoom de 5.000 palabras es fuente cruda, no memoria. La memoria es la destilación de 5 líneas que sacas de él.
5. **Las notas de interacción son tuyas.** Son introspección operativa — no se comparten, no se citan en contenido publicado, no salen del sistema. Capturar una interacción involucra a otras personas; trátalo con ese cuidado.

---

## 6. Tus primeros pasos al clonar

1. **Lee** este documento completo, luego `Hoja_De_Ruta_Raul.md` (la metodología) y `FOLDER-ARCHITECTURE.md` (el mapa).
2. **Declara tu fuente canónica.** Qué carpeta es canon, qué es derivado. Escríbelo en el README.
3. **Renombra el sistema.** /RAUL/ lleva el nombre de su owner original. El tuyo lleva el tuyo. Ajusta nombres de carpetas, rutas y referencias — el patrón es portable, la identidad no.
4. **Vacía los buzones y el archivo histórico.** `01-inbox/`, `05-archive/` y la memoria del runtime son del owner original. Empiezas en limpio.
5. **Revisa los dominios.** /RAUL/ trae dominios reales (Genteca, Plenus, etc.). Los tuyos son otros. Borra los que no apliquen, crea los tuyos con la anatomía estándar de domain pack.
6. **Conserva la maquinaria, reemplaza el contenido.** Los agentes Tier 0 (orquestador + investigador + contratador), la taxonomía de 6 clases, el patrón Modelo A, la estructura de gobernanza — eso es el patrón, se queda. Los especialistas de dominio, el conocimiento, los proyectos — eso es contenido, lo reemplazas.
7. **Monta el modo remoto** (los dos buzones de Drive + el tablero de estado + la rutina de captura) siguiendo `OPERATIVA-REMOTA-Y-COLABORADORES.md`.
8. **No actives todo de golpe.** Un dominio funcionando de punta a punta vale más que cinco a medias. Máximo 1-2 dominios nuevos por mes.

---

## 7. Lo que NO debes asumir

- **No asumas que el sistema recuerda lo que tú no capturaste.** No tiene memoria mágica. Si no entró, no existe para él.
- **No asumas que los colaboradores deben adaptarse a ti.** La carga de absorción es de tu PKA, no de ellos (idea 2.2).
- **No asumas que más agentes = mejor.** /RAUL/ tiene ~30 agentes y eso es una desviación deliberada del consejo canónico (~8). Funciona porque su owner acepta el costo de mantenerlos. Si tú no, empieza con pocos.
- **No asumas que la automatización resuelve la captura.** Hay canales que ningún sistema puede ver solo (una llamada, una conversación presencial). Ahí la captura es disciplina humana, no software. Aceptarlo es parte del diseño honesto.

---

## 8. Hacia dónde va este documento

Este es un **documento semilla** (v0.1). Cubre lo esencial para que un owner nuevo no esté perdido, pero está marcado para crecer hacia la **Guía de Usuarios Owner** completa, que deberá desarrollar con más profundidad:

- El detalle operativo de cada modo de trabajo, con ejemplos paso a paso.
- El catálogo completo de buenas prácticas de interacción humano ↔ sistema agéntico **y** humano ↔ humano, con casos.
- Guía de troubleshooting por síntoma.
- Recomendaciones de adopción gradual para una persona sin experiencia previa con sistemas agénticos.
- Integración de la capa de captura de interacciones una vez aprobada e implementada.

Cuando se aborde esa guía completa, este documento es el punto de partida — no se reescribe desde cero, se expande.

---

## 9. Referencias

- `02-knowledge-base/00-raul-intelligence/methodology/Hoja_De_Ruta_Raul.md` — metodología completa para construir un PKA.
- `04-system/01-config/FOLDER-ARCHITECTURE.md` — arquitectura de carpetas detallada.
- `04-system/03-governance/OPERATIVA-REMOTA-Y-COLABORADORES.md` — operativa local/remoto y colaboradores.
- `04-system/03-governance/DECISIONS.md` — log de decisiones arquitectónicas.
- `02-knowledge-base/01-foundations/PROPUESTA_capa-de-captura-de-interacciones_v1.md` — propuesta para capturar interacciones multicanal (en estado de propuesta al momento de esta v0.1).
- `02-knowledge-base/01-foundations/PKA-AUDIT-FRAMEWORK_RAUL.md` — framework de auditoría del sistema.
