"""
Descarga masiva de documentos técnicos Genteca
Destino: G:\Mi unidad\WorkspaceIA\RAG_SOURCES\
Ejecutar: python C:\WorkspaceIA\descargar_genteca.py
"""

import requests
from pathlib import Path

DESTINO_BASE = Path(r"G:\Mi unidad\WorkspaceIA\RAG_SOURCES")

ARCHIVOS = {
    "Genius": [
        ("E_GOCT.pdf",         "https://www.genteca.com.ve/biblioteca/genius/E_GOCT.pdf"),
        ("I_GOCT.pdf",         "https://genteca.com.ve/biblioteca/genius/I_GOCT.pdf"),
        ("I_GUCT_P.pdf",       "https://genteca.com.ve/biblioteca/genius/I_GUCT_P.pdf"),
        ("E_GII_P.pdf",        "https://genteca.com.ve/biblioteca/genius/E_GII_P.pdf"),
        ("I_GII_P.pdf",        "https://genteca.com.ve/biblioteca/genius/I_GII_P.pdf"),
        ("I_GI_P.pdf",         "https://genteca.com.ve/biblioteca/genius/I_GI_P.pdf"),
        ("I_GIII_P.pdf",       "https://genteca.com.ve/biblioteca/genius/I_GIII_P.pdf"),
        ("I_GSPT.pdf",         "https://genteca.com.ve/wp-content/uploads/2025/10/I_GSPT.pdf"),
        ("GIOLINK_V2.pdf",     "https://genteca.com.ve/biblioteca/genius/GIOLINK%20V2.pdf"),
        ("S_TR002.pdf",        "https://genteca.com.ve/biblioteca/genius/S_TR002.pdf"),
        ("CT_genius_V2.pdf",   "https://genteca.com.ve/catalogos/tecnicos/CT_genius_V2.pdf"),
    ],
    "Exceline_Profesional": [
        ("E_GSM-L.pdf",                    "https://genteca.com.ve/biblioteca/exceline_profesional/E_GSM-L.pdf"),
        ("E_GST-RC.pdf",                   "https://genteca.com.ve/biblioteca/exceline_profesional/E_GST-RC.pdf"),
        ("E_GST-RP.pdf",                   "https://genteca.com.ve/biblioteca/exceline_profesional/E_GST-RP.pdf"),
        ("E_GST.pdf",                      "https://genteca.com.ve/biblioteca/exceline_profesional/E_GST.pdf"),
        ("E_GCF.pdf",                      "https://www.genteca.com.ve/biblioteca/exceline_profesional/E_GCF.pdf"),
        ("E_GRF-S.pdf",                    "https://genteca.com.ve/biblioteca/exceline_profesional/E_GRF-S.pdf"),
        ("E_GTP-A.pdf",                    "https://genteca.com.ve/biblioteca/exceline_profesional/E_GTP-A.pdf"),
        ("GBC_HDE_V3.pdf",                 "https://genteca.com.ve/biblioteca/exceline_profesional/GBC_HDE_V3.pdf"),
        ("GD-HE-GMP5-01-V1.pdf",           "https://genteca.com.ve/biblioteca/exceline_profesional/GD-HE-GMP5-01-V1.pdf"),
        ("CAT_TRI_VERTICAL.pdf",           "https://www.genteca.com.ve/biblioteca/exceline_profesional/CAT_TRI_VERTICAL.pdf"),
        ("CT_excelinepro_V1.pdf",          "https://genteca.com.ve/catalogos/tecnicos/CT_excelinepro_V1.pdf"),
        ("Hoja_especificaciones_Tecnicas.pdf", "https://genteca.com.ve/biblioteca/exceline_profesional/Hoja%20especificaciones%20Tecnicas.pdf"),
        ("Nota-aplicacion-AA.pdf",         "https://genteca.com.ve/biblioteca/exceline_profesional/Nota-aplicacion-A-A.pdf"),
        ("S_CT003.pdf",                    "https://genteca.com.ve/biblioteca/exceline_profesional/S_CT003.pdf"),
        ("S_CP002.pdf",                    "https://genteca.com.ve/biblioteca/exceline_profesional/S_CP002.pdf"),
        ("GRA-MV_HDE_V7.pdf",             "https://genteca.com.ve/wp-content/uploads/2025/12/GRA-MV_HDE_V7.pdf"),
        ("GTC-MR_HDE_V6.pdf",             "https://genteca.com.ve/wp-content/uploads/2025/12/GTC-MR_HDE_V6.pdf"),
        ("I_GMS-U.pdf",                   "https://genteca.com.ve/wp-content/uploads/2025/10/I_GMS-U.pdf"),
    ],
    "Exceline": [
        ("E_GSM-RT.pdf",                  "https://www.genteca.com.ve/biblioteca/exceline/E_GSM-RT.pdf"),
        ("E_GSM-N.pdf",                   "https://www.genteca.com.ve/biblioteca/exceline/E_GSM-N.pdf"),
        ("E_GSM-RB.pdf",                  "https://genteca.com.ve/biblioteca/exceline/E_GSM-RB.pdf"),
        ("GSM-NG_HDE_V2.pdf",             "https://www.genteca.com.ve/biblioteca/exceline/GSM-NG_HDE_V2.pdf"),
        ("E_GFE-MV.pdf",                  "https://genteca.com.ve/biblioteca/exceline/E_GFE-MV.pdf"),
        ("E_GFR-MV.pdf",                  "https://genteca.com.ve/biblioteca/exceline/E_GFR-MV.pdf"),
        ("E_GFR-MV7H.pdf",               "https://genteca.com.ve/wp-content/uploads/2025/10/E_GFR-MV7H.pdf"),
        ("E_GTC-A.pdf",                   "https://genteca.com.ve/biblioteca/exceline/E_GTC-A.pdf"),
        ("E_GTC-B1L.pdf",                "https://genteca.com.ve/biblioteca/exceline/E_GTC-B1L.pdf"),
        ("G_GTC-B1L.pdf",                "https://genteca.com.ve/biblioteca/exceline/G_GTC-B1L.pdf"),
        ("GD-HE-326-01-CH-V1-E.pdf",     "https://genteca.com.ve/biblioteca/exceline/GD-HE-326-01-CH-V1-E.pdf"),
        ("GD-331-04-VE-V1-E.pdf",        "https://genteca.com.ve/biblioteca/exceline/GD-331-04-VE-V1-E%20(PAGINAS).pdf"),
        ("GD-HE-CH-V1.pdf",              "https://genteca.com.ve/biblioteca/exceline/GD-HE-CH-V1.pdf"),
        ("Hoja_Especificaciones_Regleta.pdf", "https://genteca.com.ve/biblioteca/exceline/Hoja%20de%20Especificaciones%20Regleta.pdf"),
        ("GFA-050.pdf",                  "https://genteca.com.ve/biblioteca/exceline/GFA-050.pdf"),
        ("C_002.pdf",                    "https://genteca.com.ve/biblioteca/exceline/C_002.pdf"),
        ("GSM-N-Protector-Neveras.pdf",  "https://genteca.com.ve/wp-content/uploads/2025/12/GSM-N-Protector-para-Neveras.pdf"),
        ("GSM-RE-Protector-AA.pdf",      "https://genteca.com.ve/wp-content/uploads/2025/12/GSM-RE-Protector-para-Aires-Acondicionados-y-Refrigeracion-Enchufable.pdf"),
    ],
    "Notas_Aplicacion": [
        ("NA-005-Proteccion-Integral-Motores.pdf", "https://genteca.com.ve/biblioteca/Nota_aplicacion/NA-005-Protecci%C3%B3n-IntegralMotores.pdf"),
        ("NA-003-Sistemas-Iluminacion.pdf",        "https://genteca.com.ve/wp-content/uploads/2025/10/NA-003-SistemasIluminacion.pdf"),
        ("01-GD-NA-Alternancia-3-cargas.pdf",      "https://genteca.com.ve/biblioteca/01-GD-NA-X-ATERNANCIA-DE-TRES-CARGA-ASIMETRICAS-VE-V1.pdf"),
        ("04-GD-NA-Control-vaciado-tanque.pdf",    "https://genteca.com.ve/biblioteca/04-GD-NA-X-CONTROL-DE-VACIADO-DE-TANQUE-CON-RELE-DE-NIVEL-Y-PROTECCION-DE-VOLTAJE-JUNIO-VE-V1.pdf"),
        ("09-GD-NA-Riego-electrovalvulas.pdf",     "https://genteca.com.ve/biblioteca/09-GD-NA-X-SISTEMA-DE-RIEGO-CON-ELECTROVALVULAS-VE-V1.pdf"),
        ("10-GD-NA-Hidroneumatico-2-bombas.pdf",   "https://genteca.com.ve/wp-content/uploads/2025/10/10-GD-NA-X-SISTEMA-HIDRONEHUMATICO-CON-ANTERNANCIA-DE-BOMBAS-TRIFASICAS-POR-MEDIO-DE-DOS-PRESOSTATOS-VE-V1.pdf"),
        ("16-GD-NA-Iluminacion-areas-comunes.pdf", "https://www.genteca.com.ve/biblioteca/16-GD-NA-X-CONTROL-DE-ILUMINACION-DE-AREAS-COMUNES-Y-PASILLOS-INTERNOS-VE-V1.pdf"),
        ("01-GD-NA-Alternancia-3-cargas-v2.pdf",   "https://genteca.com.ve/wp-content/uploads/2025/10/01-GD-NA-X-ATERNANCIA-DE-TRES-CARGA-ASIMETRICAS-VE-V1.pdf"),
        ("Nota-Genius-Redes-Comunicacion.pdf",     "https://genteca.com.ve/biblioteca/Nota-de-Aplicacion-Genius-Redes-Comunicacion.pdf"),
    ],
    "Catalogos": [
        ("CAT_PRO_2023_V2.pdf",               "https://genteca.com.ve/Catalogos/Comercial/CAT_PRO_2023_V2.pdf"),
        ("Catalogo-Comercial-2019.pdf",        "https://genteca.com.ve/Catalogos/Comercial/Catalogo%20Comercial%20Todas%20las%20Lineas%202019%20V2.pdf"),
        ("CatalogoMod-2021.pdf",               "https://www.genteca.com.ve/Catalogos/Comercial/CatalogoMod-06-08-2021_Ozz_baja.pdf"),
        ("catalogo-comercial-exceline.pdf",    "https://genteca.com.ve/wp-content/uploads/2025/12/catalogo-comercial-exceline.pdf"),
        ("catalogo-genius.pdf",               "https://genteca.com.ve/wp-content/uploads/2025/12/catalogo-genius.pdf"),
        ("catalogo-control-y-distribucion.pdf","https://genteca.com.ve/wp-content/uploads/2025/12/catalogo-control-y-distribucion.pdf"),
        ("CAT_TRI_VERTICAL-wp.pdf",            "https://genteca.com.ve/wp-content/uploads/2025/10/CAT_TRI_VERTICAL.pdf"),
    ],
}

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
    print(f"Destino: {DESTINO_BASE}")
    if error > 0:
        print("Los archivos con ERROR deben descargarse manualmente desde el browser.")

if __name__ == "__main__":
    main()
