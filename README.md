# Simulador de Tráfico con SUMO y TraCI

## Descripción
Este proyecto implementa un simulador de tráfico vehicular utilizando SUMO (Simulation of Urban MObility) y su interfaz de control TraCI (Traffic Control Interface). El sistema permite simular el movimiento de vehículos en una red de carreteras, con control programático de la simulación a través de Python.

## Requisitos del Sistema
- Python 3.x
- SUMO (Simulation of Urban MObility)
- Biblioteca TraCI para Python

## Estructura del Proyecto
```
proyecto_movilidad/
├── red.netcfg          # Configuración de la red de carreteras
├── red.net.xml         # Red generada (archivo generado)
├── rutas.rou.xml       # Definición de rutas y vehículos
├── simulacion.sumocfg  # Configuración de la simulación
└── control_traci.py    # Script de control de la simulación
```

## Componentes Principales

### 1. Configuración de la Red (red.netcfg)
Define una red de carreteras en forma de cuadrícula 3x3 con las siguientes características:
- Tamaño de celda: 100m
- Bordes de conexión: 100m
- Genera bordes normales e internos para la conectividad

### 2. Definición de Rutas (rutas.rou.xml)
- Define el tipo de vehículo con parámetros de aceleración, deceleración y velocidad máxima
- Establece rutas específicas usando bordes de la red
- Programa la salida de vehículos en diferentes momentos

### 3. Control de Simulación (control_traci.py)
Implementa la lógica de control de la simulación con las siguientes funcionalidades:
- Inicialización de la simulación con interfaz gráfica
- Monitoreo en tiempo real de vehículos
- Reinicio automático de la simulación
- Control de velocidad y visualización

## Guía de Uso

### 1. Generación de la Red
```bash
netgenerate -c red.netcfg
```
Este comando genera el archivo `red.net.xml` que contiene la red de carreteras.

### 2. Ejecución de la Simulación
```bash
python control_traci.py
```
El script:
- Inicia la interfaz gráfica de SUMO
- Carga la red y las rutas
- Comienza la simulación automáticamente
- Muestra información de los vehículos en tiempo real

### 3. Controles de la Simulación
- **Play/Pause**: Controla el inicio/pausa de la simulación
- **Velocidad**: Ajusta la velocidad de la simulación
- **Zoom**: Permite acercar/alejar la vista
- **Pan**: Permite mover la vista

## Personalización

### Modificación de la Red
Edita `red.netcfg` para cambiar:
- Tamaño de la cuadrícula
- Longitud de los bordes
- Configuración de conexiones

### Modificación de Rutas
Edita `rutas.rou.xml` para:
- Añadir más vehículos
- Cambiar las rutas
- Modificar parámetros de los vehículos

### Modificación del Control
Edita `control_traci.py` para:
- Cambiar la frecuencia de monitoreo
- Añadir lógica de control adicional
- Modificar el comportamiento de reinicio

## Consideraciones Técnicas

### Manejo de Bordes
- Los bordes normales son los principales caminos
- Los bordes internos (prefijo ':') manejan las conexiones
- Las rutas deben usar bordes conectados correctamente

### Control de Tiempo
- La simulación usa pasos discretos
- El tiempo entre pasos es configurable
- La velocidad de la simulación es ajustable

### Monitoreo
- Información de posición, velocidad y borde actual
- Actualización cada 5 pasos de simulación
- Logging de eventos importantes

## Solución de Problemas

### Problemas Comunes
1. **Vehículos no visibles**
   - Verificar que los bordes en la ruta están conectados
   - Asegurar que los vehículos tienen rutas válidas

2. **Errores de conexión**
   - Verificar que SUMO está instalado correctamente
   - Asegurar que la ruta a SUMO está en el PATH

3. **Problemas de rendimiento**
   - Ajustar el tiempo entre pasos
   - Reducir la frecuencia de monitoreo

## Contribuciones
Las contribuciones son bienvenidas. Por favor, sigue estas pautas:
1. Fork el repositorio
2. Crea una rama para tu feature
3. Envía un pull request

## Licencia
Este proyecto está bajo la licencia MIT. Ver el archivo LICENSE para más detalles. 