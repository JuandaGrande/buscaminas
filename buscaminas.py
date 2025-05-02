import random
import time
import pandas as pd


def generar_tablero(tamaño):

    #Definir la cantidad de minas
    cant_minas=0
    if tamaño == 6:
            cant_minas = 4
    elif tamaño == 8:
            cant_minas = 9
    else:
            cant_minas = 15

    # Crear el tablero vacío
    tablero = [[0 for i in range(tamaño)] for i in range(tamaño)]

    #Generar posiciones para las minas
    posiciones = random.sample(range(tamaño*tamaño), cant_minas)
    print(posiciones)

    for pos in posiciones:
        fila = pos//tamaño
        col = pos % tamaño
        tablero[fila][col] = "M"

    return tablero

tablero=generar_tablero(6)
for fila in tablero:
      print(fila)