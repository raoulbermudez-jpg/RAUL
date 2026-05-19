---
doc_type: VA-5-guardrails
project_id: portfolio-naming-ip-2026
domain: genteca
version: v1.0
author: Vael
fecha: 2026-05-13
inputs:
  - Vera_VR-1_tech-inventory-hybrid_v1.md
  - Orlan_OL-1_differentiation-matrix_v1.md
  - 00-project-charter.md §3 decisión 4 (override curva inversa universal)
  - 01-checkpoint-1-resolution.md (Decisiones 1-3)
  - Vael_VA-1_messaging-architecture_v1.md (claims de referencia)
nota_clasificacion: >
  ✅ = RTB de Vera sostiene el claim sin caveat adicional.
  ⚠ = claim sostenible con matiz — el caveat literal debe acompañar el claim en cualquier uso.
  ❌ = claim no sostenido por RTB disponible o cruce de riesgo regulatorio/descriptividad.
  Gate Bruna = ítem que escala a Bruna en Phase 3 para decisión final antes de pasar a producción.
---

# VA-5 — Guardrails de Claims
## Portfolio Naming IP 2026 (Genteca)

> Claims organizados por nodo. Esta lista alimenta directamente el gate de Bruna en Phase 3. La categorización ✅ / ⚠ / ❌ es propuesta de Vael — la decisión de aprobación formal (BR-2 del proyecto) es de Bruna. Ningún claim ⚠ o ❌ pasa a Solenne, Vivienne ni producción sin gate explícito de Bruna.

---

## NODO-A — StaggerStart (Reconexión temporal aleatoria post-falla)

### Claims defendibles ✅

| Claim | RTB que lo sostiene |
|-------|---------------------|
| "Retardo de reconexión configurable de 5 a 180 segundos (GSM-MB) / 180-300 segundos (GSM-RB) / 3 minutos fijo (GSM-NG)" | HDE GSM-MB v6, HDE GSM-RB, HDE GSM-NG — valores explícitos documentados |
| "Componente aleatoria en el retardo de reconexión para evitar que dos o más equipos protegidos arranquen simultáneamente" | Documentado textualmente en HDEs GSM-MB v3-n, v4, v5, v6, v6-rv1; HDE GSM-NG |
| "Previene el pico de demanda simultáneo en instalaciones con múltiples protectores" | Consecuencia directa del mecanismo documentado — inferencia técnica sostenida |
| "Normas verificadas: IEC 61000-4-x, COVENIN 3445" | Citadas en HDEs correspondientes |

### Claims con caveat ⚠

| Claim | Caveat literal requerido |
|-------|--------------------------|
| "Tecnología de reconexión inteligente Genteca" | Caveat: la función de staggered restart existe en la competencia industrial (Eaton C445 — "Voltage Loss Restart"). El diferenciador de Genteca es la ejecución en el segmento residencial/comercial de bajo costo, no la exclusividad de la función. |
| "La única reconexión escalonada en protectores residenciales de bajo costo en VE/MX" | Caveat: requiere búsqueda de mercado confirmatoria. La competencia directa en el segmento residencial/comercial VE/MX no tiene equivalente nombrado identificado, pero no se realizó búsqueda exhaustiva en este segmento. |
| "Override curva inversa universal: StaggerStart presente en toda la gama Exceline / Exceline Profesional / Genius" | Caveat: override Owner de facto (charter §3 decisión 4) — no verificado producto por producto. Si el abogado pide confirmación individual, I+D debe auditar. [Gate Bruna: defendibilidad del override en publicidad] |

### Claims prohibidos ❌

| Claim | Razón |
|-------|-------|
| "Tecnología exclusiva Genteca de reconexión aleatoria" | Eaton C445 implementa la misma función con documentación verificada (Eaton application note ap042004en) |
| "El único protector que evita arranques simultáneos" | No se puede sostener "único" — claim de exclusividad sin base competitiva completa |

---

## NODO-B — FlickerGuard (Detección sub-ciclo de perturbaciones de voltaje)

### Claims defendibles ✅

| Claim | RTB que lo sostiene |
|-------|---------------------|
| "Detección de flicker en 20ms (GSM-L)" | HDE GSM-L v10 — dato explícito y único en la gama. Fuente primaria verificada. |
| "Detección de falla de voltaje genérica a partir de 60ms (GSM-L)" | HDE GSM-L v10 |
| "Desconexión por flicker/inestabilidad en 150ms (GSM-MB, GSM-RB, GSM-RE, GSM-NG)" | HDEs correspondientes — valores documentados |
| "Tiempo de desconexión variable según intensidad de falla de voltaje: 0,02 a 2 segundos (GSM-AV06)" | HDE GSM-AV06 — dato explícito |
| "Tiempo de desconexión variable según intensidad: 0,4 a 3 segundos (GSM-RB)" | HDE GSM-RB — dato explícito |
| "Protección contra parpadeos e inestabilidad de voltaje documentada en GSM-MB, GSM-RB, GSM-RE, GSM-L, GSM-NG" | HDEs correspondientes |
| "Normas: IEC 61000-4-4, IEC 61000-4-14, IEC 60947-1" | Citadas en HDEs |

### Claims con caveat ⚠

| Claim | Caveat literal requerido |
|-------|--------------------------|
| "La especificación de detección de flicker más agresiva en supervisores de voltaje monofásico para uso residencial/comercial en VE/MX" | Caveat: ningún competidor directo en este segmento publicó una especificación en ms equivalente en la investigación de Orlan. Sin embargo, la investigación no fue exhaustiva de todo el mercado VE/MX. La afirmación se sostiene sobre los competidores investigados. [Gate Bruna: alcance de la afirmación competitiva antes de usar en publicidad] |
| "Detección sub-ciclo documentada sin equivalente en la competencia directa" | Caveat: aplica a la gama de supervisores residenciales/comerciales de bajo costo. La competencia de gama industrial alta (ABB, Siemens power quality analyzers) tiene detección sub-ciclo pero no es la misma categoría de producto. |
| "Curva inversa V-t algorítmica (tiempo de desconexión inversamente proporcional a la desviación de voltaje)" | Caveat: este comportamiento está documentado con datos en las HDEs pero sin esa denominación formal en ningún documento Genteca. La denominación es la descripción técnica correcta del comportamiento medido. I+D debe confirmar si existe denominación interna formal. [Gate Bruna: use de la denominación en naming y claims antes de que I+D confirme] |

### Claims prohibidos ❌

| Claim | Razón |
|-------|-------|
| "El único protector que detecta flicker" | Búsqueda OMPI pendiente no permite afirmar unicidad. Otros fabricantes pueden tener productos equivalentes no identificados. |
| "Protección en tiempo real contra parpadeos" | "Tiempo real" es impreciso — el RTB correcto es la especificación en ms. El claim genérico puede crear compromisos de especificación que no se puedan sostener. |
| "Detección de flicker en 20ms en toda la gama" | El dato de 20ms es exclusivo del GSM-L. El resto de la gama tiene 150ms. Extender el claim al portafolio completo es factualmente incorrecto. |

---

## NODO-C — Thermo-Safe (Modelo térmico NTC integrado)

### Claims defendibles ✅

| Claim | RTB que lo sostiene |
|-------|---------------------|
| "Protección térmica integrada en GSM-MB, GSM-RB, GSM-RE" | Confirmada por etiqueta de empaque versión V10/V9/V13 — mención explícita "AHORA CON PROTECCIÓN TÉRMICA" |
| "Sensor NTC embebido en el protector — sin módulo adicional ni cableado externo" | Confirmado por empaque e integración documentada en HDEs |
| "Detección de temperatura real del entorno del motor (no solo corriente)" | Mecanismo documentado — NTC lee temperatura física, a diferencia del modelo I-t puro de NODO-D |
| "Desconexión por sobrecalentamiento con indicación en LED" | Documentado en HDE |

### Claims con caveat ⚠

| Claim | Caveat literal requerido |
|-------|--------------------------|
| "Parámetros específicos del sensor NTC (umbral de disparo, rango de temperatura, histéresis)" | Caveat: estos parámetros no están en las HDEs actuales de la KB (v6/v6-rv1 del GSM-MB no incluyen la sección NTC). Este claim requiere la HDE actualizada de I+D antes de ser usado en ningún documento externo. [Gap documental crítico — Vera NOTA-2 / Checkpoint 1 gap 1] |
| "Protección térmica que complementa la protección por corriente — dos capas de seguridad" | Caveat: el claim es técnicamente correcto (NTC mide temperatura física; NODO-D mide corriente + imagen térmica calculada). Requiere aclarar que NODO-C aplica a GSM-MB/RB/RE (monofásico) y NODO-D aplica a Genius/Exceline Profesional (trifásico) — no son el mismo producto ni la misma instalación. |
| "Integración NTC estándar de serie, sin costo de módulo adicional" | Caveat: el claim competitivo (vs. módulo Siemens) es correcto pero requiere la acotación "en protectores monofásicos para uso residencial/comercial". No es comparable directamente con los módulos de temperatura de Siemens SIMOCODE o Schneider LTMR que son para aplicaciones industriales trifásicas. [Gate Bruna: alcance del claim comparativo] |
| "Thermo-Safe — Caso A (NTC visible en empaque)" | Caveat: si el nombre Thermo-Safe o la mención NTC aparece en el empaque, Bruna debe resolver el Caso A vs Caso B (impacto en descriptividad del nombre para SAPI). El messaging externo en Caso A debe ser más cuidadoso con los claims de temperatura. [Gate Bruna: Caso A/B — decisión pendiente] |

### Claims prohibidos ❌

| Claim | Razón |
|-------|-------|
| "Temperatura exacta del motor, monitoreo continuo con precisión [X]°C" | Los parámetros cuantitativos del NTC (precisión, rango, umbral) no están en ninguna HDE actual. Este claim no tiene soporte documental hoy. |
| "La única protección térmica real en protectores monofásicos de bajo costo" | Requiere búsqueda de mercado confirmatoria que no se realizó. No se puede sostener "única" sin verificación exhaustiva. |

---

## NODO-D — ThermalCurve (Curva inversa I-t diferenciada cold/hot)

> **Nota de estado crítico:** NODO-D tiene el perfil de riesgo más alto del portafolio. Orlan clasifica este nodo como rojo en la matriz de diferenciación. La curva inversa I-t cold/hot es estándar IEC 60947-4-1 / IEEE C37.112 presente en toda la competencia industrial relevante. Los claims de este nodo tienen nivel de gate máximo para Bruna.

### Claims defendibles ✅

| Claim | RTB que lo sostiene |
|-------|---------------------|
| "Curva de disparo frío vs curva de disparo caliente: curva caliente = curva fría / 3" | Documentado en GIII+ HDE sección E y en todos los relés Genius con clase 10 (curva fría 10, caliente 3) |
| "Clase térmica ajustable de 5 a 30 en pasos de 1 (GUCT+, GIII+, GSPT-MV)" | Documentado en HDEs correspondientes |
| "Memoria térmica: retención del estado térmico hasta 2 horas" | Documentado en GIII+ HDE y confirmado en GOCT, GSPT, GOC |
| "Implementado según IEC 60255-8-1990 e IEEE C37.112-1996" | Citados explícitamente en HDEs de GIII+, GSPT-MV, GOC |
| "Umbral de falla por sobrecarga: 100% de la imagen térmica calculada" | Documentado en HDE GIII+ |
| "Clases disponibles con curva gráfica: 5, 10, 15, 20, 25, 30 (GIII+ HDE sección E)" | Documentado |

### Claims con caveat ⚠

| Claim | Caveat literal requerido |
|-------|--------------------------|
| "Algoritmo de imagen térmica propietario Genteca" | Caveat: el algoritmo implementa el estándar IEEE C37.112 / IEC 60255-8. La implementación específica puede tener parámetros propietarios, pero esto requiere que Vera documente qué aspecto de la implementación es propietario más allá del estándar. Sin ese RTB adicional, el claim de "propietario" no se sostiene. [Gate Bruna crítico — este es el gate que define si ThermalCurve sobrevive como nombre] |
| "La protección que se adapta al estado real del motor" | Caveat: la adaptación cold/hot está documentada en Genteca y es el beneficio real — pero la misma adaptación existe en toda la competencia industrial (Siemens 3RB3, Eaton C441, Schneider LTMR, Rockwell E300). El claim es técnicamente correcto para describir la función; no puede usarse como diferenciador competitivo sin acotación de segmento. |
| "ThermalCurve — nombre registrable como marca" | Caveat: SAPI/IMPI pueden considerar este nombre descriptivo del mecanismo técnico estándar de la categoría. La defensibilidad del nombre depende de que Bruna argumente el RTB diferenciador propietario. Sin ese argumento, ThermalCurve tiene probabilidad alta de objeción por descriptividad. [Gate Bruna: decisión crítica Phase 3] |

### Claims prohibidos ❌

| Claim | Razón |
|-------|-------|
| "La protección térmica más avanzada del mercado" | NODO-D es rojo en la matriz de Orlan. La función es estándar IEC ubiqua en toda la competencia industrial. Este claim no tiene base competitiva. |
| "Tecnología exclusiva Genteca de curva inversa cold/hot" | La curva inversa I-t cold/hot existe documentada en Siemens 3RB3, Eaton C441, Schneider LTMR, Rockwell E300, entre otros. No es exclusiva. |
| "Algoritmo térmico único en la industria" | Completamente insostenible — es el algoritmo estándar de la industria IEC/IEEE. |
| "Protección de sobrecarga inteligente sin equivalente en el mercado" | La función tiene equivalente documentado en toda la competencia de gama media-alta. |

---

## NODO-E — ForensLog (Registro forense histórico de fallas)

### Claims defendibles ✅

| Claim | RTB que lo sostiene |
|-------|---------------------|
| "Registro de las últimas 100 fallas (GIII+MV)" | HDE GIII+MV-V1 en español e inglés — dato explícito y verificado |
| "Registro de las últimas 20 fallas (gama Genius estándar: GIII+, GUCT+, GSPT, GOC, GOCT, GI+, GII+)" | HDE GIII+ y catálogo Genius — datos verificados |
| "Registro de las últimas 80 fallas (GSPT-MV)" | Manual técnico GSPT-MV — dato verificado |
| "Campos por evento: tipo de falla + valor medido + hora + fecha + duración" | Documentado en HDE GIII+ sección F |
| "Retención de parámetros activos al momento de la falla (GIII+MV)" | HDE GIII+MV HDE español sección comunicaciones |
| "Acceso dual al historial: pantalla LCD + MODBUS RTU" | Documentado en HDEs GIII+/GIII+MV |
| "Reloj con fecha incluido — timestamp completo por evento (GIII+)" | HDE GIII+ sección programador horario |
| "Registro en memoria no volátil — circular, sobreescritura del evento más antiguo" | Documentado en HDEs |
| "10 veces más registros que Rockwell E300 (100 vs 10 en GIII+MV)" | Rockwell E300: 5 trip records + 5 warning records verificados en manual E300 193-UM015. GIII+MV: 100 fallas verificado en HDE. Claim aritmético sostenido. |

### Claims con caveat ⚠

| Claim | Caveat literal requerido |
|-------|--------------------------|
| "ForensLog — registro de 100 fallas" (en publicidad o naming sin acotación de producto) | Caveat: "100 fallas" aplica exclusivamente al GIII+MV. La gama Genius estándar tiene 20 fallas. Si el nombre ForensLog se usa como denominación del portafolio completo Genius, el claim de "100 fallas" debe ir siempre acompañado de la acotación "en GIII+MV". [Decisión de acotación pendiente Solenne Phase 4 — Checkpoint 1 Decisión 3] |
| "El mayor registro de fallas en relés de motor de baja tensión en su segmento" | Caveat: basado en los competidores investigados por Orlan. Eaton C441 y Siemens SIMOCODE no tienen capacidad de registro confirmada en datasheet primario (marcados como [CLAIM] en OL-1). Requiere verificación confirmatoria para usar en material externo. [Gate Bruna: alcance del claim comparativo] |
| "Diagnóstico completo sin herramientas externas" | Caveat: el acceso vía bus requiere GIO-Link y software GIO-Tool. El acceso vía pantalla LCD sí es sin herramientas externas. El claim debe acotarse a "acceso en campo vía pantalla" para ser limpio. |

### Claims prohibidos ❌

| Claim | Razón |
|-------|-------|
| "Registro de 100 fallas — gama Genius completa" | Factualmente incorrecto. La gama estándar tiene 20 fallas. 100 es exclusivo del GIII+MV. |
| "El único relé con registro forense de fallas" | La función de registro de fallas existe en toda la competencia. El diferenciador es la capacidad (100 eventos) y la completitud de campos, no la unicidad de la función. |

---

## NODO-F — TripleLock (Bloqueo permanente tras tercera falla recurrente)

### Claims defendibles ✅

| Claim | RTB que lo sostiene |
|-------|---------------------|
| "Bloqueo permanente tras 3 fallas de corriente en menos de 30 minutos" | Documentado explícitamente en GIII+ HDE sección E, GOC HDE sección E, catálogo Genius, catálogo trifásico GSC |
| "Tiempo de disparo permanente en tercera falla: menos de 1 segundo" | GOC HDE sección E: "Trip Delay because of 3 Current Failures: <1 sec in less than 30 min" — dato explícito |
| "Reset manual obligatorio para restablecer operación tras bloqueo permanente" | Documentado en múltiples HDEs |
| "Aplica a cualquier tipo de falla de corriente: sobrecarga, desbalance de corriente, pérdida de fase por corriente" | Documentado en HDEs GIII+, GOC, catálogo |
| "Presente en: GOCT, GUCT+, GSPT, GSPT-MV, GIII+, GIII+MV, GOC (Genius) y GSC-CR, GSC-MB (Exceline Profesional)" | HDEs y catálogos correspondientes |

### Claims con caveat ⚠

| Claim | Caveat literal requerido |
|-------|--------------------------|
| "Función nombrada y diferenciada — la competencia solo tiene parámetros configurables sin identidad de feature" | Caveat: basado en la investigación de Orlan — ningún competidor identificado tiene nombre comercial de fantasía para esta función. Sin embargo, Schneider LTMR, Eaton C440/C441 y Rockwell E300 tienen funciones de conteo de fallas y reset inhibit no completamente verificadas en datasheet primario en algunos casos (marcados [CLAIM] en OL-1). [Gate Bruna: alcance del claim diferenciador en publicidad] |
| "TripleLock — nombre registrable como marca clase 9" | Caveat: "Triple" como componente numérico descriptor + "Lock" con saturación en clase 9 seguridad física. Búsqueda sectorial pendiente (BR-2 previo). [Gate Bruna: viabilidad del nombre antes de que Solenne genere candidatos adicionales] |
| "El sistema no permite rearranque automático tras diagnóstico crítico — obliga intervención técnica deliberada" | Caveat: el claim es correcto para la función de bloqueo permanente. Debe acotarse a "tras tres fallas de corriente en ventana de 30 minutos" — no aplica a otras categorías de falla (voltaje, frecuencia) que tienen lógica de rearranque diferente. |

### Claims prohibidos ❌

| Claim | Razón |
|-------|-------|
| "El único sistema de bloqueo inteligente para motores" | La función existe en la competencia como parámetro configurable — el diferenciador es el naming y la visibilidad del feature, no la unicidad de la función |
| "Protección total contra ciclos de falla repetida" | "Total" es absoluto no sostenido — aplica a fallas de corriente en 30 minutos, no a todos los escenarios de falla posibles |

---

## NODO-G — TaskMemory (Memoria de estado y reanudación de tarea post-corte)

### Claims defendibles ✅

| Claim | RTB que lo sostiene |
|-------|---------------------|
| "Reanudación automática de la tarea al restablecer la energía, sin intervención del usuario" | Texto literal de HDE GRN-MV v9: "retoma automáticamente la última función al restablecerse la energía, sin requerir intervención del usuario" |
| "Tres modos persistidos: vaciado de pozo, llenado de tanque, espera" | HDE GRN-MV v9, sección características generales |
| "Sin equivalente nombrado en controladores de nivel/bombeo residencial-comercial identificado en la competencia" | Investigación Orlan OL-1 — ningún fabricante identificado tiene función equivalente nombrada en este segmento. [NODO-G calificado verde por Orlan] |

### Claims con caveat ⚠

| Claim | Caveat literal requerido |
|-------|--------------------------|
| "Tiempo de confirmación de 10 segundos antes de actuar la salida post-restablecimiento" | Caveat: este RTB fue confirmado verbalmente por I+D. La HDE GRN-MV v9 no lo incluye. No debe usarse en material externo hasta que la HDE sea actualizada o se provea addendum. [Gap documental — Checkpoint 1 gap 3 / Vera NOTA-4] |
| "TaskMemory — función sin equivalente en la industria" | Caveat: la investigación de Orlan cubre los fabricantes de la lista obligatoria (ABB/Siemens/Schneider/Eaton/Rockwell/Chint/LS/Lovato). No se investigó la totalidad del mercado de controladores de nivel/bombeo. El claim "sin equivalente" aplica a los competidores investigados. [Gate Bruna: alcance del claim antes de uso externo] |
| "TaskMemory — nombre registrable como marca clase 9" | Caveat: riesgo de colisión con clase 9 software/apps (gestión de procesos — "task memory" es término de informática). Búsqueda sectorial en clase 9 software es crítica antes de confirmar viabilidad del nombre. [Gate Bruna: confirmar que Solenne evite candidatos con "Task" + "Memory" como descriptores literales si hay colisión] |

### Claims prohibidos ❌

| Claim | Razón |
|-------|-------|
| "El equipo aprende tu rutina de riego/bombeo" | "Aprender" implica IA/ML — el mecanismo es persistencia de modo operativo, no aprendizaje de patrones. El claim es semánticamente incorrecto. |
| "Memoria inteligente que recuerda todo" | El scope de la memoria es específico: modo operativo del GRN-MV. Ampliar a "todo" es sobredimensionado e incorrecto. |
| "Aplicable a toda la gama Exceline Profesional" | TaskMemory es función específica del GRN-MV — no aplica a otros productos de la línea. |

---

## NODO-H — Ecosystem GIO (Conectividad industrial integrada)

### Claims defendibles ✅

| Claim | RTB que lo sostiene |
|-------|---------------------|
| "MODBUS RTU integrado en todos los relés Genius — sin módulo adicional" | Documentado en catálogo Genius y HDEs de toda la gama |
| "Velocidades MODBUS: 9600 baud (todos los Genius) / 9600-19200-38400 baud (GIII+MV)" | HDE GIII+MV y catálogo Genius |
| "Red de hasta 32 relés en bus RS-485 vía GIO-A-RS485K" | HDE GIO-Link |
| "Variables accesibles vía bus: corriente (I1/I2/I3), voltaje (L1/L2/L3), frecuencia, kW, kVA, kWh, factor de potencia, temperatura, histórico de fallas, estados de alarma, encendido/apagado remoto, parámetros con contraseña" | Documentado en catálogo Genius y HDEs individuales |
| "GIO PORT integrado en todos los relés Genius — interfaz física propietaria" | Documentado en catálogo Genius |
| "GIO-Tool: monitorización en tiempo real, extracción de históricos, gráficas de tendencias, exportación CSV" | HDE GIO-Tool |
| "Protocolo MODBUS RTU: formato 8N1, direcciones 1-127" | HDE GIII+ sección F |

### Claims con caveat ⚠

| Claim | Caveat literal requerido |
|-------|--------------------------|
| "Conectividad industrial integrada desde el diseño — sin módulos adicionales" | Caveat: aplica a la gama Genius. Exceline y Exceline Profesional no tienen GIO PORT. El claim debe acotarse a "gama Genius". |
| "La conectividad industrial más completa en su clase de producto en VE/MX" | Caveat: la investigación de Orlan muestra que la mayoría de competidores directos en gama media requieren módulo adicional para MODBUS. Sin embargo, Schneider TeSys T tiene RS485 Modbus disponible (marcado como [CLAIM parcial] en OL-1 — no completamente verificado). [Gate Bruna: alcance del claim comparativo antes de uso en publicidad] |
| "Ecosystem GIO — denominación propietaria Genteca para el sistema de conectividad" | Caveat: la documentación formal del Ecosystem GIO como sistema diferenciado de MODBUS puro está pendiente (Checkpoint 1 gap 4 — I+D debe elaborar antes de reunión con abogado). El claim de denominación propietaria es correcto, pero el abogado muy probablemente pedirá documentación que delimite qué es propiedad Genteca vs el protocolo estándar. |
| "Candidatos de naming para NODO-H (Solenne Phase 4)" | Caveat obligatorio: los 4 candidatos no deben contener "MODBUS" ni términos de protocolo estándar. Deben anclar en la familia GIO o crear nombres para el ecosystem propietario, no para el protocolo subyacente. [Checkpoint 1 Decisión 1 — instrucción explícita para Solenne] |

### Claims prohibidos ❌

| Claim | Razón |
|-------|-------|
| "Tecnología de comunicación MODBUS propietaria Genteca" | MODBUS RTU es protocolo abierto de la industria (Modbus Organization). No puede reclamarse como propietario. |
| "Conectividad sin límites para toda la gama Genteca" | La conectividad GIO aplica a la gama Genius. Exceline no tiene GIO PORT. Además, MODBUS RTU tiene límites técnicos reales (32 nodos, velocidades documentadas). |
| "El único relé con MODBUS integrado en la clase" | Schneider TeSys T tiene RS485 Modbus (no completamente verificado si es nativo o módulo, pero el claim de "único" no se sostiene con la información disponible). |

---

## Temas sensibles para Bruna — Resumen ejecutivo

Los siguientes 7 ítems deben ir a Bruna en Phase 3 antes de cerrar cualquier decision sobre naming o claims externos. Son los gates que bloquean producción (Aurelio, Nerea, Solenne, Vivienne) si no se resuelven.

| # | Tema | Nodo | Riesgo | Input para Bruna |
|---|------|------|--------|-----------------|
| 1 | **Override curva inversa universal de facto** | NODO-A, NODO-B, NODO-D | Defendibilidad en publicidad y con abogado sin auditoría producto por producto | Charter §3 decisión 4 establece el override Owner. Bruna decide si ese override es sostenible en claims externos o si se acota a "gama verificada". |
| 2 | **ThermalCurve — diferenciador algorítmico propietario** | NODO-D | Riesgo de descriptividad alto (nombre + función estándar IEC). Nodo calificado rojo por Orlan. | Si Vera puede documentar en Phase 3 un parámetro propietario más allá del estándar IEC (ej: factor cold/hot diferencial, parámetro de enfriamiento específico), el nombre sobrevive. Si no, Bruna rechaza ThermalCurve y Solenne genera candidatos de reemplazo para el nodo. |
| 3 | **Thermo-Safe Caso A/B** | NODO-C | Impacto en descriptividad según si NTC aparece en empaque | Bruna resuelve si el empaque actual (con mención NTC/protección térmica) activa el Caso A (doble caveat) o si el naming se sostiene sin modificación. |
| 4 | **FlickerGuard — búsqueda OMPI ampliada** | NODO-B | Colisión potencial con productos LED en Australia/UK que usan "FlickerGuard" o "Flicker Guard" | Búsqueda OMPI pendiente del proyecto previo. Bruna confirma si la coexistencia en subclase diferente de clase 9 es navegable o si el nombre requiere ajuste. |
| 5 | **TaskMemory — colisión clase 9 software** | NODO-G | "Task memory" como término de gestión de procesos en informática. Riesgo en IMPI MX especialmente. | Bruna confirma la estrategia: ¿se registra en la subclase de equipo eléctrico con argumento de equivalencia perceptual? ¿O se genera nombre alternativo para IMPI MX? |
| 6 | **TripleLock — colisión clase 9 seguridad física** | NODO-F | "Lock" como raíz saturada en cerraduras y sistemas de seguridad física en clase 9 | Búsqueda sectorial pendiente. Bruna confirma si "TripleLock" para equipo de protección eléctrica colisiona con marcas de seguridad física o si la subclase de protección de motores está limpia. |
| 7 | **NODO-H — candidatos de naming sin términos de protocolo estándar** | NODO-H | Riesgo de usar "MODBUS" o derivados en candidatos de naming | Bruna confirma que los 4 candidatos de Solenne para NODO-H no contienen términos registrados o descriptivos del protocolo MODBUS, y que el ecosystem GIO como denominación propietaria está clara y documentadamente diferenciado del protocolo subyacente. |

---

## Supuestos y límites

**Insumos aguas arriba:**
- Vera VR-1 v1.0 y Orlan OL-1 v1.0 (ambos 2026-05-13): claims verificados contra estas versiones. Varios datos de competencia en OL-1 marcados [CLAIM] — no son RTBs verificados contra datasheet primario y no deben usarse como base de claims comparativos externos hasta verificación en Phase 5.
- Charter §3 decisión 4: override universal asumido — no auditado producto por producto. Este VA-5 marca con ⚠ cualquier claim que dependa de ese override para audiencias externas.
- Checkpoint 1 Resolución: ForensLog RTB decisión diferida a Solenne (Decisión 3) y ThermalCurve diferido a Bruna (Decisión 2).

**Validez temporal:** Este VA-5 es válido mientras los RTBs de Vera no cambien. Triggers de actualización:
- I+D provee HDE con parámetros NTC del NODO-C: los claims ⚠ de NODO-C que dependen de parámetros cuantitativos pasan a ✅ o permanecen ⚠ según lo que la HDE confirme.
- Vera documenta diferenciador algorítmico propietario en NODO-D: el claim ⚠ de "propietario" puede pasar a ✅ o seguir en ⚠ según la solidez del RTB.
- HDE GRN-MV actualizada con tiempo de confirmación 10s: el claim ⚠ de NODO-G pasa a ✅.
- Bruna resuelve gates 1-7: los ⚠ correspondientes pasan a ✅ (aprobados) o ❌ (rechazados) según decisión formal BR-2 de este proyecto.

**Este documento es propuesta de Vael.** La categorización ✅/⚠/❌ no constituye aprobación legal ni marcaria. La decisión formal para uso de cada claim en material externo (deck para abogado, publicidad, packaging, material de ventas) es de Bruna en Phase 3 apoyada en RISK-POLICY.md y con el contexto de SAPI/IMPI del abogado marcario externo.

---

*Vael — VA-5 Phase 2 completa. Listo para Phase 3 (Bruna).*
