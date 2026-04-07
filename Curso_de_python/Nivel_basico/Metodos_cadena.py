nombre_curso = "python"
nueva_cadena= nombre_curso.upper() #convertir una cadena en mayusculas 
nueva_cadena_min = nombre_curso.lower() #convertir a minusculas
#print(nueva_cadena)
#print(nueva_cadena_min)

mensaje = " Hola mundo "
nueva_cadena_sin = mensaje.strip()
print(nueva_cadena_sin)

mensaje_bien = "Hola mundo desde Python"
#cadena_buscar = mensaje_bien.find("Python")
print()

cadena_buscar1 = mensaje_bien.index("Python")
#print(cadena_buscar1)

mensaje_bien = "Hola mundo desde Python"
cadena_reemplazar = mensaje_bien.replace("Python", "DJango")
#print(cadena_reemplazar)

palabras = ["manzana", "Banana", "cereza"]

resultado=' , '.join(palabras)
#print(resultado)