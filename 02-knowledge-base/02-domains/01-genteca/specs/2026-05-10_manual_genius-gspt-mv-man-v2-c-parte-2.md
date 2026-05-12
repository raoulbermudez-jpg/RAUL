---
title: "GSPT-MV Manual de Instalación - Ajustes de Pantalla y Especificaciones Técnicas"
type: Technical
source: "GSPT-MV_MAN-V2_C.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GSPT-MV"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GSPT-MV Manual de Instalación

## 10.1 Guía Rápida de Programación para GSPT

### Configuración de Parámetros por Defecto

#### Voltaje y Protección de Voltaje
- **Voltaje Nominal**: 480V
- **Bajo Voltaje (UV)**: 180V
- **Sobre Voltaje (OV)**: 242V
- **Desbalance de Voltaje**: 10%
- **Frecuencia**: 60Hz
- **FS**: 103

#### Tiempos y Arranques
- **TC Mínimo Apagado**: 10"
- **TD**: 30"
- **TC**: 600"
- **Máximo Arranques/h**: 12
- **Modo de Rearme**: AUTO/MANUAL

#### Protección de Corriente
- **Corriente Nominal**: 100A
- **TC Sobrecarga**: Por
- **Subcarga**: Activada (NO/SI)
- **Subcarga In**: 40%
- **TD Subcarga**: 600"
- **TC Subcarga**: 107

### Descripción de Pantallas de Fallas

#### Historico de Fallas

Los registros de fallas incluyen:
- Tipo de Falla
- Valor registrado de la falla
- Valor mínimo de voltaje
- Número de la falla
- Fases involucradas
- Porcentaje de desbalance de voltaje

**Ejemplo de Bajo Voltaje (UV):**
- Valores de voltaje durante falla: 167, 169, 168 VAC
- Porcentaje desbalance: 0%
- Fases involucradas: V12
- Número de falla: 17
- Variación de frecuencia: 68.0 Hz

**Ejemplo de Desbalance de Voltaje (VUB):**
- Valores de voltaje durante falla: 221, 267, 264 VAC
- Porcentaje desbalance: 11%
- Tipo de falla: VUB
- Porcentaje de calor: Valor medido según pantalla

### Funciones Especiales del Teclado

- **Up&Down**: Activar ventana de ajuste (requiere clave si está protegido)
- **Down desde pantalla de inicio**: Test de LCD
- **Select**: Ajustar parámetro / Aceptar cambio
- **Para encender el motor**: Presionar botón correspondiente

### Configuración de Botones Pulsadores
- START
- ADJUST
- SELECT

### Códigos de Fallas - Glosario de Abreviaturas

| Código | Significado |
|--------|-------------|
| UV | Bajo Voltaje |
| OV | Sobre Voltaje |
| VUB | Desbalance de Voltaje |
| FS | Frecuencia |
| VSP | Pérdida de Fase por Voltaje |
| CSP | Pérdida de Fase por Corriente |
| PR | Fase Invertida |
| CUB | Desbalance de Corriente |
| TM | Temperatura del Motor |
| OL | Sobre Corriente |
| UC | Baja Corriente |
| RL | Rotor Bloqueado |
| SM | Arranque Forzado |
| TEF | Falla de Energía |
| PF | Factor de Potencia |
| OT | Sobre Temperatura |
| 3F | Tercera Falla |
| Sph | Arranques Por Hora |

| Abreviatura | Significado |
|------------|-------------|
| TEMP. | Temperatura |
| PELIN | Peligro |
| COMP. | Compensación |
| T. | Tiempo |
| HRS | Horas |
| BR | Relé Asociado |

## 11 SUBTRONIG GSPT-MV Instrucciones de Desmontaje

### 11.1.1 Desmontaje Riel Simétrico DIN (Sin Caja de CT's)

1. Usando dos destornilladores planos, hale hacia abajo (2 mm aprox.) los ganchos de retención dispuestos al fondo inferior del SUBTRONIG GSPT-MV tal como se muestra en la figura.

2. Mediante el destornillador desplace los ganchos de retención a la posición 2 y saque el SUBTRONIG GSPT-MV del Riel Simétrico.

**Recomendaciones**: Hale suavemente y hacia abajo los ganchos de retención unos 2 mm aprox. Un movimiento brusco para sacar cada gancho podría desprenderlo.

### 11.1.2 Desmontaje Riel Simétrico DIN (Con Caja de CT's)

1. Usando dos destornilladores planos, hale hacia abajo (2 mm aprox.) los ganchos de retención dispuestos al fondo inferior de la Caja de CT's acoplada al SUBTRONIG GSPT-MV.

2. Mediante los destornilladores en la posición 2, saque el conjunto SUBTRONIG GSPT-MV - Caja de CTs del DIN Riel.

### 11.2.1 Desmontaje de Superficie Plana (Sin Caja de CT's)

1. Destornille los 4 tornillos que fijan al SUBTRONIG GSPT-MV a la Superficie Plana a través de los sujetadores insertables.

2. Saque el SUBTRONIG GSPT-MV de dicha superficie.

### 11.2.2 Desmontaje de Superficie Plana (Con Caja de CT's)

1. Destornille los 4 tornillos que fijan al conjunto SUBTRONIG GSPT-MV - Caja de CT a la Superficie Plana a través de los sujetadores insertables.

2. Saque el conjunto SUBTRONIG GSPT-MV - Caja de CT de dicha superficie.

### 11.3.1 Desmontaje del Empotrado en Panel (FLUSH MOUNTING)

1. Retire los Ganchos Sujetadores para Frontal. Para ello hale suavemente en el punto indicado en la figura y deslice hacia atrás la pieza.

2. Remueva el frontal insertable (Flush Mounting) y el SUBTRONIG GSPT-MV.

**PELIGRO**: Apague el interruptor de alimentación (Breaker) y desconecte todo el cableado del SUBTRONIG GSPT-MV antes de proceder a desmontarlo. Hacer caso omiso puede resultar en daños a los equipos o personas.

## SUBTRONIG GSPT-MV Especificaciones Técnicas

### A) Fuente de Poder

| Parámetro | Valor | Norma |
|-----------|-------|-------|
| Voltaje de Operación, Ue | 200, 208, 220, 230, 240, 400, 420, 440, 460, 480 VAC | — |
| Límites de Operación de Voltaje Ue | 72 → 672 VAC | — |
| Consumo Promedio, In | 38 mA | — |
| Frecuencia Nominal, Fn | 50/60 Hz | — |
| Frecuencia de Operación | 42 > 70 Hz | — |
| Modo de Operación | Continuo | — |

### B) Condiciones Ambientales, Límites de Operación e Instalación

| Parámetro | Valor | Norma |
|-----------|-------|-------|
| Normas - Europa | IEC61010-1, IEC60255-6, IEC60947-1 LVD & EMC | — |
| Normas - USA | UL (pendiente), NFPA, Dispositivos Auxiliares, UL508 | — |
| Aprobación Europea | CE (pendiente), Dispositivos de Bajo Voltaje IEC60947-1 | — |
| Temperatura Ambiental (Operación) | -5 °C a 55 °C (23 °F a 131 °F) | — |
| Temperatura Ambiental (Almacenaje) | -10 °C a +70 °C (14 °F a 158 °F) | — |
| Humedad Relativa Máxima | 85% R.H. | — |
| Resistencia a Vibraciones | Clase 1, Amplitud < 0.035 mm, 10 Hz < f < 150 Hz | IEC 60255-21-1 |
| Protección a Objetos/Agua | IP20, Protección contra objetos > 12.5 mm, ninguna protección contra agua | IEC 60529 |
| Nivel de Contaminación | Grado 3 | IEC 60255-5 |
| Categoría Protección Sobre Voltaje | Categoría III, 4 kV | IEC 60255-5 |
| Voltaje de Aislamiento Nominal | 500 V | IEC 60255-5 |
| Prueba de Impulso | 5 kV | IEC 60255-5 |
| Prueba Dieléctrica | 2.5 kV 50/60 Hz @ 1 min | UL-508 |
| Protección al Fuego de la Carcasa | V-0 | UL-94 |
| Material de la Carcasa | Polímeros: LEXAN, ABS, VYDYNE | — |
| Posiciones de Montaje | Sin Restricciones | — |
| Tipos de Montaje | DIN Riel Simétrico, Superficie Plana, Empotrable (Flush Mounting) | — |

### B) Dimensiones y Peso

| Parámetro | Valor |
|-----------|-------|
| Dimensión GSPT | 175 x 90 x 78.0 (L x A x H) mm |
| Dimensión Caja CT | 175 x 90 x 79.8 (L x A x H) mm |
| Dimensión GSPT + Caja CT | 175 x 90 x 157.8 (L x A x H) mm |
| Peso GSPT | 463 g (1.53 lb) |
| Peso Caja CT | 882 g (1.94 lb) |
| Peso GSPT + Caja CT | 1345 g (2.95 lb) |
| Torque de Apretado de Borneras | 5.2 Kg-cm (4.5 Ib-in) |
| Cableado de Borneras | AWG 12-18, L = 7-8 mm (5/16") |
| Cableado por agujeros Caja CT | 0 < 18 mm, máximo AWG 0 |

### C) Características de Control

| Parámetro | Valor | Norma |
|-----------|-------|-------|
| Capacidad de los Contactos | A300 PILOT DUTY, 3 A @ 240 VAC, 1.5 A @ 480 VAC | UL 508 Sección 139.1 |
| Expectativa de Vida Eléctrica | 100,000 Operaciones | — |
| Expectativa de Vida Mecánica | 10,000,000 Operaciones | — |
| Categoría de Uso | AC-15, Capacidad para cargas > 72 VA | IEC 60947-5-1 |

### D) Ajustes de Rango, Mediciones

**Modelo de Voltaje - Multivoltaje (MV)**

| Parámetro | Valor | Precisión |
|-----------|-------|-----------|
| Rango de Medición de Voltaje, Um | 0 → 672 VAC | ±2% VAC |
| Rango de Frecuencia | 45.0 → 70.0 Hz | 1% |
| Factor Potencia Instantáneo | 0.00 → 1.00 | 8% |
| Potencia Aparente Instantánea (kVA) | 0.0 → 999.9 kVA | 4% |
| Potencia Real Instantánea (kW) | 0.0 → 999.9 kW | 4% |
| Consumo de Energía (kWH) | 0 → 999,999 kW/H | 4% |
| Horas de trabajo acumuladas del motor | 0 → 999,999 H | 1% |
| Entrada de Temperatura | -20 °C → 200 °C | 1% |

**Modelo de Corriente**

| Modelo | Rango de Medición (A) |
|--------|----------------------|
| 050 | 4.5 → 500 |
| 100 | 3.0 → 1000 |
| 180 | 5.5 → 1800 |

### E) Funciones y Algoritmos de Protección

#### Protección de Voltaje

| Función | Parámetro | Valor | Observaciones |
|---------|-----------|-------|---------------|
| **Bajo Voltaje (UV)** | Rango ajustable @ Imotor = 0 u OC | -20% → +5% del voltaje nominal | Ajustable (Entrega de Fábrica = -10%) |
| **Sobre Voltaje (OV)** | Rango ajustable @ Imotor = 0 u OC | +5% → +20% del voltaje nominal | Ajustable (Entrega de Fábrica = +10%) |
| **Histéresis de Voltaje** | Umbral | ±3% del voltaje nominal VAC | — |
| **Desbalance de Voltaje (VUB)** | Rango ajustable | 2% → 10% | Ajustable |
| **Pérdida de Fase de Voltaje (VSP)** | Criterio de activación | IN VUB > 33%, OUT VUB < 28% | — |
| **Frecuencia Nominal** | — | 50 ó 60 Hz | Ajustable |
| **Variación de Frecuencia** | Rango ajustable | 2% → 10% | Ajustable |
| **Fase Invertida (PR)** | Detección | Secuencia ABC Normal, Secuencia CBA Invertida | — |

#### Tiempos de Desconexión

| Función | Parámetro | Valor |
|---------|-----------|-------|
| **Temporizado a la Desconexión por Fase Invertida (PR)** | — | < 1 seg |
| **Temporizado a la Desconexión por otras Fallas de Voltaje (TD)** | Rango ajustable | 1 → 30 seg |
| **Temporizado a la Conexión (TC)** | Rango ajustable | 0 → 600 seg |
| **Temporizado a la Desconexión (TD) por VSP** | — | seg |

#### Protección de Corriente

| Función | Parámetro | Valor | Observaciones |
|---------|-----------|-------|---------------|
| **Sobrecarga (OL)** | Ajuste nivel | 5% → 50% | Ajustable |
| **Temporizado conexión por Sobrecarga (OC)** | — | 10 a 60 Minutos | Ajustable |
| **Clase Térmica** | — | Clase 10 | — |
| **Ajuste Dinámico - Modelo del Motor (Curva Fría/Curva Caliente)** | Rango | vara de 1 → 1/3 de clase 10 | Según el tiempo de encendido y nivel de carga del motor |
| **Tiempo Máximo entre curvas Fría/Caliente** | — | 2 Horas (de 1 a 1/3 ó de 1/3 a 1) | IEC 60255-8-1999, IEEE Std. 037.112-1996 |
| **Tiempo Desconexión de Falla por Sobrecarga de Clase 10** | — | Según el nivel de Sobrecarga | — |
| **Umbral de Calor para Falla por Sobrecarga** | — | 100% | — |
| **Desbalance de Corriente (CUB)** | Criterio | CUB > 48% | — |
| **Pérdida de Fase por Corriente (CSP)** | Criterio | CUB > 60% | — |
| **Detección Rotor Bloqueado Acelerado (LR)** | Reajuste | CONTINUO al 100% | — |
| **Temporizado Desconexión por CSP** | — | 3 Seg. | — |
| **Temporizado Desconexión por CUB** | — | 4 Seg. | — |

#### Protección Térmica

| Función | Parámetro | Valor |
|---------|-----------|-------|
| **Tiempo de Enfriamiento Máquina Térmica** | — | 10 Minutos (Ajustable) |

#### Subcarga

| Función | Parámetro | Valor |
|---------|-----------|-------|
| **Subcarga** | Activación | SI/NO |
| **Tipo Desconexión por Subcarga (UC)** | Detección | relativa a corriente Nominal Inom |
| **Temporizado Desconexión por Subcarga (UC)** | Rango | 5 → 600 Min. (Ajustable) |
| **Temporizado Conexión por Subcarga (UC)** | Rango | 2 → 500 (Selección Usuario) |

#### Tercera Falla

| Función | Parámetro | Valor |
|---------|-----------|-------|
| **Detección de Tercera (3ª) Falla** | Activación | SI/NO |
| **Criterio por Tercera (3ª) Falla** | Condición | 3 Fallas de Corriente en menos de 30 min. |
| **Tiempo Desconexión para Detección Rotor Bloqueado Acelerado** | — | 3 Seg |

#### Modo de Rearme

| Parámetro | Valor |
|-----------|-------|
| **Modo de Rearme** | Automático/Manual |
