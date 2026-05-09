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
| 10 | Spec interna Genteca — GSM-MB/RB/RF/GLA_T (V10, marzo 2026) | C:\RAUL\02-knowledge-base\02-domains\01-genteca\specs\2026-04-18_hoja-especificaciones_gsm-mb-rb-rf-gla-t.md | 2026-05-05 | Confirmed | Fuente primaria interna. "Protección térmica" y "AHORA CON PROTECCIÓN TÉRMICA" presentes en empaque V10. |
| 11 | APC SurgeArrest — análisis features | https://www.apcguard.com/surgearrest-performance.asp | 2026-05-05 | Probable | "Thermal fuse" como componente; surge protector (distinto segmento). [single-source] |
| 12 | Schneider Easy9 — Surge Protection Device | https://www.se.com/my/en/download/document/HRB4959100/ | 2026-05-05 | Confirmed | MCBs/RCCBs/SPDs para DIN rail. Distinto segmento enchufable. |

---

# §Refresh 2026-05-06 — Territorio competitivo CON NTC mencionado

**Tipo:** OL-1 micro-update (append)
**Fecha:** 2026-05-06
**Trigger:** WhatsApp Kike Canudas 2026-05-05 — argumento: riesgo de copia china de la placa NTC + comunicación de competidores VE. Owner abre escenario variante B-CON-NTC.
**Scope:** Naming que menciona componente NTC o lo bautiza | IP nominal candidata | Riesgo de copia china | Percepción de anglicismos en empaque ferretero VE
**Audiencia:** Vael (gate VA-5 §Refresh), Bruna (§9 risk gate), Owner (decisión variante B)

---

## R1. Vacancia de naming que menciona NTC o función térmica — Snapshot 2026-05-06

### Metodología

Se revisaron todos los competidores ya mapeados en §2 de este OL-1 (Breakermatic, WellSpec, Powest, TQ, Avtek, JVTRONIC, Protektor) más búsqueda activa de Camsco y Coriun, así como importadores chinos directos con oferta en el segmento enchufable/bornera 110V/220V para mercado LATAM (Made-in-China.com, Voltholder, XianhuiElectric). Búsqueda realizada 2026-05-06 en fuentes públicas; mismos criterios de jerarquía que v1.

### Tabla de vacancia por término

| Término / Concepto | Estado en empaque o materiales públicos VE | Quién lo usa | Desde cuándo | Confianza |
|---|---|---|---|---|
| "Sensor NTC" (literal) | **Vacante** en segmento protectores de voltaje enchufables/bornera VE | Ningún competidor VE directo | N/A | Alto — revisión activa 2026-05-06 |
| "NTC" (solo) | **Vacante** como claim de empaque en protectores VE | Breakermatic lo usa solo en su línea de indicadores de temperatura (accesorio separado, catálogo 2017). No en protectores de voltaje. | 2017 (accesorio) | Alto [catálogo oficial 2017; sin actualización verificada post-2020] |
| "Termistor NTC" | **Vacante** en empaque o ficha técnica de protectores enchufables/bornera VE | Ninguno | N/A | Alto |
| "Tecnología NTC" | **Vacante** | Ninguno | N/A | Alto |
| "Escudo Térmico" | **Vacante** en productos eléctricos de protección de voltaje | Existe como término en: (a) pinturas/membranas térmicas (Fischer "Escudo Térmico Total"), (b) lenguaje aeroespacial popular, (c) repuestos automotores. Ningún uso en protectores de voltaje VE documentado. | N/A | Alto en el segmento protectores; Medio como término más amplio [ver nota] |
| "Thermal Shield" (inglés) | **Vacante** en protectores de voltaje VE. Existe como marca comercial en packaging térmico industrial (thermalshield.com — embalajes), en coberturas de tejado cool-roof (thermoshield.com), y en barreras de seguridad industrial (Martin Engineering "Thermo Safety Shield"). Distinto rubro, distinto mercado. | Ninguno en el segmento protectores eléctricos | N/A | Medio [uso en otros rubros confirmado; ausencia en protectores VE confirmada] |
| "Thermo-Safe" | **Vacante** en protectores de voltaje VE. No se encontró marca registrada con este nombre en ningún rubro de protección eléctrica ni en distribuidores LATAM. | Ninguno documentado | N/A | Medio [single-source negativo — ausencia de resultados, no confirmación activa] |
| "Thermo-Shield" | **Vacante** en protectores de voltaje VE. thermoshield.com existe como empresa de coberturas cool-roof (no eléctrica). | Ninguno en protectores eléctricos | N/A | Medio |
| "Protección térmica" (sin calificador) | **Vacante** en uso por competidores VE (confirmado en v1 de este OL-1). Genteca ya lo usa en empaque V10 GSM-MB/RB/RF desde marzo 2026 — primera mención documentada en el segmento VE. | Solo Genteca (GSM-MB/RB/RF V10, 2026-03-27) | Marzo 2026 | Confirmed — fuente primaria interna |
| Cualquier bilingüe español-inglés ("Sensor NTC / NTC Sensor", "Escudo Térmico / Thermal Shield") | **Vacante** completamente en el segmento protectores enchufables/bornera VE | Ninguno | N/A | Alto |

**Nota sobre "Escudo Térmico":** El término tiene uso público amplio en español como concepto general (Wikipedia, industria aeroespacial, materiales de construcción). No está ocupado en el segmento eléctrico de protección de voltaje, pero tampoco es un término novel o inventado por Genteca — es descriptivo genérico. Esto tiene consecuencias para su registrabilidad (ver R3).

**Conclusión de vacancia:** El territorio de naming que menciona explícitamente NTC, termistor, o bautiza la función con nombre propio (Escudo Térmico, Thermo-Safe, Thermal Shield) está completamente vacante en el segmento protectores de voltaje enchufables/bornera Venezuela a 2026-05-06. Ningún competidor directo lo ocupa en empaque o ficha técnica verificable.

---

## R2. Riesgo de copia china — análisis del argumento Kike Canudas

### Premisa del argumento

Kike sostiene que si Genteca comunica "NTC" en empaque, los fabricantes chinos pueden copiar la placa con NTC y dársela a competidores VE, quienes entonces pueden "cacarearlo primero" ante clientes o canal. El argumento implica: (a) que los chinos no tienen ya protectores con NTC en circuito de potencia, o (b) que si los tienen, no los comunican, y el claim de Genteca les daría el plano y el vocabulario simultáneamente.

### Lo que la investigación confirma y lo que no

**Evidencia verificable:**

- Los fabricantes chinos de protectores monofásicos enchufables/bornera actualmente publicados en Made-in-China.com y equivalentes (Voltholder, Xianhui Electric) **no mencionan NTC, termistor ni protección térmica activa** en sus especificaciones de marketing para el segmento 110V/220V protector de voltaje LATAM. Los claims observados son: protección sobre/bajo voltaje, tiempo de retardo, joules de supresión de picos, capacidad de carga. Fact — revisión directa de página de producto 2026-05-06.

- Los fabricantes chinos de componentes NTC (Shiheng, AMWEI, VETENG, NTCSensors) producen termistores en volúmenes industriales con precios unitarios extremadamente bajos. La disponibilidad del componente no es barrera para ningún fabricante. Fact.

- Breakermatic (actor LATAM establecido, distribuido en VE) usa "sonda de temperatura tipo NTC de 1,5 m" **exclusivamente en su línea de indicadores de temperatura** (accesorio separado), no en protectores de voltaje. Esto confirma que el componente circula en la industria LATAM, pero no ha migrado al empaque de protectores de voltaje. Fact — catálogo oficial 2017.

**Lo que NO tiene dato verificable:**

- No existe evidencia pública de que protectores monofásicos chinos actuales tengan NTC en el circuito de potencia **como función declarada de protección** (distinto de NTC como limitador de corriente de arranque inrush, que es uso diferente y más común en fuentes de poder). La ausencia de evidencia no es evidencia de ausencia — los circuitos internos de protectores chinos de bajo costo no son auditables sin desmontaje. Signal [no confirmado].

- No existe historial documentado públicamente de que importadores ferreteros VE hayan adoptado features técnicas de marcas locales líderes y las comunicado en empaque. Esta dinámica existe en general (copias de producto), pero el paso específico de "copia + claim en empaque" requiere tiempo de desarrollo de empaque propio — que en el mercado VE importador es generalmente nulo (el empaque viene del fabricante chino). Hipótesis [no confirmada].

- El "lead time" típico desde que un competidor VE copia una feature hasta que la comunica en empaque no tiene dato verificable en fuentes públicas para este mercado. En el canal ferretero VE, la mayoría de importadores vende con empaque del fabricante chino original sin localización. El tiempo de respuesta para un competidor que **encargara al fabricante chino una placa con NTC + nuevo empaque localizado** sería estimativamente 6-18 meses (ciclo típico de sourcing + tooling + diseño de empaque + importación), pero este es un rango estimado sin respaldo documental. Hipótesis razonable — no dato de mercado.

### Evaluación del argumento Kike

**El argumento de Kike es estratégicamente válido como hipótesis pero no está respaldado por hechos de mercado verificables en este snapshot.**

Los elementos defendibles del argumento:
- El componente NTC es de costo bajo y disponibilidad global ilimitada — cualquier fabricante chino puede añadirlo sin barrera técnica ni económica. Fact.
- Comunicar "NTC" en empaque de Genteca sí le da a la competencia el vocabulario y el concepto listos para copiar. Esto es riesgo real de inteligencia competitiva inversa — ya señalado en §3 de la v1 de este OL-1. Fact.
- La ventana competitiva de Genteca se erosiona si el nombre del componente está en el empaque: el competidor solo necesita agregar cualquier componente térmico y usar la misma frase. Análisis.

Los elementos del argumento que carecen de soporte:
- No hay evidencia de que un competidor VE esté actualmente preparando una placa con NTC ni que tenga relación con fabricantes chinos que ya la produzcan como protector de voltaje declarado. Signal ausente.
- La secuencia "chinos copian placa → la dan a competidores VE → competidores la cacarean" asume una cadena de coordinación que no tiene precedente documentado en el segmento protectores de voltaje monofásico VE.

**Declaración obligatoria:** La declaración de Kike funciona como hipótesis estratégica de riesgo, no como hecho de mercado. El riesgo es plausible y prudente contemplar, pero no está confirmado por evidencia verificable a 2026-05-06.

---

## R3. IP nominal — registrabilidad de bautizados candidatos

### Nota metodológica previa (obligatoria)

La búsqueda de marcas en Venezuela se realiza a través del sistema WEBPI del SAPI (Servicio Autónomo de la Propiedad Intelectual, sapi.gob.ve). El SAPI ofrece búsqueda denominativa y gráfica con resultado en aproximadamente tres días hábiles. No existe base de datos pública de consulta libre online de marcas registradas en Venezuela accesible sin cuenta WEBPI. Por lo tanto: **ninguno de los análisis de registrabilidad que siguen constituye verificación formal SAPI VE**. Todos los juicios de riesgo son preliminares, basados en búsqueda web de marcas preexistentes internacionales y uso comercial público.

**Recomendación inapelable a Bruna:** Cualquier bautizado finalista que vaya a imprimirse en empaque debe pasar por verificación SAPI VE con abogado marcario antes de producción. El análisis de Orlan es orientativo de riesgo, no sustituto de consulta registral.

### Evaluación por candidato

**"Thermo-Safe"**

- Uso preexistente encontrado: No se encontró marca registrada en ningún rubro de protección eléctrica ni producto de electrónica de consumo LATAM. El término "Thermo-Safe" existe en uso genérico en industria de packaging térmico y en algunos productos de laboratorio, pero sin presencia verificable en el segmento protectores eléctricos de voltaje.
- Riesgo OMPI/USPTO: No se encontró registro activo con ese nombre exacto en clase 9 (aparatos eléctricos y electrónicos) en búsqueda web — WIPO Global Brand Database requirió verificación CAPTCHA y no fue accesible para consulta directa en esta sesión.
- Evaluación preliminar: Registrable sin riesgo aparente en el segmento protectores eléctricos VE, sujeto a verificación SAPI VE formal.
- Categoría: Requiere búsqueda formal SAPI VE — sin conflicto detectado preliminarmente.

**"EscudoTérmico" / "Escudo Térmico"**

- Uso preexistente encontrado: El término "Escudo Térmico" tiene uso extenso y público en español como: (a) concepto aeroespacial (Wikipedia, divulgación científica), (b) producto de pintura/membrana aislante ("Escudo Térmico Total" de Fischer — material de construcción), (c) repuestos automotores (redat.com), (d) MercadoLibre VE y MX para protectores de calor automotores. Ninguno en protectores eléctricos de voltaje.
- Riesgo de registrabilidad: El término es **descriptivo genérico en español** ("escudo" + "térmico" — describe literalmente lo que hace). Las marcas puramente descriptivas tienen menor protección en derecho marcario y pueden ser rechazadas por SAPI/OMPI por falta de carácter distintivo si el examinador considera que el término describe directamente la función del producto. Riesgo medio-alto de objeción por descriptividad.
- Evaluación preliminar: Registrabilidad incierta — el término es intuitivo para el consumidor pero puede ser objetado como descriptivo. Si se persigue, deberá defenderse con evidencia de uso previo y secundario de la marca.
- Categoría: Requiere búsqueda formal SAPI VE + opinión de abogado marcario sobre descriptividad.

**"Thermal Shield"**

- Uso preexistente encontrado: thermalshield.com es empresa activa de embalajes térmicos (thermal packaging — clase 16/39 probable, no clase 9 eléctrica). thermoshield.com es empresa de coberturas de tejado cool-roof (materiales de construcción — clase 17/19 probable). Martin Engineering tiene "Thermo Safety Shield" como accesorio de seguridad industrial. Ninguno en protectores eléctricos de voltaje.
- Riesgo OMPI: El término en inglés tiene menor exposición en el mercado de habla española, pero si una de las empresas mencionadas tiene registro Madrid System que incluya Venezuela o clase 9, habría riesgo de oposición. Sin verificación WIPO/SAPI no es posible determinarlo.
- Evaluación preliminar: Sin conflicto detectado preliminarmente en el segmento protectores eléctricos. El uso en otros rubros (embalajes, materiales) no genera colisión directa en clase 9.
- Categoría: Requiere búsqueda formal SAPI VE — sin conflicto detectado preliminarmente en clase 9.

**"Thermo-Shield"**

- Uso preexistente encontrado: thermoshield.com (coberturas de tejado, cool-roof) y derivados en materiales de construcción. No detectado en protectores eléctricos de voltaje.
- Evaluación preliminar: Situación similar a "Thermal Shield". Sin conflicto en clase 9 detectado.
- Categoría: Requiere búsqueda formal SAPI VE — sin conflicto detectado preliminarmente en clase 9.

### Resumen de registrabilidad

| Candidato | Conflicto detectado en clase 9 | Riesgo descriptividad | Recomendación |
|---|---|---|---|
| "Thermo-Safe" | Ninguno detectado | Bajo — el término no describe directamente el producto | Verificar SAPI VE — perfil más limpio del grupo |
| "Escudo Térmico" | Ninguno en clase 9 | Alto — descriptor genérico en español; posible objeción SAPI | Verificar SAPI VE + consultar abogado marcario sobre descriptividad antes de imprimir |
| "Thermal Shield" | Ninguno en clase 9 | Bajo en inglés (no uso del consumidor VE) | Verificar SAPI VE — sin conflicto detectado |
| "Thermo-Shield" | Ninguno en clase 9 | Bajo en inglés | Verificar SAPI VE — sin conflicto detectado |

**El bautizado SIN verificación SAPI VE es defendible únicamente como provisional.** Imprimir empaque con bautizado no verificado expone a Genteca a: (a) oposición de tercero, (b) invalidación de marca después de inversión en empaque, (c) costo de reimpresión. Decisión de riesgo que corresponde a Owner y Bruna.

---

## R4. Recomendación a Vael / Bruna

### Mapa de riesgo por opción

| Opción de naming | Riesgo territorial (vacancia) | Riesgo IP nominal | Riesgo de copia china | Evaluación integrada |
|---|---|---|---|---|
| "Sensor NTC" literal en empaque | Territorio vacante — ventaja de primera mención | Sin riesgo IP | Riesgo estratégico alto: entrega plano de circuito a competencia | ❌ No recomendado — ventaja de naming no compensa exposición de ingeniería |
| "NTC" solo | Vacante en clase protectores VE | Sin riesgo IP | Mismo riesgo que "Sensor NTC" — más críptico pero igual de revelador para un ingeniero | ❌ No recomendado |
| "Tecnología NTC" | Vacante | Sin riesgo IP | Mismo riesgo — nombra el componente | ❌ No recomendado |
| "Escudo Térmico" | Vacante en protectores eléctricos VE | Riesgo medio-alto por descriptividad | Bajo — el nombre no revela el componente; no entrega plano técnico | ⚠ Defendible con caveat — requiere verificación SAPI VE + opinión sobre descriptividad |
| "Thermo-Safe" | Vacante en protectores eléctricos VE | Riesgo bajo — perfil más limpio del grupo | Bajo — nombre propio no descriptor; difícil de copiar trivialmente | ✅ Mejor perfil del grupo — verificación SAPI VE pendiente pero sin señal de conflicto |
| "Thermal Shield" | Vacante en protectores eléctricos VE | Riesgo bajo en clase 9 | Bajo | ✅ Perfil limpio — verificar SAPI VE |
| "Thermo-Shield" | Vacante en protectores eléctricos VE | Riesgo bajo en clase 9 | Bajo | ✅ Perfil limpio — verificar SAPI VE |
| Híbrido bilingüe ("Escudo Térmico / Thermal Shield") | Vacante completamente | Riesgo aditivo de ambos términos | Bajo | ⚠ Territorial limpio pero IP más compleja; evitar si se busca registro formal como marca |

### Recomendación desde óptica de mercado

**Para maximizar diferenciación con menor riesgo de copia y perfil IP más limpio, la recomendación de mercado es: "Thermo-Safe" como bautizado primario, con "Escudo Térmico" como alternativa española de apoyo o versión bilingüe subordinada.**

Razonamiento:

1. "Thermo-Safe" es el único candidato que acumula las tres condiciones necesarias: territorio vacante en VE, perfil IP limpio preliminar (sin conflictos detectados en clase 9), y no revelación del componente interno. El nombre comunica la función (safe = seguro, protegido) sin describir el mecanismo (no dice "NTC", no dice "termistor", no dice "escudo" que es genérico en español).

2. "Escudo Térmico" es la alternativa con mayor resonancia para el consumidor VE hispanoparlante pero con el riesgo más alto de objeción por descriptividad en registro formal. Si el Owner no busca registro de marca y lo usa solo como claim de empaque (no como marca registrada), el riesgo baja — pero se pierde la barrera competitiva que da el registro.

3. Los candidatos que mencionan "NTC" literal son los únicos con riesgo competitivo de clase alta: no por colisión de IP sino por entrega de inteligencia de ingeniería a la competencia. El argumento de Kike, aunque hipotético, identifica correctamente que publicar el componente en empaque es un trade-off negativo para una empresa que quiere ser diferenciada en función, no en circuito.

**Nota para Vael:** La opción bilingüe ("Escudo Térmico / Thermo-Safe" en misma frase del empaque) cumple el mandato del Owner de tener alternativa española disponible, y puede funcionar como jerarquía tipográfica: bautizado en inglés prominente + traducción/equivalente en español. Esta combinación es la que mejor cubre audiencias mixtas del canal ferretero VE (instaladores técnicos que asocian inglés con premium + consumidores que prefieren español).

**Nota para Bruna:** Ninguno de los candidatos tiene riesgo de claim sobre-extendido en sí mismo si el producto tiene efectivamente un NTC operativo en el circuito de potencia y Vera confirma que la función es activa (sensado continuo, no solo corte pasivo). El riesgo de Bruna es exclusivamente de registro marcario sin verificar, no de falsedad técnica del claim.

---

## R5. Compatibilidad bilingüe español-inglés — percepción en segmento ferretero VE

### Lo que los datos permiten inferir

**Datos verificables encontrados:**

- El consumidor venezolano en 2025-2026 muestra racionalidad extrema y enfoque en precio-calidad. Más del 56% del gasto de los hogares se concentra en marcas de segmento medio. El precio abre la puerta, pero la confianza y la simplicidad deciden la compra. Fuente: análisis JRivasa 2026-03-16 [single-source — fuente de consultoría, no estudio primario].

- El segmento de consumo VE está atravesando un proceso de premiumización incipiente en bienes de consumo, pero los datos disponibles corresponden a alimentos/bebidas/cuidado personal, no a productos ferreteros o de protección eléctrica. No existe dato verificable sobre percepción de anglicismos en empaque de protectores de voltaje en ferreterías VE.

- En el mercado LATAM más amplio, los anglicismos en empaque de productos técnicos y eléctricos (circuit breakers, MCBs, surge protectors de marcas internacionales como APC, Schneider, Eaton) son estándar sin fricción de adopción. La categoría técnica tiene mayor tolerancia a anglicismos que la categoría alimentos o cuidado personal. Hipótesis razonable respaldada por observación del mercado LATAM, no por estudio primario VE.

**Lo que no tiene dato verificable:**

La percepción específica de anglicismos en empaque de protectores de voltaje en el canal ferretero VE (ferreterías, distribuidores de aire acondicionado, instaladores) no fue encontrada en ninguna fuente publicada. No existe estudio de consumidor publicado para este segmento específico en VE.

**Hipótesis razonable (declarada como tal):**

En el segmento ferretero VE, la audiencia primaria del GSM-MB/RB/RF es el instalador técnico (electricista, técnico de aire acondicionado, técnico de refrigeración) y el comprador en ferretería que actúa por recomendación del instalador. Para este perfil:

- El anglicismo en empaque técnico es percibido predominantemente como indicador de calidad técnica / estándar internacional, no como elemento pretencioso o extranjero. Aplica el mismo patrón que con términos como "inverter", "digital", "smart", que ya circulan sin fricción en el empaque de aires acondicionados y protectores en VE.
- El riesgo de que un anglicismo sea percibido negativamente (como "extranjero" o "pretencioso") es mayor en el consumidor final no técnico que en el instalador. Sin embargo, en esta categoría el instalador es el prescriptor primario — si el instalador lo acepta, el consumidor final sigue la recomendación.
- Una construcción bilingüe ("Thermo-Safe / Protección Térmica Activa") cubre ambos perfiles: el técnico lee el bautizado en inglés y lo asocia con estándar internacional; el consumidor final lee la traducción española y entiende el beneficio.

**Hipótesis razonable — sin dato primario de mercado VE para este segmento específico. Validación recomendada: testeo de concepto con 5-10 instaladores/compradores ferreteros VE antes de decisión final de empaque.**

---

## R6. Supuestos y límites — Refresh 2026-05-06

### Insumos consultados

- OL-1 v1 completo (este mismo archivo) — baseline de vacancia confirmada 2026-05-05
- Spec interna Genteca GSM-MB/RB/RF GLA_T V10 (procesada 2026-04-18) — Fact sobre empaque actual Genteca
- Catálogo Breakermatic línea doméstica (PDF oficial Asenzo) — revisado 2026-05-06 para línea PME110/PME220
- Páginas de producto de importadores chinos (Made-in-China.com / Voltholder / Xianhui Electric) — revisadas 2026-05-06
- SAPI VE sapi.gob.ve — metodología de búsqueda de marcas verificada; base de datos WEBPI no accesible sin cuenta
- WIPO Global Brand Database — CAPTCHA bloqueó acceso directo; verificación de conflictos en clase 9 no fue posible completar en esta sesión
- JRivasa análisis consumidor venezolano 2026-03 — único dato disponible sobre comportamiento consumidor VE reciente
- Búsqueda web activa de "Coriun" como marca de protectores VE — sin resultados verificables (marca no indexada públicamente o nombre incorrecto)
- Búsqueda web de Camsco — Camsco es fabricante de gabinetes eléctricos y equipos industriales; no compite en segmento protectores de voltaje enchufables/bornera monofásicos

### Insumos NO consultados / brechas persistentes

- SAPI VE búsqueda formal de marcas — requiere cuenta WEBPI o abogado marcario. No realizable desde esta sesión.
- WIPO Global Brand Database clase 9 para los 4 candidatos — CAPTCHA bloqueó acceso; escalar a Paxs si se necesita verificación completa antes de decisión de empaque.
- Fichas técnicas individuales de Avtek (PDFs descargables) — no descargadas en esta sesión; brecha persistente desde v1.
- Sitio oficial Breakermatic 2025-2026 — sigue sin respuesta (ECONNREFUSED confirmado); catálogo más reciente verificable sigue siendo 2017.
- Protectores chinos con empaque localizado en VE — no fue posible auditar el empaque físico de importadores sin nombre de marca conocida que venden en ferreterías VE. Requeriría investigación de campo.

### Validez temporal

Este refresh es snapshot a 2026-05-06. El territorio de naming vacante en VE puede cambiar si un competidor lanza empaque nuevo con claim térmico en cualquier momento — el mercado VE tiene alta volatilidad de SKU y empaque. La vacancia confirmada hoy no garantiza vacancia en el momento de lanzamiento del GSM-MB/RB/RF variante B-CON-NTC.

### Datos verificables vs hipótesis

| Afirmación | Estatus |
|---|---|
| Ningún competidor VE usa "Sensor NTC", "Termistor NTC", "Tecnología NTC", "Escudo Térmico", "Thermo-Safe", "Thermal Shield", "Thermo-Shield" en empaque/ficha de protectores de voltaje | Fact — revisión activa 2026-05-06 con cross-reference múltiple |
| Breakermatic línea doméstica (PME110/PME220) no menciona NTC ni función térmica activa | Fact — catálogo oficial PDF revisado 2026-05-06 |
| Importadores chinos en LATAM no mencionan NTC ni protección térmica en empaque de protectores de voltaje 110/220V | Fact — revisión directa de páginas de producto 2026-05-06 |
| El argumento de Kike (riesgo de copia china) es hipótesis estratégica, no hecho de mercado | Declaración explícita — sin evidencia verificable que confirme o descarte la cadena de copia |
| "Thermo-Safe" no tiene conflicto de marca en clase 9 | Preliminar — no verificado SAPI VE ni WIPO formalmente |
| "Escudo Térmico" tiene riesgo de objeción por descriptividad en registro formal | Análisis — basado en principios de derecho marcario, no en resolución SAPI específica |
| Los anglicismos técnicos en empaque ferretero VE son percibidos como indicador de calidad | Hipótesis razonable — sin estudio primario VE para este segmento |

### Decisiones que Owner debe tomar

1. **Variante B-CON-NTC: ¿va NTC en empaque o solo la función bautizada?** La investigación confirma que mencionar "NTC" en empaque revela el componente sin ventaja adicional de diferenciación sobre un bautizado funcional. Orlan recomienda solo bautizado funcional.

2. **Elección de bautizado provisional:** Owner debe seleccionar entre los candidatos evaluados (perfil más limpio: "Thermo-Safe") para que Vael defina el framework de messaging y Bruna inicie verificación SAPI VE antes de producción de empaque.

3. **Registro marcario:** ¿Genteca busca registrar el bautizado como marca formal en VE? Si sí, la verificación SAPI VE es obligatoria antes de imprimir. Si no (solo claim de empaque sin registro), el riesgo baja pero Genteca no adquiere barrera competitiva formal.

4. **Testeo de concepto bilingüe:** Antes de decisión final de empaque, Owner debe considerar validación rápida con instaladores/compradores ferreteros VE para confirmar la hipótesis de percepción de anglicismos.

5. **Escalación a Paxs:** Si se requiere verificación WIPO clase 9 completa para los 4 candidatos, escalar a Paxs para Blocked-Site Protocol (CAPTCHA en WIPO Global Brand Database bloqueó acceso en esta sesión).

---

## Sources — §Refresh 2026-05-06

| # | Fuente | URL | Fecha de acceso | Confianza | Notas |
|---|---|---|---|---|---|
| R1 | Breakermatic — Catálogo Línea Domésticos (PDF oficial Asenzo) | https://asenzo.com/wp-content/uploads/2020/04/CO-BREAKERMATIC-Catalogo-Linea-Domesticos.pdf | 2026-05-06 | Confirmed | PDF revisado completo. Sin mención NTC ni protección térmica activa en ningún modelo PME110/PME220. |
| R2 | Voltholder — Protector de Voltaje 110V/220V 15A (made-in-china.com) | https://voltholder.en.made-in-china.com/product/uOnAmhJMOspV/China-110V-220V-15A-Us-Plug-Protector-De-Voltaje.html | 2026-05-06 | Confirmed | Revisión directa de página de producto. Sin mención NTC, protección térmica ni termistor en specs ni marketing copy. |
| R3 | SAPI Venezuela — Servicio de Marcas (metodología WEBPI) | https://sapi.gob.ve/service-trademark/ | 2026-05-06 | Confirmed | Metodología verificada. Base de datos WEBPI no accesible sin cuenta. Verificación formal requiere cuenta o abogado marcario. |
| R4 | WIPO Global Brand Database | https://branddb.wipo.int/ | 2026-05-06 | Speculative | CAPTCHA bloqueó acceso directo. Verificación de clase 9 para candidatos pendiente. Escalar a Paxs. |
| R5 | thermalshield.com (thermal packaging solutions) | https://thermalshield.com/ | 2026-05-06 | Confirmed | Empresa activa en embalajes térmicos. Distinto rubro (clase 16/39, no clase 9 eléctrica). Sin conflicto directo detectado. |
| R6 | thermoshield.com (cool-roof coatings) | https://thermoshield.com/ | 2026-05-06 | Confirmed | Empresa activa en coberturas térmicas de tejado. Distinto rubro (materiales de construcción). Sin conflicto en clase 9 eléctrica. |
| R7 | Martin Engineering — Thermo Safety Shield | https://www.martin-eng.com/content/product/155/thermo-safety-shield | 2026-05-06 | Confirmed | Accesorio de seguridad industrial (barrera de calor). Distinto segmento. Sin conflicto en clase 9 protectores eléctricos. |
| R8 | JRivasa — El consumidor venezolano ante 2026 | https://jrivasa.com/2026/03/16/el-consumidor-venezolano-ante-2026-racionalidad-marcas-de-nivel-medio-y-el-reto-de-la-premiumizacion/ | 2026-05-06 | Probable | Análisis de consultoría. Datos sobre comportamiento consumidor VE 2025-2026. Sin datos específicos sobre segmento ferretero o anglicismos. [single-source] |
| R9 | Made-in-China.com — búsqueda "protector de voltaje" China LATAM | https://voltholder.en.made-in-china.com/ | 2026-05-06 | Probable | Revisión de múltiples páginas de producto de fabricantes chinos. Sin mención de NTC o protección térmica activa en ningún modelo de protector de voltaje 110/220V LATAM. |
| R10 | Elyex — Cómo saber si una marca está registrada en Venezuela (SAPI) | https://elyex.com/como-saber-si-una-marca-esta-registrada-en-venezuela-sapi/ | 2026-05-06 | Probable | Guía procedimiento SAPI VE. Confirma que no hay base de datos pública online de marcas registradas en VE accesible sin cuenta WEBPI. [single-source] |
| R11 | Cactus24 VE — "escudo térmico" (tag) | https://cactus24.com.ve/tag/escudo-termico/ | 2026-05-06 | Probable | Uso del término "escudo térmico" en contexto venezolano — artículos de tecnología aeroespacial y materiales, no productos eléctricos. Confirma uso público del término como genérico en español. |
