# DELTA DE COPY — EMPAQUES GSM-MB / GSM-RB / GSM-RF
**Documento de trabajo para Ozwaldo — v1**
**Fecha:** 2026-04-19
**Preparado por:** Equipo técnico y de marca — Genteca
**Aplica a:** Empaques GLA (tiro + retiro) de los tres modelos. Diferencias entre modelos: color y aplicación únicamente. El copy de la función térmica es idéntico para los tres.

---

## 1. RESUMEN EJECUTIVO

Se actualiza el empaque de los modelos GSM-MB, GSM-RB y GSM-RF para comunicar una nueva función de protección térmica incorporada en las versiones V10/V9/V13 (27/03/2026). El copy actual no refleja esta función o la describe con lenguaje que excede lo técnicamente sustentable.

**Secciones que cambian:**
- TIRO (frente): Insignia principal — texto de la cintilla "NUEVO / AHORA CON..."
- RETIRO (reverso) — sección CARACTERÍSTICAS: un bullet existente se reemplaza
- RETIRO (reverso) — sección FUNCIONAMIENTO: una oración existente se reemplaza

**Secciones que NO cambian:**
- Todo el resto del empaque (especificaciones, voltaje, amperaje, certificaciones, marca, fotografías, etc.)

**Estado de aprobación del copy:**
- Parte del copy está aprobado y puede implementarse ya.
- Dos claims específicos están condicionados a confirmación de I&D (ver Sección 3).
- Ozwaldo puede avanzar con la versión segura (ver Sección 4).

---

## 2. TABLA DELTA POR SECCIÓN

> Convención de flags:
> - ✅ APROBADO — copy seguro, puede usarse
> - ⚠️ CONDICIONAL — requiere confirmación de I&D antes de usar
> - ❌ RECHAZADO — no usar bajo ninguna circunstancia

---

### SECCIÓN A: TIRO — Cintilla / Insignia principal

| Campo | Contenido |
|---|---|
| **Texto actual (eliminar)** | NUEVO / AHORA CON / PROTECCIÓN POR / CALENTAMIENTO |
| **Versión A — Estudio de mercado** | NUEVO / Ahora con / Protección térmica contra / sobrecalentamiento del protector |
| **Flag Vera — Versión A** | ✅ "Protección térmica" APROBADO. ⚠️ "sobrecalentamiento del protector" CONDICIONAL (ver Flag I&D #1) |
| **Versión B — Agentes (Vael)** | NUEVO / AHORA CON / PROTECCIÓN / TÉRMICA |
| **Flag Vera — Versión B** | ✅ APROBADO sin condiciones. Más breve, más seguro. |
| **Recomendación Oz** | **Implementar Versión B: NUEVO / AHORA CON / PROTECCIÓN / TÉRMICA** |

**Justificación de la recomendación:** La Versión B está aprobada sin condiciones por la validación técnica, es visualmente más limpia para el espacio disponible (~30 caracteres por línea), y la precisión técnica se desarrolla en el retiro donde el consumidor tiene tiempo de leer. La Versión A puede adoptarse en una revisión posterior una vez que I&D confirme el Flag #1.

---

### SECCIÓN B: RETIRO — CARACTERÍSTICAS (bullet de función térmica)

| Campo | Contenido |
|---|---|
| **Texto actual (eliminar)** | "Nueva protección por sobrecalentamiento que protege la integridad de la instalación eléctrica." |
| **Versión A — Estudio de mercado** | (*) Actúa cuando el protector o sus conexiones se calientan en exceso. (*) Ayuda a reducir fallas por falsos contactos. Sensor térmico interno que abre el circuito al detectar sobrecalentamiento del protector. No reemplaza breakers termomagnéticos de la instalación. |
| **Flag Vera — Versión A** | ⚠️ "o sus conexiones" CONDICIONAL (Flag I&D #1). ❌ "Ayuda a reducir fallas por falsos contactos" RECHAZADO. ✅ "Sensor térmico interno que abre el circuito..." APROBADO. ✅ "No reemplaza breakers termomagnéticos" APROBADO Y NECESARIO. |
| **Versión B — Agentes (Vael)** | (*) Sensor térmico interno que detecta sobrecalentamiento del protector y sus conexiones, y abre el circuito antes de que el calor provoque una falla. (*) Reduce el riesgo de fallas por falsos contactos y conexiones deficientes que se calientan en exceso. |
| **Flag Vera — Versión B** | ⚠️ "y sus conexiones" CONDICIONAL (Flag I&D #1). ❌ "Reduce el riesgo de fallas por falsos contactos" RECHAZADO. |
| **Recomendación Oz — versión segura para implementar ya** | • Sensor térmico interno que detecta sobrecalentamiento del protector y abre el circuito para prevenir daños por calor. |
| **Recomendación Oz — versión completa si I&D confirma Flag #1** | • Sensor térmico interno que detecta sobrecalentamiento del protector y sus conexiones, y abre el circuito para prevenir daños por calor. |

**Nota sobre el disclaimer:** La frase "No reemplaza breakers termomagnéticos de la instalación" está técnicamente aprobada y es necesaria, pero debe ubicarse en la sección INFORMACIÓN DE SEGURIDAD, no en CARACTERÍSTICAS. Trasladarla no elimina el mensaje; lo coloca donde corresponde por tipo de contenido y no interrumpe la narrativa comercial.

**Sobre el bullet de "falsos contactos":** Rechazado en ambas versiones. La promesa no está respaldada en documentación técnica oficial y no es controlable en campo. No incluir bajo ninguna forma.

---

### SECCIÓN C: RETIRO — FUNCIONAMIENTO (oración de función térmica)

| Campo | Contenido |
|---|---|
| **Texto actual (eliminar)** | "Ambos rojos fijos + LED verde intermitente = Alta temperatura." + "Si la instalación se calienta por sobrecarga u otra condición, el protector abre el circuito." |
| **Nota sobre la primera oración** | La descripción de los LEDs ("Ambos rojos fijos + LED verde intermitente = Alta temperatura") es una indicación de estado y puede mantenerse sin cambio si corresponde al comportamiento real del producto. Solo se reemplaza la segunda oración. |
| **Versión A — Estudio de mercado** | Sin propuesta de cambio en esta sección. |
| **Flag Vera — texto actual** | ❌ "Si la instalación se calienta por sobrecarga u otra condición" RECHAZADO — sobredimensiona la protección al implicar que cubre la instalación entera. |
| **Versión B — Agentes (Vael)** | "Si el protector o sus bornes de conexión alcanzan temperatura elevada, el dispositivo abre el circuito para prevenir daños por calor." |
| **Flag Vera — Versión B** | ⚠️ "bornes de conexión" CONDICIONAL (mismo Flag I&D #1). ✅ El resto está aprobado. |
| **Recomendación Oz — versión segura para implementar ya** | Si el protector alcanza temperatura elevada, el dispositivo abre el circuito para prevenir daños por calor. |
| **Recomendación Oz — versión completa si I&D confirma Flag #1** | Si el protector o sus bornes de conexión alcanzan temperatura elevada, el dispositivo abre el circuito para prevenir daños por calor. |

---

## 3. FLAGS DE I&D — PENDIENTES DE CONFIRMACIÓN

Estos dos puntos deben consultarse con el equipo de Ingeniería y Desarrollo de Genteca antes de aprobar el copy final en las versiones condicionales.

---

### FLAG #1 — Alcance físico del sensor NTC: ¿protector solo, o también bornes/conexiones?

**Pregunta:** ¿El sensor NTC está posicionado de modo que detecte exclusivamente la temperatura interna del protector (PCB/relé), o también detecta temperatura en los bornes de conexión?

**Impacto en copy:** Si la respuesta es "solo el protector": usar versiones seguras (sin mencionar "conexiones" ni "bornes"). Si la respuesta es "sí detecta también los bornes o conexiones": usar versiones completas.

**Claims afectados:**
- TIRO: "contra sobrecalentamiento del protector" (Versión A)
- CARACTERÍSTICAS: "y sus conexiones" en el bullet del sensor
- FUNCIONAMIENTO: "o sus bornes de conexión"

---

### FLAG #2 — Rearme: ¿automático o requiere ciclo de energía?

**Pregunta:** Cuando el sensor abre el circuito por temperatura elevada, ¿el protector rearma automáticamente al bajar la temperatura, o el usuario debe apagar y encender el equipo?

**Impacto en copy:** Si el rearme es automático, puede mencionarse en FUNCIONAMIENTO como característica de uso. Si requiere ciclo de energía, debe indicarse claramente para evitar reclamos de usuarios. En cualquier caso, este dato debe reflejarse en la sección FUNCIONAMIENTO con una línea adicional.

**Claims afectados:** No hay copy actual que lo mencione — se necesita agregar una línea nueva en FUNCIONAMIENTO según la respuesta.

---

## 4. NOTA PARA OZWALDO

### Qué puedes implementar ahora mismo (sin esperar a I&D)

**TIRO:**
Reemplazar la cintilla actual por:
```
NUEVO
AHORA CON
PROTECCIÓN
TÉRMICA
```

**CARACTERÍSTICAS (reemplazar el bullet actual sobre la protección térmica):**
```
• Sensor térmico interno que detecta sobrecalentamiento del protector y abre el circuito para prevenir daños por calor.
```

**FUNCIONAMIENTO (reemplazar la oración rechazada):**
```
Si el protector alcanza temperatura elevada, el dispositivo abre el circuito para prevenir daños por calor.
```

**INFORMACIÓN DE SEGURIDAD (agregar o reubicar desde CARACTERÍSTICAS):**
```
• No reemplaza los breakers termomagnéticos de la instalación eléctrica.
```

---

### Qué queda en suspenso hasta respuesta de I&D

- La mención a "sus conexiones" o "bornes de conexión" en CARACTERÍSTICAS y FUNCIONAMIENTO (Flag #1)
- La posible línea adicional en FUNCIONAMIENTO sobre el comportamiento de rearme (Flag #2)

Estas son modificaciones menores de copy sobre la estructura que ya estarás editando. Puedes dejar un placeholder o nota en el archivo de trabajo para incorporarlas en cuanto llegue la confirmación.

---

### Qué NO implementar bajo ninguna circunstancia

- ❌ Cualquier mención a "falsos contactos" en cualquier sección
- ❌ "protege la integridad de la instalación eléctrica" (el texto actual)
- ❌ "Si la instalación se calienta por sobrecarga u otra condición" (el texto actual de FUNCIONAMIENTO)

---

*Documento preparado para revisión interna. Una vez confirmados los Flags de I&D, se emitirá v2 con el copy final completo.*
