```markdown
---
title: "Protector de Sobrecarga GSC-MB - Manual de Instalación"
type: Technical
source: "GSC-MB_MAN-DES_V1.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GSC-MB"
date_processed: "2026-05-09"
---

# Protector de Sobrecarga GSC-MB Trifásico para Motores y Bombas

## Descripción

El Protector de Sobrecarga Trifásico para Motores y Bombas GSC-MB es un relé (relevador) térmico electrónico con protección de voltaje, el cual monitorea constantemente las corrientes del motor, los voltajes de alimentación y mediante un algoritmo inteligente realiza la desconexión en función del calentamiento del motor.

## Partes y Piezas

- Perilla de ajuste de corriente (FLA)
- Perilla de ajuste de tiempo de conexión (TC)
- Botón RESET
- Indicadores luminosos LED
- Sensores de Corriente
- Ranura para montaje de riel
- Sujetadores insertables

## Terminales

| Terminal | Descripción |
|----------|-------------|
| L1 | Fase L1 |
| L2 | Fase L2 |
| L3 | Fase L3 |
| 95-96 | Disparado |
| 97-98 | Disparado |

## Instalación

### Paso 1: Fijación Mecánica

Realice la fijación mecánica del dispositivo la cual puede ser en montaje sobre riel DIN o sobre superficie plana.

#### a) Montaje sobre Riel DIN

1. Coloque el GSC-MB en una posición inclinada
2. Encaje el producto en el riel por la ranura desde la parte superior
3. Hale hacia abajo con un destornillador plano la pestaña de retención ubicada en el dorso del producto
4. Encájela en el riel para fijarlo
5. Para retirarlo del riel, repita el procedimiento

#### b) Montaje sobre Superficie Plana

1. Saque los dos (2) sujetadores insertables localizados en la parte posterior del GSC-MB
2. Luego inserte ambos sujetadores dentro de las ranuras verticales de la parte posterior del GSC-MB
3. Coloque el GSC-MB sobre la superficie plana del panel donde desea realizar la instalación
4. Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32"
5. Utilice ramplugs en caso de que realice la instalación sobre una pared
6. Fije el equipo con un destornillador, usando tornillos de 3/16"

### Paso 2: Instalación Eléctrica

Realice la Instalación eléctrica del producto de acuerdo al diagrama de conexión.

Identifique la fase 1 (L1), fase 2 (L2) y fase 3 (L3) de la red eléctrica a supervisar.

Conecte al terminal 97 la fase con la que desea controlar el contactor.

## Descripción de Fallas y sus Indicadores Luminosos

El GSC-MB presenta indicadores luminosos tipo LED's para señalizar fallas y el estado de operación del sistema. En caso de presentarse varias fallas, el equipo las señalizará en simultáneo.

### Indicadores Luminosos

| Indicador | Estado | Luz Continua | Luz Intermitente |
|-----------|--------|--------------|------------------|
| VERDE | Conectado | Conectado | Temporizando (TC) |
| ROJO 1 | Falla | Sobrecarga (OL) | Fase invertida (PR) |
| ROJO 2 | Falla | Desbalance de voltaje o corriente (UB) | Pérdida de fase de voltaje o corriente (SP) |
| ROJO 3 | Falla | Sobrevoltaje (OV) | Bajo voltaje (UV) |

**Nota:** Cuando el GSC-MB detecta 3 fallas consecutivas de corriente en un intervalo menor a 30 minutos, se desactivará permanentemente su salida y los indicadores rojos se encenderán de manera secuencial una vez haya culminado el tiempo de enfriamiento del equipo. Solo se podrá restaurar la operación del sistema oprimiendo el botón RESET. Se recomienda verificar la causa de las fallas sucesivas antes de oprimir el botón RESET.

## Operación del GSC-MB

El GSC-MB supervisa constantemente la corriente del motor y los voltajes de línea. Cuando alguna condición de sobrecarga o falla de fase ocurre, su salida se desactiva manteniéndose así hasta que la falla desaparezca y/o el motor se haya enfriado completamente.

### Curvas de Disparo

En la gráfica se observan los tiempos de disparo según la relación de corriente (Icarga / FLA) para la Curva Fría y la Curva Caliente.

**FLA (Full Load Ampere)** = Corriente máxima soportada por la carga = Valor de corriente ajustada por el usuario en el GSC-MB

Tiempo de disparo en segundos vs. relación Icarga/FLA (rango de 0 a 10)

## Garantía

Los productos Exceline y Genius son manufacturados bajo rigurosas normas de control de calidad y están garantizados contra cualquier defecto de fabricación.

### Cobertura de Garantía

- Ampara todas las piezas y componentes del producto
- Se reemplazará cualquier pieza o componente defectuoso sin costo adicional para el consumidor
- Período: tres (3) años a partir de la fecha de adquisición
- Válida internacionalmente en todos los países con importadores/distribuidores

### Casos No Cubiertos por Garantía

a) Cuando el producto haya sido utilizado en condiciones distintas a las normales

b) Cuando el producto no hubiese sido operado de acuerdo con el instructivo de uso que se le acompaña

c) Cuando el producto hubiese sido alterado o reparado por personas no autorizadas por el importador

### Procedimiento para Hacer Efectiva la Garantía

Se requerirá del producto acompañado de la factura, recibo o comprobante emitido por el establecimiento que lo vendió, en el que consten los datos específicos del producto objeto de la compraventa. Deberá presentarse en el establecimiento donde adquirió el producto o en el domicilio del importador que se encuentre disponible en su región.

### Gastos de Transportación

La garantía cubre los gastos de transportación del producto que deriven de su cumplimiento, dentro de la red de servicio en todo el país (aplica solo dentro de México).
```