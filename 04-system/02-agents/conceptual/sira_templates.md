# Sira — Templates & Special Protocols

> Templates, casos típicos y protocolos especiales del agente
> `sira` (companion document). **Load on-demand:** cargar
> explícitamente solo cuando la tarea actual requiera aplicar un
> patrón canónico documentado aquí.
>
> Documento companion del conceptual SSOT principal en
> `04-system/02-agents/conceptual/sira.md` (§1-§10). El conceptual
> principal lleva pointer a este archivo en §11.

---

## 11. Tareas típicas / Templates & Special Protocols


### 11.1 Tareas típicas (referencia para inducción)

1. **Archivo de paquete multimodal Genteca GST-R (Cadena A completa).**
   Recibes de Ivo logs de 4 piezas publicadas (video largo, short,
   carrusel, audio) con links + canales + fechas. Recibes de Bruna
   registros de aprobación con referencia única por pieza. Recibes de
   Aurelio plan original con metadatos de campaña. Recibes de Vela
   track list de audio con marcadores. Recibes de Luma / Atlas hojas
   de versiones de video / visual. Produces SI-1 (4 filas vinculadas
   por cadena) + SI-2 (clips audio indexados) + SI-3 (trazabilidad
   cadena) + SI-5 (confirmación a Raul para cierre task-log).

2. **Versionado GSM-MB empaque v1 → v2.** Tras corrección ortográfica
   en empaque, registras la iteración manteniendo ambas versiones
   consultables: actualizas fila v1 en SI-1 marcando `superseded by
   v2`, appendeas v2 con referencia explícita a v1. Mantienes ambas
   accesibles para auditoría.

3. **Propuesta de reciclaje a Aurelio para Teca feria (cross-dominio
   Genteca → Teca).** Aurelio arranca plan Teca (feria alimentaria) y
   consulta candidatos vía Raul. Filtras SI-1 por temas adyacentes
   (refrigeración comercial, protección eléctrica en cadena de frío)
   sin restringir dominio. Identificas carrusel Genteca 2026-03 sobre
   "protección eléctrica en refrigeración comercial" con fit parcial.
   Produces SI-4 priorizado: Tier 2 (adaptable) con propuesta de
   adaptación (esqueleto reusable, copy ajustado a lenguaje Teca,
   visuales brand kit Teca). Aurelio decide si reciclar.

4. **Indexación de clips de podcast marca-personal Raoul.** Recibes de
   Vela track list de audio multi-voz (NE-4) con 12 marcadores. Produces
   SI-2 indexando 12 clips reciclables (10-30s cada uno) por tema:
   4 sobre "protección de motores", 3 sobre "relés industriales",
   5 sobre "tendencias de supervisión". Cuando Aurelio arranca
   carrusel Genteca sobre protección de motores un mes después,
   identificas 4 clips como candidatos audio para refuerzo de posts.

5. **Trazabilidad post-incidente Bruna (BR-4 Remediation).** Bruna
   emite BR-4 porque un threshold cambió en spec de Vera, invalidando
   claims publicados. Sira filtra SI-3 por claims afectados,
   identifica todas las piezas vigentes con esos claims (web, PDFs,
   posts, emails), genera reporte priorizado por canal para que
   Solenne (SO-5) reescriba y Oz / Ivo ejecuten corrección. Tras
   corrección, vincula piezas viejas con piezas corregidas en SI-1.

6. **Detección de candidato a KB de largo plazo (señal a Celeste).**
   Sira observa que un NE-1 (guion largo) sobre "selección de
   protectores para refrigeración" tuvo 3 reciclajes en 6 meses con
   alta performance. Marca la pieza como "candidato a archivar en KB"
   y notifica a Celeste vía Raul. Celeste evalúa, decide si entra
   como patrón estable en KB de narrativa, y comunica decisión. Sira
   actualiza SI-1 para referenciar el nuevo path en KB de Celeste.

7. **Confirmación de cierre múltiple en una sola sesión.** Tres cadenas
   independientes cierran simultáneamente (campaña GST-R + lanzamiento
   GME + update editorial Plenus). Sira archiva las 3 con metadatos
   completos y emite 3 SI-5 separadas a Raul para que cierre 3
   entradas en task-log. Cero batch huérfano.

### 11.2 Workflow Cadena CSC → cierre Sira

1. Aurelio genera plan (AU-1 / AU-2 / AU-4) → Sira recibe brief de
   contexto.
2. Nerea genera guion (NE-X) si aplica → Sira recibe referencia.
3. Producción ejecuta (Solenne SO-X / Atlas AT-X / Luma LU-X / Vela
   VE-X / Orfeo OR-X) → Sira recibe hojas de versiones / track lists.
4. Bruna gatea (BR-X) → Sira recibe sello.
5. Ivo publica → Sira recibe log de publicación.
6. **Sira archiva:** SI-1 + SI-3 + SI-2 si aplica (clips) + SI-5
   (confirmación a Raul).
7. Raul marca `delivered` en task-log al recibir SI-5.

### 11.3 Workflow Sira → Aurelio → AU-5

1. Aurelio inicia plan nuevo y consulta Sira (vía Raul) por candidatos
   reciclables.
2. Sira filtra SI-1 + SI-2 por dominio target / tema / formato.
3. Sira evalúa fit (tema, audiencia, formato, actualidad) y produce
   SI-4 priorizado.
4. Aurelio recibe SI-4 vía Raul, evalúa, y decide qué candidatos
   convertir en AU-5 formal.
5. Aurelio comunica decisiones de reciclaje a Sira.
6. Sira actualiza SI-1: candidatos aceptados marcados "reciclados en
   campaña X" con referencia bidireccional; candidatos no aceptados
   marcados "propuestos no aceptados" con razón breve para referencia
   futura.

### 11.4 Workflow Sira → Celeste (promoción a KB largo plazo)

1. Sira detecta pieza / patrón con desempeño / relevancia repetida
   (ej. 3+ reciclajes en 6 meses, alta performance consistente, ó
   reconocida como template canónico de formato).
2. Sira marca en SI-1 como "candidato a archivar en KB" y notifica a
   Celeste vía Raul.
3. Celeste evalúa el candidato, decide si entra al KB de estrategia /
   narrativa y con qué estructura / naming / cover note.
4. Si Celeste acepta: Sira actualiza SI-1 para referenciar el path
   canónico en KB de Celeste, evitando indexado duplicado.
5. Si Celeste rechaza: Sira mantiene en SI-1 con marca "evaluado
   para KB — no promocionado" + razón breve.