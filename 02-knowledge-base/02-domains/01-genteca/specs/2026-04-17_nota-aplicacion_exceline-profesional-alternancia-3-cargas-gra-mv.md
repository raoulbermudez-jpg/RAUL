# Nota de Aplicación — Alternancia de Tres Cargas Asimétricas con GRA-MV

**Línea:** Exceline Profesional  
**Código:** 01-GD-NA  
**Tipo de documento:** Nota de Aplicación  
**Versión:** v2  
**Fabricante:** Gente, Generación de Tecnología, C.A. — www.genteca.com.ve  
**Referencia PDF:** 01-GD-NA-Alternancia-3-cargas-v2.pdf (Notas_Aplicacion/01-GD-NA-Alternancia-3-cargas-v2.pdf en RAG_SOURCES)

---

## Descripción de la Aplicación

**Aplicación:** Alternancia de tres cargas asimétricas usando un relé alternador GRA-MV  
**Voltaje de la instalación:** 120/220 V~  
**Grado de dificultad:** Bajo-Medio

---

## Introducción

Un relé alternador es un dispositivo electrónico de control que opera activando cargas eléctricas en forma alternada en aplicaciones con bombas, compresores, aires acondicionados, unidades de refrigeración o sistemas de riego.

El relé alternador GRA-MV fue diseñado para ser usado en cualquier aplicación de automatismos en general y puede funcionar con voltajes nominales de alimentación de 120 V~ y 220 V~.

Esta nota aplica específicamente al caso de **sistemas hidroneumáticos de tres bombas** y a **sistemas de riego con activación de diferentes zonas**, donde se requiere que tres cargas operen en forma alternada asimétricamente.

---

## Lista de Equipos

| Equipo | Modelo | Características |
|--------|--------|-----------------|
| Relé Alternador | GRA-MV | Multivoltaje 120/220 V~ — alterna posición de contactos al detectar cambio cerrado→abierto entre entradas 3 y 2 — compacto y fácil de instalar |

---

## Principio de Funcionamiento

Cada vez que el GRA-MV detecta un cambio de **cerrado a abierto** entre sus entradas 3 y 2 (señal de control), genera una actuación sobre los contactos de su etapa de salida, cambiando su posición. Esto produce la alternancia entre las tres cargas según el diagrama de tiempo de la Figura N°1.

**Diagrama de tiempo para tres cargas asimétricas:**

```
Control  _____|‾‾‾|___|‾‾‾|___|‾‾‾|___
Carga 1  _____|‾‾‾‾‾‾‾|_______________|
Carga 2  _____________|‾‾‾‾‾‾‾|_______|
Carga 3  _______________________|‾‾‾‾‾|
```

---

## Esquema de Conexión (Figura N°2)

```
120/220 V~
     ↓
  [CONTROL]
     ↓
  [GRA-MV]
    ├── [CARGA 1]
    ├── [CARGA 2]
    └── [CARGA 3]
```

La Carga 3 se conecta a través de un relé adicional activado por el GRA-MV. Las tres cargas se activan en forma secuencial según el estado del GRA-MV.

---

## Notas

- Este esquema es útil para sistemas de riego con activación de diferentes zonas
- Para sistemas hidroneumáticos con dos bombas (más común), ver Nota de Aplicación `2026-04-17_nota-aplicacion_exceline-profesional-hidroneumatico-2-bombas-GRA-GRC.md`
- La variante con bombas trifásicas y dos presostatos se cubre en `2026-04-17_nota-aplicacion_exceline-profesional-hidroneumatico-2-bombas-trifasicas-presostatos.md`

---

## Diagramas

> Los diagramas de tiempo (Figura N°1) y el esquema de conexión completo (Figura N°2) son gráficos en el PDF original. Fuente: `G:\Mi unidad\WorkspaceIA\RAG_SOURCES\Notas_Aplicacion\01-GD-NA-Alternancia-3-cargas-v2.pdf`
