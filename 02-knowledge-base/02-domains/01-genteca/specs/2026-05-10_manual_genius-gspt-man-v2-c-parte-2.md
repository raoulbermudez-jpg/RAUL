---
title: "GSPT Manual de Instalación - Especificaciones Técnicas"
type: Technical
source: "GSPT_MAN-V2_C.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GSPT"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GSPT Especificaciones Técnicas

## A) Fuente de Poder

| Parámetro | 208/220/240 VAC | 400 VAC | 440/480 VAC |
|-----------|-----------------|---------|------------|
| Voltaje de Operación, Ue | 208/220/240 | 400 | 440/480 |
| Límites de Operación de Voltaje Ue | 145–312 | 228–532 | 264–672 |
| Consumo Promedio, In | 45 mA | — | — |
| Frecuencia Nominal, Fn | 50/60 Hz | — | — |
| Frecuencia de Operación | 42–70 Hz | — | — |
| Modo de Operación | Continuo | — | — |

## B) Condiciones Ambientales, Límites de Operación e Instalación

| Ítem | Especificación | Norma/Referencia |
|-----|----------------|------------------|
| **b.1** | Normas para EUROPA: IEC61010-1, IEC60255-6, IEC60947-1, LVD y EMC | — |
| **b.2** | Normas para USA: UL (pendiente), NKCR, Dispositivos Auxiliares UL508 | — |
| **b.3** | Aprobación Europea: CE (pendiente), Dispositivos de Bajo Voltaje IEC60947-1 | — |
| **b.4** | Temperatura Ambiental (Operación) | 5–55 °C (23–131 °F) |
| **b.5** | Temperatura Ambiental (Almacenaje) | -10–+70 °C (14–158 °F) |
| **b.6** | Humedad Relativa Máxima | 85% R.H. |
| **b.7** | Resistencia a Vibraciones | Clase 1, Amplitud <0.035 mm, 1 G, 10 Hz < f < 150 Hz | IEC 60255-21-1 |
| **b.8** | Protección a Objetos/Agua (IP20) | Protegido contra objetos >12.6 mm, sin protección contra agua | IEC 60529 |
| **b.9** | Nivel de Contaminación | Grado 3 | IEC 60255-5 |
| **b.10** | Protección contra Exceso de Voltaje | Categoría III | IEC 60255-5 |
| **b.11** | Voltaje de Aislamiento Nominal | 500 V | UL |
| **b.12** | Prueba de Impulso | 5 kV | IEC 60255-5 |
| **b.13** | Prueba Dieléctrica | 2.5 kV, 50/60 Hz, 1 min | UL 508 |
| **b.14** | Grado de Protección al Fuego de la Carcaza | V-0 | UL-94 |
| **b.15** | Material de la Carcasa | Polímeros: LEXAN, ABS, VYDYNE | — |
| **b.16** | Posiciones de Montaje | Sin Restricciones | — |
| **b.17** | Tipos de Montaje | Riel DIN Simétrico IEC 715, DIN 43880; Superficie Plana, Tornillo 3/16"×1/2" Tipo NEMA | — |
| **b.18** | Tipo de Tornillo de Borneras | Plano M3 |
| **b.18** | Torque de Apretado de Borneras | 5.1 kg-cm / 4.4 lb-in | — |
| **b.19** | Cableado de Borneras | 10–18 AWG | — |
| **b.19** | Cableado en el Sensor de Corriente | P <1 mm, AWG 4 | — |
| **b.20** | Medidas | 92 × 91 × 96 (L×A×H) mm | — |
| **b.21** | Peso | 494 g (1.09 lb) | — |

## C) Características de Control

| Ítem | Especificación | Referencia |
|-----|----------------|-----------|
| **c.1** | Capacidad de los Contactos (para Circuitos de Control) | 1 A @ 240 VAC, 0.5 A @ 480 VAC, Pilot Duty UL 508 | Sección 139.1 |
| **c.2** | Expectativa de Vida Eléctrica | 100,000 Operaciones | — |
| **c.3** | Expectativa de Vida Mecánica | 10,000,000 Operaciones | — |
| **c.4** | Categoría de Uso | AC-15, Capacidad para Cargas >72 VA | IEC 60947-5-1 |

## D) Ajustes de Rango, Mediciones

| Ítem | 208 | 400 | 480 | Precisión |
|-----|-----|-----|-----|-----------|
| **d.1** Rango de Medición de Voltaje, Um | 0–312 | 0–532 | 0–672 | ±2% |
| **d.2** Rango de Medición de Corriente, Im | 04–12 A | 1.5–40, 03–125 | 32–800 | ±4% |

| Ítem | Rango | Tolerancia |
|-----|-------|-----------|
| **d.3** | Rango de Frecuencia | 45.0–70.0 Hz | ±1% |
| **d.4** | Factor Potencia Instantáneo | 0.00–1.00 | ±8% |
| **d.5** | Potencia Aparente Instantánea (kVA) | 0.0–999.9 kVA | ±4% |
| **d.6** | Potencia Real Instantánea (kW) | 0.0–999.9 kW | ±4% |
| **d.7** | Consumo de Energía (kWh) | 0–999,999 kW/h | ±4% |
| **d.8** | Horas de Trabajo Acumuladas del Motor | 0–999,999 H | ±1% |

## E) Funciones y Algoritmos de Protección

### Según Modelo de Voltaje (208/400/480 VAC)

| Ítem | 208 | 400 | 480 | Ajuste |
|-----|-----|-----|-----|--------|
| **e.1** | Bajo Voltaje (UV) @ Imotor=0 UOC | 165–225 | 320–380 | 350–460 | Ajustable |
| **e.2** | Sobre Voltaje (OV) @ Imotor=0 UOC | 215–270 | 420–480 | 460–580 | Ajustable |
| **e.3** | Umbral Histéresis de Voltaje | 6 | 10 | 12 VAC | — |
| **e.4** | Desbalance de Voltaje (VUB) | 2%–10% | Ajustable | — |
| **e.5** | Pérdida de Fase de Voltaje (VSP) | IN VUB >33%, OUT VUB <28% | — |
| **e.6** | Frecuencia Nominal | 50, 60 Hz | Ajustable | — |
| **e.7** | Variación de Frecuencia | 2%–10% | Ajustable | — |
| **e.8** | Fase Invertida (PR) | Secuencia ABC Normal, Secuencia CBA Invertida | — |
| **e.9** | Temporizado a la Desconexión por Fase Invertida (PR) | 1–59 seg | Ajustable |
| **e.10** | Temporizado a la Desconexión por Otras Fallas de Voltaje (TD) | 1–30 seg | Ajustable |
| **e.11** | Temporizado a la Conexión (TC) | 0–600 seg | Ajustable |
| **e.12** | Temporizado a la Desconexión por VSP (TD) | 3 seg | — |
| **e.13** | Modo de Rearme | Automático/Manual | Según Norma |

### Según Modelo de Corriente (04/12/32/80 A)

| Ítem | 04 | 12 | 32 | 80 | Ajuste |
|-----|----|----|----|----|--------|
| **e.14** | Ajuste Corriente Nominal | 1.5–4 | 3.5–12.5 | 10–32 | 25–80 A | — |
| **e.15** | Ajuste Nivel Sobrecarga (OL) | 5%–50% | Ajustable | — |
| **e.15b** | Temporizado Conexión por Sobrecarga (OC) | 10–60 Minutos | Ajustable | — |
| **e.16** | Clase Térmica | 10 | — |
| **e.17** | Ajuste Dinámico Modelo de Motor (Curva Fría/Caliente) | Clase Térmica varía de 1–18 de la clase 10 según tiempo de encendido y nivel de carga del motor | IEC 60955-8 |
| **e.18** | Tiempo Máximo entre Curvas Fría/Caliente | 2 Horas (de 1 a 1/3 ó de 1/3 a 1) | IEC 60255-8-1990 |
| **e.19** | Tiempo Desconexión de Falla por Sobrecarga Clase 10 | Según el nivel de Sobrecarga | IEEE Std. 037.112, 1996 |
| **e.20** | Umbral de Calor para Falla por Sobrecarga | 100% | — |
| **e.21** | Desbalance de Corriente (CUB) | CUB >48% | — |
| **e.22** | Pérdida de Fase por Corriente (CSP) | CUB >60% | — |
| **e.23** | Detección Rotor Bloqueado Acelerado (LR) | Continuo | — |
| **e.24** | Temporizado Desconexión por CSP | 3 seg | — |
| **e.25** | Temporizado Desconexión por CUB | 4 seg | — |
| **e.26** | Subcarga | SI/NO | Selección Usuario |
| **e.27** | Tipo Desconexión por Subcarga (UC) | Detección relativa a corriente Nominal Inom | Selección Usuario |
| **e.28** | Ajuste Nivel Subcarga (UC) | 30%–90% | Ajustable |
| **e.29** | Temporizado Desconexión por Subcarga (UC) | 5–600 seg | Ajustable |
| **e.30** | Temporizado Conexión por Subcarga (UC) | 2–500 min | Ajustable |
| **e.31** | Detección de Tercera (3ª) Falla | SI/NO | Selección Usuario |
| **e.32** | Desconexión Permanente por Tercera (3ª) Falla | 3 Fallas de Corriente en menos de 30 min | IEEE Std 037.110-1996 |
| **e.33** | Tiempo Desconexión para Rotor Bloqueado Acelerado | 3 seg | — |
| **e.34** | Protección Adicional para Bombas: Máximo Número de Arranques por Hora | Máximo automático hasta 12 según HP; Mínimo 1 min, seleccionable por usuario | NEMA MG10 |
| **e.36** | Tiempo Mínimo entre Arranques | 1–10 min | — |

### Histórico de Fallas

| Ítem | Especificación | Referencia |
|-----|----------------|-----------|
| **f.4** | Reporte de 80 Últimas Fallas (Datos de Tipo Falla, Valor, Hora, Fecha y Tiempo de Duración) | Ver Manual Usuario |

### Retención de Parámetros

| Ítem | Especificación | Referencia |
|-----|----------------|-----------|
| **1.5** | Retención de Parámetros: Ajustes de Voltaje, Ajustes de Corrientes, Modo de Rearme, cuándo ocurrieron las fallas | Ver Manual Usuario |
| **1.6** | Bloqueo de Parámetros | 0000 Libre, 0001–9999 Bloqueado | Selección Usuario |

## F) Funciones y Algoritmos de Protección (Comunicación)

| Ítem | Especificación | Referencia |
|-----|----------------|-----------|
| **f.1** | Protocolo de Comunicación | MODBUS RTU @ 9600 8N1 | Ver Manual Usuario |
| **f.2** | Puerto de Comunicación | Puerto GIO PORT (*) | Ver Manual Usuario |
| **f.3** | Rango de Direcciones | 1–127 | — |

*(*) Se requiere GIO PLUG para la comunicación a través de GIO Port. El GIO PLUG se suministra por separado.

## G) Compatibilidad Electromagnética para Ambiente Industrial Severo

| Ítem | Estándar de Inmunidad/Emisión |
|-----|-------------------------------|
| **g.1** | Descarga Electrostática | IEC 61000-4-2 |
| **g.2** | Inmunidad a Ruido Eléctrico Radiado | IEC 61000-4-3 |
| **g.3** | Transientes Rápidas | IEC 61000-4-4 |
| **g.4** | Picos de Alta Energía | IEC 61000-4-5 |
| **g.5** | Perturbaciones Conducidas | IEC 61000-4-6 |
| **g.6** | Campos Magnéticos | IEC 61000-4-8 |
| **g.7** | Reducciones e Interrupciones de Voltaje | IEC 61000-4-11 |
| **g.8** | Armónicos | IEC 61000-4-13 |
| **g.9** | Fluctuaciones de Voltaje | IEC 61000-4-14 |
| **g.10** | Desbalance Trifásico | IEC 61000-4-27 |
| **g.11** | Variaciones de Frecuencia | IEC 61000-4-28 |

## Máximo Número de Arranques por Hora según Potencia (HP)

Cuando el usuario selecciona el límite automático de máximo número de arranques por hora, el GSPT predispone los siguientes valores de acuerdo al motor instalado:

| HP | Máx. Arranques por Hora (Sph) |
|----|------|
| 1 | 20 |
| 1.5 | 20 |
| 2 | 20 |
| 3 | 20 |
| 5 | 15 |
| 7.5 | 15 |
| 10 | 12 |
| 15 | 10 |
| 20 | 8 |
| 25 | 8 |
| 30 | 6 |
| 40 | 6 |
| 50 | 5 |
| 60 | 5 |
| 75 | 4 |
| 100 | 4 |
| 125 | 3 |
| 150 | 3 |
| 200 | 2 |

**Nota:** HP = Potencia nominal del motor instalado. Sph = Cantidad máxima de arranques permitidos por hora.

El tiempo de disparo (seg) se calcula como: Icarga / Inom + 2

**Nota:** Inom = Valor de corriente calibrada por el usuario en el SUB nC GSPT. Inom es lo mismo que la corriente del motor con su máxima carga FLA tal como se muestra en los ajustes del producto.

## Cómo Ordenar el GSPT de Acuerdo a sus Necesidades

| Voltaje | Corriente | Opciones | Idioma |
|---------|-----------|----------|--------|
| 208 | 04 | S – Estándar | S – Español |
| 480 | 12 32 80 | — | E – Inglés |
| — | — | — | — |

**Referencia:** 208 = 208/220/240 VAC; 480 = 440/480 VAC

## Información de Contacto

**Fabricado en la REPÚBLICA BOLIVARIANA DE VENEZUELA**

**Distribuido por:** GENTECA, GENERACIÓN ELECTRÓNICA DE TECNOLOGÍA, C.A.
- R.I.F.: J-00223173-4
- Dirección: Av. El Buen Pastor, Cruce con Calle Vargas, Edificio Alba, Piso 1, Local 1-A, Boleíta Norte, Caracas, Zona Postal 1070
- Teléfono: +(58)(212) 237.0711 (Master)
- Fax: +(58)(212) 235.2497
- E-mail: genteven@genteca.com.ve
- Página web: www.genteca.com.ve

**Distribuido en México:** PROTECTORES EXCELINE S.A. DE CV
- R.F.C.: PEX1806124Y5
- Dirección: Fernando Zárraga 55, Ciudad Satélite, Naucalpan de Juárez, Edo. de México, C.P. 53100
- Teléfono: +(55) 5572-9200
- E-mail: contacto@exceline.com.mx
- Página web: www.exceline.com.mx

**Distribuido en Panamá:** COMAR TRADING INC.
- R.U.C.: 319589-50908-21 DV-06
- Dirección: Final Calle 18, Edif. 44, Local 4, Zona Libre de Colón, Apartado Postal 030200900
- Teléfono: +(507) 433-1043
- Fax: +(507) 433-2837

---

**NOTA:** Las especificaciones y descripciones mostradas en este documento están sujetas a cambio sin previo aviso.
