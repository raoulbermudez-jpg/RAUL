---
cliente: Gama (Cadena de Supermercados Gama Express)
sector: Retail alimentario Venezuela
canal_consultoria: Cora Urrea (cora.urrea@gmail.com)
status: V0.1 — CANDIDATO. Requiere validación Cora / Gama antes de uso en pieza pública oficial
ultima_actualizacion: 2026-05-18
proposito: Spec visual para entregables Vivienne / DocBuilder / Atlas en proyectos Gama (Notoriedad 2026 + futuros)
---

# Brand Kit — Gama (V0.1 candidato)

> ⚠ **STATUS: V0.1 CANDIDATO.** Este brand kit se construye en colaboración con Cora basándose en observación de materiales públicos Gama + corrección post-V5/V6 ("rojo vino tinto, no rojo Gama"). **No usar para pieza pública oficial sin validación previa.** Para entregables a Cora (internos de la consultoría), aplicar y reportar discrepancias en cover note del VI-1 para feedback.

---

## 1. Paleta de color

### Primarios

| Rol | Hex | RGB | Uso |
|---|---|---|---|
| **Rojo Gama (primary)** | `#E30613` | 227, 6, 19 | Color firmante de marca. Logos, headers principales, énfasis crítico. **Rojo saturado y vibrante**, NO granate / vino tinto. |
| **Blanco** | `#FFFFFF` | 255, 255, 255 | Fondos limpios, espacio negativo, contraste sobre rojo |
| **Negro corporativo** | `#1A1A1A` | 26, 26, 26 | Texto cuerpo, ejes de chart. NO usar `#000000` puro (muy duro). |

### Secundarios (uso analítico / charts)

| Rol | Hex | Uso |
|---|---|---|
| **Gris medio** | `#6B6B6B` | Texto secundario, labels de chart, anotaciones |
| **Gris claro** | `#E5E5E5` | Fondos sutiles, líneas de gridline, separadores |
| **Ámbar alerta** | `#F2A900` | Highlight de hallazgos relevantes (no críticos), warnings suaves |
| **Verde validación** | `#2D8F47` | Confirmaciones, métricas positivas, "OK" |

### Anti-paleta (NO usar)

| Hex | Por qué no |
|---|---|
| `#7B1C1C` o similar granate / vino tinto | Confundido históricamente con Gama (caso V5/V6 2026-05-18). NO es rojo Gama. |
| `#FF0000` rojo puro | Excesivamente saturado, lectura visual agresiva |
| Cualquier rojo con tono naranja (`#FF4500`) | Lectura de marca incorrecta |
| Magentas (`#E91E63`) | No es la familia Gama |

### Paleta para charts comparativos (cadenas competidoras)

Cuando un chart compara Gama vs competidores (Páramo, Rio, Plan Suárez, Central Madeirense, etc.):

- **Gama:** `#E30613` siempre (color firmante)
- **Competidores:** paleta gris/azul neutra sin protagonismo:
  - Páramo: `#4A6FA5`
  - Rio: `#7C8B9B`
  - Plan Suárez: `#9CAEC0`
  - Central Madeirense: `#5B7090`
  - Forum: `#8FA3B8`
  - Plazas: `#6D8499`
  - Luz Marina: `#A8B9C7`
  - Otros: `#BCC9D4`

**Principio:** Gama nunca compite visualmente — siempre destaca por color, los competidores son una familia visual unificada.

---

## 2. Tipografía

### Principal

| Rol | Tipografía | Fallback | Uso |
|---|---|---|---|
| **Headers / títulos** | Montserrat Bold (700) | Calibri Bold, Arial Bold | Slide titles, section headers, key call-outs |
| **Sub-headers** | Montserrat SemiBold (600) | Calibri Light, Arial | Subtítulos, labels de bloque |
| **Body** | Open Sans Regular (400) | Calibri, Arial | Texto cuerpo, bullets, párrafos |
| **Caveats / nota** | Open Sans Italic (400) | Calibri Italic | Notas metodológicas, fuentes, caveats |
| **Charts (labels)** | Open Sans Regular (400) | Calibri, Arial | Ejes, leyendas, anotaciones de chart |

### Tamaños sugeridos (PPTX)

| Elemento | Tamaño |
|---|---|
| Slide title (header principal) | 32-36 pt |
| Sub-header | 22-26 pt |
| Body text | 16-18 pt (NUNCA <14 pt para audiencia ejecutiva) |
| Caveats / fuente | 10-12 pt |
| Chart axis labels | 11-13 pt |
| Chart data labels | 10-12 pt |

### Tamaños sugeridos (Word formal)

| Elemento | Tamaño |
|---|---|
| Heading 1 (capítulo) | 20-24 pt |
| Heading 2 (sección) | 16-18 pt |
| Heading 3 (sub-sección) | 13-14 pt |
| Body | 11 pt |
| Caveats / nota a pie | 9-10 pt |
| Chart inline | 10-11 pt labels |

---

## 3. Reglas visuales (do / don't)

### Do

- **Pirámide Minto explícita:** cada bloque temático tiene slide descriptiva (datos) → slide analítica (lectura). El cliente Gama pidió esto explícitamente en reunión 18/05/2026.
- **Infografía sobre bullets:** si un slide tiene relaciones / flujos / jerarquías → diagrama, no lista. Bullets son fallback (ver Vivienne §6.3 paso 2).
- **Gama destaca, competidores en familia neutra:** ver paleta charts comparativos arriba.
- **Caveats visibles** cuando n<30 o cualquier corte con base pequeña: flag "REFERENCIAL" + nota literal.
- **White space disciplinado:** un slide sparse no es vacío, es enfocado.
- **Charts de barras horizontales** preferidos sobre pie charts en rankings de marcas (más legibles).
- **Notas metodológicas anexas** (anexo del deck o documento metodológico separado) cuando se usan técnicas estadísticas no-triviales (z-test, BH-FDR, KDA, MDS, etc.).

### Don't

- **Rojo vino tinto / granate confundido con rojo Gama** (caso V5/V6 corregido).
- **Pie charts con >5 slices** — ilegibles.
- **Slides con >4 bullets sin justificación** — reformatear como diagrama/matriz.
- **Bloques de slides descriptivas sin slide analítica de cierre** — el lector se ahoga en datos.
- **Tipografías decorativas / serif elegantes** — no son Gama, Gama es retail accesible.
- **Fondos con textura o gradientes complejos** — limpieza visual antes que decoración.
- **Sombreado / efectos 3D en charts** — visual ruidoso, restar legibilidad.
- **Logo Gama con desproporciones o sobre fondo conflictivo** — usar siempre con clear-space + sobre blanco o sobre rojo Gama puro.

---

## 4. Aplicación en herramientas de producción

### matplotlib (charts)

Snippet recomendado para inicio de cualquier `make_charts.py` en proyectos Gama:

```python
import matplotlib.pyplot as plt

# Paleta Gama
GAMA_RED = '#E30613'
GAMA_BLACK = '#1A1A1A'
GAMA_GRAY_MID = '#6B6B6B'
GAMA_GRAY_LIGHT = '#E5E5E5'
GAMA_AMBER = '#F2A900'
GAMA_GREEN = '#2D8F47'

# Familia competidores (neutros azul-gris)
COMP_COLORS = {
    'Páramo': '#4A6FA5',
    'Rio': '#7C8B9B',
    'Plan Suárez': '#9CAEC0',
    'Central Madeirense': '#5B7090',
    'Forum': '#8FA3B8',
    'Plazas': '#6D8499',
    'Luz Marina': '#A8B9C7',
    'Otros': '#BCC9D4',
}

# Configuración global
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Open Sans', 'Calibri', 'Arial', 'DejaVu Sans'],
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.titleweight': 'bold',
    'axes.labelsize': 11,
    'axes.edgecolor': GAMA_GRAY_MID,
    'axes.linewidth': 0.8,
    'xtick.color': GAMA_BLACK,
    'ytick.color': GAMA_BLACK,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'grid.color': GAMA_GRAY_LIGHT,
    'grid.linewidth': 0.5,
})
```

### python-pptx (decks)

Helpers recomendados para `build_deck.py` en proyectos Gama:

```python
from pptx.dml.color import RGBColor
from pptx.util import Pt

GAMA_RED = RGBColor(0xE3, 0x06, 0x13)
GAMA_BLACK = RGBColor(0x1A, 0x1A, 0x1A)
GAMA_GRAY_MID = RGBColor(0x6B, 0x6B, 0x6B)
GAMA_GRAY_LIGHT = RGBColor(0xE5, 0xE5, 0xE5)

FONT_HEADER = 'Montserrat'  # Bold para títulos
FONT_BODY = 'Open Sans'      # Regular para body

TITLE_SIZE = Pt(32)
SUBHEADER_SIZE = Pt(22)
BODY_SIZE = Pt(16)
CAVEAT_SIZE = Pt(11)
```

### python-docx (Word)

Helpers para `build_word.py`:

```python
from docx.shared import RGBColor, Pt

GAMA_RED_DOCX = RGBColor(0xE3, 0x06, 0x13)
GAMA_BLACK_DOCX = RGBColor(0x1A, 0x1A, 0x1A)
GAMA_GRAY_MID_DOCX = RGBColor(0x6B, 0x6B, 0x6B)

H1_SIZE = Pt(22)
H2_SIZE = Pt(17)
H3_SIZE = Pt(13)
BODY_SIZE_WORD = Pt(11)
```

---

## 5. Items pendientes de validación con Cora / Gama

Este brand kit es V0.1 construido por inferencia y corrección post-V5/V6. Items que requieren validación directa antes de pieza pública oficial:

1. **Hex exacto del rojo Gama.** `#E30613` es la mejor aproximación a "rojo saturado vibrante" pedido por Cora, pero el manual de marca oficial de Gama (si existe) puede tener un Pantone / hex específico distinto. **Acción:** pedir a Cora si Gama tiene manual de identidad o si puede consultarlo internamente.
2. **Tipografía oficial.** Montserrat + Open Sans son inferencia razonable para retail moderno. Si Gama usa otra familia (ej. Roboto, Lato, una corporativa custom), reemplazar.
3. **Logo Gama oficial en alta resolución.** Pedir a Cora para uso en covers de deck / portadas de reporte.
4. **Color secundario corporativo de Gama** (si existe — algunas cadenas usan un segundo color además del rojo). Pendiente confirmar.
5. **Restricciones de uso del logo:** clear-space mínimo, fondos permitidos, versiones (monocromo / outline / etc.). Pendiente confirmar.

**Cuándo escalar:** cuando una pieza vaya a publicarse externamente por Gama (no solo a Cora como insumo de consultoría), validar los 5 items con Cora antes del render final.

---

## 6. Referencias cruzadas

- Vivienne SSOT: `04-system/02-agents/conceptual/vivienne.md` §6.1 paso 6 (brand kit pre-flight obligatorio)
- Memoria: `feedback_vivienne_token_explosion_pattern_v1` (workaround para decks grandes)
- Memoria: `feedback_external_consultancy_scoping_cycle` (workflow consultoría externa)
- Proyecto activo: `03-projects/consultoria-externa/gama-notoriedad-2026/`
- Drive cliente: `G:\Mi unidad\RAUL\colaboradores\Genteca\Cora-Urrea\02_De_Raoul_Para_Cora\`
