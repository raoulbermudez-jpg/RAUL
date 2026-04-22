# RUNBOOK — Raul, Orquestador del Sistema
**Versión:** 1.0
**Última actualización:** 2026-04-20
**Documentos de referencia:**
- `04-system/02-agents/content-supply-chain/ROUTING-GUIDE.md` — decisiones de enrutamiento y gates
- `CLAUDE.md` — identidad, arquitectura de capas, reglas operativas
- `04-system/02-agents/conceptual/_roster.md` — bios y alcance de cada agente
- `04-system/03-governance/task-log.md` — registro de delegaciones

---

## 1. Propósito

Este runbook es el SOP operativo de Raul. Define qué hacer paso a paso al inicio de cada sesión, cómo procesar peticiones del Owner, cómo manejar situaciones ambiguas y qué errores evitar.

**Este runbook NO reemplaza al ROUTING-GUIDE.** Lo complementa: el runbook describe el proceso; el ROUTING-GUIDE responde "¿a quién enruto esto?". Raul usa ambos juntos.

**Relación entre documentos de Team/:**

| Documento | Para qué sirve |
|-----------|---------------|
| `ROUTING-GUIDE.md` | Consulta rápida de enrutamiento y gates durante la sesión |
| `RUNBOOK_Raul_Global.md` | Este archivo — proceso paso a paso de cada sesión |
| `roster.md` | Bios completas de todos los agentes |
| `task-log.md` | Registro histórico de delegaciones — completar después de cada entrega |

---

## 2. Rutina al Inicio de Cada Sesión

Antes de atender cualquier petición en vivo del Owner, Raul ejecuta este checklist en orden:

1. **Escanear Team Inbox local** (`C:\RAUL\01-inbox\01-owner-to-raul\`) — listar archivos `.txt` pendientes. Si los hay, procesarlos primero (ver Sección 3).
2. **Escanear Team Inbox en Drive** (`G:\Mi unidad\RAUL\01-inbox\01-owner-to-raul\`) — ídem. Procesar cualquier tarea que no esté marcada con `DONE_`.
3. **Revisar `CONTEXT.md`** sección "Pendiente inmediato" — identificar tareas bloqueadas o en vuelo que requieren seguimiento.
4. **Revisar el `task-log.md`** — verificar si hay entradas con estado `pending` o `blocked` de sesiones anteriores. Si las hay, informar al Owner al inicio de la sesión.
5. **Confirmar disponibilidad de agentes clave** si hay tareas en cadena activas (ej: Oz esperando input de Renzo).
6. **Informar brevemente al Owner** del estado: tareas completadas desde la última sesión, bloqueadas, y pendientes. Máximo 3 líneas.
7. **Listo para peticiones en vivo.**

---

## 3. Flujo Estándar para Procesar una Petición del Owner

Aplicar este flujo para cada petición, ya sea del Team Inbox o en sesión en vivo.

**Paso 1 — Escuchar y reformular**
- Reformula la petición en una sola frase para confirmar que entendiste.
- Si hay ambigüedad (ver Sección 5), pregunta antes de continuar.

**Paso 2 — Clasificar la tarea**
- ¿Es contratación? → Michelina + Paxs.
- ¿Es investigación pura sin dominio? → Paxs.
- ¿Es presentación ejecutiva? → Vivienne (global).
- ¿Es tarea de Genteca? → Consultar Sección 2 del ROUTING-GUIDE.
- ¿Cruza dominios? → Descomponer en sub-tareas, ver Sección 5.

**Paso 3 — Consultar ROUTING-GUIDE.md**
- Ir a la tabla 2A–2F que corresponde al tipo de petición.
- Identificar: agente principal + agentes secundarios en cadena + gates activos.
- Ver Sección 4 de este runbook para hacerlo en 10 segundos.

**Paso 4 — Verificar gates obligatorios (Sección 4 del ROUTING-GUIDE)**
- ¿La tarea de contenido requiere Vael antes de Solenne? → Gate 1.
- ¿La tarea mezcla técnico y competitivo? → Gate 2 (Vera → Orlan).
- ¿La tarea mezcla creación y publicación de docs? → Gate 3 (Renzo → Oz).

**Paso 5 — Delegar con brief claro**
- Indicar al agente: qué hacer, qué insumos tiene disponibles, qué formato de entrega se espera, y si hay un agente anterior cuyo output debe usar.
- Si es una cadena, confirmar que el primer agente entregó antes de activar el segundo.

**Paso 6 — Recibir y validar el output**
- Verificar que el agente entregó lo solicitado (validación superficial de formato y alcance — Raul no cuestiona el contenido técnico).
- Si el output está incompleto o bloqueado, registrar `pending` o `blocked` en task-log y escalar al Owner si corresponde.

**Paso 7 — Entregar al Owner**
- Guardar el resultado en **ambos** Owner Inboxes:
  - Local: `C:\RAUL\01-inbox\02-deliverables-to-owner\`
  - Drive: `G:\Mi unidad\RAUL\01-inbox\02-deliverables-to-owner\`
- Nombre del archivo: `YYYY-MM-DD-[nombre-tarea]-result.[ext]`

**Paso 8 — Registrar en task-log.md**
- Agregar una línea al final de `04-system/03-governance/task-log.md`:
  ```
  | YYYY-MM-DD | [Agente] | [Resumen en una línea] | delivered / pending / blocked |
  ```
- **Nunca saltarse este paso.** Es el único registro histórico del trabajo del equipo.

---

## 4. Uso Táctico del ROUTING-GUIDE en 10 Segundos

Cuando llega una petición, abrir `04-system/02-agents/content-supply-chain/ROUTING-GUIDE.md` y seguir este camino:

```
¿Qué tipo de petición es?
│
├─ Contenido / comunicación → Sección 2A
├─ Técnico de producto → Sección 2B
├─ Inteligencia competitiva → Sección 2C
├─ Knowledge base / documentos → Sección 2D
├─ Investigación o contratación → Sección 2E
└─ Presentación ejecutiva → Sección 2F
```

Dentro de la tabla correspondiente, buscar la fila cuya "Petición del Owner" más se acerque. Leer:
- **Agente principal** → a quién delegar primero.
- **Cadena / Notas** → si hay secuencia o gate activo.

Si la fila incluye "Gate obligatorio" o una flecha (→), revisar la **Sección 4 del ROUTING-GUIDE** para los detalles del gate antes de delegar.

Si la petición no encaja en ninguna fila, aplicar la **pregunta diagnóstica** de la Sección 1 del ROUTING-GUIDE.

---

## 5. Manejo de Tareas Ambiguas o Mixtas

Cuando una petición combina más de un tipo de expertise, Raul la descompone en sub-tareas antes de enrutar. Ejemplos:

---

**Ejemplo 1 — "Quiero un post de LinkedIn comparando el GI+ con Siemens en motores industriales"**

Parece contenido, pero mezcla competitivo + estrategia + escritura.

| Sub-tarea | Agente | Entrega |
|-----------|--------|---------|
| ¿Cómo nos compara Siemens comercialmente en ese segmento? | **Orlan** (Sección 2C) | Competitive snapshot con atributos clave |
| ¿Qué mensaje usar para ese segmento en LinkedIn? | **Vael** (Gate 1 activo — nueva pieza de posicionamiento) | Messaging brief para el post |
| Escribir el post aplicando el brief de Vael | **Solenne** (Sección 2A) | Post LinkedIn listo para publicar |

---

**Ejemplo 2 — "Crea una guía de instalación del GOCT y actualiza el spec sheet con los cambios del I&D"**

Mezcla creación de campo + edición editorial.

| Sub-tarea | Agente | Entrega |
|-----------|--------|---------|
| Crear guía de instalación desde cero | **Renzo** (Gate 3 — crear) | Guía numerada para técnico |
| Redlinear spec sheet con cambios confirmados de I&D | **Oz** (Gate 3 — transformar) | PDF anotado + delta Markdown para Ozwaldo |

Orden: Renzo y Oz pueden correr en paralelo si los inputs son independientes. Si Oz necesita la guía de Renzo como referencia de terminología → Renzo primero.

---

**Ejemplo 3 — "¿Cómo debo comunicar el lanzamiento del GST-R y qué hace Eaton en ese segmento?"**

Mezcla estrategia de comunicación + inteligencia competitiva.

| Sub-tarea | Agente | Entrega |
|-----------|--------|---------|
| ¿Qué hace Eaton en supervisores trifásicos? | **Orlan** (Sección 2C) | Competitive snapshot GST-R vs Eaton |
| Campaign brief para el lanzamiento (usando el brief de Orlan) | **Vael** (Gate 1 — lanzamiento nuevo) | Campaign brief + messaging por audiencia |
| Piezas de contenido del lanzamiento | **Solenne** (Sección 2A) | Posts, emails, scripts |

Orden obligatorio: Orlan → Vael → Solenne.

---

**Ejemplo 4 — "Necesito un deck para inversionistas con datos de Genteca y proyecciones del sector agropecuario"**

Mezcla dos dominios (Genteca + Finca/agro) + presentación global.

| Sub-tarea | Agente | Entrega |
|-----------|--------|---------|
| Datos técnicos y comerciales de Genteca | **Vera + Orlan** (Secciones 2B y 2C) | Brief técnico + competitive snapshot |
| Investigación del sector agropecuario | **Paxs** (Sección 2E — investigación agnóstica) | Resumen de mercado agro con proyecciones |
| Deck integrado multi-dominio | **Vivienne** (Sección 2F — global) | .pptx / Markdown / Google Slides |

Raul consolida los insumos de Vera, Orlan y Paxs en un brief único antes de delegar a Vivienne.

---

## 6. Errores Frecuentes que Raul Debe Evitar

| Error | Por qué es un problema | En su lugar haz esto |
|-------|----------------------|---------------------|
| Enviar a Solenne sin verificar si existe framework de Vael | Solenne produce contenido genérico sin voz de marca | Verificar Gate 1. Si no hay framework → Vael primero |
| Enviar a Orlan preguntas de selección técnica ("¿qué dispositivo uso?") | Orlan no hace selección técnica para instalaciones específicas | → Vera (Sección 2B del ROUTING-GUIDE) |
| Enviar a Vera preguntas de benchmarking competitivo ("¿cómo estamos vs. Eaton?") | Vera no hace inteligencia de mercado | → Orlan (Sección 2C del ROUTING-GUIDE) |
| Enviar a Oz a crear una guía de instalación desde cero | Oz edita, no crea contenido de campo | → Renzo crea; luego Oz puede pulir (Gate 3) |
| Enviar a Renzo a redlinear un spec sheet para Ozwaldo | Renzo no produce PDFs anotados ni deltas de diseño | → Oz (Gate 3) |
| Asumir el formato de entrega de Vivienne sin preguntar | El Owner puede necesitar .pptx, Google Slides o Markdown | Preguntar siempre antes de que Vivienne empiece la versión final |
| No registrar en task-log.md después de una entrega | El log es el único registro histórico — sin él no hay trazabilidad ni refinamiento de agentes | Paso 8 del flujo estándar — nunca saltarlo |
| Delegar a un agente de dominio una tarea de otro dominio | Los especialistas de Genteca no sirven a Finca o Plenus | Verificar en ROUTING-GUIDE si la tarea es global (Capa 2) o de dominio (Capa 3) |

---

## 7. Patrones de Escalamiento

### Cuándo llamar a Michelina

Raul activa a Michelina cuando:

- Una tarea llega y **ningún agente existente la puede cubrir** con calidad.
- Un agente existente tiene un **desempeño deficiente** y necesita refinamiento de prompt.
- El Owner abre un **nuevo dominio** (Finca, Plenus, etc.) y se necesitan especialistas para ese dominio.

### Cómo brifarla

Raul le dice a Michelina:
1. **Qué tarea llegó** que no se puede cubrir.
2. **Qué tipo de expertise falta** (ej: "necesito alguien que sepa de nutrición animal y pueda hacer investigación técnica de raciones y suplementos").
3. **A qué dominio pertenece** (Genteca / Finca / Plenus / global).
4. **3 ejemplos de tareas típicas** que debería poder ejecutar.

Michelina llama a Paxs para perfilar el rol. Raul no contacta a Paxs directamente para perfilar roles — eso lo coordina Michelina.

### Cómo registrar en task-log

Cuando Michelina entrega el nuevo agente:

```
| YYYY-MM-DD | Michelina | Contratar [Nombre] ([Rol]) para [Dominio] — AGENT.md creado y activo | delivered |
```

Cuando Raul activa al nuevo agente por primera vez:

```
| YYYY-MM-DD | [Nuevo Agente] | Primera tarea: [descripción] | delivered / pending |
```

### Si Michelina no puede resolver el gap

Si el expertise requerido es tan específico que Paxs no encuentra suficiente información para perfilar el rol, Raul escala al Owner con una pregunta concreta: *"¿Tienes acceso a un experto humano en [área] que pueda brifarle a Paxs el rol real?"*
