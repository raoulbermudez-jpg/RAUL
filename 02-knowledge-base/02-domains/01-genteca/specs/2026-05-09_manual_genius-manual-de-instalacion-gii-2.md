```markdown
---
title: "Manual de Instalación GII+"
type: Technical
source: "Manual de Instalacion GII+ (2).pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GII+"
date_processed: "2026-05-09"
---

# GII+ Manual de Instalación

## Descripción General

GII+ es un Relé (Relevador) digital para Protección contra Fallas de Fase diseñado para proteger la carga conectada a la red de distribución contra daños ocasionados por fallas comunes de voltaje. Provee una pantalla LCD para indicar el estado de la salida.

### Alertas de Seguridad

**ALERTA:** Solo personal técnico calificado con conocimientos en Relés (Relevadores) de protección y la carga asociada debería realizar la instalación, arranque y mantenimiento del sistema. Hacer caso omiso podría resultar en lesiones a personas y/o daños a los equipos conectados.

**ALERTA:** Este producto puede activar al Contactor y hacer que arranque el sistema o carga conectada en forma automática. El usuario debe tomar precauciones para evitar cualquier riesgo o daño.

**AVISO:** Este producto ha sido diseñado para Ambiente Industrial Severo. De ser utilizado en Ambiente Residencial el usuario podría requerir algunas medidas en caso de que note algún ruido eléctrico inesperado en artefactos domésticos.

**ALERTA:** Errores en la conexión o la aplicación en ambientes fuera de los límites especificados del GII+ pueden resultar en un mal funcionamiento, o daños en sus componentes.

## Partes y Piezas

### Vista Frontal

1. **Indicadores Luminosos (LED's)**
   - Luz Fija - CONECTADO (ON)
   - Luz Intermitente - TEMPORIZADO (TC) a la Conexión
   - Luz Fija - FALLA

2. **Pantalla LCD**
3. **Botón Pulsador de Rearme (Arranque)**
4. **Botones Pulsadores para Ajustes**
5. **Botón Pulsador para Selección**
6. **Frontal Insertable para Flush Mounting**
7. **Gancho Sujetador para Frontal**
8. **Ranura posterior para montaje en Riel simétrico**
9. **Sujetador Insertable para Montaje en Superficie Plana**
10. **Gancho de Retención para montaje en Riel simétrico**
11. **Terminales Enchufables**
12. **GIO PORT (Puerto de Comunicación)**
13. **Cubierta plástica protectora del GIO PORT**

## Montaje Mecánico

### Montaje sobre Riel Simétrico DIN

**PRECAUCIÓN:** GII+ debe ser instalado en lugar accesible, libre de polvo, sucio, humedad y vibraciones. Que tenga suficiente espacio para la circulación de aire alrededor de su cubierta y fácil acceso a los controles de operación disponible. SOLO DE USO INTERIOR.

**Instrucciones:**

a) Coloque el GII+ en posición inclinada enganchando la ranura posterior con el Riel, luego empuje presionando el GII+ hasta que haga CLICK.

### Montaje sobre Superficie Plana

**Instrucciones:**

a) Saque los dos (2) sujetadores insertables localizados en la parte posterior del GII+, y luego insértelos dentro de las ranuras verticales que también se encuentran en la parte posterior del GII+.

b) Coloque el GII+ sobre la superficie plana del panel y fíjelo usando tornillos 3/16 x 1/2 pulgadas, empleando un destornillador o desarmador adecuado.

**Recomendación para Montaje en Superficie Plana:**

Haga dos (2) agujeros de 4 mm (5/32 pulgadas) de diámetro sobre la superficie plana del panel antes de instalar el GII+.

### Montaje Empotrable (Flush Mounting)

**Instrucciones:**

a) Realice el corte del panel de acuerdo a las dimensiones especificadas:
   - Guía para Montaje Empotrable en Panel: 111 mm x 85 mm
   - Tolerancia: +/-2 mm

b) Remueva los Ganchos Sujetadores para Frontal y el Frontal Insertable. Para remover los Ganchos Sujetadores levántelos suavemente y deslice.

c) Inserte el Frontal del GII+ en el panel.

d) Coloque el GII+ desde la parte posterior y use los Ganchos Sujetadores para Frontal para fijar el GII+, hasta que haga CLICK.

## Dimensiones Generales

- Ancho: 105 mm
- Alto: 124 mm
- Profundidad: 86 mm

**Guía para Superficie Plana:**
- Ancho: 64.5 mm (Tolerancia: +/-2 mm)
- Alto: 90 mm
- Separación entre agujeros: 85 mm

## Diagrama de Conexión

### Designación de Terminales

| Terminal | Descripción |
|----------|-------------|
| L1 | Entrada de Voltaje (Fase R) |
| L3 | Entrada de Voltaje (Fase S) |
| L5 | Entrada de Voltaje (Fase T) |
| 2, 4, 6, 7, 9, 11 | No utilizados |
| 8 | Contacto para Control de Contactor |
| 10 | Contacto Común |
| 12 | Contacto para Señalización Auxiliar |

### Estados de Contactos

**Estado Normal:**
- 10 – 12 conectado
- 8 – 10 abierto

**Estado Disparado (Falla):**
- 10 – 12 abierto
- 8 – 10 conectado

**Precaución:** Desconecte el suministro de energía antes de instalar el GII+. Hacer caso omiso puede resultar en lesiones severas incluso la muerte.

**Precaución:** Verifique que el modelo GII+ seleccionado para instalar corresponda con el voltaje nominal de línea del sistema a conectar.

## Operación

GII+ supervisa constantemente los valores de voltaje de línea. Cuando una condición de falla dañina ocurre, su salida se desactiva, manteniéndose así, hasta que la falla desaparezca totalmente.

Utilice el Botón Pulsador Rearme para restablecer manualmente el GII+ cuando sea requerido.

El GII+ dispone de Temporizador a la Conexión (TC) y a la Desconexión (TD), para prevenir falsos disparos en casos de rápidas y eventuales fluctuaciones de la red.

**Especificación de Operación:**
- Tensión de entrada: 210 V (por fase)
- Frecuencia: 60.0 Hz
- Modo: Manual
- Capacidad de contacto: 10 A / CA
```