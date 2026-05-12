---
title: "GSPT-MV - Relé de Protección Total de Bombas en General"
type: Technical
source: "GSPT-MV_HDE_V2_C.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "GSPT-MV"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GSPT-MV - Relé de Protección Total de Bombas en General

## Descripción General

SUBTRONIG GSPT-MV es un Relé (Relevador) trifásico para Protección de Bombas en general basado en tecnología de microcontroladores, diseñado especialmente para proteger motores con clase térmica 10, contra los daños ocasionados por fallas comunes de corriente y voltaje.

SUBTRONIG GSPT-MV supervisa constantemente la Corriente de consumo del Motor y los principales parámetros eléctricos tales como el Voltaje de Línea, Frecuencia de Red, Potencia Aparente, Potencia Real, Factor de Potencia y Consumo de Energía. En caso de presentarse una condición anormal de falla, SUBTRONIG GSPT-MV desactivará su salida hasta que la falla desaparezca y el motor se haya enfriado completamente.

## Características Generales

### Medición de:
- Corriente
- Voltaje
- Frecuencia
- Factor de Potencia (PF), Potencia Aparente (kVA), Potencia Real (kW) y Consumo de Energía (kWH)
- Temperatura

### Ajuste de:
- Sobrecarga
- Subcarga por límite inferior de corriente
- Sobre Voltaje
- Bajo Voltaje
- Desbalance de Corriente
- Desbalance de Voltaje
- Frecuencia
- Temporizado a la Desconexión por Falla
- Temporizado a la Conexión después de Falla de Voltaje
- Temporizado a la Conexión después de Sobrecarga
- Modo de Rearme AUTO/MANUAL
- Clave Secreta (Password)

### Comunicación:
- GIO Port (Protocolo MODBUS RTU)
- Encendido/Apagado Remoto
- Retención de parámetros configurados al generarse fallas, con posibilidad de ser vistos en computador PC

### Reportes:
- Reporte de Voltaje y Corriente
- Reporte de PF, KVA, KWH y KW
- Reporte de Valores Ajustados
- Reporte de Tiempo acumulado de trabajo del Motor
- Reporte del Modo de Encendido
- Reporte de Últimas 80 Fallas
- Reporte de Frecuencia de Red
- Reporte de Temperatura del Motor

### Protección contra:
- Excesos de arranques falsos (Límite de veces según la potencia del motor)
- Sobrecarga
- Subcarga
- Sobre Voltaje / Bajo Voltaje
- Variación de Frecuencia
- Desbalance de Voltaje
- Desbalance de Corriente
- Pérdida de Fase
- Fase Invertida
- Rotor Bloqueado
- Temperatura

### Características Físicas:
- Montaje sobre Superficie Plana, Montaje sobre Din-Rail o Montaje Empotrable en Panel (Flush Mounting)
- Pantalla Cristal Líquido (LCD), 16x2, para indicación de valores de corriente y voltaje así como reportes del estado de la carga
- Cuatro (4) botones pulsadores para ajustes de parámetros de operación y de protección (uno de REARME, dos de AJUSTE y uno de SELECCIÓN)
- Material de la Carcasa UL94V0
- Una (1) salida de Relé tipo SPDT (3A@240V~/1.5A@480V~)
- Una (1) Entrada tipo Analógica para temperatura (sensor PTC100)
- Disponibles con CT Interno
- Memoria Térmica

## Ventajas Distintivas

SUBTRONIG GSPT-MV excede la protección convencional de Bombas proporcionando las siguientes prestaciones:

- Provee protección fija contra eventos de Rotor Bloqueado acelerado
- Posibilita al usuario ajustar el Temporizado de Conexión, después de Sobrecarga
- Adapta automáticamente los límites extremos permitidos de Sobrevoltaje y Bajo voltaje, en función del voltaje nominal de alimentación configurable por el usuario
- Contiene un esquema de medición multivoltaje que permite ser configurado para operar con diferentes suministros nominales
- Limita la cantidad máxima de arranques falsos permitidos, por hora de servicio, según la capacidad del motor en HP
- Dispone de Pantalla LCD que indica el estado de los parámetros eléctricos de corriente y voltaje del motor
- Puerto de comunicaciones con Protocolo MODBUS RTU

## Voltajes de Operación

- Voltajes estándares: 208, 220, 230, 240, 400, 440, 480 V~
- Voltajes especiales: 200, 420, 460 V~

## Normas de Producto Aplicadas

### Diseñado conforme a las Normas CE (LVD y EMC):
- IEC 61010-1
- IEC 60255-6
- IEC 60255-8
- IEC 60947-1

### Diseñado según Norma:
- UL 508
- IEEE 37.112
- NEMA MG10

## Funciones Generales y Rangos de Ajustes

| Función | Rango |
|---------|-------|
| Sobre Voltaje | +5% a +20% del Voltaje Nominal |
| Bajo Voltaje | -20% a -5% del Voltaje Nominal |
| Desbalance de Voltaje | +/-2% a +/-10% Frecuencia Nominal |
| Pérdida de Fase por Voltaje | IN VUB > 33% - OUT VUB < 28% |
| Temporizado a la Desconexión por Fase Invertida | < 1s |
| Temporizado a la Conexión, después de Falla de Voltaje | 0 a 600s |
| Detección Variación de Frecuencia | 2% a 10% |
| Ajuste Nivel de Sobrecarga | 5% a 50% |
| Detección de Subcarga | Límite inferior ajustable, relativo a I nominal |
| Temporizado a la conexión, después de Sobrecarga | 10 a 60 min., ajustable por el usuario |
| Desbalance de Corriente | CUB > 48% |
| Pérdida de Fase por Corriente | CUB > 60% |
| Clase Térmica IEC 60255-8 | Clase 10 |

## Especificaciones Técnicas

### A) Fuente de Poder

| Parámetro | Especificación |
|-----------|----------------|
| Voltaje de Operación, Ue | 200, 208, 220, 230, 240, 400, 420, 440, 460, 480 V~ |
| Límites de Operación de Voltaje Ue | 72 → 672 V~ |
| Consumo Promedio, In | 38 mA |
| Frecuencia Nominal, Fu | 50/60 Hz |
| Frecuencia de Operación | 42 → 70 Hz |
| Modo de Operación | Continuo |

### B) Condiciones Ambientales, Límites de Operación e Instalación

| Parámetro | Especificación |
|-----------|----------------|
| Normas, Requisitos para EUROPA | IEC61010-1, IEC60255-6, IEC60947-1 (LVD & EMC) |
| Normas, Requisitos para USA | UL (pendiente), UL508 |
| Aprobación Europea | CE (pendiente), IEC60947-1 |
| Temperatura Ambiental (Operación) | -9 °C a 55 °C (23 °F a 131 °F) |
| Temperatura Ambiental (Almacenaje) | -10 °C a +70 °C (14 °F a 158 °F) |
| Humedad Relativa Máxima | 85% R.H. |
| Resistencia a Vibraciones | Clase 1 |
| Protección a Objetos/agua | P20 (Protección contra objetos > 12.6mm, ninguna protección contra agua) |
| Nivel de Contaminación | Grado 3 IEC 60255-5 |
| Categoría Protección Sobre Voltaje | Categoría III, 4KV |
| Voltaje de Aislamiento Nominal | 500V |
| Prueba de Impulso | 5 KV |
| Prueba Dieléctrica | 2.5 KV 50/60 Hz @ 1 min |
| Protección al Fuego de la Carcasa | V-0 (UL-94) |
| Material de la Carcasa | ABS, VYDYNE o LEXAN |
| Posiciones de Montaje | Sin Restricciones |
| Tipos de Montaje | DIN Riel Simétrico, Superficie Plana, Empotrable (Flush Mounting) |
| Tipo de Tornillo de Borneras | Plano M2.5 |
| Torque de Apretado de Borneras | 5.2 Kg-cm (4.5 Ib-in) |
| Cableado de Borneras | AWG 12-18, L=7-8mm (5/16) |
| Cableado por agujeros Caja CT | < 18 mm, máximo AWG 0 |

### C) Características de Control

| Parámetro | Especificación |
|-----------|----------------|
| Capacidad de los Contactos | 3A@240V~, 1.5A@480V~ (PILOT DUTY UL 508) |
| Expectativa de Vida Eléctrica | 100,000 Operaciones |
| Expectativa de Vida Mecánica | 10,000,000 Operaciones |
| Categoría de Uso | AC-15 |

### D) Ajustes de Rango, Mediciones (Modelo Multivoltaje - MV)

| Parámetro | Especificación | Tolerancia |
|-----------|----------------|-----------|
| Rango de Medición de Voltaje, Um | 0 → 672 | 4.2% |
| Rango de Medición de Corriente, Im (Modelo 050) | 1.5 → 500 | 4.2% |
| Rango de Medición de Corriente, Im (Modelo 100) | 30 → 1000 | 4.2% |
| Rango de Medición de Corriente, Im (Modelo 180) | 55 → 1800 | 4.2% |
| Rango de Frecuencia | 45.0 → 70.0 Hz | 1% |
| Factor Potencia Instantáneo | 0.00 → 1.00 | 8% |
| Potencia Aparente Instantánea kVA | 0.0 → 999.9 | 4% |
| Potencia Real Instantánea kW | 0.0 → 999.9 | 4% |
| Consumo de Energía kWH | 0 → 999999 | 4% |
| Horas de trabajo acumuladas del motor | 0 → 999999 H | 1% |
| Entrada de Temperatura | -20 °C → 200 °C | 1% |

### E) Funciones y Algoritmos de Protección

| Función | Especificación |
|---------|----------------|
| Bajo Voltaje (UV) @ Imotor=0 u 0C | -20% → -5% del voltaje nominal, Ajustable |
| Sobre Voltaje (OV) @ Imotor=0 u 0C | +5% → +20% del voltaje nominal, Ajustable |
| Umbral Histéresis de Voltaje | +/-3% del voltaje nominal Ve |
| Desbalance de Voltaje (VUB) | 2% → 10% Ajustable |
| Pérdida de Fase de Voltaje (VSP) | IN VUB > 33%, OUT VUB < 28% |
| Frecuencia Nominal | 50 o 60 Hz Ajustable |
| Variación de Frecuencia | 2% - 10% Ajustable |
| Fase Invertida (PR) | Secuencia ABC Normal, Secuencia CBA Invertida |
| Temporizado a la Desconexión por Fase Invertida (PR) | < 1s |
| Temporizado a la Desconexión por otras Fallas de Voltaje (TD) | 1 → 30s Ajustable |
| Temporizado a la Conexión (TC) | 0 → 600s Ajustable |
| Temporizado a la Desconexión por VSP | 3 S |
| Modo de Rearme | Automático/Manual Selección |
| Ajuste Corriente Nominal (Modelo 050) | 15 → 50 A |
| Ajuste Corriente Nominal (Modelo 100) | 30 → 100 A |
| Ajuste Corriente Nominal (Modelo 180) | 55 → 180 A |
| Ajuste Nivel Sobrecarga (OL) | Ajustable |
| Temporizado conexión por sobrecarga (OC) | 10 a 60 Minutos Ajustable |
| Clase Térmica | Clase 10 (IEC 60255-8) |
| Tiempo Máximo entre curvas Fría/Caliente | 2 Horas (de 1 a 1/3 o de 1/3 a 1) |
| Tiempo Desconexión de Falla por Sobrecarga | Según el nivel de Sobrecarga de Clase 10 |
| Umbral de Calor para Falla por Sobrecarga | 100% |
| Desbalance de Corriente (CUB) | CUB > 48% |
| Pérdida de fase por Corriente (CSP) | CUB > 60% |
| Detección Rotor Bloqueado Acelerado (LR) | CONTINUO al 100% |
| Temporizado Desconexión por CSP | 3 S |
| Temporizado Desconexión por CUB | 4 S |
| Tiempo de Enfriamiento Máquina Térmica | 480 S |
| Subcarga | SI/NO Selección Usuario |
| Tipo Desconexión por Subcarga (UC) | Detección relativa a corriente Nominal Inom |
| Temporizado Desconexión por Subcarga (UC) | 5 → 600 S. Ajustable |
| Temporizado Conexión por Subcarga (UC) | 2 → 500 Min. Ajustable |
| Detección de Tercera (3°) Falla | SI/NO Selección Usuario |
| Desconexión permanente por Tercera (3°) Falla | 3 Fallas de Corriente en menos de 30 min. |
| Tiempo desconexión para Rotor bloqueado acelerado | 3 S |
| Compensación por temperatura | SI/NO Selección usuario |
| Ajuste Temperatura Inicial Ti | 20 → 150 °C Ajustable |
| Ajuste Temperatura Máxima Tm | 50 → 200 °C Ajustable |
| Sensor (Tipo) | Platino 100 Ohm, 3 Cables (PT100) |
| Temperatura de desconexión | Valor Tm ajustado |
| Temperatura de conexión | (Tm - Ti) /6 + Ti |
| Máximo número de arranques por hora | SI/NO Selección usuario |
| Número de arranques por hora | Máximo automático, hasta 12 según HP; Mínimo seleccionable por usuario |
| Tiempo mínimo entre arranques | 1 Min. |

### F) Comunicaciones y Funciones Especiales

| Parámetro | Especificación |
|-----------|----------------|
| Protocolo de Comunicación | MODBUS RTU @ 9600 8N1 |
| Puerto de Comunicación | Puerto GIO PORT |
| Rango de Direcciones | 1 → 127 |
| Reporte de 80 últimas fallas | Tipo Falla, Valor, Hora, Fecha y Tiempo de Duración |
| Retención de parámetros configurados cuando ocurrieron las fallas | Ajustes de voltaje, Ajustes de corrientes, control de temperatura, modo de rearme |
| Bloqueo de Parámetros | 0000 Libre, 0001 a 9999 Bloqueado |

**Nota:** Se requiere GIO PLUG para la comunicación a través de GIO Port. El GIO PLUG se suministra por separado.

### G) Compatibilidad Electromagnética para Ambiente Industrial Severo - Estándares de Inmunidad y Emisiones

| Estándar | Referencia |
|----------|-----------|
| Descarga Electrostática | IEC 61000-4-2 |
| Inmunidad a Ruido Eléctrico Radiado | IEC 61000-4-3 |
| Transientes Rápidas | IEC 61000-4-4 |
| Picos de Alta Energía | IEC 61000-4-5 |
| Perturbaciones Conducidas | IEC 61000-4-6 |
| Campos Magnéticos | IEC 61000-4-8 |
| Interrupciones de Energía | IEC 61000-4-11 |
| Armónicos | IEC 61000-4-13 |
| Fluctuaciones de Voltaje | IEC 61000-4-14 |
| Desbalance Trifásico | IEC 61000-4-27 |
| Variaciones de Frecuencia | IEC 61000-4-28 |

## Dimensiones y Peso

| Dimensión | Especificación |
|-----------|----------------|
| Dimensión GSP | 175 x 90 x 78.0 (L x A x H) mm |
| Dimensión Caja CT | 175 x 90 x 79.8 (L x A x H) mm |
| Dimensión GSP + Caja CT | 175 x 90 x 157.8 (L x A x H) mm |
| Peso GSP | 0.463 kg (1.53 lb) |
| Peso Caja CT | 0.882 kg (1.94 lb) |
| Peso GSP + Caja CT | 1.345 kg (2.95 lb) |

## Diagrama de Conexión

El dispositivo cuenta con:
- Terminales de conexión para entrada de voltaje (L1, L2, L3)
- Salida a relé de control (11, 12, 13)
- Entrada para sensor de temperatura PT100
- Caja desmontable para CTs (Transformadores de Corriente)
- Puerto GIO para comunicación serial

**Estados del Relé:**
- Disparado: 8-10 (Conectado)
- Abierto: 6-8 (Conectado)
- Abierto: 6-8 (Desconectado)
- Conectado: 8-10 (Desconectado)

*Modo Configurable - Ver Manual de Usuario*

## Herramientas Requeridas para Instalación o Conexión

- Destornillador adecuado para tornillos tipo M2.5 para la conexión en terminales
- Destornillador adecuado para tornillos 3/16" x 1/2" para el montaje en Superficie Plana

## Cómo Ordenar GSPT-MV

**Formato de Código:**
- GSPT = Código base del producto
- MV = Multivoltaje
- Voltajes estándares disponibles: 208, 220, 230, 240, 400, 440, 480 V~
- Voltajes especiales disponibles: 200, 420, 460 V~
- Rango de corriente disponible:
  - 050: 15-50A
  - 100: 30-100A
  - 180: 55-180A
- Idioma:
  - S = Español
  - E = Inglés

## Información de Seguridad

### Alerta

Solamente personal técnico calificado con conocimientos en relés (Relevadores) de sobrecarga y de la maquinaria a proteger debería realizar la instalación, arranque y mantenimiento del sistema. Hacer caso omiso podría resultar en lesiones a personas y/o daños a los equipos conectados.

## Medidas a Considerar Respecto a la Compatibilidad Electromagnética

Este producto ha sido diseñado para Ambiente Industrial Severo. De ser utilizado en Ambiente Residencial el usuario podría requerir algunas medidas en caso de que note algún ruido eléctrico inesperado en artefactos domésticos.

## Número Máximo de Arranques por Hora

Cuando el usuario selecciona el límite automático de máximo número de arranques por hora, el GSPT-MV predispone los siguientes valores de acuerdo al motor instalado:

- HP = Potencia nominal del motor instalado
- Sph = Cantidad máxima de arranques permitidos por hora

Esta función aplica con valores en aproximación a lo prescrito en estándar NEMA MG10.

---

**Nota:** Las especificaciones y descripciones mostradas en este documento están sujetas a cambio sin previo aviso.

Fabricado en la REPÚBLICA BOLIVARIANA DE VENEZUELA
Distribuido por GENTECA, GENERACIÓN DE TECNOLOGÍA, C.A.
