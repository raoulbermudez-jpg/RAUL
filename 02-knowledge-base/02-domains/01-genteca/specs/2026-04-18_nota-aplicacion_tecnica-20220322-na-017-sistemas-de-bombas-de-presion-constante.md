---
title: "y su duración."
type: Technical
source: "11_Biblioteca_Tecnica_20220322_NA-017-SISTEMAS-DE-BOMBAS-DE-PRESION-CONSTANTE.pdf"
product_line: "Genteca"
date_processed: "2026-04-18"
---

# y su duración.

[ 2 ] Veriﬁque el ajuste de voltaje mínimo y máximo recomendado por el fabricante, dado que algunos equipos pueden ser hasta del
+/-5%
[ 1 ] La capacidad de protección es similar entre un GI+ y GII+, con la diferencia de que, al elegir un GII+, se podrá programar eventos
como un racionamiento, ya que cuenta con control horario y permite la visualización de las fallas incluyendo la hora a la que ocurrió
y su duración.
www.genteca.com.ve
excelinevzla
NOTA DE APLICACIÓN
NA 2022/03-V1-017
Protección para bombas de presión constante
controladas con variadores de frecuencia
En las ediﬁcaciones residenciales o comerciales, se espera que el caudal de agua suministrado en
cualquier punto sea siempre igual sin importar cuántas personas utilizan el agua de forma
simultánea, por esto, muchas ediﬁcaciones optan por los sistemas de presión constante. Estos
equipos cuentan con un variador de frecuencia, que a medida que cambia el consumo de agua,
incrementa o disminuye la velocidad del motor con la ﬁnalidad de mantener la presión constante.
Estos sistemas, al igual que cualquier dispositivo conectado a la electricidad, pueden verse
afectados por las fallas de voltaje en la red eléctrica y los picos de alta energía, lo que
alteraría la continuidad del suministro de agua.
A continuación, exponemos el esquema de conexión y los productos que se requieren
para garantizar la protección de este sistema:
Un Relé Trifásico de Protección Contra Fallas de fase (GI+) o un Relé Trifásico de Protección
contra Fallas de Fase con Control Horario (GII+). Ambos equipos supervisan constantemente
el voltaje de las líneas y desconectan completamente el variador de la red ante la presencia
fallas de voltaje como: voltaje alto o bajo, desbalance fase invertida, fase pérdida o una
variación de frecuencia después
[ 1 ].
Tres módulos de supresión de picos de alta energía (GMP5-35), para evitar que los equipos se
vean afectados por los transitorios rápidos producto de las descargas atmosféricas o de la
conmutación de las subestaciones eléctricas. El modelo de este equipo se selecciona de
acuerdo al voltaje de la instalación.
Un contactor de acuerdo a los requerimientos de voltaje y corriente de la instalación (Este
equipo no se encuentra dentro de nuestra oferta de productos).
Esquema de conexión
El esquema de conexión para la protección del sistema de presión constante consiste en un
Relé de Protección contra Fallas de Fase (GI+ o GII+) que realizará la apertura de un
contactor, cuando ocurra una falla y realizará la conexión cuando el estado de la red eléctrica
sea adecuado, de forma automática sin la intervención del personal técnico. Al momento de
instalarlo, es importante veriﬁcar los ajustes de los siguientes parámetros en la
conﬁguración del relé:
01
MODO DE
REARME
UMBRAL DE
VOLTAJE BAJO
[2]
UMBRAL DE
VOLTAJE ALTO
[2]
% DE
DESBALANCE
% VARIACIÓN DE
FRECUENCIA
TIEMPO DE
DETECCIÓN
TIEMPO DE
CONEXIÓN
AUTO
+10% Voltaje
nominal
-10% Voltaje
nominal
4
2
1 S
>  180 S

Asimismo en este esquema, los supresores de picos de alta energía están conectados entre
fase y tierra y serán los encargados de drenar a tierra cualquier transitorio rápido, evitando
que este llegue al variador de frecuencia o al sistema de bombas.
Sistema trifásico
208 VAC
GI+208S
GMP5-3520
Relé de protección contra fallas de fase 208/220 V~
Supresor de Picos 280 V~
GI+480S
GMP5-3540
Relé de protección contra fallas de fase 440/480 V~
Supresor de Picos  440 V~
Sistema trifásico
480 VAC
www.genteca.com.ve
excelinevzla
NOTA DE APLICACIÓN
NA 2022/03-V1-017
02
L3
L2
L1
Tierra
Sensor
de Presión
SISTEMA HIDRAULICO
BOMBAS Y TUBERIAS

RECOMENDACIONES
Es importante incluir rutinas de mantenimiento para la inspección del estado de los
supresores de picos, cuando la ventana de identificación de los GMP5-35 está en rojo,
indica que este debe ser sustituido.
El calibre del cable para la conexión de los supresores de picos es un punto importante a
cuidar en esta instalación, se recomienda en este caso que sea mínimo AWG 10, siendo el
máximo permitido AWG 6.
Verifique la existencia y calidad de la conexión a tierra del sistema eléctrico, es importante
para garantizar la apropiada protección ante una descarga de alta energía.
Mantenga siempre las protecciones independientes por sistema en sus instalaciones, por
ejemplo, la iluminación y el aire acondicionado Algunos equipos requieren condiciones
especiales de protección, además evita que, al regresar la energía, todos los equipos
conecten simultáneamente produciendo una alta demanda de energía que podría
ocasionar desconexiones indeseadas por voltaje bajo.
La selección del contactor es básica para la seguridad y confiabilidad de cualquier
aplicación, al igual que el uso del tamaño del cable apropiado para el consumo de
corriente. Verifique puntos como:
Cantidad de Polos: En este caso deben ser tres polos
Categoría: AC1 para cargas resistivas o AC3 para cargas inductivas.
Corriente: en caso de no tener la corriente nominal de la instalación puede realizar la
medición de la corriente por fase y seleccionar el contactor de capacidad superior
comercialmente.
Bobina del Contactor: Se dimensiona en función del voltaje de la señal de control.
Contactos auxiliares: Permiten señales del estado del contactor, es importante definir
si se requiere normalmente cerrados (NC) o normalmente abiertos (NO)
www.genteca.com.ve
excelinevzla
NOTA DE APLICACIÓN
03
NA 2022/03-V1-017
Para conocer más acerca de nuestros equipos y sus aplicaciones visite www.genteca.com.ve.
En caso de cualquier inquietud a contactarnos directamente a través del correo info@genteca.com.ve
Información Adcional
1.
2.
3.
4.
5.
▶
▶
▶
▶
▶
