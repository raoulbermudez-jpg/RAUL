---
document_id: "PKA-AUDIT-CHECKLIST"
document_type: "operational-checklist"
author: "GitHub Copilot (Copilot Chat in VS Code)"
creation_date: "2026-05-08"
purpose: "Proporcionar un checklist operacional para auditar la salud y coherencia del PKA contra sus propios principios"
audience: ["Raoul Bermúdez (Owner)", "Claude Opus 4.7", "Agentes del sistema"]
status: "draft-for-review"
ssot_for: []
depends_on: ["FOLDER-ARCHITECTURE.md", "NAMING-CONVENTIONS.md", "DECISIONS.md"]
version: "1.0"
how_to_use: "Completar regularmente (fin de mes o ciclo de 5 proyectos). Marcar con [x] si se cumple. Anotar problemas. Registrar hallazgos en DECISIONS.md"
---

# PKA-AUDIT-CHECKLIST.md
## Sistema Raul 2026 — Auditoría de Salud del Sistema

**Propósito:** Checklist operacional para validar que el PKA sigue sus propios principios de arquitectura, gobernanza y naming.

**Quién lo usa:** Raoul, Claude/LLMs en sesiones de auditoría, especialistas de dominio  
**Cuándo:** Fin de cada mes o después de 5 proyectos completados  
**Cómo:** Completar cada sección y anotar hallazgos

---

## Instrucciones de uso

- Revisar esta lista regularmente (recomendado: fin de cada mes o al cierre de ciclo de 5 proyectos).
- Completar cada sección con un `[x]` si se cumple, o anotar el problema encontrado.
- Registrar cualquier fallo o desviación en `DECISIONS.md` con fecha y contexto.
- Usar el resultado para actualizar el PKA o documentar decisiones de excepciones.

---

## A. ARQUITECTURA LÓGICA

### A1 — Estructura de raíz

- [ ] `01-inbox/` existe y tiene subcarpetas: `01-owner-to-raul/`, `02-deliverables-to-owner/`, `03-raw-sources/`, `README.md`
- [ ] `02-knowledge-base/` existe con: `_index.md`, `00-raul-intelligence/`, `01-foundations/`, `02-domains/`, `03-cross-cutting/`, `04-sops-and-playbooks/`, `05-glossary-and-tables/`, `README.md`
- [ ] `03-projects/` existe y contiene al menos un dominio con proyectos
- [ ] `04-system/` existe con: `01-config/`, `02-agents/`, `03-governance/`, `04-tools-and-scripts/`, `05-indexes/`, `06-companion-docs/`, `README.md`
- [ ] `05-archive/` existe (puede estar vacío inicialmente)
- [ ] `.claude/` existe en raíz (derivado de agentes, NO para mover)

**Problemas encontrados:**
```
(anotaciones aquí)
```

---

### A2 — Dominios en `02-knowledge-base/02-domains/`

Revisar cada dominio activo:

#### Dominio: `01-genteca/`
- [ ] Tiene `_index.md` con alcance, marcas, equipos y tipos de proyectos
- [ ] Tiene subcarpeta `wiki/` con `_index.md`
- [ ] Tiene subcarpeta `specs/` con `_index-specs.md` (si aplica)
- [ ] Tiene subcarpeta `assets/` con `_index.md` (si aplica)
- [ ] Archivos de wiki siguen patrón `NN-slug.md`
- [ ] `wiki/_index.md` lista todos los artículos y sus propósitos

#### Dominio: `02-plenus-metabolica/`
- [ ] Tiene `_index.md` con alcance, marcas, equipos y tipos de proyectos
- [ ] Tiene subcarpeta `wiki/` con `_index.md`
- [ ] Tiene subcarpeta `specs/` (si aplica)
- [ ] Tiene subcarpeta `assets/` (si aplica)

#### Dominio: `03-finca-ganaderia/`
- [ ] Tiene `_index.md`
- [ ] Estructura de subcarpetas apropiada para dominio

#### Dominio: `04-teca-teak4food/`
- [ ] Tiene `_index.md`
- [ ] Estructura apropiada

#### Dominio: `05-marca-personal-raoul/`
- [ ] Tiene `_index.md`
- [ ] Estructura apropiada

#### Dominio: `99-other-domains/`
- [ ] Existe como captura de temas transversales futuros

**Problemas encontrados:**
```
(anotaciones aquí)
```

---

### A3 — Raul-Intelligence (Memoria operativa)

- [ ] `02-knowledge-base/00-raul-intelligence/_index.md` existe y mapea los archivos
- [ ] `estilo-y-voz.md` existe y documenta preferencias de tono del Owner
- [ ] `patrones-de-delegacion.md` existe con notas sobre qué agente funciona para qué tarea
- [ ] `preferencias-del-owner.md` existe con decisiones y correcciones registradas
- [ ] Al menos un `aprendizajes-<dominio>.md` existe (ej. `aprendizajes-genteca.md`)
- [ ] Archivos en esta carpeta se actualizan después de sesiones significativas (no automáticamente)

**Problemas encontrados:**
```
(anotaciones aquí)
```

---

## B. GOBERNANZA Y CONTROL

### B1 — Documentos de sistema

- [ ] `04-system/01-config/CLAUDE.md` existe con instrucciones maestras
- [ ] `04-system/01-config/CONTEXT_core.md` existe con contexto general
- [ ] `04-system/01-config/FOLDER-ARCHITECTURE.md` existe y está actualizado
- [ ] `04-system/01-config/NAMING-CONVENTIONS.md` existe y define patrones vigentes
- [ ] `04-system/01-config/OWNER_PROFILE.md` existe y describe preferencias del Owner
- [ ] `04-system/03-governance/DECISIONS.md` existe con decisiones arquitectónicas registradas
- [ ] `04-system/03-governance/MIGRATION-PLAN.md` existe (puede estar completado)
- [ ] `04-system/03-governance/task-log.md` existe como log canónico de tareas
- [ ] `04-system/03-governance/RISK-POLICY.md` existe con políticas de riesgo
- [ ] `04-system/03-governance/SECURITY-AND-ACCESS.md` existe (si aplica)

**Problemas encontrados:**
```
(anotaciones aquí)
```

### B2 — Índices canónicos

- [ ] `04-system/05-indexes/domains-index.md` existe y lista todos los dominios activos
- [ ] `04-system/05-indexes/projects-index.md` existe y lista proyectos activos (con estado)
- [ ] `04-system/05-indexes/kb-index-by-domain.md` existe con inventario de KB por dominio
- [ ] `04-system/05-indexes/research-index.md` existe (si aplica)
- [ ] Los índices están con timestamp de última actualización
- [ ] Los índices incluyen referencias cruzadas a archivos de configuración

**Problemas encontrados:**
```
(anotaciones aquí)
```

---

## C. CONVENCIONES DE NOMBRES

### C1 — Carpetas top-level

- [ ] Todas las carpetas top-level tienen formato `NN-nombre/` (2 dígitos + guion + nombre)
- [ ] No hay espacios en nombres de carpeta
- [ ] No hay caracteres especiales no permitidos

### C2 — Dominios

- [ ] Dominios en `02-knowledge-base/02-domains/` siguen: `NN-nombre-dominio/`
- [ ] Dominios en `03-projects/` siguen: `nombre-dominio/` (sin número)
- [ ] Todos los dominios tienen sufijo apropiado (sin espacios, minúsculas, guiones)

### C3 — Proyectos

- [ ] Proyectos en `03-projects/<dominio>/` siguen patrón: `YYYY-MM_slug-descriptivo/`
- [ ] Proyectos tienen etapas numeradas `00-`, `01-`, `02-`, `03-`, `04-`
- [ ] No hay excepciones de naming sin documentar
- [ ] **AUDITORÍA:** No hay carpetas con espacios como `GME Estudios de mercado/` (VIOLATION ENCONTRADA: revisar en D3)
- [ ] **AUDITORÍA:** Todas las carpetas de proyecto usan minúsculas y guiones (no CamelCase ni espacios)

### C4 — Archivos de dominio

- [ ] Artículos de wiki siguen: `NN-slug-descriptivo.md`
- [ ] Specs de producto siguen: `YYYY-MM-DD_tipo-doc_slug-producto.md`
- [ ] Índices de carpeta: `_index.md` o `_index-<tipo>.md`
- [ ] Archivos fundacionales: UPPERCASE (ej. `DECISIONS.md`, `CLAUDE.md`)

### C5 — Archivos companion

- [ ] Archivos companion tienen sufijo ` PERPLEXITY` (si aplica)
- [ ] Se distinguen claramente de archivos core del sistema
- [ ] Se documentan en `DECISIONS.md` cuando se promocionan a core

**Problemas encontrados:**
```
(anotaciones aquí)
```

---

## D. FLUJOS OPERATIVOS

### D1 — Entrada y salida (`01-inbox`)

- [ ] `01-owner-to-raul/` contiene briefs, pedidos, requests del Owner
- [ ] `02-deliverables-to-owner/` contiene entregas, borradores para revisión
- [ ] `03-raw-sources/` contiene insumos crudos sin procesar
- [ ] `01-inbox/README.md` explica qué admite cada subcarpeta y quién las procesa
- [ ] Existe un bot o proceso definido que revisa `01-owner-to-raul/` regularmente
- [ ] Los archivos en inbox tienen una política de retención / limpieza documentada
- [ ] No se versionan archivos de inbox (están en `.gitignore`)

**Problemas encontrados:**
```
(anotaciones aquí)
```

### D2 — Compilación KB (`02-knowledge-base`)

- [ ] Existe un proceso definido para que contenido de `01-inbox/03-raw-sources/` se compile a `wiki/`
- [ ] Existe claridad sobre quién es responsable de compilar (ej. Celeste, Paxs, especialistas por dominio)
- [ ] Los artículos wiki tienen una fecha de última revisión (en frontmatter o comentario)
- [ ] Los artículos wiki enlazan a proyectos relacionados en `03-projects/`
- [ ] Existe distinción clara entre `wiki/` (conocimiento estable), `specs/` (productos), `assets/` (visual)
- [ ] No hay duplicación de contenido entre `02-knowledge-base/` y `03-projects/`

**Problemas encontrados:**
```
(anotaciones aquí)
```

### D3 — Ejecución de proyectos (`03-projects`)

- [ ] Cada proyecto tiene su `README.md` con descripción, stakeholders, deliverables
- [ ] Cada proyecto tiene su propia estructura de etapas `00-brief` a `04-published`
- [ ] Los proyectos enlazan a la KB relevante del dominio
- [ ] No hay proyectos "huérfanos" sin enlace a dominio o sin propósito claro
- [ ] Los proyectos completados se mueven a `05-archive/` con documentación de cierre
- [ ] **AUDITORÍA PROFUNDA:** Revisar proyectos incompletos en `03-projects/genteca/`:
  - [ ] `2025-04_GME Estudios de mercado/` — estado desconocido, carpeta tiene violation naming (espacios)
  - [ ] Otros proyectos sin etapas `04-published/` — ¿completar, archivar, o abandonar?
  - [ ] Crear registry de proyectos incompletos en `PROJECT-INCOMPLETE-REGISTRY.md`

**Problemas encontrados:**
```
(anotaciones aquí)
```

### D4 — Agentes y routing (`04-system/02-agents`)

- [ ] Agentes conceptuales viven en `04-system/02-agents/conceptual/`
- [ ] Agentes derivados en `.claude/agents/` están sincronizados con conceptuales
- [ ] Existe un documento de routing: quién es responsable de qué tipo de tarea
- [ ] Cada agente tiene una ficha conceptual con: rol, responsabilidades, qué dominio(s) atiende
- [ ] La arquitectura de content supply chain está documentada (`ARCHITECTURE_Content-Supply-Chain.md`)

**Problemas encontrados:**
```
(anotaciones aquí)
```

---

## E. FUENTES DE VERDAD (SSOT)

### E1 — Documentos canónicos

- [ ] `04-system/01-config/FOLDER-ARCHITECTURE.md` es SSOT de estructura
- [ ] `04-system/01-config/NAMING-CONVENTIONS.md` es SSOT de nombres
- [ ] `04-system/03-governance/DECISIONS.md` es SSOT de decisiones arquitectónicas
- [ ] `04-system/03-governance/task-log.md` es SSOT de delegaciones y outcomes
- [ ] `04-system/05-indexes/domains-index.md` es SSOT de dominios activos
- [ ] `04-system/05-indexes/projects-index.md` es SSOT de proyectos activos
- [ ] Cada dominio `_index.md` es SSOT de alcance, marcas, equipos del dominio
- [ ] No hay duplicación significativa de información entre estos archivos

### E2 — Documentos auxiliares (companion)

- [ ] Los documentos companion están claramente marcados
- [ ] Los documentos companion NO deben usarse como fuente de verdad
- [ ] Si un companion dice algo distinto al canonical, el canonical prevalece

**Problemas encontrados:**
```
(anotaciones aquí)
```

---

## F. MANTENIMIENTO Y ACTUALIZACIÓN

### F1 — Refresco periódico

- [ ] `domains-index.md` fue actualizado en los últimos 30 días
- [ ] `projects-index.md` fue actualizado en los últimos 30 días
- [ ] Cada dominio `_index.md` fue actualizado en los últimos 60 días
- [ ] `DECISIONS.md` registra decisiones de los últimos 30 días (si hubo cambios)

### F2 — Cambios estructurales

- [ ] Cualquier cambio de carpetas o movimiento de archivos se registra en `DECISIONS.md`
- [ ] Cambios de naming se documentan en `DECISIONS.md`
- [ ] Cambios de flujo de trabajo se documentan en `DECISIONS.md`
- [ ] No hay cambios no documentados

### F3 — Sincronización de agentes

- [ ] Agentes conceptuales en `04-system/02-agents/conceptual/` están al día
- [ ] Agentes en `.claude/agents/` son derivados de conceptuales (no originales)
- [ ] Si se modifica un agente conceptual, se propaga a `.claude/`

**Problemas encontrados:**
```
(anotaciones aquí)
```

---

## G. RIESGOS Y EXCEPCIONES

### G1 — Scripts y dependencias de rutas (CRÍTICO por auditoría profunda)

- [ ] Revisar scripts Python en `04-system/04-tools-and-scripts/scripts/`:
  - [ ] `fase4_kb_formatter.py` — ¿usa env vars o rutas hardcodeadas?
  - [ ] `pendrive_pipeline.py` — ¿usa env vars o rutas hardcodeadas a `04-system/05-indexes/`?
  - [ ] `descargar_genteca_v2.py` — ¿tiene dependencias de rutas?
- [ ] **HALLAZGO:** 3 scripts tienen rutas hardcodeadas (CRÍTICO)
- [ ] Crear `04-system/01-config/SCRIPTS-DEPENDENCIES.md` antes de mover carpetas (I.2 en IMPROVEMENTS)
- [ ] No separar `05-indexes/` hasta confirmar scripts actualizados

### G2 — Naming violations

- [ ] No hay excepciones de naming no documentadas
- [ ] Si existen archivos con espacios o caracteres especiales, están en `DECISIONS.md`
- [ ] No hay archivos llamados `_backup_`, `_old_`, `_temp_` sin propósito explícito
- [ ] **HALLAZGO:** `GME Estudios de mercado/` tiene espacios (violation de C3) — renombrar o documentar excepción

### G3 — Duplicación

- [ ] No hay archivos core duplicados en múltiples carpetas
- [ ] Si un concepto aparece en `02-knowledge-base/` y `03-projects/`, hay claridad sobre quién es SSOT
- [ ] No hay proyectos duplicados con nombres similares

### G4 — Outsiders / Contenido fuera de lugar

- [ ] No hay archivos huérfanos en raíz (todos están en una de las 5 carpetas principales)
- [ ] No hay contenido importante en `05-archive/` que debería estar en KB o proyectos activos
- [ ] No hay archivos binarios pesados en lugares donde deberían estar comprimidos o enlazados

**Problemas encontrados:**
```
(anotaciones aquí)
```

---

## H. RESUMEN Y PRÓXIMOS PASOS

### Fecha de auditoría: _______________

### Puntuación general (marcar una):
- [ ] Verde (0–1 problemas menores) → Sistema saludable, no requiere cambios urgentes
- [ ] Amarillo (2–5 problemas moderados) → Requiere pequeños ajustes, planificar en próximo ciclo
- [ ] Rojo (6+ problemas críticos) → Requiere intervención inmediata, escalar a Claude/Raoul

### Problemas críticos identificados:
```
1. 
2. 
3. 
```

### Recomendaciones inmediatas:
```
1. 
2. 
3. 
```

### Registro de decisión:
- Auditoría completada: _____ (fecha)
- Auditor: _______________
- Entrada registrada en: `DECISIONS.md` ☐

---

**Fin de checklist**
