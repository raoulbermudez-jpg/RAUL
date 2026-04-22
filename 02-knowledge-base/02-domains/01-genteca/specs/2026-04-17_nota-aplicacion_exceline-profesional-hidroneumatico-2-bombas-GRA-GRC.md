# Nota de Aplicación — Sistema Hidroneumático con Alternancia de Dos Bombas Trifásicas por Medio de Dos Presostatos

**Producto(s):** Relé Alternador GRA-MV + Relé Octal GRC-8  
**Línea:** Exceline Profesional  
**Tipo de documento:** Nota de Aplicación  
**Número de referencia:** 10-GD-NA  
**Voltaje de la instalación:** 220 V~  
**Grado de dificultad:** Medio  
**Fabricante:** Gente, Generación de Tecnología, C.A.

---

## Descripción de la Aplicación

Los sistemas hidroneumáticos son utilizados para impulsar agua a presión desde un tanque hasta los puntos de edificaciones donde es requerido el servicio. Las bombas succionan el agua del tanque de almacenamiento y la impulsan hacia el tanque presurizado, de acuerdo a la señal de control de los presostatos.

La gran mayoría de los sistemas hidroneumáticos poseen dos o más bombas que operan en forma alternada, lo que permite dosificar su utilización y prolongar su vida útil. Por este motivo se hace necesaria la utilización de un relé alternador **GRA-MV**.

Se incluye además un relé octal **GRC-8** que permite la activación de ambas bombas de forma simultánea, en caso de que la presión no sea suficiente con una sola bomba.

---

## Lista de Equipos

| Equipo | Modelo | Función |
|--------|--------|---------|
| Relé Alternador | GRA-MV | Alternancia de bombas |
| Relé Octal | GRC-8-220VAC | Activación simultánea de ambas bombas |

---

## Equipos Involucrados

### GRA-MV — Relé Alternador

- Multivoltaje: 120/220 V~
- Cada vez que el dispositivo detecta un cambio de cerrado a abierto entre sus entradas 3 y 2, genera una actuación sobre los contactos de su etapa de salida, cambiando su posición.
- Compacto y fácil de instalar.

### GRC-8 — Relé Octal

- Relé electromecánico de propósito general activado por bobina.
- Base de conexión octal que facilita el montaje y desmontaje.
- Botón de prueba manual.
- Indicador mecánico de cierre.

---

## Modos de Funcionamiento

El selector manual permite indicar el modo de funcionamiento deseado:

| Posición del Selector | Modo |
|-----------------------|------|
| **Posición 1** | Bomba 1 encendida / Bomba 2 en mantenimiento. La bomba 1 permanecerá encendida siempre que el presostato 1 lo permita. La bomba 2 no se activa bajo ninguna circunstancia. |
| **Posición 2** | Funcionamiento automático (Relé alternador). Ambas bombas funcionan de forma alternada según la señal del presostato 1. Si una sola bomba no es suficiente y la presión sigue cayendo, se cierra el presostato 2 y el relé octal activa ambas bombas simultáneamente hasta alcanzar el nivel de presión requerido. |
| **Posición 3** | Bomba 2 encendida / Bomba 1 en mantenimiento. La bomba 2 permanecerá encendida siempre que el presostato 1 lo permita. La bomba 1 no se activa bajo ninguna circunstancia. |

---

## Nota Importante sobre Configuración de Presostatos

> El presostato 2 **solo** se debe activar si la presión cae por debajo del límite inferior del presostato 1, y debe desactivarse **primero que el presostato 1** cuando la presión se eleve. Es importante configurar los límites de presión de ambos presostatos de forma correcta para garantizar el funcionamiento adecuado.

---

## Diagramas

### Diagrama de Conexión del Sistema Hidroneumático con 2 Bombas (Página 2)

**Tipo:** Diagrama de conexión de control monofásico — Unifilar de control  
**Ubicación en PDF original:** Página 2

![Diagrama hidroneumático 2 bombas GRA-GRC](../../../Assets/Diagrams/Trifilares/GRA-GRC-hidroneumatico-2-bombas-diagrama-conexion-p2.png)

**Componentes del circuito:**

| Componente | Función en el circuito |
|------------|----------------------|
| Interruptor (220 V / 60 Hz) | Alimentación principal del circuito de control |
| Selector (3 posiciones) | Selección manual del modo de operación |
| Presostato 1 | Control principal de nivel de presión. Detecta variación de cerrado a abierto para activar el alternador |
| Presostato 2 | Control secundario de nivel de presión. Activa el relé octal cuando la presión cae por debajo del límite inferior del presostato 1 |
| GRA-MV (Relé Alternador) — terminales 1,2,3,4 / 5,6,7,8 | Alterna el arranque entre Contactor Bomba 1 y Contactor Bomba 2 |
| GRC-8-220VAC (Relé Octal) — terminales 1 al 8 | Activa simultáneamente ambos contactores cuando el presostato 2 se cierra |
| Contactor Bomba 1 | Energiza Motor Bomba Monofásica 1 |
| Contactor Bomba 2 | Energiza Motor Bomba Monofásica 2 |
| Bomba Monofásica 1 (M) | Bomba hidráulica 1 |
| Bomba Monofásica 2 (M) | Bomba hidráulica 2 |

**Descripción del circuito:**

1. La alimentación de 220 V / 60 Hz pasa por el interruptor principal.
2. El selector de 3 posiciones determina el modo de operación.
3. En modo automático (posición 2), el Presostato 1 controla la entrada del GRA-MV (entre terminales 3 y 2).
4. Cada cambio de estado (cerrado → abierto) del Presostato 1 hace conmutar los contactos de salida del GRA-MV, alternando entre Contactor Bomba 1 y Contactor Bomba 2.
5. Si la presión sigue bajando, el Presostato 2 se cierra y activa la bobina del GRC-8-220VAC.
6. El GRC-8 cierra simultáneamente los contactos hacia ambos contactores, arrancando las dos bombas al mismo tiempo.
7. Al recuperar la presión, el Presostato 2 se abre primero, el GRC-8 se desactiva, y ambas bombas quedan nuevamente bajo control del GRA-MV.

**Notas de cableado:**
- El cableado del diagrama muestra sistema monofásico a 220 V / 60 Hz.
- Las bombas indicadas son monofásicas, aunque el título de la nota menciona "bombas trifásicas" — el diagrama presentado en la página 2 muestra conexión monofásica. Para bombas trifásicas se requerirían contactores y protección de motor trifásica adicional.
- El relé GRC-8 se alimenta con bobina a 220 VAC (modelo GRC-8-220VAC).
