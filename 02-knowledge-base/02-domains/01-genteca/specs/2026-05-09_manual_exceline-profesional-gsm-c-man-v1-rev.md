```markdown
---
title: "GSM-C Supervisor Monofásico - Manual de Instalación"
type: Technical
source: "GSM-C_MAN_V1_REV.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GSM-C"
date_processed: "2026-05-09"
---

# GSM-C Supervisor Monofásico

## Descripción del Producto

El GSM-C es un supervisor monofásico de voltaje, diseñado para proteger equipos de refrigeración y aires acondicionados ante fallas de voltaje.

## Partes y Piezas

- **LED VERDE**: Indicador de voltaje normal
- **LED ROJO**: Indicador de falla de voltaje
- **Perilla de ajuste de tiempo de conexión**: Ubicada en la parte frontal
- **Gancho de sujeción para riel**: Permite montaje en riel DIN
- **Orificio para montaje en superficie**: Para instalación en panel plano
- **Orificio para montaje en riel**: Para instalación en riel DIN simétrico
- **Terminales de conexión**: F/F1, N/F2, NC, C, NA

## Instalación Mecánica

### Montaje sobre Riel DIN

1. Coloque el GSM-C en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
2. Para retirarlo del riel, use un destornillador plano y hale hacia abajo el gancho de retención ubicado en el dorso del GSM-C.

### Montaje sobre Superficie Plana

1. Coloque el GSM-C sobre la superficie plana del panel donde desea realizar la instalación.
2. Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32".
3. Utilice ramplugs en caso de que realice la instalación sobre una pared.
4. Fije el equipo con un destornillador, usando tornillos de 3/16".

## Instalación Eléctrica

### Paso 1: Preparación

Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

### Paso 2: Conexión de Cables

#### Conexión en 120 V~

- Identifique la fase (F) y el neutro (N) de la red eléctrica a supervisar y conéctelos a los terminales 3 y 4.
- Conecte el voltaje a controlar o interrumpir al terminal 7 (C) y la carga al terminal 8 (NC).

#### Conexión en 220 V~

- Identifique las fases 1 (F/F1) y 2 (F2) de la red eléctrica y conéctelas a los terminales 3 y 4.
- Conecte el voltaje a supervisar al terminal 7 (C) y la carga al terminal 8 (NC).

### Paso 3: Ajuste y Verificación

1. Ajuste la perilla del tiempo de conexión entre 3 y 5 minutos, de acuerdo a los requerimientos de su instalación.
2. Reconecte la energía eléctrica y verifique el funcionamiento del GSM-C y del equipo protegido.

## Diagrama de Conexión Estándar

```
F ——— 3
N ——— 4
         7 (C)  ——— Carga (Bobina del contactor)
         8 (NC)
F1 ———— 3
F2 ———— 4
         7 (C)  ——— Carga (Bobina del contactor)
         8 (NC)
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

- **Conectado Fijo**: Voltaje normal
- **Intermitente**: Tiempo de espera

### Indicador Rojo - Falla de Voltaje

- **Fijo**: Voltaje alto
- **Intermitente**: Voltaje bajo
- **Pulsante**: Inestabilidad
```