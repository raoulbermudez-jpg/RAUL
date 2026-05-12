---
title: "Manual de Instalación GSPT"
type: Technical
source: "I_GSPT.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GSPT"
version_status: "vigente"
date_processed: "2026-05-10"
---

# Manual de Instalación GSPT

## Descripción General

El GSPT es un Relé digital para Protección de Bombas Sumergibles que supervisa constantemente la Corriente del Motor y los principales parámetros eléctricos tales como Voltaje, Frecuencia, Factor de potencia, Potencia real, Potencia aparente y Consumo de energía, dando la protección más confiable contra Sobrecargas, Falla de fase, Fase invertida, Pérdida de fase, Desbalances, Arranques excesivos.

**ALERTA:** Solo personal técnico calificado con conocimientos en relés de sobrecarga y de la maquinaria a proteger, debería realizar la instalación, arranque y mantenimiento del sistema. Hacer caso omiso podría resultar en lesiones a personas y/o daños a los equipos conectados.

**ALERTA:** Este producto puede activar al Contactor y hacer que arranque el motor de forma automática. El usuario debe tomar precauciones para evitar cualquier riesgo o daño.

## Partes y Piezas

### Componentes Frontal y Posterior

- **Pantalla LCD:** Presenta información de mediciones, estados, configuraciones e historia, en texto y números.
- **Indicadores luminosos (LED's):**
  - **FALLA:** Luz roja fija, indica apagado de salida, debido a falla.
  - **CONTROL:** Luz verde; intermitente indica temporizado de reconexión, fijo indica estado normal.
- **Pulsador REARME:** Reanuda la operación después de parada, bajo modo de rearme manual.
- **Pulsadores AJUSTE:** Introduce datos para ajustar distintas configuraciones.
- **Pulsador SELECCIÓN:** Selecciona el parámetro o estado deseado para lectura y/o ajuste.
- **Ranura posterior:** Para montaje en riel simétrico.
- **Sujetadores insertables:** Para montaje en superficies planas.
- **Gancho de retención:** Para montaje en riel simétrico.
- **Orificios con sensores de corriente:** Para pasar cables de alimentación al motor.
- **Entradas de Voltaje de Línea (L1 L2 L3):** Conexiones de voltaje.
- **Contactos del Relé (95-96) y (97-98):**
  - 95-96 conectado / 95-96 abierto: Disparado / Normal
  - 97-98 abierto / 97-98 conectado: Estado de operación
- **GIO PORT:** Puerto de comunicación.
- **Cubierta plástica protectora:** Del puerto GIO PORT.

## Montaje

### Montaje sobre Riel Simétrico DIN

**PRECAUCIÓN:** El GSPT debe ser instalado en lugar accesible, libre de polvo, suciedad, humedad y vibraciones. Que tenga suficiente espacio para la circulación de aire alrededor de su cubierta y fácil acceso a los controles de operación. SOLO PARA USO INTERIOR.

**Instrucciones para Montaje Mecánico:**

1. Coloque el GSPT en posición inclinada enganchando la ranura posterior con el riel.
2. Luego empuje presionando el frente del GSPT hasta que haga CLICK.

**AVISO:** Este producto ha sido diseñado para Ambiente Industrial Severo. De ser utilizado en Ambiente Residencial el usuario podría requerir algunas medidas en caso de que note algún ruido eléctrico inesperado en artefactos domésticos.

**ALERTA:** Errores en la conexión o la aplicación en ambientes fuera de los límites especificados del GSPT, pueden resultar en un mal funcionamiento, o daños en sus componentes.

### Montaje sobre Superficie Plana

**Instrucciones para Montaje Mecánico:**

1. Saque los dos (2) sujetadores insertables localizados en la parte posterior del GSPT.
2. Luego inserte ambos sujetadores dentro de las ranuras verticales de la parte posterior del GSPT.
3. Coloque el GSPT sobre la superficie plana del panel y fijelo usando tornillos 3/16" x 1/2", empleando un destornillador adecuado.

**Recomendación para Montaje sobre Superficie Plana:** Haga dos (2) agujeros de 5/32" de diámetro sobre la superficie del panel antes de instalar el GSPT.

## Dimensiones Generales

**Guía para Superficie Plana:** Proporciona las medidas necesarias para preparar la instalación en superficies planas.

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

**Estados de Contactos:**
- 95-96 Conectado / 97-98 Abierto: Disparado
- 95-96 Abierto / 97-98 Conectado: Normal

## Diagrama Básico de Instalación

**PELIGRO:** Desconecte el suministro de energía antes de instalar el GSPT. Hacer caso omiso puede resultar en lesiones severas incluso la muerte.

**PRECAUCIÓN:** Verifique que el modelo GSPT seleccionado para instalar corresponda con el voltaje nominal de línea y rango de corriente del motor.

El diagrama incluye:
- Interruptor o Breaker
- Fusibles (Opcionales): 5A, 600V
- Contactor con Bobina
- Conexiones de Entrada de Voltaje (L1, L2, L3)
- Sensor de Corriente
- Motor de Bomba Sumergible
- Luz Piloto
- Alarma Opcional

## Recomendaciones para Cableado

- Evite apretar excesivamente los tornillos M3 de los terminales durante la conexión. Torque máx: 4.4 lb-in (5.1 kg-cm).
- Pelar los aislantes de los cables a conectar entre 6 a 7 mm.
- Usar cables para terminales: entre AWG10 (4mm²) y AWG18.
- El máximo tamaño de los cables del motor a pasar por orificios de sensores de corrientes será de: AWG 4 (11mm).
- Conecte los terminales de Voltaje de Entrada L1L2L3 antes del Contactor y su respectivo circuito de arranque.
- Siempre pase los tres cables del motor por los tres orificios de sensores de corrientes. Dejar algún orificio sin cablear ocasionará falsas lecturas de desbalance.

## Operación

El GSPT constantemente supervisa valores de corriente del motor y parámetros de voltaje, frecuencia y potencia de la red. Cuando alguna condición de falla dañina ocurre, su salida se desactiva, manteniéndose así hasta que la falla desaparezca, las condiciones del sistema se hayan reestablecido y el motor se haya enfriado.

El GSPT dispone de:
- Un temporizador a la Conexión (Arranque)
- Un temporizador a la Desconexión por presencia de Falla

Estos temporizadores están incorporados para prevenir falsos disparos debido a las eventuales fluctuaciones de voltaje de la red.

Si en alguna ocasión llegase a suceder Otres o más) fallas de corriente en un intervalo menor a treinta minutos, el GSPT desactivará permanentemente su salida, y solo se podrá restaurar la operación del sistema manualmente, oprimiendo el pulsador de REARME. (Se recomienda verificar las causas de las tres fallas sucesivas).

### Características de la Pantalla LCD

El GSPT consta de una Pantalla de Cristal Líquido (LCD) para indicar el estado de salida y de falla de parámetros tales como:
- Corriente
- Voltaje
- Desbalance
- Frecuencia
- Potencia
- Factor de potencia
- Consumo de energía

### Controles y Comunicación

Está provisto de cuatro (04) botones pulsadores:
- Uno de REARME
- Dos de AJUSTE
- Uno de SELECCIÓN

Para ajustes de parámetros eléctricos de operación y protección.

También está provisto de puerto de comunicaciones para lectura de datos por medio de sistemas computarizados (GIO PORT, Protocolo MODBUS RTU).

### Indicadores Luminosos LED

| Estado | Led Verde | Led Rojo |
|--------|-----------|----------|
| Luz Continua | Contactor conectado o habilitado (ON) | Falla de voltaje o corriente (FALLA) |
| Luz Intermitente | Temporizando (TC) | — |

## Desmontaje

### Desmontaje (Riel Simétrico DIN)

**PELIGRO:** Apague el interruptor de alimentación (Breaker) y desconecte todos los cables al GSPT antes de proceder a desmontarlo. Hacer caso omiso puede resultar en daños a los equipos o personas.

**Instrucciones:**

1. Usando un destornillador plano, hale hacia abajo el Gancho de Retención dispuesto en la parte inferior del GSPT.
2. Mediante el destornillador desplace el gancho a la posición 2, saque el GSPT del Riel simétrico.

**Recomendaciones para el Desmontaje desde DIN Riel:** Hale suavemente y hacia abajo el gancho de retención unos 2mm aprox. Un movimiento brusco para sacar el gancho podría desprenderlo.

### Desmontaje (Superficie Plana)

1. Destornille ambos tornillos que fijan al GSPT a la superficie plana a través de los sujetadores insertables.
2. Luego saque el GSPT de dicha superficie.

## Guía Rápida de Programación para GSPT

**Versión de Software 1.12**

### Pantallas de Estado del Relé

#### 1.1 Desconectado por MODBUS
- Voltajes: 220V, 218V, 222V
- Estado: OFF
- Modo: MODBUS

#### 1.2 Desconectado Bajo Modo Manual
- Voltajes: 220V, 218V, 222V
- Estado: OFF
- Modo: MANUAL

#### 1.3 Desconectado por 3ª Falla
- Voltajes: 220V, 218V, 222V
- Estado: OFF
- Indicador: 3RA FALLA

#### 1.4 Temporizado a la Conexión (TC)
- Voltajes: 220V, 220V, 200V
- Duración: 15"
- Porcentaje de carga: 7%

#### 1.5 Temporizado a la Conexión (TC)
- Voltajes: 220V, 220V, 200V
- Estado: OFF, TC
- Tiempo mínimo: 40s

#### 1.6 TC por Subcarga
- Voltajes: 220V, 222V, 218V
- Indicador: FASE INVERTIDA
- Duración: 10"
- Porcentaje: 7%

#### 1.7 Bajo Voltaje (UV)
- Voltajes: 167V, 169V, 168V
- Tipo de Falla: UV
- Valor: 167V
- Fase: V12
- Porcentaje: 0%

#### 1.8 Sobre Voltaje (OV)
- Voltajes: 240V, 239V, 241V
- Tipo de Falla: OV
- Valor: 241V
- Fase: V31
- Porcentaje: 0%

#### 1.9 Desbalance de Voltaje (VUB)
- Voltajes: 221V, 267V, 264V
- Tipo de Falla: VUB
- Porcentaje de Desbalance: 11%

#### 1.10 Variación de Frecuencia (FS)
- Voltajes: 220V, 218V, 222V
- Tipo de Falla: FS
- Valor: 63.6 Hz
- Porcentaje: 0%

#### 1.11 Pérdida de Fase (VSP)
- Voltajes: 107V, 105V, 214V
- Tipo de Falla: VSP
- Fase Involucrada: L2
- Porcentaje: 50%

#### 1.12 Fase Invertida (PR)
- Tipo de Falla: FASE INVERTIDA
- Porcentaje: 0%

#### 1.13 Porcentaje (%) de Calor Acumulado
- Voltajes: 220V, 218V, 222V
- Indicador: CALOR
- Porcentaje: 50.4%

#### 1.14 Sobrecalentamiento
- Voltajes: 220V, 218V, 222V
- Indicador: CALOR EXCESIVO

#### 1.15 Relé Desviado
- Voltajes: 220V, 220V, 200V
- Indicador: RELE DESVIADO
- Porcentaje: 7%

### Pantalla de Inicio

**0.1 Pantalla de Inicio:**
- Modelo: GSPT
- Año: 2008
- Voltaje: 208V
- Versión de Software: v1.08

### Pantalla Principal

**1. Medición de Voltaje y Desbalance:**
- V12: 220V
- V23: 220V
- V31: 200V
- VUB: 7%
- Corrientes: I1, I2, I3 (en Amperios)
- CUB: Desbalance de Corriente

**2. Medición kW-kVA-PF-kWH:**
- Potencia Aparente: 110.0 kVA
- Factor de Potencia: 0.80 PF
- Potencia Real: 100.0 kW
- Consumo de Energía: 290000 kWH

**3. Histórico de Fallas:**
- Número de Falla: 19
- Fecha: 17/05
- Hora: 20:50
- Duración: 120'
- Tipo de Falla: UV
- Valor: 100V
- Fase: V12

**4. Contador de Horas del Motor:**
- Fecha y Hora: 02/06/05 14:11

**5. Temperatura del Motor, Frecuencia y Modo REARME:**
- Temperatura: 000025
- Frecuencia: 60.0 Hz
- Modo: AUTO

### Configuración de Ajustes (Menú Principal 7)

**7.1 Ajuste de Voltaje:**
- Voltaje Nominal: 280V
- Bajo Voltaje: 180V
- Sobre Voltaje: 240%
- Desbalance: 10%
- Frecuencia: 10%
- FS (Variación de Frecuencia): 10%
- TC Mín. OFF (Tiempo mínimo): 10"
- TD (Tiempo de Desconexión): 30"
- TC (Tiempo de Conexión): 600"

**7.2 Ajuste de Corriente:**

**7.2.1 Subcarga:**
- Subcarga: IN 40%
- TD Subcarga (Tiempo de Desconexión por Subcarga): 600"
- TC Subcarga (Tiempo de Conexión por Subcarga): 10%

**7.2.2 Ajuste Nominal de Corriente:**
- Corriente Nominal: 100A
- Sobrecarga: 11...20%
- TC Sobrecarga (Tiempo de Conexión): 10"
- Subcarga: NO
- 3ª Falla: OFF / NO
- Arranques/h: NO
- Máx. Arranques/h: 15

**7.3 Ajuste de Reloj:**
- Hora: 13:50
- Fecha: 07/31/03

**7.4 Modo de REARME:**
- Opciones: AUTO / MANUAL

**7.5 Cambio de Clave:**
- Ingrese Clave: 0000

**7.6 Dirección MODBUS:**
- Dirección: 001

**7.7 Borrar Histórico:**
- Mensaje: BORRANDO...

**7.8 Desea Forzar el Arranque:**
- Opciones: SI / NO

**7.9 Recobrar Valores de Fábrica:**
- Opciones: SI / NO

**7.10 Recobrando Valores:**
- Mensaje: RECOBRANDO VALORES

### Funciones Especiales del Teclado

- Presione simultáneamente los botones para entrar al menú (pantalla 7). Si el producto está protegido, introduzca la Clave.
- Presione simultáneamente los botones para activar la opción de Salida Rápida.
- Para validar el Valor de Ajuste a seleccionar.
- Presione simultáneamente los botones para activar la Pantalla de Inicio.

### Descripción de Pantallas de Fallas

#### Sobre Voltaje / Bajo Voltaje (N° 1.7 y 1.8)

**Valores de Voltaje durante Falla:**
- Voltaje Fase 1: 167V
- Voltaje Fase 2: 169V
- Voltaje Fase 3: 168V

**Tipo de Falla:**
- UV para Bajo Voltaje
- OV para Sobrevoltaje

**Información Mostrada:**
- Porcentaje (%) Desbalance Voltaje
- Fases Involucradas en la Falla
- Valor Extremo en la Falla

#### Voltaje, Frecuencia y Calor (N° 1.9 al 1.12)

**Valores de Voltaje durante Falla:**
- Voltaje Fase 1: 221V
- Voltaje Fase 2: 267V
- Voltaje Fase 3: 264V

**Tipo de Falla:**
- VUB para Desbalance Voltaje
- FS para Variación de Frecuencia
- VSP para Pérdida de Fase
- FASE INVERTIDA

**Información Mostrada:**
- Valores de Voltaje durante Falla
- Porcentaje (%) Desbalance Voltaje
- Fase Involucrada en la Falla
- Descripción de la Falla
- Porcentaje de Desbalance
- Porcentaje de Calor
- Valor Medido según la Pantalla

#### Histórico de Fallas

**Datos Registrados:**
- Número de la Falla: 19
- Fecha de la Falla: 17/05
- Hora de la Falla: 20:50
- Duración de la Falla (minutos): 120'
- Tipo de Falla: UV
- Valor Registrado de la Falla: 100V
- Fase Involucrada en la Falla: V12

## Glosario de Abreviaturas

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
| PR | Fase Invertida |
| UV | Bajo Voltaje |
| OV | Sobre Voltaje |
| CUB | Desbalance de Corriente |
| PROG. | Programación |
| T | Tiempo |
| HRS | Horas |
