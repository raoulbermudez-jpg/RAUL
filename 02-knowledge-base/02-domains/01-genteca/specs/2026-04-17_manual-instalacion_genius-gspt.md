# Manual de Instalación — Genius SUBtronic GSPT

**Producto:** Genius SUBtronic GSPT  
**Tipo de documento:** Manual de Instalación  
**Referencia:** MV-02-01070.E-01-S  
**Versión de Software:** 1.12  
**Fabricante:** Gente, Generación de Tecnología, C.A. — www.genteca.com.ve

---

## 1. Descripción General

El **GSPT** es un Relé digital para **Protección de Bombas Sumergibles** que supervisa constantemente la Corriente del Motor y los principales parámetros eléctricos tales como Voltaje, Frecuencia, Factor de potencia, Potencia real, Potencia aparente y Consumo de energía, dando protección confiable contra Sobrecargas, Falla de fase, Fase invertida, Pérdida de fase, Desbalances y Arranques excesivos.

> **ALERTA:** Solo personal técnico calificado con conocimientos en relés de sobrecarga y de la maquinaria a proteger debe realizar la instalación, arranque y mantenimiento del sistema.

> **AVISO:** Diseñado para Ambiente Industrial Severo. En uso Residencial puede generar ruido eléctrico inesperado en artefactos domésticos.

---

## 2. Partes y Piezas

| N.° | Componente |
|-----|-----------|
| 1 | Pantalla de lectura LCD (mediciones, estados, configuraciones e historia) |
| 2 | Indicadores luminosos LED: FALLA (rojo fijo), CONTROL (verde intermitente = temporizando, fijo = normal) |
| 3 | Pulsador REARME: reanuda operación tras parada por falla |
| 4 | Pulsadores AJUSTE: introducen datos de configuración |
| 5 | Pulsador SELECCIÓN: selecciona parámetro o estado para lectura/ajuste |
| 6 | Ranura posterior para montaje en riel simétrico |
| 7 | Sujetadores insertables para montaje en superficie plana |
| 8 | Gancho de retención para riel simétrico |
| 9 | Orificios con sensores de corriente para pasar cables del motor |
| 10 | Entradas de Voltaje de Línea (L1, L2, L3) |
| 11 | Contactos del Relé: 95-96 y 97-98 (Disparado: 95-96 conectado / 97-98 abierto; Normal: 95-96 abierto / 97-98 conectado) |
| 12 | GIO PORT (puerto de comunicación MODBUS RTU) |
| 13 | Cubierta plástica protectora del GIO PORT |

---

## 3. Montaje en Riel Simétrico DIN

> **PRECAUCIÓN:** Instalar en lugar accesible, libre de polvo, sucio, humedad y vibraciones. Con suficiente circulación de aire alrededor de la cubierta y fácil acceso a los controles. **SOLO PARA USO INTERIOR.**

1. Colocar el GSPT en posición inclinada enganchando la ranura posterior con el riel.
2. Empujar presionando el GSPT hasta que haga **CLICK**.

---

## 4. Montaje sobre Superficie Plana

1. Sacar los dos (2) sujetadores insertables de la parte posterior del GSPT.
2. Insertar ambos sujetadores dentro de las ranuras verticales de la parte posterior.
3. Colocar el GSPT sobre la superficie plana del panel.
4. Fijar usando tornillos 3/16" x 1/2" con destornillador adecuado.

**Recomendación:** Hacer dos agujeros de 5/32" de diámetro sobre la superficie del panel antes de instalar (ver dimensiones generales).

---

## 5. Dimensiones Generales

| Dimensión | Valor |
|-----------|-------|
| Ancho | 100 mm |
| Alto | 111 mm |
| Profundidad | 96.15 mm |
| Ancho frontal | 93 mm |
| Alto frontal | 91 mm |
| Separación agujeros superficie plana | 72 mm |
| Diámetro agujeros montaje | 5/32" |

---

## 6. Diagrama de Conexión

> **PELIGRO:** Desconecte el suministro de energía antes de instalar el GSPT. Puede resultar en lesiones severas incluso la muerte.

> **PRECAUCIÓN:** Verifique que el modelo GSPT seleccionado corresponda con el voltaje nominal de línea y rango de corriente del motor.

### 6.1 Designación de Terminales

| Terminal | Descripción |
|----------|-------------|
| L1 | Entrada Voltaje (Fase R) |
| L2 | Entrada Voltaje (Fase S) |
| L3 | Entrada Voltaje (Fase T) |
| 95 / 96 | Contactos para Señalización Auxiliar |
| 97 / 98 | Contactos para Control de Contactor |
| 95-96 conectado / 97-98 abierto | Estado Disparado |
| 95-96 abierto / 97-98 conectado | Estado Normal |

### Recomendaciones para Cableado

- Torque máximo en terminales M3: 4.4 lb-in (5.1 kg-cm).
- Pelar aislantes de cables a conectar entre 6 y 7 mm.
- Calibre para terminales: entre AWG 10 (4 mm²) y AWG 18.
- Máximo tamaño de cables del motor para los orificios de sensores de corriente: AWG 4 (11 mm).
- Conectar los terminales L1, L2, L3 antes del Contactor y su respectivo circuito de arranque.
- Siempre pasar los **tres cables del motor** por los tres orificios de sensores de corriente. Dejar algún orificio sin cablear ocasionará falsas lecturas de desbalance.

---

## 7. Operación

El GSPT supervisa constantemente corriente del motor, voltaje, frecuencia y potencia de la red. Cuando ocurre una condición de falla dañina, su salida se desactiva hasta que:
- La falla desaparezca.
- Las condiciones del sistema se hayan restablecido.
- El motor se haya enfriado.

Dispone de:
- Temporizador a la Conexión (Arranque).
- Temporizador a la Desconexión por presencia de Falla.

Si ocurren **tres o más fallas de corriente en un intervalo menor a 30 minutos**, el GSPT desactivará permanentemente su salida. Solo se restaura manualmente con el pulsador de REARME.

### Descripción de Fallas y sus Indicaciones Luminosas

| LED | Luz Continua | Luz Intermitente |
|-----|-------------|-----------------|
| Verde | Contactor conectado o habilitado (ON) | Temporizando (TC) |
| Rojo | Falla de voltaje o corriente (FALLA) | — |

---

## 8. Instrucciones de Desmontaje

> **PELIGRO:** Apague el interruptor de alimentación (Breaker) y desconecte todos los cables del GSPT antes de proceder.

### 8.1 Desmontaje desde Riel Simétrico DIN
1. Usando un destornillador plano, halar hacia abajo el Gancho de Retención ubicado en la parte inferior del GSPT.
2. Desplazar el gancho a posición 2 (aprox. 2 mm) y sacar el GSPT del riel.

**Recomendación:** Halar suavemente y hacia abajo unos 2 mm. Un movimiento brusco puede desprenderlo.

### 8.2 Desmontaje desde Superficie Plana
1. Destornillar ambos tornillos que fijan el GSPT a la superficie.
2. Sacar el GSPT de la superficie.

---

## 9. Guía Rápida de Programación (Software v1.12)

### Pantallas de Estado del Relé

| Pantalla | Descripción |
|----------|-------------|
| 1.1 | Desconectado por MODBUS |
| 1.2 | Desconectado Bajo Modo Manual |
| 1.3 | Desconectado por 3era. Falla |
| 1.4 | Temporizado a la Conexión (TC) |
| 1.5 | Temporizado a la Conexión (TC) — MIN OFF TC |
| 1.6 | TC por Subcarga |
| 1.7 | Bajo Voltaje (UV) |
| 1.8 | Sobre Voltaje (OV) |
| 1.9 | Desbalance de Voltaje (VUB) |
| 1.10 | Variación de Frecuencia (FS) |
| 1.11 | Pérdida de Fase (VSP) |
| 1.12 | Fase Invertida (PR) |
| 1.13 | Porcentaje (%) de Calor Acumulado |
| 1.14 | Sobrecalentamiento |
| 1.15 | Relé Desviado |

### Menú Principal de Ajustes (Pantalla 7)

- Ajuste Voltaje
- Ajuste Corriente
- Ajuste Reloj
- Modo de Rearme
- Cambio de Clave
- Dirección MODBUS
- Borrar Histórico
- Reiniciar Equipo
- Salir

### Glosario de Abreviaturas

| Abreviatura | Significado |
|-------------|-------------|
| Sph | Arranques por hora |
| JF | Tercera falla |
| BR | Relé desviado |
| SM | Arranque forzado |
| TEF | Falla de energía |
| FS | Frecuencia |
| RL | Rotor bloqueado |
| PF | Factor de potencia |
| UC | Baja corriente |
| OL | Sobre corriente |
| VSP | Pérdida de fase por voltaje |
| CSP | Pérdida de fase por corriente |
| VUB | Desbalance de voltaje |
| PR | Fase invertida |
| UV | Bajo voltaje |
| OV | Sobre voltaje |
| CUB | Desbalance de corriente |

---

## 10. Especificaciones Técnicas

### A) Fuente de Poder

| Parámetro | 208/220/240 VAC | 400 VAC | 440/480 VAC |
|-----------|----------------|---------|-------------|
| Voltaje de Operación (Ue) | 208/220/240 | 400 | 440/480 | VAC |
| Límites de Voltaje de Operación (Ue) | 145 → 312 | 228 → 532 | 264 → 672 | VAC |
| Consumo Promedio (In) | 45 mA | — | — |
| Frecuencia Nominal (Fn) | 50/60 Hz | — | — |
| Frecuencia de Operación | 42 → 70 Hz | — | — |
| Modo de Operación | Continuo | — | — |

### B) Condiciones Ambientales, Límites de Operación e Instalación

| Parámetro | Valor | Norma |
|-----------|-------|-------|
| Normas para EUROPA | IEC61010-1, IEC60255-6, IEC60947-1 | LVD & EMC |
| Normas para USA | UL (pendiente), Dispositivos Auxiliares | UL508 |
| Aprobación Europea | CE (pendiente), Dispositivos de Bajo Voltaje | IEC60947-1 |
| Temperatura Ambiental (Operación) | -5 °C a 55 °C (23 °F a 131 °F) | — |
| Temperatura Ambiental (Almacenaje) | -10 °C a +70 °C (14 °F a 158 °F) | — |
| Humedad Relativa Máxima | 85% R.H. | — |
| Resistencia a Vibraciones | Clase 1, Amplitud <0.035mm @ 1G 10Hz < f < 150Hz | IEC 60255-21-1 |
| Protección a Objetos/Agua | IP20, protegido contra objetos >12.5mm, sin protección contra agua | IEC 60529 |
| Nivel de Contaminación | Grado 3 | IEC 60255-5 |
| Protección Exceso Voltaje | Categoría III | IEC 60255-5 |
| Voltaje de Aislamiento Nominal | 500V | Según UL |
| Prueba de Impulso | 5 KV | IEC 60255-5 |
| Prueba Dieléctrica | 2.5 KV 50/60 Hz @ 1 min | UL 508 |
| Grado de Protección al Fuego | V-0 | UL-94 |
| Material de la Carcasa | Polímeros: LEXAN, ABS, VYDYNE | — |
| Posiciones de Montaje | Sin Restricciones | — |
| Tipos de Montaje | Riel DIN Simétrico / Superficie Plana, Tornillo 3/16" x 1/2" | IEC 715, DIN 43880, Tipo NEMA |
| Tipo de Tornillo de Borneras | Plano M3 | — |
| Torque de Apretado de Borneras | 5.1 Kg-cm / 4.4 lb-in | — |
| Cableado de Borneras | 10-18 AWG | — |
| Cableado en Sensor de Corriente | Ø ≤ 11mm, AWG 4 | — |
| Medidas | 92 x 91 x 96 mm (L x A x H) | — |
| Peso | 494 g (1.09 lb) | — |

### C) Características de Control

| Parámetro | Valor | Norma |
|-----------|-------|-------|
| Capacidad de los Contactos | B300 Pilot Duty — 1A @240 VAC, 0.5A @480 VAC | UL 508 Sección 139.1 |
| Expectativa de Vida Eléctrica | 100,000 Operaciones | — |
| Expectativa de Vida Mecánica | 10,000,000 Operaciones | — |
| Categoría de Uso | AC-15, Capacidad para Cargas 72 VA | IEC 60947-5-1 |

### D) Ajustes de Rango, Mediciones

| Parámetro | Modelo 208 | Modelo 400 | Modelo 480 |
|-----------|-----------|-----------|-----------|
| Rango de Medición de Voltaje (Um) | 0 → 312 VAC ±2% | 0 → 532 VAC ±2% | 0 → 672 VAC ±2% |
| Rango de Medición de Corriente — Modelo 04 | 1.5 → 40 A, ±2% | — | — |
| Rango de Medición de Corriente — Modelo 12 | 0.3 → 125 A, ±2% | — | — |
| Rango de Medición de Corriente — Modelo 32 | 1 → 320 A, ±2% | — | — |
| Rango de Medición de Corriente — Modelo 80 | 2.5 → 800 A, ±2% | — | — |
| Rango de Frecuencia | 45.0 → 70.0 Hz | 1% tolerancia |
| Factor Potencia Instantáneo | 0.00 → 1.00 | 8% tolerancia |
| Potencia Aparente Instantánea | 0.0 → 999.9 kVA | 4% tolerancia |
| Potencia Real Instantánea | 0.0 → 999.9 kW | 4% tolerancia |
| Consumo de Energía | 0 → 999999 kW/H | 4% tolerancia |
| Horas de trabajo acumuladas del motor | 0 → 999999 H | 1% tolerancia |

### E) Funciones y Algoritmos de Protección

| Función | Modelo 208 | Modelo 400 | Modelo 480 |
|---------|-----------|-----------|-----------|
| Bajo Voltaje UV (@Imotor=0 o OC) | 165 → 225 V | 320 → 380 V | 360 → 480 V | Ajustable |
| Sobre Voltaje OV (@Imotor=0 o OC) | 215 → 270 V | 420 → 480 V | 480 → 580 V | Ajustable |
| Umbral Histéresis de Voltaje | 6 VAC | 10 VAC | 12 VAC | — |
| Desbalance de Voltaje (VUB) | 2% → 10% | — | — | Ajustable |
| Pérdida de Fase de Voltaje (VSP) | IN VUB >33%, OUT VUB <28% | — |
| Frecuencia Nominal | 50 ó 60 Hz | — | Ajustable |
| Variación de Frecuencia | 2% → 10% | — | Ajustable |
| Fase Invertida (PR) | Secuencia ABC Normal, Secuencia CBA Invertida |
| Temporizado a la Desconexión por Fase Invertida | <1 seg |
| Temporizado a la Desconexión por otras Fallas de Voltaje (TD) | 1 → 30 seg | Ajustable |
| Temporizado a la Conexión (TC) | 0 → 600 seg | Ajustable |
| Temporizado a la Desconexión por TD por VSP | 3 seg |
| Modo de Rearme | Automático / Manual | Selección Usuario |

#### Protección de Corriente

| Función | Modelo 04 | Modelo 12 | Modelo 32 | Modelo 80 |
|---------|----------|----------|----------|----------|
| Ajuste Corriente Nominal | 1.5 → 4 A | 3.5 → 12.5 A | 10 → 32 A | 25 → 80 A |
| Ajuste Nivel Sobrecarga (OL) | 5% → 50% | — | Ajustable |
| Temporizado conexión por sobrecarga (OC) | 10 a 60 Minutos | Ajustable |
| Clase Térmica | 10 | — |
| Ajuste Dinámico Modelo del Motor (Curva Fría/Caliente) | Clase Térmica variable 1 → 1/3 de la clase 10 según nivel de carga | IEC 60255-8 |
| Desbalance de Corriente (CUB) | CUB >48% |
| Pérdida de fase por Corriente (CSP) | CUB >60% |
| Detección Rotor Bloqueado Acelerado (LR) | CONTINUO |
| Temporizado Desconexión por CSP | 3 seg |
| Temporizado Desconexión por CUB | 4 seg |
| Subcarga | SI / NO | Selección Usuario |
| Ajuste Nivel Subcarga (UC) | 30% → 90% | Ajustable |
| Temporizado Desconexión por Subcarga (UC) | 5 → 600 seg | Ajustable |
| Temporizado Conexión por Subcarga (UC) | 2 → 500 min | Ajustable |
| Detección de Tercera (3ª) Falla | SI / NO | Selección Usuario |
| Desconexión permanente por Tercera Falla | 3 fallas en menos de 30 min | IEEE Std C37.112-1996 |

#### Protección Adicional para Bombas Sumergibles

| Función | Valor |
|---------|-------|
| Máximo número de arranques por hora | SI / NO — Selección usuario |
| Número de arranques por hora | Máximo automático hasta 12 según HP; Mínimo seleccionable por usuario | NEMA MG10 AJUSTABLE |
| Tiempo mínimo entre arranques | 1 a 10 Min. | NEMA MG10 |

### F) Comunicación

| Parámetro | Valor |
|-----------|-------|
| Protocolo de Comunicación | MODBUS RTU @ 9600 8N1 |
| Puerto de Comunicación | GIO PORT (*) |
| Rango de Direcciones | 1 → 127 |
| Histórico de Fallas | Reporte de 80 últimas fallas (Tipo, Valor, Hora, Fecha y Tiempo de Duración) |
| Retención de parámetros ante falla | Ajustes de voltaje, corriente, modo de rearme |
| Bloqueo de Parámetros | 0000 Libre — 0001 → 9999 Bloqueado |

(*) Se requiere GIO PLUG para comunicación a través de GIO Port. El GIO PLUG se suministra por separado.

### G) Compatibilidad Electromagnética — Ambiente Industrial Severo

| Parámetro | Norma |
|-----------|-------|
| Descarga Electrostática | IEC 61000-4-2 |
| Inmunidad a Ruido Eléctrico Radiado | IEC 61000-4-3 |
| Transientes Rápidas | IEC 61000-4-4 |
| Picos de Alta Energía | IEC 61000-4-5 |
| Perturbaciones Conducidas | IEC 61000-4-6 |
| Campos Magnéticos | IEC 61000-4-8 |
| Reducciones e Interrupciones de Voltaje | IEC 61000-4-11 |
| Armónicos | IEC 61000-4-13 |
| Fluctuaciones de Voltaje | IEC 61000-4-14 |
| Desbalance Trifásico | IEC 61000-4-27 |
| Variaciones de Frecuencia | IEC 61000-4-28 |

---

## 11. Curva Fría — Curva Caliente

La curva térmica del GSPT opera en función de I_carga / I_nom. El rango de Tiempo de Disparo varía de 1 a 10,000 segundos según la relación de corriente.

### Arranques Permitidos por Hora (Sph)

| HP | Sph máximo (automático) |
|----|------------------------|
| 1 | 12 |
| 1.5 | 12 |
| 2 | 12 |
| 3 | 12 |
| 5 | 7 |
| 7.5 | 7 |
| 10 | 5 |
| 15 | 5 |
| 20 | 4 |
| 25 | 4 |
| 30 | 4 |
| 40 | 3 |
| 50 | 3 |
| 60 | 3 |
| 75 | 3 |
| 100 | 3 |
| 125 | 2 |
| 150 | 2 |
| 200 | 2 |
| 250 | 2 |

---

## 12. Cómo Ordenar GSPT

```
GSPT — [Voltaje] — [Corriente] — [Opciones] — [Idioma]

Voltaje:   208 = 208/220/240 VAC
           480 = 440/480 VAC

Corriente: 04 = 1-4 A
           12 = 3.5-12.5 A
           32 = 10-32 A
           80 = 25-80 A

Opciones:  S = Estándar
           R = Con medición de temperatura

Idioma:    S = Español
           E = Inglés
```

---

## Diagramas

### Diagrama 1 — Diagrama Básico de Instalación (Página 2)

Diagrama trifásico (trifiliar) de instalación básica del GSPT para bomba sumergible.

**Componentes del circuito:**
- Alimentación trifásica: L1, L2, L3 (R, S, T)
- Interruptor termomagnético
- Fusibles opcionales 5A, 600V
- GSPT Subtronic (terminales L1, L2, L3 en la parte superior; terminales 95, 96, 97, 98 para señalización y control)
- GIO Port (puerto de comunicación)
- Contactor (bobina controlada por contactos 97-98 del GSPT)
- Motor trifásico de la bomba sumergible
- Alarma (conectada a contactos 95-96)
- Luz piloto de alarma opcional

**Secuencia de conexión:**
1. Red trifásica → Interruptor → Fusibles opcionales → Terminales L1/L2/L3 del GSPT
2. El GSPT detecta parámetros eléctricos a través de los sensores de corriente internos
3. Contactos 97-98 controlan la bobina del Contactor
4. El Contactor alimenta el motor de la bomba sumergible
5. Contactos 95-96 activan alarma en caso de falla

**Clasificación del diagrama:** Trifiliar (trifásico)
**Ubicación en PDF original:** Página 2

### Diagrama 2 — Guía Rápida de Programación — Mapa de Pantallas (Página 4)

Diagrama de navegación de pantallas del software v1.12. No es un diagrama de conexión eléctrica sino un mapa de flujo de programación del equipo. Se incluye como referencia para configuración.

---

## Información de Contacto

Buzzom ACSA 0158, P.O. Box 28537, Miami, FL, 33102, USA.  
Avenida El Buen Pastor cruce con calle Vargas, Edificio Alba, Piso 1, Local 1-A, Boleíta Norte, Caracas — Venezuela, Zona Postal 1070.  
Telf.: ++(58 212) 237.07.11 (Master) / 34.77 / 11.51  
Fax: ++(58 212) 235.24.97  
e-mail: genteven@genteca.com.ve — www.genteca.com.ve
