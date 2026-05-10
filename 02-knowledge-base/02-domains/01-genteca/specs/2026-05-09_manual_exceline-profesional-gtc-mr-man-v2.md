```markdown
---
title: "Manual de Instalación - Relé Temporizador Multifunción y Multirango GTC-MR"
type: Technical
source: "GTC-MR_MAN_V2.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GTC-MR"
date_processed: "2026-05-09"
---

# Manual de Instalación - Relé Temporizador Multifunción y Multirango

## Descripción del Producto

El GTC-MR es un temporizador con múltiples rangos ajustables y cuatro modos de operación seleccionables:
- Ciclado simétrico (CICLO)
- Pulso o intervalo (PULSO)
- Temporizado a la conexión (TC)
- Temporizado a la desconexión (TD)

En todos los casos, excepto TD, la función se activa al energizar el temporizador. Para TD, se requiere una señal auxiliar para el control de la temporización. Este dispositivo es compatible con voltajes nominales de 120/220 V~.

## Partes y Piezas

| Componente | Descripción |
|-----------|------------|
| Contacto NA | Contacto normalmente abierto |
| Contacto Común | Terminal común |
| Contacto NC | Contacto normalmente cerrado |
| Perilla de Tiempo | Control de duración de temporización |
| Perilla de Rango | Selector de base de tiempo (segundos, minutos, horas) |
| Perilla de Modo | Selector de modo de operación |
| LED VERDE | Indicador de carga conectada |
| LED ROJO | Indicador de producto encendido |
| Entrada de control auxiliar (AUX) | Terminal A1-A2 para señal auxiliar |
| Gancho de sujeción para riel simétrico | Mecanismo de fijación a riel DIN |
| Orificios para montaje en superficie | Para instalación sobre superficie plana |
| Ranura para montaje de riel | Para instalación en riel DIN |

## Instalación

### Paso 1: Fijación Mecánica

**Montaje sobre Riel DIN:**
- Coloque el GTC-MR en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GTC-MR y retire el producto del riel.

**Montaje sobre Superficie Plana:**
- Coloque el GTC-MR sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".

**Dimensiones:**
- 51 mm de altura
- 88 mm de profundidad

### Paso 2: Instalación Eléctrica

1. **Desconecte el breaker** antes de iniciar el trabajo eléctrico para evitar accidentes.

2. **Conecte los cables de alimentación** en 120/220 V~.

3. **Conexión según el modo de operación requerido:**

#### Paso 3A: Conexión para los modos TC, CICLO y PULSO
- Conecte el voltaje a controlar o interrumpir al terminal 7 (Contacto Común) y la carga o la salida al contactor al terminal 8 (NA).

#### Paso 3B: Conexión para el modo Temporizado a la Desconexión (TD)
- Realice la misma conexión indicada en el paso anterior, añadiendo una conexión adicional.
- El cable de control auxiliar debe conectarse al terminal 2 (AUX).

4. **Realice el ajuste a la perilla MODO** de acuerdo a la forma de trabajo requerido.

5. **Ajuste la base de tiempo** en la que se desea trabajar, mediante la perilla RANGO. Se puede seleccionar en segundos, minutos u horas.

6. **Configure el tiempo** en el que se requiere la temporización, mediante el ajuste de la perilla TIEMPO. Observe que existen 2 escalas en esta perilla (naranja y blanca) relacionadas con el color de la base de tiempo de la perilla RANGO.

7. **Reconecte la energía eléctrica** y verifique el funcionamiento del GTC-MR y del equipo protegido.

## Diagrama de Conexión Estándar

```
Voltaje a controlar     120 ó 220 V~
o interrumpir       ↓
Terminal 7 (A1) ←──────┘
Terminal 8 (A2) → Carga o Bobina del contactor
```

## Modos de Operación

### Temporizado a la Conexión (TC)
Al aplicar la alimentación, el relé espera el tiempo programado (TR) en las perillas de tiempo y rango para luego activar la carga.

### Pulso o Intervalo (PULSO)
Al aplicar la alimentación, la carga se activa inmediatamente y permanece encendida durante el tiempo programado (TR) en las perillas de tiempo y rango. Luego de transcurrido se desactiva.

### Ciclado Simétrico (CICLO)
La carga se activa y desactiva de forma cíclica, con tiempos (TR) iguales de encendido y apagado, según lo programado en las perillas de tiempo y rango.

### Temporizado a la Desconexión (TD)
La carga se activa con la presencia de la señal de control. Al desaparecer la señal, comienza la temporización (TR), según lo programado en las perillas de tiempo y rango. Al finalizar la misma, la carga se desactiva. La señal de control auxiliar (AUX) es obligatoria solo para este modo.

## Indicadores Luminosos LED

### LED VERDE
| Estado | Significado |
|--------|------------|
| ON | Carga encendida |
| OFF | Carga apagada |

### LED ROJO
| Estado | Significado |
|--------|------------|
| ON | Producto encendido |
| OFF | Producto apagado |

## Descripción de Terminales

| Terminal | Descripción |
|----------|------------|
| 1, 6 | No utilizados |
| 2 | Entrada de control auxiliar (AUX) |
| 3 | Entrada de voltaje 1 (A1) |
| 4 | Entrada de voltaje 2 (A2) |
| 5 | Contacto normalmente cerrado (NC) |
| 7 | Contacto común (C) |
| 8 | Contacto normalmente abierto (NA) |

**Nota:** La señal de control auxiliar (AUX) es requerida solo para el modo TD.
```