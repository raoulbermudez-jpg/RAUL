```markdown
---
title: "Protección de Motores con Corriente Nominal Superior a 80 A - GUCT con Toroides Externos"
type: Technical
source: "Notas de CT Toroides Externos GUCT.pdf"
product_line: "Genius"
document_type: "nota-aplicacion"
product_code: "GUCT"
date_processed: "2026-05-09"
---

# Protección de Motores con Corriente Nominal Superior a 80 A

## Descripción General

El GUCT proporciona protección contra cortocircuito desde tablero de control y arranque para motores con corriente nominal superior a 80 A, mediante la utilización de toroides externos.

## Modelos Aplicables

- GUCT 208 00
- GUCT 480 00

**Especificación de cableado:** Cable AWG 14

## Utilización del GUCT con Toroides Externos

### Tabla de Selección de Toroides

| Rango de Corriente Nominal (A) | Toroide Relación /5 |
|---|---|
| 13 - 17 | 50 |
| 15 - 20 | 60 |
| 19 - 25 | 75 |
| 25 - 33 | 100 |
| 31 - 42 | 125 |
| 38 - 50 | 150 |
| 50 - 67 | 200 |
| 63 - 83 | 250 |
| 75 - 100 | 300 |
| 100 - 133 | 400 |
| 125 - 167 | 500 |
| 150 - 200 | 600 |
| 188 - 250 | 750 |
| 200 - 267 | 800 |
| 250 - 333 | 1000 |
| 300 - 400 | 1200 |
| 375 - 500 | 1500 |
| 500 - 667 | 2000 |

## Notas Técnicas

1. Los modelos identificados como GUCT+20800S y GUCT+48000S se utilizan exclusivamente con CT externos. Estos modelos protegen motores con corriente nominal hasta 660 A.

2. El usuario debe especificar la corriente nominal del motor. Con este dato seleccionará un rango de corriente según tabla adyacente, con la cual determinará la relación /5 que requerirá para los CT externos a instalar.

3. El usuario debe programar el GUCT con CT externos añadiendo las instrucciones de ajustes contenidas en esta nota de aplicación. Todas las demás funciones y protecciones seguirán ajustándose de acuerdo a las Instrucciones de Instalación y Manual de usuario disponibles anteriormente.

4. La calibración del GUCT se mantiene garantizada, siempre que los CT externos sean comerciales, de clase 1, secundario 5A.

## Ejemplo de Aplicación

Si un motor consume una corriente nominal de 350 amperios, los toroides externos a seleccionar serán de valor igual a 1200.

## Diagrama de Conexión

```
       L1    L2    L3
       |     |     |
    X1 H1  X1 H1  X1 H1
       |     |     |
       └─────┴─────┘
            |
          GUCT
    (desde tablero de control
     y arranque)
       |     |     |     |     |
      95    96    97    98    [COM]
```

Protección contra cortocircuito (M 3~)
```