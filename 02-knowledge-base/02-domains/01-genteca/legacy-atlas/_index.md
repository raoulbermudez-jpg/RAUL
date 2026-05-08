# Genteca — Legacy Atlas (2026-03)

**Estado:** archivo de consulta. NO es la KB activa.
**Origen:** atlas y RAG generados por el Owner con Claude Opus 4.6 en marzo 2026 sobre el dominio Genteca (protecciones eléctricas para motores trifásicos), originalmente subidos a NotebookLM como base de conocimiento.
**Rescatado al repo:** 2026-05-07 desde Google Drive (`WorkspaceIA Backup/Genteca/02_ProtMotores_Atlas/`) y OneDrive local (`Desktop\GENTE\Base de conocimiento IA\Genius y protectores trifasicos\`).
**Auditado por Vera:** 2026-05-07 — reporte en respuesta a delegación de la sesión, sin archivo de salida formal.

## Qué hay aquí

| Archivo | Tamaño | Origen | Estado tras auditoría |
|---|---|---|---|
| `ProtMotores_Atlas_1_Motores_Trifasicos.md` | 35 KB | Drive (.gdoc) | INTEGRADO selectivo a `wiki/tech/motores-trifasicos-fundamentos.md` |
| `ProtMotores_Atlas_2_Protecciones_Electricas.md` | 35 KB | Drive (.gdoc) | INTEGRADO selectivo a `wiki/tech/protecciones-electricas-motores.md` |
| `ProtMotores_Atlas_3_Aplicaciones.md` | 32 KB | Drive (.gdoc) | INTEGRADO (tablas clave) a `wiki/tech/aplicaciones-bombeo-refrigeracion.md` |
| `ProtMotores_Atlas_4_Mercado_Venezuela.md` | 27 KB | Drive (.gdoc) | PARCIAL: archivado aquí + argumentos técnicos puros extraídos a `wiki/tech/argumentos-venta-tecnicos-INTERNO-PENDIENTE-GATE.md` (uso interno solamente, pendiente gate Bruna) |
| `ProtMotores_Atlas_5_Exceline_Profesional.txt` | 31 KB | OneDrive (.txt) | ARCHIVADO solo (specs ya en `specs/` activos) |
| `ProtMotores_Atlas_6_Genius.txt` | 37 KB | OneDrive (.txt) | ARCHIVADO solo (specs ya en `specs/` activos) |
| `ProtMotores_RAG_Integrador_v2.txt` | 32 KB | OneDrive (.txt) | INTEGRADO selectivo a `wiki/tech/protocolo-seleccion-producto-genteca.md` |
| `ProtMotores_URLs_Bibliography.md` | 12 KB | Drive (.gdoc) | INTEGRADO completo a `wiki/references/referencias-bibliograficas-motores-trifasicos.md` |

## Qué se descartó (no archivado)

- `ProtMotores_URLs_CopyPaste_NotebookLM.md` — instrumental obsoleto para cargar URLs en NotebookLM. Contenido duplicado en Bibliography. Eliminado 2026-05-07.

## Riesgos detectados por Vera (resumen)

- **R1 — Atlas 4 contiene SALES_ARGs comparativos contra Schneider y genéricos chinos.** Bruna ya estableció en gate GME (Precedente #3) que comparativos directos sin evidencia de ensayo son de uso restringido. NO usar este atlas para material externo sin pasar por Bruna.
- **R2 — GST-RD y GST-RG aparecen como "en desarrollo próximo"** pero no hay evidencia de progreso en 6 semanas. En los wikis integrados, las referencias a estos productos fueron neutralizadas o marcadas como "estado desconocido al 2026-05-07". Pendiente aclarar con engineering.
- **R3 — La "calculadora costo-beneficio" del Atlas 4 con "Y% probabilidad de falla"** es plantilla, no dato real. NO usar como cálculo cuantitativo.
- **R4 — Datos de costo de rebobinado y de compresor hermético** (rangos %) son estimaciones de mercado venezolano sin fuente citada. Aceptables para argumentación interna; validar antes de uso externo.
- **R5 — Tablas de corriente nominal por HP** están correctamente marcadas como aproximadas; usar siempre el valor de placa del motor.

## Por qué se mantienen estos archivos

1. **Trazabilidad histórica** — preserva la base de conocimiento que el Owner construyó en marzo 2026.
2. **Consulta puntual** — si algún wiki integrado necesita ampliarse, el material original está aquí.
3. **Auditable** — futuro lector puede comparar lo integrado con lo original y entender qué se descartó.

No editar estos archivos. Para actualizar conocimiento, editar los wikis integrados (`wiki/tech/`).
