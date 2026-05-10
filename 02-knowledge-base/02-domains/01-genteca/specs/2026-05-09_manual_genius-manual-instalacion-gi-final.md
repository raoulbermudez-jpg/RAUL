---
title: "Manual de Instalación GI+"
type: Technical
source: "Manual Instalacion GI+ Final.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GI+"
date_processed: "2026-05-09"
---

# GI+ Manual de Instalación

## 1. Descripción General

GI+ es un Relé (Relevador) digital para Protección contra Fallas de Fase diseñado para proteger la carga conectada a la red de distribución contra daños ocasionados por fallas comunes de voltaje. Provee un Display LCD para indicar el estatus de la salida.

### Advertencias Importantes

**ALERTA:** Solo personal técnico calificado con conocimientos en relés (relevadores) de protección y la carga asociada debería realizar la instalación, arranque y mantenimiento del sistema. Hacer caso omiso podría resultar en lesiones a personas y/o daños a los equipos conectados.

**ALERTA:** Este producto puede activar al Contactor y hacer que arranque el sistema o carga conectada en forma automática. El usuario debe tomar precauciones para evitar cualquier riesgo o daño.

**AVISO:** Este producto ha sido diseñado para Ambiente Industrial Severo. De ser utilizado en Ambiente Residencial el usuario podría requerir algunas medidas en caso de que note algún ruido eléctrico inesperado en artefactos domésticos.

**ALERTA:** Errores en la conexión o la aplicación en ambientes fuera de los límites especificados del GI+ pueden resultar en un mal funcionamiento, o daños en sus componentes.

## 2. GI+ Partes y Piezas

### Vista Frontal

1. **Indicadores Luminosos (LEDs)**
   - LED Verde - Luz Fija: CONECTADO (ON)
   - LED Verde - Luz Intermitente: TEMPORIZADO (TC) a la Conexión
   - LED Rojo - Luz Fija: FALLA

2. **Pantalla LCD**

3. **Botón Pulsador de Rearme (Arranque)**

4. **Botones Pulsadores para Ajustes**

5. **Botón Pulsador para Selección**

6. **Frontal Insertable para Flush Mounting**

### Vista Posterior

7. **Gancho Sujetador para Frontal**

8. **Ranura posterior para montaje en Riel simétrico**

9. **Sujetador Insertable para Montaje en Superficie Plana**

10. **Gancho de Retención para montaje en Riel simétrico**

11. **Terminales Enchufables**

12. **GIO PORT (Puerto de Comunicación)**

13. **Cubierta plástica protectora del GIO PORT**

## 3. GI+ Montaje sobre Riel Simétrico DIN

### Instrucciones para Montaje Mecánico

**PRECAUCIÓN:** GI+ debe ser instalado en lugar accesible, libre de polvo, suciedad, humedad y vibraciones. Que tenga suficiente espacio para la circulación de aire alrededor de su cubierta y fácil acceso a los controles de operación disponible. SOLO DE USO INTERIOR.

a) Coloque el GI+ en posición inclinada enganchando la ranura posterior con el Riel, luego empuje presionando el GI+ hasta que haga CLICK.

## 4. GI+ Montaje sobre Superficie Plana

### Instrucciones para Montaje Mecánico

a) Saque los dos (2) sujetadores insertables localizados en la parte posterior del GI+, y luego insértelos dentro de las ranuras verticales que también se encuentran en la parte posterior del GI+.

b) Coloque el GI+ sobre la superficie plana del panel y fíjelo usando tornillos 3/16" x 1/2", empleando un destornillador (desarmador) adecuado.

### Recomendación para Montaje en Superficie Plana

Haga dos (2) agujeros de 5/32" de diámetro sobre la superficie plana del panel antes de instalar el GI+.

## 5. GI+ Montaje Empotrable (Flush Mounting)

### Instrucciones para Montaje Mecánico

a) Realice el corte del panel de acuerdo a la guía para montaje empotrable en panel.

b) Remueva los Ganchos Sujetadores para Frontal y el Frontal Insertable. Para remover los Ganchos Sujetadores levántelos suavemente y deslice.

c) Inserte el Frontal del GI+ en el panel.

d) Coloque el GI+ desde la parte posterior y use los Ganchos Sujetadores para Frontal para fijar el GI+, hasta que haga CLICK.

## 6. GI+ Dimensiones Generales

- **Altura:** 105 mm
- **Ancho:** 124 mm
- **Profundidad:** 86 mm
- **Agujeros de montaje en superficie plana:** 85 mm (separación vertical)
- **Tolerancia de corte para montaje empotrable:** +/- 2 mm

## 7. Diagrama de Conexión

### PELIGRO
Desconecte el suministro de energía antes de instalar el GI+. Hacer caso omiso puede resultar en lesiones severas incluso la muerte.

### PRECAUCIÓN
Verifique que el modelo GI+ seleccionado para instalar corresponda con el voltaje nominal de línea del sistema a conectar.

### 7.1 Designación de Terminales

| Terminal | Descripción |
|----------|-------------|
| L1 | Entrada de Voltaje (Fase R) |
| L3 | Entrada de Voltaje (Fase S) |
| L5 | Entrada de Voltaje (Fase T) |
| 2, 4, 6, 7, 9, 11 | No utilizados |
| 8 | Contacto para Control de Contactor |
| 10 | Contacto Común |
| 12 | Contacto para Señalización Auxiliar |

### Estados de Operación

**Disparado:**
- 10 – 12 conectado
- 8 – 10 abierto

**Normal:**
- 10 – 12 abierto
- 8 – 10 conectado

### 7.2 Diagrama Básico de Instalación

PRECAUCIÓN: Los siguientes ejemplos pueden diferir respecto de las conexiones requeridas para los equipos del usuario. El instalador debe determinar la forma adecuada de realizar las conexiones, de manera que simplemente interrumpa o apague el circuito de arranque del equipo a proteger. Hacer caso omiso podría resultar en daños por cortocircuitos o sobrecargas, sobre cables y partes de los equipos eléctricos.

## 8. GI+ Operación

GI+ supervisa constantemente los valores de voltaje de línea. Cuando una condición de falla dañina ocurre, su salida se desactiva, manteniéndose así, hasta que la falla desaparezca totalmente. El GI+ dispone de Temporizadora la Conexión (TC) y a la Desconexión (TD), para prevenir falsos disparos en casos de rápidas y eventuales fluctuaciones.