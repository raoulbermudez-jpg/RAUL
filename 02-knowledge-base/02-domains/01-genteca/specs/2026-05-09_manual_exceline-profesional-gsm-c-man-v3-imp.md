```markdown
---
title: "GSM-C Manual de Instalación - Supervisor Monofásico para Refrigeración"
type: Technical
source: "GSM-C_MAN_V3_IMP.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GSM-C"
date_processed: "2026-05-09"
---

# Manual de Instalación - Supervisor Monofásico para Refrigeración GSM-C

## Descripción del Producto

El GSM-C es un supervisor monofásico de voltaje, diseñado para proteger equipos de refrigeración y aires acondicionados ante fallas de voltaje.

## Partes y Piezas

- **Orificio para montaje**: Permite fijación en superficie
- **Contacto Común**: Terminal de conexión
- **Contacto NA**: Contacto normalmente abierto en superficie
- **Contacto NC**: Contacto normalmente cerrado
- **Perilla de Voltaje Bajo**: Ajuste de umbral bajo
- **Perilla de Voltaje Alto**: Ajuste de umbral alto
- **LED VERDE**: Indicador del estado del relé
- **LED ROJO**: Indicador de falla de voltaje alto
- **LED ROJO**: Indicador de falla de voltaje bajo
- **Perilla de Tiempo de Conexión**: Ajuste de tiempo
- **Ranura para montaje de Riel**: Para montaje en riel DIN
- **Gancho de Sujeción**: Para riel simétrico
- **Terminales A1/F y A2/N**: Entradas de voltaje

## Instalación

### Paso 1: Montaje Mecánico

Fije mecánicamente el dispositivo mediante montaje en riel DIN o sobre superficie plana.

#### Montaje sobre Riel DIN

- Coloque el GSM-C en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel: con un destornillador plano hale hacia abajo el gancho de retención ubicado en el dorso del GSM-C y retire el producto del riel.

#### Montaje sobre Superficie Plana

- Coloque el GSM-C sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".
- Dimensiones: 88 mm × 51 mm

### Paso 2: Instalación Eléctrica

**ADVERTENCIA**: Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

#### Conexión en 120 V~

- Identifique la fase (F) y el neutro (N) de la red eléctrica a supervisar.
- Conéctelos a los terminales 3 y 4 respectivamente.

#### Conexión en 220 V~

- Identifique fase 1 (A1) y fase 2 (A2) de la red eléctrica a supervisar.
- Conéctelos a los terminales 3 y 4 respectivamente.

#### Conexión de Carga

- Conecte el voltaje a controlar o interrumpir al terminal 7 (Contacto Común).
- Conecte la carga o salida al contactor al terminal 8 (NA).

#### Ajustes Finales

- Ajuste las perillas de voltaje bajo, voltaje alto y tiempo de conexión de acuerdo a los requerimientos de la aplicación.
- Reconecte la energía eléctrica y verifique el funcionamiento del GSM-C y del equipo protegido.

## Indicadores Luminosos LED

### LED VERDE - Voltaje Normal

| Estado | Indicación |
|--------|-----------|
| Fijo | Voltaje conectado |
| Intermitente | Tiempo de espera |

### LED ROJO - Falla de Voltaje Alto

| Estado | Indicación |
|--------|-----------|
| Fijo | Voltaje alto |
| Intermitente | Inestabilidad |

### LED ROJO - Falla de Voltaje Bajo

| Estado | Indicación |
|--------|-----------|
| Fijo | Voltaje bajo |
| Intermitente | Inestabilidad |

## Diagrama de Conexión Estándar

```
Voltaje a controlar o interrumpir (A1/F - 120 ó 220 V~)
                    ↓
            [GSM-C SUPERVISOR]
                    ↓
        Terminal 7 (Común C)
                    ↓
        Carga o Bobina del contactor
                    ↓
        Terminal 8 (Normalmente Abierto NA)
```

## Terminales - Descripción

| Terminal | Descripción |
|----------|-------------|
| 1, 2, 6 | No utilizado |
| 3 | Entrada de voltaje 1 (A1/F) |
| 4 | Entrada de voltaje 2 (A2/N) |
| 5 | Contacto normalmente cerrado (NC) |
| 7 | Contacto común (C) |
| 8 | Contacto normalmente abierto (NA) |
```