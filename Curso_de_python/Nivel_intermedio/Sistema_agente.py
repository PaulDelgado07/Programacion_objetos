print("Sistema de gestion de estudiantes. ")
print("-----------------------------------")

estudiantes = []
while True:
    # Menú de opciones
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Calcular promedio general")
    print("4. Buscar estudiante")
    print("5. salir")


    numero = int(input("Ingrese numero que desea navegar: "))
    if numero == 1:
        nombre = input("Ingrese el nombre del estudiante: "),#Ingreso el nombre
        nota = (input("Ingrese la nota del estuante ")) #Ingresa la nota

        estudiante = {
            "Nombre": nombre,
            "Nota": nota
        }
        estudiantes.append(estudiante)
        print("Estudiante agregado.")
    elif numero == 2:
        for e in estudiantes:
            print(f"Nombre:{str(e["Nombre"])}")
    elif numero == 3:
        pass 
    elif numero == 4:
        pass 
    elif numero == 5:
        print("--cerrando programa--")
        break 