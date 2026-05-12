---
title: "GUCT+ - Relé de Protección y Control para Generadores, Transformadores y Motores"
type: Technical
source: "GUCT+ c-CT GD-HE8005-CO-V.03.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "GUCT+"
version_status: "historica"
date_processed: "2026-05-10"
---

# GUCT+ - Relé de Protección y Control para Generadores, Transformadores y Motores

## Descripción General

GUCT+ es un relé trifásico para protección y control basado en tecnología de microcontroladores, diseñado especialmente para proteger motores, transformadores y equipos trifásicos en general contra los daños ocasionados por fallas comunes de voltaje y fallas de corriente por sobrecarga y subcarga.

GUCT+ supervisa constantemente la corriente de consumo del equipo y los principales parámetros eléctricos tales como voltaje de línea, frecuencia de red y factor de potencia. En caso de presentarse una condición anormal de falla, GUCT+ desactivará su salida hasta que la falla desaparezca y el equipo se haya enfriado completamente. Temporizadores a la conexión y a la desconexión por falla están incorporados para prevenir disparos innecesarios debido a las rápidas fluctuaciones del sistema.

## Características Generales

### Medición
- Corriente
- Voltaje
- Frecuencia
- Factor de Potencia (PF)
- Potencia aparente (kVA)
- Potencia real (kW)
- Consumo de energía (kWH)

### Ajustes
- Sobrecarga
- Subcarga
- Sobre voltaje
- Bajo voltaje
- Desbalance de voltaje
- Frecuencia
- Temporizado a la desconexión por falla
- Temporizado a la conexión después de falla de voltaje
- Clase térmica del motor
- Ajuste de reloj
- Programador de horario (eventos semanales & días especiales)
- Modo de rearme AUTO/MANUAL
- Clave secreta (Password)

### Comunicación
- GIO Port (Protocolo MODBUS RTU)
- Encendido/Apagado remoto

### Reportes
- Reporte de voltaje y corriente
- Reporte de PF, kVA, kW y kWH
- Reporte de tiempo acumulado de trabajo del motor
- Reporte del modo de encendido
- Reporte de últimas 20 fallas
- Reporte de frecuencia de red

### Protecciones
- Sobrecarga / Subcarga
- Sobre voltaje / Bajo voltaje
- Variación de frecuencia
- Desbalance de voltaje
- Pérdida de fase
- Fase invertida
- Desbalance de corriente
- Rotor bloqueado

### Características Físicas
- Montaje sobre superficie plana o montaje sobre Din-Rail
- Pantalla cristal líquido (LCD) 16x2 para indicación de valores de corriente y voltaje así como reportes del estado de la carga
- Cuatro (4) botones pulsadores para ajustes de parámetros de operación y de protección (uno de rearme, dos de ajuste y uno de selección)
- Material de la carcasa UL94V0
- Dos (2) salidas de relé contrapuestas SPST 1.0A@240V~ / 0.5A@480V~
- Disponibles con CT interno o para conexión CT externos
- Memoria térmica

## Normas de Producto Aplicadas

Diseñado conforme a las normas CE (LVD y EMC):
- IEC 61010-1
- IEC 60255-6
- IEC 60255-8
- IEC 60947-1
- UL 508
- IEEE C37.112
- NOM-003

## Funciones Generales y Rango de Aplicaciones

| Función | Rango |
|---------|-------|
| Sobre voltaje | 5% a 20% del voltaje nominal |
| Bajo voltaje | -20% al -5% del voltaje nominal |
| Desbalance de voltaje | 2% al 10% del voltaje nominal |
| Pérdida de fase por voltaje | IN 33% - OUT 28% |
| Variación de frecuencia | +/-2% al +/-10% frecuencia nominal |
| Ajuste nivel de sobrecarga | 5% al 50% |
| Detección de subcarga | Ajustable por PF o por Inominal |
| Desbalance de corriente | CUB > 48% |
| Pérdida de fase por corriente | CUB > 60% |
| Detección de factor de potencia | 0.0 al 1.0 |
| Clase térmica IEC 60255-8 | 5 a 35 (en pasos de uno a uno) |

## Especificaciones Técnicas

### A) Fuente de Poder

| Parámetro | Voltaje 208/220/240 | Voltaje 440/480 |
|-----------|-------------------|-----------------|
| Voltaje de operación Ue | 208/220/240 | 440/480 |
| Límites de operación de voltaje Ue | 145 > 312 | 264 > 672 |
| Consumo promedio In | 45 mA | 45 mA |
| Frecuencia nominal Fn | 50/60 Hz | 50/60 Hz |
| Frecuencia de operación | 42 → 70 Hz | 42 → 70 Hz |
| Modo de operación | Continuo | Continuo |

### B) Condiciones Ambientales, Límites de Operación e Instalación

- **Normas, requisitos para Europa**: LVD & EMC (IEC 60947-1)
- **Normas, requisitos para USA**: UL (pendiente), NKCR, Dispositivos auxiliares UL508
- **Aprobación europea**: CE (pendiente)
- **Temperatura ambiental (operación)**: -5°C a 55°C (23°F a 131°F)
- **Temperatura ambiental (almacenaje)**: -10°C a +70°C (14°F a 158°F)
- **Humedad relativa máxima**: 85% RH
- **Clase de resistencia a vibraciones**: 1, Amplitud 0.5g, Rango 4 Hz < f < 150 Hz (IEC 60255-21-1)
- **Protección a objetos/agua**: IP20, protegido contra objetos > 12.5 mm, ninguna protección contra agua (IEC 60529)
- **Nivel de contaminación**: Grado 3 (IEC 60255-5)
- **Protección contra exceso de voltaje**: Categoría III
- **Voltaje de aislamiento nominal**: 500V (UL)
- **Prueba de impulso**: 5 KV (IEC 60255-5)
- **Prueba dieléctrica**: 2.5 KV 50/60 Hz @ 1 min (UL 508)
- **Grado de protección al fuego de la carcaza**: V-0 (UL-94)
- **Material de la carcasa**: Polímeros LEXAN, ABS, VYDYNE
- **Posiciones de montaje**: Sin restricciones (IEC 715)
- **Tipos de montaje**: Riel DIN simétrico (DIN 43880), Superficie plana con tornillo 3/16" x 1/2" (Tipo NEMA)
- **Tipo de tornillo de borneras**: Plano M3
- **Torque de apretado de borneras**: 5.1 Kg-cm / 4.4 Ib-in
- **Cableado de borneras**: 10-18 AWG
- **Cableado en el sensor de corriente**: Y < 11 mm, AWG 4
- **Medidas**: 92 x 91 x 96 (L x A x H) mm
- **Peso**: 494 g (1.09 lb)

### C) Características de Control

- **Capacidad de los contactos**: B300 Pilot Duty UL 508, 0.1 (para circuitos de control) 1A@240 V~, 0.5 A@480 V~, Sección 139.1
- **Expectativa de vida eléctrica**: 100,000 operaciones
- **Expectativa de vida mecánica**: 10,000,000 operaciones
- **Categoría de uso**: AC-15, capacidad para cargas > 72 VA (IEC 60947-5-1)

### D) Ajustes de Rango, Mediciones

| Parámetro | Rango 208 | Rango 480 | Precisión |
|-----------|----------|----------|-----------|
| Rango de medición de voltaje Um | 0 > 312 | 0 > 672 | 2.3% |
| **Otros parámetros:** | | | |
| Rango de frecuencia | 45.0 → 70.0 Hz | | 1% |
| Factor potencia instantáneo | 0.00 – 1.00 | | 8% |
| Potencia aparente instantánea kVA | 0.0 > 999.9 kVA | | 4% |
| Potencia real instantánea kW | 0.0 > 999.9 kW | | 4% |
| Consumo de energía kWH | 0 > 999999 kW/H | | 4% |
| Horas de trabajo acumuladas del motor | 0 – 999999 H | | 1% |

**Rango de medición de corriente (CT)** - Modelo EXT (CT/5):
- Rango: 5% → 333% CT
- Precisión: 2.2%

### E) Funciones y Algoritmos de Protección

| Función | Rango 208 | Rango 480 | Ajustable |
|---------|----------|----------|-----------|
| Bajo voltaje (UV) Glmotor = 0 | 165 > 225 | 350 > 460 | Sí |
| Umbral histéresis voltaje | 2.3% | 2.3% | Sí |
| Desbalance de voltaje (VUB) | 2% > 10% | 2% > 10% | Sí |
| Pérdida de fase de voltaje (VSP) | IN VUB > 33%, OUT VUB < 28% | IN VUB > 33%, OUT VUB < 28% | — |
| Frecuencia nominal | 50 / 60 Hz | 50 / 60 Hz | Ajustable |
| Variación de frecuencia | 2% > 10% | 2% > 10% | Ajustable |
| Fase invertida (PR) | Secuencia ABC Normal, Secuencia CBA Invertida | Secuencia ABC Normal, Secuencia CBA Invertida | — |
| Temporizado a la desconexión (PR) por otras fallas de voltaje (TD) | 1 > 308 | 1 > 308 | Ajustable |
| Temporizado a la conexión (TC) | 0 > 600 s | 0 > 600 s | Ajustable |
| Temporizado a la desconexión (TD) por VSP | 35 | 35 | — |
| Modo de rearme | Automático/Manual | Automático/Manual | Usuario |
| Tiempo mínimo entre 2 arranques | 50 x Clase Térmica | 50 x Clase Térmica | — |

**Según el modelo de corriente**:
- **Ajuste corriente nominal**: Ver tabla 1
- **Ajuste nivel sobrecarga (OL)**: 5% > 50% Ajustable
- **Ajuste de clase térmica**: 5 > 35 Ajustable
- **Ajuste dinámico del motor (Curva fría/Curva caliente)**: Clase térmica varía de 7 > 18 o clase ajustada según el tiempo de encendido y nivel de carga del motor
- **Tiempo máximo entre curvas fría/caliente**: 2 horas (de 1/3 a 1/3 a 1)
- **Tiempo desconexión de falla por sobrecarga**: Según el nivel de sobrecarga y clase ajustada (IEEE 37.112-1998 CA)
- **Umbral de calor para falla por sobrecarga**: 100%
- **Desbalance de corriente (CUB)**: CUB > 48%
- **Pérdida de fase por corriente (CSP)**: CUB > 60%
- **Detección rotor bloqueado acelerado (LR)**: Sí/No
- **Umbral de calor por alta inercia**: 100%
- **Temporizado conexión por alta inercia**: 20 > 120 s Ajustable
- **Tiempo de enfriamiento máquina térmica**: 50 x clase térmica ajustada
- **Subcarga**: Sí/No
- **Tipo desconexión por subcarga (UC)**: % Inom ó FP (Factor de potencia)
- **Desconexión por subcarga (%Inom)**: 30% > 90% Ajustable
- **Desconexión por subcarga (PF)**: 0.3 > 0.9 Ajustable
- **Temporizado desconexión por subcarga (UC)**: 5 > 600 s Ajustable
- **Temporizado conexión por subcarga (UC)**: 2500 Min.
- **Detección de tercera (3%) falla**: Sí/No con desconexión permanente
- **Tercera falla**: 3 fallas de corriente en menos de 105 min. con tiempo desconexión para rotor bloqueado acelerado: 8 s

### F) Comunicaciones y Funciones Especiales

- **Protocolo de comunicación**: MODBUS RTU @ 9600 8N1 (ver manual)
- **Puerto de comunicación**: Puerto GIO PORT (*) (ver manual)
- **Rango de direcciones**: 1 > 127
- **Histórico de fallas**: Reporte de 20 últimas fallas (datos de tipo falla, valor, hora, fecha y tiempo de duración) (ver manual)
- **Bloqueo de parámetros**: 0000 Libre, 0001 > 9999 Bloqueado

(*) Se requiere GIOPlug para la comunicación a través de GIO Port. El GIOPLUG se suministra por separado.

### G) Compatibilidad Electromagnética para Ambiente Industrial Severo

Estándares de inmunidad y emisiones:
- **Inmunidad a ruido eléctrico radiado**: IEC 61000-4-3
- **Transientes rápidas**: IEC 61000-4-4
- **Picos de alta energía**: IEC 61000-4-5
- **Perturbaciones conducidas**: IEC 61000-4-6
- **Campos magnéticos**: IEC 61000-4-8
- **Reducciones e interrupciones de voltaje**: IEC 61000-4-11
- **Armónicos**: IEC 61000-4-13
- **Fluctuaciones de voltaje**: IEC 61000-4-14
- **Desbalance trifásico**: IEC 61000-4-27
- **Variaciones de frecuencia**: IEC 61000-4-28

## Características del Programador Horario

- **Ajuste reloj/fecha**: hh:mm dd/mm/aa
- **Control programador horario**: Sí/No (selección usuario)
- **Feriados programables**: 20

## Características Físicas y Montaje

### Indicadores y Controles
- Pantalla LCD 16x2
- Botones pulsadores (rearme, ajustes, selección)
- Indicadores luminosos
- Puerto GIO PORT

### Opciones de Montaje
- **Montaje en riel DIN simétrico** (DIN 43880)
- **Montaje en superficie plana** con sujetadores insertables (tornillo 3/16" x 1/2")

### Especificaciones de Contactos
- **Normal**: 95-96 Abierto, 97-98 Conectado
- **Disparado**: 95-96 Conectado, 97-98 Abierto

## Herramientas Requeridas para Instalación o Conexión

- Destornillador adecuado para tornillos tipo M3 para la conexión en terminales
- Destornillador adecuado para tornillos 3/16" x 1/2" para el montaje en superficie plana

## CT Externos Sugeridos Según la Corriente Nominal

| Rango de Corriente Nominal | Toroide | Clase Térmica |
|---------------------------|---------|---------------|
| 13 a 17 A | 50/5 | — |
| 15 a 20 A | 60/5 | — |
| 19 a 25 A | 75/5 | Normas IEEE C37-112, IEC 60255-8 |
| 25 a 33 A | 100/5 | — |
| 31 a 42 A | 125/5 | — |
| 38 a 50 A | 150/5 | — |
| 50 a 67 A | 200/5 | — |
| 63 a 83 A | 250/5 | — |
| 75 a 100 A | 300/5 | — |
| 100 a 133 A | 400/5 | — |
| 125 a 167 A | 500/5 | — |
| 150 a 200 A | 600/5 | — |
| 190 a 250 A | 750/5 | — |
| 200 a 260 A | 800/5 | — |
| 250 a 330 A | 1000/5 | — |
| 300 a 400 A | 1200/5 | — |
| 375 a 500 A | 1500/5 | — |
| 500 a 660 A | 2000/5 | — |

## Información de Seguridad

Solo personal técnico calificado con conocimientos en relés de sobrecarga y de la maquinaria a proteger debería realizar la instalación, arranque y mantenimiento del sistema. Hacer caso omiso podría resultar en lesiones a personas y/o daños a los equipos conectados.

## Medidas a Considerar Respecto a la Compatibilidad Electromagnética

Este producto ha sido diseñado para ambiente industrial severo. De ser utilizado en ambiente residencial, el usuario podría requerir algunas medidas en caso de que note algún ruido eléctrico inesperado en artefactos domésticos.

## Diagrama de Conexión

Los cables del motor pasan primero por los orificios del GUCT+.

Terminales de conexión: L1, L2, L3 para 3~, 50/60 Hz.

## Cómo Ordenar GUCT+

| Campo | Opciones |
|-------|----------|
| Programador horario | Disponible |
| Voltaje | 208, 208/220/240 V~ o 480, 440/480 V~ |
| Corriente | 00 - CT Externos |
| Idioma | S - Español, E - Inglés, P - Portugués |

## Nota

Las especificaciones y descripciones mostradas en este documento están sujetas a cambio sin previo aviso.

## Fabricante

**Generación de Tecnología**

Fabricado en la República Bolivariana de Venezuela por GENTE, Generación de Tecnología, C.A., RIF: J-00223173-4

Av. El Buen Pastor cruce con calle Vargas, Edif. Alba, Piso 1, Local 1-A, Boleita Norte, Caracas - Venezuela, Zona Postal 1070.

Telf.: ++(58 212) 237.07.11 / Fax: ++(58 212) 235.24.97

E-mail: genteven@genteca.com.ve / www.genteca.com.ve
