# URLs BIBLIOGRAPHY — PROTECCIONES ELÉCTRICAS PARA MOTORES TRIFÁSICOS

**Proyecto:** ProtMotores | Versión 1.0 | Marzo 2026
**Archivo:** Para documentación del proyecto, bibliografía y referencia humana

---

NOTA: Este archivo es para documentación y referencia humana.
Para cargar en NotebookLM, usar el archivo: ProtMotores_URLs_CopyPaste_NotebookLM.txt

**Total: 22 fuentes verificadas en 4 bloques temáticos**

---

## BLOQUE 1 — MOTORES TRIFÁSICOS: FUNDAMENTOS, DESEQUILIBRIO Y FALLAS
(9 fuentes | PMC: 2 | MDPI: 6 | Wiley Open Access: 1)

### https://pmc.ncbi.nlm.nih.gov/articles/PMC6510962/
Ibitowa O.A. et al. (2019). Dataset on the performance of a three phase induction motor under balanced and unbalanced supply voltage conditions. Data in Brief. PMC Free Article.
Contenido: Datos experimentales de un motor trifásico operando con 0-5% de desequilibrio de tensión. Parámetros eléctricos y mecánicos medidos a diferentes valores de deslizamiento. Referencia de datos para los 6 escenarios de desequilibrio normalizados por NEMA. Directamente relevante para el argumento del monitor de red.

### https://pmc.ncbi.nlm.nih.gov/articles/PMC12526899/
Advancements in Induction Motor Fault Diagnosis and Condition Monitoring: A Comprehensive Review (2025). PMC Free Article.
Contenido: Revisión completa de métodos de diagnóstico de fallas en motores de inducción. Clasificación de fallas eléctricas (desequilibrio, monofásico, sobre/subtensión, secuencia inversa, sobrecarga, cortocircuito interno) y mecánicas. Técnicas de detección: MCSA, análisis de vibración, imágenes térmicas. Publicación reciente (2025) con estado del arte actualizado.

### https://www.mdpi.com/2075-1702/9/9/203
Cherif H. et al. (2021). Three-Phase Induction Motors Online Protection against Unbalanced Supply Voltages. Machines, 9(9), 203. MDPI Open Access.
Contenido: Método de detección online de desequilibrio de tensión usando componentes simétricas. Validación experimental para múltiples condiciones de operación. Comparación con indicadores de la literatura. Relevante para la selección de umbrales en monitores de red.

### https://www.mdpi.com/2075-1702/9/1/2
Moreira A.B. et al. (2021). Thermal Analysis of Low-Power Three-Phase Induction Motors Operating under Voltage Unbalance and Inter-Turn Short Circuit Faults. Machines, 9(1), 2. MDPI Open Access.
Contenido: Análisis térmico por elementos finitos del motor bajo desequilibrio de tensión y cortocircuito entre espiras. Confirma que las herramientas de diagnóstico convencionales pueden no proporcionar el tiempo de aviso suficiente. Relevante para la justificación del PTC vs relé de corriente.

### https://www.mdpi.com/1996-1073/17/24/6324
Piechocki M. et al. (2024). Induction Motors Under Voltage Unbalance Combined with Voltage Subharmonics. Energies, 17(24), 6324. MDPI Open Access.
Contenido: Análisis de pulsaciones de par y vibración de motores de inducción bajo desequilibrio combinado con subarmónicos. Investigación experimental y FEM. Contexto: La red venezolana presenta ambas condiciones simultáneamente.

### https://www.mdpi.com/1996-1073/17/1/8
Tabora J.M. et al. (2024). Exploring the Effects of Voltage Variation and Load on the Electrical and Thermal Performance of Motors. Energies, 17(1), 8. MDPI.
Contenido: Análisis de motores bajo subtensión y sobretensión con diferentes cargas. Análisis técnico, económico y térmico. Cuantifica el impacto de la variación de tensión en eficiencia, factor de potencia y temperatura. Directamente relevante para el contexto de subtensión en Venezuela.

### https://www.mdpi.com/1996-1073/15/23/9232
Guasch-Pesquer L. et al. (2022). Improved Method for Determining Voltage Unbalance Factor Using Induction Motors. Energies, 15(23), 9232. MDPI.
Contenido: Método alternativo para determinar el Factor de Desequilibrio de Tensión usando el Factor de Desequilibrio de Corriente del motor. Validación con 20 puntos de desequilibrio en 3 motores. Base técnica para el uso del relé electrónico (amperimétrico) como alternativa/complemento al monitor voltimétrico.

### https://www.mdpi.com/1996-1073/17/2/387
Ewert P. et al. (2024). Microcontroller-Based Embedded System for the Diagnosis of Stator Winding Faults and Unbalanced Supply Voltage. Energies, 17(2), 387. MDPI.
Contenido: Sistema embebido de bajo costo basado en microcontrolador ARM Cortex-M4 para detección de fallas de estátor y desequilibrio de tensión usando flujo axial. Posibilidad de distinguir entre cortocircuito interno y desequilibrio de tensión.

### https://onlinelibrary.wiley.com/doi/10.1155/2022/7423018
Shaikh S. et al. (2022). Protection System Design of Induction Motor for Industries. Modelling and Simulation in Engineering. Hindawi/Wiley Open Access.
Contenido: Diseño de sistema de protección industrial contra monofásico y sobrecalentamiento. Comparación de definiciones NEMA, IEEE e IEC de desequilibrio de tensión. Prototipo de protección con detección de monofásico, subtensión y sobretensión.

---

## BLOQUE 2 — PROTECCIONES: DISPOSITIVOS, COORDINACIÓN Y SELECCIÓN
(8 fuentes | Publicaciones técnicas abiertas de industria)

### https://www.pumpsandsystems.com/pump-protection
Pumps & Systems. Pump Protection: Electronic vs. Bimetallic Overload Relays.
Contenido: Diferencias entre relés de sobrecarga bimetálicos y electrónicos. Modelo térmico dinámico vs bimetálico. Causas principales de falla de motores (ERA study: overload, single phasing, phase imbalance, ground fault). Referencia técnica directa para la justificación del relé electrónico en aplicaciones de bombeo.

### https://www.pumpsandsystems.com/microprocessor-based-pumpmotor-protection-relays
Pumps & Systems. Microprocessor-Based Pump/Motor Protection Relays.
Contenido: Funciones de los relés electrónicos modernos: protección de marcha en seco (baja corriente en sumergibles), fuga a tierra, monitoreo de temperatura con sensores RTD/PTC, comunicaciones. Por qué un motor sumergible que opera en seco tiene BAJA corriente, no alta — argumento clave para la venta del PTC.

### https://www.thedriller.com/articles/86540-three-phase-pump-and-motor-protection
The Driller. Three-Phase Pump and Motor Protection.
Contenido: Tiempos de respuesta de relés de sobrecarga (hasta 20s para monofásico) vs monitores de fases electrónicos (respuesta inmediata). Curva de derating de HP por desequilibrio de tensión (NEMA). Curva de reducción de vida útil del motor por desequilibrio. Referencia con datos numéricos directamente usables en argumentos de venta.

### https://www.piprocessinstrumentation.com/pumps-motors-drives/article/15563645/what-a-pumps-motor-protection-relay-is-trying-to-say
PI Process Instrumentation. What a Pump's Motor Protection Relay is Trying to Say.
Contenido: Interpretación de las señales de disparo del relé de protección. Curva de operación del motor a diferentes tensiones (Figura 1: tensión vs corriente). Explicación práctica de cada tipo de disparo: stall, sobrecarga térmica, jam. Función de retardo de reinicio para pozos que necesitan recuperación de nivel.

### https://www.electrical4u.com/motor-thermal-overload-protection/
Electrical4U. Motor Thermal Overload Protection.
Contenido: Principio de operación de la protección térmica de sobrecarga. Tipos de relés (bimetálico, RTD). Circuito de control con bobina del contactor y contactos NC en serie. Causas de sobrecalentamiento: sobrecarga, rotor bloqueado, subtensión, monofásico, desequilibrio, variaciones bruscas de tensión. Referencia didáctica en inglés.

### https://www.eaton.com/content/dam/eaton/products/industrialcontrols-drives-automation-sensors/overload-relays/User's%20Guide%20to%20IEC%20Type%201%20and%20Type%202%20Coordination.PDF
Eaton Corporation. User's Guide to IEC Type 1 and Type 2 Coordination.
Contenido: Definición y diferencias entre coordinación Tipo 1 y Tipo 2 según IEC 60947. Comparación con estándares UL y CSA. Tablas de selección de guardamotores por HP. Criterios de pass/fail para cada tipo de coordinación. Referencia técnica de fabricante.

### https://minilecgroup.com/understanding-overload-protection-and-its-types-in-motor-pump-protection-relays/
Minilec Group. Understanding Overload Protection and its Types in Motor/Pump Protection Relays (2023).
Contenido: Comparación entre protección de sobrecarga térmica (bimetálica) y electrónica. Funciones adicionales: voltaje, monofásico, secuencia inversa, marcha en seco (underload), rotor bloqueado, desequilibrio, falla a tierra. Criterios de selección por tipo de aplicación.

### https://minilecgroup.com/motor-pump-protection-relays/
Minilec Group. 3-Phase Motor Protection Relays with Current Sensing.
Contenido: Descripción de relés electrónicos de protección trifásica. Lista completa de funciones de protección. Diferencias vs relé térmico estándar. Incluye PTC, falla de fase, secuencia inversa, sub/sobretensión, falla a tierra. Referencia de producto aplicable directamente a la especificación de protección de motores.

---

## BLOQUE 3 — APLICACIONES: BOMBEO, REFRIGERACIÓN Y MÁQUINAS ROTATIVAS
(3 fuentes | Publicaciones técnicas y recursos de fabricantes)

### https://cyclestopvalves.com/pages/pump-and-motor-protection-devices
Cycle Stop Valves, Inc. Pump and Motor Protection Devices.
Contenido: Análisis de protección de bombas superficiales y sumergibles. Por qué los relés de sobrecarga no protegen marcha en seco (corriente baja, no alta). Clasificación de relés: Clase 10 para sumergibles, Clase 20 para superficiales. Dispositivos de protección específicos para bombas. Perspectiva práctica del instalador.

### https://www.se.com/us/en/download/document/ECT204/
Schneider Electric. Cahier Technique No. 204: LV Protection Devices and Variable Speed Drives. Rueil-Malmaison: Schneider Electric.
Contenido: Protección de motores con variadores de frecuencia (VFD). Fenómenos específicos en instalaciones con VFD. Protección de cortocircuito, sobrecarga y coordinación en circuitos con VFD. Relevante para motores con control de velocidad variable en sistemas de bombeo y ventilación.

### https://www.se.com/us/en/download/document/ECT207/
Schneider Electric. Cahier Technique No. 207: Electric Motors — How to Improve Their Control and Protection. Rueil-Malmaison: Schneider Electric.
Contenido: Métodos de protección de motores eléctricos, control de arranque, selección de protecciones. Guía técnica completa de Schneider Electric disponible gratuitamente. Directamente usable como referencia técnica de alto nivel para la base de conocimiento.

---

## BLOQUE 4 — MANUALES Y GUÍAS DE FABRICANTES (REFERENCIA TÉCNICA)
(2 fuentes | Documentos técnicos abiertos de WEG)

### https://static.weg.net/medias/downloadcenter/ha0/h5f/WEG-motors-specification-of-electric-motors-50039409-brochure-english-web.pdf
WEG Equipamentos Elétricos S.A. Specification of Electric Motors (50039409). Jaraguá do Sul: WEG. Descarga gratuita.
Contenido: Guía completa de especificación de motores WEG: conceptos fundamentales, par, potencia, eficiencia, clases de aislamiento (Arrhenius aplicado), grados de protección IP, regímenes de servicio, selección por aplicación. Guía didáctica en inglés con aplicaciones prácticas para la selección de motores.

### https://electrical-engineering-portal.com/download-center/books-and-guides/schneider-electric
Electrical Engineering Portal. Schneider Electric MV/LV Technical Guides and Studies.
Contenido: Colección completa de Cahiers Techniques de Schneider Electric disponibles para descarga. Incluye guías de protección de motores, coordinación de protecciones, redes industriales, calidad de energía. Punto de acceso centralizado a toda la documentación técnica gratuita de Schneider.

---

## RESUMEN DE FUENTES

- Total fuentes: 22
- PMC (siempre libres): 2
- MDPI (siempre libres): 6
- Wiley/Hindawi Open Access: 1
- Publicaciones técnicas industria (abiertas): 8
- Documentos técnicos fabricantes (acceso libre): 5
- Porcentaje acceso libre verificado: ~95% (21/22)
- 1 fuente pendiente verificación: se.com/ECT207 (Schneider puede requerir registro)

---

**FIN DEL ARCHIVO BIBLIOGRAPHY**
Proyecto ProtMotores | Versión 1.0 | Marzo 2026
