---
title: "Guía de Instalación GI+"
type: Technical
source: "Guia de Instalacion GI+ Final.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GI+"
version_status: "vigente"
date_processed: "2026-05-10"
---

# Guía de Instalación GI+

## ALERTA DE SEGURIDAD

Solo personal técnico calificado con conocimientos en relés (relevadores) de protección y la carga asociada debería realizar la instalación, arranque y mantenimiento del sistema. Hacer caso omiso podría resultar en lesiones a personas y/o daños a los equipos conectados.

## GI+ PARTES Y PIEZAS

### Vista Frontal

1. **Indicadores Luminosos (LEDs)**:
   - LED VERDES - Luz Fija: CONECTADO (ON)
   - LED VERDES - Luz Intermitente: TEMPORIZADO (TC) a la Conexión
   - LED ROJO - Luz Fija: FALLA

2. **Pantalla LCD**

3. **Botón Pulsador de Rearme (Arranque)**

4. **Botones Pulsadores para Ajustes**

5. **Botón Pulsador para Selección**

6. **Frontal Insertable para Flush Mounting**

7. **Gancho Sujetador para Frontal**

8. **Ranura posterior para montaje en Riel simétrico**

9. **Sujetador Insertable para Montaje en Superficie Plana**

10. **Gancho de Retención para montaje en Riel simétrico**

11. **Terminales Enchufables**

12. **GIO PORT (Puerto de Comunicación)**

13. **Cubierta plástica protectora del GIO PORT**

### Características Generales

GI+ está provisto de pantalla LCD para indicar las fallas, el estado de la salida (voltaje, desbalance, frecuencia y estado de la carga) y el registro histórico de las últimas 20 fallas detectadas. Dispone de cuatro (4) botones pulsadores (Rearme, Ajuste (2) y Selección) para el ajuste de parámetros eléctricos tales como Voltaje Máximo, Voltaje Mínimo, Variación de Frecuencia, Temporizado a la Desconexión y Temporizado a la Conexión. GI+ está provisto de un puerto de Comunicación para lectura de datos por medio de sistemas computarizados (GIO Port, protocolo MODBUS RTU).

## GI+ ESPECIFICACIONES TÉCNICAS

### A) Fuente de Poder

| Parámetro | 120 V | 208/220 V | 440/480 V |
|-----------|-------|-----------|-----------|
| Voltaje de Operación, Ue | 120 | 208/220 | 440/480 V~ |
| Límite de Operación de Voltaje, Ue | 72 > 168 | 145 > 312 | 264 > 672 V~ |
| Consumo Promedio, In | 44 mA | — | — |
| Frecuencia de Operación | 42 → 70 Hz | — | — |
| Modo de Operación | Continuo | — | — |

### B) Condiciones Ambientales, Límites de Operación e Instalación

| Parámetro | Valor |
|-----------|-------|
| Temperatura Ambiental (Operación) | -10 °C a +60 °C (14 °F a 140 °F) |
| Temperatura Ambiental (Almacenaje) | -10 °C a +70 °C (14 °F a 158 °F) |
| Humedad Relativa Máxima | 85% R.H. |
| Protección a Objetos/Agua | P20, Protegido contra objetos > 125 mm, IEC 60529, ninguna protección contra agua |
| Nivel de Contaminación | Grado 3, IEC 60255-5 |
| Protección contra Exceso de Voltaje | Categoría III, 4KV, IEC 60255-5 |
| Voltaje de Aislamiento Nominal | 500V, UL IEC 60255-5 |
| Prueba de Impulso | 5 KV, IEC 60255-5 |
| Prueba Dieléctrica | 2.5 KV 50/60 Hz @ 1 min, UL 508 |
| Grado de Protección al Fuego de la Carcaza | 5 VA, UL-94 |
| Material de la Carcaza | Polímeros: LEXAN 500R, ABS, Nylon |
| Tipo de Montaje | Riel DIN Simétrico IEC 715, DIN 43880; Superficie Plana, tornillo 3/16" x 1/2", Tipo NEMA; Empotrable (Flush Mounting) |
| Tipo de Tornillo de Borneras | Plano M2.5 |
| Torque de Apretado de Borneras | 5.2 Kg-cm (4.5 lb-in) |
| Medidas | 105 x 90 x 68 (L x A x H) mm |
| Peso | 0.23 Kg (0.506 lb) |

### C) Características de Control

| Parámetro | Valor |
|-----------|-------|
| Capacidad de los Contactos | 3 A @ 240 V~, 1.5 A @ 480 V~ UL 508, Pilot Duty Sección 139.1 |
| Expectativa de vida Eléctrica | 100,000 Operaciones |
| Expectativa de vida Mecánica | 10,000,000 Operaciones |

### D) Ajustes de Rango, Mediciones (Modelo de Voltaje)

| Parámetro | 120 V | 208 V | 480 V |
|-----------|-------|-------|-------|
| Rango de Medición de Voltaje, Um | 0 > 168 | 0 > 300 | 0 > 672 V~, 2% |
| Rango de Frecuencia | 45.0 — 70.0 Hz, 1% Precisión | — | — |

### F) Comunicaciones y Otras Funciones Especiales

| Parámetro | Descripción |
|-----------|-------------|
| Protocolo de Comunicaciones | MODBUS RTU @ 9600 8N1 |
| Puerto de Comunicación | GIO PORT (*) - ver Manual de Usuario |
| Reporte Histórico de Fallas | Reporte de últimas 20 fallas, tipo de falla y valor - Ver Manual de Usuario |
| Bloqueo de Parámetros (Clave) | 0000 Libre, 0001-9999 Bloqueado - Selección del Usuario |

(*) Se requiere GIO-PLUG para la comunicación a través de GIO Port. El GIO-PLUG se suministra por separado.

## DIMENSIONES GENERALES

- Largo: 105 mm
- Ancho: 90 mm
- Alto: 68 mm

Modelo GI+L480S: 99.8 mm

## CÓMO ORDENAR GI+

**Formato:** GI+L-[VOLTAJE]-[IDIOMA]

### Voltaje:
- 120 = 120 V~
- 208 = 208/220 V~
- 480 = 440/480 V~

### Idioma:
- S = ESPAÑOL
- E = INGLÉS
- P = PORTUGUÉS

## GI+ AJUSTES DE PANTALLA

### Guía Rápida de Programación para GI+

#### Pantallas de Estado del Relé

**0. Pantalla de Inicio**
- Generación de información de estado

**1.1 Conectado bajo Modo AUTO**
- Indicador: CONECTADO
- Modo: AUTO
- Información de voltaje y frecuencia

**1.2 Desconectado bajo Modo MANUAL**
- Estado: OFF
- Modo: MANUAL

**1.3 Desconectado por MODBUS**
- Estado: OFF
- Modo: MODBUS

**1.4 Temporizado a la Conexión (TC)**
- Muestra el tiempo de conexión

**1.5 Bajo Voltaje (UV)**
- Visualiza voltaje mínimo y fases

**1.6 Sobre Voltaje (OV)**
- Visualiza voltaje máximo y fases

**1.7 Pérdida de Fase (VSP)**
- Detección de pérdida de fase

**1.8 Fase Invertida (PR)**
- Indicación de secuencia invertida

**1.9 Variación de Frecuencia (FS)**
- Visualiza variación de frecuencia

**1.10 Desbalance de Voltaje (VUB)**
- Muestra porcentaje de desbalance

#### Pantallas de Fallas

**4.1.1 Bajo Voltaje**
- Tipo: BAJO VOLT.
- Voltaje: 180V

**4.1.2 Sobre Voltaje**
- Tipo: SOBRE VOLT.
- Voltaje: 250V

**4.1.3 Clave Incorrecta**
- Aviso de error en ingreso de contraseña

**4.1.4 Desbalance y Frecuencia**
- DESBALANCE 10%
- FRECUENCIA 50 Hz

**4.1.5 Frecuencia**
- FS: Variación de Frecuencia
- Rango: 42 Hz

**4.1.6 Modo de Rearme**
- AUTO
- MANUAL

**4.1.7 Temporizado a la Desconexión**
- TD: Tiempo configurado

#### Menú Principal de Ajustes

**2. Histórico de Fallas**
- Registro de últimas 20 fallas
- Tipo de falla
- Valores registrados
- Fases involucradas

**3. Configuración de Botones Pulsadores**
- REARME
- AJUSTE
- SELECCIÓN
- DIRECCIÓN MODBUS

#### Funciones Especiales de Botones Pulsadores

- Presione simultáneamente los botones para entrar al menú (pantalla 4). Si el producto está protegido, introduzca la Clave.
- Presione simultáneamente los botones para activar o desactivar la opción de Salida Rápida.
- Presione simultáneamente los botones para activar la Pantalla 0 de Inicio.

#### Validación de Ajustes

Presione simultáneamente los botones para validar el Valor de Ajuste.

### Descripción de Pantallas de Fallas

#### Sobre Voltaje / Bajo Voltaje

- **Tipo de Falla**: UV para Bajo Voltaje, OV para Sobrevoltaje
- **Valores de Voltaje**: Voltajes durante falla en cada fase (V31, V12, V23)
- **Número de Falla**: Identificador secuencial

#### Voltaje y Frecuencia

- **Tipo de Falla**: VUB para Desbalance Voltaje, FS para Variación de Frecuencia, VSP para Pérdida de Fase
- **Valor registrado**: Porcentaje de desbalance, variación de frecuencia, o fase involucrada
- **Valores extremos**: Valor mínimo de voltaje registrado
- **Fases involucradas**: Identificación de fases afectadas

#### Histórico de Fallas

- Tipo de Falla (ej: Bajo Voltaje)
- Número de la Falla
- Valores de Voltaje durante Falla
- Fases Involucradas en la Falla
- Valor Extremo en la falla

## INSTALACIÓN

### Pasos de Instalación:

1. **Desconecte** el interruptor o fusibles de alimentación eléctrica.

2. **Atornille** el GI+ sobre superficie, o móntelo en un riel simétrico.

3. **Conecte** los cables según el diagrama de conexión.

4. **Ajuste** la protección mediante los botones de programación, de acuerdo a las especificaciones del equipo a proteger.

5. **Reconecte** el interruptor o fusibles de alimentación.

## DIAGRAMA DE CONEXIÓN

### Conexiones Normal/Falla:

| Condición | Terminales |
|-----------|-----------|
| Normal | 8-10 CONECTADO; 10-12 ABIERTO |
| Falla | 8-10 ABIERTO; 10-12 CONECTADO |

### Componentes:

- CONTACTOR (usuario provisto por el usuario)
- Li, L2, L3 — Alimentación trifásica 50/60 Hz
- Terminales de conexión: 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24
- A PROTEGER: Salida hacia equipo a proteger

## GLOSARIO DE ABREVIATURAS

| Abreviatura | Significado |
|-------------|-------------|
| FS | VARIACIÓN DE FRECUENCIA |
| VSP | PÉRDIDA DE FASE VOLTAJE |
| PR | FASE INVERTIDA |
| UV | BAJO VOLTAJE |
| OV | SOBRE VOLTAJE |
| VUB | DESBALANCE VOLTAJE |
| TD | TEMPORIZADO A LA DESCONEXIÓN |
| TC | TEMPORIZADO A LA CONEXIÓN |
| PROG. | PROGRAMADOR |
| VOLT. | VOLTAJE |

## NOTA

Las especificaciones y descripciones mostradas en este documento están sujetas a cambio sin previo aviso.
