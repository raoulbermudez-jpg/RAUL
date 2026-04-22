---
title: "En el esquema mostrado a continuación, se presenta una aplicación"
type: Technical
source: "11_Biblioteca_Tecnica_CONTROL-DE-VACIADO-DE-TANQUE-CON-RELE-DE-NIVEL-Y-SUPERVISION-DE-VOLTAJE.pdf"
product_line: "Genteca"
date_processed: "2026-04-18"
---

# En el esquema mostrado a continuación, se presenta una aplicación

En el esquema mostrado a continuación, se presenta una aplicación
para el control y supervisión de voltaje de un sistema de vaciado de
tanque para una residencia o condominio. El mismo puede trabajar
a través de un sistema hidroneumático o de forma directa a la
acometida de agua principal. El tanque es surtido de agua de forma
externa y se controla el llenado del mismo con un flotante
mecánico.
Las características eléctricas y mecánicas de la bomba vendrán
dadas en función del líquido a transportar, el caudal a  manejar y la
distancia de traslado del líquido.
El montaje del supervisor de voltaje GSM-L 220 y del relé
GRN-MV  dentro del tablero de control se podrá hacer sobre un
riel DIN.
La utilización de un contactor para el manejo de la carga permite
que el diagrama presentado a continuación pueda ser utilizado en
equipos de distintas capacidades, siempre que el contactor se
dimensione de acuerdo a la carga que va a manejar.
EL FUNCIONAMIENTO DE LA APLICACIÓN SERÍA EL SIGUIENTE:
1. Mientras no se presente ninguna falla en el suministro eléctrico, los
contactos 5 y 6 del supervisor de voltaje GSM-L 220 permanecen
conectados, alimentando de esta forma al común (terminal 7) del
relé de nivel GRN-MV.
2. Si el líquido está por debajo del electrodo de nivel bajo, el relé no
va a permitir el encendido de la bomba. La bomba sólo podrá ser
alimentada si hay líquido en el tanque.
NOTA DE APLICACIÓN

VOLTAJE DE LA INSTALACIÓN:

220 V~
ALTO
BAJO
MEDIO
GRADO DE DIFICULTAD
LISTA DE EQUIPOS
SUPERVISOR MONOFÁSICO GSM-L
RELÉ DE NIVEL   GRN-MV
CONTROL PARA EVITAR FUNCIONAMIENTO EN VACÍO CON RELÉ
DE NIVEL Y SUPERVISIÓN DE VOLTAJE

Para evitar daños en la
bomba, es importante
impedir que trabaje en
vacío, monitoreando
constantemente el nivel
del tanque
El GRN-MV es un relé
electrónico diseñado para el
control de nivel de líquidos
conductores mediante sondas
existentes en la instalación.
• Sensibilidad ajustable mediante
perilla.
• Multivoltaje: 120 / 220 V~
•
Indicadores
luminosos:
alimentación y salida de
control activada.
• Compacto y fácil de instalar.
GRN-MV

Supervisor monofásico
• Protección contra sobre
voltaje y bajo voltaje.
• Ciclo de espera luego de una
falla: 3 minutos.
• Indicadores luminosos: ciclo
de espera, falla de voltaje y
voltaje normal.
• Voltaje mínimo de salida
ajustable.
• Compacto y fácil de instalar.
• Permite el manejo de cargas
por medio de contactor.
También permite el manejo
directo de equipos hasta 1 HP.
GSM-L

NOTA DE APLICACIÓN


Programador horario
diario/semanal
diseñado para la
automatización de
cargas eléctricas
accionadas por un
contactor
• Para
incorporar
la
funcionalidad de racionamiento
de acuerdo a un horario
establecido.
• Cuenta con pantalla LCD y
teclado
que
facilitan
la
programación de los eventos.
Se pueden programar hasta 20
eventos: 10 encendidos y 10
apagados.
GTC-B1C
Casos de falla:
1. Si se presenta alguna perturbación en el suministro eléctrico, bajo o alto
voltaje, los contactos 5 y 6 del supervisor de voltaje GSM-L 220 se
desconectan, por lo que no se alimenta el común del relé de nivel
GRN-MV, interrumpiendo la alimentación de la bobina del contactor. En
este caso, los contactos 6 y 7 del supervisor de voltaje GSM-L 220
permanecen conectados, encendiendo la luz piloto indicadora de falla de
voltaje.
2. Si el nivel del tanque está por debajo del electrodo de nivel bajo, se
desactiva la salida del relé, desconectando los terminales 7 y 8 (lo que
interrumpe la alimentación de la bobina del contactor) y conectando los
terminales 6 y 7 (encendido de la luz piloto indicadora de tanque vacío).
¿Es posible incorporar la función de racionamiento de agua, además del
control y supervisión de voltaje de mi sistema?
Sí, es posible. Entendiendo el racionamiento como la suspensión de
entrada de agua del exterior para llenar el tanque en un perÍodo de
tiempo indicado, se pueden configurar mediante el programador horario
GTC-B1C los días y las horas que se puede bombear agua hacia el
hidroneumático o acometida principal de agua.
SUMINISTRO DE
AGUA AL TANQUE
SUMINISTRO DE
AGUA HACIA
RESIDENCIA
BOMBA MONOFÁSICA
TANQUE
Bobina del
contactor de la
bomba
220 V
220 V
60 Hz
5
6
7
8
1
2
3
4
RELÉ DE NIVEL
Luz piloto
220 V
Tanque Vacío
Electrodo común
Electrodo bajo
M
Interruptor
5
6
7
8
1
2
3
4

SUPERVISOR
MONOFÁSICO
Luz piloto
220 V
Falla de voltaje
GSM-L 220
GRN-MV

NOTA DE APLICACIÓN

POR EJEMPLO:
Su empresa de servicio de agua decide por mantenimiento suministrar agua con el siguiente horario:
• De Lunes a Viernes sólo entrará agua al tanque en los horarios:
5:00am a 7:00am – 6:00pm a 9:00pm.
• Los días Sábados el horario será:
5:00am a 7:00am – 12:00pm a 2:00pm - 6:00pm a 9:00pm.
• Los Domingos no se tendrá racionamiento.
Suministro de agua normal.
Debido a esta medida usted decide controlar el suministro  hacia su condominio/vivienda con el siguiente horario:
• De Lunes a Viernes:
6:00am a 7:30am – 12:30pm a 2:00pm – 6:30pm a 9:00pm
• Los Sábados:
7:00am a 9:00am – 01:00pm a 03:00pm – 6:30pm a 9:30pm
• Los Domingos no habrá racionamiento.
El horario que usted decida para su período de racionamiento lo deberá programar en el GTC-B1C, dependiendo de la capacidad de su tanque
de agua y en función del número de puntos de agua a utilizar. Como el día domingo no hay racionamiento de agua, usted podrá colocar su
programador en MODO MANUAL ON, para permitir el bombeo de agua de forma continua, manteniendo la protección de voltaje activa
y el relé de nivel indicando la disponibilidad de agua.
A1
A2
6
4
5
TANQUE
220 V~
220 V
60 Hz
5
6
7
8
1
2
3
4
M
5
6
7
8
1
2
3
4
Luz piloto
220 V~
Falla de voltaje
Luz piloto
220 V~
Tanque vacío
GSM-L 220
SUPERVISOR
MONOFÁSICO
GRN-MV
RELÉ DE NIVEL
GTC-B1C MV
PROGRAMADOR HORARIO
Luz piloto
220 V
Racionamiento Activo
Bobina del
contactor de la
bomba
Interruptor
SUMINISTRO DE
AGUA AL TANQUE
SUMINISTRO DE
AGUA HACIA
RESIDENCIA
Electrodo bajo
Electrodo común
BOMBA MONOFÁSICA

NOTA DE APLICACIÓN

El funcionamiento de la aplicación con el programador horario
sería el siguiente:
1. Mientras no se presente ninguna falla en el suministro eléctrico, los
contactos 5 y 6 del supervisor de voltaje GSM-L 220 permanecen
conectados, alimentando de esta forma al común (terminal 7) del
relé de nivel GRN-MV.
2. Si el nivel del tanque está por encima del electrodo de nivel bajo, se
activa la salida del relé, conectando los terminales 7 y 8.
3. Al conectarse los terminales 7 y 8 del relé de nivel GRN-MV, se
alimenta el común (terminal 5) del programador horario GTC-B1C.

4. Cuando alguno de los eventos esté activo, el programador horario
GTC-B1C conectará los terminales 4 y 5, de esta forma se energiza
la bobina de control del contactor, permitiendo la conexión de la
bomba.
5. Mientras no haya ningún evento activo, el programador horario
GTC-B1C conectará los terminales 5 y 6, encendiendo la luz piloto
que indica que no hay suministro de agua hacia la residencia o
condominio (racionamiento activo).
Casos de falla:
1. Si se presenta alguna perturbación en el suministro eléctrico, bajo o
alto voltaje, los contactos 5 y 6 del supervisor de voltaje GSM-L
220 se desconectan, por lo que no se alimenta el común del relé de
nivel GRN-MV, interrumpiendo la alimentación de la bobina del
contactor. En este caso, los contactos 6 y 7 del supervisor de voltaje
GSM-L 220 permanecen conectados, encendiendo la luz piloto
indicadora de falla de voltaje.
2. Si el nivel del tanque está por debajo del electrodo de nivel bajo, se
desactiva la salida del relé, desconectando los terminales 7 y 8 (lo
que interrumpe la alimentación de la bobina del contactor) y
conectando los terminales 6 y 7 (encendido de la luz piloto
indicadora de tanque vacío).
