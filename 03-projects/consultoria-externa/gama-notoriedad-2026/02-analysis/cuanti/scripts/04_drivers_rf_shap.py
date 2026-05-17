"""
04_drivers_rf_shap.py — CU-3 RF + SHAP Analysis
Proyecto: Gama Notoriedad 2026
Autor: Cuanti V3
Fecha: 2026-05-17

Proposito:
  Reproducir el analisis de drivers con Random Forest + SHAP como validacion
  del logit ejecutado en 00_cuanti_master.py.
  Compara: AUC logit vs AUC RF, top features logit vs top SHAP importances.

Inputs:
  - BBDD raw: 01-data-raw/NUEVO BBDD Notoriedad 2026.xlsx
  - X_df: P23 asociaciones Gama (10 variables binarias)
  - y: P21=Gama (binario)

Outputs:
  - CU3_rf_shap_YYYYMMDD_v1.json
  - plots/shap_summary.png
  - plots/shap_beeswarm.png

ESTADO: REQUIERE scikit-learn y shap instalados.
  pip install scikit-learn shap  (requiere autorizacion Owner segun RISK-POLICY)

Para ejecutar:
  python 04_drivers_rf_shap.py
"""

import sys
import os
import json
import datetime
import warnings

sys.stdout.reconfigure(encoding='utf-8')
warnings.filterwarnings('ignore')

# ─── CONSTANTES ─────────────────────────────────────────────────────────────
FECHA   = "20260517"
VERSION = "v1"
N_TREES = 500
RANDOM_STATE = 42
N_FOLDS = 5
ALPHA   = 0.05

ROOT         = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
ANALYSIS_DIR = os.path.join(ROOT, '02-analysis')
CUANTI_DIR   = os.path.join(ANALYSIS_DIR, 'cuanti')
JSON_OUT     = os.path.join(CUANTI_DIR, 'outputs', 'json')
PLOTS_DIR    = os.path.join(CUANTI_DIR, 'plots')

sys.path.insert(0, ANALYSIS_DIR)
sys.path.insert(0, os.path.dirname(__file__))  # para utils

from utils import NumpyEncoder, dump_json

# Mapeo exacto P23 Gama (sin ambiguedad por keyword)
P23_GAMA_PREFIXES = {
    'mayor_categorias': '{P23:1}',
    'mayor_calidad':    '{P23:2}',
    'menor_precio':     '{P23:3}',
    'mejor_atienden':   '{P23:4}',
    'promociones':      '{P23:5}',
    'atractiva':        '{P23:6}',
    'limpio_ordenado':  '{P23:8}',
    'seguro':           '{P23:12}',
    'rapidez_caja':     '{P23:13}',
    'hacer_valer':      '{P23:21}',
}

def check_dependencies():
    """Verifica que sklearn y shap esten instalados."""
    try:
        import sklearn
        import shap
        return True, sklearn.__version__, shap.__version__
    except ImportError as e:
        return False, None, str(e)

if __name__ == "__main__":
    print(f"[CU-3 RF+SHAP] Iniciando — {datetime.datetime.now().isoformat()}")

    deps_ok, skl_v, shap_v = check_dependencies()
    if not deps_ok:
        print(f"  ERROR: scikit-learn o shap no instalados.")
        print(f"  Mensaje: {shap_v}")
        print(f"  Accion: pip install scikit-learn shap  (requiere autorizacion Owner)")
        result = {
            "estado": "ABORTADO_DEPS_FALTANTES",
            "error": shap_v,
            "accion_requerida": "pip install scikit-learn shap"
        }
        dump_json(result, os.path.join(JSON_OUT, f'CU3_rf_shap_{FECHA}_{VERSION}_FAILED.json'))
        sys.exit(1)

    print(f"  scikit-learn {skl_v} | shap {shap_v}")

    import numpy as np
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import StratifiedKFold, cross_val_score
    from sklearn.metrics import roc_auc_score
    import shap
    import statsmodels.api as sm

    from common_bbdd import load_df, get_masks

    df    = load_df()
    masks = get_masks(df)
    n     = len(df)

    # Construir X e y
    X_data = {}
    for attr, prefix in P23_GAMA_PREFIXES.items():
        cands = [c for c in df.columns if prefix in c and 'Gama' in c]
        if cands:
            s = df[cands[0]]
            X_data[attr] = (s.notna() & (s.astype(str).str.strip() != '') & (s != 0)).astype(int)
        else:
            print(f"  ADVERTENCIA: columna no encontrada para {attr} ({prefix})")
            X_data[attr] = pd.Series(0, index=df.index)

    X_df = pd.DataFrame(X_data)
    y    = masks['Pref-Gama'].astype(int)

    print(f"  n={n}, n_pref={int(y.sum())}, n_features={X_df.shape[1]}")

    # ── Logit AUC (baseline) ────────────────────────────────────────────────
    print("  Calculando AUC logit...")
    X_const = sm.add_constant(X_df.astype(float))
    logit_model = sm.Logit(y.astype(float), X_const).fit(disp=0)
    logit_proba = logit_model.predict(X_const)
    auc_logit = roc_auc_score(y, logit_proba)
    print(f"  AUC logit = {auc_logit:.4f}")

    # ── Random Forest ────────────────────────────────────────────────────────
    print(f"  Entrenando RF (n_estimators={N_TREES})...")
    rf = RandomForestClassifier(
        n_estimators=N_TREES,
        max_depth=None,
        class_weight='balanced',
        random_state=RANDOM_STATE,
        n_jobs=-1
    )

    # Cross-validation AUC
    cv = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=RANDOM_STATE)
    auc_rf_cv = cross_val_score(rf, X_df, y, cv=cv, scoring='roc_auc')
    print(f"  AUC RF CV (mean ± std) = {auc_rf_cv.mean():.4f} ± {auc_rf_cv.std():.4f}")

    # Fit en toda la muestra para SHAP
    rf.fit(X_df, y)

    # Gini importance (nativa del RF)
    gini_imp = dict(zip(X_df.columns, rf.feature_importances_))

    # ── SHAP ────────────────────────────────────────────────────────────────
    print("  Calculando SHAP values...")
    explainer   = shap.TreeExplainer(rf)
    shap_values = explainer.shap_values(X_df)

    # shap_values[1] = shap values para clase positiva (pref Gama = 1)
    shap_pos = shap_values[1] if isinstance(shap_values, list) else shap_values
    mean_abs_shap = {attr: float(abs(shap_pos[:, i]).mean())
                     for i, attr in enumerate(X_df.columns)}

    # Ranking por SHAP
    shap_ranking = sorted(mean_abs_shap.items(), key=lambda x: -x[1])

    # ── Plots ────────────────────────────────────────────────────────────────
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        # SHAP summary bar plot
        fig, ax = plt.subplots(figsize=(10, 6))
        attrs = [r[0] for r in shap_ranking]
        vals  = [r[1] for r in shap_ranking]
        ax.barh(attrs[::-1], vals[::-1], color='#3275a8')
        ax.set_xlabel('Mean |SHAP value|')
        ax.set_title('Feature Importance (SHAP) — Drivers de Preferencia Gama')
        plt.tight_layout()
        plot_path = os.path.join(PLOTS_DIR, f'shap_bar_{FECHA}_{VERSION}.png')
        plt.savefig(plot_path, dpi=150)
        plt.close()
        print(f"  Plot guardado: {plot_path}")

        # SHAP beeswarm
        shap.summary_plot(shap_pos, X_df, show=False)
        bee_path = os.path.join(PLOTS_DIR, f'shap_beeswarm_{FECHA}_{VERSION}.png')
        plt.savefig(bee_path, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"  Beeswarm guardado: {bee_path}")
    except Exception as e:
        print(f"  Plots no generados (matplotlib no disponible o error): {e}")

    # ── Comparativa logit vs RF/SHAP ─────────────────────────────────────────
    logit_ranking = [
        ('mejor_atienden',  5.731, 0.007),
        ('promociones',     3.640, 0.031),
        ('limpio_ordenado', 3.987, 0.061),
    ]
    convergencia = []
    for rank_pos, (attr, shap_imp) in enumerate(shap_ranking[:3], 1):
        logit_match = any(l[0] == attr for l in logit_ranking)
        convergencia.append({
            "rank_shap": rank_pos, "atributo": attr,
            "mean_abs_shap": round(shap_imp, 4),
            "en_top3_logit": logit_match
        })

    auc_diff = auc_rf_cv.mean() - auc_logit
    nonlinearity_relevant = abs(auc_diff) > 0.05

    result = {
        "metadata": {
            "proyecto": "Gama Notoriedad 2026",
            "fecha_ejecucion": datetime.datetime.now().isoformat(),
            "sklearn_version": skl_v, "shap_version": shap_v,
            "n": n, "n_pref_gama": int(y.sum())
        },
        "auc_comparacion": {
            "auc_logit": round(float(auc_logit), 4),
            "auc_rf_cv_mean": round(float(auc_rf_cv.mean()), 4),
            "auc_rf_cv_std": round(float(auc_rf_cv.std()), 4),
            "diferencia_rf_minus_logit": round(float(auc_diff), 4),
            "no_linealidades_relevantes": nonlinearity_relevant,
            "interpretacion": (
                "AUC RF > AUC Logit + 0.05: no-linealidades importan, reportar RF+SHAP"
                if nonlinearity_relevant else
                "AUC RF ~ AUC Logit: logit es suficiente como modelo principal"
            )
        },
        "shap_importances": mean_abs_shap,
        "shap_ranking_top5": shap_ranking[:5],
        "gini_importances": gini_imp,
        "convergencia_logit_vs_shap": convergencia,
        "conclusion": (
            "Los top-3 SHAP coinciden con los top-3 logit: logit es suficiente y robusto."
            if all(c['en_top3_logit'] for c in convergencia) else
            "Divergencia entre SHAP y logit: RF capta no-linealidades importantes. Reportar RF+SHAP."
        )
    }

    out_path = os.path.join(JSON_OUT, f'CU3_rf_shap_{FECHA}_{VERSION}.json')
    dump_json(result, out_path)
    print(f"  Guardado: {out_path}")
    print(f"\n[OK] CU-3 RF+SHAP completado.")
    print(f"  AUC logit={result['auc_comparacion']['auc_logit']:.4f} | AUC RF={result['auc_comparacion']['auc_rf_cv_mean']:.4f}")
    print(f"  Conclusion: {result['conclusion']}")
