# GST-R — Copy de Etiquetas (ETQ) — v1
**Línea:** Exceline Profesional — Supervisores Trifásicos de Voltaje
**Preparado por:** Oz (Technical Documentation Editor)
**Fecha:** 2026-04-20
**Dirigido a:** Ozwaldo (Diseñador Gráfico) + Keiddys (aprobación)
**Fuentes consultadas:** GSM-R120B_ETQ_V10.pdf · GST_Exceline_Presentacion_JuntaDirectiva_V3_texto.md · GST-R_nueva_linea_brief_tecnico_v1.md

---

## RESUMEN EJECUTIVO

### Las 3 decisiones más importantes que el owner debe tomar para aprobar el copy

1. **Nomenclatura del producto de motores: ¿GST-RM o GST-RG?**
   La Presentación JD V3 y el brief de tarea usan **GST-RM** (ProMotor). El brief técnico de Vera usa **GST-RG**. Este documento usa GST-RM siguiendo el brief del owner, pero si el código de pedido oficial es GST-RG, todo el copy de ese producto debe actualizarse antes de enviarlo a Ozwaldo. Es la decisión de mayor impacto antes de fabricar etiquetas.

2. **TD exacto de la curva inversa (GST-RM y GST-RR): ¿0,5–3 s o a definir?**
   La Presentación JD cita "TD curva inversa: 0,5–3 s auto" para ambos productos. El brief técnico de Vera marca este valor como "A DEFINIR" hasta que I&D publique la función tiempo-voltaje exacta. Para aprobar el copy que va en la etiqueta, I&D debe confirmar si 0,5–3 s es publicable como especificación oficial o solo como valor indicativo.

3. **Color del encabezado: ¿son los mismos Pantone de la línea GSM monofásica o se diferencian para la línea trifásica profesional?**
   El brief técnico de Vera señala que esta decisión debe coordinarse con Ozwaldo y Keiddys antes del diseño. La Presentación JD asigna: Verde (GST-RT), Negro (GST-RD), Gris (GST-RM), Azul (GST-RR). Este documento usa esos colores como base, pero los hexes/Pantones exactos para la línea trifásica profesional deben ser confirmados.

---

### Qué es distinto a la etiqueta de referencia GSM-R120B

| Elemento | GSM-R120B (referencia) | GST-R (nueva línea) |
|---|---|---|
| **Tamaño** | 61 × 80,9 mm | Sugiero 70 × 95 mm — producto más grande (80×100×38 mm), más parámetros a mostrar. GST-RD sugiero 85 × 110 mm por su tamaño físico mayor (105×90×68 mm). |
| **Fases** | Monofásico (F, N, Tierra) | Trifásico (L1, L2, L3 / 95-COM, 96-NC, 98-NA) |
| **Diales gráficos** | 3 diales: MÍNIMO, MÁXIMO, RECONEXIÓN | GST-RT/RM/RR: 2–3 diales según producto. GST-RD: **ningún dial** — ajuste digital, los diales confundirían al instalador |
| **Protecciones adicionales** | Solo voltaje | + Fase perdida, fase invertida, desbalance, variación de frecuencia |
| **Curva inversa** | No aplica | Solo GST-RM y GST-RR: badge visual específico |
| **Color de header** | Azul Pantone 2925C | Variable por producto: Verde / Negro / Gris / Azul (ver cada sección) |
| **Capacidad en BTU/HP** | Sí (120 V~ / 1,5 HP / 18.000 BTU) | No aplica — protección de circuito trifásico, no por carga específica |
| **Badge "ALTA CARGA"** | Sí | No — reemplazado por badges de diferenciador por producto |
| **Protección térmica** | Sí | No — la línea GST-R no tiene protección térmica |
| **Logo** | Exceline (parte inferior) | Exceline Profesional (parte inferior — versión profesional del logo) |

---

---

## PRODUCTO 1 — GST-RT · ProTransfer

**Color del header: VERDE**
**Zona:** Tableros con ATS, generadores, acometidas

---

### Sección A — Copy propuesto

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ENCABEZADO — fondo verde]
Exceline Profesional
ProTransfer — GST-RT
Supervisor Trifásico de Voltaje para Tableros y Transferencias
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[CARACTERÍSTICAS CLAVE]
• TD AJUSTABLE: 0,5–10 s — control preciso en acometida
• TC MÍNIMO GARANTIZADO: 5 s — seguro con ATS y generadores
• IDEAL PARA ATS / TRANSFERENCIAS AUTOMÁTICAS
• 6 protecciones: alto V · bajo V · fase perdida · fase invertida · desbalance · frecuencia

[APLICACIONES]
• Tableros generales de distribución
• Transferencias automáticas (ATS)
• Generadores de respaldo
• Tableros de conmutación
• Acometidas industriales y comerciales

[DATOS TÉCNICOS]
TD: 0,5–10 s   |   TC: 5–600 s   |   V-bajo: 165–200 V~*   |   V-alto: 264 V~ fijo*
(*Modelo 220. Modelo 440: 350–420 V~ / 575 V~ fijo)

[MODELOS]
GST-RT220: 208/220 V~     GST-RT440: 440/480 V~

[NORMAS]
Diseñado según COVENIN 3445 | IEC 61000-4-2/-4-3/-4-4/-4-5
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Frase de argumento (para badge secundario o zona de texto):**
> *"No apaga todo si puede evitarlo. Solo corta cuando es necesario."*

---

### Sección B — Notas para Ozwaldo

**Color dominante del encabezado:**
- Verde. El tono aprobado en la Presentación JD es "VERDE" sin especificar Pantone. Sugiero **Pantone 368C** (verde limpio, industrial) o **Pantone 355C** (verde más saturado, visible en estante). Confirmar con Keiddys.
- Acento: **Naranja Pantone 151C** (mismo que la línea GSM-R120B) para resaltar el badge y el rango sugerido en los diales.
- Texto sobre fondo oscuro: blanco.

**Elemento visual prioritario:**
- El badge **"IDEAL PARA ATS / TRANSFERENCIAS"** debe ser el elemento de mayor peso visual después del nombre comercial. Es el diferenciador principal de este modelo en el punto de venta.

**Diales gráficos sugeridos (2 diales, no 3):**
- Dial 1 — **BAJO VOLTAJE** (ajustable): rango 165–200 V~ (modelo 220), zona naranja en rango sugerido ~185–195 V~
- Dial 2 — **RECONEXIÓN TC** (ajustable): rango 5–600 s, zona naranja en rango sugerido ~30–60 s
- El sobre voltaje es fijo (264 V~) — no requiere dial; mostrar como valor fijo en la tabla de datos técnicos.

**Terminales en laterales (igual estructura que GSM-R120B pero adaptado a trifásico):**
- Lateral izquierdo — ENTRADA: L1, L2, L3
- Lateral derecho — SALIDA: 95 (COM), 96 (NC), 98 (NA)

**Íconos sugeridos:**
- Ícono de tablero eléctrico / rack de distribución
- Símbolo de transferencia (flecha bidireccional entre dos fuentes)
- NO incluir símbolo de curva inversa — este producto NO la tiene

**Dimensiones sugeridas:** 70 × 95 mm (más alto que la referencia monofásica para acomodar 6 protecciones + terminales trifásicos + 2 diales)

---

### Sección C — Decisiones pendientes

1. **¿El sobre voltaje del GST-RT es fijo (264 V~ / 575 V~) o ajustable?** El brief técnico de Vera lo señala como gap #7: el GST-R genérico original tenía AMBOS ajustables; el GST-RM base (origen del GST-RT) tiene sobre voltaje fijo. Si I&D lo hace ajustable en la versión nueva, el copy de datos técnicos y el diseño de diales deben cambiar (se añadiría un tercer dial para MÁXIMO V).
2. **Pantone exacto del verde** — confirmar con Keiddys antes de que Ozwaldo elija el fondo.
3. **Frase de argumento en etiqueta** — "No apaga todo si puede evitarlo" es la frase aprobada en la Presentación JD. Confirmar si va impresa en la etiqueta o solo en materiales de punto de venta.

---

---

## PRODUCTO 2 — GST-RD · ProDigital

**Color del header: NEGRO**
**Zona:** Acometidas críticas, subtableros, variadores, PLC — Zonas 1 y 2

---

### Sección A — Copy propuesto

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ENCABEZADO — fondo negro]
Exceline Profesional
ProDigital — GST-RD
Supervisor Trifásico Digital de Voltaje — LCD + Modbus RTU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[CARACTERÍSTICAS CLAVE]
• PANTALLA LCD — voltaje de las 3 fases en tiempo real
• HISTORIAL 20 FALLAS — tipo, valor, fase, fecha y hora
• CONTRASEÑA DE SEGURIDAD — bloqueo de parámetros (0000–9999)
• MODBUS RTU — integración SCADA/BMS vía RS485

[APLICACIONES]
• Variadores de frecuencia y arrancadores suaves
• Controladores lógicos (PLC) y salas de control
• Instrumentación crítica y laboratorios
• Subtableros industriales con equipos sensibles
• Acometidas de gran envergadura

[DATOS TÉCNICOS]
TD: 1–30 s   |   TC: 0–600 s   |   V-bajo: 165–225 V~*   |   V-alto: 215–270 V~*
Desbalance: 2–10% ajustable   |   IP20
(*Modelo 220. Modelo 440: 350–460 V~ / 460–580 V~)

[MODELOS]
GST-RD120: 120 V~     GST-RD220: 208/220 V~     GST-RD440: 440/480 V~

[NORMAS]
IEC 61010-1 · IEC 60255-6 · IEC 60947-1 · UL 508 · CE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Frase de argumento (para badge secundario):**
> *"TQ tiene pantalla. El GST-RD también — más historial, contraseña y soporte local."*

*(Nota: esta frase es para material de punto de venta y vendedor — evaluar si es apropiada imprimirla directamente en la etiqueta o si queda mejor en tarjeta/hanger. Ver Decisiones Pendientes.)*

---

### Sección B — Notas para Ozwaldo

**Color dominante del encabezado:**
- Negro. Fondo negro con texto blanco para el header. Acento en **blanco puro** y/o **Pantone 151C naranja** para los badges de LCD, Historial, Contraseña.
- Considerar un toque de gris (Cool Gray 10C, igual que la referencia GSM-R120B) para zonas secundarias.

**Elemento visual prioritario:**
- La pantalla LCD es el diferenciador #1. **Ozwaldo debe incluir una representación gráfica de la pantalla LCD** mostrando los valores de voltaje (ej: VL1-L2: 218V / VL2-L3: 221V / VL3-L1: 219V). Esto comunica instantáneamente en el punto de venta lo que ningún competidor sin pantalla puede mostrar.
- Los 4 badges de características clave (LCD / HISTORIAL / CONTRASEÑA / MODBUS) deben presentarse como íconos visuales, no solo texto.

**Sin diales gráficos:**
- El GST-RD tiene ajuste digital por botones. Los diales analógicos gráficos (como en GSM-R120B) NO deben incluirse — confundirían al instalador haciéndolo buscar perillas que no existen. En su lugar: representación de botones o pantalla.

**Terminales en laterales:**
- Lateral izquierdo — ENTRADA: L1, L2, L3
- Lateral derecho — SALIDA: 95 (COM), 96 (NC), 98 (NA) + nota de GIO Port (RS485) si hay espacio

**Íconos sugeridos:**
- Pantalla LCD (representación gráfica — ver arriba)
- Ícono de candado/contraseña
- Ícono de red/comunicación (Modbus/RS485)
- Ícono de historial/log de fallas
- Ícono de rearme manual (flecha circular)

**Dimensiones sugeridas:** 85 × 110 mm — el dispositivo físico mide 105×90×68 mm, que es significativamente más grande que los otros 3 modelos. La etiqueta también debe ser más grande para no quedar visualmente pequeña sobre el aparato.

**Montaje:**
- Incluir los 3 tipos de montaje como íconos pequeños al pie: DIN rail / superficie / empotrable (flush)

---

### Sección C — Decisiones pendientes

1. **¿La frase anti-TQ va en la etiqueta o solo en material de venta?** La Presentación JD la propone para "respuesta a TQ con pantalla" — pero ponerla directamente en la etiqueta física es agresivo. Sugerencia Oz: dejarla para hanger/tarjeta en punto de venta y en la hoja de especificaciones. Confirmar con Keiddys.
2. **¿El GIO-Plug (módulo RS485 para Modbus) se incluye en el producto o se vende por separado?** (Gap #10 del brief de Vera). Si se incluye, el copy puede decir "Modbus RTU incluido". Si se vende aparte, la etiqueta debe decir "Puerto GIO para Modbus RTU (módulo opcional)".
3. **Confirmación del código GST-RD** — el brief de Vera señala que la nomenclatura final no está 100% confirmada (Gap #5). Verificar con I&D si el código de pedido es GST-RD120/220/440 o usa otra convención.
4. **Rearme manual/auto** — el copy no lo menciona explícitamente en bullets para no saturar el espacio. Si Keiddys lo considera diferenciador importante (la Presentación JD lo lista), puede reemplazar el bullet de Modbus en una versión alternativa.

---

---

## PRODUCTO 3 — GST-RM · ProMotor

**Color del header: GRIS**
**Zona:** Motores, bombas, ventiladores industriales

---

### Sección A — Copy propuesto

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ENCABEZADO — fondo gris oscuro]
Exceline Profesional
ProMotor — GST-RM
Supervisor Trifásico de Voltaje para Motores y Bombas
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[CARACTERÍSTICAS CLAVE]
• CURVA INVERSA DE VOLTAJE — reacción proporcional a la falla
• TD 0,5–3 s AUTOMÁTICO según severidad del voltaje
• RECONEXIÓN DESDE 5 s — rearranque rápido de motores
• 6 protecciones: alto V · bajo V · fase perdida · fase invertida · desbalance · frecuencia

[APLICACIONES]
• Motores industriales de inducción
• Bombas centrífugas y sumergibles
• Ventiladores y extractores industriales
• Sopladores y maquinaria de producción
• Sistemas hidroneumáticos

[DATOS TÉCNICOS]
TD: 0,5–3 s (curva inv. auto)   |   TC: 5–300 s   |   V-bajo: 165–200 V~*   |   V-alto: 230–270 V~*
(*Modelo 220. Modelo 440: 350–420 V~ / 495–575 V~)

[MODELOS]
GST-RM220: 208/220 V~     GST-RM440: 440/480 V~

[NORMAS]
Diseñado según COVENIN 3445 | IEC 61000-4-2/-4-3/-4-4/-4-5
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Frase de argumento (para badge secundario):**
> *"Reacción proporcional — más rápido ante fallas más graves."*

---

### Sección B — Notas para Ozwaldo

**Color dominante del encabezado:**
- Gris oscuro. La Presentación JD especifica "GRIS" sin Pantone. Sugiero **Cool Gray 10C** (mismo que se usa como secundario en la línea GSM-R120B — crea coherencia visual) o **Pantone 431C** (gris azulado industrial). El acento debe ser **Pantone 151C naranja** para los badges, especialmente el badge de CURVA INVERSA.
- Texto sobre fondo gris oscuro: blanco.

**Elemento visual prioritario:**
- El badge **"CURVA INVERSA DE VOLTAJE"** es el diferenciador absoluto de este producto vs. cualquier protector genérico de tiempo fijo. Debe ser el elemento más visible después del nombre comercial — sugerencia: badge rectangular naranja con texto blanco, posición inmediatamente debajo del nombre "ProMotor".

**Íconos sugeridos:**
- **Símbolo de curva inversa:** una línea curva descendente (tiempo en eje Y, desviación de voltaje en eje X) — simple, técnica, comunica el concepto de un vistazo. Es la representación estándar en relés de protección.
- Ícono de motor eléctrico (M dentro de círculo)
- Ícono de bomba hidráulica
- NO incluir ícono de compresor ni snowflake/refrigeración — ese es el GST-RR

**Diales gráficos sugeridos (2 diales):**
- Dial 1 — **BAJO VOLTAJE** (ajustable): rango 165–200 V~ (modelo 220), zona naranja en rango sugerido
- Dial 2 — **RECONEXIÓN TC** (ajustable): rango 5–300 s
- El sobre voltaje es fijo (confirmar con I&D si es 264 V~ fijo o ajustable — Gap #2 del brief Vera). Si es fijo: mostrar como valor en tabla, no como dial.
- **No hay dial de TD** — la curva inversa es automática; no hay perilla de TD para el usuario. Esto es diferente al GSM-R120B y debe quedar claro visualmente (el TD es un valor mostrado, no un ajuste).

**Terminales en laterales:**
- Lateral izquierdo — ENTRADA: L1, L2, L3
- Lateral derecho — SALIDA: 95 (COM), 96 (NC), 98 (NA)

**Dimensiones sugeridas:** 70 × 95 mm (igual que GST-RT — misma carcasa física 80×100×38 mm)

**Nota crítica para Ozwaldo:** Este producto NO incluye protección de ciclado corto. Si el diseño usa iconografía de refrigeración por error, puede generar confusión en el canal. El GST-RR (ProFrio, azul) es el de refrigeración.

---

### Sección C — Decisiones pendientes

1. **Nomenclatura: ¿GST-RM o GST-RG?** — Decisión crítica #1 del Resumen Ejecutivo. Confirmar con I&D el código de pedido oficial antes de enviar a Ozwaldo.
2. **TD exacto de curva inversa: ¿0,5–3 s es publicable?** — La Presentación JD dice "0,5–3 s auto". El brief técnico de Vera lo marca como "A DEFINIR". I&D debe confirmar si estos valores son la especificación publicable o son indicativos de desarrollo.
3. **¿El sobre voltaje del GST-RM es fijo (264 V~) o ajustable?** La Presentación JD cita "V-alto: 230–270 V~" para el ProMotor (igual que el GST-RR), lo que sugiere que podría ser ajustable en la versión nueva. El brief técnico no confirma el cambio. Impacta si hay dial de MÁXIMO en la etiqueta.
4. **¿Hay perilla de TD en la versión con curva inversa?** (Gap #11 del brief Vera). Si la curva es 100% automática y la perilla de TD desaparece, la etiqueta debe reflejar esto. Si la perilla cambia de función (ej: ajuste de sensibilidad), debe mencionarse.

---

---

## PRODUCTO 4 — GST-RR · ProFrio

**Color del header: AZUL**
**Zona:** Compresores de refrigeración y aire acondicionado

---

### Sección A — Copy propuesto

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ENCABEZADO — fondo azul]
Exceline Profesional
ProFrio — GST-RR
Supervisor Trifásico de Voltaje para Refrigeración y Aire Acondicionado
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[CARACTERÍSTICAS CLAVE]
• PROTECCIÓN DE CICLADO CORTO — ciclo de espera 3 min obligatorio
• CURVA INVERSA DE VOLTAJE — reacción proporcional a la falla
• VOLTAJE ALTO Y BAJO AJUSTABLES — control independiente por perilla
• 6 protecciones: alto V · bajo V · fase perdida · fase invertida · desbalance · frecuencia

[APLICACIONES]
• Compresores de A/A central
• Cuartos fríos y cámaras frigoríficas
• Chillers de agua helada
• Equipos industriales de refrigeración
• Sistemas VRF y multisplit trifásicos

[DATOS TÉCNICOS]
TD: 0,5–3 s (curva inv. auto)   |   TC: 180–600 s (mín. 3 min)   |   V-bajo: 165–200 V~*   |   V-alto: 230–270 V~*
(*Modelo 220. Modelo 440: 350–420 V~ / 495–575 V~)

[MODELOS]
GST-RR220: 208/220 V~     GST-RR440: 440/480 V~

[NORMAS]
Diseñado según COVENIN 3445 | IEC 61000-4-2/-4-3/-4-4/-4-5
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Frase de argumento (para badge secundario):**
> *"Los genéricos reconectan antes de tiempo y matan el compresor."*

*(Evaluar si va en etiqueta física o en material de venta — ver Decisiones Pendientes.)*

**Frase alternativa más técnica para etiqueta:**
> *"Reconexión mínima: 3 minutos — protege la mecánica del compresor."*

---

### Sección B — Notas para Ozwaldo

**Color dominante del encabezado:**
- Azul. La Presentación JD especifica "AZUL". El azul de la línea de referencia (GSM-R120B) es **Pantone 2925C**. Para la línea trifásica GST-RR, sugiero mantener el mismo Pantone 2925C para crear coherencia visual entre la línea monofásica de refrigeración (GSM-R120B/R150B) y la trifásica (GST-RR). Confirmar con Keiddys si se quiere diferenciar o unificar.
- Acento: **Pantone 151C naranja** para los badges críticos (CICLADO CORTO, CURVA INVERSA).
- Texto sobre fondo azul: blanco.

**Elemento visual prioritario:**
- El badge **"PROTECCIÓN DE CICLADO CORTO"** con el valor **"3 MIN"** es el diferenciador EXCLUSIVO de toda la línea — ningún otro modelo GST-R lo tiene, y los genéricos no lo tienen. Debe ser el primer elemento después del nombre comercial. Sugiero un badge de mayor tamaño que los demás, con el valor "3 MIN" en número grande.

**Íconos sugeridos:**
- **Ícono de ciclado corto / reloj:** un reloj o cronómetro mostrando 3 minutos — comunica visualmente la espera obligatoria.
- **Símbolo de curva inversa** (mismo que GST-RM — línea curva descendente) — pero en posición secundaria respecto al badge de ciclado corto.
- Ícono de compresor / snowflake / copo de nieve — diferencia este producto del GST-RM en el punto de venta de canal refrigeración.
- Ícono de A/A (split unit)

**Diales gráficos sugeridos (3 diales — único producto de la línea con 3 diales):**
- Dial 1 — **BAJO VOLTAJE** (ajustable): rango 165–200 V~ (modelo 220), zona naranja en rango sugerido
- Dial 2 — **ALTO VOLTAJE** (ajustable): rango 230–270 V~ (modelo 220) — **este dial es diferenciador vs. GST-RT y GST-RM** donde el sobre voltaje es fijo. Ozwaldo debe destacarlo visualmente.
- Dial 3 — **RECONEXIÓN TC** (ajustable): rango 180–600 s — marcar claramente el mínimo de 180 s (3 min) con una zona de color de advertencia. El piso de 180 s no se puede bajar; esto es una protección por hardware.

**Terminales en laterales:**
- Lateral izquierdo — ENTRADA: L1, L2, L3
- Lateral derecho — SALIDA: 95 (COM), 96 (NC), 98 (NA)

**Dimensiones sugeridas:** 70 × 100 mm (ligeramente más alto que GST-RT/RM para acomodar 3 diales + badge doble CICLADO CORTO + CURVA INVERSA)

**Nota crítica para Ozwaldo:** El TC mínimo de 180 s (3 minutos) es una restricción de hardware — el técnico NO puede configurarlo por debajo de ese valor. Esto debe quedar claro visualmente en el dial de RECONEXIÓN. Sugerencia: zona de "zona prohibida" o tope visual en la escala del dial antes de 180 s, similar a como el GSM-R120B usa la zona naranja para indicar el rango sugerido.

---

### Sección C — Decisiones pendientes

1. **TD exacto de curva inversa: ¿0,5–3 s es publicable?** — Mismo gap que GST-RM. I&D debe confirmar antes de fijar el copy.
2. **¿El Pantone azul es 2925C (igual al GSM-R120B monofásico) o diferente para la línea trifásica?** Impacta coherencia visual del canal refrigeración. Si se unifica: el técnico asocia el azul con "refrigeración Exceline" en todas las líneas. Si se diferencia: la línea profesional trifásica tiene identidad propia separada de la residencial/comercial.
3. **Frase argumental en etiqueta:** "Los genéricos reconectan antes de tiempo y matan el compresor" es poderosa para el vendedor. Evaluar si es apropiada en la etiqueta física o solo en material POP. La alternativa técnica ("Reconexión mínima: 3 minutos") es más apropiada para la etiqueta.
4. **¿El sobre voltaje del GST-RR nuevo sigue siendo ajustable?** La base actual GST-RR ya tiene OV ajustable (confirmado en brief Vera: 230–270 V~ / 495–575 V~). El brief confirma que se mantiene. Pero I&D debe validar que no cambia con la adición de curva inversa.

---

---

## ANEXO — Tabla resumen de copy por producto

| Elemento | GST-RT ProTransfer | GST-RD ProDigital | GST-RM ProMotor | GST-RR ProFrio |
|---|---|---|---|---|
| **Color header** | Verde | Negro | Gris | Azul |
| **Descriptor** | Tableros y Transferencias | Digital — LCD + Modbus RTU | Motores y Bombas | Refrigeración y A/A |
| **Bullet 1** | TD AJUSTABLE 0,5–10 s | PANTALLA LCD | CURVA INVERSA | PROTECCIÓN CICLADO CORTO |
| **Bullet 2** | TC MÍNIMO 5 s | HISTORIAL 20 FALLAS | TD 0,5–3 s AUTO | CURVA INVERSA |
| **Bullet 3** | IDEAL ATS/TRANSFERENCIAS | CONTRASEÑA | RECONEXIÓN DESDE 5 s | V-ALTO Y V-BAJO AJUSTABLES |
| **Bullet 4** | 6 protecciones | MODBUS RTU | 6 protecciones | 6 protecciones |
| **TD en etiqueta** | 0,5–10 s (ajustable) | 1–30 s (digital) | 0,5–3 s (curva inv. auto) | 0,5–3 s (curva inv. auto) |
| **TC en etiqueta** | 5–600 s | 0–600 s | 5–300 s | 180–600 s (mín. 3 min) |
| **Diales gráficos** | 2 (V-bajo, TC) | Ninguno | 2 (V-bajo, TC) | 3 (V-bajo, V-alto, TC) |
| **Badge diferenciador** | ATS/TRANSFERENCIAS | LCD + HISTORIAL + CONTRASEÑA | CURVA INVERSA | CICLADO CORTO 3 MIN |
| **Dimensiones sugeridas** | 70 × 95 mm | 85 × 110 mm | 70 × 95 mm | 70 × 100 mm |
| **Modelos** | 220 / 440 | 120 / 220 / 440 | 220 / 440 | 220 / 440 |
| **Normas** | COVENIN 3445 + IEC 61000-4 | IEC 61010-1 + UL 508 + CE | COVENIN 3445 + IEC 61000-4 | COVENIN 3445 + IEC 61000-4 |

---

*Documento preparado por Oz — Technical Documentation Editor*
*Versión: v1 | Fecha: 2026-04-20*
*Dirigido a: Ozwaldo (diseño) + Keiddys (aprobación)*
*Pendiente de aprobación antes de producción de arte final*
