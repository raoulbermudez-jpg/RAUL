---
title: "GSPT Manual de Instalación - Ajustes de Pantalla e Instrucciones de Desmontaje"
type: Technical
source: "I_GSPT-MV - LR 10MAR.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GSPT-MV"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GSPT Manual de Instalación

## 10. Ajustes de Pantalla

### 10.1 Guía rápida de programación para GSPT

#### Pantalla de Inicio
- **Modelo:** GSP MV 2007
- **Voltaje/Corriente:** 480V 180A
- **Versión:** v1.09 ES
- **Opciones de Menú:**
  - 0 Pantalla de Inicio
  - 1 Pantalla de Fallas
  - 2 Medición kW-KVA-PF-kWH
  - 3 Histórico de Fallas
  - 4 Contador Hrs. del Motor
  - 5 Temperatura del Motor, Frecuencia y Modo REARME

#### Pantallas de Fallas

**1.1 Desconectado por MODBUS**
- 220 220 200 7%
- OFF MODBUS

**1.2 Desconectado bajo Modo MANUAL**
- 220 220 200 7%
- OFF MANUAL

**1.3 Desconectado por 3ra Falla**
- 220 220 200 7%
- OFF 3ra FALLA

**1.4 Temporizado a la Conexión (TC)**
- v12 v23 v V3 VUB
- 220 220 200 7%
- TC 15

**1.5 TC por Subcarga**
- 11 12 13
- 220 220 200 7%
- uc TC 10'

**1.6 Tiempo entre arranque**
- 220 220 200 7%
- P = 110.0 kVA | 100.0 KM
- MIN Op OO 0.95 PF 290000 kWh

**1.7 Arranque hora y**
- 220 220 200 7%
- Sph TC 10"

**1.8 Bajo Voltaje (UV)**
- 2000" UV 100Y v12
- 100 220 280 7%
- UV 100V v12

**1.9 Sobre Voltaje (OV)**
- 220 220 280 7%
- OV 280V V31

**1.10 Desbalance de Voltaje (VUB)**
- 220 220 200 10%
- VUB 10%

**1.11 Variación de Frecuencia (FS)**
- 60.0 HZ
- CUB 5%
- AUTO TM 20%
- 220 220 200 7%
- FS 63.6 HZ

**1.12 Pérdida de Fase (VSP)**
- 120 100 200 71%
- VSP L2

**1.13 Fase Invertida (PR)**
- 220 220 200 7%
- FASE INVERTIDA

**1.14 Porcentaje (%) de Calor Acumulado**
- 220 220 200 7%

**1.15 Sobrecalentamiento**
- 220 220 200 7%
- CALOR ESIVO

**1.16 Temperatura Máxima**
- 220 220 200 7%
- OT 60°C
- IT Relé Desviado
- 220 220 200 7%
- RELE DESVIADO

### Configuración de Botones Pulsadores

**Pantalla de Fallas - Descripción:**

| Elemento | Descripción |
|----------|-------------|
| Tipo de Falla | UV para Bajo Voltaje, OV para Sobrevoltaje, FS para Frecuencia, VUB para Desbalance de Voltaje, VSP para Pérdida de Fase por Voltaje, PR para Fase Invertida |
| Valores de Voltaje durante Falla | Lecturas de voltaje en las fases involucradas |
| Número de la Falla | Identificación secuencial de la falla |
| Fases Involucradas | v12, v23, v31, etc. |
| Valor Extremo en la Falla | Magnitud registrada del parámetro de falla |
| Porcentaje Desbalance Voltaje | % VUB registrado |

### Menú Principal de Ajustes (Opción 7)

**7.1 Ajuste Voltaje**
- V NOMINAL: 480V
- BAJO VOLT.: 180V
- SOBRE VOLT.: 242
- DESBALANCE: 10%
- FRECUENCIA: 60HZ
- FS: 10%
- TC MIN: OFF 10'
- TD: 30"
- TC: 600"

**7.2 Ajuste Corriente**
- I NOMINAL: 100A
- SOBRECARGA: 20%
- TC SOBRECAR.: 10'
- SUBCARGA: NO
- 3ra FALLA: OFF
- ARRANQUES/h: YES
- SUECARGA In: 40%
- TD SUBCARGA: 600"
- TC SUBCARGA: 10°

**7.2.1 MAX. ARRANQUES/h**

**7.4 Modo de Rearme**
- AUTO
- MANUAL

**7.5 Ajuste Reloj**
- INGRESE CLAVE: 0000

**7.5.1 Verificar Clave**

**7.6 Dirección MODBUS**
- 001

**7.7 Ajuste Temperatura**
- TEMP. COMP: SI
- TEMP. Ti: 55°C
- TEMP. Tm: 120°C

**7.8 Borrar Histórico**
- BORRANDO...
- RECOBRANDO VALORES

**7.9 Reiniciar Equipo**
- START ADJUST: SELECT

### Funciones Especiales del Teclado

- **Up&Down:** Para activar la ventana de ajuste. Si el producto está protegido, se debe introducir la clave correspondiente; en caso contrario se mostrará directamente el menú de ajuste.
- **Up&Select:** Para mostrar la pantalla de inicio del producto.
- **Down (desde pantalla de inicio):** Para realizar el test de LCD.
- **Select:** Para ajustar cualquier parámetro y para aceptar cualquier cambio.
- **Encender el motor:** Presionar Select.

### Glosario de Abreviaturas

| Abreviatura | Significado |
|-------------|------------|
| Sph | ARRANQUES POR HORA (Starts Per Hour) |
| 3F | TERCERA FALLA (Third Failure) |
| RL | ROTOR BLOQUEADO |
| SM | ARRANQUE FORZADO |
| FS | FRECUENCIA |
| PF | FACTOR DE POTENCIA |
| UC | BAJA CORRIENTE |
| OL | SOBRE CORRIENTE |
| PR | FASE INVERTIDA |
| UV | BAJO VOLTAJE |
| OV | SOBRE VOLTAJE |
| VUB | DESBALANCE DE VOLTAJE |
| VSP | PÉRDIDA DE FASE POR VOLTAJE |
| CSP | PÉRDIDA DE FASE POR CORRIENTE |
| CUB | DESBALANCE DE CORRIENTE |
| TEMP. | TEMPERATURA |
| COMP. | COMPENSACIÓN |
| HRS | HORAS |
| TD | TIEMPO |
| TM | TEMPERATURA DEL MOTOR |

---

## 11. Instrucciones de Desmontaje

### 11.1 Desmontaje Riel Simétrico DIN

#### 11.1.1 Sin Caja de CT's

**PELIGRO:** Apague el interruptor de alimentación (Breaker) y desconecte todo el cableado del SUBTIRONIG GSPT antes de proceder a desmontarlo. Hacer caso omiso puede resultar en daños a los equipos o personas.

**Procedimiento:**
a) Usando dos destornilladores planos, hale hacia abajo (2 mm aprox.) los ganchos de retención dispuestos al fondo inferior del SUBTIRONIG GSPT.

b) Mediante el destornillador desplace los ganchos de retención a la posición 2 y saque el SUBTIRONIG GSPT del Riel Simétrico.

#### 11.1.2 Con Caja de CT's

**Procedimiento:**
a) Usando dos destornilladores planos, hale hacia abajo (2 mm aprox.) los ganchos de retención dispuestos al fondo inferior de la Caja de CT's acoplada al SUBTRONIG GSPT.

b) Mediante los destornilladores en la posición 2, saque el conjunto SUBTRONIG GSPT-Caja de CTs del DIN Riel.

**Recomendaciones para Desmontaje DIN Riel:**
- Hale suavemente y hacia abajo los Ganchos de Retención unos 2 mm aprox.
- Un movimiento brusco para sacar cada gancho podría desprenderlo.

### 11.2 Desmontaje de Superficie Plana

#### 11.2.1 Sin Caja CT's

**Procedimiento:**
a) Destornille los 4 tornillos que fijan al SUBUIRONIG GSPT a la Superficie Plana a través de los sujetadores insertables y luego saque el SUBTIRONIG GSPT de dicha superficie.

#### 11.2.2 Con Caja de CT's

**Procedimiento:**
a) Destornille los 4 tornillos que fijan al conjunto SUBTIRONIG GSPT - Caja de CT a la Superficie Plana a través de los sujetadores insertables y luego saque el Conjunto SUBTIRONIG GSPT - Caja de CT de dicha superficie.

### 11.3 Desmontaje del Empotrado en Pánel (FLUSH MOUNTING)

#### 11.3.1 Procedimiento

a) Retire los Ganchos Sujetadores para Frontal. Para ello hale suavemente en el punto indicado y deslice hacia atrás la pieza.

b) Remueva el frontal insertable (Flush Mounting) y el SUBTIRONIG GSPT.

---

## Especificaciones Técnicas SUBTRONIC GSPT

### A) Fuente de Poder

| Parámetro | Especificación | Unidad |
|-----------|----------------|--------|
| a.1 | Voltaje de Operación, Ue | 200, 208, 220, 230, 240, 400, 420, 440, 460, 480 VAC |
| a.2 | Límites de Operación de Voltaje Ue | 72—>672 | VAC |
| a.3 | Consumo Promedio, In | 38 | mA |
| a.4 | Frecuencia Nominal, Fu | 50/60 | Hz |
| a.5 | Frecuencia de Operación | 42—>70 | Hz |
| a.6 | Modo de Operación | Continuo | — |

### B) Condiciones Ambientales, Límites de Operación e Instalación

| Parámetro | Especificación |
|-----------|----------------|
| b.1 | Normas, Requisitos para EUROPA: EC61010-1, IEC60255-6, IEC60947-1, LVD & EMC |
| b.2 | Normas, Requisitos para USA: UL (pendiente), NKCR, Dispositivos Auxiliares, UL 508 |
| b.3 | Aprobación Europea: CE (pendiente), Dispositivos de Bajo Voltaje IEC60947-1 |
| b.4 | Temperatura Ambiental (Operación): -5°C a 55°C (23°F a 131°F) |
| b.5 | Temperatura Ambiental (Almacenamiento): 10°C a +85°C (14°F a 158°F) |
| b.6 | Humedad Relativa Máxima o R.H.: — |
| b.7 | Resistencia a Vibraciones: 10Hz < f < 150Hz, Clase 1, Amplitud <0.035mm o 1G IEC 60255-21-1 |
| b.8 | Protección a Objetos/agua: IP20, Protección contra objetos > 12.5mm, ninguna protección contra agua IEC 60529 |
| b.9 | Nivel de Contaminación: Grado 3 IEC 60255-5 |
| b.10 | Categoría Protección Sobre Voltaje: Categoría III, 4KV IEC 60255-5 |
| b.11 | Voltaje de Aislamiento Nominal: 500V IEC 60255-5 |
| b.12 | Prueba de Impulso: 5KV IEC 60255-5 |
| b.13 | Prueba Dieléctrica: 2.5 KV 50/60 Hz @ 1min UL-508 |
| b.14 | Protección al Fuego de la Carcasa: v-0 UL-94 |
| b.15 | Material de la Carcasa: Polímeros: LEXAN, ABS, VYDYNE |
| b.16 | Posiciones de Montaje: Sin Restricciones |
| b.17 | Tipos de Montaje: DIN Riel Simétrico IEC 715, DIN 43880; Superficie Plana; Empotrable (Flush Mounting) |
| b.18 | Tipo de Tornillo de Borneras: Plano M2.5; Torque de Apretado: 5.2 Kg-cm (4.5 Ib-in) |
| b.19 | Cableado de Borneras: AWG 12-18, L=7-8mm (5/16); Cableado por agujeros Caja CT: 4% <18 mm, máximo AWG 0 |
| b.20 | Dimensión GSPT: 175 x 90 x 78.0 (LxAxH) mm |
| b.21 | Dimensión Caja CT: 175 x 90 x 79.8 (LxAxH) mm |
| b.22 | Dimensión GSPT+Caja CT: 175 x 90 x 157.8 (LxAxH) mm |
| b.23 | Peso GSPT: 463 g (1.53 lb) |

### C) Características de Control

| Parámetro | Especificación |
|-----------|----------------|
| c.1 | Capacidad de los Contactos: A300 PILOT DUTY UL 508 (para Circuitos de Control) 3 A @ 240 VAC, 1.5 A @ 480 VAC Sección 139.1 |
| c.2 | Expectativa de Vida Eléctrica: 100.000 Operaciones |
| c.3 | Expectativa de Vida Mecánica: 10.000.000 Operaciones |
| c.4 | Categoría de Uso: AC-15, Capacidad para cargas > 72 VA IEC 60947-5-1 |

### D) Ajustes de Rango, Mediciones

**Modelo de Voltaje: MV (Multivoltaje VAC)**

| Parámetro | Especificación | Tolerancia |
|-----------|----------------|-----------|
| d.1 | Medición de Voltaje | VAC | ±2% |
| d.2 | Rango de Medición de Voltaje, Um | 0→672 | Precisión |
| d.3 | Rango de Frecuencia | 45.0—>70.0 Hz | 1% |
| d.4 | Factor Potencia Instantáneo | 0.00—>1.00 | 2% |
| d.5 | Potencia Aparente Instantánea kVA | 0.0—>999.9 kVA | 4% |
| d.6 | Potencia Real Instantánea kW | 0.0—>999.9 kW | 4% |
| d.7 | Consumo de Energía kWH | 0—>999999 kW/H | 4% |
| d.8 | Horas de trabajo acumuladas del motor | 0—>999999 H | 1% |
| d.9 | Entrada de Temperatura | -20°C—>200°C | 1% |

**Modelo de Corriente: 050, 100, 180 A**

| Parámetro | 050 | 100 | 180 | Unidad |
|-----------|-----|-----|-----|--------|
| d.2 | Rango de Medición de Corriente, Im | 4.5—>500 | 30—>1000 | 55—>1800 | Precisión ±2% |

### E) Funciones y Algoritmos de Protección

| Parámetro | Especificación |
|-----------|----------------|
| e.1 | Bajo Voltaje (UV) Qi motor = 0 u OC IR | Ajustable |
| e.2 | Sobre Voltaje (OV) | Ajustable (Entrega de Fábrica = +10%) |
| e.3 | Umbral Histéresis de Voltaje | +/-3% del voltaje nominal VAC |
| e.4 | Desbalance de Voltaje (VUB) | 2% > 10% Ajustable |
| e.5 | Pérdida de Fase de Voltaje (VSP) | IN VUB > 33%, OUT VUB < 28% |
| e.6 | Frecuencia Nominal | 50 ó 60 Hz Ajustable |
| e.7 | Variación de Frecuencia | 2% > 10% Ajustable |
| e.8 | Fase Invertida (PR) | Secuencia ABC Normal, Secuencia CBA Invertida |
| e.9 | Temporizado a la Desconexión por Fase Invertida (PR) | <1 seg |
| e.10 | Temporizado a la Desconexión por otras Fallas de Voltaje (TD) | 1—>30 seg Ajustable |
| e.11 | Temporizado a la Conexión (TC) | 0—>600 seg Ajustable |
| e.12 | Temporizado a la Desconexión por (TD) por VSP | 3 seg |
| e.13 | Modo de Rearme | Automático/Manual Selección |
| e.14 | Ajuste Corriente Nominal | 050: 15→50 A; 100: 30-100 A; 180: 55-180 A |
| e.15 | Ajuste Nivel Sobrecarga (OL) | 5%—>50% Ajustable |
| e.15b | Temporizado conexión por sobrecarga (OC) | 10 a 60 Minutos Ajustable |
| e.16 | Clase Térmica | 10 |
| e.17 | Ajuste Dinámico Modelo del Motor (Curva Fría/Curva Caliente) | Clase Térmica vara de 1 →1/3 de la clase 10 IFC 60255-8 según el tiempo de encendido y nivel de carga del motor |
| e.18 | Tiempo Máximo entre curvas Fría/Caliente | 2 Horas (de 1 a 1/3 ó de 1/3 a 1) IEC 60255-8-1990 |
| e.19 | Tiempo Desconexión de Falla por Sobrecarga de Clase 10 | Según el nivel de Sobrecarga y IEEE Std. 037.112-1996 |
| e.20 | Umbral de Calor para Falla por Sobrecarga | 100% |
| e.21 | Desbalance de Corriente (CUB) | CUB > 48% |
| e.22 | Pérdida de fase por Corriente (CSP) | CUB > 60% |
| e.23 | Detección Rotor Bloqueado Acelerado (LR) | CONTINUO EN REAJUSTE |
| e.24 | Temporizado Desconexión por CSP | 3 Seg. |
| e.25 | Temporizado Desconexión por CUB | 4 Seg. |
| e.26 | Tiempo de Enfriamiento Máquina Térmica | 10 Minutos Adjustable |
| e.27 | Subcarga | SI/NO |
| e.28 | Tipo Desconexión por Subcarga (UC) | Detección relativa a corriente Nominal Inom Seg. Ajustable |
| e.29 | Temporizado Desconexión por Subcarga (UC) | 5—>600 Min. Ajustable |
| e.30 | Temporizado Conexión por Subcarga (UC) | 2—>500 Selección Usuario |
| e.31 | Detección de Tercera (3*) Falla | SI/NO |
| e.32 | Desconexión permanente por Tercera (3*) Falla | Catas de Corriente en menos de 30 min. C37.112-1996 |
| e.33 | Tiempo desconexión para Rotor bloqueado acelerado | 3 Seg |

---

**Código de Documento:** BT MV-02-0121.0-01-S

---

*Documento técnico de la línea Genius de Genteca - Empresa venezolana de protección eléctrica*
