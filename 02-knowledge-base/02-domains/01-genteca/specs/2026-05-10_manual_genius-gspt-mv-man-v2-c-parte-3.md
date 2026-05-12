---
title: "GSPT-MV Manual de Instalación - Características Sensor Temperatura y Comunicaciones"
type: Technical
source: "GSPT-MV_MAN-V2_C.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GSPT-MV"
version_status: "vigente"
date_processed: "2026-05-10"
---

# Características Sensor Temperatura

## Compensación y Ajustes

| Parámetro | Especificación | Notas |
|-----------|----------------|-------|
| e.34 | Compensación por temperatura | SI/NO Selección usuario |
| e.35 | Ajuste Temperatura Inicial Ti | 20→150 °C Ajustable |
| e.36 | Ajuste Temperatura Máxima Tm | 50→200 °C Ajustable |
| e.37 | Sensor (Tipo) | Platino 100 Ohm, 3 Cables (PT100) Compatible con sensores de 2 y 4 cables |
| e.38 | Temperatura de desconexión | Valor Tm ajustado |
| e.39 | Temperatura de conexión | (Tm - Ti) /6 + Mi |
| e.40 | Máximo número de arranques por hora | SI/NO Selección usuario |
| e.41 | Número de arranques por hora | Máximo automático, hasta 12 según HP; Mínimo seleccionable por usuario AJUSTABLE |
| e.42 | Tiempo mínimo entre arranques | 1 a 10 Min. NEMA MG10 |

## Histórico de Fallas

- Reporte de 80 últimas fallas (Datos de Tipo Falla, Valor, Hora, Fecha y Tiempo de Duración)
- Retención de parámetros configurados cuando ocurrieron las fallas: Ajustes de voltaje, Ajustes de corrientes, control de temperatura, modo de rearme

## Bloqueo de Parámetros

| Estado | Rango |
|--------|-------|
| Libre | 0000 |
| Bloqueado | 0001 > 9999 |

# Protección Adicional para Bombas

Se requiere GIO PLUG para la comunicación a través de GIO Port. El GIO PLUG se suministra por separado.

# Compatibilidad Electromagnética para Ambiente Industrial Severo

## Estándares de Inmunidad y Emisiones

| e.ref | Característica | Norma |
|-------|---|---|
| 9.1 | Descarga Electrostática | IEC 61000-4-2 |
| 9.2 | Inmunidad a Ruido Eléctrico Radiado | IEC 61000-4-3 |
| 9.3 | Transientes Rápidas | IEC 61000-4-4 |
| 9.4 | Picos de Alta Energía | IEC 61000-4-5 |
| 9.5 | Perturbaciones Conducidas | IEC 61000-4-6 |
| 9.6 | Campos Magnéticos | IEC 61000-4-8 |
| 9.7 | DI , DOT | IEC 61000-4-11 |
| 9.8 | Armónicos | IEC 61000-4-13 |
| 9.9 | Fluctuaciones de Voltaje | IEC 61000-4-14 |
| 9.10 | Desbalance Trifásico | IEC 61000-4-27 |
| 9.11 | Variaciones de Frecuencia | IEC 61000-4-28 |

# Comunicaciones y Funciones Especiales

| Parámetro | Especificación | Referencia |
|-----------|---|---|
| f.1 | Protocolo de Comunicación | MODBUS RTU @ 9600 8N1 |
| f.2 | Puerto de Comunicación | Puerto GIO PORT (*) |
| f.3 | Rango de Direcciones | 1 > 127 |

(*) Se requiere GIO PLUG para la comunicación a través de GIO Port. El GIO PLUG se suministra por separado.

# Curvas de Disparo GSPT-MV

El producto cuenta con dos curvas de disparo:
- **Curva Fría**
- **Curva Caliente**

El tiempo de disparo varía en función de la relación I carga / I nom (Corriente de carga / Corriente nominal), donde I nom es el valor de corriente calibrada por el usuario en el GSPT-MV, equivalente a la corriente del motor con su máxima carga FLA tal como se muestra en los ajustes del producto.

# Números Permitidos de Arranques por Hora

Cuando el usuario selecciona el límite automático de máximo número de arranques por hora, el GSPT-MV predispone valores de acuerdo al motor instalado:

- **HP**: Potencia nominal del motor instalado
- **Sph**: Cantidad máxima de arranques permitidos por hora

Esta función se provee de acuerdo a recomendaciones del estándar NEMA MG10.

---

**NOTA**: Las especificaciones y descripciones mostradas en este documento están sujetas a cambio sin previo aviso.
