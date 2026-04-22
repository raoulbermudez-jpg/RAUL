---
title: "funcionamiento del"
type: Technical
source: "11_Biblioteca_Tecnica_SistemaHIDRONEUMATICO-RacionamientoHORARIO-ProteccionINTEGRAL-USANDO-DosBOMBAS-TRIFASICAS.pdf"
product_line: "Genius"
date_processed: "2026-04-18"
---

# funcionamiento del

funcionamiento del
compresor de acuerdo al
nivel de líquido en el
tanque presurizado
•
Sensibilidad
ajustable
mediante perilla.
• Multivoltaje: 120/220 V~
•
Indicadores
luminosos:
alimentación y salida de
control activada.
• Compacto
y
fácil
de
instalar.
NOTA DE APLICACIÓN

VOLTAJE DE LA INSTALACIÓN:

220 V~
ALTO
BAJO
MEDIO
GRADO DE DIFICULTAD
LISTA DE EQUIPOS
SUPERVISOR MONOFÁSICO GSM-L

SISTEMA HIDRONEUMÁTICO CON RACIONAMIENTO HORARIO Y PROTECCIÓN
INTEGRAL USANDO ALTERNANCIA DE DOS BOMBAS TRIFÁSICAS
Los sistemas hidroneumáticos son utilizados para impulsar agua a
presión desde un tanque hasta los puntos del edificio donde es
requerido el servicio. Los elementos principales que conforman
un sistema hidroneumático son:
• Bombas: Succionan el agua del tanque de almacenamiento y
la impulsan hacia el tanque presurizado.
PARA GARANTIZAR EL CORRECTO FUNCIONAMIENTO DE UN SISTEMA HIDRONEUMÁTICO ES NECESARIO PROTEGER CADA UNA DE SUS PARTES
Protección de la bomba
contra fallas de corriente
y voltaje
• Protege contra sobrecargas,
sobre voltaje, bajo voltaje,
desbalances, pérdida de fase
y fase invertida.
• Protección por tercera falla
de corriente.
• Permite visualizar los estados
de operación y fallas en
un computador, mediante
protocolo MODBUS RTU
(requiere adaptador GIO-Plug).
Control de la bomba
de acuerdo al nivel
de líquido
• Protege la bomba de
operaciones indebidas en
tareas de llenado y vaciado
de tanques.
• Cuenta con tres cables con
contactos SPDT: un cable
común,
un
cable
para
apagado en nivel máximo y
un cable para apagado en
nivel mínimo, de acuerdo a la
aplicación a implementar.
Protección del motor del
compresor de aire
• Protección contra sobre
voltaje y bajo voltaje.
• Ciclo de espera luego de
una falla: 3 minutos.
• Compacto y fácil de instalar.
• Permite el manejo de cargas
por medio de contactor.
También permite el manejo
directo de equipos hasta 1
HP.


GFE-MV
GSM-L
GRN-MV
GOCT
• Tanque presurizado: Dentro de éste hay un volumen de aire que
el agua bombeada comprime hasta que la presión alcanza un
nivel máximo preestablecido.
• Compresor de aire: Repone el volumen de aire que se escapa
mezclado con el agua, evitando que el tanque pierda su capacidad
de presurizar el sistema.
• Presostato: Controla los niveles de presión del sistema.
SUPER TÉRMICO GOCT
FLOTANTE ELÉCTRICO GFE-MV
PROGRAMADOR HORARIO GTC-B1C

RELÉ DE NIVEL GRN-MV
RELÉ ALTERNADOR GRA-MV

NOTA DE APLICACIÓN


Control del
funcionamiento del
compresor de acuerdo al
nivel de líquido en el
tanque presurizado
• Multivoltaje: 120/220 V~.
• Cada vez que el dispositivo
detecta un cambio de cerrado
a abierto entre sus entradas 3
y 2, genera una actuación
sobre los contactos de su
etapa de salida, cambiando su
posición.
• Compacto y fácil de instalar.

GRA-MV
Racionamiento horario
•
Para
incorporar
la
funcionalidad de racionamiento
de acuerdo a un horario
previamente establecido.
• Cuenta con pantalla LCD
y teclado que facilitan la
programación de los eventos.
Se pueden programar hasta
20 eventos: 10 encendidos y
10 apagados.
GTC-B1C
FUNCIONAMIENTO
Por medio del interruptor de racionamiento, el usuario selecciona
de forma manual el modo de funcionamiento del sistema. Si el
usuario activa el racionamiento, se enciende una luz indicadora
(racionamiento funcionando) y el sistema funcionará solamente en
las horas establecidas en el programador horario GTC-B1C. Si el
usuario desactiva el racionamiento, se apaga la luz indicadora y el
programador horario deja de tener influencia en el funcionamiento
del sistema.

Si se presenta alguna falla de voltaje o corriente en la alimentación
de alguna de las dos bombas, el respectivo relé GOCT
desconectará el equipo e indicará que hay una falla por medio del
encendido de una alarma (alarma bomba 1 o alarma bomba 2).
Si no hay ninguna falla en el suministro eléctrico de las bombas, cada
relé GOCT conectará sus contactos 97 y 98, alimentando uno de
los terminales de la bobina de su respectivo contactor.
De acuerdo a la señal de control del presostato que está
monitoreando el nivel de presión del tanque presurizado, se
activarán de forma alternada la bomba 1 y la bomba 2, encendiendo
sus respectivos indicadores de funcionamiento, siempre y cuando
haya agua en el tanque de suministro (flotante hacia arriba).
Por otra parte, cuando el nivel de agua dentro del tanque
presurizado alcance el electrodo de nivel alto, se activa la salida del
relé de nivel GRN-MV, permitiendo el arranque del compresor de
aire siempre que los niveles de voltaje sean los adecuados. Caso
contrario, el protector GSM-L interrumpirá la alimentación del
compresor y se encenderá una luz indicadora de falla de voltaje.

DIAGRAMA DE CONEXIONES
En el esquema mostrado a continuación, se presenta una aplicación para el control y protección integral de un sistema hidroneumático
usando alternancia de dos bombas trifásicas con racionamiento horario.
SISTEMA HIDRONEUMÁTICO CON RACIONAMIENTO HORARIO Y PROTECCIÓN INTEGRAL USANDO ALTERNANCIA DE DOS
BOMBAS TRFÁSICAS
NOTA DE APLICACIÓN


Interruptor
contra corto
K2
PRESOSTATO
BAJA
PRESIÓN
Contactor
Bomba 1
Contactor
Bomba 2
Bomba 2
en funcionamiento
K1
Bomba 1
en funcionamiento
Alarma
Bomba 1
Alarma
Bomba 2
Tablero
Encendido
Racionamiento
Funcionando
Falla de voltaje
Compresor
Compresor
Encendido
Compresor
de Aire
Tanque
Presurizado
Relé de Protección Integral
Relé de Protección Integral
Programador Horario
Relé Alternador
Relé de Nivel
Protector Monofásico de
Voltaje
Bomba 1
Bomba 2
K1
K2
PRESOSTATO
ALTA
PRESIÓN
AZÚL
NEGRO
MARRÓN
L1
L2
L3
95
96
97 98
L1
A1 A2
A2
A2
4
A2
5
A2
6
L2
L3
95
96
97 98
SWITCH SPDT
RACIONAMIENTO
FLOTANTE
ELÉCTRICO
GFE-MV
ELECTRODO
BAJO
TANQUE DE SUMINISTRO
DE AGUA
ELECTRODO
COMÚN
GSM-L
SUMNISTRO 3F
208 / 220 V
L1  L2  L3
I1      I2      I3
I1      I2      I3
SISTEMA HIDRONEUMÁTOCO CON RACIONAMIENTO DE HORARIO Y
PROTECCIÓN INTEGRAL GENIUS USANDO ALTERNANCIA DE DOS
BOMBAS TRIFÁSICOS

PROCEDIMIENTO PARA EL AJUSTE DE CORRIENTE DEL GOCT

NOTA DE APLICACIÓN


El GOCT cumple las funciones de un relé de sobrecarga y de un protector de voltaje. Una vez instalado el GOCT, ajuste la perilla de corriente
como tradicionalmente configura un térmico. Adicionalmente, el GOCT detecta pérdida de fase por corriente producto de malas conexiones
o fallas en alguno de los contactos del contactor, siempre y cuando esté ajustado correctamente.
El procedimiento de ajuste fino debe llevarse a cabo cuando el sistema esté operando en condiciones normales a plena carga.
1. Programar día y hora actual
2. Configurar cada evento
PROGRAMACIÓN DEL GTC-B1C
