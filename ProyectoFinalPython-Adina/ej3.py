# EJERCICIO 3
# Crea un programa que simule una partida de dados entre dos amigos, siendo 
# las normas del juego las siguientes: 
# Cada jugador lanzará dos dados de 6 simultáneamente y apuntará los resulta
# dos obtenidos. Si alguno de los números obtenidos por los jugadores coincide, 
# el Jugador1 ganará la ronda. Por el contrario, si ninguno de los números coinci
# de ganará el Jugador2. 

import random

# Función para lanzar los dados
def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)

while True:
    puntos_jugador1 = 0
    puntos_jugador2 = 0

    # Bucle hasta que el jugador 1 o 2 gane 3 rondas
    while puntos_jugador1 < 3 and puntos_jugador2 < 3:
        j1_d1, j1_d2 = lanzar_dados()
        j2_d1, j2_d2 = lanzar_dados()

        print(f"Jugador1 ha obtenido: {j1_d1} y {j1_d2}")
        print(f"Jugador2 ha obtenido: {j2_d1} y {j2_d2}")

        # Si hay números repetidos entre los 4 dados gana el jugador 1
        lista = [j1_d1, j1_d2, j2_d1, j2_d2]

        if len(lista) != len(set(lista)):
            print("Gana la ronda: Jugador1")
            puntos_jugador1 += 1
        else:
            print("Gana la ronda: Jugador2")
            puntos_jugador2 += 1

        # Muestro el marcador
        print(f"Marcador -> Jugador1: {puntos_jugador1} | Jugador2: {puntos_jugador2}")

    # Muestro el ganador
    if puntos_jugador1 == 3:
        print("¡Enhorabuena! Jugador1 ha ganado la partida.")
    else:
        print("¡Enhorabuena! Jugador2 ha ganado la partida.")

    # Indico si quiere jugar otra vez
    while True:
        respuesta = input("¿Desea jugar otra partida? (SI/NO): ").upper()
        if respuesta == "SI":
            break
        elif respuesta == "NO":
            print("Fin del programa.")
            exit()
        else:
            print("No hemos entendido su respuesta. Repítala, por favor.")