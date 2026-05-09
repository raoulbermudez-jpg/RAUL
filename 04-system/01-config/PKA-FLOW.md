---
document_id: "PKA-FLOW"
document_type: "core-architecture"
author: "GitHub Copilot (Copilot Chat in VS Code)"
creation_date: "2026-05-08"
purpose: "Documentar el flujo end-to-end del contenido en el PKA: desde captura hasta archivo, incluyendo procesamiento, compilación y ejecución"
audience: ["Raoul Bermúdez", "Agentes del sistema", "Nuevos colaboradores"]
status: "draft-for-review"
ssot_for: ["content-lifecycle", "routing-decision-tree"]
depends_on: ["FOLDER-ARCHITECTURE.md", "DECISIONS.md"]
version: "1.0"
how_to_use: "Referencia para entender cómo fluye el contenido a través del PKA. Usar para entrenar agentes o nuevos colaboradores. Actualizar si cambia el flujo."
---

# PKA-FLOW.md
## Flujo operativo end-to-end del PKA

**Propósito:** Documento visual y narrativo que explica cómo el contenido se captura, procesa, compila, ejecuta y retroalimenta en el PKA.

**Audiencia:** Raoul, agentes, colaboradores nuevos  
**Últimas actualización:** 2026-05-08  

---

## DIAGRAMA DE FLUJO (6 fases)

```
┌─────────────────────────────────────────────────────────────────────┐
│ 1. CAPTURA                                                          │
│    ↓                                                                │
│    Briefs, pedidos, raw sources llegan a 01-inbox/                 │
│    • owner-to-raul/ ← briefs del Owner                             │
│    • raw-sources/ ← insumos sin procesar (PDFs, transcripciones)   │
│    • deliverables-to-owner/ ← borradores para revisión             │
└──────────────┬──────────────────────────────────────────────────────┘
               │
               ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 2. PROCESAMIENTO / DECISIÓN DE ROUTING                              │
│    ↓                                                                │
│    ¿Qué sucede con este contenido?                                 │
│                                                                    │
│    ÁRBOL DE DECISIÓN:                                              │
│    ├─ Es conocimiento reutilizable y estable?                      │
│    │  ├─ SÍ → Va a 02-knowledge-base/ (compilación KB)             │
│    │  └─ Debe enlazarse a dominio específico                       │
│    │                                                               │
│    ├─ Es un brief o proyecto de ejecución?                         │
│    │  ├─ SÍ → Va a 03-projects/<dominio>/ (ejecución)              │
│    │  └─ Se crea como 00-brief y avanza a 04-published             │
│    │                                                               │
│    ├─ Es aprendizaje o feedback del Owner?                         │
│    │  ├─ SÍ → Va a 02-knowledge-base/00-raul-intelligence/         │
│    │  └─ Se documenta para futuras decisiones                      │
│    │                                                               │
│    └─ Es archivo histórico o completado?                           │
│       ├─ SÍ → Va a 05-archive/                                     │
│       └─ Se documenta con fecha de archivo                         │
│                                                                    │
└──────────────┬──────────────────────────────────────────────────────┘
               │
               ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 3. COMPILACIÓN / INGESTA A KB                                       │
│    ↓                                                                │
│    Contenido raw → KB estructurada en 02-knowledge-base/            │
│                                                                    │
│    Estructura de dominio:                                          │
│    02-knowledge-base/02-domains/<dominio>/                         │
│    ├─ _index.md (SSOT del dominio)                                 │
│    ├─ wiki/                                                        │
│    │  ├─ _index.md                                                 │
│    │  └─ NN-articulo-slug.md (artículos compilados)                │
│    ├─ specs/ (si aplica)                                           │
│    │  └─ especificaciones de producto                              │
│    └─ assets/ (si aplica)                                          │
│       └─ recursos visuales o datos                                 │
│                                                                    │
│    Responsables: Celeste (compilador de KB), especialistas         │
│    Cadencia: Cambios ad-hoc + revisión trimestral                  │
│                                                                    │
└──────────────┬──────────────────────────────────────────────────────┘
               │
               ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 4. EJECUCIÓN / CONSUMO EN PROYECTOS                                 │
│    ↓                                                                │
│    Proyectos consumen KB y generan entregas                         │
│                                                                    │
│    Flujo de etapas:                                                │
│    03-projects/<dominio>/<proyecto>/                               │
│    ├─ 00-brief/ (contexto y objetivos)                             │
│    ├─ 01-research/ (investigación, referencias a KB)               │
│    ├─ 02-production/ (contenido en desarrollo)                     │
│    ├─ 03-review/ (revisión con Owner)                              │
│    └─ 04-published/ (deliverable final)                            │
│                                                                    │
│    Enlaces: Cada proyecto referencia wiki/ del dominio             │
│    Responsables: PM de proyecto, especialistas                     │
│                                                                    │
└──────────────┬──────────────────────────────────────────────────────┘
               │
               ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 5. SALIDA / ENTREGA                                                 │
│    ↓                                                                │
│    Entregas se preparan en 01-inbox/02-deliverables-to-owner/      │
│                                                                    │
│    Deliverable → Aprobación del Owner → Archivo                    │
│    └─ Si aprobado: Archivo en 05-archive/                          │
│    └─ Si feedback: Vuelve a 03-projects/<proyecto>/02-production/  │
│                                                                    │
└──────────────┬──────────────────────────────────────────────────────┘
               │
               ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 6. FEEDBACK / LOOP DE APRENDIZAJE                                   │
│    ↓                                                                │
│    Después de cada proyecto:                                       │
│    ├─ Aprendizajes documentados en                                 │
│    │  02-knowledge-base/00-raul-intelligence/aprendizajes-<dom>.md  │
│    ├─ Decisiones registradas en                                    │
│    │  04-system/03-governance/DECISIONS.md                         │
│    ├─ Patrones de delegación actualizados                          │
│    │  02-knowledge-base/00-raul-intelligence/patrones-delegacion.md│
│    └─ KB refinada con nuevos insights                              │
│                                                                    │
└─────────────────────────────────────────────────────────────────────┘
```

---

## DESCRIPCIÓN POR FASE

### Fase 1: CAPTURA (01-inbox/)

**Qué sucede:**
- Briefs, pedidos y raw sources llegan a `01-inbox/`
- Contenido entra sin procesar y sin clasificar
- No se versionan (está en `.gitignore`)

**Subcarpetas:**
- `01-owner-to-raul/` — Pedidos directos del Owner (briefs, requests)
- `02-deliverables-to-owner/` — Borradores listos para revisión
- `03-raw-sources/` — Insumos crudos: PDFs, transcripciones, enlaces, notas

**Responsables:**
- Raoul (ingresa contenido)
- Agente/Bot (revisa regularmente `01-owner-to-raul/`)

**Cadencia:**
- Revisión diaria o continua

**Salida de esta fase:**
Contenido catalogado y listo para decisión de routing

---

### Fase 2: PROCESAMIENTO / DECISIÓN

**Qué sucede:**
- Se determina dónde debe vivir el contenido
- Decisión basada en naturaleza del contenido

**Árbol de decisión detallado:**

#### ¿Es conocimiento reutilizable y estable?
**Ejemplos:**
- Definición técnica de "dispositivo de protección contra sobrecorriente"
- Regulaciones ICONTEC para equipos eléctricos
- Recetas de preparación de alimentos procesados
- Estudios de mercado sobre tendencias de consumo

**Destino:** `02-knowledge-base/02-domains/<dominio>/wiki/`  
**Proceso:** Compilación a artículos indexados (NN-slug.md)  
**Responsable:** Compilador (Celeste) + especialista del dominio  

#### ¿Es un brief o proyecto de ejecución?
**Ejemplos:**
- "Hacer estudios de mercado para GME"
- "Redactar especificaciones de producto X"
- "Crear propuesta de venta para Cliente Y"

**Destino:** `03-projects/<dominio>/<proyecto>/00-brief/`  
**Proceso:** Crear proyecto con etapas 00-04  
**Responsable:** PM de proyecto  

#### ¿Es aprendizaje o feedback operativo?
**Ejemplos:**
- "Esta vez el Owner prefirió tono más formal"
- "El agente Vera excelente para análisis competitivo"
- "Demanda de productos X se concentra en región Y"

**Destino:** `02-knowledge-base/00-raul-intelligence/`  
**Archivos:** patrones-delegacion.md, estilo-y-voz.md, aprendizajes-<dominio>.md  
**Responsable:** Raoul + agente compilador  

#### ¿Es archivo histórico o completado?
**Ejemplos:**
- Proyecto archivado hace 6 meses
- Brief obsoleto de 2024
- Raw source ya procesado y no referenciado

**Destino:** `05-archive/`  
**Proceso:** Mover con documentación de cierre  
**Responsable:** Raoul o gestor de archivo  

---

### Fase 3: COMPILACIÓN / INGESTA A KB

**Qué sucede:**
- Raw sources se transforman en artículos de conocimiento indexados
- Se integran a la wikia de su dominio
- Se crean enlaces cruzados a proyectos relacionados

**Estructura de dominio resultante:**

```
02-knowledge-base/02-domains/01-genteca/
├─ _index.md (SSOT: alcance, marcas, equipos, tipos de proyecto)
├─ wiki/
│  ├─ _index.md (listado de todos los artículos)
│  ├─ 01-proteccion-dispositivos-overcorriente.md
│  ├─ 02-regulaciones-icontec-equipos.md
│  ├─ 03-mercado-latinoamericano-proteccion.md
│  └─ ... (índice de artículos)
├─ specs/ (si aplica)
│  ├─ _index-specs.md
│  ├─ 2026-05-08_producto_gme-dispositivo-x.md
│  └─ ... (especificaciones de producto)
└─ assets/
   ├─ _index.md
   ├─ gráficos-mercado-2025.png
   └─ ... (recursos visuales)
```

**Responsables:**
- **Celeste:** Compilador de KB — transforma raw sources en artículos estructurados
- **Especialista de dominio:** Revisa y amplía conocimiento
- **Raoul:** Aprueba incorporación de nuevo conocimiento al dominio

**Cadencia:**
- Cambios ad-hoc (cuando hay raw sources nuevos)
- Revisión de coherencia: trimestral
- Auditoría de completitud: semestral

---

### Fase 4: EJECUCIÓN / CONSUMO EN PROYECTOS

**Qué sucede:**
- Proyectos consumen la KB compilada
- Utilizan artículos como referencias, marcos teóricos, contexto
- Generan nuevas entregas (reports, propuestas, especificaciones)

**Estructura de proyecto:**

```
03-projects/01-genteca/2026-05_gme-estudio-mercado/
├─ README.md (contexto, stakeholders, deliverables esperados)
├─ 00-brief/
│  └─ brief-owner.md (qué quiere, por qué, cuándo)
├─ 01-research/
│  ├─ _index.md
│  ├─ referencias-kb.md (enlaza a wiki/)
│  ├─ búsqueda-competencia.md
│  └─ tendencias-mercado-2025.md
├─ 02-production/
│  ├─ borrador-01.md
│  ├─ borrador-02.md (feedback Owner)
│  └─ análisis-datos.xlsx
├─ 03-review/
│  ├─ versión-pendiente-aprobación.md
│  └─ feedback-owner.md
└─ 04-published/
   ├─ estudio-mercado-gme-FINAL.md
   └─ presentación-ejecutiva.pptx
```

**Enlaces clave:**
- Cada proyecto referencia `02-knowledge-base/02-domains/<dominio>/wiki/`
- Las referencias son explícitas en archivos (markdown links)
- Crea trazabilidad: KB → Proyecto → Delivery

**Responsables:**
- **PM de proyecto:** Gestión de flujo etapas
- **Especialista de dominio:** Coordinación técnica
- **Raoul:** Revisión y aprobación final

**Cadencia:**
- Depende del proyecto (semanal, quincenal, mensual)
- Punto de sincronización: después de 03-review

---

### Fase 5: SALIDA / ENTREGA

**Qué sucede:**
- Deliverable final se prepara para presentación
- Se envía a Owner para aprobación
- Se registra en `01-inbox/02-deliverables-to-owner/`

**Flujo de aprobación:**

```
04-published/ 
    ↓
Preparar deliverable
    ↓
Enviar a 01-inbox/02-deliverables-to-owner/
    ↓
¿Owner aprueba?
    ├─ SÍ → Archivo en 05-archive/ + snapshot
    └─ NO → Feedback → Vuelve a 02-production/
```

**Responsables:**
- **PM de proyecto:** Prepara deliverable
- **Raoul:** Envía y coordina feedback
- **Gestor de archivo:** Mueve a 05-archive/

**Documentación:**
- Fecha de entrega
- Versión final
- Feedback recibido (si aplica)

---

### Fase 6: FEEDBACK / LOOP DE APRENDIZAJE

**Qué sucede:**
- Se capturan aprendizajes de la ejecución
- Se actualiza conocimiento del Owner (raul-intelligence)
- Se refinan flujos y patrones

**Documentos actualizados:**

1. **`02-knowledge-base/00-raul-intelligence/aprendizajes-<dominio>.md`**
   - "La demanda de producto X se concentra en región Y"
   - "El Owner prefiere formato de reporte ejecutivo sobre tablas"
   - "Esta regulación cambió en 2025, afecta especificaciones"

2. **`04-system/03-governance/DECISIONS.md`**
   - "Decisión: para futuros estudios GME, usar metodología X"
   - "Excepción aprobada: naming de carpeta con espacios"
   - "Cambio de responsable: antes Vera, ahora Orlan"

3. **`02-knowledge-base/00-raul-intelligence/patrones-delegacion.md`**
   - "Vera → muy buena para análisis competitivo"
   - "Solenne → mejor para redacción de propuestas B2B"
   - "Oz → indispensable para diseño visual"

4. **KB refinada** (nuevos artículos o actualización de existentes)
   - Agregar "Regulaciones ICONTEC actualizadas 2025"
   - Actualizar "Tendencias de mercado latinoamericano"

**Responsables:**
- **Raoul:** Captura aprendizajes durante sesión de feedback
- **Compilador (Celeste):** Integra a 00-raul-intelligence y KB
- **Agentes:** Proporcionan retroalimentación sobre efectividad

**Cadencia:**
- Inmediatamente después de cierre de proyecto (1-2 días)
- O en sesión semanal de revisión

---

## EJEMPLOS DE FLUJO END-TO-END

### Ejemplo 1: Brief → Proyecto → Entrega

```
CAPTURA:
Owner envía brief a 01-inbox/01-owner-to-raul/:
"Necesito estudio de mercado para GME en mercados latinoamericanos"

PROCESAMIENTO:
Decisión: Es un proyecto de ejecución
Destino: 03-projects/01-genteca/

COMPILACIÓN KB:
Celeste revisa si existen artículos sobre:
- Mercados latinoamericanos (sí, en wiki/)
- Regulaciones de protección (sí, en wiki/)
Si faltan, crea artículos nuevos antes de proyecto

EJECUCIÓN:
1. Crear 2026-05_estudio-mercado-latinoamericano/
2. 00-brief: copiar pedido Owner
3. 01-research: investigar, enlazar a wiki/
4. 02-production: redactar análisis
5. 03-review: feedback Owner
6. 04-published: versión final

SALIDA:
Mover a 01-inbox/02-deliverables-to-owner/
Owner aprueba → Archivo en 05-archive/

FEEDBACK:
- Aprendizaje: "Preferencias Owner por gráficos vs tablas"
- DECISIONS.md: "Metodología confirmada para futuros estudios"
- KB: Actualizar "Tendencias de mercado 2026"
```

### Ejemplo 2: Raw source → Compilación a KB (sin proyecto)

```
CAPTURA:
Transcripción de entrevista con distribuidor de equipos

PROCESAMIENTO:
Decisión: Es conocimiento reutilizable
Destino: 02-knowledge-base/

COMPILACIÓN:
Celeste procesa transcripción → Crea artículo
02-knowledge-base/02-domains/01-genteca/wiki/
└─ 04-canales-distribucion-equipos-lam.md

Artículo contiene:
- Resumen de canales
- Actores clave
- Preferencias de mercado
- Referencias a artículos relacionados

EJECUCIÓN:
No hay proyecto inmediato, pero el artículo está disponible
para futuros proyectos que lo necesiten

FEEDBACK:
- Documento queda registrado en wiki/_index.md
- Disponible para referencia en proyectos futuros
```

---

## DECISIÓN DE ROUTING: ÁRBOL COMPLETO

```
¿Nuevo contenido llegó a 01-inbox/?
│
├─ ¿Es solicitud de Owner (brief, pedido)?
│  ├─ SÍ → 03-projects/<dominio>/ (PROYECTO)
│  └─ Crear proyecto con etapas 00-04
│
├─ ¿Es raw source sin procesar?
│  ├─ ¿Se puede compilar a conocimiento reutilizable?
│  │  ├─ SÍ → 02-knowledge-base/02-domains/<dominio>/wiki/ (KB)
│  │  └─ Compilación por Celeste
│  │
│  └─ ¿NO, es específico de un proyecto?
│     └─ Mover a 03-projects/<proyecto>/01-research/
│
├─ ¿Es retroalimentación operativa o aprendizaje?
│  ├─ SÍ → 02-knowledge-base/00-raul-intelligence/ (INTELIGENCIA)
│  └─ Documentar en patrones, preferencias, aprendizajes
│
├─ ¿Es entrega de proyecto completado?
│  ├─ SÍ → 01-inbox/02-deliverables-to-owner/
│  └─ Esperar aprobación Owner
│
└─ ¿Nada de lo anterior? ¿Es histórico u obsoleto?
   └─ SÍ → 05-archive/ (ARCHIVO)
      └─ Documentar con fecha y razón de archivo
```

---

## RESPONSABLES POR FASE

| Fase | Actividad Principal | Responsable | Frecuencia |
|------|---------------------|-------------|-----------|
| 1. Captura | Monitorear inbox | Raoul, Bot | Diaria/continua |
| 2. Procesamiento | Decisión de routing | Raoul, Claude | Ad-hoc |
| 3. Compilación KB | Integrar a dominio | Celeste | Ad-hoc |
| 4. Ejecución | Gestionar proyecto | PM, especialista | Según proyecto |
| 5. Salida | Preparar entrega | PM, Raoul | Fin de proyecto |
| 6. Feedback | Capturar aprendizajes | Raoul, compilador | Post-proyecto |

---

## ÍNDICES Y REFERENCIAS CRUZADAS

El flujo es posible porque existen índices que conectan fases:

- `02-knowledge-base/02-domains/<dominio>/_index.md` — SSOT del dominio (enlaza Wiki, specs, assets)
- `02-knowledge-base/02-domains/<dominio>/wiki/_index.md` — Listado de artículos con propósito
- `03-projects/` — Proyectos por dominio, enlazan a wiki/
- `04-system/05-indexes/` — Índices canónicos: domains-index.md, projects-index.md, kb-index-by-domain.md
- `05-archive/` — Snapshot de proyectos completados (preserva estructura)

---

## PRÓXIMOS PASOS / MEJORAS

Este flujo es operativo pero se puede mejorar con:

1. **II.2 (PKA-FLOW.md)** — Este documento (✓ completo)
2. **I.2 (SCRIPTS-DEPENDENCIES)** — Documentar cómo scripts acceden a índices y raw sources
3. **I.1 (SSOT-MATRIX)** — Clarificar quién es responsable de cada índice en este flujo
4. **III.1 (Automatización)** — Script para validar que proyecto referencia KB correctamente

---

**Versión:** 1.0  
**Última revisión:** 2026-05-08  
**Próxima revisión:** 2026-08-08 (trimestral)
