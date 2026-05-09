```markdown
---
title: "Supervisor Monofásico GSM-C - Manual de Instalación"
type: Technical
source: "GSM-C_MAN_V1.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GSM-C"
date_processed: "2026-05-09"
---

# Supervisor Monofásico para Refrigeración y Aire Acondicionado GSM-C

## Descripción del Producto

El GSM-C es un supervisor monofásico de voltaje, diseñado para proteger equipos de refrigeración y aire acondicionado ante fallas de voltaje. Puede ser instalado en montaje sobre riel DIN o sobre superficie plana.

## Partes y Piezas

- Perilla de ajuste de tiempo de conexión
- LED VERDE - Indicador de voltaje normal
- LED ROJO - Indicador de falla de voltaje
- Gancho de sujeción para riel
- Ranura para montaje de Riel DIN
- Orificios para montaje en superficie
- Terminales: F/F1, N/F2, NC, C, NA

## PASO 1: Fijación Mecánica

### Montaje sobre Riel DIN

- Coloque el GSM-C en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GSM-C y retire el producto del riel.

### Montaje sobre Superficie Plana

- Coloque el GSM-C sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".

## PASO 2: Instalación Eléctrica

### Paso 2.1: Desconectar Breaker
Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

### Paso 2.2: Conectar Cables de Alimentación

**Conexión en 120 V~**
- Identifique la fase (F) y el neutro (N) de la red eléctrica a supervisar y conéctelos a los terminales 3 y 4.

**Conexión en 220 V~**
- Conecte las fases F1 y F2 de la red a los terminales 3 y 4.

### Paso 2.3: Conectar la Carga
- Conecte el voltaje a controlar o interrumpir al terminal 7 (C) y la carga al terminal 8 (NA).
- La carga se conecta típicamente a la bobina del contactor.

### Paso 2.4: Ajustar Tiempo de Conexión
Ajuste la perilla del tiempo de conexión entre 180 y 300 segundos (3 y 5 minutos) de acuerdo con los requerimientos de su instalación.

### Paso 2.5: Reconexión y Verificación
Reconecte la energía eléctrica y verifique el funcionamiento del GSM-C y del equipo protegido.

## Indicadores Luminosos

### INDICADOR VERDE - Voltaje Normal
- **Conectado Fijo**: Voltaje dentro del rango normal
- **Intermitente con Tiempo de Espera**: Sistema en período de espera

### INDICADOR ROJO - Falla de Voltaje
- **Fijo**: Voltaje alto
- **Intermitente**: Voltaje bajo
- **Pulsante**: Inestabilidad del voltaje

## Diagrama de Conexión Estándar

| Terminal | Descripción |
|----------|-------------|
| 1, 2, 5 | No utilizado |
| 3 | Entrada de voltaje 1 (F/F1) |
| 4 | Entrada de voltaje 2 (N/F2) |
| 6 | Normalmente Cerrado (NC) |
| 7 | Común (C) |
| 8 | Normalmente Abierto (NA) |

```