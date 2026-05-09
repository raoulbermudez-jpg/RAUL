```markdown
---
title: "Manual de Supervisor Monofásico de Voltaje para GSM-L"
type: Technical
source: "GSM-L_MAN_V1_REV5.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GSM-L"
date_processed: "2026-05-09"
---

# Manual de Supervisor Monofásico de Voltaje para GSM-L

## Descripción General

El GSM-L de Exceline Profesional es un supervisor de voltaje diseñado para proteger cargas eléctricas hasta 1.5 HP (también se puede utilizar junto con un contactor para proteger cargas superiores) en motores eléctricos monofásicos ante fallas de voltaje como:

- Altos y bajos
- Variaciones extremas
- Inestabilidad o parpadeos

## Partes y Piezas

- Contacto Común
- Contacto NC (Normalmente Cerrado)
- Contacto NA (Normalmente Abierto)
- Perilla de Voltaje Bajo
- Perilla de Voltaje Alto
- Perilla de Tiempo de Reconexión
- LED VERDE: Indicador del estado del relé (voltaje normal)
- LED ROJO: Indicador de falla de voltaje
- Gancho de sujeción para riel DIN
- Orificio de fijación para montaje en superficie

## Instalación

### Montaje sobre Superficie Plana

**PASO 1:**

1. Coloque el GSM-L sobre la superficie plana del panel donde desea realizar la instalación.
2. Marque con un lápiz los orificios.
3. Con un taladro abra dos agujeros de 5/32".
4. Utilice ramplugs en caso de que realice la instalación sobre una pared.
5. Fije el equipo con un destornillador, usando tornillos de 3/16".

### Montaje sobre Riel DIN

1. Coloque el GSM-L en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
2. Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GSM-L y retire el producto del riel.

### Instalación Eléctrica

**PASO 2:**

1. Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

2. Realice la conexión en 120 V~:
   - Identifique la fase (F) y el neutro (N) de la red eléctrica a supervisar y conéctelos a los terminales 3 y 4.

3. Realice la conexión en 220 V~:
   - Identifique fase 1 (A1) y fase 2 (A2) de la red eléctrica a supervisar y conéctelos a los terminales 3 y 4.

4. Conecte el voltaje a controlar o interrumpir al terminal 7 (Contacto Común) y la carga o la salida al contactor al terminal 6 (NA).

5. Ajuste las perillas de voltaje bajo, voltaje alto y tiempo de conexión de acuerdo a los requerimientos de la aplicación.

6. Reconecte la energía eléctrica y verifique el funcionamiento del GSM-L y del equipo protegido.

## Indicadores Luminosos LED

### INDICADOR LED VERDE

| Estado | Condición |
|--------|-----------|
| Fijo | Voltaje normal |
| Intermitente | Tiempo de espera |

### INDICADOR LED ROJO - Falla de Voltaje Alto

| Estado | Condición |
|--------|-----------|
| Fijo | Voltaje alto |
| Intermitente | Inestabilidad |

### INDICADOR LED ROJO - Falla de Voltaje Bajo

| Estado | Condición |
|--------|-----------|
| Fijo | Voltaje bajo |
| Intermitente | Inestabilidad |

## Diagrama de Conexión Estándar

### Terminales - Descripción

| Terminal | Descripción |
|----------|-------------|
| 1, 2, 8 | No utilizado |
| 3 | Entrada de voltaje fase 1 (A1) |
| 4 | Entrada de voltaje fase 2 (A2) |
| 5 | Contacto normalmente cerrado (NC) |
| 6 | Contacto normalmente abierto (NA) |
| 7 | Contacto común (C) |

### Conexiones de Entrada

- **120 ó 220 V~**: F/A1 y N/A2
- **Carga o Bobina del contactor**: Voltaje a controlar o interrumpir
```