import sys
import os
import json
sys.stdout.reconfigure(encoding='utf-8')

from docx import Document

carpeta = r"G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\01_De_Cora_Para_Raoul\Notoriedad V2.0\Cualitativo Gama"

# Inventario
archivos = []
try:
    for f in os.listdir(carpeta):
        ruta = os.path.join(carpeta, f)
        if os.path.isfile(ruta):
            archivos.append(f)
except Exception as e:
    print(f"ERROR listando carpeta: {e}")
    sys.exit(1)

print(f"=== INVENTARIO ===")
print(f"Total archivos: {len(archivos)}")
for i, f in enumerate(sorted(archivos)):
    fpath = os.path.join(carpeta, f)
    size = os.path.getsize(fpath)
    print(f"  [{i+1}] {f}  ({size:,} bytes)")

print()
print("=== EXTRACCION DE TEXTO ===")
print()

resultados = {}

for fname in sorted(archivos):
    fpath = os.path.join(carpeta, fname)
    ext = os.path.splitext(fname)[1].lower()

    if ext in ('.docx', '.doc'):
        try:
            doc = Document(fpath)
            parrafos = []
            for p in doc.paragraphs:
                txt = p.text.strip()
                if txt:
                    parrafos.append(txt)
            texto = "\n".join(parrafos)
            resultados[fname] = texto
            print(f"--- ARCHIVO: {fname} ---")
            print(f"Caracteres: {len(texto)}")
            print(f"Parrafos: {len(parrafos)}")
            print()
            print(texto[:500])
            print("[... continua ...]")
            print()
        except Exception as e:
            resultados[fname] = f"ERROR: {e}"
            print(f"ERROR extrayendo {fname}: {e}")
    elif ext in ('.txt', '.md'):
        try:
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f_:
                texto = f_.read()
            resultados[fname] = texto
            print(f"--- ARCHIVO: {fname} ---")
            print(f"Caracteres: {len(texto)}")
            print(texto[:500])
            print("[... continua ...]")
            print()
        except Exception as e:
            resultados[fname] = f"ERROR: {e}"
    else:
        print(f"SKIP (extension no soportada): {fname}")

# Guardar resultados completos en JSON para lectura posterior
output_path = r"C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\02-analysis\cuali_textos.json"
with open(output_path, 'w', encoding='utf-8') as jf:
    json.dump(resultados, jf, ensure_ascii=False, indent=2)

print(f"\n=== GUARDADO EN: {output_path} ===")
print(f"Total docs procesados: {len(resultados)}")
total_chars = sum(len(v) for v in resultados.values() if not v.startswith("ERROR"))
print(f"Total caracteres extraidos: {total_chars:,}")
