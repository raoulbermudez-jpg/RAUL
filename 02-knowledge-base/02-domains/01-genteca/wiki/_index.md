# Genteca — Wiki (index)

**Estado:** stub. Esta carpeta se poblará en fases post-migración con artículos compilados sobre el dominio Genteca: fundamentos técnicos, patrones de aplicación, lecciones aprendidas de proyectos cerrados, guías de decisión.

## Subcarpetas

- `brand/` — Identidad de marca y estrategia digital de Exceline / Genius. **Poblado 2026-04-30.**
  - `01-identidad-de-marca.md` — logos, Pantones, tipografías, atributos, esloganes, usos, fotografía.
  - `02-estrategia-digital-y-audiencias.md` — diagnóstico IG, benchmarking, audiencias, posicionamiento, pilares, framework digital, campaña AA/Refr.
- `market/` — Market intelligence específico de Genteca (competidores, HMI, tendencias, benchmarking). Provisional bajo el dominio; se reevaluará promover a `03-cross-cutting/02-marketing-tecnico.md` si crece el marketing transversal (ver `FOLDER-ARCHITECTURE.md` §9).

## Qué va aquí (cuando se pueble)

- `01-fundamentos-tecnicos.md` — fundamentos de protección eléctrica aplicables a la línea Genteca.
- `02-proteccion-motores.md` — patrones de protección para motores (refrigeración, bombas, VRF).
- `03-proteccion-bombas-hidroneumaticos.md` — patrones para bombas sumergibles e hidroneumáticos.
- `04-HMI-y-comunicacion-MODBUS.md` — GIO-Link, MODBUS RTU, integración HMI.
- `05-lecciones-de-campo.md` — patrones observados en proyectos ejecutados.

## Qué NO va aquí

- Hojas de especificación de producto → `specs/`.
- Material visual → `assets/`.
- Documentos de un proyecto en curso → `/RAUL/03-projects/genteca/<proyecto>/`.
- SOPs generales no específicos de Genteca → `/RAUL/02-knowledge-base/04-sops-and-playbooks/`.

## Producción y consumo

- **Producido por:** Paxs + Vera + Orlan compilando desde `01-inbox/03-raw-sources/` y proyectos cerrados.
- **Consumido por:** todos los agentes que trabajen tareas Genteca, como contexto persistente antes de ir a internet.
