```markdown
---
title: "GII+ Manual de Instalación"
type: Technical
source: "GII_MAN_V4_VE.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GII+"
date_processed: "2026-05-09"
---

# GII+ MANUAL DE INSTALACIÓN

## 1. DESCRIPCIÓN GENERAL

GII+ es un Relé (Relevador) digital para Protección contra Fallas de Fase diseñado para proteger la carga conectada a la red de distribución contra daños ocasionados por fallas comunes de voltaje. Provee una pantalla LCD para indicar el estado de la salida.

### Alertas de Seguridad

**ALERTA:** Solo personal técnico calificado con conocimientos en Relés (Relevadores) de protección y la carga asociada debería realizar la instalación, arranque y mantenimiento del sistema. Hacer caso omiso podría resultar en lesiones a personas y/o daños a los equipos conectados.

**ALERTA:** Este producto puede activar al Contactor y hacer que arranque el sistema o carga conectada en forma automática. El usuario debe tomar precauciones para evitar cualquier riesgo o daño.

**AVISO:** Este producto ha sido diseñado para Ambiente Industrial Severo. De ser utilizado en Ambiente Residencial el usuario podra requerir algunas medidas en caso de que note algún ruido eléctrico inesperado en artefactos domésticos.

**ALERTA:** Errores en la conexión o la aplicación en ambientes fuera de los límites especificados del GII+ pueden resultar en un mal funcionamiento, o daños en sus componentes.

## 2. GII+ PARTES Y PIEZAS

### Vista Frontal

1. **Indicadores Luminosos (LEDs)**
   - Luz Fija - CONECTADO (ON)
   - Luz Intermitente - TEMPORIZADO (TC) a la Conexión

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

### Indicadores LED

- **LED VERDE:** Luz Fija - CONECTADO (ON)
- **LED ROJO:** Luz Fija - FALLA

## 3. GII+ MONTAJE SOBRE RIEL SIMÉTRICO DIN

### Instrucciones para Montaje Mecánico

a) Coloque el GII+ en posición inclinada enganchando la ranura posterior con el Riel, luego empuje presionando el GII+ hasta que haga CLICK, tal como se muestra en la figura.

**PRECAUCIÓN:** GII+ debe ser instalado en lugar accesible, libre de polvo, sucio, humedad y vibraciones. Que tenga suficiente espacio para la circulación de aire alrededor de su cubierta y fácil acceso a los controles de operación disponible. SOLO DE USO INTERIOR.

## 4. GII+ MONTAJE SOBRE SUPERFICIE PLANA

### Instrucciones para Montaje Mecánico

a) Saque los dos (2) sujetadores insertables localizados en la parte posterior del GII+, y luego insértelos dentro de las ranuras verticales que también se encuentran en la parte posterior del GII+.

b) Coloque el GII+ sobre la superficie plana del panel y fíjelo usando tornillos 3/16 x 1/2 pulgadas, empleando un destornillador o desarmador adecuado.

### Recomendación para Montaje en Superficie Plana

Haga dos (2) agujeros de 4 mm (5/32 pulgadas) de diámetro sobre la superficie plana del panel antes de instalar el GII+. Ver Guía para Superficie Plana mostrada en el punto 6 (GII+ Dimensiones Generales).

## 5. GII+ MONTAJE EMPOTRABLE (FLUSH MOUNTING)

### Instrucciones para Montaje Mecánico

a) Realice el corte del panel de acuerdo a la figura de Guía para Montaje Empotrable en Panel:
   - Dimensiones: 111 mm x 85 mm
   - Tolerancia: +/-2 mm
   - Profundidad: 64.5 mm

b) Remueva los Ganchos Sujetadores para Frontal y el Frontal Insertable. Para remover los Ganchos Sujetadores levántelos suavemente y deslice.

c) Inserte el Frontal del GII+ en el panel.

d) Coloque el GII+ desde la parte posterior y use los Ganchos Sujetadores para Frontal para fijar el GII+, hasta que haga CLICK.

## 6. GII+ DIMENSIONES GENERALES

- **Altura:** 124 mm
- **Ancho:** 105 mm
- **Profundidad:** 86 mm
- **Profundidad (frontal):** 8.99 mm

## 7. GII+ DIAGRAMA DE CONEXIÓN

**PELIGRO:** Desconecte el suministro de energía antes de instalar el GII+. Hacer caso omiso puede resultar en lesiones severas incluso la muerte.

**PRECAUCIÓN:** Verifique que el modelo GII+ seleccionado para instalar corresponda con el voltaje nominal de línea del sistema a conectar.

### 7.1 Designación de Terminales

| TERMINAL | DESCRIPCIÓN |
|----------|-------------|
| L1 | Entrada de Voltaje (Fase R) |
| L3 | Entrada de Voltaje (Fase S) |
| L5 | Entrada de Voltaje (Fase T) |
| 2, 4, 6, 7, 9, 11 | No utilizados |
| 8 | Contacto para Control de Contactor |
| 10 | Contacto Común |
| 12 | Contacto para Señalización Auxiliar |

### Estados de Salida

- **10 - 12 conectado / 8 - 10 abierto:** Disparado
- **10 - 12 abierto / 8 - 10 conectado:** Normal

### 7.2 Diagrama Básico de Instalación

El diagrama muestra las conexiones de entrada de voltaje (L1, L3, L5) desde la red, conexión a bobina del contactor, y terminales de control.

## 8. GII+ OPERACIÓN

GII+ supervisa constantemente los valores de voltaje de línea. Cuando una condición de falla dañina ocurre, su salida se desactiva, manteniéndose así, hasta que la falla desaparezca totalmente. El GII+ dispone de Temporizador a la Conexión (TC) y a la Desconexión (TD).

Utilice el Botón Pulsador Rearme para conectar manualmente cuando GII+ está en estado de falla y el Interruptor para prevenir falsos disparos en casos de rápidas y eventuales fluctuaciones.

---

*Accesorio se vende por separado.
```