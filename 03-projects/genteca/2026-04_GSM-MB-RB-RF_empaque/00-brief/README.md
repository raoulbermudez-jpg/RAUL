# 00-brief — GSM-MB / RB / RF / RE empaque

Materia prima cruda que alimenta el workstream. **No editar archivos depositados aquí**: son fuentes para que la cadena CSC los procese (Vera técnico, Orlan mercado, Vael message framework, Bruna gate, Solenne copy).

## Subcarpetas

| Carpeta | Qué va aquí | Convención de nombre |
|---|---|---|
| `innovaciones/` | Documentación técnica cruda de las dos innovaciones (NTC + tiempo respuesta < 30 ms). Notas de Raoul, descripciones de funcionamiento, casos de uso, sustento técnico. | `innovacion_<NTC\|tiempo-respuesta\|...>_YYYY-MM-DD.md` |
| `specs-i-d/` | Datasheets, specs internos I&D, mediciones, curvas, reportes de laboratorio. | `spec_<producto>_<tema>_YYYY-MM-DD.{pdf,md}` |
| `market-research/` | Estudios de mercado, análisis competencia (TQ, Protector, otros), datasheets de competidores. | `market-research_<tema>_YYYY-MM-DD.{pdf,md}` |
| `transcripts/` | Transcripciones crudas de reunión (Tactiq, Otter, etc.). Las actas destiladas por reunión viven en `03-review-and-release/`. | `transcript_<participantes>_YYYY-MM-DD.{md,txt}` |
| `whatsapp/` | Intercambios WhatsApp copiados a `.txt`. Identificar contacto/grupo y fecha. | `wa_<contacto-o-grupo>_YYYY-MM-DD.txt` |

## Archivos sueltos en raíz `00-brief/`

- `empaque_estudio.pptx` — input inicial del proyecto (abril 2026).

## Notas

- Si un input toca privacidad de terceros (clientes, instaladores nombrados) y no debe entrar al repo público, marcarlo en el filename con prefijo `_private_` y verificar que `.gitignore` lo excluye antes de commit.
- Decisiones que salgan de procesar este material van a `03-review-and-release/` (deltas, actas, emails).
