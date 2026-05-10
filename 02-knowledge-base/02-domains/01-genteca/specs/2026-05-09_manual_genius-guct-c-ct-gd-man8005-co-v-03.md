```markdown
---
title: "GUCT+ Manual de Instalación"
type: Technical
source: "GUCT+ c-CT GD-MAN8005-CO-V.03.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GUCT+"
date_processed: "2026-05-09"
---

# GUCT+ MANUAL DE INSTALACIÓN

## DESCRIPCIÓN GENERAL

GUCT+ es un Relé (Relevador) electrónico para Protección y Control para Generadores, Transformadores y Motores que supervisa constantemente las corrientes del motor y voltajes de alimentación. Mediante algoritmos de modelaje térmico protege contra sobrecarga, subcarga y fallas de voltaje.

### Alertas y Avisos

**ALERTA:** Solo personal técnico calificado con conocimientos en relevadores de sobrecarga y de la maquinaria a proteger, debería realizar la instalación, arranque y mantenimiento del sistema. Hacer caso omiso podría resultar en lesiones a personas y/o daños a los equipos conectados.

**AVISO:** Este producto ha sido diseñado para Ambiente Industrial Severo. De ser utilizado en Ambiente Residencial el usuario podría requerir algunas medidas en caso de que note algún ruido eléctrico inesperado en artefactos domésticos.

**ALERTA:** Este producto puede activar al Contactor y hacer que arranque el motor de forma automática. El usuario debe tomar precauciones para evitar cualquier riesgo o daño.

**ALERTA:** Errores en la conexión o la aplicación en ambientes fuera de los límites especificados del GUCT+, pueden resultar en un mal funcionamiento, o daños en sus componentes.

## PARTES Y PIEZAS

1. **Pantalla de lectura:**
   - PANTALLA LCD: Presenta información de mediciones, estados, configuraciones e historia, en texto y números.

2. **Indicadores luminosos (LED's):**
   - FALLA: Luz roja fija, indica apagado de salida, debido a falla.
   - CONTROL: Luz verde; intermitente indica temporizado de reconexión, fijo indica estado normal.

3. **Pulsador REARME:** Reanuda la operación después de parada, bajo modo de rearme manual.

4. **Pulsadores AJUSTE:** Introduce datos para ajustar distintas configuraciones.

5. **Pulsador SELECCIÓN:** Selecciona el parámetro o estado deseado para lectura y/o ajuste.

6. **Ranura posterior para montaje en riel simétrico.**

7. **Sujetadores insertables para montaje en superficies planas.**

8. **Gancho de retención para montaje en riel simétrico.**

9. **Orificios con sensores de corriente:** Para pasar cables de alimentación al motor.

10. **Entradas de Voltaje de Línea:** L1 L2 L3.

11. **Contactos del Relé:** (95-96) y (97-98).
    - 95-96 conectado / 97-98 abierto = Disparado
    - 95-96 abierto / 97-98 conectado = Normal

12. **GIO PORT:** Puerto de comunicación.

13. **Cubierta plástica protectora del puerto GIO PORT.**

## MONTAJE SOBRE RIEL SIMÉTRICO DIN

**Instrucciones para Montaje Mecánico:**

Coloque el GUCT+ en posición inclinada enganchando la ranura posterior con el riel. Luego empuje presionando el GUCT+ hasta que haga CLICK, tal como se muestra en la figura.

**PRECAUCIÓN:** GUCT+ debe ser instalado en lugar accesible, libre de polvo, sucio, humedad y vibraciones. Que tenga suficiente espacio para la circulación de aire alrededor de su cubierta y fácil acceso a los controles de operación.

## MONTAJE SOBRE SUPERFICIE PLANA

**Instrucciones para Montaje Mecánico:**

a) Saque los dos (2) sujetadores insertables localizados en la parte posterior del GUCT+. Luego inserte ambos sujetadores dentro de las ranuras verticales de la parte posterior del GUCT+.

b) Coloque el GUCT+ sobre la superficie plana del panel y fíjelo usando tornillos 3/16" x 1/2", empleando un destornillador (desarmador) adecuado.

**Recomendación para Montaje sobre Superficie Plana:**

Haga dos (2) agujeros de 4mm (5/32") de diámetro sobre la superficie del panel antes de instalar el GUCT+.

## DIMENSIONES GENERALES

- Altura: 111 mm
- Ancho: 101 mm
- Profundidad: 69 mm
- Espaciado para orificios de montaje: 72 mm x 92 mm
- Diámetros de orificios de montaje: 4 mm (5/32")

## DIAGRAMA DE CONEXIÓN

### Designación de Terminales

| TERMINAL | DESCRIPCIÓN |
|----------|-------------|
| L1 | Entrada Voltaje (Fase R) |
| L2 | Entrada Voltaje (Fase S) |
| L3 | Entrada Voltaje (Fase T) |
| 95 | Contactos para Señalización Auxiliar |
| 96 | Contactos para Señalización Auxiliar |
| 97 | Contactos para Control de Contactor |
| 98 | Contactos para Control de Contactor |

### Estados de Contactos

- **95-96 Conectado / 97-98 Abierto:** Disparado
- **95-96 Abierto / 97-98 Conectado:** Normal

### Recomendaciones para Cableado

- Evite apretar excesivamente los tornillos M3 de los terminales durante la conexión. Torque máximo: 5,1 Kg•cm / 4,4 lb-in.
- Pelar los aislantes de los cables a conectar entre 6 a 7 mm.
- Usar cables para terminales: entre AWG10 y AWG18.
- El máximo tamaño de los cables del motor a pasar por orificios de sensores de corrientes será de: AWG 4.
- Conecte los terminales de Voltaje de Entrada L1L2L3 antes del Contactor y su respectivo circuito de arranque.
- Siempre pase los tres cables del motor por los tres orificios de sensores de corrientes. Dejar algún orificio sin cablear ocasionará falsas lecturas de desbalance.

### Diagrama Básico de Instalación

El GUCT+ incluye:
- Interruptor contra cortocircuito
- Protección contra cortocircuito con fusibles opcionales (5A, 600V)
- Conexión a bobina del contactor
- Puerto GIO para comunicación serial con otros dispositivos (opcional, requiere GIOPlug Adaptador)
- Circuito de control y arranque

**Aplicable con los siguientes modelos:**
- GUCT+20800S
- GUCT+48000S

## OPERACIÓN

GUCT+ constantemente supervisa valores de corriente, parámetros de voltaje, frecuencia, potencia de la red en Generadores, Transformadores y Motores. Cuando alguna condición de falla dañina ocurre, el GUCT+ desconectará al circuito arrancador del motor, manteniendo al motor apagado hasta que la falla eléctrica desaparezca y el motor se haya enfriado.

## DESMONTAJE (RIEL SIMÉTRICO DIN)

(Sección incompleta en documento fuente)

---

**PELIGRO:** Desconecte el suministro de energía antes de instalar el GUCT+. Hacer