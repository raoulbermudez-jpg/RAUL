"""
Descarga masiva Genteca — PARTE 2
URLs corregidas segun mapa de Comet (archivos movidos a WordPress)
Ejecutar: python C:\WorkspaceIA\descargar_genteca_v2.py
"""

import requests
from pathlib import Path

DESTINO_BASE = Path(r"G:\Mi unidad\WorkspaceIA\RAG_SOURCES")

ARCHIVOS = {
    "Exceline": [
        ("E_GSM-RB-AltaCarga.pdf",   "https://genteca.com.ve/wp-content/uploads/2025/12/GSM-RB-Protector-para-Aires-Acondicionados-y-Refrigeracion-de-Alta-Carga.pdf"),
        ("GSM-NG_HDE_V2.pdf",        "https://genteca.com.ve/wp-content/uploads/2025/11/GSM-NG_HDE_V2.pdf"),
        ("E_GSM-AS.pdf",             "https://genteca.com.ve/wp-content/uploads/2025/12/GSM-AS-Protector-de-voltaje-para-aires-acondicionados-tipo-consolaSplit.pdf"),
        ("GTC-B1C-MV-Programador.pdf","https://genteca.com.ve/wp-content/uploads/2025/12/GTC-B1C-MV-Programador-Horario-DiarioSemanal-de-Control-para-Cargas-Electricas.pdf"),
        ("GTC-B1L-MV-Programador.pdf","https://genteca.com.ve/wp-content/uploads/2025/12/GTC-B1L-MV-Programador-Horario-Digital-de-Bornera-para-Equipos-Electricos-en-General-220V.pdf"),
        ("GVF-HI-Flotante.pdf",      "https://genteca.com.ve/wp-content/uploads/2025/10/GVF-HI-050-075-Flotante-mecanico.pdf"),
        ("C_003.pdf",                "https://genteca.com.ve/wp-content/uploads/2025/10/C_003.pdf"),
        ("G_GTC-B1L.png",            "https://genteca.com.ve/wp-content/uploads/2025/10/G_GTC-B1L-scaled.png"),
    ],
    "Exceline_Profesional": [
        ("GSC-MB-Sobrecarga-Trifasico.pdf", "https://genteca.com.ve/wp-content/uploads/2025/12/GSC-MB-Protector-de-Sobrecarga-Trifasico-para-Motores-y-Bombas.pdf"),
    ],
    "Catalogos": [
        ("CAT_TRI_1_IMP.pdf",  "https://genteca.com.ve/wp-content/uploads/2025/10/CAT_TRI_1_IMP.pdf"),
        ("CAT_BRE_1.pdf",      "https://genteca.com.ve/wp-content/uploads/2025/10/CAT_BRE_1.pdf"),
    ],
}

# Estos 3 no estan publicados — requieren solicitud a info@genteca.com.ve
NO_DISPONIBLES = [
    "GD-HE-CH-V1.pdf         — Documentacion GBP-060/GBP-065",
    "GD-331-04-VE-V1-E.pdf   — Kit GBI-P060 doc 1",
    "GD-HE-326-01-CH-V1-E.pdf — Kit GBI-P060 doc 2",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"
}

def descargar(nombre, url, carpeta):
    destino = carpeta / nombre
    if destino.exists():
        print(f"  [YA EXISTE]  {nombre}")
        return "existe"
    try:
        r = requests.get(url, headers=HEADERS, timeout=30, stream=True)
        if r.status_code == 200:
            with open(destino, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"  [OK]         {nombre}")
            return "ok"
        else:
            print(f"  [ERROR {r.status_code}]  {nombre}  ->  {url}")
            return "error"
    except Exception as e:
        print(f"  [EXCEPCION]  {nombre}  ->  {e}")
        return "error"

def main():
    ok = error = existe = 0
    for categoria, archivos in ARCHIVOS.items():
        carpeta = DESTINO_BASE / categoria
        carpeta.mkdir(parents=True, exist_ok=True)
        print(f"\n=== {categoria} ({len(archivos)} archivos) ===")
        for nombre, url in archivos:
            resultado = descargar(nombre, url, carpeta)
            if resultado == "ok":      ok += 1
            elif resultado == "error": error += 1
            else:                      existe += 1

    print(f"\n{'='*50}")
    print(f"RESUMEN: {ok} descargados | {existe} ya existian | {error} errores")
    print(f"\nArchivos NO disponibles online (solicitar a info@genteca.com.ve):")
    for item in NO_DISPONIBLES:
        print(f"  - {item}")

if __name__ == "__main__":
    main()
