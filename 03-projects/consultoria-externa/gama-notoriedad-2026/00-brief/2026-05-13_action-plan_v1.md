# Plan de acción — Gama Notoriedad 2026
**Fecha:** 2026-05-13
**Versión:** v1.1 (decisiones Owner cerradas 2026-05-13; respuestas Cora pendientes)
**Autor:** Claude para Raoul

---

## 0. Decisiones Owner 2026-05-13 (ratifican o cierran lo propuesto)

1. **Dominio definitivo:** `03-projects/consultoria-externa/gama-notoriedad-2026/`. Nuevo dominio abierto formalmente, primer cliente.
2. **División de trabajo:** Cora hace análisis estadístico; Raoul hace deck y narrativa Minto; Claude apoya en ambas fases pero no las lidera.
3. **Encuadre comercial:** Pro bono — favor a Cora. Aplicamos **versión ligera** del PKA: análisis sólido + Vivienne para el deck, sin desplegar Aurelio AU-1 completo ni Bruna BR formal. Una sola revisión interna antes de entregar a Cora.
4. **Siguiente paso operativo:** Crear draft Gmail a Cora con HTML brief adjunto. Esperar respuestas para cerrar plan v2 con scope final.

Estas decisiones invalidan o ajustan algunas secciones del cuerpo del plan (las dejo abajo como propuesta original pero deben leerse a la luz de estas decisiones).

---

## 1. Encaje en el sistema /RAUL/

### 1.1 Dominio propuesto

**Nuevo dominio:** `03-projects/consultoria-externa/`
**Proyecto:** `gama-notoriedad-2026/`

Justificación:
- No es trabajo Genteca (separar contablemente y operativamente).
- No es `marca-personal-raoul/` (consultoría para tercero ≠ marca personal).
- `research-generic/` no encaja (eso es research sin cliente).
- Abrir `consultoria-externa/` deja estructura limpia para futuros clientes (tuyos o de Cora).

### 1.2 Encaje con PKA / Capa CSC

Esta cadena es un patrón **research → deck**, similar a lo que ya validamos en sesiones GME y SAPI. Mapeo tentativo de agentes:

| Capa | Agente | Rol en este proyecto |
|---|---|---|
| 1. Estrategia | Aurelio (AU-1) | Brief + objetivo de presentación + audiencia + métricas de éxito |
| 2. Insumos | — | Cora trae la data ya tabulada (no requiere Vera/Orlan/Paxs en este caso) |
| 3. Análisis | Claude directo (o nuevo rol "consultor analítico" si se repite) | MECE de hallazgos, cruces, narrativa |
| 4. Mensaje | Vael (VA-1 análogo) | Arquitectura de mensaje del deck (pilares Minto) |
| 5. Riesgo | Bruna (BR-1 análogo) | Caveats sobre comparabilidad 2025↔2026 (n distinto, geografía distinta) |
| 6. Producción | **Vivienne (VI-1)** | Outline Markdown SSOT → PPTX editable |
| 7. Distribución | Manual (entregamos a Cora) | No requiere Ivo |

**Gap detectado:** no tenemos agente con expertise específica en investigación de mercado / análisis estadístico de notoriedad. Tres opciones:
- (a) Yo (Claude) tomo ese rol esta vez. Validar si el patrón se repite antes de invertir en agente nuevo.
- (b) Contratar agente "Analista de Estudios de Mercado" vía Michelina si esto va a ser recurrente.
- (c) Cora hace el análisis y nosotros solo el deck. Más limpio si su rol es ese.

→ **Decisión pendiente del Owner: ¿quién hace el análisis?** Ver Sección 5.

---

## 2. Hallazgos del review inicial

### 2.1 Lo que hay en 2026 (`Notoriedad para IA 2026.xlsx`)
- 1 hoja "Para IA (2)", 1050 filas × 25 columnas.
- N=402.
- Breakdown: Total, Género (M/F), Edad (4 bandas 25-64), NSE (C+/C/D/E).
- **No hay breakdown geográfico.**
- ~10 atributos de marca (P22 importancia / P23 asociación).
- 15 categorías para precio (P32 — mejor precio).
- **2 preguntas nuevas exclusivas 2026 sobre Gama:** P33 (precios bajos/medios/altos) y P34 (evolución últimos 6 meses).

### 2.2 Lo que hay en 2025 (`Tablas Notoriedad DEMO VF 2025.xlsx`)
- 7 hojas (% VERT, ABS, SIG, SIG2, VERT, Hoja1, Hoja2).
- N=785.
- Breakdown: Total, Género, Edad, NSE (C+/C/D/E), **Geografía (18+ zonas Caracas)**.
- 20 atributos de marca (P22/P23) — superset del 2026.
- 20 categorías P28 (precio/calidad/variedad) — superset del 2026.
- Preguntas exclusivas 2025: P36-P43 (delivery, área gourmet, secciones especializadas, comportamiento por categoría).

### 2.3 Marcas medidas (universo competitivo)
Plaza's, Central Madeirense, Forum, Río, Páramo, Plan Suárez, Luz, La Muralla, Híper Líder, **Gama** (foco del estudio).

### 2.4 Caveats estructurales (críticos)

⚠ **Comparabilidad 2025↔2026 limitada por 3 razones:**

1. **Tamaño muestral muy distinto** (785 vs 402) → significancia estadística asimétrica; un 5pp de diferencia 2025↔2026 puede no ser significativo.
2. **Cobertura geográfica distinta** (2025 con 18+ zonas Caracas; 2026 sin geografía visible) → si 2026 se hizo en una sub-geografía, no es comparable a 2025-total sino a 2025 filtrado por esa zona.
3. **Cuestionario reducido en 2026** (10 atributos vs 20; 15 categorías vs 20; sin delivery/área gourmet) → solo el subset común se puede comparar 1:1.

→ **Plan de mitigación:** Bruna (o yo en su lugar) integra caveat literal en cada slide comparativa: "Comparación limitada a preguntas/atributos comunes en ambas olas. n2025=785 vs n2026=402; precaución al interpretar diferencias menores a X pp."

---

## 3. Plan de trabajo en 5 fases

### Fase 0 — Setup [día 0, ya hecho parcialmente]
- [x] Carpeta `03-projects/consultoria-externa/gama-notoriedad-2026/` creada.
- [x] Inventario de fuentes.
- [ ] Confirmación Owner sobre dominio definitivo.
- [ ] Respuestas Cora a preguntas (brief HTML).
- [ ] Decisión Owner sobre división de trabajo (quién hace análisis vs deck).
- [ ] Confirmar confidencialidad / NDA.

### Fase 1 — Alineación de scope [día 1-2]
- Cerrar brief Aurelio (AU-1 análogo) con base en respuestas Cora.
- Mapa de preguntas comparables 2025↔2026 (tabla matricial: qué pregunta del 2026 mapea a qué del 2025, % de match, caveats).
- Definir 5-7 atributos "relevantes para la marca" (eje de matriz de posicionamiento) — input clave de Cora/Gama, NO inventarlo.
- Definir audiencia y formato final del deck (Junta? Mercadeo? CEO? PPT genérico?).
- Definir si C+/C combinado es el lente principal o secundario.

### Fase 2 — Análisis (MECE) [día 3-6]

**Pilares MECE propuestos** (sujetos a ajuste con respuestas de Cora):

**Pilar A — Salud de marca (Brand health)**
- A1. Embudo de marca completo: Awareness TOM → Awareness espontáneo total → Awareness asistido → Consideración → Trial últimos 3 meses → Preferida (P16, P17, P19, P20, P21).
- A2. Embudo Gama vs competencia (Plaza, Central Madeirense, Páramo principalmente — los 3 que típicamente lideran TOM).
- A3. Conversión entre etapas (qué % cae entre awareness y consideración, consideración y trial, etc.) — diagnóstico de dónde se pierde la marca.
- A4. Comparativo 2025 vs 2026: ¿gana, mantiene o pierde tracción en cada etapa?

**Pilar B — Posicionamiento (Matriz)**
- B1. Importancia de atributos (P22) — promedios de los 10 atributos en 2026.
- B2. Asociación de atributos por marca (P23) — share of voice por atributo para Gama vs competencia.
- B3. **Matriz Importancia (eje X) × Asociación Gama (eje Y)** — los 4 cuadrantes:
  - Alta-Alta = fortalezas a defender
  - Alta-Baja = brechas críticas (oportunidad)
  - Baja-Alta = sobre-inversión (desperdicio)
  - Baja-Baja = irrelevantes
- B4. Comparativo 2025 vs 2026: ¿en qué atributos Gama ha mejorado / empeorado?

**Pilar C — Precio (DEEP DIVE — foco del estudio)**
- C1. Ranking de cadenas por precio percibido global (P31 — orden 1 a 10).
- C2. Mejor precio por categoría — 15 categorías (P32) — heatmap Gama vs competencia.
- C3. Percepción de nivel de precio de Gama (P33 — bajos/medios/altos) — total y por segmento.
- C4. Percepción de evolución de precios Gama últimos 6 meses (P34) — total y por segmento.
- C5. Comparativo 2025 vs 2026 donde aplique (P28 tiene precio pero estructura distinta — requiere mapping cuidadoso).

**Pilar D — Comportamiento de compra**
- D1. Última compra (P24) — share de Gama vs competencia.
- D2. Razón de última compra (P25) — qué impulsó la elección.
- D3. Misiones de compra (P26) — qué cadena gana cada misión.
- D4. Lugar habitual por categoría (P30) — donde lidera Gama y donde no.

**Pilar E — Segmentación: C+/C combinado vs Total**
- E1. Para cada hallazgo de A/B/C/D: ¿C+/C ve algo distinto al Total?
- E2. Diferencias accionables — solo se reportan donde hay diferencia material (no llenar el deck de cruces que dicen lo mismo).

### Fase 3 — Arquitectura de mensaje (Minto) [día 6-7]

**Estructura piramidal:**

**Top — 1 tesis principal** (a redactar tras Fase 2):
> "Gama [diagnóstico salud de marca] y [diagnóstico precio]; recomendamos [3 movimientos]."

**Nivel 2 — 3-4 argumentos sustentando la tesis** (uno por pilar prioritario, ordenados por relevancia para la decisión).

**Nivel 3 — Evidencia: datos editables + visualizaciones**.

### Fase 4 — Producción del deck (Vivienne) [día 7-9]
- Outline Markdown SSOT en `03-deck/VI-1_gama-notoriedad-2026_outline.md`.
- Estructura: Portada / Resumen ejecutivo (1 slide la tesis) / Metodología y caveats / Pilar A / Pilar B / Pilar C / Pilar D / Recomendaciones / Anexos.
- Charts editables: nativos PowerPoint (no imágenes pegadas). Datos como tablas Excel-link.
- Revisión interna con Owner antes de mandar a Cora.

### Fase 5 — Entrega y ciclo de feedback [día 10-12]
- Envío a Cora con cover note.
- 1-2 rondas de feedback estimadas.
- Cierre + archivado.

**Esfuerzo total estimado:** 10-12 días calendario asumiendo ~3 h/día. Sujeto a depender de cuán rápido responda Cora preguntas críticas (especialmente: quién hace el análisis y qué atributos son "relevantes").

---

## 4. Riesgos identificados

| ID | Riesgo | Mitigación |
|---|---|---|
| R1 | Comparabilidad 2025↔2026 limitada (n y geografía distintos) | Caveat literal en todas las comparativas. Filtrar 2025 a sub-geografía si 2026 tiene una geografía oculta. |
| R2 | Confidencialidad de datos de tercero | NO commitear Excel ni outputs crudos. Confirmar NDA con Cora. |
| R3 | Scope creep (Cora puede agregar pedidos en el camino) | Cerrar brief AU-1 antes de empezar Fase 2. Pedidos nuevos generan v2. |
| R4 | "Atributos relevantes" no definidos por nosotros | Pedir input explícito a Cora — son input, no output. |
| R5 | Confusión sobre quién hace análisis vs quién hace deck | Cerrar antes de empezar (preguntas a Cora + Owner). |
| R6 | Charts no realmente editables si no se cuida la producción | Vivienne entrega nativos PPT con data en tabla; verificar al final. |
| R7 | Pirámide de Minto requiere una tesis fuerte; si los datos no la sustentan tendremos que matizar | Aceptarlo desde el principio — Minto sin tesis clara es solo una lista jerarquizada. |

---

## 5. Decisiones pendientes (lista corta)

### Owner (Raoul)
1. ¿Dominio final: `consultoria-externa/` (recomendado) o `marca-personal-raoul/clients/`?
2. ¿Quién hace el análisis: Cora, tú, yo, o reparto?
3. ¿Es paga esta consultoría? ¿Hay deadline duro?
4. ¿Quieres que yo proponga un agente nuevo "Analista de Mercado" vía Michelina si esto se va a repetir?
5. ¿Permiso para usar PKA framework completo (Aurelio + Vivienne) o lo manejamos ligero esta primera vez?
6. ¿Aplicar tono Owner-style en el correo a Cora? (recomendado dado que es colaboradora conocida [[reference_genteca_contacts]])

### Cora
Ver brief HTML separado: `2026-05-13_brief-questions-cora_v1.html`.

---

## 6. Outputs comprometidos en esta fase 0

- [x] `README.md` del proyecto.
- [x] Este plan de acción (v1).
- [x] Brief HTML para Cora (`2026-05-13_brief-questions-cora_v1.html`).
- [x] Draft de correo a Cora (`99-comms/2026-05-13_draft-email-cora_v1.md`).
- [ ] Pendiente respuesta Owner + Cora → plan v2 con scope cerrado.
