```markdown
---
title: "Manual de Instalación - Relé Alternador GRA-MV"
type: Technical
source: "GRA-MV_MAN_V1_IMP.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GRA-MV"
date_processed: "2026-05-09"
---

# Manual de Instalación - Relé Alternador GRA-MV

## Descripción General

El GRA-MV es un dispositivo electrónico de control que opera activando dos cargas eléctricas en forma alterna. Diseñado para ser usado en cualquier aplicación de automatismo y principalmente para alternar entre dos bombas de sistemas hidroneumáticos.

El producto cuenta con una perilla que permite seleccionar:
- **Modo AUTO**: Alterna la salida del relé de forma automática mediante el cambio eléctrico en la señal de control
- **Modo MANUAL**: Selección directa de EQUIPO 1 o EQUIPO 2

## Partes y Piezas

- Contacto NA (Normalmente Abierto)
- Contacto NC (Normalmente Cerrado)
- Contacto Común (C)
- Perilla de modo (EQUIPO 1 / AUTO / EQUIPO 2)
- LED VERDE indicador de equipo 1 conectado
- LED VERDE indicador de equipo 2 conectado
- Ranura para montaje de Riel DIN
- Gancho de sujeción para riel simétrico
- Orificios para montaje en superficie
- Terminal de señal de control (CONTROL)
- Terminales de alimentación (A1, A2)

## Instalación

### Paso 1: Fijación Mecánica del Dispositivo

El GRA-MV puede instalarse sobre Riel DIN o sobre superficie plana.

#### Montaje sobre Riel DIN

- Coloque el GRA-MV en posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click
- Para retirarlo del riel, utilice un destornillador plano para halar hacia abajo el gancho de retención ubicado en el dorso del GRA-MV

#### Montaje sobre Superficie Plana

- Coloque el GRA-MV sobre la superficie plana del panel donde desea realizar la instalación
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de máximo 4 mm ó 5/32"
- Utilice ramplugs en caso de que realice la instalación sobre una pared
- Fije el equipo con un destornillador, usando tornillos de 3/16"

### Paso 2: Instalación Eléctrica del Producto

**Paso 2.1**: Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

**Paso 2.2**: Conecte los cables de alimentación en 120 / 220 V~ a los terminales A1 y A2.

**Paso 2.3**: Conecte el voltaje a controlar o interrumpir al terminal 7 (Contacto Común C), el EQUIPO 1 al terminal 8 (NA) y el EQUIPO 2 al terminal 6 (NC).

**Paso 2.4**: Conecte la señal de control al terminal 2 (CONTROL).

**Paso 2.5**: Ajuste el modo de operación:
- **EQUIPO 1 o EQUIPO 2 (modo MANUAL)**: Permite activar directamente uno de los dos equipos
- **AUTO**: El relé alternador cambia automáticamente entre ambos equipos según las condiciones de operación, activada por la señal de CONTROL

**Paso 2.6**: Reconecte la energía eléctrica y verifique el funcionamiento del GRA-MV y del equipo controlado.

## Diagrama de Conexión Estándar

```
120/220 V~  ──┬──────────────────────────────────┐
              │                                  │
             A1                                 A2
              │                                  │
         Bobina del            Bobina del    Bobina del
         Contactor             Contactor     Contactor
         EQUIPO 1              Equipo 1      Equipo 2
              │                  │              │
              │                  ├──────┬───────┤
              │                  │      │       │
              ├────────────┬─────┴──────┤       │
              │            │            │       │
         Terminal 7    Terminal 8   Terminal 6  │
         (Común C)      (NA)          (NC)      │
              │            │            │       │
           ┌──┴────────┬───┴────────┬───┴───┬──┘
           │           │            │       │
      Señal de     Salida Relé   Salida    │
      Control      NA (T7-8)     Relé NC   │
    (Terminal 2)  Equipo 2      (T7-6)    │
           │                     Equipo 1  │
       LED EQUIPO 1                        │
       LED EQUIPO 2                        │
```

## Modo de Operación Automático

### Descripción del Ciclo

| Intervalo | Descripción | Estado |
|-----------|-------------|--------|
| T0 – T1 | Señal de control desactivada. Salida del relé activa es NC (terminales 7-6 conectados). Ambos equipos apagados. | - |
| T1 – T2 | Señal de control activa. Salida del relé activa es NC (terminales 7-6 conectados). EQUIPO 1 encendido. | ✓ |
| T2 | Flanco de bajada: se alterna la salida del relé. Ahora la salida activa es NA (terminales 7-8 conectados). | Cambio |
| T2 – T3 | Señal de control desactivada. Salida del relé activa es NA (terminales 7-8 conectados). Ambos equipos apagados. | - |
| T3 – T4 | Señal de control activa. Salida del relé activa es NA (terminales 7-8 conectados). EQUIPO 2 encendido. | ✓ |
| T4 | Flanco de bajada: se alterna la salida del relé. Ahora la salida activa es NC (terminales 7-6 conectados). | Cambio |
| T4 – T5 | Se inicia el ciclo nuevamente. | Reinicio |

## Indicadores Luminosos LED

| Indicador | Estado | Descripción |
|-----------|--------|-------------|
| LED VERDE EQUIPO 1 | ON | Equipo 1 encendido |
| LED VERDE EQUIPO 1 | OFF | Equipo 1 apagado |
| LED VERDE EQUIPO 2 | ON | Equipo 2 encendido |
| LED VERDE EQUIPO 2 | OFF | Equipo 2 apagado |

## Descripción de Terminales

| Terminal | Descripción |
|----------|-------------|
| 1, 5 | No utilizado |
| 2 | Entrada de control (CONTROL) |
| 3 | Entrada de voltaje 1 (A1) |
| 4 | Entrada de voltaje 2 (A2) |
| 6 | Contacto normalmente cerrado (NC) |
| 7 | Contacto común (C) |
| 8 | Contacto normalmente abierto (NA) |
```