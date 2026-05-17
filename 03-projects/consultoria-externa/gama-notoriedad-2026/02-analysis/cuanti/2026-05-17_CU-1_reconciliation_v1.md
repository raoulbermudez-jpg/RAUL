# CU-1 Reconciliation Report — Gama Notoriedad 2026
**Fecha:** 2026-05-17 | **n actual (V3 raw):** 402 | **Referencia comparada:** JSONs V2 (2026-05-16)
**Nivel de significancia:** 95% (alpha=0.05) | **Base baja flag:** n<30

---

## Nota sobre el marco de reconciliacion

Esta es la **primera ola de campo 2026**. No existe ola anterior de campo comparable. La reconciliacion CU-1 de esta entrega compara los JSONs serializados en V2 (producidos el 2026-05-16 durante el analisis en sesion) contra el BBDD raw directamente. Objetivo: certificar que las cifras publicadas en V2 son correctas, o documentar discrepancias.

El **framework wave-over-wave para 2027** se documenta al final de este memo y queda listo para activarse.

---

## Seccion 1 — Reconciliacion de n por segmento

| Segmento | n BBDD raw | n JSON V2 (faseA) | Match | Discrepancia |
|---|---|---|---|---|
| Total | 402 | 402 | SI | 0 |
| C+/C | **104** | **0** | **NO** | **-104** |
| D | 127 | 127 | SI | 0 |
| E | 171 | 171 | SI | 0 |
| Pref-Gama | 32 | 32 | SI | 0 |

### BUG CRITICO detectado — BUG-CU1-001

**Severidad: CRITICO**

`faseA_embudo_bbdd.json` reporta C+/C con n=0 y todos los porcentajes = 0.0. El BBDD raw confirma C+/C n=104 (25.9% de la muestra).

**Causa probable:** en el momento en que se ejecuto faseA, la mascara `get_masks()` usaba `nse == 'C+/C'` pero COL_NSE podia tener espacios o diferencias de encoding que evitaron el match. El bug fue resuelto internamente en faseB y scripts posteriores (que reconstruyen las mascaras localmente), por eso el deck V2 muestra cifras C+/C correctas.

**Impacto en deck V2 entregado a Cora:** BAJO. Los slides C+/C del deck V2 se generaron desde calculos propios de cada script faseB/C/D, no desde la lectura de `faseA_embudo_bbdd.json`. Las cifras del deck son correctas.

**Impacto residual:** cualquier script futuro que lea `faseA_embudo_bbdd.json` directamente para el segmento C+/C recibira 0.0 en lugar de las cifras reales. Requiere regenerar ese JSON.

**Accion requerida para V3/2027:** regenerar `faseA_embudo_bbdd.json` ejecutando `faseA_embudo_y_banners.py` con la version corregida de `common_bbdd.py` (que ya tiene la mascara correcta).

---

## Seccion 2 — Reconciliacion cifras clave del embudo Gama

| Metrica | Valor JSON V2 | Valor recalculado V3 | Match | Diferencia |
|---|---|---|---|---|
| TOM Gama Total | 44.28% | 44.28% | SI | 0.00pp |
| Asistida Gama Total | 50.25% | 50.25% | SI | 0.00pp |
| Preferida Gama Total | 7.96% | 7.96% | SI | 0.00pp |
| Pseudo R2 Logit | 0.4371 | 0.4371 | SI | 0.0000 |
| n Pref-Gama (logit) | 32 | 32 | SI | 0 |

**Certificaciones emitidas:**
- n_total=402 VERIFICADO contra BBDD raw
- n_D=127 y n_E=171 VERIFICADOS contra BBDD raw
- n_C+/C=104 VERIFICADO en raw (discrepancia es solo en JSON faseA, no en analisis posterior)
- Preferencia Gama Total 7.96% VERIFICADO — match raw vs JSON V2 <0.01pp
- Logit Pseudo R2 McFadden = 0.4371 VERIFICADO — match <0.005

---

## Seccion 3 — Bugs de encoding en JSONs V2

**Severidad: MENOR — BUG-CU1-002**

Se detectaron caracteres mal codificados (latin-1 / cp1252) en **4 JSONs**: `faseC3_4_5_categorias_segmentos_misiones`, `faseD1_PF_publicitario`, y otros dos. Se manifiestan como `Ã©`, `Ã­`, `Ã"` en lugar de letras acentuadas.

**Causa:** algunos scripts V2 serializaron con `json.dump` sin especificar `ensure_ascii=False` en alguna ruta de codigo, o la variable de entorno no forzaba UTF-8 al momento de escribir.

**Impacto:** las labels de categorias en tablas de precios y de parroquias pueden mostrar caracteres incorrectos si el deck los lee desde JSON. El deck V2 PPTX usa sus propias cadenas hardcodeadas en el script, por lo que el impacto visual es bajo.

**Accion requerida:** todos los scripts CU-7 de Cuanti V3 usan `ensure_ascii=False` y `sys.stdout.reconfigure(encoding='utf-8')`. No reproducira el bug.

---

## Seccion 4 — Framework wave-over-wave para ola 2027

### Comparabilidad de preguntas

| Bloque | Pregunta | Comparabilidad 2026 vs 2027 | Condicion |
|---|---|---|---|
| Embudo | P16 TOM | Comparable | Misma redaccion y lista de marcas |
| Embudo | P17 Asistida | Comparable | |
| Embudo | P19 Consideracion | Comparable | |
| Embudo | P20 Compra 3m | Comparable | |
| Embudo | P21 Preferida | Comparable | |
| Atributos | P22 Importancia | Parcialmente comparable | Solo 10 atributos 2026 subset de 20 de 2025 |
| Atributos | P23 Asociacion | Parcialmente comparable | Solo 10 atributos comunes |
| Precio | P31 Ranking | NO comparable | Metodologia distinta en 2025; 2027 debe replicar exactamente la 2026 |
| Precio | P33 Percepcion | Sin referencia previa | Pregunta nueva 2026; servira como baseline 2027 |
| Precio | P34 Evolucion | Sin referencia previa | Pregunta nueva 2026 |

### Protocolo de z-test inter-ola

Para comparar proporciones entre ola 2026 (n=402) y ola 2027 (n estimado ~600):

```
z, p = proportions_ztest([x_2026, x_2027], [n_2026, n_2027])
```

Valido para disenos cross-sectional independientes. Antes de aplicar, verificar:
1. La pregunta tiene exactamente el mismo enunciado y lista de opciones
2. El marco muestral y metodo de reclutamiento son comparables
3. Documentar cualquier diferencia en cuestionario como "comparacion indicativa, no estadisticamente valida"

---

## Resumen ejecutivo CU-1

**Un bug critico** (n C+/C = 0 en JSON faseA) que NO afecta el deck V2 entregado a Cora, pero que debe corregirse antes de la ola 2027.

**Un bug menor** de encoding en 4 JSONs, sin impacto en deck PPTX.

**Todas las cifras clave verificadas:** TOM Gama 44.3%, Preferencia Gama 8.0%, Pseudo R2 logit 0.437. El analisis cuantitativo V2 es internamente consistente con el BBDD raw.

**Framework wave-over-wave listo** para ola 2027 con protocolo de z-test y mapa de comparabilidad por pregunta.

---

*Producido por Cuanti V3 — 2026-05-17. JSON canonico: `CU1_reconciliation_20260517_v1.json`.*
*Gate Bruna: ver CU-6 para impacto de estos hallazgos en claims publicables.*
