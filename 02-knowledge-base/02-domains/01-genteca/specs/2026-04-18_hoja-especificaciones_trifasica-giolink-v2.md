---
title: "GIO-Link DESCRIPCIÓN GENERAL"
type: Technical
source: "04_Proteccion_Trifasica_GIOLINK-V2.pdf"
product_line: "Genius"
document_type: "hoja-especificaciones"
product_code: "GIO-LINK"
date_processed: "2026-04-18"
---

# GIO-Link DESCRIPCIÓN GENERAL

GIO-Link DESCRIPCIÓN GENERAL
GIO-Link es un conjunto de dispositivos de comunicación previstos para que las familias de Relés (Relevadores) de Protección,
intercambien información con equipos terminales maestros y computadores compatibles, que dispongan un software de supervisión e interfaz al usuario (software
a ser provisto por el cliente). Los dispositivos GIO-Link están diseñados con componentes que proveen aislación, permitiendo la interconexión de datos, en
condición de seguridad eléctrica entre los equipos y usuarios.
GIO-Link PARTES Y PIEZAS ALTERNATIVAS
2
GIO-PLUG-USB
GIO-Link
GIO-A-RS485K
GIO-A-RS232K
ATENCIÓN: Para la utilización adecuada de estos
dispositivos, el usuario debe tener conocimientos de
comunicación serial e integración de equipos, en específico de
los estándares RS485 y RS232.
ALERTA: Sólo personal técnico calificado con conocimientos
en Relé (Relevadores) de protección y la carga asociada debería
realizar la instalación, arranque y mantenimiento del sistema.
Hacer caso omiso podría resultar en lesiones a personas y/o
daños a los equipos conectados.
ATENCIÓN: Los equipos Terminales o de Computación, con
los cuales se instalará la comunicación con los Relés (Relevadores)
de Protección, deben disponer un puerto de comunicación serial,
y tener un software de supervisión compatible con el Protocolo
MODBUS RTU, en modo Maestro.
GIO-PLUG-RJ45
GIO-PLUG-USB
GIO-PLUG-RJ45
GIO-A-RS485K
GIO-A-RS232K
Conector, que provee aislación eléctrica y comunica a un Relé (Relevador) de Protección, directamente con un Terminal maestro o
Computador, a través de su puerto USB.
Conector, que provee aislación eléctrica y conecta un Relé (Relevador) de Protección, con un Adaptador o Concentrador  intermedio, del
conjunto GIO-Link.
Conjunto de Adaptador que convierte señales de datos de los Relés (Relevadores) de Protección, en señales compatibles con un
Bus de Comunicación, bajo estándar RS-485 (incluye cable GIO-Plug).
Conjunto de Adaptador que convierte señales de datos de los Relés (Relevadores) de Protección, en señales compatibles con un
Puerto de Comunicación, bajo estándar RS-232 (incluye cable GIO-Plug).
(Para mayor información lea la sección 5, acerca de las distintas configuraciones alternativas, para la comunicación de datos)
PRECAUCIÓN: Los dispositivos deben ser instalados en
lugar accesible, libre de polvo, sucio, humedad y vibraciones.
SOLO DE USO INTERIOR.
GIO-Link MONTAJE
3
Los dispositivos adaptadores y conectores de GIO-Link pueden ser montados en cualquier posición, sin restricciones en cuanto a orientación. No se
requieren orificios ni tornillos para la fijación. El Instalador puede organizar y sujetar las piezas y cables mediante el uso de correas o cintas de nylon o similar.
MANUAL DE INSTALACIÓN
1/4
GIO-Link  MV-02-0011-8.02-S
1

GIO-Link DIMENSIONES GENERALES
4
Modelo GIO-A-RS485K
4.1 Dimensiones de los conectores GIO-PLUG
24mm
4.2 Dimensiones de los Adaptadores
42,7mm
74,5mm
5.1 Sistema GIO-Link con estándar RS-232
Alternativa para comunicar un (1) solo RELÉ (RELEVADOR) DE PROTECCIÓN, por cada puerto serial tipo COM RS-232 disponible en un Terminal o
Computadora.
- Adaptador, modelo GIO-A-RS232K        (una pieza)
- Conector, modelo GIO-PLUG-RJ45    (una pieza)
5.2 Sistema GIO-Link con estándar RS-485
Alternativa para comunicar de uno (1) a treinta y dos (2) RELÉ (RELEVADORES) DE PROTECCIÓN, a través de un Bus de Comunicación tipo RS-485, que
se encuentre adaptado al Terminal o Computadora.
Opción A: Mediante Adaptadores del conjunto GIO-Link.
Con esta opción, a cada Relé (Relevador) de Protección se asigna un Adaptador.
- Conector, modelo  GIO-PLUG-RJ45
- Adaptador, modelo  GIO-A-RS485K
- Convertidor RS-232/RS-485 (Nota 1) (uno por Computador)
5.3 Sistema GIO-Link con estándar USB
Alternativa para comunicar de uno a varios RELÉS (RELEVADORES) DE PROTECCIÓN, a través de puertos USB, mediante el siguiente adaptador acoplado
al Terminal o Computadora:
- Conector, modelo GIO-PLUG-USB
Nota 1: Software de Supervisión, Terminales o Computadores y Convertidores tipo RS-232/RS-485, son equipos y partes a ser provistas por el usuario.
GIO-Link CONFIGURACIONES ALTERNATIVAS PARA LA COMUNICACIÓN DE DATOS
5
MODELO
Conector GIO-PLUG-RJ45
Conector GIO-PLUG-USB
Adaptador GIO-A-RS485K
Adaptador GIO-A-RS232K
DIMENSIONES
Cable   60 cm
Cable 200 cm
7,45 x 4,27 x 2,02 cm
7,07 x 4,27 x 2,34 cm
PESO
0,062Kg
0,085Kg
0,034Kg
0,037Kg
23,48mm
32,5mm
30mm
40mm
59,8mm
Modelo GIO-A-RS232K
42,7mm
70,7mm
20,2mm
2/4
GIO-Link  MV-02-0011-8.02-S
} NOTA: uno para cada Relé (Relevador)

GIO-Link DIAGRAMAS DE CONEXIÓN
6
ATENCIÓN: Verifique cuidadosamente las conexiones de los
cables, para asegurar que ninguno exceda el limite de voltaje nominal
de operación (12  V c.d.). Errores en las conexiones pueden
originar una operación incorrecta, o daños a los dispositivos
Dependiendo de las alternativas, los dispositivos de GIO-Link pueden conectarse de las siguientes maneras:
6.1 Diagrama de conexión para sistema GIO-Link con estándar RS-232
Cable de comunicación RS-232
RELÉ
(RELEVADOR)
GIO PORT
CONECTOR
GIO-PLUG-RJ45
ADAPTADOR
GIO-A-RS232K
TERMINAL O COMPUTADOR
6.2 Diagrama de conexión para sistema GIO-Link con estándar RS-485
GIO PORT
IMPEDANCIA DE TERMINACIÓN
PARA AMBOS EXTREMOS
DEL BUS CABLEADO
Cable de comunicación RS-232
COMPUTADOR
PE
GND (0V)
S- (B)
S+ (A)
+12V
ADAPTADOR
GIO-A-RS485K
1
2
3
4
5
ADAPTADOR
GIO-A-RS485K
1
2
3
4
5
PE
GND (0V)
S- (B)
S+ (A)
+12V
1 nF
120
1 nF
120
OPCIÓN A: Mediante ADAPTADORES
DB-9
CONVERTIDOR
RS-485/RS232
FUENTE DE PODER
(a ser provisto por el
usuario)
UN ADAPTADOR
GIO-A-RS485K
POR RELÉ
(RELEVADOR)
GIO PORT
GIO PORT
HASTA 32
RELÉ
(RELEVADORES)
UN CONECTOR
GIO-PLUG-RJ45
POR RELÉ
(RELEVADOR)
BUS RS-485
3/4
GIO-Link  MV-02-0011-8.02-S

GIO-Link ESPECIFICACIONES TÉCNICAS
9
NOTA: Las especificaciones y descripciones mostradas en este documento están sujetas a cambio sin previo aviso.
Puerto de Comunicación
Tipo de Conector
Máxima cantidad de
Relevadores por adaptador
Protocolo de Comunicación
GIO-A-RS232K
DB-9
1
c.1
c.2
c.3
c.4
C) Comunicaciones y Otras Funciones Especiales
GIO-A-RS485K
Terminales de Bornera
32
MODBUS RTU, 9600 8N1
D) Compatibilidad Electromagnética para Ambiente Industrial
Severo,
Estándares
de
Inmunidad
y
Emisiones
Descarga Electrostática
Inmunidad a Ruido Eléctrico Radiado
Transientes Rápidas
Perturbaciones Conducidas
Campos Magnéticos
Perturbaciones eléctricas, 1Mhz
Perturbaciones Conducidas,
Modo común (0-150 Khz)
d.1
d.2
d.3
d.4
d.5
d.6
d.7
IEC 61000-4-2
IEC 61000-4-3
IEC 61000-4-4
IEC 61000-4-6
IEC 61000-4-8
IEC 60255-22-1
IEC 61000-4-16
IEC 60255-22-7
IEC 60255-5
IEC 60255-5
UL IEC 60255-5
IEC 60255-5
UL 508
UL-94
B) Condiciones Ambientales, Límites de Operación e Instalación
-5 ºC a 55 ºC (23 ºF a 131 ºF)
-10 ºC a + 70 ºC (14 ºF a 158 ºF)
85% R.H.
Grado 3
Categoría III, 4KV
500V
5 KV
2,5 KV 50/60 Hz@1min
VO
Polímeros: LEXAN 500R
Sin Restricciones
Plano, M2.5
0,4 Nm (4,0 Kgfcm)
AWG 14 hasta AWG 30
b.1
b.2
b.3
b.4
b.5
b.6
b.7
b.8
b.9
b.10
b.11
b.12
b.13
b.14
b.15
b.16
b.17
b.18
Temperatura Ambiental  (Operación)
Temperatura Ambiental (Almacenaje)
Humedad Relativa Máxima
Nivel de Contaminación
Protección contra Exceso de Voltaje
Voltaje de Aislamiento Nominal
Prueba de Impulso
Prueba Dieléctrica
Grado de Protección al Fuego de la Carcaza
Material de la Carcaza
Posiciones de Montaje
Tipo de Tornillo
Torque de Apretado de Borneras
Cableado de Borneras
MODELO
Conector GIO-PLUG-RJ45
Conector GIO-PLUG-USB
Adaptador GIO-A-RS485
Adaptador GIO-A-RS232
DIMENSIONES
Cable 60 cm
Cable 200 cm
7,45 x 4,27 x 2,02 cm
7,07 x 4,27 x 2,34 cm
PESO
0,062Kg
0,085Kg
0,034Kg
0,037Kg
GIO-A-RS232K
Autoalimentación
2 mA
Contínuo
A) Alimentación
Modelos
Alimentación
Límite de Operación
Consumo promedio
Modo de operación
a.1
a.2
a.3
a.4
a.5
GIO-A-RS485K
Fuente auxiliar externa
7-12 V c.d.
10 mA
Contínuo
GIO-Link AJUSTE DE PARÁMETROS
7
Los conectores y adaptadores GIO-Link no requieren ajustes
físicos (“hardware”). Para el funcionamiento, configure el software y/o
manejadores de comunicaciones (“drivers”) que se tenga
previsto utilizar, con los siguientes parámetros:
7.1 Parámetros para el uso de los dispositivos
GIO-PLUG-RJ45 y GIO-A-RS485K:
Ajuste el controlador del puerto de comunicación provisto en el terminal o
Computador maestro, para que funcione con los siguiente valores:
Protocolo

MODBUS RTU
Velocidad de transmisión:
9600 Baudios
Longitud por palabra:
8
Paridad:

N
BIT de parada:

1
7.2 Parámetros para el uso del dispositivo GIO-PLUG-USB
Para utilizar el conector GIO-PLUG-USB directamente en cualquier
puerto USB de un Computador maestro, lea las instrucciones contenidas
por separado, en el MANUAL DE USUARIO GIO-Tool.
GIO-
PLUG-USB
A-RS485K
A-RS232K
Tool
Conector con cable, para comunicar por USB a
un Relevador de Protección, con un Computador.
Conjunto de Adaptador, para enlazar un
Relé (Relevador) de Protección, con un Bus de
comunicación RS485, incluye cable
GIO-Plug.
Conjunto de Adaptador, para enlazar un
Relé (Relevador) de Protección, con un Puerto
de comunicación RS232, incluye cable
GIO-Plug.
Software, para monitorizar, configurar y generar
reportes, con los Relé (Relevadores) de Protección.
COMO ORDENAR GIO-Link
Los conectores y adaptadores GIO-Link permiten que los RELÉS
(RELEVADORES) DE PROTECCIÓN de la marca puedan comunicarse,
con otros equipos Terminales maestros o Computadores de supervisión,
mediante el uso del PROTOCOLO MODBUS-RTU y adaptadores apropiados.
Mediante el protocolo MODBUS-RTU los Relés (Relevadores) de Protección
intercambian
información
con
otros
dispositivos
maestros,
conectados en un Bus de comunicación.  Los dispositivos que monitorizan
o controlan, tales como Terminales o Computadores  se denominan
MAESTROS, mientras que los RELÉS (RELEVADORES) DE PROTECCIÓN
se asignan como ESCLAVOS.
Los RELÉS (RELEVADORES) DE PROTECCIÓN comunican en un esquema
denominado UNICAST.  Cuando un Terminal maestro interroga o remite
comandos al Relevador, después de recibida y cumplida la instrucción,
el Relé (Relevador) retorna una respuesta de confirmación al Terminal maestro.
Un Bus de comunicación con estándar RS485 puede enlazar hasta 32
Relé (Relevadores). Si se requieren instalaciones con mayores cantidades,
se pueden aplicar dispositivos repetidores estándares, para extender
el alcance.
GIO-Link OPERACIÓN
8
4/4
GIO-Link  MV-02-0011-8.02-S
Generación
de Tecnología
Diseñado por:
Fabricado en la República Bolivariana de Venezuela por
GENTE, Generación de Tecnología, C.A., RIF: J-00223173-4
Av. El Buen Pastor cruce con calle Vargas, Edif. Alba, Piso 1,
Local 1-A, Boleíta Norte, Caracas - Venezuela, Zona Postal 1070.
Telf.: ++(58 212) 237.07.11 / Fax: ++(58 212)  235.24.97
E-mail: genteven@genteca.com.ve / www.genteca.com.ve
