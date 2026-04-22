# Hoja de Especificaciones — Programador Horario Digital GTC-B1C MV con Salida de Control

**Línea:** Exceline Profesional  
**Código de producto:** GTC-B1C MV  
**Tipo de documento:** Hoja de Especificaciones  
**Fabricante:** Gente, Generación de Tecnología, C.A. — www.genteca.com.ve  
**Referencia PDF:** GTC-B1C-MV-Programador.pdf (Exceline/GTC-B1C-MV-Programador.pdf en RAG_SOURCES)

---

## Descripción General

El GTC-B1C MV es un programador horario semanal para la automatización de cargas eléctricas accionadas por un contactor. Cuenta con un contacto SPDT capaz de manejar hasta 3,5 A @ 250V~ para uso en circuitos de control.

Aplicaciones: aires acondicionados, sistemas de iluminación, avisos comerciales, sistemas de bombeo, sistemas de riego, sistemas de ventilación forzada, piscinas, y cualquier equipo controlado por contactor.

---

## Características Generales

- Programador semanal de múltiples eventos: hasta 16 encendidos y 16 apagados
- 3.000 horas de respaldo en ausencia de energía (batería CR2032)
- Nunca pierde eventos programados al cambiar la batería
- Multivoltaje 120/220 V~
- Pantalla LCD con menú en español
- Batería de respaldo reemplazable
- 15 combinaciones de programas diarios
- Salida de control SPDT: 3,5 A @ 250V~
- Montaje superficial, riel simétrico o cajón 2"×4"
- Funciones adicionales: cuenta regresiva, modo aleatorio (simular presencia), horario de verano (DST), modo manual (ON/OFF permanente)

---

## Normas Aplicadas

- IEC 61000-4-2 — Descarga electrostática
- IEC 61000-4-3 — Inmunidad a Ruido Eléctrico Radiado
- IEC 61000-4-4 — Transientes Rápidas
- IEC 61000-4-5 — Picos de Alta Energía
- NOM-003-SCFI-2000 — Especificaciones de seguridad en productos eléctricos
- IEC 60730-1 — Controles automáticos para uso doméstico y similar

---

## Especificaciones Técnicas

| Parámetro | Valor |
|-----------|-------|
| Voltaje nominal de operación | 120/220 V~ |
| Límites de operación de voltaje | 84-285 V~ |
| Frecuencia eléctrica del suministro | 50/60 Hz |
| Consumo máximo | 155 mA |
| Expectativa de vida de los contactos | 100.000 operaciones |
| Cantidad máxima de eventos programables | 16 encendidos + 16 apagados |
| Intervalo mínimo entre eventos | 1 minuto |
| Pantalla de visualización | LCD |
| Vida de la batería en ausencia de electricidad | 3.000 horas |
| Tipo de batería reemplazable | CR2032 |
| Temperatura ambiental de operación | -5 °C a +55 °C (23 °F a 131 °F) |
| Humedad relativa | 85% |
| Material de la carcasa | ABS |
| Peso | 0,15 Kg (0,33 lb) |
| Control auxiliar de contactores y arrancadores | 3,5 A @ 250V~ |
| Medidas | 112,6 × 51,7 × 80 mm |

---

## Características Físicas (descripción de botones)

1. Pantalla LCD — hora actual y programación de eventos
2. Botón Prog — ingreso al menú de programación
3. Botón Reloj — ajustar reloj y salir del menú
4. Botón Día — seleccionar días de la semana
5. Botón Hora — ajustar hora y formato
6. Botón Minutos — ajustar minutos
7. Botón R — borrar eventos y reiniciar hora (mantener 5 s)
8. Botón modo rearme — cambiar entre Auto y Manual
9. Cubierta protectora y bornes de conexión
10. Tapa posterior de batería reemplazable
11. Gancho sujetador para riel simétrico
12. Guías de orificios para montaje superficial o cajón 2"×4"
13. Laminilla plástica roja descartable (protección batería en almacenaje)
14. Batería

---

## Diagrama de Conexión

```
SUMINISTRO ELÉCTRICO 3~ → GTC-B1C MV (A1-A2)
                                    ↓
                    Salida SPDT: terminales 4 (NA) / 5 (Común) / 6 (NC)
                                    ↓
                              CONTACTOR → CARGA A AUTOMATIZAR
```

Terminal 4: Contacto conectado durante eventos activos (NA)  
Terminal 5: Común  
Terminal 6: Desconectado durante eventos activos (NC)

---

## Modos de Funcionamiento

| Modo | Descripción |
|------|-------------|
| Manual ON | Equipo encendido permanentemente sin seguir eventos |
| Manual OFF | Equipo apagado permanentemente sin seguir eventos |
| Auto ON | Equipo encendido hasta el próximo evento de apagado |
| Auto OFF | Equipo apagado hasta el próximo evento de encendido (default de fábrica) |

---

## Cómo Ordenar

```
GTC-B1C MV
  Aplicación: C = Control (circuito auxiliar/contactor)
  Voltaje: MV = 120/220 V~
```

---

## Diagramas

> Las vistas dimensionales y el esquema de conexión completo son gráficos en el PDF original. Fuente: `G:\Mi unidad\WorkspaceIA\RAG_SOURCES\Exceline\GTC-B1C-MV-Programador.pdf`
