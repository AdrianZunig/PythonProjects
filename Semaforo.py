import time # Simula el tiempo de espera entre cambios de estado
"""
Simula el cambio de estado del semáforo
"""
def semaforo(): # Función que simula el semáforo
    # bucle infinito(true), para simular el semáforo
    while True: 
        print("\n🔴 ROJO - Detente")
        time.sleep(4) # Espera 4 segundos en rojo

        print("🟡 AMARILLO - Precaución")
        time.sleep(2) # Espera 2 segundos en amarillo

        print("🟢 VERDE - Avanza")    
        time.sleep(4) # Espera 4 segundos en verde
semaforo() # Llama a la función 
