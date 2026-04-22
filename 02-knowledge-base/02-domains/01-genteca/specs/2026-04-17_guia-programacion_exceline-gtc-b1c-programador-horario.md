# Guía de Programación — Programador Horario Digital GTC-B1C

**Línea:** Exceline  
**Código de producto:** GTC-B1C  
**Tipo de documento:** Guía de Programación  
**Fabricante:** Gente, Generación de Tecnología, C.A. — www.genteca.com.ve  
**Referencia PDF:** C_003.pdf (Exceline/C_003.pdf en RAG_SOURCES)

---

## Descripción del Teclado

| # | Tecla | Función |
|---|-------|---------|
| 1 | Pantalla LCD | Visualización de programación de eventos |
| 2 | Prog | Ingresar al Menú de Programación |
| 3 | Reloj | Ajustar reloj / Salir del Menú |
| 4 | Día | Seleccionar días de la semana |
| 5 | Hora | Ajustar la hora |
| 6 | Minutos | Ajustar los minutos |
| 7 | Pulsador R | Restaurar el GTC-B1C, borrar programación, recuperar estado original de fábrica |
| 8 | Manual | Encender o apagar manualmente la carga |
| 9 | Cubierta protectora | Bornes de conexión de cables |
| 10 | Tapa posterior | Batería reemplazable |
| 11 | Gancho sujetador | Montaje en riel simétrico |
| 12 | Guías de orificios | Montaje sobre superficie o cajón 2"×4" |
| 13 | Laminilla plástica roja | Protección de batería durante almacenaje (descartable) |

---

## A. Ajustes Básicos

### A.1 — Cómo Seleccionar el Formato de Hora

- Para **formato 24 horas**: presionar tecla Reloj hasta que desaparezca el indicador AM/PM
- Para **formato 12 horas**: presionar tecla Reloj hasta que aparezca el indicador AM/PM

### A.2 — Cómo Ajustar la Hora

Presionar y mantener oprimida la tecla **Reloj**, luego presionar la tecla **Hora** varias veces hasta llegar a la hora deseada.

### A.3 — Cómo Ajustar los Minutos

Presionar y mantener oprimida la tecla **Reloj**, luego presionar la tecla **Minutos** varias veces hasta los minutos deseados.

### A.4 — Cómo Ajustar el Día

Presionar y mantener oprimida la tecla **Reloj**, luego presionar la tecla **Día** varias veces hasta que la pantalla indique el día deseado.

---

## B. Cómo Programar el Encendido y Apagado de Equipos

El programador horario permite programar hasta **10 eventos por semana** (cada evento tiene una hora de encendido ON y una hora de apagado OFF).

### B.1 — Cómo Programar el Encendido de un Equipo

1. Presionar la tecla **Prog** para ingresar a la pantalla de programación
2. La pantalla mostrará el indicador **ON** y el número de evento (ej. 1) en la parte inferior izquierda
3. Presionar la tecla **Día** para seleccionar la combinación de días (ver Tabla B.2)
4. Presionar la tecla **Hora** hasta fijar la hora deseada
5. Presionar la tecla **Minutos** para fijar los minutos

### B.2 — Tabla de Combinaciones de Días

| Opción | Días |
|--------|------|
| 1 | LUN MAR MIE JUE VIE SAB |
| 2 | LUN |
| 3 | MAR |
| 4 | MIE |
| 5 | JUE |
| 6 | VIE |
| 7 | SAB |
| 8 | DOM |
| 9 | LUN MAR MIE JUE VIE |
| 10 | SAB DOM |
| 11 | LUN MAR MIE JUE VIE SAB |
| 12 | LUN MIE VIE |
| 13 | MAR JUE SAB |
| 14 | LUN MAR MIE |
| 15 | JUE VIE SAB |
| 16 | Solo para borrar eventos |

### B.3 — Cómo Programar el Apagado de un Equipo

1. Presionar la tecla **Prog** para avanzar a la pantalla de apagado (OFF) del evento 1
2. Seleccionar la **misma combinación de días** que el encendido (importante)
3. Fijar la hora y los minutos de apagado

> **IMPORTANTE:** Si no se usa la misma combinación de días para encendido y apagado, el funcionamiento no será el adecuado.

### B.4 — Cómo Borrar un Evento

1. Presionar **Prog** para ingresar al modo de configuración de eventos
2. Seleccionar el número del evento a borrar con la tecla **Prog**
3. Presionar **Día** hasta que desaparezcan todos los días de la parte superior de la pantalla
4. Repetir para el apagado (OFF) del mismo evento
5. Regresar a pantalla principal con la tecla **Reloj**

---

## C. Modos de Funcionamiento

Presionar la tecla **Manual** para ciclar entre modos:

| Modo | Descripción |
|------|-------------|
| Manual ON | Equipo encendido permanentemente (ignora eventos programados) |
| Manual OFF | Equipo apagado permanentemente (ignora eventos programados) |
| Auto ON | Equipo encendido hasta el próximo evento de apagado |
| Auto OFF | Equipo apagado hasta el próximo evento de encendido (**opción prefijada de fábrica**) |

> Para que el programador ejecute los eventos programados, debe permanecer en modo **AUTO**.

---

## D. Funciones Adicionales

### D.1 — Función de Cuenta Regresiva (Encendido Temporal)

Mantiene encendido un equipo durante un período determinado sin perder la programación habitual.

**Procedimiento:**
1. Presionar y mantener oprimida la tecla **Reloj**, luego presionar la tecla para ingresar a pantalla COUNTDOWN
2. Fijar las horas de retardo con la tecla **Hora**; fijar los minutos con la tecla **Minutos**
3. Rango: mínimo 1 minuto — máximo 9 horas 59 minutos
4. Presionar la tecla **Manual** para iniciar el conteo regresivo
5. Al finalizar el conteo, el equipo se apaga y el programador retorna a su programación habitual
6. Para detener el conteo: presionar **Manual**; para salir manualmente: presionar y mantener **Reloj** y luego **Manual**

### D.2 — Función Aleatoria (Simular Presencia)

Simula presencia de personas mediante encendido y apagado aleatorio entre las **06:00 PM y las 06:00 AM**.

**Requisito:** Tener eventos previamente programados entre esas horas.  
Los eventos ocurrirán con variaciones aleatorias de hasta **30 minutos** antes de los horarios programados.

**Activar:** Presionar simultáneamente las teclas y → aparece la letra **R** en pantalla.  
**Cancelar:** Repetir la combinación → desaparece la letra R.

### D.3 — Horario de Verano (DLST)

Para países donde se adelanta el reloj en temporada de verano:  
Presionar simultáneamente las teclas y → aparece **+1h** en pantalla (adelanta 1 hora).  
Para cancelar: repetir los mismos pasos.

---

## E. Reinicio del Programador

Oprimir el botón **R** para:
- Reiniciar el programador
- **Borrar toda la programación**
- Recuperar el estado original de fábrica

> **Advertencia:** Siempre presionar el botón R antes de programar por primera vez y cada vez que se reemplace la batería.

---

## Información de Seguridad

> Los cables deben quedar firmemente conectados. Si están flojos o en mal estado se produce una mala conexión y pueden dañar el programador y el equipo a controlar. **RIESGO DE CHOQUE ELÉCTRICO.** Antes de cualquier reparación, cambio de batería o mantenimiento, desconectar el suministro eléctrico al programador y al equipo.
