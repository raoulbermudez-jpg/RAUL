# Domains Index — /RAUL/

Mapa central de dominios del sistema /RAUL/, su estado de activación y las rutas principales de conocimiento y proyectos.

## Propósito

Este archivo funciona como índice maestro de dominios.  
Su objetivo es permitir que el Owner, Claude y otros copilotos ubiquen rápidamente:

- qué dominios existen,
- cuáles están activos o congelados,
- dónde vive su knowledge base,
- dónde viven sus proyectos,
- y qué nivel de madurez tiene cada dominio dentro del sistema.

No sustituye los `_index.md` de cada dominio.  
Cada `_index.md` de dominio sigue siendo la puerta de entrada principal a ese espacio.

## Convención de estados

- **Activo** — dominio ya creado, con estructura válida y utilizable.
- **Plantilla v1 validada** — dominio cuyos índices principales ya fueron revisados y aprobados por el Owner.
- **Inicial / stub** — dominio creado, pero todavía no poblado con materiales reales o proyectos activos.
- **Congelado** — no debe expandirse ni trabajarse hasta nueva orden del Owner.
- **Pendiente** — previsto en arquitectura, pero aún no desplegado o no priorizado.

## Dominios del sistema

| Dominio | Estado | KB | Projects | Nota |
|---|---|---|---|---|
| Genteca | Activo · Plantilla v1 validada | `02-knowledge-base/02-domains/01-genteca/` | `03-projects/genteca/` | Dominio más maduro a la fecha; índices de dominio, wiki y market ya validados por el Owner. |
| Plenus-metabólica | Activo · Inicial / stub | `02-knowledge-base/02-domains/02-plenus-metabolica/` | `03-projects/plenus-metabolica/` | Estructura completa creada en Fase 3 cross-dominios; pendiente revisión fina del Owner y futura consolidación con NotebookLM. |
| Finca-ganadería | Pendiente | `02-knowledge-base/02-domains/03-finca-ganaderia/` _(proyectado)_ | `03-projects/finca-ganaderia/` _(proyectado)_ | Dominio previsto en la arquitectura general, pero aún no activado en la práctica. |
| Teca / Teak4Food | Congelado | `02-knowledge-base/02-domains/04-teca-teak4food/` _(objetivo esperado)_ | `03-projects/teca-teak4food/` | No iniciar Fase 3 hasta nueva orden explícita del Owner. |
| Marca personal Raoul | Congelado | `02-knowledge-base/02-domains/05-marca-personal-raoul/` _(objetivo esperado)_ | `03-projects/marca-personal-raoul/` | No iniciar Fase 3 hasta nueva orden explícita del Owner. |
| Research-generic | Congelado | `02-knowledge-base/02-domains/research-generic/` | `03-projects/research-generic/` | Espacio transversal / experimental de investigación; no expandir por ahora. |
| Sandbox | Congelado | `02-knowledge-base/02-domains/sandbox/` _(si aplica)_ | `03-projects/sandbox/` | Espacio experimental; no expandir por ahora. |

## Dominios activos hoy

### 1. Genteca

**Ruta KB:** `02-knowledge-base/02-domains/01-genteca/`  
**Ruta proyectos:** `03-projects/genteca/`

Estado actual:

- Dominio más desarrollado del sistema.
- Plantilla v1 ya validada por el Owner.
- Tiene:
  - `_index.md` de dominio validado,
  - `wiki/_index.md`,
  - `wiki/market/_index.md` validado,
  - `specs/` con fichas técnicas migradas,
  - `assets/` estructurado,
  - proyectos activos migrados con `README.md`.

Subíndices principales:

- `02-knowledge-base/02-domains/01-genteca/_index.md`
- `02-knowledge-base/02-domains/01-genteca/wiki/_index.md`
- `02-knowledge-base/02-domains/01-genteca/wiki/market/_index.md`

### 2. Plenus-metabólica

**Ruta KB:** `02-knowledge-base/02-domains/02-plenus-metabolica/`  
**Ruta proyectos:** `03-projects/plenus-metabolica/`

Estado actual:

- Dominio ya creado estructuralmente.
- Tiene plantilla inicial sólida, pero aún debe revisarse en detalle por el Owner.
- Incluye:
  - `_index.md` de dominio,
  - `wiki/_index.md`,
  - `wiki/market/_index.md`,
  - `specs/_index-specs.md`,
  - `assets/_index.md`.
- Diseñado explícitamente con una “puerta abierta” para futura consolidación desde NotebookLM.

Subíndices principales:

- `02-knowledge-base/02-domains/02-plenus-metabolica/_index.md`
- `02-knowledge-base/02-domains/02-plenus-metabolica/wiki/_index.md`
- `02-knowledge-base/02-domains/02-plenus-metabolica/wiki/market/_index.md`

## Dominios congelados

Los siguientes dominios existen como intención de arquitectura o como placeholders, pero no deben expandirse todavía:

- Teca / Teak4Food
- Marca personal Raoul
- Research-generic
- Sandbox

Regla operativa:

- No iniciar Fase 3 de estos dominios sin luz verde explícita del Owner.
- No crear índices extensos, subcarpetas o proyectos nuevos salvo instrucción directa.

## Nota sobre numeración

Actualmente existe una decisión pendiente sobre la numeración de dominios.

Situación:

- En la práctica se creó `02-plenus-metabolica/`.
- En una versión previa de la arquitectura, Plenus aparecía como `03-plenus-metabolica/`, con `02-finca-ganaderia/` antes.

Hasta que el Owner lo formalice en `DECISIONS.md`, debe asumirse que:

- la numeración puede reflejar prioridad de activación,
- y no necesariamente el orden histórico original de planificación.

## Relación con otros índices del sistema

Este archivo se complementa con:

- `04-system/05-indexes/projects-index.md` — mapa central de proyectos.
- `04-system/05-indexes/companion-docs-index.md` — documentos auxiliares y companion docs.
- `_index.md` de cada dominio — puerta principal de navegación dentro de cada espacio.
- `04-system/01-config/FOLDER-ARCHITECTURE.md` — arquitectura general del sistema.

## Regla de mantenimiento

Actualizar este archivo cuando ocurra cualquiera de estos eventos:

- se crea un dominio nuevo,
- cambia el estado de un dominio,
- un dominio pasa de stub a activo,
- un dominio queda congelado o se descongela,
- se redefine la numeración oficial de dominios.

Este índice debe mantenerse breve, operativo y fiel al estado real del sistema.