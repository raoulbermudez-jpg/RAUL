```markdown
---
title: "Manual de Supervisor Monofásico de Voltaje para GSM-L"
type: Technical
source: "GSM-L_MAN_V1_REV1.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GSM-L"
date_processed: "2026-05-09"
---

# Manual de Supervisor Monofásico de Voltaje para GSM-L

## Descripción del Producto

El GSM-L de Exceline Profesional es un supervisor de voltaje diseñado para proteger cargas de 1 HP en montaje sobre riel DIN o sobre superficie plana. (También se puede utilizar junto con un contactor para proteger cargas superiores) en motores eléctricos monofásicos ante fallas de voltaje como alto, bajo voltaje, variaciones extremas, inestabilidad o parpadeos.

## Partes y Piezas

- Perilla de ajuste del valor de desconexión por voltaje bajo
- LED VERDE: Indicador del estado del relé
- LED ROJO: Indicador de falla de voltaje
- Orificio para montaje en riel DIN (simétrico)
- Orificio para montaje en superficie
- Terminales: NA, C, NC, F/F1, N/F2

## Instalación

### Paso 1: Fijación Mecánica

#### Montaje sobre Superficie Plana

- Coloque el GSM-L sobre la superficie plana del panel donde desea realizar la instalación
- Marque con un lápiz los orificios
- Con un taladro abra dos agujeros de 5/32"
- Utilice ramplugs en caso de que realice la instalación sobre una pared
- Fije el equipo con un destornillador, usando tornillos de 3/16"

#### Montaje sobre Riel DIN

- Coloque el GSM-L en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GSM-L y retire el producto del riel

### Paso 2: Instalación Eléctrica

1. **Desconecte el breaker** antes de iniciar el trabajo eléctrico para evitar accidentes

2. **Conecte los cables de alimentación:**

   **Conexión en 120 V~**
   - Identifique la fase (F) y el neutro (N) de la red eléctrica a supervisar
   - Conéctelos a los terminales 3 y 4
   - Conecte el voltaje a controlar o interrumpir al terminal 6 (C) y la carga o la salida al contactor al terminal 5 (NA)

   **Conexión en 220 V~**
   - Identifique fase 1 (F1) y fase 2 (F2) de la red eléctrica a supervisar
   - Conéctelos a los terminales 3 y 4

3. **Ajuste la perilla de bajo voltaje** de acuerdo a los niveles requeridos por su instalación

4. **Reconecte la energía eléctrica** y verifique el funcionamiento del GSM-L y del equipo protegido

## Diagrama de Conexión Estándar

```
Voltaje a controlar o interrumpir (24 V~/230 V~/220 V~)
├─ F/F1 (Terminal 3)
├─ N/F2 (Terminal 4)
├─ NA (Terminal 5) → Carga o Bobina del contactor
└─ C (Terminal 6)
```

## Descripción de Terminales

| Terminal | Descripción |
|----------|-------------|
| 1, 2, 8 | No utilizado |
| 3 | Entrada de voltaje 1 (F/F1) |
| 4 | Entrada de voltaje 2 (N/F2) |
| 5 | Normalmente abierto (NA) |
| 6 | Común (C) |
| 7 | Normalmente Cerrado (NC) |

## Indicadores Luminosos

### Indicador Verde - Voltaje Normal

| Estado | Significado |
|--------|------------|
| Conectado Fijo | Voltaje normal |
| Intermitente | Tiempo de espera |

### Indicador Rojo - Falla de Voltaje

| Estado | Significado |
|--------|------------|
| Fijo | Voltaje alto |
| Intermitente | Voltaje bajo |
| Pulsante | Inestabilidad |
```