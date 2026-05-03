# Raul Intelligence — Índice de Aprendizajes

**Propósito:** Este índice es la única entrada que Raul carga siempre. Lee las descripciones, decide qué archivos son relevantes para la tarea en curso, y carga solo esos. No cargues todos los archivos — es ineficiente.

**Protocolo de carga:**
1. Lee este índice (~100 tokens)
2. Identifica qué archivos aplican a la tarea
3. Carga solo esos (típico: 1-3 archivos)
4. Al terminar la tarea: actualiza el archivo relevante con el aprendizaje nuevo

---

## Archivos disponibles

| Archivo | Descripción | Cargar cuando... |
|---|---|---|
| `estilo-y-voz.md` | Cómo escribe y comunica Raoul: tono, vocabulario, estructuras preferidas, lo que evita | La tarea requiere redactar en nombre de Raoul o ajustar el tono de un output |
| `patrones-de-delegacion.md` | Qué agente funciona mejor para qué tipo de tarea; errores de routing corregidos | Hay duda sobre a quién delegar o la tarea es ambigua |
| `preferencias-del-owner.md` | Decisiones que Raoul ha tomado, correcciones que ha hecho, lo que aprueba sin pedir cambios | Tarea de alto riesgo, decisión con alternativas, o output de alto impacto |
| `aprendizajes-genteca.md` | Especificidades del dominio Genteca aprendidas en producción (más allá de lo que dice el KB) | Cualquier tarea del dominio Genteca |

## Subcarpetas

| Carpeta | Descripción | Cargar cuando... |
|---|---|---|
| `methodology/` | Hoja de Ruta /RAUL/: metodología destilada para construir PKA personales modulares. Documento vivo, versionado, publicable. Apéndice privado en `_private/` (gitignored) | Tarea estratégica de norte: planeación de fases, decisiones arquitecturales, justificación de patrones, onboarding de nuevo colaborador al sistema |

---

## Cómo actualizar este índice

Si creas un archivo o subcarpeta nueva en esta carpeta, añade una fila a la tabla correspondiente antes de cerrar la tarea.

---

**Última actualización:** 2026-05-04
**Entradas totales:** 4 archivos activos + 1 subcarpeta (`methodology/`)
