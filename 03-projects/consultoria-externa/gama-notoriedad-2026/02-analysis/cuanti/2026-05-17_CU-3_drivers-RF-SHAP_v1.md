# CU-3 Drivers Analysis — RF/SHAP vs Logit — Gama Notoriedad 2026
**Fecha:** 2026-05-17 | **Target:** P21=Gama (preferencia binaria) | **n=402 | n_pref=32 | n_no_pref=370**
**Modelo ejecutado:** Logit (statsmodels) | **Pseudo R2 McFadden:** 0.4371 (ROBUSTO >0.4)

---

## Nota sobre RF/SHAP

scikit-learn y shap **no estan instalados** en el entorno actual. El analisis RF+SHAP esta documentado metodologicamente (diseno, hipotesis, codigo) pero sus valores numericos son `PENDIENTE_INSTALACION`.

Para activar: `pip install scikit-learn shap` — requiere autorizacion Owner (RISK-POLICY zona amarilla).

El logit fue **reproducido exitosamente** e identico al V2 (Pseudo R2 diff < 0.005). La seccion de comparativa metodologica logit vs RF/SHAP esta completa.

---

## Seccion 1 — Logit reproducido: tabla de drivers

**Modelo:** `Logit(Y_Gama) ~ X1..X10 + const`
**Y:** P21 contiene Gama (1) vs no Gama (0)
**X1-X10:** P23 asociacion Gama con cada uno de los 10 atributos (binario 0/1)
**Calidad del modelo:** Pseudo R2 McFadden = 0.4371 (ROBUSTO), LLR p = 1.63e-16

### Tabla maestra de drivers

| Atributo | OR | IC95 OR | p-value | Sig | % asociado a Gama | Interpretacion |
|---|---|---|---|---|---|---|
| **mejor_atienden** | **5.731** | **[1.608, 20.432]** | **0.007** | **SIG p<0.01** | 21.9% | Driver principal: 5.7x odds |
| **promociones** | **3.640** | **[1.126, 11.769]** | **0.031** | **SIG p<0.05** | 8.9% | Driver secundario: 3.6x odds |
| limpio_ordenado | 3.987 | [0.940, 16.913] | 0.061 | TENDENCIA p<0.10 | 31.1% | Borderline: incluir con caveat |
| mayor_categorias | 1.880 | [0.614, 5.758] | 0.269 | no sig | 17.9% | No driver independiente |
| atractiva | 1.732 | [0.527, 5.695] | 0.366 | no sig | 28.9% | No driver independiente |
| hacer_valer | 1.611 | [0.583, 4.456] | 0.358 | no sig | 11.4% | No driver independiente |
| seguro | 1.696 | [0.470, 6.128] | 0.420 | no sig | 29.6% | No driver independiente |
| mayor_calidad | 1.152 | [0.339, 3.915] | 0.821 | no sig | 26.6% | No driver independiente |
| rapidez_caja | 0.755 | [0.197, 2.898] | 0.682 | no sig | 21.1% | No driver (tendencia negativa) |
| menor_precio | 1.029 | [0.274, 3.862] | 0.966 | no sig | 7.2% | No driver (irrelevante) |

**Nota sobre IC95:** Los IC95 de los OR son amplios por n_pref=32 (REFERENCIAL). Los puntos estimados son direccionalmente robustos (convergencia triple: logit + razon espontanea + z-score). Reportar siempre OR + IC95, no solo el punto.

---

## Seccion 2 — Convergencia triple de evidencia para top drivers

Esta es la validacion mas importante del estudio: **tres metodologias independientes apuntan al mismo driver**.

| Driver | Logit OR (p) | Razon espontanea P21.1 | Z-score asociacion P23 |
|---|---|---|---|
| **Atencion (mejor_atienden)** | OR=5.73 (p=0.007) | #1 razon: ~53% de pref-Gama | Z moderado (+0.47) — sobre-indexa vs mercado |
| **Promociones** | OR=3.64 (p=0.031) | mencionada por pref-Gama | Bajo % absoluto (9%) — alta palanca de conversion |
| Limpieza y orden | OR=3.99 (p=0.061) | mencionada como higiene | Alto % asociacion (31%) — amplia base |

**Conclusion:** la convergencia en atencion es muy robusta. No es un artefacto del logit. Es el activo diferenciador mas real que tiene Gama.

---

## Seccion 3 — Tabla comparativa logit vs RF/SHAP (metodologica)

| Dimension | Logit (ejecutado) | Random Forest + SHAP (pendiente) |
|---|---|---|
| Estado | EJECUTADO — resultados arriba | PENDIENTE instalacion sklearn/shap |
| Interpretabilidad | ALTA: OR, IC95, p-values estandar | MEDIA sin SHAP; ALTA con SHAP |
| Supuesto clave | Linealidad en log-odds | Ninguno (metodo no-parametrico) |
| Multicolinealidad | Sensible (pero verificado: max corr entre predictores < 0.7) | Robusto — lo maneja internamente |
| Con n=402 y 10 pred. binarios | Apropiado (ratio 40:1, bien) | Estable con n>200; OK para explorar |
| Recomendacion con estos datos | Suficiente como modelo principal | Util como validacion de robustez |

### Hipotesis que RF+SHAP validaria (cuando se instale)

1. **Hipotesis de convergencia:** si los SHAP importance values del RF coinciden con los top-2 del logit (mejor_atienden, promociones), el logit es metodologicamente suficiente para reportar.
2. **Hipotesis de no-linealidades:** si RF revela interacciones (ej. `limpio AND atractiva` como combinacion sinergica), el logit esta subestimando ese efecto. Posible: el combo limpieza+atractiva podria ser el real driver de preferencia mas que cada uno por separado.
3. **Hipotesis de AUC:** si AUC_RF > AUC_logit + 0.05 en validacion cruzada, las no-linealidades son suficientemente importantes para reportarlas.

### Codigo de RF+SHAP (listo para ejecutar cuando se instalen librerias)

```python
# Ver 04_drivers_rf_shap.py en scripts/
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score
import shap

rf = RandomForestClassifier(n_estimators=500, max_depth=None,
                             class_weight='balanced', random_state=42)
cv_auc = cross_val_score(rf, X_df, y, cv=StratifiedKFold(5),
                          scoring='roc_auc').mean()
rf.fit(X_df, y)
explainer = shap.TreeExplainer(rf)
shap_values = explainer.shap_values(X_df)
# shap.summary_plot(shap_values[1], X_df)  # plot guardado en plots/
```

---

## Seccion 4 — Caveats del logit (para CU-6)

1. **n_pref_gama=32 (REFERENCIAL):** los OR son direccionalmente validos pero los IC95 son anchos. No interpretar OR=5.73 como "exactamente 5.73x". El rango real [1.6, 20.4] incluye valores desde moderado hasta muy alto.

2. **Desbalanceo 32:370 (~1:12):** dentro del umbral aceptable para logit estandar (peor limite recomendado: 1:20). Si en 2027 n_pref baja del 6%, considerar Firth penalized logit.

3. **Variables de asociacion P23 son autopercepcion:** el respondente marca que atributos asocia con Gama. Hay sesgo de consistencia cognitiva: el preferente de Gama puede sobre-atribuir virtudes a su marca preferida. Los OR pueden estar inflados por este sesgo.

4. **Los 7 atributos no-significativos no son "irrelevantes":** no son drivers *independientes* cuando se controlan los otros. Si se corre cada uno solo, probablemente todos son significativos. La multicolinealidad entre atributos hace que el logit multivariate distribuya el efecto en los mas diferenciadores.

5. **Recomendacion de reporteo:** mencionar los 2 drivers significativos como "drivers confirmados" y limpio_ordenado como "driver con evidencia consistente pero borderline estadistico".

---

*Producido por Cuanti V3 — 2026-05-17. JSON canonico: `CU3_drivers_20260517_v1.json`.*
*Gate Bruna: revisar seccion 4 antes de usar OR en claims publicos.*
