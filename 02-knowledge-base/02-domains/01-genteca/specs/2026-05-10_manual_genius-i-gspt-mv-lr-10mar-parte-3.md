---
title: "GSPT-MV - Manual de Instalación"
type: Technical
source: "I_GSPT-MV - LR 10MAR.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GSPT-MV"
version_status: "vigente"
date_processed: "2026-05-10"
---

# GSPT-MV - Manual de Instalación

## Características Sensor Temperatura

| Parámetro | Rango/Especificación | Notas |
|-----------|----------------------|-------|
| e.34 - Compensación por temperatura | SI/NO | Selección usuario |
| e.35 - Ajuste Temperatura Inicial Ti | 20—150 °C | Ajustable |
| e.36 - Ajuste Temperatura Máxima Tm | 50—200 °C | Ajustable |
| e.37 - Sensor (Tipo) | Platino 100 Ohm, 3 Cables (PT100) | Compatible con sensores de 2 y 4 cables. Protección adicional para bomba |
| e.38 - Temperatura de desconexión | Valor Tm ajustado | — |
| e.39 - Temperatura de conexión | (Tm - Ti) /6+Ti | — |
| e.40 - Máximo número de arranques por hora | SI/NO | Selección usuario |
| e.41 - Número de arranques por hora | Máximo automático, hasta 12 según HP; Mínimo seleccionable por usuario | NEMA MG10. AJUSTABLE |
| e.42 - Tiempo mínimo entre arranques | 1210 Min. | NEMA MG10 |

## F) Comunicaciones y Funciones Especiales

| Parámetro | Especificación | Referencia |
|-----------|----------------|-----------|
| f.1 - Protocolo de Comunicación | MODBUS RTU @ 9600 8N1 | Ver Manual Usuario |
| f.2 - Puerto de Comunicación | GIO PORT (*) | Usuario |
| f.3 - Rango de Direcciones | 1—127 | — |
| f.4 - Histórico de Fallas | Reporte de 80 últimas fallas (Datos de Tipo Falla, Valor, Hora, Fecha y Tiempo de Duración) | Ver Manual Usuario |
| f.5 - Retención de parámetros configurados cuando ocurrieron las fallas | Ajustes de voltaje, Ajustes de corrientes, control de temperatura, modo de rearme | Ver Manual Usuario |
| f.6 - Bloqueo de Parámetros | 0000 Libre, 0001—9999 Bloqueado | Usuario |

**Nota:** (*) Se requiere GIO PLUG para la comunicación a través de GIO Port. El GIO PLUG se suministra por separado.

## G) Compatibilidad Electromagnética para Ambiente Industrial Severo, Estándares de Inmunidad y Emisiones

| Parámetro | Estándar |
|-----------|----------|
| g.1 - Descarga Electrostática | IEC 61000-4-2 |
| g.2 - Inmunidad a Ruido Eléctrico Radiado | IEC 61000-4-3 |
| g.3 - Transientes Rápidas | IEC 61000-4-4 |
| g.4 - Picos de Alta Energía | IEC 61000-4-5 |
| g.5 - Perturbaciones Conducidas | IEC 61000-4-6 |
| g.6 - Campos Magnéticos | IEC 61000-4-8 |
| g.7 - Reducciones e Interrupciones de Voltaje | IEC 61000-4-14 |
| g.8 - Armónicos | IEC 61000-4-13 |
| g.9 - Fluctuaciones de Voltaje | IEC 61000-4-14 |
| g.10 - Desbalance Trifásico | IEC 61000-4-27 |
| g.11 - Variaciones de Frecuencia | IEC 61000-4-28 |

## Curvas de Disparo

### Curva Fría y Curva Caliente

Tiempo de Disparo (seg): 1.0, 2.0, 3.0, 4.0, 5.0

I carga / I nom *

**(*) I nom = Valor de corriente calibrada por el usuario en el SUBTIMING GSPT. I nom es lo mismo que la corriente del motor con su máxima carga FLA tal como se muestra en los ajustes del producto.**

## Números Permitidos de Arranques por Hora

Cuando el usuario selecciona el límite automático de máximo número de arranques por hora, el GSPT predispone los siguientes valores, de acuerdo al motor instalado:

- **HP** = Potencia nominal del motor instalado
- **Sph** = Cantidad máxima de arranques permitidos por hora

Esta función se provee de acuerdo a recomendaciones del estándar NEMA MG10.

---

**NOTA:** Las especificaciones y descripciones mostradas en este documento están sujetas a cambio sin previo aviso.

**Código de Documento:** MV-02-0121.0-01-S
