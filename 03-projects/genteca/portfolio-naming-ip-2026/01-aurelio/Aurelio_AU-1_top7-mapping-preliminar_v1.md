---
doc_type: AU-1-mapping
project_id: portfolio-naming-ip-2026
domain: genteca
version: v1.0
fecha: 2026-05-13
author: Aurelio
nota: Mapeo preliminar — Vera y Orlan pueden ajustar categoría tecnológica en Phase 1.
      Solenne hace el mapping final en Phase 4 y genera candidatos adicionales hasta 4/tech.
---

# AU-1 — Top 7 Mapping Preliminar
## Proyecto: Portfolio Naming IP 2026 (Genteca)

> **Propósito de este documento:** dar a Vera (inventario) y Orlan (differentiation matrix) en Phase 1 el punto de partida sobre cómo los 7 candidatos anchor del proyecto previo se mapean provisionalmente a las categorías tecnológicas que ellos van a formalizar. No es prescriptivo — si el inventario híbrido sugiere otra granularidad, Vera y Orlan ajustan y lo comunican en Checkpoint 1 Owner.
>
> Solenne consume este mapping en Phase 4 para no partir de cero. Los 7 son anchor, no exclusivos — Solenne puede mover un candidato a otra tech si el inventario lo justifica mejor.

---

## Tabla de mapping preliminar

| # | Marca (anchor) | Tecnología ancla actual | Producto donde vive actualmente | Categoria tecnologica probable (inventario hibrido) | Linea comercial primaria | Audiencia primaria (charter §5) | Beneficio del beneficio L2 (si identificable) | Bruna BR-2 previo |
|---|---|---|---|---|---|---|---|---|
| 1 | **StaggerStart** | Staggered Intelligent Reconnect — algoritmo de escalonamiento aleatorio en la reconexión post-evento | GSM-MB / RB / RE | Logica de reconexion inteligente — algoritmo de escalonado temporal aleatorio para prevenir pico de demanda simultanea en reencendido | Exceline (residencial + comercio pequeno/mediano) | Duenos de hogar / duenos de comercio — consumidor no tecnico | El compresor del sistema (AC, refrigerador, bomba) no recibe el golpe de corriente del reencendido simultaneo de todos los equipos protegidos — vida util prolongada, menos fallas post-apagon | ✅ Aprobado batch 1 |
| 2 | **ForensLog** | 100-Fault Forensic History — registro forense de los ultimos 100 eventos de falla con timestamp y tipo | GIII+ / MV | Diagnostico forense y registro historico de eventos — log de fallas indexado con capacidad de auditoria | Exceline Profesional / Genius | Industria + instaladores como influenciadores tecnicos + especificadores | El tecnico de mantenimiento reconstruye el historial de fallas exacto sin depender de testimonio del operador — diagnostico preciso, menos tiempo fuera de servicio, menos costo de intervencion | ✅ Aprobado batch 1 |
| 3 | **FlickerGuard** | 20ms Flicker Detection — deteccion de eventos de flicker en ventana de 20 milisegundos | GSM-L | Proteccion por voltaje / deteccion de perturbaciones rapidas — deteccion de flicker sub-ciclo | Exceline (residencial) | Duenos de hogar (AC, refrigerador como equipos a proteger) | El compresor del aire acondicionado o el compresor del refrigerador no sufre el estres mecanico de los arranques forzados por flicker — el equipo no se dana prematuramente | ⚠ Busqueda OMPI ampliada pendiente |
| 4 | **Thermo-Safe** | Funcion termica integrada con sensor NTC — modelo de temperatura en tiempo real con curva de disparo cold/hot | GSM-MB / RB / RE | Modelo termico integrado — sensor NTC + logica cold/hot de disparo por temperatura | Exceline (residencial + comercio) | Duenos de hogar / duenos de comercio | El motor del equipo no se quema por sobrecalentamiento encubierto — la proteccion detecta temperatura real, no solo corriente | ⚠⚠ Caso A (doble caveat si NTC visible en empaque) / ⚠ Caso B (caveat simple, sin NTC en empaque) |
| 5 | **TripleLock** | Triple-Fault Lockout — bloqueo de reconexion automatica tras tres fallas consecutivas dentro de ventana de tiempo | Genius GIII+ / GUCT / GOC | Logica de proteccion multi-falla — bloqueo escalonado post-falla repetida con requirimiento de reset manual o temporizacion | Genius (premium + especificadores) | Especificadores tecnicos + instaladores de proyectos premium | El equipo industrial no cicla entre falla y rearranque destructivo — el bloqueo fuerza intervencion tecnica deliberada antes de continuar operacion | ⚠ Busqueda sectorial seguridad fisica pendiente |
| 6 | **TaskMemory** | Smart Task Memory — memoria de estado que conserva la tarea en curso y la retoma tras evento de corte/restauracion | GRN-MV | Logica de memoria de estado y recuperacion de tarea — persistencia de modo operativo post-corte | Exceline Profesional / Genius | Industria / comercio profesional (duenos de equipos de riego, bombeo, procesos automatizados) | El proceso de bombeo o riego no requiere supervision humana en el reencendido post-corte — el equipo retoma solo donde estaba, sin perder el ciclo | ⚠ Colision potencial con software (clase 9 amplia) — pendiente busqueda sectorial |
| 7 | **ThermalCurve** | Cold/Hot Thermal Curve Model — curva de disparo termica diferenciada segun temperatura inicial del motor (frio vs caliente) | Genius (linea premium) | Modelo termico algoritmico — curva inversa I-t diferenciada cold/hot (override universal de facto) | Genius (premium) | Especificadores tecnicos + instaladores de proyectos premium | El motor industrial no sufre disparo prematuro en arranque en caliente ni proteccion insuficiente en arranque en frio — la curva se adapta al estado real del motor, no a un patron fijo | ⚠⚠ Riesgo descriptividad alto — pendiente resolucion Bruna Phase 3 |

---

## Notas de lectura para Vera y Orlan (Phase 1)

### Para Vera

La columna "Categoria tecnologica probable" es la hipotesis de Aurelio basada en la documentacion disponible. Al construir el inventario hibrido con granularidad 6-9 nodos, considera:

- Si dos de los 7 comparten la misma tecnologia raiz (por ejemplo, ThermalCurve y Thermo-Safe ambas involucran NTC + logica termica), Vera decide si son un nodo unico con dos expresiones o dos nodos distintos, y lo justifica brevemente en el inventario.
- El override curva inversa V-t algorítmica + I-t cold/hot es universal de facto (charter §3 decision 4). No audites producto por producto. Si el KB muestra excepcion documentada, reporta al Owner en Checkpoint 1, no al deck.
- TaskMemory (GRN-MV) tiene contexto adicional: la memoria de estado y el tiempo de confirmacion 10s estan confirmados verbalmente por I&D pero sin actualizacion en HDE/MAN. Vera puede referenciarlo en el inventario con nota "pendiente actualizacion documental HDE" — esto alimenta la lista de documentos que el abogado podra pedir a I&D.

### Para Orlan

La columna "Linea comercial primaria" te da el marco para la differentiation matrix. Competidores de referencia: ABB / Siemens / Schneider / Eaton / Rockwell / Chint / LS / Lovato. Para cada nodo del inventario: verde (Genteca unica o primera en clase), amarillo (paridad bien ejecutada), rojo (gap o paridad debil). Sin tabla por producto — la matrix es por tecnologia/nodo.

### Para Solenne (Phase 4)

Este mapping te da la base. Tus pasos en Phase 4:

1. Confirmar que cada uno de los 7 encaja en un nodo del inventario Vera aprobado en Checkpoint 1. Si un candidato no encaja limpiamente, reporta a Aurelio / Owner antes de continuar.
2. Completar hasta 4 candidatos por nodo — los 7 anchor cuentan como candidato 1 de su nodo si pasan el filtro de impacto. Los nodos sin anchor del Top 7 reciben 4 candidatos nuevos todos.
3. Filtro operativo: impacto audiencia primaria → factibilidad SAPI VE → factibilidad IMPI MX. No metas candidatos debiles para cumplir la cuota de 4.
4. ThermalCurve (⚠⚠): si Bruna en Phase 3 lo degrada a ❌, genera un candidato de reemplazo para ese nodo. No esperes instruccion adicional de Aurelio — es comportamiento esperado.

---

## Relacion entre los 7 y las 6-9 tecnologias del inventario hibrido

Este esquema es hipotetico antes de Phase 1. Vera y Orlan pueden reorganizarlo completamente.

```
Hipotesis de agrupacion (orientativa, no prescriptiva):

NODO A — Logica de reconexion inteligente
  Anchor: StaggerStart

NODO B — Proteccion por voltaje / deteccion de perturbaciones rapidas
  Anchor: FlickerGuard
  [Posible inclusion: algoritmo de deteccion <30ms si Vera lo separa como nodo propio]

NODO C — Modelo termico integrado (NTC)
  Anchor: Thermo-Safe
  [Posible fusion con NODO D si Vera evalua que comparten raiz algorítmica]

NODO D — Modelo termico algoritmico — curva inversa I-t cold/hot
  Anchor: ThermalCurve
  [Atencion: riesgo descriptividad. Si Vera lo documenta con RTB solido,
   Bruna tiene mas base para defender en Phase 3]

NODO E — Diagnostico forense y registro historico
  Anchor: ForensLog

NODO F — Logica de proteccion multi-falla / bloqueo escalonado
  Anchor: TripleLock

NODO G — Memoria de estado y recuperacion de tarea
  Anchor: TaskMemory

NODO H (sin anchor del Top 7) — slot abierto para tecnologia/feature adicional
  que Vera identifique en el inventario hibrido como nodo registrable independiente.
  Vera y Orlan llenan si corresponde.

NODO I (sin anchor del Top 7) — idem NODO H.
```

Si Vera fusiona C+D en un nodo unico, el portafolio queda en 6-7 nodos. Si separa <30ms como nodo independiente (FlickerDetect vs FlickerGuard, por ejemplo), puede llegar a 8-9. El target del Owner es 6-9 — el inventario manda, no esta hipotesis.

---

## Supuestos especificos de este mapping

- La asignacion de "Audiencia primaria" a cada candidato sigue la matriz del charter §5, no es interpretacion de Aurelio — es el esquema del Owner.
- El "Beneficio del beneficio L2" en esta tabla es preliminar. Vael lo confirma o refina en Phase 2 con su messaging architecture. Si Vael encuentra un L2 mas preciso o descarta alguno, su VA-2 sobreescribe esta columna para todos los efectos de produccion posterior.
- Los 7 BR-2 previos son carry-over del proyecto `2026-05-07_marcas-anglicismos-junta`. Son informacion historica valida, pero no constituyen sello formal para este proyecto. Bruna en Phase 3 produce el BR-2 formal del presente portafolio.
- TaskMemory: la semantica LED y el tiempo 10s estan confirmados verbalmente por I&D (ver memoria GRN-MV_LED_permisivo). La marca "TaskMemory" describe la funcion de memoria de estado, no el protocolo LED — por eso el riesgo de descriptividad aqui es de colision de clase (software), no de descriptividad del producto electrico.
