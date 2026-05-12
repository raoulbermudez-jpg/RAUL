---
title: "GUCT+ c-CT Manual de Instalación"
type: Technical
source: "GUCT+ c-CT GD-MAN8005-CO-V1.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GUCT+"
version_status: "historica"
date_processed: "2026-05-10"
---

# GUCT+ c-CT Manual de Instalación

## 9.3 Ajuste de Eventos

Los modelos GUCT+ tienen las opciones de menú "AJUSTE RELOJ" y "PROG. HORARIO". A continuación se muestra un ejemplo de ajuste de eventos y días feriados.

### EVENTO 01 (ejemplo):
De Martes a Sábado
- ON: 7:30 hrs
- OFF: 16:45 hrs

### FERIADO 01 (ejemplo)
24 de Junio

El procedimiento de ajuste incluye la navegación mediante menú con las opciones:
- AJUSTE VOLTAJE
- AJUSTE CORRIENTE
- MODO DE REARME
- AJUSTE RELOJ
- CAMBIO DE CLAVE
- DIRECCIÓN MODBUS
- PROG. HORARIO
- BORRAR HISTORICO
- REINICIAR EQUIPO
- SALIR

Se utiliza SELECCIÓN para cambiar entre días (Lunes a Domingo) e ingresar parámetros de encendido (ON) y apagado (OFF).

---

## ESPECIFICACIONES TÉCNICAS

### A) Fuente de Poder

| Parámetro | Valor |
|-----------|-------|
| Voltaje de Operación (Ue) | 208/220/240 V~ ó 440/480 V~ |
| Límites de Operación de Voltaje (Ue) | 145 > 312 V~ ó 264 > 672 V~ |
| Consumo Promedio (In) | 45 mA |
| Frecuencia Nominal (Fn) | 50/60 Hz |
| Frecuencia de Operación | 42 > 70 Hz |
| Modo de Operación | Continuo |

### B) Condiciones Ambientales, Límites de Operación e Instalación

| Parámetro | Especificación | Norma |
|-----------|----------------|-------|
| Normas Requisitos EUROPA | IEC61010-1, IEC60255-6, IEC60947-1 LVD & EMC | — |
| Normas Requisitos USA | UL (pendiente), NKCR, Dispositivos Auxiliares UL508 | — |
| Aprobación Europea | CE (pendiente), Dispositivos de Bajo Voltaje | IEC60947-1 |
| Temperatura Ambiental (Operación) | -5 °C a 55 °C (23 °F a 131 °F) | — |
| Temperatura Ambiental (Almacenaje) | -10 °C a +70 °C (14 °F a 158 °F) | — |
| Humedad Relativa Máxima | 85% R.H. | — |
| Resistencia a Vibraciones | Clase 1, Amplitud <0.035 mm ó 1G, 10 Hz < f < 150 Hz | IEC 60255-21-1 |
| Protección a Objetos/Agua (IP20) | Protegido contra Objetos > 12.5 mm, ninguna protección contra agua | IEC 60529 |
| Nivel de Contaminación | Grado 3 | IEC 60255-5 |
| Protección contra Exceso de Voltaje | Categoría III | IEC 60255-5 |
| Voltaje de Aislamiento Nominal | 500 V | — |
| Prueba de Impulso | 5 kV | IEC 60255-5 |
| Prueba Dieléctrica | 2.5 kV 50/60 Hz @ 1 min | UL 508 |
| Grado de Protección al Fuego de la carcaza | V-0 | UL-94 |
| Material de la Carcasa | Polímeros: LEXAN, ABS, VYDYNE | — |
| Posiciones de Montaje | Sin Restricciones | — |
| Tipos de Montaje | Riel DIN Simétrico DIN 43880, Superficie Plana, Tornillo 3/16" x 1/2" Tipo NEMA | IEC 715 |
| Tipo de Tornillo de Borneras | Plano M3 | — |
| Torque de Apretado de Borneras | 5.1 Kg-cm / 4.4 lb-in | — |
| Cableado de Borneras | 10-18 AWG | — |
| Cableado en el Sensor de Corriente | ø < 11 mm, AWG 4 | — |
| Medidas | 92 x 91 x 96 (L x A x H) mm | — |
| Peso | 494 g / 1.09 lb | — |

### C) Características de Control

| Parámetro | Especificación | Norma |
|-----------|----------------|-------|
| Capacidad de los Contactos (para Circuitos de Control) | B300 Pilot Duty, 1 A @ 240 V~, 0.5 A @ 480 V~ | UL 508 Sección 139.1 |
| Expectativa de Vida Eléctrica | 100,000 Operaciones | — |
| Expectativa de Vida Mecánica | 10,000,000 Operaciones | — |
| Categoría de Uso | AC-15, Capacidad para Cargas > 72 VA | IEC60947-5-1 |

### D) Ajustes de Rango, Mediciones

| Parámetro | Rango | Precisión |
|-----------|-------|-----------|
| Rango de Medición de Voltaje (Um) | 0 > 312 V~ (208 V) ó 0 > 672 V~ (480 V) | +2% |
| Rango de Medición de Corriente (Im) | 5% > 333% CT (Modelo de Corriente EXT CT/5) | +2% |
| Rango de Frecuencia | 45.0 > 70.0 Hz | 1% |
| Factor Potencia Instantáneo | 0.00 > 1.00 | 8% |
| Potencia Aparente Instantánea (kVA) | 0.0 > 999.9 kVA | 4% |
| Potencia Real Instantánea (kW) | 0.0 > 999.9 kW | 4% |
| Consumo de Energía (kWH) | 0 > 999,999 kW/H | 4% |
| Horas de trabajo acumuladas del motor | 0 — 999,999 H | 1% |

### E) Funciones y Algoritmos de Protección

#### Protección de Voltaje

| Función | Especificación |
|---------|----------------|
| Bajo Voltaje (UV) | 165 > 225 V~ (208 V) ó 350 > 460 V~ (480 V), Ajustable |
| Sobre Voltaje (OV) | 215 > 270 V~ (208 V) ó 460 > 580 V~ (480 V), Ajustable |
| Umbral Histéresis de Voltaje | 6 V~ (208 V) ó 12 V~ (480 V) |
| Desbalance de Voltaje (VUB) | 2% > 10%, Ajustable |
| Pérdida de Fase de Voltaje (VSP) | IN VUB > 33%, OUT VUB < 28% |
| Frecuencia Nominal | 50 ó 60 Hz, Ajustable |
| Variación de Frecuencia | 2% > 10%, Ajustable |
| Fase Invertida (PR) | Secuencia ABC Normal, Secuencia CBA Invertida |
| Temporizado a la Desconexión por Fase Invertida (PR) | < 1 s |
| Temporizado a la Desconexión por otras Fallas de Voltaje (TD) | 1 > 30 s, Ajustable |
| Temporizado a la Conexión (TC) | 0 > 600 s, Ajustable |
| Temporizado a la Desconexión por VSP | 3 s |

#### Protección de Corriente

| Función | Especificación |
|---------|----------------|
| Ajuste Corriente Nominal | Seleccionar en Página 4 |
| Ajuste Nivel Sobrecarga (OL) | 5% > 50%, Ajustable |
| Ajuste de Clase Térmica | 5 > 35, Ajustable |
| Ajuste Dinámico Modelo del Motor (Curva Fría/Curva Caliente) | Clase Térmica varía de 1 > 18 de la clase ajustada según el tiempo de encendido y nivel de carga | IEC 60255-8 |
| Tiempo Máximo entre curvas Fría/Caliente | 2 Horas (de 1 a 1/3 ó de 1/3 a 1) | IEC 60255-190 |
| Tiempo Desconexión de Falla por Sobrecarga | Según el nivel de Sobrecarga y Clase ajustada | IEEE Std. 37.112-1996 |
| Umbral de Calor para Falla por Sobrecarga | 100% |
| Desbalance de Corriente (CUB) | CUB > 48% |
| Pérdida de Fase por Corriente (CSP) | CUB > 60% |
| Temporizado Desconexión por CSP | 1 s |
| Temporizado Desconexión por CUB | 2 s |

#### Opciones de Control Especial

| Función | Especificación |
|---------|----------------|
| Opción de Alta Inercia | SI / NO |
| Umbral de Calor por Alta Inercia | 400% |
| Temporizado Conexión por Alta Inercia | 20 > 120 s, Ajustable |
| Tiempo de Enfriamiento Máquina Térmica | 50 x Clase Térmica Ajustada s |
| Subcarga | SI / NO |
| Tipo Desconexión por Subcarga (UC) | % Inom ó FP (Factor Potencia) |
| Desconexión por Subcarga (%Inom) | 30% > 90%, Ajustable |
| Desconexión por Subcarga (PF) | 0.3 > 0.9, Ajustable |
| Temporizado Desconexión por Subcarga (UC) | 5 > 600 s, Ajustable |
| Temporizado Conexión por Subcarga (UC) | 2 > 500 s, Ajustable |
| Detección de Tercera (3°) Falla | SI / NO |
| SN 3 Fallas de Corriente en menos de 105 min |
| Tiempo Desconexión para 3 Fallas | 3 s |
| Modo de Rearme | Automático / Manual, Selección |
| Tiempo mínimo entre 2 arranques | 50 x Clase Térmica s |

#### Características Programador Horario

| Característica | Especificación |
|----------------|----------------|
| Ajuste Reloj / Fecha | hh:mm dd/mm/aa |
| Control Prog. Horario | SI / NO, Selección Usuario |
| Número de Eventos programables | 60 |
| Número de Feriados programables | 20 |

### F) Comunicaciones y Funciones Especiales

| Parámetro | Especificación |
|-----------|----------------|
| Protocolo de Comunicación | MODBUS RTU @ 9600 8N1 |
| Puerto de Comunicación | Puerto GIO PORT (*) |
| Rango de Direcciones | 1 > 127 |
| Histórico de Fallas | Reporte de 20 últimas fallas (Datos de Tipo Falla, Valor, Hora, Fecha y Tiempo de Duración) |
| Bloqueo de Parámetros | 0000 Libre, 0001 > 9999 Bloqueado |

(*) Se requiere GIOPlug para la comunicación a través de GIO Port. El GIOPLUG se suministra por separado.

### Transformadores de Corriente (CT) Externos Sugeridos

| Rango de Corriente Nominal (A) | Toroide (A/5) |
|--------------------------------|---------------|
| 13 a 17 | 50/5 |
| 15 a 20 | 60/5 |
| 19 a 25 | 75/5 |
| 25 a 33 | 100/5 |
| 31 a 42 | 125/5 |
| 38 a 50 | 150/5 |
| 50 a 67 | 200/5 |
| 63 a 83 | 250/5 |
| 75 a 100 | 300/5 |
| 100 a 133 | 400/5 |
| 125 a 167 | 500/5 |
| 150 a 200 | 600/5 |
| 190 a 250 | 750/5 |
| 200 a 260 | 800/5 |
| 250 a 330 | 1000/5 |
| 300 a 400 | 1200/5 |
| 375 a 500 | 1500/5 |
| 500 a 660 | 2000/5 |

### G) Compatibilidad Electromagnética para Ambiente Industrial Severo

#### Estándares de Inmunidad y Emisiones

| Ensayo | Norma |
|--------|-------|
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

#### Curvas de Disparo

Las curvas de disparo térmica se ajustan según clase (5, 10, 15, 20, 25, 30) con normas IEEE C37-112 e IEC 60255-8.

- Curva Caliente = Curva Fría / 3
- I nom = Valor de Corriente calibrada por el usuario en el GUCT+

---

## Cómo Ordenar GUCT+

**Formato de Pedido:**

GUCT+ - [CONTROL] - [VOLTAJE] - [CORRIENTE] - [IDIOMA]

Donde:
- **CONTROL:** Voltaje + Corriente + Programador Horario
- **VOLTAJE:** 
  - 208: 208/220/240 V~
  - 480: 440/480 V~
- **CORRIENTE:** 
  - 00: CT Externos
- **IDIOMA:**
  - S: ESPAÑOL
  - E: INGLÉS
  - P: PORTUGUÉS

---

## Información del Fabricante

**Diseñado y Fabricado por:**

Generación de Tecnología

**Genteca, Generación de Tecnología, C.A.**
- RIF: J-00223173-4
- Av. El Buen Pastor cruce con Calle Vargas
- Edif. Alba, Piso 1, Local I-A
- Boleita Norte, Caracas - Venezuela
- Zona Postal 1070

**Contacto:**
- Teléfono: ++(58 212) 237.07.11
- Fax: ++(58 212) 235.24.97
- E-mail: genteven@genteca.com.ve
- Sitio Web: www.genteca.com.ve

**Nota:** Las especificaciones y descripciones mostradas en este documento están sujetas a cambio sin previo aviso.
