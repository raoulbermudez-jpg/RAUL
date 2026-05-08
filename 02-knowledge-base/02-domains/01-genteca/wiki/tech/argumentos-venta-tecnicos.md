# Argumentos de venta técnicos — Genteca

> ## ✅ 7 de 8 ARGUMENTOS APROBADOS PARA USO EXTERNO (BR-2 2026-05-07)
>
> **Estado:** BR-2 emitido por Bruna 2026-05-07 tras autorización del Owner.
> **Fecha de extracción inicial:** 2026-05-07.
> **Origen:** Atlas 4 legacy (mercado Venezuela, marzo 2026) + RAG Integrador secciones 5-6.
> **Log de claims:** `03-projects/genteca/_governance/2026-05-03_genteca_claim-approval-log_v1.md` (entradas #22 a #28 — appendeadas 2026-05-07).
>
> **Distribución de veredictos:**
>
> | # | Argumento | Veredicto | Uso externo |
> |---|---|---|---|
> | 1 | Monitor de red | 🟡 AMARILLO con caveat | ✅ aprobado |
> | 2 | Relé electrónico vs bimetálico | 🟡 AMARILLO con caveat | ✅ aprobado |
> | 3 | Coordinación Tipo 2 | 🟢 VERDE | ✅ aprobado sin cambios |
> | 4 | PTC para sumergibles | 🟡 AMARILLO con caveat | ✅ aprobado |
> | 5 | Clase 10 para bombas | 🟢 VERDE | ✅ aprobado sin cambios |
> | 6 | Anti-short cycle hardware GST-RR/GSC-CR | 🟢 VERDE | ✅ aprobado (verificar ficha técnica vigente) |
> | 7 | Cable sumergible (reformulado) | 🟡 AMARILLO con caveat | ✅ aprobado tras reformulación |
> | **8** | **COVENIN 3445** | 🔴 **ROJO** | **❌ PENDIENTE — no usar externamente** |
>
> **Reglas de uso:**
> - Los argumentos VERDE pueden usarse externamente sin caveat adicional.
> - Los argumentos AMARILLO requieren incluir el caveat literal escrito en la sección "Caveat literal" de cada argumento (también en el log de claims).
> - El Argumento 8 (COVENIN 3445) NO puede usarse externamente bajo ninguna forma hasta verificación SENCAMER/FONDONORMA del certificado vigente.
> - Los argumentos comparativos contra terceros (Schneider, ABB, genéricos chinos, WEG) **siguen vetados** — viven en `legacy-atlas/ProtMotores_Atlas_4_Mercado_Venezuela.md` solo para consulta histórica.
>
> **Por qué este documento existe:**
> Vera identificó (auditoría 2026-05-07) que el Atlas 4 tiene argumentos técnicos basados en física verificable — útiles. Pero también argumentos comparativos contra terceros que están en zona Precedente #3 de Bruna (gate GME) — riesgosos. Este documento contiene **solo los argumentos basados en física verificable**.

---

## 1. Argumento — Monitor de red obligatorio en Venezuela

**Fundamento técnico (verificable):**
El relé de sobrecarga protege contra sobrecarga por corriente. No detecta adecuadamente:
- Falta de fase (10-60s en bimetálico vs <500ms en monitor de red)
- Desequilibrio de fases
- Subtensión

El monitor de red detecta las tres condiciones por voltaje, antes de que la corriente de falla se establezca.

**Frase utilizable internamente:**
"El relé térmico es la última línea de defensa: actúa cuando ya hay corriente de falla. El monitor de red actúa antes de que la corriente de falla se establezca, al detectar la condición de red que la causará. Son complementarios, no sustitutos."

**Analogía interna:** "Es como tener airbag pero no cinturón de seguridad. El airbag (relé térmico) actúa cuando ya ocurrió el impacto. El cinturón (monitor de red) evita que llegue al impacto."

**Pendiente para gate Bruna:** referencias a "tres causas principales de quema en Venezuela" sin estadística publicable; la base es observación de campo sólida pero no cuantificada formalmente.

---

## 2. Argumento — Relé electrónico vs bimetálico

**Fundamento técnico (verificable, basado en especificaciones de los propios dispositivos):**

Tres limitaciones del bimetálico que no son discutibles:

1. **No detecta desequilibrio.** Solo detecta pérdida total de una fase, en 30-60 segundos. Con 5% de desequilibrio (frecuente en CORPOELEC), el motor trabaja con ~50% más de temperatura sin que el relé lo detecte.

2. **No tiene memoria térmica real.** Tres arranques sucesivos en una hora: el bimetálico no acumula correctamente el calor del segundo y tercer arranque. El motor puede estar al límite térmico sin que el relé lo sepa.

3. **Tiempo de disparo en stall: 30-90 segundos.** Un motor de 5 kW bloqueado con 7×In durante 60 segundos puede quemarse. El relé electrónico con función locked rotor dispara en 2-5 segundos.

**Costo de referencia (verificable):**
- Diferencial relé bimetálico vs electrónico: 2-4× en precio del relé.
- El relé representa 10-20% del costo total del conjunto de maniobra (guardamotor + contactor + relé).
- Diferencial real sobre costo total: 5-15%.

**Frase utilizable internamente:**
"El relé bimetálico tiene tres limitaciones críticas para Venezuela: no detecta desequilibrio, no tiene memoria térmica real, y su disparo en stall puede llegar a 90 segundos. El electrónico cubre las tres por 5-15% más sobre el costo del conjunto."

**Pendiente para gate Bruna:** datos de "5% desequilibrio frecuente en CORPOELEC" — observación sólida sin estadística publicable.

---

## 3. Argumento — Coordinación Tipo 2

**Fundamento técnico (verificable, basado en IEC 60947-4-1):**

| Coordinación | Tras cortocircuito |
|---|---|
| Tipo 1 | Posible reemplazo de contactor + relé. Planta para hasta llegar repuestos. |
| Tipo 2 | Solo reemplazo de fusibles (que se tienen en stock). Rearranque rápido. |

**Costo:** diferencial de 15-25% del conjunto de maniobra.

**Frase utilizable internamente:**
"Con coordinación Tipo 2, después de un cortocircuito solo reemplazas fusibles — que tienes en stock de todos modos. La planta rearrancan en minutos, no en días esperando un contactor nuevo. El diferencial 15-25% se paga solo en el primer evento."

**Pendiente para gate Bruna:** ningún dato cuantitativo arriesgado en este argumento; probablemente seguro tras revisión.

---

## 4. Argumento — PTC para sumergibles

**Fundamento técnico (verificable, basado en física del motor sumergible):**

Cuando una bomba sumergible opera sin agua:
1. Pierde su refrigerante natural (el agua).
2. La carga hidráulica desaparece o disminuye.
3. La corriente del motor BAJA (no sube).
4. La temperatura del devanado sube rápidamente.

El relé de sobrecarga calibrado para In NO detecta esta condición — la corriente está en rango normal o por debajo.

El termistor PTC en el devanado mide temperatura real, no corriente. A 150-160°C dispara.

**Costo de referencia (cualitativo):**
- PTC + relé con entrada PTC: incremento mínimo sobre el conjunto.
- Motor sumergible: diseño especial, 3-10× más costoso que motor superficial equivalente.

**Frase utilizable internamente:**
"En bombas sumergibles, la marcha en seco es el problema más frecuente. El relé de sobrecarga no la detecta porque cuando la bomba opera sin agua, la corriente baja, no sube. El PTC sí la detecta porque mide temperatura real del devanado. Para un motor sumergible que cuesta varias veces más que uno superficial, el diferencial de costo del PTC es marginal."

**Pendiente para gate Bruna:** afirmación "marcha en seco es el problema más frecuente" en sumergibles — observación de campo sólida; afirmación "3-10× más costoso" sin fuente citada.

---

## 5. Argumento — Clase 10 para bombas

**Fundamento técnico (verificable, basado en IEC 60947-4-1 + curva de carga):**

Bomba centrífuga: inercia baja, arranque 2-5 segundos.

| Clase | Tiempo disparo @7.2×In | Adecuación a bomba |
|---|---|---|
| 10 | <10s | Correcta (arranque dentro del margen) |
| 20 | <20s | Sobreprotegida — ante stall puede tardar 20s en disparar |

**Frase utilizable internamente:**
"La Clase 20 se diseñó para cargas de alta inercia con arranque de 10-20 segundos (compresores pistón, molinos). Una bomba centrífuga arranca en 2-5 segundos. Con Clase 20, ante un stall de la bomba el relé puede tardar 20 segundos en disparar — un motor de 3-5 kW en stall durante 20 segundos puede quemarse. Con Clase 10, el disparo ocurre en <10 segundos y el arranque normal está dentro del margen."

**Pendiente para gate Bruna:** ninguna afirmación arriesgada; argumento puramente técnico.

---

## 6. Argumento — Anti-short cycle en hardware (productos GENTECA)

**Fundamento técnico (verificable, basado en diseño de productos GST-RR y GSC-CR):**

Cada arranque de un compresor de refrigeración genera calor en el devanado equivalente a 15-30 segundos de operación a plena carga (corriente de arranque 5-7×In durante el periodo de aceleración).

Si un termostato mal calibrado o defectuoso genera ciclos de 1 minuto on / 1 minuto off, el motor no alcanza a disipar el calor entre arranques. En 2-4 horas puede alcanzar temperatura destructiva, incluso con corriente de operación normal.

**Diferenciador GENTECA:** el GST-RR y el GSC-CR tienen el tiempo mínimo de reconexión de **180 segundos restringido por hardware**. No se puede configurar por debajo de este valor por diseño del producto. Otros protectores ajustables permiten configurar el temporizador desde 0 o 5 segundos según ajuste del instalador — si el instalador olvida ajustarlo correctamente, el compresor sufre short cycling desde el primer día.

**Frase utilizable internamente:**
"Con el GST-RR y el GSC-CR, el anti-short cycle está en el hardware. No se puede configurar incorrectamente. No se puede olvidar. No depende de que el técnico instalador sepa por qué los compresores necesitan 3 minutos entre arranques. Para compresores herméticos (que no se rebobinan, se reemplazan completos), esa garantía de hardware tiene valor económico real."

**Pendiente para gate Bruna:** la afirmación es verificable contra ficha técnica del producto. Probablemente segura. Verificar que la afirmación "otros protectores permiten configurar desde 0 o 5 segundos" no genere comparación específica con marcas.

---

## 7. Argumento — Cable sumergible correctamente dimensionado

**Fundamento técnico (verificable, basado en física eléctrica):**

Caída de tensión en cable: ΔV = I × R_cable.

En redes con variabilidad de tensión (subtensión por debajo de Vn nominal), la caída adicional en el cable se acumula sobre la subtensión de red. Si el motor opera ya por debajo de Vn (por causa de la red) y suma una caída adicional en cable insuficiente, puede recibir tensión sustancialmente menor a la nominal.

A 91% de Vn (ejemplo numérico):
- Par de arranque: 0.91² = 83% del nominal (par ∝ V²)
- Corriente: sube para compensar
- Sobrecalentamiento incluso con carga normal

**Norma de diseño:** caída máxima en cable 3% de Vn — para 220V, máximo 6.6V; para 440V, máximo 13.2V.

Para 60 metros de profundidad y 5 HP a 220V: mínimo 6 mm² (no 2.5 mm² como se usa frecuentemente para ahorrar).

**Frase utilizable externamente (BR-2 aprobado, ver caveat):**
"El cable de un motor sumergible es parte del sistema de protección, no solo un conductor. En redes con variabilidad de tensión, una caída adicional en cable insuficiente se acumula sobre la subtensión de red — el motor puede recibir tensión sustancialmente menor a la nominal. A 91% de Vn, el par de arranque es 83% del nominal y la corriente sube para compensar. Calcular siempre con holgura sobre el 3% de caída máxima."

**Caveat literal para uso externo:** la magnitud de la subtensión de red depende de cada zona y cada instalación; el ejemplo del 91% es ilustrativo, no estadística.

**Estado:** 🟡 AMARILLO tras reformulación — aprobado para uso externo con caveat literal (BR-2 2026-05-07 tras reformulación autorizada por Owner).

---

## 8. Argumento — COVENIN 3445 (Exceline Profesional)

> ### 🔴 BLOQUEADO — NO USAR EXTERNAMENTE
>
> **Estado:** ROJO en BR-1 2026-05-07. NO se autorizó en BR-2.
> **Razón:** afirmar cumplimiento normativo con una norma específica sin presentar el número de certificado vigente y su alcance por modelo es riesgo regulatorio directo (precedente BR-2 entrada #13 sobre claim de certificación IEC/COVENIN para línea GSM).
>
> **Acción requerida antes de uso:** alguien técnico/legal de Genteca verifica en SENCAMER/FONDONORMA el estado y número de COVENIN 3445 vigente para los modelos Exceline Profesional + alcance por modelo. Sin ese dato, Bruna no puede gatear.

**Fundamento normativo (verificable):**

COVENIN 3445 es la norma venezolana aplicable a dispositivos de supervisión y protección eléctrica. Los productos Exceline Profesional están diseñados según esta norma.

**Frase que se podría usar (PENDIENTE verificación):**
"Los productos importados europeos cumplen IEC; los americanos cumplen UL. Para instalaciones formales en Venezuela, la especificación técnica local requiere COVENIN. Exceline Profesional es la opción que cumple con el marco normativo local."

**Por qué está bloqueado:** sin certificado vigente verificable + alcance por modelo, la afirmación entra en zona de riesgo regulatorio. La frase es comercialmente valiosa si es real; el problema es el "si es real" — necesita evidencia documental.

---

## 9. Manejo de objeciones — patrones internos

### Objeción: "Ya tengo relé térmico, es suficiente."

**Respuesta interna (no contradecir decisión pasada):**
"El relé térmico que tiene es la tercera línea de defensa — actúa cuando ya hay corriente anormal. Lo que le falta son la primera y la segunda: el monitor de red detecta condiciones antes de que la corriente sea anormal. Son complementarios."

### Objeción: "El precio es muy alto."

**Reencuadre técnico (sin comparar con marcas específicas):**
"¿Cuánto vale el motor que se está protegiendo? Para un motor estándar la protección puede parecer cara. Para un compresor hermético que no se rebobina (se reemplaza completo) o un motor sumergible de diseño especial, la protección representa una fracción pequeña del valor del equipo y puede salvar el 100% si actúa correctamente."

> **Cuidado:** evitar mencionar precios específicos de competidores ("Schneider cuesta 4 veces más") — esto es comparativo no verificable y va contra el precedente Bruna.

### Objeción: "Tengo experiencia con genéricos y no me han fallado."

**Respuesta neutral:**
"Entendido. El hardware genérico puede funcionar bien en aplicaciones de bajo riesgo con red estable. Dos preguntas técnicas: ¿la red de su instalación tiene desequilibrio medido? ¿Algún motor se le ha quemado en los últimos 2 años? Si la respuesta a la segunda es sí, en la mayoría de los casos la causa es falta de fase o desequilibrio — algo que el relé térmico básico no detecta bien."

> **Cuidado:** la calculadora de costo-beneficio "Y% probabilidad de falla en 3 años" del Atlas 4 es **placeholder, no dato real**. NO usarla con cifras hasta tener fuente verificable.

---

## 10. Argumentos del Atlas 4 que NO se incluyen aquí (gate Bruna definitivo)

Los siguientes argumentos del Atlas 4 quedaron archivados en `legacy-atlas/` y NO fueron extraídos a este documento porque tienen claims comparativos contra terceros sin evidencia verificable o datos placeholder:

- Argumentos contra "genéricos chinos" con afirmaciones de calidad relativa ("certificaciones impresas no siempre corresponden a ensayos reales", "tasa de falla prematura mayor")
- Comparativos directos de precio Schneider vs alternativas
- Calculadora costo-beneficio con "Y% probabilidad de falla" sin Y real
- Afirmaciones cuantitativas sobre "rebobinado 30-60% del valor del motor" sin fuente específica
- Caracterización de canales de distribución (Caracas 60-70%, etc.) sin fuente

Si en algún momento el equipo comercial necesita usar estos argumentos, requieren paso por gate Bruna con respaldo de evidencia (ensayo, encuesta de mercado, dato verificable).

---

**Próximo paso:** Argumento 8 (COVENIN 3445) requiere verificación documental con SENCAMER/FONDONORMA antes de uso externo. Una vez tengas el certificado vigente y alcance por modelo, Bruna puede emitir BR-2 adicional para appendear al log de claims.

**Historial de versiones:**

- **v1.0 — 2026-05-08:** 7/8 argumentos aprobados externamente (BR-2 2026-05-07 → log claims #22-28). Argumento 7 (cable sumergible) reformulado eliminando dato cuantitativo "210V CORPOELEC" no respaldado, convertido a "redes con variabilidad de tensión". Argumento 8 (COVENIN 3445) sigue ROJO — pendiente verificación documental.
- **v0.1 — 2026-05-07:** extracción inicial desde Atlas 4 legacy, marcado como "INTERNO-PENDIENTE-GATE" para revisión Bruna.
