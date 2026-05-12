---
title: "GSPT Manual de Instalación"
type: Technical
source: "GSPT_MAN-V2_C.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GSPT"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GSPT Manual de Instalación

## Descripción General

El GSPT es un Relé digital para Protección de Bombas en General que supervisa constantemente la Corriente del Motor y los principales parámetros eléctricos tales como Voltaje, Frecuencia, Factor de potencia, Potencia real, Potencia aparente y Consumo de energía, dando la protección más confiable contra Sobrecargas, Falla de fase, Fase invertida, Pérdida de fase, Desbalances, Arranques excesivos.

### Alerta de Seguridad

Solo personal técnico calificado con conocimientos en relés de sobrecarga y de la maquinaria a proteger, debería realizar la instalación, arranque y mantenimientos del sistema. Hacer caso omiso podría resultar en lesiones a personas y/o daños a los equipos conectados.

**Advertencia adicional:** Este producto puede activar al Contactor y hacer que arranque el motor de forma automática. El usuario debe tomar precauciones para evitar cualquier riesgo o daño.

## Partes y Piezas

### Componentes Principales

1. Pantalla de lectura LCD
2. Indicadores luminosos (LED's)
3. Pulsador REARME
4. Pulsadores AJUSTE
5. Pulsador SELECCIÓN
6. Ranura posterior para montaje en riel simétrico
7. Sujetadores insertables para montaje en superficies planas
8. Gancho de retención para montaje en riel simétrico
9. Orificios con sensores de corriente para pasar cables de alimentación al motor
10. Entradas de Voltaje de Línea (L1, L2, L3)
11. Contactos del Relé (95-96) y (97-98)
12. GIO PORT (puerto de comunicación)
13. Cubierta plástica protectora del puerto GIO PORT

### Indicadores Luminosos (LED's)

**Led Verde:**
- Luz continua: Contactor conectado o habilitado (ON)
- Luz intermitente: Temporizando (TC)

**Led Rojo:**
- Luz continua fija: Indica apagado de salida, debido a falla

### Estados de Contactos del Relé

- 95-96 conectado / 97-98 abierto: Estado disparado
- 95-96 abierto / 97-98 conectado: Estado normal

### Pantalla LCD

Presenta información de mediciones, estados, configuraciones e historia, en texto y números.

## Montaje

### Precauciones Generales

El GSPT debe ser instalado en lugar accesible, libre de polvo, suciedad, humedad y vibraciones. Que tenga suficiente espacio para la circulación de aire alrededor de su cubierta y fácil acceso a los controles de operación. SOLO PARA USO INTERIOR.

**Aviso:** Este producto ha sido diseñado para Ambiente Industrial Severo. De ser utilizado en Ambiente Residencial el usuario podría requerir algunas medidas en caso de que note algún ruido eléctrico inesperado en artefactos domésticos.

**Alerta:** Errores en la conexión o la aplicación en ambientes fuera de los límites especificados del GSPT, pueden resultar en un mal funcionamiento, o daños en sus componentes.

### Montaje sobre Riel Simétrico DIN

Instrucciones para Montaje Mecánico:

1. Coloque el GSPT en posición inclinada enganchando la ranura posterior con el riel.
2. Empuje presionando el GSPT hasta que haga CLICK.

### Montaje sobre Superficie Plana

Instrucciones para Montaje Mecánico:

a) Saque los dos (2) sujetadores insertables localizados en la parte posterior del GSPT. Luego inserte ambos sujetadores dentro de las ranuras verticales de la parte posterior del GSPT.

b) Coloque el GSPT sobre la superficie plana del panel y fijelo usando tornillos 3/16" x 1/2", empleando un destornillador adecuado.

**Recomendación para Montaje sobre Superficie Plana:** Haga dos (2) agujeros de 5/32" de diámetro sobre la superficie del panel antes de instalar el GSPT.

## Dimensiones Generales

- Altura: 111 mm
- Ancho: 93 mm
- Profundidad: 37 mm
- Guía para Superficie Plana: 100 mm x 96.15 mm

## Diagrama de Conexión

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

### Estados de Salida

| ESTADO | 95-96 | 97-98 |
|--------|-------|-------|
| Disparado | Conectado | Abierto |
| Normal | Abierto | Conectado |

### Peligro

Desconecte el suministro de energía antes de instalar el GSPT. Hacer caso omiso puede resultar en lesiones severas incluso la muerte.

### Precaución

Verifique que el modelo GSPT seleccionado para instalar corresponda con el voltaje nominal de línea y rango de corriente del motor.

### Diagrama Básico de Instalación

El diagrama muestra la conexión de:
- Interruptor de línea (L1, L2, L3)
- Fusibles opcionales 5A, 600V
- GSPT con terminales de entrada de voltaje (L1, L2, L3)
- Contactos de salida (95-96, 97-98)
- Contactor y bobina
- Motor
- Alarma opcional
- Luz piloto

### Recomendaciones para Cableado

- Evite apretar excesivamente los tornillos M3 de los terminales durante la conexión. Torque máximo: 4.4 Ib-in (5.11 kg-cm).
- Pelar los aislantes de los cables a conectar entre 6 a 7 mm.
- Usar cables para terminales: entre AWG10 (4 mm²) y AWG 18.
- El máximo tamaño de los cables de motor a pasar por orificios de sensores de corrientes será de: AWG 4 (11 mm²).
- Conecte los terminales de Voltaje de Entrada L1 L2 L3 antes del contactor y su respectivo circuito de arranque.
- Siempre pase los tres cables del motor por los tres orificios de sensores de corrientes. Dejar algún orificio sin cablear ocasionará falsas lecturas de desbalance.

## Operación

El GSPT constantemente supervisa valores de corriente del motor y parámetros de voltaje, frecuencia y potencia de la red. Cuando alguna condición de falla dañina ocurre, su salida se desactiva, manteniéndose así hasta que la falla desaparezca, las condiciones del sistema se hayan restablecido y el motor se haya enfriado.

### Temporizadores

- Temporizador a la Conexión Arranque
- Temporizador a la Desconexión por presencia de Falla

Estos temporizadores están incorporados al GSPT para prevenir falsos disparos debido a las eventuales fluctuaciones de voltaje de la red.

### Fallas Sucesivas

Si en alguna ocasión llegase a suceder tres o más fallas de corriente en un intervalo menor a treinta minutos, el GSPT desactivará permanentemente su salida, y solo se podrá restaurar la operación del sistema manualmente, oprimiendo el pulsador de REARME. Se recomienda verificar las causas de las tres fallas sucesivas.

### Características de Operación

El GSPT consta de una Pantalla de Cristal Líquido (LCD) para indicar el estado de salida y de falla de parámetros tales como corriente, voltaje, desbalance, frecuencia, potencia, factor de potencia y consumo de energía, entre otros.

Está provisto de cuatro (04) botones pulsadores:
- Uno de REARME
- Dos de AJUSTE
- Uno de SELECCIÓN

Estos se utilizan para ajustes de parámetros eléctricos de operación y protección.

Además, el GSPT está provisto de puerto de comunicaciones para lectura de datos por medio de sistemas computarizados (GIO PORT, Protocolo MODBUS RTU).

## Desmontaje

### Peligro

Apague el interruptor de alimentación (Breaker) y desconecte todos los cables al GSPT antes de proceder a desmontarlo. Hacer caso omiso puede resultar en daños a los equipos o personas.

### Desmontaje (Riel Simétrico DIN)

a) Usando un destornillador plano, hale hacia abajo el Gancho de Retención dispuesto en la parte inferior del GSPT.

b) Mediante el destornillador desplace el gancho a la posición 2 y saque el GSPT del Riel simétrico.

**Recomendaciones para el Desmontaje desde DIN Riel:** Hale suavemente y hacia abajo el gancho de retención unos 2 mm aproximadamente. Un movimiento brusco para sacar el gancho podría desprenderlo.

### Desmontaje (Superficie Plana)

Destornille ambos tornillos que fijan al GSPT, a la superficie plana a través de los sujetadores insertables y luego saque el GSPT de dicha superficie.

## Guía Rápida de Programación GSPT Versión de Software 1.12

### Pantallas de Operación

#### 1.1 Desconectado por MODBUS o Pantalla de Inicio
```
220 218 222 1
OFF MODBUS
```

#### 1.2 Desconectado Bajo Modo Manual
```
220 218 222 1
OFF MANUAL
TC 600"
```

#### 1.3 Desconectado por 3era. Falla
```
2008 v1.08
2 TD
```

#### 1.4 Temporizado a la Conexión (TC)
```
220 220 200 7%
TC 15"
```

#### 1.5 Temporizado a la Conexión (TC)
```
220 220 200 7%
MIN OFF TC 40"
```

#### 1.6 TC por Subcarga
```
220 220 200 7%
Sph TC 10"
```

#### 1.7 Bajo Voltaje (UV)
```
167 169 168 0%
UV 167V  V12 19 17/05 20:50
120 UV 100V v12
```

#### 1.8 Sobre Voltaje (OV)
```
240 239 241 0%
OV 241V  V31 v
```

#### 1.9 Desbalance de Voltaje (VUB)
```
221 267 264 11%
VUB 11%
```

#### 1.10 Variación de Frecuencia (FS)
```
220 218 222 0%
FS 63.6 Hz
FREC: 60.0 Hz
MODO: AUTO
```

#### 1.11 Pérdida de Fase (VSP)
```
107 08 a 50%
SI
```

#### 1.12 Fase Invertida (PR)
```
220 222 218 0%
FASE INVERTIDA
```

#### 1.13 Porcentaje (%) de Calor Acumulado
```
220 218 222 0%
CALOR 50.4%
```

#### 1.14 Sobrecalentamiento (AD)
```
220 218 222 0%
CALOR EXCESIVO (AD)
```

#### 1.15 Relé Desviado
```
220 220 200 71%
RELE DESVIADO (M€)
```

### Pantalla de Inicio (7.1)

Configuración por defecto:
- V NOMINAL: 280V
- BAJO VOLT.: 180V
- SOBRE VOLT.: 240V
- DESBALANCE: 10%
- FRECUENCIA: 102% / FS: 10%
- TC MIN. OFF: 10"
- TD: 30" / TC: 600"

### Menú de Ajuste de Corriente (7.2)

- GSPT: 208V
- I NOMINAL: 100A
- SUBCARGA: 40%
- SUBCARGA: 600"
- SUBCARGA: 10%
- SOBRECARGA: 20%
- SOBRECARGA: 10"
- SUBCARGA: NO
- 3RA FALLA OFF: NO
- ARRANQUES /h: NO

### Acceso al Menú Principal (7)

Presione simultáneamente los botones AJUSTE y SELECCIÓN para entrar al menú (pantalla 7). Si el producto está protegido, introduzca la Clave.

### Menú Principal de Ajustes (7)

- AJUSTE VOLTAJE
- AJUSTE CORRIENTE
- AJUSTE RELOJ
- MODO DE REARME
- CAMBIO DE CLAVE
- DIRECCIÓN MODBUS
- BORRAR HISTORICO
- REINICIAR EQUIPO
- SALIR

### Modo de Rearme (7.4)

- AUTO
- MANUAL

### Verificar Clave (7.5 y 7.6)

Ingrese clave: 0000

### Dirección MODBUS (7.7)

Dirección por defecto: 001

### Funciones Especiales del Teclado (8)

- Presione simultáneamente los botones AJUSTE y SELECCIÓN para entrar al menú (pantalla 7). Si el producto está protegido, introduzca la Clave.
- Presione simultáneamente los botones AJUSTE y SELECCIÓN para activar la opción de Salida Rápida.
- Para validar el Valor de Ajuste a seleccionar.
- Presione simultáneamente los botones AJUSTE y SELECCIÓN para activar la Pantalla 0 de Inicio.

### Histórico de Fallas (7.2.2)

El equipo registra:
- Fecha de la Falla
- Hora de la Falla
- Número de la Falla
- Porcentaje (%) Desbalance Voltaje
- Duración de la Falla (minutos)
- Fase Involucrada en la Falla

### Pantalla de Medición (2)

Presenta valores de:
- kW (Potencia Real)
- kVA (Potencia Aparente)
- PF (Factor de Potencia)
- kWH (Consumo de energía)

### Contador de Horas del Motor (4)

- Fecha y hora actual
- Total de horas de operación

### Temperatura del Motor, Frecuencia y Modo REARME (5)

- Frecuencia: 60.0 Hz
- Modo: AUTO

### Configuración de Botones (6)

- AJUSTE
- SELECCIÓN

### Opciones de Forzado (8.1)

- Función: ¿DESEA FORZAR EL ARRANQUE? SI/NO
- Función: RECOBRANDO VALORES DE FÁBRICA SI/NO

### Descripción de Fallas

#### Sobre Voltaje / Bajo Voltaje (N° 1.7 y 1.8)

- Valores de Voltaje durante Falla
- Porcentaje (%) Desbalance Voltaje
- Duración de la Falla (minutos)
- Fases Involucradas en la Falla

Tipos de falla:
- UV para Bajo Voltaje
- OV para Sobrevoltaje

#### Voltaje, Frecuencia y Calor (N° 1.9 al 1.12)

- Valores de Voltaje durante Falla
- Porcentaje (%) Desbalance Voltaje
- Descripción de la Falla
- Fase Involucrada en la Falla
- Porcentaje de Desbalance Voltaje
- Porcentaje de Calor
- Valor Medido según la Pantalla

Tipos de falla:
- VUB para Desbalance Voltaje
- FS para Variación de Frecuencia
- VSP para Pérdida de Fase
- FASE INVERTIDA

## Glosario de Abreviaturas

| ABREVIATURA | SIGNIFICADO |
|-------------|-------------|
| Sph | ARRANQUE POR HORA |
| 3F | TERCERA FALLA |
| BR | RELE DESVIADO |
| SM | ARRANQUE FORZADO |
| TEF | FALLA DE ENERGÍA |
| FS | FRECUENCIA |
| RL | ROTOR BLOQUEADO |
| PF | FACTOR DE POTENCIA |
| UC | BAJA CORRIENTE |
| Dep | SOBRE CORRIENTE |
| CSP | PERDIDA DE FASE POR CORRIENTE |
| VUB | DESBALANCE DE VOLTAJE |
| PR | FASE INVERTIDA |
| UV | BAJO VOLTAJE |
| OV | SOBREVOLTAJE |
| CUB | DESBALANCE DE CORRIENTE |
| PROG. | PROGRAMACIÓN |
| T. | TIEMPO |
| HRS | HORAS |
