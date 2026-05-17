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
