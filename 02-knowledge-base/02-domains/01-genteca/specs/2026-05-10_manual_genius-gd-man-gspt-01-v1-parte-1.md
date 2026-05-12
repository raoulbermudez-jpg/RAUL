---
title: "Manual de Instalación GSPT - Relé Digital para Protección de Bombas Sumergibles"
type: Technical
source: "GD-MAN-GSPT-01-V1.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GSPT"
version_status: "vigente"
date_processed: "2026-05-10"
---

# Manual de Instalación GSPT

## Descripción General

El GSPT es un Relé digital para Protección de Bombas Sumergibles que supervisa constantemente la Corriente del Motor y los principales parámetros eléctricos tales como Voltaje, Frecuencia, Factor de potencia, Potencia real, Potencia aparente y Consumo de energía, dando la protección más confiable contra Sobrecargas, Falla de fase, Fase invertida, Pérdida de fase, Desbalances y Arranques excesivos.

### Advertencias de Seguridad

**ALERTA:** Solo personal técnico calificado con conocimientos en relés de sobrecarga y de la maquinaria a proteger, debería realizar la instalación, arranque y mantenimiento del sistema. Hacer caso omiso podría resultar en lesiones a personas y/o daños a los equipos conectados.

**ALERTA:** Este producto puede activar al Contactor y hacer que arranque el motor de forma automática. El usuario debe tomar precauciones para evitar cualquier riesgo o daño.

**PELIGRO:** Desconecte el suministro de energía antes de instalar el GSPT. Hacer caso omiso puede resultar en lesiones severas incluso la muerte.

**PRECAUCIÓN:** El GSPT debe ser instalado en lugar accesible, libre de polvo, sucio, humedad y vibraciones. Que tenga suficiente espacio para la circulación de aire alrededor de su cubierta y fácil acceso a los controles de operación. SOLO PARA USO INTERIOR.

**AVISO:** Este producto ha sido diseñado para Ambiente Industrial Severo. De ser utilizado en Ambiente Residencial el usuario podría requerir algunas medidas en caso de que note algún ruido eléctrico inesperado en artefactos domésticos.

**ALERTA:** Errores en la conexión o la aplicación en ambientes fuera de los límites especificados del GSPT, pueden resultar en un mal funcionamiento, o daños en sus componentes.

## Partes y Piezas

### Vista Frontal

1. **Pantalla LCD:** Presenta información de mediciones, estados, configuraciones e historia, en texto y números.

2. **Indicadores luminosos (LED's):**
   - **FALLA:** Luz roja fija, indica apagado de salida, debido a falla.
   - **CONTROL:** Luz verde; intermitente indica temporizado de reconexión, fijo indica estado normal.

3. **Pulsador REARME:** Reanuda la operación después de parada, bajo modo de rearme manual.

4. **Pulsadores AJUSTE:** Introduce datos para ajustar distintas configuraciones.

5. **Pulsador SELECCIÓN:** Selecciona el parámetro o estado deseado para lectura y/o ajuste.

### Vista Posterior

6. **Ranura posterior:** Para montaje en riel simétrico.

7. **Sujetadores insertables:** Para montaje en superficies planas.

8. **Gancho de retención:** Para montaje en riel simétrico.

9. **Orificios con sensores de corriente:** Para pasar cables de alimentación al motor.

10. **Entradas de Voltaje de Línea:** L1, L2, L3.

11. **Contactos del Relé:**
    - 95-96 conectado: Disparado
    - 95-96 abierto: Normal
    - 97-98 abierto: Disparado
    - 97-98 conectado: Normal

12. **GIO PORT:** Puerto de comunicación.

13. **Cubierta plástica protectora:** Del puerto GIO PORT.

## Montaje

### Montaje sobre Riel Simétrico DIN

Coloque el GSPT en posición inclinada enganchando la ranura posterior con el riel. Luego empuje presionando el frente del GSPT hasta que haga CLICK.

### Montaje sobre Superficie Plana

**Instrucciones:**

a) Saque los dos (2) sujetadores insertables localizados en la parte posterior del GSPT. Luego inserte ambos sujetadores dentro de las ranuras verticales de la parte posterior del GSPT.

b) Coloque el GSPT sobre la superficie plana del panel y fijelo usando tornillos 3/16" x 1/2", empleando un destornillador adecuado.

**Recomendación:** Haga dos (2) agujeros de 5/32" de diámetro sobre la superficie del panel antes de instalar el GSPT.

## Dimensiones Generales

- Alto: 127 mm
- Ancho: 93 mm
- Profundidad: 112 mm (aproximadamente, según guía para superficie plana)

## Designación de Terminales

| Terminal | Descripción |
|----------|-------------|
| L1 | Entrada Voltaje (Fase R) |
| L2 | Entrada Voltaje (Fase S) |
| L3 | Entrada Voltaje (Fase T) |
| 95 | Contactos para Señalización Auxiliar |
| 96 | Contactos para Señalización Auxiliar |
| 97 | Contactos para Control de Contactor |
| 98 | Contactos para Control de Contactor |

## Diagrama Básico de Instalación

El GSPT se conecta:
- Entradas de voltaje (L1, L2, L3) antes del Contactor y su respectivo circuito de arranque
- Los tres cables del motor deben pasar por los tres orificios de sensores de corrientes
- Contactos del relé (95-96, 97-98) para control y señalización

**PRECAUCIÓN:** Verifique que el modelo GSPT seleccionado para instalar corresponda con el voltaje nominal de línea y rango de corriente del motor.

## Recomendaciones para Cableado

- Evite apretar excesivamente los tornillos M3 de los terminales durante la conexión. Torque máximo: 4.4 Ib-in (5.1 kg-cm).

- Pelar los aislantes de los cables a conectar entre 6 a 7 mm.

- Usar cables para terminales: entre AWG10 (4 mm²) y AWG18.

- El máximo tamaño de los cables del motor a pasar por orificios de sensores de corrientes será de: AWG 4 (11 mm).

- Conecte los terminales de Voltaje de Entrada L1L2L3 antes del Contactor y su respectivo circuito de arranque.

- Siempre pase los tres cables del motor por los tres orificios de sensores de corrientes. Dejar algún orificio sin cablear ocasionará falsas lecturas de desbalance.

## Operación

El GSPT constantemente supervisa valores de corriente del motor y parámetros de voltaje, frecuencia y potencia de la red. Cuando alguna condición de falla dañina ocurre, su salida se desactiva, manteniéndose así hasta que la falla desaparezca, las condiciones del sistema se hayan reestablecido y el motor se haya enfriado.

Dispone de:
- Un temporizador a la Conexión (Arranque)
- Un temporizador a la Desconexión por presencia de Falla

Estos están incorporados al GSPT para prevenir falsos disparos debido a las eventuales fluctuaciones de voltaje de la red.

### Función de Triple Falla

Si en alguna ocasión llegase a suceder tres (o más) fallas de corriente en un intervalo menor a treinta minutos, el GSPT desactivará permanentemente su salida, y solo se podrá restaurar la operación del sistema manualmente, oprimiendo el pulsador de REARME. Se recomienda verificar las causas de las tres fallas sucesivas.

### Características de Operación

El GSPT consta de:
- Pantalla LCD para indicar el estado de salida y de falla de parámetros: corriente, voltaje, desbalance, frecuencia, potencia, factor de potencia y consumo de energía
- Cuatro (4) botones pulsadores: uno de REARME, dos de AJUSTE y uno de SELECCIÓN, para ajustes de parámetros eléctricos de operación y protección
- Puerto de comunicaciones para lectura de datos por medio de sistemas computarizados (GIO PORT, Protocolo MODBUS RTU)
- Indicadores luminosos tipo LED's para señalizar fallas y el estado de operación del sistema

### Descripción de Indicadores Luminosos

| Indicador | Luz Continua | Luz Intermitente |
|-----------|--------------|------------------|
| Led Verde | Contactor conectado o habilitado (ON) | Temporizando (TC) |
| Led Rojo | Falla de voltaje o corriente (FALLA) | — |

## Desmontaje

### Desmontaje desde Riel Simétrico DIN

**PELIGRO:** Apague el interruptor de alimentación (Breaker) y desconecte todos los cables al GSPT antes de proceder a desmontarlo. Hacer caso omiso puede resultar en daños a los equipos o personas.

a) Usando un destornillador plano, hale hacia abajo el Gancho de Retención dispuesto en la parte inferior del GSPT.

b) Mediante el destornillador desplace el gancho a la posición abierta, saque el GSPT del Riel simétrico.

**Recomendaciones:** Hale suavemente y hacia abajo el gancho de retención unos 2 mm aproximadamente. Un movimiento brusco para sacar el gancho podría desprenderlo.

### Desmontaje desde Superficie Plana

a) Destornille ambos tornillos que fijan al GSPT a la superficie plana a través de los sujetadores insertables y luego saque el GSPT de dicha superficie.

## Guía Rápida de Programación - Software Versión 1.12

### Pantallas Principales

#### 1.1 Desconectado por MODBUS o Pantalla de Inicio
- Voltaje nominal: 220V (ejemplo)
- Muestra fase R, S, T

#### 1.2 Desconectado Bajo Modo Manual
- Estado: OFF MANUAL
- Voltaje: 220V

#### 1.3 Desconectado por 3era. Falla
- Estado: OFF 3RA FALLA

#### 1.4 Temporizado a la Conexión (TC)
- Estado: TC 15"

#### 1.5 Temporizado a la Conexión (TC) Continuado
- MIN OFF TC 40"

#### 1.6 TC por Subcarga
- TC 10"

#### 1.7 Bajo Voltaje (UV)
- UV 167V V12

#### 1.8 Sobre Voltaje (OV)
- OV 241V V31

#### 1.9 Desbalance de Voltaje (VUB)
- VUB 11%

#### 1.10 Variación de Frecuencia (FS)
- FS 63.6 Hz

#### 1.11 Pérdida de Fase (VSP)
- Detección de pérdida de fase

#### 1.12 Fase Invertida (PR)
- FASE INVERTIDA

#### 1.13 Porcentaje (%) de Calor Acumulado
- CALOR 50.4%

#### 1.14 Sobrecalentamiento (AD)
- CALOR EXCESIVO (AD)

#### 1.15 Relé Desviado
- RELE DESVIADO

### Parámetros de Configuración Default

- V NOMINAL: 280V (opciones: 220, etc.)
- BAJO VOLT.: 180V
- SOBRE VOLT.: 240%
- DESBALANCE: 10%
- FRECUENCIA: 102 Hz / FS: 10%
- TC MIN. OFF: 10 s
- TD: 30"
- GSPT: 208V / V1.08
- SUBCARGA: IN 40% / 900% / 10%
- I NOMINAL: 100A
- SOBRECARGA: 20%
- SOBRECAR.: 10%
- SUBCARGA NO
- 3RA FALLA: OFF / NO
- CLAVE INCORRECTA
- ARRANQUES/h: No
- MAX ARRANQUES/h: 15

### Mediciones Disponibles

- kW, kVA (Potencia)
- PF (Factor de Potencia)
- kWH (Consumo de energía)
- Hora y Fecha
- Histórico de Fallas

### Menú Principal de Ajustes

- **AJUSTE VOLTAJE**
- **AJUSTE CORRIENTE**
- **AJUSTE RELOJ HH**
- **MODO DE REARME** (AUTO/MANUAL)
- **CAMBIO DE CLAVE**
- **DIRECCION MODBUS**
- **BORRAR HISTORICO**
- **REINICIAR EQUIPO**

### Descripciones de Pantallas de Fallas

#### Sobre Voltaje / Bajo Voltaje (N° 1.7 y 1.8)
- Valores de Voltaje durante Falla
- Porcentaje (%) Desbalance Voltaje
- Duración de la Falla (minutos)
- Fases Involucradas en la Falla
- Tipo de Falla
- Valor Extremo en la Falla
- Valor Registrado de la Falla

#### Voltaje, Frecuencia y Calor (N° 1.9 al 1.12)
- Valores de Voltaje durante Falla
- Porcentaje (%) Desbalance Voltaje
- Descripción de la Falla
- Tipo de Falla
- Fase Involucrada en la Falla
- Porcentaje de Desbalance
- Porcentaje de Calor
- Valor Medido según la Pantalla

### Histórico de Fallas

El equipo registra:
- Fecha de la Falla
- Hora de la Falla
- Número de la Falla
- Duración de la Falla (minutos)
- Fase Involucrada en la Falla
- Tipo de Falla
- Valor Registrado de la Falla

### Funciones Especiales del Teclado

- Presione simultáneamente los botones AJUSTE y SELECCIÓN para entrar al menú (pantalla 7). Si el producto está protegido, introduzca la Clave.

- Presione simultáneamente los botones para activar la opción de Salida Rápida.

- Presione simultáneamente los botones para validar el Valor de Ajuste a seleccionar.

- Presione simultáneamente los botones para activar la Pantalla 0 de Inicio.

### Glosario de Abreviaturas

| Abreviatura | Significado |
|-------------|-------------|
| Sph | Arranque por Hora |
| 3F | Tercera Falla |
| BR | Relé Desviado |
| SM | Arranque Forzado |
| TEF | Falla de Energía |
| FS | Frecuencia |
| RL | Rotor Bloqueado |
| PF | Factor de Potencia |
| UC | Baja Corriente |
| OL | Sobre Corriente |
| VSP | Pérdida de Fase por Voltaje |
| CSP | Pérdida de Fase por Corriente |
| VUB | Desbalance de Voltaje |
| OV | Sobrevoltaje |
| CUB | Desbalance de Corriente |
| PROG. | Programación |
| T | Tiempo |
| HRS | Horas |
