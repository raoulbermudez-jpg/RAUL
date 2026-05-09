---
title: "GST-RM Manual de Instalación"
type: Technical
source: "GST-RM_MAN_V1.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GST-RM"
date_processed: "2026-05-09"
---

# Manual de Instalación GST-RM
## Supervisor Trifásico para Motores, Transferencias y Sistemas de Distribución

El Supervisor Trifásico para motores, Transferencias y Sistemas de Distribución GST-RM es un relé electrónico de protección, diseñado para evitar los daños que ocasionan las fluctuaciones de voltaje, pérdida de fase, fase invertida y corrimiento de frecuencia en motores, transferencias, sistemas de distribución y bombas trifásicas.

## Partes y Piezas

- **Perilla de ajuste de voltaje bajo**
- **Perilla de ajuste de tiempo de desconexión**
- **Perilla de ajuste de tiempo de conexión**
- **Orificio para montaje en superficie**
- **Ranura para montaje de riel**
- **Topes para montaje de riel**
- **Indicador verde** - Estado del relé
- **Indicador rojo** - Falla de voltaje
- **Gancho de sujeción** - Para riel simétrico
- **Terminales**: 98, 95, 96, L1, L2, L3

## Instalación

### Montaje sobre Riel DIN

**PASO 1:**
- Coloque el GST-RM en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GST-RM y retire el producto del riel.

### Montaje sobre Superficie Plana

**PASO 1:**
- Coloque el GST-RM sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".

### Instalación Eléctrica

**PASO 2:**

1. **Desconecte el breaker** antes de iniciar el trabajo eléctrico para evitar accidentes.

2. **Conecte los cables de alimentación:**
   - Identifique la fase 1 (L1), fase 2 (L2) y fase 3 (L3) de la red eléctrica a supervisar y conéctelos al supervisor GST-RM y a la entrada del contactor.

3. **Ajuste la perilla de voltaje bajo** de acuerdo a los requerimientos de su instalación. En caso de no tenerlos, ajuste la perilla en el valor recomendado dentro del rango sugerido (370-410 V~).

4. **Ajuste las perillas de tiempo de desconexión y conexión** de acuerdo a los requerimientos de su instalación.
   - **Tiempo de desconexión:** 0.5 a 10 segundos
   - **Tiempo de conexión:** 0.05 a 60 segundos

5. **Realice las conexiones según el diagrama estándar:**
   - Terminal 98-95 conectado (Normal)
   - Terminal 99-96 abierto (Falla)
   - El extremo A1 del contactor se conecta con el terminal 98
   - El extremo A2 se conecta con L1
   - El terminal 95 se conecta con L2

6. **Reconecte la energía eléctrica** y verifique el funcionamiento del GST-RM y del equipo protegido.

**Nota:** Tenga presente que el calibre de los cables que van hacia el contactor sea el adecuado según la carga que maneja el motor.

## Indicadores Luminosos

### Indicador Verde - VOLTAJE NORMAL
- **Fijo:** Conectado
- **Intermitente:** Tiempo de espera

### Indicador Rojo - FALLA DE VOLTAJE
- **Fijo:** Sobre voltaje
- **Intermitente:** Bajo voltaje / Fase invertida
- **Pulsante:** Desbalance / Falla de frecuencia
- **Pérdida de fase:** Fijo

## Descripción de Terminales

| Terminal | Descripción |
|----------|-------------|
| 98 | Normalmente abierto (NA) |
| 95 | Común (C) |
| 96 | Normalmente cerrado (NC) |
| L1 | Fase L1 |
| L2 | Fase L2 |
| L3 | Fase L3 |