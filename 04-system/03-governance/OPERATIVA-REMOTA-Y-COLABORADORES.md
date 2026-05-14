# Operativa remota /RAUL/ — Owner desde celular + colaboradores

**Versión:** 2.0
**Fecha:** 2026-05-14
**Aplica a:** Owner (Raoul Bermúdez) + colaboradores Genteca / Academicos / futuros dominios.

> **v2.0 — rediseño del modelo remoto.** Refleja el rediseño de InboxBot a
> capture-only (conceptual v5.0, 2026-05-14). El cambio central: **InboxBot
> ya no procesa nada remotamente** — solo captura, encola y notifica. El
> procesamiento real ocurre cuando el Owner abre una sesión desktop. Ver
> `04-system/02-agents/conceptual/inboxbot.md` y la entrada 2026-05-14 en
> `DECISIONS.md`.

Este documento responde:

1. ¿Dónde dejo tareas cuando estoy fuera del PC, y qué pasa con ellas?
2. ¿Cómo trabajo cuando estoy remoto vs cuando estoy en el desktop?
3. ¿Cómo trabajo con los colaboradores externos vía Drive?

---

## Parte 1 — Los dos modos de trabajo: remoto y desktop

El sistema /RAUL/ tiene **dos entornos de ejecución distintos**, y entender
la diferencia es la clave de todo:

| | **Modo desktop** | **Modo remoto** |
|---|---|---|
| Quién opera | Raul (orquestador) + especialistas, en sesión Claude Code | InboxBot, como rutina automática en la nube |
| Qué alcanza | Todo el repositorio `C:\RAUL\` + la nube | **Solo** la nube (`G:\Mi unidad\RAUL\`) |
| Qué puede hacer | Procesar, delegar, producir entregables, escribir al KB, gobernar, commitear | **Solo capturar**: detectar lo que entró, encolarlo, notificar |
| Cuándo | Cuando el Owner abre una sesión | Cada 2h en ventana diurna (trigger automático) |

**Por qué esta separación:** InboxBot corre en un entorno que **no tiene
acceso al repositorio**. No puede leer el KB, no puede delegar a
especialistas reales, no puede escribir a `02-knowledge-base/` ni
`03-projects/`. Pretender que sí podía fue la causa de las escrituras
fantasma de mayo 2026. El rediseño v5.0 lo acota a lo que su entorno
**sí** puede hacer con honestidad: capturar y encolar.

### 1.1 Canales canónicos vivos (Google Drive)

Toda la operación remota corre sobre **Google Drive**, cuenta
`raoul.bermudez@gmail.com`. OneDrive **no es canal**. La ruta legacy
`C:\Users\User\Mi unidad\RAUL\` es una cueva muerta (no sincroniza).

| Canal | Ruta filesystem (PC) | Para qué |
|---|---|---|
| **Inbox del Owner** | `G:\Mi unidad\RAUL\01-inbox\01-owner-to-raul\` | Aquí **dejas** tareas desde el celular |
| **Outbox del Owner** | `G:\Mi unidad\RAUL\01-inbox\02-deliverables-to-owner\` | Aquí **recibes** los entregables que Raul produjo en sesión desktop |
| **Tablero de estado** | `G:\Mi unidad\RAUL\01-inbox\_ESTADO.md` | Aquí **consultas** el estado de todo, en un solo archivo |
| Cola de trabajo | `G:\Mi unidad\RAUL\01-inbox\00-cola\` | Interno — InboxBot deja aquí un ticket por ítem capturado; Raul-desktop los consume. No necesitas abrirla; el tablero la resume |

**Mental model remoto = 3 cosas.** Dejas en `01-owner-to-raul/`, recibes
en `02-deliverables-to-owner/`, consultas `_ESTADO.md`. Nada más. Los
canales de gobernanza (decisiones, junta, reguladores, third-parties) y
`03-raw-sources/` **no son parte del mundo remoto** — son desktop/repo.

### 1.2 Cómo dejar una tarea desde el celular

1. App **Google Drive** (la app Drive, no Docs ni Files), cuenta `raoul.bermudez@gmail.com`.
2. Navega a `Mi unidad / RAUL / 01-inbox / 01-owner-to-raul`.
3. "+" → **Subir** o **Crear nuevo**. Cualquier formato sirve para la
   captura — `.txt`/`.md` siguen siendo lo más cómodo, pero ya **no es
   crítico**: InboxBot solo captura el nombre y el tipo; la lectura a fondo
   la hace Raul en sesión desktop con el tooling completo.
4. **Nombre descriptivo**, sin caracteres especiales. Bueno:
   `2026-05-14_GSM_brief_inverter.txt`. Malo: `Doc1`, `Untitled`.
5. **Contenido**, como si me hablaras: qué quieres, para quién, para
   cuándo, qué insumos consultar, agente sugerido si tienes preferencia.

### 1.3 Qué pasa con la tarea — el flujo capture-only

Cuando dejas algo en `01-owner-to-raul/`:

1. **InboxBot** (próximo ciclo, máx ~2h) lo detecta.
2. **Captura** el ítem: crea un `TICKET_*.md` en `00-cola/` con metadata
   (fuente, archivos, tipo, timestamp) + una línea literal. Estado:
   `PENDIENTE-RAUL`. **No lee el contenido a fondo, no interpreta, no
   procesa.**
3. **Acusa recibo:** deja un marcador `CAPTURADO_*.txt` junto a tu archivo
   (significa "capturé y encolé esto" — **no** "está hecho").
4. **Regenera `_ESTADO.md`** — el tablero único con todo lo pendiente.
5. **Prepara un borrador Gmail** ([InboxBot] Ciclo de captura...) con el
   digest. Borrador — no se envía solo.
6. **Loguea el ciclo** en `00-cola/_log-ciclos.md` (heartbeat — incluso si
   no había nada nuevo, deja constancia de que corrió).

**La tarea queda ENCOLADA, no resuelta.** El trabajo real —leer,
delegar, producir el entregable, escribir al repo— ocurre cuando abres
una **sesión desktop**: ahí Raul lee la cola, te muestra el digest, trian
juntos, y produce los entregables reales en `02-deliverables-to-owner/`.

### 1.4 Cuando vuelves al desktop — el ritual de cola

Al abrir una sesión Claude Code, lo primero que hace Raul es **leer la
cola de trabajo** y presentarte un digest: "Desde la última sesión
InboxBot capturó N ítems: [...]. ¿Los triamos?". Para cada ticket que
atiendan, Raul transiciona su estado (`PENDIENTE-RAUL` →
`EN-PROCESO-RAUL` → `RESUELTO`) y produce el entregable real. Si abres
sesión y no mencionas la cola, Raul igual la trae a colación.

### 1.5 Cómo recibir y leer los entregables

App Drive móvil → `Mi unidad / RAUL / 01-inbox / 02-deliverables-to-owner /`.
Markdown lo abre como texto plano (o usa Markor / Obsidian para vista
renderizada); PDF/PPTX se abren nativos; SVG → "Abrir con" → Chrome.

### 1.6 Frecuencia de InboxBot

**Configuración vigente:** cada 2h en ventana **6:00–23:00 Caracas**, 10
disparos diarios. Fuera de esa ventana, en pausa. Routine `raul-inboxbot`,
trigger `trig_01RgGGbpCvckUzSwkyGMDNtm`, cron UTC
`0 0,2,3,10,12,14,16,18,20,22 * * *`. Gestión vía `/schedule` o el panel
de Routines.

**Prompt del Routine** (no cambió con el rediseño v5.0 — solo cambió lo
que el algoritmo hace al disparar):

```
Ejecuta InboxBot. Lee y sigue C:\RAUL\.claude\agents\inboxbot\AGENT.md
```

| Escenario | Intervalo | Ventana |
|---|---|---|
| Operación normal (default) | 2 h | 6:00–23:00 |
| Varias tareas urgentes desde celular | 1 h | 6:00–23:00 |
| Baja actividad / vacaciones | 4 h o pausar | 8:00–20:00 |

### 1.7 Verificar que InboxBot está vivo

1. Sube un `.txt` mínimo a `01-owner-to-raul/`.
2. Espera al próximo ciclo (máx ~2h).
3. Verifica:
   - Aparece un `TICKET_*.md` nuevo en `00-cola/`.
   - Aparece un `CAPTURADO_*.txt` junto a tu archivo.
   - `_ESTADO.md` se regeneró (timestamp reciente, tu ítem en "Cola del Owner").
   - Hay una fila nueva en `00-cola/_log-ciclos.md`.
   - Hay un borrador Gmail `[InboxBot] Ciclo de captura...`.
4. Si algo falla → revisar `00-cola/_log-ciclos.md` (el heartbeat
   distingue "no había nada" de "el trigger no disparó").

### 1.8 Errores comunes

| Síntoma | Causa probable | Solución |
|---|---|---|
| Dejé una tarea y no aparece ticket tras 2h+ | Routine inactiva, o archivo en cueva legacy | Verificar Routines; usar siempre la app Drive (ruta `G:\Mi unidad\`) |
| El ticket existe pero sigue `PENDIENTE-RAUL` hace días | Normal — no hubo sesión desktop aún | El procesamiento real espera a que abras sesión. `_ESTADO.md` lo destaca como "añejo" si pasa el umbral |
| Veo `_log-ciclos.md` con filas pero "ítems: 0" | Normal — InboxBot corrió y no había nada nuevo | Ninguna — el heartbeat es por diseño |
| Esperaba un entregable y no está | InboxBot no produce entregables — solo captura | El entregable lo produce Raul en sesión desktop. Revisa el estado del ticket en `_ESTADO.md` |

---

## Parte 2 — Trabajo con colaboradores vía RAUL/colaboradores

### 2.1 Qué es

Estructura de Drive compartido entre el Owner y cada colaborador externo.
Cada colaborador tiene su carpeta en
`RAUL/colaboradores/<Dominio>/<Nombre-Apellido>/` con **tres subcarpetas
fijas**:

```
<Nombre-Apellido>/
├── 01_De_<Nombre>_Para_Raoul/   ← el colaborador deja cosas para el Owner
├── 02_De_Raoul_Para_<Nombre>/   ← el Owner deja cosas para el colaborador
└── 03_Archivo/                   ← histórico de mensajes ya procesados
```

Convención desde la perspectiva del nombre: `01_De_X_Para_Raoul` = "de X
hacia Raoul", `02_De_Raoul_Para_X` = "de Raoul hacia X".

### 2.2 Estructura actual

**Genteca** (`RAUL/colaboradores/Genteca/`): Oswaldo, Ana-Mendez,
Liliam-Ramirez, Rhinoska-Celis, Valeria-Ostos, Julio-Heredia, Cora-Urrea.
Más `_memoria-tareas-pendientes/` (carpeta especial, no es colaborador —
prefijo `_`).

**Academicos** (`RAUL/colaboradores/Academicos/`): Daniel-Rubio.

(Emails y roles en la memoria `reference_genteca_contacts.md`. IDs de
carpetas Drive en `reference_drive_exchange_ids.md`.)

> **Nota de higiene 2026-05-14:** `Daniel-Rubio/` tiene la subcarpeta del
> Owner mal nombrada (`01_De_Raoul_Para_Daniel` — debería ser
> `02_De_Raoul_Para_Daniel`). Pendiente de corrección manual del Owner —
> ver el cierre del incidente
> `incidents/2026-05-13_inboxbot_phantom-writes-and-scope-overreach.md`.

### 2.3 Cómo se capturan los archivos de un colaborador

InboxBot escanea **todos** los `01_De_X_Para_Raoul/` de todos los
dominios igual que escanea el inbox del Owner. Cuando un colaborador deja
un archivo:

1. InboxBot lo **captura** como un ticket (`fuente: colaborador:<nombre>`)
   en `00-cola/`, igual que un ítem del Owner.
2. La actividad del colaborador aparece en la sección "Actividad de
   colaboradores" del `_ESTADO.md` — así el Owner ve, en un solo lugar,
   qué llegó de quién sin abrir carpeta por carpeta.
3. El procesamiento real (leer, delegar, producir respuesta) lo hace Raul
   en sesión desktop. El entregable, si lo hay, lo escribe Raul en el
   `02_De_Raoul_Para_<X>/` del colaborador.

**InboxBot nunca escribe en `02_De_Raoul_Para_X/`** — eso es de Raul-desktop.
**InboxBot nunca infiere el dominio** desde la ubicación de la carpeta
(la ubicación no es contrato — incidente Cora 2026-05-13). Solo etiqueta
el ticket con la fuente; el dominio lo decide Raul desde el contenido.

### 2.4 Onboarding de un colaborador nuevo

1. Crear `RAUL/colaboradores/<Dominio>/<Nombre-Apellido>/` con las tres
   subcarpetas `01_De_<Nombre>_Para_Raoul/`, `02_De_Raoul_Para_<Nombre>/`,
   `03_Archivo/`.
2. Compartir **solo esa carpeta** (no el folder maestro ni el de dominio):
   - **Nominativa (preferida):** email del colaborador → Editor. Aplica
     cuando el dominio acepta shares externos (Gmail personal, grupompr.com).
   - **Por link (fallback):** "Cualquiera con el enlace" → Editor. Para
     dominios que bloquean shares nominativos a externos (caso Genteca).
3. Enviar el instructivo copiable (§2.6).
4. Registrar en `colaboradores.md` y anotar el ID de carpeta en
   `reference_drive_exchange_ids.md`.

### 2.5 Flujo del día a día

**Owner pide algo:** deja el archivo en `02_De_Raoul_Para_<X>/`, avisa por
WhatsApp/email (Drive no notifica solo). El colaborador trabaja y sube la
respuesta a `01_De_<X>_Para_Raoul/`.

**Colaborador inicia:** sube a `01_De_<X>_Para_Raoul/`, avisa al Owner.
InboxBot lo captura en el próximo ciclo; Raul lo procesa en sesión desktop.

### 2.6 Instructivo COPIABLE para el colaborador

---

> **Asunto: Acceso a tu carpeta compartida — sistema RAUL/colaboradores**
>
> Hola [Nombre],
>
> Te compartí una carpeta en mi Google Drive llamada `[Tu-Nombre]`. La uso
> para intercambiar archivos contigo de forma ordenada.
>
> Dentro verás tres subcarpetas:
>
> - **`01_De_[TuNombre]_Para_Raoul/`** — aquí **tú me dejas cosas a mí**.
>   Lo que subas aquí me llega.
> - **`02_De_Raoul_Para_[TuNombre]/`** — aquí **yo te dejo cosas a ti**
>   (briefs, documentos para revisar, archivos para tu trabajo).
> - **`03_Archivo/`** — histórico de lo ya procesado. No necesitas tocarlo.
>
> ## Cómo trabajar
>
> 1. **Cuando yo te pida algo:** lo encuentras en `02_De_Raoul_Para_...`,
>    trabajas, y subes la respuesta a `01_De_..._Para_Raoul`. Avísame por
>    WhatsApp/email cuando termines.
> 2. **Cuando quieras enviarme algo:** súbelo a `01_De_..._Para_Raoul` y
>    avísame. No hace falta esperar a que te pida nada.
> 3. **Nombres de archivo:** usa fecha `YYYY-MM-DD` al inicio si son
>    versiones (ej. `2026-05-14_propuesta-v2.pdf`).
> 4. **No borres archivos viejos** — yo me encargo del archivado.
>
> ## Lo que NO debes hacer
>
> - No compartas la carpeta con terceros sin avisarme.
> - No subas información sensible no pensada para mí (contraseñas, PII).
> - No renombres las subcarpetas — el sistema automatizado las busca por
>   nombre exacto.
>
> Drive no avisa por defecto de archivos nuevos; revisa cuando te escriba.
>
> Saludos,
> Raoul Bermúdez

---

### 2.7 Reglas de seguridad y orden

1. Cada colaborador ve **solo su propia carpeta**. Nunca compartir el
   folder maestro ni el de dominio.
2. No mezclar dominios en una carpeta de colaborador.
3. Documentos confidenciales (legales, financieros) van en folders
   dedicados, no en folders de colaborador.
4. Auditoría de accesos cada ~6 meses.
5. Offboarding: revocar acceso → mover a
   `RAUL/colaboradores/_archived/<Nombre>_offboarded_YYYY-MM-DD/` →
   registrar en `colaboradores.md`.

### 2.8 Bridge con almacenamiento corporativo del colaborador

Algunos colaboradores trabajan en sistemas corporativos (SharePoint, Box)
que el sistema /RAUL/ **no puede leer**. La solución: el **Owner opera el
bridge manualmente** — descarga del sistema corporativo y copia a la
carpeta `01_De_<X>_Para_Raoul/` del colaborador en Drive.

**Caso de referencia:** SharePoint Genteca compartido con Liliam Ramírez.
Liliam trabaja en SharePoint; el Owner descarga lo que necesita procesar y
lo copia a `colaboradores/Genteca/Liliam-Ramirez/01_De_Liliam_Para_Raoul/`.
SharePoint es source-of-truth; la copia en Drive es staging.

---

## Parte 3 — Resumen accionable

### Para el Owner desde el celular (modo remoto)

1. **Dejar tareas** → app Drive → `Mi unidad/RAUL/01-inbox/01-owner-to-raul/`.
2. **Consultar estado** → `Mi unidad/RAUL/01-inbox/_ESTADO.md` — un solo
   archivo con todo: cola del Owner, actividad de colaboradores, flags.
3. **Recibir entregables** → `Mi unidad/RAUL/01-inbox/02-deliverables-to-owner/`.
4. **Aviso por Gmail** → Borradores → `[InboxBot]`.

   Recuerda: lo que dejas remotamente queda **encolado**, no resuelto. El
   trabajo real espera a tu próxima sesión desktop.

### Para el Owner en el desktop (modo desktop)

1. Abrir sesión Claude Code → Raul lee la cola y te muestra el digest.
2. Triar los tickets pendientes, procesar los que toquen.
3. Raul produce los entregables reales y transiciona el estado de los tickets.

### Para colaboradores

1. **Envían** al Owner en `01_De_<X>_Para_Raoul/`.
2. **Reciben** del Owner en `02_De_Raoul_Para_<X>/`.
3. Aviso por canal externo (Drive no notifica solo).

### Rutas que NO se usan

- `C:\Users\User\Mi unidad\RAUL\` (cueva legacy Backup & Sync).
- `C:\Users\User\OneDrive\RAUL\` (OneDrive no es canal del sistema).

---

*Documento mantenido en* `C:\RAUL\04-system\03-governance\OPERATIVA-REMOTA-Y-COLABORADORES.md`. *Cambios en rutas, frecuencia o convenciones se actualizan aquí + se reflejan en `inboxbot/AGENT.md` y `raul/AGENT.md` si aplica.*
