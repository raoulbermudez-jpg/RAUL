# Trifasica U GIOTOOL

> **Fuente:** 04_Proteccion_Trifasica_U_GIOTOOL.pdf
> **OCR procesado:** 2026-04-18 | Motor: Tesseract v5.4.0 (eng)
> **Estado:** Texto extraído por OCR — puede contener imprecisiones en caracteres especiales

---

<!-- Page 1 -->
@ Generacion
(4) de Tecnologia (@Genius GIO-Tool
GIO-TOOL DESCRIPCION GENERAL

GIO-Tool es un software para supervision y manejo de informacién de los RELES DE PROTECCION Genius. El software GIO-Tool detecta
dispositivos, monitoriza en tiempo real los valores de las mediciones, las variables de estados y las alarmas, incluyendo acceso a las memorias
de historial eléctrico. Mediante este software se facilita la Monitorizacién y Generacién de reportes aprovechando las facilidades que representa
un Computador PC 0 compatible (equipo a ser provisto por el usuario)

ATENCION: Para utilizar adecuadamente este producto, ATENCION: Para poner en funcionamiento este software,
se requiere una instalacion eléctrica dotada con uno 0 més
RELES DE PROTECCION, debidamente conectados con
: ADAPTADORES de la familia GlO-Link. Ver Manual de
de los estindares RS485 y RS232. Instalacién de GlO-Link para mayor informacion

la persona que lo instale y lo use debe tener conocimientos
de comunicacién serial e integracién de equipos, en especifico

Los RELES DE PROTECCION Genius, son dispositivos que pueden enviar y recibir informacién por intermedio de un SISTEMA DE
COMUNICACION GIO-Link (exclusivo de Genius). El Sistema de Comunicacién es un conjunto compuesto por software, dispositivos y
accesorios, que permiten realizar transferencias a través de un Bus de datos, con destino hacia Terminales o Computadores PC compatibles.

Adaptadores
GIO-A-RS232

6
GIO-A-RS485,

GIOTOOL,

Figura | Caracteristicas generales del programa GIOTOOL y accesorios que componen las conexiones

El software GIO-Tool (version 1.0) provee varias funciones,
entre las cuales se destacan:

I. Deteccién automatica de Relés de Proteccién que se encuentran
conectados al Bus de Datos.

2. Monitorizacién en tiempo real, de las medicines, estados, alarmas y
configuracién de cada Relé de Proteccién

3. Extraccién y almacenamiento de eventos histéricos, memorizados en
cada Relé de Proteccién.

4. Despliegue de Pantallas para visualizacién de parametros y configuraciones.

5. Despliegue de Pantallas para visualizacién de histéricos de alarmas.

6. Generacién de Reportes de datos, en Pantalla e impresos.

7. Generacién de Graficos y Reportes de Tendencias.

8. Almacenamiento de listas de configuracién de pardmetros, de cada
Relé de Proteccién.

9. Impresién de reportes.

10. Comunicacién por MODBUS o MODBUS/TCP.

@ Genius


<!-- Page 2 -->
(2) COMPATIBILIDAD CON EQUIPOS Y DISPOSITIVOS

2.1 Requerimientos minimos del equipo para
instalar el software

Las siguientes caracteristicas son las minimas requeridas para utilizar el software
GIO-Tool, en cualquier Computador PC tipo “Desktop” o “Laptop”.

Computador PC compatible. (no disponible

para equipos con sistema operativo MAC).

Windows 2000, Windows XP.
Memoria RAM 512 MB minimo; Recomendado, 1GB

Espacio en Disco Duro | 200 MB
| x COM RS-232 ; | x USB

Convertidor RS-485/RS-232 (dependiendo del estandar

que se elija con los Adaptadores GIO-LINK)
2.2 Capacidades y funciones disponibles en la actual
version de software GIO-Tool

Version actual del software GIO-Tool: 1.0

a) Dispositivos compatibles con esta version:

Las siguientes familias de RELES DE PROTECCION de la marca Genius ,
son compatibles con el software Gio-Too!

atel foci)

Ts GOE =: Spr i GUCT

(Futuras versiones del software GIO-Tool seran previstas para soportar
mas funciones avanzadas, y otras familias de RELES DE PROTECCION).
Para una lista completa de los Dispositivos y Funciones soportados,
remitase a la seccién Especificaciones Técnicas, al final de este documento.

Gill

a

b) Funciones disponibles con esta versién:
Lectura de Variables
(@& Corrientes
© Voltajes
(& Potencias
(& Temperatura
© Parametros de Configuracion

oe & Alarmas
Funciones disponibles < (a Deteccién automatica
en esta version © Deteccién miltiple

& Indicacion del estado de la conexion
& Graficos de Tendencias

[& Reportes

i Impresién

@f Muestras en tiempo real

i Diagrama de la red

i Tablas de Historicos
(Compatible con bus MODBUS
(Compatible con MODBUS/TCP

Escritura de Variables

En versiones futuras
<S_% Guardado de memoria

(no disponible actualmente)

@ Genius

(3 } ADAPTADORES DE COMUNICACION QUE SON
COMPATIBLES CON GIO-Tool

El software Gio-Tool detecta los RELES DE PROTECCION conectados a un
Bus de Comunicacion,a través de varios estandares alternativos de comunicacion.

Los siguientes son los accesorios del sistema GlO-Link, con los cuales se
pueden realizar adaptaciones y conexiones, entre Relevadores y Computadoras:

S5@oQ!

CONECTOR GONECTOR ADAPTADOR ADAPTADOR
GIO-PLUG-RJII_GIO-PLUG-USB GIO-A-RS48S GIO-A-RS232

Sistema GIO-Link en base al estandar RS-232

Con esta alternativa, el Software puede manejar un (1) solo
RELE DE PROTECCION

Se requiere un Terminal o Computador con Puerto serial COM RS-232,
acoplado con los siguientes accesorios:

Adaptador, modelo GIO-A-RS232_ (Una pieza)
Conector, modelo GIO-PLUG-RJ45._ (Una pieza)

Sistema GIO-Link en base al estandar RS-485

Con esta alternativa, el Software puede manejar varios RELES DE PROTECCION
Se requiere un Terminal 0 Computador con Puerto serial
tipo COM RS-232, acoplado con los siguientes accesorios:

Utilizacién de Adaptadores, uno por cada Relevador

de Proteccién

Con esta opcién, a cada Relés de Proteccién se le asigna un Adaptador.
Se requiere un Terminal o Computador con Puerto serial COM RS-232,
acoplado con los siguientes accesorios:

Conector, modelo GIO-PLUG-RJ45
Adaptador, modelo GIO-A-RS485
Convertidor RS-232/RS-485 (Nota |)

(uno para cada Relé)
(uno para cada Relé)
(uno por Computador)

Sistema GIO-Link en base a USB

Con esta alternativa, el Software puede manejar de uno a varios
RELES DE PROTECCION (un RELE por cada puerto USB que sea
conectado).

Se requiere un Terminal o Computador con Puerto Serial Universal
USB, acoplado el siguiente accesorio:

Conector y Adaptador modelo GIO-PLUG-USB

Nota |:Terminales o Computadores y Convertidores tipo RS-232/RS-485
son equipos y partes a ser provistas por el usuario.

[ZOWAECES OD)


<!-- Page 3 -->
(4) PANTALLA PRINCIPAL DEL SOFTWARE GIO-Tool

4.2 Aspecto General del Software GIO-Tool

een

a . ~ + GieSTOOL

Figura 2 Elementos destacados de la interfaz del Usuario, en el software GIO-Tool

Elementos destacados en la Pantalla Principal:

Meni

Barra de Herramientas Generales.
Barra de Herramientas de Conexién. (6
Barra de Estado de la Conexién.
Cuadro de Informacién del (!
Dispositivo Detectado.

Cuadro de Informacién del Dispositivo
Seleccionado.

Lista de Dispositivos.

Mapa de la Red de los Dispositivos.
Opciones del Area de Trabajo.
Area reservada para versiones futuras.

m(olayal>

Deteccién automatica de Relés conectados al Bus de Comunicacién.

El software GIO-Tool detecta los RELES DE PROTECCION conectados al
Bus de Comunicacién acoplado al Computador.a través de varios estindares
alternativos de comunicacién.

El software inicia las operaciones con la deteccién automatica de los Relés
que se encuentren conectados al Bus de Comunicacién.

Inicialmente, el software GIO-Tool detecta el conjunto (que puede
ser de un solo elemento), de RELES DE PROTECCION presentes en
el Bus de Comunicacién.

Las identificaciones de los dispositivos que son detectados quedan
registradas en un archivo de lista, siendo este archivo almacenado en
el Disco Duro del Computador. La siguiente vez que se requiera
trabajar con un determinado grupo de dispositivos, el usuario puede
volver a seleccionar una nueva deteccién o simplemente abrir un
archivo con una lista de dispositivos que haya sido anteriormente
almacenada en la Computadora.

Una vez que se carga una lista (ya sea por una orden de deteccién o
por acceso desde un archivo) se puede trabajar con cualquiera de los
dispositivos, que aparecen listados en el cuadro “Lista De Dispositivos”.

Para comenzar a trabajar con un Relé de Proteccién, sélo hay que
hacer “clic” sobre el identificador de dicho Relé, presentado en esa
lista. Si la lista posee un solo renglon, este se selecciona y abre
automaticamente.

@ Genius

4.3 Médulo ASISTENTE

Para hacer més facil la deteccién de los dispositivos, el usuario cuenta con un
““Asistente”, que se despliega al iniciar el programa y puede ser llamado en cualquier
momento desde el ment “Herramientas”,“Asistente”.

a) Ejecute el Inicio del programa, y espere hasta que se abra una ventana con titulo
de'“Asistente”. Observe el aspecto ilustrado en la Figura 3.

Seleccione una de las siguientes opciones:

I Detectar uno 0 mas Dispositivos conectados al computador (no se requiere
conocer las direcciones logicas previamente asignadas a cada dispositivo presente).

 Abrir una lista de dispositivos existentes, desde un archivo creado durante una
deteccion anterior.

Detectar uno o més
Dispositivos conectados al
computador

Abriruna lista de
disposiivos existente

Figura 3 Primera ventana del asistente

b) Espere que aparezca una ventana con subtitulo “Seleccién del Puerto de
Comunicacién”. Si va a utilizar comunicacién MODBUS, Indique el numero
del puerto COM, con el que desee conectarse a los dispositivos (ver Figura
4). Si posteriormente requiere cambiar el numero del puerto COM, puede
hacerlo a través de la “barra de herramientas de conexién” (descrita mas
adelante, ver Figura 8). Si va a utilizar comunicacién MODBUS/TCP haga clic
en la casilla"MODBUSTCPIIP” y complete las casillas de direccion IP y Puerto
de Comunicacién.

‘Selecci6n del Puerto de Comunicacién |
P Utes TCPAP

Por favor, seleccione el numero de puerto que |
se yaa utiizar:

Seleccién del Puerto de Comunicaci6n,

Por favor, seleccione la direccién de IP que se
va a.utiizar y el puerto de comunicacién

Deir, fis fee. fe. fos

AB. | | aa

Figura 4 — Seleccion del puerto COM desde el

asistente y parametros MODBUS/TCP

zs


<!-- Page 4 -->
€) Si inicialmente seleccioné la opcién “Detectar uno © mas Dispositivos”,
haga una prueba de la conexién (ver Figura 5). Compruebe que el numero
del puerto COM seleccionado es el adecuado, en caso contrario puede pulsar
dentro de la ventana el botén “Anterior” para regresar al paso anterior, y
seleccionar otro. Al concluir la comprobacién del puerto seleccionado, avance
hacia la siguiente ventana del programa, pulsando el botén “Siguiente”.

Prueba de Conexién

an digo cn oa Se
Argue senda r
eee
SBRECAA Seto gh pele cone
SESODNECTAN yevestanee tlpoto ole
Seen lao Sonsgapenscts x
Sacapmorpasesaice ‘

newcnefs —3]
8) a) _d. |

Prueba de Conexion

La Comunicacién se
establecio
correctamente.
Puede oprimir
SIGUIENTE

ja) 4) Be

=)

Figura 5 Conexion del dispositivo

en el asistente

d) Observe cuando aparezca una ventana con titulo de “Detectar Dispositivos” (ver
Figura 6). Para la deteccién automatica, introduzca el rango de direcciones Modbus
que seran examinadas durante la biisqueda de dispositivos. Usualmente se consideran
numeraciones bajas (comenzando por la direccién Modbus N° |).El rango de direcciones
permitidas esta delimitado desde 1 hasta 127. La direccin 0 0 direcciones mayores a
127 no son validas. Todos los dispositivos de las marca GENIUS salen de fabrica con

la direccién predeterminada “1”.

= Detectar Dispositivos

Deteccién de Dispositivos
femme
Dieesin Fat

—
oo

—

Ui

© (ipa Sepoaives decide alata actual
v — xX
cept Conca

Figura 6

Ventana de Deteccién
de Dispositivos

@ Genius

4.4 Barra de herramientas

Observe la Pantalla principal en la seccion de Barras de Herramientas, alli
encontrara dos principales caracteristicas:

™@ Barra de Herramientas Generales

@ Barra de Herramientas de Conexion

Descripcién de cada botén de la Barra de Herramientas Generales:

®®O O88 ©0600

Figura 7 Barra de herramientas con Comandos Generales

icono

‘Ho

Funcion

Abre una lista de dispositivos previamente detectados.

Botén “Guardar”. Guarda los cambios de la lista actual.
Botén “Guardar Como”. Guarda la lista actual con un nuevo
nombre que se especifique.

Deteccién de dispositivos.Abre el asistente de deteccion
automatica de dispositivos.

Abre la pestafia de pardmetros de configuracién del
dispositivo en linea.

(Botén reservado para uso en futuras versiones del software).

(Botén reservado para uso en futuras versiones del software).

Generacién de reportes. Permite elaborar un reporte de las caracteristicas
de cada Dispositivo, o generar un reporte tipo tabla (Excel) con tablas de
cconfiguracion e informacion historica e imprimirlos.

oO Abre la ventana para la configuracion de preferencias del usuario.
ss @


<!-- Page 5 -->
4.5 Barra de herramientas

Descripcién de cada botén de la Barra de Herramientas
de Conexién:

Figura 8 Barra de herramientas de conexion

icono

Puerto COM: [3

Funcién

Cambia el puerto de comunicacién.Abre el asistente
para efectuar los cambios. Para el modo MODBUS/TCP
permite cambiar la direccién de IP y el puerto,

Boton “Conectar”. Inicia la conexién de comunicacion.

Botén “Desconectar”. Termina la conexién con el
dispositivo actual.

Descripcién del uso de la Barra de Estado de Conexién:

Observe al lado derecho de la Barra de Herramientas de conexidn. La Barra de estado
contiene cuatro partes:

® Un icono que muestra el estado de conexi6n y desconexién (ver Figura 9).

@® Un mensaje de estado de conexién.

© Un mensaje de estado. Si no hay problemas muestra el mensaje “OK”. Si existe
algun problema con la comunicacién se muestra el mensaje de error respectivo.

© Una lista de mensajes de estado de comunicacion

Conectadgs
“2

fra/08/2008 10.30 Reconexion
13/08/2008 10:30 Se abrié el puerto.

El dispositivo se encuentra Desconectado

Figura 9 Barra de estado de conexién

@ Genius

4.6 Cuadros de Informacién

La pantalla principal del software GIO-Tool contiene dos Cuadros de Informacién, que
muestran los datos relevantes del dispositivo seleccionado y detectado:

Figura lO Cuadros de informacion

A) Cuadro de Informacién del Dispositivo Detectado.
B) Cuadro de Informacién del Dispositivo Seleccionado.

CUADRO DE INFORMACION DEL DISPOSITIVO DETECTADO

Este cuadro muestra informacién del dispositivo detectado, segiin una direccién
MODBUS indicada (0 direccién de IP si se trabaja con MODBUS/TCP).

La siguiente informacién se verifica y actualiza cada segundo:

Tipo: Gil
Vottsje: 480 V
Corriente 100 A
Versién: 2,25

Figura Il

Cuadro de Informacion del
dispositivo detectado

familia de dispositivo presente en la direccisn MODBUS
especificada.

valor de voltaje nominal, segiin modelo.

rango de corriente nominal, segiin modelo.

versién del firmware del dispositivo.

Voltaje:
Corriente:
Version:

CUADRO DE INFORMACION DEL DISPOSITIVO
SELECCIONADO

Este cuadro muestra informacién creada por el usuario y no depende del contenido
del dispositivo conectado fisicamente, Este Cuadro de Informacién se actualiza solo
si el usuario cambia de dispositivo, o el usuario modifica a informacion directamente.

La siguiente informacién es mostrada en este cuadro:

Nombre:
Genius Ill+ 2.25

Descripcion:
Genius i+, v2.25, 480, 1004

Dit MB: Re

Cuadro de Informacion del
dispositivo seleccionado

Figura l2

Nombre: rétulo que identifica al dispositive dentro de una lista.
Descripcién: describe al dispositivo seleccionado
Dir MB: indica la direccisn MODBUS del dispositivo seleccionado

I-S] 0}


<!-- Page 6 -->
La informacién en este cuadro es editable, el usuario puede modificar los valores
correspondiente en la lista de dispositivos. El usuario puede personalizar el nombre
de cada dispositivo y su descripcion. Para que los cambios tengan efecto el usuario
debe guardar la lista (menéi“Archivo”, opcién “Guardar” o pulsar el botén “Guardar’).

Este cuadro también permite cambiar la direccién MODBUS que se esta explorando.
Al cambiar en este cuadro la direccién MODBUS, se modifica también la direccion
indicada en la lista de dispositivos, para el dispositivo actualmente seleccionado.

ATENCION: la direccién MODBUS mostrada en este cuadro, es la direccién que se
configuré en la lista de dispositivos, a cual se utilizara para buscar al dispositivo en la
red MODBUS. $i el usuario modifica este parametro, no alteraré la direccién MODBUS
registrada en la memoria del dispositive conectado.

Informacién sobre conexién de un modelo equivocado

Cuando se selecciona un dispositivo de la lista pero se conecta otro de tipo diferente,
el programa GlO-Tool muestra un mensaje de error y cambia el aspecto del cuadro
de informacién del Dispositivo Seleccionado, para contrastarlo con el cuadro de
informacién del Dispositivo Detectado, Un ejemplo de error se muestra en la siguiente
ilustracién, en donde el Equipo Detectado es un tipo “Genius Ill” mientras que el
Equipo Seleccionado es un tipo Genius Il, en la misma direccién MODBUS.

Figura 13 _ Indicacién de error por deteccién de Tipo diferente al seleccionado

(5 AREA DE TRABAJO DEL SOFTWARE GIOTOOL

El usuario dispone de un area de trabajo con cuatro opciones a las que puede acceder
por pestafias (ver Figura 14).

Figura 14

Pestafias de las opciones del area de trabajo

Opcién PRINCIPAL:
Opcién EQUIPO EN LINEA: Visualiza los parémetros en linea del dispositive

Selecciona el dispositive de trabajo.

seleccionado.
Opcién REPORTES:
Opcién GRAFICOS:

Genera reportes de los datos en linea.
Genera graficos de tendencias de las variables
monitorizadas y genera reportes de datos

@ Genius

Es la seleccion por defecto cuando inicia el software GIO-Tool.
Esta area de trabajo muestra la LISTA DE DISPOSITIVOS, y el MAPA DEL BUS DE
COMUNICACION con los dispositivos configurados.

LISTA DE DISPOSITIVOS

Este elemento permite seleccionar el dispositivo de trabajo haciendo “clic”
sobre el nombre correspondiente.

Si la lista posee varios elementos, antes de seleccionar uno en particular, no
se establece la conexién con ningun otro dispositivo. Sélo un elemento
permanece cargado en la memoria para trabajo y conexién a la vez. Para
cambiar de elemento hay que seleccionar otro de la lista de dispositivos
detectados.

Si la lista posee un solo elemento, éste se carga automaticamente al abrir el
archivo o hacer la deteccion.

La lista contiene lo siguiente:

Nombre: El nombre del dispositivo

Tipo: El tipo segtin modelo

Dir MB: La direccisn MODBUS del dispositivo
Comentario: Informacién referente al dispositivo

Estos parametros, excepto el Tipo de dispositivo, se pueden editar en El
Cuadro De Informacién Del Dispositivo Seleccionado, con lo que se puede
personalizar la informacién.

El valor de la direccién MODBUS mostrado en la lista de dispositivos se puede
modificar para el elemento actualmente seleccionado, cambiando el valor en
la casilla “Dir MB” del Cuadro Del Dispositivo Seleccionado.
Para cambiar el nombre y el comentario del dispositive, se debe modificar el

cuadro de edicién de texto del cuadro Dispositivo Seleccionado.

Figura 15 Lista de dispositivos

1O-Tool MV-O7-O117.0-01-S B!|0


<!-- Page 7 -->
MAPA DEL BUS DE COMUNICACION

Este diagrama se presenta en base a los dispositivos configurados. Por cada
dispositivo se muestran los siguientes datos:

 Direccién MODBUS
m Nombre y tipo de dispositivo.

Estos datos son idénticos a los de la lista de dispositivos.

Mapa del Bus de Comunicacion

Figura 16

5.2 Opcién EQUIPO EN LINEA

Esta opcién del area de trabajo contiene los parametros de Mediciones y
Configuraciones del dispositive.
El 4rea de EQUIPO EN LINEA posee a su vez varias opciones secundarias,
en diferentes pestafias. Las opciones y variables mostradas dependen del tipo
de dispositivo (Gl, Gll, Glll, GOC, etc.). La informacién que se presenta es
actualizada cada dos segundos.

Aunque los grupos bajo la opcin EQUIPO EN LINEA pueden variar; hay tres
pestafias que siempre se encuentran presentes, para cualquier tipo de
dispositivos:

@ Grupo IDENTIFICACION: muestra las caracteristicas mas relevantes del
modelo y la direccién MODBUS utilizada.
'@ Grupo MONITOREO: permite ver las variables eléctricas.

1 Grupo CONFIGURACION: permite ver los pardmetros de operacién del

dispositivo.

PESTANA DE IDENTIFICACION (ver Figura 17)
Esta area presenta la informacion de identificacién y caracteristicas generales

del dispositivo, tales como:

=D: Muestra un rétulo que identifica el tipo de dispositive
(GI, Gll, Gill, GOC, etc).

1 ModeloVoltaje: Indica el voltaje nominal del dispositivo.
™ Modelo.Corriente: Indica el rango de corriente nominal del dispositivo,
siaplica.

@ Modelo Idioma: Indica el idioma del dispositivo.

@ Modelo RTC: Indica si el dispositivo maneja medicion de
temperatura RTC, o sin RTC.
@ Version: Muestra la version del “firmware” del dispositivo.

®@ Direccion.Modbus:

@ Genius

Muestra la direcci6n del dispositivo en la red Modbus.

GRUPO DE MONITOREO (ver Figura 18)

Esta drea contiene las variables eléctricas y estados que maneja el tipo de
dispositivo. Las alarmas se muestran como un indicador tipo LED: apagado
indica ausencia de alarma y encendido presencia de la alarma.

 Mediciones de voltajes.

Ml Mediciones de corrientes.

Ml Medicién de frecuencia de la linea.

Variables de estado del motor y alarmas. Las variables particulares
dependen del tipo de dispositivo particular.

GRUPO CONFIGURACION (ver Figura 19)

Esta area permite visualizar los pardmetros que han sido configurados en cada
dispositivo.

(la posibilidad de efectuar cambios de parametros esta reservada para futuras
versiones del software GIO-Tool.)

Muestra los niveles de voltaje y corriente que se consideran como sobrecargas
© fuera de rango; los tiempos de conexién y desconexién, datos del motor,
modos de operacién, hora y fecha.

GRUPO HISTORICO
Muestra la tabla del historico de fallas del dispositivo.

Pestaiia de Identificacion

Pestafia de Configuracién

O7.0-O1-S 10}


<!-- Page 8 -->
© GENERACION DE REPORTES

El software GIO-Tool permite generar un reporte completo de las
variables y configuraciones actualmente presentes en cada dispositivo
conectado. El reporte esta conformado por la captura de los datos,
en el momento en que se genera, cubriendo dos aspectos:

Informe de Variables y Configuraciones.
Informe de Tablas e Histéricos

Para acceder a esta opcién, ubique la Pantalla Principal, luego oprima
el botén de Informes (Figura 20) 0 accédalo desde el meni, pulsando
el meni “Dispositivo” seguido luego de la opcién “Reportes”

Figura 20 Boton de informes

Al oprimir esta opcién, se visualiza la carpeta de didlogo de Informes (Figura 21).
Para generar reportes deben estar presentes las siguientes condiciones:

 Debe haber un dispositivo conectado fisicamente, y el programa
debe estar en estado CONECTADO.
 Debe haber un dispositivo seleccionado de la lista de dispositivos.

Una vez generado el reporte, el usuario puede abrirlo e imprimirlo en
cualquier momento. El archivo de reportes es un archivo separado por
comas (formato CSV) que puede manejar con cualquier procesador de hojas
de calculo (como Excel), o imprimirse desde el software GIO-Tool si asi lo
desea, Se recomienda esta Ultima opcién, para lo cual solamente se requiere
hacer “clic” sobre el botén “imprimir reporte” de la opcién “Reportes” del
area de trabajo.

Ventana de Dialogo de elaboracién de reportes

@ Genius

La informacién generada sobre las variables y tablas queda disponible en
dos archivos auxiliares, separados si asi se requiere. Estos archivos tienen
extensiones .dat.txt y .dat.csv.

Nota: Para importar los datos desde otras aplicaciones del usuario, (por
ejemplo a EXCEL), el usuario deberd seleccionar la primera columna, y luego
en el ment “Datos” de EXCEL, seleccionar “Texto en Columnas”, para
separar los datos.

= Reporte:

Seleccione el nombre del
archivo de trabajo.

Uilice esta opcién para cambiar el nombre del archivo del reports,
crear un nombre nuevo o poraiizer un archive de report ya
existent para reescribio  imprimio,

© Note: siiizaun archivo existente se perderd si velve a generar el
informe (2 sobreescribirs)

Archivo de repore:
Freporte_20070818_1648.cev.

Figura 22 Cuadro de didlogo para abrir y guardar reportes.

(7) PREFERENCIAS

La opcién de preferencias se activa utilizando el botén de la barra de
herramientas general (Figura 23) o a través de la opcién de menu:
“Herramientas”, seguido luego de “Preferencias”.

Esta opcién permite personalizar algunas opciones de visualizacién y guardarlas
en un archivo de configuracién. Si lo desea, puede hacer que la configuracién
sea la que se establezca por defecto para utilizarse automaticamente la proxima
vez que abra el programa haciendo uso del boton “Guardar Como Preferido”,
(Figura 24).

Boton de Preferencias

Figura 23

0-O1-S] ®


<!-- Page 9 -->
Preferencias del Usuario

Tan de Fite fo lens
= oo

6 Apa prnbpot create

ae

Figura 24 Cuadro de dialogos de Preferencias

GENERACION DE GRAFICOS DE TENDENCIAS

El software GIO-Tool dispone de una funcién que permite graficar
las variables eléctricas y estados que cada dispositivo, segiin lo indicado
en GRUPO MONITOREO (ver seccién 5.2).

Cada vez que un dispositivo se encuentra seleccionado y conectado,
las variables del GRUPO MONITOREO son registradas y
almacenadas. La pestaiia GRAFICOS permite visualizarlas y generar
una exportacién de los datos en formato de texto, separado por

comas, compatible con Microsoft EXCEL.

Figura 25 Pantalla de graficos de tendencias.

8.1 Pantalla de graficos de tendencias.

La pantalla de gréficos de tendencias contiene tres zonas:

m Area del grafico.
i Lista de variables y rangos.
m Area de Herramientas.

@ Genius

El Area de grafico dispone de tres escalas para mostrar las variables.
Cada variable se representa con un color diferente y en la zona
inferior del grafico se muestra la leyenda. Debajo de cada eje vertical
se presenta un conjunto de cuadros de colores, que corresponden
con los de las variables, indicando con cual escala se est4 representando
cada una de elas.

La Lista de variables y rangos permite seleccionar las variables a
mostrar en el grafico, marcando la casilla de verificacién de cada una.
Adicionalmente, una casilla de edicién de texto indica cual de las tres
escalas esté utilizando la variable; esta casilla es editable y se puede
ingresar un numero en el rango de 1a 3. Los rangos de las escalas se
editan en los cuadros de edicién de texto que se encuentran sobre
la lista de variables.

El Area de Herramientas presenta un conjunto de botones para ajustar
las opciones de visualizacién del grafico. Se proporcionan dos juegos
de cuadros de edicién, para asignar las fechas de inicio y final, mostrables
en el eje horizontal (dia, mes, afio, hora y minuto). Si se desea, se
puede ajustar este rango automaticamente, seleccionando el rango
deseado de tiempo en la lista de seleccién de rango, con las siguientes

opciones:

@ Cinco minutos, quince minutos, treinta minutos.
m Una hora, dos horas, cuatro horas, ocho horas, doce horas.

m Un dia, dos dias, tres dias, una semana, quince dias, un mes

Cuando se utiliza la lista de rangos de tiempo, el rango se ajusta

automaticamente para que coincida en fecha de finalizacién con la fecha
indicada en las casillas de fecha final, modificandose la fecha de inicio. Si
se quiere ajustar la fecha de finalizacién asi como la hora actual, se puede

oprimir el botén de Fecha Actual que posee un icono de reloj.

Ke

Refrescar

|

Exportar

Inicio/Final:

415 minutos >| > 8B Ks
fat +|5 x |2008 >| 15 vjj/35 wv
fat +|5 x |2008 | 15 y|[50 >|

Figura 26 Barra de herramientas de graficos de tendencias.


<!-- Page 10 -->
Botén

Nombre

Funcion

Muestra el grafico con lineas que unen

(9) GIO-Tool ESPECIFICACIONES TECNICAS

El Botén Refrescar permite actualizar el grafico una vez que se han hecho
cambios en las configuraciones. E| Botén Exportar permite guardar los datos
mostrados en la grafica actual en un archivo de texto separado por comas.

Se dispone de dos Botones que modifican la visualizacién, con esto se puede
mostrar el grafico con lineas, puntos en equis, o ambos:

Existen dos Modos de enfoque especial, mutuamente
excluyentes: modo lupa y modo cursor. El primero

permite hacer acercamientos en cualquier zona del

grafico y el segundo permite sefialar un punto del
tiempo en el grafico y conocer los valores de las

variables en dicho punto.

@ Genius

documento)

Grafco de Liness 344 punto, A Identificacién del software
Grafico de Puntos Muestra el grifico colocando una equis a. Nombre GIO-Tool
en cada punto. a2 Archivo giotool.exe
Entra en modo de Lupa. Permite hacer a3 Version 1.0
IP
Lupa acercamientos con el raton,
seleccionando el area de interés. Los
acercamientos son apilables y se sale |
de ellos con un clic en boton derecho B — Requerimientos del Equipo Terminal o Computador
del ratén. Cada vez que se efectiia un
aumento se muestra un icono adicional - ; j sponil
de lupa en el borde superior del grafico. b.1 | Equipo PC Compatible. (no disponible para
equipos con sistema operativo MAC)
Cursor Entra en modo de Cursor. Este modo - - - '
deshabilita el modo de Lupa. Permite b.2 | Sistema Operativo | Windows 2000 / Windows XP.
mostrar el valor de las variables en el -
punto del tiempo que sefiale el usuario. b.3 | Memoria RAM 512 MB minimo.
con el apuntador del raton. b.4.| Disco Duro 200 MB
Hora Actual Actualiza la hora actual en el final de! b.5 | Puerto de COM RS-232
rango de tiempo. Comunicacién USB con asignacién de
. Refresca el grafico para que tome los puerto COM emulado.
Actualizar Rango
cambios en el rango de tiempo. Debe 7
coprimirse
luego de hacer un cambio en las fechas |
‘© rango de tiempo. C_ Especificaciones de Comunicacion
Refrescar Efectiia un refrescamiento automatic c.l | Velocidad de transmisién 9600 bps
‘atoms del grafico alrededor de cada diez - -
wuromaticamente segundos. El valor final del rango de c.2 Paridad Ninguna
tiempo se actualiza y las curvas “se
desplazan” hacia el lado izquierdo del c.3_ Bits 8
grafico para dar cabida a nuevos datos. 4 Bit de parada |
Abre la ventana de exportacién de L i
Ext atencia para
Portar datos de tendencias. Los datos ch P . 10
exportados corresponderan al rango Request to Send
mostrado en el grafico en el momento oe
de oprimir este botén. <b Tiempo para deteccién de 999s
falla de comunicacién
w Refrescar Refresca el grafico ante cualquier ——
Reeser ‘cambio en el rango 0 en la configuracion ¢.7 | Protocolo de comunicacion Modbus - RTU
—S del grafico. - :
or Branco. Sistema GIO-Link en
Maximizar Maximiza el area del grafico ocultando Adaptadores para comunicacion base al estandar RS-
la cabecera del programa. c.8 | (Vea la seccion 3 de este

232

Sistema GIO-Link en
base al estandar RS-
485

Sistema GIO-Link en
base al estandar USB
(Para mayor informacion,
vea el MANUAL DE
INSTALACION GIO-Link
(Version para

conectores y adaptadores)

= @


