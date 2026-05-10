---
title: "GST-RR - Manual de Instalación para Refrigeración y Aire Acondicionado"
type: Technical
source: "GST-RR_MAN_V1.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GST-RR"
date_processed: "2026-05-09"
---

# GST-RR - Manual de Instalación y Aire Acondicionado

## Descripción del Producto

El Supervisor Trifásico para Refrigeración y Aire Acondicionado GST-RR es un relé electrónico de protección, diseñado para evitar los daños que ocasionan las fluctuaciones de voltaje, pérdida de fase, fase invertida y corrimiento de frecuencia en compresores trifásicos y equipos de refrigeración y aire acondicionado.

El GST-RR es un relé en montaje sobre riel DIN o sobre superficie plana.

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

### PASO 1: Fijación Mecánica

Realice la fijación mecánica del dispositivo según el tipo de montaje seleccionado.

### PASO 2: Instalación de Conexiones Eléctricas

1. **Desconecte el breaker** antes de iniciar el trabajo eléctrico para evitar accidentes.

2. **Identifique las fases**: Identifique la fase 1 (L1), fase 2 (L2) y fase 3 (L3) de la red eléctrica a supervisar y conéctelos al supervisor GST-RR y a la entrada del contactor.

3. **Ajuste de perillas de voltaje**:
   - Ajuste la perilla de voltaje bajo y voltaje alto de acuerdo a los valores recomendados dentro del rango sugerido.
   - En casos donde no tenga claros los valores, ajústelas en el valor recomendado dentro del rango sugerido.

4. **Conexión con contactor**:
   - El extremo A1 del contactor se conecta con el terminal 98.
   - El extremo A2 se conecta con L1.
   - El terminal 95 se conecta con L2.
   - El terminal 96 se conecta con L3.

5. **Nota de calibre de cables**: Tenga presente que el calibre de los cables que van hacia el contactor sea el adecuado según la carga que maneja el motor.

6. **Verificación final**: Reconecte la energía eléctrica y verifique el funcionamiento del GST-RR y del equipo protegido.

## Indicadores Luminosos

### Indicador Verde - Voltaje Normal
- **Conectado Fijo**: Funcionamiento normal
- **Intermitente**: Equipo en espera de conexión

### Indicador Rojo - Falla de Voltaje
- **Sobre voltaje - Fijo**: Voltaje alto
- **Bajo voltaje - Intermitente**: Voltaje bajo
- **Desbalance - Pulsante**: Desbalance entre fases
- **Fase invertida - Intermitente**: Inversión de fase
- **Falla de frecuencia - Pulsante**: Corrimiento de frecuencia

## Diagrama de Conexión Estándar

| Condición | Terminal | Estado |
|-----------|----------|--------|
| Normal | 98-95 conectado | Normal |
| Falla | 96-95 abierto | Falla |

## Terminales de Conexión

| Terminal | Descripción |
|----------|-------------|
| 98 | Normalmente abierto (NA) |
| 95 | Común (C) |
| 96 | Normalmente cerrado (NC) |
| L1 | Fase L1 |
| L2 | Fase L2 |
| L3 | Fase L3 |