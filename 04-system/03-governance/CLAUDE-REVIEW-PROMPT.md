---
document_id: "CLAUDE-REVIEW-PROMPT"
document_type: "instruction-template"
author: "GitHub Copilot (Copilot Chat in VS Code)"
creation_date: "2026-05-08"
purpose: "Proporcionar un prompt estructura para que Claude Opus 4.7 revise y evalúe los 3 documentos de auditoría PKA antes de ejecutar cambios"
audience: ["Raoul Bermúdez", "Claude Opus 4.7"]
status: "ready-to-use"
ssot_for: []
depends_on: ["PKA-AUDIT-CHECKLIST.md", "PKA-IMPROVEMENTS-SUMMARY.md", "PKA-FLOW.md"]
version: "1.0"
how_to_use: "Copiar este prompt completo (desde 'Contexto' hasta 'Firma') y pegarlo en Claude Opus. Claude evaluará y responderá con sugerencias estructuradas."
---

# CLAUDE-REVIEW-PROMPT.md
## Instrucción estructurada para que Claude Opus 4.7 revise los documentos de auditoría del PKA

**Propósito:** Proporcionar un prompt template que Raoul puede copiar y pegar directamente en Claude Opus para obtener evaluación estructurada de los documentos de auditoría.

---

## INSTRUCCIÓN PARA COPIAR Y PEGAR EN CLAUDE OPUS 4.7

```
=================================================================
CONTEXTO
=================================================================

Soy Raoul Bermúdez. Tengo un PKA (Personal Knowledge Assistant) 
local-first y vendor-neutral, construido con ayuda de Claude Opus 4.7 
e inspirado en metodología ICOR-TOM.

Mi equipo incluye:
- GitHub Copilot (análisis automático, recomendaciones)
- Claude Opus 4.7 (evaluación, decisiones arquitectónicas)
- Agentes especializados (Vera, Orlan, Solenne, Vael, Celeste, etc.)

El PKA está documentado en: /RAUL/04-system/

=================================================================
DOCUMENTOS A REVISAR
=================================================================

He solicitado a GitHub Copilot que haga una auditoría de mi PKA y 
prepare 3 documentos:

1. PKA-AUDIT-CHECKLIST.md
   → Checklist operacional para validar que el PKA sigue sus principios
   → Ubicación: 04-system/03-governance/PKA-AUDIT-CHECKLIST.md

2. PKA-IMPROVEMENTS-SUMMARY.md
   → Análisis técnico y recomendaciones de mejora priorizadas
   → Ubicación: 04-system/03-governance/PKA-IMPROVEMENTS-SUMMARY.md

3. PKA-FLOW.md
   → Guía visual y narrativa del flujo operativo (captura → archivo)
   → Ubicación: 04-system/01-config/PKA-FLOW.md

Todos incluyen frontmatter YAML que explica:
- author: GitHub Copilot
- purpose: su función específica
- status: draft-for-review (esperan tu evaluación)
- how_to_use: cómo usarlos

NOTA IMPORTANTE: Copilot también ejecutó una AUDITORÍA PROFUNDA 
(no solo análisis de documentos) y encontró hallazgos críticos:
- 3 scripts Python con rutas hardcodeadas
- Proyectos incompletos sin documentación
- Naming violations (carpetas con espacios)
Estos hallazgos están documentados en PKA-IMPROVEMENTS-SUMMARY.md 
(sección ⚠️ AUDITORÍA PROFUNDA) y en las actualizaciones de checklist.

=================================================================
TU TAREA
=================================================================

Revisa los 3 documentos y proporciona evaluación estructurada:

A) EVALUACIÓN GENERAL
   ├─ ¿Es correcto el análisis de la arquitectura actual del PKA?
   ├─ ¿Los documentos reflejan bien la realidad del sistema?
   └─ ¿Falta contexto o hay suposiciones incorrectas?

B) MEJORAS: ¿ESTÁN BIEN PRIORIZADAS?
   ├─ ¿Acuerdas con que SSOT y separación de índices son "Prioridad Alta"?
   ├─ ¿Hay mejoras que deberían ser más urgentes?
   └─ ¿Hay mejoras que son innecesarias o de bajo valor?

C) RIESGOS: ¿QUÉ NO VIO COPILOT?
   ├─ Cambios estructurales que podrían romper agentes o scripts
   ├─ Dependencias entre mejoras que no se mencionaron
   ├─ Conflictos con decisiones existentes en DECISIONS.md
   └─ Impacto en flujos operativos que podrían no ser obvios

D) ORDEN DE EJECUCIÓN
   ├─ ¿La secuencia propuesta es óptima?
   ├─ ¿Hay cambios que DEBEN ejecutarse juntos?
   └─ ¿Hay cambios que DEBEN ejecutarse separados?

E) FALTANTES O CAMBIOS
   ├─ ¿Hay mejoras importantes que Copilot no identificó?
   ├─ ¿Hay recomendaciones que deberían modificarse?
   ├─ ¿Hay scope creep o recomendaciones fuera de alcance?
   └─ ¿Algo contradice la filosofía local-first / vendor-neutral?

F) RECOMENDACIÓN FINAL
   ├─ ¿Ejecutar tal como está propuesto?
   ├─ ¿Ejecutar con cambios menores?
   ├─ ¿Rechazar algunas mejoras?
   └─ ¿Retrasar todo y revisar primero [X]?

=================================================================
FORMATO DE RESPUESTA SOLICITADA
=================================================================

Por favor, responde en este formato:

## A. EVALUACIÓN GENERAL
[Tu análisis en 2–3 párrafos]

## B. MEJORAS: ¿BIEN PRIORIZADAS?
[Tu evaluación de prioridades]

## C. RIESGOS NO IDENTIFICADOS
[Lista de riesgos que ves]

## D. ORDEN DE EJECUCIÓN RECOMENDADO
[Secuencia que recomiendas]

## E. CAMBIOS O FALTANTES
[Sugerencias específicas]

## F. RECOMENDACIÓN FINAL
[Tu veredicto: qué hacer]

## G. NOTAS ADICIONALES
[Contexto o aclaraciones]

=================================================================
CONTEXTO ADICIONAL (si lo necesitas)
=================================================================

Mi PKA actual tiene:
- 5 dominios principales (Genteca, Plenus, Finca, Teca, Marca personal)
- ~8 proyectos activos
- KB compilada en wiki/specs/assets por dominio
- Agentes conceptuales en 04-system/02-agents/conceptual/
- Índices en 04-system/05-indexes/ (sin separación de logs aún)

Mi filosofía:
- Local-first: archivos en disco, no en SaaS
- Vendor-neutral: Markdown + carpetas, sin lock-in
- Multi-LLM: Claude, Perplexity, GPT según tarea
- Sostenible: bajo mantenimiento, escalable a 15+ dominios

Mi equipo:
- Responsable: Raoul Bermúdez (Owner del PKA)
- Compilador KB: Celeste
- Especialistas por dominio: Vera, Orlan, Solenne, Vael, Renzo, Oz
- Agentes de operación: Paxs, conceptual agents

=================================================================
FIRMA
=================================================================

He preparado este prompt siguiendo recomendación de GitHub Copilot.
Espero tu evaluación antes de que él ejecute cualquier cambio.

Gracias,
Raoul Bermúdez

=================================================================
```

---

## Cómo usar este documento

1. **Copiar:** Selecciona TODO el contenido entre las líneas `=================================================================`
2. **Pegar en Claude Opus:** Abre [claude.ai](https://claude.ai) y pega en un nuevo chat
3. **Esperar respuesta:** Claude te dará evaluación estructurada con recomendaciones
4. **Registrar decisión:** Anota la respuesta de Claude y crea entrada en `DECISIONS.md`
5. **Compartir con Copilot:** Comparte la respuesta de Claude conmigo para ejecutar cambios aprobados

---

## Qué esperar de Claude

Claude Opus 4.7 te dirá:

- ✅ **Si el análisis es correcto** → Copilot identificó bien los problemas
- ⚠️ **Si hay riesgos ocultos** → Situaciones específicas que podrían romper algo
- 📋 **Orden óptimo de ejecución** → Qué hacer primero, qué después
- 💡 **Mejoras que faltan** → Cosas valiosas que Copilot no sugirió
- ❌ **Si hay que rechazar algo** → Cambios que no valen la pena o son riesgosos
- 🔄 **Recomendación final** → Veredicto claro sobre qué proceder

---

## Alternativa: Si prefieres hacer 2 instrucciones separadas

Si prefieres no incluir el prompt en los documentos de auditoría, puedes:

1. **Primero:** Los 3 documentos de auditoría (AUDIT-CHECKLIST, IMPROVEMENTS, FLOW)
2. **Después:** Una nueva sesión en Claude donde copias y pegas ESTE prompt

De cualquier forma, el prompt está listo para usar. Solo elige tu flujo preferido.

---

**Documento preparado por:** GitHub Copilot  
**Versión:** 1.0 | **Fecha:** 2026-05-08  
**Listo para usar:** Sí, copia todo entre las líneas `=================================================================`
