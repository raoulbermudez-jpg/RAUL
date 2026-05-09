```markdown
---
title: "GSM-C - Supervisor Monofásico para Refrigeración y Aire Acondicionado"
type: Technical
source: "GSM-C_MAN_V1_Imprimir.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GSM-C"
date_processed: "2026-05-09"
---

# Manual de Instalación - Supervisor Monofásico GSM-C

## Descripción del Producto

El GSM-C es un supervisor monofásico de voltaje, diseñado para proteger equipos de refrigeración y aires acondicionados ante fallas de voltaje. Puede instalarse en montaje sobre riel DIN o sobre superficie plana.

## Partes y Piezas

- LED VERDE: Indicador de voltaje normal
- LED ROJO: Indicador de falla de voltaje
- Perilla de ajuste de tiempo de conexión
- Gancho de sujeción para montaje de riel DIN
- Orificios para montaje en superficie
- Ranura para montaje de riel simétrico
- Terminales: F/F1, N/F2, NC, C, NA

## Instalación Mecánica

### Montaje sobre Riel DIN

- Coloque el GSM-C en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GSM-C y retire el producto del riel.

### Montaje sobre Superficie Plana

- Coloque el GSM-C sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".

## Instalación Eléctrica

### PASO 1: Desconexión de Energía

Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

### PASO 2: Conexión de Cables

#### Conexión en 120 V~

- Identifique la fase (F) y el neutro (N) de la red eléctrica a supervisar.
- Conéctelos a los terminales 3 y 4.
- Conecte el voltaje a controlar o interrumpir al terminal 7 (C) y la carga al terminal 8 (NC).

#### Conexión en 220 V~

- Identifique las fases 1 (F/F1) y 2 (F2) de la red.
- Conéctelos a los terminales 3 y 4.

### PASO 3: Ajuste del Tiempo de Conexión

Ajuste la perilla del tiempo de conexión entre 3 y 5 minutos, de acuerdo a los requerimientos de su instalación.

### PASO 4: Verificación

Reconecte la energía eléctrica y verifique el funcionamiento del GSM-C y del equipo protegido.

## Diagrama de Conexión Estándar

```
Conexión 120 V~        Conexión 220 V~
      F    N                F1   F2
      |    |                |    |
      3    4                3    4
      |    |                |    |
    +----GSM-C----+       +----GSM-C----+
    |             |       |             |
    C      NC     NA      C      NC     NA
    7      6      8       7      6      8
    |      |      |       |      |      |
```

## Descripción de Terminales

| Terminal | Descripción |
|----------|-------------|
| 1, 2, 5 | No utilizado |
| 3 | Entrada de voltaje 1 (F/F1) |
| 4 | Entrada de voltaje 2 (N/F2) |
| 6 | Normalmente Cerrado (NC) |
| 7 | Común (C) |
| 8 | Normalmente Abierto (NA) |

## Indicadores Luminosos

### Indicador Verde - Voltaje Normal
- **Conectado Fijo**: Voltaje dentro de los rangos normales
- **Intermitente Tiempo de Espera**: En período de espera durante la conexión

### Indicador Rojo - Falla de Voltaje
- **Fijo**: Voltaje alto
- **Intermitente**: Voltaje bajo
- **Pulsante**: Inestabilidad de voltaje
```