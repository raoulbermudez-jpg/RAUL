---
title: "GSM-C Supervisor Monofásico"
type: Technical
source: "GSM-C_MAN_V1_C.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GSM-C"
version_status: "historica"
date_processed: "2026-05-10"
---

# GSM-C Supervisor Monofásico

## Descripción General

El GSM-C es un supervisor monofásico de voltaje, diseñado para proteger equipos de refrigeración y aires acondicionados ante fallas de voltaje.

## Partes y Piezas

- **Perilla de ajuste de tiempo de conexión**: Control para ajustar el tiempo de respuesta
- **LED VERDE**: Indicador del estado del relé (voltaje normal)
- **LED ROJO**: Indicador de falla de voltaje
- **Ranura para montaje de riel DIN**: Para instalación en riel simétrico
- **Orificios para montaje en superficie**: Para fijación directa en panel
- **Sujeción para riel simétrico**: Soporte de montaje
- **Gancho de retención**: Ubicado en el dorso para desmontar del riel

## Instalación

### Paso 1: Fijación Mecánica

#### Montaje sobre Riel DIN

- Coloque el GSM-C en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GSM-C y retire el producto del riel.

#### Montaje sobre Superficie Plana

- Coloque el GSM-C sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".

### Paso 2: Instalación Eléctrica

**ADVERTENCIA**: Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

#### Conexión en 120 V~

- Identifique la fase (F) y el neutro (N) de la red eléctrica a supervisar.
- Conéctelos a los terminales 3 y 4 respectivamente.

#### Conexión en 220 V~

- Identifique fase 1 (F1) y fase 2 (F2) de la red eléctrica a supervisar.
- Conéctelos a los terminales 3 y 4 respectivamente.

#### Diagrama de Conexión Estándar

1. Voltaje a controlar o interrumpir (24 V~/230 V~/220 V~) a través de F/F1 y N/F2
2. Conecte los cables de alimentación
3. Conecte el voltaje a controlar o interrumpir al terminal 7 (C) y la carga al terminal 8 (NA)
4. Ajuste la perilla del tiempo de conexión entre 3 y 5 minutos, de acuerdo a los requerimientos de su instalación (rango: 200-280 para valores nominales)
5. Reconecte la energía eléctrica y verifique el funcionamiento del GSM-C y del equipo protegido.

## Terminales

| Terminal | Descripción |
|----------|-------------|
| 1, 2, 5 | No utilizado |
| 3 | Entrada de voltaje 1 (F/F1) |
| 4 | Entrada de voltaje 2 (N/F2) |
| 6 | Normalmente Cerrado (NC) |
| 7 | Común (C) |
| 8 | Normalmente abierto (NA) |

## Indicadores Luminosos

### Indicador Verde (Voltaje Normal)

| Estado | Condición |
|--------|-----------|
| Fijo | Conectado |
| Intermitente | Tiempo de espera |

### Indicador Rojo (Falla de Voltaje)

| Estado | Condición |
|--------|-----------|
| Fijo | Voltaje alto |
| Intermitente | Voltaje bajo |
| Pulsante | Inestabilidad |
