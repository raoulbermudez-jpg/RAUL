# SOP: Investigación Técnica

**Versión:** 1.0
**Última actualización:** 2026-05-01
**Dominio:** Cross-cutting (aplica a todos los dominios)
**Agente responsable:** Raul (orquestación) → Vera / Orlan / Paxs (ejecución)

---

## Propósito

Estandarizar cómo se inicia, ejecuta y archiva una investigación técnica, desde la necesidad del Owner hasta el artículo KB o reporte listo para uso.

## Alcance

Aplica a cualquier tarea que requiera investigar información externa: selección de dispositivos, benchmarks de productos, análisis competitivo, lectura de normas, o investigación de un tema nuevo sin cobertura en la KB existente. No cubre producción de contenido editorial (eso sigue la Content Supply Chain).

## Precondiciones

- [ ] La necesidad está definida con suficiente contexto (dominio, propósito, audiencia del output)
- [ ] Se verificó que la KB existente no tiene ya una respuesta usable (`02-knowledge-base/` + `_index.md` del dominio)
- [ ] El Owner o Raul ha identificado el tipo de investigación (ver Paso 1)

---

## Pasos

### 1. Clasificar el tipo de investigación

Determinar cuál agente ejecutará la tarea:

| Tipo | Descripción | Agente |
|------|-------------|--------|
| Selección / comparación de dispositivos | Elegir el relay, protector o equipo correcto para una aplicación. Validar con normas IEC/NEMA/UL. | **Vera** |
| Inteligencia competitiva / posicionamiento | Benchmarks comerciales y estratégicos. ¿Cómo se compara Exceline vs ABB/Eaton/Schneider/Siemens? | **Orlan** |
| Investigación general profunda | Cualquier tema sin agente especializado: industria, tecnología, regulación, mercado. | **Paxs** |

**Resultado esperado:** tipo identificado → agente asignado.

---

### 2. Preparar el brief al agente

Redactar un brief usando `04-system/04-tools-and-scripts/templates/agent-brief-template.md`.

Campos críticos para investigación técnica:

- **Objetivo:** qué pregunta concreta debe responder la investigación.
- **Contexto:** dominio (Genteca / Finca / etc.), proyecto que origina la necesidad, decisión que depende del resultado.
- **Inputs:** fuentes disponibles (datasheet, manual, URL, consulta del cliente). Si hay un archivo, indicar ruta.
- **Output esperado:** formato del entregable (tabla comparativa, artículo KB, reporte ejecutivo, application note). Incluir ruta destino.
- **Constraints:** limitaciones de tiempo, normas aplicables, región, voltaje nominal.

---

### 3. Delegar al agente y validar el output

Enviar el brief al agente seleccionado. Al recibir el resultado, verificar:

- [ ] La pregunta original queda respondida (no requiere una segunda ronda de investigación)
- [ ] Las fuentes están citadas (datasheet, norma, URL con fecha de acceso)
- [ ] El output está en el formato pedido
- [ ] No hay afirmaciones sin respaldo — especialmente en selección de dispositivos o normas

Si el output es incompleto o genera nuevas preguntas, enviar una segunda iteración al mismo agente con las brechas identificadas. No más de 2 iteraciones antes de escalar al Owner.

**Resultado esperado:** entregable validado listo para archivar.

---

### 4. Archivar en la KB

Ubicar el output en la carpeta correcta:

| Tipo de output | Destino |
|----------------|---------|
| Artículo enciclopédico (definición, norma, concepto) | `02-knowledge-base/[dominio]/01-encyclopedia/` |
| Guía de selección o comparación de productos | `02-knowledge-base/[dominio]/02-product-guides/` |
| Reporte de inteligencia competitiva | `02-knowledge-base/[dominio]/03-competitive-intelligence/` |
| SOP o playbook derivado de la investigación | `02-knowledge-base/04-sops-and-playbooks/` |
| Reporte de uso interno (no reutilizable) | `03-projects/[dominio]/[proyecto]/02-production/` |

Usar `04-system/04-tools-and-scripts/templates/kb-article-template.md` si el output es un artículo de KB.

Actualizar el `_index.md` de la carpeta destino con una línea de entrada para el nuevo documento.

**Resultado esperado:** archivo guardado, `_index.md` actualizado.

---

### 5. Registrar en el task-log

Añadir una entrada en `04-system/03-governance/task-log.md`:

```
| YYYY-MM-DD | [Tipo] | [Descripción breve] | [Agente] | [Ruta output] |
```

---

## Manejo de errores

| Error | Causa probable | Acción |
|-------|---------------|--------|
| El agente devuelve información genérica sin citar fuentes | Brief demasiado vago | Reformular con pregunta más específica y constraints concretos |
| Conflicto entre fuentes (ej. dos datasheets con specs distintas) | Versiones distintas del mismo producto | Indicar la fuente más reciente; documentar el conflicto en el artículo |
| La KB ya tiene información parcial sobre el tema | No se revisó el `_index.md` antes de delegar | Parar, leer el artículo existente, actualizar en lugar de duplicar |
| Ningún agente cubre la necesidad | Gap de especialización | Escalar a Michelina para evaluar si se necesita un nuevo agente |

---

## Outputs

- Artículo KB, tabla comparativa, reporte o application note en la ruta destino acordada
- Entrada en `_index.md` del directorio destino
- Entrada en `task-log.md`

## Referencias

- `04-system/04-tools-and-scripts/templates/agent-brief-template.md` — brief estándar para cualquier agente
- `04-system/04-tools-and-scripts/templates/kb-article-template.md` — estructura de artículo KB
- `02-knowledge-base/[dominio]/_index.md` — índice del dominio relevante
- `04-system/01-config/CLAUDE.md` → sección Capa 2 — routing de agentes especializados

---

## Notas de versión

- **v1.0 — 2026-05-01** — documento inicial. Cubre Vera, Orlan, Paxs como agentes de investigación; routing por tipo de tarea; ciclo completo hasta archivado KB.
