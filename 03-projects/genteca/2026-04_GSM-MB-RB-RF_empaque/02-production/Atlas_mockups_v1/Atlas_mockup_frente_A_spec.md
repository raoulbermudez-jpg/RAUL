# Spec — Atlas Mockup Frente Alternativa A
**Documento:** Atlas_mockup_frente_A_spec
**Fecha:** 2026-05-03
**Proyecto:** 2026-04_GSM-MB-RB-RF_empaque
**Output:** AT-2 Static Key Visual — Arte casi final para presentación a Junta Directiva
**Modelo de referencia:** GSM-RB (los otros 3 modelos — MB, RF, RE — siguen mismo layout con paleta correspondiente)
**Archivo de mockup:** Atlas_mockup_frente_A.svg

---

## 1. Copy aplicado (literal Solenne SO-1, sin modificación)

| Elemento | Texto exacto aplicado |
|---|---|
| Lengüeta línea 1 | NUEVO |
| Lengüeta línea 2 | LA PROTECCIÓN MÁS COMPLETA |
| Frase 1 — dato | <0,03 s |
| Frase 1 — descriptor | El más rápido ante parpadeos |
| Frase 2 | Protege tecnología Inverter |
| Frase 3 | Sensor NTC incorporado* |
| Asterisco — remisión | Ver información del Sensor NTC al reverso del empaque. |

No se reescribió ni acortó ningún texto. El asterisco cumple la condición de visibilidad requerida por Bruna §2 Claim D.

---

## 2. Decisiones de diseño clave

### 2.1 Estructura de zonas

El tiro se organiza en 7 zonas verticales:

1. **Logo Exceline Profesional** (placeholder para vectorial de Oz)
2. **Lengüeta naranja** (cintilla full-width #FF8200)
3. **Imagen del producto** (placeholder para foto oficial de Oz — GSM-RB)
4. **Bloque causa-efecto Frases 1 + 2** (zona crítica — ver §2.2)
5. **Badge NTC independiente** (Frase 3, fuera de la cápsula)
6. **Asterisco de remisión al retiro**
7. **Franja de specs técnicas + QR + barcode**

### 2.2 Mecanismo de conexión visual Frase 1 ↔ Frase 2 (Condición Bruna §2 Claim C)

**Problema a resolver:** "Protege tecnología Inverter" no puede estar en el tiro desconectado visualmente del dato de velocidad (Bruna §2 Claim C, condición inamovible). Si la conexión no se garantiza, la Frase 2 debe mover al retiro.

**Solución implementada — Cápsula unificadora:** Las Frases 1 y 2 se encierran en un mismo rectángulo con fondo gradiente naranja translúcido y borde #FF8200 de 2px. Este contenedor visual agrupa las dos frases ANTES de que el lector las lea, estableciendo la relación causa-efecto por agrupamiento perceptual (principio Gestalt de proximidad/unidad). La Frase 3 (NTC) queda explícitamente fuera de esta cápsula, reforzando su estatus como "capa adicional independiente".

**Elemento conector interno:** Dentro de la cápsula, entre las Frases 1 y 2, se coloca un ícono de 3 elementos en línea horizontal: onda eléctrica (parpadeo) → flecha de interceptación → símbolo "INVERTER". Este ícono visualiza la cadena causal sin añadir texto. Es el único elemento gráfico que no está en el copy de Solenne; su función es estrictamente de conexión visual entre claims aprobados.

**Jerarquía tipográfica del dato cuantitativo:** "<0,03 s" se coloca en 72px Montserrat Black con filtro glow naranja, contra 15px para el texto descriptivo de la Frase 1. La diferencia de escala (4,8:1) garantiza que el valor cuantitativo sea el primer elemento que el ojo capta. La condición "tipografía notoriamente mayor" de Solenne SO-1 está cumplida.

### 2.3 Borde izquierdo naranja sólido

La cápsula lleva un borde izquierdo de 6px en #FF8200 sólido. Este recurso refuerza el agrupamiento y crea un elemento de marca consistente que Atlas recomienda mantener para los tres mockups (coherencia de familia).

### 2.4 Frase 3 — NTC como capa adicional

El badge NTC se coloca en un rectángulo separado (#1e1e1e con stroke #444), diferenciado de la cápsula naranja. Tipografía 18px vs 72px del dato de velocidad y 22px de "Protege tecnología Inverter". La diferencia de tamaño y contenedor establece la jerarquía de tercer claim sin necesitar anotación verbal.

### 2.5 Ícono de parpadeo (sistema Exceline)

El ícono de parpadeo/rayo implementado corresponde al ícono "Parpadeos" del sistema de íconos de fallas del sistema eléctrico venezolano de Exceline (brand wiki §Íconos de Fallas). Se usa la forma de rayo con círculo de contexto eléctrico. Oz debe reemplazar este ícono esquemático por el vectorial oficial del brand kit.

### 2.6 Paleta aplicada

| Elemento | Color | Pantone / Referencia |
|---|---|---|
| Naranja principal | #FF8200 | Pantone 151 C |
| Gris corporativo (textos secundarios) | #737578 | Pantone Cool Gray 9C |
| Fondo principal | #1a1a1a → #0d0d0d | Gradiente — base arte Oz |
| Texto principal | #ffffff | — |
| Texto secundario | #cccccc / #888888 | — |
| Dato cuantitativo | #FF8200 con glow | Naranja principal + filtro |

No se introdujo ningún color fuera del brand kit Exceline Profesional.

### 2.7 Tipografía

Montserrat en todas las variantes de peso (400 Book, 500 Medium, 600 SemiBold, 700 Bold, 900 Black), según uso en empaques del brand kit (brand wiki §Sistema Tipográfico: "En empaques, dummies, gigantografías y exhibiciones PdV"). Nota: Futura Bold / Heavy son alternativas para títulos; para este mockup se usa Montserrat como fuente de referencia. Oz puede ajustar a Futura para los títulos si el sistema de Oz lo requiere.

---

## 3. Condiciones de Bruna respetadas

| Condición | Origen | Estado en mockup |
|---|---|---|
| "Protege tecnología Inverter" en proximidad visual con "<0,03 s" | Bruna §2 Claim C | CUMPLIDA — misma cápsula, mismo contenedor visual |
| "<0,03 s" en tipografía notoriamente mayor que descriptor Frase 1 | SO-1 Brief Atlas A | CUMPLIDA — 72px vs 15px (relación 4,8:1) |
| Asterisco de NTC visible y legible, remite al retiro | Bruna §2 Claim D | CUMPLIDA — asterisco 22px en posición prominente + nota de remisión |
| Lengüeta "La Protección más completa" requiere 3 sub-claims en tiro | Bruna §2 Claim F | CUMPLIDA — los 3 sub-claims (velocidad + inverter + NTC) están en el tiro |
| Nada con "protege al motor" / "protege a la carga" | Bruna §2 Claim H | CUMPLIDA — no aparece ninguna formulación de este tipo |
| Nada con "garantiza la protección" / "evita daños" | Bruna §2 Claim L | CUMPLIDA |

---

## 4. Riesgos identificados

### 4.1 Densidad visual (riesgo táctico — no estructural)

Con 4 elementos en el tiro (lengüeta + Frases 1+2 agrupadas + Frase 3), el tiro es el más denso del set de tres alternativas. La cápsula unificadora mitiga el riesgo al agrupar Frases 1 y 2 en una unidad visual, pero el blister físico es pequeño. Si en el arte final de Oz las frases quedan apretadas, la solución recomendada es reducir el cuerpo de los textos descriptivos (15px → 13px) y aumentar el espacio interior de la cápsula.

**Severidad:** Táctico. Oz puede resolverlo en el redline sin cambio de copy ni de claims.

### 4.2 Ícono conector — debe ser reemplazado por vectorial oficial

El ícono de onda → flecha → "INVERTER" incluido en este mockup es esquemático. Oz debe reemplazarlo por el ícono vectorial de "Parpadeos" del brand kit y una representación estándar del símbolo inverter (onda cuadrada AC). Si el brand kit no tiene símbolo inverter estandarizado, Oz debe proponer uno a Raul antes del redline final.

**Severidad:** Táctico. No afecta claims ni gates.

### 4.3 Placeholder de imagen de producto

La imagen del producto GSM-RB es un placeholder. Oz inserta la foto oficial. La composición de la Zona 3 asume proporciones estándar del blíster; si la foto del producto tiene proporciones diferentes, Oz ajusta la Zona 3 sin afectar las otras zonas.

### 4.4 Adaptación a otros 3 modelos

Este mockup usa GSM-RB como referencia. Para GSM-MB / RF / RE:
- Mismo layout
- Paleta específica del modelo (si cada modelo tiene color diferenciador propio — Oz confirma)
- Datos numéricos de HDE actualizados por modelo (nominals, corriente, potencia)
- Los claims de tiro son idénticos para los 4 modelos (copy idéntico salvo color/aplicación, per WORKSTREAM_v5)

---

## 5. Pendientes para Oz (redline final)

1. Reemplazar placeholder de logo por vectorial oficial Exceline Profesional.
2. Reemplazar placeholder de imagen de producto por foto oficial GSM-RB (+ otros 3 modelos).
3. Reemplazar ícono esquemático de parpadeo por ícono vectorial del brand kit.
4. Crear/confirmar ícono de "equipo inverter" si no existe en el brand kit.
5. Ajustar tipografía a Futura Bold/Heavy para títulos si el sistema Oz lo requiere (Montserrat en mockup es compatible con el brand kit; Futura es la opción canónica para títulos).
6. Añadir datos técnicos numéricos reales de cada modelo en la franja de specs.
7. Adaptar el mockup para GSM-MB / RF / RE (paleta de color por modelo + datos de HDE).
8. Preparar el archivo para CMYK + sangrado 3mm cuando sea el arte final.
9. Confirmar si el QR existente en el arte original Oz se redirecciona o se añade uno nuevo (decisión Aurelio + Vael — pendiente memo lateral).

---

## 6. Notas de producción

- **Datasheet I&D:** Ninguna de las 3 alternativas puede imprimirse hasta que I&D emita el datasheet actualizado con "<30 ms" documentado (condición de producción Bruna §2 Claim A, reiterada en WORKSTREAM_v5). El arte puede avanzar; la impresión está condicionada a ese documento.
- **Lengüeta condicional:** Si en producción se elimina alguno de los 3 sub-claims del tiro por restricciones de espacio, la lengüeta debe cambiar a "Nuevo. Una protección más completa" (Bruna §2 Claim F). Esta condición está documentada en SO-1 y en Bruna_gate_empaque_v1.

---

*Atlas — Static Visual Production Lead — Sistema /RAUL/*
*Spec emitido: 2026-05-03*
