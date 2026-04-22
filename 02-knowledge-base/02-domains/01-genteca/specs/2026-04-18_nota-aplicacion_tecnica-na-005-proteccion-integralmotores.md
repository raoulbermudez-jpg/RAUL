---
title: "www.genteca.com.ve"
type: Technical
source: "11_Biblioteca_Tecnica_NA-005-Proteccion-IntegralMotores.pdf"
product_line: "Genteca"
date_processed: "2026-04-18"
---

# www.genteca.com.ve

www.genteca.com.ve
excelinevzla
NOTA DE APLICACIÓN
NA 2021-V1-005
Protección integral de motores
Al momento de instalar un motor trifásico es importante identiﬁcar como resguardarlo de
las fallas de voltaje que son cada vez más frecuentes y críticas en la red eléctrica y ante las
fallas mecánicas como una sobrecarga o un rotor trancado. Cualquiera de estas fallas
reduce la vida útil del motor, además de los efectos indirectos del daño en el equipo como:
paradas en la producción por tiempo de reparación y los costos de reparar o sustituir el
motor y posiblemente algunas partes adicionales. En estos casos nuestra recomendación es
incluir en su tablero de protección nuestro relé integral de protección GOCT, el
cual impide la conexión del motor en condiciones de riesgo por fallas de voltaje en la red y
garantiza una desconexión apropiada ante fallas mecánicas como sobrecargas y rotor
trancado. Asimismo, si ocurren tres fallas de corriente en menos de treinta minutos se
producirá la desconexión permanente del motor requiriendo el arranque manual del
protector, por ende, la asistencia de personal técnico al área del equipo.
A continuación, se presentan los esquemas de conexión que incluyen el relé integral de
protección GOCT para las fallas de voltaje y corriente, en conjunto con los módulos
supresores de picos de alta energía, los cuales direccionaran hacia el sistema de puesta a
tierra las descargas atmosféricas y/o las sobretensiones originadas por interconexión de
líneas eléctricas.

Solución Ideal para motores trifásicos de:
•  Ventilación forzada y extracción.
•  Compresores de aire
•  Máquinas y herramientas
•  Grúas eléctricas
Esquemas de conexión
En los relés de protección trifásica integral los cables que activan el motor pasan a través de
este para supervisar el consumo de corriente, la práctica común es colocar el relé entre la
salida del breaker y el contactor, agregando tres cables de menor calibre para el monitoreo
del voltaje (que se pueden tomar o del breaker o del contactor), cuidando mantener el
orden de conexión del motor para evaluar que la secuencia sea correcta. La activación del
contactor se realiza utilizando la salida de relé normalmente abierta (97-98), la cual cerrara
cuando las condiciones de voltaje sean apropiadas y se abrirá cuando el voltaje o la corriente
pongan en riesgo el motor. Asimismo, cuenta con una salida de relé normalmente cerrada
que permite colocar indicadores de alarma en el tablero (95-96).
01

En la solución que presentamos a continuación incorporamos nuestro relé de protección
integral, tres de nuestros módulos supresores de picos de alta energía (GMP-5-35XX
conectados entre cada una de las fases y tierra, el contactor, la protección de corto circuito
para el motor y un indicador luminosa de que el equipo esta desconectado.
www.genteca.com.ve
excelinevzla
NOTA DE APLICACIÓN
NA 2021-V1-005
02
Tripped: 95 - 96 closed

.97 - 98 open
Normal: 95 - 96 open

.97 - 98 closed
GOCT
Use GIO PLUG (Optional) for serial
communication with other devices
Power Supply
wires must pass
through GOCT
holes before
connectiong
to 3Ø Motor
(Before line starter circuits)
V2
(From line
starter circuits)
Figura 1. Diagrama de conexiones del producto.
Figura 2. Esquema de conexiones para la protección de un motor
F1
F2
F3
TIERRA
CONTACTOR
SUPRESORES
DE PICOS
PROTECCION CONTRA
CORTOCIRCUITOS
RELE DE
PROTECCION
INTEGRAL
GOCT
MOTOR
TRIFASICO

www.genteca.com.ve
excelinevzla
NOTA DE APLICACIÓN
03
NA 2021-V1-005
Conﬁguración del relé de protección integral
Este relé de protección integral es sencillo de conﬁgurar, tiene tres parámetros:
1- Modo de rearme (Auto/Manual): Es una práctica común colocarlo en Auto para que
después de una falla el equipo se conecte automáticamente después de desaparecida
está y transcurrido el tiempo de conexión. En el caso, de que por alguna razón se deba
colocar en manual, se requerirá pulsar el botón verde de rearme del producto para que se
realice la activación del motor.
2- Corriente de sobrecarga (FLA): Se requiere conocer tanto la Corriente Nominal como
el Factor de servicio, que es un valor porcentual que generalmente se mueve entre 10 y
25%. Estos valores se ubican en la placa del motor. Por ejemplo, el valor a colocar en la perilla
es la corriente nominal más el factor de servicio. Por ejemplo si la corriente nominal de un
motor es 10 A y el factor de servicio es de 25%, el valor a colocar es de 12,5 A.
3- Tiempo de Conexión (TC): Es el tiempo que esperara el relé de protección para
reconectar el motor cuando se encuentra en modo automático, después de una falla de
voltaje. En este caso hay dos recomendaciones: Para los equipos de refrigeración
este tiempo debe ser mayor a los tres minutos y si se tienen más de un protector en la
instalación se recomienda conﬁgurarlos en valores diferentes para que la reconexión no se
realice en simultaneo, produciendo un pico de demanda.
Funcionalidad del relé de protección integral.
El relé de protección integral impedirá la conexión del motor antes un desbalance de Voltaje
VUB, variación de la Frecuencia nominal FREC por encima de los parámetros conﬁgurados,
perdida de Fase de Voltaje VSP y ante una secuencia invertida, asimismo la desconexión
será inmediata ante estas fallas sin importar el estado de la corriente.
Fallas de voltaje alto y bajo: El relé no permitirá la conexión del motor en condiciones falla de
voltaje alto o bajo y solo se detecta cuando el motor presenta condición de sobrecarga o
cuando la corriente es cero (motor apagado por falla u otro control).
- Voltaje bajo UV: Se determina la presencia de sí el voltaje es menor que el ajustado por
el usuario.
- Voltaje alto OV: Se determina la presencia de sí el voltaje es mayor que el ajustado por
el usuario.
Fallas de Sobre Corriente: Las fallas de sobrecarga se pueden generar por: Pérdida de fase de
corriente (CSP) o desbalance de corriente (CUB) con un tiempo de detección ﬁjo de 3 s y por
sobrecarga (OL) que se basa en el modelo térmico cuya curva para clase 10 se observa en el
graﬁco a continuación.

GOCT Curva Fr’a -  Curva Caliente
Tiempo de Disparo (s)
I carga / I nom *
(*) I nom= Valor de corriente calibrada por el usuario en el GOCT.
I nom es lo mismo que la corriente del motor con su m‡xima carga FLA tal como se muestra en los ajustes del producto.
1
10
100
1000
10000
0,0
1,0
2,0
3,0
4,0
5,0
6,0
7,0
8,0
9,0
10,0
Curva Fría
Curva Caliente
www.genteca.com.ve
excelinevzla
NOTA DE APLICACIÓN
En los parámetros de la gráﬁca, Icarga es la corriente del equipo y la Inom es la corriente
conﬁgurada, con esta relación se determina el tiempo que tardara en disparar o desconec-
tar el relé, si es la primera vez usara la curva fría, en las siguientes oportunidades lo realizara
con la curva caliente (aproximadamente tres veces más rápido). Si ocurren tres fallas sucesi-
vas de corriente en menos de 30 minutos, el relé desconectara de forma permanente hasta
que un usuario lo rearme.
NA 2021-V1-005
04
▶ GOCT: Relé de Protección Integral
ra Motores trifásicos, basado en
tecnología de microcontroladores,
diseñado
especíﬁcamente
para
proteger motores eléctricos contra
los
daños
causados
por
fallas
comunes de corriente y voltaje.
▶ GMP5-3540: Supresor de picos de
alta energía producidas tanto por
descargas
atmosféricas
como
internas por la conexión y descon-
exión subestaciones eléctricas o
grandes maquinas eléctricas. Corri-
ente máxima de descarga 70 kA,
con tiempo de respuesta menor a
25 ns.
▶ GTPA: Temporizador con retardo
a la conexión (Opcional) en serie
con la bobina del contactor.
Productos requeridos para los esquemas eléctricos

www.genteca.com.ve
excelinevzla
NOTA DE APLICACIÓN
En caso de cualquier inquietud a contactarnos directamente a través del correo info@genteca.com.ve
Información Adcional
NA 2021-V1-005
04
Recomendaciones
1. Utilice un relé trifásico integral por cada motor protegido y no conecte cargas adicionales en la línea de protección,
ya que podría afectar la detección de las fallas, produciendo desconexiones por falsos desbalances o fases perdidas
de corriente.
2. Instruya al personal de operaciones para que identiﬁque el apagado por tercera falla (los tres leds rojos titilando en
forma secuencial) y realice una correcta veriﬁcación del sistema antes de presionar el botón verde de rearme, ya que
la falla mecánica podría continuar presente.
3. Es importante incluir rutinas de mantenimiento para la inspección del estado de los supresores de picos, cuando la
ventana de los GMP5-35XX está en rojo, indica que este debe ser sustituido.
4. Los supresores de picos son módulos independientes por fase, se conectan entre fase y tierra. El calibre del cable es
otro punto importante a cuidar en esta instalación, se recomienda en este caso que sea mínimo AWG 10, siendo el
máximo permitido AWG 6.
5. Veriﬁque la conexión a tierra del sistema eléctrico, es importante para la apropiada protección ante una descarga de
alta energía.
6. Mantenga siempre las protecciones independientes por equipo en sus instalaciones, algunos equipos requieren
condiciones especiales de protección y además evita que regresar la energía todos los equipos conecten en simulta-
neo (lo que produce una alta demanda que podría ocasionar otros problemas).
7. En caso de usar el retardador a la conexión veriﬁque que el cable que deﬁne el modelo de voltaje este separado
para que este conﬁgurado para 120/240.
8. La selección del contactor es básico para esta aplicación, además de utilizar el tamaño de cable apropiado para el
consumo de corriente.
▶ Cantidad de Polos: En este caso deben ser tres polos
▶ Categoría: AC1 para cargas resistivas o AC3 para cargas inductivas.
▶ Corriente: en caso de no tener la corriente nominal de la instalación puede realizar la medición de la
corriente por fase y seleccionar el contactor de capacidad superior comercialmente.
▶ Bobina del Contactor: Se dimensiona en función del voltaje de la señal de control, para el esquema
presentado esta en función de la señal de la instalación.
▶ Contactos auxiliares: Permiten señales del estado del contactor, es importante deﬁnir si se requiere normal-
mente cerrados (NC) o normalmente abiertos (NO).
