# DELTA DE COPY — EMPAQUES GSM-MB / GSM-RB / GSM-RF
**Documento de trabajo para Ozwaldo — v3**
**Fecha:** 2026-04-19
**Preparado por:** Equipo técnico y de marca — Genteca
**Aplica a:** Empaques GLA (tiro + retiro) de los tres modelos. Diferencias entre modelos: color y aplicación únicamente. El copy de la función térmica es idéntico para los tres.
**Cambios respecto a v2:** Flag #2 (rearme automático) confirmado como definitivo. Eliminados el asterisco (*) y todas las notas condicionales. Copy 100% cerrado y aprobado para imprenta.

---

## 1. RESUMEN EJECUTIVO

Se actualiza el empaque de los modelos GSM-MB, GSM-RB y GSM-RF para comunicar la nueva función de protección térmica incorporada en las versiones V10/V9/V13 (27/03/2026).

**Estado de aprobación del copy:**
- El copy del TIRO está aprobado. ✅
- El copy de CARACTERÍSTICAS está aprobado. ✅
- El copy de FUNCIONAMIENTO está aprobado. ✅
- El disclaimer de INFORMACIÓN DE SEGURIDAD está aprobado. ✅

**Todo el copy está cerrado. No quedan flags abiertos. Listo para implementar en la versión final de diseño.**

**Secciones que cambian:**
- TIRO (frente): Insignia principal — texto de la cintilla
- RETIRO (reverso) — sección CARACTERÍSTICAS: un bullet existente se reemplaza
- RETIRO (reverso) — sección FUNCIONAMIENTO: una oración existente se reemplaza y se agrega una línea nueva
- RETIRO (reverso) — sección INFORMACIÓN DE SEGURIDAD: se agrega o reubica un disclaimer

**Secciones que NO cambian:**
- Todo el resto del empaque (especificaciones, voltaje, amperaje, certificaciones, marca, fotografías, etc.)

---

## 2. TABLA DELTA POR SECCIÓN

> Convención de flags:
> - ✅ APROBADO — copy seguro, puede usarse
> - ❌ RECHAZADO — no usar bajo ninguna circunstancia

---

### SECCIÓN A: TIRO — Cintilla / Insignia principal

| Campo | Contenido |
|---|---|
| **Texto actual (eliminar)** | NUEVO / AHORA CON / PROTECCIÓN POR / CALENTAMIENTO |
| **Versión final aprobada** | NUEVO / AHORA CON / PROTECCIÓN / TÉRMICA |
| **Flag** | ✅ APROBADO |

**Justificación:** Más breve, más seguro, visualmente más limpio para el espacio disponible (~30 caracteres por línea). La precisión técnica del mecanismo se desarrolla en el retiro.

---

### SECCIÓN B: RETIRO — CARACTERÍSTICAS (bullet de función térmica)

| Campo | Contenido |
|---|---|
| **Texto actual (eliminar)** | "Nueva protección por sobrecalentamiento que protege la integridad de la instalación eléctrica." |
| **Versión final aprobada** | Ver copy propuesto abajo |
| **Flag** | ✅ APROBADO |

**Copy propuesto — CARACTERÍSTICAS:**

```
• Sensor térmico ubicado junto al relé de potencia: detecta el calor generado por corriente excesiva y abre el circuito antes de que el calor dañe el relé o la tarjeta electrónica.
• Protección adicional: si los bornes de conexión presentan falso contacto, mala conexión o restos de aislante, el calor generado en esos puntos también activa el sensor y desconecta la carga.
```

**Notas técnicas de soporte (para uso interno — no van al empaque):**
- El sensor detecta calor por mecanismo primario (corriente excesiva → calienta el relé de potencia) y por mecanismo secundario (bornes con alta impedancia por falso contacto → calor conducido hasta el protector).
- El copy NO afirma que el sensor "monitorea los bornes" directamente — dice que el calor generado en los bornes activa el sensor.
- El término "NTC" no aparece en el copy.

**Nota sobre el disclaimer:** La frase "No reemplaza los breakers termomagnéticos de la instalación eléctrica" va en INFORMACIÓN DE SEGURIDAD, no en CARACTERÍSTICAS.

---

### SECCIÓN C: RETIRO — FUNCIONAMIENTO (oración de función térmica)

| Campo | Contenido |
|---|---|
| **Texto actual (eliminar)** | "Si la instalación se calienta por sobrecarga u otra condición, el protector abre el circuito." |
| **Versión final aprobada** | Ver copy propuesto abajo |
| **Flag** | ✅ APROBADO |

**Copy propuesto — FUNCIONAMIENTO:**

```
Si el protector detecta temperatura elevada — por corriente excesiva o por calor proveniente de bornes con conexión deficiente — abre el circuito para prevenir daños por calor.
Al normalizarse la temperatura, el protector reconecta automáticamente.
```

**Fundamento del rearme automático (confirmado):**
- Por física del NTC: al bajar la temperatura, el sensor restaura el circuito de control automáticamente — no requiere intervención del usuario.
- Consistente con el patrón del producto: todos los rearmes son automáticos al normalizar la condición (voltaje, temperatura, etc.).
- La descripción del retiro actual lo respalda: "Tras cualquier falla: reconecta al cumplirse el tiempo de espera ajustado" — aplica también a fallas térmicas.

**Nota sobre la oración de LEDs:** La descripción del estado de LEDs ("Ambos rojos fijos + LED verde intermitente = Alta temperatura") es una indicación de estado y puede mantenerse sin cambio si corresponde al comportamiento real del producto. No es objeto de este delta.

---

## 3. FLAGS DE I&D — ESTADO FINAL

### FLAG #1 — Posición y alcance del sensor NTC ✅ RESUELTO

**Respuesta confirmada por owner (I&D):**
- El sensor NTC está ubicado junto al relé de potencia.
- Mecanismo primario: corriente excesiva → calienta el relé → NTC detecta ese calor → desconecta.
- Mecanismo secundario (confirmado): bornes flojos, con restos de aislante o alta impedancia → generan calor → ese calor se conduce al protector → NTC también lo detecta.
- El sensor NO "monitorea los bornes" directamente — actúa por temperatura, venga de donde venga.

**Impacto en copy:** Las menciones a "bornes de conexión" y "conexión deficiente" están habilitadas. El copy respeta la condición de wording establecida.

---

### FLAG #2 — Comportamiento de rearme ✅ RESUELTO

**Decisión técnica confirmada:** El rearme es AUTOMÁTICO al bajar la temperatura.

**Fundamento:**
1. Por física del NTC: al descender la temperatura, el sensor restaura el circuito de control automáticamente.
2. El retiro actual dice "Tras cualquier falla: reconecta al cumplirse el tiempo de espera ajustado" — aplica también a fallas térmicas.
3. Patrón consistente con el resto del producto: todos los rearmes son automáticos al normalizar la condición.

**Acción:** El asterisco (*) ha sido eliminado. La línea de rearme es definitiva y no requiere validación adicional.

---

## 4. NOTA PARA OZWALDO

### Copy final — TODO definitivo, listo para implementar

**TIRO:**
```
NUEVO
AHORA CON
PROTECCIÓN
TÉRMICA
```
✅ Definitivo.

---

**CARACTERÍSTICAS (reemplazar el bullet actual sobre protección térmica):**
```
• Sensor térmico ubicado junto al relé de potencia: detecta el calor generado por corriente excesiva y abre el circuito antes de que el calor dañe el relé o la tarjeta electrónica.
• Protección adicional: si los bornes de conexión presentan falso contacto, mala conexión o restos de aislante, el calor generado en esos puntos también activa el sensor y desconecta la carga.
```
✅ Definitivo.

---

**FUNCIONAMIENTO (reemplazar la oración rechazada y agregar línea de rearme):**
```
Si el protector detecta temperatura elevada — por corriente excesiva o por calor proveniente de bornes con conexión deficiente — abre el circuito para prevenir daños por calor.
Al normalizarse la temperatura, el protector reconecta automáticamente.
```
✅ Definitivo. Ambas oraciones aprobadas sin condiciones. No quedan placeholders.

---

**INFORMACIÓN DE SEGURIDAD (agregar o reubicar desde CARACTERÍSTICAS):**
```
• No reemplaza los breakers termomagnéticos de la instalación eléctrica.
```
✅ Definitivo.

---

### Qué NO implementar bajo ninguna circunstancia

- ❌ Cualquier mención a "falsos contactos" como promesa de reducción de fallas
- ❌ "protege la integridad de la instalación eléctrica" (el texto actual)
- ❌ "Si la instalación se calienta por sobrecarga u otra condición" (el texto actual de FUNCIONAMIENTO)
- ❌ El término "NTC" en ninguna sección visible al consumidor

---

*v3 emitida con todos los flags resueltos. Copy 100% cerrado y aprobado. Ozwaldo puede proceder directamente a la versión final de diseño para imprenta.*
