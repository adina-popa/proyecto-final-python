# EJERCICIO 5
#Para este programa deberás definir una tupla compuesta por 15 números enteros positivos aleatorios entre 0 y 100, estos números serán los ganadores del
#último sorteo de la lotería.

import random

# Tupla con los números ganadores (15 números enteros positivos)
numeros = tuple(random.randint(0, 100) for _ in range(15))

def pedir_numero():
    while True:
        dato = input("Introduce un número entero positivo: ")

        # Le indico al usuario que no ha introducido un número
        try:
            numero = float(dato)
        except:
            print("El dato introducido no es un número. Por favor, vuelva a intentarlo.")
            continue
        
        # Le indico al usuario que el número introducido no es entero
        if not numero.is_integer():
            print("No ha introducido un número entero. Por favor, vuelva a intentarlo.")
            continue

        numero = int(numero)

        # Le indico al usuario que el número introducido no es entero positivo
        if numero < 0:
            print("No ha introducido un número entero positivo. Por favor, vuelva a intentarlo.")
            continue

        return numero

while True:
    numero_usuario = pedir_numero()

    # Muestro los datos
    print("Números ganadores:", numeros)
    print("Número más pequeño:", min(numeros))
    print("Número más grande:", max(numeros))

    # Cuento el número de repeticiones
    veces = numeros.count(numero_usuario)

    if veces > 0:
        premio = 15 + (veces - 1) * 5

        if veces == 1:
            print(f"¡Felicidades! Su número {numero_usuario} se encuentra dentro de la lista de ganadores. Ha ganado un total de {premio}€")
        else:
            print(f"¡Felicidades! Su número {numero_usuario} se encuentra dentro de la lista de ganadores y se ha repetido {veces} veces. Ha ganado un total de {premio}€")
        break
    else:
        # Pregunto al usuario si quiere volver a intentarlo
        while True:
            respuesta = input("Lo sentimos. Su número no ha resultado premiado. ¿Desea volver a intentarlo? (SI/NO): ").upper()
            if respuesta == "SI":
                break
            elif respuesta == "NO":
                exit()
            else:
                print("No hemos logrado entender su respuesta. Repítala, por favor.")