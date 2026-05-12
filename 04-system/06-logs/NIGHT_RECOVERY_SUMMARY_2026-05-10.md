# Resumen sesión nocturna — Recuperación HDE+MAN imagen-solo

**Período:** 2026-05-09 22:00 → 2026-05-10 02:45
**Outcome:** ✅ 100% completado, 0 errores residuales

---

## Lo que se logró

| Métrica | Valor |
|---|---|
| KB Genteca specs antes  | 2.116 .md |
| KB Genteca specs ahora  | **2.237 .md** |
| Specs nuevas en KB hoy  | **+121** |
| Archivos OCR'd          | 102 (los 2 respaldos resultaron ser duplicados, descartados post-OCR) |
| Errores conexión Haiku  | 14 (todos recuperados con split) |
| Partes generadas (split)| 33 |
| Errores residuales      | **0** |

### Distribución de los 121 specs nuevos

| Por línea | Cuenta | | Por tipo doc | Cuenta |
|---|---|---|---|---|
| Genius              | 54 | | Manual                  | 47 |
| Exceline            | 47 | | Hoja-especificaciones   | 42 |
| Exceline-Profesional| 20 | | Otro (clasif. subóptima)| 32 |

`version_status` poblado en frontmatter:
- `vigente`: ~80 (HDE/MAN en carpetas activas del pendrive)
- `historica`: ~41 (HDE/MAN solo en `\Versiones anteriores\` — productos legacy o docs pre-2008)

---

## Pipeline ejecutado

```
1. Inventario pendrive D:                          17.017 archivos
   ├─ Procesables texto                             4.745 (ya en staging desde 2026-05-08)
   ├─ Imágenes assets                               2.232 (catalogado)
   └─ Diseño puro                                   7.127 (catalogado)

2. Identificación HDE+MAN imagen-solo:               108 candidatos
   - 73 HDE + 35 MAN
   - 47 Exceline / 21 Exceline-Prof / 40 Genius

3. Refinamiento de selección (b):                   108 → 107
   - -1 AppleDouble Mac (._*.pdf basura)

4. Dedup por documento lógico:                      107 → 102 + 2 respaldos
   - 99 clusters únicos directos
   - 3 clusters multi-versión resueltos por mtime+versión
   - 5 versiones obsoletas descartadas
   - +2 respaldos de tamaño dispar (validados como duplicados después)

5. OCR Tesseract spa+eng @ 300 DPI:                 104/104 OK (17 min)
   - Validación piloto: 5 archivos, calidad ⭐⭐⭐⭐+
   - Ningún error en batch

6. Fase 4 Haiku → KB:                               88 OK + 14 errores connection
   - Causa: chars OCR > 20K en manuales largos saturaba el SDK
   - Errores 100% en manuales Genius de 6-10+ páginas

7. Recovery con splitter (bin-pack por chars):       14 → 33 partes (≤15K c/u)
   - Sin re-OCR, split por marcadores `--- PAGE N ---` existentes
   - Backup de originales como .pre_split_bak

8. Fase 4 sobre las 33 partes:                      33/33 OK (21 min, 0 errores)

9. Limpieza post-procesamiento:                     121/121 archivos
   - Strip de wrapper `` ```markdown ... ``` `` que Haiku agregaba
```

---

## Cambios en el repo

### Modificado
- [`04-system/04-tools-and-scripts/fase4_kb_formatter.py`](../04-tools-and-scripts/fase4_kb_formatter.py)
  - System prompt ahora maneja header `[VERSION_STATUS:]` → frontmatter `version_status` field
  - System prompt ahora elimina marcadores `--- PAGE N ---` del body
  - Truncación input: `6000 → 50000` chars (para acomodar manuales OCR'd)
  - max_tokens: `2048 → 8192` (para outputs largos)

### Nuevos artefactos en `04-system/06-logs/`
- `ocr_candidates_hde_man.{json,csv}` — lista inicial 108 candidatos
- `ocr_candidates_hde_man_v2.{json,csv}` — re-scoreada con penalización de carpetas obsoletas
- `ocr_candidates_final.json` — 102 ganadores tras dedup por versión
- `ocr_dedup_report.md` — clusters multi-versión y decisiones
- `ocr_batch_20260510_0024.log` — log OCR Tesseract (104 archivos)
- `ocr_split_recovery_20260510_0216.log` — log primer intento splitter (page-based)
- `split_by_chars_20260510_0220.log` — log segundo splitter (char-based, exitoso)
- `fase4_20260510_0049.log` — fase 4 inicial (88 OK, 14 errores)
- `fase4_20260510_0221.log` — fase 4 sobre partes (33/33 OK)
- `fase4_progress.json.pre_ocr_bak` — backup pre-recovery
- `fase4_progress.json.pre_split_bak` — backup pre-clean errors

### Scripts en `04-system/07-temp/ocr_pilot/`
- `run_ocr.py` — OCR piloto 5 archivos (validación inicial)
- `run_ocr_batch.py` — OCR batch 104 archivos
- `dedup_versions.py` — clustering por versión lógica
- `ocr_split_recovery.py` — splitter v1 (por páginas, threshold 8 — incompleto)
- `split_by_chars.py` — splitter v2 (bin-pack por chars, threshold 15K — exitoso)
- `strip_md_fence.py` — limpieza post-procesamiento

### Tessdata local (no en git, fuera de tracked dirs)
- `04-system/07-temp/tessdata/` — 3.9 MB eng + 2.2 MB spa + 10 MB osd
- Permite usar Tesseract sin tocar Program Files

---

## Lo que NO se hizo (pendiente decisión Owner)

### 1. Reclasificar 32 specs `_otro_` → `_hoja-especificaciones_`
Causa: heurística `infer_doc_type` busca "hde" en filename pero estos archivos usan prefijo "he-" (ej. `gd-he-122`, `gd-he-261`). Son HDE legítimas mal clasificadas.

**Acción sugerida:** sweep batch que renombre archivos cuyo `document_type` en frontmatter sea `hoja-especificaciones` pero cuyo prefijo de nombre sea `_otro_`. ~5 min de scripting.

### 2. ~691 archivos `contenido-corto` (skipped antes)
Fragmentos cortos de texto extraído de etiquetas/artes (códigos, voltajes, fechas). Decisión previa: no recuperar — su info útil ya vive en el HDE canónico.

### 3. ~1.227 imagen-solo restantes (ETQ/GLA/PAD)
Artes de etiqueta/empaque/tampografía. Decisión previa: no recuperar como specs — pertenecen al catálogo de assets.

### 4. ~33 'otros' borderline 300 chars
Decisión previa: filtro `ya-en-kb` funciona bien, no recuperar.

### 5. 355 entradas históricas en `progress.json` errors[]
Son las del incidente "credit balance too low" del 2026-05-09. Todas reprocesadas exitosamente y ahora en `done[]`. Las entradas en `errors[]` están duplicadas (también en done) — solo ruido histórico. Recomiendo limpieza simple cuando lo decidas.

---

## Notas técnicas para próximos batches

1. **Splitter v2 (`split_by_chars.py`) es el camino**. Rápido (sin re-OCR), evita Connection errors, balancea bins por chars respetando boundaries de página.

2. **Threshold 15K chars/parte funciona bien con Haiku 4.5 + max_tokens 8192**. No bajar mucho más — generaría partes excesivamente fragmentadas. No subir más — vuelve el riesgo de timeout.

3. **Patrón de errores Connection**: empíricamente Haiku da Connection error en input >~20K chars + output >~5K tokens. El splitter v2 evita ese régimen.

4. **`encoding=utf-8-sig`** al leer JSONs guardados con PowerShell (`Set-Content -Encoding utf8` añade BOM). Para escribir sin BOM en PowerShell: `[System.IO.File]::WriteAllText(path, content, [System.Text.UTF8Encoding]::new($false))`.

5. **Mojibake en paths del inventario**: `Ã±/Ã©` se revierten con `bytes.encode('cp1252').decode('utf-8')` en Python. Causa: `os.walk()` originalmente serializó paths Mac-encoded como cp1252.

---

## Spot-check final de calidad

3 archivos revisados al azar:

✅ `gd-man-052-01-v2-us-c-parte-1.md` (Genius manual splitteado): frontmatter completo, `version_status: "vigente"`, contenido técnico inglés intacto, sin truncar mid-oración (split respetó boundaries de página).

✅ `gsm-recs-hde-v3-n.md` (Exceline HDE histórica): frontmatter con `version_status: "historica"` correcto, descripción de producto en español impecable, terminología técnica preservada (rangos voltaje, modos de protección).

✅ `i-gspt-mv-lr-10mar-parte-1.md` (Genius "I" manual splitteado): part 1/3 procesada correctamente, sin pérdida visible.

---

**Para mañana:** ¿Querés que arme el sweep de reclasificación `_otro_` → `_hoja-especificaciones_` (item #1)? Es bajo riesgo y termina de pulir el batch.
