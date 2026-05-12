---
title: "GUCT+ Manual de Instalación"
type: Technical
source: "GUCT+ c-CT GD-MAN8005-CO-V1.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GUCT+"
version_status: "historica"
date_processed: "2026-05-10"
---

# GUCT+ Manual de Instalación

## Descripción General

GUCT+ es un Relé (Relevador) electrónico para Protección y Control para Generadores, Transformadores y Motores que supervisa constantemente las corrientes del motor y voltajes de alimentación. Mediante algoritmos de modelaje térmico protege contra sobrecarga, subcarga y fallas de voltaje.

### Alertas de Seguridad

**ALERTA:** Solo personal técnico calificado con conocimientos en relevadores de sobrecarga y de la maquinaria a proteger, debería realizar la instalación, arranque y mantenimiento del sistema. Hacer caso omiso podría resultar en lesiones a personas y/o daños a los equipos conectados.

**AVISO:** Este producto ha sido diseñado para Ambiente Industrial Severo. De ser utilizado en Ambiente Residencial el usuario podría requerir algunas medidas en caso de que note algún ruido eléctrico inesperado en artefactos domésticos.

**ALERTA:** Este producto puede activar al Contactor y hacer que arranque el motor de forma automática. El usuario debe tomar precauciones para evitar cualquier riesgo o daño.

**ALERTA:** Errores en la conexión o la aplicación en ambientes fuera de los límites especificados del GUCT+, pueden resultar en un mal funcionamiento, o daños en sus componentes.

## Partes y Piezas

### Componentes Principales

1. **Pantalla de lectura - PANTALLA LCD:** Presenta información de mediciones, estados, configuraciones e historia, en texto y números.

2. **Indicadores luminosos (LED's):**
   - FALLA: Luz roja fija, indica apagado de salida, debido a falla.
   - CONTROL: Luz verde; intermitente indica temporizado de reconexión, fijo indica estado normal.

3. **Pulsador REARME:** Reanuda la operación después de parada, bajo modo de rearme manual.

4. **Pulsadores AJUSTE:** Introduce datos para ajustar distintas configuraciones.

5. **Pulsador SELECCIÓN:** Selecciona el parámetro o estado deseado para lectura y/o ajuste.

6. **Ranura posterior:** Para montaje en riel simétrico.

7. **Sujetadores insertables:** Para montaje en superficies planas.

8. **Gancho de retención:** Para montaje en riel simétrico.

9. **Orificios con sensores de corriente:** Para pasar cables de alimentación al motor.

10. **Entradas de Voltaje de Línea:** L1, L2, L3.

11. **Contactos del Relé:**
    - (95-96) y (97-98)
    - 95-96 conectado / 97-98 abierto: Disparado
    - 95-96 abierto / 97-98 conectado: Normal

12. **GIO PORT:** Puerto de comunicación.

13. **Cubierta plástica protectora:** Del puerto GIO PORT.

## Montaje

### Montaje sobre Riel Simétrico DIN

**PRECAUCIÓN:** GUCT+ debe ser instalado en lugar accesible, libre de polvo, sucio, humedad y vibraciones. Que tenga suficiente espacio para la circulación de aire alrededor de su cubierta y fácil acceso a los controles de operación.

**Instrucciones para Montaje Mecánico:**

Coloque el GUCT+ en posición inclinada enganchando la ranura posterior con el riel. Luego empuje presionando el GUCT+ hasta que haga CLICK.

### Montaje sobre Superficie Plana

**Instrucciones para Montaje Mecánico:**

a) Saque los dos (2) sujetadores insertables localizados en la parte posterior del GUCT+. Luego inserte ambos sujetadores dentro de las ranuras verticales de la parte posterior del GUCT+.

b) Coloque el GUCT+ sobre la superficie plana del panel y fijelo usando tornillos 3/16" x 1/2", empleando un destornillador (desarmador) adecuado.

**Recomendación para Montaje sobre Superficie Plana:** Haga dos (2) agujeros de 4mm (5/32") de diámetro sobre la superficie del panel antes de instalar el GUCT+.

## Dimensiones Generales

**Guía para Superficie Plana:**
- Altura: 92 mm
- Ancho: 92 mm
- Profundidad: variable según montaje

## Diagrama de Conexión

### Designación de Terminales

| TERMINAL | DESCRIPCIÓN |
|----------|-------------|
| L1 | Entrada Voltaje (Fase R) |
| L2 | Entrada Voltaje (Fase S) |
| L3 | Entrada Voltaje (Fase T) |
| 95, 96 | Contactos para Señalización Auxiliar |
| 97, 98 | Contactos para Control de Contactor |

**Tabla de Estados de Contactos:**

| Estado | 95-96 | 97-98 |
|--------|-------|-------|
| Disparado | Conectado | Abierto |
| Normal | Abierto | Conectado |

### Diagrama Básico de Instalación

Aplicable con los siguientes modelos:
- GUCT+20800S
- GUCT+48000S

**Componentes incluidos:**
- Contactor manejado desde Circuito de Control y Arranque
- Protección contra Cortocircuito
- Conexiones de Voltaje (L1, L2, L3)
- Circuito de Control y Arranque

### Recomendaciones para Cableado

- Evite apretar excesivamente los tornillos M3 de los terminales durante la conexión. Torque máximo: 5,1 Kgecm / 4,4 lb-in.
- Pelar los aislantes de los cables a conectar entre 6 a 7 mm.
- Usar cables para terminales: entre AWG 10 y AWG 18.
- El máximo tamaño de los cables del motor a pasar por orificios de sensores de corrientes será de: AWG 4.
- Conecte los terminales de Voltaje de Entrada L1, L2, L3 antes del Contactor y su respectivo circuito de arranque.
- Siempre pase los tres cables del motor por los tres orificios de sensores de corrientes. Dejar algún orificio sin cablear ocasionará falsas lecturas de desbalance.
- Fusibles Opcionales: 5A, 600V
- Cable AWG 14 recomendado

## Operación

GUCT+ constantemente supervisa valores de corriente, parámetros de voltaje, frecuencia, potencia de la red en Generadores, Transformadores y Motores. Cuando alguna condición de falla dañina ocurre, el GUCT+ desconectará al circuito arrancador del motor, manteniendo al motor apagado hasta que la falla eléctrica desaparezca y el motor se haya enfriado.

### Características de Operación

- Dispone de un temporizador a la Conexión (Arranque) y de un temporizador a la Desconexión por presencia de Falla, los cuales están incorporados al GUCT+ para prevenir falsos disparos debido a las eventuales fluctuaciones de voltaje de la red.
- Si en alguna ocasión llegase a suceder tres o más fallas de corriente en un intervalo menor a treinta minutos, el GUCT+ desactivará permanentemente su salida, y solo se podrá restaurar la operación del sistema manualmente, oprimiendo el pulsador de REARME. Se recomienda verificar las causas de las tres fallas sucesivas.
- Pantalla de Cristal Líquido (LCD) para indicar el estado de salida y de falla de parámetros tales como corriente, voltaje, desbalance, frecuencia, potencia, factor de potencia y consumo de energía.
- Cuatro (4) botones pulsadores: uno de REARME, dos de AJUSTE y uno de SELECCIÓN para ajustes de parámetros eléctricos de operación y protección.
- Puerto de comunicaciones para lectura de datos por medio de sistemas computarizados (GIO PORT, Protocolo MODBUS RTU).
- Indicadores luminosos tipo LED's para señalizar fallas y el estado de operación del sistema.

### Descripción de Fallas e Indicaciones Luminosas

| Estado | Luz Continua | Luz Intermitente |
|--------|--------------|------------------|
| Led Verde (ON) | Contactor conectado o habilitado | Temporizando (TC) |
| Led Rojo | Falla de voltaje o corriente (FALLA) | — |

## Instrucciones de Desmontaje

**PELIGRO:** Apague el interruptor de alimentación (Breaker) y desconecte todos los cables al GUCT+ antes de proceder a desmontarlo. Hacer caso omiso puede resultar en daños a los equipos o personas.

### Desmontaje (Riel simétrico DIN)

a) Usando un destornillador (desarmador) plano, hale hacia abajo el Gancho de Retención dispuesto en la parte inferior del GUCT+.

b) Mediante el destornillador (desarmador) desplace el gancho a la posición 2, saque el GUCT+ del Riel simétrico.

**Recomendaciones para el Desmontaje desde DIN Riel:** Hale suavemente y hacia abajo el gancho de retención unos 2mm aproximadamente. Un movimiento brusco para sacar el gancho podría desprenderlo.

### Desmontaje (Superficie Plana)

Desatornille (desarme) ambos tornillos que fijan al GUCT+, a la superficie plana a través de los sujetadores insertables y luego saque el GUCT+ de dicha superficie.

## Guía Rápida de Programación para GUCT+

**Versión de Software: 1.12**

### Pantallas de Estado del Relevador

**1.1 Desconectado por MODBUS**
- Estado: OFF
- Voltajes mostrados: 220V, 218V, 222V

**1.2 Desconectado por Prog. Horario**
- Estado: OFF PROG. HORARIO

**1.3 Desconectado Bajo Modo Manual**
- Estado: OFF MANUAL

**1.4 Desconectado por 3era. Falla**
- Estado: OFF 3RA FALLA

**1.5 Temporizado a la Conexión (TC)**
- Estado: TC 15"

**1.6 TC por Subcarga**
- Estado: UC TC

**1.7 Bajo Voltaje (UV)**
- Ejemplo: 167V, 169V, 168V
- Indicación: 03

**1.8 Sobre Voltaje (OV)**
- Ejemplo: 240V, 239V, 241V
- Indicación: 03

**1.9 Desbalance de Voltaje (VUB)**
- Ejemplo: 221V, 267V, 264V
- Desbalance: 11%

**1.10 Variación de Frecuencia (FS)**
- Ejemplo: 63.6 Hz

**1.11 Pérdida de Fase (VSP)**
- Ejemplo: 107V, 105V, 214V
- Desbalance: 50%

**1.12 Fase Invertida (PR)**
- Ejemplo: 220V, 222V, 218V
- Indicación: 02

**1.13 Porcentaje (%) de Calor Acumulado**
- Ejemplo: 50.4%

**1.14 Sobrecalentamiento**
- Estado: CALOR EXCESIVO

### Pantalla de Inicio (0.1)

- Modelo: GUCT 208V 4A
- Versión: 2008 v1.14 SP

### Pantalla Principal (2)

Muestra:
- Voltajes: V12, V23, V31
- VUB (Desbalance de Voltaje)
- Corrientes: I1, I2, I3
- CUB (Desbalance de Corriente)

### Medición kW-kVA-PF-kWH (2)

- Potencia Aparente: 110.0 kVA
- Factor de Potencia: 0.80 PF
- Potencia Real: 100.0 kW
- Consumo: 290000 kWH

### Histórico de Fallas (3)

Registra:
- Fecha de la Falla
- Hora de la Falla
- Número de la Falla
- Tipo de Falla
- Valor Registrado de la Falla
- Valor Extremo en la Falla
- Fase Involucrada en la Falla
- Duración de la Falla (minutos)

### Contador Hrs. del Motor (4)

- Hora actual: 14:11
- Total de horas: 000025
- Fecha: 02/06/05

### Temperatura del Motor, Frecuencia y Modo REARME (5)

- Frecuencia: 60.0 Hz
- Modo: AUTO

### Menú Principal de Ajustes (7)

- AJUSTE VOLTAJE
- AJUSTE CORRIENTE
- AJUSTE RELOJ
- PROG HORARIO
- MODO DE REARME
- CAMBIO DE CLAVE
- DIRECCIÓN MODBUS
- BORRAR HISTÓRICO
- REINICIAR EQUIPO
- SALIR

### Submenu de Ajuste de Voltaje (7.1)

- BAJO VOLTAJE: 180V
- SOBRE VOLTAJE: 242V
- DESBALANCE: 10%
- FRECUENCIA: 60Hz
- FS: 10%
- TD: 30"
- TC: 600"
- SALIR

### Submenu de Ajuste de Corriente (7.2)

**Tipo de Subcarga (7.2.1):**
- NOMINAL: SELECCIONAR
- CLASE MOTOR: NFPA
- SOBRECARGA
- SUBCARGA
- ALTA INERCIA
- BLOQUEO: 3"
- 3RA FALLA: OFF
- SALIR

**Ajuste disponible en modelos para CT externos (7.2.1.1):**
- IN: 40%

**Factor de Subcarga (7.2.1.2):**
- SUBCARGA PF: 0.5

**Tipo de Arranque (7.2.2):**
- T. DE ARRANQUE: 20"
- SALIR

### Menú de Ajuste de Reloj (7.3)

- Hora: 13:50
- Fecha: 07/31/03

### Menú de Programación Horaria (7.4)

- LMMJVSDF: ON 00:00
- ST: 01/60
- OFF: 00:00
- AJUSTE EVENTOS
- AJUSTE FERIADOS
- SALIR

**Ajuste de Feriados (7.5):**
- FERIADO
- DÍA: 1
- MES: 1
- Fecha ejemplo: 01/20

### Modo de Rearme (7.6)

- AUTO
- MANUAL

### Cambio de Clave (7.7)

- Protección con clave numérica

### Dirección MODBUS (7.8)

- DIRECCIÓN MODBUS: 001
- Ingreso con clave

### Borrar Histórico (7.9)

- BORRANDO...
- Opción para forzar rearme arranque: SI/NO

### Reiniciar Equipo (1.9.1)

- RECOBRAR VALORES DE FÁBRICA: SI/NO
- RECOBRANDO VALORES

### Configuración de Botones

**Pulsadores:**
- AJUSTE
- SELECCIÓN

### Funciones Especiales del Teclado

- Presione simultáneamente los botones para entrar al menú (panel 7). Si el producto está protegido, introduzca la Clave.
- Presione simultáneamente los botones AD para activar la opción de Salida Rápida.
- Para validar el Valor de Ajuste a seleccionar.
- Presione simultáneamente los botones para activar la Pantalla 0 de Inicio.

## Descripción de Pantallas de Fallas

### Sobre Voltaje / Bajo Voltaje (N° 1.7 y 1.8)

Muestra:
- Valores de Voltaje durante Falla
- Número de la Falla
- Porcentaje (%) Desbalance Voltaje
- Duración de la Falla (minutos)
- Fase Involucrada en la Falla
- Fases Involucradas en la Falla
- Tipo de Falla
- Valor Registrado de la Falla
- Valor Extremo en la Falla

### Voltaje, Frecuencia y Calor (N° 1.9 al 1.12)

Muestra:
- Valores de Voltaje durante Falla
- Porcentaje (%) Desbalance Voltaje
- Fase Involucrada en la Falla
- Descripción de la Falla
- Tipo de Falla
- Porcentaje de Desbalance
- Valor Medido según la Pantalla

## Glosario de Abreviaturas

| ABREVIATURA | SIGNIFICADO |
|------------|-------------|
| OL | SOBRE CORRIENTE |
| UC | BAJA CORRIENTE |
| CSP | PÉRDIDA DE FASE POR CORRIENTE |
| CUB | DESBALANCE DE CORRIENTE |
| FS | FRECUENCIA |
| PR | FASE INVERTIDA |
| VSP | PÉRDIDA DE FASE POR VOLTAJE |
| RL | ROTOR BLOQUEADO |
| VUB | DESBALANCE DE VOLTAJE |
| UV | BAJO VOLTAJE |
| OV | SOBREVOLTAJE |
| V | VOLTAJE |
| I | CORRIENTE |
| PF | FACTOR DE POTENCIA |
| TC | TEMPORIZADO A LA CONEXIÓN |
| TD | TEMPORIZADO A LA DESCONEXIÓN |
| SM | ARRANQUE FORZADO |
| TEF | FALLA DE ENERGÍA |
| PROG. | PROGRAMACIÓN |

---

*Generación de Tecnología*
