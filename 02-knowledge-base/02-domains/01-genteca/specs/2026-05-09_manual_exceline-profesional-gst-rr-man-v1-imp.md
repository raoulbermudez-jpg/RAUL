```markdown
---
title: "Manual de Instalación GST-RR - Supervisor Trifásico para Refrigeración y Aire Acondicionado"
type: Technical
source: "GST-RR_MAN_V1_IMP.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GST-RR"
date_processed: "2026-05-09"
---

# Manual de Instalación GST-RR

## Descripción del Producto

El Supervisor Trifásico para Refrigeración y Aire Acondicionado GST-RR es un relé (relevador) electrónico de protección, diseñado para evitar los daños que ocasionan las fluctuaciones de voltaje, pérdida de fase, fase invertida y corrimiento de frecuencia en compresores trifásicos y equipos de refrigeración y aire acondicionado.

## Partes y Piezas

- Perilla de ajuste de voltaje bajo
- Perilla de ajuste de voltaje alto
- Perilla de ajuste de tiempo de conexión
- Orificio para montaje en superficie
- Ranura para montaje de riel
- Topes para montaje de riel
- Indicador verde - Estado del relé
- Indicador rojo - Falla de voltaje
- Gancho de sujeción para riel simétrico
- Terminales: 98, 95, 96, L1, L2, L3

## Instalación

### Montaje sobre Riel DIN

- Coloque el GST-RR en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GST-RR y retire el producto del riel.

### Montaje sobre Superficie Plana

- Coloque el GST-RR sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".

## Instalación Eléctrica

### Paso 1: Preparación de Seguridad

Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

### Paso 2: Conexión de Fases

- Identifique la fase 1 (L1), fase 2 (L2) y fase 3 (L3) de la red eléctrica a supervisar.
- Conéctelos al supervisor GST-RR y a la entrada del contactor.

### Paso 3: Ajuste de Voltajes

Ajuste las perillas de voltaje bajo y voltaje alto de acuerdo a los valores recomendados:

**Rango de Voltaje Bajo:** 165 - 195 V

**Rango de Voltaje Alto:** 240 - 270 V

En caso de no tenerlos, ajústelas en el valor recomendado dentro del rango sugerido.

### Paso 4: Ajuste del Tiempo de Conexión

Ajuste la perilla de tiempo de conexión de acuerdo a los requerimientos de su instalación.

### Paso 5: Conexión del Contactor

- El extremo A1 del contactor se conecta con el terminal 98.
- El extremo A2 se conecta con L1.
- El terminal 95 se conecta con L2.
- El terminal 96 se conecta con L3.

*Tenga presente que el calibre de los cables que van hacia el contactor sea el adecuado según la carga que maneja el motor.

### Paso 6: Verificación

Reconecte la energía eléctrica y verifique el funcionamiento del GST-RR y del equipo protegido.

## Diagrama de Conexión Estándar

**Normal:** 98-95 conectado
**Falla:** 96-95 abierto

```
Equipo
a proteger          Contactor
        x
        A1  A2  L1
    3 ~ L2
        L3

                    98  95  96  L1  L2  L3
                    [GST-RR]
```

## Descripción de Terminales

| TERMINAL | DESCRIPCIÓN |
|----------|-------------|
| 98 | Normalmente abierto (NA) |
| 95 | Común (C) |
| 96 | Normalmente cerrado (NC) |
| L1 | Fase L1 |
| L2 | Fase L2 |
| L3 | Fase L3 |

## Indicadores Luminosos

### Indicador Verde - VOLTAJE NORMAL

| Estado | Significado |
|--------|-------------|
| Conectado Fijo | Voltaje normal |
| Intermitente | Voltaje bajo (rango 165-195 V) o Voltaje alto (rango 240-270 V) |

### Indicador Rojo - FALLA DE VOLTAJE

| Estado | Significado |
|--------|-------------|
| Fijo | Sobre voltaje (> 270 V) |
| Intermitente | Bajo voltaje (< 165 V) o Fase invertida |
| Pulsante | Desbalance o Falla de frecuencia |

```