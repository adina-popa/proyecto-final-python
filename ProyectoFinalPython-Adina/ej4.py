# EJERCICIO 4
# Tras la creación de las dos clases, deberás crear un programa que:
#◼ Solicite al usuario los datos necesarios para crear un objeto de la clase Italiano. Recuerda que el idioma y la nacionalidad ya tienen valores
#definidos por lo que no se le deberían preguntar al usuario.
#◼ El programa deberá contener un método que reciba los datos introducidos por el usuario para crear con ellos un objeto/instancia de la
#clase italiano.
#◼ Por último, se deberá mostrar por pantalla el mensaje del saludo,
#llamando a la función saludar desde el objeto de la clase ITALIANO
#que se ha creado.

# Creo la clase padre Persona
class Persona:
    def __init__(self, nombre, apellido, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad

    # Sobreescribo el método saludar
    def saludar(self):
        print(f"Hola, soy {self.nombre} {self.apellido}.")

# Creo la clase que hereda de Persona
class Italiano(Persona):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido, "italiana")
        self.idioma = "italiano"

    def saludar(self):
        print(f"Buongiorno! Mi nombre es {self.nombre} {self.apellido}, "
              f"soy de nacionalidad {self.nacionalidad} y mi idioma principal es {self.idioma}.")

# Pido nombre y apellido al usuario
nombre = input("Introduce el nombre: ")
apellido = input("Introduce el apellido: ")

# Creo el objeto
persona = Italiano(nombre, apellido)

# Muestro el saludo
persona.saludar()