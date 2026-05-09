```markdown
---
title: "GSM-C Manual de Instalación - Supervisor Monofásico para Refrigeración"
type: Technical
source: "GSM-C_MAN_V3.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GSM-C"
date_processed: "2026-05-09"
---

# Manual de Instalación - GSM-C
## Supervisor Monofásico para Refrigeración

El GSM-C es un supervisor monofásico de voltaje, diseñado para proteger equipos de refrigeración y aires acondicionados ante fallas de voltaje.

## Partes y Piezas

- Orificio para montaje en superficie
- Contacto Común
- Contacto NA en superficie
- Contacto NC
- Perilla de Voltaje Bajo
- Perilla de Voltaje Alto
- Perilla de Indicador del Tiempo de Conexión
- LED VERDE: Indicador del estado del relé
- LED ROJO: Indicador de falla de voltaje alto
- LED ROJO: Indicador de falla de voltaje bajo
- Ranura para montaje de Riel DIN
- Gancho de sujeción para riel simétrico
- Orificio para montaje en superficie
- Terminales A1/F y A2/N

## Instalación

### Paso 1: Montaje Mecánico

Fije mecánicamente el dispositivo mediante montaje en riel DIN o sobre superficie plana.

#### Montaje sobre Riel DIN

- Coloque el GSM-C en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GSM-C y retire el producto del riel.

#### Montaje sobre Superficie Plana

- Coloque el GSM-C sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".

Dimensiones: 51 mm de ancho, 88 mm de alto.

### Paso 2: Instalación Eléctrica

#### Precaución

Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

#### Conexión de Alimentación

**Conexión en 120 V~**
- Identifique la fase (F) y el neutro (N) de la red eléctrica a supervisar y conéctelos a los terminales 3 y 4.

**Conexión en 220 V~**
- Identifique fase 1 (A1) y fase 2 (A2) de la red eléctrica a supervisar y conéctelos a los terminales 3 y 4.

#### Conexión de Carga

Conecte el voltaje a controlar o interrumpir al terminal 7 (Contacto Común) y la carga o salida al contactor al terminal 8 (NA).

#### Ajuste y Verificación

- Ajuste las perillas de voltaje bajo, voltaje alto y tiempo de conexión de acuerdo a los requerimientos de la aplicación.
- Reconecte la energía eléctrica y verifique el funcionamiento del GSM-C y del equipo protegido.

## Indicadores Luminosos LED

### Indicador LED Verde
- **Voltaje Normal Conectado**: Fijo
- **Tiempo de Espera**: Intermitente

### Indicador LED Rojo - Falla de Voltaje Alto
- **Voltaje Alto**: Fijo
- **Inestabilidad**: Intermitente

### Indicador LED Rojo - Falla de Voltaje Bajo
- **Voltaje Bajo**: Fijo
- **Inestabilidad**: Intermitente

## Diagrama de Conexión Estándar

```
Voltaje a controlar          A1/F ─────┐
o interrumpir                          │ GSM-C
                             A2/N ─────┤
                                       │
120 ó 220 V~                           │
                             Terminal 7 (C)
                             Terminal 8 (NA)
                                       │
                            Carga o Bobina
                            del contactor
```

## Descripción de Terminales

| Terminal | Descripción |
|----------|-------------|
| 1, 2, 6 | No utilizado |
| 3 | Entrada de voltaje 1 (A1/F) |
| 4 | Entrada de voltaje 2 (A2/N) |
| 5 | Contacto normalmente cerrado (NC) |
| 7 | Contacto común (C) |
| 8 | Contacto normalmente abierto (NA) |
```