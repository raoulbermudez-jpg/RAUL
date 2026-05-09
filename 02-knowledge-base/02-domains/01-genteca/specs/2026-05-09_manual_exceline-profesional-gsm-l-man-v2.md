---
title: "GSM-L Manual de Instalación - Supervisor Monofásico con Manejo de Carga"
type: Technical
source: "GSM-L_MAN_V2.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GSM-L"
date_processed: "2026-05-09"
---

# Manual de Instalación - Supervisor Monofásico con Manejo de Carga

## Descripción General

El GSM-L es un supervisor de voltaje diseñado para proteger cargas de hasta 1,5 HP en motores eléctricos monofásicos frente a fallas de voltaje. Este dispositivo puede utilizarse también en conjunto con un contactor para proteger cargas de mayor capacidad. Ofrece protección confiable contra problemas como alto y bajo voltaje, variaciones extremas, inestabilidad y parpadeos de energía, asegurando un funcionamiento seguro y eficiente de los equipos.

## Partes y Piezas

- **Orificio para montaje en superficie**: Permite la fijación directa a paneles
- **Contacto Común (C)**: Terminal 7
- **Contacto NA (Normalmente Abierto)**: Terminal 6
- **Contacto NC (Normalmente Cerrado)**: Terminal 5
- **Perilla de Voltaje Bajo**: Ajuste de protección de bajo voltaje
- **Perilla de Voltaje Alto**: Ajuste de protección de alto voltaje
- **Perilla de Tiempo de Conexión**: Ajuste del tiempo de reacción del relé
- **Ranura para montaje en Riel DIN**: Permite instalación en carril estándar
- **LED VERDE**: Indicador del estado del relé
- **LED ROJO**: Indicador de falla de voltaje alto
- **LED ROJO**: Indicador de falla de voltaje bajo
- **Gancho de sujeción para riel simétrico**: Facilita el montaje y desmontaje
- **Orificio para montaje en superficie**: Alternativa de instalación plana

## Instalación

### Paso 1: Fijación Mecánica del Dispositivo

#### Montaje sobre Riel DIN

- Coloque el GSM-L en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GSM-L y retire el producto del riel.

#### Montaje sobre Superficie Plana

- Coloque el GSM-L sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".

**Dimensiones de montaje:**
- Altura entre orificios: 51 mm
- Ancho de los orificios: 8 mm

### Paso 2: Instalación Eléctrica del Producto

#### Precaución
Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

#### Conexión en 120 V~

- Identifique la fase (F) y el neutro (N) de la red eléctrica a supervisar.
- Conéctelos a los terminales 3 y 4.

#### Conexión en 220 V~

- Identifique fase 1 (A1) y fase 2 (A2) de la red eléctrica a supervisar.
- Conéctelos a los terminales 3 y 4.

#### Conexión de Carga

- Conecte el voltaje a controlar o interrumpir al terminal 7 (Contacto Común).
- Conecte la carga o la salida al contactor al terminal 6 (NA - Normalmente Abierto).

#### Finalización

- Ajuste las perillas de voltaje bajo, voltaje alto y tiempo de conexión de acuerdo a los requerimientos de la aplicación.
- Reconecte la energía eléctrica y verifique el funcionamiento del GSM-L y del equipo protegido.

## Indicadores Luminosos LED

### Indicador LED Verde

| Estado | Condición |
|--------|-----------|
| Fijo | Voltaje normal conectado |
| Intermitente | Tiempo de espera |

### Indicador LED Rojo - Falla de Voltaje Alto

| Estado | Condición |
|--------|-----------|
| Fijo | Voltaje alto |
| Intermitente | Inestabilidad |

### Indicador LED Rojo - Falla de Voltaje Bajo

| Estado | Condición |
|--------|-----------|
| Fijo | Voltaje bajo |
| Intermitente | Inestabilidad |

## Diagrama de Conexión Estándar

```
        Voltaje a controlar
        o interrumpir
           (120 ó 220 V~)
              │
              │
          A1/F (3)
          A2/N (4)
              │
           [GSM-L]
              │
              ├─ C (7) ─────┐
              │             │
              └─ NA (6) ────┤
                            │
                      Carga o Bobina
                      del contactor
```

## Tabla de Terminales

| Terminal | Descripción |
|----------|-------------|
| 1, 2, 8 | No utilizado |
| 3 | Entrada de voltaje 1 (A1/F) |
| 4 | Entrada de voltaje 2 (A2/N) |
| 5 | Contacto normalmente cerrado (NC) |
| 6 | Contacto normalmente abierto (NA) |
| 7 | Contacto común (C) |