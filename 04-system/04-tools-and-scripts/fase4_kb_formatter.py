"""
fase4_kb_formatter.py
Fase 4: Convierte archivos de staging (texto extraído) → entradas KB estructuradas
Genteca Knowledge Base — Sistema /RAUL/

Uso:
  python fase4_kb_formatter.py              # procesa todos los pendientes
  python fase4_kb_formatter.py --dry-run    # solo estima cantidad y costo
  python fase4_kb_formatter.py --limit 50   # procesa solo 50 archivos (prueba)
  python fase4_kb_formatter.py --reset      # borra el progreso y empieza de cero
"""

import os
import sys
import json
import time
import re
import argparse
from pathlib import Path
from datetime import datetime
import logging

# ── Configuración ──────────────────────────────────────────────────────────────
STAGING       = Path("C:/RAUL/01-inbox/03-raw-sources/genteca/pendrive-D")
KB_SPECS      = Path("C:/RAUL/02-knowledge-base/02-domains/01-genteca/specs")
INDEXES_DIR   = Path("C:/RAUL/04-system/05-indexes")
PROGRESS_FILE = INDEXES_DIR / "fase4_progress.json"
LOG_FILE      = INDEXES_DIR / f"fase4_{datetime.now().strftime('%Y%m%d_%H%M')}.log"
ENV_FILE      = Path("C:/RAUL/.env")

MODEL         = "claude-haiku-4-5-20251001"
MIN_CHARS     = 300    # archivos con menos contenido útil se omiten
BATCH_SIZE    = 5      # archivos por lote antes de pausa
BATCH_DELAY   = 1.5    # segundos entre lotes (respetar rate limits)

LINEA_LABEL = {
    "exceline":             "Exceline",
    "exceline-profesional": "Exceline Profesional",
    "genius":               "Genius",
}

# ── Logging ────────────────────────────────────────────────────────────────────
INDEXES_DIR.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger(__name__)


# ── API Key ────────────────────────────────────────────────────────────────────
def get_api_key() -> str:
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if key:
        return key
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("ANTHROPIC_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return ""


# ── Helpers ────────────────────────────────────────────────────────────────────
def infer_doc_type(filename: str) -> str:
    f = filename.lower()
    if any(x in f for x in ["hde", "spec", "especificacion", "hoja"]):
        return "hoja-especificaciones"
    if any(x in f for x in ["cat", "catalogo"]):
        return "catalogo"
    if any(x in f for x in ["man", "manual", "inst", "guia-inst"]):
        return "manual"
    if any(x in f for x in ["na-", "nota", "aplicacion"]):
        return "nota-aplicacion"
    if any(x in f for x in ["gui", "prog", "programacion"]):
        return "guia-programacion"
    return "otro"


def extract_product_code(text: str) -> str:
    pattern = r'\b(G[A-Z]{1,3}-[A-Z0-9]{1,6}(?:-[A-Z0-9]+)?)\b'
    matches = re.findall(pattern, text[:1000])
    return matches[0] if matches else "N/A"


def content_chars(raw: str) -> int:
    lines = raw.splitlines()
    content = "\n".join(l for l in lines if not l.startswith("[") and l.strip())
    return len(content)


def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    return {"done": [], "skipped": [], "errors": []}


def save_progress(prog: dict):
    PROGRESS_FILE.write_text(json.dumps(prog, ensure_ascii=False, indent=2), encoding="utf-8")


def kb_slug_exists(slug: str) -> bool:
    pattern = f"*_{slug}.md"
    return bool(list(KB_SPECS.glob(pattern)))


# ── Prompt ─────────────────────────────────────────────────────────────────────
SYSTEM = """Eres un procesador de documentos técnicos para la Knowledge Base de Genteca (empresa venezolana de protección eléctrica).

Recibirás texto extraído de un documento de la línea Exceline, Exceline Profesional o Genius.

Genera un archivo Markdown con este formato EXACTO:

---
title: "[nombre del producto o documento]"
type: Technical
source: "[nombre archivo original]"
product_line: "[línea indicada]"
document_type: "[hoja-especificaciones|catalogo|manual|nota-aplicacion|guia-programacion|otro]"
product_code: "[código del producto, ej: GSM-LPM, GST-RR, o N/A]"
date_processed: "[FECHA_HOY]"
---

# [Título principal]

[Contenido limpio y estructurado]

Reglas:
- Elimina artefactos de OCR obvios: letras sueltas verticales, texto espejado, coordenadas de diseño gráfico
- Mantén TODA la información técnica: características, especificaciones, normas, rangos, tablas
- Usa headers ## para secciones si el original las tiene
- NO inventes ni agregues información que no esté en el texto fuente
- Devuelve SOLO el Markdown, sin explicaciones adicionales"""


def build_user_msg(raw: str, linea: str, today: str) -> str:
    return f"LINEA: {LINEA_LABEL.get(linea, linea)}\nFECHA_HOY: {today}\n\n{raw[:6000]}"


# ── Procesar un archivo ────────────────────────────────────────────────────────
def process_file(client, staging_path: Path, linea: str, today: str) -> tuple[str, str]:
    raw = staging_path.read_text(encoding="utf-8", errors="ignore")

    # Filtros rápidos
    if raw.startswith("[PDF_IMAGEN_SOLO]"):
        return "skip", "imagen-solo"
    if content_chars(raw) < MIN_CHARS:
        return "skip", "contenido-corto"

    slug = staging_path.stem
    if kb_slug_exists(slug):
        return "skip", "ya-en-kb"

    # Llamada a la API
    doc_type = infer_doc_type(staging_path.name)
    product_code = extract_product_code(raw)

    msg = build_user_msg(raw, linea, today)
    response = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        system=SYSTEM,
        messages=[{"role": "user", "content": msg}],
    )
    md_content = response.content[0].text.strip()

    # Nombre de archivo de salida
    out_name = f"{today}_{doc_type}_{linea}-{slug}.md"
    out_path = KB_SPECS / out_name
    out_path.write_text(md_content, encoding="utf-8")

    return "done", out_name


# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--reset", action="store_true")
    args = parser.parse_args()

    api_key = get_api_key()
    if not api_key and not args.dry_run:
        log.error("ANTHROPIC_API_KEY no encontrada. Configúrala como variable de entorno o en C:\\RAUL\\.env")
        sys.exit(1)

    # Recolectar archivos pendientes
    all_files = []
    for linea in ["exceline", "exceline-profesional", "genius"]:
        folder = STAGING / linea
        if folder.exists():
            for f in sorted(folder.glob("*.txt")):
                all_files.append((f, linea))

    log.info(f"Archivos en staging: {len(all_files)}")

    if args.reset and PROGRESS_FILE.exists():
        PROGRESS_FILE.unlink()
        log.info("Progreso reiniciado.")

    prog = load_progress()
    done_set = set(prog["done"])
    skip_set = set(prog["skipped"])

    pending = [(f, l) for f, l in all_files if f.name not in done_set and f.name not in skip_set]
    log.info(f"Pendientes: {len(pending)} | Ya procesados: {len(done_set)} | Omitidos antes: {len(skip_set)}")

    if args.limit > 0:
        pending = pending[:args.limit]
        log.info(f"Modo limitado: procesando {len(pending)}")

    if args.dry_run:
        # Estimar cuántos pasarían el filtro
        rich = 0
        for f, l in pending[:500]:  # muestra en 500
            try:
                raw = f.read_text(encoding="utf-8", errors="ignore")
                if not raw.startswith("[PDF_IMAGEN_SOLO]") and content_chars(raw) >= MIN_CHARS:
                    rich += 1
            except Exception:
                pass
        ratio = rich / min(len(pending), 500)
        estimated_rich = int(len(pending) * ratio)
        cost_usd = estimated_rich * 1600 / 1_000_000 * 0.80 + estimated_rich * 600 / 1_000_000 * 4.0
        log.info(f"--- DRY RUN ---")
        log.info(f"Archivos ricos estimados: {estimated_rich} de {len(pending)}")
        log.info(f"Costo estimado Haiku: ~${cost_usd:.2f} USD")
        log.info(f"Tiempo estimado (~{BATCH_DELAY}s/lote de {BATCH_SIZE}): ~{int(estimated_rich/BATCH_SIZE*BATCH_DELAY/60)} minutos")
        return

    import anthropic as ant
    client = ant.Anthropic(api_key=api_key)

    today = datetime.now().strftime("%Y-%m-%d")
    done_count = skipped_count = error_count = 0

    log.info("=" * 60)
    log.info(f"FASE 4 — Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log.info("=" * 60)

    for i, (f_path, linea) in enumerate(pending, 1):
        try:
            status, detail = process_file(client, f_path, linea, today)
            if status == "done":
                done_count += 1
                prog["done"].append(f_path.name)
                log.info(f"[{i}/{len(pending)}] OK  {f_path.name} → {detail}")
            else:
                skipped_count += 1
                prog["skipped"].append(f_path.name)
                log.info(f"[{i}/{len(pending)}] SKIP ({detail}) {f_path.name}")

        except Exception as e:
            error_count += 1
            prog["errors"].append({"file": f_path.name, "error": str(e)})
            log.error(f"[{i}/{len(pending)}] ERROR {f_path.name}: {e}")

        # Guardar progreso y pausar cada lote
        if i % BATCH_SIZE == 0:
            save_progress(prog)
            time.sleep(BATCH_DELAY)

        if i % 100 == 0:
            log.info(f"--- Checkpoint: OK={done_count} | Skip={skipped_count} | Error={error_count} ---")

    save_progress(prog)

    log.info("=" * 60)
    log.info(f"FASE 4 COMPLETA — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log.info(f"Procesados: {done_count} | Omitidos: {skipped_count} | Errores: {error_count}")
    log.info(f"KB actualizado: {KB_SPECS}")
    log.info("=" * 60)


if __name__ == "__main__":
    main()
