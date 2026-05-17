"""
05_segmentation_kmeans_lca.py — CU-4 K-means formal + LCA proxy
Proyecto: Gama Notoriedad 2026
Autor: Cuanti V3
Fecha: 2026-05-17

Proposito:
  Validacion formal del clustering exploratorio de 00_cuanti_master.py.
  K-means con silhouette coefficient + BayesianGaussianMixture como proxy LCA.

Inputs:
  - BBDD raw (via common_bbdd.py)
  - Variables: P22 Likert (8) + NSE + P33 + Pref_Gama

Outputs:
  - CU4_kmeans_lca_YYYYMMDD_v1.json
  - plots/silhouette_YYYYMMDD.png
  - plots/kmeans_profiles_YYYYMMDD.png

ESTADO: REQUIERE scikit-learn.
  pip install scikit-learn  (autorizacion Owner requerida — RISK-POLICY)

Para ejecutar:
  python 05_segmentation_kmeans_lca.py
"""

import sys
import os
import json
import datetime
import warnings

sys.stdout.reconfigure(encoding='utf-8')
warnings.filterwarnings('ignore')

FECHA   = "20260517"
VERSION = "v1"
K_RANGE = range(2, 7)
RANDOM_STATE = 42

ROOT         = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
ANALYSIS_DIR = os.path.join(ROOT, '02-analysis')
CUANTI_DIR   = os.path.join(ANALYSIS_DIR, 'cuanti')
JSON_OUT     = os.path.join(CUANTI_DIR, 'outputs', 'json')
PLOTS_DIR    = os.path.join(CUANTI_DIR, 'plots')

sys.path.insert(0, ANALYSIS_DIR)
sys.path.insert(0, os.path.dirname(__file__))
from utils import NumpyEncoder, dump_json

LIKERT_MAP = {
    'Muy Importante': 5, 'Importante': 4,
    'Algo importante': 3, 'Poco importante': 2, 'Nada Importante': 1
}

def check_sklearn():
    try:
        import sklearn
        return True, sklearn.__version__
    except ImportError:
        return False, None

if __name__ == "__main__":
    print(f"[CU-4 K-means/LCA] Iniciando — {datetime.datetime.now().isoformat()}")

    ok, version = check_sklearn()
    if not ok:
        print("  ERROR: scikit-learn no instalado.")
        print("  Accion: pip install scikit-learn  (autorizacion Owner requerida)")
        result = {"estado": "ABORTADO_DEPS_FALTANTES",
                  "accion": "pip install scikit-learn"}
        dump_json(result, os.path.join(JSON_OUT, f'CU4_kmeans_{FECHA}_{VERSION}_FAILED.json'))
        sys.exit(1)

    print(f"  scikit-learn {version}")

    import numpy as np
    import pandas as pd
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score
    from sklearn.mixture import BayesianGaussianMixture
    from sklearn.preprocessing import StandardScaler
    from common_bbdd import load_df, get_masks, COL_NSE, COL_P33

    df    = load_df()
    masks = get_masks(df)
    n     = len(df)

    # Construir matriz
    p22_cols = [c for c in df.columns if '{P22}' in c]
    p22_num  = pd.DataFrame()
    for col in p22_cols:
        key = 'P22_' + col.split(']')[-1].strip()[:20].replace(' ', '_')
        p22_num[key] = df[col].astype(str).str.strip().map(LIKERT_MAP)

    nse_num = df[COL_NSE].astype(str).str.strip().map({'C+/C': 3, 'D': 2, 'E': 1}).fillna(2.0)
    p33_num = df[COL_P33].astype(str).str.strip().apply(lambda x:
        1 if 'econ' in x.lower() and 'mucho' in x.lower() else
        2 if 'econ' in x.lower() else
        3 if 'igual' in x.lower() else
        4 if 'poco' in x.lower() and 'caro' in x.lower() else
        5 if 'mucho' in x.lower() and 'caro' in x.lower() else 3)
    pref_g  = masks['Pref-Gama'].astype(float)

    X = pd.concat([p22_num.fillna(3), nse_num.rename('NSE'),
                   p33_num.rename('P33_precio'), pref_g.rename('Pref_Gama')], axis=1).dropna()

    scaler = StandardScaler()
    X_z    = scaler.fit_transform(X)
    print(f"  Matrix: {X.shape}")

    # ── K-means con elbow + silhouette ──────────────────────────────────────
    print("  K-means evaluacion...")
    inertias    = {}
    silhouettes = {}
    for k in K_RANGE:
        km = KMeans(n_clusters=k, n_init=20, random_state=RANDOM_STATE)
        labels = km.fit_predict(X_z)
        inertias[k] = float(km.inertia_)
        if k > 1:
            silhouettes[k] = float(silhouette_score(X_z, labels, sample_size=min(400, n)))

    k_silhouette_best = max(silhouettes, key=silhouettes.get)
    print(f"  Silhouette por k: {silhouettes}")
    print(f"  k optimo (silhouette): {k_silhouette_best}")

    # Ajuste final con k optimo
    km_final = KMeans(n_clusters=k_silhouette_best, n_init=50, random_state=RANDOM_STATE)
    labels_final = km_final.fit_predict(X_z)
    X_labeled = X.copy()
    X_labeled['cluster'] = labels_final

    # Perfiles
    perfiles = {}
    for c in range(k_silhouette_best):
        sub = X_labeled[X_labeled['cluster'] == c]
        n_c = len(sub)
        perfiles[f'seg_{c+1}'] = {
            "n": n_c, "pct": round(n_c/n*100, 1),
            "NSE_promedio": round(float(sub['NSE'].mean()), 2),
            "pct_pref_gama": round(float(sub['Pref_Gama'].mean()*100), 1),
            "precio_percep": round(float(sub['P33_precio'].mean()), 2),
            "P22_medias": {col: round(float(sub[col].mean()), 2)
                          for col in p22_num.columns if col in sub.columns}
        }

    # ── Bayesian GMM como proxy LCA ─────────────────────────────────────────
    print("  BayesianGaussianMixture (proxy LCA)...")
    bgm_scores = {}
    for k in K_RANGE:
        bgm = BayesianGaussianMixture(n_components=k, covariance_type='full',
                                       n_init=5, random_state=RANDOM_STATE, max_iter=500)
        bgm.fit(X_z)
        # BIC aproximado para GMM (menor = mejor)
        n_params = k * (X_z.shape[1] + X_z.shape[1]*(X_z.shape[1]+1)//2) + k - 1
        log_lik  = bgm.score(X_z) * n
        bic      = -2 * log_lik + n_params * np.log(n)
        bgm_scores[k] = float(bic)

    k_bic_best = min(bgm_scores, key=bgm_scores.get)
    print(f"  BIC proxy por k: {bgm_scores}")
    print(f"  k optimo (BIC): {k_bic_best}")

    # ── Plots ─────────────────────────────────────────────────────────────────
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(1, 2, figsize=(12, 5))

        # Elbow
        axes[0].plot(list(inertias.keys()), list(inertias.values()), 'o-', color='#3275a8')
        axes[0].set_xlabel('k (numero de clusters)')
        axes[0].set_ylabel('Inercia (within-cluster SS)')
        axes[0].set_title('Elbow criterion — K-means')

        # Silhouette
        axes[1].plot(list(silhouettes.keys()), list(silhouettes.values()), 's-', color='#e07b39')
        axes[1].axvline(x=k_silhouette_best, linestyle='--', alpha=0.5)
        axes[1].set_xlabel('k')
        axes[1].set_ylabel('Silhouette coefficient')
        axes[1].set_title(f'Silhouette — k optimo = {k_silhouette_best}')

        plt.tight_layout()
        plot_path = os.path.join(PLOTS_DIR, f'kmeans_elbow_silhouette_{FECHA}_{VERSION}.png')
        plt.savefig(plot_path, dpi=150)
        plt.close()
        print(f"  Plot guardado: {plot_path}")
    except Exception as e:
        print(f"  Plot no generado: {e}")

    result = {
        "metadata": {"proyecto": "Gama Notoriedad 2026",
                     "fecha_ejecucion": datetime.datetime.now().isoformat(),
                     "sklearn_version": version, "n": n},
        "kmeans": {
            "inertias": {str(k): v for k, v in inertias.items()},
            "silhouettes": {str(k): v for k, v in silhouettes.items()},
            "k_optimo_silhouette": k_silhouette_best,
            "silhouette_score_optimo": silhouettes.get(k_silhouette_best),
            "perfiles": perfiles
        },
        "bgm_proxy_lca": {
            "bic_por_k": {str(k): v for k, v in bgm_scores.items()},
            "k_optimo_bic": k_bic_best
        },
        "recomendacion_k": (
            k_silhouette_best if k_silhouette_best == k_bic_best
            else f"Ambiguedad: silhouette sugiere k={k_silhouette_best}, BIC sugiere k={k_bic_best}. "
                 f"Elegir segun interpretabilidad sustantiva de perfiles."
        )
    }

    dump_json(result, os.path.join(JSON_OUT, f'CU4_kmeans_{FECHA}_{VERSION}.json'))
    print(f"\n[OK] CU-4 K-means/LCA completado.")
