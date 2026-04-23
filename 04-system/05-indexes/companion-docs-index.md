# Companion Docs Index — /RAUL/

Índice de documentos auxiliares creados como apoyo de diseño, continuidad conversacional y consulta operativa dentro del sistema /RAUL/.

## Propósito

Este archivo existe para identificar y explicar los documentos companion del sistema.

Estos documentos sirven para:

- preservar contexto entre sesiones largas,
- resumir trabajo ya realizado,
- registrar memoria operativa,
- mantener bibliotecas de consulta,
- y capturar procedimientos reutilizables.

Su presencia dentro de `/RAUL/` es intencional: permite que el contexto siga versionado junto con el sistema y accesible para el Owner y copilotos como Claude.

## Regla de estatus

Los documentos companion **no son SSOT automático** del sistema.

Su función es:

- apoyar,
- orientar,
- resumir,
- y acelerar continuidad.

Pero no deben interpretarse por defecto como autoridad final sobre arquitectura, reglas o gobernanza del sistema.

## Qué sí se considera core hoy

En el estado actual de `/RAUL/`, los documentos más cercanos a función core son:

- los archivos estructurales y de configuración que el Owner mantiene en `04-system/01-config/`,
- los índices operativos en `04-system/05-indexes/` como `domains-index.md` y `projects-index.md`,
- los `_index.md` de dominios ya revisados y aprobados por el Owner,
- y cualquier archivo que el Owner use explícitamente como referencia activa del sistema.

## Convención de naming actual

En esta etapa, los documentos companion creados con apoyo de Perplexity llevan el sufijo `PERPLEXITY` en el nombre del archivo.

Ese sufijo cumple tres funciones:

1. indicar origen,
2. distinguirlos de archivos operativos del sistema,
3. evitar que un copiloto los confunda con norma consolidada.

## Archivos companion actuales

### Config / contexto

- `04-system/01-config/CONTEXT_session-2026-04-22 PERPLEXITY.md`
  - Snapshot de contexto para retomar el trabajo en un hilo nuevo.
  - Resume el estado del sistema, commits relevantes, dominios activos y pendientes.

### Índices / continuidad

- `04-system/05-indexes/session-log_2026-04-22 PERPLEXITY.md`
  - Resumen cronológico de la sesión de trabajo.
  - Sirve como memoria operativa de qué se revisó, qué se aprobó y qué quedó pendiente.

- `04-system/05-indexes/core-sources-index PERPLEXITY.md`
  - Biblioteca de archivos y fuentes internas importantes del sistema.
  - Sirve como mapa de consulta rápida.

### Método / guía reusable

- `04-system/04-tools-and-scripts/KB-SYSTEM-GUIDE PERPLEXITY.md`
  - Guía reutilizable para construir sistemas tipo `/RAUL/`.
  - Puede servir luego como base para onboarding, capacitación o curso.

## Cómo deben usarse

Uso recomendado:

- como memoria de trabajo,
- como apoyo para retomar conversaciones,
- como documentos de diseño,
- como material de consulta,
- como borradores de futuras convenciones o procedimientos.

Uso no recomendado:

- tratarlos automáticamente como norma oficial,
- usarlos para contradecir un índice de dominio ya validado por el Owner,
- duplicar indefinidamente contenido que ya fue integrado a un archivo operativo más estable.

## Criterio de promoción a archivo core

Un contenido companion puede promoverse a archivo core cuando:

- deja de ser solo contexto y pasa a ser referencia operativa estable,
- se consulta repetidamente como documento de trabajo,
- organiza navegación del sistema,
- o define una convención permanente.

Cuando eso ocurra, el Owner puede decidir una de estas acciones:

- crear un nuevo archivo core sin sufijo `PERPLEXITY`,
- fusionar parte del contenido en un archivo operativo ya existente,
- o renombrar el archivo y retirarle el sufijo si pasa a cumplir función estructural.

## Relación con los índices operativos

Este archivo convive con índices operativos del sistema, especialmente:

- `04-system/05-indexes/domains-index.md`
- `04-system/05-indexes/projects-index.md`

La diferencia es simple:

- `domains-index.md` y `projects-index.md` describen el estado operativo del sistema.
- Los archivos `PERPLEXITY` preservan contexto, memoria y método.

## Regla práctica para Claude y otros copilotos

Si un copiloto consulta estos documentos, debe asumir lo siguiente:

- los archivos con sufijo `PERPLEXITY` son documentos de apoyo,
- son válidos para recuperar contexto y orientar decisiones,
- pero cualquier cambio estructural del sistema debe confirmarse contra los archivos core y la validación explícita del Owner.

## Mantenimiento

Actualizar este archivo cuando ocurra cualquiera de estas situaciones:

- se crea un nuevo documento companion,
- se elimina o archiva uno existente,
- uno de ellos se convierte en archivo core,
- cambia la convención de naming,
- o se reorganiza la carpeta `04-system/`.

Este índice debe mantenerse breve, claro y fiel al estado real del sistema.