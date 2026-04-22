# Nota de Aplicación — Protección de Sistemas de Iluminación

**Línea:** Exceline Profesional  
**Código:** NA 2021-V1-003  
**Tipo de documento:** Nota de Aplicación  
**Fabricante:** Gente, Generación de Tecnología, C.A. — www.genteca.com.ve  
**Referencia PDF:** NA-003-Sistemas-Iluminacion.pdf (Notas_Aplicacion/NA-003-Sistemas-Iluminacion.pdf en RAG_SOURCES)

---

## Descripción de la Aplicación

**Aplicación:** Tablero de protección y control para sistemas de iluminación halógenos, fluorescentes y LEDs en comercios, industrias e instalaciones deportivas  
**Fallas protegidas:** Voltaje alto, voltaje bajo, inestabilidad, parpadeos, apagones

---

## Problema

Los sistemas de iluminación modernos (halógenos, fluorescentes, LEDs) son especialmente sensibles a las fallas eléctricas, particularmente a la inestabilidad y los parpadeos. Sin protección, requieren sustitución frecuente de luminarias.

---

## Solución Propuesta

Instalar un tablero de protección y control que:
1. Desconecte por completo el sistema al detectar distorsiones o fallas en el sistema eléctrico
2. Reconecte las líneas solo cuando las condiciones eléctricas sean seguras

---

## Equipos del Tablero

| Equipo | Modelo | Función |
|--------|--------|---------|
| Supervisor de voltaje monofásico | GSM-L (GSML120 o GSML220) | Protección contra alto y bajo voltaje en instalaciones monofásicas |
| Supervisor de voltaje trifásico | GST (GST208 o GST440) | Protección contra alto/bajo voltaje + desbalance + fase perdida + fase invertida |
| Supresor de picos de alta energía | GMP5-35 (GMP5-3520 o GMP5-3540) | Direcciona descargas atmosféricas y sobretensiones por conmutación hacia tierra |
| Contactor | Según corriente de instalación | Desconexión/conexión de las cargas |

---

## Esquemas de Conexión

### Esquema 1 — Instalaciones Trifásicas con Cargas Trifásicas y Bifásicas

```
L1 ──[MCB/Fusible]──┬──[GMP5-35]──┬── Tierra
L2 ──[MCB/Fusible]──┼──[GMP5-35]──┤
L3 ──[MCB/Fusible]──┴──[GMP5-35]──┘
         │
      [GST] ──→ Bobina Contactor (A1-A2)
         │
      [CONTACTOR] ──→ Sistema de Iluminación
                      (cargas trifásicas y bifásicas)
```

- Para 208 VAC: GST220 + GMP5-3520
- Para 480 VAC: GST440 + GMP5-3540
- Las cargas no deben estar conectadas a neutro en este esquema

### Esquema 2 — Instalaciones Trifásicas con Cargas Monofásicas

```
F1 ──[GMP5-35]──Tierra       F1──[GSM-L]──┐
F2 ──[GMP5-35]──Tierra  →   F2──[GSM-L]──┼──→ Bobina Contactor (A2-A1)
F3 ──[GMP5-35]──Tierra       F3──[GSM-L]──┘
                                    ↓
                              [CONTACTOR] ──→ Sistema Iluminación Trifásico
                                              con Cargas Monofásicas
```

Bornes de cada GSM-L: terminales 5-6-7-8 (entrada) y 1-2-3-4 (salida)

- Para 120 VAC F-N: GSML120 + GMP5-3520
- Para 230 VAC F-N: GSML220 + GMP5-3540
- Se puede agregar un cuarto supresor entre neutro y tierra (opcional)

### Esquema 3 — Instalaciones Bifásicas o Monofásicas

```
F1 ──[GMP5-35]──Tierra       F1──[GSM-L]──┐
F2 ──[GMP5-35]──Tierra  →   F2──[GSM-L]──┼── Salidas en serie ──→ Bobina Contactor
N                                           ↓
                              [CONTACTOR] ──→ Sistema Iluminación Bifásico/Monofásico
```

- Para un solo supresor y supervisor si el sistema es completamente monofásico
- Para 120 VAC F-N: GSML120 + GMP5-3520
- Para 230 VAC F-N: GSML220 + GMP5-3540

---

## Recomendaciones de Configuración

| Producto | Parámetro | Valor recomendado |
|----------|-----------|-------------------|
| GSML | Voltaje bajo | Según especificaciones del fabricante del equipo |
| GST | Voltaje bajo | Según especificaciones del fabricante del equipo |
| GST | Voltaje alto | Según especificaciones del fabricante del equipo |
| GST | Tiempo de detección | 0,5 segundos (mínimo) |
| GST / GSML | Tiempo de conexión | 1 min — Luminarias LED / 3 min — Fluorescentes y halógenas (*) |

(*) El tiempo de conexión depende del tipo de lámparas: las lámparas fluorescentes y halógenas requieren más tiempo de recuperación después de un apagón o parpadeo.

---

## Recomendaciones Adicionales

1. **Mantenimiento de supresores:** Inspeccionar el estado de los GMP5-35 regularmente. Si la ventana está en **rojo**, el supresor debe ser sustituido.
2. **Cable de tierra de supresores:** Calibre entre AWG 10 y AWG 6.
3. **Verificar calidad de tierra:** La conexión a tierra es fundamental para la protección ante descargas de alta energía.
4. **Protecciones independientes por sistema:** Evitar que al regresar la energía todos los equipos conecten simultáneamente (alta demanda de corriente).
5. **Selección del contactor:**
   - Cantidad de polos: 2 (bifásico) o 3 (trifásico)
   - Categoría: AC1 (cargas resistivas) o AC3 (cargas inductivas)
   - Corriente: seleccionar el valor estándar inmediatamente superior a la corriente máxima de la instalación
   - Bobina: según voltaje de la señal de control (24, 120, 240 VAC, etc.)
   - Contactos auxiliares: definir si se requieren NC o NO

---

## Contacto

Consultas: info@genteca.com.ve | www.genteca.com.ve | @excelinevzla
