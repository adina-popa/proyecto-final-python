# EJERCICIO 1
# Crea un programa que solicite al usuario introducir un número entero positivo y 
# lo almacene en una variable. 
#Si lo introducido por el usuario:
#a) No es un número se deberá mostrar por pantalla un mensaje de error
#que le informe de que lo introducido no es un número, similar a: “El dato introducido no es número. Por favor, vuelva a intentarlo”. Tras ello, el
#programa deberá volver a solicitarle que introduzca un número entero
#positivo.
#b) No es un número entero se deberá mostrar por pantalla un mensaje de
#error que le informe de que lo introducido no es un número entero,
#similar a: “No ha introducido un número entero. Por favor, vuelva a intentarlo”. Tras ello, el programa deberá volver a solicitarle que introduzca un número entero positivo.
#c) No es un número entero positivo se deberá mostrar por pantalla un mensaje de error que le informe de que lo introducido no es un número entero positivo, similar a: “No ha introducido un número entero positivo.
#Por favor, vuelva a intentarlo”. Tras ello, el programa deberá volver a
#solicitarle que introduzca un número entero positivo.
#d) Es un número entero positivo deberás crear una función que lo reciba y
#compruebe si el número es primo o no. La función deberá devolver un
#mensaje que informe al usuario del resultado.

# Función para comprobar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

while True:
    dato = input("Introduce un número entero positivo: ")

    # Le indico al usuario que no ha introducido un número
    try:
        numero = float(dato)
    except:
        print("El dato introducido no es un número. Por favor, vuelva a intentarlo.")
        continue

    # Le indico al usuario que no ha introducido un número entero
    if not numero.is_integer():
        print("No ha introducido un número entero. Por favor, vuelva a intentarlo.")
        continue

    numero = int(numero)

    # Le indico al usuario que no ha introducido un número positivo
    if numero <= 0:
        print("No ha introducido un número entero positivo. Por favor, vuelva a intentarlo.")
        continue

    # Compruebo si el número es primo
    if es_primo(numero):
        print("El número es primo.")
    else:
        print("El número no es primo.")

    break

    