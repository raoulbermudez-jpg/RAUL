"""
utils.py — Utilidades compartidas para scripts Cuanti V3
Proyecto: Gama Notoriedad 2026
Autor: Cuanti (agente analitico)
Fecha: 2026-05-17

Contenido:
  - NumpyEncoder: JSON encoder para tipos numpy (bool, int64, float64)
  - dump_json: wrapper json.dump con encoder y utf-8
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

import json
import numpy as np


class NumpyEncoder(json.JSONEncoder):
    """Serializa tipos numpy a Python nativos para json.dump."""
    def default(self, obj):
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, (np.bool_,)):
            return bool(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)


def dump_json(data, path, indent=2):
    """Escribe data a path con UTF-8 y NumpyEncoder."""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=indent, cls=NumpyEncoder)


# ─── EXTENSION V4 WoW — carga estandarizada BBDD 2025 ───────────────────────

BBDD_2025_PATH = (
    'G:/Mi unidad/RAUL/colaboradores/Genteca/Cora-Urrea/'
    '01_De_Cora_Para_Raoul/Notoriedad V2.0/Notoriedad 2025.xlsx'
)
SHEET_2025 = 'NotoriedadVF2V23_SPSS2'

# Nota: @PONDERAR_1 = todo cero en BBDD 2025. Ver decision D-CU7-001 en
# CU7_wow_results_20260517_v1.json. weighted=True es parametro de firma
# para compatibilidad futura cuando exista un factor de ponderacion valido.
def load_bbdd_2025(weighted=False, path=None, sheet=None):
    """
    Carga BBDD Notoriedad 2025 en DataFrame estandarizado.

    Parametros:
      weighted (bool): Si True, aplicar @PONDERAR_1 como peso.
                       ACTUALMENTE NO OPERATIVO — @PONDERAR_1 = todo cero.
                       Documentado en D-CU7-001.
      path (str): Override de path. Default: BBDD_2025_PATH.
      sheet (str): Override de hoja. Default: SHEET_2025.

    Returns:
      df (pd.DataFrame): BBDD 2025 con columnas NSE_harm y EDAD_harm.
      meta (dict): Metadatos (n, cols, ponderacion aplicada, deff).

    Columnas demograficas clave:
      COL_NSE_25  = 'NSE'              (C+, C, D, E)
      COL_NSE_HARM= 'NSE_harm'         (C+/C, D, E — harmonizada con 2026)
      COL_MUN_25  = 'V535'             (Municipio)
      COL_GEN_25  = 'GEN'              (Genero)
      COL_EDAD_25 = 'EDAD'             (Grupo edad)
      PONDER_COL  = '@PONDERAR_1'      (Factor de ponderacion — vacio)
    """
    import pandas as pd

    p = path or BBDD_2025_PATH
    s = sheet or SHEET_2025
    df = pd.read_excel(p, sheet_name=s, engine='openpyxl')

    # NSE harmonization: C+/C para C+ y C
    def _nse_harm(v):
        v = str(v).strip()
        if v in ('C+', 'C'): return 'C+/C'
        return v if v in ('D', 'E') else 'Otro'

    df['NSE_harm'] = df['NSE'].apply(_nse_harm)

    # Edad groups
    def _edad_harm(v):
        v = str(v).strip()
        if '25 a 34' in v: return '25-34'
        if '35 a 44' in v: return '35-44'
        if '45 a 54' in v: return '45-54'
        if '55' in v or '64' in v: return '55-64'
        return 'Otro'

    df['EDAD_harm'] = df['EDAD'].apply(_edad_harm)

    # Municipio harmonization
    def _mun_harm(v):
        v = str(v).strip()
        mapping = {
            'Baruta': 'Baruta', 'Sucre': 'Sucre', 'Chacao': 'Chacao',
            'Libertador': 'Libertador', 'El Hatillo': 'El Hatillo',
            'FORANEOS': 'FORANEOS', 'Foraneos': 'FORANEOS'
        }
        return mapping.get(v, 'Otro')

    df['MUN_harm'] = df['V535'].apply(_mun_harm)

    # Check weight
    w = df['@PONDERAR_1']
    w_ok = float(w.max()) > 0

    if weighted and w_ok:
        deff = None  # Would compute if weights varied
        nota_pond = 'Ponderacion aplicada con @PONDERAR_1'
    else:
        nota_pond = 'Sin ponderacion — @PONDERAR_1 vacia (todos cero) — Decision D-CU7-001'
        deff = 1.0

    meta = {
        'n': len(df),
        'cols': len(df.columns),
        'ponderacion_aplicada': weighted and w_ok,
        'deff': deff,
        'nota_ponderacion': nota_pond,
        'nse_dist': df['NSE_harm'].value_counts().to_dict(),
        'mun_dist': df['MUN_harm'].value_counts().to_dict(),
    }
    return df, meta
