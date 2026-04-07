#Metodo tradicional
cuadrados = []

# for x in range(10): 
#     elevado = x**2 
#     cuadrados.append(elevado)
# print(cuadrados)

#Comprension de listas
# cuadrados = [ x**2 for x in range(10)]



# comprension de listas
# numeros = [1,2,3,4,5,6,7,8,9,10]
# pares = [x for x in numeros if x % 2==0]

# metodo tradicional 
# numeros1 = [1,2,3,4,5,6,7,8,9,10]
# pares = []
# for i in numeros1: 
#     if i % 2==0:
#         pares.append(i)
# print(pares)
    

# comprension de listras
palabras = ["Python", "Django", "Flash"]
contar_palabras = [len(palabra) for palabra in palabras ]


#metodo tradicional 
palabras = ["Python", "Django", "Flash"]
contar_palabras = []

for i in palabras:
    contar_palabras.append(len(i))
print(contar_palabras)

    
