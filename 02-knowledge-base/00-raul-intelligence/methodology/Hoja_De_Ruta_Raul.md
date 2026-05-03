# Hoja de Ruta /RAUL/ — Metodología para construir PKA personales modulares

**Versión:** v0.3
**Última actualización:** 2026-05-04
**Tipo:** documento metodológico vivo
**Audiencia:** publicable. Detalles internos sensibles viven en `_private/Apendice_A_Notas_Privadas.md` (gitignored).

---

## 0. Sobre este documento

### 0.1. Qué es

Este documento es la **metodología destilada** detrás de la construcción de /RAUL/, un Personal Knowledge Assistant (PKA) modular y multi-dominio para una sola persona. No es un plan de proyecto: es la captura de los principios, patrones y trade-offs que han demostrado ser útiles construyendo el sistema, listos para que otra persona pueda aplicarlos a su propio PKA.

Coexiste con dos tipos de documento adyacentes:

- **Plan operativo** (no este documento): qué hacer la próxima semana en /RAUL/. Vive en `04-system/03-governance/MIGRATION-PLAN.md` y similares.
- **Decisiones registradas** (no este documento): qué se decidió y cuándo. Vive en `04-system/03-governance/DECISIONS.md`.

Esta hoja de ruta vive **encima** de ambos: explica por qué la arquitectura es como es y cómo se construye una nueva.

### 0.2. Audiencia

Doble capa:

- **Capa pública (este archivo):** un lector externo puede usar este documento para construir su propio PKA. Sin nombres de contactos, contratos, ni casos sensibles. Ejemplos /RAUL/ se usan como ilustración, no como confesión.
- **Capa privada (`_private/Apendice_A_Notas_Privadas.md`):** detalles operativos sensibles del operador. Excluida de git.

### 0.3. Cómo se actualiza

- **Versionado semántico:** v0.x para iteraciones, v1.0 cuando la metodología pase su primera auditoría completa.
- **Changelog corto al final** del documento. Cambios mayores merecen entrada explícita.
- **Cuándo iterar:** cuando un patrón nuevo se valide en uso real, cuando un principio falle en práctica, cuando un descarte deba revertirse, cuando se añada un dominio nuevo que estrese la metodología.

---

## 1. Definición operativa de PKA personal

### 1.1. Qué es

Un Personal Knowledge Assistant (PKA) personal es un sistema de archivos, agentes LLM, gobernanza y workflows que asiste a **una sola persona** a:

- Capturar, organizar y recuperar conocimiento personal y profesional.
- Producir outputs de calidad consistente a través de múltiples dominios de actividad.
- Mantener trazabilidad de decisiones, fuentes y resultados.
- Evolucionar con el operador sin requerir reescritura cuando cambian las herramientas subyacentes.

### 1.2. Qué NO es

- **No es un repositorio de notas pasivo.** Un PKA produce — no solo almacena.
- **No es un agente LLM con memoria.** Un PKA tiene agentes, pero su valor está en la arquitectura que los hace consistentes y trazables.
- **No es un sistema empresarial.** No tiene clientes externos, ni equipos de mantenimiento, ni SLAs. El operador es proveedor y consumidor.
- **No es un wiki.** Un wiki es un componente; el PKA tiene wiki + producción + governance + memoria + cadenas de delivery.
- **No es vendor-locked.** Si depende exclusivamente de una app o un LLM, es un workflow, no un PKA.

### 1.3. Por qué "personal" cambia el problema

Un PKA personal NO es un PKA organizacional miniaturizado. Las diferencias importan:

| Dimensión | PKA organizacional | PKA personal |
|---|---|---|
| Operador | Equipo distribuido | 1 persona |
| Dominios | Uniformes (vertical único) | Heterogéneos (negocio, hogar, salud, marca personal, finanzas...) |
| Presupuesto cognitivo | Distribuido entre miembros | Limitado al operador único |
| Ciclo de feedback | Métricas de equipo | Auto-percepción del operador |
| Riesgo | Reputacional/contractual con terceros | Reputacional propio + operativo personal |
| Justificación de overhead | ROI medible en horas-equipo | ROI medido en fricción del operador |

**Consecuencia metodológica:** un PKA personal debe priorizar fricción baja para el operador. Cualquier estructura que sume fricción sin retorno claro es deuda neta. Lo que para una empresa es "buen formalismo" para un individuo puede ser parálisis.

---

## 2. Principios rectores

Los principios siguientes son las reglas que sostienen las decisiones arquitecturales. Cuando hay conflicto entre principios, gana el principio con número menor (orden de precedencia).

### 2.1. Fuente canónica portable

El conocimiento importante vive en formatos abiertos: Markdown, YAML, JSON, CSV, texto plano. El PKA no debe depender exclusivamente de Notion, Obsidian, Airtable, Google Drive, ClickUp, Coda, ni ninguna otra app cerrada como **única fuente de verdad**.

**Test operativo:** si mañana la app cae, ¿se pierde el sistema? Si la respuesta es sí, no es fuente canónica.

**Aceptable:** usar apps externas como interfaz, indexador, o complemento de visualización. Inaceptable: que sean el único lugar donde existe la información.

### 2.2. Agnóstico en arquitectura, específico en ejecución

La arquitectura del PKA debe permitir sustituir LLM, base vectorial, herramienta, o aplicación **sin reconstruir todo el sistema**. La ejecución concreta sí puede usar herramientas específicas.

**Aplicación en /RAUL/:** Modelo A (ver §3.2) separa el conceptual SSOT (vendor-neutral) del thin-adapter (específico por LLM). Permite que el mismo agente conceptual se ejecute en Claude Code hoy y en otro runtime mañana sin reescribir la lógica.

### 2.3. Pocos agentes centrales, muchos contextos de dominio

**Recomendación canónica de la literatura PKA:** no escalar multiplicando agentes especializados. Escalar mediante contextos, reglas, taxonomías, plantillas, evaluaciones y validadores.

**Tensión documentada en /RAUL/:** /RAUL/ se ha desviado deliberadamente de este principio. Tiene ~30 agentes, no ~8. La justificación: en lugar de 8 agentes con prompts inflados que hacen "varios trabajos", /RAUL/ tiene agentes pequeños con responsabilidades cinceladas y handoffs explícitos. Esto produce trazabilidad superior y permite rotación de modelos por agente (Opus en Aurelio, Haiku en Ivo).

**Lección honesta:** la decisión de /RAUL/ no es universalmente correcta. Si tu PKA tendrá un solo operador con baja capacidad de mantener 30 agentes, mejor sigue el principio canónico (~8 agentes + domain packs ricos). /RAUL/ funciona porque su operador acepta el costo de mantener muchos agentes a cambio de claridad de boundaries.

**Regla de bolsillo:** empieza con pocos. Crea un agente nuevo solo cuando un boundary real lo justifique, nunca por anticipación.

### 2.4. Separación cinco-capas

El PKA distingue rigurosamente entre:

1. **Fuentes originales** (lo que llegó al sistema desde fuera).
2. **Notas / wiki** (lo que el operador o el sistema interpretaron sobre las fuentes).
3. **Proyectos activos** (trabajo en curso por dominio).
4. **Outputs** (entregables finales).
5. **Operaciones / governance / agentes** (la maquinaria que produce los anteriores).

Mezclar estas capas es la causa raíz de la mayoría de PKAs muertos: una nota interpretativa se confunde con una fuente, una decisión queda enterrada en un proyecto, un output viejo se trata como verdad actual.

### 2.5. Trazabilidad obligatoria

Toda conclusión, decisión, recomendación, output o acción relevante debe poder rastrearse a:

- Fuente (¿de dónde salió?).
- Dominio (¿a qué área del sistema pertenece?).
- Fecha (¿cuándo fue válido?).
- Agente / workflow que lo generó (¿quién lo produjo?).
- Confianza (¿qué tan robusto es?).
- Estado (¿vigente, obsoleto, en revisión?).

**Test operativo:** elige una recomendación cualquiera del sistema. ¿Puedes en menos de 2 minutos identificar fuente, fecha, autor y confianza? Si no, hay deuda de trazabilidad.

### 2.6. Revisión humana en límites claros

El operador humano debe ser el último filtro para acciones de alto blast radius:

- Publicación externa de contenido.
- Envío de mensajes / emails / eventos.
- Borrado de información canónica.
- Modificación de memoria crítica.
- Decisiones financieras, legales, médicas, reputacionales.
- Acciones sobre infraestructura compartida.

Para todo lo demás (lectura, edición de borradores, propuestas), el sistema puede operar sin pedir confirmación.

**Anti-patrón:** pedir confirmación para todo. Erosiona la confianza del operador y entrena a aprobar sin leer.

### 2.7. Reconstruibilidad desde fuente

Si pierdes índices, caches, dashboards o memoria volátil, debes poder reconstruir el sistema desde la fuente canónica.

**Test operativo:** simula pérdida de `04-system/05-indexes/`. ¿El sistema se recupera? Si no, los índices están haciendo trabajo de fuente canónica y eso es un bug arquitectural.

### 2.8. Autosostenibilidad

El sistema debe poder **crecerse a sí mismo**. Debe existir un mecanismo para:

- Investigar un dominio nuevo (research).
- Diseñar agentes nuevos (hire).
- Validar que el resultado encaja con la arquitectura existente.

En /RAUL/ esto vive en Tier 0: Raul (orchestrator), Paxs (research), Michelina (hiring). Sin este kernel, cada extensión del sistema requiere intervención manual del operador, lo que vuelve el sistema lento de evolucionar.

### 2.9. Vendor-neutralidad multi-LLM

El PKA debe sobrevivir al cambio de proveedor de LLM. Modelo A (§3.2) es la implementación operativa de este principio.

### 2.10. Aprendizaje continuo medible

El sistema debe tener un canal explícito para incorporar aprendizajes:

- Feedback del operador → memoria persistente.
- Fricciones detectadas → ajustes a agentes / workflows.
- Decisiones tomadas → registro en DECISIONS.md.
- Errores cometidos → patrón documentado para no repetir.

**Anti-patrón:** depender de la memoria del operador para no repetir errores. La memoria humana es poco confiable a 6 meses; el sistema debe materializar el aprendizaje.

### 2.11. Aprendizaje del operador como subsistema

El PKA tiene **dos funciones**, no una:

1. **Producir outputs** para el operador (lo que la mayoría de PKAs declaran).
2. **Observar al operador y devolverle insights sobre sí mismo** — patrones de decisión, fortalezas activas, antipatrones recurrentes, ángulos ciegos, distancia entre estilo dominante y estilo aspiracional.

La segunda función es **subsistema explícito**, no efecto secundario. Materializarla requiere:

- **Observation log estructurado** del operador (no eventos sueltos: patrones agregados).
- **Reflection cycles periódicos** que producen reportes de patrones (no sugerencias en tiempo real, no interrupciones del flujo).
- **Validación humana antes de internalización** — los insights no se vuelven memoria del sistema ni del operador automáticamente.

**Distinción crítica que marca un límite duro:**

| Función | Quién es el actor | Quién es el revisor | Riesgo |
|---|---|---|---|
| Mirror coach (observa y devuelve insights) | Humano sigue actuando | Humano valida insights | Bajo |
| Clon mejorado (actúa por el operador) | Sistema actúa | Humano revisa después | Alto, opaco |

Mirror coach es **pre-requisito** de cualquier delegación de voz. Sin auto-conciencia activa del operador, un clon amplifica sesgos más rápido de lo que el operador los detecta.

**Advertencia crítica — el punto ciego estructural del clon:** un clon mejorado puede aprender a "sonar bien" ante el operador precisamente porque está amplificando sus sesgos con más consistencia que el operador mismo. Cuando el operador revisa el output y lo aprueba porque "suena como yo", esa aprobación no es prueba de que el output esté libre de sesgos — al contrario, "sonar como yo" puede ser el síntoma del problema. La validación humana es condición necesaria pero **no suficiente**: el operador no puede detectar sus propios ángulos ciegos por definición. Esto es argumento adicional, no decorativo, para Mirror Coach previo: si el operador no sabe cuáles son sus sesgos, no puede detectarlos en el output del clon. Ningún nivel de revisión humana resuelve este punto ciego sola — solo el trabajo previo de auto-conciencia del operador lo mitiga.

**Anti-patrón:** automatizar "el sistema decide por ti" antes de que el operador haya validado al menos 3 ciclos de reflection report con cambios de comportamiento adoptados.

---

## 3. Arquitectura de referencia /RAUL/

Esta sección describe cómo /RAUL/ materializa los principios. Otros PKAs pueden materializarlos de otra forma; lo importante son los principios, no las decisiones de implementación específicas.

### 3.1. Estructura de carpetas

```text
RAUL/
├── 01-inbox/                    # Buzones operativos (gitignored)
│   ├── 01-owner-to-raul/
│   ├── 02-deliverables-to-owner/
│   └── 03-raw-sources/
│
├── 02-knowledge-base/           # Conocimiento canónico
│   ├── 00-raul-intelligence/    # Memoria del propio sistema (este archivo vive aquí)
│   ├── 01-foundations/          # Principios y reglas universales
│   ├── 02-domains/              # Wikis por dominio (Genteca, Plenus, etc.)
│   ├── 03-cross-cutting/        # Conocimiento transversal
│   ├── 04-sops-and-playbooks/   # Procedimientos canónicos
│   └── 05-glossary-and-tables/  # Glosario y tablas de referencia
│
├── 03-projects/                 # Proyectos activos por dominio
│   ├── genteca/
│   ├── plenus/
│   └── ...
│
├── 04-system/                   # Maquinaria del sistema
│   ├── 01-config/               # FOLDER-ARCHITECTURE, CONTEXT
│   ├── 02-agents/               # Conceptual SSOT + thin-adapters
│   │   ├── conceptual/          # Vendor-neutral SSOT
│   │   ├── content-supply-chain/ # Documentos transversales del CSC
│   │   └── _taxonomy.md
│   ├── 03-governance/           # DECISIONS, MIGRATION-PLAN, RISK-POLICY
│   ├── 04-tools-and-scripts/    # Scripts auxiliares
│   ├── 05-indexes/              # Índices derivados (reconstruibles)
│   └── 06-companion-docs/       # Fuentes externas no canónicas
│
└── 05-archive/                  # Histórico (gitignored, backup aparte)
```

**Mapeo a la estructura PKA genérica del checklist auditor:**

| /RAUL/ | PKA genérica | Comentario |
|---|---|---|
| `01-inbox/` | `00_inbox/` | Coincide |
| `01-inbox/03-raw-sources/` | `01_sources/` | /RAUL/ los trata como inbox operativo, no como capa permanente |
| `02-knowledge-base/02-domains/` | `02_wiki/` | Wiki por dominio |
| `03-projects/` | `03_projects/` | Coincide |
| (no existe estandarizado) | `04_operations/` | Tasks/calendar viven en apps externas (Drive/Calendar) — gap aceptado |
| `01-inbox/02-deliverables-to-owner/` | `05_outputs/` | /RAUL/ entrega vía inbox al owner |
| `04-system/02-agents/` | `06_agents/` | Coincide |
| `02-knowledge-base/00-raul-intelligence/` | `07_memory/` | Coincide en función |
| `04-system/05-indexes/` | `08_indexes/` | Coincide |
| (no existe formal) | `09_integrations/` | Diferido — /RAUL/ asume Claude Code primario por ahora |
| (parcial vía Ivo IV-1) | `10_logs/` | Gap parcial — ver §10 |

### 3.2. Modelo A: Conceptual SSOT + Thin-Adapter

Innovación core de /RAUL/. Cada agente existe en dos formas:

**Conceptual SSOT** (`04-system/02-agents/conceptual/<agente>.md`):
- Vendor-neutral, ~600-1000 líneas.
- Identity, mission, scope, boundaries, outputs codificados, interactions, antipatterns, examples.
- Lo escribe el operador (con asistencia de un LLM). Es la fuente de verdad.

**Thin-Adapter** (`.claude/agents/<agente>/AGENT.md`):
- Específico por runtime (Claude Code en /RAUL/), ~100 líneas.
- Frontmatter con `description`, `tools`, `model`. Body con path mappings y runtime notes.
- Apunta al conceptual. **Nunca duplica lógica.**

**Por qué importa:** cuando aparezca un runtime mejor (otro LLM, otro orquestador), se reescribe el thin-adapter. El conceptual no se toca. La inversión cognitiva del operador en diseñar el agente NO se pierde.

**Test operativo:** elige un agente. ¿Puedes leer solo el conceptual y entender qué hace? ¿El thin-adapter aporta solo plomería de runtime? Si el thin-adapter contiene lógica de negocio, hay leak.

### 3.3. Taxonomía 6 clases de agentes

Lock 2026-05-01. Cada agente del sistema pertenece a UNA y solo UNA clase:

| Clase | Función | Ejemplos /RAUL/ |
|---|---|---|
| **Orchestration** | Coordina y delega | Raul |
| **Governance** | Vigila riesgo, calidad, decisiones | Bruna |
| **Global-service** | Servicio transversal multi-dominio | Paxs (research), Michelina (hiring), Vivienne (slides) |
| **Domain-specialist** | Experto vertical de un dominio | Vera, Renzo, Oz, Orlan (Genteca) |
| **Content-supply-chain** | Producción editorial / audiovisual | Aurelio, Vael, Solenne, Nerea, Atlas, Luma, Vela, Orfeo, Sira, Celeste, Ivo |
| **Execution-utility** | Acciones operativas concretas | Inboxbot |

**Por qué importa:** sin esta taxonomía, cada agente nuevo se diseña desde cero y termina con boundaries borrosos. Con la taxonomía, hay 6 plantillas mentales que aceleran el diseño y previenen overlap.

### 3.4. Familias de outputs codificados

Cada agente productor tiene una familia de outputs nombrada y numerada:

- AU-1, AU-2, ... AU-5 → outputs de Aurelio (Content Strategist).
- VA-1 ... VA-5 → outputs de Vael (Brand & Messaging).
- BR-1 ... BR-5 → outputs de Bruna (Risk & Claims Governance).
- ... y así para todos.

**Por qué importa:**
- Trazabilidad: "esta pieza viene de SO-3 que consumió VA-4 con BR-2 aplicado".
- Rúbricas: cada output tiene criterios de calidad propios.
- Reciclaje: Sira indexa por familia, no por archivo, lo que permite recuperación semántica.

### 3.5. Gates secuenciales

El Content Supply Chain (CSC) tiene gates explícitos en lugar de handoffs implícitos:

- Gate 1: brief estratégico aprobado (Aurelio AU-1).
- Gate 2: arquitectura de mensaje aprobada (Vael VA-X).
- Gate 3: claims gateados por riesgo (Bruna BR-X).
- Gate 4: copy / guion ejecutables (Solenne SO-X / Nerea NE-X).
- Gate 5: pieza producida y publicable (Atlas/Luma/Vela/Orfeo).

**Por qué importa:** cuando una pieza falla en producción, el log de gates muestra exactamente dónde se quebró la cadena. Sin gates, los handoffs se vuelven informales y la fricción se distribuye difusamente.

### 3.6. Memoria de dos capas

| Capa | Implementación | Persistencia | Quién edita |
|---|---|---|---|
| **Memoria volátil del runtime** | `.claude/projects/<repo>/memory/` (auto-memory de Claude Code) | Entre sesiones del mismo runtime | El LLM, supervisado por operador |
| **Memoria de governance** | `02-knowledge-base/00-raul-intelligence/` + `04-system/03-governance/DECISIONS.md` | Permanente, en git | Operador, en colaboración con LLM |

**Por qué importa:** la memoria volátil es rápida y barata pero específica de un runtime y un proyecto. Si cambias de runtime, se pierde. La memoria de governance es lenta de actualizar pero portable y auditable. Un PKA serio tiene ambas.

---

## 4. Roadmap de construcción en 6 fases

### Fase 0 — Cimientos (semana 1-2)

**Objetivo:** levantar la estructura mínima portable.

**Entregables:**
- Estructura de carpetas top-level (5-7 carpetas máximo).
- `README.md` raíz: qué es el PKA, para qué sirve, cómo se usa.
- `.gitignore` que excluye buzones operativos, binarios, secretos, archivo histórico.
- `04-system/03-governance/DECISIONS.md` vacío con plantilla.
- `04-system/03-governance/RISK-POLICY.md` con principios mínimos de revisión humana.
- `02-knowledge-base/00-raul-intelligence/_index.md` con primeros archivos de memoria.
- Fuente canónica declarada explícitamente (qué carpeta es canon, qué es derivado).

**Criterio de salida:** un colaborador externo puede entender la estructura en 10 minutos leyendo solo el README. Si requiere explicación verbal, no está listo.

**Riesgo principal:** sobre-diseñar la estructura antes de tener trabajo real. Mantener mínimo viable.

### Fase 1 — Tier 0 (semanas 2-3)

**Objetivo:** kernel autosostenible que pueda hacer crecer al sistema.

**Entregables:**
- **Orchestrator** (en /RAUL/: Raul). Conceptual SSOT + thin-adapter. Sabe cómo delegar.
- **Researcher** (en /RAUL/: Paxs). Sabe investigar dominios desconocidos.
- **Hirer** (en /RAUL/: Michelina). Sabe diseñar agentes nuevos colaborando con el researcher.

**Criterio de salida:** el sistema puede recibir "necesito un agente que haga X" y entregar conceptual + thin-adapter listo, sin que el operador escriba el agente desde cero.

**Riesgo principal:** que los tres agentes Tier 0 hagan demasiado. Boundaries estrechas: orchestrator NO investiga, researcher NO contrata, hirer NO delega.

### Fase 2 — Cadena transversal (semanas 4-8)

**Objetivo:** una cadena funcional que opere a través de dominios.

**En /RAUL/ esto es el CSC** (Content Supply Chain): Aurelio → Vael → Bruna → Solenne/Nerea → Atlas/Luma/Vela/Orfeo → Sira/Celeste → Ivo.

**Otros PKAs pueden tener otras cadenas transversales:** investigación → análisis → reporte; ingesta → clasificación → archivado; intake → triage → derivación.

**Entregables:**
- Conceptual SSOT + thin-adapter para cada agente de la cadena.
- Documento de arquitectura que describe la cadena, los gates, las cadenas alternativas (B/C/D).
- Una primera campaña / pieza / output recorrido completo end-to-end (smoke test).

**Criterio de salida:** un brief entra al sistema y produce un output publicable, con log completo de la cadena y caveats integrados.

**Riesgo principal:** diseñar la cadena en abstracto. Solo el smoke test revela los gaps reales.

### Fase 3 — Activación de dominios + domain packs (continuo, paralelizable)

**Objetivo:** llevar el sistema a multi-dominio real con plantilla común.

**Por cada dominio nuevo:**
- Crear `02-knowledge-base/02-domains/<dominio>/` con domain pack (ver §5).
- Identificar gap de domain-specialists (qué Vera/Oz-equivalentes hacen falta).
- Hire round vía Tier 0: Paxs investiga el dominio → Michelina diseña los agentes → operador valida.
- Smoke test: la cadena transversal de Fase 2 produce un output dentro del dominio nuevo.

**Criterio de salida:** cada dominio activo tiene domain pack + N domain-specialists + 1 caso end-to-end validado.

**Riesgo principal:** activar más dominios de los que el operador puede mantener. Regla: máximo 1-2 dominios nuevos por mes, después de Fase 2 validada.

### Fase 4 — Validación end-to-end + métricas (semanas 12-16)

**Objetivo:** medir si el sistema funciona o solo existe.

**Entregables:**
- KPIs por dominio (output volume, time-to-publish, gate rejection rate, recycle rate).
- Golden outputs y rúbricas de evaluación por agente productor.
- Bitácora de fricciones reales por dominio.
- Iteración 1 sobre conceptuales con base en métricas, no en intuición.

**Criterio de salida:** dashboard "/PKA/ está produciendo X piezas/semana en Y dominios con Z% gate-rejection".

**Riesgo principal:** medir lo medible en lugar de lo importante. Las métricas deben servir a la fricción del operador, no a un cuadro estético.

### Fase 5 — Madurez operativa (continuo, después de F4)

**Objetivo:** el sistema aprende, no solo produce.

**Ciclos canónicos:**
- **Curation** (en /RAUL/: Celeste, cada 4-6 semanas). Qué entró a KB, qué se descartó, qué quedó pendiente.
- **Reciclaje** (en /RAUL/: Sira, cuando hay oportunidad detectada). Catálogo en `04-system/05-indexes/` actualizándose.
- **Logging operativo** (en /RAUL/: Ivo, por cada pieza publicada). Chain logs + outputs index.
- **Memoria institucional de riesgo** (en /RAUL/: Bruna BR-5). Precedentes por tipo de claim.
- **Auditoría trimestral** del propio sistema (ver §9).

**Criterio de salida:** dashboards en `04-system/05-indexes/` que un humano lee en 5 minutos para saber el estado del sistema.

**Riesgo principal:** ciclos que se vuelven ritual sin valor. Cada ciclo debe rendir output observable; si no, se elimina o se rediseña.

### Fase 6 — Mirror Coach + persona delegation (después de F5 estable)

**Objetivo:** materializar el principio §2.11 (aprendizaje del operador como subsistema). Esta fase **no se inicia hasta que F5 lleve al menos 3 meses estable** — antes carece de señal suficiente.

#### F6.1 — Observation log + Reflection cycles (Mirror Coach)

**Construye:** capacidad del sistema para devolver al operador insights sobre sus propios patrones de decisión.

**Entregables:**
- **Observation log estructurado** en `02-knowledge-base/00-raul-intelligence/operator-patterns/` (gitignored). Registra patrones agregados, no eventos sueltos. Ejemplo: "rechazo a verbosidad cuando hay >3 alternativas no acotadas" en lugar de "Raoul aprobó commit X a las 14:23".
- **Agente "Espejo / Coach"** (clase: governance o global-service). Conceptual SSOT + thin-adapter. Lee observation log + DECISIONS + memoria de governance. Produce reflection reports.
- **Reflection report mensual / trimestral** en `02-knowledge-base/00-raul-intelligence/reflection-reports/<YYYY-MM>.md`. **Estructura narrativa, no dashboard de bullets** (la literatura muestra que dashboards son ignorados a partir del tercer mes). Máximo 400 palabras. Estructura canónica:
  1. **Síntesis del período** (2-3 frases): qué tipo de período fue éste en términos del operador.
  2. **Patrón central observado** con evidencia concreta del observation log (no abstracción genérica; citar caso específico).
  3. **Patrón contra el grano** (ver §10.6): un insight que el operador ha tendido a ignorar, marcado explícitamente como tal. Permanece en cada reporte hasta validación o descarte activo.
  4. **Distancia estilo dominante vs aspiracional** en una sola dimensión concreta (ej.: "decides rápido cuando el dominio es técnico, pausas cuando es relacional"), no en abstracciones tipo "más asertivo / menos asertivo".
  5. **Una sola pregunta abierta al final** (ej.: "¿qué harías diferente si supieras esto hace 6 meses?"). El framing es de hipótesis, nunca de diagnosis.

  Voz del agente: "noté que..." nunca "tienes el patrón de...". El cambio de comportamiento debe ser autogenerado por el operador, no prescrito por el sistema.

- **Salvaguarda anti-echo-chamber.** El agente Espejo está en riesgo estructural de optimizar hacia los insights que el operador valida como "útiles" y dejar fuera los que ignora. Esto convierte el coach en confirmación de narrativa existente — exactamente lo opuesto a su función. Regla obligatoria del agente Espejo: cada reflection report debe incluir **al menos un insight de la categoría "ignorado N veces por el operador"** (donde N≥2). Si el operador lo ignora de nuevo, se registra y permanece en el siguiente reporte hasta que sea validado o descartado **activamente con justificación**. La inclusión de insights contra el grano no es opcional, es contractual del agente.

**Criterio de salida F6.1:** tres reflection reports leídos por el operador con al menos un cambio de comportamiento adoptado por insight del reporte (no por intuición previa). Los insights no aplicados también se registran — son señal sobre qué tipo de feedback el operador ignora.

**Riesgo principal:** reportes que el operador deja sin leer porque interrumpen flujo o porque son demasiado largos. Reflection report debe leerse en <10 minutos; si no, se rediseña.

#### F6.2 — Persona profile + delegated voice (clon acotado)

**Gateado por F6.1 funcionando 6+ meses con señal estable.** No se inicia antes.

**Construye:** capacidad de que ciertos agentes invoquen "voz delegada del operador" en superficies acotadas.

**Entregables:**
- **Persona profile** en `02-knowledge-base/00-raul-intelligence/persona-profile.md`. Voz, criterios de priorización, vetoes, antipatrones a evitar, estilos de escritura por contexto. Editable solo por el operador, nunca por agentes. Versionado con fecha de revisión cada 6 meses.
- **Lista explícita de superficies habilitadas** para voz delegada (ejemplo posible: redacción de emails personales bajo cierto umbral, priorización de backlog, respuestas a colaboradores recurrentes). Lista corta y conservadora.
- **Etiquetado obligatorio** de outputs que usen voz delegada como "voz delegada de Raoul" para que receptores humanos puedan calibrar.

**Reglas duras:**
- NUNCA voz delegada en decisiones irreversibles o de alto blast radius (legal, financiero, contractual con terceros, ruptura / despido / cierre de relaciones).
- NUNCA voz delegada sin firma de operador en la versión vigente del profile.
- El profile se revisa cada 6 meses; los humanos cambian, el clon también debe.

**Criterio de salida F6.2:** persona profile estabilizado (cambios menores entre revisiones consecutivas) + al menos un agente lo invoca productivamente sin que el operador detecte voz extraña en el output ni receptores humanos detecten artificialidad.

**Riesgo principal:** scope creep de superficies habilitadas. Cada nueva superficie debe ser autorizada explícitamente; nunca por defecto.

---

## 5. Domain packs: anatomía estándar

Todo dominio activo del PKA debe tener un domain pack. La plantilla canónica (adaptada del checklist PKA Genérico):

```text
02-knowledge-base/02-domains/<dominio>/
├── README.md                   # Qué es este dominio, alcance, fuera-de-alcance
├── domain_profile.md           # Audiencias, productos, voz, temas sensibles
├── glossary.md                 # Vocabulario interno y externo del dominio
├── taxonomy.md                 # Categorías, etiquetas, relaciones jerárquicas
├── risks.md                    # Tipos de riesgo activos (técnico, legal, reputacional)
├── workflows.md                # Cadenas operativas frecuentes (en prosa estructurada, no YAML)
├── tools_allowed.md            # Qué herramientas pueden usarse en este dominio
├── eval_rubrics.md             # Criterios de calidad para outputs del dominio
└── output_templates/           # Plantillas reutilizables (briefs, reports, posts)
```

**Adaptación para /RAUL/:** los domain packs viven en `02-knowledge-base/02-domains/<dominio>/` (wiki) y `04-system/06-companion-docs/<dominio>/` (fuentes externas). Para v0.1 de la metodología basta con los archivos de la plantilla; la integración wiki/companion-docs se pulirá en iteraciones futuras.

**Antipatrón:** crear un domain pack vacío con todos los archivos pero sin contenido real. Mejor tener 3 archivos completos que 9 placeholders.

**Criterio de salida de un domain pack:** un agente recién contratado para el dominio puede leer el pack y producir un output decente sin preguntar al operador.

---

## 6. Validadores especializados por tipo de riesgo

Gap a cerrar en /RAUL/ y patrón valioso del checklist PKA Genérico.

**Idea:** Bruna (en /RAUL/) o el "validator agent" (en otros PKAs) no debe ser un solo agente que evalúa todo riesgo. Debe ser un **meta-validador que delega a sub-validadores especializados** por tipo de riesgo.

**Tipos de validador recomendados:**

| Validador | Cuándo se activa | Qué evalúa |
|---|---|---|
| `safety_risk_validator` | Hay claims sobre seguridad física, técnica, eléctrica | Cumplimiento normativo, condiciones de operación |
| `health_or_wellbeing_validator` | Hay claims sobre salud o bienestar | Evidencia clínica, advertencias obligatorias |
| `financial_risk_validator` | Hay decisiones financieras o claims de retorno | Rangos de incertidumbre, disclaimers |
| `legal_compliance_validator` | Hay términos contractuales o legales | Jurisdicción, cláusulas obligatorias |
| `technical_accuracy_validator` | Hay especificaciones técnicas | Cross-check con fuentes, rangos de tolerancia |
| `privacy_security_validator` | Hay datos personales o secretos | PII, anonimización, exposición de credenciales |
| `reputational_risk_validator` | Hay contenido público o referencia a terceros | Tono, atribución, derecho de respuesta |
| `claims_evidence_validator` | Hay claim que requiere RTB | Trazabilidad a fuente verificable |
| `data_quality_validator` | Hay agregaciones o transformaciones de datos | Outliers, missingness, sesgo |
| `publication_readiness_validator` | Antes de publicar | Formato, branding, caveats integrados |

**Activación:** por **tipo de riesgo detectado en el output**, no por dominio. Un mismo dominio puede activar 0, 1 o varios validadores en una misma pieza.

**Implementación recomendada:** cuando /RAUL/ active esta capa, Bruna se mantiene como meta-validador (gate 4 fases del CSC) y los sub-validadores se invocan como agentes hijo cuando Bruna detecta el tipo de riesgo correspondiente. Defer a Fase 5 / 6.

---

## 7. Memoria explícita estructurada

Gap parcial en /RAUL/ — la auto-memory de Claude Code cubre parte, pero la memoria explícita en repo (legible por humanos y otros runtimes) es más débil.

**Archivos canónicos recomendados** (`02-knowledge-base/00-raul-intelligence/`):

| Archivo | Contenido | Editable por agentes |
|---|---|---|
| `user_profile.md` | Quién es el operador, contexto, roles | No, solo humano |
| `preferences.md` | Cómo le gusta que se trabaje | Sí, con confirmación |
| `constraints.md` | Restricciones (legales, contractuales, personales) | No, solo humano |
| `decisions.md` | Espejo / extracto de DECISIONS.md relevante para agentes | No, derivado |
| `goals.md` | Objetivos vigentes por dominio | Sí, con confirmación |
| `people.md` | Personas importantes, roles, cómo interactuar | Sí (registrar contactos) |
| `organizations.md` | Organizaciones clave, contexto | Sí (registrar) |
| `writing_style.md` | Voz y tono del operador | No, solo humano |
| `domain_boundaries.md` | Reglas explícitas de no-cross-contamination entre dominios | No, solo humano |
| `terminology.md` | Vocabulario preferido / a evitar | Sí, con confirmación |
| `active_context.md` | Qué está en curso ahora mismo | Sí |

**Distinción clave:** memoria editable por agentes vs solo humano. Las restricciones legales y la voz del operador NUNCA deben ser editadas por un LLM sin revisión.

**Estado /RAUL/:** parcial. Los archivos `estilo-y-voz.md`, `patrones-de-delegacion.md`, `preferencias-del-owner.md`, `aprendizajes-genteca.md` cubren parte. Falta: `constraints.md`, `goals.md`, `domain_boundaries.md` formal. Iteración futura.

---

## 8. Tool Registry y schemas

Gap declarado en /RAUL/, diferido a Fase 5+.

### 8.1. Tool Registry

Cada herramienta que un agente puede invocar debe estar registrada con:

```text
- name: gmail.create_draft
- description: Crea un draft de email en Gmail
- inputs: { to, subject, body }
- outputs: { draft_id, status }
- permissions: { read: false, write: true, send: false }
- human_approval_required_for: [send]
- error_modes: [auth_expired, recipient_invalid, rate_limited]
```

**Por qué importa:** sin registry, los permisos y blast radius de cada herramienta están enterrados en cada agente. Con registry, hay un solo lugar para auditar "qué puede hacer el sistema sin pedir permiso".

### 8.2. Schemas para outputs estructurados

Cada familia de outputs (AU-X, VA-X, etc.) debería tener un schema explícito (JSON Schema o equivalente liviano en YAML).

**Por qué importa:** valida automáticamente que los outputs cumplen estructura esperada antes de pasar al siguiente gate. Reduce errores de handoff.

**Estado /RAUL/:** los outputs tienen estructura descrita en prosa en cada conceptual. Suficiente para v0.1 de la metodología. Schema formal diferido.

---

## 9. Sistema de auditoría y madurez

### 9.1. Sistema de puntuación 0-5

Adaptado del checklist PKA Genérico. Para cada área del sistema:

| Puntaje | Significado |
|---:|---|
| 0 | No existe |
| 1 | Existe mínimo, incompleto, desordenado |
| 2 | Existe parcial, sin estándar |
| 3 | Funciona aceptable, brechas visibles |
| 4 | Bien implementado, documentado, usable |
| 5 | Excelente, completo, mantenible, probado |

### 9.2. Cadencia recomendada

- **Auditoría trimestral** del sistema completo. Resultado: reporte en `02-knowledge-base/00-raul-intelligence/methodology/audits/<YYYY-QX>.md`.
- **Mini-auditoría mensual** de un área específica (rotando: agentes, dominios, governance, etc.).
- **Auditoría ad-hoc** cuando se detecte fricción recurrente o cuando un cambio mayor entre.

### 9.3. Criterios de salud (15 ítems)

El PKA puede considerarse saludable si cumple:

- [ ] Estructura clara y navegable sin guía externa.
- [ ] Fuente canónica portable identificada.
- [ ] Tier 0 (orchestrator + research + hire) operativo.
- [ ] Al menos una cadena transversal validada end-to-end.
- [ ] Domain packs para todos los dominios activos.
- [ ] Memoria explícita en repo, complementaria a la auto-memory.
- [ ] DECISIONS.md viva (entradas en últimos 30 días si hubo trabajo).
- [ ] Boundaries entre dominios documentados.
- [ ] Validadores activos para los tipos de riesgo del operador.
- [ ] Trazabilidad de outputs a fuentes (test: 2 minutos por output).
- [ ] Reconstruibilidad probada (test: borrar índices y recuperar).
- [ ] Backups automatizados a un canal alternativo (no-git).
- [ ] Logs de ejecuciones consultables (al menos del último mes).
- [ ] Reglas de seguridad / privacidad documentadas.
- [ ] Auditoría trimestral ejecutada al menos una vez.

### 9.4. Reportes de auditoría

Plantilla en `02-knowledge-base/00-raul-intelligence/methodology/audits/_template.md` (cuando exista). Estructura mínima:

1. Resumen ejecutivo.
2. Puntajes por área.
3. Brechas por severidad (crítica / alta / media / baja).
4. Recomendaciones priorizadas.
5. Próxima auditoría: fecha + foco.

---

## 10. Aprendizajes operativos /RAUL/

Patrones validados en construcción real. No son universales — son lo que ha funcionado para /RAUL/ específicamente. Otros PKAs validarán los suyos propios.

### 10.1. Comunicación humano ↔ sistema

- **Drafts en texto antes de escribir a disco.** Cuando el LLM va a producir un archivo no trivial, primero muestra el draft completo en chat. El operador valida o corrige. Solo después se escribe. Reduce reescrituras y permission loops.
- **Esperar autorización literal.** Para operaciones de blast radius medio o alto, el sistema pide confirmación explícita y espera literal "Ejecuta paso X" o equivalente. No "tú decides" implícito.
- **No auto-continuar después de validación parcial.** Si una sub-tarea fue aprobada, el sistema NO continúa con el resto del plan automáticamente. Cada hito requiere reautorización.
- **Resumir al cierre con qué cambió y qué sigue, en 1-2 frases.** No reportes largos. El operador lee el diff si quiere detalle.

### 10.2. Migración / refactor

- **Pause entre agentes en migraciones grandes.** Migrar 12 agentes en una sesión satura al operador. Pausar 1-2 días entre cada uno permite validar uso real.
- **Preservar histórico al reorganizar.** Archivos obsoletos van a `06-companion-docs/` o equivalente, no se borran. Recuperar después es más barato que perder contexto.
- **Cambios estructurales en commits temáticos.** No commit-único de "todo el cambio". 4-5 commits temáticos por área permiten revertir parcial sin reescribir el sistema.

### 10.3. Antipatterns observados

- **Agentes con scope difuso "el experto en X".** Sin lista explícita de outputs y boundaries, el agente termina haciendo de todo y nada bien.
- **Memoria "evergreen".** La memoria sin fecha y sin estado se vuelve ruido en 6 meses. Toda entrada de memoria debe tener fecha y un mecanismo de decaimiento.
- **Pedir confirmación para todo.** Genera fatiga y entrena a aprobar sin leer.
- **Documentación desincronizada.** Conceptual dice X, runtime hace Y, README dice Z. La verdad operativa es lo que el agente ejecuta, no lo que dice el doc. Cuando se detecta divergencia, sincronizar todo el stack en una sola pasada.

### 10.4. Decisiones reversibles vs irreversibles

- **Reversibles** (proceder sin pedir confirmación si están dentro del scope autorizado): editar archivos en repo, crear conceptuales, reorganizar carpetas.
- **Irreversibles o de alto blast radius** (siempre pedir confirmación): commit-push a remote, borrado de archivos, envío de mensajes externos, modificación de memoria crítica, cambios en branding del operador.

**Test del costo de pausar:** si el costo de pausar para confirmar es menor que el costo de revertir un error, pausar siempre.

### 10.5. Hire de agentes nuevos

Patrón validado:

1. **Trigger:** detectar fricción recurrente que ningún agente actual cubre.
2. **Research** (Paxs en /RAUL/): qué hacen profesionales humanos en ese rol, qué herramientas usan, qué outputs entregan.
3. **Persona design** (Michelina en /RAUL/): conceptual SSOT con identity, mission, scope, boundaries, outputs, antipatterns.
4. **Validación humana del conceptual** ANTES de crear thin-adapter.
5. **Thin-adapter** específico al runtime.
6. **Smoke test** con caso real.
7. **Iteración 1** después del primer uso real, no antes.

**Antipatrón:** diseñar el agente perfecto en el papel antes de probarlo. La primera versión siempre tiene boundaries equivocados; el uso revela cuáles.

### 10.6. Aprendizajes del operador

Patrones que rigen la relación operador ↔ sistema cuando éste devuelve insights al operador (Mirror Coach, Fase 6.1). Documentados aquí aunque la fase no esté operativa todavía, porque las reglas previenen errores de diseño desde antes.

- **El sistema NO propone cambios de comportamiento al operador en tiempo real.** Reportes son periódicos (mensual o trimestral). Interrumpir el flujo erosiona confianza y el operador desconecta.
- **El operador valida cada insight antes de internalizar.** Los insights del reflection report no se vuelven memoria del sistema ni del operador automáticamente. Revisión activa requerida.
- **El observation log es propiedad del operador.** Ningún output externo, ningún agente productor, ninguna pieza publicada cita patrones del operador. Es introspección, no material de marketing.
- **La persona profile se versiona y se firma.** Cambios mayores requieren firma explícita del operador en el archivo (ejemplo: línea `operator-approved: 2026-MM-DD`). Sin firma vigente, agentes no usan el profile.
- **Los insights no aplicados también son señal.** Si el operador ignora repetidamente un patrón propuesto, eso enseña al sistema qué tipo de feedback es ruido vs señal para este operador.
- **Mirror coach precede a clon.** Sin §2.11 funcionando, voz delegada queda prohibida. La regla protege al operador de ser desplazado por un clon que aprendió sus sesgos.
- **Anti-echo-chamber por diseño.** El agente Espejo NO puede entregar reportes que sean solo confirmación de la narrativa que el operador ya tiene de sí mismo. Cada reporte incluye al menos un insight ignorado ≥2 veces, marcado explícitamente. La salvaguarda es contractual del agente, no opcional. Razón: sin diseño activo, el sistema converge hacia confirmar lo que el operador valida como útil — exactamente lo opuesto a coaching real (riesgo documentado en literatura de chatbots de reflection).

---

## 11. Lo que descartamos del checklist PKA Genérico

| Recomendación descartada | Justificación |
|---|---|
| 10 dominios genéricos numerados (`dominio_01-10`) | /RAUL/ usa dominios reales nombrados (Genteca, Plenus, etc.), dimensionados por necesidad real. La numeración rígida no aporta. |
| LLM Gateway elaborado como capa explícita | Modelo A (conceptual SSOT + thin-adapter) cubre el agnosticismo necesario sin overhead de gateway. Reevaluable cuando /RAUL/ corra simultáneamente en >1 runtime. |
| Workflows en YAML formal estandarizado | Para PKA personal, los workflows como prosa estructurada en cada conceptual son más legibles y menos frágiles. YAML diferido a F5+ si se necesita orquestación automatizada. |
| JSON Schema formal desde día 1 para todos los outputs | Overhead alto para PKA personal. Estructura en prosa basta para v0.1. Schema formal diferido a F5+ cuando haya validación automática real. |
| Client discovery questionnaire / workshop guide | No aplica para PKA personal sin clientes externos. El operador es proveedor y consumidor. |
| Clonación completa del operador como objetivo del PKA | El clon sin Mirror Coach previo amplifica sesgos sin que el operador los detecte. Si llega, la clonación es subordinada a la auto-conciencia del operador (§2.11), no su sustituto. Voz delegada solo en superficies acotadas, gateada por F6.1 estable, etiquetada como tal. |

---

## 12. Glosario

- **PKA:** Personal Knowledge Assistant. Sistema integrado de archivos, agentes LLM, governance y workflows que asiste a una persona en gestión de conocimiento y producción de outputs.
- **Conceptual SSOT:** Single Source of Truth conceptual. Documento vendor-neutral que define un agente. No depende de runtime específico.
- **Thin-adapter:** capa fina específica del runtime que invoca al conceptual. ~100 líneas, sin lógica de negocio.
- **Modelo A:** la combinación Conceptual SSOT + Thin-Adapter. Patrón de diseño core de /RAUL/ que materializa el principio de vendor-neutralidad.
- **Familia de outputs:** conjunto numerado de outputs codificados de un agente productor (AU-1..AU-5, VA-1..VA-5, etc.).
- **Gate:** punto de control en una cadena de producción donde un output debe ser aprobado antes de avanzar al siguiente paso.
- **Domain pack:** conjunto estandarizado de archivos que define un dominio (profile, glossary, taxonomy, risks, workflows, tools, rubrics, templates).
- **Tier 0:** kernel autosostenible compuesto por orchestrator + researcher + hirer.
- **CSC:** Content Supply Chain. Cadena transversal de /RAUL/ desde brief estratégico hasta publicación.
- **Auto-memory:** memoria volátil específica de un runtime LLM (en /RAUL/: la de Claude Code en `.claude/projects/<repo>/memory/`).
- **Memoria de governance:** memoria permanente en repo, portable entre runtimes (en /RAUL/: `02-knowledge-base/00-raul-intelligence/` + `DECISIONS.md`).

---

## 13. Referencias y companion docs

- `04-system/03-governance/DECISIONS.md` — registro vivo de decisiones del sistema.
- `04-system/03-governance/MIGRATION-PLAN.md` — plan operativo de migración.
- `04-system/03-governance/RISK-POLICY.md` — política de riesgo y revisión humana.
- `04-system/01-config/FOLDER-ARCHITECTURE.md` — arquitectura de carpetas detallada.
- `04-system/02-agents/_taxonomy.md` — taxonomía de las 6 clases de agentes.
- `04-system/02-agents/content-supply-chain/ARCHITECTURE_Content-Supply-Chain.md` — arquitectura del CSC.
- `02-knowledge-base/00-raul-intelligence/methodology/_private/Apendice_A_Notas_Privadas.md` — apéndice privado (gitignored).

**Documentos externos consultados para esta v0.1:**
- `PKA_AUDIT_CHECKLIST_GENERIC.md` v1.0 (referencia auditora). Adoptado parcialmente, descartes documentados en §11.

---

## Changelog

### v0.3 — 2026-05-04

- Incorporadas 3 mejoras destiladas del reporte de investigación de Paxs (`_private/research/2026-05-04_paxs_ai-coach-cloning.md`):
  - **R1** — Reflection report rediseñado de dashboard de bullets a formato narrativo de máximo 400 palabras con 5 partes canónicas (síntesis, patrón central con evidencia, patrón contra el grano, distancia estilo dominante vs aspiracional, una pregunta abierta). Voz "noté que..." en lugar de "tienes el patrón de...". Razón: la literatura de positive computing muestra que dashboards de bullets se ignoran a partir del tercer mes; reportes narrativos con pregunta abierta correlacionan con cambio de comportamiento adoptado.
  - **R2** — Salvaguarda anti-echo-chamber añadida como regla contractual del agente Espejo (en F6.1 entregables y §10.6). Cada reflection report debe incluir al menos un insight de categoría "ignorado N≥2 veces por el operador", marcado explícitamente, que permanece hasta validación o descarte activo con justificación. Razón: sin diseño activo, los sistemas de reflection convergen hacia confirmar la narrativa del operador (echo chamber), riesgo documentado en literatura de chatbots de reflection.
  - **AC1** — Advertencia crítica añadida a §2.11: el clon puede aprender a "sonar bien" precisamente porque amplifica los sesgos del operador con más consistencia de la que el operador mismo tiene. La validación humana es necesaria pero no suficiente; el operador no puede detectar sus propios ángulos ciegos por definición. Argumento estructural adicional para Mirror Coach previo.
- 5 recomendaciones (R3-R8) y 4 advertencias (AC2-AC5) del reporte de Paxs **diferidas a v0.4+** porque son fixes preventivos contra riesgos que aún no se materializan (Fase 6 está a meses de distancia). Reporte completo preservado en `_private/research/2026-05-04_paxs_ai-coach-cloning.md` para reactivación cuando se diseñe el conceptual del agente Espejo.

### v0.2 — 2026-05-04

- Añadido principio §2.11 "Aprendizaje del operador como subsistema": el PKA tiene dos funciones (producir outputs + devolver insights al operador). Distinción Mirror Coach vs Clon Mejorado con límite duro entre ambos.
- Añadida Fase 6 al roadmap: F6.1 Mirror Coach (observation log + reflection cycles + agente Espejo) y F6.2 Persona Profile + Delegated Voice (gateado por F6.1 estable 6+ meses). Reglas duras de blast radius para voz delegada.
- Añadida §10.6 "Aprendizajes del operador": 6 patrones que rigen la relación operador ↔ sistema cuando éste devuelve insights (cadencia, validación humana, propiedad del log, firma del profile, señal de insights ignorados, prerrequisito Mirror Coach → clon).
- Añadida entrada en §11 descartando "clonación completa del operador como objetivo del PKA" con justificación.
- Solo metodología — no se construye nada operativo en esta versión. F6 declarada pero no iniciada.

### v0.1 — 2026-05-04

- Versión inicial.
- Outline aprobado previamente con 14 secciones + apéndice privado.
- Incorpora 10 ideas valiosas del checklist PKA Genérico (§5, §6, §7, §8, §9 principalmente).
- Documenta 5 descartes del checklist con justificación (§11).
- Eleva 8 patrones /RAUL/ a metodología generalizable (§3, §10).
- Apéndice privado en `_private/` excluido de git.
