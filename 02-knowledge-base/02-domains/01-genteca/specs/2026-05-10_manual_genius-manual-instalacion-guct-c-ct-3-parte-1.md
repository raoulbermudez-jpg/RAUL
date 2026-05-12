---
title: "Manual de Instalación GUCT+ con CT Externo"
type: Technical
source: "Manual Instalacion GUCT+ c-CT (3).pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GUCT+"
version_status: "historica"
date_processed: "2026-05-10"
---

# Manual de Instalación GUCT+

## Descripción General

GUCT+ es un Relé (Relevador) electrónico para Protección y Control para Generadores, Transformadores y Motores que supervisa constantemente las corrientes del motor y voltajes de alimentación. Mediante algoritmos de modelaje térmico protege contra sobrecarga, subcarga y fallas de voltaje.

## Alertas y Avisos Importantes

**ALERTA:** Solo personal técnico calificado con conocimientos en relevadores de sobrecarga y de la maquinaria a proteger, debería realizar la instalación, arranque y mantenimiento del sistema. Hacer caso omiso podría resultar en lesiones a personas y/o daños a los equipos conectados.

**AVISO:** Este producto ha sido diseñado para Ambiente Industrial Severo. De ser utilizado en Ambiente Residencial el usuario podría requerir algunas medidas en caso de que note algún ruido eléctrico inesperado en artefactos domésticos.

**ALERTA:** Este producto puede activar al Contactor y hacer que arranque el motor de forma automática. El usuario debe tomar precauciones para evitar cualquier riesgo o daño.

**ALERTA:** Errores en la conexión o la aplicación en ambientes fuera de los límites especificados del GUCT+, pueden resultar en un mal funcionamiento, o daños en sus componentes.

## Partes y Piezas

1. **Pantalla de lectura (LCD):** Presenta información de mediciones, estados, configuraciones e historia, en texto y números.

2. **Indicadores luminosos (LED's):**
   - FALLA: Luz roja fija, indica apagado de salida debido a falla.
   - CONTROL: Luz verde; intermitente indica temporizado de reconexión, fijo indica estado normal.

3. **Pulsador REARME:** Reanuda la operación después de parada, bajo modo de rearme manual.

4. **Pulsadores AJUSTE:** Introduce datos para ajustar distintas configuraciones.

5. **Pulsador SELECCIÓN:** Selecciona el parámetro o estado deseado para lectura y/o ajuste.

6. **Ranura posterior:** Para montaje en riel simétrico.

7. **Sujetadores insertables:** Para montaje en superficies planas.

8. **Gancho de retención:** Para montaje en riel simétrico.

9. **Orificios con sensores de corriente:** Para pasar cables de alimentación al motor.

10. **Entradas de Voltaje de Línea:** L1, L2, L3.

11. **Contactos del Relé:** (95-96) y (97-98).
    - 95-96 conectado / 95-96 abierto: Disparado / Normal
    - 97-98 abierto / 97-98 conectado

12. **GIO PORT:** Puerto de comunicación.

13. **Cubierta plástica protectora:** Del puerto GIO PORT.

## Montaje sobre Riel Simétrico DIN

**PRECAUCIÓN:** GUCT+ debe ser instalado en lugar accesible, libre de polvo, sucio, humedad y vibraciones. Que tenga suficiente espacio para la circulación de aire alrededor de su cubierta y fácil acceso a los controles de operación.

### Instrucciones para Montaje Mecánico

Coloque el GUCT+ en posición inclinada enganchando la ranura posterior con el riel. Luego empuje presionando el GUCT+ hasta que haga CLICK.

## Montaje sobre Superficie Plana

### Instrucciones para Montaje Mecánico

a) Saque los dos (2) sujetadores insertables localizados en la parte posterior del GUCT+. Luego inserte ambos sujetadores dentro de las ranuras verticales de la parte posterior del GUCT+.

b) Coloque el GUCT+ sobre la superficie plana del panel y fijelo usando tornillos 3/16" x 1/2", empleando un destornillador adecuado.

**Recomendación para Montaje sobre Superficie Plana:** Haga dos (2) agujeros de 4mm (5/32") de diámetro sobre la superficie del panel antes de instalar el GUCT+.

## Dimensiones Generales

- Altura: 92 mm
- Ancho: incluye orificios de 4mm (5/32") para montaje en superficie plana

## Diagrama de Conexión

**PELIGRO:** Desconecte el suministro de energía antes de instalar el GUCT+. Hacer caso omiso puede resultar en lesiones severas incluso la muerte.

**PRECAUCIÓN:** Verifique que el modelo GUCT+ seleccionado para instalar corresponda con el voltaje nominal de línea y rango de corriente del motor.

### Designación de Terminales

| TERMINAL | DESCRIPCIÓN |
|----------|-------------|
| L1 | Entrada Voltaje (Fase R) |
| L2 | Entrada Voltaje (Fase S) |
| L3 | Entrada Voltaje (Fase T) |
| 95 | Contactos para Señalización Auxiliar |
| 96 | Contactos para Señalización Auxiliar |
| 97 | Contactos para Control de Contactor |
| 98 | Contactos para Control de Contactor |

**Estados de Contactos:**
- 95-96 Conectado \ Disparado
- 97-98 Abierto \ Normal
- 95-96 Abierto \ Normal
- 97-98 Conectado

### Diagrama Básico de Instalación

Aplicable con los siguientes modelos:
- GUCT+20800S
- GUCT+48000S

El diagrama incluye:
- Protección contra cortocircuito
- Contactor manejado desde Circuito de control y Arranque
- Entradas L1, L2, L3
- Cable AWG 14
- Fusibles opcionales: 5A, 600V

### Recomendaciones para Cableado

- Evite apretar excesivamente los tornillos M3 de los terminales durante la conexión. Torque máximo: 5,1 Kgecm / 4,4 lb-in.
- Pelar los aislantes de los cables a conectar entre 6 a 7 mm.
- Usar cables para terminales: entre AWG10 y AWG18.
- El máximo tamaño de los cables del motor a pasar por orificios de sensores de corrientes será de: AWG 4.
- Conecte los terminales de Voltaje de Entrada L1L2L3 antes del Contactor y su respectivo circuito de arranque.
- Siempre pase los tres cables del motor por los tres orificios de sensores de corrientes. Dejar algún orificio sin cablear ocasionará falsas lecturas de desbalance.

## Operación

GUCT+ constantemente supervisa valores de corriente, parámetros de voltaje, frecuencia, potencia de la red en Generadores, Transformadores y Motores. Cuando alguna condición de falla dañina ocurre, el GUCT+ desconectará al circuito arrancador del motor, manteniendo al motor apagado hasta que la falla eléctrica desaparezca y el motor se haya enfriado.

El dispositivo dispone de:
- Temporizador a la Conexión (Arranque)
- Temporizador a la Desconexión por presencia de Falla

Estos están incorporados al GUCT+ para prevenir falsos disparos debido a las eventuales fluctuaciones de voltaje de la red.

Si en alguna ocasión llegase a suceder tres o más fallas de corriente en un intervalo menor a treinta minutos, el GUCT+ desactivará permanentemente su salida, y solo se podrá restaurar la operación del sistema manualmente, oprimiendo el pulsador de REARME. (Se recomienda verificar las causas de las tres fallas sucesivas).

### Características del GUCT+

GUCT+ consta de:
- Pantalla de Cristal Líquido (LCD) para indicar el estado de salida y de falla de parámetros tales como corriente, voltaje, desbalance, frecuencia, potencia, factor de potencia y consumo de energía
- Cuatro (4) botones pulsadores: uno de REARME, dos de AJUSTE y uno de SELECCIÓN para ajustes de parámetros eléctricos de operación y protección
- Puerto de comunicaciones para lectura de datos por medio de sistemas computarizados (GIO PORT, Protocolo MODBUS RTU)
- Indicadores luminosos tipo LED's para señalizar fallas y el estado de operación del sistema

### Descripción de Fallas y sus Indicaciones Luminosas

| Luz | Estado |
|-----|--------|
| Led Verde (ON) | Contactor conectado o habilitado |
| Led Verde (Intermitente) | Temporizando (TC) |
| Led Rojo | Falla de voltaje o corriente (FALLA) |

## Instrucciones de Desmontaje

**PELIGRO:** Apague el interruptor de alimentación (Breaker) y desconecte todos los cables al GUCT+ antes de proceder a desmontarlo. Hacer caso omiso puede resultar en daños a los equipos o personas.

### Desmontaje (Riel Simétrico DIN)

a) Usando un destornillador plano, hale hacia abajo el Gancho de Retención dispuesto en la parte inferior del GUCT+.

b) Mediante el destornillador desplace el gancho a la posición 2 y saque el GUCT+ del Riel simétrico.

**Recomendaciones para el Desmontaje desde DIN Riel:**
Hale suavemente y hacia abajo el gancho de retención unos 2mm aproximadamente. Un movimiento brusco para sacar el gancho podría desprenderlo.

### Desmontaje (Superficie Plana)

Desatornille ambos tornillos que fijan al GUCT+, a la superficie plana a través de los sujetadores insertables y luego saque el GUCT+ de dicha superficie.

## Guía Rápida de Programación para GUCT+

Versión de Software: 1.12

### Pantallas de Estado del Relevador

**0. Pantalla de Inicio**
- Información: GUCT 208V 4A / 200S v1.14 SP / NED

**1. Pantallas de Estado:**

1.1 - Desconectado por MODBUS (OFF MODBUS)
1.2 - Desconectado por Prog. Horario (OFF PROG.HORARIO)
1.3 - Desconectado Bajo Modo Manual (OFF MANUAL)
1.4 - Desconectado por 3era. Falla (OFF 3RA FALLA)
1.5 - Temporizado a la Conexión (TC)
1.6 - TC por Subcarga
1.7 - Bajo Voltaje (UV)
1.8 - Sobre Voltaje (OV)
1.9 - Desbalance de Voltaje (VUB)
1.10 - Variación de Frecuencia (FS)
1.11 - Pérdida de Fase (VSP)
1.12 - Fase Invertida (PR)
1.13 - Porcentaje (%) de Calor Acumulado
1.14 - Sobrecalentamiento

**2. Pantalla Principal**
- Medición de voltajes (V12, V23, V31)
- Desbalance de voltaje (VUB)
- Corrientes (I1, I2, I3)
- Desbalance de corriente (CUB)

**2 bis. Medición kW-kVA-PF-kWH**
- Potencia aparente (kVA)
- Potencia activa (kW)
- Factor de potencia (PF)
- Consumo de energía (kWH)

**3. Histórico de Fallas**
- Fecha y hora de la falla
- Tipo de falla
- Valores registrados

**4. Contador Horas del Motor**
- Total de horas
- Fecha de registro

**5. Temperatura del Motor, Frecuencia y Modo REARME**
- Frecuencia (Hz)
- Modo de rearme (AUTO/MANUAL)

### Menú Principal de Ajustes (7)

- AJUSTE VOLTAJE
- AJUSTE CORRIENTE
- AJUSTE RELOJ
- PROG HORARIO
- MODO DE REARME
- CAMBIO DE CLAVE
- DIRECCION MODBUS
- BORRAR HISTORICO
- REINICIAR EQUIPO
- SALIR

### Ajuste de Voltaje (7.1)

- Bajo Voltaje: 180V
- Sobre Voltaje: 242V
- Desbalance: 10%
- Frecuencia: 60Hz
- FS (Variación de Frecuencia): 10%
- TD (Temporizado a la Desconexión): 30"
- TC (Temporizado a la Conexión): 600"

### Ajuste de Corriente (7.2)

**7.2.1 - Tipo de Subcarga y Parámetros:**
- Subcarga: 600"
- TC Subcarga: 10"

**7.2.1.1 - Nominal:**
- Clase Motor: Estándar
- Subcarga IN: 40%

**7.2.1.2 - Parámetros de Subcarga:**
- Subcarga PF: 0.5

**7.2.2 - Configuración de Sobrecarga y Subcarga:**
- Nominal
- Clase Motor
- Sobrecarga
- Subcarga
- Alta Inercia
- Bloqueo: 3"
- 3RA FALLA: OFF

**7.3 - T. de Arranque:** 20"

### Ajuste del Reloj (7.4)

**7.4.1:**
- Hora: 13:50
- Fecha: 07/31/03

### Programación Horaria (7.4)

**7.4:**
- LMMJVSDF
- ON 00:00
- OFF 00:00
- St 01/60

### Modo de Rearme (7.5-7.6)

- AUTO
- MANUAL

### Cambio de Clave (7.7)

- Ingrese Clave: 0000

### Dirección MODBUS (7.8)

- Dirección: 001
- Ingrese Clave: 0000

### Funciones Especiales del Teclado

Presione simultáneamente los botones (AD) para:
- Entrar al menú (panel 7). Si el producto está protegido, introduzca la Clave.
- Activar la opción de Salida Rápida.
- Validar el Valor de Ajuste a seleccionar.

Presione simultáneamente los botones para activar la Pantalla 0 de Inicio.

## Glosario de Abreviaturas

| ABREVIATURA | DESCRIPCIÓN |
|-------------|------------|
| OL | Sobre Corriente |
| uc | Baja Corriente |
| CSP | Pérdida de Fase por Corriente |
| CUB | Desbalance de Corriente |
| FS | Frecuencia |
| PR | Fase Invertida |
| VSP | Pérdida de Fase por Voltaje |
| RL | Rotor Bloqueado |
| VUB | Desbalance de Voltaje |
| UV | Bajo Voltaje |
| OV | Sobrevoltaje |
| M | Voltaje |
| I | Corriente |
| PF | Factor de Potencia |
| TC | Temporizador a la Conexión |
| TD | Temporizador a la Desconexión |
| SM | Arranque Forzado |
| TEF | Falla de Energía |
| PROG | Programación |

## Descripción de Pantallas de Fallas

### Sobre Voltaje / Bajo Voltaje (Nº 1.7 y 1.8)
- Valores de voltaje durante falla
- Porcentaje (%) de desbalance de voltaje
- Duración de la falla (minutos)
- Fase involucrada en la falla
- Tipo de falla
- Valor registrado de la falla
- Valor extremo en la falla

### Voltaje, Frecuencia y Calor (Nº 1.9 al 1.12)
- Valores de voltaje durante falla
- Porcentaje (%) de desbalance de voltaje
- Descripción de la falla
- Fase involucrada en la falla
- Tipo de falla
- Porcentaje de desbalance
- Valor medido según la pantalla

### Tipos de Falla

- **UV:** Bajo Voltaje
- **OV:** Sobrevoltaje
- **VUB:** Desbalance de Voltaje
- **FS:** Variación de Frecuencia
- **VSP:** Pérdida de Fase por Voltaje

### Histórico de Fallas

Cada registro contiene:
- Número de la falla
- Fecha de la falla
- Hora de la falla
- Tipo de falla
- Valor registrado de la falla
- Fase involucrada en la falla
- Duración de la falla
