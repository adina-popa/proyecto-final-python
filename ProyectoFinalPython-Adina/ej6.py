# EJERCICIO 6
# Para este programa deberás crear una agenda en la que un usuario pueda almacenar sus contactos. 
# Creo un diccionario vacío para guardar los contactos.

agenda = {}

# Creo un bucle while para poder introducir los contactos
while True:
    nombre = input("Introduce el nombre: ")

    # Compruebo si el nombre ya existe
    if nombre in agenda:
        print("El nombre ya existe. Por favor, vuelva a intentarlo.")
        continue

    telefono = input("Introduce el número de teléfono: ")

    # Guardo el contacto en la agenda
    agenda[nombre] = telefono

    # Pregunto al usuario si quiere continuar o salir
    pregunta = input("¿Desea continuar o salir del programa? (S/N): ")
    if pregunta.upper() == "N":
        break

# Muestro como quedaría la agenda con los contactos
print("AGENDA DE CONTACTOS:")
for nombre in agenda:
    print(nombre, ":", agenda[nombre])