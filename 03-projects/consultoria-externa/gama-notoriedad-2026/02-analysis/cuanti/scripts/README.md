# CU-7 Scripts Package — Cuanti V3 — Gama Notoriedad 2026

**Autor:** Cuanti (agente analitico)
**Fecha:** 2026-05-17
**Proyecto:** Notoriedad de Marca — Gama Excelsior — Ola 2026

---

## Resumen del paquete

Scripts Python reproducibles para los analisis cuantitativos de la capa Cuanti V3.
Complementan y elevan el analisis V2 (Raoul, 2026-05-16) sin reemplazarlo.

---

## Estructura de archivos

```
cuanti/
  scripts/
    00_cuanti_master.py        # Master: ejecuta CU-1 a CU-5 (disponible hoy)
    04_drivers_rf_shap.py      # CU-3 RF+SHAP (requiere scikit-learn+shap)
    05_segmentation_kmeans_lca.py  # CU-4 k-means/LCA formal (requiere scikit-learn)
    utils.py                   # NumpyEncoder para json.dump + helpers
    requirements.txt           # Librerias requeridas

  outputs/
    json/
      CU1_reconciliation_20260517_v1.json
      CU2_stat_pack_20260517_v1.json
      CU3_drivers_20260517_v1.json
      CU4_segmentation_20260517_v1.json  (clustering Ward/scipy)
      CU5_pricing_20260517_v1.json
      p33_p34_corrected.json             (precios con categorias correctas)
      EXEC_META_20260517_v1.json

  plots/
    (vacias hasta instalar scikit-learn/shap/matplotlib)

  2026-05-17_CU-1_reconciliation_v1.md
  2026-05-17_CU-2_stat-pack_v1.md
  2026-05-17_CU-3_drivers-RF-SHAP_v1.md
  2026-05-17_CU-4_segmentation_v1.md
  2026-05-17_CU-5_pricing_v1.md
  2026-05-17_CU-6_caveats-para-bruna_v1.md  <- GATE BRUNA (leer primero)
```

---

## Como reproducir el analisis (en 5 pasos)

### Prerequisitos

1. Python instalado (3.10+)
2. Librerias disponibles: `pandas`, `numpy`, `scipy`, `statsmodels`, `openpyxl`
3. BBDD raw en `01-data-raw/NUEVO BBDD Notoriedad 2026.xlsx`
4. Scripts V2 en `02-analysis/` (common_bbdd.py y los faseX_*.py)

### Pasos

**Paso 1 — Verificar entorno**

```
python -c "import pandas, numpy, scipy, statsmodels; print('OK')"
```

**Paso 2 — Ejecutar analisis principal (CU-1 a CU-5)**

```
cd 02-analysis/cuanti/scripts
python 00_cuanti_master.py
```

Produce los JSONs en `outputs/json/` y muestra progreso en consola.
Tiempo estimado: 2-3 minutos.

**Paso 3 (opcional) — RF+SHAP (requiere autorizacion Owner)**

```
pip install scikit-learn shap matplotlib
python 04_drivers_rf_shap.py
```

Produce `CU3_rf_shap_20260517_v1.json` y plots en `plots/`.

**Paso 4 (opcional) — K-means formal (requiere autorizacion Owner)**

```
pip install scikit-learn matplotlib  # si no instalado en paso 3
python 05_segmentation_kmeans_lca.py
```

Produce `CU4_kmeans_20260517_v1.json` y plots.

**Paso 5 — Gate Bruna**

Leer `2026-05-17_CU-6_caveats-para-bruna_v1.md` antes de publicar cualquier cifra.

---

## Convenciones de naming

| Tipo | Patron | Ejemplo |
|---|---|---|
| JSONs intermedios | `CU[N]_[descriptor]_[YYYYMMDD]_v[N].json` | `CU3_drivers_20260517_v1.json` |
| Reportes Markdown | `YYYY-MM-DD_CU-[N]_[descriptor]_v[N].md` | `2026-05-17_CU-3_drivers-RF-SHAP_v1.md` |
| Scripts | `0N_[accion].py` | `04_drivers_rf_shap.py` |
| Plots | `[tipo]_[YYYYMMDD]_v[N].png` | `shap_bar_20260517_v1.png` |

---

## Diferencias V2 vs V3

| Capacidad | V2 (2026-05-16) | V3 (2026-05-17) |
|---|---|---|
| Logit drivers | Si | Si (reproducido + IC95) |
| z-tests significancia | Parcial (Gama vs comp) | Completo (Gama x genero, NSE, municipio) |
| IC95 para % clave | No | Si (Wilson method) |
| Chi-cuadrado NSE x preferencia | No | Si |
| RF + SHAP | No | Documentado, pendiente instalacion |
| Clustering/segmentacion | No | Si (Ward + hipotesis LCA) |
| K-means formal | No | Pendiente instalacion sklearn |
| Precio P33 con categorias correctas | Parcial | Si (categorias reales verificadas) |
| P34 evolucion precio | Si | Si (verificado) |
| CU-6 Caveats Memo formal | No | Si (gate Bruna) |
| Wave-over-wave framework 2027 | No | Si (protocolo completo) |
| Reconciliacion JSON vs BBDD raw | Parcial (faseA) | Completa (todos los JSONs) |

---

## Bugs conocidos en V2 (documentados en CU-1)

1. **BUG-CU1-001 (CRITICO):** `faseA_embudo_bbdd.json` tiene n_C+/C=0. No afecta el deck V2 (los scripts faseB lo calculan correctamente), pero el JSON canonical de faseA es incorrecto.
2. **BUG-CU1-002 (MENOR):** 4 JSONs de V2 tienen caracteres mal codificados (latin-1 en lugar de UTF-8) en labels de texto. Los scripts V3 no reproducen este bug.

---

## Contacto y custodia

- **Analisis V3:** Cuanti (agente analitico, RAUL workspace)
- **Analisis V2:** Raoul Bermudez (raoul.bermudez@gmail.com)
- **Coordinacion cliente:** Cora Urrea
- **Gate de publicacion:** Bruna (ver CU-6)
- **NDA:** BBDD raw y JSONs no se comparten fuera del equipo. Solo los reportes .md y el deck PPTX van a Gama.
