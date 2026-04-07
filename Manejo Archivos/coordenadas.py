# entrada = [4, 5, 2, 4, 2, 8, 5] 

# sin_duplicados = [] 

# for num in entrada: 
#     if num not in sin_duplicados: 
#         sin_duplicados.append(num)

# print(sin_duplicados)

# estudiantes = ["ana", "Luis", "maria", "Luis", "ANA", "Carlos", "carlos"]

# nombres_unicos = [ ]

# for nombre in estudiantes: 
#     nombre_formateado = nombre.capitalize()

#     if nombre_formateado not in nombres_unicos: 
#         nombres_unicos.append(nombre_formateado)
    
# nombres_unicos.sort()

# print(nombres_unicos)

# numeros = [4, 5, 2, 4, 2, 8, 5, 10, 8, 12]
# pares_unicos = [ ]

# for num in numeros: 
#     if num % 2==0: 
#         if num not in pares_unicos: 
#             pares_unicos.append(num)

# ordenado = pares_unicos.sort()
# print(pares_unicos)


"""
Paso a paso de lo que tienes que hacer

Convierte todo el texto a minúsculas con .lower().

Recorre cada carácter del texto.

Si el carácter no es espacio, revisa si ya está en el diccionario:

Si sí, suma 1.

Si no, inicializa en 1.

Al final, devuelve el diccionario con los resultados.
"""
# def contar_letras(texto): 
#     texto = texto.lower() 
#     conteo = {}

#     for letra in texto: 
#         if letra != " ":
#             if letra in conteo: 
#                 conteo[letra] += 1
#             else:
#                 conteo[letra] = 1
#     return conteo 

# texto = "Hola mundo"

# resultado = contar_letras(texto) 
# print(resultado)

# def contar_vocales(texto):
#     texto = texto.lower()
#     vocales = {}

#     for letra in texto:
#         if letra in "aeiou":
#             if letra in vocales: 
#                 vocales[letra] += 1
#             else: 
#                 vocales[letra] = 1
#     return vocales

# texto = "Programar es divertido" 
# resultado = contar_vocales(texto)
# print(resultado)
            
# def contar_palabras(texto):
#     texto = texto.lower() 
#     conteo = {}

#     for signo in [",", ".", "!", "?", ";", ":", "¿", "¡"]: 
#         texto = texto.replace(signo,"")

#     texto = texto.split()

#     for palabra in texto: 
#         if palabra in conteo: 
#             conteo[palabra] += 1
#         else: 
#             conteo[palabra] = 1 
#     return conteo

# texto = "Python es divertido, y aprender Python es genial"

# print(contar_palabras(texto))

# def analizar_pares(lista): 
#     pares = []
#     for num in lista:
#         if num % 2==0: 
#             pares.append(num)
    
#     suma_num = sum(pares)

#     resultado = {
#         "numeros" : pares,
#         "suma" : suma_num,
#     }
#     return resultado

# numeros = [2, 5, 8, 3, 10, 7]

# print(analizar_pares(numeros))

# estudiantes = {
#     "Ana": [90, 85, 88],
#     "Luis": [70, 75, 72],
#     "María": [95, 98, 100]
# }

# for nombres, notas in estudiantes.items(): 
#     promedio = sum(notas)/len(notas)
    
#     if promedio == 7.00: 
#         aprobado = print("Aprobado")
#     else: 
#         Reprobado = print("Reprobado.")

    
#     print(f"{nombres} tiene un promedio de: {promedio:.2f}")

estudiantes = [] 

while True:
    try: 
        print("Ingrese el nombre del estudiante, si no desea continuar ponga (Salir)")
        nombre = input("Ingrese el nombre del estudiante: ")
        nombre = nombre.lower()
        if nombre == "salir":
            print("--El programa se cerró--")
            break

        notas = {}
        notas["matematica"] = int(input("Ingrese la nota de matemticas: "))
        notas["Ingles"] = int(input("Ingrese la nota de Ingles: "))
        notas["ciencias"] = int(input("Ingrese la nota de Ciencias: "))

        promedio = sum(notas)/len()

    except ValueError: 
        print("No se puede ingresar caracter en enteros.")
        break 
