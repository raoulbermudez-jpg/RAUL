---
title: "Manual de Instalación Genius GOC"
type: Technical
source: "Manual Inst GOCT Final.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GOC"
version_status: "vigente"
date_processed: "2026-05-10"
---

# Manual de Instalación Genius GOC

## Descripción General

GOC es un Relé electrónico para Protección Integral de Motores que supervisa constantemente las corrientes del motor y voltajes de alimentación.

Mediante algoritmos de modelaje térmico protege contra sobrecarga y fallas de voltaje.

## Partes y Piezas

### Indicadores Luminosos (LEDs)

- **CONECTADO (ON)** - Luz verde fija
- **SOBRECARGA (OL)** - Luz roja fija
- **SOBREVOLTAJE (OV)** - Luz roja fija
- **TEMPORIZADO (TC)** - Luz verde intermitente
- **FASE INVERTIDA (PR)** - Luz roja intermitente
- **DESBALANCE (UB)** - Luz roja fija
- **PÉRDIDA DE FASE (SP)** - Luz roja intermitente
- **BAJO VOLTAJE (UV)** - Luz roja intermitente

### Componentes Principales

1. Indicadores Luminosos (LEDs)
2. Perilla de Ajuste de corriente máxima FLA
3. Perilla de Ajuste de temporizado de conexión TC
4. Ranura posterior para montaje en riel simétrico
5. Sujetadores insertables para montaje en superficies planas
6. Gancho de retención para montaje en riel simétrico
7. Orificios con sensores de corriente para pasar cables de alimentación al motor
8. Entradas de Voltaje de Línea (L1, L2, L3)
9. Contactos del Relé (95-96) y (97-98)
10. GIO PORT (puerto de comunicación)
11. Selector para Modo de REARME AUTO / MANUAL
12. Pulsador para Arranque MANUAL (REARME MANUAL)
13. Cubierta plástica protectora del puerto GIO PORT

### Estados de Contactos del Relé

| Estado | 95-96 | 97-98 |
|--------|-------|-------|
| Normal | Abierto | Conectado |
| Disparado | Conectado | Abierto |

## Montaje Mecánico

### Montaje sobre Riel Simétrico DIN

**PRECAUCIÓN:** GOC debe ser instalado en lugar accesible, libre de polvo, suciedad, humedad y vibraciones. Que tenga suficiente espacio para la circulación de aire alrededor de su cubierta y fácil acceso a los controles de operación. SOLO PARA USO INTERIOR.

a) Coloque el GOC en posición inclinada enganchando la ranura posterior con el riel. Luego empuje presionando el GOC hasta que haga CLICK.

### Montaje sobre Superficie Plana

a) Saque los dos (2) sujetadores insertables localizados en la parte posterior del GOC. Luego inserte ambos sujetadores dentro de las ranuras verticales de la parte posterior del GOC.

b) Coloque el GOC sobre la superficie plana del panel y fijelo usando tornillos 3/16" x 1/2", empleando un destornillador adecuado.

**Recomendación:** Haga dos (2) agujeros de 5/32" de diámetro sobre la superficie del panel antes de instalar el GOC.

## Dimensiones Generales

- Medidas: 92 x 91 x 96 (L x A x H) mm
- Peso: 398 g (0.87 lb)

## Diagrama de Conexión

### Designación de Terminales

| Terminal | Descripción |
|----------|-------------|
| L1 | Entrada Voltaje (Fase R) |
| L2 | Entrada Voltaje (Fase S) |
| L3 | Entrada Voltaje (Fase T) |
| 95-96 | Contactos para Señalización Auxiliar |
| 97-98 | Contactos para Control de Contactor |

### Diagrama Básico de Instalación

El diagrama incluye:
- Interruptor de alimentación principal
- Contactor
- Fusibles (5A, 600V)
- Conexión GOC con GIO Port
- Botón de REARME manual
- Bobina del contactor
- Luz piloto de alarma (opcional)

### Recomendaciones para Cableado

- Evite apretar excesivamente los tornillos M3 de los terminales. Torque máximo: 4.4 Ib-in (5.1 kg-cm)
- Pelar los aislantes de los cables a conectar entre 6 a 7 mm
- Usar cables para terminales: entre AWG10 (4mm²) y AWG18
- El máximo tamaño de los cables del motor a pasar por orificios de sensores de corrientes será de: AWG 4 (11mm)
- Conecte los terminales de Voltaje de Entrada L1, L2, L3 antes del Contactor y su respectivo circuito de arranque
- Siempre pase los tres cables del motor por los tres orificios de sensores de corrientes. Dejar algún orificio sin cablear ocasionará falsas lecturas de desbalance

## Ajustes de Parámetros

### Procedimiento para Ajuste de Sobrecarga

a) Asegúrese que el Interruptor de la alimentación esté apagado (OFF).

**PRECAUCIÓN:** Con el uso de un amperímetro, verifique que la corriente de operación del motor aplicando su carga máxima de trabajo, sea menor que la establecida por el fabricante (FLA - Full Load Amperage).

**ATENCIÓN:** Cualquier cambio intencional o accidental en la posición de las perillas, después de ajustado el GOC podría causar variaciones en su funcionamiento. En este caso repita el procedimiento.

**NOTA:** Se recomienda efectuar este procedimiento operando el motor con su mayor carga de trabajo, de acuerdo a lo especificado en los datos de placa del motor.

b) Deslice el Selector de Modo de Rearme AUTO/MANUAL a la posición MANUAL.

c) Coloque el suiche del Interruptor de la alimentación a la posición ON (El motor continuará apagado debido a que el contactor se mantendrá desconectado por intermedio del GOC).

d) Oprima el botón pulsador de REARME y sosténgalo presionado (el motor arrancará y se mantendrá en marcha), mientras ejecuta los siguientes pasos.

e) Gire lentamente a la izquierda la perilla FLA hasta que el LED verde se encienda (ON). En este instante, el valor ajustado corresponderá a la corriente nominal del motor de acuerdo a su carga de trabajo.

f) Gire lentamente a la derecha la perilla FLA hasta alcanzar el nivel deseado de protección:
- Led Verde ON = In (corriente nominal)
- Led Rojo 1 ON = Sobrecarga 10%
- Led Rojo 2 ON = Sobrecarga 15%
- Led Rojo 3 ON = Sobrecarga 20%

g) Deslice el Selector de Modo de Rearme AUTO/MANUAL para seleccionar el modo de arranque deseado.

### Procedimiento para Ajuste de TC

a) Usando un destornillador plano, gire la perilla de ajuste de Temporizado de Conexión (TC) al valor de tiempo de retardo deseado (TC es el tiempo desde la recuperación de una falla por voltaje, hasta la reconexión), de acuerdo a sus necesidades de aplicación.

## Operación Genius GOC

Genius GOC supervisa constantemente la corriente del motor y los voltajes de línea. Cuando alguna condición de sobrecarga o falla de fase ocurre, su salida se desactiva manteniéndose así hasta que la falla desaparezca y/o el motor se haya enfriado completamente.

El GOC dispone un modo de arranque automático temporizado, por medio de un retardo interno (TEMPORIZADO-TC) el cual previene falsos disparos, en caso de rápidas y eventuales fluctuaciones de voltaje de la red.

Si en alguna ocasión llegase a suceder tres (3 o más) fallas de corriente en un intervalo menor a 30 minutos, el GOC desactivará permanentemente su salida, y solo se podrá restaurar la operación del sistema manualmente, oprimiendo el pulsador de REARME. Se recomienda verificar las causas de las tres fallas sucesivas.

### Descripción de Fallas y sus Indicaciones Luminosas

| Condición | Luz Continua | Luz Intermitente |
|-----------|--------------|------------------|
| **Led Verde** | Contactor conectado o habilitado (ON) | Temporizando (TC) |
| **Led Rojo 1** | Falla por Sobrecarga (OL) | Falla por Fase Invertida (PR) |
| **Led Rojo 2** | Falla por Desbalance de voltaje o corriente (UB) | Pérdida de Fase de Voltaje o Corriente (SP) |
| **Led Rojo 3** | Falla por Sobre Voltaje (OV) | Falla por Bajo voltaje (UV) |

**NOTA:** Cuando el GOC está seleccionado en modo de Rearme MANUAL o se encuentra bajo la condición de 3era falla, se presentarán los indicadores luminosos (LED Rojo 1, LED Rojo 2 y LED Rojo 3) encendidos de manera secuencial después de su correspondiente tiempo de protección. Esta condición se mantiene permanente hasta tanto el Usuario presione el Botón Pulsador de REARME.

### Modos de Rearme

**Rearme Manual:** En cada ocasión que se dispare una protección, se tendrá que presionar nuevamente el botón pulsador de REARME por 1 segundo, para rehabilitar la operación del Contactor.

**Rearme Automático:** También se requerirá pulsar el botón de REARME por 1 segundo, si ocurriesen 3 ó más fallas sucesivas por corrientes, en menos de 30 minutos. Se recomienda verificar las causas de las tres fallas sucesivas.

## Instrucciones de Desmontaje

**PELIGRO:** Apague el interruptor de alimentación (Breaker) y desconecte todos los cables al GOC antes de proceder a desmontarlo. Hacer caso omiso puede resultar en daños a los equipos o personas.

### Desmontaje (Riel Simétrico DIN)

a) Usando un destornillador plano, hale hacia abajo el Gancho de Retención dispuesto en la parte inferior del GOC.

b) Mediante el destornillador desplace el gancho a la posición 2, saque el GOC del Riel simétrico.

**Recomendación:** Hale suavemente y hacia abajo el gancho de retención unos 2 mm aproximadamente. Un movimiento brusco para sacar el gancho podría desprenderlo.

### Desmontaje (Superficie Plana)

a) Destornille ambos tornillos que fijan al GOC, a la superficie plana a través de los sujetadores insertables y luego saque el GOC de dicha superficie.

## Especificaciones Técnicas

### A) Fuente de Poder

| Parámetro | 208/220 VAC | 440/480 VAC |
|-----------|------------|------------|
| Voltaje de Operación, Ue | 208/220 | 440/480 |
| Límite de Operación de Voltaje, Ue | 124-300 | 264-672 |
| Consumo Promedio, In | 38 mA | — |
| Frecuencia Nominal Fn | 50 / 60 Hz | — |
| Frecuencia de Operación | 42–70 Hz | — |
| Modo de Operación | Continuo | — |

### B) Condiciones Ambientales, Límites de Operación e Instalación

| Parámetro | Valor |
|-----------|-------|
| Normas (EUROPA) | IEC61010-1, IEC60255-6, IEC60947-1, LVD & EMC |
| Normas (USA) | UL (pendiente), NKCR, Dispositivos Auxiliares UL508 |
| Aprobación Europea | CE (pendiente), IEC60947-1 |
| Temperatura Ambiental (Operación) | -5°C a 55°C (23°F a 131°F) |
| Temperatura Ambiental (Almacenaje) | -10°C a +70°C (14°F a 158°F) |
| Humedad Relativa Máxima | 85% R.H. |
| Resistencia a Vibraciones | Clase 1, Amplitud <0.035 mm @ 10 Hz < f < 150 Hz, IEC 60255-21-1 |
| Protección a Objetos/Agua | IP20, Protegido contra objetos > 125 mm, ninguna protección contra agua (IEC 60529) |
| Nivel de Contaminación | Grado 3 (IEC 60255-5) |
| Protección contra Exceso de Voltaje | Categoría III (IEC 60255-5) |
| Voltaje de Aislamiento Nominal | 500 V (UL) |
| Prueba de Impulso | 5 KV (IEC 60255-5) |
| Prueba Dieléctrica | 2.5 KV @ 50/60 Hz, 1 min (UL 508) |
| Grado de Protección al Fuego de la carcaza | V0 (UL-94) |
| Material de la Carcaza | Polímeros: LEXAN 500R, ABS, Nylon |
| Posiciones de Montaje | Sin Restricciones |
| Tipos de Montaje | Riel DIN Simétrico; Superficie Plana (Tornillo 3/16" x 1/2") |
| Tipo de Tornillo de Borneras | Plano M3 |
| Torque de Apretado de Borneras | 5.1 Kg-cm / 4.4 Ib-in |
| Cableado de Borneras | >10 AWG (4 mm²) <18 AWG |
| Cableado en el Sensor de Corriente | d < 11 mm, AWG 4 |
| Medidas | 92 x 91 x 96 (L x A x H) mm |
| Peso | 398 g (0.87 lb) |

### C) Características de Control

| Parámetro | Valor |
|-----------|-------|
| (para Circuitos de Control) Pilot Duty | Sección 139.1 |
| Expectativa de Vida Eléctrica | 100,000 Operaciones |
| Expectativa de Vida Mecánica | 10,000,000 Operaciones |
| Categoría de Uso | AC-15, Capacidad para Cargas > 72 VA (IEC60947-5-1) |

### D) Ajustes de Rango, Mediciones

| Modelo/Parámetro | 208 VAC | 480 VAC | Unidad |
|------------------|---------|---------|--------|
| Rango de medición de Voltaje, Um | 145–285 | 300–625 | VAC |
| Rango de Corriente | 1–4 | 3.5–12.5 | A |
| | 10–32 | 25–80 | A |
| Medición de Frecuencia | Precisión +/- 2% Hz |

### E) Funciones y Algoritmos de Protección

| Función | 208 VAC | 480 VAC | Norma/Referencia |
|---------|---------|---------|------------------|
| Bajo Voltaje (UV) @ Imotor=0 ó OL | 180 | 384 | VAC |
| Sobre Voltaje (OV) @ Imotor=0 ó OL | 261 | 540 | VAC |
| Umbral de Histéresis en el Voltaje | 7 | 12 | VAC |
| Ajuste de Corriente (FLA) | 1–4, 3.5–12.5, 10–32, 25–80 | Ajustable | — |
| Desbalance de Voltaje (VUB) | IN +/-8%, OUT +/-6% | — |
| Pérdida de fase de Voltaje (VSP) | IN VUB > 33%, OUT VUB < 28% | — |
| Fase Invertida (PR) | Secuencia ABC Normal, CBA Invertida | — |
| Desbalance de Corriente (CUB) | CUB > 48% | IEC 60255-8-1990 |
| Pérdida de Fase de Corriente (CSP) | CUB > 60% | IEC 60255-8-1990 |
| Clase Térmica | Curva Fría: 10, Curva Caliente: 3 | IEC 60255-8-1990 |
| Temporizado a la Desconexión por Falla de Sobrecorriente | Según el Nivel de Carga Extrema Inversa | IEC 60255-8-1990 |
| Desconexión permanente por Tercera Falla de Corriente | 3 Fallas de Corriente en menos de 30 min | IEEE Std. 037.112-1996 |
| Temporizado a la Desconexión por Fase Invertida | < 1 seg | — |
| Temporizado a la Desconexión por Otras Fallas de Voltaje (TD) | 3 seg | — |
| Temporizado a la Conexión por enfriamiento | 480 seg | — |
| Temporizado a la Conexión (TC) | 5–300 seg | Ajustable |
| Modo de Rearme | Automático/Manual | Selector Deslizante |

### F) Comunicaciones

| Parámetro | Especificación |
|-----------|----------------|
| Protocolo de Comunicaciones | MODBUS RTU @ 9600 8N1 |
| Puerto de Comunicaciones | GIO PORT |
| Reporte Histórico de Fallas | Últimas 20 Fallas |

**Nota:** Se requiere GPLUG para la comunicación a través de GIO Port. El GPLUG se suministra por separado.

### G) Compatibilidad Electromagnética para Ambiente Industrial Severo

- Descarga Electrostática (IEC 61000-4-2)
- Inmunidad a Ruido Eléctrico Radiado (IEC 61000-4-3)
- Transientes Rápidas (IEC 61000-4-4)
- Picos de Alta Energía (IEC 61000-4-5)
- Perturbaciones Conducidas (IEC 61000-4-6)
- Campos Magnéticos (IEC 61000-4-8)
- Reducciones e Interrupciones de Voltaje (IEC 61000-4-11)
- Armónicos (IEC 61000-4-13)
- Fluctuaciones de Voltaje (IEC 61000-4-14)
- Desbalance Trifásico (IEC 61000-4-27)
- Variaciones de Frecuencia (IEC 61000-4-28)

## Curvas de Protección Térmica

El GOC presenta dos curvas de operación:

- **Curva Fría:** Tiempo de disparo de 10 segundos a 1.0 In
- **Curva Caliente:** Tiempo de disparo de 3 segundos a 1.0 In

(Donde In = Valor de corriente calibrada por el usuario en el GOC, equivalente a la corriente del motor con su máxima carga FLA)

## Cómo Ordenar Genius GOC

**Formato:** GOCT [Número de Fases]-[Voltaje]-[Corriente]-[Idioma]

| Parámetro | Opciones |
|-----------|----------|
| Número de Fases | T – TRIFÁSICO |
| Voltaje | 208 – 208/220 VAC; 480 – 440/480 VAC |
| Corriente | 1–4 A; 3.5–12.5 A; 10–32 A; 25–80 A |
| Idioma | S – ESPAÑOL; E – INGLÉS; P – PORTUGUÉS |

---

**Información de Contacto:**

Genteca Buzcom ACSA 0158, P.O. Box 28537 Miami, FL 33102, USA

Avenida El Buen Pastor cruce con calle Vargas, Edificio Alba, Piso 1, Local 1-A, Boleíta Norte, Caracas - Venezuela, Zona Postal 1070

Teléfono: ++(58 212) 237.07.11 (Master) / 34.77 / 11.51 / Fax: ++(58 212) 235.24.97

Correo: genteven@genteca.com.ve | Web: www.genteca.com.ve

**NOTA:** Las especificaciones y descripciones mostradas en este documento están sujetas a cambio sin previo aviso.
