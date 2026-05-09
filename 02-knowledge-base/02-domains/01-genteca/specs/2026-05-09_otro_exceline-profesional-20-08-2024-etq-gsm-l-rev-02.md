```markdown
---
title: "GSM-L120 / GSM-L220 - Supervisor de Voltaje Bajo Monofásico"
type: Technical
source: "20-08-2024_ETQ_GSM-L - Rev-02.pdf"
product_line: "Exceline Profesional"
document_type: "hoja-especificaciones"
product_code: "GSM-L120, GSM-L220"
date_processed: "2026-05-09"
---

# GSM-L - Supervisor de Voltaje Bajo Monofásico

## Modelos

- **GSM-L120**: Supervisor de voltaje bajo monofásico 120V
- **GSM-L220**: Supervisor de voltaje bajo monofásico 220V

## Especificaciones Técnicas

### Capacidad de Contactos
- **16 A / 1.5 HP @ 120V~** (GSM-L120)
- **8 A / 1.5 HP @ 220V** (GSM-L220)

### Tipo de Relé
- SPDT (Single Pole Double Throw)

## Esquema de Conexión

### Bornes de Conexión

#### GSM-L120
| Borne | Función |
|-------|---------|
| 5 | Alimentación línea |
| 6 | Contacto Común (Voltaje Normal) |
| 7 | Contacto Común / Alimentación retorno |
| 3, 4 | Salida de relé |

#### GSM-L220
| Borne | Función |
|-------|---------|
| 5 | Alimentación línea |
| 6 | Contacto Común (Voltaje Normal) |
| 7 | Contacto Común / Alimentación retorno |
| 3, 4 | Salida de relé |

### Configuración de Contactos
- **Bornes 5 y 3, y 6 y 4**: Alimentación de relé - Contactos de conexión
- **Borne 7**: Contacto Común
- **Bornes 6 y 7 conectados**: Voltaje Normal
- **Bornes 5 y 7 desconectados**: Funcionamiento en voltaje bajo

## Rangos de Operación

### GSM-L120 (120V)
| Condición | Rango (V) |
|-----------|-----------|
| Voltaje Bajo | 50 - 125 |
| Voltaje Normal | 130 - 140 |
| Voltaje Alto | 145 - 250 |
| Temporizado | 5 - 300 |

### GSM-L220 (220V)
| Condición | Rango (V) |
|-----------|-----------|
| Voltaje Bajo | 50 - 235 |
| Voltaje Normal | 245 - 255 |
| Voltaje Alto | 265+ |
| Temporizado | 5 - 300 |

## Funcionamiento

- **Relé tipo SPDT**: Proporciona cambio de contacto normalmente abierto/cerrado
- **Protección de voltaje bajo**: Supervisa el voltaje de línea y actúa cuando este desciende por debajo del umbral programado
- **Temporización ajustable**: Permite retardos de 5 a 300 unidades según configuración
```