# RISK-POLICY.md
## Política de gestión de riesgos — Sistema /RAUL/

**Versión:** 1.0
**Última actualización:** 2026-04-25

---

## 1. Alcance

Esta política aplica a todas las acciones de los agentes y del Owner sobre el sistema /RAUL/: modificaciones de archivos, ejecución de scripts, interacciones con servicios externos (Google Drive, Gmail, GitHub, APIs) y delegaciones a LLMs.

---

## 2. Clasificación de acciones por riesgo

### Zona verde — acción libre

Los agentes pueden ejecutar sin solicitar confirmación:

- Leer cualquier archivo del repo.
- Crear o editar archivos `.md` en `02-knowledge-base/`, `03-projects/`, `04-system/`.
- Crear archivos nuevos en `01-inbox/02-deliverables-to-owner/`.
- Ejecutar scripts de solo lectura o análisis (sin side effects externos).
- Consultar web (Paxs, Orlan, Vera) con queries de investigación.

### Zona amarilla — confirmar antes de ejecutar

Los agentes deben explicitar la acción y esperar aprobación del Owner:

- Ejecutar scripts que escriben en disco fuera de `/RAUL/`.
- Modificar archivos de governance (`DECISIONS.md`, `MIGRATION-PLAN.md`).
- Modificar archivos de configuración de agentes (`AGENT.md`, `CLAUDE.md`).
- Hacer `git push` a `origin`.
- Interactuar con Google Drive (leer o escribir).
- Crear borradores de Gmail.
- Instalar paquetes Python (`pip install`).

### Zona roja — solo con instrucción explícita del Owner

Solo ejecutar si el Owner da la orden directa y explícita:

- `git reset --hard`, `git push --force`, `git branch -D`.
- Eliminar o mover archivos fuera del repo.
- Modificar el trigger de InboxBot o cualquier automatización externa.
- Reconfigurar Google Drive Desktop sync.
- Acceder a credenciales, tokens o archivos `.env`.
- Ejecutar cualquier acción con efecto sobre sistemas de producción o externos irreversibles.

---

## 3. Manejo de errores

- Si un agente encuentra un error inesperado durante una tarea, **para y reporta** antes de intentar autocorrección destructiva.
- Si un script falla, no reintentar con flags que bypass permisos o validaciones (ej. `--force`, `--no-verify`) sin aprobación del Owner.
- Los errores de lectura/escritura de archivos se loguean en el reporte de entrega al Owner Inbox.

---

## 4. Reversibilidad

Antes de ejecutar cualquier acción de Zona Amarilla o Roja, el agente debe evaluar:

1. ¿Es reversible? Si no, explicitar claramente al Owner.
2. ¿Hay un backup o estado guardado? Si no, sugerir crearlo primero.
3. ¿El cambio afecta sistemas compartidos o externos? Si sí, escalar a Zona Roja.

---

## 5. Incidentes

Si ocurre una acción no autorizada o un error con impacto real (archivo borrado, push forzado, datos enviados a servicio externo), el agente debe:

1. Reportar inmediatamente al Owner con detalle de lo ocurrido.
2. Proponer el rollback más seguro disponible.
3. Registrar el incidente en `DECISIONS.md` con lección aprendida.

---

## Notas de versión

- **v1.0 — 2026-04-25** — documento inicial.
