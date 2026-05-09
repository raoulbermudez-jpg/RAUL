```markdown
---
title: "Protector de Sobrecarga Trifásico para GSC-CR - Manual de Instalación"
type: Technical
source: "GSC-CR_MAN-DES_V1.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GSC-CR"
date_processed: "2026-05-09"
---

# Protector de Sobrecarga Trifásico para GSC-CR
## Manual de Instalación
### Compresores de Refrigeración y Aire Acondicionado

## Descripción

El Protector de Sobrecarga Trifásico para Compresores de Refrigeración y Aire Acondicionado GSC-CR es un relé térmico electrónico con protección de voltaje, el cual monitorea constantemente las corrientes del compresor y los voltajes de alimentación. Mediante un algoritmo inteligente realiza la desconexión en función del calentamiento del compresor.

## Indicadores Luminosos

El GSC-CR presenta indicadores luminosos tipo LED's para señalizar fallas y el estado de operación del sistema. En caso de presentarse varias fallas, el equipo las señalizará en simultáneo.

| INDICADOR | LUZ CONTINUA | LUZ INTERMITENTE |
|-----------|--------------|------------------|
| VERDE | Conectado | Temporizando (TC) |
| ROJO 1 | Falla por sobrecarga (OL) | Falla por fase invertida (PR) |
| ROJO 2 | Falla por desbalance de voltaje o corriente (UB) | Pérdida de fase de voltaje o corriente (SP) |
| ROJO 3 | Falla por sobrevoltaje (OV) | Falla por bajo voltaje (UV) |

**Nota:** Cuando el GSC-CR detecta 3 fallas consecutivas de corriente en un intervalo menor a 30 minutos, se desactivará permanentemente su salida y los indicadores rojos se encenderán de manera secuencial una vez haya culminado el tiempo de enfriamiento del equipo. Solo se podrá restaurar la operación del sistema oprimiendo el botón RESET. Se recomienda verificar la causa de las fallas sucesivas antes de oprimir el botón RESET.

## Instalación

### Paso 1: Fijación Mecánica

Realice la fijación mecánica del dispositivo la cual puede ser en montaje sobre riel DIN o sobre superficie plana.

#### a) Montaje sobre Riel DIN

1. Coloque el GSC-CR en una posición inclinada
2. Encaje el producto en el riel por la ranura desde la parte superior
3. Hale hacia abajo con un destornillador plano la pestaña de retención ubicada en el dorso del producto y encájela en el riel para fijarlo
4. Para retirarlo del riel repita el procedimiento

#### b) Montaje sobre Superficie Plana

1. Saque los dos (2) sujetadores insertables localizados en la parte posterior del GSC-CR
2. Luego inserte ambos sujetadores dentro de las ranuras verticales de la parte posterior del GSC-CR
3. Coloque el GSC-CR sobre la superficie plana del panel donde desea realizar la instalación
4. Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32"
5. Utilice ramplugs en caso de que realice la instalación sobre una pared
6. Fije el equipo con un destornillador, usando tornillos de 3/16"

### Paso 2: Diagrama de Conexión

Realice la instalación eléctrica del producto de acuerdo al diagrama de conexión. Identifique la fase 1 (L1), fase 2 (L2) y fase 3 (L3) de la red.

## Partes y Piezas

- Perilla de ajuste de corriente (FLA)
- Perilla de ajuste de tiempo de conexión (TC)
- Botón de RESET
- Indicadores luminosos
- Sensores de Corriente
- Sujetador insertable
- Ranura para montaje de riel

## Terminales

| TERMINAL | DESCRIPCIÓN |
|----------|-------------|
| L1 | Fase L1 |
| L2 | Fase L2 |
| L3 | Fase L3 |
| 95-96 | Conectado/Disparado |
| 97-98 | Abierto/Disparado |

## Operación

El GSC-CR supervisa constantemente la corriente del motor y los voltajes de línea. Cuando alguna condición de sobrecarga o falla de fase ocurre, su salida se desactiva manteniéndose así hasta que la falla desaparezca y/o el motor se haya enfriado completamente.

Los tiempos de disparo varían según la relación de corriente (Icarga / FLA) para la Curva Fría y la Curva Caliente. La relación se grafica en función del tiempo de disparo (segundos) versus la relación de corriente, con rangos desde 0,0 a 10,0 en la escala de Icarga/FLA y tiempos de disparo desde 1 segundo a 10000 segundos.

**FLA (Full Load Ampere)** = Corriente máxima soportada por la carga, equivalente al valor de corriente ajustada por el usuario en el GSC-CR.

## Garantía

Los productos Exceline y Genius son manufacturados bajo rigurosas normas de control de calidad y están garantizados contra cualquier defecto de fabricación. Esta garantía ampara todas las piezas y componentes del producto.

**Período de Garantía:** Tres (3) años a partir de la fecha de adquisición.

**Garantía Internacional:** La presente garantía tiene validez en todos los países con importadores/distribuidores. Es válida en un país distinto al de origen de compra, siempre y cuando cumpla con las condiciones establecidas.

**Casos No Cubiertos por Garantía:**
- Cuando el producto haya sido utilizado en condiciones distintas a las normales
- Cuando el producto no hubiese sido operado de acuerdo con el instructivo de uso que se le acompaña
- Cuando el producto hubiese sido alterado o reparado por personas no autorizadas por el importador

**Requisitos para Hacer Efectiva la Garantía:** Se requerirá del producto acompañado de la factura, recibo o comprobante emitido por el establecimiento que lo vendió, en el que consten los datos específicos del producto objeto de la compraventa.

**Gastos de Transportación:** La garantía cubre los gastos de transportación del producto que deriven de su cumplimiento, dentro de la red de servicio en todo el país.
```