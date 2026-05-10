```markdown
---
title: "GIII+MV - Nota de Aplicación: Protección de Motores mediante Toroides Externos"
type: Technical
source: "GIII+ MV GD-NA8003-VE-V.02.pdf"
product_line: "Genius"
document_type: "nota-aplicacion"
product_code: "GIII+MV"
date_processed: "2026-05-09"
---

# GIII+MV - Protección de Motores mediante Toroides Externos

## 1. Diagrama de Conexión GIII+MV con Toroides Externos

```
L1 L2 L3
   |
   |-- Protección contra cortocircuito
   |
   +-- Entrada Digital (Fila A)
   |
   +-- GIII+MV
   |
   +-- Relé Auxiliar
   |
   +-- Relé Control (circuito de control y arranque)
   |
   M (3~)

Contactor manejado desde Circuito de control y Arranque

Disparado: 8-10 CONECTADO
          6-8 ABIERTO

Normal:   8-10 ABIERTO
          6-8 CONECTADO

Cable AWG 14
```

## 2. Toroides Externos Sugeridos según la Corriente Nominal

| Rango de Corriente Nominal (A) | Toroide Relación /5 |
|--------------------------------|-------------------|
| 150 - 200                      | 600               |
| 190 - 250                      | 750               |
| 200 - 260                      | 800               |
| 250 - 330                      | 1000              |
| 300 - 350                      | 1200              |
| 375 - 500                      | 1500              |
| 500 - 660                      | 2000              |

## 3. Notas Importantes

1. El modelo identificado como GIII+MV000S se utiliza exclusivamente con CT externos. Este modelo protege motores con corriente nominal hasta 660 A.

2. El usuario debe especificar la corriente nominal del motor. Con este dato seleccionará un rango de corriente según la tabla adyacente, con la cual determinará la relación /5 que requerirá para los CT externos a instalar.

3. El usuario debe programar el GIII+MV con CT externos añadiendo las instrucciones de ajustes contenidas en esta nota de aplicación. (Todas las demás funciones y protecciones seguirán ajustándose de acuerdo al Manual de Instalación GIII+MV).

4. La calibración del GIII+MV se mantiene garantizada, siempre que los CT externos sean comerciales, de clase 1, secundario 5A.

## 4. Ajuste de CT Externos y Corriente Nominal en el Menú de Protección por Corriente

### Procedimiento de Ajuste

1. **Presionar ambos pulsadores de AJUSTE** desde la pantalla de Operación.

2. **En AJUSTE VOLTAJE**, presionar un pulsador de AJUSTE para llegar hasta AJUSTE CORRIENTE.

3. **En AJUSTE CORRIENTE**, presionar el Pulsador SELECCIÓN para acceder a CT.

4. **En CT**, presionar un pulsador de AJUSTE para llegar a la relación adecuada (consultar TABLA DE CT EXTERNOS SUGERIDOS SEGÚN LA CORRIENTE NOMINAL).

5. Luego de marcada la relación deseada de CT externo, presione el pulsador SELECCIÓN.

6. **Presionar ambos pulsadores de AJUSTE** para llegar hasta I NOMINAL.

7. **En AJUSTE CORRIENTE I NOMINAL**, presionar un pulsador de AJUSTE CORRIENTE para seleccionar el valor deseado.

8. Presionar un pulsador de AJUSTE para llegar al valor deseado (ejemplo: cambiar valor de 300 a 350A).

9. Presionar el pulsador de SELECCIÓN para ajustar el valor deseado.

10. Regreso al MENÚ DE CORRIENTE. Seguir con otros ajustes de corriente o salir al menú principal.

### Ejemplo

Para un motor con corriente FLA = 350A:
- Cambiar relación a 1200/5 según la tabla
- Establecer I NOMINAL a 350A

## Nota General

LAS DEMÁS FUNCIONES SON AJUSTABLES DE FORMA SIMILAR A LO DESCRITO EN EL MANUAL DE INSTALACIÓN.

---

**Fabricante:** Genteca - Generación de Tecnología, C.A.  
**RIF:** J-00223173-4  
**Ubicación:** Av. El Buen Pastor cruce con Calle Vargas, Edif. Alba, Piso 1, Local 1-A, Boleíta Norte, Caracas - Venezuela, Zona Postal 1070  
**Teléfono:** +58 212 237.07.11  
**Fax:** +58 212 235.24.97  
**Email:** genteven@genteca.com.ve  
**Web:** www.genteca.com.ve
```