```markdown
---
title: "Etiquetas con Toroide v5"
type: Technical
source: "Etiquetas con toroide v5.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "N/A"
date_processed: "2026-05-09"
---

# Etiquetas con Toroide

## Configuración de Circuitos

### Entrada Digital
- Opción de Temperatura

### Salidas y Relés

#### Circuito de Control
- **Relé de Control (Control Relay)**
- **Relé Auxiliar (Aux Relay)**

### Conexiones de Toroide Externo

El sistema permite el uso de **GIO PLUG (Opcional)** para:
- Comunicación serial con dispositivos X1
- Comunicación serie con otros dispositivos

### Estados de Funcionamiento

| Estado | Condición | X1 | H1 |
|--------|-----------|----|----|
| Normal | Antes de circuitos de arranque | Conectado | Desconectado |
| Disparo (Tripped) | Activado | Desconectado | Conectado |

### Conexión de Toroide en Disparo
- **X1**: Abierto (Open)
- **H1**: Abierto (Open)
- Estado: Conectado (Connected)

## Notas
- Opcional: GIO PLUG para comunicación externa
- Compatible con circuitos de arranque de línea (line starter circuits)
```