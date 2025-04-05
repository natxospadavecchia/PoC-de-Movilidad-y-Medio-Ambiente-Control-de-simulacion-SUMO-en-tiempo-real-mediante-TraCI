import traci
import os
import sys
import time

def iniciar_simulacion():
    # Ruta al archivo de configuración SUMO
    sumo_cfg = "simulacion.sumocfg"

    # Comando para iniciar SUMO en modo GUI
    sumo_cmd = ["sumo-gui", "-c", sumo_cfg, "--start", "--quit-on-end=false"]

    # Inicia TraCI con el comando definido
    traci.start(sumo_cmd)
    print("Simulación SUMO iniciada vía TraCI.")
    
    # Pausa inicial para que puedas ver la ventana
    print("Esperando 5 segundos para que puedas ver la ventana...")
    time.sleep(5)

    # Verificar que la red se ha cargado correctamente
    edges = traci.edge.getIDList()
    print(f"Red cargada con {len(edges)} bordes totales.")
    
    # Mostrar las rutas disponibles
    routes = traci.route.getIDList()
    print(f"Rutas disponibles: {routes}")
    
    # Mostrar información de la ruta 'ruta_simple'
    if "ruta_simple" in routes:
        route_edges = traci.route.getEdges("ruta_simple")
        print(f"Ruta 'ruta_simple' usa los bordes: {route_edges}")

def bucle_simulacion():
    while True:  # Bucle infinito para mantener la simulación activa
        paso = 0
        try:
            print("\nIniciando nueva iteración de la simulación...")
            while traci.simulation.getMinExpectedNumber() > 0:
                # Mostrar información de los vehículos cada 5 pasos
                if paso % 5 == 0:
                    vehicles = traci.vehicle.getIDList()
                    print(f"\nPaso {paso}: {len(vehicles)} vehículos en la simulación")
                    for veh_id in vehicles:
                        pos = traci.vehicle.getPosition(veh_id)
                        edge = traci.vehicle.getRoadID(veh_id)
                        speed = traci.vehicle.getSpeed(veh_id)
                        print(f"  Vehículo {veh_id}:")
                        print(f"    - Posición: {pos}")
                        print(f"    - Borde actual: {edge}")
                        print(f"    - Velocidad: {speed:.2f} m/s")

                traci.simulationStep()
                paso += 1
                # Aumentar el retraso entre pasos para ver mejor el movimiento
                time.sleep(0.5)
            
            # Cuando termina la simulación, la reiniciamos
            print("\nSimulación completada, reiniciando...")
            traci.load(["-c", "simulacion.sumocfg"])  # Recarga la configuración
            time.sleep(2)  # Pequeña pausa entre iteraciones
            
        except Exception as e:
            print("Error en la simulación:", e)
            print("Detalles del error:", str(e))
            break  # Si hay un error, salimos del bucle
    
    traci.close()
    print("Simulación finalizada.")

if __name__ == "__main__":
    iniciar_simulacion()
    bucle_simulacion()