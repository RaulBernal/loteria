from datetime import datetime
import random

from participantes import listado

def guardar_en_fichero(lista):
    # Calcular el número de elementos
    total_elementos = len(lista)
    
    # Generar número aleatorio entre el mínimo y el máximo de "numero"
    numero_aleatorio = random.randint(1, total_elementos)
    
    # Encontrar el elemento correspondiente en la lista
    elemento_seleccionado = next((item for item in lista if item["numero"] == numero_aleatorio), None)
    
    # Generar el nombre del fichero con la fecha y hora actuales
    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_fichero = f"{fecha_hora_actual}_Sorteo.txt"
    
    # Guardar el resultado en el fichero
    with open(nombre_fichero, 'w') as fichero:
        if elemento_seleccionado:
            contenido = f'Número aleatorio: {numero_aleatorio}, Address: {elemento_seleccionado["address"]}'
            print(contenido)  # Imprimir por pantalla
            fichero.write(contenido)  # Escribir en el fichero
        else:
            print("Elemento no encontrado.")

# Llamar a la función
guardar_en_fichero(listado)
