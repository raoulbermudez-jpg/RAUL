# Nota de Aplicación — Sistema Hidroneumático con Alternancia de Dos Bombas Trifásicas por Dos Presostatos

**Línea:** Exceline Profesional  
**Código:** 10-GD-NA  
**Tipo de documento:** Nota de Aplicación  
**Fabricante:** Gente, Generación de Tecnología, C.A. — www.genteca.com.ve  
**Referencia PDF:** 10-GD-NA-Hidroneumatico-2-bombas.pdf (Notas_Aplicacion/10-GD-NA-Hidroneumatico-2-bombas.pdf en RAG_SOURCES)

---

## Descripción de la Aplicación

**Aplicación:** Sistema hidroneumático con alternancia de dos bombas trifásicas mediante GRA-MV y relé octal GRC-8, controlado por dos presostatos  
**Voltaje de la instalación:** 220 V~  
**Grado de dificultad:** Medio

> **Nota de superposición:** Existe también la nota del piloto `2026-04-17_nota-aplicacion_exceline-profesional-hidroneumatico-2-bombas-GRA-GRC.md` que cubre el mismo sistema con bombas monofásicas. Esta nota cubre el caso con **bombas trifásicas** usando **dos presostatos** para activación simultánea.

---

## Lista de Equipos

| Equipo | Modelo | Características |
|--------|--------|-----------------|
| Relé Alternador | GRA-MV | Multivoltaje 120/220 V~ — alterna salida según señal de control — compacto y fácil de instalar |
| Relé Octal | GRC-8 | Relé electromecánico de propósito general — base de conexión octal para fácil montaje/desmontaje — botón de prueba manual — indicador mecánico de cierre |

---

## Descripción del Sistema Hidroneumático

Los sistemas hidroneumáticos impulsan agua a presión desde un tanque de almacenamiento hasta los puntos de una edificación donde se requiere el servicio. Las bombas succionan el agua del tanque y la impulsan hacia el tanque presurizado según la señal de los presostatos.

La mayoría de los sistemas poseen dos o más bombas que operan en forma alternada para dosificar su utilización y prolongar su vida útil — de ahí la necesidad del GRA-MV. El relé octal GRC-8 permite la activación simultánea de ambas bombas cuando la presión de una sola bomba no es suficiente.

---

## Modos de Funcionamiento (mediante selector manual)

| Posición del Selector | Descripción |
|-----------------------|-------------|
| **Posición 1** | Bomba 1 encendida permanentemente según Presostato 1 / Bomba 2 en mantenimiento (nunca se activa) |
| **Posición 2** | Funcionamiento automático — ambas bombas alternan según señal del Presostato 1 mediante el GRA-MV |
| **Posición 3** | Bomba 2 encendida permanentemente según Presostato 1 / Bomba 1 en mantenimiento (nunca se activa) |

---

## Activación Simultánea (Posición 2, modo Auto)

En modo automático con Posición 2:
- Las bombas alternan controladas por el **Presostato 1**
- Si una sola bomba no es suficiente para satisfacer la demanda y la presión sigue cayendo, se cierra el **Presostato 2**
- El Presostato 2 activa el **Relé Octal GRC-8**, que activa ambas bombas simultáneamente hasta alcanzar el nivel de presión requerido

---

## Diagrama de Conexión

```
220 V~ / 60 Hz
      ↓
  INTERRUPTOR
      ↓
  ┌───────────────────────────────────────────┐
  │         PRESOSTATO 1                      │
  │         ↓                                 │
  │    GRA-MV (Relé Alternador)               │
  │    Terminales 3-6 / 1-8 / 4-5 / 2-7      │
  │    ┌────────────────┐                     │
  │    ↓                ↓                     │
  │ CONTACTOR        CONTACTOR                │
  │  BOMBA 1          BOMBA 2                 │
  │    ↓                ↓                     │
  │  BOMBA             BOMBA                  │
  │  TRIFÁSICA 1      TRIFÁSICA 2             │
  │                                           │
  │  PRESOSTATO 2 → GRC-8-220VAC             │
  │  (activa ambas bombas simultáneamente)    │
  └───────────────────────────────────────────┘
```

**Conexión del GRC-8:**

| Terminal GRC-8 | Conexión |
|----------------|----------|
| 3 | — |
| 6 | — |
| 1 | Relé Alternador |
| 8 | Presostato 2 |
| 4 | — |
| 5 | — |
| 2 | — |
| 7 | — |

---

## Nota de Configuración de Presostatos

> Es importante configurar los límites de presión de ambos presostatos de forma correcta para garantizar el funcionamiento adecuado:
> - El **Presostato 2** solo debe activarse si la presión cae por debajo del límite inferior del Presostato 1
> - El Presostato 2 debe desactivarse **antes** que el Presostato 1 cuando la presión se eleve

---

## Diagramas

> El esquema de conexión completo con terminales numerados del GRC-8, contactores, selector y bombas es un gráfico en el PDF original. Fuente: `G:\Mi unidad\WorkspaceIA\RAG_SOURCES\Notas_Aplicacion\10-GD-NA-Hidroneumatico-2-bombas.pdf`
