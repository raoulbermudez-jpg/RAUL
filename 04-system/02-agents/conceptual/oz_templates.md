# Oz — Templates & Special Protocols

> Templates, casos típicos y protocolos especiales del agente
> `oz` (companion document). **Load on-demand:** cargar
> explícitamente solo cuando la tarea actual requiera aplicar un
> patrón canónico documentado aquí.
>
> Documento companion del conceptual SSOT principal en
> `04-system/02-agents/conceptual/oz.md` (§1-§10). El conceptual
> principal lleva pointer a este archivo en §11.

---

## 11. Special Protocols / Templates


### 11.1 Tareas tÃ­picas (referencia para inducciÃ³n)

1. **Redline de empaque GSM-MB con cambios tÃ©cnicos y de claim:** el
   Owner sube la hoja glasÃ© tiro+retiro y un brief con cambios (NTC con
   asterisco, badge Inverter Compatible, lengÃ¼eta nueva). Oz lee
   ambos, produce redline grÃ¡fico canÃ³nico (formato Â§6.4) + tabla delta
   + handoff a Oswaldo.

2. **Consistencia terminolÃ³gica en familia GST-R:** el Owner quiere que
   los 4 spec sheets de la lÃ­nea GST-R usen los mismos tÃ©rminos en todo
   momento (*"tensiÃ³n nominal"* siempre, nunca *"voltaje nominal"*). Oz
   revisa los 4 documentos, identifica todas las inconsistencias y
   entrega delta consolidado con correcciones por documento.

3. **Mejora de wording sin cambios de spec:** el Owner pide que el
   manual del GII+ sea mÃ¡s claro para distribuidores no tÃ©cnicos. Oz
   mejora la redacciÃ³n de cada secciÃ³n â€” sin cambiar ningÃºn valor
   tÃ©cnico â€” y entrega el delta para aprobaciÃ³n antes de pasarlo a
   Oswaldo.

4. **RevisiÃ³n editorial post-Renzo:** Renzo creÃ³ una guÃ­a de
   instalaciÃ³n del GOCT. El Owner quiere que Oz la revise para
   consistencia terminolÃ³gica con el spec sheet del GOCT, la formatee
   segÃºn los estÃ¡ndares de documentaciÃ³n Genteca, y produzca la versiÃ³n
   lista para publicaciÃ³n.

5. **Formalizar draft tÃ©cnico en spec sheet:** el Owner (o I&D) entrega
   un borrador en texto plano del nuevo GSPT-MV con valores tÃ©cnicos
   confirmados. Oz toma ese borrador y produce el spec sheet completo
   siguiendo la estructura y estilo de los documentos existentes en KB
   â€” listo para Oswaldo sin que el Owner tenga que maquetarlo.

6. **ReasignaciÃ³n de modelo + nueva lÃ­nea (caso GST-RG â†’ GST-RM /
   ProMotor):** el Owner instruye un cambio de naming + nuevos
   diferenciadores (curva inversa, badge crÃ­tico, color de fondo).
   Oz produce redline grÃ¡fico canÃ³nico (ver ejemplo vivo en
   `03-projects/genteca/2026-04_GST-R_etiquetas/01-strategy-and-design/REDLINE_GST-RM220_ETQ_T.pdf`),
   propuesta visual de mercado, tabla delta y handoff a Oswaldo.

### 11.2 Checklist de entrega antes de enviar brief a Oswaldo

Aplica a TODOS los tipos de brief. Verificar que Raul ha provisto todo
esto antes de generar el brief:

- [ ] CÃ³digo de producto confirmado (exacto â€” sin variaciones
  ortogrÃ¡ficas).
- [ ] Dimensiones confirmadas en mm (no estimaciones ni "igual que el
  anterior").
- [ ] Colores Pantone confirmados (no "verde parecido al del GST").
- [ ] Specs tÃ©cnicas validadas por Jhoswer / MartÃ­n / Vera (no
  borradores).
- [ ] Documento de referencia disponible (etiqueta / HDE anterior en KB
  o adjunto explÃ­cito).
- [ ] Deadline con fecha real (no "lo antes posible").
- [ ] Canal de revisiÃ³n definido: Â¿Oz revisa el borrador de Oswaldo
  antes que Raul, o va directo a Raul?

Si algÃºn Ã­tem estÃ¡ incompleto, Oz debe **seÃ±alarlo antes de redactar el
brief** y escalar a Raul.

### 11.3 Brief Templates (subconjunto inicial)

Los siguientes 4 templates corresponden a las piezas mÃ¡s frecuentes en
Genteca hoy. **No agotan el universo Â§2.1.** Cuando aparezca una pieza
fuera de estos cuatro casos, ver Â§11.4.

#### 11.3.1 Template Etiqueta Frontal

```markdown
# Brief Etiqueta Frontal â€” [CÃ“DIGO DE PRODUCTO]
**Fecha:** YYYY-MM-DD
**Solicitado por:** Raoul Bermudez
**Para:** Oswaldo (ogutierrez@genteca.com.ve)
**Deadline:** DD-MMM-YYYY

## Dimensiones
- Ancho: ___ mm
- Alto: ___ mm
- Sangrado: ___ mm (si aplica)

## Referencia base
- Archivo anterior: [nombre o "nuevo â€” sin referencia"]
- UbicaciÃ³n: [ruta en repo o Drive]

## Colores Pantone
- Color primario: Pantone ___
- Color secundario: Pantone ___
- Fondo: [color / blanco / transparente]

## Logo(s) a incluir
- [ ] Exceline Profesional (versiÃ³n: ___)
- [ ] Genteca (versiÃ³n: ___)
- [ ] NTC â€” ProtecciÃ³n TÃ©rmica (sÃ­ / no)
- [ ] Otro: ___

## JerarquÃ­a de badges (orden descendente de importancia visual)
1. [badge mÃ¡s prominente â€” texto exacto + posiciÃ³n sugerida]
2. [segundo badge]
3. [tercer badge]
4. (agregar los que correspondan)

## Voltajes a mostrar
- Rango de voltaje: ___ V a ___ V
- Formato requerido: [ej. "110Vâ€“240V" / "110/220V" / "Multivoltaje"]
- Voltajes venezolanos especÃ­ficos a destacar: [sÃ­ / no â€” cuÃ¡les]

## CÃ³digo(s) de modelo
- CÃ³digo exacto: ___
- Mostrar variantes en misma etiqueta: [sÃ­ / no â€” cuÃ¡les]

## Diferenciadores a destacar
- [diferenciador 1 â€” texto exacto o parÃ¡frasis aceptable]
- [diferenciador 2]

## Texto obligatorio
- PaÃ­s de fabricaciÃ³n: ___
- Avisos legales: ___
- Otros textos fijos: ___

## Formato de entrega
- [ ] PDF imprimible (CMYK)
- [ ] AI / EPS (editable)
- [ ] Ambos

## Notas adicionales para Oswaldo
[Cualquier instrucciÃ³n especÃ­fica que no caiga en los campos anteriores]
```

#### 11.3.2 Template Etiqueta Lateral

```markdown
# Brief Etiqueta Lateral â€” [CÃ“DIGO DE PRODUCTO]
**Fecha:** YYYY-MM-DD
**Solicitado por:** Raoul Bermudez
**Para:** Oswaldo (ogutierrez@genteca.com.ve)
**Deadline:** DD-MMM-YYYY

## Dimensiones
- Ancho: ___ mm
- Alto: ___ mm
- Sangrado: ___ mm

## Referencia base
- Archivo anterior: [nombre o "nuevo"]
- UbicaciÃ³n: ___

## Especificaciones tÃ©cnicas a incluir (valores confirmados por I&D)
| ParÃ¡metro | Valor |
|---|---|
| Voltaje de operaciÃ³n | ___ V |
| Corriente nominal | ___ A |
| Potencia mÃ¡xima | ___ W / VA |
| Frecuencia | ___ Hz |
| Temperatura de operaciÃ³n | ___Â°C a ___Â°C |
| [otros parÃ¡metros] | ___ |

## Funciones de protecciÃ³n a listar
- [protecciÃ³n 1]
- [protecciÃ³n 2]
- (completar segÃºn producto)

## Normativas a mencionar
- [ ] IEC ___ (especificar nÃºmero)
- [ ] COVENIN ___
- [ ] UL ___
- [ ] Ninguna por ahora

## CÃ³digo de barras / QR
- [ ] No incluir
- [ ] CÃ³digo de barras â€” nÃºmero: ___
- [ ] QR â€” URL destino: ___

## Texto obligatorio
- PaÃ­s de fabricaciÃ³n: ___
- Advertencias de seguridad: ___
- Batch code / lote: [campo en blanco para impresiÃ³n posterior / fijo]

## Formato de entrega
- [ ] PDF imprimible (CMYK)
- [ ] AI / EPS
- [ ] Ambos

## Notas adicionales para Oswaldo
___
```

#### 11.3.3 Template HDE (Hoja de Especificaciones)

```markdown
# Brief HDE â€” [CÃ“DIGO DE PRODUCTO]
**Fecha:** YYYY-MM-DD
**Solicitado por:** Raoul Bermudez
**Para:** Oswaldo (ogutierrez@genteca.com.ve)
**Deadline:** DD-MMM-YYYY

## Documento base
- [ ] ActualizaciÃ³n de HDE existente â€” archivo: ___
- [ ] HDE nueva (sin documento anterior)

## Fuente de especificaciones tÃ©cnicas
- Documento: [spec sheet en KB / brief de I&D / otro]
- Revisado por: [Jhoswer / MartÃ­n / Vera]
- Estado: [confirmado / pendiente de validaciÃ³n tÃ©cnica]

## Tabla de especificaciones (valores confirmados)
| ParÃ¡metro | Valor | Unidad |
|---|---|---|
| ___ | ___ | ___ |

## CaracterÃ­sticas / funcionalidades (bullets)
- [caracterÃ­stica 1]
- [caracterÃ­stica 2]

## Diagrama de conexiÃ³n
- [ ] No incluir
- [ ] Usar diagrama existente â€” archivo: ___
- [ ] Diagrama nuevo â€” descripciÃ³n: ___

## ImÃ¡genes del producto
- [ ] Foto disponible â€” archivo: ___
- [ ] Render 3D disponible â€” archivo: ___
- [ ] Dejar espacio para imagen (a proveer despuÃ©s)

## Audiencia primaria
- [ ] TÃ©cnicos de campo / instaladores
- [ ] Distribuidores
- [ ] Usuarios finales

## ExtensiÃ³n
- PÃ¡ginas: [1 pÃ¡gina / 2 pÃ¡ginas / sin lÃ­mite]
- Idioma: [espaÃ±ol / inglÃ©s / bilingÃ¼e]

## Notas tÃ©cnicas especiales
[Trip class, curvas IDMT, advertencias de instalaciÃ³n, etc. â€” solo si
aplica]

## Notas adicionales para Oswaldo
___
```

#### 11.3.4 Template GuÃ­a RÃ¡pida

```markdown
# Brief GuÃ­a RÃ¡pida â€” [CÃ“DIGO DE PRODUCTO]
**Fecha:** YYYY-MM-DD
**Solicitado por:** Raoul Bermudez
**Para:** Oswaldo (ogutierrez@genteca.com.ve)
**Deadline:** DD-MMM-YYYY

## Audiencia objetivo
- [ ] Instalador elÃ©ctrico
- [ ] TÃ©cnico de refrigeraciÃ³n / HVAC
- [ ] Usuario final no tÃ©cnico

## Formato fÃ­sico
- TamaÃ±o del papel: [A4 / carta / ___]
- Plegable: [sÃ­ â€” tipo: ___ / no]
- PÃ¡ginas: ___

## Pasos de instalaciÃ³n
(MÃ¡ximo 8 pasos. Texto exacto o borrador â€” Oz refina la redacciÃ³n.)

1. [paso 1]
2. [paso 2]
3. [...]

## Imagen requerida por paso
| Paso | DescripciÃ³n de la imagen |
|---|---|
| 1 | ___ |
| 2 | ___ |

## Advertencias crÃ­ticas (ANTES o DURANTE instalaciÃ³n)
- [advertencia 1 â€” texto exacto o descripciÃ³n]
- [advertencia 2]

## Diagrama de cableado
- [ ] No incluir
- [ ] Usar diagrama existente â€” archivo: ___
- [ ] Diagrama nuevo â€” descripciÃ³n de la conexiÃ³n: ___

## QR / cÃ³digo de acceso
- [ ] No incluir
- [ ] QR â€” URL destino: ___ [video / PDF / pÃ¡gina web]

## Idioma(s)
- [ ] Solo espaÃ±ol
- [ ] BilingÃ¼e espaÃ±ol / inglÃ©s

## Revisado por (contenido tÃ©cnico)
- Nombre: ___
- Fecha de validaciÃ³n: ___

## Notas adicionales para Oswaldo
___
```

### 11.4 AdaptaciÃ³n / extensiÃ³n de templates

Cuando aparezca una pieza fuera del subconjunto Â§11.3 (ej. counterpad
POP, dÃ­ptico de catÃ¡logo, PDF digital descargable, video script de
producto, cenefa de gÃ³ndola, dangler), Oz puede:

1. **Adaptar el template mÃ¡s cercano** aÃ±adiendo o quitando campos
   segÃºn corresponda al tipo de pieza. Ej.: para un counterpad POP,
   partir del template Etiqueta Frontal pero aÃ±adir campos de
   "ubicaciÃ³n en el PDV", "interacciÃ³n con producto fÃ­sico",
   "durabilidad esperada".
2. **Proponer un template nuevo a Raul/Owner** si el caso es recurrente
   (mÃ¡s de 2-3 piezas similares en pocos meses). La propuesta se
   registra como adiciÃ³n a Â§11.3 vÃ­a Michelina si requiere refinement
   formal del conceptual.

**Regla operativa invariable:** sea cual sea el tipo de pieza, **nunca
enviar brief con campos obligatorios vacÃ­os** (regla de Â§11.2).

### 11.5 Workflow Raul â†’ Oz â†’ Oswaldo

1. Raul entrega solicitud a Oz (ej. "brief etiqueta frontal GST-RM /
   redline empaque GSM-MB / propuesta visual nuevo POP").
2. Oz verifica el checklist Â§11.2 â€” seÃ±ala cualquier campo faltante a
   Raul antes de continuar.
3. Oz rellena el template aplicable de Â§11.3 (o adaptaciÃ³n Â§11.4) con
   la informaciÃ³n provista + datos del KB Genteca (specs, dimensiones
   de productos existentes).
4. Oz produce el output canÃ³nico solicitado (OC-1/OC-2/OC-3/OC-4 segÃºn
   corresponda).
5. Oz entrega el handoff package completo a Raul para aprobaciÃ³n antes
   de envÃ­o a Oswaldo.
6. Raul aprueba â†’ Oz envÃ­a a Oswaldo (CC: Raul, BCC: segÃºn reglas de
   comunicaciÃ³n externa Genteca).

**Objetivo operativo:** pasar de 4+ rondas de correcciÃ³n a 1â€“2 mÃ¡ximo,
eliminando ambigÃ¼edad desde el brief inicial.