```markdown
---
title: "Protector de Sobrecarga Trifásico para Compresores de Refrigeración y Aire Acondicionado GSC-CR"
type: Technical
source: "GSC-CR_MAN-DES_V1_IMP.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GSC-CR"
date_processed: "2026-05-09"
---

# Protector de Sobrecarga Trifásico para GSC-CR

## Descripción General

El Protector de Sobrecarga Trifásico para Compresores de Refrigeración y Aire Acondicionado GSC-CR es un relé térmico electrónico con protección de voltaje, el cual monitorea constantemente las corrientes del compresor, los voltajes de alimentación y mediante un algoritmo inteligente realiza la desconexión en función del calentamiento del compresor.

## Instalación

### Paso 1: Fijación Mecánica del Dispositivo

#### a) Montaje sobre Riel DIN

1. Coloque el GSC-CR en una posición inclinada
2. Encaje el producto en el riel por la ranura desde la parte superior
3. Hale hacia abajo con un destornillador plano la pestaña de retención ubicada en el dorso del producto
4. Encájela en el riel para fijarlo
5. Para retirarlo del riel, repita el procedimiento

#### b) Montaje sobre Superficie Plana

1. Saque los dos (2) sujetadores insertables localizados en la parte posterior
2. Coloque el GSC-CR sobre la superficie plana del panel donde desea realizar la instalación
3. Marque con un lápiz los orificios
4. Con un taladro abra dos agujeros de 5/32"
5. Utilice ramplugs en caso de que realice la instalación sobre una pared
6. Inserte ambos sujetadores dentro de las ranuras verticales de la parte posterior del GSC-CR
7. Fije el equipo con un destornillador, usando tornillos de 3/16"

### Paso 2: Instalación Eléctrica

1. Realice la instalación eléctrica del producto de acuerdo al diagrama de conexión
2. Identifique la fase 1 (L1), fase 2 (L2) y fase 3 (L3) de la red
3. Conecte los cables de alimentación
4. Conecte los cables para activar el contactor

## Partes y Piezas

- Indicadores luminosos
- Perilla de ajuste de corriente (FLA)
- Perilla de ajuste de tiempo de conexión (TC)
- Botón de RESET
- Sensores de Corriente

## Terminales de Conexión

| TERMINAL | DESCRIPCIÓN |
|----------|-------------|
| L1 | Fase L1 |
| L2 | Fase L2 |
| L3 | Fase L3 |
| 95-96 | Conectado |
| 97-98 | Disparado/Abierto |

## Indicadores Luminosos y Descripción de Fallas

El GSC-CR presenta indicadores luminosos tipo LED's para señalizar fallas y el estado de operación del sistema. En caso de presentarse varias fallas, el equipo las señalizará en simultáneo.

### Indicador Verde

| ESTADO | CONDICIÓN |
|--------|-----------|
| Luz Continua | Conectado |
| Luz Intermitente | Temporizando (TC) |

### Indicador Rojo 1

| ESTADO | CONDICIÓN |
|--------|-----------|
| Luz Continua | Falla por sobrecarga (OL) |
| Luz Intermitente | Falla por fase invertida (PR) |

### Indicador Rojo 2

| ESTADO | CONDICIÓN |
|--------|-----------|
| Luz Continua | Falla por desbalance de voltaje o corriente (UB) |
| Luz Intermitente | Pérdida de fase de voltaje o corriente (UB) |

### Indicador Rojo 3

| ESTADO | CONDICIÓN |
|--------|-----------|
| Luz Continua | Falla por sobrevoltaje (OV) |
| Luz Intermitente | Falla por bajo voltaje (UV) |

## Operación del GSC-CR

El GSC-CR supervisa constantemente la corriente del motor y los voltajes de línea. Cuando alguna condición de sobrecarga o falla de fase ocurre, su salida se desactiva manteniéndose así hasta que la falla desaparezca y/o el motor se haya enfriado completamente.

### Tiempos de Disparo

Los tiempos de disparo varían según la relación de corriente (Icarga / FLA) para la Curva Fría y la Curva Caliente.

**FLA (Full Load Ampere)** = Corriente máxima soportada por la carga
**FLA** = Valor de corriente ajustada por el usuario en el GSC-CR

### Desactivación Permanente

Cuando el GSC-CR detecta 3 fallas consecutivas de corriente en un intervalo menor a 30 minutos, se desactivará permanentemente su salida y los indicadores rojos se encenderán de manera secuencial una vez haya culminado el tiempo de enfriamiento del equipo. Solo se podrá restaurar la operación del sistema oprimiendo el botón RESET. Se recomienda verificar la causa de las fallas sucesivas antes de oprimir el botón RESET.

## Garantía

Los productos Exceline y Genius son manufacturados bajo rigurosas normas de control de calidad y están garantizados contra cualquier defecto de fabricación. 

### Cobertura de Garantía

- Ampara todas las piezas y componentes del producto
- Se reemplazará cualquier pieza o componente defectuoso, sin costo adicional para el consumidor
- Duración: tres (3) años a partir de la fecha de adquisición
- Validez internacional en todos los países con importadores/distribuidores

### Condiciones de Invalidez

La garantía no será válida en los siguientes casos:

a) Cuando el producto haya sido utilizado en condiciones distintas a las normales

b) Cuando el producto no hubiese sido operado de acuerdo con el instructivo de uso que se le acompaña

c) Cuando el producto hubiese sido alterado o reparado por personas no autorizadas por el importador

### Requisitos para Hacer Efectiva la Garantía

Se requerirá del producto acompañado de la factura, recibo o comprobante emitido por el establecimiento que lo vendió, en el que consten los datos específicos del producto objeto de la compraventa. Deberá presentarse en el establecimiento donde adquirió el producto o en el domicilio del importador que se encuentre disponible en su región.

### Gastos de Transportación

La garantía cubre los gastos de transportación del producto que deriven de su cumplimiento, dentro de la red de servicio en todo el país.
```