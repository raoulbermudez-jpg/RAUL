# Manual de Instalación — Arrancador Trifásico Directo GMS-U

**Línea:** Exceline Profesional / Genius  
**Código de producto:** GMS-U  
**Tipo de documento:** Manual de Instalación  
**Fabricante:** Gente, Generación de Tecnología, C.A. — www.genteca.com.ve  
**Referencia PDF:** I_GMS-U.pdf (Exceline_Profesional/I_GMS-U.pdf en RAG_SOURCES)

---

## 1. Descripción General

GMS-U es un Arrancador trifásico directo diseñado para realizar la conexión y desconexión de motores trifásicos a través de un contactor, mientras es protegido, supervisado y controlado por un Relé de Protección contra fallas de fase y corriente **GUCT**.

> **ALERTA:** Solo personal técnico calificado con conocimientos en tableros y de la maquinaria a proteger debería realizar la instalación, arranque y mantenimiento del sistema.

> **AVISO:** Este producto ha sido diseñado para ambiente industrial severo. De ser utilizado en ambiente residencial, el usuario podría requerir algunas medidas en caso de notar ruido eléctrico inesperado en artefactos domésticos.

---

## 2. Modelos Disponibles

| Modelo | Voltaje | Corriente | HP (208V) | HP (480V) |
|--------|---------|-----------|-----------|-----------|
| GMS-U20804S | 208/220 V~ | 1-4 A | 0,5-0,75 HP | — |
| GMS-U20812S | 208/220 V~ | 3,5-12,5 A | 0,75-3 HP | — |
| GMS-U20832S | 208/220 V~ | 10-32 A | 3-7,5 HP | — |
| GMS-U48004S | 440/480 V~ | 1-4 A | — | 0,5-2 HP |
| GMS-U48012S | 440/480 V~ | 3,5-12,5 A | — | 2-7,5 HP |

---

## 3. Aplicaciones del Relé GUCT incorporado

El arrancador GMS-U incorpora el relé GUCT que supervisa constantemente:
- Corriente de consumo del motor (sobrecarga y subcarga)
- Voltaje de la línea trifásica

Para aplicaciones específicas, se pueden conectar dispositivos auxiliares en la **Bornera Auxiliar:**

- **Bomba hidráulica con control de nivel:** flotante eléctrico o sonda de nivel con relé de nivel
- **Bomba hidráulica o neumática con control de presión:** presostato

---

## 4. Características Físicas

- Gabinete metálico: 300 × 200 × 150 mm / Peso: 5,2 Kg
- Selector ON/OFF en la puerta
- Bornera de entrada L1, L2, L3
- Bornera de contactor
- Bornera externa para auxiliares (control)
- Relé de protección integral GUCT integrado

---

## 5. Dimensiones Generales

- Medidas: 300 × 200 × 150 mm
- Peso: 5,2 Kg

---

## 6. Diagrama Básico de Instalación

```
Red Trifásica L1 L2 L3
       ↓
[BORNERA DE ENTRADA L1 L2 L3]
       ↓
[RELÉ DE PROTECCIÓN INTEGRAL GUCT]
Bornes 95 96 97 98 ← terminales de relé GUCT
       ↓
[SELECTOR ON/OFF]  [A1-A2 bobina contactor]
       ↓
[CONTACTOR]
       ↓
[BORNERA EXTERNA AUXILIAR → CARGA]
       ↓
Motor Trifásico
```

---

## 7. Ajuste de Parámetros del Protector GUCT

### 7.1 — Parámetros de Voltaje (preestablecidos por el fabricante)

- Bajo voltaje: 187 V~ (GMS-U 208V)
- Voltaje nominal: 208 V~
- Sobre voltaje: 228 V~

### 7.2 — Procedimiento de Configuración

Usar el teclado del relé GUCT para acceder al menú:

| Sección del menú | Parámetros |
|-----------------|------------|
| Ajuste Voltaje | Bajo volt., sobre volt., desbalance, frecuencia |
| Ajuste Corriente | Subcarga tipo, TD subcarga, TC subcarga, FS, salir |
| Ajuste Reloj | Programación horaria |
| Modo de Rearme | Manual / Auto |
| Cambio de Clave | Acceso al menú |
| Dirección Modbus | Comunicación |
| Borrar Histórico | Registro de fallas |
| Reiniciar Equipo | Restaurar valores de fábrica |

### 7.2.4 — Configuración del Modo de Rearme

- **Manual:** un operador debe presionar el botón Rearme para reconectar la carga después de una falla
- **Auto:** la carga se reconecta automáticamente después de establecidas las condiciones y los tiempos de espera

---

## 8. Vista General del Menú GUCT (pantalla de inicio)

```
BAJO VOLT. 187V
GUCT 208V 4A         2008 V1.14 SP
Pantalla Principal:
V12   V23   V31   VUB
 220   220   200    7%
I1    I2    I3    CUB
  2     2     2    0%
 I NOMINAL 2.0A
Medición: kW-kVA-PF-kWH
110.0kVA  100.0kW
0.80PF  290000kWH
```

---

## 9. Especificaciones Técnicas del Relé GUCT

### A. Voltaje de Alimentación

| Parámetro | Rango |
|-----------|-------|
| Modelos según voltaje de operación | 220 V~ / 480 V~ |
| Rango de operación del protector | 145-264 V~ / 312-672 V~ |
| Frecuencia de operación | 60 Hz ±10% |

### B. Ajustes de Protección por Corriente

| Código | Parámetro | Rango |
|--------|-----------|-------|
| c.27 | Ajuste nivel sobrecarga (OL) | 5% a 50% (ajustable) |
| c.28 | Ajuste de clase térmica | 5 a 30 (ajustable) |
| c.29 | Curva de caliente del motor | Según clase IEC 60255-8 |
| c.30 | Tiempo máximo entre curvas fría/caliente | 2 horas (IEC 60255-8-1990) |
| c.31 | Tiempo desconexión por sobrecarga | Según nivel de sobrecarga y clase — IEEE Std. |

---

## 10. Cómo Ordenar

```
GMS-U [VOLTAJE] [CORRIENTE] [SUPERVISIÓN]
  208 → 208/220 V~
  480 → 440/480 V~

Corriente:
  04 → 1-4 A (0,5-0,75 HP @ 208V / 0,5-2 HP @ 480V)
  12 → 3,5-12,5 A (0,75-3 HP @ 208V / 2-7,5 HP @ 480V)
  32 → 10-32 A (3-7,5 HP @ 208V / 7,5-20 HP @ 480V)
  80 → 25-80 A (7,5-25 HP @ 208V / 20-50 HP @ 480V)

Supervisión:
  S → Estándar
  U → Subcarga y Fallas de fases
```

---

## Diagramas

> Los diagramas de conexión completos, vistas del panel de instrumentos y las curvas de disparo por sobrecarga son gráficos en el PDF original. Fuente: `G:\Mi unidad\WorkspaceIA\RAG_SOURCES\Exceline_Profesional\I_GMS-U.pdf`
