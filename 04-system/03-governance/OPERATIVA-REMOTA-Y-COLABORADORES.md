# Instructivo operativa remota /RAUL/ — Owner desde celular + RAUL-Exchange con colaboradores

**Versión:** 1.0
**Fecha:** 2026-05-04
**Aplica a:** Owner (Raoul Bermúdez) + colaboradores Genteca/Panamá/futuros dominios.

Este documento responde tres preguntas operativas del día a día:

1. ¿Dónde coloco las tareas para que el sistema /RAUL/ las procese cuando estoy fuera del PC?
2. ¿Dónde recibo los entregables que el sistema produce?
3. ¿Cómo trabajo con los colaboradores externos vía Drive (RAUL-Exchange)?

---

## Parte 1 — Operación remota Owner ↔ /RAUL/ (desde celular)

### 1.1 Canales canónicos vivos

Toda la operación del sistema /RAUL/ desde fuera del PC corre sobre **Google Drive**, en la cuenta personal `raoul.bermudez@gmail.com`. OneDrive **no es canal de InboxBot** y la ruta legacy `C:\Users\User\Mi unidad\RAUL\` es una cueva muerta (no sincroniza con la nube).

| Canal | Ruta filesystem (PC) | Equivalente en app móvil Drive |
|---|---|---|
| **Inbox del Owner (tú colocas tareas aquí)** | `G:\Mi unidad\RAUL\01-inbox\01-owner-to-raul\` | `Mi unidad/RAUL/01-inbox/01-owner-to-raul/` |
| **Outbox del Owner (entregables del sistema)** | `G:\Mi unidad\RAUL\01-inbox\02-deliverables-to-owner\` | `Mi unidad/RAUL/01-inbox/02-deliverables-to-owner/` |
| **Archivado de tareas procesadas** | `G:\Mi unidad\RAUL\01-inbox\01-owner-to-raul\_archived\` | (visible desde móvil — referencia histórica) |

### 1.2 Cómo dejar una tarea desde el celular

**Pasos:**

1. Abre la app **Google Drive** en el celular (no Google Docs ni Files, la app Drive específica).
2. Verifica que estás logueado en la cuenta `raoul.bermudez@gmail.com`.
3. Navega a `Mi unidad / RAUL / 01-inbox / 01-owner-to-raul`.
4. Toca el botón "+" abajo a la derecha → **Subir** (o **Crear nuevo**).
5. **Formato preferido:** `.txt` o `.md` directos.
   - Apps recomendadas para escribir en el celular y subir directo a Drive: Markor (Android, gratis), iA Writer, Obsidian móvil, o Bloc de notas Android (que crea `.txt`).
   - Evita "Crear → Documento de Google" si la tarea es texto simple — eso genera un `.gdoc` que es un puntero a Drive web, no un archivo de texto. InboxBot v3.2 puede manejarlo via Drive MCP, pero `.txt`/`.md` es más robusto.
6. **Nombre del archivo:** descriptivo, sin caracteres especiales. Ejemplos buenos:
   - `2026-05-10_GSM_brief_inverter_competencia.txt`
   - `urgente_revisar_email_keiddys.md`
   - Ejemplos malos: `Doc1`, `Untitled`, `nota`.
7. **Contenido del archivo:** redacta la tarea como si me hablaras directamente. Lo más útil:
   - Qué quieres que produzca (entregable concreto).
   - Para quién es (audiencia).
   - Para cuándo (urgencia).
   - Qué insumos debo consultar (rutas, archivos, contactos).
   - Si tienes preferencia por algún agente o formato, dilo.

**Ejemplo de contenido tipo brief:**

```
Tarea: revisar copy del email a Ana Méndez sobre brief MPR

Contexto: Tengo borrador en C:\Raul\03-projects\genteca\... revisarlo y
proponer 2 alternativas — una más directa y otra más diplomática.

Audiencia: Ana Méndez (Genteca, gerente).

Para cuándo: hoy en la tarde si es posible, mañana máximo.

Agente sugerido: Solenne.

Pregunta abierta: ¿debería incluir la mención del CC a Oz o no? Tu juicio.
```

### 1.3 Cómo se procesa la tarea

1. **InboxBot** corre cada **4 horas** (o según frecuencia que tengas configurada en Routines de Claude Code Desktop).
2. Detecta archivos nuevos en `01-owner-to-raul/`, los pasa a Raul (orquestador).
3. Raul delega al agente especialista correspondiente.
4. El resultado se deposita en `02-deliverables-to-owner/` con nombre `YYYY-MM-DD_[agente]_[task_id]_[STATUS].md`.
5. InboxBot crea un `DONE_[task_id].txt` en el inbox y **mueve el archivo fuente** a `_archived/` con prefijo de fecha (v3.2 del agente). El inbox queda limpio.
6. **Gmail draft** se crea automáticamente como aviso (asunto: `[InboxBot] resumen tarea`). Lo encontrarás en tu app Gmail → Borradores.

### 1.4 Cómo recibir y leer los entregables desde el celular

**Pasos:**

1. App Drive móvil → `Mi unidad / RAUL / 01-inbox / 02-deliverables-to-owner /`.
2. Los entregables están organizados por workstream. Cada entrega típica es una carpeta con README de lectura prioritaria.
3. Para abrir Markdown desde el celular:
   - Drive lo abre como texto plano.
   - Para vista renderizada: app Markor (Android), o copia el contenido a Obsidian móvil si quieres edición.
4. Para abrir PDF / PPTX: la app Drive los abre nativamente.
5. Para abrir SVG (mockups Atlas): tap "Abrir con" → Chrome móvil. Renderiza el SVG como imagen.

### 1.5 Frecuencia de InboxBot — cómo ajustarla

**Ubicación:** Claude Code Desktop → Routines.

**Recomendaciones de intervalo:**

| Escenario | Intervalo sugerido |
|---|---|
| Operación normal (default) | 4 h |
| Día con varias tareas urgentes desde celular | 1 h |
| Vacaciones o periodos de baja actividad | 12 h o pausar |

**Prompt recomendado del Routine:**

```
Ejecuta InboxBot. Lee y sigue C:\RAUL\.claude\agents\inboxbot\AGENT.md
```

Ese prompt simple deja a `AGENT.md` como única fuente de verdad. No hardcodear rutas en el Routine — si las rutas cambian (ej. nueva carpeta de canal), solo se actualiza `AGENT.md` y el Routine sigue funcionando.

### 1.6 Verificar que InboxBot está funcionando

**Test sencillo cada cierto tiempo:**

1. Crea desde el celular un `.txt` mínimo en `01-owner-to-raul/` con contenido tipo *"Test InboxBot YYYY-MM-DD: si lees esto, responde con ack."*.
2. Espera al próximo ciclo (max 4 h con configuración default).
3. Verifica:
   - El `.txt` debe haberse movido a `_archived/` con prefijo de fecha.
   - Debe existir `DONE_test-inboxbot-YYYY-MM-DD.txt` en el inbox.
   - Debe existir entregable en `02-deliverables-to-owner/`.
   - Debe existir borrador Gmail con asunto `[InboxBot] Test InboxBot`.
4. Si alguno de los tres falla → revisar `C:\Raul\04-system\03-governance\inboxbot-tasklog.md` para diagnosticar.

### 1.7 Errores comunes y soluciones

| Síntoma | Causa probable | Solución |
|---|---|---|
| Tarea colocada desde celular no se procesa después de 4 h | Routine no está activa o frecuencia mayor | Verificar Routines en Claude Code Desktop |
| Tarea aparece en G: pero queda sin DONE marker | El archivo es `.gdoc` y Drive MCP no estaba disponible | Subir como `.txt`/`.md` o ejecutar manualmente |
| No veo entregable en el celular | Drive no terminó de sincronizar | Forzar sync (jalar hacia abajo en la app Drive) |
| InboxBot no encuentra el archivo aunque lo veo en G: | Cargaste el archivo en `C:\Users\User\Mi unidad\` (cueva legacy) | Usar siempre app Drive móvil o ruta `G:\Mi unidad\` desde PC |

---

## Parte 2 — Trabajo con colaboradores vía RAUL-Exchange

### 2.1 Qué es RAUL-Exchange

**RAUL-Exchange** es la estructura de Drive compartido entre el Owner y cada colaborador externo (empleado de Genteca, contratista, contraparte de Panamá, etc.). Existe como una jerarquía de carpetas en la cuenta `raoul.bermudez@gmail.com`, donde cada colaborador tiene su propia carpeta con dos sub-canales: `inbox` y `outbox`.

**Convención de nombres (importante):**

- **`outbox/` del colaborador**: Owner deposita archivos para que el colaborador los descargue. El colaborador ve este folder como **"recibido del Owner"**.
- **`inbox/` del colaborador**: Colaborador deposita archivos para que el Owner los reciba. El colaborador ve este folder como **"para enviar al Owner"**.

Esta convención es desde la perspectiva del **Owner que pone/recibe**. Para el colaborador, es invertido (lo que está en `outbox` es lo que él recibe; lo que está en `inbox` es lo que él envía).

### 2.2 Estructura actual

**Genteca** (root: `RAUL-Exchange/Genteca/`):

| Persona | Email | Carpeta personal |
|---|---|---|
| Oz | ogutierrez@genteca.com.ve | `Oz/inbox/`, `Oz/outbox/` |
| Ana Méndez | amendez@genteca.com.ve | `Ana-Mendez/inbox/`, `Ana-Mendez/outbox/` |
| Liliam Ramírez | lramirez@genteca.com.ve | `Liliam-Ramirez/inbox/`, `Liliam-Ramirez/outbox/` |
| Rhinoska Celis | Rcelis@genteca.com.ve | `Rhinoska-Celis/inbox/`, `Rhinoska-Celis/outbox/` |
| Valeria Ostos | vostos@genteca.com.ve | `Valeria-Ostos/inbox/`, `Valeria-Ostos/outbox/` |
| Julio Heredia | jheredia@genteca.com.ve | `Julio-Heredia/inbox/`, `Julio-Heredia/outbox/` |
| Cora Urrea | cora.urrea@gmail.com | `Cora-Urrea/inbox/`, `Cora-Urrea/outbox/` |
| MPR Juan de Abreu | jdeabreu@grupompr.com | `MPR-JuanDeAbreu/inbox/`, `MPR-JuanDeAbreu/outbox/` |

**Panamá** (root: `RAUL-Exchange/Panama/`):

| Carpeta | Uso |
|---|---|
| `EmbassyClub/inbox/` y `outbox/` | Intercambio operativo apartamento |
| `Contratos/` | Documentos legales |
| `Finanzas/` | Estados, recibos |
| `Reparaciones/` | Cotizaciones, fotos, facturas |
| `Analisis-Mercado/` | Investigación inmobiliaria |

(IDs específicos de cada carpeta están en memoria persistente: `reference_drive_exchange_ids.md`).

### 2.3 Cómo onboardear a un colaborador nuevo

**Pasos del Owner:**

1. **Crear carpeta personal** en `RAUL-Exchange/[Dominio]/[Nombre-Apellido]/` con dos subcarpetas: `inbox/` y `outbox/`.
   - Nombrado: capitalizado y guion, sin espacios. Ej: `Maria-Lopez`.
   - Si requiere convención de domain pack: `RAUL-Exchange/Genteca/Maria-Lopez/`.
2. **Compartir SOLO esa carpeta** con el colaborador desde Drive web:
   - Click derecho en la carpeta `Maria-Lopez/` → Compartir → introducir email del colaborador → permiso **Editor** (puede subir y descargar) → Enviar.
   - **No compartas el folder maestro `RAUL-Exchange/`** ni el folder del dominio. Solo la carpeta de la persona — así no ve carpetas de otros colaboradores.
3. **Enviar al colaborador el instructivo del colaborador** (sección 2.5 abajo, copiable como email o PDF).
4. **Registrar la relación** en `C:\Raul\04-system\03-governance\colaboradores.md` (crear si no existe) con: nombre, email, carpeta, dominio, fecha de onboarding, propósito del intercambio.
5. Confirmar que la memoria persistente `reference_drive_exchange_ids.md` tiene el ID de la nueva carpeta. Si no, anotarlo manualmente la próxima sesión Claude Code.

### 2.4 Flujo del día a día con un colaborador

**Caso A — Owner pide algo al colaborador:**

1. Owner deposita archivo en **`outbox/` del colaborador** (ej. brief, documento a revisar, planilla).
2. Owner avisa al colaborador (email, WhatsApp, Slack — fuera de Drive). Drive no notifica automáticamente cambios en folders compartidos a no ser que el colaborador active alertas.
3. Colaborador descarga, trabaja, sube respuesta al **`inbox/`** del mismo folder.
4. Owner revisa cuando el colaborador avisa que terminó.
5. Owner mueve el archivo a un folder de archivado interno o lo procesa según corresponda.

**Caso B — Colaborador inicia intercambio (ej. envía documento espontáneo):**

1. Colaborador sube a su **`inbox/`** (su perspectiva: "estoy enviando esto al Owner").
2. Colaborador avisa al Owner.
3. InboxBot puede recoger archivos del `inbox/` de colaboradores **si AGENT.md tiene ese canal activo** (línea 18 de AGENT.md: "Activo (cuando exista la subcarpeta)").
4. Si InboxBot lo procesa: el archivo se mueve a `_archived/` dentro del `inbox/` del colaborador y un DONE marker aparece allí.
5. Si requiere acción del Owner: el resultado va al outbox del Owner como entregable normal.

### 2.5 Instructivo COPIABLE para enviar al colaborador

(Texto que el Owner puede copiar a un email o PDF cuando comparta la carpeta con un nuevo colaborador.)

---

> **Asunto: Acceso a tu carpeta compartida — sistema RAUL-Exchange**
>
> Hola [Nombre],
>
> Te he compartido una carpeta en mi Google Drive llamada `[Tu-Nombre]`. La uso para intercambiar archivos contigo de forma organizada — más limpio que email para documentos grandes o múltiples versiones.
>
> ## Cómo funciona
>
> Dentro de tu carpeta verás dos subcarpetas:
>
> - **`outbox/`** — aquí yo te dejo cosas. Lo que veas aquí es **lo que recibes de mí** (briefs, documentos para revisar, planillas, archivos para tu trabajo).
> - **`inbox/`** — aquí tú me dejas cosas. Lo que subas aquí **me llega a mí**.
>
> Piénsalo así:
> - **`outbox/` = "lo que sale de mí hacia ti"**
> - **`inbox/` = "lo que entra a mí desde ti"**
>
> ## Cómo trabajar
>
> 1. **Cuando yo te pida algo:** revisas `outbox/`, descargas el archivo, trabajas, y subes la respuesta a `inbox/`. Avísame por WhatsApp / email cuando termines.
> 2. **Cuando tú quieras enviarme algo:** súbelo a `inbox/` y avísame. No hace falta que esperes a que yo te pida nada.
> 3. **Nombres de archivo:** usa fechas YYYY-MM-DD al inicio si son versiones (ej. `2026-05-10_propuesta-v2.pdf`). Ayuda a no confundir versiones.
> 4. **No hace falta borrar archivos viejos** — yo me encargo del archivado. Pero si quieres limpiar lo tuyo, puedes.
>
> ## Lo que NO debes hacer
>
> - No compartas la carpeta con terceros sin avisarme.
> - No subas información sensible que no esté pensada para mí (PII, contraseñas, etc.).
> - No cambies el nombre de las subcarpetas `inbox/` y `outbox/` — el sistema automatizado las busca por nombre exacto.
>
> ## Notificaciones
>
> Drive no avisa por defecto cuando hay archivos nuevos. Si quieres recibir notificación:
> - En Drive web → click derecho en la carpeta → Configuración → Activar notificaciones.
> - O simplemente revisa cuando te avise por WhatsApp / email.
>
> Cualquier duda, escríbeme.
>
> Saludos,
> Raoul Bermúdez

---

### 2.6 Reglas de seguridad y orden

1. **Cada colaborador ve SOLO su propia carpeta.** Nunca compartir `RAUL-Exchange/` ni el folder de dominio.
2. **No mezclar dominios** dentro de una carpeta de colaborador. Si Ana Méndez trabaja para Genteca, su carpeta vive en `RAUL-Exchange/Genteca/Ana-Mendez/`. Si en algún futuro trabaja también para Plenus, se crea folder separado `RAUL-Exchange/Plenus/Ana-Mendez/`.
3. **Documentos confidenciales** (legales, financieros) van en folders dedicados (ej. `Panama/Contratos/`), no en folders de colaborador, porque los folders de colaborador son territorio compartido.
4. **Auditoría periódica** (sugerido cada 6 meses): revisar quién tiene acceso a qué desde Drive web → Configuración compartida. Revocar accesos de personas que ya no colaboran.
5. **Ofboarding:** cuando un colaborador deja la organización: revocar acceso desde Drive web → mover su carpeta a `RAUL-Exchange/_archived/[Nombre]_offboarded_YYYY-MM-DD/` → registrar en `colaboradores.md`.

### 2.7 Diferencia entre inbox del Owner (Parte 1) e inbox de colaborador

**Importante no confundir:**

| Folder | Quién deposita | Quién lee | Procesado por InboxBot? |
|---|---|---|---|
| `Mi unidad/RAUL/01-inbox/01-owner-to-raul/` | Owner (yo) | InboxBot → Raul → especialistas | Sí, default cada 4 h |
| `RAUL-Exchange/[Dominio]/[Nombre]/inbox/` | Colaborador | InboxBot (si activo) → Raul → ... | Sí, si AGENT.md tiene activado canal colaboradores |
| `RAUL-Exchange/[Dominio]/[Nombre]/outbox/` | Owner (manualmente) o Raul (vía InboxBot tras procesar) | Colaborador (lee desde Drive web/móvil) | No procesa, solo deposita |

El inbox del Owner es el **canal directo de tareas tuyas**. Los inbox de colaboradores son canales **para que ellos te envíen cosas a ti** (no son tareas tuyas, son insumos externos que tú decidirás qué hacer con ellos).

---

## Parte 3 — Resumen accionable de una sola página

### Para el Owner desde el celular

1. **Tareas para el sistema** → app Drive móvil → `Mi unidad/RAUL/01-inbox/01-owner-to-raul/` → subir `.txt` o `.md`.
2. **Recibir entregables** → app Drive móvil → `Mi unidad/RAUL/01-inbox/02-deliverables-to-owner/` → buscar carpeta con fecha más reciente → leer `00_README_lee_primero.md`.
3. **Aviso por Gmail** → app Gmail → Borradores → buscar `[InboxBot]`.

### Para colaboradores (desde su Drive)

1. **Reciben** archivos del Owner en su `outbox/`.
2. **Envían** archivos al Owner en su `inbox/`.
3. Aviso por canal externo (WhatsApp/email), Drive no notifica por sí mismo.

### Rutas que NO debes usar

- `C:\Users\User\Mi unidad\RAUL\` (cueva legacy Backup & Sync)
- `C:\Users\User\OneDrive\RAUL\` (OneDrive no es canal del sistema)

### Frecuencia de InboxBot

- Default 4 h. Configurable en Claude Code Desktop → Routines.
- Test sencillo cada cierto tiempo (sección 1.6) para verificar que sigue vivo.

---

*Documento mantenido en* `C:\Raul\04-system\03-governance\OPERATIVA-REMOTA-Y-COLABORADORES.md`. *Cualquier cambio sustantivo en rutas, frecuencia o convenciones se actualiza aquí + se refleja en `inboxbot/AGENT.md` si aplica.*
