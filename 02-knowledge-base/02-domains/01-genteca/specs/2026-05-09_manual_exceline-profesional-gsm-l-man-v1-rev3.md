---
title: "Manual de Supervisor Monofásico de Voltaje para GSM-L"
type: Technical
source: "GSM-L_MAN_V1_REV3.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GSM-L"
date_processed: "2026-05-09"
---

# Manual de Supervisor Monofásico de Voltaje para GSM-L

## Descripción del Producto

El GSM-L de Exceline Profesional es un supervisor de voltaje diseñado para proteger cargas de 1 HP (también se puede utilizar junto con un contactor para proteger cargas superiores) en motores eléctricos monofásicos ante fallas de voltaje como:

- Altos y bajos voltajes
- Variaciones extremas
- Inestabilidad o parpadeos

## Partes y Piezas

- Contacto Común
- Contacto NC (Normalmente Cerrado)
- Contacto NA (Normalmente Abierto)
- Perilla de ajuste por Voltaje Bajo
- Perilla de ajuste por Voltaje Alto
- Perilla de ajuste de Tiempo de conexión
- LED VERDE - Indicador del estado del relé (voltaje normal)
- LED ROJO - Indicador de falla
- Gancho de sujeción para riel
- Orificios para montaje en superficie

## Instalación

### Montaje sobre Superficie Plana

- Coloque el GSM-L sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".

### Montaje sobre Riel DIN

- Coloque el GSM-L en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GSM-L y retire el producto del riel.

## Instalación Eléctrica

### Paso 1: Preparación de Seguridad

Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

### Paso 2: Conexión en 120 V~

- Identifique la fase (F) y el neutro (N) de la red eléctrica a supervisar y conéctelos a los terminales 3 y 4.
- Conecte el voltaje a controlar o interrumpir al terminal 7 (Contacto Común) y la carga o la salida al contactor al terminal 6 (NA).

### Paso 3: Conexión en 220 V~

- Identifique fase 1 (A1) y fase 2 (A2) de la red eléctrica a supervisar y conéctelos a los terminales 3 y 4.

### Paso 4: Ajuste y Verificación

- Ajuste las perillas de voltaje bajo, voltaje alto y tiempo de conexión de acuerdo a los requerimientos de la aplicación.
- Reconecte la energía eléctrica y verifique el funcionamiento del GSM-L y del equipo protegido.

## Diagrama de Conexión Estándar

```
F/A1 ─── Terminal 3
N/A2 ─── Terminal 4

Terminal 7 (Contacto Común) ─── Carga o Bobina del contactor
Terminal 6 (NA) ─── Voltaje a controlar o interrumpir

120 ó 220 V~
```

## Indicadores Luminosos LED

### INDICADOR VERDE
- **Voltaje Normal**: Conectado Fijo
- **Tiempo de espera**: Intermitente

### INDICADOR ROJO
- **Voltaje Alto**: Fijo
- **Inestabilidad**: Intermitente
- **Voltaje Bajo**: Fijo
- **Inestabilidad**: Intermitente

## Descripción de Terminales

| Terminal | Descripción |
|----------|-------------|
| 1, 2, 8 | No utilizado |
| 3 | Entrada de voltaje fase 1 (A1) |
| 4 | Entrada de voltaje fase 2 (A2) |
| 5 | Contacto normalmente cerrado (NC) |
| 6 | Contacto normalmente abierto (NA) |
| 7 | Contacto común (C) |