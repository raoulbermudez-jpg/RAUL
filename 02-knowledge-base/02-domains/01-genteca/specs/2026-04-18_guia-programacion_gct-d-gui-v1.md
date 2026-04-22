---
title: "Función relacionada"
type: Technical
source: "GCT-D_GUI_V1.pdf"
product_code: "GCT-D"
product_line: "Exceline Profesional"
document_type: "guia-programacion"
date_processed: "2026-04-18"
---

# Función relacionada

Función relacionada
Estado
Co m p r e s o r
D e s c o n g e l a d o
A l a r m a
Ve n t i l a c i ó n
Compresor
Alarma
Descongelado
Ventilación
ARRIBA
ABAJO
SALIR/ATRÁS
ENTER/AJUSTE
Encendido cuando el compresor está en funcionamiento,
destella en caso de retardo, protección, bloqueo habilitado.
Corriente (refrigeración, congelado y ventilación
Temperatura de uso
Temperatura de almacenado
Longitud de cable de sonda
Producto (dimensiones externas)
Longitud del cable de la sonda
Rango de control de temperatura (sonda NTC)
Resolución de la pantalla
Precisión
Tipo de sonda
20/10A/5A/ 240V
-5°C - 55°C. Humedad relativa: 10% - 90v
-30°C – 85°C.
2m (incluyendo la sonda)
Largo 77 × Ancho 34.5 × Fondo 58 (mm)
Largo 71 × Ancho 29 (mm)
-50...110°C (-58...230°F)
1°C / 0.1°C (con modo de cambio entre entero y decimal)
NTC: ±0.5°C (-30°C a 50°C), para otros rangos, ±1°C
NTC (-50°C ~ 120°C)
Encendido cuando el ventilador está funcionando.
Encendido cuando la alarma esta activada; destella cuando
la alarma este silencio.
Encendido al descongelar: destella en caso de habilitado
manual.
Alimentación
80 a 260V ± 10% 50/60Hz
Más Información
El GCT-D es un controlador de temperatura digital utilizado
principalmente para controlar sistemas de refrigeración, con funciones
integradas de descongelamiento (defrost) y gestión de ventiladores.
GCT-D
CONTROLADOR DIGITAL
DE TEMPERATURA
DESCRIPCIÓN DEL DISPLAY Y CODIFICACIÓN
ESPECIFICACIONES TÉCNICAS
DUAL (DESCARCHE AUTOMÁTICO)
GUÍA RÁPIDA
S2
SALIDAS
Compresor
Descarche
Ventilador
20A@ 240 V~
10A@ 240 V~
5A@ 240 V~
80 a 260 V~
SERIAL N°:
-50 a 110 °C
ALIMENTACIÓN
TEMPERATURA
S1
AUXILIAR
Max 5 VDC
DIAGRAMA DE CONEXIÓN
72 ± 0.5  mm
30 ±
0.5 mm
MONTAJE EN PANEL
Página 1/2

* Para acceder a estas conﬁguraciones Presionar “set”
durante 5 segundos. Utilizar las ﬂechas para navegar entre las secciones.
LEYENDA
• Temp: Temperatura
• Pb1: Sonda 1 (Ambiente)
• Pb2: Sonda 2 (Descongelado y Ventilador)
• Set: Set-point
CONFIGURACIÓN BÁSICA
CONFIGURACIÓN Y VALORES
PREDETERMINADOS
Página 2/2
GCT-D
GUÍA RÁPIDA
Temp PB1
SET
PB1
PB2
Pulsar SET
Pulsar SET
Pulsar SET
Temp de PB1
Temp de PB2
Pulsar  SET
En pantalla
Ajustar
Setpoint
Encendido Inicial
SECCION DE
CONFIGURACIÓN
SIGLAS
UNIDAD
DESCRIPCIÓN
VALOR
PREDETERMINADO
Co m p r e s o r
Co n ﬁg u ra c i ó n
A l a r m a
Ve n t i l a d o r e s
D e s c o n g e l a d o
Diferencial del compresor. El compresor se detiene
al alcanzar el setpoint y se reanuda cuando la
temperatura supera el setpoint en este valor.
Límite inferior del setpoint. Valor mínimo que se
puede ajustar como temperatura deseada.
Límite superior del setpoint. Valor máximo que
se puede ajustar como temperatura deseada.
Presencia de la sonda del evaporador (sonda 2).
Indica si está instalada (y) o no (n).
Diferencial de alarma. Margen para evitar
activaciones/desactivaciones intermitentes
de la alarma de temperatura.
Temperatura de parada de ventiladores. Los
ventiladores se apagan cuando la sonda del
evaporador alcanza o baja de este valor.
Tiempo de retardo de ventiladores después del
descongelamiento. Tiempo de espera para que
drene el agua antes de reactivar los ventiladores.
Diferencial de ventiladores. Los ventiladores se
reactivan cuando la temperatura del evaporador
supera FSt + FAd.
Temperatura de ﬁn de descongelamiento. El ciclo
termina cuando la sonda del evaporador alcanza
este valor.
Duración máxima del descongelamiento.
Tiempo de seguridad para ﬁnalizar el ciclo
si no se alcanza dSt.
Intervalo entre descongelamientos. Tiempo entre
el inicio de dos ciclos consecutivos.
dIF
LSE
HSE
H42
AFd
FSt
Fdt
FAd
dSt
dit
dEt
2,0
-50,0
99,0
y
2,0
2,0
0
2,0
8,0
6
30
°C/°F
°C/°F
°C/°F
Bandera
(sí/no)
°C/°F
°C/°F
min
°C/°F
°C/°F
Horas
min
Temp de Set
