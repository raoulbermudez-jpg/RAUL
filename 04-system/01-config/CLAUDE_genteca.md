# CLAUDE_genteca.md
## Reglas específicas del dominio Genteca

**Versión:** 1.0
**Última actualización:** 2026-04-25
**Cargar junto con:** `CLAUDE_core.md` + `CONTEXT_genteca.md`

---

## Agentes disponibles para Genteca (Capa 3)

| Agente | Cuándo usarlo |
|--------|---------------|
| **Vera** | Selección o comparación de relés/protectores; IEC/NEMA; cross-referencia vs. ABB/Schneider/Eaton/Siemens |
| **Orlan** | Inteligencia de mercado, benchmarking competidores, market sizing, HMI trends |
| **Solenne** | Contenido B2B: blog, LinkedIn, email, video scripts, case studies, product copy |
| **Vael** | Estrategia de marca y mensajería, positioning, tono de voz, campaign briefs, launch kits |
| **Celeste** | Ingesta de documentos desde `01-inbox/03-raw-sources/` hacia KB; PDF/Word → Markdown |
| **Renzo** | Diagramas eléctricos (PNG/JPG/PDF), guías de instalación, troubleshooting técnico de campo |
| **Oz** | Redlines de fichas técnicas, PDFs anotados para Ozwaldo, delta documents de cambios visuales |

---

## Terminología técnica obligada

| Usar | Evitar |
|------|--------|
| tensión nominal | voltaje nominal |
| corriente nominal | amperaje (en contexto técnico) |
| relé de protección | protector (en contexto técnico formal) |
| protector de voltaje | regulador (para los productos de la línea residencial) |
| supervisión de fase | monitoreo de fase |
| IEC 60947 | solo la norma, sin parafrasear incorrectamente |

---

## Tono para contenido Genteca

- **B2B técnico industrial:** preciso, confiable, sin hipérbole.
- **B2C Exceline (residencial):** más directo, beneficio-centric, sin jerga técnica pesada.
- **LinkedIn / redes:** profesional, propósito claro, alineado con voz de la marca. No informalidad excesiva.
- Los materiales para **Ozwaldo** (diseñador) deben ser PDFs anotados o Markdown con instrucciones claras de cambio; nunca texto libre ambiguo.

---

## Equipo humano — routing de aprobaciones

| Persona | Rol | Qué necesita de Raul |
|---------|-----|----------------------|
| **Keiddys** | Gerente de Marca y Comunicaciones | Aprobaciones finales, estrategia, decisiones sobre tono y posicionamiento |
| **Valeria** | Experta en lenguaje y contenido; edita videos | Textos finales, scripts listos para grabación |
| **Oscar** | Audiovisuales e IA para imagen/video | Briefs de producción de video con spec clara |
| **Ozwaldo** | Diseño gráfico | PDFs anotados con deltas, briefs con todas las dimensiones y specs técnicas |

**Regla:** Raul nunca entrega directamente a Ozwaldo sin que Keiddys haya aprobado el contenido textual y técnico primero.

---

## Rutas clave Genteca

| Qué | Dónde |
|-----|-------|
| Índice de dominio | `02-knowledge-base/02-domains/01-genteca/_index.md` |
| Specs técnicas (192 docs) | `02-knowledge-base/02-domains/01-genteca/specs/` |
| Wiki compilada | `02-knowledge-base/02-domains/01-genteca/wiki/` |
| Market intelligence | `02-knowledge-base/02-domains/01-genteca/wiki/market/` |
| Assets visuales | `02-knowledge-base/02-domains/01-genteca/assets/` |
| Proyectos activos | `03-projects/genteca/` |
