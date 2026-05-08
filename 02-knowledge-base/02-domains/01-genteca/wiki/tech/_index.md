# Genteca — Wiki técnico (index)

**Propósito:** artículos compilados de conocimiento técnico aplicable al dominio Genteca: fundamentos de electrotecnia, protecciones eléctricas, aplicaciones, protocolos de selección.
**Audiencia:** todos los agentes que trabajen tareas Genteca como contexto persistente, antes de consultar fuentes externas.

## Artículos vigentes

| Archivo | Contenido | Origen |
|---|---|---|
| `motores-trifasicos-fundamentos.md` | Conceptos físicos, parámetros nominales, mecanismos de falla, curvas características de motores trifásicos de inducción. Tablas de corriente nominal por HP a 220V/440V 60Hz. | Atlas 1 (legacy 2026-03), curado |
| `protecciones-electricas-motores.md` | Tecnologías de protección (bimetálico, electrónico, monitor de red, guardamotor, PTC, diferencial), clases de disparo IEC, coordinación Tipo 1/2, comparativas técnicas. | Atlas 2 (legacy 2026-03), curado |
| `aplicaciones-bombeo-refrigeracion.md` | Tablas operativas de selección: clase IEC por aplicación, cable sumergible por profundidad. Patrones de falla específicos por aplicación (bombas, compresores, ventiladores, transportadores). | Atlas 3 (legacy 2026-03), tablas extraídas |
| `protocolo-seleccion-producto-genteca.md` | Protocolo paso-a-paso de selección de producto Genteca (Exceline Profesional + Genius) según aplicación + Q&A técnicos. | RAG Integrador (legacy 2026-03), curado |
| `argumentos-venta-tecnicos.md` | 7/8 argumentos aprobados para uso externo (BR-2 2026-05-07): 3 VERDE sin cambios + 4 AMARILLO con caveat literal. Argumento 8 (COVENIN 3445) sigue 🔴 ROJO — pendiente verificación SENCAMER/FONDONORMA. Log de claims: `_governance/2026-05-03_genteca_claim-approval-log_v1.md` entradas #22-28. | Atlas 4 (legacy 2026-03), extracción selectiva |

## Política de actualización

- Los wikis aquí se editan directamente cuando hay corrección o actualización técnica.
- Los archivos legacy en `legacy-atlas/` NO se editan — son histórico.
- Cualquier cambio sustantivo a un wiki debería tener entrada en `DECISIONS.md` si afecta criterios de selección o claims técnicos.

## Riesgo de claims

Cualquier claim numérico, comparativo o de desempeño en estos wikis que vaya a usarse en material EXTERNO (LinkedIn, blog, email a cliente, deck a junta, packaging) debe pasar por Bruna antes de la publicación. Los wikis son referencia interna; la externalización es decisión gateada.

**Excepción declarada:** los argumentos de venta del archivo `argumentos-venta-tecnicos.md` ya pasaron BR-2 con caveats literales (excepto Argumento 8 COVENIN 3445). Pueden usarse externamente respetando el caveat literal de cada uno y el log de claims.

## Última actualización

- **2026-05-08:** argumentos de venta renombrados de `argumentos-venta-tecnicos-INTERNO-PENDIENTE-GATE.md` → `argumentos-venta-tecnicos.md` tras BR-2 aprobado por el Owner.
- **2026-05-07:** creación inicial integrando atlas legacy de marzo 2026 (auditoría Vera).
