#extraer archivos .txt 
def leer_archivo_txt(archivo_txt):
    with open("informacion.txt") as file:
        contenido = file.read()
        print(contenido)

leer_archivo_txt()