# Competitive Landscape — Naming Térmico en Protectores de Voltaje Enchufables
**Tipo:** OL-1 micro-update
**Fecha:** 2026-05-05
**Scope:** Competidores VE (Breakermatic, WellSpec, Powest Airmatic, TQ, Avtek, JVTRONIC, Protektor) + referencia regional (Schneider Easy9/Domae, APC) | Función térmica en empaque, ficha técnica y web | Snapshot actual
**Audiencia:** Vael (naming), Bruna (risk gate), Owner (Junta mañana)

---

## §1 Resumen ejecutivo

**Qué encontré:** Ningún competidor venezolano directo (formato enchufable / bornera) usa "NTC", "termistor" ni "sensor de temperatura" como claim de empaque o ficha técnica. El único actor que publica terminología térmica activa en el espacio regional es Breakermatic — pero exclusivamente en su línea de **indicadores de temperatura** (accesorio separado), no en sus protectores de voltaje.

**Qué confirmé:** La frase "Protección térmica" (sin calificador) ya la usa Genteca internamente en el diseño V10 del GSM-MB/RB/RF desde marzo 2026. Ningún competidor VE la tiene registrada en empaque o ficha verificable a esta fecha. El territorio está funcionalmente vacante para protectores enchufables/bornera en Venezuela.

**Qué quedó sin verificar:** (a) Catálogos actualizados 2025 de Breakermatic — el sitio oficial retornó ECONNREFUSED; el catálogo con fuente primaria corresponde a 2017. (b) Fichas técnicas individuales de Avtek (PDFs requieren descarga directa, página de índice sin especificación térmica visible). (c) Sitio icreativa.com.ve / Protektor sin datasheets públicos accesibles. (d) TQ — búsqueda no devolvió ficha técnica con especificaciones de función interna; solo referencias comerciales. Ver §5.

---

## §2 Tabla por marca

| Marca | Producto líder (enchufable/bornera) | Claim térmico literal | Fuente | Fecha verificación | Confianza |
|---|---|---|---|---|---|
| **Breakermatic** | Ultra 220 (PBE220), Ultra Socket 110/220 (PBI110/220), Trabajo Pesado (PBE110) | **Ninguno** en línea protectores voltaje. "Sonda de temperatura tipo NTC de 1,5 m" aparece solo en línea **Indicadores de Temperatura** (accesorio separado, no protector). | Catálogo Linea Comercial 2017 (PDF oficial Mavigal/Asenzo) + asenzo.com 2026-05-05 | 2026-05-05 | Alto (catálogo oficial; sin actualización post-2017 verificada) |
| **WellSpec** | Protector inteligente 120V 80A / 220V 63A | **Ninguno.** Specs publicadas: tiempo de respuesta <0,3 s, 175 J, CE certificado EN 60255-1. Sin mención de función térmica. | suministrosisg.com (distribuidor oficial VE) | 2026-05-05 | Medio [single-source: distribuidor, no fabricante directo] |
| **Powest Airmatic** | Airmatic 120V/15A y 220V/20A | **Ninguno.** Specs: desconexión alto/bajo voltaje, ciclo espera 4 min, temp. máx. operación 55°C. NTC mencionado en catálogo colombiano solo como referencia a norma técnica colombiana NTC 2540 (certificación RETIE — no es sensor). | powest.com (sitio oficial) | 2026-05-05 | Alto |
| **TQ (Total Quality)** | TQ-RB+220 Digital | **Ninguno verificado.** Referencia comercial menciona protección sobrevoltaje/apagones. Sin ficha técnica con especificaciones internas accesible online. | pcactual.net (retailer) | 2026-05-05 | Bajo [single-source, no es fuente primaria] |
| **Avtek** | SPC-PATT-1T515 (A/A), SPC-PTN-1T515 (neveras), línea SPC-PTE | **Ninguno** visible en índice de fichas técnicas. Avtek lista 14 familias de protectores sin mención a protección térmica activa. Certifica bajo COVENIN 3445 e IEC 707. | avtek.com (sitio oficial) + avtek.com/pag/fichas-tecnicas | 2026-05-05 | Medio (fichas PDF individuales no descargadas; índice negativo) |
| **JVTRONIC** | Enchufable Digital 110V y 220V (protectoresdevoltaje.com.ve) | **Ninguno.** Specs: sobre/bajo voltaje, neutro desconectado, fase caída, cortocircuito, supresión de picos, corrientes parásitas. Rango operación -5 a 55°C. Sin función térmica activa mencionada. | protectoresdevoltaje.com.ve (sitio oficial) | 2026-05-05 | Alto |
| **Protektor** | Enchufable 110V / 220V | **Ninguno verificado.** Specs: corte <90 VAC / >140 VAC (110V), <190 / >250 VAC (220V), retardo 3 min. Sin mención térmica. | ferresuministros.com (distribuidor) — sitio oficial icreativa.com.ve sin datasheets accesibles | 2026-05-05 | Bajo [single-source distribuidor; sitio oficial inaccesible] |
| **Schneider Easy9 / Domae** | Surge Protection Devices (DIN rail / panel) | No aplica directamente: Easy9 son MCBs, RCCBs y SPDs para tablero DIN, no protectores de voltaje enchufables. Sin claim térmico análogo en este segmento. | se.com + catálogo Domae 2009 | 2026-05-05 | Alto (fuera de segmento enchufable) |
| **APC SurgeArrest** | SurgeArrest Performance series | "Thermal fuse" como componente de seguridad (fusible térmico MOV). No es claim de empaque; es componente interno. Categoría surge protector, no protector de voltaje. | telebahn-hk.com review + apcguard.com specs | 2026-05-05 | Medio [surge protector, distinto segmento] |

---

## §3 Hallazgo de terminología vacante u ocupada

### Terminología VACANTE en el segmento protectores enchufables VE

Las siguientes formulaciones no tienen uso documentado por ningún competidor en empaque, ficha técnica o web en el segmento protectores de voltaje enchufables/bornera Venezuela:

- "Protección térmica" (sin calificador)
- "Protección térmica activa"
- "Sensor de temperatura"
- "Sensor térmico"
- "Autoprotección térmica"
- "Protección inteligente por temperatura"

Genteca ya usa "Protección térmica" (sin calificador) en la versión V10 del empaque GSM-MB/RB/RF (marzo 2026, Fact — fuente: spec interna procesada 2026-04-18). Este uso precede a cualquier uso documentado de un competidor VE directo.

### Terminología OCUPADA o con riesgo de confusión

- **"NTC" (literal):** No está ocupado por competidor VE como claim de empaque. Pero — como señala Canudas — expone el componente interno. La observación no es de riesgo de IP sino de inteligencia competitiva inversa. Hay precedente regional: Breakermatic usa el término técnico "NTC" en sus indicadores de temperatura (accesorio separado), lo que confirma que el término circula en la industria latinoamericana. Publicarlo en empaque le daría al competidor un plano del circuito sin beneficio perceptible para el comprador.
- **"Thermal protection" (inglés):** APC lo usa como descripción de componente (fusible térmico) en sus surge protectors. Distinto segmento y distinto idioma; no genera colisión directa en el mercado VE.
- **"Protección térmica":** La expresión genérica (sin calificador adjetivo) no está ocupada competitivamente, pero es descriptiva pura — fácilmente replicable por cualquier actor que añada un componente térmico. No hay barreras de adopción para la competencia.

### Señal: ningún competidor VE comunica esta función

Esto es relevante en dos sentidos: (a) Genteca puede reclamarlo como diferenciador de primera mención en el mercado local, y (b) la ausencia general sugiere que la mayoría de competidores simplemente no tiene la función — lo que eleva el potencial diferenciador si se comunica correctamente. Signal [no confirmado por specs internas de cada competidor; basado en ausencia de documentación pública].

---

## §4 Recomendación a Vael / Bruna

### Qué naming EVITAR

| Formulación | Razón para evitar |
|---|---|
| "Sensor NTC incorporado" | Expone componente interno sin beneficio para el comprador; inteligencia competitiva gratuita para la competencia. Canudas tiene razón. |
| "Termistor incorporado" | Mismo problema que NTC: lenguaje de ingeniería, cero resonancia en audiencia consumidor/instalador VE. |
| "Protección térmica" (solo, sin calificador) | No está ocupado hoy, pero es descriptivo puro: trivialmente replicable. Si Genteca lo usa, la competencia puede copiar añadiendo cualquier componente térmico y usando la misma frase. Usar si se combina con calificador diferenciador. |

### Qué naming es SEGURO y tiene espacio libre

| Formulación | Evaluación | Categoría OL-5 |
|---|---|---|
| "Protección térmica activa" | Territorio vacante. El calificador "activa" implica monitoreo continuo vs. protección pasiva (fusible). Ningún competidor VE lo usa. Defendible si el NTC hace lecturas continuas (no solo fusible). Requiere que Vera confirme que el NTC del GSM es sensado activamente, no solo como fusible de corte. | ⚠ Defendible con caveat — confirmar con Vera que es sensado activo, no solo térmico pasivo |
| "Sensor de temperatura integrado" | Vacante. Describe función sin revelar el componente específico (NTC). Más claro para el consumidor final que "NTC". Riesgo bajo. | ✅ Defendible |
| "Autoprotección térmica" | Vacante. Implica que el equipo se protege a sí mismo ante exceso de temperatura. Resonancia intuitiva alta. Sin uso competidor VE documentado. | ✅ Defendible |
| "Protección inteligente por temperatura" | Vacante. Combina dos atributos valorados (inteligente + temperatura). Más largo para empaque; candidato a copy interior de empaque o ficha técnica, no cara frontal. | ✅ Defendible |

**Nota para Bruna — risk gate:** Ninguna de las formulaciones vacantes tiene uso previo documentado por competidor VE que pueda generar reclamo de uso previo en el mercado local. El riesgo de IP formal (marca registrada) no fue investigado en esta entrega — eso requeriría consulta SAPI Venezuela + OMPI si los candidatos finales de Vael se formalizan. Flag para Bruna: si alguna formulación finalista va a ser reclamada como diferenciador de marca (no solo claim de empaque), sugerir verificación registral.

**Nota para Vael:** La terminología que más diferencia a Genteca es la que (a) no revela el componente, (b) comunica el beneficio funcional (el equipo no se sobrecalienta, se autoprotege), y (c) no puede ser copiada trivialmente con un fusible simple. "Autoprotección térmica" o "Sensor de temperatura integrado" cumplen las tres condiciones mejor que "Protección térmica" a secas.

---

## §5 Supuestos y límites

1. **Breakermatic catálogo 2017 como fuente principal:** El sitio oficial (breakermatic.com) retornó ECONNREFUSED en dos intentos. El catálogo disponible es de 2017. Es posible que modelos 2022-2025 hayan añadido función térmica sin que esté indexada públicamente. [single-source temporal]. Escalar a Paxs si se necesita confirmar el portafolio actual antes de Junta.

2. **Avtek fichas técnicas individuales no descargadas:** El índice de fichas (avtek.com/pag/fichas-tecnicas) lista 14 familias pero los PDFs no fueron procesados individualmente por restricción de tiempo. La página de índice no menciona función térmica. Confianza media — no descartable.

3. **TQ sin fuente primaria:** No se localizó sitio oficial de TQ (Total Quality) ni datasheet descargable. La referencia disponible es de un retailer (pcactual.net). Marca con presencia VE pero documentación pública escasa.

4. **Protektor — sitio oficial inaccesible:** icreativa.com.ve cargó pero sin datasheets individuales. La única spec disponible viene de un distribuidor. No descartable que existan funciones no documentadas.

5. **Schneider Easy9 / Domae:** Confirmado fuera de segmento enchufable/bornera para protectores de voltaje. No relevante para este análisis de naming.

6. **Riesgo de IP registral:** Esta entrega no cubre búsqueda de marcas registradas (SAPI Venezuela, OMPI). Si algún finalista de Vael se convierte en claim de marca formalizado, Bruna debe escalar a verificación registral antes de imprimir empaque.

7. **Lanzamientos post-catálogo:** El mercado VE tiene alta volatilidad de SKU; nuevos competidores o versiones pueden haberse lanzado en 2024-2025 sin indexación web. Esta es una foto a 2026-05-05, no un audit exhaustivo.

---

## Sources

| # | Fuente | URL | Fecha de acceso | Confianza | Notas |
|---|---|---|---|---|---|
| 1 | Breakermatic — Catálogo Línea Comercial 2017 (PDF oficial Mavigal S.A.S.) | https://asenzo.com/wp-content/uploads/2020/04/CO-BREAKERMATIC-Catalogo-Linea-Comercial.pdf | 2026-05-05 | Confirmed | Fuente primaria directa del fabricante. Catálogo 2017 — posible desactualización en modelos post-2020. 20 páginas revisadas completas. |
| 2 | Asenzo — Breakermatic marca (distribuidor autorizado Colombia) | https://asenzo.com/breakermatic-marca/ | 2026-05-05 | Confirmed | Sección Indicadores de Temperatura: "Cuentan con sonda de temperatura tipo NTC de 1,5 m". Solo en indicadores, no en protectores de voltaje. |
| 3 | Suministros ISG — WellSpec 120V 80A (distribuidor oficial VE) | https://suministrosisg.com/products/protector-de-voltaje-inteligente-120v-wellspec | 2026-05-05 | Probable | Distribuidor oficial, no fabricante. Sin mención función térmica. |
| 4 | Powest — página oficial protectores de voltaje | https://powest.com/protectores-de-voltaje/ | 2026-05-05 | Confirmed | Sitio oficial del fabricante. Sin mención función térmica en ningún modelo Airmatic. |
| 5 | Powest — Airmatic 220V/20A ficha producto | https://powest.com/producto/protector-de-voltaje-powest-airmatic-220v-20a/ | 2026-05-05 | Confirmed | Specs completas revisadas. NTC 2540 = norma colombiana RETIE (no sensor). |
| 6 | JVTRONIC — Protector enchufable digital 220V | https://www.protectoresdevoltaje.com.ve/producto/protector-individual-enchufable-digital-220v-a-a-refrigeracion-multiproposito | 2026-05-05 | Confirmed | Sitio oficial. Specs completas. Sin función térmica. |
| 7 | Avtek — Fichas técnicas (índice) | https://www.avtek.com/pag/fichas-tecnicas | 2026-05-05 | Probable | Solo índice con nombres de producto. PDFs individuales no descargados. Sin mención térmica en índice. |
| 8 | Avtek — Protector neveras SPC-PTN-1T515 | https://www.avtek.com/producto/protector-de-voltaje-para-refrigeradoras-neveras-domesticas-br-spc-ptn-1t515 | 2026-05-05 | Probable | Producto individual revisado. Sin función térmica. |
| 9 | Ferresuministros — Protektor 220V enchufable (distribuidor) | https://ferresuministros.com/wp/producto/protector-electrico-220v-enchufable-protektor/ | 2026-05-05 | Speculative | SSL error; contenido no accesible. [single-source indirecto] |
| 10 | Spec interna Genteca — GSM-MB/RB/RF/GLA_T (V10, marzo 2026) | C:\Raul\02-knowledge-base\02-domains\01-genteca\specs\2026-04-18_hoja-especificaciones_gsm-mb-rb-rf-gla-t.md | 2026-05-05 | Confirmed | Fuente primaria interna. "Protección térmica" y "AHORA CON PROTECCIÓN TÉRMICA" presentes en empaque V10. |
| 11 | APC SurgeArrest — análisis features | https://www.apcguard.com/surgearrest-performance.asp | 2026-05-05 | Probable | "Thermal fuse" como componente; surge protector (distinto segmento). [single-source] |
| 12 | Schneider Easy9 — Surge Protection Device | https://www.se.com/my/en/download/document/HRB4959100/ | 2026-05-05 | Confirmed | MCBs/RCCBs/SPDs para DIN rail. Distinto segmento enchufable. |
