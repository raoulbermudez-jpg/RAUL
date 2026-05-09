---
title: "GST-RM Manual de Instalación"
type: Technical
source: "GST-RM_MAN_R_V1.pdf"
product_line: "Exceline Profesional"
document_type: "manual"
product_code: "GST-RM"
date_processed: "2026-05-09"
---

# GST-RM Manual de Instalación

## Paso 1: Desconexión de energía
Desconecte el breaker antes de iniciar el trabajo eléctrico para evitar accidentes.

## Paso 2: Instalación eléctrica del producto

### Conexión de cables de alimentación
1. Identifique la fase 1 (L1), fase 2 (L2) y fase 3 (L3) de la red eléctrica a supervisar
2. Conecte estas fases al supervisor GST-RM y a la entrada del contactor

### Ajuste de perilla de voltaje
Ajuste la perilla de voltaje bajo de acuerdo a los requerimientos de su instalación. En caso de no tenerlos, ajuste la perilla en el valor recomendado dentro del rango sugerido (300-500).

**Nota importante:** Verifique que el calibre de los cables que van hacia el contactor sea el adecuado según la carga que maneja el motor.

## Diagrama de conexión estándar

| Terminal | Descripción |
|----------|-------------|
| 98 | Normalmente abierto (NA) |
| 95 | Común (C) |
| 96 | Normalmente cerrado (NC) |
| A1 | Bobina contactor |
| A2 | Bobina contactor |
| L1 | Fase L1 |
| L2 | Fase L2 |
| L3 | Fase L3 |

**Conexión de extremos:**
- El extremo A2 se conecta con L1
- El terminal 95 se conecta con L2
- El terminal 96 se conecta con L3

## Indicadores luminosos

### Indicador VERDE - Voltaje Normal
- **Conectado Fijo:** Voltaje normal (390-410V)
- **Tiempo de espera Intermitente:** Equipo en ciclo de espera

### Indicador ROJO - Falla de voltaje
- **Sobre voltaje Fijo:** Voltaje superior al rango normal
- **Bajo voltaje Intermitente:** Voltaje inferior al rango normal
- **Pérdida de fase Fijo:** Una o más fases ausentes
- **Fase invertida Intermitente:** Secuencia de fases incorrecta
- **Desbalance Pulsante:** Desbalance entre fases
- **Falla de frecuencia Pulsante:** Frecuencia fuera de rango

## Rangos de operación
- **Normal:** 98-95 conectado
- **Falla:** 99-68, 99-55 abierto
- **Desconexión:** 0.5-1.0 segundos
- **Conexión:** 60 segundos

## Paso 3: Verificación final
Reconecte la energía eléctrica y verifique el funcionamiento del GST-RM y del equipo protegido.

---

**Especificaciones del documento:**
- Tamaño: 260 mm (ancho) × 90 mm (alto)
- Versión: V1
- Fecha: 30/08/23
- Supervisor: Sergio Sierra
- Diseñador: Oswaldo Gutiérrez