# CLAUDE-CODE-RULES — Proyecto C:\WorkspaceIA\PROJECTS\Claude code

**Versión:** 1.0  
**Última actualización:** 2026-04-20  

**Alcance:** Estas reglas aplican a cómo debe trabajar Claude Code dentro de este repo.  
Complementan a `RUNBOOK_Raul_Global.md` (cómo opera Raul) y `ROUTING-GUIDE.md` (cómo se enrutan tareas).

---

## 1. Principios

- Este repo es el **“cerebro operativo”** del sistema Raul (Team/, .claude/, etc.).  
- Claude Code puede **leer y editar libremente archivos del proyecto**, pero **no debe ejecutar scripts o comandos peligrosos sin confirmación del Owner**.  
- El modo base deseado es equivalente a `acceptEdits`: acelera ediciones de archivos y comandos de filesystem de bajo riesgo.  

---

## 2. Qué Claude Code PUEDE hacer sin preguntar

Dentro de este proyecto (directorio raíz y subcarpetas):

- **Lectura de archivos**
  - Leer cualquier archivo de texto (`.md`, `.txt`, `.json`, `.yaml`, `.py`, etc.).
  - Usar comandos tipo `ls`, `cat`, `grep`, `sed`, `wc` y similares para inspección de contenido y estructura del repo.

- **Edición y creación de archivos**
  - Crear y editar archivos en `Team/`, `.claude/` y el resto del árbol `./**` del proyecto.
  - Operaciones típicas sobre documentación: crear, modificar, renombrar, reorganizar ficheros mientras se mantenga dentro del workspace.

- **Filesystem de bajo riesgo**
  - Usar comandos como `mkdir`, `mv`, `cp`, `rm` **dentro del workspace** para organizar archivos.  
  - No debe intentar operar fuera del directorio del proyecto.

---

## 3. Qué SIEMPRE requiere confirmación explícita (va a ask)

Claude Code **NO debe ejecutar** estos comandos sin un “Yes” manual del Owner:

- **Cualquier script o intérprete:**
  - Comandos que empiecen por `python`, `python3`, `pip`, `node`, `npm`, `npx`, `uv`, `powershell`, `pwsh`, `.ps1`, `.bat`, etc.  
- **Comandos de red o instalación:**
  - `curl`, `wget`, `git push`, instalaciones de paquetes, o cualquier otro comando que toque red o servicios externos.  
- **Operaciones destructivas o irreversibles:**
  - Borrados masivos o peligrosos, por ejemplo patrones tipo `rm -rf`.  
  - Cualquier cosa que pueda afectar credenciales, secretos, `.env` u otros archivos sensibles.

Regla mental:

> Si el comando **“corre cosas”** (interpretes, builds, installs, scripts) o puede romper/mandar datos, Claude debe pedir autorización.

---

## 4. Relación con settings.local.json

En este repo existe un archivo `.claude/settings.local.json` que implementa estas reglas a nivel técnico:

- `allow` incluye, entre otros:
  - Lectura del repo (`Read(./**)`) y de las fuentes RAG de Drive.
  - Escritura en `Team/` y `.claude/`.
  - Edición en `./**`.
  - Comandos Bash de inspección y filesystem de bajo riesgo (`ls`, `grep`, `sed`, `mkdir`, `mv`, `cp`, `wc`, `git status`, etc.).
- `ask` incluye:
  - Comandos Bash que ejecutan código o tocan red (`python`, `pip`, `npm`, `git push`, `curl`, `rm -rf`, etc.).

Si en el futuro se modifica `.claude/settings.local.json`, debe mantenerse alineado con estos principios para que el proyecto siga “sintiéndose” igual de rápido pero seguro.

---

## 5. Uso práctico de estas reglas

- En sesiones normales, Claude puede:
  - Leer y navegar el conocimiento del sistema (Team/, .claude/, RAG_SOURCES) sin fricción.
  - Editar y crear documentación, prompts y archivos internos sin pedir permiso todo el tiempo.
- Cada vez que Claude proponga ejecutar un comando que entra en la zona de `ask`:
  - Debe explicitar el comando completo.
  - Esperar la aprobación del Owner antes de ejecutarlo.

Estas reglas existen para que Raul y Claude Code puedan trabajar rápido sobre el conocimiento del sistema, sin renunciar al control sobre scripts, instalaciones y operaciones de riesgo.
