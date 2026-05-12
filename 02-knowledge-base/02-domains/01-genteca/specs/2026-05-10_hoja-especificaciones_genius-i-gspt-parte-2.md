---
title: "GSPT - Especificaciones Técnicas"
type: Technical
source: "I_GSPT.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "GSPT"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GSPT ESPECIFICACIONES TÉCNICAS

## A) Fuente de Poder

| Parámetro | Especificación | Unidad | Tolerancia |
|-----------|----------------|--------|-----------|
| Voltaje de Operación, Ue | 208/220/240, 400, 440/480 | VAC | — |
| Límites de Operación de Voltaje Ue | 145-312 (228-532, 264-672) | VAC | — |
| Consumo Promedio, In | 45 | mA | — |
| Frecuencia Nominal, Fn | 50/60 | Hz | — |
| Frecuencia de Operación | 42-70 | Hz | — |
| Rango de Frecuencia | 45.0-70.0 | Hz | 1% |
| Factor Potencia Instantáneo | 0.00-1.00 | — | 8% |
| Potencia Aparente Instantánea | 0.0-999.9 | kVA | 4% |
| Potencia Real Instantánea | 0.0-999.9 | kW | 4% |
| Consumo de Energía | 0-999999 | kWH | 4% |
| Horas de trabajo acumuladas del motor | 0-999999 | H | 1% |
| Modo de Operación | Continuo | — | — |

## B) Condiciones Ambientales, Límites de Operación e Instalación

| Parámetro | Especificación |
|-----------|----------------|
| Normas, Requisitos para EUROPA | EAN LVD & EMC |
| Normas, Requisitos para USA | UL (pendiente), NKCR, UL508 |
| Aprobación Europea CE | Pendiente |
| Dispositivos de Bajo Voltaje | IEC60947-1 |
| Temperatura Ambiental (Operación) | -5 °C a 55 °C (23 °F a 131 °F) |
| Temperatura Ambiental (Almacenamiento) | -10 °C a +70 °C (14 °F a 158 °F) |
| Humedad Relativa Máxima | 85% R.H. |
| Resistencia a Vibraciones | Clase 1, Amplitud 0.1 mm, 10 Hz-1 kHz |
| Nivel de Contaminación | Grado 3, IEC 60255-5 |
| Protección contra Excesos de Voltaje | Categoría III, IEC 60255-5 |
| Voltaje Mínimo | 500 VAC, 27 A |
| Prueba de Impulso | 5 kV |
| Prueba Dieléctrica | 2.5 kV, 50/60 Hz @ 1 min, UL508 |
| Grado de Protección al Fuego de la carcasa | V-0, UL-94 |
| Material de la Carcasa | Policarbonato/ABS |
| Posiciones de Montaje | Sin Restricciones |
| Tipos de Montaje | Niel DIN Siemon DIN 43880 |
| Montaje | Superficie Plana, Tornillo 3/16" x 1/2", Tipo NEMA |
| Tipo de Tornillo de Borneras | Plano M3 |
| Torque de Apretado de Borneras | 5.1 kg-cm / 4.4 lbf·in |
| Cableado de Borneras | 10-18 AWG |
| Cableado en el Sensor de Corriente | O ≤ 11 mm, AWG 4 |
| Dimensiones | 92 x 91 x 96 (L x A x H) mm |

## C) Características de Control

| Parámetro | Especificación |
|-----------|----------------|
| Capacidad de los Contactos | 8300 Pilot Duty, UL 508 |
| Capacidad para Circuitos de Control | 1 A @ 240 VAC, 0.5 A @ 480 VAC |
| Expectativa de Vida Eléctrica | 100,000 Operaciones |
| Expectativa de Vida Mecánica | 10,000,000 Operaciones |
| Categoría de Uso | AC-15, Capacidad para Cargas > 72 VA, IEC 60947-5-1 |

## D) Ajustes de Rango, Mediciones

### Según Modelo de Voltaje (208, 400, 480 V)

| Parámetro | 208 V | 400 V | 480 V | Unidad |
|-----------|-------|-------|-------|--------|
| Bajo Voltaje (LW) @ Imotor=0 UOC | 185-225 | 380-450 | 460 | VAC |
| Sobre Voltaje (OV) @ Imotor=0 UOC | 215-270 | 420-480 | 460-580 | Ajustable |
| Umbral Histéresis de Voltaje | 6, 10, 12 | — | — | VAC |

### Según Modelo de Corriente (04, 12, 32, 80 A)

| Parámetro | Especificación |
|-----------|----------------|
| Frecuencia Nominal | 50/60 Hz, Ajustable |
| Variación de Frecuencia | 2%-10%, Ajustable |
| Pérdida de Fase de Voltaje (VSP) | IN: VUB > 39%, OUT: VUB < 28% |
| Fase Invertida (PR) | Secuencia ABC Normal, Secuencia CBA Invertida, Temporizado a la Desconexión < 1 seg |
| Temporizado a la Desconexión por Fallas de Voltaje (TD) | 1-30 seg, Ajustable |
| Temporizado a la Conexión (TC) | 0-600 seg, Ajustable |
| Ajuste Corriente Nominal | 15-41 A (modelo 04), 35-125 A (modelo 12), 10-32 A, 25-80 A |
| Ajuste Nivel Sobrecarga (OL) | 5%-50%, Ajustable |
| Temporizado Conexión por Sobrecarga (OC) | 10-60 Minutos, Ajustable |
| Clase Térmica | 10, IEC 60255-9 |
| Ajuste Dinámico Modelo del Motor | Clase Térmica varía 1-1/3 según tiempo de encendido y nivel de carga |
| Tiempo Máximo entre Curvas Fría/Caliente | 2 Horas, IEC 60255-8-1999 |
| Umbral de Calor para Parada por Sobrecarga | 100% |
| Desbalance de Corriente (CUB) | CUB > 48% |
| Pérdida de Fase por Corriente (CSP) | CUB > 60% |
| Detección Rotor Bloqueado Acelerado (LR) | Continuo |
| Temporizado Desconexión por CSP | 3 seg |
| Temporizado Desconexión por CUB | 4 seg |
| Tipo Desconexión por Subcarga (UC) | Detección relativa a corriente Nominal Inom, Selección Usuario |
| Ajuste Nivel Subcarga (UC) | 30%-90%, Ajustable |
| Temporizado Desconexión por Subcarga (UC) | 5-600 seg, Ajustable |
| Temporizado Conexión por Subcarga (UC) | 2-500 min, Ajustable |
| Detección de Tercera (3ª) Falla | SI/NO, Selección Usuario |
| Desconexión Permanente por Tercera (3ª) Falla | 3 Fallas de Corriente en menos de 30 min |
| Tiempo Desconexión para Rotor Bloqueado Acelerado | 3 seg |
| Protección Adicional para Bombas Sumergibles | SI/NO, Selección Usuario |
| Máximo Número de Arranques por Hora | Automático hasta 12 según HP, Mínimo Ajustable, NEMA MG10 |
| Número de Arranques Máximo por Hora | 0000: Libre, 0001-9999: Selección Usuario, Bloqueado Usuario |
| Tiempo Mínimo entre Arranques | 1-10 min, NEMA MG10 |

## E) Funciones y Algoritmos de Protección

| Parámetro | Especificación |
|-----------|----------------|
| Modo de Rearme | Automático, Manual, Usuario |
| Retención de Parámetros | Ajustes de voltaje, Ajustes de corrientes, Modo de rearme configurados cuando ocurrieron las fallas |

### Tabla: Números Permitidos de Arranques por Hora (Según NEMA MG10)

| HP | Arranques por Hora |
|----|--------------------|
| 1 | 8 |
| 1.5 | 8 |
| 2 | 8 |
| 3 | 8 |
| 5 | 8 |
| 7.5 | 8 |
| 10 | 8 |
| 15 | 6 |
| 20 | 6 |
| 25 | 6 |
| 30 | 5 |
| 40 | 5 |
| 50 | 4 |
| 60 | 4 |
| 75 | 3 |
| 100 | 3 |
| 125 | 2 |
| 150 | 2 |
| 200 | 2 |

## F) Funciones y Algoritmos de Protección (Continuación)

| Parámetro | Especificación |
|-----------|----------------|
| Protocolo de Comunicación | MODBUS RTU @ 9600 8N1 |
| Puerto de Comunicación | Puerto GIO PORT (*) |
| Rango de Direcciones | 1-127 |
| Histórico de Fallas | Reporte de 80 últimas fallas |
| Tipo Falla, Valor, Hora, Fecha y Tiempo | Usuario |
| Bloqueo de Parámetros | Usuario |

(*) Se requiere GIO PLUG para la comunicación a través de GIO Port. El GIO PLUG se suministra por separado.

## G) Compatibilidad Electromagnética para Ambiente Industrial Severo, Estándares de Inmunidad y Emisiones

| Parámetro | Estándar |
|-----------|----------|
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

## Cómo Ordenar GSPT de Acuerdo a sus Necesidades

Formato de Código: **GSPT — [VOLTAJE] — [CORRIENTE] — [OPCIONES] — [IDIOMA]**

### Opciones:

| Campo | Opciones |
|-------|----------|
| Voltaje | 208 (208/220/240 VAC), 480 (440/480 VAC) |
| Corriente | 04 (1-4 A), 12 (4-12 A), 32 (10-32 A), 80 (25-80 A) |
| Opciones | S (Estándar), R (Con Medición de Temperatura) |
| Idioma | S (Español), E (Inglés) |

## Información de Contacto

**Genteca - Generación de Tecnología**

Avenida El Buen Pastor, cruce con calle Vargas, Edificio Alba, Piso 1, Local 1-A, Boleita Norte, Caracas - Venezuela, Zona Postal 1070.

- Teléfono: ++(58-212) 237.07.11 (Master) / 34.77 / 11.51
- Fax: ++(58-212) 235.24.97
- E-mail: genteven@genteca.com.ve
- Web: www.genteca.com.ve

P.O. Box 28537, Miami, FL 33102, USA.

---

**Nota:** Las especificaciones y descripciones mostradas en este documento están sujetas a cambio sin previo aviso.
