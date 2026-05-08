# Bibliografía técnica — Motores trifásicos y protecciones

**Total:** 22 fuentes curadas en 4 bloques temáticos
**Estado de acceso:** ~95% acceso abierto verificado al 2026-05-07
**Origen:** compilada por el Owner durante el desarrollo del proyecto ProtMotores (2026-03) e integrada al wiki técnico de Genteca tras auditoría Vera 2026-05-07

> **Nota de uso:** las URLs deben verificarse antes de cualquier cita en material externo. Las fuentes IEC/NEMA pueden tener ediciones más recientes que las citadas a continuación; usar la vigente al momento de la cita.

---

## Bloque 1 — Motores trifásicos: fundamentos, desequilibrio y fallas

**9 fuentes** | PMC: 2 · MDPI: 6 · Wiley Open Access: 1

- **https://pmc.ncbi.nlm.nih.gov/articles/PMC6510962/**
  Ibitowa O.A. et al. (2019). *Dataset on the performance of a three phase induction motor under balanced and unbalanced supply voltage conditions.* Data in Brief. PMC Free Article.
  Datos experimentales motor trifásico con 0-5% desequilibrio. Referencia directa para el argumento del monitor de red.

- **https://pmc.ncbi.nlm.nih.gov/articles/PMC12526899/**
  *Advancements in Induction Motor Fault Diagnosis and Condition Monitoring: A Comprehensive Review* (2025). PMC Free Article.
  Revisión completa de métodos de diagnóstico. Estado del arte 2025.

- **https://www.mdpi.com/2075-1702/9/9/203**
  Cherif H. et al. (2021). *Three-Phase Induction Motors Online Protection against Unbalanced Supply Voltages.* Machines, 9(9), 203. MDPI Open Access.
  Detección online de desequilibrio con componentes simétricas.

- **https://www.mdpi.com/2075-1702/9/1/2**
  Moreira A.B. et al. (2021). *Thermal Analysis of Low-Power Three-Phase Induction Motors Operating under Voltage Unbalance and Inter-Turn Short Circuit Faults.* Machines, 9(1), 2. MDPI Open Access.
  Análisis térmico FEM. Justificación PTC vs relé corriente.

- **https://www.mdpi.com/1996-1073/17/24/6324**
  Piechocki M. et al. (2024). *Induction Motors Under Voltage Unbalance Combined with Voltage Subharmonics.* Energies, 17(24), 6324. MDPI Open Access.
  Pulsaciones par/vibración bajo desequilibrio + subarmónicos. Relevante para red venezolana.

- **https://www.mdpi.com/1996-1073/17/1/8**
  Tabora J.M. et al. (2024). *Exploring the Effects of Voltage Variation and Load on the Electrical and Thermal Performance of Motors.* Energies, 17(1), 8. MDPI.
  Subtensión/sobretensión con diferentes cargas. Análisis técnico-económico-térmico.

- **https://www.mdpi.com/1996-1073/15/23/9232**
  Guasch-Pesquer L. et al. (2022). *Improved Method for Determining Voltage Unbalance Factor Using Induction Motors.* Energies, 15(23), 9232. MDPI.
  Método amperimétrico como alternativa al voltimétrico.

- **https://www.mdpi.com/1996-1073/17/2/387**
  Ewert P. et al. (2024). *Microcontroller-Based Embedded System for the Diagnosis of Stator Winding Faults and Unbalanced Supply Voltage.* Energies, 17(2), 387. MDPI.
  Sistema embebido bajo costo (ARM Cortex-M4) para detección de fallas.

- **https://onlinelibrary.wiley.com/doi/10.1155/2022/7423018**
  Shaikh S. et al. (2022). *Protection System Design of Induction Motor for Industries.* Modelling and Simulation in Engineering. Hindawi/Wiley Open Access.
  Comparación NEMA/IEEE/IEC del desequilibrio de tensión.

---

## Bloque 2 — Protecciones: dispositivos, coordinación y selección

**8 fuentes** | Publicaciones técnicas abiertas de industria

- **https://www.pumpsandsystems.com/pump-protection**
  *Pump Protection: Electronic vs. Bimetallic Overload Relays.* Pumps & Systems.
  Diferencias bimetálico vs electrónico. ERA study sobre causas de falla.

- **https://www.pumpsandsystems.com/microprocessor-based-pumpmotor-protection-relays**
  *Microprocessor-Based Pump/Motor Protection Relays.* Pumps & Systems.
  Por qué un sumergible en seco tiene BAJA corriente, no alta — argumento PTC.

- **https://www.thedriller.com/articles/86540-three-phase-pump-and-motor-protection**
  *Three-Phase Pump and Motor Protection.* The Driller.
  Tiempos de respuesta relé sobrecarga vs monitor de fases. Curva de derating NEMA.

- **https://www.piprocessinstrumentation.com/pumps-motors-drives/article/15563645/what-a-pumps-motor-protection-relay-is-trying-to-say**
  *What a Pump's Motor Protection Relay is Trying to Say.* PI Process Instrumentation.
  Interpretación de señales de disparo. Función de retardo de reinicio.

- **https://www.electrical4u.com/motor-thermal-overload-protection/**
  *Motor Thermal Overload Protection.* Electrical4U.
  Principio operación protección térmica. Causas de sobrecalentamiento.

- **https://www.eaton.com/content/dam/eaton/products/industrialcontrols-drives-automation-sensors/overload-relays/User's%20Guide%20to%20IEC%20Type%201%20and%20Type%202%20Coordination.PDF**
  *User's Guide to IEC Type 1 and Type 2 Coordination.* Eaton Corporation.
  Definición y diferencias coordinación Tipo 1 / Tipo 2. Tablas selección guardamotores.

- **https://minilecgroup.com/understanding-overload-protection-and-its-types-in-motor-pump-protection-relays/**
  *Understanding Overload Protection and its Types in Motor/Pump Protection Relays* (2023). Minilec Group.
  Comparación bimetálico vs electrónico con funciones adicionales.

- **https://minilecgroup.com/motor-pump-protection-relays/**
  *3-Phase Motor Protection Relays with Current Sensing.* Minilec Group.
  Lista completa funciones relés electrónicos.

---

## Bloque 3 — Aplicaciones: bombeo, refrigeración y máquinas rotativas

**3 fuentes** | Publicaciones técnicas y recursos de fabricantes

- **https://cyclestopvalves.com/pages/pump-and-motor-protection-devices**
  *Pump and Motor Protection Devices.* Cycle Stop Valves, Inc.
  Análisis protección bombas. Por qué relé sobrecarga no protege marcha en seco.

- **https://www.se.com/us/en/download/document/ECT204/**
  Schneider Electric. *Cahier Technique No. 204: LV Protection Devices and Variable Speed Drives.*
  Protección motores con VFD. Coordinación en circuitos con VFD.

- **https://www.se.com/us/en/download/document/ECT207/**
  Schneider Electric. *Cahier Technique No. 207: Electric Motors — How to Improve Their Control and Protection.*
  Métodos de protección y control de motores eléctricos. Guía técnica completa.

---

## Bloque 4 — Manuales y guías de fabricantes

**2 fuentes** | Documentos técnicos abiertos

- **https://static.weg.net/medias/downloadcenter/ha0/h5f/WEG-motors-specification-of-electric-motors-50039409-brochure-english-web.pdf**
  WEG Equipamentos Elétricos S.A. *Specification of Electric Motors* (50039409). Descarga gratuita.
  Guía completa especificación motores: par, potencia, eficiencia, aislamiento (Arrhenius), IP, regímenes.

- **https://electrical-engineering-portal.com/download-center/books-and-guides/schneider-electric**
  *Schneider Electric MV/LV Technical Guides and Studies.* Electrical Engineering Portal.
  Acceso centralizado a Cahiers Techniques de Schneider.

---

## Resumen estadístico

| Tipo | Cantidad |
|---|---|
| Total fuentes | 22 |
| PMC (siempre libres) | 2 |
| MDPI (siempre libres) | 6 |
| Wiley/Hindawi Open Access | 1 |
| Publicaciones técnicas industria (abiertas) | 8 |
| Documentos técnicos fabricantes (acceso libre) | 5 |

**Verificadas como acceso libre:** 21/22 (~95%).
**1 fuente con acceso variable:** se.com/ECT207 (puede requerir registro Schneider).

## Normas adicionales referenciadas

Las normas siguientes son de pago (IEC, NEMA, IEEE) pero se citan cuando aplica. Las versiones académicas pueden estar disponibles en IEEE Xplore con suscripción.

- **IEC 60034-1** — Rotating electrical machines: Rating and performance.
- **IEC 60034-5** — Degrees of protection (IP Code) for rotating machines.
- **IEC 60947-2** — Low-voltage circuit-breakers.
- **IEC 60947-4-1** — Contactors and motor-starters.
- **IEC 60947-5-1** — Control circuit devices.
- **NEMA MG1** — Motors and Generators (incluye sec. 12.44 voltage variation, sec. 12.45 unbalanced voltages).
- **NEMA ICS 2** — Industrial control: Controllers, Contactors, and Overload Relays Rated 600V.
- **IEEE Std 3004.8** — Recommended Practice for Motor Protection in Industrial and Commercial Power Systems.
- **COVENIN 159** — Instalaciones Eléctricas en Edificaciones.
- **COVENIN 3028** — Motores eléctricos de corriente alterna: Motores trifásicos de inducción de jaula.
- **COVENIN 3445** — Norma venezolana aplicable a dispositivos de supervisión y protección eléctrica (relevante para línea Exceline Profesional).

## Referencias clásicas adicionales

- **Chapman, S.J.** (2012). *Máquinas Eléctricas* (5ª edición). McGraw-Hill. Texto universitario, biblioteca técnica.
- **Dakin, T.W.** (1948). *Electrical Insulation Deterioration Treated as a Chemical Rate Phenomenon.* AIEE Transactions, Vol. 67, pp. 113-122. Origen científico de la regla de los 10°C (Arrhenius) para vida útil del aislamiento.

---

**Última actualización:** 2026-05-07 — versión inicial integrada desde Atlas 8 (legacy 2026-03).
