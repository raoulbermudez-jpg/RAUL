```markdown
---
title: "GRA-MV - Relé Alternador para Sistemas Hidroneumáticos de Dos Bombas"
type: Technical
source: "GRA-MV_MAN_V1.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GRA-MV"
date_processed: "2026-05-09"
---

# Manual de Instalación - GRA-MV
## Relé Alternador Sistemas Hidroneumáticos de Dos Bombas

## Descripción del Producto

El GRA-MV es un dispositivo electrónico de control que opera activando dos cargas eléctricas en forma alterna. Diseñado para ser usado en cualquier aplicación de automatismo y principalmente para alternar entre dos bombas de sistemas hidroneumáticos. 

El producto tiene una perilla que permite seleccionar:
- **Modo AUTO**: alterna la salida del relé de forma automática mediante el cambio eléctrico en la señal de control
- **Modo MANUAL**: selección directa de EQUIPO 1 o EQUIPO 2

## Partes y Piezas

- **Contacto NA**: Contacto normalmente abierto
- **Contacto Común**: Contacto común del relé
- **Contacto NC**: Contacto normalmente cerrado
- **Perilla de modo**: Selecciona AUTO, EQUIPO 1 o EQUIPO 2
- **LED VERDE Equipo 1**: Indicador de equipo 1 conectado
- **LED VERDE Equipo 2**: Indicador de equipo 2 conectado
- **Ranura para montaje de Riel**: Para instalación en riel DIN
- **Gancho de sujeción para riel simétrico**
- **Orificio para montaje en superficie**: Fijación mecánica alternativa
- **Terminal CONTROL (A1 A2)**: Señal de control

## Instalación

### Paso 1: Fijación Mecánica

#### Montaje sobre Riel DIN

- Coloque el GRA-MV en una posición inclinada y fíjelo en el riel, haciendo presión hasta que haga Click
- Para retirarlo del riel, use un destornillador plano y hale hacia abajo el gancho de retención ubicado en el dorso del GRA-MV

#### Montaje sobre Superficie Plana

- Coloque el GRA-MV sobre la superficie plana del panel donde desea realizar la instalación
- Marque con un lápiz los orificios y abra dos agujeros con taladro de máximo 4 mm (5/32")
- Utilice ramplugs si realiza la instalación sobre una pared
- Fije el equipo con destornillador, usando tornillos de 3/16"

### Paso 2: Instalación Eléctrica

1. **Desconecte el breaker** antes de iniciar el trabajo eléctrico para evitar accidentes

2. **Conecte los cables de alimentación** en conexión 120 / 220 V~

3. **Conecte el voltaje** a controlar o interrumpir al terminal 7 (Contacto Común)

4. **Conecte la señal de control** al terminal 2 (CONTROL)

5. **Conexiones de salida**:
   - EQUIPO 1: conectar salida al contactor 1 al terminal 8 (NA)
   - EQUIPO 2: conectar salida al contactor 2 al terminal 6 (NC)

6. **Reconecte la energía eléctrica** y verifique el funcionamiento del GRA-MV y del equipo controlado

## Modos de Operación

### EQUIPO 1 o EQUIPO 2 (Modo MANUAL)
Permite activar directamente uno de los dos equipos mediante la selección en la perilla.

### AUTO (Modo Automático)
El relé alternador cambia automáticamente entre ambos equipos según las condiciones de operación, activada por la señal de CONTROL.

## Diagrama de Conexión Estándar

```
Señal control → Terminal 2
Bobina del Contactor Equipo 1 ← Terminal 8 (NA)
Bobina del Contactor Equipo 2 ← Terminal 6 (NC)
Voltaje de alimentación → Terminal 7 (Común)
LED EQUIPO 1 ← Indicador estado
LED EQUIPO 2 ← Indicador estado
```

## Funcionamiento Automático - Diagrama de Tiempos

### T0 – T1
- La señal de control se encuentra desactivada
- La salida del relé activa es NC (terminales 7-6 conectados)
- Los dos equipos se encuentran apagados

### T1 – T2
- La señal de control se encuentra activa
- La salida del relé activa es NC (terminales 7-6 conectados)
- Permanece encendido EQUIPO 1

### T2
- En el flanco de bajada se alterna la salida del relé
- Ahora la salida del relé activa es NA (terminales 7-8 conectados)

### T2 – T3
- La señal de control se encuentra desactivada
- La salida del relé activa es NA (terminales 7-8 conectados)
- Los dos equipos se encuentran apagados

### T3 – T4
- La señal de control se encuentra activa
- La salida del relé activa es NA (terminales 7-8 conectados)
- Permanece encendido EQUIPO 2

### T4
- En el flanco de bajada se alterna la salida del relé
- Ahora la salida del relé activa es NC (terminales 7-6 conectados)

### T4 – T5
- Se inicia el ciclo nuevamente como en el intervalo T0-T1

## Indicadores Luminosos LED

### EQUIPO 1 - Indicador LED Verde
- **ON**: Equipo 1 encendida
- **OFF**: Equipo 1 apagada

### EQUIPO 2 - Indicador LED Verde
- **ON**: Equipo 2 encendido
- **OFF**: Equipo 2 apagado

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