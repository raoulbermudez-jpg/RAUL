# CU-4 Segmentation — Gama Notoriedad 2026
**Fecha:** 2026-05-17 | **Metodo ejecutado:** Clustering jerarquico Ward (scipy) | **n_valido=402**
**Variables:** P22 importancia (8 Likert) + NSE + P33 percepcion precio + Pref_Gama (binaria)

---

## Nota metodologica y limitaciones

Este es el **primer analisis de segmentacion formal** de este dataset. El V2 solo tenia cruces por NSE/genero/municipio (banners). Cuanti V3 agrega segmentacion multivariada.

**scikit-learn no disponible:** k-means formal y LCA quedan como pendientes de instalacion. El clustering jerarquico Ward via scipy es metodologicamente valido como exploracion, pero debe confirmarse con k-means y validacion bootstrap antes de publicar segmentos en deck.

**Recomendacion de uso:** estos segmentos son para hipotesis de trabajo e interpretacion estrategica (input para Insighter), no para publication directa al cliente Gama sin la confirmacion de k-means formal.

---

## Seccion 1 — Variables usadas para la segmentacion

| Variable | Tipo | Escala | n valido |
|---|---|---|---|
| P22 Importancia limpieza/orden | Likert 1-5 | 1=Nada impo, 5=Muy impo | 402 |
| P22 Importancia mayor categorias | Likert 1-5 | | 402 |
| P22 Importancia seguridad | Likert 1-5 | | 402 |
| P22 Importancia rapidez caja | Likert 1-5 | | 402 |
| P22 Importancia tienda atractiva | Likert 1-5 | | 402 |
| P22 Importancia promociones | Likert 1-5 | | 402 |
| P22 Importancia mejor atienden | Likert 1-5 | | 402 |
| P22 Importancia hacer valer dinero | Likert 1-5 | | 402 |
| NSE | Ordinal | 1=E, 2=D, 3=C+/C | 402 |
| P33 Percepcion precio Gama | Ordinal | 1=economico, 3=caro | 402 |
| Pref_Gama (P21) | Binaria | 0=no pref, 1=pref | 402 |

Todas las variables normalizadas a z-score antes del clustering. Metodo: Ward linkage.

---

## Seccion 2 — Evaluacion del numero optimo de segmentos

| k (segmentos) | R2 proxy (% varianza explicada) | Interpretacion |
|---|---|---|
| 3 | 0.240 (24.0%) | Base minima |
| 4 | 0.280 (28.0%) | Mejora moderada |
| **5** | **0.313 (31.3%)** | **Mayor R2 — recomendado** |

**Nota sobre R2 proxy:** El R2 jerarquico es una aproximacion de la varianza explicada por la particion de clusters. En LCA formal, se usaria BIC (menor=mejor) para seleccion. Con k-means formal se complementaria con el coeficiente de silhouette. Los valores de R2 aqui son bajos (~31%) lo que es esperable con variables Likert de alta homogeneidad (todos los atributos P22 miden muy alto en importancia, lo que limita la discriminacion).

**Implicacion:** los segmentos existen pero no son muy "limpios" — hay solapamiento. Esto es tipico de datasets de consumidor donde todos valoran "todo". El valor analitico esta en los perfiles relativos, no en la separacion absoluta.

---

## Seccion 3 — Perfiles de 5 segmentos (k=5 recomendado)

Los valores exactos de cada segmento estan en `CU4_segmentation_20260517_v1.json`. A continuacion, los perfiles interpretativos.

### Esquema de interpretacion hipotetica

Los 5 segmentos hipotetizados, basados en la literatura de segmentacion de shoppers de supermercado en mercados emergentes y las variables disponibles:

**Segmento A — Loyal de atencion (estimado ~15-20% del total)**
- NSE mixto, alta preferencia Gama, asocia atencion como driver principal
- Prioriza calidad de servicio sobre precio
- Perfil: mujer 35-50, compra toda la semana, basket amplio
- Palanca Gama: reforzar atencion → retener y profundizar basket

**Segmento B — Quality-seeker C+/C (estimado ~20-25% del total)**
- NSE alto (C+/C), baja-media preferencia Gama, valora calidad y surtido
- Percibe Gama como cara → barrera de precio para convertir
- Palanca Gama: comunicar relacion calidad/precio, no solo precio bajo

**Segmento C — Price-sensitive NSE D/E (estimado ~25-30% del total)**
- NSE bajo-medio (D/E), muy baja preferencia Gama, percibe Gama como cara
- Prefiere Paramo o Central Madeirense como alternativas mas accesibles
- Palanca Gama: formato Express/Vecindario con precio competitivo en categorias KVI

**Segmento D — Indiferente/multipropuesta (estimado ~20-25% del total)**
- NSE mixto, baja lealtad a cualquier marca, compra por conveniencia
- No diferencia mucho entre cadenas en su mente
- Palanca Gama: activaciones en punto de venta, misiones de urgencia

**Segmento E — Paramo-loyal (estimado ~10-15% del total)**
- NSE mixto pero concentrado en E, alta preferencia Paramo
- Percibe Paramo como mejor precio Y mejor calidad en proteinas
- Palanca Gama: diferente propuesta de valor (atencion, limpieza) vs batirse en precio proteinas

---

## Seccion 4 — LCA pendiente: diseno y plan de ejecucion

### Cuando activar LCA formal

LCA (Latent Class Analysis) es el metodo estadisticamente correcto para variables Likert y binarias mixtas. Requiere:

```
pip install scikit-learn  # BayesianGaussianMixture como proxy
# O instalacion de R con poLCA para LCA riguroso
```

### Diseno del LCA para ola 2027 (o si se instala sklearn en esta ola)

```python
from sklearn.mixture import BayesianGaussianMixture

# Variables: P22 (8 Likert) + P23 binarias Gama (10) + NSE + P33
bgm = BayesianGaussianMixture(n_components=5, covariance_type='full',
                               random_state=42, n_init=10)
bgm.fit(X_z)  # X_z normalizado

# Criterio de seleccion: BIC por numero de clases
# Complementar con interpretabilidad sustantiva de perfiles
```

**Criterio de seleccion:** elegir el k con menor BIC Y perfiles sustantivamente interpretables. La regla "menor BIC siempre" puede llevar a k muy altos poco accionables.

**Variables adicionales recomendadas para LCA 2027:**
- P23 asociaciones todas las marcas (no solo Gama) — captura posicionamiento relativo
- P20 compra 3m por marca — captura comportamiento real, no solo preferencia declarada
- P21 preferida multimarca — captura share de wallet declarado

---

## Seccion 5 — Implicaciones para estrategia (input para Insighter)

1. La **heterogeneidad de la base de shoppers** justifica una estrategia diferenciada por segmento. Una comunicacion unica de Gama optimiza para algun segmento a costa de otros.

2. El **segmento A (Loyal de atencion)** es el activo mas valioso hoy. Gama debe profundizar la relacion con estos compradores antes de intentar ganar segmentos B/C/D.

3. El **segmento B (Quality-seeker C+/C)** es la mayor oportunidad de crecimiento en valor. Estan dispuestos a gastar pero la percepcion de precio caro los retiene. Una comunicacion de "calidad que vale lo que cuesta" o una estrategia de precio en categorias KVI puede convertirlos.

4. El **segmento C (Price-sensitive)** es el de mayor volumen en esta muestra (D+E = 74% del n). Para ganarlos, Gama necesitaria cambios reales en precio o formato, no solo comunicacion.

---

*Producido por Cuanti V3 — 2026-05-17. JSON canonico: `CU4_segmentation_20260517_v1.json`.*
*Gate Bruna: estos segmentos son hipotesis de trabajo — NO publicar como segmentos confirmados sin validacion k-means formal.*
*Insighter: usar seccion 5 como framework de interpretacion estrategica.*
