# EJERCICIO 2
# Con los datos mostrados en la tabla anterior crea un programa que: 
# ◼ Muestre por pantalla cuántos alumnos suspendieron cada asignatu
# ra. Ejemplo: Inglés se ha suspendido por 3 alumnos 
# ◼ Realiza la media de las notas de cada alumno y muéstralas por pan
# talla. Ejemplo: El alumno1 ha tenido una nota media de 7.25 
# ◼ Muestra por pantalla los nombres de los alumnos que han aprobado 
# el curso, sabiendo que para aprobar necesitan obtener una nota media igual o superior a 5. Ejemplo: Los alumnos que han aprobado 
# el curso son: Alumno1, ….

# Creo un diccionario con los alumnos y sus notas
notas = {
    "Alumno1": [8, 8, 9, 4],
    "Alumno2": [7, 6, 7, 2],
    "Alumno3": [10, 7, 8, 9],
    "Alumno4": [4, 4, 3, 2],
    "Alumno5": [9, 8, 9, 6]
}

# Lista de las asignaturas (por orden de las notas)
asignaturas = ["Latín", "Castellano", "Francés", "Inglés"]

# Muestro cuántos alumnos han suspendido cada asignatura
for i in range(len(asignaturas)):
    suspensos = 0

    # Recorro cada alumno
    for alumno in notas:
        # Si la nota es menor que 5: suspenso
        if notas[alumno][i] < 5:
            suspensos += 1

    print(f"{asignaturas[i]} se ha suspendido por {suspensos} alumnos")

# Calculo la media de cada alumno
aprobados = []  # Lista para guardar los alumnos que aprueban

for alumno in notas:
    # Calculo la media
    media = sum(notas[alumno]) / len(notas[alumno])

    # Muestro la media
    print(f"El {alumno} ha tenido una nota media de {media}")

    # Si aprueba (media >= 5), lo guardo
    if media >= 5:
        aprobados.append(alumno)

# Muestro los nombres de los alumnos aprobados
print("Los alumnos que han aprobado el curso son:", ", ".join(aprobados))