```markdown
---
title: "GI+ Guía de Instalación"
type: Technical
source: "Guia de Instalacion GI+.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GI+"
date_processed: "2026-05-09"
---

# GI+ GUÍA DE INSTALACIÓN

## ALERTA

Solo personal técnico calificado con conocimientos en relés (relevadores) de protección y la carga asociada debería realizar la instalación, arranque y mantenimiento del sistema. Hacer caso omiso podría resultar en lesiones a personas y/o daños a los equipos conectados.

## GI+ PARTES Y PIEZAS

### Vista Frontal

1. **Indicadores Luminosos (LEDs)**
   - Luz Fija - CONECTADO (ON)
   - Luz Intermitente - TEMPORIZADO (TC) a la Conexión
   - LED Verde
   - LED Rojo Luz Fija - FALLA

2. **Pantalla LCD**

3. **Botón Pulsador de Rearme (Arranque)**

4. **Botones Pulsadores para Ajustes**

5. **Botón Pulsador para Selección**

6. **Frontal Insertable para Flush Mounting**

7. **Gancho Sujetador para Frontal**

### Vista Posterior

8. **Ranura posterior para montaje en Riel simétrico**

9. **Sujetador Insertable para Montaje en Superficie Plana**

10. **Gancho de Retención para montaje en Riel simétrico**

11. **Terminales Enchufables**

12. **GIO PORT (Puerto de Comunicación)**

13. **Cubierta plástica protectora del GIO PORT**

## GI+ DIMENSIONES GENERALES

- **Largo:** 105 mm (5/32")
- **Alto:** 124 mm
- **Profundidad:** 86 mm
- **Guía para Superficie Plana:** 85 mm
- **Altura adicional:** 8.99 mm / 09 mm

## GI+ ESPECIFICACIONES TÉCNICAS

### A) Fuente de Poder

| Parámetro | Especificación |
|-----------|----------------|
| Voltaje de Operación, Ue | 120 / 208-220 / 440-480 V~ |
| Límite de Operación de Voltaje, Ue | 72-168 / 145-312 / 264-672 V~ |
| Consumo Promedio, In | 44 mA |
| Frecuencia Nominal Fn | 50/60 Hz |
| Frecuencia de Operación | 42-70 Hz |
| Modo de Operación | Continuo |

### B) Condiciones Ambientales, Límites de Operación e Instalación

| Parámetro | Especificación | Norma |
|-----------|----------------|-------|
| Temperatura Ambiental (Operación) | -5 °C a 55 °C (23 °F a 131 °F) | |
| Temperatura Ambiental (Almacenaje) | -10 °C a +70 °C (14 °F a 158 °F) | |
| Humedad Relativa Máxima | 85% R.H. | |
| Protección a Objetos/Agua | IP20, Protegido contra objetos > 12.5mm, ninguna protección contra agua | IEC 60529 |
| Nivel de Contaminación | Grado 3 | IEC 60255-5 |
| Protección contra Exceso de Voltaje | Categoría III, 4KV | IEC 60255-5 |
| Voltaje de Aislamiento Nominal | 500V | UL IEC 60255-5 |
| Prueba de Impulso | 5 KV | IEC 60255-5 |
| Prueba Dieléctrica | 2.5 KV 50/60 Hz@1min | UL 508 |
| Grado de Protección al Fuego de la Carcaza | 5 VA | UL-94 |
| Material de la Carcaza | Polímeros: LEXAN 500R, ABS, Nylon | |
| Tipos de Montaje | Riel DIN Simétrico, Superficie Plana (tornillo 3/16" x 1/2"), Empotrable (Flush Mounting) | IEC 715, DIN 43880, Tipo NEMA |
| Tipo de Tornillo de Borneras | Plano M2.5 | |
| Torque de Apretado de Borneras | 5.2 Kg-cm (4.5 lb-in) | |
| Cableado de Borneras | AWG 30-12, L=7-8mm (5/16) | |
| Medidas | 105 x 90 x 68 (L x A x H) mm | |
| Peso | 0.23 Kg (0.506 lb) | |

### C) Características de Control

| Parámetro | Especificación | Norma |
|-----------|----------------|-------|
| Capacidad de los Contactos | 3 A@240 V~, 1.5 A@480 V~ | UL 508, Pilot Duty Sección 139.1 |
| Expectativa de vida Eléctrica | 100,000 Operaciones | |
| Expectativa de vida Mecánica | 10,000,000 Operaciones | |

### D) Ajustes de Rango, Mediciones

| Parámetro | Especificación (por Modelo de Voltaje) | Precisión |
|-----------|----------------------------------------|-----------|
| Rango de Medición de Voltaje, Um | 0-168 V~ (120V) / 0-300 V~ (208V) / 0-672 V~ (480V) | ±2% |
| Rango de Frecuencia | 45.0-70.0 Hz | ±1% |

### E) Algoritmos y Funciones de Protección

| Función | Rango (por Modelo de Voltaje) | Ajustabilidad |
|---------|-------------------------------|---------------|
| Bajo Voltaje (UV) | 95-115V (120V) / 165-225V (208V) / 350-460V (480V) | Ajustable |
| Sobre Voltaje (OV) | 125-145V (120V) / 215-270V (208V) / 460-580V (480V) | Ajustable |
| Umbral de Histéresis en el Voltaje | 3V (120V) / 6V (208V) / 12V (480V) | |
| Desbalance de Voltaje (VUB) | 2%-10% | Ajustable |
| Pérdida de Fase de Voltaje (VSP) | INV VUB > 33%, OUT VUB < 28% | |
| Frecuencia Nominal | 50 ó 60 Hz | Ajustable |
| Variación de Frecuencia (FREC) | 2%-10% | Ajustable |
| Fase Invertida (PR) | Secuencia ABC normal, secuencia CBA invertida | |
| Temporizado a la Desconexión por Fase Invertida | < 1 s | |
| Temporizado a la Desconexión por Otras Fallas de Voltaje (TD) | 1-30 s | Ajustable |
| Temporizado a la Conexión (TC) | 0-600 s | Ajustable |
| Modo de Rearme | Automático/Manual | Selección del Usuario |

### F) Comunicaciones y Otras Funciones