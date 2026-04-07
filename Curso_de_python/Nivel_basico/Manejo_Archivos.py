"""
"r" : modo de lectura por defecto. el archivo debe existir 
"w" : modo de escritura. Crea un archivo nuevo o trunca el archivo existente 
"a" : Modo de anexado. Crea un archivo nuevo o agrega datos al final del archivo existente
"b" :Modo binario. se puede combinar con los otros metodo para leer numeros binarios
"x" :Modo exclusivo. crea un nuevo archivo pero fallara si el archivo ya existe 
"""
#with open('Curso_de_python/Nivel_basico/infomacion.txt','r', encoding= 'utf-8') as file: 
#    contenido = file.read()
#    print(contenido)

with open('Curso_de_python/Nivel_basico/Nueva_Informacion.txt', 'w', encoding= 'utf-8') as file: 
    file.write("Primero linea del texto.\n")
    file.write("Segunda linea del texto.\n")
