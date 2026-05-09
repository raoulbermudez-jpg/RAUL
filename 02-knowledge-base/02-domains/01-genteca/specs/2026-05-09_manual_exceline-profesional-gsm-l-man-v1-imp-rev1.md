```markdown
---
title: "GSM-L Manual de Instalación - Supervisor Monofásico con Manejo de Carga"
type: Technical
source: "GSM-L_MAN_V1_IMP_REV1.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GSM-L"
date_processed: "2026-05-09"
---

# Manual de Instalación - GSM-L Supervisor Monofásico con Manejo de Carga

## Descripción General

El GSM-L de Exceline Profesional es un supervisor de voltaje diseñado para proteger cargas de hasta 1,5 HP en motores eléctricos monofásicos frente a fallas de voltaje. Este dispositivo puede utilizarse también en conjunto con un contactor para proteger cargas de mayor capacidad. Ofrece protección confiable contra problemas como alto y bajo voltaje, variaciones extremas, inestabilidad y parpadeos de energía, asegurando un funcionamiento seguro y eficiente de los equipos.

## Partes y Piezas

- Contacto NA (Normalmente Abierto)
- Contacto Común
- Contacto NC (Normalmente Cerrado)
- Perilla de Voltaje Bajo
- Perilla de Voltaje Alto
- Perilla de Tiempo de Conexión
- LED VERDE: Indicador del estado del relé
- LED ROJO: Indicador de falla de voltaje alto
- LED ROJO: Indicador de falla de voltaje bajo
- Gancho de sujeción para riel simétrico
- Ranura para montaje de Riel DIN
- Orificios para montaje en superficie

## Instalación

### Paso 1: Fijación Mecánica del Dispositivo

La fijación mecánica puede realizarse en montaje sobre Riel DIN o sobre superficie plana.

#### Montaje sobre Riel DIN

- Coloque el GSM-L en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click.
- Para retirarlo del riel, con un destornillador plano hale hacia abajo el gancho de retención que está ubicado en el dorso del GSM-L y retire el producto del riel.

#### Montaje sobre Superficie Plana

- Coloque el GSM-L sobre la superficie plana del panel donde desea realizar la instalación.
- Marque con un lápiz los orificios y con un taladro abra dos agujeros de 5/32". Utilice ramplugs en caso de que realice la instalación sobre una pared.
- Fije el equipo con un destornillador, usando tornillos de 3/16".
- Dimensiones: 51 mm x 88 mm

### Paso 2: Instalación Eléctrica del Producto

1. **Desconecte el breaker** antes de iniciar el trabajo eléctrico para evitar accidentes.

2. **Conecte los cables de alimentación:**

   **Conexión en 120 V~**
   - Identifique la fase (F) y el neutro (N) de la red eléctrica a supervisar y conéctelos a los terminales 3 y 4.

   **Conexión en 220 V~**
   - Identifique fase 1 (A1) y fase 2 (A2) de la red eléctrica a supervisar y conéctelos a los terminales 3 y 4.

3. **Conecte el voltaje a controlar o interrumpir** al terminal 7 (Contacto Común) y la carga o la salida al contactor al terminal 6 (NA).

4. **Ajuste las perillas** de voltaje bajo, voltaje alto y tiempo de conexión de acuerdo a los requerimientos de la aplicación.

5. **Reconecte la energía eléctrica** y verifique el funcionamiento del GSM-L y del equipo protegido.

## Indicadores Luminosos LED

### Indicador LED Verde
- **VOLTAJE NORMAL CONECTADO:** Fijo
- **TIEMPO DE ESPERA:** Intermitente

### Indicador LED Rojo - Falla de Voltaje Alto
- **VOLTAJE ALTO:** Fijo
- **INESTABILIDAD:** Intermitente

### Indicador LED Rojo - Falla de Voltaje Bajo
- **VOLTAJE BAJO:** Fijo
- **INESTABILIDAD:** Intermitente

## Diagrama de Conexión Estándar

```
Voltaje a controlar     Carga o Bobina
o interrumpir           del contactor
A1/F ─────────────────────────┐
     │                         │
  [GSM-L]                      │
     │                         │
A2/N ─────────────────────────┘
     │
120 ó 220 V~
     │
Terminal NA (6) ──────────────→ Carga o salida al contactor
Terminal C (7)
Terminal NC (5)
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
```