---
title: "Manual de Instalación GUCT+ C-CT"
type: Technical
source: "Manual Instalacion GUCT+ c-CT (3).pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GUCT+"
version_status: "historica"
date_processed: "2026-05-10"
---

# Manual de Instalación GUCT+ C-CT

## 9.3 Ajuste de Eventos

Los modelos GUCT+ tienen las opciones de menú "AJUSTE RELOJ" y "PROG. HORARIO". A continuación se muestra un ejemplo de ajuste de eventos y días feriados.

### EVENTO 01 (ejemplo):
De Martes a Sábado
- ON: 7:30 hrs
- OFF: 16:45 hrs

### FERIADO 01 (ejemplo):
24 de Junio

El procedimiento de programación se realiza a través del menú de navegación utilizando los botones de SELECCIÓN para cambiar entre días (L-Lunes, M-Martes, J-Jueves, V-Viernes, S-Sábado, D-Domingo) e ingresar las horas de encendido (ON) y apagado (OFF).

**Nota:** Para ajustar un nuevo evento o feriado, pulse Y o D para buscar el número a asignar al mismo y luego pulse 9 para ingresarlo. Llegará a la pantalla 7.4.1 (para eventos) ó 7.4.2 (para feriado). Siga los pasos indicados en el ejemplo. Si desea salir, presione SALIR.

---

## ESPECIFICACIONES TÉCNICAS GUCT+

### A) Fuente de Poder

| Parámetro | Especificación |
|-----------|----------------|
| Voltaje de Operación, Ue | 208/220/240 V~ ó 440/480 V~ |
| Límites de Operación de Voltaje Ue | 145 > 312 V~ ó 264 > 672 V~ |
| Consumo Promedio, In | 45 mA |
| Frecuencia Nominal, Fn | 50/60 Hz |
| Frecuencia de Operación | 42 → 70 Hz |
| Modo de Operación | Continuo |

### B) Condiciones Ambientales, Límites de Operación e Instalación

**Normas:**
- IEC 61010-1, IEC 60255-6
- Para EUROPA: IEC 60947-1 LVD & EMC
- Para USA: UL (pendiente), NKCR, Dispositivos Auxiliares UL 508
- Aprobación Europea: CE (pendiente), Dispositivos de Bajo Voltaje IEC 60947-1

| Parámetro | Especificación |
|-----------|----------------|
| Temperatura Ambiental (Operación) | -5 °C a 55 °C (23 °F a 131 °F) |
| Temperatura Ambiental (Almacenaje) | -10 °C a +70 °C (14 °F a 158 °F) |
| Humedad Relativa Máxima | 85% R.H. |
| Resistencia a Vibraciones | Clase 1, Amplitud <0.035mm ó 1G, 10Hz < f < 150Hz (IEC 60255-21-1) |
| Protección a Objetos/Agua | IP20: Protegido contra objetos > 12.5mm, ninguna protección contra agua (IEC 60529) |
| Nivel de Contaminación | Grado 3 (IEC 60255-5) |
| Protección contra Exceso de Voltaje | Categoría III (IEC 60255-5) |
| Voltaje de Aislamiento Nominal | 500V |
| Prueba de Impulso | 5 KV (IEC 60255-5) |
| Prueba Dieléctrica | 2.5 KV @ 50/60 Hz, 1 min (UL 508) |
| Grado de Protección al Fuego de la carcasa | V-0 (UL-94) |
| Material de la Carcasa | Polímeros: LEXAN, ABS, VYDYNE |
| Posiciones de Montaje | Sin Restricciones |
| Tipos de Montaje | Riel DIN Simétrico (DIN 43880), Superficie Plana, Tornillo 3/16" x 1/2" (Tipo NEMA) |
| Tipo de Tornillo de Borneras | Plano M3 |
| Torque de Apretado de Borneras | 5.1 Kg-cm / 4.4 lb-in |
| Cableado de Borneras | 10-18 AWG |
| Cableado en el Sensor de Corriente | @ < 11mm, AWG 4 |
| Medidas | 92 x 91 x 96 (L x A x H) mm |
| Peso | 494 g (1.09 lb) |

### C) Características de Control

| Parámetro | Especificación |
|-----------|----------------|
| Capacidad de los Contactos B300 Pilot Duty (para Circuitos de Control) | 1 A @ 240 V~, 0.5 A @ 480 V~ (UL 508, Sección 139.1) |
| Expectativa de Vida Eléctrica | 100,000 Operaciones |
| Expectativa de Vida Mecánica | 10,000,000 Operaciones |
| Categoría de Uso | AC-15, Capacidad para Cargas > 72 VA (IEC 60947-5-1) |

### D) Ajustes de Rango, Mediciones

| Parámetro | Especificación |
|-----------|----------------|
| Rango de Medición de Voltaje, Um (Modelo 208 V~) | 0 → 312 V~, ±2% precisión |
| Rango de Medición de Voltaje, Um (Modelo 480 V~) | 0 → 672 V~, ±2% precisión |
| Rango de Medición de Corriente, Im | 5% → 333% CT (Modelo EXT CT/5), ±2% precisión |
| Rango de Frecuencia | 45.0 → 70.0 Hz, ±1% |
| Factor Potencia Instantáneo | 0.00 → 1.00, ±8% |
| Potencia Aparente Instantánea, kVA | 0.0 → 999.9 kVA, ±4% |
| Potencia Real Instantánea, kW | 0.0 → 999.9 kW, ±4% |
| Consumo de Energía, kWH | 0 → 999999 kW/H, ±4% |
| Horas de trabajo acumuladas del motor | 0 → 999999 H, ±1% |

### E) Funciones y Algoritmos de Protección

**Protecciones de Voltaje (Rotor bloqueado acelerado):**

| Función | Especificación (208 V~ / 480 V~) |
|---------|----------------------------------|
| Bajo Voltaje (UV) @ Imotor=0 u OC | 165 → 225 / 350 → 460 V~, Ajustable |
| Sobre Voltaje (OV) @ Imotor=0 u OC | 215 → 270 / 460 → 580 V~, Ajustable |
| Umbral Histéresis de Voltaje | 6 / 12 V~ |
| Desbalance de Voltaje (VUB) | 2% → 10%, Ajustable |
| Pérdida de Fase de Voltaje (VSP) | IN: VUB > 33%, OUT: VUB < 28% |
| Frecuencia Nominal | 50 ó 60 Hz, Ajustable |
| Variación de Frecuencia | 2% → 10%, Ajustable |
| Fase Invertida (PR) | Secuencia ABC Normal, Secuencia CBA Invertida |
| Temporizado a la Desconexión por Fase Invertida (PR) | < 1 s |
| Temporizado a la Desconexión por otras Fallas de Voltaje (TD) | 1 → 30 s, Ajustable |
| Temporizado a la Conexión (TC) | 0 → 600 s, Ajustable |
| Temporizado a la Desconexión por VSP | 3 s |
| Modo de Rearme | Automático/Manual, Selección Usuario |
| Tiempo mínimo entre 2 arranques | 50 x Clase Térmica (s) |

**Protecciones de Corriente:**

| Función | Especificación |
|---------|----------------|
| Ajuste Corriente Nominal | (Ver página 4) |
| Ajuste Nivel Sobrecarga (OL) | 5% → 50%, Ajustable |
| Ajuste de Clase Térmica | 5 → 35, Ajustable |
| Ajuste Dinámico Modelo del Motor (Curva Fría/Curva Caliente) | Clase Térmica varía de 1 → 18 de la clase ajustada según IEC 60255-8, según el tiempo de encendido y nivel de carga del motor |
| Tiempo Máximo entre curvas Fría/Caliente | 2 Horas (de 1 a 1/3 ó de 1/3 a 1) (IEC 60255-90) |
| Tiempo Desconexión de Falla por Sobrecarga | Según el nivel de Sobrecarga y Clase ajustada (IEEE Std. 37.112-1996) |
| Umbral de Calor para Falla por Sobrecarga | 100% |
| Desbalance de Corriente (CUB) | CUB > 48% |
| Pérdida de fase por Corriente (CSP) | CUB > 60% |
| Selección del Lado Carga (LR) | SINO |
| Temporizado Desconexión por CSP | 1 s |
| Temporizado Desconexión por CUB | 2 s |
| Opción de Alta Inercia | SI/NO |
| Umbral de calor por Alta Inercia | 400% |
| Temporizado Conexión por Alta Inercia | 20 → 120 s, Ajustable |
| Tiempo de Enfriamiento Máquina Térmica | 50 x Clase Térmica Ajustada (s) |
| Subcarga | SI/NO |
| Tipo Desconexión por Subcarga (UC) | % Inom ó FP (Factor Potencia) |
| Desconexión por Subcarga (%Inom) | 30% → 90%, Ajustable |
| Desconexión por Subcarga (PF) | 0.3 → 0.9, Ajustable |
| Temporizado Desconexión por Subcarga (UC) | 5 → 600 s, Ajustable |
| Temporizado Conexión por Subcarga (UC) | 2 → 500 Min, Ajustable |
| Detección de Tercera (3ª) Falla | SI/NO |
| SN 3 Fallas de Corriente en menos de 105 min | (Según uso) |
| Tiempo Desconexión para 3ª Falla | 3 s |

**Características Programador Horario:**

| Parámetro | Especificación |
|-----------|----------------|
| Ajuste Reloj / Fecha | hh:mm dd/mm/aa |
| Control Prog. Horario | SI/NO, Selección Usuario |
| Núm. Eventos programables | 60, Selección Usuario |
| Núm. Feriados programables | 20, Selección Usuario |

### F) Comunicaciones y Funciones Especiales

| Parámetro | Especificación |
|-----------|----------------|
| Protocolo de Comunicación | MODBUS RTU @ 9600 8N1 |
| Puerto de Comunicación | GIO PORT (*) |
| Rango de Direcciones | 1 → 127 |
| Histórico de Fallas | Reporte de 20 últimas fallas (Datos de Tipo Falla, Valor, Hora, Fecha y Duración) |
| Bloqueo de Parámetros | 0000 Libre, 0001 → 9999 Bloqueado |

(*) Se requiere GIOPlug para la comunicación a través de GIO Port. El GIOPLUG se suministra por separado.

### CT Externos Sugeridos, Según la Corriente Nominal

| Rango de corriente nominal | Toroide |
|---------------------------|---------|
| 13 a 17 A | 50/5 |
| 15 a 20 A | 60/5 |
| 19 a 25 A | 75/5 |
| 25 a 33 A | 100/5 |
| 31 a 42 A | 125/5 |
| 38 a 50 A | 150/5 |
| 50 a 67 A | 200/5 |
| 63 a 83 A | 250/5 |
| 75 a 100 A | 300/5 |
| 100 a 133 A | 400/5 |
| 125 a 167 A | 500/5 |
| 150 a 200 A | 600/5 |
| 190 a 250 A | 750/5 |
| 200 a 260 A | 800/5 |
| 250 a 330 A | 1000/5 |
| 300 a 400 A | 1200/5 |
| 375 a 500 A | 1500/5 |
| 500 a 660 A | 2000/5 |

### Cómo Ordenar GUCT+

**Formato:** G[VOLTAJE]-[CORRIENTE]-[PROGRAMADOR HORARIO]-[CONTROL]-[IDIOMA]

- **Voltaje:** 208 (208/220/240 V~) ó 480 (440/480 V~)
- **Corriente:** 00 (CT Externos)
- **Programador Horario:** S (Sí)
- **Control:** (Voltaje y/o Corriente según se requiera)
- **Idioma:** S (Español), E (Inglés), P (Portugués)

### G) Compatibilidad Electromagnética para Ambiente Industrial Severo, Estándares de Inmunidad y Emisiones

| Parámetro | Norma |
|-----------|-------|
| Descarga Electrostática | IEC 61000-4-2 |
| Inmunidad a Ruido Eléctrico Radiado | IEC 61000-4-3 |
| Transientes Rápidas | IEC 61000-4-4 |
| Picos de Alta Energía | IEC 61000-4-5 |
| Perturbaciones Conducidas | IEC 61000-4-6 |
| Campos Magnéticos | IEC 61000-4-8 |
| Reducciones e Interrupciones de Voltaje | IEC 61000-4-11 |
| Armónicos | IEC 61000-4-13 |
| Fluctuaciones de Voltaje | IEC 61000-4-14 |
| Desbalance Trifásico | IEC 61000-4-27 |
| Variaciones de Frecuencia | IEC 61000-4-28 |

### Curva Fría de Disparo

**Clases Térmicas disponibles:**
- Clase 5
- Clase 10
- Clase 15
- Clase 20
- Clase 25
- Clase 30

**Normas de referencia:** IEEE C37-112, IEC 60255-8

**Nota:** Curva Caliente = Curva Fría / 3

---

## Información del Fabricante

**Diseñado y Fabricado por:**
GENTECA - Generación de Tecnología, C.A.
RIF: J-00223173-4
Av. El Buen Pastor cruce con Calle Vargas, Edif. Alba, Piso 1, Local I-A
Boleita Norte, Caracas - Venezuela, Zona Postal 1070

**Contacto:**
- Tel: ++(58 212) 237.07.11
- Fax: ++(58 212) 235.24.97
- Email: genteven@genteca.com.ve
- Web: www.genteca.com.ve

Fabricado en la República Bolivariana de Venezuela

**Nota:** Las especificaciones y descripciones mostradas en este documento están sujetas a cambio sin previo aviso.
