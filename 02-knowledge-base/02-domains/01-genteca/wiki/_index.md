# Genteca — Wiki (index)

**Estado:** parcialmente poblado. Esta carpeta contiene artículos compilados sobre el dominio Genteca: fundamentos técnicos, patrones de aplicación, lecciones aprendidas, guías de decisión.

## Subcarpetas

- `brand/` — Identidad de marca, estrategia y procesos de comunicaciones de Exceline / Genius. **Poblado 2026-04-30; ampliado 2026-05-13.**
  - `01-identidad-de-marca.md` — logos, Pantones, tipografías, atributos, esloganes, usos, fotografía.
  - `02-estrategia-digital-y-audiencias.md` — diagnóstico IG, benchmarking, audiencias, posicionamiento, pilares, framework digital, campaña AA/Refr.
  - `03-comunicaciones-organigrama-y-procesos-2026.md` — organigrama del área, 8 funciones, checklist 13 materiales por producto nuevo, soporte ESC, Trade Marketing / Plan Tienda Ideal, portal web, redes sociales.
  - `04-estrategia-2026-marca-y-comunicaciones.md` — marco 4P, posicionamiento formal Exceline + Exceline Profesional, cadena de influencia × medio, calendario de lanzamientos 2026, 11 campañas estacionales, eventos del sector.
- `market/` — Market intelligence específico de Genteca (competidores, HMI, tendencias, benchmarking). Provisional bajo el dominio; se reevaluará promover a `03-cross-cutting/02-marketing-tecnico.md` si crece el marketing transversal (ver `FOLDER-ARCHITECTURE.md` §9).
- `tech/` — **Poblado 2026-05-07.** Artículos técnicos compilados desde el atlas legacy de marzo 2026 tras auditoría Vera. Ver `tech/_index.md` para detalle. Incluye: fundamentos de motores trifásicos, protecciones eléctricas, aplicaciones (bombeo/refrigeración/ventiladores/transportadores), protocolo de selección de producto Genteca, y argumentos de venta técnicos (uso interno pendiente gate Bruna).
- `references/` — **Poblado 2026-05-07.** Bibliografía técnica curada (22 fuentes académicas y técnicas con ~95% acceso abierto) sobre motores trifásicos y sus protecciones. Ver `references/_index.md`.

## Qué se podría añadir en el futuro

- `04-HMI-y-comunicacion-MODBUS.md` — GIO-Link, MODBUS RTU, integración HMI.
- `05-lecciones-de-campo.md` — patrones observados en proyectos ejecutados (GME, GST, GSM).

## Qué NO va aquí

- Hojas de especificación de producto → `specs/`.
- Material visual → `assets/`.
- Documentos de un proyecto en curso → `/RAUL/03-projects/genteca/<proyecto>/`.
- SOPs generales no específicos de Genteca → `/RAUL/02-knowledge-base/04-sops-and-playbooks/`.

## Producción y consumo

- **Producido por:** Paxs + Vera + Orlan compilando desde `01-inbox/03-raw-sources/` y proyectos cerrados.
- **Consumido por:** todos los agentes que trabajen tareas Genteca, como contexto persistente antes de ir a internet.
