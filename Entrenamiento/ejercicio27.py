estudiantes = []

cantidad = int(input("Ingrese la cantidad de estudiantes: "))

for i in range(cantidad): 
    #Pedir nombres al estudiante
    nombre = input(f"Ingrese el nombre del estudiante { i+1}: ")
    notas = [ ]
    for j in range(3):
        #Ingresar las notas de los estudiantes 
        nota = float(input(f"Nota {j+1}: ")) 