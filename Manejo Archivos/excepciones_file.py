def leer_archivo():
    try:
        archivo = open("C:/Users/Paul/OneDrive/Desktop/Progrmar/ventas.txt","r")
        contenido = archivo.read()
        print(contenido) 
    except FileNotFoundError:
        print("---El archivo no se a encontrado---")
        archivo.close()
    finally:
        print("El archivo se a cerrado correctamente.") 
# leer_archivo()

def leer_archivo_relativo():
    try:
        archivo = open("C:/Users/Paul/OneDrive/Desktop/Progrmar/ventas.txt", "r")
        contenido = archivo.read()
        print(contenido)
    except FileNotFoundError: 
        print("el archivo no se a encontrado---")
        archivo.close()
    finally:
        print("El archivo se a cerrado exitosamente...")

leer_archivo_relativo()