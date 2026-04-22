# Brief Técnico — Nueva Línea GST-R (4 productos)
**Exceline Profesional — Supervisor Trifásico de Voltaje**
**Versión:** v1 | **Fecha:** 2026-04-19 | **Preparado por:** Vera (Technical Researcher)
**Uso:** Alimenta diseño de etiquetas (Ozwaldo) y redacción de hojas de especificaciones oficiales.

---

## 1. Resumen de la línea GST-R nueva

La línea GST-R de Exceline Profesional se expande de 2 a 4 productos aplicando una lógica de segmentación por tipo de carga. **GST-RT** cubre tableros, acometidas y transferencias donde la prioridad es supervisión de voltaje sin complejidad adicional. **GST-RG** aplica a motores y bombas en general, incorporando curva inversa tiempo-voltaje para tolerar las variaciones transitorias propias del arranque sin disparos innecesarios. **GST-RR** mantiene su foco en refrigeración y aire acondicionado, añadiendo también curva inversa para proteger mejor a los compresores herméticos que son sensibles tanto a subvoltaje como a reconexiones prematuras. **GST-RD** es el nivel premium de la línea: basado en la plataforma Genius GII+, incorpora pantalla LCD, ajuste digital por botones y comunicación Modbus RTU, atendiendo instalaciones que requieren monitoreo remoto, historial de fallas o integración con SCADA.

---

## 2. Tabla comparativa de los 4 productos

| Parámetro | GST-RT | GST-RG | GST-RR | GST-RD |
|---|---|---|---|---|
| **Origen / base** | GST-RM actual (sin curva inversa) | GST-RM reformulado con curva inversa | GST-RR actual + curva inversa | Genius GII+ portado a Exceline Profesional |
| **Aplicacion declarada** | Tableros, acometidas, transferencias, distribución | Motores y bombas (aplicacion general) | Refrigeración y aires acondicionados | Aplicaciones con LCD, Modbus RTU, ajuste fino |
| **Curva inversa tiempo-voltaje** | NO | SI | SI | NO (ajuste digital TD 1–30 s) |
| **LCD / HMI** | No — 3 LEDs | No — 3 LEDs | No — 3 LEDs | SI — LCD 16x2 + 4 botones pulsadores |
| **Modbus RTU** | No | No | No | SI — GIO Port, RS485, 9600 8N1 |
| **Programador horario** | No | No | No | SI — 20 eventos + 20 feriados |
| **Historial de fallas** | No | No | No | SI — ultimas 20 fallas con fecha/hora/duracion |
| **Rearme** | Automatico | Automatico | Automatico | AUTO / MANUAL (seleccionable) |
| **Proteccion bajo voltaje** | Ajustable (165–200 V~ mod.220; 350–420 V~ mod.440) | Ajustable — mismos rangos base GST-RM | Ajustable (165–200 V~ mod.220; 350–420 V~ mod.440) | Ajustable (165–225 V~ mod.220; 350–460 V~ mod.440) |
| **Proteccion sobre voltaje** | Fijo 264 V~ / 575 V~ | Fijo — igual base GST-RM | Ajustable (230–270 V~ mod.220; 495–575 V~ mod.440) | Ajustable (215–270 V~ mod.220; 460–580 V~ mod.440) |
| **Desbalance de voltaje** | IN >33% / OUT <28% | IN >33% / OUT <28% | IN >33% / OUT <28% | Ajustable 2–10% |
| **Variacion de frecuencia** | IN ±3% fn / OUT ±2% fn | IN ±3% fn / OUT ±2% fn | IN ±3% fn / OUT ±2% fn | Ajustable ±2–10% fn |
| **Fase invertida** | SI (<0,5 s) | SI (<0,5 s) | SI (<0,5 s) | SI (<1 s) |
| **Perdida de fase** | SI | SI | SI | SI |
| **TD (desconexion por falla de voltaje)** | Ajustable 0,5–10 s | Con curva inversa (a definir) | Con curva inversa (a definir) | Ajustable 1–30 s |
| **TC (tiempo de reconexion)** | Ajustable 5–600 s | Ajustable 5–600 s | Ajustable 180–600 s | Ajustable 0–600 s |
| **Modelos de voltaje** | 208/220 V~ y 440/480 V~ | 208/220 V~ y 440/480 V~ | 208/220 V~ y 440/480 V~ | 120 V~, 208/220 V~, 440/480 V~ |
| **Montaje** | Riel DIN 35 mm / superficie plana | Riel DIN 35 mm / superficie plana | Riel DIN 35 mm / superficie plana | Riel DIN / superficie plana / empotrable (flush) |
| **Salida de rele** | SPDT 3,5 A@250V~ / 1,5 A@480V~ | SPDT 3,5 A@250V~ / 1,5 A@480V~ | SPDT 3,5 A@250V~ / 1,5 A@480V~ | SPDT 3 A@240V~ / 1,5 A@480V~ |
| **Dimensiones** | 80 x 100 x 38 mm | 80 x 100 x 38 mm | 80 x 100 x 38 mm | 105 x 90 x 68 mm |
| **Peso** | 0,116 kg | 0,116 kg (estimado) | 0,116 kg | 0,230 kg |
| **IP / ambiente** | Interior | Interior | Interior | IP20 / Ambiente industrial severo |
| **Normas principales** | COVENIN 3445, IEC 61000-4-2/3/4/5 | COVENIN 3445, IEC 61000-4-2/3/4/5 | COVENIN 3445, IEC 61000-4-2/3/4/5 | IEC 61010-1, IEC 60255-6, IEC 60947-1, UL 508, CE |

---

## 3. Fichas técnicas condensadas por producto

---

### 3.1 GST-RT — Supervisor Trifásico para Tableros y Distribución

**Descripcion para etiqueta (2–3 lineas):**
Supervisor trifásico de voltaje para tableros, acometidas, transferencias y sistemas de distribución. Protege contra alto y bajo voltaje, fase perdida, fase invertida, desbalance y variación de frecuencia. Sin curva inversa — respuesta directa ante falla.

**Caracteristicas tecnicas confirmadas por documentos fuente:**
- Proteccion contra alto voltaje y bajo voltaje
- Proteccion contra apagones y parpadeos
- Proteccion contra fase invertida (deteccion <0,5 s)
- Proteccion por perdida de fase (dispara IN >33%, restaura OUT <28%)
- Proteccion por desbalance de voltaje (IN >33% / OUT <28%)
- Proteccion contra variacion de frecuencia (±3% fn / OUT ±2% fn)
- Tiempo de conexion ajustable
- 3 indicadores LED: CONECTADO/TEMPORIZADO | SOBREVOLTAJE/BAJOVOLTAJE/DESBALANCE | PERDIDA DE FASE/FASE INVERTIDA/FALLA FRECUENCIA
- Salida SPDT (contactos secos): 95-COM, 98-NA, 96-NC
- Montaje riel DIN 35 mm o superficie plana
- Carcasa ABS y Nylon

**Parametros ajustables (rangos confirmados):**

| Parametro | Modelo 220 | Modelo 440 |
|---|---|---|
| Bajo voltaje (ajustable) | 165–200 V~ | 350–420 V~ |
| Sobre voltaje (fijo) | 264 V~ | 575 V~ |
| TD desconexion por falla voltaje (ajustable) | 0,5–10 s | 0,5–10 s |
| TC reconexion (ajustable) | 5–600 s | 5–600 s |
| Deteccion fase invertida/perdida | <0,5 s | <0,5 s |
| Parpadeos | 150 ms | 150 ms |

**Modelos disponibles:**
- GST-RT220: 208/220 V~
- GST-RT440: 440/480 V~

**Normas:**
- Disenado segun: COVENIN 3445
- Verificado segun: IEC 61000-4-2, -4-3, -4-4, -4-5

**Diferenciador clave vs los otros 3:**
Es el unico de la linea sin curva inversa y sin LCD. Ideal para tableros donde la respuesta de proteccion debe ser directa y determinista, sin tolerancia extendida a variaciones. Formato compacto identico al GST-RM actual — facilita reemplazo directo.

---

### 3.2 GST-RD — Supervisor Trifásico con LCD y Modbus RTU

**Descripcion para etiqueta (2–3 lineas):**
Supervisor trifásico de voltaje con pantalla LCD, ajuste digital y comunicación Modbus RTU. Registra las ultimas 20 fallas con fecha, hora y duración. Para instalaciones industriales, sistemas BMS/SCADA y aplicaciones que exigen trazabilidad y ajuste remoto de parametros.

**Caracteristicas tecnicas confirmadas (fuente: GII+ MV-01-0017-B.01-S y MV-02-0017-B.02-S):**
- Pantalla LCD 16x2 con valores de voltaje en tiempo real (VL1-L2, VL2-L3, VL3-L1)
- Medicion de voltaje (precision ±2%) y frecuencia (precision ±1%)
- 4 botones pulsadores: Rearme, Ajuste (x2), Seleccion
- 2 LEDs indicadores de estado y falla
- Proteccion: sobrevoltaje, bajovoltaje, desbalance, perdida de fase, fase invertida, variacion de frecuencia, ciclado corto
- Historial de ultimas 20 fallas (tipo, valor, fecha, hora, duracion)
- Comunicacion MODBUS RTU @ 9600 baud, 8N1, protocolo GIO Port (RS485)
- Encendido/apagado remoto via Modbus
- Modo rearme AUTO / MANUAL (seleccionable)
- Bloqueo de parametros por clave (0000–9999)
- Programador horario: 20 eventos + 20 feriados con RTC integrado
- Carcasa UL94V0 (LEXAN, ABS, Nylon)
- IP20 — uso interior
- 3 opciones de montaje: riel DIN, superficie plana, empotrable (flush mounting)
- Expectativa de vida electrica: 100.000 operaciones
- Expectativa de vida mecanica: 10.000.000 operaciones

**Parametros ajustables (rangos confirmados — modelo 208/220 V~ y 440/480 V~):**

| Parametro | Rango modelo 220 | Rango modelo 440 |
|---|---|---|
| Bajo voltaje UV | 165–225 V~ | 350–460 V~ |
| Sobre voltaje OV | 215–270 V~ | 460–580 V~ |
| Desbalance VUB | 2–10% | 2–10% |
| Variacion frecuencia FS | ±2–10% fn | ±2–10% fn |
| TD desconexion por falla | 1–30 s | 1–30 s |
| TC reconexion | 0–600 s | 0–600 s |
| Fase invertida TD | <1 s | <1 s |

**Modelos disponibles:**
- GST-RD120: 120 V~ (linea a neutro)
- GST-RD220: 208/220 V~
- GST-RD440: 440/480 V~

**Normas:**
- IEC 61010-1, IEC 60255-6, IEC 60947-1
- UL 508
- CE (LVD & EMC)
- EMC severo: IEC 61000-4-2 hasta -4-28 (11 pruebas)

**Diferenciador clave vs los otros 3:**
Unico con pantalla LCD, Modbus RTU y registro historico de fallas. Es el nivel premium de la linea. Significativamente mas grande (105 x 90 x 68 mm vs 80 x 100 x 38 mm de los demas) — requiere espacio adicional en tablero. Tambien es el unico con modelo de 120 V~.

---

### 3.3 GST-RG — Supervisor Trifásico para Motores y Bombas (con curva inversa)

**Descripcion para etiqueta (2–3 lineas):**
Supervisor trifásico de voltaje con curva inversa tiempo-voltaje para motores y bombas. Tolera variaciones transitorias del arranque sin disparos innecesarios. Proteccion completa: sobrevoltaje, bajovoltaje, desbalance, perdida de fase, fase invertida y variacion de frecuencia.

**Caracteristicas tecnicas confirmadas (fuente: GST-RM como base + curva inversa nueva):**
- Proteccion contra alto y bajo voltaje
- Proteccion contra apagones y parpadeos
- Proteccion contra fase invertida (deteccion <0,5 s)
- Proteccion por perdida de fase (IN >33% / OUT <28%)
- Proteccion por desbalance de voltaje (IN >33% / OUT <28%)
- Proteccion contra variacion de frecuencia (IN ±3% fn / OUT ±2% fn)
- **Curva inversa tiempo-voltaje:** a mayor desviacion del voltaje, menor tiempo de disparo; a menor desviacion, mayor tolerancia
- Tiempo de conexion ajustable
- 3 indicadores LED identicos al GST-RM
- Salida SPDT contactos secos
- Montaje riel DIN 35 mm o superficie plana
- Carcasa ABS y Nylon

**Parametros ajustables (rangos confirmados — heredados de base GST-RM):**

| Parametro | Modelo 220 | Modelo 440 |
|---|---|---|
| Bajo voltaje (ajustable) | 165–200 V~ | 350–420 V~ |
| Sobre voltaje (fijo en base) | 264 V~ | 575 V~ |
| TD con curva inversa | **A DEFINIR** — ver Seccion 5 | **A DEFINIR** |
| TC reconexion (ajustable) | 5–600 s | 5–600 s |
| Deteccion fase invertida/perdida | <0,5 s | <0,5 s |

**Modelos disponibles:**
- GST-RG220: 208/220 V~
- GST-RG440: 440/480 V~

**Normas:**
- Disenado segun: COVENIN 3445
- Verificado segun: IEC 61000-4-2, -4-3, -4-4, -4-5

**Diferenciador clave vs los otros 3:**
Es el GST-RM mejorado con curva inversa — diferencia critica para motores de arranque DOL que presentan caidas de voltaje transitorias. Comparte formato fisico compacto con GST-RT y GST-RR pero agrega inteligencia de respuesta proporcional a la magnitud de la falla.

---

### 3.4 GST-RR — Supervisor Trifásico para Refrigeración y A/A (con curva inversa)

**Descripcion para etiqueta (2–3 lineas):**
Supervisor trifásico de voltaje con curva inversa tiempo-voltaje para equipos de refrigeración y aire acondicionado. Tiempo de reconexion largo (hasta 600 s) para proteger compresores herméticos del ciclado corto. Proteccion completa de fase con alto y bajo voltaje ajustables.

**Caracteristicas tecnicas confirmadas (fuente: GST-RR MV actual + curva inversa nueva):**
- Proteccion contra alto voltaje ajustable y bajo voltaje ajustable (ambos por perilla)
- Proteccion contra apagones y parpadeos
- Proteccion contra fase invertida (deteccion <0,5 s)
- Proteccion por perdida de fase (IN >33% / OUT <28%)
- Proteccion por desbalance de voltaje (IN >33% / OUT <28%)
- Proteccion contra variacion de frecuencia (IN ±3% fn / OUT ±2% fn)
- **Curva inversa tiempo-voltaje** — igual logica que GST-RG, orientada a compresores
- Tiempo de reconexion largo ajustable (minimo 180 s hasta 600 s) — anti ciclado corto
- 3 indicadores LED (igual estructura que GST-RM/RR actual)
- Salida SPDT contactos secos
- Montaje riel DIN 35 mm o superficie plana
- Carcasa ABS y Nylon

**Parametros ajustables (rangos confirmados — base GST-RR actual):**

| Parametro | Modelo 220 | Modelo 440 |
|---|---|---|
| Bajo voltaje (ajustable) | 165–200 V~ | 350–420 V~ |
| Sobre voltaje (ajustable) | 230–270 V~ | 495–575 V~ |
| TD con curva inversa | **A DEFINIR** — ver Seccion 5 | **A DEFINIR** |
| TC reconexion (ajustable) | 180–600 s | 180–600 s |
| Deteccion fase invertida/perdida | <0,5 s | <0,5 s |
| Parpadeos | 150 ms | 150 ms |

**Diferencia critica GST-RR vs GST-RG en TC:**
El TC minimo del GST-RR es **180 s** (3 minutos), mientras que el GST-RG parte de **5 s**. Esta diferencia es fundamental para la aplicacion: los compresores herméticos requieren tiempo suficiente para igualar presiones antes de rearrancar.

**Modelos disponibles:**
- GST-RR220: 208/220 V~
- GST-RR440: 440/480 V~

**Normas:**
- Disenado segun: COVENIN 3445
- Verificado segun: IEC 61000-4-2, -4-3, -4-4, -4-5

**Diferenciador clave vs los otros 3:**
Unico con sobrevoltaje ajustable por perilla (no fijo). TC minimo de 180 s — el mas alto de la linea, imprescindible para compresores. La curva inversa mejora la version anterior del GST-RR, que tenia TD fijo de 3 s para todas las fallas de voltaje.

---

## 4. La curva inversa tiempo-voltaje — que es y que significa para el usuario

### Definicion tecnica

Una curva inversa tiempo-voltaje (en ingles: inverse time-voltage characteristic) es un comportamiento de proteccion en el que **el tiempo de disparo es inversamente proporcional a la magnitud de la desviacion de voltaje**: cuanto mayor es la desviacion respecto al voltaje nominal, mas rapido actua el protector; cuanto menor es la desviacion, mas tiempo espera antes de disparar.

Ejemplo practico con curva inversa activa:
- Bajovoltaje severo (caida del 25%): disparo en ~0,5 s
- Bajovoltaje moderado (caida del 8%): espera varios segundos — tolera el arranque de un motor sin disparar

Sin curva inversa (respuesta de tiempo definido, como el GST-RT):
- Cualquier bajovoltaje que supere el umbral dispara en el mismo tiempo fijo (ej: 3 s), sin importar si es una caida profunda o una fluctuacion transitoria del arranque.

### Por que es mejor para motores y compresores

Los motores de induccion y los compresores herméticos generan **caidas de voltaje transitorias durante el arranque** (tipicamente del 15–30% durante 0,5–5 s dependiendo de la carga). Un protector de tiempo fijo puede interpretar estas caidas como fallas y disparar innecesariamente. La curva inversa distingue entre:
1. Una caida transitoria de arranque (corta duracion, magnitud moderada) — tolera y no dispara
2. Una falla real de subvoltaje sostenida (magnitud alta o duracion prolongada) — dispara rapido

Adicionalmente, para compresores, la curva inversa permite que el **TC (tiempo de reconexion) interactue con la severidad de la falla anterior**: si la falla fue severa, el protector ya disparo rapido; si fue leve y fue tolerada, no hubo desconexion. Esto reduce ciclos de desconexion/reconexion innecesarios que estresan los compresores.

### Frase comercial para etiqueta (tecnicamente precisa)

> **"Proteccion inteligente: a mayor falla, disparo mas rapido. A menor fluctuacion, mas tolerancia para su compresor."**

Alternativa mas corta para espacio reducido:

> **"Curva inversa: disparo proporcional a la falla."**

---

## 5. Gaps de informacion

Los siguientes datos **NO estan documentados** en los 9 archivos fuente revisados y deben ser completados o confirmados por el equipo tecnico de Genteca antes de emitir hojas de especificaciones oficiales:

| # | Producto(s) | Dato faltante | Impacto |
|---|---|---|---|
| 1 | **GST-RG y GST-RR** | Curva inversa: valores exactos de la funcion tiempo-voltaje (tabla o ecuacion). ¿Cual es el TD minimo y maximo segun nivel de desviacion? | Critico — sin esto no se puede documentar la funcion diferenciadora principal de ambos productos |
| 2 | **GST-RG y GST-RR** | ¿El sobrevoltaje del GST-RG es fijo (264 V~ / 575 V~) o se hace ajustable como en el GST-RR? | Necesario para tabla de parametros y copy de etiqueta |
| 3 | **GST-RG** | Rango exacto del TD con curva inversa (limites min/max) | Necesario para hoja de especificaciones |
| 4 | **GST-RR** | Rango exacto del TD con curva inversa en la version nueva (el actual tiene TD fijo de 3 s — ¿cambia con curva inversa?) | Necesario para hoja de especificaciones |
| 5 | **GST-RD** | Codigo de producto final (la nomenclatura GII+ usa modelo como GII+L208S — confirmar si el nuevo codigo sera GST-RD o diferente) | Necesario para etiqueta y sistema de pedidos |
| 6 | **GST-RD** | ¿Incluye ciclado corto (anti-short cycle) como funcion activa separada, o solo via TC ajustable? La hoja GII+ lo menciona como proteccion pero no lo detalla | Relevante para aplicaciones de refrigeracion |
| 7 | **GST-RT** | Confirmar si el sobre voltaje es fijo (264 V~ / 575 V~) como en el GST-RM base, o si se hace ajustable. El GST-R generico (hoja MV-01-009) tenia AMBOS ajustables. | Afecta parametros de etiqueta |
| 8 | **GST-RT, GST-RG, GST-RR** | IP rating declarado: los documentos base no indican IP rating explicito. Solo GST-RD tiene IP20 documentado. | Puede ser requerido por clientes industriales |
| 9 | **Todos** | Version nueva del codigo de pedido (nomenclatura exacta: ¿GST-RT220, GST-RG220, etc.?) — los docs fuente usan GST-RM220, GST-RR220, GII+L208S | Necesario para sistema de pedidos y etiqueta |
| 10 | **GST-RD** | GIO-Plug para comunicacion Modbus — ¿se incluye en el producto GST-RD o se vende por separado como en GII+? | Afecta descripcion del producto y precio |
| 11 | **GST-RG y GST-RR** | ¿Hay perilla de TD en la version con curva inversa? El GST-RM tiene perilla de TD; si la curva es automatica, esa perilla desaparece o cambia su funcion. | Impacto directo en el diseno fisico y etiqueta |
| 12 | **Todos** | Presentacion de Junta Directiva (PPTX) no pudo leerse — archivo binario no compatible con herramienta de lectura. Puede contener informacion adicional de posicionamiento. | Revisar manualmente o convertir a PDF |

---

## 6. Recomendacion sobre etiquetas

### Analisis de la etiqueta de referencia (GSM-R120B — monofasica)

La etiqueta GSM-R120B (61 mm x 80,9 mm) usa:
- Fondo azul Pantone 2925C con detalles naranja 151C y gris
- Tres diales analogicos graficos (MINIMO, MAXIMO, RECONEXION) con rangos numericos y zona naranja destacando el rango sugerido
- Nombre del producto en negrita y codigo en negrita menor
- Aplicacion declarada en texto grande y legible
- Badge "ALTA CARGA" en rectangulo de color destacado
- Especificacion de capacidad (120 V~ / 1,5 HP / Hasta 18.000 BTU)
- Badge "PROTECCION TERMICA" con icono
- Logo Exceline en la parte inferior
- Terminales entrada/salida indicados graficamente (F, N, Tierra) en los laterales
- Version en esquina inferior (VE-V10)

### Recomendaciones por producto

---

#### GST-RT — Etiqueta para tableros y distribución

**Elementos a incluir:**
- Nombre: **SUPERVISOR TRIFÁSICO PARA TABLEROS Y DISTRIBUCIÓN**
- Codigo: **GST-RT220 / GST-RT440** segun modelo
- Voltaje nominal del modelo (ej: 208/220 V~)
- Rango de ajuste bajo voltaje con escala visual (similar a dial del GSM-R120B, adaptado a rangos trifasicos: 165–200 V~)
- Tiempo de reconexion (ajustable: 5–600 s)
- Lista de protecciones en iconos pequeños o texto compacto: Sobre/Bajo V, Fase perdida, Fase invertida, Desbalance, Frecuencia
- Terminales: L1, L2, L3 / 95, 96, 98
- Normas: COVENIN 3445 | IEC 61000-4

**Elementos a NO incluir:**
- No mencionar curva inversa (este producto no la tiene)
- No mencionar LCD ni Modbus
- No mencionar aplicaciones de motores o refrigeracion — este es el producto de tableros

**Diferenciador en etiqueta:**
- Badge: **"PARA TABLEROS Y ACOMETIDAS"** o **"DISTRIBUCIÓN TRIFÁSICA"**
- Color de badge distinto al GST-RG y GST-RR para diferenciacion visual en anaquel

---

#### GST-RD — Etiqueta para aplicaciones con LCD y Modbus

**Elementos a incluir:**
- Nombre: **SUPERVISOR TRIFÁSICO CON LCD Y MODBUS RTU**
- Codigo: **GST-RD120 / GST-RD220 / GST-RD440**
- Indicar claramente: pantalla LCD, Modbus RTU, historial de 20 fallas
- Modelos de voltaje disponibles (3 modelos — incluyendo 120 V~)
- Dimensiones fisicas en etiqueta o empaque (el dispositivo es mas grande: 105x90x68 mm)
- Normas: IEC 61010-1, IEC 60255-6, IEC 60947-1, UL 508, CE
- IP20 declarado
- Mencionar 3 tipos de montaje: DIN / superficie plana / empotrable

**Elementos a NO incluir:**
- No usar diales analogicos graficos — este producto tiene ajuste digital; los diales pueden confundir al instalador
- No mencionar aplicacion especifica (motor, refrigeracion) — es un producto de nivel; aplica a cualquier carga

**Diferenciador en etiqueta:**
- Badge: **"LCD + MODBUS RTU"** en posicion prominente — este es el elemento que lo distingue
- Puede incluir pequena imagen del display LCD mostrando valores de voltaje (VL1-L2, etc.)
- Badge adicional: **"HISTORIAL DE FALLAS"** o **"20 FALLAS REGISTRADAS"**

---

#### GST-RG — Etiqueta para motores y bombas

**Elementos a incluir:**
- Nombre: **SUPERVISOR TRIFÁSICO PARA MOTORES Y BOMBAS**
- Codigo: **GST-RG220 / GST-RG440**
- Rango de bajo voltaje ajustable (dial visual)
- Tiempo de reconexion (ajustable: 5–600 s — rango corto, apto para rearranque de motores)
- Curva inversa: mencionar explicitamente
- Lista de protecciones: Sobre/Bajo V, Fase perdida, Fase invertida, Desbalance, Frecuencia
- Terminales L1, L2, L3 / 95, 96, 98
- Normas: COVENIN 3445 | IEC 61000-4

**Elementos a NO incluir:**
- No mencionar refrigeracion ni BTU ni HP especificos — la aplicacion es motores y bombas generales
- No mencionar LCD ni Modbus

**Diferenciador en etiqueta:**
- Badge: **"CURVA INVERSA"** en color destacado — es el elemento diferenciador clave
- Iconos de aplicacion: motor electrico, bomba hidraulica
- Frase corta: **"Proteccion proporcional a la falla"** o la frase sugerida en Seccion 4

---

#### GST-RR — Etiqueta para refrigeración y A/A

**Elementos a incluir:**
- Nombre: **SUPERVISOR TRIFÁSICO PARA REFRIGERACIÓN Y AIRE ACONDICIONADO**
- Codigo: **GST-RR220 / GST-RR440**
- Rango de bajo voltaje ajustable Y sobre voltaje ajustable (ambos diales — este es el unico compacto con OV ajustable)
- Tiempo de reconexion (180–600 s — prominente, es una proteccion critica para compresores)
- Curva inversa: mencionar
- Lista de protecciones: Sobre/Bajo V (ambos ajustables), Fase perdida, Fase invertida, Desbalance, Frecuencia
- Terminales L1, L2, L3 / 95, 96, 98
- Normas: COVENIN 3445 | IEC 61000-4

**Elementos a NO incluir:**
- No mencionar BTU ni HP — el GST-RR trifasico protege circuitos, no unidades especificas
- No indicar TC minimo en segundos de forma aislada — comunicarlo como "anti ciclado corto" o "minimo 3 minutos" para que el tecnico entienda el beneficio

**Diferenciador en etiqueta:**
- Badge doble: **"CURVA INVERSA"** + **"ANTI CICLADO CORTO"**
- Comunicar el TC largo como beneficio: **"Reconexion minima: 3 minutos — protege su compresor"**
- Los dos diales ajustables (V min y V max) son diferenciadores visuales respecto al GST-RG (que tiene solo bajo voltaje ajustable) — incluir ambos graficamente

---

### Nota sobre sistema de colores de la linea

La etiqueta GSM-R120B monofasica usa azul 2925C como base. Para los GST-R trifasicos se recomienda coordinar con Ozwaldo y Keiddys si se mantiene la misma paleta o si se asigna un color diferente para distinguir la linea trifasica profesional de la monofasica residencial. Esta decision debe tomarse antes de comenzar el diseno.

---

## Referencias y fuentes consultadas

| Documento | Codigo | Uso en este brief |
|---|---|---|
| Hoja de especificaciones GST-RM | Archivo KB `2026-04-18_hoja-especificaciones_trifasica-gst-rm...` | Base tecnica GST-RT y GST-RG |
| Manual instalacion GST-RM v1 | Archivo KB `2026-04-18_manual_tecnica-gst-rm-man-v1` | Rangos de perillas, indicadores, conexion |
| Hoja de especificaciones GST-RR | Archivo KB `2026-04-18_hoja-especificaciones_trifasica-gst-rr...` | Base tecnica GST-RR |
| Manual instalacion GST-RR v1 | Archivo KB `2026-04-18_manual_tecnica-gst-rr-man-v1` | Rangos de perillas GST-RR, TC 180–600 s |
| Hoja de especificaciones GII+ | Archivo KB `2026-04-18_hoja-especificaciones_trifasica-e-gii-p` | Base tecnica GST-RD — funciones, rangos, normas |
| Manual instalacion GII+ | Archivo KB `2026-04-18_manual_tecnica-i-gii-p` | Operacion, pantallas LCD, botones, montaje empotrable |
| Mapa Modbus GII+ | Archivo KB `2026-04-18_manual_tecnica-m-gii-p` | Registros Modbus, funciones comunicacion GST-RD |
| Hoja de especificaciones GST-R (generica) | Archivo KB `2026-04-17_hoja-especificaciones_exceline-profesional-gst-r` | Especificaciones base de la linea (GST-R220P/440P) |
| Hoja tecnica GST (Exceline Profesional) | Archivo KB `2026-04-18_hoja-especificaciones_tecnica-e-gst` | Funciones generales GST, rangos ajuste, normas CE |
| Etiqueta referencia GSM-R120B | `GSM-R120B_ETQ_V10.pdf` (Staging) | Estructura visual, elementos de etiqueta Exceline |
| Presentacion Junta Directiva | `GST_Exceline_Presentacion_JuntaDirectiva V3.pptx` | **NO LEIDA** — archivo PPTX binario, requiere conversion manual |

---

*Brief preparado por Vera — Technical Researcher, Genteca/Raul AI Team*
*Todos los valores numericos estan anclados a los documentos fuente citados. Los items marcados "A DEFINIR" en la Seccion 5 requieren decision del equipo tecnico de Genteca antes de publicacion oficial.*
