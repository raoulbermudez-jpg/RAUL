# DELTA DE COPY — EMPAQUES GSM-MB / GSM-RB / GSM-RF
**Documento de trabajo para Ozwaldo — v2**
**Fecha:** 2026-04-19
**Preparado por:** Equipo técnico y de marca — Genteca
**Aplica a:** Empaques GLA (tiro + retiro) de los tres modelos. Diferencias entre modelos: color y aplicación únicamente. El copy de la función térmica es idéntico para los tres.
**Cambios respecto a v1:** Flags #1 y #2 respondidos por I&D. Copy de CARACTERÍSTICAS y FUNCIONAMIENTO actualizado a versión final (Flag #1 completo; Flag #2 con asterisco pendiente de confirmación de impresión).

---

## 1. RESUMEN EJECUTIVO

Se actualiza el empaque de los modelos GSM-MB, GSM-RB y GSM-RF para comunicar la nueva función de protección térmica incorporada en las versiones V10/V9/V13 (27/03/2026).

**Estado de aprobación del copy:**
- El copy del TIRO está aprobado. ✅
- El copy de CARACTERÍSTICAS está aprobado. ✅
- El copy de FUNCIONAMIENTO está casi cerrado: la descripción del mecanismo es definitiva; la mención al rearme automático lleva (*) hasta confirmación final de I&D antes de imprimir.
- El disclaimer de INFORMACIÓN DE SEGURIDAD está aprobado. ✅

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
> - ⚠️ CONDICIONAL — requiere confirmación antes de imprimir
> - ❌ RECHAZADO — no usar bajo ninguna circunstancia

---

### SECCIÓN A: TIRO — Cintilla / Insignia principal

| Campo | Contenido |
|---|---|
| **Texto actual (eliminar)** | NUEVO / AHORA CON / PROTECCIÓN POR / CALENTAMIENTO |
| **Versión final aprobada** | NUEVO / AHORA CON / PROTECCIÓN / TÉRMICA |
| **Flag** | ✅ APROBADO sin condiciones |

**Justificación:** Más breve, más seguro, visualmente más limpio para el espacio disponible (~30 caracteres por línea). La precisión técnica del mecanismo se desarrolla en el retiro.

---

### SECCIÓN B: RETIRO — CARACTERÍSTICAS (bullet de función térmica)

| Campo | Contenido |
|---|---|
| **Texto actual (eliminar)** | "Nueva protección por sobrecalentamiento que protege la integridad de la instalación eléctrica." |
| **Versión final aprobada** | Ver copy propuesto abajo |
| **Flag** | ✅ APROBADO — basado en confirmación I&D Flag #1 |

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
| **Versión final** | Ver copy propuesto abajo |
| **Flag** | ✅ Mecanismo APROBADO. ⚠️ Línea de rearme CONDICIONAL — confirmada como probable pero requiere validación final de I&D antes de imprimir |

**Copy propuesto — FUNCIONAMIENTO:**

```
Si el protector detecta temperatura elevada — por corriente excesiva o por calor proveniente de bornes con conexión deficiente — abre el circuito para prevenir daños por calor.
El dispositivo rearma automáticamente al descender la temperatura. (*)

(*) Pendiente de confirmación final por I&D antes de imprimir.
```

**Nota sobre la oración de LEDs:** La descripción del estado de LEDs ("Ambos rojos fijos + LED verde intermitente = Alta temperatura") es una indicación de estado y puede mantenerse sin cambio si corresponde al comportamiento real del producto. No es objeto de este delta.

---

## 3. FLAGS DE I&D — ESTADO ACTUALIZADO

### FLAG #1 — Posición y alcance del sensor NTC ✅ RESUELTO

**Respuesta confirmada por owner (I&D):**
- El sensor NTC está ubicado junto al relé de potencia.
- Mecanismo primario: corriente excesiva → calienta el relé → NTC detecta ese calor → desconecta.
- Mecanismo secundario (confirmado): bornes flojos, con restos de aislante o alta impedancia → generan calor → ese calor se conduce al protector → NTC también lo detecta.
- El sensor NO "monitorea los bornes" directamente — actúa por temperatura, venga de donde venga.

**Impacto en copy:** Las menciones a "bornes de conexión" y "conexión deficiente" están habilitadas, siempre que el wording deje claro que el sensor actúa por calor (no por monitoreo directo de los bornes). El copy propuesto en este documento respeta esa condición.

---

### FLAG #2 — Comportamiento de rearme ⚠️ PARCIALMENTE RESUELTO

**Respuesta del owner:** Probablemente automático al bajar la temperatura, pero no confirmado al 100%.

**Decisión:** Incluir la información en el copy marcada con (*). Ozwaldo debe dejar un placeholder claro en el archivo de trabajo. Keiddys confirma con I&D antes de aprobar para imprenta.

**Acción pendiente:** Keiddys confirma con I&D: ¿el rearme es automático al bajar la temperatura, o requiere ciclo de energía (apagar/encender)?

---

## 4. NOTA PARA OZWALDO

### Copy final — listo para implementar

**TIRO:**
```
NUEVO
AHORA CON
PROTECCIÓN
TÉRMICA
```
✅ Definitivo — sin condiciones.

---

**CARACTERÍSTICAS (reemplazar el bullet actual sobre protección térmica):**
```
• Sensor térmico ubicado junto al relé de potencia: detecta el calor generado por corriente excesiva y abre el circuito antes de que el calor dañe el relé o la tarjeta electrónica.
• Protección adicional: si los bornes de conexión presentan falso contacto, mala conexión o restos de aislante, el calor generado en esos puntos también activa el sensor y desconecta la carga.
```
✅ Definitivo — basado en confirmación I&D.

---

**FUNCIONAMIENTO (reemplazar la oración rechazada y agregar línea de rearme):**
```
Si el protector detecta temperatura elevada — por corriente excesiva o por calor proveniente de bornes con conexión deficiente — abre el circuito para prevenir daños por calor.
El dispositivo rearma automáticamente al descender la temperatura. (*)
```
✅ Primera oración: definitiva.
⚠️ Segunda oración (rearme automático): incluir con (*) — **dejar placeholder** hasta confirmación I&D.

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

*v2 emitida con Flags #1 y #2 respondidos. Única pendiente antes de aprobar para imprenta: confirmación de I&D sobre rearme automático (Flag #2). Una vez confirmado, este documento puede cerrarse como definitivo.*
