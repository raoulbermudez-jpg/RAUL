---
title: "Manual de Instalación GSPT - Especificaciones Técnicas"
type: Technical
source: "GD-MAN-GSPT-01-V1.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GSPT"
version_status: "vigente"
date_processed: "2026-05-10"
---

# Especificaciones Técnicas GSPT

## A) Fuente de Poder

| Parámetro | Especificación | Unidad |
|-----------|----------------|--------|
| Voltaje de Operación, Ue | 208/220/240, 400, 440/480, Otros | VAC |
| Límites de Operación de Voltaje Ue | 145-312, 228-532, 264-672 | VAC |
| Consumo Promedio, In | 45 | mA |
| Rango de Frecuencia | 45.0-70.0 | Hz |
| Frecuencia Nominal, Fn | 50/60 | Hz |
| Frecuencia de Operación | 42-70 | Hz |
| Modo de Operación | Continuo | — |

### Parámetros Medidos

| Parámetro | Rango | Tolerancia |
|-----------|-------|-----------|
| Factor Potencia Instantáneo | 0.00-1.00 | 8% |
| Potencia Aparente Instantánea | 0.0-999.9 | kVA (4%) |
| Potencia Real Instantánea | 0.0-999.9 | kW (4%) |
| Consumo de Energía | 0-999999 | kWH (4%) |
| Horas de trabajo acumuladas del motor | 0-999999 | H (1%) |

## B) Condiciones Ambientales, Límites de Operación e Instalación

| Aspecto | Especificación | Norma/Estándar |
|--------|----------------|-----------------|
| Normas para Europa | LVD & EMC | — |
| Normas para USA | UL (pendiente), NKCR, UL508 | — |
| Dispositivos de Bajo Voltaje | IEC60947-1 | — |
| Aprobación Europea CE | Pendiente | — |
| Temperatura Ambiental (Operación) | -5°C a 55°C (23°F a 131°F) | — |
| Temperatura Ambiental (Almacenamiento) | -10°C a +70°C (14°F a 158°F) | — |
| Humedad Relativa Máxima | 85% R.H. | — |
| Resistencia a Vibraciones | Clase 1 | — |
| Protección a Objetos/Agua | IP20 | IEC 60529 |
| Nivel de Contaminación | Grado 3 | IEC 60259 |
| Protección contra Exceso de Voltaje | Categoría II | IEC 60255 |
| Voltaje Mínimo de Sostenimiento | 500 | V |
| Prueba de Impulso | — | IEC 60255 |
| Prueba Dieléctrica | 2.5 kV 50/60 Hz @ tmin | UL 508 |
| Grado de Protección al Fuego de la Carcaza | V-0 | UL-94 |
| Material de la Carcasa | Polímeros: LEXAN o 2.10 | — |
| Posiciones de Montaje | 7/15° | — |
| Tipos de Montaje | DIN métrico | DIN 43880 |
| Montaje | Superficie Plana, Tornillo 3/16" x 1/2" | — |
| Tipo de Tornillo de Borneras | Plano M3 | — |
| Torque de Apretado de Borneras | 5.1 Kg-cm / 4.4 Ib-in | — |
| Cableado de Borneras | 10-18 AWG | — |
| Cableado en el Sensor de Corriente | < 11 mm | AWG 4 |
| Dimensiones (L x A x H) | 2 x 91 mm | — |

## C) Características de Control

| Característica | Especificación | Estándar |
|----------------|----------------|----------|
| Capacidad de los Contactos | 8300 Pilot Duty | UL 508 |
| Contactos para Circuitos de Control | 1A @ 240 VAC, 0.54 @ 480 VAC | — |
| Expectativa de Vida Eléctrica | 100,000 Operaciones | — |
| Expectativa de Vida Mecánica | 10,000,000 Operaciones | — |
| Categoría de Uso | AC-15, Capacidad para Cargas > 72 VA | IEC 60947-5-1 |

## D) Ajustes de Rango, Mediciones

| Parámetro | Modelo de Voltaje | Modelo de Corriente |
|-----------|-------------------|-------------------|
| | 208 | 400 | 480 | 04 | 12 | 32 | 80 |
| Rango de Medición Um | 0-312 | 0-582 | 0-672 | — | — | — | — |
| Rango de Medición de Corriente Im | — | — | — | 1.5-40 | 0.3-125 | 1-320 | 2.5-800 |

## E) Funciones y Algoritmos de Protección

### Protección de Voltaje

| Parámetro | Modelo 208 | Modelo 400 | Modelo 480 | Ajuste |
|-----------|-----------|-----------|-----------|--------|
| Subtensión (UV) | 165-225 | 330-450 | 385-540 | Ajustable |
| Sobretensión (OV) | 215-270 | 420-480 | 460-580 | Ajustable |
| Umbral Histéresis de Voltaje | 6 | 10 | 12 | VAC |

### Desbalance y Pérdida de Voltaje

| Función | Especificación |
|---------|----------------|
| Desbalance de Voltaje (VUB) | 2%-10% Ajustable |
| Pérdida de Fase de Voltaje (VSP) | IN: VUB > 33%, OUT: VUB < 28% |
| Frecuencia Nominal | 50/60 Hz Ajustable |
| Variación de Frecuencia | 2%-10% Ajustable |

### Fase Invertida y Temporización

| Función | Especificación |
|---------|----------------|
| Fase Invertida (PR) | Secuencia ABC Normal, Secuencia CBA Invertida |
| Temporizado a la Desconexión por Fase Invertida (PR) | < 1 seg |
| Temporizado a la Desconexión por otras Fallas de Voltaje (TD) | 1-30 seg Ajustable |
| Temporizado a la Conexión (TC) | 0-600 seg Ajustable |
| Temporizado a la Desconexión por (TD) por 3 fallas | — seg |
| Modo de Rearme | Automático/Manual Selección Usuario |
| Tipo NEMA | 0.13 |

### Protección de Corriente

| Parámetro | Modelo 04 | Modelo 12 | Modelo 32 | Modelo 80 |
|-----------|-----------|-----------|-----------|-----------|
| Ajuste Corriente Nominal | 1.5-4 | 3.5-12.5 | 10-92 | 25-80 | A |
| Ajuste Nivel Sobrecarga (OL) | 5%-50% Ajustable | — | — | — |
| Temporizado conexión por sobrecarga (OC) | 10-60 Minutos Ajustable | — | — | — |

### Clase Térmica y Ajuste Dinámico

| Función | Especificación |
|---------|----------------|
| Clase Térmica | 10 |
| Ajuste Dinámico (Curva Fría/Curva Caliente) | Clase Térmica varía de 1-1/3 de la clase 10 según el tiempo de encendido y nivel de carga del motor |
| Tiempo Máximo entre curvas Fría/Caliente | 2 Horas (de 1 a 1/3 ó de 1/3 a 1) |
| Umbral de Calor para Disparo por Sobrecarga | 100% |

### Desbalance y Pérdida de Corriente

| Función | Especificación |
|---------|----------------|
| Desbalance de Corriente (CUB) | CUB > 48% |
| Pérdida de fase por Corriente (CSP) | CUB > 60% |
| Detección Rotor Bloqueado Acelerado (LR) | CONTINUO |
| Temporizado Desconexión por CSP | 3 seg |
| Temporizado Desconexión por CUB | 4 seg |

### Protección por Subcarga

| Función | Especificación |
|---------|----------------|
| Subcarga | SI/NO Selección Usuario |
| Tipo Desconexión por Subcarga (UC) | Detección relativa a corriente Nominal Inom |
| Temporizado Desconexión por Subcarga (UC) | 5-600 seg Ajustable |
| Temporizado Conexión por Subcarga (UC) | 2-500 Min. Ajustable |

### Protección por Tercera Falla

| Función | Especificación |
|---------|----------------|
| Detección de Tercera (3ª) Falla | SI/NO Selección Usuario |
| Desconexión permanente por Tercera (3ª) Falla | 3 Fallas de Corriente en menos de 30 min de Duración |
| Tiempo desconexión para Rotor bloqueado acelerado | 3 seg |

### Protección Adicional

| Función | Especificación |
|---------|----------------|
| Protección adicional para bombas sumergibles | — |
| Máximo número de arranques por hora | SI/NO Selección; Máximo automático hasta 12 según HP; Mínimo seleccionable por usuario |
| Tiempo mínimo entre arranques | 1-10 Min. |

## F) Funciones y Algoritmos de Protección (Comunicación)

| Parámetro | Especificación |
|-----------|----------------|
| Protocolo de Comunicación | MODBUS RTU @ 9600 8N1 |
| Puerto de Comunicación | Puerto GIO PORT (*) |
| Rango de Direcciones | 1-127 |

### Histórico de Fallas

| Función | Especificación |
|---------|----------------|
| Reporte de 80 últimas fallas | Datos de Tipo Falla, Valor, Hora, Fecha y Tiempo |
| Retención de parámetros configurados | Ajustes de voltaje, Ajustes de corrientes, modo de rearme |
| Bloqueo de Parámetros | 0000 Libre, 0001-9999 Bloqueado |

(*) Se requiere GIO PLUG para la comunicación a través de GIO Port. El GIO PLUG se suministra por separado.

## G) Compatibilidad Electromagnética para Ambiente Industrial Severo

### Estándares de Inmunidad y Emisiones

| Aspecto | Estándar |
|--------|----------|
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

## Curva Fría - Curva Caliente: Números Permitidos de Arranques por Hora

Cuando el usuario selecciona el límite automático de máximo número de arranques por hora, el GSPT predispone los siguientes valores, de acuerdo al motor instalado:

| HP | Sph (Arranques/Hora) |
|----|---------------------|
| 1 | 12 |
| 1.5 | 9 |
| 2 | 7 |
| 3 | 6 |
| 5 | 5 |
| 7.5 | 4 |
| 10 | 4 |
| 15 | 3 |
| 20 | 3 |
| 25 | 2 |
| 30 | 2 |
| 40 | 2 |
| 50 | 2 |
| 60 | 1 |
| 75 | 1 |
| 100 | 1 |
| 125 | 1 |
| 150 | 1 |
| 200 | 1 |

Donde:
- **HP** = Potencia nominal del motor instalado
- **Sph** = Cantidad máxima de arranques permitidos por hora
- **Inom** = Valor de corriente calibrada por el usuario en el SUB INC GSPT

Inom es lo mismo que la corriente del motor con su máxima carga FLA tal como se muestra en los ajustes del producto.

## Cómo Ordenar GSPT de Acuerdo a sus Necesidades

| Opción | Especificación |
|--------|----------------|
| Voltaje | 208 (208/220/240 VAC), 480 (440/480 VAC) |
| Corriente | 04 (1-4A), 12 (3.5-12.5A), 32 (10-92A), 80 (25-80A) |
| Opciones | S (Estándar), R (Con Medición de Temperatura) |
| Idioma | S (Español), E (Inglés) |

## Información de Contacto y Distribución

**Fabricado y distribuido por:** GENTECA, GENERACIÓN DE TECNOLOGÍA, CA.  
R.I.F.: J-00223173-4  
Av. El Buen Pastor, Cruce con Calle Vargas, Edificio Alba, Piso 1, Local 1-A, Boleíta Norte, Caracas, Estado Miranda, Zona Postal 1070, REPÚBLICA BOLIVARIANA DE VENEZUELA  
Tlf.: +(58)(212) 237.0711 (Master)  
Fax: +(58)(212) 235.2497  
E-mail: genteven@genteca.com.ve  
Página web: www.genteca.com.ve

**Distribuidores:**

- **Colombia:** REDES ELECTRICAS, S.A., NIT: 860.062.958-6, Calle 18, N° 25-60, Paloquemao, Bogotá, Tlf.: +(57) 1-3647000, e-mail: gerencia.ventas@redeselectricas.com

- **México:** DUIDA S.A. DE CV., R.F.C. DUIO90113MK5, Fernando Zárraga 55, Ciudad Satélite, Naucalpan de Juárez, Edo. de México, C.P. 53100, Tlf.: +(55) 5572-9200, e-mail: contacto@exceline.com.mx, página web: www.exceline.com.mx

- **Panamá:** COMAR TRADING INC., R.U.C. 319589-50908-21 DV-06, final Calle 18, Edif. 44, local 4, Zona Libre de Colón, Apartado Postal 030200900, Tlf.: +(507) 433-1043, Fax: +(507) 433-2837

---

**NOTA:** Las especificaciones y descripciones mostradas en este documento están sujetas a cambio sin previo aviso.
