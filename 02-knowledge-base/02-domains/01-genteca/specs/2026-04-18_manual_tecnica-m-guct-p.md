---
title: "GENIUS GUCT+"
type: Technical
source: "11_Biblioteca_Tecnica_M_GUCT_P.pdf"
product_line: "Genius"
document_type: "manual"
product_code: "GUCT+"
date_processed: "2026-04-18"
---

# GENIUS GUCT+

GENIUS GUCT+

MAPA DE DIRECCIONES MODBUS


GRUPO
ADDRESS
DESCRIPCION
ACCESO
GENTE
ACCESO
USUARIO
MIN
MAX
PASO
UNIDAD
TIPO DE
FORMATO
VALOR DE
FABRICA
ID
00000
ID
R
R
12
12


F0
13

00001
MODELO
R
R
162
252
1


NOTA2

00002
VERSION
R
R
0
255
1

F2


00003
ADDRESS_MODBUS
R/W
R/W
1
127
1

F3
1

00004
RESTAURAR_SISTEMA
R
R/W
0
1
1

F7

00005
CLAVE_ACTIVA
R/W
R/W
0
65535
1

F4
0
SEGURIDAD
00006
SERIAL_L
R/W
R
0
65535
1



CALIBRACION
00008
CAL_VL1L2_L
R/W
R
-
3,4028E+3
8
3,40277E+38
1

F37
NOTA1

00010
CAL_VL2L3_L
R/W
R
-
3,4028E+3
8
3,40277E+38
1

F37
NOTA1

00012
CAL_VL3L1_L
R/W
R
-
3,4028E+3
8
3,40277E+38
1

F37
NOTA1

00014
CAL_IA_L
R/W
R
-
3,4028E+3
8
3,40277E+38
1

F38
NOTA1

00016
CAL_IB_L
R/W
R
-
3,4028E+3
8
3,40277E+38
1

F38
NOTA1

00018
CAL_IC_L
R/W
R
-
3,4028E+3
8
3,40277E+38
1

F38
NOTA1

00020
CAL_FRECUENCIA_L
R/W
R
-
3,4028E+3
8
3,40277E+38
1

F5
1,00

00032
RESERVADO
R
R

GENIUS GUCT+


00033
MENU_VOLTAJE_BAJO
R
R/W
350
460
1
VAC
F35
432

00034
MENU_VOLTAJE_ALTO
R
R/W
469
580
1
VAC
F36
520
AJUSTE VOLTAJE
00035
MENU_VDESBALANCE
R
R/W
2
10
1
%
F7
6

00036
MENU_FRECUENCIALINE
R
R/W
0
1
1

F42
1

00037
MENU_FRECUENCIA
R
R/W
2
10
1
%
F7
2

00038
MENU_TD_VOLTAJE
R
R/W
1
30
1
Seg
F7
10

00039
MENU_TC_VOLTAJE
R
R/W
0
600
1
Seg
F7
60

00040
RESERVADO
R
R







00064
RESERVADO
R
R







00065
MENU_I_NOMINAL
R
R/W
15
180
1
AMP
F39


00066
MENU_CLASE_MOTOR
R
R/W
5
30
1

F7
5

00067
MENU_SOBRECARGA
R
R/W
5
50
1
%
F7
10

00068
MENU_SUBCARGA
R
R/W
0
1
1

F52
0

00069
MENU_LARGA_ACELERACI
ON
R
R/W
0
1
1

F7
0

00070
MENU_RL_ACELERADO
R
R/W
0
1
1

F7
0
AJUSTE
CORRIENTE
00071
MENU_TERCERA_FALLA
R
R/W
0
1
1

F7
0

00072
RESERVADO
R
R







00073
MENU_IN_PF
R
R/W
0
1
1

F52
0

00074
MENU_TD_SUBCARGA
R
R/W
5
600
1
Seg
F7
50

00075
MENU_TC_SUBCARGA
R
R/W
2
500
1
Min
F7
5

00076
RESERVADO
R
R







00077
MENU_SUBCARGA_PF
R
R/W
3
9
1
PF/10
F7
5

00078
MENU_SUBCARGA_IN
R
R/W
30
90
1
%
F7
80

00079
MENU_TIEMPO_LARGA_AC
R
R/W
20
120
1
Seg
F7
20

GENIUS GUCT+

EL

00128
MINUTO
R
R/W
0
59
1
Min
F7


00129
HORA
R
R/W
0
23
1
Horas
F7

RELOJ
00130
DIA_SEMANA
R
R
1
7
1

F41


00131
DIA
R
R/W
1
31
1
Dia
F7


00132
MES
R
R/W
1
12
1
Mes
F7


00133
ANO
R
R/W
0
45
1
Año
F7

ESTATUS
00160
FALLA
R
R
0



F18


00161
TIEMPO_CONEXION
R
R
0
30000
1
Seg
F7


00162
RELE
R
R
0
1
1

F7


00163
MODO_REARME
R
R/W
0
1
1

F19
0

00164
CONTROL_ON_OFF
R
R/W
0
6
1

F10


00165
ARRANQUE_TOTAL
R/W
R
0
65535
1

F7
1

00166
CONTADOR_DE_AF
R/W
R/W
0
65535
1

F7


00192
FRECUENCIA
R
R
400
700
1
Hz/10
F7


00193
PERIODO
R
R
14280
25000
1
uS
F7

MEDICIONES
00194
VL1L2
R
R
0

1
VAC
F7


00195
VL2L3
R
R
0
1
VAC
F7


00196
VL3L1
R
R
0

1
VAC
F7


00197
VPROMEDIO
R
R
0

1
VAC
F7


00198
IA
R
R
0

1
AMP/10
F7


00199
IB
R
R
0

1
AMP/10
F7


00200
IC
R
R
0

1
AMP/10
F7


00201
IPROMEDIO
R
R
0

1
AMP/10
F7

GENIUS GUCT+


00202
FACTOR DE POTENCIA
R
R
0
100
1
FP/100
F7


00203
CAPACIDAD_TEMP
R
R
0
65535
1
%
F7


00204
POTENCIA_W
R
R
0
9999
1

F45
0

00205
POTENCIA_VA
R
R
0
9999
1

F45
0

00206
TOTAL_ENERGIA_L
R/W
R
0
99999999
1
10xW/H
F8
0

00208
TOTAL_HORAS_L
R/W
R
0
59999940
1
Min
F8
0

00210
CAPACIDAD_TERMICA_L
R
R


1

F5


00213
CLASE_DINAMICA
R
R
6
20
1

F7

AJUSTES DEL
01536
CONTROL_HORARIO
R/W
R/W
0
1
1

F7
0
PRODUCTO
1537-2017
Evento  01/60 - 60/60
R/W
R/W
0



F48


3072-3152
Feriado 01/20 - 01/20
R/W
R/W
0



F49

HISTORICO
04096
NUMERO_TOTAL_FALLAS
R
R/W
0
20
1

F7
0

04097
POINTER_FALLAS
R
R
0
19
1

F7


4098-4418
Falla     01/20 - 20/20
R
R
0



F50





NOTA1: dichos valores son definidos en el momento de la calibración del producto
NOTA2: ver identificación electrónica del la familia genius

GENIUS GUCT+

FORMATOS DE DATOS


CODIGO
FORMATO
TIPO
DEFINICION
F0
8 bits
Identificador del producto

1
GI

2
GII & GII+

3
GII_LN

10
GOC-T

11
GOC-S

12
GIII

13
GUC-T

14
GSPMV
F1
8 bits
Modelo del producto

bits 2...0
Tesión nominal del producto (1 A 4):


1= 120V


2= 240V


3= 380V


4= 480V

bits 4…3
Corriente nominal del producto (solo GIII) (0 a 3):


0= 50A@GIII


1= 100A@GIII


2= 180A@GIII


3= CT@GIII

bits 6…5
Idioma  (0 a 3):  GII, GII+, GIII y GIII+


1= ESPAÑOL


2= INGLES


3= PORTUGUES

bit 7
0= Producto sin RTC  (GII+ y GIII+)


1= Producto con RTC

bits 5…3
Corriente nominal del producto (solo GOC) (1 a 4):


1= 4A@GOC


2= 12A@GOC


3= 32A@GOC

GENIUS GUCT+



4= 80A@GOC


Ejemplo: G3 240VAC 30-100Amp Español sin RTC


Modelo tensión=  0x02


Modelo corriente=  0x01<<3 = 0x08


Idioma= 0x01<<5=  0x20


MODELO =  0x20 | 0x08 | 0x02 = 0x2A
F2
8 bits
Version del software

bits 4...0
Versión menor del software (0 a 31)

bits 7…5
Versión mayor del software (0 a 7)


Ejemplo: G2+  Software v1.04


Versión menor= 0x04


Versión mayor= 0x01<<5= 0x20


VERSION= 0x20 | 0x04 = 0x24
F3
16 bits
Dirección ModBus del dispositivo

byte 0
Dirección (1 a 127)

byte 1
nulo
F4
16 bits
Unsigned int - Indicador de protección de escritura

0x0000
Parámetros desprotegidos - Calibración protegida

0x0001
Parámetros protegidos - Calibración protegida

0xFFFF
Parámetros protegidos - Calibración desprotegida

0x0002 a 0xFFFE Código encriptado del password del producto - Parámetros y Calibración protegidos
F5
32 bits
Float 24bits

0xNNNNNN00
Float 24 bits


Ejemplo: Valor1 = 1,023  = 0x003F82F1
F6
16 bits
Unsigned char

byte 0
Valor

byte 1
nulo
F7
16 bits
Unsigned int
F8
32 bits
Unsigned Long

GENIUS GUCT+

F9
16 bits
Signed int
F10
16 bits
Estado del producto - Control ON/OFF


GOCT v01,v02; GI ;  GII y GII+

0
ON

1
OFF FALLA

2
OFF TIEMPO DE CONEXIÓN DE VOLTAJE

3
OFF MODBUS

4
OFF MANUAL

5
OFF TERCERA FALLA (Solo productos con medición de corriente)

6
OFF HORARIO (Solo Productos con RTC)


GIII+ / GUCT

0
ON

1
OFF FALLA

2
OFF TIEMPO DE CONEXIÓN DE VOLTAJE

3
OFF MODBUS

4
OFF MANUAL

5
OFF TERCERA FALLA (Solo productos con medición de corriente)

6
OFF HORARIO (Solo Productos con RTC)

7
OFF TIEMPO DE CONEXION DE CORRIENTE

8
OFF TIEMPO DE CONEXIÓN DE BAJA CORRIENTE


GSPMV / GSPT

0
ON

1
OFF FALLA

2
TEMPORIZANDO

3
OFF MODBUS

4
OFF MANUAL

5
OFF TERCERA FALLA

7
OFF RELE DESVIADO
F11
32 bits
Eventos del control horario

bits 5...0
ON Minutos - 0 a 59

bits 10…6
ON Hora - 0 a 23

bits 16…11
OFF Minutos - 0 a 59

bits 21…17
OFF Hora - 0 a23

bits 23…22
No utilizados

bits 24
Evento activo el día Lunes

GENIUS GUCT+


bits 25
Evento activo el día Martes

bits 26
Evento activo el día Miercoles

bits 27
Evento activo el día Jueves

bits 28
Evento activo el día Viernes

bits 29
Evento activo el día Sabado

bits 30
Evento activo el día Domingo

bits 31
Evento activo el día Feriado
F12
80 bits
Falla en el historico - GIII

byte 0
Tipo de falla (0 a 11)


0= FREC - Falla de frecuencia


1= PR - Fase invertida


2= VSP - Fase perdida de tensión


3= VUB -  Desbalance de voltaje


4= UV - Voltaje bajo


5= OV - Voltaje alto


6= RT - Falla del rotor


7= PF - Falla por factor de potencia


8= CUB - Desbalance de corriente


9= UC - Subcarga de corriente


10= OL - Sobrecarga de corriente


11= CSP - Fase perdida de corriente


12= AF- Arranque forzado


13= TEF- Falla total de energía

byte 2...1
Valor principal de la falla (magnitud)

byte 3
Valor auxiliar (fase)

byte 4
Día - 1 a  31                       (Cero si el producto no tiene RTC)

byte 5
Mes - 1 a 12                      (Cero si el producto no tiene RTC)

byte 6
Hora - 0 a 23                     (Cero si el producto no tiene RTC)

byte 7
Minutos - 0 a 59                 (Cero si el producto no tiene RTC)

byte 9...8
Duración (0 a 9999 min)      (Cero si el producto no tiene RTC)
F13
16 bits
Feriado del control horario - GIII & GII+

byte 0
Día

byte 1
Mes
F14
16 bits
Puntero del historico GII

GENIUS GUCT+


byte 0
Número de fallas (0 a 20)

byte 1
Puntero  (0 a 19)
F15
16 bits
Falla en el historico - Valor principal - GII

bits 9...0
Valor de la falla

bits 11…10
MSbits duración falla (solo GII+) - D13…D12


El tiempo de falla será D13 D12…..D1 D0 - (0 a 9999 min) - (ver F16)


Si D13=D12=1 => La falla está activa, por lo que no se ha registrado la duración

bits 15…12
Valor de la falla


0= FREC - Falla de frecuencia


1= PR - Fase invertida


2= VSP3 - Fase perdida L3


3= VSP1 - Fase perdida L1


4= VSP2 - Fase perdida L2


5= VUB -  Desbalance de voltaje


6= UV12 - Voltaje bajo linea L1L2


7= UV23 - Voltaje bajo linea L2L3


8= UV31 - Voltaje bajo linea L3L1


9= OV12 - Voltaje alto linea L1L2


10= OV23 - Voltaje alto linea L2L3


11= OV31 - Voltaje alto linea L3L1


12= LN - Perdida de neutro
F16
32 bits
Falla en el historico - Valor secundario - GII+

bits 5...0
Minutos - 0 a 59

bits 10…6
Hora - 0 a 23

bits 15…11
Día - 1 a  31

bits 19…16
Mes - 1 a 12

bits 32…20
LSbits duración falla  - D11…D0 - (0 a 9999 min)


El tiempo de falla será D13 D12…..D1 D0 - (0 a 9999 min) - (ver F15)


Si D13=D12=1 => La falla está activa, por lo que no se ha registrado la duración
F17
16 bits
Registro de fallas G2

0
No Falla

bit 0
Falla - Frecuencia

bit 1
Falla - Fase invertida - PR

bit 2
Falla - Fase perdida de tensión - VSP

GENIUS GUCT+


bit 3
Falla - Desbalance de tensión - VUB

bit 4
Falla - UV

bit 5
Falla - OV
F18
16 bits
Registro de fallas G3

0
No Falla

bit 0
Falla - Frecuencia

bit 1
Falla - Fase invertida - PR

bit 2
Falla - Fase perdida de tensión - VSP

bit 3
Falla - Desbalance de tensión - VUB

bit 4
Falla - UV

bit 5
Falla - OV

bit 6
Falla - Rotor Bloqueado

bit 7
Falla - Factor Potencia

bit 8
Falla - Desbalance de corriente - CUB

bit 9
Falla - UC

bit 10
Falla - OL

bit 11
Falla - Fase perdida de corriente - CSP
F19
1 bits
Modo de rearme

0
MANUAL

1
AUTO
F20
8 bits
Unsigned char  - Factor para cálculo de tensión - GI & GOC

Valor
Voltaje  = Vnom* ( Valor /300 + 0,6) (V)


Vnom = Tensión nominal de producto


Vnom= 120     @    modelo = 120V


Vnom= 214     @    modelo = 220V


Vnom= 380     @    modelo = 380V


Vnom= 460     @    modelo = 480V
F21
8 bits
Unsigned char  - Factor para cálculo de frecuencia de la red - GI

Valor
Frecuencia = 31250 / ( Valor + 460 ) (Hz)
F22
8 bits
Unsigned char  - Factor para cálculo de fase -GI

Valor
Fase = Valor * 6 ( grados )

GENIUS GUCT+

F23
8 bits
Unsigned char  - Factor para cálculo del nivel de voltaje bajo - GI

Valor
UV= Vnom*((K2-(K1* Valor /128)) / 300+0.6)  (V)


Vnom = Tensión nominal de producto


K1= 44   -   K2= 115  - Vnom= 120     @    modelo = 120V


K1= 39   -   K2= 100  - Vnom= 214     @    modelo = 220V


K1= 44   -   K2= 112  - Vnom= 380     @    modelo = 380V


K1= 39   -   K2= 93    - Vnom= 460     @    modelo = 480V
F24
8 bits
Unsigned char  - Factor para cálculo del nivel de voltaje alto - GI

Valor
OV= Vnom*((K2+(K1*valor/128)) / 300+0.6)  (V)


Vnom = Tensión nominal de producto


K1= 44   -   K2= 120  - Vnom= 120   @    modelo = 120V


K1= 38   -   K2= 142  - Vnom= 214   @    modelo = 220V


K1= 44   -   K2= 117  - Vnom= 380   @    modelo = 380V


K1= 40   -   K2= 146  - Vnom= 460   @    modelo = 480V
F25
8 bits
Unsigned char  - Factor para cálculo del nivel del tiempo de desconexión TD - GI

Valor
TD= int(2 + Valor * 0.0703 )/4(s)
F26
8 bits
Unsigned char  - Factor para cálculo del nivel del tiempo de conexión TC - GI

Valor
TC= int(20 + Valor * 4,628)/4 (s)
F27
8 bits
Registro de fallas GI

0
No Falla

bit 0
Falla - UV

bit 1
Falla - OV

bit 2
Falla - Desbalance de tensión - VUB

bit 3
Falla - Fase invertida - PR

bit 4
Falla - Fase perdida de tensión - VSP
F28
32 bits
Cuenta del tiempo para la conexión del rele  - GI

byte 0
TC_L

byte 1
nulo

byte 2
TC_H

byte 3
nulo


Conexión en =  ((TC_H*256 +  TC_L) *0.25 )  (s)

GENIUS GUCT+

F29
16 bits
Cuenta del tiempo para la conexión del rele - GOC

Valor
Conexión en =  ((2 *  Valor ) + 1) (s)
F30
8 bits
Registro de fallas GOC

0
No Falla

bit 0
Falla - OV

bit 1
Falla - UV

bit 2
Falla - Desbalance de corriente - CUB

bit 3
Falla - Desbalance de tensión - VUB

bit 4
Falla - Fase perdida de tensión - VSP

bit 5
Falla - Fase perdida de corriente - CSP

bit 6
Falla - Fase invertida - PR

bit 7
Falla - OL
F31
32 bits
Unsigned char  - Factor para cálculo de calor acumulado - GOC

byte 0
CALOR_L

byte 1
nulo

byte 2
CALOR_H

byte 3
nulo


Calor =  ((CALOR_H*256 + CALOR_L) / 616) (%)
F32
8 bits
Unsigned char  - Factor para cálculo de frecuencia de la red - GOC

Valor
Frecuencia = 15625 / ( Valor + 128 ) (Hz)
F33
8 bits
Unsigned char  - Factor para cálculo de fase - GOC

Valor
Fase = Valor * 3,6 ( grados )
F34
8 bits
Unsigned char  - Factor para cálculo de corriente - GOC

Valor
I = Valor(In) * K1 * Valor(I_MAXIMO) / ( K2 * 250 ) donde In es IA, IB ó IC


K1 =   40  K2 = 73    @    modelo = 1,0  -  4,0 A


K1 = 125  K2 = 73    @    modelo = 3,5 - 12,5 A


K1 = 320  K2 = 73    @    modelo = 10,0  - 32,0 A


K1 = 800  K2 = 73    @    modelo = 25,0  - 80,0 A
F35
16bits
Unsigned int - Valor de umbral de voltaje bajo - UV

Valor
GII & GIII

Min=  95V  -   Max= 115V   -  Valor fabrica= 108V   @   modelo= 120V

GENIUS GUCT+



Min= 165V  -   Max= 225V   -  Valor fabrica= 187V   @   modelo= 220V


Min= 320V  -   Max= 380V   -  Valor fabrica= 360V   @   modelo= 380V


Min= 350V  -   Max= 460V   -  Valor fabrica= 432V   @   modelo= 440V


GSPMV


Min= 160V  -  Max= 190V  - Valor de fábrica= 180V  @ Voltaje Nominal= 200V


Min= 166V  -  Max= 197V  - Valor de fábrica= 187V  @ Voltaje Nominal= 208V


Min= 176V  -  Max= 209V  - Valor de fábrica= 198V  @ Voltaje Nominal= 220V


Min= 184V  -  Max= 218V  - Valor de fábrica= 207V  @ Voltaje Nominal= 230V


Min= 192V  -  Max= 228V  - Valor de fábrica= 216V  @ Voltaje Nominal= 240V


Min= 320V  -  Max= 380V  - Valor de fábrica= 360V  @ Voltaje Nominal= 400V


Min= 336V  -  Max= 399V  - Valor de fábrica= 378V  @ Voltaje Nominal= 420V


Min= 352V  -  Max= 418V  - Valor de fábrica= 396V  @ Voltaje Nominal= 440V


Min= 368V  -  Max= 437V  - Valor de fábrica= 414V  @ Voltaje Nominal= 460V


Min= 384V  -  Max= 456V  - Valor de fábrica= 432V  @ Voltaje Nominal= 480V
F36
16bits
Unsigned int - Valor de umbral de voltaje alto - OV - GII & GIII

Valor
GII & GIII


Min= 125V  -   Max= 145V   -  Valor fabrica= 132V   @   modelo= 120V


Min= 215V  -   Max= 270V   -  Valor fabrica= 229V   @   modelo= 220V


Min= 420V  -   Max= 480V   -  Valor fabrica= 440V   @   modelo= 380V


Min= 460V  -   Max= 580V   -  Valor fabrica= 528V   @   modelo= 440V


GSPMV


Min= 210V  -  Max= 240V  - Valor de fábrica= 220V  @ Voltaje Nominal= 200V


Min= 218V  -  Max= 249V  - Valor de fábrica= 228V  @ Voltaje Nominal= 208V


Min= 231V  -  Max= 264V  - Valor de fábrica= 242V  @ Voltaje Nominal= 220V


Min= 241V  -  Max= 276V  - Valor de fábrica= 253V  @ Voltaje Nominal= 230V


Min= 252V  -  Max= 288V  - Valor de fábrica= 264V  @ Voltaje Nominal= 240V


Min= 420V  -  Max= 480V  - Valor de fábrica= 440V  @ Voltaje Nominal= 400V


Min= 441V  -  Max= 504V  - Valor de fábrica= 462V  @ Voltaje Nominal= 420V


Min= 462V  -  Max= 528V  - Valor de fábrica= 484V  @ Voltaje Nominal= 440V


Min= 483V  -  Max= 552V  - Valor de fábrica= 506V  @ Voltaje Nominal= 460V


Min= 504V  -  Max= 576V  - Valor de fábrica= 528V  @ Voltaje Nominal= 480V
F37
32 bits
Float 24bits - Factor de calibración de voltaje  GIII & GSPMV

0xNNNNNN00
Float 24 bits


GIII


Valor de fabrica = 0,1179   @   modelo= 220V

GENIUS GUCT+



Valor de fabrica = 0,2034   @   modelo= 380V


Valor de fabrica = 0,2559   @   modelo= 440V


GSPMV


Valor de fabrica = 0.2559   @   modelo= MV
F38
32 bits
Float 24bits - Factor de calibración de corriente - GIII & GSPMV

0xNNNNNN00
Float 24 bits


Valor de fabrica = 1,891   @   modelo= 50A


Valor de fabrica = 3,783   @   modelo= 100A


Valor de fabrica = 6,809   @   modelo= 180A
F39
16bits
Unsigned int - Corriente nominal - GIII & GSP

Valor
Min= 15A  -  Max= 50A    -    Valor fabrica= 25A    @   modelo= 50A


Min= 30A  -  Max= 100A  -    Valor fabrica= 45A    @   modelo= 100A


Min= 55A  -  Max= 180A  -    Valor fabrica= 60A    @   modelo= 180A


Min= 100A  -  Max= 133A  -  Modelo CT =400/5    @   modelo= GIII CTs EXT


Min= 125A  -  Max= 166A  -  Modelo CT =500/5    @   modelo= GIII CTs EXT


Min= 150A  -  Max= 200A  -  Modelo CT =600/5    @   modelo= GIII CTs EXT


Min= 187A  -  Max= 250A  -  Modelo CT =750/5    @   modelo= GIII CTs EXT


Min= 200A  -  Max= 266A  -  Modelo CT =800/5    @   modelo= GIII CTs EXT  (Valor fábrica)


Min= 250A  -  Max= 333A  -  Modelo CT =1000/5   @   modelo= GIII CTs EXT


Min= 300A  -  Max= 400A  -  Modelo CT =1200/5   @   modelo= GIII CTs EXT


Min= 375A  -  Max= 500A  -  Modelo CT =1500/5   @   modelo= GIII CTs EXT


Min= 500A  -  Max= 666A  -  Modelo CT =2000/5   @   modelo= GIII CTs EXT
F40
16 bits
Cuenta del tiempo para la conexión del rele  - GII

Valor
Conexión en =  (Valor *0.25 )  (s)
F41
16 bits
Indica el día de la semana

1
LUNES

2
MARTES

3
MIERCOLES

4
JUEVES

5
VIERNES

6
SABADO

7
DOMINGO

GENIUS GUCT+

F42
1 bits
Frecuencia de la red

0
50Hz

1
60Hz



F43
8 bits
Unsigned char  - Factor para cálculo de Corriente Nominal - GOC

Valor
I = Valor * K1 / K2


K1 =   4  K2 = 73       @    modelo = 1,0  -  4,0 A


K1 = 12,5  K2 = 73    @    modelo = 3,5 - 12,5 A


K1 = 32  K2 = 73       @    modelo = 10,0  - 32,0 A


K1 = 80  K2 = 73       @    modelo = 25,0  - 80,0 A
F44
16 bits
Indica la relacion del CT /5 instalado al GIII

0
400

1
500

2
600

3
750

4
800

5
1000

6
1200

7
1500

8
2000
F45
16 bits
Unsigned int - Valor de la Potencia Real  y Potencia Aparente GIII -GSP-GUCT

Valor
POTENCIA W  = Valor * 10W      @ modelo = 50A, 100A ó 180 A GIII-GSPT / modelo = 4A,12A, 32A, 80A
GUCT


POTENCIA VA = Valor * 10VA    @ modelo = 50A, 100A ó 180 A GIII-GSPT /  modelo = 4A,12A, 32A, 80A
GUCT


POTENCIA W  = Valor * 100W    @ modelo = CTs EXT


POTENCIA VA = Valor * 100VA   @ modelo = CTs EXT
F46
16 bits
Indica el Voltaje de Operación del GSP

0
200 VAC

1
208 VAC

2
220 VAC

3
230 VAC

4
240 VAC

5
400 VAC

GENIUS GUCT+


6
420 VAC

7
440 VAC

8
460 VAC

9
480 VAC
F47
16 bits
Indica como de almacenan las fallas en el histórico de eventos GSP


Nota: Cada falla ocupa 80 registros en el histórico y el formato de los datos almacenados se conservan


iguales a los  establecidos en el mapa modbus

Unsigned Int 0
Código de la Falla

Unsigned Int 1
Valor Principal de la Falla

Unsigned Int 2
Valor Auxiliar de la Falla

Unsigned Int 3
Día de ocurrencia de la Falla

Unsigned Int 4
Mes de ocurrencia de la Falla

Unsigned Int 5
Hora de ocurrencia de la Falla

Unsigned Int 6
Minuto de ocurrnecia de la Falla

Unsigned Int 7
Duración de la Falla

Unsigned Int 9
Menú Voltaje Nominal

Unsigned Int 10
Menú Voltaje Bajo

Unsigned Int 11
Menú Voltaje Alto

Unsigned Int 12
Menú Desbalance de Voltaje

Unsigned Int 13
Menú Ajuste de Frecuencia

Unsigned Int 14
Menú Ajuste de corrimiento de Frecuecia

Unsigned Int 15
Menú Tiempo Mínimo de Apagado

Unsigned Int 16
Menú Tiempo de Desconexión por Voltaje

Unsigned Int 17
Menu Tiempo de Conexión por Voltaje

Unsigned Int 20
Menú Corriente Nominal

Unsigned Int 21
Menú de Sobrecarga

Unsigned Int 22
Menú Tiempo de Conexión por Sobrecarga

Unsigned Int 23
Menú Opción Subcarga

Unsigned Int 24
Menú Tercera Falla

Unsigned Int 25
Menú Arranques Por Hora

Unsigned Int 27
Menú Ajuste de Subcarga

Unsigned Int 28
Menú Tiempo de Desconexión por Subcarga

Unsigned Int 29
Menú Tiempo de Conexión por Subcarga

Unsigned Int 31
Menú Número de Arranques por Hora

Unsigned Int 32
Menú  Opción Temperatura

Unsigned Int 33
Menú Temperatura Mínima

GENIUS GUCT+


Unsigned Int 34
Menú Temperatura Máxima

Unsigned Int 35
Valor de la Falla

Unsigned Int 36
Tiempo de Conexión

Unsigned Int 37
Estado del Relé

Unsigned Int 38
Modo de Rearme

Unsigned Int 39
Control ON\ OFF

Unsigned Int 40
Arranque Total

Unsigned Int 41
Contador de Arranque Forzado

Unsigned Int 42
Frecuencia

Unsigned Int 43
Período

Unsigned Int 44
VL1L2

Unsigned Int 45
VL2L3

Unsigned Int 46
VL3L1

Unsigned Int 47
Voltaje Promedio

Unsigned Int 48
IA

Unsigned Int 49
IB

Unsigned Int 50
IC

Unsigned Int 51
Corriente Promedio

Unsigned Int 52
Factor de Potencia

Unsigned Int 53
Capacidad de Temperatura

Unsigned Int 54
Potencia W

Unsigned Int 55
Potencia VA

Unsigned Int 56
Acumulador de Energía Bajo

Unsigned Int 57
Acumulador de Energía Alto

Unsigned Int 58
Acumulador de Horas de Operación Bajo

Unsigned Int 59
Acumulador de Horas de Operación Alto

Unsigned Int 60
Acumulador de Capacidad Térmica Bajo

Unsigned Int 61
Acumulador de Capacidad Térmica Alto

Unsigned Int 62
Temperatura

Unsigned Int 63
Clase Dinámica



F48
16 bits
Indica como de almacenan los eventos en el GUCT


Nota: Cada configuración de eventos en el GUCT ocupa 8 registros en modbus

Unsigned  Int 0
Dia de la Semana

Bit 0   LUNES

Bit 1   MARTES

Bit 2   MIERCOLES

GENIUS GUCT+


Bit 3   JUEVES

Bit 4   VIERNES

Bit 5   SABADO

Bit 6   DOMINGO

Bit 7   FERIADO

Unsigned Int 1
Hora de Encendido  del Evento

Unsigned Int 2
Minuto de Encendido del Evento

Unsigned Int 3
Hora de Apagado del Evento

Unsigned Int 4
Minuto de Apagado del Evento
F49
16 bits
Indica como de almacenan los feriados en el GUCT


Nota: Cada configuración de feriados en el GUCT ocupa 2 registros en modbus

Unsigned Int 0
Mes

Unsigned Int 1
Dia



F50
16 bits
Indica como de almacenan llas fallas en el GUCT


Nota: Cada falla en el GUCT ocupa 16 registros en modbus

Unsigned Int 0
Tipo de Falla

Unsigned Int 1
Valor Principal de la Falla

Unsigned Int 2
Valor Auxiliar de la Falla

Unsigned Int 3
Dia de ocurrencia de la Falla

Unsigned Int 4
Mes de ocurrencia de la Falla

Unsigned Int 5
Hora de ocurrencia de la Falla

Unsigned Int 6
Minuto de ocurrencia de la Falla

Unsigned Int 7
Duración de la Falla
F51
16 bits
Registro de fallas GSP

0
No Falla

bit 0
Falla - Frecuencia

bit 1
Falla - Fase invertida - PR

bit 2
Falla - Fase perdida de tensión - VSP

bit 3
Falla - Desbalance de tensión - VUB

bit 4
Falla - UV

bit 5
Falla - OV

bit 6
Falla - OT

bit 7
Falla - Rotor Bloqueado

GENIUS GUCT+


bit 8
No Aplica

bit 9
Falla - Desbalance de corriente - CUB

bit 10
Falla - UC

bit 11
Falla - OL

bit 12
Falla - Fase perdida de corriente - CSP

bit 13
Falla - Bypass - BR

bit 14
Falla - Falla Energía en la alimentación - TEF
F52
16 bits
Opción en menú

0
NO

1
SI
F53
16 bits
Corriente GUCT

Valor
Valor Corriente = Valor/100 @ modelo = 4A y 12A


Valor Corriente = Valor/10 @  modelo = 32A y 80A
