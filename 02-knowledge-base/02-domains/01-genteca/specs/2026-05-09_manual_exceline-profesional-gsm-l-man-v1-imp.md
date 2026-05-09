```markdown
---
title: "GSM-L Manual de Instalación - Supervisor Monofásico con Manejo de Carga"
type: Technical
source: "GSM-L_MAN_V1_IMP.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GSM-L"
date_processed: "2026-05-09"
---

# Manual de Instalación - GSM-L

## Descripción del Producto

El GSM-L de Exceline Profesional es un supervisor de voltaje diseñado para proteger cargas de hasta 1,5 HP en motores eléctricos monofásicos frente a fallas de voltaje. Este dispositivo puede utilizarse también en conjunto con un contactor para proteger cargas de mayor capacidad. Ofrece protección confiable contra problemas como alto y bajo voltaje, variaciones extremas, inestabilidad y parpadeos de energía, asegurando un funcionamiento seguro y eficiente de los equipos.

## Partes y Piezas

- **Contacto NA**: Contacto normalmente abierto
- **Contacto Común**: Terminal común del relé
- **Contacto NC**: Contacto normalmente cerrado
- **Perilla de Voltaje Bajo**: Ajuste de límite inferior de voltaje
- **Perilla de Voltaje Alto**: Ajuste de límite superior de voltaje
- **Perilla de Tiempo de Conexión**: Control del tiempo de espera del relé
- **LED VERDE**: Indicador del estado del relé
  - Voltaje normal: Fijo
  - Tiempo de espera: Intermitente
- **LED ROJO (Voltaje Alto)**: Indicador de falla de voltaje alto
  - Voltaje alto: Fijo
  - Inestabilidad: Intermitente
- **LED ROJO (Voltaje Bajo)**: Indicador de falla de voltaje bajo
  - Voltaje bajo: Fijo
  - Inestabilidad: Intermitente
- **Gancho de sujeción para riel simétrico**: Fijación en riel DIN
- **Orificio para montaje en superficie**: Fijación sobre panel plano
- **Ranura para montaje de Riel**: Ubicación del riel DIN

## Instalación

### Paso 1: Fijación Mecánica del Dispositivo

La fijación puede realizarse en montaje sobre riel DIN o sobre superficie plana.

#### Montaje sobre Riel DIN

- Coloque el GSM-L en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- **Para retirarlo del riel**: Con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GSM-L y retire el producto del riel.

#### Montaje sobre Superficie Plana

- Coloque el GSM-L sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32".
- Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".

**Dimensiones**: 51 mm × 88 mm

### Paso 2: Instalación Eléctrica del Producto

#### Procedimiento General

1. **Desconecte el breaker** antes de iniciar el trabajo eléctrico para evitar accidentes.

2. **Conecte los cables de alimentación**:
   
   **Conexión en 120 V~:**
   - Identifique la fase (F) y el neutro (N) de la red eléctrica a supervisar
   - Conéctelos a los terminales 3 y 4

   **Conexión en 220 V~:**
   - Identifique fase 1 (A1) y fase 2 (A2) de la red eléctrica a supervisar
   - Conéctelos a los terminales 3 y 4

3. **Conexión de carga**:
   - Conecte el voltaje a controlar o interrumpir al terminal 7 (Contacto Común)
   - Conecte la carga o la salida al contactor al terminal 6 (NA)

4. **Ajuste de parámetros**:
   - Ajuste las perillas de voltaje bajo, voltaje alto y tiempo de conexión de acuerdo a los requerimientos de la aplicación

5. **Verificación**:
   - Reconecte la energía eléctrica y verifique el funcionamiento del GSM-L y del equipo protegido

## Diagrama de Conexión Estándar

```
A1/F ─────────────┐
                  │
            [GSM-L]
                  │
A2/N ─────────────┘
(120 ó 220 V~)

Terminal 6 (NA) ──── Carga o Bobina del contactor
Terminal 7 (C)  ──── Voltaje a controlar o interrumpir
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

## Indicadores Luminosos LED

### LED VERDE - Estado Normal
- **Fijo**: Voltaje normal - Relé conectado
- **Intermitente**: Tiempo de espera

### LED ROJO - Falla de Voltaje Alto
- **Fijo**: Voltaje alto detectado
- **Intermitente**: Inestabilidad en voltaje alto

### LED ROJO - Falla de Voltaje Bajo
- **Fijo**: Voltaje bajo detectado
- **Intermitente**: Inestabilidad en voltaje bajo
```