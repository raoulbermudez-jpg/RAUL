---
title: "Departamento de I&D"
type: Technical
source: "11_Biblioteca_Tecnica_Nota-de-Aplicacion-Genius-Redes-Comunicacion.pdf"
product_code: "GENIUS"
product_line: "Genius"
date_processed: "2026-04-18"
---

# Departamento de I&D

Departamento de I&D
NOTA DE APLICACIÓN
COMUNICACIÓN REMOTA
PROTOCOLO MODBUS RTU


Realizado por
Revisado por
Autorizado por:
Fecha de Revisión
Milton Alfaro.
Liliam Ramírez.
Ana Méndez.
15/05/2015








NOTA DE
APLICACION

MONTAJE DE DOS O MÁS RELÉS
GENIUS EN UNA RED RS-485





• Introducción a las redes MODBUS RTU sobre RS485.
• Relés compatibles para montaje en red.
• Accesorios disponibles para montaje en red.
• Planificación de la red.
• Elementos necesarios para un montaje.
• Diagrama de conexiones.
• Programación de las direcciones MODBUS de los dispositivos.
• Integración del GIO TOOL en sistemas de red MODBUS.


















INTRODUCCIÓN A LAS REDES MODBUS RTU SOBRE RS485.

MODBUS es un protocolo de comunicación serial abierto enmarcado en el concepto de Bus de Campo de Control, su topología
está basada en una arquitectura maestro/esclavo o cliente/servidor con una estructura de Bus lineal en donde sólo existe un maestro,

Departamento de I&D
NOTA DE APLICACIÓN
COMUNICACIÓN REMOTA
PROTOCOLO MODBUS RTU


Realizado por
Revisado por
Autorizado por:
Fecha de Revisión
Milton Alfaro.
Liliam Ramírez.
Ana Méndez.
15/05/2015


el cual controla el acceso al medio y monitoriza el funcionamiento de la red, y uno o más dispositivos programables actúan como
esclavos, que responden y proceden según lo requerido por el maestro.


El protocolo interconecta los equipos de campo, como sensores, actuadores, controladores Lógicos Programables (PLCs), Motores
y otros tipos de dispositivos físicos de entrada/salida  para una comunicación efectiva, y es usado ampliamente en la
automatización de procesos industriales y fabricación de productos. Según el estándar Modbus y dada su implementación, en una
red Modbus habrá un maestro y hasta un máximo de 247 dispositivos esclavo. Esta limitación está determinada por el simple hecho
que en una trama Modbus la dirección del esclavo se representa con un solo Byte



Esclavo
2
Esclavo
1
Esclavo
3
Esclavo
5
Esclavo
7
Esclavo
4
Esclavo
6
Esclavo
247




Fig.1. Red MODBUS típica montada en una arquitectura de bus.


La comunicación se da en forma serial asíncrona bajo los estándares RS-232 o RS-845 para enlace semi-dúplex (half-duplex) yRS-
422 para enlace dúplex (full-duplex), utiliza diferentes medios físicos como son los de soporte metálico (cables), radio frecuencia
(RF), fibra óptica o infrarrojo (IR) y cuya velocidad de transmisión está prevista en valores discretos para el rango de 75 a 19.200
Baudios.


MODOS DE TRANSMISIÓN DEL MODBUS.

Los modos de transmisión definen como se envían los paquetes de datos entre maestros y esclavos, el protocolo MODBUS define
dos principales modos de transmisión:


MODBUS RTU (Remote Terminl Unit). La comunicación entre dispositivos se realiza por medio de datos binarios. Esta es la
opción más usada del protocolo y es la que se implemento en nuestras tarjetas.
MODBUS ASCII (American Standard Code for Information Interchange). La comunicación entre dispositivos se hace por medio
de caracteres ASCII.

Departamento de I&D
NOTA DE APLICACIÓN
COMUNICACIÓN REMOTA
PROTOCOLO MODBUS RTU

1 Para mayor referencia, consulte el documento MODBUS APPLICATION PROTOCOL  SPECIFICATION, disponible en www.modbus.org
2 Consulte la Especificación “MODBUS over serial line specification and implementation guide” de libre revisión en www.modbus.org

Realizado por
Revisado por
Autorizado por:
Fecha de Revisión
Milton Alfaro.
Liliam Ramírez.
Ana Méndez. .
15/05/2015


En una red MODBUS RTU puede haber hasta 247 esclavos, pero solamente un maestro. Toda comunicación inicia con el maestro
haciendo una solicitud a un esclavo, el cual responde al maestro lo que fue solicitado. En ambos mensajes (pregunta y respuesta),
la estructura utilizada es la misma: Dirección, Código de Función, Datos y CRC. Solamente el campo de datos tiene un tamaño
variable


Tabla Nº. 1.Estructura de los mensajes MODBUS.






El campo dirección es el primer byte de la trama  e indica el dispositivo al que va dirigido el mensaje. Cada dispositivo de la red
debe tener asignada una dirección única, diferente de cero. Igualmente, cuando un dispositivo responde a un mensaje, debe enviar
en primer lugar su dirección para que el maestro reconozca la procedencia del mensaje. El maestro también puede enviar un
mensaje destinado a la dirección 0 (cero), lo que significa que el mensaje es destinado a todos los esclavos de la red (“Broadcast”).
En este caso, ningún esclavo ira a responder al maestro.


En el campo Código de Función el maestro especifica el tipo de servicio o función solicitada al esclavo (lectura, escritura, etc.).
De acuerdo con el protocolo, cada función es utilizada para acceder un tipo específico de dato.


El campo Datos contiene la información necesaria para que los dispositivos puedan ejecutar las funciones solicitadas, o la
información enviada por los dispositivos al maestro como respuesta a una función.


El campo CRC es el último de la trama y permite al maestro y a los dispositivos detectar errores de transmisión.  Ocasionalmente,
debido a ruido eléctrico o a interferencias de otra naturaleza, se puede producir alguna modificación en el mensaje mientras se está
transmitiendo. El control de errores por medio de CRC asegura que los dispositivos receptores o el maestro no efectuaran acciones
incorrectas debido a una modificación accidental del mensaje. Si hay un error en el CRC, los esclavos no emitirán respuesta1.


La interconexión de los dispositivos MODBUS  en los ambientes industriales se hace con frecuencia en un bus  RS485
(oficialmente TIA/EIA–485-A), ya que éste puede operar en ambientes altamente ruidosos en una distancia de hasta 1200 metros.
El bus RS485 está diseñado para soportar hasta 32 terminales o esclavos, aunque con el uso de repetidores se puede soportar todos
los esclavos necesarios. El uso de un cable blindado ayuda a atenuar los ruidos eléctricos que pueden filtrarse entre los datos del
sistema diferencial que utiliza el estándar RS485.  Para distancias menores se ha aceptado el uso de un par de cables trenzados
comunes. De cualquier modo, debe tomarse en cuenta que debido a las frecuencias que intervienen en el cambio de datos y a las
distancias inciertas entre los terminales, se producen reflexiones indeseadas de la señal que se traducen en interferencia, por lo
cual se requiere el uso de una terminación con una impedancia características en los extremos del montaje2.

Dirección (1 byte)
Código de la Función (1 byte)
Datos (Variable: n bytes)
CRC (2 bytes)

Departamento de I&D
NOTA DE APLICACIÓN
COMUNICACIÓN REMOTA
PROTOCOLO MODBUS RTU

3 Se recomienda consultar los manuales y hojas de especificaciones de estos productos.

Realizado por
Revisado por
Autorizado por:
Fecha de Revisión
Milton Alfaro.
Liliam Ramírez.
Ana Méndez. .
15/05/2015



RELÉS GENIUS COMPATIBLES PARA MONTAJES EN REDES MODBUS RTU SOBRE RS485.

GI+
GII+
GOC-T


GUC-T
GSPT



GIII+
GSPT-MV

ACCESORIOS GENIUS NECESARIOS PARA MONTAJE EN RED  RS485.


GIO-PLUG-RJ453
GIO-A-RS485

Departamento de I&D
NOTA DE APLICACIÓN
COMUNICACIÓN REMOTA
PROTOCOLO MODBUS RTU


Realizado por
Revisado por
Autorizado por:
Fecha de Revisión
Milton Alfaro.
Liliam Ramírez.
Ana Méndez. .
15/05/2015



PLANIFICACIÓN DE LA RED.
El sistema GIO-LINK opera de acuerdo a una arquitectura del tipo Maestro/Esclavo, y sobre el protocolo industrial estándar
MODBUS-RTU. Las funciones MODBUS implementadas en los relés GENIUS son las siguientes:

Código 03: (Read Holding Registers) Lectura de bloques de memoria permanente.
Código 06: (Write Single Register). Escritura de un bloque de memoria permanente.
Código 08: (Diagnostics). Verificación de la comunicación serial.

Con el sistema GIO-A-485 es posible interconectar hasta 32 dispositivos esclavos sin usar repetidores y hasta 127 usando
repetidores. La velocidad de comunicación de los relés GENIUS es de 9600 baudios (bits/segundo). Todos los Relés Genius
vienen programados de fábrica con la Dirección MODBUS 01,  por lo cual será necesario asignar una dirección distinta a cada
relé.

ELEMENTOS NECESARIOS PARA EL MONTAJE DE UNA RED.
En la planificación de una red intervienen con frecuencia factores como el número de dispositivos que necesiten conectarse, las
distancias a alcanzar y las limitaciones establecidas en el montaje. Mientras más acentuados sean estos factores, hay más
consideraciones a tener en cuenta.

Si se planea construir una red con un número mayor a 32 relés, debe incorporarse un repetidor RS-485 por cada 32 relés
adicionales.

Mientras mayor sea la distancia, debe tenerse mayor consideración a las conexiones, los cables y las terminaciones. Incluso, para
distancias mayores a 1200 metros, podría incorporarse una pasarela intermedia a otra tecnología con mayor alcance.

Para el montaje de una red de varios dispositivos, será necesario desarrollar un bus de comunicación en RS485, el cual estará
conformado por los siguientes elementos:

1. GIO-PLUG-RJ45 por cada relé de protección Genius a conectar a la red.
2. Adaptador GIO-A-RS485K por cada relé de protección Genius a conectar en la red.
3. Fuente 12V (Provista por el usuario).
4. Convertidor RS485 a RS232, USB, ETHERNET u otro. Depende de puerto que vaya a utilizarse en el computador asignado al
maestro o al tipo de enlace que quiera implementarse  (Provisto por el usuario).
5. Un repetidor RS485 por cada 32 relés adicionales (Provisto por el usuario).
6. Cable de 4 hilos para configurar el bus



















DIAGRAMA DE CONEXIÓN DE LA RED.

Departamento de I&D
NOTA DE APLICACIÓN
COMUNICACIÓN REMOTA
PROTOCOLO MODBUS RTU


Realizado por
Revisado por
Autorizado por:
Fecha de Revisión
Milton Alfaro.
Liliam Ramírez.
Ana Méndez. .
15/05/2015




Fig.2. Diagrama de conexión para el sistema GIO-Link.

1. PE. Protective Earth.
2. GND (0V).
3. S- (B).
4. S+ (A).
5. 12V









CONFIGURACIÓN DE LAS DIRECCIONES DE LOS DISPOSITIVOS.
En los Relés Genius con interfaz digital (GI+, GII+, GUC-T, GSPT, GIII+ y GSPT-MV), la dirección ID MODBUS se puede
cambiar directamente en pantalla a través del menú principal de ajustes, en la opción ´DIRECCIÓN MODBUS´ (Consultar manual
de instalación respectivo). En el caso de los Relés Genius GOC-T, debe seguirse un procedimiento especial para poder cambiar la
dirección MODBUS, utilizando el programa ejecutable GIOIDCONFIG (proporcionado por Generación de Tecnología, C.A.).

Departamento de I&D
NOTA DE APLICACIÓN
COMUNICACIÓN REMOTA
PROTOCOLO MODBUS RTU


Realizado por
Revisado por
Autorizado por:
Fecha de Revisión
Milton Alfaro.
Liliam Ramírez.
Ana Méndez. .
15/05/2015




Fig.3. Programa Ejecutable para cambiar la dirección MODBUS en los Relés Genius.


PASOS PARA CAMBIAR LA DIRECCIÓN MODBUS CON GIOIDCONFIG.

Una vez construida la red e instalada la interfaz (RS485-USB ó RS485-RS232) al PC, abra el programa GIOIDCONFIG y siga las
instrucciones del mismo tal como se ilustra en los siguientes pasos:

Paso 1: Ubique el puerto COM en el que tiene conectada la interfaz a la red (Para determinarlo,  revise los puertos activos en el
Administrador de Dispositivos de las Propiedades del PC).


Fig.4. Cuadro de Dialogo para la revisión de los puertos activos en el Administrador de Dispositivos de
las Propiedades del PC.




Paso 2: Seleccione el puerto correspondiente y presione “Conectar”

Departamento de I&D
NOTA DE APLICACIÓN
COMUNICACIÓN REMOTA
PROTOCOLO MODBUS RTU


Realizado por
Revisado por
Autorizado por:
Fecha de Revisión
Milton Alfaro.
Liliam Ramírez.
Ana Méndez. .
15/05/2015



Fig.5. Cuadro Dialogo para la selección del Puerto correspondiente.


Paso 3: Una vez que el programa ha detectado el puerto COM, estará listo para buscar el relé. Conecte un solo relé Genius a la
red para identificarlo. Si hay más de un relé conectado, el programa identificará el primero.




Fig.6. Cuadro Dialogo para la detección automática del puerto seleccionado.







Paso 4: Si prefiere establecer un rango de búsqueda en lugar de esperar por el recorrido completo de todas las direcciones (1 a
127), desmarque la Opción “Rango Automático” y establezca el rango que prefiera. Si no conoce la dirección MODBUS que
tiene programada en el dispositivo, simplemente deje la opción marcada. Luego presione “Buscar”. Espere mientras se ejecuta
la búsqueda.

Departamento de I&D
NOTA DE APLICACIÓN
COMUNICACIÓN REMOTA
PROTOCOLO MODBUS RTU


Realizado por
Revisado por
Autorizado por:
Fecha de Revisión
Milton Alfaro.
Liliam Ramírez.
Ana Méndez. .
15/05/2015



Fig.7. Cuadro Dialogo para la configuración de la dirección del Genius.

Paso 5: Cuando el relé haya sido detectado,  puede cambiar la dirección MODBUS de acuerdo a la planificación que se tiene
para la red.


Fig.8. Cuadro Dialogo para la configuración del cambio de dirección de Genius.

Departamento de I&D
NOTA DE APLICACIÓN
COMUNICACIÓN REMOTA
PROTOCOLO MODBUS RTU

4 Consulte el Manual del Usuario de GIO TOOL
Realizado por
Revisado por
Autorizado por:
Fecha de Revisión
Milton Alfaro.
Liliam Ramírez.
Ana Méndez. .
15/05/2015



Paso 6: Una vez que la dirección deseada ha sido configurada en el relé Genius, el software ofrece la posibilidad de programar
otro relé. En este momento puede desconectar el que ya ha sido programado y conectar otro. También podría repetir la
búsqueda con el relé que acaba de programar para verificar que efectivamente está programado con la nueva dirección
MODBUS.



Fig.9. Cuadro Dialogo para la configuración de otro Relé Genius.

Cuando cada dispositivo tenga su nueva dirección configurada correctamente, la red estará lista para operar.  Se recomienda
colocar a cada equipo una etiqueta con la dirección MODBUS que quedó configurada.


INTEGRACIÓN DEL GIO TOOL EN SISTEMAS DE RED MODBUS.

1. Descargue el Software desde la dirección WEB http://www.genteca.com.ve/soportetécnico/biblioteca.p.aspx
2. Instale el Software GIOTOOL y siga las instrucciones que se proporcionan en el Manual del Usuario GIOTOOL4.
3. Si en vez de utilizar el software GIOTOOL,  se integraran los relés GENIUS a un sistema de software SCADA compatible
con MODBUS-RTU, debe solicitar a Generación de Tecnología, C.A. los Mapas MODBUS de los relés a integrar.
