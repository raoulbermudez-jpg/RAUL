---
title: "GSPT - Relé de Protección para Bombas en General"
type: Technical
source: "GSPT_HDE_V2_C.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "GSPT"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GSPT - Relé de Protección para Bombas en General

## Descripción General

SUBTRONIG GSPT es un Relé (Relevador) trifásico para Protección de Bombas en General basado en tecnología de microcontroladores, diseñado especialmente para proteger motores con clase térmica 10, contra los daños ocasionados por fallas comunes de corriente y voltaje.

SUBTRONIG GSPT supervisa constantemente la Corriente de Consumo del Motor y los principales parámetros eléctricos tales como el Voltaje de Línea, Frecuencia de Red, Potencia Aparente, Potencia Real, Factor de Potencia y Consumo de energía. En caso de presentarse una condición anormal de falla, SUBTRONIG GSPT desactivará su salida hasta que la falla desaparezca y el motor se haya enfriado completamente. Temporizadores a la Conexión y a la Desconexión por Falla están incorporados a este relé para prevenir disparos innecesarios debido a las rápidas fluctuaciones del sistema.

## Características Generales

### Medición de:
* Corriente
* Voltaje
* Frecuencia
* Factor de Potencia (PF), Potencia Aparente (kVA), Potencia Real (kW) y Consumo de Energía (kWH)

### Protección contra:
* Excesos de arranques falsos (Límite de veces según la potencia del motor)
* Sobrecarga
* Subcarga
* Sobre Voltaje / Bajo Voltaje
* Desbalance de Voltaje
* Desbalance de Corriente
* Pérdida de Fase
* Fase Invertida
* Rotor Bloqueado

### Ajustes disponibles:
* Sobrecarga
* Subcarga por límite inferior de corriente
* Sobre Voltaje
* Bajo Voltaje
* Desbalance de Corriente
* Desbalance de Voltaje
* Frecuencia
* Temporizado a la Desconexión por Falla
* Temporizado a la Conexión después de Falla de Voltaje
* Temporizado a la Conexión después de Sobrecarga
* Modo de Rearme AUTO/MANUAL
* Clave Secreta (Password)

### Características Físicas:
* Montaje sobre Superficie Plana, Montaje sobre Din-Rail o Montaje Empotrable en Panel (Flush Mounting)
* Pantalla Cristal Líquido (LCD), 16x2, para indicación de valores de corriente y voltaje así como reportes del estado de la carga
* Cuatro (4) botones pulsadores para ajustes de parámetros de operación y de protección (uno de REARME, dos de AJUSTE y uno de SELECCIÓN)
* Material de la Carcasa UL94V0
* Dos (2) salidas de relé contrapuestas, DPST 1.0A@240V~ / 0.5A@480V~
* Disponibles con CT Interno
* GIO Port (Protocolo MODBUS RTU)
* Encendido/Apagado Remoto
* Retención de parámetros configurados al generarse fallas, con posibilidad de ser vistos en un computador PC
* Memoria Térmica

### Reportes:
* Reporte de Voltaje y Corriente
* Reporte de PF, KVA, KWH y KW
* Reporte de Valores Ajustados
* Reporte de Tiempo acumulado de trabajo del Motor
* Reporte del Modo de Encendido
* Reporte de Últimas 80 Fallas
* Reporte de Frecuencia de Red

## Normas de Producto Aplicadas

Diseñado conforme a las Normas CE (LVD y EMC):
* IEC 61010-1
* IEC 60255-6
* IEC 60255-8
* IEC 60947-1

Diseñado según Norma:
* UL 508
* IEEE 37.112
* NEMA MG10

## Funciones Generales & Rango de Aplicaciones

SUBTRONIG GSPT proporciona protección eléctrica por medio de las siguientes funciones generales y rangos de ajustes:

| Función | Rango |
|---------|-------|
| Sobre Voltaje | 5% a 20% del Voltaje Nominal |
| Bajo Voltaje | -20% al -5% del Voltaje Nominal |
| Desbalance de Voltaje | 2% al 10% del Voltaje Nominal |
| Pérdida de Fase por Voltaje | (IN 33% - OUT 28%) |
| Temporizado a la Desconexión por Fase Invertida | < 15 |
| Temporizado a la Conexión, después de Falla de Voltaje | 0 a 600 s |
| Temporizado a la Desconexión por Falla de Voltaje | 1 a 30 s |
| Detección Variación de Frecuencia | +/-2% al +/-10% Frecuencia Nominal |
| Ajuste Nivel de Sobrecarga | 5% al 50% |
| Detección de Subcarga | Límite inferior ajustable, relativo a I nominal |
| Temporizado a la conexión, después de Sobrecarga | 10 a 60 min. ajustable por el usuario |
| Desbalance de Corriente | CUB > 48% |
| Pérdida de Fase por Corriente | CUB > 60% |
| Clase Térmica | IEC 60255-8 |

## Características Físicas - Dimensiones

* Largo: 91 mm
* Ancho: 96.15 mm
* Alto: 93 mm
* Peso: 0.494 Kg (1.09 lb)

## Información de Seguridad

Solo personal técnico calificado con conocimientos en relés de sobrecarga y de la maquinaria a proteger, debería realizar la instalación, arranque y mantenimiento del sistema. Hacer caso omiso podría resultar en lesiones a personas y/o daños a los equipos conectados.

## Medidas a Considerar Respecto a la Compatibilidad Electromagnética

Este producto ha sido diseñado para Ambiente Industrial Severo. De ser utilizado en Ambiente Residencial, el usuario podría requerir algunas medidas en caso de que note algún ruido eléctrico inesperado en artefactos domésticos.

## Instalación - Diagrama de Conexión

Los Cables del Motor pasan primero por los orificios del GSPT. El voltaje se empalma antes del contactor. Usar GIOPlug (Adaptador Opcional) para comunicación serial con otros dispositivos.

## Herramientas Requeridas para Instalación o Conexión

* Destornillador adecuado para tornillos tipo M3 para la conexión en terminales
* Destornillador adecuado para tornillos 3/16" x ½" para el montaje en Superficie Plana

## Cómo Ordenar SUBTRONIG GSPT

Formato: GSPT — [VOLTAJE] — [CORRIENTE] — [OPCIONES] — [IDIOMA]

**Voltaje:**
* 208 — 208/220/240V~
* 480 — 440/480V~

**Corriente:**
* 1-4A
* 3.5-125A
* 10-32 A
* 25-80 A

**Opciones:**
* S — ESTÁNDAR

**Idioma:**
* S — ESPAÑOL
* E — INGLÉS

## Especificaciones Técnicas

### A) Fuente de Poder

| Parámetro | 208/220/240V | 400V | 440/480V |
|-----------|--------------|------|----------|
| Voltaje de Operación, Ue | 208/220/240V | 400V | 440/480V |
| Límites de Operación de Voltaje | 445>319 | 228>532 | 264>672 |
| Consumo Promedio, In | 45 mA | - | - |
| Frecuencia Nominal, Fn | 50/60 Hz | - | - |
| Frecuencia de Operación | 42 >70 Hz | - | - |
| Modo de Operación | Continuo | - | - |

### B) Condiciones Ambientales

* Normas - Requisitos para EUROPA: IEC 61010-1, IEC 60255-6, IEC 60947-1 (LVD & EMC)
* Normas - Requisitos para USA: UL 508 (pendiente), NEMA
* Temperatura Ambiental (Operación): -5°C a 55°C (-23°F a 131°F)
* Temperatura Ambiental (Almacenaje): -40°C a +70°C (-14°F a 158°F)
* Humedad Relativa Máxima: 85% R.H.
* Resistencia a Vibraciones: Clase 1, Amplitud <0.035 mm, 1G 10 Hz < 150 Hz
* Protección a Objetos/agua: IP20, Protección contra objetos > 12.5 mm, ninguna protección contra agua
* Nivel de Contaminación: Grado 3
* Protección contra Exceso de Voltaje: Categoría III
* Voltaje de Aislamiento: 500 V Nominal
* Grado de protección al Fuego de la carcaza: UL-94 0
* Material de la Carcasa: Polímeros: LEXAN, ABS, VYDYNE
* Posiciones de Montaje: Sin Restricciones
* Tipos de Montaje: Riel DIN Simétrico DIN 43880, Superficie Plana Tornillo 3/16" x ½" Tipo NEMA
* Tipo de Tornillo de Borneras: Plano M3
* Torque de Apretado de Borneras: 5.1 Kg-cm / 4.4 Ib-in
* Cableado de Borneras: 10-18 AWG
* Cableado en el Sensor de Corriente: 9<11 mm, AWG 4
* Medidas: 92 x 91 x 96 (L x A x H) mm
* Peso: 0.494 Kg

### C) Características de Control

* Capacidad de los Contactos (para Circuitos de Control): 1 A @ 240 V~, 0.5 A @ 480 V~, A300 PILOT DUTY UL 508 Sección 139.1
* Expectativa de Vida Eléctrica: 100,000 Operaciones
* Expectativa de Vida Mecánica: 10,000,000 Operaciones
* Categoría de Uso: AC-15, Capacidad para cargas > 72 VA

### D) Ajustes de Rango, Mediciones

| Parámetro | 208V | 400V | 480V |
|-----------|------|------|------|
| Rango de Medición de voltaje, Um | 0>312 | 0>672 | - |
| Rango de Medición de corriente, Im | 1.5>40 | 0.3>125 | 1>320 / 25>800 |

### Otros Parámetros Medidos:

| Parámetro | Rango | Tolerancia |
|-----------|-------|-----------|
| Rango de Frecuencia | 45.0 - 70.0 Hz | 1% |
| Factor Potencia Instantáneo | 0.00 → 1.00 | 8% |
| Potencia Aparente Instantánea (kVA) | 0.0 → 999.9 kVA | 4% |
| Potencia Real Instantánea (kW) | 0.0 → 999.9 kW | 4% |
| Consumo de Energía (WH) | 0 → 999999 KW/H | 4% |
| Horas de trabajo acumuladas del motor | 0 → 999999 H | 1% |

### E) Funciones y Algoritmos de Protección

**Según el Modelo de Voltaje:**

| Función | 208V | 400V | 480V | Ajustable |
|---------|------|------|------|-----------|
| Bajo Voltaje (UV) @ Imotor=0 u OC | 350>460 | 165>225 | 320>380 | Sí |
| Sobre Voltaje (OV) @ Imotor=0 u OC | - | 215-270 | 420>480 / 460>580 | Sí |
| Umbral Histéresis de Voltaje | 6 | 10 | 12 | - |
| Desbalance de Voltaje (VUB) | 2% > 10% | - | - | Ajustable |
| Pérdida de Fase de Voltaje (VSP) | IN VUB > 33%, OUT VUB < 28% | - | - | - |
| Frecuencia Nominal | 50.6 / 60 Hz | - | - | Ajustable |
| Variación de Frecuencia | 2% > 10% | - | - | Ajustable |
| Fase Invertida (PR) | Secuencia ABC Normal, Secuencia CBA Invertida | - | - | - |
| Temporizado a la Desconexión por Fase Invertida (PR) | - | - | - | Sí |
| Temporizado a la Desconexión por otras Fallas de Voltaje (TD) | 1> 30 s | - | - | Ajustable |
| Temporizado a la Conexión (TC) en VSP | - | - | - | Ajustado a 35 |

**Según el Modelo de Corriente:**

| Función | Rango |
|---------|-------|
| Modo de Rearme | Automático/Manual |
| Ajuste Corriente Nominal | 1.5>4 / 3.5>125 / 10>32 / 25>80 A |
| Ajuste Nivel Sobrecarga (OL) | 5% > 50% |
| Temporizado conexión por sobrecarga (OC) | 10 a 60 Minutos |
| Clase Térmica | 10 |
| Ajuste Dinámico (Curva Fría / Curva Caliente) | Clase Térmica varía del 18 de la clase 10 según el tiempo de encendido y nivel de carga del motor |
| Tiempo Máximo entre curvas Fría/Caliente | 2 Horas |
| Tiempo Desconexión de Falla por Sobrecarga | Según el nivel de Sobrecarga de Clase 10 |
| Umbral de Calor para Falla por Sobrecarga | 100% |
| Desbalance de Corriente (CUB) | CUB > 48% |
| Pérdida de fase por Corriente (CSP) | CUB > 60% |
| Detección Rotor Bloqueado (LR) | Reajuste del Calor Acelerado Continuo |
| Temporizado Desconexión por CSP | 3 S |
| Temporizado Desconexión por CUB | 4 S |
| Subcarga | SI/NO - Selección Usuario |
| Tipo Desconexión por Subcarga (UC) | Detección relativa a corriente Nominal Inom - Selección Usuario |
| Ajuste Nivel Subcarga (UC) | 30% > 90% |
| Temporizado Desconexión por Subcarga (UC) | 5 > 600 Seg. |
| Temporizado Conexión por Subcarga (UC) | 2 > 500 Min. |
| Detección de Tercera (3ª) Falla | SI/NO - Selección Usuario |
| Desconexión permanente por Tercera (3ª) Falla | 3 Fallas de Corriente en menos de 30 min. |
| Tiempo desconexión para Rotor bloqueado acelerado | 3 Seg |
| Máximo numero de arranques por hora | Selección usuario - Máximo automático hasta 12 |
| Numero de arranques por hora según HP | Mínimo - AJUSTABLE |
| Tiempo mínimo entre arranques | 1 a 10 Min. |

### F) Funciones y Algoritmos de Comunicación

* Protocolo de Comunicación: MODBUS RTU @ 9600 8N1
* Puerto de Comunicación: GIO PORT (Se requiere GIO PLUG para la comunicación)
* Rango de Direcciones: 1 > 127
* Histórico de Fallas: Reporte de 80 últimas fallas (Datos de Tipo Falla, Valor, Hora, Fecha y Tiempo de Duración)
* Retención de parámetros configurados cuando ocurrieron las fallas: Ajustes de voltaje, Ajustes de corrientes, Modo de rearme
* Bloqueo de Parámetros: 0000 Libre, 0001 > 9999 - Selección Usuario

### G) Compatibilidad Electromagnética para Ambiente Industrial Severo

Estándares de Inmunidad y Emisiones:
* Descarga Electrostática: IEC 61000-4-2
* Inmunidad a Ruido Eléctrico Radiado: IEC 61000-4-3
* Transientes Rápidas: IEC 61000-4-4
* Picos de Alta Energía: IEC 61000-4-5
* Perturbaciones Conducidas: IEC 61000-4-6
* Campos Magnéticos: IEC 61000-4-8
* Reducciones e Interrupciones de Voltaje: IEC 61000-4-11
* Armónicos: IEC 61000-4-13
* Fluctuaciones de Voltaje: IEC 61000-4-14
* Desbalance Trifásico: IEC 61000-4-27
* Variaciones de Frecuencia: IEC 61000-4-28

## Curvas de Protección Térmica

El dispositivo cuenta con dos curvas de operación (Curva Fría y Curva Caliente) que varían según el tiempo de encendido y nivel de carga del motor. La transición máxima entre curvas es de 2 horas.

## Protección Adicional para Bombas - Número de Arranques por Hora

Cuando el usuario selecciona el límite automático de máximo número de arranques por hora, el GSPT predispone los siguientes valores de acuerdo al motor instalado:

* HP = Potencia nominal del motor instalado
* Sph = Cantidad máxima de arranques permitidos por hora

Esta función aplica con valores en aproximación a lo prescrito en estándar NEMA MG10.

## Nota

Las especificaciones y descripciones mostradas en este documento están sujetas a cambio sin previo aviso.
