```markdown
---
title: "Manual de Instalación - Supervisor Monofásico para Refrigeración GSM-C"
type: Technical
source: "GSM-C_MAN_V2_IMP.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GSM-C"
date_processed: "2026-05-09"
---

# Manual de Instalación - Supervisor Monofásico para Refrigeración GSM-C

## Descripción del Producto

El GSM-C de Exceline Profesional es un supervisor monofásico de voltaje, diseñado para proteger equipos de refrigeración y aires acondicionados ante fallas de voltaje.

## Partes y Piezas

- **Contacto Común**: Terminal de conexión común
- **Contacto NA**: Contacto normalmente abierto
- **Contacto NC**: Contacto normalmente cerrado
- **Perilla de Voltaje Alto**: Ajuste de límite superior de voltaje
- **Perilla de Voltaje Bajo**: Ajuste de límite inferior de voltaje
- **Perilla de Tiempo de Conexión**: Ajuste del tiempo de espera
- **LED VERDE**: Indicador del estado del relé
- **LED ROJO (Voltaje Alto)**: Indicador de falla de voltaje alto
- **LED ROJO (Voltaje Bajo)**: Indicador de falla de voltaje bajo
- **Gancho de Sujeción**: Para montaje en riel simétrico
- **Ranura para Riel**: Para montaje sobre riel DIN
- **Orificios para Montaje**: Para montaje en superficie plana

## Instalación

### Paso 1: Fijación Mecánica del Dispositivo

La fijación puede realizarse en montaje sobre riel DIN o sobre superficie plana.

#### Montaje sobre Riel DIN

- Coloque el GSM-C en posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo: con un destornillador plano, hale hacia abajo el gancho de retención ubicado en el dorso del GSM-C y retire el producto del riel.

#### Montaje sobre Superficie Plana

- Coloque el GSM-C sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".
- Dimensiones: 51 mm × 88 mm

### Paso 2: Instalación Eléctrica del Producto

**Advertencia**: Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

#### Conexión en 120 V~

- Identifique la fase (F) y el neutro (N) de la red eléctrica a supervisar.
- Conéctelos a los terminales 3 y 4 respectivamente.

#### Conexión en 220 V~

- Identifique fase 1 (A1) y fase 2 (A2) de la red eléctrica a supervisar.
- Conéctelos a los terminales 3 y 4 respectivamente.

#### Conexión de Carga

- Conecte el voltaje a controlar o interrumpir al terminal 7 (Contacto Común).
- Conecte la carga o salida al contactor al terminal 8 (NA).

#### Ajustes y Verificación

- Ajuste las perillas de voltaje bajo, voltaje alto y tiempo de conexión de acuerdo a los requerimientos de la aplicación.
- Reconecte la energía eléctrica y verifique el funcionamiento del GSM-C y del equipo protegido.

## Indicadores Luminosos LED

### LED VERDE - Indicador de Estado Normal

| Estado | Comportamiento |
|--------|---|
| Voltaje Normal Conectado | Fijo |
| Tiempo de Espera | Intermitente |

### LED ROJO - Indicador de Falla de Voltaje Alto

| Estado | Comportamiento |
|--------|---|
| Voltaje Alto | Fijo |
| Inestabilidad | Intermitente |

### LED ROJO - Indicador de Falla de Voltaje Bajo

| Estado | Comportamiento |
|--------|---|
| Voltaje Bajo | Fijo |
| Inestabilidad | Intermitente |

## Diagrama de Conexión Estándar

**Entrada de Voltaje a Controlar o Interrumpir** → Terminal A1/F y A2/N (120 ó 220 V~)

**Salida de Carga o Bobina del Contactor** → Terminal de Contacto (C) y Contacto Normalmente Abierto (NA)

## Tabla de Terminales

| Terminal | Descripción |
|----------|-------------|
| 1, 2, 6 | No utilizado |
| 3 | Entrada de voltaje 1 (A1/F) |
| 4 | Entrada de voltaje 2 (A2/N) |
| 5 | Contacto normalmente cerrado (NC) |
| 7 | Contacto común (C) |
| 8 | Contacto normalmente abierto (NA) |
```